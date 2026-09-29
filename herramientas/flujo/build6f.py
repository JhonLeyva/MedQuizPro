import os, sys, json, shutil, importlib
from engine4 import build4
from c6 import F6
for m in ["content6" + c for c in "abcdefghijklmnop"]:
    if os.path.exists(m + ".py"):
        importlib.import_module(m)
full = "--full" in sys.argv
ex = set(open("existing_names.txt").read().split())
for d in ("out/flujogramas", "out3/flujogramas", "out4/flujogramas", "out5/flujogramas"):
    ex |= set(os.listdir(d)) | {f + ".svg" for f in os.listdir(d)}
nuevos = [p["id"] for p in json.load(open("../nuevos6.json"))]
specs = {}
for f in F6:
    assert f["id"] not in specs, "id repetido: " + f["id"]
    specs[f["id"]] = f
extra = set(specs) - set(nuevos)
assert not extra, extra
ids = [i for i in nuevos if i in specs]
if full:
    assert len(ids) == 500, (len(ids), sorted(set(nuevos) - set(specs)))
shutil.rmtree("out6", ignore_errors=True); os.makedirs("out6/flujogramas")
col = [specs[i]["archivo"] for i in ids if specs[i]["archivo"] + ".svg" in ex]
assert not col, "nombres repetidos: " + ", ".join(col)
names, order = set(), []
for i in ids:
    f = specs[i]
    n = f["archivo"] + ".svg"
    assert __import__("re").fullmatch(r"[a-z0-9-]+\.svg", n), "nombre no ASCII: " + n
    assert n not in ex and n not in names, "nombre repetido: " + n
    names.add(n)
    open("out6/flujogramas/" + n, "w").write(build4(f))
    order.append((i, f["archivo"], f["titulo"], f.get("tipo", "arbol")))
json.dump(order, open("out6/order.json", "w"), ensure_ascii=False)
from collections import Counter
print("ok", len(order), dict(Counter(o[3] for o in order)))
