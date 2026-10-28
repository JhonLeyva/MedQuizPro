/* MedQuizPlus · visor de imágenes médicas (zoom, desplazamiento, brillo/contraste, invertir y series por cortes).
   Uso:  MQP.visorImagen.abrir({ titulo, alt, imagenes: ["a.jpg"] o ["c1.jpg", "c2.jpg", …], atribucion: { autor, licencia, licenciaUrl, fuente, fuenteUrl, nota } }, botonQueLoAbrio)
   Solo muestra imágenes que TÚ aportas: cada una debe tener licencia que permita su uso en una web con planes de pago (o ser propia y anonimizada).
   La atribución se muestra siempre. Sin dependencias; no envía datos a ningún servidor. Teclado: + − 0 zoom · Shift+flechas mover · ↑ ↓ corte · I invertir · Esc cerrar. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function enlace(url, txt) { return /^https?:\/\//i.test(url || "") ? '<a href="' + esc(url) + '" target="_blank" rel="noopener noreferrer">' + esc(txt) + "</a>" : esc(txt); }
  var ZMIN = 1, ZMAX = 8, dlg = null, previo = null;

  function cerrar() { if (!dlg) return; if (dlg.close) { try { dlg.close(); } catch (e) {} } dlg.remove(); dlg = null; document.documentElement.classList.remove("vi-abierto"); if (previo && previo.focus && document.body.contains(previo)) previo.focus(); previo = null; }

  function abrir(o, disparador) {
    var imgs = (o.imagenes || []).slice(); if (!imgs.length) return;
    previo = disparador || document.activeElement; var guardado = previo; cerrar(); previo = guardado;
    var a = o.atribucion || {}, serie = imgs.length > 1;
    var S = { z: 1, x: 0, y: 0, br: 100, ct: 100, inv: false, i: 0 };
    dlg = document.createElement("dialog"); dlg.className = "vi-dlg"; dlg.setAttribute("aria-labelledby", "viT");
    dlg.innerHTML = '<div class="vi"><header class="vi-cab"><h2 id="viT">' + esc(o.titulo || "Imagen") + '</h2><button type="button" class="vi-x" data-a="cerrar" aria-label="Cerrar el visor">✕</button></header>' +
      '<div class="vi-barra" role="toolbar" aria-label="Herramientas de la imagen">' +
      '<button type="button" data-a="mas" aria-label="Acercar">+</button><button type="button" data-a="menos" aria-label="Alejar">−</button><button type="button" data-a="ajustar">Ajustar</button>' +
      '<label class="vi-sl">Brillo <input type="range" min="40" max="200" value="100" data-r="br" aria-label="Brillo"></label>' +
      '<label class="vi-sl">Contraste <input type="range" min="40" max="260" value="100" data-r="ct" aria-label="Contraste"></label>' +
      '<button type="button" data-a="inv" aria-pressed="false">Invertir</button><button type="button" data-a="reset">Restablecer</button></div>' +
      (serie ? '<div class="vi-serie"><label for="viCorte">Corte <output id="viCorteN" aria-live="polite">1 / ' + imgs.length + '</output></label><input id="viCorte" type="range" min="1" max="' + imgs.length + '" value="1" aria-label="Corte de la serie (flechas arriba y abajo)"></div>' : "") +
      '<div class="vi-marco" id="viMarco" tabindex="0" aria-label="Imagen: ' + esc(o.alt || o.titulo || "") + '. Arrastra para mover, rueda para acercar."><img id="viImg" src="' + esc(imgs[0]) + '" alt="' + esc(o.alt || o.titulo || "Imagen médica") + '" draggable="false"></div>' +
      '<p class="vi-info" id="viInfo" aria-live="polite"></p>' +
      '<footer class="vi-atr"><p>' + (a.nota ? "<strong>" + esc(a.nota) + "</strong><br>" : "") + [a.autor ? "Autor: " + esc(a.autor) : "", a.licencia ? "Licencia: " + enlace(a.licenciaUrl, a.licencia) : "", a.fuente ? "Fuente: " + enlace(a.fuenteUrl, a.fuente) : ""].filter(Boolean).join(" · ") +
      '</p><p class="vi-aviso">Material educativo. No sustituye el informe radiológico ni el juicio clínico.</p></footer></div>';
    document.body.appendChild(dlg); document.documentElement.classList.add("vi-abierto");
    var marco = dlg.querySelector("#viMarco"), img = dlg.querySelector("#viImg"), info = dlg.querySelector("#viInfo");

    function limites() { var w = marco.clientWidth * (S.z - 1) / 2, h = marco.clientHeight * (S.z - 1) / 2; return { w: w, h: h }; }
    function pintar() {
      var l = limites(); S.x = Math.max(-l.w, Math.min(l.w, S.x)); S.y = Math.max(-l.h, Math.min(l.h, S.y));
      img.style.transform = "translate(" + S.x + "px," + S.y + "px) scale(" + S.z + ")";
      img.style.filter = "brightness(" + S.br + "%) contrast(" + S.ct + "%)" + (S.inv ? " invert(1)" : "");
      marco.classList.toggle("is-zoom", S.z > 1);
      info.textContent = "Zoom " + Math.round(S.z * 100) + " % · Brillo " + S.br + " % · Contraste " + S.ct + " %" + (S.inv ? " · invertida" : "") + (serie ? " · corte " + (S.i + 1) + " de " + imgs.length : "");
    }
    function zoom(f, cx, cy) {
      var nz = Math.max(ZMIN, Math.min(ZMAX, S.z * f)); if (nz === S.z) return;
      var r = marco.getBoundingClientRect(), px = (cx == null ? r.left + r.width / 2 : cx) - (r.left + r.width / 2), py = (cy == null ? r.top + r.height / 2 : cy) - (r.top + r.height / 2);
      var k = nz / S.z; S.x = px - (px - S.x) * k; S.y = py - (py - S.y) * k; S.z = nz; if (S.z === 1) { S.x = 0; S.y = 0; } pintar();
    }
    function corte(n) { if (!serie) return; S.i = Math.max(0, Math.min(imgs.length - 1, n)); img.src = imgs[S.i]; var c = dlg.querySelector("#viCorte"); c.value = S.i + 1; dlg.querySelector("#viCorteN").textContent = (S.i + 1) + " / " + imgs.length; pintar(); }
    function reset() { S.z = 1; S.x = 0; S.y = 0; S.br = 100; S.ct = 100; S.inv = false; [].forEach.call(dlg.querySelectorAll("[data-r]"), function (r) { r.value = 100; }); var b = dlg.querySelector("[data-a=inv]"); b.setAttribute("aria-pressed", "false"); pintar(); }

    dlg.addEventListener("click", function (ev) {
      var b = ev.target.closest && ev.target.closest("[data-a]"); if (!b) { if (ev.target === dlg) cerrar(); return; }
      var x = b.getAttribute("data-a");
      if (x === "cerrar") cerrar(); else if (x === "mas") zoom(1.4); else if (x === "menos") zoom(1 / 1.4); else if (x === "ajustar") { S.z = 1; S.x = 0; S.y = 0; pintar(); }
      else if (x === "inv") { S.inv = !S.inv; b.setAttribute("aria-pressed", String(S.inv)); pintar(); } else if (x === "reset") reset();
    });
    dlg.addEventListener("input", function (ev) { var r = ev.target.getAttribute && ev.target.getAttribute("data-r"); if (r) { S[r] = +ev.target.value; pintar(); } else if (ev.target.id === "viCorte") corte(+ev.target.value - 1); });
    marco.addEventListener("wheel", function (ev) { ev.preventDefault(); zoom(ev.deltaY < 0 ? 1.15 : 1 / 1.15, ev.clientX, ev.clientY); }, { passive: false });
    marco.addEventListener("dblclick", function (ev) { if (S.z > 1) { S.z = 1; S.x = 0; S.y = 0; pintar(); } else zoom(2.5, ev.clientX, ev.clientY); });
    /* arrastre y pellizco con eventos de puntero */
    var ptrs = {}, dist0 = 0, z0 = 1;
    marco.addEventListener("pointerdown", function (ev) { marco.setPointerCapture(ev.pointerId); ptrs[ev.pointerId] = { x: ev.clientX, y: ev.clientY }; var ids = Object.keys(ptrs); if (ids.length === 2) { dist0 = Math.hypot(ptrs[ids[0]].x - ptrs[ids[1]].x, ptrs[ids[0]].y - ptrs[ids[1]].y); z0 = S.z; } });
    marco.addEventListener("pointermove", function (ev) {
      var p = ptrs[ev.pointerId]; if (!p) return; var ids = Object.keys(ptrs);
      if (ids.length === 2) { var d = Math.hypot(ptrs[ids[0]].x - ptrs[ids[1]].x, ptrs[ids[0]].y - ptrs[ids[1]].y); ptrs[ev.pointerId] = { x: ev.clientX, y: ev.clientY }; d = Math.hypot(ptrs[ids[0]].x - ptrs[ids[1]].x, ptrs[ids[0]].y - ptrs[ids[1]].y); if (dist0) zoom((z0 * d / dist0) / S.z); return; }
      S.x += ev.clientX - p.x; S.y += ev.clientY - p.y; ptrs[ev.pointerId] = { x: ev.clientX, y: ev.clientY }; pintar();
    });
    function suelta(ev) { delete ptrs[ev.pointerId]; dist0 = 0; }
    marco.addEventListener("pointerup", suelta); marco.addEventListener("pointercancel", suelta);
    dlg.addEventListener("keydown", function (ev) {
      var k = ev.key, t = ev.target && ev.target.tagName; if (t === "INPUT" && ev.target.type === "range" && /Arrow/.test(k)) return;
      if (k === "+" || k === "=") { zoom(1.4); ev.preventDefault(); } else if (k === "-" || k === "_") { zoom(1 / 1.4); ev.preventDefault(); } else if (k === "0") { S.z = 1; S.x = 0; S.y = 0; pintar(); }
      else if (k === "i" || k === "I") { dlg.querySelector("[data-a=inv]").click(); }
      else if (ev.shiftKey && /^Arrow/.test(k)) { var s = 40; if (k === "ArrowLeft") S.x += s; if (k === "ArrowRight") S.x -= s; if (k === "ArrowUp") S.y += s; if (k === "ArrowDown") S.y -= s; pintar(); ev.preventDefault(); }
      else if (serie && k === "ArrowUp") { corte(S.i - 1); ev.preventDefault(); } else if (serie && k === "ArrowDown") { corte(S.i + 1); ev.preventDefault(); }
    });
    dlg.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
    window.addEventListener("resize", pintar);
    dlg.addEventListener("close", function () { window.removeEventListener("resize", pintar); });
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", "");
    pintar(); dlg.querySelector(".vi-x").focus();
  }
  M.visorImagen = { abrir: abrir, cerrar: cerrar };
})();
