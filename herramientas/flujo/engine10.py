"""Diseños 26, 28, 31, 35-38, 43-45 y 49 (Entrega 4). Se dibujan con engine7.build7 (tipo = nombre del diseño).
 26 carriles       · algoritmo en carriles por servicio (quién hace qué y en qué orden)
 28 capas          · corte por capas de un tejido con la profundidad de la lesión y lo que cambia en cada capa
 31 venn           · diagrama de Venn de tres síndromes/enfermedades con la región del caso
 35 dermatomas     · silueta con niveles segmentarios y el nivel del caso
 36 genealogia     · árbol genealógico con símbolos estándar y patrón de herencia
 37 farmaco        · ruta del fármaco o la toxina por compartimentos (sangre → membrana → citoplasma → núcleo)
 38 antes_despues  · dos paneles (antes / después del tratamiento) con la intervención y los cambios
 43 pruebas        · tabla 2×2 de pruebas diagnósticas con sensibilidad, especificidad y valores predictivos calculados
 44 linea_vida     · eje de edad con barras de tamizaje/vacunas y el marcador del paciente
 45 triptico       · tres imágenes reales en columnas con pie y la del caso resaltada
 49 dos_preguntas  · dos (o tres) preguntas encadenadas: lo que se responde primero decide lo siguiente"""
import math
from engine import wrap, tw, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE
from engine2 import X0, X1
from engine3 import section, case_chip, AMBER, AMBER_L
from engine5 import ORANGE, ORANGE_L, GREEN, GREEN_L, RED, RED_L
from engine6 import credito
from engine9 import _fin, _caja_txt, _img, _img_h

W = X1 - X0
GRIS = "#94a3b8"


def _flecha(s, x1, y1, x2, y2, color=TEAL, sw=2.2):
    """Línea con punta de flecha en (x2, y2)."""
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - 9 * math.cos(a), y2 - 9 * math.sin(a)
    s.line(x1, y1, bx, by, color, sw)
    px, py = -math.sin(a) * 5, math.cos(a) * 5
    s.add(f'<polygon points="{bx+px:.1f},{by+py:.1f} {bx-px:.1f},{by-py:.1f} {x2:.1f},{y2:.1f}" fill="{color}"/>')


def _codo(s, x1, y1, x2, y2, color=TEAL, sw=2.2):
    """Conector en codo (horizontal-vertical-horizontal) con punta en el extremo."""
    xm = (x1 + x2) / 2
    s.line(x1, y1, xm, y1, color, sw)
    s.line(xm, y1, xm, y2, color, sw)
    _flecha(s, xm, y2, x2, y2, color, sw)


def _caja(s, x, y, w, t, dd, on, ft=11.5, fd=10.5, minh=0, num=None):
    """Caja con título en negrita y detalle; la del caso va en naranja. Devuelve el alto."""
    tl, dl, th = _caja_txt(t, dd, w - 20, ft, fd)
    h = max(th + 20, minh)
    s.rect(x, y, w, h, ORANGE_L if on else "#ffffff", ORANGE if on else TEAL, 2.2 if on else 1.4, rx=10)
    s.text(x + 10, y + 16, tl, ft, 800, "#9a3412" if on else INK, "start", w - 20, lh=16)
    if dl:
        s.text(x + 10, y + 16 + len(tl) * 16 + 1, dl, fd, 400, SLATE, "start", w - 20, lh=14.5)
    if num is not None:
        s.circle(x, y, 11, ORANGE if on else TEAL_D, "#ffffff", 2)
        s.text(x, y + 4, str(num), 11, 800, "#ffffff", maxw=0)
    return h


def _hh(t, dd, w, ft=11.5, fd=10.5):
    tl, dl, th = _caja_txt(t, dd, w - 20, ft, fd)
    return th + 20


# ════════════════════════════════════════════════════════════ 26 CARRILES
def carriles(s, y, d):
    """d: rotulo, carriles=[nombre], pasos=[(carril, titulo, detalle, caso?)] en orden, veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    car = d["carriles"]
    pasos = d["pasos"]
    n = len(pasos)
    lw = 108
    gx = 14
    cw = (W - lw - gx * (n - 1) - 10) / n
    cw = max(cw, 110)
    hs = [_hh(t, dd, cw) for _, t, dd, _ in pasos]
    rh = max(hs) + 26
    top = y
    for i, nombre in enumerate(car):
        yy = top + i * rh
        s.rect(X0, yy, W, rh, "#f8fafc" if i % 2 == 0 else "#f1f5f9", LINE, 1, rx=0)
        s.rect(X0, yy, lw, rh, TEAL_D, rx=0)
        s.text(X0 + lw / 2, yy + rh / 2 - 4 * (len(wrap(nombre, lw - 14, 11.5, True)) - 1) + 4,
               wrap(nombre, lw - 14, 11.5, True), 11.5, 800, "#ffffff", maxw=lw - 14, lh=14)
    pos = []
    for i, (c, t, dd, on) in enumerate(pasos):
        x = X0 + lw + 10 + i * (cw + gx)
        yy = top + c * rh + 13
        pos.append((x, yy, hs[i]))
    for i in range(n - 1):
        x1, y1, h1 = pos[i]
        x2, y2, h2 = pos[i + 1]
        _codo(s, x1 + cw, y1 + h1 / 2, x2, y2 + h2 / 2, ORANGE if pasos[i + 1][3] else TEAL)
    for i, (c, t, dd, on) in enumerate(pasos):
        x, yy, _ = pos[i]
        _caja(s, x, yy, cw, t, dd, on, num=i + 1)
    y = top + len(car) * rh
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 28 CAPAS
def capas(s, y, d):
    """d: rotulo, capas=[(nombre, grosor_txt, color, titulo_fila, detalle_fila)] de superficial a profunda,
    prof = índice de la capa más profunda alcanzada en el caso, lateral_titulo, veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    cap = d["capas"]
    prof = d["prof"]
    lw = 300
    rx = X0 + lw + 36
    rw = X1 - rx
    hs = [max(54, _hh(f, g, rw - 6, 12, 11)) for _, _, _, f, g in cap]
    top = y + 24
    yy = top
    for i, ((nom, gr, col, f, g), h) in enumerate(zip(cap, hs)):
        on = i <= prof
        s.rect(X0, yy, lw, h, col, "#ffffff", 2, rx=0)
        if on:
            s.add(f'<rect x="{X0}" y="{yy:.1f}" width="{lw}" height="{h:.1f}" fill="#b91c1c" opacity="0.22"/>')
        s.text(X0 + 14, yy + h / 2 - 2, nom, 12.5, 800, INK, "start", lw - 100)
        s.text(X0 + 14, yy + h / 2 + 14, gr, 10.5, 400, SLATE, "start", lw - 100)
        if i == prof:
            s.text(X0 + lw - 12, yy + h / 2 + 4, "◄ llega aquí", 11, 800, "#b91c1c", "end", 96)
        cur = i == prof
        fy = yy
        s.rect(rx, fy + 2, rw, h - 4, ORANGE_L if cur else "#ffffff", ORANGE if cur else LINE, 2.2 if cur else 1.2, rx=8)
        tl, dl, _ = _caja_txt(f, g, rw - 24, 12, 11)
        s.text(rx + 12, fy + 20, tl, 12, 800, "#9a3412" if cur else INK, "start", rw - 24, lh=16)
        if dl:
            s.text(rx + 12, fy + 20 + len(tl) * 16, dl, 11, 400, SLATE, "start", rw - 24, lh=15)
        yy += h
    s.line(X0 + lw + 6, top + 6, X0 + lw + 6, yy - 6, "#b91c1c", 2.5, "4 4")
    _flecha(s, X0 + lw + 6, yy - 10, X0 + lw + 6, yy - 6, "#b91c1c")
    s.text(rx, top - 6, d.get("lateral_titulo", "Según la profundidad").upper(), 10.5, 800, MUTED, "start", rw)
    s.text(X0, top - 6, "CAPAS (DE SUPERFICIAL A PROFUNDA)", 10.5, 800, MUTED, "start", lw)
    case_chip(s, rx + rw - 60, top + sum(hs[:prof]) + 2, d.get("tag", "ESTE CASO"))
    return _fin(s, yy, d)


# ════════════════════════════════════════════════════════════ 31 VENN
_REG = {  # centro de cada región (dx, dy) respecto al centro del dibujo, y ancho de texto
    "A": (-128, -62, 88), "B": (128, -62, 88), "C": (0, 128, 110), "AB": (0, -90, 70), "AC": (-70, 42, 78),
    "BC": (70, 42, 78), "ABC": (0, -4, 74)}


def venn(s, y, d):
    """d: rotulo, conjuntos=[(nombre, color)] (2 o 3), regiones={'A': [líneas], 'AB': [...], 'ABC': [...]}, caso='AB',
    lado_titulo, lado=[(titulo, [líneas], on)], veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    conj = d["conjuntos"]
    tres = len(conj) == 3
    VW = 520
    cx, cy = X0 + VW / 2, y + (210 if tres else 140)
    R = 112 if tres else 104
    cen = [(-72, -46), (72, -46), (0, 66)] if tres else [(-62, 0), (62, 0)]
    for (nom, col), (dx, dy) in zip(conj, cen):
        s.add(f'<circle cx="{cx+dx:.1f}" cy="{cy+dy:.1f}" r="{R}" fill="{col}" fill-opacity="0.22" stroke="{col}" stroke-width="2.4"/>')
    ncx = [(-130, -170), (130, -170), (0, 190)] if tres else [(-100, -116), (100, -116)]
    for (nom, col), (dx, dy) in zip(conj, ncx):
        s.text(cx + dx, cy + dy, wrap(nom, 150, 12.5, True), 12.5, 800, INK, maxw=150, lh=15)
    regs = d["regiones"]
    if not tres:
        reg_pos = {"A": (-100, -4, 80), "B": (100, -4, 80), "AB": (0, -4, 58)}
    else:
        reg_pos = _REG
    for k, lines in regs.items():
        dx, dy, w = reg_pos[k]
        on = k == d.get("caso")
        ls = []
        for l in lines:
            ls += wrap(l, w, 10.5)
        h = len(ls) * 13 + 8
        if on:
            s.rect(cx + dx - w / 2 - 5, cy + dy - h / 2 - 2, w + 10, h + 4, "#ffffff", ORANGE, 2.6, rx=8)
        s.text(cx + dx, cy + dy - h / 2 + 12, ls, 10.5, 800 if on else 600, "#9a3412" if on else INK, maxw=w, lh=13)
    bottom = cy + (R + 106 if tres else R + 14)
    lx = X0 + VW + 20
    lw = X1 - lx
    yy = y
    s.text(lx, yy + 12, d.get("lado_titulo", "Cómo leer el diagrama").upper(), 10.5, 800, MUTED, "start", lw)
    yy += 24
    for t, ls, on in d["lado"]:
        yy += _caja(s, lx, yy, lw, t, ls, on) + 10
    return _fin(s, max(bottom, yy), d)


# ════════════════════════════════════════════════════════════ 35 DERMATOMAS
def _silueta(s, cx, top, hgt):
    """Silueta humana frontal sencilla (cabeza, tronco, brazos, piernas) de alto hgt."""
    u = hgt / 100
    f, st = "#e2e8f0", "#94a3b8"
    s.add(f'<circle cx="{cx:.1f}" cy="{top+7*u:.1f}" r="{6.5*u:.1f}" fill="{f}" stroke="{st}" stroke-width="1.6"/>')
    s.add(f'<rect x="{cx-3*u:.1f}" y="{top+12*u:.1f}" width="{6*u:.1f}" height="{4*u:.1f}" fill="{f}" stroke="{st}" stroke-width="1.2"/>')
    s.add(f'<path d="M{cx-17*u:.1f},{top+17*u:.1f} Q{cx},{top+13*u:.1f} {cx+17*u:.1f},{top+17*u:.1f} L{cx+14*u:.1f},{top+53*u:.1f} L{cx-14*u:.1f},{top+53*u:.1f} Z" fill="{f}" stroke="{st}" stroke-width="1.6"/>')
    for sg in (-1, 1):
        s.add(f'<path d="M{cx+sg*17*u:.1f},{top+18*u:.1f} L{cx+sg*27*u:.1f},{top+22*u:.1f} L{cx+sg*30*u:.1f},{top+52*u:.1f} L{cx+sg*25*u:.1f},{top+52*u:.1f} L{cx+sg*21*u:.1f},{top+28*u:.1f} Z" fill="{f}" stroke="{st}" stroke-width="1.4"/>')
        s.add(f'<path d="M{cx+sg*1*u:.1f},{top+53*u:.1f} L{cx+sg*14*u:.1f},{top+53*u:.1f} L{cx+sg*12*u:.1f},{top+97*u:.1f} L{cx+sg*4*u:.1f},{top+97*u:.1f} Z" fill="{f}" stroke="{st}" stroke-width="1.4"/>')


def dermatomas(s, y, d):
    """d: rotulo, niveles=[(rotulo, fracción_altura_0a1, referencia)] de arriba abajo, caso=índice, lado=[(titulo,[líneas],on)],
    veredicto/claves. La silueta ocupa la izquierda; a la derecha de cada nivel, su referencia anatómica."""
    y = section(s, y + 10, d["rotulo"])
    H = d.get("alto", 330)
    cx = X0 + 150
    _silueta(s, cx, y + 6, H)
    for i, (rot, fr, ref) in enumerate(d["niveles"]):
        on = i == d["caso"]
        yy = y + 6 + 17 * H / 100 + fr * (53 - 17) * H / 100 if fr <= 1 else y + 6 + fr / 100 * H
        s.add(f'<rect x="{cx-30*H/100*0.55:.1f}" y="{yy-3:.1f}" width="{60*H/100*0.55:.1f}" height="6" fill="{ORANGE if on else TEAL}" opacity="{0.9 if on else 0.45}" rx="3"/>')
        s.line(cx + 22 * H / 100 * 0.55, yy, X0 + 262, yy, ORANGE if on else GRIS, 2 if on else 1.2, None if on else "3 3")
        s.text(X0 + 270, yy + 4, rot, 12, 800, "#9a3412" if on else INK, "start", 56)
        s.text(X0 + 332, yy + 4, wrap(ref, 170, 10.5)[0], 10.5, 600 if on else 400, "#9a3412" if on else SLATE, "start", 170)
    x = X0 + 540
    w = X1 - x
    yy = y
    for t, ls, on in d["lado"]:
        yy += _caja(s, x, yy, w, t, ls, on) + 10
    return _fin(s, max(yy, y + H + 14), d)


# ════════════════════════════════════════════════════════════ 36 GENEALOGÍA
def _simb(s, x, y, sexo, est, r=17):
    """Símbolo estándar: cuadrado (varón) o círculo (mujer); lleno = afectado, mitad = portador."""
    f = "#1e293b" if est == "afectado" else "#ffffff"
    if sexo == "M":
        s.add(f'<rect x="{x-r:.1f}" y="{y-r:.1f}" width="{2*r}" height="{2*r}" fill="{f}" stroke="#1e293b" stroke-width="2.2"/>')
        if est == "portador":
            s.add(f'<rect x="{x-r:.1f}" y="{y-r:.1f}" width="{r}" height="{2*r}" fill="#1e293b"/>')
    else:
        s.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{f}" stroke="#1e293b" stroke-width="2.2"/>')
        if est == "portador":
            s.add(f'<path d="M{x:.1f},{y-r:.1f} A{r},{r} 0 0 0 {x:.1f},{y+r:.1f} Z" fill="#1e293b"/>')
    if est == "muerto":
        s.line(x - r - 5, y + r + 5, x + r + 5, y - r - 5, "#1e293b", 2)


def genealogia(s, y, d):
    """d: rotulo, personas=[(clave, sexo 'M'|'F', estado 'afectado'|'portador'|'sano'|'muerto', generación, posición_x 0-1, etiqueta)],
    parejas=[(k1, k2)], hijos=[((k1, k2), [claves])], caso=clave del paciente, lado=[(titulo,[líneas],on)], veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    gen_h = 104
    ng = max(p[3] for p in d["personas"]) + 1
    PW_ = 560
    pos = {}
    for k, sx, est, g, fx, et in d["personas"]:
        pos[k] = (X0 + 40 + fx * (PW_ - 80), y + 34 + g * gen_h, sx, est, et)
    for g in range(ng):
        s.text(X0 + 2, y + 38 + g * gen_h, ["I", "II", "III", "IV", "V"][g], 12, 800, MUTED, "start", 20)
    for k1, k2 in d["parejas"]:
        a, b = pos[k1], pos[k2]
        s.line(a[0] + 17, a[1], b[0] - 17, b[1], "#1e293b", 2)
    for par, hijos in d["hijos"]:
        a, b = pos[par[0]], pos[par[1]]
        mx, my = (a[0] + b[0]) / 2, a[1]
        by = my + 44
        xs = [pos[h][0] for h in hijos]
        s.line(mx, my, mx, by, "#1e293b", 2)
        s.line(min(xs + [mx]), by, max(xs + [mx]), by, "#1e293b", 2)
        for h in hijos:
            s.line(pos[h][0], by, pos[h][0], pos[h][1] - 17, "#1e293b", 2)
    for k, (x, yy, sx, est, et) in pos.items():
        _simb(s, x, yy, sx, est)
        if k == d.get("caso"):
            _flecha(s, x - 44, yy + 36, x - 18, yy + 20, ORANGE, 3)
            s.text(x - 44, yy + 52, "paciente", 10.5, 800, "#9a3412", maxw=70)
        if et:
            s.text(x, yy + 33, wrap(et, 84, 10), 10, 500, SLATE, maxw=84, lh=12)
    # leyenda
    ly = y + 34 + (ng - 1) * gen_h + 74
    lx = X0 + 6
    for sx, est, tx in (("M", "sano", "Varón"), ("F", "sano", "Mujer"), ("M", "afectado", "Afectado"), ("F", "portador", "Portadora")):
        _simb(s, lx + 10, ly, sx, est, 9)
        s.text(lx + 26, ly + 4, tx, 10.5, 600, SLATE, "start", 80)
        lx += 110
    x = X0 + PW_ + 20
    w = X1 - x
    yy = y
    for t, ls, on in d["lado"]:
        yy += _caja(s, x, yy, w, t, ls, on) + 10
    return _fin(s, max(yy, ly + 22), d)


# ════════════════════════════════════════════════════════════ 37 RUTA DEL FÁRMACO
def farmaco(s, y, d):
    """d: rotulo, zonas=[(nombre, color)] de afuera hacia adentro, pasos=[(zona, titulo, detalle, caso?)] en orden,
    veredicto/claves. Cada zona es una franja; los pasos van numerados y conectados."""
    y = section(s, y + 10, d["rotulo"])
    zonas = d["zonas"]
    pasos = d["pasos"]
    lw = 112
    por = {}
    for i, p in enumerate(pasos):
        por.setdefault(p[0], []).append(i)
    top = y
    pos = {}
    for zi, (nom, col) in enumerate(zonas):
        idx = por.get(zi, [])
        n = max(1, len(idx))
        cw = (W - lw - 24 - 16 * (n - 1)) / n
        cw = min(cw, 300)
        hs = [_hh(pasos[i][1], pasos[i][2], cw) for i in idx] or [28]
        zh = max(hs) + 30
        s.rect(X0, top, W, zh, col, "#ffffff", 2, rx=0)
        s.rect(X0, top, lw, zh, TEAL_D, rx=0)
        s.text(X0 + lw / 2, top + zh / 2 - 4 * (len(wrap(nom, lw - 14, 11.5, True)) - 1) + 4,
               wrap(nom, lw - 14, 11.5, True), 11.5, 800, "#ffffff", maxw=lw - 14, lh=14)
        for j, i in enumerate(idx):
            pos[i] = (X0 + lw + 20 + j * (cw + 16), top + 15, cw, hs[j])
        top += zh
    for i in range(len(pasos) - 1):
        x1, y1, w1, h1 = pos[i]
        x2, y2, w2, h2 = pos[i + 1]
        col = ORANGE if pasos[i + 1][3] else TEAL
        if abs(y1 - y2) < 2:
            _flecha(s, x1 + w1, y1 + h1 / 2, x2, y2 + h2 / 2, col)
        else:
            _flecha(s, x1 + w1 / 2, y1 + h1, x2 + w2 / 2, y2 - 2, col)
    for i, (z, t, dd, on) in enumerate(pasos):
        x, yy, w, h = pos[i]
        _caja(s, x, yy, w, t, dd, on, num=i + 1)
    return _fin(s, top, d)


# ════════════════════════════════════════════════════════════ 38 ANTES Y DESPUÉS
def antes_despues(s, y, d):
    """d: rotulo, antes={titulo, datos[(rótulo, valor)], img?}, despues={…}, intervencion (texto), cambios=[(texto, 'mejora'|'peor'|'igual')],
    veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    pw = (W - 150) / 2
    alto = 0
    for k in ("antes", "despues"):
        p = d[k]
        h = 40 + (_img_h(p["img"]) + 8 if p.get("img") else 0) + len(p["datos"]) * 26 + 10
        alto = max(alto, h)
    for k, x, col, bg in (("antes", X0, RED, RED_L), ("despues", X1 - pw, GREEN, GREEN_L)):
        p = d[k]
        s.rect(x, y, pw, alto, bg, col, 2, rx=14)
        s.text(x + pw / 2, y + 26, p["titulo"].upper(), 13, 800, col, maxw=pw - 20)
        yy = y + 40
        if p.get("img"):
            im = p["img"]
            _img(s, x + (pw - im["W"]) / 2, yy, im)
            yy += _img_h(im) + 8
        for r, v in p["datos"]:
            s.text(x + 16, yy + 16, r, 11.5, 600, SLATE, "start", pw * 0.5)
            s.text(x + pw - 16, yy + 16, v, 12, 800, INK, "end", pw * 0.45)
            s.line(x + 12, yy + 24, x + pw - 12, yy + 24, "#ffffff", 1.4)
            yy += 26
    mx = X0 + pw + 75
    il = wrap(d["intervencion"], 126, 12, True)
    s.rect(mx - 66, y + alto / 2 - 20 - len(il) * 8, 132, 40 + len(il) * 16, TEAL_D, rx=12)
    s.text(mx, y + alto / 2 - 4 - (len(il) - 1) * 8 + 8 - 6, il, 12, 800, "#ffffff", maxw=118, lh=16)
    _flecha(s, X0 + pw + 4, y + alto / 2 + 40 + len(il) * 8, X1 - pw - 4, y + alto / 2 + 40 + len(il) * 8, TEAL, 3)
    y += alto + 16
    cols = {"mejora": (GREEN, GREEN_L, "▲"), "peor": (RED, RED_L, "▼"), "igual": (MUTED, "#f1f5f9", "=")}
    n = len(d["cambios"])
    cw = (W - 10 * (n - 1)) / n
    ch = max(len(wrap(t, cw - 40, 11.5, True)) for t, _ in d["cambios"]) * 15 + 18
    for i, (t, tipo) in enumerate(d["cambios"]):
        c, bg, sg = cols[tipo]
        x = X0 + i * (cw + 10)
        s.rect(x, y, cw, ch, bg, c, 1.6, rx=10)
        s.text(x + 16, y + ch / 2 + 5, sg, 14, 800, c, maxw=0)
        s.text(x + 32, y + 18, wrap(t, cw - 40, 11.5, True), 11.5, 800, INK, "start", cw - 40, lh=15)
    return _fin(s, y + ch, d)


# ════════════════════════════════════════════════════════════ 43 TABLA 2×2 DE PRUEBAS
def pruebas(s, y, d):
    """d: rotulo, enfermedad (texto), prueba (texto), vp, fp, fn, vn, pide ('sens'|'esp'|'vpp'|'vpn'|'lr+'), lado=[(titulo,[líneas],on)],
    veredicto/claves. Calcula las medidas a partir de los cuatro valores."""
    y = section(s, y + 10, d["rotulo"])
    vp, fp, fn, vn = d["vp"], d["fp"], d["fn"], d["vn"]
    sens, esp = vp / (vp + fn), vn / (vn + fp)
    vpp, vpn = vp / (vp + fp), vn / (vn + fn)
    med = {"sens": ("Sensibilidad", "VP / (VP + FN)", f"{vp}/{vp+fn}", sens), "esp": ("Especificidad", "VN / (VN + FP)", f"{vn}/{vn+fp}", esp),
           "vpp": ("Valor predictivo +", "VP / (VP + FP)", f"{vp}/{vp+fp}", vpp), "vpn": ("Valor predictivo −", "VN / (VN + FN)", f"{vn}/{vn+fn}", vpn)}
    tx, ty = X0 + 90, y + 52
    cw, ch = 150, 70
    s.text(tx + cw, y + 14, d["enfermedad"].upper(), 10.5, 800, MUTED, maxw=2 * cw)
    s.text(tx + cw / 2, y + 40, "Enfermos", 12, 800, RED, maxw=cw)
    s.text(tx + cw * 1.5, y + 40, "Sanos", 12, 800, GREEN, maxw=cw)
    s.text(X0 + 40, ty + ch - 6, wrap(d["prueba"], 80, 10.5, True), 10.5, 800, MUTED, maxw=80, lh=13)
    celdas = [("VP", vp, 0, 0, GREEN_L, GREEN), ("FP", fp, 1, 0, RED_L, RED), ("FN", fn, 0, 1, RED_L, RED), ("VN", vn, 1, 1, GREEN_L, GREEN)]
    s.text(X0 + 40, ty + ch * 1.5 + 6, ["Prueba", "negativa"], 10.5, 800, MUTED, maxw=80, lh=13)
    s.text(X0 + 40, ty + ch / 2 - 16 - 0, ["Prueba", "positiva"], 10.5, 800, MUTED, maxw=80, lh=13)
    for k, v, cx, cy, bg, col in celdas:
        s.rect(tx + cx * cw, ty + cy * ch, cw, ch, bg, "#ffffff", 3, rx=0)
        s.text(tx + cx * cw + cw / 2, ty + cy * ch + 30, str(v), 24, 800, col, maxw=cw - 20)
        s.text(tx + cx * cw + cw / 2, ty + cy * ch + 52, {"VP": "verdadero +", "FP": "falso +", "FN": "falso −", "VN": "verdadero −"}[k], 11, 600, SLATE, maxw=cw - 20)
    yb = ty + 2 * ch + 18
    n = 4
    bw = (2 * cw + 90 - 8 * (n - 1)) / n
    for i, k in enumerate(("sens", "esp", "vpp", "vpn")):
        nom, fm, fr, val = med[k]
        on = k == d["pide"]
        x = X0 + i * (bw + 8)
        s.rect(x, yb, bw, 102, ORANGE_L if on else "#ffffff", ORANGE if on else TEAL, 2.4 if on else 1.4, rx=10)
        s.text(x + bw / 2, yb + 18, wrap(nom, bw - 10, 10.5, True), 10.5, 800, "#9a3412" if on else MUTED, maxw=bw - 10)
        s.text(x + bw / 2, yb + 60, f"{val*100:.0f} %" if val * 100 >= 10 or val == 0 else f"{val*100:.1f} %", 21, 800, "#9a3412" if on else TEAL_D, maxw=bw - 10)
        s.text(x + bw / 2, yb + 78, fm, 9.5, 500, SLATE, maxw=bw - 8)
        s.text(x + bw / 2, yb + 92, fr, 9.5, 700, SLATE, maxw=bw - 8)
    x = X0 + 2 * cw + 130
    w = X1 - x
    yy = y
    for t, ls, on in d["lado"]:
        yy += _caja(s, x, yy, w, t, ls, on) + 10
    return _fin(s, max(yy, yb + 102), d)


# ════════════════════════════════════════════════════════════ 44 LÍNEA DE VIDA
def linea_vida(s, y, d):
    """d: rotulo, eje=(mín, máx, paso), unidad, barras=[(texto, desde, hasta, detalle, caso?)], marcador=(edad, texto),
    veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    a, b, paso = d["eje"]
    lx, rx_ = X0 + 250, X1 - 20
    f = lambda v: lx + (v - a) / (b - a) * (rx_ - lx)
    n = len(d["barras"])
    rh = 38
    top = y + 26
    for v in range(a, b + 1, paso):
        s.line(f(v), top - 4, f(v), top + n * rh, "#e2e8f0", 1)
        s.text(f(v), top - 8, f"{v}", 10.5, 600, MUTED, maxw=30)
    s.text(rx_, top - 22, d.get("unidad", "años"), 10.5, 700, MUTED, "end", 60)
    for i, (t, d0, d1, dd, on) in enumerate(d["barras"]):
        yy = top + i * rh
        if i % 2 == 0:
            s.rect(X0, yy, W, rh, "#f8fafc", "none", rx=0)
        s.text(X0 + 8, yy + 16, wrap(t, 236, 11.5, True)[0], 11.5, 800, "#9a3412" if on else INK, "start", 236)
        s.text(X0 + 8, yy + 31, wrap(dd, 236, 10)[0], 10, 400, SLATE, "start", 236)
        s.rect(f(d0), yy + 8, max(6, f(d1) - f(d0)), 22, ORANGE if on else TEAL, rx=6)
    e, et = d["marcador"]
    s.line(f(e), top - 2, f(e), top + n * rh + 6, "#b91c1c", 2.6)
    s.rect(f(e) - tw(et, 11, True) / 2 - 8, top + n * rh + 6, tw(et, 11, True) + 16, 22, "#b91c1c", rx=11)
    s.text(f(e), top + n * rh + 21, et, 11, 800, "#ffffff", maxw=0)
    return _fin(s, top + n * rh + 34, d)


# ════════════════════════════════════════════════════════════ 45 TRÍPTICO DE IMÁGENES
def triptico(s, y, d):
    """d: rotulo, imgs=[(imagen(PX), titulo, [líneas], caso?)] (2 o 3), veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    n = len(d["imgs"])
    cw = (W - 14 * (n - 1)) / n
    hh = max(_img_h(im) for im, _, _, _ in d["imgs"])
    ph = []
    for im, t, ls, on in d["imgs"]:
        tl, dl, th = _caja_txt(t, ls, cw - 24, 12.5, 11)
        ph.append(th + 26)
    ph = max(ph)
    for i, (im, t, ls, on) in enumerate(d["imgs"]):
        x = X0 + i * (cw + 14)
        s.rect(x, y, cw, hh + ph + 40, ORANGE_L if on else "#ffffff", ORANGE if on else TEAL, 2.4 if on else 1.4, rx=14)
        s.circle(x + 18, y + 18, 11, ORANGE if on else TEAL_D, "#ffffff", 2)
        s.text(x + 18, y + 22, str(i + 1), 11, 800, "#ffffff", maxw=0)
        _img(s, x + (cw - im["W"]) / 2, y + 34 + (hh - _img_h(im)) / 2, im)
        tl, dl, th = _caja_txt(t, ls, cw - 24, 12.5, 11)
        ty = y + 34 + hh + 8
        s.text(x + 12, ty + 12, tl, 12.5, 800, "#9a3412" if on else INK, "start", cw - 24, lh=17)
        if dl:
            s.text(x + 12, ty + 12 + len(tl) * 17, dl, 11, 400, SLATE, "start", cw - 24, lh=16)
        if on:
            case_chip(s, x + cw - 56, y, d.get("tag", "ESTE CASO"))
    return _fin(s, y + hh + ph + 40, d)


# ════════════════════════════════════════════════════════════ 49 DOS PREGUNTAS ENCADENADAS
def dos_preguntas(s, y, d):
    """d: rotulo, pasos=[(pregunta, respuesta, razón)] (2 o 3), veredicto/claves."""
    y = section(s, y + 10, d["rotulo"])
    nw = 74
    bw = W - nw - 10
    for i, (q, r, z) in enumerate(d["pasos"]):
        ql = wrap(q, bw - 30, 13, True)
        rl = wrap(r, bw - 60, 13.5, True)
        zl = wrap(z, bw - 60, 11.5)
        h = 18 + len(ql) * 18 + 14 + len(rl) * 19 + len(zl) * 16 + 18
        s.rect(X0, y, nw, h, TEAL_D, rx=14)
        s.text(X0 + nw / 2, y + h / 2 - 6, "PASO", 10.5, 800, "#99f6e4", maxw=nw - 8)
        s.text(X0 + nw / 2, y + h / 2 + 22, str(i + 1), 28, 800, "#ffffff", maxw=nw - 8)
        x = X0 + nw + 10
        s.rect(x, y, bw, h, "#ffffff", TEAL, 1.6, rx=14)
        s.text(x + 16, y + 28, ql, 13, 800, INK, "start", bw - 30, lh=18)
        ry = y + 18 + len(ql) * 18 + 6
        rh = len(rl) * 19 + len(zl) * 16 + 18
        s.rect(x + 12, ry, bw - 24, rh, ORANGE_L, ORANGE, 2, rx=10)
        s.text(x + 28, ry + 20, rl, 13.5, 800, "#9a3412", "start", bw - 60, lh=19)
        s.text(x + 28, ry + 20 + len(rl) * 19, zl, 11.5, 400, SLATE, "start", bw - 60, lh=16)
        y += h
        if i < len(d["pasos"]) - 1:
            s.arrow_down(X0 + nw / 2, y, y + 26, TEAL)
            s.text(X0 + nw + 20, y + 18, "entonces…", 11, 700, MUTED, "start", 100)
            y += 28
    return _fin(s, y, d)


LAYOUTS10 = {"carriles": carriles, "capas": capas, "venn": venn, "dermatomas": dermatomas, "genealogia": genealogia,
             "farmaco": farmaco, "antes_despues": antes_despues, "pruebas": pruebas, "linea_vida": linea_vida,
             "triptico": triptico, "dos_preguntas": dos_preguntas}
