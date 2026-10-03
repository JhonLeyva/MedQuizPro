"""Busca en Wikimedia Commons con reintentos (la API corta con 429).
Uso: python3 cm.py buscar "texto" [n]      → títulos de archivos
     python3 cm.py info "File:Nombre.jpg"    → tamaño, licencia, autor, descripción"""
import json, re, subprocess, sys, time

UA = "MedQuizPro/1.0 (educational project; contact via github jhonleyva/medquizpro)"


def api(params):
    args = ["curl", "-sS", "-G", "-A", UA, "https://commons.wikimedia.org/w/api.php"]
    for k, v in params.items():
        args += ["--data-urlencode", f"{k}={v}"]
    for intento in range(6):
        r = subprocess.run(args, capture_output=True, text=True).stdout
        try:
            return json.loads(r)
        except ValueError:
            time.sleep(5 * (intento + 1))
    raise SystemExit("sin respuesta de la API")


if sys.argv[1] == "buscar":
    n = sys.argv[3] if len(sys.argv) > 3 else "15"
    d = api({"action": "query", "list": "search", "srsearch": sys.argv[2], "srnamespace": "6", "srlimit": n, "format": "json"})
    for x in d["query"]["search"]:
        if not x["title"].lower().endswith(".pdf") and not x["title"].lower().endswith(".djvu"):
            print(x["title"])
else:
    d = api({"action": "query", "titles": sys.argv[2], "prop": "imageinfo", "iiprop": "size|extmetadata", "format": "json"})
    for p in d["query"]["pages"].values():
        ii = p["imageinfo"][0]
        m = ii["extmetadata"]
        g = lambda k: re.sub(r"<[^>]+>", "", m.get(k, {}).get("value", "")).strip()
        print(p["title"], ii["width"], "x", ii["height"], "|", g("LicenseShortName"), "|", g("Artist")[:90], "|", g("ImageDescription")[:250])
