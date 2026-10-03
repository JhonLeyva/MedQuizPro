/* MedQuizPlus · Feedback clínico visual post-pregunta
 *
 * Uso desde la plataforma:
 *   MQPFeedback.render(contenedor, tarjeta, { seleccion: "C", modo: "learn" })
 *     seleccion: letra elegida por el estudiante (null si no se conoce)
 *     modo: "quick" (Explicación rápida) | "learn" (Aprender) | "check" (Comprobar)
 *
 * Las tarjetas se registran con MQPFeedback.register({...}); el esquema está en README.md.
 */
(function () {
  "use strict";

  var MODES = [
    { id: "quick", label: "⚡ Explicación rápida" },
    { id: "learn", label: "📖 Aprender" },
    { id: "check", label: "🔄 Comprobar" }
  ];

  var PISTA_TIPOS = {
    decisivo: { icon: "🔥", label: "Dato decisivo" },
    gravedad: { icon: "⚠️", label: "Dato de gravedad" },
    contexto: { icon: "🟡", label: "Dato de contexto" },
    descarta: { icon: "🧩", label: "Descarta otras opciones" }
  };

  var cards = [];

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  // Marcado mínimo en los datos: **negrita** y ✎ (complemento editorial pendiente de revisión).
  function fmt(s) {
    return esc(s)
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/✎/g, '<span class="ed" title="Complemento editorial: no está en el comentario fuente, pendiente de revisión médica">✎</span>');
  }

  function vignette(card) {
    var tipoDe = {};
    card.pistas.forEach(function (p) { if (!tipoDe[p.k]) tipoDe[p.k] = p.tipo; });
    return esc(card.enunciado).replace(/\{\{(\w+)\|(.+?)\}\}/g, function (_, k, txt) {
      return '<mark class="pk t-' + (tipoDe[k] || "contexto") + '" data-k="' + k + '">' + txt + "</mark>";
    });
  }

  function alt(card, letra) {
    for (var i = 0; i < card.alternativas.length; i++) if (card.alternativas[i].letra === letra) return card.alternativas[i];
    return null;
  }

  function sec(id, modes, inner, extra) {
    return '<section class="sec s-' + id + '" data-modes="' + modes + '"' + (extra || "") + ">" + inner + "</section>";
  }
  function conceal(prompt, body) {
    return '<div class="cz"><button type="button" class="cz-btn">' + esc(prompt) + '</button><div class="cz-body">' + body + "</div></div>";
  }

  /* ---------- Secciones ---------- */

  function sPregunta(card, st) {
    var correcta = card.correcta;
    var lis = card.alternativas.map(function (a) {
      var cls = "", tags = "";
      if (a.letra === correcta) { cls = "is-correct"; tags += '<span class="tag ok">Correcta</span>'; }
      if (st.sel && a.letra === st.sel) {
        if (a.letra !== correcta) cls = "is-wrong";
        tags = '<span class="tag ' + (a.letra === correcta ? "ok" : "bad") + '">Tu respuesta</span>' + tags;
      }
      return '<li class="' + cls + '"><span class="l">' + a.letra + "</span><span>" + esc(a.texto) + '</span><span class="tags">' + tags + "</span></li>";
    }).join("");
    return sec("pregunta", "quick learn check",
      '<h3>La pregunta que acabas de responder <small>' + esc(card.examen) + " · Pregunta " + card.numero + "</small></h3>" +
      '<p class="vignette">' + vignette(card) + "</p>" +
      '<ol class="alts">' + lis + "</ol>");
  }

  function sResultado(card, st) {
    var c = alt(card, card.correcta);
    var html;
    if (!st.sel) {
      html = '<div class="result none"><div class="result-top"><span class="result-status">Respuesta correcta: ' + c.letra + ". " + esc(c.texto) + "</span></div>" +
        "<p>" + fmt(card.porQueCorrecta.resumen) + "</p></div>";
    } else if (st.sel === card.correcta) {
      html = '<div class="result ok"><div class="result-top"><span class="result-status">🟢 Correcta</span>' +
        '<span class="result-ans">Tu respuesta <b>' + c.letra + ". " + esc(c.texto) + "</b></span></div>" +
        "<p>" + fmt(card.porQueCorrecta.resumen) + "</p>" +
        '<p class="muted">Acertaste. Comprueba que fue por la razón correcta: ' + fmt(card.aciertoClave) + "</p></div>";
    } else {
      var s = alt(card, st.sel);
      html = '<div class="result bad"><div class="result-top"><span class="result-status">🔴 Incorrecta</span>' +
        '<span class="result-ans">Tu respuesta <b>' + s.letra + ". " + esc(s.texto) + "</b></span>" +
        '<span class="result-ans">Respuesta correcta <b>' + c.letra + ". " + esc(c.texto) + "</b></span></div>" +
        "<p>" + fmt(card.porQueCorrecta.resumen) + "</p></div>";
    }
    return sec("resultado", "quick learn check", html);
  }

  function sError(card, st) {
    if (!st.sel || st.sel === card.correcta) return "";
    var a = alt(card, st.sel);
    if (!a || !a.error) return "";
    // inferido=false: no hay base para suponer el razonamiento del estudiante; se explica la alternativa.
    var lead = a.error.inferido ? "🔴 ¿Dónde estuvo el error?" : "🔴 Esta alternativa no es correcta porque…";
    return sec("error", "quick learn check",
      '<div class="errbox"><span class="lead">' + lead + "</span><p>" + fmt(a.error.texto) + "</p></div>");
  }

  function sEvalua(card) {
    return sec("evalua", "learn check",
      "<h3>🎯 ¿Qué evaluaba?</h3><div class=\"chips\">" +
      card.evalua.map(function (e) { return '<span class="chip">' + esc(e) + "</span>"; }).join("") + "</div>");
  }

  function sPistas(card, st) {
    var items = card.pistas.map(function (p) {
      var t = PISTA_TIPOS[p.tipo];
      var onlyLearn = p.tipo === "decisivo" ? "" : ' data-modes="learn check"';
      return '<li class="pista t-' + p.tipo + '" data-k="' + p.k + '"' + onlyLearn + '><span class="kind">' + t.icon + " " + esc(p.etiqueta || t.label) + "</span>" +
        '<span class="dato">' + fmt(p.dato) + '</span><span class="sig">' + fmt(p.significa) + "</span></li>";
    }).join("");
    var legend = '<div class="legend" data-modes="learn check">' +
      '<span><i style="background:var(--warn)"></i>Decisivo</span><span><i style="background:var(--bad)"></i>Gravedad</span>' +
      '<span><i style="background:var(--info)"></i>Contexto</span><span><i style="background:var(--cls)"></i>Descarta opciones</span>' +
      "<span>Los datos están resaltados en la pregunta. Pasa el cursor por una pista para ubicarla.</span></div>";
    var body = '<ul class="pistas">' + items + "</ul>" + legend;
    return sec("pistas", "quick learn check",
      "<h3>🔑 Las pistas que debías reconocer</h3>" +
      conceal("Antes de mirar: ¿qué dato de la viñeta decide la respuesta? Piénsalo y toca para ver las pistas.", body));
  }

  function sRazonamiento(card) {
    var r = card.razonamiento;
    var chain = '<ol class="chain" data-modes="learn check">' + r.pasos.map(function (p) {
      return '<li><span class="q">' + esc(p.q) + '</span><span class="a">' + fmt(p.a) + "</span></li>";
    }).join("") + "</ol>";
    var rule = '<div class="rule"><div><b>Si veo</b><span>' + fmt(r.regla.veo) + "</span></div><div><b>Pienso</b><span>" +
      fmt(r.regla.pienso) + "</span></div><div><b>Hago</b><span>" + fmt(r.regla.hago) + "</span></div></div>";
    return sec("razonamiento", "quick learn check",
      "<h3>🧠 Razonamiento clínico <small>" + esc(r.ruta) + "</small></h3>" +
      conceal("Razónalo tú: ¿qué tiene, qué tan grave es y qué dato decide? Toca para comparar.", chain + rule));
  }

  /* ---------- Algoritmo (SVG generado desde los datos) ---------- */

  var G = { W: 760, top: 30, rowH: 112, evX: 196, cols: [340, 620], rectW: [210, 200], dW: 230, dH: 84 };

  function nodeBox(n) {
    var cx = G.cols[n.col], cy = G.top + 42 + n.row * G.rowH;
    if (n.kind === "decision") return { cx: cx, cy: cy, w: G.dW, h: G.dH };
    var h = 26 + 16 * n.lines.length;
    return { cx: cx, cy: cy, w: G.rectW[n.col], h: h };
  }

  function algoSVG(card, st, uid) {
    var a = card.algoritmo, byId = {}, maxRow = 0;
    a.nodes.forEach(function (n) { byId[n.id] = n; n._b = nodeBox(n); if (n.row > maxRow) maxRow = n.row; });
    var H = G.top + 42 + maxRow * G.rowH + 42 + 20;
    var out = [];
    out.push('<svg viewBox="0 0 ' + G.W + " " + H + '" role="img" aria-label="Algoritmo con la ruta del paciente resaltada">');
    out.push("<defs>" + ["mut", "ok", "line"].map(function (k) {
      return '<marker id="' + uid + "-a-" + k + '" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path class="arrow-' + k + '" d="M0,0 L10,5 L0,10 z"/></marker>';
    }).join("") + "</defs>");
    out.push('<text class="lane" x="' + G.evX + '" y="16" text-anchor="end">ESTE PACIENTE</text>');

    // Aristas
    a.edges.forEach(function (e) {
      var s = byId[e.from]._b, t = byId[e.to]._b, d, lx, ly, anchor;
      if (byId[e.from].col === byId[e.to].col) {
        var y1 = s.cy + s.h / 2, y2 = t.cy - t.h / 2 - 2;
        d = "M" + s.cx + "," + y1 + " L" + t.cx + "," + y2;
        lx = s.cx + 10; ly = (y1 + y2) / 2 + 4; anchor = "start";
      } else {
        var x1 = s.cx + s.w / 2, x2 = t.cx - t.w / 2 - 2;
        d = "M" + x1 + "," + s.cy + " L" + x2 + "," + t.cy;
        lx = (x1 + x2) / 2; ly = s.cy - 8; anchor = "middle";
      }
      var m = e.ruta ? "mut" : "line";
      out.push('<g class="edge' + (e.ruta ? " e-route" : "") + '" data-to="' + e.to + '">' +
        '<path class="e-line" d="' + d + '" marker-end="url(#' + uid + "-a-" + m + ')"/>' +
        '<text class="e-label" x="' + lx + '" y="' + ly + '" text-anchor="' + anchor + '">' + esc(e.label) + "</text></g>");
    });

    // Nodos
    a.nodes.forEach(function (n) {
      var b = n._b, shape;
      if (n.kind === "decision") {
        shape = '<polygon class="n-shape" points="' + b.cx + "," + (b.cy - b.h / 2) + " " + (b.cx + b.w / 2) + "," + b.cy + " " + b.cx + "," + (b.cy + b.h / 2) + " " + (b.cx - b.w / 2) + "," + b.cy + '"/>';
      } else {
        var rx = n.kind === "start" ? b.h / 2 : 7;
        shape = '<rect class="n-shape" x="' + (b.cx - b.w / 2) + '" y="' + (b.cy - b.h / 2) + '" width="' + b.w + '" height="' + b.h + '" rx="' + rx + '"/>';
      }
      var fs = n.kind === "decision" ? 12.5 : 13, lh = n.kind === "decision" ? 15 : 16;
      var y0 = b.cy - ((n.lines.length - 1) * lh) / 2 + 4.5;
      var txt = '<text class="n-text" text-anchor="middle" style="font-size:' + fs + 'px">' + n.lines.map(function (l, i) {
        return '<tspan x="' + b.cx + '" y="' + (y0 + i * lh) + '">' + esc(l) + "</tspan>";
      }).join("") + "</text>";

      var ev = "";
      if (n.evidencia) {
        var left = b.cx - b.w / 2;
        var ey0 = b.cy - ((n.evidencia.length - 1) * 15) / 2 + 4;
        ev = '<line class="ev-line" x1="' + (G.evX + 4) + '" y1="' + b.cy + '" x2="' + (left - 4) + '" y2="' + b.cy + '"/>' +
          '<text class="ev-text" text-anchor="end">' + n.evidencia.map(function (l, i) {
            return '<tspan x="' + G.evX + '" y="' + (ey0 + i * 15) + '">' + esc(l) + "</tspan>";
          }).join("") + "</text>";
      }

      var nOp = (n.opciones || []).length;
      var badges = (n.opciones || []).map(function (L, i) {
        var cls = L === card.correcta ? "correct" : (st.sel === L ? "wrong" : "");
        var bx = b.cx + b.w / 2 - 6 - (nOp - 1 - i) * 26, by = b.cy - b.h / 2 + 2;
        if (n.kind === "decision") { bx = b.cx + 30 + i * 26; by = b.cy - b.h / 2 + 8; }
        return '<g class="badge ' + cls + '"><title>Opción ' + L + (st.sel === L ? " (tu respuesta)" : "") + '</title><circle cx="' + bx + '" cy="' + by + '" r="11"/><text x="' + bx + '" y="' + (by + 4) + '" text-anchor="middle">' + L + "</text></g>";
      }).join("");

      out.push('<g class="node k-' + n.kind + (n.ruta ? " is-route" : "") + (n.final ? " final" : "") + '" data-id="' + n.id + '">' + ev + shape + txt + badges + "</g>");
    });
    out.push("</svg>");
    return out.join("");
  }

  function sAlgoritmo(card, st, uid) {
    var opcionesEnAlgo = {};
    card.algoritmo.nodes.forEach(function (n) { (n.opciones || []).forEach(function (L) { opcionesEnAlgo[L] = 1; }); });
    var wrongInAlgo = st.sel && st.sel !== card.correcta && opcionesEnAlgo[st.sel];
    return sec("algoritmo", "learn check",
      '<h3>🗺️ Ruta del paciente en el algoritmo <small>' + esc(card.algoritmo.titulo) + "</small></h3>" +
      '<div class="algo-bar"><div class="algo-legend"><span><span class="swatch"></span>Ruta de este paciente</span>' +
      '<span><span class="dot ok">' + card.correcta + "</span>Respuesta correcta</span>" +
      (wrongInAlgo ? '<span><span class="dot bad">' + st.sel + "</span>A dónde lleva tu respuesta</span>" : "") +
      '<span><span class="dot mut">·</span>Dónde serían correctas las otras opciones</span></div>' +
      '<button type="button" class="btn primary algo-play"></button></div>' +
      '<div class="algo-scroll">' + algoSVG(card, st, uid) + "</div>" +
      (card.algoritmo.nota ? '<p class="muted">' + fmt(card.algoritmo.nota) + "</p>" : ""));
  }

  function sCorrecta(card) {
    var c = alt(card, card.correcta);
    return sec("correcta", "learn check",
      "<h3>✅ ¿Por qué " + c.letra + " es la correcta?</h3>" +
      conceal("Explícalo con tus palabras y toca para comparar.", "<p>" + fmt(card.porQueCorrecta.texto) + "</p>"));
  }

  function sOtras(card, st) {
    var lis = card.alternativas.map(function (a) {
      var cls = a.letra === card.correcta ? "is-correct" : (a.letra === st.sel ? "is-chosen" : "");
      var you = a.letra === st.sel ? '<span class="youtag">Tu respuesta</span>' : "";
      var reason = a.letra === card.correcta ? "<span>🟢 <strong>Correcta.</strong> " + fmt(a.porQue) + "</span>" : "<span>" + fmt(a.porQue) + "</span>";
      return '<li class="' + cls + '"><span class="l alts-l"><span class="dot ' + (a.letra === card.correcta ? "ok" : (a.letra === st.sel ? "bad" : "mut")) + '">' + a.letra + "</span></span>" +
        '<span class="opt">' + esc(a.texto) + you + '</span><span class="rsn">' + conceal("¿Por qué sí o por qué no? Toca para comprobar.", reason) + "</span></li>";
    }).join("");
    return sec("otras", "learn check", "<h3>❌ ¿Por qué no las otras?</h3><ul class=\"why\">" + lis + "</ul>");
  }

  function sTrampas(card) {
    if (!card.trampas || !card.trampas.length) return "";
    return sec("trampas", "learn", "<h3>⚠️ Trampa frecuente</h3><div class=\"trap\">" +
      card.trampas.map(function (t) { return "<div>" + fmt(t) + "</div>"; }).join("") + "</div>");
  }

  function sNoConfundir(card) {
    var n = card.noConfundir;
    if (!n) return "";
    var head = "<thead><tr><th></th>" + n.columnas.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead>";
    var body = "<tbody>" + n.filas.map(function (f) {
      return '<tr class="' + (f.esEste ? "this" : "") + '"><th>' + esc(f.dx) + "</th>" + f.celdas.map(function (c) { return "<td>" + fmt(c) + "</td>"; }).join("") + "</tr>";
    }).join("") + "</tbody>";
    return sec("noconfundir", "learn",
      '<details class="more"><summary>⚠️ No confundir con… ' + esc(n.titulo) + '</summary><div class="body"><div class="tbl-scroll"><table class="cmp">' + head + body + "</table></div>" +
      (n.nota ? '<p class="muted">' + fmt(n.nota) + "</p>" : "") + "</div></details>");
  }

  function sYSi(card, st) {
    var y = card.ySi;
    if (!y) return "";
    var i = st.ysi || 0, v = y.variaciones[i];
    var chips = '<div class="whatif-chips">' + y.variaciones.map(function (vv, j) {
      return '<button type="button" data-ysi="' + j + '" aria-pressed="' + (j === i) + '">¿Y si… ' + esc(vv.chip) + "?</button>";
    }).join("") + "</div>";
    var pair = '<div class="whatif"><div><b class="lab">Caso original</b><span>' + fmt(y.original.dato) + '</span><span class="res">' + fmt(y.original.resultado) + "</span></div>" +
      '<div class="chg"><b class="lab">¿Y si…?</b><span>' + fmt(v.cambio) + '</span><span class="res">' + fmt(v.resultado) + "</span>" +
      (v.fuente ? '<span class="muted" style="font-size:.8125rem">' + fmt(v.fuente) + "</span>" : "") + "</div></div>";
    return sec("ysi", "learn check",
      "<h3>🧪 ¿Qué pasaría si cambiamos un dato?</h3>" + chips + pair +
      '<div class="governs"><b>Variable que gobierna el algoritmo:</b> ' + fmt(y.variable) + "</div>");
  }

  function sFisio(card) {
    var f = card.fisiopatologia;
    if (!f) return "";
    var fig = f.figura && FIGS[f.figura] ? '<figure class="fig" style="margin:0">' + FIGS[f.figura]() + "<figcaption>" + fmt(f.pie) + "</figcaption></figure>" : "";
    return sec("fisio", "learn",
      '<details class="more"><summary>🧬 ¿Por qué ocurre? ' + esc(f.titulo) + '</summary><div class="body">' +
      f.texto.map(function (t) { return "<p>" + fmt(t) + "</p>"; }).join("") + fig + "</div></details>");
  }

  function sRecuerda(card) {
    return sec("recuerda", "quick learn",
      "<h3>🎯 Si solo recuerdas 3 cosas…</h3><ol class=\"remember\">" +
      card.recuerda.map(function (r) { return "<li><span>" + fmt(r) + "</span></li>"; }).join("") + "</ol>");
  }

  function sComprueba(card, st) {
    var q = card.comprueba, ans = st.quiz;
    var opts = q.opciones.map(function (o) {
      var cls = "";
      if (ans) { if (o.letra === q.correcta) cls = "ok"; else if (o.letra === ans) cls = "bad"; }
      return '<button type="button" data-quiz="' + o.letra + '" class="' + cls + '"' + (ans ? " disabled" : "") + '><span class="l">' + o.letra + "</span><span>" + esc(o.texto) + "</span></button>";
    }).join("");
    var expl = ans ? '<div class="expl"><strong>' + (ans === q.correcta ? "🟢 Bien razonado." : "🔴 No exactamente. La respuesta es " + q.correcta + ".") + "</strong><p>" + fmt(q.explicacion) + '</p><div><button type="button" class="btn quiz-reset">Intentar de nuevo</button></div></div>' : "";
    return sec("comprueba", "learn check",
      "<h3>🔄 Compruébalo <small>Una variación del caso, no la misma pregunta</small></h3>" +
      '<div class="quiz"><p>' + fmt(q.pregunta) + '</p><div class="opts">' + opts + "</div>" + expl + "</div>");
  }

  function sFuentes(card) {
    var qa = card.qa.map(function (x) { return '<li class="' + (x.flag ? "flag" : "") + '">' + fmt(x.t) + "</li>"; }).join("");
    return sec("fuentes", "learn",
      '<details class="more"><summary>📚 Fuentes y control de calidad</summary><div class="body">' +
      '<div class="subhead">Fuentes</div><ul class="src">' + card.fuentes.map(function (f) { return "<li>" + fmt(f) + "</li>"; }).join("") + "</ul>" +
      '<p class="muted"><span class="ed" style="vertical-align:0;font-size:1em">✎</span> marca los complementos editoriales que no están en el comentario fuente. Deben pasar revisión médica antes de publicar.</p>' +
      '<div class="subhead">Marcado para revisión</div><ul class="flags">' + card.revision.map(function (r) { return "<li>" + fmt(r) + "</li>"; }).join("") + "</ul>" +
      '<div class="subhead">Checklist de calidad</div><ul class="qa">' + qa + "</ul></div></details>");
  }

  /* ---------- Figuras esquemáticas ---------- */

  var FIGS = {
    // Corte transversal del tórax: el segmento libre se mueve al revés que el resto de la pared.
    flail: function () {
      function panel(x0, title, inward) {
        var cx = x0 + 120, cy = 112, r = 70;
        var wall = '<path class="f-wall" d="M' + (cx + r * Math.cos(-2.2)) + "," + (cy + r * Math.sin(-2.2)) +
          " A" + r + "," + r + " 0 1,1 " + (cx + r * Math.cos(2.2)) + "," + (cy + r * Math.sin(2.2)) + '"/>';
        var p1 = [cx + r * Math.cos(-2.2), cy + r * Math.sin(-2.2)], p2 = [cx + r * Math.cos(2.2), cy + r * Math.sin(2.2)];
        var bulge = inward ? 34 : -22;
        var seg = '<path class="f-seg" d="M' + p1[0] + "," + p1[1] + " Q" + (cx - r + bulge) + "," + cy + " " + p2[0] + "," + p2[1] + '"/>';
        var ax = cx - r - (inward ? 26 : -2), dir = inward ? 1 : -1;
        var arrow = '<path class="f-arrow" d="M' + (ax + dir * 24) + "," + cy + " l" + (-dir * 10) + ",-7 l0,14 z\"/>" +
          '<line class="f-redline" x1="' + (ax - dir * 2) + '" y1="' + cy + '" x2="' + (ax + dir * 16) + '" y2="' + cy + '"/>';
        var outer = inward
          ? '<path class="f-arrow-mut" d="M' + (cx + r + 22) + "," + cy + ' l-10,-7 l0,14 z"/><line class="f-stroke" x1="' + (cx + r + 6) + '" y1="' + cy + '" x2="' + (cx + r + 14) + '" y2="' + cy + '"/>'
          : '<path class="f-arrow-mut" d="M' + (cx + r + 4) + "," + cy + ' l10,-7 l0,14 z"/><line class="f-stroke" x1="' + (cx + r + 12) + '" y1="' + cy + '" x2="' + (cx + r + 22) + '" y2="' + cy + '"/>';
        return '<text class="f-ttl" x="' + cx + '" y="20" text-anchor="middle">' + title + "</text>" + wall + seg + arrow + outer +
          '<text class="f-txt" x="' + cx + '" y="206" text-anchor="middle">' + (inward ? "El segmento se hunde" : "El segmento protruye") + "</text>";
      }
      return '<svg viewBox="0 0 520 220" role="img" aria-label="Movimiento paradójico del tórax inestable">' +
        panel(0, "INSPIRACIÓN", true) + panel(270, "ESPIRACIÓN", false) + "</svg>";
    },
    // Útero esquemático: DPP (hematoma retroplacentario oculto) frente a placenta previa.
    dpp: function () {
      function uterus(x0) {
        return '<path class="f-uterus" d="M' + (x0 + 110) + ",40 C" + (x0 + 30) + ",40 " + (x0 + 20) + ",120 " + (x0 + 60) + ",168 C" +
          (x0 + 78) + ",188 " + (x0 + 96) + ",192 " + (x0 + 100) + ",206 L" + (x0 + 120) + ",206 C" + (x0 + 124) + ",192 " + (x0 + 142) + ",188 " +
          (x0 + 160) + ",168 C" + (x0 + 200) + ",120 " + (x0 + 190) + ",40 " + (x0 + 110) + ',40 Z"/>';
      }
      var a = 0, b = 270;
      return '<svg viewBox="0 0 520 268" role="img" aria-label="Desprendimiento prematuro de placenta frente a placenta previa">' +
        '<text class="f-ttl" x="' + (a + 110) + '" y="22" text-anchor="middle">DPP</text>' + uterus(a) +
        '<path class="f-hema" d="M' + (a + 76) + ",58 Q" + (a + 110) + ",44 " + (a + 144) + ",58 Q" + (a + 110) + ',74 ' + (a + 76) + ',58 Z"/>' +
        '<path class="f-plac" d="M' + (a + 62) + ",70 Q" + (a + 110) + ",58 " + (a + 158) + ",70 Q" + (a + 110) + ',100 ' + (a + 62) + ',70 Z"/>' +
        '<circle class="f-red" cx="' + (a + 110) + '" cy="218" r="3"/>' +
        '<text class="f-txt" text-anchor="middle"><tspan x="' + (a + 110) + '" y="238">Sangre retenida tras la placenta:</tspan><tspan x="' + (a + 110) + '" y="254">poco sangrado externo</tspan></text>' +
        '<text class="f-ttl" x="' + (b + 110) + '" y="22" text-anchor="middle">PLACENTA PREVIA</text>' + uterus(b) +
        '<path class="f-plac" d="M' + (b + 70) + ",150 Q" + (b + 110) + ",215 " + (b + 150) + ",150 Q" + (b + 110) + ',172 ' + (b + 70) + ',150 Z"/>' +
        '<circle class="f-red" cx="' + (b + 104) + '" cy="216" r="4"/><circle class="f-red" cx="' + (b + 116) + '" cy="224" r="4"/>' +
        '<text class="f-txt" text-anchor="middle"><tspan x="' + (b + 110) + '" y="246">Placenta sobre el cuello:</tspan><tspan x="' + (b + 110) + '" y="262">sangrado indoloro</tspan></text></svg>';
    }
  };

  /* ---------- Render y comportamiento ---------- */

  var uidSeq = 0;

  function render(root, card, opts) {
    var st = { sel: (opts && opts.seleccion) || null, mode: (opts && opts.modo) || "learn", ysi: 0, quiz: null, step: 0 };
    var uid = "mqp" + (++uidSeq);

    function draw() {
      var head = '<header class="fb-head"><div class="fb-kicker">' + esc(card.especialidad) + " · " + esc(card.tema) + "</div>" +
        "<h2>🩺 ¿Por qué esta era la respuesta?</h2>" +
        '<div class="modes" role="group" aria-label="Modo de visualización">' + MODES.map(function (m) {
          return '<button type="button" data-mode="' + m.id + '" aria-pressed="' + (st.mode === m.id) + '">' + m.label + "</button>";
        }).join("") + "</div></header>";
      root.innerHTML = '<article class="fb mode-' + st.mode + '">' + head +
        sPregunta(card, st) + sResultado(card, st) + sError(card, st) + sEvalua(card) + sPistas(card, st) +
        sRazonamiento(card) + sAlgoritmo(card, st, uid) + sCorrecta(card) + sOtras(card, st) + sTrampas(card) +
        sNoConfundir(card) + sYSi(card, st) + sFisio(card) + sRecuerda(card) + sComprueba(card, st) + sFuentes(card) +
        "</article>";
      applyMode();
      initAlgo();
    }

    function applyMode() {
      root.querySelectorAll("[data-modes]").forEach(function (el) {
        el.hidden = el.getAttribute("data-modes").split(" ").indexOf(st.mode) < 0;
      });
    }

    // Secuencia de la ruta: arista de entrada + nodo, en orden de filas.
    function routeSeq() {
      var seq = [];
      card.algoritmo.nodes.filter(function (n) { return n.ruta; }).sort(function (a, b) { return a.row - b.row; }).forEach(function (n) {
        var e = root.querySelector('.edge.e-route[data-to="' + n.id + '"]');
        var g = root.querySelector('.node[data-id="' + n.id + '"]');
        seq.push([e, g].filter(Boolean));
      });
      return seq;
    }
    var timers = [];
    function setLit(k) {
      routeSeq().forEach(function (group, i) {
        group.forEach(function (el) {
          el.classList.toggle("lit", i < k);
          var line = el.querySelector(".e-line");
          if (line) line.setAttribute("marker-end", line.getAttribute("marker-end").replace(/-a-\w+\)/, i < k ? "-a-ok)" : "-a-mut)"));
        });
      });
    }
    function initAlgo() {
      var btn = root.querySelector(".algo-play");
      if (!btn) return;
      var total = routeSeq().length;
      if (st.mode === "check") {
        setLit(st.step);
        btn.textContent = st.step >= total ? "↺ Reiniciar la ruta" : (st.step === 0 ? "▶ ¿Por dónde empieza? Revela el primer paso" : "▶ ¿Qué sigue? Revela el siguiente paso");
      } else {
        setLit(total);
        btn.textContent = "▶ Recorrer la ruta del paciente";
      }
    }
    function playRoute() {
      timers.forEach(clearTimeout); timers = [];
      var total = routeSeq().length;
      var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (reduce) { setLit(total); return; }
      setLit(0);
      for (var i = 1; i <= total; i++) timers.push(setTimeout(setLit.bind(null, i), 120 + i * 480));
    }

    root.onclick = function (ev) {
      var t = ev.target.closest("button");
      if (!t || !root.contains(t)) return;
      if (t.dataset.mode) { st.mode = t.dataset.mode; st.step = 0; st.quiz = null; try { localStorage.setItem("mqp-mode", st.mode); } catch (e) {} draw(); return; }
      if (t.classList.contains("cz-btn")) {
        t.parentNode.classList.add("open");
        if (t.closest(".s-pistas")) root.querySelector(".fb").classList.add("pistas-shown");
        return;
      }
      if (t.classList.contains("algo-play")) {
        if (st.mode === "check") { var total = routeSeq().length; st.step = st.step >= total ? 0 : st.step + 1; initAlgo(); }
        else playRoute();
        return;
      }
      if (t.dataset.ysi) { st.ysi = +t.dataset.ysi; redrawKeepScroll(); return; }
      if (t.dataset.quiz) { st.quiz = t.dataset.quiz; redrawKeepScroll(); return; }
      if (t.classList.contains("quiz-reset")) { st.quiz = null; redrawKeepScroll(); return; }
    };
    // Redibuja sin perder lo que el estudiante ya desplegó.
    function redrawKeepScroll() {
      var open = [].map.call(root.querySelectorAll(".cz.open"), function (el) { return [].indexOf.call(root.querySelectorAll(".cz"), el); });
      var det = [].map.call(root.querySelectorAll("details"), function (d) { return d.open; });
      var pist = root.querySelector(".fb").classList.contains("pistas-shown");
      draw();
      var cz = root.querySelectorAll(".cz");
      open.forEach(function (i) { if (cz[i]) cz[i].classList.add("open"); });
      root.querySelectorAll("details").forEach(function (d, i) { d.open = !!det[i]; });
      if (pist) root.querySelector(".fb").classList.add("pistas-shown");
    }
    root.onmouseover = function (ev) {
      var p = ev.target.closest(".pista");
      root.querySelectorAll("mark.focus").forEach(function (m) { m.classList.remove("focus"); });
      if (p) root.querySelectorAll('mark.pk[data-k="' + p.dataset.k + '"]').forEach(function (m) { m.classList.add("focus"); });
    };

    draw();
    return {
      setSeleccion: function (L) { st.sel = L; st.quiz = null; draw(); },
      setModo: function (m) { st.mode = m; st.step = 0; draw(); }
    };
  }

  window.MQPFeedback = {
    register: function (card) { cards.push(card); },
    cards: function () { return cards.slice(); },
    figuras: FIGS,
    render: render
  };
})();
