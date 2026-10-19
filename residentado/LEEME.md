# Banco de Residentado Médico (RM)

Fuente: *Banco comentado, preguntas de exámenes RM 2014-2019* (Estudios M&C, ed. 2020, 307 páginas).
Las preguntas son de los exámenes oficiales; **los comentarios son de redacción propia** (90-170 palabras, con fisiopatología,
por qué fallan las otras opciones y una perla clínica) y las fuentes se verificaron en PubMed y en gob.pe.

## Estado
| Lote | Preguntas | Flujogramas | Notas |
|---|---|---|---|
| 1 | 100 (anatomía, anestesiología, fisiología, cardiología, cirugía torácica y vascular, abdomen agudo inicial) | 100 SVG, 27 diseños distintos | `RM-CAR-001`…, `RM-CB-001`…, etc. |

Quedan unas 1 200 preguntas del PDF por revisar en lotes de 100 (orden del libro: cirugía general, dermatología, embriología,
endocrinología, infectología, gastroenterología, ginecoobstetricia, hematología, nefrología, neumología, neurología, oftalmología,
ORL, pediatría, psiquiatría, reumatología, salud pública, traumatología, urgencias y urología).

## Cómo está armado
- Las preguntas se agregan a `bancos/<especialidad>.json` con ID `RM-<PREFIJO>-NNN` y `examen_origen` «Residentado Médico AAAA · pregunta oficial»
  (la plataforma las separa del ENAM por ese texto). Campos extra: `tema`, `año`, `fuentes` y, si corresponde, `nota_revision`.
- Flujogramas: `flujogramas/rm-<id>-<tema>.svg`, registrados en `algoritmos.js`.
- `tools/extraer_residentado.py`: extrae el PDF (2 columnas) a un JSON intermedio.
- `residentado/lotes/loteNN*.py`: preguntas revisadas a mano (enunciado, 5 opciones, clave, comentario, fuentes).
- `residentado/integrar.py <lote> [--aplicar]`: arma las preguntas y las agrega a `bancos/`.
- `herramientas/flujo/`: motor de flujogramas (`build_rm.py`, `content_rm01*.py`, `c_rm.py`, `check27.cjs`, `hoja.py`).
  Uso: `python3 build_rm.py <salida> content_rm01a,content_rm01b,… && node check27.cjs <salida>/flujogramas <salida>/png`.
- Imágenes: PubMed Central (`img/pmc.py`) con licencia CC BY y crédito bajo cada imagen, Wikimedia Commons y dibujos propios.

## Claves y preguntas corregidas en el lote 1 (el libro tiene errores)
- **RM-CAR-024** (HTA 150/100): clave del libro A (estilo de vida) → **C** (terapia combinada), por las guías ACC/AHA 2025 y ESC 2024.
- **RM-CAR-036** (inicio de la troponina): la extracción automática daba E; la imagen del libro dice B (4 horas).
- **RM-CAR-018** (Duke): el libro admite dos respuestas (hemocultivo y ecocardiografía, ambos mayores); se reemplazaron dos opciones.
- **RM-CB-008** (articulación sinovial): tenía 3 respuestas válidas; se reemplazaron tres opciones.
- **RM-CAR-003** (shock de bajo gasto): «resistencia vascular alta» también era correcta; se reemplazaron dos opciones.
- Preguntas de redacción discutible que se mantienen con la clave del libro y una nota: RM-CIR-006 (ASA), RM-CIR-008, RM-CAR-016, RM-CAR-029, RM-CAR-033, RM-CB-016.
- Repetidas en el libro (misma clave): feocromocitoma (2), embolia cardiaca (2), shock de bajo gasto (2), várices (2), TPSV (2).
