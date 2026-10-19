# Estado del proyecto Residentado Médico (para retomar en un chat nuevo)

Rama de trabajo: `claude/ecstatic-ramanujan-6z8vx6` (NO está en main; nada está publicado aún).

## Objetivo
Banco RM del PDF "Banco comentado – Residentado Médico Perú 2014-2019 (Estudios M&C, 2020)": hasta 500 preguntas, cada una con comentario docente propio (90-170 palabras), bibliografía verificada (hasta 2026, MINSA/EsSalud solo con número y año verificados), un flujograma SVG (motor en herramientas/flujo, estilo MedQuizPlus, sin Venn), imágenes médicas reales con crédito.

## Reglas del usuario (vigentes)
- Variar diseños; incluir criterios dx oficiales, escalas/puntajes con conducta por rango, tríadas/pentadas/banderas rojas (solo si el tema los tiene; nunca inventar).
- Sin dibujos no interpretables: usar imágenes reales; no dejar espacios en blanco en tarjetas/paneles.
- Si la imagen ya trae flechas/marcas/calipers NO añadir propias, solo describirlas; si no trae, añadirlas en español (sin rótulos en inglés).
- Sin "ejemplo pediátrico". Texto resumido pero completo.
- NUEVO: TODA clasificación va en un cuadro (`clasif=dict(...)` en `c26.S`, motor `engine11.py`; tipo `cuadro` para diseño de cuadro puro), con el caso del examen resaltado.
- NUEVO: pie de imagen "Imagen referencial de …" (nunca "no de la paciente").

## Hecho
- Lotes 1-3 (300 preguntas + 300 flujogramas) en bancos/*.json, flujogramas/ y algoritmos.js (registrados).
- 4 ejemplos con cuadro de clasificación (RM-CIR-074 Goligher, RM-CIR-118 Hinchey/Kaiser, TRA-057 Graf, RM-CIR-085 Todani) enviados al usuario: ESPERAN SU APROBACIÓN.
- Lote 4: preguntas en el banco; módulos de flujogramas content_rm_p13…p18 (p14, p15, p17, p18 terminados y verificados; p13 y p16 pendientes de informe) viven en el scratchpad de la sesión anterior (`.../scratchpad/h/herramientas/flujo/`), pueden haberse perdido: si no están, reconstruir esos IDs.
- Lote 5: 4 archivos residentado/lotes/lote05a-d.py con fuentes verificadas; AÚN NO integrados al banco.

## Pendiente (en orden)
1. Preguntar al usuario si aprobó los 4 ejemplos de cuadro de clasificación.
2. Reconvertir las clasificaciones de los ~300-400 flujogramas ya hechos a `clasif` y normalizar pies "Imagen referencial…"; auditar lote 1 (criterios/escalas/banderas rojas).
3. Ensamblar lote 4 (p13-p18), `check27.cjs`, registrar ("Residentado Médico · lote 4").
4. Integrar lote 5: `python3 residentado/integrar.py lote05a --aplicar` (uno por uno, sin pipes a head), luego flujogramas (~100 IDs) y registro.
5. Subir `?v=` en index.html/app/index.html, commit y push.
6. Decisión abierta del usuario: publicar lotes ya (merge a main + subida manual a Hostinger: bancos/, flujogramas/, algoritmos.js, catalogo.js, index.html, app/index.html) o esperar a los 5 lotes. No abrir PR salvo que lo pida.

## Dudas clínicas anotadas (claves no cambiadas)
Loxoscelismo lote05a (24 h vs 6 h), neumonía ambulatoria (amoxicilina no ofrecida), ceftriaxona 250 mg vs 500 mg, malaria NTS 233-2025 vs 054, RM-CIR-125/076/081/084, RM-INF-031 (ELISA 3-4 vs 2-4 sem), RM-NEU-012 (Anthonisen sin esputo).
