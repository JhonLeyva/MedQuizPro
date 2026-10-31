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
    lab = json.load(open(os.path.join(RAIZ, "guardia", "laboratorio.json"), encoding="utf-8"))
    cab = ("/* MedQuizPlus · «Sobrevive a la Guardia» · 10 casos piloto (v2). ARCHIVO GENERADO: no se edita a mano.\n"
           "   Fuente: guardia/casos/*.json + guardia/imagenes.json  ·  Regenerar: python3 tools/guardia_empaquetar.py\n"
           "   Cada caso es un grafo de decisiones fijo y revisable: la evolución depende SOLO de lo que elige el alumno (no de un modelo de IA).\n"
           "   Simulación educativa: no sirve para dirigir la atención de pacientes reales. */\n")
    cuerpo = "(function () {\n  \"use strict\";\n  var CASOS = " + json.dumps(casos, ensure_ascii=False, separators=(",", ":")) + ";\n  var IMAGENES = " + json.dumps(imgs, ensure_ascii=False, separators=(",", ":")) + ";\n" \
             "  if (typeof module !== \"undefined\" && module.exports) { module.exports = CASOS; module.exports.IMAGENES = IMAGENES; }\n  if (typeof window !== \"undefined\") { window.MQP_GUARDIA = CASOS; window.MQP_GUARDIA_IMG = IMAGENES; }\n})();\n"
    return cab + cuerpo, ("/* MedQuizPlus · catálogo de laboratorio de «Sobrevive a la Guardia». ARCHIVO GENERADO desde guardia/laboratorio.json (python3 tools/guardia_empaquetar.py).\n   Intervalos EDUCATIVOS: no son de un laboratorio peruano; prevalece el del laboratorio que procesa la muestra. */\n(function () { \"use strict\"; var LAB = " + json.dumps(lab, ensure_ascii=False, separators=(",", ":")) + ";\n  if (typeof module !== \"undefined\" && module.exports) module.exports = LAB; if (typeof window !== \"undefined\") window.MQP_GUARDIA_LAB = LAB; })();\n")
def construir_consulta():
    casos = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(RAIZ, "consulta", "casos", "*.json")))]
    cab = ("/* MedQuizPlus · «Consulta Clínica Experta» · casos piloto. ARCHIVO GENERADO: no se edita a mano.\n"
           "   Fuente: consulta/casos/*.json  ·  Regenerar: python3 tools/guardia_empaquetar.py\n"
           "   Los resultados de cada prueba están predefinidos en el caso: no hay IA ni resultados aleatorios.\n"
           "   Simulación educativa: no sirve para dirigir la atención de pacientes reales. */\n")
    return cab + "(function () { \"use strict\"; var CASOS = " + json.dumps(casos, ensure_ascii=False, separators=(",", ":")) + ";\n  if (typeof module !== \"undefined\" && module.exports) module.exports = CASOS; if (typeof window !== \"undefined\") window.MQP_CONSULTA = CASOS; })();\n"
def construir_uci():
    casos = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(RAIZ, "guardia", "uci", "*.json")))]
    cab = ("/* MedQuizPlus · «Sobrevive a la Guardia» · UCI y Paciente Crítico · casos. ARCHIVO GENERADO: no se edita a mano.\n"
           "   Fuente: guardia/uci/*.json  ·  Regenerar: python3 tools/guardia_empaquetar.py\n"
           "   Misma estructura y motor que los casos de emergencias; se carga solo al abrir la modalidad. Simulación educativa. */\n")
    return cab + "(function () { \"use strict\"; var CASOS = " + json.dumps(casos, ensure_ascii=False, separators=(",", ":")) + ";\n  if (typeof module !== \"undefined\" && module.exports) module.exports = CASOS; if (typeof window !== \"undefined\") window.MQP_GUARDIA_UCI = CASOS;\n})();\n"
def construir_biblioteca():
    datos = json.load(open(os.path.join(RAIZ, "guardia", "biblioteca_lab.json"), encoding="utf-8"))
    return ("/* MedQuizPlus · biblioteca de valores de laboratorio (se carga solo al abrirla). ARCHIVO GENERADO desde guardia/biblioteca_lab.json (python3 tools/guardia_empaquetar.py).\n   Valores orientativos: cada laboratorio informa su propio intervalo según el método y el equipo. */\n"
            "(function () { \"use strict\"; var BIB = " + json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + ";\n  if (typeof module !== \"undefined\" && module.exports) module.exports = BIB; if (typeof window !== \"undefined\") window.MQP_GUARDIA_BIB = BIB; })();\n")
if __name__ == "__main__":
    ruta5 = os.path.join(RAIZ, "guardia_uci.js"); nuevo5 = construir_uci()
    ruta4 = os.path.join(RAIZ, "guardia_biblioteca.js"); nuevo4 = construir_biblioteca()
    ruta3 = os.path.join(RAIZ, "consulta_casos.js"); nuevo3 = construir_consulta()
    ruta = os.path.join(RAIZ, "guardia_casos.js"); ruta2 = os.path.join(RAIZ, "guardia_lab.js"); nuevo, nuevo2 = construir()
    if "--check" in sys.argv:
        ok = os.path.exists(ruta) and open(ruta, encoding="utf-8").read() == nuevo and os.path.exists(ruta2) and open(ruta2, encoding="utf-8").read() == nuevo2
        ok = ok and os.path.exists(ruta3) and open(ruta3, encoding="utf-8").read() == nuevo3 and os.path.exists(ruta4) and open(ruta4, encoding="utf-8").read() == nuevo4 and os.path.exists(ruta5) and open(ruta5, encoding="utf-8").read() == nuevo5
        print("guardia_casos.js, guardia_lab.js, consulta_casos.js, guardia_biblioteca.js y guardia_uci.js al día" if ok else "guardia_casos.js/guardia_lab.js/consulta_casos.js/guardia_biblioteca.js DESACTUALIZADO: ejecuta python3 tools/guardia_empaquetar.py"); sys.exit(0 if ok else 1)
    open(ruta, "w", encoding="utf-8").write(nuevo); open(ruta2, "w", encoding="utf-8").write(nuevo2); open(ruta3, "w", encoding="utf-8").write(nuevo3); open(ruta4, "w", encoding="utf-8").write(nuevo4); open(ruta5, "w", encoding="utf-8").write(nuevo5); print("escrito", ruta, len(nuevo), "bytes;", ruta2, len(nuevo2), "bytes")
