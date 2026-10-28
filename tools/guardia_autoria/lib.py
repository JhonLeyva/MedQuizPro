"""Ayuda de autoría de casos «Sobrevive a la Guardia» v3. Genera guardia/casos/*.json (los JSON son la fuente de verdad; este script es solo el medio de producirlos).
Reglas que impone (y que luego vuelve a comprobar tests/guardia_test.js):
  · cada nodo de decisión tiene EXACTAMENTE cinco alternativas, una óptima y una «de omisión» (esperar/diferir: es lo que ocurre si se agota el tiempo);
  · las letras A–E se asignan DESPUÉS de definir la conducta correcta y los distractores, con una secuencia pseudoaleatoria global, balanceada y sin patrones
    (sin repeticiones contiguas ni progresiones de 3), y se guardan fijas en el JSON junto con la clave; las explicaciones van por alternativa, no por posición;
  · longitud comparable: avisa si la correcta es la más larga o si el rango de longitudes de un nodo es excesivo.
"""
import json, os, random, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAL = {"o": "optima", "a": "aceptable", "i": "incorrecta", "p": "peligrosa"}
FECHA = "2026-10-28"
COMP = {"rec": "Reconocimiento y triaje", "dx": "Diagnóstico e interpretación de estudios", "tto": "Tratamiento inicial", "seg": "Seguridad del paciente", "dis": "Disposición y seguimiento"}
LETRAS = "ABCDE"
AVISOS = []

def secuencia(n, semilla=20261028):
    """Letras de la respuesta correcta: bolsas barajadas (equilibrio) con restricciones locales anti-patrón."""
    rnd = random.Random(semilla); out = []
    def valido(l):
        if out and out[-1] == l: return False
        if len(out) >= 2 and (ord(out[-1]) - ord(out[-2])) == (ord(l) - ord(out[-1])) and out[-1] != out[-2]: return False   # progresión aritmética (ABC, CBA, ACE…)
        if len(out) >= 3 and out[-3] == out[-1] and out[-2] == l: return False                                              # patrón ABAB
        return True
    while len(out) < n:
        for _ in range(500):
            bolsa = list(LETRAS); rnd.shuffle(bolsa); ok = True; ent = list(out)
            for l in bolsa:
                if not valido(l): ok = False; break
                out.append(l)
            if ok: break
            del out[len(ent):]
        else: raise RuntimeError("no se pudo generar la secuencia")
    return out[:n]
_SEC = secuencia(2000)
_EST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "letras.json")     # «caso/nodo» → letra correcta: estable entre ejecuciones; borrar el archivo y reejecutar todos los casos en orden regenera todo
_MAPA = json.load(open(_EST)) if os.path.exists(_EST) else {}
def _letra(clave):
    if clave not in _MAPA:
        _MAPA[clave] = _SEC[len(_MAPA)]; json.dump(_MAPA, open(_EST, "w"), indent=0)
    return _MAPA[clave]

def D(texto, cal, sig, expl, omision=False, **extra):
    d = {"texto": texto.strip(), "calidad": CAL[cal], "siguiente": sig, "explicacion": expl.strip()}
    if omision: d["omision"] = True
    d.update(extra); return d

def N(estado, vit, grav, tipo, peso, decs, pregunta="¿Qué haces ahora?", tema="", comp="tto", refs=(), ayuda=None, img=None, lab=None, tiempo=None, deterioro=False, interp_lab=False):
    n = {"estado": estado, "vitales": vit, "gravedad": grav, "tipo": tipo, "peso": peso, "pregunta": pregunta, "_decs": decs, "_tema": tema, "_comp": comp, "_refs": list(refs)}
    if ayuda: n["ayuda"] = ayuda
    if img: n["imagen"] = {"id": img[0], "consigna": img[1]}
    if lab: n["laboratorio"] = {"titulo": lab[0], "resultados": [dict({"prueba": x[0], "valor": x[1]}, **({"etiqueta": x[2]} if len(x) > 2 and x[2] else {}), **({"ref": x[3]} if len(x) > 3 and x[3] else {})) for x in lab[1]], "ocultar_marcas": bool(interp_lab)}
    if tiempo: n["tiempo"] = tiempo
    if deterioro: n["deterioro"] = True
    return n

def F(tipo, titulo, msg): return {"final": {"tipo": tipo, "titulo": titulo, "mensaje": msg}}
def R(id, tipo, titulo, org, autores, anio, vig, rec, pmid=None, doi=None, url=None, version=None, complementaria=False):
    r = {"id": id, "tipo": tipo, "titulo": titulo, "organismo": org, "autores": autores, "anio": anio, "version": version or "", "pmid": pmid or "", "doi": doi or "", "url": url or "", "fecha_consulta": FECHA, "vigencia": vig, "recomendacion": rec}
    if complementaria: r["complementaria"] = True
    return r

_SUB = re.compile(r"(?<![,;:(]) (ya que|pues|porque|aunque|mientras|dado que|por lo que|siendo|pese a que|a pesar de que|a pesar de|para que)\b")
def _estilo(t):
    """Puntuación uniforme en TODAS las alternativas: coma antes de la subordinada, para que el estilo no delate la correcta."""
    return _SUB.sub(lambda m: ", " + m.group(1), t)

def _asignar(caso_id, nid, n, omision=True):
    decs = n.pop("_decs"); tema = n.pop("_tema"); comp = n.pop("_comp"); refs = n.pop("_refs")
    donde = f"{caso_id}/{nid}"
    assert len(decs) == 5, f"{donde}: deben ser 5 alternativas y hay {len(decs)}"
    assert sum(d["calidad"] == "optima" for d in decs) == 1, f"{donde}: una y solo una óptima"
    if omision: assert sum(bool(d.get("omision")) for d in decs) == 1, f"{donde}: una y solo una alternativa de omisión (qué pasa si se agota el tiempo)"
    assert not [d for d in decs if d.get("omision") and d["calidad"] == "optima"], f"{donde}: la omisión no puede ser la óptima"
    objetivo = _letra(f"{caso_id}/{nid}")
    correcta = next(d for d in decs if d["calidad"] == "optima"); otras = [d for d in decs if d is not correcta]
    rnd = random.Random(f"{caso_id}:{nid}:{len(decs)}"); rnd.shuffle(otras)
    orden = []; it = iter(otras)
    for l in LETRAS: orden.append(correcta if l == objetivo else next(it))
    for l, d in zip(LETRAS, orden):
        d["id"] = l; d.setdefault("tema", tema); d.setdefault("competencia", COMP[comp]); d.setdefault("refs", list(refs))
        for k in ("texto", "explicacion"): assert d[k] and "  " not in d[k], f"{donde}/{l}: {k} vacío o con doble espacio"
        assert not re.search(r"\b(opción|alternativa|letra)\s+[A-E]\b", d["explicacion"]), f"{donde}/{l}: la explicación no debe nombrar letras (se reordenan)"
        assert not re.search(r"(?i)todas las anteriores|ninguna de las anteriores", d["texto"]), f"{donde}/{l}: prohibido «todas/ninguna de las anteriores»"
        d["texto"] = _estilo(d["texto"])
        assert 45 <= len(d["texto"]) <= 190, f"{donde}/{l}: longitud de la alternativa fuera de 45–190 ({len(d['texto'])})"
    L = [len(d["texto"]) for d in orden]; lc = len(correcta["texto"])
    if lc == max(L) and L.count(lc) == 1: AVISOS.append(f"{donde}: la correcta es la más larga ({lc} vs {sorted(L)})")
    if max(L) / min(L) > 1.7: AVISOS.append(f"{donde}: rango de longitudes amplio {sorted(L)}")
    n["decisiones"] = orden; n["clave"] = objetivo
    return n

def construir(c):
    """c: dict del caso con nodos creados por N()/F(); asigna letras y valida el grafo básico."""
    for nid, n in c["nodos"].items():
        if "final" not in n: _asignar(c["id"], nid, n)
    ids = set(c["nodos"])
    for nid, n in c["nodos"].items():
        if "final" in n: continue
        for d in n["decisiones"]: assert d["siguiente"] in ids, f"{c['id']}/{nid}/{d['id']}: destino {d['siguiente']} no existe"
    return c

def guardar(c):
    construir(c)
    ruta = os.path.join(RAIZ, "guardia", "casos", c["id"] + ".json")
    json.dump(c, open(ruta, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    cl = "".join(n["clave"] for n in c["nodos"].values() if "clave" in n)
    print(c["id"], len([n for n in c["nodos"].values() if "final" not in n]), "nodos de decisión · claves:", cl)
    for a in AVISOS: print("  AVISO", a)
    AVISOS.clear()


# ---------- Consulta Clínica Experta ----------
def Q(enunciado, decs, tema="", comp="dx", refs=(), peso=2):
    """Pregunta de opción única de la consulta (cinco alternativas A–E, una óptima). Las letras se asignan igual que en la guardia."""
    return {"enunciado": enunciado, "peso": peso, "_decs": decs, "_tema": tema, "_comp": comp, "_refs": list(refs)}

def guardar_consulta(c):
    for k, q in c["preguntas"].items():
        nodo = {"_decs": q.pop("_decs"), "_tema": q.pop("_tema"), "_comp": q.pop("_comp"), "_refs": q.pop("_refs")}
        _asignar(c["id"], k, nodo, omision=False)
        q["decisiones"] = nodo["decisiones"]; q["clave"] = nodo["clave"]
        for d in q["decisiones"]: d.pop("siguiente", None)
    ruta = os.path.join(RAIZ, "consulta", "casos", c["id"] + ".json"); os.makedirs(os.path.dirname(ruta), exist_ok=True)
    json.dump(c, open(ruta, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(c["id"], "preguntas:", {k: q["clave"] for k, q in c["preguntas"].items()}, "· pruebas:", len(c["pruebas"]))
    for a in AVISOS: print("  AVISO", a)
    AVISOS.clear()
