import json,os,re,sys,importlib
exec(open("common7.py").read())
used=set()
for m in ["sel5","sel6","sel7"]:
    mod=importlib.import_module(m); used|={t[0] for t in mod.SEL}|set(getattr(mod,"EXC",{}))
pool=[p["n"] for p in json.load(open("pool7.json")) if p["n"] not in used]
STOP=set("de la el en los las del con por para una un que se su al es y o a e u lo le más cual cuál qué que como años año paciente presenta hace desde sin mujer varón niño".split())
W=re.compile(r"[a-záéíóúüñ0-9]+")
def toks(s): return {w for w in W.findall(s.lower()) if w not in STOP and len(w)>2}
bank=[]
for f in sorted(os.listdir("site/bancos")):
    for p in json.load(open("site/bancos/"+f))["preguntas"]:
        ops=p["opciones"]; c=p.get("correcta")
        cor=ops[c] if isinstance(c,int) and isinstance(ops,list) else str(p.get("clave_correcta",""))
        bank.append((p["id"],p.get("tema",""),cor,toks(p["enunciado"]+" "+cor),toks(p["enunciado"])))
def norm(s): return re.sub(r'[^a-z0-9áéíóúüñ]+',' ',s.lower()).strip()
def sim(a,b): return len(a&b)/max(1,len(a|b))
json.dump(pool,open("pool8.json","w"))
i0,i1=int(sys.argv[1]),int(sys.argv[2])
for n in pool[i0:i1]:
    x=q[n]; e=clean(x["enunciado"])
    hl="".join(x["hl"]) or "-"
    cor=" / ".join(x["opciones"].get(k,"") for k in x["hl"])
    t=toks(e+" "+cor)
    best=sorted(bank,key=lambda b:-sim(t,b[3]))[:2]
    print(f"### {n} hl={hl} verif={x['verif']}")
    print(e)
    for k in "ABCDE": print(f"  {k}) {clean(x['opciones'].get(k,''))}")
    print("  COM:",clean(x["comentario"])[:420])
    for b in best: print(f"  ~{sim(t,b[3]):.2f} {b[0]} [{b[1]}] -> {b[2][:70]}")
    for k in "ABCDE":
        a=norm(clean(x["opciones"].get(k,"")))
        if len(a)<4 or (k=="E" and "E" not in x["hl"]): continue
        hits=[b for b in bank if norm(b[2])==a or (len(a)>8 and (a in norm(b[1]) ))]
        for b in hits[:3]: print(f"  ={k} {b[0]} [{b[1]}] -> {b[2][:60]}")
