import os, shutil, engine7, xml.etree.ElementTree as ET
from engine7 import build7
import content_fix4 as c
shutil.rmtree('/tmp/fix',ignore_errors=True); os.makedirs('/tmp/fix/flujogramas')
for f in c.FIX:
    engine7.AVISOS.clear()
    svg=build7(f); ET.fromstring(svg); assert not engine7.AVISOS and "RESPUESTA" not in svg.upper()
    open(f"/tmp/fix/flujogramas/{f['archivo']}.svg","w").write(svg)
print("ok")
