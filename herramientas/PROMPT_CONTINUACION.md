# MedQuizPro — instrucciones para continuar el trabajo

Eres el asistente técnico de MedQuizPro/MedQuizPlus, un banco de preguntas del ENAM (examen médico peruano) publicado en Hostinger: https://lime-louse-621404.hostingersite.com. Responde siempre en español, de forma breve y sin jerga.

## Reglas del repositorio
- Repo `jhonleyva/medquizpro`, clonado en `/home/user/MedQuizPro`. Trabaja en la rama que te asigne la sesión; si es nueva, créala desde `origin/claude/sweet-franklin-dbg0mc` (ahí está todo el trabajo más reciente). No abras PR salvo que te lo pida.
- Cada entrega es un ZIP en la raíz del repo, con commit y `git push -u origin <tu rama>`. Si falla por red, reintenta a los 2, 4, 8 y 16 s. Después envíalo con SendUserFile (display `attach`).
- El pie de cada commit lo indica el system-reminder de la sesión nueva. No pongas identificadores de modelo en commits ni en archivos.
- Trabaja en tu scratchpad. Copia primero `herramientas/` ahí: `cp -r /home/user/MedQuizPro/herramientas/. $S/`. Los scripts usan rutas relativas a esa carpeta y a `$S/flujo/`.

- **Código de la web:** la copia más reciente está en `herramientas/plataforma_materias/` (versión `?v=20260930-materias`); la anterior, en la rama `origin/claude/clever-franklin-1fao9i` (versión `20260928-plataforma`). Antes de entregar cambios de código, pide al usuario que abra `public_html/index.html` en Hostinger y busque el texto `?v=`: si coincide con una de esas versiones, trabaja sobre esa copia; si no, pídele que descargue los archivos que vas a tocar y trabaja sobre ellos.
- **Al terminar cada tarea, actualiza este archivo** (estado, herramientas nuevas, próxima tarea) y súbelo con commit y push, para que el siguiente chat sepa todo lo hecho.

## Estado actual (30-sep-2026)
- **Rama con el trabajo más reciente:** `claude/vibrant-albattani-g7t3b3` (parte de `claude/sweet-franklin-dbg0mc` + bloque ENAM 2026). Total 2380 preguntas y 2106 flujogramas: **faltan los 274 flujogramas del bloque ENAM 2026**.
- **Bancos:** 2380 preguntas (bloques 1 a 8 = 1713 + 393 de Ciencias Básicas + 274 del bloque ENAM 2026). `site/bancos/` ya tiene las 2380.
  - `herramientas/site/bancos/` tiene los 17 JSON finales (ciencias_basicas.json con 485).
- **Flujogramas:** 2106, uno por pregunta. No falta ninguno.
  - `herramientas/site/algoritmos.js` es el registro completo actual (2106 entradas); úsalo como base del próximo bloque.
  - `herramientas/site/verificar-flujogramas.html` ya espera 2106.
  - `herramientas/flujo/existing_names_todos.txt`: todos los nombres de SVG ya usados. Ningún nombre nuevo puede repetirse.
  - Hecho: `MedQuizPro_flujogramas_sin_palabra_respuesta.zip` corrige 143 SVG (80 del bloque 6, regenerados con `herramientas/flujo/rebuild6.py`; 63 de los bloques 2–5, texto reemplazado). Nombres sin cambio. Bloques 2–8 revisados: ya no dicen «respuesta». Los 97 SVG antiguos del bloque 1 solo están en el servidor y no se revisaron.
- **Banco de Ciencias Básicas (nuevo, 29-sep-2026):** del PDF `Banco_Ciencias_Básicas.pdf` (Villamedic, ed. 2019, 458 preguntas con tabla de claves y sin comentarios) entraron 393 preguntas, todas en `ciencias_basicas.json` (CB-093 a CB-485; CB queda en 485 y el total del sitio en 2106).
  - Paquete: `MedQuizPro_ciencias_basicas_393_preguntas.zip` (solo `bancos/ciencias_basicas.json` + `LEEME.txt`).
  - `examen_origen`: "ENAM · Ciencias Básicas 2019" (debe empezar por "ENAM": el filtro de la web publicada solo muestra esas), `año` 2019. Cada una lleva comentario docente propio.
  - Herramientas en `herramientas/cb/`: `parse.py` (PDF → `cbq.json`), `r00…r09.py` (revisión: `D[n]=(tema, clave, comentario)`, `O` opciones, `N` enunciado, `X` excluidas con motivo), `merge.py` (valida), `build.py` (lista FIX de ortografía), `leeme.py`, `testcb.cjs`, `nuevoscb.json`.
  - 65 omitidas (56 repetidas, 9 mal planteadas) y 12 claves del PDF corregidas.
  - Flujogramas hechos: `MedQuizPro_flujogramas_ciencias_basicas.zip` (393 SVG, `algoritmos.js` con 2106 entradas, verificadores `verificar-flujogramas-bloquecb.html` y general a 2106).
    Herramientas en `herramientas/flujo/`: `ccb.py` (lista `FCB`; curva por defecto en `fases`), `refcb.py` (fuentes), `contentcba…j.py`, `buildcbf.py`, `finishcb.py`, `chkcb.sh`, `e2ecb.cjs`, `existing_namescb.txt`, `ordercb.json`.
    Para un bloque siguiente: añade a `existing_namescb.txt` los nombres de `ordercb.json` y usa como base `outcb/pack/algoritmos.js` (2106).
- **Materias de Ciencias Básicas (30-sep-2026):** las 485 preguntas de `ciencias_basicas.json` llevan el campo `"categoria"` con una de 9 materias (Anatomía 70 · Histología y Biología Celular 32 · Embriología 35 · Fisiología 62 · Bioquímica y Genética 55 · Microbiología e Inmunología 42 · Farmacología básica y autonómica 166 · Patología general 20 · Epidemiología y Bioestadística 3).
  - Código de la plataforma modificado en `herramientas/plataforma_materias/` (catalogo.js, main.js, styles.css, index.html, app/app.js, app/index.html, `cambios.diff` y LEEME). Paquete: `MedQuizPro_ciencias_basicas_materias.zip`.
    - catalogo.js: `categorias: [9 nombres]` en Ciencias Básicas; `normalizar` copia `categoria`; `filtrar` acepta `categorias: []` o `categoria` (solo recorta especialidades con categorías); `MQP.contarCategorias`.
    - main.js: selector «Materia» en la tarjeta (`alEntrenar(esp, materia)`), `abrir(cfg)` pasa `cfg.categoria/categorias`, `M.ui.contarMaterias` y `M.ui.tituloMateria`, la etiqueta de tema muestra «Materia · tema».
    - app/app.js: paso «Materias» en el armador cuando se elige Ciencias Básicas (`conf.categorias`), tarjetas y `ACCIONES.especialidad` pasan la materia.
    - Versión de caché: `?v=20260930-materias`.
  - **Ojo:** ese código se hizo sobre la copia de la plataforma del 28-sep (rama `origin/claude/clever-franklin-1fao9i`). Si el usuario trae sus archivos reales del servidor (Hostinger, `public_html`), aplica sobre ellos los cambios de `cambios.diff` en lugar de reemplazar a ciegas. Si su `index.html` contiene `20260928-plataforma`, es la misma versión y el ZIP sirve tal cual.
  - Herramientas de la clasificación: `herramientas/cb/materias/` (`rules.py` reglas por palabras, `ov1.py` correcciones manuales por número de pregunta, `apply.py`, `e2e.cjs` prueba en navegador). Preguntas nuevas de Ciencias Básicas deben traer `"categoria"` con uno de los 9 nombres exactos.
  - Segunda revisión independiente (otro chat, 30-sep-2026): coincide en 460 de 485. Las 25 diferencias (casos de frontera: tóxicos, anafilaxia, vitaminas, reparación tisular) están en `herramientas/cb/materias/comparacion_segunda_revision.txt` (id | segunda revisión | la publicada). No se cambió nada: manda la clasificación publicada.
- **PDF original** (`Banco_ENAM_Respuestas_Resaltadas.pdf`, 2497 preguntas): ya no está en disco. Su versión procesada es `herramientas/parsed.json`.
- **Bloque ENAM 2026 (30-sep-2026):** de los 2 PDF `ENAM COMENTADO 2026 - 1.pdf` y `- 2.pdf` (están en la rama `main`; 180 preguntas cada uno, 4 alternativas A-D, clave y comentario Villamedic) entraron 274 (PDF 1: 143; PDF 2: 131). Paquete: `MedQuizPro_bloque_ENAM2026_274_preguntas.zip` (17 bancos + LEEME con la lista de IDs y de omitidas).
  - Omitidas 86: 83 por repetir concepto y respuesta ya publicados (lista en `e26/dupx.py` y en `t2/*.txt` con código `X`), 2 por página faltante en el PDF 2 (n.º 101-102) y 1 por clave dudosa (PDF 1 n.º 112).
  - `examen_origen`: «ENAM Extraordinario 2026 · pregunta oficial» (PDF 1) y «ENAM Extraordinario II 2026 · pregunta oficial» (PDF 2), `año` 2026. Se dejaron 4 opciones (la web las acepta). Las de Ciencias Básicas llevan `categoria`.
  - Comentario: el del PDF (sin «como vimos en clase» ni menciones a la academia); en el PDF 2 se añade al final la «perla». Solo la PDF 2 n.º 100 lleva comentario propio (faltaba en el PDF).
  - Herramientas en `herramientas/e26/`: PDF 1 tiene texto limpio por OCR (`render.py` + tesseract `spa --psm 4` → `parse.py` → `p1.json`; `fix.py`/`fix2` corrige OCR; `man1.py` parches y exclusiones; `a1.txt` = `n|código|tema`). PDF 2 es imagen con marca de agua: el OCR sale mal, se transcribió a mano mirando las páginas (`t2/*.txt`, formato `@n|código|tema`, líneas `E:` `A:`-`D:` `K:` `M:` `P:`). `cand.py` junta ambos → `cand.json`; `build26.py` construye `zip26/bancos` desde `site/bancos` (¡no volver a correrlo sobre bancos que ya tienen las 274: se duplican!); `leeme26.py`; `test26.cjs` (Playwright sobre `plataforma_materias` con los bancos nuevos: 2380, 0 errores).
  - Tesseract no viene instalado: `apt-get install -y tesseract-ocr tesseract-ocr-spa`; también `pip install pymupdf pillow numpy scikit-learn`. Usa `OMP_THREAD_LIMIT=1` y `xargs -P 4` o el OCR es lentísimo.
  - Para los flujogramas del bloque: la base es `nuevos26.json` (274, con `id`, `tema`, `especialidad`); los nombres nuevos no deben repetir `flujo/existing_names_todos.txt`.
- **PDF revisado completo.** Las 391 pendientes se revisaron en el bloque 8 (`sel8.py`: 134 en `SEL`, 257 en `EXC`). Ya no quedan preguntas del PDF por usar.

## GUÍA RÁPIDA: cómo trabajar (léela antes de empezar)

### A. Si el usuario pide preguntas nuevas (de un PDF o de otra fuente)
1. **Extraer.** Instala `pymupdf` (`pip install pymupdf`) y usa `herramientas/cb/parse.py` como modelo: separa cada pregunta en `{n, enunciado, opciones{A..E}, clave}`; si el PDF trae tabla de claves al final, léela.
2. **Revisar una por una** en archivos `rNN.py` (modelo: `herramientas/cb/r00.py`), por tandas de 50:
   - `D[n] = ("tema corto", "LETRA", "comentario docente")`
   - `O[n] = {"C": "texto corregido"}` para arreglar o completar opciones (siempre 5 opciones).
   - `N[n] = "enunciado corregido"` y `X[n] = "motivo"` para excluir.
   - Tú decides la clave: si la del PDF está mal u obsoleta, corrígela (y cuéntalo en el LEEME). Si dos opciones son correctas, cambia una opción para que quede una sola.
   - Excluye repetidas (dentro del PDF o ya publicadas en `site/bancos/`), mal planteadas o que dependen de una imagen.
3. **Comentario docente** (lo que el usuario pidió explícitamente): 90-160 palabras, en español claro, explicando por qué la opción correcta lo es, por qué fallan las demás y un dato clínico útil para el ENAM (MINSA, guías vigentes, textos de referencia). No copiar el comentario del PDF si está mal.
4. **Construir** con `merge.py` (valida que no falte ninguna) y `build.py` (lista FIX de ortografía, blancos → `______`). Formato de cada pregunta nueva:
   `{id, especialidad, examen_origen, enunciado, opciones:[5], correcta:índice, clave_correcta:"A".."E", explicacion, comentario (igual), tema, año}`.
   - **`examen_origen` DEBE empezar por "ENAM"** (p. ej. "ENAM 2024 · pregunta oficial" o "ENAM · Ciencias Básicas 2019"): la web publicada solo muestra esas.
   - IDs consecutivos por archivo (`PREFIJO-NNN`). Base: `site/bancos/`. **Cuidado:** no reconstruyas sobre un banco que ya contiene las nuevas (se duplican).
   - Van al archivo de la especialidad correspondiente (si el usuario dice una carpeta, todas ahí).
5. **Probar** con Playwright (`testcb.cjs` como modelo): cargan todas, total correcto, sin errores JS.
6. **Entregar** ZIP con `bancos/<archivo>.json` (solo los que cambian) + `LEEME.txt` (qué contiene, cuántas entraron/omitidas, claves corregidas, cómo instalar, lista de IDs).

### B. Si el usuario pide los flujogramas de un bloque
1. Copia `herramientas/flujo/*` al scratchpad. Crea `cXX.py` (copia de `ccb.py`), `buildXXf.py` (copia de `buildcbf.py` apuntando a tu `nuevosXX.json`, a `existing_names_todos.txt` y a `outXX/`) y `contentXXa…py` por tandas de 40.
2. Cada flujograma es propio de su pregunta. Campos comunes:
   `V("tipo", "ID", "nombre-archivo-ascii", "Título", "ESPECIALIDAD ENAM: TEMA", "ESPECIALIDAD", ("Tema general", [2 líneas]), ("Caso o 'Pregunta de …'", [1-2 líneas]), {datos del diseño}, [3 perlas], "Fuente")`.
   Árbol: `A("ID", "archivo", "Título", barra, esp, tema, caso, Q("¿Pregunta?", [L("rama", "TÍTULO", ["línea"], path=True), ...], path=True), ("Tabla", [("Col1", True), ("Col2", False)], [("Fila", ["c1", "c2"]), ...]), perlas, fuente)`.
3. **Los 8 diseños y sus datos** (ver ejemplos en `contentcba.py`):
   - `tarjetas`: `{"rotulo", "ans": índice, "cards": [4 × {"titulo", "datos": [3 × ("Etiqueta", "valor", bool)], "pie"}]}`
   - `embudo`: `{"rotulo", "inicio", "candidatos": [4], "pasos": [2 × ("criterio", [descartados])], "final": ("DIAGNÓSTICO", [2 líneas]), "nota"}` (cada paso debe descartar al menos uno).
   - `fases`: `{"rotulo", "ans", "fases": [3 × ("Nombre", "tiempo", "CLAVE", [líneas])], "chips_titulo", "chips": [4 × ("texto", bool)]}` (la curva es opcional; `ccb.py` pone una por defecto).
   - `matriz`: `{"rotulo", "eje_x", "eje_y", "cols": [2], "rows": [3], "caso": (fila, col), "cells": [3 filas × 2 celdas ("TÍTULO", [líneas])]}`
   - `puntaje`: `{"rotulo", "escala", "total": número, "max": número, "total_label", "interpreta", "items": [3 × ("ítem", "valor", bool)], "bandas": [3 × ("rango", "nombre", "acción", bool)]}` (el número del círculo debe ser corto: ≤ 4 cifras).
   - `radial`: `{"rotulo", "centro", "centro_sub", "ans", "items": [5 × ("TÍTULO", [1-2 líneas])], "ruta": [4 pasos]}`
   - `termometro`: `{"rotulo", "niveles": [4 × ("nombre", "sub", [líneas])], "caso_nivel", "ruta_titulo", "paso_label", "pasos": [3 × (n, "título", [línea], bool)]}` (se dibuja de abajo arriba).
   - `arbol`: `A(...)` con `Q()` y `L()` como arriba.
   Reparte los diseños más o menos por igual.
4. **Límites de texto** (si se pasan, `check.cjs` lo marca): nombre de nivel del termómetro ≤ ~92 px (≈ 14 caracteres en negrita), valor de ítem de puntaje ≤ ~90 px, rango de banda de puntaje ≤ ~100 px, títulos de tarjeta cortos. Acorta y vuelve a correr.
5. **Prohibido:** la palabra «respuesta» en cualquier texto del SVG (el build lo rechaza: usa «reacción», «efecto», «defensa»…), el sello «✓ RESPUESTA», nombres no ASCII o repetidos, etiqueta de especialidad equivocada.
6. **Comprobar cada tanda** con `./chkXX.sh contentXXa`: build + `overlap` (0 solapamientos) + `check.cjs` (0 desbordes) + `check2.cjs` (0 fuera de caja) + hoja de contacto (`../sh_*.png`, mírala).
7. **Empaquetar** con `finishXX.py` (modelo `finishcb.py`): `algoritmos.js` = base `site/algoritmos.js` + nuevas; galería `verificar-flujogramas-bloqueXX.html`; verificador general con el nuevo total; `LEEME.txt`. Prueba e2e (`e2ecb.cjs` como modelo) y entrega el ZIP (`flujogramas/`, `algoritmos.js`, verificadores, `LEEME.txt`).
8. Al terminar, copia las herramientas nuevas a `herramientas/flujo/`, actualiza `site/algoritmos.js`, `site/verificar-flujogramas.html`, `existing_names_todos.txt` y este archivo; commit y push.

## Contenido de `herramientas/`
**Datos del PDF y selección**
- `parsed.json`: lista de 2497 preguntas con campos `{n, enunciado, opciones{A..E}, hl:[letras resaltadas], verif:None|"Verificar: …", comentario}`. El enunciado termina en `(ENAM AAAA …)`, de donde sale el año.
- `pool7.json`: candidatas que había al empezar el bloque 7, `{n, dup, sim}`.
- `sel7.py`: selección del bloque 7. Contiene:
  - `SEL`: tuplas `(n, ARCHIVO, "tema", "LETRA")`.
  - `COM[n]`: comentario propio.
  - `OPT[n]={"A":…}`: corrección de opciones.
  - `ENU[n]`: enunciado corregido.
  - `EXC[n]`: motivo de exclusión.
  - Al final, `_DUPB` quita 50 preguntas que repetían conceptos ya publicados.
- `sel5.py`, `sel6.py`, `build6.py`, `nuevos6.json`: bloques anteriores, solo como referencia.

**Construcción de bancos**
- `common7.py`: carga `q` (el `parsed.json` por n) y define `clean()`, `strip_src()`, `strip_resp()`, `year_of()` y las listas FIX de palabras partidas. Importa `fix6.py`.
- `build7.py`: construye los bancos.
  - Lee `zip6/bancos/*.json` como base. **Para el bloque 8, cambia `_base` a `site/bancos/` o a `zip7/bancos/`.**
  - Añade `SEL` con IDs `PREFIJO-NNN` consecutivos por archivo.
  - Aplica `COM`, `OPT` y `ENU`, más `post7()` (lista `POST`, `JOIN` de `join7.json`, blancos → `______`, `(mayor)/(menor)` → `>`/`<`).
  - Escribe `zip7/bancos/` (los 17 archivos) y `nuevos7.json`.
- `scanjoin7.py`: detecta palabras partidas comparando con el vocabulario de los bancos y las añade a `join7.json`. Ciclo: build → scan → build.
- `leeme7.py`: genera `zip7/LEEME.txt` (formato de los LEEME anteriores, con la lista por especialidad).
- `test7.cjs`: prueba con Playwright sobre `site/`. Levanta el servidor con `cd site && nohup python3 -m http.server 8765 &`.

**Web y flujogramas**
- `site/`: copia local de la web (`index.html`, `main.js`, `styles.css`, `algoritmos.js`, verificadores).
  - `site/flujogramas/` está vacío. Para probar imágenes, extrae ahí los SVG de los ZIP `MedQuizPro_flujogramas_bloque2..6.zip`.
- `flujo/`: motor de flujogramas.
  - Motores: `engine.py`, `engine2.py`, `engine3.py` y `engine4.py`, cuya función `build4(spec)` genera el SVG.
  - `c4.py`, `c5.py`, `c6.py`: ayudantes `A()`, `V()`, `Q()`, `L()`, `T()`.
  - `content6a…n.py`: los 500 flujogramas del bloque 6, como ejemplo del formato.
  - `build6f.py`: genera `out6/flujogramas/*.svg` y `out6/order.json`.
  - Controles: `overlap6.py` (solapamientos), `check.cjs` y `check2.cjs` (texto desbordado), `e2e7.cjs` y `verif7.cjs` (prueba en la web).
  - `existing_names.txt`: los 982 nombres de SVG ya usados.
  - `LEEME_flujogramas_bloque6.txt`: modelo de LEEME.
- **Entorno:**
  - Playwright está en `/opt/node22/lib/node_modules/playwright`, con `executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'`.
  - Fuentes de medición: `/usr/share/fonts/truetype/liberation/LiberationSans-*.ttf`, usadas con PIL.

## Formatos
**Banco** (`bancos/<archivo>.json`): `{"especialidad":…, "preguntas":[…]}`.
- Pregunta nueva: `{id, especialidad, examen_origen:"ENAM AAAA · pregunta oficial", enunciado, opciones:[5 textos], correcta:índice, clave_correcta:"A".."E", explicacion, comentario (igual que explicacion), tema, año}`.
- La primera pregunta de cada archivo usa un formato antiguo sin `correcta`. No la toques.

**Archivos y prefijos** (código en `sel7`):

| Código | Archivo | Prefijo |
|---|---|---|
| CB | ciencias_basicas | CB |
| CA | cardiologia | CAR |
| CI | cirugia | CIR |
| EN | endocrinologia | END |
| GA | gastroenterologia | GAS |
| GI | ginecologia | GIN |
| HE | hematologia | HEM |
| IN | infectologia | INF |
| NE | nefrologia (incluye urología) | NEF |
| NR | neumologia | NEU |
| NL | neurologia | NRL |
| OF | oftalmo_orl | OFT |
| PE | pediatria | PED |
| PS | psiquiatria | PSI |
| RE | reumatologia (incluye dermatología) | REU |
| SP | salud_publica | SP |
| TR | traumatologia | TRA |

**`algoritmos.js`**: objeto `window.MQP_ALGORITMOS` con entradas `"ID": { titulo, imagen: "flujogramas/<archivo>.svg", alt: "Flujograma: <titulo>" }`. Las nuevas se añaden antes del `};` final. Sin entrada, el modal muestra un "esquema de ejemplo".

## Flujo A: nuevo bloque de preguntas (detalle histórico; la guía rápida manda)
1. **Candidatas.** Del pool, calcula las no usadas (fuera de `SEL`/`EXC` de todos los `sel*.py`). Crea vistas de 45–50 preguntas con estado OK/VER/SIN, `hl` y similitud contra el banco. Descarta las que tienen similitud ≥0,3 con el banco o con otra ya aceptada.
2. **Revisión, una por una.** Tú decides la clave; no te fíes del resaltado.
   - Incluye las "Verificar" y las sin resaltado si la clave es clara según el comentario, MINSA y guías vigentes.
   - Si el comentario del PDF defiende otra opción, está cortado o no corresponde, escribe `COM`.
   - Excluye y anota en `EXC` con su motivo:
     - clave ambigua u obsoleta (p. ej. TAR diferido en gestantes con VIH, mucolíticos en lactantes, Gleason 4, pelvimetría);
     - enunciado incompleto o que depende de una imagen;
     - pregunta casi idéntica;
     - **mismo concepto con la misma respuesta que otra ya publicada** o aceptada.
3. **Construcción y limpieza.** Ejecuta build → scanjoin → build.
   - Busca: `COI`/`SatOI`, `( -)`, números de página sueltos ("2"), `(PACIENTE ROBOT)`, referencias "(Opción X)"/"(Alternativa X)" que no coincidan con la clave.
   - Comprueba que el comentario mencione la opción correcta.
4. **Duplicados.** Compara las nuevas con todo el banco por `tema` y enunciado. Reemplaza las que repitan concepto y respuesta.
5. **Entrega.** LEEME → prueba en `site` (bancos cargan, total correcto, preguntas nuevas visibles, sin errores de JS) → ZIP `MedQuizPro_bloqueN_500_preguntas.zip` (`bancos/` + `LEEME.txt`) → commit, push y envío.

## Flujo B: flujogramas de un bloque (detalle histórico; la guía rápida manda)
- **Estilo MedQuizPlus.** Barra de título, "TEMA GENERAL" y "CASO CLÍNICO" resaltado (en `top_row`), algoritmo, tabla opcional, perlas y fuente. Contenido basado en MINSA y literatura actual (Harrison 22.ª, Williams 26.ª, Nelson, ATLS 11.ª, guías vigentes).
- **Variedad de diseños.** Repártelos más o menos por igual entre `arbol` (`A()`) y los 7 diseños de `V()`: embudo, fases, matriz, puntaje, radial, tarjetas y termómetro.
- **Prohibido:**
  - el sello naranja "✓ RESPUESTA" y cualquier etiqueta o rótulo con la palabra "RESPUESTA";
  - nombres de archivo que no sean ASCII en minúscula (`[a-z0-9-]+\.svg`) o que ya existan (`existing_names.txt`);
  - usar la etiqueta de especialidad equivocada en dermatología u ORL dentro de REU u OFT.
- **Cada flujograma es propio de su pregunta.** Parte del caso clínico concreto (edad, datos clave) y muestra la ruta hasta el diagnóstico o la conducta correcta, marcada visualmente ("ESTE CASO", ruta resaltada, rombo), pero sin escribir la palabra "respuesta".
- **Plantillas de los verificadores:** `site/verificar-flujogramas-bloque6.html` (cópialo y cambia la lista de IDs por la del bloque 7) y `site/verificar-flujogramas.html` (cambia "deben ser 1079" por 1579).
- **Proceso por tandas:**
  1. Escribe `content7a…py` sobre un `c7.py` (copia de `c6.py`, lista `F7`) y un `build7f.py` (copia de `build6f.py` que lea `../nuevos7.json` y escriba en `out7`).
  2. Pasa `overlap`, `check`/`check2` y revisa hojas de contacto.
  3. Genera `algoritmos.js` completo (1079 + 500 = 1579 entradas), `verificar-flujogramas-bloque7.html` y `verificar-flujogramas.html` actualizado a 1579.
  4. Prueba e2e en `site`.
  5. Empaqueta `MedQuizPro_flujogramas_bloque7.zip` (`flujogramas/`, `algoritmos.js`, verificadores, `LEEME.txt`), haz commit, push y envíalo.

## Instalación para el usuario (va en cada LEEME)
1. Haz una copia de respaldo de `public_html/bancos/`.
2. Sube el ZIP a `public_html` y usa "Extraer" hacia `public_html`, no a una carpeta nueva. Acepta reemplazar.
3. Recarga con Ctrl+F5.
4. Opcional: abre `verificar-flujogramas.html` y revisa que el total cuadre y no haya ninguno "sin pregunta".

## Flujogramas con ilustración y 20 diseños (pedido del usuario, 30-sep-2026)
- Cada flujograma debe ir acorde a su pregunta (datos del caso, alternativas) y llevar un **dibujo propio del tema que muestre el caso** (p. ej. quemaduras: cuerpo con la regla de los 9 y las zonas quemadas; hernias: pelvis con los orificios; Rx, ecografías, ECG, lesiones…).
- Se amplía a **20 diseños**: los 8 de antes + 12 nuevos: 9 cálculo, 10 mapa anatómico, 11 semáforo, 12 cronología (hechos en `flujo/engine5.py`), y por hacer: 13 comparador de imágenes, 14 escalera terapéutica, 15 ciclo/mecanismo, 16 lista de criterios, 17 balanza, 18 red de atención (niveles I-1 a III), 19 mapa corporal de signos, 20 árbol con imagen.
- `flujo/engine5.py`: `build5(spec)`, ilustraciones `ilu_cuerpo_nueve`, `ilu_pelvis_hernias`, `ilu_rx_volvulo`, `ilu_eco_tn` (SVG dibujado a mano dentro de `panel()`, con `pie()` después del dibujo). `flujo/demo26.py`: los 4 ejemplos (CIR-133, CIR-158, CIR-150, GIN-274), salida en `flujo/out26demo/`. Entregado `MedQuizPro_ejemplo_4_flujogramas_ENAM2026.zip` (4 SVG + PNG + algoritmos.js con 2110). (Superado por el ejemplo 2, abajo.)
- La cronología usa columna fija de nombres a la izquierda y barra en la misma fila (el usuario pidió que texto y barra coincidan).
- **Imágenes reales (ya funciona).** El usuario habilitó la red a Wikimedia. Usa `commons.wikimedia.org/w/api.php` para buscar (licencia y autor en `extmetadata`) y baja de `upload.wikimedia.org` con miniaturas de tamaño estándar (`/thumb/<h>/<hh>/<Archivo>/960px-<Archivo>`); `thumb.wikimedia.org` está bloqueado y la API corta si se piden muchas seguidas (error 429: espera y reintenta). Solo licencias libres (CC BY, CC BY-SA, CC0, dominio público) y crédito debajo de cada imagen (autor · Wikimedia Commons · licencia · cambios).
- `flujo/img/`: `bajar.sh` (bajadas a `img/orig/`), `prep.py` (recorte, tamaño, gris; borra flechas azules del autor) y los JPG finales. `flujo/engine6.py`: `foto()` incrusta el JPG en base64 dentro del SVG y dibuja marcas en fracciones 0-1 del recuadro: `flecha`, `circulo`, `corchete` (con guías `hasta`), `caja`, `texto`. Siempre ver la imagen (Read) y ubicar las marcas mirando el PNG ampliado; verificar que cada flecha cae sobre lo que nombra.
- Diseños hechos en `engine6.py`: 13 `comparador` (2 imágenes lado a lado + tarjetas), 14 `escalera` (trazo real + chequeo de inestabilidad + peldaños con salto del caso), 19 `mapa_signos` (cuerpo dibujado con signos numerados + tarjetas con foto), 20 `arbol_imagen` (pregunta → 2 ramas; la del caso con dibujo o foto). Dibujos: `ilu_nino_sarampion`, `ilu_rx_ddc` (esquema de Rx de cadera infantil con Hilgenreiner, Perkins, Shenton). Faltan: 15 ciclo, 16 criterios, 17 balanza, 18 red de atención.
- Ejemplo 2 (`flujo/demo27.py`, `flujo/pack27.py`, salida `flujo/out27demo/`): CIR-136 neumotórax (2 Rx reales), CAR-079 TSV inestable (ECG real), PED-247 sarampión (fotos CDC de Koplik y exantema), TRA-057 DDC (esquema dibujado). Entregado `MedQuizPro_ejemplo2_4_flujogramas_imagenes_reales.zip`: 8 SVG (4 nuevos + 4 del ejemplo 1), 4 PNG, `algoritmos.js` con 2114 y `bancos/traumatologia.json` (errata «a los Y meses» → «a los 9 meses» en TRA-057). **Esperar la aprobación del usuario antes de hacer los ~266 restantes.**
- Prueba como `<img>` (igual que la web): `flujo/imgtest.cjs <dir_svg> <dir_png>` carga el SVG como data URL y comprueba `naturalWidth` y captura; las fotos base64 se ven.
- Para ver PNG: `node shot.cjs <dir_svg> <dir_png>` (script en `flujo/shot26.cjs`); controles: `check.cjs` (0 desbordes). `check2.cjs` marca como «fuera de caja» los rótulos dentro de los dibujos: es esperado.

## Próxima tarea sugerida
Si el usuario aprueba el ejemplo 2: hacer los 266 flujogramas restantes del bloque ENAM 2026 (base `herramientas/e26/nuevos26.json`; ya hechos: CIR-133, CIR-158, CIR-150, GIN-274, CIR-136, CAR-079, PED-247, TRA-057; `algoritmos.js` pasa de 2114 a 2380; verificador general a 2380), con imagen real o dibujo en cada uno y los 20 diseños repartidos. Antes: 2106 preguntas y 2106 flujogramas. Ciencias Básicas ya está clasificada por materias (pendiente solo que el usuario suba el ZIP de materias o te pase sus archivos del servidor para adaptarlo).
Bancos y flujogramas están al día (1713). El PDF ya no tiene más preguntas: si el usuario pide más, pregúntale qué prefiere antes de empezar: (1) aceptar las ~250 oficiales omitidas por repetir tema, (2) rescatar algunas de clave dudosa, o (3) escribir preguntas de práctica nuevas (no oficiales).
