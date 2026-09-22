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

### Configurar la llave

En el servidor, en la misma carpeta que `api.php`:

```
cp config.example.php config.php
```

y dentro de `config.php` se escribe la llave, que se obtiene en
<https://aistudio.google.com/apikey>:

```php
return ['gemini_api_key' => 'AIza...'];
```

`config.php` está en `.gitignore` y el `.htaccess` impide abrirlo desde el navegador.
Si el hosting permite variables de entorno, `GEMINI_API_KEY` también sirve y tiene prioridad.

### Cómo se comunican

`POST /api.php` con `Content-Type: application/json`:

```json
{ "mensaje": "¿Cómo diferencio shock séptico de cardiogénico?",
  "historial": [ { "rol": "usuario", "texto": "…" }, { "rol": "tutor", "texto": "…" } ] }
```

Respuesta correcta — `200`:

```json
{ "respuesta": "El shock séptico es distributivo…" }
```

Cualquier fallo devuelve `{ "error": "…" }` con un mensaje ya redactado para mostrarle
al usuario; el detalle técnico queda en el registro de errores de PHP, nunca en la respuesta.

### Ajustes de `api.php`

| Constante | Valor | Qué hace |
|---|---|---|
| `MODELO` | `gemini-2.5-flash` | Modelo de Gemini al que se pregunta. |
| `MAX_CARACTERES` | 1500 | Largo máximo de la pregunta. |
| `MAX_HISTORIAL` | 16 | Mensajes previos que se reenvían como contexto. |
| `LIMITE_POR_MINUTO` | 12 | Preguntas por IP y por minuto, para que nadie agote la llave. |

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
