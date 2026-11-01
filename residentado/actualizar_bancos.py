#!/usr/bin/env python3
"""Vuelca a bancos/*.json el comentario, las fuentes y la nota de los lotes lote08_* ya integrados (emparejando por enunciado).
Uso: python3 residentado/actualizar_bancos.py [--aplicar]"""
import glob, importlib, json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(AQUI, "lotes"))
mods = [os.path.basename(f)[:-3] for f in sorted(glob.glob(AQUI + "/lotes/lote08_*.py")) if "base" not in f]
nuevo = {}
for m in mods:
    for q in importlib.import_module(m).L: nuevo[q["e"].strip()] = q
cambios = 0; vistos = set()
for f in sorted(glob.glob(RAIZ + "/bancos/*.json")):
    d = json.load(open(f, encoding="utf-8")); tocado = False
    for p in d["preguntas"]:
        if "Residentado Médico 2020" not in p.get("examen_origen", ""): continue
        q = nuevo.get(p["enunciado"].strip())
        if not q: continue
        vistos.add(p["enunciado"].strip())
        if p["comentario"] != q["c"] or p.get("fuentes") != q["f"] or p.get("nota_revision") != q.get("nota"):
            p["comentario"] = p["explicacion"] = q["c"]; p["fuentes"] = q["f"]
            if q.get("nota"): p["nota_revision"] = q["nota"]
            else: p.pop("nota_revision", None)
            tocado = True; cambios += 1
    if tocado and "--aplicar" in sys.argv: json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(cambios, "preguntas con cambios;", len(vistos), "emparejadas de", len(nuevo))
