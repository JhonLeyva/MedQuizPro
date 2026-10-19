<?php
// php tests/flashcards_test.php  → sale con código 1 si algo falla
require __DIR__ . '/../flashcards_lib.php';
$f = 0; $n = 0;
function ok(bool $c, string $m): void { global $f, $n; $n++; if (!$c) { $f++; echo "FALLA: $m\n"; } }
$t0 = 1_800_000_000; $D = 86400;
$nuevo = ['estado' => 'nuevo', 'facilidad' => 2.5, 'intervalo' => 0, 'repeticiones' => 0, 'lapsos' => 0];

$r = fc_planificar($nuevo, 'otra_vez', $t0); ok($r['estado'] === 'aprendiendo' && $r['proximo'] === $t0 + 600, 'nuevo+otra_vez = 10 min');
$r = fc_planificar($nuevo, 'bien', $t0);      ok($r['estado'] === 'repaso' && $r['intervalo'] === 1 && $r['proximo'] === $t0 + $D, 'nuevo+bien = 1 día');
$r = fc_planificar($nuevo, 'facil', $t0);     ok($r['intervalo'] === 4 && $r['facilidad'] === 2.65, 'nuevo+facil = 4 días, facilidad sube');
$r = fc_planificar($nuevo, 'dificil', $t0);   ok($r['intervalo'] === 1 && $r['facilidad'] === 2.35, 'nuevo+dificil = 1 día, facilidad baja');

$rep = ['estado' => 'repaso', 'facilidad' => 2.5, 'intervalo' => 10, 'repeticiones' => 3, 'lapsos' => 0];
$r = fc_planificar($rep, 'bien', $t0);    ok($r['intervalo'] === 25, 'repaso 10d + bien = 25d');
$r = fc_planificar($rep, 'dificil', $t0); ok($r['intervalo'] === 12 && $r['facilidad'] === 2.35, 'repaso 10d + dificil = 12d');
$r = fc_planificar($rep, 'facil', $t0);   ok($r['intervalo'] === 33, 'repaso 10d + facil = 33d');
$r = fc_planificar($rep, 'otra_vez', $t0);ok($r['estado'] === 'reaprendiendo' && $r['lapsos'] === 1 && $r['intervalo'] === 5 && $r['facilidad'] === 2.3, 'lapso: reaprendiendo, intervalo a la mitad');
$re = $r; $r = fc_planificar($re, 'bien', $t0 + 600); ok($r['estado'] === 'repaso' && $r['intervalo'] === 5, 'reaprendiendo+bien vuelve a repaso con intervalo reducido');

$chico = ['estado' => 'repaso', 'facilidad' => 1.3, 'intervalo' => 1, 'repeticiones' => 1, 'lapsos' => 0];
$r = fc_planificar($chico, 'bien', $t0); ok($r['intervalo'] >= 2, 'siempre avanza al menos 1 día');
$gran = ['estado' => 'repaso', 'facilidad' => 3.0, 'intervalo' => 300, 'repeticiones' => 9, 'lapsos' => 0];
$r = fc_planificar($gran, 'facil', $t0); ok($r['intervalo'] === 365, 'tope de 365 días');
$bajo = ['estado' => 'repaso', 'facilidad' => 1.3, 'intervalo' => 10, 'repeticiones' => 3, 'lapsos' => 2];
$r = fc_planificar($bajo, 'otra_vez', $t0); ok($r['facilidad'] === 1.3, 'facilidad nunca baja de 1.3');
ok($r['repeticiones'] === 4, 'cuenta repeticiones');

try { fc_planificar($nuevo, 'excelente', $t0); ok(false, 'rechaza calificación inválida'); } catch (InvalidArgumentException $e) { ok(true, ''); }
ok(fc_planificar($nuevo, 'bien', $t0)['proximo'] > $t0, 'una tarjeta nueva no es "conocida" hasta calificarla (nace nuevo)');
$p = fc_previas($nuevo, $t0); ok($p === ['otra_vez' => '10 min', 'dificil' => '1 día', 'bien' => '1 día', 'facil' => '4 días'], 'previas de botones');
ok(fc_etiqueta(45 * $D) === '2 meses' || fc_etiqueta(45 * $D) === '1 mes', 'etiqueta meses');
ok(fc_huella('A-1', 'Hola  mundo') === fc_huella('a-1', ' hola mundo '), 'huella normaliza espacios y mayúsculas');
ok(fc_huella('A-1', 'x') !== fc_huella('A-2', 'x'), 'huella distingue preguntas');
echo $f ? "$f de $n pruebas fallaron\n" : "OK: $n pruebas pasaron\n"; exit($f ? 1 : 0);
