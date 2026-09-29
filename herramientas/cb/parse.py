import re, json
t = open("cb.txt").read()
ki = t.index("CIENCIAS BÁSICAS – CLAVES")
body, keyt = t[:ki], t[ki:]
# quitar cabeceras de página
body = re.sub(r"Mejores médicos\.\s*\n\s*www\.villamedicgroup\.com\s*\n[\s\n]*Página \| \d+\s*\n", "\n", body)
body = body.replace("\f", "")
body = re.sub(r"BANCO DE PREGUNTAS CIENCIAS BÁSICAS\s*\nED\. 2019\s*\n", "", body)
# claves
toks = [x.strip() for x in re.sub(r"Mejores médicos\.|www\.villamedicgroup\.com|Página \| \d+|Pregunta|Clave|CIENCIAS BÁSICAS – CLAVES", " ", keyt).split()]
key = {}
i = 0
while i < len(toks) - 1:
    if toks[i].isdigit() and re.fullmatch(r"[A-E]", toks[i + 1]):
        key[int(toks[i])] = toks[i + 1]; i += 2
    else: i += 1
parts = re.split(r"\n\s*(\d{1,3})\)\s*\n", "\n" + body)
Q = []
for k in range(1, len(parts), 2):
    n = int(parts[k]); txt = parts[k + 1]
    lines = [l.strip() for l in txt.split("\n")]
    # opciones: línea "A." sola
    # separar "A. texto" en dos líneas
    nl = []
    for l in lines:
        m = re.match(r"^([A-E])\.\s+(\S.*)$", l)
        if m: nl += [m.group(1) + ".", m.group(2)]
        else: nl.append(l)
    lines = nl
    idx = [j for j, l in enumerate(lines) if re.fullmatch(r"[A-E]\.", l)]
    starts = [j for j in idx if lines[j] == "A."]
    s = starts[-1] if starts else None
    stem = " ".join(l for l in lines[:s] if l) if s is not None else " ".join(lines)
    opts = {}
    if s is not None:
        cur = None
        for l in lines[s:]:
            if re.fullmatch(r"[A-E]\.", l): cur = l[0]; opts[cur] = []
            elif cur and l: opts[cur].append(l)
        opts = {a: " ".join(v) for a, v in opts.items()}
    stem = re.sub(r"\s+", " ", stem).strip()
    Q.append({"n": n, "enunciado": stem, "opciones": opts, "clave": key.get(n)})
print(len(Q), len(key), [q["n"] for q in Q if len(q["opciones"]) != 5], [q["n"] for q in Q if not q["clave"]])
ns = [q["n"] for q in Q]; print("orden ok", ns == list(range(1, 459)))
json.dump(Q, open("cbq.json", "w"), ensure_ascii=False, indent=0)
