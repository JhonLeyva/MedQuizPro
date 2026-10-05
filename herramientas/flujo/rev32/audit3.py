import sys; sys.path.insert(0, ".")
import json, re, os, importlib, c28
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
E=json.load(open('rev30/entrega3.json')); spec={f["id"]:f for f in c28.F28}
def txt(o):
    if isinstance(o,str): return o+" "
    if isinstance(o,dict): return "".join(txt(v) for k,v in o.items() if k!="credito")
    if isinstance(o,(list,tuple)): return "".join(txt(v) for v in o)
    return ""
KW=r"Gleason|ISUP|Glasgow|Apgar|Silverman|Downes|Child[- ]Pugh|MELD|NYHA|Killip|Forrester|CURB|CRB|CHA₂?DS|HAS-BLED|Wells|Centor|McIsaac|Alvarado|Ranson|BISAP|Atlanta|Balthazar|Forrest|Rockall|Blatchford|Bishop|Manning|perfil biofísico|FIGO|TNM|Breslow|Clark|Fontaine|Rutherford|CEAP|Hinchey|Tokio|Bethesda|BI-RADS|TI-RADS|Lauren|Borrmann|Los Ángeles|Savary|Parkland|Ballard|Capurro|Tanner|Kramer|Lund|Garden|Gustilo|Salter|Neer|Weber|Ottawa|Ann Arbor|Rai|Binet|Durie|GOLD|GINA|mMRC|KDIGO|AKIN|RIFLE|Light|Marshall|Fisher|Hunt|WFNS|NIHSS|ABCD|Rankin|Hoehn|Mallampati|ASA|Aldrete|Caprini|Padua|Duke|Jones|Westley|Bhutani|Sarnat|Karnofsky|ECOG|Dukes|Bosniak|Clavien|West Haven|Zargar|Sydney|OLGA|Ferriman|Rotterdam|POP-Q|Baden|Hodge|DeLee|Graf|Kellgren|ACR/EULAR|SLEDAI|TIMI|GRACE|HEART|Ginebra|PERC|PESI|Sokolow|Mobitz|Lown|Wallace|Spetzler|MMSE|MoCA|CAGE|AUDIT|PHQ|Hamilton|Beck|Edimburgo|Yale|qSOFA|SOFA|SIRS|APACHE|Wagner|PEDIS|Rumack|Gell|Coombs y Gell|Waterlow|Braden|Norton|Barthel|Katz|Lawton|Pfeiffer|Yesavage|Tinetti|Holliday|Waterlow|Lansky|Page|Sheehan|Amsel|Nugent|Papanicolaou|NIC|ASC-US|Hurley|PASI|SCORAD|Fitzpatrick|Vesikari|Dehidrat|AIEPI|Gómez|Waterlow|Waterlow|Cobb|Risser|Ponseti|Pirani|Dimeglio|Lachman|Ficat|Steinberg|Herring|Catterall|Seddon|Meyerding|Frankel|ASIA|Denis|Lauge|Danis|Schatzker|AO|Pauwels|Mason|Tossy|Rockwood|Allman|Tile|Young-Burgess|Roper|METAVIR|Hoehn|Glasgow-Blatchford|Wilson|Mayo|Truelove|Montreal|Paris|Harvey|Crohn|Vienna|Lille|Maddrey|Hunt y Hess|ICROP|Tanner|Hurley|Clark|Rye|Reed|Lukes|Kiel|WHO|Fried|Siewert|Barcelona|BCLC|Milan|Ishak|Knodell|Scheuer|Brunt|Kleiner|Sanyal|Lugano|Revised|Durie|ISS|IPI|Sokal|Hasford|Gail|Tyrer|NOTCH|Nottingham|Elston|Van Nuys|Bloom|Pap|Mantoux|Fontaine|Leriche|Stanford|DeBakey|Crawford|Wagner|Texas|Sanders|Essex|Hawkins|Kellgren|Outerbridge|Ahlback|Insall|Gartland|Holstein|Monteggia|Galeazzi|Colles|Smith|Barton|Frykman|Herbert|Mayfield|Lichtman|Seddon|Sunderland|Mackinnon|Medical Research Council|MRC|Daniels|Ashworth|Tardieu|GMFCS|Prechtl|Denver|Bayley|Haizea|EEDP|TEPSI|Battelle|Brazelton|Dubowitz|Finnegan|Thompson|Sarnat|Papile|Volpe|Bell|Walsh|Usher|Bell|Bethesda|Wood|Pulmonary|Tal|Taussig|Bierman|Silverman|BROSJOD|ROSE|NOM|SRU|ETROP"
res=[]
for i in E:
    f=spec[i]; t=txt({k:v for k,v in f.items() if k not in("escala",)})
    en = (f.get("escala") or {}).get("nombre","") + " " + txt((f.get("d") or {}).get("escala","")) + " " + (txt(f.get("escala") or {}))
    hits=sorted(set(m.group(0) for m in re.finditer(KW,t)))
    falt=[h for h in hits if h not in en]
    if falt: res.append((i,f["tipo"],bool(f.get("escala")),falt))
for r in res: print(r)
print(len(res))
