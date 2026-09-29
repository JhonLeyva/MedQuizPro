import json,re,os,collections
voc=collections.Counter()
W=re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")
for f in os.listdir("zip7/bancos"):
    for p in json.load(open("zip7/bancos/"+f))["preguntas"]:
        for k in ("enunciado","comentario"): voc.update(w.lower() for w in W.findall(p[k]))
        for o in p["opciones"]: voc.update(w.lower() for w in W.findall(o))
for x in json.load(open("parsed.json")):
    voc.update(w.lower() for w in W.findall(x["comentario"]+" "+x["enunciado"]))
N=json.load(open("nuevos7.json"))
J=json.load(open("join7.json")) if os.path.exists("join7.json") else []
seen={a for a,b in J}
for p in N:
    for txt in [p["enunciado"],p["comentario"]]+p["opciones"]:
        toks=re.findall(r"\S+",txt)
        for a,b in zip(toks,toks[1:]):
            a2=re.sub(r"^\W+","",a); b2=re.sub(r"\W+$","",b)
            if not re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",a2 or "-") or not re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",b2 or "-"): continue
            j=(a2+b2).lower()
            if voc[j]>=2 and (voc[a2.lower()]<=3 or voc[b2.lower()]<=3) and a2+" "+b2 not in seen:
                J.append([a2+" "+b2,a2+b2]); seen.add(a2+" "+b2)
json.dump(J,open("join7.json","w"),ensure_ascii=False)
print(len(J))
