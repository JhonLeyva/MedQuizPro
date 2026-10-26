<?php
/**
 * cuenta.php — cuentas de usuario, planes y cobro (Mercado Pago, Checkout Pro).
 *
 * Todo viaja por JSON:  cuenta.php?a=<acción>
 *
 *   estado     (GET)   qué está activo: cuentas, pagos, límites y planes
 *   me         (GET)   la sesión actual: usuario y plan, o usuario:null
 *   registro   (POST)  crea la cuenta y abre sesión
 *   ingresar   (POST)  abre sesión
 *   salir      (POST)  cierra sesión
 *   comprar    (POST)  crea el cobro de un plan de un examen (PayU o Mercado Pago) y devuelve cómo ir a pagar
 *   espera     (POST)  se apunta a la lista de espera de un examen cuyo banco aún no abrió
 *   webhook    (POST)  aviso de Mercado Pago: se verifica el pago y se activa el plan
 *   payu       (POST)  confirmación de PayU: se verifica la firma y se activa el plan
 *   retorno    (GET)   a donde PayU devuelve al estudiante; solo lo redirige al app
 *   progreso_leer / progreso_guardar   el progreso de estudio del estudiante, guardado en su cuenta
 *   exportar   (POST)  descarga de TODOS los datos de la cuenta (derecho de acceso)
 *   eliminar   (POST)  borra la cuenta y su progreso, pidiendo la contraseña (derecho de cancelación)
 *   admin      (GET)   (solo tú) lista de cuentas y pagos en CSV o JSON; exige MQP_ADMIN_TOKEN
 *   dueno_activar (POST) con tu clave MQP_ADMIN_TOKEN, marca tu cuenta como «dueño»: todos los exámenes sin pagar
 *
 * Un plan SOLO se activa desde "webhook" (tras consultar el pago a Mercado Pago con tu token)
 * o desde "payu" (tras verificar la firma con tu ApiKey). Nada que llegue del navegador
 * puede activar un plan.
 *
 * Configuración (variables de entorno, o config.php si el hosting no las permite):
 *   PAYU_MERCHANT_ID, PAYU_ACCOUNT_ID, PAYU_API_KEY   datos de tu comercio en PayU Latam (Perú)
 *   PAYU_TEST           "1" para el entorno de pruebas (sandbox) de PayU
 *   PASARELA            payu | mercadopago  (si no se indica: PayU si está configurado, si no Mercado Pago)
 *   MP_ACCESS_TOKEN     token de acceso de tu aplicación de Mercado Pago
 *   MP_WEBHOOK_SECRET   clave secreta del webhook (recomendada: valida la firma del aviso)
 *   MQP_LIMITES         "1" para activar los límites del plan gratuito (por defecto: apagados)
 *   MQP_SITE_URL        URL pública del sitio, ej. https://midominio.com (por defecto se deduce)
 *   MQP_ADMIN_TOKEN     clave larga (16+ caracteres) para descargar tu lista de cuentas; sin ella esa acción no existe
 *   MP_API_BASE         solo para pruebas: otra URL para la API de Mercado Pago
 *
 * Los datos viven en cuenta_datos/mqp.sqlite (la carpeta se protege con su propio .htaccess).
 */

declare(strict_types=1);

require_once __DIR__ . '/flashcards_lib.php';

/* ====================== AJUSTES ====================== */

/** Periodos de los planes de pago único (sin renovación automática). */
const PERIODOS = [
    'mensual'    => ['nombre' => 'mensual',    'dias' => 30],
    'trimestral' => ['nombre' => 'trimestral', 'dias' => 90],
    'anual'      => ['nombre' => 'anual',      'dias' => 365],
];
/**
 * Cada examen tiene sus propios planes (precios en soles). "abierto" = el banco ya está publicado y se puede comprar;
 * los demás aceptan lista de espera hasta que se publique su banco: NO se les cobra por contenido que no existe.
 * Cuando un banco abre, basta con poner 'abierto' => true.
 */
const EXAMENES = [
    'essalud'     => ['nombre' => 'EsSalud',            'abierto' => false, 'precios' => ['mensual' => 19.00, 'trimestral' => 45.00, 'anual' => 129.00]],
    'enam'        => ['nombre' => 'ENAM',               'abierto' => true,  'precios' => ['mensual' => 29.00, 'trimestral' => 69.00, 'anual' => 199.00]],
    'residentado' => ['nombre' => 'Residentado Médico', 'abierto' => false, 'precios' => ['mensual' => 35.00, 'trimestral' => 85.00, 'anual' => 249.00]],
    'encaps'      => ['nombre' => 'ENCAPS SERUMS',      'abierto' => false, 'precios' => ['mensual' => 25.00, 'trimestral' => 59.00, 'anual' => 169.00]],
];
/** Datos de un plan, o null si el examen o el periodo no existen. */
function plan_info(string $examen, string $periodo): ?array {
    if (!isset(EXAMENES[$examen], PERIODOS[$periodo])) return null;
    $e = EXAMENES[$examen];
    return ['examen' => $examen, 'periodo' => $periodo, 'nombre' => 'Premium ' . $e['nombre'] . ' ' . PERIODOS[$periodo]['nombre'],
            'soles' => (float)$e['precios'][$periodo], 'dias' => PERIODOS[$periodo]['dias'], 'abierto' => $e['abierto']];
}
const LIMITE_GRATIS_DIARIO = 20;      // preguntas por día en el plan gratuito (si los límites están activos)
const MIN_CLAVE            = 8;
const INTENTOS_LOGIN       = 6;       // por correo+IP cada 15 minutos
const VENTANA_LOGIN        = 900;

/* ====================== UTILIDADES ====================== */

function ajuste(string $env, string $clave, string $def = ''): string {
    static $cfg = null;
    $v = getenv($env);
    if ($v !== false && $v !== '') return (string)$v;
    if ($cfg === null) {
        $f = __DIR__ . '/config.php';
        $cfg = is_file($f) ? (array)(include $f) : [];
    }
    return isset($cfg[$clave]) ? (string)$cfg[$clave] : $def;
}

function responder(array $d, int $codigo = 200): never {
    http_response_code($codigo);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo json_encode($d, JSON_UNESCAPED_UNICODE);
    exit;
}
function fallo(string $msg, int $codigo = 400): never { responder(['ok' => false, 'error' => $msg], $codigo); }

function es_https(): bool {
    return (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
        || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
}
function url_sitio(): string {
    $u = ajuste('MQP_SITE_URL', 'site_url');
    if ($u !== '') return rtrim($u, '/');
    return (es_https() ? 'https' : 'http') . '://' . ($_SERVER['HTTP_HOST'] ?? 'localhost');
}
function limites_activos(): bool { return ajuste('MQP_LIMITES', 'limites') === '1'; }
function payu_ok(): bool {
    return ajuste('PAYU_MERCHANT_ID', 'payu_merchant_id') !== '' && ajuste('PAYU_ACCOUNT_ID', 'payu_account_id') !== '' && ajuste('PAYU_API_KEY', 'payu_api_key') !== '';
}
function mp_ok(): bool { return ajuste('MP_ACCESS_TOKEN', 'mp_access_token') !== ''; }
/** Pasarela en uso: 'payu', 'mercadopago' o '' (sin cobro). */
function pasarela(): string {
    $p = strtolower(ajuste('PASARELA', 'pasarela'));
    if ($p === 'payu' && payu_ok()) return 'payu';
    if ($p === 'mercadopago' && mp_ok()) return 'mercadopago';
    return payu_ok() ? 'payu' : (mp_ok() ? 'mercadopago' : '');
}
function pagos_activos(): bool { return pasarela() !== ''; }

function db(): PDO {
    static $pdo = null;
    if ($pdo) return $pdo;
    $dir = __DIR__ . '/cuenta_datos';
    if (!is_dir($dir)) @mkdir($dir, 0750, true);
    if (!is_file($dir . '/.htaccess')) @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n");
    $pdo = new PDO('sqlite:' . $dir . '/mqp.sqlite', null, null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    $pdo->exec('PRAGMA journal_mode=WAL; PRAGMA foreign_keys=ON;');
    $pdo->exec('CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT, correo TEXT NOT NULL UNIQUE, nombre TEXT NOT NULL,
        clave TEXT NOT NULL, examen TEXT, universidad TEXT, creado INTEGER NOT NULL,
        plan TEXT, premium_hasta INTEGER NOT NULL DEFAULT 0)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS progreso (usuario INTEGER PRIMARY KEY, datos TEXT NOT NULL, actualizado INTEGER NOT NULL)');
    $cols = array_column($pdo->query('PRAGMA table_info(usuarios)')->fetchAll(), 'name');
    if (!in_array('acepto_en', $cols, true)) $pdo->exec('ALTER TABLE usuarios ADD COLUMN acepto_en INTEGER');
    if (!in_array('dueno', $cols, true)) $pdo->exec('ALTER TABLE usuarios ADD COLUMN dueno INTEGER NOT NULL DEFAULT 0');
    $pdo->exec('CREATE TABLE IF NOT EXISTS pagos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, mp_id TEXT NOT NULL UNIQUE, usuario INTEGER NOT NULL,
        plan TEXT NOT NULL, monto REAL NOT NULL, creado INTEGER NOT NULL)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS suscripciones (usuario INTEGER NOT NULL, examen TEXT NOT NULL, plan TEXT NOT NULL, hasta INTEGER NOT NULL, PRIMARY KEY (usuario, examen))');
    $pdo->exec('CREATE TABLE IF NOT EXISTS lista_espera (usuario INTEGER NOT NULL, examen TEXT NOT NULL, creado INTEGER NOT NULL, PRIMARY KEY (usuario, examen))');
    $pdo->exec('CREATE TABLE IF NOT EXISTS ordenes (
        ref TEXT PRIMARY KEY, usuario INTEGER NOT NULL, plan TEXT NOT NULL, monto REAL NOT NULL, creado INTEGER NOT NULL)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
        frente TEXT NOT NULL, dorso TEXT NOT NULL, pregunta TEXT NOT NULL DEFAULT \'\', tema TEXT NOT NULL DEFAULT \'\',
        especialidad TEXT NOT NULL DEFAULT \'\', fuente TEXT NOT NULL DEFAULT \'\', huella TEXT NOT NULL,
        estado TEXT NOT NULL DEFAULT \'nuevo\', facilidad REAL NOT NULL DEFAULT 2.5, intervalo INTEGER NOT NULL DEFAULT 0,
        repeticiones INTEGER NOT NULL DEFAULT 0, lapsos INTEGER NOT NULL DEFAULT 0,
        creado INTEGER NOT NULL, ultimo INTEGER NOT NULL DEFAULT 0, proximo INTEGER NOT NULL, UNIQUE (usuario, huella))');
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_fc_cola ON flashcards(usuario, proximo)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS repasos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, tarjeta INTEGER NOT NULL REFERENCES flashcards(id) ON DELETE CASCADE,
        usuario INTEGER NOT NULL, t INTEGER NOT NULL, calificacion TEXT NOT NULL, estado_antes TEXT NOT NULL,
        intervalo_antes INTEGER NOT NULL, intervalo_despues INTEGER NOT NULL)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_repasos_t ON repasos(usuario, t)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS intentos (clave TEXT NOT NULL, t INTEGER NOT NULL)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_intentos ON intentos(clave, t)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS ritmo (clave TEXT NOT NULL, t INTEGER NOT NULL)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_ritmo ON ritmo(clave, t)');
    foreach (['pagos', 'ordenes'] as $t) {                    // migración: cada pago y orden recuerda de qué examen es
        $cs = array_column($pdo->query('PRAGMA table_info(' . $t . ')')->fetchAll(), 'name');
        if (!in_array('examen', $cs, true)) $pdo->exec('ALTER TABLE ' . $t . " ADD COLUMN examen TEXT NOT NULL DEFAULT 'enam'");
    }
    // migración: quien tenía un plan único pasa a tener ese mismo plan en ENAM (el único banco abierto)
    $pdo->exec("INSERT OR IGNORE INTO suscripciones(usuario, examen, plan, hasta) SELECT id, 'enam', plan, premium_hasta FROM usuarios WHERE premium_hasta > 0 AND plan IS NOT NULL");
    return $pdo;
}

function iniciar_sesion(): void {
    if (session_status() === PHP_SESSION_ACTIVE) return;
    session_name('mqp_sid');
    session_set_cookie_params(['lifetime' => 60 * 60 * 24 * 30, 'path' => '/', 'secure' => es_https(), 'httponly' => true, 'samesite' => 'Lax']);
    session_start();
}

function cuerpo(): array {
    $raw = file_get_contents('php://input') ?: '';
    $j = json_decode($raw, true);
    return is_array($j) ? $j : [];
}

/** Los POST del sitio llevan una cabecera propia: un formulario de otro sitio no puede enviarla. */
function exigir_post_del_sitio(): void {
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') fallo('Método no permitido.', 405);
    if (($_SERVER['HTTP_X_MQP'] ?? '') !== '1') fallo('Solicitud no válida.', 403);
}

function suscripciones_de(int $uid): array {
    $st = db()->prepare('SELECT examen, plan, hasta FROM suscripciones WHERE usuario = ? AND hasta > ?'); $st->execute([$uid, time()]);
    $m = []; foreach ($st->fetchAll() as $f) $m[$f['examen']] = ['plan' => $f['plan'], 'hasta' => (int)$f['hasta']];
    return $m;
}
function usuario_publico(?array $u): ?array {
    if (!$u) return null;
    $subs = suscripciones_de((int)$u['id']);
    if ((int)($u['dueno'] ?? 0) === 1) foreach (array_keys(EXAMENES) as $ex) $subs[$ex] = ['plan' => 'dueño', 'hasta' => 4102444800];   // la cuenta del dueño tiene todos los exámenes, sin pagar
    $en = $subs['enam'] ?? null;                              // la plataforma de estudio hoy solo tiene el banco ENAM: ese plan define "premium"
    $st = db()->prepare('SELECT examen FROM lista_espera WHERE usuario = ?'); $st->execute([(int)$u['id']]);
    return [
        'id' => (int)$u['id'], 'nombre' => $u['nombre'], 'correo' => $u['correo'], 'examen' => $u['examen'],
        'premium' => (bool)$en, 'plan' => $en ? $en['plan'] : null, 'premium_hasta' => $en ? $en['hasta'] : null,
        'suscripciones' => (object)$subs, 'espera' => array_column($st->fetchAll(), 'examen'), 'dueno' => (int)($u['dueno'] ?? 0) === 1,
    ];
}
function usuario_actual(): ?array {
    iniciar_sesion();
    $id = (int)($_SESSION['uid'] ?? 0);
    if (!$id) return null;
    $st = db()->prepare('SELECT * FROM usuarios WHERE id = ?'); $st->execute([$id]);
    $u = $st->fetch();
    return $u ?: null;
}

/** Límite de escrituras por usuario (evita abuso y bucles del navegador): `max` acciones cada `seg` segundos. */
function limitar_ritmo(int $uid, string $accion, int $max, int $seg = 60): void {
    $db = db(); $k = $uid . '|' . $accion; $ahora = time();
    $db->prepare('DELETE FROM ritmo WHERE t < ?')->execute([$ahora - 3600]);
    $st = $db->prepare('SELECT COUNT(*) FROM ritmo WHERE clave = ? AND t > ?'); $st->execute([$k, $ahora - $seg]);
    if ((int) $st->fetchColumn() >= $max) { header('Retry-After: ' . $seg); fallo('Vas muy rápido. Espera un momento e inténtalo de nuevo.', 429); }
    $db->prepare('INSERT INTO ritmo(clave, t) VALUES (?, ?)')->execute([$k, $ahora]);
}

function ip(): string { return substr((string)($_SERVER['REMOTE_ADDR'] ?? '0'), 0, 45); }

function limitar_login(string $correo): void {
    $k = hash('sha256', strtolower($correo) . '|' . ip());
    $db = db();
    $db->prepare('DELETE FROM intentos WHERE t < ?')->execute([time() - VENTANA_LOGIN]);
    $st = $db->prepare('SELECT COUNT(*) FROM intentos WHERE clave = ?'); $st->execute([$k]);
    if ((int)$st->fetchColumn() >= INTENTOS_LOGIN) fallo('Demasiados intentos. Espera unos minutos y vuelve a probar.', 429);
}
function anotar_intento(string $correo): void {
    db()->prepare('INSERT INTO intentos(clave, t) VALUES (?, ?)')->execute([hash('sha256', strtolower($correo) . '|' . ip()), time()]);
}

/* ====================== MERCADO PAGO ====================== */

function mp(string $metodo, string $ruta, ?array $datos = null): array {
    $base = rtrim(ajuste('MP_API_BASE', 'mp_api_base', 'https://api.mercadopago.com'), '/');
    $ch = curl_init($base . $ruta);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 20, CURLOPT_CUSTOMREQUEST => $metodo,
        CURLOPT_HTTPHEADER => ['Authorization: Bearer ' . ajuste('MP_ACCESS_TOKEN', 'mp_access_token'), 'Content-Type: application/json'],
    ]);
    if ($datos !== null) curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($datos, JSON_UNESCAPED_UNICODE));
    $r = curl_exec($ch);
    $c = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    $j = is_string($r) ? json_decode($r, true) : null;
    return ['codigo' => $c, 'datos' => is_array($j) ? $j : []];
}

function firma_valida(string $dataId): bool {
    $secreto = ajuste('MP_WEBHOOK_SECRET', 'mp_webhook_secret');
    if ($secreto === '') return true;                      // sin secreto configurado, solo se confía en la consulta directa a MP
    $h = $_SERVER['HTTP_X_SIGNATURE'] ?? '';
    $rid = $_SERVER['HTTP_X_REQUEST_ID'] ?? '';
    $ts = $v1 = '';
    foreach (explode(',', $h) as $par) {
        $p = explode('=', trim($par), 2);
        if (count($p) === 2) { if ($p[0] === 'ts') $ts = $p[1]; if ($p[0] === 'v1') $v1 = $p[1]; }
    }
    if ($ts === '' || $v1 === '') return false;
    $calc = hash_hmac('sha256', "id:" . strtolower($dataId) . ";request-id:$rid;ts:$ts;", $secreto);
    return hash_equals($calc, $v1);
}

function activar_plan(int $uid, string $examen, string $periodo, string $mpId, float $monto): void {
    $info = plan_info($examen, $periodo); if (!$info) return;
    $db = db();
    $db->beginTransaction();
    try {
        $ya = $db->prepare('SELECT 1 FROM pagos WHERE mp_id = ?'); $ya->execute([$mpId]);
        if ($ya->fetch()) { $db->commit(); return; }       // el aviso puede llegar repetido: se activa una sola vez
        $u = $db->prepare('SELECT 1 FROM usuarios WHERE id = ?'); $u->execute([$uid]);
        if (!$u->fetch()) { $db->rollBack(); return; }
        $s = $db->prepare('SELECT hasta FROM suscripciones WHERE usuario = ? AND examen = ?'); $s->execute([$uid, $examen]);
        $actual = (int)($s->fetchColumn() ?: 0);
        $hasta = max(time(), $actual) + $info['dias'] * 86400;   // renovar suma al tiempo que ya tenía
        $db->prepare('INSERT INTO suscripciones(usuario, examen, plan, hasta) VALUES (?,?,?,?) ON CONFLICT(usuario, examen) DO UPDATE SET plan = excluded.plan, hasta = excluded.hasta')->execute([$uid, $examen, $periodo, $hasta]);
        $db->prepare('INSERT INTO pagos(mp_id, usuario, plan, monto, creado, examen) VALUES (?,?,?,?,?,?)')->execute([$mpId, $uid, $periodo, $monto, time(), $examen]);
        $db->commit();
    } catch (Throwable $e) { $db->rollBack(); throw $e; }
}

/* ====================== ACCIONES ====================== */

try {
    $a = (string)($_GET['a'] ?? '');

    if ($a === 'dueno_activar') {
        // El dueño (con la clave de MQP_ADMIN_TOKEN, que solo él conoce) marca SU cuenta ya creada como cuenta de dueño: acceso a todo sin pagar.
        // No depende del correo (que no está verificado): sin la clave nadie puede activarlo.
        exigir_post_del_sitio();
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión primero.', 401);
        $tok = ajuste('MQP_ADMIN_TOKEN', 'admin_token');
        if (strlen($tok) < 16) fallo('Acción desconocida.', 404);
        limitar_login('dueno|' . $u['correo']);
        if (!hash_equals($tok, (string)(cuerpo()['token'] ?? ''))) { anotar_intento('dueno|' . $u['correo']); fallo('Clave incorrecta.', 401); }
        db()->prepare('UPDATE usuarios SET dueno = 1 WHERE id = ?')->execute([(int)$u['id']]);
        responder(['ok' => true, 'usuario' => usuario_publico(usuario_actual())]);
    }

    if ($a === 'admin') {
        // Lista de cuentas y pagos para el dueño del sitio. Nunca incluye contraseñas.
        $tok = ajuste('MQP_ADMIN_TOKEN', 'admin_token');
        if (strlen($tok) < 16) fallo('Acción desconocida.', 404);
        limitar_login('admin');
        $dado = (string)($_GET['token'] ?? ($_SERVER['HTTP_X_ADMIN_TOKEN'] ?? ''));
        if (!hash_equals($tok, $dado)) { anotar_intento('admin'); fallo('No autorizado.', 401); }
        $db = db();
        $us = $db->query('SELECT u.id, u.nombre, u.correo, u.universidad, u.examen, u.creado,
            (SELECT COUNT(*) FROM pagos p WHERE p.usuario = u.id) AS pagos, (SELECT COALESCE(SUM(monto),0) FROM pagos p WHERE p.usuario = u.id) AS total_soles,
            (SELECT group_concat(examen || \':\' || plan || \' hasta \' || date(hasta, \'unixepoch\'), \' | \') FROM suscripciones s WHERE s.usuario = u.id AND s.hasta > strftime(\'%s\',\'now\')) AS planes,
            (SELECT group_concat(examen, \', \') FROM lista_espera w WHERE w.usuario = u.id) AS espera
            FROM usuarios u ORDER BY u.id')->fetchAll();
        $f = fn($t) => $t ? date('Y-m-d H:i', (int)$t) : '';
        $filas = array_map(fn($u) => [
            'id' => (int)$u['id'], 'nombre' => $u['nombre'], 'correo' => $u['correo'], 'universidad' => $u['universidad'], 'examen' => $u['examen'],
            'registrado' => $f($u['creado']), 'planes_activos' => (string)$u['planes'], 'lista_de_espera' => (string)$u['espera'],
            'pagos' => (int)$u['pagos'], 'total_soles' => (float)$u['total_soles'],
        ], $us);
        if (($_GET['formato'] ?? 'csv') === 'json') responder(['ok' => true, 'total' => count($filas), 'cuentas' => $filas]);
        header('Content-Type: text/csv; charset=utf-8'); header('Content-Disposition: attachment; filename="cuentas-medquizplus-' . date('Ymd') . '.csv"'); header('Cache-Control: no-store');
        $o = fopen('php://output', 'w'); fwrite($o, "\xEF\xBB\xBF");                       // BOM: Excel abre bien las tildes
        fputcsv($o, array_keys($filas[0] ?? ['id' => '', 'nombre' => '', 'correo' => '', 'universidad' => '', 'examen' => '', 'registrado' => '', 'planes_activos' => '', 'lista_de_espera' => '', 'pagos' => '', 'total_soles' => '']));
        foreach ($filas as $r) fputcsv($o, array_map(fn($v) => is_string($v) && preg_match('/^[=+\-@\t\r]/', $v) ? "'" . $v : $v, $r));   // evita fórmulas de Excel en datos escritos por usuarios
        fclose($o); exit;
    }

    if ($a === 'estado') {
        responder(['ok' => true, 'cuentas' => true, 'pagos' => pagos_activos(), 'pasarela' => pasarela(), 'limites' => limites_activos(),
            'limite_diario' => LIMITE_GRATIS_DIARIO, 'periodos' => PERIODOS, 'examenes' => EXAMENES]);
    }

    if ($a === 'me') {
        responder(['ok' => true, 'usuario' => usuario_publico(usuario_actual())]);
    }

    if ($a === 'registro') {
        exigir_post_del_sitio();
        $d = cuerpo();
        $nombre = trim((string)($d['nombre'] ?? ''));
        $correo = strtolower(trim((string)($d['correo'] ?? '')));
        $clave = (string)($d['clave'] ?? '');
        $examen = in_array($d['examen'] ?? '', ['enam', 'residentado', 'essalud', 'encaps'], true) ? $d['examen'] : null;
        $uni = mb_substr(trim((string)($d['universidad'] ?? '')), 0, 120);
        if (($d['acepto'] ?? false) !== true) fallo('Para crear tu cuenta debes aceptar la política de privacidad y los términos y condiciones.');
        if (mb_strlen($nombre) < 2 || mb_strlen($nombre) > 80) fallo('Escribe tu nombre.');
        if (!filter_var($correo, FILTER_VALIDATE_EMAIL) || strlen($correo) > 120) fallo('Revisa el correo electrónico.');
        if (strlen($clave) < MIN_CLAVE || strlen($clave) > 200) fallo('La contraseña debe tener al menos ' . MIN_CLAVE . ' caracteres.');
        $db = db();
        $ex = $db->prepare('SELECT 1 FROM usuarios WHERE correo = ?'); $ex->execute([$correo]);
        if ($ex->fetch()) fallo('Ya existe una cuenta con ese correo. Prueba ingresando.', 409);
        $db->prepare('INSERT INTO usuarios(correo, nombre, clave, examen, universidad, creado, acepto_en) VALUES (?,?,?,?,?,?,?)')
           ->execute([$correo, $nombre, password_hash($clave, PASSWORD_DEFAULT), $examen, $uni, time(), time()]);
        iniciar_sesion(); session_regenerate_id(true);
        $_SESSION['uid'] = (int)$db->lastInsertId();
        responder(['ok' => true, 'usuario' => usuario_publico(usuario_actual())], 201);
    }

    if ($a === 'ingresar') {
        exigir_post_del_sitio();
        $d = cuerpo();
        $correo = strtolower(trim((string)($d['correo'] ?? '')));
        $clave = (string)($d['clave'] ?? '');
        limitar_login($correo);
        $st = db()->prepare('SELECT * FROM usuarios WHERE correo = ?'); $st->execute([$correo]);
        $u = $st->fetch();
        if (!$u || !password_verify($clave, $u['clave'])) { anotar_intento($correo); fallo('Correo o contraseña incorrectos.', 401); }
        iniciar_sesion(); session_regenerate_id(true);
        $_SESSION['uid'] = (int)$u['id'];
        responder(['ok' => true, 'usuario' => usuario_publico($u)]);
    }

    if ($a === 'progreso_leer') {
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión.', 401);
        $st = db()->prepare('SELECT datos, actualizado FROM progreso WHERE usuario = ?'); $st->execute([(int)$u['id']]);
        $f = $st->fetch();
        responder(['ok' => true, 'datos' => $f ? json_decode($f['datos'], true) : null, 'actualizado' => $f ? (int)$f['actualizado'] : null]);
    }

    if ($a === 'progreso_guardar') {
        exigir_post_del_sitio();
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión.', 401);
        $raw = file_get_contents('php://input') ?: '';
        if (strlen($raw) > 1500000) fallo('El progreso es demasiado grande.', 413);
        $d = json_decode($raw, true)['datos'] ?? null;
        if (!is_array($d) || ($d['v'] ?? 0) !== 1 || !is_array($d['respuestas'] ?? null)) fallo('Datos de progreso no válidos.');
        if (count($d['respuestas']) > 20000 || count($d['sesiones'] ?? []) > 500) fallo('El progreso es demasiado grande.', 413);
        // solo se guarda la estructura conocida (nada de campos arbitrarios)
        $limpio = ['v' => 1, 'respuestas' => $d['respuestas'], 'favoritos' => is_array($d['favoritos'] ?? null) ? $d['favoritos'] : new stdClass(),
            'sesiones' => is_array($d['sesiones'] ?? null) ? $d['sesiones'] : [], 'ultima' => $d['ultima'] ?? null,
            'preferencias' => is_array($d['preferencias'] ?? null) ? $d['preferencias'] : new stdClass(),
            'borrados' => is_array($d['borrados'] ?? null) ? $d['borrados'] : new stdClass(), 'reinicioGlobal' => (int)($d['reinicioGlobal'] ?? 0)];
        db()->prepare('INSERT INTO progreso(usuario, datos, actualizado) VALUES (?,?,?) ON CONFLICT(usuario) DO UPDATE SET datos = excluded.datos, actualizado = excluded.actualizado')
            ->execute([(int)$u['id'], json_encode($limpio, JSON_UNESCAPED_UNICODE), time()]);
        responder(['ok' => true, 'actualizado' => time()]);
    }

    if ($a === 'exportar') {
        exigir_post_del_sitio();
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión.', 401);
        $db = db();
        $p = $db->prepare('SELECT datos, actualizado FROM progreso WHERE usuario = ?'); $p->execute([(int)$u['id']]); $pr = $p->fetch();
        $pg = $db->prepare('SELECT examen, plan, monto, creado FROM pagos WHERE usuario = ? ORDER BY id'); $pg->execute([(int)$u['id']]);
        header('Content-Disposition: attachment; filename="mis-datos-medquizplus.json"');
        responder(['ok' => true, 'generado' => date('c'), 'cuenta' => [
            'nombre' => $u['nombre'], 'correo' => $u['correo'], 'universidad' => $u['universidad'], 'examen' => $u['examen'],
            'registrada' => date('c', (int)$u['creado']), 'acepto_politica' => $u['acepto_en'] ? date('c', (int)$u['acepto_en']) : null,
            'suscripciones_activas' => (object)suscripciones_de((int)$u['id'])],
            'pagos' => array_map(fn($x) => ['examen' => $x['examen'], 'plan' => $x['plan'], 'monto_soles' => (float)$x['monto'], 'fecha' => date('c', (int)$x['creado'])], $pg->fetchAll()),
            'progreso' => $pr ? json_decode($pr['datos'], true) : null,
            'flashcards' => (function () use ($db, $u) { $q = $db->prepare('SELECT frente, dorso, pregunta, tema, especialidad, fuente, estado, intervalo, repeticiones, lapsos, creado, ultimo, proximo FROM flashcards WHERE usuario = ?'); $q->execute([(int)$u['id']]); return $q->fetchAll(); })(),
            'feynman' => (function () use ($db, $u) {      // Tutor Feynman IA: sesiones y transcripciones del propio estudiante (la tabla existe solo si lo usó)
                try {
                    $q = $db->prepare('SELECT id, origen, pregunta_id, tema, especialidad, estado, fase, creado, actualizado FROM feynman_sesiones WHERE usuario = ? ORDER BY creado'); $q->execute([(int)$u['id']]);
                    $t = $db->prepare('SELECT n, rol, texto, via, fase, creado FROM feynman_turnos WHERE sesion = ? ORDER BY n');
                    return array_map(function ($s) use ($t) { $t->execute([$s['id']]); return $s + ['turnos' => $t->fetchAll()]; }, $q->fetchAll());
                } catch (Throwable $e) { return []; }
            })()]);
    }

    if ($a === 'eliminar') {
        exigir_post_del_sitio();
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión.', 401);
        limitar_login((string)$u['correo']);
        if (!password_verify((string)(cuerpo()['clave'] ?? ''), $u['clave'])) { anotar_intento((string)$u['correo']); fallo('La contraseña no es correcta.', 401); }
        $db = db(); $db->beginTransaction();
        $db->prepare('DELETE FROM progreso WHERE usuario = ?')->execute([(int)$u['id']]);
        $db->prepare('DELETE FROM usuarios WHERE id = ?')->execute([(int)$u['id']]);   // los registros de pago se conservan sin datos personales (obligación contable)
        $db->commit();
        iniciar_sesion(); $_SESSION = []; session_destroy();
        responder(['ok' => true]);
    }

    if ($a === 'espera') {
        exigir_post_del_sitio();
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión para unirte a la lista de espera.', 401);
        $examen = (string)(cuerpo()['examen'] ?? '');
        if (!isset(EXAMENES[$examen])) fallo('Examen no válido.');
        db()->prepare('INSERT OR IGNORE INTO lista_espera(usuario, examen, creado) VALUES (?,?,?)')->execute([(int)$u['id'], $examen, time()]);
        responder(['ok' => true, 'usuario' => usuario_publico(usuario_actual())]);
    }

    /* ====================== FLASHCARDS ====================== */

    if (strncmp($a, 'fc_', 3) === 0) {
        $u = usuario_actual(); if (!$u) fallo('Inicia sesión para usar tus flashcards.', 401);
        $uid = (int)$u['id']; $db = db(); $ahora = time();
        $corto = fn($v, int $n) => mb_substr(trim(preg_replace('/[ \t]+/u', ' ', (string)$v)), 0, $n);
        $fila = fn(array $f) => [
            'id' => (int)$f['id'], 'frente' => $f['frente'], 'dorso' => $f['dorso'], 'pregunta' => $f['pregunta'], 'tema' => $f['tema'],
            'especialidad' => $f['especialidad'], 'fuente' => $f['fuente'], 'estado' => $f['estado'], 'intervalo' => (int)$f['intervalo'],
            'repeticiones' => (int)$f['repeticiones'], 'lapsos' => (int)$f['lapsos'], 'creado' => (int)$f['creado'],
            'ultimo' => (int)$f['ultimo'], 'proximo' => (int)$f['proximo'],
        ];

        if ($a === 'fc_crear') {
            exigir_post_del_sitio(); limitar_ritmo($uid, 'fc_crear', 20);
            $lista = cuerpo()['tarjetas'] ?? null;
            if (!is_array($lista) || !$lista || count($lista) > 8) fallo('Envía entre 1 y 8 tarjetas.');
            $tot = $db->prepare('SELECT COUNT(*) FROM flashcards WHERE usuario = ?'); $tot->execute([$uid]);
            if ((int)$tot->fetchColumn() + count($lista) > 3000) fallo('Llegaste al máximo de 3000 flashcards.', 409);
            $creadas = []; $repetidas = 0;
            $ins = $db->prepare('INSERT OR IGNORE INTO flashcards(usuario, frente, dorso, pregunta, tema, especialidad, fuente, huella, creado, proximo) VALUES (?,?,?,?,?,?,?,?,?,?)');
            $db->beginTransaction();
            foreach ($lista as $t) {
                if (!is_array($t)) continue;
                $fr = $corto($t['frente'] ?? '', 600); $do = trim((string)($t['dorso'] ?? '')); $do = mb_substr($do, 0, 1500);
                if (mb_strlen($fr) < 5 || mb_strlen($do) < 2) { $db->rollBack(); fallo('Cada tarjeta necesita frente y dorso.'); }
                $pre = $corto($t['pregunta'] ?? '', 40);
                $ins->execute([$uid, $fr, $do, $pre, $corto($t['tema'] ?? '', 120), $corto($t['especialidad'] ?? '', 80), $corto($t['fuente'] ?? '', 400), fc_huella($pre, $fr), $ahora, $ahora]);
                if ($ins->rowCount()) $creadas[] = (int)$db->lastInsertId(); else $repetidas++;
            }
            $db->commit();
            responder(['ok' => true, 'creadas' => count($creadas), 'repetidas' => $repetidas], 201);
        }

        if ($a === 'fc_listar') {
            $st = $db->prepare('SELECT * FROM flashcards WHERE usuario = ? ORDER BY creado DESC, id DESC LIMIT 3000'); $st->execute([$uid]);
            $tarjetas = array_map($fila, $st->fetchAll());
            $c = $db->prepare('SELECT COUNT(*) FROM flashcards WHERE usuario = ? AND proximo <= ?'); $c->execute([$uid, $ahora]);
            $hoy = $db->prepare('SELECT COUNT(*) FROM repasos WHERE usuario = ? AND t >= ?'); $hoy->execute([$uid, strtotime('today')]);
            responder(['ok' => true, 'tarjetas' => $tarjetas, 'pendientes' => (int)$c->fetchColumn(), 'repasadas_hoy' => (int)$hoy->fetchColumn(), 'ahora' => $ahora]);
        }

        if ($a === 'fc_cola') {
            $st = $db->prepare('SELECT * FROM flashcards WHERE usuario = ? AND proximo <= ? ORDER BY proximo ASC, id ASC LIMIT 20'); $st->execute([$uid, $ahora]);
            $cola = array_map(fn($f) => $fila($f) + ['previas' => fc_previas($f, $ahora)], $st->fetchAll());
            $c = $db->prepare('SELECT COUNT(*) FROM flashcards WHERE usuario = ? AND proximo <= ?'); $c->execute([$uid, $ahora]);
            responder(['ok' => true, 'cola' => $cola, 'pendientes' => (int)$c->fetchColumn(), 'ahora' => $ahora]);
        }

        if ($a === 'fc_repasar') {
            exigir_post_del_sitio(); limitar_ritmo($uid, 'fc_repasar', 150);
            $d = cuerpo(); $id = (int)($d['id'] ?? 0); $cal = (string)($d['calificacion'] ?? '');
            if (!in_array($cal, FC_CALIFICACIONES, true)) fallo('Calificación no válida.');
            $st = $db->prepare('SELECT * FROM flashcards WHERE id = ? AND usuario = ?'); $st->execute([$id, $uid]); $t = $st->fetch();
            if (!$t) fallo('No encontramos esa tarjeta.', 404);
            if ((int)($d['ultimo'] ?? -1) !== (int)$t['ultimo']) fallo('Esa tarjeta ya se repasó (quizá en otra pestaña). Recarga la lista.', 409);   // evita contar dos veces un doble clic
            $n = fc_planificar($t, $cal, $ahora);
            $db->beginTransaction();
            $db->prepare('UPDATE flashcards SET estado=?, facilidad=?, intervalo=?, repeticiones=?, lapsos=?, ultimo=?, proximo=? WHERE id=? AND usuario=?')
               ->execute([$n['estado'], $n['facilidad'], $n['intervalo'], $n['repeticiones'], $n['lapsos'], $ahora, $n['proximo'], $id, $uid]);
            $db->prepare('INSERT INTO repasos(tarjeta, usuario, t, calificacion, estado_antes, intervalo_antes, intervalo_despues) VALUES (?,?,?,?,?,?,?)')
               ->execute([$id, $uid, $ahora, $cal, $t['estado'], (int)$t['intervalo'], $n['intervalo']]);
            $db->commit();
            responder(['ok' => true, 'proximo' => $n['proximo'], 'estado' => $n['estado'], 'ultimo' => $ahora]);
        }

        if ($a === 'fc_editar') {
            exigir_post_del_sitio(); limitar_ritmo($uid, 'fc_editar', 60);
            $d = cuerpo(); $id = (int)($d['id'] ?? 0);
            $fr = $corto($d['frente'] ?? '', 600); $do = mb_substr(trim((string)($d['dorso'] ?? '')), 0, 1500);
            if (mb_strlen($fr) < 5 || mb_strlen($do) < 2) fallo('Cada tarjeta necesita frente y dorso.');
            $st = $db->prepare('UPDATE flashcards SET frente = ?, dorso = ? WHERE id = ? AND usuario = ?'); $st->execute([$fr, $do, $id, $uid]);
            if (!$st->rowCount()) fallo('No encontramos esa tarjeta.', 404);
            responder(['ok' => true]);
        }

        if ($a === 'fc_borrar') {
            exigir_post_del_sitio(); limitar_ritmo($uid, 'fc_borrar', 60);
            $st = $db->prepare('DELETE FROM flashcards WHERE id = ? AND usuario = ?'); $st->execute([(int)(cuerpo()['id'] ?? 0), $uid]);
            if (!$st->rowCount()) fallo('No encontramos esa tarjeta.', 404);
            responder(['ok' => true]);
        }

        if ($a === 'fc_exportar') {
            $st = $db->prepare('SELECT frente, dorso, especialidad, tema, fuente FROM flashcards WHERE usuario = ? ORDER BY id'); $st->execute([$uid]);
            header('Content-Type: text/csv; charset=utf-8'); header('Content-Disposition: attachment; filename="mis-flashcards-medquizplus.csv"'); header('Cache-Control: no-store');
            $o = fopen('php://output', 'w'); fwrite($o, "\xEF\xBB\xBF");
            fputcsv($o, ['Frente', 'Dorso', 'Etiquetas', 'Fuente']);                      // en Anki: Archivo → Importar; columnas 1 y 2 = frente y dorso
            $seg = fn($v) => is_string($v) && preg_match('/^[=+\-@\t\r]/', $v) ? "'" . $v : $v;
            foreach ($st->fetchAll() as $f) fputcsv($o, [$seg($f['frente']), $seg($f['dorso']), str_replace(' ', '_', trim($f['especialidad'] . ' ' . $f['tema'])), $seg($f['fuente'])]);
            fclose($o); exit;
        }

        fallo('Acción desconocida.', 404);
    }

    if ($a === 'salir') {
        exigir_post_del_sitio();
        iniciar_sesion(); $_SESSION = []; session_destroy();
        responder(['ok' => true]);
    }

    if ($a === 'comprar') {
        exigir_post_del_sitio();
        $u = usuario_actual();
        if (!$u) fallo('Inicia sesión para comprar un plan.', 401);
        if (!pagos_activos()) fallo('El cobro en línea todavía no está activo.', 503);
        $d = cuerpo();
        $examen = (string)($d['examen'] ?? 'enam'); $plan = (string)($d['plan'] ?? '');
        $p = plan_info($examen, $plan);
        if (!$p) fallo('Plan no válido.');
        if (!$p['abierto']) fallo('El banco de ' . EXAMENES[$examen]['nombre'] . ' todavía está en construcción, por eso aún no se vende. Únete a la lista de espera y te avisamos cuando abra.', 409);
        $site = url_sitio();
        if (pasarela() === 'payu') {
            $merchant = ajuste('PAYU_MERCHANT_ID', 'payu_merchant_id'); $key = ajuste('PAYU_API_KEY', 'payu_api_key');
            $ref = 'mqp-' . $u['id'] . '-' . $examen . '-' . $plan . '-' . bin2hex(random_bytes(5));      // única por intento
            $monto = number_format($p['soles'], 2, '.', '');
            db()->prepare('INSERT INTO ordenes(ref, usuario, plan, monto, creado, examen) VALUES (?,?,?,?,?,?)')->execute([$ref, (int)$u['id'], $plan, $p['soles'], time(), $examen]);
            $test = ajuste('PAYU_TEST', 'payu_test') === '1';
            responder(['ok' => true, 'form' => [
                'action' => $test ? 'https://sandbox.checkout.payulatam.com/ppp-web-gateway-payu/' : 'https://checkout.payulatam.com/ppp-web-gateway-payu/',
                'fields' => [
                    'merchantId' => $merchant, 'accountId' => ajuste('PAYU_ACCOUNT_ID', 'payu_account_id'),
                    'description' => 'MedQuizPlus · ' . $p['nombre'], 'referenceCode' => $ref, 'amount' => $monto,
                    'tax' => '0', 'taxReturnBase' => '0', 'currency' => 'PEN',
                    'signature' => md5($key . '~' . $merchant . '~' . $ref . '~' . $monto . '~PEN'),
                    'test' => $test ? '1' : '0', 'buyerEmail' => $u['correo'],
                    'responseUrl' => $site . '/cuenta.php?a=retorno', 'confirmationUrl' => $site . '/cuenta.php?a=payu',
                ],
            ]]);
        }
        $r = mp('POST', '/checkout/preferences', [
            'items' => [['title' => 'MedQuizPlus · ' . $p['nombre'], 'quantity' => 1, 'unit_price' => $p['soles'], 'currency_id' => 'PEN']],
            'payer' => ['email' => $u['correo']],
            'external_reference' => $u['id'] . '|' . $examen . '|' . $plan,
            'back_urls' => ['success' => $site . '/app/#/inicio?pago=ok', 'pending' => $site . '/app/#/planes?pago=pendiente', 'failure' => $site . '/app/#/planes?pago=error'],
            'auto_return' => 'approved',
            'notification_url' => $site . '/cuenta.php?a=webhook',
        ]);
        $url = $r['datos']['init_point'] ?? '';
        if ($r['codigo'] >= 300 || $url === '') { error_log('[cuenta] MP preferencia: HTTP ' . $r['codigo'] . ' ' . json_encode($r['datos'])); fallo('No pudimos iniciar el pago. Inténtalo de nuevo en un momento.', 502); }
        responder(['ok' => true, 'url' => $url]);
    }

    if ($a === 'retorno') {
        // PayU devuelve aquí al estudiante (GET). Esto NO activa nada: solo lo manda a la pantalla correcta.
        $estado = (string)($_GET['transactionState'] ?? '');
        $dest = $estado === '4' ? '/app/#/inicio?pago=ok' : ($estado === '7' ? '/app/#/planes?pago=pendiente' : '/app/#/planes?pago=error');
        header('Location: ' . url_sitio() . $dest, true, 302);
        exit;
    }

    if ($a === 'payu') {
        // Confirmación servidor a servidor de PayU (application/x-www-form-urlencoded). Se verifica la firma con la ApiKey.
        if (pasarela() !== 'payu') responder(['ok' => true]);
        $f = $_POST;
        $ref = (string)($f['reference_sale'] ?? ''); $valor = (string)($f['value'] ?? ''); $mon = (string)($f['currency'] ?? '');
        $estado = (string)($f['state_pol'] ?? ''); $sign = strtolower((string)($f['sign'] ?? $f['signature'] ?? ''));
        $merchant = ajuste('PAYU_MERCHANT_ID', 'payu_merchant_id'); $key = ajuste('PAYU_API_KEY', 'payu_api_key');
        if ((string)($f['merchant_id'] ?? '') !== $merchant) responder(['ok' => false], 400);
        // PayU firma el valor con UN decimal cuando el segundo es cero (150.00 → 150.0)
        $v = number_format((float)$valor, 2, '.', ''); if (substr($v, -1) === '0') $v = substr($v, 0, -1);
        $calc = md5($key . '~' . $merchant . '~' . $ref . '~' . $v . '~' . $mon . '~' . $estado);
        if (!hash_equals($calc, $sign)) { error_log('[cuenta] confirmación PayU con firma inválida'); responder(['ok' => false], 400); }
        if ($estado !== '4') responder(['ok' => true]);             // 4 = aprobada; el resto no activa nada
        $st = db()->prepare('SELECT * FROM ordenes WHERE ref = ?'); $st->execute([$ref]);
        $o = $st->fetch();
        if (!$o) { error_log('[cuenta] PayU: referencia desconocida ' . $ref); responder(['ok' => true]); }
        if ($mon !== 'PEN' || (float)$valor + 0.001 < (float)$o['monto']) { error_log('[cuenta] PayU: monto/moneda inesperados en ' . $ref); responder(['ok' => true]); }
        $tx = (string)($f['transaction_id'] ?? $f['reference_pol'] ?? '');
        if ($tx === '') responder(['ok' => true]);
        activar_plan((int)$o['usuario'], (string)$o['examen'], (string)$o['plan'], 'payu:' . $tx, (float)$valor);
        responder(['ok' => true]);
    }

    if ($a === 'webhook') {
        // Mercado Pago avisa con ?type=payment&data.id=... (o JSON). Siempre se responde 200 para que no reintente sin fin.
        $d = cuerpo();
        $tipo = (string)($_GET['type'] ?? $_GET['topic'] ?? $d['type'] ?? '');
        $id = (string)($_GET['data_id'] ?? $_GET['data.id'] ?? $_GET['id'] ?? ($d['data']['id'] ?? ''));
        if ($tipo !== 'payment' || !preg_match('/^\d{3,20}$/', $id) || !pagos_activos()) responder(['ok' => true]);
        if (!firma_valida($id)) { error_log('[cuenta] webhook con firma inválida'); responder(['ok' => false], 401); }
        $r = mp('GET', '/v1/payments/' . $id);
        $pg = $r['datos'];
        if ($r['codigo'] !== 200 || ($pg['status'] ?? '') !== 'approved') responder(['ok' => true]);
        $ref = explode('|', (string)($pg['external_reference'] ?? ''));
        $uid = (int)($ref[0] ?? 0);
        $examen = count($ref) >= 3 ? (string)$ref[1] : 'enam'; $plan = (string)($ref[count($ref) >= 3 ? 2 : 1] ?? '');   // referencias antiguas: "uid|plan" (ENAM)
        $info = plan_info($examen, $plan);
        if (!$uid || !$info) { error_log('[cuenta] pago ' . $id . ' con referencia desconocida'); responder(['ok' => true]); }
        $monto = (float)($pg['transaction_amount'] ?? 0);
        if (($pg['currency_id'] ?? '') !== 'PEN' || $monto + 0.001 < $info['soles']) { error_log('[cuenta] pago ' . $id . ' con monto/moneda inesperados'); responder(['ok' => true]); }
        activar_plan($uid, $examen, $plan, $id, $monto);
        responder(['ok' => true]);
    }

    fallo('Acción desconocida.', 404);
} catch (Throwable $e) {
    error_log('[cuenta] ' . $e->getMessage());
    fallo('Algo salió mal. Inténtalo de nuevo en un momento.', 500);
}
