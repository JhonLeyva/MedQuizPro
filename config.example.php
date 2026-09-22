<?php
/**
 * Copia este archivo como config.php y escribe tu llave de Gemini.
 *
 *   cp config.example.php config.php
 *
 * config.php NO debe subirse a Git ni compartirse: contiene tu llave.
 * La llave se obtiene en https://aistudio.google.com/apikey
 */

return [
    // Obligatorio. Tu llave de Google AI Studio.
    'gemini_api_key' => 'PEGA-AQUI-TU-LLAVE-DE-GEMINI',

    // Opcional. Déjalo vacío y api.php le pregunta a Google qué modelos admite
    // tu llave y elige el mejor disponible. Solo escribe un nombre aquí si
    // quieres fijar uno concreto, por ejemplo 'gemini-3.0-flash'.
    'gemini_model' => '',

    // Opcional. Palabra secreta para abrir el diagnóstico desde el navegador:
    //   https://tudominio.com/api.php?accion=diagnostico&token=LA-PALABRA
    // Te dice exactamente qué modelos ve tu llave. Déjalo vacío para desactivarlo.
    'diagnostico_token' => '',
];
