import json,os,sys,re
pat=re.compile(sys.argv[1],re.I)
for f in sorted(os.listdir("site/bancos")):
    for p in json.load(open("site/bancos/"+f))["preguntas"]:
        ops=p["opciones"]; c=p.get("correcta")
        cor=ops[c] if isinstance(c,int) and isinstance(ops,list) else str(p.get("clave_correcta",""))
        txt=p.get("tema","")+" | "+cor+("" if "-t" in sys.argv else " | "+p["enunciado"])
        if pat.search(txt): print(p["id"],"[",p.get("tema",""),"] ->",cor,"||",p["enunciado"][:150])
