"""Baja una imagen de Wikimedia Commons (miniatura estándar 960 px o la original si es menor).
Uso: python3 wm.py "<Nombre de archivo en Commons>" <destino> [ancho_original]"""
import hashlib, sys, subprocess, urllib.parse
name = sys.argv[1].replace(" ", "_")
dest = sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
h = hashlib.md5(name.encode()).hexdigest()
q = urllib.parse.quote(name)
if w > 500:
    tw_ = 960 if w > 960 else 500
    url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{q}/{tw_}px-{q}"
elif w > 120:
    # miniatura apenas menor que la original: el servidor de miniaturas limita menos que el de originales (429)
    ext = ".png" if name.lower().endswith((".tif", ".tiff", ".gif", ".svg")) else ""
    url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{q}/{w - 4}px-{q}{ext}"
else:
    url = f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{q}"
import time
for intento in range(6):
    # el servidor responde 429 si se piden muchas seguidas: esperar y reintentar la misma URL
    subprocess.run(["curl", "-sS", "-A", "MedQuizPro/1.0 (educational; contact jhonleyva)", "-o", dest, url])
    if not open(dest, "rb").read(15).lstrip().startswith(b"<"):
        break
    time.sleep(12 * (intento + 1))
print(subprocess.run(["file", dest], capture_output=True, text=True).stdout.strip())
