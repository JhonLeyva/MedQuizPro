<?php
/**
 * Estudio con evidencia: confianza por intento y «Repaso de hoy». Lógica pura (sin red ni base de datos).
 *
 * La CONFIANZA es un dato metacognitivo: no cambia el puntaje ni se confunde con el recuerdo. El servidor decide si el intento fue
 * correcto (compara con la clave del banco) y calcula la etiqueta; el navegador solo informa la letra y el nivel de confianza.
 *   fallo + seguro            → falso_concepto  («Falso concepto de alta prioridad»)
 *   fallo + adiviné/dudaba    → refuerzo        (dificultad; NO se asume una creencia errónea consolidada)
 *   fallo sin indicar         → refuerzo
 *   acierto + adiviné         → laguna          (posible laguna de comprensión)
 *   acierto + dudaba          → acierto_dudoso
 *   acierto + seguro          → acierto_seguro  (se registra; no se declara dominio del tema)
 *   acierto sin indicar       → acierto
 * Pruebas: php tests/estudio_test.php
 */
declare(strict_types=1);

const ES_CONFIANZAS = ['baja', 'media', 'alta'];
const ES_PENDIENTES = ['falso_concepto', 'refuerzo', 'laguna', 'acierto_dudoso'];
const ES_PESO = ['falso_concepto' => 4, 'refuerzo' => 3, 'laguna' => 2, 'acierto_dudoso' => 1];
const ES_VENTANA_DIAS = 180;
const ES_MAX_REFUERZO = 30;
const ES_TEXTOS = [
    'falso_concepto' => 'Falso concepto de alta prioridad',
    'refuerzo' => 'Necesita refuerzo',
    'laguna' => 'Posible laguna de comprensión',
    'acierto_dudoso' => 'Acierto con dudas',
    'acierto_seguro' => 'Acierto con seguridad',
    'acierto' => 'Acierto',
];

function es_etiqueta(bool $acierto, ?string $confianza): string
{
    if ($confianza !== null && !in_array($confianza, ES_CONFIANZAS, true)) { throw new InvalidArgumentException('confianza no válida'); }
    if (!$acierto) { return $confianza === 'alta' ? 'falso_concepto' : 'refuerzo'; }
    return match ($confianza) { 'baja' => 'laguna', 'media' => 'acierto_dudoso', 'alta' => 'acierto_seguro', default => 'acierto' };
}

/**
 * Preguntas por reforzar. Una pregunta está pendiente si la etiqueta de su ÚLTIMO intento es pendiente; sale de la lista cuando un intento
 * posterior es un acierto. Prioridad = peso de la etiqueta (4/3/2/1) + recurrencia (intentos anteriores pendientes, máx. 3). No es FSRS ni un
 * calendario: es una regla simple y explicable. Un solo acierto seguro no declara dominio: solo saca la pregunta de esta lista.
 * @param array<int,array{pregunta:string,etiqueta:string,t:int}> $intentos cualquier orden
 * @return array<int,array{pregunta:string,etiqueta:string,score:int,intentos:int,pendientes_previos:int,ultimo:int}>
 */
function es_priorizar(array $intentos, int $ahora): array
{
    $desde = $ahora - ES_VENTANA_DIAS * 86400;
    $por = [];
    foreach ($intentos as $i) { if ($i['t'] >= $desde) { $por[$i['pregunta']][] = $i; } }
    $o = [];
    foreach ($por as $id => $lista) {
        usort($lista, static fn($a, $b) => $a['t'] <=> $b['t']);
        $ult = $lista[count($lista) - 1];
        if (!in_array($ult['etiqueta'], ES_PENDIENTES, true)) { continue; }
        $prev = 0;
        foreach (array_slice($lista, 0, -1) as $x) { if (in_array($x['etiqueta'], ES_PENDIENTES, true)) { $prev++; } }
        $o[] = ['pregunta' => (string) $id, 'etiqueta' => $ult['etiqueta'], 'score' => ES_PESO[$ult['etiqueta']] + min(3, $prev), 'intentos' => count($lista), 'pendientes_previos' => $prev, 'ultimo' => $ult['t']];
    }
    usort($o, static fn($a, $b) => [$b['score'], $b['ultimo']] <=> [$a['score'], $a['ultimo']]);
    return array_slice($o, 0, ES_MAX_REFUERZO);
}

/** Calibración real: de las veces que marcó cada nivel de confianza, cuántas acertó (con n visible: pocos datos no concluyen nada). */
function es_calibracion(array $intentos): array
{
    $c = ['baja' => ['n' => 0, 'aciertos' => 0], 'media' => ['n' => 0, 'aciertos' => 0], 'alta' => ['n' => 0, 'aciertos' => 0]];
    foreach ($intentos as $i) {
        if (!isset($c[$i['confianza'] ?? ''])) { continue; }
        $c[$i['confianza']]['n']++;
        if (!empty($i['correcta'])) { $c[$i['confianza']]['aciertos']++; }
    }
    return $c;
}
