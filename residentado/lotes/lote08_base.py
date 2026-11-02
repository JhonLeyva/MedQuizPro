# -*- coding: utf-8 -*-
"""Residentado Médico 2020 · utilidades: construye cada pregunta con enunciado, opciones y clave tomados del PDF oficial
(crudo.json = texto extraído; claves.json = respuesta marcada en amarillo en el PDF) y solo se escribe tema, comentario y fuentes."""
import json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
CRUDO = json.load(open(os.path.join(AQUI, "..", "rm2020", "crudo.json"), encoding="utf-8"))
CLAVES = json.load(open(os.path.join(AQUI, "..", "rm2020", "claves.json"), encoding="utf-8"))
BANCO = {"CIRUGIA_GENERAL": "cirugia", "GINECOLOGIA_Y_OBSTETRICIA": "ginecologia", "OFTALMOLOGIA": "oftalmo_orl",
         "ANATOMIA_PATOLOGICA": "ciencias_basicas", "ANESTESIOLOGIA": "ciencias_basicas", "PSIQUIATRIA": "psiquiatria",
         "UROLOGIA": "nefrologia", "PEDIATRIA": "pediatria"}
NEL = "Nelson Tratado de Pediatría 22.ª ed. (2024)"


def _limpia(t):
    t = re.sub(r"\s+", " ", t).strip()
    return t if t.endswith((".", "?", "!", ":", "...")) else t + "."


def hacer(L, pdf, n, tema, cat, c, f, nota=None, a=None, k=None, e=None, o=None):
    q = next(x for x in CRUDO[pdf] if x["n"] == n)
    clave = k or CLAVES[pdf][str(n)][0]
    ops = o or [_limpia(q["o"][x]) for x in "ABCDE"]
    L.append(dict(a=a or BANCO[pdf], cat=cat, tema=tema, año=2020, ext=False, e=e or q["e"], o=ops, k=clave, c=c, f=f, nota=nota))
