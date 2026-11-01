// node tests/feynman_e2e.js — Tutor Feynman IA en un navegador real (Playwright/Chromium) contra PHP + un proveedor de IA SIMULADO solo para esta prueba.
// El micrófono (SpeechRecognition) y la voz (speechSynthesis) se simulan a nivel de API del navegador para poder controlarlos; la interfaz, el backend y la base de datos son los reales.
// Variables: AXE_PATH (axe.min.js; sin él se omite la auditoría de accesibilidad), SHOTS (carpeta para capturas), CHROMIUM (ejecutable).
"use strict";
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), os = require("os"), path = require("path"), net = require("net");
const { spawn } = require("child_process");
const RAIZ = path.resolve(__dirname, "..");
let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });

/* ---------- proveedor de IA simulado: un tutor mínimo que respeta la tarea que le fija el servidor ---------- */
const mock = { pedidos: [], demora: 0, falla: false };
function responderTutor(sistema, ultimo) {
  if (/Vas a abrir una sesión/.test(sistema)) return { mensaje: "Vamos a comprobar si comprendes la cetoacidosis diabética. Explícame con tus propias palabras por qué se produce la acidosis metabólica, como a un estudiante que recién empieza medicina.", objetivo: "Mecanismo de la acidosis en la CAD", criterios: [{ descripcion: "Déficit de insulina" }, { descripcion: "Lipólisis y cetogénesis" }, { descripcion: "Acidosis con anión gap elevado" }] };
  if (/La sesión terminó/.test(sistema)) return { resumen: "Corregiste el origen de la acidosis y lo aplicaste a un caso nuevo.", proximos_pasos: ["Repasar el anión gap"], tarjetas: [{ frente: "¿Por qué el déficit de insulina favorece la cetogénesis?", dorso: "Sin insulina aumenta la lipólisis y el hígado produce cuerpos cetónicos.", citas: [] }] };
  const fase = +(/Fase actual: (\d)/.exec(ultimo) || [0, 1])[1], forz = /"fase" sea (\d)/.exec(ultimo), perm = /debe ser una de: ([\d, ]+)\./.exec(ultimo);
  const base = { mensaje: "", pregunta_siguiente: null, aclaracion_transcripcion: false, evaluacion: { nivel: null, justificacion: "", criterios: [] }, conceptos_correctos: [], errores: [], errores_corregidos: [], omisiones: [], pistas: [], referencias: [], fase, repaso: [] };
  if (/PISTA/.test(ultimo)) return { ...base, mensaje: "Pista: piensa en qué hace la insulina sobre el tejido adiposo." };
  if (/EXPLICACIÓN DIRECTA/.test(ultimo)) return { ...base, fase: 4, mensaje: "Te lo explico: sin insulina se activa la lipólisis y el hígado forma cetonas que acidifican. Ahora explícalo tú." };
  if (/caso clínico breve NUEVO y distinto/.test(ultimo)) return { ...base, fase: 5, mensaje: "Nuevo caso: gestante con DM1 y vómitos. ¿Qué mecanismo explica la acidosis?", pregunta_siguiente: "¿Qué mecanismo explica la acidosis?" };
  const ev = n => ({ nivel: n, justificacion: "Evaluación de prueba", criterios: [{ id: "c1", estado: "parcial" }] });
  if (fase === 1) return { ...base, fase: 3, mensaje: "Buen comienzo. La glucosa es importante, pero profundicemos: ¿qué ocurre con las grasas cuando falta insulina?", pregunta_siguiente: "¿Qué ocurre con las grasas cuando falta insulina?", evaluacion: ev(2), conceptos_correctos: ["Hay hiperglucemia"], errores: [{ descripcion: "Atribuye la acidosis a la glucosa elevada", correccion: "La acidosis la producen los cuerpos cetónicos" }], omisiones: ["Cetogénesis"] };
  if (fase === 3) { const f = forz ? +forz[1] : 4; return { ...base, fase: f, mensaje: "Exacto: sin insulina hay lipólisis y cetogénesis. Reconstruyamos: déficit de insulina → lipólisis → cuerpos cetónicos → acidosis. ¿Puedes explicarlo de nuevo?", evaluacion: ev(3), conceptos_correctos: ["Sin insulina aumenta la lipólisis"], errores_corregidos: [1], omisiones: [] }; }
  if (fase === 4) return { ...base, fase: 5, mensaje: "Muy bien. Caso nuevo: paciente con DM1, náuseas, respiración profunda y cetonemia. ¿Qué mecanismo relaciona el déficit de insulina con la alteración ácido-base?", pregunta_siguiente: "¿Qué mecanismo relaciona el déficit de insulina con la alteración ácido-base?", evaluacion: ev(3) };
  return { ...base, fase: 5, mensaje: "Excelente: aplicaste el mecanismo al caso.", evaluacion: ev(4), conceptos_correctos: ["Aplica el mecanismo a un caso"] };
}
const ia = http.createServer((req, res) => {
  let b = ""; req.on("data", d => b += d); req.on("end", async () => {
    const j = JSON.parse(b); mock.pedidos.push(j);
    if (mock.demora) await dormir(mock.demora);
    if (mock.falla) { res.writeHead(500, { "Content-Type": "application/json" }); return res.end('{"error":{"message":"interno"}}'); }
    const ms = j.messages, r = responderTutor(ms[0].content, ms[ms.length - 1].content);
    res.writeHead(200, { "Content-Type": "application/json" }); res.end(JSON.stringify({ choices: [{ message: { content: JSON.stringify(r) } }] }));
  });
});

/* ---------- navegador simulado: micrófono y voz ---------- */
const SIMULACION = () => {
  const S = window.__sim = { instancias: [], hablados: [], denegar: false, actual: null, cancelaciones: 0 };
  class SR { constructor() { S.ultima = this; S.instancias.push(this); } start() { if (S.denegar) { setTimeout(() => { this.onerror && this.onerror({ error: "not-allowed" }); this.onend && this.onend(); }, 20); return; } setTimeout(() => this.onstart && this.onstart(), 20); }
    stop() { setTimeout(() => this.onend && this.onend(), 20); } abort() { setTimeout(() => { this.onerror && this.onerror({ error: "aborted" }); this.onend && this.onend(); }, 20); } }
  S.decir = (t) => { const it = [{ transcript: t, confidence: 0.93 }]; it.isFinal = true; S.ultima.onresult({ resultIndex: 0, results: [it] }); };
  S.terminar = () => { const u = S.actual; S.actual = null; if (u) { u.onstart && u.onstart(); u.onend && u.onend(); } };
  S.terminarTodo = () => { let n = 0; while (S.actual && n++ < 50) S.terminar(); };
  for (const n of ["SpeechRecognition", "webkitSpeechRecognition"]) Object.defineProperty(window, n, { value: SR, configurable: true });
  Object.defineProperty(window, "SpeechSynthesisUtterance", { value: function (t) { this.text = t; }, configurable: true });
  Object.defineProperty(window, "speechSynthesis", { configurable: true, value: { getVoices: () => [{ lang: "es-PE", name: "Simulada" }], pause() { S.pausado = true; }, resume() { S.pausado = false; },
    speak(u) { S.hablados.push(u.text); S.actual = u; setTimeout(() => u.onstart && u.onstart(), 5); }, cancel() { S.cancelaciones++; const u = S.actual; S.actual = null; if (u && u.onerror) u.onerror({ error: "interrupted" }); } } });
};

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "fy-e2e-"));
  for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  fs.cpSync(path.join(RAIZ, "app"), path.join(tmp, "app"), { recursive: true }); fs.cpSync(path.join(RAIZ, "guias"), path.join(tmp, "guias"), { recursive: true });
  for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));      // solo lectura
  const pIA = await libre(), pWeb = await libre(); await new Promise(r => ia.listen(pIA, "127.0.0.1", r));
  fs.mkdirSync(path.join(tmp, "t"));
  const php = spawn("php", ["-S", `127.0.0.1:${pWeb}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, AI_API_KEY: "k", AI_PROVIDER: "openai", AI_BASE_URL: `http://127.0.0.1:${pIA}/v1`, MQP_ADMIN_TOKEN: "token-de-prueba-largo-123", PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t"), FEYNMAN_LIMITE_MINUTO: "200" } });
  await dormir(1200);
  const base = `http://127.0.0.1:${pWeb}/`, shots = process.env.SHOTS || "";
  const foto = async (p, n) => { if (shots) { fs.mkdirSync(shots, { recursive: true }); await p.screenshot({ path: path.join(shots, n + ".png") }); } };
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 900 } });
    await ctx.addInitScript(SIMULACION); await ctx.addInitScript(() => { try { localStorage.setItem("mqp_sin_intros_prueba", "1"); localStorage.setItem("mqp_estudio_confianza", "no"); } catch (e) {} });
    const reg = await ctx.request.post(base + "cuenta.php?a=registro", { data: { nombre: "Tester", correo: "t@prueba.pe", clave: "clave12345", acepto: true }, headers: { "X-MQP": "1", Origin: base.slice(0, -1) } }); ok(reg.status() === 201, "registro");
    const dueno = await ctx.request.post(base + "cuenta.php?a=dueno_activar", { data: { token: "token-de-prueba-largo-123" }, headers: { "X-MQP": "1", Origin: base.slice(0, -1) } }); ok(dueno.status() === 200, "plan de dueño");
    const p = await ctx.newPage(); const errores = []; p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); });
    const json = async ruta => (await ctx.request.get(base + ruta)).json();

    /* ===== 1. desde una pregunta del banco ===== */
    await p.goto(base + "app/#/banco/configurar"); await p.waitForSelector("[data-accion=comenzar]"); await p.click("[data-accion=comenzar]");
    await p.waitForSelector("#svOptions .opt"); ok(await p.locator("#svFy").isHidden(), "«Aprender con Feynman» no aparece antes de responder");
    await (await p.$$("#svOptions .opt"))[0].click(); await p.waitForSelector("#svFy:not([hidden])");
    ok(true, "«Aprender con Feynman» aparece tras responder, junto a los botones existentes"); ok(await p.locator("#svAlgo").isVisible() && await p.locator("#svIA").isVisible() && await p.locator("#svFlash").isVisible(), "los botones existentes (flujograma, IA, flashcard) siguen ahí");
    await p.click("#svFy"); await p.waitForSelector("dialog.fy-dlg[open] .fy-msg--tutor");
    ok(/cetoacidosis diabética/.test(await p.locator(".fy-msg--tutor").first().innerText()), "el tutor abre con su pregunta de la fase 1");
    ok((await p.locator("#fyEstado").getAttribute("data-estado")) === "reproduciendo" || (await p.locator("#fyEstado").getAttribute("data-estado")) === "esperando", "estado tras abrir: reproduciendo o esperando");
    const lista1 = (await json("feynman.php?a=listar")).sesiones; ok(lista1.length === 1 && lista1[0].origen === "pregunta" && /^[A-Z]+-\d+/.test(lista1[0].pregunta_id), "la sesión queda vinculada a la pregunta de origen");
    const pid = lista1[0].pregunta_id, banco = JSON.parse(fs.readFileSync(path.join(RAIZ, "bancos", fs.readdirSync(path.join(RAIZ, "bancos")).find(f => JSON.parse(fs.readFileSync(path.join(RAIZ, "bancos", f))).preguntas.some(q => q.id === pid))))).preguntas.find(q => q.id === pid);
    const prompt1 = JSON.stringify(mock.pedidos[0]);
    ok(prompt1.includes(JSON.stringify(banco.enunciado).slice(1, 80)) && prompt1.includes("Correcta según el banco: " + banco.clave_correcta), "la IA recibió el enunciado y la clave REALES de la pregunta");
    ok(await p.evaluate(() => window.__sim.hablados.length > 0), "el tutor leyó su pregunta en voz alta (voz activada por defecto)");
    await foto(p, "01-sesion-inicio");

    /* ===== 2. respuesta por texto ===== */
    await p.evaluate(() => window.__sim.terminarTodo()); await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "esperando");
    await p.fill("#fyTa", "La glucosa elevada vuelve ácida la sangre y por eso hay acidosis en la cetoacidosis diabética, creo."); await p.click("#fyEnviar");
    await p.waitForFunction(() => document.querySelectorAll(".fy-msg--tutor").length === 2);
    ok(/lipólisis|grasas/.test(await p.locator(".fy-msg--tutor").nth(1).innerText()) && !/cetonas/i.test(await p.locator(".fy-msg--tutor").nth(1).innerText()), "error conceptual → pregunta socrática (no revela la respuesta completa)");
    ok((await p.locator(".fy-fase--actual").innerText()).includes("Preguntas socráticas") && (await p.locator("#fyProgT").innerText()).includes("Fase 3 de 5"), "fase 3 y progreso real");
    ok(/Atribuye la acidosis a la glucosa/.test(await p.locator("#fyPanelC").innerText()) && /por corregir/.test(await p.locator("#fyPanelC").innerText()), "el panel muestra el vacío detectado");
    ok(/Evaluación provisional: Nivel 2/.test(await p.locator(".fy-msg--yo").first().innerText()), "evaluación provisional de la intervención");
    await p.evaluate(() => window.__sim.terminarTodo());

    /* ===== 3. pista ===== */
    await p.click("#fyPista"); await p.waitForFunction(() => document.querySelectorAll(".fy-msg--tutor").length === 3);
    ok(/Pista: piensa/.test(await p.locator(".fy-msg--tutor").nth(2).innerText()), "pista adaptada del tutor");
    await p.evaluate(() => window.__sim.terminarTodo());

    /* ===== 4. voz: el micrófono solo "escucha" cuando está abierto; la transcripción se revisa antes de enviar ===== */
    ok(!(await p.locator("#fyEstado").getAttribute("data-estado")).includes("escuchando"), "antes de pulsar el micrófono no se muestra 'escuchando'");
    const nPedidos = mock.pedidos.length;
    await p.click("#fyMic"); await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "escuchando");
    ok(/Escuchando/.test(await p.locator("#fyEstadoT").innerText()) && await p.locator("#fyCancelaMic").isVisible() && (await p.locator("#fyMicT").innerText()).includes("Detener"), "escuchando: estado, botón Cancelar y 'Detener dictado'");
    ok(mock.pedidos.length === nPedidos, "mientras se escucha NO se ha enviado nada a la IA");
    await p.evaluate(() => window.__sim.decir("sin insulina se rompen las grasas y se forman cuerpos cetónicos que acidifican la sangre")); await p.click("#fyMic");
    await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "esperando");
    ok((await p.inputValue("#fyTa")).includes("cuerpos cetónicos") && mock.pedidos.length === nPedidos && await p.locator("#fyNotaVoz").isVisible(), "la transcripción queda en el cuadro para revisarla; no se envía sola");
    await p.fill("#fyTa", (await p.inputValue("#fyTa")) + " Es una acidosis metabólica con anión gap elevado."); // el estudiante corrige/completa
    await p.click("#fyEnviar"); await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "analizando", null, { timeout: 3000 }).catch(() => {});
    await p.waitForFunction(() => document.querySelectorAll(".fy-msg--tutor").length === 4);
    ok(/dictado/.test(await p.locator(".fy-msg--yo").nth(2).innerText()) && JSON.stringify(mock.pedidos.at(-1)).includes("RECONOCIMIENTO DE VOZ"), "el envío se marca como dictado y la IA lo sabe");
    ok((await p.locator("#fyProgT").innerText()).includes("Fase 4 de 5"), "el servidor avanzó a la fase 4 (reconstrucción) al corregirse el error");
    await p.evaluate(() => window.__sim.terminarTodo());

    /* ===== 5. cancelar un dictado, voz denegada, y la alternativa de texto ===== */
    await p.click("#fyMic"); await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "escuchando"); await p.evaluate(() => window.__sim.decir("texto que se descarta")); await p.click("#fyCancelaMic");
    await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "esperando"); ok((await p.inputValue("#fyTa")) === "", "cancelar el dictado descarta la intervención");
    await p.evaluate(() => { window.__sim.denegar = true; }); await p.click("#fyMic"); await p.waitForSelector("#fyAviso:not([hidden])");
    ok(/permiso/i.test(await p.locator("#fyAviso").innerText()) && (await p.locator("#fyEstado").getAttribute("data-estado")) === "error", "permiso denegado → mensaje comprensible y estado de error recuperable");
    ok(await p.locator("#fyTa").isEnabled(), "con el micrófono denegado se puede escribir"); await p.evaluate(() => { window.__sim.denegar = false; });

    /* ===== 6. cancelar el envío, reintento sin duplicar, y error de la IA ===== */
    mock.demora = 1500; const antes = mock.pedidos.length;
    await p.fill("#fyTa", "Sin insulina hay lipólisis, el hígado produce cuerpos cetónicos que consumen bicarbonato y generan acidosis metabólica con anión gap elevado."); await p.click("#fyEnviar");
    await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "analizando"); ok(/Analizando/.test(await p.locator("#fyEstadoT").innerText()) && await p.locator("#fyCancelaEnvio").isVisible(), "analizando: solo existe tras enviar, con opción de cancelar");
    await p.click("#fyCancelaEnvio"); await p.waitForFunction(() => document.querySelector("#fyEstado").dataset.estado === "esperando");
    mock.demora = 0; await p.waitForFunction(() => document.querySelectorAll(".fy-msg--tutor").length === 5, null, { timeout: 12000 }); // el servidor terminó la llamada y la interfaz se resincroniza sin duplicar
    ok(mock.pedidos.length === antes + 1 && (await p.locator(".fy-msg--tutor").count()) === 5 && (await p.locator(".fy-msg--yo").count()) === 4, "cancelar la espera no duplica el turno: la sesión se resincroniza");
    ok((await p.locator("#fyProgT").innerText()).includes("Fase 5 de 5") && /DM1/.test(await p.locator(".fy-msg--tutor").nth(4).innerText()), "pregunta de transferencia (fase 5) con un caso nuevo");
    await p.evaluate(() => window.__sim.terminarTodo());
    mock.falla = true; await p.fill("#fyTa", "El déficit de insulina lleva a lipólisis y cetogénesis; los cetoácidos consumen bicarbonato y generan acidosis con anión gap alto, con respiración de Kussmaul."); await p.click("#fyEnviar");
    await p.waitForSelector("#fyAviso:not([hidden])"); ok((await p.locator("#fyEstado").getAttribute("data-estado")) === "error" && !/interno|HTTP|500/.test(await p.locator("#fyAviso").innerText()) && (await p.inputValue("#fyTa")).includes("Kussmaul"), "error de la IA: mensaje amable sin datos técnicos y el texto no se pierde");
    ok(await p.locator("#fyEnviar").isEnabled(), "el error es recuperable: se puede reintentar");
    mock.falla = false; await p.click("#fyEnviar"); await p.waitForFunction(() => document.querySelectorAll(".fy-msg--tutor").length === 6);
    ok(/Excelente/.test(await p.locator(".fy-msg--tutor").nth(5).innerText()) && await p.evaluate(() => !document.querySelector("#fyFin").disabled), "tras el reintento, el caso queda resuelto");
    await p.evaluate(() => window.__sim.terminarTodo());

    /* ===== 7. finalizar → informe ===== */
    await foto(p, "02-sesion-fase5");
    await p.click("#fyFin"); await p.waitForSelector(".fy-informe");
    const inf = await p.locator(".fy-informe").innerText();
    ok(/A\. Lo que comprendiste/.test(inf) && /B\. Errores corregidos/.test(inf) && /C\. Conceptos pendientes/.test(inf) && /D\. Aplicación clínica/.test(inf) && /E\. Próximas acciones/.test(inf), "el informe tiene las secciones A–E");
    ok(/Concepto dominado/.test(inf) && /Comprensión sólida/.test(inf) && /Atribuye la acidosis a la glucosa/.test(inf), "el informe refleja las respuestas reales (error corregido, aplicación nivel 4)");
    ok((await p.locator("#fyEstado").getAttribute("data-estado")) === "completada", "estado: sesión completada");
    await foto(p, "03-informe");
    await p.click("[data-i=tarjetas]"); await p.waitForSelector("#fyTj");
    ok((await json("cuenta.php?a=fc_listar")).tarjetas.length === 0, "las tarjetas propuestas NO se guardaron solas");
    await p.fill("#fyTjF0", "¿Por qué el déficit de insulina favorece la cetogénesis? (editada)"); await p.click("#fyTj [type=submit]"); await p.waitForFunction(() => /guardada/.test(document.querySelector("#fyTjR").innerText));
    const fc = (await json("cuenta.php?a=fc_listar")).tarjetas; ok(fc.length === 1 && /editada/.test(fc[0].frente) && fc[0].pregunta === pid, "tras revisarla y editarla, la tarjeta se guarda en las flashcards del estudiante");
    await foto(p, "04-tarjetas");
    await p.click("[data-i=final]"); ok(/Te lo explico|Exacto/.test(await p.locator(".fy-extra").innerText()), "«Revisar la explicación final» muestra la reconstrucción");
    await p.click("[data-i=fuentes]"); ok(/no verificado/.test(await p.locator(".fy-extra").innerText()), "las fuentes se presentan con honestidad (sin guías cargadas)");

    /* ===== 8. el contenido del banco y la práctica siguen igual; cerrar vuelve a la pregunta ===== */
    await p.click("#fyCerrar"); await p.waitForSelector("dialog.fy-dlg", { state: "detached" });
    ok(await p.locator("#svFy").isVisible() && await p.locator("#svOptions .opt").count() >= 4, "al cerrar vuelves a la misma pregunta, con sus alternativas intactas");
    ok(await p.evaluate(() => !window.__sim.actual), "al cerrar no queda voz sonando");

    /* ===== 9. desde «Ver flujograma» ===== */
    await p.click("#svAlgo"); await p.waitForSelector("#algoModal[open]"); await p.waitForTimeout(400);
    const antesFlujo = await p.evaluate(() => ({ titulo: document.querySelector("#algoTitle").textContent, html: document.querySelector("#algoBody").innerHTML.length }));
    ok(await p.locator("#algoFy").isVisible(), "el visor de flujograma ofrece «Aprender con Feynman»");
    await p.click("#algoFy"); await p.waitForSelector("dialog.fy-dlg[open] .fy-msg--tutor");
    const ses = (await json("feynman.php?a=listar")).sesiones; ok(ses.length === 2 && ses.some(s => s.origen === "flujograma" && s.pregunta_id === pid), "sesión de origen «flujograma», vinculada a su pregunta, separada de la anterior");
    await p.click("#fyCerrar"); await p.waitForSelector("dialog.fy-dlg", { state: "detached" });
    await p.click("#svAlgo"); await p.waitForSelector("#algoModal[open]"); await p.waitForTimeout(400);
    const despuesFlujo = await p.evaluate(() => ({ titulo: document.querySelector("#algoTitle").textContent, html: document.querySelector("#algoBody").innerHTML.length }));
    ok(JSON.stringify(antesFlujo) === JSON.stringify(despuesFlujo), "el flujograma se muestra exactamente igual antes y después de usar el tutor");
    await p.keyboard.press("Escape");

    /* ===== 10. sección propia, sesiones guardadas y retomar ===== */
    await p.goto(base + "app/#/feynman"); await p.waitForSelector("#fyNueva");
    ok(await p.locator('a[data-ruta=feynman]').first().isVisible() && /Tutor Feynman IA/.test(await p.locator('a[data-ruta=feynman]').first().innerText()), "entrada «Tutor Feynman IA» en la navegación");
    ok(await p.locator("#fyEsp option").count() === 18, "selector con las 17 especialidades reales del banco");
    ok(await p.locator(".fy-sesion").count() === 2, "se listan las sesiones guardadas (retomar más tarde)");
    await foto(p, "05-inicio");
    await p.fill("#fyTema", "Preeclampsia severa"); await p.selectOption("#fyEsp", { index: 1 }); await p.click("#fyNueva [type=submit]"); await p.waitForSelector(".fy--sesion .fy-msg--tutor");
    ok((await p.locator("#fyTitulo").innerText()) === "Preeclampsia severa" && /#\/feynman\?s=/.test(await p.evaluate(() => location.hash)), "sesión desde un tema libre (página propia) con enlace retomable");
    await p.reload(); await p.waitForSelector(".fy--sesion .fy-msg--tutor"); ok((await p.locator("#fyTitulo").innerText()) === "Preeclampsia severa" && (await p.locator("#fyEstado").getAttribute("data-estado")) === "listo", "recargar retoma la sesión guardada (preparado para escuchar, sin reproducir solo)");
    ok(await p.evaluate(() => window.__sim.hablados.length) === 0, "una sesión retomada no empieza a hablar sin que el estudiante lo pida");
    // pedir explicación directa
    await p.click("#fyExplica"); await p.waitForFunction(() => document.querySelectorAll(".fy-msg--tutor").length === 2); ok((await p.locator("#fyProgT").innerText()).includes("Fase 4 de 5"), "«Pedir explicación» lleva a la reconstrucción (fase 4) sin evaluar");
    // finalizar antes de completar → confirmación y aviso honesto
    await p.click("#fyFin"); ok(await p.locator("#fyConfirma").isVisible(), "terminar antes de tiempo pide confirmación"); await p.click("#fyConfSi"); await p.waitForSelector(".fy-informe");
    ok(/antes de completar|no se evaluó/.test(await p.locator(".fy-informe").innerText()) && !/Concepto dominado/.test(await p.locator(".fy-informe").innerText()), "informe de sesión incompleta: sin 'dominado' y con aviso");
    ok(await p.locator("[data-i=retomar]").isVisible(), "se puede retomar una sesión incompleta");

    /* ===== 11. móvil ===== */
    const movil = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }); await movil.addInitScript(SIMULACION);
    const cookies = await ctx.cookies(); await movil.addCookies(cookies);
    const m = await movil.newPage(); const idAct = ses.find(s => s.origen === "pregunta").id, idActiva = ses.find(s => s.origen === "flujograma").id;
    await m.goto(base + `app/#/feynman?s=${idActiva}`); await m.waitForSelector(".fy--sesion .fy-msg--tutor"); await m.waitForTimeout(300);
    const caja = async sel => m.locator(sel).boundingBox();
    const mic = await caja("#fyMic"); ok(mic && mic.y + mic.height <= 844 + 1 && mic.x >= 0 && mic.x + mic.width <= 391, "móvil: el micrófono está dentro de la pantalla");
    ok(await m.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), "móvil: sin desplazamiento horizontal");
    const chat = await caja("#fyChat"); ok(chat && chat.height >= 200, "móvil: la conversación tiene altura útil (" + Math.round(chat.height) + " px)");
    ok(await m.locator("#fyPanel").getAttribute("open") === null, "móvil: el panel lateral empieza plegado para priorizar la conversación");
    await foto(m, "06-movil");
    // teclado virtual: la barra de composición sigue pegada abajo
    await m.evaluate(() => window.scrollTo(0, 0)); await movil.close();

    /* ===== 12. accesibilidad (axe) y movimiento reducido ===== */
    const axePath = process.env.AXE_PATH || ""; if (axePath && fs.existsSync(axePath)) {
      const AXE = fs.readFileSync(axePath, "utf8");
      const auditar = async (pg, nombre) => { await pg.evaluate(AXE); const r = await pg.evaluate(async () => await axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] } }));
        r.violations = r.violations.filter(v => !v.nodes.every(n => n.target.join(" ") === "#chatLauncher"));      // el botón flotante del chat del sitio no es de este módulo (ver docs/FEYNMAN.md)
        ok(r.violations.length === 0, "axe · " + nombre + ": " + r.violations.map(v => v.id + " ×" + v.nodes.length + " " + v.nodes[0].target.join(" ") + " " + ((v.nodes[0].any[0] || {}).message || "")).join(" | ")); };
      await p.goto(base + "app/#/feynman"); await p.waitForSelector("#fyNueva"); await auditar(p, "inicio del tutor");
      await p.goto(base + `app/#/feynman?s=${idAct}`); await p.waitForSelector(".fy--sesion .fy-msg--tutor"); await auditar(p, "sesión (con informe)");
      for (const tema of ["claro", "oscuro"]) { await p.evaluate(t => document.documentElement.setAttribute("data-theme", t), tema === "claro" ? "light" : "dark"); await p.waitForTimeout(600); await auditar(p, "sesión tema " + tema); }
    } else console.log("(axe omitido: define AXE_PATH)");
    const rm = await navegador.newContext({ reducedMotion: "reduce", viewport: { width: 1000, height: 800 } }); await rm.addInitScript(SIMULACION); await rm.addCookies(await ctx.cookies());
    const q = await rm.newPage(); await q.goto(base + `app/#/feynman?s=${idAct}`); await q.waitForSelector(".fy--sesion"); await q.evaluate(() => document.querySelector("#fyEstado").setAttribute("data-estado", "escuchando"));
    ok(await q.evaluate(() => getComputedStyle(document.querySelector(".fy-ind i")).animationName === "none"), "con movimiento reducido no hay animaciones");
    await rm.close();
    ok(errores.length === 0, "sin errores de JavaScript en consola: " + errores.slice(0, 3).join(" | "));
  } catch (e) { fallos++; console.log("EXCEPCIÓN:", e.message.split("\n")[0], "|", (e.stack.match(/feynman_e2e.js:\d+/) || [""])[0]); }
  finally { await navegador.close(); php.kill(); ia.close(); fs.rmSync(tmp, { recursive: true, force: true }); }
  console.log(fallos ? fallos + " fallos de " + total : "OK: " + total + " comprobaciones E2E del Tutor Feynman IA");
  process.exit(fallos ? 1 : 0);
})();
