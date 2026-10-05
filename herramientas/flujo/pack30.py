"""Paquete de la Entrega 3 (flujogramas 1001-1500 de algoritmos.js, revisados).
Uso: python3 build28.py <out> $(ids de rev30/entrega3.json) && node check27.cjs <out>/flujogramas <out>/png
     && python3 pack30.py <out> <carpeta_paquete> <zip>
Copia los SVG, actualiza títulos y textos alternativos en algoritmos.js, arma un visor HTML y el LEEME
(diseños usados, clasificaciones, créditos de imágenes de PubMed Central y Commons). Deja algoritmos.js en ../site."""
import json, os, re, shutil, sys, zipfile, importlib, html, collections
import c27, c28

# DOS y CON_CREDITO pierden los créditos de sus fotos: se guardan para el LEEME
_dos, _cc = c27.DOS, c27.CON_CREDITO


def _dos_con_creditos(a, b, **k):
    r = _dos(a, b, **k)
    r["fotos"] = [a, b]
    return r


class _Ilu:
    def __init__(self, f, im):
        self.f, self.foto = f, im

    def __call__(self, *a, **k):
        return self.f(*a, **k)


def _cc_con_credito(im, *a, **k):
    return _Ilu(_cc(im, *a, **k), im)


c27.DOS = c28.DOS = _dos_con_creditos
c27.CON_CREDITO = _cc_con_credito
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
from engine9 import CATALOGO

OUT, B, ZIP = sys.argv[1], sys.argv[2], sys.argv[3]
order = json.load(open(f"{OUT}/order.json"))
assert [o[0] for o in order] == json.load(open("rev30/entrega3.json"))
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
assert not set(c28.CORRIGE) & {o[0] for o in order}, "hay claves que corregir: añadir el banco al paquete"


# 2. Fotos de cada flujograma (en cualquier parte de la ficha) con su crédito
def fotos(o, cred=None, acc=None):
    acc = [] if acc is None else acc
    if isinstance(o, _Ilu):
        fotos(o.foto, cred, acc)
    elif isinstance(o, dict):
        c = o["credito"] if isinstance(o.get("credito"), str) and o.get("credito") else cred
        if "foto" in o:
            acc.append((os.path.basename(o["foto"]), c or "?"))
        for k, v in o.items():
            ck = o.get(f"{k}_credito")
            fotos(v, ck if isinstance(ck, str) and ck else c, acc)
    elif isinstance(o, (list, tuple)):
        for v in o:
            fotos(v, cred, acc)
    return acc


def visual(o):
    if callable(o):
        return True
    if isinstance(o, dict):
        return "foto" in o or any(visual(v) for v in o.values())
    if isinstance(o, (list, tuple)):
        return any(visual(v) for v in o)
    return False


NOMBRE = {k: (n, nom) for n, k, nom in CATALOGO}
creditos = collections.defaultdict(set)
usos = collections.Counter()
filas = []
n_esc = n_tri = n_img = n_real = n_multi = n_vis = 0
for i, archivo, titulo, tipo, *_ in order:
    f = spec[i]
    usos[tipo] += 1
    extra = ["Diseño %d · %s" % NOMBRE.get(tipo, (0, tipo))]
    if f.get("escala"):
        n_esc += 1
        extra.append("Clasificación: " + f["escala"]["nombre"])
    if f.get("triada"):
        n_tri += 1
        extra.append("Signos/criterios: " + ", ".join(g[0] for g in f["triada"]["grupos"]))
    n_vis += visual(f)
    fs = sorted(set(fotos(f)))
    if fs:
        n_img += 1
        n_multi += len(fs) >= 2
        reales = [x for x in fs if "MedQuizPro" not in x[1]]
        n_real += bool(reales)
        for foto, cred in fs:
            creditos[cred].add(foto)
        extra.append("Imágenes: " + ", ".join(x[0] for x in fs))
    filas.append((i, archivo, titulo, f["esp"], extra))
sin = creditos.pop("?", set())
assert not sin, f"fotos sin crédito: {sin}"

# 3. Visor HTML (abre los SVG de flujogramas/ sin servidor)
items = "\n".join(
    f'<figure data-t="{html.escape((i + " " + t + " " + " ".join(e)).lower())}"><figcaption><b>{i}</b> · {html.escape(t)}'
    f'<small>{html.escape(e[0])}</small></figcaption><a href="flujogramas/{a}.svg" target="_blank">'
    f'<img loading="lazy" src="flujogramas/{a}.svg" alt="{html.escape(t)}"></a></figure>'
    for i, a, t, _, e in filas)
open(f"{B}/ver-entrega3.html", "w").write(f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Entrega 3 · 500 flujogramas</title>
<style>body{{font-family:Arial,sans-serif;margin:0;background:#f1f5f9;color:#0f172a}}header{{position:sticky;top:0;background:#0f766e;color:#fff;padding:12px 16px}}
input{{width:100%;max-width:520px;padding:8px;border-radius:6px;border:0;font-size:15px}}main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;padding:16px}}
figure{{margin:0;background:#fff;border-radius:10px;padding:10px;box-shadow:0 1px 3px #0002}}figcaption{{font-size:13px;margin-bottom:6px}}
small{{display:block;color:#0f766e;font-weight:bold}}img{{width:100%;height:auto;border:1px solid #e2e8f0;border-radius:6px}}</style></head><body>
<header><b>Entrega 3 · flujogramas 1001-1500 revisados</b><br><input id="q" placeholder="Buscar por ID, tema, diseño o especialidad (ej. GIN-, Glasgow, grafica)"></header>
<main id="m">{items}</main>
<script>q.oninput=()=>{{const v=q.value.toLowerCase();for(const f of m.children)f.style.display=f.dataset.t.includes(v)?'':'none'}}</script></body></html>""")

# 4. LEEME
detalle = "\n".join(f"{k + 1:3}. {i} · {t}" + "".join(f"\n       + {x}" for x in extra) for k, (i, a, t, e, extra) in enumerate(filas))
propias = {c: v for c, v in creditos.items() if "MedQuizPro" in c}
pmc = {c: v for c, v in creditos.items() if "MedQuizPro" not in c and "PMC" in c}
commons = {c: v for c, v in creditos.items() if "MedQuizPro" not in c and "PMC" not in c}
lista = lambda d: "\n".join(f"- {c} ({', '.join(sorted(v))})" for c, v in sorted(d.items()))
dis = "\n".join(f"  {n:2}. {nom}: {usos[k]}" for n, k, nom in CATALOGO if usos[k])
falta = "\n".join(f"  {n:2}. {nom}" for n, k, nom in CATALOGO if not usos[k])
LEEME = f"""MedQuizPro · Entrega 3: flujogramas 1001 a 1500 revisados
========================================================

Qué es
------
Los flujogramas 1001 a 1500 del banco (en el orden de algoritmos.js), rehechos uno por uno con el estándar de la
Entrega 2 y con lo nuevo que pidió:

- MÁS DIVERSIDAD: {len(usos)} diseños distintos en esta entrega (antes eran 20). Se programaron diseños nuevos:
  lectura guiada de imagen, mapa de zonas, regla de umbrales, tabla de decisión, reloj de urgencia, cuadrícula de
  diferenciales con foto, gráfica clínica con el punto del caso, pirámide, panel de laboratorio, gasometría paso a
  paso, calendario de dosis, lista de verificación, signos de alarma, dosis por peso, cadena de transmisión, grados
  con foto, cascada fisiopatológica, ECG por territorios y monitor de signos vitales.
- Clasificación o escala oficial con su nombre (Glasgow, CURB-65, Tokio 2018, ATLS, Roper-Hall, METAVIR, AIEPI,
  Hinchey, ICROP3, FIGO, KDIGO, NYHA, Child-Pugh, Ranson...), con el caso marcado y el porqué: {n_esc} flujogramas.
- Signos, tríadas y criterios con nombre propio, marcando cuáles están en el caso: {n_tri} flujogramas.
- Imágenes que guían: {n_vis} flujogramas llevan foto, dibujo o ECG ({n_real} con foto o estudio real; {n_multi} con 2 o más
  fotos). Los demás se apoyan en diseños gráficos (reglas, gráficas, monitor, semáforo, pirámide...).
  · Fotos reales de PubMed Central (NCBI) con licencia libre: radiografías, TC, fondo de ojo, histología.
  · Fotos reales de Wikimedia Commons (Rx, TC, ecografías, frotis, fotos clínicas sin caras).
  · Cuando no había foto libre o útil: dibujos y ECG PROPIOS hechos para entenderse solos.
- Tabla «Opciones de la pregunta» con las 5 alternativas ACTUALES del banco y por qué cada una sí o no.
- Puntos clave y fuentes al 2026 (AHA/ILCOR 2025, ATLS 11.ª, ADA 2026, GINA/GOLD 2025, KDIGO, IDSA, CDC,
  OMS, ACOG, NICE, MINSA, Harrison 22.ª, Nelson 22.ª, Williams 26.ª...).

Diseños usados (n.º del catálogo de 50 · veces)
-----------------------------------------------
{dis}

Diseños del catálogo que aún no se usan (quedan para la Entrega 4)
-----------------------------------------------------------------
{falta}

Verificación
------------
- Los 500 se construyeron y pasaron el verificador de encaje: 0 textos fuera de su recuadro, 0 franjas con hueco,
  XML válido, sin la palabra prohibida y el mismo nombre de archivo que el publicado.
- Se revisaron a ojo en hojas de 5 (las 20 tandas de 25): marcas en su sitio, sin caras, texto legible.
- Prueba en la app: las 500 entradas de algoritmos.js cargan su imagen y cada ID existe en su banco.

Cómo instalar
-------------
1. Copiar la carpeta flujogramas/ sobre la del sitio (mismos nombres: se reemplazan).
2. Copiar algoritmos.js sobre el del sitio (incluye ya las Entregas 1 y 2; solo cambian el título y el texto
   alternativo de estas 500 entradas).
Para revisarlos sin instalar: abrir ver-entrega3.html (tiene buscador).
Esta entrega no cambia ninguna clave del banco. Algunas alternativas se muestran en la tabla abreviadas cuando eran
muy largas, o con otra palabra cuando decían «respuesta» (reservada en las imágenes); el banco no se toca.

Detalle de los 500
------------------
{detalle}

Imágenes de PubMed Central (NCBI), licencias CC BY / CC0 (son de otros pacientes; así se indica bajo cada una)
-------------------------------------------------------------------------------------------------------------
{lista(pmc)}

Imágenes de Wikimedia Commons (son de otros pacientes; así se indica bajo cada una)
----------------------------------------------------------------------------------
{lista(commons)}

Imágenes propias de MedQuizPro (no son de pacientes; se pueden usar libremente en el sitio)
------------------------------------------------------------------------------------------
{lista(propias)}
"""
open(f"{B}/LEEME.txt", "w").write(LEEME)

with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(B):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, B))
print("ok", len(order), "diseños", len(usos), "escalas", n_esc, "tríadas", n_tri, "con imagen", n_img, "reales", n_real,
      "2+", n_multi, "créditos PMC", len(pmc), "Commons", len(commons), "propios", len(propias))
