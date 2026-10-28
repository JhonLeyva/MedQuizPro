/* MedQuizPlus · «Sobrevive a la Guardia» v2: motor, recomendaciones personalizadas e informe del caso.
   El caso avanza SOLO por las transiciones definidas en guardia_casos.js (generado desde guardia/casos/*.json). No hay IA dentro del juego:
   la evolución, el puntaje y el informe salen de datos validados. El progreso se guarda en M.progreso.preferencia("guardia"),
   que ya se sincroniza con la cuenta del alumno. Simulación educativa: no dirige la atención de pacientes reales. */
(function (raiz) {
  "use strict";
  var PUNTOS = { optima: 10, aceptable: 5, incorrecta: 0, peligrosa: 0 };
  var ETQ = { optima: "Decisión óptima", aceptable: "Aceptable, mejorable", incorrecta: "Incorrecta", peligrosa: "Peligrosa" };
  var SEVERIDAD = { optima: "Correcta", aceptable: "Mejorable (sin daño probable)", incorrecta: "Error mayor", peligrosa: "Error crítico (riesgo vital)" };
  var GRAV = ["Estable", "Inestable", "Crítico"];
  var NIVEL = { 1: "Nivel 1 · Básico", 2: "Nivel 2 · Intermedio", 3: "Nivel 3 · Avanzado" };
  var MIN_TOTAL = 30;       // respuestas mínimas en el banco para personalizar
  var MIN_AREA = 8;         // respuestas mínimas en una especialidad para juzgarla
  var VENTANA_RECIENTE = 14 * 86400000;
  var DIA = 86400000;

  /* ---------- lógica pura (se prueba en Node) ---------- */
  function maximo(caso, id, memo) {
    memo = memo || {};
    if (memo[id] !== undefined) return memo[id];
    var n = caso.nodos[id], mx = 0;
    if (!n.final) n.decisiones.forEach(function (d) { mx = Math.max(mx, PUNTOS[d.calidad] + maximo(caso, d.siguiente, memo)); });
    return (memo[id] = mx);
  }
  function porcentaje(caso, puntos) { var m = maximo(caso, caso.inicio); return m ? Math.round(puntos / m * 100) : 0; }
  /* estado guardado: { casos: { id: { mejor, intentos, completados, ultimo, final, criticos, t } } }. Los ids de casos archivados se conservan. */
  function desbloqueado(caso, guardado) {
    if (!caso.requiere) return true;
    var r = guardado && guardado.casos && guardado.casos[caso.requiere.caso];
    return !!(r && r.mejor >= caso.requiere.minimo);
  }
  function registrar(guardado, caso, resultado, ahora) {
    var g = JSON.parse(JSON.stringify(guardado || { casos: {} })); g.casos = g.casos || {};
    var r = g.casos[caso.id] || { mejor: 0, intentos: 0, completados: 0 };
    r.intentos++; r.completados++; r.mejor = Math.max(r.mejor, resultado.pct); r.ultimo = resultado.pct; r.final = resultado.tipo; r.criticos = resultado.criticos || 0; r.t = ahora || Date.now();
    g.casos[caso.id] = r; return g;
  }
  function barajar(a) { var b = a.slice(); for (var i = b.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = b[i]; b[i] = b[j]; b[j] = t; } return b; }

  /* Análisis del recorrido del alumno: todo el informe D/F sale de sus decisiones reales (camino: [{nodo, decision}]). */
  function analizar(caso, camino, puntos) {
    var maxTotal = maximo(caso, caso.inicio), criticos = [], mayores = [], comp = {}, temas = [], vistos = {}, usadas = {}, orden = [];
    var decisiones = camino.map(function (p, i) {
      var d = p.decision, opt = p.nodo.decisiones.filter(function (x) { return x.calidad === "optima"; })[0];
      var item = { n: i + 1, estado: p.nodo.estado, elegida: d, optima: opt, severidad: SEVERIDAD[d.calidad],
        alternativas: p.nodo.decisiones.filter(function (x) { return x.id !== d.id && x.id !== opt.id; }) };
      if (d.calidad === "peligrosa") criticos.push(item); else if (d.calidad === "incorrecta") mayores.push(item);
      var c = comp[d.competencia || "Otras"] || (comp[d.competencia || "Otras"] = { nombre: d.competencia || "Otras", pts: 0, n: 0 });
      c.pts += PUNTOS[d.calidad]; c.n++;
      if (d.calidad !== "optima" && d.tema && !vistos[d.tema]) { vistos[d.tema] = 1; temas.push(d.tema); }
      (d.refs || []).concat(opt ? opt.refs || [] : []).forEach(function (r) { if (!usadas[r]) { usadas[r] = 1; orden.push(r); } });
      return item;
    });
    var competencias = Object.keys(comp).map(function (k) { return { nombre: comp[k].nombre, pct: Math.round(comp[k].pts / (comp[k].n * 10) * 100), n: comp[k].n }; });
    return { puntos: puntos, max: maxTotal, pct: porcentaje(caso, puntos), decisiones: decisiones, criticos: criticos, mayores: mayores, competencias: competencias, temas: temas, refsUsadas: orden };
  }

  /* ---------- recomendaciones personalizadas (sin tocar el servidor: solo el progreso local del propio alumno) ---------- */
  function rd() { if (typeof module !== "undefined" && module.exports) { try { return require("./rendimiento.js"); } catch (e) { return null; } } return raiz.MQP && raiz.MQP.rendimiento; }
  /* estadísticas por especialidad del banco: acierto, intervalo de Wilson, reciente vs histórico y temas con fallos repetidos */
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
        var media = (a.ok + 1) / (a.n + 2), s = 0.55 * (1 - media);               // debilidad con prior Beta(1,1): pocos datos tienden al 50 %
        var incert = (a.hi - a.lo) / 100; s += 0.1 * incert;                         // intervalo de Wilson ancho = estimación poco firme
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

  var API = { maximo: maximo, porcentaje: porcentaje, desbloqueado: desbloqueado, registrar: registrar, analizar: analizar, estadisticas: estadisticas, recomendar: recomendar, PUNTOS: PUNTOS, MIN_TOTAL: MIN_TOTAL, MIN_AREA: MIN_AREA };
  if (typeof module !== "undefined" && module.exports) { module.exports = API; return; }

  /* ---------- interfaz ---------- */
  var M = raiz.MQP || (raiz.MQP = {});
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function url(u) { return /^https?:\/\//i.test(u || "") ? u : ""; }
  function enlace(href, txt) { return url(href) ? '<a href="' + esc(href) + '" target="_blank" rel="noopener noreferrer">' + esc(txt) + '</a>' : esc(txt); }
  function cargar() { var g = M.progreso && M.progreso.preferencia("guardia"); return g && g.casos ? g : { casos: {} }; }
  function guardar(g) { if (M.progreso) M.progreso.preferencia("guardia", g); }
  var AVISO = "Simulación educativa. No sirve para dirigir la atención de pacientes reales ni sustituye el juicio clínico ni los protocolos de tu institución.";
  var IMG = function () { return raiz.MQP_GUARDIA_IMG || {}; };
  function licenciaCorta(u) { var m = /licenses\/([a-z-]+)\/([\d.]+)/i.exec(u || ""); return m ? "CC " + m[1].toUpperCase() + " " + m[2] : "licencia abierta"; }
  function abrirImagen(id, disparador) {
    var im = IMG()[id]; if (!im || !M.visorImagen) return;
    M.visorImagen.abrir({ titulo: "Imagen del caso", alt: im.alt, imagenes: [im.src],
      atribucion: { nota: "Imagen real de la literatura médica publicada, de otro paciente.", licencia: licenciaCorta(im.licencia), licenciaUrl: im.licencia, fuente: "autoría y fuente completas en el informe final del caso" } }, disparador);
  }
  function refN(caso, ids) { return (ids || []).map(function (r) { for (var i = 0; i < caso.referencias.length; i++) if (caso.referencias[i].id === r) return i + 1; return null; }).filter(Boolean); }

  /* ----- lista + recomendaciones ----- */
  var cacheEst = { clave: "", valor: null };
  function estadisticasAlumno(datos) {
    if (!datos || !datos.preguntas || !M.progreso) return null;
    var p = M.progreso.leer(), resp = p.respuestas || {}, ids = Object.keys(resp), tmax = 0;
    ids.forEach(function (i) { if (resp[i] && resp[i].t > tmax) tmax = resp[i].t; });
    var clave = ids.length + ":" + tmax + ":" + Math.floor(Date.now() / DIA);      // se recalcula solo si cambian las respuestas (o pasa un día)
    if (cacheEst.clave !== clave) cacheEst = { clave: clave, valor: estadisticas(datos.preguntas, resp, Date.now()) };
    return cacheEst.valor;
  }
  function tarjetaRecomendada(rec) {
    var enc = rec.modo === "personalizado" ? "Casos recomendados para ti" : rec.modo === "provisional" ? "Casos recomendados para ti (provisional)" : "Por dónde empezar";
    var intro = rec.modo === "invitacion"
      ? "Todavía no tenemos suficientes respuestas tuyas en el banco (" + rec.total + " de " + MIN_TOTAL + ") para recomendarte con criterio, así que no inventamos una recomendación. Estos son buenos puntos de partida; responde preguntas en el banco" + (rec.faltan ? " (te faltan " + rec.faltan + ")" : "") + " para personalizarlos."
      : rec.modo === "provisional"
        ? "Tenemos pocas respuestas en las especialidades de estos casos, por eso la sugerencia es provisional y se afina a medida que practicas."
        : "Calculado con tus propias respuestas en el banco (acierto por especialidad con su intervalo de confianza, tendencia reciente frente a histórica, temas con fallos repetidos y tu historial en la guardia).";
    return '<section class="card card--spaced gd-rec" aria-labelledby="gdRecT"><h2 class="card__h" id="gdRecT">' + enc + '</h2><p class="muted small">' + esc(intro) + '</p><ul class="gd-rec__l">' + rec.items.map(function (i) {
      return '<li class="gd-rec__i"><p class="gd-niv">' + esc(NIVEL[i.caso.dificultad]) + ' · ' + esc(i.caso.especialidad) + (i.provisional ? ' · <span class="gd-prov">provisional</span>' : "") + '</p><h3>' + esc(i.caso.titulo) + '</h3><ul class="gd-rec__m">' + i.motivos.map(function (m) { return '<li>' + esc(m) + '</li>'; }).join("") + '</ul><a class="btn btn--primary btn--sm" href="#/guardia/' + esc(i.caso.id) + '">Empezar el caso</a></li>';
    }).join("") + '</ul><p class="muted small">Es una sugerencia, no una restricción: todos los casos están abiertos abajo. Se calcula en tu navegador con tu progreso; no se envía nada a ningún servidor ni se comparte con otros alumnos.</p></section>';
  }
  function especialidades(casos) { var s = {}; casos.forEach(function (c) { c.especialidad.split(" · ").forEach(function (x) { s[x] = 1; }); }); return Object.keys(s).sort(); }

  function lista(cont, datos) {
    var g = cargar(), casos = raiz.MQP_GUARDIA || [];
    var hechos = casos.filter(function (c) { return g.casos[c.id]; }).length;
    var rec = recomendar(casos, g, estadisticasAlumno(datos), Date.now());
    var h = '<header class="page-head"><p class="kicker">Simulador</p><h1 class="page-head__title">Sobrevive a la Guardia</h1><p class="page-head__lead">Diez casos clínicos por decisiones, con bibliografía verificable e imágenes reales: eliges la conducta, el caso evoluciona y al final recibes un informe con tu razonamiento, tus errores y qué reforzar. Complementa al banco de preguntas.</p></header>' +
      '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
      '<dl class="gd-kpis"><div class="gd-kpi"><dt>Casos completados</dt><dd>' + hechos + ' / ' + casos.length + '</dd></div><div class="gd-kpi"><dt>Mejor puntaje medio</dt><dd>' + (hechos ? Math.round(casos.reduce(function (s, c) { return s + (g.casos[c.id] ? g.casos[c.id].mejor : 0); }, 0) / hechos) + " %" : "—") + '</dd></div></dl>' +
      tarjetaRecomendada(rec) +
      '<div class="gd-filtro"><label for="gdFil">Explorar por especialidad</label><select id="gdFil"><option value="">Todas las especialidades (' + casos.length + ' casos)</option>' + especialidades(casos).map(function (e) { return '<option value="' + esc(e) + '">' + esc(e) + '</option>'; }).join("") + '</select></div>' +
      '<ul class="gd-lista" id="gdLista">' + casos.map(function (c) {
        var r = g.casos[c.id], tieneImg = (c.imagenes || []).length;
        return '<li class="gd-caso" data-esp="' + esc(c.especialidad) + '"><p class="gd-niv">' + esc(NIVEL[c.dificultad]) + ' · ' + esc(c.especialidad) + '</p><h2>' + esc(c.titulo) + '</h2><p>' + esc(c.resumen) + '</p>' +
          '<p class="muted small">≈ ' + c.duracion_min + ' min · ' + c.referencias.length + ' referencias verificables' + (tieneImg ? ' · ' + (tieneImg === 1 ? "1 imagen real" : tieneImg + " imágenes reales") : "") + '</p>' +
          (r ? '<p class="gd-mejor">Mejor puntaje: <b>' + r.mejor + ' %</b> · Intentos: ' + r.intentos + '</p>' : "") +
          '<a class="btn btn--primary btn--sm" href="#/guardia/' + esc(c.id) + '">' + (r ? "Reintentar el caso" : "Empezar el caso") + '</a></li>';
      }).join("") + '</ul>';
    cont.innerHTML = h;
    var f = cont.querySelector("#gdFil");
    f.addEventListener("change", function () { [].forEach.call(cont.querySelectorAll(".gd-caso"), function (li) { li.hidden = !!f.value && li.getAttribute("data-esp").split(" · ").indexOf(f.value) < 0; }); });
  }

  /* ----- un caso ----- */
  function figura(id, consigna, final) {
    var im = IMG()[id]; if (!im) return "";
    return '<figure class="gd-img"><button type="button" class="gd-img__b" data-img="' + esc(id) + '" aria-label="Ampliar la imagen del caso (zoom y desplazamiento)"><img src="' + esc(im.src) + '" alt="' + esc(im.alt) + '" width="' + im.ancho + '" height="' + im.alto + '"></button>' +
      '<figcaption>' + (consigna ? '<strong>' + esc(consigna) + '</strong><br>' : "") + 'Imagen real de la literatura médica publicada, de otro paciente (' + esc(licenciaCorta(im.licencia)) + ').' + (final ? ' Autoría y fuente en la ficha de abajo.' : ' La autoría y la fuente completas aparecen en el informe final para no adelantar el diagnóstico.') + ' Pulsa la imagen para ampliarla, desplazarla y ajustar brillo y contraste.</figcaption></figure>';
  }
  function ligarImagenes(cont) { [].forEach.call(cont.querySelectorAll("[data-img]"), function (b) { b.addEventListener("click", function () { abrirImagen(b.getAttribute("data-img"), b); }); }); }

  function jugar(cont, caso) {
    var g0 = cargar();
    if (!desbloqueado(caso, g0)) { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">Este caso aún está bloqueado</p><a class="btn btn--primary" href="#/guardia">Volver a los casos</a></div>'; return; }
    var nodo = caso.nodos[caso.inicio], puntos = 0, camino = [], tInicio = 0, usarTiempo = false, reloj = null, bloqueado = false, vistas = [];
    var maxTotal = maximo(caso, caso.inicio);

    function pararReloj() { if (reloj) { clearInterval(reloj); reloj = null; } }
    function paso() {
      pararReloj();
      if (nodo.final) { fin(); return; }
      bloqueado = false; tInicio = Date.now();
      if (nodo.imagen && vistas.indexOf(nodo.imagen.id) < 0) vistas.push(nodo.imagen.id);
      var opciones = barajar(nodo.decisiones);
      var vit = Object.keys(nodo.vitales).map(function (k) { return '<div><dt>' + esc(k) + '</dt><dd>' + esc(nodo.vitales[k]) + '</dd></div>'; }).join("");
      var previas = vistas.filter(function (i) { return !nodo.imagen || i !== nodo.imagen.id; });
      cont.innerHTML = '<div class="gd-juego"><header class="gd-top"><a class="link-arrow" href="#/guardia">← Casos</a><h1>' + esc(caso.titulo) + '</h1>' +
        '<p class="gd-prog">Decisión ' + (camino.length + 1) + ' · Puntaje ' + puntos + ' / ' + maxTotal + '</p></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        (camino.length === 0 ? '<p class="muted small gd-ctx">' + esc(caso.contexto) + '</p>' : "") +
        '<section class="gd-paciente" aria-label="Estado del paciente"><div class="gd-grav gd-grav--' + nodo.gravedad + '" role="status"><span aria-hidden="true"></span>Estado: <b>' + GRAV[nodo.gravedad] + '</b></div>' +
        '<p class="gd-estado">' + esc(nodo.estado) + '</p><dl class="gd-vit">' + vit + '</dl></section>' +
        (nodo.imagen ? figura(nodo.imagen.id, nodo.imagen.consigna) : "") +
        (previas.length ? '<p class="gd-prev"><span>Imágenes de este caso (puedes volver a verlas):</span> ' + previas.map(function (i, k) { return '<button type="button" class="btn btn--ghost btn--sm" data-img="' + esc(i) + '">Ver imagen ' + (k + 1) + '</button>'; }).join(" ") + '</p>' : "") +
        '<label class="gd-tiempo"><input type="checkbox" id="gdT"' + (usarTiempo ? " checked" : "") + '> Mostrar cronómetro de la decisión (solo informativo: no quita puntos)</label><p class="gd-crono" id="gdC" aria-live="off" hidden></p>' +
        '<h2 class="gd-q">¿Qué haces ahora?</h2><div class="gd-ops" role="group" aria-label="Decisiones">' + opciones.map(function (o) { return '<button type="button" class="gd-op" data-id="' + esc(o.id) + '">' + esc(o.texto) + '</button>'; }).join("") + '</div>' +
        '<div id="gdFb" role="status" aria-live="polite"></div></div>';
      ligarImagenes(cont);
      var t = cont.querySelector("#gdT"), c = cont.querySelector("#gdC");
      function tic() { var s = Math.floor((Date.now() - tInicio) / 1000); c.textContent = "Llevas " + s + " s en esta decisión"; }
      function reloj_() { c.hidden = !t.checked; pararReloj(); if (t.checked) { tic(); reloj = setInterval(tic, 1000); } }
      t.addEventListener("change", function () { usarTiempo = t.checked; reloj_(); }); if (usarTiempo) reloj_();
      [].forEach.call(cont.querySelectorAll(".gd-op"), function (b) { b.addEventListener("click", function () { elegir(b.getAttribute("data-id")); }); });
    }
    function elegir(id) {
      if (bloqueado) return; bloqueado = true; pararReloj();
      var d = nodo.decisiones.filter(function (x) { return x.id === id; })[0]; if (!d) return;
      var seg = Math.round((Date.now() - tInicio) / 1000);
      puntos += PUNTOS[d.calidad]; camino.push({ nodo: nodo, decision: d, segundos: seg });
      [].forEach.call(cont.querySelectorAll(".gd-op"), function (b) {
        b.disabled = true; var x = nodo.decisiones.filter(function (z) { return z.id === b.getAttribute("data-id"); })[0];
        if (x.id === d.id) b.classList.add("is-sel", "is-" + x.calidad); else if (x.calidad === "optima") b.classList.add("is-mejor");
      });
      var sig = caso.nodos[d.siguiente];
      var opt = nodo.decisiones.filter(function (x) { return x.calidad === "optima"; })[0], rn = refN(caso, d.refs);
      cont.querySelector("#gdFb").innerHTML = '<div class="gd-fb gd-fb--' + d.calidad + '"><p class="gd-fb__t">' + ETQ[d.calidad] + ' · ' + PUNTOS[d.calidad] + ' pts</p><p>' + esc(d.explicacion) + '</p>' +
        (d.calidad !== "optima" ? '<p class="gd-fb__opt"><b>Lo óptimo era:</b> ' + esc(opt.texto) + '</p>' : "") +
        (rn.length ? '<p class="muted small">Respaldo: referencia' + (rn.length > 1 ? "s " : " ") + rn.join(", ") + ' (detalle completo al terminar el caso).</p>' : "") +
        '<button type="button" class="btn btn--primary" id="gdSig">' + (sig.final ? "Ver el desenlace y el informe" : "Continuar: ver la evolución") + '</button></div>';
      var bt = cont.querySelector("#gdSig"); bt.focus(); bt.addEventListener("click", function () { nodo = sig; paso(); });
    }

    /* ---- informe final A–F ---- */
    function refHtml(r, n, usada) {
      var ids = [];
      if (r.pmid) ids.push(enlace("https://pubmed.ncbi.nlm.nih.gov/" + r.pmid + "/", "PMID " + r.pmid));
      if (r.doi) ids.push(enlace("https://doi.org/" + r.doi, "DOI " + r.doi));
      if (r.url) ids.push(enlace(r.url, "Enlace"));
      return '<li class="gd-ref"><p><b>[' + n + ']</b> ' + esc(r.titulo) + (usada ? ' <span class="gd-prov">usada en tus decisiones</span>' : "") + '</p>' +
        '<p class="muted small">' + esc(r.organismo) + ' · ' + esc(r.autores) + ' · ' + esc(r.anio) + (r.version ? " · " + esc(r.version) : "") + ' · ' + esc(({ guia: "Guía", consenso: "Consenso", revision: "Revisión sistemática/narrativa", ensayo: "Ensayo clínico", norma: "Norma" })[r.tipo] || r.tipo) + '</p>' +
        '<p class="muted small">' + ids.join(" · ") + ' · Consultada el ' + esc(r.fecha_consulta) + '</p>' +
        '<p class="small"><b>Qué recomienda (con nuestras palabras):</b> ' + esc(r.recomendacion) + '</p><p class="muted small"><b>Vigencia:</b> ' + esc(r.vigencia) + '</p></li>';
    }
    function fin() {
      var f = nodo.final, an = analizar(caso, camino, puntos), pct = an.pct, inf = caso.informe, IM = IMG();
      var g = registrar(cargar(), caso, { pct: pct, tipo: f.tipo, criticos: an.criticos.length }); guardar(g);
      var rel = (inf.casos_relacionados || []).map(function (id) { return (raiz.MQP_GUARDIA || []).filter(function (c) { return c.id === id; })[0]; }).filter(Boolean);
      var usadas = {}; an.refsUsadas.forEach(function (r) { usadas[r] = 1; });
      var h = '<div class="gd-juego gd-informe"><header class="gd-top"><a class="link-arrow" href="#/guardia">← Casos</a><h1>' + esc(caso.titulo) + '</h1></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<section class="gd-final gd-final--' + f.tipo + '"><p class="gd-niv">Desenlace</p><h2>' + esc(f.titulo) + '</h2><p>' + esc(f.mensaje) + '</p><p class="gd-pts"><b>' + pct + ' %</b><span>' + puntos + ' de ' + an.max + ' puntos posibles</span></p></section>' +
        '<nav class="gd-indice" aria-label="Secciones del informe"><a href="#gdA">A. Resumen</a> <a href="#gdB">B. Razonamiento</a>' + (caso.imagenes.length ? ' <a href="#gdC">C. Imágenes</a>' : "") + ' <a href="#gdD">D. Tus decisiones</a> <a href="#gdE">E. Tratamiento</a> <a href="#gdF">F. Resultado y referencias</a></nav>';
      /* A */
      h += '<section class="card card--spaced" id="gdA"><h2 class="card__h">A. Resumen clínico</h2><p>' + esc(inf.resumen_clinico) + '</p></section>';
      /* B */
      h += '<section class="card card--spaced" id="gdB"><h2 class="card__h">B. Razonamiento paso a paso</h2><p class="muted small">Así se razona el caso de forma ideal:</p><ol class="gd-razon">' + inf.razonamiento.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ol>' +
        '<p class="muted small">Tu recorrido:</p><ol class="gd-trail">' + camino.map(function (p) { return '<li class="gd-t gd-t--' + p.decision.calidad + '"><p><b>' + ETQ[p.decision.calidad] + ':</b> ' + esc(p.decision.texto) + '</p><p class="muted small">Tiempo: ' + p.segundos + ' s (informativo)</p></li>'; }).join("") + '</ol></section>';
      /* C */
      if (caso.imagenes.length) {
        h += '<section class="card card--spaced" id="gdC"><h2 class="card__h">C. Interpretación de las imágenes</h2><p>' + esc(inf.imagen_interpretacion) + '</p>';
        caso.imagenes.forEach(function (id) {
          var im = IM[id], r = im.revelar;
          h += figura(id, "", true) + '<details class="gd-reg"><summary>Ficha de la imagen: fuente, autoría, licencia y modificaciones</summary><dl class="gd-dl">' +
            '<div><dt>Figura original</dt><dd>' + esc(r.titulo_figura) + '</dd></div><div><dt>Modalidad y región</dt><dd>' + esc(r.modalidad) + ' · ' + esc(r.region) + '</dd></div><div><dt>Hallazgo evaluado</dt><dd>' + esc(r.hallazgo) + '</dd></div>' +
            '<div><dt>Artículo</dt><dd>' + esc(r.articulo) + ' (' + esc(r.autores) + '; ' + esc(r.revista) + ', ' + esc(r.anio) + ') · ' + enlace("https://pubmed.ncbi.nlm.nih.gov/" + r.pmid + "/", "PMID " + r.pmid) + ' · ' + enlace(r.enlace, r.pmcid) + '</dd></div>' +
            '<div><dt>Fuente de la imagen</dt><dd>' + esc(r.fuente) + '</dd></div><div><dt>Licencia</dt><dd>' + enlace(im.licencia, licenciaCorta(im.licencia)) + ' · ' + esc(r.copyright) + '</dd></div>' +
            '<div><dt>Modificaciones</dt><dd>' + esc(r.modificaciones) + '</dd></div><div><dt>Licencia verificada el</dt><dd>' + esc(r.verificada_el) + '</dd></div></dl></details>';
        });
        h += '<p class="muted small">La imagen procede de otro paciente, sin datos identificables. Es material educativo: no sustituye el informe radiológico.</p></section>';
      }
      /* D */
      h += '<section class="card card--spaced" id="gdD"><h2 class="card__h">D. Análisis de tus decisiones</h2>' + an.decisiones.map(function (x) {
        var rn = refN(caso, x.elegida.refs);
        return '<details class="gd-dec gd-dec--' + x.elegida.calidad + '"' + (x.elegida.calidad !== "optima" ? " open" : "") + '><summary>Decisión ' + x.n + ': ' + esc(x.severidad) + '</summary>' +
          '<p class="gd-t__e">' + esc(x.estado.slice(0, 160)) + (x.estado.length > 160 ? "…" : "") + '</p>' +
          '<p><b>Tu respuesta:</b> ' + esc(x.elegida.texto) + '</p><p class="small">' + esc(x.elegida.explicacion) + '</p>' +
          (x.elegida.calidad !== "optima" ? '<p><b>Lo preferible:</b> ' + esc(x.optima.texto) + '</p><p class="small"><b>Por qué:</b> ' + esc(x.optima.explicacion) + '</p>' : '<p class="small">Fue la mejor opción disponible.</p>') +
          (x.alternativas.length ? '<p class="small"><b>Por qué las otras opciones eran inferiores:</b></p><ul class="gd-alt">' + x.alternativas.map(function (a) { return '<li><b>' + esc(a.texto) + '</b> (' + ETQ[a.calidad].toLowerCase() + '): ' + esc(a.explicacion) + '</li>'; }).join("") + '</ul>' : "") +
          (rn.length ? '<p class="muted small">Respaldo: referencia' + (rn.length > 1 ? "s " : " ") + rn.join(", ") + '.</p>' : "") + '</details>';
      }).join("") + '</section>';
      /* E */
      h += '<section class="card card--spaced" id="gdE"><h2 class="card__h">E. Tratamiento y seguimiento</h2><div class="gd-tabla">' + inf.tratamiento.map(function (t) {
        return '<div class="gd-tr"><p class="gd-tr__i"><b>' + esc(t.item) + '</b></p><p>' + esc(t.detalle) + '</p><p class="muted small"><b>Dosis / unidades:</b> ' + esc(t.dosis) + '</p></div>'; }).join("") + '</div>' +
        '<p class="muted small">No se fija una dosis universal cuando depende del peso, la función renal, la edad o el protocolo local; consulta la guía y el protocolo vigentes de tu institución.</p></section>';
      /* F */
      h += '<section class="card card--spaced" id="gdF"><h2 class="card__h">F. Resultado y refuerzo</h2><p><b>Puntaje:</b> ' + puntos + ' de ' + an.max + ' (' + pct + ' %) · <b>Errores críticos:</b> ' + an.criticos.length + ' · <b>Errores mayores:</b> ' + an.mayores.length + '</p>' +
        (an.criticos.length ? '<ul class="gd-crit">' + an.criticos.map(function (x) { return '<li>Decisión ' + x.n + ': ' + esc(x.elegida.texto) + '</li>'; }).join("") + '</ul>' : '<p class="small">No cometiste errores críticos (decisiones que ponen en riesgo la vida).</p>') +
        '<h3 class="gd-h3">Competencias</h3><ul class="gd-comp">' + an.competencias.map(function (c) { return '<li><span>' + esc(c.nombre) + '</span><span class="gd-barra" aria-hidden="true"><i style="width:' + c.pct + '%"></i></span><b>' + c.pct + ' %</b></li>'; }).join("") + '</ul>' +
        '<h3 class="gd-h3">Qué reforzar</h3>' + (an.temas.length ? '<ul class="gd-temas">' + an.temas.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join("") + '</ul>' : '<p class="small">Todas tus decisiones fueron las óptimas. ¡Buen trabajo!</p>') +
        '<p class="muted small">Temas relacionados para el banco: ' + inf.temas_relacionados.map(esc).join(" · ") + '.</p><p class="gd-clave"><b>Idea clave:</b> ' + esc(inf.mensaje_clave) + '</p>' +
        (rel.length ? '<p class="small"><b>Casos relacionados:</b> ' + rel.map(function (c) { return '<a href="#/guardia/' + esc(c.id) + '">' + esc(c.titulo) + '</a>'; }).join(" · ") + '</p>' : "") +
        '<h3 class="gd-h3">Referencias del caso</h3><ul class="gd-refs">' + caso.referencias.map(function (r, i) { return refHtml(r, i + 1, usadas[r.id]); }).join("") + '</ul>' +
        '<h3 class="gd-h3">Diferencias entre fuentes y limitaciones</h3><ul>' + caso.discrepancias.map(function (x) { return '<li class="small">' + esc(x) + '</li>'; }).join("") + '</ul>' +
        '<p class="muted small">Caso redactado a partir de las fuentes citadas; no fue revisado por un especialista externo. Si ves una discrepancia con tu guía vigente, prevalece la guía.</p></section>' +
        '<div class="gd-acc"><a class="btn btn--primary" href="#/guardia/' + esc(caso.id) + '" data-reintentar>Reintentar el caso</a><a class="btn btn--ghost" href="#/guardia">Volver a los casos</a>' +
        rel.slice(0, 1).map(function (c) { return '<a class="btn btn--ghost" href="#/guardia/' + esc(c.id) + '">Siguiente: ' + esc(c.titulo) + '</a>'; }).join("") + '</div></div>';
      cont.innerHTML = h; ligarImagenes(cont);
      var re = cont.querySelector("[data-reintentar]"); re.addEventListener("click", function (ev) { ev.preventDefault(); jugar(cont, caso); window.scrollTo(0, 0); });
      window.scrollTo(0, 0);
    }
    paso();
  }

  var dentro = false;     // true mientras el alumno navega dentro de #/guardia: evita repetir la introducción
  window.addEventListener("hashchange", function () { if (!/^#\/guardia/.test(location.hash)) dentro = false; });
  function montar(cont, arg, datos) {
    var casos = raiz.MQP_GUARDIA || [];
    var caso = arg ? casos.filter(function (c) { return c.id === arg; })[0] : null;
    var primeraEntrada = !dentro; dentro = true;      // cualquier pantalla del módulo cuenta como «ya estoy dentro»
    if (arg && !caso) { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">No encontramos ese caso</p><a class="btn btn--primary" href="#/guardia">Ver los casos</a></div>'; return; }
    if (caso) { jugar(cont, caso); return; }
    lista(cont, datos);
    var I = M.guardiaIntro;
    var rep = document.createElement("p"); rep.className = "gd-repetir";
    rep.innerHTML = '<button type="button" class="link-arrow" id="gdVerIntro">▶ Ver la introducción</button>';
    var kp = cont.querySelector(".gd-aviso");
    if (kp && I) { kp.after(rep); rep.querySelector("button").addEventListener("click", function () { I.mostrar({}); }); }
    /* La introducción aparece al ENTRAR al módulo desde fuera (no al volver a la lista desde un caso) y salvo que el alumno la haya omitido */
    if (I && primeraEntrada && !I.omitida() && !document.querySelector(".gi"))
      I.mostrar({ alTerminar: function () { var b = cont.querySelector("a.btn"); if (b) b.focus({ preventScroll: true }); } });
  }
  API.montar = montar; M.guardia = API;
})(typeof window !== "undefined" ? window : this);
