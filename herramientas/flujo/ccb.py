"""Ayudantes del bloque CB (393 flujogramas de Ciencias Básicas, 8 diseños)."""
from c4 import Q, L, T, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
FCB = []


def _base(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente):
    return dict(tipo=tipo, id=id_, archivo=archivo, titulo=titulo, barra=barra, esp=esp,
                tema={"title": tema[0], "lines": tema[1]}, caso={"title": caso[0], "lines": caso[1]},
                perlas=perlas, fuente=fuente)


def A(id_, archivo, titulo, barra, esp, tema, caso, arbol, tabla, perlas, fuente):
    f = _base("arbol", id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente)
    f["arbol"] = {"kind": "topic", "title": "", "children": [arbol]}
    f["tabla"] = T(*tabla)
    FCB.append(f)


def V(tipo, id_, archivo, titulo, barra, esp, tema, caso, d, perlas, fuente, tabla=None):
    f = _base(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente)
    if tipo == "fases" and "curvas" not in d:
        # curva por defecto: pico en la fase marcada del caso
        import math
        n = len(d["fases"]); c = (d["ans"] + 0.5) / n
        vals = [round(0.05 + 0.9 * math.exp(-((j / 6 - c) / 0.22) ** 2), 2) for j in range(7)]
        d = dict(d, curvas=[(d.get("curva", "Relevancia en este caso"), AMBER, vals)])
    f["d"] = d
    f["tabla"] = T(*tabla) if tabla else None
    FCB.append(f)
