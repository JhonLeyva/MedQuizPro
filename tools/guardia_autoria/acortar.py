import sys
def aplicar(arch, R):
    g = open(arch).read()
    for a, b in R:
        if a not in g: print("NO ENCONTRADO:", a[:60]); sys.exit(1)
        g = g.replace(a, b)
    open(arch, "w").write(g)
