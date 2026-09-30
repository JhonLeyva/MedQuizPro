"""Galería de prueba de dibujos: python3 galeria.py <salida.svg> (edita la lista CASOS)."""
import sys
from engine import SVG
import ilu7 as I

def hoja(casos, out, cols=3, cw=340, ch=360):
    s = SVG()
    for k, (tit, f) in enumerate(casos):
        x, y = 10 + (k % cols) * cw, 10 + (k // cols) * ch
        s.rect(x, y, cw - 10, ch - 10, "#ffffff", "#cbd5e1", 1, rx=6)
        s.text(x + 6, y + 14, tit, 11, 700, "#334155", "start", 0)
        f(s, x + 8, y + 22)
    H = 20 + ((len(casos) + cols - 1) // cols) * ch
    open(out, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{cols*cw+20}" height="{H}" font-family="Arial">'
                         f'<rect width="100%" height="100%" fill="#fff"/>' + "".join(s.p) + "</svg>")
