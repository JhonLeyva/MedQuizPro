// node tests/acceso_test.js — acceso cerrado: solo el dueño y quien tenga un plan activo ven los contenidos; sin config abierta todo sigue igual.
// Usa php -S con tests/router_acceso.php (imita las reglas de .htaccess; el .htaccess real no se puede probar aquí).
"use strict";
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net"), { spawn, spawnSync } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
const TOKEN = "clave-de-dueno-muy-larga-123";
function preparar(cerrado) {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "acc-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  for (const d of ["bancos", "guardia", "serums", "consulta"]) fs.cpSync(path.join(RAIZ, d), path.join(tmp, d), { recursive: true });
  fs.copyFileSync(path.join(RAIZ, "Banco_ENAM_Respuestas_Resaltadas.pdf"), path.join(tmp, "Banco_ENAM_Respuestas_Resaltadas.pdf"));
  fs.writeFileSync(path.join(tmp, "config.php"), "<?php return ['cerrado' => '" + (cerrado ? "1" : "0") + "', 'admin_token' => '" + TOKEN + "'];");
  fs.mkdirSync(path.join(tmp, "t")); return tmp;
}
async function servidor(cerrado) {
  const tmp = preparar(cerrado), puerto = await libre();
  const php = spawn("php", ["-S", `127.0.0.1:${puerto}`, "-t", tmp, path.join(tmp, "tests_router.php")], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } });
  fs.copyFileSync(path.join(RAIZ, "tests/router_acceso.php"), path.join(tmp, "tests_router.php")); await dormir(1300);
  return { tmp, php, base: `http://127.0.0.1:${puerto}/` };
}
function cliente(base) {
  let cookie = "";
  const pedir = async (ruta, o = {}) => { const r = await fetch(base + ruta, { redirect: "manual", ...o, headers: { ...(o.headers || {}), ...(cookie ? { cookie } : {}) } }); const sc = r.headers.get("set-cookie"); if (sc) cookie = sc.split(";")[0]; return r; };
  const post = (ruta, cuerpo) => pedir(ruta, { method: "POST", headers: { "Content-Type": "application/json", "X-MQP": "1" }, body: JSON.stringify(cuerpo) });
  return { pedir, post, sinSesion: () => { cookie = ""; } };
}
const bd = (tmp, sql) => spawnSync("php", ["-r", `$p = new PDO('sqlite:${tmp}/cuenta_datos/mqp.sqlite'); ${sql}`]);

(async () => {
  const orig = fs.readFileSync(path.join(RAIZ, "bancos/cardiologia.json"));
  const C = await servidor(true), O = await servidor(false);
  try {
    /* ---- acceso cerrado ---- */
    const a = cliente(C.base);
    let r = await a.pedir("bancos/cardiologia.json"); ok(r.status === 401 && (await r.json()).acceso === "sin_sesion", "cerrado: sin sesión → 401 y no entrega las preguntas");
    for (const f of ["guardia_casos.js", "serums_casos.js", "consulta_casos.js", "Banco_ENAM_Respuestas_Resaltadas.pdf", "serums/indice.json", "guardia/casos/" + fs.readdirSync(path.join(RAIZ, "guardia/casos"))[0]]) { r = await a.pedir(f); ok(r.status === 401, "cerrado: sin sesión no se entrega " + f + " (" + r.status + ")"); }
    r = await a.pedir("cuenta.php?a=estado"); const est = await r.json(); ok(est.cerrado === true, "estado informa que el acceso está cerrado");
    r = await a.post("cuenta.php?a=registro", { nombre: "Estudiante Uno", correo: "uno@ejemplo.com", clave: "clave-segura-1", acepto: true, examen: "enam" }); ok(r.status === 200 || r.status === 201, "cualquiera puede registrarse (" + r.status + ")");
    r = await a.pedir("bancos/cardiologia.json"); ok(r.status === 402 && (await r.json()).acceso === "sin_plan", "registrado sin plan → 402");
    r = await a.pedir("serums_casos.js"); ok(r.status === 402, "registrado sin plan no ve los casos");
    /* plan activo (lo que hace el webhook de pago): se escribe en la base como lo haría cuenta.php */
    const id = (await (await a.pedir("cuenta.php?a=me")).json()).usuario.id;
    bd(C.tmp, `$p->exec("INSERT INTO suscripciones(usuario, examen, plan, hasta) VALUES (${id}, 'enam', 'mensual', " . (time() + 86400) . ")");`);
    r = await a.pedir("bancos/cardiologia.json"); const cuerpo = Buffer.from(await r.arrayBuffer()); ok(r.status === 200 && cuerpo.equals(orig) && /application\/json/.test(r.headers.get("content-type")), "con plan activo se entrega el archivo idéntico");
    const et = r.headers.get("etag"); r = await a.pedir("bancos/cardiologia.json", { headers: { "If-None-Match": et } }); ok(r.status === 304, "con plan activo responde 304 si no cambió"); ok(/private/.test((await a.pedir("bancos/cardiologia.json")).headers.get("cache-control")), "cerrado: la caché es privada");
    bd(C.tmp, `$p->exec("UPDATE suscripciones SET hasta = " . (time() - 5) . " WHERE usuario = ${id}");`);
    r = await a.pedir("bancos/cardiologia.json"); ok(r.status === 402, "plan vencido → 402");
    /* dueño */
    const d = cliente(C.base); await d.post("cuenta.php?a=registro", { nombre: "La Dueña", correo: "duena@ejemplo.com", clave: "clave-segura-2", acepto: true });
    r = await d.pedir("bancos/cardiologia.json"); ok(r.status === 402, "la cuenta del dueño aún no activada es una cuenta más");
    r = await d.post("cuenta.php?a=dueno_activar", { token: TOKEN }); ok(r.status === 200, "el dueño activa su cuenta con su clave");
    r = await d.pedir("bancos/cardiologia.json"); ok(r.status === 200 && Buffer.from(await r.arrayBuffer()).equals(orig), "el dueño entra a todo");
    r = await d.pedir("serums/audio/tormenta.mp3"); ok(r.status === 200 && /audio\/mpeg/.test(r.headers.get("content-type")), "el dueño recibe el audio");
    r = await d.pedir("Banco_ENAM_Respuestas_Resaltadas.pdf"); ok(r.status === 200 && /pdf/.test(r.headers.get("content-type")), "el dueño recibe los PDF");
    /* la sesión cerrada vuelve a bloquear */
    d.sinSesion(); r = await d.pedir("bancos/cardiologia.json"); ok(r.status === 401, "sin la cookie vuelve a bloquear");
    /* una cookie inventada no sirve */
    const f = cliente(C.base); r = await fetch(C.base + "bancos/cardiologia.json", { headers: { cookie: "mqp_sid=abcdef1234567890abcdef1234567890" } }); ok(r.status === 401, "una cookie de sesión inventada no sirve");
    /* rutas peligrosas: nunca se entrega nada fuera de la lista, ni siquiera al dueño */
    for (const f of ["../config.php", "config.php", "cuenta_datos/mqp.sqlite", "bancos/../config.php", "bancos/../cuenta.php", "%2e%2e/config.php", "bancos/.htaccess", "guardia/../../etc/passwd", "app/app.js", "acceso.php", "bancos/cardiologia.json%00.php", "/etc/passwd", "bancos//cardiologia.json", "bancos\\cardiologia.json", "cuenta.php", "bancos/", "bancos"]) {
      r = await d.pedir("acceso.php?f=" + encodeURIComponent(f)); ok(r.status === 404, "ruta bloqueada: " + JSON.stringify(f) + " (" + r.status + ")"); }
    r = await d.pedir("bancos/no-existe.json"); ok(r.status === 404, "un archivo que no existe da 404");
    r = await d.pedir("cuenta.php?a=estado"); ok(r.status === 200, "cuenta.php sigue accesible para poder iniciar sesión");
    /* ---- acceso abierto (por defecto): nada cambia ---- */
    const o = cliente(O.base); r = await o.pedir("bancos/cardiologia.json"); ok(r.status === 200 && Buffer.from(await r.arrayBuffer()).equals(orig), "abierto: cualquiera ve el archivo, idéntico al original");
    r = await o.pedir("cuenta.php?a=estado"); ok((await r.json()).cerrado === false, "abierto: el estado lo indica");
    r = await o.pedir("acceso.php?f=" + encodeURIComponent("../config.php")); ok(r.status === 404, "abierto: tampoco se entrega config.php");
  } finally { C.php.kill(); O.php.kill(); fs.rmSync(C.tmp, { recursive: true, force: true }); fs.rmSync(O.tmp, { recursive: true, force: true }); }
  console.log(`acceso_test: ${total - fallos}/${total} comprobaciones correctas`); process.exit(fallos ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
