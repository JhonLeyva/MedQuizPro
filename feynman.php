<?php
/**
 * feynman.php — API del Tutor Feynman IA.
 *
 *  GET  ?a=estado                      ¿IA configurada?, especialidades del banco, rúbrica (sin sesión)
 *  GET  ?a=listar                      mis sesiones
 *  GET  ?a=ver&id=…                    una sesión (solo la mía) con su conversación, panel e informe
 *  POST ?a=crear                       {origen: pregunta|flujograma|tema, pregunta_id?, elegida?, flujograma?, tema?, especialidad?, nueva?}
 *  POST ?a=turno                       {id, req_id, accion: responder|pista|explicacion, texto?, via: texto|voz}
 *  POST ?a=finalizar                   {id}            cierra la sesión y calcula el informe
 *  POST ?a=otro_caso                   {id, req_id}    sesión completada → nuevo caso de aplicación
 *  POST ?a=reanudar                    {id}            sesión incompleta → activa
 *  POST ?a=tarjetas                    {id, decisiones:[{i, estado: guardada|descartada}]}
 *  POST ?a=borrar                      {id}
 *
 * Seguridad: sesión de cuenta.php (cookie mqp_sid) + plan activo (como el tutor de IA); POST con cabecera X-MQP y mismo origen;
 * cada consulta filtra por usuario; la llave de IA nunca sale del servidor; el navegador no puede escribir evaluaciones ni fases.
 * Variables: AI_API_KEY, AI_PROVIDER, AI_MODEL, AI_BASE_URL (las del tutor), FEYNMAN_AI_MODEL, FEYNMAN_LIMITE_MINUTO (8),
 * FEYNMAN_LIMITE_DIA (150 llamadas), FEYNMAN_PRESUPUESTO_CARACTERES_DIA (300000), FEYNMAN_TIMEOUT (50 s).
 */
declare(strict_types=1);

require_once __DIR__ . '/feynman_lib.php';

ignore_user_abort(true);   // si el navegador cancela, la llamada en curso termina y se guarda completa o no se guarda: nunca a medias
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');
header('Referrer-Policy: same-origin');

const FY_MSG_GENERICO = 'No pude procesar tu mensaje. Inténtalo de nuevo en un momento.';
const FY_MAX_SESIONES = 50;
const FY_MAX_TURNOS_TOTAL = 90;

function fy_resp(array $d, int $codigo = 200): never
{
    http_response_code($codigo);
    echo json_encode($d, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}
/** Error controlado: se lanza (no exit) para que los bloques finally liberen el bloqueo de la sesión. */
final class FyError extends RuntimeException {}
function fy_fallo(string $msg, int $codigo = 400, string $interno = ''): never
{
    if ($interno !== '') { error_log('[feynman] ' . $interno); }
    throw new FyError($msg, $codigo);
}

function fy_db(): PDO
{
    static $pdo = null;
    if ($pdo) { return $pdo; }
    $archivo = __DIR__ . '/cuenta_datos/mqp.sqlite';
    if (!is_file($archivo)) { fy_fallo('Inicia sesión para usar el Tutor Feynman IA.', 401); }
    $pdo = new PDO('sqlite:' . $archivo, null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
    $pdo->exec('PRAGMA foreign_keys=ON; PRAGMA busy_timeout=5000;');
    $pdo->exec("CREATE TABLE IF NOT EXISTS feynman_sesiones (
        id TEXT PRIMARY KEY, usuario INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
        origen TEXT NOT NULL, pregunta_id TEXT NOT NULL DEFAULT '', elegida TEXT NOT NULL DEFAULT '', flujograma TEXT NOT NULL DEFAULT '',
        tema TEXT NOT NULL, especialidad TEXT NOT NULL DEFAULT '', estado TEXT NOT NULL DEFAULT 'activa', fase INTEGER NOT NULL DEFAULT 1,
        datos TEXT NOT NULL, procesando_hasta INTEGER NOT NULL DEFAULT 0, creado INTEGER NOT NULL, actualizado INTEGER NOT NULL, finalizado INTEGER NOT NULL DEFAULT 0)");
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_fy_ses ON feynman_sesiones(usuario, actualizado)');
    $pdo->exec("CREATE TABLE IF NOT EXISTS feynman_turnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, sesion TEXT NOT NULL REFERENCES feynman_sesiones(id) ON DELETE CASCADE,
        n INTEGER NOT NULL, rol TEXT NOT NULL, texto TEXT NOT NULL, via TEXT NOT NULL DEFAULT 'texto', fase INTEGER NOT NULL,
        accion TEXT NOT NULL DEFAULT 'responder', req_id TEXT, meta TEXT NOT NULL DEFAULT '{}', creado INTEGER NOT NULL, UNIQUE (sesion, n))");
    $pdo->exec('CREATE UNIQUE INDEX IF NOT EXISTS ux_fy_req ON feynman_turnos(sesion, req_id) WHERE req_id IS NOT NULL');
    $pdo->exec('CREATE TABLE IF NOT EXISTS feynman_uso (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER NOT NULL, t INTEGER NOT NULL, chars INTEGER NOT NULL DEFAULT 0)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_fy_uso ON feynman_uso(usuario, t)');
    return $pdo;
}

/** Misma sesión de cuenta.php. 401 sin sesión, 402 sin plan activo (igual que el tutor de IA). */
function fy_exigir_usuario(): int
{
    session_name('mqp_sid');
    @session_start(['read_and_close' => true]);
    $uid = (int) ($_SESSION['uid'] ?? 0);
    if ($uid <= 0) { fy_fallo('Inicia sesión para usar el Tutor Feynman IA.', 401); }
    $db = fy_db();
    $st = $db->prepare('SELECT 1 FROM suscripciones WHERE usuario = ? AND hasta > ? LIMIT 1'); $st->execute([$uid, time()]);
    $ok = $st->fetchColumn() !== false;
    if (!$ok) { $st = $db->prepare('SELECT dueno FROM usuarios WHERE id = ?'); $st->execute([$uid]); $ok = (int) $st->fetchColumn() === 1; }
    if (!$ok) { fy_fallo('El Tutor Feynman IA es parte de los planes de pago. Activa un plan para usarlo.', 402); }
    return $uid;
}

function fy_exigir_post(): array
{
    if (strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? '')) !== 'POST') { header('Allow: POST'); fy_fallo('Método no permitido.', 405); }
    if (($_SERVER['HTTP_X_MQP'] ?? '') !== '1') { fy_fallo('Solicitud no válida.', 403); }
    $origen = (string) ($_SERVER['HTTP_ORIGIN'] ?? '');
    if ($origen !== '') {
        $a = strtolower((string) parse_url($origen, PHP_URL_HOST));
        $b = strtolower((string) preg_replace('/:\d+$/', '', (string) ($_SERVER['HTTP_HOST'] ?? '')));
        if ($a !== '' && $b !== '' && $a !== $b) { fy_fallo('Solicitud no válida.', 403, 'origen no permitido'); }
    }
    $crudo = (string) file_get_contents('php://input');
    if (strlen($crudo) > 20000) { fy_fallo('La solicitud es demasiado grande.', 413); }
    $j = json_decode($crudo, true);
    return is_array($j) ? $j : [];
}

function fy_id($v): string
{
    $v = (string) $v;
    if (!preg_match('/^[a-f0-9]{24}$/', $v)) { fy_fallo('No encontramos esa sesión.', 404); }
    return $v;
}

/** Sesión del usuario o 404 (nunca distingue «no existe» de «es de otro»). */
function fy_sesion(PDO $db, int $uid, string $id): array
{
    $st = $db->prepare('SELECT * FROM feynman_sesiones WHERE id = ? AND usuario = ?'); $st->execute([$id, $uid]);
    $f = $st->fetch();
    if (!$f) { fy_fallo('No encontramos esa sesión.', 404); }
    return $f;
}

/* ---------- límites de consumo ---------- */

/** Registra una llamada a la IA y rechaza si se pasó del ritmo, de las llamadas diarias o del presupuesto en caracteres. Devuelve el id del registro. */
function fy_cobrar_llamada(PDO $db, int $uid): int
{
    $ahora = time();
    $db->prepare('DELETE FROM feynman_uso WHERE t < ?')->execute([$ahora - 172800]);
    $q = static function (string $sql, array $p) use ($db): int { $s = $db->prepare($sql); $s->execute($p); return (int) $s->fetchColumn(); };
    $porMinuto = max(1, (int) fy_ajuste('FEYNMAN_LIMITE_MINUTO', 'feynman_limite_minuto', '8'));
    $porDia = max(1, (int) fy_ajuste('FEYNMAN_LIMITE_DIA', 'feynman_limite_dia', '150'));
    $presupuesto = max(5000, (int) fy_ajuste('FEYNMAN_PRESUPUESTO_CARACTERES_DIA', 'feynman_presupuesto_caracteres_dia', '300000'));
    $hoy = strtotime('today');
    if ($q('SELECT COUNT(*) FROM feynman_uso WHERE usuario = ? AND t > ?', [$uid, $ahora - 60]) >= $porMinuto) { header('Retry-After: 60'); fy_fallo('Vas muy rápido. Espera un minuto y continúa.', 429); }
    if ($q('SELECT COUNT(*) FROM feynman_uso WHERE usuario = ? AND t >= ?', [$uid, $hoy]) >= $porDia) { header('Retry-After: 3600'); fy_fallo('Llegaste al límite diario del Tutor Feynman IA. Vuelve mañana; tu práctica sigue funcionando.', 429); }
    if ($q('SELECT COALESCE(SUM(chars),0) FROM feynman_uso WHERE usuario = ? AND t >= ?', [$uid, $hoy]) >= $presupuesto) { header('Retry-After: 3600'); fy_fallo('Llegaste al presupuesto diario de uso de la IA. Vuelve mañana; tu práctica sigue funcionando.', 429); }
    $db->prepare('INSERT INTO feynman_uso(usuario, t, chars) VALUES (?,?,0)')->execute([$uid, $ahora]);
    return (int) $db->lastInsertId();
}
function fy_descontar(PDO $db, int $idUso, int $chars): void { $db->prepare('UPDATE feynman_uso SET chars = ? WHERE id = ?')->execute([max(0, $chars), $idUso]); }

/** Una llamada al modelo con contrato JSON validado; 1 reintento con la corrección. Devuelve los datos validados. */
function fy_llamar_validado(PDO $db, int $uid, string $sistema, array $mensajes, callable $validar, int $maxTok = 1400): array
{
    $uso = fy_cobrar_llamada($db, $uid);
    $chars = 0;
    for ($intento = 0; $intento < 2; $intento++) {
        $r = fy_ia($sistema, $mensajes, $maxTok);
        $chars += mb_strlen($sistema) + mb_strlen(implode('', array_column($mensajes, 'texto'))) + mb_strlen($r['texto']);
        if (!$r['ok']) {
            fy_descontar($db, $uso, $chars);
            if ($r['http'] === 503) { fy_fallo('El Tutor Feynman IA todavía no está configurado en este servidor. Tu práctica y tus flashcards siguen funcionando.', 503, $r['detalle']); }
            fy_fallo($r['http'] === 429 ? 'El tutor está recibiendo muchas consultas ahora mismo. Inténtalo en un minuto.' : 'El servicio de IA no respondió. Inténtalo de nuevo en un momento; tu texto no se perdió.', $r['http'] === 429 ? 429 : 502, $r['detalle']);
        }
        $v = $validar(fy_extraer_json($r['texto']));
        if ($v['ok']) { fy_descontar($db, $uso, $chars); return $v['d'] + ['_crudo' => $r['texto']]; }
        error_log('[feynman] respuesta inválida del modelo (intento ' . ($intento + 1) . '): ' . $v['error']);
        $mensajes[] = ['rol' => 'tutor', 'texto' => mb_substr($r['texto'], 0, 600)];
        $mensajes[] = ['rol' => 'usuario', 'texto' => 'Tu respuesta no es válida: ' . $v['error'] . '. Responde SOLO con el objeto JSON del contrato, respetando la TAREA DEL TURNO.'];
    }
    fy_descontar($db, $uso, $chars);
    fy_fallo('El tutor devolvió una respuesta que no pude usar. Inténtalo de nuevo; tu texto no se perdió.', 502, 'respuesta inválida tras reintento');
}

/* ---------- bloqueo contra duplicados ---------- */

function fy_bloquear(PDO $db, int $uid, string $id): void
{
    $ahora = time();
    $st = $db->prepare('UPDATE feynman_sesiones SET procesando_hasta = ? WHERE id = ? AND usuario = ? AND procesando_hasta < ?');
    $st->execute([$ahora + 90, $id, $uid, $ahora]);
    if ($st->rowCount() !== 1) { fy_fallo('Todavía se está procesando tu mensaje anterior. Espera un momento.', 409); }
}
function fy_liberar(PDO $db, string $id): void { $db->prepare('UPDATE feynman_sesiones SET procesando_hasta = 0 WHERE id = ?')->execute([$id]); }

/* ---------- vista pública de una sesión ---------- */

function fy_turnos(PDO $db, string $id): array
{
    $st = $db->prepare('SELECT n, rol, texto, via, fase, accion, req_id, meta, creado FROM feynman_turnos WHERE sesion = ? ORDER BY n'); $st->execute([$id]);
    return $st->fetchAll();
}

function fy_vista(PDO $db, array $f): array
{
    $e = json_decode($f['datos'], true);
    $turnos = array_map(static function ($t) {
        $m = json_decode($t['meta'], true) ?: [];
        return ['n' => (int) $t['n'], 'rol' => $t['rol'], 'texto' => $t['texto'], 'via' => $t['via'], 'fase' => (int) $t['fase'], 'accion' => $t['accion'], 'creado' => (int) $t['creado'],
            'nivel' => $m['nivel'] ?? null, 'aclaracion' => !empty($m['aclaracion']), 'guias' => $m['guias'] ?? [], 'citadas' => $m['citadas'] ?? [], 'pistas' => $m['pistas'] ?? []];
    }, fy_turnos($db, $f['id']));
    $activa = $f['estado'] === 'activa';
    $out = ['ok' => true, 'sesion' => [
        'id' => $f['id'], 'estado' => $f['estado'], 'origen' => $f['origen'], 'pregunta_id' => $f['pregunta_id'], 'elegida' => $f['elegida'], 'flujograma' => $f['flujograma'],
        'tema' => $f['tema'], 'especialidad' => $f['especialidad'], 'objetivo' => $e['objetivo'], 'fase' => $e['fase'], 'fase_nombre' => FY_FASES[$e['fase']],
        'fases' => FY_FASES, 'ayuda' => $e['ayuda'], 'creado' => (int) $f['creado'], 'actualizado' => (int) $f['actualizado'],
        'puede_finalizar' => $activa && fy_puede_finalizar($e), 'puede_pista' => $activa && $e['ayuda'] < 3,
        'intervenciones_restantes' => max(0, FY_MAX_TURNOS_ESTUDIANTE - $e['turnos_estudiante']),
    ], 'turnos' => $turnos, 'panel' => fy_panel($e), 'rubrica' => fy_niveles()];
    if (!$activa) { $out['informe'] = fy_informe($e, $f['estado']); }
    return $out;
}

function fy_guardar(PDO $db, string $id, array $e, ?string $estado = null): void
{
    $sql = 'UPDATE feynman_sesiones SET datos = ?, fase = ?, actualizado = ?' . ($estado !== null ? ', estado = ?, finalizado = ?' : '') . ' WHERE id = ?';
    $p = [json_encode($e, JSON_UNESCAPED_UNICODE), $e['fase'], time()];
    if ($estado !== null) { array_push($p, $estado, $estado === 'activa' ? 0 : time()); }
    $p[] = $id;
    $db->prepare($sql)->execute($p);
}

/** Fragmentos de guías oficiales (vacío si no hay guías cargadas): hasta 3 nacionales y 3 internacionales. */
function fy_recuperar_guias(string $consulta): array
{
    $r = [];
    if (guias_indice()['fragmentos']) {
        foreach (['nacional', 'internacional'] as $tipo) { foreach (guias_buscar($consulta, 3, ['tipo' => $tipo]) as $x) { $r[] = $x; } }
    }
    return $r;
}

/* ====================== ENCAMINADO ====================== */

$a = (string) ($_GET['a'] ?? '');
$metodo = strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? 'GET'));

try {
    if ($a === 'estado') {
        fy_resp(['ok' => true, 'ia_lista' => fy_ia_lista(), 'proveedor' => strtolower(fy_ajuste('AI_PROVIDER', 'ai_provider', 'gemini')), 'guias' => count(guias_indice()['docs']),
            'especialidades' => fy_especialidades(), 'rubrica' => fy_niveles(), 'fases' => FY_FASES, 'max_texto' => FY_MAX_TEXTO]);
    }

    if ($a === 'listar' && $metodo === 'GET') {
        $uid = fy_exigir_usuario(); $db = fy_db();
        $st = $db->prepare('SELECT id, origen, pregunta_id, tema, especialidad, estado, fase, datos, actualizado FROM feynman_sesiones WHERE usuario = ? ORDER BY actualizado DESC LIMIT 50'); $st->execute([$uid]);
        fy_resp(['ok' => true, 'sesiones' => array_map(static function ($f) {
            $e = json_decode($f['datos'], true);
            return ['id' => $f['id'], 'origen' => $f['origen'], 'pregunta_id' => $f['pregunta_id'], 'tema' => $f['tema'], 'especialidad' => $f['especialidad'], 'estado' => $f['estado'],
                'fase' => (int) $f['fase'], 'fase_nombre' => FY_FASES[(int) $f['fase']], 'objetivo' => $e['objetivo'], 'nivel_actual' => $e['nivel_actual'], 'actualizado' => (int) $f['actualizado']];
        }, $st->fetchAll())]);
    }

    if ($a === 'ver' && $metodo === 'GET') {
        $uid = fy_exigir_usuario(); $db = fy_db();
        fy_resp(fy_vista($db, fy_sesion($db, $uid, fy_id($_GET['id'] ?? ''))));
    }

    if ($a === 'crear') {
        $d = fy_exigir_post(); $uid = fy_exigir_usuario(); $db = fy_db();
        $origen = (string) ($d['origen'] ?? '');
        if (!in_array($origen, ['pregunta', 'flujograma', 'tema'], true)) { fy_fallo('Origen no válido.'); }
        $pid = fy_limpiar($d['pregunta_id'] ?? '', 40); $q = null; $elegida = '';
        if ($origen !== 'tema') {
            $q = fy_pregunta($pid);
            if (!$q) { fy_fallo('No encontramos esa pregunta en el banco.', 404); }
            $elegida = fy_limpiar($d['elegida'] ?? '', 2);
            if (!isset($q['opciones'][$elegida])) { $elegida = ''; }
        } else { $pid = ''; }
        $especialidad = $q ? $q['especialidad'] : fy_limpiar($d['especialidad'] ?? '', 80);
        $tema = fy_limpiar($d['tema'] ?? '', 120);
        if ($origen === 'tema' && mb_strlen($tema) < 3) { fy_fallo('Escribe el tema o concepto que quieres dominar (mínimo 3 letras).'); }
        if ($tema === '') { $tema = $especialidad !== '' ? $especialidad . ' · ' . $pid : $pid; }

        if (empty($d['nueva']) && $pid !== '') {          // continuidad: la misma pregunta (con el mismo origen) retoma la sesión activa en vez de abrir otra
            $st = $db->prepare("SELECT id FROM feynman_sesiones WHERE usuario = ? AND pregunta_id = ? AND origen = ? AND estado = 'activa' ORDER BY actualizado DESC LIMIT 1"); $st->execute([$uid, $pid, $origen]);
            if ($id = $st->fetchColumn()) { fy_resp(fy_vista($db, fy_sesion($db, $uid, (string) $id)) + ['retomada' => true]); }
        }
        $st = $db->prepare('SELECT COUNT(*) FROM feynman_sesiones WHERE usuario = ?'); $st->execute([$uid]);
        if ((int) $st->fetchColumn() >= FY_MAX_SESIONES) { fy_fallo('Llegaste al máximo de ' . FY_MAX_SESIONES . ' sesiones guardadas. Borra alguna para crear otra.', 409); }

        $sesion = ['origen' => $origen, 'tema' => $tema, 'especialidad' => $especialidad, 'elegida' => $elegida];
        $e0 = fy_estado_inicial([], '');
        $bloque = fy_bloque_datos($sesion, $q, $e0, ['ayuda' => 0, 'tarea' => 'Abre la sesión.', 'forzada' => null, 'permitidas' => [1]], [], 'texto');
        $ini = fy_llamar_validado($db, $uid, FY_SISTEMA_INICIO, [['rol' => 'usuario', 'texto' => $bloque]], 'fy_validar_inicio', 900);

        $e = fy_estado_inicial($ini['criterios'], $ini['objetivo']);
        $id = bin2hex(random_bytes(12)); $ahora = time();
        $db->beginTransaction();
        $db->prepare('INSERT INTO feynman_sesiones(id, usuario, origen, pregunta_id, elegida, flujograma, tema, especialidad, estado, fase, datos, creado, actualizado) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)')
            ->execute([$id, $uid, $origen, $pid, $elegida, preg_replace('/[^A-Za-z0-9._\-]/', '', fy_limpiar($d['flujograma'] ?? '', 120)), $tema, $especialidad, 'activa', 1, json_encode($e, JSON_UNESCAPED_UNICODE), $ahora, $ahora]);
        $db->prepare("INSERT INTO feynman_turnos(sesion, n, rol, texto, via, fase, accion, creado) VALUES (?,1,'tutor',?,'texto',1,'inicio',?)")->execute([$id, $ini['mensaje'], $ahora]);
        $db->commit();
        fy_resp(fy_vista($db, fy_sesion($db, $uid, $id)) + ['retomada' => false], 201);
    }

    if (in_array($a, ['turno', 'otro_caso'], true)) {
        $d = fy_exigir_post(); $uid = fy_exigir_usuario(); $db = fy_db();
        $f = fy_sesion($db, $uid, fy_id($d['id'] ?? ''));
        $req = (string) ($d['req_id'] ?? '');
        if (!preg_match('/^[A-Za-z0-9_-]{8,64}$/', $req)) { fy_fallo('Solicitud no válida.'); }
        $st = $db->prepare('SELECT 1 FROM feynman_turnos WHERE sesion = ? AND req_id = ?'); $st->execute([$f['id'], $req]);
        if ($st->fetchColumn()) { fy_resp(fy_vista($db, $f) + ['repetida' => true]); }       // el mismo envío dos veces no se procesa dos veces

        $e = json_decode($f['datos'], true);
        if ($a === 'otro_caso') {
            if ($f['estado'] !== 'completada' || $e['fase'] !== 5) { fy_fallo('Solo puedes pedir otro caso cuando la sesión terminó en la fase de aplicación.', 409); }
            $accion = 'nuevo_caso'; $texto = ''; $via = 'texto';
        } else {
            $accion = (string) ($d['accion'] ?? 'responder');
            if (!in_array($accion, ['responder', 'pista', 'explicacion'], true)) { fy_fallo('Acción no válida.'); }
            $via = ($d['via'] ?? 'texto') === 'voz' ? 'voz' : 'texto';
            $texto = fy_limpiar($d['texto'] ?? '', FY_MAX_TEXTO);
            if ($f['estado'] !== 'activa') { fy_fallo('Esta sesión ya terminó. Puedes revisar el informe o empezar otra.', 409); }
            if ($accion === 'responder' && mb_strlen($texto) < 2) { fy_fallo('Escribe o dicta tu explicación antes de enviar.'); }
            if (mb_strlen((string) ($d['texto'] ?? '')) > FY_MAX_TEXTO) { fy_fallo('Tu intervención supera los ' . FY_MAX_TEXTO . ' caracteres. Divídela o resúmela.', 413); }
            if ($accion === 'responder' && $e['turnos_estudiante'] >= FY_MAX_TURNOS_ESTUDIANTE) { fy_fallo('Alcanzaste el máximo de intervenciones de esta sesión. Finalízala para ver tu informe.', 409); }
            if ($accion === 'pista' && $e['ayuda'] >= 3) { fy_fallo('Ya usaste las pistas disponibles. Puedes pedir la explicación directa.', 409); }
        }
        $turnos = fy_turnos($db, $f['id']);
        if (count($turnos) >= FY_MAX_TURNOS_TOTAL) { fy_fallo('La sesión alcanzó su longitud máxima. Finalízala para ver tu informe.', 409); }

        fy_bloquear($db, $uid, $f['id']);
        try {
            $q = $f['pregunta_id'] !== '' ? fy_pregunta($f['pregunta_id']) : null;
            $plan = fy_plan_turno($e, $accion);
            $recuperados = fy_recuperar_guias($f['tema'] . ' ' . $f['especialidad'] . ' ' . $e['objetivo'] . ' ' . ($q ? mb_substr($q['enunciado'], 0, 300) : '') . ' ' . $texto);
            $bloque = fy_bloque_datos($f, $q, $e, $plan, $recuperados, $via);
            $final = $bloque . "<<<ESTUDIANTE\n" . ($accion === 'responder' ? $texto : '(el estudiante no escribió texto: ' . ($accion === 'pista' ? 'pidió una pista' : ($accion === 'explicacion' ? 'pidió la explicación directa' : 'pidió un caso nuevo')) . ')') . "\nESTUDIANTE>>>\n"
                . 'Responde solo con el JSON del contrato.';
            $previos = array_map(static fn($t) => ['rol' => $t['rol'], 'texto' => $t['texto']], $turnos);
            $nGuias = count($recuperados);
            $idsCrit = array_column($e['criterios'], 'id'); $idsAb = array_column(fy_errores_abiertos($e), 'id');
            $e2 = $e; $e2['turnos_estudiante'] += $accion === 'responder' ? 1 : 0;
            $r = fy_llamar_validado($db, $uid, FY_SISTEMA, fy_armar_mensajes($previos, $final), static function ($j) use ($nGuias, $idsCrit, $idsAb, $e2, $plan, $texto) {
                $v = fy_validar_turno($j, $nGuias, $idsCrit, $idsAb);
                if (!$v['ok']) { return $v; }
                $t = fy_validar_transicion($e2, $plan, $v['d'], $texto);
                return $t['ok'] ? $v : ['ok' => false, 'error' => 'transición de fase no admisible: ' . $t['motivo']];
            });
            [$limpio, $citadas] = guias_validar_citas($r['mensaje'], $nGuias);
            $r['mensaje'] = $limpio;
            $fichas = array_map(static fn($x, $i) => guias_cita($x, $i + 1), $recuperados, array_keys($recuperados));
            $e3 = fy_aplicar($e2, $plan, $r, $texto);
            if ($r['repaso'] && $e3['fase'] >= 4) { $e3 = fy_agregar_tarjetas($e3, $r['repaso'], $fichas); }
            $nivel = fy_nivel_efectivo($e2, $plan, $r, $texto);
            $n = count($turnos); $ahora = time();
            $db->beginTransaction();
            if ($accion !== 'nuevo_caso') {
                $db->prepare('INSERT INTO feynman_turnos(sesion, n, rol, texto, via, fase, accion, req_id, meta, creado) VALUES (?,?,?,?,?,?,?,?,?,?)')
                    ->execute([$f['id'], $n + 1, 'estudiante', $accion === 'responder' ? $texto : ($accion === 'pista' ? '(pidió una pista)' : '(pidió la explicación directa)'), $via, $e['fase'], $accion, $req,
                        json_encode(['nivel' => $nivel], JSON_UNESCAPED_UNICODE), $ahora]);
                $n++;
            }
            $db->prepare('INSERT INTO feynman_turnos(sesion, n, rol, texto, via, fase, accion, req_id, meta, creado) VALUES (?,?,?,?,?,?,?,?,?,?)')
                ->execute([$f['id'], $n + 1, 'tutor', $r['mensaje'], 'texto', $e3['fase'], $accion, $accion === 'nuevo_caso' ? $req : null,
                    json_encode(['aclaracion' => $r['aclaracion_transcripcion'], 'guias' => $fichas, 'citadas' => $citadas, 'pistas' => $r['pistas']], JSON_UNESCAPED_UNICODE), $ahora]);
            fy_guardar($db, $f['id'], $e3, $accion === 'nuevo_caso' ? 'activa' : null);
            $db->commit();
        } catch (Throwable $x) {
            if ($db->inTransaction()) { $db->rollBack(); }
            throw $x;
        } finally {
            fy_liberar($db, $f['id']);
        }
        fy_resp(fy_vista($db, fy_sesion($db, $uid, $f['id'])));
    }

    if ($a === 'finalizar') {
        $d = fy_exigir_post(); $uid = fy_exigir_usuario(); $db = fy_db();
        $f = fy_sesion($db, $uid, fy_id($d['id'] ?? ''));
        if ($f['estado'] !== 'activa') { fy_resp(fy_vista($db, $f)); }
        $e = json_decode($f['datos'], true);
        $estado = fy_puede_finalizar($e) ? 'completada' : 'incompleta';
        fy_bloquear($db, $uid, $f['id']);
        try {
            if ($e['turnos_estudiante'] > 0 && fy_ia_lista()) {          // el cierre con IA es un extra: si falla o se limita, el informe se entrega igual
                try {
                    $cierre = fy_llamar_validado($db, $uid, FY_SISTEMA_CIERRE, [['rol' => 'usuario', 'texto' => fy_resumen_para_cierre($f, $e) . 'Responde solo con el JSON del contrato.']],
                        static fn($j) => fy_validar_cierre($j, 0), 1000);
                    $e['cierre'] = ['resumen' => $cierre['resumen'], 'proximos_pasos' => $cierre['proximos_pasos']];
                    $e = fy_agregar_tarjetas($e, $cierre['tarjetas'], []);
                } catch (Throwable $x) { error_log('[feynman] cierre sin IA: ' . $x->getMessage()); }
            }
            fy_guardar($db, $f['id'], $e, $estado);
        } finally { fy_liberar($db, $f['id']); }
        fy_resp(fy_vista($db, fy_sesion($db, $uid, $f['id'])));
    }

    if ($a === 'reanudar') {
        $d = fy_exigir_post(); $uid = fy_exigir_usuario(); $db = fy_db();
        $f = fy_sesion($db, $uid, fy_id($d['id'] ?? ''));
        if ($f['estado'] !== 'incompleta' && $f['estado'] !== 'activa') { fy_fallo('Solo se pueden retomar las sesiones que terminaste antes de completarlas.', 409); }
        if ($f['estado'] === 'incompleta') { fy_guardar($db, $f['id'], json_decode($f['datos'], true), 'activa'); }
        fy_resp(fy_vista($db, fy_sesion($db, $uid, $f['id'])));
    }

    if ($a === 'tarjetas') {
        $d = fy_exigir_post(); $uid = fy_exigir_usuario(); $db = fy_db();
        $f = fy_sesion($db, $uid, fy_id($d['id'] ?? ''));
        $e = json_decode($f['datos'], true);
        foreach (is_array($d['decisiones'] ?? null) ? $d['decisiones'] : [] as $x) {
            if (is_array($x) && is_int($x['i'] ?? null) && isset($e['tarjetas'][$x['i']]) && in_array($x['estado'] ?? '', ['guardada', 'descartada'], true)) { $e['tarjetas'][$x['i']]['estado'] = $x['estado']; }
        }
        fy_guardar($db, $f['id'], $e);
        fy_resp(fy_vista($db, fy_sesion($db, $uid, $f['id'])));
    }

    if ($a === 'borrar') {
        $d = fy_exigir_post(); $uid = fy_exigir_usuario(); $db = fy_db();
        $f = fy_sesion($db, $uid, fy_id($d['id'] ?? ''));
        $db->prepare('DELETE FROM feynman_sesiones WHERE id = ? AND usuario = ?')->execute([$f['id'], $uid]);
        fy_resp(['ok' => true]);
    }

    fy_fallo('Acción desconocida.', 404);
} catch (FyError $x) {
    fy_resp(['ok' => false, 'error' => $x->getMessage()], $x->getCode());
} catch (Throwable $x) {
    error_log('[feynman] ' . get_class($x) . ': ' . $x->getMessage());
    fy_resp(['ok' => false, 'error' => FY_MSG_GENERICO], 500);
}
