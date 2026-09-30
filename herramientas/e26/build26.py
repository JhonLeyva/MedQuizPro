import json,os,re,shutil,collections
from dupx import DUP
BASE="/home/user/MedQuizPro/herramientas/site/bancos"
ARCH={"CB":"ciencias_basicas","CA":"cardiologia","CI":"cirugia","EN":"endocrinologia","GA":"gastroenterologia","GI":"ginecologia","HE":"hematologia",
"IN":"infectologia","NE":"nefrologia","NR":"neumologia","NL":"neurologia","OF":"oftalmo_orl","PE":"pediatria","PS":"psiquiatria","RE":"reumatologia","SP":"salud_publica","TR":"traumatologia"}
MAT={"AN":"Anatomía","HI":"Histología y Biología Celular","EM":"Embriología","FI":"Fisiología","BQ":"Bioquímica y Genética","MI":"Microbiología e Inmunología","FA":"Farmacología básica y autonómica","PA":"Patología general","EP":"Epidemiología y Bioestadística"}
ORIG={"PDF1":"ENAM Extraordinario 2026 · pregunta oficial","PDF2":"ENAM Extraordinario II 2026 · pregunta oficial"}
def tidy(s):
    for a,b in [("Pa02","PaO₂"),("Sat02","SatO₂"),("Sato2","SatO₂"),("SatO2","SatO₂"),("Fi02","FiO₂"),("PaO2","PaO₂"),("(«72h)","(≤72 h)"),("grados | a Y","grados I a V"),("Hinchey |","Hinchey I"),
                ("fase |","fase I"),("clase |","clase I"),("tipo |","tipo I"),("categoría |-","categoría I-"),("), |-2",", I-2"),("<« O, 7","< 0,7"),("mEq//L","mEq/L"),
                ("FC 15 x', FR 28 x,","FC 115 x', FR 28 x',"),("PA 380/50","PA 80/50"),("Anti- HBs","Anti-HBs"),("puestos |l.","puestos I-1.")]:
        s=s.replace(a,b)
    s=re.sub(r" \|-(\d)",r" I-\1",s)
    s=re.sub(r"«(?=[a-záéíóú])(?![^«»]{0,40}»)","",s)
    s=s.replace("Mallampati |","Mallampati I").replace("consumo de 02","consumo de O₂")
    s=s.replace("x”","x'").replace("x´","x'").replace("X'","x'").replace(" ,",",").replace(" .",".")
    s=re.sub(r"\s+"," ",s).strip()
    return s
C=json.load(open('cand.json'))
ok=[c for c in C if 'excluida' not in c and (c['src'],c['n']) not in DUP]
out={}; nuevos=[]
for c in ok:
    code,_,mat=c['esp'].partition(":")
    a=ARCH[code]
    if a not in out: out[a]=json.load(open(f"{BASE}/{a}.json"))
    d=out[a]; pref=re.match(r"([A-Z]+)-",d["preguntas"][0]["id"]).group(1)
    last=max(int(p["id"].split("-")[1]) for p in d["preguntas"])
    nid=f"{pref}-{last+1:03d}"
    ops=[tidy(o) for o in c['opciones']]; com=tidy(c['comentario']); enu=tidy(c['enunciado'])
    p={"id":nid,"especialidad":d["especialidad"]}
    if a=="ciencias_basicas": p["categoria"]=MAT[mat]
    p.update({"examen_origen":ORIG[c['src']],"enunciado":enu,"opciones":ops,"correcta":"ABCD".index(c['clave']),
       "clave_correcta":c['clave'],"explicacion":com,"comentario":com,"tema":c['tema'],"año":2026})
    d["preguntas"].append(p); nuevos.append({"pdf":c['src'],"n":c['n'],"archivo":a,**p})
shutil.rmtree("zip26",ignore_errors=True); os.makedirs("zip26/bancos")
for a,d in out.items():
    open(f"zip26/bancos/{a}.json","w",encoding="utf-8").write(json.dumps(d,ensure_ascii=False,indent=2)+"\n")
json.dump(nuevos,open("nuevos26.json","w"),ensure_ascii=False,indent=1)
tot=sum(len(json.load(open(f"{BASE}/{f}"))["preguntas"]) for f in os.listdir(BASE) if f[:-5] not in out)+sum(len(d["preguntas"]) for d in out.values())
print(len(nuevos),collections.Counter(n['archivo'] for n in nuevos),"total",tot)
