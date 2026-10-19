# Funciones nuevas (flashcards, rendimiento, Guardia, IA con guías, modo espejo, seguridad)

Detalle de las flashcards: `FLASHCARDS.md`.

## Rendimiento y plan de estudio (`rendimiento.js`, en «Mi progreso»)
Estadística descriptiva sobre los resultados reales del alumno (último intento de cada pregunta + simulacros completados).
- Muestra por separado: aciertos actuales, último simulacro, **estimación a futuro** y su incertidumbre.
- La estimación (rango de % de aciertos, intervalo de Wilson al 95 %) solo aparece con ≥100 preguntas respondidas **y** ≥2 simulacros de ≥20 preguntas; si no, dice qué falta.
- **No hay nota ENAM proyectada**: la escala del examen no está validada contra datos.
- Prioridad de estudio = 50 % bajo acierto (con prior Beta(1,1)) + 20 % peso en el banco + 15 % incertidumbre + 15 % tiempo sin practicar; cada tema explica sus motivos. «Peso» = tamaño de la especialidad en este banco, no el blueprint oficial.
- Pruebas: `node tests/rendimiento_test.js`.

## Sobrevive a la Guardia (`guardia_casos.js`, `guardia.js`, ruta `#/guardia`)
Casos clínicos como **grafo de decisiones fijo** (no depende de IA). 8 casos: crisis asmática, apendicitis, diarrea en lactante, preeclampsia, choque séptico, infarto con elevación del ST, hemorragia posparto y neumotórax a tensión.
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

## Preguntar a la IA de la Guía: guías oficiales con citas (`guias_lib.php`, `tools/`, `guias/`)
Cuando hay guías cargadas, la IA recupera fragmentos y **cita la fuente con página**; si no hay, solo usa el comentario del banco y el botón dice «Preguntar a la IA».
- **Carga:** PDF en `guias/pdf/` + ficha en `guias/manifest.json` (título, institución, país, tipo nacional/internacional, año, versión, estado vigente/reemplazada/retirada, `temas` en español). Luego `python3 tools/ingestar_guias.py` genera `guias/indice.json` con la página de cada fragmento y `python3 tools/verificar_indice.py` comprueba que **cada fragmento aparece tal cual en la página que declara**. Pasos completos en `guias/README.md`.
- **Búsqueda:** BM25 en PHP puro (sin extensiones), en un índice local; hasta 3 fragmentos **nacionales** y 3 **internacionales** por consulta, siempre etiquetados (no se mezclan países como una sola norma). Es búsqueda por palabras: una consulta en español halla guías en inglés gracias a `temas` del manifiesto; no hay búsqueda semántica (haría falta un servicio de embeddings).
- **Citas:** el prompt exige `[G#]` tras cada dato de una guía; el servidor **elimina las citas a números inexistentes** y devuelve las fichas (institución, año, versión, página, extracto, enlace y aviso si la guía fue reemplazada o retirada). Lo que no lleve cita se muestra como no verificado. Si nada es relevante, la IA debe decir «No encontré esto en las guías cargadas».
- Hoy `guias/manifest.json` está **vacío**: no hay ninguna guía cargada.

## Modo espejo MINSA Perú vs. guía internacional (`espejo.js`, `guias/comparaciones.json`)
Botón «MINSA Perú vs. guía internacional» solo si existe una comparación validada para esa pregunta (por id o por tema). Panel con pestañas [MINSA Perú] [Guía internacional] [Comparar], matriz con tipos (diferencia real, equivalentes, población distinta, actualización, condicionada por recursos), cada celda con su cita y «Fuente no disponible» cuando falta un lado. Capa aparte: no toca el flujograma original.
- Formato y verificación: cada celda lleva `frag` (id de fragmento real) y `cita_literal`; `python3 tools/verificar_comparaciones.py` exige que la cita aparezca en ese fragmento, que cada columna use una guía del tipo correcto y que una «discrepancia» tenga las dos fuentes.
- Hoy `comparaciones.json` está **vacío**: el botón no aparece en ninguna pregunta hasta que se carguen guías y comparaciones.

## Flashcards con IA
En el panel «Convertir en flashcard», «Proponer más con IA» pide hasta 3 tarjetas (JSON validado en el servidor: sin vacías ni duplicadas, citas solo a fuentes recuperadas). La `fuente` de cada tarjeta incluye institución, año, versión y página cuando cita una guía. Siempre editables y marcadas «revisa los datos».

## Seguridad y costos
- Cuenta del alumno obligatoria para IA y flashcards; aislamiento entre usuarios probado.
- IA: tope diario de consultas por usuario (`AI_LIMITE_CONTEXTO_DIA`), **presupuesto diario en caracteres** por usuario (`AI_PRESUPUESTO_CARACTERES_DIA`, 150 000 por defecto; aproxima el gasto en tokens, no el dinero real), **caché de 24 h** de la primera consulta de una conversación (misma pregunta/consulta/guías) y límite de ritmo en escrituras de flashcards.
- Si el proveedor de IA falla o no hay llave, la práctica, las flashcards y la guardia siguen funcionando.
- **Cuenta del dueño:** el dueño crea su cuenta normal y, en Perfil → «Soy el dueño del sitio», introduce `MQP_ADMIN_TOKEN`; esa cuenta tiene todos los exámenes sin pagar. No depende del correo (no está verificado).
- Variables de entorno: `AI_API_KEY`, `AI_PROVIDER`, `AI_MODEL`, `AI_BASE_URL`, `AI_LIMITE_MINUTO`, `AI_LIMITE_DIA`, `AI_LIMITE_CONTEXTO_DIA`, `AI_PRESUPUESTO_CARACTERES_DIA`, `MQP_ADMIN_TOKEN` (16+ caracteres), `MQP_SITE_URL`, más las de pagos.

## Migraciones y datos
`migraciones/` tiene las versiones `.up.sql` / `.down.sql` de flashcards, ritmo y marca de dueño (la aplicación crea las tablas sola). Los `.down` que borran datos están marcados como destructivos: copia antes `cuenta_datos/mqp.sqlite`. Documentos, fragmentos y comparaciones viven en archivos JSON versionados (`guias/`), no en la base de datos.

## Términos y condiciones (`terminos.html`)
**Borrador sin revisión legal.** Hay campos amarillos (titular, RUC, domicilio, devoluciones, jurisdicción, libro de reclamaciones) que debes completar, y conviene que un abogado lo revise antes de publicarlo. Está enlazado en el pie, en el registro y en el menú de la app.

## Accesibilidad
Auditoría automática con axe-core (WCAG 2.2 AA, etiquetas wcag2a/2aa/21a/21aa/22aa) sobre 20 pantallas y paneles, en tema claro y oscuro: **0 violaciones** al cierre de esta ronda (`node tests/a11y_axe.js`, ver instrucciones en el archivo). Esto no sustituye una prueba con lector de pantalla ni una auditoría manual: no se probó con NVDA/VoiceOver.

## Cómo correr todas las pruebas
```
php tests/flashcards_test.php        # calendario de repasos
node tests/rendimiento_test.js       # estadística del panel
node tests/guardia_test.js           # grafo de los 8 casos y motor de puntaje
python3 tests/guias_test.py          # ingesta, verificación de citas, búsqueda, espejo (con guías FICTICIAS de prueba)
python3 tests/api_test.py            # autenticación, permisos, límites, caché, presupuesto, dueño
python3 tests/migraciones_test.py    # migraciones reversibles
node tests/a11y_axe.js               # accesibilidad (necesita un servidor PHP en marcha)
```

## Lo que sigue pendiente
- **Cargar guías reales** (PDF oficiales del MINSA e internacionales) y **comparaciones validadas**: sin ellas, las citas, el modo espejo y las tarjetas con fuente no tienen contenido. El código ya está probado con documentos ficticios de prueba.
- **Revisión médica** de los 8 casos de la guardia y de cualquier comparación que se cargue.
- **Predictor de nota ENAM/Residentado:** no existe ni debe existir hasta tener datos reales suficientes y una escala validada (el panel solo muestra estadística descriptiva).
- **FSRS**, búsqueda semántica con embeddings, historial de conversaciones guardado por usuario, control de gasto en dinero real (no en caracteres), pruebas con lector de pantalla y prueba en el hosting real.
- **Control de acceso del banco en el servidor:** los bancos son archivos estáticos; hoy los límites del plan gratuito se aplican en la app, no en el servidor.
- Completar los datos amarillos de `privacidad.html` y `terminos.html`.

## Introducción de «Sobrevive a la Guardia» (`guardia_intro.js`)
Pantalla cinematográfica (4 escenas en una sola línea de tiempo) que aparece al **entrar al módulo desde fuera** (menú lateral) y lleva a la lista real de casos (`#/guardia`).
- **No aparece** al volver a la lista desde un caso, al abrir un enlace directo a un caso, ni si el alumno la omitió antes.
- **Omitir introducción** (o Esc) guarda la preferencia `guardiaIntro = "omitir"` en `M.progreso.preferencia` (se sincroniza con la cuenta) con respaldo en `localStorage`. **Iniciar guardia** no la desactiva (y reactiva si estaba omitida). «Ver la introducción» en la lista la repite en cualquier momento.
- Sin audio. `prefers-reduced-motion`: se muestra todo de inmediato y sin animaciones. Si el alumno navega a otra sección con la intro abierta, se desmonta sola (sin timers ni listeners colgados). Foco atrapado en la intro; Espacio/Intro adelantan a la pregunta final.
- **El fondo es una escena dibujada en SVG/CSS (pasillo de emergencias, camilla, monitor), no una fotografía.** La foto `app/assets/guardia-hospital.jpg` (pasillo de emergencias aportado por el dueño del proyecto) se usa como fondo; si falta o no carga, queda la escena vectorial como respaldo.
- Pruebas: recorrido con Playwright (entrada desde el menú, 4 escenas, iniciar, omitir, persistencia tras recargar, repetición, enlace directo, navegación con la intro abierta, movimiento reducido, móvil).
