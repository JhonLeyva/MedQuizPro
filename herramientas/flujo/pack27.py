"""Arma el paquete del ejemplo 27: 4 flujogramas nuevos con imágenes reales + los 4 del ejemplo anterior,
algoritmos.js acumulado (site + 8) y el banco de Traumatología con la errata corregida."""
import os
import re
import shutil
from demo27 import F as F27
from demo26 import F as F26

B = "out27demo/pack"
shutil.rmtree(B, ignore_errors=True)
os.makedirs(f"{B}/flujogramas")
os.makedirs(f"{B}/vistas")
os.makedirs(f"{B}/bancos")
for f in F27:
    shutil.copy(f"out27demo/flujogramas/{f['archivo']}.svg", f"{B}/flujogramas/")
    shutil.copy(f"out27demo/vistas/{f['archivo']}.png", f"{B}/vistas/")
for f in F26:
    shutil.copy(f"out26demo/flujogramas/{f['archivo']}.svg", f"{B}/flujogramas/")
shutil.copy("../site/bancos/traumatologia.json", f"{B}/bancos/")

js = open("../site/algoritmos.js", encoding="utf-8").read().rstrip()
assert js.endswith("};")
ya = set(re.findall(r'^\s*"([A-Z]+-\d+)"\s*:', js, re.M))
nuevas = ""
for f in F26 + F27:
    assert f["id"] not in ya, f["id"]
    t = f["titulo"].replace('"', "'")
    nuevas += (f'  "{f["id"]}": {{ titulo: "{t}", imagen: "flujogramas/{f["archivo"]}.svg", '
               f'alt: "Flujograma: {t}" }},\n')
cuerpo = js[:-2].rstrip()
if not cuerpo.endswith(","):
    cuerpo += ","
js = cuerpo + "\n" + nuevas + "};\n"
open(f"{B}/algoritmos.js", "w", encoding="utf-8").write(js)
n = len(re.findall(r'^\s*"([A-Z]+-\d+)"\s*:', js, re.M))
print("entradas en algoritmos.js:", n)
