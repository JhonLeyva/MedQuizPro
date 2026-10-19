"""Imágenes reales de la tanda de mejora (500 flujogramas). Lee orig/ y escribe JPG finales.
Cambios hechos a las originales: recorte, tamaño, escala de grises en las imágenes radiológicas y,
donde se indica, se borraron flechas, letras o rótulos en inglés del autor para poner marcas propias en español."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from prep import guardar

G = lambda f: Image.open("orig/" + f).convert("L")
C = lambda f: Image.open("orig/" + f).convert("RGB")


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


# Colangiorresonancia con coledocolitiasis (Hellerhoff, CC BY-SA 3.0): se borran las flechas y letras rojas
im = C("cprm_coledoco.jpg")
a = np.array(im).astype(int)
rojo = (a[..., 0] - a[..., 1] > 60) & (a[..., 0] - a[..., 2] > 60)
guardar(rellenar(im, rojo, 7).convert("L").crop((60, 150, 620, 820)), "cprm_coledoco.jpg", 560, 88)

# Derrame pericárdico, vista subcostal (Ben Smith, UOTW 25, CC BY-SA 4.0): se recorta el ícono y la «P»
im = G("derrame_peric.jpg")
im.paste(0, (378, 30, 430, 100))   # ícono del operador sobre fondo negro
# rótulos del equipo abajo a la izquierda: se borran solo las letras (claras) rellenando con lo vecino
a = np.array(im)
m = np.zeros(a.shape, bool)
m[245:297, 75:140] = a[245:297, 75:140] > 170
im = rellenar(im, m, 3)
im.paste(0, (75, 258, 110, 297))   # restos del ícono del equipo, fuera del abanico
guardar(im.crop((80, 30, 440, 297)), "derrame_subcostal.jpg", 360, 90)
# Alternancia eléctrica en el taponamiento (Jer5150, CC BY-SA 3.0): derivación V1
guardar(G("tamponade_heil.png").crop((60, 462, 400, 548)), "alternancia_v1.jpg", 340, 92)

# Hematoma epidural derecho, TC axial (Hellerhoff, CC BY-SA 4.0)
guardar(G("epi_87w.jpg").crop((60, 0, 460, 450)), "epidural_derecho.jpg", 400, 88)

# Tetralogía de Fallot, esquema rotulado en español (LadyofHats / Pitana, CC BY-SA 4.0): solo la mitad de Fallot
guardar(C("fallot_esquema.png").crop((420, 30, 960, 660)), "fallot_esquema.jpg", 540, 90)

# Tumor de Pancoast derecho (Jmarchn, CC BY-SA 3.0): se borra la «P» del autor
im = G("pancoast_rx.jpg")
guardar(rellenar(im, caja(im, (156, 86, 168, 100)), 3), "pancoast_rx.jpg", 500, 90)
# Síndrome de Horner (Waster, CC BY 2.5): franja de los ojos
guardar(C("horner.jpg").crop((40, 470, 920, 700)), "horner_ojos.jpg", 880, 88)

# Embarazo tubario derecho visto por laparoscopía (Hic et nunc, CC BY-SA 3.0)
guardar(C("ectopico_tubal.jpg"), "ectopico_tubario.jpg", 760, 86)

# Encefalopatía de Wernicke, RM FLAIR (CC BY-SA 3.0): tálamos mediales hiperintensos
guardar(G("wernicke_rm.jpg").crop((60, 120, 440, 560)), "wernicke_flair.jpg", 380, 90)

# Esquistocitos en la PTT (Hospital Universitario de Berna, CC BY-SA 4.0): círculos azules del autor
guardar(C("esquistocitos.jpg"), "esquistocitos.jpg", 330, 92)

# Desprendimiento de placenta, pieza quirúrgica (Mikael Häggström, CC0): sin la regla con texto
guardar(C("dpp_original.jpg").crop((0, 20, 760, 500)), "dpp_pieza.jpg", 760, 86)

# Neumonía del lóbulo inferior izquierdo con derrame (James Heilman, CC BY 3.0):
# se borran el círculo negro y los textos del equipo
im = G("neumonia_lll.jpg")
m = Image.new("L", im.size, 0)
ImageDraw.Draw(m).ellipse((718, 511, 950, 709), outline=255, width=4)
m = np.array(m) > 0
guardar(rellenar(im, m, 5).crop((95, 0, 900, 720)), "neumonia_lii.jpg", 805, 88)
