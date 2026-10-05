import sys; sys.path.insert(0, ".")
import json, re, os, importlib, collections, c28
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
E=json.load(open('rev30/entrega3.json')); spec={f["id"]:f for f in c28.F28}
pies=collections.Counter(); otros=[]
def walk(o, i, key=""):
    if isinstance(o,dict):
        for k,v in o.items():
            if isinstance(v,str) and k.endswith("pie"): pies[v]+=1
            walk(v,i,k)
    elif isinstance(o,(list,tuple)):
        for v in o: walk(v,i,key)
    elif isinstance(o,str):
        if re.search(r"otr[oa]s? (paciente|persona|niñ|mujer|bebé|varón|gestante|lactante|caso)|no es de un paciente|de enseñanza\.$|^Esquema\.?$", o, re.I) and key!="credito":
            otros.append((i,key,o))
for i in E: walk(spec[i], i)
print(len(pies)); 
for p,n in pies.most_common(): print(n, repr(p))
print("----", len(otros))
for x in otros: print(x)
