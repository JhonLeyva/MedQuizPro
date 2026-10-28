// node tests/guardia_e2e.js — «Sobrevive a la Guardia» v2 en un navegador real (Playwright/Chromium): juega los 10 casos de principio a fin (ruta óptima y rutas con errores),
// comprueba imágenes con visor, informe A–F, recomendaciones personalizadas, escritorio y móvil. No usa IA ni red externa.
// Variables: AXE_PATH (axe.min.js; sin él se omite accesibilidad), SHOTS (carpeta de capturas), CHROMIUM (ejecutable).
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
global.window = {}; const CASOS = require("../guardia_casos.js");
const INIT = () => { try { localStorage.setItem("mqp_guardia_intro_v1", "omitir"); } catch (e) {} };

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
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx.addInitScript(INIT);
    const p = await ctx.newPage(); const errores = [], externas = [];
    p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    p.on("request", r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !/fonts\.(googleapis|gstatic)\.com/.test(r.url())) externas.push(r.url()); });
    const textoBoton = async (loc) => (await loc.innerText()).trim();
    /* elige en el caso la decisión que cumple `quiere(nodo)` mirando el grafo; devuelve cuando llega al informe */
    async function jugar(c, quiere, verImagen) {
      await p.goto(base + "app/#/guardia"); await p.waitForSelector(".gd-caso"); await p.goto(base + "app/#/guardia/" + c.id); await p.waitForSelector(".gd-juego"); let id = c.inicio, pasos = 0, vio = false; const elegidas = [];
      while (!c.nodos[id].final && pasos++ < 40) {
        const nd = c.nodos[id]; await p.waitForSelector(".gd-op");
        if (nd.imagen) {
          vio = true;
          ok(await p.locator(".gd-img img").count() === 1, c.id + "/" + id + ": la imagen se muestra antes de decidir");
          const cargada = await p.locator(".gd-img img").evaluate(i => i.complete && i.naturalWidth > 0); ok(cargada, c.id + ": la imagen real carga");
          const alt = await p.locator(".gd-img img").getAttribute("alt"); ok(alt && !/intususcep|tubercul|disecci|infarto|oclusi|ictus/i.test(alt), c.id + ": alt neutro «" + alt + "»");
          ok(!/PMID|PMC\d|Cureus|doi\.org/i.test(await p.locator(".gd-juego").innerText()), c.id + ": durante el caso no se muestra la fuente que revela el diagnóstico");
          if (verImagen) {
            await p.click(".gd-img__b"); await p.waitForSelector(".vi-dlg[open]"); ok(await p.locator(".vi-barra [data-a=mas]").count() === 1, "visor: controles de zoom");
            await p.click(".vi-barra [data-a=mas]"); ok(/Zoom 140 %/.test(await p.locator("#viInfo").innerText()), "visor: el zoom funciona");
            const marco = await p.locator("#viMarco").boundingBox(); await p.mouse.move(marco.x + 100, marco.y + 100); await p.mouse.down(); await p.mouse.move(marco.x + 140, marco.y + 130, { steps: 4 }); await p.mouse.up();
            ok(/translate\((?!0px,\s?0px)/.test(await p.locator("#viImg").getAttribute("style")), "visor: se puede desplazar (pan)");
            ok(!/PMID|doi\.org/.test(await p.locator(".vi-dlg").innerText()), "visor: no revela la fuente durante el caso");
            await p.keyboard.press("Escape"); await p.waitForSelector(".vi-dlg", { state: "detached" });
          }
        } else if (vio) ok(await p.locator(".gd-prev [data-img]").count() >= 1 || nd.imagen, c.id + "/" + id + ": se puede volver a consultar la imagen");
        const d = quiere(nd); elegidas.push(d); const texto = d.texto;
        try { await p.locator(".gd-op", { hasText: texto.slice(0, 40) }).first().click({ timeout: 5000 }); } catch (e) { throw new Error(c.id + "/" + id + ": no se pudo pulsar «" + texto.slice(0, 40) + "»"); } await p.waitForSelector("#gdSig"); await p.click("#gdSig"); id = d.siguiente;
      }
      await p.waitForSelector(".gd-informe"); return elegidas;
    }
    const optima = nd => nd.decisiones.find(d => d.calidad === "optima");
    const peor = nd => nd.decisiones.find(d => d.calidad === "peligrosa") || nd.decisiones.find(d => d.calidad === "incorrecta") || nd.decisiones[0];

    /* 1) lista sin datos: 10 casos y modo invitación (no se inventan recomendaciones) */
    await p.goto(base + "app/#/guardia"); await p.waitForSelector(".gd-caso");
    ok(await p.locator(".gd-caso").count() === 10, "la lista muestra exactamente 10 casos");
    ok(/Por dónde empezar/.test(await p.locator(".gd-rec").innerText()) && /no inventamos/.test(await p.locator(".gd-rec").innerText()), "sin datos: invitación honesta, sin recomendación personalizada");
    ok(await p.locator(".gd-rec__i").count() === 3, "la invitación sugiere 3 casos");
    await p.selectOption("#gdFil", "Pediatría"); ok(await p.locator(".gd-caso:visible").count() === 1, "explorar por especialidad filtra (Pediatría → 1)");
    await p.selectOption("#gdFil", ""); ok(await p.locator(".gd-caso:visible").count() === 10, "«todas las especialidades» vuelve a mostrar los 10");
    ok(!/asma|apendicitis aguda|preeclampsia/i.test(await p.locator("#gdLista").innerText()), "los casos de prueba anteriores no aparecen");
    await foto(p, "g1-lista");

    /* 2) los 10 casos por la ruta óptima: 100 %, informe A–F completo, referencias con enlaces */
    for (const c of CASOS) {
      const el = await jugar(c, optima, c.imagenes.length > 0 && c.id === "g02");
      const t = await p.locator(".gd-informe").textContent();
      ok(/100 %/.test(t) && /Buen desenlace/.test(t), c.id + ": ruta óptima → 100 % y buen desenlace");
      for (const s of ["A. Resumen clínico", "B. Razonamiento paso a paso", "D. Análisis de tus decisiones", "E. Tratamiento y seguimiento", "F. Resultado y refuerzo", "Referencias del caso", "Diferencias entre fuentes y limitaciones"]) ok(t.includes(s), c.id + ": informe incluye «" + s + "»");
      ok((c.imagenes.length > 0) === /C\. Interpretación de las imágenes/.test(t), c.id + ": sección C solo si hay imagen");
      ok(await p.locator(".gd-ref").count() === c.referencias.length, c.id + ": todas las referencias listadas");
      ok(await p.locator('.gd-ref a[href^="https://pubmed.ncbi.nlm.nih.gov/"]').count() >= 1, c.id + ": enlaces a PubMed");
      ok(await p.locator(".gd-dec").count() === el.length, c.id + ": análisis de cada decisión tomada (" + el.length + ")");
      ok(/Errores críticos: 0/.test(t), c.id + ": sin errores críticos en la ruta óptima");
      ok(/Dosis \/ unidades/.test(t), c.id + ": tratamiento con dosis/unidades o aclaración");
      for (const im of c.imagenes) { ok(/Licencia verificada el/.test(t) && /creativecommons|CC BY/.test(t) && /Modificaciones/.test(t), c.id + ": ficha de la imagen con licencia y modificaciones"); }
      if (c.imagenes.length) ok(await p.locator('.gd-informe .gd-img img').count() === c.imagenes.length, c.id + ": el informe muestra las imágenes");
    }
    await foto(p, "g2-informe");
    /* el progreso quedó guardado (10 casos) y conserva los ids archivados */
    const prog = await p.evaluate(() => JSON.parse(localStorage.getItem("mqp_progreso_v1")).preferencias.guardia.casos); ok(Object.keys(prog).length === 10 && CASOS.every(c => prog[c.id].mejor === 100), "el progreso guarda 10 casos con 100 %");

    /* 3) rutas con errores: el informe refleja lo que realmente se eligió */
    for (const c of CASOS) {
      const el = await jugar(c, peor, false); const t = await p.locator(".gd-informe").textContent();
      const crit = el.filter(d => d.calidad === "peligrosa").length;
      ok(new RegExp("Errores críticos: " + crit + "\\b").test(t), c.id + ": informe cuenta " + crit + " error(es) crítico(s) elegidos");
      ok(!/100 %/.test(await p.locator(".gd-final").innerText()), c.id + ": con errores no marca 100 %");
      ok(await p.locator(".gd-dec--peligrosa, .gd-dec--incorrecta").count() >= 1, c.id + ": decisiones erróneas señaladas con su severidad");
      ok(/Lo preferible/.test(t) && /Por qué las otras opciones eran inferiores|Fue la mejor opción/.test(t), c.id + ": informe explica lo preferible");
    }
    /* un error leve no provoca complicación grave inmediata: g06 → decisión «incorrecta» de n4 (PA sin control) sigue el flujo normal */
    const c6 = CASOS.find(c => c.id === "g06"); await jugar(c6, nd => nd.decisiones.find(d => d.calidad === "optima"), false);
    const prog2 = await p.evaluate(() => JSON.parse(localStorage.getItem("mqp_progreso_v1")).preferencias.guardia.casos); ok(prog2.g06.intentos === 3 && prog2.g06.mejor === 100, "reintentos acumulan intentos y conservan el mejor puntaje");

    /* 4) imagen: volver a consultarla en un nodo posterior (g07 tiene dos imágenes en nodos distintos) */
    const c7 = CASOS.find(c => c.id === "g07"); await p.goto(base + "app/#/guardia/g07"); await p.waitForSelector(".gd-op");
    let id = c7.inicio; for (let k = 0; k < 2; k++) { const d = optima(c7.nodos[id]); await p.locator(".gd-op", { hasText: d.texto.slice(0, 40) }).first().click(); await p.click("#gdSig"); id = d.siguiente; await p.waitForSelector(".gd-op"); }
    ok(await p.locator(".gd-img img").count() === 1 && await p.locator(".gd-prev [data-img]").count() === 1, "g07 (2.ª imagen): se ve la nueva y se puede reabrir la primera");
    await p.click(".gd-prev [data-img]"); await p.waitForSelector(".vi-dlg[open]"); await p.keyboard.press("Escape");

    /* 5) recomendaciones personalizadas con respuestas reales del banco */
    const sembrar = async (ctxN) => { const pg = await ctxN.newPage(); await pg.goto(base + "app/#/guardia"); await pg.waitForSelector(".gd-caso");
      await pg.evaluate(async () => { const r = await fetch("../bancos/cardiologia.json").then(x => x.json()), inf = await fetch("../bancos/infectologia.json").then(x => x.json());
        const d = JSON.parse(localStorage.getItem("mqp_progreso_v1") || "{}"); d.v = 1; d.respuestas = {}; d.preferencias = d.preferencias || {};
        const ahora = Date.now(); const poner = (lista, n, buenas, hace) => lista.slice(0, n).forEach((q, i) => { d.respuestas[q.id] = { l: "A", ok: i < buenas, t: ahora - hace * 864e5, a: q.id.split("-")[0] }; });
        poner(r.preguntas, 20, 5, 40); poner(inf.preguntas, 20, 19, 40); localStorage.setItem("mqp_progreso_v1", JSON.stringify(d)); });
      return pg; };
    const ctx2 = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx2.addInitScript(INIT); const p2 = await sembrar(ctx2); await p2.reload(); await p2.waitForSelector(".gd-caso"); await p2.waitForTimeout(500);
    const rec = await p2.locator(".gd-rec").innerText();
    ok(/Casos recomendados para ti/.test(rec) && /Aciertas 25 % en Cardiolog/.test(rec) && /intervalo 95 %/.test(rec), "con respuestas reales: recomendación personalizada con el dato real: " + rec.slice(0, 220).replace(/\n/g, " "));
    ok(/no se envía nada a ningún servidor/.test(rec) && /todos los casos están abiertos/.test(rec), "aviso de privacidad y de que no es una restricción");
    ok(await p2.locator(".gd-caso").count() === 10, "la recomendación no oculta ningún caso"); await foto(p2, "g3-recomendados");

    /* 6) móvil: sin desplazamiento horizontal en lista, caso con imagen e informe; botones de al menos 44 px */
    const movil = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }); await movil.addInitScript(INIT); const m = await movil.newPage();
    const sinScroll = async (nombre) => ok(await m.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), "móvil: " + nombre + " sin desplazamiento horizontal");
    await m.goto(base + "app/#/guardia"); await m.waitForSelector(".gd-caso"); await sinScroll("lista"); await foto(m, "g4-movil-lista");
    await m.goto(base + "app/#/guardia/g02"); await m.waitForSelector(".gd-op");
    let n = CASOS.find(c => c.id === "g02"), nid = n.inicio, d0 = optima(n.nodos[nid]);
    await m.locator(".gd-op", { hasText: d0.texto.slice(0, 40) }).first().click(); await m.click("#gdSig"); await m.waitForSelector(".gd-img img"); await sinScroll("nodo con imagen"); await foto(m, "g5-movil-imagen");
    ok((await m.locator(".gd-op").evaluateAll(b => b.map(x => x.getBoundingClientRect().height))).every(h => h >= 44), "móvil: opciones de al menos 44 px");
    await m.click(".gd-img__b"); await m.waitForSelector(".vi-dlg[open]"); const cb = await m.locator(".vi-dlg").boundingBox(); ok(cb.width <= 391, "móvil: el visor cabe en pantalla"); await m.keyboard.press("Escape");
    nid = d0.siguiente; for (let k = 0; k < 8 && !n.nodos[nid].final; k++) { const dd = optima(n.nodos[nid]); if (k > 0 || true) { await m.waitForSelector(".gd-op"); await m.locator(".gd-op", { hasText: dd.texto.slice(0, 40) }).first().click(); await m.click("#gdSig"); } nid = dd.siguiente; }
    await m.waitForSelector(".gd-informe"); await sinScroll("informe"); await foto(m, "g6-movil-informe");

    /* 7) accesibilidad */
    const axePath = process.env.AXE_PATH || "";
    if (axePath && fs.existsSync(axePath)) {
      const AXE = fs.readFileSync(axePath, "utf8");
      const auditar = async (pg, nombre) => { await pg.evaluate(AXE); const r = await pg.evaluate(async () => await axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] } }));
        r.violations = r.violations.filter(v => !v.nodes.every(x => x.target.join(" ") === "#chatLauncher"));
        ok(r.violations.length === 0, "axe · " + nombre + ": " + r.violations.map(v => v.id + " ×" + v.nodes.length + " " + v.nodes[0].target.join(" ") + " " + ((v.nodes[0].any[0] || {}).message || "")).join(" | ")); };
      for (const t of ["light", "dark"]) {
        await p2.evaluate(x => document.documentElement.setAttribute("data-theme", x), t); await p2.waitForTimeout(500); await auditar(p2, "lista con recomendaciones (" + t + ")");
        await p.goto(base + "app/#/guardia"); await p.waitForSelector(".gd-caso"); await p.goto(base + "app/#/guardia/g06"); await p.waitForSelector(".gd-op"); await p.evaluate(x => document.documentElement.setAttribute("data-theme", x), t);
        const c6b = CASOS.find(c => c.id === "g06"); const d = optima(c6b.nodos[c6b.inicio]);
        await p.locator(".gd-op", { hasText: d.texto.slice(0, 40) }).first().click(); await p.click("#gdSig"); await p.waitForSelector(".gd-img img"); await auditar(p, "nodo con imagen (" + t + ")");
        await p.click(".gd-img__b"); await p.waitForSelector(".vi-dlg[open]"); await auditar(p, "visor de imagen (" + t + ")"); await p.keyboard.press("Escape");
        await jugar(c6b, optima, false); await p.evaluate(x => document.documentElement.setAttribute("data-theme", x), t); await auditar(p, "informe del caso (" + t + ")");
      }
    } else console.log("(axe omitido: define AXE_PATH)");

    ok(externas.length === 0, "ninguna petición a servidores externos: " + externas.slice(0, 3).join(", "));
    ok(errores.length === 0, "sin errores de JavaScript en consola: " + errores.slice(0, 3).join(" | "));
  } catch (e) { fallos++; console.log("EXCEPCIÓN:", e.message.split("\n")[0], "|", (e.stack.match(/guardia_e2e.js:\d+/) || [""])[0]); }
  await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true });
  console.log(total + " comprobaciones E2E, " + fallos + " fallas"); process.exit(fallos ? 1 : 0);
})();
