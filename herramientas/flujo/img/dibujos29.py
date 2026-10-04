"""Esquemas propios de la Entrega 2 (cuando no hay foto libre que sirva): dibujos simples, rotulados en español,
pensados para que cualquiera los entienda. Uso: python3 dibujos29.py <nombre> (sin argumentos los hace todos)."""
import math, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, FancyBboxPatch, Rectangle, PathPatch, Arc
from matplotlib.path import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
PIEL = "#f6dccb"
TINTA = "#1f2937"
ROJO = "#c62828"
AZUL = "#1e5bb8"
VIOLETA = "#7b2d6b"
GRIS = "#6b7280"
plt.rcParams["font.family"] = "DejaVu Sans"


def lienzo(W, H, fondo="#ffffff", px=(860, None)):
    """Figura de W×H unidades (y hacia abajo), salida de px[0] píxeles de ancho."""
    ancho = px[0]
    fig = plt.figure(figsize=(ancho / 100, ancho * H / W / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), W, H, color=fondo, zorder=0))
    return fig, ax


def guardar(fig, nombre):
    fig.savefig(os.path.join(AQUI, nombre), dpi=100, pil_kwargs=dict(quality=92))
    plt.close(fig)
    print(nombre)


def rot(ax, x, y, t, s=11, c=TINTA, w="bold", ha="center", va="center", fondo=None, z=10, giro=0):
    kw = dict(fontsize=s, color=c, fontweight=w, ha=ha, va=va, zorder=z, linespacing=1.15, rotation=giro)
    if fondo:
        kw["bbox"] = dict(boxstyle="round,pad=0.25", fc=fondo, ec="none", alpha=.92)
    ax.text(x, y, t, **kw)


def curva(ax, pts, c=TINTA, lw=2, z=3, ls="-"):
    p = np.array(pts, float)
    t = np.linspace(0, 1, 100)
    # Bézier de grado n
    n = len(p) - 1
    b = sum(math.comb(n, k) * ((1 - t) ** (n - k))[:, None] * (t ** k)[:, None] * p[k] for k in range(n + 1))
    ax.plot(b[:, 0], b[:, 1], color=c, lw=lw, zorder=z, ls=ls, solid_capstyle="round")
    return b


# ───────────────────────────────────────────────────────── ingle: hernia crural vs inguinal
def hernia_crural():
    fig, ax = lienzo(100, 70, PIEL)
    # pubis y espina ilíaca
    ax.add_patch(Ellipse((86, 50), 20, 8, angle=-20, fc="#efe6d8", ec="#b9a888", lw=2, zorder=2))
    rot(ax, 86, 59, "pubis", 19, GRIS, "normal")
    ax.add_patch(Circle((9, 14), 2.6, fc="#efe6d8", ec="#b9a888", lw=2, zorder=2))
    rot(ax, 12, 5, "espina ilíaca", 19, GRIS, "normal")
    # vasos femorales (pasan por debajo del ligamento)
    for x0, c, n in ((37, ROJO, "arteria"), (45, AZUL, "vena")):
        ax.add_patch(FancyBboxPatch((x0 - 3.2, 20), 6.4, 52, boxstyle="round,pad=0,rounding_size=3", fc=c, ec="none", alpha=.88, zorder=2))
        rot(ax, x0, 54, n, 19, "#ffffff", giro=90)
    # ligamento inguinal
    curva(ax, [(11, 16), (45, 30), (78, 45)], "#7a5c2e", 7, 4)
    rot(ax, 17, 30, "ligamento\ninguinal", 21, "#7a5c2e")
    # hernia inguinal (encima del ligamento): contorno punteado
    ax.add_patch(Ellipse((60, 24), 15, 10, angle=25, fc="none", ec=GRIS, lw=3, ls=(0, (4, 3)), zorder=5))
    rot(ax, 66, 9, "inguinal: ENCIMA", 20, GRIS)
    # hernia crural (debajo del ligamento, medial a la vena)
    ax.add_patch(Ellipse((60, 54), 17, 14, fc="#8e3b78", ec="#5c1f4c", lw=3, alpha=.94, zorder=5))
    rot(ax, 60, 54, "CRURAL", 20, "#ffffff")
    rot(ax, 71, 66, "DEBAJO, medial a la vena", 19, "#5c1f4c")
    guardar(fig, "dib_hernia_crural.jpg")


# ───────────────────────────────────────────────────────── nomograma de Rumack-Matthew (paracetamol)
def nomograma_paracetamol():
    fig = plt.figure(figsize=(8.6, 6.0), dpi=100)
    ax = fig.add_axes([0.14, 0.14, 0.82, 0.80])
    t = np.linspace(4, 24, 200)
    linea = 150 * 2 ** (-(t - 4) / 4)            # línea de tratamiento (150 µg/mL a las 4 h, vida media 4 h)
    ax.fill_between(t, linea, 1000, color="#fde2e1", zorder=0)
    ax.fill_between(t, 3, linea, color="#e3f4ea", zorder=0)
    ax.plot(t, linea, color=ROJO, lw=4, zorder=3)
    ax.set_yscale("log")
    ax.set_xlim(4, 24)
    ax.set_ylim(3, 1000)
    ax.set_xticks([4, 8, 12, 16, 20, 24])
    ax.set_yticks([5, 10, 50, 150, 500])
    ax.set_yticklabels(["5", "10", "50", "150", "500"])
    ax.tick_params(labelsize=17)
    ax.set_xlabel("horas desde la ingesta", fontsize=19, fontweight="bold", color=TINTA)
    ax.set_ylabel("paracetamol (µg/mL)", fontsize=19, fontweight="bold", color=TINTA)
    ax.grid(True, which="major", color="#cbd5e1", lw=1)
    for s_ in ax.spines.values():
        s_.set_color("#94a3b8")
    ax.text(15.5, 220, "ENCIMA: dar\nN-acetilcisteína", fontsize=21, fontweight="bold", color=ROJO, ha="center", va="center")
    ax.text(9.5, 7, "DEBAJO: riesgo bajo", fontsize=20, fontweight="bold", color="#15803d", ha="center", va="center")
    ax.annotate("línea de tratamiento\n(150 a las 4 h)", xy=(6.2, 150 * 2 ** (-(2.2) / 4)), xytext=(10.5, 90), fontsize=17,
                color=ROJO, fontweight="bold", ha="left", va="center", arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=2.5))
    guardar(fig, "dib_nomograma_paracetamol.jpg")


# ───────────────────────────────────────────────────────── úlcera péptica: balanza agresión / defensa
def balanza_ulcera():
    fig, ax = lienzo(100, 76, "#ffffff")
    # soporte y fiel inclinado hacia la agresión (izquierda baja)
    ax.add_patch(Polygon([(46, 62), (54, 62), (50, 30)], closed=True, fc="#94a3b8", ec="none", zorder=2))
    ang = math.radians(12)
    x0, y0, x1, y1 = 50 - 34 * math.cos(ang), 30 + 34 * math.sin(ang), 50 + 34 * math.cos(ang), 30 - 34 * math.sin(ang)
    ax.plot([x0, x1], [y0, y1], color="#475569", lw=6, zorder=3, solid_capstyle="round")
    ax.add_patch(Circle((50, 30), 2.2, fc="#475569", zorder=4))
    for (cx, cy), c, t, lin in (((x0, y0), ROJO, "AGRESIÓN", ["ácido (HCl)", "pepsina", "H. pylori", "AINE, tabaco"]),
                                ((x1, y1), "#15803d", "DEFENSA", ["moco", "bicarbonato", "flujo de sangre", "prostaglandinas"])):
        ax.plot([cx - 9, cx, cx + 9], [cy + 14, cy, cy + 14], color="#64748b", lw=2, zorder=2)
        ax.add_patch(FancyBboxPatch((cx - 16, cy + 14), 32, 3, boxstyle="round,pad=0,rounding_size=1.5", fc=c, ec="none", zorder=3))
        rot(ax, cx, cy - 5, t, 26, c)
        rot(ax, cx, cy + 27, "\n".join(lin), 21, TINTA, "normal")
    rot(ax, 50, 6, "úlcera = gana la agresión", 26, TINTA)
    guardar(fig, "dib_balanza_ulcera.jpg")


# ───────────────────────────────────────────────────────── ingle por dentro: hernia directa vs indirecta
def hernia_inguinal():
    fig, ax = lienzo(100, 70, PIEL)
    # ligamento inguinal (abajo) y recto (a la derecha = línea media)
    curva(ax, [(6, 30), (45, 52), (80, 62)], "#7a5c2e", 7, 3)
    rot(ax, 18, 49, "ligamento inguinal", 18, "#7a5c2e", giro=-25)
    ax.add_patch(FancyBboxPatch((82, 4), 14, 62, boxstyle="round,pad=0,rounding_size=3", fc="#e7b8a8", ec="#b98473", lw=2, zorder=2))
    rot(ax, 89, 34, "recto abdominal", 18, "#7c3f33", giro=90)
    # vasos epigástricos inferiores
    curva(ax, [(40, 50), (44, 30), (52, 6)], ROJO, 6, 4)
    rot(ax, 56, 8, "vasos epigástricos", 18, ROJO, ha="left")
    # triángulo de Hesselbach (entre vasos, recto y ligamento)
    ax.add_patch(Polygon([(41, 50), (81, 61), (81, 22), (47, 22)], closed=True, fc="#fde68a", ec="#ca8a04", lw=2.5, alpha=.55, zorder=2))
    rot(ax, 65, 44, "triángulo de\nHesselbach", 18, "#854d0e")
    # anillo inguinal profundo (lateral a los vasos)
    ax.add_patch(Circle((28, 34), 5, fc="#ffffff", ec="#1e5bb8", lw=3, zorder=5))
    rot(ax, 23, 14, "INDIRECTA:\npor el anillo profundo,\nlateral a los vasos", 18, AZUL)
    ax.annotate("", xy=(28, 38), xytext=(23, 24), arrowprops=dict(arrowstyle="-|>", color=AZUL, lw=2.5), zorder=6)
    rot(ax, 65, 29, "DIRECTA:\nmedial a los vasos", 17, "#854d0e")
    rot(ax, 4, 66, "lado derecho visto desde dentro del abdomen", 15, GRIS, "normal", ha="left")
    guardar(fig, "dib_hernia_inguinal.jpg")


# ───────────────────────────────────────────────────────── coartación de aorta
def coartacion():
    fig, ax = lienzo(100, 72, "#ffffff")
    R_ = "#d64545"
    # corazón
    ax.add_patch(Ellipse((22, 54), 26, 22, fc="#f2b8b5", ec="#b84a4a", lw=2.5, zorder=2))
    rot(ax, 22, 56, "corazón", 21, "#7f1d1d")
    # aorta ascendente, cayado y descendente con estrechez
    t = np.linspace(math.pi, 0, 60)
    xs, ys = 40 + 16 * np.cos(t), 26 - 14 * np.sin(t)
    ax.plot([26, 24], [44, 28], color=R_, lw=16, solid_capstyle="round", zorder=3)
    ax.plot(xs, ys, color=R_, lw=16, solid_capstyle="round", zorder=3)
    ax.plot([56, 56], [26, 40], color=R_, lw=16, solid_capstyle="butt", zorder=3)
    ax.plot([56, 56], [40, 45], color=R_, lw=5, solid_capstyle="butt", zorder=3)        # estrechez
    ax.plot([56, 56], [45, 70], color=R_, lw=16, solid_capstyle="butt", zorder=3)
    # ramas a la cabeza y brazos
    for x0 in (32, 40, 48):
        ax.plot([x0, x0 - 2], [14, 3], color=R_, lw=7, zorder=2, solid_capstyle="round")
    ax.annotate("", xy=(52, 42.5), xytext=(68, 42.5), arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=3), zorder=6)
    rot(ax, 69, 42.5, "ESTRECHEZ\ntras la subclavia\nizquierda", 17, TINTA, ha="left")
    rot(ax, 58, 7, "brazos: pulso FUERTE,\nPA alta", 17, "#15803d", ha="left")
    rot(ax, 60, 64, "piernas: pulso DÉBIL,\nPA baja", 17, ROJO, ha="left")
    guardar(fig, "dib_coartacion.jpg")


# ───────────────────────────────────────────────────────── canal endémico
def canal_endemico():
    fig = plt.figure(figsize=(8.6, 5.6), dpi=100)
    ax = fig.add_axes([0.11, 0.15, 0.86, 0.80])
    sem = np.arange(1, 53)
    base = 20 + 12 * np.sin((sem - 8) / 52 * 2 * np.pi) ** 2
    q1, q2, q3 = base * .7, base, base * 1.35
    ax.fill_between(sem, 0, q1, color="#bbf7d0", label="éxito")
    ax.fill_between(sem, q1, q2, color="#fef9c3")
    ax.fill_between(sem, q2, q3, color="#fed7aa")
    ax.fill_between(sem, q3, 60, color="#fecaca")
    casos = (q1 + q2) / 2 * (1 + 0.05 * np.sin(sem / 2))
    casos[30:38] = q3[30:38] * np.array([1.1, 1.3, 1.5, 1.6, 1.5, 1.3, 1.1, .9])
    ax.plot(sem, casos, color=TINTA, lw=3.5, marker="o", ms=4)
    for y, t, c in ((6, "ÉXITO", "#15803d"), ((q1[2] + q2[2]) / 2 - 2.5, "SEGURIDAD", "#a16207"), ((q2[2] + q3[2]) / 2, "ALERTA", "#c2410c"),
                    (55, "EPIDEMIA", ROJO)):
        ax.text(2, y, t, fontsize=16, fontweight="bold", color=c, va="center")
    ax.annotate("casos por encima\nde lo esperado", xy=(33, casos[32]), xytext=(37, 58), fontsize=15, fontweight="bold",
                color=ROJO, arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=2.5), va="top")
    ax.annotate("endemia: dentro\nde lo esperado", xy=(16, casos[15]), xytext=(17, 50), fontsize=15, fontweight="bold",
                color=TINTA, arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=2.5), ha="center", va="top")
    ax.set_xlim(1, 52)
    ax.set_ylim(0, 60)
    ax.set_xlabel("semanas epidemiológicas", fontsize=18, fontweight="bold", color=TINTA)
    ax.set_ylabel("casos", fontsize=18, fontweight="bold", color=TINTA)
    ax.tick_params(labelsize=15)
    guardar(fig, "dib_canal_endemico.jpg")


# ───────────────────────────────────────────────────────── zonas de Kramer
def kramer():
    fig, ax = lienzo(100, 80, "#ffffff")
    piel = "#f3d2b8"
    # bebé de frente (silueta simple)
    ax.add_patch(Ellipse((25, 12), 15, 16, fc=piel, ec="#b58a6a", lw=2, zorder=2))           # cabeza
    ax.add_patch(FancyBboxPatch((15, 20), 20, 26, boxstyle="round,pad=0,rounding_size=6", fc=piel, ec="#b58a6a", lw=2, zorder=2))
    for x0, ang in ((12, 20), (38, -20)):                                                       # brazos
        ax.add_patch(Ellipse((x0, 31), 6, 20, angle=ang, fc=piel, ec="#b58a6a", lw=2, zorder=1))
    for x0 in (20, 30):                                                                         # piernas
        ax.add_patch(FancyBboxPatch((x0 - 3.5, 45), 7, 26, boxstyle="round,pad=0,rounding_size=3", fc=piel, ec="#b58a6a", lw=2, zorder=1))
    # zonas (de arriba abajo) con amarillo creciente
    zonas = [(4, 20, "1", "cabeza y cuello", "≈ 5 mg/dL"), (20, 33, "2", "tórax hasta el ombligo", "≈ 10 mg/dL"),
             (33, 46, "3", "abdomen bajo y muslos", "≈ 12 mg/dL"), (46, 64, "4", "piernas y brazos", "≈ 15 mg/dL"),
             (64, 74, "5", "palmas y plantas", "> 15 mg/dL")]
    amar = ["#fde68a", "#fcd34d", "#fbbf24", "#f59e0b", "#d97706"]
    for (y0, y1, n, t, v), c in zip(zonas, amar):
        ax.add_patch(Rectangle((4, y0), 42, y1 - y0, fc=c, ec="none", alpha=.45, zorder=3))
        ax.plot([4, 50], [y1, y1], color="#92400e", lw=1.2, ls=(0, (4, 3)), zorder=4)
        ax.add_patch(Circle((54, (y0 + y1) / 2), 3.2, fc="#92400e", zorder=5))
        rot(ax, 54, (y0 + y1) / 2, n, 18, "#ffffff")
        rot(ax, 59, (y0 + y1) / 2 - 2, t, 16, TINTA, ha="left")
        rot(ax, 59, (y0 + y1) / 2 + 2.6, v, 15, "#92400e", "normal", ha="left")
    rot(ax, 50, 78, "la ictericia avanza de la cabeza a los pies", 17, GRIS, "normal")
    guardar(fig, "dib_kramer.jpg")


# ───────────────────────────────────────────────────────── tarjeta colorimétrica de heces (atresia biliar)
def tarjeta_heces():
    fig, ax = lienzo(100, 62, "#ffffff")
    cols = ["#f4f1e6", "#ece4c4", "#e2d79d", "#d9b44a", "#c99a2e", "#9a7b2a", "#6f6a2b"]
    for i, c in enumerate(cols):
        x = 4 + i * 13.4
        ax.add_patch(FancyBboxPatch((x, 14), 11, 24, boxstyle="round,pad=0,rounding_size=2", fc=c, ec="#94a3b8", lw=1.5, zorder=2))
        rot(ax, x + 5.5, 42, str(i + 1), 19, TINTA)
    ax.add_patch(FancyBboxPatch((2.5, 11), 39, 37, boxstyle="round,pad=0,rounding_size=2", fc="none", ec=ROJO, lw=4, zorder=3))
    rot(ax, 22, 6, "1-3: ANORMAL (acolia)", 19, ROJO)
    rot(ax, 72, 6, "4-7: normal", 19, "#15803d")
    rot(ax, 50, 56, "heces pálidas después de los 14 días = estudiar atresia biliar", 16, GRIS, "normal")
    guardar(fig, "dib_tarjeta_heces.jpg")


# ───────────────────────────────────────────────────────── ángulo de Cobb
def cobb():
    fig, ax = lienzo(100, 80, "#ffffff")
    # columna en S: vértebras como rectángulos inclinados a lo largo de una curva
    ys = np.linspace(6, 74, 12)
    xs = 38 + 9 * np.sin((ys - 6) / 68 * np.pi)
    dx = np.gradient(xs, ys)
    angs = np.degrees(np.arctan(dx))
    for i, (x, y, a) in enumerate(zip(xs, ys, angs)):
        col = "#f1d9b5" if i not in (2, 9) else "#fbbf24"
        ax.add_patch(Rectangle((x - 6, y - 2.4), 12, 4.8, angle=-a, rotation_point="center", fc=col, ec="#a07b4f", lw=1.8, zorder=3))
    # líneas por los platillos de las vértebras extremas (2 y 9)
    for i, c in ((2, AZUL), (9, AZUL)):
        a = math.radians(-angs[i])
        x0, y0 = xs[i], ys[i] + (-2.4 if i == 2 else 2.4)
        ax.plot([x0 - 30 * math.cos(a), x0 + 40 * math.cos(a)], [y0 - 30 * math.sin(a), y0 + 40 * math.sin(a)], color=c, lw=3, zorder=4)
    rot(ax, 82, 14, "vértebra más\ninclinada arriba", 16, AZUL)
    rot(ax, 82, 66, "vértebra más\ninclinada abajo", 16, AZUL)
    rot(ax, 82, 40, "ángulo entre\nlas dos líneas\n= ángulo de Cobb", 18, ROJO)
    rot(ax, 14, 40, "10-25°: leve\n25-45°: moderada\n> 45°: grave", 16, TINTA, ha="center")
    guardar(fig, "dib_cobb.jpg")


# ───────────────────────────────────────────────────────── bañera: incidencia, prevalencia, salidas
def banera():
    fig, ax = lienzo(100, 66, "#ffffff")
    # grifo (incidencia)
    ax.add_patch(Rectangle((20, 4), 18, 5, fc="#94a3b8", ec="none", zorder=3))
    ax.add_patch(Rectangle((34, 9), 4, 8, fc="#94a3b8", ec="none", zorder=3))
    for k in range(5):
        ax.add_patch(Circle((36, 20 + k * 3.2), 0.9, fc=AZUL, ec="none", zorder=3))
    rot(ax, 14, 7, "INCIDENCIA\n(casos nuevos)", 17, AZUL)
    # bañera (prevalencia)
    ax.add_patch(Polygon([(18, 34), (82, 34), (78, 58), (22, 58)], closed=True, fc="#e0f2fe", ec="#475569", lw=3, zorder=2))
    ax.add_patch(Polygon([(19.6, 40), (80.4, 40), (78, 58), (22, 58)], closed=True, fc="#60a5fa", ec="none", alpha=.85, zorder=2.5))
    rot(ax, 50, 49, "PREVALENCIA\n(todos los enfermos)", 19, "#ffffff")
    # salidas: curación y muerte
    ax.annotate("", xy=(92, 60), xytext=(80, 52), arrowprops=dict(arrowstyle="-|>", color="#15803d", lw=3))
    rot(ax, 91, 47, "curación", 16, "#15803d")
    ax.annotate("", xy=(8, 60), xytext=(20, 52), arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=3))
    rot(ax, 9, 47, "muerte\n(letalidad)", 16, ROJO)
    rot(ax, 71, 15, "Si casi nadie muere\nni se cura (crónica)\ny entran casos nuevos:\nla prevalencia SUBE", 16, TINTA)
    guardar(fig, "dib_banera.jpg")


# ───────────────────────────────────────────────────────── triángulo femoral (NAVEL)
def triangulo_femoral():
    fig, ax = lienzo(100, 74, PIEL)
    # bordes: ligamento inguinal (arriba), sartorio (lateral) y aductor largo (medial)
    ax.add_patch(Polygon([(10, 16), (90, 30), (56, 72)], closed=True, fc="#fbe7da", ec="none", zorder=1))
    curva(ax, [(6, 14), (50, 22), (92, 31)], "#7a5c2e", 6, 3)
    rot(ax, 18, 10.5, "ligamento inguinal", 17, "#7a5c2e", giro=-9)
    ax.plot([10, 56], [16, 72], color="#c08a6a", lw=10, solid_capstyle="round", zorder=2)
    ax.plot([90, 56], [30, 72], color="#c08a6a", lw=10, solid_capstyle="round", zorder=2)
    rot(ax, 22, 46, "sartorio", 17, "#7c3f33", giro=-50)
    rot(ax, 87, 55, "aductor\nlargo", 17, "#7c3f33")
    # estructuras de lateral a medial: nervio, arteria, vena, espacio, linfáticos
    ax.plot([33, 46], [22, 60], color="#eab308", lw=7, solid_capstyle="round", zorder=4)
    ax.plot([43, 51], [24, 62], color=ROJO, lw=12, solid_capstyle="round", zorder=4)
    ax.plot([54, 56], [26, 64], color=AZUL, lw=15, solid_capstyle="round", zorder=4)
    for y in (30, 35, 40):
        ax.add_patch(Circle((68, y), 1.4, fc="#16a34a", ec="none", zorder=4))
    rot(ax, 28, 30, "NERVIO", 17, "#a16207")
    rot(ax, 40, 66, "ARTERIA\n(pulso)", 17, ROJO)
    rot(ax, 73, 66, "VENA\n(medial al pulso)", 17, AZUL)
    rot(ax, 71, 35, "linfáticos", 16, "#15803d", ha="left")
    rot(ax, 4, 70, "← LATERAL", 16, GRIS, ha="left")
    rot(ax, 96, 70, "MEDIAL →", 16, GRIS, ha="right")
    rot(ax, 50, 4, "De lateral a medial: N-A-V-(espacio)-L", 18, TINTA)
    guardar(fig, "dib_triangulo_femoral.jpg")


# ───────────────────────────────────────────────────────── pupilas: dónde está la lesión
def pupilas():
    fig, ax = lienzo(100, 38, "#ffffff")
    casos = [(18, 0.6, "PUNTIFORMES\n(protuberancia,\nopioides)", ROJO),
             (50, 2.0, "NORMALES\n(3-4 mm)", "#15803d"),
             (82, 4.3, "DILATADA FIJA\nde un lado\n(III par, herniación)", AZUL)]
    for cx, r, txt, col in casos:
        for dx in (-7, 7):
            ax.add_patch(Ellipse((cx + dx, 10), 12, 8, fc="#ffffff", ec="#9ca3af", lw=2, zorder=2))
            rp = r if (cx != 82 or dx == -7) else 2.0
            ax.add_patch(Circle((cx + dx, 10), 3.4, fc="#8b5a2b", ec="none", zorder=3))
            ax.add_patch(Circle((cx + dx, 10), rp if rp < 3.3 else 3.2, fc="#111111", ec="none", zorder=4))
        rot(ax, cx, 26, txt, 17, col)
    guardar(fig, "dib_pupilas.jpg")


# ───────────────────────────────────────────────────────── colecciones del cuero cabelludo del recién nacido
def craneo_rn():
    fig, ax = lienzo(116, 52, "#ffffff")
    SANG = "#9f1239"
    for nombre, txt, x0 in (("CAPUT", "edema de la piel\nCRUZA la sutura", 16),
                            ("CEFALOHEMATOMA", "bajo el periostio\nNO cruza la sutura", 49),
                            ("SUBGALEAL", "bajo la galea: cruza\ny puede dar choque", 82)):
        ax.add_patch(Rectangle((x0, 15), 32, 6, fc="#f6dccb", ec="none", zorder=1))          # piel
        ax.add_patch(Rectangle((x0, 21), 32, 5, fc="#fdf2e9", ec="none", zorder=1))          # subcutáneo
        ax.plot([x0, x0 + 32], [26, 26], color="#92400e", lw=3, zorder=4)                    # galea
        ax.add_patch(Rectangle((x0, 33), 15, 6, fc="#d1d5db", ec="#6b7280", lw=1.5, zorder=5))   # hueso
        ax.add_patch(Rectangle((x0 + 17, 33), 15, 6, fc="#d1d5db", ec="#6b7280", lw=1.5, zorder=5))
        ax.plot([x0, x0 + 15, x0 + 16, x0 + 17, x0 + 32], [32.6, 32.6, 37, 32.6, 32.6], color="#7c3aed", lw=2.5, zorder=6)  # periostio
        if nombre == "CAPUT":
            ax.add_patch(Ellipse((x0 + 16, 19), 28, 9, fc="#fde68a", ec="#ca8a04", lw=2, alpha=.9, zorder=3))
        elif nombre == "CEFALOHEMATOMA":
            ax.add_patch(Ellipse((x0 + 7.5, 32.6), 13, 9, fc=SANG, ec="#7c3aed", lw=2.5, zorder=4.5))
        else:
            ax.add_patch(Ellipse((x0 + 16, 29.5), 31, 6, fc=SANG, ec="none", zorder=3))
        rot(ax, x0 + 16, 6, nombre, 17, TINTA)
        rot(ax, x0 + 16, 46, txt, 15, SANG if nombre != "CAPUT" else "#a16207")
    for y, t, c in ((18, "piel", "#7c3f33"), (26, "galea", "#92400e"), (32, "periostio", "#7c3aed"), (36.5, "hueso", GRIS)):
        rot(ax, 14.5, y, t, 14, c, ha="right")
    guardar(fig, "dib_craneo_rn.jpg")


# ───────────────────────────────────────────────────────── Rx de tórax con derrame pleural derecho (esquema)
def derrame():
    fig, ax = lienzo(100, 80, "#111111")
    AM = "#facc15"
    ax.add_patch(FancyBboxPatch((8, 8), 84, 68, boxstyle="round,pad=0,rounding_size=10", fc="#9ca3af", ec="none", zorder=1))   # partes blandas
    pd = ax.add_patch(Ellipse((31, 40), 30, 56, fc="#1f2937", ec="none", zorder=2))   # pulmón derecho (a la izquierda del lector)
    ax.add_patch(Ellipse((70, 40), 28, 54, fc="#1f2937", ec="none", zorder=2))   # pulmón izquierdo
    # mediastino y corazón desplazados al lado sano
    ax.add_patch(Rectangle((50, 8), 8, 30, fc="#d1d5db", ec="none", zorder=3))
    ax.add_patch(Ellipse((63, 56), 22, 22, fc="#d1d5db", ec="none", zorder=3))
    ax.plot([54, 55.5], [6, 30], color="#111111", lw=5, zorder=4)                 # tráquea (aire)
    # líquido: blanco, con borde superior cóncavo que sube hacia afuera (Damoiseau)
    t = np.linspace(0, 1, 40)
    xs = 14 + 34 * t
    ys = 34 + 14 * (t ** 1.6)
    liq = ax.add_patch(Polygon([(10, 34)] + list(zip(xs, ys)) + [(50, 80), (10, 80)], closed=True, fc="#e5e7eb", ec="none", zorder=3))
    liq.set_clip_path(pd)
    rot(ax, 30, 57, "LÍQUIDO\n(blanco)", 22, "#111111")
    ax.annotate("", xy=(20, 36), xytext=(8, 20), arrowprops=dict(arrowstyle="-|>", color=AM, lw=2.5), zorder=6)
    rot(ax, 2, 13, "curva que sube\nhacia afuera", 20, AM, ha="left")
    ax.annotate("", xy=(56, 22), xytext=(78, 12), arrowprops=dict(arrowstyle="-|>", color=AM, lw=2.5), zorder=6)
    rot(ax, 76, 6, "tráquea y corazón\nal otro lado", 20, AM)
    rot(ax, 12, 76, "DER", 19, "#ffffff")
    rot(ax, 88, 76, "IZQ", 19, "#ffffff")
    guardar(fig, "dib_derrame.jpg")


# ───────────────────────────────────────────────────────── dengue: qué prueba según el día de enfermedad
def dengue_pruebas():
    fig, ax = lienzo(100, 60, "#ffffff")
    x0, x1, yb = 10, 96, 48            # eje: día 0 a día 21
    dx = (x1 - x0) / 21
    ax.add_patch(Rectangle((x0, 6), 5 * dx, yb - 6, fc="#fee2e2", ec="none", zorder=1))
    rot(ax, x0 + 2.5 * dx, 9.5, "FASE FEBRIL\n(días 1-5)", 15, ROJO)
    ax.plot([x0, x1], [yb, yb], color=TINTA, lw=2.5, zorder=3)
    for d in (0, 5, 7, 10, 14, 21):
        ax.plot([x0 + d * dx] * 2, [yb, yb + 1.5], color=TINTA, lw=2, zorder=3)
        rot(ax, x0 + d * dx, yb + 4, str(d), 15, TINTA, "normal")
    rot(ax, (x0 + x1) / 2, 57.5, "días desde que empezó la fiebre", 15, GRIS, "normal")
    d = np.linspace(0, 21, 300)
    ns1 = 30 * np.exp(-((d - 2.5) / 2.0) ** 2)
    igm = 26 * np.exp(-((d - 11) / 4.5) ** 2) / (1 + np.exp(-(d - 5) / 0.7))
    igg = 22 / (1 + np.exp(-(d - 14) / 1.8))
    for y, c, t, xl, yl in ((ns1, ROJO, "NS1 / RT-PCR", 3.0, 14), (igm, AZUL, "IgM", 11, 19), (igg, "#15803d", "IgG", 18.5, 23)):
        ax.plot(x0 + d * dx, yb - y, color=c, lw=4, zorder=4)
        rot(ax, x0 + xl * dx, yb - 30 - (yl - 14) * 0 if False else yb - max(y) - 3.5, t, 17, c)
    guardar(fig, "dib_dengue_pruebas.jpg")


# ───────────────────────────────────────────────────────── regla de los 9 (quemaduras del adulto)
def regla9():
    fig, ax = lienzo(100, 70, "#ffffff")
    QUE = "#f87171"
    SANA = "#f6dccb"
    def figura(cx, titulo, tronco):
        ax.add_patch(Circle((cx, 12), 4.5, fc=SANA, ec="#9a6b52", lw=2, zorder=2))
        ax.add_patch(Rectangle((cx - 7, 17.5), 14, 20, fc=QUE, ec="#9a6b52", lw=2, zorder=2))
        for dx in (-1, 1):
            ax.add_patch(Polygon([(cx + dx * 7, 18), (cx + dx * 11.5, 19.5), (cx + dx * 13.5, 36), (cx + dx * 10.5, 36.5), (cx + dx * 8.5, 22)],
                                 closed=True, fc=QUE, ec="#9a6b52", lw=2, zorder=2))
            ax.add_patch(Rectangle((cx + (0.3 if dx > 0 else -6.8), 37.5), 6.5, 22, fc=SANA, ec="#9a6b52", lw=2, zorder=2))
        rot(ax, cx, 12, "4,5", 14, TINTA)
        rot(ax, cx, 27, tronco, 17, "#ffffff")
        rot(ax, cx - 13, 28, "4,5", 14, TINTA)
        rot(ax, cx + 13, 28, "4,5", 14, TINTA)
        rot(ax, cx - 3.5, 49, "9", 15, TINTA)
        rot(ax, cx + 3.5, 49, "9", 15, TINTA)
        rot(ax, cx, 3.5, titulo, 16, GRIS)
    figura(24, "ADELANTE", "18")
    figura(64, "ATRÁS", "18")
    rot(ax, 24, 64, "periné 1 %", 14, GRIS, "normal")
    rot(ax, 90, 26, "rojo =\nquemado\n(este caso)", 15, ROJO)
    rot(ax, 64, 66, "Brazos 9 + 9, tronco 18 + 18 = 54 %", 17, ROJO)
    guardar(fig, "dib_regla9.jpg")


# ───────────────────────────────────────────────────────── otoscopía: tapón de cerumen
def cerumen():
    fig, ax = lienzo(100, 72, "#ffffff")
    ax.add_patch(Circle((36, 37), 32, fc="#111111", ec="none", zorder=1))          # campo del otoscopio
    ax.add_patch(Circle((36, 37), 24, fc="#f4b6a6", ec="#d08a78", lw=2, zorder=2))   # piel del conducto
    ax.add_patch(Circle((40, 33), 13, fc="#d6dbe0", ec="#9ca3af", lw=1.5, zorder=3))  # tímpano al fondo
    t = np.linspace(0, 2 * math.pi, 40)
    r = 19 + 2.2 * np.sin(5 * t) + 1.2 * np.cos(9 * t)
    ax.add_patch(Polygon(list(zip(34 + r * np.cos(t), 39 + 0.9 * r * np.sin(t))), closed=True, fc="#8a5a2b", ec="#5b3a1a", lw=2, zorder=4))
    for k in range(25):
        a, d = k * 2.4, 4 + (k * 7) % 13
        ax.add_patch(Circle((34 + d * math.cos(a), 39 + d * math.sin(a)), 1.1, fc="#6b4220", ec="none", zorder=5))
    ax.annotate("", xy=(30, 42), xytext=(72, 52), arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=2.5), zorder=6)
    rot(ax, 72, 55, "CERUMEN\n(tapón)", 19, "#5b3a1a", ha="left")
    ax.annotate("", xy=(47, 24), xytext=(74, 14), arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=2.5), zorder=6)
    rot(ax, 75, 12, "tímpano\ncasi no se ve", 17, GRIS, ha="left")
    ax.annotate("", xy=(14, 25), xytext=(6, 8), arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=2.5), zorder=6)
    rot(ax, 2, 5, "piel del conducto", 16, "#b45f4d", ha="left")
    guardar(fig, "dib_cerumen.jpg")


# ───────────────────────────────────────────────────────── posturas: decorticación y descerebración
def posturas():
    fig, ax = lienzo(100, 80, "#ffffff")
    PIEL_ = "#9a6b52"
    def cuerpo(cx, flex, col, titulo, sub, lugar):
        ax.add_patch(Circle((cx, 13), 4.5, fc="#f6dccb", ec=PIEL_, lw=2, zorder=3))
        ax.plot([cx, cx], [17.5, 40], color=PIEL_, lw=10, solid_capstyle="round", zorder=2)          # tronco
        for dx in (-1, 1):
            ax.plot([cx + dx * 2.5, cx + dx * 3.5], [40, 60], color=PIEL_, lw=7, solid_capstyle="round", zorder=2)   # piernas rectas
            ax.plot([cx + dx * 3.5, cx + dx * 4.5], [60, 64], color=PIEL_, lw=5, solid_capstyle="round", zorder=2)   # pies en punta
            if flex:      # codo doblado, puño sobre el pecho
                ax.plot([cx + dx * 4, cx + dx * 10], [21, 31], color=col, lw=7, solid_capstyle="round", zorder=4)
                ax.plot([cx + dx * 10, cx + dx * 3], [31, 24], color=col, lw=7, solid_capstyle="round", zorder=4)
                ax.add_patch(Circle((cx + dx * 3, 24), 2, fc=col, ec="none", zorder=5))
            else:         # brazos rectos pegados, muñeca girada hacia afuera
                ax.plot([cx + dx * 4, cx + dx * 8], [21, 42], color=col, lw=7, solid_capstyle="round", zorder=4)
                ax.plot([cx + dx * 8, cx + dx * 11], [42, 45], color=col, lw=5, solid_capstyle="round", zorder=4)
        rot(ax, cx, 3.5, titulo, 19, col)
        rot(ax, cx, 70.5, sub, 17, TINTA)
        rot(ax, cx, 77.5, lugar, 15, col, "normal")
    cuerpo(22, True, AZUL, "DECORTICACIÓN", "brazos FLEXIONADOS", "lesión sobre el mesencéfalo")
    cuerpo(78, False, ROJO, "DESCEREBRACIÓN", "brazos EXTENDIDOS", "lesión del tronco (más grave)")
    rot(ax, 50, 40, "en ambas:\npiernas\nextendidas", 16, GRIS, "normal")
    guardar(fig, "dib_posturas.jpg")


# ───────────────────────────────────────────────────────── fórmula obstétrica G P(TPAV)
def formula_obstetrica():
    fig, ax = lienzo(100, 58, "#ffffff")
    cajas = [("G", "4", "embarazos", "#475569"), ("T", "1", "a término\n(41 sem)", AZUL), ("P", "2", "pretérmino\n(gemelar)", "#a16207"),
             ("A", "2", "abortos\n(ectóp., mola)", ROJO), ("V", "3", "hijos vivos", "#15803d")]
    for k, (l, n, t, c) in enumerate(cajas):
        x = 4 + k * 19.2
        ax.add_patch(FancyBboxPatch((x, 8), 16, 18, boxstyle="round,pad=0,rounding_size=2", fc="#ffffff", ec=c, lw=3, zorder=2))
        rot(ax, x + 8, 13, l, 19, c)
        rot(ax, x + 8, 21.5, n, 26, TINTA)
        rot(ax, x + 8, 34, t, 15, c)
    rot(ax, 50, 3, "G4  P 1-2-2-3   (término - pretérmino - abortos - vivos)", 17, TINTA)
    rot(ax, 50, 49, "Según la clave cada gemelo cuenta como un parto pretérmino.\nCon la regla TPAL internacional el gemelar es UN parto: P1213.", 14, GRIS, "normal")
    guardar(fig, "dib_formula_obstetrica.jpg")


# ───────────────────────────────────────────────────────── partograma: fase activa
def partograma():
    fig, ax = lienzo(100, 66, "#ffffff")
    x0, y0, w, h = 12, 6, 82, 48          # horas 0-8 en x; dilatación 4-10 cm en y (abajo 4)
    for k in range(0, 9):
        ax.plot([x0 + k * w / 8] * 2, [y0, y0 + h], color="#e5e7eb", lw=1.5, zorder=1)
        rot(ax, x0 + k * w / 8, y0 + h + 3.5, str(k), 15, GRIS, "normal")
    for d in range(4, 11):
        y = y0 + h - (d - 4) * h / 6
        ax.plot([x0, x0 + w], [y, y], color="#e5e7eb", lw=1.5, zorder=1)
        rot(ax, x0 - 3, y, str(d), 15, GRIS, "normal")
    def pt(hr, d):
        return x0 + hr * w / 8, y0 + h - (d - 4) * h / 6
    ax.plot(*zip(pt(0, 4), pt(6, 10)), color="#16a34a", lw=3, zorder=2)
    ax.plot(*zip(pt(4, 4), pt(8, 8)), color=ROJO, lw=3, ls="--", zorder=2)
    rot(ax, *pt(1.0, 9.2), "1 cm/hora\n(esperado)", 15, "#15803d")
    rot(ax, *pt(6.6, 5.4), "si cruza:\nparto lento", 15, ROJO)
    a, b = pt(1, 6), pt(3, 8)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=AZUL, lw=4, zorder=4)
    for q in (a, b):
        ax.add_patch(Circle(q, 1.3, fc=AZUL, ec="none", zorder=5))
    rot(ax, *pt(3.4, 6.3), "este caso:\n6 → 8 cm en 2 h", 16, AZUL, ha="left")
    rot(ax, 4, 3, "cm", 14, GRIS, "normal")
    rot(ax, 54, 64, "horas de fase activa", 15, GRIS, "normal")
    guardar(fig, "dib_partograma.jpg")


# ───────────────────────────────────────────────────────── profundidad de las quemaduras
def piel_quemadura():
    fig, ax = lienzo(100, 64, "#ffffff")
    capas = [(12, 6, "#f9d5c4", "epidermis"), (18, 13, "#f2b8a2", "dermis\nsuperficial"),
             (31, 12, "#e79d86", "dermis\nprofunda"), (43, 9, "#fde68a", "grasa")]
    for y, hh, c, t in capas:
        ax.add_patch(Rectangle((27, y), 66, hh, fc=c, ec="#b98473", lw=1, zorder=1))
        rot(ax, 25.5, y + hh / 2, t, 15, TINTA, ha="right")
    grados = [("1.er\ngrado", 18, "roja,\nsin ampolla"), ("2.º\nsuperficial", 31, "ampollas,\nse blanquea"),
              ("2.º\nprofundo", 43, "blanquecina,\nduele poco"), ("3.er\ngrado", 52, "escara,\nno duele")]
    for k, (t, yfin, d) in enumerate(grados):
        x = 30 + k * 16
        ax.add_patch(Rectangle((x, 12), 11, yfin - 12, fc="#7f1d1d", alpha=.55, ec="none", zorder=2))
        col = AZUL if k == 1 else ROJO
        rot(ax, x + 5.5, 5.5, t, 14, col)
        rot(ax, x + 5.5, 58.5, d, 13, AZUL if k == 1 else TINTA, "bold" if k == 1 else "normal")
    ax.add_patch(Rectangle((44.5, 10.5), 15, 53, fc="none", ec=AZUL, lw=3, zorder=5))
    guardar(fig, "dib_piel_quemadura.jpg")


# ───────────────────────────────────────────────────────── ubicación de la placenta respecto al OCI
def placenta():
    fig, ax = lienzo(100, 52, "#ffffff")
    tipos = [("NORMAL", (-130, -50), "lejos del cuello"), ("BAJA", (5, 55), "a < 2 cm del OCI\n(este caso: 1 cm)"),
             ("MARGINAL", (5, 89), "llega al borde\ndel OCI"), ("PREVIA TOTAL", (55, 125), "cubre el OCI")]
    for k, (t, (a0, a1), d) in enumerate(tipos):
        cx = 12.5 + k * 25
        ax.add_patch(Ellipse((cx, 21), 20, 28, fc="#fde2e4", ec="#9f1239", lw=2.5, zorder=1))
        ax.add_patch(Rectangle((cx - 2.5, 34.6), 5, 6, fc="#fde2e4", ec="#9f1239", lw=2.5, zorder=1))
        ang = np.radians(np.linspace(a0, a1, 40))
        ax.plot(cx + 8.3 * np.cos(ang), 21 + 12 * np.sin(ang), color="#7f1d1d", lw=11, solid_capstyle="round", zorder=3)
        ax.plot([cx - 1.6, cx + 1.6], [35.3, 35.3], color=TINTA, lw=2.5, zorder=4)
        rot(ax, cx + 4.5, 38.5, "OCI", 11, GRIS, "normal", ha="left")
        col = AZUL if t == "BAJA" else TINTA
        rot(ax, cx, 3, t, 15, col)
        rot(ax, cx, 47, d, 13, col, "normal")
    guardar(fig, "dib_placenta.jpg")


HACER = {"hernia_crural": hernia_crural, "nomograma_paracetamol": nomograma_paracetamol,
         "balanza_ulcera": balanza_ulcera, "hernia_inguinal": hernia_inguinal, "coartacion": coartacion, "canal_endemico": canal_endemico, "kramer": kramer, "tarjeta_heces": tarjeta_heces, "cobb": cobb, "banera": banera, "triangulo_femoral": triangulo_femoral, "pupilas": pupilas, "craneo_rn": craneo_rn, "derrame": derrame, "dengue_pruebas": dengue_pruebas, "regla9": regla9, "cerumen": cerumen, "posturas": posturas, "formula_obstetrica": formula_obstetrica, "partograma": partograma, "piel_quemadura": piel_quemadura, "placenta": placenta}

if __name__ == "__main__":
    for n in sys.argv[1:] or HACER:
        HACER[n]()
