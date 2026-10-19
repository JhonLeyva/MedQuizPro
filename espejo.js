/* MedQuizPlus · Modo espejo: «MINSA Perú» vs. «Guía internacional».
   Solo aparece cuando existe una comparación validada para la pregunta (guias/comparaciones.json, verificada con tools/verificar_comparaciones.py).
   Es una capa aparte: no toca el flujograma ni la explicación originales. Un lado sin fuente muestra «Fuente no disponible». */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var BASE = M.base || "";
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  var TIPOS = { discrepancia: "Diferencia real", equivalente: "Equivalentes", poblacion: "Población distinta", actualizacion: "Actualización en el tiempo", recursos: "Condicionada por recursos" };
  var cache = {}, panel = null, previo = null;

  function consultar(q) {
    var k = q.id + "|" + (q.tema || "");
    if (!cache[k]) cache[k] = fetch(BASE + "api.php?accion=comparacion&pregunta=" + encodeURIComponent(q.id) + "&tema=" + encodeURIComponent(q.tema || q.categoria || ""), { credentials: "same-origin" })
      .then(function (r) { return r.json(); }).then(function (j) { return (j && j.comparacion) || null; }, function () { return null; });
    return cache[k];
  }
  function disponible(q) { return consultar(q).then(function (c) { return !!(c && (c.nacional || c.internacional)); }); }

  function cita(c) {
    if (!c) return '<span class="es-sin">Sin cita</span>';
    return '<span class="es-cita">' + esc(c.institucion) + ', ' + esc(c.anio) + (c.version ? ' · ' + esc(c.version) : '') + ' · <b>p. ' + esc(c.pagina) + '</b>' + (c.estado !== "vigente" ? ' · <em>' + esc(c.aviso || c.estado) + '</em>' : "") + '</span>';
  }
  function tarjeta(lado, titulo) {
    if (!lado) return '<div class="es-nd" role="status"><b>Fuente no disponible</b><p>Todavía no hay una ' + (titulo === "MINSA Perú" ? "norma peruana" : "guía internacional") + ' cargada y verificada para este tema.</p></div>';
    var c = lado.cita;
    return '<div class="es-fuente"><p class="es-fuente__t">' + esc(c.titulo) + '</p><p class="es-fuente__m">' + esc(c.institucion) + ' · ' + esc(c.pais) + ' · ' + esc(c.anio) + (c.version ? ' · ' + esc(c.version) : '') + ' · estado: <b>' + esc(c.estado) + '</b></p>' +
      (c.aviso ? '<p class="es-aviso">⚠ ' + esc(c.aviso) + '</p>' : "") + (lado.resumen ? '<p>' + esc(lado.resumen) + '</p>' : "") + (c.url ? '<p><a href="' + esc(c.url) + '" target="_blank" rel="noopener noreferrer">Abrir el documento</a></p>' : "") + '</div>';
  }
  function criterios(filas, k, titulo) {
    var f = filas.filter(function (x) { return x[k]; });
    if (!f.length) return '<p class="muted">No hay criterios cargados para este lado.</p>';
    return '<ul class="es-crit">' + f.map(function (x) { return '<li><b>' + esc(x.criterio) + '</b><p>' + esc(x[k].texto) + '</p>' + cita(x[k].cita) + '</li>'; }).join("") + '</ul>';
  }
  function celda(c) { return c ? '<p>' + esc(c.texto) + '</p>' + cita(c.cita) : '<span class="es-sin">Fuente no disponible</span>'; }
  function comparar(c) {
    if (!c.filas.length) return '<p class="muted">Esta comparación aún no tiene criterios cargados.</p>';
    return '<div class="es-tabla-w"><table class="es-tabla"><caption class="sr-only">Comparación de recomendaciones</caption><thead><tr><th scope="col">Criterio</th><th scope="col">MINSA Perú</th><th scope="col">Guía internacional</th><th scope="col">Tipo</th></tr></thead><tbody>' +
      c.filas.map(function (x) { return '<tr class="es-f es-f--' + x.tipo + '"><th scope="row">' + esc(x.criterio) + '</th><td>' + celda(x.nacional) + '</td><td>' + celda(x.internacional) + '</td><td><span class="es-tipo es-tipo--' + x.tipo + '">' + esc(TIPOS[x.tipo]) + '</span>' + (x.nota ? '<p class="es-nota">' + esc(x.nota) + '</p>' : "") + '</td></tr>'; }).join("") +
      '</tbody></table></div><p class="es-leyenda">Solo se marca «Diferencia real» cuando ambas fuentes dicen algo distinto para la misma población y momento. Una diferencia por población, fecha o recursos locales se etiqueta aparte. Ninguna de las dos guías es «mejor» por defecto.</p>';
  }

  function cerrar() { if (!panel) return; if (panel.close) panel.close(); panel.remove(); panel = null; if (previo && previo.focus) previo.focus(); }
  function abrir(q, origen) {
    previo = origen || document.activeElement; cerrar(); previo = origen || previo;
    consultar(q).then(function (c) {
      if (!c) return;
      panel = document.createElement("dialog"); panel.className = "fc-dlg es-dlg"; panel.setAttribute("aria-labelledby", "esT");
      var ambos = !!(c.nacional && c.internacional), vistas = [["nac", "MINSA Perú"], ["int", "Guía internacional"]]; if (ambos || c.filas.length) vistas.push(["cmp", "Comparar"]);
      var activa = ambos ? "cmp" : (c.nacional ? "nac" : "int");
      panel.innerHTML = '<div class="fc-form"><header class="fc-head"><h2 id="esT">Modo espejo · ' + esc(c.titulo) + '</h2><button type="button" class="fc-x" aria-label="Cerrar" data-x>✕</button></header>' +
        '<div class="es-tabs" role="tablist" aria-label="Fuente">' + vistas.map(function (v) { return '<button type="button" role="tab" class="es-tab" id="esTab-' + v[0] + '" aria-controls="esP-' + v[0] + '" data-v="' + v[0] + '">' + v[1] + '</button>'; }).join("") + '</div>' +
        '<div class="es-cuerpo">' +
          '<section role="tabpanel" id="esP-nac" aria-labelledby="esTab-nac" hidden>' + tarjeta(c.nacional, "MINSA Perú") + (c.nacional ? criterios(c.filas, "nacional") : "") + '</section>' +
          '<section role="tabpanel" id="esP-int" aria-labelledby="esTab-int" hidden>' + tarjeta(c.internacional, "Guía internacional") + (c.internacional ? criterios(c.filas, "internacional") : "") + '</section>' +
          '<section role="tabpanel" id="esP-cmp" aria-labelledby="esTab-cmp" hidden>' + comparar(c) + '</section></div>' +
        '<p class="es-pie">Capa de estudio aparte: no modifica el flujograma ni la explicación del banco. No sustituye el juicio clínico ni los protocolos de tu institución.</p></div>';
      document.body.appendChild(panel);
      function ir(v) {
        [].forEach.call(panel.querySelectorAll(".es-tab"), function (b) { var on = b.getAttribute("data-v") === v; b.setAttribute("aria-selected", on ? "true" : "false"); b.tabIndex = on ? 0 : -1; });
        [].forEach.call(panel.querySelectorAll("[role=tabpanel]"), function (p) { p.hidden = p.id !== "esP-" + v; });
      }
      panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) { cerrar(); return; } var b = ev.target.closest && ev.target.closest(".es-tab"); if (b) ir(b.getAttribute("data-v")); });
      panel.addEventListener("keydown", function (ev) {
        var tabs = [].slice.call(panel.querySelectorAll(".es-tab")), i = tabs.indexOf(document.activeElement);
        if (i >= 0 && (ev.key === "ArrowRight" || ev.key === "ArrowLeft")) { ev.preventDefault(); var n = tabs[(i + (ev.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length]; n.focus(); ir(n.getAttribute("data-v")); }
      });
      panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
      ir(activa); panel.showModal(); panel.querySelector("#esTab-" + activa).focus();
    });
  }
  M.espejo = { disponible: disponible, abrir: abrir, cerrar: cerrar };
})();
