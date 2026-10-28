/* MedQuizPlus · «Sobrevive a la Guardia» · núcleo puro (sin DOM): puntaje ponderado, temporizador, sesión recuperable, interconsulta,
   laboratorio (intervalos aplicables y conversiones validadas), análisis del recorrido, reglas de desenlace y recomendaciones.
   Se carga en el navegador (window.MQP.guardiaNucleo) y en Node (tests). No usa IA: todo sale de los datos validados del caso. */
(function (raiz) {
  "use strict";
  var PUNTOS = { optima: 10, aceptable: 5, incorrecta: 0, peligrosa: 0 };
  var ETQ = { optima: "Decisión óptima", aceptable: "Aceptable, mejorable", incorrecta: "Incorrecta", peligrosa: "Peligrosa" };
  var SEVERIDAD = { optima: "Correcta", aceptable: "Mejorable (sin daño probable)", incorrecta: "Error recuperable", peligrosa: "Error crítico (riesgo vital)" };
  var LETRAS = ["A", "B", "C", "D", "E"];
  /* tiempos iniciales de diseño (segundos) por tipo de decisión; cada nodo puede fijar `tiempo` propio dentro de LIMITES */
  var TIEMPOS = { critica: 45, diagnostica: 120, interpretacion: 150 };
  var TIPOS = { critica: "Decisión crítica de emergencia", diagnostica: "Decisión diagnóstica", interpretacion: "Interpretación de pruebas o imágenes" };
  var LIMITES = [20, 300];
  var AVISO_SEG = 10;                                   // aviso cuando quedan ≤ 10 s o ≤ 25 % del tiempo
  var PENAL_AYUDA = { 1: 0, 2: 1, 3: 3 };              // puntos pedagógicos que se descuentan del nodo (antes del peso); orientar no es un error
  var MODOS = {
    entrenamiento: { id: "entrenamiento", nombre: "Entrenamiento", cronometro: false, ayuda: true, retro: "inmediata", texto: "Sin presión de tiempo. Recibes la explicación tras cada decisión y puedes consultar al especialista (con una penalización pedagógica moderada)." },
    cronometrada: { id: "cronometrada", nombre: "Simulación cronometrada", cronometro: true, ayuda: false, retro: "final", texto: "Cada decisión tiene su tiempo según su tipo. Sin interconsulta y con la explicación completa al terminar el caso." }
  };
  var MIN_TOTAL = 30, MIN_AREA = 8, VENTANA_RECIENTE = 14 * 86400000, DIA = 86400000;

  /* ---------- puntaje ponderado por importancia clínica ---------- */
  function peso(nodo) { return nodo.peso || 1; }
  function maximo(caso, id, memo) {
    memo = memo || {};
    if (memo[id] !== undefined) return memo[id];
    var n = caso.nodos[id], mx = 0;
    if (!n.final) n.decisiones.forEach(function (d) { mx = Math.max(mx, PUNTOS[d.calidad] * peso(n) + maximo(caso, d.siguiente, memo)); });
    return (memo[id] = mx);
  }
  function porcentaje(caso, puntos) { var m = maximo(caso, caso.inicio); return m ? Math.round(puntos / m * 100) : 0; }      // solo sobre la ruta óptima; el puntaje del alumno se calcula sobre los nodos que recorrió (analizar)
  function maximoRecorrido(camino) { return camino.reduce(function (s, p) { return s + 10 * peso(p.nodo); }, 0); }
  function desbloqueado() { return true; }               // v2/v3: sin bloqueos por requisitos
  function puntosNodo(nodo, decision, nivelAyuda) {
    var base = PUNTOS[decision.calidad], pen = nivelAyuda ? PENAL_AYUDA[nivelAyuda] || 0 : 0;
    return Math.max(0, base - pen) * peso(nodo);
  }
  function registrar(guardado, caso, resultado, ahora) {
    var g = JSON.parse(JSON.stringify(guardado || { casos: {} })); g.casos = g.casos || {};
    var r = g.casos[caso.id] || { mejor: 0, intentos: 0, completados: 0 };
    r.intentos++; r.completados++; r.mejor = Math.max(r.mejor, resultado.pct); r.ultimo = resultado.pct; r.final = resultado.tipo; r.criticos = resultado.criticos || 0; r.t = ahora || Date.now();
    if (resultado.modo) { r.modo = resultado.modo; if (resultado.modo === "cronometrada") r.mejorCrono = Math.max(r.mejorCrono || 0, resultado.pct); }
    g.casos[caso.id] = r; return g;
  }
  function barajar(a, rnd) { rnd = rnd || Math.random; var b = a.slice(); for (var i = b.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)), t = b[i]; b[i] = b[j]; b[j] = t; } return b; }

  /* ---------- temporizador (reloj inyectable → determinista en pruebas) ---------- */
  function tiempoNodo(nodo) {
    var t = nodo.tiempo || TIEMPOS[nodo.tipo || "diagnostica"] || TIEMPOS.diagnostica;
    return Math.max(LIMITES[0], Math.min(LIMITES[1], t));
  }
  /* estado: corriendo/pausado; el tiempo pausado no cuenta. `usadoMs` permite restaurar una sesión sin reiniciar el reloj. */
  function crearReloj(limiteS, ahora, usadoMs) {
    ahora = ahora || Date.now; var acum = usadoMs || 0, desde = null, pausas = 0, limite = limiteS * 1000;
    var r = {
      iniciar: function () { if (desde === null) desde = ahora(); return r; },
      pausar: function () { if (desde !== null) { acum += ahora() - desde; desde = null; pausas++; } return r; },
      detener: function () { if (desde !== null) { acum += ahora() - desde; desde = null; } return r; },
      corriendo: function () { return desde !== null; },
      usadoMs: function () { return acum + (desde !== null ? ahora() - desde : 0); },
      restanteMs: function () { return Math.max(0, limite - r.usadoMs()); },
      restanteS: function () { return Math.ceil(r.restanteMs() / 1000); },
      agotado: function () { return r.usadoMs() >= limite; },
      pausas: function () { return pausas; },
      limiteS: limiteS,
      /* 'normal' | 'aviso' (≤ 25 % o ≤ AVISO_SEG s) | 'agotado' */
      nivel: function () { if (r.agotado()) return "agotado"; var rs = r.restanteMs() / 1000; return (rs <= AVISO_SEG || r.restanteMs() <= limite * 0.25) ? "aviso" : "normal"; }
    };
    return r;
  }
  function formatoTiempo(s) { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ":" + (s % 60 < 10 ? "0" : "") + (s % 60); }

  /* ---------- sesión recuperable ---------- */
  var VERSION_SESION = 3;
  function serializarSesion(e) {
    return JSON.stringify({ v: VERSION_SESION, caso: e.caso, modo: e.modo, nodo: e.nodo, puntos: e.puntos, vistas: e.vistas || [], usadoMs: Math.round(e.usadoMs || 0), pausado: !!e.pausado, ayudaNodo: e.ayudaNodo || [], t: e.t || 0,
      camino: (e.camino || []).map(function (p) { return { n: p.nodoId, d: p.decisionId, s: p.segundos, a: p.ayuda || [], x: p.agotado ? 1 : 0 }; }), resultados: e.resultados || [] });
  }
  /* valida contra el caso: una sesión que no coincide con el caso actual se descarta en vez de romper el juego */
  function restaurarSesion(texto, caso, modosValidos) {
    var s; try { s = JSON.parse(texto); } catch (e) { return null; }
    if (!s || s.v !== VERSION_SESION || s.caso !== caso.id || !caso.nodos[s.nodo] || caso.nodos[s.nodo].final || !MODOS[s.modo]) return null;
    var camino = [], id = caso.inicio;
    for (var i = 0; i < s.camino.length; i++) {
      var p = s.camino[i], nd = caso.nodos[p.n]; if (!nd || nd.final || p.n !== id) return null;
      var d = nd.decisiones.filter(function (x) { return x.id === p.d; })[0]; if (!d) return null;
      camino.push({ nodoId: p.n, nodo: nd, decision: d, decisionId: p.d, segundos: p.s, ayuda: p.a || [], agotado: !!p.x }); id = d.siguiente;
    }
    if (id !== s.nodo) return null;
    return { caso: s.caso, modo: s.modo, nodo: s.nodo, puntos: s.puntos, vistas: s.vistas || [], usadoMs: s.usadoMs || 0, pausado: !!s.pausado, ayudaNodo: s.ayudaNodo || [], t: s.t, camino: camino, resultados: s.resultados || [] };
  }

  /* ---------- interconsulta: tres niveles, siempre desde la lógica validada del caso ---------- */
  function especialistas(caso) { return caso.especialistas || []; }
  function ayudaDisponible(modo, nivelPrevio) { return !!MODOS[modo].ayuda; }
  /* devuelve { ok, pertinente, texto, nivel, derivar } — nunca inventa: n1/n2 son texto del nodo y n3 se arma con la decisión óptima y su justificación */
  function consultarEspecialista(caso, nodoId, nivel, especialidadId) {
    var nd = caso.nodos[nodoId], a = nd.ayuda || {}, esp = especialistas(caso), rec = a.especialista || (esp[0] && esp[0].id), per = a.pertinentes || [rec];
    var nombre = function (id) { var e = esp.filter(function (x) { return x.id === id; })[0]; return e ? e.nombre : id; };
    if (especialidadId && per.indexOf(especialidadId) < 0)
      return { ok: true, pertinente: false, nivel: nivel, derivar: rec, texto: "Esta consulta no corresponde a mi área en este momento del caso. Te sugiero interconsultar con: " + nombre(rec) + "." };
    var opt = nd.decisiones.filter(function (d) { return d.calidad === "optima"; })[0], texto;
    if (nivel === 1) texto = a.n1; else if (nivel === 2) texto = a.n2;
    else {
      var refs = (opt.refs || []).map(function (r) { for (var i = 0; i < caso.referencias.length; i++) if (caso.referencias[i].id === r) return "[" + (i + 1) + "]"; return ""; }).join(" ");
      texto = "Conducta recomendada: " + opt.texto + ". Justificación: " + opt.explicacion + (refs ? " Respaldo: referencia(s) " + refs + "." : "");
    }
    return { ok: !!texto, pertinente: true, nivel: nivel, texto: texto || "", especialista: nombre(especialidadId || rec) };
  }

  /* ---------- laboratorio: intervalo aplicable, marca y conversiones validadas ---------- */
  /* paciente: { edad (años), sexo: "F"|"M", embarazo: bool, trimestre: 1|2|3 } · prueba.intervalos[]: { sexo, edad_min, edad_max, condicion, bajo, alto, texto } */
  function intervaloAplicable(prueba, paciente) {
    paciente = paciente || {}; var cond = paciente.embarazo ? "gestacion-t" + (paciente.trimestre || 1) : null, mejor = null, mejorPts = -1;
    (prueba.intervalos || []).forEach(function (iv) {
      if (iv.sexo && iv.sexo !== "todos" && paciente.sexo && iv.sexo !== paciente.sexo) return;
      if (iv.edad_min != null && paciente.edad != null && paciente.edad < iv.edad_min) return;
      if (iv.edad_max != null && paciente.edad != null && paciente.edad >= iv.edad_max) return;
      if (iv.condicion && iv.condicion !== cond) return;
      var pts = (iv.condicion ? 4 : 0) + (iv.sexo && iv.sexo !== "todos" ? 2 : 0) + (iv.edad_min != null || iv.edad_max != null ? 1 : 0);
      if (pts > mejorPts) { mejor = iv; mejorPts = pts; }
    });
    return mejor;
  }
  function marca(valor, iv) {
    if (iv == null || typeof valor !== "number" || (iv.bajo == null && iv.alto == null)) return null;
    if (iv.bajo != null && valor < iv.bajo) return "bajo"; if (iv.alto != null && valor > iv.alto) return "alto"; return "normal";
  }
  /* factores de conversión: solo los que se derivan de la masa molar (ver tests); sin factor validado no se convierte */
  var CONVERSIONES = {
    "glucosa": { de: "mg/dL", a: "mmol/L", f: 0.0555, masa: 180.16 },
    "creatinina": { de: "mg/dL", a: "µmol/L", f: 88.4, masa: 113.12 },
    "bilirrubina_total": { de: "mg/dL", a: "µmol/L", f: 17.1, masa: 584.66 },
    "hemoglobina": { de: "g/dL", a: "g/L", f: 10, masa: null },
    "calcio": { de: "mg/dL", a: "mmol/L", f: 0.2495, masa: 40.08 },
    "urea": { de: "mg/dL", a: "mmol/L", f: 0.357, masa: null }
  };
  function convertir(prueba, valor, desde, hacia) {
    var c = CONVERSIONES[prueba];
    if (!c) return null;
    if (desde === c.de && hacia === c.a) return valor * c.f;
    if (desde === c.a && hacia === c.de) return valor / c.f;
    return null;
  }

  /* ---------- análisis del recorrido: todo el informe sale de lo que el alumno realmente eligió ---------- */
  function analizar(caso, camino, puntos, opts) {
    opts = opts || {};
    var maxTotal = camino.reduce(function (s, p) { return s + 10 * peso(p.nodo); }, 0), criticos = [], mayores = [], comp = {}, temas = [], vistos = {}, usadas = {}, orden = [], tiempoTotal = 0, limiteTotal = 0, agotados = 0, ayudas = [], penal = 0;
    var decisiones = camino.map(function (p, i) {
      var d = p.decision, nd = p.nodo, opt = nd.decisiones.filter(function (x) { return x.calidad === "optima"; })[0], niv = (p.ayuda || []).reduce(function (m, x) { return Math.max(m, x); }, 0);
      var lim = tiempoNodo(nd), item = { n: i + 1, nodoId: p.nodoId, estado: nd.estado, tipo: nd.tipo || "diagnostica", peso: peso(nd), pregunta: nd.pregunta, elegida: d, optima: opt, severidad: SEVERIDAD[d.calidad], agotado: !!p.agotado,
        segundos: p.segundos || 0, limite: lim, nivelAyuda: niv, penalizacion: niv ? Math.min(PUNTOS[d.calidad], PENAL_AYUDA[niv] || 0) * peso(nd) : 0,
        alternativas: nd.decisiones.filter(function (x) { return x.id !== d.id && x.id !== opt.id; }) };
      if (p.agotado) { agotados++; item.severidad = "Tiempo agotado: se aplicó la conducta de espera"; }
      if (d.calidad === "peligrosa") criticos.push(item); else if (d.calidad === "incorrecta") mayores.push(item);
      tiempoTotal += item.segundos; limiteTotal += lim; penal += item.penalizacion; if (niv) ayudas.push({ n: i + 1, nivel: niv, niveles: p.ayuda });
      var c = comp[d.competencia || "Otras"] || (comp[d.competencia || "Otras"] = { nombre: d.competencia || "Otras", pts: 0, n: 0 });
      c.pts += PUNTOS[d.calidad]; c.n++;
      if (d.calidad !== "optima" && d.tema && !vistos[d.tema]) { vistos[d.tema] = 1; temas.push(d.tema); }
      (d.refs || []).concat(opt ? opt.refs || [] : []).forEach(function (r) { if (!usadas[r]) { usadas[r] = 1; orden.push(r); } });
      return item;
    });
    var competencias = Object.keys(comp).map(function (k) { return { nombre: comp[k].nombre, pct: Math.round(comp[k].pts / (comp[k].n * 10) * 100), n: comp[k].n }; });
    var crudo = camino.reduce(function (s, p) { return s + PUNTOS[p.decision.calidad]; }, 0), maxCrudo = camino.length * 10;
    return { puntos: puntos, max: maxTotal, maxRutaOptima: maximo(caso, caso.inicio), pct: maxTotal ? Math.round(puntos / maxTotal * 100) : 0, pctSinAyudas: maxTotal ? Math.round((puntos + penal) / maxTotal * 100) : 0, crudo: crudo, maxCrudo: maxCrudo, decisiones: decisiones, criticos: criticos, mayores: mayores, competencias: competencias, temas: temas, refsUsadas: orden,
      tiempoTotal: tiempoTotal, limiteTotal: limiteTotal, agotados: agotados, ayudas: ayudas, penalizacion: penal, modo: opts.modo || "entrenamiento" };
  }

  /* ---------- reglas de desenlace (se comprueban al validar el caso) ---------- */
  /* Un desenlace fatal solo es alcanzable pasando por ≥ 2 errores críticos (decisiones «peligrosas») y desde un nodo marcado `deterioro`;
     los errores recuperables nunca llevan a la muerte. Devuelve la lista de problemas (vacía si el caso cumple). */
  function validarDesenlaces(caso) {
    var prob = [], ids = Object.keys(caso.nodos);
    /* mínimo de decisiones no óptimas (y de peligrosas) en cualquier ruta hasta cada nodo */
    var no = {}, pe = {}; no[caso.inicio] = 0; pe[caso.inicio] = 0; var cola = [caso.inicio];
    while (cola.length) {
      var cur = cola.shift(), nd0 = caso.nodos[cur]; if (nd0.final) continue;
      nd0.decisiones.forEach(function (d) {
        var a = no[cur] + (d.calidad === "optima" ? 0 : 1), b = pe[cur] + (d.calidad === "peligrosa" ? 1 : 0), ch = false;
        if (no[d.siguiente] === undefined || a < no[d.siguiente]) { no[d.siguiente] = a; ch = true; }
        if (pe[d.siguiente] === undefined || b < pe[d.siguiente]) { pe[d.siguiente] = b; ch = true; }
        if (ch) cola.push(d.siguiente);
      });
    }
    ids.forEach(function (id) {
      var nd = caso.nodos[id]; if (nd.final) return;
      nd.decisiones.forEach(function (d) {
        var dest = caso.nodos[d.siguiente]; if (!dest) return;
        if (dest.final && dest.final.tipo === "fatal") {
          if (d.calidad !== "peligrosa") prob.push(id + "/" + d.id + ": un desenlace fatal solo puede seguir a una decisión peligrosa");
          if (!nd.deterioro) prob.push(id + "/" + d.id + ": el desenlace fatal debe venir de un nodo de deterioro");
        }
        if (d.calidad === "peligrosa" && !(dest.deterioro || dest.final)) prob.push(id + "/" + d.id + ": una decisión peligrosa debe llevar a deterioro o a un desenlace");
        if (d.calidad === "optima" && dest.final && dest.final.tipo !== "bueno") prob.push(id + "/" + d.id + ": la decisión óptima no puede terminar en desenlace " + dest.final.tipo);
        if (d.calidad === "incorrecta" && dest.deterioro && no[id] < 1) prob.push(id + "/" + d.id + ": un primer error recuperable no puede provocar deterioro (debe haber un error previo)");
      });
    });
    /* la muerte exige ≥ 2 decisiones no óptimas en la ruta, una de ellas peligrosa: nunca «dos respuestas incorrectas y muere» */
    ids.forEach(function (id) { if (caso.nodos[id].final && caso.nodos[id].final.tipo === "fatal" && no[id] !== undefined && (no[id] < 2 || pe[id] < 1)) prob.push(id + ": desenlace fatal alcanzable con menos de 2 decisiones no óptimas o sin ninguna peligrosa"); });
    return prob;
  }

  /* ---------- recomendaciones personalizadas (progreso local del propio alumno) ---------- */
  function rd() { if (typeof module !== "undefined" && module.exports) { try { return require("./rendimiento.js"); } catch (e) { return null; } } return raiz.MQP && raiz.MQP.rendimiento; }
  function estadisticas(preguntas, respuestas, ahora) {
    ahora = ahora || Date.now();
    var R = rd(), base = R ? R.calcular(preguntas, respuestas, [], ahora) : null, porId = {}, ex = {};
    preguntas.forEach(function (q) { porId[q.id] = q; });
    Object.keys(respuestas || {}).forEach(function (id) {
      var r = respuestas[id], q = porId[id]; if (!r || !q) return;
      var e = ex[q.archivo] || (ex[q.archivo] = { nRec: 0, okRec: 0, nHist: 0, okHist: 0 });
      if (r.t && ahora - r.t <= VENTANA_RECIENTE) { e.nRec++; if (r.ok) e.okRec++; } else { e.nHist++; if (r.ok) e.okHist++; }
    });
    var areas = {};
    ((base && base.areas) || []).forEach(function (a) {
      var e = ex[a.archivo] || { nRec: 0, okRec: 0, nHist: 0, okHist: 0 };
      areas[a.archivo] = { archivo: a.archivo, nombre: a.nombre, n: a.n, ok: a.ok, pct: a.pct, lo: a.lo, hi: a.hi, ultimo: a.ultimo, nRec: e.nRec, okRec: e.okRec, nHist: e.nHist, okHist: e.okHist,
        temas: (a.temas || []).filter(function (t) { return t.falladas.length >= 3 && t.tema !== "(sin tema)"; }).map(function (t) { return t.tema; }) };
    });
    return { global: { n: base ? base.global.n : 0 }, areas: areas };
  }
  var NIVEL = { 1: "Nivel 1 · Básico", 2: "Nivel 2 · Intermedio", 3: "Nivel 3 · Avanzado" };
  function recomendar(casos, guardado, est, ahora) {
    ahora = ahora || Date.now();
    var g = (guardado && guardado.casos) || {}, total = est && est.global ? est.global.n : 0;
    function sinJugar(c) { return !g[c.id]; }
    if (!est || total < MIN_TOTAL) {
      var inv = casos.slice().sort(function (a, b) { return (sinJugar(b) - sinJugar(a)) || (a.dificultad - b.dificultad); }).slice(0, 3);
      return { modo: "invitacion", total: total, faltan: Math.max(0, MIN_TOTAL - total), items: inv.map(function (c) { return { caso: c, motivos: ["Buen punto de partida: " + NIVEL[c.dificultad].toLowerCase() + (sinJugar(c) ? " y aún no lo has jugado" : "")], provisional: true }; }) };
    }
    var items = casos.map(function (c) {
      var motivos = [], score = 0, mejorArea = null, juzgables = 0, prov = false;
      (c.areas_banco || []).forEach(function (k) {
        var a = est.areas[k]; if (!a) return;
        if (a.n < MIN_AREA) { prov = true; return; }
        juzgables++;
        var media = (a.ok + 1) / (a.n + 2), s = 0.55 * (1 - media);
        var incert = (a.hi - a.lo) / 100; s += 0.1 * incert;
        var tend = 0;
        if (a.nRec >= 5 && a.nHist >= 5 && a.okRec / a.nRec < a.okHist / a.nHist - 0.1) { tend = 0.15; s += tend; }
        if (a.temas.length) s += 0.1;
        if (!mejorArea || s > mejorArea.s) mejorArea = { s: s, a: a, tend: tend, media: media };
      });
      if (mejorArea) {
        score = mejorArea.s; var a = mejorArea.a;
        motivos.push("Aciertas " + a.pct + " % en " + a.nombre + " (" + a.ok + " de " + a.n + " respuestas; intervalo 95 %: " + a.lo + "–" + a.hi + " %)");
        if (mejorArea.tend) motivos.push("Tu acierto reciente (últimos 14 días: " + Math.round(a.okRec / a.nRec * 100) + " %) es menor que el histórico (" + Math.round(a.okHist / a.nHist * 100) + " %)");
        if (a.temas.length) motivos.push("Tienes fallos repetidos en: " + a.temas.slice(0, 2).join(", "));
      } else { score = 0.15; motivos.push("Aún no tenemos respuestas suficientes en " + (c.areas_banco || []).length + " especialidad(es) de este caso"); }
      var r = g[c.id];
      if (!r) { score += 0.05; motivos.push("Aún no lo has jugado"); }
      else if (r.mejor < 60) { score += 0.1; motivos.push("Tu mejor puntaje fue " + r.mejor + " %: conviene reintentarlo"); }
      else if (r.mejor >= 80) { score -= 0.3; motivos.push("Ya lo dominaste (" + r.mejor + " %)"); }
      return { caso: c, score: score, motivos: motivos, provisional: !juzgables };
    }).sort(function (x, y) { return y.score - x.score; });
    var pocos = items.every(function (i) { return i.provisional; });
    return { modo: pocos ? "provisional" : "personalizado", total: total, items: items.slice(0, 3) };
  }

  var API = { PUNTOS: PUNTOS, ETQ: ETQ, SEVERIDAD: SEVERIDAD, LETRAS: LETRAS, TIEMPOS: TIEMPOS, TIPOS: TIPOS, LIMITES: LIMITES, AVISO_SEG: AVISO_SEG, PENAL_AYUDA: PENAL_AYUDA, MODOS: MODOS, MIN_TOTAL: MIN_TOTAL, MIN_AREA: MIN_AREA, NIVEL: NIVEL, CONVERSIONES: CONVERSIONES,
    peso: peso, maximo: maximo, maximoRecorrido: maximoRecorrido, porcentaje: porcentaje, desbloqueado: desbloqueado, puntosNodo: puntosNodo, registrar: registrar, barajar: barajar, tiempoNodo: tiempoNodo, crearReloj: crearReloj, formatoTiempo: formatoTiempo,
    serializarSesion: serializarSesion, restaurarSesion: restaurarSesion, consultarEspecialista: consultarEspecialista, ayudaDisponible: ayudaDisponible, intervaloAplicable: intervaloAplicable, marca: marca, convertir: convertir,
    analizar: analizar, validarDesenlaces: validarDesenlaces, estadisticas: estadisticas, recomendar: recomendar };
  if (typeof module !== "undefined" && module.exports) module.exports = API; else (raiz.MQP = raiz.MQP || {}).guardiaNucleo = API;
})(typeof window !== "undefined" ? window : this);
