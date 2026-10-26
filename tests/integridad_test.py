#!/usr/bin/env python3
"""python3 tests/integridad_test.py — comprueba que el contenido académico NO cambió: bancos de preguntas (enunciados, alternativas,
claves, comentarios), algoritmos/flujogramas (algoritmos.js, flujogramas/, herramientas/flujo/) y las guías.
Compara con tests/integridad_contenido.json (línea base fijada ANTES de añadir el Tutor Feynman IA).
  python3 tests/integridad_test.py            verifica
  python3 tests/integridad_test.py --regenerar  reescribe la línea base (solo si el dueño aprobó un cambio de contenido)"""
import hashlib, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, "tests", "integridad_contenido.json")
def sha(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def arbol(rel):
    """hash agregado de todos los archivos de una carpeta (rutas ordenadas)"""
    h = hashlib.sha256(); n = 0
    for d, ds, fs in os.walk(os.path.join(RAIZ, rel)):
        ds.sort()
        for f in sorted(fs):
            p = os.path.join(d, f); h.update(os.path.relpath(p, RAIZ).encode() + b"\0" + sha(p).encode() + b"\n"); n += 1
    return {"archivos": n, "sha256": h.hexdigest()}
def calcular():
    ar = {}
    for f in sorted(os.listdir(os.path.join(RAIZ, "bancos"))): ar["bancos/" + f] = sha(os.path.join(RAIZ, "bancos", f))
    for f in ("algoritmos.js", "catalogo.js"): ar[f] = sha(os.path.join(RAIZ, f))
    ids = 0
    for f in os.listdir(os.path.join(RAIZ, "bancos")):
        ids += len(json.load(open(os.path.join(RAIZ, "bancos", f), encoding="utf-8"))["preguntas"])
    return {"archivos": ar, "carpetas": {c: arbol(c) for c in ("flujogramas", "herramientas/flujo", "guias")}, "preguntas": ids}
if "--regenerar" in sys.argv:
    json.dump(calcular(), open(BASE, "w"), indent=1, sort_keys=True); print("línea base escrita"); sys.exit(0)
esperado = json.load(open(BASE)); actual = calcular(); fallos = 0
def ok(c, m):
    global fallos
    if not c: fallos += 1; print("FALLA:", m)
ok(actual["preguntas"] == esperado["preguntas"], f"número de preguntas {actual['preguntas']} ≠ {esperado['preguntas']}")
for k, v in esperado["archivos"].items(): ok(actual["archivos"].get(k) == v, f"{k} fue modificado")
for k, v in esperado["carpetas"].items(): ok(actual["carpetas"][k] == v, f"la carpeta {k}/ cambió ({actual['carpetas'][k]['archivos']} vs {v['archivos']} archivos)")
print(f"{fallos} fallos" if fallos else f"OK: {actual['preguntas']} preguntas, {len(actual['archivos'])} archivos y {sum(c['archivos'] for c in actual['carpetas'].values())} archivos de carpetas protegidas intactos")
sys.exit(1 if fallos else 0)
