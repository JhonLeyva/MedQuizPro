"""Ayudantes del bloque ENAM 2026 (266 flujogramas con imagen, 20 diseños, engine7.build7)."""
from c4 import Q, L, T
from engine7 import imagen

F26 = []
NELSON = "Nelson Tratado de Pediatría 22.ª ed. (2024)"
ATLS = "ATLS 11.ª ed. (2025)"
HARRISON = "Harrison Principios de Medicina Interna 22.ª ed. (2025)"
WILLIAMS = "Williams Obstetricia 26.ª ed. (2022)"
SCHWARTZ = "Schwartz Principios de Cirugía 11.ª ed."
SABISTON = "Sabiston Tratado de Cirugía 21.ª ed."
MINSA = "MINSA Perú"
WIKI = "Imagen: Wikimedia Commons (licencia indicada en la imagen)."


def D(ilu, W, H):
    """Imagen dibujada: ilu(s, x, y) dentro de un recuadro W×H."""
    return {"ilu": ilu, "W": W, "H": H}


def P(archivo, W, H, marcas=(), credito="", fondo="#000000"):
    """Foto real (flujo/img/<archivo>) con marcas en fracciones del recuadro."""
    return {"foto": archivo, "W": W, "H": H, "marcas": list(marcas), "credito": credito, "fondo": fondo}


def ILU(im):
    """Convierte una imagen D/P en la función que piden los diseños 9-12 (engine5)."""
    return lambda s, x, y: imagen(s, x, y, im)


def B(titulo, img, notas, pie=None, ans=-1, rotulo="Así se ve en este caso"):
    """Franja «imagen del caso» para los 8 diseños antiguos."""
    return {"titulo": titulo, "img": img, "notas": notas, "pie": pie, "ans": ans, "rotulo": rotulo}


def S(tipo, id_, archivo, titulo, barra, esp, tema, caso, perlas, fuente, d=None, arbol=None, banda=None, tabla=None):
    f = dict(tipo=tipo, id=id_, archivo=archivo, titulo=titulo, barra=barra, esp=esp,
             tema={"title": tema[0], "lines": tema[1]}, caso={"title": caso[0], "lines": caso[1]},
             perlas=perlas, fuente=fuente, banda=banda, tabla=T(*tabla) if tabla else None)
    if tipo == "arbol":
        f["arbol"] = {"kind": "topic", "title": "", "children": [arbol]}
    else:
        f["d"] = d
    F26.append(f)
    return f
