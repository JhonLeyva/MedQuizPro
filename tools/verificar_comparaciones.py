#!/usr/bin/env python3
"""Valida guias/comparaciones.json contra guias/indice.json: cada celda debe apuntar a un fragmento REAL y su `cita_literal` debe aparecer,
tal cual, en ese fragmento. Una discrepancia sin las dos citas no es válida. Sale con código 1 si algo falla.
Uso: python3 tools/verificar_comparaciones.py [--comparaciones guias/comparaciones.json] [--indice guias/indice.json]"""
import argparse, json, re, sys

TIPOS = {"discrepancia", "equivalente", "poblacion", "actualizacion", "recursos"}
norm = lambda t: re.sub(r"\s+", " ", t).strip().lower()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--comparaciones", default="guias/comparaciones.json"); ap.add_argument("--indice", default="guias/indice.json")
    a = ap.parse_args()
    comps = json.load(open(a.comparaciones, encoding="utf-8")); ix = json.load(open(a.indice, encoding="utf-8"))
    frag = {f["id"]: f for f in ix["fragmentos"]}; docs = {d["id"]: d for d in ix["docs"]}; mal = 0
    def celda(c, donde, tipo_doc):
        nonlocal mal
        if c is None: return
        if not c.get("texto"):
            return
        f = frag.get(c.get("frag", ""))
        if not f: print(f"✗ {donde}: el fragmento '{c.get('frag')}' no existe"); mal += 1; return
        if docs[f["doc"]]["tipo"] != tipo_doc: print(f"✗ {donde}: el fragmento es de una guía {docs[f['doc']]['tipo']}, no {tipo_doc}"); mal += 1
        q = c.get("cita_literal", "")
        if len(q) < 15 or norm(q) not in norm(f["texto"]): print(f"✗ {donde}: la cita_literal no aparece en el fragmento {f['id']}"); mal += 1
    for c in comps:
        for lado in ("nacional", "internacional"):
            s = c.get(lado)
            if s:
                f = frag.get(s.get("frag", ""))
                if not f: print(f"✗ {c.get('id')}.{lado}: fragmento inexistente"); mal += 1
                elif docs[f["doc"]]["tipo"] != lado: print(f"✗ {c.get('id')}.{lado}: tipo de guía incorrecto"); mal += 1
        for i, fila in enumerate(c.get("filas", [])):
            if fila.get("tipo") not in TIPOS: print(f"✗ {c.get('id')} fila {i}: tipo no válido"); mal += 1
            celda(fila.get("nacional"), f"{c.get('id')} fila {i} nacional", "nacional"); celda(fila.get("internacional"), f"{c.get('id')} fila {i} internacional", "internacional")
            if fila.get("tipo") == "discrepancia" and not (fila.get("nacional") and fila.get("internacional")):
                print(f"✗ {c.get('id')} fila {i}: una discrepancia necesita las dos fuentes"); mal += 1
    print(f"{len(comps)} comparaciones revisadas, {mal} problemas"); sys.exit(1 if mal else 0)


if __name__ == "__main__":
    main()
