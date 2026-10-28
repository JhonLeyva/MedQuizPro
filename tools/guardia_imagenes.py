#!/usr/bin/env python3
"""Búsqueda y registro de imágenes médicas REALES para «Sobrevive a la Guardia» (Open-i / PubMed Central, solo licencias que permiten uso comercial).

  python3 tools/guardia_imagenes.py buscar "intussusception ultrasound" [-n 12]     lista candidatos con su licencia VERIFICADA en el XML de PMC
  python3 tools/guardia_imagenes.py fijar PMC9606179 PMC9606179_cureus-0014-00000030710-i03 --id g01-eco --modalidad ecografia \
        --region abdomen --hallazgo "..." [--recorte x0,y0,x1,y1]                    descarga, comprueba y registra la imagen en guardia/imagenes.json
  python3 tools/guardia_imagenes.py verificar                                          re-comprueba que cada imagen registrada existe, su hash y su licencia

Reglas: solo CC0 / dominio público / CC BY / CC BY-SA (se rechazan NC y ND); la licencia sale del XML oficial del artículo (efetch db=pmc), no de la web
del editor; se avisa si el pie de figura menciona reproducción con permiso/adaptación (posible material de terceros). Imágenes de pacientes
identificables (rostros, tatuajes, nombres) NO deben registrarse: se revisan a ojo antes de «fijar». No se modifica el contenido diagnóstico de la imagen.
"""
import argparse, hashlib, json, os, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(RAIZ, "guardia", "img"); REG = os.path.join(RAIZ, "guardia", "imagenes.json")
UA = "MedQuizPlus-guardia-builder/1.0 (educational case library)"
OK_LIC = re.compile(r"creativecommons\.org/(licenses/(by|by-sa)/\d\.\d|publicdomain/zero/1\.0|publicdomain/mark)", re.I)
CACHE = os.environ.get("GUARDIA_IMG_CACHE", "")      # carpeta opcional para no repetir consultas a Open-i (que responde de forma intermitente)
def get(url, binario=False, intento=0):
    """Descarga con curl (Open-i cierra las conexiones de algunos clientes HTTP de Python); hasta 5 intentos con espera creciente; caché opcional."""
    import subprocess
    cf = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest()) if CACHE else ""
    if cf and os.path.exists(cf): d = open(cf, "rb").read(); return d if binario else d.decode("utf-8", "replace")
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", UA, url], capture_output=True)
    cuerpo = r.stdout; html = cuerpo[:15].lstrip().lower().startswith(b"<!doctype") and "openi" in url        # Open-i devuelve una página HTML de error cuando está saturado
    if binario and not (cuerpo[:4] == b"\x89PNG" or cuerpo[:2] == b"\xff\xd8"): html = True            # una imagen debe empezar con la firma PNG/JPEG
    if r.returncode != 0 or not cuerpo or html:
        if intento < 4: time.sleep(5 + intento * 8); return get(url, binario, intento + 1)
        raise RuntimeError("falló la descarga de %s: %s" % (url, r.stderr.decode()[:200]))
    if cf: os.makedirs(CACHE, exist_ok=True); open(cf, "wb").write(cuerpo)
    return cuerpo if binario else cuerpo.decode("utf-8", "replace")
def licencia_pmc(pmcid):
    """Licencia, copyright y advertencias leídos del XML oficial del artículo."""
    x = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=%s&retmode=xml" % pmcid.replace("PMC", ""))
    urls = re.findall(r'(?:ali:license_ref[^>]*>|license[^>]*xlink:href=")(https?://[^<"]+)', x)
    lic = next((u for u in urls if "creativecommons" in u), urls[0] if urls else "")
    texto = re.sub(r"<[^>]+>", " ", (re.findall(r"<license.*?</license>", x, re.S) or [""])[0]); texto = re.sub(r"\s+", " ", texto).strip()[:260]
    copy = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", (re.findall(r"<copyright-statement>.*?</copyright-statement>", x, re.S) or [""])[0])).strip()
    perm = bool(re.search(r"reprinted|reproduced with permission|adapted from|courtesy of|with permission", x, re.I))
    return {"url": lic, "texto": texto, "copyright": copy, "valida": bool(OK_LIC.search(lic)), "posible_terceros": perm, "xml": x}
def cmd_buscar(a):
    q = urllib.parse.quote(a.consulta); n = a.n; vistos = 0; pag = 1
    while vistos < n:
        crudo = get("https://openi.nlm.nih.gov/api/search?query=%s&it=%s&m=%d&n=%d" % (q, a.tipo, (pag - 1) * 10 + 1, 10)).strip()
        d = json.loads(crudo) if crudo.startswith("{") else {"list": []}      # sin resultados Open-i devuelve vacío
        for it in d.get("list", []):
            vistos += 1
            try: L = licencia_pmc(it["pmcid"] if it["pmcid"].startswith("PMC") else "PMC" + it["pmcid"])
            except Exception as e: L = {"url": "?", "valida": False, "posible_terceros": False}
            cap = re.sub(r"<[^>]+>", "", it["image"]["caption"]); cap = re.sub(r"\s+", " ", cap)[:230]
            if a.validas and not L["valida"]: continue
            print("%s PMC%s PMID %s | %s %s | %s | %s" % ("✔" if L["valida"] else "✘", it["pmcid"].replace("PMC", ""), it.get("pmid"), it.get("journal_title", ""), (it.get("journal_date") or {}).get("year"), L["url"].replace("https://creativecommons.org/", "cc:"), "⚠terceros" if L["posible_terceros"] else ""))
            print("    img:", os.path.basename(it["imgLarge"]).rsplit(".", 1)[0], "\n    título:", re.sub(r"<[^>]+>", "", it["title"])[:140], "\n    pie:", cap)
            if vistos >= n: break
        if not d.get("list"): break
        pag += 1
def cmd_fijar(a):
    pmcid = a.pmcid if a.pmcid.startswith("PMC") else "PMC" + a.pmcid
    d = json.loads(get("https://openi.nlm.nih.gov/api/search?query=%s&it=%s&m=1&n=30" % (urllib.parse.quote(a.consulta), a.tipo)))
    it = next((x for x in d["list"] if os.path.basename(x["imgLarge"]).startswith(a.imagen)), None)
    if not it: sys.exit("No encuentro esa imagen con la consulta dada (usa la misma de «buscar»).")
    L = licencia_pmc(pmcid)
    if not L["valida"]: sys.exit("LICENCIA NO ADMITIDA: %s" % (L["url"] or "sin licencia"))
    if L["posible_terceros"] and not a.confirmo_original: sys.exit("El artículo menciona permisos/adaptaciones: comprueba que ESTA figura es original de los autores y repite con --confirmo-original")
    datos = get("https://openi.nlm.nih.gov" + it["imgLarge"], binario=True)
    os.makedirs(IMG, exist_ok=True); ext = os.path.splitext(it["imgLarge"])[1]; dest = os.path.join(IMG, a.id + ext)
    open(dest, "wb").write(datos)
    from PIL import Image
    im = Image.open(dest); w, h = im.size
    if a.recorte: x0, y0, x1, y1 = [int(v) for v in a.recorte.split(",")]; im = im.crop((x0, y0, x1, y1)); im.save(dest)
    reg = json.load(open(REG)) if os.path.exists(REG) else {"version": 1, "imagenes": {}}
    reg["imagenes"][a.id] = {"archivo": "guardia/img/" + a.id + ext, "sha256": hashlib.sha256(open(dest, "rb").read()).hexdigest(), "ancho": im.size[0], "alto": im.size[1], "original": {"ancho": w, "alto": h},
        "titulo_figura": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", it["image"]["caption"])).strip(), "articulo": re.sub(r"<[^>]+>", "", it["title"]).strip(), "autores": it["authors"], "revista": it.get("journal_title", ""), "anio": (it.get("journal_date") or {}).get("year"),
        "pmid": it.get("pmid"), "pmcid": pmcid, "enlace": "https://pmc.ncbi.nlm.nih.gov/articles/%s/" % pmcid, "fuente_imagen": "Open-i (NLM) · PubMed Central",
        "licencia": L["url"], "copyright": L["copyright"], "verificada_el": time.strftime("%Y-%m-%d"), "modalidad": a.modalidad, "region": a.region, "hallazgo_evaluado": a.hallazgo,
        "modificaciones": ("Recorte %s px del original de 512 px de ancho." % a.recorte if a.recorte else "Ninguna (se muestra la imagen tal como la sirve Open-i, 512 px de ancho; sin ajustes de brillo ni contraste en el archivo).")}
    json.dump(reg, open(REG, "w"), indent=1, ensure_ascii=False); print("registrada:", a.id, im.size, L["url"])
def cmd_quitar(a):
    reg = json.load(open(REG)); v = reg["imagenes"].pop(a.id, None)
    if v and os.path.exists(os.path.join(RAIZ, v["archivo"])): os.remove(os.path.join(RAIZ, v["archivo"]))
    json.dump(reg, open(REG, "w"), indent=1, ensure_ascii=False); print("quitada:", a.id, bool(v))
def cmd_verificar(a):
    reg = json.load(open(REG)); mal = 0
    for k, v in reg["imagenes"].items():
        p = os.path.join(RAIZ, v["archivo"]); ok = os.path.exists(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() == v["sha256"]
        L = licencia_pmc(v["pmcid"]); ok2 = L["valida"] and L["url"] == v["licencia"]
        print(("ok " if ok and ok2 else "MAL"), k, "" if ok else "(archivo/hash)", "" if ok2 else "(licencia: %s)" % L["url"]); mal += not (ok and ok2)
    sys.exit(1 if mal else 0)
p = argparse.ArgumentParser(); s = p.add_subparsers(dest="c", required=True)
b = s.add_parser("buscar"); b.add_argument("consulta"); b.add_argument("-n", type=int, default=12); b.add_argument("--tipo", default="xg"); b.add_argument("--validas", action="store_true")
f = s.add_parser("fijar"); f.add_argument("pmcid"); f.add_argument("imagen"); f.add_argument("--consulta", required=True); f.add_argument("--id", required=True); f.add_argument("--modalidad", required=True); f.add_argument("--region", required=True)
f.add_argument("--hallazgo", required=True); f.add_argument("--recorte"); f.add_argument("--tipo", default="xg"); f.add_argument("--confirmo-original", action="store_true")
s.add_parser("verificar"); q = s.add_parser("quitar"); q.add_argument("id")
a = p.parse_args(); {"buscar": cmd_buscar, "fijar": cmd_fijar, "verificar": cmd_verificar, "quitar": cmd_quitar}[a.c](a)
