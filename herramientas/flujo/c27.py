"""Ayudantes de la tanda de mejora (500 flujogramas ya publicados que se rehacen con imágenes reales,
tríadas/tétradas/péntadas oficiales y verificación de encaje). Mismo motor que el bloque ENAM 2026 (build7)."""
from c26 import S as _S, D, P, B, ILU, Q, L, NELSON, ATLS, HARRISON, WILLIAMS, SCHWARTZ, SABISTON, MINSA
from engine7 import _img_draw, _img_h

F27 = []


def S(*a, **k):
    """Igual que c26.S, pero registra en F27 (se reconstruye con el mismo nombre de archivo ya publicado)."""
    return _S(*a, _reg=F27, **k)


def DOS(a, b, sep=14, vertical=False):
    """Dos imágenes (con su crédito) en un mismo recuadro: lado a lado o una debajo de la otra."""
    ha, hb = _img_h(a, 0), _img_h(b, 0)
    if vertical:
        W, H = max(a["W"], b["W"]), ha + sep + hb

        def ilu(s, x, y):
            _img_draw(s, x + (W - a["W"]) / 2, y, a)
            _img_draw(s, x + (W - b["W"]) / 2, y + ha + sep, b)
    else:
        W, H = a["W"] + sep + b["W"], max(ha, hb)

        def ilu(s, x, y):
            _img_draw(s, x, y, a)
            _img_draw(s, x + a["W"] + sep, y, b)
    return {"ilu": ilu, "W": W, "H": H}


def CON_CREDITO(im, ancho=None, dx=0):
    """Para los diseños 9-12 (engine5), que solo dibujan la imagen: la dibuja con su crédito debajo."""
    return lambda s, x, y: _img_draw(s, x + dx, y, im)


def TR(items, grupos, nota=None, rotulo="Signos con nombre propio"):
    """Tríada / tétrada / péntada epónima oficial: items = [(signo, dato del caso, presente)],
    grupos = [(nombre, desde, hasta)] (índices de items, inclusive)."""
    return {"rotulo": rotulo, "items": items, "grupos": grupos, "nota": nota}
