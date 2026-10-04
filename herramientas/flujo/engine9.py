"""Diseños 21-50 (Entrega 3: más variedad de flujogramas). Se dibujan con engine7.build7 (tipo = nombre del diseño).
Hechos:
 21 lectura   · lectura guiada de una imagen real: pines numerados sobre la imagen + pasos de lectura + tira comparativa
 22 zonas     · mapa de zonas concéntricas (diana) con la zona del caso + escalones con foto a la derecha
 23 regla     · reglas de umbrales (valor del caso sobre bandas de color: normal → grave)
 24 decision  · tabla de decisión de dos entradas con el paso previo común y la celda del caso
Catálogo completo (25-50 por hacer) en CATALOGO."""
import math
from engine import wrap, tw, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE
from engine2 import X0, X1
from engine3 import section, case_chip, AMBER, AMBER_L
from engine5 import panel, ORANGE, ORANGE_L, GREEN, GREEN_L, RED, RED_L
import engine6
from engine6 import foto, credito, fila_cards, DARK

CATALOGO = [
    (1, "arbol", "Árbol de decisión"), (2, "radial", "Mapa radial"), (3, "fases", "Fases con curva"),
    (4, "termometro", "Termómetro de gravedad"), (5, "tarjetas", "Tarjetas comparativas"), (6, "embudo", "Embudo diagnóstico"),
    (7, "puntaje", "Puntaje"), (8, "matriz", "Matriz 2 ejes"), (9, "calculo", "Cálculo paso a paso"),
    (10, "anatomia", "Mapa anatómico"), (11, "semaforo", "Semáforo"), (12, "cronologia", "Cronología"),
    (13, "comparador", "Comparador de imágenes"), (14, "escalera", "Escalera terapéutica"), (15, "ciclo", "Ciclo / mecanismo"),
    (16, "criterios", "Lista de criterios"), (17, "balanza", "Balanza"), (18, "red", "Red de atención (niveles)"),
    (19, "mapa_signos", "Mapa corporal de signos"), (20, "arbol_imagen", "Árbol con imagen"),
    (21, "lectura", "Lectura guiada de imagen"), (22, "zonas", "Mapa de zonas (diana)"), (23, "regla", "Regla de umbrales"),
    (24, "decision", "Tabla de decisión 2 entradas"),
    (25, "reloj", "Reloj de urgencia (acciones por minuto)"), (26, "carriles", "Algoritmo en carriles por servicio"),
    (27, "cuadricula", "Cuadrícula 2×2 de diferenciales con foto"), (28, "capas", "Corte por capas con la lesión"),
    (29, "grafica", "Gráfica clínica con el punto del caso"), (30, "piramide", "Pirámide de prioridades"),
    (31, "venn", "Diagrama de Venn de síndromes"), (32, "laboratorio", "Panel de laboratorio interpretado"),
    (33, "gasometria", "Gasometría paso a paso"), (34, "calendario", "Calendario de dosis o controles"),
    (35, "dermatomas", "Dermatomas y territorios nerviosos"), (36, "genealogia", "Árbol genealógico"),
    (37, "farmaco", "Ruta del fármaco en la célula"), (38, "antes_despues", "Antes y después del tratamiento"),
    (39, "checklist", "Lista de verificación"), (40, "alarma", "Signos de alarma"),
    (41, "dosis", "Dosis por peso"), (42, "transmision", "Cadena de transmisión"),
    (43, "pruebas", "Tabla 2×2 de pruebas diagnósticas"), (44, "linea_vida", "Línea de vida: tamizajes por edad"),
    (45, "triptico", "Tríptico de imágenes"), (46, "grados_foto", "Grados con foto real"),
    (47, "cascada", "Cascada fisiopatológica"), (48, "ecg_mapa", "ECG: derivaciones y territorio"),
    (49, "dos_preguntas", "Dos preguntas encadenadas"), (50, "monitor", "Monitor de signos vitales del caso"),
]
HECHOS = {"lectura", "zonas", "regla", "decision", "cuadricula", "alarma", "cascada", "checklist", "monitor",
          "piramide", "grados_foto", "laboratorio", "reloj", "transmision", "dosis", "ecg_mapa", "grafica"}


def _img_h(im):
    return im["H"] + (18 if im.get("credito") else 0)


def _img(s, x, y, im):
    """Imagen (foto o dibujo) con su recuadro de verificación y crédito debajo."""
    from engine7 import imagen
    imagen(s, x, y, im)
    if im.get("credito"):
        credito(s, x, y + im["H"] + 13, im["W"], im["credito"])


def _pin(s, x, y, w, h, fx, fy, n, color=ORANGE):
    """Marca numerada sobre la imagen (va dentro de su recuadro de verificación)."""
    cx, cy = x + fx * w, y + fy * h
    s.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="14" fill="{DARK}" opacity="0.45"/>')
    s.circle(cx, cy, 12, color, "#ffffff", 2)
    s.text(cx, cy + 4.5, str(n), 12, 800, "#ffffff", maxw=0)


engine6.MARCAS["pin"] = _pin


def _nota_h(t, d, w):
    tl = wrap(t, w, 12.5, True)
    dl = wrap(d, w, 11.5) if d else []
    return tl, dl, len(tl) * 17 + len(dl) * 16 + (3 if dl else 0)


# ════════════════════════════════════════════════════════════ 21 LECTURA GUIADA DE IMAGEN
def lectura(s, y, d):
    """Imagen grande con pines numerados; a la derecha, qué mirar en orden (el paso del caso resaltado);
    abajo, una tira con imágenes de los otros grados para comparar y el veredicto."""
    y = section(s, y + 10, d["rotulo"])
    im = dict(d["img"])
    pines = d.get("pines", [])
    im["marcas"] = list(im.get("marcas", [])) + [("pin", fx, fy, i + 1) for i, (fx, fy) in enumerate(pines)]
    PW = im["W"] + 28
    pie_l = wrap(d.get("img_pie", ""), PW - 28, 11) if d.get("img_pie") else []
    PH = 40 + _img_h(im) + (8 + len(pie_l) * 15 if pie_l else 0) + 12
    x = X0 + PW + 18
    w = X1 - x
    pasos = d["pasos"]
    med = [_nota_h(t, dd, w - 62) for t, dd, _ in pasos]
    nat = [h + 24 for _, _, h in med]
    GAP = 8
    nh = sum(nat) + GAP * (len(nat) - 1)
    H = max(PH, nh)
    panel(s, X0, y, PW, H, d["img_titulo"])
    iy = y + 38 + (H - PH) / 2
    _img(s, X0 + 14, iy, im)
    if pie_l:
        s.text(X0 + 14, iy + _img_h(im) + 16, pie_l, 11, 600, SLATE, "start", PW - 28, lh=15)
    extra = (H - nh) / len(nat)
    cy = y
    for i, ((t, dd, on), (tl, dl, th), h0) in enumerate(zip(pasos, med, nat)):
        h = h0 + extra
        s.rect(x, cy, w, h, TEAL_L if on else "#f8fafc", TEAL if on else LINE, 2 if on else 1.2, rx=10)
        s.circle(x + 24, cy + h / 2, 12, ORANGE if i < len(pines) else TEAL)
        s.text(x + 24, cy + h / 2 + 4.5, str(i + 1), 12, 800, "#ffffff", maxw=0)
        top = cy + (h - th) / 2
        s.text(x + 46, top + 13, tl, 12.5, 800, TEAL_D if on else INK, "start", w - 62, lh=17)
        if dl:
            s.text(x + 46, top + 13 + len(tl) * 17 + 3, dl, 11.5, 400, "#334155", "start", w - 62, lh=16)
        if on:
            case_chip(s, x + w - tw("◆ ESTE CASO", 10, True) / 2 - 20, cy, d.get("tag", "ESTE CASO"))
        cy += h + GAP
    y += H
    if d.get("tira"):
        y = _tira(s, y + 22, d["tira"], d.get("tira_titulo", "Compara"), d.get("tira_credito"))
    if d.get("veredicto"):
        t, dd = d["veredicto"]
        tl = wrap(t, X1 - X0 - 40, 13.5, True)
        dl = wrap(dd, X1 - X0 - 40, 12) if dd else []
        h = 22 + len(tl) * 19 + len(dl) * 17 + 14
        y += 18
        s.rect(X0, y, X1 - X0, h, TEAL_D, rx=12)
        s.text(X0 + 20, y + 26, tl, 13.5, 800, "#ffffff", "start", X1 - X0 - 40, lh=19)
        if dl:
            s.text(X0 + 20, y + 26 + len(tl) * 19, dl, 12, 500, "#ccfbf1", "start", X1 - X0 - 40, lh=17)
        y += h
    return y


def _tira(s, y, items, titulo, cred=None):
    """Fila de imágenes del mismo alto con su rótulo; la del caso con borde naranja."""
    s.text(X0, y + 12, titulo.upper(), 11, 800, MUTED, "start", 900)
    y += 24
    n, gap = len(items), 14
    cw = (X1 - X0 - gap * (n - 1)) / n
    IH = d_ih = min(170, max(110, cw * 0.62))
    labs = []
    for im, t, sub, on in items:
        tl = wrap(t, cw - 24, 12.5, True)
        sl = wrap(sub, cw - 24, 11) if sub else []
        labs.append((tl, sl))
    lh = max(len(tl) * 17 + len(sl) * 15 for tl, sl in labs)
    CH = 12 + IH + 10 + lh + 12
    for i, ((im, t, sub, on), (tl, sl)) in enumerate(zip(items, labs)):
        x = X0 + i * (cw + gap)
        s.rect(x, y, cw, CH, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 2.4 if on else 1.4, rx=12)
        iw = min(cw - 24, im["W"] * IH / im["H"])
        ih = iw * im["H"] / im["W"]
        _img(s, x + (cw - iw) / 2, y + 12 + (IH - ih) / 2, {**im, "W": iw, "H": ih, "credito": ""})
        ty = y + 12 + IH + 10 + 13
        s.text(x + cw / 2, ty, tl, 12.5, 800, "#9a3412" if on else INK, maxw=cw - 24, lh=17)
        if sl:
            s.text(x + cw / 2, ty + len(tl) * 17, sl, 11, 500, SLATE, maxw=cw - 24, lh=15)
        if on:
            case_chip(s, x + cw / 2, y, "ESTE CASO")
    y += CH
    if cred:
        credito(s, X0, y + 14, X1 - X0, cred)
        y += 18
    return y


# ════════════════════════════════════════════════════════════ 22 MAPA DE ZONAS (DIANA)
def zonas(s, y, d):
    """Zonas concéntricas dibujadas (de adentro hacia afuera) con la zona del caso; a la derecha, escalones
    (estadios o grados) con foto opcional y el del caso resaltado."""
    y = section(s, y + 10, d["rotulo"])
    anillos = d["anillos"]                    # [(nombre, sub)] de adentro hacia afuera
    radios = d.get("radios") or [(i + 1) / len(anillos) for i in range(len(anillos))]
    caso = d.get("caso_anillo", -1)
    DW = d.get("ancho_dibujo", 400)
    R = DW / 2 - 26
    nota_l = wrap(d.get("nota", ""), DW - 28, 11) if d.get("nota") else []
    # escalones a la derecha
    x = X0 + DW + 18
    w = X1 - x
    esc = d["escalones"]                      # [(etiqueta, nombre, detalle, img|None, on)]
    filas = []
    for etq, nom, det, im, on in esc:
        tw_img = 0
        if im:
            tw_img = min(150, im["W"] * 96 / im["H"])
        tx = 64 + (tw_img + 12 if im else 0)
        tl = wrap(nom, w - tx - 14, 12.5, True)
        dl = wrap(det, w - tx - 14, 11.5) if det else []
        h = max(48, len(tl) * 17 + len(dl) * 16 + 22, 96 + 16 if im else 0)
        filas.append((tl, dl, h, tw_img, tx))
    GAP = 8
    eh = sum(f[2] for f in filas) + GAP * (len(filas) - 1) + (30 if d.get("escalones_titulo") else 0)
    DH = 40 + 2 * R + 18 + (len(nota_l) * 15 + 8 if nota_l else 0) + 12
    H = max(DH, eh)
    panel(s, X0, y, DW, H, d["dibujo_titulo"])
    cx, cy = X0 + DW / 2, y + 40 + R + 6 + (H - DH) / 2
    s.add(f'<g data-box="{cx-R-4:.1f} {cy-R-4:.1f} {2*R+8:.1f} {2*R+8:.1f}">')
    tonos = ["#ccfbf1", "#99f6e4", "#5eead4", "#2dd4bf", "#14b8a6"]
    # desplaza: el anillo externo es un círculo corrido hacia un lado (p. ej. la zona III de la retina es una media
    # luna temporal): el centro de los demás se corre al revés para que todo quepa
    dx = d.get("desplaza", 0) * R
    n = len(anillos)
    ccx = cx - dx / 2 if dx else cx
    if dx:
        Rin = R - abs(dx) / 2
        radios = [r * Rin / R for r in radios[:-1]] + [1.0 - abs(dx) / 2 / R]
    for i in range(n - 1, -1, -1):
        r = R * radios[i]
        on = i == caso
        ox = ccx + (dx if (dx and i == n - 1) else 0)
        s.add(f'<circle cx="{ox:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{ORANGE_L if on else tonos[min(i, 4)]}" '
              f'stroke="{ORANGE if on else "#ffffff"}" stroke-width="{3 if on else 2}"/>')
    # rótulos de cada anillo, en la parte alta de su franja (el desplazado, en medio de su media luna)
    for i, (nom, sub) in enumerate(anillos):
        on = i == caso
        col = "#9a3412" if on else TEAL_D
        if dx and i == n - 1:
            r_in = R * radios[i - 1]
            lx = ccx + (r_in + dx + R * radios[i]) / 2 if dx > 0 else ccx - (r_in - dx + R * radios[i]) / 2
            mw = abs(dx) + R * radios[i] - r_in - 8
            s.text(lx, cy - 4, wrap(nom, mw, 12.5, True), 12.5, 800, col, maxw=mw, lh=16)
            if sub:
                s.text(lx, cy + 12 + (len(wrap(nom, mw, 12.5, True)) - 1) * 16, wrap(sub, mw, 10), 10, 600, col, maxw=mw, lh=13)
            continue
        r0 = R * (radios[i - 1] if i else 0)
        r1 = R * radios[i]
        ty = cy - (r0 + r1) / 2 if i else cy - r1 * 0.45
        mw = 2 * math.sqrt(max(r1 ** 2 - (cy - ty) ** 2, 1)) - 16 if i else r1 * 1.6
        s.text(ccx, ty + 1, nom, 12.5, 800, col, maxw=mw)
        if sub:
            s.text(ccx, ty + 15, sub, 10, 600, col, maxw=mw)
    cx = ccx
    for px, py, lab, col in d.get("puntos", []):
        X, Y = cx + px * R, cy + py * R
        s.circle(X, Y, 6, col, "#ffffff", 1.5)
        s.text(X, Y + 20, lab, 10.5, 800, INK, maxw=90)
    s.add('</g>')
    if nota_l:
        s.text(X0 + 14, cy + R + 26, nota_l, 11, 600, SLATE, "start", DW - 28, lh=15)
    # escalones
    yy = y
    if d.get("escalones_titulo"):
        s.text(x, y + 14, d["escalones_titulo"].upper(), 11, 800, MUTED, "start", w)
        yy += 30
    extra = (H - eh) / len(filas)
    for (etq, nom, det, im, on), (tl, dl, h0, tw_img, tx) in zip(esc, filas):
        h = h0 + extra
        s.rect(x, yy, w, h, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 2.2 if on else 1.3, rx=10)
        s.rect(x + 10, yy + h / 2 - 17, 44, 34, ORANGE if on else TEAL, rx=8)
        s.text(x + 32, yy + h / 2 + 5, etq, 13, 800, "#ffffff", maxw=38)
        if im:
            ih = 96
            iw = tw_img
            _img(s, x + 64, yy + (h - ih) / 2, {**im, "W": iw, "H": ih, "credito": ""})
        th = len(tl) * 17 + len(dl) * 16
        top = yy + (h - th) / 2
        s.text(x + tx, top + 13, tl, 12.5, 800, "#9a3412" if on else INK, "start", w - tx - 14, lh=17)
        if dl:
            s.text(x + tx, top + 13 + len(tl) * 17, dl, 11.5, 400, SLATE, "start", w - tx - 14, lh=16)
        if on:
            case_chip(s, x + w - tw("◆ ESTE CASO", 10, True) / 2 - 20, yy, d.get("tag", "ESTE CASO"))
        yy += h + GAP
    y += H
    if d.get("credito"):
        credito(s, X0, y + 14, X1 - X0, d["credito"])
        y += 18
    if d.get("claves"):
        y = fila_cards(s, y + 20, d["claves"], None, d.get("claves_titulo"))
    return y


# ════════════════════════════════════════════════════════════ 23 REGLA DE UMBRALES
SEV = [("#dcfce7", "#15803d"), ("#fef9c3", "#a16207"), ("#ffedd5", "#c2410c"), ("#fee2e2", "#b91c1c"), ("#fecdd3", "#9f1239")]


def regla(s, y, d):
    """Una o más reglas horizontales: bandas de color (de normal a grave) y el valor del caso marcado.
    regla = {nombre, que, min, max, bandas: [(desde, hasta, nombre, sev)], ticks, caso: valor|None, caso_txt, invertida}."""
    y = section(s, y + 10, d["rotulo"])
    W = X1 - X0
    for rg in d["reglas"]:
        tl = wrap(rg["nombre"], W - 40, 13.5, True)
        ql = wrap(rg.get("que", ""), W - 40, 11.5) if rg.get("que") else []
        BAR_Y = 26 + len(tl) * 19 + len(ql) * 16 + (48 if rg.get("caso") is not None else 14)
        H = BAR_Y + 40 + 30 + (46 if rg.get("pie") else 6)
        s.rect(X0, y, W, H, "#ffffff", LINE, 1.5, rx=12)
        s.text(X0 + 20, y + 26, tl, 13.5, 800, INK, "start", W - 40, lh=19)
        if ql:
            s.text(X0 + 20, y + 26 + len(tl) * 19, ql, 11.5, 500, SLATE, "start", W - 40, lh=16)
        bx0, bx1 = X0 + 30, X1 - 30
        vmin, vmax = rg["min"], rg["max"]
        X = lambda v: bx0 + (v - vmin) / (vmax - vmin) * (bx1 - bx0)
        by = y + BAR_Y
        for a, b, nom, sev in rg["bandas"]:
            fill, ink = SEV[sev]
            xa, xb = X(max(a, vmin)), X(min(b, vmax))
            s.rect(xa, by, xb - xa, 40, fill, "#ffffff", 2, rx=6)
            s.text((xa + xb) / 2, by + 25, nom, 12, 800, ink, maxw=xb - xa - 10)
        for v in rg.get("ticks", []):
            s.line(X(v), by + 40, X(v), by + 48, "#64748b", 1.5)
            s.text(X(v), by + 62, rg.get("fmt", "{}").format(v).replace(".", ","), 11, 700, SLATE, maxw=50)
        if rg.get("caso") is not None:
            cxv = X(rg["caso"])
            s.add(f'<polygon points="{cxv-9:.1f},{by-14:.1f} {cxv+9:.1f},{by-14:.1f} {cxv:.1f},{by-2:.1f}" fill="{ORANGE}"/>')
            lab = rg.get("caso_txt", "ESTE CASO")
            lw = tw("◆ " + lab, 10.5, True) + 20
            lx = min(max(cxv - lw / 2, X0 + 12), X1 - 12 - lw)
            s.rect(lx, by - 40, lw, 22, AMBER_L, AMBER, 1.5, rx=11)
            s.text(lx + lw / 2, by - 25, "◆ " + lab, 10.5, 800, "#b45309", maxw=lw - 12)
        pie = rg.get("pie")
        if pie:
            pl = wrap(pie, W - 60, 11.5, True)
            s.rect(X0 + 20, by + 74, W - 40, 30, ORANGE_L if rg.get("pie_on") else "#f8fafc",
                   ORANGE if rg.get("pie_on") else LINE, 1.2, rx=8)
            s.text(X0 + W / 2, by + 94, pl[0], 11.5, 700, "#9a3412" if rg.get("pie_on") else SLATE, maxw=W - 60)
        y += H + 14
    y -= 14
    if d.get("banda"):                       # imagen que muestra de dónde sale el valor (p. ej. la DXA)
        from engine7 import banda
        y = banda(s, y + 20, d["banda"])
    if d.get("claves"):
        y = fila_cards(s, y + 20, d["claves"], None, d.get("claves_titulo"))
    return y


# ════════════════════════════════════════════════════════════ 24 TABLA DE DECISIÓN DE DOS ENTRADAS
def decision(s, y, d):
    """Paso previo común a todos (banda naranja) → tabla filas × columnas con la conducta en cada celda.
    caso = (fila, columna) o (fila, None) si el enunciado no da la columna (se resalta la fila)."""
    y = section(s, y + 10, d["rotulo"])
    W = X1 - X0
    if d.get("previo"):
        t, dd = d["previo"]
        tl = wrap(t, W - 120, 14, True)
        dl = wrap(dd, W - 120, 12) if dd else []
        h = 22 + len(tl) * 19 + len(dl) * 17 + 12
        s.rect(X0, y, W, h, ORANGE, rx=12)
        s.rect(X0 + 14, y + h / 2 - 16, 74, 32, "#ffffff", rx=16)
        s.text(X0 + 51, y + h / 2 + 5, d.get("previo_etq", "PASO 1"), 11.5, 800, ORANGE, maxw=64)
        s.text(X0 + 104, y + 25, tl, 14, 800, "#ffffff", "start", W - 120, lh=19)
        if dl:
            s.text(X0 + 104, y + 25 + len(tl) * 19, dl, 12, 600, "#fff7ed", "start", W - 120, lh=17)
        y += h
        s.arrow_down(X0 + W / 2, y + 2, y + 24, ORANGE)
        y += 30
    cols, rows, cells = d["cols"], d["rows"], d["cells"]
    fr, fc = d["caso"]
    RW = d.get("ancho_filas", 200)
    nc = len(cols)
    cw = (W - RW) / nc
    # cabecera
    s.rect(X0, y, W, 34, "#f1f5f9", LINE, 1.2, rx=10)
    s.text(X0 + 14, y + 22, d.get("eje_y", "").upper(), 10.5, 800, MUTED, "start", RW - 20)
    for j, c in enumerate(cols):
        cl = wrap(c, cw - 20, 11.5, True)
        s.text(X0 + RW + j * cw + cw / 2, y + 22 - (len(cl) - 1) * 7, cl, 11.5, 800,
               "#9a3412" if j == fc else "#334155", maxw=cw - 20, lh=14)
    hh = 34
    if any(len(wrap(c, cw - 20, 11.5, True)) > 1 for c in cols):
        hh = 34 + 14 * (max(len(wrap(c, cw - 20, 11.5, True)) for c in cols) - 1)
        s.rect(X0, y, W, hh, "#f1f5f9", LINE, 1.2, rx=10)
        s.text(X0 + 14, y + hh / 2 + 4, d.get("eje_y", "").upper(), 10.5, 800, MUTED, "start", RW - 20)
        for j, c in enumerate(cols):
            cl = wrap(c, cw - 20, 11.5, True)
            s.text(X0 + RW + j * cw + cw / 2, y + hh / 2 + 4 - (len(cl) - 1) * 7, cl, 11.5, 800,
                   "#9a3412" if j == fc else "#334155", maxw=cw - 20, lh=14)
    y += hh + 6
    for i, (rn, rsub) in enumerate(rows):
        rl = wrap(rn, RW - 28, 12.5, True)
        rs = wrap(rsub, RW - 28, 10.5) if rsub else []
        cm = []
        for j in range(nc):
            t, ls = cells[i][j]
            tl = wrap(t, cw - 24, 12, True)
            bl = []
            for l in ls:
                bl += wrap(l, cw - 24, 11)
            cm.append((tl, bl))
        h = max(len(rl) * 17 + len(rs) * 14 + 26, max(len(tl) * 16 + len(bl) * 15 + 26 for tl, bl in cm))
        on_r = i == fr
        s.rect(X0, y, RW - 6, h, ORANGE if on_r else "#f8fafc", ORANGE if on_r else LINE, 1.5, rx=10)
        top = y + (h - (len(rl) * 17 + len(rs) * 14)) / 2
        s.text(X0 + 14, top + 13, rl, 12.5, 800, "#ffffff" if on_r else INK, "start", RW - 28, lh=17)
        if rs:
            s.text(X0 + 14, top + 13 + len(rl) * 17, rs, 10.5, 500, "#ffedd5" if on_r else SLATE, "start", RW - 28, lh=14)
        for j, (tl, bl) in enumerate(cm):
            cx = X0 + RW + j * cw
            on = on_r and (fc is None or fc == j)
            s.rect(cx + 3, y, cw - 6, h, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 2.2 if on else 1.2, rx=10)
            top = y + (h - (len(tl) * 16 + len(bl) * 15)) / 2
            s.text(cx + 15, top + 12, tl, 12, 800, "#9a3412" if on else INK, "start", cw - 24, lh=16)
            if bl:
                s.text(cx + 15, top + 12 + len(tl) * 16, bl, 11, 400, SLATE, "start", cw - 24, lh=15)
            if on and (fc == j or j == nc - 1):
                case_chip(s, cx + cw - tw("◆ ESTE CASO", 10, True) / 2 - 22, y, d.get("tag", "ESTE CASO"))
        y += h + 6
    y -= 6
    if d.get("nota"):
        nl = wrap(d["nota"], W - 30, 11.5)
        s.text(X0 + 4, y + 22, nl, 11.5, 600, TEAL_D, "start", W - 20, lh=16)
        y += 14 + len(nl) * 16
    if d.get("claves"):
        y = fila_cards(s, y + 20, d["claves"], None, d.get("claves_titulo"))
    return y




def _veredicto(s, y, v):
    """Barra oscura final: (título, detalle)."""
    t, dd = v
    tl = wrap(t, X1 - X0 - 40, 13.5, True)
    dl = wrap(dd, X1 - X0 - 40, 12) if dd else []
    h = 22 + len(tl) * 19 + len(dl) * 17 + 14
    s.rect(X0, y, X1 - X0, h, TEAL_D, rx=12)
    s.text(X0 + 20, y + 26, tl, 13.5, 800, "#ffffff", "start", X1 - X0 - 40, lh=19)
    if dl:
        s.text(X0 + 20, y + 26 + len(tl) * 19, dl, 12, 500, "#ccfbf1", "start", X1 - X0 - 40, lh=17)
    return y + h


def _fin(s, y, d):
    if d.get("veredicto"):
        y = _veredicto(s, y + 18, d["veredicto"])
    if d.get("claves"):
        y = fila_cards(s, y + 20, d["claves"], None, d.get("claves_titulo"))
    return y


def _caja_txt(t, dd, w, ft=12.5, fd=11.5):
    tl = wrap(t, w, ft, True)
    dl = []
    for l in ([dd] if isinstance(dd, str) else (dd or [])):
        dl += wrap(l, w, fd)
    return tl, dl, len(tl) * 17 + len(dl) * 16


def _txt(s, x, top, tl, dl, w, on, col_on="#9a3412", ft=12.5, fd=11.5, anchor="start"):
    s.text(x, top + 13, tl, ft, 800, col_on if on else INK, anchor, w, lh=17)
    if dl:
        s.text(x, top + 13 + len(tl) * 17, dl, fd, 400, SLATE, anchor, w, lh=16)


# ════════════════════════════════════════════════════════════ 27 CUADRÍCULA 2×2
def cuadricula(s, y, d):
    """Cuatro casillas (2×2), cada una con foto opcional, título y datos; la del caso resaltada.
    Con cols/rows (p. ej. FODA: interno/externo × favorable/desfavorable) se rotulan los ejes."""
    y = section(s, y + 10, d["rotulo"])
    cols, rows = d.get("cols"), d.get("rows")
    RW = 120 if rows else 0
    x0 = X0 + RW
    W = X1 - x0
    gap = 14
    cw = (W - gap) / 2
    if cols:
        for j, c in enumerate(cols):
            s.rect(x0 + j * (cw + gap), y, cw, 30, "#f1f5f9", LINE, 1.2, rx=8)
            s.text(x0 + j * (cw + gap) + cw / 2, y + 20, c, 11.5, 800, "#334155", maxw=cw - 16)
        y += 38
    cel = d["celdas"]
    IH = d.get("alto_img", 150)
    for r in range(2):
        meds = []
        for c in range(2):
            t, ls, im, on = cel[r * 2 + c]
            tl, dl, th = _caja_txt(t, ls, cw - 28)
            meds.append((tl, dl, th))
        hasimg = any(cel[r * 2 + c][2] for c in range(2))
        h = 14 + (IH + 12 if hasimg else 0) + max(m[2] for m in meds) + 16
        if rows:
            rl = wrap(rows[r], RW - 20, 11.5, True)
            s.rect(X0, y, RW - 8, h, "#f1f5f9", LINE, 1.2, rx=8)
            s.text(X0 + (RW - 8) / 2, y + h / 2 + 4 - (len(rl) - 1) * 7.5, rl, 11.5, 800, "#334155", maxw=RW - 20, lh=15)
        for c in range(2):
            t, ls, im, on = cel[r * 2 + c]
            tl, dl, th = meds[c]
            x = x0 + c * (cw + gap)
            s.rect(x, y, cw, h, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 2.4 if on else 1.4, rx=12)
            ty = y + 14
            if im:
                iw = min(cw - 28, im["W"] * IH / im["H"])
                ih = iw * im["H"] / im["W"]
                _img(s, x + (cw - iw) / 2, ty + (IH - ih) / 2, {**im, "W": iw, "H": ih, "credito": ""})
                ty += IH + 12
            elif hasimg:
                ty += (IH + 12) / 2 - 8
            _txt(s, x + 14, ty, tl, dl, cw - 28, on)
            if on:
                case_chip(s, x + cw - tw("◆ ESTE CASO", 10, True) / 2 - 20, y, d.get("tag", "ESTE CASO"))
        y += h + gap
    y -= gap
    if d.get("credito"):
        credito(s, X0, y + 14, X1 - X0, d["credito"])
        y += 18
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 40 SIGNOS DE ALARMA
def alarma(s, y, d):
    """Signos de alarma (triángulo rojo si están en el caso) → qué hacer si hay al menos uno; imagen opcional."""
    y = section(s, y + 10, d["rotulo"])
    im = d.get("img")
    RWd = (im["W"] + 28) if im else 300
    LW = X1 - X0 - RWd - 18
    sig = d["signos"]
    meds = [_caja_txt(t, dd, LW - 70) for t, dd, _ in sig]
    rows_h = [max(44, m[2] + 20) for m in meds]
    s.rect(X0, y, LW, 34, RED_L, "#fca5a5", 1.2, rx=10)
    s.text(X0 + 16, y + 22, d.get("lista_titulo", "Signos de alarma").upper(), 11.5, 800, "#991b1b", "start", LW - 150)
    s.text(X0 + LW - 16, y + 22, "EN EL CASO", 10.5, 800, "#991b1b", "end", 100)
    yy = y + 40
    for (t, dd, pres), (tl, dl, th), h in zip(sig, meds, rows_h):
        s.rect(X0, yy, LW, h, "#fff1f2" if pres else "#ffffff", "#ef4444" if pres else LINE, 1.6 if pres else 1.1, rx=8)
        cx, cy = X0 + 22, yy + h / 2
        col = "#dc2626" if pres else "#cbd5e1"
        s.add(f'<polygon points="{cx:.1f},{cy-11:.1f} {cx+12:.1f},{cy+9:.1f} {cx-12:.1f},{cy+9:.1f}" fill="{col}"/>')
        s.text(cx, cy + 6, "!", 11, 800, "#ffffff", maxw=0)
        _txt(s, X0 + 44, yy + (h - th) / 2, tl, dl, LW - 140, pres, "#991b1b")
        lab = "Sí" if pres is True else ("No" if pres is False else "Sin dato")
        s.text(X0 + LW - 16, yy + h / 2 + 4, lab, 12, 800, "#dc2626" if pres else MUTED, "end", 80)
        yy += h + 6
    LH = yy - 6 - y
    # panel derecho: imagen opcional + acción
    x = X1 - RWd
    a_t, a_d = d["accion"]
    atl, adl, ath = _caja_txt(a_t, a_d, RWd - 32, 13.5, 12)
    ah = ath + 50
    ih = (40 + _img_h(im) + 10) if im else 0
    H = max(LH, ih + 14 + ah)
    if im:
        panel(s, x, y, RWd, ih, d.get("img_titulo", "Así se ve"))
        _img(s, x + 14, y + 38, im)
    ay = y + (ih + 14 if im else 0)
    ah = H - (ay - y)
    s.rect(x, ay, RWd, ah, "#dc2626", rx=12)
    s.text(x + 16, ay + 24, d.get("accion_rotulo", "Si hay uno o más").upper(), 10.5, 800, "#fecaca", "start", RWd - 32)
    top = ay + 34 + (ah - 34 - ath) / 2 - 6
    s.text(x + 16, top + 13, atl, 13.5, 800, "#ffffff", "start", RWd - 32, lh=17)
    if adl:
        s.text(x + 16, top + 13 + len(atl) * 17, adl, 12, 500, "#fee2e2", "start", RWd - 32, lh=16)
    y += H
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 47 CASCADA FISIOPATOLÓGICA
def cascada(s, y, d):
    """De la causa al signo: cada paso del mecanismo (izquierda, con flechas hacia abajo) y, en su misma fila,
    lo que produce en el caso (derecha)."""
    y = section(s, y + 10, d["rotulo"])
    LW = d.get("ancho_pasos", 430)
    AW = 46
    x2 = X0 + LW + AW
    RW = X1 - x2
    if d.get("cabeceras"):
        a, b = d["cabeceras"]
        s.text(X0, y + 12, a.upper(), 10.5, 800, MUTED, "start", LW)
        s.text(x2, y + 12, b.upper(), 10.5, 800, MUTED, "start", RW)
        y += 22
    for i, (t, dd, efs) in enumerate(d["pasos"]):
        tl, dl, th = _caja_txt(t, dd, LW - 60)
        em = [_caja_txt(et, ed, RW - 30, 12, 11) + (on,) for et, ed, on in efs]
        eh = sum(m[2] + 22 for m in em) + 6 * max(len(em) - 1, 0)
        h = max(th + 26, eh, 46)
        s.rect(X0, y, LW, h, TEAL_L, TEAL_B, 1.5, rx=10)
        s.circle(X0 + 22, y + h / 2, 12, TEAL)
        s.text(X0 + 22, y + h / 2 + 4.5, str(i + 1), 12, 800, "#ffffff", maxw=0)
        _txt(s, X0 + 44, y + (h - th) / 2, tl, dl, LW - 60, False)
        if em:
            s.arrow_right(X0 + LW + 6, x2 - 6, y + h / 2, ORANGE)
        ey = y + (h - eh) / 2
        for tl2, dl2, th2, on in em:
            hh = th2 + 22
            s.rect(x2, ey, RW, hh, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 1.8 if on else 1.2, rx=10)
            s.text(x2 + 14, ey + 11 + 13, tl2, 12, 800, "#9a3412" if on else INK, "start", RW - 30, lh=17)
            if dl2:
                s.text(x2 + 14, ey + 11 + 13 + len(tl2) * 17, dl2, 11, 400, SLATE, "start", RW - 30, lh=16)
            ey += hh + 6
        y += h
        if i < len(d["pasos"]) - 1:
            s.arrow_down(X0 + LW / 2, y + 2, y + 22, TEAL)
            y += 24
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 39 LISTA DE VERIFICACIÓN
def checklist(s, y, d):
    """Pasos en orden con su casilla (el que pide la pregunta resaltado) y, a la derecha, lo que NO se hace."""
    y = section(s, y + 10, d["rotulo"])
    no = d.get("no_hacer", [])
    RW = 300 if no else 0
    LW = X1 - X0 - (RW + 18 if no else 0)
    yy = y
    for i, (t, dd, on) in enumerate(d["pasos"]):
        tl, dl, th = _caja_txt(t, dd, LW - 90)
        h = max(46, th + 24)
        s.rect(X0, yy, LW, h, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 2.2 if on else 1.2, rx=10)
        s.text(X0 + 20, yy + h / 2 + 5, str(i + 1), 14, 800, ORANGE if on else TEAL, maxw=0)
        s.rect(X0 + 38, yy + h / 2 - 11, 22, 22, ORANGE if on else TEAL, rx=5)
        s.text(X0 + 49, yy + h / 2 + 5, "✓", 13, 800, "#ffffff", maxw=0)
        _txt(s, X0 + 74, yy + (h - th) / 2, tl, dl, LW - 90, on)
        if on:
            case_chip(s, X0 + LW - tw("◆ ESTE CASO", 10, True) / 2 - 20, yy, d.get("tag", "PRIMERO"))
        yy += h + 8
    LH = yy - 8 - y
    if no:
        x = X1 - RW
        meds = [_caja_txt(t, dd, RW - 56, 12, 11) for t, dd in no]
        nh = 40 + sum(m[2] + 16 for m in meds) + 10
        H = max(LH, nh)
        s.rect(x, y, RW, H, RED_L, "#fca5a5", 1.5, rx=12)
        s.text(x + 16, y + 26, d.get("no_titulo", "No hacer").upper(), 11.5, 800, "#991b1b", "start", RW - 32)
        cy = y + 40 + (H - nh) / 2
        for tl, dl, th in meds:
            s.text(x + 22, cy + 13, "✕", 13, 800, "#dc2626", maxw=0)
            s.text(x + 40, cy + 13, tl, 12, 800, "#7f1d1d", "start", RW - 56, lh=17)
            if dl:
                s.text(x + 40, cy + 13 + len(tl) * 17, dl, 11, 400, "#7f1d1d", "start", RW - 56, lh=16)
            cy += th + 16
        LH = H
    y += LH
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 50 MONITOR DE SIGNOS VITALES
def monitor(s, y, d):
    """Pantalla de monitor con los signos vitales del caso (rojo alto, azul bajo, verde normal) y, a la derecha,
    cómo se leen juntos."""
    y = section(s, y + 10, d["rotulo"])
    MW = d.get("ancho_monitor", 470)
    vals = d["valores"]
    ncol = 2
    tw_ = (MW - 36 - 12) / ncol
    th_ = 82
    nfil = (len(vals) + 1) // 2
    ecg_h = 84 if d.get("ecg") else 0
    MH = 50 + ecg_h + nfil * (th_ + 10) + 8
    lect = d["lectura"]
    x = X0 + MW + 18
    w = X1 - x
    meds = [_caja_txt(t, dd, w - 30) for t, dd, _ in lect]
    lh = sum(m[2] + 24 for m in meds) + 8 * (len(meds) - 1)
    H = max(MH, lh)
    s.rect(X0, y, MW, H, "#0b1220", "#334155", 3, rx=16)
    s.rect(X0 + 12, y + 12, 150, 24, "#1e293b", rx=6)
    s.text(X0 + 22, y + 29, d.get("titulo_monitor", "MONITOR · ESTE CASO"), 10.5, 800, "#5eead4", "start", 132)
    yy = y + 50
    if d.get("ecg"):
        pts = []
        n = int((MW - 40) / 46)
        for k in range(n):
            bx = X0 + 20 + k * 46
            base = yy + 58
            pts += [(bx, base), (bx + 12, base), (bx + 15, base - 6), (bx + 18, base), (bx + 21, base + 4),
                    (bx + 24, base - 30), (bx + 27, base + 8), (bx + 30, base), (bx + 38, base - 8), (bx + 44, base)]
        s.add('<polyline points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + '" fill="none" stroke="#4ade80" stroke-width="2"/>')
        s.text(X0 + MW - 20, yy + 6, d["ecg"], 10.5, 800, "#4ade80", "end", 200)
        yy += ecg_h
    COL = {"alto": ("#f87171", "#450a0a"), "bajo": ("#60a5fa", "#0c1e3d"), "ok": ("#4ade80", "#052e16")}
    for k, (sig, val, uni, est) in enumerate(vals):
        cx = X0 + 18 + (k % ncol) * (tw_ + 12)
        cy = yy + (k // ncol) * (th_ + 10)
        fg, bg = COL[est]
        s.rect(cx, cy, tw_, th_, bg, fg, 1.5, rx=10)
        s.text(cx + 12, cy + 22, sig, 11.5, 800, fg, "start", tw_ - 24)
        s.text(cx + tw_ / 2, cy + 58, val, 26, 800, fg, maxw=tw_ - 24)
        s.text(cx + tw_ - 12, cy + 22, uni + (" ▲" if est == "alto" else (" ▼" if est == "bajo" else "")), 10.5, 700, fg, "end", tw_ / 2)
    cy = y + (H - lh) / 2
    for (t, dd, on), (tl, dl, th) in zip(lect, meds):
        h = th + 24
        s.rect(x, cy, w, h, ORANGE_L if on else "#f8fafc", ORANGE if on else LINE, 2 if on else 1.2, rx=10)
        _txt(s, x + 15, cy + 12, tl, dl, w - 30, on)
        cy += h + 8
    y += H
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 30 PIRÁMIDE
def piramide(s, y, d):
    """Pirámide de niveles (de la cima a la base) con el nivel del caso y su descripción al lado."""
    y = section(s, y + 10, d["rotulo"])
    niv = d["niveles"]
    n = len(niv)
    PW = d.get("ancho", 420)
    x = X0 + PW + 26
    w = X1 - x
    meds = [_caja_txt(t, dd, w - 30) for _, t, dd in niv]
    rh = max(56, max(m[2] for m in meds) + 22)
    gap = 6
    caso = d.get("caso", -1)
    cxp = X0 + PW / 2
    for i, ((et, t, dd), (tl, dl, th)) in enumerate(zip(niv, meds)):
        yy = y + i * (rh + gap)
        wt = 100 + (PW - 100) * i / n
        wb = 100 + (PW - 100) * (i + 1) / n
        on = i == caso
        fill = ORANGE if on else ["#ccfbf1", "#99f6e4", "#5eead4", "#2dd4bf", "#14b8a6", "#0d9488"][min(i, 5)]
        s.add(f'<polygon points="{cxp-wt/2:.1f},{yy:.1f} {cxp+wt/2:.1f},{yy:.1f} {cxp+wb/2:.1f},{yy+rh:.1f} {cxp-wb/2:.1f},{yy+rh:.1f}" '
              f'fill="{fill}" stroke="#ffffff" stroke-width="2"/>')
        s.text(cxp, yy + rh / 2 + 5, et, 12.5, 800, "#ffffff" if (on or i >= 3) else TEAL_D, maxw=wt - 12)
        s.rect(x, yy, w, rh, ORANGE_L if on else "#ffffff", ORANGE if on else LINE, 2 if on else 1.2, rx=10)
        _txt(s, x + 15, yy + (rh - th) / 2, tl, dl, w - 30, on)
        if on:
            case_chip(s, x + w - tw("◆ ESTE CASO", 10, True) / 2 - 20, yy, d.get("tag", "ESTE CASO"))
    y += n * (rh + gap) - gap
    if d.get("pie"):
        s.text(cxp, y + 18, d["pie"], 10.5, 700, MUTED, maxw=PW)
        y += 22
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 46 GRADOS CON FOTO
def grados_foto(s, y, d):
    """Los grados de una clasificación en fila, cada uno con su foto o dibujo, y el del caso resaltado."""
    y = section(s, y + 10, d["rotulo"])
    if d.get("criterio"):
        cl = wrap(d["criterio"], X1 - X0 - 20, 12, True)
        s.text(X0 + 4, y + 14, cl, 12, 700, TEAL_D, "start", X1 - X0 - 20, lh=17)
        y += len(cl) * 17 + 10
    items = [(im, f"{etq} · {nom}" if nom else etq, det, on) for etq, nom, det, im, on in d["grados"]]
    y = _tira(s, y, items, d.get("tira_titulo", ""), d.get("credito")) if True else y
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 32 PANEL DE LABORATORIO
def laboratorio(s, y, d):
    """Resultados del caso con su valor normal y una flecha (↑ alto, ↓ bajo); a la derecha, qué significa cada uno.
    Abajo, el patrón que forman juntos."""
    y = section(s, y + 10, d["rotulo"])
    W = X1 - X0
    c1, c2, c3 = 200, 150, 150
    c4 = W - c1 - c2 - c3
    s.rect(X0, y, W, 32, "#f1f5f9", LINE, 1.2, rx=8)
    for t, xx, ww in (("Examen", X0 + 14, c1), ("Valor del caso", X0 + c1 + 10, c2), ("Normal", X0 + c1 + c2 + 10, c3),
                      ("Qué significa", X0 + c1 + c2 + c3 + 10, c4)):
        s.text(xx, y + 21, t.upper(), 10.5, 800, MUTED, "start", ww - 20)
    y += 38
    COL = {"↑": ("#dc2626", "#fef2f2"), "↓": ("#2563eb", "#eff6ff"), "=": ("#15803d", "#f0fdf4")}
    for ex, val, ref, fl, sig in d["valores"]:
        sl = wrap(sig, c4 - 24, 11.5)
        el = wrap(ex, c1 - 24, 12, True)
        h = max(40, len(sl) * 16 + 18, len(el) * 17 + 16)
        fg, bg = COL[fl]
        s.rect(X0, y, W, h, bg, LINE, 1, rx=8)
        s.text(X0 + 14, y + h / 2 + 4 - (len(el) - 1) * 8.5, el, 12, 800, INK, "start", c1 - 24, lh=17)
        s.text(X0 + c1 + 10, y + h / 2 + 5, val + ("  " + fl if fl != "=" else ""), 13, 800, fg, "start", c2 - 16)
        s.text(X0 + c1 + c2 + 10, y + h / 2 + 4, ref, 11.5, 500, SLATE, "start", c3 - 16)
        s.text(X0 + c1 + c2 + c3 + 10, y + h / 2 + 4 - (len(sl) - 1) * 8, sl, 11.5, 500, "#334155", "start", c4 - 24, lh=16)
        y += h + 4
    y -= 4
    return _fin(s, y, d)



# ════════════════════════════════════════════════════════════ 25 RELOJ / LÍNEA DE PASOS
def reloj(s, y, d):
    """Pasos o tiempos sobre una línea (como un recorrido de metro): cada estación con su hora o número,
    título y detalle; la del caso resaltada. Más de 5 pasos se reparten en dos filas."""
    y = section(s, y + 10, d["rotulo"])
    pasos = d["pasos"]                # [(etiqueta, título, detalle, on)]
    n = len(pasos)
    filas = [pasos] if n <= 5 else [pasos[:(n + 1) // 2], pasos[(n + 1) // 2:]]
    W = X1 - X0
    if d.get("intro"):
        il = wrap(d["intro"], W - 20, 12, True)
        s.text(X0 + 4, y + 14, il, 12, 700, TEAL_D, "start", W - 20, lh=17)
        y += len(il) * 17 + 10
    k0 = 0
    for fila in filas:
        m = len(fila)
        cw = W / m
        meds = [_caja_txt(t, dd, cw - 22, 12, 11) for _, t, dd, _ in fila]
        ch = max(mm[2] for mm in meds) + 26
        ly = y + 26
        for j in range(m - 1):                 # tramos entre estaciones (sin cruzar los números)
            s.line(X0 + j * cw + cw / 2 + 23, ly, X0 + (j + 1) * cw + cw / 2 - 23, ly, TEAL_B, 6)
        for j, ((et, t, dd, on), (tl, dl, th)) in enumerate(zip(fila, meds)):
            cx = X0 + j * cw + cw / 2
            r = 22
            s.add(f'<circle cx="{cx:.1f}" cy="{ly:.1f}" r="{r}" fill="{ORANGE if on else "#ffffff"}" stroke="{ORANGE if on else TEAL}" stroke-width="3"/>')
            s.text(cx, ly + 4.5, et, 11.5 if len(et) <= 4 else 9.5, 800, "#ffffff" if on else TEAL_D, maxw=2 * r - 6)
            by = ly + r + 12
            s.rect(X0 + j * cw + 5, by, cw - 10, ch, ORANGE_L if on else "#f8fafc", ORANGE if on else LINE, 2 if on else 1.2, rx=10)
            s.text(cx, by + 20, tl, 12, 800, "#9a3412" if on else INK, maxw=cw - 22, lh=17)
            if dl:
                s.text(cx, by + 20 + len(tl) * 17, dl, 11, 400, SLATE, maxw=cw - 22, lh=16)
            if on:
                case_chip(s, cx, by + ch, d.get("tag", "ESTE CASO"))
        y = ly + 22 + 12 + ch + 22
        k0 += m
    y -= 8
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 42 CADENA DE TRANSMISIÓN
def transmision(s, y, d):
    """Eslabones de la cadena (agente → reservorio → salida → vía → entrada → huésped) y debajo de cada uno la medida
    que la corta; la medida del caso resaltada."""
    y = section(s, y + 10, d["rotulo"])
    es = d["eslabones"]               # [(eslabón, qué es en esta enfermedad, medida, on)]
    n = len(es)
    W = X1 - X0
    gap = 26
    cw = (W - gap * (n - 1)) / n
    m1 = [_caja_txt(a, b, cw - 20, 12, 11) for a, b, _, _ in es]
    m2 = [_caja_txt(c, None, cw - 20, 11.5, 11) for _, _, c, _ in es]
    h1 = max(mm[2] for mm in m1) + 26
    h2 = max(mm[2] for mm in m2) + 30
    for i, ((a, b, c, on), (tl, dl, th), (tl2, _, th2)) in enumerate(zip(es, m1, m2)):
        x = X0 + i * (cw + gap)
        s.rect(x, y, cw, h1, TEAL_L, TEAL, 1.6, rx=14)
        s.text(x + cw / 2, y + 20, tl, 12, 800, TEAL_D, maxw=cw - 20, lh=17)
        if dl:
            s.text(x + cw / 2, y + 20 + len(tl) * 17, dl, 11, 400, SLATE, maxw=cw - 20, lh=16)
        if i < n - 1:
            s.arrow_right(x + cw + 3, x + cw + gap - 3, y + h1 / 2, TEAL)
        s.line(x + cw / 2, y + h1 + 2, x + cw / 2, y + h1 + 16, ORANGE if on else "#cbd5e1", 2.5, dash="4 3")
        yy = y + h1 + 18
        s.rect(x, yy, cw, h2, ORANGE if on else "#ffffff", ORANGE if on else LINE, 2 if on else 1.2, rx=10)
        s.text(x + cw / 2, yy + 14, "✂ CORTA", 9.5, 800, "#ffedd5" if on else MUTED, maxw=cw - 20)
        s.text(x + cw / 2, yy + 31, tl2, 11.5, 800, "#ffffff" if on else INK, maxw=cw - 20, lh=16)
        if on:
            case_chip(s, x + cw / 2, yy + h2, d.get("tag", "ESTE CASO"))
    y += h1 + 18 + h2 + 12
    if d.get("img"):
        from engine7 import banda
        y = banda(s, y + 10, d["img"])
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 41 DOSIS POR PESO
def dosis(s, y, d):
    """Cálculo de la dosis con el peso del caso: ficha del paciente → (dosis por kg × peso = total) en cajas grandes,
    y debajo cada alternativa medida contra ese total (la que coincide resaltada)."""
    y = section(s, y + 10, d["rotulo"])
    W = X1 - X0
    pw = 170
    peso, quien = d["peso"]
    pasos = d["pasos"]                       # [(etiqueta, valor grande, detalle)] separados por operadores
    ops = d.get("ops", ["×", "="])
    n = len(pasos)
    x0 = X0 + pw + 30
    gap = 40
    cw = (X1 - x0 - gap * (n - 1)) / n
    meds = [_caja_txt(dd, None, cw - 20, 11, 11) for _, _, dd in pasos]
    ch = 76 + max(m[2] for m in meds)
    s.rect(X0, y, pw, ch, TEAL_D, rx=16)
    s.text(X0 + pw / 2, y + 26, "PESO DEL CASO", 10.5, 800, "#99f6e4", maxw=pw - 20)
    s.text(X0 + pw / 2, y + 62, peso, 28, 800, "#ffffff", maxw=pw - 16)
    ql = wrap(quien, pw - 24, 11)
    s.text(X0 + pw / 2, y + 84, ql, 11, 500, "#ccfbf1", maxw=pw - 24, lh=15)
    s.arrow_right(X0 + pw + 4, x0 - 4, y + ch / 2, TEAL)
    for i, ((et, val, dd), (tl, _, th)) in enumerate(zip(pasos, meds)):
        x = x0 + i * (cw + gap)
        last = i == n - 1
        s.rect(x, y, cw, ch, ORANGE_L if last else "#ffffff", ORANGE if last else TEAL, 2.2 if last else 1.6, rx=14)
        s.text(x + cw / 2, y + 22, et.upper(), 10.5, 800, "#9a3412" if last else MUTED, maxw=cw - 16)
        s.text(x + cw / 2, y + 56, val, 22, 800, "#9a3412" if last else TEAL_D, maxw=cw - 16)
        s.text(x + cw / 2, y + 78, tl, 11, 800, SLATE, maxw=cw - 20, lh=15)
        if last:
            case_chip(s, x + cw / 2, y + ch, d.get("tag", "DOSIS DEL CASO"))
        if i < n - 1:
            s.text(x + cw + gap / 2, y + ch / 2 + 11, ops[min(i, len(ops) - 1)], 30, 800, TEAL, maxw=gap)
    y += ch + 22
    if d.get("alternativas"):
        alts = d["alternativas"]             # [(alternativa, comentario, ok)]
        s.text(X0 + 4, y + 14, d.get("alt_titulo", "Cada alternativa contra el cálculo").upper(), 10.5, 800, MUTED, "start", W)
        y += 24
        m = len(alts)
        aw = (W - 10 * (m - 1)) / m
        mm = [_caja_txt(a, c, aw - 20, 12, 11) for a, c, _ in alts]
        ah = max(t[2] for t in mm) + 40
        for j, ((a, c, ok), (tl, dl, th)) in enumerate(zip(alts, mm)):
            x = X0 + j * (aw + 10)
            s.rect(x, y, aw, ah, GREEN_L if ok else "#f8fafc", GREEN if ok else LINE, 2 if ok else 1.2, rx=10)
            s.text(x + aw / 2, y + 18, "✓ COINCIDE" if ok else "✗ NO", 9.5, 800, GREEN if ok else "#b91c1c", maxw=aw - 16)
            s.text(x + aw / 2, y + 36, tl, 12, 800, INK, maxw=aw - 20, lh=17)
            if dl:
                s.text(x + aw / 2, y + 36 + len(tl) * 17, dl, 11, 400, SLATE, maxw=aw - 20, lh=16)
        y += ah
    if d.get("img"):
        from engine7 import banda
        y = banda(s, y + 14, d["img"])
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 48 ECG: DERIVACIONES Y TERRITORIO
_ECG_TERR = [("Inferior", ["II", "III", "aVF"], "Coronaria derecha (80 %)"),
             ("Lateral", ["I", "aVL", "V5", "V6"], "Circunfleja"),
             ("Septal", ["V1", "V2"], "Descendente anterior (septales)"),
             ("Anterior", ["V3", "V4"], "Descendente anterior")]


def _latido(s, cx, by, w, st, color):
    """Un complejo esquemático: st = 'sube' | 'baja' | 'q' (onda Q + ST arriba) | 'normal'."""
    a = w / 60
    dy = {"sube": -14, "baja": 10, "q": -14}.get(st, 0)
    q = 9 if st == "q" else 2
    pts = [(-28, 0), (-20, 0), (-17, -5), (-14, 0), (-8, 0), (-6, q), (-2, -30), (2, 8), (5, dy), (12, dy - 4 if st != "baja" else dy + 2),
           (17, dy - 2 if st == "sube" or st == "q" else -6), (22, 0), (28, 0)]
    s.add('<polyline points="' + " ".join(f"{cx + px * a:.1f},{by + py:.1f}" for px, py in pts) +
          f'" fill="none" stroke="{color}" stroke-width="2.2" stroke-linejoin="round"/>')


def ecg_mapa(s, y, d):
    """Las 12 derivaciones en su cuadrícula (I aVR V1 V4 / II aVL V2 V5 / III aVF V3 V6) con el ST de cada una;
    a la derecha, qué territorio y qué arteria corresponden (el del caso resaltado). Debajo, el ECG real o propio."""
    y = section(s, y + 10, d["rotulo"])
    der = d["derivaciones"]                  # {"V2": "sube", "II": "baja", ...}; las que no están: normal
    GW = d.get("ancho", 470)
    cols = [["I", "II", "III"], ["aVR", "aVL", "aVF"], ["V1", "V2", "V3"], ["V4", "V5", "V6"]]
    cw, rh = GW / 4, 78
    s.rect(X0, y, GW, rh * 3 + 8, "#fff7f7", "#fecaca", 1.2, rx=10)
    for i in range(1, 4):
        s.line(X0 + i * cw, y + 6, X0 + i * cw, y + rh * 3 + 2, "#fecaca", 1)
    COLS = {"sube": "#dc2626", "q": "#dc2626", "baja": "#2563eb", "normal": "#475569"}
    for c, col in enumerate(cols):
        for r, nm in enumerate(col):
            st = der.get(nm, "normal")
            cx, cy = X0 + c * cw + cw / 2, y + 8 + r * rh
            on = st != "normal"
            if on:
                s.rect(X0 + c * cw + 4, cy, cw - 8, rh - 6, "#fee2e2" if st != "baja" else "#dbeafe", rx=8)
            s.text(X0 + c * cw + 12, cy + 18, nm, 12, 800, COLS[st], "start", 40)
            _latido(s, cx + 8, cy + 48, cw - 30, st, COLS[st])
    leyenda = d.get("leyenda", "Rojo: ST elevado · Azul: ST descendido (espejo) · Gris: normal")
    s.text(X0 + GW / 2, y + rh * 3 + 26, leyenda, 10.5, 700, MUTED, maxw=GW)
    x = X0 + GW + 22
    w = X1 - x
    terr = d.get("territorios", _ECG_TERR)
    caso = d.get("caso", [])
    meds = [_caja_txt(f"{t}: {', '.join(dv)}", a, w - 30) for t, dv, a in terr]
    yy = y
    for (t, dv, a), (tl, dl, th) in zip(terr, meds):
        on = t in caso
        h = th + 22
        s.rect(x, yy, w, h, ORANGE_L if on else "#f8fafc", ORANGE if on else LINE, 2 if on else 1.2, rx=10)
        _txt(s, x + 15, yy + 11, tl, dl, w - 30, on)
        yy += h + 7
    if d.get("territorio_txt"):
        tl = wrap(d["territorio_txt"], w - 10, 11.5, True)
        s.text(x + 4, yy + 12, tl, 11.5, 800, "#9a3412", "start", w - 10, lh=16)
        yy += len(tl) * 16 + 6
    y = max(y + rh * 3 + 34, yy)
    if d.get("img"):
        from engine7 import banda
        y = banda(s, y + 12, d["img"])
    return _fin(s, y, d)


# ════════════════════════════════════════════════════════════ 29 GRÁFICA CLÍNICA CON EL PUNTO DEL CASO
def grafica(s, y, d):
    """Gráfica x-y (curva fisiológica o clínica) con zonas sombreadas y el punto del caso marcado; a la derecha,
    cómo se lee. d: x=(min, max, [(valor, rótulo)]), y=(min, max, [(valor, rótulo)]), eje_x, eje_y,
    series=[(nombre, [(x, y)...], color)], zonas=[(x0, x1, rótulo, color)], caso=(x, y, texto), notas=[(t, det, on)]."""
    y = section(s, y + 10, d["rotulo"])
    GW = d.get("ancho", 540)
    GH = d.get("alto", 300)
    notas = d.get("notas", [])
    x = X0 + GW + 22
    w = X1 - x
    meds = [_caja_txt(t, dd, w - 30) for t, dd, _ in notas]
    nh = sum(m[2] + 22 for m in meds) + 8 * max(0, len(meds) - 1)
    H = max(GH + 40, nh)
    s.rect(X0, y, GW, H, "#ffffff", LINE, 1.2, rx=12)
    L_, R_, T_, B_ = X0 + 58, X0 + GW - 18, y + 20, y + H - 48
    (xa, xb, xt), (ya, yb, yt) = d["x"], d["y"]
    px = lambda v: L_ + (v - xa) / (xb - xa) * (R_ - L_)
    py = lambda v: B_ - (v - ya) / (yb - ya) * (B_ - T_)
    for x0, x1, lab, col in d.get("zonas", []):
        s.rect(px(x0), T_, px(x1) - px(x0), B_ - T_, col, "none", 0, rx=0)
        s.text((px(x0) + px(x1)) / 2, T_ + 16, lab, 10.5, 800, SLATE, maxw=px(x1) - px(x0) - 6)
    for v, lab in yt:
        s.line(L_, py(v), R_, py(v), "#e2e8f0", 1)
        s.text(L_ - 8, py(v) + 4, lab, 10.5, 600, MUTED, "end", 50)
    for v, lab in xt:
        s.line(px(v), B_, px(v), B_ + 5, "#94a3b8", 1.5)
        s.text(px(v), B_ + 19, lab, 10.5, 600, MUTED, maxw=70)
    s.line(L_, B_, R_, B_, "#94a3b8", 1.5)
    s.line(L_, T_, L_, B_, "#94a3b8", 1.5)
    s.text((L_ + R_) / 2, B_ + 38, d.get("eje_x", ""), 11, 700, SLATE, maxw=R_ - L_)
    s.add(f'<text x="{X0 + 16:.1f}" y="{(T_ + B_) / 2:.1f}" transform="rotate(-90 {X0 + 16:.1f} {(T_ + B_) / 2:.1f})" '
          f'text-anchor="middle" font-size="11" font-weight="700" fill="{SLATE}">{d.get("eje_y", "")}</text>')
    ly = T_ + 34
    for nom, pts, col in d["series"]:
        s.add('<polyline points="' + " ".join(f"{px(a):.1f},{py(b):.1f}" for a, b in pts) +
              f'" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        if len(d["series"]) > 1:
            s.line(R_ - 150, ly, R_ - 128, ly, col, 3)
            s.text(R_ - 122, ly + 4, nom, 10.5, 700, col, "start", 120)
            ly += 18
    if d.get("caso"):
        cx, cy, ct = d["caso"]
        s.line(px(cx), py(cy), px(cx), B_, ORANGE, 2, "5 4")
        s.add(f'<circle cx="{px(cx):.1f}" cy="{py(cy):.1f}" r="9" fill="{ORANGE}" stroke="#ffffff" stroke-width="3"/>')
        case_chip(s, px(cx), py(cy) - 14, ct)
    cy = y + (H - nh) / 2
    for (t, dd, on), (tl, dl, th) in zip(notas, meds):
        h = th + 22
        s.rect(x, cy, w, h, ORANGE_L if on else "#f8fafc", ORANGE if on else LINE, 2 if on else 1.2, rx=10)
        _txt(s, x + 15, cy + 11, tl, dl, w - 30, on)
        cy += h + 8
    y += H
    if d.get("img"):
        from engine7 import banda
        y = banda(s, y + 12, d["img"])
    return _fin(s, y, d)


LAYOUTS9 = {"lectura": lectura, "zonas": zonas, "regla": regla, "decision": decision, "cuadricula": cuadricula,
            "alarma": alarma, "cascada": cascada, "checklist": checklist, "monitor": monitor, "piramide": piramide,
            "grados_foto": grados_foto, "laboratorio": laboratorio,
            "reloj": reloj, "transmision": transmision, "dosis": dosis, "ecg_mapa": ecg_mapa, "grafica": grafica}
