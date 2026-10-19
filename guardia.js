/* MedQuizPlus · «Sobrevive a la Guardia»: motor y pantallas.
   El caso avanza SOLO por las transiciones definidas en guardia_casos.js. El progreso se guarda en M.progreso.preferencia("guardia"),
   que ya se sincroniza con la cuenta del alumno. Simulación educativa: no dirige la atención de pacientes reales. */
(function (raiz) {
  "use strict";
  var PUNTOS = { optima: 10, aceptable: 5, incorrecta: 0, peligrosa: 0 };
  var ETQ = { optima: "Decisión óptima", aceptable: "Aceptable, mejorable", incorrecta: "Incorrecta", peligrosa: "Peligrosa" };
  var GRAV = ["Estable", "Inestable", "Crítico"];
  var NIVEL = { 1: "Nivel 1 · Básico", 2: "Nivel 2 · Intermedio", 3: "Nivel 3 · Avanzado" };

  /* ---------- lógica pura (se prueba en Node) ---------- */
  function maximo(caso, id, memo) {
    memo = memo || {};
    if (memo[id] !== undefined) return memo[id];
    var n = caso.nodos[id], mx = 0;
    if (!n.final) n.decisiones.forEach(function (d) { mx = Math.max(mx, PUNTOS[d.calidad] + maximo(caso, d.siguiente, memo)); });
    return (memo[id] = mx);
  }
  function porcentaje(caso, puntos) { var m = maximo(caso, caso.inicio); return m ? Math.round(puntos / m * 100) : 0; }
  /* estado guardado: { casos: { id: { mejor, intentos, completados, ultimo, t } } } */
  function desbloqueado(caso, guardado) {
    if (!caso.requiere) return true;
    var r = guardado && guardado.casos && guardado.casos[caso.requiere.caso];
    return !!(r && r.mejor >= caso.requiere.minimo);
  }
  function registrar(guardado, caso, resultado, ahora) {
    var g = JSON.parse(JSON.stringify(guardado || { casos: {} })); g.casos = g.casos || {};
    var r = g.casos[caso.id] || { mejor: 0, intentos: 0, completados: 0 };
    r.intentos++; r.completados++; r.mejor = Math.max(r.mejor, resultado.pct); r.ultimo = resultado.pct; r.final = resultado.tipo; r.t = ahora || Date.now();
    g.casos[caso.id] = r; return g;
  }
  function barajar(a) { var b = a.slice(); for (var i = b.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = b[i]; b[i] = b[j]; b[j] = t; } return b; }

  var API = { maximo: maximo, porcentaje: porcentaje, desbloqueado: desbloqueado, registrar: registrar, PUNTOS: PUNTOS };
  if (typeof module !== "undefined" && module.exports) { module.exports = API; return; }

  /* ---------- interfaz ---------- */
  var M = raiz.MQP || (raiz.MQP = {});
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function cargar() { var g = M.progreso && M.progreso.preferencia("guardia"); return g && g.casos ? g : { casos: {} }; }
  function guardar(g) { if (M.progreso) M.progreso.preferencia("guardia", g); }
  var AVISO = "Simulación educativa. No sirve para dirigir la atención de pacientes reales ni sustituye el juicio clínico ni los protocolos de tu institución.";

  function lista(cont) {
    var g = cargar(), casos = raiz.MQP_GUARDIA || [];
    var hechos = casos.filter(function (c) { return g.casos[c.id]; }).length;
    var h = '<header class="page-head"><p class="kicker">Simulador</p><h1 class="page-head__title">Sobrevive a la Guardia</h1><p class="page-head__lead">Casos clínicos por decisiones: eliges la conducta, el caso evoluciona y al final ves tu puntaje, tus errores y qué reforzar. Complementa al banco de preguntas.</p></header>' +
      '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
      '<dl class="gd-kpis"><div class="gd-kpi"><dt>Casos completados</dt><dd>' + hechos + ' / ' + casos.length + '</dd></div><div class="gd-kpi"><dt>Mejor puntaje medio</dt><dd>' + (hechos ? Math.round(casos.reduce(function (s, c) { return s + (g.casos[c.id] ? g.casos[c.id].mejor : 0); }, 0) / hechos) + " %" : "—") + '</dd></div></dl>' +
      '<ul class="gd-lista">' + casos.map(function (c) {
        var r = g.casos[c.id], libre = desbloqueado(c, g), req = c.requiere ? casos.filter(function (x) { return x.id === c.requiere.caso; })[0] : null;
        return '<li class="gd-caso' + (libre ? "" : " is-bloq") + '"><p class="gd-niv">' + esc(NIVEL[c.dificultad]) + ' · ' + esc(c.especialidad) + '</p><h2>' + esc(c.titulo) + '</h2><p>' + esc(c.resumen) + '</p>' +
          (r ? '<p class="gd-mejor">Mejor puntaje: <b>' + r.mejor + ' %</b> · Intentos: ' + r.intentos + '</p>' : "") +
          (libre ? '<a class="btn btn--primary btn--sm" href="#/guardia/' + esc(c.id) + '">' + (r ? "Reintentar el caso" : "Empezar el caso") + '</a>'
            : '<p class="gd-lock">Se desbloquea al sacar ' + c.requiere.minimo + ' % o más en «' + esc(req ? req.titulo : "") + '».</p>') + '</li>';
      }).join("") + '</ul>';
    cont.innerHTML = h;
  }

  function jugar(cont, caso) {
    var g0 = cargar();
    if (!desbloqueado(caso, g0)) { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">Este caso aún está bloqueado</p><p class="empty-state__text">Completa antes el caso anterior con el puntaje indicado.</p><a class="btn btn--primary" href="#/guardia">Volver a los casos</a></div>'; return; }
    var nodo = caso.nodos[caso.inicio], puntos = 0, camino = [], tInicio = 0, usarTiempo = false, reloj = null, bloqueado = false;
    var maxTotal = maximo(caso, caso.inicio);

    function pararReloj() { if (reloj) { clearInterval(reloj); reloj = null; } }
    function paso() {
      pararReloj();
      if (nodo.final) { fin(); return; }
      bloqueado = false; tInicio = Date.now();
      var opciones = barajar(nodo.decisiones);
      var vit = Object.keys(nodo.vitales).map(function (k) { return '<div><dt>' + esc(k) + '</dt><dd>' + esc(nodo.vitales[k]) + '</dd></div>'; }).join("");
      cont.innerHTML = '<div class="gd-juego"><header class="gd-top"><a class="link-arrow" href="#/guardia">← Casos</a><h1>' + esc(caso.titulo) + '</h1>' +
        '<p class="gd-prog">Decisión ' + (camino.length + 1) + ' · Puntaje ' + puntos + ' / ' + maxTotal + '</p></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<section class="gd-paciente" aria-label="Estado del paciente"><div class="gd-grav gd-grav--' + nodo.gravedad + '" role="status"><span aria-hidden="true"></span>Estado: <b>' + GRAV[nodo.gravedad] + '</b></div>' +
        '<p class="gd-estado">' + esc(nodo.estado) + '</p><dl class="gd-vit">' + vit + '</dl></section>' +
        '<label class="gd-tiempo"><input type="checkbox" id="gdT"' + (usarTiempo ? " checked" : "") + '> Mostrar cronómetro de la decisión (solo informativo: no quita puntos)</label><p class="gd-crono" id="gdC" aria-live="off" hidden></p>' +
        '<h2 class="gd-q">¿Qué haces ahora?</h2><div class="gd-ops" role="group" aria-label="Decisiones">' + opciones.map(function (o) { return '<button type="button" class="gd-op" data-id="' + esc(o.id) + '">' + esc(o.texto) + '</button>'; }).join("") + '</div>' +
        '<div id="gdFb" role="status" aria-live="polite"></div></div>';
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
      var opt = nodo.decisiones.filter(function (x) { return x.calidad === "optima"; })[0];
      cont.querySelector("#gdFb").innerHTML = '<div class="gd-fb gd-fb--' + d.calidad + '"><p class="gd-fb__t">' + ETQ[d.calidad] + ' · ' + PUNTOS[d.calidad] + ' pts</p><p>' + esc(d.explicacion) + '</p>' +
        (d.calidad !== "optima" ? '<p class="gd-fb__opt"><b>Lo óptimo era:</b> ' + esc(opt.texto) + '</p>' : "") +
        '<button type="button" class="btn btn--primary" id="gdSig">' + (sig.final ? "Ver el desenlace" : "Continuar: ver la evolución") + '</button></div>';
      var bt = cont.querySelector("#gdSig"); bt.focus(); bt.addEventListener("click", function () { nodo = sig; paso(); });
    }
    function fin() {
      var pct = porcentaje(caso, puntos), f = nodo.final;
      var g = registrar(cargar(), caso, { pct: pct, tipo: f.tipo }); guardar(g);
      var temas = [], vistos = {};
      camino.forEach(function (p) { if (p.decision.calidad !== "optima" && p.decision.tema && !vistos[p.decision.tema]) { vistos[p.decision.tema] = 1; temas.push(p.decision.tema); } });
      var sig = (raiz.MQP_GUARDIA || []).filter(function (c) { return c.requiere && c.requiere.caso === caso.id && desbloqueado(c, g); });
      cont.innerHTML = '<div class="gd-juego"><header class="gd-top"><a class="link-arrow" href="#/guardia">← Casos</a><h1>' + esc(caso.titulo) + '</h1></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<section class="gd-final gd-final--' + f.tipo + '"><p class="gd-niv">Desenlace</p><h2>' + esc(f.titulo) + '</h2><p>' + esc(f.mensaje) + '</p><p class="gd-pts"><b>' + pct + ' %</b><span>' + puntos + ' de ' + maxTotal + ' puntos posibles</span></p></section>' +
        '<section class="card card--spaced"><h2 class="card__h">Tus decisiones</h2><ol class="gd-trail">' + camino.map(function (p) {
          return '<li class="gd-t gd-t--' + p.decision.calidad + '"><p class="gd-t__e">' + esc(p.nodo.estado.slice(0, 110)) + (p.nodo.estado.length > 110 ? "…" : "") + '</p><p><b>' + ETQ[p.decision.calidad] + ':</b> ' + esc(p.decision.texto) + '</p><p class="gd-t__x">' + esc(p.decision.explicacion) + '</p><p class="muted small">Tiempo: ' + p.segundos + ' s (informativo)</p></li>';
        }).join("") + '</ol></section>' +
        '<section class="card card--spaced"><h2 class="card__h">Qué reforzar</h2>' + (temas.length ? '<ul class="gd-temas">' + temas.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join("") + '</ul>' : '<p>Todas tus decisiones fueron las óptimas. ¡Buen trabajo!</p>') +
        '<p class="muted small">Busca estos temas en el banco de preguntas o conviértelos en flashcards desde la explicación de cada pregunta.</p></section>' +
        '<section class="card card--spaced"><h2 class="card__h">Fuentes del caso</h2><ul class="gd-fuentes">' + caso.fuentes.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join("") + '</ul>' +
        '<p class="muted small">Fuentes citadas por nombre. No se verificó el texto contra el documento original ni se indica página: confirma siempre con la guía vigente.</p></section>' +
        '<div class="gd-acc"><a class="btn btn--primary" href="#/guardia/' + esc(caso.id) + '" data-reintentar>Reintentar el caso</a><a class="btn btn--ghost" href="#/guardia">Volver a los casos</a>' +
        sig.map(function (c) { return '<a class="btn btn--ghost" href="#/guardia/' + esc(c.id) + '">Siguiente: ' + esc(c.titulo) + '</a>'; }).join("") + '</div></div>';
      var re = cont.querySelector("[data-reintentar]"); re.addEventListener("click", function (ev) { ev.preventDefault(); jugar(cont, caso); window.scrollTo(0, 0); });
      window.scrollTo(0, 0);
    }
    paso();
  }

  var dentro = false;     // true mientras el alumno navega dentro de #/guardia: evita repetir la introducción
  window.addEventListener("hashchange", function () { if (!/^#\/guardia/.test(location.hash)) dentro = false; });
  function montar(cont, arg) {
    var casos = raiz.MQP_GUARDIA || [];
    var caso = arg ? casos.filter(function (c) { return c.id === arg; })[0] : null;
    var primeraEntrada = !dentro; dentro = true;      // cualquier pantalla del módulo cuenta como «ya estoy dentro»
    if (arg && !caso) { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">No encontramos ese caso</p><a class="btn btn--primary" href="#/guardia">Ver los casos</a></div>'; return; }
    if (caso) { jugar(cont, caso); return; }
    lista(cont);
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
