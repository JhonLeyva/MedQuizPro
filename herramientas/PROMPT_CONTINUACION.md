# MedQuizPro — instrucciones para continuar el trabajo

Eres el asistente técnico de MedQuizPro/MedQuizPlus, un banco de preguntas del ENAM (examen médico peruano) publicado en Hostinger: https://lime-louse-621404.hostingersite.com. Responde siempre en español, de forma breve y sin jerga.

## Reglas del repositorio
- Repo `jhonleyva/medquizpro`, clonado en `/home/user/MedQuizPro`. Trabaja en la rama que te asigne la sesión; si es nueva, créala desde `origin/claude/sweet-franklin-dbg0mc` (ahí está todo el trabajo más reciente). No abras PR salvo que te lo pida.
- Cada entrega es un ZIP en la raíz del repo, con commit y `git push -u origin <tu rama>`. Si falla por red, reintenta a los 2, 4, 8 y 16 s. Después envíalo con SendUserFile (display `attach`).
- El pie de cada commit lo indica el system-reminder de la sesión nueva. No pongas identificadores de modelo en commits ni en archivos.
- Trabaja en tu scratchpad. Copia primero `herramientas/` ahí: `cp -r /home/user/MedQuizPro/herramientas/. $S/`. Los scripts usan rutas relativas a esa carpeta y a `$S/flujo/`.

## Estado actual (29-sep-2026, actualizado)
- **Rama con el trabajo más reciente:** `claude/sweet-franklin-dbg0mc`. Tiene los bloques 7 y 8, el banco de Ciencias Básicas (485) y sus flujogramas (total 2106 preguntas y 2106 flujogramas).
- **Bancos:** 1713 preguntas, bloques 1 a 8.
  - Último paquete: `MedQuizPro_bloque8_134_preguntas.zip`.
  - `herramientas/site/bancos/` ya contiene esos 17 JSON finales.
- **Flujogramas:** existen para las 1713 preguntas de los bloques 1–8. No falta ninguno.
  - Último paquete: `MedQuizPro_flujogramas_bloque8.zip`, con `algoritmos.js` de 1713 entradas (en `herramientas/flujo/`: `content8a…d.py`, `c8.py`, `build8f.py`, `finish8.py`, `chk8.sh`, `existing_names8.txt`; el bloque 7 usa `content7a…n.py`, `c7.py`, `build7f.py`, `finish7.py`).
  - Para un bloque 9, añade a `existing_names8.txt` los nombres de `out8/flujogramas` y usa como base `out8/pack/algoritmos.js`.
  - Hecho: `MedQuizPro_flujogramas_sin_palabra_respuesta.zip` corrige 143 SVG (80 del bloque 6, regenerados con `herramientas/flujo/rebuild6.py`; 63 de los bloques 2–5, texto reemplazado). Nombres sin cambio. Bloques 2–8 revisados: ya no dicen «respuesta». Los 97 SVG antiguos del bloque 1 solo están en el servidor y no se revisaron.
- **Banco de Ciencias Básicas (nuevo, 29-sep-2026):** del PDF `Banco_Ciencias_Básicas.pdf` (Villamedic, ed. 2019, 458 preguntas con tabla de claves y sin comentarios) entraron 393 preguntas, todas en `ciencias_basicas.json` (CB-093 a CB-485; CB queda en 485 y el total del sitio en 2106).
  - Paquete: `MedQuizPro_ciencias_basicas_393_preguntas.zip` (solo `bancos/ciencias_basicas.json` + `LEEME.txt`).
  - `examen_origen`: "ENAM · Ciencias Básicas 2019" (debe empezar por "ENAM": el filtro de la web publicada solo muestra esas), `año` 2019. Cada una lleva comentario docente propio.
  - Herramientas en `herramientas/cb/`: `parse.py` (PDF → `cbq.json`), `r00…r09.py` (revisión: `D[n]=(tema, clave, comentario)`, `O` opciones, `N` enunciado, `X` excluidas con motivo), `merge.py` (valida), `build.py` (lista FIX de ortografía), `leeme.py`, `testcb.cjs`, `nuevoscb.json`.
  - 65 omitidas (56 repetidas, 9 mal planteadas) y 12 claves del PDF corregidas.
  - Flujogramas hechos: `MedQuizPro_flujogramas_ciencias_basicas.zip` (393 SVG, `algoritmos.js` con 2106 entradas, verificadores `verificar-flujogramas-bloquecb.html` y general a 2106).
    Herramientas en `herramientas/flujo/`: `ccb.py` (lista `FCB`; curva por defecto en `fases`), `refcb.py` (fuentes), `contentcba…j.py`, `buildcbf.py`, `finishcb.py`, `chkcb.sh`, `e2ecb.cjs`, `existing_namescb.txt`, `ordercb.json`.
    Para un bloque siguiente: añade a `existing_namescb.txt` los nombres de `ordercb.json` y usa como base `outcb/pack/algoritmos.js` (2106).
- **PDF original** (`Banco_ENAM_Respuestas_Resaltadas.pdf`, 2497 preguntas): ya no está en disco. Su versión procesada es `herramientas/parsed.json`.
- **PDF revisado completo.** Las 391 pendientes se revisaron en el bloque 8 (`sel8.py`: 134 en `SEL`, 257 en `EXC`). Ya no quedan preguntas del PDF por usar.

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

## Flujo A: nuevo bloque de preguntas
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

## Flujo B: flujogramas de un bloque (siguiente: bloque 7, 500 IDs de `nuevos7.json`)
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

## Próxima tarea sugerida
Bancos y flujogramas al día: 2106 preguntas y 2106 flujogramas.
Bancos y flujogramas están al día (1713). El PDF ya no tiene más preguntas: si el usuario pide más, pregúntale qué prefiere antes de empezar: (1) aceptar las ~250 oficiales omitidas por repetir tema, (2) rescatar algunas de clave dudosa, o (3) escribir preguntas de práctica nuevas (no oficiales).
