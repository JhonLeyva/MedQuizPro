"""Tres diseños nuevos (bloque 5): embudo diagnóstico, puntaje con medidor y matriz de doble entrada.
Se suman a los 5 anteriores (árbol, radial, fases, termómetro, tarjetas)."""
from engine import SVG, wrap, tw, block_h, draw_block, header, perlas, escape, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE, ACCENTS
from engine2 import top_row, table, X0, X1, build_general
from engine3 import section, case_chip, LAYOUTS3, AMBER, AMBER_L

BAND = ["#10b981", "#f59e0b", "#f97316", "#e11d48", "#be123c"]
FUN = ["#f0fdfa", "#ccfbf1", "#99f6e4", "#5eead4", "#2dd4bf", "#14b8a6"]


# ─────────────────────────────────────────────────────────── 6. EMBUDO DIAGNÓSTICO
def _chips(s, x, y, w, items, struck):
    """Fila(s) de chips; devuelve alto usado. struck=True: descartado (gris tachado)."""
    cx, cy, rh = x, y, 26
    pos = []
    for it in items:
        cw = tw(("✕ " if struck else "") + it, 11, False) + 22
        if cx + cw > x + w and cx > x:
            cx, cy = x, cy + rh + 6
        pos.append((cx, cy, cw, it))
        cx += cw + 6
    for cx, cy, cw, it in pos:
        if struck:
            s.rect(cx, cy, cw, rh, "#f8fafc", "#e2e8f0", 1, rx=13)
            s.text(cx + cw / 2, cy + 17.5, "✕ " + it, 11, 500, "#94a3b8", maxw=0)
            s.line(cx + 22, cy + 13.5, cx + cw - 10, cy + 13.5, "#94a3b8", 1.2)
        else:
            s.rect(cx, cy, cw, rh, "#ffffff", LINE, 1.2, rx=13)
            s.text(cx + cw / 2, cy + 17.5, it, 11, 600, "#334155", maxw=0)
    return (pos[-1][1] - y + rh) if pos else 0


def _chips_h(w, items, struck):
    cx, rows = 0, 1
    for it in items:
        cw = tw(("✕ " if struck else "") + it, 11, False) + 22
        if cx + cw > w and cx > 0:
            cx, rows = 0, rows + 1
        cx += cw + 6
    return rows * 26 + (rows - 1) * 6


def embudo(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    FW, cx = 540, X0 + 270          # ancho máximo del embudo y su centro
    RX = X0 + FW + 34               # columna derecha (descartes)
    RW = X1 - RX
    s.text(RX, y + 12, "DIAGNÓSTICOS EN JUEGO", 10.5, 800, MUTED, "start", RW)
    bands = [(d["inicio"], d["candidatos"], False)] + [(p, desc, True) for p, desc in d["pasos"]]
    n = len(bands)
    wmin = 250
    widths = [FW - i * (FW - wmin) / n for i in range(n + 1)]
    yy = y + 24
    for i, (txt, chips, struck) in enumerate(bands):
        wt, wb = widths[i], widths[i + 1]
        tl = wrap(txt, wb - 44 if i == 0 else wb - 64, 12.5, True)
        ch = _chips_h(RW, chips, struck) if chips else 0
        h = max(56, len(tl) * 17 + 26, ch + 18)
        pts = f"{cx-wt/2:.1f},{yy:.1f} {cx+wt/2:.1f},{yy:.1f} {cx+wb/2:.1f},{yy+h:.1f} {cx-wb/2:.1f},{yy+h:.1f}"
        s.add(f'<polygon points="{pts}" fill="{FUN[min(i, len(FUN)-1)]}" stroke="{TEAL_B}" stroke-width="1.5"/>')
        if i == 0:
            s.text(cx, yy + 16, "SE SOSPECHA", 9.5, 800, TEAL, maxw=0)
            s.text(cx, yy + h / 2 + 10 - (len(tl) - 1) * 8.5, tl, 12.5, 800, TEAL_D, maxw=wb - 44, lh=17)
        else:
            s.circle(cx - wb / 2 + 26, yy + h / 2, 11, TEAL)
            s.text(cx - wb / 2 + 26, yy + h / 2 + 4, str(i), 11, 800, "#ffffff", maxw=0)
            s.text(cx + 10, yy + h / 2 + 4.5 - (len(tl) - 1) * 8.5, tl, 12.5, 600, INK, maxw=wb - 64, lh=17)
        if chips:
            s.line(cx + (wt + wb) / 4 + 4, yy + h / 2, RX - 8, yy + h / 2, "#cbd5e1", 1.2, "3 3")
            _chips(s, RX, yy + h / 2 - ch / 2, RW, chips, struck)
        yy += h + 4
    # salida del embudo → diagnóstico
    s.arrow_down(cx, yy, yy + 26)
    yy += 30
    t, ls = d["final"]
    fw = max(widths[-1] + 60, 340)
    fh = max(block_h(t, ls, fw, 14, 12)[0], 70)
    draw_block(s, cx - fw / 2, yy, fw, fh, t, ls, "answer", 14, 12)
    case_chip(s, cx + fw / 2 - 64, yy)
    if d.get("nota"):
        nl = wrap(d["nota"], RW - 28, 11.5)
        nh = len(nl) * 16 + 44
        s.rect(RX, yy + (fh - nh) / 2, RW, nh, AMBER_L, "#fcd34d", 1.2)
        s.text(RX + 14, yy + (fh - nh) / 2 + 20, "CLAVE DEL CASO", 10, 800, "#b45309", "start", RW - 28)
        s.text(RX + 14, yy + (fh - nh) / 2 + 38, nl, 11.5, 500, "#92400e", "start", RW - 28, lh=16)
    return yy + fh


# ─────────────────────────────────────────────────────────── 7. PUNTAJE CON MEDIDOR
def puntaje(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    LW = 540
    # tabla de criterios
    rows = []
    for crit, pts, on in d["items"]:
        cl = wrap(crit, LW - 120, 12)
        rows.append((cl, pts, on, max(34, len(cl) * 16 + 16)))
    hh = 34
    s.rect(X0, y, LW, hh, "#f1f5f9", LINE, rx=10)
    s.text(X0 + 16, y + 22, d["escala"].upper(), 11.5, 800, "#334155", "start", LW - 110)
    s.text(X0 + LW - 18, y + 22, "PUNTOS", 10.5, 800, MUTED, "end", 90)
    yy = y + hh
    for i, (cl, pts, on, h) in enumerate(rows):
        s.rect(X0, yy, LW, h, TEAL_L if on else ("#ffffff" if i % 2 == 0 else "#f8fafc"), "#e2e8f0", 1, rx=0)
        s.rect(X0 + 14, yy + h / 2 - 10, 20, 20, TEAL if on else "#ffffff", TEAL if on else "#94a3b8", 1.5, rx=5)
        if on:
            s.text(X0 + 24, yy + h / 2 + 5, "✓", 13, 800, "#ffffff", maxw=0)
        s.text(X0 + 46, yy + h / 2 + 4.5 - (len(cl) - 1) * 8, cl, 12, 700 if on else 500, TEAL_D if on else "#334155", "start", LW - 120, lh=16)
        s.text(X0 + LW - 18, yy + h / 2 + 5, str(pts), 13, 800, TEAL if on else MUTED, "end", 90)
        yy += h
    s.rect(X0, yy, LW, 40, TEAL, rx=0)
    s.text(X0 + 16, yy + 25, d.get("total_label", "Puntaje de este caso"), 12.5, 800, "#ffffff", "start", LW - 110)
    s.text(X0 + LW - 18, yy + 26, str(d["total"]), 16, 800, "#ffffff", "end", 90)
    yy += 40
    s.rect(X0, y, LW, yy - y, "none", LINE, 1.5, rx=10)
    left_bottom = yy
    # medidor
    RX = X0 + LW + 30
    RW = X1 - RX
    s.circle(RX + 54, y + 50, 46, TEAL_L, TEAL, 3)
    s.text(RX + 54, y + 50, str(d["total"]), 26, 800, TEAL_D, maxw=0)
    s.text(RX + 54, y + 70, "de " + str(d["max"]), 11, 700, MUTED, maxw=0)
    s.text(RX + 114, y + 36, "INTERPRETACIÓN", 10.5, 800, MUTED, "start", RW - 120)
    s.text(RX + 114, y + 56, wrap(d.get("interpreta", ""), RW - 120, 12.5, True), 12.5, 800, TEAL_D, "start", RW - 120, lh=17)
    by = y + 112
    for i, (rango, etiqueta, conducta, on) in enumerate(d["bandas"]):
        col = BAND[min(i, len(BAND) - 1)] if len(d["bandas"]) > 2 else BAND[i * 3]
        cl = wrap(conducta, RW - 150, 11.5)
        h = max(52, len(cl) * 15 + 34)
        s.rect(RX + 24, by, RW - 24, h, TEAL if on else "#ffffff", TEAL if on else LINE, 2 if on else 1.3, rx=10)
        s.rect(RX + 24, by, 10, h, col, rx=4)
        s.text(RX + 46, by + 22, rango, 12, 800, "#ffffff" if on else col, "start", 100)
        assert len(wrap(etiqueta, RW - 160, 12.5, True)) == 1, "etiqueta larga: " + etiqueta
        s.text(RX + 150, by + 22, wrap(etiqueta, RW - 160, 12.5, True)[0], 12.5, 800, "#ffffff" if on else INK, "start", RW - 160)
        s.text(RX + 150, by + 40, cl, 11.5, 400, "#ecfeff" if on else SLATE, "start", RW - 160, lh=15)
        if on:
            s.add(f'<polygon points="{RX+4:.1f},{by+h/2-9:.1f} {RX+4:.1f},{by+h/2+9:.1f} {RX+20:.1f},{by+h/2:.1f}" fill="{AMBER}"/>')
            case_chip(s, RX + RW - 62, by)
        by += h + 8
    return max(left_bottom, by - 8)


# ─────────────────────────────────────────────────────────── 8. MATRIZ DE DOBLE ENTRADA
def matriz(s, y, d):
    y = section(s, y + 10, d["rotulo"])
    rows, cols, cells = d["rows"], d["cols"], d["cells"]
    rc, cc = d["caso"]
    HW = 150                     # ancho de encabezados de fila
    gx0 = X0 + HW + 12
    nc = len(cols)
    gap = 12
    cw = (X1 - gx0 - gap * (nc - 1)) / nc
    # eje X
    s.text(gx0, y + 12, "→ " + d["eje_x"].upper(), 10.5, 800, TEAL, "start", X1 - gx0)
    y += 22
    chh = max(len(wrap(c, cw - 20, 12.5, True)) for c in cols) * 17 + 18
    for j, c in enumerate(cols):
        x = gx0 + j * (cw + gap)
        on = j == cc
        s.rect(x, y, cw, chh, "#e0f2f1" if on else "#f1f5f9", TEAL if on else LINE, 1.5, rx=10)
        cl = wrap(c, cw - 20, 12.5, True)
        s.text(x + cw / 2, y + chh / 2 + 4.5 - (len(cl) - 1) * 8.5, cl, 12.5, 800, TEAL_D if on else "#334155", maxw=cw - 20, lh=17)
    yl = wrap("↓ " + d["eje_y"].upper(), HW - 4, 10.5, True)
    s.text(X0, y + chh / 2 + 4 - (len(yl) - 1) * 7.5, yl, 10.5, 800, TEAL, "start", HW - 4, lh=15)
    y += chh + gap
    for i, r in enumerate(rows):
        hs = [max(block_h(t, ls, cw, 13, 11.5)[0], 76) for t, ls in cells[i]]
        rl = wrap(r, HW - 22, 12.5, True)
        h = max(max(hs), len(rl) * 17 + 20)
        on_r = i == rc
        s.rect(X0, y, HW, h, "#e0f2f1" if on_r else "#f1f5f9", TEAL if on_r else LINE, 1.5, rx=10)
        s.text(X0 + HW / 2, y + h / 2 + 4.5 - (len(rl) - 1) * 8.5, rl, 12.5, 800, TEAL_D if on_r else "#334155", maxw=HW - 22, lh=17)
        for j, (t, ls) in enumerate(cells[i]):
            x = gx0 + j * (cw + gap)
            on = (i, j) == (rc, cc)
            draw_block(s, x, y, cw, h, t, ls, "answer" if on else "plain", 13, 11.5,
                       accent=None if on else ACCENTS[(i * nc + j) % len(ACCENTS)])
            if on:
                case_chip(s, x + cw / 2, y + h)
        y += h + gap
    return y - gap + 10


LAYOUTS4 = dict(LAYOUTS3, embudo=embudo, puntaje=puntaje, matriz=matriz)


def build4(spec):
    if spec.get("tipo", "arbol") == "arbol":
        return build_general(spec)
    s = SVG()
    y = header(s, spec["barra"], spec["esp"])
    if spec["tipo"] == "radial":
        y, _ = top_row(s, y, spec["tema"], spec["caso"], "Ruta del caso: abajo del mapa")
    else:
        y, _ = top_row(s, y, spec["tema"], spec["caso"], "Marca dónde cae este caso", "rombo")
    y = LAYOUTS4[spec["tipo"]](s, y + 8, spec["d"])
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
