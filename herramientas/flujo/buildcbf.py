import os, sys, json, shutil, importlib
from engine4 import build4
from ccb import FCB as F8
for m in ["contentcb" + c for c in "abcdefghijklmnopqrst"]:
    if os.path.exists(m + ".py"):
        importlib.import_module(m)
full = "--full" in sys.argv
ex = set(open("existing_namescb.txt").read().split())
for d in ():
    ex |= set(os.listdir(d)) | {f + ".svg" for f in os.listdir(d)}
nuevos = [p["id"] for p in json.load(open("../cb/nuevoscb.json"))]
specs = {}
for f in F8:
    assert f["id"] not in specs, "id repetido: " + f["id"]
    specs[f["id"]] = f
extra = set(specs) - set(nuevos)
assert not extra, extra
ids = [i for i in nuevos if i in specs]
if full:
    assert len(ids) == 393, (len(ids), sorted(set(nuevos) - set(specs)))
shutil.rmtree("outcb", ignore_errors=True); os.makedirs("outcb/flujogramas")
col = [specs[i]["archivo"] for i in ids if specs[i]["archivo"] + ".svg" in ex]
assert not col, "nombres repetidos: " + ", ".join(col)
names, order = set(), []
for i in ids:
    f = specs[i]
    n = f["archivo"] + ".svg"
    assert __import__("re").fullmatch(r"[a-z0-9-]+\.svg", n), "nombre no ASCII: " + n
    assert n not in ex and n not in names, "nombre repetido: " + n
    names.add(n)
    svg = build4(f)
    assert "RESPUESTA" not in svg.upper(), "palabra prohibida en " + i
    for k in ("tema", "caso"):
        assert f[k]["title"], "falta " + k + " en " + i
    open("outcb/flujogramas/" + n, "w").write(svg)
    order.append((i, f["archivo"], f["titulo"], f.get("tipo", "arbol")))
json.dump(order, open("outcb/order.json", "w"), ensure_ascii=False)
from collections import Counter
print("ok", len(order), dict(Counter(o[3] for o in order)))
