"""Biblioteca de dibujos propios para los flujogramas del bloque ENAM 2026.
Cada función dibuja en coordenadas locales (lienzo indicado) y se ubica con translate/scale.
Colores suaves por órgano; lo que importa en el caso va en naranja y con número o rótulo."""
import math
from xml.sax.saxutils import escape

ORANGE, ORANGE_L = "#ea580c", "#ffedd5"
INK, SLATE, MUTED = "#0f172a", "#334155", "#64748b"
TEAL, TEAL_D = "#0f766e", "#134e4a"
SKIN, SKIN_D = "#fde7d4", "#e9b48f"
RED, BLUE, YEL, GREEN, VIOLET = "#dc2626", "#2563eb", "#eab308", "#16a34a", "#7c3aed"
ORG = {"higado": "#e7a882", "vesicula": "#86efac", "estomago": "#fbcfe8", "bazo": "#c4b5fd", "pancreas": "#fde68a",
       "duodeno": "#fbcfe8", "colon": "#fed7aa", "delgado": "#fecdd3", "apendice": "#fed7aa", "vejiga": "#fef9c3",
       "rinon": "#fca5a5"}
STK = "#9a6b52"


def g(s, x, y, inner, sc=1.0):
    s.add(f'<g transform="translate({x:.1f},{y:.1f}) scale({sc})">{inner}</g>')


def t(x, y, txt, col=INK, fs=11, anchor="middle", fw=800, halo=True):
    """Rótulo sin control de ancho (dentro del dibujo). Con halo blanco para que se lea sobre el dibujo."""
    h = (f'<text x="{x}" y="{y}" font-size="{fs}" font-weight="{fw}" fill="none" stroke="#ffffff" stroke-width="3" '
         f'stroke-linejoin="round" text-anchor="{anchor}" data-max="0">{escape(txt)}</text>') if halo else ""
    return h + (f'<text x="{x}" y="{y}" font-size="{fs}" font-weight="{fw}" fill="{col}" text-anchor="{anchor}" '
                f'data-max="0">{escape(txt)}</text>')


def tl(x, y, lines, col=INK, fs=11, anchor="middle", fw=800, lh=None, halo=True):
    lh = lh or fs * 1.3
    return "".join(t(x, y + i * lh, l, col, fs, anchor, fw, halo) for i, l in enumerate(lines))


def num(x, y, n, col=ORANGE, r=10):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#ffffff" stroke-width="2"/>'
            + t(x, y + 4, str(n), "#ffffff", 11.5 if r >= 10 else 10, halo=False))


def flecha(x1, y1, x2, y2, col=ORANGE, sw=2.2, dash=None):
    a = math.atan2(y2 - y1, x2 - x1)
    xe, ye = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = [(x2, y2), (x2 - 10 * math.cos(a - 0.45), y2 - 10 * math.sin(a - 0.45)), (x2 - 10 * math.cos(a + 0.45), y2 - 10 * math.sin(a + 0.45))]
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{xe:.1f}" y2="{ye:.1f}" stroke="{col}" stroke-width="{sw}"{d}/>'
            f'<polygon points="{" ".join(f"{u:.1f},{v:.1f}" for u, v in p)}" fill="{col}"/>')


def guia(x1, y1, x2, y2, col=SLATE):
    """Línea de guía fina de un rótulo a su estructura, con punto en la estructura."""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.3"/>'
            f'<circle cx="{x2}" cy="{y2}" r="2.6" fill="{col}"/>')


def P(d, fill, stroke=STK, sw=1.8, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" {extra}/>'


def E(cx, cy, rx, ry, fill, stroke=STK, sw=1.8, rot=0, extra=""):
    tr = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{tr} {extra}/>'


def C(cx, cy, r, fill, stroke=STK, sw=1.8, extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def piedra(cx, cy, r=5, col="#78716c"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="#44403c" stroke-width="1.2"/>'


def burbujas(pts, r=3.2):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#111827" stroke="#ffffff" stroke-width="0.8"/>' for x, y in pts)


# ════════════════════════════════════════════════════════════ ABDOMEN (lienzo 300×330)
def abdomen(s, x, y, on=(), marcas=(), extra="", rotulos=(), sc=1.0, sin_delgado=False):
    """Abdomen de frente con los órganos. Derecha del paciente = izquierda del dibujo.
    on: órganos resaltados (higado, vesicula, estomago, bazo, pancreas, duodeno, colon_asc, colon_trans,
    colon_desc, sigmoides, ciego, apendice, delgado, ileon, vejiga). marcas: (n, x, y).
    rotulos: (x, y, texto, anchor) con halo."""
    f = lambda k, base: ORANGE if k in on else ORG.get(base, base)
    p = (P("M18 16 Q150 -6 282 16 L292 300 Q150 334 8 300 Z", SKIN, SKIN_D, 2)
         + '<path d="M28 40 Q150 10 272 40" fill="none" stroke="#d6a684" stroke-width="1.5" stroke-dasharray="4 4"/>'
         # hígado (derecha del paciente) y vesícula
         + P("M24 42 C60 20 176 22 188 42 L182 66 C150 92 86 110 26 112 Z", f("higado", "higado"))
         + E(112, 104, 11, 17, f("vesicula", "vesicula"), rot=-20)
         # estómago y bazo
         + P("M178 44 C214 30 256 46 254 84 C252 116 222 132 190 128 C178 126 172 116 180 110 C204 110 222 98 220 80 C218 62 200 58 184 64 Z", f("estomago", "estomago"))
         + E(266, 78, 14, 30, f("bazo", "bazo"), rot=12)
         # duodeno (C) y páncreas
         + P("M150 118 C124 116 116 142 124 160 C132 176 158 176 170 168", "none", f("duodeno", "#e879a0"), 9, 'stroke-linecap="round"')
         + P("M150 136 C176 124 214 122 246 116 C252 124 246 132 238 134 C206 140 178 146 156 150 Z", f("pancreas", "pancreas"))
         # marco colónico
         + P("M58 262 L52 170", "none", f("colon_asc", "colon"), 14, 'stroke-linecap="round"')
         + P("M60 148 L240 146", "none", f("colon_trans", "colon"), 14, 'stroke-linecap="round"')
         + P("M250 160 L250 246", "none", f("colon_desc", "colon"), 14, 'stroke-linecap="round"')
         + P("M250 246 C250 268 226 286 196 286 C176 286 170 272 160 276", "none", f("sigmoides", "colon"), 14, 'stroke-linecap="round"')
         + E(60, 270, 15, 13, f("ciego", "colon"))
         + P("M58 282 C56 296 66 304 74 300", "none", f("apendice", "#f59e0b"), 7, 'stroke-linecap="round"'))
    if not sin_delgado:
        p += P("M92 180 C120 166 150 196 178 176 C206 158 226 190 206 206 C182 222 150 196 126 214 C104 230 136 248 162 236 "
               "C190 224 220 240 206 258 C190 272 150 250 120 262 C102 268 84 262 76 266",
               "none", f("delgado", "delgado"), 11, 'stroke-linecap="round"')
        p += P("M92 262 C84 264 78 266 72 268", "none", f("ileon", "delgado"), 11, 'stroke-linecap="round"')
    p += E(150, 306, 22, 12, f("vejiga", "vejiga"))
    p += extra
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    p += t(10, 12, "D", MUTED, 11, "start", halo=False) + t(290, 12, "I", MUTED, 11, "end", halo=False)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ VÍA BILIAR Y PÁNCREAS (lienzo 320×260)
def via_biliar(s, x, y, calculos=(), vesicula="normal", fistula=False, aire=False, coledoco_dilatado=False,
               pancreas="normal", rotulos=(), marcas=(), extra="", sc=1.0, color_calc="#78716c"):
    """Hígado, vesícula, cístico, colédoco, conducto pancreático y duodeno.
    calculos: 'vesicula', 'cistico', 'coledoco', 'ampolla'. vesicula: normal|inflamada|distendida.
    pancreas: normal|inflamado."""
    vfill = {"normal": ORG["vesicula"], "inflamada": "#fca5a5", "distendida": "#86efac"}[vesicula]
    vst = RED if vesicula == "inflamada" else STK
    vw = 4 if vesicula == "inflamada" else 1.8
    cw = 11 if coledoco_dilatado else 7
    p = (P("M10 20 C60 0 250 4 300 24 C306 50 262 76 206 86 C150 96 110 104 70 112 C36 116 8 92 10 20 Z", ORG["higado"])
         + t(160, 44, "Hígado", "#7c2d12", 11)
         # conductos hepáticos y colédoco
         + P("M150 70 L158 110 M186 72 L166 110 M162 108 L162 150", "none", "#15803d", cw, 'stroke-linecap="round"')
         + P("M162 150 C162 176 170 196 186 212", "none", "#15803d", cw, 'stroke-linecap="round"')
         # vesícula y cístico
         + P("M162 124 C140 128 128 138 118 146", "none", "#15803d", 6, 'stroke-linecap="round"')
         + P("M120 140 C92 140 62 160 58 186 C56 206 74 214 92 204 C112 190 126 166 124 146 Z", vfill, vst, vw)
         # duodeno en C y páncreas
         + P("M150 170 C150 200 162 238 204 242 C242 244 250 218 246 196", "none", "#f9a8d4", 22, 'stroke-linecap="round"')
         + P("M200 206 C232 196 272 188 310 182 C314 196 306 206 296 208 C262 214 232 222 204 226 Z",
             "#fdba74" if pancreas == "inflamado" else ORG["pancreas"], ORANGE if pancreas == "inflamado" else STK,
             3 if pancreas == "inflamado" else 1.8)
         + P("M306 196 C270 200 232 206 192 212", "none", "#a16207", 3)
         + C(188, 214, 5, "#f472b6", "#9d174d", 1.5))
    if pancreas == "inflamado":
        p += "".join(f'<path d="M{206+i*20} 232 q4 7 0 13" fill="none" stroke="{ORANGE}" stroke-width="2"/>' for i in range(5))
    pos = {"vesicula": [(80, 186), (92, 178), (74, 176)], "cistico": [(126, 142)], "coledoco": [(162, 164), (164, 178)],
           "ampolla": [(186, 208)]}
    for c in calculos:
        for (cx, cy) in pos[c]:
            p += piedra(cx, cy, 6 if c != "ampolla" else 5, color_calc)
    if fistula:
        p += P("M86 206 C98 226 128 232 152 222", "none", ORANGE, 4, 'stroke-dasharray="5 4"')
    if aire:
        p += burbujas([(154, 88), (172, 90), (160, 128), (162, 142)], 3)
    p += extra
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    g(s, x, y, p, sc)


def pancreas_col(s, x, y, tipo="edema", rotulos=(), marcas=(), sc=1.0):
    """Corte del abdomen superior: estómago delante, páncreas detrás y la colección según Atlanta.
    tipo: edema | aguda | seudoquiste | necrosis | necrosis_gas (lienzo 320×220)."""
    p = (P("M10 30 Q160 -10 310 30 L310 200 Q160 230 10 200 Z", SKIN, SKIN_D, 2)
         + P("M70 40 C120 20 220 20 262 46 C280 70 262 92 220 92 C170 92 120 96 86 86 C62 78 56 54 70 40 Z", ORG["estomago"])
         + t(166, 64, "Estómago", "#9d174d", 10.5)
         + E(160, 196, 16, 12, "#e2e8f0", "#64748b") + t(160, 200, "col.", MUTED, 9, halo=False)
         + P("M40 150 C80 130 150 130 200 132 C240 134 272 128 290 118 C300 132 292 148 272 152 C230 160 150 162 90 170 C60 174 36 166 40 150 Z",
             "#fdba74" if tipo != "normal" else ORG["pancreas"], ORANGE if tipo == "edema" else STK, 2))
    p += t(100, 168, "Páncreas", "#92400e", 10.5)
    if tipo == "aguda":
        p += P("M120 100 C150 96 200 98 232 104 C226 124 180 126 140 124 C120 122 112 112 120 100 Z", "#bae6fd", "#7dd3fc", 1, 'opacity="0.9"')
    elif tipo == "seudoquiste":
        p += C(170, 110, 30, "#bae6fd", "#0369a1", 5)
    elif tipo in ("necrosis", "necrosis_gas"):
        p += P("M126 96 C160 86 214 92 236 110 C240 132 206 142 170 140 C136 138 116 124 126 96 Z", "#a8a29e", "#57534e", 3)
        p += "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#78716c" opacity="0.7"/>' for cx, cy, r in
                     [(150, 112, 7), (184, 120, 9), (212, 110, 6), (170, 102, 5)])
        if tipo == "necrosis_gas":
            p += burbujas([(144, 104), (160, 120), (196, 106), (220, 120), (178, 132), (206, 128)], 4)
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CAPAS DE LA PARED (lienzo 330×250)
CAPAS_EST = [("Mucosa", "#f9a8d4", 30), ("Muscular de la mucosa", "#f472b6", 8), ("Submucosa", "#fde68a", 36),
             ("Muscular propia", "#fca5a5", 52), ("Subserosa", "#fef3c7", 20), ("Serosa", "#a7f3d0", 10)]
CAPAS_ESO = [("Mucosa (Barrett)", "#fdba74", 30), ("Muscular de la mucosa", "#f472b6", 8), ("Submucosa", "#fde68a", 40),
             ("Muscular propia", "#fca5a5", 58), ("Adventicia (sin serosa)", "#e2e8f0", 24)]


def pared_capas(s, x, y, capas=CAPAS_EST, invade=None, etiquetas_t=None, sonda=False, sc=1.0, titulo=None):
    """Corte de la pared con sus capas y el tumor que llega hasta la capa 'invade' (índice)."""
    X, W = 20, 170
    p = ""
    yy = 30
    lims = []
    for i, (nom, col, h) in enumerate(capas):
        p += f'<rect x="{X}" y="{yy}" width="{W}" height="{h}" fill="{col}" stroke="#ffffff" stroke-width="1"/>'
        p += t(X + W + 10, yy + h / 2 + 4, nom, SLATE, 10.5, "start", 700)
        lims.append((yy, yy + h))
        yy += h
    p += t(X - 16 if sonda else X, 22 if not sonda else 12, "Luz del órgano", MUTED, 10, "start", halo=False)
    if titulo:
        p += t(X + W + 10, 22, titulo, TEAL_D, 11, "start")
    if invade is not None:
        bot = lims[invade][1] - (2 if invade < len(capas) - 1 else 0)
        p += P(f"M{X+44} 26 C{X+40} 60 {X+50} {bot-10} {X+78} {bot} C{X+104} {bot-6} {X+118} 60 {X+112} 26 Z",
               ORANGE, "#9a3412", 2, 'opacity="0.9"')
        p += t(X + 78, 22, "Tumor", "#9a3412", 10.5) if sonda else t(X + 118, 22, "Tumor", "#9a3412", 10.5, "start")
    if etiquetas_t:
        for i, lab in etiquetas_t:
            a, b = lims[i]
            p += f'<line x1="{X-4}" y1="{a+2}" x2="{X-4}" y2="{b-2}" stroke="{TEAL}" stroke-width="3"/>'
            p += t(X - 8, (a + b) / 2 + 4, lab, TEAL_D, 10, "end")
    if sonda:
        p += P(f"M{X+158} 4 L{X+158} 22", "none", "#334155", 8, 'stroke-linecap="round"')
        p += "".join(f'<path d="M{X+146-k*6} {30+k*9} Q{X+158} {36+k*10} {X+170+k*6} {30+k*9}" fill="none" stroke="#0ea5e9" stroke-width="1.6"/>' for k in range(4))
        p += t(X + 172, 12, "sonda de ultrasonido", "#0369a1", 10, "start")
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ BARRAS DE LABORATORIO
def lab_barras(s, x, y, items, W=320, xmax=10, titulo="Veces el valor normal", sc=1.0):
    """items: (nombre, valor, veces, on). Barra horizontal con línea en 1× (límite normal)."""
    LW = 118
    bw = W - LW - 10
    p = t(LW, 12, titulo, MUTED, 10, "start", 700, halo=False)
    for i, (nom, val, veces, on) in enumerate(items):
        yy = 24 + i * 34
        w = min(veces, xmax) / xmax * bw
        p += t(LW - 8, yy + 15, nom, INK if on else SLATE, 11, "end", 800 if on else 600, halo=False)
        p += f'<rect x="{LW}" y="{yy}" width="{bw}" height="22" rx="4" fill="#f1f5f9"/>'
        p += f'<rect x="{LW}" y="{yy}" width="{max(w,3):.1f}" height="22" rx="4" fill="{ORANGE if on else "#94a3b8"}"/>'
        p += t(LW + max(w, 3) + 6 if w < bw - 60 else LW + w - 6, yy + 15, val, INK if w < bw - 60 else "#ffffff", 10.5,
               "start" if w < bw - 60 else "end", 800, halo=False)
    x1 = LW + bw / xmax
    hh = 24 + len(items) * 34
    p += f'<line x1="{x1:.1f}" y1="20" x2="{x1:.1f}" y2="{hh}" stroke="{TEAL}" stroke-width="2" stroke-dasharray="4 3"/>'
    p += t(x1, hh + 12, "normal", TEAL, 10, halo=False)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CUERPO ADULTO DE FRENTE (lienzo 240×440)
_ZC = {"cara": "C120 40 28", "cuello": "M110 66 H130 V80 H110 Z", "torax": "M70 80 H170 L176 170 H64 Z",
       "abdomen": "M64 170 H176 L170 240 H70 Z", "pelvis": "M70 240 H170 L164 268 H76 Z",
       "brazo_d": "M70 84 L50 92 L36 170 L54 174 L66 120 Z", "antebrazo_d": "M36 170 L54 174 L46 238 L28 236 Z",
       "mano_d": "E37 250 10 15", "muslo_d": "M76 268 H118 L114 360 H84 Z", "pierna_d": "M84 360 H114 L108 418 H90 Z",
       "pie_d": "E98 426 15 7"}


def _mir(d):
    """Refleja una zona del lado derecho del paciente (izquierda del dibujo) al otro lado."""
    if d.startswith("E"):
        cx, cy, rx, ry = map(float, d[1:].split())
        return f"E{240-cx} {cy} {rx} {ry}"
    out = []
    for tok in d.split():
        if tok[0] in "MLHVZ":
            c, rest = tok[0], tok[1:]
            if c == "H":
                out.append("H" + str(240 - float(rest)))
            elif c in "ML":
                out.append(c + str(240 - float(rest)))
            else:
                out.append(tok)
        else:
            out.append(tok)
    return " ".join(out)


for _k in list(_ZC):
    if _k.endswith("_d"):
        _ZC[_k[:-2] + "_i"] = _mir(_ZC[_k])


def _zona(d, fill, stroke=SKIN_D):
    if d.startswith("C"):
        cx, cy, r = d[1:].split()
        return C(cx, cy, r, fill, stroke, 2)
    if d.startswith("E"):
        cx, cy, rx, ry = d[1:].split()
        return E(cx, cy, rx, ry, fill, stroke, 2)
    return P(d, fill, stroke, 2)


def cuerpo(s, x, y, zonas=None, marcas=(), extra="", rotulos=(), sc=1.0, pre=""):
    """Adulto de frente. zonas: {zona: color}. Zonas: cara, cuello, torax, abdomen, pelvis, brazo_d/i,
    antebrazo_d/i, mano_d/i, muslo_d/i, pierna_d/i, pie_d/i (d = derecha del paciente = izquierda del dibujo)."""
    zonas = zonas or {}
    p = pre
    for k, d in _ZC.items():
        p += _zona(d, zonas.get(k, SKIN))
    p += (C(110, 36, 3, "#334155", "none", 0) + C(130, 36, 3, "#334155", "none", 0)
          + '<path d="M112 52 Q120 57 128 52" fill="none" stroke="#9a6b52" stroke-width="1.6"/>')
    p += extra
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    p += t(4, 12, "D", MUTED, 11, "start", halo=False) + t(236, 12, "I", MUTED, 11, "end", halo=False)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ PIEL EN CAPAS (lienzo 330×235)
def piel_capas(s, x, y, prof="2s", sc=1.0):
    """Corte de piel. prof: 1 | 2s (ampolla) | 2p | 3 (escara) | electrica (hueso caliente, músculo necrótico)."""
    X, W = 14, 176
    capas = [("Epidermis", "#fcd9bd", 30, 14), ("Dermis papilar", "#f9c0a8", 44, 24), ("Dermis reticular", "#f4a99b", 68, 46),
             ("Hipodermis (grasa)", "#fde68a", 114, 42), ("Músculo", "#f87171", 156, 38), ("Hueso", "#e7e5e4", 194, 30)]
    p = ""
    for nom, col, yy, h in capas:
        p += f'<rect x="{X}" y="{yy}" width="{W}" height="{h}" fill="{col}"/>'
        p += t(X + W + 8, yy + h / 2 + 4, nom, SLATE, 10.5, "start", 700)
    p += ('<path d="M60 44 L62 100 M60 44 L56 30" stroke="#78350f" stroke-width="2" fill="none"/>'
          '<ellipse cx="62" cy="104" rx="5" ry="7" fill="#fca5a5" stroke="#9a3412"/>'
          '<path d="M130 72 q6 6 0 12 q-6 6 0 12 q6 6 0 12" stroke="#0369a1" stroke-width="2" fill="none"/>'
          '<path d="M150 50 L150 110" stroke="#eab308" stroke-width="2"/>')
    if prof == "1":
        p += f'<rect x="{X}" y="30" width="{W}" height="14" fill="{ORANGE}" opacity="0.45"/>'
        p += t(X + W / 2, 22, "Solo epidermis: eritema", "#9a3412", 10.5)
    elif prof == "2s":
        p += (f'<path d="M50 30 C58 4 118 4 126 30 Z" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.6"/>'
              f'<rect x="{X}" y="30" width="{W}" height="30" fill="{ORANGE}" opacity="0.35"/>')
        p += t(88, 22, "Ampolla", "#92400e", 10.5)
    elif prof == "2p":
        p += f'<rect x="{X}" y="30" width="{W}" height="70" fill="{ORANGE}" opacity="0.45"/>'
    elif prof == "3":
        p += (f'<rect x="{X}" y="26" width="{W}" height="92" fill="#57534e" opacity="0.8"/>'
              f'<rect x="{X}" y="22" width="{W}" height="8" fill="#e7e5e4" stroke="#a8a29e"/>')
        p += t(X + W / 2, 16, "Escara: seca, blanca, indolora", "#44403c", 10.5)
    elif prof == "electrica":
        p += ('<rect x="14" y="194" width="176" height="30" fill="#fb923c"/>'
              + '<rect x="14" y="156" width="176" height="38" fill="#7f1d1d" opacity="0.35"/>'
              + '<circle cx="40" cy="30" r="5" fill="#57534e"/>')
        p += t(X + W / 2, 182, "Músculo pegado al hueso: necrosis", "#7f1d1d", 10.5)
        p += t(X + W / 2, 216, "Hueso: más resistencia, más calor", "#7c2d12", 10.5)
        p += t(40, 20, "Piel casi intacta", "#44403c", 10.5, "start")
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ MALLAMPATI (lienzo 460×160)
def mallampati(s, x, y, clase=1, sc=1.0):
    p = ""
    for k in range(4):
        cx = 58 + k * 115
        on = k + 1 == clase
        p += f'<rect x="{cx-54}" y="4" width="108" height="150" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{3 if on else 1.4}"/>'
        p += E(cx, 70, 42, 50, "#7f1d1d", "#9f1239", 3)
        p += P(f"M{cx-40} 50 Q{cx} 12 {cx+40} 50 Q{cx} 34 {cx-40} 50 Z", "#fecdd3", "#9f1239", 1.2)          # paladar blando
        p += P(f"M{cx-26} 56 L{cx-30} 100 M{cx+26} 56 L{cx+30} 100", "none", "#fda4af", 4)                  # pilares
        p += E(cx, 50, 5, 12, "#fb7185", "#9f1239", 1.2)                                                    # úvula
        top = {1: 104, 2: 86, 3: 64, 4: 42}[k + 1]
        p += P(f"M{cx-42} 120 C{cx-42} {top} {cx+42} {top} {cx+42} 120 Z", "#f87171", "#b91c1c", 1.6)         # lengua
        p += t(cx, 142, f"Clase {'I II III IV'.split()[k]}", ORANGE if on else SLATE, 12)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ VIABILIDAD DEL ASA (lienzo 450×200)
def asa_viabilidad(s, x, y, caso=2, sc=1.0, vertical=False):
    if vertical:
        return _asa_vertical(s, x, y, caso, sc)
    est = [("#f9a8d4", "Viable", ["Rosada y brillante,", "peristalsis y pulso"]),
           ("#a855f7", "Recuperable", ["Violácea que vuelve al", "rosado al liberar y calentar"]),
           ("#1f2937", "Necrosis", ["Negra, sin brillo,", "sin peristalsis ni pulso"])]
    p = ""
    for k, (col, tit, ls) in enumerate(est):
        cx = 75 + k * 150
        on = k == caso
        p += f'<rect x="{cx-70}" y="2" width="140" height="192" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{3 if on else 1.3}"/>'
        p += P(f"M{cx-52} 40 C{cx-30} 20 {cx+30} 20 {cx+52} 40 L{cx+52} 64 C{cx+30} 44 {cx-30} 44 {cx-52} 64 Z", col, "#6b21a8" if k == 1 else "#374151", 1.5)
        p += P(f"M{cx-40} 56 L{cx} 110 L{cx+40} 56", "#fef3c7", "#d97706", 1.2, 'opacity="0.9"')
        p += P(f"M{cx} 110 L{cx} 70", "none", RED if k < 2 else "#6b7280", 3)
        p += t(cx + 16, 96, "pulso" if k < 2 else "sin pulso", RED if k < 2 else "#6b7280", 10)
        p += t(cx, 132, tit, ORANGE if on else INK, 12.5)
        p += tl(cx, 152, ls, SLATE, 10.5, fw=600)
    g(s, x, y, p, sc)


def _asa_vertical(s, x, y, caso, sc):
    """Las tres filas una debajo de otra (lienzo 270×320)."""
    est = [("#f9a8d4", "Viable", ["Rosada y brillante,", "con peristalsis y pulso"]),
           ("#a855f7", "Recuperable", ["Violácea: vuelve al rosado", "al liberar y calentar"]),
           ("#1f2937", "Necrosis", ["Negra, sin brillo, sin", "peristalsis ni pulso"])]
    p = ""
    for k, (col, tit, ls) in enumerate(est):
        yy = k * 106
        on = k == caso
        p += f'<rect x="0" y="{yy}" width="270" height="98" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{3 if on else 1.3}"/>'
        cx = 58
        p += P(f"M{cx-46} {yy+26} C{cx-26} {yy+8} {cx+26} {yy+8} {cx+46} {yy+26} L{cx+46} {yy+46} C{cx+26} {yy+28} {cx-26} {yy+28} {cx-46} {yy+46} Z", col, "#374151", 1.5)
        p += P(f"M{cx-34} {yy+40} L{cx} {yy+88} L{cx+34} {yy+40}", "#fef3c7", "#d97706", 1.2)
        p += P(f"M{cx} {yy+88} L{cx} {yy+50}", "none", RED if k < 2 else "#6b7280", 3)
        p += t(118, yy + 30, tit, ORANGE if on else INK, 13, "start")
        p += tl(118, yy + 52, ls, SLATE, 10.5, "start", 600)
        p += t(118, yy + 84, "pulso (+)" if k < 2 else "sin pulso", RED if k < 2 else "#6b7280", 10.5, "start")
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ HERIDA: TIPOS DE CIERRE (lienzo 460×170)
def herida_cierre(s, x, y, caso=0, sc=1.0):
    tit = [("Primario", ["Se sutura en las", "primeras horas"]), ("Segunda intención", ["Queda abierta y", "cierra sola"]),
           ("Terciario (diferido)", ["Abierta 3-5 días,", "luego se sutura"])]
    p = ""
    for k, (tt, ls) in enumerate(tit):
        cx = 76 + k * 154
        on = k == caso
        p += f'<rect x="{cx-72}" y="2" width="144" height="164" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{3 if on else 1.3}"/>'
        p += f'<rect x="{cx-60}" y="20" width="120" height="70" rx="8" fill="{SKIN}" stroke="{SKIN_D}"/>'
        if k == 0:
            p += f'<line x1="{cx-40}" y1="55" x2="{cx+40}" y2="55" stroke="#9f1239" stroke-width="2"/>'
            p += "".join(f'<line x1="{cx-34+i*17}" y1="46" x2="{cx-34+i*17}" y2="64" stroke="#1e3a8a" stroke-width="2.2"/>' for i in range(5))
        elif k == 1:
            p += E(cx, 55, 42, 16, "#f87171", "#9f1239", 1.5) + "".join(C(cx - 28 + i * 14, 55 + (i % 2) * 4, 3, "#fca5a5", "none", 0) for i in range(5))
        else:
            p += E(cx, 55, 36, 11, "#fca5a5", "#9f1239", 1.2) + "".join(f'<line x1="{cx-30+i*15}" y1="44" x2="{cx-30+i*15}" y2="66" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="3 2"/>' for i in range(5))
        p += t(cx, 112, tt, ORANGE if on else INK, 12)
        p += tl(cx, 132, ls, SLATE, 10.5, fw=600)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ PERINÉ: VISTA DE FRENTE (lienzo 300×250)
def ano_frontal(s, x, y, lesion="fisura", sc=1.0):
    p = (P("M20 30 C60 10 130 16 150 40 C170 16 240 10 280 30 C300 90 300 190 270 230 C230 250 170 244 150 214 C130 244 70 250 30 230 C0 190 0 90 20 30 Z", SKIN, SKIN_D, 2)
         + C(150, 128, 20, "#be185d", "#831843", 2) + C(150, 128, 7, "#500724", "none", 0)
         + "".join(f'<line x1="{150+9*math.cos(a):.1f}" y1="{128+9*math.sin(a):.1f}" x2="{150+19*math.cos(a):.1f}" y2="{128+19*math.sin(a):.1f}" stroke="#831843" stroke-width="1.2"/>' for a in [k * math.pi / 6 for k in range(12)])
         + t(150, 58, "12 · anterior", MUTED, 10, halo=False) + t(112, 206, "6 · posterior", MUTED, 10, halo=False))
    if lesion == "fisura":
        p += (P("M147 150 L150 176 L153 150 Z", "#dc2626", "#7f1d1d", 1.2) + E(150, 186, 9, 7, "#fda4af", "#be185d", 1.5)
              + t(186, 150, "Fisura en la línea", INK, 10.5, "start") + t(186, 163, "media posterior", INK, 10.5, "start")
              + guia(184, 156, 153, 162) + t(174, 228, "Hemorroide centinela", INK, 10.5, "start") + guia(172, 224, 156, 190))
    elif lesion == "trombosis":
        p += (E(176, 142, 15, 12, "#6d28d9", "#3b0764", 2) + E(173, 138, 5, 3, "#a78bfa", "none", 0)
              + t(150, 226, "Nódulo violáceo y tenso:", INK, 10.5) + t(150, 240, "coágulo en una vena externa", SLATE, 10, fw=700)
              + guia(176, 214, 176, 154))
    elif lesion == "absceso":
        p += (E(150, 174, 32, 20, "#f87171", "#b91c1c", 2, extra='opacity="0.9"') + E(150, 172, 14, 8, "#fde68a", "#ca8a04", 1.2)
              + t(150, 226, "Roja, caliente y fluctuante (pus)", INK, 10.5)
              + f'<line x1="120" y1="172" x2="180" y2="172" stroke="#111827" stroke-width="2" stroke-dasharray="5 3"/>'
              + t(150, 240, "- - - incisión y drenaje", ORANGE, 10.5))
    elif lesion == "fistula":
        p += (C(200, 160, 5, "#b91c1c", "#7f1d1d", 1.5) + P("M200 160 C186 150 172 140 162 132", "none", ORANGE, 3, 'stroke-dasharray="5 3"')
              + t(150, 226, "Orificio externo a 2 cm del ano", INK, 10.5) + t(150, 240, "- - - trayecto hacia el canal anal", ORANGE, 10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CANAL ANAL EN CORTE (lienzo 320×270)
def ano_coronal(s, x, y, tipo="fistula", sc=1.0):
    """Corte coronal: esfínter interno (EAI), externo (EAE), elevador, línea dentada.
    tipo: fistula (transesfinteriana baja) | esfinterotomia | hemorroide."""
    p = (P("M20 250 L20 120 L120 104 L120 0 L200 0 L200 104 L300 120 L300 250 Z", "#fef3c7", "none", 0)
         + t(52, 200, "grasa", "#a16207", 10, halo=False)
         + P("M110 0 L110 104 L136 116 L136 226 L150 236 L164 226 L164 116 L190 104 L190 0", "#fbcfe8", "#be185d", 1.5)
         + P("M136 116 L136 226 M164 116 L164 226", "none", "#f9a8d4", 12)                                       # EAI
         + "".join(P(f"M{a} {y0} L{a} {y1}", "none", "#dc2626", 18) for a in (116, 184) for y0, y1 in ((122, 160), (164, 200), (204, 236)))
         + P("M112 112 L24 60", "none", "#b91c1c", 12, 'stroke-linecap="round"') + P("M188 112 L296 60", "none", "#b91c1c", 12, 'stroke-linecap="round"')
         + '<line x1="140" y1="176" x2="160" y2="176" stroke="#111827" stroke-width="1.6" stroke-dasharray="3 2"/>'
         + P("M10 244 L140 244 M160 244 L310 244", "none", SKIN_D, 5)
         + t(150, 60, "Recto", "#9d174d", 10.5)
         + t(20, 48, "Elevador del ano", "#7f1d1d", 10, "start") + t(100, 146, "EAE", "#7f1d1d", 10.5, "end")
         + t(224, 212, "EAI", "#be185d", 10.5, "start") + guia(222, 208, 168, 206, "#be185d")
         + t(224, 180, "Línea dentada", INK, 10, "start") + guia(222, 176, 160, 176))
    if tipo == "fistula":
        p += (P("M137 180 L118 206 L96 224 L64 244", "none", ORANGE, 4, 'stroke-dasharray="6 3"')
              + C(137, 180, 4, "#7f1d1d", "none", 0) + C(64, 244, 5, "#b91c1c", "#7f1d1d", 1.5)
              + t(34, 266, "Trayecto por la parte baja del EAE", "#9a3412", 10.5, "start"))
    elif tipo == "esfinterotomia":
        p += (f'<line x1="158" y1="196" x2="170" y2="226" stroke="#111827" stroke-width="3"/>'
              + t(236, 238, "Corte lateral", ORANGE, 10.5, "start") + t(236, 251, "del EAI", ORANGE, 10.5, "start")
              + guia(234, 236, 168, 214, ORANGE))
    elif tipo == "hemorroide":
        p += E(140, 158, 8, 16, "#7c3aed", "#4c1d95", 1.5) + E(160, 158, 8, 16, "#7c3aed", "#4c1d95", 1.5)
        p += t(224, 146, "Hemorroide interna", "#4c1d95", 10.5, "start") + guia(222, 142, 166, 152, "#4c1d95")
    g(s, x, y, p, sc)


def hemorroides_grados(s, x, y, caso=3, sc=1.0):
    """Grados de la hemorroide interna según el prolapso (lienzo 470×170)."""
    ds = [("I", ["No se prolapsa"]), ("II", ["Sale y vuelve", "sola"]), ("III", ["Sale y hay que", "reducirla con la mano"]),
          ("IV", ["Afuera, no se", "puede reducir"])]
    p = ""
    for k, (gr, ls) in enumerate(ds):
        cx = 58 + k * 118
        on = k + 1 == caso
        p += f'<rect x="{cx-55}" y="2" width="110" height="164" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{3 if on else 1.3}"/>'
        p += P(f"M{cx-24} 10 L{cx-24} 80 L{cx+24} 80 L{cx+24} 10", "#fbcfe8", "#be185d", 1.5)
        p += f'<line x1="{cx-40}" y1="80" x2="{cx+40}" y2="80" stroke="{SKIN_D}" stroke-width="4"/>'
        hy = [44, 70, 88, 94][k]
        p += E(cx - 10, hy, 10, 16, "#7c3aed", "#4c1d95", 1.4)
        if k == 1:
            p += flecha(cx + 16, 96, cx + 16, 60, SLATE, 1.6)
        if k == 2:
            p += t(cx + 26, 104, "✋", INK, 14, halo=False)
        p += t(cx, 128, "Grado " + gr, ORANGE if on else INK, 12)
        p += tl(cx, 146, ls, SLATE, 10, fw=600)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ HERNIA INCISIONAL ESTRANGULADA (lienzo 320×230)
def hernia_incisional(s, x, y, sc=1.0):
    p = (P("M40 10 Q160 -4 280 10 L290 220 Q160 236 30 220 Z", SKIN, SKIN_D, 2)
         + '<line x1="160" y1="30" x2="160" y2="200" stroke="#9f1239" stroke-width="2"/>'
         + "".join(f'<line x1="152" y1="{40+i*16}" x2="168" y2="{40+i*16}" stroke="#9f1239" stroke-width="1.5"/>' for i in range(10))
         + E(160, 120, 42, 34, "#fca5a5", "#b91c1c", 3) + E(160, 120, 42, 34, "#dc2626", "none", 0, 'opacity="0.25"')
         + t(214, 76, "Masa tensa, roja,", INK, 10.5, "start") + t(214, 90, "irreductible", INK, 10.5, "start") + guia(212, 86, 196, 104)
         + t(40, 214, "Cicatriz de laparotomía mediana", SLATE, 10, "start", 600))
    # recuadro: asa atrapada en el cuello del saco
    p += (f'<rect x="200" y="140" width="110" height="74" rx="8" fill="#ffffff" stroke="#cbd5e1"/>'
          + P("M214 186 C230 150 280 150 296 186", "none", "#7e22ce", 10, 'stroke-linecap="round"')
          + P("M232 178 L232 200 M278 178 L278 200", "none", "#475569", 4)
          + t(255, 206, "cuello estrecho", SLATE, 9.5, halo=False))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ NEUMOTÓRAX ABIERTO: PARCHE DE 3 LADOS (lienzo 450×210)
def torax_valvula(s, x, y, sc=1.0):
    p = (P("M20 20 Q100 0 180 20 L186 200 L14 200 Z", SKIN, SKIN_D, 2)
         + P("M100 20 L100 200", "none", "#e9b48f", 1.5)
         + f'<rect x="36" y="86" width="44" height="44" fill="#e0f2fe" stroke="#0369a1" stroke-width="1.5" opacity="0.9"/>'
         + C(58, 108, 6, "#7f1d1d", "none", 0)
         + P("M34 84 H82 M82 84 V132 M34 84 V132", "none", "#f59e0b", 5)
         + t(58, 150, "lado libre", ORANGE, 10.5) + t(100, 196, "Hemitórax derecho", SLATE, 10, halo=False))
    for k, (tt, ins) in enumerate((("Inspira:", True), ("Espira:", False))):
        bx = 212 + k * 118
        p += f'<rect x="{bx}" y="20" width="108" height="150" rx="10" fill="#ffffff" stroke="#cbd5e1"/>'
        p += P(f"M{bx+20} 60 L{bx+20} 130", "none", SKIN_D, 8)
        if ins:
            p += P(f"M{bx+26} 60 L{bx+26} 130", "none", "#0369a1", 4)
            p += flecha(bx + 80, 95, bx + 34, 95, "#94a3b8", 2) + t(bx + 60, 88, "✕", RED, 16, halo=False)
            p += tl(bx + 54, 150, ["el parche se pega:", "no entra aire"], SLATE, 9.5, fw=700)
        else:
            p += P(f"M{bx+26} 60 L{bx+26} 100 L{bx+50} 128", "none", "#0369a1", 4)
            p += flecha(bx + 10, 112, bx + 90, 140, ORANGE, 2.4)
            p += tl(bx + 54, 150, ["el aire sale por", "el lado libre"], SLATE, 9.5, fw=700)
        p += t(bx + 54, 40, tt, INK, 11.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ MANIOBRA DE PRINGLE (lienzo 330×230)
def higado_pringle(s, x, y, sc=1.0):
    p = (P("M10 30 C80 0 280 6 320 36 C318 80 250 110 190 118 C140 124 90 122 50 110 C20 98 6 70 10 30 Z", ORG["higado"])
         + P("M150 50 L130 70 L160 78 L140 98", "none", RED, 3) + C(138, 104, 3, RED, "none", 0) + C(146, 112, 2.5, RED, "none", 0)
         + t(206, 56, "Laceración que sangra", "#7f1d1d", 10.5, "start")
         + E(110, 124, 12, 18, ORG["vesicula"], rot=-20)
         + P("M168 116 L168 206", "none", BLUE, 12) + P("M180 116 L182 206", "none", RED, 6) + P("M156 116 L154 206", "none", "#15803d", 6)
         + P("M140 206 C140 226 250 226 250 206", "none", "#f9a8d4", 16, 'stroke-linecap="round"')
         + f'<rect x="136" y="150" width="62" height="12" rx="4" fill="#64748b" stroke="#1f2937"/>'
         + P("M198 152 L236 140 M198 160 L236 172", "none", "#1f2937", 4, 'stroke-linecap="round"')
         + t(244, 150, "Pinza: Pringle", ORANGE, 11.5, "start") + t(244, 166, "(ligamento", SLATE, 10, "start", 600)
         + t(244, 180, "hepatoduodenal)", SLATE, 10, "start", 600)
         + t(96, 176, "Porta", BLUE, 10, "end") + guia(98, 172, 164, 178, BLUE)
         + t(96, 194, "Colédoco", "#15803d", 10, "end") + guia(98, 190, 154, 192, "#15803d")
         + t(214, 200, "Arteria hepática", RED, 10, "start") + guia(212, 196, 184, 190, RED))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ ENFERMEDAD INFLAMATORIA INTESTINAL (lienzo 220×230)
def intestino_eii(s, x, y, modo="crohn", sc=1.0):
    """Marco colónico + íleon; en rojo los tramos enfermos. crohn: salteado con íleon; cu: continuo desde el recto."""
    base = "#fed7aa"
    seg = {"ileon": "M40 196 C60 200 70 194 84 190", "ciego": "E36 190 13 12", "asc": "M34 176 L30 70",
           "trans": "M40 54 L180 54", "desc": "M190 66 L190 160", "sigm": "M190 160 C190 190 160 196 140 192",
           "recto": "M136 196 L130 222"}
    enf = {"crohn": {"ileon", "ciego", "trans"}, "cu": {"recto", "sigm", "desc"}}[modo]
    p = ""
    for k, d in seg.items():
        col = RED if k in enf else base
        if d.startswith("E"):
            cx, cy, rx, ry = d[1:].split()
            p += E(cx, cy, rx, ry, col, "#9a3412", 1.4)
        else:
            p += P(d, "none", col, 16, 'stroke-linecap="round"')
    p += P("M30 70 Q30 54 44 54 M180 54 Q190 54 190 66", "none", base, 16)
    if modo == "crohn":
        p += (t(110, 100, "Lesiones salteadas,", "#7f1d1d", 10.5) + t(110, 114, "íleon terminal y colon", "#7f1d1d", 10.5)
              + f'<rect x="72" y="130" width="76" height="46" rx="6" fill="#fecaca" stroke="#b91c1c"/>'
              + "".join(f'<rect x="{76+(i%5)*14}" y="{134+(i//5)*14}" width="12" height="11" rx="4" fill="#fca5a5" stroke="#b91c1c" stroke-width="0.8"/>' for i in range(15))
              + t(110, 188, "«empedrado»", "#7f1d1d", 10))
    else:
        p += t(110, 110, "Continua desde el recto,", "#7f1d1d", 10.5) + t(110, 124, "solo mucosa, sin íleon", "#7f1d1d", 10.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ EDEMA CEREBRAL Y MANITOL (lienzo 330×220)
def cerebro_osmosis(s, x, y, sc=1.0):
    p = (C(110, 110, 96, "#e7e5e4", "#57534e", 5) + C(110, 110, 88, "#fbcfe8", "#be185d", 2)
         + "".join(f'<path d="M{50+k*24} {60+(k%2)*10} q12 16 0 32 q-12 16 0 32" fill="none" stroke="#be185d" stroke-width="1.6"/>' for k in range(6))
         + t(110, 214, "Cerebro edematoso: ↑ PIC", "#9d174d", 11)
         + P("M236 20 L236 200", "none", "#fecaca", 30) + P("M236 20 L236 200", "none", RED, 2, 'fill="none" opacity="0.5"')
         + "".join(t(236, 50 + k * 40, "M", "#1d4ed8", 12) for k in range(4))
         + t(236, 216, "vaso", RED, 10.5)
         + "".join(flecha(170, 70 + k * 36, 216, 70 + k * 36, "#0284c7", 2.4) for k in range(4))
         + t(272, 90, "Manitol:", "#1d4ed8", 10.5, "start") + t(272, 104, "arrastra", "#1d4ed8", 10.5, "start")
         + t(272, 118, "agua del", "#1d4ed8", 10.5, "start") + t(272, 132, "cerebro", "#1d4ed8", 10.5, "start")
         + t(272, 146, "al plasma", "#1d4ed8", 10.5, "start"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ VÍA AÉREA QUEMADA (lienzo 320×250)
def via_aerea_quemada(s, x, y, sc=1.0):
    p = (P("M60 20 C120 0 190 20 200 80 C204 110 196 130 184 140 L180 170 L150 176 L150 240 L90 240 L92 160 C60 150 40 120 40 80 C40 50 46 30 60 20 Z", SKIN, SKIN_D, 2)
         + P("M184 96 L204 104 L186 112", SKIN, SKIN_D, 2)
         + P("M184 122 C170 124 160 120 150 116", "none", "#57534e", 5)
         + P("M150 116 C130 120 116 140 118 176 L120 240", "none", "#fda4af", 16)
         + E(126, 170, 14, 10, ORANGE, "#9a3412", 2) + E(112, 170, 10, 8, ORANGE, "#9a3412", 2, extra='opacity="0.8"')
         + P("M206 100 C160 108 130 130 122 180 L122 240", "none", "#38bdf8", 5, 'stroke-linecap="round"')
         + "".join(C(160 + k * 8, 118 - (k % 2) * 4, 2.2, "#1f2937", "none", 0) for k in range(4))
         + E(160, 60, 14, 8, "#fca5a5", "#b91c1c", 1.5) + E(90, 70, 12, 8, "#fca5a5", "#b91c1c", 1.5)
         + t(230, 60, "Quemadura facial", INK, 10.5, "start") + guia(228, 56, 172, 60)
         + t(230, 120, "Hollín en la boca", INK, 10.5, "start") + guia(228, 116, 186, 118)
         + t(230, 170, "Edema de la laringe:", "#9a3412", 10.5, "start") + t(230, 184, "cierra la vía aérea", "#9a3412", 10.5, "start")
         + guia(228, 172, 140, 170, "#9a3412")
         + t(230, 216, "Tubo endotraqueal", "#0369a1", 10.5, "start") + guia(228, 212, 124, 212, "#0369a1"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ H. PYLORI EN LA MUCOSA (lienzo 330×190)
def hpylori(s, x, y, sc=1.0):
    p = (f'<rect x="0" y="110" width="330" height="80" fill="#fbcfe8"/>'
         + "".join(P(f"M{20+k*52} 110 L{24+k*52} 176 L{40+k*52} 176 L{44+k*52} 110", "#ffffff", "#be185d", 1.2) for k in range(6))
         + f'<rect x="0" y="70" width="330" height="40" fill="#bae6fd" opacity="0.8"/>'
         + t(6, 64, "Moco", "#0369a1", 10.5, "start") + t(6, 104, "Epitelio", "#9d174d", 10.5, "start")
         + t(165, 26, "Luz gástrica: ácido (HCl)", "#b91c1c", 11))
    for k, (bx, by) in enumerate([(80, 88), (160, 92), (240, 86)]):
        p += P(f"M{bx-18} {by} q6 -8 12 0 q6 8 12 0 q6 -8 12 0", "none", GREEN, 5, 'stroke-linecap="round"')
        p += P(f"M{bx+18} {by} l14 -6 M{bx+18} {by} l14 2", "none", GREEN, 1.4)
    p += (C(118, 60, 16, "#e0e7ff", "#6366f1", 1.2, 'opacity="0.9"') + t(118, 64, "NH₃", "#4338ca", 10.5, halo=False)
          + t(260, 60, "Ureasa → NH₃", "#4338ca", 10.5) + t(260, 74, "neutraliza el ácido", "#4338ca", 10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CASCADA DE CORREA (lienzo 560×150)
def mucosa_correa(s, x, y, caso=3, sc=1.0):
    et = ["Gastritis crónica", "Atrofia", "Metaplasia intestinal", "Displasia", "Adenocarcinoma"]
    p = ""
    for k, nom in enumerate(et):
        cx = 56 + k * 112
        on = k == caso
        p += f'<rect x="{cx-50}" y="2" width="100" height="144" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{3 if on else 1.3}"/>'
        p += f'<rect x="{cx-40}" y="14" width="80" height="70" rx="6" fill="#fce7f3" stroke="#be185d"/>'
        n = 4 if k != 1 else 2
        for i in range(n):
            gx = cx - 30 + i * (60 / max(n - 1, 1))
            p += P(f"M{gx-6} 16 L{gx-6} 70 L{gx+6} 70 L{gx+6} 16", "#ffffff", "#be185d", 1)
            if k == 2:
                p += C(gx, 40, 4, "#ffffff", "#64748b", 1)
            if k >= 3:
                p += "".join(C(gx + (j % 2) * 3 - 1.5, 24 + j * 9, 2.3, "#4c1d95", "none", 0) for j in range(5))
        if k == 0:
            p += "".join(C(cx - 28 + j * 12, 78, 2.5, "#1d4ed8", "none", 0) for j in range(5))
        if k == 4:
            p += E(cx, 60, 30, 18, "#7c3aed", "#4c1d95", 1.5, extra='opacity="0.7"')
        p += tl(cx, 104, nom.split(" ", 1) if len(nom) > 12 else [nom], ORANGE if on else INK, 10.5)
        if k < 4:
            p += flecha(cx + 50, 50, cx + 62, 50, SLATE, 1.6)
    g(s, x, y, p, sc)
