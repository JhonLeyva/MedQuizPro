# MedQuizPro — landing page

Landing interactiva para una plataforma de preguntas tipo **ENAM / Residentado Médico (RM) / EsSalud**.
Sitio estático: HTML, CSS y JavaScript sin dependencias ni compilación.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La página. Todo el contenido está escrito en el HTML, el JS solo lo enriquece. |
| `styles.css` | Estilos y paleta, con tema claro y tema oscuro. |
| `main.js` | Interacciones: menú móvil, pregunta de muestra, filtro de bancos, cuenta regresiva, contadores y validación del registro. |
| `.htaccess` | Caché y compresión para hosting Apache (Hostinger, cPanel). |
| `artifact.html` | La misma página compilada en un solo archivo, para publicarla en un sitio que solo acepta una página. |

## Secciones

- **Portada** con una pregunta de examen que se puede responder ahí mismo (tres preguntas rotativas con explicación).
- **Bancos de Preguntas** — marcador de posición, filtrable por ENAM / RM / EsSalud.
- **Simulacros Gratis** — marcador de posición, con cuenta regresiva al próximo simulacro abierto.
- **Cómo funciona** — tres pasos.
- **Registro** — formulario con validación en el navegador (no envía datos a ningún servidor).

## Ver la página

Basta abrir `index.html` en el navegador, o servirla:

```
python3 -m http.server 8000
```

## Publicar

Subir `index.html`, `styles.css`, `main.js` y `.htaccess` a la raíz del hosting.
Al cambiar los estilos o el script, subir el número de versión de `?v=20260922`
en `index.html` para que el navegador no sirva la copia vieja.

Las cifras, los bancos y las fechas son contenido de ejemplo.
