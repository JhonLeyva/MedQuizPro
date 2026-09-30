import re, json, collections
VB=collections.Counter(json.load(open('vocab_bank.json')))
UNITS=[("mEqfL","mEq/L"),("mEqf","mEq/"),("mgfdL","mg/dL"),("mgfdl","mg/dl"),("gfdL","g/dL"),("mmolfL","mmol/L"),("yumolfL","µmol/L"),("mUIfml","mUI/ml"),("copiasfml","copias/ml"),("copiasfmL","copias/mL"),
("gfkg","g/kg"),("mlfkg","ml/kg"),("mgfkg","mg/kg"),("mgfdía","mg/día"),("kgf","kg/"),("UfL","U/L"),("ufL","U/L"),("fpL","/µL"),("fuL","/µL"),("mOsmf","mOsm/"),("IECAJARA","IECA/ARA"),("AAPJAAPCC","AAP/AAPCC"),
("FEVIJFVC","FEV1/FVC"),("FEVIÍFVC","FEV1/FVC"),("HbAlc","HbA1c"),("bocafnariz","boca/nariz"),("albúminafcreatinina","albúmina/creatinina"),("náuseasfvómitos","náuseas/vómitos"),("insulinafdextrosa","insulina/dextrosa"),
("polimorfonuclearesfmm","polimorfonucleares/mm"),("mgf","mg/"),("gf","g/"),("lAFAS","IAFAS"),("IlAFAS","IAFAS"),("lECA","IECA"),("lAM","IAM"),("lOT","IOT"),("VIl","VII"),("EvWw","EvW"),("ISBl","ISBI"),("ElA","EIA")]
MAN={"fleo":"íleo","leon":"íleon","hidrogéreos":"hidroaéreos","hidrogaéreos":"hidroaéreos","heonato":"neonato","oximetrña":"oximetría","protocalo":"protocolo","justificariía":"justificaría","retraiída":"retraída","dire":"aire",
"sindrome":"síndrome","Sindrome":"Síndrome","especificamente":"específicamente","sistemica":"sistémica","sistemico":"sistémico","indice":"índice","interes":"interés","timpano":"tímpano","hepatica":"hepática","regimen":"régimen",
"odinofagía":"odinofagia","amigdalas":"amígdalas","menorragía":"menorragia","primipara":"primípara","multipara":"multípara","episiotomia":"episiotomía","Pelvimetria":"Pelvimetría","pelvimetria":"pelvimetría","linfadenopatias":"linfadenopatías",
"sintomas":"síntomas","acetilcisteina":"acetilcisteína","meningea":"meníngea","bacilifera":"bacilífera","rigidamente":"rígidamente","Plasmaferesis":"Plasmaféresis","estasís":"estasis","Cesórea":"Cesárea","cesóáreas":"cesáreas",
"láóctica":"láctica","intrahepótica":"intrahepática","metáófisis":"metáfisis","demós":"demás","Guillgin":"Guillain","Schónlein":"Schönlein","Sschónlein":"Schönlein","Galpin":"Guillain","linguísticas":"lingüísticas",
"Hodakin":"Hodgkin","Hodokin":"Hodgkin","Leishamania":"Leishmania","Paviik":"Pavlik","sultfonamidas":"sulfonamidas","ciclofostamida":"ciclofosfamida","Ciclofostamida":"Ciclofosfamida","politransftundidos":"politransfundidos",
"microinftartos":"microinfartos","olicina":"glicina","oluconato":"gluconato","olicémicos":"glicémicos","codgulopatía":"coagulopatía","dórtico":"aórtico","iradiado":"irradiado","esoftugopatía":"esofagopatía","distagia":"disfagia",
"exantermna":"exantema","sigmoidectoría":"sigmoidectomía","linfuadenectoría":"linfadenectomía","rmonocional":"monoclonal","rmoderado":"moderado","instumentado":"instrumentado","antiinflamatoriío":"antiinflamatorio",
"Suspenader":"Suspender","núuseas":"náuseas","utilia":"utiliza","hipoalouminemia":"hipoalbuminemia","AJCCO":"AJCC","Especuloscopíia":"Especuloscopía","enfernedad":"enfermedad","hipofosfaternia":"hipofosfatemia",
"hipormagnesemia":"hipomagnesemia","hipoglucernia":"hipoglucemia","hernodinámico":"hemodinámico","hernorroides":"hemorroides","levernente":"levemente","serohernático":"serohemático","serohnemático":"serohemático","hermatoma":"hematoma",
"hernofagocítico":"hemofagocítico","hernólisis":"hemólisis","pigrnientarios":"pigmentarios","multisistérmico":"multisistémico","Hipertiroidisrmmo":"Hipertiroidismo","predeciblernente":"predeciblemente","adernás":"además","hiperbilirubinemia":"hiperbilirrubinemia",
"normocíitica":"normocítica","citometriía":"citometría","retinopatíia":"retinopatía","acetilcisteiína":"acetilcisteína","radíial":"radial","epidéermica":"epidérmica","periíanal":"perianal","violúceo":"violáceo","lliofemoral":"iliofemoral","lliaca":"ilíaca",
"metilpreadnisolona":"metilprednisolona","biarmniótica":"biamniótica","mielicéricas":"melicéricas","buloso":"bulloso","Streptococo":"Streptococcus","colelap":"colelap","atrogénico":"iatrogénico"}
def fix(s):
    for a,b in UNITS: s=re.sub(r"(?<![A-Za-zÁÉÍÓÚáéíóúñ])"+re.escape(a),b,s)
    def w(m):
        x=m.group(0)
        if x in MAN: return MAN[x]
        if VB[x.lower()]: return x
        for a,b in (("rn","m"),("ii","i"),("íí","í"),("ií","í"),("fi","/"),("ó","a"),("á","ó")):
            if a in x:
                y=x.replace(a,b)
                if VB[y.lower()]>=2: return y
        return x
    s=re.sub(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",w,s)
    s=re.sub(r"\s+([,.;:])",r"\1",s)
    s=s.replace(" ,",",").replace("¡ilíaca","ilíaca").replace("*C","°C").replace("Ul ","UI ").replace(" Ul"," UI")
    return s

TOK={"dérea":"aérea","cérea":"aérea","Ill":"III","lll":"III","ll":"II","Il":"II","Tlb":"T1b","Tla":"T1a","UJL":"U/L","ABLI":"ABL1","EXG":"EKG","Fil":"FII","rkK":"rK","Naci":"NaCl","HCI":"HCl",
 "moderadosevero":"moderado-severo","violáceanecrótica":"violáceo-necrótica","ANCApositiva":"ANCA positiva","Alos":"A los","Tónnis":"Tönnis","hno":"no","sim":"sin","colelap":"colecistectomía laparoscópica","lg":"1 g","Xx":"x'"}
def fix2(s):
    s=fix(s)
    s=re.sub(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",lambda m: TOK.get(m.group(0),m.group(0)),s)
    s=s.replace("fphCG","β-hCG").replace("fphC","β-hC").replace("V6I7F","V617F").replace("(934;q11)","(q34;q11)").replace("rK39","rK39").replace("rK 39","rK39")
    s=s.replace("/mwm","/mm³").replace("/mr”","/mm³").replace("/mm*","/mm³").replace("/mm»","/mm³").replace("/mm”","/mm³").replace("g//dL","g/dL").replace("mg//g","mg/g").replace("mEq[L","mEq/L").replace("*”C","°C").replace(" ec,"," °C,")
    s=re.sub(r"(?<=\d), (?=\d{3}\b)"," ",s)   # 23, 000 -> 23 000
    s=re.sub(r"(?<=\d), (?=\d)",",",s)         # 37, 8 -> 37,8
    s=re.sub(r"(?<=\d), ?O\b",",0",s)
    s=s.replace("VIII!","VIII").replace("(XI!)","(XII)")
    s=re.sub(r"\s+"," ",s).strip()
    return s
