/* MedQuizPlus · Atlas de anatomía (Anatomy Learning), cargado dentro de la plataforma con un <iframe>.
   Dos usos: la página «Atlas de anatomía» (#/anatomia) y el botón «Ver en el atlas» de las preguntas de anatomía, que abre el
   mismo atlas en una ventana sobre la pregunta (así no se pierde el avance del simulador).
   La dirección del <iframe> la entrega Anatomy Learning: se pone abajo en CFG.url. Mientras esté vacía, el botón no aparece y la
   página dice que el atlas está en preparación. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var CFG = {
    url: "https://browser.anatomylearning.com/",   // visor web de Anatomy Learning (el que abre «Web Browser» en su portada)
    licencia: "",       // número de licencia que Anatomy Learning pide citar (si lo asignan)
    nombre: "Anatomy Learning"
  };
  var panel = null, previo = null;

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function disponible() { return /^https:\/\//i.test(CFG.url); }
  /* ¿La pregunta es de anatomía? Se mira la categoría, el tema y la especialidad. */
  function esAnatomia(q) {
    if (!q) return false;
    return /anatom/i.test([q.categoria, q.tema, q.especialidad].join(" "));
  }
  function credito() {
    return '<p class="an-credito">Atlas 3D de <b>' + esc(CFG.nombre) + '</b>' + (CFG.licencia ? " · Licencia N.º " + esc(CFG.licencia) : "") + '</p>';
  }
  function marco(clase) {
    if (!disponible()) {
      return '<div class="an-vacio" role="status"><b>El atlas de anatomía se está preparando.</b><p>Muy pronto podrás explorarlo aquí, en 3D, sin salir del simulador.</p></div>';
    }
    return '<iframe class="an-marco ' + (clase || "") + '" src="' + esc(CFG.url) + '" title="Atlas 3D de anatomía (' + esc(CFG.nombre) + ')" loading="lazy" ' +
      'allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen referrerpolicy="origin"></iframe>' + credito();
  }

  /* Página aparte dentro del simulador: #/anatomia */
  function pagina(par) {
    var pista = par && par.tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(par.tema) + '</b></p>' : "";
    return '<header class="page-head"><p class="kicker">Anatomía</p><h1 class="page-head__title">Atlas de anatomía en 3D</h1>' +
      '<p class="page-head__lead">Explora las estructuras en 3D: rota, haz zoom y consulta los nombres para repasar lo que falló.</p></header>' + pista + marco("an-marco--pagina");
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
      (tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(tema) + '</b></p>' : "") + marco("an-marco--ventana") + '</div>';
    document.body.appendChild(panel);
    panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) cerrar(); });
    panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
    if (panel.showModal) panel.showModal(); else panel.setAttribute("open", "");
    var x = panel.querySelector(".fc-x"); if (x && x.focus) x.focus();
  }

  function mostrarMenu() { var n = document.getElementById("navAna"); if (n) n.hidden = !disponible(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mostrarMenu); else mostrarMenu();

  M.anatomia = { disponible: disponible, esAnatomia: esAnatomia, abrir: abrir, cerrar: cerrar, pagina: pagina, config: CFG };
})();
