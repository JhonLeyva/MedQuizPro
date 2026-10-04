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

# ── TRA-029 · Artrosis de rodilla izquierda, Rx AP (James Heilman, MD, Commons, CC BY-SA 3.0)
if hacer("oa_rodilla.jpg"):
    o = Image.open("orig/oa_rodilla.jpg").convert("L").crop((0, 300, 960, 1060))
    o = ImageOps.autocontrast(o, cutoff=0.5).point(lambda v: int(255 * (v / 255) ** 2.2))
    guardar(o, "oa_rodilla.jpg", 480, 88)
# ── GAS-050 · Gastritis erosiva hemorrágica (Amadalvarez, Commons, CC BY-SA 4.0); se recorta el borde azul
if hacer("gastritis_erosiva.jpg"):
    guardar(Image.open("orig/gastritis_erosiva.jpg").convert("RGB").crop((0, 40, 470, 438)), "gastritis_erosiva.jpg", 400, 88)
# ── GAS-051 · Cáncer de colon estenosante en la colonoscopía (G. Narasimha Murthy, Commons, CC0)
if hacer("ca_colon.jpg"):
    guardar(Image.open("orig/ca_colon.jpg").convert("RGB").crop((60, 0, 900, 830)), "ca_colon.jpg", 420, 88)

# ── GIN-141 · Cérvix «en fresa» en la colposcopía (Aribodor et al., BMC Public Health 2024, PMC10988871, CC BY 4.0)
if hacer("cervix_fresa.jpg"):
    o = Image.open("orig/cervix_fresa.jpg").convert("RGB").crop((0, 95, 744, 446))
    a = np.array(o).astype(int)
    m = (a.sum(2) < 200)                      # líneas negras y letras «S» del autor
    m[:, :int(0.15 * a.shape[1])] = False
    o = rellenar(o, m, 7)
    guardar(o, "cervix_fresa.jpg", 500, 88)
# ── GAS-052 · TC: masa hipodensa en la cabeza del páncreas (Sone et al., Surg Case Rep 2026, PMC13572855, CC BY 4.0), panel A
if hacer("pancreas_ca_tc.jpg"):
    o = Image.open("orig/pancreas_ca_tc.jpg").convert("L").crop((0, 0, 700, 580))
    o0 = o
    a = np.array(o)
    m = np.zeros(a.shape, bool)
    m[:118, :122] = True                                   # letra del panel
    m[90:240, 380:600] = a[90:240, 380:600] > 200          # rótulos SMV / SMA
    o = rellenar(o, m, 7).crop((125, 115, 700, 580))
    guardar(o, "pancreas_ca_tc.jpg", 480, 88)
# ── NEF-063 · Angio-TC con émbolo en silla de montar (Aung Myat y Arif Ahsan, Commons, CC BY 2.0), corte axial
if hacer("tep_tc.jpg"):
    guardar(Image.open("orig/tep_tc.jpg").convert("L").crop((0, 278, 401, 546)), "tep_tc.jpg", 401, 88)
# ── INF-075 · Inclusión de citomegalovirus «en ojo de búho» (CDC, Commons, dominio público)
if hacer("cmv_inclusion.jpg"):
    guardar(Image.open("orig/cmv_inclusion.jpg").convert("RGB").crop((300, 40, 940, 600)), "cmv_inclusion.jpg", 420, 88)
# ── INF-075 · Esofagitis por cándida en la endoscopía (James Heilman, MD, Commons, CC BY-SA 3.0)
if hacer("candida_esof.jpg"):
    guardar(Image.open("orig/candida_esof.jpg").convert("RGB").crop((110, 60, 900, 700)), "candida_esof.jpg", 420, 88)
# ── INF-076 · Trofozoítos de E. histolytica con hematíes fagocitados (CDC, Commons, dominio público)
if hacer("ameba.jpg"):
    guardar(Image.open("orig/ameba.jpg").convert("RGB"), "ameba.jpg", 282, 92)
# ── CIR-082 · Íleo adinámico: asas de delgado y colon dilatadas (Radiopaedia 11177, Commons, dominio público)
if hacer("ileo_rx.jpg"):
    guardar(Image.open("orig/ileo_rx.jpg").convert("L").crop((0, 0, 500, 560)), "ileo_rx.jpg", 400, 88)
# ── GIN-141 · Tricomonas en fresco, contraste de fases (CDC/PHIL, Commons, dominio público)
if hacer("trico.jpg"):
    guardar(Image.open("orig/trico.png").convert("RGB").crop((230, 60, 830, 560)), "trico.jpg", 420, 88)
# ── GIN-141 · Seudohifas de cándida en KOH (Mikael Häggström, Commons, CC0); se conservan sus flechas
if hacer("candida_koh.jpg"):
    guardar(Image.open("orig/candida_koh.jpg").convert("RGB").crop((30, 30, 480, 480)), "candida_koh.jpg", 400, 88)

# ── NEF-066 · Torsión testicular: Doppler sin flujo dentro del testículo (Abu-Sharikh et al., Medicine 2026, PMC13574465, CC BY 4.0), panel B
if hacer("torsion_eco.jpg"):
    o = Image.open("orig/torsion_eco.jpg").convert("RGB").crop((880, 95, 1600, 682))
    guardar(o, "torsion_eco.jpg", 440, 88)
# ── PED-144 · Rx de membrana hialina: vidrio esmerilado y broncograma aéreo (Xie et al., Front Pediatr 2026, PMC13260572, CC BY 4.0)
if hacer("emh_rx2.jpg"):
    guardar(Image.open("orig/emh_rx.jpg").convert("L").crop((40, 120, 760, 760)), "emh_rx2.jpg", 420, 88)
# ── OFT-033 · Glaucoma agudo de ángulo cerrado (Jonathan Trobe, MD, Commons, CC BY 3.0)
if hacer("glaucoma_agudo.jpg"):
    guardar(Image.open("orig/glaucoma_agudo.jpg").convert("RGB"), "glaucoma_agudo.jpg", 360, 92)
# ── TRA-031 · Fractura diafisaria desplazada de húmero (Ivtorov, Commons, CC BY-SA 4.0)
if hacer("humero_fx.jpg"):
    guardar(Image.open("orig/humero_fx.jpg").convert("L").crop((0, 420, 960, 1509)), "humero_fx.jpg", 360, 88)
# ── REU-040 · Melanoma (asimetría) de la serie ABCD del NCI (dominio público)
if hacer("melanoma.jpg"):
    guardar(Image.open("orig/melanoma_abcd.jpg").convert("RGB").crop((0, 0, 470, 300)), "melanoma.jpg", 400, 88)
# ── REU-040 · Carcinoma basocelular nodular al microscopio (Mikael Häggström, Commons, CC0)
if hacer("bcc_patologia.jpg"):
    guardar(Image.open("orig/bcc_pato.jpg").convert("RGB").crop((60, 60, 900, 870)), "bcc_patologia.jpg", 400, 88)

# ── REU-044 · Sacroileítis bilateral en la Rx de pelvis (Ameer et al., Front Pharmacol 2026, PMC13553827, CC BY 4.0), panel E
if hacer("sacroileitis_rx.jpg"):
    o = Image.open("orig/ea_rx.jpg").convert("L").crop((745, 30, 1351, 728))
    guardar(ImageEnhance.Contrast(o).enhance(1.2), "sacroileitis_rx.jpg", 420, 88)
# ── CB-056 · Viuda negra, Latrodectus mactans (Juan Carlos Fonseca Mata, Commons, CC BY-SA 4.0)
if hacer("latrodectus.jpg"):
    guardar(Image.open("orig/latrodectus.jpg").convert("RGB").crop((240, 120, 860, 560)), "latrodectus.jpg", 400, 88)
# ── CB-056 · Escorpión Tityus (Charles J. Sharp, Commons, CC BY-SA 4.0)
if hacer("escorpion.jpg"):
    guardar(Image.open("orig/escorpion.jpg").convert("RGB").crop((100, 20, 900, 600)), "escorpion.jpg", 400, 88)
# ── CB-055 · Encías del escorbuto (CDC, Commons, dominio público); solo boca
if hacer("escorbuto.jpg"):
    guardar(Image.open("orig/escorbuto.jpg").convert("RGB").crop((180, 90, 880, 380)), "escorbuto.jpg", 400, 88)

# ── CB-057 · Botón gustativo rotulado en español (NEUROtiker, Commons, CC BY-SA 3.0)
if hacer("boton_gustativo.jpg"):
    guardar(Image.open("orig/boton_gustativo.jpg").convert("RGB"), "boton_gustativo.jpg", 500, 92)
# ── GAS-055 · Progresión de Barrett en la histología (Leonard et al., Dis Esophagus 2026, PMC13313527, CC BY 4.0): 4 paneles sin letra
if hacer("barrett_a.jpg"):
    o = Image.open("orig/barrett_histo.jpg").convert("RGB")
    for k, (x0, y0, x1, y1) in {"a": (0, 0, 372, 340), "b": (380, 0, 755, 340), "c": (0, 350, 372, 691), "d": (380, 350, 755, 691)}.items():
        guardar(o.crop((x0 + 34, y0 + 34, x1, y1)), f"barrett_{k}.jpg", 330, 88)

# ── GIN-155 · Cuello uterino normal vs corto con embudo en la eco transvaginal (Pongchaikul et al., Clin Microbiol Rev 2026,
#    PMC13560723, CC BY 4.0); se borran los rótulos en inglés y las cifras del equipo
if hacer("cervix_corto.jpg"):
    o = Image.open("orig/cervix_corto.jpg").convert("RGB")
    a = np.array(o).astype(int)
    blanco = (a.min(2) > 150) & ((a.max(2) - a.min(2)) < 70)
    m = np.zeros(a.shape[:2], bool)
    for x0, y0, x1, y1 in [(0, 0, 1600, 32), (50, 95, 330, 195), (20, 235, 250, 360), (0, 320, 140, 405), (300, 160, 540, 390),
                           (600, 25, 800, 190), (900, 95, 1140, 195), (815, 320, 970, 420), (960, 320, 1210, 455),
                           (1250, 255, 1490, 405), (1455, 25, 1600, 190)]:
        m[y0:y1, x0:x1] |= blanco[y0:y1, x0:x1]
    m[530:588, 640:800] = True
    m[530:588, 1450:1600] = True
    o = rellenar(o, m, 5)
    guardar(o.crop((0, 30, 800, 588)), "cervix_normal_eco.jpg", 400, 88)
    guardar(o.crop((810, 30, 1600, 588)), "cervix_corto_eco.jpg", 400, 88)
# ── REU-046 · Piel escaldada estafilocócica en la mano de un lactante (OpenStax Microbiology, Commons, CC BY 4.0)
if hacer("ssss.jpg"):
    guardar(Image.open("orig/ssss.jpg").convert("RGB"), "ssss.jpg", 400, 90)
# ── REU-047 · Onicomicosis del primer dedo (James Heilman, MD, Commons, CC BY-SA 3.0); sin EXIF
if hacer("onicomicosis.jpg"):
    guardar(Image.open("orig/onicomicosis.jpg").convert("RGB").crop((0, 0, 960, 760)), "onicomicosis.jpg", 400, 88)
# ── OFT-034 · Leucocoria por retinoblastoma (J. Morley-Smith, Commons, dominio público): solo los ojos
if hacer("leucocoria.jpg"):
    guardar(Image.open("orig/leucocoria.png").convert("RGB").crop((0, 10, 250, 80)), "leucocoria.jpg", 250, 92)

# ── CB-060 · COVID-19: vidrio esmerilado y consolidaciones bilaterales (Wang et al., Curr Med Imaging 2026, PMC13613316, CC BY 4.0), panel A
if hacer("covid_tc.jpg"):
    o = Image.open("orig/covid_tc.jpg").convert("L").crop((10, 50, 373, 291))
    a = np.array(o); m = np.zeros(a.shape, bool); m[:40, :50] = True
    guardar(rellenar(o, m, 3), "covid_tc.jpg", 400, 88)
# ── NRL-044 · Lóbulos cerebrales rotulados en español (ElizabethFG, Commons, CC BY-SA 3.0)
if hacer("lobulos.jpg"):
    guardar(Image.open("orig/lobulos.jpg").convert("RGB"), "lobulos.jpg", 480, 90)

# ── INF-083 · Mucor: hifas anchas no septadas en ángulo recto (Yale Rosen, Commons, CC BY-SA 2.0)
if hacer("mucor.jpg"):
    guardar(Image.open("orig/mucor.jpg").convert("RGB").crop((0, 0, 900, 700)), "mucor.jpg", 400, 88)
# ── CIR-093 · Gangrena seca de los dedos en un diabético (James Heilman, MD, Commons, CC BY-SA 3.0); sin EXIF
if hacer("gangrena.jpg"):
    guardar(Image.open("orig/gangrena.jpg").convert("RGB").crop((60, 0, 900, 820)), "gangrena.jpg", 380, 88)
# ── PED-160 · Granuloma umbilical (T. S. Cullen 1916, Commons, dominio público)
if hacer("granuloma_umb.jpg"):
    guardar(Image.open("orig/granuloma_umb.jpg").convert("RGB").crop((20, 40, 310, 330)), "granuloma_umb.jpg", 290, 90)

if hacer("hig_metas.jpg"):
    # James Heilman, MD · Commons · CC BY-SA 3.0 (MultipleLiverMets2008.jpg): TC axial con múltiples metástasis hipodensas
    guardar(Image.open("orig/liver_mets.jpg").convert("RGB").crop((40, 20, 900, 690)), "hig_metas.jpg", 380, 88)

if hacer("podagra.jpg"):
    # Gonzosft · Commons · CC BY 3.0 de (Podagra.jpg): la flecha negra es de la foto original
    guardar(Image.open("orig/podagra.jpg").convert("RGB"), "podagra.jpg", 500, 88)
