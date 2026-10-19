<?php
// php tests/guias_test.php <indice.json>  (lo invoca guias_test.py con un índice de guías FICTICIAS)
require __DIR__ . '/../guias_lib.php';
$ix = $argv[1]; $f = 0; $n = 0;
function ok(bool $c, string $m): void { global $f, $n; $n++; if (!$c) { $f++; echo "FALLA: $m\n"; } }

$r = guias_buscar('¿Cuál es el tratamiento inicial del síndrome zeta?', 5, [], $ix);
ok(count($r) >= 2, 'encuentra fragmentos relevantes (con tildes y mayúsculas)');
ok(($r[0]['doc']['id'] ?? '') !== '' && $r[0]['fragmento']['pagina'] >= 1, 'cada resultado trae documento y página');
ok(guias_buscar('infarto agudo de miocardio troponina', 5, [], $ix) === [], 'consulta sin relación → NO inventa resultados');
ok(guias_buscar('', 5, [], $ix) === [], 'consulta vacía → vacío');
$nac = guias_buscar('síndrome zeta tratamiento', 5, ['tipo' => 'nacional'], $ix); $int = guias_buscar('zeta syndrome treatment fluids', 5, ['tipo' => 'internacional'], $ix);
ok($nac && array_unique(array_column(array_column($nac, 'doc'), 'tipo')) === ['nacional'], 'filtro nacional no mezcla países');
ok($int && array_unique(array_column(array_column($int, 'doc'), 'tipo')) === ['internacional'], 'filtro internacional');
$es = guias_buscar('¿Cuál es el tratamiento inicial del síndrome zeta?', 5, ['tipo' => 'internacional'], $ix);
ok(count($es) >= 1, 'una consulta en español halla la guía en inglés gracias a sus «temas»');
$c = guias_cita($nac[0], 1);
ok($c['estado'] === 'reemplazada' && str_contains($c['aviso'], 'reemplazada') && str_contains($c['aviso'], 'Guía de prueba 2025'), 'avisa que la guía está reemplazada');
ok($c['institucion'] === 'Institución ficticia' && $c['anio'] === 2021 && $c['version'] === 'v1' && $c['pagina'] >= 1, 'la cita incluye institución, año, versión y página');
ok(guias_cita($int[0], 2)['aviso'] === '', 'guía vigente: sin aviso');
// el extracto citado sale del fragmento real
ok(str_contains(guias_normalizar($ix ? file_get_contents($ix) : ''), guias_normalizar(substr($c['extracto'], 0, 30))), 'el extracto proviene del índice');
// validación de citas
[$t, $ci, $inv] = guias_validar_citas('Se hospitaliza si hay hipotensión [G2]. Además X [G7] y Y [G0].', 3);
ok($ci === [2] && $inv === [7, 0] && !str_contains($t, 'G7') && !str_contains($t, 'G0') && str_contains($t, '[G2]'), 'cita inexistente se elimina e informa; la válida se conserva');
[$t2, $c2, $i2] = guias_validar_citas('Sin citas aquí.', 3); ok($c2 === [] && $i2 === [] && $t2 === 'Sin citas aquí.', 'sin citas no cambia nada');
ok(guias_buscar('zeta', 5, [], '/no/existe.json') === [], 'sin índice → vacío');
// modo espejo
$cp = $argv[2] ?? ''; $comps = guias_comparaciones($cp);
ok(count($comps) === 2, 'lee las comparaciones');
$c = guias_comparacion_para('Q-1', '', $comps, $ix);
ok($c && $c['id'] === 'zeta' && $c['nacional']['cita']['pagina'] >= 1 && $c['internacional']['cita']['tipo'] === 'internacional', 'se halla por id de pregunta, con las dos fuentes citadas');
ok(guias_comparacion_para('Q-999', 'Síndrome ZETA', $comps, $ix)['id'] === 'zeta', 'se halla por tema (sin tildes ni mayúsculas)');
ok($c['filas'][1]['tipo'] === 'discrepancia' && $c['filas'][1]['internacional']['cita']['pagina'] >= 1, 'cada celda lleva su cita real');
$solo = guias_comparacion_para('', 'otro tema', $comps, $ix);
ok($solo && $solo['nacional'] !== null && $solo['internacional'] === null, 'lado sin fuente → null («Fuente no disponible»), sin fabricar nada');
ok(guias_comparacion_para('Q-5', 'tema que no existe', $comps, $ix) === null, 'sin comparación validada → null');
$falso = [['id' => 'x', 'preguntas' => ['Q-9'], 'nacional' => ['frag' => 'no-existe'], 'internacional' => null, 'filas' => [['criterio' => 'c', 'tipo' => 'discrepancia', 'nacional' => ['texto' => 'dato', 'frag' => 'no-existe'], 'internacional' => null]]]];
$cf = guias_comparacion_para('Q-9', '', $falso, $ix); ok($cf['nacional'] === null && $cf['filas'][0]['nacional']['cita'] === null, 'un fragmento inexistente nunca aparece como respaldado');
echo $f ? "$f de $n pruebas PHP fallaron\n" : "OK: $n pruebas PHP pasaron\n"; exit($f ? 1 : 0);
