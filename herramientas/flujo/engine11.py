"""Cuadro de clasificación: toda clasificación, escala o estadificación del tema se muestra en un cuadro.
Spec: clasif=dict(titulo="Clasificación de Goligher", cols=["Grado", "Prolapso", "Se reduce", "Conducta"],
                  filas=[["I", "No", "—", "Fibra y líquidos"], ...], caso=2 (índice de fila o lista de índices),
                  nota="texto opcional bajo el cuadro")"""
from engine import wrap, tw, TEAL, TEAL_D, TEAL_L, INK, SLATE, MUTED, LINE
from engine2 import X0, X1
from engine3 import section, case_chip
from engine5 import ORANGE, ORANGE_L


def clasificacion(s, y, c):
    y = section(s, y, c["titulo"])
    cols = c["cols"]
    filas = c["filas"]
    caso = c.get("caso")
    caso = set([caso] if isinstance(caso, int) else (caso or []))
    W = X1 - X0
    n = len(cols)
    w0 = max(c.get("ancho_primera", 130), 125 if caso else 0)
    wr = (W - w0) / (n - 1)
    ws = [w0] + [wr] * (n - 1)
    xs = [X0]
    for w in ws[:-1]:
        xs.append(xs[-1] + w)
    # encabezado
    hl = [wrap(t, ws[i] - 16, 11.5, True) for i, t in enumerate(cols)]
    hh = max(len(l) for l in hl) * 15 + 14
    s.rect(X0, y, W, hh, TEAL_D, rx=0)
    for i, ls in enumerate(hl):
        s.text(xs[i] + 10, y + 19, ls, 11.5, 800, "#ffffff", "start", ws[i] - 16, lh=15)
    y += hh
    for r, fila in enumerate(filas):
        cel = []
        for i, t in enumerate(fila):
            cel.append(wrap(str(t), ws[i] - 16, 11.5, i == 0))
        rh = max(len(l) for l in cel) * 15 + 14
        on = r in caso
        s.rect(X0, y, W, rh, ORANGE_L if on else ("#f8fafc" if r % 2 == 0 else "#ffffff"), ORANGE if on else LINE, 2 if on else 1, rx=0)
        for i, ls in enumerate(cel):
            s.text(xs[i] + 10, y + 19, ls, 11.5, 800 if i == 0 else 500, "#9a3412" if on and i == 0 else (INK if i == 0 else SLATE), "start", ws[i] - 16, lh=15)
        if on:
            case_chip(s, xs[0] + ws[0] - 54, y + rh / 2, c.get("tag", "ESTE CASO"))
        y += rh
    if c.get("nota"):
        nl = wrap(c["nota"], W, 11)
        s.text(X0, y + 16, nl, 11, 600, MUTED, "start", W, lh=15)
        y += 8 + len(nl) * 15
    return y



def cuadro(s, y, d):
    """Diseño «cuadro»: el cuerpo es el cuadro de clasificación (spec clasif) y, opcionalmente, un veredicto y tarjetas."""
    from engine9 import _fin
    if d.get("rotulo"):
        y = section(s, y + 10, d["rotulo"])
    return _fin(s, y - 6, d)


LAYOUTS11 = {"cuadro": cuadro}
