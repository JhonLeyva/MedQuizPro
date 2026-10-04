"""Figuras de PubMed Central (NCBI) con licencia libre.
  python3 pmc.py buscar "texto" [n]      → artículos open access con licencia CC BY / CC0 (PMCID, licencia, título, n.º de figuras)
  python3 pmc.py figs PMC1234567         → figuras del artículo: etiqueta, leyenda, URL de la imagen
  python3 pmc.py bajar PMC1234567 N dest → baja la figura N (1, 2…) a dest (jpg/png) y guarda dest.json con el crédito
Solo se aceptan licencias CC BY, CC BY-SA y CC0 (las NC/ND no sirven para la web). Crédito: autores · revista año · PMCID · licencia."""
import json, re, subprocess, sys, time, urllib.parse, xml.etree.ElementTree as ET

EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
UA = "MedQuizPro-docencia/1.0 (uso educativo)"


def get(url, binary=False, tries=4):
    for k in range(tries):
        r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", UA, url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout if binary else r.stdout.decode("utf-8", "replace")
        time.sleep(2 ** (k + 1))
    raise SystemExit("no se pudo bajar " + url)


def licencia(root):
    lic = root.find(".//license")
    href = ""
    if lic is not None:
        href = lic.get("{http://www.w3.org/1999/xlink}href") or ""
        if not href:
            for e in lic.iter():
                h = e.get("{http://www.w3.org/1999/xlink}href") or (e.text or "")
                if "creativecommons" in h:
                    href = h
                    break
        if not href:
            href = "".join(lic.itertext())
    m = re.search(r"creativecommons\.org/(licenses|publicdomain)/([a-z\-]+)/(\d\.\d)?", href)
    if not m:
        return "?", href[:80]
    tipo = m.group(2).upper()
    if m.group(1) == "publicdomain":
        return "CC0", href
    return f"CC {tipo} {m.group(3) or ''}".strip(), href


def libre(lic):
    return lic.startswith("CC0") or (lic.startswith("CC BY") and "NC" not in lic and "ND" not in lic)


def articulo(pmcid):
    for k in range(5):
        # NCBI limita a ~3 consultas por segundo: si responde con un error, esperar y repetir
        x = get(EU + f"efetch.fcgi?db=pmc&id={pmcid.replace('PMC', '')}")
        try:
            root = ET.fromstring(x.encode())
            break
        except ET.ParseError:
            time.sleep(2 + 3 * k)
    else:
        raise SystemExit("NCBI no devolvió XML válido para " + pmcid)
    art = root.find(".//article")
    tit = "".join(art.find(".//article-title").itertext()) if art.find(".//article-title") is not None else ""
    autores = []
    for c in art.findall(".//contrib[@contrib-type='author']"):
        sn = c.find(".//surname")
        if sn is not None:
            autores.append(sn.text)
    revista = art.findtext(".//journal-title") or art.findtext(".//journal-id") or ""
    anio = art.findtext(".//pub-date/year") or ""
    lic, href = licencia(art)
    figs = []
    for f in art.iter("fig"):
        g = f.find(".//graphic")
        if g is None:
            continue
        cap = " ".join("".join(f.find("caption").itertext()).split()) if f.find("caption") is not None else ""
        figs.append({"label": f.findtext("label") or "", "caption": cap,
                     "href": g.get("{http://www.w3.org/1999/xlink}href")})
    return {"pmcid": pmcid, "titulo": tit, "autores": autores, "revista": revista, "anio": anio,
            "licencia": lic, "lic_url": href, "figs": figs}


def credito(a):
    au = a["autores"]
    quien = (au[0] + " et al.") if len(au) > 2 else (" y ".join(au) if au else "Autores")
    return f"{quien} · {a['revista']} {a['anio']} · {a['pmcid']} (PubMed Central) · {a['licencia']}"


def buscar(q, n=12):
    term = f"({q}) AND open access[filter] AND (cc by license[filter] OR cc0 license[filter])"
    r = json.loads(get(EU + "esearch.fcgi?db=pmc&retmode=json&retmax=%d&term=%s" % (n, urllib.parse.quote(term))))
    ids = r["esearchresult"]["idlist"]
    print("resultados:", r["esearchresult"]["count"])
    for i in ids:
        try:
            a = articulo("PMC" + i)
        except Exception as e:
            print("PMC" + i, "error", e)
            continue
        print(f"PMC{i} | {a['licencia']} | {len(a['figs'])} fig | {a['revista']} {a['anio']} | {a['titulo'][:110]}")
        time.sleep(0.4)


def figs(pmcid):
    a = articulo(pmcid)
    print(a["titulo"], "|", a["licencia"], "|", credito(a))
    for k, f in enumerate(a["figs"], 1):
        print(f"  [{k}] {f['label']}: {f['caption'][:400]}")


def url_fig(pmcid, href):
    # 1.º la copia oficial de PMC en AWS (PMC Article Datasets): no pide captcha
    base = href.rsplit(".", 1)[0] if re.search(r"\.(jpe?g|png|gif|webp|tiff?)$", href, re.I) else href
    for v in range(4, 0, -1):
        r = subprocess.run(["curl", "-sS", "--max-time", "40", f"https://pmc-oa-opendata.s3.amazonaws.com/{pmcid}.{v}/{pmcid}.{v}.json"],
                           capture_output=True)
        if r.returncode or not r.stdout.startswith(b"{"):
            continue
        for m in json.loads(r.stdout).get("media_urls", []):
            nom = m.split("?")[0].rsplit("/", 1)[1]
            if nom.rsplit(".", 1)[0] == base and re.search(r"\.(jpe?g|png|gif|webp)$", nom, re.I):
                return m.split("?")[0].replace("s3://pmc-oa-opendata/", "https://pmc-oa-opendata.s3.amazonaws.com/")
    html = get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/")
    base = href.rsplit(".", 1)[0]
    m = re.findall(r'https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^"\s]*?/' + re.escape(base) + r'\.(?:jpg|jpeg|png|gif|webp)', html)
    if not m:
        raise SystemExit("no encontré la imagen " + href + " en la página")
    return m[0]


def bajar(pmcid, n, dest):
    a = articulo(pmcid)
    if not libre(a["licencia"]):
        raise SystemExit(f"licencia no libre ({a['licencia']}): no usar")
    f = a["figs"][int(n) - 1]
    u = url_fig(pmcid, f["href"])
    data = get(u, binary=True)
    if u.endswith(".webp") or data[:4] == b"RIFF":
        from PIL import Image
        import io
        Image.open(io.BytesIO(data)).convert("RGB").save(dest, quality=93)
    else:
        open(dest, "wb").write(data)
    meta = {**{k: a[k] for k in ("pmcid", "titulo", "autores", "revista", "anio", "licencia", "lic_url")},
            "fig": f, "url": u, "credito": credito(a)}
    json.dump(meta, open(dest + ".json", "w"), ensure_ascii=False, indent=1)
    print("ok", dest, len(data), "bytes ·", meta["credito"])


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "buscar":
        buscar(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 12)
    elif c == "figs":
        figs(sys.argv[2])
    elif c == "bajar":
        bajar(*sys.argv[2:5])


def cap(q, rx, n=20):
    """Como buscar, pero muestra solo las figuras cuya leyenda contiene la expresión rx."""
    term = f"({q}) AND open access[filter] AND (cc by license[filter] OR cc0 license[filter])"
    r = json.loads(get(EU + "esearch.fcgi?db=pmc&retmode=json&retmax=%d&term=%s" % (n, urllib.parse.quote(term))))
    for i in r["esearchresult"]["idlist"]:
        try:
            a = articulo("PMC" + i)
        except Exception:
            continue
        for k, f in enumerate(a["figs"], 1):
            if re.search(rx, f["caption"], re.I):
                print(f"PMC{i} [{k}] {a['licencia']} | {a['revista']} {a['anio']} | {f['caption'][:260]}")
        time.sleep(0.34)


if __name__ == "__main__" and sys.argv[1] == "cap":
    cap(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 20)
