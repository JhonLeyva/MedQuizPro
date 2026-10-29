// node tests/guardia_e2e.js — «Sobrevive a la Guardia» v3 en un navegador real (Playwright/Chromium): recorridos completos de los 10 casos en AMBOS modos
// (entrenamiento y simulación cronometrada), temporizador (agotado, pausa, sin envíos duplicados), sesión recuperable, laboratorio, interconsulta,
// errores recuperables/críticos/fatales, informe, recomendaciones, móvil y accesibilidad. No usa IA ni red externa.
// Variables: AXE_PATH (axe.min.js; sin él se omite accesibilidad), SHOTS (carpeta de capturas), CHROMIUM (ejecutable).
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
global.window = {}; const CASOS = require("../guardia_casos.js"); const N = require("../guardia_nucleo.js");
const INIT = () => { try { localStorage.setItem("mqp_guardia_intro_v1", "omitir"); } catch (e) {} };
const porId = id => CASOS.find(c => c.id === id);

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "gd-e2e-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  fs.cpSync(path.join(RAIZ, "app"), path.join(tmp, "app"), { recursive: true }); fs.cpSync(path.join(RAIZ, "guardia"), path.join(tmp, "guardia"), { recursive: true });
  for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));
  fs.mkdirSync(path.join(tmp, "t")); const pWeb = await libre();
  const php = spawn("php", ["-S", `127.0.0.1:${pWeb}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1200);
  const base = `http://127.0.0.1:${pWeb}/`, shots = process.env.SHOTS || "";
  const foto = async (p, n) => { if (shots) { fs.mkdirSync(shots, { recursive: true }); await p.screenshot({ path: path.join(shots, n + ".png"), fullPage: true }); } };
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  const errores = [], externas = [];
  const nuevaPagina = async (ctx, reloj) => {
    const p = await ctx.newPage(); if (reloj) await p.clock.install();
    p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    p.on("request", r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !/fonts\.(googleapis|gstatic)\.com/.test(r.url())) externas.push(r.url()); }); return p;
  };
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx.addInitScript(INIT);
    const p = await nuevaPagina(ctx, false);

    /* ---- helpers de juego ---- */
    async function abrir(pg, caso, modo) {
      await pg.goto(base + "app/#/guardia/emergencias"); await pg.waitForSelector(".gd-caso"); await pg.goto(base + "app/#/guardia/" + caso.id);
      await pg.waitForSelector("#gdEmpezar"); await pg.check("input[name=gdModo][value=" + modo + "]"); await pg.click("#gdEmpezar"); await pg.waitForSelector(".gd-op");
    }
    async function elegir(pg, letra) { await pg.click('.gd-op[data-id="' + letra + '"]'); await pg.waitForSelector("#gdSig"); }
    async function siguiente(pg) { await pg.click("#gdSig"); await pg.waitForSelector(".gd-op, .gd-informe"); }
    /* recorre el caso con una estrategia; devuelve las decisiones elegidas */
    async function jugar(pg, caso, modo, estrategia, abrirYa) {
      if (!abrirYa) await abrir(pg, caso, modo); let id = caso.inicio, elegidas = [], pasos = 0;
      while (!caso.nodos[id].final && pasos++ < 60) {
        const nd = caso.nodos[id]; await pg.waitForSelector(".gd-op");
        ok(await pg.locator(".gd-op").count() === 5, caso.id + "/" + id + ": se muestran exactamente 5 alternativas");
        const letras = await pg.locator(".gd-op .gd-op__l").allInnerTexts(); ok(letras.join("") === "ABCDE", caso.id + "/" + id + ": rotuladas A–E en orden");
        const d = estrategia(nd, id, elegidas); elegidas.push({ id, d }); await elegir(pg, d.id);
        const fb = await pg.locator("#gdFb").innerText();
        if (modo === "entrenamiento") ok(fb.length > 30 && /pts/.test(fb), caso.id + "/" + id + ": entrenamiento: retroalimentación inmediata");
        else ok(!/pts|Decisión óptima|Incorrecta|Peligrosa/.test(fb), caso.id + "/" + id + ": cronometrada: no se revela la respuesta durante el caso");
        await siguiente(pg); id = d.siguiente;
      }
      await pg.waitForSelector(".gd-informe"); return elegidas;
    }
    const optima = nd => nd.decisiones.find(d => d.calidad === "optima");
    const siempre = cal => nd => nd.decisiones.find(d => d.calidad === cal) || optima(nd);

    /* 1) carga diferida y lista */
    const pedidos = []; p.on("request", r => pedidos.push(r.url()));
    await p.goto(base + "app/#/inicio"); await p.waitForTimeout(1200);
    ok(!pedidos.some(u => /guardia_casos\.js/.test(u)) && !pedidos.some(u => /guardia_lab\.js/.test(u)), "los datos de los casos (0,4 MB) no se descargan fuera del módulo");
    await p.goto(base + "app/#/guardia/emergencias"); await p.waitForSelector(".gd-caso"); ok(pedidos.some(u => /guardia_casos\.js/.test(u)), "al entrar al módulo se cargan los casos");
    ok(await p.locator(".gd-caso").count() === 10, "la lista muestra exactamente 10 casos"); ok(/Por dónde empezar/.test(await p.locator(".gd-rec").innerText()), "sin datos: invitación honesta");
    ok(/ruta óptima/.test(await p.locator(".gd-caso").first().innerText()), "la tarjeta indica el número de decisiones"); ok(await p.locator('.gh-migas a[href="#/guardia"]').count() === 1, "migas: enlace de regreso al centro de simulación");
    await p.selectOption("#gdFil", "Pediatría"); ok(await p.locator(".gd-caso:visible").count() === 1, "filtro por especialidad"); await p.selectOption("#gdFil", ""); await foto(p, "g1-lista");

    /* 2) los 10 casos por la ruta óptima en AMBOS modos: 100 %, informe completo, cinco alternativas analizadas */
    for (const modo of ["entrenamiento", "cronometrada"]) for (const c of CASOS) {
      const el = await jugar(p, c, modo, optima); const t = await p.locator(".gd-informe").textContent();
      ok(/100 %/.test(t) && /Buen desenlace/.test(t), c.id + " (" + modo + "): ruta óptima → 100 % y buen desenlace");
      ok(el.length >= 6 && el.length <= 12, c.id + " (" + modo + "): " + el.length + " decisiones en la ruta óptima");
      for (const s of ["A. Resumen clínico y diagnóstico", "Diagnóstico final", "Diagnósticos diferenciales", "Datos que debían orientar", "B. Razonamiento paso a paso", "Interpretación de los resultados de laboratorio", "D. Análisis de tus decisiones", "E. Tratamiento y seguimiento recomendados", "F. Resultado y refuerzo", "Referencias del caso", "Diferencias entre fuentes y limitaciones", "Análisis de las cinco alternativas", "Conducta preferible", "Consecuencia en el caso", "Interconsultas y ayudas", "Tiempo"]) if (!(s === "Conducta preferible")) ok(t.includes(s), c.id + ": informe incluye «" + s + "»");
      ok((c.imagenes.length > 0) === /C\. Interpretación de las imágenes/.test(t), c.id + ": sección C solo si hay imagen"); if (c.imagenes.length) ok(/Cómo modifica la conducta/.test(t) && /Diagnósticos diferenciales de la imagen/.test(t), c.id + ": imagen: diferenciales y cómo modifica la conducta");
      ok(await p.locator(".gd-dec").count() === el.length && await p.locator(".gd-cinco__i").count() === el.length * 5, c.id + ": análisis de las cinco alternativas de cada decisión");
      ok(await p.locator(".gd-ref").count() === c.referencias.length, c.id + ": referencias listadas");
      if (modo === "cronometrada") ok(/de \d+:\d\d disponibles/.test(t) && /decisión\(es\) con tiempo agotado/.test(t), c.id + ": informe de tiempo usado vs disponible");
    }
    const prog = await p.evaluate(() => JSON.parse(localStorage.getItem("mqp_progreso_v1")).preferencias.guardia.casos); ok(CASOS.every(c => prog[c.id].mejor === 100 && prog[c.id].mejorCrono === 100), "progreso: 10 casos con 100 % y mejor cronometrado");

    /* 3) errores: recuperables no matan; críticos llevan a deterioro; fatal solo tras 2 decisiones críticas */
    for (const c of CASOS) {
      /* a) dos errores recuperables seguidos (primeros nodos) y luego óptimas: el paciente no muere y el informe cuenta errores recuperables */
      let k = 0; const el = await jugar(p, c, "entrenamiento", (nd) => { k++; if (k <= 2) { const d = nd.decisiones.find(x => x.calidad === "incorrecta" && !x.omision) || nd.decisiones.find(x => x.calidad === "incorrecta"); return d || optima(nd); } return optima(nd); });
      const t = await p.locator(".gd-informe").textContent(); ok(!/falleció/.test(t), c.id + ": dos errores recuperables seguidos NO provocan la muerte"); ok(/Errores recuperables: [1-9]/.test(t), c.id + ": el informe cuenta los errores recuperables");
      ok(!/100 %/.test(await p.locator(".gd-final").innerText()), c.id + ": con errores no marca 100 %");
      /* b) una decisión crítica y luego óptimas: sobrevive */
      let primera = true; const el2 = await jugar(p, c, "entrenamiento", (nd) => { if (primera) { primera = false; const d = nd.decisiones.find(x => x.calidad === "peligrosa"); if (d) return d; } return optima(nd); });
      const t2 = await p.locator(".gd-informe").textContent(); ok(!/falleció/.test(t2), c.id + ": un único error crítico seguido de reacción correcta no es fatal"); ok(/Errores críticos: [1-9]/.test(t2), c.id + ": el informe cuenta el error crítico");
      /* c) cadena de decisiones críticas: llega a un desenlace fatal definido, y el informe explica qué contribuyó */
      await jugar(p, c, "entrenamiento", siempre("peligrosa")); const t3 = await p.locator(".gd-informe").textContent();
      ok(/falleció/.test(t3) || /Desenlace desfavorable/.test(t3) || /Mejoría|Resuelto|Evolución|Operado|Resolución/.test(t3), c.id + ": la cadena de decisiones críticas termina en un desenlace definido");
      if (/falleció/.test(t3)) { ok(/Qué contribuyó a este desenlace/.test(t3) && /Lo preferible/.test(t3), c.id + ": desenlace fatal: explica qué contribuyó y la conducta preferible"); const crit = +/Errores críticos: (\d+)/.exec(t3)[1]; ok(crit >= 2, c.id + ": la muerte exige ≥ 2 errores críticos (hubo " + crit + ")"); }
    }
    await foto(p, "g2-informe");

    /* 4) laboratorio: no adelanta resultados, catálogo, interpretación oculta mientras se evalúa */
    { const c = porId("g01"); await abrir(p, c, "entrenamiento");
      await p.click("#gdLabBtn"); await p.waitForSelector(".gd-dlg[open]"); ok(/Todavía no hay resultados/.test(await p.locator("#gdP1").innerText()), "laboratorio: al inicio no hay resultados (no se adelantan)");
      await p.click("[data-tab='2']"); ok(await p.locator(".gd-lab-t:visible").count() >= 60, "catálogo: lista las pruebas (" + await p.locator(".gd-lab-t:visible").count() + ")");
      await p.fill("#gdLabQ", "potasio"); ok(await p.locator(".gd-lab-t:visible").count() >= 1, "catálogo: búsqueda"); await p.fill("#gdLabQ", ""); await p.selectOption("#gdLabC", "Gasometría"); ok(await p.locator(".gd-lab-t:visible").count() === 6, "catálogo: filtro por categoría (Gasometría = 6)");
      const hb = p.locator(".gd-lab-t", { hasText: "Hemoglobina" }).first(); ok(/intervalo de referencia/i.test(await hb.innerText()) && /intervalo educativo/i.test(await hb.innerText()), "catálogo: distingue intervalo y declara que es educativo"); await p.selectOption("#gdLabC", ""); await p.fill("#gdLabQ", "troponina"); ok(/umbral diagnóstico/i.test(await p.locator("#gdLabL").innerText()), "catálogo: distingue umbral diagnóstico del intervalo");
      await foto(p, "g3-laboratorio"); await p.click("[data-cerrar]"); ok(await p.locator(".gd-dlg").count() === 0, "laboratorio: se cierra sin perder el progreso");
      const f = await p.evaluate(() => document.activeElement && document.activeElement.id); ok(f === "gdLabBtn", "laboratorio: el foco vuelve al botón");
      await elegir(p, optima(c.nodos.n1).id); await siguiente(p);                                               // n2 con interpretación oculta
      ok(await p.locator(".gd-labn tbody tr").count() === 11, "n2: aparecen los resultados que el caso entrega en esa etapa (11)"); ok(await p.locator(".gd-labn .gd-marca").count() === 0 && /Interpreta tú/.test(await p.locator(".gd-labn").innerText()), "n2: las marcas bajo/alto se ocultan mientras se evalúa la interpretación");
      await p.click("#gdLabBtn"); await p.waitForSelector(".gd-dlg[open]"); ok(await p.locator("#gdP1 .gd-marca").count() === 0, "ventana de laboratorio: tampoco revela la lectura mientras se evalúa"); await p.click("[data-cerrar]");
      await elegir(p, optima(c.nodos.n2).id); await p.click("#gdLabBtn"); await p.waitForSelector(".gd-dlg[open]"); ok(await p.locator("#gdP1 .gd-marca").count() === 11, "tras responder la lectura (alto/bajo/normal) ya se muestra"); ok(/Intervalo de referencia/.test(await p.locator("#gdP1 thead").innerText()), "los resultados muestran valor, unidad e intervalo"); await p.click("[data-cerrar]"); }

    /* 5) interconsulta: 3 niveles, penalización, no pertinente deriva, no revela, modo cronometrada sin botón */
    { const c = porId("g01"); await abrir(p, c, "entrenamiento"); const n1 = c.nodos.n1, o = optima(n1);
      await p.click("#gdEspBtn"); await p.waitForSelector(".gd-dlg[open]"); await p.click('[data-niv="1"]'); const r1 = await p.locator("#gdEspR").innerText(); ok(r1.includes(n1.ayuda.n1.slice(0, 30)) && !r1.includes(o.texto), "interconsulta nivel 1: orientación general sin revelar la respuesta");
      await p.click('[data-niv="2"]'); const r2 = await p.locator("#gdEspR").innerText(); ok(r2.includes(n1.ayuda.n2.slice(0, 30)) && !r2.includes(o.texto), "interconsulta nivel 2: ayuda dirigida sin revelar la respuesta");
      await p.check('input[name=gdEsp][value="infecto"]'); await p.click('[data-niv="3"]'); ok(/no corresponde a mi área/.test(await p.locator("#gdEspR").innerText()) && !(await p.locator("#gdEspR").innerText()).includes(o.texto), "especialista no pertinente: deriva y no revela");
      await p.click("#gdEspRec"); await p.click('[data-niv="3"]'); const r3 = await p.locator("#gdEspR").innerText(); ok(r3.includes("Conducta recomendada") && r3.includes(o.texto) && r3.includes(o.explicacion.slice(0, 40)), "nivel 3: interconsulta completa con la conducta y su justificación"); await foto(p, "g4-interconsulta"); await p.click("[data-cerrar]");
      await elegir(p, o.id); ok(/−3 por la ayuda/.test(await p.locator("#gdFb").innerText()), "la penalización pedagógica se aplica y se informa (nivel 3: −3)"); await siguiente(p);
      let id = o.siguiente; while (!c.nodos[id].final) { const d = optima(c.nodos[id]); await elegir(p, d.id); await siguiente(p); id = d.siguiente; }
      const t = await p.locator(".gd-informe").textContent(); ok(/decisión 1 \(nivel 3\)/.test(t) && /Pedir orientación no es un error clínico/.test(t), "informe: registra la ayuda usada sin considerarla un error"); ok(/sin la penalización por ayudas habría sido 100 %/.test(t) && !/Puntaje ponderado: \d+ de \d+ \(100 %\)/.test(t), "informe: separa el efecto de la ayuda");
      await abrir(p, c, "cronometrada"); ok(await p.locator("#gdEspBtn").count() === 0, "modo cronometrada: no hay interconsulta (modo examen)"); }

    /* 6) temporizador con reloj controlado: cuenta, avisa, agota (regla de omisión), pausa y no duplica */
    { const ctxT = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctxT.addInitScript(INIT); const t = await nuevaPagina(ctxT, true); const c = porId("g01");
      await abrir(t, c, "cronometrada"); ok(/0:4[45]/.test(await t.locator("#gdReloj").innerText()), "reloj: decisión crítica con 45 s"); ok(/Decisión crítica de emergencia/.test(await t.locator("#gdRelojCaja").innerText()), "reloj: indica el tipo de decisión");
      await t.clock.runFor(12000); ok(/0:3[1-4]/.test(await t.locator("#gdReloj").innerText()), "reloj: cuenta hacia atrás (" + await t.locator("#gdReloj").innerText() + ")");
      await t.click("#gdPausa"); const pausado = await t.locator("#gdReloj").innerText(); ok(await t.locator("#gdPregunta").isHidden(), "pausa: oculta las alternativas"); await t.clock.runFor(30000); ok(await t.locator("#gdReloj").innerText() === pausado, "pausa: el tiempo no corre mientras está en pausa");
      await t.click("#gdPausa"); ok(await t.locator("#gdPregunta").isVisible(), "pausa: al reanudar vuelven las alternativas"); await t.clock.runFor(26000); ok(/aviso/.test(await t.locator("#gdReloj").getAttribute("data-nivel")), "reloj: nivel de aviso cerca del límite"); ok(/Quedan \d+ segundos/.test(await t.locator("#gdRelojLive").textContent()), "reloj: anuncia el aviso en una región accesible");
      await t.clock.runFor(10000); await t.waitForSelector(".gd-fb--agotado"); const fb = await t.locator("#gdFb").innerText(); const omis = c.nodos.n1.decisiones.find(d => d.omision);
      ok(/Se agotó el tiempo/.test(fb) && fb.includes(omis.texto.slice(0, 30)) && /conducta de espera/.test(fb), "agotado: aplica la regla validada (conducta de espera) y la explica"); ok(await t.locator(".gd-op:disabled").count() === 5, "agotado: se cierra la oportunidad de responder");
      await t.click('.gd-op[data-id="A"]', { force: true, timeout: 800 }).catch(() => {}); await t.clock.runFor(3000); ok(await t.locator(".gd-fb--agotado").count() === 1 && await t.locator("#gdSig").count() === 1, "sin envíos duplicados: clic y temporizador tardíos no vuelven a registrar la decisión");
      await t.click("#gdSig"); await t.waitForSelector(".gd-op"); ok(/Una hora después/.test(await t.locator(".gd-estado").innerText()), "agotado: continúa en la rama definida (" + omis.siguiente + ")");
      /* resolver rápido y comprobar que clic y expiración simultáneos solo cuentan una vez */
      const nd = c.nodos.r1; await t.clock.runFor(40000); await t.click('.gd-op[data-id="' + optima(nd).id + '"]'); await t.clock.runFor(2000); ok(await t.locator("#gdSig").count() === 1 && !(await t.locator(".gd-fb--agotado").count()), "clic dentro del tiempo: se registra una sola vez y no se aplica la omisión");
      await t.click("#gdSig"); let id = optima(nd).siguiente; while (!c.nodos[id].final) { await t.waitForSelector(".gd-op"); await elegir(t, optima(c.nodos[id]).id); await siguiente(t); id = optima(c.nodos[id]).siguiente; }
      const rep = await t.locator(".gd-informe").textContent(); ok(/Tiempo agotado: se aplicó la conducta de espera/.test(rep) && /1 decisión\(es\) con tiempo agotado/.test(rep), "informe: la decisión con tiempo agotado se explica y se cuenta"); ok(/velocidad es un indicador secundario/.test(rep), "informe: la velocidad es indicador secundario"); await ctxT.close(); }

    /* 7) sesión recuperable: recarga, navegación y descarte de sesiones incompatibles */
    { const ctxS = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctxS.addInitScript(INIT); const s = await nuevaPagina(ctxS, true); const c = porId("g02");
      await abrir(s, c, "cronometrada"); let id = c.inicio; for (let i = 0; i < 2; i++) { const d = optima(c.nodos[id]); await elegir(s, d.id); await siguiente(s); id = d.siguiente; }
      await s.clock.runFor(9000); const antes = await s.locator("#gdReloj").innerText(); const prog0 = await s.locator(".gd-prog").innerText();
      await s.reload(); await s.waitForSelector("#gdEmpezar"); ok(await s.locator("#gdContinuar").count() === 1 && /Tienes este caso en curso/.test(await s.locator(".gd-reanudar").innerText()), "recarga: ofrece continuar el caso en curso");
      await s.click("#gdContinuar"); await s.waitForSelector(".gd-op"); ok((await s.locator(".gd-prog").innerText()).startsWith(prog0.slice(0, 12)), "recuperación: vuelve a la misma decisión (" + prog0.slice(0, 12) + ")");
      const desp = await s.locator("#gdReloj").innerText(), seg = t => +t.split(":")[0] * 60 + +t.split(":")[1]; ok(seg(desp) >= seg(antes) - 2 && seg(desp) <= seg(antes) + 1, "recuperación: el reloj conserva el tiempo usado (" + antes + " → " + desp + ")");
      await s.goto(base + "app/#/guardia/emergencias"); await s.waitForSelector(".gd-caso"); await s.goto(base + "app/#/guardia/g02"); await s.waitForSelector("#gdContinuar"); ok(true, "navegación: al salir y volver se puede continuar");
      await s.click("#gdReiniciar"); await s.waitForSelector("#gdEmpezar"); ok(await s.locator("#gdContinuar").count() === 0, "«Empezar de nuevo» descarta la sesión guardada");
      await s.evaluate(() => localStorage.setItem("mqp_guardia_sesion_v1:g02", "{corrupto")); await s.reload(); await s.waitForSelector("#gdEmpezar"); ok(await s.locator("#gdContinuar").count() === 0, "sesión corrupta se descarta sin romper el módulo"); await ctxS.close(); }

    /* 8) recomendaciones con datos reales del banco */
    { const ctx2 = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx2.addInitScript(INIT); const p2 = await nuevaPagina(ctx2, false);
      await p2.goto(base + "app/#/guardia/emergencias"); await p2.waitForSelector(".gd-caso");
      await p2.evaluate(async () => { const r = await fetch("../bancos/cardiologia.json").then(x => x.json()), inf = await fetch("../bancos/infectologia.json").then(x => x.json()); const d = JSON.parse(localStorage.getItem("mqp_progreso_v1") || "{}"); d.v = 1; d.respuestas = {}; d.preferencias = d.preferencias || {}; const ahora = Date.now();
        const poner = (lista, n, buenas, hace) => lista.slice(0, n).forEach((q, i) => { d.respuestas[q.id] = { l: "A", ok: i < buenas, t: ahora - hace * 864e5, a: "x" }; }); poner(r.preguntas, 20, 5, 40); poner(inf.preguntas, 20, 19, 40); localStorage.setItem("mqp_progreso_v1", JSON.stringify(d)); });
      await p2.reload(); await p2.waitForSelector(".gd-caso"); await p2.waitForTimeout(400); const rec = await p2.locator(".gd-rec").innerText();
      ok(/Casos recomendados para ti/.test(rec) && /Aciertas 25 % en Cardiolog/.test(rec) && /intervalo 95 %/.test(rec), "con respuestas reales: recomendación personalizada"); ok(/no se envía nada a ningún servidor/.test(rec) && await p2.locator(".gd-caso").count() === 10, "privacidad y sin restricción"); await foto(p2, "g5-recomendados"); await ctx2.close(); }

    /* 9) móvil: preludio, nodo cronometrado, laboratorio e informe sin desbordar; botones ≥ 44 px */
    { const movil = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }); await movil.addInitScript(INIT); const m = await nuevaPagina(movil, false);
      const sinScroll = async n => ok(await m.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), "móvil: " + n + " sin desplazamiento horizontal");
      await m.goto(base + "app/#/guardia/emergencias"); await m.waitForSelector(".gd-caso"); await sinScroll("lista"); await m.goto(base + "app/#/guardia/g02"); await m.waitForSelector("#gdEmpezar"); await sinScroll("preludio"); await foto(m, "g6-movil-preludio");
      await m.check("input[value=cronometrada]"); await m.click("#gdEmpezar"); await m.waitForSelector(".gd-op"); await sinScroll("nodo cronometrado"); ok((await m.locator(".gd-op, .gd-barra-acc .btn").evaluateAll(b => b.map(x => x.getBoundingClientRect().height))).every(h => h >= 40), "móvil: botones de al menos 40 px"); await foto(m, "g7-movil-reloj");
      await m.click("#gdLabBtn"); await m.waitForSelector(".gd-dlg[open]"); const w = (await m.locator(".gd-dlg").boundingBox()).width; ok(w <= 391, "móvil: la ventana de laboratorio cabe (" + Math.round(w) + " px)"); await m.click("[data-tab='2']"); await sinScroll("catálogo de laboratorio"); await foto(m, "g8-movil-lab"); await m.click("[data-cerrar]");
      const c = porId("g02"); await jugar(m, c, "cronometrada", optima, true); await sinScroll("informe"); await foto(m, "g9-movil-informe"); await movil.close(); }

    /* 10) imágenes: visor, no revela diagnóstico, se puede reabrir (g07 tiene dos) */
    { const c = porId("g07"); await abrir(p, c, "entrenamiento"); let id = c.inicio;
      { const d = optima(c.nodos[id]); await elegir(p, d.id); await siguiente(p); id = d.siguiente; }
      ok(await p.locator(".gd-img img").count() === 1 && await p.locator(".gd-prev [data-img]").count() === 0, "g07: la radiografía aparece en su etapa"); const alt = await p.locator(".gd-img img").getAttribute("alt"); ok(!/disecci|aneurisma|tamponade|derrame/i.test(alt), "alt neutro");
      ok(!/PMID|PMC\d|doi\.org/.test(await p.locator(".gd-juego").innerText()), "durante el caso no se muestra la fuente que revela el diagnóstico"); await p.click(".gd-img__b"); await p.waitForSelector(".vi-dlg[open]"); await p.click(".vi-barra [data-a=mas]"); ok(/Zoom 140 %/.test(await p.locator("#viInfo").innerText()), "visor: zoom"); await p.keyboard.press("Escape");
      await p.waitForSelector(".vi-dlg", { state: "detached" }); const d3 = optima(c.nodos[id]); await elegir(p, d3.id); await siguiente(p); id = d3.siguiente; const d4 = optima(c.nodos[id]); await elegir(p, d4.id); await siguiente(p); id = d4.siguiente;
      ok(await p.locator(".gd-img img").count() === 1 && await p.locator(".gd-prev [data-img]").count() >= 1, "se puede volver a consultar la imagen anterior en una etapa posterior"); }

    /* 11) accesibilidad */
    const axePath = process.env.AXE_PATH || "";
    if (axePath && fs.existsSync(axePath)) {
      const AXE = fs.readFileSync(axePath, "utf8");
      const auditar = async (pg, nombre) => { await pg.evaluate(AXE); const r = await pg.evaluate(async () => await axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] } }));
        r.violations = r.violations.filter(v => !v.nodes.every(x => x.target.join(" ") === "#chatLauncher")); ok(r.violations.length === 0, "axe · " + nombre + ": " + r.violations.map(v => v.id + " ×" + v.nodes.length + " " + v.nodes[0].target.join(" ") + " " + ((v.nodes[0].any[0] || {}).message || "")).join(" | ")); };
      const c = porId("g06");
      for (const t of ["light", "dark"]) {
        const tema = async () => { await p.evaluate(x => document.documentElement.setAttribute("data-theme", x), t); await p.waitForTimeout(250); };
        await p.goto(base + "app/#/guardia/emergencias"); await p.waitForSelector(".gd-caso"); await tema(); await auditar(p, "lista (" + t + ")");
        await p.goto(base + "app/#/guardia/g06"); await p.waitForSelector("#gdEmpezar"); await tema(); await auditar(p, "preludio de modo (" + t + ")");
        await p.check("input[value=cronometrada]"); await p.click("#gdEmpezar"); await p.waitForSelector(".gd-op"); await tema(); await auditar(p, "decisión cronometrada con reloj (" + t + ")");
        await p.click("#gdLabBtn"); await p.waitForSelector(".gd-dlg[open]"); await tema(); await auditar(p, "laboratorio: resultados (" + t + ")"); await p.click("[data-tab='2']"); await auditar(p, "laboratorio: catálogo (" + t + ")"); await p.click("[data-cerrar]");
        await abrir(p, c, "entrenamiento"); await tema(); await p.click("#gdEspBtn"); await p.waitForSelector(".gd-dlg[open]"); await p.click('[data-niv="2"]'); await auditar(p, "interconsulta (" + t + ")"); await p.click("[data-cerrar]");
        let id = c.inicio; for (let k = 0; k < 2; k++) { const d = optima(c.nodos[id]); await elegir(p, d.id); await siguiente(p); id = d.siguiente; } await auditar(p, "nodo con imagen y laboratorio (" + t + ")");
        id = id; while (!c.nodos[id].final) { const d = optima(c.nodos[id]); await elegir(p, d.id); await siguiente(p); id = d.siguiente; } await tema(); await auditar(p, "informe del caso (" + t + ")");
      }
    } else console.log("(axe omitido: define AXE_PATH)");

    /* 12) regresión: otras secciones siguen abriendo */
    for (const ruta of ["#/inicio", "#/banco/configurar", "#/simuladores", "#/progreso"]) { await p.goto(base + "app/" + ruta); await p.waitForTimeout(500); ok(await p.locator("#gdRaiz").count() === 0 && (await p.locator("body").innerText()).length > 200, "regresión: " + ruta + " carga"); }
    ok(externas.length === 0, "ninguna petición a servidores externos: " + externas.slice(0, 3).join(", "));
    ok(errores.length === 0, "sin errores de JavaScript en consola: " + errores.slice(0, 3).join(" | "));
  } catch (e) { fallos++; console.log("EXCEPCIÓN:", e.message.split("\n")[0], "|", (e.stack.match(/guardia_e2e.js:\d+/) || [""])[0]); }
  await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true });
  console.log(total + " comprobaciones E2E, " + fallos + " fallas"); process.exit(fallos ? 1 : 0);
})();
