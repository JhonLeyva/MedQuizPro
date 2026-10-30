<?php
/**
 * acceso.php — puerta de los contenidos (bancos de preguntas, flujogramas, casos, guías, PDF).
 *
 * El .htaccess manda aquí cada petición a esos archivos: ?f=<ruta relativa>. Con el acceso abierto (por defecto) entrega el archivo sin más.
 * Con MQP_CERRADO=1 (o 'cerrado' => '1' en config.php) solo lo entrega a quien tenga sesión de cuenta (cookie mqp_sid) y sea el dueño
 * o tenga un plan activo; a los demás responde 401 (sin sesión) o 402 (sin plan). Nunca sirve archivos fuera de la lista ni fuera de la carpeta del sitio.
 * Es independiente de cuenta.php para no tocar su funcionamiento: solo lee las tablas usuarios y suscripciones.
 */
declare(strict_types=1);

const ACC_PREFIJOS = ['bancos', 'flujogramas', 'herramientas', 'residentado', 'guardia', 'consulta', 'serums', 'atlas3d'];
const ACC_RAIZ_JS = ['guardia_casos', 'guardia_lab', 'guardia_biblioteca', 'consulta_casos', 'serums_casos', 'algoritmos'];
const ACC_TIPOS = [
    'json' => 'application/json; charset=utf-8', 'js' => 'text/javascript; charset=utf-8', 'css' => 'text/css; charset=utf-8', 'html' => 'text/html; charset=utf-8',
    'webp' => 'image/webp', 'png' => 'image/png', 'jpg' => 'image/jpeg', 'jpeg' => 'image/jpeg', 'svg' => 'image/svg+xml', 'pdf' => 'application/pdf',
    'mp3' => 'audio/mpeg', 'glb' => 'model/gltf-binary', 'gltf' => 'model/gltf+json', 'bin' => 'application/octet-stream', 'woff2' => 'font/woff2', 'txt' => 'text/plain; charset=utf-8',
];

function acc_ajuste(string $env, string $clave): string {
    $v = getenv($env); if ($v !== false && $v !== '') return (string)$v;
    static $cfg = null; if ($cfg === null) { $f = __DIR__ . '/config.php'; $cfg = is_file($f) ? (array)(include $f) : []; }
    return isset($cfg[$clave]) ? (string)$cfg[$clave] : '';
}
function acc_cerrado(): bool { return acc_ajuste('MQP_CERRADO', 'cerrado') === '1'; }

/** Estado de acceso de la sesión actual: 'ok', 'sin_sesion' o 'sin_plan'. */
function acc_estado(): string {
    if (session_status() !== PHP_SESSION_ACTIVE) {
        if (!isset($_COOKIE['mqp_sid'])) return 'sin_sesion';
        session_name('mqp_sid'); session_set_cookie_params(['path' => '/', 'httponly' => true, 'samesite' => 'Lax']);
        @session_start(['read_and_close' => true]);   // solo lectura: no bloquea otras peticiones
    }
    $id = (int)($_SESSION['uid'] ?? 0); if (!$id) return 'sin_sesion';
    $bd = __DIR__ . '/cuenta_datos/mqp.sqlite'; if (!is_file($bd)) return 'sin_sesion';
    try {
        $pdo = new PDO('sqlite:' . $bd, null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
        $u = $pdo->prepare('SELECT id, dueno FROM usuarios WHERE id = ?'); $u->execute([$id]); $f = $u->fetch();
        if (!$f) return 'sin_sesion';
        if ((int)($f['dueno'] ?? 0) === 1) return 'ok';
        $s = $pdo->prepare('SELECT COUNT(*) FROM suscripciones WHERE usuario = ? AND hasta > ?'); $s->execute([$id, time()]);
        return (int)$s->fetchColumn() > 0 ? 'ok' : 'sin_plan';
    } catch (Throwable $e) { return 'sin_sesion'; }   // ante cualquier duda, cerrado
}

function acc_negar(int $codigo, string $msg): never {
    http_response_code($codigo); header('Content-Type: application/json; charset=utf-8'); header('Cache-Control: no-store');
    echo json_encode(['ok' => false, 'acceso' => $codigo === 401 ? 'sin_sesion' : 'sin_plan', 'error' => $msg], JSON_UNESCAPED_UNICODE); exit;
}
function acc_no_existe(): never { http_response_code(404); header('Content-Type: text/plain; charset=utf-8'); echo 'No encontrado.'; exit; }

/* ---- ruta pedida: solo rutas relativas de la lista, sin saltos de carpeta ni archivos ocultos ---- */
$f = (string)($_GET['f'] ?? '');   // PHP ya lo decodificó una vez; no se decodifica de nuevo
if ($f === '' || strlen($f) > 300 || strpbrk($f, "\0\\") !== false || $f[0] === '/' || preg_match('#(^|/)\.#', $f) || strpos($f, '//') !== false) acc_no_existe();
$partes = explode('/', $f); $ext = strtolower(pathinfo($f, PATHINFO_EXTENSION));
$permitido = (count($partes) > 1 && in_array($partes[0], ACC_PREFIJOS, true)) || (count($partes) === 1 && ($ext === 'pdf' || ($ext === 'js' && in_array(pathinfo($f, PATHINFO_FILENAME), ACC_RAIZ_JS, true))));
if (!$permitido || !isset(ACC_TIPOS[$ext])) acc_no_existe();
$ruta = realpath(__DIR__ . '/' . $f); $raiz = realpath(__DIR__);
if ($ruta === false || $raiz === false || strpos($ruta, $raiz . DIRECTORY_SEPARATOR) !== 0 || !is_file($ruta)) acc_no_existe();

if (acc_cerrado()) {
    $e = acc_estado();
    if ($e === 'sin_sesion') acc_negar(401, 'Inicia sesión para ver este contenido.');
    if ($e === 'sin_plan') acc_negar(402, 'Necesitas un plan activo para ver este contenido.');
}

$mt = (int)filemtime($ruta); $tam = (int)filesize($ruta); $etag = '"' . dechex($mt) . '-' . dechex($tam) . '"';
header('Content-Type: ' . ACC_TIPOS[$ext]); header('X-Content-Type-Options: nosniff'); header('ETag: ' . $etag);
header('Cache-Control: ' . (acc_cerrado() ? 'private, no-cache' : 'no-cache'));   // se revalida siempre (304 si no cambió); con acceso cerrado nunca lo guarda una caché compartida
if (($_SERVER['HTTP_IF_NONE_MATCH'] ?? '') === $etag) { http_response_code(304); exit; }
header('Content-Length: ' . $tam);
if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'HEAD') readfile($ruta);
