import json,collections,os
exec(open("sel7.py").read())
q={x["n"]:x for x in json.load(open("parsed.json"))}
N=json.load(open("nuevos7.json"))
fix=sum(1 for n,a,t,l in SEL if q[n]["hl"] and q[n]["hl"][0]!=l)
sin=sum(1 for n,a,t,l in SEL if not q[n]["hl"])
ver=sum(1 for n,a,t,l in SEL if q[n]["verif"])
ncom=sum(1 for n,a,t,l in SEL if n in COM)
anos=collections.Counter(p["año"] for p in N)
by=collections.defaultdict(list)
for p in N: by[p["archivo"]].append(p)
esp={a:json.load(open(f"zip7/bancos/{a}.json"))["especialidad"] for a in by}
L=[]
L+=["MedQuizPro - Bloque 7 del Banco ENAM (500 preguntas nuevas)","="*60,"","Qué contiene",
"- Carpeta bancos/ con los 17 archivos JSON (todas las especialidades), completos:",
"  preguntas de los bloques 1 a 6 + las 500 nuevas (1579 en total). Se reemplaza el archivo completo.",
"  Las 1079 preguntas anteriores no cambian.",
f"- Preguntas del PDF que quedaban pendientes (ENAM 2020 a 2024). Esta vez se revisaron también las",
f"  marcadas \"Verificar\" y las que no tenían respuesta resaltada: {ver} marcadas \"Verificar\" y {sin} sin resaltado",
f"  entraron tras comprobar la clave con el comentario y la literatura actual (MINSA, guías vigentes).",
f"- Claves corregidas: en {fix} preguntas la letra resaltada en el PDF estaba equivocada y se usó la correcta.",
f"  En {ncom} preguntas el comentario del PDF no correspondía, era incompleto o defendía otra opción,",
f"  y se reemplazó por una explicación propia.",
"- Se omitieron: las que dependen de una imagen, las de clave ambigua u obsoleta, las casi idénticas",
"  a otra del banco y las que repiten un concepto ya publicado (mismo tema y misma respuesta).",
"- Texto limpiado: palabras partidas por el PDF, subíndices (SatO₂, pCO₂, HCO₃⁻), números de página",
"  sueltos, espacios de completar unificados como ______ y signos (mayor)/(menor) convertidos a > y <.",
"- Años: "+", ".join(f"{a} ({anos[a]})" for a in sorted(anos))+".","",
"Cómo instalarlo en Hostinger",
"1. public_html/bancos/: descarga una copia de respaldo de los archivos actuales.",
"2. Sube el ZIP a public_html y usa \"Extraer\" con destino public_html (NO una carpeta nueva).",
"   Acepta reemplazar los archivos.",
"3. Recarga la web con Ctrl+F5.",
"4. Opcional: abre verificar-flujogramas.html; debe seguir en 1079 abren bien y 0 sin pregunta.",
"   Las 500 preguntas nuevas aún no tienen flujograma propio: \"Ver algoritmo\" muestra el aviso",
"   genérico hasta que se suba el paquete de flujogramas del bloque 7.","",
"Preguntas nuevas por especialidad"]
for a,ps in sorted(by.items(),key=lambda kv:-len(kv[1])):
    L.append(f"- {esp[a]} ({a}.json): {len(ps)}  [{ps[0]['id']} a {ps[-1]['id']}]")
    for p in ps: L.append(f"    {p['id']}  {p['tema']}  (PDF n.º {p['pdf_pregunta']})")
    L.append("")
open("zip7/LEEME.txt","w").write("\n".join(L).rstrip()+"\n")
print("\n".join(L[:32]))
