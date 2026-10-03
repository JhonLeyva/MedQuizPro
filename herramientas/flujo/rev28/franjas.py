"""Recorta la franja «Así se ve en este caso» de cada PNG y arma hojas para revisar las marcas.
Uso: python3 rev28/franjas.py <dir_salida_build> <hoja.png> [IDs...]"""
import json, re, sys
from PIL import Image
out, hoja = sys.argv[1], sys.argv[2]
order = json.load(open(out + "/order.json"))
ids = sys.argv[3:]
recs = []
for o in order:
    if ids and o[0] not in ids:
        continue
    svg = open(f"{out}/flujogramas/{o[1]}.svg").read()
    m = re.search(r'<text x="[\d.]+" y="([\d.]+)"[^>]*><tspan[^>]*>ASÍ SE VE EN ESTE CASO<', svg)
    if not m:
        continue
    y = float(m.group(1))
    im = Image.open(f"{out}/png/{o[1]}.png")
    k = im.width / 1000
    recs.append(im.crop((0, int((y - 14) * k), im.width, min(im.height, int((y + 470) * k)))).resize((700, int(484 * 0.7))))
if recs:
    H = sum(r.height for r in recs) + 8 * len(recs)
    c = Image.new("RGB", (700, H), "white")
    yy = 0
    for r in recs:
        c.paste(r, (0, yy)); yy += r.height + 8
    c.save(hoja)
print(len(recs))
