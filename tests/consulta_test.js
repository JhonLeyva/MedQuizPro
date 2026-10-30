// node tests/consulta_test.js — «Consulta Clínica Experta»: estructura de los casos, cinco alternativas por decisión, reparto de letras y pistas de estilo,
// clasificación de pruebas, resultados coherentes con el catálogo de laboratorio, bloqueos, puntaje ponderado, informe de pruebas y sesión recuperable.
"use strict";
const fs = require("fs"), path = require("path"), cp = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
global.window = {}; const CASOS = require("../consulta_casos.js"), N = require("../consulta_nucleo.js"), LAB = require("../guardia_lab.js");
const G = require("../guardia_nucleo.js");
const Q = ["interpretacion", "diagnostico", "tratamiento", "seguimiento"], LET = ["A", "B", "C", "D", "E"];
const palabras = t => t.trim().split(/\s+/).length, media = a => a.reduce((s, x) => s + x, 0) / (a.length || 1);

ok(cp.spawnSync("python3", [path.join(RAIZ, "tools/guardia_empaquetar.py"), "--check"]).status === 0, "consulta_casos.js está al día con consulta/casos/*.json");
ok(CASOS.length >= 4, "al menos 4 casos piloto");
const esp = new Set(CASOS.map(c => c.especialidad)); ok(esp.size === CASOS.length, "una especialidad distinta por caso piloto");
const labIds = new Set(LAB.pruebas.map(t => t.id));
const correctas = [], todas = [];
for (const c of CASOS) {
  ok(/^c\d\d$/.test(c.id) && c.modalidad === "consulta", c.id + ": id y modalidad");
  for (const k of ["titulo", "especialidad", "resumen", "contexto", "motivo", "paciente", "referencias", "discrepancias", "anamnesis", "antecedentes", "examen", "hipotesis", "pruebas", "preguntas", "informe"]) ok(c[k] != null && c[k] !== "", c.id + ": campo " + k);
  ok(c.referencias.length >= 1 && c.referencias.every(r => r.titulo && r.recomendacion && (r.pmid || r.doi || r.url) && r.fecha_consulta), c.id + ": referencias (una guía por caso; limitación declarada) con identificador y fecha de consulta");
  ok(c.referencias.some(r => r.tipo === "guia"), c.id + ": al menos una guía");
  ok(c.discrepancias.length >= 1 && c.discrepancias.some(d => /perua|MINSA|EsSalud/i.test(d)), c.id + ": declara la situación de la norma peruana");
  const ids = new Set(); const unico = i => { const a = !ids.has(i); ids.add(i); return a; };
  N.aplanar(c).forEach(q => ok(unico(q.id) && q.texto && q.respuesta, c.id + ": pregunta " + q.id)); c.antecedentes.forEach(a => ok(unico(a.id) && a.texto, c.id + ": antecedente " + a.id)); c.examen.forEach(x => ok(unico(x.id) && x.hallazgo && x.maniobra, c.id + ": maniobra " + x.id));
  ok(N.aplanar(c).filter(q => q.relevancia === "clave").length >= 2 && c.examen.some(x => x.relevancia === "clave"), c.id + ": datos clave definidos");
  /* hipótesis */
  const hp = c.hipotesis.opciones; ok(hp.filter(o => o.tipo === "principal").length === 1 && hp.filter(o => o.tipo === "diferencial").length >= 2 && c.hipotesis.max >= 2, c.id + ": una hipótesis principal y ≥ 2 diferenciales");
  ok(new Set(hp.map(o => o.id)).size === hp.length, c.id + ": ids de hipótesis únicos");
  /* pruebas */
  const pc = c.pruebas, cls = k => pc.filter(t => t.clasificacion === k);
  ok(new Set(pc.map(t => t.id)).size === pc.length, c.id + ": ids de pruebas únicos");
  ok(cls("prioritaria").length >= 1 && cls("razonable").length >= 1 && cls("innecesaria").length >= 1 && cls("danina").length >= 1, c.id + ": hay pruebas prioritarias, razonables, innecesarias y perjudiciales");
  ok(new Set(pc.map(t => t.categoria)).size >= 2, c.id + ": pruebas agrupadas en varias categorías");
  pc.forEach(t => {
    ok(["prioritaria", "razonable", "innecesaria", "danina"].includes(t.clasificacion) && t.justificacion && t.justificacion.length > 20, c.id + "/" + t.id + ": clasificación y justificación");
    ok(t.resultado && (t.resultado.tipo === "texto" ? !!t.resultado.texto : t.resultado.tipo === "lab" && t.resultado.lab.length), c.id + "/" + t.id + ": resultado predefinido");
    if (t.resultado.tipo === "lab") t.resultado.lab.forEach(r => ok(labIds.has(r.prueba) && (typeof r.valor === "number" || typeof r.valor === "string"), c.id + "/" + t.id + ": prueba de laboratorio " + r.prueba + " existe en el catálogo"));
    if (t.bloqueante) ok(t.clasificacion === "prioritaria" && t.mensaje_bloqueo && !t.mensaje_bloqueo.includes(t.nombre), c.id + "/" + t.id + ": bloqueo solo en prioritarias, con mensaje que no nombra la prueba");
    if (t.clasificacion === "prioritaria") ok(t.cambia_conducta, c.id + "/" + t.id + ": prioritaria declara qué cambia en la conducta");
  });
  ok(pc.some(t => t.bloqueante), c.id + ": al menos una prueba esencial bloqueante");
  /* alternativas */
  Q.forEach(k => {
    const q = c.preguntas[k], d = q.decisiones, t = c.id + "/" + k;
    ok(d.length === 5, t + ": cinco alternativas"); ok(d.map(x => x.id).join("") === "ABCDE", t + ": letras A–E en orden");
    ok(d.filter(x => x.calidad === "optima").length === 1 && d.every(x => ["optima", "incorrecta", "peligrosa"].includes(x.calidad)), t + ": una sola óptima y sin calidades difusas");
    ok(new Set(d.map(x => x.texto)).size === 5, t + ": sin alternativas duplicadas");
    d.forEach(x => { ok(x.explicacion && x.explicacion.length > 30, t + x.id + ": explicación"); ok(!/\b(la|opci[oó]n|alternativa|respuesta) [A-E]\b/i.test(x.explicacion), t + x.id + ": la explicación no cita letras"); });
    const L = d.map(x => palabras(x.texto)), o = d.findIndex(x => x.calidad === "optima");
    ok(Math.max(...L) / Math.min(...L) <= 1.6, t + ": longitudes comparables (" + L.join(",") + ")");
    ok(d.every(x => x.texto.length >= 60 && x.texto.length <= 190), t + ": longitud absoluta razonable");
    correctas.push({ caso: c.id, k, letra: d[o].id, mas_larga: d[o].texto.length === Math.max(...d.map(x => x.texto.length)), coma: (d[o].texto.match(/,/g) || []).length, comaMedia: media(d.filter((x, i) => i !== o).map(x => (x.texto.match(/,/g) || []).length)), rango: d.map(x => x.texto.length).sort((a, b) => b - a).indexOf(d[o].texto.length) });
    d.forEach(x => todas.push(x));
    ok(q.peso >= 1, t + ": peso");
  });
  ok(Object.keys(c.preguntas).sort().join() === Q.slice().sort().join(), c.id + ": las cuatro preguntas del flujo");
  /* informe */
  const inf = c.informe; ok(inf.diagnostico_final && inf.diagnosticos_diferenciales.length >= 2 && inf.datos_clave.length && inf.razonamiento.length && inf.tratamiento.length && inf.mensaje_clave, c.id + ": informe completo");
  ok(inf.tratamiento.every(t => t.item && t.detalle && t.dosis), c.id + ": tratamiento con detalle y dosis/unidades (o aclaración)");
  ok(inf.tratamiento.every(t => !/\b\d+\s?(mg|g|mcg|µg|UI|mL)\b/i.test(t.dosis) || /protocolo|guía|según/i.test(t.dosis)), c.id + ": no fija dosis universales sin remitir a la guía");
  /* puntaje */
  const mejor = Q.reduce((r, k) => (r[k] = c.preguntas[k].decisiones.find(d => d.calidad === "optima").id, r), {});
  const ideal = { anamnesis: N.aplanar(c).map(q => q.id), antecedentes: c.antecedentes.map(a => a.id), examen: c.examen.map(x => x.id), hipotesis: { sel: [hp.find(o => o.tipo === "principal").id], principal: hp.find(o => o.tipo === "principal").id }, solicitadas: pc.filter(t => t.clasificacion === "prioritaria" || t.clasificacion === "razonable").map(t => t.id), respuestas: mejor };
  const ev = N.evaluar(c, ideal); ok(ev.total === 100 && ev.criticos.length === 0 && ev.pruebas.listas.perjudiciales.length === 0 && ev.pruebas.listas.omitidasImportantes.length === 0, c.id + ": recorrido ideal = 100 %");
  const peor = { anamnesis: [], antecedentes: [], examen: [], hipotesis: { sel: [], principal: null }, solicitadas: pc.filter(t => t.clasificacion === "danina").map(t => t.id), respuestas: Q.reduce((r, k) => (r[k] = (c.preguntas[k].decisiones.find(d => d.calidad === "peligrosa") || c.preguntas[k].decisiones.find(d => d.calidad === "incorrecta")).id, r), {}) };
  const ev2 = N.evaluar(c, peor); ok(ev2.total <= 25 && ev2.criticos.length === Q.filter(k => c.preguntas[k].decisiones.some(d => d.calidad === "peligrosa")).length && ev2.pruebas.listas.perjudiciales.length >= 1, c.id + ": recorrido peor ≤ 15 % con 4 errores críticos (fue " + ev2.total + ")");
  /* pedir de más no baja a quien ya hizo lo esencial más que la penalización acotada; las «razonables» no penalizan */
  const sinRaz = Object.assign({}, ideal, { solicitadas: pc.filter(t => t.clasificacion === "prioritaria").map(t => t.id) }); ok(N.evaluar(c, sinRaz).total === 100, c.id + ": omitir pruebas «razonables» no penaliza");
  const conInn = Object.assign({}, ideal, { solicitadas: ideal.solicitadas.concat(pc.filter(t => t.clasificacion === "innecesaria").map(t => t.id)) }); const ci = N.evaluar(c, conInn); ok(ci.total < 100 && ci.total >= 90, c.id + ": pedir innecesarias penaliza poco (" + ci.total + ")");
  const sinPrio = Object.assign({}, ideal, { solicitadas: [] }); ok(N.evaluar(c, sinPrio).total < ev.total && N.evaluar(c, sinPrio).pruebas.listas.omitidasImportantes.length === cls("prioritaria").length, c.id + ": omitir prioritarias penaliza y las lista");
  ok(N.bloqueos(c, []).length >= 1 && N.bloqueos(c, pc.filter(t => t.bloqueante).map(t => t.id)).length === 0, c.id + ": bloqueos solicitables");
  /* sesión */
  const e = { caso: c.id, etapa: "pruebas", anamnesis: [ideal.anamnesis[0]], antecedentes: [], examen: [], hipotesis: ideal.hipotesis, solicitadas: [], borrador: [pc[0].id], respuestas: {}, reevaluaciones: 1, segundos: 12.5, t: 1 };
  const r = N.restaurar(N.serializar(e), c); ok(r && r.etapa === "pruebas" && r.borrador[0] === pc[0].id && r.reevaluaciones === 1, c.id + ": la sesión se restaura");
  ok(N.restaurar(N.serializar(Object.assign({}, e, { solicitadas: ["zzz"] })), c) === null, c.id + ": sesión con prueba inexistente se descarta");
  ok(N.restaurar(N.serializar(Object.assign({}, e, { respuestas: { diagnostico: "Z" } })), c) === null, c.id + ": sesión con respuesta inválida se descarta");
  ok(N.restaurar("{no json", c) === null && N.restaurar(N.serializar(Object.assign({}, e, { caso: "otro" })), c) === null, c.id + ": sesión corrupta o de otro caso se descarta");
}
/* ---- estadística global de las alternativas (mismas exigencias que el simulador de urgencias) ---- */
const n = correctas.length, cuenta = LET.map(l => correctas.filter(x => x.letra === l).length);
ok(n >= 16, "al menos 16 decisiones evaluadas"); ok(Math.max(...cuenta) <= Math.ceil(n * 0.35), "letras correctas sin sesgo (" + cuenta.join(",") + ")"); ok(cuenta.every(x => x >= 1), "las cinco letras aparecen como correctas (" + cuenta.join(",") + ")");
for (let i = 2; i < n; i++) ok(!(correctas[i].letra === correctas[i - 1].letra && correctas[i].letra === correctas[i - 2].letra), "sin tres iguales seguidas en " + correctas[i].caso + "/" + correctas[i].k);
ok(correctas.filter(x => x.mas_larga).length / n <= 0.35, "la correcta no es sistemáticamente la más larga (" + correctas.filter(x => x.mas_larga).length + "/" + n + ")");
ok(Math.abs(media(correctas.map(x => x.rango)) - 2) < 0.7, "rango medio de longitud de la correcta ≈ centro (" + media(correctas.map(x => x.rango)).toFixed(2) + ")");
ok(Math.abs(media(correctas.map(x => x.coma)) - media(correctas.map(x => x.comaMedia))) < 0.8, "comas de la correcta ≈ comas de las incorrectas");
const abs = /\b(siempre|nunca|todos|todas|ningún|ninguna|cualquier|únicamente|exclusivamente)\b/i; const rate = f => { const s = todas.filter(f); return s.length ? s.filter(x => abs.test(x.texto)).length / s.length : 0; };
ok(Math.abs(rate(x => x.calidad === "optima") - rate(x => x.calidad !== "optima")) < 0.2, "palabras absolutas repartidas entre correcta e incorrectas");
ok(new Set(todas.map(x => x.texto)).size === todas.length, "ninguna alternativa repetida entre casos");
/* ---- validaciones del núcleo ---- */
ok(Object.values(N.PESOS).reduce((s, x) => s + x, 0) === 100, "los pesos del puntaje suman 100");
ok(N.PESOS.pruebas >= N.PESOS.anamnesis && N.PESOS.diagnostico >= N.PESOS.seguimiento, "pesos coherentes con la importancia clínica");
ok(N.registrar(null, CASOS[0], 80, 1).casos.c01.mejor === 80 && N.registrar(N.registrar(null, CASOS[0], 80, 1), CASOS[0], 60, 2).casos.c01.mejor === 80, "registrar conserva el mejor puntaje");
ok(typeof G.NIVEL === "object", "el simulador de urgencias sigue disponible (niveles compartidos)");
/* ---- reglas de presentación (también para los casos nuevos) ---- */
for (const c of CASOS) {
  const mayus = t => /^[A-ZÁÉÍÓÚÑ«¿¡β\d]/.test(String(t).trim());
  ok(mayus(c.titulo) && mayus(c.resumen) && mayus(c.contexto) && mayus(c.motivo), c.id + ": título, resumen, contexto y motivo de consulta empiezan con mayúscula");
  ok(typeof c.paciente.edad_texto === "string" && /^\d/.test(c.paciente.edad_texto) && (c.paciente.sexo === "F" || c.paciente.sexo === "M"), c.id + ": paciente con sexo y edad para mostrar «Niña de 20 meses», «Mujer de 38 años»…");
  ok(c.hipotesis.opciones.every(o => mayus(o.dx)) && c.pruebas.every(t => mayus(t.nombre) && mayus(t.justificacion)) && c.examen.every(x => mayus(x.maniobra) && mayus(x.hallazgo)) && N.aplanar(c).every(q => mayus(q.texto) && mayus(q.respuesta)), c.id + ": hipótesis, pruebas, examen y anamnesis empiezan con mayúscula");
  ok(c.pruebas.every(t => t.resultado.tipo !== "texto" || mayus(t.resultado.texto) || /^(pH|pCO|pO)/.test(t.resultado.texto)), c.id + ": los resultados en texto empiezan con mayúscula");
}
console.log(fallos ? "FALLARON " + fallos + " de " + total : "OK: " + total + " comprobaciones de Consulta Clínica Experta");
process.exit(fallos ? 1 : 0);
