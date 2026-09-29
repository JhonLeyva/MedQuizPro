import json
from merge import Q, D, X
N = json.load(open("nuevoscb.json"))
cam = [(n, Q[n]["clave"], D[n][1]) for n in sorted(D) if D[n][1] != Q[n]["clave"]]
rep = {n: m for n, m in X.items() if m.startswith("Repite") or m.startswith("Muy similar")}
otr = {n: m for n, m in X.items() if n not in rep}
L = ["MedQuizPro - Banco de Ciencias Básicas (%d preguntas nuevas)" % len(N), "=" * 62, "",
"Qué contiene",
"- bancos/ciencias_basicas.json completo: las 92 preguntas que ya tenía + %d nuevas (%d en total)." % (len(N), 92 + len(N)),
"  Solo cambia ese archivo; las demás especialidades no se tocan.",
"- Origen: PDF \"Banco de preguntas Ciencias Básicas, ed. 2019\" (458 preguntas con su tabla de claves).",
"  En la web aparecen como \"ENAM · Ciencias Básicas 2019\".",
"- Cada pregunta trae un comentario docente nuevo, escrito para esta entrega (el PDF no traía",
"  comentarios): explica por qué la opción correcta lo es, por qué fallan las demás y añade el",
"  dato clínico útil para el ENAM, según la literatura actual y las normas del MINSA.",
"- Se revisaron las 458 una por una:",
"  * %d entraron." % len(N),
"  * %d se omitieron por estar repetidas dentro del mismo PDF o ya publicadas en el banco." % len(rep),
"  * %d se omitieron por estar mal planteadas (opciones sin relación, clave ambigua o varias correctas)." % len(otr),
"  * En %d la clave del PDF estaba equivocada o desactualizada y se usó la correcta:" % len(cam),
"    " + ", ".join("n.º %d (%s→%s)" % c for c in cam) + ".",
"  * Varias preguntas con opciones mal escritas o con dos opciones válidas se corrigieron para",
"    que tengan una sola opción correcta. Las de 4 opciones se completaron a 5.",
"- Texto limpiado: faltas de ortografía, nombres de microorganismos y fármacos, espacios para",
"  completar unificados como ______.", "",
"Cómo instalarlo en Hostinger",
"1. public_html/bancos/: descarga una copia de respaldo de ciencias_basicas.json.",
"2. Sube el ZIP a public_html y usa \"Extraer\" con destino public_html (NO una carpeta nueva).",
"   Acepta reemplazar el archivo.",
"3. Recarga la web con Ctrl+F5.",
"   Las preguntas nuevas aún no tienen flujograma propio: \"Ver algoritmo\" muestra el aviso genérico.", "",
"Preguntas nuevas (%s a %s)" % (N[0]["id"], N[-1]["id"])]
L += ["    %s  %s  (PDF n.º %d)" % (p["id"], p["tema"], p["n"]) for p in N]
L += ["", "Preguntas omitidas"] + ["    n.º %d: %s" % (n, m) for n, m in sorted(X.items())]
open("zipcb/LEEME.txt", "w").write("\n".join(L) + "\n")
print("\n".join(L[:26]))
