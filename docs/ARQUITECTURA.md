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

## 4. Hero y médico 3D (`index.html`, `pro.css` §17-18, `pro.js`, `hero3d.js`)
- Texto/CTA a la izquierda; escenario `#heroStage` a la derecha con el médico centrado a ~75 % del ancho, ~65 % del alto visible, ligeramente girado hacia el texto.
- `hero3d.js`: plataforma circular baja (blanco mate, borde turquesa sutil), sombra de contacto y sombra ambiente, cámara con 9° de elevación (`CONFIG.pedestal`, `framing`, `cameraElevationDeg`, `lookDown`). Se mantiene `AnimationMixer`/idle procedural, seguimiento limitado del cursor, `prefers-reduced-motion`, pausa fuera de pantalla.
- Sin WebGL o sin modelo: el escenario muestra los anillos CSS (`.orbit--static`), la landing sigue funcionando.
- Móvil/tablet: el escenario baja bajo el texto (300–400 px), tarjetas auxiliares ocultas.

## 5. Archivos
Inicio del app tipo "bienvenida", lista de bancos (`#/banco`, configurador en `#/banco/configurar`) y buscador global en la barra superior.

Modificados: `index.html`, `pro.css`, `pro.js`, `hero3d.js`. Añadidos al repo (copia de la versión en producción v20260930 + cambios): `catalogo.js` (solo se añadió el icono `lupa`), `app/index.html`, `app/app.js`, `app/app.css`.

## 6. Pendiente / limitaciones
- No hay autenticación ni cuentas: el registro de la landing es demostrativo; no se simuló nada nuevo.
- No se rediseñó el sistema visual completo del app (ya usa los tokens de `styles.css`); no hay página de planes dentro del app.
- Probado con Chromium + SwiftShader (sin GPU real) y datos de prueba; falta revisar en dispositivos reales y en Hostinger.
