#!/usr/bin/env python3
"""Empaqueta los casos de la Misión SERUMS (serums/casos/*.json) y el registro de evidencia en serums_casos.js.
Uso: python3 tools/serums_empaquetar.py [--check]   (--check falla si serums_casos.js no está al día)."""
import glob, json, os, sys
R = os.path.join(os.path.dirname(__file__), "..")
def construir():
    casos = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(R, "serums", "casos", "*.json")))]
    ev = json.load(open(os.path.join(R, "serums", "evidencia.json"), encoding="utf-8"))
    cuerpo = json.dumps({"casos": casos, "evidencia": ev}, ensure_ascii=False, separators=(",", ":"))
    return "/* Generado por tools/serums_empaquetar.py. No editar a mano. */\nwindow.MQP_SERUMS=" + cuerpo + ";\n"
destino = os.path.join(R, "serums_casos.js")
t = construir()
if "--check" in sys.argv:
    ok = os.path.isfile(destino) and open(destino, encoding="utf-8").read() == t
    print("serums_casos.js al día" if ok else "serums_casos.js desactualizado: ejecuta tools/serums_empaquetar.py"); sys.exit(0 if ok else 1)
open(destino, "w", encoding="utf-8").write(t); print("serums_casos.js:", len(t) // 1024, "KB")
