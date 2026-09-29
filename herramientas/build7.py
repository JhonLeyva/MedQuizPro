import json,re,os,shutil,collections
exec(open("common7.py").read())
from sel7 import SEL,COM,OPT,ENU
def fin(s):
    s=re.sub(r"\s*\((?:PACIENTE ROBOT|Paciente Robot|paciente robot)\)","",s)
    s=re.sub(r"\s*\(Nota importante[^)]*\)?\s*$","",s)
    return s.strip()
POST=[("la a lternativa","la alternativa"),("la 2 agudeza","la agudeza"),("T 2 37.5","T 37.5"),("hace 1 semana parto","hace 1 semana tuvo un parto"),("g eneral","general"),("2 ml/k g","2 mL/kg"),("6 a 8 x dia","6 a 8 por día"),("ces área","cesárea"),("s alud","salud"),("ad iposo","adiposo"),("Cuá l es","Cuál es"),("(mayor) 40 gr alcohol/día","más de 40 g de alcohol al día"),
("20 hrs de","20 horas de"),("redefi nir","redefinir"),("genera r inflamación","generar inflamación"),("má s tardía","más tardía"),("insuficiencia r espiratoria","insuficiencia respiratoria"),
("indicado r de","indicador de"),(" gr de azúcar"," g de glucosa"),("iz quierda","izquierda"),("esperar ía","esperaría"),("on das U","ondas U"),("de l gonococo","del gonococo"),
("tr ata de","trata de"),("in icial","inicial"),("t órax","tórax"),("alt ura","altura"),("pa ra","para"),("diagnósti co","diagnóstico"),("de l paciente","del paciente"),
("ma tinal","matinal"),("enferme dad","enfermedad"),("a l os","a los"),("p rolongarse","prolongarse"),("otro s diagnósticos","otros diagnósticos"),
("V2 -(mayor) V6","V2 a V6"),("(mayor) 40 mg/m2/h","> 40 mg/m²/h"),("(mayor) 200mg/dl","> 200 mg/dL"),("(menor) 2","< 2"),("mlU/L","mUI/L"),("( -)","(-)"),("( -4)","(-4)"),("COI","CO₂"),(" ug"," µg"),("antibioticoterap ia","antibioticoterapia"),("diaforeis","diaforesis"),
("diluye. ______","diluye ______"),("______ ______","______"),("flexo ex tensión","flexoextensión"),("frecuencia cardíaca (Alternativa A)","frecuencia cardíaca (alternativa B)")]
JOIN=json.load(open("join7.json"))
JOIN=[(a,b.replace("Carcinoembrionario","Antígeno carcinoembrionario").replace("postprandiales","posprandiales")) for a,b in JOIN]
def post7(s):
    for a,b in JOIN: s=re.sub(r"(?<![\wÁÉÍÓÚÜÑáéíóúüñ])"+re.escape(a)+r"(?![\wÁÉÍÓÚÜÑáéíóúüñ])",b,s)
    for a,b in POST: s=s.replace(a,b)
    s=re.sub(r"\s*(?:…|\.{2,})[….]*\s*"," ______ ",s)
    s=re.sub(r" ______ ([:.,?])",r" ______\1",s)
    s=re.sub(r"\s+"," ",s).strip()
    for a,b in POST: s=s.replace(a,b)
    return s
def _base(a):
    return "zip6/bancos/"+a+".json"
out={}; nuevos=[]; PREF={}
for n,arch,tema,letra in SEL:
    if arch not in out:
        out[arch]=json.load(open(_base(arch)))
        PREF[arch]=re.match(r"([A-Z]+)-",out[arch]["preguntas"][0]["id"]).group(1)
    d=out[arch]; x=q[n]
    last=max(int(p["id"].split("-")[1]) for p in d["preguntas"])
    nid=f"{PREF[arch]}-{last+1:03d}"
    anio=year_of(n)
    ops=[clean(OPT.get(n,{}).get(k) or x["opciones"][k]) for k in "ABCDE"]
    com=COM[n] if n in COM else fin(strip_resp(clean(x["comentario"])))
    enu=ENU[n] if n in ENU else clean(strip_src(x["enunciado"]))
    enu=post7(enu); ops=[post7(o) for o in ops]; com=re.sub(r"(?<=[a-z]) ______ (?=[a-z])","... ",post7(com)) if n not in COM else com
    p={"id":nid,"especialidad":d["especialidad"],"examen_origen":f"ENAM {anio} · pregunta oficial",
       "enunciado":enu,"opciones":ops,"correcta":"ABCDE".index(letra),
       "clave_correcta":letra,"explicacion":com,"comentario":com,"tema":tema,"año":anio}
    d["preguntas"].append(p); nuevos.append((n,arch,p))
print(len(SEL),len(set(t[0] for t in SEL)))
shutil.rmtree("zip7",ignore_errors=True); os.makedirs("zip7/bancos")
for f in os.listdir("zip6/bancos"):
    a=f[:-5]
    d=out.get(a) or json.load(open("zip6/bancos/"+f))
    json.dump(d,open(f"zip7/bancos/{a}.json","w"),ensure_ascii=False,indent=2)
json.dump([{"pdf_pregunta":n,"archivo":a,**p} for n,a,p in nuevos],open("nuevos7.json","w"),ensure_ascii=False,indent=1)
print(collections.Counter(a for _,a,_ in nuevos))
tot=sum(len(json.load(open("zip7/bancos/"+f))["preguntas"]) for f in os.listdir("zip7/bancos"))
print("total",tot)
