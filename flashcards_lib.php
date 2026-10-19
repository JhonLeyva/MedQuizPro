<?php
/**
 * Flashcards de MedQuizPlus: repaso espaciado.
 *
 * Planificador propio, determinista y documentado (variante de SM-2 con pasos de aprendizaje).
 * No es FSRS: FSRS necesita pesos entrenados con datos de repaso reales y hoy no los hay.
 * Si más adelante hay datos suficientes, basta con reemplazar planificar() (misma firma).
 *
 *  estado          nuevo | aprendiendo | repaso | reaprendiendo
 *  facilidad       multiplicador de intervalo (empieza en 2.5; mínimo 1.3)
 *  intervalo       días del último intervalo de "repaso"
 *
 *  nuevo / aprendiendo:   otra_vez → 10 min · dificil → 1 día · bien → 1 día · facil → 4 días
 *  repaso:   otra_vez → lapso: 10 min, el intervalo se reduce a la mitad (mín. 1 día), facilidad −0.20
 *            dificil → ×1.2 (al menos +1 día), facilidad −0.15
 *            bien    → ×facilidad (al menos +1 día)
 *            facil   → ×facilidad×1.3 (al menos +1 día), facilidad +0.15
 *  reaprendiendo:   otra_vez → 10 min · dificil → 1 día · bien/facil → el intervalo ya reducido
 *  Intervalo máximo: 365 días.
 *
 * Crear o guardar una tarjeta NO la marca como conocida: nace "nuevo" y vence de inmediato.
 */

const FC_CALIFICACIONES = ['otra_vez', 'dificil', 'bien', 'facil'];
const FC_MAX_DIAS = 365;
const FC_PASO_MIN = 10;

/** @param array $t fila de la tarjeta (estado, facilidad, intervalo, repeticiones, lapsos) */
function fc_planificar(array $t, string $cal, int $ahora): array {
    if (!in_array($cal, FC_CALIFICACIONES, true)) throw new InvalidArgumentException('calificación no válida');
    $estado = (string)($t['estado'] ?? 'nuevo');
    $fac = (float)($t['facilidad'] ?? 2.5);
    $int = (int)($t['intervalo'] ?? 0);
    $rep = (int)($t['repeticiones'] ?? 0);
    $lap = (int)($t['lapsos'] ?? 0);
    $dia = 86400;
    $r = ['estado' => $estado, 'facilidad' => $fac, 'intervalo' => $int, 'repeticiones' => $rep + 1, 'lapsos' => $lap, 'proximo' => $ahora];

    if ($estado === 'nuevo' || $estado === 'aprendiendo') {
        if ($cal === 'otra_vez') { $r['estado'] = 'aprendiendo'; $r['proximo'] = $ahora + FC_PASO_MIN * 60; }
        elseif ($cal === 'dificil') { $r['estado'] = 'repaso'; $r['intervalo'] = 1; $r['facilidad'] = max(1.3, $fac - 0.15); $r['proximo'] = $ahora + $dia; }
        elseif ($cal === 'bien') { $r['estado'] = 'repaso'; $r['intervalo'] = 1; $r['proximo'] = $ahora + $dia; }
        else { $r['estado'] = 'repaso'; $r['intervalo'] = 4; $r['facilidad'] = $fac + 0.15; $r['proximo'] = $ahora + 4 * $dia; }
    } elseif ($estado === 'reaprendiendo') {
        if ($cal === 'otra_vez') { $r['proximo'] = $ahora + FC_PASO_MIN * 60; }
        elseif ($cal === 'dificil') { $r['estado'] = 'repaso'; $r['intervalo'] = max(1, $int); $r['proximo'] = $ahora + $dia; }
        else { $r['estado'] = 'repaso'; $r['intervalo'] = max(1, $int); $r['proximo'] = $ahora + max(1, $int) * $dia; }
    } else {   // repaso
        if ($cal === 'otra_vez') {
            $r['estado'] = 'reaprendiendo'; $r['lapsos'] = $lap + 1; $r['facilidad'] = max(1.3, $fac - 0.20);
            $r['intervalo'] = max(1, (int)round($int * 0.5)); $r['proximo'] = $ahora + FC_PASO_MIN * 60;
        } else {
            if ($cal === 'dificil') { $n = max($int + 1, (int)round($int * 1.2)); $r['facilidad'] = max(1.3, $fac - 0.15); }
            elseif ($cal === 'bien') { $n = max($int + 1, (int)round($int * $fac)); }
            else { $n = max($int + 1, (int)round($int * $fac * 1.3)); $r['facilidad'] = $fac + 0.15; }
            $r['intervalo'] = min(FC_MAX_DIAS, $n); $r['proximo'] = $ahora + $r['intervalo'] * $dia;
        }
    }
    $r['facilidad'] = round($r['facilidad'], 2);
    return $r;
}

/** Texto corto para el botón: "10 min", "1 día", "3 días", "2 meses". */
function fc_etiqueta(int $segundos): string {
    if ($segundos < 3600) return max(1, (int)round($segundos / 60)) . ' min';
    $d = (int)round($segundos / 86400);
    if ($d < 1) return '1 día';
    if ($d < 31) return $d . ($d === 1 ? ' día' : ' días');
    $m = (int)round($d / 30);
    return $m < 12 ? $m . ($m === 1 ? ' mes' : ' meses') : '1 año';
}

/** Intervalos que se mostrarán en cada botón antes de calificar. */
function fc_previas(array $t, int $ahora): array {
    $o = [];
    foreach (FC_CALIFICACIONES as $c) $o[$c] = fc_etiqueta(fc_planificar($t, $c, $ahora)['proximo'] - $ahora);
    return $o;
}

/** Huella para no duplicar tarjetas: misma pregunta de origen + mismo frente. */
function fc_huella(string $pregunta, string $frente): string {
    return hash('sha256', mb_strtolower(trim($pregunta)) . '|' . mb_strtolower(preg_replace('/\s+/u', ' ', trim($frente))));
}
