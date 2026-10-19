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

def malformacion_anorrectal():
    """Malformación anorrectal en el varón (corte sagital, adelante = izquierda): baja con fístula perineal
    frente a alta con fístula rectouretral (meconio en la orina, periné plano)."""
    from matplotlib.patches import Ellipse, FancyBboxPatch, Arc
    fig, ax = lienzo(100, 66)

    def panel(ox, alta):
        # piel del periné y pene
        ax.plot([ox + 9, ox + 16, ox + 30, ox + 47], [41, 50, 53, 49], color="#9a6b52", lw=3, zorder=3)
        ax.add_patch(FancyBboxPatch((ox + 2, 33), 7, 6, boxstyle="round,pad=1.2", fc="#f6dccb", ec="#9a6b52", lw=2, zorder=2))
        rot(ax, ox + 5.5, 29, "pene", 12, GRIS, w="normal")
        # pubis, vejiga y uretra
        ax.add_patch(FancyBboxPatch((ox + 12, 21), 3, 9, boxstyle="round,pad=0.8", fc="#e7e5e4", ec="#78716c", lw=1.5, zorder=2))
        ax.add_patch(Ellipse((ox + 22, 19), 14, 12, fc="#fef3c7", ec="#ca8a04", lw=2, zorder=3))
        rot(ax, ox + 22, 19, "vejiga", 13, "#92400e", w="normal")
        ax.plot([ox + 22, ox + 22, ox + 15, ox + 5], [25, 40, 42, 36], color="#ca8a04", lw=3, zorder=3)
        rot(ax, ox + 14.5, 45.5, "uretra", 11, "#92400e", w="normal")
        # sacro
        ax.add_patch(Arc((ox + 52, 26), 16, 40, theta1=110, theta2=250, color="#78716c", lw=5, zorder=2))
        # recto
        fondo = 28 if alta else 45
        ax.add_patch(FancyBboxPatch((ox + 32, 8), 8, fondo - 8, boxstyle="round,pad=1.5", fc="#d6b38a", ec="#7c4a1e", lw=2.2, zorder=3))
        rot(ax, ox + 36, 14, "recto", 13, "#7c2d12", w="normal", giro=90)
        if alta:
            ax.plot([ox + 32, ox + 22.5], [29, 38], color=ROJO, lw=3.5, zorder=4)
            ax.annotate("", xy=(ox + 36, 51.5), xytext=(ox + 36, 30.5), arrowprops=dict(arrowstyle="<->", lw=1.8, color=GRIS), zorder=4)
            rot(ax, ox + 40.5, 41, "lejos\n> 1 cm", 11, GRIS, w="normal", fondo="#ffffff")
            rot(ax, ox + 25, 59, "fístula a la uretra (meconio en la orina)", 13, ROJO)
            rot(ax, ox + 25, 63.5, "periné plano, sin ano", 13, TINTA, w="normal")
        else:
            ax.plot([ox + 33, ox + 27], [46, 52.5], color=ROJO, lw=3.5, zorder=4)
            rot(ax, ox + 25, 59, "fístula al periné", 13, ROJO)
            rot(ax, ox + 25, 63.5, "(sale meconio por la piel)", 13, TINTA, w="normal")
        rot(ax, ox + 25, 3, ("ALTA · rectouretral" if alta else "BAJA · perineal"), 16, ROJO if alta else "#15803d")

    panel(1, False)
    panel(51, True)
    ax.plot([50.5, 50.5], [6, 65], color="#cbd5e1", lw=1.5, ls="--")
    guardar(fig, "dib_malformacion_anorrectal.jpg")


def ciclo_familiar():
    """Ciclo vital familiar: formación (pareja), expansión (hijos), dispersión (los hijos se van), contracción (pareja mayor)."""
    from matplotlib.patches import Circle, FancyBboxPatch, Polygon
    fig, ax = lienzo(100, 46)

    def persona(x, y, h, col):
        ax.add_patch(Circle((x, y - h * 0.82), h * 0.17, fc=col, ec="white", lw=1.5, zorder=4))
        ax.add_patch(FancyBboxPatch((x - h * 0.17, y - h * 0.6), h * 0.34, h * 0.6, boxstyle="round,pad=0.4", fc=col, ec="white", lw=1.5, zorder=4))

    def casa(x):
        ax.add_patch(Polygon([(x - 9, 22), (x, 14), (x + 9, 22)], closed=True, fc="#e2e8f0", ec="#94a3b8", lw=1.5, zorder=1))
        ax.add_patch(Rectangle((x - 7.5, 22), 15, 14, fc="#f8fafc", ec="#94a3b8", lw=1.5, zorder=1))

    P1, P2, H = "#0f766e", "#14b8a6", "#f59e0b"
    xs = [11, 36, 61, 89]
    for x in xs:
        casa(x)
    persona(8, 35, 12, P1); persona(14, 35, 12, P2)
    persona(31, 35, 12, P1); persona(36.5, 35, 12, P2); persona(40.5, 35, 7, H); persona(43, 35, 6, H)
    persona(58, 35, 12, P1); persona(64, 35, 12, P2)
    persona(72.5, 35, 10, H); persona(77, 35, 10, H)
    ax.annotate("", xy=(80.5, 17.5), xytext=(69.5, 17.5), arrowprops=dict(arrowstyle="-|>", lw=2.2, color=ROJO), zorder=5)
    rot(ax, 75, 12, "los hijos se van", 14, ROJO, w="normal")
    persona(86, 35, 12, "#64748b"); persona(92, 35, 12, "#94a3b8")
    for x, t, c in zip(xs, ["Formación", "Expansión", "Dispersión", "Contracción"], [TINTA, TINTA, ROJO, TINTA]):
        rot(ax, x, 41.5, t, 16, c)
    for a in (23.5, 48.5):
        ax.annotate("", xy=(a + 1.8, 29), xytext=(a - 1.8, 29), arrowprops=dict(arrowstyle="-|>", lw=2, color=GRIS), zorder=5)
    guardar(fig, "dib_ciclo_familiar.jpg")


def atresia_esofago():
    """Atresia de esófago (Gross): A sin fístula (sin gas en el abdomen), C con fístula distal (85 %, gas en el estómago)
    y H (fístula sin atresia)."""
    from matplotlib.patches import FancyBboxPatch, Ellipse
    fig, ax = lienzo(100, 62)
    TR_, ES = "#cbd5e1", "#fda4af"

    def traquea(ox):
        ax.add_patch(FancyBboxPatch((ox + 7, 8), 5, 30, boxstyle="round,pad=0.6", fc=TR_, ec="#64748b", lw=1.5, zorder=2))
        for k in range(8):
            ax.plot([ox + 6.6, ox + 12.4], [10 + k * 3.6, 10 + k * 3.6], color="#94a3b8", lw=1, zorder=3)
        ax.plot([ox + 9.5, ox + 5], [38.6, 44], color="#64748b", lw=4, zorder=2)
        ax.plot([ox + 9.5, ox + 14], [38.6, 44], color="#64748b", lw=4, zorder=2)

    def estomago(ox, gas):
        ax.add_patch(Ellipse((ox + 21, 51), 15, 10, fc="#fecdd3", ec="#be123c", lw=2, zorder=2))
        if gas:
            ax.add_patch(Ellipse((ox + 21, 48.5), 8, 3.6, fc="#111827", ec="none", zorder=3))
            rot(ax, ox + 21, 58.8, "gas en el estómago", 12, GRIS, w="normal")
        else:
            rot(ax, ox + 21, 58.8, "SIN gas en el abdomen", 12, ROJO)

    def esof(ox, y0, y1):
        ax.add_patch(FancyBboxPatch((ox + 18, y0), 6, y1 - y0, boxstyle="round,pad=0.8", fc=ES, ec="#be123c", lw=1.8, zorder=2))

    # A: bolsón superior ciego + muñón inferior, sin fístula
    traquea(0); esof(0, 6, 22); esof(0, 36, 46); estomago(0, False)
    rot(ax, 21, 28.5, "bolsón\nciego", 12, "#9f1239", w="normal")
    rot(ax, 9.5, 23, "tráquea", 11, "#334155", w="normal", giro=90)
    rot(ax, 28.5, 13, "esófago", 11, "#9f1239", w="normal", giro=90)
    rot(ax, 16.5, 2, "Tipo A (~8 %)", 15, ROJO)
    # C: bolsón superior ciego + fístula del esófago inferior a la tráquea
    o = 34
    traquea(o); esof(o, 6, 20); esof(o, 30, 46); estomago(o, True)
    ax.plot([o + 12.4, o + 18], [31, 33], color=ROJO, lw=3.5, zorder=4)
    rot(ax, o + 27.5, 25.5, "fístula\ndistal", 12, ROJO)
    rot(ax, o + 16.5, 2, "Tipo C (~85 %)", 15, TINTA)
    # H: esófago continuo con fístula
    o = 67
    traquea(o); esof(o, 6, 46); estomago(o, True)
    ax.plot([o + 12.4, o + 18], [20, 22], color=ROJO, lw=3.5, zorder=4)
    rot(ax, o + 21, 30, "fístula\nen H", 12, ROJO, fondo="#ffffff")
    rot(ax, o + 16.5, 2, "Tipo H (~4 %)", 15, TINTA)
    for xx in (33.5, 66.5):
        ax.plot([xx, xx], [5, 61], color="#cbd5e1", lw=1.5, ls="--")
    guardar(fig, "dib_atresia_esofago.jpg")


def hilio_pulmonar():
    """Cara mediastínica de cada pulmón con el hilio: a la derecha el bronquio queda detrás (y arriba, bronquio
    epiarterial) de la arteria; a la izquierda la arteria queda arriba y el bronquio debajo. Venas abajo y adelante."""
    from matplotlib.patches import Ellipse, Circle
    fig, ax = lienzo(100, 66)
    AZ_A, ROJ_V, BR = "#3b82f6", "#ef4444", "#f8fafc"

    def pulmon(cx, titulo, der):
        ax.add_patch(Ellipse((cx, 34), 40, 54, fc="#fde2e4", ec="#be123c", lw=2, zorder=1))
        rot(ax, cx, 3.5, titulo, 16, TINTA)
        # orientación: adelante y atrás
        if der:
            rot(ax, cx - 17, 62.5, "← atrás", 12, GRIS, w="normal"); rot(ax, cx + 15, 62.5, "adelante →", 12, GRIS, w="normal")
            br, ar = (cx - 6, 25), (cx + 5, 31)
        else:
            rot(ax, cx - 15, 62.5, "← adelante", 12, GRIS, w="normal"); rot(ax, cx + 17, 62.5, "atrás →", 12, GRIS, w="normal")
            br, ar = (cx + 1, 37), (cx + 1, 25)
        ax.add_patch(Circle(br, 5, fc=BR, ec="#475569", lw=3, zorder=3))
        ax.add_patch(Circle(br, 2.6, fc="white", ec="#94a3b8", lw=1.5, zorder=4))
        ax.add_patch(Circle(ar, 4.3, fc=AZ_A, ec="#1e3a8a", lw=2, zorder=3))
        vx = cx + 7 if der else cx - 7
        for vy in (42, 49):
            ax.add_patch(Circle((vx, vy), 3.4, fc=ROJ_V, ec="#7f1d1d", lw=2, zorder=3))
        return br, ar, vx

    br, ar, vx = pulmon(25, "Pulmón DERECHO", True)
    rot(ax, br[0] - 1, br[1] - 8.5, "bronquio:\nDETRÁS", 12, TINTA, fondo="#ffffff")
    rot(ax, ar[0] + 9, ar[1] - 4, "arteria", 12, "#1d4ed8", fondo="#ffffff")
    rot(ax, vx + 9, 46, "venas", 12, "#b91c1c", fondo="#ffffff")
    br, ar, vx = pulmon(75, "Pulmón IZQUIERDO", False)
    rot(ax, br[0] + 12, br[1] + 1, "bronquio:\nDEBAJO", 12, TINTA, fondo="#ffffff")
    rot(ax, ar[0] + 11, ar[1] - 2, "arteria:\narriba", 12, "#1d4ed8", fondo="#ffffff")
    rot(ax, vx - 9, 46, "venas", 12, "#b91c1c", fondo="#ffffff")
    guardar(fig, "dib_hilio_pulmonar.jpg")


def lobulos_pulmon():
    """Pulmones de frente: derecho con 3 lóbulos, izquierdo con 2 y la língula (parte del lóbulo superior izquierdo)."""
    from matplotlib.patches import Polygon
    import numpy as np
    fig, ax = lienzo(100, 70)

    def forma(cx, sgn):
        t = np.linspace(0, 1, 60)
        borde_ext = [(cx + sgn * (4 + 22 * np.sin(np.pi * 0.5 * u) ** 0.8), 8 + 52 * u) for u in t]
        borde_int = [(cx + sgn * 3, 60 - 52 * u) for u in t]
        return borde_ext + borde_int

    # derecho (izquierda del dibujo): lóbulos superior, medio e inferior
    ax.add_patch(Polygon(forma(48, -1), closed=True, fc="#fecdd3", ec="#9f1239", lw=2.5, zorder=1))
    ax.add_patch(Polygon([(45, 32), (24, 36), (22, 50), (45, 46)], closed=True, fc="#fde68a", ec="none", zorder=2, alpha=.9))
    ax.plot([45, 24], [32, 36], color="#9f1239", lw=2, zorder=3)
    ax.plot([45, 22], [46, 52], color="#9f1239", lw=2, zorder=3)
    rot(ax, 34, 20, "superior", 13, TINTA, w="normal")
    rot(ax, 34, 42, "medio", 13, "#92400e")
    rot(ax, 33, 56, "inferior", 13, TINTA, w="normal")
    rot(ax, 30, 3.5, "DERECHO: 3 lóbulos", 14, TINTA)
    # izquierdo: superior (con língula) e inferior
    ax.add_patch(Polygon(forma(52, 1), closed=True, fc="#fecdd3", ec="#9f1239", lw=2.5, zorder=1))
    ax.add_patch(Polygon([(55, 40), (61.5, 41), (59.5, 54), (55, 54)], closed=True, fc=ROJO, ec="none", zorder=2, alpha=.75))
    ax.plot([69, 61], [25, 59.5], color="#9f1239", lw=2, zorder=3)
    rot(ax, 62, 20, "superior", 13, TINTA, w="normal")
    rot(ax, 69, 50, "inferior", 13, TINTA, w="normal")
    rot(ax, 86, 42, "LÍNGULA", 14, ROJO, fondo="#ffffff")
    ax.annotate("", xy=(58, 47), xytext=(80, 42), arrowprops=dict(arrowstyle="-|>", lw=2.2, color=ROJO), zorder=5)
    rot(ax, 72, 3.5, "IZQUIERDO: 2 lóbulos", 14, TINTA)
    # tráquea
    ax.plot([50, 50], [0.5, 8], color="#64748b", lw=6, zorder=0)
    rot(ax, 50, 67, "Derecha del paciente = izquierda del dibujo", 11, GRIS, w="normal")
    guardar(fig, "dib_lobulos_pulmon.jpg")


def espirograma():
    """Espirograma: volúmenes (VC, VRI, VRE, VR) y capacidades (CV, CPT, CRF)."""
    import numpy as np
    fig, ax = lienzo(100, 62)
    Y = lambda v: 56 - v * 8.2          # litros a coordenada (0 a 6 L)
    x = np.linspace(4, 70, 600)
    y = []
    for xx in x:
        if xx < 26:
            v = 2.4 + 0.25 * (1 - np.cos(2 * np.pi * (xx - 4) / 7.3))
        elif xx < 36:
            v = 2.4 + (5.8 - 2.4) * np.sin(np.pi / 2 * (xx - 26) / 10)
        elif xx < 48:
            v = 5.8 - (5.8 - 1.2) * np.sin(np.pi / 2 * (xx - 36) / 12)
        else:
            v = 2.4 + 0.25 * (1 - np.cos(2 * np.pi * (xx - 48) / 7.3)) if xx > 52 else 1.2 + (2.4 - 1.2) * (xx - 48) / 4
        y.append(Y(v))
    ax.plot(x, y, color="#0f766e", lw=3, zorder=3)
    for v in (0, 1.2, 2.4, 2.9, 5.8):
        ax.plot([2, 96], [Y(v), Y(v)], color="#e2e8f0", lw=1, zorder=1)
    def llave(xc, v0, v1, txt, col, lado="d"):
        ax.annotate("", xy=(xc, Y(v1)), xytext=(xc, Y(v0)), arrowprops=dict(arrowstyle="<->", lw=2, color=col), zorder=4)
        rot(ax, xc + (1.2 if lado == "d" else -1.2), (Y(v0) + Y(v1)) / 2, txt, 12, col, ha="left" if lado == "d" else "right", fondo="#ffffff")
    llave(73, 2.4, 2.9, "Vol. corriente", "#0f766e")
    llave(73, 2.9, 5.8, "Reserva inspiratoria", "#2563eb")
    llave(73, 1.2, 2.4, "Reserva espiratoria", "#7c3aed")
    llave(73, 0, 1.2, "Volumen residual", GRIS)
    llave(60, 1.2, 5.8, "CAPACIDAD\nVITAL", ROJO, lado="i")
    ax.add_patch(Rectangle((2, Y(1.2)), 94, Y(0) - Y(1.2), fc="#f1f5f9", ec="none", zorder=0))
    rot(ax, 30, Y(0.6), "no se puede expulsar (no entra en la CV)", 12, GRIS, w="normal")
    rot(ax, 50, 3, "Capacidad pulmonar total = CV + volumen residual", 14, TINTA)
    guardar(fig, "dib_espirograma.jpg")


def galeazzi():
    """Displasia de cadera izquierda: signo de Galeazzi (rodilla izquierda más baja con caderas y rodillas flexionadas)
    y pliegues del muslo asimétricos (vista posterior)."""
    from matplotlib.patches import FancyBboxPatch, Ellipse, Arc
    fig, ax = lienzo(100, 62)
    PIEL, BORDE = "#f6dccb", "#9a6b52"
    # panel 1: de frente, rodillas flexionadas (izquierda del paciente = derecha del dibujo)
    ax.plot([3, 47], [52, 52], color=GRIS, lw=3)
    for x0, top, col in ((12, 18, BORDE), (28, 26, ROJO)):
        ax.add_patch(FancyBboxPatch((x0, top), 9, 52 - top, boxstyle="round,pad=1.2", fc=PIEL, ec=col, lw=2.5, zorder=2))
        ax.add_patch(Ellipse((x0 + 4.5, top), 11, 6, fc=PIEL, ec=col, lw=2.5, zorder=3))
    ax.plot([8, 44], [18, 18], color="#2563eb", lw=1.6, ls="--", zorder=4)
    ax.annotate("", xy=(42, 26), xytext=(42, 18), arrowprops=dict(arrowstyle="<->", lw=2, color="#2563eb"), zorder=5)
    rot(ax, 16.5, 57, "derecha", 12, GRIS, w="normal"); rot(ax, 32.5, 57, "izquierda", 12, ROJO)
    rot(ax, 25, 5, "Signo de Galeazzi", 15, TINTA)
    rot(ax, 25, 10.5, "rodilla izquierda más baja", 12, ROJO, w="normal")
    ax.plot([50, 50], [3, 60], color="#cbd5e1", lw=1.5, ls="--")
    # panel 2: vista posterior, pliegues (izquierda del paciente = izquierda del dibujo)
    for cx, n, col in ((64, 3, ROJO), (84, 2, BORDE)):
        ax.add_patch(Ellipse((cx, 22), 19, 16, fc=PIEL, ec=BORDE, lw=2, zorder=1))
        ax.add_patch(FancyBboxPatch((cx - 7, 27), 14, 25, boxstyle="round,pad=1", fc=PIEL, ec=BORDE, lw=2, zorder=1))
        for k in range(n):
            yy = 31 + k * 6
            ax.add_patch(Arc((cx, yy), 12, 4, theta1=200, theta2=340, color=col, lw=2.4, zorder=3))
    ax.plot([74, 74], [15, 29], color=BORDE, lw=2, zorder=2)
    rot(ax, 64, 57, "izquierda", 12, ROJO); rot(ax, 84, 57, "derecha", 12, GRIS, w="normal")
    rot(ax, 74, 5, "Pliegues asimétricos", 15, TINTA)
    rot(ax, 74, 10.5, "vista de espaldas", 12, GRIS, w="normal")
    guardar(fig, "dib_galeazzi.jpg")


HACER["galeazzi"] = galeazzi
HACER["hilio_pulmonar"] = hilio_pulmonar
HACER["lobulos_pulmon"] = lobulos_pulmon
HACER["espirograma"] = espirograma
HACER["atresia_esofago"] = atresia_esofago
HACER["ciclo_familiar"] = ciclo_familiar
HACER["malformacion_anorrectal"] = malformacion_anorrectal


# ── Revisión de la Entrega 3: celdas que no tenían imagen (letra grande: la celda se ve a ~45 %)
def _pared(ax):
    """Corte de lado del abdomen bajo: pared a la izquierda, ombligo arriba."""
    from matplotlib.patches import Ellipse
    ax.add_patch(Rectangle((2, 6), 8, 52, fc="#f6dccb", ec="#b45309", lw=1.5, zorder=1))
    ax.add_patch(Ellipse((6, 12), 7, 5, fc="#e8b796", ec="#b45309", lw=1, zorder=2))
    rot(ax, 9, 3, "ombligo", 13, TINTA)


def uraco_permeable():
    from matplotlib.patches import Ellipse
    fig, ax = lienzo(60, 60, px=(340, None))
    _pared(ax)
    ax.add_patch(Ellipse((32, 47), 26, 18, fc="#fde68a", ec="#b45309", lw=1.5, zorder=2))
    rot(ax, 32, 47, "vejiga", 14, "#92400e")
    ax.plot([10, 14, 21], [12, 30, 42], color="#b45309", lw=9.9, solid_capstyle="round", zorder=2)
    ax.plot([10, 14, 21], [12, 30, 42], color="#fde68a", lw=6.8, solid_capstyle="round", zorder=3)
    rot(ax, 37, 26, "uraco\nabierto", 14, "#92400e")
    for k in range(3):
        ax.add_patch(Circle((14 + k * 3.4, 9 + k * 0.5), 1.1, fc="#facc15", ec="#a16207", zorder=4))
    rot(ax, 40, 11, "sale orina", 14, ROJO)
    guardar(fig, "dib_uraco.jpg")


def onfalomesenterico():
    fig, ax = lienzo(60, 60, px=(340, None))
    _pared(ax)
    xs = [28, 34, 40, 46, 52, 54, 50, 44, 38, 32, 27, 28]
    ys = [46, 43, 45, 43, 45, 51, 55, 53, 55, 53, 50, 46]
    ax.plot(xs, ys, color="#be185d", lw=15.3, solid_capstyle="round", solid_joinstyle="round", zorder=2)
    ax.plot(xs, ys, color="#fbcfe8", lw=11.2, solid_capstyle="round", solid_joinstyle="round", zorder=3)
    rot(ax, 41, 49, "íleon", 13, "#9d174d", z=12)
    ax.plot([10, 18, 28], [12, 28, 45], color="#be185d", lw=9.9, solid_capstyle="round", zorder=2)
    ax.plot([10, 18, 28], [12, 28, 45], color="#fbcfe8", lw=6.8, solid_capstyle="round", zorder=3)
    rot(ax, 39, 27, "conducto\nabierto", 14, "#9d174d")
    for k in range(3):
        ax.add_patch(Circle((14 + k * 3.4, 9 + k * 0.5), 1.1, fc="#a16207", ec="#713f12", zorder=4))
    rot(ax, 41, 11, "sale heces", 14, ROJO)
    guardar(fig, "dib_onfalomesenterico.jpg")


def prerrenal():
    from matplotlib.patches import Ellipse
    fig, ax = lienzo(60, 46, px=(340, None))
    ax.add_patch(Ellipse((12, 12), 18, 15, fc="#fecaca", ec=ROJO, lw=1.5, zorder=2))
    rot(ax, 12, 12, "corazón", 13, "#991b1b")
    ax.plot([21, 28, 28], [12, 12, 44], color=ROJO, lw=7.2, zorder=1)
    ax.plot([28, 43], [27, 27], color=ROJO, lw=2.2, ls=(0, (3, 2)), zorder=2)
    ax.add_patch(Ellipse((49, 27), 11, 20, fc="#fde2e4", ec="#9f1239", lw=1.5, zorder=3))
    rot(ax, 49, 27, "riñón\nsano", 12, "#9f1239")
    rot(ax, 44, 9, "llega\npoca sangre", 13, ROJO)
    rot(ax, 13, 35, "deshidratación\nhipotensión", 12, TINTA)
    guardar(fig, "dib_prerrenal.jpg")


def globo_vesical():
    from matplotlib.patches import Ellipse, Arc
    fig, ax = lienzo(60, 54, px=(340, None))
    ax.add_patch(Ellipse((30, 22), 34, 30, fc="#fde68a", ec="#b45309", lw=1.4, zorder=2))
    rot(ax, 30, 20, "vejiga\nllena", 16, "#92400e")
    ax.add_patch(Arc((30, 46), 40, 12, theta1=200, theta2=340, ec="#64748b", lw=2.7, zorder=4))
    rot(ax, 8, 46, "pubis", 12, GRIS)
    ax.plot([30, 30], [37, 53], color="#b45309", lw=5.4, zorder=3)
    ax.add_patch(Circle((30, 42), 2.2, fc="#7f1d1d", ec="none", zorder=5))
    rot(ax, 47, 44, "coágulo\no cálculo", 12, ROJO)
    guardar(fig, "dib_globo_vesical.jpg")


HACER.update(uraco_permeable=uraco_permeable, onfalomesenterico=onfalomesenterico, prerrenal=prerrenal, globo_vesical=globo_vesical)


def gram_pmn():
    """Gram de secreción uretral con neutrófilos y sin bacterias visibles (Chlamydia o Mycoplasma)."""
    import random
    from matplotlib.patches import Ellipse
    r = random.Random(3)
    fig, ax = lienzo(60, 60, px=(340, None))
    ax.add_patch(Circle((30, 26), 24, fc="#fde7ef", ec="#94a3b8", lw=1.4, zorder=1))
    for cx, cy in [(20, 16), (36, 14), (42, 30), (24, 34), (32, 40), (14, 28), (44, 20)]:
        ax.add_patch(Circle((cx, cy), 4.2, fc="#fbcfe8", ec="#db2777", lw=1.2, zorder=2))
        for k in range(3):
            ax.add_patch(Ellipse((cx - 1.8 + k * 1.8, cy + r.uniform(-1, 1)), 1.8, 2.4, fc="#7e22ce", ec="none", zorder=3))
    rot(ax, 30, 55, "solo neutrófilos:\nel germen no se ve", 13, "#7e22ce")
    guardar(fig, "dib_gram_pmn.jpg")
HACER["gram_pmn"] = gram_pmn


def beriberi():
    """Las dos formas del beriberi: seco (nervios) y húmedo (corazón con edema)."""
    from matplotlib.patches import Ellipse
    fig, ax = lienzo(60, 46, px=(340, None))
    ax.plot([30, 30], [4, 42], color="#cbd5e1", lw=1, ls="--")
    rot(ax, 15, 5, "SECO", 14, "#7e22ce")
    ax.plot([10, 10, 20], [12, 34, 38], color="#7e22ce", lw=4.5, solid_capstyle="round")
    rot(ax, 15, 43, "nervios:\npie caído", 11, "#7e22ce")
    rot(ax, 45, 5, "HÚMEDO", 14, ROJO)
    ax.add_patch(Ellipse((45, 18), 18, 14, fc="#fecaca", ec=ROJO, lw=1.4))
    rot(ax, 45, 18, "corazón\ngrande", 10, "#991b1b")
    for k in range(4):
        ax.add_patch(Circle((38 + k * 4.5, 32), 1.6, fc="#bae6fd", ec="#0369a1", lw=1.5))
    rot(ax, 45, 41, "edema", 12, "#0369a1")
    guardar(fig, "dib_beriberi.jpg")
HACER["beriberi"] = beriberi


def naat():
    """Prueba molecular (NAAT/PCR) en orina: así se diagnostican Chlamydia y Mycoplasma."""
    fig, ax = lienzo(50, 50, px=(340, None))
    ax.add_patch(FancyBboxPatch((18, 6), 14, 30, boxstyle="round,pad=1.2", fc="#fef9c3", ec="#a16207", lw=1.4))
    ax.add_patch(Rectangle((17, 3), 16, 5, fc="#64748b", ec="#334155", lw=1))
    rot(ax, 25, 22, "orina", 12, "#a16207")
    rot(ax, 25, 44, "PCR (NAAT)", 16, "#0f766e")
    guardar(fig, "dib_naat.jpg")
HACER["naat"] = naat


def ulcera_idiopatica():
    """Úlcera esofágica idiopática del VIH: grande, y la biopsia no muestra virus ni hongos."""
    from matplotlib.patches import Ellipse
    fig, ax = lienzo(50, 50, px=(340, None))
    ax.add_patch(Circle((25, 21), 18, fc="#fbcfe8", ec="#be185d", lw=1.4))
    ax.add_patch(Circle((25, 21), 6, fc="#3f0d1f", ec="none"))
    ax.add_patch(Ellipse((15, 26), 10, 6, fc="#fef3c7", ec="#b45309", lw=1.5))
    rot(ax, 25, 44, "biopsia: sin virus\nni hongos", 12, "#9d174d")
    guardar(fig, "dib_ulcera_idiopatica.jpg")
HACER["ulcera_idiopatica"] = ulcera_idiopatica

if __name__ == "__main__":
    for n in sys.argv[1:] or HACER:
        HACER[n]()
