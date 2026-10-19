#!/usr/bin/env python3
"""Ingesta de guías clínicas oficiales → guias/indice.json (con página de origen de cada fragmento).

Uso:  python3 tools/ingestar_guias.py [--manifest guias/manifest.json] [--pdfs guias/pdf] [--salida guias/indice.json]
Requiere `pdftotext` (poppler-utils). Los PDF deben estar descritos en el manifiesto; un PDF sin ficha no se indexa.
No inventa nada: si un PDF no tiene texto extraíble (escaneado) se avisa y se omite (haría falta OCR)."""
import argparse, hashlib, json, os, re, subprocess, sys, datetime

CAMPOS = ("id", "archivo", "titulo", "institucion", "pais", "tipo", "anio", "version", "estado")
MAX = 900      # caracteres por fragmento
SOLAPE = 160   # se repite el final del fragmento anterior para no cortar una recomendación a la mitad


def normalizar(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def paginas_pdf(ruta: str):
    out = subprocess.run(["pdftotext", "-layout", ruta, "-"], capture_output=True, check=True).stdout.decode("utf-8", "replace")
    pag = out.split("\f")
    if pag and not pag[-1].strip():
        pag.pop()
    return pag


def trocear(texto: str):
    parrafos = [normalizar(p) for p in re.split(r"\n\s*\n", texto) if normalizar(p)]
    frag, actual = [], ""
    for p in parrafos:
        while len(p) > MAX:                                   # párrafo largo: se corta en un límite de oración
            corte = p.rfind(". ", 0, MAX)
            corte = corte + 1 if corte > MAX // 2 else MAX
            if actual:
                frag.append(actual); actual = ""
            frag.append(p[:corte].strip()); p = p[corte:].strip()
        if len(actual) + len(p) + 1 <= MAX:
            actual = (actual + " " + p).strip()
        else:
            if actual:
                frag.append(actual)
            actual = (actual[-SOLAPE:] + " " + p).strip() if actual and len(actual) > SOLAPE and len(actual[-SOLAPE:]) + len(p) < MAX else p
    if actual:
        frag.append(actual)
    return [f for f in frag if len(f) >= 40]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="guias/manifest.json")
    ap.add_argument("--pdfs", default="guias/pdf")
    ap.add_argument("--salida", default="guias/indice.json")
    a = ap.parse_args()
    man = json.load(open(a.manifest, encoding="utf-8"))
    if not isinstance(man, list):
        sys.exit("El manifiesto debe ser una lista de documentos.")
    docs, frags, errores = [], [], 0
    for d in man:
        falta = [c for c in CAMPOS if d.get(c) in (None, "")]
        if falta:
            print(f"✗ {d.get('id', '?')}: faltan campos {falta}"); errores += 1; continue
        if d["tipo"] not in ("nacional", "internacional") or d["estado"] not in ("vigente", "reemplazada", "retirada"):
            print(f"✗ {d['id']}: 'tipo' o 'estado' no válido"); errores += 1; continue
        ruta = os.path.join(a.pdfs, d["archivo"])
        if not os.path.isfile(ruta):
            print(f"✗ {d['id']}: no existe {ruta}"); errores += 1; continue
        pags = paginas_pdf(ruta)
        n0 = len(frags)
        for i, t in enumerate(pags, 1):
            for j, f in enumerate(trocear(t), 1):
                frags.append({"id": f"{d['id']}-p{i}-{j}", "doc": d["id"], "pagina": i, "texto": f,
                              "hash": hashlib.sha256(f.encode()).hexdigest()[:16]})
        if len(frags) == n0:
            print(f"✗ {d['id']}: el PDF no tiene texto extraíble (¿escaneado? haría falta OCR)"); errores += 1; continue
        meta = {k: d[k] for k in CAMPOS if k != "archivo"}
        for k in ("url", "reemplazada_por", "temas", "fecha_consulta"):
            if d.get(k):
                meta[k] = d[k]
        meta["paginas"] = len(pags); meta["archivo"] = d["archivo"]
        docs.append(meta)
        print(f"✓ {d['id']}: {len(pags)} páginas, {len(frags) - n0} fragmentos")
    os.makedirs(os.path.dirname(a.salida) or ".", exist_ok=True)
    json.dump({"generado": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "docs": docs, "fragmentos": frags},
              open(a.salida, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"Índice: {len(docs)} documentos, {len(frags)} fragmentos → {a.salida}")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
