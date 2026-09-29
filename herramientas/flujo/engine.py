"""Generador de flujogramas SVG con el estilo MedQuizPlus (8 diseños)."""
from PIL import ImageFont
from xml.sax.saxutils import escape

FONTS = {
    False: "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    True: "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
}
_cache = {}
SAFETY = 1.07  # margen para Segoe UI / Roboto


def tw(s, fs, bold=False):
    k = (fs, bold)
    if k not in _cache:
        _cache[k] = ImageFont.truetype(FONTS[bold], size=100)
    return _cache[k].getlength(s) * fs / 100 * SAFETY


def wrap(s, maxw, fs, bold=False):
    out = []
    for para in s.split("\n"):
        cur = ""
        for w in para.split(" "):
            t = (cur + " " + w).strip()
            if tw(t, fs, bold) <= maxw or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


TEAL = "#0f766e"; TEAL_D = "#134e4a"; TEAL_L = "#f0fdfa"; TEAL_B = "#99f6e4"
INK = "#0f172a"; SLATE = "#475569"; MUTED = "#64748b"; LINE = "#cbd5e1"; BORDER = "#94a3b8"
ACCENTS = ["#0ea5e9", "#f59e0b", "#8b5cf6", "#10b981", "#e11d48", "#6366f1"]


class SVG:
    def __init__(self):
        self.p = []

    def add(self, s):
        self.p.append(s)

    def rect(self, x, y, w, h, fill, stroke="none", sw=1.5, rx=10, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, color=TEAL, sw=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{sw}"{d}/>')

    def arrow_down(self, x, y1, y2, color=TEAL):
        self.line(x, y1, x, y2 - 7, color)
        self.add(f'<polygon points="{x-5:.1f},{y2-8:.1f} {x+5:.1f},{y2-8:.1f} {x:.1f},{y2:.1f}" fill="{color}"/>')

    def arrow_right(self, x1, x2, y, color=TEAL):
        self.line(x1, y, x2 - 7, y, color)
        self.add(f'<polygon points="{x2-8:.1f},{y-5:.1f} {x2-8:.1f},{y+5:.1f} {x2:.1f},{y:.1f}" fill="{color}"/>')

    def circle(self, cx, cy, r, fill, stroke="none", sw=0):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def text(self, x, y, lines, fs=12, weight=400, fill=INK, anchor="middle", maxw=0, lh=None, italic=False):
        if isinstance(lines, str):
            lines = [lines]
        lh = lh or round(fs * 1.42, 1)
        ts = "".join(
            f'<tspan x="{x:.1f}" dy="{0 if i == 0 else lh}">{escape(l)}</tspan>' for i, l in enumerate(lines))
        st = "italic" if italic else "normal"
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs}" font-weight="{weight}" font-style="{st}" '
                 f'fill="{fill}" text-anchor="{anchor}" data-max="{maxw:.0f}">{ts}</text>')
        return len(lines) * lh

    def badge(self, right_x, top_y, label="✓ RESPUESTA"):
        return  # sin etiqueta "✓ RESPUESTA": la respuesta se distingue solo por el color
        w = tw(label, 10, True) + 16
        self.rect(right_x - w, top_y - 10, w, 20, "#f59e0b", rx=10)
        self.text(right_x - w / 2, top_y + 4, label, 10, 700, "#ffffff", maxw=0)

    def pill(self, cx, cy, label, fill):
        w = max(32, tw(label, 11, True) + 16)
        self.rect(cx - w / 2, cy - 10, w, 20, fill, rx=10)
        self.text(cx, cy + 4, label, 11, 700, "#ffffff", maxw=0)


def block_h(title, lines, w, tfs=13.5, bfs=12, pad=18):
    """Alto de una tarjeta con título + cuerpo envuelto a lo ancho w."""
    tl = wrap(title, w - 28, tfs, True) if title else []
    bl = []
    for l in lines:
        bl += wrap(l, w - 28, bfs)
    h = pad + len(tl) * tfs * 1.42 + (6 if tl and bl else 0) + len(bl) * 17 + pad - 4
    return h, tl, bl


def draw_block(s, x, y, w, h, title, lines, style="plain", tfs=13.5, bfs=12, align="middle", accent=None):
    """style: plain | answer | dashed | soft | accent."""
    fills = {
        "plain": ("#ffffff", LINE, INK, SLATE, None),
        "answer": (TEAL, TEAL, "#ffffff", "#ecfeff", None),
        "dashed": ("#ffffff", BORDER, "#334155", MUTED, "6 4"),
        "soft": (TEAL_L, TEAL_B, INK, SLATE, None),
        "warn": ("#fff1f2", "#fda4af", "#9f1239", "#881337", None),
    }
    fill, stroke, tc, bc, dash = fills[style]
    s.rect(x, y, w, h, fill, stroke, 1.8 if style == "soft" else 1.5, dash=dash)
    if accent:
        s.rect(x + 1, y + 1, 6, h - 2, accent, rx=3)
    _, tl, bl = block_h(title, lines, w, tfs, bfs)
    content = len(tl) * tfs * 1.42 + (6 if tl and bl else 0) + len(bl) * 17
    cy = y + (h - content) / 2 + tfs * 0.95
    tx = x + w / 2 if align == "middle" else x + 18 + (6 if accent else 0)
    mw = w - 28
    if tl:
        s.text(tx, cy, tl, tfs, 700, tc, align, mw)
        cy += len(tl) * tfs * 1.42 + 6
    if bl:
        s.text(tx, cy - 1.5, bl, bfs, 400, bc, align, mw, lh=17)


# ---------------------------------------------------------------- partes comunes

def header(s, titulo_barra, esp):
    lines = wrap(titulo_barra, 540, 11.5, True)
    hh = 56 if len(lines) == 1 else 68
    s.rect(16, 16, 968, hh, TEAL)
    mid = 16 + hh / 2
    s.add(f'<text x="36" y="{mid+7:.1f}" font-size="20" font-weight="800" fill="#ffffff">MedQuiz<tspan fill="#5eead4">Plus</tspan></text>')
    s.line(170, mid - 10, 170, mid + 10, "#5eead4", 1.5)
    s.text(184, mid + 4 - (len(lines) - 1) * 8, lines, 11.5, 700, "#ffffff", "start", 542, lh=16)
    # La etiqueta va junto al título: la esquina derecha la tapa la barra de zoom del visor.
    w = tw(esp, 10, True) + 22
    x = 184 + max(tw(l, 11.5, True) for l in lines) + 18
    if len(lines) == 1 and x + w <= 780:
        s.rect(x, mid - 12, w, 24, TEAL_D, rx=12)
        s.text(x + w / 2, mid + 4, esp, 10, 700, "#99f6e4", maxw=w - 16)
    return 16 + hh + 18


def case_box(s, y, caso, sub):
    tl = wrap(caso, 592, 14.5, True)
    sl = wrap(sub, 592, 12)
    h = 28 + len(tl) * 19 + len(sl) * 17 + 10
    s.rect(190, y, 620, h, "#ffffff", BORDER)
    s.text(500, y + 28.5, tl, 14.5, 700, INK, maxw=592, lh=19)
    s.text(500, y + 28.5 + len(tl) * 19 + 3.5, sl, 12, 400, TEAL, maxw=592, lh=17)
    return y + h


def perlas(s, y, items, fuente):
    bl = []
    for it in items:
        ls = wrap("• " + it, 884, 12)
        bl += [ls[0]] + ["   " + l for l in ls[1:]]
    fl = wrap("Fuente: " + fuente, 884, 10.5)
    h = 28 + 22 + len(bl) * 18 + len(fl) * 15 + 12
    s.rect(40, y, 920, h, "#fffbeb", "#fbbf24")
    s.text(58, y + 28, "PUNTOS CLAVE ENAM:", 12, 800, "#b45309", "start", 884)
    s.text(58, y + 50, bl, 12, 500, "#92400e", "start", 884, lh=18)
    s.text(58, y + 50 + len(bl) * 18 + 4, fl, 10.5, 400, "#a16207", "start", 884, lh=15, italic=True)
    return y + h


# ---------------------------------------------------------------- 8 diseños

def hexagon(s, y, pregunta, x1=180, x2=820):
    ql = wrap(pregunta, (x2 - x1) - 150, 13.5, True)
    h = max(70, 26 + len(ql) * 18 + 10)
    m = y + h / 2
    s.add(f'<polygon points="{x1},{m:.1f} {x1+40},{y:.1f} {x2-40},{y:.1f} {x2},{m:.1f} {x2-40},{y+h:.1f} {x1+40},{y+h:.1f}" '
          f'fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>')
    s.circle(x1 + 62, m, 13, "#f59e0b")
    s.text(x1 + 62, m + 5.5, "?", 16, 800, "#ffffff")
    cx = (x1 + 90 + x2 - 40) / 2
    s.text(cx, m + 5 - (len(ql) - 1) * 9, ql, 13.5, 700, "#78350f", maxw=(x2 - x1) - 150, lh=18)
    return y + h


def branches(s, y, top_from, left, right, ans, lx=270, rx=730, w=400, lab=("SÍ", "NO")):
    """Dibuja la bifurcación desde top_from (y del borde inferior del nodo) hacia dos cajas."""
    s.line(500, top_from, 500, y + 22)
    s.line(lx, y + 22, rx, y + 22)
    s.arrow_down(lx, y + 22, y + 62)
    s.arrow_down(rx, y + 22, y + 62)
    s.pill(lx, y + 40, lab[0], "#059669")
    s.pill(rx, y + 40, lab[1], "#e11d48")
    by = y + 62
    hl = block_h(left[0], left[1], w)[0]
    hr = block_h(right[0], right[1], w)[0]
    h = max(hl, hr, 90)
    draw_block(s, lx - w / 2, by, w, h, left[0], left[1], "answer" if ans == "si" else "dashed")
    draw_block(s, rx - w / 2, by, w, h, right[0], right[1], "answer" if ans == "no" else "dashed")
    if ans in ("si", "no"):
        bx = (lx if ans == "si" else rx) + w / 2 - 8
        s.badge(bx, by)
    return by + h


def lay_decision(s, y, d):
    s.arrow_down(500, y, y + 26)
    y2 = hexagon(s, y + 26, d["pregunta"])
    return branches(s, y2, y2, d["si"], d["no"], d["ans"])


def lay_double(s, y, d):
    s.arrow_down(500, y, y + 26)
    y1 = y + 26
    # Primera pregunta a la izquierda-centro, salida lateral a la derecha
    ybot = hexagon(s, y1, d["q1"], 120, 640)
    mid = (y1 + ybot) / 2
    ex = d["exit"]
    w = 290
    h = max(block_h(ex[0], ex[1], w)[0], 80)
    bx, byy = 670, mid - h / 2
    s.arrow_right(640, bx, mid)
    s.pill(655, mid - 14, d.get("exit_label", "NO"), d.get("exit_color", "#e11d48"))
    draw_block(s, bx, byy, w, h, ex[0], ex[1], "answer" if d["ans"] == "exit" else "dashed")
    if d["ans"] == "exit":
        s.badge(bx + w - 8, byy)
    # Segunda pregunta
    s.arrow_down(380, ybot, ybot + 40)
    s.pill(380, ybot + 18, d.get("q1_label", "SÍ"), d.get("q1_color", "#059669"))
    y2 = max(ybot + 40, byy + h + 16)
    if y2 > ybot + 40:
        s.line(380, ybot + 40, 380, y2)
    ybot2 = hexagon(s, y2, d["q2"])
    return branches(s, ybot2, ybot2, d["si"], d["no"], d["ans"])


def _branches_from(s, y, x0, left, right, ans):
    lx, rx, w = 230, 690, 400
    s.line(x0, y, x0, y + 22)
    s.line(lx, y + 22, rx, y + 22)
    s.arrow_down(lx, y + 22, y + 62)
    s.arrow_down(rx, y + 22, y + 62)
    s.pill(lx, y + 40, "SÍ", "#059669")
    s.pill(rx, y + 40, "NO", "#e11d48")
    by = y + 62
    h = max(block_h(left[0], left[1], w)[0], block_h(right[0], right[1], w)[0], 90)
    draw_block(s, lx - w / 2, by, w, h, left[0], left[1], "answer" if ans == "si" else "dashed")
    draw_block(s, rx - w / 2, by, w, h, right[0], right[1], "answer" if ans == "no" else "dashed")
    if ans in ("si", "no"):
        s.badge((lx if ans == "si" else rx) + w / 2 - 8, by)
    return by + h


def lay_hub(s, y, d):
    cards = d["cards"]
    cw, gap = 270, 22
    hs = [max(block_h(c[0], c[1], cw)[0], 92) for c in cards]
    r1, r2 = max(hs[0], hs[1]), max(hs[2], hs[3])
    top = y + 28
    rows = [(top, r1), (top + r1 + gap, r2)]
    ch = max(block_h(d["centro"][0], d["centro"][1], 340)[0], 96)
    total = r1 + gap + r2
    cy = top + (total - ch) / 2
    s.arrow_down(500, y, cy)
    draw_block(s, 330, cy, 340, ch, d["centro"][0], d["centro"][1], "answer")
    s.badge(662, cy)
    pos = [(40, 0), (690, 0), (40, 1), (690, 1)]
    for i, c in enumerate(cards):
        x, r = pos[i]
        ry, rh = rows[r]
        col = ACCENTS[i % 4] if len(c) < 3 else c[2]
        my = ry + rh / 2
        my = min(max(my, cy + 18), cy + ch - 18)
        if x < 500:
            s.line(310, my, 330, my, col); s.circle(330, my, 4, col)
        else:
            s.line(690, my, 670, my, col); s.circle(670, my, 4, col)
        draw_block(s, x, ry, cw, rh, c[0], c[1], "plain", accent=col)
    return top + total


def lay_steps(s, y, d):
    steps = d["steps"]
    per = 3
    bw, gx = 292, 22
    x0 = 40
    yy = y + 26
    s.arrow_down(500, y, yy)
    rows = [steps[i:i + per] for i in range(0, len(steps), per)]
    n = 1
    for ri, row in enumerate(rows):
        h = max(max(block_h(t, b, bw - 34)[0] for t, b in row), 80)
        for ci, (t, b) in enumerate(row):
            x = x0 + ci * (bw + gx)
            s.rect(x, yy, bw, h, TEAL_L, TEAL_B, 1.8)
            s.circle(x + 22, yy + 24, 13, TEAL)
            s.text(x + 22, yy + 29, str(n), 13, 800, "#ffffff")
            tl = wrap(t, bw - 62, 13.5, True)
            bl = []
            for l in b:
                bl += wrap(l, bw - 62, 12)
            s.text(x + 48, yy + 29, tl, 13.5, 700, INK, "start", bw - 62)
            s.text(x + 48, yy + 29 + len(tl) * 19 + 3, bl, 12, 400, SLATE, "start", bw - 62, lh=17)
            if ci < len(row) - 1:
                s.arrow_right(x + bw + 2, x + bw + gx - 2, yy + h / 2)
            n += 1
        yy += h
        if ri < len(rows) - 1:
            s.arrow_down(500, yy, yy + 26)
            yy += 26
    s.arrow_down(500, yy, yy + 26)
    yy += 26
    lab, txt = d["final"]
    tl = wrap(txt, 780, 15, True)
    h = 30 + 16 + len(tl) * 21 + 6
    s.rect(80, yy, 840, h, TEAL_D, rx=10)
    s.text(500, yy + 25, lab.upper(), 11.5, 800, "#5eead4", maxw=800)
    s.text(500, yy + 50, tl, 15, 700, "#ffffff", maxw=780, lh=21)
    s.badge(912, yy)
    return yy + h


def lay_compare(s, y, d):
    cols, rows = d["cols"], d["rows"]
    n = len(cols)
    x0, W, lw = 40, 920, 170
    cw = (W - lw) / n
    yy = y + 26
    s.arrow_down(500, y, yy)
    # cabecera
    hh = max(len(wrap(c[0], cw - 20, 12.5, True)) for c in cols) * 17 + 22
    s.rect(x0, yy, W, hh, "#f1f5f9", LINE, rx=10)
    s.text(x0 + lw / 2, yy + hh / 2 + 4, d.get("corner", "Criterio"), 11, 800, MUTED, maxw=lw - 16)
    for i, (name, ans) in enumerate(cols):
        cx = x0 + lw + i * cw
        if ans:
            s.rect(cx + 3, yy + 3, cw - 6, hh - 6, TEAL, rx=8)
        ls = wrap(name, cw - 20, 12.5, True)
        s.text(cx + cw / 2, yy + hh / 2 + 4 - (len(ls) - 1) * 8.5, ls, 12.5, 700,
               "#ffffff" if ans else INK, maxw=cw - 20, lh=17)
        if ans:
            bw = tw("✓ RESPUESTA", 10, True) + 16
            rx = cx + cw - 6
            if rx - bw - 8 < 500 < rx + 8:
                rx = cx + 6 + bw
            s.badge(rx, yy)
    yy += hh
    for ri, (lab, cells) in enumerate(rows):
        wl = [wrap(c, cw - 22, 11.5) for c in cells]
        ll = wrap(lab, lw - 24, 11.5, True)
        h = max(max(len(w) for w in wl), len(ll)) * 16 + 20
        bg = "#ffffff" if ri % 2 == 0 else "#f8fafc"
        s.rect(x0, yy, W, h, bg, "#e2e8f0", 1, rx=0)
        for i in range(n):
            if cols[i][1]:
                s.rect(x0 + lw + i * cw + 3, yy, cw - 6, h, TEAL_L, "none", rx=0)
        s.text(x0 + 14, yy + h / 2 + 4 - (len(ll) - 1) * 8, ll, 11.5, 700, "#334155", "start", lw - 24, lh=16)
        for i, w in enumerate(wl):
            cx = x0 + lw + i * cw + cw / 2
            s.text(cx, yy + h / 2 + 4 - (len(w) - 1) * 8, w, 11.5, 600 if cols[i][1] else 400,
                   TEAL_D if cols[i][1] else SLATE, maxw=cw - 22, lh=16)
        yy += h
    s.rect(x0, y + 26, W, yy - y - 26, "none", LINE, 1.5, rx=10)
    return yy


def lay_ladder(s, y, d):
    lv = d["levels"]; n = len(lv); ans = d["ans"]
    gap = 16; w = (920 - gap * (n - 1)) / n
    hs = [block_h(t, b, w)[0] for t, b in lv]
    base = max(hs[i] + 18 * (n - 1 - i) for i in range(n)) + 14
    yy = y + 26
    s.arrow_down(500, y, yy)
    s.text(60, yy + 14, d.get("eje", "▲ Mayor gravedad / intensidad"), 11, 700, MUTED, "start", 500)
    top0 = yy + 28
    bottom = top0 + base
    for i, (t, b) in enumerate(lv):
        x = 40 + i * (w + gap)
        h = base - (n - 1 - i) * 18
        yt = bottom - h
        st = "answer" if i == ans else "soft"
        s.rect(x, yt, w, h, TEAL if i == ans else TEAL_L, TEAL if i == ans else TEAL_B, 1.8)
        s.rect(x, yt, w, 6, ACCENTS[i % len(ACCENTS)], rx=3)
        _, tl, bl = block_h(t, b, w)
        tc, bc = ("#ffffff", "#ecfeff") if i == ans else (INK, SLATE)
        s.text(x + w / 2, yt + 30, tl, 13.5, 700, tc, maxw=w - 28)
        s.text(x + w / 2, yt + 30 + len(tl) * 19 + 4, bl, 12, 400, bc, maxw=w - 28, lh=17)
        if i == ans:
            s.badge(x + w - 8, yt)
        if i < n - 1:
            s.arrow_right(x + w + 1, x + w + gap - 1, bottom - 24, BORDER)
    return bottom


def lay_timeline(s, y, d):
    ph = d["phases"]; n = len(ph); ans = d["ans"]
    gap = 18; w = (920 - gap * (n - 1)) / n
    yy = y + 26
    s.arrow_down(500, y, yy)
    ly = yy + 34
    s.line(40 + w / 2, ly, 40 + (n - 1) * (w + gap) + w / 2, ly, BORDER, 3)
    h = max(max(block_h(p[1], p[2], w)[0] for p in ph), 96)
    for i, (tag, t, b) in enumerate(ph):
        cx = 40 + i * (w + gap) + w / 2
        col = TEAL if i == ans else ACCENTS[i % len(ACCENTS)]
        s.circle(cx, ly, 11, "#ffffff", col, 3)
        s.circle(cx, ly, 5, col)
        tl = wrap(tag, w - 10, 11, True)
        s.text(cx, yy + 8 - (len(tl) - 1) * 14, tl, 11, 800, col, maxw=w - 10, lh=14)
        s.line(cx, ly + 11, cx, ly + 30, col, 2, "3 3")
        draw_block(s, cx - w / 2, ly + 30, w, h, t, b, "answer" if i == ans else "plain")
        if i == ans:
            s.badge(cx + w / 2 - 8, ly + 30)
    return ly + 30 + h


def lay_grid(s, y, d):
    cards = d["cards"]
    w, gx, gy = 445, 30, 20
    yy = y + 26
    s.arrow_down(500, y, yy)
    if d.get("rotulo"):
        s.text(500, yy + 16, d["rotulo"].upper(), 11.5, 800, MUTED, maxw=900)
        yy += 28
    for r in range(0, len(cards), 2):
        pair = cards[r:r + 2]
        h = max(max(block_h(c[0], c[1], w - 50)[0] for c in pair), 86)
        for i, (t, b, ok) in enumerate(pair):
            x = 40 + i * (w + gx)
            s.rect(x, yy, w, h, TEAL if ok else "#ffffff", TEAL if ok else LINE, 1.5)
            s.circle(x + 28, yy + 28, 14, "#ffffff" if ok else "#fff1f2", "none" if ok else "#fda4af", 0 if ok else 1.5)
            s.text(x + 28, yy + 33.5, "✓" if ok else "✕", 15, 800, TEAL if ok else "#e11d48")
            tl = wrap(t, w - 70, 13.5, True)
            bl = []
            for l in b:
                bl += wrap(l, w - 70, 12)
            s.text(x + 54, yy + 29, tl, 13.5, 700, "#ffffff" if ok else INK, "start", w - 70)
            s.text(x + 54, yy + 29 + len(tl) * 19 + 3, bl, 12, 400, "#ecfeff" if ok else SLATE, "start", w - 70, lh=17)
            if ok:
                s.badge(x + w - 8, yy)
        yy += h + gy
    return yy - gy


LAYOUTS = {"decision": lay_decision, "double": lay_double, "hub": lay_hub, "steps": lay_steps,
           "compare": lay_compare, "ladder": lay_ladder, "timeline": lay_timeline, "grid": lay_grid}


def build(spec):
    s = SVG()
    y = header(s, spec["barra"], spec["esp"])
    y = case_box(s, y, spec["caso"], spec["sub"])
    y = LAYOUTS[spec["tipo"]](s, y, spec["d"])
    y = perlas(s, y + 26, spec["perlas"], spec["fuente"])
    H = y + 18
    t = escape(spec["titulo"])
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H:.0f}" '
            f'viewBox="0 0 1000 {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" '
            f'aria-label="{t}"><title>{t}</title>'
            f'<rect x="0.75" y="0.75" width="998.5" height="{H-1.5:.1f}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>')
    return head + "".join(s.p) + "</svg>"
