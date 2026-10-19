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
    var bl = o.blanco || 0, total = ok + mal + bl, R = 52, C = 2 * Math.PI * R;
    var tramos = [["ok", ok, "Correctas"], ["mal", mal, "Incorrectas"], ["bl", bl, "Sin responder"]].filter(function (t) { return t[1] > 0; });
    var G = tramos.length > 1 ? 3 : 0;                       // 3 px de aire entre tramos
    var pct = total ? Math.round(ok / total * 100) : 0, acum = 0, arcos = "";
    tramos.forEach(function (t) {
      var len = Math.max(C * t[1] / total - G, 0);
      arcos += '<circle class="g-donut__' + t[0] + '" cx="70" cy="70" r="' + R + '" stroke-dasharray="' + len.toFixed(1) + " " + (C - len).toFixed(1) + '" stroke-dashoffset="' + (-acum).toFixed(1) + '" transform="rotate(-90 70 70)" data-tip="' + t[2] + ": " + miles(t[1]) + " (" + Math.round(t[1] / total * 100) + '%)"/>';
      acum += len + G;
    });
    return '<figure class="g-fig g-donut"><svg viewBox="0 0 140 140" role="img" aria-label="' + esc((o.titulo || "Aciertos") + ": " + pct + "% correctas, " + ok + " de " + total) + '">' +
      '<circle class="g-donut__pista" cx="70" cy="70" r="' + R + '"/>' + arcos +
      '<text x="70" y="68" class="g-donut__num" text-anchor="middle">' + pct + '%</text><text x="70" y="88" class="g-donut__sub" text-anchor="middle">correctas</text></svg>' +
      '<figcaption class="g-leyenda"><span><i class="g-sw g-sw--ok"></i>Correctas <b>' + miles(ok) + '</b></span><span><i class="g-sw g-sw--mal"></i>Incorrectas <b>' + miles(mal) + '</b></span>' +
      (bl ? '<span><i class="g-sw g-sw--bl"></i>Sin responder <b>' + miles(bl) + '</b></span>' : "") + '</figcaption></figure>';
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

  /* ---------------------------------------------------------------- web pública: el banco, en vivo */
  var COL_AREA = ["#0f766e", "#0d9488", "#115e59", "#0a7f74", "#134e4a", "#0b6b63"];   // solo el verde-azulado de la marca: una tonalidad distinta por área (texto blanco legible)

  function squarify(vals, W, H) {
    var tot = vals.reduce(function (a, b) { return a + b; }, 0), sc = W * H / tot, a = vals.map(function (v) { return v * sc; });
    var res = [], x = 0, y = 0, w = W, h = H, i = 0;
    while (i < a.length) {
      var lado = Math.min(w, h), fila = [], j = i, s = 0, mejor = Infinity;
      while (j < a.length) {
        var t = fila.concat(a[j]), ss = s + a[j], mx = Math.max.apply(null, t), mn = Math.min.apply(null, t);
        var peor = Math.max(lado * lado * mx / (ss * ss), ss * ss / (lado * lado * mn));
        if (fila.length && peor > mejor) break;
        mejor = peor; fila = t; s = ss; j++;
      }
      if (w >= h) { var cw = s / h, yy = y; fila.forEach(function (r, k) { var rh = r / cw; res.push({ i: i + k, x: x, y: yy, w: cw, h: rh }); yy += rh; }); x += cw; w -= cw; }
      else { var rh2 = s / w, xx = x; fila.forEach(function (r, k) { var rw = r / rh2; res.push({ i: i + k, x: xx, y: y, w: rw, h: rh2 }); xx += rw; }); y += rh2; h -= rh2; }
      i = j;
    }
    return res;
  }

  function contar(el, fin, dur) {
    var reducido = false; try { reducido = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
    if (reducido) { el.textContent = miles(fin); return; }
    var t0 = null;
    (function paso(t) { if (t0 === null) t0 = t; var k = Math.min((t - t0) / dur, 1); el.textContent = miles(Math.round(fin * (1 - Math.pow(1 - k, 3)))); if (k < 1) requestAnimationFrame(paso); })(performance.now());
  }

  function areaAnios(porAnio) {
    var ks = Object.keys(porAnio).sort(), vals = ks.map(function (k) { return porAnio[k]; });
    if (!ks.length) return "";
    var W = 460, H = 220, L = 14, R = 14, T = 34, B = 30, iw = W - L - R, ih = H - T - B, max = Math.max.apply(null, vals) * 1.12;
    function X(i) { return L + (ks.length === 1 ? iw / 2 : iw * i / (ks.length - 1)); } function Y(v) { return T + ih * (1 - v / max); }
    var pts = vals.map(function (v, i) { return [X(i), Y(v)]; }), d = "M" + pts[0][0] + " " + pts[0][1];
    for (var i = 1; i < pts.length; i++) { var cx = (pts[i - 1][0] + pts[i][0]) / 2; d += " C" + cx + " " + pts[i - 1][1] + " " + cx + " " + pts[i][1] + " " + pts[i][0] + " " + pts[i][1]; }
    var area = d + " L" + pts[pts.length - 1][0] + " " + (T + ih) + " L" + pts[0][0] + " " + (T + ih) + " Z";
    return '<figure class="g-fig"><svg class="g-svg sp-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="Preguntas publicadas por año del examen, de ' + esc(ks[0]) + " a " + esc(ks[ks.length - 1]) + '">' +
      '<defs><linearGradient id="spGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" style="stop-color:var(--brand);stop-opacity:.4"/><stop offset="1" style="stop-color:var(--brand);stop-opacity:0"/></linearGradient></defs>' +
      '<path d="' + area + '" fill="url(#spGrad)"/><path class="sp-linea" d="' + d + '"/>' +
      pts.map(function (p, i) { return '<circle class="sp-punto" cx="' + p[0] + '" cy="' + p[1] + '" r="5"/><circle class="g-hit" cx="' + p[0] + '" cy="' + p[1] + '" r="16" tabindex="0" data-tip="ENAM ' + esc(ks[i]) + ": " + miles(vals[i]) + ' preguntas"/><text x="' + p[0] + '" y="' + (p[1] - 13) + '" text-anchor="middle" class="sp-val">' + miles(vals[i]) + '</text><text x="' + p[0] + '" y="' + (H - 8) + '" text-anchor="middle" class="sp-eje">' + esc(ks[i]) + '</text>'; }).join("") + '</svg>' +
      tabla(["Año", "Preguntas"], ks.map(function (k) { return [k, miles(porAnio[k])]; })) + '</figure>';
  }

  function bancoEnVivo() {
    var sec = document.getElementById("analisis"); if (!sec || !window.MQP || !MQP.cargarTodo) return;
    var cK = document.getElementById("anKpis"), cM = document.getElementById("anMapa"), cL = document.getElementById("anLeyenda");
    var datos = null, hecho = false, sel = null, todas = [];
    function mapa() {
      if (!datos) return;
      var W = cM.clientWidth || 600, H = Math.round(W < 560 ? W * 1.15 : W * 0.56);
      cM.style.height = H + "px";
      var rects = squarify(datos.esp.map(function (e) { return e.n; }), 100, 100);
      cM.innerHTML = rects.map(function (r) {
        var e = datos.esp[r.i], pxW = r.w / 100 * W, pxH = r.h / 100 * H, grande = pxW > 130 && pxH > 80,
          lineas = Math.ceil(e.nombre.length * 8.6 / Math.max(pxW - 26, 1)), medio = pxW > 70 && lineas <= 4 && (lineas * 16 + 44) <= pxH;   // el nombre solo se escribe si cabe entero
        return '<div class="tm' + (e.archivo === sel ? " is-sel" : "") + '" role="button" aria-pressed="' + (e.archivo === sel) + '" data-arch="' + esc(e.archivo) + '" tabindex="0" style="left:' + r.x.toFixed(3) + '%;top:' + r.y.toFixed(3) + '%;width:' + r.w.toFixed(3) + '%;height:' + r.h.toFixed(3) + '%;--c:' + COL_AREA[e.area % COL_AREA.length] + '" data-tip="' + esc(e.nombre + " · " + miles(e.n) + " preguntas (" + e.areaNombre + ")") + '"><span class="tm__in">' +
          (medio ? '<b>' + esc(e.nombre) + '</b>' : "") + '<i>' + miles(e.n) + (grande ? " preguntas" : "") + '</i></span></div>';
      }).join("");
    }
    function detalle() {
      var e = datos.esp.filter(function (x) { return x.archivo === sel; })[0]; if (!e) return;
      var qs = todas.filter(function (q) { return q.archivo === sel; }), algos = window.MQP_ALGORITMOS || {}, base = MQP.base || "";
      var temas = {}, anios = {}, flujos = 0;
      qs.forEach(function (q) { var tm = q.categoria || q.tema; if (tm) temas[tm] = (temas[tm] || 0) + 1; var m = /(20\d\d)/.exec(q.examen || ""); if (m) anios[m[1]] = (anios[m[1]] || 0) + 1; var a = algos[q.id]; if (a && a.imagen) flujos++; });
      var tk = Object.keys(temas).sort(function (a, b) { return temas[b] - temas[a]; }).slice(0, 5), ak = Object.keys(anios).sort();
      var ej = qs.filter(function (q) { var a = algos[q.id]; return a && a.imagen && q.enunciado.length < 330; })[0] || qs[0];
      var mx = Math.max.apply(null, tk.map(function (k) { return temas[k]; }).concat(1));
      var barras = tk.length ? '<h4>Temas más frecuentes</h4><ul class="det__bar">' + tk.map(function (k) { return '<li><span>' + esc(k) + '</span><i><u style="width:' + Math.round(temas[k] / mx * 100) + '%"></u></i><b>' + temas[k] + '</b></li>'; }).join("") + '</ul>'
        : ak.length ? '<h4>Convocatorias</h4><ul class="det__bar">' + ak.map(function (k) { return '<li><span>ENAM ' + esc(k) + '</span><i><u style="width:' + Math.round(anios[k] / Math.max.apply(null, ak.map(function (z) { return anios[z]; })) * 100) + '%"></u></i><b>' + anios[k] + '</b></li>'; }).join("") + '</ul>' : "";
      var img = ej && algos[ej.id] && algos[ej.id].imagen ? '<figure class="det__flujo"><img alt="Flujograma clínico de una pregunta de ' + esc(e.nombre) + '" loading="lazy" src="' + esc(base + algos[ej.id].imagen) + '"><figcaption>Flujograma de esta pregunta</figcaption></figure>' : "";
      var cD = document.getElementById("anDetalle");
      cD.innerHTML = '<p class="det__area">' + esc(e.areaNombre) + '</p><h3>' + esc(e.nombre) + '</h3>' +
        '<dl class="det__kpis"><div><dt>Preguntas</dt><dd>' + miles(qs.length) + '</dd></div><div><dt>Con flujograma</dt><dd>' + miles(flujos) + '</dd></div><div><dt>Comentadas</dt><dd>' + miles(qs.filter(function (q) { return q.comentario; }).length) + '</dd></div></dl>' +
        barras +
        (ej ? '<h4>Una pregunta de este banco</h4><blockquote class="det__q">' + esc(ej.enunciado) + '</blockquote>' : "") + img +
        '<a class="btn btn--primary btn--block" href="#registro" data-app="app/#/banco">Practicar ' + esc(e.nombre) + ' gratis</a>';
      mapa(); chips();
    }
    function chips() {
      var c = document.getElementById("anChips"); if (!c) return;
      c.innerHTML = datos.esp.map(function (e) { return '<button class="chip" type="button" data-arch="' + esc(e.archivo) + '" aria-pressed="' + (e.archivo === sel) + '">' + esc(e.nombre) + ' <span class="chip__n">' + miles(e.n) + '</span></button>'; }).join("");
    }
    function elegir(t) { var b = t.closest && t.closest("[data-arch]"); if (!b || b.getAttribute("data-arch") === sel) return; sel = b.getAttribute("data-arch"); detalle(); }
    cM.addEventListener("click", function (ev) { elegir(ev.target); });
    var cC = document.getElementById("anChips"); if (cC) cC.addEventListener("click", function (ev) { elegir(ev.target); });
    cM.addEventListener("keydown", function (ev) { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); elegir(ev.target); } });
    function pintar() {
      if (hecho) return; hecho = true;
      MQP.cargarTodo().then(function (d) {
        var porEsp = {}, porAnio = {}, algos = window.MQP_ALGORITMOS || {}, flujos = 0;
        d.preguntas.forEach(function (q) {
          porEsp[q.archivo] = (porEsp[q.archivo] || 0) + 1;
          var m = /(20\d\d)/.exec(q.examen || ""); if (m) porAnio[m[1]] = (porAnio[m[1]] || 0) + 1;
          var a = algos[q.id]; if (a && (a.imagen || (a.pasos && a.pasos.length))) flujos++;
        });
        var areas = MQP.areas.map(function (a) { return a.id; });
        var esp = MQP.especialidades.filter(function (e) { return porEsp[e.archivo]; }).map(function (e) {
          var ai = Math.max(0, areas.indexOf(e.area)); return { archivo: e.archivo, nombre: e.nombre, n: porEsp[e.archivo], area: ai, areaNombre: (MQP.area(e.area) || {}).nombre || "" };
        }).sort(function (a, b) { return b.n - a.n; });
        if (!esp.length) { sec.hidden = true; return; }
        datos = { esp: esp };
        var anios = Object.keys(porAnio).sort();
        cK.innerHTML = [["Preguntas comentadas", d.preguntas.length, "con su explicación"], ["Flujogramas clínicos", flujos, "uno por pregunta"], ["Especialidades", esp.length, "agrupadas en " + MQP.areas.length + " áreas"], ["Convocatorias", anios.length, anios.length ? anios[0] + " – " + anios[anios.length - 1] : ""]].map(function (k) {
          return '<div class="spot__kpi"><span class="spot__num" data-fin="' + k[1] + '">0</span><span class="spot__et">' + esc(k[0]) + '</span><span class="spot__sub">' + esc(k[2]) + '</span></div>';
        }).join("");
        [].forEach.call(cK.querySelectorAll(".spot__num"), function (el) { contar(el, +el.getAttribute("data-fin"), 1400); });
        if (cL) cL.innerHTML = MQP.areas.map(function (a, i) { return '<li><i style="background:' + COL_AREA[i % COL_AREA.length] + '"></i>' + esc(a.nombre) + '</li>'; }).join("");
        todas = d.preguntas; sel = esp[0].archivo; detalle(); 
        mapa();
        if ("ResizeObserver" in window) { var ult = cM.clientWidth; new ResizeObserver(function () { if (Math.abs(cM.clientWidth - ult) > 8) { ult = cM.clientWidth; mapa(); } }).observe(cM); }
        iniciarTips();
      }, function () { sec.hidden = true; });
    }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { io.disconnect(); pintar(); } }, { rootMargin: "300px 0px" });
      io.observe(sec);
    } else pintar();
  }

  /* ---------------------------------------------------------------- web pública: celulares animados con pantallas reales del banco */
  function celulares() {
    var box = document.getElementById("movilPhones"); if (!box || !window.MQP || !MQP.cargarTodo) return;
    var reducido = false; try { reducido = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
    var hecho = false, visible = true, timers = [];
    function rec(t, n) { t = String(t); return t.length > n ? t.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : t; }
    var LOGO = '<div class="ph__logo"><span class="ph__marca"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"><path d="M12 5.5v13M5.5 12h13"/></svg></span><span>MedQuiz<b>Plus</b></span></div>';
    function esp(f, ms) { timers.push(setTimeout(function () { if (!visible && !reducido) { timers.push(setTimeout(function () { esp(f, 600); }, 600)); return; } f(); }, ms)); }

    function pintar() {
      if (hecho) return; hecho = true;
      MQP.cargarTodo().then(function (d) {
        var algos = window.MQP_ALGORITMOS || {}, base = MQP.base || "";
        var cand = d.preguntas.filter(function (q) { var a = algos[q.id]; return q.comentario && q.comentario.length > 60 && q.enunciado.length < 200 && q.opciones.length >= 4 && a && a.imagen; });
        if (cand.length < 3) { box.parentNode.hidden = true; return; }
        for (var j = cand.length - 1; j > 0; j--) { var r = Math.floor(Math.random() * (j + 1)), t = cand[j]; cand[j] = cand[r]; cand[r] = t; }
        var vistas = {}, qs = []; cand.forEach(function (q) { if (qs.length < 3 && !vistas[q.especialidad]) { vistas[q.especialidad] = 1; qs.push(q); } });

        /* teléfono central: una pregunta se responde sola, con toque y comentario, y pasa a la siguiente */
        var P = document.getElementById("phPregunta"), k = 0;
        P.innerHTML = LOGO + '<div class="ph__bar"><span id="phArea"></span><span><b id="phN">1</b>/3</span></div><p class="ph__stem" id="phStem"></p><ul class="ph__ops" id="phOps"></ul><div class="ph__why" id="phWhy"></div><span class="ph__chip" id="phChip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2.5" width="6" height="5" rx="1"/><rect x="3" y="16.5" width="6" height="5" rx="1"/><rect x="15" y="16.5" width="6" height="5" rx="1"/><path d="M12 7.5v4M6 16.5V14h12v2.5M12 11.5V14"/></svg>Ver flujograma</span><span class="ph__toque" id="phToque"></span>';
        function ver(q) {
          document.getElementById("phArea").textContent = q.especialidad; document.getElementById("phN").textContent = String((k % 3) + 1);
          document.getElementById("phStem").textContent = rec(q.enunciado, 150);
          document.getElementById("phOps").innerHTML = q.opciones.slice(0, 4).map(function (o) { return '<li data-l="' + esc(o.letra) + '"><b>' + esc(o.letra) + '</b><span>' + esc(rec(o.texto, 44)) + '</span></li>'; }).join("");
          var w = document.getElementById("phWhy"); w.className = "ph__why"; w.innerHTML = '<b>Comentario docente</b>' + esc(rec(q.comentario, 110));
          document.getElementById("phChip").className = "ph__chip"; P.classList.remove("is-in"); void P.offsetWidth; P.classList.add("is-in");
        }
        function ciclo() {
          var q = qs[k % 3]; ver(q);
          if (reducido) { var o0 = document.querySelector('#phOps [data-l="' + q.clave + '"]'); if (o0) o0.classList.add("is-ok"); document.getElementById("phWhy").classList.add("is-on"); return; }
          esp(function () {
            var op = document.querySelector('#phOps [data-l="' + q.clave + '"]'); if (!op) return;
            var rp = op.getBoundingClientRect(), rc = P.getBoundingClientRect(), tq = document.getElementById("phToque");
            tq.style.left = (rp.left - rc.left + rp.width * 0.7) + "px"; tq.style.top = (rp.top - rc.top + rp.height * 0.5) + "px"; tq.className = "ph__toque is-on";
            esp(function () { op.classList.add("is-ok"); tq.className = "ph__toque"; esp(function () { document.getElementById("phWhy").classList.add("is-on"); esp(function () { document.getElementById("phChip").classList.add("is-on"); esp(function () { k++; ciclo(); }, 3400); }, 900); }, 450); }, 650);
          }, 1500);
        }
        ciclo();

        /* teléfono izquierdo: las especialidades reales con su tamaño, desplazándose */
        var conteo = {}; d.preguntas.forEach(function (p) { conteo[p.archivo] = (conteo[p.archivo] || 0) + 1; });
        var lista = MQP.especialidades.filter(function (e) { return conteo[e.archivo]; }).map(function (e) { return { e: e, n: conteo[e.archivo] }; }).sort(function (a, b) { return b.n - a.n; });
        var max = lista[0].n, fila = function (t) { return '<li><span class="ph__ico">' + MQP.icono(t.e.icono) + '</span><span class="ph__nom">' + esc(t.e.nombre) + '<i><u style="--w:' + Math.round(t.n / max * 100) + '%"></u></i></span><small>' + miles(t.n) + '</small></li>'; };
        document.getElementById("phEsp").innerHTML = LOGO + '<div class="ph__bar"><span>Banco ENAM</span><span>' + miles(d.preguntas.length) + ' preguntas</span></div><p class="ph__tit">Especialidades</p><div class="ph__busca"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><span>Buscar especialidad…</span></div><div class="ph__scroll"><ul class="ph__esp ph__esp--mov">' + lista.map(fila).join("") + lista.map(fila).join("") + '</ul></div>';

        /* teléfono derecho: el flujograma real, con zoom y desplazamiento continuos */
        document.getElementById("phFlujo").innerHTML = LOGO + '<div class="ph__bar"><span>Flujograma clínico</span><span class="ph__zoom"><b>−</b><b class="ph__mas">+</b></span></div><div class="ph__vista"><img class="ph__img" alt="" loading="lazy" src="' + esc(base + algos[qs[0].id].imagen) + '"></div><p class="ph__pie">Toca para acercar · arrastra para moverte</p>';
      }, function () { box.parentNode.hidden = true; });
    }
    if ("IntersectionObserver" in window) { var io = new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) pintar(); box.classList.toggle("is-activo", visible); }, { rootMargin: "200px 0px" }); io.observe(box); } else { pintar(); box.classList.add("is-activo"); }
  }

  /* ---------------------------------------------------------------- hero: un "estudiante" resuelve 4 preguntas reales en la pantalla */
  function heroPantalla() {
    var app = document.getElementById("hsApp"); if (!app || !window.MQP || !MQP.cargarTodo) return;
    var reducido = false; try { reducido = matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
    if (reducido) return;                                    // sin movimiento: se queda la pregunta estática del HTML
    var $ = function (id) { return document.getElementById(id); };
    var cuerpo = $("hsCuerpo"), elN = $("hsN"), elArea = $("hsArea"), elStem = $("hsStem"), elOps = $("hsOps"), elFb = $("hsFb"), elImg = $("hsImg"), elPill = $("hsPill");
    var flujo = $("hsFlujo"), vista = $("hsVista"), imgF = $("hsFlujoImg"), res = $("hsRes"), cur = $("hsCursor");
    var pool = [], activo = false, enPantalla = true, hayData = false;
    function rec(t, n) { t = String(t); return t.length > n ? t.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : t; }

    /* pausa el guion cuando la pestaña o el hero no se ven */
    var pausado = function () { return document.hidden || !enPantalla; }, reanudar = [];
    function pasar() { return new Promise(function (ok) { if (!pausado()) return ok(); reanudar.push(ok); }); }
    function liberar() { if (pausado()) return; var l = reanudar; reanudar = []; l.forEach(function (f) { f(); }); }
    document.addEventListener("visibilitychange", liberar);
    if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { enPantalla = e[0].isIntersecting; liberar(); }).observe(app);
    function esp(ms) { return new Promise(function (ok) { setTimeout(ok, ms); }).then(pasar); }

    /* cursor */
    function pos(el, dx, dy) {
      var r = el.getBoundingClientRect(), a = app.getBoundingClientRect();
      return { x: r.left - a.left + (dx == null ? r.width * 0.5 : dx), y: r.top - a.top + (dy == null ? r.height * 0.55 : dy) };
    }
    function ir(el, dx, dy, ms) { if (!el) return esp(ms || 300); var p = pos(el, dx, dy); cur.style.transitionDuration = (ms || 1000) + "ms"; cur.style.left = p.x + "px"; cur.style.top = p.y + "px"; return esp((ms || 1000) + 80); }
    function clic() { cur.classList.add("is-click"); return esp(260).then(function () { cur.classList.remove("is-click"); }); }
    function setCursorInicio() { cur.style.transitionDuration = "0ms"; cur.style.left = app.clientWidth * 0.82 + "px"; cur.style.top = app.clientHeight * 0.92 + "px"; cur.classList.add("is-on"); }

    function mostrar(q, n) {
      cuerpo.classList.remove("is-in"); void cuerpo.offsetWidth; cuerpo.classList.add("is-in");
      elN.textContent = String(n + 1);
      elArea.textContent = q.especialidad + " · " + (q.examen.replace(/\s*·.*$/, "") || "ENAM");
      elStem.textContent = rec(q.enunciado, 200);
      elOps.innerHTML = q.opciones.slice(0, 4).map(function (o) { return '<li data-l="' + esc(o.letra) + '"><b>' + esc(o.letra) + '</b><span>' + esc(rec(o.texto, 60)) + '</span></li>'; }).join("");
      elFb.hidden = true; elFb.innerHTML = ""; elFb.className = "mapp__fb";
      if (q.imagen) { elImg.src = q.imagen; elImg.hidden = false; }
    }
    function zoomar(z, x, y) { vista.style.setProperty("--z", z); vista.style.setProperty("--tx", x + "%"); vista.style.setProperty("--ty", y + "%"); }

    /* el flujograma de una pregunta fallada: se abre, se acerca, se mueve y se cierra */
    function verFlujo(q) {
      imgF.src = q.imagen; zoomar(1, 0, 0);
      flujo.hidden = false; void flujo.offsetWidth; flujo.classList.add("is-in");
      return esp(900)
        .then(function () { return ir($("hsMas"), null, null, 1100); }).then(clic).then(function () { zoomar(1.8, -6, -4); return esp(900); })
        .then(function () { return clic(); }).then(function () { zoomar(2.6, -16, -10); return esp(1000); })
        .then(function () { return ir(vista, vista.clientWidth * 0.62, vista.clientHeight * 0.55, 1000); })
        .then(function () { cur.classList.add("is-drag"); zoomar(2.6, -30, -18); cur.style.transitionDuration = "1300ms"; var p = pos(vista, vista.clientWidth * 0.34, vista.clientHeight * 0.38); cur.style.left = p.x + "px"; cur.style.top = p.y + "px"; return esp(1500); })
        .then(function () { cur.classList.remove("is-drag"); return esp(500); })
        .then(function () { return ir($("hsMenos"), null, null, 1000); }).then(clic).then(function () { zoomar(1.8, -6, -4); return esp(600); })
        .then(function () { return clic(); }).then(function () { zoomar(1, 0, 0); return esp(700); })
        .then(function () { return ir($("hsSeguir"), null, null, 900); }).then(clic)
        .then(function () { flujo.classList.remove("is-in"); return esp(350); })
        .then(function () { flujo.hidden = true; });
    }

    function pregunta(q, n, acierta) {
      mostrar(q, n);
      var ok = elOps.querySelector('[data-l="' + q.clave + '"]'), otras = [].filter.call(elOps.children, function (li) { return li !== ok; });
      var elegida = acierta ? ok : otras[0];
      return esp(1300).then(function () { return ir(elegida, 60, null, 1300); })
        .then(clic).then(function () {
          elegida.classList.add(acierta ? "is-sel" : "is-mal");
          return esp(700);
        }).then(function () {
          ok.classList.add("is-ok");
          elFb.innerHTML = '<b>' + (acierta ? "Correcto" : "Incorrecto") + '</b> · Comentario docente: ' + esc(rec(q.comentario, 110)) +
            '<span class="mapp__verflujo" id="hsVerFlujo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2.5" width="6" height="5" rx="1"/><rect x="3" y="16.5" width="6" height="5" rx="1"/><rect x="15" y="16.5" width="6" height="5" rx="1"/><path d="M12 7.5v4M6 16.5V14h12v2.5M12 11.5V14"/></svg>Ver algoritmo / Flujograma</span>';
          elFb.className = "mapp__fb " + (acierta ? "is-ok" : "is-mal"); elFb.hidden = false;
          return esp(acierta ? 2400 : 1500);
        }).then(function () {
          if (acierta) return null;
          var btn = $("hsVerFlujo");                              // el cursor pulsa "Ver algoritmo / Flujograma", igual que en el banco
          return ir(btn, null, null, 1100).then(function () { btn.classList.add("is-pulsado"); return clic(); }).then(function () { return esp(250); }).then(function () { return verFlujo(q); });
        });
    }

    function resultados(lista) {
      var ok = lista.filter(function (r) { return r.ok; }).length, filas = lista.map(function (r) { return { etiqueta: r.esp, valor: r.ok ? 100 : 0, max: 100, texto: r.ok ? "100%" : "0%", sub: r.ok ? "1 de 1" : "0 de 1" }; }).sort(function (a, b) { return a.valor - b.valor; });
      res.innerHTML = '<p class="mr__tit">Resultado de la sesión</p><div class="mr__fila">' + donut(ok, lista.length - ok, { titulo: "Resultado" }) +
        '<dl class="mr__kpis"><div><dt>Correctas</dt><dd>' + ok + ' / ' + lista.length + '</dd></div><div><dt>Incorrectas</dt><dd>' + (lista.length - ok) + '</dd></div></dl></div>' + barras(filas, {});
      res.hidden = false; void res.offsetWidth; res.classList.add("is-in");
      return esp(6500).then(function () { res.classList.remove("is-in"); return esp(400); }).then(function () { res.hidden = true; });
    }

    function sortear() {
      var c = pool.slice(), t, r, j; for (j = c.length - 1; j > 0; j--) { r = Math.floor(Math.random() * (j + 1)); t = c[j]; c[j] = c[r]; c[r] = t; }
      var v = {}, e = []; c.forEach(function (q) { if (e.length < 4 && !v[q.especialidad]) { v[q.especialidad] = 1; e.push(q); } });
      return e;
    }
    function guion() {
      var qs = sortear(), lista = [], n = 0, pat = [true, false, true, false];    // 2 correctas y 2 incorrectas, intercaladas
      if (qs.length < 4) return;
      function paso() {
        if (n >= 4) { return esp(400).then(function () { return resultados(lista); }).then(function () { return esp(500).then(guion); }); }
        var i = n++; return pregunta(qs[i], i, pat[i]).then(function () { lista.push({ esp: qs[i].especialidad, ok: pat[i] }); return paso(); });
      }
      setCursorInicio(); paso();
    }
    function iniciar() {
      MQP.cargarTodo().then(function (d) {
        var algos = window.MQP_ALGORITMOS || {}, base = MQP.base || "";
        pool = d.preguntas.filter(function (q) { var a = algos[q.id]; return q.comentario && q.comentario.length > 50 && q.enunciado.length <= 220 && q.opciones.length >= 4 && a && a.imagen && q.clave; });
        pool.forEach(function (q) { q.imagen = base + algos[q.id].imagen; });
        if (pool.length < 8) return;
        app.style.setProperty("--top-h", $("hsTop").offsetHeight + "px");
        elPill.textContent = "Banco de preguntas"; $("hsT").textContent = "4";
        guion();
      }, function () {});
    }
    setTimeout(iniciar, 400);
  }
  function iniciarPublico() { bancoEnVivo(); celulares(); heroPantalla(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciarPublico); else iniciarPublico();

  window.MQP_GRAF = { donut: donut, linea: linea, barras: barras, columnas: columnas, calor: calor, iniciarTips: iniciarTips };
})();
