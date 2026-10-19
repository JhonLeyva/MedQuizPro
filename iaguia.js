/* MedQuizPlus · «Preguntar a la IA» sobre la pregunta que acabas de responder.
   El navegador solo habla con api.php (que guarda la llave). Se envía el contexto de la pregunta; el servidor lo trata como datos.
   Hoy la única fuente que recibe la IA es el comentario docente de tu banco: aún no hay guías (MINSA / internacionales) cargadas,
   y el panel lo dice. Las respuestas no se guardan en el servidor. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var BASE = M.base || "";
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  var panel = null, previo = null, historial = [], ocupado = false;

  function cerrar() { if (!panel) return; if (panel.close) panel.close(); panel.remove(); panel = null; historial = []; ocupado = false; if (previo && previo.focus) previo.focus(); }

  function contexto(q, letra) {
    var ops = {}; (q.opciones || []).forEach(function (o) { ops[o.letra] = o.texto; });
    return { id: q.id, especialidad: q.especialidad || "", tema: q.tema || q.categoria || "", enunciado: q.enunciado, opciones: ops, elegida: letra || "", correcta: q.clave, comentario: q.comentario || "" };
  }
  function burbuja(lista, clase, html) { var d = document.createElement("div"); d.className = "ia-b ia-b--" + clase; d.innerHTML = html; lista.appendChild(d); lista.scrollTop = lista.scrollHeight; return d; }

  function abrir(q, letra, disparador) {
    if (!q || !q.id) return;
    previo = disparador || document.activeElement; cerrar(); previo = disparador || previo;
    var ctx = contexto(q, letra);
    panel = document.createElement("dialog"); panel.className = "fc-dlg ia-dlg"; panel.setAttribute("aria-labelledby", "iaT");
    panel.innerHTML = '<div class="fc-form"><header class="fc-head"><h2 id="iaT">Preguntar a la IA</h2><button type="button" class="fc-x" aria-label="Cerrar" data-x>✕</button></header>' +
      '<p class="ia-base">Respondo sobre <b>' + esc(q.id) + '</b> usando el <b>comentario docente de tu banco</b>. Aún no hay guías MINSA ni internacionales cargadas: lo que añada fuera de ese comentario es conocimiento general, <b>no verificado</b> en una guía. Ayuda para estudiar; no sustituye el juicio clínico ni los protocolos institucionales.</p>' +
      '<div class="ia-chat" id="iaChat" role="log" aria-live="polite" aria-label="Conversación"></div>' +
      '<div class="ia-sug" id="iaSug">' + ["¿Por qué esa es la correcta?", letra && letra !== q.clave ? "¿Por qué mi respuesta (" + letra + ") no es la mejor?" : "Explícame los distractores", "Dame un resumen para memorizar"].map(function (t) { return '<button type="button" class="chip" data-s="' + esc(t) + '">' + esc(t) + '</button>'; }).join("") + '</div>' +
      '<form class="ia-form" id="iaForm"><label class="sr-only" for="iaIn">Tu pregunta</label><textarea id="iaIn" rows="2" maxlength="600" placeholder="Escribe tu duda sobre esta pregunta…"></textarea><button type="submit" class="btn btn--primary" id="iaEnviar">Enviar</button></form></div>';
    document.body.appendChild(panel);
    var chat = panel.querySelector("#iaChat"), inp = panel.querySelector("#iaIn"), btn = panel.querySelector("#iaEnviar");
    panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) cerrar(); });
    panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });

    function preguntar(texto) {
      texto = String(texto || "").trim(); if (!texto || ocupado) return;
      ocupado = true; btn.disabled = true; panel.querySelector("#iaSug").hidden = true; inp.value = "";
      burbuja(chat, "yo", esc(texto)); var esp = burbuja(chat, "ia", '<i class="ia-esp">Pensando…</i>');
      fetch(BASE + "api.php", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify({ mensaje: texto, historial: historial.slice(-12), contexto: ctx }) })
        .then(function (r) { return r.text().then(function (c) { var j = null; try { j = JSON.parse(c); } catch (e) {} return { http: r.status, j: j || {} }; }); })
        .then(function (r) {
          var t = r.j.respuesta;
          if (r.http === 200 && typeof t === "string" && t.trim()) {
            historial.push({ rol: "usuario", texto: texto }, { rol: "tutor", texto: t });
            var f = (r.j.fuentes || []).map(function (s) { return esc(s.titulo) + " (" + esc(s.pregunta) + ")"; }).join(" · ");
            esp.innerHTML = '<p>' + esc(t).replace(/\n{2,}/g, "</p><p>").replace(/\n/g, "<br>") + '</p><p class="ia-src">Fuente entregada a la IA: ' + (f || "ninguna") + '. ' + (r.j.verificado === false ? "Lo que añada fuera de esa fuente no está verificado en una guía." : "") + '</p>';
          } else if (r.http === 401) esp.innerHTML = 'Para preguntarle a la IA necesitas una cuenta. <a href="#/registro">Crear cuenta</a> · <a href="#/ingresar">Ingresar</a>';
          else if (r.http === 503 || r.http === 502 || !r.j.error) esp.innerHTML = '<span class="ia-err">El tutor de IA no está disponible en este momento. Tu práctica y tus flashcards siguen funcionando; vuelve a intentarlo más tarde.</span>';
          else esp.innerHTML = '<span class="ia-err">' + esc(r.j.error) + '</span>';
        }, function () { esp.innerHTML = '<span class="ia-err">No hay conexión con el servidor. Inténtalo de nuevo.</span>'; })
        .then(function () { ocupado = false; btn.disabled = false; inp.focus(); chat.scrollTop = chat.scrollHeight; });
    }
    panel.querySelector("#iaForm").addEventListener("submit", function (ev) { ev.preventDefault(); preguntar(inp.value); });
    inp.addEventListener("keydown", function (ev) { if (ev.key === "Enter" && !ev.shiftKey) { ev.preventDefault(); preguntar(inp.value); } });
    panel.querySelector("#iaSug").addEventListener("click", function (ev) { var b = ev.target.closest && ev.target.closest("[data-s]"); if (b) preguntar(b.getAttribute("data-s")); });
    panel.showModal(); inp.focus();
  }
  M.iaguia = { abrir: abrir, cerrar: cerrar };
})();
