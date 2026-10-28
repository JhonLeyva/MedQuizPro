/* MedQuizPlus — plataforma de estudio (app/index.html).
 * Enrutador por hash (#/inicio, #/examenes/enam, #/simuladores/enam-2020…) y vistas.
 * Todo sale de datos reales:
 *   - preguntas, especialidades y simuladores: catalogo.js + bancos/*.json
 *   - progreso, falladas, favoritas y sesiones: MQP.progreso (hoy, este navegador)
 * La práctica usa el mismo motor que la web pública (main.js → MQP.practica).
 * Para añadir una sección: una entrada en RUTAS y una función que devuelva su HTML. */
(function () {
  "use strict";

  var M = window.MQP;
  var raiz = document.getElementById("vistaRuta");
  var sesion = document.getElementById("vistaSesion");
  if (!M || !raiz || !M.practica) return;

  var datos = null;        // { preguntas, porArchivo, fallos }
  var conteo = null;       // conteo por examen (M.ui.contarPorExamen)
  var porId = {};          // id → pregunta
  var reduced = false;
  try { reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}

  /* ---------- utilidades ---------- */
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  var I = M.icono;
  var fmtFecha = null;
  try { fmtFecha = new Intl.DateTimeFormat("es-PE", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" }); } catch (e) {}
  function fecha(t) { return fmtFecha ? fmtFecha.format(new Date(t)) : new Date(t).toLocaleString(); }
  function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }
  function recorte(txt, n) { txt = String(txt || ""); return txt.length > n ? txt.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : txt; }
  function examenPreferido() {
    var e = M.progreso.preferencia("examen");
    return M.examen(e) ? e : "enam";
  }
  function saludo() {
    var h = new Date().getHours();
    return h < 12 ? "Buenos días" : h < 19 ? "Buenas tardes" : "Buenas noches";
  }
  function vacio(icono, titulo, texto, accion) {
    return '<div class="empty-state">' +
      '<span class="empty-state__icon">' + I(icono) + '</span>' +
      '<p class="empty-state__title">' + esc(titulo) + '</p>' +
      '<p class="empty-state__text">' + esc(texto) + '</p>' +
      (accion || "") + '</div>';
  }
  function cabecera(kicker, titulo, texto, extra) {
    return '<header class="page-head">' +
      (kicker ? '<p class="kicker">' + kicker + '</p>' : "") +
      '<h1 class="page-head__title">' + titulo + '</h1>' +
      (texto ? '<p class="page-head__lead">' + texto + '</p>' : "") +
      (extra || "") + '</header>';
  }
  function cargando() { return '<div class="app-loading" role="status">' + I("libro") + '<span>Cargando el banco de preguntas…</span></div>'; }

  /* ---------- cuenta, plan y límites (cuenta.php) ----------
     Si cuenta.php no responde (sitio estático, sin PHP) la plataforma funciona como siempre: sin cuentas ni límites. */
  var CUENTA = { disponible: false, listo: false, estado: null, usuario: null };
  function api(accion, datos) {
    var opt = { method: datos ? "POST" : "GET", credentials: "same-origin", cache: "no-store" };
    if (datos) { opt.headers = { "Content-Type": "application/json", "X-MQP": "1" }; opt.body = JSON.stringify(datos); }
    return fetch(M.base + "cuenta.php?a=" + accion, opt).then(function (r) {
      return r.json().then(function (j) { return { http: r.status, ok: r.ok && j && j.ok !== false, j: j || {} }; });
    });
  }
  function cargarCuenta() {
    return api("estado").then(function (e) {
      if (!e.ok) throw 0;
      CUENTA.estado = e.j; CUENTA.disponible = true;
      return api("me");
    }).then(function (m) { CUENTA.usuario = m.j.usuario || null; })
      .catch(function () { CUENTA.disponible = false; CUENTA.usuario = null; })
      .then(function () { CUENTA.listo = true; return sincronizar(); });
  }
  /* ---------- progreso en la cuenta: se fusiona al entrar y se guarda unos segundos después de cada cambio ---------- */
  var SYNC = { cargando: false, timer: 0, ultimo: 0, error: false };
  function empujar() {
    if (!CUENTA.usuario) return Promise.resolve();
    return api("progreso_guardar", { datos: M.progreso.leer() }).then(function (r) { SYNC.error = !r.ok; if (r.ok) SYNC.ultimo = Date.now(); }).catch(function () { SYNC.error = true; });
  }
  function sincronizar() {
    if (!CUENTA.usuario || SYNC.cargando) return Promise.resolve();
    SYNC.cargando = true;
    return api("progreso_leer").then(function (r) {
      if (!r.ok) throw new Error("leer");
      var local = M.progreso.leer(), fus = r.j.datos ? M.progreso.fusionar(local, r.j.datos) : local;
      M.progreso.importar(fus);
      return api("progreso_guardar", { datos: fus });
    }).then(function (r) { SYNC.error = !r.ok; if (r.ok) SYNC.ultimo = Date.now(); })
      .catch(function () { SYNC.error = true; })
      .then(function () { SYNC.cargando = false; if (!M.practica.activa()) render(true); });
  }
  window.addEventListener("mqp:progreso", function (ev) {
    if (!CUENTA.usuario || SYNC.cargando || (ev.detail && ev.detail.importado)) return;
    clearTimeout(SYNC.timer); SYNC.timer = setTimeout(empujar, 1500);
  });
  function esPremium() { return !!(CUENTA.usuario && CUENTA.usuario.premium); }
  function limitesActivos() { return CUENTA.disponible && CUENTA.estado && CUENTA.estado.limites && !esPremium(); }
  function hechasHoy() {
    var r = M.progreso.leer().respuestas, ini = new Date(); ini.setHours(0, 0, 0, 0);
    var n = 0, t0 = ini.getTime();
    for (var id in r) if (Object.prototype.hasOwnProperty.call(r, id) && r[id].t >= t0) n++;
    return n;
  }
  /* devuelve el motivo si el plan gratuito no permite iniciar esta actividad */
  function bloqueo(cfg) {
    if (!limitesActivos()) return "";
    if (cfg.modo === "simulacro" && cfg.simulador === "enam-2020") return "simulacro";
    if (hechasHoy() >= CUENTA.estado.limite_diario) return "limite";
    return "";
  }
  function fechaLarga(seg) {
    try { return new Intl.DateTimeFormat("es-PE", { day: "numeric", month: "long", year: "numeric" }).format(new Date(seg * 1000)); } catch (e) { return new Date(seg * 1000).toLocaleDateString(); }
  }
  function soles(n) { return "S/ " + (n % 1 ? n.toFixed(2) : n); }

  /* ---------- sesiones de práctica ---------- */
  function iniciar(cfg) {
    var motivo = bloqueo(cfg);
    if (motivo) { location.hash = "#/planes?motivo=" + motivo; return; }
    cfg.volverTexto = cfg.volverTexto || "Volver";
    raiz.hidden = true;
    sesion.hidden = false;
    document.body.classList.add("en-sesion");
    M.practica.abrir(cfg);
    window.scrollTo(0, 0);
  }
  document.addEventListener("mqp:sesion-cerrada", function () {
    document.body.classList.remove("en-sesion");
    sesion.hidden = true;
    raiz.hidden = false;
    render();
  });
  /* Botones con data-accion dentro de las vistas */
  var ACCIONES = {};
  raiz.addEventListener("click", function (ev) {
    var b = ev.target.closest ? ev.target.closest("[data-accion]") : null;
    if (!b || b.disabled) return;
    var fn = ACCIONES[b.getAttribute("data-accion")];
    if (fn) { ev.preventDefault(); fn(b); }
  });

  function idsFalladas() {
    var r = M.progreso.leer().respuestas, ids = [];
    for (var id in r) if (Object.prototype.hasOwnProperty.call(r, id) && !r[id].ok && porId[id]) ids.push(id);
    ids.sort(function (a, b) { return r[b].t - r[a].t; });
    return ids;
  }
  function idsFavoritas() {
    var f = M.progreso.leer().favoritos, ids = [];
    for (var id in f) if (Object.prototype.hasOwnProperty.call(f, id) && porId[id]) ids.push(id);
    ids.sort(function (a, b) { return f[b] - f[a]; });
    return ids;
  }
  function archivosDeArea(area) {
    return M.especialidades.filter(function (e) { return e.area === area; }).map(function (e) { return e.archivo; });
  }

  ACCIONES.continuar = function () {
    var u = M.progreso.leer().ultima;
    if (!u) return;
    iniciar({ titulo: u.titulo, archivos: u.archivos, ids: u.ids, i: u.i, respuestas: u.respuestas, modo: "estudio", volverTexto: "Volver al inicio" });
  };
  ACCIONES.especialidad = function (b) {
    var esp = M.especialidad(b.getAttribute("data-archivo")), ex = M.examen(b.getAttribute("data-examen"));
    var materia = b.getAttribute("data-categoria") || "";
    iniciar({ titulo: M.ui.tituloMateria(esp.nombre, materia) + (ex.id !== "enam" ? " · " + ex.nombre : ""), archivos: [esp.archivo], examen: ex.id,
      categoria: materia, volverTexto: "Volver a " + ex.nombre });
  };
  ACCIONES.area = function (b) {
    var area = M.area(b.getAttribute("data-area")), ex = M.examen(b.getAttribute("data-examen"));
    iniciar({ titulo: area.nombre + " · " + ex.nombre, archivos: archivosDeArea(area.id), examen: ex.id, volverTexto: "Volver a " + ex.nombre });
  };
  ACCIONES.examen = function (b) {
    var ex = M.examen(b.getAttribute("data-examen"));
    iniciar({ titulo: ex.nombre + " · preguntas tipo", examen: ex.id, volverTexto: "Volver a " + ex.nombre });
  };
  ACCIONES.falladas = function (b) {
    var id = b.getAttribute("data-id");
    var ids = id ? [id] : idsFalladas();
    if (!ids.length) return;
    iniciar({ titulo: id ? "Repaso de una pregunta fallada" : "Preguntas falladas", ids: ids, volverTexto: "Volver a falladas", noGuardar: true });
  };
  ACCIONES.repaso = function (b) {      // «Repaso de hoy»: practica las preguntas por reforzar (los ids vienen del servidor; solo se usan los que existen en el banco)
    var ids = (b.getAttribute("data-ids") || "").split(",").filter(function (id) { return porId[id]; });
    if (!ids.length) return;
    iniciar({ titulo: ids.length === 1 ? "Refuerzo de una pregunta" : "Refuerzo · Repaso de hoy", ids: ids, volverTexto: "Volver a Repaso de hoy", noGuardar: true });
  };
  ACCIONES.favoritas = function (b) {
    var id = b.getAttribute("data-id");
    var ids = id ? [id] : idsFavoritas();
    if (!ids.length) return;
    iniciar({ titulo: id ? "Pregunta favorita" : "Preguntas favoritas", ids: ids, volverTexto: "Volver a favoritas", noGuardar: true });
  };

  /* ======================================================================
     VISTAS
     ====================================================================== */

  /* ---------- Inicio ---------- */
  function vistaInicio() {
    var p = M.progreso.leer();
    var ex = M.examen(examenPreferido());
    var res = M.progreso.resumen();
    var fall = idsFalladas().length;
    var u = p.ultima;

    var continuar;
    if (u && u.ids && u.ids.length) {
      var v = pct(u.respondidas || 0, u.total || u.ids.length);
      continuar = '<article class="card card--continue">' +
        '<p class="card__eyebrow">Continuar entrenamiento</p>' +
        '<h2 class="card__title">' + esc(u.titulo) + '</h2>' +
        (u.especialidad && u.especialidad !== u.titulo ? '<p class="card__sub">' + esc(u.especialidad) + '</p>' : "") +
        '<div class="meter" aria-label="Progreso de la sesión"><span class="meter__fill" style="width:' + v + '%"></span></div>' +
        '<p class="card__meta"><b>' + (u.respondidas || 0) + " / " + (u.total || u.ids.length) + '</b> preguntas · última actividad ' + esc(fecha(u.t)) + '</p>' +
        '<button class="btn btn--primary" type="button" data-accion="continuar">Continuar' + I("flecha", "btn__arrow") + '</button>' +
        '</article>';
    } else {
      continuar = '<article class="card card--continue card--start">' +
        '<p class="card__eyebrow">Empieza a entrenar</p>' +
        '<h2 class="card__title">Tu primera sesión</h2>' +
        '<p class="card__sub">Elige una especialidad del banco ' + esc(ex.nombre) + ' y resuelve sus preguntas comentadas. Aquí aparecerá la sesión que dejes a medias.</p>' +
        '<a class="btn btn--primary" href="#/examenes/' + ex.id + '">Ir al banco ' + esc(ex.nombre) + I("flecha", "btn__arrow") + '</a>' +
        '</article>';
    }

    var resumen;
    if (res.respondidas) {
      resumen = '<dl class="kpis">' +
        '<div class="kpi"><dt>Preguntas respondidas</dt><dd>' + M.miles(res.respondidas) + '</dd></div>' +
        '<div class="kpi"><dt>Correctas</dt><dd>' + M.miles(res.correctas) + '</dd></div>' +
        '<div class="kpi"><dt>Aciertos</dt><dd>' + res.porcentaje + '%</dd></div>' +
        '</dl>';
    } else {
      resumen = '<p class="muted">Todavía no hay respuestas registradas. Tus cifras aparecerán aquí en cuanto resuelvas tu primera pregunta.</p>';
    }

    var recientes = p.sesiones.slice(0, 4);
    var actividad = recientes.length ? listaSesiones(recientes) : '<p class="muted">Aquí verás tus últimas sesiones y simulacros.</p>';

    var nFav = idsFavoritas().length;
    var ya = res.respondidas
      ? "Llevas " + M.plural(res.respondidas, "pregunta respondida", "preguntas respondidas") + " con " + res.porcentaje + "% de aciertos."
      : "Estamos contigo en tu preparación para " + ex.nombre + ". Elige un banco o un simulador y empieza cuando quieras.";
    var bienvenida = '<section class="welcome__hi card"><h1 class="welcome__title">' + esc(saludo()) + ' <span aria-hidden="true">👋</span></h1>' +
      '<p>' + esc(ya) + '</p>' + continuar.replace("card card--continue", "welcome__continue") + '</section>';
    function promo(titulo, texto, botones) {
      return '<section class="promo card"><h2 class="promo__title">' + titulo + '</h2><p class="promo__text">' + texto + '</p><div class="promo__actions">' + botones + '</div></section>';
    }
    function bot(href, icono, texto, extra) {
      return '<a class="btn btn--primary btn--tile" href="' + href + '">' + I(icono) + '<span>' + texto + '</span>' + (extra || "") + '</a>';
    }
    var tarjetas =
      promo("Prepárate para tu examen",
        "Practica con preguntas comentadas por especialidad y mídete con simulacros cronometrados. Cada pregunta trae su comentario y su flujograma.",
        bot("#/banco", "libro", "Banco de preguntas") + bot("#/simuladores", "reloj", "Simuladores")) +
      promo("Refuerza lo que ya practicaste",
        "Repasa las preguntas que fallaste, las que guardaste con la estrella y mira en qué especialidades vas mejor.",
        bot("#/falladas", "cruz", "Falladas", fall ? '<b class="btn__n">' + fall + '</b>' : "") + bot("#/favoritas", "estrella", "Favoritas", nFav ? '<b class="btn__n">' + nFav + '</b>' : "") + bot("#/progreso", "grafico", "Mi progreso"));

    var avisoPago = parametros.pago === "ok" ? '<div class="notice ' + (esPremium() ? "notice--ok" : "") + '" role="status" id="avisoPago">' + (esPremium() ? '<b>¡Tu plan Premium está activo!</b> Gracias por tu compra. Ya puedes usar todo sin límites.' : '<b>Estamos confirmando tu pago.</b> Esto suele tardar unos segundos; esta página se actualiza sola.') + '</div>' : "";
    return avisoPago + '<div class="welcome"><div class="welcome__side">' + bienvenida + '</div><div class="welcome__main">' + tarjetas +
      '<div class="welcome__two">' +
        '<section class="card"><div class="card__head"><h2 class="card__h">Tu resumen</h2><a class="link-arrow" href="#/progreso">Ver mi progreso <span aria-hidden="true">→</span></a></div>' + resumen + '</section>' +
        '<section class="card"><div class="card__head"><h2 class="card__h">Actividad reciente</h2></div>' + actividad + '</section>' +
      '</div></div></div>';
  }

  var esperaPago = 0;
  function esperarPago() {
    if (parametros.pago !== "ok" || !CUENTA.disponible || esPremium()) return;
    var intentos = 0; clearInterval(esperaPago);
    esperaPago = setInterval(function () {
      intentos++;
      api("me").then(function (m) {
        CUENTA.usuario = m.j.usuario || CUENTA.usuario;
        if (esPremium()) { clearInterval(esperaPago); if (ruta().nombre === "inicio") render(true); pintarChrome(); }
      });
      if (intentos >= 15) clearInterval(esperaPago);
    }, 2500);
  }

  function listaSesiones(lista) {
    return '<ul class="activity">' + lista.map(function (s) {
      var v = pct(s.correctas, s.respondidas || s.total);
      return '<li class="activity__item">' +
        '<span class="activity__icon' + (s.tipo === "simulacro" ? " is-sim" : "") + '">' + I(s.tipo === "simulacro" ? "reloj" : "libro") + '</span>' +
        '<span class="activity__body"><b>' + esc(s.titulo) + '</b><small>' + (s.tipo === "simulacro" ? "Simulacro" : "Estudio") + " · " + esc(fecha(s.t)) + '</small></span>' +
        '<span class="activity__score" title="' + s.correctas + ' correctas de ' + (s.tipo === "simulacro" ? s.total : s.respondidas) + '">' + s.correctas + "/" + (s.tipo === "simulacro" ? s.total : s.respondidas) + '<small>' + v + '%</small></span>' +
        '</li>';
    }).join("") + '</ul>';
  }

  /* ---------- Exámenes ---------- */
  function vistaExamenes() {
    var tarjetas = M.examenes.map(function (e) {
      var c = conteo[e.id], n = 0;
      for (var a in c.porArchivo) if (c.porArchivo[a]) n++;
      var vivo = e.estado === "disponible";
      var lista = vivo
        ? '<li><b>' + c.total + '</b> preguntas comentadas</li>' +
          (c.oficiales ? '<li><b>' + c.oficiales + '</b> oficiales ENAM ' + esc(Object.keys(c.anios).join(", ")) + '</li>' : "") +
          '<li><b>' + n + '</b> especialidades</li><li>Simuladores cronometrados</li>'
        : '<li>Banco por especialidad en construcción</li>' +
          (c.total ? '<li><b>' + c.total + '</b> preguntas tipo publicadas</li>' : "") + '<li>Simulador: próximamente</li>';
      return '<article class="exam' + (vivo ? " exam--live" : "") + '">' +
        '<div class="exam__top"><span class="exam__mark" aria-hidden="true">' + esc(e.nombre.charAt(0)) + '</span>' +
        '<span class="badge ' + (vivo ? "badge--ok" : "badge--soon") + '">' + (vivo ? "Disponible" : "Próximamente") + '</span></div>' +
        '<h2 class="exam__name">' + esc(e.nombre) + '</h2><p class="exam__desc">' + esc(e.nombreLargo === e.nombre ? e.titulo : e.nombreLargo) + '</p>' +
        '<ul class="exam__list' + (vivo ? "" : " exam__list--muted") + '">' + lista + '</ul>' +
        '<a class="btn ' + (vivo ? "btn--primary" : "btn--ghost") + ' btn--block exam__cta" href="#/examenes/' + e.id + '">Explorar ' + esc(e.id === "residentado" ? "Residentado" : e.nombre) + '</a>' +
        '</article>';
    }).join("");
    return cabecera("Exámenes", "Elige tu examen", "ENAM tiene su banco completo; Residentado Médico y EsSalud crecen con cada actualización.") +
      '<div class="exams exams--app">' + tarjetas + '</div>';
  }

  /* ---------- Detalle de examen: áreas y especialidades ---------- */
  function vistaExamen(id) {
    var ex = M.examen(id);
    if (!ex) return vistaNoEncontrada();
    var c = conteo[ex.id];
    var vivo = ex.estado === "disponible";
    var extra = '<ul class="explorer__stats">' +
      (c.total ? '<li>' + I("check") + M.plural(c.total, vivo ? "pregunta comentada" : "pregunta tipo", vivo ? "preguntas comentadas" : "preguntas tipo") + '</li>' : "") +
      (c.oficiales ? '<li>' + I("check") + c.oficiales + ' oficiales ENAM ' + esc(Object.keys(c.anios).join(", ")) + '</li>' : "") +
      (vivo ? '<li>' + I("check") + 'Comentario y flujograma en cada pregunta</li>' : "") + '</ul>';
    var aviso = vivo ? "" :
      '<div class="soon-banner"><span class="soon-banner__icon">' + I("reloj") + '</span>' +
      '<div class="soon-banner__copy"><p class="soon-banner__title">Próximamente</p><p>' +
      (c.total ? "Estamos construyendo el banco completo por especialidad. Mientras tanto ya puedes resolver " + M.plural(c.total, "pregunta tipo publicada", "preguntas tipo publicadas") + "." : "Estamos construyendo el banco completo por especialidad.") +
      '</p></div>' + (c.total ? '<button class="btn btn--ghost btn--sm" type="button" data-accion="examen" data-examen="' + ex.id + '">Practicar ' + M.plural(c.total, "pregunta tipo", "preguntas tipo") + '</button>' : "") + '</div>';

    var ord = ORDENES[parametros.orden] ? parametros.orden : "az";
    var filtros = '<div class="filters" role="search">' +
      '<div class="combo" id="fCombo">' + I("lupa") +
      '<input type="text" id="fEsp" role="combobox" aria-expanded="false" aria-controls="fLista" aria-autocomplete="list" placeholder="Buscar o elegir especialidades…" value="' + esc(parametros.q || "") + '" autocomplete="off">' +
      '<button class="combo__btn" type="button" id="fAbrir" aria-label="Ver todas las especialidades" tabindex="-1">' + I("chevron", "combo__chev") + '</button>' +
      '<ul class="combo__lista" id="fLista" role="listbox" aria-multiselectable="true" hidden></ul></div>' +
      '<label class="filters__sort"><span>Ordenar por</span><select id="fOrden">' + Object.keys(ORDENES).map(function (k) { return '<option value="' + k + '"' + (k === ord ? " selected" : "") + '>' + ORDENES[k] + '</option>'; }).join("") + '</select></label>' +
      '</div><div class="filters__sel" id="fSel" hidden></div>' +
      '<div class="filters__meta"><p class="filters__count muted small" id="fCuenta" aria-live="polite"></p>' + botonReiniciarBanco(ex) + '</div><div class="specs specs--app" id="gridEsp"></div>' +
      '<div id="fVacio" hidden>' + vacio("lupa", "Ninguna especialidad coincide", "Prueba con otra palabra o quita los filtros.", '<button class="btn btn--ghost" type="button" id="fLimpiar">Quitar filtros</button>') + '</div>';
    return '<nav class="crumbs" aria-label="Ruta"><a href="#/examenes">Exámenes</a><span aria-hidden="true">/</span><span aria-current="page">' + esc(ex.nombre) + '</span></nav>' +
      cabecera(vivo ? "Banco disponible" : "Próximamente", esc(ex.titulo), esc(ex.lema), extra) + aviso + filtros;
  }
  /* las tarjetas de especialidad son el componente compartido (main.js → MQP.ui) */
  /* ---------- reiniciar: borra las respuestas de un banco o de una especialidad (pide confirmación en dos pasos) ---------- */
  function idsDe(exId, archivo) {
    return M.filtrar(datos.preguntas, { examen: exId, archivos: archivo ? [archivo] : null }).map(function (q) { return q.id; });
  }
  function respondidasEn(ids) { var r = M.progreso.leer().respuestas, n = 0; ids.forEach(function (id) { if (r[id]) n++; }); return n; }
  function botonReiniciarBanco(ex) {
    var n = respondidasEn(idsDe(ex.id, null));
    return n ? '<button class="btn btn--ghost btn--sm btn--reset" type="button" data-accion="reiniciar" data-examen="' + ex.id + '" data-etiqueta="Reiniciar banco ' + esc(ex.nombre) + '">' + I("reinicio") + '<span>Reiniciar banco ' + esc(ex.nombre) + '</span></button>' : "";
  }
  ACCIONES.reiniciar = function (b) {
    var span = b.querySelector("span") || b, original = b.getAttribute("data-etiqueta") || "Reiniciar";
    if (b.getAttribute("data-armado") !== "1") {
      b.setAttribute("data-armado", "1"); b.classList.add("is-armed");
      span.textContent = "Pulsa otra vez para confirmar";
      setTimeout(function () { if (b.isConnected) { b.removeAttribute("data-armado"); b.classList.remove("is-armed"); span.textContent = original; } }, 4000);
      return;
    }
    var exId = b.getAttribute("data-examen"), archivo = b.getAttribute("data-archivo") || "";
    var n = M.progreso.reiniciar(idsDe(exId, archivo));
    var nombre = archivo ? M.especialidad(archivo).nombre : "el banco " + M.examen(exId).nombre;
    render(true);
    var c = document.getElementById("fCuenta"); if (c) c.textContent = "Se reinició " + nombre + ": " + M.plural(n, "respuesta borrada", "respuestas borradas") + ".";
  };

  var ORDENES = { az: "Orden alfabético (A–Z)", preguntas: "Más preguntas", pendientes: "Menos avance", reforzar: "Por reforzar (menos aciertos)" };
  var tarjetasEsp = [];
  function montarTarjetas(exId) {
    var c = conteo[exId], prog = M.ui.progresoPorArchivo(exId), k = 0;
    var vivo = M.examen(exId).estado === "disponible", grid = document.getElementById("gridEsp");
    tarjetasEsp = [];
    M.especialidades.forEach(function (esp) {
      var t = M.ui.tarjetaEspecialidad(esp, k++, function (e, materia) {
        var attrs = { "data-archivo": esp.archivo, "data-examen": exId, "data-categoria": materia || "" };
        ACCIONES.especialidad({ getAttribute: function (n) { return attrs[n]; } });
      });
      var ok = datos.porArchivo[esp.archivo] && datos.porArchivo[esp.archivo].ok;
      var p = prog[esp.archivo] || {}, total = c.porArchivo[esp.archivo] || 0;
      t.actualizar(ok ? { estado: "ok", total: total, respondidas: p.respondidas || 0, tipo: !vivo,
        materias: esp.categorias.length ? M.ui.contarMaterias(datos.preguntas, esp.archivo, exId) : null } : { estado: "error" });
      t.nodo.setAttribute("data-esp", esp.archivo);
      if (p.respondidas) {
        var rb = document.createElement("button");
        rb.type = "button"; rb.className = "spec__reset"; rb.setAttribute("data-accion", "reiniciar");
        rb.setAttribute("data-archivo", esp.archivo); rb.setAttribute("data-examen", exId); rb.setAttribute("data-etiqueta", "Reiniciar");
        rb.setAttribute("aria-label", "Reiniciar " + esp.nombre);
        rb.innerHTML = I("reinicio") + "<span>Reiniciar</span>";
        var pg = t.nodo.querySelector(".spec__progress");
        if (pg) pg.insertAdjacentElement("afterend", rb); else t.nodo.appendChild(rb);
      }
      tarjetasEsp.push({ nodo: t.nodo, esp: esp, total: total, resp: p.respondidas || 0, corr: p.correctas || 0 });
    });
    ordenarTarjetas("az");
    tarjetasEsp.forEach(function (x) { grid.appendChild(x.nodo); });
  }
  function ordenarTarjetas(clave) {
    var grid = document.getElementById("gridEsp");
    function alfa(a, b) { return a.esp.nombre.localeCompare(b.esp.nombre, "es"); }
    function avance(x) { return x.total ? x.resp / x.total : 1; }
    function acierto(x) { return x.resp >= 3 ? x.corr / x.resp : 2; }       // sin datos suficientes, al final
    var f = { az: alfa,
      preguntas: function (a, b) { return b.total - a.total || alfa(a, b); },
      pendientes: function (a, b) { return avance(a) - avance(b) || alfa(a, b); },
      reforzar: function (a, b) { return acierto(a) - acierto(b) || alfa(a, b); } }[clave] || alfa;
    tarjetasEsp.sort(f);
    if (grid) tarjetasEsp.forEach(function (x) { grid.appendChild(x.nodo); });
  }

  /* buscador con lista desplegable de selección múltiple; el estado vive en la URL
     (#/examenes/enam?q=…&esp=a,b&orden=…), así atrás / recargar lo conservan */
  function enlazarFiltros(exId) {
    var inp = document.getElementById("fEsp"), lista = document.getElementById("fLista"), sel = document.getElementById("fOrden"), combo = document.getElementById("fCombo");
    if (!inp || !lista || !sel) return;
    function norm(t) { return String(t || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, ""); }
    var validos = {}; M.especialidades.forEach(function (e) { validos[e.archivo] = e; });
    var elegidas = (parametros.esp || "").split(",").filter(function (a) { return validos[a]; });
    var alfa = M.especialidades.slice().sort(function (x, y) { return x.nombre.localeCompare(y.nombre, "es"); });
    var total = {}; tarjetasEsp.forEach(function (x) { total[x.esp.archivo] = x.total; });
    var activo = -1, visibles = [];

    function pintarLista() {
      var q = norm(inp.value.trim());
      visibles = alfa.filter(function (e) { return !q || norm(e.nombre).indexOf(q) !== -1; });
      lista.innerHTML = visibles.length ? visibles.map(function (e, i) {
        var on = elegidas.indexOf(e.archivo) !== -1;
        return '<li role="option" id="fo' + i + '" data-esp="' + e.archivo + '" aria-selected="' + on + '" class="combo__op' + (i === activo ? " is-activo" : "") + '"><span class="combo__chk" aria-hidden="true">' + (on ? "✓" : "") + '</span><span class="combo__nom">' + esc(e.nombre) + '</span><small>' + (total[e.archivo] || 0) + '</small></li>';
      }).join("") : '<li class="combo__vacio">Ninguna especialidad coincide</li>';
      if (activo >= 0) inp.setAttribute("aria-activedescendant", "fo" + activo); else inp.removeAttribute("aria-activedescendant");
    }
    function abrir(v) { lista.hidden = !v; inp.setAttribute("aria-expanded", String(v)); combo.classList.toggle("is-abierto", v); if (v) pintarLista(); }
    function pintarSeleccion() {
      var cont = document.getElementById("fSel");
      if (!elegidas.length) { cont.hidden = true; cont.innerHTML = ""; return; }
      var preguntas = elegidas.reduce(function (n, a) { return n + (total[a] || 0); }, 0);
      cont.hidden = false;
      cont.innerHTML = '<span class="filters__sel-t">Elegidas:</span>' + elegidas.map(function (a) { return '<button type="button" class="pill" data-quitar="' + a + '" aria-label="Quitar ' + esc(validos[a].nombre) + '">' + esc(validos[a].nombre) + ' <span aria-hidden="true">✕</span></button>'; }).join("") +
        '<button type="button" class="btn btn--primary btn--sm" id="fEntrenar">Entrenar ' + (elegidas.length === 1 ? "esta especialidad" : "las " + elegidas.length + " elegidas") + ' · ' + M.plural(preguntas, "pregunta", "preguntas") + '</button>' +
        '<button type="button" class="link-btn" id="fQuitarTodo">Quitar todas</button>';
    }
    function aplicar() {
      var q = norm(inp.value.trim()), n = 0;
      tarjetasEsp.forEach(function (x) {
        var ver = elegidas.length ? elegidas.indexOf(x.esp.archivo) !== -1 : (!q || norm(x.esp.nombre).indexOf(q) !== -1);
        x.nodo.hidden = !ver; if (ver) n++;
      });
      document.getElementById("fVacio").hidden = n > 0;
      document.getElementById("fCuenta").textContent = n === tarjetasEsp.length ? M.plural(n, "especialidad", "especialidades") + " · " + ORDENES[sel.value].toLowerCase() : n + " de " + tarjetasEsp.length + " especialidades";
      var qs = [];
      if (inp.value.trim() && !elegidas.length) qs.push("q=" + encodeURIComponent(inp.value.trim()));
      if (elegidas.length) qs.push("esp=" + elegidas.join(","));
      if (sel.value !== "az") qs.push("orden=" + sel.value);
      history.replaceState(null, "", "#/examenes/" + encodeURIComponent(exId) + (qs.length ? "?" + qs.join("&") : ""));
      pintarSeleccion();
    }
    function alternar(arch) {
      var i = elegidas.indexOf(arch);
      if (i === -1) elegidas.push(arch); else elegidas.splice(i, 1);
      aplicar(); pintarLista();
    }

    inp.addEventListener("focus", function () { abrir(true); });
    inp.addEventListener("input", function () { activo = -1; abrir(true); aplicar(); });
    document.getElementById("fAbrir").addEventListener("click", function () { if (lista.hidden) { abrir(true); inp.focus(); } else abrir(false); });
    inp.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowDown" || ev.key === "ArrowUp") { ev.preventDefault(); if (lista.hidden) abrir(true); if (!visibles.length) return; activo = (activo + (ev.key === "ArrowDown" ? 1 : visibles.length - 1)) % visibles.length; pintarLista(); var el = document.getElementById("fo" + activo); if (el && el.scrollIntoView) el.scrollIntoView({ block: "nearest" }); }
      else if (ev.key === "Enter") { ev.preventDefault(); if (activo >= 0 && visibles[activo]) alternar(visibles[activo].archivo); else if (visibles.length === 1) alternar(visibles[0].archivo); }
      else if (ev.key === "Escape") { abrir(false); }
      else if (ev.key === "Backspace" && !inp.value && elegidas.length) { elegidas.pop(); aplicar(); pintarLista(); }
    });
    lista.addEventListener("mousedown", function (ev) { ev.preventDefault(); });          // no pierde el foco del campo
    lista.addEventListener("click", function (ev) { var li = ev.target.closest && ev.target.closest("[data-esp]"); if (li) alternar(li.getAttribute("data-esp")); });
    document.addEventListener("click", function cierra(ev) {
      if (!document.getElementById("fCombo")) { document.removeEventListener("click", cierra); return; }
      var ruta = ev.composedPath ? ev.composedPath() : [];            // el clic en una opción re-pinta la lista: se mira la ruta original
      if (ruta.indexOf(combo) === -1) abrir(false);
    });
    sel.addEventListener("change", function () { ordenarTarjetas(sel.value); aplicar(); });
    document.getElementById("fSel").addEventListener("click", function (ev) {
      var q = ev.target.closest && ev.target.closest("[data-quitar]");
      if (q) { alternar(q.getAttribute("data-quitar")); return; }
      if (ev.target.id === "fQuitarTodo") { elegidas = []; aplicar(); pintarLista(); }
      if (ev.target.id === "fEntrenar") {
        var ex = M.examen(exId);
        iniciar({ titulo: elegidas.length === 1 ? validos[elegidas[0]].nombre : M.plural(elegidas.length, "especialidad", "especialidades") + " · " + ex.nombre, archivos: elegidas.slice(), examen: ex.id, volverTexto: "Volver a " + ex.nombre });
      }
    });
    document.getElementById("fLimpiar").addEventListener("click", function () { inp.value = ""; elegidas = []; aplicar(); pintarLista(); inp.focus(); });
    ordenarTarjetas(sel.value);
    aplicar();
  }

  /* ---------- Banco de preguntas: configurador de sesión ---------- */
  var conf = { examen: null, archivos: [], categorias: [], filtro: "todas", cantidad: 20, orden: "aleatorio", modo: "estudio" };
  /* especialidades elegidas que se pueden recortar por materia (hoy: Ciencias Básicas) */
  function conMaterias() {
    return conf.archivos.filter(function (a) { var e = M.especialidad(a); return e && e.categorias.length; });
  }
  function opcion(nombre, valor, texto, detalle, activo, deshabilitado) {
    return '<label class="pick' + (deshabilitado ? " is-disabled" : "") + '">' +
      '<input type="radio" name="' + nombre + '" value="' + esc(valor) + '"' + (activo ? " checked" : "") + (deshabilitado ? " disabled" : "") + '>' +
      '<span class="pick__box"><b>' + esc(texto) + '</b>' + (detalle ? '<small>' + esc(detalle) + '</small>' : "") + '</span></label>';
  }
  function candidatas() {
    return M.filtrar(datos.preguntas, { examen: conf.examen, archivos: conf.archivos, categorias: conf.categorias, filtro: conf.filtro });
  }
  /* ---------- Banco: elegir un banco (lista) ---------- */
  function vistaBancos() {
    var filas = M.examenes.map(function (e) {
      var c = conteo[e.id], vivo = e.estado === "disponible";
      var sub = vivo ? M.plural(c.total, "pregunta comentada", "preguntas comentadas") : (c.total ? M.plural(c.total, "pregunta tipo", "preguntas tipo") : "Banco en construcción");
      return '<li><a class="bank-row" href="#/examenes/' + e.id + '"><span class="bank-row__mark' + (vivo ? " is-live" : "") + '">' + esc(e.nombre.charAt(0)) + '</span>' +
        '<span class="bank-row__name">' + esc(e.nombre) + '<small>' + esc(sub) + '</small></span>' +
        (vivo ? "" : '<span class="badge badge--soon">Próximamente</span>') + I("chevron", "bank-row__go") + '</a></li>';
    }).join("");
    return cabecera("Banco de preguntas", "Selecciona un banco de preguntas", "Elige el examen que preparas y entra por área y especialidad.") +
      '<div class="bank-list card"><ul>' + filas +
      '<li class="bank-list__sep"><a class="bank-row" href="#/banco/configurar"><span class="bank-row__mark bank-row__mark--custom">' + I("ajustes") + '</span>' +
      '<span class="bank-row__name">Arma tu sesión a medida<small>Varias especialidades, materias, filtros y cantidad de preguntas</small></span>' + I("chevron", "bank-row__go") + '</a></li></ul></div>';
  }

  function vistaBanco() {
    if (!conf.examen) conf.examen = examenPreferido();
    var c = conteo[conf.examen];
    var p = M.progreso.leer();
    var base = M.filtrar(datos.preguntas, { examen: conf.examen, archivos: conf.archivos, categorias: conf.categorias });
    var nNo = 0, nFa = 0, nFav = 0;
    for (var k = 0; k < base.length; k++) {
      var r = p.respuestas[base[k].id];
      if (!r) nNo++; else if (!r.ok) nFa++;
      if (p.favoritos[base[k].id]) nFav++;
    }
    var n = candidatas().length;
    var usar = conf.cantidad ? Math.min(conf.cantidad, n) : n;

    var exams = M.examenes.map(function (e) {
      var t = conteo[e.id].total;
      return opcion("examen", e.id, e.nombre, t ? M.plural(t, "pregunta", "preguntas") + (e.estado !== "disponible" ? " tipo" : "") : "Próximamente", conf.examen === e.id, !t);
    }).join("");

    var chips = '<button class="chip" type="button" data-esp="" aria-pressed="' + (!conf.archivos.length) + '">Todas</button>' +
      M.areas.map(function (area) {
        return M.especialidades.filter(function (e) { return e.area === area.id; }).map(function (e) {
          var t = c.porArchivo[e.archivo] || 0;
          return '<button class="chip" type="button" data-esp="' + e.archivo + '" aria-pressed="' + (conf.archivos.indexOf(e.archivo) >= 0) + '"' + (t ? "" : " disabled") + '>' + esc(e.nombre) + ' <span class="chip__n">' + t + '</span></button>';
        }).join("");
      }).join("");

    /* materias: aparecen solo si entre las especialidades elegidas hay una con categorías */
    var paso = 0;
    var conCat = conMaterias(), materias = "";
    if (conCat.length) {
      var nombres = [], cuenta = {};
      conCat.forEach(function (a) {
        var e = M.especialidad(a), cm = M.ui.contarMaterias(datos.preguntas, a, conf.examen);
        e.categorias.forEach(function (nm) {
          if (nombres.indexOf(nm) < 0) nombres.push(nm);
          cuenta[nm] = (cuenta[nm] || 0) + (cm[nm] || 0);
        });
      });
      var chipsMat = '<button class="chip" type="button" data-cat="" aria-pressed="' + (!conf.categorias.length) + '">Todas las materias</button>' +
        nombres.map(function (nm) {
          var t = cuenta[nm] || 0;
          return '<button class="chip" type="button" data-cat="' + esc(nm) + '" aria-pressed="' + (conf.categorias.indexOf(nm) >= 0) + '"' + (t ? "" : " disabled") + '>' + esc(nm) + ' <span class="chip__n">' + t + '</span></button>';
        }).join("");
      materias = '<fieldset class="builder__step"><legend><span>' + (++paso + 2) + '</span>Materias <small>' +
        (conf.categorias.length ? M.plural(conf.categorias.length, "elegida", "elegidas") : "todas") + (conCat.length === 1 ? " · " + esc(M.especialidad(conCat[0]).nombre) : "") +
        '</small></legend><div class="chips chips--compact chips--wrap" id="bCat">' + chipsMat + '</div></fieldset>';
    }
    var cantidades = [10, 20, 40, 0].map(function (q) {
      return opcion("cantidad", String(q), q ? String(q) : "Todas", "", conf.cantidad === q, false);
    }).join("");

    var tiempo = conf.modo === "simulacro" ? " · " + M.duracion(usar * 60) : "";
    return '<nav class="crumbs" aria-label="Ruta"><a href="#/banco">Banco de preguntas</a><span aria-hidden="true">/</span><span aria-current="page">Arma tu sesión</span></nav>' + cabecera("Banco de preguntas", "Arma tu sesión", "Elige examen, especialidades, qué preguntas incluir y cómo quieres resolverlas.") +
      '<form class="builder" id="builder" onsubmit="return false">' +
        '<fieldset class="builder__step"><legend><span>1</span>Examen</legend><div class="picks">' + exams + '</div></fieldset>' +
        '<fieldset class="builder__step"><legend><span>2</span>Especialidades <small>' + (conf.archivos.length ? M.plural(conf.archivos.length, "elegida", "elegidas") : "todas") + '</small></legend><div class="chips chips--compact chips--wrap" id="bEsp">' + chips + '</div></fieldset>' +
        materias +
        '<fieldset class="builder__step"><legend><span>' + (3 + paso) + '</span>Preguntas</legend><div class="picks">' +
          opcion("filtro", "todas", "Todas", M.plural(base.length, "pregunta", "preguntas"), conf.filtro === "todas", !base.length) +
          opcion("filtro", "no-respondidas", "No respondidas", String(nNo), conf.filtro === "no-respondidas", !nNo) +
          opcion("filtro", "falladas", "Falladas", String(nFa), conf.filtro === "falladas", !nFa) +
          opcion("filtro", "favoritas", "Favoritas", String(nFav), conf.filtro === "favoritas", !nFav) +
        '</div></fieldset>' +
        '<fieldset class="builder__step"><legend><span>' + (4 + paso) + '</span>Número de preguntas</legend><div class="picks picks--compact">' + cantidades + '</div></fieldset>' +
        '<fieldset class="builder__step"><legend><span>' + (5 + paso) + '</span>Orden</legend><div class="picks">' +
          opcion("orden", "aleatorio", "Aleatorio", "Mezcla las preguntas", conf.orden === "aleatorio") +
          opcion("orden", "secuencial", "En orden", "Como están en el banco", conf.orden === "secuencial") +
        '</div></fieldset>' +
        '<fieldset class="builder__step"><legend><span>' + (6 + paso) + '</span>Modo</legend><div class="picks">' +
          opcion("modo", "estudio", "Estudio", "Ves la explicación al responder", conf.modo === "estudio") +
          opcion("modo", "simulacro", "Simulacro", "Cronometrado, resultado al final", conf.modo === "simulacro") +
        '</div></fieldset>' +
        '<div class="builder__go">' +
          '<p class="builder__sum" aria-live="polite">' + (usar ? "<b>" + M.plural(usar, "pregunta", "preguntas") + "</b>" + tiempo : "No hay preguntas con esta selección") + '</p>' +
          '<button class="btn btn--primary btn--lg" type="button" data-accion="comenzar"' + (usar ? "" : " disabled") + '>Comenzar' + I("flecha", "btn__arrow") + '</button>' +
        '</div>' +
      '</form>';
  }
  function enlazarBanco() {
    var f = document.getElementById("builder");
    if (!f) return;
    f.addEventListener("change", function (ev) {
      var t = ev.target;
      if (t.name === "examen") { conf.examen = t.value; conf.archivos = []; conf.categorias = []; conf.filtro = "todas"; }
      else if (t.name === "filtro") conf.filtro = t.value;
      else if (t.name === "cantidad") conf.cantidad = parseInt(t.value, 10);
      else if (t.name === "orden") conf.orden = t.value;
      else if (t.name === "modo") conf.modo = t.value;
      repintar(t.name ? 'input[name="' + t.name + '"]:checked' : null);
    });
    document.getElementById("bEsp").addEventListener("click", function (ev) {
      var b = ev.target.closest ? ev.target.closest(".chip") : null;
      if (!b || b.disabled) return;
      var a = b.getAttribute("data-esp");
      if (!a) conf.archivos = [];
      else if (conf.archivos.indexOf(a) >= 0) conf.archivos.splice(conf.archivos.indexOf(a), 1);
      else conf.archivos.push(a);
      if (!conMaterias().length) conf.categorias = [];
      if (conf.filtro !== "todas") conf.filtro = "todas";
      repintar('#bEsp [data-esp="' + a + '"]');
    });
    var bCat = document.getElementById("bCat");
    if (bCat) bCat.addEventListener("click", function (ev) {
      var b = ev.target.closest ? ev.target.closest(".chip") : null;
      if (!b || b.disabled) return;
      var c = b.getAttribute("data-cat");
      if (!c) conf.categorias = [];
      else if (conf.categorias.indexOf(c) >= 0) conf.categorias.splice(conf.categorias.indexOf(c), 1);
      else conf.categorias.push(c);
      if (conf.filtro !== "todas") conf.filtro = "todas";
      var sel = '#bCat .chip[data-cat="' + (window.CSS && CSS.escape ? CSS.escape(c) : c) + '"]';
      repintar(sel);
    });
  }
  /* repinta la vista sin perder el foco del control que se tocó */
  function repintar(selectorFoco) {
    var y = window.scrollY;
    render(true);
    window.scrollTo(0, y);
    if (selectorFoco) { var n = raiz.querySelector(selectorFoco); if (n) n.focus({ preventScroll: true }); }
  }
  ACCIONES.comenzar = function () {
    var ex = M.examen(conf.examen);
    var partes = conf.archivos.length === 1 ? M.especialidad(conf.archivos[0]).nombre : conf.archivos.length ? M.plural(conf.archivos.length, "especialidad", "especialidades") : "Todas las especialidades";
    if (conf.categorias.length) partes += " · " + (conf.categorias.length === 1 ? conf.categorias[0] : M.plural(conf.categorias.length, "materia", "materias"));
    var n = candidatas().length, usar = conf.cantidad ? Math.min(conf.cantidad, n) : n;
    iniciar({
      titulo: (conf.modo === "simulacro" ? "Simulacro · " : "") + ({ "no-respondidas": "No respondidas · ", falladas: "Falladas · ", favoritas: "Favoritas · " }[conf.filtro] || "") + ex.nombre + " · " + partes,
      examen: conf.examen, archivos: conf.archivos.slice(), categorias: conf.categorias.slice(), filtro: conf.filtro,
      cantidad: conf.cantidad || null, orden: conf.orden, modo: conf.modo,
      tiempo: conf.modo === "simulacro" ? usar * 60 : null,
      volverTexto: "Volver al banco", repetirIds: conf.filtro === "todas"
    });
  };

  /* ---------- Simuladores ---------- */
  function datosSimulador(sim, archivo) {
    var lista = M.filtrar(datos.preguntas, { examen: sim.examen, origen: sim.origen, archivos: archivo ? [archivo] : null });
    var n = sim.cantidad ? Math.min(sim.cantidad, lista.length) : lista.length;
    var esp = {};
    for (var k = 0; k < lista.length; k++) esp[lista[k].archivo] = true;
    return { disponibles: lista.length, n: n, segundos: n * (sim.segundosPorPregunta || 60), especialidades: Object.keys(esp).length };
  }
  function vistaSimuladores() {
    var tarjetas = M.simuladores.map(function (sim) {
      var vivo = sim.estado === "disponible";
      var d = vivo ? datosSimulador(sim) : null;
      var datosTxt = !vivo ? "" : sim.eligeEspecialidad
        ? "Hasta " + sim.cantidad + " preguntas · 1 min por pregunta"
        : M.plural(d.n, "pregunta", "preguntas") + " · " + M.duracion(d.segundos) + " · " + M.plural(d.especialidades, "especialidad", "especialidades");
      return '<article class="sim-tile' + (vivo ? "" : " sim-tile--soon") + (sim.id === "enam-2020" ? " sim-tile--feature" : "") + '">' +
        '<div class="sim-tile__top"><span class="sim-tile__icon">' + I(sim.icono) + '</span>' +
        '<span class="badge ' + (vivo ? "badge--brand" : "badge--soon") + '">' + (vivo ? esc(M.examen(sim.examen).nombre) : "Próximamente") + '</span></div>' +
        '<h2 class="sim-tile__title">' + esc(sim.titulo) + '</h2>' +
        '<p class="sim-tile__desc">' + esc(sim.descripcion) + '</p>' +
        (vivo ? '<p class="sim-tile__facts">' + datosTxt + '</p><a class="sim-tile__link" href="#/simuladores/' + sim.id + '">' + (sim.eligeEspecialidad ? "Elegir especialidad" : "Preparar simulacro") + ' <span aria-hidden="true">→</span></a>' : "") +
        '</article>';
    }).join("");
    var hist = M.progreso.leer().sesiones.filter(function (s) { return s.tipo === "simulacro"; }).slice(0, 8);
    return cabecera("Simuladores", "Simula el examen antes de enfrentarlo", "Reloj global de 60 segundos por pregunta, sin ver respuestas hasta entregar y resultado por especialidad al final.") +
      '<div class="sims sims--app">' + tarjetas + '</div>' +
      '<section class="card card--spaced"><div class="card__head"><h2 class="card__h">Tus simulacros</h2></div>' +
      (hist.length ? listaSesiones(hist) : '<p class="muted">Cuando termines un simulacro, su resultado quedará aquí.</p>') + '</section>';
  }
  function vistaSimulador(id) {
    var sim = M.simulador(id);
    if (!sim) return vistaNoEncontrada();
    var migas = '<nav class="crumbs" aria-label="Ruta"><a href="#/simuladores">Simuladores</a><span aria-hidden="true">/</span><span aria-current="page">' + esc(sim.titulo) + '</span></nav>';
    if (sim.estado !== "disponible") {
      return migas + cabecera("Próximamente", esc(sim.titulo), esc(sim.descripcion)) +
        vacio("reloj", "Este simulador todavía no está disponible", "Se habilitará cuando su banco esté completo. Mientras tanto puedes practicar con el ENAM.", '<a class="btn btn--primary" href="#/simuladores">Ver simuladores disponibles</a>');
    }
    var elegir = "";
    var archivo = sim.eligeEspecialidad ? (simEsp[id] || "") : null;
    if (sim.eligeEspecialidad) {
      var c = conteo[sim.examen];
      elegir = '<label class="field field--select"><span class="field__label">Especialidad</span><select id="simEsp">' +
        '<option value="">Elige una especialidad</option>' +
        M.especialidades.map(function (e) {
          var t = c.porArchivo[e.archivo] || 0;
          return '<option value="' + e.archivo + '"' + (archivo === e.archivo ? " selected" : "") + (t ? "" : " disabled") + '>' + esc(e.nombre) + " (" + t + ")</option>";
        }).join("") + '</select></label>';
    }
    var d = datosSimulador(sim, archivo || null);
    var listo = !sim.eligeEspecialidad || !!archivo;
    return migas + cabecera(esc(M.examen(sim.examen).nombre), esc(sim.titulo), esc(sim.descripcion)) +
      '<div class="sim-intro">' +
        '<section class="card">' + elegir +
          '<dl class="kpis kpis--3">' +
            '<div class="kpi"><dt>Preguntas</dt><dd>' + (listo ? d.n : "—") + '</dd></div>' +
            '<div class="kpi"><dt>Tiempo</dt><dd>' + (listo ? M.duracion(d.segundos) : "—") + '</dd></div>' +
            '<div class="kpi"><dt>Especialidades</dt><dd>' + (listo ? d.especialidades : "—") + '</dd></div>' +
          '</dl>' +
          '<button class="btn btn--primary btn--lg btn--block" type="button" data-accion="simular" data-sim="' + sim.id + '"' + (listo && d.n ? "" : " disabled") + '>Comenzar simulacro' + I("flecha", "btn__arrow") + '</button>' +
        '</section>' +
        '<section class="card"><h2 class="card__h">Antes de empezar</h2><ul class="rules">' +
          '<li>El reloj corre desde que pulsas <b>Comenzar</b> y el simulacro se entrega solo al llegar a cero.</li>' +
          '<li>Puedes cambiar tus respuestas, tachar alternativas y marcar preguntas para revisarlas antes de entregar.</li>' +
          '<li>El mapa de preguntas te muestra cuáles te faltan.</li>' +
          '<li>Al terminar verás tu puntaje, el resultado por especialidad y la revisión con comentario y flujograma.</li>' +
          (sim.orden === "aleatorio" ? '<li>Las preguntas se eligen al azar en cada intento.</li>' : "") +
        '</ul></section>' +
      '</div>';
  }
  var simEsp = {};
  function enlazarSimulador(id) {
    var s = document.getElementById("simEsp");
    if (!s) return;
    s.addEventListener("change", function () { simEsp[id] = s.value; repintar("#simEsp"); });
  }
  ACCIONES.simular = function (b) {
    var sim = M.simulador(b.getAttribute("data-sim"));
    var archivo = sim.eligeEspecialidad ? simEsp[sim.id] : null;
    if (sim.eligeEspecialidad && !archivo) return;
    var d = datosSimulador(sim, archivo);
    iniciar({
      titulo: sim.titulo + (archivo ? " · " + M.especialidad(archivo).nombre : ""),
      examen: sim.examen, origen: sim.origen, archivos: archivo ? [archivo] : null,
      cantidad: sim.cantidad, orden: sim.orden, modo: "simulacro", tiempo: d.segundos,
      simulador: sim.id, volverTexto: "Salir del simulacro"
    });
  };

  /* ---------- análisis de datos del estudiante (todo sale de su propio progreso) ---------- */
  var DIA = 86400000, G = window.MQP_GRAF;
  function ymd(t) { var d = new Date(t); return d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate(); }
  function etiquetaDia(t) { try { return new Intl.DateTimeFormat("es-PE", { day: "numeric", month: "short" }).format(new Date(t)); } catch (e) { return ymd(t); } }
  function analizar() {
    var r = M.progreso.leer().respuestas, p = M.progreso.leer();
    var dias = {}, anios = {}, franjas = [0, 1, 2, 3].map(function () { return { n: 0, ok: 0 }; });
    var total = 0, ok = 0;
    for (var id in r) {
      if (!Object.prototype.hasOwnProperty.call(r, id)) continue;
      var x = r[id]; if (!x || !x.t) continue;
      total++; if (x.ok) ok++;
      var k = ymd(x.t), d = dias[k] || (dias[k] = { t: new Date(new Date(x.t).setHours(0, 0, 0, 0)).getTime(), n: 0, ok: 0 });
      d.n++; if (x.ok) d.ok++;
      var h = new Date(x.t).getHours(), f = franjas[h < 6 ? 0 : h < 12 ? 1 : h < 19 ? 2 : 3]; f.n++; if (x.ok) f.ok++;
      var q = porId[id], m = q && /(20\d\d)/.exec(q.examen || "");
      if (m) { var a = anios[m[1]] || (anios[m[1]] = { n: 0, ok: 0 }); a.n++; if (x.ok) a.ok++; }
    }
    var lista = Object.keys(dias).map(function (k) { return dias[k]; }).sort(function (a, b) { return a.t - b.t; });
    // racha: días seguidos con actividad hasta hoy (o ayer)
    var racha = 0, cur = new Date(); cur.setHours(0, 0, 0, 0);
    if (!dias[ymd(cur.getTime())]) cur = new Date(cur.getTime() - DIA);
    while (dias[ymd(cur.getTime())]) { racha++; cur = new Date(cur.getTime() - DIA); }
    var mejor = lista.slice().sort(function (a, b) { return b.n - a.n; })[0] || null;
    var sims = p.sesiones.filter(function (s) { return s.tipo === "simulacro" && s.total; }).slice().reverse();
    return { total: total, ok: ok, dias: lista, anios: anios, franjas: franjas, racha: racha, mejor: mejor, sims: sims };
  }
  function panel(titulo, nota, cuerpo, extra) {
    return '<section class="an-panel' + (extra ? " " + extra : "") + '"><h2>' + titulo + '</h2>' + (nota ? '<p class="an-nota">' + nota + '</p>' : "") + cuerpo + '</section>';
  }
  function analisisProgreso() {
    if (!G) return "";
    var A = analizar(), mal = A.total - A.ok, html = "";
    // 1 · resumen: dona + cifras
    html += '<div class="an-grid an-grid--3">' +
      '<section class="an-panel"><h2>Tus aciertos</h2><p class="an-nota">Sobre tu último intento de cada pregunta.</p>' + G.donut(A.ok, mal, { titulo: "Aciertos" }) + '</section>' +
      '<section class="an-panel"><h2>Tu constancia</h2><p class="an-nota">Actividad diaria de las últimas 12 semanas.</p>' +
        '<dl class="an-resumen"><div><dt>Racha actual</dt><dd>' + M.plural(A.racha, "día", "días") + '</dd></div>' +
        '<div><dt>Días con práctica</dt><dd>' + A.dias.length + '</dd></div>' +
        '<div><dt>Mejor día</dt><dd>' + (A.mejor ? M.plural(A.mejor.n, "pregunta", "preguntas") + " · " + esc(etiquetaDia(A.mejor.t)) : "—") + '</dd></div></dl>' +
        '<div style="margin-top:16px">' + G.calor(A.dias.map(function (d) { return { fecha: new Date(d.t), n: d.n }; }), { semanas: 12 }) + '</div></section></div>';
    // 2 · evolución diaria (línea) + volumen (columnas), cada una con su escala
    if (A.dias.length >= 2) {
      var ult = A.dias.slice(-14);
      var pts = ult.map(function (d) { var v = Math.round(d.ok / d.n * 100); return { x: etiquetaDia(d.t), y: v, n: d.n + (d.n === 1 ? " pregunta" : " preguntas"), tip: etiquetaDia(d.t) + ": " + v + "% de aciertos (" + d.ok + " de " + d.n + ")" }; });
      var primera = pts[0].y, ultima = pts[pts.length - 1].y, dif = ultima - primera;
      var insight = pts.length >= 3 ? '<p class="an-insight">' + (dif > 3 ? "Tu porcentaje subió " + dif + " puntos entre el primer y el último día mostrados." : dif < -3 ? "Tu porcentaje bajó " + Math.abs(dif) + " puntos entre el primer y el último día mostrados: conviene repasar tus falladas." : "Tu porcentaje se mantiene estable en estos días.") + '</p>' : "";
      html += '<div class="an-grid">' + panel("Evolución de tus aciertos", "% de respuestas correctas por día, en tus últimos " + pts.length + " días con práctica.", G.linea(pts, { titulo: "Aciertos por día", colX: "Día", colY: "Aciertos" }) + insight) +
        panel("Preguntas por día", "Cuántas preguntas resolviste cada día (últimos 10 días con práctica).", G.columnas(ult.slice(-10).map(function (d) { var f = new Date(d.t); return { etiqueta: f.getDate() + "/" + (f.getMonth() + 1), valor: d.n, texto: String(d.n), tip: etiquetaDia(d.t) + ": " + M.plural(d.n, "pregunta", "preguntas") }; }), { colA: "Día", colB: "Preguntas" })) + '</div>';
    }
    // 3 · por año del examen
    var anios = Object.keys(A.anios).sort();
    if (anios.length) {
      var filas = anios.map(function (a) { var v = A.anios[a], pc = Math.round(v.ok / v.n * 100); return { etiqueta: "ENAM " + a, sub: v.n + (v.n === 1 ? " respondida" : " respondidas"), valor: pc, max: 100, texto: pc + "%", tip: "ENAM " + a + ": " + pc + "% (" + v.ok + " de " + v.n + ")" }; });
      html += '<div class="an-grid">' + panel("Aciertos por año del examen", "Con qué años del ENAM rindes mejor.", G.barras(filas, { colA: "Examen", colB: "Aciertos" }));
    } else html += '<div class="an-grid">';
    // 4 · hora del día
    var nomF = ["Madrugada", "Mañana", "Tarde", "Noche"], subF = ["0–6 h", "6–12 h", "12–19 h", "19–24 h"], conDatos = A.franjas.filter(function (f) { return f.n >= 3; });
    if (A.total >= 6 && conDatos.length >= 2) {
      var best = 0; A.franjas.forEach(function (f, i) { if (f.n >= 3 && (A.franjas[best].n < 3 || f.ok / f.n > A.franjas[best].ok / A.franjas[best].n)) best = i; });
      html += panel("¿A qué hora rindes mejor?", "% de aciertos según la hora del día (solo franjas con 3 o más respuestas).",
        G.columnas(A.franjas.map(function (f, i) { var v = f.n >= 3 ? Math.round(f.ok / f.n * 100) : 0; return { etiqueta: nomF[i] + " " + subF[i], valor: v, texto: f.n >= 3 ? v + "%" : "—", tip: nomF[i] + " (" + subF[i] + "): " + (f.n >= 3 ? v + "% en " + f.n + " respuestas" : "pocas respuestas (" + f.n + ")") }; }), { max: 100, colA: "Franja", colB: "Aciertos" }) +
        '<p class="an-insight">Tu mejor franja hasta ahora: <b>' + nomF[best].toLowerCase() + '</b> (' + Math.round(A.franjas[best].ok / A.franjas[best].n * 100) + '% de aciertos).</p>');
    }
    html += '</div>';
    // 5 · simulacros
    if (A.sims.length >= 2) {
      var sp = A.sims.slice(-12).map(function (s) { var v = Math.round(s.correctas / s.total * 100); return { x: etiquetaDia(s.t), y: v, n: s.correctas + " de " + s.total, tip: s.titulo + " · " + etiquetaDia(s.t) + ": " + v + "% (" + s.correctas + " de " + s.total + ")" }; });
      html += '<div class="an-grid">' + panel("Evolución de tus simulacros", "Puntaje de cada simulacro terminado, del más antiguo al más reciente.", G.linea(sp, { titulo: "Puntaje de simulacros", colX: "Fecha", colY: "Puntaje" }), "an-panel--ancho") + '</div>';
    } else if (A.sims.length === 1) {
      html += '<div class="an-grid">' + panel("Evolución de tus simulacros", "", '<p class="an-vacio">Terminaste 1 simulacro. Con el siguiente verás aquí cómo evoluciona tu puntaje.</p>', "an-panel--ancho") + '</div>';
    }
    return html;
  }

  /* ---------- Mi progreso ---------- */
  var MINIMO = 3;   // respuestas mínimas en una especialidad para juzgarla
  /* ---------- Rendimiento y plan de estudio (rendimiento.js: estadística descriptiva, sin nota proyectada) ---------- */
  function panelRendimiento() {
    if (!M.rendimiento) return "";
    var p = M.progreso.leer();
    var R = M.rendimiento.calcular(datos.preguntas, p.respuestas, p.sesiones, Date.now());
    if (!R.global.n) return "";
    var G1 = R.global, E = R.estimacion;
    var sim = R.simulacros.length ? R.simulacros[R.simulacros.length - 1] : null;
    var bloqueEst = E.suficiente
      ? '<p class="rd__big">' + E.rango[0] + '–' + E.rango[1] + ' %</p><p class="rd__sub">de aciertos esperados en preguntas parecidas a las del banco (intervalo de confianza del 95 %).' +
        (E.tendencia ? ' Tus simulacros ' + (E.tendencia > 0 ? "mejoran" : "bajan") + ' ' + Math.abs(E.tendencia) + ' puntos entre la primera y la segunda mitad.' : "") + '</p>'
      : '<p class="rd__big rd__big--off">Todavía necesitamos más resultados para estimar tu desempeño</p><p class="rd__sub">Para hacerlo falta: ' + E.faltan.map(esc).join(" y ") + '.</p>';
    var h = '<section class="card card--spaced rd"><div class="card__head"><h2 class="card__h">Tu rendimiento, con los datos que hay</h2></div>' +
      '<div class="rd__grid">' +
        '<div class="rd__c"><p class="rd__t">1 · Aciertos actuales</p><p class="rd__big">' + G1.pct + ' %</p><p class="rd__sub">' + G1.ok + ' de ' + G1.n + ' en tu último intento de cada pregunta. Rango plausible: ' + G1.lo + '–' + G1.hi + ' %. Cubres el ' + G1.cobertura + ' % del banco.</p></div>' +
        '<div class="rd__c"><p class="rd__t">2 · Simulacros recientes</p>' + (sim ? '<p class="rd__big">' + sim.pct + ' %</p><p class="rd__sub">Último simulacro (' + sim.ok + ' de ' + sim.total + '). Simulacros contados: ' + R.simulacros.length + '.</p>' : '<p class="rd__big rd__big--off">Sin simulacros completos</p><p class="rd__sub">Cuentan los de al menos 20 preguntas.</p>') + '</div>' +
        '<div class="rd__c"><p class="rd__t">3 · Estimación a futuro</p>' + bloqueEst + '</div>' +
        '<div class="rd__c"><p class="rd__t">4 · Incertidumbre</p><p class="rd__sub">Los rangos se calculan con intervalos de Wilson: con pocas respuestas son amplios y se estrechan al practicar. Es una estimación estadística, <b>no una nota</b> ni una promesa: no convertimos tu % a la escala del ENAM porque esa relación no está validada.</p></div>' +
      '</div></section>';
    var plan = R.plan.map(function (z, i) {
      var temas = z.temas.length ? '<p class="rd__temas">Temas con más errores: ' + z.temas.map(function (t) { return esc(t.tema) + ' (' + t.falladas.length + ')'; }).join(" · ") + '</p>' : "";
      return '<li class="rd__item"><span class="rd__n">' + (i + 1) + '</span><div><h3>' + esc(z.nombre) + '</h3><ul class="rd__why">' + z.motivos.map(function (m) { return '<li>' + esc(m) + '</li>'; }).join("") + '</ul>' + temas +
        '<p class="rd__meta">' + esc(z.meta) + '</p><div class="rd__btn">' +
        (z.falladas.length ? '<button class="btn btn--primary btn--sm" type="button" data-accion="refuerzo" data-archivo="' + esc(z.archivo) + '" data-modo="falladas">Repasar mis ' + z.falladas.length + ' falladas</button>' : "") +
        '<button class="btn btn--ghost btn--sm" type="button" data-accion="refuerzo" data-archivo="' + esc(z.archivo) + '" data-modo="banco">Practicar la especialidad</button>' +
        '<a class="btn btn--ghost btn--sm" href="#/flashcards">Mis flashcards</a></div></div></li>';
    }).join("");
    return h + '<section class="card card--spaced rd"><div class="card__head"><h2 class="card__h">Qué estudiar primero</h2><span class="muted small">Prioridad = bajo acierto + peso en el banco + pocos datos + tiempo sin practicar</span></div><ol class="rd__plan">' + plan + '</ol>' +
      '<p class="muted small card__note">«Peso» es el tamaño de la especialidad en este banco, no el blueprint oficial del examen. Las metas son orientativas.</p></section>';
  }
  ACCIONES.refuerzo = function (b) {
    var esp = M.especialidad(b.getAttribute("data-archivo")); if (!esp) return;
    if (b.getAttribute("data-modo") === "falladas") {
      var ids = idsFalladas().filter(function (id) { return porId[id] && porId[id].archivo === esp.archivo; });
      if (ids.length) { iniciar({ titulo: "Refuerzo · " + esp.nombre, ids: ids, volverTexto: "Volver a mi progreso", noGuardar: true }); return; }
    }
    iniciar({ titulo: esp.nombre, archivos: [esp.archivo], examen: "enam", volverTexto: "Volver a mi progreso" });
  };

  function vistaProgreso() {
    var res = M.progreso.resumen();
    var p = M.progreso.leer();
    if (!res.respondidas) {
      return cabecera("Mi progreso", "Tu progreso", "Aquí verás tus aciertos por especialidad, tus fortalezas y lo que te conviene reforzar.") +
        vacio("grafico", "Todavía no hay datos", "Resuelve tus primeras preguntas y esta sección se llenará con tus propios resultados.", '<a class="btn btn--primary" href="#/examenes/enam">Empezar con el ENAM</a>');
    }
    var filas = [];
    for (var k = 0; k < M.especialidades.length; k++) {
      var e = M.especialidades[k], r = res.porArchivo[e.archivo];
      var total = 0;
      for (var x in conteo) total += conteo[x].porArchivo[e.archivo] || 0;
      filas.push({ esp: e, total: total, respondidas: r ? r.respondidas : 0, correctas: r ? r.correctas : 0, pct: r ? pct(r.correctas, r.respondidas) : null });
    }
    var juzgables = filas.filter(function (f) { return f.respondidas >= MINIMO; });
    var fuertes = juzgables.slice().sort(function (a, b) { return b.pct - a.pct || b.respondidas - a.respondidas; }).slice(0, 3);
    var debiles = juzgables.slice().sort(function (a, b) { return a.pct - b.pct || b.respondidas - a.respondidas; }).slice(0, 3);
    function mini(lista, clase) {
      if (!lista.length) return '<p class="muted">Responde al menos ' + MINIMO + ' preguntas de una especialidad para verla aquí.</p>';
      return '<ul class="rank">' + lista.map(function (f) {
        return '<li class="rank__item"><span>' + esc(f.esp.nombre) + '</span><b class="' + clase + '">' + f.pct + '%</b><small>' + f.correctas + "/" + f.respondidas + '</small></li>';
      }).join("") + '</ul>';
    }
    var tabla = '<ul class="bars bars--wide bars--table">' + filas.filter(function (f) { return f.respondidas; }).sort(function (a, b) { return b.respondidas - a.respondidas; }).map(function (f) {
      return '<li class="bars__row" title="' + esc(f.esp.nombre) + ': ' + f.correctas + ' de ' + f.respondidas + ' correctas">' +
        '<span class="bars__label">' + esc(f.esp.nombre) + '<small>' + f.respondidas + " de " + f.total + ' respondidas</small></span>' +
        '<span class="bars__track"><span class="bars__fill" style="--v:' + f.pct + '"></span></span>' +
        '<span class="bars__val">' + f.pct + '%</span></li>';
    }).join("") + '</ul>';
    var sinTocar = filas.filter(function (f) { return !f.respondidas && f.total; });
    var simulacros = p.sesiones.filter(function (s) { return s.tipo === "simulacro"; }).length;
    return cabecera("Mi progreso", "Tu progreso", "Calculado con tus propias respuestas. Por ahora se guarda solo en este navegador.") +
      '<dl class="kpis kpis--4">' +
        '<div class="kpi"><dt>Preguntas respondidas</dt><dd>' + M.miles(res.respondidas) + '<small> / ' + M.miles(datos.preguntas.length) + '</small></dd></div>' +
        '<div class="kpi"><dt>Correctas</dt><dd>' + M.miles(res.correctas) + '</dd></div>' +
        '<div class="kpi"><dt>Aciertos</dt><dd>' + res.porcentaje + '%</dd></div>' +
        '<div class="kpi"><dt>Simulacros terminados</dt><dd>' + simulacros + '</dd></div>' +
      '</dl>' +
      analisisProgreso() +
      panelRendimiento() +
      '<div class="grid-2 card--spaced">' +
        '<section class="card"><div class="card__head"><h2 class="card__h">Áreas fuertes</h2></div>' + mini(fuertes, "is-ok") + '</section>' +
        '<section class="card"><div class="card__head"><h2 class="card__h">Áreas por reforzar</h2>' + (debiles.length ? '<a class="link-arrow" href="#/falladas">Repasar falladas <span aria-hidden="true">→</span></a>' : "") + '</div>' + mini(debiles, "is-bad") + '</section>' +
      '</div>' +
      '<section class="card card--spaced"><div class="card__head"><h2 class="card__h">Aciertos por especialidad</h2><span class="muted small">% de aciertos en tu último intento de cada pregunta</span></div>' + tabla +
        (sinTocar.length ? '<p class="muted small card__note">Sin empezar: ' + sinTocar.map(function (f) { return esc(f.esp.nombre); }).join(" · ") + '</p>' : "") + '</section>' +
      '<section class="card card--spaced"><div class="card__head"><h2 class="card__h">Actividad reciente</h2></div>' +
        (p.sesiones.length ? listaSesiones(p.sesiones.slice(0, 10)) : '<p class="muted">Aún no terminaste ninguna sesión.</p>') + '</section>';
  }

  /* ---------- Falladas y favoritas ---------- */
  function listaPreguntas(ids, accion, conRespuesta) {
    var r = M.progreso.leer().respuestas;
    return '<ul class="qlist">' + ids.map(function (id) {
      var q = porId[id], resp = r[id];
      return '<li class="qitem">' +
        '<div class="qitem__meta"><span class="tag">' + esc(q.especialidad) + '</span>' + (q.tema ? '<span class="tag tag--tema">' + esc(q.tema) + '</span>' : "") + '<span class="qitem__id">' + esc(q.id) + '</span></div>' +
        '<p class="qitem__stem">' + esc(recorte(q.enunciado, 180)) + '</p>' +
        '<div class="qitem__foot">' +
          (conRespuesta && resp ? '<span class="qitem__ans">Tu respuesta: <b class="is-bad">' + esc(resp.l) + '</b> · Correcta: <b class="is-ok">' + esc(q.clave) + '</b></span>' : '<span class="qitem__ans">' + esc(q.examen) + '</span>') +
          '<button class="btn btn--ghost btn--sm" type="button" data-accion="' + accion + '" data-id="' + esc(id) + '">Practicar</button>' +
        '</div></li>';
    }).join("") + '</ul>';
  }
  function vistaFalladas() {
    var ids = idsFalladas();
    if (!ids.length) {
      return cabecera("Seguimiento", "Preguntas falladas", "Las preguntas cuyo último intento fue incorrecto.") +
        vacio("check", "No tienes preguntas falladas", "Cuando falles una pregunta aparecerá aquí para que la repases. Si luego la respondes bien, sale de la lista.", '<a class="btn btn--primary" href="#/banco">Ir al banco</a>');
    }
    return cabecera("Seguimiento", "Preguntas falladas", "Las preguntas cuyo último intento fue incorrecto. Al acertarlas, salen de la lista.",
      '<div class="page-head__actions"><button class="btn btn--primary" type="button" data-accion="falladas">Repasar ' + M.plural(ids.length, "pregunta", "preguntas") + I("flecha", "btn__arrow") + '</button></div>') +
      listaPreguntas(ids, "falladas", true);
  }
  function vistaFavoritas() {
    var ids = idsFavoritas();
    if (!ids.length) {
      return cabecera("Seguimiento", "Favoritas", "Las preguntas que guardaste con la estrella.") +
        vacio("estrella", "Aún no guardaste preguntas", "Pulsa la estrella en cualquier pregunta del banco o de un simulacro para guardarla aquí.", '<a class="btn btn--primary" href="#/banco">Ir al banco</a>');
    }
    return cabecera("Seguimiento", "Favoritas", "Las preguntas que guardaste con la estrella.",
      '<div class="page-head__actions"><button class="btn btn--primary" type="button" data-accion="favoritas">Practicar ' + M.plural(ids.length, "favorita", "favoritas") + I("flecha", "btn__arrow") + '</button></div>') +
      listaPreguntas(ids, "favoritas", false);
  }

  /* ---------- Perfil ---------- */
  function listaPlanes(u) {
    var EX = (CUENTA.estado && CUENTA.estado.examenes) || {}, subs = u.suscripciones || {}, ks = Object.keys(subs);
    if (!ks.length) return '<span class="badge">Plan gratuito</span>';
    return ks.map(function (k) { return '<span class="badge badge--ok">' + esc((EX[k] && EX[k].nombre) || k) + ' · ' + esc(subs[k].plan) + '</span> <span class="muted small">hasta el ' + esc(fechaLarga(subs[k].hasta)) + '</span>'; }).join("<br>");
  }
  function tarjetaCuenta() {
    if (!CUENTA.disponible) return '<p class="muted">Las cuentas no están disponibles ahora. Tu progreso se guarda solo en este navegador.</p>';
    var u = CUENTA.usuario;
    if (!u) return '<p class="muted">Crea una cuenta gratis para activar un plan Premium. Tu progreso sigue guardándose en este navegador.</p><div class="card__actions"><a class="btn btn--primary" href="#/registro">Crear cuenta</a><a class="btn btn--ghost" href="#/ingresar">Ingresar</a></div>';
    return '<p><b>' + esc(u.nombre) + '</b><br><span class="muted">' + esc(u.correo) + '</span></p>' +
      '<p>' + listaPlanes(u) + '</p>' +
      '<p class="muted small">' + (SYNC.error ? "No pudimos guardar tu progreso en la cuenta; se reintentará con tu próxima respuesta." : "Tu progreso se guarda en tu cuenta" + (SYNC.ultimo ? " · sincronizado a las " + new Date(SYNC.ultimo).toLocaleTimeString("es-PE", { hour: "2-digit", minute: "2-digit" }) : "") + ".") + '</p>' +
      '<div class="card__actions"><a class="btn btn--primary" href="#/planes">' + (u.premium ? "Renovar o cambiar plan" : "Ver planes") + '</a><button class="btn btn--ghost" type="button" data-accion="salir">Cerrar sesión</button></div>' +
      (u.dueno ? '<p><span class="badge badge--ok">Cuenta del dueño</span> <span class="muted small">acceso a todos los exámenes</span></p>' : "") +
      '<details class="datos-cuenta"><summary>Mis datos y privacidad</summary>' +
        '<p class="muted small">Puedes descargar todo lo que guardamos de ti o eliminar tu cuenta. Más detalles en la <a href="../privacidad.html" target="_blank" rel="noopener">Política de privacidad</a>.</p>' +
        '<div class="card__actions"><button class="btn btn--ghost btn--sm" type="button" data-accion="exportar">Descargar mis datos</button><button class="btn btn--ghost btn--sm btn--danger" type="button" data-accion="eliminar">Eliminar mi cuenta</button></div>' +
        '<div id="elimForm" class="elim" hidden><p class="small">Se borrarán tu cuenta y tu progreso guardado. Tu plan Premium activo se perderá y no hay reembolso automático. Esto no se puede deshacer.</p>' +
        '<label class="field"><span class="field__label">Tu contraseña</span><input type="password" id="elimClave" autocomplete="current-password"></label>' +
        '<button class="btn btn--primary btn--sm btn--danger" type="button" data-accion="eliminarOk">Eliminar definitivamente</button></div>' +
        '<p class="form-error" id="cuentaMsg" role="alert" hidden></p></details>' +
      (u.dueno ? "" : '<details class="datos-cuenta"><summary>Soy el dueño del sitio</summary><p class="muted small">Con la clave de administración (MQP_ADMIN_TOKEN) esta cuenta tendrá todos los exámenes sin pagar.</p>' +
        '<label class="field"><span class="field__label">Clave de administración</span><input type="password" id="duenoClave" autocomplete="off"></label>' +
        '<button class="btn btn--ghost btn--sm" type="button" data-accion="duenoActivar">Activar</button><p class="form-error" id="duenoMsg" role="alert" hidden></p></details>');
  }
  function vistaPerfil() {
    var p = M.progreso.leer();
    var ex = examenPreferido();
    var nRes = Object.keys(p.respuestas).length, nFav = Object.keys(p.favoritos).length;
    return cabecera("Perfil", "Tu perfil", "Preferencias y datos de estudio de este navegador.") +
      '<div class="grid-2">' +
        '<section class="card"><h2 class="card__h">Examen que preparas</h2><p class="muted small">Se usa para el inicio y el banco de preguntas.</p>' +
          '<div class="picks picks--stack" id="pfExamen">' + M.examenes.map(function (e) {
            return opcion("pfExamen", e.id, e.nombre, e.estado === "disponible" ? "Banco disponible" : "Próximamente", ex === e.id, false);
          }).join("") + '</div></section>' +
        '<section class="card"><h2 class="card__h">Cuenta</h2>' + tarjetaCuenta() + '</section>' +
      '</div>' +
      '<section class="card card--spaced"><h2 class="card__h">Datos guardados en este navegador</h2>' +
        '<dl class="kpis kpis--3"><div class="kpi"><dt>Preguntas respondidas</dt><dd>' + nRes + '</dd></div>' +
        '<div class="kpi"><dt>Favoritas</dt><dd>' + nFav + '</dd></div>' +
        '<div class="kpi"><dt>Sesiones</dt><dd>' + p.sesiones.length + '</dd></div></dl>' +
        '<div class="danger"><p>Borrar el progreso elimina respuestas, favoritas y sesiones de este navegador. No se puede deshacer.</p>' +
        '<button class="btn btn--ghost btn--danger" type="button" data-accion="borrar"' + (nRes || nFav || p.sesiones.length ? "" : " disabled") + '>Borrar mi progreso</button></div>' +
      '</section>';
  }
  function enlazarPerfil() {
    var g = document.getElementById("pfExamen");
    if (g) g.addEventListener("change", function (ev) {
      M.progreso.preferencia("examen", ev.target.value);
      conf.examen = null;
      pintarChrome();
    });
  }
  ACCIONES.borrar = function (b) {
    if (b.getAttribute("data-armado") !== "1") {
      b.setAttribute("data-armado", "1");
      b.classList.add("is-armed");
      b.textContent = "Pulsa otra vez para borrar";
      setTimeout(function () { if (b.isConnected) { b.removeAttribute("data-armado"); b.classList.remove("is-armed"); b.textContent = "Borrar mi progreso"; } }, 4000);
      return;
    }
    M.progreso.borrar();
    render();
  };

  /* ---------- Planes ---------- */
  var ORDEN_EX = ["essalud", "enam", "residentado", "encaps"];
  function vistaPlanes() {
    var EX = (CUENTA.estado && CUENTA.estado.examenes) || null, PER = (CUENTA.estado && CUENTA.estado.periodos) || null;
    var motivo = parametros.motivo, pago = parametros.pago;
    var aviso = "";
    if (motivo === "limite") aviso = '<div class="notice notice--warn" role="status"><b>Llegaste al límite de hoy.</b> El plan gratuito incluye ' + CUENTA.estado.limite_diario + ' preguntas por día. Con un plan sigues sin límite.</div>';
    else if (motivo === "simulacro") aviso = '<div class="notice notice--warn" role="status"><b>El simulacro ENAM 2020 completo es de pago.</b> Con el plan gratuito puedes usar el simulacro rápido y el de especialidad.</div>';
    if (pago === "pendiente") aviso = '<div class="notice" role="status"><b>Tu pago está pendiente.</b> Cuando la pasarela lo confirme, tu plan se activa solo. Puede tardar unos minutos.</div>';
    if (pago === "error") aviso = '<div class="notice notice--bad" role="alert"><b>No se completó el pago.</b> No se te cobró nada. Puedes intentarlo de nuevo.</div>';
    if (!CUENTA.disponible || !EX || !PER) {
      return cabecera("Planes", "Planes", "Los planes se activarán en cuanto el servidor de cuentas esté disponible.") +
        vacio("candado", "Todavía no hay planes disponibles", "Mientras tanto toda la plataforma sigue siendo de acceso libre.", '<a class="btn btn--primary" href="#/inicio">Ir al inicio</a>');
    }
    var pagos = CUENTA.estado.pagos, u = CUENTA.usuario;
    var subs = (u && u.suscripciones) || {}, espera = (u && u.espera) || [];
    var sel = EX[parametros.examen] ? parametros.examen : (EX[examenPreferido()] ? examenPreferido() : "enam");
    var ex = EX[sel];
    var tabs = '<nav class="chips chips--wrap plan-tabs" aria-label="Examen del plan">' + ORDEN_EX.filter(function (k) { return EX[k]; }).map(function (k) {
      return '<a class="chip"' + (k === sel ? ' aria-current="true"' : "") + ' href="#/planes?examen=' + k + '">' + esc(EX[k].nombre) + (subs[k] ? " ✓" : "") + '</a>';
    }).join("") + '</nav>';
    var vigente = subs[sel] ? '<div class="notice notice--ok" role="status"><b>Tu plan ' + esc(subs[sel].plan) + ' de ' + esc(ex.nombre) + ' está activo</b> hasta el ' + esc(fechaLarga(subs[sel].hasta)) + '. Si compras otro periodo, se suma al que ya tienes.</div>' : "";
    var comunes = ex.abierto
      ? ["Preguntas ilimitadas, sin tope diario", "Simulacro ENAM 2020 completo", "Todos los simuladores y el tutor de IA", "Comentario docente y flujograma en cada pregunta", "Progreso, falladas y favoritas"]
      : ["Banco de " + ex.nombre + " en construcción", "Simuladores y tutor de IA incluidos", "Comentario docente y flujograma", "Te avisamos apenas abra"];
    function tarjeta(id, destacado, insignia) {
      var per = PER[id], precio = ex.precios[id], mes = precio / (per.dias / 30);
      var etiqueta = id === "mensual" ? "por 30 días" : id === "trimestral" ? "por 3 meses · " + soles(Math.round(mes * 100) / 100) + "/mes" : "por 12 meses · " + soles(Math.round(mes * 100) / 100) + "/mes";
      var boton = !ex.abierto ? '<button class="btn btn--ghost btn--lg btn--block" type="button" disabled>Próximamente</button>'
        : '<button class="btn ' + (destacado ? "btn--primary" : "btn--ghost") + ' btn--lg btn--block" type="button" data-accion="comprar" data-examen="' + sel + '" data-plan="' + id + '"' + (pagos ? "" : " disabled") + '>' + (pagos ? (subs[sel] ? "Renovar" : "Elegir este plan") : "Cobro próximamente") + '</button>';
      return '<article class="plan' + (destacado ? " plan--pro" : "") + '">' + (insignia ? '<span class="plan__badge">' + insignia + '</span>' : "") +
        '<h2 class="plan__name">' + esc(per.nombre.charAt(0).toUpperCase() + per.nombre.slice(1)) + '</h2>' +
        '<p class="plan__price"><span class="plan__amount">' + soles(precio) + '</span><span class="plan__per">' + etiqueta + '</span></p>' + boton +
        '<ul class="plan__list">' + comunes.map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + '</ul></article>';
    }
    var gratis = '<article class="plan"><h2 class="plan__name">Gratis</h2><p class="plan__price"><span class="plan__amount">S/ 0</span><span class="plan__per">sin tarjeta</span></p>' +
      (u ? '<span class="btn btn--ghost btn--lg btn--block is-static">' + (subs[sel] ? "Incluido" : "Tu plan actual") + '</span>' : '<a class="btn btn--ghost btn--lg btn--block" href="#/registro">Crear cuenta gratis</a>') +
      '<ul class="plan__list"><li>' + (CUENTA.estado.limites ? CUENTA.estado.limite_diario + " preguntas por día" : "Banco por especialidad") + '</li><li>Simulacro rápido y por especialidad</li><li>Comentario docente y flujograma</li><li>Progreso, falladas y favoritas</li></ul></article>';
    var cierre = ex.abierto ? "" :
      '<div class="notice" role="status"><b>El banco de ' + esc(ex.nombre) + ' todavía no está publicado.</b> Por eso no lo vendemos aún. ' +
      (espera.indexOf(sel) >= 0 ? 'Ya estás en la lista de espera: te avisamos al abrir.' : (u ? '<button class="btn btn--primary btn--sm" type="button" data-accion="espera" data-examen="' + sel + '">Avisarme cuando abra</button>' : '<a class="btn btn--primary btn--sm" href="#/registro">Crea tu cuenta para que te avisemos</a>')) + '</div>';
    return cabecera("Planes", "Elige tu examen y tu plan", "Cada examen tiene sus propios planes. Pago único por periodo, sin renovación automática, en soles.") +
      aviso + tabs + vigente + cierre + '<div class="plans plans--app">' + gratis + tarjeta("mensual", false, "") + tarjeta("trimestral", true, "Más elegido") + tarjeta("anual", false, "Mejor precio") + '</div>' +
      '<p class="muted small plans__foot" id="planError" role="alert" hidden></p>' +
      '<p class="muted small plans__foot">El cobro lo procesa ' + (CUENTA.estado.pasarela === "payu" ? "PayU" : "Mercado Pago") + ': MedQuizPlus no ve ni guarda los datos de tu tarjeta.</p>';
  }
  ACCIONES.espera = function (b) {
    api("espera", { examen: b.getAttribute("data-examen") }).then(function (r) {
      if (r.ok) { CUENTA.usuario = r.j.usuario; render(true); }
    });
  };
  ACCIONES.comprar = function (b) {
    var plan = b.getAttribute("data-plan"), examen = b.getAttribute("data-examen") || "enam";
    if (!CUENTA.usuario) { location.hash = "#/registro?plan=" + plan + "&examen=" + examen; return; }
    var err = document.getElementById("planError"), txt = b.textContent;
    err.hidden = true; b.disabled = true; b.textContent = "Abriendo el pago…";
    api("comprar", { examen: examen, plan: plan }).then(function (r) {
      if (r.ok && r.j.form) {                       // PayU: se envía un formulario a su pantalla de pago
        var f = document.createElement("form"); f.method = "POST"; f.action = r.j.form.action;
        Object.keys(r.j.form.fields).forEach(function (k) { var i = document.createElement("input"); i.type = "hidden"; i.name = k; i.value = r.j.form.fields[k]; f.appendChild(i); });
        document.body.appendChild(f); f.submit(); return;
      }
      if (r.ok && r.j.url) { location.href = r.j.url; return; }
      throw new Error(r.j.error || "No pudimos iniciar el pago.");
    }).catch(function (e) {
      b.disabled = false; b.textContent = txt; err.textContent = e.message || "No pudimos iniciar el pago."; err.hidden = false;
    });
  };

  /* ---------- Ingresar / Crear cuenta ---------- */
  function campo(id, etiqueta, tipo, extra) {
    return '<div class="field"><label for="' + id + '">' + etiqueta + '</label><input id="' + id + '" name="' + id + '" type="' + tipo + '" ' + (extra || "") + '></div>';
  }
  function vistaAuth(modo) {
    if (!CUENTA.disponible) {
      return cabecera("Cuenta", "Cuentas no disponibles", "El servidor de cuentas no responde ahora. La plataforma sigue funcionando sin cuenta.") +
        vacio("candado", "No pudimos conectar con el servidor", "Revisa tu conexión y vuelve a intentarlo.", '<a class="btn btn--primary" href="#/inicio">Ir al inicio</a>');
    }
    if (CUENTA.usuario) { return cabecera("Cuenta", "Ya iniciaste sesión", "Entraste como " + esc(CUENTA.usuario.nombre) + ".", '<div class="page-head__actions"><a class="btn btn--primary" href="#/inicio">Ir al inicio</a></div>'); }
    var reg = modo === "registro";
    return cabecera("Cuenta", reg ? "Crea tu cuenta" : "Ingresa a tu cuenta", reg ? "Gratis y sin tarjeta. Guarda tu cuenta para pasar a Premium cuando quieras." : "Con tu correo y tu contraseña.") +
      '<div class="auth card"><form id="authForm" novalidate>' +
      (reg ? campo("a-nombre", "Nombre y apellido", "text", 'autocomplete="name" maxlength="80" required') : "") +
      campo("a-correo", "Correo electrónico", "email", 'autocomplete="email" maxlength="120" required') +
      campo("a-clave", "Contraseña" + (reg ? " (mínimo 8 caracteres)" : ""), "password", 'autocomplete="' + (reg ? "new-password" : "current-password") + '" minlength="8" maxlength="200" required') +
      (reg ? '<div class="field"><label for="a-uni">Universidad (opcional)</label><select id="a-uni" name="a-uni">' + (window.MQP_UNIVERSIDADES ? window.MQP_UNIVERSIDADES.opciones() : '<option value="">—</option>') + '</select></div>' : "") +
      (reg ? '<div class="field"><label>¿Qué examen preparas?</label><div class="picks picks--row">' + ["essalud|EsSalud", "enam|ENAM", "residentado|Residentado", "encaps|ENCAPS SERUMS"].map(function (x, i) { var p = x.split("|"); return opcion("a-examen", p[0], p[1], "", p[0] === "enam", false); }).join("") + '</div></div>' : "") +
      (reg ? '<label class="check"><input type="checkbox" id="a-acepto"><span>He leído y acepto la <a href="../privacidad.html" target="_blank" rel="noopener">Política de privacidad</a> y los <a href="../terminos.html" target="_blank" rel="noopener">Términos y condiciones</a>.</span></label>' : "") +
      '<p class="form-error" id="authError" role="alert" hidden></p>' +
      '<button class="btn btn--primary btn--lg btn--block" type="submit">' + (reg ? "Crear mi cuenta" : "Ingresar") + '</button></form>' +
      '<p class="auth__alt">' + (reg ? '¿Ya tienes cuenta? <a href="#/ingresar">Ingresa</a>' : '¿Primera vez? <a href="#/registro">Crea tu cuenta gratis</a>') + '</p></div>';
  }
  function enlazarAuth(modo) {
    var f = document.getElementById("authForm"); if (!f) return;
    var err = document.getElementById("authError"), btn = f.querySelector("button[type=submit]");
    f.addEventListener("submit", function (ev) {
      ev.preventDefault(); err.hidden = true;
      var d = { correo: f.querySelector("#a-correo").value.trim(), clave: f.querySelector("#a-clave").value };
      if (modo === "registro") { d.nombre = f.querySelector("#a-nombre").value.trim(); d.universidad = f.querySelector("#a-uni").value; d.acepto = f.querySelector("#a-acepto").checked; var x = f.querySelector("input[name=a-examen]:checked"); d.examen = x ? x.value : ""; }
      if (modo === "registro" && !d.acepto) { err.textContent = "Para crear tu cuenta debes aceptar la política de privacidad y los términos y condiciones."; err.hidden = false; return; }
      if (!d.correo || d.clave.length < 8 || (modo === "registro" && d.nombre.length < 2)) { err.textContent = modo === "registro" ? "Completa tu nombre, un correo válido y una contraseña de al menos 8 caracteres." : "Escribe tu correo y tu contraseña."; err.hidden = false; return; }
      var txt = btn.textContent; btn.disabled = true; btn.textContent = "Un momento…";
      api(modo === "registro" ? "registro" : "ingresar", d).then(function (r) {
        if (!r.ok) throw new Error(r.j.error || "No se pudo completar.");
        CUENTA.usuario = r.j.usuario;
        if (d.examen) M.progreso.preferencia("examen", d.examen);
        sincronizar();
        var plan = parametros.plan;
        location.hash = plan ? "#/planes?plan=" + encodeURIComponent(plan) + (parametros.examen ? "&examen=" + encodeURIComponent(parametros.examen) : "") : "#/inicio";
      }).catch(function (e) {
        btn.disabled = false; btn.textContent = txt; err.textContent = e.message || "No se pudo completar."; err.hidden = false;
      });
    });
  }
  function cerrarLocal() { CUENTA.usuario = null; SYNC.ultimo = 0; M.progreso.descartar(); location.hash = "#/inicio"; render(); }
  ACCIONES.salir = function () {
    // se guarda lo último en la cuenta y se quita el progreso de este dispositivo (puede ser un equipo compartido)
    empujar().then(function () { return api("salir", {}); }).then(cerrarLocal).catch(cerrarLocal);
  };
  ACCIONES.exportar = function (b) {
    b.disabled = true;
    api("exportar", {}).then(function (r) {
      if (!r.ok) throw new Error(r.j.error || "No se pudo descargar.");
      var blob = new Blob([JSON.stringify(r.j, null, 2)], { type: "application/json" }), a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = "mis-datos-medquizplus.json"; document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
    }).catch(function (e) { var m = document.getElementById("cuentaMsg"); if (m) { m.textContent = e.message; m.hidden = false; } })
      .then(function () { b.disabled = false; });
  };
  ACCIONES.duenoActivar = function (b) {
    var m = document.getElementById("duenoMsg"), t = document.getElementById("duenoClave").value; m.hidden = true;
    if (!t) { m.textContent = "Escribe la clave."; m.hidden = false; return; }
    b.disabled = true;
    api("dueno_activar", { token: t }).then(function (r) { if (!r.ok) throw new Error(r.j.error || "No se pudo activar."); CUENTA.usuario = r.j.usuario; render(true); })
      .catch(function (e) { m.textContent = e.message; m.hidden = false; }).then(function () { b.disabled = false; });
  };
  ACCIONES.eliminar = function () { var f = document.getElementById("elimForm"); if (f) { f.hidden = !f.hidden; if (!f.hidden) document.getElementById("elimClave").focus(); } };
  ACCIONES.eliminarOk = function (b) {
    var clave = document.getElementById("elimClave").value, m = document.getElementById("cuentaMsg");
    if (!clave) { m.textContent = "Escribe tu contraseña para confirmar."; m.hidden = false; return; }
    b.disabled = true;
    api("eliminar", { clave: clave }).then(function (r) {
      if (!r.ok) throw new Error(r.j.error || "No se pudo eliminar.");
      cerrarLocal();
    }).catch(function (e) { b.disabled = false; m.textContent = e.message; m.hidden = false; });
  };

  function vistaNoEncontrada() {
    return vacio("capas", "No encontramos esta sección", "Puede que el enlace haya cambiado.", '<a class="btn btn--primary" href="#/inicio">Ir al inicio</a>');
  }

  /* ======================================================================
     Enrutador
     ====================================================================== */
  var RUTAS = {
    inicio: { titulo: "Inicio", vista: vistaInicio, alMontar: esperarPago },
    noencontrada: { titulo: "No encontrada", vista: vistaNoEncontrada },
    planes: { titulo: "Planes", vista: vistaPlanes },
    anatomia: { titulo: "Atlas de anatomía", vista: function () { return M.anatomia ? M.anatomia.pagina(parametros) : ""; } },
    ingresar: { titulo: "Ingresar", vista: function () { return vistaAuth("ingresar"); }, alMontar: function () { enlazarAuth("ingresar"); } },
    registro: { titulo: "Crear cuenta", vista: function () { return vistaAuth("registro"); }, alMontar: function () { enlazarAuth("registro"); } },
    examenes: { titulo: "Exámenes", vista: function (arg) { return arg ? vistaExamen(arg) : vistaExamenes(); }, alMontar: function (arg) { if (arg && M.examen(arg)) { montarTarjetas(arg); enlazarFiltros(arg); } } },
    banco: { titulo: "Banco de preguntas", vista: function (arg) { return arg === "configurar" ? vistaBanco() : vistaBancos(); }, alMontar: function (arg) { if (arg === "configurar") enlazarBanco(); } },
    simuladores: { titulo: "Simuladores", vista: function (arg) { return arg ? vistaSimulador(arg) : vistaSimuladores(); }, alMontar: function (arg) { if (arg) enlazarSimulador(arg); } },
    progreso: { titulo: "Mi progreso", vista: vistaProgreso },
    falladas: { titulo: "Preguntas falladas", vista: vistaFalladas },
    favoritas: { titulo: "Favoritas", vista: vistaFavoritas },
    guardia: { titulo: "Sobrevive a la Guardia", vista: function () { return '<div id="gdRaiz"></div>'; }, alMontar: function (arg) { var r = document.getElementById("gdRaiz"); if (r && M.guardia && M.guardia.montar) M.guardia.montar(r, arg, datos); } },
    consulta: { titulo: "Consulta Clínica Experta", vista: function () { return '<div id="cqRaiz"></div>'; }, alMontar: function (arg) { var r = document.getElementById("cqRaiz"); if (r && M.consulta && M.consulta.montar) M.consulta.montar(r, arg); } },
    feynman: { titulo: "Tutor Feynman IA", vista: function () { return '<div id="fyRaiz"></div>'; }, alMontar: function () { var r = document.getElementById("fyRaiz"); if (r && M.feynman) M.feynman.montar(r, parametros); } },
    repaso: { titulo: "Repaso de hoy", vista: function () { return '<div id="rpRaiz"></div>'; }, alMontar: function () { var r = document.getElementById("rpRaiz"); if (r && M.estudio) M.estudio.montarRepaso(r); } },
    flashcards: { titulo: "Mis Flashcards", vista: function () { return '<div id="fcRaiz"></div>'; }, alMontar: function () { var r = document.getElementById("fcRaiz"); if (r && M.flashcards) M.flashcards.montar(r); } },
    perfil: { titulo: "Perfil", vista: vistaPerfil, alMontar: enlazarPerfil }
  };

  var parametros = {};
  function ruta() {
    var h = (location.hash || "").replace(/^#\/?/, "").split("?");
    var partes = h[0].split("/");
    parametros = {};
    (h[1] || "").split("&").forEach(function (kv) {
      var p = kv.split("="); if (p[0]) { try { parametros[p[0]] = decodeURIComponent(p[1] || ""); } catch (e) {} }
    });
    var vacia = partes[0] === "";
    var nombre = vacia ? "inicio" : RUTAS[partes[0]] ? partes[0] : "noencontrada";
    var arg = "";
    try { arg = nombre === "noencontrada" ? "" : decodeURIComponent(partes[1] || ""); } catch (e) {}
    return { nombre: nombre, arg: arg };
  }

  function pintarChrome() {
    var r = ruta();
    var links = document.querySelectorAll("[data-ruta]");
    for (var k = 0; k < links.length; k++) {
      if (links[k].getAttribute("data-ruta") === (r.nombre === "consulta" ? "guardia" : r.nombre)) links[k].setAttribute("aria-current", "page");
      else links[k].removeAttribute("aria-current");
    }
    document.getElementById("tbTitle").textContent = RUTAS[r.nombre].titulo;
    document.title = RUTAS[r.nombre].titulo + " · MedQuizPlus";
    var ex = M.examen(examenPreferido());
    var tc = document.getElementById("tbCuenta");
    if (tc) {
      if (!CUENTA.disponible) tc.hidden = true;
      else { tc.hidden = false;
        if (CUENTA.usuario) { tc.href = "#/perfil"; tc.textContent = (esPremium() ? "★ " : "") + CUENTA.usuario.nombre.split(/\s+/)[0]; tc.className = "topbar__acct" + (esPremium() ? " is-premium" : ""); }
        else { tc.href = "#/ingresar"; tc.textContent = "Ingresar"; tc.className = "topbar__acct"; } }
    }
    var tb = document.getElementById("tbExam");
    tb.textContent = ex.nombre;
    var nf = datos ? idsFalladas().length : 0, nv = datos ? idsFavoritas().length : 0;
    var cf = document.getElementById("cntFalladas"), cv = document.getElementById("cntFavoritas");
    cf.hidden = !nf; cf.textContent = String(nf);
    cv.hidden = !nv; cv.textContent = String(nv);
  }

  function render(mismaRuta) {
    pintarChrome();
    if (!datos) { raiz.innerHTML = cargando(); return; }
    var r = ruta();
    var def = RUTAS[r.nombre];
    raiz.innerHTML = '<div class="page' + (mismaRuta ? "" : " page--in") + '">' + def.vista(r.arg) + '</div>';
    if (def.alMontar) def.alMontar(r.arg);
    if (!mismaRuta) {
      window.scrollTo(0, 0);
      var v = document.getElementById("vista");
      if (v && document.activeElement && document.activeElement !== document.body) v.focus({ preventScroll: true });
    }
  }

  window.addEventListener("hashchange", function () {
    cerrarMenu();
    if (M.practica.activa()) {
      M.practica.cerrar();   // dispara mqp:sesion-cerrada → render()
      return;
    }
    render();
  });
  window.addEventListener("mqp:progreso", function () { if (!M.practica.activa()) pintarChrome(); });

  /* ---------- menú lateral en móvil ---------- */
  var side = document.getElementById("side");
  var abrirBtn = document.getElementById("sideOpen");
  var scrim = document.getElementById("sideScrim");
  function abrirMenu() {
    document.body.classList.add("menu-abierto");
    abrirBtn.setAttribute("aria-expanded", "true");
    scrim.hidden = false;
    var primero = side.querySelector("a[aria-current], a");
    if (primero) primero.focus();
  }
  function cerrarMenu() {
    if (!document.body.classList.contains("menu-abierto")) return;
    document.body.classList.remove("menu-abierto");
    abrirBtn.setAttribute("aria-expanded", "false");
    scrim.hidden = true;
  }
  abrirBtn.addEventListener("click", abrirMenu);
  document.getElementById("sideClose").addEventListener("click", function () { cerrarMenu(); abrirBtn.focus(); });
  scrim.addEventListener("click", cerrarMenu);
  document.addEventListener("keydown", function (ev) { if (ev.key === "Escape" && document.body.classList.contains("menu-abierto")) { cerrarMenu(); abrirBtn.focus(); } });
  side.addEventListener("click", function (ev) { if (ev.target.closest && ev.target.closest("a")) cerrarMenu(); });

  /* ---------- buscador global: especialidades y simuladores reales ---------- */
  (function () {
    var inp = document.getElementById("gsInput"), lista = document.getElementById("gsList");
    if (!inp || !lista) return;
    function norm(t) { return String(t || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, ""); }
    var items = [];
    function cargar() {
      if (items.length) return;
      M.especialidades.forEach(function (e) { items.push({ t: e.nombre, k: "Especialidad · ENAM", h: "#/examenes/enam?q=" + encodeURIComponent(e.nombre) }); });
      M.simuladores.forEach(function (x) { if (x.estado === "disponible") items.push({ t: x.titulo, k: "Simulador", h: "#/simuladores/" + x.id }); });
      [["Mi progreso", "#/progreso"], ["Preguntas falladas", "#/falladas"], ["Favoritas", "#/favoritas"], ["Arma tu sesión", "#/banco/configurar"]].forEach(function (p) { items.push({ t: p[0], k: "Sección", h: p[1] }); });
    }
    var sel = -1, res = [];
    function pintar() {
      lista.innerHTML = res.length ? res.map(function (r, i) { return '<li role="option" id="gs' + i + '"' + (i === sel ? ' aria-selected="true"' : "") + '><a href="' + r.h + '"><b>' + esc(r.t) + '</b><small>' + esc(r.k) + '</small></a></li>'; }).join("") : '<li class="gs__none">Sin resultados</li>';
      lista.hidden = !inp.value.trim();
      inp.setAttribute("aria-expanded", String(!lista.hidden));
    }
    inp.addEventListener("input", function () { cargar(); var q = norm(inp.value.trim()); res = q ? items.filter(function (i) { return norm(i.t).indexOf(q) !== -1; }).slice(0, 7) : []; sel = -1; pintar(); });
    inp.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") { inp.value = ""; res = []; pintar(); return; }
      if (ev.key === "ArrowDown" || ev.key === "ArrowUp") { ev.preventDefault(); if (!res.length) return; sel = (sel + (ev.key === "ArrowDown" ? 1 : res.length - 1)) % res.length; pintar(); }
      if (ev.key === "Enter") { var r = res[sel < 0 ? 0 : sel]; if (r) { ev.preventDefault(); location.hash = r.h; inp.value = ""; res = []; pintar(); inp.blur(); } }
    });
    lista.addEventListener("click", function () { inp.value = ""; res = []; pintar(); });
    document.addEventListener("click", function (ev) { if (!ev.target.closest(".gsearch")) { lista.hidden = true; } });
  })();

  /* ---------- análisis al terminar una práctica o un simulacro (main.js entrega los datos; todo se calcula de este intento) ---------- */
  function ritmo(seg) { return seg >= 90 ? Math.floor(seg / 60) + " min " + Math.round(seg % 60) + " s" : Math.round(seg) + " s"; }
  function analisisResultado(d) {
    var cont = d.contenedor; if (!cont || !G) return;
    var total = d.preguntas.length, ok = 0, mal = 0, bl = 0, por = {}, orden = [];
    d.preguntas.forEach(function (q, i) {
      var r = d.respuestas[i], g = por[q.especialidad] || (por[q.especialidad] = { n: 0, ok: 0 });
      if (!g.n) orden.push(q.especialidad);
      g.n++;
      if (!r) bl++; else if (r === q.clave) { ok++; g.ok++; } else mal++;
    });
    var simulacro = d.modo === "simulacro", pctG = total ? Math.round(ok / total * 100) : 0;
    var filas = orden.map(function (k) { var g = por[k], v = Math.round(g.ok / g.n * 100); return { nombre: k, n: g.n, ok: g.ok, v: v }; });
    var barras = filas.slice().sort(function (a, b) { return a.v - b.v || b.n - a.n; }).map(function (f) {
      return { etiqueta: f.nombre, sub: f.ok + " de " + f.n, valor: f.v, max: 100, texto: f.v + "%", tip: f.nombre + ": " + f.v + "% (" + f.ok + " de " + f.n + " correctas)" };
    });
    var html = '<div class="an-cols2"><section class="an-panel"><h3>Tu resultado</h3>' + G.donut(ok, mal, { blanco: bl, titulo: "Resultado" }) + '</section>' +
      '<section class="an-panel"><h3>Rendimiento por especialidad</h3><p class="an-nota">De la que más a la que menos necesitas reforzar.</p>' + G.barras(barras, { colA: "Especialidad", colB: "Correctas" }) + '</section></div>';

    // ritmo (solo simulacro, donde hay reloj)
    var recos = [];
    if (simulacro && d.duracion && total) {
      var porPreg = d.duracion / total, ideal = d.limite / total;
      html += '<section class="an-panel"><h3>Tu ritmo</h3><p class="an-nota">Segundos por pregunta frente al tiempo que da el simulacro.</p>' +
        G.barras([{ etiqueta: "Tu ritmo", valor: Math.round(porPreg), max: Math.round(Math.max(porPreg, ideal) * 1.1), texto: ritmo(porPreg) + " / preg.", tip: "Tu ritmo: " + ritmo(porPreg) + " por pregunta" },
                  { etiqueta: "Tiempo disponible", valor: Math.round(ideal), max: Math.round(Math.max(porPreg, ideal) * 1.1), texto: ritmo(ideal) + " / preg.", tip: "El simulacro da " + ritmo(ideal) + " por pregunta" }], { colA: "Medida", colB: "Segundos" }) + '</section>';
      if (d.porTiempo) recos.push({ t: "mal", p: "Se acabó el tiempo antes de terminar.", s: "Entrena a ritmo de examen: el simulacro rápido te da 1 minuto por pregunta.", href: "#/simuladores/enam-rapido", a: "Hacer un simulacro rápido" });
      else if (porPreg > ideal * 0.9) recos.push({ t: "info", p: "Terminaste muy justo de tiempo (" + ritmo(porPreg) + " por pregunta).", s: "Practica decidir más rápido las preguntas que ya dominas para tener margen en las difíciles." });
    }
    // comparación con tu intento anterior del mismo tipo
    var ses = M.progreso.leer().sesiones, actual0 = ses[0], previo = null;
    for (var i = 1; i < ses.length; i++) if (ses[i].tipo === (simulacro ? "simulacro" : "estudio") && ses[i].titulo === (d.cfg.titulo || "Práctica") && ses[i].total) { previo = ses[i]; break; }
    if (previo) {
      var pv = Math.round(previo.correctas / previo.total * 100), dif = pctG - pv;
      recos.push({ t: dif > 0 ? "ok" : dif < 0 ? "mal" : "info", p: dif > 0 ? "Mejoraste " + dif + " puntos frente a tu intento anterior (" + pv + "% → " + pctG + "%)." : dif < 0 ? "Bajaste " + Math.abs(dif) + " puntos frente a tu intento anterior (" + pv + "% → " + pctG + "%)." : "Igualaste tu intento anterior (" + pv + "%).", s: fecha(previo.t) });
    }
    // recomendaciones por especialidad (solo con 2+ preguntas, para no juzgar por una sola)
    var jz = filas.filter(function (f) { return f.n >= 2; });
    var debiles = jz.filter(function (f) { return f.v < 60; }).sort(function (a, b) { return a.v - b.v; }).slice(0, 3);
    var fuertes = jz.filter(function (f) { return f.v >= 80; }).sort(function (a, b) { return b.v - a.v; }).slice(0, 2);
    debiles.forEach(function (f) { recos.push({ t: "mal", p: "Refuerza " + f.nombre + ": " + f.ok + " de " + f.n + " correctas (" + f.v + "%).", s: "Practica sus preguntas comentadas y revisa los flujogramas.", href: "#/examenes/enam?q=" + encodeURIComponent(f.nombre), a: "Practicar " + f.nombre }); });
    fuertes.forEach(function (f) { recos.push({ t: "ok", p: "Vas bien en " + f.nombre + " (" + f.v + "%).", s: "Repásala de vez en cuando para mantenerla." }); });
    if (mal) recos.push({ t: "info", p: "Fallaste " + M.plural(mal, "pregunta", "preguntas") + ".", s: "Leer el comentario de cada error es lo que más sube tu puntaje.", href: "#/falladas", a: "Repasar mis falladas" });
    if (bl && !d.porTiempo) recos.push({ t: "info", p: "Dejaste " + M.plural(bl, "pregunta", "preguntas") + " sin responder.", s: "Pregúntate si fue falta de tiempo o de conocimiento; cada caso se entrena distinto." });
    recos.push({ t: "info", p: "Sigue la evolución de todos tus intentos.", s: "", href: "#/progreso", a: "Ver mi progreso" });
    html += '<section class="an-panel"><h3>Recomendaciones para ti</h3><p class="an-nota">Calculadas solo con este intento: orientan tu estudio, no predicen tu nota real.</p><ul class="an-recos">' +
      recos.map(function (r) { return '<li class="an-reco an-reco--' + r.t + '"><p>' + esc(r.p) + (r.s ? "<small>" + esc(r.s) + "</small>" : "") + '</p>' + (r.href ? '<a href="' + r.href + '">' + esc(r.a) + ' →</a>' : "") + '</li>'; }).join("") + '</ul></section>';
    cont.innerHTML = html;
    var viejo = cont.parentNode && cont.parentNode.querySelector(".sim-result__areas");   // el análisis ya incluye el rendimiento por especialidad
    if (viejo) viejo.hidden = true;
  }
  document.addEventListener("mqp:resultado", function (ev) { try { analisisResultado(ev.detail); } catch (e) { if (window.console) console.warn("[app] análisis", e); } });

  if (G) G.iniciarTips();

  /* ---------- arranque ---------- */
  sesion.hidden = true;
  render();
  cargarCuenta().then(function () { if (!M.practica.activa()) render(true); });
  M.cargarTodo().then(function (d) {
    datos = d;
    conteo = M.ui.contarPorExamen(d);
    for (var k = 0; k < d.preguntas.length; k++) porId[d.preguntas[k].id] = d.preguntas[k];
    if (d.fallos === M.especialidades.length) {
      raiz.innerHTML = '<div class="page">' + vacio("libro", "No se pudo cargar el banco", "Revisa tu conexión y vuelve a intentarlo.", '<button class="btn btn--primary" type="button" onclick="location.reload()">Reintentar</button>') + '</div>';
      return;
    }
    render(true);
  });
})();
