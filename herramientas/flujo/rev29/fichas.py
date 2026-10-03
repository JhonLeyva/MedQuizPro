"""Fichas de revisión de la entrega 2 (500 a 999) en tandas de 25: rev29/tNN.txt"""
import json, re, sys
sys.path.insert(0, ".")
from c28 import BANCO, opciones
js = open("../site/algoritmos.js", encoding="utf-8").read()
orden = re.findall(r'"([A-Z]+-\d+)":\s*\{[^}]*?imagen:', js)
E1 = orden[500:1000]
json.dump(E1, open("rev29/entrega2.json", "w"))
for t in range(0, 500, 25):
    out = []
    for i in E1[t:t + 25]:
        q = BANCO[i]
        ops, ci = opciones(i)
        out.append(f"### {i} | {q.get('tema')} | {q.get('año')}")
        out.append(q["enunciado"].strip())
        for k, o in enumerate(ops):
            out.append(f"  {'*' if k == ci else ' '}{'ABCDE'[k]}) {o}")
        out.append("EXP: " + re.sub(r"\s+", " ", q.get("explicacion", ""))[:900])
        out.append("")
    open(f"rev29/t{t // 25:02d}.txt", "w").write("\n".join(out))
print(len(E1))
