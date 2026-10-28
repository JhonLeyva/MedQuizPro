/* MedQuizPlus · «Consulta Clínica Experta» · núcleo puro (sin DOM): evaluación ponderada por importancia clínica, informe de pruebas
   (pertinentes / bajo valor / omitidas importantes / perjudiciales / que habrían cambiado la conducta), bloqueos por pruebas esenciales omitidas
   y sesión recuperable. Reutiliza la tabla de puntos de la guardia. Todo sale de los datos validados del caso: no hay IA ni resultados aleatorios. */
(function (raiz) {
  "use strict";
  var PUNTOS = { optima: 10, aceptable: 5, incorrecta: 0, peligrosa: 0 };
  var ETAPAS = ["motivo", "anamnesis", "antecedentes", "examen", "hipotesis", "pruebas", "resultados", "diagnostico", "tratamiento", "seguimiento", "informe"];
  var NOMBRES = { motivo: "Motivo de consulta", anamnesis: "Anamnesis", antecedentes: "Antecedentes", examen: "Examen físico", hipotesis: "Hipótesis", pruebas: "Solicitud de pruebas", resultados: "Resultados e interpretación", diagnostico: "Diagnóstico", tratamiento: "Tratamiento", seguimiento: "Seguimiento y derivación", informe: "Informe" };
  /* peso de cada componente en el puntaje (suman 100): refleja su importancia clínica, no la cantidad de preguntas */
  var PESOS = { anamnesis: 10, examen: 10, hipotesis: 10, pruebas: 25, interpretacion: 10, diagnostico: 15, tratamiento: 12, seguimiento: 8 };
  var NOMBRE_COMP = { anamnesis: "Anamnesis", examen: "Examen físico", hipotesis: "Hipótesis y diferenciales", pruebas: "Selección de pruebas", interpretacion: "Interpretación de resultados", diagnostico: "Diagnóstico", tratamiento: "Tratamiento", seguimiento: "Seguimiento, alarma y derivación" };
  var CLASES = { prioritaria: "Pertinente y prioritaria", razonable: "Razonable, no imprescindible", innecesaria: "Innecesaria o de bajo valor", danina: "Potencialmente perjudicial o contraindicada" };
  var PEN_DANINA = 15, PEN_INNECESARIA = 5, PEN_MAX = 50;

  function por(lista, id) { for (var i = 0; i < lista.length; i++) if (lista[i].id === id) return lista[i]; return null; }
  function aplanar(caso) { var r = []; caso.anamnesis.forEach(function (c) { c.preguntas.forEach(function (q) { r.push(q); }); }); return r; }
  function pct(a, b) { return b ? Math.round(a / b * 100) : 100; }

  /* cobertura de lo importante: no se penaliza preguntar de más; solo cuenta lo clave que se omitió */
  function coberturaClave(items, hechos) {
    var clave = items.filter(function (x) { return x.relevancia === "clave"; }), ok = clave.filter(function (x) { return hechos.indexOf(x.id) >= 0; });
    return { pct: pct(ok.length, clave.length), omitidos: clave.filter(function (x) { return hechos.indexOf(x.id) < 0; }), hechos: ok.length, total: clave.length };
  }
  function evaluarHipotesis(caso, h) {
    h = h || { sel: [], principal: null }; var ops = caso.hipotesis.opciones, correcta = ops.filter(function (o) { return o.tipo === "principal"; })[0];
    var incluida = h.sel.indexOf(correcta.id) >= 0, p = h.principal === correcta.id ? 100 : incluida ? 60 : 0;
    var difs = ops.filter(function (o) { return o.tipo === "diferencial"; }), cubiertos = difs.filter(function (o) { return h.sel.indexOf(o.id) >= 0; });
    return { pct: p, correcta: correcta, incluida: incluida, comoPrincipal: h.principal === correcta.id, diferencialesCubiertos: cubiertos.length, diferenciales: difs };
  }
  /* Informe de pruebas: cinco listas con su justificación; no hay una única lista aceptable (las «razonables» no se penalizan) */
  function evaluarPruebas(caso, solicitadas) {
    var pr = caso.pruebas, pedidas = pr.filter(function (t) { return solicitadas.indexOf(t.id) >= 0; }), no = pr.filter(function (t) { return solicitadas.indexOf(t.id) < 0; });
    var prioritarias = pr.filter(function (t) { return t.clasificacion === "prioritaria"; });
    var l = {
      pertinentes: pedidas.filter(function (t) { return t.clasificacion === "prioritaria" || t.clasificacion === "razonable"; }),
      bajoValor: pedidas.filter(function (t) { return t.clasificacion === "innecesaria"; }),
      omitidasImportantes: no.filter(function (t) { return t.clasificacion === "prioritaria"; }),
      perjudiciales: pedidas.filter(function (t) { return t.clasificacion === "danina"; }),
      cambiariaConducta: no.filter(function (t) { return t.cambia_conducta; })
    };
    var base = pct(prioritarias.length - l.omitidasImportantes.length, prioritarias.length), pen = Math.min(PEN_MAX, l.perjudiciales.length * PEN_DANINA + l.bajoValor.length * PEN_INNECESARIA);
    return { listas: l, base: base, penalizacion: pen, pct: Math.max(0, base - pen), tiempoCritico: l.omitidasImportantes.filter(function (t) { return t.tiempo_critico; }) };
  }
  /* pruebas cuya ausencia impide decidir con seguridad: la primera vez se pide reconsiderar; luego el alumno puede continuar bajo su responsabilidad */
  function bloqueos(caso, solicitadas) { return caso.pruebas.filter(function (t) { return t.bloqueante && solicitadas.indexOf(t.id) < 0; }); }
  function puntajeMCQ(q, letra) { var d = por(q.decisiones, letra); return d ? PUNTOS[d.calidad] * 10 : 0; }
  function resultadosSolicitados(caso, solicitadas) { return caso.pruebas.filter(function (t) { return solicitadas.indexOf(t.id) >= 0; }); }

  function evaluar(caso, e) {
    var preg = caso.preguntas, an = coberturaClave(aplanar(caso), e.anamnesis || []), ex = coberturaClave(caso.examen, e.examen || []);
    var hip = evaluarHipotesis(caso, e.hipotesis), pru = evaluarPruebas(caso, e.solicitadas || []);
    var r = e.respuestas || {}, comp = {
      anamnesis: an.pct, examen: ex.pct, hipotesis: hip.pct, pruebas: pru.pct,
      interpretacion: puntajeMCQ(preg.interpretacion, r.interpretacion), diagnostico: puntajeMCQ(preg.diagnostico, r.diagnostico), tratamiento: puntajeMCQ(preg.tratamiento, r.tratamiento), seguimiento: puntajeMCQ(preg.seguimiento, r.seguimiento)
    };
    var total = 0, sumaPesos = 0; Object.keys(PESOS).forEach(function (k) { total += comp[k] * PESOS[k]; sumaPesos += PESOS[k]; });
    var criticos = Object.keys(preg).filter(function (k) { var d = por(preg[k].decisiones, r[k]); return d && d.calidad === "peligrosa"; }), mayores = Object.keys(preg).filter(function (k) { var d = por(preg[k].decisiones, r[k]); return d && d.calidad === "incorrecta"; });
    return { total: Math.round(total / sumaPesos), componentes: Object.keys(PESOS).map(function (k) { return { id: k, nombre: NOMBRE_COMP[k], peso: PESOS[k], pct: comp[k] }; }), anamnesis: an, examen: ex, hipotesis: hip, pruebas: pru, criticos: criticos, mayores: mayores };
  }

  /* sesión recuperable */
  var VERSION = 1;
  function serializar(e) { return JSON.stringify({ v: VERSION, caso: e.caso, etapa: e.etapa, anamnesis: e.anamnesis || [], antecedentes: e.antecedentes || [], examen: e.examen || [], hipotesis: e.hipotesis || { sel: [], principal: null }, solicitadas: e.solicitadas || [], borrador: e.borrador || [], respuestas: e.respuestas || {}, reevaluaciones: e.reevaluaciones || 0, segundos: e.segundos || 0, t: e.t || 0 }); }
  function restaurar(texto, caso) {
    var s; try { s = JSON.parse(texto); } catch (x) { return null; }
    if (!s || s.v !== VERSION || s.caso !== caso.id || ETAPAS.indexOf(s.etapa) < 0 || s.etapa === "informe") return null;
    var okIds = function (lista, ids) { return (ids || []).every(function (i) { return !!por(lista, i); }); };
    if (!okIds(aplanar(caso), s.anamnesis) || !okIds(caso.examen, s.examen) || !okIds(caso.antecedentes, s.antecedentes) || !okIds(caso.pruebas, s.solicitadas) || !okIds(caso.pruebas, s.borrador)) return null;
    for (var k in (s.respuestas || {})) { if (!caso.preguntas[k] || !por(caso.preguntas[k].decisiones, s.respuestas[k])) return null; }
    return s;
  }
  function registrar(guardado, caso, pct, ahora) {
    var g = JSON.parse(JSON.stringify(guardado || { casos: {} })); g.casos = g.casos || {};
    var r = g.casos[caso.id] || { mejor: 0, intentos: 0 }; r.intentos++; r.mejor = Math.max(r.mejor, pct); r.ultimo = pct; r.t = ahora || Date.now(); g.casos[caso.id] = r; return g;
  }

  var API = { PUNTOS: PUNTOS, ETAPAS: ETAPAS, NOMBRES: NOMBRES, PESOS: PESOS, NOMBRE_COMP: NOMBRE_COMP, CLASES: CLASES, coberturaClave: coberturaClave, evaluarHipotesis: evaluarHipotesis, evaluarPruebas: evaluarPruebas, bloqueos: bloqueos, puntajeMCQ: puntajeMCQ,
    resultadosSolicitados: resultadosSolicitados, evaluar: evaluar, serializar: serializar, restaurar: restaurar, registrar: registrar, aplanar: aplanar };
  if (typeof module !== "undefined" && module.exports) module.exports = API; else (raiz.MQP = raiz.MQP || {}).consultaNucleo = API;
})(typeof window !== "undefined" ? window : this);
