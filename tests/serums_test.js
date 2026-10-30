// node tests/serums_test.js — Misión SERUMS: motor puro, casos, registro de evidencia e índice documental. Sin red ni navegador.
"use strict";
const fs = require("fs"), path = require("path"), { spawnSync } = require("child_process");
const R = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const N = require("../serums_nucleo.js");
const ev = JSON.parse(fs.readFileSync(path.join(R, "serums/evidencia.json"), "utf8")), ind = JSON.parse(fs.readFileSync(path.join(R, "serums/indice.json"), "utf8"));
const casos = fs.readdirSync(path.join(R, "serums/casos")).sort().map(f => JSON.parse(fs.readFileSync(path.join(R, "serums/casos", f), "utf8")));

ok(casos.length === 10, "hay diez casos");
ok(spawnSync("python3", [path.join(R, "tools/serums_empaquetar.py"), "--check"]).status === 0, "serums_casos.js está al día con los JSON");
casos.forEach(c => { const e = N.validarCaso(c, ev, ind); ok(e.length === 0, "caso válido " + c.id + ": " + e.join(" | ")); });
ok(new Set(casos.map(c => c.id)).size === 10, "ids únicos");

/* evidencia: estados válidos, sin inventar, y los casos solo citan documentos vigentes e indexados */
ok(ev.fuentes.every(f => ev.estados.indexOf(f.estado) >= 0), "estados de vigencia válidos");
ok(ev.fuentes.every(f => f.verificado && f.numero), "cada fuente tiene fecha de verificación y número");
ok(ev.fuentes.filter(f => f.indexada).every(f => ind.docs.some(d => d.id === f.id)), "las fuentes marcadas como indexadas existen en el índice");
casos.forEach(c => c.momentos.forEach(m => m.opciones.forEach(o => (o.ref || []).forEach(r => {
  const f = ev.fuentes.find(x => x.id === r.doc); ok(f && f.estado === "Normativa vigente verificada" && f.indexada, c.id + " solo cita fuentes vigentes e indexadas: " + r.doc); }))));
ok(!JSON.stringify(casos).includes("246-MINSA"), "ningún caso usa la NTS 246 no verificada");
const noVig = ev.fuentes.filter(f => f.estado !== "Normativa vigente verificada").map(f => f.id);
casos.forEach(c => (c.evidencia || []).forEach(id => ok(noVig.indexOf(id) < 0, c.id + " no usa documentos en revisión o históricos")));
ok(casos.every(c => c.estado_publicacion === "Pendiente de revisión clínica"), "ningún caso se presenta como validado sin revisión clínica");
ok(casos.every(c => c.pendientes.length >= 1), "cada caso declara lo que está pendiente");
ok(casos.filter(c => c.evidencia.length === 0).every(c => c.pendientes.join(" ").includes("validación científica")), "los casos sin fuente indexada se declaran pendientes de validación científica");
ok(casos.every(c => c.momentos.every(m => m.opciones.filter(o => o.calidad === "optima").length === 1)), "una única opción óptima por decisión");
ok(casos.every(c => c.momentos.length >= 5 && c.momentos.length <= 8), "entre 5 y 8 momentos de decisión");

/* ayudantes de partida */
const elegir = (c, cal, e0) => { let e = e0 || N.iniciar(c, null, 1000), t = 1000; while (!e.fin) { const m = N.momentoActual(c, e); const orden = cal === "optima" ? ["optima"] : cal === "peligrosa" ? ["peligrosa", "incorrecta", "aceptable"] : ["incorrecta", "peligrosa", "aceptable"]; let o = null; for (const q of orden) { o = o || m.opciones.find(x => x.calidad === q && N.disponibilidad(x, e).ok); } o = o || m.opciones.find(x => N.disponibilidad(x, e).ok); t += 7000; e = N.decidir(c, e, o.id, t).estado; } return e; };
casos.forEach(c => {
  const ideal = N.evaluar(c, elegir(c, "optima")), mal = N.evaluar(c, elegir(c, "peligrosa")), reg = N.evaluar(c, elegir(c, "incorrecta"));
  ok(ideal.total >= 90 && ideal.criticos.length === 0 && ideal.desenlace === "favorable", c.id + ": el recorrido ideal da ≥ 90 sin errores críticos (" + ideal.total + ")");
  ok(mal.total < 60 && mal.criticos.length > 0 && mal.desenlace === "desfavorable", c.id + ": el recorrido peligroso da < 60 (" + mal.total + ")");
  ok(reg.total < ideal.total && reg.total < 60, c.id + ": el recorrido incorrecto puntúa menos que el ideal (" + reg.total + ")");
  ok(ideal.ejes.reduce((a, x) => a + (x.pct == null ? 0 : x.puntos), 0) > 0 && Math.abs(ideal.ejes.reduce((a, x) => a + x.peso, 0) - 100) < 1e-9, c.id + ": los pesos de los ejes suman 100");
  /* determinismo: dos corridas iguales producen estados iguales (menos el tiempo real) */
  const a = elegir(c, "optima"), b = elegir(c, "optima"); ok(JSON.stringify(a.historial) === JSON.stringify(b.historial) && JSON.stringify(a.inventario) === JSON.stringify(b.inventario), c.id + ": determinista");
});

/* un error crítico limita el puntaje a 74 aunque el resto sea ideal */
{ const c = casos.find(x => x.id === "s06"); let e = N.iniciar(c, null, 0); let t = 0;
  while (!e.fin) { const m = N.momentoActual(c, e); const o = (m.id === "m5" ? m.opciones.find(x => x.calidad === "peligrosa") : m.opciones.find(x => x.calidad === "optima" && N.disponibilidad(x, e).ok)) || m.opciones.find(x => N.disponibilidad(x, e).ok); e = N.decidir(c, e, o.id, t += 5000).estado; }
  const r = N.evaluar(c, e); ok(r.criticos.length >= 1 && r.total <= N.TOPE_CRITICO && r.topado_por_error_critico, "error crítico: puntaje limitado a " + N.TOPE_CRITICO + " (" + r.total + ")"); }

/* reloj: el tiempo simulado y el real se registran por separado */
{ const c = casos[0]; let e = N.iniciar(c, null, 1000); const o = N.momentoActual(c, e).opciones[0]; const r = N.decidir(c, e, o.id, 1000 + 42000).estado;
  ok(r.t_sim === o.min && Math.round(r.t_real) === 42, "tiempo simulado (" + r.t_sim + " min) y real (" + Math.round(r.t_real) + " s) separados");
  const largo = N.decidir(c, e, o.id, 1000 + 99999000).estado; ok(largo.t_real <= 600, "una pausa larga no infla el tiempo real"); }

/* inventario: consumo, bloqueo por falta de insumo y no mutación */
{ const c = casos.find(x => x.id === "s02"); const est = { inventario: { sulfato_mg: 2 } }; let e = N.iniciar(c, est, 0); e = N.decidir(c, e, "a", 1).estado; /* m1 */
  const antes = JSON.stringify(e); const m2 = N.momentoActual(c, e); const opA = m2.opciones.find(o => o.calidad === "optima");
  ok(!N.disponibilidad(opA, e).ok && /Insumo insuficiente/.test(N.disponibilidad(opA, e).motivo), "sin sulfato de magnesio suficiente la opción queda bloqueada con motivo");
  const r = N.decidir(c, e, opA.id, 2); ok(!r.ok && JSON.stringify(e) === antes, "decidir una opción bloqueada no cambia el estado");
  const c1 = casos[0], e1 = N.iniciar(c1, null, 0), o1 = N.momentoActual(c1, e1).opciones[0], copia = JSON.stringify(e1); N.decidir(c1, e1, o1.id, 5); ok(JSON.stringify(e1) === copia, "decidir no muta el estado recibido");
  const e2 = elegir(c, "optima"); ok(e2.inventario.sulfato_mg === e2.inventario_inicial.sulfato_mg - 5, "el consumo se descuenta del inventario"); ok(N.evaluar(c, e2).consumo.sulfato_mg === 5, "el informe reporta el consumo"); }
{ const c = casos.find(x => x.id === "s07"); const e = N.iniciar(c, null, 0); ok(e.inventario.sro === 2 && e.inventario.oxigeno === 0, "el caso de desabastecimiento ajusta el inventario inicial"); }
ok(N.establecimiento({ distancia_min: -5, categoria: "X", ambito: "luna", comunicacion: "?", nombre: "a".repeat(200), inventario: { sro: "abc" } }).nombre.length === 60 && N.establecimiento({ categoria: "X" }).categoria === "I-2", "la configuración del establecimiento se sanea");

/* eventos contextuales y vía bloqueada */
{ const c = casos.find(x => x.id === "s05"); let e = N.iniciar(c, null, 0); ok(e.flags.indexOf("via_bloqueada") < 0, "la vía empieza transitable"); e = N.decidir(c, e, "a", 1).estado; e = N.decidir(c, e, "a", 2).estado;
  ok(e.flags.indexOf("via_bloqueada") >= 0 && e.historial.some(h => h.tipo === "evento"), "al llegar a la referencia se bloquea la vía (evento)");
  const m = N.momentoActual(c, e), b = m.opciones.find(o => o.bloquea_si); ok(!N.disponibilidad(b, e).ok, "con la vía bloqueada no se puede solicitar la ambulancia");
  ok(N.tiempoReferencia(e) === N.tiempoReferencia(N.iniciar(c, null, 0)) * 2, "la vía bloqueada duplica el tiempo de traslado");
  ok(N.tiempoReferencia(N.iniciar(c, { ambulancia: false }, 0)) === N.tiempoReferencia(N.iniciar(c, null, 0)) + 60, "sin ambulancia el traslado se demora más"); }
{ const c = casos.find(x => x.id === "s01"); let e = N.iniciar(c, null, 0); e = N.decidir(c, e, "d", 1).estado; /* m1 d: 10 min */ ok(e.eventos_vistos.length === 0, "el evento por tiempo aún no se dispara"); e = N.decidir(c, e, "d", 2).estado; ok(e.eventos_vistos.length === 1 && e.gravedad >= 2, "el evento por tiempo se dispara al pasar los minutos y agrava"); }

/* pruebas de la posta */
{ const c = casos.find(x => x.id === "s03"); let e = N.iniciar(c, { inventario: { prueba_dengue: 0 } }, 0); let r = N.solicitarPrueba(c, e, "p1", 1); ok(!r.ok && /Insumo/.test(r.motivo), "sin insumo no se solicita la prueba");
  e = N.iniciar(c, null, 0); r = N.solicitarPrueba(c, e, "p1", 1); ok(r.ok && r.estado.t_sim === 20 && r.estado.inventario.prueba_dengue === e.inventario.prueba_dengue - 1 && r.estado.pruebas.length === 1, "la prueba consume insumo y tiempo"); ok(!N.solicitarPrueba(c, r.estado, "p1", 2).ok, "no se repite la prueba"); }

/* taxonomía de errores y explicaciones */
casos.forEach(c => c.momentos.forEach(m => m.opciones.forEach(o => { ok(!!o.retro && (o.calidad === "optima" || N.ERRORES[o.error]), c.id + "/" + m.id + "/" + o.id + " tiene explicación y tipo de error"); })));
ok(Object.keys(N.ERRORES).length >= 7, "taxonomía de errores");
ok(["clinico", "seguridad", "recursos", "referencia", "comunitario"].every(k => casos.some(c => c.momentos.some(m => m.eje === k))) && casos.every(c => new Set(c.momentos.map(m => m.eje)).size >= 4), "los casos trabajan los cinco ejes (al menos cuatro cada uno)");

/* validador: detecta casos defectuosos */
{ const malo = JSON.parse(JSON.stringify(casos[0])); malo.momentos[0].opciones[0].texto += " 500 mg"; malo.momentos[0].opciones[0].ref = undefined; ok(N.validarCaso(malo, ev, ind).some(x => /cantidad de medicamento/.test(x)), "el validador rechaza dosis sin cita");
  const m2 = JSON.parse(JSON.stringify(casos[1])); m2.momentos[0].opciones[0].ref = [{ doc: "ins-gpc03-2025", pag: 9999 }]; ok(N.validarCaso(m2, ev, ind).some(x => /no existe en el índice/.test(x)), "el validador rechaza páginas inexistentes");
  const m3 = JSON.parse(JSON.stringify(casos[2])); m3.momentos[0].opciones.forEach(o => { if (o.calidad === "optima") o.calidad = "aceptable"; }); ok(N.validarCaso(m3, ev, ind).some(x => /sin opción óptima/.test(x)), "el validador exige una opción óptima");
  const m4 = JSON.parse(JSON.stringify(casos[3])); m4.estado_publicacion = "Aprobado"; ok(N.validarCaso(m4, ev, ind).length > 0, "el validador rechaza estados de publicación inventados"); }

/* recuperación documental: devuelve fragmentos reales con página; no inventa */
{ const r = N.buscar(ind, "criterios de severidad sulfato de magnesio", 3, ["ins-gpc03-2025"]); ok(r.length > 0 && r.every(x => x.doc === "ins-gpc03-2025" && x.pagina > 0 && x.texto.length > 20), "la búsqueda devuelve fragmentos con documento y página");
  ok(r.every(x => ind.fragmentos.some(f => f.doc === x.doc && f.pagina === x.pagina && f.texto === x.texto)), "cada resultado es un fragmento textual del índice");
  ok(N.buscar(ind, "zzzxyz qqqwww", 3, ["nts221-tb"]).length === 0, "sin coincidencias no devuelve nada"); ok(N.buscar(ind, "tos con flema 15 días", 2, ["nts221-tb"]).length > 0, "recupera la definición de sintomático respiratorio");
  ok(N.buscar(ind, "sarampión", 3, ["nts221-tb"]).every(x => x.doc === "nts221-tb"), "respeta el filtro de documentos"); }

/* progreso, aprendizaje adaptativo y campaña */
{ let p = null; const c1 = casos[0], c2 = casos[1]; p = N.registrarIntento(p, c1, N.evaluar(c1, elegir(c1, "optima")), 10); p = N.registrarIntento(p, c2, N.evaluar(c2, elegir(c2, "incorrecta")), 20);
  ok(p.casos.s01.mejor >= 90 && p.casos.s02.intentos === 1 && p.intentos.length === 2, "se registra cada intento"); const r = N.resumenProgreso(p); ok(r.intentos === 2 && r.eje_flojo && Object.keys(r.medias).length > 0, "resumen por eje y eje flojo");
  const rec = N.recomendar(casos, p); ok(rec && rec.caso && casos.some(c => c.id === rec.caso) && /eje|intentado|Repite/.test(rec.motivo), "recomienda según el eje más flojo");
  ok(N.recomendar(casos, null).caso === "s01", "sin historial sugiere el primer caso"); let q = null; for (let i = 0; i < 70; i++) q = N.registrarIntento(q, c1, N.evaluar(c1, elegir(c1, "optima")), i); ok(q.intentos.length === 60, "el historial se acota"); }
{ const c = casos[0]; let camp = N.campanaNueva(null, 30), e = elegir(c, "optima"); camp = N.campanaCerrarDia(camp, N.evaluar(c, e), e);
  ok(camp.dia === 2 && camp.inventario.oxigeno === e.inventario.oxigeno && camp.reputacion > 50 && camp.resultados.length === 1, "campaña: el inventario y la reputación pasan al día siguiente"); }


/* introducción: audio de tormenta de 30 s y relámpagos sincronizados con sus truenos */
{ const mp3 = path.join(R, "serums/audio/tormenta.mp3"); ok(fs.existsSync(mp3) && fs.statSync(mp3).size > 100000 && fs.statSync(mp3).size < 900000, "existe el audio de la tormenta (tamaño razonable)");
  const pr = spawnSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp3]); if (pr.status === 0) { const d = parseFloat(String(pr.stdout)); ok(d >= 30 && d < 30.2, "el audio dura 30 s (" + d + ")"); } else console.log("(ffprobe no disponible: se omite la duración)");
  const js = fs.readFileSync(path.join(R, "serums.js"), "utf8"), py = fs.readFileSync(path.join(R, "tools/serums_audio.py"), "utf8");
  const rel = [...js.matchAll(/\{ t: ([\d.]+), x: \d+, y0/g)].map(m => +m[1]), tru = [...py.matchAll(/\(([\d.]+), [\d.]+\)/g)].map(m => +m[1]).slice(0, 6);
  ok(rel.length === 6 && tru.length === 6 && rel.every((t, i) => t <= tru[i] && tru[i] - t <= 1.0) && rel.every((t, i) => i === 0 || (t - rel[i - 1] >= 3.5 && t - rel[i - 1] <= 5.5)), "seis relámpagos separados 4–5 s, cada uno antes de su trueno (< 1 s): " + rel + " / " + tru);
  ok(fs.existsSync(path.join(R, "guardia/portadas/serums-intro.webp")) && fs.statSync(path.join(R, "guardia/portadas/serums-intro.webp")).size < 200000, "la imagen de la introducción está optimizada"); }

console.log(`serums_test: ${total - fallos}/${total} comprobaciones correctas`); process.exit(fallos ? 1 : 0);
