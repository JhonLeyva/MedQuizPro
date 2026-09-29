# MedQuizPro — landing page + tutor de IA

Landing interactiva para una plataforma de preguntas tipo **ENAM / Residentado Médico (RM) / EsSalud**,
con un **chatbot de inteligencia artificial** en la esquina inferior derecha.
Sitio estático (HTML, CSS y JavaScript sin dependencias ni compilación) + un único archivo PHP
que hace de puente con el modelo de IA.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La página, incluido el widget de chat. Todo el contenido está en el HTML; el JS solo lo enriquece. |
| `styles.css` | Estilos y paleta, con tema claro y tema oscuro. |
| `main.js` | Interacciones: menú móvil, pregunta de muestra, filtro de bancos, cuenta regresiva, registro y **el chatbot**. |
| `api.php` | El backend del chatbot. Recibe el mensaje, llama al modelo de IA con la llave del servidor y devuelve el texto. |
| `config.example.php` | Plantilla de configuración para hostings sin variables de entorno. Se copia como `config.php`. |
| `.env.example` | Las variables de entorno que hay que definir (forma recomendada). |
| `.htaccess` | Caché, compresión y bloqueo del acceso web a `config.php` y `.env`. |
| `build-artifact.mjs` | Regenera `artifact.html` a partir de los tres archivos de la página. |
| `artifact.html` | La misma página en un solo archivo, para publicarla donde solo se admite una página (sin chat: no hay PHP detrás). |

## El chatbot

```
Navegador  →  POST /api.php  →  API del modelo de IA  →  respuesta  →  widget
```

La llave **nunca** sale del servidor: el navegador solo habla con `api.php`.
En el código del frontend no hay ninguna credencial, ni el mensaje de sistema del tutor.

Lo que hace el widget:

- botón flotante abajo a la derecha;
- pantalla inicial con «Hola 👋 ¿En qué puedo ayudarte?» y tres ejemplos que se pueden pulsar;
- escribir y enviar con **Enter** (Mayús+Enter salta de línea);
- indicador de «escribiendo…» mientras espera;
- **mantiene el contexto**: reenvía los últimos 10 turnos, así que «¿y sus síntomas?» sigue hablando del tema anterior;
- botones de **nueva conversación**, **minimizar** (guarda la conversación) y **cerrar** (la termina);
- la conversación sobrevive a recargar la página mientras dure la pestaña (`sessionStorage`), y se borra al cerrarla;
- funciona en escritorio, tablet y móvil (en móvil se abre como hoja inferior);
- ante cualquier fallo muestra un mensaje amable, nunca un error técnico.

### 1. Elegir proveedor y conseguir la llave

| `AI_PROVIDER` | Dónde se saca la llave | Notas |
|---|---|---|
| `gemini` *(por defecto)* | <https://aistudio.google.com/apikey> | Tiene plan gratuito. El modelo se detecta solo. |
| `openai` | <https://platform.openai.com/api-keys> | También sirve para cualquier API compatible con OpenAI (Groq, DeepSeek, OpenRouter, Together…) poniendo `AI_BASE_URL`. |
| `anthropic` | <https://console.anthropic.com/settings/keys> | Claude. |

### 2. Poner la llave en el servidor

**Recomendado: variables de entorno** (en Hostinger: hPanel → Sitios web → Avanzado → Variables de entorno).
Las nombres están en `.env.example`:

```
AI_API_KEY=tu-llave
AI_PROVIDER=gemini
AI_MODEL=
```

**Alternativa** si el hosting no las admite:

```
cp config.example.php config.php
```

y escribir la llave dentro. `config.php` está en `.gitignore` y el `.htaccess` impide abrirlo
desde el navegador. Las variables de entorno tienen prioridad sobre `config.php`.

### 3. Cambiar el modelo más adelante

Solo hay que cambiar `AI_MODEL` (o `ai_model` en `config.php`) y recargar. No se toca el código.

- **Gemini**: déjalo **vacío** y `api.php` le pregunta a Google qué modelos admite la llave
  y elige el mejor disponible (`gemini-3.0-flash` → `2.5-flash` → `2.0-flash` → `flash-latest`),
  guardando la elección 6 horas en caché. Si un modelo se retira, lo detecta y vuelve a elegir solo.
  Para fijar uno a mano: `AI_MODEL=gemini-2.5-flash`.
- **OpenAI**: `AI_MODEL=gpt-4o-mini` (o el que prefieras).
- **Anthropic**: `AI_MODEL=claude-opus-5`.
- **Otro proveedor compatible con OpenAI**: `AI_PROVIDER=openai` + `AI_BASE_URL=https://api.groq.com/openai/v1` + `AI_MODEL=…`.

### 4. Comprobar que funciona

```
curl https://tudominio.com/api.php?accion=estado
→ {"listo":true}            (false = falta la llave)

curl -X POST https://tudominio.com/api.php \
     -H 'Content-Type: application/json' \
     -d '{"mensaje":"¿Qué es la insuficiencia cardíaca?"}'
```

Y en la web: abrir el botón del chat y escribir una pregunta.

Si algo falla, poner una palabra secreta en `AI_DIAGNOSTICO_TOKEN` y abrir:

```
https://tudominio.com/api.php?accion=diagnostico&token=TU-PALABRA
```

Dice qué proveedor está activo, si la llave está puesta (nunca la muestra) y, con Gemini,
la lista exacta de modelos que ve la llave. `AI_DEBUG=1` añade además el detalle técnico
del error a la respuesta del chat; vuelve a ponerlo en `0` cuando termines.

### Límites de uso

Como el chat es público, `api.php` cuenta las peticiones por dirección IP:
**10 por minuto** y **150 al día** (`AI_LIMITE_MINUTO` y `AI_LIMITE_DIA`).
Al pasarse responde `429` con un aviso amable. Además rechaza las peticiones que
llegan desde otro dominio.

### El protocolo

`POST /api.php` con `Content-Type: application/json`:

```json
{ "mensaje": "¿Cómo diferencio shock séptico de cardiogénico?",
  "historial": [ { "rol": "usuario", "texto": "…" }, { "rol": "tutor", "texto": "…" } ] }
```

También acepta los nombres en inglés (`message`, `history`, `role`, `text`).

Respuesta correcta — `200`:

```json
{ "respuesta": "El shock séptico es distributivo…", "reply": "…" }
```

Fallo — el cuerpo solo trae un texto para enseñar al usuario; el motivo real queda
en el log de errores del servidor:

```json
{ "error": "Lo siento, no pude procesar tu mensaje. Inténtalo nuevamente." }
```

### Ajustes de `api.php`

| Constante | Valor | Qué hace |
|---|---|---|
| `MAX_CARACTERES` | 2000 | Largo máximo de un mensaje. |
| `MAX_HISTORIAL_TURNOS` | 10 | Turnos de conversación que se reenvían como contexto. |
| `LIMITE_MINUTO_DEF` / `LIMITE_DIA_DEF` | 10 / 150 | Límite por IP (se pueden cambiar por variable de entorno). |
| `MAX_TOKENS_RESPUESTA` | 900 | Largo máximo de la respuesta. |
| `TEMPERATURA` | 0.4 | Cuánto se permite improvisar al modelo. |
| `CACHE_MODELO_SEGUNDOS` | 21600 | Cuánto dura en caché el modelo elegido (solo Gemini). |
| `INSTRUCCION` | — | El papel del tutor. Solo existe en el servidor. |

Requisitos del hosting: **PHP 8.0 o superior** con la extensión cURL activada
(Hostinger la trae activada por defecto).

## Secciones de la página

- **Portada** con una pregunta de examen que se puede responder ahí mismo (tres preguntas rotativas con explicación).
- **Bancos de Preguntas** — marcador de posición, filtrable por ENAM / RM / EsSalud.
- **Simulacros Gratis** — marcador de posición, con cuenta regresiva al próximo simulacro abierto.
- **Cómo funciona** — tres pasos.
- **Registro** — formulario con validación en el navegador (no envía datos a ningún servidor).
- **Tutor** — el chatbot descrito arriba.

## Ver la página en local

El chat necesita PHP, así que conviene levantar el servidor de PHP:

```
AI_API_KEY=tu-llave php -S localhost:8000
```

y abrir <http://localhost:8000>. Con `python3 -m http.server` la página se ve,
pero el chat responderá con el mensaje de error (no hay PHP detrás).

## Publicar

Subir `index.html`, `styles.css`, `main.js`, `api.php`, `config.example.php` y `.htaccess`
a la raíz del hosting (`public_html`), y definir allí `AI_API_KEY` (o crear `config.php`).
Al cambiar los estilos o el script, subir el número de versión de `?v=20260925`
en `index.html` para que el navegador no sirva la copia vieja.

`artifact.html` se genera con `node build-artifact.mjs` y va sin el widget de chat,
porque un archivo suelto no tiene un servidor donde guardar la llave.

Las cifras, los bancos y las fechas son contenido de ejemplo.
