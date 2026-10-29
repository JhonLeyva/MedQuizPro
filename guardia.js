/* MedQuizPlus · «Sobrevive a la Guardia» v3: pantallas (modos, temporizador, laboratorio, interconsulta, informe).
   La lógica pura vive en guardia_nucleo.js. El caso avanza SOLO por las transiciones validadas de guardia_casos.js: no hay IA dentro del juego.
   El progreso se guarda en M.progreso.preferencia("guardia") (se sincroniza con la cuenta); la sesión en curso, en el navegador.
   Simulación educativa: no dirige la atención de pacientes reales. */
(function (raiz) {
  "use strict";
  var M = raiz.MQP || (raiz.MQP = {});
  var G = function () { return M.guardiaNucleo; };
  /* Los datos de los casos (~0,4 MB) y del laboratorio se cargan solo al entrar al módulo, no en cada página de la app. */
  var SRC = (document.currentScript && document.currentScript.src) || "", BASE = SRC.replace(/guardia\.js(\?.*)?$/, ""), VER = (SRC.split("?")[1] || "");
  var cargaDatos = null;
  function cargarScript(nombre) { return new Promise(function (ok, mal) { var s = document.createElement("script"); s.src = BASE + nombre + (VER ? "?" + VER : ""); s.onload = ok; s.onerror = function () { mal(new Error(nombre)); }; document.head.appendChild(s); }); }
  function asegurarDatos() {
    if (raiz.MQP_GUARDIA && raiz.MQP_GUARDIA_LAB) return Promise.resolve();
    if (!cargaDatos) cargaDatos = Promise.all([cargarScript("guardia_casos.js"), cargarScript("guardia_lab.js")]).then(function () {}, function (e) { cargaDatos = null; throw e; });
    return cargaDatos;
  }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function url(u) { return /^https?:\/\//i.test(u || "") ? u : ""; }
  function enlace(href, txt) { return url(href) ? '<a href="' + esc(href) + '" target="_blank" rel="noopener noreferrer">' + esc(txt) + '</a>' : esc(txt); }
  function cargar() { var g = M.progreso && M.progreso.preferencia("guardia"); return g && g.casos ? g : { casos: {} }; }
  function guardar(g) { if (M.progreso) M.progreso.preferencia("guardia", g); }
  var AVISO = "Simulación educativa. No sirve para dirigir la atención de pacientes reales ni sustituye el juicio clínico ni los protocolos de tu institución.";
  var GRAV = ["Estable", "Inestable", "Crítico"];
  var DIA = 86400000, CLAVE_SESION = "mqp_guardia_sesion_v1", CLAVE_FX = "mqp_guardia_fx", CLAVE_MODO = "mqp_guardia_modo";
  var mem = {};
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { if (v === undefined) return mem[k] || null; if (v === null) delete mem[k]; else mem[k] = v; } return null; }
  function efectosActivos() { var f = ls(CLAVE_FX); if (f === "off") return false; if (f === "on") return true; return !(raiz.matchMedia && raiz.matchMedia("(prefers-reduced-motion: reduce)").matches); }
  var IMG = function () { return raiz.MQP_GUARDIA_IMG || {}; };
  var LAB = function () { return raiz.MQP_GUARDIA_LAB || { pruebas: [] }; };
  function prueba(id) { var p = LAB().pruebas; for (var i = 0; i < p.length; i++) if (p[i].id === id) return p[i]; return null; }
  function licenciaCorta(u) { var m = /licenses\/([a-z-]+)\/([\d.]+)/i.exec(u || ""); return m ? "CC " + m[1].toUpperCase() + " " + m[2] : "licencia abierta"; }
  function refN(caso, ids) { return (ids || []).map(function (r) { for (var i = 0; i < caso.referencias.length; i++) if (caso.referencias[i].id === r) return i + 1; return null; }).filter(Boolean); }

  /* ---------- diálogo modal accesible (reutilizado por laboratorio e interconsulta) ---------- */
  var dlgActual = null, dlgPrevio = null;
  function cerrarDialogo() { if (!dlgActual) return; try { dlgActual.close(); } catch (e) {} dlgActual.remove(); dlgActual = null; document.documentElement.classList.remove("vi-abierto"); if (dlgPrevio && document.body.contains(dlgPrevio)) dlgPrevio.focus(); dlgPrevio = null; }
  function dialogo(titulo, html, clase, disparador) {
    var prev = disparador || document.activeElement; cerrarDialogo(); dlgPrevio = prev;
    var d = document.createElement("dialog"); d.className = "gd-dlg " + (clase || ""); d.setAttribute("aria-labelledby", "gdDlgT");
    d.innerHTML = '<div class="gd-dlg__c"><header class="gd-dlg__h"><h2 id="gdDlgT">' + esc(titulo) + '</h2><button type="button" class="vi-x" data-cerrar aria-label="Cerrar">✕</button></header><div class="gd-dlg__b">' + html + '</div></div>';
    document.body.appendChild(d); dlgActual = d; document.documentElement.classList.add("vi-abierto");
    d.addEventListener("click", function (ev) { if (ev.target === d || (ev.target.closest && ev.target.closest("[data-cerrar]"))) cerrarDialogo(); });
    d.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrarDialogo(); });
    if (d.showModal) d.showModal(); else d.setAttribute("open", ""); d.querySelector("[data-cerrar]").focus(); return d;
  }

  /* ---------- laboratorio: resultados del paciente + catálogo de referencia ---------- */
  var MARCA = { bajo: "↓ Bajo", normal: "✓ Normal", alto: "↑ Alto", alterado: "⚠ Alterado" };
  /* mayúscula inicial en todo lo que se muestra de un resultado (valores, intervalos, títulos); respeta siglas y nombres de especie («Escherichia coli») */
  function mayus1(t) { t = t == null ? "" : String(t); return /^(pH|pCO|pO|mEq|mmol|mmHg|µ)/.test(t) ? t : t.charAt(0).toUpperCase() + t.slice(1); }
  function perfilTxt(p) { if (!p) return "perfil no definido"; return (p.sexo === "F" ? "mujer" : "varón") + ", " + p.edad_texto + (p.embarazo ? ", gestante (" + p.trimestre + ".º trimestre)" : ""); }
  function perfilNum(p) { return p ? { edad: p.edad, sexo: p.sexo, embarazo: !!p.embarazo, trimestre: p.trimestre } : {}; }
  function filaResultado(r, paciente, ocultar) {
    var t = prueba(r.prueba), N = G(); if (!t) return "";
    var iv = r.ref ? { bajo: r.ref.bajo, alto: r.ref.alto, texto: r.ref.texto || "" } : N.intervaloAplicable(t, perfilNum(paciente)), txt = iv ? (iv.texto || "") : "Sin intervalo cargado para este perfil";
    var m = null;
    if (t.cualitativa) m = typeof r.valor === "string" ? (r.valor.toLowerCase() === t.normal ? "normal" : "alterado") : null; else m = typeof r.valor === "number" && iv ? N.marca(r.valor, iv) : null;
    if (t.cualitativa) txt = t.normal === "normal" ? "Normal" : "Normal: " + mayus1(t.normal);
    var conv = ""; var c = N.CONVERSIONES[r.prueba]; if (c && typeof r.valor === "number" && t.unidad === c.de) conv = ' <span class="muted small">(≈ ' + (Math.round(N.convertir(r.prueba, r.valor, c.de, c.a) * 100) / 100) + " " + esc(c.a) + ")</span>";
    return '<tr><th scope="row">' + esc(mayus1(r.etiqueta || t.nombre)) + '</th><td><b>' + esc(mayus1(r.valor)) + '</b> ' + esc(t.unidad) + conv + '</td><td>' + esc(mayus1(txt)) + (r.ref ? ' <span class="muted small">(ensayo del caso)</span>' : "") + '</td><td>' + (ocultar || !m ? '<span class="muted small">' + (ocultar ? "Interpreta tú" : "—") + '</span>' : '<span class="gd-marca gd-marca--' + m + '">' + MARCA[m] + '</span>') + '</td></tr>';
  }
  function tablaResultados(res, paciente, nodoActivoSinResponder) {
    if (!res.length) return '<p class="muted">Todavía no hay resultados de laboratorio. Aparecen aquí cuando el caso los entrega; no se adelantan.</p>';
    return res.map(function (g) {
      var ocultar = g.ocultar && g.nodoId === nodoActivoSinResponder;
      return '<h3 class="gd-h3">' + esc(mayus1(g.titulo)) + '</h3><div class="gd-scroll"><table class="gd-tabla-lab"><thead><tr><th scope="col">Prueba</th><th scope="col">Resultado</th><th scope="col">Intervalo de referencia</th><th scope="col">Lectura</th></tr></thead><tbody>' +
        g.items.map(function (r) { return filaResultado(r, paciente, ocultar); }).join("") + '</tbody></table></div>' + (ocultar ? '<p class="muted small">Las marcas de alto/bajo se muestran cuando respondas esta decisión: la interpretación forma parte de lo que se evalúa.</p>' : "");
    }).join("");
  }
  function tarjetaCatalogo(t, paciente) {
    var N = G(), iv = N.intervaloAplicable(t, perfilNum(paciente)), aplic = iv ? iv.texto : (t.cualitativa ? "Normal: " + t.normal : "No hay un intervalo cargado para este perfil: consulta la norma o el laboratorio");
    var otros = (t.intervalos || []).filter(function (x) { return x !== iv; });
    var c = N.CONVERSIONES[t.id];
    return '<article class="gd-lab-t" data-cat="' + esc(t.categoria) + '"><h3>' + esc(t.nombre) + (t.sinonimos.length ? ' <span class="muted small">(' + t.sinonimos.map(esc).join(", ") + ')</span>' : "") + '</h3>' +
      '<p class="gd-lab-iv"><span class="gd-tipo">Intervalo de referencia</span> <b>' + esc(aplic) + '</b> ' + esc(t.unidad) + ' <span class="muted small">· para ' + esc(perfilTxt(paciente)) + '</span></p>' +
      (otros.length ? '<details class="gd-lab-otros"><summary>Otros intervalos cargados</summary><ul>' + otros.map(function (x) { return '<li>' + esc((x.sexo === "F" ? "Mujeres" : x.sexo === "M" ? "Varones" : "Todos") + (x.condicion ? " (" + x.condicion.replace("gestacion-t", "gestación, trimestre ") + ")" : "") + (x.edad_min != null ? ", ≥ " + x.edad_min + " años" : "") + ": " + x.texto + " " + t.unidad) + '</li>'; }).join("") + '</ul></details>' : "") +
      (c ? '<p class="small"><span class="gd-tipo">Conversión validada</span> 1 ' + esc(c.de) + ' = ' + esc(c.f) + ' ' + esc(c.a) + '</p>' : "") +
      (t.umbrales.length ? '<ul class="gd-lab-um">' + t.umbrales.map(function (u) { return '<li><span class="gd-tipo gd-tipo--' + esc(u.tipo) + '">' + esc({ umbral_diagnostico: "Umbral diagnóstico", objetivo_terapeutico: "Objetivo terapéutico", valor_critico: "Valor crítico" }[u.tipo] || u.tipo) + '</span> ' + esc(u.texto) + (u.pmid ? ' ' + enlace("https://pubmed.ncbi.nlm.nih.gov/" + u.pmid + "/", "PMID " + u.pmid) : "") + '</li>'; }).join("") + '</ul>' : "") +
      (t.advertencias.length ? '<ul class="gd-lab-adv small">' + t.advertencias.map(function (a) { return '<li>⚠ ' + esc(a) + '</li>'; }).join("") + '</ul>' : "") +
      '<p class="muted small">Método: ' + esc(t.metodo) + ' · <b>' + esc(t.fuente_tipo === "educativo" ? "Intervalo educativo" : "Fuente verificada") + '</b>: ' + esc(t.fuente) + (t.criticos ? "" : " · Valores críticos: no incluidos (cada laboratorio define los suyos).") + '</p></article>';
  }
  function abrirLaboratorio(caso, res, nodoActivoSinResponder, disparador) {
    var cats = {}; LAB().pruebas.forEach(function (t) { cats[t.categoria] = 1; });
    var html = '<div class="gd-tabs" role="tablist" aria-label="Laboratorio"><button type="button" role="tab" id="gdT1" aria-selected="true" aria-controls="gdP1" data-tab="1">Resultados del paciente</button><button type="button" role="tab" id="gdT2" aria-selected="false" aria-controls="gdP2" data-tab="2" tabindex="-1">Catálogo de referencia</button></div>' +
      '<div role="tabpanel" id="gdP1" aria-labelledby="gdT1">' + tablaResultados(res, caso.paciente, nodoActivoSinResponder) + '</div>' +
      '<div role="tabpanel" id="gdP2" aria-labelledby="gdT2" hidden><p class="gd-aviso" role="note">' + esc(LAB().aviso) + ' Distingue <b>intervalo de referencia</b>, <b>umbral diagnóstico</b>, <b>objetivo terapéutico</b> y <b>valor crítico</b>: no son lo mismo.</p>' +
      '<div class="gd-lab-f"><label for="gdLabQ">Buscar prueba</label><input id="gdLabQ" type="search" autocomplete="off" placeholder="p. ej. potasio, TGO, lactato"><label for="gdLabC">Categoría</label><select id="gdLabC"><option value="">Todas</option>' + Object.keys(cats).map(function (c) { return '<option>' + esc(c) + '</option>'; }).join("") + '</select></div>' +
      '<p class="muted small" id="gdLabN" aria-live="polite"></p><div id="gdLabL">' + LAB().pruebas.map(function (t) { return tarjetaCatalogo(t, caso.paciente); }).join("") + '</div></div>';
    var d = dialogo("Laboratorio y valores de referencia", html, "gd-dlg--lab", disparador);
    function tab(n) { [1, 2].forEach(function (i) { var b = d.querySelector("#gdT" + i), on = i === n; b.setAttribute("aria-selected", on); b.tabIndex = on ? 0 : -1; d.querySelector("#gdP" + i).hidden = !on; }); }
    [].forEach.call(d.querySelectorAll("[data-tab]"), function (b) { b.addEventListener("click", function () { tab(+b.getAttribute("data-tab")); }); b.addEventListener("keydown", function (ev) { if (ev.key === "ArrowRight" || ev.key === "ArrowLeft") { var n = +b.getAttribute("data-tab") === 1 ? 2 : 1; tab(n); d.querySelector("#gdT" + n).focus(); } }); });
    var q = d.querySelector("#gdLabQ"), c = d.querySelector("#gdLabC");
    function filtrar() {
      var tx = q.value.trim().toLowerCase(), n = 0;
      [].forEach.call(d.querySelectorAll(".gd-lab-t"), function (a) { var ok = (!c.value || a.getAttribute("data-cat") === c.value) && (!tx || a.textContent.toLowerCase().indexOf(tx) >= 0); a.hidden = !ok; if (ok) n++; });
      d.querySelector("#gdLabN").textContent = n + " prueba" + (n === 1 ? "" : "s") + " mostrada" + (n === 1 ? "" : "s");
    }
    q.addEventListener("input", filtrar); c.addEventListener("change", filtrar); filtrar();
  }


  /* catálogo de referencia sin caso (acceso rápido del centro de simulación): el intervalo se elige según un perfil genérico, no el de un paciente */
  var PERFILES = [{ id: "m", txt: "Varón adulto", p: { edad: 30, edad_texto: "30 años", sexo: "M", embarazo: false } }, { id: "f", txt: "Mujer adulta no gestante", p: { edad: 30, edad_texto: "30 años", sexo: "F", embarazo: false } },
    { id: "g1", txt: "Gestante, 1.er trimestre", p: { edad: 30, edad_texto: "30 años", sexo: "F", embarazo: true, trimestre: 1 } }, { id: "g2", txt: "Gestante, 2.º trimestre", p: { edad: 30, edad_texto: "30 años", sexo: "F", embarazo: true, trimestre: 2 } }, { id: "g3", txt: "Gestante, 3.er trimestre", p: { edad: 30, edad_texto: "30 años", sexo: "F", embarazo: true, trimestre: 3 } }];
  function abrirCatalogo(disparador) {
    var cats = {}; LAB().pruebas.forEach(function (t) { cats[t.categoria] = 1; });
    var html = '<p class="gd-aviso" role="note">' + esc(LAB().aviso) + ' Distingue <b>intervalo de referencia</b>, <b>umbral diagnóstico</b>, <b>objetivo terapéutico</b> y <b>valor crítico</b>: no son lo mismo.</p>' +
      '<div class="gd-lab-f"><label for="gdLabP">Perfil</label><select id="gdLabP">' + PERFILES.map(function (x) { return '<option value="' + x.id + '">' + esc(x.txt) + '</option>'; }).join("") + '</select><label for="gdLabQ">Buscar prueba</label><input id="gdLabQ" type="search" autocomplete="off" placeholder="p. ej. potasio, TGO, lactato"><label for="gdLabC">Categoría</label><select id="gdLabC"><option value="">Todas</option>' + Object.keys(cats).map(function (c) { return '<option>' + esc(c) + '</option>'; }).join("") + '</select></div>' +
      '<p class="muted small" id="gdLabN" aria-live="polite"></p><div id="gdLabL"></div>';
    var d = dialogo("Laboratorio y valores de referencia", html, "gd-dlg--lab", disparador), P = d.querySelector("#gdLabP"), q = d.querySelector("#gdLabQ"), c = d.querySelector("#gdLabC");
    function pintar() {
      var per = PERFILES.filter(function (x) { return x.id === P.value; })[0].p;
      d.querySelector("#gdLabL").innerHTML = LAB().pruebas.map(function (t) { return tarjetaCatalogo(t, per); }).join("");
      var tx = q.value.trim().toLowerCase(), n = 0;
      [].forEach.call(d.querySelectorAll(".gd-lab-t"), function (a) { var ok = (!c.value || a.getAttribute("data-cat") === c.value) && (!tx || a.textContent.toLowerCase().indexOf(tx) >= 0); a.hidden = !ok; if (ok) n++; });
      d.querySelector("#gdLabN").textContent = n + " prueba" + (n === 1 ? "" : "s") + " mostrada" + (n === 1 ? "" : "s");
    }
    P.addEventListener("change", pintar); q.addEventListener("input", pintar); c.addEventListener("change", pintar); pintar();
  }

  /* ---------- lista y recomendaciones ---------- */
  var cacheEst = { clave: "", valor: null };
  function estadisticasAlumno(datos) {
    if (!datos || !datos.preguntas || !M.progreso) return null;
    var p = M.progreso.leer(), resp = p.respuestas || {}, ids = Object.keys(resp), tmax = 0;
    ids.forEach(function (i) { if (resp[i] && resp[i].t > tmax) tmax = resp[i].t; });
    var clave = ids.length + ":" + tmax + ":" + Math.floor(Date.now() / DIA);
    if (cacheEst.clave !== clave) cacheEst = { clave: clave, valor: G().estadisticas(datos.preguntas, resp, Date.now()) };
    return cacheEst.valor;
  }
  function tarjetaRecomendada(rec) {
    var MIN = G().MIN_TOTAL, NIVEL = G().NIVEL;
    var enc = rec.modo === "personalizado" ? "Casos recomendados para ti" : rec.modo === "provisional" ? "Casos recomendados para ti (provisional)" : "Por dónde empezar";
    var intro = rec.modo === "invitacion"
      ? "Todavía no tenemos suficientes respuestas tuyas en el banco (" + rec.total + " de " + MIN + ") para recomendarte con criterio, así que no inventamos una recomendación. Estos son buenos puntos de partida; responde preguntas en el banco" + (rec.faltan ? " (te faltan " + rec.faltan + ")" : "") + " para personalizarlos."
      : rec.modo === "provisional" ? "Tenemos pocas respuestas en las especialidades de estos casos, por eso la sugerencia es provisional y se afina a medida que practicas."
        : "Calculado con tus propias respuestas en el banco (acierto por especialidad con su intervalo de confianza, tendencia reciente frente a histórica, temas con fallos repetidos y tu historial en la guardia).";
    return '<section class="card card--spaced gd-rec" aria-labelledby="gdRecT"><h2 class="card__h" id="gdRecT">' + enc + '</h2><p class="muted small">' + esc(intro) + '</p><ul class="gd-rec__l">' + rec.items.map(function (i) {
      return '<li class="gd-rec__i"><p class="gd-niv">' + esc(NIVEL[i.caso.dificultad]) + ' · ' + esc(i.caso.especialidad) + (i.provisional ? ' · <span class="gd-prov">provisional</span>' : "") + '</p><h3>' + esc(i.caso.titulo) + '</h3><ul class="gd-rec__m">' + i.motivos.map(function (m) { return '<li>' + esc(m) + '</li>'; }).join("") + '</ul><a class="btn btn--primary btn--sm" href="#/guardia/' + esc(i.caso.id) + '">Empezar el caso</a></li>';
    }).join("") + '</ul><p class="muted small">Es una sugerencia, no una restricción: todos los casos están abiertos abajo. Se calcula en tu navegador con tu progreso; no se envía nada a ningún servidor ni se comparte con otros alumnos.</p></section>';
  }
  function especialidades(casos) { var s = {}; casos.forEach(function (c) { c.especialidad.split(" · ").forEach(function (x) { s[x] = 1; }); }); return Object.keys(s).sort(); }
  function lista(cont, datos) {
    var g = cargar(), casos = raiz.MQP_GUARDIA || [], NIVEL = G().NIVEL;
    var hechos = casos.filter(function (c) { return g.casos[c.id]; }).length;
    var rec = G().recomendar(casos, g, estadisticasAlumno(datos), Date.now());
    var h = '<nav class="gh-migas" aria-label="Ruta"><a href="#/guardia">Centro de simulación</a><span aria-hidden="true">›</span><span aria-current="page">Guardia de emergencias</span></nav>' +
      '<header class="gh-modal gh-modal--rojo"><img class="gh-modal__img" src="../guardia/portadas/emergencias.webp" alt="" width="800" height="600" loading="eager" decoding="async"><div class="gh-modal__txt"><p class="gh-kicker">Emergencias</p><h1 class="gh-modal__t">Guardia de emergencias</h1><p>Casos clínicos por decisiones con cinco alternativas, pruebas de laboratorio, imágenes reales, tiempo por etapa e interconsulta. Al final recibes un informe con tu razonamiento, tus errores y qué reforzar. Complementa al banco de preguntas.</p></div></header>' +
      '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
      '<dl class="gd-kpis"><div class="gd-kpi"><dt>Casos completados</dt><dd>' + hechos + ' / ' + casos.length + '</dd></div><div class="gd-kpi"><dt>Mejor puntaje medio</dt><dd>' + (hechos ? Math.round(casos.reduce(function (s, c) { return s + (g.casos[c.id] ? g.casos[c.id].mejor : 0); }, 0) / hechos) + " %" : "—") + '</dd></div></dl>' +
      tarjetaRecomendada(rec) +
      '<div class="gd-filtro"><label for="gdFil">Explorar por especialidad</label><select id="gdFil"><option value="">Todas las especialidades (' + casos.length + ' casos)</option>' + especialidades(casos).map(function (e) { return '<option value="' + esc(e) + '">' + esc(e) + '</option>'; }).join("") + '</select></div>' +
      '<ul class="gd-lista" id="gdLista">' + casos.map(function (c) {
        var r = g.casos[c.id], tieneImg = (c.imagenes || []).length, nDec = contarDecisiones(c);
        return '<li class="gd-caso" data-esp="' + esc(c.especialidad) + '"><p class="gd-niv">' + esc(NIVEL[c.dificultad]) + ' · ' + esc(c.especialidad) + '</p><h2>' + esc(c.titulo) + '</h2><p>' + esc(c.resumen) + '</p>' +
          '<p class="muted small">≈ ' + c.duracion_min + ' min · ' + nDec + ' decisiones en la ruta óptima · ' + c.referencias.length + ' referencias' + (tieneImg ? ' · ' + (tieneImg === 1 ? "1 imagen real" : tieneImg + " imágenes reales") : "") + '</p>' +
          (r ? '<p class="gd-mejor">Mejor puntaje: <b>' + r.mejor + ' %</b> · Intentos: ' + r.intentos + '</p>' : "") +
          '<a class="btn btn--primary btn--sm" href="#/guardia/' + esc(c.id) + '">' + (r ? "Reintentar el caso" : "Empezar el caso") + '</a></li>';
      }).join("") + '</ul>';
    cont.innerHTML = h;
    var f = cont.querySelector("#gdFil");
    f.addEventListener("change", function () { [].forEach.call(cont.querySelectorAll(".gd-caso"), function (li) { li.hidden = !!f.value && li.getAttribute("data-esp").split(" · ").indexOf(f.value) < 0; }); });
  }
  function contarDecisiones(caso) { var id = caso.inicio, n = 0; while (!caso.nodos[id].final && n < 60) { var o = caso.nodos[id].decisiones.filter(function (d) { return d.calidad === "optima"; })[0]; id = o.siguiente; n++; } return n; }

  /* ---------- imágenes ---------- */
  function abrirImagen(id, disparador) {
    var im = IMG()[id]; if (!im || !M.visorImagen) return;
    M.visorImagen.abrir({ titulo: "Imagen del caso", alt: im.alt, imagenes: [im.src],
      atribucion: { nota: "Imagen real de la literatura médica publicada, de otro paciente.", licencia: licenciaCorta(im.licencia), licenciaUrl: im.licencia, fuente: "autoría y fuente completas en el informe final del caso" } }, disparador);
  }
  function figura(id, consigna, final) {
    var im = IMG()[id]; if (!im) return "";
    return '<figure class="gd-img"><button type="button" class="gd-img__b" data-img="' + esc(id) + '" aria-label="Ampliar la imagen del caso (zoom y desplazamiento)"><img src="' + esc(im.src) + '" alt="' + esc(im.alt) + '" width="' + im.ancho + '" height="' + im.alto + '"></button>' +
      '<figcaption>' + (consigna ? '<strong>' + esc(consigna) + '</strong><br>' : "") + 'Imagen real de la literatura médica publicada, de otro paciente (' + esc(licenciaCorta(im.licencia)) + ').' + (final ? ' Autoría y fuente en la ficha de abajo.' : ' La autoría y la fuente completas aparecen en el informe final para no adelantar el diagnóstico.') + ' Pulsa la imagen para ampliarla, desplazarla y ajustar brillo y contraste.</figcaption></figure>';
  }
  function ligarImagenes(cont) { [].forEach.call(cont.querySelectorAll("[data-img]"), function (b) { b.addEventListener("click", function () { abrirImagen(b.getAttribute("data-img"), b); }); }); }

  /* ---------- un caso ---------- */
  var detener = null;                  // limpia temporizadores/listeners del caso que se está jugando
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
  function guardarSesion(e) { ls(CLAVE_SESION + ":" + e.caso, G().serializarSesion(e)); }
  function borrarSesion(id) { ls(CLAVE_SESION + ":" + id, null); }

  function preludio(cont, caso) {
    var N = G(), crudo = ls(CLAVE_SESION + ":" + caso.id), ses = crudo ? N.restaurarSesion(crudo, caso) : null, modo = ls(CLAVE_MODO) === "cronometrada" ? "cronometrada" : "entrenamiento";
    if (crudo && !ses) borrarSesion(caso.id);                         // sesión incompatible con la versión actual del caso: se descarta
    var tiempos = Object.keys(N.TIPOS).map(function (k) { return '<li>' + esc(N.TIPOS[k]) + ': ' + N.TIEMPOS[k] + ' s por defecto (' + (k === "critica" ? "30–60 s" : "1–3 min") + ' según la complejidad; cada decisión fija el suyo)</li>'; }).join("");
    cont.innerHTML = '<div class="gd-juego"><header class="gd-top"><a class="link-arrow" href="#/guardia/emergencias">← Guardia de emergencias</a><h1>' + esc(caso.titulo) + '</h1></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
      (ses ? '<section class="card card--spaced gd-reanudar" aria-labelledby="gdRe"><h2 class="card__h" id="gdRe">Tienes este caso en curso</h2><p>' + esc(N.MODOS[ses.modo].nombre) + ' · decisión ' + (ses.camino.length + 1) + '. ' + (ses.modo === "cronometrada" ? "El reloj de la decisión actual conserva el tiempo ya usado." : "") + '</p><button type="button" class="btn btn--primary" id="gdContinuar">Continuar donde lo dejé</button> <button type="button" class="btn btn--ghost" id="gdReiniciar">Empezar de nuevo</button></section>' : "") +
      '<section class="card card--spaced"><h2 class="card__h">Elige cómo jugar</h2><p>' + esc(caso.contexto) + '</p><fieldset class="gd-modos"><legend class="sr-only">Modo de juego</legend>' +
      Object.keys(N.MODOS).map(function (k) { var m = N.MODOS[k]; return '<label class="gd-modo"><input type="radio" name="gdModo" value="' + k + '"' + (k === modo ? " checked" : "") + '><span><b>' + esc(m.nombre) + '</b><br><span class="muted small">' + esc(m.texto) + '</span></span></label>'; }).join("") + '</fieldset>' +
      '<ul class="muted small gd-tiempos">' + tiempos + '</ul><p class="muted small">La velocidad es un indicador secundario: la puntuación principal refleja la calidad de tus decisiones, ponderada por su importancia clínica. Si se agota el tiempo se aplica la conducta de espera definida para esa decisión, y se explica al final.</p>' +
      '<label class="gd-tiempo"><input type="checkbox" id="gdFx"' + (efectosActivos() ? " checked" : "") + '> Efectos visuales del monitor (alertas y pulso al deteriorarse; se respeta «reducir movimiento»)</label>' +
      '<p><button type="button" class="btn btn--primary" id="gdEmpezar">Empezar el caso</button></p></section></div>';
    var fx = cont.querySelector("#gdFx"); fx.addEventListener("change", function () { ls(CLAVE_FX, fx.checked ? "on" : "off"); });
    function modoSel() { var r = cont.querySelector("input[name=gdModo]:checked"); return r ? r.value : "entrenamiento"; }
    cont.querySelector("#gdEmpezar").addEventListener("click", function () { var m = modoSel(); ls(CLAVE_MODO, m); borrarSesion(caso.id); jugar(cont, caso, m, null); });
    if (ses) {
      cont.querySelector("#gdContinuar").addEventListener("click", function () { jugar(cont, caso, ses.modo, ses); });
      cont.querySelector("#gdReiniciar").addEventListener("click", function () { borrarSesion(caso.id); preludio(cont, caso); });
    }
  }

  function jugar(cont, caso, modo, sesion) {
    var N = G(), MODO = N.MODOS[modo], maxTotal = N.maximo(caso, caso.inicio);
    var nodoId = sesion ? sesion.nodo : caso.inicio, nodo = caso.nodos[nodoId], puntos = sesion ? sesion.puntos : 0, camino = sesion ? sesion.camino.slice() : [], vistas = sesion ? sesion.vistas.slice() : [];
    var resultados = sesion ? sesion.resultados.slice() : [], ayudaNodo = sesion ? sesion.ayudaNodo.slice() : [], reloj = null, resuelto = false, tInicio = 0, ticker = null, persistidor = null, pausado = false, usadoRestaurado = sesion ? sesion.usadoMs : 0, ultimoAviso = "";
    if (detener) detener();

    function estado() { return { caso: caso.id, modo: modo, nodo: nodoId, puntos: puntos, vistas: vistas, usadoMs: reloj ? reloj.usadoMs() : 0, pausado: pausado, ayudaNodo: ayudaNodo, t: Date.now(), camino: camino, resultados: resultados }; }
    function persistir() { guardarSesion(estado()); }
    function parar() { if (ticker) { clearInterval(ticker); ticker = null; } if (persistidor) { clearInterval(persistidor); persistidor = null; } if (reloj) reloj.detener(); }
    function salir() { parar(); persistir(); window.removeEventListener("hashchange", alIrse); window.removeEventListener("pagehide", persistir); document.removeEventListener("keydown", teclas); cerrarDialogo(); if (detener === salir) detener = null; }
    function alIrse() { if (!/^#\/guardia\//.test(location.hash) || location.hash.indexOf(caso.id) < 0) salir(); }
    function terminar() { parar(); window.removeEventListener("hashchange", alIrse); window.removeEventListener("pagehide", persistir); document.removeEventListener("keydown", teclas); if (detener === salir) detener = null; }
    detener = salir; window.addEventListener("hashchange", alIrse); window.addEventListener("pagehide", persistir);
    function teclas(ev) {
      if (dlgActual || resuelto || pausado || !nodo || nodo.final) return; var t = ev.target && ev.target.tagName; if (t === "INPUT" || t === "TEXTAREA" || t === "SELECT" || ev.ctrlKey || ev.metaKey || ev.altKey) return;
      var k = (ev.key || "").toUpperCase(); if (N.LETRAS.indexOf(k) >= 0) { var b = cont.querySelector('.gd-op[data-id="' + k + '"]'); if (b && !b.disabled) { ev.preventDefault(); b.click(); } }
    }
    document.addEventListener("keydown", teclas);

    function bloqueResultados() {
      var n = nodo.laboratorio; if (!n) return "";
      return '<section class="gd-labn" aria-label="Resultados de laboratorio"><h3 class="gd-h3">' + esc(n.titulo) + '</h3><div class="gd-scroll"><table class="gd-tabla-lab"><thead><tr><th scope="col">Prueba</th><th scope="col">Resultado</th><th scope="col">Intervalo de referencia</th><th scope="col">Lectura</th></tr></thead><tbody>' + n.resultados.map(function (r) { return filaResultado(r, caso.paciente, n.ocultar_marcas); }).join("") + '</tbody></table></div>' + (n.ocultar_marcas ? '<p class="muted small">Interpreta los valores comparándolos con el intervalo de referencia: la lectura se muestra al responder.</p>' : "") + '<p class="muted small">Intervalos educativos, no de un laboratorio peruano (detalle en «Laboratorio y valores de referencia»).</p></section>';
    }
    function pintarReloj() {
      var t = cont.querySelector("#gdReloj"); if (!t || !reloj) return;
      var s = reloj.restanteS(), niv = reloj.nivel();
      t.textContent = N.formatoTiempo(s); t.setAttribute("data-nivel", niv); cont.querySelector("#gdBarra").style.width = Math.max(0, reloj.restanteMs() / (reloj.limiteS * 10)) + "%";
      cont.querySelector("#gdRelojCaja").className = "gd-reloj gd-reloj--" + niv;
      var live = cont.querySelector("#gdRelojLive"), msg = niv === "aviso" && ultimoAviso !== "aviso" ? "Quedan " + s + " segundos" : niv === "agotado" ? "Tiempo agotado" : "";
      if (msg && ultimoAviso !== niv) { live.textContent = msg; ultimoAviso = niv; }
    }
    function paso() {
      parar(); cerrarDialogo();
      if (nodo.final) { fin(); return; }
      resuelto = false; pausado = false; ultimoAviso = ""; tInicio = Date.now();
      if (nodo.imagen && vistas.indexOf(nodo.imagen.id) < 0) vistas.push(nodo.imagen.id);
      if (nodo.laboratorio && !resultados.some(function (r) { return r.nodoId === nodoId; })) resultados.push({ nodoId: nodoId, titulo: nodo.laboratorio.titulo, ocultar: !!nodo.laboratorio.ocultar_marcas, items: nodo.laboratorio.resultados });
      var vit = Object.keys(nodo.vitales).map(function (k) { return '<div><dt>' + esc(k) + '</dt><dd>' + esc(nodo.vitales[k]) + '</dd></div>'; }).join("");
      var previas = vistas.filter(function (i) { return !nodo.imagen || i !== nodo.imagen.id; }), fx = efectosActivos(), tipo = nodo.tipo || "diagnostica";
      var limite = N.tiempoNodo(nodo), usadoPrevio = usadoRestaurado; usadoRestaurado = 0;
      cont.innerHTML = '<div class="gd-juego' + (fx ? " gd-fx" : "") + '"><header class="gd-top"><a class="link-arrow" href="#/guardia/emergencias">← Guardia de emergencias</a><h1>' + esc(caso.titulo) + '</h1>' +
        '<p class="gd-prog">Decisión ' + (camino.length + 1) + ' · Puntaje ' + puntos + ' de ' + N.maximoRecorrido(camino) + ' posibles hasta ahora · ' + esc(MODO.nombre) + '</p></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<div class="gd-barra-acc"><button type="button" class="btn btn--ghost btn--sm" id="gdLabBtn">🧪 Laboratorio y valores de referencia</button>' + (MODO.ayuda ? ' <button type="button" class="btn btn--ghost btn--sm" id="gdEspBtn">👩‍⚕️ Consultar al especialista</button>' : '') +
        (MODO.cronometro ? ' <button type="button" class="btn btn--ghost btn--sm" id="gdPausa" aria-pressed="false">⏸ Pausar</button>' : "") + '</div>' +
        (MODO.cronometro ? '<div class="gd-reloj gd-reloj--normal" id="gdRelojCaja"><p class="gd-reloj__t"><span class="gd-reloj__tipo">' + esc(N.TIPOS[tipo]) + '</span> · Tiempo restante: <b id="gdReloj" role="timer" aria-live="off">' + N.formatoTiempo(limite) + '</b></p><div class="gd-reloj__b" aria-hidden="true"><i id="gdBarra"></i></div><p class="sr-only" id="gdRelojLive" aria-live="polite"></p></div>' : "") +
        (nodo.deterioro ? '<p class="gd-alerta" role="alert">⚠ El estado del paciente empeora. Reevalúa y actúa.</p>' : "") +
        (camino.length === 0 ? '<p class="muted small gd-ctx">' + esc(caso.contexto) + '</p>' : "") +
        '<section class="gd-paciente gd-paciente--g' + nodo.gravedad + '" aria-label="Estado del paciente"><div class="gd-grav gd-grav--' + nodo.gravedad + '" role="status"><span aria-hidden="true"></span>Estado: <b>' + GRAV[nodo.gravedad] + '</b></div>' +
        '<p class="gd-estado">' + esc(nodo.estado) + '</p><dl class="gd-vit">' + vit + '</dl></section>' + bloqueResultados() +
        (nodo.imagen ? figura(nodo.imagen.id, nodo.imagen.consigna) : "") +
        (previas.length ? '<p class="gd-prev"><span>Imágenes de este caso (puedes volver a verlas):</span> ' + previas.map(function (i, k) { return '<button type="button" class="btn btn--ghost btn--sm" data-img="' + esc(i) + '">Ver imagen ' + (k + 1) + '</button>'; }).join(" ") + '</p>' : "") +
        '<div id="gdPregunta"><h2 class="gd-q" id="gdQ">' + esc(nodo.pregunta || "¿Qué haces ahora?") + '</h2><p class="muted small">Elige una de las cinco alternativas (también puedes pulsar A, B, C, D o E).</p><div class="gd-ops" role="group" aria-labelledby="gdQ">' +
        nodo.decisiones.map(function (o) { return '<button type="button" class="gd-op" data-id="' + esc(o.id) + '"><span class="gd-op__l" aria-hidden="true">' + esc(o.id) + '</span><span class="gd-op__t"><span class="sr-only">Alternativa ' + esc(o.id) + ': </span>' + esc(o.texto) + '</span></button>'; }).join("") + '</div></div>' +
        '<div id="gdFb" role="status" aria-live="polite"></div></div>';
      ligarImagenes(cont);
      cont.querySelector("#gdLabBtn").addEventListener("click", function (ev) { abrirLaboratorio(caso, resultados, resuelto ? null : nodoId, ev.currentTarget); });
      var eb = cont.querySelector("#gdEspBtn"); if (eb) eb.addEventListener("click", function (ev) { abrirEspecialista(ev.currentTarget); });
      [].forEach.call(cont.querySelectorAll(".gd-op"), function (b) { b.addEventListener("click", function () { elegir(b.getAttribute("data-id"), false); }); });
      if (MODO.cronometro) {
        reloj = N.crearReloj(limite, Date.now, usadoPrevio); reloj.iniciar(); pintarReloj();
        ticker = setInterval(function () { pintarReloj(); if (reloj.agotado() && !resuelto) elegir(null, true); }, 250);
        var pb = cont.querySelector("#gdPausa"); pb.addEventListener("click", function () { alternarPausa(pb); });
      } else { reloj = N.crearReloj(1e9, Date.now, 0); reloj.iniciar(); }
      persistidor = setInterval(persistir, 5000); persistir();
    }
    function alternarPausa(pb) {
      if (resuelto) return; var ops = cont.querySelector("#gdPregunta");
      if (!pausado) { pausado = true; reloj.pausar(); ops.hidden = true; pb.setAttribute("aria-pressed", "true"); pb.textContent = "▶ Reanudar"; cont.querySelector("#gdFb").innerHTML = '<p class="gd-pausa">Caso en pausa. El tiempo no corre y las alternativas están ocultas hasta que reanudes.</p>'; persistir(); }
      else { pausado = false; reloj.iniciar(); ops.hidden = false; pb.setAttribute("aria-pressed", "false"); pb.textContent = "⏸ Pausar"; cont.querySelector("#gdFb").innerHTML = ""; }
    }
    function abrirEspecialista(disparador) {
      var esp = caso.especialistas || [], a = nodo.ayuda || {}, rec = a.especialista || (esp[0] && esp[0].id), sel = rec;
      var html = '<p class="muted small">La interconsulta usa la lógica validada del caso y sus fuentes; no improvisa. Orientar no es un error, pero en entrenamiento las ayudas más concretas restan puntos pedagógicos: nivel 1 sin penalización, nivel 2 −' + N.PENAL_AYUDA[2] + ' y nivel 3 −' + N.PENAL_AYUDA[3] + ' (antes de ponderar).</p>' +
        '<fieldset class="gd-esp"><legend>Especialidad</legend>' + esp.map(function (e) { return '<label><input type="radio" name="gdEsp" value="' + esc(e.id) + '"' + (e.id === rec ? " checked" : "") + '> ' + esc(e.nombre) + '</label>'; }).join("") + '<p><button type="button" class="btn btn--ghost btn--sm" id="gdEspRec">Usar la recomendada por el sistema</button></p></fieldset>' +
        '<div class="gd-niveles"><button type="button" class="btn btn--ghost" data-niv="1">1 · Orientación general</button><button type="button" class="btn btn--ghost" data-niv="2">2 · Ayuda dirigida (−' + N.PENAL_AYUDA[2] + ')</button><button type="button" class="btn btn--ghost" data-niv="3">3 · Interconsulta completa (−' + N.PENAL_AYUDA[3] + ')</button></div><div id="gdEspR" role="status" aria-live="polite"></div>';
      var d = dialogo("Consultar al especialista", html, "gd-dlg--esp", disparador);
      d.querySelector("#gdEspRec").addEventListener("click", function () { var r = d.querySelector('input[name=gdEsp][value="' + rec + '"]'); if (r) { r.checked = true; r.focus(); } });
      [].forEach.call(d.querySelectorAll("[data-niv]"), function (b) { b.addEventListener("click", function () {
        var niv = +b.getAttribute("data-niv"), r = d.querySelector("input[name=gdEsp]:checked"), resp = N.consultarEspecialista(caso, nodoId, niv, r ? r.value : rec);
        if (resp.pertinente) { ayudaNodo.push(niv); persistir(); }
        d.querySelector("#gdEspR").innerHTML = '<div class="gd-resp' + (resp.pertinente ? "" : " gd-resp--no") + '"><p class="gd-resp__q">' + (resp.pertinente ? esc(resp.especialista || "Especialista") + " · nivel " + niv : "Sin interconsulta registrada") + '</p><p>' + esc(resp.texto) + '</p></div>';
      }); });
    }
    function elegir(id, agotado) {
      if (resuelto || pausado) return; resuelto = true; parar();
      var d = agotado ? nodo.decisiones.filter(function (x) { return x.omision; })[0] : nodo.decisiones.filter(function (x) { return x.id === id; })[0]; if (!d) { resuelto = false; return; }
      var seg = Math.round(Math.min(reloj ? reloj.usadoMs() : 0, MODO.cronometro ? N.tiempoNodo(nodo) * 1000 : 1e9) / 1000), niv = ayudaNodo.reduce(function (m, x) { return Math.max(m, x); }, 0);
      puntos += agotado ? 0 : N.puntosNodo(nodo, d, niv); camino.push({ nodoId: nodoId, nodo: nodo, decision: d, decisionId: d.id, segundos: seg, ayuda: ayudaNodo.slice(), agotado: !!agotado }); ayudaNodo = [];
      [].forEach.call(cont.querySelectorAll(".gd-op"), function (b) { b.disabled = true; if (MODO.retro === "inmediata") { var x = nodo.decisiones.filter(function (z) { return z.id === b.getAttribute("data-id"); })[0]; if (x.id === d.id) b.classList.add("is-sel", "is-" + x.calidad); else if (x.calidad === "optima") b.classList.add("is-mejor"); } else if (b.getAttribute("data-id") === d.id) b.classList.add("is-sel"); });
      var sig = caso.nodos[d.siguiente], opt = nodo.decisiones.filter(function (x) { return x.calidad === "optima"; })[0], rn = refN(caso, d.refs), h = "";
      if (agotado) h = '<div class="gd-fb gd-fb--agotado"><p class="gd-fb__t">⏱ Se agotó el tiempo</p><p>No se registró una decisión a tiempo: se aplicó la conducta de espera definida para esta etapa («' + esc(d.texto) + '»). ' + (MODO.retro === "inmediata" ? esc(d.explicacion) : "Su análisis completo aparecerá al terminar el caso.") + '</p>';
      else if (MODO.retro === "inmediata") h = '<div class="gd-fb gd-fb--' + d.calidad + '"><p class="gd-fb__t">' + N.ETQ[d.calidad] + ' · ' + (N.PUNTOS[d.calidad]) + ' pts' + (niv && N.PENAL_AYUDA[niv] ? ' (−' + N.PENAL_AYUDA[niv] + ' por la ayuda)' : "") + '</p><p>' + esc(d.explicacion) + '</p>' + (d.calidad !== "optima" ? '<p class="gd-fb__opt"><b>Lo preferible era (' + esc(opt.id) + '):</b> ' + esc(opt.texto) + '</p>' : "") + (rn.length ? '<p class="muted small">Respaldo: referencia' + (rn.length > 1 ? "s " : " ") + rn.join(", ") + ' (detalle al terminar el caso).</p>' : "");
      else h = '<div class="gd-fb gd-fb--neutra"><p class="gd-fb__t">Decisión registrada (' + esc(d.id) + ')</p><p>En la simulación cronometrada la explicación completa se muestra al terminar el caso.</p>';
      h += '<button type="button" class="btn btn--primary" id="gdSig">' + (sig.final ? "Ver el desenlace y el informe" : "Continuar: ver la evolución") + '</button></div>';
      cont.querySelector("#gdFb").innerHTML = h; var bt = cont.querySelector("#gdSig"); bt.focus(); persistirTrasDecidir(d.siguiente);
      bt.addEventListener("click", function () { nodoId = d.siguiente; nodo = sig; paso(); });
    }
    function persistirTrasDecidir(sigId) { var e = estado(); e.nodo = sigId; e.usadoMs = 0; guardarSesion(e); }

    /* ---- informe final ---- */
    function cincoAlternativas(x) {
      return '<ol class="gd-cinco" type="A">' + nodoPorId(x.nodoId).decisiones.map(function (a) {
        var tags = (a.id === x.elegida.id ? ' <span class="gd-prov">tu elección</span>' : "") + (a.calidad === "optima" ? ' <span class="gd-prov gd-prov--ok">correcta</span>' : "");
        return '<li class="gd-cinco__i gd-cinco__i--' + a.calidad + '"><p><b>' + esc(a.id) + '.</b> ' + esc(a.texto) + tags + '</p><p class="small"><b>' + N.ETQ[a.calidad] + ':</b> ' + esc(a.explicacion) + '</p></li>';
      }).join("") + '</ol>';
    }
    function nodoPorId(id) { return caso.nodos[id]; }
    function fin() {
      terminar(); var f = nodo.final, an = N.analizar(caso, camino, puntos, { modo: modo }), pct = an.pct, inf = caso.informe, IM = IMG(), fatal = f.tipo === "fatal";
      var g = N.registrar(cargar(), caso, { pct: pct, tipo: f.tipo, criticos: an.criticos.length, modo: modo }); guardar(g); borrarSesion(caso.id);
      var rel = (inf.casos_relacionados || []).map(function (id) { return (raiz.MQP_GUARDIA || []).filter(function (c) { return c.id === id; })[0]; }).filter(Boolean);
      var usadas = {}; an.refsUsadas.forEach(function (r) { usadas[r] = 1; });
      var h = '<div class="gd-juego gd-informe"><header class="gd-top"><a class="link-arrow" href="#/guardia/emergencias">← Guardia de emergencias</a><h1>' + esc(caso.titulo) + '</h1></header><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<section class="gd-final gd-final--' + f.tipo + '"><p class="gd-niv">Desenlace</p><h2>' + esc(f.titulo) + '</h2><p>' + esc(f.mensaje) + '</p><p class="gd-pts"><b>' + pct + ' %</b><span>' + puntos + ' de ' + an.max + ' puntos ponderados posibles en las decisiones que tomaste · ' + esc(N.MODOS[modo].nombre) + '</span></p></section>' +
        (fatal ? '<section class="card card--spaced gd-fatal" aria-labelledby="gdFat"><h2 class="card__h" id="gdFat">Qué contribuyó a este desenlace</h2><p class="small">Un desenlace fatal solo ocurre en este caso tras una secuencia de errores críticos definida de antemano. Estas fueron las decisiones que más contribuyeron y la conducta preferible en cada una:</p><ul>' +
          (an.criticos.length ? an.criticos.map(function (x) { return '<li><b>Decisión ' + x.n + ' (' + esc(x.elegida.id) + '):</b> ' + esc(x.elegida.texto) + '<br><b>Lo preferible (' + esc(x.optima.id) + '):</b> ' + esc(x.optima.texto) + '<br><span class="small">' + esc(x.optima.explicacion) + '</span></li>'; }).join("") : '<li>' + esc(f.mensaje) + '</li>') + '</ul></section>' : "") +
        '<nav class="gd-indice" aria-label="Secciones del informe"><a href="#gdA">A. Resumen</a> <a href="#gdB">B. Razonamiento</a>' + (caso.imagenes.length ? ' <a href="#gdC">C. Imágenes</a>' : "") + ' <a href="#gdL">Laboratorio</a> <a href="#gdD">D. Tus decisiones</a> <a href="#gdE">E. Tratamiento</a> <a href="#gdF">F. Resultado y referencias</a></nav>';
      h += '<section class="card card--spaced" id="gdA"><h2 class="card__h">A. Resumen clínico y diagnóstico</h2><p>' + esc(inf.resumen_clinico) + '</p>' +
        (inf.diagnostico_final ? '<p><b>Diagnóstico final:</b> ' + esc(inf.diagnostico_final) + '</p>' : "") +
        (inf.diagnosticos_diferenciales ? '<p><b>Diagnósticos diferenciales:</b></p><ul class="gd-alt">' + inf.diagnosticos_diferenciales.map(function (x) { return '<li><b>' + esc(x.dx) + ':</b> ' + esc(x.por_que_no) + '</li>'; }).join("") + '</ul>' : "") +
        (inf.datos_clave ? '<p><b>Datos que debían orientar el razonamiento:</b></p><ul class="gd-alt">' + inf.datos_clave.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul>' : "") + '</section>';
      h += '<section class="card card--spaced" id="gdB"><h2 class="card__h">B. Razonamiento paso a paso</h2><p class="muted small">Así se razona el caso de forma ideal:</p><ol class="gd-razon">' + inf.razonamiento.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ol>' +
        '<p class="muted small">Tu recorrido:</p><ol class="gd-trail">' + an.decisiones.map(function (x) { return '<li class="gd-t gd-t--' + x.elegida.calidad + '"><p><b>' + N.ETQ[x.elegida.calidad] + (x.agotado ? " (tiempo agotado)" : "") + ' (' + esc(x.elegida.id) + '):</b> ' + esc(x.elegida.texto) + '</p></li>'; }).join("") + '</ol></section>';
      if (caso.imagenes.length) {
        h += '<section class="card card--spaced" id="gdC"><h2 class="card__h">C. Interpretación de las imágenes</h2><p><b>Hallazgos e interpretación:</b> ' + esc(inf.imagen_interpretacion) + '</p>' +
          (inf.imagen_diferenciales ? '<p><b>Diagnósticos diferenciales de la imagen:</b></p><ul class="gd-alt">' + inf.imagen_diferenciales.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul>' : "") +
          (inf.imagen_conducta ? '<p><b>Cómo modifica la conducta:</b> ' + esc(inf.imagen_conducta) + '</p>' : "");
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
      h += '<section class="card card--spaced" id="gdL"><h2 class="card__h">Interpretación de los resultados de laboratorio</h2>' + (inf.interpretacion_laboratorio ? '<ul class="gd-alt">' + inf.interpretacion_laboratorio.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul>' : "") +
        tablaResultados(resultados.map(function (r) { return { nodoId: r.nodoId, titulo: r.titulo, ocultar: false, items: r.items }; }), caso.paciente, null) + '<p class="muted small">Los intervalos son educativos (no de un laboratorio peruano).</p></section>';
      h += '<section class="card card--spaced" id="gdD"><h2 class="card__h">D. Análisis de tus decisiones</h2>' + an.decisiones.map(function (x) {
        var rn = refN(caso, x.elegida.refs), dest = caso.nodos[x.elegida.siguiente], cons = dest && !dest.final ? dest.estado : (dest && dest.final ? dest.final.mensaje : "");
        return '<details class="gd-dec gd-dec--' + x.elegida.calidad + '"' + (x.elegida.calidad !== "optima" || x.agotado ? " open" : "") + '><summary>Decisión ' + x.n + ': ' + esc(x.severidad) + ' · peso ' + x.peso + '</summary>' +
          '<p class="gd-t__e">' + esc(x.estado.slice(0, 170)) + (x.estado.length > 170 ? "…" : "") + '</p><p><b>' + esc(x.pregunta || "") + '</b></p>' +
          '<p><b>Tu respuesta (' + esc(x.elegida.id) + '):</b> ' + esc(x.elegida.texto) + (x.agotado ? ' <span class="gd-prov">tiempo agotado</span>' : "") + '</p>' +
          (x.elegida.calidad !== "optima" ? '<p><b>Conducta preferible (' + esc(x.optima.id) + '):</b> ' + esc(x.optima.texto) + '</p>' : '<p class="small">Fue la mejor alternativa.</p>') +
          '<p class="small"><b>Análisis de las cinco alternativas:</b></p>' + cincoAlternativas(x) +
          (cons ? '<p class="small"><b>Consecuencia en el caso:</b> ' + esc(cons.slice(0, 220)) + (cons.length > 220 ? "…" : "") + '</p>' : "") +
          '<p class="muted small">Tiempo: ' + x.segundos + ' s' + (modo === "cronometrada" ? ' de ' + x.limite + ' s (' + esc(N.TIPOS[x.tipo]) + ')' : ' (sin presión de tiempo)') + (x.nivelAyuda ? ' · Ayuda de nivel ' + x.nivelAyuda + (x.penalizacion ? ' (−' + x.penalizacion + ' pts ponderados)' : " (sin penalización)") : "") + (rn.length ? ' · Respaldo: referencia' + (rn.length > 1 ? "s " : " ") + rn.join(", ") : "") + '</p></details>';
      }).join("") + '</section>';
      h += '<section class="card card--spaced" id="gdE"><h2 class="card__h">E. Tratamiento y seguimiento recomendados</h2><div class="gd-tabla">' + inf.tratamiento.map(function (t) {
        return '<div class="gd-tr"><p class="gd-tr__i"><b>' + esc(t.item) + '</b></p><p>' + esc(t.detalle) + '</p><p class="muted small"><b>Dosis / unidades:</b> ' + esc(t.dosis) + '</p></div>'; }).join("") + '</div>' +
        '<p class="muted small">No se fija una dosis universal cuando depende del peso, la función renal, la edad o el protocolo local; consulta la guía y el protocolo vigentes de tu institución.</p></section>';
      h += '<section class="card card--spaced" id="gdF"><h2 class="card__h">F. Resultado y refuerzo</h2><p><b>Puntaje ponderado:</b> ' + puntos + ' de ' + an.max + ' (' + pct + ' %)' + (an.penalizacion ? ' · sin la penalización por ayudas habría sido ' + an.pctSinAyudas + ' %' : "") + ' · <b>Errores críticos:</b> ' + an.criticos.length + ' · <b>Errores recuperables:</b> ' + an.mayores.length + '</p>' +
        '<p><b>Tiempo:</b> ' + N.formatoTiempo(an.tiempoTotal) + ' usados' + (modo === "cronometrada" ? ' de ' + N.formatoTiempo(an.limiteTotal) + ' disponibles · ' + an.agotados + ' decisión(es) con tiempo agotado' : ' (modo entrenamiento, sin límite)') + '. La velocidad es un indicador secundario.</p>' +
        '<p><b>Interconsultas y ayudas:</b> ' + (an.ayudas.length ? an.ayudas.map(function (a) { return 'decisión ' + a.n + ' (nivel ' + a.nivel + ')'; }).join(", ") + '. Pedir orientación no es un error clínico.' : modo === "cronometrada" ? "no disponibles en la simulación cronometrada." : "no usaste ayudas.") + '</p>' +
        (an.criticos.length ? '<ul class="gd-crit">' + an.criticos.map(function (x) { return '<li>Decisión ' + x.n + ': ' + esc(x.elegida.texto) + '</li>'; }).join("") + '</ul>' : '<p class="small">No cometiste errores críticos (decisiones que ponen en riesgo la vida).</p>') +
        '<h3 class="gd-h3">Competencias</h3><ul class="gd-comp">' + an.competencias.map(function (c) { return '<li><span>' + esc(c.nombre) + '</span><span class="gd-barra" aria-hidden="true"><i style="width:' + c.pct + '%"></i></span><b>' + c.pct + ' %</b></li>'; }).join("") + '</ul>' +
        '<h3 class="gd-h3">Qué reforzar</h3>' + (an.temas.length ? '<ul class="gd-temas">' + an.temas.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join("") + '</ul>' : '<p class="small">Todas tus decisiones fueron las óptimas. ¡Buen trabajo!</p>') +
        '<p class="muted small">Temas relacionados para el banco: ' + inf.temas_relacionados.map(esc).join(" · ") + '.</p><p class="gd-clave"><b>Idea clave:</b> ' + esc(inf.mensaje_clave) + '</p>' +
        (rel.length ? '<p class="small"><b>Casos relacionados:</b> ' + rel.map(function (c) { return '<a href="#/guardia/' + esc(c.id) + '">' + esc(c.titulo) + '</a>'; }).join(" · ") + '</p>' : "") +
        '<h3 class="gd-h3">Referencias del caso</h3><ul class="gd-refs">' + caso.referencias.map(function (r, i) { return refHtml(r, i + 1, usadas[r.id]); }).join("") + '</ul>' +
        '<h3 class="gd-h3">Diferencias entre fuentes y limitaciones</h3><ul>' + caso.discrepancias.map(function (x) { return '<li class="small">' + esc(x) + '</li>'; }).join("") + '</ul>' +
        '<p class="muted small">Caso redactado a partir de las fuentes citadas; no fue revisado por un especialista externo. Si ves una discrepancia con tu guía vigente, prevalece la guía.</p></section>' +
        '<div class="gd-acc"><a class="btn btn--primary" href="#/guardia/' + esc(caso.id) + '" data-reintentar>Reintentar el caso</a><a class="btn btn--ghost" href="#/guardia/emergencias">Volver a los casos</a>' +
        rel.slice(0, 1).map(function (c) { return '<a class="btn btn--ghost" href="#/guardia/' + esc(c.id) + '">Siguiente: ' + esc(c.titulo) + '</a>'; }).join("") + '</div></div>';
      cont.innerHTML = h; ligarImagenes(cont);
      var re = cont.querySelector("[data-reintentar]"); re.addEventListener("click", function (ev) { ev.preventDefault(); preludio(cont, caso); window.scrollTo(0, 0); });
      window.scrollTo(0, 0);
    }
    paso();
  }

  var dentro = false;
  window.addEventListener("hashchange", function () { if (!/^#\/guardia/.test(location.hash)) dentro = false; });
  function montar(cont, arg, datos) {
    if (!(raiz.MQP_GUARDIA && raiz.MQP_GUARDIA_LAB)) {
      cont.innerHTML = '<p class="muted" role="status">Cargando los casos…</p>';
      asegurarDatos().then(function () { if (/^#\/guardia/.test(location.hash)) montar(cont, arg, datos); }, function () { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">No se pudieron cargar los casos</p><p class="empty-state__text">Revisa tu conexión e inténtalo de nuevo.</p><a class="btn btn--primary" href="#/guardia/emergencias">Reintentar</a></div>'; });
      return;
    }
    var casos = raiz.MQP_GUARDIA || [];
    var caso = arg && arg !== "emergencias" ? casos.filter(function (c) { return c.id === arg; })[0] : null;
    var primeraEntrada = !dentro; dentro = true;
    if (!arg && M.guardiaHub) { if (detener) detener(); M.guardiaHub.montar(cont, datos, primeraEntrada); return; }
    if (arg && arg !== "emergencias" && !caso) { cont.innerHTML = '<div class="empty-state"><p class="empty-state__title">No encontramos ese caso</p><a class="btn btn--primary" href="#/guardia/emergencias">Ver los casos</a></div>'; return; }
    if (detener) detener();
    if (caso) { preludio(cont, caso); return; }
    lista(cont, datos);
    var I = M.guardiaIntro;
    var rep = document.createElement("p"); rep.className = "gd-repetir";
    rep.innerHTML = '<button type="button" class="link-arrow" id="gdVerIntro">▶ Ver la introducción</button>';
    var kp = cont.querySelector(".gd-aviso");
    if (kp && I) { kp.after(rep); rep.querySelector("button").addEventListener("click", function () { I.mostrar({}); }); }
  }
  M.guardia = { montar: montar, asegurarDatos: asegurarDatos, abrirLaboratorio: abrirLaboratorio, tablaResultados: tablaResultados, filaResultado: filaResultado, tarjetaCatalogo: tarjetaCatalogo, dialogo: dialogo, cerrarDialogo: cerrarDialogo, figura: figura, ligarImagenes: ligarImagenes, refHtml: refHtml, esc: esc, enlace: enlace, ls: ls, AVISO: AVISO, perfilTxt: perfilTxt, efectosActivos: efectosActivos, mayus1: mayus1, cargar: cargar, estadisticasAlumno: estadisticasAlumno, abrirCatalogo: abrirCatalogo, contarDecisiones: contarDecisiones };
})(typeof window !== "undefined" ? window : this);
