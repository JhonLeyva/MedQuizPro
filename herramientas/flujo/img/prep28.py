"""Imágenes reales de la revisión completa (entrega 1). Lee orig/ y escribe JPG finales.
Cambios a las originales: recorte, tamaño, escala de grises en radiología y, donde se indica, se borraron
líneas, letras o rótulos del autor para poner marcas propias en español."""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from prep import guardar


def rellenar(im, m, crecer=5):
    """Borra la zona m (máscara booleana) rellenándola desde los píxeles vecinos."""
    if crecer:
        m = np.array(Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MaxFilter(crecer))) > 0
    a = np.array(im).astype(float)
    if a.ndim == 2:
        a = a[..., None]
    known = ~m
    for _ in range(300):
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


def segmento(shape, p0, p1, ancho):
    """Máscara de los píxeles a menos de «ancho» del segmento p0-p1."""
    yy, xx = np.mgrid[0:shape[0], 0:shape[1]]
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    t = ((xx - x0) * dx + (yy - y0) * dy) / (dx * dx + dy * dy)
    t = t.clip(0, 1)
    return np.hypot(xx - (x0 + t * dx), yy - (y0 + t * dy)) < ancho


SOLO = sys.argv[1:]


def hacer(nombre):
    return not SOLO or nombre in SOLO


# ── tanda 00
if hacer("hsa_tc.jpg"):
    # TC de hemorragia subaracnoidea (George Jallo, CC BY-SA 3.0): se borra la línea negra que trazó el autor
    im = Image.open("orig/hsa_tc.jpg").convert("L")
    a = np.array(im)
    m = segmento(a.shape, (63, 139.5), (378, 437.7), 2.4)   # recta ajustada a los píxeles de la línea
    im = rellenar(im, m, 3)
    guardar(im.crop((20, 60, 456, 560)), "hsa_tc.jpg", 436, 85)
if hacer("helecho.jpg"):
    # Test del helecho positivo (Paul_012, CC BY-SA 2.0): recorte del campo del microscopio
    guardar(Image.open("orig/helecho.jpg").convert("RGB").crop((190, 160, 770, 740)), "helecho.jpg", 460, 82)
if hacer("ferropenia.jpg"):
    # Frotis de anemia ferropénica (Ed Uthman, CC BY 2.0): recorte
    guardar(Image.open("orig/ferropenia.jpg").convert("RGB").crop((250, 40, 820, 470)), "ferropenia.jpg", 560, 85)
if hacer("hiperk_ecg.jpg"):
    # ECG de hiperpotasemia de 8,2 mmol/L (Agbayani y Gonzales, CC BY 4.0): derivaciones V2 a V4
    guardar(Image.open("orig/hiperk_ecg.jpg").convert("RGB").crop((470, 128, 958, 410)), "hiperk_ecg.jpg", 488, 85)
if hacer("linfo_reactivo.jpg"):
    # Linfocito reactivo (SpicyMilkBoy, CC BY-SA 4.0)
    guardar(Image.open("orig/linfo_reactivo.jpg").convert("RGB"), "linfo_reactivo.jpg", 420, 85)
if hacer("rubeola.jpg"):
    # Exantema de rubéola en la espalda (CDC, dominio público): sin los glúteos
    guardar(Image.open("orig/rubeola.jpg").convert("RGB").crop((0, 0, 500, 520)), "rubeola.jpg", 420, 85)
if hacer("emh_rx.jpg"):
    # Rx de enfermedad de membrana hialina, 29 semanas (Mikael Häggström, CC0)
    guardar(Image.open("orig/emh_rx.png").convert("L").crop((60, 40, 900, 700)), "emh_rx.jpg", 520, 85)
