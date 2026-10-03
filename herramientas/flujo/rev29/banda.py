"""Agrega una franja (banda=B(...)) al final de la llamada S(...) de un ID en un content29*.py.
Uso desde Python: poner(archivo, id, texto_banda) — texto_banda empieza con 'banda=B(' y es Python válido."""
import re


def poner(archivo, id_, banda):
    s = open(archivo).read()
    i = s.index(f'"{id_}"')
    i = s.rindex("S(", 0, i)
    j = s.find("\n\n# ", i)
    j = len(s.rstrip()) if j < 0 else j
    bloque = s[i:j].rstrip()
    assert bloque.endswith(")"), id_
    assert "banda=" not in bloque, id_ + " ya tiene franja"
    nuevo = bloque[:-1] + ",\n  " + banda.strip() + ")"
    s = s[:i] + nuevo + s[i + len(bloque):]
    open(archivo, "w").write(s)
