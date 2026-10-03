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

# ── tanda 01
if hacer("bronquiolitis_rx.jpg"):
    # Bronquiolitis: hiperinsuflación (Di Nardo et al., CC BY 2.0); sin la letra del borde
    guardar(Image.open("orig/bronquiolitis_rx.jpg").convert("L").crop((0, 0, 342, 333)), "bronquiolitis_rx.jpg", 342, 88)
if hacer("meconio_rx.jpg"):
    # Aspiración de meconio (Kinderradiologie Olgahospital Stuttgart, CC BY-SA 4.0); sin el texto superior
    guardar(Image.open("orig/meconio_rx.jpg").convert("L").crop((0, 28, 744, 740)), "meconio_rx.jpg", 440, 85)
if hacer("mallory.jpg"):
    # Desgarro de Mallory-Weiss con coágulo (Doctor roach, CC BY-SA 4.0)
    guardar(Image.open("orig/mallory.jpg").convert("RGB"), "mallory.jpg", 440, 85)
if hacer("retinopatia.jpg"):
    # Retinopatía diabética (Hao et al., CC BY 4.0); sin la letra del panel
    guardar(Image.open("orig/retinopatia.png").convert("RGB").crop((60, 0, 860, 730)), "retinopatia.jpg", 420, 85)
if hacer("mantoux.jpg"):
    # Aplicación de la tuberculina (Greg Knobloch/CDC, dominio público)
    guardar(Image.open("orig/mantoux.jpg").convert("RGB").crop((0, 60, 960, 630)), "mantoux.jpg", 440, 85)
if hacer("toxo_rm.jpg"):
    # Toxoplasmosis cerebral en sida, RM FLAIR (Jmarchn, CC BY-SA 3.0)
    guardar(Image.open("orig/toxo_rm.png").convert("L").crop((10, 60, 490, 600)), "toxo_rm.jpg", 400, 85)
if hacer("giardia.jpg"):
    # Giardia: trofozoíto (Stefan Walkowski, CC BY-SA 4.0)
    guardar(Image.open("orig/giardia.jpg").convert("RGB").crop((0, 0, 500, 440)), "giardia.jpg", 420, 85)
if hacer("atresia_rx.jpg"):
    # Atresia esofágica: bolsa ciega con contraste y aire gástrico (Nevit Dilmen, CC BY-SA 3.0)
    guardar(Image.open("orig/atresia_rx.jpg").convert("L").crop((100, 0, 900, 1300)), "atresia_rx.jpg", 320, 85)
if hacer("janeway.jpg"):
    # Lesiones de Janeway en la palma (Warfieldian, CC BY-SA 4.0)
    guardar(Image.open("orig/janeway.jpg").convert("RGB"), "janeway.jpg", 440, 85)
if hacer("periamig.jpg"):
    # Absceso periamigdalino derecho (James Heilman, CC BY-SA 3.0); se borró la flecha azul del autor
    im = Image.open("orig/periamig.jpg").convert("RGB")
    a = np.array(im).astype(int)
    m = (a[..., 2] > a[..., 0] + 30) & (a[..., 2] > a[..., 1] + 10)
    m[:, :350] = False
    m[700:, :] = False
    guardar(rellenar(im, m, 7).crop((0, 80, 960, 1123)), "periamig.jpg", 400, 85)
if hacer("ascitis.jpg"):
    # Ascitis masiva por cirrosis (James Heilman, CC BY-SA 3.0)
    guardar(Image.open("orig/ascitis.jpg").convert("RGB"), "ascitis.jpg", 420, 85)
if hacer("cilindro_granuloso.jpg"):
    # Cilindro granuloso «pardo» de la necrosis tubular (Mohsenin, CC BY 4.0), panel b ampliado
    im = Image.open("orig/cilindros4.jpg").convert("RGB").crop((274, 2, 498, 134))
    guardar(im.resize((im.width * 2, im.height * 2), Image.LANCZOS), "cilindro_granuloso.jpg", 440, 88)

# ── tanda 02
if hacer("polipo.jpg"):
    # Pólipo pediculado extirpado (RobLekarzMD, CC BY-SA 4.0)
    guardar(Image.open("orig/polipo.jpg").convert("RGB").crop((180, 120, 840, 640)), "polipo.jpg", 420, 85)
if hacer("vcs_venas.jpg"):
    # Síndrome de vena cava superior: venas superficiales dilatadas en el tórax (EMAHkempny, CC BY-SA 4.0); sin rostro
    guardar(Image.open("orig/vcs_venas.jpg").convert("RGB").crop((0, 60, 500, 667)), "vcs_venas.jpg", 360, 85)
if hacer("endometrioma.jpg"):
    # Endometrioma en vidrio esmerilado (Keckstein et al., CC BY 4.0)
    guardar(Image.open("orig/endometrioma.jpg").convert("L").crop((30, 0, 470, 352)), "endometrioma.jpg", 420, 85)
if hacer("urt_colin.jpg"):
    # Habones de urticaria colinérgica (Danielpercy, dominio público)
    guardar(Image.open("orig/urt_colin2.jpg").convert("RGB").crop((0, 100, 960, 1050)), "urt_colin.jpg", 400, 85)
if hacer("apendicitis_eco.jpg"):
    # Apendicitis aguda en la ecografía (Borbély Márton, CC BY-SA 4.0)
    guardar(Image.open("orig/apendicitis_eco.png").convert("L").crop((40, 0, 920, 760)), "apendicitis_eco.jpg", 420, 85)
if hacer("bridas_rx.jpg"):
    # Obstrucción del intestino delgado: asas dilatadas con niveles (Igboeze, CC BY-SA 4.0)
    guardar(Image.open("orig/bridas_rx.jpg").convert("L"), "bridas_rx.jpg", 460, 85)
if hacer("versicolor.jpg"):
    # Pitiriasis versicolor en el abdomen (Sarahrosenau, CC BY-SA 2.0)
    guardar(Image.open("orig/versicolor.jpg").convert("RGB"), "versicolor.jpg", 440, 85)
if hacer("lcn.jpg"):
    # Longitud cráneo-nalga a las 12 semanas (Wolfgang Moroder, CC BY-SA 3.0)
    guardar(Image.open("orig/lcn.jpg").convert("L"), "lcn.jpg", 440, 85)
if hacer("manguito.jpg"):
    # Músculos del manguito rotador (InjuryMap, CC BY-SA 4.0); se borraron los rótulos en inglés para poner los rótulos en español
    a = Image.open("orig/manguito.png").convert("RGBA")
    bg = Image.new("RGBA", a.size, "white")
    bg.alpha_composite(a)
    im = bg.convert("RGB")
    g = np.array(im.convert("L"))
    m = np.zeros(g.shape, bool)
    for x0, y0, x1, y1 in [(170, 35, 300, 64), (650, 35, 790, 64), (415, 74, 548, 102), (415, 258, 538, 290), (415, 338, 548, 372), (762, 330, 830, 384)]:
        m[y0:y1, x0:x1] = g[y0:y1, x0:x1] < 150
    guardar(rellenar(im, m, 5), "manguito.jpg", 560, 88)
if hacer("cara_mp.jpg"):
    # Presentación de cara mentoposterior (Hirst 1898, dominio público); sin la leyenda
    guardar(Image.open("orig/cara_mp.jpg").convert("L").crop((10, 8, 322, 300)), "cara_mp.jpg", 312, 88)

# ── tanda 03
if hacer("ictericia.jpg"):
    # Ictericia de las escleras en hepatitis A (dominio público): solo la franja de los ojos
    guardar(Image.open("orig/ictericia.jpg").convert("RGB").crop((300, 150, 780, 300)), "ictericia.jpg", 440, 85)
if hacer("strongy.jpg"):
    # Larva rabditoide de Strongyloides stercoralis (CDC, dominio público)
    guardar(Image.open("orig/strongy2.jpg").convert("RGB"), "strongy.jpg", 460, 85)
if hacer("lazo.jpg"):
    # Prueba del lazo positiva en dengue (CDC, dominio público)
    im = Image.open("orig/lazo.gif").convert("RGB")
    guardar(im.resize((im.width * 4 // 3, im.height * 4 // 3), Image.LANCZOS), "lazo.jpg", 440, 85)
if hacer("russell.jpg"):
    # Signo de Russell en los nudillos (Kyukyusha, dominio público); sin el rótulo en inglés
    guardar(Image.open("orig/russell.png").convert("RGB").crop((40, 430, 960, 1120)), "russell.jpg", 400, 85)
if hacer("midriasis.jpg"):
    # Midriasis bilateral (Soldier of Wasteland, CC BY-SA 4.0)
    guardar(Image.open("orig/midriasis.jpg").convert("RGB"), "midriasis.jpg", 480, 85)
if hacer("saco.jpg"):
    # Embarazo temprano: saco gestacional con embrión (Nevit Dilmen, CC BY-SA 3.0); sin los datos del equipo
    guardar(Image.open("orig/saco.jpg").convert("L").crop((40, 130, 500, 431)), "saco.jpg", 440, 85)
if hacer("pancreatitis_tc.jpg"):
    # Pancreatitis aguda exudativa en la TC (Hellerhoff, CC BY-SA 3.0)
    guardar(Image.open("orig/pancreatitis_tc.jpg").convert("L").crop((0, 60, 960, 808)), "pancreatitis_tc.jpg", 420, 85)
if hacer("zoster_tzanck.jpg"):
    # Herpes zóster en banda (Fixi/Cremer, CC BY-SA 3.0) + Tzanck con células gigantes multinucleadas (NIAID, dominio público)
    guardar(Image.open("orig/zoster.jpg").convert("RGB").crop((0, 40, 500, 572)), "zoster.jpg", 500, 88)
    guardar(Image.open("orig/tzanck.png").convert("RGB"), "tzanck.jpg", 330, 90)
    lado(["zoster.jpg", "tzanck.jpg"], "zoster_tzanck.jpg", 300)
if hacer("ulcera_endo.jpg"):
    # Úlcera gástrica profunda en el antro, endoscopía (Samir, CC BY-SA 3.0)
    a = Image.open("orig/ulcera_endo.png").convert("RGBA")
    bg = Image.new("RGBA", a.size, "black")
    bg.alpha_composite(a)
    guardar(bg.convert("RGB").crop((0, 0, 330, 330)), "ulcera_endo.jpg", 330, 88)

# ── tanda 04
if hacer("cilindro_hematico.jpg"):
    # Cilindro hemático en el sedimento (Mohsenin, CC BY 4.0), panel d ampliado
    im = Image.open("orig/cilindros4.jpg").convert("RGB").crop((272, 152, 498, 296))
    guardar(im.resize((im.width * 2, im.height * 2), Image.LANCZOS), "cilindro_hematico.jpg", 440, 88)
if hacer("papiledema.jpg"):
    # Papiledema grave (Bansal, Dabbs y Long, CC BY 2.0)
    guardar(Image.open("orig/papiledema.jpg").convert("RGB").crop((40, 0, 460, 375)), "papiledema.jpg", 420, 85)
if hacer("tobillo.jpg"):
    # Ligamentos del tobillo, rótulos en español (Servier Medical Art, CC BY 4.0)
    a = Image.open("orig/tobillo.png").convert("RGBA")
    bg = Image.new("RGBA", a.size, "white")
    bg.alpha_composite(a)
    guardar(bg.convert("RGB"), "tobillo.jpg", 560, 88)
if hacer("oxalato.jpg"):
    # Cristales de oxalato de calcio en orina (NASA/JSC, dominio público), zona central ampliada
    im = Image.open("orig/oxalato.jpg").convert("RGB").crop((120, 0, 420, 215))
    guardar(im.resize((im.width * 3 // 2, im.height * 3 // 2), Image.LANCZOS), "oxalato.jpg", 450, 88)
if hacer("coartacion.jpg"):
    # Coartación de aorta (BruceBlaus, CC BY-SA 4.0), panel superior
    guardar(Image.open("orig/coartacion.png").convert("RGB").crop((0, 0, 330, 450)), "coartacion.jpg", 330, 88)
if hacer("hidradenitis.jpg"):
    # Hidradenitis supurativa Hurley II en la axila (Alharbi et al., CC BY 2.5); sin la oreja
    guardar(Image.open("orig/hidradenitis.jpg").convert("RGB").crop((60, 200, 500, 662)), "hidradenitis.jpg", 400, 85)
if hacer("oxiuro.jpg"):
    # Huevo de Enterobius vermicularis (Ajay Kumar Chaurasiya, CC BY 4.0)
    guardar(Image.open("orig/oxiuro.jpg").convert("RGB").crop((300, 0, 960, 420)), "oxiuro.jpg", 440, 85)

# ── tanda 05
if hacer("esporotricosis.jpg"):
    # Esporotricosis linfocutánea del brazo (CDC/Lucille K. Georg, dominio público)
    guardar(Image.open("orig/esporotricosis.jpg").convert("RGB"), "esporotricosis.jpg", 460, 85)
if hacer("diu.jpg"):
    # DIU con levonorgestrel en el útero (Hic et nunc, dominio público)
    guardar(Image.open("orig/diu.jpg").convert("RGB").crop((120, 0, 860, 1047)), "diu.jpg", 320, 88)
if hacer("tvp.jpg"):
    # Trombosis venosa profunda de la pierna derecha (James Heilman, CC BY-SA 3.0); se borró la flecha azul del autor
    im = Image.open("orig/tvp.jpg").convert("RGB")
    a = np.array(im).astype(int)
    m = (a[..., 2] > a[..., 0] + 40) & (a[..., 2] > a[..., 1] + 20)
    guardar(rellenar(im, m, 7).crop((0, 0, 960, 1534)), "tvp.jpg", 300, 85)
if hacer("feo_tc.jpg"):
    # Feocromocitoma suprarrenal izquierdo, TC coronal (Drahreg01, CC BY-SA 3.0)
    guardar(Image.open("orig/feo_tc.jpg").convert("L"), "feo_tc.jpg", 500, 85)
if hacer("lla_real.jpg"):
    # Leucemia linfoblástica aguda B, aspirado de médula (VashiDonsk, CC BY-SA 3.0)
    im = Image.open("orig/lla_real.jpg").convert("RGB")
    guardar(im.resize((im.width * 4 // 3, im.height * 4 // 3), Image.LANCZOS), "lla_real.jpg", 440, 88)
if hacer("gottron.jpg"):
    # Pápulas de Gottron (Dugan, Huber, Miller y Rider, CC BY-SA 3.0); sin la leyenda
    guardar(Image.open("orig/gottron.jpg").convert("RGB").crop((0, 0, 500, 395)), "gottron.jpg", 440, 85)

# ── tanda 06
def _rgba_blanco(ruta):
    a = Image.open(ruta).convert("RGBA")
    bg = Image.new("RGBA", a.size, "white")
    bg.alpha_composite(a)
    return bg.convert("RGB")


if hacer("graf.jpg"):
    # Ángulos de Graf en la ecografía de cadera (Nevit Dilmen, CC BY-SA 3.0)
    guardar(_rgba_blanco("orig/graf.png"), "graf.jpg", 480, 88)
if hacer("megaesofago.jpg"):
    # Megaesófago chagásico con bario (dominio público); sin los números de la placa
    guardar(Image.open("orig/megaesofago.jpg").convert("L").crop((0, 40, 250, 363)), "megaesofago.jpg", 250, 88)
if hacer("hematoma_oreja.jpg"):
    # Hematoma agudo del pabellón auricular (Klaus D. Peter, CC BY 3.0 DE)
    guardar(Image.open("orig/hematoma_oreja.jpg").convert("RGB").crop((60, 120, 900, 1200)), "hematoma_oreja.jpg", 360, 85)
if hacer("petequias.jpg"):
    # Petequias en la pierna en PTI con 3000 plaquetas (James Heilman, CC BY-SA 4.0)
    guardar(Image.open("orig/petequias.jpg").convert("RGB"), "petequias.jpg", 460, 85)
if hacer("ishihara.jpg"):
    # Lámina 9 de Ishihara (dominio público): se lee «74»
    guardar(_rgba_blanco("orig/ishihara.png"), "ishihara.jpg", 360, 88)
if hacer("chagas_ecg_rx.jpg"):
    # ECG de enseñanza (FA, propio) + megaesófago chagásico con bario (dominio público)
    lado(["ecg_fa.jpg", "megaesofago.jpg"], "chagas_ecg_rx.jpg", 300)

# ── tanda 07
if hacer("gonococo.jpg"):
    # Diplococos gramnegativos dentro de un neutrófilo (Graham Beards, CC BY-SA 4.0)
    guardar(Image.open("orig/gonococo.jpg").convert("RGB").crop((120, 60, 840, 640)), "gonococo.jpg", 440, 85)
if hacer("kaposi.jpg"):
    # Sarcoma de Kaposi en la piel (dominio público)
    guardar(Image.open("orig/kaposi.jpg").convert("RGB"), "kaposi.jpg", 460, 85)
if hacer("ferruginoso.jpg"):
    # Cuerpos ferruginosos (de asbesto) en biopsia pulmonar (Nephron, CC BY-SA 3.0)
    guardar(Image.open("orig/ferruginoso.jpg").convert("RGB").crop((0, 80, 960, 900)), "ferruginoso.jpg", 440, 85)
if hacer("colera.jpg"):
    # Heces en «agua de arroz» del cólera (Ajay Kumar Chaurasiya, CC BY-SA 4.0), recipiente ampliado
    guardar(Image.open("orig/colera.jpg").convert("RGB").crop((380, 380, 860, 920)), "colera.jpg", 360, 88)
if hacer("ecg_qt_tdp.jpg"):
    pass   # generado con ecg29.py (qt_largo + torsades)
if hacer("hidronefrosis.jpg"):
    # Cálculo ureteral con hidronefrosis, TC (James Heilman, CC BY-SA 3.0); la flecha roja es del autor
    guardar(Image.open("orig/hidronefrosis.png").convert("RGB").crop((0, 20, 960, 600)), "hidronefrosis.jpg", 460, 85)
if hacer("bota.jpg"):
    # Corazón en bota de la tetralogía de Fallot (Medicalpal, CC BY-SA 4.0)
    guardar(Image.open("orig/bota.jpg").convert("L").crop((0, 80, 960, 1141)), "bota.jpg", 380, 85)
if hacer("hidrocefalia.jpg"):
    # Hidrocefalia: ventrículos muy dilatados en la TC (Hellerhoff, CC BY-SA 4.0), corte axial
    guardar(Image.open("orig/hidrocefalia.jpg").convert("L").crop((0, 0, 480, 460)), "hidrocefalia.jpg", 400, 85)

# ── tanda 08
if hacer("strep_petequias.jpg"):
    # Faringitis estreptocócica con petequias en el paladar blando (CDC/Heinz F. Eichenwald, dominio público)
    guardar(Image.open("orig/strep_petequias.jpg").convert("RGB"), "strep_petequias.jpg", 440, 85)
if hacer("tb_miliar.jpg"):
    # Tuberculosis miliar en la Rx de tórax (Herreros y col., CC BY 4.0), sin la letra del panel
    guardar(Image.open("orig/tb_miliar.jpg").convert("L").crop((0, 30, 717, 658)), "tb_miliar.jpg", 400, 85)
if hacer("pavlik.jpg"):
    # Esquema del arnés de Pavlik (Londenp, CC BY-SA 3.0)
    guardar(Image.open("orig/pavlik.jpg").convert("RGB"), "pavlik.jpg", 336, 90)

# ── tanda 09
if hacer("lepto.jpg"):
    # Sufusión conjuntival con ictericia en leptospirosis (Daniel Ostermayer, CC BY 4.0); un solo ojo
    guardar(Image.open("orig/lepto.jpg").convert("RGB"), "lepto.jpg", 330, 90)
if hacer("sarna_surco.jpg"):
    # Surco de escabiosis (Michael Geary, dominio público)
    guardar(Image.open("orig/sarna_surco.jpg").convert("RGB"), "sarna_surco.jpg", 440, 88)
if hacer("cprm.jpg"):
    # Colangiorresonancia con coledocolitiasis (Hellerhoff, CC BY-SA 3.0); las letras y flechas rojas son del autor
    guardar(Image.open("orig/cprm.jpg").convert("L").crop((40, 0, 840, 1012)), "cprm.jpg", 400, 85)
if hacer("hipersegm.jpg"):
    # Neutrófilo hipersegmentado en anemia megaloblástica (Ed Uthman, CC BY 2.0)
    guardar(Image.open("orig/hipersegm.jpg").convert("RGB"), "hipersegm.jpg", 400, 88)
if hacer("megalo_mont.jpg"):
    # Foto real (izquierda) + frotis dibujado con frotis29.py (derecha)
    lado(["hipersegm.jpg", "frotis_megalo.jpg"], "megalo_mont.jpg", 300)
if hacer("otitis_ext.jpg"):
    # Otitis externa grave (James Heilman, CC BY 3.0), recortada a la oreja
    guardar(Image.open("orig/otitis_ext.jpg").convert("RGB").crop((300, 800, 2500, 3000)), "otitis_ext.jpg", 400, 85)
if hacer("conjuntivitis.jpg"):
    # Conjuntivitis bacteriana (Gzzz, CC BY-SA 4.0), recortada a un ojo
    guardar(Image.open("orig/conjuntivitis.jpg").convert("RGB").crop((150, 700, 1950, 1800)), "conjuntivitis.jpg", 440, 85)
if hacer("pliegue.jpg"):
    # Signo del pliegue por deshidratación (DRobert, CC BY-SA 4.0)
    guardar(Image.open("orig/pliegue.jpg").convert("RGB").crop((0, 100, 768, 900)), "pliegue.jpg", 400, 85)
if hacer("acne.jpg"):
    # Acné comedoniano en la frente (Dr. Thomas Brinkmeier, CC BY 4.0)
    guardar(Image.open("orig/acne_comed.jpg").convert("RGB").crop((400, 800, 3000, 2800)), "acne.jpg", 440, 85)
if hacer("fijador.jpg"):
    # Fijador externo en la pierna (Ortopedikus, CC BY-SA 4.0), recortado a la pierna
    guardar(Image.open("orig/fijador.jpg").convert("RGB").crop((400, 150, 960, 639)), "fijador.jpg", 440, 85)

# ── tanda 10
if hacer("psoriasis_mont.jpg"):
    # Psoriasis en placas en la espalda (Marnanel, CC BY-SA 3.0) + piqueteado ungueal (Seenms, CC BY-SA 3.0)
    guardar(Image.open("orig/psoriasis.jpg").convert("RGB"), "psoriasis.jpg", 400, 88)
    guardar(Image.open("orig/una_psor.jpg").convert("RGB"), "una_psor.jpg", 400, 88)
    lado(["psoriasis.jpg", "una_psor.jpg"], "psoriasis_mont.jpg", 300)
if hacer("pca.jpg"):
    # Esquema del conducto arterioso persistente, rótulos en español (BrownCow, CC BY 4.0)
    guardar(_rgba_blanco("orig/pca.png"), "pca.jpg", 600, 90)
if hacer("collarin.jpg"):
    # Dos rescatistas colocan el collar cervical mientras sostienen la cabeza (Baedr-9439, CC0), dibujo
    guardar(_rgba_blanco("orig/collar_app.png"), "collarin.jpg", 480, 88)
if hacer("paracentesis.jpg"):
    # Paracentesis abdominal, esquema en español (BruceBlaus, CC BY-SA 4.0)
    guardar(_rgba_blanco("orig/paracentesis.png"), "paracentesis.jpg", 440, 88)
if hacer("sarampion_mont.jpg"):
    # Manchas de Koplik (CDC PHIL 6111) + exantema (CDC PHIL 4497), dominio público
    lado(["koplik.jpg", "sarampion_exantema.jpg"], "sarampion_mont.jpg", 240)
if hacer("hiv_eco.jpg"):
    # Hemorragia de la matriz germinal en ecografía transfontanelar (Prashanth Saddala, CC BY-SA 3.0), sin los datos del equipo
    guardar(Image.open("orig/hiv_eco.jpg").convert("L").crop((90, 0, 470, 330)), "hiv_eco.jpg", 380, 88)
if hacer("varices_wale.jpg"):
    # Várices esofágicas con puntos rojos (red wale) en la endoscopía (Samir, dominio público)
    guardar(Image.open("orig/varices_wale.jpg").convert("RGB"), "varices_wale.jpg", 330, 90)
