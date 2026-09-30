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
def lab_barras(s, x, y, items, W=320, xmax=10, titulo="Veces el valor normal", sc=1.0, ref=1):
    """items: (nombre, valor, veces, on). Barra horizontal con línea en ref (límite normal); ref=None la omite."""
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
    if ref is not None:
        x1 = LW + ref * bw / xmax
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


# ════════════════════════════════════════════════════════════ OBSTETRICIA
PINK, PINK_D, AMN = "#fbcfe8", "#be185d", "#dbeafe"


def _feto(cx, cy, sc=1.0, col="#fcd5b5"):
    """Feto cefálico (cabeza abajo) centrado en (cx, cy)."""
    k = sc
    return (E(cx + 6 * k, cy - 48 * k, 44 * k, 58 * k, col, SKIN_D, 1.6, rot=-10)
            + C(cx, cy + 34 * k, 36 * k, col, SKIN_D, 1.6)
            + P(f"M{cx+30*k} {cy-70*k} q26 {18*k} 8 {44*k}", "none", SKIN_D, 5 * k, 'stroke-linecap="round"')
            + P(f"M{cx-28*k} {cy-20*k} q-18 {22*k} 6 {36*k}", "none", SKIN_D, 5 * k, 'stroke-linecap="round"'))


def utero_gestante(s, x, y, tipo="normal", marcas=(), rotulos=(), sc=1.0):
    """Útero gestante en corte (lienzo 300×330). tipo: normal | dpp | rotura | rpm | oligo | corio | saf | dilatado."""
    liq = {"oligo": "#e0f2fe", "corio": "#fef3c7"}.get(tipo, AMN)
    p = (E(150, 150, 124, 142, PINK, PINK_D, 3) + E(150, 150, 108 if tipo != "oligo" else 96, 126 if tipo != "oligo" else 112, liq, "#93c5fd", 1.5)
         + P("M40 70 C80 20 170 10 230 30 L210 62 C160 44 100 50 62 88 Z", "#9f1239", "#881337", 1.5))
    p += _feto(150, 170, 0.95 if tipo != "oligo" else 0.85)
    # cuello
    if tipo == "dilatado":
        p += P("M118 286 L126 322 M182 286 L174 322", "none", PINK_D, 8) + t(214, 316, "5 cm", ORANGE, 11, "start")
    else:
        p += P("M138 288 L138 324 M162 288 L162 324", "none", PINK_D, 8)
    if tipo == "dpp":
        p += P("M70 62 C110 44 176 36 222 44 L214 70 C170 66 120 72 84 92 Z", "#450a0a", "none", 0, 'opacity="0.9"')
        p += P("M150 324 q-4 10 0 16 q4 10 0 16", "none", "#450a0a", 3)
        p += t(248, 20, "Hematoma", "#450a0a", 10.5, "start") + t(248, 34, "retroplacentario", "#450a0a", 10.5, "start") + guia(246, 38, 200, 52)
    if tipo == "rotura":
        p += (P("M44 230 L58 216 L50 204 L66 190", "none", "#7f1d1d", 5) + E(20, 250, 20, 30, "#b91c1c", "none", 0, 'opacity="0.8"')
              + t(4, 300, "Desgarro del segmento", "#7f1d1d", 10.5, "start") + t(4, 314, "(cicatriz previa)", "#7f1d1d", 10, "start", 600))
    if tipo == "rpm":
        p += "".join(f'<path d="M{146+k*8} {330+k*4} q3 6 0 10" fill="#60a5fa" stroke="#1d4ed8" stroke-width="1"/>' for k in range(2))
        p += t(214, 326, "líquido claro", "#1d4ed8", 10.5, "start") + P("M142 290 L158 290", "none", "#ffffff", 4)
    if tipo == "corio":
        p += E(150, 150, 108, 126, "none", RED, 3, extra='stroke-dasharray="6 4"')
        p += t(238, 110, "Membranas", RED, 10.5, "start") + t(238, 124, "infectadas", RED, 10.5, "start")
    if tipo == "saf":
        p += "".join(C(cx, cy, 5, "#1f2937", "none", 0) for cx, cy in [(96, 66), (130, 50), (170, 44), (204, 48)])
        p += t(238, 24, "Trombos en la", "#1f2937", 10.5, "start") + t(238, 38, "placenta", "#1f2937", 10.5, "start")
    p += t(250, 60, "placenta", "#9f1239", 10, "start") if tipo not in ("dpp", "saf") else ""
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    g(s, x, y, p, sc)


def cervix(s, x, y, largo=25, cerclaje=True, sc=1.0):
    """Cuello uterino en corte con la longitud medida (lienzo 300×220)."""
    L_ = 60 + largo * 2
    p = (P(f"M40 20 C40 10 260 10 260 20 L260 60 C200 70 180 80 180 90 L180 {90+L_} L120 {90+L_} L120 90 C120 80 100 70 40 60 Z", PINK, PINK_D, 2)
         + f'<line x1="150" y1="84" x2="150" y2="{90+L_}" stroke="#9f1239" stroke-width="2" stroke-dasharray="4 3"/>'
         + t(150, 40, "cavidad uterina", PINK_D, 10.5))
    p += (f'<line x1="200" y1="88" x2="200" y2="{90+L_}" stroke="{TEAL}" stroke-width="2"/>'
          + f'<line x1="194" y1="88" x2="206" y2="88" stroke="{TEAL}" stroke-width="2"/><line x1="194" y1="{90+L_}" x2="206" y2="{90+L_}" stroke="{TEAL}" stroke-width="2"/>'
          + t(212, 94 + L_ / 2, f"{largo} mm", TEAL_D, 12, "start"))
    if cerclaje:
        p += (E(150, 90 + L_ * 0.35, 36, 8, "none", "#1d4ed8", 3) + t(40, 90 + L_ * 0.35 + 4, "cerclaje", "#1d4ed8", 11, "start"))
    p += t(150, 108 + L_, "orificio externo", MUTED, 10, halo=False)
    g(s, x, y, p, sc)


def ctg(s, x, y, patron="tardias", W=560, sc=1.0):
    """Cardiotocografía: FCF arriba (60-200 lpm) y contracciones abajo, 10 minutos (lienzo W×230)."""
    H1, H2 = 130, 60
    X0_, X1_ = 40, W - 10
    fy = lambda v: 10 + (200 - v) / 140 * H1
    p = f'<rect x="{X0_}" y="10" width="{X1_-X0_}" height="{H1}" fill="#fff1f2" stroke="#fecdd3"/>'
    p += f'<rect x="{X0_}" y="{H1+30}" width="{X1_-X0_}" height="{H2}" fill="#f0fdf4" stroke="#bbf7d0"/>'
    for v in (80, 110, 140, 170):
        p += f'<line x1="{X0_}" y1="{fy(v):.1f}" x2="{X1_}" y2="{fy(v):.1f}" stroke="#fecdd3" stroke-width="1"/>'
        p += t(X0_ - 4, fy(v) + 4, str(v), MUTED, 9.5, "end", 600, halo=False)
    for k in range(11):
        xx = X0_ + k * (X1_ - X0_) / 10
        p += f'<line x1="{xx:.1f}" y1="10" x2="{xx:.1f}" y2="{H1+30+H2}" stroke="#e2e8f0" stroke-width="1"/>'
    n = 400
    pts, cpts = [], []
    import math as _m
    for i in range(n + 1):
        tt = i / n * 10
        if patron == "sinusoidal":
            v = 150 + 10 * _m.sin(2 * _m.pi * tt / 0.33) if tt < 7.5 else 150 - (tt - 7.5) * 26 + 3 * _m.sin(i)
            v = max(v, 88)
            c = 0.12 + 0.1 * max(0, _m.sin(2 * _m.pi * tt / 3.3)) ** 2
        elif patron == "tardias":
            c = sum(max(0, _m.cos(_m.pi * (tt - (0.9 + 2 * k)) / 1.3)) ** 2 for k in range(5) if abs(tt - (0.9 + 2 * k)) < 0.65)
            dec = sum(max(0, _m.cos(_m.pi * (tt - (1.6 + 2 * k)) / 1.3)) ** 2 for k in range(5) if abs(tt - (1.6 + 2 * k)) < 0.65)
            v = 145 - 28 * dec + 1.2 * _m.sin(i * 1.7)
            c = 0.1 + 0.85 * c
        else:
            v = 140 + 6 * _m.sin(i * 0.9) + 4 * _m.sin(i * 0.37)
            c = 0.1 + 0.7 * max(0, _m.sin(2 * _m.pi * tt / 3.3)) ** 6
        xx = X0_ + tt / 10 * (X1_ - X0_)
        pts.append(f"{xx:.1f},{fy(v):.1f}")
        cpts.append(f"{xx:.1f},{H1+30+H2-c*H2*0.95:.1f}")
    p += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#1e293b" stroke-width="1.6"/>'
    p += f'<polyline points="{" ".join(cpts)}" fill="none" stroke="#15803d" stroke-width="1.6"/>'
    p += t(X0_ + 4, 24, "FCF (lpm)", "#9f1239", 10, "start", halo=False) + t(X0_ + 4, H1 + 44, "Contracciones", "#15803d", 10, "start", halo=False)
    p += t((X0_ + X1_) / 2, H1 + 30 + H2 + 16, "10 minutos", MUTED, 10, halo=False)
    g(s, x, y, p, sc)


def partograma(s, x, y, puntos=((0, 6), (4, 6)), sc=1.0):
    """Dilatación (4-10 cm) contra horas (0-10); puntos del caso en naranja (lienzo 460×250)."""
    X0_, Y0_, W_, H_ = 50, 16, 390, 190
    fx = lambda h: X0_ + h / 10 * W_
    fy = lambda d: Y0_ + (10 - d) / 6 * H_
    p = f'<rect x="{X0_}" y="{Y0_}" width="{W_}" height="{H_}" fill="#f8fafc" stroke="#cbd5e1"/>'
    for d in range(4, 11):
        p += f'<line x1="{X0_}" y1="{fy(d):.1f}" x2="{X0_+W_}" y2="{fy(d):.1f}" stroke="#e2e8f0"/>' + t(X0_ - 6, fy(d) + 4, f"{d}", MUTED, 10, "end", 600, halo=False)
    for h in range(0, 11, 2):
        p += t(fx(h), Y0_ + H_ + 16, f"{h} h", MUTED, 10, halo=False)
    p += f'<line x1="{fx(0):.1f}" y1="{fy(6):.1f}" x2="{fx(4):.1f}" y2="{fy(10):.1f}" stroke="{GREEN}" stroke-width="2.5"/>'
    p += t(fx(4) + 6, fy(10) + 14, "progreso esperado (≥ 1 cm/h)", GREEN, 10, "start")
    p += P(f"M{fx(puntos[0][0]):.1f} {fy(puntos[0][1]):.1f} L{fx(puntos[-1][0]):.1f} {fy(puntos[-1][1]):.1f}", "none", ORANGE, 3)
    for hh, dd in puntos:
        p += C(fx(hh), fy(dd), 7, ORANGE, "#7c2d12", 2)
    p += t(fx(2), fy(6) + 24, "4 h sin cambio con buenas contracciones", "#9a3412", 10.5)
    p += t(12, Y0_ + H_ / 2, "cm", MUTED, 10, halo=False)
    g(s, x, y, p, sc)


def pelvis_sagital(s, x, y, defecto="cistocele", sc=1.0):
    """Pelvis femenina en corte sagital (lienzo 320×300). Adelante = izquierda.
    defecto: normal | cistocele | rectocele | cisto_recto | uterino | cupula | cupula_malla."""
    cist = defecto in ("cistocele", "cisto_recto")
    rect = defecto in ("rectocele", "cisto_recto")
    p = (E(58, 170, 16, 30, "#e7e5e4", "#a8a29e", 2, rot=20)
         + P("M246 20 C300 70 300 170 250 236 L236 226 C280 164 278 76 232 32 Z", "#e7e5e4", "#a8a29e", 2)
         + t(40, 214, "pubis", MUTED, 10, halo=False) + t(298, 250, "sacro", MUTED, 10, "end", halo=False)
         + '<line x1="20" y1="262" x2="300" y2="262" stroke="#e9b48f" stroke-width="3"/>' + t(24, 256, "periné", MUTED, 10, "start", halo=False))
    # recto (detrás)
    rpath = "M252 40 C262 110 236 170 204 206 C190 222 182 240 178 262" if not rect else "M252 40 C262 110 236 170 204 196 C160 206 170 236 178 262"
    p += P(rpath, "none", "#fcd34d", 20, 'stroke-linecap="round"') + P(rpath, "none", "#d97706", 2)
    # vagina
    if defecto in ("uterino",):
        vpath = "M168 150 C156 196 140 230 128 262"
    elif defecto.startswith("cupula"):
        vpath = "M150 230 C142 244 136 254 128 262"
    else:
        vpath = "M168 150 C156 196 140 230 128 262"
    p += P(vpath, "none", "#f9a8d4", 16, 'stroke-linecap="round"') + P(vpath, "none", PINK_D, 1.5)
    # vejiga
    p += P("M78 110 C74 70 140 62 146 104 C150 136 132 150 108 150 C88 150 80 132 78 110 Z", ORG["vejiga"], "#ca8a04", 2)
    if cist:
        p += E(140, 196, 20, 24, ORG["vejiga"], "#ca8a04", 2) + P("M112 150 C124 162 132 170 136 176", "none", ORG["vejiga"], 14)
    # útero
    if defecto == "uterino":
        p += (P("M120 250 C110 220 140 200 160 214 C176 226 170 254 156 268 Z", PINK, PINK_D, 2)
              + E(142, 280, 22, 11, "#fda4af", PINK_D, 2) + E(146, 282, 9, 5, "#7f1d1d", "none", 0)
              + t(160, 300, "cérvix fuera de la vulva, con úlcera", "#7f1d1d", 10.5))
    elif defecto.startswith("cupula"):
        p += E(130, 274, 26, 12, "#f9a8d4", PINK_D, 2) + t(160, 300, "cúpula vaginal evertida (sin útero)", "#9d174d", 10.5)
        if defecto == "cupula_malla":
            p += P("M150 232 C200 200 240 130 256 96", "none", "#2563eb", 3, 'stroke-dasharray="6 3"') + t(196, 128, "malla al promontorio", "#1d4ed8", 10.5, "start")
    else:
        p += E(176, 108, 40, 26, PINK, PINK_D, 2, rot=-50) + E(168, 146, 12, 10, PINK, PINK_D, 2)
        p += t(200, 70, "útero", PINK_D, 10.5, "start")
    if cist:
        p += t(8, 40, "Cistocele: la vejiga baja", "#a16207", 10.5, "start") + t(8, 54, "por la pared anterior", "#a16207", 10.5, "start")
        p += guia(60, 58, 132, 190, "#a16207")
    if rect:
        p += t(236, 284, "Rectocele: el recto", "#b45309", 10.5) + t(236, 298, "empuja la pared posterior", "#b45309", 10.5)
        p += guia(236, 274, 178, 214, "#b45309")
    if defecto not in ("uterino",) and not defecto.startswith("cupula"):
        p += t(76, 104, "vejiga", "#a16207", 10, "end", halo=True) if not cist else ""
    g(s, x, y, p, sc)


def atfp(s, x, y, sc=1.0):
    """Piso pélvico visto desde arriba: arco tendinoso de la fascia pélvica (ATFP) y la fascia pubocervical (lienzo 330×240)."""
    p = (P("M165 18 C100 20 50 60 34 120 C28 170 60 214 110 226 L220 226 C270 214 302 170 296 120 C280 60 230 20 165 18 Z", "#f5f5f4", "#a8a29e", 3)
         + P("M130 24 L200 24 L196 40 L134 40 Z", "#e7e5e4", "#a8a29e", 2) + t(165, 36, "pubis", MUTED, 10, halo=False)
         + C(62, 170, 7, "#e7e5e4", "#a8a29e", 2) + C(268, 170, 7, "#e7e5e4", "#a8a29e", 2)
         + t(58, 194, "espina", MUTED, 10, halo=False) + t(272, 194, "ciática", MUTED, 10, halo=False)
         + P("M136 40 L62 170", "none", "#ffffff", 5) + P("M136 40 L62 170", "none", TEAL, 2.5)
         + P("M194 40 L268 170", "none", "#ffffff", 5) + P("M194 40 L268 170", "none", TEAL, 2.5)
         + P("M140 70 C150 66 180 66 190 70 L196 160 C180 170 150 170 134 160 Z", "#fce7f3", PINK_D, 2)
         + t(165, 120, "vagina y", PINK_D, 10) + t(165, 134, "fascia", PINK_D, 10)
         + P("M190 90 L230 92 M192 130 L246 134", "none", PINK_D, 2)
         + P("M140 90 L118 92 M138 130 L108 134", "none", ORANGE, 2, 'stroke-dasharray="4 3"')
         + t(18, 60, "ATFP (línea blanca)", TEAL_D, 10.5, "start") + guia(80, 64, 96, 100, TEAL)
         + t(10, 130, "desinsertada:", ORANGE, 10.5, "start") + t(10, 144, "defecto paravaginal", ORANGE, 10.5, "start"))
    g(s, x, y, p, sc)


def anexo_torsion(s, x, y, lado="der", sc=1.0):
    """Útero y anexos de frente; el anexo del lado indicado está torcido (lienzo 330×220).
    lado = lado de la paciente (der = izquierda del dibujo)."""
    p = (P("M130 60 C130 30 200 30 200 60 L196 130 C190 150 140 150 134 130 Z", PINK, PINK_D, 2) + P("M152 146 L152 176 L178 176 L178 146", PINK, PINK_D, 2)
         + t(165, 100, "útero", PINK_D, 10.5))
    torc = 0 if lado == "der" else 1
    for k, sx in enumerate((1, -1)):
        bx = 165 - sx * 35
        ox = 165 - sx * 110
        tw_ = k == torc
        p += P(f"M{bx} 60 C{bx - sx*30} 40 {ox + sx*30} 40 {ox} 60", "none", "#f472b6", 6, 'stroke-linecap="round"')
        if tw_:
            p += "".join(f'<line x1="{(bx+ox)/2 - 14 + i*7}" y1="44" x2="{(bx+ox)/2 - 8 + i*7}" y2="60" stroke="{ORANGE}" stroke-width="3"/>' for i in range(5))
            p += C(ox, 100, 46, "#7e22ce", "#3b0764", 2.5) + C(ox + 8, 94, 26, "#a855f7", "none", 0, 'opacity="0.6"')
            p += t(ox, 164, "8 cm, torcido", "#581c87", 10.5) + t((bx + ox) / 2, 34, "pedículo girado", ORANGE, 10.5)
        else:
            p += E(ox, 86, 20, 14, "#fde68a", "#ca8a04", 1.6) + t(ox, 118, "ovario normal", MUTED, 10, halo=False)
    p += t(10, 14, "D", MUTED, 11, "start", halo=False) + t(320, 14, "I", MUTED, 11, "end", halo=False)
    g(s, x, y, p, sc)


def utero_frontal(s, x, y, tipo="adenomiosis", sc=1.0):
    """Útero en corte frontal (lienzo 300×240). tipo: adenomiosis | endometrio | tamoxifeno | mioma."""
    grande = tipo == "adenomiosis"
    if grande:
        p = P("M60 40 C60 0 240 0 240 40 L232 150 C224 190 76 190 68 150 Z", "#f9a8d4", PINK_D, 2.5)
        p += "".join(C(cx, cy, 4, "#9d174d", "none", 0, 'opacity="0.7"') for cx, cy in [(90, 60), (210, 70), (100, 130), (200, 140), (150, 30), (120, 100), (190, 104)])
        p += P("M130 60 L170 60 L162 130 L138 130 Z", "#fecdd3", "#be185d", 1.5)
        p += t(150, 210, "Útero grande, globuloso y blando:", "#9d174d", 10.5) + t(150, 224, "endometrio dentro del músculo", "#9d174d", 10.5)
    else:
        p = P("M90 40 C90 10 210 10 210 40 L204 140 C198 170 102 170 96 140 Z", "#f9a8d4", PINK_D, 2.5)
        ancho = {"endometrio": 18, "tamoxifeno": 16, "mioma": 6}[tipo]
        p += P(f"M{150-ancho} 44 L{150+ancho} 44 L{150+ancho*0.5} 140 L{150-ancho*0.5} 140 Z", "#fda4af", "#be185d", 1.5)
        if tipo in ("endometrio", "tamoxifeno"):
            p += (f'<line x1="{150-ancho}" y1="76" x2="{150+ancho}" y2="76" stroke="{TEAL}" stroke-width="2"/>'
                  + t(230, 80, f"{'18 mm' if tipo == 'endometrio' else '> 4-5 mm'}", TEAL_D, 11.5, "start") + guia(228, 76, 150 + ancho, 76, TEAL))
            if tipo == "tamoxifeno":
                p += E(150, 104, 7, 10, "#e11d48", "#9f1239", 1.2) + t(230, 110, "pólipo o hiperplasia", "#9f1239", 10.5, "start")
        if tipo == "mioma":
            p += C(106, 70, 20, "#fef3c7", "#a16207", 2) + C(196, 110, 16, "#fef3c7", "#a16207", 2)
        p += P("M138 160 L138 200 L162 200 L162 160", "#f9a8d4", PINK_D, 2)
        p += t(150, 226, "endometrio" if tipo != "mioma" else "miomas", "#9d174d", 10.5)
    g(s, x, y, p, sc)


def mama(s, x, y, tipo="absceso", lado="izq", sc=1.0):
    """Mama de frente (lienzo 300×240). lado de la paciente: define dónde queda el cuadrante externo."""
    ext = 1 if lado == "izq" else -1       # izq: lo externo (axila) queda a la derecha del dibujo
    p = (C(150, 125, 100, SKIN, SKIN_D, 2) + C(150, 125, 24, "#d6a684", "#9a6b52", 1.5) + C(150, 125, 8, "#9a6b52", "none", 0)
         + "".join(P(f"M{150+18*math.cos(a):.0f} {125+18*math.sin(a):.0f} L{150+80*math.cos(a):.0f} {125+80*math.sin(a):.0f}", "none", "#f9a8d4", 2)
                   for a in [k * math.pi / 4 for k in range(8)])
         + '<line x1="150" y1="22" x2="150" y2="228" stroke="#cbd5e1" stroke-dasharray="4 4"/><line x1="46" y1="125" x2="254" y2="125" stroke="#cbd5e1" stroke-dasharray="4 4"/>'
         + t(150 + ext * 120, 20, "axila", MUTED, 10, halo=False))
    if tipo in ("absceso", "mastitis"):
        cx, cy = 150 + ext * 52, 76
        if tipo == "mastitis":
            p += P(f"M150 125 L{150+ext*96} 60 L{150+ext*60} 30 Z", "#f87171", "none", 0, 'opacity="0.55"')
        else:
            p += C(cx, cy, 34, "#fca5a5", "#b91c1c", 2.5) + C(cx, cy, 18, "#fde68a", "#ca8a04", 1.5)
            p += t(cx, cy - 42, "absceso de 5 cm", "#7f1d1d", 10.5)
        p += t(150 + ext * 60, 236, "cuadrante superoexterno", MUTED, 10, halo=False)
    if tipo == "papiloma":
        p += (P(f"M150 125 L{150+ext*60} 70", "none", "#be185d", 4) + E(150 + ext * 34, 100, 8, 5, "#e11d48", "#881337", 1.2)
              + P("M150 133 q-4 10 0 16 q4 -6 0 -16 Z", RED, "#7f1d1d", 1)
              + t(150 + ext * 30, 172, "papiloma dentro de un conducto", "#881337", 10.5)
              + t(150, 222, "secreción con sangre por el pezón", RED, 10.5))
    g(s, x, y, p, sc)


def gemelar_t(s, x, y, sc=1.0):
    """Esquema ecográfico del signo de la T (monocoriónica biamniótica) (lienzo 330×250)."""
    p = (f'<rect x="0" y="0" width="330" height="250" rx="8" fill="#0b0f19"/>'
         + P("M20 40 C80 20 250 20 310 40 L310 70 C250 56 80 56 20 70 Z", "#94a3b8", "none", 0)
         + t(165, 34, "UNA placenta", "#0b0f19", 11, halo=False)
         + E(96, 150, 68, 76, "#111827", "#475569", 1) + E(234, 150, 68, 76, "#111827", "#475569", 1)
         + '<line x1="165" y1="62" x2="165" y2="230" stroke="#e5e7eb" stroke-width="2"/>'
         + C(96, 150, 22, "#6b7280", "none", 0) + C(234, 150, 22, "#6b7280", "none", 0)
         + t(96, 196, "saco 1", "#9ca3af", 10, halo=False) + t(234, 196, "saco 2", "#9ca3af", 10, halo=False)
         + P("M150 66 L180 66", "none", "#facc15", 3) + P("M165 66 L165 100", "none", "#facc15", 3)
         + t(200, 100, "«T»: membrana fina", "#facc15", 11, "start", halo=False) + t(200, 114, "que llega recta", "#facc15", 11, "start", halo=False))
    g(s, x, y, p, sc)


def pelvis_sinfisis(s, x, y, sc=1.0):
    """Pelvis ósea de frente con la sínfisis del pubis separada (lienzo 330×220)."""
    b, b2 = "#f5f5f4", "#a8a29e"
    p = (P("M160 60 C120 20 60 20 30 50 C14 80 30 120 60 140 L110 170 C130 150 150 130 158 110 Z", b, b2, 2.5)
         + P("M170 60 C210 20 270 20 300 50 C316 80 300 120 270 140 L220 170 C200 150 180 130 172 110 Z", b, b2, 2.5)
         + P("M140 56 H190 L184 120 C176 140 154 140 146 120 Z", "#e7e5e4", b2, 2)
         + P("M84 150 C100 190 130 200 150 196 L150 162 C130 164 110 156 100 146 Z", b, b2, 2)
         + P("M246 150 C230 190 200 200 180 196 L180 162 C200 164 220 156 230 146 Z", b, b2, 2)
         + f'<rect x="150" y="160" width="30" height="40" fill="#fee2e2" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/>'
         + flecha(160, 214, 130, 214, RED, 2) + flecha(170, 214, 200, 214, RED, 2)
         + t(165, 238, "sínfisis separada: dolor que impide caminar", "#7f1d1d", 10.5))
    g(s, x, y, p, sc)


def formula_obstetrica(s, x, y, G=3, P4=(1, 1, 1, 2), sc=1.0, resaltar=(0, 1, 2, 3, 4)):
    """Recuadros G y P (T-P-A-V) (lienzo 470×150)."""
    labs = [("G", str(G), "gestaciones"), ("T", str(P4[0]), "a término"), ("P", str(P4[1]), "pretérmino"),
            ("A", str(P4[2]), "abortos"), ("V", str(P4[3]), "hijos vivos")]
    p = ""
    for k, (l, v, desc) in enumerate(labs):
        bx = 10 + k * 92 + (16 if k > 0 else 0)
        on = k in resaltar
        p += f'<rect x="{bx}" y="20" width="80" height="80" rx="12" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{2.5 if on else 1.3}"/>'
        p += t(bx + 40, 72, v, ORANGE if on else INK, 34, halo=False) + t(bx + 40, 16, l, TEAL_D, 12, halo=False)
        p += t(bx + 40, 118, desc, SLATE, 10.5, fw=700, halo=False)
    p += t(115, 140, "P = T · P · A · V", MUTED, 10.5, halo=False)
    g(s, x, y, p, sc)


def gestante(s, x, y, zonas=None, marcas=(), extra="", rotulos=(), sc=1.0):
    """Mujer embarazada de frente (cuerpo + útero grávido)."""
    panza = (E(120, 208, 64, 54, SKIN, SKIN_D, 2) + C(120, 214, 2.5, "#9a6b52", "none", 0))
    cuerpo(s, x, y, zonas, marcas, panza + extra, rotulos, sc)


def alveolo(s, x, y, sc=1.0):
    """Alveolos sin y con surfactante (lienzo 360×190)."""
    p = ""
    for k, (tit, ok) in enumerate((("Sin surfactante", False), ("Con surfactante", True))):
        cx = 90 + k * 180
        p += f'<rect x="{cx-84}" y="4" width="168" height="182" rx="10" fill="{ORANGE_L if ok else "#ffffff"}" stroke="{ORANGE if ok else "#cbd5e1"}" stroke-width="{2.5 if ok else 1.3}"/>'
        if ok:
            p += C(cx, 90, 52, "#e0f2fe", "#0369a1", 2) + C(cx, 90, 48, "none", "#facc15", 3, 'stroke-dasharray="3 3"')
            p += E(cx - 44, 118, 10, 7, "#fde68a", "#ca8a04", 1.2) + t(cx, 164, "Abierto: se ventila", "#0369a1", 10.5)
            p += t(cx + 40, 34, "surfactante", "#a16207", 10, halo=False)
        else:
            p += P(f"M{cx-40} 90 C{cx-30} 70 {cx+30} 70 {cx+40} 90 C{cx+30} 104 {cx-30} 104 {cx-40} 90 Z", "#e0f2fe", "#0369a1", 2)
            p += t(cx, 164, "Colapsa: membrana hialina", "#b91c1c", 10.5)
        p += t(cx, 24, tit, INK, 11.5)
    p += t(270, 130, "neumocito II", "#a16207", 9.5, "start", halo=False)
    g(s, x, y, p, sc)


def tira_orina(s, x, y, valores, sc=1.0):
    """Tira reactiva: valores = [(nombre, color, texto, on)] (lienzo 460×120)."""
    n = len(valores)
    p = f'<rect x="10" y="30" width="{n*66+20}" height="30" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>'
    for k, (nom, col, txt, on) in enumerate(valores):
        bx = 22 + k * 66
        p += f'<rect x="{bx}" y="34" width="42" height="22" rx="3" fill="{col}" stroke="{ORANGE if on else "#94a3b8"}" stroke-width="{3 if on else 1}"/>'
        p += t(bx + 21, 22, nom, INK if on else SLATE, 10, fw=800 if on else 600, halo=False)
        p += t(bx + 21, 78, txt, ORANGE if on else SLATE, 11, fw=800, halo=False)
    g(s, x, y, p, sc)


def curva_percentil(s, x, y, punto=(0.8, 0.28), xlab="Semanas", ylab="Peso", ticks=("24", "28", "32", "36", "40"),
                    etiquetas=("p97", "p90", "p50", "p10", "p3"), marca="este caso", sc=1.0, r=7):
    """Curvas de percentiles genéricas; punto en fracciones (x, y) del área (y=0 abajo) (lienzo 340×230)."""
    X0_, Y0_, W_, H_ = 44, 12, 250, 180
    p = f'<rect x="{X0_}" y="{Y0_}" width="{W_}" height="{H_}" fill="#f8fafc" stroke="#cbd5e1"/>'
    offs = [0.9, 0.78, 0.55, 0.33, 0.22]
    for k, (o, lab) in enumerate(zip(offs, etiquetas)):
        pts = " ".join(f"{X0_+i/20*W_:.1f},{Y0_+H_-(o*(0.35+0.65*i/20)**1.1)*H_:.1f}" for i in range(21))
        p += f'<polyline points="{pts}" fill="none" stroke="{TEAL if lab == "p50" else "#94a3b8"}" stroke-width="{2 if lab == "p50" else 1.4}"/>'
        p += t(X0_ + W_ + 4, Y0_ + H_ - o * H_ + 4, lab, TEAL_D if lab == "p50" else MUTED, 10, "start", 700, halo=False)
    for k, tk in enumerate(ticks):
        p += t(X0_ + k * W_ / (len(ticks) - 1), Y0_ + H_ + 14, tk, MUTED, 10, halo=False)
    px, py = X0_ + punto[0] * W_, Y0_ + H_ - punto[1] * H_
    p += C(px, py, r, ORANGE, "#7c2d12", 2) + t(px - 10, py + 22, marca, "#9a3412", 10.5, "end")
    p += t(X0_ + W_ / 2, Y0_ + H_ + 30, xlab, MUTED, 10, halo=False) + t(8, Y0_ + 10, ylab, MUTED, 10, "start", halo=False)
    g(s, x, y, p, sc)


def eje_hho(s, x, y, bloqueo=True, sc=1.0):
    """Eje hipotálamo-hipófisis-ovario con la retroalimentación de estrógenos (lienzo 300×290)."""
    p = (E(150, 34, 70, 22, "#e0e7ff", "#6366f1", 2) + t(150, 39, "Hipotálamo", "#3730a3", 11)
         + flecha(150, 58, 150, 94, "#6366f1", 2.4) + t(160, 80, "GnRH", "#3730a3", 10.5, "start")
         + E(150, 116, 52, 20, "#fae8ff", "#a21caf", 2) + t(150, 121, "Hipófisis", "#86198f", 11)
         + flecha(150, 138, 150, 176, "#a21caf", 2.4) + t(160, 162, "FSH y LH", "#86198f", 10.5, "start")
         + E(150, 206, 62, 30, "#fef3c7", "#ca8a04", 2) + C(170, 202, 16, "#ffffff", "#ca8a04", 1.5) + t(128, 210, "Ovario", "#92400e", 11)
         + t(208, 246, "folículo → ovulación", "#92400e", 10.5)
         + P("M86 206 C30 180 30 60 80 36", "none", RED, 2.4, 'stroke-dasharray="6 4"') + t(6, 128, "estrógenos (–)", RED, 10.5, "start"))
    if bloqueo:
        p += (C(80, 36, 13, "#ffffff", ORANGE, 3) + P("M72 28 L88 44 M88 28 L72 44", "none", ORANGE, 3)
              + t(20, 276, "Clomifeno bloquea el receptor: el hipotálamo", ORANGE, 10.5, "start")
              + t(20, 290, "«no ve» estrógenos y sube la GnRH", ORANGE, 10.5, "start"))
    g(s, x, y, p, sc)


def vwf(s, x, y, sc=1.0):
    """Adhesión plaquetaria: el factor de von Willebrand une colágeno y plaqueta y transporta el FVIII (lienzo 360×200)."""
    p = (f'<rect x="0" y="150" width="360" height="40" fill="#fecaca"/>' + t(180, 176, "colágeno expuesto (vaso lesionado)", "#7f1d1d", 10.5)
         + P("M40 150 Q60 120 90 130 Q120 140 140 110 Q160 80 190 96", "none", "#7c3aed", 5, 'stroke-linecap="round"')
         + E(220, 80, 44, 26, "#fde68a", "#ca8a04", 2) + t(220, 84, "plaqueta", "#92400e", 10.5)
         + C(190, 96, 6, "#16a34a", "none", 0) + t(196, 120, "GPIb", "#15803d", 10, "start")
         + C(100, 128, 9, "#0ea5e9", "#0369a1", 1.5) + t(100, 110, "FVIII", "#0369a1", 10.5)
         + t(20, 40, "Factor de von Willebrand (violeta):", "#6d28d9", 10.5, "start")
         + t(20, 54, "puente entre colágeno y plaqueta", "#6d28d9", 10.5, "start")
         + t(20, 68, "y protege al factor VIII", "#6d28d9", 10.5, "start"))
    g(s, x, y, p, sc)


def bebe(s, x, y, zonas=None, marcas=(), extra="", rotulos=(), sc=1.0):
    """Lactante de frente (lienzo 240×330). zonas: cabeza, torax, abdomen, brazo_d/i, pierna_d/i, higado."""
    z = zonas or {}
    f = lambda k: z.get(k, SKIN)
    p = (P("M76 128 C72 110 168 110 164 128 L172 222 C160 248 80 248 68 222 Z", f("torax"), SKIN_D, 2)
         + P("M72 180 H168 L172 222 C160 248 80 248 68 222 Z", f("abdomen"), SKIN_D, 2)
         + P("M76 132 L40 170 L52 184 L82 156 Z", f("brazo_d"), SKIN_D, 2) + P("M164 132 L200 170 L188 184 L158 156 Z", f("brazo_i"), SKIN_D, 2)
         + C(44, 182, 10, f("brazo_d"), SKIN_D, 2) + C(196, 182, 10, f("brazo_i"), SKIN_D, 2)
         + P("M84 236 L70 300 L94 304 L108 244 Z", f("pierna_d"), SKIN_D, 2) + P("M156 236 L170 300 L146 304 L132 244 Z", f("pierna_i"), SKIN_D, 2)
         + E(80, 308, 14, 7, f("pierna_d"), SKIN_D, 2) + E(160, 308, 14, 7, f("pierna_i"), SKIN_D, 2)
         + C(120, 70, 54, f("cabeza"), SKIN_D, 2)
         + C(100, 66, 4, "#334155", "none", 0) + C(140, 66, 4, "#334155", "none", 0)
         + '<path d="M110 96 Q120 102 130 96" fill="none" stroke="#9a6b52" stroke-width="2"/>'
         + P("M116 76 Q120 86 124 76", "none", "#9a6b52", 2) + C(120, 214, 3, "#9a6b52", "none", 0))
    if "higado" in z:
        p += P("M74 184 C96 176 140 178 150 190 C140 210 96 214 76 206 Z", z["higado"], "#9a3412", 1.8, 'opacity="0.85"')
    p += extra
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    g(s, x, y, p, sc)


def embarazos_linea(s, x, y, items, sc=1.0):
    """Lista vertical de embarazos: items = [(título, detalle, cuenta_como, color)] (lienzo 220×400)."""
    p = '<line x1="30" y1="20" x2="30" y2="320" stroke="#cbd5e1" stroke-width="3"/>'
    n = len(items)
    for k, (tit, det, cuenta, col) in enumerate(items):
        yy = 30 + k * (280 / max(n - 1, 1)) if n > 1 else 60
        p += C(30, yy, 16, col, "#ffffff", 3) + t(30, yy + 5, str(k + 1), "#ffffff", 12, halo=False)
        p += t(56, yy - 4, tit, INK, 11.5, "start", halo=False) + t(56, yy + 12, det, SLATE, 10.5, "start", 600, halo=False)
        p += f'<rect x="56" y="{yy+20}" width="{len(cuenta)*6.4+14:.0f}" height="18" rx="9" fill="{ORANGE_L}" stroke="{ORANGE}"/>'
        p += t(63, yy + 33, cuenta, "#9a3412", 10, "start", halo=False)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ RX DE TÓRAX DIBUJADA (lienzo 300×280)
def torax_rx(s, x, y, patron="normal", lado="der", sc=1.0, rotulos=(), marcas=()):
    """Rx PA esquemática. patron: normal | intersticial | consolidacion | hiperinsuflacion | derrame | cavidad |
    nivel | edema | sdra | fibrosis | neumotorax | dbp. lado de la lesión = lado del paciente (der = izquierda del dibujo)."""
    p = ('<rect x="0" y="0" width="300" height="280" rx="8" fill="#0b1220"/>'
         + P("M40 40 C40 20 130 16 140 40 L140 240 C100 250 50 246 30 230 C24 170 26 90 40 40 Z", "#1f2937", "none", 0)
         + P("M260 40 C260 20 170 16 160 40 L160 240 C200 250 250 246 270 230 C276 170 274 90 260 40 Z", "#1f2937", "none", 0)
         + "".join(f'<path d="M{34+k*2} {60+k*30} Q90 {40+k*30} 146 {70+k*30}" fill="none" stroke="#475569" stroke-width="3"/>'
                   f'<path d="M{266-k*2} {60+k*30} Q210 {40+k*30} 154 {70+k*30}" fill="none" stroke="#475569" stroke-width="3"/>' for k in range(6))
         + '<rect x="140" y="10" width="20" height="260" fill="#64748b"/>'
         + P("M126 120 C110 150 112 210 140 232 L200 232 C226 214 218 150 170 128 Z", "#94a3b8", "none", 0)
         + P("M30 236 Q80 212 140 238 M160 238 Q220 212 270 236", "none", "#cbd5e1", 4)
         + t(14, 18, "D", "#94a3b8", 12, "start", halo=False) + t(286, 18, "I", "#94a3b8", 12, "end", halo=False))
    L_ = lado == "der"
    xl = 80 if L_ else 220
    if patron == "intersticial":
        import random as _r
        rr = _r.Random(3)
        p += "".join(f'<circle cx="{rr.uniform(40,136) if i%2 else rr.uniform(164,262):.0f}" cy="{rr.uniform(50,226):.0f}" r="1.8" fill="#e2e8f0" opacity="0.7"/>' for i in range(260))
        p += "".join(f'<path d="M{rr.uniform(40,130):.0f} {rr.uniform(50,220):.0f} l{rr.uniform(-12,12):.0f} {rr.uniform(-12,12):.0f}" stroke="#cbd5e1" stroke-width="1" opacity="0.6"/>' for _ in range(60))
    elif patron == "consolidacion":
        p += E(xl, 170 if L_ else 160, 44, 40, "#e5e7eb", "none", 0, extra='opacity="0.85"')
        p += "".join(f'<path d="M{xl-20+k*10} {160+k*6} l16 -4" stroke="#1f2937" stroke-width="2"/>' for k in range(4))
    elif patron == "hiperinsuflacion":
        p += P("M30 250 Q80 236 140 252 M160 252 Q220 236 270 250", "none", "#cbd5e1", 4)
    elif patron == "derrame":
        p += P(f"M{30 if L_ else 160} 160 Q{90 if L_ else 250} 176 {140 if L_ else 270} 150 L{140 if L_ else 270} 240 L{30 if L_ else 160} 240 Z", "#e5e7eb", "none", 0)
    elif patron in ("cavidad", "nivel"):
        cy_ = 80 if patron == "cavidad" else 150
        p += C(xl, cy_, 28, "#e5e7eb", "none", 0) + C(xl, cy_, 18, "#0b1220", "none", 0)
        if patron == "nivel":
            p += f'<rect x="{xl-18}" y="{cy_}" width="36" height="18" fill="#e5e7eb"/>' + f'<line x1="{xl-18}" y1="{cy_}" x2="{xl+18}" y2="{cy_}" stroke="#ffffff" stroke-width="2"/>'
        else:
            p += "".join(C(xl + dx, cy_ + dy, 3, "#e5e7eb", "none", 0) for dx, dy in [(-40, 30), (30, 36), (-20, 50), (20, 60)])
    elif patron in ("edema", "sdra"):
        for cx_ in (90, 210):
            p += E(cx_, 150, 48, 70, "#e5e7eb", "none", 0, extra='opacity="0.55"')
        if patron == "edema":
            p += P("M110 110 C80 150 90 200 140 236 L204 236 C240 200 222 140 180 118 Z", "#cbd5e1", "none", 0)
    elif patron == "fibrosis":
        import random as _r
        rr = _r.Random(5)
        for cx_ in (70, 230):
            p += "".join(C(cx_ + rr.uniform(-30, 30), rr.uniform(150, 226), rr.uniform(4, 7), "none", "#e2e8f0", 1.4) for _ in range(26))
    elif patron == "neumotorax":
        p += P(f"M{130 if L_ else 170} 60 C{100 if L_ else 200} 90 {100 if L_ else 200} 180 {130 if L_ else 170} 210", "none", "#e5e7eb", 2)
    elif patron == "dbp":
        import random as _r
        rr = _r.Random(8)
        p += "".join(f'<path d="M{rr.uniform(40,130) if i%2 else rr.uniform(170,260):.0f} {rr.uniform(50,220):.0f} l{rr.uniform(-18,18):.0f} {rr.uniform(-18,18):.0f}" stroke="#e5e7eb" stroke-width="2" opacity="0.7"/>' for i in range(60))
        p += "".join(C(rr.uniform(44, 128) if i % 2 else rr.uniform(172, 256), rr.uniform(60, 210), rr.uniform(5, 9), "#0b1220", "#94a3b8", 1) for i in range(12))
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += f'<text x="{rx_}" y="{ry_}" font-size="10.5" font-weight="800" fill="#facc15" text-anchor="{anc}" data-max="0">{escape(txt)}</text>'
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ NIÑO DE PIE (lienzo 220×380)
def nino(s, x, y, zonas=None, marcas=(), extra="", rotulos=(), sc=1.0, obeso=False, genu_varo=False):
    """Niño de frente. zonas: cabeza, torax, abdomen, brazo_d/i, pierna_d/i, mano_d/i."""
    z = zonas or {}
    f = lambda k: z.get(k, SKIN)
    tw_ = 30 if obeso else 0
    p = (C(110, 56, 42, f("cabeza"), SKIN_D, 2) + C(95, 52, 3.5, "#334155", "none", 0) + C(125, 52, 3.5, "#334155", "none", 0)
         + '<path d="M100 74 Q110 80 120 74" fill="none" stroke="#9a6b52" stroke-width="2"/>'
         + f'<rect x="102" y="96" width="16" height="10" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="2"/>'
         + P(f"M{74-tw_/2} 106 H{146+tw_/2} L{150+tw_/2} 170 H{70-tw_/2} Z", f("torax"), SKIN_D, 2)
         + P(f"M{70-tw_/2} 170 H{150+tw_/2} C{154+tw_} 206 {148+tw_/2} 222 {144+tw_/2} 232 H{76-tw_/2} C{72-tw_/2} 222 {66-tw_} 206 {70-tw_/2} 170 Z", f("abdomen"), SKIN_D, 2)
         + P(f"M{74-tw_/2} 110 L{50-tw_/2} 120 L{40-tw_/2} 214 L{56-tw_/2} 216 L{70-tw_/2} 150 Z", f("brazo_d"), SKIN_D, 2)
         + P(f"M{146+tw_/2} 110 L{170+tw_/2} 120 L{180+tw_/2} 214 L{164+tw_/2} 216 L{150+tw_/2} 150 Z", f("brazo_i"), SKIN_D, 2)
         + C(48 - tw_ / 2, 224, 10, f("mano_d"), SKIN_D, 2) + C(172 + tw_ / 2, 224, 10, f("mano_i"), SKIN_D, 2))
    if genu_varo:
        p += P("M80 232 L106 232 Q86 300 104 364 L84 364 Q56 300 80 232 Z", f("pierna_d"), SKIN_D, 2)
        p += P("M114 232 L140 232 Q164 300 136 364 L116 364 Q134 300 114 232 Z", f("pierna_i"), SKIN_D, 2)
    else:
        p += P("M80 232 H106 L104 364 H84 Z", f("pierna_d"), SKIN_D, 2) + P("M114 232 H140 L136 364 H116 Z", f("pierna_i"), SKIN_D, 2)
    p += E(92, 370, 14, 6, SKIN, SKIN_D, 2) + E(128, 370, 14, 6, SKIN, SKIN_D, 2)
    p += extra
    for n, mx, my in marcas:
        p += num(mx, my, n)
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    g(s, x, y, p, sc)


def puntos_piel(zona_bbox, n, col="#b91c1c", r=(2.5, 4), seed=1, op=0.85):
    """Lesiones puntiformes aleatorias dentro de un rectángulo (x0, y0, x1, y1)."""
    import random as _r
    rr = _r.Random(seed)
    x0, y0, x1, y1 = zona_bbox
    return "".join(C(f"{rr.uniform(x0,x1):.1f}", f"{rr.uniform(y0,y1):.1f}", f"{rr.uniform(*r):.1f}", col, "none", 0, f'opacity="{op}"') for _ in range(n))


# ════════════════════════════════════════════════════════════ TINCIÓN DE GRAM (lienzo 220×160)
def gram(s, x, y, tipo="cocos_cadena", sc=1.0):
    """Campo de microscopio. tipo: cocos_cadena | cocos_racimo | diplococos | bacilos_neg | bacilos_pos | cocobacilos."""
    import random as _r
    rr = _r.Random(4)
    pos = tipo in ("cocos_cadena", "cocos_racimo", "diplococos", "bacilos_pos")
    col = "#6d28d9" if pos else "#e11d48"
    p = C(110, 80, 76, "#fdf4ff" if pos else "#fff1f2", "#94a3b8", 3)
    for k in range(8):
        cx, cy = 60 + rr.uniform(0, 100), 40 + rr.uniform(0, 80)
        if tipo == "cocos_cadena":
            p += "".join(C(cx + i * 7, cy + i * 2, 3.2, col, "none", 0) for i in range(5))
        elif tipo == "cocos_racimo":
            p += "".join(C(cx + rr.uniform(-7, 7), cy + rr.uniform(-7, 7), 3.2, col, "none", 0) for _ in range(6))
        elif tipo == "diplococos":
            p += C(cx, cy, 3.4, col, "none", 0) + C(cx + 7, cy, 3.4, col, "none", 0)
        elif tipo in ("bacilos_neg", "bacilos_pos"):
            p += f'<rect x="{cx:.0f}" y="{cy:.0f}" width="13" height="5" rx="2.5" fill="{col}" transform="rotate({rr.uniform(0,180):.0f} {cx:.0f} {cy:.0f})"/>'
        else:
            p += f'<rect x="{cx:.0f}" y="{cy:.0f}" width="7" height="4.5" rx="2.2" fill="{col}"/>'
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ FROTIS DE SANGRE (lienzo 300×200)
def frotis(s, x, y, tipo="normal", sc=1.0):
    """tipo: normal | microcitica | esferocitos | drepanocitos | blastos_auer | vivax | hemofagocito | plaquetas_bajas."""
    import random as _r
    rr = _r.Random(11)
    p = f'<rect x="0" y="0" width="300" height="200" rx="10" fill="#fdf2f8"/>'
    pts = [(rr.uniform(16, 284), rr.uniform(16, 184)) for _ in range(34)]
    for i, (cx, cy) in enumerate(pts):
        if tipo == "microcitica":
            p += C(cx, cy, 9, "#fecdd3", "#e11d48", 1.2) + C(cx, cy, 6, "#fff1f2", "none", 0)
        elif tipo == "esferocitos" and i % 3 == 0:
            p += C(cx, cy, 9, "#e11d48", "#9f1239", 1)
        elif tipo == "drepanocitos" and i % 3 == 0:
            p += P(f"M{cx-12} {cy} Q{cx} {cy-12} {cx+12} {cy} Q{cx} {cy-5} {cx-12} {cy} Z", "#e11d48", "#9f1239", 1)
        else:
            p += C(cx, cy, 12, "#fda4af", "#e11d48", 1) + C(cx, cy, 4.5, "#fecdd3", "none", 0)
        if tipo == "vivax" and i % 7 == 0:
            p += C(cx, cy, 14, "#fbcfe8", "#be185d", 1) + P(f"M{cx-6} {cy} q6 -8 12 0", "none", "#6d28d9", 2) + C(cx + 6, cy, 2, "#7f1d1d", "none", 0)
    if tipo == "blastos_auer":
        for cx, cy in [(80, 70), (200, 120), (140, 150)]:
            p += C(cx, cy, 24, "#c4b5fd", "#6d28d9", 1.5) + C(cx, cy, 17, "#7c3aed", "none", 0)
            p += f'<line x1="{cx-8}" y1="{cy-24}" x2="{cx+10}" y2="{cy-10}" stroke="#be123c" stroke-width="2.5"/>'
    if tipo == "hemofagocito":
        p += C(150, 100, 46, "#e9d5ff", "#7c3aed", 2) + C(130, 90, 10, "#fda4af", "#e11d48", 1) + C(160, 110, 10, "#fda4af", "#e11d48", 1) + C(150, 80, 6, "#6d28d9", "none", 0)
    if tipo == "plaquetas_bajas":
        p += C(60, 60, 3, "#7c3aed", "none", 0)
    elif tipo == "normal":
        p += "".join(C(rr.uniform(20, 280), rr.uniform(20, 180), 2.5, "#7c3aed", "none", 0) for _ in range(10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CEREBRO EN CORTE (TC o eco) (lienzo 280×260)
def tc_craneo(s, x, y, lesion="normal", estilo="tc", sc=1.0):
    """lesion: normal | cmv | toxo | ncc | lacunas | epidural | edema | occipital | ventriculos."""
    bg = "#0b1220"
    p = f'<rect x="0" y="0" width="280" height="260" rx="10" fill="{bg}"/>'
    if estilo == "eco":
        p += P("M140 10 L14 250 Q140 290 266 250 Z", "#1f2937", "none", 0)
    p += E(140, 132, 116, 118, "#e5e7eb" if estilo == "tc" else "none", "#e5e7eb" if estilo == "eco" else "none", 0 if estilo == "tc" else 1)
    p += E(140, 132, 106, 108, "#6b7280", "none", 0)
    grande = lesion in ("cmv", "ventriculos")
    vw = 18 if grande else 9
    p += P(f"M{128-vw} 96 C{120-vw} 120 {122-vw} 150 {132-vw/2} 164 L136 150 L136 100 Z", "#111827", "none", 0)
    p += P(f"M{152+vw} 96 C{160+vw} 120 {158+vw} 150 {148+vw/2} 164 L144 150 L144 100 Z", "#111827", "none", 0)
    if lesion == "cmv":
        p += "".join(C(cx, cy, 4, "#ffffff", "none", 0) for cx, cy in [(104, 100), (100, 124), (106, 150), (176, 100), (180, 126), (174, 152)])
    elif lesion == "toxo":
        p += "".join(C(cx, cy, 4, "#ffffff", "none", 0) for cx, cy in [(70, 90), (210, 160), (120, 200), (190, 70), (90, 180)])
    elif lesion == "ncc":
        for cx, cy in [(80, 110), (200, 150), (170, 70)]:
            p += C(cx, cy, 13, "#0f172a", "#cbd5e1", 1.5) + C(cx + 4, cy - 3, 3, "#f8fafc", "none", 0)
        p += C(100, 190, 5, "#ffffff", "none", 0)
    elif lesion == "lacunas":
        p += "".join(C(cx, cy, 5, "#111827", "none", 0) for cx, cy in [(116, 120), (164, 128), (126, 150), (158, 104), (112, 96)])
    elif lesion == "epidural":
        p += P("M40 80 C30 120 34 160 50 190 C66 170 70 120 60 84 Z", "#f8fafc", "none", 0)
        p += P("M150 40 L150 230", "none", "#fbbf24", 1.5, 'stroke-dasharray="4 3"')
    elif lesion == "edema":
        p += E(140, 132, 106, 108, "#9ca3af", "none", 0, 'opacity="0.35"')
    elif lesion == "occipital":
        p += P("M100 220 C120 236 160 236 180 220 L170 190 C150 200 130 200 110 190 Z", "#374151", "none", 0)
    p += t(140, 250, "adelante ↑" if estilo == "tc" else "", "#94a3b8", 9.5, halo=False)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ RIÑONES Y VÍAS URINARIAS (lienzo 300×280)
def rinon_vias(s, x, y, opcion="normal", lado="der", sc=1.0, rotulos=()):
    """opcion: normal | pielonefritis | rvu | litiasis | trauma | hidronefrosis | rinones_pequenos | prostata."""
    p = (P("M50 40 C20 50 20 130 50 140 C70 146 84 120 76 90 C84 60 70 34 50 40 Z", ORG["rinon"], "#9f1239", 2)
         + P("M250 40 C280 50 280 130 250 140 C230 146 216 120 224 90 C216 60 230 34 250 40 Z", ORG["rinon"], "#9f1239", 2)
         + P("M76 96 C90 150 118 200 136 232", "none", "#fde68a", 7, 'stroke-linecap="round"')
         + P("M224 96 C210 150 182 200 164 232", "none", "#fde68a", 7, 'stroke-linecap="round"')
         + E(150, 244, 44, 30, ORG["vejiga"], "#ca8a04", 2) + t(150, 250, "vejiga", "#a16207", 10, halo=False)
         + t(10, 16, "D", MUTED, 11, "start", halo=False) + t(290, 16, "I", MUTED, 11, "end", halo=False))
    xk = 50 if lado == "der" else 250
    if opcion == "pielonefritis":
        p += P(f"M{xk} 40 C{xk-30 if lado=='der' else xk+30} 50 {xk-30 if lado=='der' else xk+30} 130 {xk} 140", "none", ORANGE, 5)
        p += "".join(C(xk + dx, 70 + dy, 4, ORANGE, "none", 0) for dx, dy in [(-6, 0), (4, 20), (-4, 40), (6, 54)])
    elif opcion == "rvu":
        p += P("M76 96 C90 150 118 200 136 232", "none", "#fbbf24", 14, 'stroke-linecap="round" opacity="0.8"')
        p += "".join(flecha(128 - k * 16, 214 - k * 36, 120 - k * 16, 196 - k * 36, ORANGE, 2.2) for k in range(3))
        p += P("M50 60 C40 70 40 110 50 120", "none", "#fbbf24", 8)
        p += t(96, 150, "orina que sube", ORANGE, 10.5, "start")
    elif opcion == "litiasis":
        p += piedra(112 if lado == "der" else 188, 196, 6)
        p += P("M76 96 C86 130 100 170 110 190", "none", "#fbbf24", 11, 'stroke-linecap="round"') if lado == "der" else ""
    elif opcion == "trauma":
        p += P(f"M{xk-8} 60 L{xk+6} 80 L{xk-6} 96 L{xk+8} 116", "none", "#7f1d1d", 4)
        p += E(xk + (22 if lado == "izq" else -22), 100, 22, 40, "#b91c1c", "none", 0, 'opacity="0.55"')
    elif opcion == "rinones_pequenos":
        p = p.replace("M50 40 C20 50 20 130 50 140", "M50 60 C34 66 34 116 50 122").replace("M250 40 C280 50 280 130 250 140", "M250 60 C266 66 266 116 250 122")
    elif opcion == "prostata":
        p += E(150, 280, 26, 14, "#fdba74", "#c2410c", 2) + t(186, 284, "próstata", "#c2410c", 10, "start")
    for rx_, ry_, txt, anc in rotulos:
        p += t(rx_, ry_, txt, INK, 10.5, anc)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ GLOMÉRULO (lienzo 260×220)
def glomerulo(s, x, y, tipo="normal", sc=1.0):
    """tipo: normal | cambios_minimos | membranosa | proliferativo (lupus IV)."""
    p = C(130, 110, 96, "#f8fafc", "#94a3b8", 3) + t(130, 214, "cápsula de Bowman", MUTED, 10, halo=False)
    loops = [(100, 80), (150, 70), (180, 110), (160, 150), (110, 150), (90, 115), (130, 112)]
    for cx, cy in loops:
        p += C(cx, cy, 24, "#fecaca", "#b91c1c", 2)
        if tipo == "membranosa":
            p += "".join(C(cx + 24 * math.cos(a), cy + 24 * math.sin(a), 3, "#1d4ed8", "none", 0) for a in [k * math.pi / 5 for k in range(10)])
        if tipo == "proliferativo":
            p += "".join(C(cx + rx_, cy + ry_, 3.2, "#4c1d95", "none", 0) for rx_, ry_ in [(-8, -6), (6, 4), (-4, 10), (9, -9)])
            p += C(cx, cy, 24, "none", "#f59e0b", 4, 'opacity="0.7"')
    if tipo == "cambios_minimos":
        p += t(130, 34, "podocitos con pies «borrados»", "#9f1239", 10)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ OTROS PEDIÁTRICOS
def hematocrito(s, x, y, valor=68, sc=1.0):
    """Tubo capilar con el hematocrito (lienzo 220×230)."""
    H = 180
    p = (f'<rect x="80" y="20" width="36" height="{H}" rx="6" fill="#fef9c3" stroke="#64748b" stroke-width="2"/>'
         + f'<rect x="82" y="{20+H-H*valor/100:.0f}" width="32" height="{H*valor/100-2:.0f}" rx="4" fill="#b91c1c"/>'
         + f'<rect x="82" y="{20+H-H*valor/100-4:.0f}" width="32" height="4" fill="#f8fafc"/>'
         + t(130, 20 + H - H * valor / 100 + 6, f"{valor} %", "#7f1d1d", 14, "start")
         + f'<line x1="70" y1="{20+H-H*0.65:.0f}" x2="126" y2="{20+H-H*0.65:.0f}" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="4 3"/>'
         + t(66, 20 + H - H * 0.65 + 4, "65 %", ORANGE, 10.5, "end") + t(98, 224, "plasma arriba, glóbulos rojos abajo", MUTED, 10))
    g(s, x, y, p, sc)


def vasos(s, x, y, caso=3, sc=1.0):
    """Cuatro bebidas con sus cucharaditas de azúcar (lienzo 440×170)."""
    it = [("Gaseosa", "#78350f", 8), ("Jugo envasado", "#f59e0b", 6), ("Leche entera", "#f8fafc", 3), ("Agua", "#bae6fd", 0)]
    p = ""
    for k, (nom, col, az) in enumerate(it):
        cx = 56 + k * 108
        on = k == caso
        p += f'<rect x="{cx-50}" y="2" width="100" height="164" rx="10" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{2.5 if on else 1.2}"/>'
        p += P(f"M{cx-22} 20 L{cx-16} 96 H{cx+16} L{cx+22} 20 Z", "#ffffff", "#94a3b8", 2) + P(f"M{cx-20} 36 L{cx-16} 96 H{cx+16} L{cx+20} 36 Z", col, "none", 0, 'opacity="0.85"')
        p += "".join(f'<rect x="{cx-34+(i%4)*18}" y="{106+(i//4)*12}" width="12" height="9" rx="2" fill="#ffffff" stroke="#94a3b8"/>' for i in range(az))
        p += t(cx, 150, nom, ORANGE if on else INK, 10.5) + t(cx, 162, f"{az} cdtas de azúcar" if az else "sin azúcar", SLATE, 9.5, fw=600)
    g(s, x, y, p, sc)


def columna_disrafia(s, x, y, tipo="oculta", sc=1.0):
    """Corte transversal de la columna lumbar: oculta | meningocele | mielomeningocele (lienzo 220×244)."""
    p = (P("M20 200 H180", "none", SKIN_D, 5) + t(100, 214, "piel", MUTED, 10, halo=False)
         + C(100, 60, 34, "#e7e5e4", "#a8a29e", 3) + C(100, 60, 16, "#fef3c7", "#ca8a04", 2) + t(100, 64, "médula", "#92400e", 9, halo=False)
         + P("M70 80 L60 130 M130 80 L140 130", "none", "#a8a29e", 10, 'stroke-linecap="round"'))
    if tipo == "oculta":
        p += P("M60 130 L84 150 M140 130 L116 150", "none", "#a8a29e", 10, 'stroke-linecap="round"')
        p += E(100, 196, 8, 5, "#9a6b52", "none", 0) + "".join(f'<path d="M{96+i*2} 192 q-4 -14 -2 -24" stroke="#1f2937" stroke-width="1.4" fill="none"/>' for i in range(5))
        p += t(116, 172, "mechón de pelo", "#9a3412", 10, "start") + t(116, 186, "y hoyuelo", "#9a3412", 10, "start")
    elif tipo == "meningocele":
        p += P("M70 130 C40 196 60 222 100 222 C140 222 160 196 130 130", "#bae6fd", "#0369a1", 2)
        p += t(100, 238, "solo meninges y LCR", "#0369a1", 10)
    else:
        p += P("M70 130 C40 196 60 222 100 222 C140 222 160 196 130 130", "#fecaca", "#b91c1c", 2)
        p += P("M100 76 L100 206", "none", "#ca8a04", 6) + t(100, 238, "médula y raíces afuera", "#b91c1c", 10)
    g(s, x, y, p, sc)


def esofago_caustico(s, x, y, tipo="alcali", sc=1.0):
    """Esófago y estómago con la lesión cáustica (lienzo 220×260)."""
    p = (P("M100 10 L100 150 C100 170 80 190 90 210 C110 250 190 250 200 200 C206 170 170 150 124 152 L124 10 Z", "#fbcfe8", "#be185d", 2)
         + t(150, 30, "esófago", "#9d174d", 10.5, "start") + t(150, 256, "estómago", "#9d174d", 10.5))
    if tipo == "alcali":
        p += P("M100 30 L100 150 L124 150 L124 30 Z", "#7f1d1d", "none", 0, 'opacity="0.8"')
        p += "".join(f'<path d="M{96} {40+k*22} l-8 6 M{128} {50+k*22} l8 6" stroke="#7f1d1d" stroke-width="2"/>' for k in range(5))
        p += t(82, 96, "necrosis de", "#7f1d1d", 10.5, "end") + t(82, 110, "licuefacción:", "#7f1d1d", 10.5, "end") + t(82, 124, "penetra", "#7f1d1d", 10.5, "end") + t(82, 138, "la pared", "#7f1d1d", 10.5, "end")
    else:
        p += P("M92 190 C110 230 180 230 192 196 L180 190 C160 210 120 214 104 186 Z", "#57534e", "none", 0)
        p += t(88, 120, "ácido: escara", "#44403c", 10.5, "end") + t(88, 134, "(coagulación)", "#44403c", 10.5, "end")
    g(s, x, y, p, sc)


def linea_xy(s, x, y, puntos, xs, ys, x_label, y_label, bandas=(), marca=None, W=320, H=200, sc=1.0):
    """Gráfico de línea genérico. puntos en unidades; bandas: [(y0, y1, color, etiqueta)]."""
    X0_, Y0_ = 46, 12
    x0, x1 = xs
    y0, y1 = ys
    fx = lambda v: X0_ + (v - x0) / (x1 - x0) * W
    fy = lambda v: Y0_ + (y1 - v) / (y1 - y0) * H
    p = f'<rect x="{X0_}" y="{Y0_}" width="{W}" height="{H}" fill="#f8fafc" stroke="#cbd5e1"/>'
    for b0, b1, col, lab in bandas:
        p += f'<rect x="{X0_}" y="{fy(b1):.1f}" width="{W}" height="{fy(b0)-fy(b1):.1f}" fill="{col}" opacity="0.35"/>'
        p += t(X0_ + W - 4, fy(b1) + 12, lab, SLATE, 9.5, "end", 700, halo=False)
    pts = " ".join(f"{fx(a):.1f},{fy(b):.1f}" for a, b in puntos)
    p += f'<polyline points="{pts}" fill="none" stroke="{TEAL}" stroke-width="2.5"/>'
    if marca:
        mx, my, lab = marca
        p += C(fx(mx), fy(my), 7, ORANGE, "#7c2d12", 2) + t(fx(mx) + 10, fy(my) - 10, lab, "#9a3412", 10.5, "start")
    p += t(X0_ + W / 2, Y0_ + H + 26, x_label, MUTED, 10, halo=False) + t(4, Y0_ + 8, y_label, MUTED, 10, "start", halo=False)
    for v in (x0, (x0 + x1) / 2, x1):
        p += t(fx(v), Y0_ + H + 13, f"{v:g}", MUTED, 9.5, halo=False)
    for v in (y0, (y0 + y1) / 2, y1):
        p += t(X0_ - 4, fy(v) + 4, f"{v:g}", MUTED, 9.5, "end", halo=False)
    g(s, x, y, p, sc)


def via_aerea_niveles(s, x, y, caso=2, sc=1.0):
    """Cuatro niveles de compromiso respiratorio (lienzo 300×300): 0 extratorácico, 1 intratorácico, 2 alveolar, 3 central."""
    p = (C(150, 30, 26, "#e0e7ff" if caso != 3 else ORANGE_L, "#6366f1" if caso != 3 else ORANGE, 2) + t(150, 34, "cerebro", "#3730a3", 10)
         + P("M142 60 L142 110 L158 110 L158 60 Z", "#bae6fd" if caso != 0 else ORANGE_L, "#0369a1" if caso != 0 else ORANGE, 2)
         + P("M150 110 L150 150 M150 150 C120 170 90 190 70 220 M150 150 C180 170 210 190 230 220", "none", "#0369a1" if caso != 1 else ORANGE, 7, 'stroke-linecap="round"')
         + "".join(C(cx, cy, 11, "#fecdd3" if caso != 2 else ORANGE, "#be185d", 1.5) for cx, cy in [(62, 232), (78, 246), (222, 232), (238, 246), (70, 260), (230, 260)]))
    labs = [("Extratorácica: estridor", 184, 86), ("Intratorácica: sibilancias", 196, 176), ("Alveolointersticial: crepitantes, quejido", 150, 290),
            ("Central: respiración irregular", 184, 36)]
    for k, (tx, lx, ly) in enumerate(labs):
        p += t(lx, ly, tx, ORANGE if k == caso else SLATE, 10.5, "start" if k != 2 else "middle", 800 if k == caso else 600)
    g(s, x, y, p, sc)


def pieza_t(s, x, y, sc=1.0):
    """Reanimador con pieza en T (lienzo 330×170)."""
    p = (f'<rect x="10" y="30" width="110" height="90" rx="10" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
         + C(45, 70, 22, "#ffffff", "#475569", 2) + P("M45 70 L58 56", "none", RED, 2.5) + t(45, 108, "PIP 20-25", INK, 10)
         + C(95, 70, 16, "#ffffff", "#475569", 2) + P("M95 70 L103 62", "none", "#1d4ed8", 2.5) + t(95, 108, "PEEP 5-6", INK, 10)
         + P("M120 76 C170 76 190 90 220 90", "none", "#94a3b8", 8) + P("M220 70 L220 110 M220 90 L262 90", "none", "#475569", 10, 'stroke-linecap="round"')
         + C(222, 60, 7, "#ffffff", "#0f766e", 2) + t(236, 52, "se tapa para dar", TEAL_D, 10, "start") + t(236, 64, "cada insuflación", TEAL_D, 10, "start")
         + E(284, 90, 22, 20, "#fde68a", "#ca8a04", 2) + t(284, 130, "mascarilla", MUTED, 10, halo=False)
         + t(65, 150, "presiones fijas y PEEP: menos daño pulmonar", "#0f766e", 10.5, "start"))
    g(s, x, y, p, sc)
