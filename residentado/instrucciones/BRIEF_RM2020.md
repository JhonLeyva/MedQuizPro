# Brief: preguntas del examen de Residentado Médico 2020 (lote 8)

Trabajas SOLO en tu archivo `residentado/lotes/lote08_<codigo>.py`. NO ejecutes git, NO ejecutes integrar.py, NO toques otros archivos. Español siempre.

## Entrada ya lista (no extraigas nada del PDF)
- `python3 /tmp/claude-0/-home-user-medquizpro/e40d7c10-2bd8-5b78-86c5-3e8e29658f65/scratchpad/rm20/ver2.py <PDF> <desde> <hasta>` imprime enunciado, opciones y `CLAVE` OFICIAL (la respuesta marcada en amarillo en el PDF). Esa clave es la verdad del examen: úsala. Si crees que es clínicamente discutible, deja la misma clave y explica el matiz en `nota=`.
- Preguntas con opciones raras (letras dentro de las opciones, p. ej. «A. Clase II») o clave doble: reconstruye las opciones tú mismo con `o=[...]` (5 opciones limpias) y `k=` correcta; explícalo en `nota=`.

## Formato del archivo (modelo: `residentado/lotes/lote08_cir_a.py`, léelo primero)
```
# -*- coding: utf-8 -*-
"""Residentado Médico 2020 · <especialidad>, preguntas A-B"""
import lote08_base as B
L = []
SAB = "..."   # constantes de libros
def Q(n, tema, cat, c, f, nota=None, **kw): B.hacer(L, "<PDF>", n, tema, cat, c, f, nota, **kw)
Q(1, "Tema corto", "Subárea", "comentario...", "fuentes...", nota=None)
```
`<PDF>` es la clave de B.CRUDO: CIRUGIA_GENERAL, GINECOLOGIA_Y_OBSTETRICIA, OFTALMOLOGIA, ANATOMIA_PATOLOGICA, ANESTESIOLOGIA, PSIQUIATRIA, UROLOGIA, PRUEBA_A, PRUEBA_B. Una entrada `Q` por pregunta de tu rango, en orden. `hacer` ya toma enunciado, opciones y clave del PDF; solo escribes el comentario `c` y las fuentes `f`.
- PRUEBA_A y PRUEBA_B son de especialidades mezcladas: pasa `a="<archivo del banco>"` en cada Q (`a=` ∈ cardiologia, ciencias_basicas, cirugia, endocrinologia, gastroenterologia, ginecologia, hematologia, infectologia, nefrologia (incluye urología), neumologia, neurologia, oftalmo_orl, pediatria, psiquiatria, reumatologia (incluye dermatología), salud_publica, traumatologia).
- Si el enunciado o una opción tiene error de OCR, corrígelo pasando `e=` y/o `o=`.

## Comentario `c` (150-230 palabras, español, SIN viñetas, redacción propia)
Fisiopatología o fundamento; por qué la clave es correcta; por qué fallan las otras opciones (menciónalas por su contenido); criterios diagnósticos oficiales con año, escalas con conducta por rango, tríadas/pentadas y banderas rojas cuando el tema los tenga (nunca inventes); manejo según guía vigente (hasta 2026); una «Perla:» final. No menciones IA, ni «el libro dice», ni «el examen».

## Fuentes `f` (exactitud ante todo)
- Cita libros con edición real (Harrison 21.ª 2022, Sabiston 21.ª 2021, Schwartz 11.ª 2019, Nelson 22.ª 2024, Williams Obstetricia 26.ª 2022, Robbins 10.ª 2021, Miller Anestesia 9.ª 2019, Kaplan y Sadock Psiquiatría 12.ª 2021, Campbell-Walsh-Wein Urología 12.ª 2020, Kanski Oftalmología 9.ª 2020, Guyton 14.ª 2021, Katzung 16.ª 2024, etc.) y SOLO artículos o guías internacionales que conozcas con certeza (autor, revista, año, volumen y páginas reales). Si dudas, verifica con `curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json"` o quita la cita. Nunca pongas puntos suspensivos ni páginas inventadas.
- Guías peruanas SOLO estas (verificadas): NTS 221-MINSA/DGIESP-2024 (TB); NTS 169-MINSA/2020/DGIESP (VIH, RM 1024-2020); NTS 159-MINSA/2019/DGIESP (transmisión materno infantil de VIH, sífilis y hepatitis B); NTS 154-MINSA/2019/DGIESP (tamizaje neonatal); NTS 214-MINSA/DGIESP-2024 (atención neonatal); GPC 03-2025 INS/MINSA (trastornos hipertensivos del embarazo); IETSI preeclampsia R.112-2021; Directiva 165-2025 (cáncer de cuello uterino); GPC apendicitis aguda EsSalud-IETSI 2022; GPC N.º 11 EsSalud-IETSI colelitiasis/colecistitis/coledocolitiasis 2018; NTS 054 malaria. No cites otra guía peruana.

## Validación (obligatoria)
`cd /home/user/medquizpro/residentado/lotes && python3 -c "import lote08_<codigo> as m; print(len(m.L)); [print(q['tema'], len(q['c'].split())) for q in m.L if not 148<=len(q['c'].split())<=240 or len(q['o'])!=5 or q['k'] not in 'ABCDE' or '...' in q['f']]"` — solo debe imprimir el conteo (debe ser 25).
Entrega (máx. 8 líneas): archivo, nº de entradas, preguntas con opciones reconstruidas o clave discutible, y citas de las que dudes.
