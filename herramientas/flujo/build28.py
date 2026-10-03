"""Construye la revisión completa (F28). Uso: python3 build28.py <salida> [ID ...] → <salida>/flujogramas + order.json
Comprueba: mismo nombre que el publicado, XML válido, sin la palabra prohibida, franja sin hueco,
notas de la franja con título + detalle."""
import xml.etree.ElementTree as ET
import os, sys, json, shutil, importlib, re
import engine7
from engine7 import build7
from c28 import F28

for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content2[89][a-z]+\.py", f)):
    importlib.import_module(m)
out, ids = sys.argv[1], sys.argv[2:]
specs = {}
for f in F28:
    assert f["id"] not in specs, "id repetido: " + f["id"]
    specs[f["id"]] = f
ids = ids or [f["id"] for f in F28]
shutil.rmtree(out + "/flujogramas", ignore_errors=True)
os.makedirs(out + "/flujogramas")
order = []
for i in ids:
    f = specs[i]
    if f.get("banda"):
        assert all(isinstance(n, (tuple, list)) for n in f["banda"]["notas"]), i + ": notas de la franja sin título"
    engine7.AVISOS.clear()
    svg = build7(f)
    assert not engine7.AVISOS, f"{i}: " + "; ".join(engine7.AVISOS)
    assert "RESPUESTA" not in svg.upper(), "palabra prohibida en " + i
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        raise AssertionError(f"SVG no es XML válido en {i}: {e}")
    open(f"{out}/flujogramas/{f['archivo']}.svg", "w").write(svg)
    order.append((i, f["archivo"], f["titulo"], f["tipo"], bool(f.get("triada")), bool(f.get("escala")), bool(f.get("banda"))))
json.dump(order, open(out + "/order.json", "w"), ensure_ascii=False)
print("ok", len(order))
