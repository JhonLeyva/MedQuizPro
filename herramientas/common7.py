import json,re,glob,os,shutil
q={x["n"]:x for x in json.load(open("parsed.json"))}
try:
    from fix6 import FIX6
except ImportError:
    FIX6=[]
from fix6 import FIX6B
FIX=[("antimicrobia na","antimicrobiana"),("el ección","elección"),("m ayores","mayores"),("descart adas","descartadas"),
("tra uma","trauma"),("ma nipulación","manipulación"),("agud a","aguda"),("vasa pre via","vasa previa"),("exa men","examen"),
("pro funda","profunda"),("visi ón","visión"),("P or ","Por "),("oxit ocina","oxitocina"),("tensió n","tensión"),
("co ncentraciones","concentraciones"),("c ualquier","cualquier"),("enfe rmedad","enfermedad"),("inmedi ata","inmediata"),
("hac e","hace"),("veno so","venoso"),("pandemi a","pandemia"),("indi ca","indica"),("procedi miento","procedimiento"),
("trí ada","tríada"),("ajusta n","ajustan"),("escalamient o","escalamiento"),("anti -D","anti-D"),("COVID -19","COVID-19"),
("omega -3","omega-3"),("24 -28","24-28"),("post - fecundación","posfecundación"),("SARS- CoV-2","SARS-CoV-2"),
("leve -moderado","leve-moderado"),("SO I:","SatO₂:"),("SOI de","SatO₂ de"),("SatOI","SatO₂"),("HCO I","HCO₃⁻"),("HCOI","HCO₃⁻"),
("PaO I","PaO₂"),("En ¿casos","En casos"),("tuberculosis .","tuberculosis."),("copias/ml ,","copias/ml,"),
("Currant jelly stools, dolor cólico y masa palpable","dolor cólico, masa palpable y heces en «jalea de grosella» (currant jelly stools)"),
("la trí ada de","la tríada de"),("pos tratamiento","postratamiento"),("El cuadro clínico más hallazgo","El cuadro clínico más el hallazgo"),
("gram negativos","gramnegativos"),("gram positivos","grampositivos"),("Propiltiuracilo","Propiltiouracilo"),("Aborto frustro","Aborto frustrado"),
("40 x′","40 x'"),("me tronidazol","metronidazol"),("c eftriaxona","ceftriaxona"),("síndr ome","síndrome"),("si tio","sitio"),("res ervan","reservan"),("hipert ensión","hipertensión"),
("suma das","sumadas"),("Tako -tsubo","Takotsubo"),("Tako-tsubo","Takotsubo"),("valvulopatía p revia","valvulopatía previa"),("β -talasemia","β-talasemia"),("hemóli sis","hemólisis"),
("inflamac ión","inflamación"),("8 -10","8-10"),("entero cutáneas","enterocutáneas"),("entero entéricas","enteroentéricas"),("hallaz gos","hallazgos"),("Est a","Esta"),
("HTLV -1","HTLV-1"),("rela ción","relación"),("combina ndo","combinando"),("diagnóstic o","diagnóstico"),("gamma gráfica","gammagráfica"),("intensivo :","intensivo:"),
("beta bloqueadores","betabloqueadores"),("faci lidad","facilidad"),("diag nosticar","diagnosticar"),("respiratorios .","respiratorios."),("trata miento","tratamiento"),
("internas ,","internas,"),("en es te","en este"),("objet ivo","objetivo"),("cultiv o","cultivo"),("octreotid e","octreotide"),("opción e s","opción es"),("costo -efectividad","costo-efectividad"),("inmedia ta","inmediata"),("desencad enante","desencadenante"),("pen icilina","penicilina"),("cl ínica","clínica"),("tó picos","tópicos"),("coron aria","coronaria"),("emergenc ia","emergencia"),("clínic as","clínicas"),("c onfirmar","confirmar"),("dexametazsona","dexametasona"),("morragi a","morragia"),("m anometría","manometría"),("c omunicación","comunicación"),("reh idratación","rehidratación"),("contex to","contexto"),("audi tivo","auditivo"),("Po r","Por"),("gluco corticoides","glucocorticoides"),("diag nóstico","diagnóstico"),("e lectrocardiográficos","electrocardiográficos"),("fiebre n i sangre","fiebre ni sangre"),("2 -6","2-6"),("hepá tico","hepático"),("pe rforada","perforada"),("visib le","visible"),("in fección","infección"),("sang re","sangre"),("efi caz","eficaz"),("pr obable","probable"),("l a depresión","la depresión"),("inmed iata","inmediata"),("ci rrosis","cirrosis"),("venti latorio","ventilatorio"),("toxina -inhibidora","toxina-inhibidora"),("u o tras","u otras"),("clínico -patológicos","clínico-patológicos"),("adecua do","adecuado"),("cui dadosa","cuidadosa"),("anemi a","anemia"),("Jod -Basedow","Jod-Basedow"),("med ida","medida"),("sufactante","surfactante"),("cefaloraquídeo","cefalorraquídeo"),("otoscopío","otoscopía"),("Butaconazol","Butoconazol"),("Anfotericin","Anfotericina B"),("Anfotericina Ba B","Anfotericina B"),("Trofozoitos","Trofozoítos"),("fémoropoplíteo","femoropoplíteo"),("toráx","tórax"),("cardiorespiratorio","cardiorrespiratorio"),("Intima","Íntima"),("En es te","En este"),("sub costal","subcostal"),("br onquial","bronquial"),("de l asma","del asma"),("inf iltrados","infiltrados"),("Guillain -Barré","Guillain-Barré"),
("anti -VHA","anti-VHA"),("epidémicos e n la","epidémicos en la"),("Erb - Duchenne","Erb-Duchenne"),("Erb- Duchenne","Erb-Duchenne"),("hidrocefalia s on","hidrocefalia son"),("un re to","un reto"),("perito neal","peritoneal"),
("Staphyhilococcus","Staphylococcus"),("Brudzinsky","Brudzinski"),("urliana","urleana"),("Sutiles","Sutiles"),("protusión","protrusión"),("microcitocis","microcitosis"),
("lautolimitados","autolimitados"),("toráxico","torácico"),("tactil","táctil"),("oxìgeno","oxígeno"),("sistòlico","sistólico"),("periférico normales","periféricos normales"),
("que,,,,,,,,,,,,,,,,,,,,,,,","que:"),("la..........…","la:"),("convulsiones…","convulsiones:"),(":¿",": ¿"),(".¿",". ¿"),(". i ¿"," ¿"),("PaCOI","PaCO₂"),("SO2","SatO₂"),("PaO2","PaO₂"),
("Tº","T°"),("Dx? probable","diagnóstico probable"),("MEG,","mal estado general,"),("en MEG","en mal estado general"),("(Brazo izquierdo.","(brazo izquierdo)."),("(Brazo derecho)","(brazo derecho)"),]
FIX5=[('Gono rrea', 'Gonorrea'), ('a denopatías', 'adenopatías'), ('abs ceso', 'absceso'), ('acci ón', 'acción'), ('adenopat ías', 'adenopatías'), ('admin istrarse', 'administrarse'), ('adu ltos', 'adultos'), ('alerg ias', 'alergias'), ('amil asa', 'amilasa'), ('antibiotico terapia', 'antibioticoterapia'), ('as ociarse', 'asociarse'), ('ba sado', 'basado'), ('c aptación', 'captación'), ('car acterísticos', 'característicos'), ('carb ohidratos', 'carbohidratos'), ('centr o', 'centro'), ('cirugí a', 'cirugía'), ('clí nico', 'clínico'), ('clíni co', 'clínico'), ('co ncepto', 'concepto'), ('comparació n', 'comparación'), ('con ducta', 'conducta'), ('con traste', 'contraste'), ('contr actura', 'contractura'), ('corti cal', 'cortical'), ('cu adro', 'cuadro'), ('cu ando', 'cuando'), ('cua dro', 'cuadro'), ('cuantitativ a', 'cuantitativa'), ('d ebe', 'debe'), ('d eberá', 'deberá'), ('demand a', 'demanda'), ('desa rrollo', 'desarrollo'), ('deso rientación', 'desorientación'), ('e levada', 'elevada'), ('e levarse', 'elevarse'), ('e stá', 'está'), ('e ventos', 'eventos'), ('ec ocardiografía', 'ecocardiografía'), ('ento rno', 'entorno'), ('es fuerzo', 'esfuerzo'), ('esfer ocitosis', 'esferocitosis'), ('estr ategias', 'estrategias'), ('evalu ación', 'evaluación'), ('f ases', 'fases'), ('f inalización', 'finalización'), ('f ístula', 'fístula'), ('fascit is', 'fascitis'), ('feb ril', 'febril'), ('fi ebre', 'fiebre'), ('ge nerando', 'generando'), ('gloti s', 'glotis'), ('gonad al', 'gonadal'), ('h emotórax', 'hemotórax'), ('h istológico', 'histológico'), ('he maturia', 'hematuria'), ('hipovol emia', 'hipovolemia'), ('inc luye', 'incluye'), ('insp iratorio', 'inspiratorio'), ('interventri cular', 'interventricular'), ('inversi ón', 'inversión'), ('llev ar', 'llevar'), ('m uy', 'muy'), ('mejo r', 'mejor'), ('muscarínico s', 'muscarínicos'), ('ner vioso', 'nervioso'), ('nor mal', 'normal'), ('norm al', 'normal'), ('ob structivo', 'obstructivo'), ('otr os', 'otros'), ('p eriférica', 'periférica'), ('p uede', 'puede'), ('pe rmite', 'permite'), ('perti nente', 'pertinente'), ('pos terior', 'posterior'), ('presen cia', 'presencia'), ('prob able', 'probable'), ('pru rito', 'prurito'), ('pulmona r', 'pulmonar'), ('r adiografía', 'radiografía'), ('res puestas', 'respuestas'), ('riniti s', 'rinitis'), ('sanitari a', 'sanitaria'), ('sensibilida d', 'sensibilidad'), ('serí a', 'sería'), ('significativam ente', 'significativamente'), ('so cial', 'social'), ('sínto mas', 'síntomas'), ('t aquicardia', 'taquicardia'), ('t rastorno', 'trastorno'), ('terap éutica', 'terapéutica'), ('tisu lar', 'tisular'), ('tóxi cos', 'tóxicos'), ('uteri no', 'uterino'), ('ventil adas', 'ventiladas'), ('vir ales', 'virales'), ('ú til', 'útil')]
FIX=FIX+FIX5

def post5(s):
    for a,b in FIX6B: s=s.replace(a,b)
    s=re.sub(r"\s?\b2c\b","",s); s=re.sub(r"^\s*2\s+(?=[A-ZÁÉÍÓÚ])","",s)
    s=re.sub(r"\bCO I\b","CO₂",s)
    s=re.sub(r"\s*\(ENAM [^)]*\)\s*\d?\s*$","",s); s=re.sub(r"\s*\(ENAM [^)]*\)\s*2\b","",s)
    s=re.sub(r"\b(SatO|SaO|PaO|pO|PaCO|pCO|FiO|Sat O|O) ?I\b(?=[\s:,.%)])",lambda m: m.group(1).replace(" ","")+"₂",s)
    s=re.sub(r"\bHCO ?I\b","HCO₃⁻",s); s=re.sub(r"\b[xX] I\b","x'",s)
    s=re.sub(r"\b(?:Sat ?O|SaO) ?I\b","SatO₂",s); s=re.sub(r"\bFiO ?I\b","FiO₂",s)
    s=s.replace("T °","T°")
    s=re.sub(r"\bpOI\b","pO₂",s); s=re.sub(r"\bpCOI\b","pCO₂",s); s=s.replace("ADA: 6 7 U/L","ADA: 67 U/L")
    s=re.sub(r"\bSat ?O2\b","SatO₂",s); s=re.sub(r"\bSaO2\b","SaO₂",s)
    s=s.replace("post - traumático","postraumático").replace("horas post - trauma","horas tras el trauma")
    s=re.sub(r"(?<!estación)(?<!altura) -(?=[A-Za-zÁÉÍÓÚáéíóúñ0-9])","-",s) if False else s
    s=re.sub(r"([A-Za-zÁÉÍÓÚáéíóúñI0-9]) -([A-Za-zÁÉÍÓÚáéíóúñ0-9])",lambda m: m.group(0) if re.search(r"(estación|presentación)$",s[:m.start()+1]) else m.group(1)+"-"+m.group(2),s)
    s=re.sub(r"([a-záéíóúñ]) - ([a-záéíóúñA-Z])",r"\1-\2",s)
    s=re.sub(r"\s*Respuesta\.? ?[A-E]\.?\s*$","",s)
    s=re.sub(r"\s*\.{3,}\s*$",":",s)
    return s
def clean(s):
    for a,b in FIX: s=s.replace(a,b)
    for a,b in FIX6: s=re.sub(r"(?<![\wÁÉÍÓÚÜÑáéíóúüñ])"+re.escape(a)+r"(?![\wÁÉÍÓÚÜÑáéíóúüñ])",b,s)
    s=re.sub(r"\s+"," ",s).strip()
    s=re.sub(r"\s+([,.;:])",r"\1",s)
    return post5(s)
def strip_src(s): return re.sub(r"\s*\(ENAM[^)]*\)\s*$","",s).strip()
def strip_resp(s):
    s=re.sub(r"\s*Respuesta:? [A-E][.:]?[^.]*\.?\s*$","",s)
    s=re.sub(r"\s*Respuesta [A-E]\s*$","",s)
    return s.strip()
PREF={}
def year_of(n):
    for k in range(n,0,-1):
        if k in q:
            m=re.search(r"\(ENAM (\d{3} ?\d)[^)]*\)",q[k]["enunciado"])
            if m: return int(m.group(1).replace(" ",""))
