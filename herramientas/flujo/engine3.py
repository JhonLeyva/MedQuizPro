"""Cuatro diseños nuevos «tema general + caso»: radial, fases con curvas, termómetro + ruta y tarjetas con datos."""
import math
from engine import SVG, wrap, tw, block_h, draw_block, header, perlas, escape, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE, ACCENTS
from engine2 import top_row, table, X0, X1

AMBER, AMBER_L, ROSE = "#f59e0b", "#fffbeb", "#e11d48"


def section(s, y, label):
    s.text(X0, y + 14, label.upper(), 11.5, 800, MUTED, "start", 900)
    return y + 26


def case_chip(s, x, y, label="ESTE CASO"):
    """Etiqueta que señala dónde cae el caso (no es la etiqueta de respuesta)."""
    w = tw("◆ " + label, 10, True) + 18
    s.rect(x - w / 2, y - 11, w, 22, AMBER_L, AMBER, 1.5, rx=11)
    s.text(x, y + 4, "◆ " + label, 10, 800, "#b45309", maxw=0)


# ─────────────────────────────────────────────────────────── 1. RADIAL
def radial(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    items, ans = d["items"], d["ans"]
    n = len(items)
    cw, gap, R, cx = 300, 16, 86, 500
    left = list(range(0, (n + 1) // 2))
    right = list(range((n + 1) // 2, n))
    hs = [max(block_h(t, b, cw, 13.5, 12)[0], 84) for t, b in items]
    colh = lambda idx: sum(hs[i] for i in idx) + gap * (len(idx) - 1)
    H = max(colh(left), colh(right), 2 * R + 40)
    pos = {}
    for col, idx, x in ((0, left, X0), (1, right, X1 - cw)):
        yy = y + (H - colh(idx)) / 2
        for i in idx:
            pos[i] = (x, yy)
            yy += hs[i] + gap
    cy = y + H / 2
    for on in (False, True):
        for i in range(n):
            if (i == ans) != on:
                continue
            x, yy = pos[i]
            tx = x + cw if x < cx else x
            ty = yy + hs[i] / 2
            ang = math.atan2(ty - cy, tx - cx)
            sx, sy = cx + (R + 8) * math.cos(ang), cy + (R + 8) * math.sin(ang)
            s.line(sx, sy, tx, ty, TEAL if on else "#cbd5e1", 3 if on else 2)
            s.circle(tx, ty, 5, TEAL if on else "#cbd5e1")
    s.circle(cx, cy, R + 8, TEAL_L, TEAL_B, 2)
    s.circle(cx, cy, R, "#ffffff", TEAL, 3)
    cl = wrap(d["centro"], 2 * R - 30, 14, True)
    s.text(cx, cy + 5 - (len(cl) - 1) * 9.5, cl, 14, 800, TEAL_D, maxw=2 * R - 30, lh=19)
    if d.get("centro_sub"):
        s.text(cx, cy + 5 + (len(cl) + 1) * 9.5, d["centro_sub"], 10.5, 600, MUTED, maxw=2 * R - 20)
    for i, (t, b) in enumerate(items):
        x, yy = pos[i]
        acc = ACCENTS[i % len(ACCENTS)]
        draw_block(s, x, yy, cw, hs[i], t, b, "answer" if i == ans else "plain", 13.5, 12, accent=None if i == ans else acc)
        if i == ans:
            case_chip(s, x + cw / 2, yy + hs[i] + 1)
    y = section(s, y + H + 22, "Cómo llega el caso al diagnóstico")
    return chips_route(s, y, d["ruta"])


def chips_route(s, y, pasos):
    n = len(pasos)
    gap = 34
    w = (X1 - X0 - gap * (n - 1)) / n
    h = max(len(wrap(p, w - 24, 12, i == n - 1)) for i, p in enumerate(pasos)) * 17 + 24
    for i, p in enumerate(pasos):
        x = X0 + i * (w + gap)
        last = i == n - 1
        s.rect(x, y, w, h, TEAL if last else "#f8fafc", TEAL if last else LINE, 1.5, rx=12)
        ls = wrap(p, w - 24, 12, last)
        s.text(x + w / 2, y + h / 2 + 4 - (len(ls) - 1) * 8.5, ls, 12, 700 if last else 500, "#ffffff" if last else "#334155", maxw=w - 24, lh=17)
        if i < n - 1:
            s.arrow_right(x + w + 4, x + w + gap - 4, y + h / 2, TEAL)
    return y + h


# ─────────────────────────────────────────────────────────── 2. FASES CON CURVAS
def fases(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    ph, ans = d["fases"], d["ans"]
    n = len(ph)
    W = X1 - X0
    colw = W / n
    if not d.get("curvas"):
        # sin curvas no hay gráfico: franja compacta (fase, tiempo y «este caso») sin recuadros vacíos
        for i, (tag, dias, _, _) in enumerate(ph):
            x = X0 + i * colw
            on = i == ans
            s.rect(x + 2, y + 10, colw - 4, 56, TEAL_L if on else "#f8fafc", TEAL if on else "#e2e8f0", 2 if on else 1, rx=10)
            s.text(x + colw / 2, y + 35, tag.upper(), 12, 800, TEAL_D if on else "#334155", maxw=colw - 20)
            s.text(x + colw / 2, y + 54, dias, 11, 600, MUTED, maxw=colw - 20)
        case_chip(s, X0 + ans * colw + colw / 2, y + 10)
        ty = y + 80
        hs = [max(block_h(t, b, colw - 16, 13.5, 12)[0], 90) for _, _, t, b in ph]
        h = max(hs)
        for i, (_, _, t, b) in enumerate(ph):
            draw_block(s, X0 + i * colw + 8, ty, colw - 16, h, t, b, "answer" if i == ans else "plain")
        y = ty + h
        if d.get("chips"):
            y = section(s, y + 24, d["chips_titulo"])
            y = chip_grid(s, y, d["chips"])
        return y
    gh = 172                                  # alto del gráfico
    gy = y + 58
    # franjas de fase
    for i, (tag, dias, _, _) in enumerate(ph):
        x = X0 + i * colw
        on = i == ans
        s.rect(x + 2, y, colw - 4, gh + 44, TEAL_L if on else "#f8fafc", TEAL if on else "#e2e8f0", 2 if on else 1, rx=10)
        s.text(x + colw / 2, y + 18, tag.upper(), 12, 800, TEAL_D if on else "#334155", maxw=colw - 20)
        s.text(x + colw / 2, y + gh + 36, dias, 11, 600, MUTED, maxw=colw - 20)
    # curvas: lista de (nombre, color, valores normalizados 0..1 por punto)
    for name, col, vals in d.get("curvas", []):
        k = len(vals)
        pts = [(X0 + 20 + j * (W - 40) / (k - 1), gy + gh - 40 - v * (gh - 70)) for j, v in enumerate(vals)]
        path = "M " + " L ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
        s.add(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    # leyenda
    lx = X0 + 18
    ancho = sum(40 + tw(nm, 10.5, True) for nm, _, _ in d.get("curvas", []))
    apilar = ancho > colw - 20          # si no cabe en la primera franja, una leyenda debajo de otra
    ly = y + 40 - (8 if apilar else 0)
    for name, col, _ in d.get("curvas", []):
        s.line(lx, ly, lx + 22, ly, col, 3)
        s.text(lx + 28, ly + 4, name, 10.5, 700, col, "start", colw - 70 if apilar else 200)
        if apilar:
            ly += 16
        else:
            lx += 40 + tw(name, 10.5, True)
    # marcador del caso
    mx = X0 + ans * colw + colw / 2
    s.line(mx, y + (ly - y + 8 if apilar and ans == 0 else 52), mx, y + gh + 20, AMBER, 2, "5 4")   # bajo el título y la leyenda
    case_chip(s, mx, y + gh + 14)
    # tarjetas por fase
    ty = y + gh + 58
    hs = [max(block_h(t, b, colw - 16, 13.5, 12)[0], 90) for _, _, t, b in ph]
    h = max(hs)
    for i, (_, _, t, b) in enumerate(ph):
        draw_block(s, X0 + i * colw + 8, ty, colw - 16, h, t, b, "answer" if i == ans else "plain")
    y = ty + h
    if d.get("chips"):
        y = section(s, y + 24, d["chips_titulo"])
        y = chip_grid(s, y, d["chips"])
    return y


def chip_grid(s, y, chips):
    x = X0
    rowh = 30
    for label, on in chips:
        w = tw(label, 11.5, on) + 30
        if x + w > X1:
            x = X0
            y += rowh + 8
        s.rect(x, y, w, rowh, TEAL if on else "#ffffff", TEAL if on else LINE, 1.5, rx=15)
        s.text(x + w / 2, y + 19.5, ("✓ " if on else "") + label, 11.5, 700 if on else 500, "#ffffff" if on else SLATE, maxw=0)
        x += w + 8
    return y + rowh


# ─────────────────────────────────────────────────────────── 3. TERMÓMETRO + RUTA
def termometro(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    lv, caso = d["niveles"], d["caso_nivel"]
    # termómetro a la izquierda
    tx, tw_, top = X0 + 30, 34, y + 10
    H = 330
    s.rect(tx, top, tw_, H, "#f1f5f9", LINE, 1.5, rx=17)
    cols = ["#10b981", "#f59e0b", "#f97316", "#e11d48"]
    seg = H / len(lv)
    for i, (rango, titulo, lines) in enumerate(lv):
        yy = top + H - (i + 1) * seg
        s.rect(tx + 5, yy + 4, tw_ - 10, seg - 8, cols[i % 4], rx=8)
        on = i == caso
        bx = tx + tw_ + 26
        bw = 330
        bh = seg - 10
        s.line(tx + tw_, yy + seg / 2, bx, yy + seg / 2, cols[i % 4] if not on else TEAL, 2 if not on else 3)
        s.rect(bx, yy + 5, bw, bh, TEAL if on else "#ffffff", TEAL if on else LINE, 1.5 if not on else 2, rx=10)
        s.text(bx + 14, yy + 27, rango, 12, 800, "#ffffff" if on else cols[i % 4], "start", 92)
        s.text(bx + 110, yy + 27, wrap(titulo, bw - 124, 12.5, True), 12.5, 700, "#ffffff" if on else INK, "start", bw - 124, lh=16)
        bl = []
        for l in lines:
            bl += wrap(l, bw - 28, 11.5)
        s.text(bx + 14, yy + 48, bl[:3], 11.5, 400, "#ecfeff" if on else SLATE, "start", bw - 28, lh=15)
        if on:
            case_chip(s, bx + bw - 60, yy + 5)
    # ruta de manejo a la derecha
    rx = X0 + 430
    rw = X1 - rx
    s.text(rx, y + 14, d["ruta_titulo"].upper(), 11.5, 800, MUTED, "start", rw)
    yy = y + 28
    for i, (paso, titulo, lines, on) in enumerate(d["pasos"]):
        h = max(block_h(titulo, lines, rw - 60, 13.5, 12)[0], 84)
        s.rect(rx, yy, rw, h, TEAL if on else TEAL_L, TEAL if on else TEAL_B, 2 if on else 1.5, rx=12)
        s.circle(rx + 28, yy + h / 2, 17, "#ffffff" if on else TEAL)
        s.text(rx + 28, yy + h / 2 + 5, str(paso), 15, 800, TEAL if on else "#ffffff")
        tl = wrap(titulo, rw - 76, 13.5, True)
        bl = []
        for l in lines:
            bl += wrap(l, rw - 76, 12)
        ch = len(tl) * 19 + 4 + len(bl) * 17
        ty = yy + (h - ch) / 2 + 13
        s.text(rx + 58, ty, tl, 13.5, 700, "#ffffff" if on else INK, "start", rw - 76)
        s.text(rx + 58, ty + len(tl) * 19 + 4, bl, 12, 400, "#ecfeff" if on else SLATE, "start", rw - 76, lh=17)
        if on:
            case_chip(s, rx + rw - 70, yy, d.get("paso_label", "ESTE CASO"))
        yy += h
        if i < len(d["pasos"]) - 1:
            s.arrow_down(rx + 28, yy + 2, yy + 22)
            yy += 24
    return max(top + H, yy)


# ─────────────────────────────────────────────────────────── 4. TARJETAS CON DATOS
def tarjetas(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    cards, ans = d["cards"], d["ans"]
    n = len(cards)
    per = 2 if n == 4 else 3
    gap = 20
    w = (X1 - X0 - gap * (per - 1)) / per
    rows = [cards[i:i + per] for i in range(0, n, per)]
    for ri, row in enumerate(rows):
        hs = []
        for c in row:
            tl = wrap(c["titulo"], w - 40, 14, True)
            # alto justo: título, datos, pie y 16 px de margen (antes sobraba aire abajo)
            hs.append(56 + len(tl) * 19 + len(c["datos"]) * 30 + len(wrap(c["pie"], w - 40, 11.5)) * 16)
        h = max(hs)
        for ci, c in enumerate(row):
            idx = ri * per + ci
            on = idx == ans
            x = X0 + ci * (w + gap)
            s.rect(x, y, w, h, "#ffffff", TEAL if on else LINE, 3 if on else 1.5, rx=14)
            s.rect(x, y, w, 8, TEAL if on else ACCENTS[idx % len(ACCENTS)], rx=4)
            tl = wrap(c["titulo"], w - 40, 14, True)
            s.text(x + 20, y + 34, tl, 14, 800, TEAL_D if on else INK, "start", w - 40, lh=19)
            yy = y + 34 + len(tl) * 19 + 2
            for lab, val, hit in c["datos"]:
                s.rect(x + 16, yy, w - 32, 26, TEAL_L if hit else "#f8fafc", TEAL if hit else "#e2e8f0", 1.5 if hit else 1, rx=8)
                s.text(x + 28, yy + 17.5, lab, 11, 700, MUTED, "start", 120)
                s.text(x + w - 28, yy + 17.5, ("✓ " if hit else "") + val, 11.5, 800 if hit else 600, TEAL_D if hit else "#334155", "end", w - 160)
                yy += 30
            pl = wrap(c["pie"], w - 40, 11.5)
            s.text(x + 20, yy + 16, pl, 11.5, 600, TEAL if on else SLATE, "start", w - 40, lh=16)
            if on:
                case_chip(s, x + w - 72, y + 4)
        y += h + gap
    s.text(X0, y + 2, "✓ = dato que coincide con el caso", 10.5, 600, MUTED, "start", 400)
    return y + 8


LAYOUTS3 = {"radial": radial, "fases": fases, "termometro": termometro, "tarjetas": tarjetas}


def build3(spec):
    s = SVG()
    y = header(s, spec["barra"], spec["esp"])
    if spec["tipo"] == "radial":
        y, _ = top_row(s, y, spec["tema"], spec["caso"], "Ruta del caso: abajo del mapa")
    else:
        y, _ = top_row(s, y, spec["tema"], spec["caso"], "Marca dónde cae este caso", "rombo")
    y = LAYOUTS3[spec["tipo"]](s, y + 8, spec["d"])
    if spec.get("tabla"):
        y = table(s, y + 28, spec["tabla"])
    y = perlas(s, y + 24, spec["perlas"], spec["fuente"])
    H = y + 18
    t = escape(spec["titulo"])
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H:.0f}" '
            f'viewBox="0 0 1000 {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" '
            f'aria-label="{t}"><title>{t}</title>'
            f'<rect x="0.75" y="0.75" width="998.5" height="{H-1.5:.1f}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>')
    return head + "".join(s.p) + "</svg>"
