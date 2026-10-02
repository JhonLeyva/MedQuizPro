"""Construye la tanda de mejora: flujogramas ya publicados rehechos con imagen real y tríadas.
Contenido en content27*.py (F27) y, para los del bloque ENAM 2026, en content26*.py (F26).
Uso: python3 build27.py <salida> [ID ...]   → <salida>/flujogramas + <salida>/order.json
Sin IDs construye todo F27; con IDs, solo esos (pueden ser de F27 o de F26)."""
import xml.etree.ElementTree as ET
import os, sys, json, shutil, importlib, re
from engine7 import build7
from c26 import F26
from c27 import F27

for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content2[67][a-z]+\.py", f)):
    importlib.import_module(m)
out, ids = sys.argv[1], sys.argv[2:]
js = open("../site/algoritmos.js").read()
publicado = dict(re.findall(r'"([A-Z]+-\d+)":\s*\{[^}]*?imagen:\s*"flujogramas/([^"]+)\.svg"', js))
specs = {}
for f in F27:
    assert f["id"] not in specs, "id repetido: " + f["id"]
    specs[f["id"]] = f
for f in F26:
    specs.setdefault(f["id"], f)
ids = ids or [f["id"] for f in F27]
shutil.rmtree(out + "/flujogramas", ignore_errors=True)
os.makedirs(out + "/flujogramas")
order = []
for i in ids:
    f = specs[i]
    # Se reemplaza el archivo ya publicado: mismo nombre, para que la app lo siga encontrando.
    assert publicado.get(i) == f["archivo"], f"{i}: el nombre no coincide con el publicado ({publicado.get(i)})"
    assert re.fullmatch(r"[a-z0-9-]+", f["archivo"]), "nombre no ASCII: " + f["archivo"]
    svg = build7(f)
    assert "RESPUESTA" not in svg.upper(), "palabra prohibida en " + i
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        raise AssertionError(f"SVG no es XML válido en {i}: {e}")
    open(f"{out}/flujogramas/{f['archivo']}.svg", "w").write(svg)
    order.append((i, f["archivo"], f["titulo"], f["tipo"], bool(f.get("triada"))))
json.dump(order, open(out + "/order.json", "w"), ensure_ascii=False)
print("ok", len(order))
