"""Hoja de contacto: python3 hoja.py <dir_png> <salida.png> [ancho_por_celda=560] [columnas=3] [patrón]"""
import sys, glob, os
from PIL import Image, ImageDraw
d, out = sys.argv[1], sys.argv[2]
W = int(sys.argv[3]) if len(sys.argv) > 3 else 560
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 3
pat = sys.argv[5] if len(sys.argv) > 5 else ""
fs = sorted(f for f in glob.glob(d + "/*.png") if pat in f)
tiles = []
for f in fs:
    im = Image.open(f).convert("RGB"); r = W / im.width; im = im.resize((W, int(im.height * r)), Image.LANCZOS)
    t = Image.new("RGB", (W, im.height + 18), "white"); t.paste(im, (0, 18)); ImageDraw.Draw(t).text((4, 3), os.path.basename(f)[:70], fill="red"); tiles.append(t)
rows = (len(tiles) + cols - 1) // cols
rh = [max(t.height for t in tiles[i * cols:(i + 1) * cols]) for i in range(rows)]
sh = Image.new("RGB", (W * cols, sum(rh)), "white"); y = 0
for i in range(rows):
    for j, t in enumerate(tiles[i * cols:(i + 1) * cols]): sh.paste(t, (j * W, y))
    y += rh[i]
sh.save(out); print(sh.size, len(tiles))
