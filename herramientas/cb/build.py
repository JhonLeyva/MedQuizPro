import json, re, os, shutil
from merge import Q, D, O, N, X, final
BASE = "/home/user/MedQuizPro/herramientas/site/bancos"
shutil.rmtree("zipcb", ignore_errors=True); os.makedirs("zipcb/bancos")
for f in os.listdir(BASE): shutil.copy(os.path.join(BASE, f), "zipcb/bancos/")
FIX = [("Pneumocrystis carinli", "Pneumocystis carinii"), ("stercolaris", "stercoralis"), ("Kal-azhar", "kala-azar"),
       ("Trichuris trichiuria", "Trichuris trichiura"), ("Cefoxitima", "Cefoxitina"), ("Ceftadizina", "Ceftazidima"),
       ("Aminoglicósidos", "Aminoglucósidos"), ("Aminoglucosisdos", "Aminoglucósidos"), ("antituberulosos", "antituberculoso"),
       ("Isomacina", "Isoniacida"), ("Captotril", "Captopril"), ("Diltiazen", "Diltiazem"), ("Flumazelino", "Flumazenil"),
       ("Fisostegmina", "Fisostigmina"), ("Pralidoxina", "Pralidoxima"), ("Vacomicina", "Vancomicina"),
       ("Crabón", "Carbón"), ("Carón vegetal", "Carbón vegetal"), ("Mesentérica superior", "Mesentérica superior"),
       ("Glándula de cooper", "Glándula de Cowper"), ("Ieo", "Íleo"), ("Rotula", "Rótula"), ("Musculo", "Músculo"), ("musculo", "músculo"),
       ("Púlmon", "Pulmón"), ("organos", "órganos"), ("Ileon", "Íleon"), ("ileon", "íleon"), ("Deciama", "Décima"), ("Decima", "Décima"),
       ("Sétima", "Séptima"), ("Cigomatico", "Cigomático"), ("hemitiroidetomía", "hemitiroidectomía"),
       ("fructuosa", "fructosa"), ("prostangladinas", "prostaglandinas"), ("prostanglandia", "prostaglandina"),
       ("pseudoestrateficado", "pseudoestratificado"), ("cilindrico ciliaco", "cilíndrico ciliado"), ("cubito simple", "cúbico simple"),
       ("vesicula", "vesícula"), ("Calciformes", "Caliciformes"), ("cuasnate", "causante"), ("aureginosa", "aeruginosa"),
       ("Desmatitis", "Dermatitis"), ("Macula densa", "Mácula densa"), ("Hemophilus", "Haemophilus"), ("Micobacterium tuberculosae", "Mycobacterium tuberculosis"),
       ("Streptococcus agalactie", "Streptococcus agalactiae"), ("Enterococo fecalis", "Enterococcus faecalis"),
       ("Escherichia coli", "Escherichia coli"), ("colinestarasa", "colinesterasa"), ("Levocabastatina", "Levocabastina"),
       ("Turbocurarina", "Tubocurarina"), ("Orfenandrina", "Orfenadrina"), ("hidroclortiazida", "hidroclorotiazida"),
       ("plocilínico", "policlínico"), ("elecccion", "elección"), ("varon alcohólico", "Varón alcohólico"), ("traido", "traído"), ("vomitos", "vómitos"),
       ("Hipertonía muscular", "Hipertonía muscular"), ("existesospecha", "existe sospecha"), ("Epidídimo", "Epidídimo"),
       ("deferente", "deferente"), ("depense", "depende"), ("glosofarínego", "glosofaríngeo"), ("Wistkott", "Wiskott"),
       ("presitémicamente", "presistémicamente"), ("Hiperkalemia", "Hiperpotasemia"), ("Cuiomicrones", "Quilomicrones"),
       ("Quiiomicrones", "Quilomicrones"), ("enzina", "enzima"), ("Superior largo", "Supinador largo"), ("lago del pulgar", "largo del pulgar"),
       ("siblantes", "sibilantes"), ("sinusual", "sinusal"), ("mapas pulmonares", "campos pulmonares"), ("otros reactivas", "reactivas"),
       ("Gubemáculum", "Gubernáculo"), ("Cavemoso", "Cavernoso"), ("Malazesia", "Malassezia"), ("Alrdedor", "Alrededor"),
       ("Nodo Auriculo VEntricular", "Nodo auriculoventricular"), ("Burkit:", "Burkitt:"), ("Epstein Baar", "Epstein-Barr"),
       ("muscularismucosae", "muscular de la mucosa"), ("LaPaO2", "La PaO2"), ("meso néfrico", "mesonéfrico"), ("Wolf ", "Wolff "),
       ("Tirocincinasa", "Tirosina cinasa"), ("insecticidad", "insecticida"), ("anhistamínicos", "antihistamínicos"), ("hitamina", "histamina"),
       ("excéresis", "exéresis"), ("retroestemal", "retroesternal"), ("hidroxicurnarina", "hidroxicumarina"), ("fitomenadona", "fitomenadiona"),
       ("tmesis", "emesis"), ("lepolíticas", "lipolíticas"), ("papilar linguales", "papilas linguales"), ("Íleo rectal", "Iliorrectal"),
       ("Proneiros", "pronefros"), ("disrupcion", "disrupción"), ("asociacion", "asociación"), ("Sindrome", "Síndrome"),
       ("Trichocephalos", "Trichocephalus"), ("Stronyloides", "Strongyloides"), ("Fluouracilo", "fluorouracilo"),
       ("ocasiono", "ocasionó"), ("Órganofosforado", "Organofosforado"), ("órganofosforados", "organofosforados"), ("órgano fosforado", "organofosforado"),
       ("órganos fosforados", "organofosforados"), ("Órganos fosforados", "Organofosforados"), ("mama refiere", "madre refiere"),
       ("Que indicaría", "Qué indicaría"), ("¿Que ", "¿Qué "), ("Glucosa pasa", "La glucosa pasa"), ("Relaciones ambas", "Relacione ambas"),
       ("Sinconcrodosis", "Sincondrosis"), ("Has de", "Haz de"), ("Hiss", "His"), ("Purkinge", "Purkinje"), ("Kajal", "Cajal"),
       ("Lieberkhun", "Lieberkühn"), ("Panetti", "Paneth"), ("aldosterina", "aldosterona"), ("labomba", "la bomba"), ("Trocleartrosis", "Trocleartrosis"),
       ("Estreptolisina\n", "Estreptomicina"), ("Céulas", "Células"), ("Celulas", "Células"), ("Guaninarq", "Guanina"), ("Citocina", "Citosina"),
       ("CLNa 9 %O", "ClNa 0,9 %"), ("Tirocina", "Tirosina"), ("Mintezol", "Tiabendazol"), ("Clorfenamina", "Clorfenamina"),
       ("Poliomielitis", "Poliovirus"), ("Papiloma virus", "Virus del papiloma humano"), ("Molluscum contagioso", "Molusco contagioso"),
       ("Apelt", "Apelt"), ("Middle Brook", "Middlebrook"), ("Jarish", "Jarisch"), ("aseveraciones", "aseveraciones"),
       ("Pregunta", "Pregunta"), ("  ", " ")]
FIX += [("acetilcisteina", "acetilcisteína"), ("Acetilcisteina", "Acetilcisteína"), ("adenohipofisis", "adenohipófisis"), ("Adenohipofisis", "Adenohipófisis"),
 ("neurohipofisis", "neurohipófisis"), ("Allopurinol", "Alopurinol"), ("Aminoglucosidos", "Aminoglucósidos"), ("B lactamicos", "betalactámicos"),
 ("B – lactámicos", "Betalactámicos"), ("Macrolidos", "Macrólidos"), ("apoptoticos", "apoptóticos"), ("barrea", "barrera"), ("Capsula", "Cápsula"),
 ("Cariolisis", "Cariólisis"), ("colonica", "colónica"), ("Cérvicofacial", "Cervicofacial"), ("Aurículotemporal", "Auriculotemporal"),
 ("Fenitoina", "Fenitoína"), ("fenitoína", "fenitoína"), ("Fenotiacina", "Fenotiazina"), ("Fusion anormal", "Fusión anormal"), ("Hassal ", "Hassall "),
 ("humero", "húmero"), ("intraepitelilal", "intraepitelial"), ("mesonefricos", "mesonéfricos"), ("Monosomia", "Monosomía"), ("muller", "Müller"),
 ("Muller", "Müller"), ("muscarinico", "muscarínico"), ("Músculocutáneo", "Musculocutáneo"), ("Músculo cutáneo", "Musculocutáneo"), ("naloxone", "naloxona"),
 ("Parasimpáticomimetico", "Parasimpaticomimético"), ("Simpaticolitico", "Simpaticolítico"), ("Sinfisis", "Sínfisis"), ("Soleo", "Sóleo"),
 ("Utero", "Útero"), ("utero", "útero"), ("vassorun", "vasorum"), ("vassorum", "vasorum"), ("via oral", "vía oral"), ("trasversas", "transversas"), ("Meticilín resistente", "resistente a meticilina"),
 ("Betaproteinas", "Betaproteínas"), ("rhabditiforme", "rabditiforme"), ("Áscaris", "Ascaris"), ("epifora", "Epífora"), ("equímosis", "equimosis"),
 ("estadíos", "estadios"), ("desecamiento", "sequedad"), ("somnolencias", "somnolencia"), ("aorto- bifemoral", "aortobifemoral"), ("by-pass", "bypass"),
 ("Pubocoxígeo", "Pubococcígeo"), ("Espermatocitos ll", "Espermatocitos II"), ("shunts fisiológicos", "cortocircuitos fisiológicos"), ("Cis_LT1", "CysLT1"),
 ("Nonne - Apelt", "Nonne-Apelt"), ("GP exceptuando", "grampositivos, exceptuando"), ("glándulas tiroideas", "glándulas tiroideas"),
 ("Blastocystis hominis?:", "Blastocystis hominis?"), ("?:", "?"), ("hemato – encefálica", "hematoencefálica"), ("hemato-testicular", "hematotesticular"),
 ("inmuno – mucoso", "inmunitario de la mucosa"), ("Ig que", "inmunoglobulina que"), ("Wernicke – Korsakoff", "Wernicke-Korsakoff"), ("Beri – Beri", "beriberi"),
 ("Pre – escolar", "Preescolar"), ("Pre – albúmina", "Prealbúmina"), ("N – acetil cisteína", "N-acetilcisteína"), ("N acetilcisteína", "N-acetilcisteína"), ("N acetilcisteina", "N-acetilcisteína"),
 ("H – 1", "H1"), ("beta – 2", "beta-2"), ("L – arginina", "L-arginina"), ("6 - Mercaptopurina", "6-mercaptopurina"), ("5 - fluorouracilo", "5-fluorouracilo"),
 ("Piperacilina / tazobactam", "Piperacilina-tazobactam"), ("Ampicilina / sulbactam", "Ampicilina-sulbactam"), ("Imipenem / Cilastatina", "Imipenem-cilastatina"), ("Piperacilina / tazobactam", "Piperacilina-tazobactam"),
 ("Pregunta", "Pregunta"), ("edinger westphal", "Edinger-Westphal"), ("meq/l", "mEq/L"), ("Acetil-colinesterasa", "Acetilcolinesterasa")]
def fx(s):
    for a, b in FIX: s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("cross – over", "entrecruzamiento (crossing-over)")
    s = re.sub(r"(\w) – (\w)", r"\1-\2", s)
    s = s.replace("por via", "por vía")
    s = re.sub(r"\s*(?:…+\.*|\.{3,})\s*", " ______ ", s).strip()
    s = re.sub(r"______ ([:?])", r"______\1", s)
    s = re.sub(r"\s+([,.;:?])", r"\1", s)
    return s
def opt(s):
    s = fx(s)
    if s.endswith(".") and len(s.split()) <= 4: s = s[:-1]
    return s[0].upper() + s[1:] if s else s
cb = json.load(open("zipcb/bancos/ciencias_basicas.json"))
# Base: el banco CB previo (92 preguntas). site/bancos ya incluye estas 393; no reconstruir sobre él.
cb["preguntas"] = [p for p in cb["preguntas"] if not p.get("examen_origen", "").startswith("Banco de Ciencias Básicas 2019")]
assert len(cb["preguntas"]) == 92, len(cb["preguntas"])
last = max(int(p["id"].split("-")[1]) for p in cb["preguntas"])
nuevos = []
for n in sorted(D):
    t, k, c = D[n]
    e, op = final(n)
    last += 1
    ops = [opt(op[a]) for a in "ABCDE"]
    i = "ABCDE".index(k)
    p = {"id": "CB-%03d" % last, "especialidad": "Ciencias Básicas",
         "examen_origen": "Banco de Ciencias Básicas 2019 · pregunta de práctica",
         "enunciado": re.sub(r"\s*______$", ":", fx(e)), "opciones": ops, "correcta": i, "clave_correcta": k,
         "explicacion": c, "comentario": c, "tema": t, "año": 2019}
    cb["preguntas"].append(p); nuevos.append(dict(p, n=n))
json.dump(cb, open("zipcb/bancos/ciencias_basicas.json", "w"), ensure_ascii=False, indent=2)
json.dump(nuevos, open("nuevoscb.json", "w"), ensure_ascii=False, indent=1)
print("nuevas", len(nuevos), "CB total", len(cb["preguntas"]), "rango", nuevos[0]["id"], nuevos[-1]["id"])
