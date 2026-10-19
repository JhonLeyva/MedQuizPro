"""Construye los flujogramas RM. Uso: python3 build_rm.py <salida> <modulo_content> [ID ...]"""
import xml.etree.ElementTree as ET
import os, sys, json, shutil, importlib
import engine7
from engine7 import build7
from c_rm import FRM
out, mod, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
for _m in mod.split(","):
    try:
        importlib.import_module(_m)
    except AssertionError as e:
        print("ERROR de ficha:", _m, e); sys.exit(1)
specs = {f["id"]: f for f in FRM}
ids = ids or [f["id"] for f in FRM]
shutil.rmtree(out + "/flujogramas", ignore_errors=True); os.makedirs(out + "/flujogramas")
order, errores = [], []
for i in ids:
    f = specs[i]
    engine7.AVISOS.clear()
    try:
        svg = build7(f)
        assert not engine7.AVISOS, f"{i}: " + "; ".join(engine7.AVISOS)
        assert "RESPUESTA" not in svg.upper(), "palabra prohibida en " + i
        ET.fromstring(svg)
    except Exception as e:
        import traceback
        print("FALLA", i, f["tipo"], type(e).__name__, str(e)[:200]); errores.append(i); continue
    open(f"{out}/flujogramas/{f['archivo']}.svg", "w").write(svg)
    order.append((i, f["archivo"], f["titulo"], f["tipo"]))
json.dump(order, open(out + "/order.json", "w"), ensure_ascii=False)
print("ok", len(order), "errores", errores)
