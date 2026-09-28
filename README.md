# MedQuizPlus — web pública + plataforma de estudio

Preparación para el **ENAM**, el **Residentado Médico** y **EsSalud**.
Sitio estático (HTML, CSS y JavaScript sin dependencias ni compilación) + un único archivo PHP
para el tutor de IA. Dos experiencias separadas:

```
MEDQUIZPLUS
├── WEB PÚBLICA  (index.html)          descubrir → entender → probar → registrarse
│   Hero con pregunta interactiva, cifras reales, selección de examen,
│   bancos por examen y especialidad, simuladores, cómo funciona,
│   características, vista previa, planes, registro, FAQ, CTA y pie.
│
└── PLATAFORMA   (app/index.html)      entrenar → resolver → analizar → mejorar
    #/inicio · #/examenes[/enam|residentado|essalud] · #/banco · #/simuladores[/id]
    #/progreso · #/falladas · #/favoritas · #/perfil
```

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | Web pública. |
| `app/index.html`, `app/app.js`, `app/app.css` | Plataforma de estudio: enrutador por `#/ruta` y sus vistas. |
| `catalogo.js` | **Datos compartidos**: exámenes, áreas, especialidades, simuladores, carga de bancos y progreso del estudiante. |
| `main.js` | Componentes compartidos: motor de práctica (modo estudio y modo simulacro), tarjetas de especialidad, modo simulación (tachado, bandera, Active Recall, ritmo de 60 s, atajos), visor de flujogramas, chat, tema y la interacción de la web pública. |
| `styles.css` | Sistema visual (tokens, claro/oscuro) y estilos de la web pública y del simulador. |
| `algoritmos.js` + `flujogramas/` | Flujograma de cada pregunta. |
| `bancos/*.json` | Las preguntas: un archivo por especialidad. |
| `api.php`, `config.example.php`, `.env.example` | Backend del tutor de IA. |
| `.htaccess` | Caché, compresión y bloqueo de `config.php` y `.env`. |
| `build-artifact.mjs` → `artifact.html` | La web pública en un solo archivo (sin chat ni plataforma). |
| `verificar-flujogramas.html` | Diagnóstico de los SVG en el servidor. |

## Regla de datos

Nada de cifras de ejemplo. Todo número visible se **cuenta en vivo** desde `bancos/*.json`
(preguntas, preguntas oficiales, especialidades, flujogramas, preguntas y tiempo de cada simulador)
o sale de las respuestas del propio estudiante. El HTML trae los valores actuales solo como respaldo.

- Los precios del plan Premium no están definidos: la tarjeta dice «Próximamente».
- Residentado y EsSalud aparecen como módulos «Próximamente» con sus especialidades; las preguntas
  tipo que ya existen (`examen_origen` «Residentado…» / «EsSalud…») se pueden practicar.
- El progreso (respuestas, falladas, favoritas, sesiones) se guarda en `localStorage`
  (`mqp_progreso_v1`) de ese navegador. El registro sigue siendo una demostración.

## Cómo crece sin rediseñar

- **Nueva pregunta**: se añade a su `bancos/<archivo>.json`. `examen_origen` decide el examen
  (empieza por `ENAM`, `Residentado` o `EsSalud`). Todas las cifras se actualizan solas.
- **Nueva especialidad**: nuevo `.json` + una línea en `ESPECIALIDADES` de `catalogo.js`.
- **Abrir Residentado o EsSalud**: cargar sus preguntas y cambiar `estado` a `"disponible"` en `EXAMENES`
  y en su simulador de `SIMULADORES`.
- **Nuevo simulador**: una entrada en `SIMULADORES` (examen, filtro de origen, cantidad, orden).
- **Categorías** dentro de una especialidad: campo `categorias: []` reservado; hoy las preguntas
  oficiales traen `tema`, que se muestra en cada pregunta.
- **Cuentas de usuario**: reemplazar `leer()`/`escribir()` de `MQP.progreso` por llamadas a la API;
  la plataforma no cambia.

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

## Ver la página en local

El chat necesita PHP, así que conviene levantar el servidor de PHP:

```
AI_API_KEY=tu-llave php -S localhost:8000
```

y abrir <http://localhost:8000>. Con `python3 -m http.server` la página se ve,
pero el chat responderá con el mensaje de error (no hay PHP detrás).

## Publicar

Subir a la raíz del hosting (`public_html`): `index.html`, `styles.css`, `catalogo.js`, `main.js`,
`algoritmos.js`, las carpetas `app/`, `bancos/` y `flujogramas/`, `api.php`, `config.example.php`
y `.htaccess`; y definir allí `AI_API_KEY` (o crear `config.php`).
La plataforma queda en `https://tudominio.com/app/`.
Al cambiar estilos o scripts, subir el número de versión de `?v=` en `index.html` y `app/index.html`.

`artifact.html` se genera con `node build-artifact.mjs` y va sin el widget de chat ni la plataforma,
porque un archivo suelto no tiene servidor detrás.
