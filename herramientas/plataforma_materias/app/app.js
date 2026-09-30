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

  /* ---------- sesiones de práctica ---------- */
  function iniciar(cfg) {
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

    var rapido = M.simulador("enam-rapido");
    var accesos = '<div class="quick">' +
      '<a class="quick__item" href="#/banco"><span class="quick__icon">' + I("libro") + '</span><span><b>Banco de preguntas</b><small>Arma tu sesión por especialidad</small></span></a>' +
      '<a class="quick__item" href="#/simuladores/enam-rapido"><span class="quick__icon">' + I("rayo") + '</span><span><b>' + esc(rapido.titulo) + '</b><small>' + rapido.cantidad + ' preguntas · ' + M.duracion(rapido.cantidad * rapido.segundosPorPregunta) + '</small></span></a>' +
      '<a class="quick__item" href="#/falladas"><span class="quick__icon quick__icon--mark">' + I("cruz") + '</span><span><b>Repasar falladas</b><small>' + (fall ? M.plural(fall, "pregunta por repasar", "preguntas por repasar") : "Aún no tienes preguntas falladas") + '</small></span></a>' +
      '</div>';

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

    var examenes = '<ul class="exam-rows">' + M.examenes.map(function (e) {
      var n = conteo ? conteo[e.id].total : null;
      return '<li><a class="exam-row" href="#/examenes/' + e.id + '">' +
        '<span class="exam-row__mark' + (e.estado === "disponible" ? " is-live" : "") + '">' + esc(e.nombre.charAt(0)) + '</span>' +
        '<span class="exam-row__name">' + esc(e.nombre) + '<small>' + (n == null ? "…" : e.estado === "disponible" ? M.plural(n, "pregunta", "preguntas") : (n ? M.plural(n, "pregunta tipo", "preguntas tipo") : "Banco en construcción")) + '</small></span>' +
        '<span class="badge ' + (e.estado === "disponible" ? "badge--ok" : "badge--soon") + '">' + (e.estado === "disponible" ? "Disponible" : "Próximamente") + '</span>' +
        '</a></li>';
    }).join("") + '</ul>';

    var recientes = p.sesiones.slice(0, 4);
    var actividad = recientes.length ? listaSesiones(recientes) : '<p class="muted">Aquí verás tus últimas sesiones y simulacros.</p>';

    return cabecera("", esc(saludo()) + ' <span aria-hidden="true">👋</span>', "¿Qué quieres practicar hoy?") +
      '<div class="dash">' +
        '<div class="dash__main">' + continuar + accesos +
          '<section class="card"><div class="card__head"><h2 class="card__h">Tu resumen</h2><a class="link-arrow" href="#/progreso">Ver mi progreso <span aria-hidden="true">→</span></a></div>' + resumen + '</section>' +
        '</div>' +
        '<div class="dash__side">' +
          '<section class="card"><div class="card__head"><h2 class="card__h">Exámenes</h2></div>' + examenes + '</section>' +
          '<section class="card"><div class="card__head"><h2 class="card__h">Actividad reciente</h2></div>' + actividad + '</section>' +
        '</div>' +
      '</div>';
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

    var bloques = M.areas.map(function (area) {
      var esps = M.especialidades.filter(function (e) { return e.area === area.id; });
      var total = 0;
      for (var k = 0; k < esps.length; k++) total += c.porArchivo[esps[k].archivo] || 0;
      return '<section class="area" data-area="' + area.id + '">' +
        '<div class="area__head"><div><h2 class="area__title">' + esc(area.nombre) + '</h2>' +
        '<p class="area__meta">' + (total ? M.plural(total, "pregunta", "preguntas") + " · " : "") + M.plural(esps.length, "especialidad", "especialidades") + '</p></div>' +
        (total && esps.length > 1 ? '<button class="btn btn--ghost btn--sm" type="button" data-accion="area" data-area="' + area.id + '" data-examen="' + ex.id + '">Entrenar el área</button>' : "") +
        '</div><div class="specs specs--app" data-area-grid="' + area.id + '"></div></section>';
    }).join("");

    return '<nav class="crumbs" aria-label="Ruta"><a href="#/examenes">Exámenes</a><span aria-hidden="true">/</span><span aria-current="page">' + esc(ex.nombre) + '</span></nav>' +
      cabecera(vivo ? "Banco disponible" : "Próximamente", esc(ex.titulo), esc(ex.lema), extra) + aviso + bloques;
  }
  /* las tarjetas de especialidad son el componente compartido (main.js → MQP.ui) */
  function montarTarjetas(exId) {
    var c = conteo[exId], prog = M.ui.progresoPorArchivo(exId), k = 0;
    var vivo = M.examen(exId).estado === "disponible";
    var grids = raiz.querySelectorAll("[data-area-grid]");
    for (var g = 0; g < grids.length; g++) {
      var area = grids[g].getAttribute("data-area-grid");
      M.especialidades.forEach(function (esp) {
        if (esp.area !== area) return;
        var t = M.ui.tarjetaEspecialidad(esp, k++, function (e, materia) {
          var attrs = { "data-archivo": esp.archivo, "data-examen": exId, "data-categoria": materia || "" };
          ACCIONES.especialidad({ getAttribute: function (n) { return attrs[n]; } });
        });
        var ok = datos.porArchivo[esp.archivo] && datos.porArchivo[esp.archivo].ok;
        var p = prog[esp.archivo] || {};
        t.actualizar(ok ? { estado: "ok", total: c.porArchivo[esp.archivo] || 0, respondidas: p.respondidas || 0, tipo: !vivo,
          materias: esp.categorias.length ? M.ui.contarMaterias(datos.preguntas, esp.archivo, exId) : null } : { estado: "error" });
        grids[g].appendChild(t.nodo);
      });
    }
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
    return cabecera("Banco de preguntas", "Arma tu sesión", "Elige examen, especialidades, qué preguntas incluir y cómo quieres resolverlas.") +
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

  /* ---------- Mi progreso ---------- */
  var MINIMO = 3;   // respuestas mínimas en una especialidad para juzgarla
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
      '<div class="grid-2">' +
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
        '<section class="card"><h2 class="card__h">Cuenta</h2>' +
          '<p class="muted">Las cuentas de usuario todavía no están disponibles. Cuando lo estén, aquí podrás iniciar sesión y conservar tu progreso en cualquier dispositivo.</p>' +
          '<a class="btn btn--ghost" href="../#registro">Ver el registro</a>' +
        '</section>' +
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

  function vistaNoEncontrada() {
    return vacio("capas", "No encontramos esta sección", "Puede que el enlace haya cambiado.", '<a class="btn btn--primary" href="#/inicio">Ir al inicio</a>');
  }

  /* ======================================================================
     Enrutador
     ====================================================================== */
  var RUTAS = {
    inicio: { titulo: "Inicio", vista: vistaInicio },
    examenes: { titulo: "Exámenes", vista: function (arg) { return arg ? vistaExamen(arg) : vistaExamenes(); }, alMontar: function (arg) { if (arg && M.examen(arg)) montarTarjetas(arg); } },
    banco: { titulo: "Banco de preguntas", vista: vistaBanco, alMontar: enlazarBanco },
    simuladores: { titulo: "Simuladores", vista: function (arg) { return arg ? vistaSimulador(arg) : vistaSimuladores(); }, alMontar: function (arg) { if (arg) enlazarSimulador(arg); } },
    progreso: { titulo: "Mi progreso", vista: vistaProgreso },
    falladas: { titulo: "Preguntas falladas", vista: vistaFalladas },
    favoritas: { titulo: "Favoritas", vista: vistaFavoritas },
    perfil: { titulo: "Perfil", vista: vistaPerfil, alMontar: enlazarPerfil }
  };

  function ruta() {
    var partes = (location.hash || "").replace(/^#\/?/, "").split("/");
    var nombre = RUTAS[partes[0]] ? partes[0] : "inicio";
    return { nombre: nombre, arg: RUTAS[partes[0]] ? decodeURIComponent(partes[1] || "") : "" };
  }

  function pintarChrome() {
    var r = ruta();
    var links = document.querySelectorAll("[data-ruta]");
    for (var k = 0; k < links.length; k++) {
      if (links[k].getAttribute("data-ruta") === r.nombre) links[k].setAttribute("aria-current", "page");
      else links[k].removeAttribute("aria-current");
    }
    document.getElementById("tbTitle").textContent = RUTAS[r.nombre].titulo;
    document.title = RUTAS[r.nombre].titulo + " · MedQuizPlus";
    var ex = M.examen(examenPreferido());
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

  /* ---------- arranque ---------- */
  sesion.hidden = true;
  render();
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
