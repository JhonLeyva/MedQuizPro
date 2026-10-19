"""Diseños 13, 14, 19 y 20 (bloque ENAM 2026): imágenes reales con marcas encima o dibujos propios.
13 comparador de imágenes · 14 escalera terapéutica · 19 mapa corporal de signos · 20 árbol con imagen.
Las fotos (licencia libre) se incrustan en base64 desde flujo/img/ y las marcas se dan en fracciones
del recuadro de la imagen (0-1), así no dependen del tamaño final."""
import base64
import math
import os
import random
from engine import SVG, wrap, tw, header, perlas, escape, hexagon, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE
from engine2 import top_row, table, X0, X1
from engine3 import section, case_chip, AMBER, AMBER_L
from engine5 import panel, ORANGE, SKIN, SKIN_D, GREEN, RED, RED_L

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
YEL, DARK = "#facc15", "#0f172a"
_n = [0]


# ════════════════════════════════════════════════════════════ FOTO + MARCAS
def foto(s, x, y, w, h, archivo, marcas=(), fondo="#000000"):
    """Imagen real incrustada (recortada a w×h con esquinas redondeadas) y marcas encima."""
    _n[0] += 1
    cid = f"fc{_n[0]}"
    data = base64.b64encode(open(os.path.join(IMG_DIR, archivo), "rb").read()).decode()
    s.add(f'<defs><clipPath id="{cid}"><rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="8"/></clipPath></defs>'
          f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="8" fill="{fondo}"/>'
          f'<image x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" preserveAspectRatio="xMidYMid slice" '
          f'clip-path="url(#{cid})" href="data:image/jpeg;base64,{data}"/>')
    for m in marcas:
        MARCAS[m[0]](s, x, y, w, h, *m[1:])


def _img(s, x, y, w, h, im, fondo="#000000"):
    """Foto (im["archivo"]) o dibujo (im["ilu"](s, x, y)) en un recuadro w×h."""
    if im.get("ilu"):
        im["ilu"](s, x, y)
    else:
        foto(s, x, y, w, h, im["archivo"], im.get("marcas", ()), fondo)


def _etq(s, x, y, w, h, cx, cy, texto, color=YEL):
    """Rótulo con fondo oscuro centrado en (cx, cy), sin salirse del recuadro. Devuelve su caja."""
    ls = texto.split("\n")
    tw_ = max(tw(l, 11.5, True) for l in ls) + 14
    th = len(ls) * 15 + 8
    bx = min(max(cx - tw_ / 2, x + 4), x + w - tw_ - 4)
    by = min(max(cy - th / 2, y + 4), y + h - th - 4)
    s.rect(bx, by, tw_, th, DARK, color, 1.2, rx=6)
    s.add(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{tw_:.1f}" height="{th:.1f}" rx="6" fill="{DARK}" opacity="0.35"/>')
    s.text(bx + tw_ / 2, by + 16, ls, 11.5, 800, color, maxw=tw_ - 10, lh=15)
    return bx, by, tw_, th


def _punta(s, x1, y1, x2, y2, color, sw=2.5):
    """Línea de (x1,y1) a (x2,y2) con punta de flecha en (x2,y2)."""
    a = math.atan2(y2 - y1, x2 - x1)
    xe, ye = x2 - 9 * math.cos(a), y2 - 9 * math.sin(a)
    s.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{xe:.1f}" y2="{ye:.1f}" stroke="{DARK}" stroke-width="{sw+2.5}" stroke-linecap="round" opacity="0.55"/>'
          f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{xe:.1f}" y2="{ye:.1f}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')
    p = [(x2, y2), (x2 - 12 * math.cos(a - 0.45), y2 - 12 * math.sin(a - 0.45)),
         (x2 - 12 * math.cos(a + 0.45), y2 - 12 * math.sin(a + 0.45))]
    s.add(f'<polygon points="{" ".join(f"{u:.1f},{v:.1f}" for u, v in p)}" fill="{color}" stroke="{DARK}" stroke-width="1"/>')


def m_flecha(s, x, y, w, h, fx, fy, lx, ly, texto, color=YEL):
    """Flecha desde el rótulo (lx, ly) hasta el punto (fx, fy)."""
    tx, ty = x + fx * w, y + fy * h
    bx, by, bw, bh = _etq(s, x, y, w, h, x + lx * w, y + ly * h, texto, color)
    # sale del borde del rótulo más cercano al punto
    sx = min(max(tx, bx), bx + bw)
    sy = by + bh if ty > by + bh else (by if ty < by else by + bh / 2)
    if by <= ty <= by + bh:
        sx = bx if tx < bx else bx + bw
    _punta(s, sx, sy, tx, ty, color)


def m_flechas(s, x, y, w, h, puntos, lx, ly, texto, color=YEL):
    """Un rótulo con varias flechas (p. ej. el mismo hallazgo en ambos pulmones)."""
    bx, by, bw, bh = _etq(s, x, y, w, h, x + lx * w, y + ly * h, texto, color)
    for fx, fy in puntos:
        tx, ty = x + fx * w, y + fy * h
        sx = min(max(tx, bx), bx + bw)
        sy = by + bh if ty > by + bh else (by if ty < by else by + bh / 2)
        if by <= ty <= by + bh:
            sx = bx if tx < bx else bx + bw
        _punta(s, sx, sy, tx, ty, color)


def m_circulo(s, x, y, w, h, fx, fy, fr, texto=None, lx=None, ly=None, color=YEL):
    """Círculo discontinuo sobre la zona; rótulo opcional unido al borde."""
    cx, cy, r = x + fx * w, y + fy * h, fr * w
    s.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{DARK}" stroke-width="5" opacity="0.5"/>'
          f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{color}" stroke-width="2.5" stroke-dasharray="7 4"/>')
    if texto:
        bx, by, bw, bh = _etq(s, x, y, w, h, x + lx * w, y + ly * h, texto, color)
        mx, my = bx + bw / 2, by + bh / 2
        a = math.atan2(my - cy, mx - cx)
        ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
        sy = by + bh if my < cy else by
        s.line(mx, sy, ex, ey, color, 2)


def m_corchete(s, x, y, w, h, fx0, fx1, fy, texto, abajo=False, hasta=None, color=YEL):
    """Corchete horizontal entre fx0 y fx1 a la altura fy; rótulo encima (o debajo si abajo=True).
    hasta: altura (fracción) a la que suben las guías punteadas de cada extremo."""
    x0, x1, yy = x + fx0 * w, x + fx1 * w, y + fy * h
    k = -7 if abajo else 7
    if hasta is not None:
        yh = y + hasta * h
        for xx in (x0, x1):
            s.add(f'<line x1="{xx:.1f}" y1="{yy:.1f}" x2="{xx:.1f}" y2="{yh:.1f}" stroke="{color}" stroke-width="2" stroke-dasharray="3 3"/>')
    d = f"M{x0:.1f} {yy+k:.1f} V{yy:.1f} H{x1:.1f} V{yy+k:.1f}"
    s.add(f'<path d="{d}" fill="none" stroke="{DARK}" stroke-width="5" opacity="0.5"/>'
          f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5"/>')
    _etq(s, x, y, w, h, (x0 + x1) / 2, yy + (18 if abajo else -16), texto, color)


def m_caja(s, x, y, w, h, fx0, fy0, fx1, fy1, texto, lx, ly, color=YEL):
    """Recuadro sobre una zona con rótulo unido por una línea."""
    x0, y0, x1, y1 = x + fx0 * w, y + fy0 * h, x + fx1 * w, y + fy1 * h
    s.add(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1-x0:.1f}" height="{y1-y0:.1f}" rx="4" fill="none" stroke="{color}" stroke-width="2.5"/>')
    bx, by, bw, bh = _etq(s, x, y, w, h, x + lx * w, y + ly * h, texto, color)
    sx = bx if bx > x1 else bx + bw
    s.line(x1 if bx > x1 else x0, (y0 + y1) / 2, sx, by + bh / 2, color, 2)


def m_texto(s, x, y, w, h, fx, fy, texto, color=YEL):
    _etq(s, x, y, w, h, x + fx * w, y + fy * h, texto, color)


MARCAS = {"flecha": m_flecha, "flechas": m_flechas, "circulo": m_circulo, "corchete": m_corchete, "caja": m_caja, "texto": m_texto}


def card6(s, x, y, w, titulo, lines, on=False, color=TEAL, tag=None, fs=11.5, hmin=0, dry=False):
    """Tarjeta con título y alto mínimo (para igualar filas). dry=True solo mide."""
    tl = wrap(titulo, w - 30, 12.5, True)
    bl = []
    for l in lines:
        bl += wrap(l, w - 30, fs)
    h = max(hmin, 16 + len(tl) * 17 + (6 if bl else 0) + len(bl) * 16 + 14)
    if dry:
        return h
    s.rect(x, y, w, h, TEAL_L if on else "#ffffff", TEAL if on else LINE, 2.2 if on else 1.5)
    s.rect(x + 1, y + 1, 6, h - 2, color, rx=3)
    s.text(x + 18, y + 24, tl, 12.5, 800, TEAL_D if on else INK, "start", w - 30, lh=17)
    s.text(x + 18, y + 24 + len(tl) * 17 + 4, bl, fs, 400, SLATE, "start", w - 30, lh=16)
    if tag:
        case_chip(s, x + w - tw("◆ " + tag, 10, True) / 2 - 18, y, tag)
    return h


def fila_cards(s, y, cards, tag, titulo=None):
    """Fila de tarjetas del mismo alto a todo el ancho."""
    if titulo:
        s.text(X0, y + 12, titulo.upper(), 11, 800, MUTED, "start", 900)
        y += 22
    n, gap = len(cards), 14
    w = (X1 - X0 - gap * (n - 1)) / n
    hm = max(card6(s, 0, 0, w, t, l, fs=11, dry=True) for t, l, _ in cards)
    for i, (t, l, on) in enumerate(cards):
        card6(s, X0 + i * (w + gap), y, w, t, l, on=on, color=AMBER if on else TEAL, tag=tag if on else None, fs=11, hmin=hm)
    return y + hm


def _pie_h(texto, w):
    return len(wrap(texto, w, 11.5)) * 16 if texto else 0


def _pie(s, x, y, w, texto):
    if texto:
        pl = wrap(texto, w, 11.5)
        s.text(x, y + 12, pl, 11.5, 500, SLATE, "start", w, lh=16)


def credito(s, x, y, w, texto):
    s.text(x, y, texto, 9.5, 500, MUTED, "start", w, italic=True)


# ════════════════════════════════════════════════════════════ DIBUJOS PROPIOS
def _g(s, x, y, sc, inner):
    s.add(f'<g transform="translate({x:.1f},{y:.1f}) scale({sc})">{inner}</g>')


def _t(x, y, t, col, fs=11, anchor="middle", fw=800):
    return (f'<text x="{x}" y="{y}" font-size="{fs}" font-weight="{fw}" fill="{col}" '
            f'text-anchor="{anchor}" data-max="0">{escape(t)}</text>')


def ilu_nino_sarampion(s, x, y):
    """Niño de frente con el exantema del sarampión: más denso en cara y tronco (días 1-2),
    empezando en piernas (día 3). Números 1-4 = signos de las tarjetas."""
    st = f'stroke="{SKIN_D}" stroke-width="2"'
    p = (f'<ellipse cx="98" cy="76" rx="9" ry="14" fill="{SKIN}" {st}/><ellipse cx="202" cy="76" rx="9" ry="14" fill="{SKIN}" {st}/>'
         f'<circle cx="150" cy="72" r="52" fill="{SKIN}" {st}/>'
         f'<path d="M104 52 C112 20 188 20 196 52 C180 36 120 36 104 52 Z" fill="#7c4a2d"/>'
         f'<rect x="140" y="122" width="20" height="12" fill="{SKIN}" {st}/>'
         f'<path d="M100 132 H200 L206 250 H94 Z" fill="{SKIN}" {st}/>'
         f'<path d="M100 138 L76 146 L58 252 L76 256 L94 172 Z" fill="{SKIN}" {st}/>'
         f'<path d="M200 138 L224 146 L242 252 L224 256 L206 172 Z" fill="{SKIN}" {st}/>'
         f'<circle cx="66" cy="264" r="11" fill="{SKIN}" {st}/><circle cx="234" cy="264" r="11" fill="{SKIN}" {st}/>'
         f'<path d="M94 250 H206 L202 288 H98 Z" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="2"/>'
         f'<path d="M102 288 H146 L142 400 H110 Z" fill="{SKIN}" {st}/><path d="M154 288 H198 L190 400 H158 Z" fill="{SKIN}" {st}/>'
         f'<ellipse cx="126" cy="408" rx="20" ry="9" fill="{SKIN}" {st}/><ellipse cx="174" cy="408" rx="20" ry="9" fill="{SKIN}" {st}/>')
    # exantema: puntos deterministas, densidad cefalocaudal
    rnd = random.Random(7)

    def zona(n, fx, col, op, rr=(2.2, 3.6)):
        out = ""
        k = 0
        while k < n:
            px, py = rnd.uniform(40, 260), rnd.uniform(20, 405)
            if fx(px, py):
                out += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{rnd.uniform(*rr):.1f}" fill="{col}" opacity="{op}"/>'
                k += 1
        return out
    cara = lambda px, py: (px - 150) ** 2 + (py - 76) ** 2 < 46 ** 2 and not (118 < px < 182 and 58 < py < 104) or \
        ((px - 98) ** 2 / 81 + (py - 76) ** 2 / 196 < 1) or ((px - 202) ** 2 / 81 + (py - 76) ** 2 / 196 < 1)
    tronco = lambda px, py: 104 < px < 196 and 138 < py < 246
    brazos = lambda px, py: (64 < px < 96 and 150 < py < 250 and px > 96 - (py - 140) * 0.3) or \
        (204 < px < 236 and 150 < py < 250 and px < 204 + (py - 140) * 0.3)
    piernas = lambda px, py: (108 < px < 142 and 292 < py < 395) or (160 < px < 192 and 292 < py < 395)
    p += zona(60, cara, "#b91c1c", 0.8) + zona(80, tronco, "#dc2626", 0.65) + zona(26, brazos, "#ef4444", 0.55) \
        + zona(14, piernas, "#f87171", 0.5, (1.8, 2.8))
    # ojos rojos (conjuntivitis), nariz con secreción, boca
    p += ('<ellipse cx="132" cy="68" rx="9" ry="6" fill="#fecaca" stroke="#b91c1c" stroke-width="1.5"/>'
          '<ellipse cx="168" cy="68" rx="9" ry="6" fill="#fecaca" stroke="#b91c1c" stroke-width="1.5"/>'
          '<circle cx="132" cy="68" r="3" fill="#1e293b"/><circle cx="168" cy="68" r="3" fill="#1e293b"/>'
          f'<path d="M150 76 L146 88 H154 Z" fill="{SKIN_D}"/>'
          '<path d="M146 90 C145 96 147 100 148 102" stroke="#93c5fd" stroke-width="2.5" fill="none"/>'
          '<ellipse cx="150" cy="104" rx="10" ry="5" fill="#9f1239"/>')
    # escala de días (izquierda)
    p += ('<line x1="30" y1="46" x2="30" y2="392" stroke="#94a3b8" stroke-width="2"/>'
          '<polygon points="24,386 36,386 30,398" fill="#94a3b8"/>'
          + _t(28, 36, "Día 1", "#b91c1c", 11) + _t(30, 200, "Día 2", "#dc2626", 11)
          + _t(30, 350, "Día 3", "#ef4444", 11))
    # marcadores numerados con guía corta hasta el signo
    mk = [(1, 262, 112, 156, 92), (2, 262, 60, 176, 67), (3, 262, 148, 160, 106), (4, 262, 196, 196, 196)]
    for n, cx, cy, tx, ty in mk:
        p += (f'<line x1="{cx-12}" y1="{cy}" x2="{tx}" y2="{ty}" stroke="#334155" stroke-width="1.6"/>'
              f'<circle cx="{tx}" cy="{ty}" r="3" fill="#334155"/>'
              f'<circle cx="{cx}" cy="{cy}" r="12" fill="{ORANGE}" stroke="#ffffff" stroke-width="2"/>'
              + _t(cx, cy + 4.5, str(n), "#ffffff", 13))
    _g(s, x, y, 1.0, p)


def ilu_rx_ddc(s, x, y):
    """Esquema de Rx AP de pelvis de un lactante con displasia de la cadera IZQUIERDA
    (a la derecha de la imagen). Líneas de Hilgenreiner, Perkins y Shenton."""
    bone, bone2, bg = "#cbd5e1", "#94a3b8", "#0b1220"
    W = 560

    def ala(lado):
        # ala ilíaca + techo acetabular. lado D: normal; lado I: techo empinado
        if lado == "D":
            return (f'<path d="M255 40 C205 12 120 16 92 56 C76 86 88 118 116 130 L132 131 L204 151 L244 116 Z" '
                    f'fill="{bone}" stroke="{bone2}" stroke-width="2"/>')
        return (f'<path d="M305 40 C355 12 440 16 468 56 C486 80 478 98 452 100 L430 98 L356 151 L316 116 Z" '
                f'fill="{bone}" stroke="{bone2}" stroke-width="2"/>')

    def pubis(mx):
        # anillo isquiopubiano, medial al cartílago trirradiado, con su agujero obturador
        f = (lambda a: a) if not mx else (lambda a: W - a)
        return (f'<path d="M{f(206)} 160 C{f(234)} 160 {f(262)} 170 {f(272)} 186 L{f(272)} 214 C{f(254)} 222 {f(234)} 222 {f(222)} 214 '
                f'C{f(214)} 232 {f(204)} 244 {f(196)} 238 C{f(190)} 218 {f(192)} 186 {f(206)} 160 Z" fill="{bone}" stroke="{bone2}" stroke-width="2"/>'
                f'<ellipse cx="{f(238)}" cy="197" rx="17" ry="12" fill="{bg}"/>')
    p = (f'<rect x="0" y="0" width="{W}" height="300" rx="10" fill="{bg}"/>'
         f'<rect x="262" y="0" width="36" height="16" rx="3" fill="{bone2}"/><rect x="262" y="20" width="36" height="18" rx="3" fill="{bone2}"/>'
         f'<path d="M250 40 H310 L300 146 C294 172 266 172 260 146 Z" fill="#64748b"/>'
         + ala("D") + ala("I") + pubis(False) + pubis(True)
         # fémur derecho (normal): metáfisis bajo Hilgenreiner, núcleo medial a Perkins, dentro del acetábulo
         + f'<path d="M140 190 L186 197 L178 300 L142 300 Z" fill="{bone}" stroke="{bone2}" stroke-width="2"/>'
         + f'<circle cx="162" cy="174" r="11" fill="{bone}" stroke="{bone2}" stroke-width="2"/>'
         # fémur izquierdo: ascendido y lateralizado, núcleo pequeño arriba y afuera
         + f'<path d="M436 146 L484 154 L474 300 L440 300 Z" fill="{bone}" stroke="{bone2}" stroke-width="2"/>'
         + f'<circle cx="462" cy="128" r="7" fill="{bone}" stroke="{bone2}" stroke-width="2"/>')
    cy_, yl = "#22d3ee", "#facc15"
    # Hilgenreiner (horizontal por los cartílagos trirradiados)
    p += f'<line x1="60" y1="155" x2="500" y2="155" stroke="{cy_}" stroke-width="2.2"/>'
    # Perkins (vertical desde el borde lateral del techo)
    p += (f'<line x1="132" y1="70" x2="132" y2="262" stroke="{cy_}" stroke-width="2.2" stroke-dasharray="6 4"/>'
          f'<line x1="430" y1="70" x2="430" y2="262" stroke="{cy_}" stroke-width="2.2" stroke-dasharray="6 4"/>')
    # índice acetabular: techo prolongado
    p += (f'<line x1="204" y1="151" x2="118" y2="128" stroke="{ORANGE}" stroke-width="2.5"/>'
          f'<line x1="356" y1="151" x2="440" y2="92" stroke="{ORANGE}" stroke-width="2.5"/>')
    # Shenton: borde inferior de la rama púbica → borde medial del cuello femoral
    p += (f'<path d="M254 184 C232 180 206 186 188 198 L181 262" fill="none" stroke="{yl}" stroke-width="2.5" stroke-dasharray="5 4"/>'
          f'<path d="M306 184 C328 180 348 182 362 190" fill="none" stroke="{yl}" stroke-width="2.5" stroke-dasharray="5 4"/>'
          f'<path d="M437 150 L441 262" fill="none" stroke="{yl}" stroke-width="2.5" stroke-dasharray="5 4"/>'
          f'<circle cx="462" cy="128" r="15" fill="none" stroke="{ORANGE}" stroke-width="2.5"/>')
    # rótulos
    p += (_t(16, 22, "D", "#94a3b8", 13, "start") + _t(544, 22, "I", "#94a3b8", 13, "end")
          + _t(64, 172, "Hilgenreiner", cy_, 11, "start")
          + _t(132, 62, "Perkins", cy_, 11) + _t(430, 62, "Perkins", cy_, 11)
          + _t(92, 147, "IA ~15°", ORANGE, 11) + _t(506, 48, "IA ~35°", ORANGE, 11)
          + _t(240, 272, "Shenton", yl, 11) + _t(240, 285, "continuo", yl, 11)
          + _t(400, 232, "Shenton", yl, 11) + _t(400, 245, "roto", yl, 11)
          + _t(518, 112, "núcleo arriba", ORANGE, 10.5) + _t(518, 125, "y afuera", ORANGE, 10.5))
    _g(s, x, y, 1.0, p)


# ════════════════════════════════════════════════════════════ DISEÑO 13: COMPARADOR
def comparador(s, y, d):
    """Dos imágenes reales lado a lado (antes/después o normal/patológico) con marcas y lectura."""
    y = section(s, y + 10, d["rotulo"]) + 10
    gap = 44
    PW = (X1 - X0 - gap) / 2
    IH = d["IH"]
    ph = max(_pie_h(im["pie"], PW - 28) for im in d["imgs"])
    H = 40 + IH + 10 + ph + 26
    for i, im in enumerate(d["imgs"]):
        x = X0 + i * (PW + gap)
        s.rect(x, y, PW, H, TEAL_L if im.get("on") else "#ffffff", TEAL if im.get("on") else LINE, 2.2 if im.get("on") else 1.5, rx=12)
        s.rect(x + 12, y + 10, tw(im["titulo"].upper(), 10, True) + 18, 20, "#ffffff", TEAL_B, 1, rx=10)
        s.text(x + 21, y + 24, im["titulo"].upper(), 10, 800, TEAL, "start", 0)
        if im.get("on"):
            case_chip(s, x + PW - 70, y, d.get("tag", "ESTE CASO"))
        _img(s, x + 12, y + 38, PW - 24, IH, im)
        _pie(s, x + 14, y + 38 + IH + 6, PW - 28, im["pie"])
        if im.get("credito"):
            credito(s, x + 14, y + H - 10, PW - 28, im["credito"])
    # flecha entre las dos imágenes
    my = y + 38 + IH / 2
    s.circle(X0 + PW + gap / 2, my, 17, ORANGE)
    s.add(f'<polygon points="{X0+PW+gap/2-6:.1f},{my-8:.1f} {X0+PW+gap/2-6:.1f},{my+8:.1f} {X0+PW+gap/2+8:.1f},{my:.1f}" fill="#ffffff"/>')
    y += H + 18
    return fila_cards(s, y, d["lectura"], d.get("tag"), d.get("lectura_titulo"))


# ════════════════════════════════════════════════════════════ DISEÑO 14: ESCALERA
def escalera(s, y, d):
    """Trazo real del caso arriba; abajo, chequeo de estabilidad y escalera de tratamiento.
    Estable: se sube peldaño a peldaño. Inestable: salto directo al último."""
    y = section(s, y + 10, d["rotulo"])
    e = d["img"]
    ph = _pie_h(e["pie"], X1 - X0 - 28)
    H = 40 + e["IH"] + 8 + ph + 24
    panel(s, X0, y, X1 - X0, H, e["titulo"])
    _img(s, X0 + 12, y + 38, X1 - X0 - 24, e["IH"], e, "#f8fafc")
    _pie(s, X0 + 14, y + 38 + e["IH"] + 4, X1 - X0 - 28, e["pie"])
    if e.get("credito"):
        credito(s, X0 + 14, y + H - 10, X1 - X0 - 28, e["credito"])
    y += H + 22
    # izquierda: chequeo de inestabilidad
    LW = 290
    s.text(X0, y + 12, d["check_titulo"].upper(), 11, 800, MUTED, "start", LW)
    cy = y + 24
    for txt, alerta in d["check"]:
        ls = wrap(txt, LW - 44, 11.5)
        hh = 14 + len(ls) * 16
        s.rect(X0, cy, LW, hh, "#fff1f2" if alerta else "#ffffff", "#fda4af" if alerta else LINE, 1.2, rx=8)
        s.circle(X0 + 16, cy + hh / 2, 9, RED if alerta else "#94a3b8")
        s.text(X0 + 16, cy + hh / 2 + 4.5, "!" if alerta else "?", 11, 800, "#ffffff", maxw=0)
        s.text(X0 + 34, cy + 19, ls, 11.5, 600 if alerta else 400, "#9f1239" if alerta else "#334155", "start", LW - 44, lh=16)
        cy += hh + 6
    vl = wrap(d["veredicto"], LW - 24, 12.5, True)
    vh = 18 + len(vl) * 17
    s.rect(X0, cy + 4, LW, vh, ORANGE, "none", 0, rx=10)
    s.text(X0 + LW / 2, cy + 22, vl, 12.5, 800, "#ffffff", maxw=LW - 24, lh=17)
    ver_y = cy + 4 + vh / 2
    left_bottom = cy + 4 + vh
    # derecha: escalera
    sx0 = X0 + LW + 60
    n = len(d["peldanos"])
    g = 24
    sw = (X1 - sx0 - g * (n - 1)) / n
    need = []
    for tit, lines in d["peldanos"]:
        tl = wrap(tit, sw - 20, 12, True)
        bl = []
        for l in lines:
            bl += wrap(l, sw - 20, 11)
        need.append((tl, bl, 46 + len(tl) * 16 + 4 + len(bl) * 15 + 12))
    hs = []
    for i, (_, _, nh) in enumerate(need):
        hs.append(max(nh, (hs[-1] + 34) if hs else nh))
    top_space = 60
    base = y + top_space + hs[-1]
    for i, (tl, bl, _) in enumerate(need):
        on = i == d["ans"]
        x = sx0 + i * (sw + g)
        ty = base - hs[i]
        s.rect(x, ty, sw, hs[i], TEAL if on else TEAL_L, TEAL if on else TEAL_B, 1.8, rx=8)
        s.circle(x + 20, ty + 20, 12, "#ffffff" if on else TEAL)
        s.text(x + 20, ty + 25, str(i + 1), 12, 800, TEAL if on else "#ffffff", maxw=0)
        s.text(x + 10, ty + 52, tl, 12, 800, "#ffffff" if on else INK, "start", sw - 20, lh=16)
        s.text(x + 10, ty + 52 + len(tl) * 16 + 4, bl, 11, 400, "#ecfeff" if on else SLATE, "start", sw - 20, lh=15)
        if i < n - 1:
            # camino del paciente estable: de un peldaño al siguiente, por abajo
            s.arrow_right(x + sw + 3, x + sw + g - 3, base - 18, "#94a3b8")
        if on:
            case_chip(s, x + sw / 2, base, d.get("tag", "ESTE CASO"))
    # salto del inestable: del veredicto sube por encima de la escalera y cae en el peldaño del caso
    tx = sx0 + d["ans"] * (sw + g) + 34
    yj = base - hs[-1] - 30
    s.add(f'<path d="M{X0+LW:.1f} {ver_y:.1f} H{sx0-22:.1f} V{yj:.1f} H{tx:.1f} V{base-hs[d["ans"]]-10:.1f}" '
          f'fill="none" stroke="{ORANGE}" stroke-width="3" stroke-linejoin="round"/>')
    s.add(f'<polygon points="{tx-7:.1f},{base-hs[d["ans"]]-12:.1f} {tx+7:.1f},{base-hs[d["ans"]]-12:.1f} '
          f'{tx:.1f},{base-hs[d["ans"]]-1:.1f}" fill="{ORANGE}"/>')
    s.text((sx0 + tx) / 2, yj - 8, d.get("salto", "Inestable: salto directo"), 11, 800, ORANGE, maxw=tx - sx0)
    s.text(sx0 + 2, base + 30, d["leyenda_estable"], 11, 600, MUTED, "start", X1 - sx0)
    s.text(sx0 + 2, base + 46, d["leyenda_inestable"], 11, 800, ORANGE, "start", X1 - sx0)
    return max(left_bottom, base + 50)


# ════════════════════════════════════════════════════════════ DISEÑO 19: MAPA CORPORAL
def mapa_signos(s, y, d):
    """Cuerpo dibujado con los signos numerados + tarjetas con foto real de los signos clave."""
    y = section(s, y + 10, d["rotulo"])
    PW, PH = 310, d.get("PH", 470)
    panel(s, X0, y, PW, PH, d["ilu_titulo"])
    d["ilu"](s, X0 + 8, y + 38)
    pl = wrap(d["ilu_pie"], PW - 30, 11)
    s.text(X0 + PW / 2, y + PH - 12 - (len(pl) - 1) * 15, pl, 11, 600, SLATE, maxw=PW - 30, lh=15)
    x, w = X0 + PW + 18, X1 - (X0 + PW + 18)
    cy = y
    for n, it in enumerate(d["signos"], 1):
        on = it.get("on", False)
        f = it.get("foto")
        fw = 200 if f else 0
        tw_ = w - 44 - (fw + 12 if f else 0)
        tl = wrap(it["tit"], tw_, 12.5, True)
        bl = []
        for l in it["lines"]:
            bl += wrap(l, tw_, 11)
        th = 16 + len(tl) * 17 + 4 + len(bl) * 15 + 12
        fh = fw * f["ratio"] if f else 0
        h = max(th, fh + 38 if f else 0)
        s.rect(x, cy, w, h, TEAL_L if on else "#ffffff", TEAL if on else LINE, 2.2 if on else 1.5)
        s.circle(x + 20, cy + 22, 12, ORANGE)
        s.text(x + 20, cy + 26.5, str(n), 13, 800, "#ffffff", maxw=0)
        s.text(x + 40, cy + 26, tl, 12.5, 800, TEAL_D if on else INK, "start", tw_, lh=17)
        s.text(x + 40, cy + 26 + len(tl) * 17 + 4, bl, 11, 400, SLATE, "start", tw_, lh=15)
        if f:
            fx = x + w - fw - 12
            _img(s, fx, cy + 12, fw, fh, f)
            if f.get("credito"):
                credito(s, fx, cy + 12 + fh + 14, fw, f["credito"])
        if on and d.get("tag"):
            case_chip(s, x + w - 70, cy, d["tag"])
        cy += h + 10
    return max(y + PH, cy - 10) + 4


# ════════════════════════════════════════════════════════════ DISEÑO 20: ÁRBOL CON IMAGEN
def arbol_imagen(s, y, d):
    """Pregunta → dos ramas; la rama del caso lleva la imagen que se pide y cómo se lee."""
    y = section(s, y + 10, d["rotulo"])
    hb = hexagon(s, y, d["pregunta"], 220, 780)
    LWc = 300
    RW = X1 - X0 - LWc - 24
    lx, rx = X0 + LWc / 2, X1 - RW / 2
    s.line(500, hb, 500, hb + 20)
    s.line(lx, hb + 20, rx, hb + 20)
    s.arrow_down(lx, hb + 20, hb + 56)
    s.arrow_down(rx, hb + 20, hb + 56, ORANGE)
    (e0, t0, l0), (e1, t1, l1) = d["ramas"]
    s.pill(lx, hb + 38, e0, "#64748b")
    s.pill(rx, hb + 38, e1, ORANGE)
    by = hb + 56
    # rama izquierda: solo texto
    h0 = card6(s, X0, by, LWc, t0, l0, fs=11.5)
    # rama derecha (caso): texto + dibujo
    x1 = X1 - RW
    tl = wrap(t1, RW - 36, 13, True)
    bl = []
    for l in l1:
        bl += wrap(l, RW - 36, 11.5)
    head = 20 + len(tl) * 18 + 4 + len(bl) * 16 + 10
    IW, IH = d["IW"], d["IH"]
    pl = wrap(d["ilu_pie"], RW - 36, 11.5)
    H = head + IH + 10 + len(pl) * 16 + 14
    s.rect(x1, by, RW, H, TEAL_L, TEAL, 2.2)
    case_chip(s, x1 + RW - 70, by, d.get("tag", "ESTE CASO"))
    s.text(x1 + 18, by + 26, tl, 13, 800, TEAL_D, "start", RW - 36, lh=18)
    s.text(x1 + 18, by + 26 + len(tl) * 18 + 4, bl, 11.5, 400, SLATE, "start", RW - 36, lh=16)
    d["ilu"](s, x1 + (RW - IW) / 2, by + head)
    s.text(x1 + 18, by + head + IH + 22, pl, 11.5, 600, SLATE, "start", RW - 36, lh=16)
    y = by + max(h0, H) + 22
    return fila_cards(s, y, d["luego"], d.get("tag"), d.get("luego_titulo"))


LAYOUTS6 = {"comparador": comparador, "escalera": escalera, "mapa_signos": mapa_signos, "arbol_imagen": arbol_imagen}


def build6(spec):
    _n[0] = 0
    s = SVG()
    y = header(s, spec["barra"], spec["esp"])
    y, _ = top_row(s, y, spec["tema"], spec["caso"], "Marca dónde cae este caso", "rombo")
    y = LAYOUTS6[spec["tipo"]](s, y + 8, spec["d"])
    if spec.get("tabla"):
        y = table(s, y + 24, spec["tabla"])
    y = perlas(s, y + 24, spec["perlas"], spec["fuente"])
    H = y + 18
    t = escape(spec["titulo"])
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink" width="1000" height="{H:.0f}" '
            f'viewBox="0 0 1000 {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" '
            f'aria-label="{t}"><title>{t}</title>'
            f'<rect x="0.75" y="0.75" width="998.5" height="{H-1.5:.1f}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>')
    return head + "".join(s.p) + "</svg>"
