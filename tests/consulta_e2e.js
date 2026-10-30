// node tests/consulta_e2e.js — «Consulta Clínica Experta» en un navegador real (Playwright/Chromium): recorridos completos de los 4 casos piloto
// (ideal y deficiente), pruebas no solicitadas que no se revelan, revisión previa al envío, bloqueo por prueba esencial omitida, sesión recuperable,
// informe con las cinco listas de pruebas, móvil y accesibilidad. No usa IA ni red externa. Variables: AXE_PATH, CHROMIUM.
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
global.window = {}; const CASOS = require("../consulta_casos.js"); const N = require("../consulta_nucleo.js");
const INIT = () => { try { localStorage.setItem("mqp_guardia_intro_v1", "omitir"); } catch (e) {} };
const letra = (q, cal) => q.decisiones.find(d => d.calidad === cal) || q.decisiones.find(d => d.calidad === "incorrecta");

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "cq-e2e-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  fs.cpSync(path.join(RAIZ, "app"), path.join(tmp, "app"), { recursive: true }); fs.cpSync(path.join(RAIZ, "guardia"), path.join(tmp, "guardia"), { recursive: true });
  for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));
  fs.mkdirSync(path.join(tmp, "t")); const pWeb = await libre();
  const php = spawn("php", ["-S", `127.0.0.1:${pWeb}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1200);
  const base = `http://127.0.0.1:${pWeb}/`;
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  const errores = [], externas = [];
  const nueva = async ctx => { const p = await ctx.newPage(); p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    p.on("request", r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !/fonts\.(googleapis|gstatic)\.com/.test(r.url())) externas.push(r.url()); }); return p; };
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } }); await ctx.addInitScript(INIT);
    const p = await nueva(ctx);
    const sig = async (pg, et) => { await pg.click('[data-sig="' + et + '"]'); await pg.waitForSelector("#cqTitulo"); };
    const abrir = async (pg, c, conservar) => { if (!conservar) { await pg.goto(base + "app/#/consulta"); await pg.evaluate(() => Object.keys(localStorage).filter(k => k.indexOf("mqp_consulta_sesion") === 0).forEach(k => localStorage.removeItem(k))); } await pg.goto(base + "app/#/consulta"); await pg.waitForSelector(".gd-caso"); await pg.goto(base + "app/#/consulta/" + c.id); await pg.waitForSelector("#cqTitulo"); };
    async function preguntar(pg, clave, ids) { for (const id of ids) { await pg.click('[data-pregunta="' + clave + ":" + id + '"]'); } }
    async function responder(pg, clave, c, cal) { const d = letra(c.preguntas[clave], cal); await pg.click('[data-mcq="' + clave + '"] [data-op="' + d.id + '"]'); await pg.waitForSelector('[data-mcq="' + clave + '"] .gd-fb'); return d; }
    async function recorrer(pg, c, perfil) {
      await abrir(pg, c); await sig(pg, "anamnesis");
      ok(/^(Niña|Niño|Mujer|Varón|Gestante|Adolescente) de \d/.test((await pg.innerText(".cq-pac__t")).trim()) && /^[A-ZÁÉÍÓÚÑ«¿¡]/.test((await pg.innerText(".cq-pac__m")).trim()), c.id + ": el paciente se presenta con título en mayúscula («" + (await pg.innerText(".cq-pac__t")).trim() + "») y el motivo en una cita ordenada");
      const an = N.aplanar(c).map(q => q.id), claveAn = N.aplanar(c).filter(q => q.relevancia === "clave").map(q => q.id);
      await preguntar(pg, "anamnesis", perfil === "ideal" ? an : claveAn.slice(0, 1)); await sig(pg, "antecedentes");
      const ant = c.antecedentes.map(a => a.id); await preguntar(pg, "antecedentes", perfil === "ideal" ? ant : []); await sig(pg, "examen");
      const ex = c.examen.map(x => x.id); await preguntar(pg, "examen", perfil === "ideal" ? ex : []);
      if (perfil === "ideal") ok((await pg.textContent(".cq-cuerpo")).includes(c.examen[0].hallazgo.slice(0, 20)), c.id + ": el hallazgo aparece tras realizar la maniobra");
      await sig(pg, "hipotesis");
      const principal = c.hipotesis.opciones.find(o => o.tipo === "principal"), difs = c.hipotesis.opciones.filter(o => o.tipo === "diferencial");
      if (perfil === "ideal") { await pg.check('[data-hip="' + principal.id + '"]'); await pg.check('[data-hip="' + difs[0].id + '"]'); await pg.check('input[name=cqPrin][value="' + principal.id + '"]'); }
      else { await pg.click('[data-sig="pruebas"]'); ok(await pg.isVisible(".gd-alerta"), c.id + ": exige al menos una hipótesis y la principal"); await pg.check('[data-hip="' + difs[0].id + '"]'); }
      await sig(pg, "pruebas");
      const quiere = perfil === "ideal" ? c.pruebas.filter(t => t.clasificacion === "prioritaria" || t.clasificacion === "razonable") : c.pruebas.filter(t => t.clasificacion === "danina" || t.clasificacion === "innecesaria").slice(0, 2);
      for (const t of quiere) await pg.check('[data-prueba="' + t.id + '"]');
      await pg.click("#cqRevisar"); await pg.waitForSelector("dialog[open] #cqEnviar");
      ok((await pg.textContent("dialog[open]")).includes(quiere[0] ? quiere[0].nombre : "No marcaste"), c.id + ": la revisión lista lo marcado");
      await pg.click("#cqEnviar");
      const bloq = N.bloqueos(c, quiere.map(t => t.id));
      if (bloq.length) { await pg.waitForSelector(".gd-alerta[role=alert]"); ok((await pg.textContent(".gd-alerta")).includes(bloq[0].mensaje_bloqueo.slice(0, 30)), c.id + ": avisa de la prueba esencial omitida");
        await pg.click("#cqRevisar"); await pg.waitForSelector("#cqEnviar"); await pg.click("#cqEnviar"); }
      await pg.waitForSelector('[data-mcq="interpretacion"]');
      const txt = await pg.textContent(".cq-cuerpo");
      for (const t of c.pruebas.filter(t => !quiere.includes(t) && t.resultado.tipo === "texto")) ok(!txt.toLowerCase().includes(t.resultado.texto.slice(0, 40).toLowerCase()), c.id + ": no revela el resultado de «" + t.nombre + "» sin solicitarlo");
      for (const t of quiere.filter(t => t.resultado.tipo === "texto")) ok(txt.toLowerCase().includes(t.resultado.texto.slice(0, 40).toLowerCase()), c.id + ": muestra «" + t.nombre + "» solicitada");
      const nLab = quiere.filter(t => t.resultado.tipo === "lab").length; if (nLab) ok(await pg.locator(".cq-cuerpo .gd-tabla-lab").count() === nLab, c.id + ": un bloque de resultados por cada prueba de laboratorio solicitada (" + nLab + ")");
      if (quiere.some(t => t.resultado.tipo === "lab")) ok(await pg.locator(".gd-tabla-lab").count() > 0 && (await pg.textContent(".gd-tabla-lab")).includes("Interpreta tú"), c.id + ": marcas de laboratorio ocultas mientras se evalúa la interpretación");
      if (perfil === "ideal") {
        const filas = await pg.locator(".cq-cuerpo .gd-tabla-lab tbody tr").evaluateAll(rs => rs.map(r => [].slice.call(r.querySelectorAll("th,td")).slice(0, 3).map(x => x.textContent.trim())));
        const mal1 = [].concat(...filas).filter(x => x && x[0] !== x[0].toUpperCase() && !/^(pH|pCO|pO)/.test(x)); ok(mal1.length === 0, c.id + ": todo lo que muestran las tablas de resultados empieza con mayúscula (" + mal1.slice(0, 3).join(" | ") + ")");
        const textos = await pg.locator(".cq-cuerpo .gd-labn p, .cq-cuerpo .gd-labn h3").allInnerTexts(); const mal2 = textos.filter(x => x.trim() && x.trim()[0] !== x.trim()[0].toUpperCase() && !/^(pH|pCO|pO)/.test(x.trim())); ok(mal2.length === 0, c.id + ": los resultados en texto empiezan con mayúscula (" + mal2.slice(0, 3).join(" | ") + ")");
        if (c.id === "c02") {
          const tit = await pg.locator(".cq-cuerpo h3.gd-h3").allInnerTexts(); ok(tit.includes("Examen completo de orina") && tit.includes("Urocultivo"), "c02: el examen completo de orina y el urocultivo se muestran en bloques separados");
          const orina = await pg.evaluate(() => { const h = [].find.call(document.querySelectorAll(".cq-cuerpo h3.gd-h3"), x => x.textContent.trim() === "Examen completo de orina"); return h ? [].map.call(h.nextElementSibling.querySelectorAll("tbody tr"), r => r.innerText) : []; });
          const claves = ["Color", "Aspecto", "Densidad", "pH", "Proteínas", "Glucosa", "Cetonas", "Bilirrubina", "Urobilinógeno", "Sangre", "Nitritos", "Esterasa", "Leucocitos", "Hematíes", "Células epiteliales", "Cilindros", "Cristales", "Bacterias", "Levaduras", "mucus"], faltan = claves.filter(k => !orina.some(r => r.includes(k)));
          ok(orina.length >= 18 && !faltan.length, "c02: el examen completo de orina trae todos los parámetros físicos, químicos y del sedimento (" + orina.length + "; faltan: " + faltan.join(", ") + ")");
          ok(!orina.some(r => /Urocultivo|Escherichia/.test(r)), "c02: el urocultivo no está mezclado dentro del examen de orina");
          ok(/Positivo: Escherichia coli ≥ 100 000 UFC\/mL/.test(await pg.textContent(".cq-cuerpo")), "c02: el urocultivo muestra «Positivo: Escherichia coli…» con mayúscula inicial");
        }
      }
      const cal = perfil === "ideal" ? "optima" : "peligrosa";
      await responder(pg, "interpretacion", c, perfil === "ideal" ? "optima" : "incorrecta");
      if (quiere.some(t => t.resultado.tipo === "lab")) ok(!(await pg.textContent(".gd-tabla-lab")).includes("Interpreta tú"), c.id + ": tras responder se muestran las marcas");
      // sin corrección durante la consulta y sin cambiar la respuesta
      const antes = await pg.textContent('[data-mcq="interpretacion"] .gd-fb__t'); ok(/Respuesta registrada \([A-E]\)/.test(antes), c.id + ": la respuesta se registra sin corregir");
      const cuerpo1 = await pg.textContent('[data-mcq="interpretacion"]'); ok(!/Incorrecta|Peligrosa|Decisión óptima|Conducta preferible|Aceptable, mejorable/.test(cuerpo1) && await pg.locator('[data-mcq="interpretacion"] .gd-op.is-optima, [data-mcq="interpretacion"] .gd-op.is-incorrecta, [data-mcq="interpretacion"] .gd-op.is-peligrosa').count() === 0, c.id + ": durante la consulta no se muestra la corrección ni se colorean las alternativas");
      const otra = c.preguntas.interpretacion.decisiones.find(d => !antes.includes("(" + d.id + ")")); await pg.click('[data-mcq="interpretacion"] [data-op="' + otra.id + '"]', { force: true });
      ok((await pg.textContent('[data-mcq="interpretacion"] .gd-fb__t')) === antes, c.id + ": no permite cambiar la respuesta ni enviarla dos veces");
      await sig(pg, "diagnostico"); await responder(pg, "diagnostico", c, perfil === "ideal" ? "optima" : "incorrecta");
      await sig(pg, "tratamiento"); await responder(pg, "tratamiento", c, cal); await sig(pg, "seguimiento"); await responder(pg, "seguimiento", c, perfil === "ideal" ? "optima" : "incorrecta");
      ok(!/Incorrecta \(tu elección|Peligrosa \(tu elección|Conducta preferible/.test(await pg.textContent(".cq-cuerpo")), c.id + ": tampoco se corrige el seguimiento antes del final");
      await pg.click('[data-sig="informe"]'); await pg.waitForSelector(".gd-informe");
      return { quiere, informe: await pg.textContent(".gd-informe") };
    }
    for (const c of CASOS) {
      const r = await recorrer(p, c, "ideal"); const pct = +/(\d+) %/.exec(await p.textContent(".gd-final .gd-pts b"))[1];
      ok(pct >= 90, c.id + ": recorrido ideal ≥ 90 % (fue " + pct + " %)");
      for (const t of ["Pruebas pertinentes que solicitaste", "Pruebas innecesarias o de bajo valor que solicitaste", "Pruebas importantes que omitiste", "Pruebas potencialmente perjudiciales que solicitaste", "Pruebas no solicitadas que habrían cambiado la conducta"]) ok(r.informe.includes(t), c.id + ": informe incluye «" + t + "»");
      ok(r.informe.includes("Referencias del caso") && r.informe.includes("Análisis de las cinco alternativas"), c.id + ": informe con referencias y análisis de cinco alternativas");
      const prog = await p.evaluate(() => localStorage.getItem("mqp_progreso_v1") || ""); ok(prog.includes(c.id), c.id + ": el progreso de la consulta se guarda");
      const r2 = await recorrer(p, c, "deficiente"); const pct2 = +/(\d+) %/.exec(await p.textContent(".gd-final .gd-pts b"))[1];
      ok(pct2 < 60 && pct2 < pct, c.id + ": recorrido deficiente < 60 % y menor que el ideal (fue " + pct2 + " %)");
      const bl = c.pruebas.filter(t => t.bloqueante); if (bl.length) ok(r2.informe.includes("reconsiderar"), c.id + ": informe registra la reconsideración");
      ok(r2.informe.includes("Pruebas innecesarias") && r2.informe.includes("omitiste"), c.id + ": informe deficiente lista omisiones");
    }
    /* sesión recuperable + estado persistido */
    const c = CASOS[0]; await abrir(p, c); await sig(p, "anamnesis"); await p.click('[data-pregunta="anamnesis:' + N.aplanar(c)[0].id + '"]'); await p.reload(); await p.waitForSelector("#cqTitulo");
    await p.goto(base + "app/#/consulta"); await p.waitForSelector(".gd-caso"); await abrir(p, c, true);
    ok((await p.textContent(".cq-cuerpo")).includes(N.aplanar(c)[0].respuesta.slice(0, 20)), "la sesión se recupera tras recargar y volver a entrar");
    /* móvil y accesibilidad */
    const m = await navegador.newContext({ viewport: { width: 375, height: 740 }, isMobile: true }); await m.addInitScript(INIT); const pm = await nueva(m);
    await abrir(pm, c); await sig(pm, "anamnesis"); for (const id of N.aplanar(c).slice(0, 3).map(q => q.id)) await pm.click('[data-pregunta="anamnesis:' + id + '"]');
    ok(await pm.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), "móvil: sin desplazamiento horizontal");
    if (process.env.AXE_PATH) {
      const axe = fs.readFileSync(process.env.AXE_PATH, "utf8");
      for (const esquema of ["light", "dark"]) {
        await p.emulateMedia({ colorScheme: esquema });
        for (const paso of ["anamnesis", "pruebas", "informe"]) {
          await abrir(p, c);
          if (paso !== "anamnesis") { await recorrer(p, c, "ideal"); if (paso === "pruebas") continue; }
          else await sig(p, "anamnesis");
          await p.evaluate(axe); const v = await p.evaluate(async () => (await axe.run(document.body, { runOnly: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] })).violations.map(x => x.id + ":" + x.nodes.length));
          ok(v.length === 0, "axe " + esquema + " " + paso + ": " + v.join(", "));
        }
      }
    }
    ok(errores.length === 0, "sin errores de consola/página: " + errores.slice(0, 3).join(" | "));
    ok(externas.length === 0, "sin peticiones externas: " + externas.slice(0, 3).join(" | "));
  } finally { await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true }); }
  console.log(fallos ? "FALLARON " + fallos + " de " + total : "OK: " + total + " comprobaciones E2E de Consulta Clínica Experta"); process.exit(fallos ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
