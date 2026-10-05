import sys; sys.path.insert(0, ".")
import json, re, os, importlib, c28
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
E=json.load(open('rev30/entrega3.json')); spec={f["id"]:f for f in c28.F28}
a,b=int(sys.argv[1]),int(sys.argv[2])
for k,i in enumerate(E[a:b],a):
    f=spec[i]; esc=(f.get("escala") or {}).get("nombre","-")
    d=f.get("d") or {}
    extra = d.get("escala") or d.get("rotulo","")
    print(f"{k:3} {i} [{f['tipo']}] ESC={esc} | {f['titulo'][:150]} | D={str(extra)[:60]} | F={f['fuente'][:110]}")
