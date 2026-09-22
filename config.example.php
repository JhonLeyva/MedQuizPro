<?php
/**
 * Configuración del tutor de IA — SOLO para hostings donde no se pueden
 * definir variables de entorno.
 *
 * Si tu hosting permite variables de entorno (Hostinger, cPanel, Plesk, Docker…),
 * usa AI_API_KEY / AI_MODEL / AI_PROVIDER y NO crees este archivo: es más seguro.
 *
 * Para usarlo:
 *
 *   cp config.example.php config.php
 *
 * y escribe tu llave abajo. config.php está en .gitignore y el .htaccess impide
 * abrirlo desde el navegador: nunca se sube a Git ni se comparte.
 */

return [
    // Obligatorio. La llave de tu proveedor de IA.
    //   Gemini    → https://aistudio.google.com/apikey   (tiene plan gratuito)
    //   OpenAI    → https://platform.openai.com/api-keys
    //   Anthropic → https://console.anthropic.com/settings/keys
    'ai_api_key' => 'PEGA-AQUI-TU-LLAVE',

    // 'gemini' (por defecto), 'openai' o 'anthropic'.
    'ai_provider' => 'gemini',

    // Opcional. El nombre del modelo.
    // Con Gemini, déjalo vacío: api.php le pregunta a Google qué modelos admite
    // tu llave y elige el mejor disponible.
    // Con OpenAI, por ejemplo 'gpt-4o-mini'. Con Anthropic, 'claude-opus-5'.
    'ai_model' => '',

    // Opcional. Solo para APIs con el mismo formato que OpenAI
    // (Groq, DeepSeek, OpenRouter, Together…). Ejemplo:
    // 'ai_base_url' => 'https://api.groq.com/openai/v1',
    'ai_base_url' => '',

    // Opcional. Límite de uso por visitante (por dirección IP).
    'limite_minuto' => 10,
    'limite_dia'    => 150,

    // Opcional. Palabra secreta para abrir el diagnóstico desde el navegador:
    //   https://tudominio.com/api.php?accion=diagnostico&token=LA-PALABRA
    // Déjalo vacío para desactivarlo.
    'diagnostico_token' => '',

    // Opcional. '1' añade el detalle técnico del error a la respuesta JSON.
    // Úsalo solo mientras configuras, y vuelve a dejarlo en '0'.
    'depurar' => '0',
];
