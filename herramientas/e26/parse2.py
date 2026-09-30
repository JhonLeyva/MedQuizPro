import re, glob, json
from parse import OPT, LET, join
RESP=re.compile(r"^\s*RESPUESTA\s*[:;.]?\s*([A-E8€6])(?![a-z])")
def lines():
    L=[]
    for p in sorted(glob.glob("txt/p2_*.txt")):
        for l in open(p).read().split("\n"):
            L.append((p,l))
    return L
def junk(l):
    s=l.strip()
    if re.match(r"^PREGUNTA\s*\d+",s): return True
    if re.match(r"^EXAMEN ENAM EXTRAORDINARIO|^Il - 2026|^II - 2026",s): return True
    w=re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]{3,}",s)
    return len(s)<25 and len(w)<=1 and not OPT.match(s) and not RESP.match(s)
def parse():
    Q=[];cur={"q":[],"c":[],"p":[],"key":None,"page":None};state="q"
    for pg,l in lines():
        if state=="q":
            m=RESP.match(l)
            if m:
                k=m.group(1); cur["key"]={"8":"B","€":"C","6":"B"}.get(k,k); state="c"; continue
            if junk(l) and not cur["q"]: continue
            if re.match(r"^\s*PREGUNTA\s*\d+",l.strip()): continue
            if cur["page"] is None and l.strip(): cur["page"]=pg
            cur["q"].append(l)
        elif state=="c":
            m=re.search(r"VILLAPEPA\s*ENAM\s*[:;]?\s*(.*)",l)
            if m: cur["p"].append(m.group(1)); state="p"; continue
            cur["c"].append(l)
        else:
            if re.match(r"^\s*PREGUNTA\s*\d+",l) or re.match(r"^\s*\d{1,3}[.,]\s+[A-ZÁÉÍÓÚ¿]",l):
                Q.append(cur); cur={"q":[],"c":[],"p":[],"key":None,"page":None}; state="q"
                if not re.match(r"^\s*PREGUNTA",l): cur["q"].append(l); cur["page"]=pg
                continue
            cur["p"].append(l)
    if cur["key"]: Q.append(cur)
    out=[]
    for i,c in enumerate(Q,1):
        stem=[];opts={};o=None
        for l in c["q"]:
            if re.match(r"^\s*PREGUNTA\s*\d+\s*$",l): continue
            m=OPT.match(l); exp="ABCDE"[len(opts)] if len(opts)<5 else None
            mm=m and {"8":"B","€":"C","6":"B"}.get(m.group(1),m.group(1))
            if m and exp and mm==exp: o=exp; opts[o]=[m.group(2)]; continue
            if o is None: stem.append(l)
            elif l.strip(): opts[o].append(l)
        com=[l for l in c["c"] if not junk(l) and not re.match(r"^\s*COMENTARIO\s+VILLAMEDIC",l)]
        com=join(com).strip()
        out.append({"src":"p2","n":i,"page":c["page"],"enunciado":join([l for l in stem if not junk(l)]).replace("\n"," "),
            "opciones":{k:join(v).replace("\n"," ") for k,v in opts.items()},"clave":c["key"],"comentario":com,
            "perla":join([l for l in c["p"] if not junk(l)]).replace("\n"," ")})
    return out
if __name__=="__main__":
    import collections
    R=parse(); print(len(R), collections.Counter(len(r["opciones"]) for r in R), collections.Counter(r["clave"] for r in R))
    for r in R:
        if len(r["opciones"])!=4 or len(r["comentario"])<400 or len(r["enunciado"])<40: print(r["n"],r["page"],len(r["opciones"]),len(r["comentario"]),r["enunciado"][:70],"|",list(r["opciones"].items())[-1:])
