/* MedQuizPlus — gráficos de análisis (SVG/HTML a mano, sin librerías).
 *
 * Cada función devuelve HTML listo para insertar. Todos los datos que se grafican son reales
 * (tu progreso en este navegador, o el conteo del banco publicado): aquí no se inventa nada.
 *
 *   MQP_GRAF.donut(correctas, incorrectas, {titulo})
 *   MQP_GRAF.linea(puntos[{x, y(0-100), n, tip}], {titulo, sufijo})
 *   MQP_GRAF.barras(filas[{etiqueta, valor, max?, texto, sub, tip}], {titulo})
 *   MQP_GRAF.columnas(filas[{etiqueta, valor, texto, tip}], {titulo})
 *   MQP_GRAF.calor(dias[{fecha:Date, n}], {semanas})
 *   MQP_GRAF.iniciarTips()      tooltips para [data-tip] (se llama una vez)
 *
 * Reglas: una sola serie por gráfico (el título la nombra), marcas finas, barras con extremo redondeado de 4 px,
 * líneas de 2 px, una sola escala por gráfico, etiquetas solo donde cuentan, y cada gráfico trae su tabla de datos.
 */
(function () {
  "use strict";
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function miles(n) { try { return Number(n).toLocaleString("es-PE"); } catch (e) { return String(n); } }

  /* tabla de datos (vista accesible alternativa) */
  function tabla(cab, filas) {
    return '<details class="g-datos"><summary>Ver datos en tabla</summary><table><thead><tr>' +
      cab.map(function (c) { return "<th scope=\"col\">" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>" +
      filas.map(function (f) { return "<tr>" + f.map(function (c, i) { return (i === 0 ? "<th scope=\"row\">" : "<td>") + esc(c) + (i === 0 ? "</th>" : "</td>"); }).join("") + "</tr>"; }).join("") +
      "</tbody></table></details>";
  }

  /* ---------------------------------------------------------------- donut */
  function donut(ok, mal, o) {
    o = o || {};
    var total = ok + mal, R = 52, C = 2 * Math.PI * R, G = total > 1 && ok && mal ? 3 : 0;   // 3 px de aire entre los dos tramos
    var pct = total ? Math.round(ok / total * 100) : 0;
    var lenOk = total ? Math.max(C * ok / total - G, 0) : 0, lenMal = total ? Math.max(C * mal / total - G, 0) : 0;
    return '<figure class="g-fig g-donut"><svg viewBox="0 0 140 140" role="img" aria-label="' + esc((o.titulo || "Aciertos") + ": " + pct + "% correctas, " + ok + " de " + total) + '">' +
      '<circle class="g-donut__pista" cx="70" cy="70" r="' + R + '"/>' +
      (ok ? '<circle class="g-donut__ok" cx="70" cy="70" r="' + R + '" stroke-dasharray="' + lenOk.toFixed(1) + " " + (C - lenOk).toFixed(1) + '" transform="rotate(-90 70 70)" data-tip="Correctas: ' + miles(ok) + ' (' + pct + '%)"/>' : "") +
      (mal ? '<circle class="g-donut__mal" cx="70" cy="70" r="' + R + '" stroke-dasharray="' + lenMal.toFixed(1) + " " + (C - lenMal).toFixed(1) + '" stroke-dashoffset="' + (-(lenOk + G)).toFixed(1) + '" transform="rotate(-90 70 70)" data-tip="Incorrectas: ' + miles(mal) + ' (' + (100 - pct) + '%)"/>' : "") +
      '<text x="70" y="68" class="g-donut__num" text-anchor="middle">' + pct + '%</text><text x="70" y="88" class="g-donut__sub" text-anchor="middle">correctas</text></svg>' +
      '<figcaption class="g-leyenda"><span><i class="g-sw g-sw--ok"></i>Correctas <b>' + miles(ok) + '</b></span><span><i class="g-sw g-sw--mal"></i>Incorrectas <b>' + miles(mal) + '</b></span></figcaption></figure>';
  }

  /* ---------------------------------------------------------------- línea */
  function linea(pts, o) {
    o = o || {};
    var W = 640, H = 230, L = 40, Rr = 18, T = 14, B = 34, iw = W - L - Rr, ih = H - T - B;
    var n = pts.length, suf = o.sufijo || "%";
    function X(i) { return L + (n === 1 ? iw / 2 : iw * i / (n - 1)); }
    function Y(v) { return T + ih * (1 - v / 100); }
    var grid = [0, 25, 50, 75, 100].map(function (v) {
      return '<line class="g-grid" x1="' + L + '" x2="' + (W - Rr) + '" y1="' + Y(v) + '" y2="' + Y(v) + '"/><text class="g-eje" x="' + (L - 8) + '" y="' + (Y(v) + 4) + '" text-anchor="end">' + v + suf + '</text>';
    }).join("");
    var d = pts.map(function (p, i) { return (i ? "L" : "M") + X(i).toFixed(1) + " " + Y(p.y).toFixed(1); }).join(" ");
    var area = n > 1 ? d + " L" + X(n - 1).toFixed(1) + " " + Y(0) + " L" + X(0).toFixed(1) + " " + Y(0) + " Z" : "";
    var paso = Math.max(1, Math.ceil(n / 6)), xs = pts.map(function (p, i) {
      return (i === n - 1 || (i % paso === 0 && (paso === 1 || n - 1 - i >= 2))) ? '<text class="g-eje" x="' + X(i).toFixed(1) + '" y="' + (H - 10) + '" text-anchor="' + (i === 0 && n > 1 ? "start" : i === n - 1 && n > 1 ? "end" : "middle") + '">' + esc(p.x) + '</text>' : "";
    }).join("");
    var pr = pts[n - 1];
    var puntos = pts.map(function (p, i) {
      return '<circle class="g-hit" cx="' + X(i).toFixed(1) + '" cy="' + Y(p.y).toFixed(1) + '" r="14" tabindex="0" data-tip="' + esc(p.tip || (p.x + ": " + p.y + suf)) + '"/>' +
        '<circle class="g-punto' + (i === n - 1 ? " g-punto--fin" : "") + '" cx="' + X(i).toFixed(1) + '" cy="' + Y(p.y).toFixed(1) + '" r="' + (i === n - 1 ? 5 : 4) + '"/>';
    }).join("");
    var fin = '<text class="g-valor" x="' + Math.min(X(n - 1), W - Rr - 4).toFixed(1) + '" y="' + (Y(pr.y) - 12).toFixed(1) + '" text-anchor="' + (n > 1 ? "end" : "middle") + '">' + pr.y + suf + '</text>';
    return '<figure class="g-fig"><svg class="g-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc((o.titulo || "Evolución") + ": último valor " + pr.y + suf + " en " + n + " puntos") + '">' + grid +
      (area ? '<path class="g-area" d="' + area + '"/>' : "") + '<path class="g-linea" d="' + d + '"/>' + puntos + fin + xs + '</svg>' +
      tabla([o.colX || "Fecha", o.colY || "Valor", "Dato"], pts.map(function (p) { return [p.x, p.y + suf, p.n != null ? p.n : ""]; })) + '</figure>';
  }

  /* ---------------------------------------------------------------- barras horizontales (HTML) */
  function barras(filas, o) {
    o = o || {};
    var max = o.max || Math.max.apply(null, filas.map(function (f) { return f.valor; }).concat([1]));
    return '<figure class="g-fig"><ul class="g-barras" role="list">' + filas.map(function (f) {
      var w = Math.max(f.valor / (f.max || max) * 100, f.valor > 0 ? 1.5 : 0);
      return '<li class="g-barra" tabindex="0" data-tip="' + esc(f.tip || (f.etiqueta + ": " + f.texto)) + '"><span class="g-barra__et">' + esc(f.etiqueta) + (f.sub ? "<small>" + esc(f.sub) + "</small>" : "") + '</span>' +
        '<span class="g-barra__pista"><span class="g-barra__rel" style="width:' + w.toFixed(1) + '%"></span></span><span class="g-barra__val">' + esc(f.texto) + '</span></li>';
    }).join("") + '</ul>' + tabla([o.colA || "Elemento", o.colB || "Valor"], filas.map(function (f) { return [f.etiqueta, f.texto + (f.sub ? " · " + f.sub : "")]; })) + '</figure>';
  }

  /* ---------------------------------------------------------------- columnas */
  function columnas(filas, o) {
    o = o || {};
    var max = o.max || Math.max.apply(null, filas.map(function (f) { return f.valor; }).concat([1]));
    return '<figure class="g-fig"><div class="g-cols" role="list" style="--n:' + filas.length + '">' + filas.map(function (f) {
      var h = Math.max(f.valor / max * 100, f.valor > 0 ? 2 : 0);
      return '<div class="g-col" role="listitem" tabindex="0" data-tip="' + esc(f.tip || (f.etiqueta + ": " + f.texto)) + '"><span class="g-col__val">' + esc(f.texto) + '</span><span class="g-col__pista"><span class="g-col__rel" style="height:' + h.toFixed(1) + '%"></span></span><span class="g-col__et">' + esc(f.etiqueta) + '</span></div>';
    }).join("") + '</div>' + tabla([o.colA || "Elemento", o.colB || "Valor"], filas.map(function (f) { return [f.etiqueta, f.texto]; })) + '</figure>';
  }

  /* ---------------------------------------------------------------- mapa de calor semanal */
  function calor(dias, o) {
    o = o || {};
    var sem = o.semanas || 12, hoy = new Date(); hoy.setHours(0, 0, 0, 0);
    var mapa = {}, max = 0;
    dias.forEach(function (d) { var k = d.fecha.toDateString(); mapa[k] = (mapa[k] || 0) + d.n; });
    for (var k in mapa) if (mapa[k] > max) max = mapa[k];
    var dow = (hoy.getDay() + 6) % 7;                     // lunes = 0
    var inicio = new Date(hoy); inicio.setDate(hoy.getDate() - dow - (sem - 1) * 7);
    var C = 15, S = 4, celdas = "", fmt;
    try { fmt = new Intl.DateTimeFormat("es-PE", { weekday: "long", day: "numeric", month: "long" }); } catch (e) { fmt = null; }
    for (var w = 0; w < sem; w++) for (var r = 0; r < 7; r++) {
      var f = new Date(inicio); f.setDate(inicio.getDate() + w * 7 + r);
      if (f > hoy) continue;
      var n = mapa[f.toDateString()] || 0, nivel = !n ? 0 : Math.min(4, 1 + Math.floor((n / max) * 3.999));
      celdas += '<rect class="g-cel g-cel--' + nivel + '" x="' + (30 + w * (C + S)) + '" y="' + (r * (C + S)) + '" width="' + C + '" height="' + C + '" rx="3" tabindex="0" data-tip="' + esc((fmt ? fmt.format(f) : f.toDateString()) + ": " + (n ? n + (n === 1 ? " pregunta" : " preguntas") : "sin actividad")) + '"/>';
    }
    var W = 30 + sem * (C + S), H = 7 * (C + S);
    var dn = ["L", "", "M", "", "V", "", "D"].map(function (t, i) { return t ? '<text class="g-eje" x="0" y="' + (i * (C + S) + 12) + '">' + t + '</text>' : ""; }).join("");
    return '<figure class="g-fig"><svg class="g-svg g-svg--calor" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="Actividad diaria de las últimas ' + sem + ' semanas">' + dn + celdas + '</svg>' +
      '<figcaption class="g-escala"><span>Menos</span><i class="g-cel g-cel--0"></i><i class="g-cel g-cel--1"></i><i class="g-cel g-cel--2"></i><i class="g-cel g-cel--3"></i><i class="g-cel g-cel--4"></i><span>Más</span></figcaption></figure>';
  }

  /* ---------------------------------------------------------------- tooltips (una sola vez) */
  var tipEl = null, activo = null;
  function iniciarTips() {
    if (tipEl) return;
    tipEl = document.createElement("div"); tipEl.className = "g-tip"; tipEl.setAttribute("role", "tooltip"); tipEl.hidden = true; document.body.appendChild(tipEl);
    function mostrar(el, x, y) {
      tipEl.textContent = el.getAttribute("data-tip"); tipEl.hidden = false;
      var w = tipEl.offsetWidth, h = tipEl.offsetHeight;
      tipEl.style.left = Math.max(8, Math.min(x - w / 2, window.innerWidth - w - 8)) + "px";
      tipEl.style.top = (y - h - 12 < 8 ? y + 18 : y - h - 12) + "px";
    }
    document.addEventListener("pointerover", function (e) { var el = e.target.closest && e.target.closest("[data-tip]"); if (!el) return; activo = el; mostrar(el, e.clientX, e.clientY); });
    document.addEventListener("pointermove", function (e) { if (activo && !tipEl.hidden) mostrar(activo, e.clientX, e.clientY); });
    document.addEventListener("pointerout", function (e) { var el = e.target.closest && e.target.closest("[data-tip]"); if (el && !el.contains(e.relatedTarget)) { tipEl.hidden = true; activo = null; } });
    document.addEventListener("focusin", function (e) { var el = e.target.closest && e.target.closest("[data-tip]"); if (!el) return; var r = el.getBoundingClientRect(); activo = el; mostrar(el, r.left + r.width / 2, r.top); });
    document.addEventListener("focusout", function () { tipEl.hidden = true; activo = null; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") tipEl.hidden = true; });
  }

  /* ---------------------------------------------------------------- web pública: el banco, en números (datos reales del banco) */
  function bancoEnNumeros() {
    var cE = document.getElementById("anEsp"), cA = document.getElementById("anAnio");
    if (!cE || !cA || !window.MQP || !MQP.cargarTodo) return;
    var hecho = false;
    function pintar() {
      if (hecho) return; hecho = true;
      MQP.cargarTodo().then(function (d) {
        var porEsp = {}, porAnio = {};
        d.preguntas.forEach(function (q) {
          porEsp[q.especialidad] = (porEsp[q.especialidad] || 0) + 1;
          var m = /(20\d\d)/.exec(q.examen || ""); if (m) porAnio[m[1]] = (porAnio[m[1]] || 0) + 1;
        });
        var esp = Object.keys(porEsp).map(function (k) { return { etiqueta: k, valor: porEsp[k], texto: miles(porEsp[k]) }; }).sort(function (a, b) { return b.valor - a.valor; });
        var anios = Object.keys(porAnio).sort().map(function (a) { return { etiqueta: a, valor: porAnio[a], texto: miles(porAnio[a]), tip: "ENAM " + a + ": " + miles(porAnio[a]) + " preguntas" }; });
        if (!esp.length) { var s0 = document.getElementById("analisis"); if (s0) s0.hidden = true; return; }
        cE.innerHTML = barras(esp.slice(0, 10), { colA: "Especialidad", colB: "Preguntas" });
        cA.innerHTML = anios.length ? columnas(anios, { colA: "Año", colB: "Preguntas" }) : "";
        iniciarTips();
      }, function () { var s = document.getElementById("analisis"); if (s) s.hidden = true; });
    }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { io.disconnect(); pintar(); } }, { rootMargin: "300px 0px" });
      io.observe(document.getElementById("analisis") || cE);
    } else pintar();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", bancoEnNumeros); else bancoEnNumeros();

  window.MQP_GRAF = { donut: donut, linea: linea, barras: barras, columnas: columnas, calor: calor, iniciarTips: iniciarTips };
})();
