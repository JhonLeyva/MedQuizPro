import json,collections
from dupx import DUP
C=json.load(open('cand.json')); N=json.load(open('nuevos26.json'))
exc=[c for c in C if 'excluida' in c]
falt=[c for c in exc if 'faltante' in c['excluida']]
dud=[c for c in exc if 'dudosa' in c['excluida'].lower()]
rep_int=[c for c in exc if c not in falt and c not in dud]
by=collections.defaultdict(list)
for p in N: by[p['archivo']].append(p)
esp={a:ps[0]['especialidad'] for a,ps in by.items()}
L=[f"MedQuizPro - Bloque ENAM 2026 ({len(N)} preguntas nuevas)","="*60,"",
"Qué contiene",
f"- Carpeta bancos/ con los {len(by)} archivos JSON que cambian. Cada archivo trae el banco completo",
f"  (las preguntas que ya tenías + las nuevas). El sitio pasa de 2106 a {2106+len(N)} preguntas.",
"- Fuente: los 2 PDF «ENAM COMENTADO 2026» (Examen ENAM Extraordinario 2026 y Extraordinario II 2026),",
"  180 preguntas cada uno = 360 en total. No hay 500: esos dos PDF solo traen 360.",
f"- Entraron {len(N)}. Se omitieron {len(C)-len(N)}:",
f"    {len(DUP)+len(rep_int)} porque repiten el mismo concepto y la misma respuesta de una pregunta ya publicada",
"       (o de otra de estos mismos PDF);",
f"    {len(falt)} porque el PDF 2 tiene una página repetida y le falta otra (preguntas 101 y 102 incompletas);",
f"    {len(dud)} por clave dudosa (PDF 1, pregunta 112: ovulación tras el pico de LH).",
"- Cada pregunta usa el comentario docente que trae el PDF (al final se añade el resumen «perla» en las del PDF 2).",
"  Solo en una (PDF 2, pregunta 100, clasificación del asma) el comentario faltaba en el PDF y se escribió uno propio.",
"- Se quitaron del comentario las menciones a la academia y frases como «como vimos en clase».",
"- Las preguntas de estos PDF tienen 4 alternativas (A-D), no 5. La web las muestra bien así.",
"- examen_origen: «ENAM Extraordinario 2026 · pregunta oficial» (PDF 1) y «ENAM Extraordinario II 2026 ·",
"  pregunta oficial» (PDF 2); año 2026. Aparecen en los bancos y simuladores del examen ENAM.",
"- Las de Ciencias Básicas llevan su materia en «categoria» (Farmacología, Anatomía, Patología, etc.).",
"- El PDF 2 venía escaneado con marca de agua: se leyó página por página y se transcribió a mano.",
"  Se corrigieron errores de lectura (cifras, unidades, SatO₂, números romanos).",
"- Claves: se revisaron todas y se usó la del PDF.",
"","Cómo instalarlo en Hostinger",
"1. public_html/bancos/: descarga una copia de respaldo de los archivos actuales.",
"2. Sube el ZIP a public_html y usa \"Extraer\" con destino public_html (NO una carpeta nueva).",
"   Acepta reemplazar los archivos.",
"3. Recarga la web con Ctrl+F5.",
f"4. Las {len(N)} preguntas nuevas aún no tienen flujograma propio: \"Ver algoritmo\" muestra el aviso",
"   genérico hasta que se suba el paquete de flujogramas de este bloque.","",
"Preguntas nuevas por especialidad"]
for a,ps in sorted(by.items(),key=lambda kv:-len(kv[1])):
    L.append(f"- {esp[a]} ({a}.json): {len(ps)}  [{ps[0]['id']} a {ps[-1]['id']}]")
    for p in ps: L.append(f"    {p['id']}  {p['tema']}  ({'PDF 1' if p['pdf']=='PDF1' else 'PDF 2'}, n.º {p['n']})")
    L.append("")
L+=["Preguntas omitidas"]
for c in exc: L.append(f"- {'PDF 1' if c['src']=='PDF1' else 'PDF 2'}, n.º {c['n']}: {c['excluida']}")
for (s,n),ref in sorted(DUP.items()): L.append(f"- {'PDF 1' if s=='PDF1' else 'PDF 2'}, n.º {n}: repite el concepto de {ref}")
open("zip26/LEEME.txt","w").write("\n".join(L).rstrip()+"\n")
print("\n".join(L[:30]))
