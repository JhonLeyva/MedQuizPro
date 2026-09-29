import json,re,collections
def detect(N):
    q=json.load(open("parsed.json"))
    voc=collections.Counter()
    for x in q:
        for t in [x["enunciado"],x["comentario"],*x["opciones"].values()]:
            voc.update(w.lower() for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",t))
    out=set()
    for p in N:
        for t in [p["enunciado"],p["explicacion"],*p["opciones"]]:
            ws=t.split()
            for i in range(len(ws)-1):
                a=re.sub(r"^[^\wÁÉÍÓÚÜÑáéíóúüñ]+","",ws[i]); b=re.match(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",ws[i+1])
                if not a or not b or not a[-1].isalpha(): continue
                b=b.group(0); j=(a+b).lower()
                if voc[j]>=2 and (voc[a.lower()]<3 or voc[b.lower()]<3):
                    out.add((a+" "+b, a+b))
    return sorted(out)
if __name__=="__main__":
    for x in detect(json.load(open("nuevos5.json"))): print(x)
