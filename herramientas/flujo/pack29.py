"""Paquete de la Entrega 2 (flujogramas 501-1000 de algoritmos.js, revisados).
Uso: python3 build28.py <out> $(ids de rev29/entrega2.json) && node check27.cjs <out>/flujogramas <out>/png
     && python3 pack28.py <out> <carpeta_paquete> <zip>
Copia los SVG, actualiza títulos y textos alternativos en algoritmos.js, arma un visor HTML y el LEEME
(precisiones de rev29/precisiones.md y créditos de imágenes). También deja algoritmos.js en ../site."""
import json, os, re, shutil, sys, zipfile, importlib, html
import c28

# DOS pierde los créditos de sus dos fotos: se guardan para el LEEME
_dos = c28.DOS


def _dos_con_creditos(a, b, **k):
    r = _dos(a, b, **k)
    r["fotos"] = [(a["foto"], a["credito"]), (b["foto"], b["credito"])]
    return r


c28.DOS = _dos_con_creditos
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content2[89][a-z]+\.py", f)):
    importlib.import_module(m)

OUT, B, ZIP = sys.argv[1], sys.argv[2], sys.argv[3]
order = json.load(open(f"{OUT}/order.json"))
spec = {f["id"]: f for f in c28.F28}
shutil.rmtree(B, ignore_errors=True)
os.makedirs(f"{B}/flujogramas")

# 1. SVG + algoritmos.js (solo cambian título y texto alternativo; el nombre de archivo es el publicado)
js = open("../site/algoritmos.js").read()


def js_str(t):
    return t.replace("\\", "\\\\").replace('"', '\\"')


for i, archivo, titulo, *_ in order:
    shutil.copy(f"{OUT}/flujogramas/{archivo}.svg", f"{B}/flujogramas/")
    m = re.search(r'"%s":\s*\{[^}]*\}' % re.escape(i), js)
    assert m and f"flujogramas/{archivo}.svg" in m.group(0), i
    blk = re.sub(r'titulo:\s*"(?:[^"\\]|\\.)*"', 'titulo: "%s"' % js_str(titulo), m.group(0))
    blk = re.sub(r'alt:\s*"(?:[^"\\]|\\.)*"', 'alt: "Flujograma: %s"' % js_str(titulo), blk)
    js = js[:m.start()] + blk + js[m.end():]
open(f"{B}/algoritmos.js", "w").write(js)
open("../site/algoritmos.js", "w").write(js)

# 2. Esta entrega no corrige claves del banco (las precisiones van al LEEME)
assert not set(c28.CORRIGE) & {o[0] for o in order}, "hay claves que corregir: añadir el banco al paquete"

# 3. Resumen por flujograma y créditos de imágenes
creditos = {}
filas = []
n_esc = n_tri = n_img = 0
for i, archivo, titulo, tipo, tri, esc, ban in order:
    f = spec[i]
    extra = []
    if f.get("escala"):
        n_esc += 1
        extra.append("Clasificación: " + f["escala"]["nombre"])
    if f.get("triada"):
        n_tri += 1
        extra.append("Signos/criterios: " + ", ".join(g[0] for g in f["triada"]["grupos"]))
    if f.get("banda"):
        n_img += 1
        img = f["banda"]["img"]
        fotos = img.get("fotos") or [(img.get("foto"), img.get("credito"))]
        for foto, cred in fotos:
            creditos.setdefault(cred, set()).add(os.path.basename(foto or ""))
        extra.append("Imagen: " + f["banda"]["titulo"])
    filas.append((i, archivo, titulo, f["esp"], extra))

# 4. Visor HTML (abre los SVG de flujogramas/ sin servidor)
items = "\n".join(
    f'<figure data-t="{html.escape((i + " " + t + " " + e).lower())}"><figcaption><b>{i}</b> · {html.escape(t)}'
    f'<small>{html.escape(e)}</small></figcaption><a href="flujogramas/{a}.svg" target="_blank">'
    f'<img loading="lazy" src="flujogramas/{a}.svg" alt="{html.escape(t)}"></a></figure>'
    for i, a, t, e, _ in filas)
open(f"{B}/ver-entrega2.html", "w").write(f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Entrega 2 · 500 flujogramas</title>
<style>body{{font-family:Arial,sans-serif;margin:0;background:#f1f5f9;color:#0f172a}}header{{position:sticky;top:0;background:#0f766e;color:#fff;padding:12px 16px}}
input{{width:100%;max-width:520px;padding:8px;border-radius:6px;border:0;font-size:15px}}main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;padding:16px}}
figure{{margin:0;background:#fff;border-radius:10px;padding:10px;box-shadow:0 1px 3px #0002}}figcaption{{font-size:13px;margin-bottom:6px}}
small{{display:block;color:#0f766e;font-weight:bold}}img{{width:100%;height:auto;border:1px solid #e2e8f0;border-radius:6px}}</style></head><body>
<header><b>Entrega 2 · flujogramas 501-1000 revisados</b><br><input id="q" placeholder="Buscar por ID, tema o especialidad (ej. GIN-, Page, dengue)"></header>
<main id="m">{items}</main>
<script>q.oninput=()=>{{const v=q.value.toLowerCase();for(const f of m.children)f.style.display=f.dataset.t.includes(v)?'':'none'}}</script></body></html>""")

# 5. LEEME
detalle = "\n".join(f"{k + 1:3}. {i} · {t}" + "".join(f"\n       + {x}" for x in extra) for k, (i, a, t, e, extra) in enumerate(filas))
propias = {c: v for c, v in creditos.items() if "MedQuizPro" in c}
reales = {c: v for c, v in creditos.items() if "MedQuizPro" not in c}
cred = "\n".join(f"- {c} ({', '.join(sorted(v))})" for c, v in sorted(reales.items()))
cred_p = "\n".join(f"- {c}: {', '.join(sorted(v))}" for c, v in sorted(propias.items()))
prec = "\n".join(l.rstrip() for l in open("rev29/precisiones.md") if l.startswith("- "))
n_prec = prec.count("\n- ") + 1
LEEME = f"""MedQuizPro · Entrega 2: flujogramas 501 a 1000 revisados
=======================================================

Qué es
------
Los flujogramas 501 a 1000 del banco (en el orden de algoritmos.js), rehechos uno por uno con el mismo estándar
de la Entrega 1 y, como pidió, con MUCHAS más imágenes que guían:

- Clasificación o escala oficial con su nombre (CURB-65, Westley, Glasgow, NIHSS, Rotterdam, Page, Wells, Light,
  Forrester, Stevenson, AHA/ACC 2025, KDIGO, DSM-5-TR...), con todos sus grados, el caso marcado con «ESTE CASO»,
  el porqué y la conducta: {n_esc} flujogramas.
- Signos, tríadas y criterios con nombre propio, marcando cuáles están en el caso: {n_tri} flujogramas.
- Imagen que guía (franja «Así se ve...», sin espacio en blanco, con marcas y notas): {n_img} flujogramas.
  · Fotos y estudios reales de Wikimedia Commons (Rx, TC, ecografías, frotis, fotos clínicas sin caras).
  · Cuando no había foto libre o útil, dibujos y trazados PROPIOS hechos para que se entiendan solos:
    ECG de enseñanza (FA, FV, QT largo, pericarditis, TEP, taponamiento...) y esquemas (regla de los 9,
    profundidad de las quemaduras, placenta baja, partograma, nervio peroneo y pie caído, balón intrauterino,
    pie plano flexible, derrame pleural...). La lista completa está al final.
- Tabla «Opciones de la pregunta» con las 5 alternativas ACTUALES del banco y por qué cada una sí o no.
- Puntos clave y fuentes actualizadas a 2026 (AHA/ACC 2025, AHA/ASA, ESC 2024, ADA 2026, GINA/GOLD 2025,
  KDIGO, IDSA, CDC, OMS/FIGO 2025, ACOG, ASCCP, NICE, MINSA, ATLS 11.ª, Harrison 22.ª, Nelson 22.ª...).

Verificación
------------
- Los 500 se construyeron y pasaron el verificador de encaje: 0 textos fuera de su recuadro, 0 franjas con hueco,
  XML válido, sin la palabra prohibida y el mismo nombre de archivo que el publicado.
- Cada franja de imagen se revisó a ojo (marcas en su sitio, sin caras, texto legible).
- Prueba en la app: las 500 entradas de algoritmos.js cargan su imagen y cada ID existe en su banco.

Cómo instalar
-------------
1. Copiar la carpeta flujogramas/ sobre la del sitio (mismos nombres: se reemplazan).
2. Copiar algoritmos.js sobre el del sitio (incluye ya los cambios de la Entrega 1; solo cambian el título y el
   texto alternativo de estas 500 entradas).
Para revisarlos sin instalar: abrir ver-entrega2.html (tiene buscador).
Esta entrega no cambia ninguna clave del banco.

Precisiones que el flujograma explica (la clave del banco NO cambia) · {n_prec}
------------------------------------------------------------------------
{prec}
- Algunas alternativas se muestran en la tabla abreviadas cuando eran muy largas, o con otra palabra cuando decían
  «respuesta» (reservada en las imágenes); el banco no se toca.

Detalle de los 500
------------------
{detalle}

Imágenes reales (Wikimedia Commons; son de otros pacientes, así se indica bajo cada una)
-------------------------------------------------------------------------------------
{cred}

Imágenes propias de MedQuizPro (no son de pacientes; se pueden usar libremente en el sitio)
------------------------------------------------------------------------------------------
{cred_p}
"""
open(f"{B}/LEEME.txt", "w").write(LEEME)

with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(B):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, B))
print("ok", len(order), "escalas", n_esc, "tríadas", n_tri, "imágenes", n_img, "créditos reales", len(reales), "propios", len(propias), "precisiones", n_prec)
