"""ECG propios (Entrega 2): trazados sintéticos en papel milimetrado real (25 mm/s, 10 mm/mV), hechos para enseñar.
Cada patrón (PATRONES) define la forma de cada derivación y el ritmo; render() dibuja las derivaciones pedidas.

Uso:  python3 ecg29.py <patron> <archivo.jpg> "II,III,aVF;I,aVL,V2" [segundos_por_celda] [tira:II]
      (filas separadas por «;», derivaciones por «,»; la tira opcional es una fila de ritmo de toda la anchura)
Desde Python: render(...) devuelve la geometría; pt() da la posición (fracción del recuadro) de un punto del trazado
para poner flechas en el flujograma."""
import json, math, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = os.path.dirname(os.path.abspath(__file__))
PXMM = 5                     # resolución de salida: 5 px por mm (se ve nítido al doble de tamaño)
CEL_H = 30                   # alto de cada fila en mm (± 1,5 mV)

# Forma normal por derivación (mV): p, q, r, s, t; el resto de parámetros es común
BASE = {
    "I": dict(p=.10, q=-.05, r=.75, s=-.10, t=.25), "II": dict(p=.15, q=-.05, r=1.15, s=-.20, t=.35),
    "III": dict(p=.06, q=-.03, r=.50, s=-.25, t=.12), "aVR": dict(p=-.12, q=0, r=.12, s=-.85, t=-.28),
    "aVL": dict(p=.05, q=-.04, r=.45, s=-.20, t=.10), "aVF": dict(p=.10, q=-.04, r=.85, s=-.20, t=.25),
    "V1": dict(p=.08, q=0, r=.20, s=-1.00, t=.08), "V2": dict(p=.08, q=0, r=.40, s=-1.40, t=.45),
    "V3": dict(p=.08, q=0, r=.80, s=-.90, t=.50), "V4": dict(p=.10, q=-.05, r=1.40, s=-.50, t=.50),
    "V5": dict(p=.10, q=-.10, r=1.40, s=-.30, t=.40), "V6": dict(p=.10, q=-.10, r=1.10, s=-.20, t=.30),
}
COMUN = dict(pr=.16, qrs=1.0, qt=.38, st=0.0, tw=1.0, u=0.0, delta=0.0, rp=0.0, j=0.0, pw=1.0, ondas=None)


def _g(t, c, w, a):
    return a * np.exp(-0.5 * ((t - c) / w) ** 2)


def _sig(x):
    return 1 / (1 + np.exp(-np.clip(x, -60, 60)))


def latido(t, d):
    """Un complejo PQRST; t en segundos desde el inicio del QRS (la P va antes). d = parámetros de la derivación."""
    w = d["qrs"]
    v = np.zeros_like(t)
    if d["p"] and d.get("con_p", True):
        v += _g(t, -d["pr"] + .05, .022 * d["pw"], d["p"])
    s_ = d["s"] * (.35 if d["st"] > .1 else 1)      # con ST elevado, la S se pierde en la elevación
    v += _g(t, .012 * w, .008 * w, d["q"]) + _g(t, .035 * w, .010 * w, d["r"]) + _g(t, .060 * w, .011 * w, s_)
    if d["delta"]:       # onda delta (WPW): empastamiento lento al inicio del QRS
        v += _g(t, .005, .022, d["delta"])
    if d["rp"]:          # R' (bloqueo de rama derecha) o QRS ancho
        v += _g(t, .100 * w, .014 * w, d["rp"])
    jt = .085 * w
    tp = d["qt"] - .09
    if d["st"]:          # desnivel del ST: meseta desde el punto J hasta la T
        v += d["st"] * _sig((t - jt + (.012 if d["st"] > 0 else 0)) / .006) * _sig((tp + .05 - t) / .03)
    if d["j"]:           # onda J / patrón tipo Brugada: elevación en domo que baja hacia la T
        v += d["j"] * _sig((t - jt + .01) / .005) * np.exp(-np.clip(t - jt, 0, None) / .07)
    v += _g(t, tp, .045 * d["tw"], d["t"])
    if d["u"]:
        v += _g(t, tp + .16, .035, d["u"])
    return v


def _params(pat, lead):
    d = dict(COMUN)
    d.update(BASE[lead])
    d.update(pat.get("todo", {}))
    for k, v in pat.get("deriv", {}).get(lead, {}).items():
        d[k] = v
    return d


def senal(pat, lead, t):
    """Voltaje (mV) de la derivación en los tiempos t (s) según el ritmo del patrón."""
    d = _params(pat, lead)
    v = np.zeros_like(t, dtype=float)
    for q in pat["qrs"]:                       # (tiempo, cambios de forma opcionales)
        tq, cambio = (q, {}) if not isinstance(q, (tuple, list)) else q
        dd = {**d, **cambio}
        dd["con_p"] = False                    # las P se dibujan aparte (pueden no ir unidas al QRS)
        m = (t > tq - .3) & (t < tq + .8)
        v[m] += latido(t[m] - tq, dd)
    for tp_ in pat.get("p", []):
        m = (t > tp_ - .15) & (t < tp_ + .25)
        v[m] += _g(t[m] - tp_, .05, .022 * d["pw"], d["p"])
    if pat.get("base"):
        v += pat["base"](t, lead)
    rng = np.random.default_rng(abs(hash(lead)) % 1000)
    return v + rng.normal(0, .006, len(t))


def ritmo_regular(fc, dur=10.0, pr=.16, inicio=.35, p=True):
    rr = 60 / fc
    qrs = list(np.arange(inicio, dur, rr))
    return dict(qrs=qrs, p=[q - pr for q in qrs] if p else [])


# ───────────────────────────────────────────────────────── patrones
def _fa(t, lead):
    k = {"V1": .09, "II": .05, "III": .05, "aVF": .05}.get(lead, .03)
    return k * (np.sin(2 * np.pi * 6.3 * t) + .6 * np.sin(2 * np.pi * 8.9 * t + 1) + .4 * np.sin(2 * np.pi * 5.1 * t + 2))


def _flutter(t, lead):
    k = {"II": -.22, "III": -.22, "aVF": -.22, "V1": .12, "aVR": .12}.get(lead, -.06)
    f = (t * 5.0) % 1.0                        # 300 por minuto: dientes de sierra
    return k * (np.where(f < .75, f / .75, (1 - f) / .25) - .5)


def _fv(t, lead):
    return .6 * np.sin(2 * np.pi * 4.7 * t) * (0.6 + .4 * np.sin(2 * np.pi * .4 * t)) + .25 * np.sin(2 * np.pi * 7.3 * t + 1)


def _tdp(t, lead):
    return .9 * np.sin(2 * np.pi * 4.2 * t) * np.sin(2 * np.pi * .22 * t + .3)


def _nada(t, lead):
    return 0 * t


def patrones():
    P = {}
    P["normal"] = dict(ritmo_regular(72), nombre="Ritmo sinusal normal")
    P["sinusal_taqui"] = dict(ritmo_regular(125), todo=dict(qt=.32), nombre="Taquicardia sinusal")
    P["bradi"] = dict(ritmo_regular(42), nombre="Bradicardia sinusal")
    # IMA con elevación del ST
    inf = {l: dict(st=.30, t=.55) for l in ("II", "III", "aVF")}
    inf.update({"III": dict(st=.38, t=.60, r=.45), "I": dict(st=-.12, t=-.10), "aVL": dict(st=-.18, t=-.15)})
    P["iam_inferior"] = dict(ritmo_regular(80), deriv=inf, nombre="IMA inferior: ST elevado en II, III y aVF")
    ant = {l: dict(st=.32, t=.65) for l in ("V1", "V2", "V3", "V4")}
    ant.update({"V1": dict(st=.22, t=.40, r=.08), "V2": dict(st=.38, t=.70, r=.15), "V3": dict(st=.40, t=.75, r=.30),
                "II": dict(st=-.05), "III": dict(st=-.12, t=-.05), "aVF": dict(st=-.08)})
    P["iam_anterior"] = dict(ritmo_regular(88), deriv=ant, nombre="IMA anterior: ST elevado de V1 a V4")
    lat = {l: dict(st=.25, t=.50) for l in ("I", "aVL", "V5", "V6")}
    lat.update({"III": dict(st=-.15, t=-.05), "aVF": dict(st=-.10)})
    P["iam_lateral"] = dict(ritmo_regular(84), deriv=lat, nombre="IMA lateral: ST elevado en I, aVL, V5 y V6")
    isq = {l: dict(st=-.15, t=-.08) for l in ("V4", "V5", "V6", "I", "II", "aVF")}
    isq["aVR"] = dict(st=.12)
    P["isquemia_sub"] = dict(ritmo_regular(96), deriv=isq, nombre="ST deprimido (isquemia subendocárdica)")
    tneg = {l: dict(t=-.35, tw=1.1) for l in ("V1", "V2", "V3", "V4")}
    P["t_invertida"] = dict(ritmo_regular(76), deriv=tneg, nombre="T invertida de V1 a V4")
    qpat = {l: dict(q=-.45, r=.25, st=.08, t=-.20) for l in ("II", "III", "aVF")}
    P["q_patologica"] = dict(ritmo_regular(70), deriv=qpat, nombre="Ondas Q patológicas (infarto antiguo)")
    # Pericarditis: ST cóncavo difuso + PR deprimido
    per = {l: dict(st=.15, t=.45) for l in ("I", "II", "aVF", "aVL", "V2", "V3", "V4", "V5", "V6")}
    per["aVR"] = dict(st=-.12)
    P["pericarditis"] = dict(ritmo_regular(98), deriv=per, base=lambda t, l: _pr_dep(t, l, P["pericarditis"]),
                             nombre="Pericarditis: ST elevado difuso y PR deprimido")
    # Potasio
    P["hiperk"] = dict(ritmo_regular(64), todo=dict(t=.0, tw=.5, p=.04, qrs=2.0), nombre="Hiperpotasemia: T picudas, QRS ancho",
                       deriv={l: dict(t=v) for l, v in dict(I=.55, II=.8, III=.4, aVR=-.6, aVL=.3, aVF=.7, V1=.5, V2=1.1,
                                                            V3=1.2, V4=1.1, V5=.9, V6=.7).items()})
    P["hipok"] = dict(ritmo_regular(78), todo=dict(st=-.06, t=.08, u=.18, qt=.40), nombre="Hipopotasemia: T aplanada y onda U")
    P["qt_largo"] = dict(ritmo_regular(60), todo=dict(qt=.56, tw=1.3), nombre="QT largo")
    P["hipoca"] = dict(ritmo_regular(70), todo=dict(qt=.54), nombre="Hipocalcemia: QT largo por ST alargado")
    P["hiperca"] = dict(ritmo_regular(70), todo=dict(qt=.30), nombre="Hipercalcemia: QT corto")
    # Arritmias
    rr = np.cumsum([.42, .71, .55, .93, .48, .62, .80, .45, .69, .58, .87, .51, .74, .46, .66, .90])
    P["fa"] = dict(qrs=[x for x in .3 + rr if x < 10], p=[], base=_fa, todo=dict(p=0), nombre="Fibrilación auricular")
    P["fa_rapida"] = dict(qrs=[x for x in .2 + np.cumsum([.38, .52, .41, .47, .36, .55, .43, .39, .50, .44, .37, .53] * 3) if x < 10],
                          p=[], base=_fa, todo=dict(p=0), nombre="Fibrilación auricular con respuesta rápida")
    P["flutter"] = dict(qrs=list(np.arange(.42, 10, .4)), p=[], base=_flutter, todo=dict(p=0), nombre="Flutter auricular 2:1")
    P["tsv"] = dict(ritmo_regular(180, p=False), todo=dict(p=0, qt=.26), nombre="Taquicardia supraventricular")
    P["tv"] = dict(ritmo_regular(170, p=False), todo=dict(p=0, qrs=2.6, qt=.32, t=-.4, rp=0),
                   deriv={l: dict(r=1.3 if l not in ("aVR", "V1") else -.2, s=-.3 if l not in ("aVR", "V1") else -1.2)
                          for l in BASE}, nombre="Taquicardia ventricular monomorfa")
    P["fv"] = dict(qrs=[], p=[], base=_fv, todo=dict(p=0), nombre="Fibrilación ventricular")
    P["torsades"] = dict(qrs=[], p=[], base=_tdp, todo=dict(p=0), nombre="Torsade de pointes")
    P["asistolia"] = dict(qrs=[], p=[], base=_nada, todo=dict(p=0), nombre="Asistolia")
    P["wpw"] = dict(ritmo_regular(75, pr=.10), todo=dict(pr=.10, delta=.45, qrs=1.3), nombre="Wolff-Parkinson-White: PR corto y onda delta")
    P["brugada"] = dict(ritmo_regular(70), deriv={"V1": dict(j=.55, t=-.30, r=.25), "V2": dict(j=.50, t=-.25, r=.35)},
                        nombre="Patrón de Brugada tipo 1 (V1-V2)")
    P["brd"] = dict(ritmo_regular(74), todo=dict(qrs=1.35),
                    deriv={"V1": dict(r=.35, s=-.45, rp=.75, t=-.15), "V2": dict(r=.40, s=-.70, rp=.60, t=-.05),
                           "I": dict(s=-.35), "V6": dict(s=-.40)}, nombre="Bloqueo de rama derecha (rSR' en V1)")
    P["bri"] = dict(ritmo_regular(72), todo=dict(qrs=1.9),
                    deriv={"V1": dict(r=.08, s=-1.6, t=.45, st=.15), "V2": dict(r=.1, s=-1.9, t=.6, st=.2),
                           "I": dict(q=0, r=1.0, s=0, rp=.6, t=-.25, st=-.1), "V6": dict(q=0, r=1.2, s=0, rp=.7, t=-.3, st=-.1),
                           "aVL": dict(q=0, r=.8, rp=.5, t=-.2, st=-.08), "V5": dict(q=0, r=1.3, s=0, rp=.6, t=-.25)},
                    nombre="Bloqueo de rama izquierda (QRS ancho)")
    P["hvi"] = dict(ritmo_regular(72), deriv={"V1": dict(s=-2.4), "V2": dict(s=-2.6), "V5": dict(r=3.0, st=-.12, t=-.25),
                                              "V6": dict(r=2.4, st=-.10, t=-.2), "I": dict(r=1.4, st=-.06, t=-.1),
                                              "aVL": dict(r=1.3, st=-.06, t=-.1)},
                    nombre="Hipertrofia ventricular izquierda (Sokolow)")
    P["tep"] = dict(ritmo_regular(118), todo=dict(qt=.33),
                    deriv={"I": dict(s=-.45), "III": dict(q=-.45, r=.40, s=-.05, t=-.25), "V1": dict(t=-.25), "V2": dict(t=-.2), "V3": dict(t=-.12)},
                    nombre="TEP: taquicardia sinusal y S1 Q3 T3")
    # Bloqueos AV
    b1 = ritmo_regular(70, pr=.32)
    P["bav1"] = dict(b1, todo=dict(pr=.32, p=.2), nombre="Bloqueo AV de primer grado (PR > 200 ms)")
    pp = list(np.arange(.25, 10, .8))          # P cada 0,8 s (75 por minuto)
    # Mobitz I: PR .16, .26, .32, luego P sin QRS
    q1, prs = [], [.16, .26, .32, None]
    for i, tpp in enumerate(pp):
        pr = prs[i % 4]
        if pr:
            q1.append(tpp + pr)
    P["mobitz1"] = dict(qrs=q1, p=pp, todo=dict(p=.24), nombre="Bloqueo AV 2.º grado Mobitz I (Wenckebach)")
    P["mobitz2"] = dict(qrs=[tpp + .18 for i, tpp in enumerate(pp) if i % 3 != 2], p=pp, todo=dict(p=.24),
                        nombre="Bloqueo AV 2.º grado Mobitz II")
    P["bav3"] = dict(qrs=list(np.arange(.9, 10, 1.6)), p=list(np.arange(.15, 10, .72)), todo=dict(qrs=1.6, t=-.2, p=.24),
                     nombre="Bloqueo AV completo (3.er grado): disociación AV")
    P["extrasistole_v"] = dict(qrs=[.35, 1.15, (1.62, dict(qrs=2.4, r=1.4, s=-.6, t=-.5, p=0)), 2.75, 3.55,
                                    (4.02, dict(qrs=2.4, r=1.4, s=-.6, t=-.5, p=0)), 5.15, 5.95, 6.75, 7.55, 8.35, 9.15],
                               p=[.19, .99, 2.59, 3.39, 4.99, 5.79, 6.59, 7.39, 8.19, 8.99], nombre="Extrasístoles ventriculares")
    P["ritmo_marcapaso"] = dict(ritmo_regular(70), nombre="Marcapasos")
    return P


def _pr_dep(t, lead, pat):
    """Segmento PR deprimido (pericarditis): pequeña meseta negativa entre la P y el QRS."""
    v = np.zeros_like(t)
    k = .08 if lead != "aVR" else -.08
    for q in pat["qrs"]:
        v -= k * _sig((t - (q - .09)) / .006) * _sig((q - .005 - t) / .006)
    return v


PATRONES = patrones()


# ───────────────────────────────────────────────────────── dibujo
def render(patron, archivo, filas, seg=2.5, tira=None, pat=None, rotulos=True, tira_seg=None):
    """filas: [[derivaciones]]; cada columna muestra el tramo siguiente del tiempo (como un ECG real de 12 derivaciones).
    Devuelve la geometría (también la guarda en <archivo>.json) para ubicar flechas con pt()."""
    pat = pat or PATRONES[patron]
    ncol = max(len(f) for f in filas)
    ancho = ncol * seg * 25
    filas_t = [(f, seg) for f in filas] + ([([tira], tira_seg or ncol * seg)] if tira else [])
    alto = CEL_H * len(filas_t)
    fig = plt.figure(figsize=(ancho / 25.4, alto / 25.4), dpi=PXMM * 25.4)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, ancho)
    ax.set_ylim(alto, 0)
    ax.axis("off")
    ax.add_patch(plt.Rectangle((0, 0), ancho, alto, color="#fff5f3", zorder=0))
    for x in np.arange(0, ancho + .01, 1):
        ax.plot([x, x], [0, alto], color="#f7c9c3" if x % 5 else "#e58f86", lw=.35 if x % 5 else .8, zorder=1)
    for y in np.arange(0, alto + .01, 1):
        ax.plot([0, ancho], [y, y], color="#f7c9c3" if y % 5 else "#e58f86", lw=.35 if y % 5 else .8, zorder=1)
    geo = dict(ancho=ancho, alto=alto, celdas=[])
    for fi, (fila, dur) in enumerate(filas_t):
        yb = fi * CEL_H + CEL_H * .55                         # línea de base
        cw = ancho / len(fila)
        for ci, lead in enumerate(fila):
            t0 = ci * dur if dur == seg else 0
            t = np.linspace(t0, t0 + dur, int(dur * 500))
            v = senal(pat, lead, t)
            x = ci * cw + (t - t0) * 25
            y = yb - v * 10
            ax.plot(x, y, color="#111111", lw=1.15, zorder=3, solid_joinstyle="round")
            if rotulos:
                ax.text(ci * cw + 1.5, fi * CEL_H + 4.2, lead, fontsize=9.5, fontweight="bold", color="#111111",
                        va="center", ha="left", zorder=4, family="DejaVu Sans")
            if ci and dur == seg:
                ax.plot([ci * cw, ci * cw], [yb - 4, yb + 4], color="#111111", lw=1.2, zorder=3)
            geo["celdas"].append(dict(lead=lead, fila=fi, x0=ci * cw, yb=yb, t0=t0, dur=dur))
    fig.savefig(os.path.join(AQUI, archivo), dpi=PXMM * 25.4, pil_kwargs=dict(quality=92))
    plt.close(fig)
    geo["qrs"] = [q if not isinstance(q, (tuple, list)) else q[0] for q in pat["qrs"]]
    geo["p"] = list(pat.get("p", []))
    json.dump(dict(geo, patron=patron), open(os.path.join(AQUI, archivo + ".json"), "w"), default=float)
    return geo


def pt(archivo, lead, t, mv=None, fila=None):
    """Fracción (fx, fy) del recuadro para el instante t (s, del trazado completo) en la derivación lead.
    mv=None: sobre el trazado; si no, a esa altura en mV."""
    geo = json.load(open(os.path.join(AQUI, archivo + ".json")))
    for c in geo["celdas"]:
        if c["lead"] == lead and c["t0"] <= t <= c["t0"] + c["dur"] and (fila is None or c["fila"] == fila):
            if mv is None:
                mv = float(senal(PATRONES[geo["patron"]], lead, np.array([t]))[0])
            return round((c["x0"] + (t - c["t0"]) * 25) / geo["ancho"], 3), round((c["yb"] - mv * 10) / geo["alto"], 3)
    raise ValueError(f"{lead} no muestra t={t}")


def qrs_en(archivo, lead, fila=None):
    """Tiempos de QRS visibles en la celda de esa derivación."""
    geo = json.load(open(os.path.join(AQUI, archivo + ".json")))
    for c in geo["celdas"]:
        if c["lead"] == lead and (fila is None or c["fila"] == fila):
            return [q for q in geo["qrs"] if c["t0"] + .1 < q < c["t0"] + c["dur"] - .3]


if __name__ == "__main__":
    patron, archivo, filas = sys.argv[1], sys.argv[2], [f.split(",") for f in sys.argv[3].split(";")]
    seg = float(sys.argv[4]) if len(sys.argv) > 4 else 2.5
    tira = sys.argv[5].split(":")[1] if len(sys.argv) > 5 else None
    g = render(patron, archivo, filas, seg, tira)
    print(archivo, f"{g['ancho']:.0f}x{g['alto']:.0f} mm", PATRONES[patron]["nombre"])
