"""Imágenes reales de los 4 ejemplos con clasificaciones (lee orig/, escribe JPG finales).
Cambios: recorte, tamaño, escala de grises y borrado del rótulo de hora del equipo."""
import numpy as np
from PIL import Image
from prep import guardar
from PIL import ImageDraw, ImageFilter


def rellenar(im, m, crecer=5):
    """Borra la zona m (máscara booleana) rellenándola desde los píxeles vecinos."""
    if crecer:
        m = np.array(Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MaxFilter(crecer))) > 0
    a = np.array(im).astype(float)
    if a.ndim == 2:
        a = a[..., None]
    known = ~m
    for _ in range(200):
        if known.all():
            break
        s = np.zeros_like(a)
        c = np.zeros(m.shape)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                k = np.roll(np.roll(known, dy, 0), dx, 1)
                s += np.roll(np.roll(a * known[..., None], dy, 0), dx, 1)
                c += k
        fill = (~known) & (c > 0)
        a[fill] = s[fill] / c[fill][:, None]
        known = known | fill
    a = a.clip(0, 255).astype("uint8")
    return Image.fromarray(a[..., 0] if a.shape[2] == 1 else a)


def caja(im, *cajas):
    """Máscara con rectángulos (x0, y0, x1, y1) en píxeles."""
    m = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(m)
    for b in cajas:
        d.rectangle(b, fill=255)
    return np.array(m) > 0



# Edema pulmonar agudo, Rx AP portátil (Frank Gaillard y Jeremy Jones, Radiopaedia, CC BY-SA 3.0):
# se borra el rótulo «@17.00HRS» y se recorta el tórax
im = Image.open("orig/edema_ap.jpg").convert("L")
a = np.array(im)
m = caja(im, (110, 0, 285, 45)) & (a > 140)
im = rellenar(im, m, 5)
guardar(im.crop((30, 20, 930, 740)), "edema_ap.jpg", 600, 85)

# Neumonía del lóbulo medio derecho (James Heilman, CC BY-SA 4.0): escala de grises y recorte
im = Image.open("orig/neumonia_lm.jpg").convert("L")
guardar(im.crop((40, 20, 920, 700)), "neumonia_lm.jpg", 600, 85)
