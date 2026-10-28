#!/usr/bin/env python3
"""Recuperación y verificación bibliográfica para «Sobrevive a la Guardia» (PubMed vía las E-utilities oficiales de NCBI).

  python3 tools/guardia_evidencia.py buscar "tokyo guidelines acute cholangitis 2018" [-n 8] [--tipo guideline|trial|review|meta]  lista PMID, año, revista, título
  python3 tools/guardia_evidencia.py ver 29045062 [29045063 …]        título, autores, revista, año, DOI, tipos de publicación y resumen breve (para leer la recomendación)
  python3 tools/guardia_evidencia.py verificar                        comprueba CADA referencia con PMID/DOI de guardia/casos/*.json contra PubMed (existe, el año y el título coinciden)

Cada consulta queda registrada en guardia/evidencia_log.jsonl (fecha, consulta, PMID devueltos): es la traza de lo que realmente se recuperó.
No se inventa nada: «verificar» falla si una referencia no existe o no coincide. Las guías sin PMID (MINSA, OMS, NICE…) se verifican leyendo la página oficial y
se marcan en el caso con su URL y fecha de consulta; este script no las puede comprobar y lo dice.
"""
import argparse, glob, json, os, re, subprocess, sys, time, urllib.parse
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(RAIZ, "guardia", "evidencia_log.jsonl"); EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(url, intento=0):
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", "MedQuizPlus-guardia-evidence/1.0 (educational)", url], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        if intento < 3: time.sleep(2 + intento * 3); return get(url, intento + 1)
        raise RuntimeError("falló " + url)
    t = r.stdout.decode("utf-8", "replace")
    if '"error"' in t[:200] and "rate" in t.lower() and intento < 3: time.sleep(3); return get(url, intento + 1)
    return t
def resumen(pmids):
    time.sleep(0.4); d = json.loads(get(EU + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids)))
    return [d["result"][p] for p in pmids if p in d["result"]]
def anio(x): m = re.search(r"(19|20)\d\d", x.get("pubdate", "") or x.get("epubdate", "")); return m.group(0) if m else "?"
def doi(x): return next((i["value"] for i in x.get("articleids", []) if i["idtype"] == "doi"), "")
def cmd_buscar(a):
    q = a.consulta + {"guideline": " AND (guideline[pt] OR practice guideline[pt])", "trial": " AND (randomized controlled trial[pt])", "review": " AND (review[pt] OR systematic review[pt])", "meta": " AND (meta-analysis[pt])"}.get(a.tipo or "", "")
    d = json.loads(get(EU + "esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=%d&term=%s" % (a.n, urllib.parse.quote(q)))); ids = d["esearchresult"]["idlist"]
    open(LOG, "a").write(json.dumps({"fecha": time.strftime("%Y-%m-%d"), "consulta": q, "pmids": ids}, ensure_ascii=False) + "\n")
    for x in (resumen(ids) if ids else []):
        print("%-9s %s | %-22s | %s" % (x["uid"], anio(x), (x.get("source") or "")[:22], re.sub(r"\s+", " ", x.get("title", ""))[:150]))
    print("(%s resultados totales)" % d["esearchresult"].get("count"))
def cmd_ver(a):
    for p in a.pmids:
        x = resumen([p])[0]; t = get(EU + "efetch.fcgi?db=pubmed&retmode=xml&id=" + p); ab = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", " ".join(re.findall(r"<AbstractText[^>]*>(.*?)</AbstractText>", t, re.S))))[:a.largo]
        print("PMID %s | %s | %s | DOI %s | %s\n  %s\n  AUTORES: %s\n  RESUMEN: %s\n" % (p, anio(x), x.get("source"), doi(x), ", ".join(x.get("pubtype", [])), re.sub(r"\s+", " ", x["title"]), ", ".join(a_["name"] for a_ in x.get("authors", [])[:4]) + (" et al." if len(x.get("authors", [])) > 4 else ""), ab))
def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
def cmd_verificar(a):
    mal = 0; n = 0; ids = {}
    for f in sorted(glob.glob(os.path.join(RAIZ, "guardia", "casos", "*.json"))):
        c = json.load(open(f, encoding="utf-8"))
        for r in c.get("referencias", []):
            n += 1
            if r.get("pmid"): ids.setdefault(str(r["pmid"]), []).append((c["id"], r))
            elif not (r.get("url") and r.get("fecha_consulta")): print("MAL  %s: referencia sin PMID y sin url+fecha_consulta: %s" % (c["id"], r.get("titulo"))); mal += 1
    lista = list(ids)
    for i in range(0, len(lista), 20):
        for x in resumen(lista[i:i + 20]):
            for cid, r in ids.pop(x["uid"]):
                ok_anio = str(r.get("anio")) == anio(x) or abs(int(r.get("anio", 0)) - int(anio(x))) <= 1      # ±1: fecha electrónica vs. del volumen
                a_, b_ = set(norm(r["titulo"]).split()), set(norm(x["title"]).split()); ok_tit = len(a_ & b_) >= max(3, int(0.5 * min(len(a_), len(b_))))      # PubMed a veces concatena el título en varios idiomas
                ok_doi = (not r.get("doi")) or r["doi"].lower() == doi(x).lower()
                if not (ok_anio and ok_tit and ok_doi): print("MAL  %s PMID %s: año %s/%s título %s doi %s → PubMed: «%s» (%s)" % (cid, x["uid"], r.get("anio"), anio(x), ok_tit, ok_doi, x["title"][:90], anio(x))); mal += 1
    for p, lst in ids.items(): print("MAL  PMID inexistente:", p, [c for c, _ in lst]); mal += 1
    print("%d referencias revisadas; %d con PMID verificadas contra PubMed; %d problemas." % (n, len(lista), mal)); sys.exit(1 if mal else 0)
p = argparse.ArgumentParser(); s = p.add_subparsers(dest="c", required=True)
b = s.add_parser("buscar"); b.add_argument("consulta"); b.add_argument("-n", type=int, default=8); b.add_argument("--tipo")
v = s.add_parser("ver"); v.add_argument("pmids", nargs="+"); v.add_argument("--largo", type=int, default=900)
s.add_parser("verificar")
a = p.parse_args(); {"buscar": cmd_buscar, "ver": cmd_ver, "verificar": cmd_verificar}[a.c](a)
