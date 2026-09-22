# MedQuizPro — landing page

Landing interactiva para una plataforma de preguntas tipo **ENAM / Residentado Médico (RM) / EsSalud**.
Sitio estático: HTML, CSS y JavaScript sin dependencias ni compilación.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La página. Todo el contenido está escrito en el HTML, el JS solo lo enriquece. |
| `styles.css` | Estilos y paleta, con tema claro y tema oscuro. |
| `main.js` | Interacciones: menú móvil, pregunta de muestra, filtro de bancos, cuenta regresiva, contadores y validación del registro. |
| `api.php` | Recibe la pregunta del chat, la reenvía a Gemini con cURL y devuelve la respuesta en JSON. |
| `config.example.php` | Plantilla de configuración. Se copia como `config.php` y ahí va la llave de Gemini. |
| `.htaccess` | Caché, compresión y bloqueo del acceso web a `config.php`. |
| `artifact.html` | La misma página compilada en un solo archivo, para publicarla en un sitio que solo acepta una página. |

## Secciones

- **Portada** con una pregunta de examen que se puede responder ahí mismo (tres preguntas rotativas con explicación).
- **Bancos de Preguntas** — marcador de posición, filtrable por ENAM / RM / EsSalud.
- **Simulacros Gratis** — marcador de posición, con cuenta regresiva al próximo simulacro abierto.
- **Cómo funciona** — tres pasos.
- **Registro** — formulario con validación en el navegador (no envía datos a ningún servidor).
- **Tutor** — widget de chat flotante que consulta a Gemini a través de `api.php`.

## El chat (tutor)

El navegador nunca ve la llave de Gemini. El widget envía la pregunta por `POST` a
`/api.php`, y es el servidor el que llama a Gemini y devuelve la respuesta.

### Cómo se elige el modelo

Google retira modelos y renombra identificadores, así que **el nombre del modelo no
está fijado en el código**. En cada arranque `api.php`:

1. Pregunta a Google qué modelos admite esta llave (endpoint `ListModels`), probando
   primero `v1beta` y después `v1`.
2. Elige el primero de `MODELOS_PREFERIDOS` que exista de verdad —
   `gemini-3.0-flash`, luego `gemini-2.5-flash`, `gemini-2.0-flash`,
   `gemini-flash-latest`. Si ninguno está, acepta variantes con sufijo
   (`gemini-3.0-flash-001`) y, en último caso, cualquier Gemini «flash» disponible.
3. Guarda la elección en caché 6 horas para no repetir la consulta.
4. Si aun así una petición devuelve 404 o `NOT_FOUND`, descarta la caché, vuelve a
   preguntar a Google y reintenta una vez.

Por eso el error «this model is no longer available» no puede repetirse: el código
se adapta solo. Para fijar un modelo a mano, se escribe su nombre en
`gemini_model` dentro de `config.php`.

### Diagnóstico

Si algo falla, pon una palabra secreta en `diagnostico_token` (en `config.php`) y abre:

```
https://tudominio.com/api.php?accion=diagnostico&token=TU-PALABRA
```

Devuelve la lista exacta de modelos que ve tu llave, en qué versión de la API, y
cuál eligió. Es lo primero que hay que mirar ante cualquier 404.

### Configurar la llave

En el servidor, en la misma carpeta que `api.php`:

```
cp config.example.php config.php
```

y dentro se escribe la llave, que se obtiene en <https://aistudio.google.com/apikey>:

```php
return [
    'gemini_api_key'    => 'AIza...',
    'gemini_model'      => '',          // vacío = se elige solo
    'diagnostico_token' => 'loquesea',  // vacío = diagnóstico desactivado
];
```

`config.php` está en `.gitignore` y el `.htaccess` impide abrirlo desde el navegador.
Si el hosting permite variables de entorno, `GEMINI_API_KEY` también sirve y tiene prioridad.

### Cómo se comunican

`POST /api.php` con `Content-Type: application/json`:

```json
{ "mensaje": "¿Cómo diferencio shock séptico de cardiogénico?",
  "historial": [ { "rol": "usuario", "texto": "…" }, { "rol": "tutor", "texto": "…" } ] }
```

También acepta los nombres en inglés (`message`, `history`, `role`, `text`).

Respuesta correcta — `200`. El texto viene por partida doble, para que valga
cualquier cliente:

```json
{ "respuesta": "El shock séptico es distributivo…",
  "reply":     "El shock séptico es distributivo…",
  "modelo":    "gemini-3.0-flash",
  "api_version": "v1beta" }
```

Fallo — se devuelve el código de Google (o `502` si no se llegó a hablar con él):

```json
{ "error": "Google HTTP 429 (RESOURCE_EXHAUSTED): Quota exceeded…",
  "origen": "gemini",
  "google_codigo": 429,
  "google_estado": "RESOURCE_EXHAUSTED",
  "modelo": "gemini-3.0-flash" }
```

El campo `origen` dice dónde se rompió: `configuracion`, `listado_de_modelos`,
`red` o `gemini`.

### Ajustes de `api.php`

| Constante | Valor | Qué hace |
|---|---|---|
| `MODELOS_PREFERIDOS` | 3.0-flash → 2.5-flash → 2.0-flash → flash-latest | Orden de preferencia. |
| `VERSIONES_API` | `v1beta`, `v1` | Versiones que se prueban, en orden. |
| `MAX_CARACTERES` | 1500 | Largo máximo de la pregunta. |
| `MAX_HISTORIAL_TURNOS` | 8 | Turnos de conversación que se reenvían. |
| `LIMITE_POR_MINUTO` | 12 | Preguntas por IP y por minuto, para que nadie agote la llave. |
| `CACHE_MODELO_SEGUNDOS` | 21600 | Cuánto dura la elección de modelo en caché. |
| `DETALLE_ERRORES` | `true` | Si el mensaje textual de Google llega al navegador. Ponlo en `false` cuando todo funcione. |

`generationConfig`: `temperature` 0.4 y `maxOutputTokens` 800.

Requisitos del hosting: PHP 7.4 o superior con la extensión cURL activada
(Hostinger la trae activada por defecto).

## Ver la página

Basta abrir `index.html` en el navegador, o servirla:

```
python3 -m http.server 8000
```

## Publicar

Subir `index.html`, `styles.css`, `main.js`, `api.php`, `config.example.php` y `.htaccess`
a la raíz del hosting (`public_html`), y crear allí `config.php` con la llave.
Al cambiar los estilos o el script, subir el número de versión de `?v=20260923`
en `index.html` para que el navegador no sirva la copia vieja.

El chat necesita PHP, así que en `file://` o en un alojamiento estático el widget se
muestra pero responde con un error de conexión. Por eso `artifact.html` se genera
sin el widget.

Las cifras, los bancos y las fechas son contenido de ejemplo.
