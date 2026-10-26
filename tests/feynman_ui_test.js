// node tests/feynman_ui_test.js — máquina de estados y voz del Tutor Feynman IA con SpeechRecognition / speechSynthesis simulados.
"use strict";
const E = require("../feynman_estado.js"), V = require("../feynman_voz.js");
let fallos = 0, total = 0;
function ok(c, m) { total++; if (!c) { fallos++; console.log("FALLA:", m); } }

/* ---------- máquina de estados ---------- */
{
  const cambios = [], m = E.crear((a, p) => cambios.push(p + ">" + a));
  ok(m.estado() === "listo", "estado inicial: preparado para escuchar");
  ok(!m.ir("procesando_audio"), "no se puede 'procesar audio' sin haber escuchado");
  ok(m.ir("escuchando") && m.estado() === "escuchando", "listo → escuchando");
  ok(!m.ir("analizando"), "mientras escucha no se puede 'analizar' (nada se envió)");
  ok(!m.ir("reproduciendo"), "mientras escucha no suena la voz de la IA");
  ok(m.ir("procesando_audio") && m.ir("esperando"), "escuchando → procesando audio → esperando (la transcripción vuelve al estudiante)");
  ok(m.ir("analizando") && m.estado() === "analizando", "al ENVIAR pasa a analizando");
  ok(!m.puedeEscuchar(), "analizando: el micrófono no puede abrirse");
  ok(m.ir("reproduciendo") && !m.puedeEscuchar() && !m.puedeEnviar(), "reproduciendo: ni micrófono ni envío (no se mezclan)");
  ok(m.ir("esperando") && m.puedeEscuchar() && m.puedeEnviar(), "esperando: ya puede hablar o enviar");
  ok(m.ir("escuchando") && m.ir("esperando"), "cancelar el dictado vuelve a esperando");
  ok(m.ir("analizando") && m.ir("error") && m.puedeEnviar() && m.puedeEscuchar(), "error recuperable: se puede reintentar enviar o hablar");
  ok(m.ir("analizando") && m.ir("completada") && m.estado() === "completada", "sesión completada");
  ok(!m.ir("escuchando"), "completada no permite abrir el micrófono");
  ok(m.ir("analizando"), "…pero 'otro caso' vuelve a analizar");
  ok(m.ir("analizando") === true && cambios.filter(c => c === "analizando>analizando").length === 0, "ir al mismo estado no dispara eventos repetidos");
  ok(Object.keys(E.ETIQUETAS).length === 8 && Object.keys(E.PERMITIDAS).every(k => E.ETIQUETAS[k]), "ocho estados con etiqueta");
}

/* ---------- entorno simulado ---------- */
function ventana(extra) {
  const w = { _t: [], setTimeout(f, ms) { w._t.push({ f, ms }); return w._t.length; }, clearTimeout(id) { if (w._t[id - 1]) w._t[id - 1] = null; }, correrTiempo() { const t = w._t.filter(Boolean); w._t = []; t.forEach(x => x.f()); } };
  return Object.assign(w, extra);
}
function SRSimulado() {
  const C = function () { C.ultimo = this; C.creados++; this.iniciado = false; };
  C.creados = 0;
  C.prototype.start = function () { if (C.lanzar) throw new Error("ya iniciado"); this.iniciado = true; };
  C.prototype.stop = function () { this.detenido = true; this.onend && this.onend(); };
  C.prototype.abort = function () { this.abortado = true; this.onerror && this.onerror({ error: "aborted" }); this.onend && this.onend(); };
  return C;
}
const res = (txt, fin, conf) => ({ resultIndex: 0, results: [Object.assign([{ transcript: txt, confidence: conf === undefined ? 0.9 : conf }], { isFinal: fin })] });

/* ---------- dictado ---------- */
{
  const ev = []; const SR = SRSimulado(); const w = ventana({ webkitSpeechRecognition: SR });
  const e = V.crearEscucha(w, { onEstado: s => ev.push("estado:" + s), onTexto: t => ev.push("texto:" + t.final + "|" + t.interino), onFin: (t, i) => ev.push("fin:" + t + ":" + i.confianza), onCancelado: () => ev.push("cancelado"), onError: x => ev.push("error:" + x.codigo) });
  ok(V.soporteEscucha(w) && e.disponible(), "detecta webkitSpeechRecognition");
  ok(e.iniciar() && !ev.includes("estado:escuchando"), "iniciar NO declara 'escuchando' hasta que el navegador confirma el micrófono");
  SR.ultimo.onstart(); ok(ev.includes("estado:escuchando"), "'escuchando' se informa al abrirse el micrófono");
  ok(e.iniciar() === false && SR.creados === 1, "doble inicio ignorado: un solo reconocimiento");
  SR.ultimo.onresult(res("la falta de insulina", false)); SR.ultimo.onresult(res("la falta de insulina activa la lipólisis", true, 0.5));
  ok(ev.includes("texto:|la falta de insulina") && ev.includes("texto:la falta de insulina activa la lipólisis|"), "transcripción parcial y final");
  e.detener(); ok(ev[ev.length - 1] === "fin:la falta de insulina activa la lipólisis:0.5", "detener entrega el texto final y la confianza más baja");
  ok(!e.activo() && ev.filter(x => x.startsWith("fin")).length === 1, "onFin exactamente una vez");
  // cancelar: no entrega texto
  ev.length = 0; e.iniciar(); SR.ultimo.onstart(); SR.ultimo.onresult(res("texto que se descarta", true)); e.cancelar();
  ok(ev.includes("cancelado") && !ev.some(x => x.startsWith("fin")) && !ev.some(x => x.startsWith("error")), "cancelar descarta la intervención sin error");
  // reintentar tras cancelar
  ev.length = 0; ok(e.iniciar(), "se puede volver a intentar tras cancelar");
  // permiso denegado
  SR.ultimo.onerror({ error: "not-allowed" }); SR.ultimo.onend();
  ok(ev.filter(x => x.startsWith("error")).join() === "error:permiso_denegado" && !ev.some(x => x.startsWith("fin")), "permiso del micrófono denegado → un único error comprensible y sin texto");
  ok(/candado|Permisos/.test(V.MENSAJES.permiso_denegado) && /escribe/.test(V.MENSAJES.permiso_denegado), "el mensaje explica cómo activar el permiso y ofrece escribir");
  ev.length = 0; e.iniciar(); SR.ultimo.onerror({ error: "no-speech" }); SR.ultimo.onend(); ok(ev.join() === "error:sin_voz", "sin voz: error recuperable (no se interpreta como falta de conocimiento)");
  ev.length = 0; e.iniciar(); SR.ultimo.onerror({ error: "network" }); SR.ultimo.onend(); ok(ev.join() === "error:red", "servicio de voz caído: error recuperable");
  ev.length = 0; e.iniciar(); SR.ultimo.onerror({ error: "audio-capture" }); SR.ultimo.onend(); ok(ev.join() === "error:sin_microfono", "sin micrófono");
  // límite de duración
  ev.length = 0; e.iniciar(); SR.ultimo.onstart(); SR.ultimo.onresult(res("dicté mucho", true)); w.correrTiempo(); ok(SR.ultimo.detenido && ev.some(x => x === "fin:dicté mucho:0.9"), "la grabación se detiene sola al llegar al límite de tiempo");
  // eventos tardíos de un reconocimiento viejo se ignoran
  ev.length = 0; e.iniciar(); const viejo = SR.ultimo; viejo.onstart(); e.cancelar(); ev.length = 0; e.iniciar(); const nuevo = SR.ultimo; viejo.onresult(res("fantasma", true)); viejo.onend();
  ok(!ev.some(x => x.includes("fantasma")) && e.activo(), "eventos de un reconocimiento anterior no afectan al actual");
  nuevo.onend();
}
{
  const ev = []; const w = ventana({});
  const e = V.crearEscucha(w, { onEstado() {}, onFin() {}, onError: x => ev.push(x.codigo) });
  ok(!V.soporteEscucha(w) && !e.disponible(), "sin SpeechRecognition se detecta"); e.iniciar(); ok(ev.join() === "no_soportado" && /Escribe/.test(V.MENSAJES.no_soportado), "navegador sin dictado → alternativa de texto");
  const SR = SRSimulado(); SR.lanzar = true; const e2 = V.crearEscucha(ventana({ SpeechRecognition: SR }), { onEstado() {}, onFin() {}, onError: x => ev.push(x.codigo) }); ev.length = 0;
  ok(e2.iniciar() === false && ev.join() === "otro" && !e2.activo(), "si start() lanza una excepción no queda 'activo' colgado");
}

/* ---------- lectura en voz alta ---------- */
function SintesisSimulada() {
  const S = { hablados: [], cancelaciones: 0, pausas: 0, reanudaciones: 0, voces: [{ lang: "en-US" }, { lang: "es_MX", name: "Mx" }, { lang: "es-ES", name: "Es" }],
    speak(u) { S.hablados.push(u); S.actual = u; }, cancel() { S.cancelaciones++; if (S.actual) { const u = S.actual; S.actual = null; u.onerror && u.onerror({ error: "interrupted" }); } },
    pause() { S.pausas++; }, resume() { S.reanudaciones++; }, getVoices() { return S.voces; },
    terminar() { const u = S.actual; S.actual = null; if (u) { u.onstart && u.onstart(); u.onend && u.onend(); } } };
  return S;
}
class Enunciado { constructor(t) { this.text = t; } }
{
  const S = SintesisSimulada(), w = ventana({ speechSynthesis: S, SpeechSynthesisUtterance: Enunciado }), ev = [];
  const h = V.crearHabla(w, { onEstado: (e, d) => ev.push(e + (d ? ":" + d : "")) });
  ok(V.soporteHabla(w) && h.disponible(), "detecta speechSynthesis");
  const largo = "Primera frase del tutor. Segunda frase con más palabras para forzar el troceado del texto largo. " + "Otra frase intermedia más larga que las anteriores y bastante extensa para llenar. ".repeat(4) + "¿Qué ocurre con la insulina?";
  ok(V.trocear(largo, 180).length >= 3 && V.trocear(largo, 180).every(p => p.length <= 270), "el texto se trocea por frases (evita el corte de Chrome)");
  ok(V.trocear("**Hola** [G1] mundo", 180)[0] === "Hola mundo", "se quitan el formato y las citas [G#] antes de leer");
  ok(V.elegirVoz(w).lang === "es_MX", "elige una voz en español (prefiere es-419/MX sobre es-ES)");
  ok(h.hablar(largo) && ev[0] === "hablando" && S.hablados.length === 1 && S.hablados[0].voice.lang === "es_MX" && S.hablados[0].lang === "es_MX", "empieza a hablar con voz en español");
  h.pausar(); ok(ev.includes("pausado") && S.pausas === 1 && h.pausado(), "pausa refleja el estado real");
  h.pausar(); ok(S.pausas === 1, "pausar dos veces no repite");
  h.reanudar(); ok(ev[ev.length - 1] === "hablando" && S.reanudaciones === 1 && !h.pausado(), "reanudar");
  const n = S.hablados.length; S.terminar(); ok(S.hablados.length === n + 1, "al terminar un trozo pasa al siguiente");
  // reemplazo: una nueva locución cancela la anterior y los eventos viejos no interfieren
  const viejo = S.actual; ev.length = 0; h.hablar("Otra respuesta nueva."); ok(S.hablados[S.hablados.length - 1].text === "Otra respuesta nueva." && ev.join() === "hablando", "hablar() reemplaza la locución anterior sin estado 'detenido' intermedio");
  viejo.onend && viejo.onend(); viejo.onerror && viejo.onerror({ error: "synthesis-failed" });
  ok(S.actual.text === "Otra respuesta nueva." && !ev.includes("error:synthesis-failed"), "eventos de una locución cancelada se ignoran (no hay audio duplicado)");
  S.terminar(); ok(ev[ev.length - 1] === "fin" && !h.hablando(), "fin de la lectura");
  // detener
  h.hablar("Texto a detener."); ev.length = 0; h.detener(); ok(ev.join() === "detenido" && !h.hablando() && S.actual === null, "detener refleja 'detenido' y vacía la cola");
  h.detener(); ok(ev.join() === "detenido", "detener sin nada sonando no emite eventos");
  // error de síntesis
  h.hablar("Error de voz."); ev.length = 0; const u = S.actual; u.onerror({ error: "synthesis-failed" }); ok(ev.join() === "error:synthesis-failed" && !h.hablando(), "error de síntesis → estado de error recuperable");
  // el navegador nunca empieza
  h.hablar("Nunca empieza."); ev.length = 0; w.correrTiempo(); ok(ev.join() === "error:no_inicio" && !h.hablando(), "si el navegador no empieza a hablar se informa (no se aparenta que suena)");
  // velocidad
  h.velocidad(1.4); h.hablar("Más rápido."); ok(S.actual.rate === 1.4, "velocidad configurable"); h.velocidad(99); h.hablar("Tope."); ok(S.actual.rate === 1.6, "velocidad acotada");
  const w2 = ventana({}); ok(!V.soporteHabla(w2) && !V.crearHabla(w2, {}).disponible() && V.crearHabla(w2, {}).hablar("x") === false, "sin síntesis de voz: no falla, solo no habla");
}
console.log(fallos ? fallos + " fallos de " + total : "OK: " + total + " comprobaciones de estados, dictado y lectura en voz alta");
process.exit(fallos ? 1 : 0);
