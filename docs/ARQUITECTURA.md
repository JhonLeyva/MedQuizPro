# MedQuizPlus — arquitectura y rediseño (octubre 2026)

## 1. Diagnóstico (Fase 1)
- **Stack:** sitio estático (HTML/CSS/JS vanilla, sin build) + `api.php` (tutor IA). Se despliega subiendo archivos a Hostinger.
- **Dos experiencias:** landing pública (`index.html`) y plataforma de estudio (`app/`, router por hash).
- **Datos (no se tocan):** `bancos/*.json`, `algoritmos.js`, `flujogramas/`, `api.php`, `.htaccess`. Todas las cifras visibles se cuentan en vivo desde los bancos (`[data-metrica]`).
- **Contratos conservados:** `window.MQP` (`catalogo.js`), `MQP.practica.abrir(cfg)`, evento `mqp:sesion-cerrada`, `mqp_progreso_v1` en localStorage, ids del quiz de muestra (`#quiz`, `#qStem`, `#qOptions`, `#qFeedback`, `#qVerdict`, `#qRing`…).
- **Real vs visual:** reales → bancos, simuladores (ENAM 2020 / rápido / por especialidad), flujogramas, tutor IA, progreso/falladas/favoritas (localStorage). Solo visuales → formulario de registro de la landing (demo, no hay cuentas), plan Premium («próximamente»), Residentado/EsSalud (solo preguntas tipo).
- **Problemas detectados:** la landing duplicaba el app (explorador de 17 especialidades + simuladores + sesión de práctica embebida); el quiz de muestra competía con el médico 3D en el hero; el app no tenía búsqueda de especialidades ni 404 real (rutas desconocidas caían en Inicio).

## 2. Arquitectura de información
| Nivel | Antes | Ahora |
|---|---|---|
| 1 Landing | Hero con quiz + doctor detrás, examenes, **explorador de bancos**, **sesión de práctica embebida**, simuladores, … | Hero (propuesta + médico 3D sobre plataforma) → Cifras → Exámenes → **Pruébalo** (quiz de muestra) → Simuladores → Cómo funciona → … → FAQ → CTA → footer |
| 2 Áreas | `app/#/inicio · examenes · banco · simuladores · progreso · falladas · favoritas · perfil` | igual (sin cambios de rutas) |
| 3 Categorías | `#/examenes/:id` con 17 tarjetas en 6 áreas | + **búsqueda** y **chips de área**; estado en la URL (`?q=…&area=…`) |
| 4 Configuración | `#/banco` (constructor) y `#/simuladores/:id` | sin cambios |
| 5 Estudio | pantalla de sesión (`body.en-sesion`) | sin cambios |

## 3. Rutas
Sin rutas eliminadas. Añadidas: `#/examenes/:id?q=&area=` (parámetros de filtro) y un manejo explícito de **ruta desconocida → «No encontramos esta sección»**. La landing ahora enlaza directo a `app/#/examenes/:id`, `app/#/banco` y `app/#/simuladores/:id`.

## 4. Hero (actualizado)
El médico 3D se retiró (`hero3d.js` y `Sin_nombre.glb` ya no están; siguen en el historial de Git si se quisieran recuperar). A la derecha del hero hay ahora una **pantalla de computador** que reproduce la plataforma resolviendo preguntas reales del banco (se sortean al cargar), con su comentario docente, un tarjeta con el flujograma de la pregunta y cifras reales bajo los botones. Código: `#heroShow` en `index.html`, `heroPantalla()` en `graficos.js`, estilos en `pro.css` §20.

## 5. Archivos
Inicio del app tipo "bienvenida", lista de bancos (`#/banco`, configurador en `#/banco/configurar`) y buscador global en la barra superior.

Modificados: `index.html`, `pro.css`, `pro.js`, `hero3d.js`. Añadidos al repo (copia de la versión en producción v20260930 + cambios): `catalogo.js` (solo se añadió el icono `lupa`), `app/index.html`, `app/app.js`, `app/app.css`.

## 6. Pendiente / limitaciones
- No hay autenticación ni cuentas: el registro de la landing es demostrativo; no se simuló nada nuevo.
- No se rediseñó el sistema visual completo del app (ya usa los tokens de `styles.css`); no hay página de planes dentro del app.
- Probado con Chromium + SwiftShader (sin GPU real) y datos de prueba; falta revisar en dispositivos reales y en Hostinger.
