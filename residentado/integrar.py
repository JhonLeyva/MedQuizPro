#!/usr/bin/env python3
"""Convierte un lote revisado (residentado/lotes/loteNN*.py) en preguntas del banco y, con --aplicar,
las agrega a bancos/<archivo>.json con IDs RM-<PREFIJO>-NNN consecutivos.

Uso: python3 residentado/integrar.py <modulo_del_lote> [--aplicar]
Salida: residentado/salida/<modulo>.json (lista de preguntas con su archivo e ID)."""
import importlib, json, os, sys, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(AQUI, "lotes"))
PREF = {"cardiologia": "CAR", "cirugia": "CIR", "ciencias_basicas": "CB", "neumologia": "NEU", "nefrologia": "NEF",
        "endocrinologia": "END", "pediatria": "PED", "hematologia": "HEM", "gastroenterologia": "GAS", "infectologia": "INF",
        "ginecologia": "GIN", "neurologia": "NRL", "oftalmo_orl": "OFT", "psiquiatria": "PSI", "reumatologia": "REU",
        "salud_publica": "SP", "traumatologia": "TRA"}


def origen(q):
    ext = " Extraordinario" if q.get("ext") else ""
    return f"Residentado Médico {q['año']}{ext} · pregunta oficial"


def main(mod, aplicar):
    L = importlib.import_module(mod).L
    sig, sal, bancos = {}, [], {}
    for q in L:
        a = q["a"]
        if a not in bancos:
            bancos[a] = json.load(open(f"{RAIZ}/bancos/{a}.json", encoding="utf-8"))
            usados = [int(m.group(1)) for p in bancos[a]["preguntas"] for m in [re.fullmatch(r"RM-%s-(\d+)" % PREF[a], p["id"])] if m]
            sig[a] = max(usados, default=0)
        sig[a] += 1
        letras = "ABCDE"
        assert len(q["o"]) == 5 and q["k"] in letras, q["tema"]
        e = {"id": f"RM-{PREF[a]}-{sig[a]:03d}", "especialidad": bancos[a]["especialidad"], "examen_origen": origen(q),
             "enunciado": q["e"], "opciones": q["o"], "correcta": letras.index(q["k"]), "clave_correcta": q["k"],
             "explicacion": q["c"], "comentario": q["c"], "tema": q["tema"], "año": q["año"], "fuentes": q["f"]}
        if q.get("cat"): e["categoria"] = q["cat"]
        if q.get("nota"): e["nota_revision"] = q["nota"]
        sal.append({"archivo": a, **e})
    os.makedirs(f"{AQUI}/salida", exist_ok=True)
    json.dump(sal, open(f"{AQUI}/salida/{mod}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(sal), "preguntas ->", f"residentado/salida/{mod}.json")
    if aplicar:
        ya = {p["id"] for b in bancos.values() for p in b["preguntas"]}
        for e in sal:
            assert e["id"] not in ya, "ya existe " + e["id"]
            bancos[e["archivo"]]["preguntas"].append({k: v for k, v in e.items() if k != "archivo"})
        for a, b in bancos.items():
            json.dump(b, open(f"{RAIZ}/bancos/{a}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print("  actualizado", a, len(b["preguntas"]))


if __name__ == "__main__":
    main(sys.argv[1], "--aplicar" in sys.argv)
