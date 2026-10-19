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
  var estadoGuias = null;       // { documentos, fragmentos, lista } de api.php?accion=guias_estado
  function cargarEstadoGuias() {
    if (estadoGuias) return Promise.resolve(estadoGuias);
    return fetch(BASE + "api.php?accion=guias_estado", { credentials: "same-origin", cache: "no-store" }).then(function (r) { return r.json(); })
      .then(function (j) { estadoGuias = j || { documentos: 0 }; M.iaguia.conGuias = (estadoGuias.documentos || 0) > 0; return estadoGuias; }, function () { estadoGuias = { documentos: 0 }; return estadoGuias; });
  }
  function fichaGuia(g, citada) {
    var e = g.estado !== "vigente";
    return '<li class="ia-g' + (citada ? " is-cit" : "") + (e ? " is-vieja" : "") + '" id="iaG' + g.n + '"><p class="ia-g__t"><b>[' + g.n + ']</b> ' + esc(g.titulo) + '</p>' +
      '<p class="ia-g__m">' + esc(g.institucion) + ' · ' + esc(g.pais) + ' (' + (g.tipo === "nacional" ? "norma nacional" : "guía internacional") + ') · ' + esc(g.anio) + (g.version ? " · " + esc(g.version) : "") + ' · <b>p. ' + esc(g.pagina) + '</b></p>' +
      (g.aviso ? '<p class="ia-g__a">⚠ ' + esc(g.aviso) + '</p>' : "") + '<blockquote class="ia-g__x">' + esc(g.extracto) + (g.extracto.length >= 420 ? "…" : "") + '</blockquote>' +
      (g.url ? '<p class="ia-g__l"><a href="' + esc(g.url) + '" target="_blank" rel="noopener noreferrer">Abrir el documento</a></p>' : "") + '</li>';
  }

  /* Formato de las respuestas: **negrita**, listas con - o 1., títulos con # y párrafos. Recibe texto YA escapado: solo añade etiquetas conocidas. */
  function md(t) {
    var out = [], lista = null, parr = [];
    function cerrarP() { if (parr.length) { out.push("<p>" + parr.join("<br>") + "</p>"); parr = []; } }
    function cerrarL() { if (lista) { out.push("</" + lista + ">"); lista = null; } }
    function en(x) { return x.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>").replace(/(^|[\s(])\*(?!\s)([^*\n]+?)\*(?=[\s).,;:!?]|$)/g, "$1<em>$2</em>"); }
    String(t).split("\n").forEach(function (l) {
      var m;
      if (/^\s*$/.test(l)) { cerrarP(); cerrarL(); return; }
      if ((m = l.match(/^\s*#{1,6}\s+(.*)$/))) { cerrarP(); cerrarL(); out.push("<p><strong>" + en(m[1]) + "</strong></p>"); return; }
      if ((m = l.match(/^\s*[-*•]\s+(.*)$/))) { cerrarP(); if (lista !== "ul") { cerrarL(); out.push("<ul>"); lista = "ul"; } out.push("<li>" + en(m[1]) + "</li>"); return; }
      if ((m = l.match(/^\s*\d+[.)]\s+(.*)$/))) { cerrarP(); if (lista !== "ol") { cerrarL(); out.push("<ol>"); lista = "ol"; } out.push("<li>" + en(m[1]) + "</li>"); return; }
      cerrarL(); parr.push(en(l));
    });
    cerrarP(); cerrarL();
    return out.join("");
  }

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
      '<div class="ia-chat" id="iaChat" role="log" aria-live="polite" aria-label="Conversación"></div>' +
      '<div class="ia-sug" id="iaSug">' + ["¿Por qué esa es la correcta?", letra && letra !== q.clave ? "¿Por qué mi respuesta (" + letra + ") no es la mejor?" : "Explícame los distractores", "Dame un resumen para memorizar"].map(function (t) { return '<button type="button" class="chip" data-s="' + esc(t) + '">' + esc(t) + '</button>'; }).join("") + '</div>' +
      '<form class="ia-form" id="iaForm"><label class="sr-only" for="iaIn">Tu pregunta</label><textarea id="iaIn" rows="2" maxlength="600" placeholder="Escribe tu duda sobre esta pregunta…"></textarea><button type="submit" class="btn btn--primary" id="iaEnviar">Enviar</button></form></div>';
    document.body.appendChild(panel);
    cargarEstadoGuias().then(function (g) {
      var t = panel && panel.querySelector("#iaT");
      if (g.documentos > 0 && t) t.textContent = "Preguntar a la IA de la Guía";
    });
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
            var cit = r.j.citadas || [], gs = r.j.guias || [];
            var cuerpo = esc(t).replace(/\[G(\d{1,2})\]/g, function (_, n) { return '<sup class="ia-c"><a href="#iaG' + n + '">[' + n + ']</a></sup>'; });
            esp.innerHTML = md(cuerpo) +
              (gs.length ? '<details class="ia-gs"' + (cit.length ? " open" : "") + '><summary>Guías consultadas (' + gs.length + ')' + (cit.length ? ", citadas: " + cit.length : ", ninguna citada") + '</summary><ul>' + gs.map(function (g) { return fichaGuia(g, cit.indexOf(g.n) >= 0); }).join("") + '</ul></details>' : "");
          } else if (r.http === 401) esp.innerHTML = 'Para preguntarle a la IA necesitas una cuenta. <a href="#/registro">Crear cuenta</a> · <a href="#/ingresar">Ingresar</a>';
          else if (r.http === 402) esp.innerHTML = 'El tutor de IA es parte de los planes de pago. <a href="#/planes">Ver planes</a>';
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
  M.iaguia = { abrir: abrir, cerrar: cerrar, conGuias: false };
  cargarEstadoGuias();   // para que el botón diga «de la Guía» solo cuando de verdad hay guías
})();
