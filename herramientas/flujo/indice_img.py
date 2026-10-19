"""Índice de imágenes ya usadas (archivo → tamaño y crédito), para reutilizarlas con su crédito exacto.
Uso: python3 indice_img.py [texto]  → escribe img/indice.json y lista las que contienen el texto."""
import importlib, json, os, re, sys
import c28, c26, c27
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content(2[6789]|30)[a-z]+\.py", f)):
    try:
        importlib.import_module(m)
    except Exception as e:
        print("no carga", m, e)
idx = {}


def walk(o, iid):
    if isinstance(o, dict):
        if o.get("foto"):
            idx.setdefault(o["foto"], {"W": o["W"], "H": o["H"], "credito": o.get("credito", ""), "usos": []})
            if o.get("credito") and not idx[o["foto"]]["credito"]:
                idx[o["foto"]]["credito"] = o["credito"]
            idx[o["foto"]]["usos"].append(iid)
        for v in o.values():
            walk(v, iid)
    elif isinstance(o, (list, tuple)):
        for v in o:
            walk(v, iid)


for f in c28.F28 + c26.F26 + c27.F27:
    walk(f, f["id"])
json.dump(idx, open("img/indice.json", "w"), ensure_ascii=False, indent=0)
q = sys.argv[1].lower() if len(sys.argv) > 1 else None
for k, v in sorted(idx.items()):
    if not q or q in k.lower() or q in v["credito"].lower():
        print(f"{k} {v['W']}x{v['H']} | {v['credito']} | {','.join(v['usos'][:3])}")
print(len(idx), "imágenes")
