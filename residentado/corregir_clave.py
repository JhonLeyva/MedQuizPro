#!/usr/bin/env python3
"""Aplica una corrección de clave/opción/comentario a UNA pregunta RM en bancos/<archivo>.json y en
residentado/salida/*.json (que usa el motor de flujogramas), de forma consistente.

Uso: python3 residentado/corregir_clave.py RM-XXX-NNN parche.json
parche.json (todas las claves opcionales):
  {"clave": "C",                       # letra nueva de la clave
   "opciones": {"3": "Texto nuevo."},  # índice (0-4) -> texto de la opción reemplazada
   "enunciado": "...",                 # reemplaza el enunciado
   "comentario": "...",                # reemplaza comentario y explicacion (90-170 palabras)
   "nota": "Clave del libro: A; corregida a C según <guía año>.",   # se agrega a nota_revision
   "fuentes": ["...", "..."]}          # reemplaza la lista de fuentes
No cambia nada más. Imprime un resumen del cambio."""
import glob, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
id_, parche = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
L = "ABCDE"


def aplicar(q):
    if "opciones" in parche:
        for i, t in parche["opciones"].items():
            q["opciones"][int(i)] = t
    if "enunciado" in parche:
        q["enunciado"] = parche["enunciado"]
    if "enunciado" in parche:
        q["enunciado"] = parche["enunciado"]
    if "clave" in parche:
        q["clave_correcta"] = parche["clave"]
        q["correcta"] = L.index(parche["clave"])
    if "comentario" in parche:
        q["comentario"] = q["explicacion"] = parche["comentario"]
        n = len(parche["comentario"].split())
        assert 90 <= n <= 175, f"comentario de {n} palabras"
    if "nota" in parche:
        q["nota_revision"] = ((q.get("nota_revision") or "") + " " + parche["nota"]).strip()
    if "fuentes" in parche:
        q["fuentes"] = parche["fuentes"]
    assert len(q["opciones"]) == 5 and q["clave_correcta"] == L[q["correcta"]]


hechos = []
for f in glob.glob(f"{RAIZ}/bancos/*.json"):
    d = json.load(open(f, encoding="utf-8"))
    for q in d["preguntas"]:
        if q["id"] == id_:
            aplicar(q)
            json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            hechos.append(os.path.relpath(f, RAIZ))
for f in glob.glob(f"{RAIZ}/residentado/salida/*.json"):
    d = json.load(open(f, encoding="utf-8"))
    if any(q["id"] == id_ for q in d):
        for q in d:
            if q["id"] == id_:
                aplicar(q)
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        hechos.append(os.path.relpath(f, RAIZ))
assert len(hechos) == 2, f"{id_}: se esperaba 1 banco + 1 salida, hay {hechos}"
print("ok", id_, hechos)
