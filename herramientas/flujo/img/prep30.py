"""Imágenes reales de la Entrega 3 (PubMed Central y Wikimedia Commons). Lee orig/ y escribe los JPG finales
(recorte, tamaño, grises en radiología; se borran flechas, círculos y letras del autor para poner marcas propias en español).
Uso: python3 prep30.py [archivo.jpg ...]  (sin argumentos rehace todas)"""
import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from prep import guardar

SOLO = set(sys.argv[1:])


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



def hacer(nombre):
    return not SOLO or nombre in SOLO


def borrar_color(im, cond, crecer=7):
    """Borra los píxeles de color (marcas del autor) que cumplen cond(r, g, b)."""
    a = np.array(im.convert("RGB")).astype(int)
    m = cond(a[..., 0], a[..., 1], a[..., 2])
    return rellenar(im.convert("RGB"), m, crecer)


AMARILLO = lambda r, g, b: (r > 140) & (g > 120) & (b < 110) & (r - b > 70)
OSCURO_AZUL = lambda r, g, b: (b > r + 25) & (b > 60)
ROJO = lambda r, g, b: (r > 150) & (g < 90) & (b < 90)

# ── CIR-080 · TC de diverticulitis por estadio de Hinchey (Papaoikonomou et al., Cureus 2025, PMC12857236, CC BY 4.0)
if hacer("hinchey0_tc.jpg") or hacer("hinchey1b_tc.jpg"):
    # se conservan los círculos y la flecha amarillos del autor (sin texto): señalan lo que se rotula en español
    o = Image.open("orig/hinchey_tc.jpg").convert("RGB")
    guardar(o.crop((8, 6, 368, 280)), "hinchey0_tc.jpg", 540, 88)
    guardar(o.crop((8, 312, 386, 586)), "hinchey1b_tc.jpg", 560, 88)
    guardar(o.crop((400, 4, 748, 282)), "hinchey1a_tc.jpg", 540, 88)
if hacer("hinchey2_tc.jpg"):
    # la línea amarilla es la medida del autor (9 cm); se recorta el panel A sin la letra
    o = Image.open("orig/hinchey2_drenaje.jpg").convert("RGB")
    guardar(o.crop((30, 8, 345, 262)), "hinchey2_tc.jpg", 470, 88)

# ── PED-142 · Retinopatía del prematuro (Zhao et al., Sci Data 2024, PMC11130119, CC BY 4.0): estadios y láser
if hacer("rop_estadios.jpg"):
    o = Image.open("orig/rop_estadios.jpg").convert("RGB")
    # paneles: a normal, c estadio 2 (cresta), d estadio 3 (proliferación), e láser reciente; se tapan las letras
    pan = {"a": (0, 0, 248, 188), "c": (500, 0, 750, 188), "d": (0, 196, 248, 382), "e": (252, 196, 498, 382)}
    for k, (x0, y0, x1, y1) in pan.items():
        p = o.crop((x0 + 2, y0 + 2, x1 - 2, y1 - 2))
        a = np.array(p)
        h, w = a.shape[:2]
        yy, xx = np.mgrid[:h, :w]
        a[(xx - w / 2) ** 2 + (yy - h / 2) ** 2 > 125 ** 2] = 0   # máscara circular: tapa la letra del panel
        guardar(Image.fromarray(a), f"rop_{k}.jpg", 330, 88)
if hacer("rop_plus.jpg"):
    # enfermedad plus (Sharafi et al., Int J Retina Vitreous 2025, PMC12639888, CC BY 4.0), panel superior izquierdo
    guardar(Image.open("orig/rop_plus.jpg").convert("RGB").crop((10, 0, 392, 296)), "rop_plus.jpg", 420, 88)

# ── TRA-028 · Rx lateral lumbar con fractura por compresión (en cuña) de L4 (James Heilman, Commons, CC BY-SA 3.0)
if hacer("cuna_l4.jpg"):
    o = Image.open("orig/l4_compresion.jpg").convert("L")
    guardar(ImageEnhance.Contrast(o.crop((170, 140, 800, 880))).enhance(1.15), "cuna_l4.jpg", 520, 88)
# ── TRA-028 · DXA lumbar con osteoporosis, ya en español (Jmarchn, Commons, CC BY-SA 3.0)
if hacer("dxa_lumbar.jpg"):
    guardar(Image.open("orig/dxa_lumbar.png").convert("RGB"), "dxa_lumbar.jpg", 772, 92)
    guardar(Image.open("orig/dxa_lumbar.png").convert("RGB").crop((358, 0, 772, 401)), "dxa_grafico.jpg", 414, 93)

# ── INF-070 · Mordedura de perro en el dorso de la mano (Assianir, Commons, CC BY-SA 3.0); sin EXIF
if hacer("mordida_perro.jpg"):
    o = Image.open("orig/morso_cane.jpg").convert("RGB")
    guardar(Image.fromarray(np.array(o.crop((0, 260, 820, 1180)))), "mordida_perro.jpg", 520, 86)
