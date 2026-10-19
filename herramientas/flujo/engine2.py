"""Diseño «tema general + ruta del caso»: árbol diagnóstico completo del tema con el camino
del paciente resaltado en verde, más tabla de diferencial y puntos clave."""
from engine import (SVG, wrap, tw, block_h, draw_block, header, perlas, escape,
                    TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE, BORDER)

X0, X1 = 40, 960
GREY = "#94a3b8"
LEVEL_GAP = 66          # espacio entre niveles (incluye la etiqueta de la rama)
TFS, BFS = 13, 11.5


def _leaves(n):
    return [n] if not n.get("children") else [l for c in n["children"] for l in _leaves(c)]


def _layout(root):
    """Asigna x, ancho y nivel a cada nodo (árbol ordenado: hojas en columnas iguales)."""
    leaves = _leaves(root)
    k, gap = len(leaves), 14
    lw = (X1 - X0 - gap * (k - 1)) / k
    for i, l in enumerate(leaves):
        l["cx"], l["w"] = X0 + i * (lw + gap) + lw / 2, lw

    def walk(n, depth):
        n["depth"] = depth
        for c in n.get("children", []):
            walk(c, depth + 1)
        if n.get("children"):
            cs = n["children"]
            n["cx"] = sum(c["cx"] for c in cs) / len(cs)
            span = (cs[-1]["cx"] + cs[-1]["w"] / 2) - (cs[0]["cx"] - cs[0]["w"] / 2)
            n["w"] = min(max(span, 300 if n["kind"] == "q" else 260), 520 if n["kind"] == "q" else 560)
            n["cx"] = min(max(n["cx"], X0 + n["w"] / 2), X1 - n["w"] / 2)
    walk(root, 0)


def _nodes(n):
    yield n
    for c in n.get("children", []):
        yield from _nodes(c)


def _height(n):
    if n["kind"] == "q":
        ql = wrap(n["title"], n["w"] - 110, 13, True)
        return max(58, 22 + len(ql) * 17 + 14)
    return max(block_h(n["title"], n.get("lines", []), n["w"], TFS, BFS)[0], 70)


def _draw_q(s, n, y, h):
    x1, x2 = n["cx"] - n["w"] / 2, n["cx"] + n["w"] / 2
    m = y + h / 2
    border = TEAL if n.get("path") else "#f59e0b"
    s.add(f'<polygon points="{x1:.1f},{m:.1f} {x1+26:.1f},{y:.1f} {x2-26:.1f},{y:.1f} {x2:.1f},{m:.1f} {x2-26:.1f},{y+h:.1f} {x1+26:.1f},{y+h:.1f}" '
          f'fill="#fffbeb" stroke="{border}" stroke-width="{2.5 if n.get("path") else 2}"/>')
    s.circle(x1 + 46, m, 12, "#f59e0b")
    s.text(x1 + 46, m + 5, "?", 15, 800, "#ffffff")
    ql = wrap(n["title"], n["w"] - 110, 13, True)
    cx = (x1 + 64 + x2 - 26) / 2
    s.text(cx, m + 4.5 - (len(ql) - 1) * 8.5, ql, 13, 700, "#78350f", maxw=n["w"] - 110, lh=17)


def _draw_box(s, n, y, h):
    x = n["cx"] - n["w"] / 2
    if n.get("answer") or (n.get("path") and not n.get("children")):
        style = "answer"                 # diagnóstico al que llega el caso
    elif n.get("path"):
        style = "soft"                   # nodo intermedio de la ruta
    else:
        style = "plain"
    draw_block(s, x, y, n["w"], h, n["title"], n.get("lines", []), style, TFS, BFS)
    if style == "soft":
        s.rect(x, y, n["w"], h, "none", TEAL, 2.2)


def _edge_pill(s, cx, cy, label, on):
    w = tw(label, 10, True) + 14
    s.rect(cx - w / 2, cy - 9, w, 18, TEAL if on else "#e2e8f0", rx=9)
    s.text(cx, cy + 3.5, label, 10, 700, "#ffffff" if on else "#334155", maxw=0)
    return w


def top_row(s, y, tema, caso, leyenda="Ruta de este caso en el algoritmo", simbolo="linea"):
    """Fila superior: TEMA GENERAL (izquierda) y CASO CLÍNICO (derecha)."""
    tw_, cw = 560, 340
    tl = wrap(tema["title"], tw_ - 36, 15, True)
    tb = []
    for l in tema["lines"]:
        tb += wrap(l, tw_ - 36, 12)
    cl = wrap(caso["title"], cw - 36, 12.5, True)
    cb = []
    for l in caso["lines"]:
        cb += wrap(l, cw - 36, 11.5)
    h = max(40 + len(tl) * 20 + 6 + len(tb) * 17 + 14, 40 + len(cl) * 17 + 6 + len(cb) * 16 + 40)
    # tema
    s.rect(X0, y, tw_, h, "#ffffff", TEAL, 2)
    s.rect(X0 + 16, y + 12, tw(("TEMA GENERAL"), 10, True) + 16, 18, TEAL_L, TEAL_B, 1, rx=9)
    s.text(X0 + 24, y + 25, "TEMA GENERAL", 10, 800, TEAL, "start", 0)
    s.text(X0 + 18, y + 54, tl, 15, 800, TEAL_D, "start", tw_ - 36, lh=20)
    s.text(X0 + 18, y + 54 + len(tl) * 20 + 4, tb, 12, 400, SLATE, "start", tw_ - 36, lh=17)
    # caso
    cx0 = X1 - cw
    s.rect(cx0, y, cw, h, "#f8fafc", LINE, 1.5)
    s.rect(cx0 + 1, y + 1, 6, h - 2, "#f59e0b", rx=3)
    s.text(cx0 + 20, y + 25, "CASO CLÍNICO", 10, 800, "#b45309", "start", 0)
    s.text(cx0 + 20, y + 48, cl, 12.5, 700, INK, "start", cw - 36, lh=17)
    s.text(cx0 + 20, y + 48 + len(cl) * 17 + 4, cb, 11.5, 400, SLATE, "start", cw - 36, lh=16)
    ly = y + h - 16
    if simbolo == "linea":
        s.line(cx0 + 20, ly - 4, cx0 + 50, ly - 4, TEAL, 3)
    else:
        s.rect(cx0 + 20, ly - 13, 30, 18, "#fffbeb", "#f59e0b", 1.5, rx=9)
        s.text(cx0 + 35, ly, "◆", 10, 800, "#b45309")
    s.text(cx0 + 58, ly, leyenda, 10.5, 700, TEAL, "start", cw - 80)
    return y + h, X0 + tw_ / 2


def table(s, y, d):
    """Tabla de diferencial rápido (sin flecha), con la columna del caso resaltada."""
    s.text(X0, y + 14, d["titulo"].upper(), 11.5, 800, MUTED, "start", 900)
    y += 24
    cols, rows = d["cols"], d["rows"]
    n = len(cols)
    W, lw = X1 - X0, 170
    cw = (W - lw) / n
    hh = max(len(wrap(c[0], cw - 20, 12.5, True)) for c in cols) * 17 + 20
    s.rect(X0, y, W, hh, "#f1f5f9", LINE, rx=10)
    s.text(X0 + lw / 2, y + hh / 2 + 4, d.get("corner", "Criterio"), 11, 800, MUTED, maxw=lw - 16)
    for i, (name, on) in enumerate(cols):
        cx = X0 + lw + i * cw
        if on:
            s.rect(cx + 3, y + 3, cw - 6, hh - 6, TEAL, rx=8)
        ls = wrap(name, cw - 20, 12.5, True)
        s.text(cx + cw / 2, y + hh / 2 + 4 - (len(ls) - 1) * 8.5, ls, 12.5, 700, "#ffffff" if on else INK, maxw=cw - 20, lh=17)
    top = y
    y += hh
    for ri, (lab, cells) in enumerate(rows):
        wl = [wrap(c, cw - 22, 11.5) for c in cells]
        ll = wrap(lab, lw - 24, 11.5, True)
        h = max(max(len(w) for w in wl), len(ll)) * 16 + 18
        s.rect(X0, y, W, h, "#ffffff" if ri % 2 == 0 else "#f8fafc", "#e2e8f0", 1, rx=0)
        for i in range(n):
            if cols[i][1]:
                s.rect(X0 + lw + i * cw + 3, y, cw - 6, h, TEAL_L, "none", rx=0)
        s.text(X0 + 14, y + h / 2 + 4 - (len(ll) - 1) * 8, ll, 11.5, 700, "#334155", "start", lw - 24, lh=16)
        for i, w in enumerate(wl):
            s.text(X0 + lw + i * cw + cw / 2, y + h / 2 + 4 - (len(w) - 1) * 8, w, 11.5,
                   600 if cols[i][1] else 400, TEAL_D if cols[i][1] else SLATE, maxw=cw - 22, lh=16)
        y += h
    s.rect(X0, top, W, y - top, "none", LINE, 1.5, rx=10)
    return y


def build_general(spec):
    s = SVG()
    y = header(s, spec["barra"], spec["esp"])
    bottom, tcx = top_row(s, y, spec["tema"], spec["caso"])
    end = tree_from_root(s, spec["arbol"], bottom, tcx)
    y = table(s, end + 30, spec["tabla"])
    y = perlas(s, y + 24, spec["perlas"], spec["fuente"])
    H = y + 18
    t = escape(spec["titulo"])
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H:.0f}" '
            f'viewBox="0 0 1000 {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" '
            f'aria-label="{t}"><title>{t}</title>'
            f'<rect x="0.75" y="0.75" width="998.5" height="{H-1.5:.1f}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>')
    return head + "".join(s.p) + "</svg>"


def tree_from_root(s, root, root_bottom, root_cx):
    """El nivel 0 es la caja TEMA (ya dibujada); se dibujan los niveles 1..n debajo."""
    _layout(root)
    root["cx"] = root_cx
    nodes = [n for n in _nodes(root)]
    depth = max(n["depth"] for n in nodes)
    lv_h = {d: max(_height(n) for n in nodes if n["depth"] == d) for d in range(1, depth + 1)}
    lv_y = {0: root_bottom}
    cur = root_bottom + LEVEL_GAP
    for d in range(1, depth + 1):
        lv_y[d] = cur
        cur += lv_h[d] + LEVEL_GAP

    def bottom_of(n):
        if n["depth"] == 0:
            return root_bottom
        return lv_y[n["depth"]] + (_height(n) if n["kind"] == "q" else lv_h[n["depth"]])

    for on_pass in (False, True):
        for n in nodes:
            cs = n.get("children", [])
            if not cs:
                continue
            targets = [c for c in cs if c.get("path")] if on_pass else cs
            if not targets:
                continue
            col, sw = (TEAL, 3) if on_pass else (GREY, 2)
            pb, top = bottom_of(n), lv_y[n["depth"] + 1]
            mid = top - 36
            s.line(n["cx"], pb, n["cx"], mid, col, sw)
            xs = [c["cx"] for c in targets] + [n["cx"]]
            if max(xs) - min(xs) > 0.5:
                s.line(min(xs), mid, max(xs), mid, col, sw)
            for c in targets:
                s.line(c["cx"], mid, c["cx"], top - 7, col, sw)
                s.add(f'<polygon points="{c["cx"]-5:.1f},{top-8:.1f} {c["cx"]+5:.1f},{top-8:.1f} {c["cx"]:.1f},{top:.1f}" fill="{col}"/>')
    for n in nodes:
        for c in n.get("children", []):
            if c.get("edge"):
                pw = _edge_pill(s, c["cx"], lv_y[c["depth"]] - 18, c["edge"], bool(c.get("path")))
                assert pw <= c["w"] + 30, f"etiqueta demasiado larga: {c['edge']} ({pw:.0f} > {c['w']:.0f})"
    for n in nodes:
        if n["depth"] == 0:
            continue
        if n["kind"] == "q":
            _draw_q(s, n, lv_y[n["depth"]], _height(n))
        else:
            _draw_box(s, n, lv_y[n["depth"]], lv_h[n["depth"]])
    return cur - LEVEL_GAP
