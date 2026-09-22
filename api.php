<?php
/**
 * api.php — puente entre el widget de chat de MedQuizPro y la API de Google Gemini.
 *
 * Diseño: el nombre del modelo NO se da por supuesto.
 * Google retira modelos y renombra identificadores, y por eso una constante fija
 * acaba devolviendo 404. Aquí el flujo es:
 *
 *   1. Se pregunta a Google qué modelos admite esta clave (endpoint ListModels).
 *   2. Se elige el primero de MODELOS_PREFERIDOS que exista de verdad.
 *   3. La elección se guarda en caché unas horas para no repetir la consulta.
 *   4. Si aun así una petición devuelve 404, se descarta la caché, se vuelve a
 *      resolver el modelo y se reintenta una vez.
 *
 * La llave se lee de config.php o de la variable de entorno GEMINI_API_KEY.
 * Nunca llega al navegador.
 */

declare(strict_types=1);

/* ====================== AJUSTES ====================== */

/** Orden de preferencia. El primero que exista para tu clave es el que se usa. */
const MODELOS_PREFERIDOS = [
    'gemini-3.0-flash',
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-flash-latest',
];

/** Versiones de la API que se prueban, en este orden. */
const VERSIONES_API = ['v1beta', 'v1'];

const MAX_CARACTERES      = 1500;  // largo máximo de la pregunta
const MAX_HISTORIAL_TURNOS = 8;    // turnos de conversación que se reenvían
const LIMITE_POR_MINUTO   = 12;    // peticiones por IP y por minuto
const TIMEOUT_SEGUNDOS    = 45;
const CACHE_MODELO_SEGUNDOS = 21600; // 6 horas

/** true = el mensaje exacto de Google viaja al navegador (útil mientras se depura). */
const DETALLE_ERRORES = true;

const BASE_URL = 'https://generativelanguage.googleapis.com/';

/* ====================== UTILIDADES ====================== */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

/** Devuelve una respuesta JSON y termina. */
function responder(int $codigo, array $cuerpo): void
{
    http_response_code($codigo);
    echo json_encode($cuerpo, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

/**
 * Petición HTTP con cURL.
 *
 * @return array{codigo:int, cuerpo:array|null, crudo:string, error:string}
 */
function peticion(string $url, ?array $payload = null): array
{
    $ch = curl_init($url);
    $opciones = [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => TIMEOUT_SEGUNDOS,
        CURLOPT_CONNECTTIMEOUT => 10,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2,
        CURLOPT_HTTPHEADER     => ['Content-Type: application/json'],
    ];
    if ($payload !== null) {
        $opciones[CURLOPT_POST]       = true;
        $opciones[CURLOPT_POSTFIELDS] = json_encode($payload, JSON_UNESCAPED_UNICODE);
    }
    curl_setopt_array($ch, $opciones);

    $crudo  = curl_exec($ch);
    $codigo = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $error  = curl_error($ch);
    curl_close($ch);

    if ($crudo === false) {
        return ['codigo' => 0, 'cuerpo' => null, 'crudo' => '', 'error' => $error];
    }

    $cuerpo = json_decode((string) $crudo, true);
    return [
        'codigo' => $codigo,
        'cuerpo' => is_array($cuerpo) ? $cuerpo : null,
        'crudo'  => (string) $crudo,
        'error'  => '',
    ];
}

/** Saca el mensaje y el estado que devolvió Google, si los hay. */
function errorDeGoogle(?array $cuerpo): array
{
    return [
        'mensaje' => (string) ($cuerpo['error']['message'] ?? ''),
        'estado'  => (string) ($cuerpo['error']['status'] ?? ''),
        'codigo'  => (int) ($cuerpo['error']['code'] ?? 0),
    ];
}

/* ====================== ENCAMINADO ====================== */

$esDiagnostico = (($_GET['accion'] ?? '') === 'diagnostico');

if (!$esDiagnostico && ($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    responder(405, ['error' => 'Este endpoint solo admite POST.']);
}

/* ====================== LA LLAVE ====================== */

$apiKey = (string) (getenv('GEMINI_API_KEY') ?: '');
$modeloForzado = '';

if (is_readable(__DIR__ . '/config.php')) {
    $config = require __DIR__ . '/config.php';
    if (is_array($config)) {
        if ($apiKey === '') {
            $apiKey = trim((string) ($config['gemini_api_key'] ?? ''));
        }
        $modeloForzado = trim((string) ($config['gemini_model'] ?? ''));
        $tokenDiagnostico = trim((string) ($config['diagnostico_token'] ?? ''));
    }
}
$tokenDiagnostico = $tokenDiagnostico ?? '';

if ($apiKey === '') {
    error_log('api.php: falta la llave de Gemini (config.php o GEMINI_API_KEY).');
    responder(500, [
        'error'  => 'El tutor todavía no está configurado en el servidor: falta la llave de Gemini.',
        'origen' => 'configuracion',
    ]);
}

$claveUrl = urlencode($apiKey);

/* ====================== RESOLUCIÓN DEL MODELO ====================== */

$archivoCache = sys_get_temp_dir() . '/medquizpro_modelo_' . sha1($apiKey) . '.json';

/** Lista los modelos que la clave puede usar en una versión de la API. */
function listarModelos(string $version, string $claveUrl): array
{
    $modelos = [];
    $token = '';
    for ($pagina = 0; $pagina < 3; $pagina++) {
        $url = BASE_URL . $version . '/models?pageSize=200&key=' . $claveUrl
             . ($token !== '' ? '&pageToken=' . urlencode($token) : '');
        $r = peticion($url);
        if ($r['codigo'] !== 200 || !is_array($r['cuerpo'])) {
            return ['modelos' => $modelos, 'codigo' => $r['codigo'], 'cuerpo' => $r['cuerpo'], 'error' => $r['error']];
        }
        foreach (($r['cuerpo']['models'] ?? []) as $m) {
            $metodos = $m['supportedGenerationMethods'] ?? $m['supportedActions'] ?? [];
            if (!in_array('generateContent', (array) $metodos, true)) {
                continue;
            }
            $modelos[] = preg_replace('#^models/#', '', (string) ($m['name'] ?? ''));
        }
        $token = (string) ($r['cuerpo']['nextPageToken'] ?? '');
        if ($token === '') {
            break;
        }
    }
    return ['modelos' => array_values(array_filter($modelos)), 'codigo' => 200, 'cuerpo' => null, 'error' => ''];
}

/** Elige el mejor modelo disponible de una lista real. */
function elegirModelo(array $disponibles): string
{
    if (!$disponibles) {
        return '';
    }
    // 1. Coincidencia exacta con la lista de preferencias.
    foreach (MODELOS_PREFERIDOS as $preferido) {
        if (in_array($preferido, $disponibles, true)) {
            return $preferido;
        }
    }
    // 2. Variante con sufijo: gemini-3.0-flash-001, -preview, etc. Gana el nombre más corto.
    foreach (MODELOS_PREFERIDOS as $preferido) {
        $candidatos = array_values(array_filter(
            $disponibles,
            static fn(string $m): bool => str_starts_with($m, $preferido)
        ));
        if ($candidatos) {
            usort($candidatos, static fn(string $a, string $b): int => strlen($a) <=> strlen($b));
            return $candidatos[0];
        }
    }
    // 3. Cualquier Gemini "flash" (rápido y barato), si no, cualquier Gemini.
    foreach (['flash', ''] as $pista) {
        $candidatos = array_values(array_filter(
            $disponibles,
            static fn(string $m): bool => str_starts_with($m, 'gemini-')
                && ($pista === '' || str_contains($m, $pista))
                && !str_contains($m, 'embedding')
                && !str_contains($m, 'vision')
        ));
        if ($candidatos) {
            usort($candidatos, static fn(string $a, string $b): int => strlen($a) <=> strlen($b));
            return $candidatos[0];
        }
    }
    return $disponibles[0];
}

/**
 * Devuelve ['modelo' => ..., 'version' => ...] o lanza un error ya formateado.
 *
 * @return array{modelo:string, version:string, disponibles:array}
 */
function resolverModelo(string $claveUrl, string $modeloForzado): array
{
    if ($modeloForzado !== '') {
        // El dueño del sitio fijó un modelo a mano: se respeta en la primera versión de API.
        return ['modelo' => $modeloForzado, 'version' => VERSIONES_API[0], 'disponibles' => []];
    }

    $ultimo = ['codigo' => 0, 'cuerpo' => null, 'error' => ''];
    foreach (VERSIONES_API as $version) {
        $r = listarModelos($version, $claveUrl);
        if ($r['codigo'] === 200 && $r['modelos']) {
            $elegido = elegirModelo($r['modelos']);
            if ($elegido !== '') {
                return ['modelo' => $elegido, 'version' => $version, 'disponibles' => $r['modelos']];
            }
        }
        $ultimo = $r;
    }

    $g = errorDeGoogle($ultimo['cuerpo'] ?? null);
    error_log('api.php: no se pudo listar modelos — HTTP ' . $ultimo['codigo'] . ' ' . $g['mensaje'] . ' ' . ($ultimo['error'] ?? ''));

    $mensaje = 'No se pudo determinar qué modelo de Gemini admite esta clave.';
    if (DETALLE_ERRORES && $g['mensaje'] !== '') {
        $mensaje .= ' Google respondió: ' . $g['mensaje'];
    } elseif (DETALLE_ERRORES && ($ultimo['error'] ?? '') !== '') {
        $mensaje .= ' Fallo de red: ' . $ultimo['error'];
    }

    responder($ultimo['codigo'] >= 400 ? $ultimo['codigo'] : 502, [
        'error'         => $mensaje,
        'origen'        => 'listado_de_modelos',
        'google_codigo' => $g['codigo'] ?: (int) $ultimo['codigo'],
        'google_estado' => $g['estado'],
    ]);
}

/** Lee la elección guardada, si sigue vigente. */
function cacheLeer(string $archivo): ?array
{
    if (!is_readable($archivo)) {
        return null;
    }
    $datos = json_decode((string) file_get_contents($archivo), true);
    if (!is_array($datos) || empty($datos['modelo']) || empty($datos['version'])) {
        return null;
    }
    if ((int) ($datos['ts'] ?? 0) < time() - CACHE_MODELO_SEGUNDOS) {
        return null;
    }
    return ['modelo' => (string) $datos['modelo'], 'version' => (string) $datos['version']];
}

function cacheGuardar(string $archivo, string $modelo, string $version): void
{
    @file_put_contents($archivo, json_encode([
        'modelo'  => $modelo,
        'version' => $version,
        'ts'      => time(),
    ]), LOCK_EX);
}

/* ====================== MODO DIAGNÓSTICO ====================== */
/* GET api.php?accion=diagnostico&token=...  →  qué modelos ve tu clave.
   Solo funciona si 'diagnostico_token' está puesto en config.php. */

if ($esDiagnostico) {
    if ($tokenDiagnostico === '' || !hash_equals($tokenDiagnostico, (string) ($_GET['token'] ?? ''))) {
        responder(403, ['error' => 'Diagnóstico no disponible.']);
    }
    $informe = ['php' => PHP_VERSION, 'curl' => function_exists('curl_init'), 'versiones' => []];
    foreach (VERSIONES_API as $version) {
        $r = listarModelos($version, $claveUrl);
        $g = errorDeGoogle($r['cuerpo'] ?? null);
        $informe['versiones'][$version] = [
            'http'     => $r['codigo'],
            'modelos'  => $r['modelos'],
            'elegido'  => $r['modelos'] ? elegirModelo($r['modelos']) : null,
            'error'    => $g['mensaje'] ?: ($r['error'] ?: null),
        ];
    }
    $informe['preferencias'] = MODELOS_PREFERIDOS;
    $informe['modelo_forzado'] = $modeloForzado ?: null;
    responder(200, $informe);
}

/* ====================== EL CHAT ====================== */

/* --- límite de uso por IP --- */
$ip = (string) ($_SERVER['REMOTE_ADDR'] ?? 'desconocida');
$archivoLimite = sys_get_temp_dir() . '/medquizpro_rl_' . sha1($ip) . '.json';
$ahora = time();
$marcas = [];
if (is_readable($archivoLimite)) {
    $previo = json_decode((string) file_get_contents($archivoLimite), true);
    if (is_array($previo)) {
        $marcas = array_values(array_filter($previo, static fn($t): bool => is_int($t) && $t > $ahora - 60));
    }
}
if (count($marcas) >= LIMITE_POR_MINUTO) {
    header('Retry-After: 60');
    responder(429, ['error' => 'Demasiadas preguntas seguidas. Espera un minuto y vuelve a intentarlo.']);
}
$marcas[] = $ahora;
@file_put_contents($archivoLimite, json_encode($marcas), LOCK_EX);

/* --- leer y validar la pregunta --- */
$entrada = json_decode((string) file_get_contents('php://input'), true);
if (!is_array($entrada)) {
    responder(400, ['error' => 'No se pudo leer la pregunta.']);
}

$mensaje = trim((string) ($entrada['mensaje'] ?? $entrada['message'] ?? ''));
if ($mensaje === '') {
    responder(400, ['error' => 'Escribe una pregunta antes de enviar.']);
}
if (mb_strlen($mensaje) > MAX_CARACTERES) {
    responder(400, ['error' => 'La pregunta es demasiado larga. Resúmela en ' . MAX_CARACTERES . ' caracteres o menos.']);
}

/* --- el papel del tutor --- */
$instruccion = <<<TXT
Eres el tutor de MedQuizPro, una plataforma peruana de preparación para el ENAM,
el Residentado Médico (RM) y los exámenes de EsSalud.

Cómo respondes:
- Siempre en español, con el registro de un docente de medicina que explica a un interno.
- Primero la respuesta directa; después el razonamiento que lleva a ella.
- Usas la terminología y las guías que se toman en los exámenes peruanos (MINSA, AIEPI,
  guías de práctica clínica nacionales) cuando vienen al caso.
- Ante un caso clínico de examen, explicas también por qué cada distractor es incorrecto.
- Si el dato depende de una guía que puede haber cambiado, o no lo sabes, lo dices.
- Alrededor de 250 palabras, salvo que te pidan más detalle.

Límite importante: esto es material de estudio. Si alguien te describe a un paciente real
o te pide una indicación para tratar a alguien ahora mismo, recuérdale que debe consultar
con un médico tratante y no le des una indicación de tratamiento individualizada.
TXT;

/* --- historial + pregunta actual --- */
$contents = [];
$historial = $entrada['historial'] ?? $entrada['history'] ?? [];
if (is_array($historial)) {
    foreach (array_slice($historial, -(MAX_HISTORIAL_TURNOS * 2)) as $turno) {
        if (!is_array($turno)) {
            continue;
        }
        $texto = trim((string) ($turno['texto'] ?? $turno['text'] ?? ''));
        if ($texto === '') {
            continue;
        }
        $rol = (string) ($turno['rol'] ?? $turno['role'] ?? 'usuario');
        $contents[] = [
            'role'  => in_array($rol, ['tutor', 'model', 'assistant'], true) ? 'model' : 'user',
            'parts' => [['text' => mb_substr($texto, 0, MAX_CARACTERES)]],
        ];
    }
}
$contents[] = ['role' => 'user', 'parts' => [['text' => $mensaje]]];

$payload = [
    'systemInstruction' => ['parts' => [['text' => $instruccion]]],
    'contents'          => $contents,
    'generationConfig'  => [
        'temperature'     => 0.4,
        'maxOutputTokens' => 800,
    ],
];

/* --- llamada, con un reintento si el modelo dejó de existir --- */
$eleccion = cacheLeer($archivoCache) ?? resolverModelo($claveUrl, $modeloForzado);
$respuesta = null;

for ($intento = 1; $intento <= 2; $intento++) {
    $url = BASE_URL . $eleccion['version'] . '/models/' . rawurlencode($eleccion['modelo'])
         . ':generateContent?key=' . $claveUrl;

    $respuesta = peticion($url, $payload);

    if ($respuesta['codigo'] === 200) {
        cacheGuardar($archivoCache, $eleccion['modelo'], $eleccion['version']);
        break;
    }

    $g = errorDeGoogle($respuesta['cuerpo']);
    $modeloRetirado = $respuesta['codigo'] === 404
        || $g['estado'] === 'NOT_FOUND'
        || stripos($g['mensaje'], 'no longer available') !== false
        || stripos($g['mensaje'], 'not found') !== false;

    if ($modeloRetirado && $intento === 1 && $modeloForzado === '') {
        // El modelo guardado ya no sirve: se descarta y se vuelve a preguntar a Google.
        error_log('api.php: modelo ' . $eleccion['modelo'] . ' rechazado (' . $g['mensaje'] . '). Resolviendo de nuevo.');
        @unlink($archivoCache);
        $eleccion = resolverModelo($claveUrl, '');
        continue;
    }
    break;
}

/* --- fallo --- */
if ($respuesta === null || $respuesta['codigo'] !== 200) {
    $g = errorDeGoogle($respuesta['cuerpo'] ?? null);
    $httpGoogle = (int) ($respuesta['codigo'] ?? 0);
    error_log('api.php: Gemini HTTP ' . $httpGoogle . ' [' . $eleccion['modelo'] . '/' . $eleccion['version'] . '] ' . $g['mensaje']);

    if ($httpGoogle === 0) {
        responder(502, [
            'error'  => 'No se pudo contactar con Google.' . (DETALLE_ERRORES && $respuesta['error'] !== '' ? ' ' . $respuesta['error'] : ''),
            'origen' => 'red',
            'modelo' => $eleccion['modelo'],
        ]);
    }

    $mensajeUsuario = DETALLE_ERRORES && $g['mensaje'] !== ''
        ? 'Google HTTP ' . $httpGoogle . ($g['estado'] !== '' ? ' (' . $g['estado'] . ')' : '') . ': ' . $g['mensaje']
        : 'El tutor no pudo responder ahora mismo. Inténtalo de nuevo.';

    responder($httpGoogle >= 400 && $httpGoogle < 600 ? $httpGoogle : 502, [
        'error'         => $mensajeUsuario,
        'origen'        => 'gemini',
        'google_codigo' => $g['codigo'] ?: $httpGoogle,
        'google_estado' => $g['estado'],
        'modelo'        => $eleccion['modelo'],
        'api_version'   => $eleccion['version'],
    ]);
}

/* --- éxito: extraer el texto --- */
$datos = $respuesta['cuerpo'] ?? [];
$candidato = $datos['candidates'][0] ?? null;

if ($candidato === null) {
    $motivo = (string) ($datos['promptFeedback']['blockReason'] ?? '');
    $texto = $motivo !== ''
        ? 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.'
        : '';
    if ($texto === '') {
        error_log('api.php: respuesta sin candidatos de ' . $eleccion['modelo']);
        responder(502, ['error' => 'El tutor no pudo responder ahora mismo. Inténtalo de nuevo.', 'origen' => 'gemini']);
    }
    responder(200, ['respuesta' => $texto, 'reply' => $texto, 'modelo' => $eleccion['modelo']]);
}

$texto = '';
foreach (($candidato['content']['parts'] ?? []) as $parte) {
    if (isset($parte['text'])) {
        $texto .= $parte['text'];
    }
}
$texto = trim($texto);

if ($texto === '') {
    $motivo = (string) ($candidato['finishReason'] ?? '');
    if ($motivo === 'SAFETY' || $motivo === 'PROHIBITED_CONTENT' || $motivo === 'BLOCKLIST') {
        $texto = 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.';
    } elseif ($motivo === 'MAX_TOKENS') {
        $texto = 'La respuesta salió demasiado larga y se cortó. Pregúntame por partes más pequeñas.';
    } else {
        error_log('api.php: respuesta vacía de ' . $eleccion['modelo'] . ' (finishReason: ' . $motivo . ')');
        responder(502, [
            'error'  => 'El tutor no pudo responder ahora mismo. Inténtalo de nuevo.',
            'origen' => 'gemini',
            'modelo' => $eleccion['modelo'],
        ]);
    }
}

responder(200, [
    'respuesta'   => $texto,
    'reply'       => $texto,
    'modelo'      => $eleccion['modelo'],
    'api_version' => $eleccion['version'],
]);
