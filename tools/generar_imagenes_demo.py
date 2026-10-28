#!/usr/bin/env python3
"""Genera las imágenes SINTÉTICAS de demo/img/ (no son estudios reales de pacientes): un «tórax» y una «serie axial» de 8 cortes, con marca de agua
«EJEMPLO». Sirven solo para probar el visor; en producción se reemplazan por imágenes con licencia que permita su uso (o propias y anonimizadas)."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
SAL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demo", "img"); os.makedirs(SAL, exist_ok=True)
rng = np.random.default_rng(7)
def fuente(n):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(p): return ImageFont.truetype(p, n)
    return ImageFont.load_default()
def marca(img, texto, n):
    capa = Image.new("L", img.size, 0); d = ImageDraw.Draw(capa); f = fuente(n)
    w = d.textlength(texto, font=f); d.text(((img.width - w) / 2, img.height * 0.46), texto, font=f, fill=70)
    capa = capa.rotate(18, resample=Image.BICUBIC); return Image.fromarray(np.clip(np.asarray(img, dtype=np.int16) + np.asarray(capa, dtype=np.int16) * 0.9, 0, 255).astype(np.uint8))
def ruido(a, s): return np.clip(a + rng.normal(0, s, a.shape), 0, 255)

# --- «radiografía» sintética 1500 x 1800 ---
W, H = 1500, 1800; im = Image.new("L", (W, H), 22); d = ImageDraw.Draw(im)
d.rounded_rectangle((250, 120, 1250, 1750), 380, fill=70)                                   # contorno del tronco
for lado in (1, -1):                                                                          # campos pulmonares
    cx = W // 2 + lado * 270; d.ellipse((cx - 250, 330, cx + 250, 1380), fill=28)
d.polygon([(690, 330), (810, 330), (860, 1100), (640, 1100)], fill=120)                      # mediastino
d.ellipse((600, 880, 960, 1250), fill=135)                                                    # silueta cardiaca
d.rectangle((715, 120, 785, 420), fill=105)                                                   # tráquea/columna
for k in range(9):                                                                            # costillas
    y = 360 + k * 105
    for lado in (1, -1):
        d.arc((W // 2 - 560 if lado < 0 else W // 2 - 20, y - 70, W // 2 + 20 if lado < 0 else W // 2 + 560, y + 190), 195 if lado < 0 else 300, 345 if lado < 0 else 405, fill=150, width=14)
d.ellipse((500, 1180, 1000, 1420), fill=115)                                                  # diafragma
im = im.filter(ImageFilter.GaussianBlur(7)); a = np.asarray(im, dtype=np.float32)
yy, xx = np.mgrid[0:H, 0:W]; a *= (1 - 0.35 * (((xx - W / 2) / (W / 1.6)) ** 2 + ((yy - H / 2) / (H / 1.6)) ** 2))
im = marca(Image.fromarray(ruido(a, 5).astype(np.uint8)), "EJEMPLO · NO ES UN ESTUDIO REAL", 78)
im.save(os.path.join(SAL, "ejemplo-torax.jpg"), quality=86)

# --- «serie axial» sintética: 8 cortes de 640 x 640 con una «lesión» que crece y se reduce ---
for k in range(8):
    S = 640; c = Image.new("L", (S, S), 12); d = ImageDraw.Draw(c); r = 250 - abs(k - 3.5) * 14
    d.ellipse((S / 2 - r, S / 2 - r * 1.1, S / 2 + r, S / 2 + r * 1.1), fill=190)               # hueso
    d.ellipse((S / 2 - r + 22, S / 2 - r * 1.1 + 22, S / 2 + r - 22, S / 2 + r * 1.1 - 22), fill=92)   # parénquima
    for lado in (1, -1): d.ellipse((S / 2 + lado * 40 - 26, S / 2 - 70, S / 2 + lado * 40 + 26, S / 2 + 20), fill=30)   # ventrículos
    lr = 10 + 30 * np.sin(np.pi * (k + 0.5) / 8); d.ellipse((S / 2 + 90 - lr, S / 2 + 40 - lr, S / 2 + 90 + lr, S / 2 + 40 + lr), fill=170)   # «lesión» hiperdensa
    c = c.filter(ImageFilter.GaussianBlur(2.2)); c = marca(Image.fromarray(ruido(np.asarray(c, dtype=np.float32), 6).astype(np.uint8)), "EJEMPLO", 70)
    c.save(os.path.join(SAL, f"ejemplo-serie-{k + 1}.jpg"), quality=88)
print("listo:", sorted(os.listdir(SAL)))
