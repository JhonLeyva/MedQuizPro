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


HACER = {"hernia_crural": hernia_crural, "nomograma_paracetamol": nomograma_paracetamol}

if __name__ == "__main__":
    for n in sys.argv[1:] or HACER:
        HACER[n]()
