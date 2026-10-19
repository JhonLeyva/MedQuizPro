/* MedQuizPlus · Flashcards (convertir en flashcard, mis flashcards y repaso espaciado)
   Todo se guarda en la cuenta del estudiante (cuenta.php → fc_*). El calendario de repasos lo calcula el servidor.
   Las tarjetas que propone "Convertir en flashcard" se arman SOLO con el contenido que ya tiene la pregunta
   (enunciado, respuesta correcta y comentario docente); aquí no se genera ni se inventa contenido médico. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var BASE = M.base || "";

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function recorte(t, n) { t = String(t || "").replace(/\s+/g, " ").trim(); return t.length > n ? t.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : t; }

  function api(accion, datos) {
    var opt = { method: datos ? "POST" : "GET", credentials: "same-origin", cache: "no-store" };
    if (datos) { opt.headers = { "Content-Type": "application/json", "X-MQP": "1" }; opt.body = JSON.stringify(datos); }
    return fetch(BASE + "cuenta.php?a=" + accion, opt).then(function (r) {
      return r.json().then(function (j) { return { http: r.status, ok: r.ok && j && j.ok !== false, j: j || {} }; }, function () { return { http: r.status, ok: false, j: {} }; });
    }, function () { return { http: 0, ok: false, j: { error: "No hay conexión con el servidor. Inténtalo de nuevo." } }; });
  }

  /* ---------- propuesta de tarjetas a partir de una pregunta ---------- */
  function textoOpcion(q, letra) {
    var o = (q.opciones || []).filter(function (x) { return x.letra === letra; })[0];
    return o ? o.texto : "";
  }
  function proponer(q, letra) {
    if (!q || !q.id || !q.enunciado) return [];
    var correcta = textoOpcion(q, q.clave);
    if (!correcta) return [];
    var por = q.comentario ? String(q.comentario).trim() : "";
    var dorso = correcta + (por ? "\n\nPor qué: " + recorte(por, 900) : "");
    var base = { pregunta: q.id, tema: q.tema || q.categoria || "", especialidad: q.especialidad || "", fuente: "Banco MedQuizPlus · " + q.id + " · comentario docente" };
    var lista = [Object.assign({ frente: recorte(q.enunciado, 560), dorso: dorso, titulo: "Caso → conducta o diagnóstico correcto" }, base)];
    if (letra && letra !== q.clave) {
      var mala = textoOpcion(q, letra);
      if (mala) lista.push(Object.assign({
        frente: "En este caso: ¿por qué «" + recorte(mala, 120) + "» no es la mejor opción?\n\n" + recorte(q.enunciado, 420),
        dorso: "La respuesta correcta es: " + correcta + (por ? "\n\n" + recorte(por, 900) : ""), titulo: "Mi error frecuente"
      }, base));
    }
    return lista;
  }

  /* ---------- panel para revisar y guardar ---------- */
  var panel = null, previo = null;
  function cerrarPanel() { if (!panel) return; if (panel.close) panel.close(); else panel.removeAttribute("open"); panel.remove(); panel = null; if (previo && previo.focus) previo.focus(); }
  function abrirPropuesta(q, letra, disparador) {
    previo = disparador || document.activeElement;
    cerrarPanel();
    var tarjetas = proponer(q, letra);
    panel = document.createElement("dialog");
    panel.className = "fc-dlg"; panel.setAttribute("aria-labelledby", "fcDlgT");
    var cuerpo;
    if (!tarjetas.length) cuerpo = '<p class="fc-aviso">No pudimos armar tarjetas con esta pregunta (le falta la respuesta o el enunciado).</p>';
    function propHTML(t, i) {
      return '<fieldset class="fc-prop"><legend><label><input type="checkbox" checked data-i="' + i + '"> ' + esc(t.titulo) + '</label></legend>' +
        '<label class="fc-lbl" for="fcF' + i + '">Frente</label><textarea id="fcF' + i + '" rows="4" maxlength="600">' + esc(t.frente) + '</textarea>' +
        '<label class="fc-lbl" for="fcD' + i + '">Dorso</label><textarea id="fcD' + i + '" rows="5" maxlength="1500">' + esc(t.dorso) + '</textarea>' +
        '<p class="fc-fuente">Fuente: ' + esc(t.fuente) + '</p></fieldset>';
    }
    if (!tarjetas.length) cuerpo = '<p class="fc-aviso">No pudimos armar tarjetas con esta pregunta (le falta la respuesta o el enunciado).</p>';
    else cuerpo = '<p class="fc-ayuda">Revisa y edita lo que quieras. Solo se guardan las tarjetas marcadas. Las del banco se arman con tu pregunta y su comentario docente.</p><div class="fc-props" id="fcProps">' +
      tarjetas.map(propHTML).join("") + '</div><p class="fc-ia"><button type="button" class="btn btn--ghost btn--sm" id="fcIA">Proponer más con IA</button> <span class="muted small">La IA usa solo el comentario del banco y las guías cargadas, con cita. Revisa siempre los datos antes de guardar.</span></p>';
    panel.innerHTML = '<form method="dialog" class="fc-form"><header class="fc-head"><h2 id="fcDlgT">Convertir en flashcard</h2><button type="button" class="fc-x" aria-label="Cerrar" data-x>✕</button></header>' +
      cuerpo + '<p class="fc-msg" id="fcMsg" role="status" aria-live="polite"></p>' +
      '<footer class="fc-foot"><button type="button" class="btn btn--ghost" data-x>Descartar</button>' + (tarjetas.length ? '<button type="submit" class="btn btn--primary" id="fcGuardar">Guardar tarjetas</button>' : "") + '</footer></form>';
    document.body.appendChild(panel);
    panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) cerrarPanel(); });
    panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrarPanel(); });
    var msg = panel.querySelector("#fcMsg"), btn = panel.querySelector("#fcGuardar");
    if (btn) panel.querySelector("form").addEventListener("submit", function (ev) {
      ev.preventDefault();
      var env = [];
      [].forEach.call(panel.querySelectorAll("input[data-i]"), function (c) {
        if (!c.checked) return;
        var i = +c.getAttribute("data-i"), t = tarjetas[i];
        env.push({ frente: panel.querySelector("#fcF" + i).value, dorso: panel.querySelector("#fcD" + i).value, pregunta: t.pregunta, tema: t.tema, especialidad: t.especialidad, fuente: t.fuente });
      });
      if (!env.length) { msg.textContent = "Marca al menos una tarjeta o pulsa Descartar."; msg.className = "fc-msg is-err"; return; }
      btn.disabled = true; btn.textContent = "Guardando…"; msg.textContent = ""; msg.className = "fc-msg";
      api("fc_crear", { tarjetas: env }).then(function (r) {
        if (r.http === 401) { msg.innerHTML = 'Para guardar tus flashcards necesitas una cuenta. <a href="#/registro">Crear cuenta</a> · <a href="#/ingresar">Ingresar</a>'; msg.className = "fc-msg is-err"; btn.disabled = false; btn.textContent = "Guardar tarjetas"; return; }
        if (!r.ok) { msg.textContent = r.j.error || "No se pudieron guardar."; msg.className = "fc-msg is-err"; btn.disabled = false; btn.textContent = "Guardar tarjetas"; return; }
        var n = r.j.creadas, rep = r.j.repetidas;
        msg.innerHTML = (n ? "Guardaste " + n + (n === 1 ? " tarjeta" : " tarjetas") + ". " : "") + (rep ? (rep === 1 ? "Una ya existía y no se duplicó. " : rep + " ya existían y no se duplicaron. ") : "") + '<a href="#/flashcards" data-x>Ir a Mis Flashcards</a>';
        msg.className = "fc-msg is-ok"; btn.hidden = true;
        window.dispatchEvent(new CustomEvent("mqp:flashcards"));
      });
    });
    var bIA = panel.querySelector("#fcIA");
    if (bIA) bIA.addEventListener("click", function () {
      bIA.disabled = true; bIA.textContent = "Pidiendo propuestas…"; msg.textContent = ""; msg.className = "fc-msg";
      var ops = {}; (q.opciones || []).forEach(function (o) { ops[o.letra] = o.texto; });
      fetch(BASE + "api.php", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ modo: "flashcards", contexto: { id: q.id, especialidad: q.especialidad || "", tema: q.tema || q.categoria || "", enunciado: q.enunciado, opciones: ops, elegida: letra || "", correcta: q.clave, comentario: q.comentario || "" } }) })
        .then(function (r) { return r.json().then(function (j) { return { http: r.status, j: j || {} }; }, function () { return { http: r.status, j: {} }; }); })
        .then(function (r) {
          if (r.http === 401) { msg.innerHTML = 'Para usar la IA necesitas una cuenta. <a href="#/registro">Crear cuenta</a> · <a href="#/ingresar">Ingresar</a>'; msg.className = "fc-msg is-err"; }
          else if (r.http === 200 && r.j.tarjetas && r.j.tarjetas.length) {
            var cont = panel.querySelector("#fcProps");
            r.j.tarjetas.forEach(function (t) {
              var i = tarjetas.length; tarjetas.push({ titulo: "Propuesta de la IA (revisa los datos)", frente: t.frente, dorso: t.dorso, pregunta: q.id, tema: q.tema || q.categoria || "", especialidad: q.especialidad || "", fuente: t.fuente });
              cont.insertAdjacentHTML("beforeend", propHTML(tarjetas[i], i));
            });
            msg.textContent = "La IA propuso " + r.j.tarjetas.length + (r.j.tarjetas.length === 1 ? " tarjeta" : " tarjetas") + ". Revísalas: pueden contener errores."; msg.className = "fc-msg is-ok";
          } else { msg.textContent = r.http === 503 || r.http === 502 || !r.j.error ? "La IA no está disponible ahora. Puedes guardar las tarjetas del banco." : r.j.error; msg.className = "fc-msg is-err"; }
        }, function () { msg.textContent = "No hay conexión con el servidor."; msg.className = "fc-msg is-err"; })
        .then(function () { bIA.disabled = false; bIA.textContent = "Proponer más con IA"; });
    });
    if (panel.showModal) panel.showModal(); else panel.setAttribute("open", "");
    var primero = panel.querySelector("textarea, button"); if (primero) primero.focus();
  }

  /* ---------- vista "Mis Flashcards" ---------- */
  var ETQ = { nuevo: "Nueva", aprendiendo: "Aprendiendo", repaso: "En repaso", reaprendiendo: "Reaprendiendo" };
  function fechaCorta(t) { try { return new Intl.DateTimeFormat("es-PE", { day: "numeric", month: "short" }).format(new Date(t * 1000)); } catch (e) { return ""; } }
  function cuando(t, ahora) {
    var d = t - ahora; if (d <= 0) return "Pendiente hoy";
    if (d < 3600) return "En " + Math.max(1, Math.round(d / 60)) + " min";
    if (d < 72000) return "Hoy más tarde";
    return "Próximo repaso: " + fechaCorta(t);
  }

  function montar(raiz) {
    raiz.innerHTML = '<div class="app-loading" role="status"><span>Cargando tus flashcards…</span></div>';
    api("fc_listar").then(function (r) {
      if (r.http === 401) {
        raiz.innerHTML = '<div class="empty-state"><p class="empty-state__title">Entra para ver tus flashcards</p><p class="empty-state__text">Tus tarjetas se guardan en tu cuenta para que las repases desde cualquier dispositivo.</p><a class="btn btn--primary" href="#/ingresar">Ingresar</a> <a class="btn btn--ghost" href="#/registro">Crear cuenta</a></div>';
        return;
      }
      if (!r.ok) { raiz.innerHTML = '<div class="empty-state"><p class="empty-state__title">No pudimos cargar tus flashcards</p><p class="empty-state__text">' + esc(r.j.error || "Inténtalo de nuevo en un momento.") + '</p><button class="btn btn--primary" type="button" data-reintentar>Reintentar</button></div>'; raiz.querySelector("[data-reintentar]").addEventListener("click", function () { montar(raiz); }); return; }
      lista(raiz, r.j);
    });
  }

  function lista(raiz, d) {
    var T = d.tarjetas, ahora = d.ahora, ped = d.pendientes;
    var cnt = { nuevo: 0, aprendiendo: 0, repaso: 0, reaprendiendo: 0 }; T.forEach(function (t) { cnt[t.estado] = (cnt[t.estado] || 0) + 1; });
    var h = '<header class="page-head"><p class="kicker">Estudio</p><h1 class="page-head__title">Mis Flashcards</h1><p class="page-head__lead">Tarjetas creadas desde tus errores. El repaso espaciado te las muestra justo antes de olvidarlas.</p></header>';
    if (!T.length) {
      raiz.innerHTML = h + '<div class="empty-state"><p class="empty-state__title">Todavía no tienes flashcards</p><p class="empty-state__text">Responde una pregunta y pulsa «Convertir en flashcard» en su comentario docente.</p><a class="btn btn--primary" href="#/banco">Ir al banco de preguntas</a></div>';
      return;
    }
    h += '<dl class="fc-kpis"><div class="fc-kpi"><dt>Pendientes ahora</dt><dd>' + ped + '</dd></div><div class="fc-kpi"><dt>Repasadas hoy</dt><dd>' + d.repasadas_hoy + '</dd></div><div class="fc-kpi"><dt>Total</dt><dd>' + T.length + '</dd></div><div class="fc-kpi"><dt>Nuevas</dt><dd>' + cnt.nuevo + '</dd></div></dl>' +
      '<div class="fc-acciones"><button class="btn btn--primary btn--lg" type="button" data-estudiar' + (ped ? "" : " disabled") + '>' + (ped ? "Repasar " + ped + (ped === 1 ? " tarjeta" : " tarjetas") : "No hay tarjetas pendientes") + '</button>' +
      '<a class="btn btn--ghost" href="' + BASE + 'cuenta.php?a=fc_exportar" download>Exportar CSV (Anki)</a></div>' +
      '<section class="card card--spaced"><h2 class="card__h">Todas tus tarjetas</h2><ul class="fc-lista">' + T.map(function (t) {
        return '<li class="fc-item" data-id="' + t.id + '"><div class="fc-item__txt"><p class="fc-item__f">' + esc(recorte(t.frente, 150)) + '</p><p class="fc-item__m"><span class="badge">' + esc(ETQ[t.estado] || t.estado) + '</span> ' + esc(t.especialidad) + (t.tema ? " · " + esc(t.tema) : "") + ' · ' + esc(cuando(t.proximo, ahora)) + '</p></div>' +
          '<div class="fc-item__btn"><button class="btn btn--ghost btn--sm" type="button" data-editar>Editar</button><button class="btn btn--ghost btn--sm btn--danger" type="button" data-borrar>Borrar</button></div></li>';
      }).join("") + '</ul></section><p class="muted small fc-nota">Calendario: variante de SM-2 con pasos de aprendizaje (no es FSRS). Crear una tarjeta no la marca como conocida: solo cuenta cuando la repasas.</p>';
    raiz.innerHTML = '<div class="fc-wrap">' + h + '</div>';
    var w = raiz.firstChild;
    var est = w.querySelector("[data-estudiar]"); if (est) est.addEventListener("click", function () { estudiar(raiz); });
    w.addEventListener("click", function (ev) {
      var li = ev.target.closest && ev.target.closest(".fc-item"); if (!li) return;
      var id = +li.getAttribute("data-id"), t = T.filter(function (x) { return x.id === id; })[0];
      if (ev.target.closest("[data-borrar]")) {
        var b = ev.target.closest("[data-borrar]");
        if (b.getAttribute("data-a") !== "1") { b.setAttribute("data-a", "1"); b.textContent = "¿Seguro? Pulsa otra vez"; setTimeout(function () { if (b.isConnected) { b.removeAttribute("data-a"); b.textContent = "Borrar"; } }, 3500); return; }
        api("fc_borrar", { id: id }).then(function (r) { if (r.ok) montar(raiz); });
      } else if (ev.target.closest("[data-editar]")) {
        li.innerHTML = '<form class="fc-edit"><label class="fc-lbl">Frente<textarea rows="4" maxlength="600" name="f">' + esc(t.frente) + '</textarea></label><label class="fc-lbl">Dorso<textarea rows="5" maxlength="1500" name="d">' + esc(t.dorso) + '</textarea></label><p class="fc-msg" role="status"></p><div class="fc-item__btn"><button type="submit" class="btn btn--primary btn--sm">Guardar</button><button type="button" class="btn btn--ghost btn--sm" data-cancelar>Cancelar</button></div></form>';
        var f = li.querySelector("form"); f.querySelector("textarea").focus();
        f.querySelector("[data-cancelar]").addEventListener("click", function () { montar(raiz); });
        f.addEventListener("submit", function (e) {
          e.preventDefault();
          api("fc_editar", { id: id, frente: f.f.value, dorso: f.d.value }).then(function (r) {
            if (r.ok) montar(raiz); else { var m = f.querySelector(".fc-msg"); m.textContent = r.j.error || "No se pudo guardar."; m.className = "fc-msg is-err"; }
          });
        });
      }
    });
  }

  /* ---------- sesión de repaso ---------- */
  function estudiar(raiz) {
    api("fc_cola").then(function (r) {
      if (!r.ok) { raiz.innerHTML = '<div class="empty-state"><p class="empty-state__title">No pudimos cargar el repaso</p><p class="empty-state__text">' + esc(r.j.error || "") + '</p><a class="btn btn--primary" href="#/flashcards" data-volver>Volver</a></div>'; return; }
      var cola = r.j.cola, i = 0, hechas = 0, otra = 0;
      if (!cola.length) { montar(raiz); return; }
      var NOM = { otra_vez: "Otra vez", dificil: "Difícil", bien: "Bien", facil: "Fácil" };
      function fin() {
        document.removeEventListener("keydown", tecla);
        raiz.innerHTML = '<div class="page"><div class="card fc-fin"><h2>¡Repaso terminado!</h2><p>Repasaste ' + hechas + (hechas === 1 ? " tarjeta" : " tarjetas") + (otra ? " y " + (otra === 1 ? "1 volverá" : otra + " volverán") + " a aparecer pronto." : ".") + '</p><button class="btn btn--primary" type="button" data-volver>Volver a Mis Flashcards</button></div></div>';
        raiz.querySelector("[data-volver]").addEventListener("click", function () { montar(raiz); });
      }
      var revelada = false;
      function pintar() {
        if (i >= cola.length) { fin(); return; }
        var t = cola[i]; revelada = false;
        raiz.innerHTML = '<div class="fc-estudio"><div class="fc-prog" aria-hidden="true"><i style="width:' + Math.round(i / cola.length * 100) + '%"></i></div>' +
          '<p class="fc-cont" aria-live="polite">Tarjeta ' + (i + 1) + ' de ' + cola.length + ' · ' + esc(t.especialidad) + (t.tema ? " · " + esc(t.tema) : "") + '</p>' +
          '<article class="fc-carta" aria-label="Tarjeta"><p class="fc-cara">Pregunta</p><p class="fc-texto">' + esc(t.frente) + '</p>' +
          '<div class="fc-dorso" id="fcDorso" hidden><p class="fc-cara">Respuesta</p><p class="fc-texto">' + esc(t.dorso) + '</p><p class="fc-src">Fuente: ' + esc(t.fuente || "tu tarjeta") + '</p></div></article>' +
          '<div class="fc-ctl"><button class="btn btn--primary btn--lg" type="button" id="fcMostrar">Mostrar respuesta <kbd>Espacio</kbd></button>' +
          '<div class="fc-notas" id="fcNotas" hidden>' + ["otra_vez", "dificil", "bien", "facil"].map(function (c, k) { return '<button class="fc-nota-b fc-nota-b--' + c + '" type="button" data-c="' + c + '"><b>' + NOM[c] + '</b><small>' + esc(t.previas[c]) + '</small><kbd>' + (k + 1) + '</kbd></button>'; }).join("") + '</div></div>' +
          '<p class="fc-msg" id="fcErr" role="alert"></p><p class="fc-salir"><button class="btn btn--ghost btn--sm" type="button" data-fin>Terminar repaso</button></p></div>';
        raiz.querySelector("#fcMostrar").addEventListener("click", mostrar);
        raiz.querySelector("[data-fin]").addEventListener("click", function () { document.removeEventListener("keydown", tecla); montar(raiz); });
        [].forEach.call(raiz.querySelectorAll("[data-c]"), function (b) { b.addEventListener("click", function () { calificar(b.getAttribute("data-c")); }); });
        raiz.querySelector("#fcMostrar").focus();
      }
      function mostrar() { if (revelada) return; revelada = true; raiz.querySelector("#fcDorso").hidden = false; raiz.querySelector("#fcMostrar").hidden = true; raiz.querySelector("#fcNotas").hidden = false; raiz.querySelector("[data-c=bien]").focus(); }
      var enviando = false;
      function calificar(c) {
        if (!revelada || enviando) return; enviando = true;
        var t = cola[i];
        api("fc_repasar", { id: t.id, calificacion: c, ultimo: t.ultimo }).then(function (r) {
          enviando = false;
          if (!r.ok) { var e = raiz.querySelector("#fcErr"); if (e) { e.textContent = r.j.error || "No se pudo registrar el repaso."; e.className = "fc-msg is-err"; } if (r.http === 409) setTimeout(function () { montar(raiz); }, 1500); return; }
          hechas++; if (c === "otra_vez") otra++; i++; pintar();
        });
      }
      function tecla(ev) {
        if (!raiz.querySelector(".fc-estudio")) { document.removeEventListener("keydown", tecla); return; }
        if (ev.target && /^(INPUT|TEXTAREA|SELECT)$/.test(ev.target.tagName)) return;
        if (ev.key === " " && !revelada) { ev.preventDefault(); mostrar(); }
        else if (revelada && "1234".indexOf(ev.key) >= 0 && ev.key) calificar(["otra_vez", "dificil", "bien", "facil"][+ev.key - 1]);
      }
      document.addEventListener("keydown", tecla);
      pintar();
    });
  }

  M.flashcards = { proponer: proponer, abrirPropuesta: abrirPropuesta, montar: montar, api: api };
})();
