<?php
/**
 * api.php — puente entre el chat de MedQuizPro y el modelo de inteligencia artificial.
 *
 * El navegador nunca ve la llave. El widget hace POST a este archivo con la pregunta
 * y el historial de la conversación; este archivo llama al proveedor de IA y devuelve
 * solo el texto de la respuesta.
 *
 * Configuración (variables de entorno, o config.php si el hosting no permite variables):
 *
 *   AI_API_KEY    la llave del proveedor            (obligatoria)
 *   AI_PROVIDER   gemini | openai | anthropic       (por defecto: gemini)
 *   AI_MODEL      nombre del modelo                 (opcional; en Gemini se autodetecta)
 *   AI_BASE_URL   solo para APIs compatibles con OpenAI (Groq, DeepSeek, OpenRouter…)
 *   AI_DEBUG      1 para ver el detalle técnico del error en la respuesta JSON
 *
 * Nada de esto llega al navegador: ante cualquier fallo el usuario recibe siempre
 * el mismo mensaje amable, y el detalle queda en el log de errores del servidor.
 */

declare(strict_types=1);

/* ====================== AJUSTES ====================== */

const MAX_CARACTERES        = 2000;   // largo máximo de un mensaje
const MAX_HISTORIAL_TURNOS  = 10;     // turnos de conversación que se reenvían como contexto
const TIMEOUT_SEGUNDOS      = 45;
const MAX_TOKENS_RESPUESTA  = 900;
const TEMPERATURA           = 0.4;
const CACHE_MODELO_SEGUNDOS = 21600;  // 6 horas (solo Gemini, que autodetecta el modelo)

/* Límite de uso por IP. Se pueden cambiar con AI_LIMITE_MINUTO y AI_LIMITE_DIA. */
const LIMITE_MINUTO_DEF = 10;
const LIMITE_DIA_DEF    = 150;

/** Lo único que ve el usuario cuando algo falla. */
const MENSAJE_GENERICO = 'Lo siento, no pude procesar tu mensaje. Inténtalo nuevamente.';

/** Gemini: orden de preferencia. El primero que exista para la llave es el que se usa. */
const MODELOS_PREFERIDOS = [
    'gemini-3.0-flash',
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-flash-latest',
];
const VERSIONES_API = ['v1beta', 'v1'];

const URL_GEMINI    = 'https://generativelanguage.googleapis.com/';
const URL_OPENAI    = 'https://api.openai.com/v1';
const URL_ANTHROPIC = 'https://api.anthropic.com/v1';

/** Modelo por defecto de cada proveedor. En Gemini, vacío = preguntarle a Google. */
const MODELO_POR_DEFECTO = [
    'gemini'    => '',
    'openai'    => 'gpt-4o-mini',
    'anthropic' => 'claude-opus-5',
];

/** El papel del tutor. Nunca se envía al navegador. */
const INSTRUCCION = <<<TXT
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
- Mantienes el hilo de la conversación: si preguntan "¿y sus síntomas?" sigues hablando
  del tema anterior.

Límite importante: esto es material de estudio. Si alguien te describe a un paciente real
o te pide una indicación para tratar a alguien ahora mismo, recuérdale que debe consultar
con un médico tratante y no le des una indicación de tratamiento individualizada.
TXT;

/* ====================== UTILIDADES ====================== */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');
header('Referrer-Policy: same-origin');

/** Devuelve una respuesta JSON y termina. */
function responder(int $codigo, array $cuerpo): void
{
    http_response_code($codigo);
    echo json_encode($cuerpo, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

/**
 * Error para el usuario: siempre el mismo texto.
 * El motivo real va al log del servidor, y solo viaja al navegador si AI_DEBUG=1.
 */
function fallar(int $codigo, string $motivoInterno, string $mensajeUsuario = MENSAJE_GENERICO): void
{
    global $DEPURAR;
    error_log('[MedQuizPro chat] ' . $motivoInterno);
    $cuerpo = ['error' => $mensajeUsuario];
    if (!empty($DEPURAR)) {
        $cuerpo['detalle'] = $motivoInterno;
    }
    responder($codigo, $cuerpo);
}

/** Lee una variable de entorno, mirando también $_SERVER/$_ENV (SetEnv de Apache). */
function entorno(string $nombre): string
{
    $valor = getenv($nombre);
    if ($valor === false || $valor === '') {
        $valor = $_SERVER[$nombre] ?? $_ENV[$nombre] ?? '';
    }
    return trim((string) $valor);
}

/** Variable de entorno; si no está, la clave de config.php; si no, el valor por defecto. */
function ajuste(string $env, string $clave, string $porDefecto = ''): string
{
    global $CONFIG;
    $valor = entorno($env);
    if ($valor !== '') {
        return $valor;
    }
    $valor = trim((string) ($CONFIG[$clave] ?? ''));
    return $valor !== '' ? $valor : $porDefecto;
}

function esVerdadero(string $valor): bool
{
    return in_array(strtolower($valor), ['1', 'true', 'si', 'sí', 'yes', 'on'], true);
}

/**
 * Petición HTTP con cURL.
 *
 * @param array<int,string> $cabeceras
 * @return array{codigo:int, cuerpo:array|null, crudo:string, error:string}
 */
function peticion(string $url, ?array $payload = null, array $cabeceras = []): array
{
    $ch = curl_init($url);
    if ($ch === false) {
        return ['codigo' => 0, 'cuerpo' => null, 'crudo' => '', 'error' => 'cURL no disponible'];
    }
    $opciones = [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => TIMEOUT_SEGUNDOS,
        CURLOPT_CONNECTTIMEOUT => 10,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2,
        CURLOPT_HTTPHEADER     => array_merge(['Content-Type: application/json'], $cabeceras),
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

/** Resume en una línea qué contestó el proveedor, para el log. */
function detalleDeError(array $r): string
{
    if ($r['error'] !== '') {
        return 'red: ' . $r['error'];
    }
    $cuerpo = is_array($r['cuerpo'] ?? null) ? $r['cuerpo'] : [];
    $error = $cuerpo['error'] ?? null;

    $mensaje = '';
    if (is_array($error)) {
        $mensaje = (string) ($error['message'] ?? $error['status'] ?? '');
    } elseif (is_string($error)) {
        $mensaje = $error;
    }
    if ($mensaje === '') {
        $mensaje = mb_substr(trim((string) $r['crudo']), 0, 300);
    }
    return 'HTTP ' . $r['codigo'] . ' ' . $mensaje;
}

/* ====================== CONFIGURACIÓN ====================== */

$CONFIG = [];
if (is_readable(__DIR__ . '/config.php')) {
    $cargado = require __DIR__ . '/config.php';
    if (is_array($cargado)) {
        $CONFIG = $cargado;
    }
}

$DEPURAR = esVerdadero(ajuste('AI_DEBUG', 'depurar', '0'));

$proveedor = strtolower(ajuste('AI_PROVIDER', 'ai_provider', 'gemini'));
if (!isset(MODELO_POR_DEFECTO[$proveedor])) {
    $proveedor = 'gemini';
}

/* La llave: AI_API_KEY es la forma recomendada; GEMINI_API_KEY se sigue admitiendo. */
$apiKey = ajuste('AI_API_KEY', 'ai_api_key');
if ($apiKey === '') {
    $apiKey = ajuste('GEMINI_API_KEY', 'gemini_api_key');
}

$modelo = ajuste('AI_MODEL', 'ai_model');
if ($modelo === '') {
    $modelo = ajuste('GEMINI_MODEL', 'gemini_model', MODELO_POR_DEFECTO[$proveedor]);
}

$baseUrl = rtrim(ajuste('AI_BASE_URL', 'ai_base_url'), '/');

$limiteMinuto = max(1, (int) ajuste('AI_LIMITE_MINUTO', 'limite_minuto', (string) LIMITE_MINUTO_DEF));
$limiteDia    = max(1, (int) ajuste('AI_LIMITE_DIA', 'limite_dia', (string) LIMITE_DIA_DEF));

$tokenDiagnostico = ajuste('AI_DIAGNOSTICO_TOKEN', 'diagnostico_token');

/* ====================== ENCAMINADO ====================== */

$accion = (string) ($_GET['accion'] ?? '');
$metodo = strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? 'GET'));

/* ¿El tutor está configurado? Lo usa el widget para avisar con elegancia. */
if ($accion === 'estado') {
    responder(200, ['listo' => $apiKey !== '']);
}

if ($accion === 'diagnostico') {
    diagnostico($proveedor, $apiKey, $modelo, $baseUrl, $tokenDiagnostico);
}

if ($metodo !== 'POST') {
    header('Allow: POST');
    responder(405, ['error' => 'Este endpoint solo admite POST.']);
}

/* Petición desde otro sitio web: se rechaza. El navegador manda Origin en los POST. */
$origen = (string) ($_SERVER['HTTP_ORIGIN'] ?? '');
if ($origen !== '') {
    $anfitrionOrigen = strtolower((string) parse_url($origen, PHP_URL_HOST));
    $anfitrionPropio = strtolower((string) preg_replace('/:\d+$/', '', (string) ($_SERVER['HTTP_HOST'] ?? '')));
    if ($anfitrionOrigen !== '' && $anfitrionPropio !== '' && $anfitrionOrigen !== $anfitrionPropio) {
        fallar(403, 'origen no permitido: ' . $origen);
    }
}

if ($apiKey === '') {
    fallar(503, 'falta la llave de IA (AI_API_KEY o config.php)',
        'El tutor todavía no está disponible. Vuelve a intentarlo más tarde.');
}

/* ====================== LÍMITE DE USO POR IP ====================== */

$ip = (string) ($_SERVER['REMOTE_ADDR'] ?? 'desconocida');
limitar($ip, $limiteMinuto, $limiteDia);

/**
 * Cuenta las peticiones de una IP en el último minuto y en el día.
 * Es un control básico contra el abuso, suficiente para una web pública pequeña.
 */
function limitar(string $ip, int $porMinuto, int $porDia): void
{
    $archivo = sys_get_temp_dir() . '/mqp_chat_' . sha1($ip) . '.json';
    $ahora = time();
    $hoy = gmdate('Y-m-d');

    $minuto = [];
    $dia = ['fecha' => $hoy, 'n' => 0];

    if (is_readable($archivo)) {
        $previo = json_decode((string) @file_get_contents($archivo), true);
        if (is_array($previo)) {
            $minuto = array_values(array_filter(
                (array) ($previo['minuto'] ?? []),
                static fn($t): bool => is_int($t) && $t > $ahora - 60
            ));
            if (is_array($previo['dia'] ?? null) && ($previo['dia']['fecha'] ?? '') === $hoy) {
                $dia = ['fecha' => $hoy, 'n' => (int) ($previo['dia']['n'] ?? 0)];
            }
        }
    }

    if (count($minuto) >= $porMinuto) {
        header('Retry-After: 60');
        responder(429, ['error' => 'Vas muy rápido. Espera un minuto y vuelve a preguntarme.']);
    }
    if ($dia['n'] >= $porDia) {
        header('Retry-After: 3600');
        responder(429, ['error' => 'Has alcanzado el límite de preguntas de hoy. Vuelve mañana.']);
    }

    $minuto[] = $ahora;
    $dia['n']++;
    @file_put_contents($archivo, json_encode(['minuto' => $minuto, 'dia' => $dia]), LOCK_EX);
}

/* ====================== LEER LA CONVERSACIÓN ====================== */

$crudoEntrada = (string) file_get_contents('php://input');
if (strlen($crudoEntrada) > 200000) {
    fallar(413, 'cuerpo demasiado grande');
}
$entrada = json_decode($crudoEntrada, true);
if (!is_array($entrada)) {
    fallar(400, 'cuerpo no es JSON');
}

$mensaje = trim((string) ($entrada['mensaje'] ?? $entrada['message'] ?? ''));
if ($mensaje === '') {
    responder(400, ['error' => 'Escribe una pregunta antes de enviar.']);
}
if (mb_strlen($mensaje) > MAX_CARACTERES) {
    responder(400, ['error' => 'El mensaje es demasiado largo. Resúmelo en ' . MAX_CARACTERES . ' caracteres o menos.']);
}

/** Historial normalizado: [['rol' => 'usuario'|'tutor', 'texto' => '...'], …] */
$historial = [];
$recibido = $entrada['historial'] ?? $entrada['history'] ?? [];
if (is_array($recibido)) {
    foreach (array_slice($recibido, -(MAX_HISTORIAL_TURNOS * 2)) as $turno) {
        if (!is_array($turno)) {
            continue;
        }
        $texto = trim((string) ($turno['texto'] ?? $turno['text'] ?? ''));
        if ($texto === '') {
            continue;
        }
        $rol = (string) ($turno['rol'] ?? $turno['role'] ?? 'usuario');
        $historial[] = [
            'rol'   => in_array($rol, ['tutor', 'model', 'assistant', 'ia'], true) ? 'tutor' : 'usuario',
            'texto' => mb_substr($texto, 0, MAX_CARACTERES),
        ];
    }
}
$historial[] = ['rol' => 'usuario', 'texto' => $mensaje];

/* ====================== LLAMADA AL PROVEEDOR ====================== */

$resultado = match ($proveedor) {
    'openai'    => hablarOpenAI($apiKey, $modelo, $baseUrl, $historial),
    'anthropic' => hablarAnthropic($apiKey, $modelo, $baseUrl, $historial),
    default     => hablarGemini($apiKey, $modelo, $historial),
};

if (!$resultado['ok']) {
    $codigo = $resultado['http'] === 429 ? 429 : 502;
    $mensajeUsuario = $resultado['http'] === 429
        ? 'El tutor está recibiendo muchas preguntas ahora mismo. Inténtalo en un minuto.'
        : MENSAJE_GENERICO;
    fallar($codigo, $proveedor . ': ' . $resultado['detalle'], $mensajeUsuario);
}

responder(200, [
    'respuesta' => $resultado['texto'],
    'reply'     => $resultado['texto'],  // nombre alternativo, por compatibilidad
]);

/* ====================== PROVEEDOR: GEMINI ====================== */

/** @return array{ok:bool, texto:string, http:int, detalle:string} */
function hablarGemini(string $apiKey, string $modeloForzado, array $historial): array
{
    $claveUrl = urlencode($apiKey);
    $archivoCache = sys_get_temp_dir() . '/mqp_modelo_' . sha1($apiKey) . '.json';

    $contents = [];
    foreach ($historial as $turno) {
        $contents[] = [
            'role'  => $turno['rol'] === 'tutor' ? 'model' : 'user',
            'parts' => [['text' => $turno['texto']]],
        ];
    }

    $payload = [
        'systemInstruction' => ['parts' => [['text' => INSTRUCCION]]],
        'contents'          => $contents,
        'generationConfig'  => [
            'temperature'     => TEMPERATURA,
            'maxOutputTokens' => MAX_TOKENS_RESPUESTA,
        ],
    ];

    $eleccion = cacheLeer($archivoCache);
    if ($eleccion === null) {
        $eleccion = resolverModeloGemini($claveUrl, $modeloForzado);
        if ($eleccion === null) {
            return ['ok' => false, 'texto' => '', 'http' => 502,
                    'detalle' => 'no se pudo determinar el modelo disponible para esta llave'];
        }
    }

    $ultimoDetalle = '';
    $ultimoHttp = 0;

    for ($intento = 1; $intento <= 2; $intento++) {
        $url = URL_GEMINI . $eleccion['version'] . '/models/' . rawurlencode($eleccion['modelo'])
             . ':generateContent?key=' . $claveUrl;
        $r = peticion($url, $payload);

        if ($r['codigo'] === 200) {
            cacheGuardar($archivoCache, $eleccion['modelo'], $eleccion['version']);
            return textoDeGemini($r['cuerpo'] ?? []);
        }

        $ultimoHttp = $r['codigo'];
        $ultimoDetalle = detalleDeError($r);

        /* El modelo guardado ya no existe: se descarta la caché y se vuelve a preguntar. */
        $retirado = $r['codigo'] === 404
            || stripos($ultimoDetalle, 'not found') !== false
            || stripos($ultimoDetalle, 'no longer available') !== false;

        if ($retirado && $intento === 1) {
            @unlink($archivoCache);
            $nuevo = resolverModeloGemini($claveUrl, '');
            if ($nuevo === null) {
                break;
            }
            $eleccion = $nuevo;
            continue;
        }
        break;
    }

    return ['ok' => false, 'texto' => '', 'http' => $ultimoHttp, 'detalle' => $ultimoDetalle];
}

/** Saca el texto de la respuesta de Gemini. */
function textoDeGemini(array $datos): array
{
    $candidato = $datos['candidates'][0] ?? null;

    if ($candidato === null) {
        if (($datos['promptFeedback']['blockReason'] ?? '') !== '') {
            return ['ok' => true, 'http' => 200, 'detalle' => '',
                    'texto' => 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.'];
        }
        return ['ok' => false, 'texto' => '', 'http' => 502, 'detalle' => 'respuesta sin candidatos'];
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
        if (in_array($motivo, ['SAFETY', 'PROHIBITED_CONTENT', 'BLOCKLIST'], true)) {
            return ['ok' => true, 'http' => 200, 'detalle' => '',
                    'texto' => 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.'];
        }
        if ($motivo === 'MAX_TOKENS') {
            return ['ok' => true, 'http' => 200, 'detalle' => '',
                    'texto' => 'La respuesta salió demasiado larga y se cortó. Pregúntame por partes más pequeñas.'];
        }
        return ['ok' => false, 'texto' => '', 'http' => 502, 'detalle' => 'respuesta vacía (' . $motivo . ')'];
    }

    return ['ok' => true, 'texto' => $texto, 'http' => 200, 'detalle' => ''];
}

/** Lista los modelos que la llave puede usar en una versión de la API. */
function listarModelosGemini(string $version, string $claveUrl): array
{
    $modelos = [];
    $token = '';
    for ($pagina = 0; $pagina < 3; $pagina++) {
        $url = URL_GEMINI . $version . '/models?pageSize=200&key=' . $claveUrl
             . ($token !== '' ? '&pageToken=' . urlencode($token) : '');
        $r = peticion($url);
        if ($r['codigo'] !== 200 || !is_array($r['cuerpo'])) {
            return ['modelos' => $modelos, 'codigo' => $r['codigo'], 'detalle' => detalleDeError($r)];
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
    return ['modelos' => array_values(array_filter($modelos)), 'codigo' => 200, 'detalle' => ''];
}

/** Elige el mejor modelo de una lista real de modelos disponibles. */
function elegirModeloGemini(array $disponibles): string
{
    if (!$disponibles) {
        return '';
    }
    foreach (MODELOS_PREFERIDOS as $preferido) {
        if (in_array($preferido, $disponibles, true)) {
            return $preferido;
        }
    }
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

/** @return array{modelo:string, version:string}|null */
function resolverModeloGemini(string $claveUrl, string $modeloForzado): ?array
{
    if ($modeloForzado !== '') {
        return ['modelo' => $modeloForzado, 'version' => VERSIONES_API[0]];
    }
    foreach (VERSIONES_API as $version) {
        $r = listarModelosGemini($version, $claveUrl);
        if ($r['codigo'] === 200 && $r['modelos']) {
            $elegido = elegirModeloGemini($r['modelos']);
            if ($elegido !== '') {
                return ['modelo' => $elegido, 'version' => $version];
            }
        }
        if ($r['detalle'] !== '') {
            error_log('[MedQuizPro chat] listado de modelos ' . $version . ': ' . $r['detalle']);
        }
    }
    return null;
}

function cacheLeer(string $archivo): ?array
{
    if (!is_readable($archivo)) {
        return null;
    }
    $datos = json_decode((string) @file_get_contents($archivo), true);
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

/* ====================== PROVEEDOR: OPENAI Y COMPATIBLES ====================== */
/* Sirve para OpenAI y para cualquier API con el mismo formato (Groq, DeepSeek,
   OpenRouter, Together, un modelo propio…): basta con cambiar AI_BASE_URL. */

function hablarOpenAI(string $apiKey, string $modelo, string $baseUrl, array $historial): array
{
    $base = $baseUrl !== '' ? $baseUrl : URL_OPENAI;
    $modelo = $modelo !== '' ? $modelo : MODELO_POR_DEFECTO['openai'];

    $mensajes = [['role' => 'system', 'content' => INSTRUCCION]];
    foreach ($historial as $turno) {
        $mensajes[] = [
            'role'    => $turno['rol'] === 'tutor' ? 'assistant' : 'user',
            'content' => $turno['texto'],
        ];
    }

    $r = peticion($base . '/chat/completions', [
        'model'       => $modelo,
        'messages'    => $mensajes,
        'temperature' => TEMPERATURA,
        'max_tokens'  => MAX_TOKENS_RESPUESTA,
    ], ['Authorization: Bearer ' . $apiKey]);

    if ($r['codigo'] !== 200) {
        return ['ok' => false, 'texto' => '', 'http' => $r['codigo'], 'detalle' => detalleDeError($r)];
    }

    $texto = trim((string) ($r['cuerpo']['choices'][0]['message']['content'] ?? ''));
    if ($texto === '') {
        return ['ok' => false, 'texto' => '', 'http' => 502, 'detalle' => 'respuesta vacía'];
    }
    return ['ok' => true, 'texto' => $texto, 'http' => 200, 'detalle' => ''];
}

/* ====================== PROVEEDOR: ANTHROPIC (CLAUDE) ====================== */

function hablarAnthropic(string $apiKey, string $modelo, string $baseUrl, array $historial): array
{
    $base = $baseUrl !== '' ? $baseUrl : URL_ANTHROPIC;
    $modelo = $modelo !== '' ? $modelo : MODELO_POR_DEFECTO['anthropic'];

    $mensajes = [];
    foreach ($historial as $turno) {
        $mensajes[] = [
            'role'    => $turno['rol'] === 'tutor' ? 'assistant' : 'user',
            'content' => $turno['texto'],
        ];
    }

    $r = peticion($base . '/messages', [
        'model'      => $modelo,
        'max_tokens' => MAX_TOKENS_RESPUESTA,
        'system'     => INSTRUCCION,
        'messages'   => $mensajes,
    ], [
        'x-api-key: ' . $apiKey,
        'anthropic-version: 2023-06-01',
    ]);

    if ($r['codigo'] !== 200) {
        return ['ok' => false, 'texto' => '', 'http' => $r['codigo'], 'detalle' => detalleDeError($r)];
    }

    /* La respuesta es una lista de bloques; solo interesan los de texto. */
    $texto = '';
    foreach ((array) ($r['cuerpo']['content'] ?? []) as $bloque) {
        if (($bloque['type'] ?? '') === 'text') {
            $texto .= (string) ($bloque['text'] ?? '');
        }
    }
    $texto = trim($texto);

    if ($texto === '') {
        if (($r['cuerpo']['stop_reason'] ?? '') === 'refusal') {
            return ['ok' => true, 'http' => 200, 'detalle' => '',
                    'texto' => 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.'];
        }
        return ['ok' => false, 'texto' => '', 'http' => 502, 'detalle' => 'respuesta vacía'];
    }
    return ['ok' => true, 'texto' => $texto, 'http' => 200, 'detalle' => ''];
}

/* ====================== DIAGNÓSTICO ====================== */
/* GET api.php?accion=diagnostico&token=…  — solo funciona si se ha puesto una
   palabra secreta en AI_DIAGNOSTICO_TOKEN (o diagnostico_token en config.php).
   Nunca muestra la llave. */

function diagnostico(string $proveedor, string $apiKey, string $modelo, string $baseUrl, string $token): void
{
    if ($token === '' || !hash_equals($token, (string) ($_GET['token'] ?? ''))) {
        responder(403, ['error' => 'Diagnóstico no disponible.']);
    }

    $informe = [
        'php'          => PHP_VERSION,
        'curl'         => function_exists('curl_init'),
        'proveedor'    => $proveedor,
        'llave'        => $apiKey !== '' ? 'configurada (' . strlen($apiKey) . ' caracteres)' : 'FALTA',
        'modelo'       => $modelo !== '' ? $modelo : '(automático)',
        'base_url'     => $baseUrl !== '' ? $baseUrl : '(por defecto)',
    ];

    if ($proveedor === 'gemini' && $apiKey !== '') {
        $claveUrl = urlencode($apiKey);
        foreach (VERSIONES_API as $version) {
            $r = listarModelosGemini($version, $claveUrl);
            $informe['versiones'][$version] = [
                'http'    => $r['codigo'],
                'modelos' => $r['modelos'],
                'elegido' => $r['modelos'] ? elegirModeloGemini($r['modelos']) : null,
                'error'   => $r['detalle'] ?: null,
            ];
        }
        $informe['preferencias'] = MODELOS_PREFERIDOS;
    }

    if ($proveedor !== 'gemini' && $apiKey !== '') {
        $prueba = $proveedor === 'openai'
            ? hablarOpenAI($apiKey, $modelo, $baseUrl, [['rol' => 'usuario', 'texto' => 'Responde solo: ok']])
            : hablarAnthropic($apiKey, $modelo, $baseUrl, [['rol' => 'usuario', 'texto' => 'Responde solo: ok']]);
        $informe['prueba'] = ['ok' => $prueba['ok'], 'detalle' => $prueba['detalle'] ?: null];
    }

    responder(200, $informe);
}
