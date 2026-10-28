# Sobrevive a la Guardia v2 — casos piloto, evidencia, imágenes y recomendaciones

## Qué hay
- **10 casos activos** (`guardia/casos/g01..g10.json`) → empaquetados en `guardia_casos.js` por `python3 tools/guardia_empaquetar.py` (artefacto generado; `tests/guardia_test.js` falla si está desactualizado).
- Especialidades: g01 colangitis grave/sepsis biliar (cirugía/gastro/emergencias) · g02 intususcepción (pediatría, **eco real**) · g03 embarazo ectópico (gineco) · g04 TB + VIH avanzado (infectología, **Rx real**) · g05 dengue con signos de alarma · g06 ictus isquémico (neurología, **TC + angio-TC reales**) · g07 disección aórtica tipo A (cardio, **Rx + angio-TC reales**) · g08 trauma hemorrágico (cirugía/trauma) · g09 cetoacidosis diabética (endocrino) · g10 choque séptico por neumonía (medicina interna/UCI).
- Los 8 casos de prueba anteriores están **archivados** en `guardia/archivo/` (ver su README). No estaban en la base de datos (archivo estático): no hay migración, el banco de preguntas, sus respuestas, explicaciones y flujogramas no se tocaron y el progreso histórico de los alumnos (`preferencias.guardia.casos.<id>`) se conserva.
- No hay IA dentro del juego: el grafo, el puntaje y el informe salen de datos validados. Si la IA externa falla, nada de este módulo se ve afectado (no usa llaves ni red).

## Esquema de un caso (v2)
`id, titulo, especialidad, dificultad, duracion_min, resumen, contexto, areas_banco[], imagenes[], referencias[], discrepancias[], inicio, nodos{}, informe{}`
- `nodos[id]`: `estado, vitales, gravedad(0-2), decisiones[]` (+ `imagen{id,consigna}`) o `final{tipo,titulo,mensaje}`.
- decisión: `id, texto, calidad(optima|aceptable|incorrecta|peligrosa), siguiente, explicacion, tema, competencia, refs[]`. Una óptima por nodo; puntaje 10/5/0/0.
- `referencias[]`: `id, tipo, titulo, organismo, autores, anio, version, pmid, doi, url, fecha_consulta, vigencia, recomendacion` (+ `complementaria`).
- `informe`: `resumen_clinico (A), razonamiento[] (B), imagen_interpretacion (C), tratamiento[{item,detalle,dosis}] (E), temas_relacionados, casos_relacionados, mensaje_clave (F)`. D y el resto de F se calculan con lo que el alumno realmente eligió (`analizar()`).

## Evidencia y verificación
- `python3 tools/guardia_evidencia.py buscar|ver|verificar` (NCBI E-utilities). `verificar` contrasta **todos** los PMID de los casos con PubMed (título, año, DOI): 22 referencias, 21 con PMID verificadas, 0 problemas. Las consultas quedan en `guardia/evidencia_log.jsonl`.
- Referencias usadas: Tokyo Guidelines 2018 (×3), Surviving Sepsis 2021, ACOG PB 193, ACC/AHA 2022 aorta, ESC 2024 aorta, AHA/ASA 2019 y 2026 ictus, ESC trauma 2023, CRASH-2, PROPPR, consenso ADA/EASD 2024, síntesis OPS 2022 dengue, SAPIT, ACTG A5221, prednisona-IRIS, y 3 revisiones de intususcepción.
- Cada decisión enlaza a las referencias que la respaldan; el informe muestra título, organismo/autores, año/versión, PMID/DOI/URL, fecha de consulta, vigencia y la recomendación en palabras propias.

## Imágenes
- Solo imágenes reales, tomadas de artículos de acceso abierto de PubMed Central vía Open-i (NLM), con licencia **leída del XML del artículo** (`tools/guardia_imagenes.py`): se aceptan CC BY / BY-SA / CC0; NC/ND se rechazan.
- Registro en `guardia/imagenes.json` por imagen: título, fuente, enlace, licencia, modalidad, región, hallazgo evaluado, SHA-256, modificaciones (ninguna: se sirven tal cual, 512 px) y fecha de verificación. Archivos con nombre opaco (`im-xxxx.png`), alt neutro, sin datos de paciente.
- Durante el caso se ve la imagen con visor (zoom, desplazamiento, brillo/contraste, teclado, pellizco) **antes** de decidir y se puede volver a abrir; fuente y diagnóstico se revelan en el informe (sección C).
- `python3 tools/guardia_imagenes.py verificar` re-comprueba hash y licencia contra PMC.

## Recomendaciones personalizadas
`guardia.js: estadisticas()` + `recomendar()`, calculadas **en el navegador** con el progreso del propio alumno (nada se envía). Reutilizan `rendimiento.js` (acierto, intervalo de Wilson).
Puntaje = 0,55·debilidad (prior Beta(1,1)) + 0,10·incertidumbre del intervalo + 0,15 si el acierto de los últimos 14 días cae >10 pts frente al histórico + 0,10 si hay temas con ≥3 fallos; +0,05 si no se jugó, +0,10 si el mejor puntaje <60 %, −0,30 si ≥80 %. Cada caso usa las especialidades de `areas_banco`.
Umbrales: <30 respuestas en el banco → **no** se personaliza (modo «Por dónde empezar», dice cuántas faltan); <8 respuestas en una especialidad → no se juzga; sin ninguna especialidad juzgable → «provisional». Es una sugerencia: los 10 casos siguen abiertos y hay filtro por especialidad. Resultado en caché por (n.º de respuestas, última fecha, día). La confianza declarada (módulo Estudio, que vive en el servidor) **no** se usa todavía.

## Pruebas
`node tests/guardia_test.js` (≈1930 comprobaciones: grafos, esquema, referencias, imágenes, informe, motor, recomendaciones) · `node tests/guardia_e2e.js` (Playwright: juega los 10 casos por ruta óptima y por rutas con errores, imágenes y visor, informe A–F, recomendaciones con datos reales del banco, móvil 390 px y axe WCAG 2.2 AA en claro/oscuro) · `python3 tools/guardia_evidencia.py verificar` · `python3 tools/guardia_imagenes.py verificar` (ambos con red).

## Limitaciones declaradas
- Casos redactados por IA (Claude) a partir de las fuentes recuperadas; **sin revisión de un especialista externo**. Hace falta revisión médica antes de usarlos como contenido de referencia.
- Las respuestas viajan en el navegador (el alumno podría inspeccionarlas): es un simulador formativo, no un examen.
- Solo se leyó el resumen de PubMed de varias guías (AHA/ASA 2026, ESC 2024, ESC trauma 2023, OPS 2022); no se leyeron los textos completos de MINSA/EsSalud/OMS. Por eso g05 (dengue) no fija volúmenes de líquidos y varios casos remiten al protocolo local para dosis. Cifras de PA del ictus: AHA/ASA 2019 (la guía 2026 la reemplaza). Ofidismo (OMS) se descartó por no poder verificar sus recomendaciones.
- Imágenes de 512 px (Open-i); la del ictus conserva las flechas de los autores; la de aorta tiene texto del equipo parcialmente ilegible. Son de otros pacientes.
- No se construyó una herramienta de autoría asistida: los casos se generaron en esta sesión y se validan con las pruebas.
