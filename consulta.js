/* MedQuizPlus · «Consulta Clínica Experta»: pantallas de la consulta ambulatoria por etapas (motivo → anamnesis → antecedentes → examen → hipótesis →
   solicitud de pruebas → resultados → diagnóstico → tratamiento → seguimiento → informe). La lógica pura vive en consulta_nucleo.js; los resultados
   de cada prueba están predefinidos en el caso (no hay IA ni resultados aleatorios) y solo se muestran si el alumno los solicita.
   Reutiliza de M.guardia el diálogo, la tabla de laboratorio con intervalos y la ficha de referencias. Simulación educativa. */
(function (raiz) {
  "use strict";
  var M = raiz.MQP || (raiz.MQP = {});
  var C = function () { return M.consultaNucleo; }, GD = function () { return M.guardia; };
  var SRC = (document.currentScript && document.currentScript.src) || "", BASE = SRC.replace(/consulta\.js(\?.*)?$/, ""), VER = (SRC.split("?")[1] || "");
  var cargaDatos = null, CLAVE_SESION = "mqp_consulta_sesion_v1", LETRAS = ["A", "B", "C", "D", "E"];
  var ETQ = { optima: "Decisión óptima", aceptable: "Aceptable, mejorable", incorrecta: "Incorrecta", peligrosa: "Peligrosa" };
  function cargarScript(n) { return new Promise(function (ok, mal) { var s = document.createElement("script"); s.src = BASE + n + (VER ? "?" + VER : ""); s.onload = ok; s.onerror = function () { mal(new Error(n)); }; document.head.appendChild(s); }); }
  function asegurarDatos() {
    var ps = [GD().asegurarDatos()];
    if (!raiz.MQP_CONSULTA) { if (!cargaDatos) cargaDatos = cargarScript("consulta_casos.js").catch(function (e) { cargaDatos = null; throw e; }); ps.push(cargaDatos); }
    return Promise.all(ps).then(function () {});
  }
  var esc = function (s) { return GD().esc(s); };
  function cargar() { var g = M.progreso && M.progreso.preferencia("consulta"); return g && g.casos ? g : { casos: {} }; }
  function guardar(g) { if (M.progreso) M.progreso.preferencia("consulta", g); }
  function por(l, id) { for (var i = 0; i < l.length; i++) if (l[i].id === id) return l[i]; return null; }
  function sesionGuardar(e) { var ahora = Date.now(); if (e.t) e.segundos = (e.segundos || 0) + Math.min(300000, Math.max(0, ahora - e.t)) / 1000; e.t = ahora; GD().ls(CLAVE_SESION + ":" + e.caso, C().serializar(e)); }
  function sesionBorrar(id) { GD().ls(CLAVE_SESION + ":" + id, null); }
  function tiempo(s) { s = Math.round(s); return Math.floor(s / 60) + " min " + (s % 60) + " s"; }
  var detener = null;

  /* ---------- lista ---------- */
  function lista(cont) {
    var g = cargar(), casos = raiz.MQP_CONSULTA || [], NIVEL = M.guardiaNucleo.NIVEL;
    cont.innerHTML = '<nav class="gh-migas" aria-label="Ruta"><a href="#/guardia">Centro de simulación</a><span aria-hidden="true">›</span><span aria-current="page">Consulta clínica experta</span></nav>' +
      '<header class="gh-modal gh-modal--azul"><img class="gh-modal__img" src="../guardia/portadas/consulta.webp" alt="" width="800" height="600" loading="eager" decoding="async"><div class="gh-modal__txt"><p class="gh-kicker">Consulta ambulatoria</p><h1 class="gh-modal__t">Consulta Clínica Experta</h1><p>Consulta ambulatoria completa: haces la anamnesis, exploras, planteas hipótesis, eliges qué pruebas pedir, interpretas los resultados y decides el diagnóstico, el tratamiento y el seguimiento. Los resultados solo aparecen si los solicitas. Al final recibes un informe de tus pruebas pedidas y omitidas.</p></div></header>' +
      '<p class="gd-aviso" role="note">' + esc(GD().AVISO) + '</p>' +
      '<ul class="gd-lista" id="cqLista">' + casos.map(function (c) {
        var r = g.casos[c.id];
        return '<li class="gd-caso"><p class="gd-niv">' + esc(NIVEL[c.dificultad]) + ' · ' + esc(c.especialidad) + '</p><h2>' + esc(c.titulo) + '</h2><p>' + esc(c.resumen) + '</p><p class="muted small">≈ ' + c.duracion_min + ' min · ' + c.pruebas.length + ' pruebas disponibles · ' + c.referencias.length + ' referencias</p>' +
          (r ? '<p class="gd-mejor">Mejor puntaje: <b>' + r.mejor + ' %</b> · Intentos: ' + r.intentos + '</p>' : "") + '<a class="btn btn--primary btn--sm" href="#/consulta/' + esc(c.id) + '">' + (r ? "Reintentar la consulta" : "Empezar la consulta") + '</a></li>';
      }).join("") + '</ul>';
  }

  /* ---------- una consulta ---------- */
  function consulta(cont, caso) {
    var N = C(), GDm = GD(), crudo = GDm.ls(CLAVE_SESION + ":" + caso.id), ses = crudo ? N.restaurar(crudo, caso) : null;
    if (crudo && !ses) sesionBorrar(caso.id);
    if (detener) detener();
    var e = ses || { caso: caso.id, etapa: "motivo", anamnesis: [], antecedentes: [], examen: [], hipotesis: { sel: [], principal: null }, solicitadas: [], borrador: [], respuestas: {}, reevaluaciones: 0, segundos: 0, t: Date.now() };
    e.t = Date.now();
    var vista = e.etapa, aviso = "", ESTAPAS = N.ETAPAS.slice(0, -1);
    function persistir() { sesionGuardar(e); }
    function salir() { persistir(); window.removeEventListener("hashchange", alIrse); window.removeEventListener("pagehide", persistir); GDm.cerrarDialogo(); if (detener === salir) detener = null; }
    function alIrse() { if (!/^#\/consulta\//.test(location.hash) || location.hash.indexOf(caso.id) < 0) salir(); }
    detener = salir; window.addEventListener("hashchange", alIrse); window.addEventListener("pagehide", persistir);
    function idx(et) { return N.ETAPAS.indexOf(et); }
    function ir(et) { if (idx(et) > idx(e.etapa)) e.etapa = et; vista = et; aviso = ""; persistir(); pintar(); var h = cont.querySelector("#cqTitulo"); if (h) h.focus({ preventScroll: false }); }

    function cabecera() {
      var pasos = ESTAPAS.map(function (et) {
        var alcanzada = idx(et) <= idx(e.etapa), actual = et === vista;
        return '<li class="cq-paso' + (actual ? " is-actual" : "") + (alcanzada && !actual ? " is-hecho" : "") + '">' + (alcanzada ? '<button type="button" data-ir="' + et + '"' + (actual ? ' aria-current="step"' : "") + '>' + esc(N.NOMBRES[et]) + '</button>' : '<span>' + esc(N.NOMBRES[et]) + '</span>') + '</li>';
      }).join("");
      return '<header class="gd-top"><a class="link-arrow" href="#/consulta">← Consulta clínica experta</a><h1>' + esc(caso.titulo) + '</h1></header><p class="gd-aviso" role="note">' + esc(GDm.AVISO) + '</p>' +
        '<nav aria-label="Etapas de la consulta"><ol class="cq-pasos">' + pasos + '</ol></nav>' +
        '<section class="gd-paciente cq-pac" aria-label="Paciente"><p class="gd-estado"><b>' + esc(GDm.perfilTxt(caso.paciente)) + '.</b> ' + esc(caso.motivo) + '</p></section>';
    }
    function pintar() {
      var cuerpo = ({ motivo: sMotivo, anamnesis: sAnamnesis, antecedentes: sAntecedentes, examen: sExamen, hipotesis: sHipotesis, pruebas: sPruebas, resultados: sResultados, diagnostico: function () { return sMCQ("diagnostico", "Diagnóstico más probable"); }, tratamiento: function () { return sMCQ("tratamiento", "Tratamiento"); }, seguimiento: function () { return sMCQ("seguimiento", "Seguimiento, alarma y derivación"); } })[vista]();
      cont.innerHTML = '<div class="gd-juego">' + cabecera() + '<div class="cq-cuerpo">' + cuerpo + '</div></div>';
      ligar();
    }
    function titulo(t, sub) { return '<h2 class="gd-q" id="cqTitulo" tabindex="-1">' + esc(t) + '</h2>' + (sub ? '<p class="muted small">' + sub + '</p>' : ""); }
    function sigBtn(texto, et, extra) { return '<p class="cq-acc"><button type="button" class="btn btn--primary" data-sig="' + et + '"' + (extra || "") + '>' + esc(texto) + '</button></p>'; }

    /* motivo */
    function sMotivo() {
      return titulo("Motivo de consulta") + '<p class="muted small">' + esc(caso.contexto) + '</p><p>' + esc(caso.resumen) + '</p>' +
        '<p class="muted small">Recorrerás las etapas de una consulta real. Puedes volver a las etapas anteriores para revisar lo que ya averiguaste, y la sesión se guarda si sales.</p>' + sigBtn("Comenzar la anamnesis", "anamnesis");
    }
    /* preguntas reveladas (anamnesis, antecedentes y examen) */
    function bloquePreguntas(grupos, hechos, clave) {
      return grupos.map(function (g) {
        return '<fieldset class="cq-grupo"><legend>' + esc(g.titulo) + '</legend><ul class="cq-q">' + g.items.map(function (q) {
          var h = hechos.indexOf(q.id) >= 0;
          return '<li>' + '<button type="button" class="btn btn--ghost btn--sm cq-preg" data-pregunta="' + clave + ':' + esc(q.id) + '"' + (h ? ' aria-disabled="true"' : "") + '>' + esc(q.texto) + (h ? ' <span class="gd-prov">hecho</span>' : "") + '</button>' +
            (h ? '<p class="cq-resp"><b>Respuesta:</b> ' + esc(q.respuesta) + '</p>' : "") + '</li>';
        }).join("") + '</ul></fieldset>';
      }).join("");
    }
    function sAnamnesis() {
      return titulo("Anamnesis", "Elige las preguntas que harías. Las respuestas aparecen debajo de cada una; no se penaliza preguntar de más, solo omitir lo importante.") +
        '<div aria-live="polite">' + bloquePreguntas(caso.anamnesis.map(function (c) { return { titulo: c.categoria, items: c.preguntas.map(function (q) { return { id: q.id, texto: q.texto, respuesta: q.respuesta }; }) }; }), e.anamnesis, "anamnesis") + '</div>' +
        '<p class="muted small">Preguntas hechas: ' + e.anamnesis.length + ' de ' + N.aplanar(caso).length + '.</p>' + sigBtn("Continuar a los antecedentes", "antecedentes");
    }
    function sAntecedentes() {
      return titulo("Antecedentes", "Elige qué antecedentes revisar.") + '<div aria-live="polite"><ul class="cq-q">' + caso.antecedentes.map(function (a) {
        var h = e.antecedentes.indexOf(a.id) >= 0;
        return '<li><button type="button" class="btn btn--ghost btn--sm cq-preg" data-pregunta="antecedentes:' + esc(a.id) + '"' + (h ? ' aria-disabled="true"' : "") + '>' + esc(a.nombre) + (h ? ' <span class="gd-prov">revisado</span>' : "") + '</button>' + (h ? '<p class="cq-resp">' + esc(a.texto) + '</p>' : "") + '</li>';
      }).join("") + '</ul></div>' + sigBtn("Continuar al examen físico", "examen");
    }
    function sExamen() {
      var reg = {}; caso.examen.forEach(function (x) { (reg[x.region] = reg[x.region] || []).push(x); });
      return titulo("Examen físico", "Elige las maniobras que realizarías. El hallazgo aparece al realizarla.") + '<div aria-live="polite">' + Object.keys(reg).map(function (r) {
        return '<fieldset class="cq-grupo"><legend>' + esc(r) + '</legend><ul class="cq-q">' + reg[r].map(function (x) {
          var h = e.examen.indexOf(x.id) >= 0;
          return '<li><button type="button" class="btn btn--ghost btn--sm cq-preg" data-pregunta="examen:' + esc(x.id) + '"' + (h ? ' aria-disabled="true"' : "") + '>' + esc(x.maniobra) + (h ? ' <span class="gd-prov">realizada</span>' : "") + '</button>' + (h ? '<p class="cq-resp"><b>Hallazgo:</b> ' + esc(x.hallazgo) + '</p>' : "") + '</li>';
        }).join("") + '</ul></fieldset>';
      }).join("") + '</div>' + sigBtn("Continuar a las hipótesis", "hipotesis");
    }
    /* hipótesis */
    function sHipotesis() {
      var h = e.hipotesis, ops = caso.hipotesis.opciones, max = caso.hipotesis.max;
      return titulo("Hipótesis diagnósticas", "Elige hasta " + max + " diagnósticos que consideras (el correcto puede ser uno de ellos, o ninguno) y marca cuál es el principal. No se te dice aquí si acertaste: se evalúa en el informe.") +
        '<fieldset class="cq-grupo"><legend>Diagnósticos que consideras</legend><ul class="cq-q">' + ops.map(function (o) {
          var sel = h.sel.indexOf(o.id) >= 0;
          return '<li class="cq-hip"><label><input type="checkbox" data-hip="' + esc(o.id) + '"' + (sel ? " checked" : "") + (!sel && h.sel.length >= max ? " disabled" : "") + '> ' + esc(o.dx) + '</label>' +
            '<label class="cq-prin"><input type="radio" name="cqPrin" value="' + esc(o.id) + '"' + (h.principal === o.id ? " checked" : "") + (sel ? "" : " disabled") + '> principal</label></li>';
        }).join("") + '</ul></fieldset><p class="muted small" id="cqHipN" aria-live="polite">' + h.sel.length + ' de ' + max + ' seleccionadas.</p>' +
        (aviso ? '<p class="gd-alerta" role="alert">' + esc(aviso) + '</p>' : "") + sigBtn("Continuar a la solicitud de pruebas", "pruebas", ' data-valida="hipotesis"');
    }
    /* pruebas */
    function sPruebas() {
      var cats = {}; caso.pruebas.forEach(function (p) { (cats[p.categoria] = cats[p.categoria] || []).push(p); });
      var sinEnviar = e.borrador.length;
      return titulo("Solicitud de pruebas", "Marca las pruebas que solicitarías, agrupadas por categoría. Antes de enviar las revisarás. Los resultados solo se muestran de lo que solicites; no se adelanta nada. Pedir pruebas innecesarias o perjudiciales resta en el informe.") +
        (aviso ? '<div class="gd-alerta" role="alert"><p>' + aviso + '</p></div>' : "") +
        Object.keys(cats).map(function (c) {
          return '<fieldset class="cq-grupo"><legend>' + esc(c) + '</legend><ul class="cq-q">' + cats[c].map(function (p) {
            var enviada = e.solicitadas.indexOf(p.id) >= 0, sel = enviada || e.borrador.indexOf(p.id) >= 0;
            return '<li><label class="cq-prueba"><input type="checkbox" data-prueba="' + esc(p.id) + '"' + (sel ? " checked" : "") + (enviada ? " disabled" : "") + '> ' + esc(p.nombre) + (enviada ? ' <span class="gd-prov">ya solicitada</span>' : "") + '</label></li>';
          }).join("") + '</ul></fieldset>';
        }).join("") + '<p class="cq-acc"><button type="button" class="btn btn--primary" id="cqRevisar">Revisar y enviar la solicitud (<span id="cqNb">' + sinEnviar + '</span>)</button></p>' +
        (e.solicitadas.length ? '<p class="small"><button type="button" class="link-arrow" data-ir="resultados">Ver los resultados que ya tienes</button></p>' : "");
    }
    function revisarEnvio(disparador) {
      var sel = e.borrador.map(function (i) { return por(caso.pruebas, i); }).filter(Boolean), cats = {};
      sel.forEach(function (p) { (cats[p.categoria] = cats[p.categoria] || []).push(p); });
      var html = (sel.length ? Object.keys(cats).map(function (c) { return '<h3 class="gd-h3">' + esc(c) + '</h3><ul>' + cats[c].map(function (p) { return '<li>' + esc(p.nombre) + '</li>'; }).join("") + '</ul>'; }).join("") : '<p>No marcaste ninguna prueba nueva.</p>') +
        '<p class="muted small">Revisa la lista: una vez enviada verás los resultados. Puedes seguir editando.</p><p class="cq-acc"><button type="button" class="btn btn--primary" id="cqEnviar">Enviar la solicitud</button> <button type="button" class="btn btn--ghost" data-cerrar>Seguir editando</button></p>';
      var d = GDm.dialogo("Revisión de la solicitud de pruebas", html, "", disparador);
      d.querySelector("#cqEnviar").addEventListener("click", function () {
        var union = e.solicitadas.concat(e.borrador), bl = N.bloqueos(caso, union);
        GDm.cerrarDialogo();
        if (bl.length && e.reevaluaciones === 0) {
          e.reevaluaciones = 1; aviso = bl.map(function (b) { return esc(b.mensaje_bloqueo); }).filter(function (x, i, a) { return a.indexOf(x) === i; }).join("</p><p>") + "</p><p>Reconsidera tu solicitud. Si aun así quieres continuar, vuelve a enviarla.";
          persistir(); pintar(); var t = cont.querySelector("#cqTitulo"); if (t) t.focus(); return;
        }
        e.solicitadas = union; e.borrador = []; ir("resultados");
      });
    }
    /* resultados */
    /* un bloque por prueba solicitada (examen de orina, urocultivo, hemograma… no se mezclan en una sola tabla) */
    function gruposLab(ocultar) {
      return N.resultadosSolicitados(caso, e.solicitadas).filter(function (p) { return p.resultado.tipo === "lab"; }).map(function (p) { return { nodoId: "res", titulo: p.resultado.titulo || p.nombre, ocultar: ocultar, items: p.resultado.lab }; });
    }
    function sResultados() {
      var pr = N.resultadosSolicitados(caso, e.solicitadas), txt = pr.filter(function (p) { return p.resultado.tipo === "texto"; }), q = caso.preguntas.interpretacion, resp = e.respuestas.interpretacion;
      return titulo("Resultados e interpretación", "Solo ves lo que solicitaste.") +
        (pr.length ? "" : '<p class="gd-alerta">No solicitaste ninguna prueba. Puedes decidir solo con la clínica, pero revisa en el informe qué habría cambiado.</p>') +
        (gruposLab(!resp).length ? GDm.tablaResultados(gruposLab(!resp), caso.paciente, resp ? null : "res") : "") +
        txt.map(function (p) { return '<section class="gd-labn"><h3 class="gd-h3">' + esc(GDm.mayus1(p.nombre)) + '</h3><p>' + esc(GDm.mayus1(p.resultado.texto)) + '</p></section>'; }).join("") +
        '<p class="cq-acc"><button type="button" class="btn btn--ghost" data-ir="pruebas">Solicitar más pruebas</button> <button type="button" class="btn btn--ghost btn--sm" id="cqLabBtn">🧪 Laboratorio y valores de referencia</button></p>' +
        mcqHtml("interpretacion", q, resp) + (resp ? sigBtn("Continuar al diagnóstico", "diagnostico") : "");
    }
    /* preguntas de cinco alternativas */
    function mcqHtml(clave, q, resp) {
      var h = '<div class="cq-mcq" data-mcq="' + clave + '"><h3 class="gd-q" id="cqQ' + clave + '">' + esc(q.enunciado) + '</h3>' + (resp ? "" : '<p class="muted small">Elige una de las cinco alternativas (también puedes pulsar A, B, C, D o E). No se corrige durante la consulta: verás el análisis al final.</p>') +
        '<div class="gd-ops" role="group" aria-labelledby="cqQ' + clave + '">' + q.decisiones.map(function (o) {
          return '<button type="button" class="gd-op' + (resp && o.id === resp ? " is-sel" : "") + '" data-op="' + esc(o.id) + '"' + (resp ? ' aria-disabled="true"' : "") + '><span class="gd-op__l" aria-hidden="true">' + esc(o.id) + '</span><span class="gd-op__t"><span class="sr-only">Alternativa ' + esc(o.id) + ': </span>' + esc(o.texto) + '</span></button>';
        }).join("") + '</div>';
      if (resp) h += '<div class="gd-fb gd-fb--neutra" role="status"><p class="gd-fb__t">Respuesta registrada (' + esc(resp) + ')</p><p>La corrección y el análisis de las cinco alternativas aparecen en el informe final, cuando termines la consulta.</p></div>';
      return h + '</div>';
    }
    function cinco(q, resp) {
      return '<ol class="gd-cinco" type="A">' + q.decisiones.map(function (a) {
        return '<li class="gd-cinco__i gd-cinco__i--' + a.calidad + '"><p><b>' + esc(a.id) + '.</b> ' + esc(a.texto) + (a.id === resp ? ' <span class="gd-prov">tu elección</span>' : "") + (a.calidad === "optima" ? ' <span class="gd-prov gd-prov--ok">correcta</span>' : "") + '</p><p class="small"><b>' + ETQ[a.calidad] + ':</b> ' + esc(a.explicacion) + '</p></li>';
      }).join("") + '</ol>';
    }
    var SIG = { interpretacion: "diagnostico", diagnostico: "tratamiento", tratamiento: "seguimiento", seguimiento: "informe" };
    var TXT_SIG = { diagnostico: "Continuar al tratamiento", tratamiento: "Continuar al seguimiento", seguimiento: "Ver el informe de la consulta" };
    function sMCQ(clave, nombre) {
      var q = caso.preguntas[clave], resp = e.respuestas[clave];
      var previo = clave === "diagnostico" ? '<p class="muted small">Con todo lo que reuniste, decide.</p>' : "";
      return titulo(nombre) + previo + mcqHtml(clave, q, resp) + (resp ? sigBtn(TXT_SIG[clave], SIG[clave]) : "");
    }
    function elegir(clave, letra) {
      if (e.respuestas[clave]) return;                   // sin envíos duplicados ni cambios de respuesta
      e.respuestas[clave] = letra; persistir(); pintar();
      var fb = cont.querySelector('[data-mcq="' + clave + '"] .gd-fb'); if (fb) fb.scrollIntoView({ block: "nearest" });
    }

    /* eventos */
    function ligar() {
      GDm.ligarImagenes(cont);
      [].forEach.call(cont.querySelectorAll("[data-sig]"), function (b) { b.addEventListener("click", function () {
        var s = b.getAttribute("data-sig");
        if (b.getAttribute("data-valida") === "hipotesis" && (!e.hipotesis.sel.length || !e.hipotesis.principal)) { aviso = "Elige al menos una hipótesis y marca cuál es la principal."; pintar(); return; }
        if (s === "informe") { informe(); return; } ir(s);
      }); });
      [].forEach.call(cont.querySelectorAll("[data-ir]"), function (b) { b.addEventListener("click", function () { vista = b.getAttribute("data-ir"); aviso = ""; persistir(); pintar(); var t = cont.querySelector("#cqTitulo"); if (t) t.focus(); }); });
      [].forEach.call(cont.querySelectorAll("[data-pregunta]"), function (b) { b.addEventListener("click", function () {
        var p = b.getAttribute("data-pregunta").split(":"), lista = e[p[0]]; if (lista.indexOf(p[1]) >= 0) return; lista.push(p[1]); persistir();
        var y = window.scrollY; pintar(); window.scrollTo(0, y); var nb = cont.querySelector('[data-pregunta="' + p[0] + ":" + p[1] + '"]'); if (nb) nb.focus({ preventScroll: true });
      }); });
      [].forEach.call(cont.querySelectorAll("[data-hip]"), function (c) { c.addEventListener("change", function () {
        var id = c.getAttribute("data-hip"), h = e.hipotesis, i = h.sel.indexOf(id);
        if (c.checked && i < 0) h.sel.push(id); if (!c.checked && i >= 0) { h.sel.splice(i, 1); if (h.principal === id) h.principal = null; }
        if (h.sel.length === 1 && !h.principal) h.principal = h.sel[0];
        persistir(); pintar(); var nc = cont.querySelector('[data-hip="' + id + '"]'); if (nc) nc.focus();
      }); });
      [].forEach.call(cont.querySelectorAll("input[name=cqPrin]"), function (r) { r.addEventListener("change", function () { e.hipotesis.principal = r.value; persistir(); }); });
      [].forEach.call(cont.querySelectorAll("[data-prueba]"), function (c) { c.addEventListener("change", function () {
        var id = c.getAttribute("data-prueba"), i = e.borrador.indexOf(id); if (c.checked && i < 0) e.borrador.push(id); if (!c.checked && i >= 0) e.borrador.splice(i, 1);
        var nb = cont.querySelector("#cqNb"); if (nb) nb.textContent = e.borrador.length; persistir();
      }); });
      var rv = cont.querySelector("#cqRevisar"); if (rv) rv.addEventListener("click", function () { revisarEnvio(rv); });
      var lb = cont.querySelector("#cqLabBtn"); if (lb) lb.addEventListener("click", function () { GDm.abrirLaboratorio(caso, gruposLab(!e.respuestas.interpretacion), e.respuestas.interpretacion ? null : "res", lb); });
      [].forEach.call(cont.querySelectorAll("[data-op]"), function (b) { b.addEventListener("click", function () { if (b.getAttribute("aria-disabled") === "true") return; elegir(b.closest("[data-mcq]").getAttribute("data-mcq"), b.getAttribute("data-op")); }); });
    }
    function teclas(ev) {
      if (document.querySelector("dialog[open]")) return; var t = ev.target && ev.target.tagName; if (t === "INPUT" || t === "TEXTAREA" || t === "SELECT" || ev.ctrlKey || ev.metaKey || ev.altKey) return;
      var k = (ev.key || "").toUpperCase(); if (LETRAS.indexOf(k) < 0) return; var m = cont.querySelector(".cq-mcq"); if (!m) return;
      var b = m.querySelector('[data-op="' + k + '"]'); if (b && b.getAttribute("aria-disabled") !== "true") { ev.preventDefault(); b.click(); }
    }
    document.addEventListener("keydown", teclas);
    var salirBase = salir; salir = function () { document.removeEventListener("keydown", teclas); salirBase(); }; detener = salir;

    /* ---- informe final ---- */
    function informe() {
      persistir(); document.removeEventListener("keydown", teclas); window.removeEventListener("hashchange", alIrse); window.removeEventListener("pagehide", persistir); if (detener === salir) detener = null;
      var ev = N.evaluar(caso, e), inf = caso.informe, pr = ev.pruebas, L = pr.listas, hip = ev.hipotesis;
      var g = N.registrar(cargar(), caso, ev.total, Date.now()); guardar(g); var seg = e.segundos || 0; sesionBorrar(caso.id);
      var lista = function (arr, vacio) { return arr.length ? '<ul class="gd-alt">' + arr.join("") + '</ul>' : '<p class="small muted">' + vacio + '</p>'; };
      var li = function (p, extra) { return '<li><b>' + esc(p.nombre) + '</b> <span class="muted small">(' + esc(p.categoria) + ')</span>: ' + esc(p.justificacion) + (extra || "") + '</li>'; };
      var res = N.resultadosSolicitados(caso, e.solicitadas), labs = res.filter(function (p) { return p.resultado.tipo === "lab"; }), items = []; labs.forEach(function (p) { p.resultado.lab.forEach(function (r) { items.push(r); }); });
      var usadas = {}; Object.keys(caso.preguntas).forEach(function (k) { caso.preguntas[k].decisiones.forEach(function (d) { (d.refs || []).forEach(function (r) { usadas[r] = 1; }); }); });
      var perdidas = ev.anamnesis.omitidos.concat(ev.examen.omitidos);
      var h = '<div class="gd-juego gd-informe"><header class="gd-top"><a class="link-arrow" href="#/consulta">← Consulta clínica experta</a><h1>' + esc(caso.titulo) + '</h1></header><p class="gd-aviso" role="note">' + esc(GDm.AVISO) + '</p>' +
        '<section class="gd-final gd-final--' + (ev.criticos.length ? "adverso" : ev.total >= 75 ? "bueno" : "regular") + '"><p class="gd-niv">Informe de la consulta</p><h2>' + esc(inf.diagnostico_final) + '</h2><p class="gd-pts"><b>' + ev.total + ' %</b><span>puntaje ponderado por importancia clínica · ' + tiempo(seg) + ' · sin límite de tiempo (la velocidad no puntúa)</span></p></section>' +
        '<nav class="gd-indice" aria-label="Secciones del informe"><a href="#cqA">Resumen</a> <a href="#cqB">Hipótesis</a> <a href="#cqC">Pruebas</a> <a href="#cqD">Resultados</a> <a href="#cqE">Decisiones</a> <a href="#cqF">Tratamiento</a> <a href="#cqG">Puntaje y referencias</a></nav>';
      h += '<section class="card card--spaced" id="cqA"><h2 class="card__h">Resumen clínico y diagnóstico</h2><p>' + esc(inf.resumen_clinico) + '</p><p><b>Diagnóstico final:</b> ' + esc(inf.diagnostico_final) + '</p><p><b>Diagnósticos diferenciales:</b></p><ul class="gd-alt">' + inf.diagnosticos_diferenciales.map(function (x) { return '<li><b>' + esc(x.dx) + ':</b> ' + esc(x.por_que_no) + '</li>'; }).join("") + '</ul>' +
        '<p><b>Datos que debían orientar el razonamiento:</b></p><ul class="gd-alt">' + inf.datos_clave.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul>' +
        '<p><b>Razonamiento paso a paso:</b></p><ol class="gd-razon">' + inf.razonamiento.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ol>' +
        '<h3 class="gd-h3">Datos importantes de la historia y el examen</h3>' + (perdidas.length ? '<p class="small">Datos importantes que no averiguaste:</p><ul class="gd-alt">' + perdidas.map(function (x) { return '<li>' + esc(x.maniobra || x.nombre || x.texto) + ': ' + esc(x.respuesta || x.hallazgo || (x.nombre ? x.texto : "")) + '</li>'; }).join("") + '</ul>' : '<p class="small">Averiguaste todos los datos clave de la historia, los antecedentes y el examen.</p>') + '</section>';
      h += '<section class="card card--spaced" id="cqB"><h2 class="card__h">Tus hipótesis</h2><p>' + (hip.comoPrincipal ? 'Tu hipótesis principal coincidió con el diagnóstico final.' : hip.incluida ? 'Incluiste el diagnóstico final entre tus hipótesis, pero no como principal.' : 'El diagnóstico final no estaba entre tus hipótesis.') + ' Cubriste ' + hip.diferencialesCubiertos + ' de ' + hip.diferenciales.length + ' diferenciales relevantes.</p><ul class="gd-alt">' +
        caso.hipotesis.opciones.map(function (o) { var s = e.hipotesis.sel.indexOf(o.id) >= 0; return '<li>' + (s ? '<span class="gd-prov">' + (e.hipotesis.principal === o.id ? "tu principal" : "tu hipótesis") + '</span> ' : "") + '<b>' + esc(o.dx) + ':</b> ' + esc(o.nota) + '</li>'; }).join("") + '</ul></section>';
      h += '<section class="card card--spaced" id="cqC"><h2 class="card__h">Informe de pruebas solicitadas</h2><p class="muted small">Cinco listas con la justificación. No existe una única lista aceptable: las pruebas «razonables» no se penalizan.</p>' +
        '<h3 class="gd-h3">Pruebas pertinentes que solicitaste</h3>' + lista(L.pertinentes.map(function (p) { return li(p, p.clasificacion === "prioritaria" ? ' <span class="gd-prov gd-prov--ok">prioritaria</span>' : ""); }), "No solicitaste ninguna prueba pertinente.") +
        '<h3 class="gd-h3">Pruebas innecesarias o de bajo valor que solicitaste</h3>' + lista(L.bajoValor.map(function (p) { return li(p); }), "No solicitaste pruebas innecesarias.") +
        '<h3 class="gd-h3">Pruebas importantes que omitiste</h3>' + lista(L.omitidasImportantes.map(function (p) { return li(p, p.tiempo_critico ? ' <span class="gd-prov">tiempo-crítica</span>' : ""); }), "No omitiste ninguna prueba prioritaria.") +
        '<h3 class="gd-h3">Pruebas potencialmente perjudiciales que solicitaste</h3>' + lista(L.perjudiciales.map(function (p) { return li(p); }), "No solicitaste pruebas perjudiciales.") +
        '<h3 class="gd-h3">Pruebas no solicitadas que habrían cambiado la conducta</h3>' + lista(L.cambiariaConducta.map(function (p) { return '<li><b>' + esc(p.nombre) + ':</b> ' + esc(p.cambia_conducta) + '</li>'; }), "Ninguna de las pruebas que omitiste habría cambiado la conducta.") +
        (e.reevaluaciones ? '<p class="small muted">Se te pidió reconsiderar la solicitud porque faltaba una prueba esencial antes de decidir con seguridad.</p>' : "") + '</section>';
      h += '<section class="card card--spaced" id="cqD"><h2 class="card__h">Resultados de laboratorio e interpretación</h2>' + (inf.interpretacion_laboratorio ? '<ul class="gd-alt">' + inf.interpretacion_laboratorio.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul>' : "") +
        (items.length ? GDm.tablaResultados(gruposLab(false), caso.paciente, null) : '<p class="muted small">No solicitaste pruebas de laboratorio.</p>') +
        res.filter(function (p) { return p.resultado.tipo === "texto"; }).map(function (p) { return '<p><b>' + esc(GDm.mayus1(p.nombre)) + ':</b> ' + esc(GDm.mayus1(p.resultado.texto)) + '</p>'; }).join("") + '<p class="muted small">Los intervalos son educativos (no de un laboratorio peruano); prevalece el del laboratorio que procesa la muestra.</p></section>';
      h += '<section class="card card--spaced" id="cqE"><h2 class="card__h">Análisis de tus decisiones</h2>' + ["interpretacion", "diagnostico", "tratamiento", "seguimiento"].map(function (k) {
        var q = caso.preguntas[k], d = por(q.decisiones, e.respuestas[k]), opt = q.decisiones.filter(function (x) { return x.calidad === "optima"; })[0];
        return '<details class="gd-dec gd-dec--' + (d ? d.calidad : "incorrecta") + '"' + (!d || d.calidad !== "optima" ? " open" : "") + '><summary>' + esc(N.NOMBRE_COMP[k]) + ' · peso ' + N.PESOS[k] + '</summary><p><b>' + esc(q.enunciado) + '</b></p><p><b>Tu respuesta' + (d ? " (" + esc(d.id) + ")" : "") + ':</b> ' + (d ? esc(d.texto) : "sin responder") + '</p>' +
          (d && d.calidad === "optima" ? '<p class="small">Fue la mejor alternativa.</p>' : '<p><b>Conducta preferible (' + esc(opt.id) + '):</b> ' + esc(opt.texto) + '</p>') + '<p class="small"><b>Análisis de las cinco alternativas:</b></p>' + cinco(q, e.respuestas[k]) + '</details>';
      }).join("") + '</section>';
      h += '<section class="card card--spaced" id="cqF"><h2 class="card__h">Tratamiento y seguimiento recomendados</h2><div class="gd-tabla">' + inf.tratamiento.map(function (t) { return '<div class="gd-tr"><p class="gd-tr__i"><b>' + esc(t.item) + '</b></p><p>' + esc(t.detalle) + '</p><p class="muted small"><b>Dosis / unidades:</b> ' + esc(t.dosis) + '</p></div>'; }).join("") + '</div><p class="muted small">No se fija una dosis universal cuando depende del peso, la edad o el protocolo local; consulta la guía y el protocolo vigentes.</p></section>';
      var temas = ev.componentes.filter(function (c) { return c.pct < 70; }).map(function (c) { return c.nombre; });
      h += '<section class="card card--spaced" id="cqG"><h2 class="card__h">Puntaje, refuerzo y referencias</h2><p><b>Puntaje ponderado:</b> ' + ev.total + ' % · <b>Errores críticos:</b> ' + ev.criticos.length + ' · <b>Errores recuperables:</b> ' + ev.mayores.length + ' · <b>Tiempo:</b> ' + tiempo(seg) + ' (indicador secundario, sin límite).</p>' +
        '<h3 class="gd-h3">Componentes del puntaje</h3><ul class="gd-comp">' + ev.componentes.map(function (c) { return '<li><span>' + esc(c.nombre) + ' (peso ' + c.peso + ')</span><span class="gd-barra" aria-hidden="true"><i style="width:' + c.pct + '%"></i></span><b>' + c.pct + ' %</b></li>'; }).join("") + '</ul>' +
        '<h3 class="gd-h3">Qué reforzar</h3>' + (temas.length ? '<ul class="gd-temas">' + temas.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join("") + '</ul>' : '<p class="small">Todos los componentes superaron el 70 %. ¡Buen trabajo!</p>') +
        '<p class="muted small">Temas relacionados para el banco: ' + inf.temas_relacionados.map(esc).join(" · ") + '.</p><p class="gd-clave"><b>Idea clave:</b> ' + esc(inf.mensaje_clave) + '</p>' +
        '<h3 class="gd-h3">Referencias del caso</h3><ul class="gd-refs">' + caso.referencias.map(function (r, i) { return GDm.refHtml(r, i + 1, usadas[r.id]); }).join("") + '</ul>' +
        '<h3 class="gd-h3">Diferencias entre fuentes y limitaciones</h3><ul>' + caso.discrepancias.map(function (x) { return '<li class="small">' + esc(x) + '</li>'; }).join("") + '</ul><p class="muted small">Caso redactado a partir de las fuentes citadas; no fue revisado por un especialista externo. Si ves una discrepancia con tu guía vigente, prevalece la guía.</p></section>' +
        '<div class="gd-acc"><a class="btn btn--primary" href="#/consulta/' + esc(caso.id) + '" data-reintentar>Reintentar la consulta</a><a class="btn btn--ghost" href="#/consulta">Volver a los casos</a></div></div>';
      cont.innerHTML = h; var re = cont.querySelector("[data-reintentar]"); re.addEventListener("click", function (x) { x.preventDefault(); consulta(cont, caso); window.scrollTo(0, 0); });
      window.scrollTo(0, 0);
    }
    pintar();
  }

  function montar(cont, arg) {
    if (!(raiz.MQP_CONSULTA && raiz.MQP_GUARDIA_LAB && M.guardia)) {
      cont.innerHTML = '<p class="muted" role="status">Cargando los casos…</p>';
      asegurarDatos().then(function () { if (/^#\/consulta/.test(location.hash)) montar(cont, arg); }, function () { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">No se pudieron cargar los casos</p><p class="empty-state__text">Revisa tu conexión e inténtalo de nuevo.</p><a class="btn btn--primary" href="#/consulta">Reintentar</a></div>'; });
      return;
    }
    if (detener) detener();
    var caso = arg ? raiz.MQP_CONSULTA.filter(function (c) { return c.id === arg; })[0] : null;
    if (arg && !caso) { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">No encontramos ese caso</p><a class="btn btn--primary" href="#/consulta">Ver los casos</a></div>'; return; }
    if (caso) consulta(cont, caso); else lista(cont);
  }
  M.consulta = { montar: montar, asegurarDatos: asegurarDatos };
})(typeof window !== "undefined" ? window : this);
