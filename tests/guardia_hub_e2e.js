// node tests/guardia_hub_e2e.js — Centro de simulación («Sobrevive a la Guardia») en un navegador real: rutas y navegación de ida y vuelta, tarjetas con datos reales,
// modalidad «Próximamente» sin enlace, recomendaciones, estadísticas calculadas con el progreso real, accesos rápidos (laboratorio, fuentes, tutor),
// imágenes del zip, responsive (escritorio/tableta/móvil), accesibilidad (axe, claro/oscuro) y ausencia de errores de consola. Variables: AXE_PATH, CHROMIUM, SHOTS.
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
global.window = {}; const GC = require("../guardia_casos.js"), CC = require("../consulta_casos.js"), N = require("../guardia_nucleo.js");
const INIT = () => { try { localStorage.setItem("mqp_guardia_intro_v1", "omitir"); } catch (e) {} };

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "gh-e2e-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  fs.cpSync(path.join(RAIZ, "app"), path.join(tmp, "app"), { recursive: true }); fs.cpSync(path.join(RAIZ, "guardia"), path.join(tmp, "guardia"), { recursive: true });
  for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));
  fs.mkdirSync(path.join(tmp, "t")); const pWeb = await libre();
  const php = spawn("php", ["-S", `127.0.0.1:${pWeb}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1200);
  const base = `http://127.0.0.1:${pWeb}/`, shots = process.env.SHOTS || "";
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  const errores = [], externas = [], malas = [];
  const nueva = async ctx => { const p = await ctx.newPage(); p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    p.on("response", r => { if (r.status() >= 400 && r.url().startsWith(base) && !/feynman\.php/.test(r.url())) malas.push(r.status() + " " + r.url()); });
    p.on("request", r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !/fonts\.(googleapis|gstatic)\.com/.test(r.url())) externas.push(r.url()); }); return p; };
  const cerrarIntro = async pg => { const hay = await pg.waitForSelector(".gi", { timeout: 2500 }).then(() => true, () => false); if (hay) { await pg.keyboard.press("Escape"); await pg.waitForSelector(".gi", { state: "detached" }); } return hay; };
  const hub = async pg => { await pg.goto(base + "app/#/guardia"); await pg.waitForSelector(".gh-hero"); await cerrarIntro(pg); await pg.waitForSelector(".gh-card"); };
  const scrollTodo = async p => { for (let i = 0; i < 12; i++) { await p.mouse.wheel(0, 600); await dormir(60); } await p.evaluate(() => window.scrollTo(0, 0)); await dormir(300); };
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1536, height: 1024 } }); await ctx.addInitScript(INIT); const p = await nueva(ctx);
    /* ---- introducción: aparece SIEMPRE al entrar (aunque exista la preferencia antigua de omitirla) ---- */
    await p.goto(base + "app/#/guardia"); await p.waitForSelector(".gh-hero");
    ok(await p.waitForSelector(".gi", { timeout: 3000 }).then(() => true, () => false), "al entrar a «Sobrevive a la Guardia» aparece la introducción aunque la preferencia antigua sea «omitir»");
    ok(/Omitir/.test(await p.innerText(".gi")) && /volverá a aparecer/.test(await p.innerText(".gi")), "la introducción avisa de que volverá a aparecer");
    await p.keyboard.press("Escape"); await p.waitForSelector(".gi", { state: "detached" }); ok(await p.locator(".gh-hero").isVisible(), "omitirla (Esc) deja ver el centro");
    ok(await p.evaluate(() => { try { return localStorage.getItem("mqp_guardia_intro_v1") === "omitir" && !(window.MQP.progreso && window.MQP.progreso.preferencia("guardiaIntro") === "omitir"); } catch (e) { return true; } }) , "omitirla no guarda ninguna preferencia nueva");
    await p.click('.side__nav a[href="#/inicio"]'); await p.waitForSelector("main, #vista"); await p.click('.side__nav a[href="#/guardia"]'); ok(await p.waitForSelector(".gi", { timeout: 3000 }).then(() => true, () => false), "al volver desde otra sección con el menú lateral, la introducción aparece de nuevo");
    await p.click("#giOmitir"); await p.waitForSelector(".gi", { state: "detached" });
    await p.click(".gh-card--rojo a.gh-btn"); await p.waitForSelector(".gd-caso"); ok(await p.locator(".gi").count() === 0, "el listado de emergencias no abre la introducción");
    await p.click('.gh-migas a[href="#/guardia"]'); await p.waitForSelector(".gh-hero"); await dormir(700); ok(await p.locator(".gi").count() === 0, "volver con las migas desde un listado no repite la introducción");
    await p.click('.side__nav a[href="#/inicio"]'); await p.click('.side__nav a[href="#/guardia"]'); ok(await p.waitForSelector(".gi", { timeout: 3000 }).then(() => true, () => false), "entrar de nuevo con el menú lateral la muestra otra vez"); await p.keyboard.press("Escape"); await p.waitForSelector(".gi", { state: "detached" });
    await p.click("#ghIntro"); ok(await p.waitForSelector(".gi", { timeout: 3000 }).then(() => true, () => false), "«Ver la introducción» la abre a demanda"); await p.keyboard.press("Escape"); await p.waitForSelector(".gi", { state: "detached" });
    /* ---- monitor vivo del hero ---- */
    ok(await p.locator("canvas.gh-monitor").count() === 1 && await p.getAttribute("canvas.gh-monitor", "aria-hidden") === "true", "el monitor animado es decorativo (aria-hidden)");
    const f1 = await p.evaluate(() => document.querySelector("canvas.gh-monitor").toDataURL()); await dormir(900); const f2 = await p.evaluate(() => document.querySelector("canvas.gh-monitor").toDataURL());
    ok(f1 !== f2, "el monitor se anima: el lienzo cambia entre fotogramas");
    const caja = await p.evaluate(() => { const c = document.querySelector("canvas.gh-monitor").getBoundingClientRect(), h = document.querySelector(".gh-hero").getBoundingClientRect(); return [c.left >= h.left - 1, c.right <= h.right + 1 || true, c.width > 100, c.height > 100]; }); ok(caja[2] && caja[3], "el lienzo del monitor tiene tamaño sobre la imagen");
    const rm = await navegador.newContext({ viewport: { width: 1536, height: 1024 }, reducedMotion: "reduce" }); await rm.addInitScript(INIT); const prm = await nueva(rm); await prm.goto(base + "app/#/guardia"); await prm.waitForSelector(".gh-hero"); await cerrarIntro(prm); await dormir(500);
    const r1 = await prm.evaluate(() => document.querySelector("canvas.gh-monitor").toDataURL()); await dormir(900); const r2 = await prm.evaluate(() => document.querySelector("canvas.gh-monitor").toDataURL()); ok(r1 === r2 && r1.length > 2000, "con «reducir movimiento» el monitor se muestra estático"); await rm.close();
    const a1 = await p.evaluate(() => document.querySelector("canvas.gh-monitor").toDataURL()); await p.click(".gh-card--rojo a.gh-btn"); await p.waitForSelector(".gd-caso"); await dormir(400);
    ok(await p.locator("canvas.gh-monitor").count() === 0, "al salir del centro el monitor se desmonta"); await hub(p);
    /* ---- sin progreso: estado vacío honesto ---- */
    await hub(p);
    ok(await p.locator("h1").first().innerText().then(t => /Sobrevive a la\s+Guardia/.test(t)), "hero con el título «Sobrevive a la Guardia»");
    ok(await p.locator(".gh-card").count() === 4, "cuatro tarjetas de modalidad");
    const hrefE = await p.getAttribute(".gh-card--rojo a.gh-btn", "href"), hrefC = await p.getAttribute(".gh-card--azul a.gh-btn", "href");
    ok(hrefE === "#/guardia/emergencias" && hrefC === "#/consulta", "botones conducen al simulador de emergencias y a la consulta clínica existentes");
    ok(/Comenzar casos de emergencia/.test(await p.innerText(".gh-card--rojo a.gh-btn")) && /Comenzar consulta clínica/.test(await p.innerText(".gh-card--azul a.gh-btn")), "textos de los botones principales");
    const rojo = await p.innerText(".gh-card--rojo"), azul = await p.innerText(".gh-card--azul"), uci = await p.innerText(".gh-card--indigo");
    ok(new RegExp("\\b" + GC.length + "\\s+Casos disponibles").test(rojo.replace(/\n/g, " ")), "cifra real de casos de emergencia (" + GC.length + ")");
    ok(new RegExp("\\b" + CC.length + "\\s+Casos disponibles").test(azul.replace(/\n/g, " ")), "cifra real de casos de consulta (" + CC.length + ")");
    const dur = a => Math.min(...a.map(c => c.duracion_min)) + " – " + Math.max(...a.map(c => c.duracion_min)) + " min";
    ok(rojo.includes(dur(GC)) && azul.includes(dur(CC)), "duración estimada calculada de los casos");
    ok(/0 de 10 casos completados/.test(rojo) && /0 de 4 consultas completadas/.test(azul), "progreso en cero al empezar");
    const UC = require("../guardia_uci.js");
    ok(await p.getAttribute(".gh-card--indigo a.gh-btn", "href") === "#/guardia/uci" && /Comenzar casos de UCI/.test(await p.innerText(".gh-card--indigo a.gh-btn")), "UCI: el botón lleva a la modalidad (ya no es «Próximamente»)");
    ok(!/Próximamente/.test(uci) && new RegExp("\\b" + UC.length + "\\s+Casos disponibles").test(uci.replace(/\n/g, " ")) && /0 de 3 casos completados/.test(uci) && uci.includes(dur(UC)), "UCI: cifras reales (" + UC.length + " casos), duración y progreso en cero");
    ok(await p.locator(".gh-chips").count() === 0 && await p.locator(".gh-card__sobre li").count() === 0, "las tarjetas de modalidad llevan solo la descripción, sin iconos ni etiquetas de especialidades");
    ok(await p.locator(".gh-rec__i").count() === 3 && /Por dónde empezar/.test(await p.innerText(".gh-rec")), "sin respuestas en el banco: «Por dónde empezar», sin personalizar");
    const rec = await p.locator(".gh-rec__a").evaluateAll(a => a.map(x => x.getAttribute("href"))); ok(rec.every(h => /^#\/guardia\/g\d\d$/.test(h)), "recomendados enlazan a casos reales");
    ok(/—/.test(await p.innerText(".gh-anillo")) && /0 \/ 10/.test(await p.innerText(".gh-est")), "estadísticas vacías sin inventar valores");
    ok(await p.locator(".gh-acc").count() === 4 && await p.locator('a.gh-acc[href="#/feynman"]').count() === 1, "cuatro accesos; el tutor enlaza a la ruta existente");
    ok(await p.locator(".gh-acc--info a, .gh-acc--info button").count() === 0 && (await p.locator(".gh-acc--info").evaluate(e => e.tagName)) === "DIV", "la tarjeta informativa de imágenes no aparenta ser un botón");
    ok(/ilustraciones generadas con IA/.test(await p.innerText(".gh-credito")), "se declara que las portadas son ilustraciones generadas con IA");
    /* imágenes del zip cargadas y optimizadas */
    await scrollTodo(p);
    const imgs = await p.locator(".gh img").evaluateAll(l => l.map(i => ({ s: i.getAttribute("src"), ok: i.complete && i.naturalWidth > 0 })));
    ok(imgs.length >= 8 && imgs.every(i => i.ok), "todas las imágenes de portada cargan (" + imgs.length + ")");
    for (const f of fs.readdirSync(path.join(RAIZ, "guardia/portadas")).filter(x => x.endsWith(".webp"))) ok(fs.statSync(path.join(RAIZ, "guardia/portadas", f)).size < 130 * 1024, "imagen optimizada < 130 KB: " + f);
    ok(await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), "escritorio sin desplazamiento horizontal");
    if (shots) { fs.mkdirSync(shots, { recursive: true }); await p.screenshot({ path: path.join(shots, "hub-escritorio.png"), fullPage: true }); }

    /* ---- navegación ida y vuelta: hub → emergencias → caso → regreso ---- */
    await p.click(".gh-card--rojo a.gh-btn"); await p.waitForSelector(".gd-caso");
    ok(/#\/guardia\/emergencias$/.test(p.url()) && await p.locator(".gd-caso").count() === GC.length, "listado de emergencias con todos los casos (" + GC.length + ")");
    ok(await p.locator(".gh-modal--rojo").count() === 1 && await p.locator(".gh-migas").innerText().then(t => /Centro de simulación/.test(t) && /Guardia de emergencias/.test(t)), "cabecera roja de la modalidad y migas");
    await p.click('.gd-caso a.btn >> nth=1'); await p.waitForSelector("#gdEmpezar"); ok(/#\/guardia\/g\d\d$/.test(p.url()), "el caso se abre en su ruta original");
    await p.click("#gdEmpezar"); await p.waitForSelector(".gd-op"); const nOps = await p.locator(".gd-op").count(); ok(nOps === 5, "el caso muestra las cinco alternativas A–E intactas");
    const idCaso = p.url().match(/g\d\d$/)[0], caso = GC.find(c => c.id === idCaso), pregunta = caso.nodos[caso.inicio].pregunta;
    ok((await p.innerText("#gdQ")).trim() === pregunta.trim(), "la pregunta coincide con los datos del caso");
    const textos = await p.locator(".gd-op__t").allInnerTexts(); ok(caso.nodos[caso.inicio].decisiones.every((d, i) => textos[i].replace(/^Alternativa [A-E]:\s*/, "").trim() === d.texto.trim()), "las alternativas coinciden con los datos del caso");
    await p.click(".gd-top .link-arrow"); await p.waitForSelector(".gd-caso"); ok(/#\/guardia\/emergencias$/.test(p.url()), "desde el caso se regresa al listado de la modalidad");
    await p.click('.gh-migas a[href="#/guardia"]'); await p.waitForSelector(".gh-hero"); ok(/#\/guardia$/.test(p.url()), "desde el listado se regresa al centro de simulación");
    /* ---- consulta ---- */
    await p.click(".gh-card--azul a.gh-btn"); await p.waitForSelector("#cqLista"); ok(await p.locator(".gh-modal--azul").count() === 1 && await p.locator("#cqLista .gd-caso").count() === CC.length, "listado de consulta con cabecera azul y todos los casos");
    await p.click("#cqLista .gd-caso a.btn >> nth=0"); await p.waitForSelector("#cqTitulo"); ok(/#\/consulta\/c\d\d$/.test(p.url()), "la consulta se abre en su ruta original");
    await p.click(".gd-top .link-arrow"); await p.waitForSelector("#cqLista"); await p.click('.gh-migas a[href="#/guardia"]'); await p.waitForSelector(".gh-hero"); ok(true, "consulta → listado → centro");
    ok(await p.locator('.side__nav a[href="#/guardia"][aria-current="page"]').count() === 1, "el menú lateral mantiene «Sobrevive a la Guardia» activo en el centro");
    /* ---- accesos ---- */
    await p.click("#ghLab"); await p.waitForSelector("dialog[open] .gb-area"); ok(/Biblioteca de valores de laboratorio/.test(await p.innerText("dialog[open] h2")), "el acceso abre la biblioteca de valores de laboratorio");
    const nAreas = await p.locator("dialog[open] .gb-area").count(), nFilas = await p.locator("dialog[open] .gb-fila").count(); ok(nAreas >= 18 && nFilas >= 300, "la biblioteca trae todas las áreas (" + nAreas + ") y más de 300 análisis (" + nFilas + ")");
    ok(await p.locator("dialog[open] .gb-area[open]").count() === 0 && /análisis en \d+ áreas/.test(await p.innerText("#gbN")), "las áreas empiezan plegadas y se anuncia el total");
    await p.click("dialog[open] .gb-area >> nth=0 >> summary"); ok(await p.locator("dialog[open] .gb-area >> nth=0").getAttribute("open") !== null && await p.locator("dialog[open] .gb-area >> nth=0 >> tbody tr:visible").count() > 20, "cada área se despliega y muestra sus análisis con unidad y valores");
    ok(/Hemoglobina/.test(await p.innerText("dialog[open] .gb-area >> nth=0")) && /13\.5 – 17\.5/.test(await p.innerText("dialog[open] .gb-area >> nth=0")), "hematología muestra la hemoglobina por edad y sexo"); await p.click("dialog[open] .gb-area >> nth=0 >> summary"); ok(await p.locator("dialog[open] .gb-area >> nth=0").getAttribute("open") === null, "se pliega de nuevo");
    await p.fill("#gbQ", "creatinina"); ok(/resultados? en \d+ áreas?/.test(await p.innerText("#gbN")) && await p.locator("dialog[open] .gb-fila:visible").count() >= 3 && await p.locator("dialog[open] .gb-area[open]:visible").count() >= 1, "el buscador filtra y abre las áreas con coincidencias");
    ok((await p.locator("dialog[open] .gb-fila:visible").allInnerTexts()).every(t => /creatinina/i.test(t)), "solo quedan análisis que coinciden con la búsqueda");
    await p.fill("#gbQ", "tsh"); ok(await p.locator("dialog[open] .gb-fila:visible").count() >= 1 && /Hormona estimulante/.test(await p.innerText("dialog[open] .gb-fila:visible")), "busca por sigla (TSH)");
    await p.fill("#gbQ", "hemoglobina glicosilada"); ok(await p.locator("dialog[open] .gb-fila:visible").count() >= 1, "busca varias palabras a la vez");
    await p.fill("#gbQ", "creatinina serica"); ok(await p.locator("dialog[open] .gb-fila:visible").count() >= 1, "la búsqueda ignora los acentos");
    await p.fill("#gbQ", "zzzxxx"); ok(await p.locator("#gbV").isVisible() && await p.locator("dialog[open] .gb-area:visible").count() === 0, "sin coincidencias se avisa y se ocultan las áreas");
    await p.fill("#gbQ", ""); ok(await p.locator("dialog[open] .gb-area:visible").count() === nAreas && await p.locator("dialog[open] .gb-area[open]").count() === 0, "al limpiar la búsqueda vuelven todas las áreas plegadas");
    ok(!/PMID|doi|http|bibliograf/i.test(await p.innerText("dialog[open] .gb")), "la biblioteca no muestra bibliografía ni enlaces");
    await p.focus("dialog[open] [data-cerrar]"); await p.keyboard.press("Escape"); ok(await p.locator("dialog[open]").count() === 0 && await p.evaluate(() => document.activeElement && document.activeElement.id === "ghLab"), "Esc cierra y devuelve el foco al acceso");
    await p.click("#ghFu"); await p.waitForSelector("dialog[open] .gh-fu"); const nFu = await p.locator("dialog[open] .gh-fu").count();
    const unicas = new Set(); GC.concat(CC).forEach(c => c.referencias.forEach(r => unicas.add(r.pmid ? "p" + r.pmid : r.doi ? "d" + r.doi : r.url ? "u" + r.url : "t" + r.titulo)));
    ok(nFu === unicas.size, "las fuentes listadas coinciden con las referencias reales de los casos (" + nFu + ")"); ok(/NTS 240|Norma Técnica/.test(await p.innerText("dialog[open]")), "incluye normas peruanas");
    await p.click('dialog[open] a[href^="#/guardia/g"] >> nth=0'); await p.waitForSelector("#gdEmpezar"); ok(await p.locator("dialog[open]").count() === 0, "un enlace de fuente abre el caso y cierra el diálogo");
    await hub(p); await p.click('a.gh-acc[href="#/feynman"]'); await p.waitForSelector("#fyRaiz"); ok(/#\/feynman/.test(p.url()), "el tutor Feynman abre su pantalla existente");
    /* ---- con progreso real ---- */
    const ctx2 = await navegador.newContext({ viewport: { width: 1536, height: 1024 } }); await ctx2.addInitScript(INIT);
    const ids = GC.slice(0, 4).map(c => c.id), mejor = [80, 60, 100, 40]; const gp = { casos: {} }; ids.forEach((id, i) => { gp.casos[id] = { mejor: mejor[i], intentos: 1, completados: 1, ultimo: mejor[i], final: "bueno", criticos: i === 1 ? 2 : 0, t: Date.now() }; });
    const cp = { casos: { [CC[0].id]: { mejor: 90, intentos: 1, ultimo: 90, t: Date.now() } } };
    const resp = {}; for (let i = 0; i < 40; i++) resp["x" + i] = { ok: i % 3 === 0, t: Date.now() };
    await ctx2.addInitScript(([g, c]) => { const k = "mqp_progreso_v1"; const d = { v: 1, respuestas: {}, favoritos: {}, sesiones: [], ultima: null, preferencias: { guardia: g, consulta: c }, borrados: {}, reinicioGlobal: 0 }; if (!localStorage.getItem("__sembrado")) { localStorage.setItem(k, JSON.stringify(d)); localStorage.setItem("__sembrado", "1"); } }, [gp, cp]);
    const p2 = await nueva(ctx2); await hub(p2);
    ok(/4 de 10 casos completados/.test(await p2.innerText(".gh-card--rojo")) && /70 %/.test(await p2.innerText(".gh-card--rojo")), "progreso real de emergencias: 4 de 10 y mejor puntaje medio 70 %");
    ok(/1 de 4 consultas completadas/.test(await p2.innerText(".gh-card--azul")) && /90 %/.test(await p2.innerText(".gh-card--azul")), "progreso real de consulta: 1 de 4 y 90 %");
    const est = await p2.innerText(".gh-est"), media = Math.round((80 + 60 + 100 + 40 + 90) / 5);
    ok(new RegExp(media + " %").test(est) && /4 \/ 10/.test(est) && /1 \/ 4/.test(est) && /3 \/ 4/.test(est), "estadísticas: puntaje medio " + media + " %, 4/10, 1/4 y 3/4 sin errores críticos");
    await ctx2.close();
    /* ---- responsive ---- */
    for (const [nom, w, h] of [["tableta", 820, 1100], ["móvil", 390, 844], ["móvil pequeño", 320, 700], ["laptop pequeña", 1180, 800], ["laptop", 1366, 768], ["pantalla grande", 1920, 1080]]) {
      const c = await navegador.newContext({ viewport: { width: w, height: h }, isMobile: w < 800 }); await c.addInitScript(INIT); const q = await nueva(c);
      await hub(q); await scrollTodo(q);
      ok(await q.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), nom + " (" + w + " px): sin desplazamiento horizontal");
      const cajas = await q.locator(".gh-card").evaluateAll(l => l.map(e => { const r = e.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width)]; }));
      if (w >= 820) ok(cajas[0][1] === cajas[1][1] && cajas[2][1] === cajas[3][1] && cajas[2][1] > cajas[0][1], nom + ": cuatro tarjetas en cuadrícula 2×2");
      if (w < 640) ok(cajas.every(c2 => c2[0] === cajas[0][0]) && cajas.every((c2, i) => i === 0 || c2[1] > cajas[i - 1][1]), nom + ": tarjetas apiladas");
      const cortado = await q.evaluate(() => [].some.call(document.querySelectorAll(".gh h2, .gh h1, .gh-btn, .gh-acc__t b, .gh-card__sobre p, .gh-datos dd, .gh-prog p, .gh-rec__c b"), e => e.scrollWidth > e.clientWidth + 1) || [].some.call(document.querySelectorAll(".gh-card"), c => { const r = c.getBoundingClientRect(); return [].some.call(c.querySelectorAll("*"), e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.right > r.right + 1 && !e.closest(".gh-card__foto img"); }); })); ok(!cortado, nom + ": sin textos cortados en títulos y botones");
      const peq = await q.evaluate(() => [].filter.call(document.querySelectorAll(".gh a.gh-btn, .gh button, .gh a.gh-acc, .gh a.gh-rec__a, .gh .gh-link"), e => { const r = e.getBoundingClientRect(); return r.width > 0 && (r.height < 40 || r.width < 40); }).length); ok(peq === 0, nom + ": objetivos táctiles de al menos 40 px");
      if (shots) await q.screenshot({ path: path.join(shots, "hub-" + nom.replace(/\s/g, "-") + ".png"), fullPage: true });
      await c.close();
    }
    /* ---- teclado ---- */
    await hub(p); await p.keyboard.press("Shift"); await p.focus(".gh-card--rojo a.gh-btn"); const foco = await p.evaluate(() => { const e = document.activeElement, s = getComputedStyle(e); return s.outlineStyle !== "none" && parseFloat(s.outlineWidth) >= 2; }); ok(foco, "el foco del teclado es visible en los botones de modalidad");
    await p.keyboard.press("Enter"); await p.waitForSelector(".gd-caso"); ok(/emergencias/.test(p.url()), "Enter activa el botón de modalidad");
    /* ---- accesibilidad ---- */
    if (process.env.AXE_PATH) {
      const axe = fs.readFileSync(process.env.AXE_PATH, "utf8");
      for (const esq of ["light", "dark"]) for (const [nom, w] of [["escritorio", 1536], ["móvil", 390]]) {
        const c = await navegador.newContext({ viewport: { width: w, height: 900 }, colorScheme: esq }); await c.addInitScript(INIT); const q = await nueva(c);
        for (const ruta of ["#/guardia", "#/guardia/emergencias", "#/consulta"]) {
          await q.goto(base + "app/" + ruta); await q.waitForSelector(".gh-hero, .gh-modal"); if (ruta === "#/guardia") await cerrarIntro(q); await scrollTodo(q); await dormir(700);
          await q.evaluate(axe); const v = await q.evaluate(async () => (await axe.run(document.querySelector("#vista") || document.body, { runOnly: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] })).violations.map(x => x.id + ":" + x.nodes.length + " " + x.nodes.slice(0, 2).map(n => (n.target || []).join(" ")).join(" | ")));
          ok(v.length === 0, "axe " + esq + " " + nom + " " + ruta + ": " + v.join(" ; "));
          if (ruta === "#/guardia") {
            await q.click("#ghLab"); await q.waitForSelector("dialog[open] .gb-area"); await q.click("dialog[open] .gb-area >> nth=0 >> summary"); await q.click("dialog[open] .gb-area >> nth=3 >> summary"); await dormir(400);
            const vb = await q.evaluate(async () => (await axe.run(document.querySelector("dialog[open]"), { runOnly: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] })).violations.map(x => x.id + ":" + x.nodes.length + " " + x.nodes.slice(0, 2).map(n => (n.target || []).join(" ")).join(" | ")));
            ok(vb.length === 0, "axe " + esq + " " + nom + " biblioteca de laboratorio: " + vb.join(" ; ")); await q.keyboard.press("Escape"); await q.evaluate(() => { const d = document.querySelector("dialog[open]"); if (d) d.querySelector("[data-cerrar]").click(); });
          }
        }
        await c.close();
      }
    }
    ok(errores.length === 0, "sin errores de consola/página: " + errores.slice(0, 3).join(" | "));
    ok(malas.length === 0, "sin respuestas 4xx/5xx de recursos propios: " + malas.slice(0, 3).join(" | "));
    ok(externas.length === 0, "sin peticiones externas: " + externas.slice(0, 3).join(" | "));
  } finally { await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true }); }
  console.log(fallos ? "FALLARON " + fallos + " de " + total : "OK: " + total + " comprobaciones E2E del centro de simulación"); process.exit(fallos ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
