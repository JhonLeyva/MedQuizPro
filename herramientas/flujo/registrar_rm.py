#!/usr/bin/env python3
"""Registra en algoritmos.js (y copia a flujogramas/) los flujogramas RM construidos.
Uso: python3 registrar_rm.py <carpeta_salida_build> "<Rótulo del bloque>" [--raiz /ruta/MedQuizPro]
<carpeta_salida_build> contiene order.json y flujogramas/*.svg (build_rm.py). Reemplaza las entradas existentes del mismo ID."""
import json, os, re, shutil, sys

out, bloque = sys.argv[1], sys.argv[2]
raiz = sys.argv[sys.argv.index("--raiz") + 1] if "--raiz" in sys.argv else "/home/user/MedQuizPro"
order = json.load(open(os.path.join(out, "order.json"), encoding="utf-8"))
ruta = os.path.join(raiz, "algoritmos.js")
js = open(ruta, encoding="utf-8").read()
fin = js.rstrip().rfind("};")
cuerpo, cola = js[:fin], js[fin:]
for id_, archivo, titulo, tipo in order:
    shutil.copy(os.path.join(out, "flujogramas", archivo + ".svg"), os.path.join(raiz, "flujogramas", archivo + ".svg"))
    esc = titulo.replace("\\", "\\\\").replace('"', '\\"')
    ent = (f'  "{id_}": {{\n    titulo: "{esc}",\n    imagen: "flujogramas/{archivo}.svg",\n'
           f'    alt: "Flujograma: {esc}"\n  }}')
    pat = re.compile(r'\n  "%s": \{.*?\n  \},?' % re.escape(id_), re.S)
    if pat.search(cuerpo):
        # conserva la coma final si la había
        cuerpo = pat.sub(lambda m: "\n" + ent + ("," if m.group(0).endswith(",") else ""), cuerpo, count=1)
        # si el nombre del archivo cambió, borra el SVG antiguo
    else:
        c = cuerpo.rstrip()
        if not c.endswith(",") and not c.endswith("{"):
            c += ","
        cuerpo = c + "\n" + (f"\n  /* ---------- {bloque} ---------- */\n" if bloque and f"{bloque} ----------" not in cuerpo else "") + ent + "\n"
        bloque_hecho = True
open(ruta, "w", encoding="utf-8").write(cuerpo.rstrip() + "\n" + cola)
print("registrados", len(order))
