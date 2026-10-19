"""Ayudantes del bloque 7 (500 flujogramas, 8 diseños)."""
from c4 import Q, L, T, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
F7 = []


def _base(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente):
    return dict(tipo=tipo, id=id_, archivo=archivo, titulo=titulo, barra=barra, esp=esp,
                tema={"title": tema[0], "lines": tema[1]}, caso={"title": caso[0], "lines": caso[1]},
                perlas=perlas, fuente=fuente)


def A(id_, archivo, titulo, barra, esp, tema, caso, arbol, tabla, perlas, fuente):
    f = _base("arbol", id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente)
    f["arbol"] = {"kind": "topic", "title": "", "children": [arbol]}
    f["tabla"] = T(*tabla)
    F7.append(f)


def V(tipo, id_, archivo, titulo, barra, esp, tema, caso, d, perlas, fuente, tabla=None):
    f = _base(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente)
    f["d"] = d
    f["tabla"] = T(*tabla) if tabla else None
    F7.append(f)
