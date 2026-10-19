#!/usr/bin/env python3
"""Comprueba que CADA fragmento del índice aparece, tal cual, en la página que declara de su PDF (citas verificables).
Uso: python3 tools/verificar_indice.py [--indice guias/indice.json] [--pdfs guias/pdf]   · sale con código 1 si algo no coincide."""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from ingestar_guias import paginas_pdf, normalizar


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--indice", default="guias/indice.json"); ap.add_argument("--pdfs", default="guias/pdf")
    a = ap.parse_args()
    ix = json.load(open(a.indice, encoding="utf-8"))
    docs = {d["id"]: d for d in ix["docs"]}; cache = {}; mal = 0; n = 0
    for f in ix["fragmentos"]:
        d = docs.get(f["doc"])
        if not d:
            print("✗", f["id"], "documento desconocido"); mal += 1; continue
        if d["id"] not in cache:
            cache[d["id"]] = [normalizar(p) for p in paginas_pdf(os.path.join(a.pdfs, d["archivo"]))]
        pags = cache[d["id"]]; n += 1
        if not (1 <= f["pagina"] <= len(pags)) or normalizar(f["texto"]) not in pags[f["pagina"] - 1]:
            print("✗", f["id"], "el texto NO está en la página", f["pagina"]); mal += 1
    print(f"{n} fragmentos revisados, {mal} con problemas")
    sys.exit(1 if mal else 0)


if __name__ == "__main__":
    main()
