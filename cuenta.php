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
 *   comprar    (POST)  crea el cobro (PayU o Mercado Pago) y devuelve cómo ir a pagar
 *   webhook    (POST)  aviso de Mercado Pago: se verifica el pago y se activa el plan
 *   payu       (POST)  confirmación de PayU: se verifica la firma y se activa el plan
 *   retorno    (GET)   a donde PayU devuelve al estudiante; solo lo redirige al app
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
 *   MP_API_BASE         solo para pruebas: otra URL para la API de Mercado Pago
 *
 * Los datos viven en cuenta_datos/mqp.sqlite (la carpeta se protege con su propio .htaccess).
 */

declare(strict_types=1);

/* ====================== AJUSTES ====================== */

/** Planes de pago único (sin renovación automática). Precios en soles. */
const PLANES = [
    'mensual'    => ['nombre' => 'Premium mensual',    'soles' => 29.00,  'dias' => 30],
    'trimestral' => ['nombre' => 'Premium trimestral', 'soles' => 69.00,  'dias' => 90],
    'anual'      => ['nombre' => 'Premium anual',      'soles' => 199.00, 'dias' => 365],
];
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
    $pdo->exec('CREATE TABLE IF NOT EXISTS pagos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, mp_id TEXT NOT NULL UNIQUE, usuario INTEGER NOT NULL,
        plan TEXT NOT NULL, monto REAL NOT NULL, creado INTEGER NOT NULL)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS ordenes (
        ref TEXT PRIMARY KEY, usuario INTEGER NOT NULL, plan TEXT NOT NULL, monto REAL NOT NULL, creado INTEGER NOT NULL)');
    $pdo->exec('CREATE TABLE IF NOT EXISTS intentos (clave TEXT NOT NULL, t INTEGER NOT NULL)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_intentos ON intentos(clave, t)');
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

function usuario_publico(?array $u): ?array {
    if (!$u) return null;
    $vigente = (int)$u['premium_hasta'] > time();
    return [
        'id' => (int)$u['id'], 'nombre' => $u['nombre'], 'correo' => $u['correo'], 'examen' => $u['examen'],
        'premium' => $vigente, 'plan' => $vigente ? $u['plan'] : null,
        'premium_hasta' => $vigente ? (int)$u['premium_hasta'] : null,
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

function activar_plan(int $uid, string $plan, string $mpId, float $monto): void {
    $db = db();
    $db->beginTransaction();
    try {
        $ya = $db->prepare('SELECT 1 FROM pagos WHERE mp_id = ?'); $ya->execute([$mpId]);
        if ($ya->fetch()) { $db->commit(); return; }       // el aviso puede llegar repetido: se activa una sola vez
        $u = $db->prepare('SELECT premium_hasta FROM usuarios WHERE id = ?'); $u->execute([$uid]);
        $f = $u->fetch();
        if (!$f) { $db->rollBack(); return; }
        $desde = max(time(), (int)$f['premium_hasta']);    // renovar suma al tiempo que ya tenía
        $hasta = $desde + PLANES[$plan]['dias'] * 86400;
        $db->prepare('UPDATE usuarios SET plan = ?, premium_hasta = ? WHERE id = ?')->execute([$plan, $hasta, $uid]);
        $db->prepare('INSERT INTO pagos(mp_id, usuario, plan, monto, creado) VALUES (?,?,?,?,?)')->execute([$mpId, $uid, $plan, $monto, time()]);
        $db->commit();
    } catch (Throwable $e) { $db->rollBack(); throw $e; }
}

/* ====================== ACCIONES ====================== */

try {
    $a = (string)($_GET['a'] ?? '');

    if ($a === 'estado') {
        responder(['ok' => true, 'cuentas' => true, 'pagos' => pagos_activos(), 'pasarela' => pasarela(), 'limites' => limites_activos(),
            'limite_diario' => LIMITE_GRATIS_DIARIO, 'planes' => PLANES]);
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
        $examen = in_array($d['examen'] ?? '', ['enam', 'residentado', 'essalud'], true) ? $d['examen'] : null;
        $uni = mb_substr(trim((string)($d['universidad'] ?? '')), 0, 120);
        if (mb_strlen($nombre) < 2 || mb_strlen($nombre) > 80) fallo('Escribe tu nombre.');
        if (!filter_var($correo, FILTER_VALIDATE_EMAIL) || strlen($correo) > 120) fallo('Revisa el correo electrónico.');
        if (strlen($clave) < MIN_CLAVE || strlen($clave) > 200) fallo('La contraseña debe tener al menos ' . MIN_CLAVE . ' caracteres.');
        $db = db();
        $ex = $db->prepare('SELECT 1 FROM usuarios WHERE correo = ?'); $ex->execute([$correo]);
        if ($ex->fetch()) fallo('Ya existe una cuenta con ese correo. Prueba ingresando.', 409);
        $db->prepare('INSERT INTO usuarios(correo, nombre, clave, examen, universidad, creado) VALUES (?,?,?,?,?,?)')
           ->execute([$correo, $nombre, password_hash($clave, PASSWORD_DEFAULT), $examen, $uni, time()]);
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
        $plan = (string)(cuerpo()['plan'] ?? '');
        if (!isset(PLANES[$plan])) fallo('Plan no válido.');
        $p = PLANES[$plan];
        $site = url_sitio();
        if (pasarela() === 'payu') {
            $merchant = ajuste('PAYU_MERCHANT_ID', 'payu_merchant_id'); $key = ajuste('PAYU_API_KEY', 'payu_api_key');
            $ref = 'mqp-' . $u['id'] . '-' . $plan . '-' . bin2hex(random_bytes(5));      // única por intento
            $monto = number_format($p['soles'], 2, '.', '');
            db()->prepare('INSERT INTO ordenes(ref, usuario, plan, monto, creado) VALUES (?,?,?,?,?)')->execute([$ref, (int)$u['id'], $plan, $p['soles'], time()]);
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
            'external_reference' => $u['id'] . '|' . $plan,
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
        activar_plan((int)$o['usuario'], (string)$o['plan'], 'payu:' . $tx, (float)$valor);
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
        $uid = (int)($ref[0] ?? 0); $plan = (string)($ref[1] ?? '');
        if (!$uid || !isset(PLANES[$plan])) { error_log('[cuenta] pago ' . $id . ' con referencia desconocida'); responder(['ok' => true]); }
        $monto = (float)($pg['transaction_amount'] ?? 0);
        if (($pg['currency_id'] ?? '') !== 'PEN' || $monto + 0.001 < PLANES[$plan]['soles']) { error_log('[cuenta] pago ' . $id . ' con monto/moneda inesperados'); responder(['ok' => true]); }
        activar_plan($uid, $plan, $id, $monto);
        responder(['ok' => true]);
    }

    fallo('Acción desconocida.', 404);
} catch (Throwable $e) {
    error_log('[cuenta] ' . $e->getMessage());
    fallo('Algo salió mal. Inténtalo de nuevo en un momento.', 500);
}
