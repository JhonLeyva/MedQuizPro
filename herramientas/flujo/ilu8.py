"""Dibujos propios para Ciencias Básicas y Salud Pública (bloque ENAM 2026).
Mismas convenciones que ilu7: coordenadas locales, lienzo indicado en cada función."""
import math
from ilu7 import (g, t, tl, num, flecha, P, E, C, ORANGE, ORANGE_L, INK, SLATE, MUTED, TEAL, TEAL_D, SKIN, SKIN_D,
                  RED, BLUE, GREEN, VIOLET)


def caja(x, y, w, h, txt, fill="#ffffff", stroke="#cbd5e1", col=INK, fs=10.5, rx=8, sw=1.5, lines=None):
    p = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    ls = lines or [txt]
    y0 = y + h / 2 - (len(ls) - 1) * fs * 0.65 + fs * 0.35
    return p + "".join(t(x + w / 2, y0 + i * fs * 1.3, l, col, fs, halo=False) for i, l in enumerate(ls))


# ════════════════════════════════════════════════════════════ MITOCONDRIA Y CIANURO (lienzo 340×210)
def mitocondria(s, x, y, sc=1.0):
    p = (E(170, 96, 150, 78, "#fed7aa", "#c2410c", 3) + E(170, 96, 132, 62, "#ffedd5", "none", 0)
         + P("M44 96 C60 50 76 140 92 96 C108 50 124 140 140 96 C156 50 172 140 188 96 C204 50 220 140 236 96 C252 50 268 140 284 96",
             "none", "#c2410c", 2.5)
         + caja(196, 18, 96, 30, "", "#fecaca", RED, lines=["citocromo", "oxidasa"], col="#7f1d1d", fs=10)
         + C(244, 62, 11, "#1e293b", "none", 0) + t(244, 66, "CN", "#ffffff", 9.5, halo=False)
         + t(170, 190, "El cianuro bloquea la respiración celular:", SLATE, 10.5) + t(170, 204, "hay O₂ en la sangre, pero la célula no lo usa", SLATE, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ MÚSCULO Y RABDOMIÓLISIS (lienzo 340×190)
def rabdo(s, x, y, sc=1.0):
    p = ("".join(E(70, 40 + k * 26, 52, 11, "#fca5a5", "#b91c1c", 1.5) for k in range(5))
         + "".join(E(230, 40 + k * 26, 52, 11, "#fecaca", "#b91c1c", 1.5, 0, 'stroke-dasharray="5 4"') for k in range(5))
         + flecha(126, 92, 172, 92, ORANGE, 2.6)
         + t(70, 182, "músculo sano", SLATE, 10.5) + t(230, 182, "fibras rotas: CK y mioglobina", RED, 10.5)
         + t(150, 12, "estatina + fibrato", ORANGE, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ MEDIASTINO DE PERFIL (lienzo 330×260)
def mediastino(s, x, y, sc=1.0):
    p = (P("M40 20 L290 20 L300 240 L30 240 Z", "#f8fafc", "#94a3b8", 1.5)
         + P("M260 20 L262 240", "none", "#94a3b8", 1) + "".join(f'<rect x="262" y="{30 + k * 34}" width="30" height="26" rx="4" fill="#e7e5e4" stroke="#78716c"/>' for k in range(6))
         + t(277, 254, "vértebras", MUTED, 9.5)
         + f'<rect x="40" y="20" width="70" height="220" fill="#e0f2fe" opacity="0.6"/>' + t(75, 252, "anterior", MUTED, 9.5)
         + E(150, 150, 50, 56, "#fecaca", "#b91c1c", 2) + t(150, 154, "corazón", "#7f1d1d", 10)
         + f'<rect x="200" y="20" width="62" height="220" fill="{ORANGE_L}" opacity="0.8"/>' + t(231, 252, "posterior", ORANGE, 9.5)
         + P("M222 20 L222 240", "none", "#d97706", 12, 'stroke-linecap="round"') + t(214, 36, "esófago", "#92400e", 9.5, "end")
         + P("M248 40 C246 100 240 160 252 240", "none", "#dc2626", 9, 'stroke-linecap="round"') + t(214, 230, "aorta descendente", RED, 9.5, "end")
         + E(248, 120, 9, 22, "none", ORANGE, 2.5) + t(160, 34, "adelante ←   → atrás", MUTED, 9.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ NERVIO LARÍNGEO RECURRENTE (lienzo 330×250)
def recurrente(s, x, y, sc=1.0):
    p = (P("M150 10 L150 240", "none", "#94a3b8", 18, 'stroke-linecap="round"') + t(150, 248, "tráquea", MUTED, 9.5)
         + E(116, 120, 28, 46, "#fda4af", "#be123c", 2) + E(184, 120, 28, 46, "#fda4af", "#be123c", 2) + t(216, 74, "tiroides", "#9f1239", 9.5, "start")
         + P("M70 10 L70 200 C70 222 100 222 106 200 C112 180 124 120 136 40", "none", "#7c3aed", 3) + t(64, 30, "vago", "#6d28d9", 10, "end")
         + P("M128 160 L136 40", "none", ORANGE, 4) + t(94, 236, "recurrente", "#6d28d9", 10)
         + C(130, 120, 14, "none", RED, 2.5) + t(208, 190, "riesgo al operar", RED, 10, "start")
         + E(150, 22, 30, 12, "#fef3c7", "#a16207", 1.5) + t(194, 26, "cuerdas vocales", "#92400e", 9.5, "start"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ LENGUA E INERVACIÓN (lienzo 300×250)
def lengua(s, x, y, sc=1.0):
    p = (P("M150 14 C222 14 250 64 242 124 C234 182 198 198 150 198 C102 198 66 182 58 124 C50 64 78 14 150 14 Z", "#fbcfe8", "#be185d", 2)
         + P("M66 70 Q150 52 234 70", "none", "#9d174d", 1.5, 'stroke-dasharray="5 4"')
         + t(150, 42, "1/3 posterior: IX", "#9d174d", 10.5)
         + P("M150 72 C110 78 66 112 76 158 C100 192 150 196 150 196 Z", ORANGE, "none", 0, 'opacity="0.45"')
         + P("M150 72 L150 196", "none", "#9d174d", 1, 'stroke-dasharray="3 3"')
         + t(112, 136, "lado lesionado", "#9a3412", 10)
         + t(150, 220, "2/3 anteriores: tacto por el lingual (V3)", ORANGE, 10.5)
         + t(150, 238, "sabor por la cuerda del tímpano (VII)", VIOLET, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ ECG CON QRS ANCHO (lienzo W×100)
def ecg_qrs_ancho(s, x, y, W=600, sc=1.0):
    p = f'<rect x="0" y="0" width="{W}" height="100" rx="8" fill="#fff1f2" stroke="#fecdd3"/>'
    p += "".join(f'<line x1="{i}" y1="0" x2="{i}" y2="100" stroke="#fecdd3" stroke-width="0.8"/>' for i in range(20, W, 20))
    pts = []
    for i in range(0, W - 10, 2):
        ph = i % 90
        v = (-30 * math.sin((ph - 30) / 22 * math.pi) if 30 <= ph < 52 else 22 * math.sin((ph - 52) / 18 * math.pi) if 52 <= ph < 70 else 0)
        pts.append(f"{i + 6},{52 + v:.1f}")
    p += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#111827" stroke-width="2"/>'
    p += f'<rect x="34" y="12" width="46" height="78" rx="4" fill="none" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="4 3"/>'
    p += t(57, 98 - 2, "QRS 140 ms", ORANGE, 10)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CÉLULA PARIETAL (lienzo 340×220)
def parietal(s, x, y, sc=1.0):
    p = (P("M60 30 L280 30 L300 190 L40 190 Z", "#e0e7ff", "#4338ca", 2) + C(170, 140, 24, "#c7d2fe", "#3730a3", 1.5)
         + t(170, 144, "núcleo", "#3730a3", 9.5) + t(170, 210, "célula parietal (cuerpo gástrico)", SLATE, 10.5)
         + C(170, 48, 16, "#fde68a", ORANGE, 2.5) + t(170, 52, "H⁺/K⁺", "#9a3412", 9)
         + flecha(170, 32, 170, 6, RED, 2.4) + t(186, 14, "H⁺ al estómago", RED, 10, "start")
         + P("M150 34 L190 62 M190 34 L150 62", "none", "#0f172a", 3) + t(96, 70, "IBP bloquea", INK, 10.5, "end")
         + "".join(C(80 + k * 36, 100, 3, "#6366f1", "none", 0) for k in range(6)))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ GLUCÓLISIS ANAEROBIA (lienzo 340×230)
def glucolisis(s, x, y, sc=1.0):
    p = (caja(120, 6, 100, 30, "Glucosa", "#fef9c3", "#ca8a04") + flecha(170, 36, 170, 70, SLATE, 2)
         + caja(120, 72, 100, 30, "Piruvato", "#fef9c3", "#ca8a04")
         + flecha(150, 102, 70, 150, ORANGE, 3) + caja(14, 152, 116, 40, "", ORANGE_L, ORANGE, lines=["Lactato", "(sin O₂)"], col="#9a3412")
         + flecha(190, 102, 270, 150, "#94a3b8", 2, "5 4") + caja(212, 152, 116, 40, "", "#f1f5f9", "#94a3b8", lines=["Mitocondria", "(con O₂)"], col=SLATE)
         + t(70, 214, "regenera NAD⁺: calambre", ORANGE, 10) + t(270, 214, "no alcanza el O₂", MUTED, 10)
         + t(176, 56, "glucólisis", MUTED, 9.5, "start"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ ALVÉOLO CON SDRA (lienzo 340×220)
def alveolo_sdra(s, x, y, sc=1.0):
    p = (C(110, 100, 74, "#e0f2fe", "#0369a1", 2) + t(110, 196, "alvéolo normal", SLATE, 10.5)
         + C(250, 100, 74, "#bae6fd", "#0369a1", 2)
         + P("M190 60 C210 40 290 40 310 60 C300 80 200 80 190 60 Z", "#f9a8d4", "#be185d", 2, 'opacity="0.95"')
         + P("M184 100 C200 82 300 82 316 100", "none", "#be185d", 5)
         + E(250, 140, 50, 22, "#fde68a", "#ca8a04", 1.5, 0, 'opacity="0.85"')
         + t(250, 72, "membrana hialina", "#9d174d", 9.5) + t(250, 144, "edema rico en proteínas", "#92400e", 9.5)
         + t(250, 196, "daño alveolar difuso", RED, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CASCADA DE LA COAGULACIÓN (lienzo 340×240)
def cascada(s, x, y, sc=1.0):
    p = (caja(16, 6, 140, 30, "", ORANGE_L, ORANGE, lines=["Contacto (vidrio)"], col="#9a3412")
         + flecha(86, 36, 86, 54, ORANGE, 2.2) + caja(36, 56, 100, 26, "XII → XIIa", ORANGE, ORANGE, col="#ffffff")
         + flecha(86, 82, 86, 98, SLATE, 2) + caja(36, 100, 100, 24, "XI → IX", "#f1f5f9", "#94a3b8")
         + flecha(86, 124, 86, 140, SLATE, 2) + caja(36, 142, 100, 24, "IX + VIII", "#f1f5f9", "#94a3b8")
         + caja(186, 56, 140, 26, "Factor tisular + VII", "#f1f5f9", "#94a3b8") + t(256, 46, "vía extrínseca", MUTED, 9.5)
         + t(86, 196 - 2, "vía intrínseca", ORANGE, 9.5)
         + flecha(136, 154, 176, 184, SLATE, 2) + flecha(256, 82, 220, 184, SLATE, 2)
         + caja(150, 186, 120, 26, "X → trombina", "#fef9c3", "#ca8a04") + flecha(210, 212, 210, 232, SLATE, 2)
         + t(210, 240 - 2, "fibrina", INK, 10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ GLP-1 (lienzo 340×220)
def glp1(s, x, y, sc=1.0):
    p = (caja(10, 86, 80, 44, "", "#ede9fe", VIOLET, lines=["GLP-1", "(fármaco)"], col="#5b21b6")
         + E(190, 108, 64, 50, "#fef3c7", "#ca8a04", 2) + t(190, 66, "islote del páncreas", "#92400e", 9.5)
         + C(166, 104, 18, "#bbf7d0", GREEN, 1.5) + t(166, 108, "β", "#166534", 11) + C(214, 112, 16, "#fecaca", RED, 1.5) + t(214, 116, "α", "#7f1d1d", 11)
         + flecha(90, 100, 146, 100, GREEN, 2.4) + flecha(90, 118, 196, 118, RED, 2.4)
         + t(150, 150, "más insulina", "#166534", 10) + t(236, 150, "menos glucagón", RED, 10)
         + flecha(214, 160, 270, 196, RED, 2.2) + E(296, 200, 34, 16, "#e7a882", "#9a3412", 1.5) + t(296, 204, "hígado", "#7c2d12", 9.5)
         + t(296, 178, "menos glucosa", RED, 9.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ P53 Y APOPTOSIS (lienzo 340×230)
def p53(s, x, y, sc=1.0):
    dna = "".join(P(f"M{14 + k * 12} 30 Q{20 + k * 12} {18 if k % 2 else 42} {26 + k * 12} 30", "none", BLUE, 2) for k in range(6))
    p = (dna + t(50, 60, "ADN dañado", BLUE, 10) + flecha(92, 30, 130, 30, SLATE, 2)
         + caja(132, 14, 76, 32, "p53", "#dcfce7", GREEN, col="#166534", fs=12)
         + flecha(170, 46, 90, 96, GREEN, 2) + flecha(170, 46, 250, 96, GREEN, 2)
         + caja(30, 98, 120, 34, "", "#f0fdf4", GREEN, lines=["Frena el ciclo", "y repara"], col="#166534")
         + caja(190, 98, 120, 34, "", "#f0fdf4", GREEN, lines=["Si no se puede:", "apoptosis"], col="#166534")
         + caja(60, 166, 220, 46, "", ORANGE_L, ORANGE, lines=["TP53 mutado: la célula dañada", "sigue dividiéndose (cáncer)"], col="#9a3412")
         + P("M140 30 L200 30", "none", RED, 0))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ E. COLI CON FIMBRIAS (lienzo 340×210)
def ecoli_fimbrias(s, x, y, sc=1.0):
    p = ("".join(f'<rect x="{10 + k * 64}" y="150" width="60" height="50" rx="6" fill="#fde2e2" stroke="#be123c" stroke-width="1.5"/>' for k in range(5))
         + t(170, 216, "urotelio (vejiga)", "#9f1239", 10)
         + E(170, 70, 70, 30, "#bbf7d0", GREEN, 2) + t(170, 74, "E. coli", "#166534", 11)
         + "".join(P(f"M{110 + k * 15} {94 + abs(k - 4) * 2} L{104 + k * 16} 148", "none", GREEN, 1.6) for k in range(9))
         + "".join(C(104 + k * 16, 148, 3, ORANGE, "none", 0) for k in range(9))
         + t(270, 128, "fimbrias tipo I", "#166534", 10, "start") + t(270, 142, "se pegan a la manosa", ORANGE, 10, "start"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ VÍAS DE ADMINISTRACIÓN (lienzo 300×230)
def vias(s, x, y, sc=1.0):
    p = (caja(10, 10, 120, 40, "", "#fee2e2", RED, lines=["Oral", "irrita, absorbe mal"], col="#7f1d1d", fs=10)
         + caja(10, 64, 120, 40, "", "#fef3c7", "#ca8a04", lines=["Intramuscular", "duele, lenta"], col="#92400e", fs=10)
         + caja(10, 118, 120, 40, "", "#f1f5f9", "#94a3b8", lines=["Inhalatoria", "no sistémica así"], col=SLATE, fs=10)
         + caja(10, 172, 120, 46, "", "#dcfce7", GREEN, lines=["Endovenosa", "100 % y controlada"], col="#166534", fs=10)
         + f'<rect x="210" y="20" width="44" height="64" rx="6" fill="#e0f2fe" stroke="#0369a1" stroke-width="2"/>'
         + P("M232 84 L232 150 C232 170 210 180 196 196", "none", "#0369a1", 3) + t(232, 56, "infusión", "#075985", 9.5)
         + flecha(196, 196, 140, 196, GREEN, 2.4))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ HISTOGRAMA ASIMÉTRICO (lienzo 340×210)
def histograma(s, x, y, sc=1.0):
    vals = [30, 52, 44, 34, 24, 16, 11, 7, 5, 3]
    p = "".join(f'<rect x="{30 + i * 28}" y="{170 - v * 2.6:.0f}" width="24" height="{v * 2.6:.0f}" fill="#bfdbfe" stroke="#1d4ed8"/>' for i, v in enumerate(vals))
    p += P("M20 170 L320 170", "none", SLATE, 1.5)
    p += P("M100 20 L100 170", "none", TEAL, 3) + t(100, 16, "mediana", TEAL, 10.5)
    p += P("M140 34 L140 170", "none", RED, 2.5, 'stroke-dasharray="5 4"') + t(150, 30, "media (arrastrada)", RED, 10.5, "start")
    p += t(240, 110, "cola: adultos mayores", MUTED, 10) + t(170, 192, "tasa de mortalidad por grupo de edad", MUTED, 10)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CELULAR CON FOTO (lienzo 260×230)
def celular(s, x, y, sc=1.0):
    p = (f'<rect x="70" y="4" width="120" height="220" rx="16" fill="#1e293b"/>' + f'<rect x="78" y="22" width="104" height="180" rx="4" fill="#f8fafc"/>'
         + f'<rect x="84" y="30" width="92" height="80" rx="4" fill="#e2e8f0"/>' + E(130, 86, 34, 14, "#ffffff", "#94a3b8", 1)
         + f'<rect x="114" y="74" width="34" height="8" rx="3" fill="#fde047"/>' + t(131, 70, "pulsera", "#a16207", 8.5, halo=False)
         + "".join(f'<rect x="86" y="{120 + k * 14}" width="{80 - k * 10}" height="6" rx="3" fill="#cbd5e1"/>' for k in range(3))
         + C(130, 186, 10, "none", "#94a3b8", 1.5)
         + C(206, 40, 22, "#ffffff", RED, 3) + P("M190 56 L222 24", "none", RED, 3)
         + t(130, 242, "sin consentimiento = violación", RED, 10)
         + t(214, 84, "nombre,", ORANGE, 9.5, "start") + t(214, 96, "historia", ORANGE, 9.5, "start"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ POBLACIÓN Y MUESTRA (lienzo 340×210)
def validez(s, x, y, sc=1.0):
    p = (C(80, 100, 66, "#e0f2fe", "#0369a1", 2) + C(80, 100, 28, "#bae6fd", "#0369a1", 2) + t(80, 104, "muestra", "#075985", 10)
         + t(80, 186, "hospital de Lima", SLATE, 10)
         + "".join(C(260, 40 + k * 64, 26, "#f1f5f9", "#94a3b8", 1.5) for k in range(3))
         + t(260, 44, "otros", SLATE, 9.5) + t(260, 108, "hospitales", SLATE, 9.5) + t(260, 172, "regiones", SLATE, 9.5)
         + "".join(flecha(148, 100, 232, 40 + k * 64, ORANGE, 2.2, "5 4") for k in range(3))
         + t(190, 206 - 2, "¿se puede generalizar?", ORANGE, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ PERÍODOS DE UNA INFECCIÓN (lienzo 380×170)
def periodos(s, x, y, sc=1.0):
    X = lambda d: 20 + d * 30
    p = (P(f"M{X(0)} 90 L{X(11)} 90", "none", SLATE, 2) + flecha(X(10.5), 90, X(11.4), 90, SLATE, 2)
         + C(X(0), 90, 6, RED, "none", 0) + t(X(0), 112, "picadura", RED, 9.5)
         + f'<rect x="{X(0)}" y="28" width="{X(4) - X(0)}" height="26" rx="6" fill="{ORANGE}" opacity="0.9"/>' + t((X(0) + X(4)) / 2, 45, "latencia", "#ffffff", 10.5, halo=False)
         + f'<rect x="{X(4)}" y="28" width="{X(9) - X(4)}" height="26" rx="6" fill="#fecaca"/>' + t((X(4) + X(9)) / 2, 45, "puede contagiar", "#7f1d1d", 10)
         + f'<rect x="{X(0)}" y="124" width="{X(5) - X(0)}" height="24" rx="6" fill="#e0e7ff"/>' + t((X(0) + X(5)) / 2, 140, "incubación", "#3730a3", 10)
         + f'<rect x="{X(5)}" y="124" width="{X(10) - X(5)}" height="24" rx="6" fill="#fef3c7"/>' + t((X(5) + X(10)) / 2, 140, "síntomas", "#92400e", 10)
         + "".join(t(X(d), 76, f"d{d}", MUTED, 9, halo=False) for d in (0, 2, 4, 6, 8, 10))
         + t(190, 14, "exposición → contagia (latencia) / síntomas (incubación)", SLATE, 10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ FASES DE UN ENSAYO CLÍNICO (lienzo 340×200)
def fases_ensayo(s, x, y, caso=3, sc=1.0):
    it = [("I", "20-80 sanos", 24), ("II", "100-300", 54), ("III", "cientos-miles", 120), ("IV", "uso real", 150)]
    p = ""
    for k, (f, n, h) in enumerate(it):
        on = k + 1 == caso
        xx = 24 + k * 78
        p += f'<rect x="{xx}" y="{170 - h}" width="60" height="{h}" rx="6" fill="{ORANGE if on else "#bfdbfe"}" stroke="{ORANGE if on else "#1d4ed8"}"/>'
        p += t(xx + 30, 164 - h, f"Fase {f}", ORANGE if on else "#1e3a8a", 10.5) + t(xx + 30, 188, n, SLATE, 9.5)
    p += P("M14 170 L330 170", "none", SLATE, 1.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CRIADEROS DE AEDES (lienzo 340×200)
def criaderos(s, x, y, sc=1.0):
    p = (P("M20 150 L80 150 L72 190 L28 190 Z", "#94a3b8", "#475569", 2) + E(50, 152, 30, 6, "#7dd3fc", "#0369a1", 1)
         + E(150, 176, 40, 16, "#475569", "#1e293b", 2) + E(150, 170, 32, 8, "#7dd3fc", "#0369a1", 1) + t(150, 150, "llanta", SLATE, 9.5)
         + f'<rect x="230" y="120" width="60" height="70" rx="8" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>' + E(260, 124, 30, 6, "#7dd3fc", "#0369a1", 1)
         + t(50, 140, "macetas", SLATE, 9.5) + t(260, 112, "tanques", SLATE, 9.5)
         + "".join(P(f"M{cx} {cy} q3 6 0 10", "none", "#334155", 2) for cx, cy in [(44, 156), (56, 158), (146, 168), (156, 170), (254, 140), (266, 150)])
         + E(170, 50, 26, 8, "#1e293b", "none", 0) + P("M152 46 L130 30 M188 46 L210 30 M160 56 L150 74 M180 56 L190 74", "none", "#1e293b", 1.6)
         + "".join(C(160 + k * 8, 50, 1.6, "#ffffff", "none", 0) for k in range(4)) + t(170, 22, "Aedes aegypti", INK, 10.5)
         + P("M16 104 L324 104", "none", ORANGE, 2, 'stroke-dasharray="6 4"') + t(170, 98, "eliminar agua estancada corta el ciclo", ORANGE, 10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CUARTO CON CONTACTOS (lienzo 320×210)
def cuarto(s, x, y, sc=1.0):
    def per(cx, col):
        return C(cx, 92, 13, SKIN, SKIN_D, 1.5) + P(f"M{cx - 16} 150 C{cx - 16} 110 {cx + 16} 110 {cx + 16} 150 Z", col, "#475569", 1.5)
    p = (f'<rect x="10" y="20" width="300" height="160" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="3"/>'
         + per(70, ORANGE) + per(150, "#bfdbfe") + per(210, "#bfdbfe") + per(270, "#bfdbfe")
         + "".join(C(100 + k * 18, 70 + (k % 2) * 10, 3, RED, "none", 0, 'opacity="0.6"') for k in range(7))
         + t(70, 170, "con TB", ORANGE, 10) + t(210, 170, "3 convivientes", SLATE, 10)
         + t(160, 204 - 2, "cuarto pequeño y cerrado: alto contagio", RED, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CERTIFICADO: CADENA DE CAUSAS (lienzo 340×220)
def certificado(s, x, y, sc=1.0):
    p = (f'<rect x="10" y="6" width="320" height="206" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
         + t(170, 26, "Causas de la muerte (certificado)", INK, 10.5)
         + caja(24, 40, 290, 34, "", "#f1f5f9", "#cbd5e1", lines=["a) Directa: hemorragia intracerebral"], col=SLATE)
         + t(170, 88, "debida a ↓", MUTED, 9.5)
         + caja(24, 96, 290, 34, "", "#f1f5f9", "#cbd5e1", lines=["b) Intermedia: convulsiones"], col=SLATE)
         + t(170, 144, "debida a ↓", MUTED, 9.5)
         + caja(24, 152, 290, 40, "", ORANGE_L, ORANGE, lines=["c) Básica: ECLAMPSIA (inició la cadena)"], col="#9a3412", sw=2.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ BOLSAS DE RESIDUOS (lienzo 340×190)
def bolsas(s, x, y, sc=1.0):
    it = [("Biocontaminados", "#dc2626", "roja"), ("Especiales", "#eab308", "amarilla"), ("Comunes", "#1f2937", "negra")]
    p = ""
    for k, (nom, col, lab) in enumerate(it):
        cx = 60 + k * 110
        on = k == 1
        p += P(f"M{cx - 34} 50 L{cx + 34} 50 L{cx + 40} 150 C{cx + 20} 162 {cx - 20} 162 {cx - 40} 150 Z", col, "#111827", 1.5)
        p += P(f"M{cx - 12} 50 L{cx - 6} 30 L{cx + 6} 30 L{cx + 12} 50", "none", "#111827", 1.5)
        p += t(cx, 176, nom, ORANGE if on else INK, 10.5) + t(cx, 104, lab, "#ffffff" if k != 1 else "#422006", 10, halo=False)
        if on:
            p += f'<rect x="{cx - 50}" y="18" width="100" height="168" rx="10" fill="none" stroke="{ORANGE}" stroke-width="2.5"/>'
    p += t(170, 12, "fármacos vencidos → especiales", ORANGE, 10)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ PUESTO DE TRABAJO ERGONÓMICO (lienzo 320×220)
def ergonomia(s, x, y, sc=1.0):
    p = (f'<rect x="150" y="120" width="150" height="10" fill="#a16207"/>' + P("M170 130 L170 200 M280 130 L280 200", "none", "#a16207", 4)
         + f'<rect x="210" y="66" width="70" height="46" rx="4" fill="#1e293b"/>' + P("M245 112 L245 120", "none", "#1e293b", 4)
         + C(110, 50, 16, SKIN, SKIN_D, 1.5) + P("M110 66 L106 130 L150 132", "none", "#2563eb", 10, 'stroke-linecap="round"')
         + P("M106 130 L150 132 L150 196", "none", "#334155", 9, 'stroke-linecap="round"') + P("M110 80 L170 116", "none", "#2563eb", 7, 'stroke-linecap="round"')
         + f'<rect x="80" y="134" width="60" height="10" fill="#64748b"/>' + P("M110 144 L110 200 M86 200 L134 200", "none", "#64748b", 4)
         + P("M126 50 L210 82", "none", GREEN, 1.5, 'stroke-dasharray="4 3"') + t(160, 52, "pantalla a la altura de los ojos", GREEN, 9.5, "start")
         + t(30, 214, "el puesto se adapta a la persona", ORANGE, 10.5, "start"))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ REDES SEPARADAS (lienzo 340×210)
def redes(s, x, y, sc=1.0):
    it = [("MINSA/SIS", 70, 60, "#bfdbfe"), ("EsSalud", 270, 60, "#bbf7d0"), ("FF. AA.", 70, 160, "#fde68a"), ("Privados", 270, 160, "#e9d5ff")]
    p = ""
    for nom, cx, cy, col in it:
        p += C(cx, cy, 40, col, "#475569", 1.5) + t(cx, cy + 4, nom, INK, 10)
        p += "".join(C(cx + 30 * math.cos(a), cy + 30 * math.sin(a), 4, "#475569", "none", 0) for a in (0.5, 2.2, 4.0))
    p += P("M110 60 L230 60", "none", "#94a3b8", 1.5, 'stroke-dasharray="3 6"') + P("M70 100 L70 120", "none", "#94a3b8", 1.5, 'stroke-dasharray="3 6"')
    p += P("M110 160 C150 120 200 100 230 70", "none", ORANGE, 2.5, 'stroke-dasharray="6 4"') + C(170, 110, 10, "#ffffff", RED, 2) + P("M164 104 L176 116 M176 104 L164 116", "none", RED, 2)
    p += t(170, 218, "cada IAFAS con su red: poca conexión", ORANGE, 10.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CARTA DE OTTAWA (lienzo 340×230)
def ottawa(s, x, y, caso=None, sc=1.0):
    it = ["Políticas públicas saludables", "Entornos que apoyan", "Acción comunitaria", "Habilidades personales", "Reorientar servicios"]
    p = C(170, 112, 36, TEAL, "none", 0) + t(170, 108, "Promoción", "#ffffff", 10, halo=False) + t(170, 122, "de la salud", "#ffffff", 10, halo=False)
    for k, nom in enumerate(it):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        cx, cy = 170 + 118 * math.cos(a), 112 + 86 * math.sin(a)
        on = caso == k
        p += P(f"M{170 + 38 * math.cos(a):.0f} {112 + 38 * math.sin(a):.0f} L{cx - 26 * math.cos(a):.0f} {cy - 18 * math.sin(a):.0f}", "none", "#94a3b8", 1.5)
        ws = nom.split(" ", 1)
        p += f'<rect x="{cx - 62:.0f}" y="{cy - 18:.0f}" width="124" height="36" rx="8" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#cbd5e1"}" stroke-width="{2 if on else 1.2}"/>'
        p += t(cx, cy - 2, ws[0], ORANGE if on else INK, 9.5) + t(cx, cy + 11, ws[1] if len(ws) > 1 else "", ORANGE if on else INK, 9.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ QUESO SUIZO (lienzo 360×200)
def queso(s, x, y, sc=1.0):
    """Modelo del queso suizo con barreras proactivas (lienzo 360×220)."""
    p = ""
    for k, nom in enumerate(["prescripción", "doble chequeo", "alerta informática"]):
        xx = 60 + k * 100
        p += f'<path d="M{xx} 50 L{xx + 30} 40 L{xx + 30} 180 L{xx} 190 Z" fill="#fde68a" stroke="#ca8a04" stroke-width="1.5"/>'
        p += "".join(E(xx + 15, cy, 6, 9, "#ffffff", "#ca8a04", 1) for cy in ([70, 140] if k != 1 else [100, 160]))
        p += t(xx + 15, 208, nom, SLATE, 9.5)
    p += flecha(10, 70, 90, 70, RED, 2.6) + P("M90 70 L150 70", "none", RED, 2.6, 'stroke-dasharray="5 4"') + C(170, 70, 10, "#ffffff", RED, 2.5)
    p += P("M164 64 L176 76 M176 64 L164 76", "none", RED, 2.5) + t(170, 32, "error detenido", GREEN, 10.5)
    p += t(180, 14, "barreras antes del error (proactivo)", ORANGE, 10.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ COMUNIDAD Y PROMOTOR (lienzo 340×200)
def comunidad(s, x, y, sc=1.0):
    p = ""
    for k, cx in enumerate((40, 110, 250, 310)):
        p += f'<rect x="{cx - 22}" y="110" width="44" height="34" fill="#fde68a" stroke="#a16207" stroke-width="1.5"/>' + P(f"M{cx - 28} 112 L{cx} 88 L{cx + 28} 112 Z", "#b45309", "#78350f", 1.5)
    p += C(180, 70, 16, SKIN, SKIN_D, 1.5) + P("M160 150 C160 100 200 100 200 150 Z", ORANGE, "#9a3412", 1.5)
    p += P("M162 64 Q180 40 198 64", "none", "#7c2d12", 5)
    p += caja(126, 156, 108, 30, "promotor/a quechua", ORANGE_L, ORANGE, col="#9a3412", fs=9.5)
    p += "".join(flecha(180, 100, cx, 104, TEAL, 1.8, "4 3") for cx in (60, 120, 240, 300))
    p += t(170, 16, "líder local que habla el idioma y conoce la cultura", SLATE, 10)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ RELOJ Y CONSULTAS (lienzo 300×190)
def reloj(s, x, y, n=4, sc=1.0):
    p = (C(70, 90, 56, "#ffffff", "#334155", 3) + "".join(P(f"M{70 + 46 * math.cos(a):.0f} {90 + 46 * math.sin(a):.0f} L{70 + 52 * math.cos(a):.0f} {90 + 52 * math.sin(a):.0f}", "none", "#334155", 2)
                                                          for a in [k * math.pi / 6 for k in range(12)])
         + P("M70 90 L70 52 M70 90 L96 90", "none", "#334155", 3) + t(70, 166, "1 hora de médico", SLATE, 10.5)
         + flecha(132, 90, 168, 90, ORANGE, 2.6))
    for k in range(n):
        p += f'<rect x="{176 + (k % 2) * 56}" y="{44 + (k // 2) * 52}" width="48" height="40" rx="6" fill="#e0f2fe" stroke="#0369a1"/>' + t(200 + (k % 2) * 56, 68 + (k // 2) * 52, "consulta", "#075985", 9)
    p += t(230, 166, f"{n} atenciones / hora", ORANGE, 10.5)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ FUENTES DE INFORMACIÓN (lienzo 340×210)
def fuentes(s, x, y, caso=1, sc=1.0):
    it = [("Primaria", "estudio original", "#e0f2fe"), ("Secundaria", "revisión sistemática", "#dcfce7"), ("Terciaria", "libro de texto, guía", "#fef3c7")]
    p = ""
    for k, (nom, ej, col) in enumerate(it):
        yy = 14 + k * 64
        on = k == caso
        p += f'<rect x="{40 + k * 30}" y="{yy}" width="{260 - k * 60}" height="50" rx="8" fill="{ORANGE_L if on else col}" stroke="{ORANGE if on else "#94a3b8"}" stroke-width="{2.5 if on else 1.2}"/>'
        p += t(170, yy + 22, nom, ORANGE if on else INK, 11) + t(170, yy + 38, ej, SLATE, 9.5)
    p += flecha(330, 30, 330, 170, MUTED, 1.8) + t(326, 196, "procesa", MUTED, 9.5, "end")
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ NIVELES DE PREVENCIÓN (lienzo 380×170)
def prevencion(s, x, y, caso=2, sc=1.0):
    it = [("Promoción", "estilos de vida", "#dcfce7"), ("Primaria", "vacunas, hierro", "#bbf7d0"), ("Secundaria", "tamizaje", "#fde68a"),
          ("Terciaria", "rehabilitar", "#fecaca")]
    p = P("M10 140 L370 140", "none", SLATE, 2) + t(20, 160, "sano", GREEN, 10, "start") + t(370, 160, "enfermo", RED, 10, "end")
    for k, (nom, ej, col) in enumerate(it):
        xx = 14 + k * 90
        on = k == caso
        p += f'<rect x="{xx}" y="30" width="84" height="96" rx="8" fill="{col}" stroke="{ORANGE if on else "#94a3b8"}" stroke-width="{3 if on else 1.2}"/>'
        p += t(xx + 42, 70, nom, ORANGE if on else INK, 10.5) + t(xx + 42, 90, ej, SLATE, 9.5)
    p += t(14 + caso * 90 + 42, 20, "hemoglobina en CRED", ORANGE, 10)
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ VIGILANCIA ACTIVA FRENTE A PASIVA (lienzo 340×200)
def vigilancia(s, x, y, sc=1.0):
    p = (caja(10, 70, 90, 50, "", "#e0f2fe", "#0369a1", lines=["Equipo de", "la red"], col="#075985")
         + "".join(caja(230, 14 + k * 62, 100, 44, "", "#f1f5f9", "#94a3b8", lines=["Establecimiento", f"{k + 1}"], col=SLATE, fs=9.5) for k in range(3))
         + "".join(flecha(102, 95, 226, 36 + k * 62, ORANGE, 2.6) for k in range(3))
         + t(160, 196 - 2, "activa: el equipo sale a buscar los casos", ORANGE, 10.5)
         + t(55, 140, "visita, revisa", ORANGE, 9.5) + t(55, 152, "registros, llama", ORANGE, 9.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ DETERMINANTES SOCIALES (lienzo 340×230)
def determinantes(s, x, y, sc=1.0):
    p = (caja(10, 10, 320, 60, "", ORANGE_L, ORANGE, lines=["ESTRUCTURALES", "posición económica · género · etnia · educación"], col="#9a3412", sw=2.5)
         + flecha(170, 70, 170, 90, SLATE, 2)
         + caja(30, 92, 280, 56, "", "#e0f2fe", "#0369a1", lines=["INTERMEDIOS", "vivienda, agua, trabajo, conductas, servicios"], col="#075985")
         + flecha(170, 148, 170, 168, SLATE, 2)
         + caja(80, 170, 180, 44, "", "#f1f5f9", "#94a3b8", lines=["Salud y equidad"], col=INK))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ CONTINUO SALUD-ENFERMEDAD (lienzo 360×150)
def continuo(s, x, y, sc=1.0):
    p = ('<defs><linearGradient id="gse" x1="0" x2="1"><stop offset="0" stop-color="#16a34a"/><stop offset="0.5" stop-color="#fde047"/>'
         '<stop offset="1" stop-color="#dc2626"/></linearGradient></defs>'
         + f'<rect x="20" y="50" width="320" height="26" rx="13" fill="url(#gse)"/>'
         + t(20, 98, "salud", GREEN, 10.5, "start") + t(340, 98, "enfermedad", RED, 10.5, "end")
         + P("M110 40 C150 10 210 10 250 40", "none", SLATE, 2) + flecha(240, 30, 252, 42, SLATE, 2)
         + P("M250 86 C210 116 150 116 110 86", "none", SLATE, 2) + flecha(120, 96, 108, 84, SLATE, 2)
         + t(180, 14, "se mueve toda la vida", SLATE, 10)
         + t(180, 138, "biológico · psicológico · social", ORANGE, 10.5))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ DOS CAMPANAS (lienzo 360×190)
def campanas(s, x, y, sc=1.0):
    def curva(mu, col):
        pts = " ".join(f"{20 + i * 3.2:.1f},{150 - 110 * math.exp(-((i - mu) / 14) ** 2):.1f}" for i in range(0, 101))
        return f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.6"/>'
    p = (curva(40, "#0369a1") + curva(58, ORANGE) + P("M20 150 L344 150", "none", SLATE, 1.5)
         + P(f"M{20 + 40 * 3.2} 40 L{20 + 40 * 3.2} 150", "none", "#0369a1", 1.5, 'stroke-dasharray="4 3"')
         + P(f"M{20 + 58 * 3.2} 40 L{20 + 58 * 3.2} 150", "none", ORANGE, 1.5, 'stroke-dasharray="4 3"')
         + t(20 + 40 * 3.2 - 6, 32, "media B", "#0369a1", 10, "end") + t(20 + 58 * 3.2 + 6, 32, "media A", ORANGE, 10, "start")
         + t(182, 172, "IMC (variable numérica, distribución normal)", SLATE, 10)
         + t(182, 186, "2 grupos independientes → t de Student", INK, 10))
    g(s, x, y, p, sc)


# ════════════════════════════════════════════════════════════ BLOQUES EN FLUJO (genérico) (lienzo W×H)
def flujo_bloques(s, x, y, items, W=340, caso=None, sc=1.0):
    """items: lista de (titulo, detalle). Bloques en vertical unidos por flechas."""
    p = ""
    h = 40
    for k, (tit, det) in enumerate(items):
        yy = 6 + k * (h + 14)
        on = k == caso
        p += f'<rect x="10" y="{yy}" width="{W - 20}" height="{h}" rx="8" fill="{ORANGE_L if on else "#ffffff"}" stroke="{ORANGE if on else "#94a3b8"}" stroke-width="{2.4 if on else 1.2}"/>'
        p += t(24, yy + 17, tit, ORANGE if on else INK, 10.5, "start") + t(24, yy + 32, det, SLATE, 9.5, "start", 600)
        if k < len(items) - 1:
            p += flecha(W / 2, yy + h, W / 2, yy + h + 13, SLATE, 1.8)
    g(s, x, y, p, sc)
