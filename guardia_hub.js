/* MedQuizPlus · Centro de simulación clínica (pantalla principal de «Sobrevive a la Guardia»).
   Solo presenta y enlaza: no toca la lógica clínica. Todo dato mostrado sale de los casos cargados (guardia_casos.js, consulta_casos.js) y del progreso real del alumno
   (M.progreso.preferencia("guardia" / "consulta")); las recomendaciones son las de M.guardiaNucleo.recomendar. Las fotografías son ilustraciones generadas con IA
   (ver guardia/portadas/LEEME.txt): no son imágenes clínicas reales. */
(function (raiz) {
  "use strict";
  var M = raiz.MQP || (raiz.MQP = {});
  var G = function () { return M.guardiaNucleo; }, GD = function () { return M.guardia; };
  var esc = function (s) { return GD().esc(s); };
  var IMG = "../guardia/portadas/";
  var SRC_HUB = (document.currentScript && document.currentScript.src) || "", BASE_HUB = SRC_HUB.replace(/guardia_hub\.js(\?.*)?$/, ""), VER_HUB = (SRC_HUB.split("?")[1] || "");
  var I = {
    pulse: '<path d="M3 12h4l2-6 4 12 2-6h6"/>', doc: '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>', brain: '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 4 3 3 0 0 0 2 4 3 3 0 0 0 3 4V4zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 4 3 3 0 0 1-2 4 3 3 0 0 1-3 4V4z"/>',
    img: '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="M21 16l-5-5-8 8"/>', chart: '<path d="M5 20V10M12 20V4M19 20v-7"/>', clock: '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 3h6"/>',
    bolt: '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>', users: '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 5a3 3 0 0 1 0 6M18 14c2 .8 3 2.700 3 6"/>',
    heart: '<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.500-9 9-9 9z"/><path d="M7 12h3l1.500-3 2 6 1.500-3h2"/>', flask: '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M8 15h8"/>',
    book: '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>', chat: '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    warn: '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.01"/>', arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>', target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.500"/><path d="M12 12l6-6"/>',
    drop: '<path d="M12 3s6 6.500 6 11a6 6 0 0 1-12 0c0-4.500 6-11 6-11z"/>', clot: '<circle cx="9" cy="10" r="4"/><circle cx="16" cy="14" r="3"/><circle cx="10" cy="17.500" r="2"/>', kidney: '<path d="M15 4c3 1 5 4 5 8s-2 8-5 8c-2 0-3-2-3-4 0-3 2-3 2-6S12 6 15 4z"/><path d="M12 12H9"/>',
    liver: '<path d="M3 10c0-3 4-5 9-5s9 2 9 6-4 8-9 8c-3 0-5-2-9-9z"/>', pill: '<rect x="3" y="9" width="18" height="6" rx="3" transform="rotate(-35 12 12)"/><path d="M9.500 7.500l5 9"/>', wind: '<path d="M3 8h11a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h8"/>',
    cup: '<path d="M7 3h10l-1 18H8z"/><path d="M7.500 9h9"/>', bowl: '<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M8 7h8"/>', gland: '<path d="M12 8c-3-3-8-1-8 3s4 6 8 3c4 3 8 1 8-3s-5-6-8-3z"/>', hormone: '<circle cx="8" cy="12" r="4"/><path d="M12 12h8M17 9l3 3-3 3"/>',
    shield: '<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/>', virus: '<circle cx="12" cy="12" r="5"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.600 5.600l2.100 2.100M16.300 16.300l2.100 2.100M18.400 5.600l-2.100 2.100M7.700 16.300l-2.100 2.100"/>',
    tube: '<path d="M9 3h6M10 3v14a2 2 0 0 0 4 0V3M10 12h4"/>', sperm: '<circle cx="8" cy="8" r="3"/><path d="M10 10c4 3 6 5 10 9"/>', capsule: '<rect x="3" y="9" width="18" height="6" rx="3" transform="rotate(-35 12 12)"/><path d="M9.500 7.500l5 9"/>', search: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>', chev: '<path d="M6 9l6 6 6-6"/>',
    file: '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/>', bar: '<path d="M5 20V12M12 20V5M19 20v-5"/>', lock: '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'
  };
  function ic(n, c) { return '<svg class="gh-ic' + (c ? " " + c : "") + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + I[n] + '</svg>'; }
  function progC() { var g = M.progreso && M.progreso.preferencia("consulta"); return g && g.casos ? g : { casos: {} }; }
  function resumen(casos, prog) {
    var n = casos.length, NIV = G().NIVEL, dif = casos.map(function (c) { return c.dificultad; }), dur = casos.map(function (c) { return c.duracion_min; }), esp = {};
    casos.forEach(function (c) { c.especialidad.split(" · ").forEach(function (x) { esp[x] = (esp[x] || 0) + 1; }); });
    var temas = Object.keys(esp).sort(function (a, b) { return esp[b] - esp[a] || (a < b ? -1 : 1); });
    var hechos = casos.filter(function (c) { return prog.casos[c.id]; }), mejor = hechos.length ? Math.round(hechos.reduce(function (s, c) { return s + prog.casos[c.id].mejor; }, 0) / hechos.length) : null;
    var nombreNivel = function (d) { return NIV[d].replace(/^Nivel \d · /, ""); };
    var dmin = Math.min.apply(null, dif), dmax = Math.max.apply(null, dif), tmin = Math.min.apply(null, dur), tmax = Math.max.apply(null, dur);
    return { n: n, nivel: n ? (dmin === dmax ? nombreNivel(dmin) : nombreNivel(dmin) + " – " + nombreNivel(dmax)) : "", tiempo: n ? (tmin === tmax ? tmin + " min" : tmin + " – " + tmax + " min") : "", temas: temas, hechos: hechos.length, mejor: mejor };
  }
  function datos(r) { return '<dl class="gh-datos"><div>' + ic("file") + '<dd>' + r.n + '</dd><dt>Casos disponibles</dt></div><div>' + ic("bar") + '<dd>' + esc(r.nivel) + '</dd><dt>Nivel</dt></div><div>' + ic("clock") + '<dd>' + esc(r.tiempo) + '</dd><dt>Tiempo por caso</dt></div></dl>'; }
  function progreso(r, etq) {
    var pct = r.n ? Math.round(r.hechos / r.n * 100) : 0;
    return '<div class="gh-prog"><p><b>' + r.hechos + ' de ' + r.n + '</b> ' + etq + (r.mejor != null ? ' · mejor puntaje medio <b>' + r.mejor + ' %</b>' : ' · aún sin intentos') + '</p><div class="gh-barra" role="img" aria-label="Progreso: ' + r.hechos + ' de ' + r.n + ' casos completados"><i style="width:' + pct + '%"></i></div></div>';
  }
  function tarjeta(o) {
    return '<article class="gh-card gh-card--' + o.tono + '" aria-labelledby="ghT' + o.id + '"><div class="gh-card__foto"><img src="' + IMG + o.img + '" alt="" width="800" height="600" loading="lazy" decoding="async"><span class="gh-pill">' + ic(o.icono) + esc(o.pill) + '</span>' + (o.pronto ? '<span class="gh-soon">Próximamente</span>' : "") +
      '<div class="gh-card__sobre"><h2 id="ghT' + o.id + '">' + esc(o.titulo) + '</h2><p>' + esc(o.texto) + '</p></div></div>' + (o.datos || "") + (o.prog || "") + o.boton + '</article>';
  }
  function boton(tono, href, txt) { return '<a class="gh-btn gh-btn--' + tono + '" href="' + href + '"><span>' + esc(txt) + '</span>' + ic("arrow") + '</a>'; }

  /* ---- recomendados (mismo algoritmo y mismos textos honestos que antes) ---- */
  function recomendados(rec) {
    var MIN = G().MIN_TOTAL, NIVEL = G().NIVEL;
    var enc = rec.modo === "personalizado" ? "Casos recomendados para ti" : rec.modo === "provisional" ? "Casos recomendados para ti (provisional)" : "Por dónde empezar";
    var intro = rec.modo === "invitacion" ? "Todavía no tenemos suficientes respuestas tuyas en el banco (" + rec.total + " de " + MIN + ") para recomendarte con criterio, así que no inventamos una recomendación. Estos son buenos puntos de partida; responde preguntas en el banco" + (rec.faltan ? " (te faltan " + rec.faltan + ")" : "") + " para personalizarlos."
      : rec.modo === "provisional" ? "Tenemos pocas respuestas en las especialidades de estos casos, por eso la sugerencia es provisional y se afina a medida que practicas."
        : "Calculado con tus propias respuestas en el banco y tu historial en la guardia. Se procesa en tu navegador; no se comparte con otros alumnos.";
    return '<section class="gh-rec" aria-labelledby="ghRecT"><header class="gh-sec-h">' + ic("target", "gh-ic--lg") + '<div><h2 id="ghRecT">' + enc + '</h2><p>' + esc(intro) + '</p></div><a class="gh-link" href="#/progreso">Ver análisis detallado ' + ic("arrow") + '</a></header><ul class="gh-rec__l">' + rec.items.map(function (i) {
      var ped = /Pediatr/i.test(i.caso.especialidad);
      return '<li class="gh-rec__i"><a class="gh-rec__a" href="#/guardia/' + esc(i.caso.id) + '" aria-label="Empezar el caso: ' + esc(i.caso.titulo) + '"><span class="gh-rec__f' + (ped ? "" : " gh-rec__f--ic") + '">' + (ped ? '<img src="' + IMG + 'pediatria.webp" alt="" width="480" height="360" loading="lazy" decoding="async">' : ic("heart", "gh-ic--lg")) + '</span><span class="gh-rec__c"><b>' + esc(i.caso.titulo) + '</b>' +
        '<span class="gh-tag">' + esc(i.caso.especialidad.split(" · ")[0]) + '</span><span class="gh-rec__n">' + ic("bar") + esc(NIVEL[i.caso.dificultad].replace(/^Nivel \d · /, "")) + '</span><span class="gh-rec__m">' + esc(i.motivos[0]) + '</span></span><span class="gh-rec__go">Empezar ' + ic("arrow") + '</span></a></li>';
    }).join("") + '</ul></section>';
  }
  /* ---- estadísticas reales ---- */
  function estadisticas(rG, rC, g, est, nCasosG) {
    var todos = []; Object.keys(g.casos).forEach(function (k) { todos.push(g.casos[k].mejor); }); var pc = progC(); Object.keys(pc.casos).forEach(function (k) { todos.push(pc.casos[k].mejor); });
    var media = todos.length ? Math.round(todos.reduce(function (s, x) { return s + x; }, 0) / todos.length) : null, R = 42, C = 2 * Math.PI * R;
    var sinCrit = Object.keys(g.casos).filter(function (k) { return (g.casos[k].criticos || 0) === 0; }).length, completos = Object.keys(g.casos).length;
    var peor = null; if (est && est.areas) Object.keys(est.areas).forEach(function (k) { var a = est.areas[k]; if (a.n >= G().MIN_AREA && (!peor || a.pct < peor.pct)) peor = a; });
    return '<section class="gh-est" aria-labelledby="ghEstT"><h2 id="ghEstT">' + ic("chart") + ' Tus estadísticas en simuladores</h2><div class="gh-est__c"><div class="gh-anillo" role="img" aria-label="' + (media != null ? "Puntaje medio " + media + " por ciento" : "Sin intentos todavía") + '"><svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="' + R + '" class="gh-anillo__f"/><circle cx="50" cy="50" r="' + R + '" class="gh-anillo__v" stroke-dasharray="' + (media != null ? (C * media / 100).toFixed(1) : 0) + " " + C.toFixed(1) + '" transform="rotate(-90 50 50)"/></svg><span><b>' + (media != null ? media + " %" : "—") + '</b><small>Puntaje medio</small></span></div>' +
      '<dl class="gh-est__l"><div><dt>Casos de emergencia completados</dt><dd>' + rG.hechos + ' / ' + rG.n + '</dd></div>' + (rC ? '<div><dt>Consultas completadas</dt><dd>' + rC.hechos + ' / ' + rC.n + '</dd></div>' : "") + '<div><dt>Emergencias sin errores críticos (último intento)</dt><dd>' + (completos ? sinCrit + ' / ' + completos : "—") + '</dd></div></dl></div>' +
      '<p class="gh-est__nota">El tiempo de resolución y el uso de interconsultas no se resumen aquí: se muestran en el informe de cada caso.</p>' +
      (peor ? '<a class="gh-refuerzo" href="#/banco">' + ic("warn") + '<span><small>Área para reforzar</small><b>' + esc(peor.nombre) + '</b><em>Aciertas ' + peor.pct + ' % en el banco (' + peor.ok + ' de ' + peor.n + ')</em></span>' + ic("arrow") + '</a>' : '<p class="gh-refuerzo gh-refuerzo--vacio">' + ic("warn") + '<span><small>Área para reforzar</small><em>Aún no hay suficientes respuestas en el banco para señalarla.</em></span></p>') + '</section>';
  }
  /* ---- fuentes y guías usadas en los casos ---- */
  function fuentes(casosG, casosC) {
    var mapa = {}, orden = [];
    function add(c, ruta) { (c.referencias || []).forEach(function (r) { var k = r.pmid ? "p" + r.pmid : r.doi ? "d" + r.doi : r.url ? "u" + r.url : "t" + r.titulo; if (!mapa[k]) { mapa[k] = { r: r, casos: [] }; orden.push(k); } mapa[k].casos.push({ id: c.id, titulo: c.titulo, ruta: ruta }); }); }
    casosG.forEach(function (c) { add(c, "guardia"); }); casosC.forEach(function (c) { add(c, "consulta"); });
    var l = orden.map(function (k) { return mapa[k]; }), pe = function (x) { return /Perú|EsSalud|MINSA|Ministerio de Salud/i.test(x.r.organismo + " " + x.r.titulo); };
    return { todas: l, peruanas: l.filter(pe), otras: l.filter(function (x) { return !pe(x); }), esPeru: pe };
  }
  function abrirFuentes(F, disparador) {
    var fila = function (x) {
      var r = x.r, ids = [];
      if (r.pmid) ids.push(GD().enlace("https://pubmed.ncbi.nlm.nih.gov/" + r.pmid + "/", "PMID " + r.pmid)); if (r.doi) ids.push(GD().enlace("https://doi.org/" + r.doi, "DOI " + r.doi)); if (r.url) ids.push(GD().enlace(r.url, "Documento"));
      return '<li class="gh-fu"><p><b>' + esc(r.titulo) + '</b></p><p class="muted small">' + esc(r.organismo) + ' · ' + esc(r.anio) + ' · ' + ids.join(" · ") + '</p><p class="muted small">' + esc(r.vigencia) + '</p><p class="small">Usada en: ' + x.casos.map(function (c) { return '<a href="#/' + c.ruta + '/' + esc(c.id) + '" data-cerrar>' + esc(c.titulo) + '</a>'; }).join(" · ") + '</p></li>';
    };
    var html = '<p class="gd-aviso" role="note">Son las referencias que respaldan los casos de este centro. Cuando una guía peruana y una internacional difieren, el caso lo declara y prevalece la más reciente. Si ves una discrepancia con tu guía vigente, prevalece la guía.</p>' +
      '<h3 class="gd-h3">Guías y normas peruanas (' + F.peruanas.length + ')</h3><ul class="gh-fu__l">' + F.peruanas.map(fila).join("") + '</ul><h3 class="gd-h3">Guías y estudios internacionales (' + F.otras.length + ')</h3><ul class="gh-fu__l">' + F.otras.map(fila).join("") + '</ul>';
    GD().dialogo("Guías y fuentes de los casos", html, "gd-dlg--lab", disparador);
  }

  function pintar(cont, ctx) {
    var casosG = raiz.MQP_GUARDIA || [], casosC = raiz.MQP_CONSULTA || [], casosU = raiz.MQP_GUARDIA_UCI || [], g = GD().cargar(), rG = resumen(casosG, g), rU = casosU.length ? resumen(casosU, g) : null, rC = casosC.length ? resumen(casosC, progC()) : null;
    var est = GD().estadisticasAlumno(ctx.datos), rec = G().recomendar(casosG, g, est, Date.now()), F = fuentes(casosG, casosC);
    var conImg = casosG.concat(casosC).filter(function (c) { return (c.imagenes || []).length; }).length;
    var cap = [["doc", "Decisiones con cinco alternativas"], ["flask", "Laboratorio y valores de referencia"], ["img", "Imágenes reales con fuente y licencia"], ["chart", "Informe con razonamiento y bibliografía"], ["clock", "Modo cronometrado opcional"]];
    var h = '<div class="gh">' +
      '<header class="gh-hero"><img class="gh-hero__img" src="' + IMG + 'hero.webp" alt="" width="1600" height="900" fetchpriority="high" decoding="async"><canvas class="gh-monitor" aria-hidden="true"></canvas><div class="gh-hero__vel"></div><div class="gh-hero__c"><p class="gh-kicker">' + ic("pulse") + 'Simuladores clínicos</p><h1>Sobrevive a la <span>Guardia</span></h1><p class="gh-hero__sub">Toma decisiones clínicas, solicita e interpreta pruebas y aprende de un informe completo con tu razonamiento y la bibliografía de cada caso.</p>' +
      '<ul class="gh-caps">' + cap.map(function (c) { return '<li>' + ic(c[0]) + '<span>' + esc(c[1]) + '</span></li>'; }).join("") + '</ul>' + (M.guardiaIntro ? '<button type="button" class="gh-link gh-link--claro" id="ghIntro">▶ Ver la introducción</button>' : "") + '</div><p class="gh-hero__lema" aria-hidden="true">Decide.<br>Actúa.<br><em>Aprende.</em></p></header>' +
      '<p class="gd-aviso" role="note">' + esc(GD().AVISO) + '</p>' +
      '<section class="gh-mods" aria-label="Modalidades"><div class="gh-mods__g gh-mods__g--4">' +
      tarjeta({ id: "E", tono: "rojo", img: "emergencias.webp", icono: "bolt", pill: "EMERGENCIAS", titulo: "Guardia de Emergencias", texto: "Enfrenta emergencias médicas, toma decisiones bajo presión y aprende a estabilizar pacientes en situaciones críticas.", datos: datos(rG), prog: progreso(rG, "casos completados"), boton: boton("rojo", "#/guardia/emergencias", "Comenzar casos de emergencia") }) +
      (rC ? tarjeta({ id: "C", tono: "azul", img: "consulta.webp", icono: "users", pill: "CONSULTA AMBULATORIA", titulo: "Consulta Clínica Experta", texto: "Evalúa pacientes desde la anamnesis hasta el tratamiento. Solicita exámenes, interpreta resultados y construye diagnósticos clínicos.", datos: datos(rC), prog: progreso(rC, "consultas completadas"), boton: boton("azul", "#/consulta", "Comenzar consulta clínica") })
        : tarjeta({ id: "C", tono: "azul", img: "consulta.webp", icono: "users", pill: "CONSULTA AMBULATORIA", titulo: "Consulta Clínica Experta", texto: "Evalúa pacientes desde la anamnesis hasta el tratamiento. Solicita exámenes, interpreta resultados y construye diagnósticos clínicos.", boton: boton("azul", "#/consulta", "Comenzar consulta clínica") })) +
      tarjeta({ id: "S", tono: "teal", img: "serums-posta.webp", icono: "users", pill: "MEDICINA RURAL Y COMUNITARIA", titulo: "Misión SERUMS", texto: "Sobrevive a la posta: decide con recursos limitados, gestiona tu inventario, refiere a tiempo y cuida a tu comunidad.", prog: '<div class="gh-prog"><p><b>Nuevo</b> · 10 casos originales con normativa peruana verificada y estado de validación declarado.</p></div>', boton: boton("teal", "#/serums", "Asumir mi posta") }) +
      (casosU.length ? tarjeta({ id: "U", tono: "indigo", img: "uci.webp", icono: "heart", pill: "CUIDADOS CRÍTICOS", titulo: "UCI y Paciente Crítico", texto: "Maneja pacientes en estado crítico: ventilación, hemodinamia, reanimación y reperfusión. Razona, decide y aprende con un informe completo.", datos: datos(rU), prog: progreso(rU, "casos completados"), boton: boton("indigo", "#/guardia/uci", "Comenzar casos de UCI") }) :
        tarjeta({ id: "U", tono: "gris", img: "uci.webp", icono: "heart", pill: "CUIDADOS CRÍTICOS", pronto: true, titulo: "UCI y Paciente Crítico", texto: "Manejo de pacientes en estado crítico. Esta modalidad todavía no está disponible: aún no hay casos publicados.", prog: '<div class="gh-prog gh-prog--uci"><p>Aún no hay casos de UCI publicados. Mientras tanto puedes practicar la toma de decisiones críticas en la Guardia de Emergencias.</p></div>', boton: '<p class="gh-btn gh-btn--off">' + ic("lock") + '<span>Próximamente</span></p>' })) +
      '</div></section>' +
      '<div class="gh-fila">' + recomendados(rec) + estadisticas(rG, rC, g, est) + '</div>' +
      '<section class="gh-accesos" aria-label="Accesos rápidos"><ul>' +
      '<li><button type="button" class="gh-acc gh-acc--verde" id="ghLab"><img src="' + IMG + 'laboratorio.webp" alt="" width="560" height="420" loading="lazy" decoding="async">' + '<span class="gh-acc__i">' + ic("flask") + '</span><span class="gh-acc__t"><b>Biblioteca de valores de laboratorio</b><small>Análisis por áreas con sus valores de referencia, por edad y sexo, y buscador.</small></span>' + ic("arrow") + '</button></li>' +
      '<li><button type="button" class="gh-acc gh-acc--ambar" id="ghFu"><img src="' + IMG + 'guias.webp" alt="" width="560" height="420" loading="lazy" decoding="async"><span class="gh-acc__i">' + ic("book") + '</span><span class="gh-acc__t"><b>Guías y fuentes de los casos</b><small>' + F.todas.length + ' referencias: ' + F.peruanas.length + ' peruanas (MINSA/EsSalud) y ' + F.otras.length + ' internacionales.</small></span>' + ic("arrow") + '</button></li>' +
      '<li><div class="gh-acc gh-acc--celeste gh-acc--info"><span class="gh-acc__i">' + ic("img") + '</span><span class="gh-acc__t"><b>Imágenes médicas reales</b><small>' + conImg + ' casos incluyen imágenes publicadas con licencia abierta y su ficha de fuente; las verás dentro de cada caso.</small></span></div></li>' +
      '<li><a class="gh-acc gh-acc--lila" href="#/feynman"><img src="' + IMG + 'tutor.webp" alt="" width="560" height="420" loading="lazy" decoding="async"><span class="gh-acc__i">' + ic("chat") + '</span><span class="gh-acc__t"><b>Tutor Feynman IA</b><small>Explica un tema con tus palabras y recibe correcciones del tutor.</small></span>' + ic("arrow") + '</a></li></ul></section>' +
      '<p class="gh-credito">Las fotografías de esta pantalla son ilustraciones generadas con IA para el diseño y el monitor del encabezado es una animación decorativa con valores de ejemplo; no son imágenes ni datos clínicos reales ni sirven para interpretación diagnóstica. Las imágenes médicas de los casos son otras: figuras publicadas con licencia abierta y su fuente.</p></div>';
    cont.innerHTML = h;
    cont.querySelector("#ghLab").addEventListener("click", function (e) { abrirBiblioteca(e.currentTarget); });
    cont.querySelector("#ghFu").addEventListener("click", function (e) { abrirFuentes(F, e.currentTarget); });
    var bi = cont.querySelector("#ghIntro"); if (bi) bi.addEventListener("click", function () { M.guardiaIntro.mostrar({}); });
  }

  /* ---------- biblioteca de valores de laboratorio (todas las áreas, buscador, secciones desplegables) ---------- */
  var cargaBib = null;
  function cargarBiblioteca() {
    if (raiz.MQP_GUARDIA_BIB) return Promise.resolve(raiz.MQP_GUARDIA_BIB);
    if (!cargaBib) cargaBib = new Promise(function (ok, mal) { var sc = document.createElement("script"); sc.src = BASE_HUB + "guardia_biblioteca.js" + (VER_HUB ? "?" + VER_HUB : ""); sc.onload = function () { ok(raiz.MQP_GUARDIA_BIB); }; sc.onerror = function () { cargaBib = null; mal(new Error("biblioteca")); }; document.head.appendChild(sc); });
    return cargaBib;
  }
  function norm(t) { return String(t || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase(); }
  function filaBib(t) {
    var vals = t.r.map(function (x) { return '<li>' + (x[0] ? '<span class="gb-g">' + esc(x[0]) + '</span>' : "") + '<b>' + esc(x[1]) + '</b></li>'; }).join("");
    return '<tr class="gb-fila" data-q="' + esc(norm(t.n + " " + t.a + " " + t.s)) + '"><th scope="row"><span class="gb-nom">' + esc(t.n) + '</span>' + (t.a ? ' <span class="gb-abr">' + esc(t.a) + '</span>' : "") + '</th><td class="gb-u">' + (t.u ? esc(t.u) : '<span aria-hidden="true">—</span><span class="sr-only">Sin unidad</span>') + '</td><td class="gb-v"><ul>' + vals + '</ul></td></tr>';
  }
  function abrirBiblioteca(disparador) {
    var d = GD().dialogo("Biblioteca de valores de laboratorio", '<p class="muted" role="status">Cargando la biblioteca…</p>', "gd-dlg--lab gb-dlg", disparador);
    cargarBiblioteca().then(function (B) {
      if (!d.isConnected) return;
      var total = B.areas.reduce(function (s, a) { return s + a.pruebas.length; }, 0);
      d.querySelector(".gd-dlg__b").innerHTML = '<div class="gb"><div class="gb-top"><label class="gb-busca" for="gbQ">' + ic("search") + '<span class="sr-only">Buscar un análisis</span><input id="gbQ" type="search" autocomplete="off" placeholder="Buscar un análisis: hemoglobina, TSH, creatinina…"></label><p class="gb-n" id="gbN" role="status" aria-live="polite">' + total + ' análisis en ' + B.areas.length + ' áreas</p></div><div class="gb-areas">' +
        B.areas.map(function (a) {
          return '<details class="gb-area" style="--c:' + esc(a.color) + '" data-n="' + a.pruebas.length + '"><summary><span class="gb-ico">' + ic(I[a.icono] ? a.icono : "flask") + '</span><span class="gb-t">' + esc(a.nombre) + '</span><span class="gb-cnt">' + a.pruebas.length + '</span>' + ic("chev", "gb-chev") + '</summary><div class="gb-scroll" tabindex="0" role="region" aria-label="Análisis de ' + esc(a.nombre) + '"><table class="gb-tabla"><thead><tr><th scope="col">Análisis</th><th scope="col">Unidad</th><th scope="col">Valores de referencia</th></tr></thead><tbody>' + a.pruebas.map(filaBib).join("") + '</tbody></table></div></details>';
        }).join("") + '</div><p class="gb-vacio" id="gbV" hidden>Ningún análisis coincide con la búsqueda.</p><p class="gb-pie">' + esc(B.nota) + '</p></div>';
      var q = d.querySelector("#gbQ"), N = d.querySelector("#gbN"), V = d.querySelector("#gbV"), areas = [].slice.call(d.querySelectorAll(".gb-area"));
      function filtrar() {
        var t = norm(q.value).trim().split(/\s+/).filter(Boolean), n = 0, hay = 0;
        areas.forEach(function (a) {
          var c = 0; [].forEach.call(a.querySelectorAll(".gb-fila"), function (f) { var ok = !t.length || t.every(function (w) { return f.getAttribute("data-q").indexOf(w) >= 0; }); f.hidden = !ok; if (ok) c++; });
          a.hidden = !!t.length && c === 0; if (t.length) a.open = c > 0; if (c) hay++; n += c; a.querySelector(".gb-cnt").textContent = t.length ? c : a.getAttribute("data-n");
        });
        N.textContent = t.length ? n + " resultado" + (n === 1 ? "" : "s") + " en " + hay + " área" + (hay === 1 ? "" : "s") : total + " análisis en " + B.areas.length + " áreas"; V.hidden = !t.length || n > 0;
        if (!t.length) areas.forEach(function (a) { a.open = false; });
      }
      q.addEventListener("input", filtrar); q.focus();
    }, function () { d.querySelector(".gd-dlg__b").innerHTML = '<p class="gd-alerta" role="alert">No se pudo cargar la biblioteca. Revisa tu conexión e inténtalo de nuevo.</p>'; });
  }

  /* ---------- monitor vivo del hero ----------
     Anima el monitor de la ilustración (trazados de ECG, presión invasiva y pletismografía + cifras que varían poco). Es decorativo: los valores son de ejemplo.
     El lienzo se coloca sobre la región del monitor de hero.webp calculando cómo «cubre» la imagen el contenedor; sin movimiento reducido se anima, y se
     detiene al salir de la pantalla, al ocultar la pestaña o al cambiar de ruta. Coordenadas en píxeles de un recorte 4× de hero.webp (origen 1360,130). */
  var BX = 1370, BY = 160, BW = 230, BH = 270, OX = 1360, OY = 130, TRAZOS = [
    { id: "ecg", color: "#2bdc78", x0: 178, x1: 690, y0: 492, m: -0.19, amp: 118, k: "ecg" }, { id: "resp", color: "#2f78c4", x0: 178, x1: 690, y0: 578, m: -0.17, amp: 16, k: "resp" },
    { id: "abp", color: "#ec3a32", x0: 195, x1: 690, y0: 645, m: -0.143, amp: 72, k: "abp" }, { id: "pleth", color: "#cfe8ff", x0: 200, x1: 690, y0: 835, m: -0.12, amp: 108, k: "pleth" }];
  var CAJAS = [[[172, 398], [692, 332], [702, 842], [192, 866]], [[748, 276], [906, 266], [912, 402], [752, 410]], [[765, 440], [948, 432], [950, 614], [768, 616]], [[808, 656], [916, 650], [919, 782], [812, 787]], [[778, 860], [891, 855], [893, 987], [780, 991]]];
  function g(x, c, w) { var d = (x - c) / w; return Math.exp(-d * d); }
  var SENAL = {
    ecg: function (f) { return 0.11 * g(f, .12, .035) - 0.07 * g(f, .215, .012) + 1 * g(f, .245, .014) - 0.22 * g(f, .275, .014) + 0.26 * g(f, .52, .06); },
    abp: function (f) { return 0.95 * g(f, .30, .07) + 0.32 * g(f, .52, .06) - 0.1; }, pleth: function (f) { return 0.95 * g(f, .34, .085) + 0.26 * g(f, .62, .08); }
  };
  function monitorVivo(hero) {
    var cv = hero.querySelector(".gh-monitor"), img = hero.querySelector(".gh-hero__img"); if (!cv || !img || !cv.getContext) return function () {};
    var ctx = cv.getContext("2d"), reducido = raiz.matchMedia && raiz.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var sc = 1, N = 256, PERIODO = 4.6, buf = {}, ult = -1, fase = 0, tPrev = 0, hr = 118, spo2 = 98, rr = 24, tHr = 0, tSp = 0, raf = 0, vivo = true, visible = true, ro = null, io = null;
    TRAZOS.forEach(function (z) { buf[z.id] = new Float32Array(N); });
    function ubicar() {
      var cw = hero.clientWidth, ch = hero.clientHeight; if (!cw || !ch) return;
      var pos = (getComputedStyle(img).objectPosition || "50% 50%").split(" "), px = parseFloat(pos[0]) / 100, py = parseFloat(pos[1]) / 100; if (isNaN(px)) px = .5; if (isNaN(py)) py = .5;
      var s = Math.max(cw / 1600, ch / 900), ox = (cw - 1600 * s) * px, oy = (ch - 900 * s) * py, dpr = Math.min(2, raiz.devicePixelRatio || 1);
      cv.style.left = (ox + BX * s) + "px"; cv.style.top = (oy + BY * s) + "px"; cv.style.width = (BW * s) + "px"; cv.style.height = (BH * s) + "px";
      sc = s * dpr; cv.width = Math.max(1, Math.round(BW * sc)); cv.height = Math.max(1, Math.round(BH * sc));
      var fuera = ox + (BX + BW) * s < 0 || ox + BX * s > cw || oy + (BY + BH) * s < 0 || oy + BY * s > ch; cv.style.display = fuera ? "none" : "block"; dibujar(performance.now() / 1000);
    }
    function valor(k, f, t) { if (k === "resp") return Math.sin(2 * Math.PI * (t * rr / 60)) * 0.5 + 0.12 * Math.sin(t * 7.3); return SENAL[k](f) + 0.025 * Math.sin(t * 53 + f * 9); }
    function avanzar(t) {
      var dt = Math.min(.25, Math.max(0, t - tPrev)); tPrev = t; fase += dt * hr / 60;
      if (t > tHr) { tHr = t + 1.6 + Math.random() * 1.4; hr = Math.max(115, Math.min(121, hr + [-1, 0, 0, 1][Math.floor(Math.random() * 4)])); }
      if (t > tSp) { tSp = t + 5 + Math.random() * 6; spo2 = Math.random() < .25 ? 97 : 98; }
      var c = Math.floor(((t % PERIODO) / PERIODO) * N), dtS = PERIODO / N;
      if (ult < 0) ult = c;
      for (var i = ult; i !== c;) { i = (i + 1) % N; var ti = t - ((c - i + N) % N) * dtS, f = (((fase - (t - ti) * hr / 60) % 1) + 1) % 1; TRAZOS.forEach(function (z) { buf[z.id][i] = valor(z.k, f, ti); }); }
      ult = c; return c;
    }
    function dibujar(t) {
      var c = reducido ? -1 : ult < 0 ? 0 : ult;
      ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height); var k = sc / 4; ctx.setTransform(k, 0, 0, k, -(BX - OX) * 4 * k, -(BY - OY) * 4 * k);
      ctx.fillStyle = "#020509"; CAJAS.forEach(function (p) { ctx.beginPath(); ctx.moveTo(p[0][0], p[0][1]); for (var i = 1; i < p.length; i++) ctx.lineTo(p[i][0], p[i][1]); ctx.closePath(); ctx.fill(); });
      ctx.lineJoin = "round"; ctx.lineCap = "round";
      TRAZOS.forEach(function (z) {
        var b = buf[z.id], an = z.x1 - z.x0, gap = reducido ? 0 : 7; ctx.strokeStyle = z.color; ctx.lineWidth = 3.4; ctx.shadowColor = z.color; ctx.shadowBlur = 5; ctx.beginPath();
        var ini = true; for (var i = 0; i < N; i++) { if (!reducido && ((i - c - 1 + N) % N) < gap) { ini = true; continue; } var x = z.x0 + an * i / (N - 1), y = z.y0 + z.m * (x - z.x0) - b[i] * z.amp; if (ini) { ctx.moveTo(x, y); ini = false; } else ctx.lineTo(x, y); }
        ctx.stroke(); ctx.shadowBlur = 0;
      });
      function txt(s2, x, y, col, px2) { ctx.save(); ctx.translate(x, y); ctx.rotate(-0.08); ctx.font = "700 " + px2 + "px Inter, Arial, sans-serif"; ctx.fillStyle = col; ctx.fillText(s2, 0, 0); ctx.restore(); }
      txt(String(hr), 760, 396, "#22f08a", 150); txt("96/52", 770, 542, "#ff3b3b", 128); txt("(68)", 826, 602, "#ff4d4d", 78); txt(String(rr), 818, 772, "#ffe02e", 146); txt(String(spo2), 786, 975, "#36d6ff", 146);
    }
    function ciclo(ms) { raf = 0; if (!vivo) return; if (visible && !document.hidden) { avanzar(ms / 1000); dibujar(ms / 1000); } raf = raiz.requestAnimationFrame(ciclo); }
    function precarga() { if (reducido) { for (var j = 0; j < N; j++) { var tj = j * PERIODO / N, f = ((tj * hr / 60) % 1); TRAZOS.forEach(function (z) { buf[z.id][j] = valor(z.k, f, tj); }); } ult = N - 1; } }
    precarga(); ubicar();
    if (img.complete) ubicar(); else img.addEventListener("load", ubicar);
    if (raiz.ResizeObserver) { ro = new ResizeObserver(ubicar); ro.observe(hero); } else raiz.addEventListener("resize", ubicar);
    if (raiz.IntersectionObserver) { io = new IntersectionObserver(function (e) { visible = e[0].isIntersecting; }); io.observe(hero); }
    if (!reducido) raf = raiz.requestAnimationFrame(ciclo);
    return function () { vivo = false; if (raf) raiz.cancelAnimationFrame(raf); if (ro) ro.disconnect(); if (io) io.disconnect(); raiz.removeEventListener("resize", ubicar); };
  }
  var detenerMonitor = null, enHub = false, sinIntroProxima = false, introHubVista = false;   // la introducción principal se muestra la primera vez de cada visita (memoria: se reinicia al recargar o salir)
  window.addEventListener("hashchange", function () { if (!/^#\/guardia\/?$/.test(location.hash)) { enHub = false; if (detenerMonitor) { detenerMonitor(); detenerMonitor = null; } } });
  document.addEventListener("click", function (e) { var a = e.target.closest && e.target.closest('.gh-migas a[href="#/guardia"]'); if (a) sinIntroProxima = true; });   // volver desde un listado del propio módulo no repite la introducción
  function montar(cont, datosApp) {
    var ctx = { datos: datosApp };
    function listo() {
      if (!/^#\/guardia\/?$/.test(location.hash)) return;
      var mostrarIntro = !introHubVista; enHub = true; sinIntroProxima = false; if (mostrarIntro) introHubVista = true;
      if (detenerMonitor) detenerMonitor(); pintar(cont, ctx); var hero = cont.querySelector(".gh-hero"); detenerMonitor = hero ? monitorVivo(hero) : null;
      var I2 = M.guardiaIntro; if (I2 && mostrarIntro && !document.querySelector(".gi")) I2.mostrar({ alTerminar: function () { var b = cont.querySelector(".gh-btn"); if (b) b.focus({ preventScroll: true }); } });
    }
    var cargas = [];
    if (!raiz.MQP_CONSULTA && M.consulta && M.consulta.asegurarDatos) cargas.push(M.consulta.asegurarDatos());
    if (!raiz.MQP_GUARDIA_UCI && GD().asegurarUci) cargas.push(GD().asegurarUci());
    if (!cargas.length) { listo(); return; }
    cont.innerHTML = '<p class="muted" role="status">Cargando el centro de simulación…</p>';
    Promise.all(cargas.map(function (p) { return p.catch(function () {}); })).then(listo, listo);
  }
  M.guardiaHub = { montar: montar };
})(typeof window !== "undefined" ? window : this);
