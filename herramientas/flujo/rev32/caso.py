import sys; sys.path.insert(0, ".")
import json, re, os, importlib, c28
for m in sorted(f[:-3] for f in os.listdir(".") if re.fullmatch(r"content30[a-z]+\.py", f)):
    importlib.import_module(m)
spec={f["id"]:f for f in c28.F28}
for i in sys.argv[1:]:
    f=spec[i]
    print(f"== {i} [{f['tipo']}] tri={bool(f.get('triada'))} esc={bool(f.get('escala'))} banda={bool(f.get('banda'))}")
    print("  T:", f["tema"]["title"], "|", " ".join(f["tema"]["lines"]))
    print("  C:", f["caso"]["title"], "|", " ".join(f["caso"]["lines"]), "|P:", " · ".join(f["perlas"]))
