"""Superpone una cuadrícula al 10 % (con rótulos) para ubicar marcas. Uso: python3 grid.py <imagen> <salida.png> [x0 y0 x1 y1]"""
import sys
from PIL import Image, ImageDraw
im = Image.open(sys.argv[1]).convert("RGB")
if len(sys.argv) > 3:
    im = im.crop(tuple(int(v) for v in sys.argv[3:7]))
im.thumbnail((700, 700))
d = ImageDraw.Draw(im)
W, H = im.size
for k in range(1, 10):
    x, y = W * k / 10, H * k / 10
    d.line([(x, 0), (x, H)], fill=(255, 0, 255), width=1)
    d.line([(0, y), (W, y)], fill=(255, 0, 255), width=1)
    d.text((x + 2, 2), f".{k}", fill=(255, 255, 0))
    d.text((2, y + 2), f".{k}", fill=(255, 255, 0))
im.save(sys.argv[2])
print(im.size)
