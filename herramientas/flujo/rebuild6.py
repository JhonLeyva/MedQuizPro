import os, importlib, shutil, re
from engine4 import build4
from c6 import F6
for m in ["content6" + c for c in "abcdefghijklmnop"]:
    if os.path.exists(m + ".py"): importlib.import_module(m)
shutil.rmtree("out6fix", ignore_errors=True); os.makedirs("out6fix/flujogramas")
for f in F6:
    svg = build4(f)
    assert "RESPUESTA" not in svg.upper(), f["id"]
    open("out6fix/flujogramas/" + f["archivo"] + ".svg", "w").write(svg)
print(len(F6))
