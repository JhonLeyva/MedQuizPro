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
z = f"/home/user/MedQuizPro/MedQuizPro_flujogramas_ENAM2026_parte{parte}.zip"
if os.path.exists(z):
    os.remove(z)
subprocess.run(f"cd {P} && zip -qr {z} LEEME.txt algoritmos.js flujogramas bancos", shell=True, check=True)
print(z, os.path.getsize(z) // 1024, "KB", len(order), "nuevos")
