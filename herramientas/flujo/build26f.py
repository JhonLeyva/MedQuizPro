"""Construye los flujogramas del bloque ENAM 2026 (contenido en content26*.py).
Uso: python3 build26f.py [--full]   → out26/flujogramas + out26/order.json"""
import os, sys, json, shutil, importlib, re
from collections import Counter
from engine7 import build7
from c26 import F26

for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content26[a-z]\.py", f)):
    importlib.import_module(m)
full = "--full" in sys.argv
ex = set(open("existing_names_todos.txt").read().split())
ex |= {l.split('"flujogramas/')[1].split('"')[0] for l in open("../site/algoritmos.js") if '"flujogramas/' in l}
for dd in ("out26demo/flujogramas", "out27demo/flujogramas"):
    ex |= set(os.listdir(dd))
HECHOS = {"CIR-133", "CIR-158", "CIR-150", "GIN-274", "CIR-136", "CAR-079", "PED-247", "TRA-057"}
nuevos = [p["id"] for p in json.load(open("../e26/nuevos26.json"))]
specs = {}
for f in F26:
    assert f["id"] not in specs, "id repetido: " + f["id"]
    assert f["id"] not in HECHOS, "ya hecho: " + f["id"]
    specs[f["id"]] = f
extra = set(specs) - set(nuevos)
assert not extra, extra
ids = [i for i in nuevos if i in specs]
if full:
    falta = sorted(set(nuevos) - set(specs) - HECHOS)
    assert not falta, (len(falta), falta)
shutil.rmtree("out26/flujogramas", ignore_errors=True)
os.makedirs("out26/flujogramas")
names, order = set(), []
for i in ids:
    f = specs[i]
    n = f["archivo"] + ".svg"
    assert re.fullmatch(r"[a-z0-9-]+\.svg", n), "nombre no ASCII: " + n
    assert n not in ex and n not in names, "nombre repetido: " + n
    names.add(n)
    svg = build7(f)
    assert "RESPUESTA" not in svg.upper(), "palabra prohibida en " + i
    assert f["tema"]["title"] and f["caso"]["title"], "falta tema/caso en " + i
    tiene_img = f["tipo"] in {"calculo", "anatomia", "semaforo", "cronologia", "comparador", "escalera",
                              "mapa_signos", "arbol_imagen", "ciclo", "criterios", "balanza", "red"} or f.get("banda")
    assert tiene_img, "sin imagen: " + i
    open("out26/flujogramas/" + n, "w").write(svg)
    order.append((i, f["archivo"], f["titulo"], f["tipo"]))
json.dump(order, open("out26/order.json", "w"), ensure_ascii=False)
print("ok", len(order), dict(Counter(o[3] for o in order)))
