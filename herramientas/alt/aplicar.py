"""Aplica las decisiones alt/r*.py a los 17 bancos ORIGINALES (site/bancos del commit 4ba94e6c2654,
antes del cambio) y escribe alt/out/bancos. Después: cp alt/out/bancos/*.json site/bancos/
Cada decisión: texto = nueva alternativa E; dict = {índice: texto}. La clave no cambia de posición."""
import json, glob, os, re, shutil, subprocess
BASE = "4ba94e6c2654"  # commit con los bancos originales

R = {}
for f in sorted(glob.glob("alt/r[0-9][0-9].py")):
    ns = {}
    exec(open(f).read(), ns)
    for k, v in ns["R"].items():
        assert k not in R, ("decisión repetida", k)
        R[k] = v
ns = {}
exec(open("alt/comentarios.py").read(), ns)
CM, usados_cm = ns["C"], set()
OUT = "alt/out/bancos"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
cambios, usados = [], set()
norm = lambda s: re.sub(r"\s+", " ", s.strip().lower().rstrip("."))
for f in sorted(glob.glob("site/bancos/*.json")):
    raw = subprocess.check_output(["git", "show", f"{BASE}:herramientas/{f}"]).decode("utf-8")
    d = json.loads(raw)
    L = d if isinstance(d, list) else d.get("preguntas", [])
    for q in L:
        if q["id"] not in R:
            continue
        usados.add(q["id"])
        r = R[q["id"]]
        r = {4: r} if isinstance(r, str) else r
        es_dict = isinstance(q["opciones"], dict)
        keys = list(q["opciones"].keys()) if es_dict else list(range(len(q["opciones"])))
        ops = list(q["opciones"].values()) if es_dict else list(q["opciones"])
        assert len(ops) == 5, q["id"]
        ci = q["correcta"] if "correcta" in q else "ABCDE".index(q["clave_correcta"].strip()[0])
        for i, txt in r.items():
            txt = txt.strip()
            assert txt and txt.lower() != norm(ops[i]), (q["id"], "sin cambio", txt)
            cambios.append((os.path.basename(f), q["id"], "ABCDE"[i], ops[i], txt, i == ci))
            ops[i] = txt
        low = [norm(o) for o in ops]
        assert len(set(low)) == 5, (q["id"], "alternativas repetidas", ops)
        if es_dict:
            q["opciones"] = dict(zip(keys, ops))
        else:
            q["opciones"] = ops
    for q in L:
        for viejo, nuevo in CM.get(q["id"], []):
            hecho = False
            for fld in ("explicacion", "comentario"):
                if q.get(fld) and viejo in q[fld]:
                    q[fld] = q[fld].replace(viejo, nuevo)
                    hecho = True
            assert hecho, (q["id"], "texto no encontrado", viejo[:40])
            usados_cm.add(q["id"])
    json.dump(d, open(f"{OUT}/{os.path.basename(f)}", "w"), ensure_ascii=False, indent=2 if raw.lstrip().startswith(("[\n", "{\n")) else None)
assert usados_cm == set(CM), set(CM) - usados_cm
falt = set(R) - usados
assert not falt, ("IDs inexistentes", falt)
json.dump(cambios, open("alt/out/cambios.json", "w"), ensure_ascii=False, indent=0)
print("preguntas cambiadas:", len(usados), "· alternativas cambiadas:", len(cambios),
      "· de ellas la clave:", sum(c[5] for c in cambios))
