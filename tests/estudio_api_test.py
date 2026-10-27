#!/usr/bin/env python3
"""python3 tests/estudio_api_test.py — confianza por intento, Repaso de hoy y tarjetas Cloze contra una copia aislada del backend (PHP embebido).
No toca cuenta_datos/ del proyecto. No usa IA."""
import http.cookiejar, json, os, shutil, socket, sqlite3, subprocess, sys, tempfile, time, urllib.error, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); fallos = 0; total = 0
def ok(c, m):
    global fallos, total
    total += 1
    if not c: fallos += 1; print("FALLA:", m)
def puerto():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p
banco = {}
for f in os.listdir(RAIZ + "/bancos"):
    for q in json.load(open(RAIZ + "/bancos/" + f, encoding="utf-8"))["preguntas"]: banco[q["id"]] = q
def letras(q): return "ABCDE"[:len(q["opciones"])] if isinstance(q["opciones"], list) else sorted(q["opciones"])
def mala(id_): q = banco[id_]; return next(l for l in letras(q) if l != q["clave_correcta"])
tmp = tempfile.mkdtemp(); proc = None
try:
    for f in ("cuenta.php", "estudio.php", "estudio_lib.php", "feynman_lib.php", "guias_lib.php", "flashcards_lib.php"): shutil.copy(os.path.join(RAIZ, f), tmp)
    shutil.copytree(RAIZ + "/bancos", tmp + "/bancos"); os.makedirs(tmp + "/guias"); open(tmp + "/guias/indice.json", "w").write('{"docs":[],"fragmentos":[]}')
    pp = puerto(); base = f"http://127.0.0.1:{pp}"
    proc = subprocess.Popen(["php", "-S", f"127.0.0.1:{pp}", "-t", tmp], env=dict(os.environ, PHP_CLI_SERVER_WORKERS="3"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    def cliente():
        cj = http.cookiejar.CookieJar(); op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        def llamar(ruta, datos=None, cab=None):
            h = {"Content-Type": "application/json", "X-MQP": "1", "Origin": base}; h.update(cab or {})
            req = urllib.request.Request(base + ruta, data=None if datos is None else json.dumps(datos).encode(), headers=h)
            try: r = op.open(req); return r.status, json.loads(r.read() or b"{}")
            except urllib.error.HTTPError as e:
                try: return e.code, json.loads(e.read() or b"{}")
                except Exception: return e.code, {}
        return llamar
    A, B, ANON = cliente(), cliente(), cliente()
    for c, n in ((A, "a"), (B, "b")): ok(c("/cuenta.php?a=registro", {"nombre": "Usuario " + n, "correo": n + "@p.pe", "clave": "clave12345", "acepto": True})[0] == 201, "registro " + n)
    rid = lambda: "r" + os.urandom(8).hex()
    ids = [i for i in banco if not isinstance(banco[i]["opciones"], dict)][:6]; q0 = ids[0]
    intento = lambda c, qid, el, conf, **k: c("/estudio.php?a=intento", dict({"pregunta_id": qid, "elegida": el, "confianza": conf, "modo": "estudio", "req_id": rid()}, **k))

    # ---- acceso
    s, j = ANON("/estudio.php?a=estado"); ok(s == 200 and j["sesion"] is False, "estado sin sesión: sesion=false (la interfaz no pide confianza)")
    s, j = A("/estudio.php?a=estado"); ok(j["sesion"] is True, "estado con sesión: true")
    for ruta, d in (("/estudio.php?a=intento", {"pregunta_id": q0, "elegida": "A"}), ("/estudio.php?a=repaso", None), ("/estudio.php?a=olvidar", {})):
        ok(ANON(ruta, d)[0] == 401, "sin sesión → 401 " + ruta)
    ok(A("/estudio.php?a=intento", {"pregunta_id": q0, "elegida": "A"}, cab={"X-MQP": "0"})[0] == 403, "sin cabecera X-MQP → 403")
    ok(A("/estudio.php?a=intento", {"pregunta_id": q0, "elegida": "A"}, cab={"Origin": "http://otro.example"})[0] == 403, "otro origen → 403")

    # ---- el servidor decide el acierto y la etiqueta (con preguntas cuyas opciones son LISTA, la mayoría del banco)
    cl = banco[q0]["clave_correcta"].strip().upper(); mal = mala(q0)
    s, j = intento(A, q0, mal, "alta"); ok(s == 201 and j["acierto"] is False and j["etiqueta"] == "falso_concepto" and j["pendiente"], "fallo con confianza alta → falso concepto (calculado en el servidor)")
    s, j = intento(A, ids[1], banco[ids[1]]["clave_correcta"].strip().upper(), "baja"); ok(j["acierto"] is True and j["etiqueta"] == "laguna", "acierto adivinando → laguna")
    s, j = intento(A, ids[2], mala(ids[2]), "baja"); ok(j["etiqueta"] == "refuerzo", "fallo con confianza baja → refuerzo")
    s, j = intento(A, ids[3], banco[ids[3]]["clave_correcta"].strip().upper(), "alta"); ok(j["etiqueta"] == "acierto_seguro" and not j["pendiente"], "acierto seguro → no pendiente")
    s, j = intento(A, ids[4], mala(ids[4]), None); ok(j["etiqueta"] == "refuerzo", "fallo sin indicar confianza → refuerzo")
    ok(intento(A, "NOEXISTE-1", "A", "alta")[0] == 404, "pregunta inexistente → 404")
    ok(intento(A, q0, "Z", "alta")[0] == 400 and intento(A, q0, "A", "segurisimo")[0] == 400, "letra o confianza inválidas → 400")
    ok(A("/estudio.php?a=intento", {"pregunta_id": q0, "elegida": "A", "confianza": "alta", "acierto": True, "etiqueta": "acierto_seguro"})[1].get("acierto") == (cl == "A"), "el cliente no puede falsear el acierto ni la etiqueta")
    # idempotencia
    r1 = rid(); s1, _ = A("/estudio.php?a=intento", {"pregunta_id": ids[5], "elegida": mala(ids[5]), "confianza": "media", "req_id": r1}); s2, j2 = A("/estudio.php?a=intento", {"pregunta_id": ids[5], "elegida": mala(ids[5]), "confianza": "media", "req_id": r1})
    db = sqlite3.connect(tmp + "/cuenta_datos/mqp.sqlite"); ok(j2["repetido"] is True and db.execute("select count(*) from intentos_respuesta where req_id=?", (r1,)).fetchone()[0] == 1, "el mismo req_id no se registra dos veces")

    # ---- Repaso de hoy con datos reales
    s, j = A("/estudio.php?a=repaso"); ok(s == 200 and j["ok"], "repaso responde")
    ok(j["ids"][0] == q0 and set(j["ids"]) >= {q0, ids[1], ids[2], ids[4], ids[5]} and ids[3] not in j["ids"], "por reforzar: el falso concepto va primero y el acierto seguro no aparece: " + str(j["ids"][:6]))
    ok(all(x["enunciado"] and x["especialidad"] and x["texto"] for x in j["refuerzo"]), "cada elemento trae enunciado y especialidad reales del banco")
    ok(j["calibracion"]["alta"]["n"] >= 2 and j["calibracion"]["alta"]["aciertos"] >= 1 and j["con_confianza"] >= 5, "calibración con los datos reales")
    ok(j["tarjetas"] == {"pendientes": 0, "total": 0} and j["semana"]["intentos"] >= 6, "tarjetas y resumen de la semana")
    # al acertar con seguridad la pregunta sale
    intento(A, q0, cl, "alta"); s, j = A("/estudio.php?a=repaso"); ok(q0 not in j["ids"], "acertar la pregunta la saca de la lista")
    # aislamiento
    s, j = B("/estudio.php?a=repaso"); ok(j["ids"] == [] and j["con_confianza"] == 0, "B no ve los datos de A")
    # tarjetas vencidas
    A("/cuenta.php?a=fc_crear", {"tarjetas": [{"frente": "¿Frente de prueba?", "dorso": "Dorso de prueba", "pregunta": q0}]}); s, j = A("/estudio.php?a=repaso"); ok(j["tarjetas"]["pendientes"] == 1, "las tarjetas vencidas reales aparecen en el repaso")

    # ---- Cloze en el servidor
    t = {"frente": "El tratamiento de elección es la {{c1::penicilina benzatínica}} en dosis única.", "dorso": "Respuesta: penicilina benzatínica", "pregunta": q0}
    s, j = A("/cuenta.php?a=fc_crear", {"tarjetas": [t]}); ok(s == 201 and j["creadas"] == 1, "tarjeta Cloze válida se guarda en el mazo existente")
    for malo in ("Texto {{c1::}} sin respuesta y más contexto.", "{{c1::Todo oculto en esta tarjeta de prueba}}", "Hay {{c1::llaves sin cerrar en este texto largo."):
        s, j = A("/cuenta.php?a=fc_crear", {"tarjetas": [dict(t, frente=malo)]}); ok(s == 400, "Cloze inválida rechazada: " + malo[:30])
    s, fc = A("/cuenta.php?a=fc_listar"); tid = next(x["id"] for x in fc["tarjetas"] if "{{c1" in x["frente"])
    ok(A("/cuenta.php?a=fc_editar", {"id": tid, "frente": "{{c1::}} roto y vacío para esta prueba", "dorso": "x y"})[0] == 400, "editar una Cloze dejándola inválida se rechaza")
    ok(A("/cuenta.php?a=fc_editar", {"id": tid, "frente": "La {{c1::penicilina}} benzatínica es de elección en la sífilis.", "dorso": "Respuesta: penicilina"})[0] == 200, "editar una Cloze válida funciona")
    s, ex = A("/cuenta.php?a=exportar", {}); ok(s == 200 and len(ex["intentos"]) >= 7 and all(set(i) == {"pregunta", "elegida", "correcta", "confianza", "etiqueta", "modo", "t"} for i in ex["intentos"]), "«Descargar mis datos» incluye los intentos propios")

    # ---- borrado y cascada
    ok(A("/estudio.php?a=olvidar", {})[0] == 200 and A("/estudio.php?a=repaso")[1]["con_confianza"] == 0, "«Borrar mi historial» lo vacía")
    intento(B, q0, mal, "alta"); ok(B("/cuenta.php?a=eliminar", {"clave": "clave12345"})[0] == 200, "B elimina su cuenta")
    db.close(); db = sqlite3.connect(tmp + "/cuenta_datos/mqp.sqlite"); ok(db.execute("select count(*) from intentos_respuesta where usuario=2").fetchone()[0] == 0, "al eliminar la cuenta se borran sus intentos (cascada)")
finally:
    if proc: proc.terminate()
    shutil.rmtree(tmp, ignore_errors=True)
print(f"{fallos} fallos de {total}" if fallos else f"OK: {total} comprobaciones de la API de estudio"); sys.exit(1 if fallos else 0)
