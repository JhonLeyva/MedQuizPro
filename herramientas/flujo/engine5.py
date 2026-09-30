"""Diseños 9-12 con ilustración propia del caso (bloque ENAM 2026).
Cada flujograma lleva un dibujo SVG hecho a mano que muestra el hallazgo del caso
(cuerpo con regla de los 9, pelvis con orificios herniarios, Rx de abdomen, ecografía…).
Diseños nuevos: calculo, anatomia, semaforo, cronologia."""
from engine import SVG, wrap, tw, header, perlas, escape, TEAL, TEAL_D, TEAL_L, TEAL_B, INK, SLATE, MUTED, LINE
from engine2 import top_row, table, X0, X1
from engine3 import section, case_chip, AMBER, AMBER_L, ROSE

ORANGE, ORANGE_L = "#ea580c", "#ffedd5"
SKIN, SKIN_D = "#fde7d4", "#e9b48f"
GREEN, GREEN_L = "#16a34a", "#dcfce7"
RED, RED_L = "#dc2626", "#fee2e2"


def panel(s, x, y, w, h, titulo):
    """Marco de la ilustración: título arriba y pie explicativo abajo."""
    s.rect(x, y, w, h, "#ffffff", LINE, 1.5, rx=12)
    s.rect(x + 12, y + 10, tw(titulo.upper(), 10, True) + 18, 20, TEAL_L, TEAL_B, 1, rx=10)
    s.text(x + 21, y + 24, titulo.upper(), 10, 800, TEAL, "start", 0)


def pie(s, x, y, w, h, texto):
    """Pie de la ilustración (se dibuja después del dibujo para que no quede tapado)."""
    if texto:
        pl = wrap(texto, w - 30, 11)
        s.rect(x + 8, y + h - 18 - len(pl) * 15, w - 16, len(pl) * 15 + 12, "#ffffff", "none", 0, rx=6)
        s.text(x + w / 2, y + h - 12 - (len(pl) - 1) * 15, pl, 11, 600, SLATE, maxw=w - 30, lh=15)


def lines_h(lines, w, fs=11.5, lh=16):
    return sum(len(wrap(l, w, fs)) for l in lines) * lh


def card(s, x, y, w, titulo, lines, on=False, color=TEAL, tag=None, fs=11.5):
    """Tarjeta con título; on=True la resalta como la del caso. Devuelve el alto."""
    tl = wrap(titulo, w - 28, 12.5, True)
    bl = []
    for l in lines:
        bl += wrap(l, w - 28, fs)
    h = 16 + len(tl) * 17 + (6 if bl else 0) + len(bl) * 16 + 14
    if on:
        s.rect(x, y, w, h, TEAL_L, TEAL, 2.2)
    else:
        s.rect(x, y, w, h, "#ffffff", LINE, 1.5)
    s.rect(x + 1, y + 1, 6, h - 2, color, rx=3)
    s.text(x + 18, y + 24, tl, 12.5, 800, TEAL_D if on else INK, "start", w - 28, lh=17)
    s.text(x + 18, y + 24 + len(tl) * 17 + 4, bl, fs, 400, SLATE, "start", w - 28, lh=16)
    if tag:
        case_chip(s, x + w - tw("◆ " + tag, 10, True) / 2 - 18, y, tag)
    return h


# ════════════════════════════════════════════════════════════ ILUSTRACIONES
def _g(s, x, y, sc, inner):
    s.add(f'<g transform="translate({x:.1f},{y:.1f}) scale({sc})">{inner}</g>')


def ilu_cuerpo_nueve(s, x, y, zonas):
    """Figura humana de frente con la regla de los 9 (valor de toda la región). zonas: partes quemadas del caso."""
    Z = lambda k: ORANGE if k in zonas else SKIN
    st = f'stroke="{SKIN_D}" stroke-width="2"'
    body = (
        f'<ellipse cx="150" cy="42" rx="30" ry="36" fill="{Z("cabeza")}" {st}/>'
        f'<rect x="140" y="74" width="20" height="14" fill="{SKIN}" {st}/>'
        f'<path d="M100 88 H200 L206 170 H94 Z" fill="{Z("torax")}" {st}/>'
        f'<path d="M94 170 H206 L200 250 H100 Z" fill="{Z("abdomen")}" {st}/>'
        f'<path d="M100 92 L70 100 L40 230 L60 236 L88 130 Z" fill="{Z("brazo_d")}" {st}/>'
        f'<path d="M200 92 L230 100 L260 230 L240 236 L212 130 Z" fill="{Z("brazo_i")}" {st}/>'
        f'<circle cx="46" cy="246" r="13" fill="{Z("brazo_d")}" {st}/><circle cx="254" cy="246" r="13" fill="{Z("brazo_i")}" {st}/>'
        f'<path d="M140 250 H160 L156 270 H144 Z" fill="{SKIN}" {st}/>'
        f'<path d="M100 250 H146 L142 360 H104 Z" fill="{Z("muslo_d")}" {st}/>'
        f'<path d="M154 250 H200 L196 360 H158 Z" fill="{Z("muslo_i")}" {st}/>'
        f'<path d="M104 360 H142 L138 470 H110 Z" fill="{Z("pierna_d")}" {st}/>'
        f'<path d="M158 360 H196 L190 470 H162 Z" fill="{Z("pierna_i")}" {st}/>'
        f'<ellipse cx="122" cy="478" rx="20" ry="9" fill="{SKIN}" {st}/><ellipse cx="178" cy="478" rx="20" ry="9" fill="{SKIN}" {st}/>'
    )
    def T(cx, cy, t, col, fs=13):
        return (f'<text x="{cx}" y="{cy}" font-size="{fs}" font-weight="800" fill="{col}" '
                f'text-anchor="middle" data-max="0">{escape(t)}</text>')
    dk, wt = "#7c2d12", "#ffffff"
    txt = (T(150, 47, "9 %", wt if "cabeza" in zonas else dk)
           + T(150, 134, "Tórax 9 %", wt if "torax" in zonas else dk, 12.5)
           + T(150, 214, "Abdomen 9 %", wt if "abdomen" in zonas else dk, 12.5)
           + T(18, 150, "9 %", dk) + T(282, 150, "9 %", dk)
           + '<path d="M156 262 L214 296" stroke="#7c2d12" stroke-width="1.5"/>' + T(246, 308, "Periné 1 %", dk, 11.5)
           + T(123, 420, "18 %", dk) + T(177, 420, "18 %", dk))
    # guías de los brazos (la etiqueta va afuera del brazo)
    txt += '<path d="M28 156 L52 170 M272 156 L248 170" stroke="#7c2d12" stroke-width="1.5"/>'
    _g(s, x, y, 0.72, body + txt)


def ilu_pelvis_hernias(s, x, y, marca):
    """Pelvis ósea de frente con los 4 orificios herniarios numerados; marca = número del caso."""
    bone, bone_d = "#f5efe2", "#a8977a"
    st = f'stroke="{bone_d}" stroke-width="2.5" stroke-linejoin="round"'
    p = (
        # ala ilíaca derecha del paciente (izquierda del dibujo) e izquierda
        f'<path d="M188 92 C160 60 120 40 78 52 C48 62 34 96 44 126 C52 150 70 168 86 186 L112 206 C130 180 160 160 190 150 Z" fill="{bone}" {st}/>'
        f'<path d="M252 92 C280 60 320 40 362 52 C392 62 406 96 396 126 C388 150 370 168 354 186 L328 206 C310 180 280 160 250 150 Z" fill="{bone}" {st}/>'
        # sacro y cóccix
        f'<path d="M186 88 H254 L246 170 C238 190 202 190 194 170 Z" fill="#ece3d0" {st}/>'
        + "".join(f'<path d="M{200+i*0} {104+i*18} H240" stroke="{bone_d}" stroke-width="1.5"/>' for i in range(4))
        # acetábulos
        + f'<circle cx="100" cy="214" r="24" fill="#ece3d0" {st}/><circle cx="340" cy="214" r="24" fill="#ece3d0" {st}/>'
        # anillo del pubis/isquion con agujero obturador (derecho e izquierdo)
        + f'<path d="M116 228 C140 212 176 214 206 236 L208 288 C188 300 150 306 124 288 C108 276 104 250 116 228 Z" fill="{bone}" {st}/>'
        + f'<path d="M324 228 C300 212 264 214 234 236 L232 288 C252 300 290 306 316 288 C332 276 336 250 324 228 Z" fill="{bone}" {st}/>'
        + f'<ellipse cx="158" cy="262" rx="30" ry="21" fill="#ffffff" {st}/>'
        + f'<ellipse cx="282" cy="262" rx="30" ry="21" fill="#ffffff" {st}/>'
        # sínfisis
        + f'<rect x="206" y="232" width="28" height="58" rx="8" fill="#e5d8bd" {st}/>'
        # ligamento inguinal: espina ilíaca anterosuperior → tubérculo púbico
        + '<path d="M50 132 Q120 200 204 238" fill="none" stroke="#0f766e" stroke-width="3" stroke-dasharray="7 4"/>'
        + '<path d="M390 132 Q320 200 236 238" fill="none" stroke="#0f766e" stroke-width="3" stroke-dasharray="7 4"/>'
        # vasos femorales derechos: pasan por debajo del ligamento hacia el muslo
        + '<path d="M112 176 L106 330" stroke="#dc2626" stroke-width="7" fill="none" stroke-linecap="round"/>'
        + '<path d="M128 184 L124 330" stroke="#2563eb" stroke-width="7" fill="none" stroke-linecap="round"/>'
        # nervio obturador: pared pélvica → canal obturador → cara interna del muslo
        + '<path d="M196 170 C184 200 168 230 150 246 C146 280 160 310 176 334" stroke="#eab308" stroke-width="4" fill="none" stroke-linecap="round"/>'
    )
    pts = {1: (80, 160), 2: (150, 196), 3: (144, 226), 4: (150, 250)}
    for n, (cx, cy) in pts.items():
        on = n == marca
        p += (f'<circle cx="{cx}" cy="{cy}" r="{15 if on else 12}" fill="{ORANGE if on else "#ffffff"}" '
              f'stroke="{ORANGE if on else "#334155"}" stroke-width="2.5"/>'
              f'<text x="{cx}" y="{cy+5}" font-size="14" font-weight="800" fill="{"#ffffff" if on else "#0f172a"}" '
              f'text-anchor="middle" data-max="0">{n}</text>')
    p += ('<text x="20" y="14" font-size="12.5" font-weight="700" fill="#0f766e" data-max="0">- - Ligamento inguinal</text>'
          '<text x="250" y="14" font-size="12.5" font-weight="700" fill="#a16207" data-max="0">— Nervio obturador</text>'
          '<text x="20" y="34" font-size="12.5" font-weight="700" fill="#b91c1c" data-max="0">Rojo y azul: arteria y vena femorales (lado derecho)</text>')
    _g(s, x, y, 0.95, p)


def ilu_rx_volvulo(s, x, y):
    """Rx simple de abdomen con asa sigmoidea dilatada en «grano de café» que apunta al hipocondrio derecho."""
    p = (
        '<rect x="0" y="0" width="300" height="330" rx="10" fill="#111827"/>'
        # columna lumbar
        + "".join(f'<rect x="138" y="{18+i*28}" width="24" height="22" rx="4" fill="#4b5563"/>' for i in range(9))
        # pelvis ósea
        + '<path d="M36 272 C58 232 110 250 140 292 M264 272 C242 232 190 250 160 292" stroke="#9ca3af" stroke-width="10" fill="none"/>'
        # marco colónico dilatado con haustras
        + '<path d="M250 250 C272 190 270 110 240 62 C200 30 110 30 70 60 C40 100 36 190 56 250" stroke="#374151" stroke-width="24" fill="none"/>'
        # grano de café: dos asas dilatadas pegadas, vértice hacia arriba y a la derecha (hipocondrio derecho del paciente = izquierda de la imagen)
        + '<g transform="rotate(-22 150 180)">'
        + '<path d="M150 292 C70 262 58 110 138 70 C150 64 162 64 172 70 C246 118 232 262 158 292 Z" fill="#e5e7eb" stroke="#f9fafb" stroke-width="4" opacity="0.93"/>'
        + '<path d="M154 290 C140 220 142 140 154 72" stroke="#6b7280" stroke-width="6" fill="none"/>'
        + '</g>'
        + '<text x="150" y="320" font-size="13" font-weight="800" fill="#fbbf24" text-anchor="middle" data-max="0">«Grano de café»</text>'
        + '<text x="14" y="24" font-size="12" font-weight="800" fill="#9ca3af" data-max="0">D</text>'
    )
    _g(s, x, y, 0.9, p)


def ilu_eco_tn(s, x, y):
    """Ecografía de 12 semanas: feto de perfil con la translucencia nucal (TN) medida en la nuca."""
    p = (
        '<defs><clipPath id="ecoclip"><rect x="0" y="0" width="330" height="270" rx="10"/></clipPath></defs>'
        '<rect x="0" y="0" width="330" height="270" rx="10" fill="#0b0f19"/>'
        '<g clip-path="url(#ecoclip)"><path d="M165 6 L10 262 Q165 300 320 262 Z" fill="#1f2937"/>'
        # saco / líquido amniótico
        '<ellipse cx="165" cy="170" rx="125" ry="70" fill="#0b0f19" stroke="#6b7280" stroke-width="3"/>'
        # feto de perfil (cabeza a la izquierda, espalda arriba)
        '<circle cx="100" cy="168" r="38" fill="#9ca3af"/>'
        '<path d="M130 150 C170 138 220 146 246 168 C252 184 236 200 206 202 C176 204 146 196 132 186 Z" fill="#9ca3af"/>'
        '<path d="M240 190 C258 196 266 208 258 220" stroke="#9ca3af" stroke-width="10" fill="none" stroke-linecap="round"/>'
        '<path d="M70 176 C74 188 84 194 94 192" stroke="#d1d5db" stroke-width="3" fill="none"/>'
        # piel de la nuca (línea brillante) separada por el espacio oscuro = TN
        '<path d="M118 124 C132 118 150 120 164 130" stroke="#f3f4f6" stroke-width="3" fill="none"/>'
        '<path d="M120 142 C134 134 150 136 162 144" stroke="#d1d5db" stroke-width="3" fill="none"/>'
        '<path d="M119 133 C133 126 150 128 163 137" stroke="#0b0f19" stroke-width="10" fill="none"/>'
        # calibradores de la medida
        '<text x="140" y="124" font-size="15" font-weight="800" fill="#fde047" text-anchor="middle" data-max="0">+</text>'
        '<text x="140" y="146" font-size="15" font-weight="800" fill="#fde047" text-anchor="middle" data-max="0">+</text>'
        '<path d="M150 118 L200 78" stroke="#fde047" stroke-width="2"/></g>'
        '<text x="204" y="74" font-size="14" font-weight="800" fill="#fde047" data-max="0">TN &gt; p95</text>'
        '<text x="14" y="22" font-size="11" font-weight="700" fill="#9ca3af" data-max="0">12 sem · corte sagital</text>'
    )
    _g(s, x, y, 1.0, p)


# ════════════════════════════════════════════════════════════ DISEÑO 9: CÁLCULO
def calculo(s, y, d):
    """Ilustración a la izquierda + pasos de la fórmula a la derecha + reparto en el tiempo."""
    y = section(s, y + 10, d["rotulo"])
    PW, PH = 250, 470
    panel(s, X0, y, PW, PH, d["ilu_titulo"])
    d["ilu"](s, X0 + 16, y + 40)
    pie(s, X0, y, PW, PH, d.get("ilu_pie"))
    x, w = X0 + PW + 20, X1 - (X0 + PW + 20)
    cy = y
    for i, (tit, lines, on) in enumerate(d["pasos"]):
        s.circle(x + 16, cy + 22, 14, TEAL if on else "#e2e8f0")
        s.text(x + 16, cy + 27, str(i + 1), 13, 800, "#ffffff" if on else "#334155", maxw=0)
        h = card(s, x + 40, cy, w - 40, tit, lines, on=on, color=AMBER if on else TEAL,
                 tag=d.get("tag") if on else None)
        cy += h + 12
    # barra de reparto en 24 h
    if d.get("reparto"):
        cy += 6
        s.text(x, cy + 12, d["reparto"]["titulo"].upper(), 11, 800, MUTED, "start", w)
        cy += 22
        tot = sum(r[1] for r in d["reparto"]["tramos"])
        bx = x
        for lab, hrs, vol, col in d["reparto"]["tramos"]:
            bw = w * hrs / tot
            s.rect(bx, cy, bw - 4, 40, col, rx=8)
            s.text(bx + bw / 2 - 2, cy + 18, vol, 13, 800, "#ffffff", maxw=bw - 16)
            s.text(bx + bw / 2 - 2, cy + 33, lab, 10.5, 600, "#ffffff", maxw=bw - 16)
            bx += bw
        cy += 52
    return max(y + PH, cy) + 4


# ════════════════════════════════════════════════════════════ DISEÑO 10: ANATOMÍA
def anatomia(s, y, d):
    """Mapa anatómico numerado + tarjetas que explican cada punto; la del caso resaltada."""
    y = section(s, y + 10, d["rotulo"])
    PW, PH = 440, 400
    panel(s, X0, y, PW, PH, d["ilu_titulo"])
    d["ilu"](s, X0 + 12, y + 34)
    pie(s, X0, y, PW, PH, d.get("ilu_pie"))
    x, w = X0 + PW + 20, X1 - (X0 + PW + 20)
    cy = y
    for n, (tit, lines) in enumerate(d["puntos"], 1):
        on = n == d["ans"]
        h = card(s, x, cy, w, f"{n}. {tit}", lines, on=on, color=ORANGE if on else "#94a3b8", tag=d.get("tag") if on else None, fs=11)
        cy += h + 10
    y = max(y + PH, cy) + 14
    if d.get("signo"):
        sg = d["signo"]
        bl = []
        for l in sg["lines"]:
            bl += wrap(l, 900 - 200, 11.5)
        h = max(78, 30 + len(bl) * 16 + 14)
        s.rect(X0, y, X1 - X0, h, AMBER_L, AMBER, 1.5, rx=12)
        s.text(X0 + 20, y + 26, sg["titulo"], 13, 800, "#92400e", "start", 700)
        s.text(X0 + 20, y + 46, bl, 11.5, 500, "#78350f", "start", 700, lh=16)
        # mini muslo con zona de dolor (solo si se pide)
        mx = X1 - 210
        if sg.get("muslo"):
          s.add(f'<g transform="translate({mx},{y+8})">'
              f'<path d="M20 4 H80 L72 {h-18} H34 Z" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="2"/>'
              f'<path d="M24 14 Q30 {h/2} 38 {h-20}" stroke="#eab308" stroke-width="3" fill="none"/>'
              f'<ellipse cx="34" cy="{h/2}" rx="10" ry="{h/4:.0f}" fill="{ORANGE}" opacity="0.55"/>'
              f'<text x="100" y="{h/2+4:.0f}" font-size="11" font-weight="700" fill="#9a3412" data-max="0">dolor medial</text></g>')
        y += h
    return y


# ════════════════════════════════════════════════════════════ DISEÑO 11: SEMÁFORO
def semaforo(s, y, d):
    """Imagen diagnóstica + chequeo de datos del caso + semáforo verde/ámbar/rojo con la conducta."""
    y = section(s, y + 10, d["rotulo"])
    PW, PH = 310, 400
    panel(s, X0, y, PW, PH, d["ilu_titulo"])
    d["ilu"](s, X0 + (PW - 270) / 2, y + 36)
    pie(s, X0, y, PW, PH, d.get("ilu_pie"))
    x, w = X0 + PW + 20, X1 - (X0 + PW + 20)
    # chequeo de datos
    s.text(x, y + 12, d["check_titulo"].upper(), 11, 800, MUTED, "start", w)
    cy = y + 22
    for txt, ok in d["check"]:
        s.rect(x, cy, w, 28, "#ffffff" if ok else "#fff1f2", LINE if ok else "#fda4af", 1.2, rx=8)
        s.circle(x + 16, cy + 14, 9, GREEN if ok else RED)
        s.text(x + 16, cy + 18.5, "✓" if ok else "!", 11, 800, "#ffffff", maxw=0)
        s.text(x + 34, cy + 18.5, txt, 11.5, 500, "#334155", "start", w - 44)
        cy += 32
    cy += 10
    cols = [(GREEN, GREEN_L), (AMBER, AMBER_L), (RED, RED_L)]
    for i, (tit, cond, cond_l) in enumerate(d["luces"]):
        c, cl = cols[i]
        on = i == d["ans"]
        ll = []
        for l in cond_l:
            ll += wrap(l, w - 90, 11)
        h = max(64, 22 + 17 + len(ll) * 15 + 12)
        s.rect(x, cy, w, h, cl if on else "#ffffff", c if on else LINE, 2.2 if on else 1.3, rx=12)
        s.circle(x + 30, cy + h / 2, 17, c)
        s.circle(x + 30, cy + h / 2, 7, "#ffffff")
        s.text(x + 60, cy + 22, tit, 12.5, 800, INK, "start", w - 90)
        s.text(x + 60, cy + 39, cond, 11.5, 700, c, "start", w - 90)
        s.text(x + 60, cy + 55, ll, 11, 400, SLATE, "start", w - 90, lh=15)
        if on:
            case_chip(s, x + w - 60, cy, d.get("tag", "ESTE CASO"))
        cy += h + 8
    return max(y + PH, cy) + 4


# ════════════════════════════════════════════════════════════ DISEÑO 12: CRONOLOGÍA
def cronologia(s, y, d):
    """Imagen del hallazgo + línea de tiempo en semanas con cada prueba y lo que detecta."""
    y = section(s, y + 10, d["rotulo"])
    PW, PH = 350, 350
    panel(s, X0, y, PW, PH, d["ilu_titulo"])
    d["ilu"](s, X0 + 10, y + 36)
    pie(s, X0, y, PW, PH, d.get("ilu_pie"))
    x, w = X0 + PW + 20, X1 - (X0 + PW + 20)
    cy = y
    for tit, lines, on in d["claves"]:
        h = card(s, x, cy, w, tit, lines, on=on, color=AMBER if on else TEAL, tag=d.get("tag") if on else None, fs=11)
        cy += h + 10
    y = max(y + PH, cy) + 22
    # eje de semanas: nombres en columna fija a la izquierda y barra en la misma fila (tipo Gantt)
    a, b = d["eje"]
    LW = 290                                   # ancho de la columna de nombres
    ax0, ax1 = X0 + LW + 20, X1 - 16
    sx = lambda wk: ax0 + (wk - a) / (b - a) * (ax1 - ax0)
    s.text(X0, y + 12, d["eje_titulo"].upper(), 11, 800, MUTED, "start", 900)
    y += 50
    rows = d["hitos"]
    RH = 36
    base = y + len(rows) * RH + 4
    # guías verticales de semanas
    for wk in range(a, b + 1, d.get("paso", 4)):
        s.line(sx(wk), y - 6, sx(wk), base, "#e2e8f0", 1)
    for i, (w0, w1, lab, sub, on) in enumerate(rows):
        ry = y + i * RH
        if on:
            s.rect(X0, ry - 2, X1 - X0, RH - 4, TEAL_L, "none", 0, rx=8)
        s.text(X0 + 10, ry + 13, lab, 11.5, 800, TEAL_D if on else INK, "start", LW - 16)
        s.text(X0 + 10, ry + 27, sub, 10.5, 600, TEAL if on else MUTED, "start", LW - 16)
        x0, x1 = sx(w0), sx(w1)
        s.rect(x0, ry + 5, max(x1 - x0, 8), 20, TEAL if on else "#94a3b8", "none", 0, rx=10)
        rng = f"{w0}-{w1} {d.get('unidad', 'sem')}"
        if tw(rng, 10, True) + 14 < x1 - x0:
            s.text((x0 + x1) / 2, ry + 19, rng, 10, 700, "#ffffff", maxw=x1 - x0 - 8)
        else:
            s.text(x1 + 6, ry + 19, rng, 10, 700, TEAL_D if on else MUTED, "start", 80)
        s.line(X0 + LW, ry + 15, x0 - 4, ry + 15, "#cbd5e1", 1, "2 4")
    s.line(ax0, base, ax1, base, "#94a3b8", 1.5)
    for wk in range(a, b + 1, d.get("paso", 4)):
        s.line(sx(wk), base - 4, sx(wk), base + 4, "#94a3b8", 1.5)
        s.text(sx(wk), base + 18, str(wk), 10.5, 600, MUTED, maxw=0)
    s.text(ax1, base + 34, d.get("eje_nombre", "semanas de gestación"), 10.5, 600, MUTED, "end", 300)
    if d.get("marca"):
        mx = sx(d["marca"])
        s.line(mx, y - 8, mx, base, ORANGE, 2, "5 4")
        case_chip(s, mx, y - 14, d.get("tag", "ESTE CASO"))
    return base + 40


LAYOUTS5 = {"calculo": calculo, "anatomia": anatomia, "semaforo": semaforo, "cronologia": cronologia}


def build5(spec):
    s = SVG()
    y = header(s, spec["barra"], spec["esp"])
    y, _ = top_row(s, y, spec["tema"], spec["caso"], "Marca dónde cae este caso", "rombo")
    y = LAYOUTS5[spec["tipo"]](s, y + 8, spec["d"])
    if spec.get("tabla"):
        y = table(s, y + 24, spec["tabla"])
    y = perlas(s, y + 24, spec["perlas"], spec["fuente"])
    H = y + 18
    t = escape(spec["titulo"])
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H:.0f}" '
            f'viewBox="0 0 1000 {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" role="img" '
            f'aria-label="{t}"><title>{t}</title>'
            f'<rect x="0.75" y="0.75" width="998.5" height="{H-1.5:.1f}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>')
    return head + "".join(s.p) + "</svg>"
