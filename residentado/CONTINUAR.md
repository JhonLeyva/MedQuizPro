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
- 4 ejemplos con cuadro de clasificación (RM-CIR-074 Goligher, RM-CIR-118 Hinchey/Kaiser, TRA-057 Graf, RM-CIR-085 Todani) enviados al usuario: APROBADOS por el usuario.
- Lote 4: preguntas en el banco; módulos content_rm_p13…p18 (los 6 terminados, 0 problemas en check27) ya están en herramientas/flujo/; falta ensamblar, registrar y aplicar la regla de cuadro de clasificación.
- Lote 5: 4 archivos residentado/lotes/lote05a-d.py con fuentes verificadas; AÚN NO integrados al banco.

## Pendiente (en orden)
1. (Hecho) El usuario aprobó los 4 ejemplos de cuadro.
2. Reconvertir las clasificaciones de los ~300-400 flujogramas ya hechos a `clasif` y normalizar pies "Imagen referencial…"; auditar lote 1 (criterios/escalas/banderas rojas).
3. Ensamblar lote 4 (p13-p18), `check27.cjs`, registrar ("Residentado Médico · lote 4").
4. Integrar lote 5: `python3 residentado/integrar.py lote05a --aplicar` (uno por uno, sin pipes a head), luego flujogramas (~100 IDs) y registro.
5. Subir `?v=` en index.html/app/index.html, commit y push.
6. DECIDIDO: el usuario eligió ESPERAR a terminar los 5 lotes antes de publicar. Opciones de publicación: publicar lotes ya (merge a main + subida manual a Hostinger: bancos/, flujogramas/, algoritmos.js, catalogo.js, index.html, app/index.html) o esperar a los 5 lotes. No abrir PR salvo que lo pida.

## Dudas clínicas anotadas (claves no cambiadas)
Loxoscelismo lote05a (24 h vs 6 h), neumonía ambulatoria (amoxicilina no ofrecida), ceftriaxona 250 mg vs 500 mg, malaria NTS 233-2025 vs 054, RM-CIR-125/076/081/084, RM-INF-031 (ELISA 3-4 vs 2-4 sem), RM-NEU-012 (Anthonisen sin esputo).

## Dónde está TODO lo que hay que saber (leer antes de trabajar)
- residentado/instrucciones/BRIEF_PREGUNTAS.md: cómo redactar preguntas, comentarios (90-170 palabras), fuentes y verificación (peer-reviewed + MINSA/EsSalud solo con número/año verificado, años recientes hasta 2026; NTS 221-2024 TB; no citar lo que no se verifique).
- residentado/instrucciones/BRIEF_FLUJOGRAMAS.md (con Adendas 1-3): cómo construir flujogramas (motor herramientas/flujo, c_rm.S, diseños disponibles, imágenes reales con crédito, check27.cjs, reglas del usuario).
- residentado/instrucciones/BRIEF_FUENTES.md: cómo verificar bibliografía.
- Flujo de trabajo: lotes en residentado/lotes/loteNN?.py -> `python3 residentado/integrar.py <lote> --aplicar` (uno por uno, sin pipes) -> content_rm_pN.py (flujogramas) -> build_rm.py -> `node check27.cjs` (debe dar 0 problemas) -> registrar_rm.py (algoritmos.js) -> subir `?v=` en index.html y app/index.html -> commit/push.
- Modelo de trabajo con subagentes: un agente por ~17 IDs, con el brief; luego un agente verificador de fuentes por lote. Las claves del libro dudosas NO se cambian sin avisar: se anotan en `nota=`.
