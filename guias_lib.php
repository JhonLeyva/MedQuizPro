<?php
/**
 * Guías clínicas: búsqueda en el índice (guias/indice.json) y validación de citas.
 *
 * El índice lo genera tools/ingestar_guias.py a partir de los PDF oficiales descritos en guias/manifest.json, conservando el número de
 * página de cada fragmento. La búsqueda es BM25 en PHP puro (sin extensiones, funciona en cualquier hosting). Nada de esto inventa
 * contenido: si el índice está vacío o no hay fragmentos relevantes, el resultado es una lista vacía.
 */
declare(strict_types=1);

const GUIAS_INDICE = __DIR__ . '/guias/indice.json';
const GUIAS_STOP = ['de','la','el','los','las','un','una','unos','unas','que','y','o','en','con','sin','por','para','del','al','se','es','son','su','sus','lo','le','a','como','mas','muy','ya','si','no','segun','cual','cuales','esta','este','estos','estas'];

/** Minúsculas, sin tildes y sin signos: así «Preeclampsia» y «preeclampsía» coinciden. */
function guias_normalizar(string $t): string {
    $t = mb_strtolower($t);
    $t = strtr($t, ['á' => 'a', 'é' => 'e', 'í' => 'i', 'ó' => 'o', 'ú' => 'u', 'ü' => 'u', 'ñ' => 'n']);
    return trim((string) preg_replace('/[^a-z0-9]+/', ' ', $t));
}
function guias_tokens(string $t): array {
    $o = [];
    foreach (explode(' ', guias_normalizar($t)) as $w) if (strlen($w) >= 3 && !in_array($w, GUIAS_STOP, true)) $o[] = $w;
    return $o;
}

/** @return array{docs: array, fragmentos: array}  (vacío si no hay índice) */
function guias_indice(?string $archivo = null): array {
    static $cache = [];
    $archivo = $archivo ?? ((string) getenv('MQP_GUIAS_INDICE') ?: GUIAS_INDICE);   // la variable solo la usan las pruebas
    if (isset($cache[$archivo])) return $cache[$archivo];
    $vacio = ['docs' => [], 'fragmentos' => []];
    if (!is_readable($archivo)) return $cache[$archivo] = $vacio;
    $j = json_decode((string) file_get_contents($archivo), true);
    if (!is_array($j) || !is_array($j['docs'] ?? null) || !is_array($j['fragmentos'] ?? null)) return $cache[$archivo] = $vacio;
    $docs = [];
    foreach ($j['docs'] as $d) if (is_array($d) && isset($d['id'])) $docs[(string) $d['id']] = $d;
    return $cache[$archivo] = ['docs' => $docs, 'fragmentos' => $j['fragmentos']];
}

/**
 * BM25 sobre los fragmentos. $filtros: 'tipo' => 'nacional'|'internacional', 'docs' => [ids].
 * Devuelve [['fragmento' => …, 'doc' => …, 'puntaje' => float], …] con los mejores $k que superen un umbral mínimo.
 */
function guias_buscar(string $consulta, int $k = 5, array $filtros = [], ?string $archivo = null): array {
    $ix = guias_indice($archivo);
    $q = array_values(array_unique(guias_tokens($consulta)));
    if (!$q || !$ix['fragmentos']) return [];
    $N = count($ix['fragmentos']); $tf = []; $df = []; $largo = []; $suma = 0;
    foreach ($ix['fragmentos'] as $i => $f) {
        $doc = $ix['docs'][(string) ($f['doc'] ?? '')] ?? null;
        if (!$doc) continue;
        if (isset($filtros['tipo']) && ($doc['tipo'] ?? '') !== $filtros['tipo']) continue;
        if (isset($filtros['docs']) && !in_array((string) $f['doc'], array_map('strval', $filtros['docs']), true)) continue;
        // 'temas' (en español) permite hallar guías en inglés con una consulta en español
        $t = guias_tokens((string) ($f['texto'] ?? '') . ' ' . implode(' ', (array) ($doc['temas'] ?? [])));; $largo[$i] = max(1, count($t)); $suma += $largo[$i];
        $c = array_count_values($t);
        foreach ($q as $w) if (isset($c[$w])) { $tf[$i][$w] = $c[$w]; $df[$w] = ($df[$w] ?? 0) + 1; }
    }
    if (!$largo) return [];
    $prom = $suma / count($largo); $res = [];
    foreach ($tf as $i => $m) {
        $s = 0.0;
        foreach ($m as $w => $f) {
            $idf = log(1 + (count($largo) - $df[$w] + 0.5) / ($df[$w] + 0.5));
            $s += $idf * ($f * 2.2) / ($f + 1.2 * (0.25 + 0.75 * $largo[$i] / $prom));
        }
        $cubre = count($m) / min(count($q), 6);              // términos de la consulta presentes (tope 6: las consultas largas no penalizan)
        if (count($m) < (count($q) <= 2 ? 1 : 2)) continue;   // una sola palabra suelta en común es una coincidencia casual: no se muestra
        $res[] = ['fragmento' => $ix['fragmentos'][$i], 'doc' => $ix['docs'][(string) $ix['fragmentos'][$i]['doc']], 'puntaje' => round($s * (0.5 + $cubre), 4)];
    }
    usort($res, fn($a, $b) => $b['puntaje'] <=> $a['puntaje']);
    return array_slice($res, 0, $k);
}

/** Ficha de una fuente lista para mostrar: título, institución, año/versión, página, extracto y estado de vigencia. */
function guias_cita(array $r, int $n): array {
    $d = $r['doc']; $f = $r['fragmento'];
    $estado = (string) ($d['estado'] ?? 'vigente');
    return [
        'n' => $n, 'id' => $f['id'], 'titulo' => (string) ($d['titulo'] ?? ''), 'institucion' => (string) ($d['institucion'] ?? ''),
        'pais' => (string) ($d['pais'] ?? ''), 'tipo' => (string) ($d['tipo'] ?? ''), 'anio' => $d['anio'] ?? null, 'version' => (string) ($d['version'] ?? ''),
        'pagina' => (int) ($f['pagina'] ?? 0), 'extracto' => mb_substr((string) $f['texto'], 0, 420), 'url' => (string) ($d['url'] ?? ''),
        'estado' => $estado, 'reemplazada_por' => (string) ($d['reemplazada_por'] ?? ''),
        'aviso' => $estado === 'vigente' ? '' : ($estado === 'reemplazada' ? 'Esta guía fue reemplazada' . (!empty($d['reemplazada_por']) ? ' por: ' . $d['reemplazada_por'] : '') . '.' : 'Esta guía fue retirada.'),
    ];
}

/**
 * Revisa las citas «[G1]» de una respuesta contra los fragmentos que de verdad se entregaron al modelo.
 * Las citas a números que no existen se quitan del texto y se informan. Devuelve [texto limpio, citadas (n), inválidas (n)].
 */
function guias_validar_citas(string $respuesta, int $entregados): array {
    $citadas = []; $invalidas = [];
    $limpio = preg_replace_callback('/\[G(\d{1,2})\]/', function ($m) use ($entregados, &$citadas, &$invalidas) {
        $n = (int) $m[1];
        if ($n >= 1 && $n <= $entregados) { $citadas[$n] = true; return $m[0]; }
        $invalidas[$n] = true; return '';
    }, $respuesta);
    return [trim((string) preg_replace('/[ \t]{2,}/', ' ', (string) $limpio)), array_keys($citadas), array_keys($invalidas)];
}
