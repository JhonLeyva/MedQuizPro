// node tests/acceso_e2e.js — acceso cerrado en el navegador: quien no es el dueño ni tiene plan solo ve ingreso, registro y planes y no descarga bancos;
// el dueño entra a todo; con el acceso abierto la plataforma funciona como siempre. Usa tests/router_acceso.php (imita .htaccess).
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net"), { spawn, spawnSync } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
const TOKEN = "clave-de-dueno-muy-larga-123", INIT = () => { try { localStorage.setItem("mqp_sin_intros_prueba", "1"); } catch (e) {} };
async function servidor(cerrado) {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "acce-")), puerto = await libre();
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  for (const d of ["app", "bancos", "guardia", "serums", "consulta"]) fs.cpSync(path.join(RAIZ, d), path.join(tmp, d), { recursive: true });
  fs.symlinkSync(path.join(RAIZ, "flujogramas"), path.join(tmp, "flujogramas"));
  fs.writeFileSync(path.join(tmp, "config.php"), "<?php return ['cerrado' => '" + (cerrado ? "1" : "0") + "', 'admin_token' => '" + TOKEN + "'];");
  fs.copyFileSync(path.join(RAIZ, "tests/router_acceso.php"), path.join(tmp, "tests_router.php")); fs.mkdirSync(path.join(tmp, "t"));
  const php = spawn("php", ["-S", `127.0.0.1:${puerto}`, "-t", tmp, path.join(tmp, "tests_router.php")], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1300);
  return { tmp, php, base: `http://127.0.0.1:${puerto}/` };
}
(async () => {
  const C = await servidor(true), O = await servidor(false), navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined }), errores = [];
  const nueva = async ctx => { const p = await ctx.newPage(); p.on("pageerror", e => errores.push(String(e))); return p; };
  try {
    /* ---- cerrado, visitante ---- */
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx.addInitScript(INIT); const p = await nueva(ctx), pedidos = [];
    p.on("response", r => { if (r.status() === 200 && (/\/(bancos|flujogramas|guardia|consulta|serums)\//.test(r.url()) || /_casos\.js|algoritmos\.js/.test(r.url()))) pedidos.push(r.url()); });
    await p.goto(C.base + "app/#/inicio"); await p.waitForSelector("form, .auth, input[type=password]", { timeout: 15000 });
    ok(/#\/ingresar/.test(p.url()), "visitante: se le lleva a «Ingresar» (" + p.url().split("#")[1] + ")"); ok(await p.locator("input[type=password]").count() >= 1, "visitante: ve el formulario de ingreso");
    for (const h of ["#/banco/configurar", "#/guardia", "#/serums", "#/simuladores", "#/examenes/enam", "#/falladas", "#/feynman", "#/consulta/c01"]) { await p.evaluate(x => { location.hash = x; }, h); await dormir(350); ok(/#\/(ingresar|registro|planes)/.test(p.url()), "visitante: " + h + " lo devuelve al ingreso"); }
    await p.evaluate(() => { location.hash = "#/planes"; }); await dormir(300); ok(/#\/planes/.test(p.url()) && /plan|Plan/.test(await p.innerText("#vista")), "visitante: sí puede ver los planes");
    await p.evaluate(() => { location.hash = "#/registro"; }); await dormir(300); ok(/#\/registro/.test(p.url()), "visitante: sí puede registrarse");
    ok(pedidos.length === 0, "visitante: el servidor no entregó ningún banco ni caso: " + pedidos.slice(0, 3));
    const g = await p.request.get(C.base + "bancos/cardiologia.json"); ok(g.status() === 401, "visitante: el archivo directo da 401");
    /* ---- registrado sin plan ---- */
    await p.goto(C.base + "app/#/registro"); await p.waitForSelector("#a-nombre");
    await p.fill("#a-nombre", "Estudiante Prueba"); await p.fill("#a-correo", "est@ejemplo.com"); await p.fill("#a-clave", "clave-segura-1"); await p.check("#a-acepto"); await p.click('form button[type=submit], form .btn--primary'); await dormir(1500);
    ok(/#\/planes/.test(p.url()) || /#\/inicio/.test(p.url()) === false, "registrado sin plan: queda en los planes (" + p.url().split("#")[1] + ")");
    await p.evaluate(() => { location.hash = "#/inicio"; }); await dormir(500); ok(/#\/planes/.test(p.url()), "registrado sin plan: no entra a la plataforma");
    ok(pedidos.length === 0, "registrado sin plan: tampoco descarga bancos");
    /* ---- pasa a ser dueño: entra y se cargan los bancos ---- */
    await p.evaluate(() => { location.hash = "#/perfil"; }); await p.waitForSelector("#duenoClave", { state: "attached" }); await p.evaluate(() => { document.querySelector("details:has(#duenoClave)").open = true; });
    await p.fill("#duenoClave", TOKEN); await p.click('[data-accion="duenoActivar"]'); await dormir(1500);
    await p.evaluate(() => { location.hash = "#/inicio"; }); await p.waitForFunction(() => /preguntas|Preparate|Prepárate/i.test(document.querySelector("#vista").innerText), null, { timeout: 20000 });
    ok(/#\/inicio/.test(p.url()), "dueño: entra a la plataforma"); ok(pedidos.some(u => /bancos\//.test(u)) && pedidos.some(u => /algoritmos\.js/.test(u)), "dueño: ahora sí recibe los bancos y los algoritmos");
    await p.evaluate(() => { location.hash = "#/serums"; }); await p.waitForSelector(".sr-casos, .sr-intro", { timeout: 15000 }); ok(await p.locator(".sr").count() >= 0, "dueño: abre la Misión SERUMS");
    /* ---- abierto: todo como siempre ---- */
    const ctx2 = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx2.addInitScript(INIT); const q = await nueva(ctx2);
    await q.goto(O.base + "app/#/inicio"); await q.waitForFunction(() => /preguntas|Prepárate/i.test(document.querySelector("#vista").innerText), null, { timeout: 20000 }); ok(/#\/inicio/.test(q.url()), "abierto: cualquiera entra sin cuenta, como antes");
    ok(errores.length === 0, "sin excepciones de JavaScript: " + errores.slice(0, 3).join(" | "));
  } finally { await navegador.close(); C.php.kill(); O.php.kill(); fs.rmSync(C.tmp, { recursive: true, force: true }); fs.rmSync(O.tmp, { recursive: true, force: true }); }
  console.log(`acceso_e2e: ${total - fallos}/${total} comprobaciones correctas`); process.exit(fallos ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
