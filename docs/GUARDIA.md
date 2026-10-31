# Sobrevive a la Guardia v3 y Consulta Clínica Experta

Simulación educativa. No dirige la atención de pacientes reales. Los casos fueron redactados a partir de las fuentes citadas y **no fueron revisados por un especialista externo**. (Documentación de la versión anterior: `docs/GUARDIA_v2.md`.)

## Arquitectura
| Pieza | Archivo |
|---|---|
| Núcleo puro del simulador de urgencias (grafo, puntaje ponderado, reloj inyectable, sesión, interconsulta, laboratorio, desenlaces) | `guardia_nucleo.js` |
| Pantallas del simulador (modos, temporizador, laboratorio, interconsulta, informe) | `guardia.js` |
| 10 casos de urgencias (fuente) → paquete generado | `guardia/casos/*.json` → `guardia_casos.js` |
| Catálogo de laboratorio | `guardia/laboratorio.json` → `guardia_lab.js` |
| Núcleo puro de la consulta ambulatoria | `consulta_nucleo.js` |
| Pantallas de la consulta | `consulta.js` |
| 4 casos de consulta (fuente) → paquete generado | `consulta/casos/*.json` → `consulta_casos.js` |
| Autoría reproducible (letras, estilo, cinco alternativas) | `tools/guardia_autoria/*.py` |
| Empaquetado (`--check` verifica que los generados estén al día) | `tools/guardia_empaquetar.py` |

Los datos (~0,5 MB) se cargan solo al entrar al módulo. No hay IA dentro del juego: la evolución depende únicamente de las decisiones y de los resultados predefinidos del caso.

## Centro de simulación (rediseño visual)
`#/guardia` es ahora la pantalla central (`guardia_hub.js` + `guardia_hub.css`): hero, tres tarjetas de modalidad, casos recomendados, estadísticas y accesos rápidos. Flujo: menú → centro → modalidad (`#/guardia/emergencias`, `#/consulta`) → caso (`#/guardia/g01`, `#/consulta/c01`, rutas originales) con migas y enlaces de regreso.
- Todos los datos salen de los casos cargados y del progreso real (`M.progreso.preferencia("guardia"/"consulta")`); las recomendaciones usan sin cambios `M.guardiaNucleo.recomendar`. No se muestran tiempo medio ni interconsultas agregadas porque no se registran por separado.
- UCI y Paciente Crítico es una tarjeta «Próximamente» sin enlaces ni cifras: la modalidad no existe.
- Accesos: biblioteca de laboratorio (catálogo con selector de perfil), guías y fuentes (referencias reales de los casos, peruanas primero), tutor Feynman (ruta existente) y una tarjeta informativa sobre las imágenes reales de los casos.
- Portadas: `guardia/portadas/*.webp`, ilustraciones generadas con IA entregadas por la propietaria (ver `guardia/portadas/LEEME.txt`); la pantalla lo declara. No se usaron las dos imágenes diagnósticas ilustrativas del paquete.
- Introducción: aparece siempre al entrar a `#/guardia` (menú lateral, otra sección); «Omitir» (botón o Esc) solo la cierra esta vez y no guarda preferencia. No se repite al volver con las migas desde un listado del módulo ni al abrir `#/guardia/emergencias` directamente; «Ver la introducción» la abre a demanda.
- Monitor vivo: `canvas.gh-monitor` sobre el monitor de la ilustración del hero (ECG, presión invasiva, pletismografía y cifras de ejemplo que varían poco). Es decorativo (`aria-hidden`), se detiene fuera de pantalla, con la pestaña oculta o al cambiar de ruta, y es estático con «reducir movimiento».
- Prueba: `node tests/guardia_hub_e2e.js` (94 comprobaciones: rutas, datos, progreso, regreso, diálogos, responsive, axe claro/oscuro).

## Ajustes posteriores
- **Consulta Clínica Experta sin corrección durante el caso:** al elegir una alternativa solo se registra («Respuesta registrada»); la corrección y el análisis de las cinco alternativas aparecen en el informe final. (El modo entrenamiento de la guardia de emergencias conserva su retroalimentación por decisión.)
- **Resultados de laboratorio por prueba:** cada prueba solicitada se muestra en su propio bloque (examen completo de orina, urocultivo, hemograma… ya no se mezclan). El examen completo de orina trae los 20 parámetros (físicos, químicos y de sedimento) en `c02` y `c03`.
- **Mayúscula inicial** en todo lo que muestran las tablas de resultados (valores, intervalos, títulos); se respetan «pH», siglas y nombres de especie.
- **Tarjetas de modalidad** solo con descripción (sin etiquetas de especialidades).
- **Biblioteca de valores de laboratorio** (`guardia_biblioteca.js`, generada desde `guardia/biblioteca_lab.json` con `tools/guardia_autoria/biblioteca_lab.py`; se carga solo al abrirla): 20 áreas y más de 300 análisis, con unidades de uso habitual en Perú y valores por edad, sexo y gestación; buscador (sin acentos, varias palabras) y áreas desplegables. Sin bibliografía; una sola nota: los valores son orientativos y cada laboratorio informa los suyos. En los análisis que también están en el catálogo de los casos, los valores coinciden (lo comprueba `tests/biblioteca_test.js`). Se corrigió además la urea del catálogo (antes tenía el intervalo del BUN) y las plaquetas (150 – 450).
- Pruebas: `node tests/biblioteca_test.js` (2 541), `node tests/guardia_hub_e2e.js` (118), `node tests/consulta_e2e.js` (257).

## Cambios de la v3 (urgencias)
1. **Cinco alternativas A–E** por decisión, una sola óptima, con distractores plausibles. Las letras correctas siguen una secuencia con semilla (sin repeticiones adyacentes, progresiones ni patrones ABAB) y se fijan en el JSON; las explicaciones son por alternativa y no citan letras. El texto se neutraliza (coma, largo, palabras absolutas/cautelosas) y `tests/guardia_test.js` mide: correcta más larga ≤ 32 %, rango medio ≈ 3, paridad de comas y palabras, duplicados y equivalentes, coherencia clave–puntaje–explicación.
2. **Temporizador** (`crearReloj`): entrenamiento (sin presión) y simulación cronometrada; límite por decisión según tipo (emergencia crítica, diagnóstica, interpretación de imagen/prueba); aviso visible, anuncio accesible, pausa que no cuenta el tiempo, restauración tras recargar, sin envíos duplicados. Si se agota se aplica la conducta de espera predefinida (`omision`) y se explica al final. La velocidad es indicador secundario.
3. **Laboratorio y valores de referencia**: resultados del paciente con valor, unidad, intervalo aplicable (edad, sexo, gestación) y marca; el catálogo distingue intervalo de referencia, umbral diagnóstico, objetivo terapéutico y valor crítico. Marcas ocultas mientras la interpretación se evalúa. Conversiones solo las derivables de la masa molar. **Los intervalos son educativos, no de un laboratorio peruano, y no se incluyen valores críticos.**
4. **Interconsulta** de tres niveles (orientación, ayuda dirigida −, completa −), solo en entrenamiento, registrada en el informe, siempre basada en la lógica validada del caso.
5. **Desenlaces diferenciados**: error recuperable, crítico (deterioro) y fatal solo tras una secuencia predefinida y defendible (nunca automático por dos fallos). Efectos sobrios, desactivables y respetuosos de «reducir movimiento».
6. **Casos más largos y ramificados** (6–12 decisiones) con imágenes reales de licencia verificada (`guardia/imagenes.json`).
7. **Informe**: resumen, diagnósticos, datos guía, imágenes, laboratorio, análisis de las cinco alternativas, tiempo, ayudas, puntaje ponderado, temas a reforzar, bibliografía.

## Consulta Clínica Experta (`#/consulta`)
Flujo: motivo → anamnesis → antecedentes → examen físico → hipótesis (hasta 3, con principal) → solicitud de pruebas (agrupadas, revisión previa al envío) → resultados e interpretación (cinco alternativas; permite pedir más pruebas) → diagnóstico → tratamiento → seguimiento/alarma/derivación → informe.

- Cada prueba del caso tiene clasificación (prioritaria, razonable, innecesaria, perjudicial), justificación y resultado predefinido; **no se revela nada que no se solicitó**.
- Prueba esencial omitida: la primera vez se pide reconsiderar (mensaje que no nombra la prueba); después se puede continuar y el informe lo registra.
- Puntaje ponderado por importancia clínica (anamnesis 10, examen 10, hipótesis 10, pruebas 25, interpretación 10, diagnóstico 15, tratamiento 12, seguimiento 8). Las pruebas «razonables» no penalizan; las innecesarias penalizan poco (5) y las perjudiciales más (15), con tope. No se puntúa velocidad.
- Informe de pruebas en cinco listas: pertinentes, innecesarias/bajo valor, importantes omitidas, perjudiciales y no solicitadas que habrían cambiado la conducta.
- Casos piloto: hipotiroidismo (medicina interna/endocrinología), ITU febril en lactante (pediatría), enfermedad inflamatoria pélvica (ginecología), faringitis estreptocócica (medicina familiar/infectología).
- Sesión recuperable por caso; progreso en `M.progreso.preferencia("consulta")`.

## Pruebas (todas reales, ejecutadas)
`node tests/guardia_test.js` (11 235 comprobaciones), `node tests/consulta_test.js` (722), `node tests/guardia_e2e.js` (1 478; ambos modos, 10 casos, temporizador con reloj simulado, sesión, laboratorio, interconsulta, desenlaces, móvil, axe WCAG 2.2 AA claro/oscuro), `node tests/consulta_e2e.js` (192; 4 casos en recorrido ideal y deficiente, pruebas no reveladas, bloqueo, sesión, móvil, axe), `python3 tools/guardia_evidencia.py verificar` (27 referencias; 26 con PMID verificadas en PubMed), `python3 tools/guardia_imagenes.py verificar`, integridad del banco y suites de regresión (Cloze, rendimiento, Feynman, estudio, flashcards, migraciones). `tests/guias_test.php` y 5 casos de `tests/api_test.py` ya fallaban en `main` antes de estos cambios (no relacionados).

## Fuentes peruanas (consultadas el 2026-10-28, tras habilitar gob.pe, EsSalud, OMS)
| Caso | Fuente peruana incorporada (consulta 2026-10-28) | Alcance / reserva |
|---|---|---|
| c01 hipotiroidismo | Guía del Hospital de Emergencias Villa El Salvador (adultos), leída completa | Guía de un hospital, no nacional; no se confirmó la resolución. Difiere de ATA/AACE en el calendario de TSH (cada 3 meses vs 6–8 semanas): ambos se declaran |
| c03 EIP | NTS 240-MINSA/DGIESP-2026 (RM 035-2026-MINSA, deroga la RM 263-2009) | PDF escaneado leído con OCR: hay que contrastar con el original. Enfoque sindrómico; el caso añade pruebas moleculares (CDC) |
| c04 faringitis | Guía pediátrica del Hospital de Emergencias Villa El Salvador | Es pediátrica (≤ 14 años); el caso es un adulto: apoyo parcial |
| c02 ITU pediátrica | No se halló guía peruana pediátrica (solo adultos, gestantes y EsSalud no complicada) | Declarado en el caso |
| g04 TB-VIH | NTS 221-MINSA/DGIESP-2024 (RM 894-2024) | Respalda tamizaje de VIH, cotrimoxazol y diagnóstico molecular; el momento del antirretroviral y el IRIS son de la norma de VIH (NTS 169-2020), no leída |
| g05 dengue | NTS 211-MINSA/DGIESP-2024 (RM 175-2024), secciones de alarma e hidratación | Coherente con el caso; volúmenes citados en el informe |
| g06 ictus | GPC N° 19 de EsSalud/IETSI (2018) | Anterior a AHA/ASA 2026; no se halló guía del MINSA |
| g09 cetoacidosis | Guía técnica RM 389-2023-MINSA (OCR) | Es para diabetes tipo 2; umbral de potasio 3,3 vs 3,5 del caso, ambos «reponer antes de insulina» |
| g10 sepsis y g01 colangitis | GPC N° 15 de EsSalud/IETSI (2018) | Anterior a la SSC 2021; en g01 solo cubre la fase de sepsis |
| g02, g03, g07, g08 | No se halló una norma peruana específica (ectópico: guía obstétrica RM 695-2006 hallada pero no leída) | Mantienen sus referencias internacionales |

## Limitaciones declaradas
- Las normas peruanas halladas son parciales (ver tabla): faltan g02, g03, g07 y g08, y no se leyó ninguna fuente de la OMS. Varias guías internacionales se leyeron solo a nivel de resumen en PubMed.
- Los intervalos de laboratorio son educativos: no se encontró un estándar nacional peruano y cada laboratorio define los suyos; no se incluyen valores críticos.
- Casos redactados por el modelo, sin revisión de especialista externo.
- Las dosis solo se citan cuando una fuente peruana leída las trae (c01, c03, g05, g06, g09), con la advertencia de verificarlas; en el resto se remite a la guía y al protocolo local.
- Las respuestas viajan en el cliente (es un recurso de estudio, no un examen vigilado).
- Imágenes reales de licencia abierta a 512 px; los casos de consulta no incluyen imágenes; no hay caso piloto de dermatología con imagen licenciada.
- El «especialista» y la consulta son lógica predefinida, no una persona ni un modelo de IA.

## UCI y paciente crítico (`#/guardia/uci`)
Tres casos con el mismo motor y estructura que los de emergencias, en `guardia/uci/u01–u03.json` (se escriben con `tools/guardia_autoria/u0N.py`; `python3 tools/guardia_empaquetar.py` genera `guardia_uci.js`, que se carga al abrir la modalidad o un caso de UCI). Llevan `"modalidad": "uci"`; los de emergencias no, y el hub y los listados los separan.

| Caso | Dificultad | Tema | Fuentes principales (verificadas en PubMed) |
|---|---|---|---|
| u01 · Insuficiencia respiratoria que no mejora con oxígeno | Intermedio | SDRA grave: vía aérea, ventilación protectora, prono, bloqueo neuromuscular, corticoide y ECMO | ATS 2024 (PMID 38032683), ESICM 2023 (PMID 37326646), PROSEVA (PMID 23688302) |
| u02 · Paciente reanimado que no despierta | Intermedio | Cuidados posparo: oxígeno y presión, ECG, reperfusión, temperatura, crisis y pronóstico multimodal | ERC/ESICM 2025 (PMID 41123621), AHA 2025 parte 11 (PMID 41122894) |
| u03 · Colapso brusco al cuarto día de una cirugía | Difícil | Shock obstructivo por embolia pulmonar de alto riesgo con trombólisis contraindicada | ESC 2019 (PMID 31504429); AHA/ACC 2026 solo como complementaria (resúmenes, PMID 42693678) |

Reglas: no hay guía peruana (MINSA/EsSalud) vigente identificada para estos temas y cada caso lo declara; las guías de 2025–2026 solo se leyeron en resumen, así que los casos no fijan metas numéricas ni dosis y piden confirmar el texto. Las pruebas estructurales de `tests/guardia_test.js` (cinco alternativas, una óptima, omisión, referencias, grafo sin ciclos, ruta de 6–12 decisiones, informe) se aplican a los 13 casos; `tests/guardia_e2e.js` juega los tres de UCI en ambos modos.

## Introducciones de los servicios (Emergencias, UCI, Consulta externa)
`intro_servicio.js` + `intro_servicio.css`: al entrar a `#/guardia/emergencias`, `#/guardia/uci` y `#/consulta` aparece la primera vez de cada visita (una variable en memoria: se repite al recargar, al salir de la página y volver, o al cerrar y reabrir la ventana, pero no al moverte dentro de la plataforma) una introducción a pantalla completa (foto en `guardia/portadas/intro-*.webp`, ilustraciones generadas con IA), con un botón «▶ Ver la introducción» en cada listado para repetirla. «Omitir» no guarda ninguna preferencia.
- **Monitores en movimiento** (lienzo en las coordenadas de la imagen): Emergencias muestra RCP (0–10 s), fibrilación y carga del desfibrilador (10–14 s), descarga (14,0 s) y ritmo recuperado a 120 /min (latido cada 0,5 s desde los 15,0 s); UCI muestra ECG, pletismografía, respiración y capnografía con FC 78, SpO₂ 96, FR 18 y PA 105/62 y la pantalla del ventilador. La consulta (sin monitores) anima la luz de la ventana, el negatoscopio y motas de polvo. Son decorativos, sin valor clínico.
- **Sonido** de 30 s por servicio (`guardia/audio/*.mp3`, sintetizado con `python3 tools/guardia_audio.py`, sin muestras): emergencias es un ambiente tenso (zumbido grave y disonante, latidos que se aceleran, rechinidos metálicos, alarma, carga y descarga de desfibrilador); UCI es el ambiente real de la unidad (monitor principal a 78 /min y camas vecinas, ventilador, bombas de infusión, alarma lejana, aire acondicionado, voces); consulta es un consultorio (aire acondicionado, voces lejanas, teclas, bolígrafo, papel, timbre de sala de espera, puerta); `hospital.mp3` acompaña la introducción principal de «Sobrevive a la Guardia» (pasillo, monitores lejanos, pasos, camilla, puertas, megafonía y un pulso grave). No se pudo escuchar el video de referencia indicado para emergencias (sin acceso a YouTube): el tema sigue el estilo tenso descrito, no es una copia. Cada tema es periódico (se repite sin cortes) y los instantes coinciden con los de la animación (lo comprueba `tests/intro_servicio_e2e.js`). Si el navegador bloquea el sonido aparece «Activar sonido»; hay botón para silenciar.
- «Reducir movimiento» dibuja un fotograma estático. Las pruebas automáticas se saltan las introducciones de servicio con la misma clave `mqp_guardia_intro_v1 = omitir` que ya usaban para la del centro. La pantalla del monitor de la UCI se dibuja sobre el cuadrilátero en perspectiva del cristal (correspondencia bilineal y texto con la base local), de modo que queda dentro del monitor a cualquier tamaño de ventana.
