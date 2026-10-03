"""Paquete de 4 ejemplos: franja de imagen sin espacio vacío + clasificación o escala oficial con el caso ubicado.
Uso: python3 build27.py out27b GIN-255 HEM-047 INF-124 GAS-054 && node check27.cjs out27b/flujogramas out27b/png
     && python3 pack27b.py"""
import json, os, re, shutil, zipfile

B = "out27b/pack"
ZIP = "../../MedQuizPro_ejemplo_4_clasificaciones.zip"
order = json.load(open("out27b/order.json"))
shutil.rmtree(B, ignore_errors=True)
os.makedirs(f"{B}/flujogramas")
os.makedirs(f"{B}/vistas")
js = open("../site/algoritmos.js").read()


def js_str(t):
    return t.replace("\\", "\\\\").replace('"', '\\"')


for i, archivo, titulo, tipo, tri in order:
    shutil.copy(f"out27b/flujogramas/{archivo}.svg", f"{B}/flujogramas/")
    shutil.copy(f"out27b/png/{archivo}.png", f"{B}/vistas/")
    m = re.search(r'"%s":\s*\{[^}]*\}' % re.escape(i), js)
    assert m and f'flujogramas/{archivo}.svg' in m.group(0), i
    blk = re.sub(r'titulo:\s*"(?:[^"\\]|\\.)*"', 'titulo: "%s"' % js_str(titulo), m.group(0))
    blk = re.sub(r'alt:\s*"(?:[^"\\]|\\.)*"', 'alt: "Flujograma: %s"' % js_str(titulo), blk)
    js = js[:m.start()] + blk + js[m.end():]
open(f"{B}/algoritmos.js", "w").write(js)

NOMBRES = {"GIN-255": "Clasificación de Page (desprendimiento de placenta)",
           "HEM-047": "Clasificación FAB de la leucemia mieloide aguda (M0-M7)",
           "INF-124": "Clasificación del dengue OPS/OMS y grupos MINSA (A, B1, B2, C)",
           "GAS-054": "Guías de Tokio 2018: gravedad de la colangitis (grado I, II, III)"}
lista = "\n".join(f"  {k + 1}. {i} · {t}\n     → {NOMBRES[i]}" for k, (i, a, t, _, _) in enumerate(order))
LEEME = f"""MedQuizPro · 4 ejemplos: sin espacio vacío y con clasificaciones oficiales
=========================================================================

Qué cambió
----------
1. Sin espacio en blanco junto a la imagen.
   Antes, en «Así se ve en este caso», la imagen era alta y las notas cortas: quedaba un
   hueco blanco grande. Ahora:
   - cada nota tiene un título y una explicación;
   - la foto se agranda o se achica (sin deformarse) para acompañar el alto de las notas;
   - las notas se reparten todo el alto, sin dejar hueco;
   - el verificador rechaza el flujograma si todavía queda un hueco.
2. Clasificaciones y escalas con su nombre oficial.
   Un bloque nuevo «Clasificación oficial» muestra el nombre (Page, FAB, Tokio...),
   todos sus grados con sus criterios y el grado del caso marcado con «ESTE CASO».
   Debajo explica por qué el caso cae ahí (✓ lo que cumple, ✕ lo que lo descarta del
   grado vecino) y la conducta que corresponde a ese grado.
   El color de cada grado va de verde (leve) a rojo (grave).
3. La Rx dibujada del dengue se cambió por una Rx real de edema pulmonar.

Los 4 ejemplos
--------------
{lista}

Notas
-----
- En el DPP, la clasificación de Page muestra que el caso es grado II (feto vivo con sufrimiento):
  el grado III exige feto muerto. El título se ajustó a eso.
- En la LMA, los bastones de Auer ubican el caso entre M1 y M4; el subtipo exacto lo da la
  citometría de flujo y la genética.
- En la colangitis, con los datos que da la pregunta el caso es grado I (solo cumple 1 criterio de grado II).

Cómo instalar
-------------
Copiar flujogramas/ y algoritmos.js sobre los del sitio (los nombres de archivo no cambian;
algoritmos.js solo actualiza el título del DPP). En vistas/ hay un PNG de cada uno.

Imágenes (Wikimedia Commons)
----------------------------
- Desprendimiento de placenta, pieza quirúrgica · Mikael Häggström · CC0
- Bastón de Auer · AFIP · dominio público
- Edema pulmonar agudo, Rx AP portátil · Frank Gaillard y Jeremy Jones (Radiopaedia) · CC BY-SA 3.0
  (se borró el rótulo de la hora y se recortó)
- Colangiorresonancia con coledocolitiasis · Hellerhoff · CC BY-SA 3.0 (se borraron flechas y letras del autor)
Las imágenes son de otros pacientes con el mismo hallazgo; así se indica bajo cada una.
"""
open(f"{B}/LEEME.txt", "w").write(LEEME)
if os.path.exists(ZIP):
    os.remove(ZIP)
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(B):
        for f in sorted(files):
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, B))
print("ok", ZIP, os.path.getsize(ZIP) // 1024, "KB")
