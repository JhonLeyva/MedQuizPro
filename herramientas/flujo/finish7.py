import json, os, re, shutil, html
from collections import Counter

order = json.load(open("out7/order.json"))
assert len(order) == 500, len(order)
P = "out7/pack"
shutil.rmtree(P, ignore_errors=True)
shutil.copytree("out7/flujogramas", P + "/flujogramas")

# algoritmos.js: 1079 anteriores + 500 nuevas
base = open("base1079.js").read().rstrip()
assert base.endswith("}\n};") or base.endswith("};"), base[-20:]
prev = re.findall(r'^  "([A-Z]+-\d+)": \{', base, re.M)
assert len(prev) == 1079, len(prev)
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
assert len(re.findall(r'^  "([A-Z]+-\d+)": \{', out, re.M)) == 1579

# galería del bloque 7
NOM = {"arbol": "árbol", "termometro": "termómetro"}
t6 = open("../site/verificar-flujogramas-bloque6.html").read()
head = t6[: t6.index('<div class="grid">') + len('<div class="grid">')]
tail = t6[t6.index("</div>\n<script>"):]
head = head.replace("bloque 6", "bloque 7")
cards = []
for i, a, t, tipo in order:
    src = "flujogramas/" + a + ".svg"
    te = html.escape(t)
    cards.append('<figure class="card"><figcaption><span class="badge">%s</span> <span class="tipo">%s</span> <b>%s</b></figcaption><a href="%s" target="_blank"><img loading="lazy" src="%s" alt="%s"></a><code>%s</code></figure>'
                 % (i, NOM.get(tipo, tipo), te, src, src, te, src))
open(P + "/verificar-flujogramas-bloque7.html", "w").write(head + "\n" + "\n".join(cards) + "\n" + tail)

# verificador general
g = open("vgen6.html").read()
old = "(con los bloques 1 a 6 deben ser 1079)"
assert old in g
g = g.replace(old, "(con los bloques 1 a 7 deben ser 1579)")
assert "1079" not in g, "queda 1079 en el verificador"
open(P + "/verificar-flujogramas.html", "w").write(g)

# LEEME
c = Counter(o[3] for o in order)
dis = ", ".join("%s (%d)" % (NOM.get(k, k), n) for k, n in c.most_common())
L = open("LEEME_flujogramas_bloque6.txt").read()
L = L[: L.index("Flujogramas por pregunta")]
L = L.replace("bloque 6", "bloque 7").replace("bloque6", "bloque7")
L = re.sub(r"  Diseños: .*\n", "  Diseños: " + dis + ".\n", L)
L = L.replace("las 579 entradas anteriores + las 500 del bloque 7 (1079 en total)",
              "las 1079 entradas anteriores + las 500 del bloque 7 (1579 en total)")
L = L.replace("Debe decir 1079 revisados y 1079 abren bien", "Debe decir 1579 revisados y 1579 abren bien")
L = L.replace("bloques 1 a 5", "bloques 1 a 6").replace("esperar 1079 entradas", "esperar 1579 entradas")
L = L.replace("=" * 86, "=" * 86)
assert "1079 revisados" not in L and "579 entradas" not in L.replace("1579", "").replace("1079 entradas", "")
L += "Flujogramas por pregunta\n" + "".join("  %-8s flujogramas/%s.svg\n" % (i, a) for i, a, _, _ in order)
open(P + "/LEEME.txt", "w").write(L)
print("pack ok", len(os.listdir(P + "/flujogramas")), dis)
