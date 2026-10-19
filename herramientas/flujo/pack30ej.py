"""Paquete de los 4 ejemplos de la Entrega 3 (diseños nuevos 21-24 e imágenes de PubMed Central).
Uso: python3 build28.py <out> CIR-080 PED-142 TRA-028 INF-070 && node check27.cjs <out>/flujogramas <out>/png
     && python3 pack30ej.py <out> <carpeta_paquete> <zip>
Cambia título y texto alternativo en una COPIA de algoritmos.js (site/ no se toca hasta la entrega completa)."""
import json, os, re, shutil, sys, zipfile, html
from engine9 import CATALOGO, HECHOS

OUT, B, ZIP = sys.argv[1], sys.argv[2], sys.argv[3]
order = json.load(open(f"{OUT}/order.json"))
shutil.rmtree(B, ignore_errors=True)
os.makedirs(f"{B}/flujogramas")
os.makedirs(f"{B}/png")
js = open("../site/algoritmos.js").read()


def js_str(t):
    return t.replace("\\", "\\\\").replace('"', '\\"')


for i, archivo, titulo, *_ in order:
    shutil.copy(f"{OUT}/flujogramas/{archivo}.svg", f"{B}/flujogramas/")
    shutil.copy(f"{OUT}/png/{archivo}.png", f"{B}/png/")
    m = re.search(r'"%s":\s*\{[^}]*\}' % re.escape(i), js)
    assert m and f"flujogramas/{archivo}.svg" in m.group(0), i
    blk = re.sub(r'titulo:\s*"(?:[^"\\]|\\.)*"', 'titulo: "%s"' % js_str(titulo), m.group(0))
    blk = re.sub(r'alt:\s*"(?:[^"\\]|\\.)*"', 'alt: "Flujograma: %s"' % js_str(titulo), blk)
    js = js[:m.start()] + blk + js[m.end():]
open(f"{B}/algoritmos.js", "w").write(js)

DIS = {"lectura": "21 · Lectura guiada de imagen", "zonas": "22 · Mapa de zonas (diana)", "regla": "23 · Regla de umbrales",
       "decision": "24 · Tabla de decisión de dos entradas"}
items = "\n".join(
    f'<figure><figcaption><b>{i}</b> · {html.escape(t)}<small>Diseño {DIS[tp]}</small></figcaption>'
    f'<a href="flujogramas/{a}.svg" target="_blank"><img src="flujogramas/{a}.svg" alt="{html.escape(t)}"></a></figure>'
    for i, a, t, tp, *_ in order)
open(f"{B}/ver-ejemplos.html", "w").write(f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Entrega 3 · 4 ejemplos</title>
<style>body{{font-family:Arial,sans-serif;margin:0;background:#f1f5f9;color:#0f172a}}header{{background:#0f766e;color:#fff;padding:12px 16px}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:14px;padding:16px}}
figure{{margin:0;background:#fff;border-radius:10px;padding:10px;box-shadow:0 1px 3px #0002}}figcaption{{font-size:13px;margin-bottom:6px}}
small{{display:block;color:#0f766e;font-weight:bold}}img{{width:100%;height:auto;border:1px solid #e2e8f0;border-radius:6px}}</style></head><body>
<header><b>Entrega 3 · 4 ejemplos con diseños nuevos e imágenes de PubMed Central</b></header><main>{items}</main></body></html>""")

hechos = "\n".join(f"  {n:2}. {nom}" + ("   ← NUEVO, usado en estos ejemplos" if k in HECHOS else "")
                   for n, k, nom in CATALOGO if n <= 24)
por_hacer = "\n".join(f"  {n:2}. {nom}" for n, k, nom in CATALOGO if n > 24)
LEEME = f"""MedQuizPro · Entrega 3 · 4 EJEMPLOS (flujogramas con diseños nuevos e imágenes de PubMed Central)
==============================================================================================

Qué es
------
Cuatro flujogramas de la Entrega 3 (1001-1500 en el orden de algoritmos.js), hechos con el mismo estándar de la
Entrega 2 y con lo nuevo que pidió:

1. MÁS DIVERSIDAD: el catálogo pasa de 20 a 50 diseños. Cada ejemplo estrena uno:
   - CIR-080 · Diverticulitis con absceso de 5 cm → diseño 21 «Lectura guiada de imagen»: TC real con puntos
     numerados que se leen en orden, el paso del caso resaltado y una tira con los otros grados (Hinchey 0, Ia, II).
     Clasificación de Hinchey modificada con el caso en Ib y su porqué.
   - PED-142 · Retinopatía del prematuro → diseño 22 «Mapa de zonas»: zonas I-II-III de la retina dibujadas
     (la III como media luna temporal) y los estadios con fotos reales de fondo de ojo (cresta, proliferación,
     enfermedad plus). Clasificación ETROP (Tipo 1 / Tipo 2) y foto de la retina tras el láser.
   - TRA-028 · Fractura en cuña por osteoporosis → diseño 23 «Regla de umbrales»: T-score de la OMS y grado de
     Genant en reglas de colores; DXA real (en español) con el T-score señalado, Rx real de fractura en cuña de L4
     y criterios diagnósticos de osteoporosis (BHOF 2022 / AACE 2020) con el caso ubicado.
   - INF-070 · Mordedura de perro en la mano → diseño 24 «Tabla de decisión»: el lavado como PASO 1 para todos,
     luego categoría de exposición de la OMS × estado del perro, con la fila del caso (III); foto real de una
     mordedura y calendario propio (vacuna días 0-3-7-14, inmunoglobulina, observar al perro 10 días).

2. IMÁGENES DE PUBMED CENTRAL (NCBI): se bajan solo de artículos de acceso abierto con licencia CC BY o CC0, con
   su crédito (autores · revista · PMCID · licencia) debajo de cada imagen. Se completan con Wikimedia Commons y,
   si no hay foto útil, con dibujos propios. De 2 a 4 imágenes por flujograma, según lo que pida la pregunta.

Verificación
------------
- Verificador de encaje: 0 problemas en los 4 (sin textos fuera de su recuadro, sin franjas con hueco, XML válido,
  sin la palabra prohibida, mismo nombre de archivo que el publicado).
- Cada imagen se revisó a ojo: marcas en su sitio, sin caras, texto legible.
- Prueba en la app: las 4 entradas cargan su imagen y abren en el modal sin errores.

Cómo verlos e instalarlos
-------------------------
- Para revisarlos: abrir ver-ejemplos.html o las imágenes de png/.
- Para publicarlos ya: copiar flujogramas/ sobre la del sitio (mismos nombres, se reemplazan) y algoritmos.js
  (solo cambian el título y el texto alternativo de estas 4 entradas). No cambia ninguna clave del banco.

Catálogo de 50 diseños
----------------------
Ya hechos (1-24):
{hechos}
Por hacer en la Entrega 3 (se irán estrenando según la pregunta):
{por_hacer}

Imágenes reales (son de otros pacientes; así se indica bajo cada una)
-------------------------------------------------------------------
PubMed Central (NCBI), acceso abierto:
- Papaoikonomou et al. · Cureus 2025 · PMC12857236 · CC BY 4.0 — TC de diverticulitis Hinchey 0, Ia, Ib y II (CIR-080)
- Zhao et al. · Scientific Data 2024 · PMC11130119 · CC BY 4.0 — fondos de ojo: estadio 2, estadio 3 y láser (PED-142)
- Sharafi et al. · Int J Retina Vitreous 2025 · PMC12639888 · CC BY 4.0 — enfermedad plus (PED-142)
Wikimedia Commons:
- Jmarchn · CC BY-SA 3.0 — densitometría (DXA) lumbar con osteoporosis (TRA-028; recortada al gráfico y la tabla)
- James Heilman, MD · CC BY-SA 3.0 — Rx lateral con fractura por compresión de L4 (TRA-028)
- Assianir · CC BY-SA 3.0 — mordedura de perro en el dorso de la mano (INF-070)
Propias de MedQuizPro: calendario de la profilaxis antirrábica (INF-070) y el dibujo de las zonas de la retina (PED-142).

Siguiente paso
--------------
Si aprueba estos ejemplos, se hacen los 500 de la Entrega 3 en tandas de 25 con este estándar, estrenando los
diseños 25-50 y buscando primero en PubMed Central.
"""
open(f"{B}/LEEME.txt", "w").write(LEEME)
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(B):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, B))
print("ok", len(order), ZIP)
