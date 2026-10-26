/* MedQuizPlus · Tutor Feynman IA — interfaz.
   Módulo ADICIONAL: no modifica preguntas, claves, comentarios ni flujogramas. Se abre desde (1) «Aprender con Feynman» en la retroalimentación de
   una pregunta, (2) el visor de «Ver flujograma» y (3) la sección #/feynman. Toda la evaluación, las fases y los resultados viven en el servidor
   (feynman.php): este archivo solo muestra lo que el servidor devuelve y manda lo que el estudiante escribe o dicta.
   Voz: feynman_voz.js (dictado y lectura del navegador); estados: feynman_estado.js. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var BASE = M.base || "";
  var Voz = M.feynmanVoz, Est = M.feynmanEstado;
  if (!Voz || !Est) return;

  /* ---------- utilidades ---------- */
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function lsGet(k, d) { try { var v = window.localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } }
  function lsSet(k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* almacenamiento bloqueado: se sigue sin recordar */ } }
  function nuevoId() { var a = new Uint8Array(12); (window.crypto || window.msCrypto).getRandomValues(a); return "r" + Array.prototype.map.call(a, function (b) { return ("0" + b.toString(16)).slice(-2); }).join(""); }
  /* formato mínimo y seguro: recibe texto SIN escapar, escapa y solo añade negrita, listas y párrafos */
  function md(t) {
    var h = esc(t).replace(/\[G(\d{1,2})\]/g, '<sup class="fy-cita">[$1]</sup>').replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>"), out = [], lista = false;
    h.split("\n").forEach(function (l) {
      var m = l.match(/^\s*(?:[-*•]|\d+[.)])\s+(.*)$/);
      if (m) { if (!lista) { out.push("<ul>"); lista = true; } out.push("<li>" + m[1] + "</li>"); return; }
      if (lista) { out.push("</ul>"); lista = false; }
      if (l.trim()) out.push("<p>" + l + "</p>");
    });
    if (lista) out.push("</ul>");
    return out.join("");
  }
  function fecha(t) { try { return new Date(t * 1000).toLocaleDateString("es-PE", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" }); } catch (e) { return ""; } }
  function ico(n) {
    var P = {
      mic: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
      stop: '<rect x="6" y="6" width="12" height="12" rx="2"/>',
      play: '<path d="M8 5v14l11-7z"/>',
      pausa: '<path d="M9 5v14M15 5v14"/>',
      voz: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11"/>',
      vozoff: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M17 9l4 6M21 9l-4 6"/>',
      enviar: '<path d="M4 12l16-8-6 16-3-7z"/>',
      pista: '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
      libro: '<path d="M4 19.5V5a2 2 0 0 1 2-2h13v15H6a2 2 0 0 0-2 2z"/>',
      cerrar: '<path d="M6 6l12 12M18 6L6 18"/>'
    };
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + P[n] + "</svg>";
  }

  /* ---------- API ---------- */
  function api(accion, datos, opt) {
    var o = { method: datos ? "POST" : "GET", credentials: "same-origin", cache: "no-store" };
    if (datos) { o.headers = { "Content-Type": "application/json", "X-MQP": "1" }; o.body = JSON.stringify(datos); }
    if (opt && opt.senal) o.signal = opt.senal;
    return fetch(BASE + "feynman.php?a=" + accion, o).then(function (r) {
      return r.json().then(function (j) { return { http: r.status, ok: r.ok && j && j.ok !== false, j: j || {} }; }, function () { return { http: r.status, ok: false, j: { error: "El servidor respondió de forma inesperada. Inténtalo de nuevo." } }; });
    }, function (e) { return { http: 0, ok: false, abortado: !!(e && e.name === "AbortError"), j: { error: "No hay conexión con el servidor. Tu texto sigue aquí: inténtalo de nuevo." } }; });
  }
  function textoError(r) {
    if (r.http === 401) return 'Para usar el Tutor Feynman IA necesitas una cuenta. <a href="#/registro">Crear cuenta</a> · <a href="#/ingresar">Ingresar</a>';
    if (r.http === 402) return 'El Tutor Feynman IA es parte de los planes de pago. <a href="#/planes">Ver planes</a>';
    return esc((r.j && r.j.error) || "Ocurrió un problema. Inténtalo de nuevo.");
  }

  /* ---------- montaje ---------- */
  var activo = null;           // un solo tutor montado a la vez (voz y micrófono son recursos únicos)

  function montar(root, opts) {
    opts = opts || {};
    if (activo) activo.destruir();
    var C = {
      root: root, vivo: true, info: null, vista: null, enviando: false, req: null, reqTexto: "", abortador: null, viaVoz: false, informeAbierto: false,
      vozOn: lsGet("mqp_fy_voz", "1") === "1", velocidad: parseFloat(lsGet("mqp_fy_vel", "1")) || 1, ultimoLeido: 0, pausado: false, confirmaFin: false, sync: null
    };
    var maq = Est.crear(function () { pintarControles(); });
    var escucha = null, habla = null, ta = null, el = {};

    function destruir() {
      if (!C.vivo) return;
      C.vivo = false; if (C.abortador) { try { C.abortador.abort(); } catch (e) {} }
      if (escucha) escucha.cancelar(); if (habla) habla.detener();
      window.removeEventListener("hashchange", alNavegar); window.removeEventListener("pagehide", destruir);
      if (C.sync) clearTimeout(C.sync);
      document.body.classList.remove("fy-activo");
      if (activo === ctl) activo = null;
    }
    function alNavegar() { if (!opts.modal && !document.body.contains(root)) destruir(); if (opts.modal && opts.alNavegar) opts.alNavegar(); }
    window.addEventListener("hashchange", alNavegar); window.addEventListener("pagehide", destruir);
    var ctl = { destruir: destruir, sesionId: function () { return C.vista && C.vista.sesion.id; } };
    activo = ctl;
    if (!opts.modal) document.body.classList.add("fy-activo");      // en móvil oculta el botón flotante del chat del sitio, que taparía el compositor

    function ocupado(msg) { root.innerHTML = '<div class="fy fy--carga" role="status" aria-live="polite"><span class="fy-spin" aria-hidden="true"></span><p>' + esc(msg) + "</p></div>"; }
    function falla(r, volver) {
      root.innerHTML = '<div class="fy fy--carga"><div class="fy-aviso fy-aviso--mal" role="alert"><p>' + textoError(r) + "</p></div>" +
        '<div class="fy-fila">' + (volver ? '<button type="button" class="btn btn--ghost btn--sm" data-a="inicio">Volver al Tutor Feynman</button>' : "") + (opts.modal ? '<button type="button" class="btn btn--ghost btn--sm" data-a="cerrar">Cerrar</button>' : "") + "</div></div>";
      root.querySelectorAll("[data-a]").forEach(function (b) { b.addEventListener("click", function () { if (b.getAttribute("data-a") === "cerrar") { if (opts.onCerrar) opts.onCerrar(); } else inicio(); }); });
    }

    /* ================= INICIO (elegir tema, retomar) ================= */
    function inicio() {
      if (!C.vivo) return;
      if (escucha) escucha.cancelar(); if (habla) habla.detener();
      C.vista = null; ocupado("Cargando el Tutor Feynman IA…");
      Promise.all([api("estado"), api("listar")]).then(function (rs) {
        if (!C.vivo) return;
        C.info = rs[0].j; var sesiones = rs[1].ok ? rs[1].j.sesiones : null, sinSesion = rs[1].http === 401 || rs[1].http === 402;
        var iaLista = C.info && C.info.ia_lista;
        root.innerHTML = '<div class="fy fy--inicio">' +
          '<header class="fy-hero"><p class="fy-eyebrow">Tutor Feynman IA</p><h2 class="fy-titulo">Explica. Comprende. Corrige. Domina.</h2>' +
          '<p class="fy-lead">Aprende medicina explicando los conceptos con tus propias palabras. Tu tutor de IA detectará los vacíos de conocimiento, te hará preguntas y te ayudará a comprender los mecanismos clínicos, no solamente a memorizar respuestas.</p>' +
          (opts.modal ? '<button type="button" class="fy-x" data-a="cerrar" aria-label="Cerrar">' + ico("cerrar") + "</button>" : "") + "</header>" +
          (sinSesion ? '<div class="fy-aviso" role="status"><p>' + textoError(rs[1]) + "</p></div>" : "") +
          (iaLista ? "" : '<div class="fy-aviso fy-aviso--mal" role="status"><p><strong>El tutor de IA todavía no está configurado en este servidor.</strong> Puedes ver tus sesiones anteriores, pero no iniciar nuevas hasta que el administrador configure la llave del proveedor (AI_API_KEY).</p></div>') +
          '<form class="fy-nueva" id="fyNueva"><h3>Elige qué quieres dominar</h3>' +
          '<label for="fyTema">Tema o concepto</label><input id="fyTema" type="text" maxlength="120" required minlength="3" placeholder="Ej.: cetoacidosis diabética, preeclampsia severa, shock séptico…" autocomplete="off">' +
          '<label for="fyEsp">Especialidad (opcional)</label><select id="fyEsp"><option value="">Sin especificar</option>' +
          ((C.info && C.info.especialidades) || []).map(function (e) { return '<option value="' + esc(e.nombre) + '">' + esc(e.nombre) + "</option>"; }).join("") + "</select>" +
          '<button class="btn btn--primary" type="submit"' + (iaLista && !sinSesion ? "" : " disabled") + ">Comenzar sesión</button></form>" +
          '<p class="fy-nota">Tip: también puedes empezar desde cualquier pregunta del banco con <strong>«Aprender con Feynman»</strong>, o desde el visor de «Ver flujograma».</p>' +
          (sesiones && sesiones.length ? '<section class="fy-lista" aria-labelledby="fyLs"><h3 id="fyLs">Tus sesiones</h3><ul>' + sesiones.map(function (s) {
            var est = { activa: "En curso", completada: "Completada", incompleta: "Incompleta" }[s.estado] || s.estado;
            return '<li class="fy-sesion"><div><strong>' + esc(s.tema) + '</strong><span class="fy-meta">' + esc(est) + " · Fase " + s.fase + " (" + esc(s.fase_nombre) + ")" + (s.especialidad ? " · " + esc(s.especialidad) : "") + " · " + fecha(s.actualizado) + '</span></div>' +
              '<div class="fy-fila"><button type="button" class="btn btn--ghost btn--sm" data-abrir="' + esc(s.id) + '">' + (s.estado === "activa" ? "Continuar" : "Ver informe") + '</button>' +
              '<button type="button" class="btn btn--ghost btn--sm fy-peligro" data-borrar="' + esc(s.id) + '" aria-label="Borrar la sesión «' + esc(s.tema) + '»">Borrar</button></div></li>';
          }).join("") + "</ul></section>" : "") + privacidadHTML() + "</div>";
        var f = root.querySelector("#fyNueva");
        f.addEventListener("submit", function (ev) {
          ev.preventDefault();
          empezar({ origen: "tema", tema: root.querySelector("#fyTema").value, especialidad: root.querySelector("#fyEsp").value });
        });
        root.querySelectorAll("[data-abrir]").forEach(function (b) { b.addEventListener("click", function () { abrirSesion(b.getAttribute("data-abrir")); }); });
        root.querySelectorAll("[data-borrar]").forEach(function (b) { b.addEventListener("click", function () {
          if (b.getAttribute("data-seguro") !== "1") { b.setAttribute("data-seguro", "1"); b.textContent = "¿Seguro? Pulsa de nuevo"; return; }
          b.disabled = true; api("borrar", { id: b.getAttribute("data-borrar") }).then(function () { inicio(); });
        }); });
        var x = root.querySelector("[data-a=cerrar]"); if (x) x.addEventListener("click", function () { if (opts.onCerrar) opts.onCerrar(); });
      });
    }
    function privacidadHTML() {
      var prov = C.info && C.info.proveedor ? { gemini: "Google Gemini", openai: "OpenAI", anthropic: "Anthropic" }[C.info.proveedor] || C.info.proveedor : "un proveedor de IA";
      return '<details class="fy-priv"><summary>Privacidad, voz y fuentes</summary><ul>' +
        "<li>Lo que escribes o dictas se envía a <strong>" + esc(prov) + "</strong> (proveedor externo de IA) para analizarlo. No enviamos tu nombre ni tu correo.</li>" +
        "<li><strong>No guardamos audio.</strong> El dictado usa el reconocimiento de voz de tu navegador; en Chrome y Edge, el audio lo procesa el servicio de voz de Google o Microsoft. Revisas el texto antes de enviarlo.</li>" +
        "<li>Guardamos solo el texto de tus sesiones, y solo tú puedes verlas. Puedes borrarlas cuando quieras; se eliminan también al borrar tu cuenta.</li>" +
        "<li>" + ((C.info && C.info.guias > 0) ? "Hay " + C.info.guias + " guía(s) oficial(es) cargada(s): cuando el tutor las usa, las cita con institución, año y página." : "Todavía <strong>no hay guías oficiales (MINSA ni internacionales) cargadas</strong>: el tutor se apoya en el comentario del banco y en conocimiento general que <strong>no está verificado</strong>. Contrasta lo importante con tus fuentes.") + "</li>" +
        "<li>Es una herramienta de estudio. No sustituye el juicio clínico y no debe usarse para decidir sobre pacientes reales.</li></ul></details>";
    }

    /* ================= CREAR / ABRIR SESIÓN ================= */
    function conInfo(f) { if (C.info) return f(); api("estado").then(function (r) { C.info = r.j || null; if (C.vivo) f(); }); }
    function empezar(ctx, nueva) {
      ocupado("Preparando tu sesión… el tutor está eligiendo el concepto y los criterios de evaluación.");
      conInfo(function () { api("crear", Object.assign({}, ctx, nueva ? { nueva: true } : {})).then(function (r) {
        if (!C.vivo) return;
        if (!r.ok) { falla(r, true); return; }
        C.vista = r.j; C.ultimoLeido = 0;
        if (!opts.modal) { try { history.replaceState(null, "", "#/feynman?s=" + r.j.sesion.id); } catch (e) {} }
        armarSesion(!r.j.retomada);
      }); });
    }
    function abrirSesion(id) {
      ocupado("Abriendo tu sesión…");
      conInfo(function () { api("ver&id=" + encodeURIComponent(id)).then(function (r) {
        if (!C.vivo) return;
        if (!r.ok) { falla(r, true); return; }
        C.vista = r.j; C.ultimoLeido = 0;
        if (!opts.modal) { try { history.replaceState(null, "", "#/feynman?s=" + id); } catch (e) {} }
        armarSesion(false);
      }); });
    }

    /* ================= PANTALLA DE SESIÓN ================= */
    function armarSesion(leerPrimero) {
      if (escucha) escucha.cancelar(); if (habla) habla.detener();
      var soporteMic = Voz.soporteEscucha(window), soporteVoz = Voz.soporteHabla(window);
      root.innerHTML = '<div class="fy fy--sesion' + (opts.modal ? "" : " fy--pagina") + '">' +
        '<header class="fy-head"><div class="fy-head__t"><p class="fy-eyebrow">Tutor Feynman IA · <span id="fyOrigen"></span></p><h2 class="fy-titulo" id="fyTitulo"></h2><p class="fy-obj" id="fyObj"></p></div>' +
        '<div class="fy-head__a"><button type="button" class="btn btn--ghost btn--sm" id="fyFin">Finalizar sesión</button>' +
        (opts.modal ? '<button type="button" class="fy-x" id="fyCerrar" aria-label="Cerrar el tutor">' + ico("cerrar") + "</button>" : '<button type="button" class="btn btn--ghost btn--sm" id="fyInicio">Mis sesiones</button>') + "</div></header>" +
        '<div class="fy-prog"><ol class="fy-fases" id="fyFases" aria-label="Fases del método Feynman"></ol><div class="fy-barra" role="progressbar" aria-valuemin="0" aria-valuemax="5" id="fyBarra" aria-label="Progreso de la sesión"><span id="fyBarraRel"></span></div><p class="fy-prog__t" id="fyProgT"></p></div>' +
        '<div id="fyConfirma" class="fy-aviso" role="alertdialog" aria-labelledby="fyConfT" hidden></div>' +
        '<div class="fy-cuerpo"><div class="fy-col">' +
        '<div id="fyInforme"></div>' +
        '<div class="fy-chat" id="fyChat" role="log" aria-live="polite" aria-relevant="additions" aria-label="Conversación con el tutor" tabindex="0"></div>' +
        '<div class="fy-estado" id="fyEstado" role="status" aria-live="polite"><span class="fy-ind" aria-hidden="true"><i></i><i></i><i></i></span><span id="fyEstadoT"></span></div>' +
        '<div class="fy-aviso fy-aviso--mal" id="fyAviso" role="alert" hidden></div>' +
        '<form class="fy-comp" id="fyForm" novalidate><label class="sr-only" for="fyTa">Tu explicación con tus propias palabras</label>' +
        '<textarea id="fyTa" rows="2" maxlength="1500" placeholder="Explícalo con tus propias palabras, como a un estudiante que recién empieza…" enterkeyhint="send"></textarea>' +
        '<p class="fy-interino" id="fyInterino" aria-hidden="true"></p><p class="fy-nota" id="fyNotaVoz" hidden>Revisa la transcripción: el dictado puede equivocarse con términos médicos. Corrige lo que haga falta y envía.</p>' +
        '<div class="fy-acciones"><div class="fy-fila">' +
        '<button type="button" class="btn btn--ghost fy-mic" id="fyMic" aria-pressed="false">' + ico("mic") + '<span id="fyMicT">Hablar</span></button>' +
        '<button type="button" class="btn btn--ghost btn--sm" id="fyCancelaMic" hidden>Cancelar</button>' +
        '<button type="button" class="btn btn--ghost btn--sm" id="fyCancelaEnvio" hidden>Cancelar envío</button></div>' +
        '<div class="fy-fila fy-fila--der"><button type="button" class="btn btn--ghost btn--sm" id="fyPista">' + ico("pista") + 'Pista</button>' +
        '<button type="button" class="btn btn--ghost btn--sm" id="fyExplica">' + ico("libro") + 'Pedir explicación</button>' +
        '<button type="submit" class="btn btn--primary" id="fyEnviar">' + ico("enviar") + 'Enviar</button></div></div>' +
        (soporteMic ? "" : '<p class="fy-nota">Tu navegador no permite dictar por voz: escribe tu respuesta. Todo lo demás funciona igual.</p>') + "</form>" +
        '<div class="fy-voz" id="fyVoz" role="group" aria-label="Voz del tutor">' + (soporteVoz ?
          '<button type="button" class="chip" id="fyVozOn" aria-pressed="' + C.vozOn + '">' + ico(C.vozOn ? "voz" : "vozoff") + "<span>Voz del tutor</span></button>" +
          '<button type="button" class="chip" id="fyPausa" hidden>' + ico("pausa") + "<span>Pausar</span></button>" +
          '<button type="button" class="chip" id="fyParar" hidden>' + ico("stop") + "<span>Detener</span></button>" +
          '<label class="fy-vel">Velocidad <select id="fyVel"><option value="0.8">Lenta</option><option value="1">Normal</option><option value="1.2">Rápida</option><option value="1.4">Muy rápida</option></select></label>'
          : '<p class="fy-nota">Tu navegador no puede leer en voz alta: puedes leer las respuestas en pantalla.</p>') + "</div></div>" +
        '<aside class="fy-lado"><details class="fy-panel" id="fyPanel" open><summary>Tu aprendizaje</summary><div id="fyPanelC"></div></details>' +
        '<details class="fy-panel" id="fyFuentes"><summary>Fuentes de referencia</summary><div id="fyFuentesC"></div></details>' + privacidadHTML() + "</aside></div></div>";
      ["Origen", "Titulo", "Obj", "Fases", "Barra", "BarraRel", "ProgT", "Confirma", "Informe", "Chat", "Estado", "EstadoT", "Aviso", "Form", "Ta", "Interino", "NotaVoz", "Mic", "MicT", "CancelaMic", "CancelaEnvio", "Pista", "Explica", "Enviar", "Fin", "Panel", "PanelC", "FuentesC", "VozOn", "Pausa", "Parar", "Vel", "Cerrar", "Inicio"].forEach(function (k) { el[k] = root.querySelector("#fy" + k); });
      ta = el.Ta; if (el.Vel) el.Vel.value = String(C.velocidad);
      if (window.matchMedia && !window.matchMedia("(min-width: 960px)").matches) el.Panel.removeAttribute("open");
      ligarVoz(); ligarEventos();
      var v = C.vista.sesion; maq = Est.crear(function () { pintarControles(); });
      if (v.estado !== "activa") maq.ir("completada");
      actualizar();
      var ult = C.vista.turnos[C.vista.turnos.length - 1];
      if (leerPrimero && C.vozOn && habla && habla.disponible() && v.estado === "activa" && ult && ult.rol === "tutor") leer(ult);
      else if (v.estado === "activa" && leerPrimero) maq.ir("esperando");      // sesión nueva: el tutor ya preguntó; sesión retomada: queda «preparado para escuchar»
      pintarControles();
      if (ta && v.estado === "activa") ta.focus({ preventScroll: true });
    }

    function ligarVoz() {
      habla = Voz.crearHabla(window, { velocidad: C.velocidad, onEstado: function (e, d) {
        if (!C.vivo) return;
        if (e === "hablando") { C.pausado = false; if (maq.estado() !== "reproduciendo") maq.ir("reproduciendo"); else pintarControles(); }
        else if (e === "pausado") { C.pausado = true; pintarControles(); }
        else if (e === "fin" || e === "detenido") { C.pausado = false; reposo(); }
        else if (e === "error") { C.pausado = false; reposo(); avisar("No se pudo reproducir la voz del tutor" + (d === "no_inicio" ? " (el navegador no la inició)" : "") + ". Puedes leer la respuesta en pantalla o pulsar «Escuchar» de nuevo."); }
      } });
      escucha = Voz.crearEscucha(window, {
        onEstado: function (e) { if (e === "escuchando") { maq.ir("escuchando"); } },
        onTexto: function (t) { if (el.Interino) el.Interino.textContent = t.interino ? "…" + t.interino : ""; },
        onFin: function (txt, info) {
          if (el.Interino) el.Interino.textContent = "";
          if (!maq.ir("esperando")) maq.ir("error");
          if (txt) { ta.value = (ta.value.trim() ? ta.value.trim() + " " : "") + txt; C.viaVoz = true; el.NotaVoz.hidden = false; ta.focus(); aviso(null);
            if (info && info.confianza < 0.6) avisar("La transcripción tiene baja confianza. Revísala con cuidado antes de enviar.", true); }
          else avisar(Voz.MENSAJES.sin_voz);
          pintarControles();
        },
        onCancelado: function () { if (el.Interino) el.Interino.textContent = ""; maq.ir("esperando"); pintarControles(); },
        onError: function (x) { if (el.Interino) el.Interino.textContent = ""; maq.ir("error", x); avisar(x.mensaje); pintarControles(); }
      });
    }
    function reposo() { if (!C.vivo) return; var s = C.vista && C.vista.sesion.estado; if (maq.estado() === "reproduciendo" || maq.estado() === "error") maq.ir(s && s !== "activa" ? "completada" : "esperando"); pintarControles(); }
    function leer(turno) {
      if (!habla || !habla.disponible()) return;
      if (escucha && escucha.activo()) return;           // nunca se lee mientras el micrófono está abierto
      if (maq.estado() === "analizando" || maq.estado() === "procesando_audio") return;
      if (maq.estado() === "error" || maq.estado() === "listo") maq.ir("esperando");
      habla.velocidad(C.velocidad); C.ultimoLeido = turno.n; aviso(null);
      habla.hablar(turno.texto);
    }

    function ligarEventos() {
      el.Form.addEventListener("submit", function (ev) { ev.preventDefault(); enviar("responder"); });
      ta.addEventListener("keydown", function (ev) { if (ev.key === "Enter" && !ev.shiftKey && !ev.isComposing && window.matchMedia && window.matchMedia("(pointer: fine)").matches) { ev.preventDefault(); enviar("responder"); } });
      ta.addEventListener("input", function () { pintarControles(); });
      el.Pista.addEventListener("click", function () { enviar("pista"); });
      el.Explica.addEventListener("click", function () { enviar("explicacion"); });
      el.CancelaEnvio.addEventListener("click", cancelarEnvio);
      el.Mic.addEventListener("click", function () {
        if (maq.estado() === "escuchando") { maq.ir("procesando_audio"); escucha.detener(); return; }       // segundo clic = detener
        if (habla) habla.detener();                                                                         // la voz del tutor se corta antes de abrir el micrófono
        if (maq.estado() === "reproduciendo") maq.ir("esperando");
        if (!maq.puedeEscuchar() || C.enviando) return;
        aviso(null); escucha.iniciar();
      });
      el.CancelaMic.addEventListener("click", function () { escucha.cancelar(); });
      el.Fin.addEventListener("click", pedirFin);
      if (el.Cerrar) el.Cerrar.addEventListener("click", function () { if (opts.onCerrar) opts.onCerrar(); });
      if (el.Inicio) el.Inicio.addEventListener("click", function () { try { history.replaceState(null, "", "#/feynman"); } catch (e) {} inicio(); });
      if (el.VozOn) el.VozOn.addEventListener("click", function () {
        C.vozOn = !C.vozOn; lsSet("mqp_fy_voz", C.vozOn ? "1" : "0"); el.VozOn.setAttribute("aria-pressed", String(C.vozOn)); el.VozOn.firstChild.outerHTML = ico(C.vozOn ? "voz" : "vozoff");
        if (!C.vozOn && habla) habla.detener();
      });
      if (el.Pausa) el.Pausa.addEventListener("click", function () { if (C.pausado) habla.reanudar(); else habla.pausar(); });
      if (el.Parar) el.Parar.addEventListener("click", function () { habla.detener(); });
      if (el.Vel) el.Vel.addEventListener("change", function () { C.velocidad = parseFloat(el.Vel.value) || 1; lsSet("mqp_fy_vel", String(C.velocidad)); habla.velocidad(C.velocidad); });
      el.Chat.addEventListener("click", function (ev) {
        var b = ev.target.closest && ev.target.closest("[data-escuchar]"); if (!b) return;
        var t = C.vista.turnos.filter(function (x) { return x.n === parseInt(b.getAttribute("data-escuchar"), 10); })[0];
        if (!t) return; if (maq.estado() === "escuchando") escucha.cancelar();
        if (maq.estado() === "reproduciendo" && C.ultimoLeido === t.n) { habla.detener(); return; }       // segundo clic en el mismo mensaje = detener
        if (maq.estado() === "reproduciendo") habla.detener();
        leer(t);
      });
    }

    /* msg es texto plano (se escapa); html:true solo para los enlaces fijos de textoError() */
    function avisar(msg, suave, html) { if (!el.Aviso) return; el.Aviso.hidden = false; el.Aviso.className = "fy-aviso" + (suave ? "" : " fy-aviso--mal"); el.Aviso.innerHTML = "<p>" + (html ? msg : esc(msg)) + "</p>"; }
    function aviso(msg) { if (!el.Aviso) return; if (msg) avisar(msg); else { el.Aviso.hidden = true; el.Aviso.innerHTML = ""; } }

    /* ---------- envío ---------- */
    function enviar(accion) {
      if (C.enviando || !C.vista || C.vista.sesion.estado !== "activa") return;
      var texto = ta.value.trim();
      if (accion === "responder" && texto.length < 2) { avisar("Escribe o dicta tu explicación antes de enviar.", true); ta.focus(); return; }
      if (maq.estado() === "escuchando" || maq.estado() === "procesando_audio") { avisar("Termina o cancela el dictado antes de enviar.", true); return; }
      if (habla) habla.detener();
      if (maq.estado() === "reproduciendo") maq.ir("esperando");
      if (!maq.ir("analizando")) return;
      C.enviando = true; aviso(null);
      var firma = accion + "|" + texto;
      if (!C.req || C.reqTexto !== firma) { C.req = nuevoId(); C.reqTexto = firma; }          // reintentar el mismo envío reutiliza el id (el servidor no lo procesa dos veces)
      C.abortador = typeof AbortController === "function" ? new AbortController() : null;
      pintarPendiente(accion, texto); pintarControles();
      api("turno", { id: C.vista.sesion.id, req_id: C.req, accion: accion, texto: texto, via: C.viaVoz ? "voz" : "texto" }, { senal: C.abortador && C.abortador.signal }).then(function (r) {
        if (!C.vivo) return;
        C.enviando = false; C.abortador = null;
        if (r.abortado) { sincronizar(0); return; }
        if (r.ok) {
          C.vista = r.j; C.req = null; ta.value = ""; C.viaVoz = false; el.NotaVoz.hidden = true;
          actualizar(); var ult = r.j.turnos[r.j.turnos.length - 1];
          if (C.vozOn && habla && habla.disponible() && ult && ult.rol === "tutor") { maq.ir("esperando"); leer(ult); } else maq.ir("esperando");
        } else {
          maq.ir("error"); actualizar();
          avisar(textoError(r) + (r.http === 0 || r.http >= 500 ? " Pulsa Enviar para reintentar." : ""), false, true);
        }
        pintarControles(); ta.focus({ preventScroll: true });
      });
    }
    /* cancelar un envío en curso: el servidor puede haberlo terminado igual, así que se vuelve a consultar la sesión */
    function cancelarEnvio() { if (C.abortador) C.abortador.abort(); }
    function sincronizar(n) {
      avisar("Cancelaste la espera. Comprobando si el tutor alcanzó a responder…", true);
      C.sync = setTimeout(function () {
        if (!C.vivo) return;
        api("ver&id=" + encodeURIComponent(C.vista.sesion.id)).then(function (r) {
          if (!C.vivo) return;
          if (r.ok && r.j.turnos.length > C.vista.turnos.length) { C.vista = r.j; C.req = null; ta.value = ""; actualizar(); maq.ir("esperando"); aviso(null); }
          else if (n < 2) sincronizar(n + 1);
          else { maq.ir("esperando"); avisar("Cancelado. Tu texto sigue en el cuadro: puedes enviarlo de nuevo.", true); }
          pintarControles();
        });
      }, n === 0 ? 2500 : 5000);
      maq.ir("esperando"); pintarControles();
    }

    /* ---------- finalizar ---------- */
    function pedirFin() {
      var v = C.vista.sesion; if (v.estado !== "activa") return;
      if (v.puede_finalizar) { finalizar(); return; }
      el.Confirma.hidden = false;
      el.Confirma.innerHTML = '<p id="fyConfT"><strong>Todavía no completaste las cinco fases.</strong> Si terminas ahora, el informe marcará como pendiente lo que no se evaluó y no lo contará como aprendido. Podrás retomar la sesión después.</p><div class="fy-fila"><button type="button" class="btn btn--primary btn--sm" id="fyConfSi">Terminar y ver informe</button><button type="button" class="btn btn--ghost btn--sm" id="fyConfNo">Seguir en la sesión</button></div>';
      el.Confirma.querySelector("#fyConfSi").addEventListener("click", function () { el.Confirma.hidden = true; finalizar(); });
      el.Confirma.querySelector("#fyConfNo").addEventListener("click", function () { el.Confirma.hidden = true; el.Fin.focus(); });
      el.Confirma.querySelector("#fyConfSi").focus();
    }
    function finalizar() {
      if (C.enviando) return;
      if (habla) habla.detener(); if (escucha) escucha.cancelar();
      if (maq.estado() === "reproduciendo") maq.ir("esperando");
      if (!maq.ir("analizando")) return;
      C.enviando = true; aviso(null); pintarControles(); el.EstadoT.textContent = "Preparando tu informe de aprendizaje…";
      api("finalizar", { id: C.vista.sesion.id }).then(function (r) {
        if (!C.vivo) return; C.enviando = false;
        if (r.ok) { C.vista = r.j; maq.ir("completada"); actualizar(); } else { maq.ir("error"); avisar(textoError(r), false, true); }
        pintarControles();
      });
    }

    /* ---------- pintar ---------- */
    function titulosNivel(n) { var r = C.vista && C.vista.rubrica; return n && r && r[n] ? "Nivel " + n + " · " + r[n].titulo : "Sin evaluar"; }
    function actualizar() {
      var v = C.vista, s = v.sesion;
      el.Origen.textContent = { pregunta: "desde una pregunta del banco", flujograma: "desde un flujograma", tema: "tema libre" }[s.origen] || "";
      el.Titulo.textContent = s.tema; el.Obj.textContent = s.objetivo ? "Objetivo: " + s.objetivo : "";
      var fases = s.fases, hecho = s.estado === "completada" ? 5 : s.fase - 1;
      el.Fases.innerHTML = Object.keys(fases).map(function (k) { k = +k; var estado = s.estado === "completada" || k < s.fase || (k === 2 && s.fase >= 3) ? "hecha" : (k === s.fase ? "actual" : "pend");
        return '<li class="fy-fase fy-fase--' + estado + '"' + (estado === "actual" ? ' aria-current="step"' : "") + '><span class="fy-fase__n" aria-hidden="true">' + k + '</span><span class="fy-fase__t">' + esc(fases[k]) + (estado === "hecha" ? '<span class="sr-only"> (completada)</span>' : "") + "</span></li>"; }).join("");
      el.Barra.setAttribute("aria-valuenow", String(hecho)); el.BarraRel.style.width = (hecho / 5 * 100) + "%";
      el.ProgT.textContent = s.estado === "activa" ? "Fase " + s.fase + " de 5 · " + s.fase_nombre : (s.estado === "completada" ? "Sesión completada" : "Sesión terminada antes de completarse");
      el.Chat.innerHTML = v.turnos.map(turnoHTML).join("");
      el.Chat.classList.toggle("fy-chat--lectura", s.estado !== "activa");
      el.Informe.innerHTML = s.estado !== "activa" ? informeHTML(v) : "";
      el.Chat.setAttribute("aria-label", s.estado !== "activa" ? "Conversación de la sesión (solo lectura)" : "Conversación con el tutor");
      el.Chat.scrollTop = s.estado === "activa" ? el.Chat.scrollHeight : 0;
      if (s.estado !== "activa" && el.Informe.scrollIntoView && !C.informeVisto) { C.informeVisto = true; el.Informe.scrollIntoView({ block: "start" }); }
      el.PanelC.innerHTML = panelHTML(v);
      el.FuentesC.innerHTML = fuentesHTML(v);
      if (s.estado !== "activa") ligarInforme();
      pintarControles();
    }
    function turnoHTML(t) {
      if (t.rol === "tutor") {
        return '<article class="fy-msg fy-msg--tutor" data-n="' + t.n + '"><header><span class="fy-quien">Tutor</span><span class="fy-fasechip">Fase ' + t.fase + "</span></header><div class=\"fy-txt\">" + md(t.texto) + "</div>" +
          (t.aclaracion ? '<p class="fy-nota">El tutor necesita aclarar un término de tu dictado; no cuenta como error ni como intento.</p>' : "") +
          (t.guias && t.guias.length ? '<details class="fy-guias"><summary>Guías consultadas (' + t.guias.length + (t.citadas.length ? ", citadas: " + t.citadas.length : ", ninguna citada") + ")</summary><ul>" + t.guias.map(function (g) {
            return "<li><strong>[" + g.n + "] " + esc(g.titulo) + "</strong><br>" + esc(g.institucion) + " · " + esc(g.pais) + " · " + esc(g.anio) + (g.version ? " · " + esc(g.version) : "") + " · p. " + esc(g.pagina) + (g.aviso ? '<br><em class="fy-mal">⚠ ' + esc(g.aviso) + "</em>" : "") +
              "<blockquote>" + esc(g.extracto) + "</blockquote>" + (g.url ? '<a href="' + esc(g.url) + '" target="_blank" rel="noopener noreferrer">Abrir el documento</a>' : "") + "</li>"; }).join("") + "</ul></details>" : "") +
          (habla && habla.disponible() ? '<footer><button type="button" class="fy-link" data-escuchar="' + t.n + '">' + ico("voz") + " Escuchar</button></footer>" : "") + "</article>";
      }
      return '<article class="fy-msg fy-msg--yo" data-n="' + t.n + '"><header><span class="fy-quien">Tú</span>' + (t.via === "voz" ? '<span class="fy-fasechip">dictado</span>' : "") + "</header><div class=\"fy-txt\">" + md(t.texto) + "</div>" +
        (t.nivel ? '<p class="fy-eval">Evaluación provisional: <strong>' + esc(titulosNivel(t.nivel)) + "</strong></p>" : "") + "</article>";
    }
    function pintarPendiente(accion, texto) {
      var d = document.createElement("article"); d.className = "fy-msg fy-msg--yo fy-msg--pend"; d.id = "fyPend";
      d.innerHTML = '<header><span class="fy-quien">Tú</span><span class="fy-fasechip">enviando…</span></header><div class="fy-txt">' + (accion === "responder" ? md(texto) : "<p>" + (accion === "pista" ? "(pediste una pista)" : "(pediste la explicación directa)") + "</p>") + "</div>";
      el.Chat.appendChild(d); el.Chat.scrollTop = el.Chat.scrollHeight;
    }
    function panelHTML(v) {
      var p = v.panel, s = v.sesion, li = function (a, vacio) { return a.length ? "<ul>" + a.map(function (x) { return "<li>" + x + "</li>"; }).join("") + "</ul>" : '<p class="fy-nota">' + vacio + "</p>"; };
      var estT = { cumplido: "Cumplido", parcial: "Parcial", ausente: "Ausente", no_evaluado: "Sin evaluar" };
      return '<h4>Lo que ya explicaste bien</h4>' + li(p.conceptos_correctos.map(esc), "Todavía no hay conceptos confirmados.") +
        "<h4>Vacíos de conocimiento detectados</h4>" + li(p.errores.map(function (e) { return esc(e.descripcion) + ' <span class="fy-tag fy-tag--' + e.estado + '">' + (e.estado === "abierto" ? "por corregir" : "corregido") + "</span>"; }).concat(p.omisiones.map(function (o) { return esc(o) + ' <span class="fy-tag">por completar</span>'; })), "Ninguno detectado por ahora.") +
        "<h4>Criterios del tema</h4>" + li(p.criterios.map(function (c) { return esc(c.descripcion) + ' <span class="fy-tag fy-tag--c-' + c.estado + '">' + estT[c.estado] + "</span>"; }), "Sin criterios.") +
        "<h4>Evaluación</h4><p>Última: <strong>" + esc(titulosNivel(p.nivel_actual)) + "</strong></p><p class=\"fy-nota\">Intentos socráticos: " + p.intentos.socratico + " · Reconstrucciones: " + p.intentos.reconstruccion + " · Aplicaciones: " + p.intentos.transferencia + "</p>" +
        "<h4>Aplicación clínica</h4><p>" + (p.aplicacion.presentada ? (p.aplicacion.nivel ? "Resultado: <strong>" + esc(titulosNivel(p.aplicacion.nivel)) + "</strong>" : "Caso presentado; falta tu respuesta.") : "Se presentará al final de la sesión.") + "</p>" +
        "<h4>Próximo objetivo</h4><p>" + esc(p.siguiente_objetivo) + "</p>" + (s.estado === "activa" ? '<p class="fy-nota">Intervenciones disponibles: ' + s.intervenciones_restantes + "</p>" : "");
    }
    function fuentesHTML(v) {
      var vistos = {}, lista = [];
      v.turnos.forEach(function (t) { (t.guias || []).forEach(function (g) { if (!vistos[g.id]) { vistos[g.id] = 1; lista.push(g); } }); });
      var base = v.sesion.pregunta_id ? "<p>Material de referencia: comentario docente del banco para la pregunta <strong>" + esc(v.sesion.pregunta_id) + "</strong> (sin modificar).</p>" : "";
      return base + (lista.length ? "<ul>" + lista.map(function (g) { return "<li><strong>" + esc(g.titulo) + "</strong><br>" + esc(g.institucion) + " · " + esc(g.anio) + (g.version ? " · " + esc(g.version) : "") + " · p. " + esc(g.pagina) + (g.url ? ' · <a href="' + esc(g.url) + '" target="_blank" rel="noopener noreferrer">documento</a>' : "") + "</li>"; }).join("") + "</ul>"
        : '<p class="fy-nota">Ninguna guía oficial citada en esta sesión. Lo que explica el tutor fuera del material del banco es conocimiento general <strong>no verificado</strong>: contrástalo con tus fuentes.</p>');
    }

    /* ---------- informe ---------- */
    function informeHTML(v) {
      var i = v.informe, s = v.sesion, lista = function (a, vacio, f) { return a && a.length ? "<ul>" + a.map(function (x) { return "<li>" + (f ? f(x) : esc(x)) + "</li>"; }).join("") + "</ul>" : '<p class="fy-nota">' + vacio + "</p>"; };
      var propuestas = (i.tarjetas || []).filter(function (t) { return t.estado === "propuesta"; }).length;
      return '<section class="fy-informe" aria-labelledby="fyInfT"><h3 id="fyInfT">Informe de aprendizaje</h3>' +
        (i.aviso ? '<div class="fy-aviso"><p>' + esc(i.aviso) + "</p></div>" : "") +
        '<p class="fy-dominio fy-dominio--' + i.dominio + '">' + esc({ dominado: "Concepto dominado", parcial: "Dominio parcial", no_demostrado: "Dominio aún no demostrado" }[i.dominio]) + " — " + esc(i.dominio_texto) + "</p>" +
        (i.resumen ? "<p>" + esc(i.resumen) + "</p>" : "") +
        "<h4>A. Lo que comprendiste</h4>" + lista(i.comprendido, "Aún no se confirmó ningún concepto explicado con tus palabras.") +
        "<h4>B. Errores corregidos</h4>" + lista(i.errores_corregidos, "No hubo errores corregidos.", function (e) { return esc(e.descripcion) + (e.correccion ? "<br><em>Corrección: " + esc(e.correccion) + "</em>" : ""); }) +
        "<h4>C. Conceptos pendientes</h4>" + lista(i.pendientes, "No quedaron pendientes registrados.") +
        "<h4>D. Aplicación clínica</h4>" + (i.aplicacion.realizada ? "<p>Resultado: <strong>" + esc(i.aplicacion.valoracion || "sin evaluar") + "</strong> (" + i.aplicacion.intentos + " intento(s)).</p>" + (i.aplicacion.razonamiento ? "<p>" + esc(i.aplicacion.razonamiento) + "</p>" : "") : "<p class=\"fy-nota\">No llegaste a resolver el caso de aplicación: no se puede afirmar que transfieras el concepto.</p>") +
        "<p class=\"fy-nota\">Niveles: explicación inicial " + esc(i.niveles.titulos.inicial || "sin evaluar") + " · reconstrucción " + esc(i.niveles.titulos.reconstruccion || "sin evaluar") + " · aplicación " + esc(i.niveles.titulos.transferencia || "sin evaluar") + ". Ayudas: " + i.ayudas.pistas + " pista(s), " + i.ayudas.explicaciones_directas + " explicación(es) directa(s).</p>" +
        (i.proximos_pasos && i.proximos_pasos.length ? "<h4>Sugerencias del tutor</h4>" + lista(i.proximos_pasos, "") : "") +
        "<h4>E. Próximas acciones</h4><div class=\"fy-fila fy-fila--wrap\">" +
        '<button type="button" class="btn btn--ghost btn--sm" data-i="repetir">Repetir la explicación</button>' +
        '<button type="button" class="btn btn--ghost btn--sm" data-i="final"' + (i.explicacion_final ? "" : " disabled") + ">Revisar la explicación final</button>" +
        '<button type="button" class="btn btn--ghost btn--sm" data-i="fuentes">Consultar las fuentes</button>' +
        (s.estado === "completada" ? '<button type="button" class="btn btn--ghost btn--sm" data-i="caso">Practicar con otro caso</button>' : '<button type="button" class="btn btn--ghost btn--sm" data-i="retomar">Retomar la sesión</button>') +
        '<button type="button" class="btn btn--primary btn--sm" data-i="tarjetas"' + (propuestas ? "" : " disabled") + ">Crear tarjetas de repaso" + (propuestas ? " (" + propuestas + ")" : "") + "</button>" +
        '<a class="btn btn--ghost btn--sm" href="#/banco" data-i="banco">Volver al banco ENAM</a></div>' +
        (i.tarjetas.length ? "" : '<p class="fy-nota">No se propusieron tarjetas: ' + (i.resumen ? "no había conceptos pendientes que reforzar o la IA no pudo generarlas." : "el cierre con IA no estuvo disponible.") + "</p>") +
        '<div id="fyInfExtra"></div><p class="fy-nota">Retomar más tarde: esta sesión queda guardada en «Mis sesiones» hasta que la borres.</p></section>';
    }
    function ligarInforme() {
      var ex = el.Informe.querySelector("#fyInfExtra"), v = C.vista, i = v.informe;
      el.Informe.querySelectorAll("[data-i]").forEach(function (b) { b.addEventListener("click", function (ev) {
        var a = b.getAttribute("data-i");
        if (a === "banco") { if (opts.onCerrar) opts.onCerrar(); return; }
        ev.preventDefault();
        if (a === "repetir") { empezar(contextoDe(v.sesion), true); }
        else if (a === "final") { ex.innerHTML = '<div class="fy-extra"><h4>Explicación reconstruida por el tutor</h4>' + md(i.explicacion_final) + '<p class="fy-nota">Es una explicación generada por IA para estudiar; contrástala con tus fuentes.</p></div>'; }
        else if (a === "fuentes") { ex.innerHTML = '<div class="fy-extra"><h4>Fuentes</h4>' + fuentesHTML(v) + "</div>"; }
        else if (a === "retomar") { b.disabled = true; api("reanudar", { id: v.sesion.id }).then(function (r) { if (r.ok) { C.vista = r.j; armarSesion(false); } else { b.disabled = false; avisar(textoError(r), false, true); } }); }
        else if (a === "caso") { b.disabled = true; maq.ir("analizando"); C.enviando = true; pintarControles(); el.EstadoT.textContent = "El tutor está preparando un caso nuevo…";
          api("otro_caso", { id: v.sesion.id, req_id: nuevoId() }).then(function (r) { C.enviando = false; if (r.ok) { C.vista = r.j; maq.ir("esperando"); armarSesion(false); var u = r.j.turnos[r.j.turnos.length - 1]; if (C.vozOn && u) leer(u); } else { maq.ir("completada"); b.disabled = false; avisar(textoError(r), false, true); pintarControles(); } }); }
        else if (a === "tarjetas") { tarjetas(ex); }
      }); });
    }
    function contextoDe(s) { return s.origen === "tema" ? { origen: "tema", tema: s.tema, especialidad: s.especialidad } : { origen: s.origen, pregunta_id: s.pregunta_id, elegida: s.elegida, flujograma: s.flujograma, tema: s.tema }; }

    /* ---------- tarjetas: se revisan, se editan y recién entonces se guardan (nunca solas) ---------- */
    function tarjetas(ex) {
      var v = C.vista, props = v.informe.tarjetas.map(function (t, i) { return { i: i, t: t }; }).filter(function (x) { return x.t.estado === "propuesta"; });
      ex.innerHTML = '<form class="fy-extra fy-tarjetas" id="fyTj"><h4>Revisa tus tarjetas de repaso</h4><p class="fy-nota">Las generó la IA a partir de lo que te costó explicar. <strong>Revisa que sean correctas</strong> antes de guardarlas; puedes editarlas o descartarlas. No se guardará nada que no marques.</p>' +
        props.map(function (x) { return '<fieldset class="fy-tj"><legend><label><input type="checkbox" checked data-i="' + x.i + '"> Guardar esta tarjeta</label></legend>' +
          '<label for="fyTjF' + x.i + '">Frente</label><textarea id="fyTjF' + x.i + '" rows="3" maxlength="600">' + esc(x.t.frente) + '</textarea><label for="fyTjD' + x.i + '">Dorso</label><textarea id="fyTjD' + x.i + '" rows="4" maxlength="1500">' + esc(x.t.dorso) + '</textarea><p class="fy-nota">Fuente: ' + esc(x.t.fuente) + "</p></fieldset>"; }).join("") +
        '<div class="fy-fila"><button class="btn btn--primary btn--sm" type="submit">Guardar las seleccionadas en mis flashcards</button><button class="btn btn--ghost btn--sm" type="button" id="fyTjNo">Cancelar</button></div><p id="fyTjR" role="status" class="fy-nota"></p></form>';
      var f = ex.querySelector("#fyTj"); f.querySelector("#fyTjNo").addEventListener("click", function () { ex.innerHTML = ""; });
      f.addEventListener("submit", function (ev) {
        ev.preventDefault(); var envio = [], dec = [], r = f.querySelector("#fyTjR");
        props.forEach(function (x) { var marcada = f.querySelector('[data-i="' + x.i + '"]').checked;
          if (marcada) envio.push({ frente: f.querySelector("#fyTjF" + x.i).value, dorso: f.querySelector("#fyTjD" + x.i).value, pregunta: v.sesion.pregunta_id, tema: v.sesion.tema, especialidad: v.sesion.especialidad, fuente: x.t.fuente });
          dec.push({ i: x.i, estado: marcada ? "guardada" : "descartada" }); });
        var btn = f.querySelector("[type=submit]"); btn.disabled = true;
        var guardar = envio.length ? fetch(BASE + "cuenta.php?a=fc_crear", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "X-MQP": "1" }, body: JSON.stringify({ tarjetas: envio }) })
          .then(function (res) { return res.json().then(function (j) { return { ok: res.ok && j.ok !== false, j: j }; }); }, function () { return { ok: false, j: { error: "Sin conexión." } }; }) : Promise.resolve({ ok: true, j: { creadas: 0, repetidas: 0 } });
        guardar.then(function (g) {
          if (!g.ok) { btn.disabled = false; r.textContent = (g.j && g.j.error) || "No se pudieron guardar. Inténtalo de nuevo."; return; }
          api("tarjetas", { id: v.sesion.id, decisiones: dec }).then(function (rr) { if (rr.ok) C.vista = rr.j; });
          r.innerHTML = "Listo: " + (g.j.creadas || 0) + " tarjeta(s) guardada(s)" + (g.j.repetidas ? " (" + g.j.repetidas + " ya existían)" : "") + '. <a href="#/flashcards">Ver mis flashcards</a>';
        });
      });
      f.querySelector("textarea").focus();
    }

    /* ---------- controles ---------- */
    function pintarControles() {
      if (!C.vivo || !el.Estado) return;
      var e = maq.estado(), v = C.vista && C.vista.sesion, activa = v && v.estado === "activa", texto = ta ? ta.value.trim() : "";
      el.Estado.setAttribute("data-estado", e);
      if (!(e === "analizando" && C.enviando && /informe|caso nuevo/.test(el.EstadoT.textContent))) el.EstadoT.textContent = Est.ETIQUETAS[e] + (e === "reproduciendo" && C.pausado ? " (en pausa)" : "");
      var escuchando = e === "escuchando", libre = activa && !C.enviando;
      ta.disabled = !activa || e === "analizando" || e === "escuchando" || e === "procesando_audio";
      el.Mic.disabled = !Voz.soporteEscucha(window) || !activa || (!escuchando && (!maq.puedeEscuchar() || C.enviando)) || e === "procesando_audio";
      el.Mic.setAttribute("aria-pressed", String(escuchando)); el.MicT.textContent = escuchando ? "Detener dictado" : "Hablar"; el.Mic.classList.toggle("is-on", escuchando);
      el.CancelaMic.hidden = !escuchando; el.CancelaEnvio.hidden = !(e === "analizando" && C.enviando && C.abortador);
      el.Enviar.disabled = !libre || !maq.puedeEnviar() || texto.length < 2;
      el.Pista.disabled = !libre || !maq.puedeEnviar() || !v.puede_pista; el.Pista.title = v && !v.puede_pista && activa ? "Ya usaste las pistas disponibles: puedes pedir la explicación directa." : "";
      el.Explica.disabled = !libre || !maq.puedeEnviar();
      el.Fin.disabled = !activa || e === "analizando" || e === "escuchando" || e === "procesando_audio";
      el.Form.hidden = !activa;
      if (el.Pausa) { var suena = e === "reproduciendo"; el.Pausa.hidden = !suena; el.Parar.hidden = !suena; el.Pausa.querySelector("span").textContent = C.pausado ? "Reanudar" : "Pausar"; }
      el.Chat.setAttribute("aria-busy", String(e === "analizando"));
      var pend = root.querySelector("#fyPend"); if (pend && e !== "analizando") pend.remove();
    }

    /* ---------- arranque ---------- */
    if (opts.sesionId) abrirSesion(opts.sesionId);
    else if (opts.contexto) empezar(opts.contexto);
    else inicio();
    return ctl;
  }

  /* ================= APERTURA EN VENTANA (desde preguntas y flujogramas) ================= */
  var dlg = null, previo = null, ctlModal = null;
  function cerrarModal() {
    if (ctlModal) { ctlModal.destruir(); ctlModal = null; }
    if (dlg) { if (dlg.close) { try { dlg.close(); } catch (e) {} } dlg.remove(); dlg = null; }
    document.documentElement.classList.remove("fy-abierto");
    if (previo && previo.focus && document.body.contains(previo)) previo.focus();
    previo = null;
  }
  /* ctx: { origen: "pregunta" | "flujograma" | "tema", pregunta_id, elegida, flujograma, tema, especialidad } */
  function abrir(ctx, disparador) {
    previo = disparador || document.activeElement; var guardado = previo; cerrarModal(); previo = guardado;
    dlg = document.createElement("dialog"); dlg.className = "fy-dlg"; dlg.setAttribute("aria-label", "Tutor Feynman IA");
    dlg.innerHTML = '<div class="fy-dlg__in"></div>'; document.body.appendChild(dlg);
    document.documentElement.classList.add("fy-abierto");
    ctlModal = montar(dlg.firstChild, { contexto: ctx, modal: true, onCerrar: cerrarModal, alNavegar: cerrarModal });
    dlg.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrarModal(); });
    if (typeof dlg.showModal === "function") dlg.showModal(); else dlg.setAttribute("open", "");
  }

  M.feynman = {
    abrir: abrir, cerrar: cerrarModal,
    /* ruta #/feynman: p.s = sesión, p.p = id de pregunta, p.o = origen, p.e = alternativa elegida, p.t = tema */
    montar: function (root, params) {
      params = params || {};
      var o = { modal: false };
      if (params.s) o.sesionId = params.s;
      else if (params.p) o.contexto = { origen: params.o === "flujograma" ? "flujograma" : "pregunta", pregunta_id: params.p, elegida: params.e || "", tema: params.t || "" };
      else if (params.t) o.contexto = { origen: "tema", tema: params.t, especialidad: params.esp || "" };
      return montar(root, o);
    }
  };
})();
