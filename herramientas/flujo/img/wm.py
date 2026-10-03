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
else:
    url = f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{q}"
subprocess.run(["curl", "-sS", "-A", "MedQuizPro/1.0 (educational; contact jhonleyva)", "-o", dest, url], check=True)
if open(dest, "rb").read(15).lstrip().startswith(b"<"):
    # a veces el original directo responde con una página de error: probar por Special:FilePath
    import time
    time.sleep(4)
    url2 = "https://commons.wikimedia.org/wiki/Special:FilePath/" + q + ("?width=960" if w > 960 else "")
    subprocess.run(["curl", "-sSL", "-A", "MedQuizPro/1.0 (educational; contact jhonleyva)", "-o", dest, url2], check=True)
print(subprocess.run(["file", dest], capture_output=True, text=True).stdout.strip())
