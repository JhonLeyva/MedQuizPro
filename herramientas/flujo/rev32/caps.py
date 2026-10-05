import sys; sys.path.insert(0, ".")
import json, re, os, importlib, c28
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
E=json.load(open('rev30/entrega3.json')); spec={f["id"]:f for f in c28.F28}
out=[]
def walk(o,i,ctx):
    if isinstance(o,dict):
        tit=o.get("titulo") or o.get("img_titulo") or o.get("ilu_titulo") or ctx
        for k,v in o.items():
            if k in("pie","img_pie","ilu_pie") and isinstance(v,str) and ("img" in o or "ilu" in o or "foto" in o or k!="pie"):
                fotos=[]
                def g(x):
                    if isinstance(x,dict):
                        if "foto" in x: fotos.append(x["foto"])
                        for y in x.values(): g(y)
                    elif isinstance(x,(list,tuple)):
                        for y in x: g(y)
                g(o.get("img") or o.get("ilu"))
                out.append((i,k,v,tit,fotos))
            walk(v,i,tit if isinstance(tit,str) else ctx)
    elif isinstance(o,(list,tuple)):
        for v in o: walk(v,i,ctx)
for i in E: walk(spec[i],i,"")
for x in out: print(json.dumps(x,ensure_ascii=False))
