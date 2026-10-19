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

    // Opcional. IPs del dueño (separadas por comas): usan el tutor de IA sin cuenta ni plan.
    // El resto de personas necesita cuenta y un plan activo. Déjalo vacío para que nadie salte esa regla.
    // Ojo: una IP la pueden compartir otras personas (redes móviles, oficinas). Una cuenta de dueño
    // (cuenta.php, dueno_activar) es más segura que una IP.
    'ips_libres' => '',

    // Opcional. Pon '1' si el hosting tiene definida una variable AI_API_KEY distinta y quieres que mande
    // la llave de este archivo. El diagnóstico (llave_origen) dice de dónde sale la llave en uso.
    'config_manda' => '',

    // Opcional. Clave de dueño (16 o más caracteres) para usar el tutor de IA sin cuenta desde cualquier equipo.
    // Abre UNA vez en cada navegador:  https://tudominio.com/api.php?accion=dueno&clave=TU-CLAVE
    // y queda activado un año. Más segura que una IP. Déjala vacía para desactivarla.
    'clave_dueno' => '',

    // Opcional. Límite de uso por visitante (por dirección IP).
    'limite_minuto' => 10,
    'limite_contexto_dia' => 40,                 // consultas diarias de IA con contexto por usuario
    'presupuesto_caracteres_dia' => 150000,      // presupuesto diario de IA por usuario (caracteres enviados + recibidos)
    'limite_dia'    => 150,

    // Opcional. Palabra secreta para abrir el diagnóstico desde el navegador:
    //   https://tudominio.com/api.php?accion=diagnostico&token=LA-PALABRA
    // Déjalo vacío para desactivarlo.
    'diagnostico_token' => '',

    // ---- Cuentas y cobro (cuenta.php) ----
    // PayU Latam (Perú): datos de tu comercio (Panel de PayU → Configuración técnica).
    'payu_merchant_id' => '', 'payu_account_id' => '', 'payu_api_key' => '',
    'payu_test' => '0',        // '1' = entorno de pruebas (sandbox)
    // 'payu' o 'mercadopago'. Si lo dejas vacío se usa PayU cuando está configurado.
    'pasarela' => '',

    // Token de acceso de tu aplicación de Mercado Pago (Tus integraciones → Credenciales de producción).
    // Sin él, la plataforma funciona con cuentas pero NO cobra.
    'mp_access_token' => '',
    // Clave secreta del webhook (Mercado Pago → Tus integraciones → Webhooks). Recomendada.
    'mp_webhook_secret' => '',
    // '1' activa los límites del plan gratuito (20 preguntas al día y simulacro completo solo Premium).
    // Déjalo en '0' hasta que el cobro esté probado.
    'limites' => '0',

    // Clave larga (16+ caracteres) para descargar tu lista de cuentas y pagos:
    //   https://TU-DOMINIO/cuenta.php?a=admin&token=TU-CLAVE   (CSV; añade &formato=json para JSON)
    'admin_token' => '',

    // Opcional. '1' añade el detalle técnico del error a la respuesta JSON.
    // Úsalo solo mientras configuras, y vuelve a dejarlo en '0'.
    'depurar' => '0',
];
