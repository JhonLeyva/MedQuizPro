"""Hoja de revisión: une los PNG pedidos reducidos (ancho 500) en columnas. Uso: python3 hoja.py <dir_png> <salida> archivo1 archivo2 ... [--desde y0 --hasta y1]"""
import sys
from PIL import Image
d, out, fs = sys.argv[1], sys.argv[2], sys.argv[3:]
ims = [Image.open(f"{d}/{f}.png").convert("RGB") for f in fs]
ims = [i.resize((500, int(i.height * 500 / i.width))) for i in ims]
H = max(i.height for i in ims)
o = Image.new("RGB", (510 * len(ims), H), "white")
for k, i in enumerate(ims):
    o.paste(i, (k * 510, 0))
o.save(out)
print(o.size)
