#!/usr/bin/env python3
"""Genera guardia_casos.js (el que carga la app) a partir de guardia/casos/*.json y guardia/imagenes.json.
La fuente de verdad son los JSON; guardia_casos.js es un artefacto generado (la prueba tests/guardia_test.js comprueba que está al día).
  python3 tools/guardia_empaquetar.py           # escribe guardia_casos.js
  python3 tools/guardia_empaquetar.py --check   # sale con 1 si guardia_casos.js no coincide con los JSON
"""
import glob, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def construir():
    casos = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(RAIZ, "guardia", "casos", "*.json")))]
    reg = json.load(open(os.path.join(RAIZ, "guardia", "imagenes.json"), encoding="utf-8"))["imagenes"]
    usadas = sorted({i for c in casos for i in c.get("imagenes", [])})
    imgs = {}
    for i in usadas:
        r = reg[i]
        imgs[i] = {"src": "../" + r["archivo"], "alt": r["alt_neutro"], "ancho": r["ancho"], "alto": r["alto"], "licencia": r["licencia"],
                   "revelar": {"titulo_figura": r["titulo_figura"], "articulo": r["articulo"], "autores": r["autores"], "revista": r["revista"], "anio": r["anio"], "pmid": r["pmid"], "pmcid": r["pmcid"],
                               "enlace": r["enlace"], "fuente": r["fuente_imagen"], "copyright": r["copyright"], "modalidad": r["modalidad"], "region": r["region"], "hallazgo": r["hallazgo_evaluado"], "modificaciones": r["modificaciones"], "verificada_el": r["verificada_el"]}}
    cab = ("/* MedQuizPlus · «Sobrevive a la Guardia» · 10 casos piloto (v2). ARCHIVO GENERADO: no se edita a mano.\n"
           "   Fuente: guardia/casos/*.json + guardia/imagenes.json  ·  Regenerar: python3 tools/guardia_empaquetar.py\n"
           "   Cada caso es un grafo de decisiones fijo y revisable: la evolución depende SOLO de lo que elige el alumno (no de un modelo de IA).\n"
           "   Simulación educativa: no sirve para dirigir la atención de pacientes reales. */\n")
    cuerpo = "(function () {\n  \"use strict\";\n  var CASOS = " + json.dumps(casos, ensure_ascii=False, separators=(",", ":")) + ";\n  var IMAGENES = " + json.dumps(imgs, ensure_ascii=False, separators=(",", ":")) + ";\n" \
             "  if (typeof module !== \"undefined\" && module.exports) { module.exports = CASOS; module.exports.IMAGENES = IMAGENES; }\n  if (typeof window !== \"undefined\") { window.MQP_GUARDIA = CASOS; window.MQP_GUARDIA_IMG = IMAGENES; }\n})();\n"
    return cab + cuerpo
if __name__ == "__main__":
    ruta = os.path.join(RAIZ, "guardia_casos.js"); nuevo = construir()
    if "--check" in sys.argv:
        ok = os.path.exists(ruta) and open(ruta, encoding="utf-8").read() == nuevo
        print("guardia_casos.js al día" if ok else "guardia_casos.js DESACTUALIZADO: ejecuta python3 tools/guardia_empaquetar.py"); sys.exit(0 if ok else 1)
    open(ruta, "w", encoding="utf-8").write(nuevo); print("escrito", ruta, len(nuevo), "bytes")
