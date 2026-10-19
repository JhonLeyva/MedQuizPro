#!/usr/bin/env python3
"""python3 tests/guias_test.py — prueba la cadena completa con guías FICTICIAS de prueba (nunca se copian a guias/):
PDF → ingesta → verificación de citas (positiva y negativa) → búsqueda BM25 en PHP → validación de citas."""
import json, os, subprocess, sys, tempfile, shutil
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fallos = 0
def ok(c, m):
    global fallos
    if not c: fallos += 1; print("FALLA:", m)

def pdf(paginas, ruta):
    """PDF mínimo con texto real (Helvetica), una página por elemento."""
    objs = []; n = 3 + 2 * len(paginas)
    def esc(t): return t.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    kids = " ".join(f"{4 + 2 * i} 0 R" for i in range(len(paginas)))
    objs.append("<< /Type /Catalog /Pages 2 0 R >>")
    objs.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(paginas)} >>")
    objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    for i, lineas in enumerate(paginas):
        cont = "BT /F1 11 Tf 50 750 Td 14 TL " + " ".join(f"({esc(l)}) Tj T*" for l in lineas) + " ET"
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents {5 + 2 * i} 0 R /Resources << /Font << /F1 3 0 R >> >> >>")
        objs.append(f"<< /Length {len(cont.encode('latin-1'))} >>\nstream\n{cont}\nendstream")
    out = b"%PDF-1.4\n"; pos = []
    for i, o in enumerate(objs, 1):
        pos.append(len(out)); out += f"{i} 0 obj\n{o}\nendobj\n".encode("latin-1")
    x = len(out); out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    for p in pos: out += f"{p:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{x}\n%%EOF".encode()
    open(ruta, "wb").write(out)

tmp = tempfile.mkdtemp()
try:
    os.makedirs(tmp + "/pdf")
    pdf([["GUIA DE PRUEBA NACIONAL (FICTICIA)", "", "La sindrome zeta se define por tres criterios: fiebre, rash y adenopatias.", "El tratamiento inicial de la sindrome zeta es reposo e hidratacion."],
         ["", "Pagina dos: la sindrome zeta grave requiere hospitalizacion si hay hipotension.", "Se reevalua a las 48 horas."]], tmp + "/pdf/nac.pdf")
    pdf([["INTERNATIONAL TEST GUIDELINE (FICTITIOUS)", "", "Zeta syndrome treatment: supportive care and fluids. Hospitalise if hypotension."]], tmp + "/pdf/int.pdf")
    json.dump([
        {"id": "nac-test", "archivo": "nac.pdf", "titulo": "Guía de prueba nacional", "institucion": "Institución ficticia", "pais": "Perú", "tipo": "nacional", "anio": 2021, "version": "v1", "estado": "reemplazada", "reemplazada_por": "Guía de prueba 2025"},
        {"id": "int-test", "archivo": "int.pdf", "titulo": "Test guideline", "institucion": "Fictitious Org", "pais": "Internacional", "tipo": "internacional", "anio": 2024, "version": "2024", "estado": "vigente", "temas": ["sindrome zeta", "tratamiento inicial"]},
        {"id": "incompleto", "archivo": "nac.pdf", "titulo": "sin campos"}], open(tmp + "/man.json", "w"))
    r = subprocess.run([sys.executable, RAIZ + "/tools/ingestar_guias.py", "--manifest", tmp + "/man.json", "--pdfs", tmp + "/pdf", "--salida", tmp + "/indice.json"], capture_output=True, text=True)
    ok(r.returncode == 1 and "faltan campos" in r.stdout, "una ficha incompleta se rechaza (código 1) sin inventar datos")
    ix = json.load(open(tmp + "/indice.json"))
    ok(len(ix["docs"]) == 2 and len(ix["fragmentos"]) >= 3, "indexa los 2 documentos válidos")
    ok({f["pagina"] for f in ix["fragmentos"] if f["doc"] == "nac-test"} == {1, 2}, "conserva la página de origen")
    v = subprocess.run([sys.executable, RAIZ + "/tools/verificar_indice.py", "--indice", tmp + "/indice.json", "--pdfs", tmp + "/pdf"], capture_output=True, text=True)
    ok(v.returncode == 0, "verificación positiva: cada fragmento está en su página")
    mal = json.loads(json.dumps(ix)); [f.__setitem__("pagina", 1) for f in mal["fragmentos"] if f["pagina"] == 2]
    json.dump(mal, open(tmp + "/mal.json", "w"))
    v2 = subprocess.run([sys.executable, RAIZ + "/tools/verificar_indice.py", "--indice", tmp + "/mal.json", "--pdfs", tmp + "/pdf"], capture_output=True, text=True)
    ok(v2.returncode == 1 and "NO está en la página" in v2.stdout, "verificación negativa: una página falsa se detecta")
    falso = json.loads(json.dumps(ix)); falso["fragmentos"][0]["texto"] = "Texto inventado que no está en el documento original de ninguna manera."
    json.dump(falso, open(tmp + "/falso.json", "w"))
    v3 = subprocess.run([sys.executable, RAIZ + "/tools/verificar_indice.py", "--indice", tmp + "/falso.json", "--pdfs", tmp + "/pdf"], capture_output=True, text=True)
    ok(v3.returncode == 1, "verificación negativa: un texto inventado se detecta")
    # modo espejo: comparación ficticia + verificador
    def fr(doc, cita):
        return next(f["id"] for f in ix["fragmentos"] if f["doc"] == doc and " ".join(cita.split()).lower() in " ".join(f["texto"].split()).lower())
    frs = {"nac-test": fr("nac-test", "tratamiento inicial de la sindrome zeta"), "int-test": fr("int-test", "supportive care and fluids")}
    frs_p2 = fr("nac-test", "grave requiere hospitalizacion")
    comp = [{"id": "zeta", "titulo": "Síndrome zeta", "temas": ["sindrome zeta"], "preguntas": ["Q-1"],
             "nacional": {"frag": frs["nac-test"], "resumen": "Norma de prueba"}, "internacional": {"frag": frs["int-test"], "resumen": "Guideline de prueba"},
             "filas": [{"criterio": "Tratamiento inicial", "tipo": "equivalente", "nacional": {"texto": "Reposo e hidratación", "frag": frs["nac-test"], "cita_literal": "tratamiento inicial de la sindrome zeta es reposo"}, "internacional": {"texto": "Cuidados de soporte y líquidos", "frag": frs["int-test"], "cita_literal": "supportive care and fluids"}},
                       {"criterio": "Hospitalización", "tipo": "discrepancia", "nacional": {"texto": "Si hay hipotensión", "frag": frs_p2, "cita_literal": "grave requiere hospitalizacion si hay hipotension"}, "internacional": None}]},
            {"id": "solo-nac", "titulo": "Solo nacional", "temas": ["otro tema"], "nacional": {"frag": frs["nac-test"]}, "internacional": None, "filas": []}]
    json.dump(comp, open(tmp + "/comp.json", "w"))
    c1 = subprocess.run([sys.executable, RAIZ + "/tools/verificar_comparaciones.py", "--comparaciones", tmp + "/comp.json", "--indice", tmp + "/indice.json"], capture_output=True, text=True)
    ok(c1.returncode == 1 and "una discrepancia necesita las dos fuentes" in c1.stdout, "verificador: una discrepancia sin las dos fuentes es inválida")
    comp[0]["filas"][1]["internacional"] = {"texto": "Si hay hipotensión", "frag": frs["int-test"], "cita_literal": "hospitalise if hypotension"}
    json.dump(comp, open(tmp + "/comp.json", "w"))
    c2 = subprocess.run([sys.executable, RAIZ + "/tools/verificar_comparaciones.py", "--comparaciones", tmp + "/comp.json", "--indice", tmp + "/indice.json"], capture_output=True, text=True)
    ok(c2.returncode == 0, "verificador: comparación válida con citas literales reales (" + c2.stdout.strip() + ")")
    comp[0]["filas"][0]["nacional"]["cita_literal"] = "esta frase no existe en la guía original"
    json.dump(comp, open(tmp + "/comp_mala.json", "w"))
    c3 = subprocess.run([sys.executable, RAIZ + "/tools/verificar_comparaciones.py", "--comparaciones", tmp + "/comp_mala.json", "--indice", tmp + "/indice.json"], capture_output=True, text=True)
    ok(c3.returncode == 1 and "cita_literal no aparece" in c3.stdout, "verificador: cita literal inventada se detecta")
    comp[0]["filas"][0]["nacional"]["cita_literal"] = "tratamiento inicial de la sindrome zeta es reposo"
    comp[0]["filas"][0]["nacional"]["frag"] = frs["int-test"]
    json.dump(comp, open(tmp + "/comp_mezcla.json", "w"))
    c4 = subprocess.run([sys.executable, RAIZ + "/tools/verificar_comparaciones.py", "--comparaciones", tmp + "/comp_mezcla.json", "--indice", tmp + "/indice.json"], capture_output=True, text=True)
    ok(c4.returncode == 1 and "no nacional" in c4.stdout, "verificador: no se mezcla una guía internacional en la columna nacional")
    comp[0]["filas"][0]["nacional"]["frag"] = frs["nac-test"]; json.dump(comp, open(tmp + "/comp.json", "w"))
    p = subprocess.run(["php", RAIZ + "/tests/guias_test.php", tmp + "/indice.json", tmp + "/comp.json"], capture_output=True, text=True)
    print(p.stdout.strip()); ok(p.returncode == 0, "pruebas PHP de búsqueda y citas")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
print(f"{fallos} fallos" if fallos else "OK: pruebas de guías pasaron"); sys.exit(1 if fallos else 0)
