import json, os, re, shutil, html
from collections import Counter

order = json.load(open("outcb/order.json"))
N = len(order)
assert N == 393, N
P = "outcb/pack"
shutil.rmtree(P, ignore_errors=True)
shutil.copytree("outcb/flujogramas", P + "/flujogramas")

# algoritmos.js: 1713 anteriores (paquete del bloque 8) + 393 de Ciencias Básicas
base = open("out8/pack/algoritmos.js").read().rstrip()
assert base.endswith("};"), base[-20:]
prev = re.findall(r'^  "([A-Z]+-\d+)": \{', base, re.M)
assert len(prev) == 1713, len(prev)
assert not set(prev) & {o[0] for o in order}
body = base[: base.rfind("};")].rstrip()
nuevas = []
for i, a, t, _ in order:
    nuevas.append('  %s: {\n    titulo: %s,\n    imagen: %s,\n    alt: %s\n  }' % (
        json.dumps(i), json.dumps(t, ensure_ascii=False),
        json.dumps("flujogramas/" + a + ".svg"),
        json.dumps("Flujograma: " + t, ensure_ascii=False)))
out = body + ",\n" + ",\n".join(nuevas) + "\n};\n"
open(P + "/algoritmos.js", "w").write(out)
TOT = 1713 + N
assert len(re.findall(r'^  "([A-Z]+-\d+)": \{', out, re.M)) == TOT

# galería de Ciencias Básicas
NOM = {"arbol": "árbol", "termometro": "termómetro"}
t6 = open("../site/verificar-flujogramas-bloque6.html").read()
head = t6[: t6.index('<div class="grid">') + len('<div class="grid">')]
tail = t6[t6.index("</div>\n<script>"):]
head = head.replace("del bloque 6", "de Ciencias Básicas (bloque CB)").replace("bloque 6", "Ciencias Básicas (bloque CB)").replace("500 flujogramas", "%d flujogramas" % N).replace("/ 500", "/ %d" % N)
assert "500" not in head
cards = []
for i, a, t, tipo in order:
    src = "flujogramas/" + a + ".svg"
    te = html.escape(t)
    cards.append('<figure class="card"><figcaption><span class="badge">%s</span> <span class="tipo">%s</span> <b>%s</b></figcaption><a href="%s" target="_blank"><img loading="lazy" src="%s" alt="%s"></a><code>%s</code></figure>'
                 % (i, NOM.get(tipo, tipo), te, src, src, te, src))
open(P + "/verificar-flujogramas-bloquecb.html", "w").write(head + "\n" + "\n".join(cards) + "\n" + tail)

# verificador general
g = open("out8/pack/verificar-flujogramas.html").read()
old = "(con los bloques 1 a 8 deben ser 1713)"
assert old in g
g = g.replace(old, "(con los bloques 1 a 8 y Ciencias Básicas deben ser %d)" % TOT)
assert "1713" not in g
open(P + "/verificar-flujogramas.html", "w").write(g)

# LEEME
c = Counter(o[3] for o in order)
dis = ", ".join("%s (%d)" % (NOM.get(k, k), n) for k, n in c.most_common())
L = ["MedQuizPro - Flujogramas de Ciencias Básicas (%d preguntas: CB-093 a CB-485, 8 diseños)" % N,
     "=" * 86, "", "Contenido",
     "- flujogramas/  -> %d SVG nuevos, uno por cada pregunta nueva de Ciencias Básicas." % N,
     "  Diseños: " + dis + ".",
     "  Cada uno trae TEMA GENERAL, CASO o pregunta resaltada, puntos clave ENAM y fuente",
     "  (textos de referencia y guías vigentes). Sin etiqueta «✓ RESPUESTA».",
     "  No se borra ni reemplaza ningún SVG existente.",
     "- algoritmos.js -> registro completo: las 1713 entradas anteriores + las %d nuevas (%d en total)." % (N, TOT),
     "- verificar-flujogramas-bloquecb.html -> galería para revisar que todo cargue (contador x / %d)." % N,
     "- verificar-flujogramas.html -> el verificador general, actualizado para esperar %d entradas." % TOT,
     "", "Requisitos",
     "- Haber subido el banco nuevo de Ciencias Básicas (ciencias_basicas.json con 485 preguntas).",
     "- Este algoritmos.js ya incluye todo lo de los bloques 1 a 8.",
     "", "Cómo instalarlo en Hostinger",
     "1. Respaldo: descarga tu algoritmos.js actual.",
     "2. Sube este ZIP directamente a public_html (no a una subcarpeta) y usa \"Extraer\";",
     "   acepta reemplazar archivos. Debe quedar public_html/flujogramas/... y public_html/algoritmos.js.",
     "3. Abre https://lime-louse-621404.hostingersite.com/verificar-flujogramas-bloquecb.html",
     "   El contador debe llegar a %d / %d." % (N, N),
     "4. Abre https://lime-louse-621404.hostingersite.com/verificar-flujogramas.html",
     "   Debe decir %d revisados y 0 sin pregunta." % TOT,
     "5. En el simulador responde una pregunta nueva de Ciencias Básicas y pulsa \"Ver algoritmo / Flujograma\".",
     "   Si ves la versión anterior, recarga con Ctrl+F5.", "", "Flujogramas por pregunta"]
L += ["  %-8s flujogramas/%s.svg" % (i, a) for i, a, _, _ in order]
open(P + "/LEEME.txt", "w").write("\n".join(L) + "\n")
print("pack ok", len(os.listdir(P + "/flujogramas")), dis)
