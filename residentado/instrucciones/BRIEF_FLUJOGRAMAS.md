# Brief: flujogramas del banco de Residentado Médico (MedQuizPro)

Eres parte de un equipo que construye UN flujograma (SVG 1000 px de ancho) por cada pregunta del banco de Residentado Médico (RM) del Perú. Trabajas en paralelo con otros agentes; cada uno tiene sus propios IDs. No toques archivos que no sean los tuyos. No hagas git commit ni push (lo hace el coordinador).

## Dónde se trabaja
- Directorio de trabajo (motor + imágenes): `/tmp/claude-0/-home-user-MedQuizPro/5345f3f0-478d-503c-8ad7-d4450f2bb0a4/scratchpad/h/herramientas/flujo` (en adelante FLUJO). Ejecuta SIEMPRE los comandos desde ahí (`cd FLUJO`).
- Preguntas: `/home/user/MedQuizPro/residentado/salida/<lote>.json` (lista de dicts con id, enunciado, opciones, clave_correcta, correcta (índice), comentario, tema, año, fuentes). El módulo c_rm.py las carga solas (BANCO[id]).
- Construir: `cd FLUJO && python3 build_rm.py /tmp/out_<tu_nombre> content_rm_<tu_modulo>` → deja SVG en `/tmp/out_<tu_nombre>/flujogramas`.
- Verificar encaje: `node check27.cjs /tmp/out_<tu_nombre>/flujogramas /tmp/out_<tu_nombre>/png` → debe decir `archivos con problemas: 0 / N` (texto fuera de caja, rótulos que se salen de la imagen, textos pisados). Corrige hasta 0. Además MIRA con Read al menos 1 de cada 3 PNG (todos los que tengan imagen real) para comprobar que se entienden.
- Tu salida: un único archivo `FLUJO/content_rm_<tu_modulo>.py` con una llamada `S(...)` por pregunta (formato abajo), más las imágenes nuevas en `FLUJO/img/` (cada imagen con su `.json` sidecar `{"credito": "..."}`).
- Ejemplos a copiar (léelos primero): `content_rm02b.py`, `content_rm02c.py`, `content_rm_demo7.py`, `content_rm02ej.py`, `content_rm01a.py`..`content_rm01e.py` (formatos de `d=dict(...)` de cada diseño). Docstrings de los diseños: `engine3.py`, `engine4.py`, `engine5.py`, `engine6.py`, `engine7.py`, `engine9.py` (cada función tiene su docstring y se ven las claves de `d` que lee), `engine10.py` (carriles, capas, dermatomas, genealogia, farmaco, antes_despues, pruebas, linea_vida, triptico, dos_preguntas).

## Formato S(...) (de c_rm.py)
```
S(tipo, "RM-CIR-0xx", "Título-frase con la respuesta (≤ 110 caracteres)",
  "Barra · tema corto",
  ("Tema general (título)", ["línea 1", "línea 2"]),            # caja izquierda
  ("Caso clínico (título)", ["línea 1", "línea 2"]),           # caja derecha (resume el enunciado)
  ["perla 1", "perla 2", ...],                                   # PUNTOS CLAVE (3-4 líneas, ver reglas)
  "Fuente: ... (con año)",
  op=("¿Criterio?", [5 razones cortas, una por opción A-E, empezando con 'Sí:' en la correcta y 'No:' en las demás],
      {indice: "nombre corto ≤ 48 caracteres"}),                  # el dict solo para opciones largas
  d=dict(...),            # datos del diseño
  banda=B("Título", PX("archivo.jpg", 300), [("nota título","nota detalle"),...], pie="..."),   # opcional: franja con imagen real
)
```
Palabras PROHIBIDAS en cualquier texto del SVG: «respuesta» (usa reacción, evolución, opción). Largo de etiquetas: si el verificador dice `ancho`, acorta el texto.

## Reglas del usuario (obligatorias, vienen de toda la conversación)
1. **Nada de dibujos esquemáticos** (siluetas de cuerpo, órganos coloreados, diagramas que el estudiante no pueda interpretar). Si va una imagen, es una imagen MÉDICA REAL (radiografía, TC, ecografía, ECG, foto clínica, histología, endoscopía) de PubMed Central (licencia CC BY / CC0 / CC BY-SA) o Wikimedia Commons, **siempre con crédito** visible. Dibujo propio solo si es imprescindible y totalmente interpretable. Si no encuentras una imagen buena y pertinente, NO pongas imagen: usa un diseño solo de texto/tablas (eso es aceptable).
2. **Señalamiento en español y sin duplicar señales**: si la imagen YA trae flechas, asteriscos, calibres, contornos o rótulos, NO agregues flechas propias; describe esas señales en el texto («la flecha blanca marca…», «el contorno azul rodea…»). Si la imagen NO trae ninguna señal, agrega tú las marcas con el mecanismo `marcas` de PX (`("flecha", fx, fy, lx, ly, "texto")`, `("circulo", ...)`, `("caja", ...)`) con rótulos en español. Si la imagen trae rótulos en inglés, retíralos (parche local con PIL) o elige otra imagen. No pongas «ejemplo pediátrico» ni aclaraciones innecesarias; sí aclara si la imagen es de referencia y no del paciente.
3. **Sin espacios en blanco** grandes dentro de tarjetas/paneles. Si queda un hueco, rellénalo con contenido útil (más notas), reduce la imagen o cambia el diseño.
4. **Nada confuso**: no usar diagramas de intersección (Venn), ni gráficos que haya que adivinar. Prefiere tablas de decisión, listas de criterios, tarjetas, escaleras de tratamiento, lectura guiada de una imagen real.
5. **Texto resumido pero completo**: 3-4 perlas, cada una ≤ ~170 caracteres. Debe incluir, cuando el tema lo tenga (no inventes si no existe): (a) criterios diagnósticos oficiales vigentes (con fuente y año), (b) escalas/puntajes/clasificaciones con la conducta por rango, (c) alertas/banderas rojas, tríadas, pentadas y signos semiológicos clave que cambian el manejo.
6. **Bibliografía actualizada**: guías y artículos recientes (idealmente 2023-2026) de organismos y revistas reconocidos; guías MINSA y EsSalud/IETSI solo si existen y las verificas (WebSearch / URL gob.pe / essalud.gob.pe). Verificadas hasta ahora: EsSalud-IETSI GPC de apendicitis aguda (2022); EsSalud-IETSI GPC de colelitiasis, colecistitis aguda y coledocolitiasis (GPC N.º 11, 2018); MINSA NTS 214-2024 (atención neonatal); GPC 03-2025 INS/MINSA de trastornos hipertensivos del embarazo; Directiva 165-2025 (cáncer de cuello uterino). No inventes citas ni números de resolución: si no hay guía peruana vigente, cita la guía internacional más reciente y no menciones Perú. ATLS 11.ª ed. (2025), WSES, ESC/AHA/ACC, GOLD/GINA 2025, ADA 2026 (Standards of Care) son válidas.
7. **Variedad de diseños**: hay 49 diseños (ver `engine9.CATALOGO`; el 31 «venn» está PROHIBIDO). Usa el que mejor represente cada pregunta y no repitas el mismo más de 2 veces en tu lote. Diseños disponibles y su motor: decision, lectura, arbol (árbol de decisión), tarjetas, cuadricula, matriz, balanza, cascada, regla, radial, embudo, alarma, laboratorio, reloj, criterios, fases, checklist, grafica, monitor, transmision, piramide, termometro, mapa_signos, ecg_mapa, dosis, semaforo, gasometria, anatomia, arbol_imagen, calculo, calendario, ciclo, comparador, cronologia, escalera, grados_foto, puntaje, red, zonas, carriles, capas, dermatomas, genealogia, farmaco, antes_despues, pruebas, linea_vida, triptico, dos_preguntas. Cada uno exige un `d` con claves concretas: **lee el docstring/código de su función** y un ejemplo en content_*.py (`grep -n 'S("<tipo>"' content_*.py`) antes de usarlo. Los diseños con imagen obligatoria (criterios, calculo, anatomia, semaforo, cronologia, comparador, escalera, mapa_signos, arbol_imagen, ciclo, balanza, red…) solo se usan si hay imagen real o el diseño admite texto.
8. **Corrección clínica**: la clave del banco ya está verificada (no la cambies). Si ves un error clínico en el comentario o en la clave, NO lo corrijas: anótalo en tu informe final.
9. Imágenes: biblioteca ya descargada en `FLUJO/img/` (ver `ls img`, con créditos en `img/*.json` o `creditos_idx.json`; muchas ya sirven: p. ej. fast_morison, rx_neumotorax_grande, tension_neumo, neumoperitoneo_pmc, absceso_hep_ct, hinchey*_tc, cullen_real, greyturner, colangitis_tc, colecistitis_eco, apendicitis_pocus, ileo_rx, volvulo_rx, bridas_rx, ogilvie_tc (en img/rm/), hernia_fem_*, varices_foto (img/rm/), pancreatitis_tc, ascitis, etc.). Para imágenes nuevas usa PubMed Central: `cd /home/user/MedQuizPro/herramientas/flujo/img && python3 pmc.py buscar "consulta en inglés" 8` → `python3 pmc.py figs PMCxxxx` → `python3 pmc.py bajar PMCxxxx N <ruta destino en FLUJO/img/nombre.jpg>` (crea el .json con el crédito). Wikimedia Commons está muy limitada por velocidad (429): evítala salvo necesidad. Mira SIEMPRE la imagen (Read) antes de usarla para comprobar que muestra lo que dices y ubicar coordenadas (fracciones 0-1).
10. Los créditos largos se salen de la caja: pasa `credito="Autor · Revista año · CC BY 4.0"` corto a `PX(..., credito=...)`.
11. No cites en el SVG el nombre de ningún modelo de IA.

## Entrega
Al terminar responde con: lista de IDs construidos y su diseño, IDs que no pudiste terminar (y por qué), imágenes nuevas usadas (archivo + crédito), y errores clínicos que detectaste en las preguntas o comentarios. Máximo 25 líneas.

## Adenda (lote 3 en adelante)
- Ya se usaron mucho: decision, lectura, checklist, tarjetas, cuadricula, arbol, fases. Prefiere, cuando encajen, los menos usados: carriles, capas, dermatomas, genealogia, farmaco, antes_despues, pruebas, linea_vida, triptico, dos_preguntas, anatomia, arbol_imagen, calculo, calendario, ciclo, comparador, cronologia, escalera, red, zonas, mapa_signos, ecg_mapa, monitor, transmision, dosis, gasometria, semaforo, termometro, regla, balanza, grados_foto, puntaje, laboratorio, criterios (con imagen).
- Ejemplos ya terminados del lote 2 (para copiar formato): `content_rm_p1.py` … `content_rm_p6.py`, `content_rm02b.py`, `content_rm02c.py`.
- Temas del lote 3: oftalmo/ORL, urología, dermatología, embriología, genética, histología, endocrinología (diabetes, tiroides, suprarrenal, hipófisis, paratiroides), infectología, etc. Para histología/dermatología/oftalmología usa fotos o imágenes reales de PubMed Central (hay muchas en img/: acne, acantosis, conjuntivitis, queratitis, hipopion, papiledema, retinopatia, melanoma, psoriasis, etc.; mira `ls img`). Para tiroides/endocrino: gammagrafía, ecografía tiroidea, TC de suprarrenal (feo_tc), ECG de hiperpotasemia (hiperk_ecg), etc. si existen; si no, texto.
- Los módulos y las salidas de este lote van con nombres p7 … p12 (content_rm_p7.py …).
- IMPORTANTE: no cites una fuente que no hayas verificado. Si dudas, cita solo lo que ya figura en el campo `fuentes` de la pregunta (ya fue verificado) y libros de texto con edición real.

## Adenda 2 (lote 4)
- Módulos p13…p18 (content_rm_p13.py …), salidas /tmp/out_p13 …. Datos en /home/user/MedQuizPro/residentado/salida/lote04a.json … lote04d.json (ya en el banco).
- Las preguntas ya traen `fuentes` verificadas (norma TB = NTS 221-MINSA/DGIESP-2024; ITS = NTS 240-MINSA/DGIESP-2026; dengue = NTS 211-MINSA/DGIESP-2024): usa esas, no la NTS 200.
- Tema: infectología, ginecología, gastroenterología, neurología, oftalmología, salud pública, etc. Imágenes reales disponibles en img/: koplik, sarampion_exantema, varicela, zoster, herpes, mantoux, tb_*, ghon_rx, neumonia_*, malaria (falcip, vivax_troz), giardia, ameba, ascaris_huevo, oxiuro, trichuris, strongy, uncinaria, candida_*, conjuntivitis, queratitis, hipopion, papiledema, retinopatia, otitis*, hidrocefalia, ncc_tc, toxo_rm, wernicke_flair, hsa_tc, glioblastoma, placenta_previa, ectopico_tubario, endometrioma, cervix_*, gemelar_lambda, dpp_pieza, diu, chancro, gonococo, cripto, leish, lepto, triatoma/romana, aedes, escabiosis, liendres, tina_capitis, etc. (mira siempre la imagen antes de usarla; si no muestra lo que dices, no la uses).
- Los diseños menos usados hasta ahora (preferir): dermatomas, ecg_mapa, monitor, calculo, calendario, ciclo, comparador, cronologia, escalera, red, zonas, mapa_signos, anatomia, arbol_imagen, semaforo, grados_foto, triptico, pruebas, capas, antes_despues.

## Adenda 3 (reglas más recientes del usuario)
- TODA clasificación/estadificación/escala por grados va en un cuadro: `clasif=dict(titulo=, cols=[...], filas=[[...]], caso=<índice de fila del caso>, ancho_primera=...)` en `c26.S` (motor engine11.clasificacion), o tipo `cuadro` si el diseño es solo la tabla. El caso del examen se resalta en naranja.
- Pie de imagen: "Imagen referencial de <qué muestra>" (p. ej. "Imagen referencial de una hemorroide mixta prolapsada"). Nunca "no de la paciente/del paciente".
- Prohibido Venn/intersecciones y cualquier diseño confuso. Ningún diseño más de 2 veces por lote. Sin espacios en blanco en tarjetas/paneles.
- Imagen con flechas/marcas propias: NO añadir marcas, solo describirlas. Sin marcas: añadir en español.
- Incluir criterios dx oficiales, escalas con conducta por rango, tríadas/pentadas/banderas rojas solo si el tema los tiene (no inventar).
