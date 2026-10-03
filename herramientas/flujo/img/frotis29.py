"""Frotis de sangre periférica dibujados (Entrega 2), con tinción tipo Wright: para mostrar la célula que define el
diagnóstico cuando no hay una foto libre adecuada. Cada patrón ubica las células especiales en posiciones fijas
(fracciones del recuadro, para apuntarlas con flechas) y rellena el resto con glóbulos rojos.

Uso:  python3 frotis29.py <patron> <archivo.jpg> [ancho_px alto_px]"""
import json, math, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, PathPatch
from matplotlib.path import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
FONDO = "#f6eef2"
HEM = "#e39aa5"          # hematíe
HEM_B = "#c9707f"        # borde
PALIDEZ = "#f6dfe4"
NUC = "#4b2a7b"          # núcleo (violeta)
CIT = "#d9c9e6"          # citoplasma de neutrófilo
BASO = "#8fb0dd"         # citoplasma basófilo (linfocito)
R = 4.0                  # radio del hematíe normal (en unidades del dibujo; el campo mide 100 de ancho)


def _hem(ax, x, y, r=R, palidez=.42, color=HEM, borde=HEM_B, z=2):
    ax.add_patch(Circle((x, y), r, fc=color, ec=borde, lw=.7, zorder=z))
    if palidez:
        ax.add_patch(Circle((x, y), r * palidez, fc=PALIDEZ, ec="none", alpha=.9, zorder=z + .1))


def _ovalo(ax, x, y, rx, ry, ang=0, palidez=.35, z=2):
    ax.add_patch(Ellipse((x, y), 2 * rx, 2 * ry, angle=ang, fc=HEM, ec=HEM_B, lw=.7, zorder=z))
    if palidez:
        ax.add_patch(Ellipse((x, y), 2 * rx * palidez, 2 * ry * palidez, angle=ang, fc=PALIDEZ, ec="none", zorder=z + .1))


def _poli(ax, pts, x, y, s=1, ang=0, color=HEM, z=2):
    a = math.radians(ang)
    p = [(x + s * (px * math.cos(a) - py * math.sin(a)), y + s * (px * math.sin(a) + py * math.cos(a))) for px, py in pts]
    ax.add_patch(Polygon(p, closed=True, fc=color, ec=HEM_B, lw=.8, zorder=z, joinstyle="round"))


def _lobulos(ax, x, y, n, r=1.5, radio=3.0, z=5, color=NUC):
    """Núcleo segmentado: n lóbulos en cadena sinuosa unidos por puentes finos (como se ven al microscopio)."""
    if n == 2:
        pts = [(x - radio * .55, y), (x + radio * .55, y)]
    else:
        pts = [(x - radio + 2 * radio * i / (n - 1), y + radio * .45 * math.sin(i * 2.1 + .4)) for i in range(n)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        ax.plot([x1, x2], [y1, y2], color=color, lw=1.4, zorder=z, solid_capstyle="round")
    for i, (px, py) in enumerate(pts):
        ax.add_patch(Ellipse((px, py), 2 * r * .95, 2 * r * 1.3, angle=25 * (-1) ** i, fc=color,
                             ec="#2e1650", lw=.5, zorder=z + .1))


def neutrofilo(ax, x, y, lobulos=3, s=1.0):
    ax.add_patch(Circle((x, y), 6.2 * s, fc=CIT, ec="#b9a3cf", lw=.8, zorder=4))
    rng = np.random.default_rng(int(x * 10 + y))
    for _ in range(60):
        a, rr = rng.uniform(0, 2 * math.pi), rng.uniform(0, 5.6 * s)
        ax.add_patch(Circle((x + rr * math.cos(a), y + rr * math.sin(a)), .14, fc="#b98fc4", ec="none", zorder=4.2))
    _lobulos(ax, x, y, lobulos, r=(1.35 if lobulos < 5 else 1.0) * s, radio=(3.0 if lobulos < 5 else 4.6) * s)


def eosinofilo(ax, x, y):
    ax.add_patch(Circle((x, y), 6.4, fc="#f3c9a8", ec="#d99b74", lw=.8, zorder=4))
    rng = np.random.default_rng(int(x + y))
    for _ in range(110):
        a, rr = rng.uniform(0, 2 * math.pi), rng.uniform(0, 5.8)
        ax.add_patch(Circle((x + rr * math.cos(a), y + rr * math.sin(a)), .38, fc="#e2603c", ec="none", zorder=4.2))
    _lobulos(ax, x, y, 2, r=1.9, radio=2.3)


def linfocito(ax, x, y, s=1.0, atipico=False):
    if atipico:   # linfocito reactivo (mononucleosis): grande, citoplasma que abraza a los hematíes, borde azul intenso
        ax.add_patch(Ellipse((x, y), 18 * s, 14 * s, angle=20, fc="#c7d8ef", ec="#3f6fb5", lw=2.2, zorder=4))
        ax.add_patch(Ellipse((x - 1.5, y + .5), 8.5 * s, 7.5 * s, fc="#5b3a8f", ec="#2e1650", lw=.5, zorder=5))
        return
    ax.add_patch(Circle((x, y), 4.6 * s, fc=BASO, ec="#5d82bd", lw=.7, zorder=4))
    ax.add_patch(Circle((x + .4 * s, y), 3.8 * s, fc=NUC, ec="#2e1650", lw=.5, zorder=5))


def blasto(ax, x, y, auer=True):
    ax.add_patch(Circle((x, y), 7.4, fc="#a9bfe3", ec="#5d82bd", lw=.8, zorder=4))
    ax.add_patch(Ellipse((x - .3, y + .2), 11.4, 10.6, fc="#7a5aa8", ec="#3f2470", lw=.6, zorder=5))
    for dx, dy in ((-1.8, 1.2), (1.6, -1.0)):
        ax.add_patch(Circle((x + dx, y + dy), 1.0, fc="#b9a6d9", ec="#3f2470", lw=.5, zorder=5.2))   # nucléolos
    if auer:
        ax.plot([x + 2.6, x + 6.2], [y - 5.6, y - 2.6], color="#c2185b", lw=2.6, zorder=6, solid_capstyle="round")


def plaqueta(ax, x, y, s=1.0):
    ax.add_patch(Circle((x, y), .8 * s, fc="#8a5fb3", ec="#5a3586", lw=.4, zorder=3))


def plasmocito(ax, x, y):
    ax.add_patch(Ellipse((x, y), 13, 9.5, angle=15, fc="#6f8fcf", ec="#3f5ea5", lw=.8, zorder=4))
    ax.add_patch(Circle((x - 2.8, y), 3.3, fc=NUC, ec="#2e1650", lw=.5, zorder=5))
    ax.add_patch(Circle((x + .4, y + .3), 1.6, fc="#dfe7f6", ec="none", zorder=4.5))       # halo perinuclear


def mancha(ax, x, y):
    """Célula «en mancha» (sombra de Gumprecht) de la LLC."""
    rng = np.random.default_rng(int(x * 7 + y))
    a = np.linspace(0, 2 * np.pi, 22)
    rr = 4.2 + rng.uniform(-1.2, 1.4, len(a))
    ax.add_patch(Polygon(list(zip(x + rr * np.cos(a), y + rr * np.sin(a))), closed=True, fc="#9d83c4", ec="#6c4f99",
                         lw=.6, alpha=.75, zorder=4))


# formas del hematíe
DREPANO = [(-6, 0), (-4.5, 2.6), (-1.5, 3.8), (2, 3.6), (5, 2.2), (6.5, .2), (4, .2), (1, .6), (-2, .2), (-4.6, -.8)]
CASCO = [(-4, -3), (4, -3), (4.2, 0), (2.4, 3.2), (0, 1.2), (-2.4, 3.2), (-4.2, 0)]
FRAG = [(-3, -1.6), (2.6, -2.4), (3.4, 1.2), (-1.8, 2.2)]
LAGRIMA = [(-4, 0), (-3, 2.6), (0, 3.6), (3, 2.4), (6, .6), (9, 0), (6, -.6), (3, -2.4), (0, -3.6), (-3, -2.6)]


def falciforme(ax, x, y, ang=0):
    _poli(ax, DREPANO, x, y, 1.25, ang, color="#d7808f")


def esquistocito(ax, x, y, ang=0, tipo="casco"):
    _poli(ax, CASCO if tipo == "casco" else FRAG, x, y, 1.2, ang)


def dacrocito(ax, x, y, ang=0):
    _poli(ax, LAGRIMA, x, y, .9, ang)


def diana(ax, x, y):
    ax.add_patch(Circle((x, y), R, fc=HEM, ec=HEM_B, lw=.7, zorder=2))
    ax.add_patch(Circle((x, y), R * .68, fc=PALIDEZ, ec="none", zorder=2.1))
    ax.add_patch(Circle((x, y), R * .32, fc="#d98593", ec="none", zorder=2.2))


def esferocito(ax, x, y):
    _hem(ax, x, y, R * .78, palidez=0, color="#c9566a", borde="#a8384d")


def anillo(ax, x, y, n=1):
    """Trofozoíto en anillo (P. falciparum) dentro de un hematíe."""
    _hem(ax, x, y)
    for k in range(n):
        cx, cy = x + (-1.4 + 2.6 * k), y + (.8 - 1.4 * k)
        ax.add_patch(Circle((cx, cy), 1.45, fc="none", ec="#3f5fb5", lw=2.0, zorder=3))
        ax.add_patch(Circle((cx + 1.1, cy + .9), .65, fc="#9c1d4f", ec="none", zorder=3.1))


def gametocito(ax, x, y, ang=20):
    ax.add_patch(Ellipse((x, y), 13, 4.6, angle=ang, fc="#a8a0d6", ec="#6a5fae", lw=.8, zorder=3))
    ax.add_patch(Ellipse((x, y), 4, 2.4, angle=ang, fc="#5b2f86", ec="none", zorder=3.1))


def howell(ax, x, y):
    _hem(ax, x, y)
    ax.add_patch(Circle((x + 1.8, y - 1.4), .7, fc="#3d1d6b", ec="none", zorder=3))


def punteado(ax, x, y):
    _hem(ax, x, y, palidez=.3)
    rng = np.random.default_rng(int(x * 3 + y))
    for _ in range(14):
        a, rr = rng.uniform(0, 2 * math.pi), rng.uniform(.6, 3.3)
        ax.add_patch(Circle((x + rr * math.cos(a), y + rr * math.sin(a)), .28, fc="#3d2a7b", ec="none", zorder=3))


def bartonella(ax, x, y):
    _hem(ax, x, y)
    rng = np.random.default_rng(int(x + y * 3))
    for _ in range(7):
        a, rr = rng.uniform(0, 2 * math.pi), rng.uniform(.5, 3.2)
        cx, cy = x + rr * math.cos(a), y + rr * math.sin(a)
        b = rng.uniform(0, math.pi)
        ax.plot([cx - .55 * math.cos(b), cx + .55 * math.cos(b)], [cy - .55 * math.sin(b), cy + .55 * math.sin(b)],
                color="#4a1f7a", lw=1.6, zorder=3, solid_capstyle="round")


def tripomastigote(ax, x, y):
    t = np.linspace(0, 1, 60)
    xs = x - 8 + 16 * t
    ys = y + 4.5 * np.sin(np.pi * t) * -1 + .8 * np.sin(6 * np.pi * t)
    ax.plot(xs, ys, color="#6a3f9e", lw=6, zorder=4, solid_capstyle="round")
    ax.plot(xs, ys - 1.4 + .5 * np.sin(14 * np.pi * t), color="#8d6cc0", lw=1.2, zorder=4.1)   # membrana ondulante
    ax.plot(xs[-1:] + np.array([0, 4]), ys[-1:] + np.array([0, 1.2]), color="#6a3f9e", lw=1, zorder=4)   # flagelo
    ax.add_patch(Circle((x - 7.2, y - .4), 1.0, fc="#3d1d6b", ec="none", zorder=4.2))                      # cinetoplasto
    ax.add_patch(Ellipse((x, y - 4.2), 2.4, 1.6, fc="#3d1d6b", ec="none", zorder=4.2))


CELULAS = dict(neutrofilo=neutrofilo, eosinofilo=eosinofilo, linfocito=linfocito, blasto=blasto, plasmocito=plasmocito,
               mancha=mancha, falciforme=falciforme, esquistocito=esquistocito, dacrocito=dacrocito, diana=diana,
               esferocito=esferocito, anillo=anillo, gametocito=gametocito, howell=howell, punteado=punteado,
               bartonella=bartonella, tripomastigote=tripomastigote,
               macro=lambda ax, x, y, ang=0: _ovalo(ax, x, y, R * 1.45, R * 1.15, ang),
               micro=lambda ax, x, y: _hem(ax, x, y, R * .72, palidez=.62),
               lapiz=lambda ax, x, y, ang=0: _ovalo(ax, x, y, R * 1.3, R * .5, ang, palidez=.5))
RADIO = dict(neutrofilo=6.6, eosinofilo=6.8, linfocito=5, blasto=8, plasmocito=7, mancha=5.4, falciforme=8,
             esquistocito=5.4, dacrocito=6, diana=R, esferocito=R * .8, anillo=R, gametocito=6.6, howell=R, punteado=R,
             bartonella=R, tripomastigote=9, macro=R * 1.45, micro=R * .72, lapiz=R * 1.3)

# Patrones: células especiales [(tipo, fx, fy, {args})] + cómo son los hematíes de relleno
PATRONES = {
    "normal": dict(esp=[("neutrofilo", .5, .5, {})], hem="normal"),
    "megaloblastica": dict(esp=[("neutrofilo", .42, .48, dict(lobulos=6, s=1.15)), ("macro", .78, .25, dict(ang=20)),
                                ("macro", .18, .78, dict(ang=-15))], hem="macro",
                           nombre="Anemia megaloblástica: neutrófilo hipersegmentado y macroovalocitos"),
    "ferropenica": dict(esp=[("lapiz", .7, .3, dict(ang=25)), ("micro", .3, .65, {})], hem="micro",
                        nombre="Anemia ferropénica: hematíes pequeños y pálidos (microcíticos hipocrómicos)"),
    "falciforme": dict(esp=[("falciforme", .35, .4, dict(ang=10)), ("falciforme", .7, .65, dict(ang=-30)),
                            ("howell", .72, .25, {}), ("diana", .25, .75, {})], hem="normal",
                       nombre="Drepanocitosis: hematíes en hoz"),
    "esquistocitos": dict(esp=[("esquistocito", .3, .35, {}), ("esquistocito", .68, .6, dict(ang=40, tipo="frag")),
                               ("esquistocito", .55, .25, dict(ang=-60)), ("esquistocito", .22, .72, dict(ang=120, tipo="frag"))],
                          hem="normal", plaquetas=1, nombre="Microangiopatía: esquistocitos y pocas plaquetas"),
    "esferocitos": dict(esp=[("esferocito", .35, .4, {}), ("esferocito", .62, .58, {}), ("esferocito", .75, .3, {}),
                             ("esferocito", .25, .7, {})], hem="normal", nombre="Esferocitos: pequeños, densos, sin palidez central"),
    "lma": dict(esp=[("blasto", .38, .45, {}), ("blasto", .72, .62, dict(auer=False))], hem="normal", plaquetas=2,
                nombre="Leucemia mieloide aguda: blastos con bastón de Auer"),
    "lla": dict(esp=[("blasto", .35, .45, dict(auer=False)), ("blasto", .68, .6, dict(auer=False))], hem="normal", plaquetas=2,
                nombre="Leucemia linfoblástica aguda: blastos sin Auer"),
    "llc": dict(esp=[("linfocito", .3, .35, dict(s=.95)), ("linfocito", .55, .55, dict(s=.95)), ("linfocito", .78, .3, dict(s=.95)),
                     ("mancha", .25, .72, {}), ("linfocito", .75, .78, dict(s=.95))], hem="normal",
                nombre="Leucemia linfocítica crónica: linfocitos pequeños y células en mancha"),
    "mononucleosis": dict(esp=[("linfocito", .4, .45, dict(atipico=True)), ("linfocito", .78, .72, {})], hem="normal",
                          nombre="Mononucleosis: linfocito reactivo (atípico)"),
    "malaria_f": dict(esp=[("anillo", .3, .35, dict(n=2)), ("anillo", .62, .5, {}), ("gametocito", .4, .75, {}),
                           ("anillo", .78, .22, {})], hem="normal", nombre="Malaria por P. falciparum: anillos y gametocito en banana"),
    "malaria_v": dict(esp=[("anillo", .35, .4, {}), ("anillo", .68, .62, {})], hem="normal", nombre="Malaria: trofozoítos en anillo"),
    "bartonella": dict(esp=[("bartonella", .32, .38, {}), ("bartonella", .6, .55, {}), ("bartonella", .75, .28, {}),
                            ("bartonella", .3, .74, {})], hem="normal", nombre="Bartonelosis: bacilos dentro de los hematíes"),
    "chagas": dict(esp=[("tripomastigote", .5, .5, {})], hem="normal", nombre="Chagas agudo: tripomastigote"),
    "eosinofilia": dict(esp=[("eosinofilo", .38, .45, {}), ("eosinofilo", .72, .7, {})], hem="normal", nombre="Eosinofilia"),
    "mieloma": dict(esp=[("plasmocito", .7, .7, {})], hem="rouleaux", nombre="Mieloma: hematíes en pila de monedas (rouleaux)"),
    "talasemia": dict(esp=[("diana", .3, .35, {}), ("diana", .62, .58, {}), ("punteado", .75, .25, {}), ("diana", .25, .72, {})],
                      hem="micro", nombre="Talasemia: microcitos, dianocitos y punteado basófilo"),
    "plomo": dict(esp=[("punteado", .35, .4, {}), ("punteado", .65, .6, {})], hem="micro", nombre="Saturnismo: punteado basófilo"),
    "mielofibrosis": dict(esp=[("dacrocito", .35, .4, dict(ang=20)), ("dacrocito", .66, .62, dict(ang=-140)),
                               ("dacrocito", .72, .25, dict(ang=200))], hem="normal", nombre="Mielofibrosis: dacrocitos (en lágrima)"),
    "esplenectomia": dict(esp=[("howell", .35, .4, {}), ("howell", .68, .6, {}), ("diana", .72, .28, {})], hem="normal",
                          nombre="Asplenia: cuerpos de Howell-Jolly"),
}


def render(patron, archivo, W=860, H=600, semilla=7):
    pat = PATRONES[patron]
    fw, fh = 100, 100 * H / W
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, fw)
    ax.set_ylim(fh, 0)
    ax.axis("off")
    ax.add_patch(plt.Rectangle((0, 0), fw, fh, color=FONDO, zorder=0))
    ocup = []
    for tipo, fx, fy, k in pat["esp"]:
        x, y = fx * fw, fy * fh
        CELULAS[tipo](ax, x, y, **k)
        ocup.append((x, y, RADIO[tipo] * (1.25 if k.get("s", 1) > 1 or k.get("atipico") or k.get("lobulos", 0) > 4 else 1)))
    rng = np.random.default_rng(semilla)
    if pat["hem"] == "rouleaux":       # pilas de monedas: filas de hematíes superpuestos
        for fila in range(7):
            y0 = 6 + fila * fh / 6.6
            x = rng.uniform(-2, 6)
            ang = rng.uniform(-12, 12)
            while x < fw + 4:
                xx, yy = x, y0 + (x - 50) * math.tan(math.radians(ang))
                if all(math.hypot(xx - ox, yy - oy) > orr + R for ox, oy, orr in ocup):
                    _hem(ax, xx, yy, palidez=.3)
                x += R * 1.15 if rng.uniform() < .85 else R * 3.5
    else:
        rr = {"normal": R, "macro": R * 1.25, "micro": R * .74}[pat["hem"]]
        pal = {"normal": .42, "macro": .3, "micro": .62}[pat["hem"]]
        pts = []
        for _ in range(9000):
            x, y = rng.uniform(-2, fw + 2), rng.uniform(-2, fh + 2)
            r = rr * rng.uniform(.92, 1.08)
            if all(math.hypot(x - ox, y - oy) > orr + r + .4 for ox, oy, orr in ocup) and \
               all(math.hypot(x - px, y - py) > pr_ + r + .5 for px, py, pr_ in pts):
                pts.append((x, y, r))
        for x, y, r in pts:
            if pat["hem"] == "macro" and rng.uniform() < .5:
                _ovalo(ax, x, y, r * 1.12, r * .9, rng.uniform(0, 180), palidez=.28)
            else:
                _hem(ax, x, y, r, palidez=pal)
    for _ in range(pat.get("plaquetas", 9)):
        x, y = rng.uniform(2, fw - 2), rng.uniform(2, fh - 2)
        plaqueta(ax, x, y)
    # viñeta suave del campo del microscopio
    g = np.linspace(-1, 1, 200)
    X, Y = np.meshgrid(g, g)
    v = np.clip((np.sqrt(X ** 2 + Y ** 2) - .95) * 1.2, 0, .22)
    ax.imshow(np.dstack([np.zeros_like(v)] * 3 + [v]), extent=(0, fw, fh, 0), zorder=20)
    fig.savefig(os.path.join(AQUI, archivo), dpi=100, pil_kwargs=dict(quality=92))
    plt.close(fig)
    return [(t, fx, fy) for t, fx, fy, _ in pat["esp"]]


if __name__ == "__main__":
    a = sys.argv
    print(render(a[1], a[2], *(int(x) for x in a[3:5])) if len(a) > 3 else render(a[1], a[2]))
