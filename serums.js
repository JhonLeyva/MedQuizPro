/* MedQuizPlus · «Misión SERUMS: sobrevive a la posta». Interfaz de la estación (#/serums y #/serums/<caso>).
   La lógica vive en serums_nucleo.js (puro, sin DOM); los casos y el registro de evidencia están en serums_casos.js (generado) y el índice documental
   en serums/indice.json (se carga solo cuando el alumno consulta al supervisor). Simulación educativa con establecimiento y casos ficticios. */
(function (raiz) {
  "use strict";
  var M = raiz.MQP || (raiz.MQP = {});
  var N = function () { return M.serumsNucleo; }, GD = function () { return M.guardia; };
  var SRC = (document.currentScript && document.currentScript.src) || "", BASE = SRC.replace(/serums\.js(\?.*)?$/, ""), VER = (SRC.split("?")[1] || "");
  var K_POSTA = "mqp_serums_posta_v1", K_SES = "mqp_serums_sesion_v1", IMG = BASE + "guardia/portadas/serums.webp";
  var AVISO = "Simulación educativa. El establecimiento, los pacientes y los casos son ficticios. Las decisiones no sustituyen la norma vigente ni el criterio clínico supervisado. La fotografía de portada es una ilustración generada con IA.";
  var CALIDAD = { optima: "Decisión óptima", aceptable: "Aceptable, mejorable", incorrecta: "Incorrecta", peligrosa: "Peligrosa (error crítico)" };
  var TABS = [["paciente", "Paciente"], ["historia", "Historia"], ["examen", "Examen físico"], ["pruebas", "Pruebas"], ["inventario", "Inventario"], ["referencia", "Referencia"], ["normativa", "Normativa"], ["evolucion", "Evolución"]];
  var cargaDatos = null, cargaIndice = null, detener = null;

  function esc(s) { return GD().esc(s); }
  function cargarScript(n) { return new Promise(function (ok, mal) { var s = document.createElement("script"); s.src = BASE + n + (VER ? "?" + VER : ""); s.onload = ok; s.onerror = function () { mal(new Error(n)); }; document.head.appendChild(s); }); }
  function asegurarDatos() {
    if (raiz.MQP_SERUMS) return Promise.resolve();
    if (!cargaDatos) cargaDatos = cargarScript("serums_casos.js").catch(function (e) { cargaDatos = null; throw e; });
    return cargaDatos;
  }
  function cargarIndice() {
    if (!cargaIndice) cargaIndice = fetch(BASE + "serums/indice.json" + (VER ? "?" + VER : "")).then(function (r) { if (!r.ok) throw new Error("indice"); return r.json(); }).catch(function (e) { cargaIndice = null; throw e; });
    return cargaIndice;
  }
  function por(l, id) { for (var i = 0; i < l.length; i++) if (l[i].id === id) return l[i]; return null; }
  function reloj(min) { var h = Math.floor(min / 60), m = min % 60; return (h ? h + " h " : "") + m + " min"; }
  function seg(s) { s = Math.round(s); return Math.floor(s / 60) + " min " + (s % 60) + " s"; }

  /* ---------- persistencia ---------- */
  function leerJson(k) { try { return JSON.parse(GD().ls(k) || "null"); } catch (e) { return null; } }
  function posta() { var p = leerJson(K_POSTA); return N().establecimiento(p || {}); }
  function guardarPosta(est) { GD().ls(K_POSTA, JSON.stringify(est)); }
  function progreso() { var g = M.progreso && M.progreso.preferencia("serums"); return g && g.casos ? g : { casos: {}, intentos: [] }; }
  function guardarProgreso(p) { if (M.progreso) M.progreso.preferencia("serums", p); }
  function sesion(caso) { var s = leerJson(K_SES + ":" + caso); return s && s.v === 1 && s.caso === caso ? s : null; }

  /* ---------- introducción cinematográfica ---------- */
  function intro(alAsumir) {
    Array.prototype.forEach.call(document.querySelectorAll("dialog.sr-intro"), function (x) { x.remove(); });
    var d = document.createElement("dialog"); d.className = "sr-intro"; d.setAttribute("aria-labelledby", "srIntroT");
    d.innerHTML = '<img class="sr-intro__img" src="' + IMG + '" alt="" width="1280" height="720"><div class="sr-intro__vel"></div><div class="sr-intro__c"><p class="sr-intro__k">Medicina rural y comunitaria</p><h2 id="srIntroT">Tu primer día como serumista</h2>' +
      '<p>Una posta de altura, pocos insumos, un hospital lejos y una comunidad que confía en ti. Cada decisión cuenta.</p><button type="button" class="sr-btn sr-btn--lg" data-asumir>Asumir mi posta</button><button type="button" class="sr-intro__o" data-omitir>Omitir</button></div>';
    document.body.appendChild(d);
    function cerrar(ir) { try { d.close(); } catch (e) {} d.remove(); try { sessionStorage.setItem("mqp_serums_intro", "1"); } catch (e) {} if (ir && alAsumir) alAsumir(); }
    d.querySelector("[data-asumir]").addEventListener("click", function () { cerrar(true); });
    d.querySelector("[data-omitir]").addEventListener("click", function () { cerrar(false); });
    d.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(false); });
    if (d.showModal) d.showModal(); else d.setAttribute("open", ""); d.querySelector("[data-asumir]").focus();
  }
  function introVista() { try { return sessionStorage.getItem("mqp_serums_intro") === "1"; } catch (e) { return false; } }

  /* ---------- portada de la estación ---------- */
  function insumosHtml(inv, ini) {
    return '<table class="sr-tabla"><caption class="sr-sr">Inventario de la posta</caption><thead><tr><th scope="col">Insumo</th><th scope="col">Disponible</th></tr></thead><tbody>' + Object.keys(N().INSUMOS).map(function (k) {
      var v = inv[k] || 0, bajo = ini && ini[k] != null ? v < ini[k] : false;
      return '<tr><th scope="row">' + esc(N().INSUMOS[k]) + '</th><td class="' + (v === 0 ? "sr-cero" : bajo ? "sr-bajo" : "") + '">' + v + (ini && ini[k] != null && ini[k] !== v ? ' <small>(inicio: ' + ini[k] + ')</small>' : "") + '</td></tr>';
    }).join("") + '</tbody></table>';
  }
  function badgeEstado(c) { return '<span class="sr-estado" title="Estado de publicación del caso">' + esc(c.estado_publicacion) + '</span>'; }

  function portada(cont, datos) {
    var casos = datos.casos, prog = progreso(), est = posta(), rec = N().recomendar(casos, prog), res = N().resumenProgreso(prog), N_ = N();
    var hechos = casos.filter(function (c) { return prog.casos[c.id]; }).length;
    var f = datos.evidencia.fuentes, nVig = f.filter(function (x) { return x.estado === "Normativa vigente verificada"; }).length;
    cont.innerHTML = '<div class="sr">' +
      '<nav class="gh-migas" aria-label="Ruta"><a href="#/guardia">Centro de simulación</a><span aria-hidden="true">›</span><span aria-current="page">Misión SERUMS</span></nav>' +
      '<header class="sr-hero"><img class="sr-hero__img" src="' + IMG + '" alt="" width="1280" height="720" fetchpriority="high"><div class="sr-hero__vel"></div><div class="sr-hero__c"><p class="sr-tags"><span class="sr-tag">Medicina rural y comunitaria</span><span class="sr-tag sr-tag--nuevo">Nuevo</span></p>' +
      '<h1>Misión SERUMS<span>Sobrevive a la posta</span></h1><p class="sr-hero__t">Atiende una posta con recursos limitados: decide, usa tu inventario, refiere a tiempo y cuida a tu comunidad. Los diez casos son originales y se apoyan en normativa peruana verificada; lo que aún falta validar está declarado.</p>' +
      '<p class="sr-hero__b"><a class="sr-btn" href="#srCasos" data-ir="srCasos">Ver los casos</a><button type="button" class="sr-btn sr-btn--claro" id="srVerIntro">▶ Ver la introducción</button></p></div></header>' +
      '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
      '<div class="sr-cols"><section class="sr-izq" id="srCasos" aria-labelledby="srCasosT" tabindex="-1"><h2 id="srCasosT">Diez casos de la posta</h2><ul class="sr-casos">' + casos.map(function (c) {
        var r = prog.casos[c.id], rc = rec && rec.caso === c.id;
        return '<li class="sr-caso' + (rc ? " is-rec" : "") + '"><p class="sr-caso__n">Caso ' + c.numero + ' · ' + esc(c.tema) + (rc ? ' · <b>Recomendado</b>' : "") + '</p><h3>' + esc(c.titulo) + '</h3><p>' + esc(c.resumen) + '</p>' +
          '<p class="sr-caso__m">' + badgeEstado(c) + '<span>≈ ' + c.duracion_min + ' min · ' + c.momentos.length + ' decisiones</span>' + (r ? '<span>Mejor: <b>' + r.mejor + ' %</b> · Intentos: ' + r.intentos + '</span>' : "") + '</p>' +
          (rc ? '<p class="sr-caso__r">' + esc(rec.motivo) + '</p>' : "") + '<a class="sr-btn sr-btn--sm" href="#/serums/' + esc(c.id) + '">' + (sesion(c.id) ? "Continuar el caso" : r ? "Reintentar" : "Comenzar el caso") + '</a></li>';
      }).join("") + '</ul></section>' +
      '<aside class="sr-der" aria-label="Panel de la posta y progreso">' +
      '<section class="sr-panel" aria-labelledby="srPostaT"><h2 id="srPostaT">Tu posta</h2><p class="sr-pz">Establecimiento ficticio configurable. Los cambios se guardan en este navegador.</p>' +
      '<form id="srForm" class="sr-form"><label>Nombre<input name="nombre" maxlength="60" value="' + esc(est.nombre) + '"></label>' +
      '<div class="sr-f2"><label>Categoría<select name="categoria">' + ["I-1", "I-2", "I-3", "I-4"].map(function (x) { return '<option' + (x === est.categoria ? " selected" : "") + '>' + x + '</option>'; }).join("") + '</select></label>' +
      '<label>Ámbito<select name="ambito">' + [["sierra", "Sierra"], ["selva", "Selva"], ["costa", "Costa rural"]].map(function (x) { return '<option value="' + x[0] + '"' + (x[0] === est.ambito ? " selected" : "") + '>' + x[1] + '</option>'; }).join("") + '</select></label></div>' +
      '<div class="sr-f2"><label>Minutos al hospital<input name="distancia_min" type="number" min="10" max="900" value="' + est.distancia_min + '"></label>' +
      '<label>Comunicación<select name="comunicacion">' + [["radio", "Radio"], ["telefono", "Teléfono"], ["ninguna", "Sin comunicación"]].map(function (x) { return '<option value="' + x[0] + '"' + (x[0] === est.comunicacion ? " selected" : "") + '>' + x[1] + '</option>'; }).join("") + '</select></label></div>' +
      '<label class="sr-chk"><input type="checkbox" name="ambulancia"' + (est.ambulancia ? " checked" : "") + '> Cuenta con ambulancia</label>' +
      '<p class="sr-form__b"><button class="sr-btn sr-btn--sm" type="submit">Guardar la posta</button><button class="sr-btn sr-btn--claro sr-btn--sm" type="button" id="srRepo">Reponer almacén</button></p><p class="sr-ok" id="srOk" role="status"></p></form>' +
      '<details class="sr-det"><summary>Inventario persistente</summary>' + insumosHtml(est.inventario) + '<p class="sr-pz">Lo que consumes en un caso se descuenta del almacén en los siguientes. «Reponer almacén» restablece las cantidades iniciales.</p></details></section>' +
      '<section class="sr-panel" aria-labelledby="srProgT"><h2 id="srProgT">Mi progreso como serumista</h2>' +
      (res.intentos ? '<p><b>' + hechos + ' de ' + casos.length + '</b> casos intentados · ' + res.intentos + ' intentos · ' + res.criticos + ' errores críticos</p><ul class="sr-ejes">' + Object.keys(N_.EJES).map(function (k) { var v = res.medias[k]; return '<li><span>' + esc(N_.EJES[k]) + '</span><span class="sr-bar" role="img" aria-label="' + (v == null ? "sin datos" : v + " %") + '"><i style="width:' + (v || 0) + '%"></i></span><b>' + (v == null ? "—" : v + " %") + '</b></li>'; }).join("") + '</ul>' + (res.eje_flojo ? '<p class="sr-pz">Eje por reforzar: <b>' + esc(N_.EJES[res.eje_flojo]) + '</b>.</p>' : "")
        : '<p class="sr-pz">Aún no has completado ningún caso. Tu progreso se calcula solo con tus intentos reales.</p>') + '</section>' +
      '<section class="sr-panel" aria-labelledby="srCampT"><h2 id="srCampT">30 días como serumista</h2><p>La campaña de 30 días usa este mismo motor: el inventario y la reputación pasan de un día al siguiente. <b>Aún no está disponible</b>: la estructura técnica y sus pruebas están listas, pero faltan los guiones de los días, que deben pasar revisión clínica.</p></section>' +
      '<section class="sr-panel" aria-labelledby="srEvT"><h2 id="srEvT">Fuentes y vigencia</h2><p>' + f.length + ' fuentes registradas: <b>' + nVig + '</b> con normativa vigente verificada, ' + (f.length - nVig) + ' en revisión o históricas. Última revisión: ' + esc(datos.evidencia.revision.ultima) + '.</p><button class="sr-btn sr-btn--claro sr-btn--sm" type="button" id="srFuentes">Ver el registro de evidencia</button></section></aside></div></div>';
    cont.querySelector("#srVerIntro").addEventListener("click", function () { intro(); });
    cont.querySelector("[data-ir]").addEventListener("click", function (ev) { ev.preventDefault(); var t = cont.querySelector("#srCasos"); t.scrollIntoView({ behavior: "smooth", block: "start" }); t.focus({ preventScroll: true }); });
    cont.querySelector("#srFuentes").addEventListener("click", function (ev) { registro(datos.evidencia, ev.currentTarget); });
    var form = cont.querySelector("#srForm");
    form.addEventListener("submit", function (ev) {
      ev.preventDefault(); var fd = new FormData(form), act = posta();
      var nuevo = N().establecimiento({ nombre: fd.get("nombre"), categoria: fd.get("categoria"), ambito: fd.get("ambito"), distancia_min: fd.get("distancia_min"), comunicacion: fd.get("comunicacion"), ambulancia: !!fd.get("ambulancia"), inventario: act.inventario });
      guardarPosta(nuevo); cont.querySelector("#srOk").textContent = "Posta guardada.";
    });
    cont.querySelector("#srRepo").addEventListener("click", function () { var act = posta(); act.inventario = JSON.parse(JSON.stringify(N().ESTABLECIMIENTO_BASE.inventario)); guardarPosta(act); portada(cont, datos); var o = cont.querySelector("#srOk"); if (o) o.textContent = "Almacén repuesto."; });
  }

  function registro(ev, disparador) {
    var fila = function (x) {
      var cls = x.estado === "Normativa vigente verificada" ? "ok" : x.estado === "Documento en revisión" ? "rev" : "hist";
      return '<li class="sr-fu"><p class="sr-fu__e sr-fu__e--' + cls + '">' + esc(x.estado) + '</p><h3>' + esc(x.titulo) + '</h3><p>' + esc(x.organismo) + ' · ' + esc(x.numero) + (x.fecha ? ' · ' + esc(x.fecha) : "") + '</p>' +
        (x.nota ? '<p class="sr-pz">' + esc(x.nota) + '</p>' : "") + '<p class="sr-pz">Verificado el ' + esc(x.verificado) + (x.indexada ? ' · texto indexado con página' : ' · texto no indexado') + (x.url ? ' · <a href="' + esc(x.url) + '" target="_blank" rel="noopener noreferrer">Abrir en el portal oficial</a>' : "") + '</p></li>';
    };
    var h = '<p class="gd-aviso" role="note">' + esc(ev.aviso) + '</p><p><b>Revisión periódica:</b> ' + esc(ev.revision.frecuencia) + '. Última: ' + esc(ev.revision.ultima) + '. ' + esc(ev.revision.regla) + '</p><ul class="sr-fus">' + ev.fuentes.map(fila).join("") + '</ul>' +
      '<h3 class="gd-h3">Historial de cambios</h3><ul>' + ev.historial.map(function (x) { return '<li>' + esc(x.fecha) + ': ' + esc(x.cambio) + '</li>'; }).join("") + '</ul>';
    GD().dialogo("Registro de evidencia de la Misión SERUMS", h, "gd-dlg--lab", disparador);
  }

  /* ---------- una atención ---------- */
  function jugar(cont, caso, datos) {
    var Nn = N();
    if (detener) detener();
    var guard = sesion(caso.id), e = guard && guard.estado && !guard.estado.fin ? guard.estado : null, tab = "paciente", ultimo = null, aviso = "";
    if (e) e.ultimo = Date.now(); else { e = Nn.iniciar(caso, posta(), Date.now()); persistir(); }
    function persistir() { GD().ls(K_SES + ":" + caso.id, JSON.stringify({ v: 1, caso: caso.id, estado: e })); }
    function salir() { if (!e.fin) persistir(); window.removeEventListener("hashchange", alIrse); GD().cerrarDialogo(); if (detener === salir) detener = null; }
    function alIrse() { if (location.hash.indexOf("#/serums/" + caso.id) !== 0) salir(); }
    detener = salir; window.addEventListener("hashchange", alIrse);

    function pintar(enfocar) {
      if (e.fin) return informe();
      var m = Nn.momentoActual(caso, e), idx = caso.momentos.indexOf(m) + 1;
      cont.innerHTML = '<div class="sr sr--caso"><nav class="gh-migas" aria-label="Ruta"><a href="#/guardia">Centro de simulación</a><span aria-hidden="true">›</span><a href="#/serums">Misión SERUMS</a><span aria-hidden="true">›</span><span aria-current="page">Caso ' + caso.numero + '</span></nav>' +
        '<header class="sr-top"><div><h1>' + esc(caso.titulo) + '</h1><p class="sr-pz">' + esc(e.establecimiento.nombre) + ' · categoría ' + esc(e.establecimiento.categoria) + ' · ' + badgeEstado(caso) + '</p></div>' +
        '<p class="sr-reloj" role="status"><span><small>Reloj de simulación</small><b id="srSim">' + reloj(e.t_sim) + '</b></span><span><small>Tiempo real</small><b id="srReal">' + seg(e.t_real) + '</b></span><span><small>Estado clínico</small><b class="sr-g sr-g--' + e.gravedad + '">' + esc(Nn.GRAVEDAD[e.gravedad]) + '</b></span></p></header>' +
        '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<div class="sr-juego"><section class="sr-ficha" aria-label="Ficha clínica"><div class="sr-tabs" role="tablist" aria-label="Ficha clínica">' + TABS.map(function (t) { return '<button role="tab" type="button" id="srT_' + t[0] + '" aria-selected="' + (t[0] === tab) + '" aria-controls="srP" tabindex="' + (t[0] === tab ? 0 : -1) + '" data-tab="' + t[0] + '">' + t[1] + '</button>'; }).join("") + '</div><div class="sr-tabp" role="tabpanel" id="srP" aria-labelledby="srT_' + tab + '" tabindex="0">' + panel(tab) + '</div></section>' +
        '<section class="sr-decision" aria-labelledby="srDecT"><p class="sr-paso">Decisión ' + idx + ' de ' + caso.momentos.length + ' · ' + esc(Nn.EJES[m.eje]) + '</p><h2 id="srDecT" tabindex="-1">' + esc(m.titulo) + '</h2><p>' + esc(m.texto) + '</p>' +
        (aviso ? '<p class="sr-aviso" role="status">' + aviso + '</p>' : "") +
        '<fieldset class="sr-ops"><legend class="sr-sr">Alternativas</legend>' + m.opciones.map(function (o) {
          var d = Nn.disponibilidad(o, e), tx = (o.cons ? Object.keys(o.cons).map(function (k) { return o.cons[k] + " × " + Nn.INSUMOS[k]; }).join(", ") : "");
          return '<label class="sr-op' + (d.ok ? "" : " is-off") + '"><input type="radio" name="op" value="' + esc(o.id) + '"' + (d.ok ? "" : " disabled") + '><span><b>' + esc(o.id.toUpperCase()) + '.</b> ' + esc(o.texto) + (tx ? '<small>Usa: ' + esc(tx) + '</small>' : "") + (d.ok ? "" : '<small class="sr-bloq">' + esc(d.motivo) + '</small>') + '</span></label>';
        }).join("") + '</fieldset><p class="sr-pz">Tu respuesta se registra sin corregirla: la explicación completa aparece en el informe final.</p><p><button type="button" class="sr-btn" id="srDecidir" disabled>Registrar decisión</button></p></section></div></div>';
      var tabs = cont.querySelectorAll("[data-tab]");
      Array.prototype.forEach.call(tabs, function (b, i) {
        b.addEventListener("click", function () { tab = b.getAttribute("data-tab"); pintar(); cont.querySelector("#srT_" + tab).focus(); });
        b.addEventListener("keydown", function (ev) { var j = ev.key === "ArrowRight" ? i + 1 : ev.key === "ArrowLeft" ? i - 1 : ev.key === "Home" ? 0 : ev.key === "End" ? tabs.length - 1 : -1; if (j < 0) return; ev.preventDefault(); tab = tabs[(j + tabs.length) % tabs.length].getAttribute("data-tab"); pintar(); cont.querySelector("#srT_" + tab).focus(); });
      });
      var rad = cont.querySelectorAll('input[name="op"]'), bt = cont.querySelector("#srDecidir");
      Array.prototype.forEach.call(rad, function (r) { r.addEventListener("change", function () { bt.disabled = false; }); });
      bt.addEventListener("click", function () {
        var sel = cont.querySelector('input[name="op"]:checked'); if (!sel) return;
        var antes = e, r = Nn.decidir(caso, e, sel.value, Date.now()); if (!r.ok) { aviso = esc(r.motivo); pintar(); return; }
        e = r.estado; aviso = consecuencia(antes, e, r.opcion); persistir(); if (e.fin) { finalizar(); return; }
        pintar(); var h = cont.querySelector("#srDecT"); if (h) h.focus();
      });
      var pr = cont.querySelectorAll("[data-prueba]");
      Array.prototype.forEach.call(pr, function (b) { b.addEventListener("click", function () {
        var r = Nn.solicitarPrueba(caso, e, b.getAttribute("data-prueba"), Date.now()); if (!r.ok) { aviso = esc(r.motivo); } else { e = r.estado; aviso = "Prueba solicitada. Pasaron " + (por(caso.pruebas, b.getAttribute("data-prueba")).min || 0) + " min de simulación."; persistir(); }
        pintar(); cont.querySelector("#srT_pruebas").focus(); }); });
      var sup = cont.querySelector("#srSup"); if (sup) sup.addEventListener("submit", function (ev) { ev.preventDefault(); supervisor(cont.querySelector("#srQ").value, cont.querySelector("#srRes"), caso, datos); });
    }

    /* describe lo que cambió en el mundo sin revelar si la decisión fue buena */
    function consecuencia(a, b, o) {
      var p = ["Decisión registrada. Pasaron " + (b.t_sim - a.t_sim) + " min de simulación."], g = {}; Object.keys(o.cons || {}).forEach(function (k) { if (a.inventario[k] !== b.inventario[k]) g[k] = a.inventario[k] - b.inventario[k]; });
      var gasto = Object.keys(g).map(function (k) { return g[k] + " × " + N().INSUMOS[k]; }); if (gasto.length) p.push("Se usó: " + gasto.join(", ") + ".");
      b.historial.slice(a.historial.length).filter(function (h) { return h.tipo === "evento"; }).forEach(function (h) { p.push("<b>Evento:</b> " + esc(h.texto)); });
      return p.map(function (x) { return x.charAt(0) === "<" ? x : esc(x); }).join(" ");
    }

    function panel(t) {
      var P = caso.paciente, v = e.vitales, h = '';
      if (t === "paciente") {
        h = '<h3>' + esc(P.titulo) + '</h3><p>' + esc(P.motivo) + '</p>' + vitales(v) + '<p class="sr-pz">Estado clínico actual: <b>' + esc(N().GRAVEDAD[e.gravedad]) + '</b>. Cambia según tus decisiones y el paso del tiempo simulado.</p>';
      } else if (t === "historia") {
        h = '<dl class="sr-dl">' + caso.historia.map(function (x) { return '<dt>' + esc(x.rotulo) + '</dt><dd>' + esc(x.texto) + '</dd>'; }).join("") + '</dl>';
      } else if (t === "examen") {
        h = (caso.examen.length ? '<dl class="sr-dl">' + caso.examen.map(function (x) { return '<dt>' + esc(x.rotulo) + '</dt><dd>' + esc(x.texto) + '</dd>'; }).join("") + '</dl>' : '<p class="sr-pz">Este caso no tiene un examen físico individual: la valoración es de la jornada.</p>') + vitales(v);
      } else if (t === "pruebas") {
        h = caso.pruebas.length ? '<ul class="sr-pruebas">' + caso.pruebas.map(function (p) {
          var hecha = e.pruebas.indexOf(p.id) >= 0, falta = p.insumo && (e.inventario[p.insumo] || 0) < 1;
          return '<li><b>' + esc(p.nombre) + '</b><small>' + p.min + ' min' + (p.insumo ? ' · usa ' + esc(N().INSUMOS[p.insumo]) : "") + '</small>' + (hecha ? '<p class="sr-res">Resultado: ' + esc(p.resultado) + '</p>' : '<button type="button" class="sr-btn sr-btn--sm sr-btn--claro" data-prueba="' + esc(p.id) + '"' + (falta ? " disabled" : "") + '>Solicitar</button>' + (falta ? '<small class="sr-bloq">Insumo insuficiente</small>' : "")) + '</li>';
        }).join("") + '</ul>' : '<p class="sr-pz">En este caso no hay pruebas disponibles en la posta.</p>';
      } else if (t === "inventario") {
        h = insumosHtml(e.inventario, e.inventario_inicial);
      } else if (t === "referencia") {
        var R = e.referencia, est = e.establecimiento, bloq = e.flags.indexOf("via_bloqueada") >= 0;
        h = '<dl class="sr-dl"><dt>Distancia al hospital</dt><dd>' + est.distancia_min + ' min por carretera</dd><dt>Ambulancia</dt><dd>' + (est.ambulancia ? "Disponible" : "No disponible: el traslado se demora más") + '</dd><dt>Comunicación</dt><dd>' + esc({ radio: "Radio", telefono: "Teléfono", ninguna: "Sin comunicación" }[est.comunicacion]) + '</dd><dt>Estado de la vía</dt><dd>' + (bloq ? "<b>Bloqueada</b>" : "Transitable") + '</dd>' +
          '<dt>Tiempo estimado de traslado</dt><dd>' + reloj(N().tiempoReferencia(e)) + '</dd><dt>Estado de la referencia</dt><dd>' + esc({ ninguna: "Sin referencia", solicitada: "Referencia de emergencia solicitada", programada: "Referencia programada", rechazada: "Referencia no realizada" }[R.estado]) + '</dd></dl><p class="sr-pz">La referencia transfiere la responsabilidad a un establecimiento de mayor capacidad; la contrarreferencia devuelve al paciente con indicaciones. Lo que decidas en el caso se evalúa con el eje «Referencia y comunicación».</p>';
      } else if (t === "normativa") {
        h = fuentesCaso() + '<form id="srSup" class="sr-sup"><label for="srQ"><b>Consultar al supervisor</b></label><p class="sr-pz">Búsqueda documental en las fuentes indexadas de este caso. No es una IA: te muestra fragmentos reales con su página.</p><div class="sr-sup__f"><input id="srQ" type="search" placeholder="Ej.: criterios de severidad" autocomplete="off" required><button class="sr-btn sr-btn--sm" type="submit">Buscar</button></div></form><div id="srRes" aria-live="polite"></div>';
      } else {
        var lin = e.historial;
        h = lin.length ? '<ol class="sr-evo">' + lin.map(function (x) {
          if (x.tipo === "evento") return '<li class="sr-evo__e"><b>Minuto ' + x.t_sim + ' · Evento.</b> ' + esc(x.texto) + '</li>';
          if (x.tipo === "prueba") return '<li><b>Minuto ' + x.t_sim + ' · Prueba solicitada.</b> ' + esc(x.texto) + '</li>';
          var m = por(caso.momentos, x.momento), o = por(m.opciones, x.opcion);
          return '<li><b>Minuto ' + x.t_sim + ' · ' + esc(m.titulo) + '.</b> Elegiste: ' + esc(o.texto) + '</li>';
        }).join("") + '</ol>' : '<p class="sr-pz">Aún no hay acciones registradas.</p>';
      }
      return h;
    }
    function vitales(v) {
      var L = { fc: ["Frecuencia cardiaca", "lpm"], fr: ["Frecuencia respiratoria", "rpm"], sat: ["Saturación de oxígeno", "%"], temp: ["Temperatura", "°C"], pas: ["PA sistólica", "mm Hg"], pad: ["PA diastólica", "mm Hg"] };
      var k = Object.keys(v).filter(function (x) { return L[x]; }); if (!k.length) return "";
      return '<ul class="sr-vit">' + k.map(function (x) { return '<li><small>' + L[x][0] + '</small><b>' + v[x] + '</b> ' + L[x][1] + '</li>'; }).join("") + '</ul>';
    }
    function fuentesCaso() {
      var ids = caso.evidencia || [], f = datos.evidencia.fuentes;
      var h = ids.length ? '<h3>Fuentes de este caso</h3><ul class="sr-fus">' + ids.map(function (id) { var x = por(f, id); return x ? '<li class="sr-fu"><p class="sr-fu__e sr-fu__e--ok">' + esc(x.estado) + '</p><h4>' + esc(x.titulo) + '</h4><p class="sr-pz">' + esc(x.numero) + ' · ' + esc(x.fecha) + '</p></li>' : ""; }).join("") + '</ul>' : '<p class="sr-pz">Este caso aún no tiene una fuente documental indexada.</p>';
      return h + '<div class="sr-pend"><b>Pendiente de validación científica</b><ul>' + caso.pendientes.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul></div>';
    }

    function finalizar() {
      var ev = Nn.evaluar(caso, e), p = Nn.registrarIntento(progreso(), caso, ev, Date.now()); guardarProgreso(p);
      var pst = posta(); Object.keys(ev.consumo).forEach(function (k) { pst.inventario[k] = Math.max(0, (pst.inventario[k] || 0) - ev.consumo[k]); }); if (!caso.inventario_ajuste) guardarPosta(pst);
      GD().ls(K_SES + ":" + caso.id, null); informe(ev);
    }

    function informe(ev) {
      ev = ev || Nn.evaluar(caso, e); var Nm = Nn, dec = e.historial.filter(function (h) { return h.tipo === "decision"; }), f = datos.evidencia.fuentes, rec = Nm.recomendar(datos.casos, progreso()), flojo = ev.ejes.filter(function (x) { return x.pct != null; }).sort(function (a, b) { return a.pct - b.pct; })[0];
      var sec = function (l, t, c) { return '<section class="sr-sec" aria-labelledby="srS' + l + '"><h2 id="srS' + l + '"><span>' + l + '</span>' + esc(t) + '</h2>' + c + '</section>'; };
      var A = '<p class="sr-nota sr-nota--' + (ev.total >= 75 ? "ok" : ev.total >= 60 ? "med" : "mal") + '"><b>' + ev.total + ' / 100</b> · ' + esc(ev.banda) + '</p>' + (ev.topado_por_error_critico ? '<p class="sr-alerta" role="alert">Cometiste al menos un error crítico de seguridad: el puntaje máximo posible queda limitado a ' + Nm.TOPE_CRITICO + '.</p>' : "") +
        '<ul class="sr-ejes">' + ev.ejes.map(function (x) { return '<li><span>' + esc(x.nombre) + ' <small>(' + x.peso + ' pts)</small></span><span class="sr-bar" role="img" aria-label="' + (x.pct == null ? "no aplica" : x.pct + " %") + '"><i style="width:' + (x.pct || 0) + '%"></i></span><b>' + (x.pct == null ? "No aplica" : x.pct + " %") + '</b></li>'; }).join("") + '</ul><p><b>Desenlace:</b> ' + esc(ev.desenlace_texto) + '</p>';
      var B = '<ol class="sr-dec">' + dec.map(function (x) {
        var m = por(caso.momentos, x.momento), o = por(m.opciones, x.opcion), mejor = m.opciones.filter(function (q) { return q.calidad === "optima"; })[0];
        return '<li class="sr-dec__i sr-dec__i--' + o.calidad + '"><h3>' + esc(m.titulo) + '</h3><p>Elegiste: <b>' + esc(o.texto) + '</b></p><p class="sr-q">' + esc(CALIDAD[o.calidad]) + (o.error ? ' · ' + esc(Nm.ERRORES[o.error]) : "") + '</p><p>' + esc(o.retro) + '</p>' +
          (o.calidad !== "optima" ? '<p><b>Mejor opción:</b> ' + esc(mejor.texto) + '. ' + esc(mejor.retro) + '</p>' : "") +
          ((o.ref || []).length ? '<p class="sr-pz">Fuente: ' + o.ref.map(function (r) { var d = por(f, r.doc); return esc(d ? d.numero : r.doc) + ', p. ' + r.pag; }).join("; ") + '</p>' : '<p class="sr-pz">Sin cita documental verificada: <b>pendiente de validación científica</b>.</p>') + '</li>';
      }).join("") + '</ol>';
      var ek = Object.keys(ev.errores), C = ek.length ? '<ul>' + ek.map(function (k) { return '<li>' + esc(Nm.ERRORES[k]) + ': <b>' + ev.errores[k] + '</b></li>'; }).join("") + '</ul>' : '<p>No cometiste errores clasificados en este intento.</p>';
      var ck = Object.keys(ev.consumo), D = ck.length ? '<ul>' + ck.map(function (k) { return '<li>' + esc(Nm.INSUMOS[k]) + ': <b>' + ev.consumo[k] + '</b> usados</li>'; }).join("") + '</ul><p class="sr-pz">Se descontaron de tu almacén persistente.</p>' : '<p>No consumiste insumos.</p>';
      var E = '<ul><li>Tiempo de simulación: <b>' + reloj(ev.t_sim) + '</b></li><li>Tiempo real: <b>' + seg(ev.t_real) + '</b></li><li>Referencia: <b>' + esc({ ninguna: "no hubo", solicitada: "de emergencia", programada: "programada", rechazada: "no realizada" }[ev.referencia.estado]) + '</b></li><li>Traslado estimado: <b>' + reloj(Nm.tiempoReferencia(e)) + '</b>' + (e.flags.indexOf("via_bloqueada") >= 0 ? ' (vía bloqueada)' : "") + '</li></ul><p class="sr-pz">El tiempo simulado mide cuánto tardó el paciente en recibir cada acción; el tiempo real, cuánto pensaste.</p>';
      var F = fuentesCaso();
      var G = (flojo ? '<p>Tu eje más bajo en este caso fue «' + esc(flojo.nombre) + '» (' + flojo.pct + ' %). Repasa las decisiones de ese eje en la sección B.</p>' : "") + (rec ? '<p>Siguiente caso sugerido: <a href="#/serums/' + esc(rec.caso) + '">' + esc(por(datos.casos, rec.caso).titulo) + '</a>. ' + esc(rec.motivo) + '</p>' : "");
      var H = '<p>Estado de publicación: <b>' + esc(caso.estado_publicacion) + '</b>. Este caso no ha sido validado por un especialista; trátalo como material de estudio y confirma siempre con la norma vigente.</p>';
      cont.innerHTML = '<div class="sr sr--informe"><nav class="gh-migas" aria-label="Ruta"><a href="#/serums">Misión SERUMS</a><span aria-hidden="true">›</span><span aria-current="page">Informe del caso ' + caso.numero + '</span></nav><h1 tabindex="-1" id="srInf">Informe: ' + esc(caso.titulo) + '</h1><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        sec("A", "Resultado", A) + sec("B", "Tus decisiones", B) + sec("C", "Errores por tipo", C) + sec("D", "Recursos e inventario", D) + sec("E", "Referencia y tiempos", E) + sec("F", "Normativa y vigencia", F) + sec("G", "Cómo mejorar", G) + sec("H", "Estado de validación", H) +
        '<p class="sr-fin"><a class="sr-btn" href="#/serums">Volver a la posta</a><button class="sr-btn sr-btn--claro" type="button" id="srRei">Reintentar el caso</button></p></div>';
      cont.querySelector("#srRei").addEventListener("click", function () { GD().ls(K_SES + ":" + caso.id, null); e = Nn.iniciar(caso, posta(), Date.now()); persistir(); aviso = ""; tab = "paciente"; pintar(); });
      var h = cont.querySelector("#srInf"); if (h) h.focus();
    }
    pintar();
  }

  function supervisor(q, salida, caso, datos) {
    salida.innerHTML = '<p class="sr-pz">Buscando…</p>';
    cargarIndice().then(function (ind) {
      var docs = (caso.evidencia || []).length ? caso.evidencia : null;
      if (!docs) { salida.innerHTML = '<p class="sr-pz">Este caso no tiene fuentes indexadas. No puedo citar documentos para esta consulta.</p>'; return; }
      var r = N().buscar(ind, q, 3, docs);
      if (!r.length) { salida.innerHTML = '<p>No encontré fragmentos relacionados en las fuentes de este caso. Prueba con otras palabras.</p>'; return; }
      salida.innerHTML = '<ul class="sr-fus">' + r.map(function (x) {
        var d = por(datos.evidencia.fuentes, x.doc);
        return '<li class="sr-fu"><p class="sr-fu__e sr-fu__e--ok">' + esc(d ? d.estado : "") + '</p><h4>' + esc(d ? d.numero : x.doc) + ' · página ' + x.pagina + '</h4><blockquote>' + esc(x.texto) + '</blockquote></li>';
      }).join("") + '</ul><p class="sr-pz">Fragmentos textuales del documento; confirma el contexto en la fuente completa.</p>';
    }).catch(function () { salida.innerHTML = '<p class="sr-pz">No se pudo cargar el índice documental. Revisa tu conexión.</p>'; });
  }

  /* ---------- entrada ---------- */
  function montar(cont, arg) {
    cont.innerHTML = '<div class="app-loading" role="status"><span>Cargando la Misión SERUMS…</span></div>';
    asegurarDatos().then(function () {
      var datos = raiz.MQP_SERUMS;
      if (arg) {
        var c = por(datos.casos, arg);
        if (!c) { cont.innerHTML = '<p>No se encontró el caso. <a href="#/serums">Volver a la posta</a></p>'; return; }
        jugar(cont, c, datos);
      } else {
        if (detener) detener();
        portada(cont, datos);
        if (!introVista()) intro();
      }
    }, function () { cont.innerHTML = '<p class="muted">No se pudo cargar la Misión SERUMS. Revisa tu conexión e inténtalo de nuevo.</p>'; });
  }

  M.serums = { montar: montar, asegurarDatos: asegurarDatos, intro: intro, AVISO: AVISO };
})(typeof window !== "undefined" ? window : this);
