<?php
/**
 * api.php — puente entre el widget de chat y la API de Gemini.
 *
 * El navegador nunca ve la llave: la petición sale desde este archivo, en el servidor.
 *
 * Configuración: copia config.example.php como config.php y escribe ahí tu llave.
 * También sirve la variable de entorno GEMINI_API_KEY si tu hosting la admite.
 */

declare(strict_types=1);

const MODELO            = 'gemini-2.5-flash';
const MAX_CARACTERES    = 1500;   // largo máximo de la pregunta
const MAX_HISTORIAL     = 16;     // mensajes previos que se reenvían
const LIMITE_POR_MINUTO = 12;     // peticiones por IP y por minuto
const TIMEOUT_SEGUNDOS  = 45;

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

/* ---------- 1. Solo se admite POST ---------- */
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    responder(405, ['error' => 'Este endpoint solo admite POST.']);
}

/* ---------- 2. La llave ---------- */
$apiKey = getenv('GEMINI_API_KEY') ?: '';
if ($apiKey === '' && is_readable(__DIR__ . '/config.php')) {
    /** @var array{gemini_api_key?: string} $config */
    $config = require __DIR__ . '/config.php';
    $apiKey = is_array($config) ? trim((string) ($config['gemini_api_key'] ?? '')) : '';
}
if ($apiKey === '') {
    error_log('api.php: falta la llave de Gemini (config.php o GEMINI_API_KEY).');
    responder(500, ['error' => 'El tutor todavía no está configurado en el servidor.']);
}

/* ---------- 3. Límite de uso por IP ---------- */
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

/* ---------- 4. Leer y validar la pregunta ---------- */
$crudo = file_get_contents('php://input');
$entrada = json_decode((string) $crudo, true);
if (!is_array($entrada)) {
    responder(400, ['error' => 'No se pudo leer la pregunta.']);
}

$mensaje = trim((string) ($entrada['mensaje'] ?? ''));
if ($mensaje === '') {
    responder(400, ['error' => 'Escribe una pregunta antes de enviar.']);
}
if (mb_strlen($mensaje) > MAX_CARACTERES) {
    responder(400, ['error' => 'La pregunta es demasiado larga. Resúmela en ' . MAX_CARACTERES . ' caracteres o menos.']);
}

/* ---------- 5. Armar la conversación para Gemini ---------- */
$instruccion = <<<TXT
Eres el tutor de MedQuizPro, una plataforma peruana de preparación para el ENAM,
el Residentado Médico (RM) y los exámenes de EsSalud.

Cómo respondes:
- Siempre en español, con el registro de un docente de medicina que explica a un interno.
- Vas al grano: primero la respuesta, después el razonamiento.
- Usas la terminología y las guías que se toman en los exámenes peruanos (MINSA, AIEPI,
  guías de práctica clínica nacionales) cuando vienen al caso.
- Si te preguntan por un caso clínico de examen, explicas también por qué los distractores
  son incorrectos.
- Si no sabes algo o el dato depende de una guía que puede haber cambiado, lo dices.
- Máximo unos 250 palabras, salvo que te pidan más detalle.

Límite importante: esto es material de estudio. Si alguien te describe a un paciente real
o te pide una indicación para tratar a alguien ahora mismo, recuérdale que debe consultar
con un médico tratante y no le des una indicación de tratamiento individualizada.
TXT;

$contents = [];
$historial = $entrada['historial'] ?? [];
if (is_array($historial)) {
    foreach (array_slice($historial, -MAX_HISTORIAL) as $turno) {
        if (!is_array($turno)) {
            continue;
        }
        $texto = trim((string) ($turno['texto'] ?? ''));
        if ($texto === '') {
            continue;
        }
        $contents[] = [
            'role'  => (($turno['rol'] ?? '') === 'tutor') ? 'model' : 'user',
            'parts' => [['text' => mb_substr($texto, 0, MAX_CARACTERES)]],
        ];
    }
}
$contents[] = ['role' => 'user', 'parts' => [['text' => $mensaje]]];

$peticion = [
    'systemInstruction' => ['parts' => [['text' => $instruccion]]],
    'contents'          => $contents,
    'generationConfig'  => [
        'temperature'     => 0.4,
        'maxOutputTokens' => 900,
    ],
    'safetySettings'    => [],
];

/* ---------- 6. Llamada a Gemini con cURL ---------- */
$url = 'https://generativelanguage.googleapis.com/v1beta/models/' . MODELO . ':generateContent';

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => TIMEOUT_SEGUNDOS,
    CURLOPT_CONNECTTIMEOUT => 10,
    CURLOPT_SSL_VERIFYPEER => true,
    CURLOPT_SSL_VERIFYHOST => 2,
    CURLOPT_HTTPHEADER     => [
        'Content-Type: application/json',
        'x-goog-api-key: ' . $apiKey,
    ],
    CURLOPT_POSTFIELDS     => json_encode($peticion, JSON_UNESCAPED_UNICODE),
]);

$respuestaCruda = curl_exec($ch);
$codigoHttp     = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
$errorCurl      = curl_error($ch);
curl_close($ch);

if ($respuestaCruda === false) {
    error_log('api.php: fallo de cURL — ' . $errorCurl);
    responder(502, ['error' => 'No se pudo contactar con el tutor. Inténtalo de nuevo.']);
}

$datos = json_decode((string) $respuestaCruda, true);

if ($codigoHttp !== 200) {
    $detalle = is_array($datos) ? ($datos['error']['message'] ?? 'sin detalle') : 'respuesta no interpretable';
    error_log('api.php: Gemini respondió ' . $codigoHttp . ' — ' . $detalle);

    if ($codigoHttp === 429) {
        responder(429, ['error' => 'El tutor está saturado en este momento. Espera un poco y vuelve a preguntar.']);
    }
    if ($codigoHttp === 400 || $codigoHttp === 401 || $codigoHttp === 403) {
        responder(500, ['error' => 'El tutor no está bien configurado en el servidor.']);
    }
    responder(502, ['error' => 'El tutor no pudo responder ahora mismo. Inténtalo de nuevo.']);
}

/* ---------- 7. Extraer el texto ---------- */
$candidato = $datos['candidates'][0] ?? null;

if ($candidato === null) {
    $motivo = $datos['promptFeedback']['blockReason'] ?? null;
    if ($motivo !== null) {
        responder(200, ['respuesta' => 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.']);
    }
    error_log('api.php: respuesta de Gemini sin candidatos.');
    responder(502, ['error' => 'El tutor no pudo responder ahora mismo. Inténtalo de nuevo.']);
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
    if ($motivo === 'SAFETY' || $motivo === 'PROHIBITED_CONTENT') {
        responder(200, ['respuesta' => 'No puedo responder a esa pregunta. Prueba a plantearla de otra forma.']);
    }
    if ($motivo === 'MAX_TOKENS') {
        responder(200, ['respuesta' => 'La respuesta salió demasiado larga y se cortó. Pregúntame por partes más pequeñas.']);
    }
    error_log('api.php: respuesta vacía de Gemini (finishReason: ' . $motivo . ').');
    responder(502, ['error' => 'El tutor no pudo responder ahora mismo. Inténtalo de nuevo.']);
}

responder(200, ['respuesta' => $texto]);
