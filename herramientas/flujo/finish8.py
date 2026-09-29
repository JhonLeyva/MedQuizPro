import json, os, re, shutil, html
from collections import Counter

order = json.load(open("out8/order.json"))
N = len(order)
assert N == 134, N
P = "out8/pack"
shutil.rmtree(P, ignore_errors=True)
shutil.copytree("out8/flujogramas", P + "/flujogramas")

# algoritmos.js: 1579 anteriores (paquete del bloque 7) + 134 nuevas
base = open("out7/pack/algoritmos.js").read().rstrip()
assert base.endswith("};"), base[-20:]
prev = re.findall(r'^  "([A-Z]+-\d+)": \{', base, re.M)
assert len(prev) == 1579, len(prev)
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
TOT = 1579 + N
assert len(re.findall(r'^  "([A-Z]+-\d+)": \{', out, re.M)) == TOT

# galería del bloque 8
NOM = {"arbol": "árbol", "termometro": "termómetro"}
t6 = open("../site/verificar-flujogramas-bloque6.html").read()
head = t6[: t6.index('<div class="grid">') + len('<div class="grid">')]
tail = t6[t6.index("</div>\n<script>"):]
head = head.replace("bloque 6", "bloque 8").replace("500 flujogramas", "%d flujogramas" % N).replace("/ 500", "/ %d" % N)
assert "500" not in head
cards = []
for i, a, t, tipo in order:
    src = "flujogramas/" + a + ".svg"
    te = html.escape(t)
    cards.append('<figure class="card"><figcaption><span class="badge">%s</span> <span class="tipo">%s</span> <b>%s</b></figcaption><a href="%s" target="_blank"><img loading="lazy" src="%s" alt="%s"></a><code>%s</code></figure>'
                 % (i, NOM.get(tipo, tipo), te, src, src, te, src))
open(P + "/verificar-flujogramas-bloque8.html", "w").write(head + "\n" + "\n".join(cards) + "\n" + tail)

# verificador general
g = open("out7/pack/verificar-flujogramas.html").read()
old = "(con los bloques 1 a 7 deben ser 1579)"
assert old in g
g = g.replace(old, "(con los bloques 1 a 8 deben ser %d)" % TOT)
assert "1579" not in g
open(P + "/verificar-flujogramas.html", "w").write(g)

# LEEME
c = Counter(o[3] for o in order)
dis = ", ".join("%s (%d)" % (NOM.get(k, k), n) for k, n in c.most_common())
L = ["MedQuizPro - Flujogramas del bloque 8 (%d preguntas, tema general + caso, 8 diseños)" % N,
     "=" * 86, "", "Contenido",
     "- flujogramas/  -> %d SVG nuevos, uno por cada pregunta del bloque 8." % N,
     "  Diseños: " + dis + ".",
     "  Cada uno trae TEMA GENERAL, CASO CLÍNICO resaltado, puntos clave ENAM y fuente",
     "  (guías MINSA y literatura vigente). Sin etiqueta «✓ RESPUESTA».",
     "  No se borra ni reemplaza ningún SVG existente.",
     "- algoritmos.js -> registro completo: las 1579 entradas anteriores + las %d del bloque 8 (%d en total)." % (N, TOT),
     "- verificar-flujogramas-bloque8.html -> galería para revisar que todo cargue (contador x / %d)." % N,
     "- verificar-flujogramas.html -> el verificador general, actualizado para esperar %d entradas." % TOT,
     "", "Requisitos",
     "- Haber subido los bancos del bloque 8 (MedQuizPro_bloque8_134_preguntas.zip).",
     "- Este algoritmos.js ya incluye todo lo de los bloques 1 a 7.",
     "", "Cómo instalarlo en Hostinger",
     "1. Respaldo: descarga tu algoritmos.js actual.",
     "2. Sube este ZIP directamente a public_html (no a una subcarpeta) y usa \"Extraer\";",
     "   acepta reemplazar archivos. Debe quedar public_html/flujogramas/... y public_html/algoritmos.js.",
     "3. Abre https://lime-louse-621404.hostingersite.com/verificar-flujogramas-bloque8.html",
     "   El contador debe llegar a %d / %d." % (N, N),
     "4. Abre https://lime-louse-621404.hostingersite.com/verificar-flujogramas.html",
     "   Debe decir %d revisados y %d abren bien." % (TOT, TOT),
     "5. En el simulador responde una pregunta del bloque 8 y pulsa \"Ver algoritmo / Flujograma\".",
     "   Si ves la versión anterior, recarga con Ctrl+F5.", "", "Flujogramas por pregunta"]
L += ["  %-8s flujogramas/%s.svg" % (i, a) for i, a, _, _ in order]
open(P + "/LEEME.txt", "w").write("\n".join(L) + "\n")
print("pack ok", len(os.listdir(P + "/flujogramas")), dis)
