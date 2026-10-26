#!/usr/bin/env python3
"""python3 tests/feynman_api_test.py — Tutor Feynman IA de punta a punta contra una copia aislada del backend (PHP embebido) y un
proveedor de IA SIMULADO que solo existe en esta prueba (el producto jamás simula la IA). No toca cuenta_datos/ del proyecto.
Cubre: acceso, contexto real del banco, fases, pistas, formato inválido, errores de IA, duplicados, concurrencia, límites, informe,
tarjetas (nunca se guardan solas), aislamiento entre estudiantes, borrado y cascada al eliminar la cuenta."""
import http.cookiejar, http.server, json, os, shutil, socket, sqlite3, subprocess, sys, tempfile, threading, time, urllib.error, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fallos = 0; total = 0
def ok(c, m):
    global fallos, total
    total += 1
    if not c: fallos += 1; print("FALLA:", m)
def puerto():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p

cola = []; pedidos = []; lock = threading.Lock()
class IA(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        cuerpo = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        with lock:
            pedidos.append(cuerpo); item = cola.pop(0) if cola else ("http", 500)
        if isinstance(item, dict) and item.get("_demora"): time.sleep(item["_demora"]); item = {k: v for k, v in item.items() if k != "_demora"}
        if isinstance(item, tuple):
            self.send_response(item[1]); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(b'{"error":{"message":"detalle interno del proveedor SECRETO"}}'); return
        txt = item if isinstance(item, str) else json.dumps(item, ensure_ascii=False)
        r = json.dumps({"choices": [{"message": {"content": txt}}]}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(r))); self.end_headers(); self.wfile.write(r)
pia = puerto(); srv = http.server.ThreadingHTTPServer(("127.0.0.1", pia), IA); threading.Thread(target=srv.serve_forever, daemon=True).start()

def T(**o):   # respuesta válida del tutor
    d = {"mensaje": "Vamos paso a paso. ¿Qué ocurre con la insulina?", "pregunta_siguiente": "¿Qué ocurre con la insulina?", "aclaracion_transcripcion": False,
         "evaluacion": {"nivel": 2, "justificacion": "Parcial", "criterios": [{"id": "c1", "estado": "parcial"}]}, "conceptos_correctos": ["La glucosa está elevada"],
         "errores": [], "errores_corregidos": [], "omisiones": ["Falta la cetogénesis"], "pistas": [], "referencias": [], "fase": 3, "repaso": []}
    d.update(o); return d
INICIO = {"mensaje": "Vamos a comprobar si comprendes la cetoacidosis diabética. Explícame con tus palabras por qué se produce la acidosis metabólica.", "objetivo": "Mecanismo de la acidosis en la CAD",
          "criterios": [{"descripcion": "Déficit de insulina"}, {"descripcion": "Lipólisis y cetogénesis"}, {"descripcion": "Acidosis con anión gap elevado"}]}
LARGA = "La falta de insulina activa la lipólisis y el hígado produce cuerpos cetónicos, que son ácidos y consumen bicarbonato. Además la glucosa alta causa diuresis osmótica."

tmp = tempfile.mkdtemp(); procs = []
try:
    for f in ("cuenta.php", "api.php", "flashcards_lib.php", "guias_lib.php", "feynman.php", "feynman_lib.php"): shutil.copy(os.path.join(RAIZ, f), tmp)
    shutil.copytree(os.path.join(RAIZ, "bancos"), tmp + "/bancos")
    os.makedirs(tmp + "/guias"); open(tmp + "/guias/indice.json", "w").write('{"docs":[],"fragmentos":[]}'); open(tmp + "/guias/comparaciones.json", "w").write("[]")
    def servidor(**extra):
        pp = puerto(); t = tempfile.mkdtemp(dir=tmp)
        env = dict(os.environ, AI_PROVIDER="openai", AI_BASE_URL=f"http://127.0.0.1:{pia}/v1", MQP_ADMIN_TOKEN="token-de-prueba-largo-123", TMPDIR=t, FEYNMAN_LIMITE_MINUTO="100", PHP_CLI_SERVER_WORKERS="4"); env.update(extra)
        if "AI_API_KEY" not in extra: env["AI_API_KEY"] = "k"
        if extra.get("AI_API_KEY") == "": env.pop("AI_API_KEY")
        procs.append(subprocess.Popen(["php", "-S", f"127.0.0.1:{pp}", "-t", tmp], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)); return f"http://127.0.0.1:{pp}"
    base = servidor(); base_lim = servidor(FEYNMAN_LIMITE_MINUTO="3"); base_sinia = servidor(AI_API_KEY="")
    time.sleep(1.2)

    def cliente(b=None):
        cj = http.cookiejar.CookieJar(); op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); b = b or base
        def llamar(ruta, datos=None, cab=None, origen=True):
            h = {"Content-Type": "application/json", "X-MQP": "1"}
            if origen: h["Origin"] = b
            h.update(cab or {})
            req = urllib.request.Request(b + ruta, data=None if datos is None else json.dumps(datos).encode(), headers=h)
            try:
                r = op.open(req); return r.status, json.loads(r.read() or b"{}")
            except urllib.error.HTTPError as e:
                try: return e.code, json.loads(e.read() or b"{}")
                except Exception: return e.code, {}
        llamar.cj = cj; llamar.base = b
        return llamar
    def registrar(c, n, dueno=True):
        s, j = c("/cuenta.php?a=registro", {"nombre": "Usuario " + n, "correo": f"{n}@prueba.pe", "clave": "clave12345", "acepto": True}); ok(s == 201, "registro " + n)
        if dueno: ok(c("/cuenta.php?a=dueno_activar", {"token": "token-de-prueba-largo-123"})[0] == 200, "plan de dueño " + n)
    A, B, SINPLAN, ANON = cliente(), cliente(), cliente(), cliente()
    registrar(A, "a"); registrar(B, "b"); registrar(SINPLAN, "sp", dueno=False)
    rid = lambda: "r" + os.urandom(8).hex()

    # ---- estado público y acceso
    s, j = ANON("/feynman.php?a=estado"); ok(s == 200 and j["ia_lista"] and len(j["especialidades"]) == 17 and len(j["rubrica"]) == 4 and "AI_API_KEY" not in json.dumps(j) and '"k"' not in json.dumps(j), "estado: IA lista, 17 especialidades, rúbrica de 4 niveles, sin secretos")
    for ruta, d in (("/feynman.php?a=listar", None), ("/feynman.php?a=ver&id=" + "a" * 24, None), ("/feynman.php?a=crear", {"origen": "tema", "tema": "cetoacidosis"}), ("/feynman.php?a=turno", {}), ("/feynman.php?a=finalizar", {}), ("/feynman.php?a=borrar", {})):
        s, _ = ANON(ruta, d); ok(s == 401, f"sin sesión {ruta} → 401 (fue {s})")
    s, _ = SINPLAN("/feynman.php?a=crear", {"origen": "tema", "tema": "cetoacidosis"}); ok(s == 402, "sin plan activo → 402")
    s, _ = A("/feynman.php?a=crear", {"origen": "tema", "tema": "cetoacidosis"}, cab={"X-MQP": "0"}); ok(s == 403, "POST sin cabecera X-MQP → 403")
    s, _ = A("/feynman.php?a=crear", {"origen": "tema", "tema": "cetoacidosis"}, cab={"Origin": "http://otro-sitio.example"}); ok(s == 403, "POST desde otro origen → 403")
    n0 = len(pedidos)

    # ---- crear desde una pregunta ENAM real
    s, j = A("/feynman.php?a=crear", {"origen": "pregunta", "pregunta_id": "NO-EXISTE-1"}); ok(s == 404, "pregunta inexistente → 404"); 
    s, j = A("/feynman.php?a=crear", {"origen": "tema", "tema": "ab"}); ok(s == 400, "tema demasiado corto")
    ok(len(pedidos) == n0, "las entradas inválidas no cuestan llamadas a la IA")
    cola.append(INICIO)
    s, j = A("/feynman.php?a=crear", {"origen": "pregunta", "pregunta_id": "END-001", "elegida": "A", "tema": "Cetoacidosis diabética", "flujograma": "cetoacidosis.svg"})
    ok(s == 201 and j["sesion"]["fase"] == 1 and j["sesion"]["estado"] == "activa" and j["sesion"]["pregunta_id"] == "END-001" and j["sesion"]["elegida"] == "A", "sesión creada desde END-001")
    sid = j["sesion"]["id"]; ok(len(j["turnos"]) == 1 and j["turnos"][0]["rol"] == "tutor" and len(j["panel"]["criterios"]) == 3, "primer turno del tutor y 3 criterios de la rúbrica")
    prompt = json.dumps(pedidos[-1], ensure_ascii=False)
    ok("Mujer de 19 años con diabetes tipo 1" in prompt and "Correcta según el banco: C" in prompt and "Alternativa que marcó el estudiante: A" in prompt and "Bolo de insulina rápida" in prompt, "la IA recibe el contexto REAL de la pregunta (enunciado, alternativas, clave, elegida)")
    ok("a@prueba.pe" not in prompt and "Usuario a" not in prompt and "clave12345" not in prompt, "no se envía información personal al proveedor")
    s, j2 = A("/feynman.php?a=crear", {"origen": "pregunta", "pregunta_id": "END-001"}); ok(s == 200 and j2.get("retomada") and j2["sesion"]["id"] == sid and len(pedidos) == n0 + 1, "misma pregunta → retoma la sesión, sin gastar IA")

    # ---- turno por texto: error conceptual → fase 3
    cola.append(T(errores=[{"descripcion": "Dice que la glucosa vuelve ácida la sangre", "correccion": "La acidosis la causan los cuerpos cetónicos"}]))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": "La glucosa elevada vuelve ácida la sangre y por eso hay acidosis en la cetoacidosis diabética.", "via": "texto"})
    ok(s == 200 and j["sesion"]["fase"] == 3 and j["panel"]["errores"] == [{"descripcion": "Dice que la glucosa vuelve ácida la sangre", "estado": "abierto"}], "error conceptual detectado → fase 3 con el error abierto")
    ok([t["rol"] for t in j["turnos"]] == ["tutor", "estudiante", "tutor"] and j["turnos"][1]["nivel"] == 2, "se guardan los turnos y el nivel (2) de la intervención")
    ok(j["panel"]["conceptos_correctos"] == ["La glucosa está elevada"] and j["panel"]["nivel_inicial"] == 2, "panel con datos reales de la sesión")

    # ---- formato inválido, error de IA y transición inadmisible: no guardan nada ni bloquean
    n = len(j["turnos"]); a0 = len(pedidos)
    cola.extend(["esto no es JSON", {"mensaje": "falta casi todo"}])
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA}); ok(s == 502 and "SECRETO" not in json.dumps(j) and "JSON" not in json.dumps(j), "formato inválido tras reintento → 502 sin datos técnicos")
    ok(len(pedidos) - a0 == 2, "un solo reintento (no se gasta IA en bucle)")
    s, v = A(f"/feynman.php?a=ver&id={sid}"); ok(len(v["turnos"]) == n, "ningún turno a medias tras el fallo")
    cola.append(("http", 500)); s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA}); ok(s == 502 and "SECRETO" not in json.dumps(j), "error del proveedor → 502 sin filtrar su detalle")
    cola.extend([T(fase=5), T(fase=5)]); s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA}); ok(s == 502, "el modelo no puede saltarse a la fase 5")
    s, v = A(f"/feynman.php?a=ver&id={sid}"); ok(v["sesion"]["fase"] == 3, "la fase no cambió")
    cola.extend(["basura", T(fase=3, mensaje="Reintento correcto: ¿qué le pasa a la lipólisis sin insulina?")])
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": "No sé muy bien, pero creo que sin insulina se rompen las grasas."}); ok(s == 200 and "Reintento correcto" in j["turnos"][-1]["texto"], "formato inválido y luego válido → se recupera con el reintento")

    # ---- pista adaptada y escalones
    cola.append(T(fase=3, mensaje="Pista: piensa en qué hace la insulina sobre el tejido adiposo.", evaluacion={"nivel": None, "justificacion": "", "criterios": []}))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "pista"}); ok(s == 200 and j["sesion"]["ayuda"] == 2 and "Pista" in j["turnos"][-1]["texto"], "pista: sube un escalón respecto al que ya pedía el progreso (sin avance → 1; pista → 2)")
    ok("PISTA" in json.dumps(pedidos[-1]) and "escalón 2" in json.dumps(pedidos[-1], ensure_ascii=False), "la IA recibe el escalón de ayuda fijado por el servidor")
    ok(j["panel"]["nivel_actual"] == 2, "una pista no cambia la evaluación")

    # ---- duplicados: mismo req_id no se procesa dos veces; dos envíos simultáneos → uno solo
    req = rid(); cola.append(T(fase=3, mensaje="Respuesta única"))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": req, "accion": "responder", "texto": LARGA}); a1 = len(pedidos)
    s2, j2 = A("/feynman.php?a=turno", {"id": sid, "req_id": req, "accion": "responder", "texto": LARGA}); ok(s2 == 200 and j2.get("repetida") and len(pedidos) == a1 and len(j2["turnos"]) == len(j["turnos"]), "mismo req_id: no se repite ni la IA ni los turnos")
    cola.extend([T(fase=3, mensaje="Lenta 1", _demora=1.5), T(fase=3, mensaje="No debería usarse")]); res = {}
    def envio(k): res[k] = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA + " " + k})
    ths = [threading.Thread(target=envio, args=("x",)), threading.Thread(target=envio, args=("y",))]; ths[0].start(); time.sleep(0.4); ths[1].start(); [t.join() for t in ths]
    ok(sorted(r[0] for r in res.values()) == [200, 409], f"dos envíos simultáneos: uno se procesa y el otro recibe 409 (fue {[r[0] for r in res.values()]})")
    cola.clear()
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "pista"}); ok(s in (200, 409) and s != 500, "el bloqueo se libera tras el envío simultáneo")

    # ---- entradas inválidas
    s, _ = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": "x" * 1501}); ok(s == 413, "intervención de más de 1500 caracteres → 413")
    s, _ = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": " "}); ok(s == 400, "intervención vacía → 400")
    s, _ = A("/feynman.php?a=turno", {"id": sid, "req_id": "corto", "accion": "responder", "texto": LARGA}); ok(s == 400, "req_id inválido → 400")
    s, _ = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "borrar_todo", "texto": LARGA}); ok(s == 400, "acción desconocida → 400")

    # ---- aclaración por voz: no consume intentos ni registra errores
    s, v = A(f"/feynman.php?a=ver&id={sid}"); intentos0 = v["panel"]["intentos"]["socratico"]; errores0 = len(v["panel"]["errores"])
    cola.append(T(fase=3, aclaracion_transcripcion=True, mensaje="Entendí «acidosis», pero ¿dijiste «metabólica» o «respiratoria»?", errores=[{"descripcion": "falso error", "correccion": "x"}], evaluacion={"nivel": 1, "justificacion": "", "criterios": []}))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": "Es una acidosis, por la... cetonas", "via": "voz"})
    ok(s == 200 and j["turnos"][-1]["aclaracion"] and j["panel"]["intentos"]["socratico"] == intentos0 and len(j["panel"]["errores"]) == errores0, "término ambiguo por voz: pide aclaración sin penalizar")
    ok("RECONOCIMIENTO DE VOZ" in json.dumps(pedidos[-1], ensure_ascii=False), "la IA sabe que la intervención viene de voz")

    # ---- el estudiante corrige: 3 → 4 → 5 (decide el servidor)
    cola.append(T(fase=4, mensaje="Exacto. Reconstruyamos: sin insulina… ¿Puedes explicarlo de nuevo?", evaluacion={"nivel": 3, "justificacion": "Corrigió", "criterios": [{"id": "c1", "estado": "cumplido"}, {"id": "c2", "estado": "cumplido"}]}, errores_corregidos=[1], omisiones=["Anión gap"]))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA}); ok(s == 200 and j["sesion"]["fase"] == 4 and j["panel"]["errores"][0]["estado"] == "corregido", "el estudiante corrige su explicación → error corregido, fase 4")
    cola.append(T(fase=5, mensaje="Muy bien. Caso nuevo: paciente con DM1, náuseas, respiración profunda y cetonemia. ¿Qué mecanismo explica la alteración ácido-base?", pregunta_siguiente="¿Qué mecanismo explica la alteración ácido-base?", evaluacion={"nivel": 3, "justificacion": "Correcta", "criterios": []}, omisiones=[]))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA + " Resumiendo: sin insulina hay cetogénesis y acidosis con anión gap alto."}); ok(s == 200 and j["sesion"]["fase"] == 5 and not j["sesion"]["puede_finalizar"], "pregunta de transferencia presentada (fase 5), aún no se puede finalizar")
    ok("DM1" in j["turnos"][-1]["texto"], "el caso de aplicación es nuevo")
    # finalizar antes de resolver el caso → incompleta (lo decide el servidor), con informe honesto; y se puede retomar
    cola.append({"resumen": "Aún falta aplicar el mecanismo.", "proximos_pasos": ["Resolver el caso"], "tarjetas": []})
    s, v = A("/feynman.php?a=finalizar", {"id": sid})
    ok(s == 200 and v["sesion"]["estado"] == "incompleta" and v["informe"]["completa"] is False and v["informe"]["aviso"] and v["informe"]["dominio"] != "dominado", "terminar sin resolver el caso → incompleta, con aviso y sin dominio")
    ok(v["informe"]["errores_corregidos"][0]["descripcion"].startswith("Dice que la glucosa") and v["informe"]["resumen"] == "Aún falta aplicar el mecanismo.", "el informe lista el error corregido real y el resumen de la IA")
    ok(A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "pista"})[0] == 409, "una sesión incompleta no recibe turnos hasta retomarla")
    s, j = A("/feynman.php?a=reanudar", {"id": sid}); ok(s == 200 and j["sesion"]["estado"] == "activa" and j["sesion"]["fase"] == 5, "retomar la sesión incompleta")

    # ---- resolver el caso → finalizar → informe, tarjetas propuestas (no guardadas)
    cola.append(T(fase=5, mensaje="Excelente: aplicaste el mecanismo.", evaluacion={"nivel": 4, "justificacion": "Aplicó el mecanismo al caso", "criterios": [{"id": "c3", "estado": "cumplido"}]}, omisiones=[]))
    s, j = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": "El déficit de insulina lleva a lipólisis y cetogénesis; los cetoácidos consumen bicarbonato y generan acidosis con anión gap elevado; la respiración de Kussmaul compensa."})
    ok(s == 200 and j["sesion"]["puede_finalizar"] and j["panel"]["nivel_transferencia"] == 4, "caso resuelto con nivel 4 → ya se puede finalizar")
    cola.append({"resumen": "Corregiste el origen de la acidosis y la aplicaste a un caso nuevo.", "proximos_pasos": ["Repasar el anión gap"], "tarjetas": [{"frente": "¿Por qué el déficit de insulina favorece la cetogénesis?", "dorso": "Sin insulina aumenta la lipólisis y el hígado produce cuerpos cetónicos.", "citas": []}]})
    s, j = A("/feynman.php?a=finalizar", {"id": sid})
    inf = j["informe"]; ok(s == 200 and j["sesion"]["estado"] == "completada" and inf["completa"] and inf["dominio"] == "dominado" and inf["aplicacion"]["nivel"] == 4 and inf["aplicacion"]["valoracion"] == "Comprensión sólida", "informe: completada, dominado, aplicación nivel 4")
    ok(inf["niveles"]["inicial"] == 2 and inf["niveles"]["reconstruccion"] == 3 and inf["comprendido"] == ["La glucosa está elevada"], "informe coherente con las respuestas reales (niveles y conceptos)")
    ok(len(inf["tarjetas"]) == 1 and inf["tarjetas"][0]["estado"] == "propuesta" and "generada por IA" in inf["tarjetas"][0]["fuente"], "tarjeta propuesta y marcada como generada por IA")
    s, fc = A("/cuenta.php?a=fc_listar"); ok(fc["tarjetas"] == [], "las tarjetas NO se guardaron solas en las colecciones del estudiante")
    s, _ = A("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "responder", "texto": LARGA}); ok(s == 409, "una sesión terminada no acepta más intervenciones")
    # el estudiante revisa/edita y recién entonces guarda por el sistema de flashcards existente
    t0 = inf["tarjetas"][0]
    s, r = A("/cuenta.php?a=fc_crear", {"tarjetas": [{"frente": t0["frente"] + " (editada)", "dorso": t0["dorso"], "pregunta": "END-001", "fuente": t0["fuente"]}]}); ok(s == 201 and r["creadas"] == 1, "la tarjeta revisada se guarda con el sistema de flashcards existente")
    s, j = A("/feynman.php?a=tarjetas", {"id": sid, "decisiones": [{"i": 0, "estado": "guardada"}, {"i": 5, "estado": "guardada"}, {"i": 0, "estado": "hackeada"}]}); ok(s == 200 and j["informe"]["tarjetas"][0]["estado"] == "guardada", "se registra la decisión (y se ignoran las inválidas)")

    # ---- otro caso de aplicación
    cola.append(T(fase=5, mensaje="Nuevo caso: gestante con DM1 y vómitos…", pregunta_siguiente="¿Qué haces primero?", evaluacion={"nivel": None, "justificacion": "", "criterios": []}))
    s, j = A("/feynman.php?a=otro_caso", {"id": sid, "req_id": rid()}); ok(s == 200 and j["sesion"]["estado"] == "activa" and j["sesion"]["fase"] == 5 and not j["sesion"]["puede_finalizar"] and "gestante" in j["turnos"][-1]["texto"], "practicar con otro caso reabre la fase 5 con un caso nuevo")

    # ---- aislamiento entre estudiantes
    for ruta, d in ((f"/feynman.php?a=ver&id={sid}", None), ("/feynman.php?a=turno", {"id": sid, "req_id": rid(), "accion": "pista"}), ("/feynman.php?a=finalizar", {"id": sid}), ("/feynman.php?a=borrar", {"id": sid}),
                    ("/feynman.php?a=tarjetas", {"id": sid, "decisiones": []}), ("/feynman.php?a=reanudar", {"id": sid}), ("/feynman.php?a=otro_caso", {"id": sid, "req_id": rid()})):
        s, _ = B(ruta, d); ok(s == 404, f"B no puede acceder a la sesión de A ({ruta.split('=')[1].split('&')[0]}) → 404 (fue {s})")
    s, j = B("/feynman.php?a=listar"); ok(j["sesiones"] == [], "B no ve las sesiones de A")
    s, j = A("/feynman.php?a=listar"); ok(len(j["sesiones"]) == 1 and j["sesiones"][0]["id"] == sid, "A ve la suya")
    s, v = A(f"/feynman.php?a=ver&id={sid}"); ok(s == 200, "A sigue viendo su sesión")

    # ---- crear desde un flujograma y desde un tema libre; explicación directa
    cola.append(INICIO); s, j = A("/feynman.php?a=crear", {"origen": "flujograma", "pregunta_id": "GIN-001", "flujograma": "algo.svg", "tema": "Preeclampsia"}); ok(s == 201 and j["sesion"]["origen"] == "flujograma" and j["sesion"]["flujograma"] == "algo.svg" and j["sesion"]["pregunta_id"] == "GIN-001", "sesión desde un flujograma, vinculada a su pregunta")
    sid2 = j["sesion"]["id"]
    cola.append(INICIO); s, j = B("/feynman.php?a=crear", {"origen": "tema", "tema": "Cetoacidosis diabética", "especialidad": "Endocrinología"}); ok(s == 201 and j["sesion"]["origen"] == "tema" and j["sesion"]["pregunta_id"] == "", "sesión desde un tema libre")
    sid3 = j["sesion"]["id"]; ok("Origen de la sesión: tema" in json.dumps(pedidos[-1], ensure_ascii=False) and "Pregunta del banco" not in json.dumps(pedidos[-1], ensure_ascii=False), "sin pregunta de origen no se inventa contexto")
    cola.append(T(fase=4, mensaje="Te lo explico: sin insulina… Ahora explícalo tú.", evaluacion={"nivel": None, "justificacion": "", "criterios": []}))
    s, j = A("/feynman.php?a=turno", {"id": sid2, "req_id": rid(), "accion": "explicacion"}); ok(s == 200 and j["sesion"]["fase"] == 4 and j["informe" if False else "panel"]["nivel_actual"] is None, "explicación directa a petición: pasa a la fase 4 sin evaluar")
    cola.append(T(fase=3, evaluacion={"nivel": None, "justificacion": "", "criterios": []}))
    cola.append(T(fase=3, evaluacion={"nivel": None, "justificacion": "", "criterios": []}))
    s, j = A("/feynman.php?a=turno", {"id": sid2, "req_id": rid(), "accion": "pista"}); ok(s == 502, "durante la explicación directa el modelo no puede volver atrás de fase")

    # ---- borrado
    s, _ = A("/feynman.php?a=borrar", {"id": sid2}); ok(s == 200, "borrar sesión")
    s, _ = A(f"/feynman.php?a=ver&id={sid2}"); ok(s == 404, "sesión borrada ya no existe")
    db = sqlite3.connect(tmp + "/cuenta_datos/mqp.sqlite"); ok(db.execute("select count(*) from feynman_turnos where sesion=?", (sid2,)).fetchone()[0] == 0, "borrar la sesión borra sus turnos (cascada)")

    # ---- límites de consumo
    L = cliente(base_lim); registrar(L, "l"); cola.extend([INICIO, T(fase=3), T(fase=3)])
    s, j = L("/feynman.php?a=crear", {"origen": "tema", "tema": "Cetoacidosis"}); idl = j["sesion"]["id"]
    ok(L("/feynman.php?a=turno", {"id": idl, "req_id": rid(), "accion": "responder", "texto": LARGA})[0] == 200, "límite: 2.ª llamada")
    ok(L("/feynman.php?a=turno", {"id": idl, "req_id": rid(), "accion": "responder", "texto": LARGA})[0] == 200, "límite: 3.ª llamada")
    a1 = len(pedidos); s, j = L("/feynman.php?a=turno", {"id": idl, "req_id": rid(), "accion": "responder", "texto": LARGA}); ok(s == 429 and len(pedidos) == a1, "límite por minuto → 429 sin llamar a la IA")

    # ---- sin llave de IA: estado honesto, sin respuestas estáticas
    Z = cliente(base_sinia); registrar(Z, "z")
    s, j = Z("/feynman.php?a=estado"); ok(j["ia_lista"] is False, "estado: IA no configurada")
    a1 = len(pedidos); s, j = Z("/feynman.php?a=crear", {"origen": "tema", "tema": "Cetoacidosis"}); ok(s == 503 and "no está configurado" in j["error"] and len(pedidos) == a1, "sin llave: 503 honesto, no se simula la IA")
    s, j = Z("/feynman.php?a=listar"); ok(j["sesiones"] == [], "sin llave no se crea ninguna sesión")

    # ---- «Descargar mis datos» incluye las sesiones del propio estudiante (y solo las suyas)
    s, ex = A("/cuenta.php?a=exportar", {}); ok(s == 200 and len(ex["feynman"]) == 1 and ex["feynman"][0]["id"] == sid and len(ex["feynman"][0]["turnos"]) >= 5 and "datos" not in ex["feynman"][0], "la exportación de datos incluye las sesiones y transcripciones propias")
    # ---- eliminar la cuenta borra sus sesiones (privacidad)
    ok(db.execute("select count(*) from feynman_sesiones where usuario=(select id from usuarios where correo='b@prueba.pe')").fetchone()[0] == 1, "B tiene una sesión")
    s, _ = B("/cuenta.php?a=eliminar", {"clave": "clave12345"}); ok(s == 200, "B elimina su cuenta")
    db.close(); db = sqlite3.connect(tmp + "/cuenta_datos/mqp.sqlite")
    ok(db.execute("select count(*) from feynman_sesiones where id=?", (sid3,)).fetchone()[0] == 0, "al eliminar la cuenta se borran sus sesiones Feynman")
    ok(db.execute("select count(*) from feynman_sesiones where id=?", (sid,)).fetchone()[0] == 1, "…y no las de otros")
finally:
    for p in procs: p.terminate()
    shutil.rmtree(tmp, ignore_errors=True)
print(f"{fallos} fallos de {total}" if fallos else f"OK: {total} comprobaciones de la API del Tutor Feynman IA"); sys.exit(1 if fallos else 0)
