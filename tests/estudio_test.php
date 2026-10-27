<?php
/** php tests/estudio_test.php — etiquetas de confianza, prioridad del repaso, calibración y validación Cloze del servidor. Sin red ni base de datos. */
declare(strict_types=1);
require __DIR__ . '/../estudio_lib.php';
require __DIR__ . '/../flashcards_lib.php';
$f = 0; $n = 0;
function ok($c, string $m): void { global $f, $n; $n++; if (!$c) { $f++; echo "FALLA: $m\n"; } }

/* ---- reglas de etiquetado (las del prompt) ---- */
ok(es_etiqueta(false, 'alta') === 'falso_concepto', 'fallo con confianza alta → falso concepto de alta prioridad');
ok(es_etiqueta(false, 'baja') === 'refuerzo' && es_etiqueta(false, 'media') === 'refuerzo', 'fallo con confianza baja/media → refuerzo (sin asumir una creencia errónea consolidada)');
ok(es_etiqueta(false, null) === 'refuerzo', 'fallo sin indicar confianza → refuerzo');
ok(es_etiqueta(true, 'baja') === 'laguna', 'acierto adivinando → posible laguna de comprensión');
ok(es_etiqueta(true, 'media') === 'acierto_dudoso' && es_etiqueta(true, 'alta') === 'acierto_seguro' && es_etiqueta(true, null) === 'acierto', 'aciertos: dudoso / seguro / sin indicar');
ok(!in_array('acierto_seguro', ES_PENDIENTES, true), 'un acierto seguro no queda pendiente, pero tampoco se declara dominio');
try { es_etiqueta(true, 'segurisimo'); ok(false, 'confianza inválida debe fallar'); } catch (InvalidArgumentException $e) { ok(true, ''); }
ok(ES_TEXTOS['falso_concepto'] === 'Falso concepto de alta prioridad', 'texto de la etiqueta pedida');

/* ---- repaso: pendiente = último intento pendiente; prioridad = peso + recurrencia ---- */
$h = 1_800_000_000; $D = 86400;
$i = fn(string $q, string $e, int $dias) => ['pregunta' => $q, 'etiqueta' => $e, 't' => $h - $dias * $D];
$r = es_priorizar([
    $i('A', 'refuerzo', 5), $i('A', 'acierto_seguro', 2),                         // A se corrigió: no pendiente
    $i('B', 'refuerzo', 9), $i('B', 'refuerzo', 4), $i('B', 'falso_concepto', 1),  // B: recurrente
    $i('C', 'laguna', 3),                                                          // C: una laguna
    $i('D', 'acierto_dudoso', 1),                                                  // D: acierto con dudas
    $i('E', 'falso_concepto', 200),                                                // E: fuera de la ventana de 180 días
    $i('F', 'acierto', 1),
], $h);
$ids = array_column($r, 'pregunta');
ok($ids === ['B', 'C', 'D'], 'pendientes ordenados por prioridad; A (corregida), E (muy antigua) y F (acierto) no aparecen: ' . implode(',', $ids));
ok($r[0]['score'] === 4 + 2 && $r[0]['pendientes_previos'] === 2 && $r[0]['intentos'] === 3, 'B: peso 4 + 2 de recurrencia');
ok($r[1]['score'] === 2 && $r[2]['score'] === 1, 'pesos de laguna (2) y acierto dudoso (1)');
$muchos = []; for ($k = 0; $k < 5; $k++) { $muchos[] = $i('R', 'refuerzo', 10 - $k); } $muchos[] = $i('R', 'falso_concepto', 0);
ok(es_priorizar($muchos, $h)[0]['score'] === 4 + 3, 'la recurrencia se limita a 3');
$ord = es_priorizar([$i('X', 'laguna', 5), $i('Y', 'laguna', 1)], $h); ok(array_column($ord, 'pregunta') === ['Y', 'X'], 'a igual prioridad, primero la más reciente');
ok(es_priorizar([], $h) === [], 'sin intentos, sin refuerzo');
$grande = []; for ($k = 0; $k < 80; $k++) { $grande[] = $i("Q$k", 'refuerzo', 1); } ok(count(es_priorizar($grande, $h)) === ES_MAX_REFUERZO, 'tope de preguntas por reforzar');

/* ---- calibración real ---- */
$c = es_calibracion([['confianza' => 'alta', 'correcta' => 1], ['confianza' => 'alta', 'correcta' => 0], ['confianza' => 'baja', 'correcta' => 1], ['confianza' => null, 'correcta' => 1], ['confianza' => 'media', 'correcta' => 0]]);
ok($c['alta'] === ['n' => 2, 'aciertos' => 1] && $c['baja'] === ['n' => 1, 'aciertos' => 1] && $c['media'] === ['n' => 1, 'aciertos' => 0], 'calibración: cuenta solo intentos con confianza');

/* ---- Cloze: validación del servidor (espejo de cloze.js) ---- */
ok(fc_cloze_error('Pregunta normal sin marcas de hueco.') === '', 'una tarjeta normal no se toca');
ok(fc_cloze_error('El tratamiento de elección es la {{c1::penicilina benzatínica}} en dosis única.') === '', 'Cloze válida');
ok(fc_cloze_error('Texto {{c1::}} vacío del hueco y más contexto.') !== '', 'hueco vacío');
ok(fc_cloze_error('Texto con {{c1::llave sin cerrar y más contexto aquí.') !== '', 'llave sin cerrar');
ok(fc_cloze_error('{{c1::Todo el texto de la tarjeta está oculto}}') !== '', 'todo oculto');
ok(fc_cloze_error('Solo }} llaves {{ sueltas en este texto largo.') !== '', 'llaves fuera de un hueco');
ok(fc_cloze_error('La {{c1::penicilina::fármaco}} benzatínica es de elección en la sífilis.') === '', 'hueco con pista');
ok(fc_cloze_error('Anidado {{c1::uno {{c2::dos}} tres}} en un texto largo aquí.') !== '', 'no se permiten huecos anidados');
echo $f ? "$f fallos de $n\n" : "OK: $n comprobaciones de confianza, repaso y Cloze\n";
exit($f ? 1 : 0);
