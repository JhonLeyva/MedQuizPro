#!/usr/bin/env python3
"""Recupera de NCBI Bookshelf (StatPearls, acceso abierto) los apartados «rango de referencia» de una prueba, para construir guardia/laboratorio.json
sin inventar valores. Registra cada consulta en guardia/evidencia_log.jsonl.
  python3 tools/guardia_lab_fuentes.py buscar "potassium"          # lista capítulos candidatos
  python3 tools/guardia_lab_fuentes.py ver NBK539791 [--ancho 1500] # imprime título, fecha, autores y los pasajes con rango de referencia
"""
import argparse, json, os, re, subprocess, sys, time, html
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); LOG = os.path.join(RAIZ, "guardia", "evidencia_log.jsonl")
CACHE = os.environ.get("GUARDIA_LAB_CACHE", "/tmp/guardia_lab_cache"); os.makedirs(CACHE, exist_ok=True)
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(url, n=0):
    h = os.path.join(CACHE, re.sub(r"\W+", "_", url)[-180:])
    if os.path.exists(h): return open(h, encoding="utf-8").read()
    time.sleep(0.45)
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", "MedQuizPlus-guardia-evidence/1.0 (educational)", url], capture_output=True)
    t = r.stdout.decode("utf-8", "replace")
    if r.returncode != 0 or not t or "rate limit" in t[:300].lower():
        if n < 4: time.sleep(2 + 2 * n); return get(url, n + 1)
        raise RuntimeError("falló " + url)
    open(h, "w", encoding="utf-8").write(t); return t
def log(o): open(LOG, "a", encoding="utf-8").write(json.dumps(dict(o, fecha=time.strftime("%Y-%m-%d")), ensure_ascii=False) + "\n")
def cmd_buscar(a):
    d = json.loads(get(EU + "esearch.fcgi?db=books&retmode=json&retmax=%d&term=%s" % (a.n, __import__("urllib.parse").parse.quote(a.consulta + " AND statpearls[book]"))))
    ids = d["esearchresult"]["idlist"]; log({"consulta": "books: " + a.consulta, "ids": ids})
    if not ids: print("(sin resultados)"); return
    s = json.loads(get(EU + "esummary.fcgi?db=books&retmode=json&id=" + ",".join(ids)))["result"]
    for i in ids: x = s.get(i, {}); print(i, x.get("accessionid") or x.get("bookid"), "|", x.get("title"), "|", x.get("pubdate", ""))
def texto(nbk):
    t = get("https://www.ncbi.nlm.nih.gov/books/%s/" % nbk)
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t); t = re.sub(r"(?s)<[^>]+>", " ", t); return re.sub(r"\s+", " ", html.unescape(t))
def cmd_ver(a):
    t = texto(a.nbk); m = re.search(r"([^.]{10,120}) - StatPearls", t); print("TÍTULO:", m.group(1).strip() if m else "?")
    for k in ("Last Update", "Authors", "Author Information"):
        m = re.search(k + r":? ([^.]{3,160})", t); print(k.upper() + ":", m.group(1).strip() if m else "?")
    n = 0
    for m in re.finditer(r"(?i)(reference range|reference interval|normal range|normal value|normal level|reference value)", t):
        i = m.start(); frag = t[max(0, i - 80): i + a.ancho]
        if re.search(r"\d", frag): print("---\n…" + frag + "…"); n += 1
        if n >= a.max: break
    log({"consulta": "books ver " + a.nbk, "pasajes": n})
def cmd_capitulos(a):
    """para cada término: capítulos StatPearls candidatos (con su título real)"""
    for term in a.terminos:
        d = json.loads(get(EU + "esearch.fcgi?db=books&retmode=json&retmax=10&term=%s" % __import__("urllib.parse").parse.quote(term + " critical findings AND statpearls[book]")))
        ids = d["esearchresult"]["idlist"]; log({"consulta": "books cap: " + term, "ids": ids}); vistos = []
        if ids:
            s2 = json.loads(get(EU + "esummary.fcgi?db=books&retmode=json&id=" + ",".join(ids)))["result"]
            for i in ids:
                n = s2.get(i, {}).get("accessionid")
                if n and n not in vistos: vistos.append(n)
        print("##", term, end=": ")
        for n in vistos[:4]:
            t = texto(n); m = re.search(r"([^.|]{3,100}) - StatPearls", t); print("%s=%s" % (n, (m.group(1).strip() if m else "?")[:60]), end=" ; ")
        print()
p = argparse.ArgumentParser(); s = p.add_subparsers(dest="c", required=True)
b = s.add_parser("buscar"); b.add_argument("consulta"); b.add_argument("-n", type=int, default=6)
c_ = s.add_parser("capitulos"); c_.add_argument("terminos", nargs="+")
v = s.add_parser("ver"); v.add_argument("nbk"); v.add_argument("--ancho", type=int, default=900); v.add_argument("--max", type=int, default=4)
a = p.parse_args(); {"buscar": cmd_buscar, "ver": cmd_ver, "capitulos": cmd_capitulos}[a.c](a)
