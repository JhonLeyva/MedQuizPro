"""Esquemas propios de la Entrega 3 (cuando no hay foto libre que sirva). Mismo estilo que dibujos29.py.
Uso: python3 dibujos30.py <nombre> (sin argumentos los hace todos)."""
import sys
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
from dibujos29 import lienzo, guardar, rot, TINTA, ROJO, AZUL, GRIS


def calendario_rabia():
    """Profilaxis posexposición de la rabia: lavado el día 0, vacuna días 0-3-7-14 (IM) e inmunoglobulina el día 0
    si la exposición es grave; el perro se observa 10 días."""
    fig, ax = lienzo(100, 66)
    X = lambda d: 10 + d * 5.6          # días 0-15
    rot(ax, 50, 4.5, "Lo que se hace y cuándo (días desde la mordedura)", 20, TINTA)
    # eje
    ax.plot([X(0), X(15)], [30, 30], color=GRIS, lw=3, zorder=2)
    for dd in range(0, 16):
        ax.plot([X(dd), X(dd)], [29, 31], color=GRIS, lw=1.5, zorder=2)
    # lavado
    ax.add_patch(FancyBboxPatch((X(0) - 6.5, 9), 13, 9, boxstyle="round,pad=0.4", fc="#e0f2fe", ec=AZUL, lw=2.5, zorder=3))
    rot(ax, X(0), 11.8, "LAVAR", 19, AZUL)
    rot(ax, X(0), 15.6, "15 min", 17, AZUL, w="normal")
    ax.annotate("", xy=(X(0), 28.6), xytext=(X(0), 18.8), arrowprops=dict(arrowstyle="-|>", lw=2.5, color=AZUL, mutation_scale=18), zorder=4)
    # vacunas
    for dd in (0, 3, 7, 14):
        ax.add_patch(Circle((X(dd), 30), 2.4, fc=ROJO, ec="white", lw=2, zorder=5))
        rot(ax, X(dd), 36.5, f"día {dd}", 19, ROJO)
    rot(ax, X(10.5), 22, "vacuna IM: 4 dosis", 19, ROJO)
    # inmunoglobulina (solo día 0) y observación del perro (días 0-10)
    ax.add_patch(FancyBboxPatch((X(0) - 6.5, 41), 30, 10.5, boxstyle="round,pad=0.4", fc="#fde68a", ec="#b45309", lw=2, zorder=3))
    rot(ax, X(0) + 8.5, 44.2, "+ inmunoglobulina", 17, "#92400e", ha="center")
    rot(ax, X(0) + 8.5, 48.6, "día 0, si es grave", 15, "#92400e", w="normal")
    ax.add_patch(FancyBboxPatch((X(0) - 1, 56), X(10) - X(0) + 2, 6.5, boxstyle="round,pad=0.3", fc="#dcfce7", ec="#15803d", lw=2, zorder=3))
    rot(ax, (X(0) + X(10)) / 2, 59.3, "observar al perro 10 días", 17, "#15803d")
    guardar(fig, "dib_calendario_rabia.jpg")


HACER = {"calendario_rabia": calendario_rabia}

if __name__ == "__main__":
    for n in sys.argv[1:] or HACER:
        HACER[n]()
