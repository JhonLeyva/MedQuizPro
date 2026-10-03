"""Imágenes reales de la revisión completa (entrega 1). Lee orig/ y escribe JPG finales.
Cambios a las originales: recorte, tamaño, escala de grises en radiología y, donde se indica, se borraron
líneas, letras o rótulos del autor para poner marcas propias en español."""
import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageFilter
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

# ── tanda 01
if hacer("oma.jpg"):
    # Otitis media aguda, otoscopia (B. Welleschik, CC BY-SA 3.0): recorte del campo
    guardar(Image.open("orig/oma.jpg").convert("RGB").crop((130, 30, 830, 730)), "oma.jpg", 420, 85)
if hacer("tep_ecg.jpg"):
    # ECG en TEP: taquicardia sinusal y bloqueo de rama derecha (Serra et al., CC BY 2.0): V1 a V3
    guardar(Image.open("orig/tep_ecg.jpg").convert("RGB").crop((452, 80, 867, 285)), "tep_ecg.jpg", 415, 88)
if hacer("pcp_rx.jpg"):
    # Neumonía por Pneumocystis, vidrio esmerilado difuso (Allen et al., CC BY 4.0): Rx de la derecha
    guardar(Image.open("orig/pcp_rx.jpg").convert("L").crop((510, 0, 960, 421)), "pcp_rx.jpg", 450, 85)
if hacer("escabiosis.jpg"):
    # Surco de escabiosis (Michael Geary, dominio público)
    guardar(Image.open("orig/escabiosis.jpg").convert("RGB"), "escabiosis.jpg", 420, 85)

# ── tanda 02
if hacer("iam_inferior.jpg"):
    # IAM con ST elevado inferior y de VD (James Heilman, CC BY-SA 3.0): derivaciones de los miembros (I-III, aVR-aVF)
    guardar(Image.open("orig/iam_inferior.jpg").convert("RGB").crop((0, 0, 384, 379)), "iam_inferior.jpg", 384, 88)

# ── tanda 03
if hacer("invaginacion_eco.jpg"):
    # Invaginación intestinal, ecografía con signo de la diana (Kalumet, CC BY-SA 3.0)
    guardar(Image.open("orig/invag2.jpg").convert("L").crop((40, 0, 920, 766)), "invaginacion_eco.jpg", 440, 85)

# ── tanda 05
if hacer("leish.jpg"):
    # Úlcera de leishmaniasis cutánea con regla (Layne Harris, dominio público)
    guardar(Image.open("orig/leish.jpg").convert("RGB"), "leish.jpg", 420, 85)

# ── tanda 07
if hacer("urato.jpg"):
    # Cristales de urato monosódico con luz polarizada y compensador rojo (Gabriel Caponetti, CC BY-SA 3.0)
    guardar(Image.open("orig/urato.jpg").convert("RGB").crop((120, 60, 900, 660)), "urato.jpg", 460, 85)

# ── tanda 08
if hacer("mola.jpg"):
    # Ecografía transvaginal de embarazo molar (Mikael Häggström, CC0): sin los rótulos del equipo
    guardar(Image.open("orig/mola.jpg").convert("L").crop((20, 60, 440, 380)), "mola.jpg", 420, 85)

# ── tanda 09
if hacer("coraliforme_rx.jpg"):
    # Rx simple de abdomen con cálculo coraliforme (Nevit Dilmen, CC BY-SA 3.0): solo el riñón y la pelvis renal
    guardar(Image.open("orig/coraliforme_rx.jpg").convert("L").crop((40, 20, 700, 640)), "coraliforme_rx.jpg", 400, 85)
if hacer("takotsubo.jpg"):
    # Ventriculografía izquierda en sístole (Gangadhar et al., CC BY 2.0): sin el borde negro
    guardar(Image.open("orig/takotsubo.gif").convert("L").crop((40, 120, 930, 920)), "takotsubo.jpg", 420, 85)
if hacer("chancro.jpg"):
    # Chancros de sífilis primaria (CDC/M. Rein, dominio público)
    guardar(Image.open("orig/chancro.jpg").convert("RGB").crop((180, 0, 760, 560)), "chancro.jpg", 400, 85)
if hacer("aedes.jpg"):
    # Aedes aegypti alimentándose (John Ragai, CC BY 2.0): recorte al mosquito
    guardar(Image.open("orig/aedes.jpg").convert("RGB").crop((230, 230, 730, 610)), "aedes.jpg", 420, 85)

# ── tanda 10
if hacer("meningococo.jpg"):
    # Exantema hemorrágico estrellado de meningococcemia en la mano (Glei y Shkurba, dominio público)
    guardar(Image.open("orig/meningococo.jpg").convert("RGB").crop((0, 60, 960, 680)), "meningococo.jpg", 420, 85)

# ── tanda 11
if hacer("cripto.jpg"):
    # Cryptococcus neoformans con tinta china (CDC/Dr. Leanor Haley, dominio público)
    guardar(Image.open("orig/cripto.jpg").convert("RGB").crop((180, 60, 900, 640)), "cripto.jpg", 400, 85)
if hacer("amiloide.jpg"):
    # Amiloide con rojo Congo bajo luz polarizada (Ed Uthman, CC BY 2.0)
    guardar(ImageEnhance.Brightness(Image.open("orig/amiloide.jpg").convert("RGB").crop((150, 150, 850, 850))).enhance(1.8), "amiloide.jpg", 360, 85)

# ── tanda 12
if hacer("piloro.jpg"):
    # Ecografía de estenosis hipertrófica del píloro (Dr Laughlin Dawes, CC BY-SA 4.0): sin el rótulo inferior del equipo
    guardar(Image.open("orig/piloro.jpg").convert("RGB").crop((0, 0, 500, 470)), "piloro.jpg", 360, 85)
if hacer("uip_tc.jpg"):
    # TC de neumonía intersticial usual con panal de abeja (Yale Rosen, CC BY-SA 2.0)
    guardar(Image.open("orig/uip_tc.jpg").convert("L"), "uip_tc.jpg", 430, 85)
