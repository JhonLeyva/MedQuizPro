// node tests/serums_e2e.js — Misión SERUMS en un navegador real (Playwright/Chromium): tarjeta (sin botón propio en el menú), introducción, portada, panel de la posta,
// recorridos completos, inventario persistente, evento de vía bloqueada, pruebas, supervisor documental, sesión recuperable, informe A–H, móvil, teclado y axe.
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
const CASOS = fs.readdirSync(path.join(RAIZ, "serums/casos")).sort().map(f => JSON.parse(fs.readFileSync(path.join(RAIZ, "serums/casos", f), "utf8")));
const AXE = process.env.AXE_PATH && fs.existsSync(process.env.AXE_PATH) ? fs.readFileSync(process.env.AXE_PATH, "utf8") : null;
const INIT = () => { try { localStorage.setItem("mqp_guardia_intro_v1", "omitir"); } catch (e) {} };

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "sr-e2e-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  for (const d of ["app", "guardia", "serums"]) fs.cpSync(path.join(RAIZ, d), path.join(tmp, d), { recursive: true });
  for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));
  fs.mkdirSync(path.join(tmp, "t")); const pWeb = await libre();
  const php = spawn("php", ["-S", `127.0.0.1:${pWeb}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1200);
  const base = `http://127.0.0.1:${pWeb}/`;
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  const errores = [], externas = [];
  const nueva = async ctx => { const p = await ctx.newPage(); p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    p.on("request", r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !/fonts\.(googleapis|gstatic)\.com/.test(r.url())) externas.push(r.url()); }); return p; };
  const portada = async (p, cerrarIntro = true) => { await p.goto(base + "app/#/serums"); await p.waitForSelector(".sr-hero, .sr-intro"); if (cerrarIntro && await p.locator(".sr-intro").count()) await p.click("[data-asumir]"); await p.waitForSelector(".sr-casos"); };
  const optima = (c, m) => m.opciones.find(o => o.calidad === "optima").id;
  async function jugar(p, c, perfil) {
    await p.goto(base + "app/#/serums/" + c.id); await p.waitForSelector("#srDecidir");
    for (let i = 0; i < c.momentos.length; i++) {
      const m = c.momentos[i]; await p.waitForSelector("#srDecT"); ok((await p.innerText("#srDecT")) === m.titulo, c.id + ": decisión " + (i + 1) + " = " + m.titulo);
      const op = perfil === "ideal" ? optima(c, m) : (m.opciones.find(o => o.calidad === "peligrosa") || m.opciones.find(o => o.calidad === "incorrecta") || m.opciones[1]).id;
      const lab = p.locator(".sr-op", { has: p.locator('input[value="' + op + '"]:not([disabled])') });
      if (!(await lab.count())) { const alt = p.locator('.sr-op:not(.is-off) input').first(); await alt.check(); } else await lab.click();
      ok(await p.isEnabled("#srDecidir"), c.id + ": el botón se habilita al elegir");
      await p.click("#srDecidir"); await dormir(40);
      if (i < c.momentos.length - 1) { const txt = await p.innerText(".sr-decision"); ok(!/Decisión óptima|Peligrosa \(error crítico\)|Mejor opción/.test(txt), c.id + ": la decisión no se corrige durante el caso"); }
    }
    await p.waitForSelector(".sr--informe");
  }
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx.addInitScript(INIT);
    const p = await nueva(ctx);

    /* tarjeta (sin botón propio en el menú) */
    await p.goto(base + "app/#/guardia"); await p.waitForSelector(".gh-card"); if (await p.locator(".gi").count()) { await p.keyboard.press("Escape"); await dormir(300); }
    ok(await p.locator(".gh-card").count() === 4 && await p.locator(".gh-card--teal").count() === 1, "el centro de simulación tiene la cuarta tarjeta");
    const tx = await p.innerText(".gh-card--teal"); ok(/Misión SERUMS/.test(tx) && /MEDICINA RURAL Y COMUNITARIA/i.test(tx) && /NUEVO/i.test(await p.evaluate(() => getComputedStyle(document.querySelector(".gh-card--teal .gh-card__foto"), "::before").content)), "la tarjeta lleva el título y las etiquetas");
    const fb = await p.evaluate(() => { const i = document.querySelector(".gh-card--teal .gh-card__foto img"), c = getComputedStyle(document.querySelector(".gh-card--teal .gh-card__foto"), "::after"); return [i.naturalWidth > 0, c.backgroundColor, c.content]; }); ok(fb[0] && fb[1] === "rgba(0, 0, 0, 0)", "la foto de la tarjeta se ve (no queda cubierta por un velo blanco)");
    ok(await p.getAttribute(".gh-card--teal a.gh-btn", "href") === "#/serums", "el botón de la tarjeta lleva a #/serums");
    ok(await p.locator('.side__nav a[data-ruta="serums"]').count() === 0, "el menú lateral no tiene un botón aparte de «Misión SERUMS»");

    /* introducción y portada */
    await p.goto(base + "app/#/serums"); await p.waitForSelector(".sr-intro"); const it = await p.innerText(".sr-intro");
    ok(/Tu primer día como serumista/i.test(it) && /Asumir mi posta/i.test(it), "introducción con el título y el botón «Asumir mi posta»");
    ok(await p.evaluate(() => document.activeElement && document.activeElement.hasAttribute("data-asumir")), "el foco inicial está en «Asumir mi posta»");
    await p.click("[data-asumir]"); await p.waitForSelector(".sr-casos"); ok(await p.locator(".sr-intro").count() === 0, "la introducción se cierra"); ok(await p.getAttribute('.side__nav a[data-ruta="guardia"]', "aria-current") === "page", "en la Misión SERUMS el menú marca «Sobrevive a la Guardia»");
    await p.goto(base + "app/#/guardia"); await p.goto(base + "app/#/serums"); await dormir(300); ok(await p.locator(".sr-intro").count() === 0, "la introducción no se repite en la misma sesión");
    await p.click("#srVerIntro"); await p.waitForSelector(".sr-intro"); await p.keyboard.press("Escape"); await dormir(100); ok(await p.locator(".sr-intro").count() === 0, "Escape cierra la introducción");
    ok(await p.locator(".sr-caso").count() === 10, "diez casos en la portada");
    ok(/Medicina rural y comunitaria/i.test(await p.innerText(".sr-tags")) && /Nuevo/i.test(await p.innerText(".sr-tags")), "etiquetas de la portada");
    ok((await p.innerText(".sr-caso")).includes("Pendiente de revisión clínica"), "cada caso muestra su estado de publicación");
    const cols = await p.evaluate(() => { const a = document.querySelector(".sr-izq").getBoundingClientRect(), b = document.querySelector(".sr-der").getBoundingClientRect(); return [a.left, b.left, a.top, b.top]; });
    ok(cols[1] > cols[0] + 300 && Math.abs(cols[2] - cols[3]) < 40, "escritorio: dos columnas");
    ok(await p.locator('img[src*="serums.webp"]').count() >= 1, "usa la imagen de la posta");

    /* panel de la posta */
    await p.fill('input[name="nombre"]', "Puesto de Salud Prueba"); await p.selectOption('select[name="ambito"]', "selva"); await p.fill('input[name="distancia_min"]', "240"); await p.click("#srForm button[type=submit]");
    ok(/guardada/.test(await p.innerText("#srOk")), "la posta se guarda"); await portada(p); ok(await p.inputValue('input[name="nombre"]') === "Puesto de Salud Prueba" && await p.inputValue('input[name="distancia_min"]') === "240", "la configuración persiste");

    /* recorrido ideal del caso 2: sin corrección en vivo, informe A–H, inventario persistente */
    const c2 = CASOS.find(c => c.id === "s02"); await jugar(p, c2, "ideal");
    ok((await p.locator(".sr-sec").count()) === 8 && (await p.locator(".sr-sec h2 span").allInnerTexts()).join("") === "ABCDEFGH", "el informe tiene las secciones A–H");
    const inf = await p.innerText(".sr--informe"); const pts = parseInt((inf.match(/(\d+) \/ 100/) || [])[1]); ok(pts >= 90, "recorrido ideal ≥ 90 en el informe (" + pts + ")");
    ok(/Pendiente de revisión clínica/.test(inf) && /GPC|Serie GPC/.test(inf) && /p\. 11/.test(inf), "el informe cita la guía con su página y declara el estado de validación");
    ok(/sulfato de magnesio/i.test(inf) && /5<\/b> usados|: 5 usados|\b5\b usados/.test(inf.replace(/\n/g, " ")), "el informe reporta el consumo de insumos");
    await portada(p); await p.click(".sr-det summary"); const inv = await p.innerText(".sr-det"); ok(/Sulfato de magnesio \(ampollas\)\s*5/.test(inv.replace(/\n/g, " ")), "el inventario persistente descontó el sulfato de magnesio");
    ok(/1 de 10/.test(await p.innerText(".sr-panel:nth-of-type(2)")) || /1 de 10/.test(await p.innerText(".sr-der")), "el progreso refleja el intento");
    await p.click("#srRepo"); await p.waitForSelector(".sr-casos"); await p.click(".sr-det summary"); ok(/Sulfato de magnesio \(ampollas\)\s*10/.test((await p.innerText(".sr-det")).replace(/\n/g, " ")), "«Reponer almacén» restablece el inventario");

    /* recorrido deficiente: error crítico */
    const c1 = CASOS.find(c => c.id === "s01"); await jugar(p, c1, "mal"); const i1 = await p.innerText(".sr--informe"); ok(/error crítico/i.test(i1) && parseInt((i1.match(/(\d+) \/ 100/) || [])[1]) < 60, "el recorrido peligroso da < 60 y señala el error crítico");

    /* vía bloqueada en el caso 5 */
    const c5 = CASOS.find(c => c.id === "s05"); await p.goto(base + "app/#/serums/s05"); await p.waitForSelector("#srDecidir");
    for (let i = 0; i < 2; i++) { await p.locator(".sr-op", { has: p.locator('input[value="a"]') }).click(); await p.click("#srDecidir"); await dormir(40); }
    await p.waitForSelector("#srDecT"); ok(/vía bloqueada|Evento/i.test(await p.innerText(".sr-aviso")), "aparece el evento de la vía bloqueada");
    ok(await p.locator('.sr-op.is-off').count() === 1 && /bloqueada/i.test(await p.innerText('.sr-op.is-off')), "la opción de ambulancia queda deshabilitada con motivo");
    await p.click("#srT_referencia"); ok(/Bloqueada/.test(await p.innerText("#srP")), "la pestaña Referencia muestra la vía bloqueada");
    await p.click("#srT_evolucion"); ok(/Evento/.test(await p.innerText("#srP")), "la pestaña Evolución registra el evento");

    /* pestañas, teclado, pruebas y supervisor */
    await p.goto(base + "app/#/serums/s03"); await p.waitForSelector("#srDecidir");
    const nombres = await p.locator('[role=tab]').allInnerTexts(); ok(nombres.join("|") === "Paciente|Historia|Examen físico|Pruebas|Inventario|Referencia|Normativa|Evolución", "las ocho pestañas del expediente");
    await p.focus("#srT_paciente"); await p.keyboard.press("ArrowRight"); ok(await p.getAttribute("#srT_historia", "aria-selected") === "true", "flechas cambian de pestaña");
    await p.click("#srT_pruebas"); await p.click('[data-prueba="p1"]'); ok(/Positiva/.test(await p.innerText("#srP")) && /20 min/.test(await p.innerText("#srSim")), "solicitar la prueba muestra su resultado y avanza el reloj");
    await p.click("#srT_inventario"); ok(/pruebas rápidas de dengue\s*19/i.test((await p.innerText("#srP")).replace(/\n/g, " ")), "la prueba descontó una unidad");
    await p.goto(base + "app/#/serums/s02"); await p.waitForSelector("#srDecidir"); await p.click("#srT_normativa"); await p.fill("#srQ", "criterios de severidad sulfato de magnesio"); await p.click("#srSup button"); await p.waitForSelector("#srRes blockquote");
    ok(/página \d+/.test(await p.innerText("#srRes")) && /no es una IA/i.test(await p.innerText("#srP")), "el supervisor cita fragmentos con página y declara que no es IA");
    await p.goto(base + "app/#/serums/s04"); await p.waitForSelector("#srDecidir"); await p.click("#srT_normativa"); await p.fill("#srQ", "diarrea"); await p.click("#srSup button"); await p.waitForSelector("#srRes p"); ok(/no tiene fuentes indexadas/.test(await p.innerText("#srRes")), "sin fuentes indexadas el supervisor no inventa");
    ok(/Pendiente de validación científica/.test(await p.innerText("#srP")), "el caso sin fuente declara «Pendiente de validación científica»");

    /* sesión recuperable */
    await p.goto(base + "app/#/serums/s06"); await p.waitForSelector("#srDecidir"); await p.locator(".sr-op", { has: p.locator('input[value="a"]') }).click(); await p.click("#srDecidir"); await p.waitForSelector("#srDecT");
    await p.reload(); await p.waitForSelector("#srDecT"); ok(/decisión 2 de 5/i.test(await p.innerText(".sr-paso")), "al recargar se recupera la sesión");

    /* registro de evidencia */
    await portada(p); await p.click("#srFuentes"); await p.waitForSelector(".sr-fu"); const reg = await p.innerText("dialog.gd-dlg"); ok(await p.locator("dialog .sr-fu").count() === 15, "el registro muestra las 15 fuentes");
    ok(/Normativa vigente verificada/.test(reg) && /Documento en revisión/.test(reg) && /Referencia histórica/.test(reg) && /No verificada/.test(reg), "el registro distingue los estados de vigencia y marca la norma no verificada"); await p.keyboard.press("Escape");

    /* móvil */
    const mov = await navegador.newContext({ viewport: { width: 390, height: 800 } }); await mov.addInitScript(INIT); const pm = await nueva(mov);
    await portada(pm); const ov = await pm.evaluate(() => document.documentElement.scrollWidth - innerWidth); ok(ov <= 1, "móvil: sin desplazamiento horizontal en la portada (" + ov + ")");
    const cm = await pm.evaluate(() => { const a = document.querySelector(".sr-izq").getBoundingClientRect(), b = document.querySelector(".sr-der").getBoundingClientRect(); return b.top > a.bottom - 5; }); ok(cm, "móvil: una columna");
    await pm.goto(base + "app/#/serums/s02"); await pm.waitForSelector("#srDecidir"); const ov2 = await pm.evaluate(() => document.documentElement.scrollWidth - innerWidth); ok(ov2 <= 1, "móvil: sin desplazamiento horizontal en la atención (" + ov2 + ")");

    /* accesibilidad (axe) en claro y oscuro */
    if (AXE) for (const esquema of ["light", "dark"]) {
      const cx = await navegador.newContext({ viewport: { width: 1280, height: 900 }, colorScheme: esquema }); await cx.addInitScript(INIT); const pa = await nueva(cx);
      for (const [nombre, paso] of [["portada", async () => { await portada(pa); }], ["atención", async () => { await pa.goto(base + "app/#/serums/s02"); await pa.waitForSelector("#srDecidir"); }], ["informe", async () => { await jugar(pa, CASOS.find(c => c.id === "s08"), "ideal"); }], ["introducción", async () => { await pa.evaluate(() => sessionStorage.clear()); await pa.goto(base + "app/#/serums"); await pa.reload(); await pa.waitForSelector(".sr-intro"); }]]) {
        await paso(); await dormir(1300); await pa.evaluate(AXE); const r = await pa.evaluate(() => axe.run(document, { runOnly: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] }));
        const v = r.violations.filter(x => x.impact !== "minor"); if (v.length) console.log(esquema, nombre, v.map(x => x.id + ": " + x.nodes.slice(0, 3).map(n => n.target.join(" ")).join(" ; ")).join("\n  "));
        ok(v.length === 0, "axe " + esquema + " · " + nombre + ": sin violaciones");
      }
      await cx.close();
    } else console.log("(axe omitido: define AXE_PATH)");

    ok(errores.length === 0, "sin errores de consola ni excepciones: " + errores.slice(0, 3).join(" | "));
    ok(externas.length === 0, "sin peticiones externas: " + externas.slice(0, 3).join(" | "));
  } finally { await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true }); }
  console.log(`serums_e2e: ${total - fallos}/${total} comprobaciones correctas`); process.exit(fallos ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
