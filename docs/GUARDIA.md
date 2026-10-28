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
| Caso | Fuente peruana incorporada | Alcance / reserva |
|---|---|---|
| c01 hipotiroidismo | Guía del Hospital de Emergencias Villa El Salvador (adultos), leída completa | Guía de un hospital, no nacional; no se confirmó la resolución. Difiere de ATA/AACE en el calendario de TSH (cada 3 meses vs 6–8 semanas): ambos se declaran |
| c03 EIP | NTS 240-MINSA/DGIESP-2026 (RM 035-2026-MINSA, deroga la RM 263-2009) | PDF escaneado leído con OCR: hay que contrastar con el original. Enfoque sindrómico; el caso añade pruebas moleculares (CDC) |
| c04 faringitis | Guía pediátrica del Hospital de Emergencias Villa El Salvador | Es pediátrica (≤ 14 años); el caso es un adulto: apoyo parcial |
| c02 ITU pediátrica | No se halló guía peruana pediátrica (solo adultos, gestantes y EsSalud no complicada) | Declarado en el caso |
| Urgencias g01–g10 | Pendiente de revisar contra normas peruanas | Mantienen las referencias internacionales |

## Limitaciones declaradas
- Las normas peruanas halladas son parciales (ver tabla); para los 10 casos de urgencias todavía no se han contrastado con textos MINSA/EsSalud/OMS. Varias guías internacionales se leyeron solo a nivel de resumen en PubMed.
- Los intervalos de laboratorio son educativos: no se encontró un estándar nacional peruano y cada laboratorio define los suyos; no se incluyen valores críticos.
- Casos redactados por el modelo, sin revisión de especialista externo.
- Las dosis solo se citan cuando una fuente peruana leída las trae (c01, c03), con la advertencia de verificarlas; en el resto se remite a la guía y al protocolo local.
- Las respuestas viajan en el cliente (es un recurso de estudio, no un examen vigilado).
- Imágenes reales de licencia abierta a 512 px; los casos de consulta no incluyen imágenes; no hay caso piloto de dermatología con imagen licenciada.
- El «especialista» y la consulta son lógica predefinida, no una persona ni un modelo de IA.
