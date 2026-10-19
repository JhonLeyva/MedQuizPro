"""Constructor único de los 20 diseños (bloque ENAM 2026) + diseños 15-18.
15 ciclo/mecanismo · 16 lista de criterios · 17 balanza · 18 red de atención.
Los 8 diseños antiguos llevan una franja «imagen del caso» (dibujo o foto real con marcas)."""
import math
from engine import SVG, wrap, tw, header, perlas, escape, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE, ACCENTS
from engine2 import top_row, table, X0, X1, tree_from_root
from engine3 import section, case_chip, LAYOUTS3, AMBER, AMBER_L
from engine4 import LAYOUTS4
from engine5 import LAYOUTS5, panel, ORANGE, GREEN, GREEN_L, RED, RED_L
import engine6
from engine6 import LAYOUTS6, foto, credito, card6, fila_cards
from engine8 import escala

VIEJOS = {"arbol", "radial", "fases", "termometro", "tarjetas", "embudo", "puntaje", "matriz"}


# ════════════════════════════════════════════════════════════ IMAGEN (dibujo o foto)
def imagen(s, x, y, im):
    """Dibuja im en (x, y) y devuelve (ancho, alto). im: {"ilu": f(s,x,y), "W", "H"} o
    {"foto": archivo, "W", "H", "marcas", "credito"}."""
    # data-box: el verificador comprueba que nada de la imagen (marcas, rótulos) se salga de su recuadro.
    s.add(f'<g data-box="{x:.1f} {y:.1f} {im["W"]:.1f} {im["H"]:.1f}">')
    if im.get("foto"):
        foto(s, x, y, im["W"], im["H"], im["foto"], im.get("marcas", ()), im.get("fondo", "#000000"))
    else:
        im["ilu"](s, x, y)
    s.add('</g>')
    return im["W"], im["H"]


def _img_h(im, w):
    """Alto total de un bloque imagen + crédito (si es foto)."""
    return im["H"] + (18 if im.get("credito") else 0)


def _img_draw(s, x, y, im):
    imagen(s, x, y, im)
    if im.get("credito"):
        credito(s, x, y + im["H"] + 13, im["W"], im["credito"])


# ════════════════════════════════════════════════════════════ FRANJA «IMAGEN DEL CASO»
AVISOS = []      # huecos detectados al construir (build27 los trata como error)


def _nota(n, w):
    """Una nota es texto o (título, detalle). Devuelve (líneas del título, líneas del detalle)."""
    if isinstance(n, (tuple, list)):
        t, d = n
        return wrap(t, w, 13, True), (wrap(d, w, 12.5) if d else [])
    return [], wrap(n, w, 13)


def _nota_alto(tl, dl):
    return len(tl) * 18 + len(dl) * 17 + (4 if tl and dl else 0)


def banda(s, y, b):
    """Imagen a la izquierda y notas numeradas a la derecha (qué se ve y por qué importa).
    Sin espacio vacío: la foto se ajusta al alto de las notas y las notas se reparten todo el alto."""
    y = section(s, y + 6, b.get("rotulo", "Así se ve en este caso"))
    GAP = 8

    tit = b["titulo"].upper()

    def medir(im):
        # el panel nunca es más angosto que su título ni que el crédito (si no, se salen)
        cred = wrap(im.get("credito", ""), 430, 9.5) if im.get("credito") else []
        PW = max(im["W"] + 28, tw(tit, 10, True) + 48, (max(tw(c, 9.5) for c in cred) + 30) if cred else 0)
        x = X0 + PW + 20
        w = X1 - x
        cu = [_nota(n, w - 60) for n in b["notas"]]
        nat = [max(44, _nota_alto(tl, dl) + 26) for tl, dl in cu]
        nh = sum(nat) + GAP * (len(nat) - 1)
        pie_l = wrap(b["pie"], PW - 28, 11) if b.get("pie") else []
        PH = 38 + im["H"] + len(cred) * 13 + (5 if cred else 0) + (8 + len(pie_l) * 15 if pie_l else 0) + 14
        return PW, x, w, cu, nat, nh, pie_l, PH, cred

    im = b["img"]
    PW, x, w, cu, nat, nh, pie_l, PH, cred = medir(im)
    if im.get("foto"):
        # La foto crece o se achica (sin deformarse) para acompañar el alto de las notas.
        obj = nh / 0.72 if nh < 0.72 * PH else max(nh, PH)
        k = (obj - (PH - im["H"])) / im["H"]
        k = max(0.8, min(k, 1.35, 430 / im["W"]))   # nunca tan chica que no se lea
        if abs(k - 1) > 0.03:
            im = {**im, "W": im["W"] * k, "H": im["H"] * k}
            PW, x, w, cu, nat, nh, pie_l, PH, cred = medir(im)
    H = max(PH, nh)
    if nh < 0.6 * H or PH < 0.6 * H:
        AVISOS.append(f"franja con hueco: notas {nh:.0f}px, imagen {PH:.0f}px, alto {H:.0f}px")
    # panel de la imagen (centrado en vertical si las notas son más altas)
    s.rect(X0, y, PW, H, "#ffffff", LINE, 1.5, rx=12)
    s.rect(X0 + 12, y + 10, min(tw(tit, 10, True) + 18, PW - 24), 20, TEAL_L, TEAL_B, 1, rx=10)
    s.text(X0 + 21, y + 24, tit, 10, 800, TEAL, "start", PW - 42)
    off = (H - PH) / 2
    iy = y + 38 + off
    imagen(s, X0 + (PW - im["W"]) / 2, iy, im)
    iy += im["H"]
    if cred:
        s.text(X0 + 14, iy + 14, cred, 9.5, 500, MUTED, "start", PW - 28, lh=13, italic=True)
        iy += len(cred) * 13 + 5
    if pie_l:
        s.text(X0 + 14, iy + 18, pie_l, 11, 600, SLATE, "start", PW - 28, lh=15)
    # notas: se reparten el alto completo, con el contenido centrado
    extra = (H - nh) / len(nat)
    cy = y
    for i, ((tl, dl), h0) in enumerate(zip(cu, nat)):
        h = h0 + extra
        on = i == b.get("ans", -1)
        s.rect(x, cy, w, h, TEAL_L if on else "#f8fafc", TEAL if on else LINE, 1.8 if on else 1.2, rx=10)
        s.circle(x + 22, cy + h / 2, 11, ORANGE if b.get("numeros", True) else TEAL)
        s.text(x + 22, cy + h / 2 + 4, str(i + 1), 11.5, 800, "#ffffff", maxw=0)
        top = cy + (h - _nota_alto(tl, dl)) / 2
        if tl:
            s.text(x + 44, top + 13.5, tl, 13, 800, TEAL_D if on else INK, "start", w - 60, lh=18)
        if dl:
            s.text(x + 44, top + (len(tl) * 18 + 4 if tl else 0) + 13, dl, 12.5, 600 if (on and not tl) else 400,
                   TEAL_D if (on and not tl) else "#334155", "start", w - 60, lh=17)
        cy += h + GAP
    return y + H


# ════════════════════════════════════════════════════════════ TRÍADAS / TÉTRADAS / PÉNTADAS
def triada(s, y, t):
    """Signos epónimos oficiales (Charcot, Beck, Cushing, Fallot...) contrastados con el caso.
    t: {"rotulo", "items": [(signo, dato del caso, presente)], "grupos": [(nombre, desde, hasta)], "nota"}.
    Cada grupo es un corchete sobre las tarjetas desde..hasta (índices desde 0, inclusive)."""
    y = section(s, y + 6, t.get("rotulo", "Signos con nombre propio"))
    items, grupos = t["items"], t.get("grupos", [])
    n = len(items)
    PAD, GAP = 16, 12
    cw = (X1 - X0 - 2 * PAD - GAP * (n - 1)) / n
    xs = [X0 + PAD + i * (cw + GAP) for i in range(n)]
    # niveles de corchete: los grupos más cortos van más abajo (más cerca de las tarjetas)
    orden = sorted(range(len(grupos)), key=lambda g: grupos[g][2] - grupos[g][1])
    LV = 40
    top = y + 22 + LV * len(grupos)
    cuerpos = []
    for i, (signo, dato, pres) in enumerate(items):
        nl = wrap(signo, cw - 46, 12.5, True)
        dl = wrap(dato, cw - 24, 11.5)
        cuerpos.append((nl, dl, pres))
    # pres None = componente anatómico (p. ej. Fallot): sin marca «en el caso»
    estado = any(p is not None for _, _, p in items)
    ch = max(14 + max(len(nl) * 17, 22) + 6 + len(dl) * 16 + 12 + (34 if estado else 0) for nl, dl, _ in cuerpos)
    nota = wrap(t["nota"], X1 - X0 - 2 * PAD, 12) if t.get("nota") else []
    H = (top - y) + ch + (14 + len(nota) * 17 if nota else 0) + 16
    s.rect(X0, y, X1 - X0, H, "#ffffff", LINE, 1.5, rx=12)
    for k, g in enumerate(orden):
        nombre, a, b = grupos[g]
        gy = top - 20 - LV * k          # el rótulo del corchete queda 8 px por encima de las tarjetas
        xa, xb = xs[a] + 6, xs[b] + cw - 6
        pres = sum(1 for i in range(a, b + 1) if items[i][2])
        tot = b - a + 1
        if not estado:
            pres = tot
        col = TEAL if pres == tot else MUTED
        s.line(xa, gy, xb, gy, col, 2)
        s.line(xa, gy, xa, gy + 8, col, 2)
        s.line(xb, gy, xb, gy + 8, col, 2)
        lab = f"{nombre.upper()} · {pres} de {tot} en el caso" if estado else nombre.upper()
        lw = tw(lab, 10.5, True) + 22
        lx = (xa + xb) / 2
        lx = min(max(lx, X0 + 10 + lw / 2), X1 - 10 - lw / 2)   # un grupo de una sola tarjeta: el rótulo no sale del recuadro
        s.rect(lx - lw / 2, gy - 12, lw, 24, TEAL_L if pres == tot else "#f1f5f9", col, 1.4, rx=12)
        s.text(lx, gy + 4, lab, 10.5, 800, TEAL_D if pres == tot else SLATE, maxw=lw - 14)
    for i, (nl, dl, pres) in enumerate(cuerpos):
        x = xs[i]
        if not estado:
            pres = True
        s.rect(x, top, cw, ch, "#f0fdfa" if pres else "#f8fafc", TEAL if pres else LINE, 1.6 if pres else 1.2, rx=10)
        s.circle(x + 20, top + 23, 10, ORANGE if pres else "#94a3b8")
        s.text(x + 20, top + 27, str(i + 1), 11, 800, "#ffffff", maxw=0)
        hn = max(len(nl) * 17, 22)
        s.text(x + 38, top + 28 - (0 if len(nl) > 1 else 0), nl, 12.5, 800, TEAL_D if pres else SLATE, "start", cw - 46, lh=17)
        s.text(x + 12, top + 14 + hn + 6 + 12, dl, 11.5, 400, "#334155" if pres else MUTED, "start", cw - 24, lh=16)
        if estado:
            etq = "✓ EN EL CASO" if pres else "— NO DESCRITO"
            s.rect(x + 12, top + ch - 12 - 22, cw - 24, 22, GREEN_L if pres else "#e2e8f0", GREEN if pres else "#cbd5e1", 1, rx=11)
            s.text(x + cw / 2, top + ch - 12 - 7, etq, 10.5, 800, "#15803d" if pres else SLATE, maxw=cw - 36)
    if nota:
        s.text(X0 + PAD, top + ch + 14 + 13, nota, 12, 600, TEAL_D, "start", X1 - X0 - 2 * PAD, lh=17)
    return y + H


# ════════════════════════════════════════════════════════════ DISEÑO 15: CICLO / MECANISMO
def ciclo(s, y, d):
    """Imagen a la izquierda; a la derecha, los pasos del mecanismo en círculo con el paso del caso."""
    y = section(s, y + 10, d["rotulo"])
    im = d["img"]
    PW = im["W"] + 28
    pie_l = wrap(d.get("img_pie", ""), PW - 28, 11) if d.get("img_pie") else []
    PH = 40 + _img_h(im, im["W"]) + 10 + len(pie_l) * 15 + 12
    x0 = X0 + PW + 16
    W = X1 - x0
    pasos = d["pasos"]
    n = len(pasos)
    bw = min(176, W / 2 - 20)
    cx = x0 + W / 2
    hs = []
    for t, l in pasos:
        tl = wrap(t, bw - 20, 12, True)
        bl = wrap(l, bw - 20, 10.5) if l else []
        hs.append((tl, bl, 14 + len(tl) * 16 + len(bl) * 14 + 10))
    hmax = max(h for _, _, h in hs)
    Rx = (W - bw) / 2 - 4
    Ry = max(120, hmax * 1.05 + 40 if n > 4 else hmax + 30)
    CH = 2 * Ry + hmax + 20
    cy = y + hmax / 2 + Ry + 10
    H = max(PH, CH + 10)
    # panel imagen
    panel(s, X0, y, PW, H, d["img_titulo"])
    _img_draw(s, X0 + 14, y + 38, im)
    if pie_l:
        s.text(X0 + 14, y + 38 + _img_h(im, 0) + 16, pie_l, 11, 600, SLATE, "start", PW - 28, lh=15)
    # anillo
    s.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{Rx:.1f}" ry="{Ry:.1f}" fill="none" stroke="{TEAL_B}" stroke-width="3" stroke-dasharray="2 6" stroke-linecap="round"/>')
    ang = [-math.pi / 2 + 2 * math.pi * i / n for i in range(n)]
    pos = [(cx + Rx * math.cos(a), cy + Ry * math.sin(a)) for a in ang]
    # flechas a lo largo del anillo, entre nodos
    for i in range(n):
        a0, a1 = ang[i], ang[i] + 2 * math.pi / n
        am = (a0 + a1) / 2
        px, py = cx + Rx * math.cos(am), cy + Ry * math.sin(am)
        tx, ty = -Rx * math.sin(am), Ry * math.cos(am)
        L = math.hypot(tx, ty)
        tx, ty = tx / L, ty / L
        s.add(f'<polygon points="{px+tx*9:.1f},{py+ty*9:.1f} {px-tx*6-ty*7:.1f},{py-ty*6+tx*7:.1f} {px-tx*6+ty*7:.1f},{py-ty*6-tx*7:.1f}" fill="{TEAL}"/>')
    if d.get("centro"):
        cw_ = max(90, 2 * Rx - bw - 16)
        cl = wrap(d["centro"], cw_, 12.5, True)
        s.text(cx, cy + 4 - (len(cl) - 1) * 8.5, cl, 12.5, 800, MUTED, maxw=cw_, lh=17)
    for i, ((tl, bl, h), (px, py)) in enumerate(zip(hs, pos)):
        on = i == d.get("ans", -1)
        bx, by = px - bw / 2, py - h / 2
        s.rect(bx, by, bw, h, ORANGE if on else "#ffffff", ORANGE if on else TEAL_B, 2, rx=10)
        s.circle(bx + 2, by + 2, 11, TEAL_D if not on else "#7c2d12")
        s.text(bx + 2, by + 6, str(i + 1), 11, 800, "#ffffff", maxw=0)
        s.text(px, by + 22, tl, 12, 800, "#ffffff" if on else INK, maxw=bw - 20, lh=16)
        if bl:
            s.text(px, by + 22 + len(tl) * 16, bl, 10.5, 500, "#fff7ed" if on else SLATE, maxw=bw - 20, lh=14)
        if on:
            case_chip(s, px, by + h, d.get("tag", "ESTE CASO"))
    y += H
    if d.get("claves"):
        y = fila_cards(s, y + 20, d["claves"], d.get("tag"), d.get("claves_titulo"))
    return y


# ════════════════════════════════════════════════════════════ DISEÑO 16: LISTA DE CRITERIOS
def criterios(s, y, d):
    """Lista de criterios con los que cumple el caso, conteo contra el umbral y la imagen del caso."""
    y = section(s, y + 10, d["rotulo"])
    im = d["img"]
    PW = im["W"] + 28
    LW = X1 - X0 - PW - 20
    # cabecera
    s.rect(X0, y, LW, 34, "#f1f5f9", LINE, rx=10)
    s.text(X0 + 16, y + 22, d["lista_titulo"].upper(), 11.5, 800, "#334155", "start", LW - 130)
    s.text(X0 + LW - 16, y + 22, "EN EL CASO", 10.5, 800, MUTED, "end", 100)
    yy = y + 34
    ok_n = 0
    for i, (txt, cumple, det) in enumerate(d["items"]):
        tl = wrap(txt, LW - 150, 12, cumple is True)
        dl = wrap(det, LW - 150, 10.5) if det else []
        h = max(38, len(tl) * 16 + len(dl) * 14 + 16)
        fill = TEAL_L if cumple is True else ("#ffffff" if i % 2 == 0 else "#f8fafc")
        s.rect(X0, yy, LW, h, fill, "#e2e8f0", 1, rx=0)
        box = TEAL if cumple is True else ("#ffffff" if cumple is False else "#f1f5f9")
        s.rect(X0 + 14, yy + 10, 20, 20, box, TEAL if cumple is True else "#94a3b8", 1.5, rx=5)
        s.text(X0 + 24, yy + 25, "✓" if cumple is True else ("✕" if cumple is False else "?"), 12, 800,
               "#ffffff" if cumple is True else "#94a3b8", maxw=0)
        s.text(X0 + 46, yy + 24, tl, 12, 700 if cumple is True else 500, TEAL_D if cumple is True else "#334155", "start", LW - 150, lh=16)
        if dl:
            s.text(X0 + 46, yy + 24 + len(tl) * 16, dl, 10.5, 500, MUTED, "start", LW - 150, lh=14)
        lab = "Sí" if cumple is True else ("No" if cumple is False else "Sin dato")
        s.text(X0 + LW - 16, yy + 24, lab, 12, 800, TEAL if cumple is True else MUTED, "end", 90)
        ok_n += cumple is True
        yy += h
    # conteo / veredicto
    vl = wrap(d["veredicto"], LW - 32, 12.5, True)
    vh = 30 + len(vl) * 17 + 10
    s.rect(X0, yy, LW, vh, TEAL, rx=0)
    s.text(X0 + 16, yy + 22, d.get("conteo", f"Cumple {ok_n} de {len(d['items'])}") + " · " + d["umbral"], 11, 800, "#99f6e4", "start", LW - 32)
    s.text(X0 + 16, yy + 42, vl, 12.5, 800, "#ffffff", "start", LW - 32, lh=17)
    yy += vh
    s.rect(X0, y, LW, yy - y, "none", LINE, 1.5, rx=10)
    # imagen
    px = X1 - PW
    pie_l = wrap(d.get("img_pie", ""), PW - 28, 11) if d.get("img_pie") else []
    PH = 40 + _img_h(im, 0) + 10 + len(pie_l) * 15 + 12
    panel(s, px, y, PW, PH, d["img_titulo"])
    _img_draw(s, px + 14, y + 38, im)
    if pie_l:
        s.text(px + 14, y + 38 + _img_h(im, 0) + 16, pie_l, 11, 600, SLATE, "start", PW - 28, lh=15)
    y = max(yy, y + PH)
    if d.get("claves"):
        y = fila_cards(s, y + 20, d["claves"], d.get("tag"), d.get("claves_titulo"))
    return y


# ════════════════════════════════════════════════════════════ DISEÑO 17: BALANZA
def balanza(s, y, d):
    """Balanza dibujada: dos platillos con los argumentos; se inclina hacia lo que pesa en el caso."""
    y = section(s, y + 10, d["rotulo"])
    W = X1 - X0
    cx = X0 + W / 2
    gana = d["gana"]              # "izq" o "der"
    tilt = -9 if gana == "izq" else 9
    # columnas de argumentos
    colw = 290
    def col_h(c):
        return 44 + sum(len(wrap(t, colw - 44, 11.5)) * 16 + 10 for t in c["items"]) + 10
    hL, hR = col_h(d["izq"]), col_h(d["der"])
    top = y + 20
    # dibujo de la balanza (centro)
    bx, by = cx, top + 30
    L = 116
    dy = L * math.sin(math.radians(tilt))
    dx = L * math.cos(math.radians(tilt))
    s.add(f'<rect x="{cx-7:.1f}" y="{by:.1f}" width="14" height="190" rx="5" fill="#64748b"/>'
          f'<path d="M{cx-60:.1f} {by+205:.1f} H{cx+60:.1f} L{cx+40:.1f} {by+185:.1f} H{cx-40:.1f} Z" fill="#475569"/>'
          f'<circle cx="{cx:.1f}" cy="{by:.1f}" r="15" fill="{AMBER}" stroke="#92400e" stroke-width="2"/>'
          f'<line x1="{cx-dx:.1f}" y1="{by-dy:.1f}" x2="{cx+dx:.1f}" y2="{by+dy:.1f}" stroke="#334155" stroke-width="7" stroke-linecap="round"/>')
    for sx, sy, lado in ((cx - dx, by - dy, "izq"), (cx + dx, by + dy, "der")):
        on = lado == gana
        col = ORANGE if on else "#64748b"
        s.add(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{sx-28:.1f}" y2="{sy+62:.1f}" stroke="#64748b" stroke-width="2"/>'
              f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{sx+28:.1f}" y2="{sy+62:.1f}" stroke="#64748b" stroke-width="2"/>'
              f'<path d="M{sx-38:.1f} {sy+62:.1f} H{sx+38:.1f} Q{sx:.1f} {sy+106:.1f} {sx-38:.1f} {sy+62:.1f} Z" fill="{col}"/>')
        s.text(sx, sy + 77, d[lado]["peso"], 10.5, 800, "#ffffff", maxw=66)
    s.text(cx, by + 232, d.get("pregunta", ""), 12, 800, "#334155", maxw=W - 2 * colw - 40)
    # columnas
    for lado, x in (("izq", X0), ("der", X1 - colw)):
        c = d[lado]
        on = lado == gana
        h = col_h(c)
        s.rect(x, top, colw, h, TEAL_L if on else "#ffffff", TEAL if on else LINE, 2.2 if on else 1.5, rx=12)
        s.text(x + 18, top + 28, c["titulo"], 13, 800, TEAL_D if on else INK, "start", colw - 36)
        yy = top + 46
        for t in c["items"]:
            tl = wrap(t, colw - 44, 11.5)
            s.circle(x + 22, yy + 7, 4, TEAL if on else "#94a3b8")
            s.text(x + 34, yy + 11, tl, 11.5, 500, "#334155", "start", colw - 44, lh=16)
            yy += len(tl) * 16 + 10
        if on:
            case_chip(s, x + colw - 70, top, d.get("tag", "ESTE CASO"))
    y = max(top + max(hL, hR), by + 250) + 16
    t, ls = d["veredicto"]
    tl = wrap(t, W - 60, 14, True)
    bl = []
    for l in ls:
        bl += wrap(l, W - 60, 12)
    h = 26 + len(tl) * 19 + len(bl) * 17 + 14
    s.rect(X0, y, W, h, TEAL_D, rx=12)
    s.text(cx, y + 28, tl, 14, 800, "#ffffff", maxw=W - 60, lh=19)
    s.text(cx, y + 28 + len(tl) * 19 + 2, bl, 12, 500, "#ccfbf1", maxw=W - 60, lh=17)
    return y + h


# ════════════════════════════════════════════════════════════ DISEÑO 18: RED DE ATENCIÓN
NIVELES = [("I-1", "Puesto de salud", "Técnico o profesional no médico"),
           ("I-2", "Puesto con médico", "Consulta médica general"),
           ("I-3", "Centro de salud", "Médicos, laboratorio básico, sin internamiento"),
           ("I-4", "Centro con internamiento", "Parto, internamiento corto, algunas especialidades"),
           ("II-1", "Hospital I", "Medicina, cirugía, pediatría, gineco-obstetricia"),
           ("II-2", "Hospital II", "Más especialidades, UCI"),
           ("III-1", "Hospital III", "Alta especialización"),
           ("III-2", "Instituto especializado", "Investigación y máxima complejidad")]


def red(s, y, d):
    """Pirámide de niveles de atención con el nivel del caso y, si aplica, la referencia."""
    y = section(s, y + 10, d["rotulo"])
    niv = d.get("niveles", NIVELES)
    n = len(niv)
    rh, gap = 44, 6
    PWmax = 560
    top = y + 8
    idx = {c: i for i, (c, _, _) in enumerate(niv)}
    caso = idx[d["caso"]]
    dest = idx.get(d.get("destino", ""), None)
    cxp = X0 + PWmax / 2
    for k, (cod, nom, desc) in enumerate(reversed(niv)):
        i = n - 1 - k
        yy = top + k * (rh + gap)
        w = 200 + (PWmax - 200) * (k + 1) / n
        on = i == caso
        de = i == dest
        fill = ORANGE if on else (TEAL if de else ["#ccfbf1", "#99f6e4", "#5eead4"][min(2, i // 3)])
        s.rect(cxp - w / 2, yy, w, rh, fill, "#ffffff", 2, rx=8)
        s.text(cxp - w / 2 + 12, yy + 27, cod, 13, 800, "#ffffff" if (on or de) else TEAL_D, "start", 60)
        s.text(cxp - w / 2 + 66, yy + 20, nom, 11.5, 800, "#ffffff" if (on or de) else INK, "start", w - 80)
        s.text(cxp - w / 2 + 66, yy + 35, desc, 10, 500, "#ffffff" if (on or de) else SLATE, "start", w - 80)
        if on:
            case_chip(s, cxp + w / 2 - 50, yy, d.get("tag", "ESTE CASO"))
    base = top + n * (rh + gap)
    s.text(cxp, base + 14, "▲ más complejidad · ▼ más cerca de la comunidad", 10.5, 700, MUTED, maxw=PWmax)
    if dest is not None and dest != caso:
        ky, kd = top + (n - 1 - caso) * (rh + gap) + rh / 2, top + (n - 1 - dest) * (rh + gap) + rh / 2
        xa = cxp + PWmax / 2 + 14
        s.add(f'<path d="M{xa-30:.1f} {ky:.1f} H{xa:.1f} V{kd:.1f} H{xa-30:.1f}" fill="none" stroke="{ORANGE}" stroke-width="3"/>')
        s.add(f'<polygon points="{xa-30:.1f},{kd-7:.1f} {xa-30:.1f},{kd+7:.1f} {xa-42:.1f},{kd:.1f}" fill="{ORANGE}"/>')
        s.text(xa + 8, (ky + kd) / 2 + 4, d.get("flecha", "Referir"), 11.5, 800, ORANGE, "start", 120)
    # columna derecha: tarjetas
    x = X0 + PWmax + 150 if dest is not None else X0 + PWmax + 30
    w = X1 - x
    cy = top
    for i, (t, ls, on) in enumerate(d["claves"]):
        h = card6(s, x, cy, w, t, ls, on=on, color=AMBER if on else TEAL, fs=11)
        cy += h + 10
    return max(base + 20, cy)


LAYOUTS7 = {"ciclo": ciclo, "criterios": criterios, "balanza": balanza, "red": red}


# ════════════════════════════════════════════════════════════ CONSTRUCTOR ÚNICO
def build7(spec):
    engine6._n[0] = 0
    s = SVG()
    tipo = spec.get("tipo", "arbol")
    y = header(s, spec["barra"], spec["esp"])
    if tipo == "arbol":
        bottom, tcx = top_row(s, y, spec["tema"], spec["caso"])
        y = tree_from_root(s, spec["arbol"], bottom, tcx)
    else:
        if tipo == "radial":
            y, _ = top_row(s, y, spec["tema"], spec["caso"], "Ruta del caso: abajo del mapa")
        else:
            y, _ = top_row(s, y, spec["tema"], spec["caso"], "Marca dónde cae este caso", "rombo")
        from engine9 import LAYOUTS9
        L = {**LAYOUTS4, **LAYOUTS5, **LAYOUTS6, **LAYOUTS7, **LAYOUTS9}
        y = L[tipo](s, y + 8, spec["d"])
    if spec.get("escala"):
        y = escala(s, y + 20, spec["escala"])
    if spec.get("banda"):
        y = banda(s, y + 20, spec["banda"])
    if spec.get("triada"):
        y = triada(s, y + 20, spec["triada"])
    if spec.get("tabla"):
        y = table(s, y + 26, spec["tabla"])
    y = perlas(s, y + 24, spec["perlas"], spec["fuente"])
    H = y + 18
    t = escape(spec["titulo"])
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H:.0f}" '
            f'viewBox="0 0 1000 {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" '
            f'aria-label="{t}"><title>{t}</title>'
            f'<rect x="0.75" y="0.75" width="998.5" height="{H-1.5:.1f}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>')
    return head + "".join(s.p) + "</svg>"
