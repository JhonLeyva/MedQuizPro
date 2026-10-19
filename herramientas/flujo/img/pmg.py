"""Guías recientes en PubMed (para actualizar la bibliografía).
Uso: python3 pmg.py "tema en inglés" [desde=2023] [n=8]  → título · revista · año · PMID"""
import json, subprocess, sys, urllib.parse, time
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(u):
    for k in range(4):
        r = subprocess.run(["curl", "-sS", "--max-time", "60", u], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode()
        time.sleep(2 ** (k + 1))
    raise SystemExit("sin conexión")
q, desde = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "2023"
n = sys.argv[3] if len(sys.argv) > 3 else "8"
term = f"({q}) AND (guideline[pt] OR practice guideline[pt] OR guideline[ti] OR guidelines[ti] OR consensus[ti] OR recommendations[ti]) AND {desde}:2026[dp]"
ids = json.loads(get(EU + "esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=%s&term=%s" % (n, urllib.parse.quote(term))))["esearchresult"]["idlist"]
if not ids:
    print("(nada)"); sys.exit()
r = json.loads(get(EU + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids)))["result"]
for i in ids:
    a = r[i]
    print(f"{a.get('pubdate','')[:4]} · {a.get('source','')} · {a.get('title','')[:150]} · PMID {i}")
