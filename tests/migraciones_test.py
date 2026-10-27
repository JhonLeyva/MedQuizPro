#!/usr/bin/env python3
"""python3 tests/migraciones_test.py — crea el esquema con cuenta.php, y comprueba que cada migración .down/.up sea reversible y no rompa datos ajenos."""
import os, shutil, sqlite3, subprocess, sys, tempfile
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); fallos = 0
def ok(c, m):
    global fallos
    if not c: fallos += 1; print("FALLA:", m)
tmp = tempfile.mkdtemp()
try:
    for f in ("cuenta.php", "flashcards_lib.php"): shutil.copy(os.path.join(RAIZ, f), tmp)
    import socket, time, urllib.request, json
    s_ = socket.socket(); s_.bind(("127.0.0.1", 0)); pp = s_.getsockname()[1]; s_.close()
    proc = subprocess.Popen(["php", "-S", f"127.0.0.1:{pp}", "-t", tmp], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    try:       # un registro de prueba obliga a la aplicación a crear todo el esquema
        urllib.request.urlopen(urllib.request.Request(f"http://127.0.0.1:{pp}/cuenta.php?a=registro", data=json.dumps({"nombre": "Mig", "correo": "m@m.pe", "clave": "clave12345", "acepto": True}).encode(),
                               headers={"Content-Type": "application/json", "X-MQP": "1", "Origin": f"http://127.0.0.1:{pp}"}))
    finally: proc.terminate(); proc.wait(timeout=5)
    ruta = tmp + "/cuenta_datos/mqp.sqlite"; ok(os.path.isfile(ruta), "cuenta.php crea la base")
    db = sqlite3.connect(ruta); db.execute("PRAGMA foreign_keys=ON")
    tablas = lambda: {r[0] for r in db.execute("select name from sqlite_master where type='table'")}
    ok({"flashcards", "repasos", "ritmo", "usuarios", "progreso"} <= tablas(), "esquema completo creado por la aplicación")
    db.execute("delete from usuarios"); db.execute("insert into usuarios(id,correo,nombre,clave,creado) values(1,'a@a','A','x',1)")
    db.execute("insert into flashcards(usuario,frente,dorso,huella,creado,proximo) values(1,'f','d','h',1,1)"); db.commit()
    sql = lambda n: open(f"{RAIZ}/migraciones/{n}.sql", encoding="utf-8").read()
    db.executescript(sql("001_flashcards.down")); ok("flashcards" not in tablas() and "repasos" not in tablas(), "001.down quita las tablas")
    ok(db.execute("select count(*) from usuarios").fetchone()[0] == 1, "001.down no toca a los usuarios")
    db.executescript(sql("001_flashcards.up")); db.executescript(sql("001_flashcards.up")); ok("flashcards" in tablas() and "repasos" in tablas(), "001.up recrea las tablas (y es repetible)")
    db.executescript(sql("002_ritmo.down")); ok("ritmo" not in tablas(), "002.down"); db.executescript(sql("002_ritmo.up")); ok("ritmo" in tablas(), "002.up")
    if sqlite3.sqlite_version_info >= (3, 35, 0):
        db.executescript(sql("003_dueno.down")); ok("dueno" not in [r[1] for r in db.execute("pragma table_info(usuarios)")], "003.down quita la columna")
        db.executescript(sql("003_dueno.up")); ok("dueno" in [r[1] for r in db.execute("pragma table_info(usuarios)")], "003.up la devuelve")
    db.executescript(sql("004_feynman.up")); db.executescript(sql("004_feynman.up")); ok({"feynman_sesiones", "feynman_turnos", "feynman_uso"} <= tablas(), "004.up crea las tablas del Tutor Feynman (y es repetible)")
    db.execute("insert into feynman_sesiones(id,usuario,origen,tema,datos,creado,actualizado) values('s1',1,'tema','t','{}',1,1)"); db.execute("insert into feynman_turnos(sesion,n,rol,texto,fase,creado) values('s1',1,'tutor','hola',1,1)"); db.commit()
    db.executescript(sql("004_feynman.down")); ok("feynman_sesiones" not in tablas() and "feynman_turnos" not in tablas(), "004.down quita las tablas"); ok(db.execute("select count(*) from usuarios").fetchone()[0] == 1, "004.down no toca a los usuarios")
    db.executescript(sql("004_feynman.up")); db.execute("insert into feynman_sesiones(id,usuario,origen,tema,datos,creado,actualizado) values('s2',1,'tema','t','{}',1,1)"); db.execute("insert into feynman_turnos(sesion,n,rol,texto,fase,creado) values('s2',1,'tutor','hola',1,1)"); db.commit()
    ok("intentos" in tablas(), "cuenta.php ya tiene su tabla «intentos» (limite de inicios de sesión): la nueva se llama intentos_respuesta")
    db.executescript(sql("005_intentos_respuesta.up")); db.executescript(sql("005_intentos_respuesta.up")); ok("intentos_respuesta" in tablas() and "intentos" in tablas(), "005.up crea intentos_respuesta (repetible) sin tocar «intentos»")
    db.execute("insert into intentos_respuesta(usuario,pregunta,elegida,correcta,etiqueta,t) values(1,'END-001','A',0,'refuerzo',1)"); db.commit()
    db.executescript(sql("005_intentos_respuesta.down")); ok("intentos_respuesta" not in tablas() and "intentos" in tablas(), "005.down quita solo su tabla"); db.executescript(sql("005_intentos_respuesta.up"))
    db.execute("insert into intentos_respuesta(usuario,pregunta,elegida,correcta,etiqueta,t) values(1,'END-001','A',0,'refuerzo',1)"); db.commit()
    db.execute("insert into flashcards(usuario,frente,dorso,huella,creado,proximo) values(1,'f','d','h2',1,1)"); db.execute("delete from usuarios where id=1"); db.commit()
    ok(db.execute("select count(*) from intentos_respuesta").fetchone()[0] == 0, "borrar la cuenta borra sus intentos con confianza (ON DELETE CASCADE)")
    ok(db.execute("select count(*) from feynman_sesiones").fetchone()[0] == 0 and db.execute("select count(*) from feynman_turnos").fetchone()[0] == 0, "borrar la cuenta borra sus sesiones y turnos Feynman (ON DELETE CASCADE)")
    ok(db.execute("select count(*) from flashcards").fetchone()[0] == 0, "borrar la cuenta borra sus tarjetas (ON DELETE CASCADE)")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
print(f"{fallos} fallos" if fallos else "OK: migraciones reversibles"); sys.exit(1 if fallos else 0)
