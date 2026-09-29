import json, glob, importlib.util, re, sys
Q = {q["n"]: q for q in json.load(open("cbq.json"))}
D, O, N, X = {}, {}, {}, {}
for f in sorted(glob.glob("r[0-9][0-9].py")):
    sp = importlib.util.spec_from_file_location(f[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    for a, b in ((D, m.D), (O, m.O), (N, m.N), (X, m.X)):
        dup = set(a) & set(b)
        assert not dup, (f, dup)
        a.update(b)
def final(n):
    q = Q[n]; op = dict(q["opciones"]); op.update(O.get(n, {}))
    return N.get(n, q["enunciado"]), op
if __name__ == "__main__":
    upto = int(sys.argv[1])
    both = set(D) & set(X); assert not both, both
    miss = [n for n in range(1, upto + 1) if n not in D and n not in X]
    print("faltan", miss)
    for n, (t, k, c) in D.items():
        e, op = final(n)
        assert sorted(op) == list("ABCDE"), (n, sorted(op))
        assert k in "ABCDE"
        if k != Q[n]["clave"]: print("clave cambiada", n, Q[n]["clave"], "->", k)
        w = len(c.split())
        if w < 70: print("corto", n, w)
    print("D", len(D), "X", len(X))
