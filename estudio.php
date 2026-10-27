<?php
/**
 * estudio.php — confianza por intento y «Repaso de hoy».
 *
 *  GET  ?a=estado      ¿hay sesión? (la interfaz solo pide confianza si hay cuenta donde guardarla)
 *  POST ?a=intento     {pregunta_id, elegida, confianza: baja|media|alta|null, modo, req_id}
 *  GET  ?a=repaso      tarjetas pendientes, preguntas por reforzar, resumen y calibración (datos reales del propio usuario)
 *  POST ?a=olvidar     borra todo el historial de intentos del usuario
 *
 * Misma sesión que cuenta.php (cookie mqp_sid); no exige plan (como las flashcards). POST con X-MQP y mismo origen. Cada consulta filtra por usuario.
 * El servidor lee la clave del banco (bancos/*.json, solo lectura) y decide el acierto y la etiqueta: el navegador no puede falsearlos.
 * Esto NO cambia el puntaje ni las respuestas de la práctica: es un registro complementario.
 */
declare(strict_types=1);

require_once __DIR__ . '/feynman_lib.php';
require_once __DIR__ . '/estudio_lib.php';

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

final class EsError extends RuntimeException {}
function es_resp(array $d, int $c = 200): never { http_response_code($c); echo json_encode($d, JSON_UNESCAPED_UNICODE); exit; }
function es_fallo(string $m, int $c = 400): never { throw new EsError($m, $c); }

function es_db(): PDO
{
    static $pdo = null;
    if ($pdo) { return $pdo; }
    $f = __DIR__ . '/cuenta_datos/mqp.sqlite';
    if (!is_file($f)) { es_fallo('Inicia sesión.', 401); }
    $pdo = new PDO('sqlite:' . $f, null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
    $pdo->exec('PRAGMA foreign_keys=ON; PRAGMA busy_timeout=5000;');
    $pdo->exec("CREATE TABLE IF NOT EXISTS intentos_respuesta (
        id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
        pregunta TEXT NOT NULL, elegida TEXT NOT NULL DEFAULT '', correcta INTEGER NOT NULL, confianza TEXT, etiqueta TEXT NOT NULL,
        modo TEXT NOT NULL DEFAULT 'estudio', req_id TEXT, t INTEGER NOT NULL)");
    $pdo->exec('CREATE INDEX IF NOT EXISTS ix_intres_u ON intentos_respuesta(usuario, pregunta, t)');
    $pdo->exec('CREATE UNIQUE INDEX IF NOT EXISTS ux_intres_req ON intentos_respuesta(usuario, req_id) WHERE req_id IS NOT NULL');
    return $pdo;
}

function es_usuario(bool $obligatorio = true): int
{
    session_name('mqp_sid');
    @session_start(['read_and_close' => true]);
    $uid = (int) ($_SESSION['uid'] ?? 0);
    if ($uid <= 0 && $obligatorio) { es_fallo('Inicia sesión para guardar tu confianza y tu repaso.', 401); }
    return $uid;
}

function es_post(): array
{
    if (strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? '')) !== 'POST') { header('Allow: POST'); es_fallo('Método no permitido.', 405); }
    if (($_SERVER['HTTP_X_MQP'] ?? '') !== '1') { es_fallo('Solicitud no válida.', 403); }
    $o = (string) ($_SERVER['HTTP_ORIGIN'] ?? '');
    if ($o !== '') {
        $a = strtolower((string) parse_url($o, PHP_URL_HOST)); $b = strtolower((string) preg_replace('/:\d+$/', '', (string) ($_SERVER['HTTP_HOST'] ?? '')));
        if ($a !== '' && $b !== '' && $a !== $b) { es_fallo('Solicitud no válida.', 403); }
    }
    $raw = (string) file_get_contents('php://input');
    if (strlen($raw) > 4000) { es_fallo('Solicitud demasiado grande.', 413); }
    $j = json_decode($raw, true);
    return is_array($j) ? $j : [];
}

$a = (string) ($_GET['a'] ?? '');
try {
    if ($a === 'estado') { es_resp(['ok' => true, 'sesion' => es_usuario(false) > 0]); }

    if ($a === 'intento') {
        $d = es_post(); $uid = es_usuario(); $db = es_db();
        $q = fy_pregunta(fy_limpiar($d['pregunta_id'] ?? '', 40));
        if (!$q) { es_fallo('No encontramos esa pregunta en el banco.', 404); }
        $elegida = fy_limpiar($d['elegida'] ?? '', 2);
        if (!isset($q['opciones'][$elegida])) { es_fallo('Alternativa no válida.'); }
        $conf = $d['confianza'] ?? null;
        if ($conf !== null && !in_array($conf, ES_CONFIANZAS, true)) { es_fallo('Confianza no válida.'); }
        $req = $d['req_id'] ?? null;
        if ($req !== null && !preg_match('/^[A-Za-z0-9_-]{8,64}$/', (string) $req)) { es_fallo('Solicitud no válida.'); }
        $modo = in_array($d['modo'] ?? '', ['estudio', 'simulacro', 'repaso'], true) ? $d['modo'] : 'estudio';
        $st = $db->prepare('SELECT COUNT(*) FROM intentos_respuesta WHERE usuario = ? AND t > ?'); $st->execute([$uid, time() - 60]);
        if ((int) $st->fetchColumn() >= 200) { header('Retry-After: 60'); es_fallo('Vas muy rápido. Espera un momento.', 429); }
        $acierto = $elegida === $q['clave'];
        $etq = es_etiqueta($acierto, $conf);
        $ins = $db->prepare('INSERT OR IGNORE INTO intentos_respuesta(usuario, pregunta, elegida, correcta, confianza, etiqueta, modo, req_id, t) VALUES (?,?,?,?,?,?,?,?,?)');
        $ins->execute([$uid, $q['id'], $elegida, $acierto ? 1 : 0, $conf, $etq, $modo, $req, time()]);
        es_resp(['ok' => true, 'acierto' => $acierto, 'etiqueta' => $etq, 'texto' => ES_TEXTOS[$etq], 'pendiente' => in_array($etq, ES_PENDIENTES, true), 'repetido' => $ins->rowCount() === 0], 201);
    }

    if ($a === 'repaso') {
        $uid = es_usuario(); $db = es_db(); $ahora = time();
        $st = $db->prepare('SELECT pregunta, correcta, confianza, etiqueta, t FROM intentos_respuesta WHERE usuario = ? AND t >= ? ORDER BY t DESC LIMIT 5000'); $st->execute([$uid, $ahora - ES_VENTANA_DIAS * 86400]);
        $filas = array_map(static fn($f) => ['pregunta' => $f['pregunta'], 'correcta' => (int) $f['correcta'], 'confianza' => $f['confianza'], 'etiqueta' => $f['etiqueta'], 't' => (int) $f['t']], $st->fetchAll());
        $ref = [];
        foreach (es_priorizar($filas, $ahora) as $r) {
            $q = fy_pregunta($r['pregunta']);
            if (!$q) { continue; }
            $ref[] = $r + ['texto' => ES_TEXTOS[$r['etiqueta']], 'especialidad' => $q['especialidad'], 'enunciado' => mb_substr($q['enunciado'], 0, 170)];
        }
        $sem = array_values(array_filter($filas, static fn($f) => $f['t'] >= $ahora - 7 * 86400));
        $cuenta = static fn(array $l, string $e) => count(array_filter($l, static fn($f) => $f['etiqueta'] === $e));
        $tj = ['pendientes' => 0, 'total' => 0];
        try {
            $q1 = $db->prepare('SELECT COUNT(*) FROM flashcards WHERE usuario = ?'); $q1->execute([$uid]); $tj['total'] = (int) $q1->fetchColumn();
            $q2 = $db->prepare('SELECT COUNT(*) FROM flashcards WHERE usuario = ? AND proximo <= ?'); $q2->execute([$uid, $ahora]); $tj['pendientes'] = (int) $q2->fetchColumn();
        } catch (Throwable $e) { /* sin tabla de tarjetas todavía */ }
        es_resp(['ok' => true, 'ahora' => $ahora, 'tarjetas' => $tj, 'refuerzo' => $ref, 'ids' => array_column($ref, 'pregunta'),
            'semana' => ['intentos' => count($sem), 'aciertos' => count(array_filter($sem, static fn($f) => $f['correcta'] === 1)), 'falsos_conceptos' => $cuenta($sem, 'falso_concepto'),
                'lagunas' => $cuenta($sem, 'laguna'), 'aciertos_dudosos' => $cuenta($sem, 'acierto_dudoso')],
            'calibracion' => es_calibracion($filas), 'con_confianza' => count(array_filter($filas, static fn($f) => $f['confianza'] !== null))]);
    }

    if ($a === 'olvidar') {
        es_post(); $uid = es_usuario(); $db = es_db();
        $db->prepare('DELETE FROM intentos_respuesta WHERE usuario = ?')->execute([$uid]);
        es_resp(['ok' => true]);
    }
    es_fallo('Acción desconocida.', 404);
} catch (EsError $x) {
    es_resp(['ok' => false, 'error' => $x->getMessage()], $x->getCode());
} catch (Throwable $x) {
    error_log('[estudio] ' . get_class($x) . ': ' . $x->getMessage());
    es_resp(['ok' => false, 'error' => 'Algo salió mal. Inténtalo de nuevo en un momento.'], 500);
}
