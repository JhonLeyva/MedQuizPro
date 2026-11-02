# Brief: actualizar la bibliografía de las preguntas RM 2020 (regla del usuario, obligatoria)

REGLA DEL USUARIO (vigente, la incumplimos en la primera pasada): cada comentario docente debe basarse en **bibliografía actualizada al 2026**: artículos de revistas prestigiosas y reconocidas, guías internacionales vigentes y guías del MINSA y de EsSalud/IETSI vigentes, todo verificado. Tu tarea es REHACER la parte bibliográfica de las preguntas que se te asignan (las que hoy no citan ninguna fuente de 2023-2026).

Trabajas SOLO en tu archivo `residentado/lotes/lote08_<codigo>.py` (te lo indica tu prompt, con la lista de números de entrada `Q` a corregir; la entrada número i es `L[i-1]`, en orden). No ejecutes git ni integrar.py. Español.

## Qué cambiar y qué NO
- Cambia SOLO `c` (comentario) y `f` (fuentes), y `nota` si hace falta. NO cambies `n`, el tema, la clave, las opciones ni el enunciado. La clave oficial (marcada en amarillo en el PDF) se mantiene siempre; si la guía vigente contradice la clave, déjala igual y explica el matiz en `nota`.
- Mantén el comentario en 150-230 palabras, redacción propia, sin viñetas, con «Perla:» final; actualiza datos, definiciones, criterios, puntos de corte, clasificaciones y conducta a lo que dicen las guías VIGENTES a 2026 (si una recomendación cambió desde el examen, dilo: «según la guía de 2024…»). Incluye criterios diagnósticos oficiales con año, escalas con conducta por rango, tríadas/pentadas y banderas rojas cuando el tema los tenga.

## Cómo buscar y verificar (obligatorio, una pregunta a la vez)
1. Carga WebSearch con ToolSearch (`select:WebSearch`) y úsalo. Busca la guía o artículo más reciente (2023-2026) del tema: guías de sociedades (ACC/AHA, ESC, ADA, KDIGO, GOLD, GINA, IDSA, ACOG, FIGO, AAP, ASA, EAU, AUA, AAO, WHO Classification 5.ª ed., DSM-5-TR, etc.), revisiones/ensayos en NEJM, Lancet, JAMA, BMJ, Annals, Circulation, Gastroenterology, etc., y OMS.
2. Para artículos: verifica en PubMed (`curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term=..."` y `esummary`) que autor, revista, año, volumen y páginas (o número de artículo) existen. Cita así: «Autor A et al. Revista 2024;vol:páginas». Si no puedes verificarlo, NO lo cites.
3. Guías peruanas: busca en gob.pe / minsa.gob.pe / ietsi.essalud.gob.pe / dge.gob.pe si existe norma técnica o GPC vigente sobre el tema (NTS, RM, GPC, Directiva) y cítala SOLO con número y año confirmados en la página oficial (por WebSearch o WebFetch). Si no encuentras una vigente, no cites ninguna peruana. Ya verificadas (puedes usarlas): NTS 221-MINSA/DGIESP-2024 (TB); NTS 169-MINSA/2020/DGIESP (VIH); NTS 159-MINSA/2019/DGIESP; NTS 154-MINSA/2019/DGIESP; NTS 214-MINSA/DGIESP-2024; GPC 03-2025 INS/MINSA (hipertensivos del embarazo); IETSI preeclampsia R.112-2021; Directiva 165-2025 (cuello uterino); GPC apendicitis aguda EsSalud-IETSI 2022; GPC 11 EsSalud-IETSI colelitiasis 2018.
4. Cada pregunta debe terminar con al menos UNA fuente de 2023-2026 verificada (guía, artículo, o edición de libro ≥2023: p. ej. Harrison 22.ª ed. 2025 si existe, Nelson 22.ª 2024, Katzung 16.ª 2024, Goodman y Gilman 14.ª 2023, Williams Obstetricia 26.ª 2022 no vale, etc. — verifica la edición y el año). Idealmente 2 o 3 fuentes (una internacional reciente, un artículo o revisión, y la peruana si existe). Puedes conservar libros clásicos como complemento.
5. NUNCA inventes ni cites de memoria sin verificar; nunca pongas puntos suspensivos ni páginas aproximadas. Si un tema no tiene guía reciente, cita la revisión o el consenso más reciente que sí exista.

## Validación (obligatoria)
`cd /home/user/medquizpro/residentado/lotes && python3 -c "
import re,lote08_<codigo> as m
for i,q in enumerate(m.L,1):
    ys=[int(y) for y in re.findall(r'(?<!\d)(20[12]\d)(?!\d)',q['f'])]
    if not any(y>=2023 for y in ys) or not 148<=len(q['c'].split())<=240 or len(q['o'])!=5 or '...' in q['f']: print('REVISAR',i,q['tema'])
print(len(m.L))"` — solo debe imprimir el conteo (si hay entradas fuera de tu lista que ya cumplían, no las toques).
Entrega (máx. 10 líneas): archivo, nº de preguntas actualizadas, guías peruanas halladas y citadas (con número y año), preguntas donde la guía vigente cambia la conducta frente a la clave oficial, y cualquier cita que no pudiste verificar (y que por eso no pusiste).
