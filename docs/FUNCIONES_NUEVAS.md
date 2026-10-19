# Funciones nuevas (flashcards, rendimiento, Sobrevive a la Guardia, Preguntar a la IA)

Detalle de las flashcards: `FLASHCARDS.md`.

## Rendimiento y plan de estudio (`rendimiento.js`, en «Mi progreso»)
Estadística descriptiva sobre los resultados reales del alumno (último intento de cada pregunta + simulacros completados).
- Muestra por separado: aciertos actuales, último simulacro, **estimación a futuro** y su incertidumbre.
- La estimación (rango de % de aciertos, intervalo de Wilson al 95 %) solo aparece con ≥100 preguntas respondidas **y** ≥2 simulacros de ≥20 preguntas; si no, dice qué falta.
- **No hay nota ENAM proyectada**: la escala del examen no está validada contra datos.
- Prioridad de estudio = 50 % bajo acierto (con prior Beta(1,1)) + 20 % peso en el banco + 15 % incertidumbre + 15 % tiempo sin practicar; cada tema explica sus motivos. «Peso» = tamaño de la especialidad en este banco, no el blueprint oficial.
- Pruebas: `node tests/rendimiento_test.js`.

## Sobrevive a la Guardia (`guardia_casos.js`, `guardia.js`, ruta `#/guardia`)
Casos clínicos como **grafo de decisiones fijo** (no depende de IA). 5 casos: crisis asmática, apendicitis, diarrea en lactante, preeclampsia, choque séptico.
- Puntaje 10/5/0 por decisión (óptima/aceptable/incorrecta o peligrosa), % sobre el mejor camino posible, cronómetro opcional **sin penalización**, historial y mejor puntaje, reintento, análisis de errores y temas a reforzar.
- Desbloqueo progresivo: cada caso de nivel 2 y 3 pide ≥60 % en el anterior.
- Guardado en `preferencias.guardia` del progreso (se sincroniza con la cuenta).
- **Contenido redactado por IA (Claude), sin revisión médica externa.** Manejo estándar, sin dosis, con fuentes citadas por nombre y **sin verificar contra el documento ni página**. Cada pantalla lleva el aviso de simulación educativa. Conviene que un médico lo revise antes de promocionarlo como contenido clínico.
- Pruebas: `node tests/guardia_test.js` (grafo sin ciclos, todo alcanzable, una decisión óptima por nodo, lo óptimo termina en buen desenlace, motor de puntaje y desbloqueo).
- Para añadir un caso: agregar un objeto a `guardia_casos.js` con el mismo formato y correr la prueba.

## Preguntar a la IA (`iaguia.js` + modo contexto de `api.php`)
Botón en la retroalimentación y en el visor de flujograma (solo con la pregunta ya corregida).
- Requiere sesión (misma cookie que `cuenta.php`) y tiene tope diario por usuario (`AI_LIMITE_CONTEXTO_DIA`, 40 por defecto) además del límite por IP.
- El servidor trata el contexto (enunciado, alternativas, respuesta del alumno, clave, comentario docente) como **datos**: lo recorta, limpia y encierra en un bloque `<<<DATOS … DATOS>>>`, neutralizando intentos de cerrarlo; el prompt le prohíbe inventar páginas, citas o dosis y le exige separar «explicación del banco» de «conocimiento general».
- La respuesta incluye `fuentes` (solo el comentario docente de esa pregunta) y `verificado: false`. **No hay guías MINSA ni internacionales cargadas**, y el panel lo dice; por eso el botón dice «Preguntar a la IA» y no «de la Guía».
- Sin llave de IA el panel muestra «no disponible» y el resto de la plataforma sigue igual. Las conversaciones no se guardan en el servidor.
- Variables: `AI_API_KEY`, `AI_PROVIDER`, `AI_MODEL`, `AI_BASE_URL`, `AI_LIMITE_CONTEXTO_DIA` (ver `config.example.php`).

## Lo que NO está hecho (necesita insumos que hoy no existen)
- **RAG con citas verificables (título, institución, año, página):** requiere los PDF oficiales (normas técnicas MINSA y guías internacionales) con su versión.
- **Modo espejo MINSA vs. internacional:** requiere las dos fuentes por tema; sin ellas el selector sería decorativo, así que no se añadió.
- **Predictor de nota ENAM/Residentado:** requiere datos reales suficientes y una escala validada.
- **Tarjetas generadas por IA y FSRS.**

## Introducción de «Sobrevive a la Guardia» (`guardia_intro.js`)
Pantalla cinematográfica (4 escenas en una sola línea de tiempo) que aparece al **entrar al módulo desde fuera** (menú lateral) y lleva a la lista real de casos (`#/guardia`).
- **No aparece** al volver a la lista desde un caso, al abrir un enlace directo a un caso, ni si el alumno la omitió antes.
- **Omitir introducción** (o Esc) guarda la preferencia `guardiaIntro = "omitir"` en `M.progreso.preferencia` (se sincroniza con la cuenta) con respaldo en `localStorage`. **Iniciar guardia** no la desactiva (y reactiva si estaba omitida). «Ver la introducción» en la lista la repite en cualquier momento.
- Sin audio. `prefers-reduced-motion`: se muestra todo de inmediato y sin animaciones. Si el alumno navega a otra sección con la intro abierta, se desmonta sola (sin timers ni listeners colgados). Foco atrapado en la intro; Espacio/Intro adelantan a la pregunta final.
- **El fondo es una escena dibujada en SVG/CSS (pasillo de emergencias, camilla, monitor), no una fotografía.** La foto `app/assets/guardia-hospital.jpg` (pasillo de emergencias aportado por el dueño del proyecto) se usa como fondo; si falta o no carga, queda la escena vectorial como respaldo.
- Pruebas: recorrido con Playwright (entrada desde el menú, 4 escenas, iniciar, omitir, persistencia tras recargar, repetición, enlace directo, navegación con la intro abierta, movimiento reducido, móvil).
