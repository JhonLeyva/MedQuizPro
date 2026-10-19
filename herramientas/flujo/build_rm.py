"""Construye los flujogramas RM. Uso: python3 build_rm.py <salida> <modulo_content> [ID ...]"""
import xml.etree.ElementTree as ET
import os, sys, json, shutil, importlib
import engine7
from engine7 import build7
from c_rm import FRM
out, mod, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
importlib.import_module(mod)
specs = {f["id"]: f for f in FRM}
ids = ids or [f["id"] for f in FRM]
shutil.rmtree(out + "/flujogramas", ignore_errors=True); os.makedirs(out + "/flujogramas")
order = []
for i in ids:
    f = specs[i]
    engine7.AVISOS.clear()
    svg = build7(f)
    assert not engine7.AVISOS, f"{i}: " + "; ".join(engine7.AVISOS)
    assert "RESPUESTA" not in svg.upper(), "palabra prohibida en " + i
    ET.fromstring(svg)
    open(f"{out}/flujogramas/{f['archivo']}.svg", "w").write(svg)
    order.append((i, f["archivo"], f["titulo"], f["tipo"]))
json.dump(order, open(out + "/order.json", "w"), ensure_ascii=False)
print("ok", len(order))
