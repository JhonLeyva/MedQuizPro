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


def muestreo():
    """Muestreo sistemático: arranque al azar y luego 1 de cada k (k = 3)."""
    from matplotlib.patches import Circle
    fig, ax = lienzo(100, 46)
    rot(ax, 50, 4.5, "Lista de pacientes: arranque al azar y luego 1 de cada 3", 19, TINTA)
    n = 15
    for i in range(n):
        x = 6 + i * 6.3
        sel = (i - 1) % 3 == 0 and i >= 1
        ax.add_patch(Circle((x, 20), 2.4, fc=ROJO if sel else "#e5e7eb", ec=TINTA if sel else GRIS, lw=1.5, zorder=3))
        rot(ax, x, 26.5, str(i + 1), 13, ROJO if sel else GRIS, w="bold" if sel else "normal")
    ax.annotate("", xy=(6 + 6.3, 16.8), xytext=(6 + 6.3, 10), arrowprops=dict(arrowstyle="-|>", lw=2.5, color=AZUL, mutation_scale=16))
    rot(ax, 6 + 6.3 + 2, 9.5, "al azar", 15, AZUL, ha="left")
    for i in range(1, 12, 3):
        x0, x1 = 6 + i * 6.3, 6 + (i + 3) * 6.3
        ax.annotate("", xy=(x1 - 1.5, 32), xytext=(x0 + 1.5, 32), arrowprops=dict(arrowstyle="-|>", lw=2, color=ROJO, mutation_scale=14,
                    connectionstyle="arc3,rad=0.35"))
        rot(ax, (x0 + x1) / 2, 39, "k = 3", 13, ROJO)
    guardar(fig, "dib_muestreo.jpg")


def tacto_rectal():
    """Tacto rectal: el dedo palpa la cara posterior de la próstata; normal, hiperplasia benigna y cáncer."""
    from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon
    fig, ax = lienzo(100, 50)
    rot(ax, 50, 4, "Qué siente el dedo en la cara posterior de la próstata", 18, TINTA)
    datos = [("NORMAL", "como la punta de la nariz:\nlisa, surco central", 7, "#fbcfe8", False),
             ("HIPERPLASIA BENIGNA", "grande, lisa, elástica;\nse borra el surco", 10, "#f9a8d4", False),
             ("CÁNCER", "nódulo duro, pétreo,\nirregular", 8, "#fbcfe8", True)]
    for k, (t, sub, r, col, nod) in enumerate(datos):
        cx = 17 + k * 33
        ax.add_patch(Ellipse((cx, 23), 2.2 * r, 1.5 * r, fc=col, ec="#9d174d", lw=2.5, zorder=3))
        if k != 1:
            ax.plot([cx, cx], [23 - 0.6 * r, 23 + 0.6 * r], color="#9d174d", lw=2, ls="--", zorder=4)
        if nod:
            ax.add_patch(Ellipse((cx + 3.5, 21), 4, 3.2, fc="#7f1d1d", ec="#450a0a", lw=1.5, zorder=5))
        rot(ax, cx, 37.5, t, 15, ROJO if nod else TINTA)
        rot(ax, cx, 44.5, sub, 13, GRIS, w="normal")
    guardar(fig, "dib_tacto_rectal.jpg")


def regla9_adulto():
    """Regla de los 9 de Wallace (adulto), sin marcar un caso: cada zona con su porcentaje."""
    from matplotlib.patches import Circle, Rectangle, Polygon
    fig, ax = lienzo(100, 70, "#ffffff")
    SANA, BORDE = "#f6dccb", "#9a6b52"

    def figura(cx, titulo):
        ax.add_patch(Circle((cx, 12), 4.5, fc=SANA, ec=BORDE, lw=2, zorder=2))
        ax.add_patch(Rectangle((cx - 7, 17.5), 14, 20, fc="#fde2d2", ec=BORDE, lw=2, zorder=2))
        for dx in (-1, 1):
            ax.add_patch(Polygon([(cx + dx * 7, 18), (cx + dx * 11.5, 19.5), (cx + dx * 13.5, 36), (cx + dx * 10.5, 36.5), (cx + dx * 8.5, 22)],
                                 closed=True, fc=SANA, ec=BORDE, lw=2, zorder=2))
            ax.add_patch(Rectangle((cx + (0.3 if dx > 0 else -6.8), 37.5), 6.5, 22, fc=SANA, ec=BORDE, lw=2, zorder=2))
        rot(ax, cx, 12, "4,5", 14, TINTA)
        rot(ax, cx, 27, "18", 18, ROJO)
        rot(ax, cx - 13, 28, "4,5", 14, TINTA)
        rot(ax, cx + 13, 28, "4,5", 14, TINTA)
        rot(ax, cx - 3.5, 49, "9", 15, TINTA)
        rot(ax, cx + 3.5, 49, "9", 15, TINTA)
        rot(ax, cx, 3.5, titulo, 16, GRIS)
    figura(24, "ADELANTE")
    figura(64, "ATRÁS")
    rot(ax, 90, 30, "cabeza 9\nbrazo 9\npierna 18\ntronco 36\nperiné 1", 14, TINTA, w="normal")
    rot(ax, 44, 66, "Suma: 9 + 9 + 9 + 18 + 18 + 36 + 1 = 100 %", 16, ROJO)
    guardar(fig, "dib_regla9_adulto.jpg")


def pictograma_ataque():
    """Tasa de ataque: 200 comensales, 80 enfermos (40 %)."""
    from matplotlib.patches import Circle
    fig, ax = lienzo(100, 52)
    rot(ax, 50, 4, "200 almorzaron (expuestos) · 80 enfermaron", 19, TINTA)
    for i in range(200):
        r, c = divmod(i, 25)
        x, y = 8 + c * 3.4, 11 + r * 3.6
        ax.add_patch(Circle((x, y), 1.25, fc=ROJO if i < 80 else "#d1d5db", ec="none", zorder=3))
    rot(ax, 50, 44, "Tasa de ataque = 80 / 200 × 100 = 40 %", 20, ROJO)
    rot(ax, 50, 49.5, "rojo = enfermó en las 24 h · gris = expuesto sano", 14, GRIS, w="normal")
    guardar(fig, "dib_ataque.jpg")


def mano_cubital():
    """Palma derecha: territorio sensitivo del cubital (4.º-5.º dedo) y del mediano; canal de Guyon y túnel carpiano."""
    from matplotlib.patches import Polygon, FancyBboxPatch, Ellipse, Rectangle
    fig, ax = lienzo(100, 80)
    PIEL2 = "#f6dccb"
    # palma
    ax.add_patch(FancyBboxPatch((30, 34), 40, 30, boxstyle="round,pad=2", fc=PIEL2, ec="#9a6b52", lw=2, zorder=2))
    dedos = [(33, 10, 7, 26), (41.5, 4, 7, 32), (50, 6, 7, 30), (58.5, 12, 7, 24)]
    for k, (x, y, w, h) in enumerate(dedos):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1.4", fc=PIEL2, ec="#9a6b52", lw=2, zorder=1))
    ax.add_patch(Polygon([(70, 60), (78, 46), (84, 36), (90, 38), (88, 46), (80, 60), (72, 66)], closed=True, fc=PIEL2, ec="#9a6b52", lw=2, zorder=1))
    ax.add_patch(Rectangle((34, 64), 32, 14, fc=PIEL2, ec="#9a6b52", lw=2, zorder=1))
    # territorio cubital: dedo meñique + mitad del anular + borde cubital de la palma (a la izquierda = palma derecha vista de frente)
    ax.add_patch(Polygon([(29.5, 66), (29.5, 36), (31.5, 14), (40.5, 12), (44, 40), (44, 66)], closed=True, fc="#fde047", alpha=0.75, ec="none", zorder=4))
    ax.add_patch(Polygon([(44, 66), (44, 40), (41.5, 5), (66.5, 11), (72, 34), (72, 66)], closed=True, fc="#93c5fd", alpha=0.6, ec="none", zorder=4))
    # canal de Guyon y túnel carpiano
    ax.add_patch(Ellipse((37, 66), 7, 4.5, fc="#dc2626", ec="white", lw=2, zorder=6))
    ax.add_patch(Ellipse((54, 67), 12, 5, fc="#1d4ed8", ec="white", lw=2, zorder=6))
    rot(ax, 37, 73, "canal de\nGuyon", 14, "#b91c1c", z=7)
    rot(ax, 56, 74, "túnel carpiano", 14, "#1d4ed8", z=7)
    rot(ax, 15, 30, "CUBITAL\n4.º (mitad)\ny 5.º dedo", 15, "#a16207")
    rot(ax, 88, 18, "MEDIANO\n1.º a 4.º\n(mitad)", 15, "#1d4ed8")
    rot(ax, 50, 2.5, "Palma de la mano derecha", 15, GRIS)
    guardar(fig, "dib_mano_cubital.jpg")


def hernias_pared():
    """Pared abdominal anterior: dónde sale cada hernia o bulto de la línea media."""
    from matplotlib.patches import Ellipse, FancyBboxPatch, Circle
    fig, ax = lienzo(100, 70)
    ax.add_patch(FancyBboxPatch((27, 6), 46, 56, boxstyle="round,pad=3", fc="#f6dccb", ec="#9a6b52", lw=2, zorder=1))
    ax.plot([50, 50], [8, 62], color="#9a6b52", lw=2, ls="--", zorder=2)
    rot(ax, 50, 67.5, "línea alba (punteada)", 13, GRIS)
    ax.add_patch(Circle((50, 38), 1.6, fc="#9a6b52", zorder=3))
    ax.add_patch(Ellipse((50, 22), 7, 5.5, fc="#f87171", ec="#991b1b", lw=2, zorder=4))
    ax.add_patch(Ellipse((50, 38), 6, 5, fc="#fdba74", ec="#9a3412", lw=2, zorder=3, alpha=0.8))
    ax.add_patch(Ellipse((50, 30), 9, 26, fc="none", ec="#2563eb", lw=2, ls=":", zorder=3))
    ax.add_patch(Ellipse((62, 50), 5, 4.5, fc="#c4b5fd", ec="#5b21b6", lw=2, zorder=3))
    rot(ax, 13, 15, "EPIGÁSTRICA", 15, "#991b1b")
    rot(ax, 13, 22, "sobre el ombligo,\nen la línea alba", 13, "#991b1b", w="normal")
    ax.annotate("", xy=(46, 22), xytext=(26, 22), arrowprops=dict(arrowstyle="-|>", lw=2, color="#991b1b"))
    rot(ax, 13, 39, "UMBILICAL", 15, "#9a3412")
    rot(ax, 13, 44.5, "en el ombligo", 13, "#9a3412", w="normal")
    ax.annotate("", xy=(47, 38), xytext=(25, 41), arrowprops=dict(arrowstyle="-|>", lw=2, color="#9a3412"))
    rot(ax, 88, 17, "DIÁSTASIS", 15, "#1d4ed8")
    rot(ax, 88, 24.5, "rectos separados,\nsin anillo ni saco", 12, "#1d4ed8", w="normal")
    ax.annotate("", xy=(55, 26), xytext=(76, 23), arrowprops=dict(arrowstyle="-|>", lw=2, color="#1d4ed8"))
    rot(ax, 88, 48, "SPIEGEL", 15, "#5b21b6")
    rot(ax, 88, 55, "borde lateral\ndel recto", 12, "#5b21b6", w="normal")
    ax.annotate("", xy=(65, 50), xytext=(77, 52), arrowprops=dict(arrowstyle="-|>", lw=2, color="#5b21b6"))
    guardar(fig, "dib_hernias_pared.jpg")


def torsion_testicular():
    """Torsión del testículo derecho (izquierda del dibujo): alto, horizontal y con el cordón enrollado."""
    import numpy as np
    from matplotlib.patches import Ellipse, FancyBboxPatch
    fig, ax = lienzo(100, 70)
    ax.add_patch(FancyBboxPatch((22, 26), 56, 38, boxstyle="round,pad=6", fc="#f6dccb", ec="#9a6b52", lw=2, zorder=1))
    ax.plot([50, 50], [24, 66], color="#9a6b52", lw=1.5, ls="--", zorder=2)
    # lado sano (derecha del dibujo = izquierda del paciente): vertical y bajo
    ax.plot([64, 64], [2, 38], color="#60a5fa", lw=6, zorder=3)
    ax.add_patch(Ellipse((64, 48), 13, 19, fc="#fde2d2", ec="#7c2d12", lw=2.5, zorder=4))
    # lado torcido: alto, horizontal, rojo, cordón en espiral
    t = np.linspace(0, 1, 200)
    ax.plot(36 + 2.8 * np.sin(t * 6 * np.pi), 2 + 26 * t, color="#2563eb", lw=6, zorder=3)
    ax.add_patch(Ellipse((36, 33), 20, 12, fc="#fca5a5", ec="#b91c1c", lw=3, zorder=4))
    rot(ax, 16, 10, "cordón\ntorcido", 15, "#1d4ed8")
    rot(ax, 15, 33, "ALTO Y\nHORIZONTAL", 15, ROJO)
    rot(ax, 87, 48, "sano:\nvertical", 15, TINTA, w="normal")
    rot(ax, 50, 68, "Derecha del paciente = izquierda del dibujo", 13, GRIS, w="normal")
    guardar(fig, "dib_torsion.jpg")


def compartimentos_pierna():
    """Corte de la pierna: los 4 compartimentos encerrados por fascias que no se estiran."""
    from matplotlib.patches import Ellipse, Wedge, Circle
    fig, ax = lienzo(100, 70)
    ax.add_patch(Ellipse((50, 36), 70, 56, fc="#f6dccb", ec="#9a6b52", lw=3, zorder=1))
    cols = [("#fca5a5", "ANTERIOR", (35, 18)), ("#fdba74", "LATERAL", (20, 38)), ("#fde68a", "POST.\nSUPERFICIAL", (52, 56)), ("#c4b5fd", "POST.\nPROFUNDO", (60, 36))]
    ax.add_patch(Wedge((50, 36), 25, 110, 200, fc=cols[0][0], ec="#7c2d12", lw=2, zorder=2))
    ax.add_patch(Wedge((50, 36), 25, 200, 245, fc=cols[1][0], ec="#7c2d12", lw=2, zorder=2))
    ax.add_patch(Wedge((50, 36), 25, 245, 330, fc=cols[3][0], ec="#7c2d12", lw=2, zorder=2))
    ax.add_patch(Wedge((50, 36), 25, 330, 470, fc=cols[2][0], ec="#7c2d12", lw=2, zorder=2))
    ax.add_patch(Circle((40, 30), 4.5, fc="white", ec="#475569", lw=2.5, zorder=3))
    ax.add_patch(Circle((32, 44), 2.5, fc="white", ec="#475569", lw=2.5, zorder=3))
    rot(ax, 40, 30, "tibia", 11, TINTA, z=4)
    rot(ax, 24, 50, "peroné", 11, TINTA)
    for c, n, (x, y) in cols:
        rot(ax, x + 8, y, n, 12, "#7f1d1d")
    rot(ax, 50, 3, "Fascias rígidas: si el músculo se hincha, sube la presión y no llega sangre", 14, ROJO)
    guardar(fig, "dib_compartimentos.jpg")


def variables():
    """Experimento: la variable independiente se manipula (música) y la dependiente se mide (analgésicos)."""
    from matplotlib.patches import FancyBboxPatch
    fig, ax = lienzo(100, 50)
    for x, t, sub, col in ((4, "VARIABLE INDEPENDIENTE", "la que el investigador\nCAMBIA: música sí / no", AZUL),
                           (58, "VARIABLE DEPENDIENTE", "la que se MIDE:\nuso de analgésicos", ROJO)):
        ax.add_patch(FancyBboxPatch((x, 12), 38, 22, boxstyle="round,pad=1.2", fc="white", ec=col, lw=3))
        rot(ax, x + 19, 17.5, t, 14, col)
        rot(ax, x + 19, 27, sub, 14, TINTA, w="normal")
    ax.annotate("", xy=(57, 23), xytext=(43, 23), arrowprops=dict(arrowstyle="-|>", lw=4, color=TINTA, mutation_scale=26))
    rot(ax, 50, 18, "causa", 13, GRIS)
    rot(ax, 50, 43, "El ruido del servicio es una variable extraña: se controla (igual para todos)", 14, GRIS, w="normal")
    rot(ax, 50, 4, "¿La música de fondo cambia el uso de analgésicos?", 17, TINTA)
    guardar(fig, "dib_variables.jpg")


def correlacion():
    """Cuatro nubes de puntos: correlación positiva, negativa, nula y no lineal."""
    import numpy as np
    from matplotlib.patches import Rectangle
    rng = np.random.default_rng(3)
    fig, ax = lienzo(100, 34)
    paneles = [("positiva (r ≈ +0,8)", lambda x: x), ("negativa (r ≈ −0,8)", lambda x: 1 - x), ("nula (r ≈ 0)", None), ("curva (r bajo)", lambda x: 4 * (x - 0.5) ** 2)]
    for k, (t, f) in enumerate(paneles):
        x0 = 2 + k * 25
        ax.add_patch(Rectangle((x0, 6), 21, 21, fc="#f8fafc", ec=GRIS, lw=1.5))
        xs = rng.random(30)
        ys = rng.random(30) if f is None else np.clip(f(xs) + rng.normal(0, 0.09, 30), 0, 1)
        ax.scatter(x0 + 1.5 + xs * 18, 25.5 - ys * 18, s=22, color=ROJO if k < 2 else AZUL, zorder=3)
        rot(ax, x0 + 10.5, 31, t, 13, TINTA)
    rot(ax, 50, 2.5, "La correlación mide si dos variables se mueven juntas (asociación), no la causa", 14, GRIS, w="normal")
    guardar(fig, "dib_correlacion.jpg")


def placa_motora():
    """Unión neuromuscular: terminal con vesículas de acetilcolina, hendidura y receptores; dónde actúa cada enfermedad."""
    from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
    fig, ax = lienzo(100, 64)
    ax.add_patch(FancyBboxPatch((28, 4), 44, 20, boxstyle="round,pad=2", fc="#fde68a", ec="#92400e", lw=2.5))
    rot(ax, 50, 7.5, "terminal del nervio", 14, "#92400e")
    for x in (36, 44, 52, 60):
        ax.add_patch(Circle((x, 16), 2.6, fc="white", ec="#92400e", lw=1.8))
        for dx, dy in ((-0.8, -0.6), (0.7, 0.2), (-0.1, 0.9)):
            ax.add_patch(Circle((x + dx, 16 + dy), 0.45, fc="#2563eb"))
    ax.add_patch(Rectangle((22, 38), 56, 22, fc="#fecaca", ec="#991b1b", lw=2.5))
    rot(ax, 50, 56, "músculo (placa motora)", 14, "#991b1b")
    for x in range(26, 76, 7):
        ax.add_patch(Rectangle((x, 37), 3.4, 3, fc="#16a34a", ec="#14532d", lw=1))
    for x in (33, 47, 61):
        ax.add_patch(Polygon([(x, 33.5), (x + 3, 33.5), (x + 1.5, 36.6)], closed=True, fc="#7c3aed", ec="#4c1d95"))
    rot(ax, 89, 37, "receptores\nde ACh", 13, "#15803d")
    rot(ax, 89, 30, "anticuerpos\n(miastenia)", 13, "#6d28d9")
    rot(ax, 12, 16, "canales de\ncalcio\n(Lambert-\nEaton)", 12, "#92400e")
    rot(ax, 50, 29.5, "hendidura: acetilcolinesterasa", 12, GRIS, w="normal")
    guardar(fig, "dib_placa_motora.jpg")


def cadera_rotacion():
    """Fractura de cadera derecha: pierna derecha (izquierda del dibujo) más corta y con el pie girado hacia afuera."""
    from matplotlib.patches import FancyBboxPatch, Ellipse, Polygon
    fig, ax = lienzo(100, 80)
    ax.add_patch(FancyBboxPatch((30, 4), 40, 14, boxstyle="round,pad=2", fc="#f6dccb", ec="#9a6b52", lw=2))
    rot(ax, 50, 10, "pelvis (paciente acostada)", 13, GRIS, w="normal")
    # pierna sana (derecha del dibujo = izquierda del paciente)
    ax.add_patch(FancyBboxPatch((53, 18), 10, 52, boxstyle="round,pad=1.5", fc="#f6dccb", ec="#9a6b52", lw=2))
    ax.add_patch(Ellipse((58, 73), 6, 6, fc="#f6dccb", ec="#9a6b52", lw=2))
    # pierna fracturada: más corta y pie rotado hacia afuera (a la izquierda del dibujo)
    ax.add_patch(FancyBboxPatch((37, 18), 10, 45, boxstyle="round,pad=1.5", fc="#fde2d2", ec=ROJO, lw=2.5))
    ax.add_patch(Polygon([(37, 64), (47, 64), (40, 73), (30, 70)], closed=True, fc="#fde2d2", ec=ROJO, lw=2.5))
    ax.plot([47, 66], [63.5, 63.5], color=AZUL, lw=1.5, ls="--")
    ax.plot([47, 66], [70.5, 70.5], color=AZUL, lw=1.5, ls="--")
    ax.annotate("", xy=(68, 63.5), xytext=(68, 70.5), arrowprops=dict(arrowstyle="<|-|>", lw=2, color=AZUL))
    rot(ax, 80, 67, "más corta", 15, AZUL)
    ax.annotate("", xy=(27, 72), xytext=(36, 76), arrowprops=dict(arrowstyle="-|>", lw=3, color=ROJO, connectionstyle="arc3,rad=-0.4"))
    rot(ax, 15, 60, "rotación\nexterna", 15, ROJO)
    ax.add_patch(Ellipse((42, 22), 6, 4, fc="none", ec=ROJO, lw=2.5, ls="--"))
    rot(ax, 18, 24, "fractura del\ncuello femoral", 14, ROJO)
    rot(ax, 50, 79, "Derecha de la paciente = izquierda del dibujo", 12, GRIS, w="normal")
    guardar(fig, "dib_cadera.jpg")


HACER = {"cadera_rotacion": cadera_rotacion, "placa_motora": placa_motora, "variables": variables, "correlacion": correlacion, "torsion_testicular": torsion_testicular, "compartimentos_pierna": compartimentos_pierna, "pictograma_ataque": pictograma_ataque, "mano_cubital": mano_cubital, "hernias_pared": hernias_pared, "regla9_adulto": regla9_adulto, "calendario_rabia": calendario_rabia, "muestreo": muestreo, "tacto_rectal": tacto_rectal}

if __name__ == "__main__":
    for n in sys.argv[1:] or HACER:
        HACER[n]()
