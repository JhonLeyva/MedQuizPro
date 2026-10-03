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


HACER = {"hernia_crural": hernia_crural, "nomograma_paracetamol": nomograma_paracetamol,
         "balanza_ulcera": balanza_ulcera, "hernia_inguinal": hernia_inguinal, "coartacion": coartacion, "canal_endemico": canal_endemico, "kramer": kramer, "tarjeta_heces": tarjeta_heces}

if __name__ == "__main__":
    for n in sys.argv[1:] or HACER:
        HACER[n]()
