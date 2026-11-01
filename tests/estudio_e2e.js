// node tests/estudio_e2e.js — confianza al responder, Repaso de hoy y tarjetas Cloze en un navegador real (Playwright/Chromium) contra PHP. No usa IA.
// Variables: AXE_PATH (axe.min.js; sin él se omite accesibilidad), SHOTS (carpeta de capturas), CHROMIUM (ejecutable).
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
const banco = {}; for (const f of fs.readdirSync(path.join(RAIZ, "bancos"))) for (const q of JSON.parse(fs.readFileSync(path.join(RAIZ, "bancos", f), "utf8")).preguntas) banco[q.enunciado.trim()] = q;
const letras = q => Array.isArray(q.opciones) ? "ABCDE".slice(0, q.opciones.length).split("") : Object.keys(q.opciones).sort();

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "est-e2e-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  fs.cpSync(path.join(RAIZ, "app"), path.join(tmp, "app"), { recursive: true }); fs.cpSync(path.join(RAIZ, "guias"), path.join(tmp, "guias"), { recursive: true });
  for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));
  fs.mkdirSync(path.join(tmp, "t")); const pWeb = await libre();
  const php = spawn("php", ["-S", `127.0.0.1:${pWeb}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1200);
  const base = `http://127.0.0.1:${pWeb}/`, shots = process.env.SHOTS || "", origen = base.slice(0, -1);
  const foto = async (p, n) => { if (shots) { fs.mkdirSync(shots, { recursive: true }); await p.screenshot({ path: path.join(shots, n + ".png") }); } };
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx.addInitScript(() => { try { localStorage.setItem("mqp_sin_intros_prueba", "1"); } catch (e) {} });
    const reg = await ctx.request.post(base + "cuenta.php?a=registro", { data: { nombre: "Tester Estudio", correo: "e@prueba.pe", clave: "clave12345", acepto: true }, headers: { "X-MQP": "1", Origin: origen } }); ok(reg.status() === 201, "registro");
    const p = await ctx.newPage(); const errores = []; p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    const json = async r => (await ctx.request.get(base + r)).json();
    const iniciar = async () => { await p.goto(base + "app/#/banco/configurar"); await p.waitForSelector("[data-accion=comenzar]"); await p.click("[data-accion=comenzar]"); await p.waitForSelector("#svOptions .opt"); await p.waitForFunction(() => window.MQP && MQP.estudio && MQP.estudio.activo()); };
    const actual = async () => { const enun = (await p.locator("#svStem").innerText()).trim(); return banco[enun]; };

    /* ===== 1. confianza antes de revelar ===== */
    await iniciar(); let q = await actual(); ok(!!q, "la pregunta mostrada existe en el banco");
    const antes = await p.evaluate(() => [...document.querySelectorAll("#svOptions .opt__text")].map(e => e.textContent));
    const L = letras(q), clave = String(q.clave_correcta).trim().toUpperCase(), mala = L.find(l => l !== clave), mala2 = L.filter(l => l !== clave)[1];
    await p.click(`#svOptions .opt[data-letra=${mala}]`); await p.waitForSelector("#estConf");
    ok(await p.locator("#svFeedback").isHidden() && (await p.locator("#svOptions .opt--right").count()) === 0, "al elegir NO se revela la respuesta todavía");
    ok(await p.locator("#estConf [data-c]").count() === 4 && await p.locator("#estConf [data-no]").count() === 1 && /Adiviné/.test(await p.locator("#estConf").innerText()) && /Dudaba entre dos/.test(await p.locator("#estConf").innerText()) && /Estoy seguro/.test(await p.locator("#estConf").innerText()), "tres niveles de confianza + responder sin indicar + no volver a preguntar");
    ok(/no cambia tu puntaje/i.test(await p.locator("#estConf").innerText()), "avisa que la confianza no cambia el puntaje");
    await p.click(`#svOptions .opt[data-letra=${mala2}]`); ok((await p.locator(`#svOptions .opt[data-letra=${mala2}]`).getAttribute("aria-pressed")) === "true" && (await p.locator(`#svOptions .opt[data-letra=${mala}]`).getAttribute("aria-pressed")) === "false" && await p.locator("#estConf").count() === 1, "se puede cambiar de alternativa antes de confirmar (una sola barra)");
    await foto(p, "e1-confianza");
    await p.click("#estConf [data-c=alta]"); await p.waitForSelector("#svFeedback:not([hidden])");
    ok(await p.locator("#estConf").count() === 0 && /incorrecta/i.test(await p.locator("#svVerdict").innerText()) && (await p.locator("#svOptions .opt--right").count()) === 1, "al confirmar se revela la respuesta con la lógica de siempre");
    await p.waitForSelector("#estNota"); ok(/Falso concepto de alta prioridad/.test(await p.locator("#estNota").innerText()) && await p.locator("#estNota a[href='#/repaso']").count() === 1, "fallo con confianza alta → «Falso concepto de alta prioridad» con enlace a Repaso de hoy");
    const despues = await p.evaluate(() => [...document.querySelectorAll("#svOptions .opt__text")].map(e => e.textContent)); ok(JSON.stringify(antes) === JSON.stringify(despues), "las alternativas conservan texto y orden");
    ok(await p.evaluate(id => { const r = JSON.parse(localStorage.getItem("mqp_progreso_v1") || "{}").respuestas || {}; return Object.values(r).some(x => x && x.ok === false); }, q.id), "el sistema de progreso original registró el fallo (puntaje intacto)");
    const rep1 = await json("estudio.php?a=repaso"); ok(rep1.ids[0] === q.id && rep1.refuerzo[0].etiqueta === "falso_concepto", "el intento quedó guardado en el servidor");

    /* ===== 2. responder sin indicar, y «no volver a preguntar» ===== */
    await p.click("#svNext"); await p.waitForFunction(() => document.querySelector("#svFeedback").hidden); ok(await p.locator("#estConf").count() === 0 && await p.locator("#estNota").count() === 0, "al cambiar de pregunta se limpia la barra y la nota");
    q = await actual(); const m2 = letras(q).find(l => l !== String(q.clave_correcta).trim().toUpperCase());
    await p.click(`#svOptions .opt[data-letra=${m2}]`); await p.waitForSelector("#estConf"); await p.click("#estConf [data-c='']"); await p.waitForSelector("#svFeedback:not([hidden])");
    await p.waitForSelector("#estNota"); ok(/refuerzo/i.test(await p.locator("#estNota").innerText()), "«Responder sin indicar» también responde (y un fallo queda para refuerzo)");
    await p.click("#svNext"); await p.waitForFunction(() => document.querySelector("#svFeedback").hidden); q = await actual();
    await p.click(`#svOptions .opt[data-letra=${letras(q)[0]}]`); await p.waitForSelector("#estConf"); await p.click("#estConf [data-no]"); await p.waitForSelector("#svFeedback:not([hidden])");
    await p.click("#svNext"); await p.waitForFunction(() => document.querySelector("#svFeedback").hidden); await p.click("#svOptions .opt >> nth=0"); await p.waitForSelector("#svFeedback:not([hidden])", { timeout: 3000 });
    ok(await p.locator("#estConf").count() === 0, "«No volver a preguntar» desactiva la barra: se responde directo");
    const n3 = (await json("estudio.php?a=repaso")).semana.intentos; ok(n3 >= 4, "todos los intentos se registraron (" + n3 + ")");

    /* ===== 3. Repaso de hoy ===== */
    await p.goto(base + "app/#/repaso"); await p.waitForSelector(".est-wrap");
    ok(await p.locator('a[data-ruta=repaso]').first().isVisible(), "entrada «Repaso de hoy» en la navegación");
    ok(/Repaso de hoy/.test(await p.locator("h1").innerText()) && await p.locator(".qitem").count() >= 2 && /Falso concepto de alta prioridad/.test(await p.locator(".qlist").innerText()), "lista de preguntas por reforzar con datos reales");
    ok(/Estoy seguro/.test(await p.locator(".est-tabla").innerText()) && /Esto no es un calendario de repetición espaciada/.test(await p.locator(".est-wrap").innerText()), "calibración real y aviso honesto sobre el criterio de orden");
    ok(await p.locator("#estAj").isChecked() === false, "el ajuste refleja que se desactivó la pregunta de confianza"); await p.check("#estAj"); await foto(p, "e2-repaso");
    const nRef = await p.locator(".qitem").count(); await p.click(".est-wrap [data-accion=repaso] >> nth=0"); await p.waitForSelector("#svOptions .opt");
    ok(/Pregunta 1 de \d+/.test(await p.locator("#svCounter").innerText()) && Math.min(20, nRef) === +(/de (\d+)/.exec(await p.locator("#svCounter").innerText())[1]), "«Practicar» abre una sesión con esas preguntas del banco");
    ok(await p.locator("#estConf").count() === 0, "(la barra aparece solo al elegir una alternativa)");
    q = await actual(); const qid = q.id; await p.click(`#svOptions .opt[data-letra=${String(q.clave_correcta).trim().toUpperCase()}]`); await p.waitForSelector("#estConf"); await p.click("#estConf [data-c=alta]"); await p.waitForSelector("#svFeedback:not([hidden])"); await dormir(400);
    const rep2 = await json("estudio.php?a=repaso"); ok(!rep2.ids.includes(qid), "acertar con seguridad una pregunta por reforzar la saca de la lista");

    /* ===== 4. Cloze ===== */
    await p.goto(base + "app/#/inicio"); await dormir(300); await iniciar(); await p.evaluate(() => { try { localStorage.setItem("mqp_estudio_confianza", "si"); } catch (e) {} });
    let panel = false;
    for (let k = 0; k < 8 && !panel; k++) {
      if (k) { await p.click("#svNext"); await p.waitForFunction(() => document.querySelector("#svFeedback").hidden); }
      q = await actual(); await p.click(`#svOptions .opt[data-letra=${letras(q)[0]}]`);
      if (await p.locator("#estConf").count()) await p.click("#estConf [data-c='']"); await p.waitForSelector("#svFeedback:not([hidden])");
      await p.click("#svFlash"); await p.waitForSelector("dialog.fc-dlg[open]");
      panel = (await p.locator(".fc-prop--cloze").count()) > 0; if (!panel) await p.keyboard.press("Escape");
    }
    ok(panel, "la pregunta ofrece una tarjeta «Perla clínica · completar el hueco (Cloze)»");
    const frente0 = await p.inputValue(".fc-prop--cloze textarea"); ok(/\{\{c1::.+\}\}/.test(frente0) && q.comentario.replace(/\s+/g, " ").includes(frente0.replace(/\{\{c\d+::([^}]*)\}\}/g, "$1")), "la frase propuesta es literal del comentario docente y oculta la respuesta");
    ok(/Así la verás: .*\[…\]/.test(await p.locator(".fc-cz-prev").innerText()), "vista previa con el hueco tapado"); await foto(p, "e3-cloze");
    // el estudiante marca otro hueco: selecciona una palabra del texto visible
    const marcado = await p.evaluate(() => { const ta = document.querySelector(".fc-prop--cloze textarea"), v = ta.value, re = /(^|[\s,.(])([A-Za-záéíóúñ]{6,})(?=[\s,.)])/g; let m; while ((m = re.exec(v))) { const ini = m.index + m[1].length, fin = ini + m[2].length; if (!/\{\{[^}]*$/.test(v.slice(0, ini)) && !/^[^{]*\}\}/.test(v.slice(fin))) { ta.focus(); ta.setSelectionRange(ini, fin); return m[2]; } } return null; });
    if (marcado) { await p.click("[data-cz=ocultar]"); ok(/\{\{c2::/.test(await p.inputValue(".fc-prop--cloze textarea")), "«Ocultar selección» crea un segundo hueco (c2): " + marcado); }
    await p.click("[data-cz=quitar]"); ok(!/\{\{/.test(await p.inputValue(".fc-prop--cloze textarea")) && /Marca al menos un hueco/.test(await p.locator(".fc-cz-prev").innerText()), "«Quitar todos los huecos» → la vista previa avisa que falta un hueco");
    await p.click("#fcGuardar"); ok(/Marca al menos un hueco/.test(await p.locator("#fcMsg").innerText()) && (await json("cuenta.php?a=fc_listar")).tarjetas.length === 0, "no se guarda una Cloze sin huecos");
    await p.fill(".fc-prop--cloze textarea", frente0); await p.click("[data-cz=ocultar]"); ok(/selecciona en el texto/i.test(await p.locator("#fcMsg").innerText()), "ocultar sin selección → ayuda clara (sin romper nada)");
    for (const c of await p.locator(".fc-prop:not(.fc-prop--cloze) input[type=checkbox]").all()) await c.uncheck();      // solo la Cloze
    await p.click("#fcGuardar"); await p.waitForFunction(() => /Guardaste/.test(document.querySelector("#fcMsg").innerText));
    const fc = (await json("cuenta.php?a=fc_listar")).tarjetas; const cz = fc.find(x => /\{\{c1::/.test(x.frente));
    ok(!!cz && /^Respuesta: /.test(cz.dorso) && cz.pregunta === q.id && /Cloze/.test(cz.fuente), "la tarjeta se guardó en el mazo existente, ligada a su pregunta y fuente");
    await p.keyboard.press("Escape");
    await p.goto(base + "app/#/flashcards"); await p.waitForSelector(".fc-item"); ok(/\[…\]/.test(await p.locator(".fc-lista").innerText()) && !/\{\{c1/.test(await p.locator(".fc-lista").innerText()) && /Completar el hueco/.test(await p.locator(".fc-lista").innerText()), "en «Mis flashcards» se ve con el hueco tapado, sin marcas");
    await p.click("[data-estudiar]"); await p.waitForSelector(".fc-carta");
    ok(/completa el hueco/i.test(await p.locator(".fc-cara").first().innerText()) && /\[…\]/.test(await p.locator(".fc-texto").first().innerText()), "en el repaso se muestra «Completa el hueco» con el hueco tapado");
    await p.click("#fcMostrar"); ok(/Respuesta: /.test(await p.locator("#fcDorso").innerText()), "al mostrar la respuesta aparece el dorso"); await foto(p, "e4-repaso-cloze");

    /* ===== 5. sin cuenta, el banqueo es exactamente el de siempre ===== */
    const anon = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await anon.addInitScript(() => { try { localStorage.setItem("mqp_sin_intros_prueba", "1"); } catch (e) {} });
    const a = await anon.newPage(); await a.goto(base + "app/#/banco/configurar"); await a.waitForSelector("[data-accion=comenzar]"); await a.click("[data-accion=comenzar]"); await a.waitForSelector("#svOptions .opt"); await dormir(600);
    await a.click("#svOptions .opt >> nth=0"); await a.waitForSelector("#svFeedback:not([hidden])", { timeout: 3000 }); ok(await a.locator("#estConf").count() === 0, "sin cuenta no se pide confianza: se responde y se revela al instante");
    await a.goto(base + "app/#/repaso"); await a.waitForSelector(".empty-state"); ok(/Entra para ver tu repaso/.test(await a.locator(".empty-state").innerText()), "Repaso de hoy sin cuenta invita a ingresar"); await anon.close();

    /* ===== 6. móvil y accesibilidad ===== */
    const movil = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }); await movil.addCookies(await ctx.cookies()); await movil.addInitScript(() => { try { localStorage.setItem("mqp_sin_intros_prueba", "1"); } catch (e) {} });
    const m = await movil.newPage(); await m.goto(base + "app/#/banco/configurar"); await m.waitForSelector("[data-accion=comenzar]"); await m.click("[data-accion=comenzar]"); await m.waitForSelector("#svOptions .opt"); await m.waitForFunction(() => window.MQP && MQP.estudio && MQP.estudio.activo());
    await m.click("#svOptions .opt >> nth=1"); await m.waitForSelector("#estConf"); const caja = await m.locator("#estConf").boundingBox();
    ok(caja && caja.x >= 0 && caja.x + caja.width <= 391 && await m.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), "móvil: la barra de confianza cabe sin desplazamiento horizontal");
    const bts = await m.locator("#estConf .btn").evaluateAll(b => b.map(x => x.getBoundingClientRect().height)); ok(bts.every(h => h >= 44), "móvil: botones de al menos 44 px de alto"); await foto(m, "e5-movil"); await movil.close();
    const axePath = process.env.AXE_PATH || "";
    if (axePath && fs.existsSync(axePath)) {
      const AXE = fs.readFileSync(axePath, "utf8");
      const auditar = async (pg, nombre) => { await dormir(700); await pg.evaluate(AXE); const r = await pg.evaluate(async () => await axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] } }));
        r.violations = r.violations.filter(v => !v.nodes.every(n => n.target.join(" ") === "#chatLauncher"));      // botón flotante del chat del sitio: preexistente
        ok(r.violations.length === 0, "axe · " + nombre + ": " + r.violations.map(v => v.id + " ×" + v.nodes.length + " " + v.nodes[0].target.join(" ") + " " + ((v.nodes[0].any[0] || {}).message || "")).join(" | ")); };
      await p.goto(base + "app/#/repaso"); await p.waitForSelector(".est-wrap"); await auditar(p, "Repaso de hoy");
      for (const t of ["dark", "light"]) { await p.evaluate(x => document.documentElement.setAttribute("data-theme", x), t); await p.waitForTimeout(600); await auditar(p, "Repaso de hoy tema " + t); }
      await iniciar(); q = await actual(); await p.click(`#svOptions .opt[data-letra=${letras(q)[0]}]`); await p.waitForSelector("#estConf"); await auditar(p, "pregunta con barra de confianza");
    } else console.log("(axe omitido: define AXE_PATH)");
    ok(errores.length === 0, "sin errores de JavaScript en consola: " + errores.slice(0, 3).join(" | "));
  } catch (e) { fallos++; console.log("EXCEPCIÓN:", e.message.split("\n")[0], "|", (e.stack.match(/estudio_e2e.js:\d+/) || [""])[0]); }
  finally { await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true }); }
  console.log(fallos ? fallos + " fallos de " + total : "OK: " + total + " comprobaciones E2E de confianza, Repaso de hoy y Cloze"); process.exit(fallos ? 1 : 0);
})();
