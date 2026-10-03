"""Clasificaciones y escalas oficiales (Page, Glasgow, CURB-65, FAB, OPS del dengue...) con el caso ubicado.
Tres formas:
  · grados en columnas (≤ 5 grados): escalera de gravedad, el grado del caso resaltado;
  · grados en filas (> 5, p. ej. FAB M0-M7): una fila por categoría;
  · puntaje: ítems con el dato del caso y sus puntos, total y rangos de conducta.
Debajo: por qué el caso cae ahí (✓ lo que cumple, ✕ lo que lo descarta del grado vecino) y la conducta."""
from engine import wrap, tw, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE
from engine2 import X0, X1
from engine3 import section, case_chip, AMBER, AMBER_L
from engine5 import ORANGE, GREEN, GREEN_L, RED, RED_L

# de menos a más grave: franja de color de cada grado (fondo, texto)
SEV = [("#dcfce7", "#166534"), ("#fef9c3", "#854d0e"), ("#ffedd5", "#9a3412"), ("#fee2e2", "#991b1b"), ("#fecaca", "#7f1d1d")]
NEU = ("#f1f5f9", "#334155")
W = X1 - X0
PAD = 16


def _sev(i, n, orden):
    if not orden:
        return NEU
    if n <= 1:
        return SEV[0]
    return SEV[round(i * (min(n, 5) - 1) / (n - 1))] if n <= 5 else SEV[min(4, i * 5 // n)]


def _cabecera(s, y, e):
    """Nombre oficial grande + para qué sirve. Devuelve el alto usado."""
    nom = e["nombre"].upper()
    nw = tw(nom, 13, True) + 30
    s.rect(X0 + PAD, y + 14, nw, 30, TEAL, rx=15)
    s.text(X0 + PAD + nw / 2, y + 34, nom, 13, 800, "#ffffff", maxw=0)
    ql = wrap(e.get("que", ""), W - 2 * PAD - nw - 18, 12.5) if e.get("que") else []
    if ql:
        s.text(X0 + PAD + nw + 16, y + 34 - (len(ql) - 1) * 8.5, ql, 12.5, 600, SLATE, "start", W - 2 * PAD - nw - 18, lh=17)
    return 14 + max(30, len(ql) * 17) + 14


def _cab_h(e):
    nw = tw(e["nombre"].upper(), 13, True) + 30
    ql = wrap(e.get("que", ""), W - 2 * PAD - nw - 18, 12.5) if e.get("que") else []
    return 14 + max(30, len(ql) * 17) + 14


# ─────────────────────────────────────────── grados en columnas
def _cols_medir(e):
    g = e["grados"]
    n = len(g)
    GAP = 12
    cw = (W - 2 * PAD - GAP * (n - 1)) / n
    cuerpos = []
    for et, nom, crit in g:
        nl = wrap(nom, cw - 24, 14, True)
        cl = [wrap(c, cw - 38, 11.5) for c in crit]
        cuerpos.append((nl, cl))
    head = max(36 + len(nl) * 19 for nl, _ in cuerpos) + 8
    body = max(sum(len(c) * 16 + 7 for c in cl) for _, cl in cuerpos) + 12
    return cw, GAP, cuerpos, head, head + body


def _cols(s, y, e):
    g = e["grados"]
    n = len(g)
    caso = e["caso"] if isinstance(e["caso"], (list, tuple)) else [e["caso"]]
    cw, GAP, cuerpos, head, ch = _cols_medir(e)
    top = y + 16          # sitio para la etiqueta «ESTE CASO» sobre la tarjeta
    # la gravedad se lee en el color de cada franja (verde → rojo)
    for i, ((et, nom, crit), (nl, cl)) in enumerate(zip(g, cuerpos)):
        x = X0 + PAD + i * (cw + GAP)
        on = i in caso
        bg, fg = _sev(i, n, e.get("orden", True))
        s.rect(x, top, cw, ch, AMBER_L if on else "#ffffff", ORANGE if on else LINE, 2.4 if on else 1.2, rx=10)
        s.rect(x + (1.2 if on else 0.6), top + (1.2 if on else 0.6), cw - (2.4 if on else 1.2), head, bg, "none", 0, rx=9)
        s.text(x + cw / 2, top + 28, et.upper(), 11, 800, fg, maxw=cw - 16)     # bajo la etiqueta «ESTE CASO»
        s.text(x + cw / 2, top + 48, nl, 14, 800, fg if not on else INK, maxw=cw - 24, lh=19)
        cy = top + head + 14
        for ln in cl:
            s.circle(x + 16, cy - 4, 3, ORANGE if on else "#94a3b8")
            s.text(x + 26, cy, ln, 11.5, 600 if on else 400, INK if on else "#334155", "start", cw - 38, lh=16)
            cy += len(ln) * 16 + 7
        if on:
            case_chip(s, x + cw / 2, top, e.get("tag", "ESTE CASO"))
    return top + ch - y


# ─────────────────────────────────────────── grados en filas
def _filas_medir(e):
    LW, NW = 70, 210
    TW_ = W - 2 * PAD - LW - NW - 30
    filas = []
    for gr in e["grados"]:
        et, nom, crit = gr[:3]
        nl = wrap(nom, NW - 16, 12.5, True)
        rl = wrap(" · ".join(crit), TW_ - 16, 11.5)
        filas.append((nl, rl, max(36, max(len(nl) * 17, len(rl) * 16) + 16)))
    return LW, NW, TW_, filas


def _filas(s, y, e):
    caso = e["caso"] if isinstance(e["caso"], (list, tuple)) else [e["caso"]]
    LW, NW, TW_, filas = _filas_medir(e)
    cy = y
    for i, (gr, (nl, rl, h)) in enumerate(zip(e["grados"], filas)):
        on = i in caso
        x = X0 + PAD
        s.rect(x, cy, W - 2 * PAD, h, AMBER_L if on else ("#ffffff" if i % 2 else "#f8fafc"), ORANGE if on else "#e2e8f0",
               2 if on else 1, rx=8)
        pw = tw(gr[0], 12, True) + 20
        s.rect(x + 10, cy + h / 2 - 12, pw, 24, ORANGE if on else TEAL, rx=12)
        s.text(x + 10 + pw / 2, cy + h / 2 + 4.5, gr[0], 12, 800, "#ffffff", maxw=0)
        s.text(x + LW + 14, cy + h / 2 + 4.5 - (len(nl) - 1) * 8.5, nl, 12.5, 800, INK if on else "#334155", "start", NW - 16, lh=17)
        s.text(x + LW + NW + 14, cy + h / 2 + 4 - (len(rl) - 1) * 8, rl, 11.5, 600 if on else 400, INK if on else SLATE, "start",
               TW_ - 16, lh=16)
        if on and len(gr) > 3 and gr[3]:
            tg = "◆ " + gr[3]
            tw_ = tw(tg, 10, True) + 16
            s.rect(X1 - PAD - 10 - tw_, cy + h / 2 - 11, tw_, 22, "#ffffff", AMBER, 1.5, rx=11)
            s.text(X1 - PAD - 10 - tw_ / 2, cy + h / 2 + 4, tg, 10, 800, "#b45309", maxw=0)
        cy += h + 6
    return cy - 6 - y


def _filas_h(e):
    return sum(h + 6 for _, _, h in _filas_medir(e)[3]) - 6


# ─────────────────────────────────────────── puntaje
def _pts_medir(e):
    SW, CW, PWc = 54, 300, 96
    DW = W - 2 * PAD - SW - CW - PWc
    filas = []
    for it in e["items"]:
        sig, crit, dato, pts = it[:4]
        cl = wrap(crit, CW - 20, 12, True)
        dl = wrap(dato, DW - 20, 11.5)
        filas.append((cl, dl, max(38, max(len(cl) * 16, len(dl) * 16) + 16)))
    return SW, CW, PWc, DW, filas


def _rangos_medir(e):
    rg = e.get("rangos", [])
    if not rg:
        return 0, 0, []
    n = len(rg)
    GAP = 10
    rw = (W - 2 * PAD - GAP * (n - 1)) / n
    cu = [(wrap(t, rw - 20, 12, True), wrap(c, rw - 20, 11.5)) for _, t, c in rg]
    rh = max(30 + len(tl) * 16 + len(cl) * 16 for tl, cl in cu) + 12
    return rw, rh, cu


def _puntaje(s, y, e):
    SW, CW, PWc, DW, filas = _pts_medir(e)
    x = X0 + PAD
    tw_all = W - 2 * PAD
    # encabezado de la tabla
    s.rect(x, y, tw_all, 30, "#f1f5f9", "#e2e8f0", 1, rx=8)
    s.text(x + SW + 10, y + 20, "CRITERIO", 10.5, 800, SLATE, "start", CW)
    s.text(x + SW + CW + 10, y + 20, "EN ESTE CASO", 10.5, 800, SLATE, "start", DW)
    s.text(x + tw_all - PWc / 2, y + 20, "PUNTOS", 10.5, 800, SLATE, maxw=PWc)
    cy = y + 34
    total = 0
    for it, (cl, dl, h) in zip(e["items"], filas):
        sig, crit, dato, pts = it[:4]
        suma = pts is not None and pts > 0
        total += pts or 0
        s.rect(x, cy, tw_all, h, TEAL_L if suma else "#ffffff", TEAL_B if suma else "#e2e8f0", 1.2, rx=8)
        bw = max(34, tw(sig, 12.5, True) + 14)
        s.rect(x + (SW - bw) / 2 + 2, cy + h / 2 - 13, bw, 26, TEAL if suma else "#94a3b8", rx=8)
        s.text(x + SW / 2 + 2, cy + h / 2 + 4.5, sig, 12.5, 800, "#ffffff", maxw=0)
        s.text(x + SW + 10, cy + h / 2 + 4 - (len(cl) - 1) * 8, cl, 12, 700, INK, "start", CW - 20, lh=16)
        s.text(x + SW + CW + 10, cy + h / 2 + 4 - (len(dl) - 1) * 8, dl, 11.5, 600 if suma else 400,
               TEAL_D if suma else SLATE, "start", DW - 20, lh=16)
        lab = f"+{pts:g}" if suma else ("0" if pts == 0 else "sin dato")
        s.text(x + tw_all - PWc / 2, cy + h / 2 + 5, lab, 14 if pts is not None else 11, 800,
               TEAL if suma else MUTED, maxw=PWc - 10)
        cy += h + 4
    # total
    tl = e.get("total_txt", f"TOTAL: {total:g} {'punto' if total == 1 else 'puntos'}")
    s.rect(x, cy + 4, tw_all, 36, TEAL_D, rx=8)
    s.text(x + 16, cy + 27, tl.upper(), 13, 800, "#ffffff", "start", tw_all - 32)
    if e.get("total_nota"):
        s.text(x + tw_all - 16, cy + 27, e["total_nota"], 11.5, 600, TEAL_B, "end", tw_all - tw(tl.upper(), 13, True) - 60)
    cy += 40
    # rangos
    rw, rh, cu = _rangos_medir(e)
    if cu:
        cy += 26
        n = len(cu)
        for i, ((rng, _, _), (tl_, cl_)) in enumerate(zip(e["rangos"], cu)):
            rx_ = x + i * (rw + 10)
            on = i == e.get("caso_rango", -1)
            bg, fg = _sev(i, n, True)
            s.rect(rx_, cy, rw, rh, AMBER_L if on else "#ffffff", ORANGE if on else LINE, 2.4 if on else 1.2, rx=10)
            s.rect(rx_ + 1, cy + 1, rw - 2, 26, bg, rx=9)
            s.text(rx_ + rw / 2, cy + 19, rng, 12, 800, fg, maxw=rw - 16)
            s.text(rx_ + 10, cy + 46, tl_, 12, 800, INK, "start", rw - 20, lh=16)
            s.text(rx_ + 10, cy + 46 + len(tl_) * 16, cl_, 11.5, 400, "#334155", "start", rw - 20, lh=16)
            if on:
                case_chip(s, rx_ + rw / 2, cy, e.get("tag", "ESTE CASO"))
        cy += rh
    return cy - y


def _puntaje_h(e):
    SW, CW, PWc, DW, filas = _pts_medir(e)
    h = 34 + sum(f[2] + 4 for f in filas) + 40
    rw, rh, cu = _rangos_medir(e)
    return h + (26 + rh if cu else 0)


# ─────────────────────────────────────────── por qué + conducta
def _porque_medir(e):
    pq = e.get("porque", [])
    lines = [(wrap(t, W - 2 * PAD - 40, 12), ok) for t, ok in pq]
    ph = (30 + sum(len(l) * 17 + 5 for l, _ in lines) + 6) if pq else 0
    cl = wrap(e["conducta"], W - 2 * PAD - 32, 12.5, True) if e.get("conducta") else []
    chh = (len(cl) * 17 + 20) if cl else 0
    return lines, ph, cl, chh


def _porque(s, y, e):
    lines, ph, cl, chh = _porque_medir(e)
    x = X0 + PAD
    if lines:
        s.text(x, y + 16, e.get("porque_titulo", "Por qué el caso cae aquí").upper(), 10.5, 800, MUTED, "start", W - 2 * PAD)
        cy = y + 38
        for l, ok in lines:
            col = GREEN if ok else RED
            s.rect(x, cy - 13, 20, 20, GREEN_L if ok else RED_L, col, 1.2, rx=5)
            s.text(x + 10, cy + 2, "✓" if ok else "✕", 12, 800, col, maxw=0)
            s.text(x + 32, cy + 2, l, 12, 600 if ok else 400, INK if ok else SLATE, "start", W - 2 * PAD - 40, lh=17)
            cy += len(l) * 17 + 5
    if cl:
        cy = y + ph + 4
        s.rect(x, cy, W - 2 * PAD, chh, TEAL, rx=8)
        s.text(x + 16, cy + 23, cl, 12.5, 800, "#ffffff", "start", W - 2 * PAD - 32, lh=17)


def escala(s, y, e):
    """e: dict(nombre, que, modo='grados'|'puntaje', grados=[(etiqueta, nombre, [criterios], tag?)], caso,
    orden=True, items=[(sigla, criterio, dato del caso, puntos)], rangos=[(rango, título, conducta)], caso_rango,
    porque=[(texto, True/False)], conducta, rotulo, tag)."""
    y = section(s, y + 6, e.get("rotulo", "Clasificación oficial"))
    modo = e.get("modo", "grados")
    filas = modo == "grados" and len(e["grados"]) > 5
    ch = _cab_h(e)
    if modo == "puntaje":
        bh = _puntaje_h(e)
    elif filas:
        bh = _filas_h(e)
    else:
        bh = 16 + _cols_medir(e)[4]
    _, ph, _, chh = _porque_medir(e)
    tail = (14 + ph + (4 + chh if chh else 0)) if (ph or chh) else 0
    H = ch + bh + tail + 16
    s.rect(X0, y, W, H, "#ffffff", LINE, 1.5, rx=12)
    _cabecera(s, y, e)
    yy = y + ch
    if modo == "puntaje":
        yy += _puntaje(s, yy, e)
    elif filas:
        yy += _filas(s, yy, e)
    else:
        yy += _cols(s, yy, e)
    if tail:
        _porque(s, yy + 14, e)
    return y + H
