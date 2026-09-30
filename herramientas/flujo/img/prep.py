"""Prepara las imágenes reales (licencia libre) que van incrustadas en los flujogramas.
Lee orig/ (bajadas con bajar.sh) y escribe los JPG finales en esta carpeta.
Cambios hechos a las originales: recorte, tamaño, escala de grises en las Rx y,
en la Rx de neumotórax grande, se borró la flecha azul del autor para poner marcas propias."""
import numpy as np
from PIL import Image, ImageFilter


def borrar_azul(im):
    """Quita trazos azules (flechas del autor) rellenando con el gris vecino."""
    a = np.array(im.convert("RGB")).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = (b - r > 35) & (b - g > 25)
    m = np.array(Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MaxFilter(7))) > 0
    out = a.mean(axis=2)
    known = ~m
    for _ in range(80):
        if known.all():
            break
        s = np.zeros_like(out)
        c = np.zeros_like(out)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                s += np.roll(np.roll(out * known, dy, 0), dx, 1)
                c += np.roll(np.roll(known, dy, 0), dx, 1)
        fill = (~known) & (c > 0)
        out[fill] = s[fill] / c[fill]
        known = known | fill
    return Image.fromarray(out.clip(0, 255).astype("uint8"))


def guardar(im, nombre, ancho, q=80):
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    im.save(nombre, "JPEG", quality=q, optimize=True)
    print(nombre, im.size)


# Rx de neumotórax derecho grande (J. Heilman, CC BY 3.0)
guardar(borrar_azul(Image.open("orig/rx_neumotorax_der.jpg")).crop((100, 80, 930, 910)), "rx_neumotorax_grande.jpg", 620)
# Mismo tipo de caso tras el drenaje con tubo (Bonilla et al., CC BY 4.0), panel A derecho
guardar(Image.open("orig/rx_antes_despues.png").convert("L").crop((520, 15, 957, 452)), "rx_tras_drenaje.jpg", 437, 85)
# ECG DII de TSV a 179 lpm (dominio público)
guardar(Image.open("orig/ecg_tsv_d2.jpg").convert("RGB"), "ecg_tsv_d2.jpg", 1400, 78)
# Manchas de Koplik y exantema del sarampión (CDC, dominio público)
guardar(Image.open("orig/koplik.jpg").convert("RGB").crop((120, 50, 400, 254)), "koplik.jpg", 280, 88)
guardar(Image.open("orig/sarampion_exantema.jpg").convert("RGB"), "sarampion_exantema.jpg", 700, 80)
