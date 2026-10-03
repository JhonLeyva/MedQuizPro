"""Imágenes reales de la Entrega 2. Lee orig/ y escribe JPG finales (recorte, tamaño, grises en radiología; donde se
indica se borraron flechas o letras del autor para poner marcas propias en español).
Uso: python3 prep29.py [archivo.jpg ...]  (sin argumentos rehace todas)"""
import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageFilter
from prep import guardar

SOLO = set(sys.argv[1:])


def hacer(nombre):
    return not SOLO or nombre in SOLO


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



def borrar_oscuro(im, cajas, umbral=70):
    """Borra lo oscuro (flechas o letras negras del autor) dentro de las cajas (x0, y0, x1, y1)."""
    g = np.array(im.convert("L"))
    m = np.zeros(g.shape, bool)
    for x0, y0, x1, y1 in cajas:
        m[y0:y1, x0:x1] = g[y0:y1, x0:x1] < umbral
    return rellenar(im, m, 7)


def lado(archivos, salida, alto, sep=12, fondo=(255, 255, 255), q=86):
    """Une imágenes ya preparadas lado a lado, al mismo alto (para que el crédito común quepa debajo)."""
    ims = [Image.open(a).convert("RGB") for a in archivos]
    ims = [im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS) for im in ims]
    out = Image.new("RGB", (sum(im.width for im in ims) + sep * (len(ims) - 1), alto), fondo)
    x = 0
    for im in ims:
        out.paste(im, (x, 0))
        x += im.width + sep
    out.save(salida, "JPEG", quality=q, optimize=True)
    print(salida, out.size)


# ── tanda 00
if hacer("volvulo_rx.jpg"):
    # Vólvulo de sigmoides en grano de café (Mont4nha, CC0)
    guardar(Image.open("orig/volvulo_rx.jpg").convert("L").crop((0, 0, 500, 590)), "volvulo_rx.jpg", 420, 85)
if hacer("atelectasia_rx.jpg"):
    # Atelectasia del pulmón derecho (Pabloes, CC BY-SA 3.0)
    guardar(Image.open("orig/atelectasia_rx.jpg").convert("L"), "atelectasia_rx.jpg", 460, 85)
if hacer("falcip.jpg"):
    # P. falciparum: gametocito en banana y anillo (Jenkayaks, CC BY-SA 3.0); se borraron las flechas negras del autor
    im = borrar_oscuro(Image.open("orig/falcip.jpg").convert("RGB"), [(470, 50, 565, 172), (615, 485, 710, 610)])
    guardar(im.crop((150, 0, 960, 723)), "falcip.jpg", 460, 85)
if hacer("vivax_troz.jpg"):
    # P. vivax: trofozoítos (CDC/PHIL 2720, dominio público)
    guardar(Image.open("orig/vivax_troz.jpg").convert("RGB"), "vivax_troz.jpg", 460, 85)
if hacer("hiperseg.jpg"):
    # Neutrófilos hipersegmentados (Osaro Erhabor, CC BY-SA 4.0): recorte al neutrófilo de arriba
    guardar(Image.open("orig/hiperseg.jpg").convert("RGB").crop((120, 0, 620, 400)), "hiperseg.jpg", 440, 85)
if hacer("lmc_frotis.jpg"):
    # LMC: leucocitosis con desviación izquierda (P. H. Orlandi Mourao, CC BY-SA 3.0)
    guardar(Image.open("orig/lmc_frotis.jpg").convert("RGB"), "lmc_frotis.jpg", 460, 85)
if hacer("romana.jpg"):
    # Signo de Romaña (PLOS NTD, CC BY 4.0): solo la zona del ojo (sin rostro identificable), ampliada
    im = Image.open("orig/romana.jpg").convert("RGB").crop((488, 252, 630, 442))
    guardar(im.resize((im.width * 2, im.height * 2), Image.LANCZOS), "romana.jpg", 368, 88)
if hacer("triatoma.jpg"):
    # Triatoma infestans picando (CDC/OMS, dominio público)
    guardar(Image.open("orig/triatoma.jpg").convert("RGB").crop((120, 60, 900, 560)), "triatoma.jpg", 460, 85)
if hacer("pilonidal.jpg"):
    # Absceso pilonidal en el surco interglúteo (Jonathanlund, CC BY-SA 4.0)
    guardar(Image.open("orig/pilonidal.jpg").convert("RGB").crop((60, 120, 900, 1180)), "pilonidal.jpg", 400, 85)
if hacer("lipemia_tubo.jpg"):
    # Suero lechoso en un tubo (Mark-shea, dominio público)
    guardar(Image.open("orig/lipemia_tubo.jpg").convert("RGB").crop((60, 0, 440, 1277)), "lipemia_tubo.jpg", 200, 85)
if hacer("placenta_previa.jpg"):
    # Placenta previa (BruceBlaus, CC BY-SA 4.0): panel inferior, sin el rótulo en inglés
    guardar(Image.open("orig/placenta_previa.png").convert("RGB").crop((0, 560, 740, 940)), "placenta_previa.jpg", 460, 88)
if hacer("epistaxis.jpg"):
    # Epistaxis anterior (Welleschik, CC BY-SA 3.0): nariz y boca, sin ojos
    guardar(Image.open("orig/epistaxis.jpg").convert("RGB").crop((150, 0, 500, 375)), "epistaxis.jpg", 380, 85)
if hacer("hiperseg2.jpg"):
    # Neutrófilo hipersegmentado (Ed Uthman, CC BY 2.0), ampliado
    im = Image.open("orig/hiperseg2.jpg").convert("RGB")
    guardar(im.resize((round(im.width * 1.4), round(im.height * 1.4)), Image.LANCZOS), "hiperseg2.jpg", 442, 88)
if hacer("xantoma_erup.jpg"):
    # Xantomas eruptivos en el brazo (Walker, An introduction to dermatology 1905, dominio público): zona del codo
    guardar(Image.open("orig/xantoma_erup.jpg").convert("RGB").crop((0, 0, 330, 640)), "xantoma_erup.jpg", 330, 85)
if hacer("xantoma_tubo.jpg"):
    # Xantomas eruptivos (Walker 1905) + suero lechoso (Mark-shea), ambos de dominio público
    lado(["xantoma_erup.jpg", "lipemia_tubo.jpg"], "xantoma_tubo.jpg", 520, fondo=(255, 255, 255))
if hacer("romana_triatoma.jpg"):
    # Signo de Romaña (PLOS NTD, CC BY 4.0) + Triatoma infestans (CDC/OMS, dominio público)
    lado(["romana.jpg", "triatoma.jpg"], "romana_triatoma.jpg", 330, fondo=(255, 255, 255))
