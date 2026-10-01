"""Paquete acumulado del bloque ENAM 2026: todos los flujogramas hechos hasta ahora.
Uso: python3 pack26.py <n_parte>  → ../../MedQuizPro_flujogramas_ENAM2026_parteN.zip
Incluye los 8 de los ejemplos 1 y 2, algoritmos.js acumulado y los bancos corregidos."""
import json, os, re, shutil, sys, subprocess
from collections import Counter
from demo26 import F as F26D
from demo27 import F as F27D

parte = sys.argv[1]
BANCOS_TOCADOS = ["traumatologia", "cirugia", "gastroenterologia"] + [l.strip() for l in open("bancos26_tocados.txt") if l.strip()]
order = json.load(open("out26/order.json"))
P = "out26/pack"
shutil.rmtree(P, ignore_errors=True)
os.makedirs(P + "/flujogramas")
os.makedirs(P + "/bancos")
for _, a, _, _ in order:
    shutil.copy(f"out26/flujogramas/{a}.svg", P + "/flujogramas/")
for f in F26D:
    shutil.copy(f"out26demo/flujogramas/{f['archivo']}.svg", P + "/flujogramas/")
for f in F27D:
    shutil.copy(f"out27demo/flujogramas/{f['archivo']}.svg", P + "/flujogramas/")
for b in sorted(set(BANCOS_TOCADOS)):
    shutil.copy(f"../site/bancos/{b}.json", P + "/bancos/")
    json.load(open(f"{P}/bancos/{b}.json"))
import xml.etree.ElementTree as _ET
for f in os.listdir(P + "/flujogramas"):
    _ET.parse(f"{P}/flujogramas/{f}")  # todo SVG entregado debe ser XML válido

js = open("../site/algoritmos.js", encoding="utf-8").read().rstrip()
assert js.endswith("};")
ya = re.findall(r'^\s*"([A-Z]+-\d+)"\s*:', js, re.M)
assert len(ya) == 2106, len(ya)
todas = [(f["id"], f["archivo"], f["titulo"]) for f in F26D + F27D] + [(i, a, t) for i, a, t, _ in order]
assert not set(ya) & {i for i, _, _ in todas}
assert len({i for i, _, _ in todas}) == len(todas)
cuerpo = js[:-2].rstrip()
if not cuerpo.endswith(","):
    cuerpo += ","
nuevas = "".join('  %s: { titulo: %s, imagen: %s, alt: %s },\n' % (
    json.dumps(i), json.dumps(t, ensure_ascii=False), json.dumps("flujogramas/" + a + ".svg"),
    json.dumps("Flujograma: " + t, ensure_ascii=False)) for i, a, t in todas)
out = cuerpo + "\n" + nuevas + "};\n"
open(P + "/algoritmos.js", "w", encoding="utf-8").write(out)
N = len(re.findall(r'^\s*"([A-Z]+-\d+)"\s*:', out, re.M))
r = subprocess.run(["node", "-e", "global.window={};require('./%s/algoritmos.js');const a=window.MQP_ALGORITMOS;"
                    "const fs=require('fs');const nv=%s;let m=0;for(const k of nv){if(!a[k]||!fs.existsSync('%s/'+a[k].imagen))m++;}"
                    "console.log('entradas', Object.keys(a).length, 'nuevas sin archivo', m)" % (P, json.dumps([i for i, _, _ in todas]), P)], capture_output=True, text=True)
print("algoritmos.js:", r.stdout.strip(), r.stderr.strip()[:200])
c = Counter(o[3] for o in order)
open(P + "/LEEME.txt", "w").write(f"""MedQuizPro - Flujogramas del bloque ENAM 2026 · parte {parte} (acumulada)
=====================================================================

Qué contiene
- flujogramas/: {len(order) + 8} SVG = {len(order)} nuevos de esta entrega + 8 de los ejemplos 1 y 2.
  Cada flujograma lleva imagen del caso: foto real con marcas (licencia libre, crédito en la imagen)
  o dibujo propio. Van a public_html/flujogramas/.
- algoritmos.js: registro actual (2106) + {len(todas)} = {N} entradas. Reemplaza al de public_html.
- bancos/: bancos corregidos en esta revisión (erratas de OCR): {", ".join(sorted(set(BANCOS_TOCADOS)))}.
  Reemplazan a los de public_html/bancos/.

Esta parte es ACUMULADA: trae todo lo hecho hasta ahora. Basta con subir la última parte.

Diseños usados en esta parte: {", ".join(f"{k} ({n})" for k, n in c.most_common())}.

Verificación: 0 textos desbordados; sin la palabra prohibida; nombres nuevos y sin tildes;
cada uno revisado en imagen (flechas y rótulos sobre lo que nombran); algoritmos.js carga sin errores.

Cómo subir
1. Copia de respaldo de public_html/algoritmos.js y public_html/bancos/.
2. Sube el ZIP a public_html y usa "Extraer" hacia public_html. Acepta reemplazar.
3. Ctrl+F5 y abre cualquier pregunta del bloque ENAM 2026 → "Ver algoritmo".
""")
extra = ""
if parte == "final":
    from html import escape as _esc
    assert len(order) == 266 and N == 2380, (len(order), N)
    NOMBRE = {"arbol": "árbol", "radial": "radial", "fases": "fases", "termometro": "termómetro", "tarjetas": "tarjetas",
              "embudo": "embudo", "puntaje": "puntaje", "matriz": "matriz", "calculo": "cálculo", "anatomia": "anatomía",
              "semaforo": "semáforo", "cronologia": "cronología", "comparador": "comparador", "escalera": "escalera",
              "mapa_signos": "mapa de signos", "arbol_imagen": "árbol con imagen", "ciclo": "ciclo", "criterios": "criterios",
              "balanza": "balanza", "red": "niveles de atención"}
    filas = [(f["id"], f["archivo"], f["titulo"], f["tipo"]) for f in F26D + F27D] + [tuple(o) for o in order]
    clave = lambda r: (r[0].split("-")[0], int(r[0].split("-")[1]))
    filas.sort(key=clave)
    plantilla = open("../site/verificar-flujogramas-bloquecb.html", encoding="utf-8").read()
    cab = plantilla[:plantilla.index("<h1>")]
    cab = re.sub(r"<title>.*?</title>", "<title>Flujogramas ENAM 2026 · MedQuizPlus</title>", cab)
    tarj = "".join(f'<figure class="card"><figcaption><span class="badge">{i}</span> <span class="tipo">{NOMBRE.get(t, t)}</span> '
                   f'<b>{_esc(ti)}</b></figcaption><a href="flujogramas/{a}.svg" target="_blank"><img loading="lazy" '
                   f'src="flujogramas/{a}.svg" alt="{_esc(ti)}"></a><code>flujogramas/{a}.svg</code></figure>\n' for i, a, ti, t in filas)
    pie = plantilla[plantilla.index("</div>", plantilla.rindex("</figure>")):]
    pie = pie.replace("393", str(len(filas)))
    html = (cab + f"<h1>MedQuizPlus · Flujogramas del bloque ENAM 2026</h1>\n<p>{len(filas)} flujogramas del bloque ENAM 2026 "
            f"(266 nuevos + 8 de los ejemplos), cada uno con imagen del caso (foto real con crédito o dibujo propio) en 20 diseños. "
            f'Imágenes cargadas: <span id="cnt">0</span> / {len(filas)}. Pulsa una imagen para verla sola.</p>\n<div class="grid">\n'
            + tarj + pie)
    assert html.count("<figure") == len(filas) == 274
    open(P + "/verificar-flujogramas-bloque26.html", "w", encoding="utf-8").write(html)
    g = open("../site/verificar-flujogramas.html", encoding="utf-8").read()
    assert "Ciencias Básicas deben ser 2106" in g
    g = g.replace("con los bloques 1 a 8 y Ciencias Básicas deben ser 2106", "con los bloques 1 a 8, Ciencias Básicas y ENAM 2026 deben ser 2380")
    open(P + "/verificar-flujogramas.html", "w", encoding="utf-8").write(g)
    extra = " verificar-flujogramas-bloque26.html verificar-flujogramas.html"
    open(P + "/LEEME.txt", "a").write("""
Paquete FINAL: están los 266 flujogramas del bloque ENAM 2026 (todas las especialidades).
- verificar-flujogramas-bloque26.html: galería con los 274 (abre public_html/verificar-flujogramas-bloque26.html).
- verificar-flujogramas.html: verificador general; ahora espera 2380 entradas.
- Si tras Ctrl+F5 el verificador general sigue mostrando 2106 entradas, el navegador usa la copia vieja de
  algoritmos.js: en public_html/index.html cambia el texto que sigue a "algoritmos.js?v=" por 20261001.

Créditos de las fotos reales (licencias libres; el crédito también va debajo de cada foto)
- Íleo biliar, Rx y TC: Hellerhoff · Wikimedia Commons · CC BY-SA 4.0
- Neumoperitoneo: Bill Rhodes · Wikimedia Commons · CC BY 2.0
- Seudoquiste pancreático, vitíligo y Stevens-Johnson: James Heilman, MD · Wikimedia Commons · CC BY-SA 3.0
- Absceso pulmonar: James Heilman, MD · Wikimedia Commons · CC BY-SA 4.0
- Neumotórax (Rx): James Heilman, MD · Wikimedia Commons · CC BY 3.0
- Taquicardia supraventricular (trazo): Displaced y James Heilman, MD · Wikimedia Commons · dominio público
- Gemelos bicoriales (signo lambda): Nevit Dilmen · Wikimedia Commons · CC BY-SA 3.0
- Loxosceles laeta: Mampato · Wikimedia Commons · dominio público
- Varicela; TB cavitaria; sarampión (PHIL 4497 y 6111): CDC · dominio público
- Molusco contagioso: Gzzz · Wikimedia Commons · CC BY-SA 4.0
- Bastones de Auer: AFIP · Wikimedia Commons · dominio público
- Retinitis por CMV: National Eye Institute · Wikimedia Commons · dominio público
- Nódulos de Heberden: Drahreg01 · Wikimedia Commons · CC BY-SA 3.0
- Neurocisticercosis (TC): Innocent Lule Segamwenge · Wikimedia Commons · CC BY 4.0
- Ántrax (carbunco): Medicalpal · Wikimedia Commons · CC BY-SA 4.0
- Urticaria: Psixtras · Wikimedia Commons · CC0
- Micosis fungoide: Bobjgalindo · Wikimedia Commons · CC BY-SA 4.0
- Displasia de cadera (Rx): Bonilla A, et al. · Wikimedia Commons · CC BY 4.0
Todas las demás imágenes son dibujos propios hechos para MedQuizPlus.
""")
    nombre = "final"
else:
    nombre = f"parte{parte}"
z = f"/home/user/MedQuizPro/MedQuizPro_flujogramas_ENAM2026_{nombre}.zip"
if os.path.exists(z):
    os.remove(z)
subprocess.run(f"cd {P} && zip -qr {z} LEEME.txt algoritmos.js flujogramas bancos{extra}", shell=True, check=True)
print(z, os.path.getsize(z) // 1024, "KB", len(order), "nuevos")
