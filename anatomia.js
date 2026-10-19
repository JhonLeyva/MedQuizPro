/* MedQuizPlus · Atlas de anatomía 3D (visor abierto del Departamento de Anatomía y Embriología del LUMC, Leiden),
   alojado en esta misma plataforma (carpeta visor3d/): sin cuentas, sin pagos y para todos los estudiantes.
   Dos usos: la página «Atlas de anatomía» (#/anatomia) y el botón «Ver en el atlas» de las preguntas de anatomía, que abre el
   mismo atlas en una ventana sobre la pregunta (así no se pierde el avance del simulador).
   Para agregar un modelo: copiar su .glb a visor3d/3dmodels/<id>/<id>.glb y sumarlo a MODELOS. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var CFG = {
    base: "../visor3d/",   // carpeta del visor, relativa a app/index.html
    nombre: "Open 3D Model · LUMC",
    externo: "https://browser.anatomylearning.com/"   // atlas externo (versión gratuita limitada), opcional
  };
  /* id = carpeta en visor3d/3dmodels; clave = palabras que lo relacionan con el tema de una pregunta */
  var MODELOS = [
    { id: "overview-skeleton", nombre: "Esqueleto completo", clave: /esquelet|hueso|oste|articul|pelvis|tor[aá]x|costill|ester/i },
    { id: "overview-colored-skull", nombre: "Cráneo (vista general)", clave: /cr[aá]ne|skull|facial|mand[ií]b|maxil|neurocr/i },
    { id: "colored-skull-base", nombre: "Base del cráneo", clave: /base del cr[aá]neo|agujero|forame|silla turca|esfenoid|temporal/i },
    { id: "exploded-view-skull", nombre: "Cráneo desarmado (vista explosionada)", clave: /suturas|huesos del cr[aá]neo/i },
    { id: "vertebrae", nombre: "Vértebras", clave: /v[eé]rtebr|columna|espinal|raqu|lumbar|cervical|dorsal|sacro|cox[ií]/i },
    { id: "upper-limb", nombre: "Miembro superior", clave: /miembro superior|brazo|antebrazo|h[uú]mero|codo|hombro|manguito|plexo braquial|axila|radio|cubital/i },
    { id: "hand", nombre: "Mano y muñeca", clave: /mano|mu[nñ]eca|carpo|escafoid|dedo|t[uú]nel|metacarp/i },
    { id: "lower-limb", nombre: "Miembro inferior", clave: /miembro inferior|muslo|f[eé]mur|rodilla|tibia|peron|tobillo|pie|cadera|menisco|cruzado|ciático|ci[aá]tico/i }
  ];
  var panel = null, previo = null;

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function disponible() { return MODELOS.length > 0; }
  /* ¿La pregunta es de anatomía? Se mira la categoría, el tema y la especialidad. */
  function esAnatomia(q) {
    if (!q) return false;
    return /anatom/i.test([q.categoria, q.tema, q.especialidad].join(" "));
  }
  function modeloPara(tema) {
    var t = String(tema || "");
    for (var i = 0; i < MODELOS.length; i++) if (MODELOS[i].clave.test(t)) return MODELOS[i].id;
    return MODELOS[0].id;
  }
  function credito() {
    return '<p class="an-credito">Modelo y visor 3D abiertos del Dept. de Anatomía y Embriología del <b>LUMC</b> (Leiden) y universidades de Países Bajos y Bélgica · ' +
      '<a href="https://anatomytool.org/open3dmodel" target="_blank" rel="noopener noreferrer">Open 3D Model</a> · licencia ' +
      '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a> (visor: GPL 3.0). ' +
      'Material educativo; no sustituye el diagnóstico médico.' +
      (CFG.externo ? ' · <a href="' + esc(CFG.externo) + '" target="_blank" rel="noopener noreferrer">Otro atlas (Anatomy Learning)</a>' : "") + '</p>';
  }
  function selector(actual) {
    return '<label class="an-sel">Región: <select data-an-modelo>' + MODELOS.map(function (m) {
      return '<option value="' + esc(m.id) + '"' + (m.id === actual ? " selected" : "") + ">" + esc(m.nombre) + "</option>";
    }).join("") + "</select></label>";
  }
  function src(id) { return CFG.base + "?model=" + encodeURIComponent(id); }
  function marco(clase, id) {
    return selector(id) + '<iframe class="an-marco ' + (clase || "") + '" src="' + esc(src(id)) + '" title="Atlas 3D de anatomía (' + esc(CFG.nombre) + ')" loading="lazy" ' +
      'allow="fullscreen" allowfullscreen></iframe>' + credito();
  }
  /* Cambiar de región sin recargar la página del simulador. */
  function enlazar(raiz) {
    var sel = raiz.querySelector("[data-an-modelo]"), fr = raiz.querySelector("iframe.an-marco");
    if (sel && fr) sel.addEventListener("change", function () { fr.src = src(sel.value); });
  }

  /* Página aparte dentro del simulador: #/anatomia */
  function pagina(par) {
    var id = modeloPara(par && par.tema);
    var pista = par && par.tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(par.tema) + '</b></p>' : "";
    setTimeout(function () { var r = document.querySelector(".an-marco--pagina"); if (r) enlazar(r.parentNode); }, 0);
    return '<header class="page-head"><p class="kicker">Anatomía</p><h1 class="page-head__title">Atlas de anatomía en 3D</h1>' +
      '<p class="page-head__lead">Explora las estructuras en 3D: arrastra para rotar, usa la rueda o pellizca para acercar, toca una estructura para ver su nombre y oculta capas con el menú superior.</p></header>' + pista +
      '<div class="an-pagina">' + marco("an-marco--pagina", id) + '</div>';
  }

  function cerrar() { if (!panel) return; if (panel.close) panel.close(); panel.remove(); panel = null; if (previo && previo.focus) previo.focus(); }

  /* Ventana sobre la pregunta: el atlas aparece grande y, al cerrarla, sigues donde estabas. */
  function abrir(q, disparador) {
    if (!disponible()) return;
    previo = disparador || document.activeElement; cerrar(); previo = disparador || previo;
    var tema = q && (q.tema || q.categoria) ? String(q.tema || q.categoria) : "";
    panel = document.createElement("dialog"); panel.className = "fc-dlg an-dlg"; panel.setAttribute("aria-labelledby", "anT");
    panel.innerHTML = '<div class="fc-form an-form"><header class="fc-head"><h2 id="anT">Atlas de anatomía</h2>' +
      '<a class="btn btn--ghost btn--sm" href="#/anatomia' + (tema ? "?tema=" + encodeURIComponent(tema) : "") + '" data-x>Abrir en pantalla completa</a>' +
      '<button type="button" class="fc-x" aria-label="Cerrar" data-x>✕</button></header>' +
      (tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(tema) + '</b></p>' : "") + marco("an-marco--ventana", modeloPara(tema)) + '</div>';
    document.body.appendChild(panel); enlazar(panel);
    panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) cerrar(); });
    panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
    if (panel.showModal) panel.showModal(); else panel.setAttribute("open", "");
    var x = panel.querySelector(".fc-x"); if (x && x.focus) x.focus();
  }

  function mostrarMenu() { var n = document.getElementById("navAna"); if (n) n.hidden = !disponible(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mostrarMenu); else mostrarMenu();

  M.anatomia = { disponible: disponible, esAnatomia: esAnatomia, abrir: abrir, cerrar: cerrar, pagina: pagina, config: CFG, modelos: MODELOS };
})();
