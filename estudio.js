/* MedQuizPlus · Estudio con evidencia: (1) confianza al responder y (2) «Repaso de hoy».
   Todo se guarda en la cuenta (estudio.php). La confianza NO cambia el puntaje ni lo que se muestra de la pregunta: es un registro aparte.
   Sin cuenta no se pide nada (no habría dónde guardarlo) y el banqueo funciona exactamente igual. Si el servidor falla, el estudiante sigue sin enterarse. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var BASE = M.base || "", KEY = "mqp_estudio_confianza";
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function lsGet(k, d) { try { var v = window.localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } }
  function lsSet(k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* sin almacenamiento: no se recuerda */ } }
  function nuevoId() { var a = new Uint8Array(12); (window.crypto || window.msCrypto).getRandomValues(a); return "i" + Array.prototype.map.call(a, function (b) { return ("0" + b.toString(16)).slice(-2); }).join(""); }
  function api(accion, datos) {
    var o = { method: datos ? "POST" : "GET", credentials: "same-origin", cache: "no-store" };
    if (datos) { o.headers = { "Content-Type": "application/json", "X-MQP": "1" }; o.body = JSON.stringify(datos); }
    return fetch(BASE + "estudio.php?a=" + accion, o).then(function (r) { return r.json().then(function (j) { return { http: r.status, ok: r.ok && j && j.ok !== false, j: j || {} }; }, function () { return { http: r.status, ok: false, j: {} }; }); },
      function () { return { http: 0, ok: false, j: {} }; });
  }

  /* ¿hay sesión? Se consulta al cargar y al volver a la pestaña (por si inició sesión después) */
  var sesion = null, ultimaRevision = 0;
  function revisarSesion() { ultimaRevision = Date.now(); return api("estado").then(function (r) { sesion = !!(r.ok && r.j.sesion); }); }
  revisarSesion();
  window.addEventListener("focus", function () { if (Date.now() - ultimaRevision > 30000) revisarSesion(); });
  window.addEventListener("hashchange", function () { if (!sesion && Date.now() - ultimaRevision > 5000) revisarSesion(); });
  function activo() { return sesion === true && lsGet(KEY, "si") === "si"; }

  /* ---------- confianza al responder (modo estudio) ---------- */
  var pend = null;
  function quitarBarra() { var b = document.getElementById("estConf"); if (b) b.remove(); pend = null; }
  function quitarNota() { var n = document.getElementById("estNota"); if (n) n.remove(); }
  function cancelar() { quitarBarra(); quitarNota(); }
  /* devuelve true si tomó el control (muestra la barra y llamará a alConfirmar(conf)); false si no corresponde pedir confianza */
  function pedirConfianza(o) {
    if (!activo() || !o || !o.contenedor || !o.pregunta) return false;
    quitarNota();
    var botones = o.contenedor.querySelectorAll(".opt");
    for (var k = 0; k < botones.length; k++) { var on = botones[k].getAttribute("data-letra") === o.letra; botones[k].classList.toggle("opt--chosen", on); botones[k].setAttribute("aria-pressed", on ? "true" : "false"); }
    var bar = document.getElementById("estConf"), nueva = !bar;
    if (!bar) { bar = document.createElement("div"); bar.id = "estConf"; bar.className = "est-conf"; bar.setAttribute("role", "group"); bar.setAttribute("aria-labelledby", "estConfT"); o.contenedor.parentNode.insertBefore(bar, o.contenedor.nextSibling); }
    pend = o;
    bar.innerHTML = '<p class="est-conf__t" id="estConfT">Elegiste la <strong>' + esc(o.letra) + '</strong>. ¿Qué tan seguro estás? <span class="est-conf__s">Esto no cambia tu puntaje.</span></p>' +
      '<div class="est-conf__bt"><button type="button" class="btn btn--ghost" data-c="baja">Adiviné</button><button type="button" class="btn btn--ghost" data-c="media">Dudaba entre dos</button><button type="button" class="btn btn--ghost" data-c="alta">Estoy seguro</button></div>' +
      '<p class="est-conf__ft"><button type="button" class="est-link" data-c="">Responder sin indicar</button><button type="button" class="est-link" data-no>No volver a preguntar</button></p>';
    bar.onclick = function (ev) {
      var b = ev.target.closest && ev.target.closest("button"); if (!b || !pend) return;
      var cb = pend.alConfirmar, conf;
      if (b.hasAttribute("data-no")) { lsSet(KEY, "no"); conf = null; }
      else { var c = b.getAttribute("data-c"); conf = c ? c : null; }
      quitarBarra(); cb(conf);
    };
    if (nueva) { var p = bar.querySelector("button"); if (p) p.focus({ preventScroll: false }); }
    return true;
  }

  /* guarda el intento (el servidor decide el acierto y la etiqueta) y, si queda algo por reforzar, lo dice */
  var TXT = { falso_concepto: "Falso concepto de alta prioridad", refuerzo: "Necesita refuerzo", laguna: "Posible laguna de comprensión", acierto_dudoso: "Acierto con dudas" };
  function registrar(q, letra, conf, modo) {
    if (sesion !== true || !q || !q.id) return;
    api("intento", { pregunta_id: q.id, elegida: letra, confianza: conf || null, modo: modo || "estudio", req_id: nuevoId() }).then(function (r) {
      if (!r.ok || !r.j.pendiente) return;
      var v = document.getElementById("svVerdict"); if (!v || !v.parentNode) return;
      quitarNota();
      var n = document.createElement("p"); n.id = "estNota"; n.className = "est-nota"; n.setAttribute("role", "status");
      n.innerHTML = 'Lo anotamos como <strong>' + esc(TXT[r.j.etiqueta] || r.j.texto) + '</strong>. Aparecerá en <a href="#/repaso">Repaso de hoy</a>.';
      v.parentNode.insertBefore(n, v.nextSibling);
    });
  }

  /* ---------- Repaso de hoy ---------- */
  var ETQ_CLASE = { falso_concepto: "est-b--alta", refuerzo: "est-b--ref", laguna: "est-b--lag", acierto_dudoso: "est-b--dud" };
  function plural(n, a, b) { return n + " " + (n === 1 ? a : b); }
  function pct(a, n) { return n ? Math.round(a / n * 100) + " %" : "—"; }
  function montarRepaso(root) {
    root.innerHTML = '<div class="app-loading" role="status"><span>Preparando tu repaso de hoy…</span></div>';
    api("repaso").then(function (r) {
      if (r.http === 401) { root.innerHTML = '<div class="empty-state"><p class="empty-state__title">Entra para ver tu repaso de hoy</p><p class="empty-state__text">Tu confianza y tus errores se guardan en tu cuenta para que el repaso sea tuyo desde cualquier dispositivo.</p><a class="btn btn--primary" href="#/ingresar">Ingresar</a> <a class="btn btn--ghost" href="#/registro">Crear cuenta</a></div>'; return; }
      if (!r.ok) { root.innerHTML = '<div class="empty-state"><p class="empty-state__title">No pudimos cargar tu repaso</p><p class="empty-state__text">Inténtalo de nuevo en un momento. Tu práctica y tus flashcards siguen funcionando.</p><button class="btn btn--primary" type="button" data-reintentar>Reintentar</button></div>'; root.querySelector("[data-reintentar]").addEventListener("click", function () { montarRepaso(root); }); return; }
      var d = r.j, ref = d.refuerzo, tj = d.tarjetas, s = d.semana, cal = d.calibracion;
      var h = '<div class="est-wrap"><header class="page-head"><p class="kicker">Estudio</p><h1 class="page-head__title">Repaso de hoy</h1><p class="page-head__lead">Lo que conviene repasar ahora: tus tarjetas vencidas y las preguntas donde tu confianza no coincidió con tu resultado.</p></header>' +
        '<dl class="fc-kpis"><div class="fc-kpi"><dt>Tarjetas pendientes</dt><dd>' + tj.pendientes + '</dd></div><div class="fc-kpi"><dt>Preguntas por reforzar</dt><dd>' + ref.length + '</dd></div><div class="fc-kpi"><dt>Intentos (7 días)</dt><dd>' + s.intentos + '</dd></div></dl>';
      h += '<section class="card card--spaced"><h2 class="card__h">1. Tus flashcards</h2>' + (tj.total ? '<p>' + (tj.pendientes ? "Tienes <strong>" + plural(tj.pendientes, "tarjeta pendiente", "tarjetas pendientes") + "</strong> según tu calendario de repaso." : "No tienes tarjetas pendientes ahora.") + '</p><p><a class="btn ' + (tj.pendientes ? "btn--primary" : "btn--ghost") + '" href="#/flashcards">' + (tj.pendientes ? "Repasar mis tarjetas" : "Ver mis tarjetas") + "</a></p>"
        : '<p class="muted">Todavía no tienes flashcards. Al terminar una pregunta puedes pulsar «Convertir en flashcard» (incluye tarjetas para completar el hueco).</p>') + "</section>";
      h += '<section class="card card--spaced"><h2 class="card__h">2. Preguntas por reforzar</h2>';
      if (!ref.length) {
        h += '<p class="muted">' + (d.con_confianza ? "No tienes preguntas por reforzar: tus últimos intentos fueron aciertos." : "Aún no hay datos. Responde en modo estudio e indica qué tan seguro estás: las preguntas que falles con seguridad, adivines o contestes con dudas aparecerán aquí.") + "</p>";
      } else {
        h += '<p class="muted small">Ordenadas por una regla simple: peso de la etiqueta (falso concepto &gt; refuerzo &gt; laguna &gt; acierto con dudas) más las veces que ya te costó. Una pregunta sale de la lista cuando la aciertas. Esto no es un calendario de repetición espaciada.</p>' +
          '<p><button class="btn btn--primary" type="button" data-accion="repaso" data-ids="' + esc(d.ids.slice(0, 20).join(",")) + '">Practicar ' + plural(Math.min(20, d.ids.length), "pregunta", "preguntas") + '</button></p><ul class="qlist">' +
          ref.map(function (x) {
            return '<li class="qitem"><div class="qitem__meta"><span class="tag">' + esc(x.especialidad) + '</span><span class="est-b ' + (ETQ_CLASE[x.etiqueta] || "") + '">' + esc(x.texto) + '</span><span class="qitem__id">' + esc(x.pregunta) + '</span></div>' +
              '<p class="qitem__stem">' + esc(x.enunciado) + (x.enunciado.length >= 170 ? "…" : "") + '</p><div class="qitem__foot"><span class="qitem__ans">Intentos: ' + x.intentos + (x.pendientes_previos ? " · ya te costó " + x.pendientes_previos + (x.pendientes_previos === 1 ? " vez antes" : " veces antes") : "") + '</span>' +
              '<button class="btn btn--ghost btn--sm" type="button" data-accion="repaso" data-ids="' + esc(x.pregunta) + '">Practicar</button></div></li>';
          }).join("") + "</ul>";
      }
      h += "</section>";
      h += '<section class="card card--spaced"><h2 class="card__h">3. Qué tan bien calibrada está tu confianza</h2>';
      if (!d.con_confianza) h += '<p class="muted">Aún no registraste tu confianza en ninguna respuesta.</p>';
      else h += '<table class="est-tabla"><thead><tr><th scope="col">Dijiste</th><th scope="col">Respuestas</th><th scope="col">Acertaste</th></tr></thead><tbody>' +
        [["alta", "Estoy seguro"], ["media", "Dudaba entre dos"], ["baja", "Adiviné"]].map(function (k) { var c = cal[k[0]]; return "<tr><th scope=\"row\">" + k[1] + "</th><td>" + c.n + "</td><td>" + (c.n ? c.aciertos + " de " + c.n + " (" + pct(c.aciertos, c.n) + ")" : "—") + "</td></tr>"; }).join("") + "</tbody></table>" +
        '<p class="muted small">' + (d.con_confianza < 20 ? "Con menos de 20 respuestas registradas estos porcentajes todavía no permiten concluir nada." : "Si te sientes seguro y aciertas menos de lo esperado, conviene revisar esos conceptos; si aciertas cuando adivinas, tienes lagunas de comprensión, no de suerte.") + "</p>";
      h += "</section>";
      h += '<section class="card card--spaced est-ajustes"><h2 class="card__h">Ajustes</h2><label class="est-check"><input type="checkbox" id="estAj"' + (lsGet(KEY, "si") === "si" ? " checked" : "") + '> Preguntarme mi confianza al responder en modo estudio</label>' +
        '<p class="muted small">En simulacro no se pregunta nada. Tu confianza no cambia el puntaje.</p><p><button class="btn btn--ghost btn--sm btn--danger" type="button" id="estOlvidar">Borrar mi historial de confianza</button></p></section></div>';
      root.innerHTML = h;
      root.querySelector("#estAj").addEventListener("change", function (e) { lsSet(KEY, e.target.checked ? "si" : "no"); });
      var ol = root.querySelector("#estOlvidar");
      ol.addEventListener("click", function () {
        if (ol.getAttribute("data-a") !== "1") { ol.setAttribute("data-a", "1"); ol.textContent = "¿Seguro? Pulsa otra vez"; return; }
        ol.disabled = true; api("olvidar", {}).then(function () { montarRepaso(root); });
      });
    });
  }

  M.estudio = { pedirConfianza: pedirConfianza, cancelar: cancelar, registrar: registrar, montarRepaso: montarRepaso, activo: activo };
})();
