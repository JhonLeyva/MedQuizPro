import sys; sys.path.insert(0, ".")
import json, re, os, importlib, c28
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
E=json.load(open('rev30/entrega3.json')); spec={f["id"]:f for f in c28.F28}
def img(o):
    if callable(o): return True
    if isinstance(o,dict): return "foto" in o or "ilu" in o or any(img(v) for v in o.values())
    if isinstance(o,(list,tuple)): return any(img(v) for v in o)
    return False
def nombre(o):
    if isinstance(o,dict):
        for k in ("titulo","nombre","t"):
            if isinstance(o.get(k),str): return o[k]
    if isinstance(o,(list,tuple)):
        for v in o:
            if isinstance(v,str) and v: return v
    return "?"
res=[]
def walk(o,i,path):
    if isinstance(o,dict):
        for k,v in o.items(): walk(v,i,path+"."+str(k))
    elif isinstance(o,(list,tuple)):
        if len(o)>=2 and all(isinstance(v,(list,tuple,dict)) for v in o):
            f=[img(v) for v in o]
            if any(f) and not all(f):
                res.append((i, spec[i]["tipo"], path, [nombre(v)+("" if x else " [SIN]") for v,x in zip(o,f)]))
        for v in o: walk(v,i,path)
for i in E: walk(spec[i].get("d") or {}, i, "d"); 
for r in res: print(r)
print(len(res))
print("=== cuadriculas / tarjetas / grados sin ninguna imagen")
for i in E:
    f=spec[i]
    if f["tipo"] in ("cuadricula",) :
        cs=f["d"]["celdas"]; n=sum(img(c) for c in cs)
        if n==0: print(i, [nombre(c) for c in cs])
