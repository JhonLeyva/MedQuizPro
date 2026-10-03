"""Paquete de la Entrega 1 (500 flujogramas revisados).
Uso: python3 build28.py <out> $(ids de rev28/entrega1.json) && node check27.cjs <out>/flujogramas <out>/png
     && python3 pack28.py <out> <carpeta_paquete> <zip>
Copia los SVG, actualiza títulos y textos alternativos en algoritmos.js, aplica la corrección de clave al banco,
arma un visor HTML y el LEEME. También deja algoritmos.js y el banco corregido en ../site."""
import json, os, re, shutil, sys, zipfile, importlib, html
import c28

# DOS pierde los créditos de sus dos fotos: se guardan para el LEEME
_dos = c28.DOS


def _dos_con_creditos(a, b, **k):
    r = _dos(a, b, **k)
    r["fotos"] = [(a["foto"], a["credito"]), (b["foto"], b["credito"])]
    return r


c28.DOS = _dos_con_creditos
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content28[a-z]+\.py", f)):
    importlib.import_module(m)

OUT, B, ZIP = sys.argv[1], sys.argv[2], sys.argv[3]
order = json.load(open(f"{OUT}/order.json"))
spec = {f["id"]: f for f in c28.F28}
shutil.rmtree(B, ignore_errors=True)
os.makedirs(f"{B}/flujogramas")
os.makedirs(f"{B}/bancos")

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

# 2. Corrección de clave en el banco
banco = json.load(open("../site/bancos/traumatologia.json"))
for q in banco["preguntas"]:
    if q["id"] in c28.CORRIGE:
        idx, motivo = c28.CORRIGE[q["id"]]
        if q["correcta"] != idx:
            q["correcta"], q["clave_correcta"] = idx, "ABCDE"[idx]
            q["explicacion"] = motivo
            q["comentario"] = (motivo + " Nota: la clave oficial publicada para esta pregunta fue C (palmar menor); "
                               "se corrige porque el palmar menor no participa en el cierre del puño.")
txt = json.dumps(banco, ensure_ascii=False, indent=2)
open(f"{B}/bancos/traumatologia.json", "w").write(txt)
open("../site/bancos/traumatologia.json", "w").write(txt)

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
open(f"{B}/ver-entrega1.html", "w").write(f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Entrega 1 · 500 flujogramas</title>
<style>body{{font-family:Arial,sans-serif;margin:0;background:#f1f5f9;color:#0f172a}}header{{position:sticky;top:0;background:#0f766e;color:#fff;padding:12px 16px}}
input{{width:100%;max-width:520px;padding:8px;border-radius:6px;border:0;font-size:15px}}main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;padding:16px}}
figure{{margin:0;background:#fff;border-radius:10px;padding:10px;box-shadow:0 1px 3px #0002}}figcaption{{font-size:13px;margin-bottom:6px}}
small{{display:block;color:#0f766e;font-weight:bold}}img{{width:100%;height:auto;border:1px solid #e2e8f0;border-radius:6px}}</style></head><body>
<header><b>Entrega 1 · 500 flujogramas revisados</b><br><input id="q" placeholder="Buscar por ID, tema o especialidad (ej. GIN-, Page, dengue)"></header>
<main id="m">{items}</main>
<script>q.oninput=()=>{{const v=q.value.toLowerCase();for(const f of m.children)f.style.display=f.dataset.t.includes(v)?'':'none'}}</script></body></html>""")

# 5. LEEME
detalle = "\n".join(f"{k + 1:3}. {i} · {t}" + "".join(f"\n       + {x}" for x in extra) for k, (i, a, t, e, extra) in enumerate(filas))
cred = "\n".join(f"- {c} ({', '.join(sorted(v))})" for c, v in sorted(creditos.items()))
LEEME = f"""MedQuizPro · Entrega 1: 500 flujogramas revisados
=================================================

Qué es
------
Los 500 flujogramas más antiguos del banco (bloques 1 a 5, en el orden de algoritmos.js), rehechos uno por uno
con lo que acordamos en los ejemplos:

- Clasificación o escala oficial con su nombre (Page, Gustilo, Tokio, Wells, Glasgow, Alvarado, West Haven, CEAP,
  Montreal, Fontaine, Burch-Wartofsky, CHA₂DS₂-VA, Bishop, Westley...), con TODOS sus grados, el caso marcado con
  «ESTE CASO», el porqué (✓ lo que cumple, ✕ lo que lo separa del grado vecino) y la conducta: {n_esc} flujogramas.
- Signos, tríadas y criterios con nombre propio (Beck, Wernicke, Gregg, Light, Amsel, Mayo, CRAB, Gurd, Jalan,
  Triple I, Roma IV, UK Working Party...), marcando cuáles están en el caso: {n_tri} flujogramas.
- Imagen real (Wikimedia Commons) solo donde aporta: Rx, TC, RM, ecografías, frotis, fotos clínicas, con marcas y
  notas «título + explicación» que llenan todo el alto (sin espacio en blanco): {n_img} flujogramas.
- Tabla «Opciones de la pregunta» con las 5 alternativas ACTUALES del banco (las ya corregidas) y por qué cada una
  sí o no.
- Puntos clave y fuentes actualizadas a 2026 (guías ESC, AHA/ILCOR 2025, ADA 2026, GINA/GOLD 2025, KDIGO, IDSA,
  CDC, OMS, ACOG, NICE, MINSA, IPNA, EAU, ATLS 11.ª, Harrison 22.ª, Nelson 22.ª...).

Verificación
------------
- Las 500 se construyeron y pasaron el verificador de encaje: 0 textos fuera de su recuadro, 0 franjas con hueco,
  XML válido, sin la palabra prohibida, mismo nombre de archivo que el publicado.
- Prueba en la app: las 500 entradas de algoritmos.js cargan su imagen y cada ID existe en su banco.

Cómo instalar
-------------
1. Copiar la carpeta flujogramas/ sobre la del sitio (mismos nombres: se reemplazan).
2. Copiar algoritmos.js sobre el del sitio (solo cambian el título y el texto alternativo de estas 500 entradas).
3. Copiar bancos/traumatologia.json (corrección de clave de TRA-003, ver abajo).
Para revisarlos sin instalar: abrir ver-entrega1.html (tiene buscador).

Corrección de clave propuesta (aplicada en bancos/traumatologia.json)
--------------------------------------------------------------------
- TRA-003 (herida en la palma que impide cerrar el puño): C → D (flexor superficial de los dedos).
  El palmar menor no flexiona los dedos y falta en el 15 % de las personas. La clave oficial publicada fue C;
  el comentario de la pregunta lo indica. Si prefiere conservar la clave oficial, no copie ese archivo.

Precisiones que el flujograma explica (la clave del banco NO cambia)
-------------------------------------------------------------------
- TRA-007: con hueso expuesto y periostio despegado corresponde a Gustilo IIIB (la explicación del banco dice IIIA);
  la conducta (lavado y desbridamiento) es la misma.
- PED-077: una crisis febril de 30 minutos ya es estado epiléptico febril, la forma más grave de la crisis compleja.
- INF-024: fiebre cada 72 h es el patrón cuartano (P. malariae); en Tumbes predomina P. vivax: la gota gruesa define.
- NEF-026: una CPK de 1500 es baja para un aplastamiento con falla renal (suele superar 5000).
- GAS-021: la «hidratación agresiva» hoy es guiada por metas (WATERFALL 2022); en choque se dan bolos.
- INF-017: para clamidia hoy se prefiere doxiciclina (CDC 2021, OMS 2024); la azitromicina queda como alternativa.
- PED-037 y PED-049: la OMS prefiere ampicilina + gentamicina; la ceftriaxona es la alternativa EV.
- NEU-013: el antibiótico en la EPOC exacerbada lo decide sobre todo el esputo purulento (GOLD 2025).
- SP-030: la definición de contacto es de la pandemia; hoy la COVID-19 se maneja como otros virus respiratorios.
- Algunas alternativas se muestran en la tabla con la ortografía corregida (Nebivolol, Kehr, Fascitis,
  Aritenoideo) o abreviadas cuando eran muy largas; el banco no se toca.

Detalle de los 500
------------------
{detalle}

Imágenes usadas (Wikimedia Commons; son de otros pacientes, así se indica bajo cada una)
-------------------------------------------------------------------------------------
{cred}
"""
open(f"{B}/LEEME.txt", "w").write(LEEME)

with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(B):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, B))
print("ok", len(order), "escalas", n_esc, "tríadas", n_tri, "imágenes", n_img, "créditos", len(creditos))
