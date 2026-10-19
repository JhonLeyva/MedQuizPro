"""Ayudantes para el contenido del bloque 4 (100 flujogramas con diseños variados)."""
F4 = []
NELSON = "Nelson Tratado de Pediatría 22.ª ed. (2024)"
ATLS = "ACS – ATLS 11.ª ed. (2025)"
TEAL, ROSE, VIOLET, SKY, AMBER = "#0d9488", "#e11d48", "#8b5cf6", "#0ea5e9", "#f59e0b"


def Q(title, children, edge=None, path=False):
    return {"kind": "q", "title": title, "children": children, "edge": edge, "path": path}


def L(edge, title, lines, path=False, children=None, answer=False):
    n = {"kind": "node" if children else "leaf", "edge": edge, "title": title, "lines": lines, "path": path}
    if children:
        n["children"] = children
    if answer:
        n["answer"] = True
    return n


def T(titulo, cols, rows):
    return {"titulo": titulo, "corner": "Criterio", "cols": cols, "rows": rows}


def _base(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente):
    return dict(tipo=tipo, id=id_, archivo=archivo, titulo=titulo, barra=barra, esp=esp,
                tema={"title": tema[0], "lines": tema[1]}, caso={"title": caso[0], "lines": caso[1]},
                perlas=perlas, fuente=fuente)


def A(id_, archivo, titulo, barra, esp, tema, caso, arbol, tabla, perlas, fuente):
    """Árbol «tema general + ruta del caso» (engine2)."""
    f = _base("arbol", id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente)
    f["arbol"] = {"kind": "topic", "title": "", "children": [arbol]}
    f["tabla"] = T(*tabla)
    F4.append(f)


def V(tipo, id_, archivo, titulo, barra, esp, tema, caso, d, perlas, fuente, tabla=None):
    """Diseños nuevos (engine3): radial, fases, termometro, tarjetas."""
    f = _base(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente)
    f["d"] = d
    f["tabla"] = T(*tabla) if tabla else None
    F4.append(f)
