/* MedQuizPlus · «Misión SERUMS: sobrevive a la posta». Interfaz de la estación (#/serums y #/serums/<caso>).
   La lógica vive en serums_nucleo.js (puro, sin DOM); los casos y el registro de evidencia están en serums_casos.js (generado) y el índice documental
   en serums/indice.json (se carga solo cuando el alumno consulta al supervisor). Simulación educativa con establecimiento y casos ficticios. */
(function (raiz) {
  "use strict";
  var M = raiz.MQP || (raiz.MQP = {});
  var N = function () { return M.serumsNucleo; }, GD = function () { return M.guardia; };
  var SRC = (document.currentScript && document.currentScript.src) || "", BASE = SRC.replace(/serums\.js(\?.*)?$/, ""), VER = (SRC.split("?")[1] || "");
  var K_POSTA = "mqp_serums_posta_v1", K_SES = "mqp_serums_sesion_v1", IMG = BASE + "guardia/portadas/serums.webp";
  var AVISO = "Simulación educativa. El establecimiento, los pacientes y los casos son ficticios. Las decisiones no sustituyen la norma vigente ni el criterio clínico supervisado. La fotografía de portada es una ilustración generada con IA.";
  var CALIDAD = { optima: "Decisión óptima", aceptable: "Aceptable, mejorable", incorrecta: "Incorrecta", peligrosa: "Peligrosa (error crítico)" };
  var TABS = [["paciente", "Paciente"], ["historia", "Historia"], ["examen", "Examen físico"], ["pruebas", "Pruebas"], ["inventario", "Inventario"], ["referencia", "Referencia"], ["normativa", "Normativa"], ["evolucion", "Evolución"]];
  var cargaDatos = null, cargaIndice = null, detener = null;

  function esc(s) { return GD().esc(s); }
  function cargarScript(n) { return new Promise(function (ok, mal) { var s = document.createElement("script"); s.src = BASE + n + (VER ? "?" + VER : ""); s.onload = ok; s.onerror = function () { mal(new Error(n)); }; document.head.appendChild(s); }); }
  function asegurarDatos() {
    if (raiz.MQP_SERUMS) return Promise.resolve();
    if (!cargaDatos) cargaDatos = cargarScript("serums_casos.js").catch(function (e) { cargaDatos = null; throw e; });
    return cargaDatos;
  }
  function cargarIndice() {
    if (!cargaIndice) cargaIndice = fetch(BASE + "serums/indice.json" + (VER ? "?" + VER : "")).then(function (r) { if (!r.ok) throw new Error("indice"); return r.json(); }).catch(function (e) { cargaIndice = null; throw e; });
    return cargaIndice;
  }
  function por(l, id) { for (var i = 0; i < l.length; i++) if (l[i].id === id) return l[i]; return null; }
  function reloj(min) { var h = Math.floor(min / 60), m = min % 60; return (h ? h + " h " : "") + m + " min"; }
  function seg(s) { s = Math.round(s); return Math.floor(s / 60) + " min " + (s % 60) + " s"; }

  /* ---------- persistencia ---------- */
  function leerJson(k) { try { return JSON.parse(GD().ls(k) || "null"); } catch (e) { return null; } }
  function posta() { var p = leerJson(K_POSTA); return N().establecimiento(p || {}); }
  function guardarPosta(est) { GD().ls(K_POSTA, JSON.stringify(est)); }
  function progreso() { var g = M.progreso && M.progreso.preferencia("serums"); return g && g.casos ? g : { casos: {}, intentos: [] }; }
  function guardarProgreso(p) { if (M.progreso) M.progreso.preferencia("serums", p); }
  function sesion(caso) { var s = leerJson(K_SES + ":" + caso); return s && s.v === 1 && s.caso === caso ? s : null; }

  /* ---------- introducción cinematográfica: tormenta en la sierra ----------
     Escena = foto + lienzo en las mismas coordenadas de la imagen (1672×941, «cover»). El lienzo anima: lluvia en dos capas, salpicaduras en los impermeables y en el camino,
     focos de la posta que suben y bajan de intensidad, y relámpagos. El audio (lluvia y truenos, 30 s) se repite sin cortes y los relámpagos siguen sus truenos.
     Con «reducir movimiento» solo se dibuja un fotograma estático. */
  var IW = 1672, IH = 941, FOCO_X = 0.62, CICLO = 30;
  var IMG_INTRO = BASE + "guardia/portadas/serums-intro.webp", AUDIO = BASE + "serums/audio/tormenta.mp3";
  var LUCES = [[1148, 437, 40, 1.0], [1232, 436, 40, 1.0], [1298, 452, 60, 1.2], [1373, 434, 40, 1.0], [1295, 374, 120, 0.7], [1612, 404, 46, 0.9], [1585, 412, 30, 0.7], [254, 571, 16, 0.8], [300, 567, 16, 0.8], [345, 563, 16, 0.8], [388, 559, 16, 0.8], [560, 205, 230, 0.55]];
  /* tipo: cerca = cae en primer plano (grande, ramificado, ilumina todo); medio = en las lomas del valle; lejos = en las cumbres del fondo (fino y tenue).
     Los instantes siguen a TRUENOS de tools/serums_audio.py: el relámpago llega antes del trueno (más antes cuanto más lejos cae). Separación entre rayos: de 4 a 5 s. */
  var RELAMPAGOS = [{ t: 4.15, x: 330, y0: 0, y1: 690, tipo: "cerca" }, { t: 8.5, x: 420, y0: 205, y1: 345, tipo: "lejos" }, { t: 13.65, x: 1000, y0: 0, y1: 470, tipo: "medio" }, { t: 17.4, x: 1190, y0: 25, y1: 215, tipo: "lejos" }, { t: 22.55, x: 1500, y0: 0, y1: 765, tipo: "cerca" }, { t: 26.65, x: 170, y0: 0, y1: 525, tipo: "medio" }];
  var TIPO_RAYO = { cerca: { ancho: 1.25, alfa: 1, velo: 0.38, ramas: true, brillo: 130 }, medio: { ancho: 0.85, alfa: 0.9, velo: 0.24, ramas: true, brillo: 70 }, lejos: { ancho: 0.5, alfa: 0.75, velo: 0.1, ramas: false, brillo: 34 } };
  var BANDERA = { x: 1444, y: 203, w: 76, h: 93, ax: 1432, bx: 1522 };   // paño de la bandera en la imagen (el asta queda fija)
  var PERSONAS = [[500, 465, 270, 400], [790, 520, 140, 250]];                                                   // x, y, ancho, alto en la imagen
  var CAMINO = [[560, 905], [1010, 905], [1390, 530], [1250, 505], [900, 745]];
  function dentro(p, poli) { var c = false; for (var i = 0, j = poli.length - 1; i < poli.length; j = i++) { var a = poli[i], b = poli[j]; if ((a[1] > p[1]) !== (b[1] > p[1]) && p[0] < (b[0] - a[0]) * (p[1] - a[1]) / (b[1] - a[1]) + a[0]) c = !c; } return c; }
  function azar(sem) { var s = sem >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }

  function sonidoTormenta() {
    var AC = raiz.AudioContext || raiz.webkitAudioContext, ctx = null, ganancia = null, fuente = null, buf = null, inicio = 0, mudo = false, vivo = true, cargando = null;
    function asegurar() {
      if (!AC) return Promise.reject(new Error("sin audio"));
      if (!ctx) { ctx = new AC(); ganancia = ctx.createGain(); ganancia.gain.value = 0; ganancia.connect(ctx.destination); }
      if (buf) return Promise.resolve();
      if (!cargando) cargando = fetch(AUDIO + (VER ? "?" + VER : "")).then(function (r) { if (!r.ok) throw new Error("audio"); return r.arrayBuffer(); }).then(function (b) { return new Promise(function (ok, mal) { ctx.decodeAudioData(b, ok, mal); }); }).then(function (b) { buf = b; }).catch(function (e) { cargando = null; throw e; });
      return cargando;
    }
    var api = {
      /* true si está sonando; false si el navegador exige un gesto del usuario */
      iniciar: function () {
        return asegurar().then(function () {
          if (!vivo) return false;
          return (ctx.state === "running" ? Promise.resolve() : ctx.resume()).then(function () {
            if (ctx.state !== "running" || !vivo) return false;
            if (!fuente) {
              fuente = ctx.createBufferSource(); fuente.buffer = buf; fuente.loop = true; fuente.loopStart = 0; fuente.loopEnd = Math.min(CICLO, buf.duration);   // el audio es periódico: cualquier ventana de 30 s enlaza sin salto
              fuente.connect(ganancia); inicio = ctx.currentTime; fuente.start(0);
            }
            ganancia.gain.cancelScheduledValues(ctx.currentTime); ganancia.gain.setValueAtTime(ganancia.gain.value, ctx.currentTime); ganancia.gain.linearRampToValueAtTime(mudo ? 0 : 0.75, ctx.currentTime + 1.8);
            return true;
          });
        }).catch(function () { return false; });
      },
      fase: function () { return ctx && fuente && ctx.state === "running" ? (ctx.currentTime - inicio) % CICLO : null; },
      silenciar: function (m) { mudo = m; if (ctx && ganancia) { ganancia.gain.cancelScheduledValues(ctx.currentTime); ganancia.gain.setValueAtTime(ganancia.gain.value, ctx.currentTime); ganancia.gain.linearRampToValueAtTime(m ? 0 : 0.75, ctx.currentTime + 0.4); } },
      detener: function () { vivo = false; if (!ctx) return; try { ganancia.gain.cancelScheduledValues(ctx.currentTime); ganancia.gain.setValueAtTime(ganancia.gain.value, ctx.currentTime); ganancia.gain.linearRampToValueAtTime(0, ctx.currentTime + 0.5); } catch (e) {} var c = ctx; setTimeout(function () { try { if (fuente) fuente.stop(); c.close(); } catch (e) {} }, 650); }
    };
    return api;
  }

  function tormenta(escena, lienzo, sonido) {
    var g = lienzo.getContext("2d"), W = 0, H = 0, s = 1, ox = 0, oy = 0, DPR = Math.min(1.5, raiz.devicePixelRatio || 1), movimiento = true, t0 = performance.now(), activo = true, raf = 0;
    try { movimiento = !raiz.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
    var R = azar(7), lejos = [], cerca = [], salp = [], ondas = [], destellos = [];
    function ajustar() {
      W = escena.clientWidth; H = escena.clientHeight; lienzo.width = Math.round(W * DPR); lienzo.height = Math.round(H * DPR);
      s = Math.max(W / IW, H / IH); ox = (W - IW * s) * FOCO_X; oy = (H - IH * s) * 0.5;
      var k = Math.min(1.6, W * H / (1280 * 720)); lejos = []; cerca = [];
      for (var i = 0; i < Math.round(280 * k); i++) lejos.push({ x: R() * W, y: R() * H, v: 0.55 + R() * 0.4, l: 0.5 + R() * 0.5 });
      for (var j = 0; j < Math.round(130 * k); j++) cerca.push({ x: R() * W, y: R() * H, v: 0.9 + R() * 0.6, l: 0.8 + R() * 0.6 });
    }
    function p(x, y) { return [ox + x * s, oy + y * s]; }
    function brillo(t) { return 0.5 + 0.5 * Math.sin(t * 2 * Math.PI / 7.5); }
    function intensidadLuz(i, t) {   // sube y baja despacio (≈ 7 s) con un parpadeo corto y desfasado por foco
      var fase = i * 1.7, lenta = 0.5 + 0.5 * Math.sin(t * 2 * Math.PI / 7.5 + fase), parp = 0.06 * Math.sin(t * 23 + i * 5) + 0.05 * Math.sin(t * 37.3 + i * 2.1) + (Math.sin(t * 3.1 + i) > 0.985 ? -0.2 : 0);
      return Math.max(0.15, 0.42 + 0.55 * lenta + parp);
    }
    function rayo(rl, sem) {   // relámpago ramificado desde las nubes hasta el punto de impacto, con brillo y destello en el suelo
      var T = TIPO_RAYO[rl.tipo], r = azar(sem), x = rl.x, py = rl.y0, px = x, puntos = [[px, py]], f = rl.rayo;
      while (py < rl.y1 - 14) { py = Math.min(rl.y1, py + (10 + r() * 20) * (0.6 + T.ancho * 0.4)); px += (r() - 0.5) * 44 * T.ancho + (x - px) * 0.1; puntos.push([px, py]); }
      function trazo(pts, ancho, alfa) { g.beginPath(); pts.forEach(function (q, i) { var c = p(q[0], q[1]); i ? g.lineTo(c[0], c[1]) : g.moveTo(c[0], c[1]); }); g.lineWidth = Math.max(0.6, ancho * s * T.ancho); g.strokeStyle = "rgba(215,228,255," + Math.min(1, alfa) + ")"; g.stroke(); }
      g.lineJoin = "round"; g.shadowColor = "rgba(170,200,255,1)"; g.shadowBlur = 24 * DPR * T.ancho;
      trazo(puntos, 7, 0.22 * f * T.alfa); trazo(puntos, 3, 0.7 * f * T.alfa); trazo(puntos, 1.2, f * T.alfa);
      if (T.ramas) for (var b = 4; b < puntos.length - 2; b += 4) { var rama = [puntos[b]], qx = puntos[b][0], qy = puntos[b][1], dir = r() < 0.5 ? -1 : 1; for (var m = 0; m < 4; m++) { qx += dir * (10 + r() * 20); qy += 10 + r() * 16; rama.push([qx, qy]); } trazo(rama, 1.6, 0.6 * f); }
      g.shadowBlur = 0;
      var fin = puntos[puntos.length - 1], c = p(fin[0], fin[1]), rr = T.brillo * s, gr = g.createRadialGradient(c[0], c[1], 0, c[0], c[1], rr);   // resplandor donde cae
      g.globalCompositeOperation = "screen"; gr.addColorStop(0, "rgba(220,232,255," + (0.8 * f) + ")"); gr.addColorStop(1, "rgba(150,180,255,0)"); g.fillStyle = gr; g.fillRect(c[0] - rr, c[1] - rr, rr * 2, rr * 2); g.globalCompositeOperation = "source-over";
    }
    function destelloRelampago(fase) {   // dos pulsos rápidos que decaen; cada tipo ilumina más o menos el paisaje
      for (var i = 0; i < RELAMPAGOS.length; i++) {
        var d = fase - RELAMPAGOS[i].t; if (d < -0.01 || d > 0.9) continue;
        var luz = d < 0.06 ? d / 0.06 : d < 0.14 ? 1 - (d - 0.06) * 5 : d < 0.22 ? 0.6 + (d - 0.14) * 4 : Math.max(0, 0.92 - (d - 0.22) * 1.4), T = TIPO_RAYO[RELAMPAGOS[i].tipo];
        return { luz: Math.max(0, luz) * (0.35 + 0.65 * T.velo / 0.38), velo: T.velo, rayo: d < 0.3 ? (d < 0.14 ? 1 : 0.7) : 0, e: RELAMPAGOS[i], i: i };
      }
      return { luz: 0, velo: 0, rayo: 0, e: null, i: 0 };
    }
    /* bandera: el paño (76×93 px de la foto) se recalcula cada fotograma con una onda que crece hacia la punta; el asta y el resto de la foto no se tocan.
       Fuera del paño desplazado se repone el fondo interpolando los colores de ambos lados; los bordes se funden con la foto. */
    var banda = null;
    function prepararBandera() {
      var im = escena.querySelector("img"); if (!im || !im.complete || !im.naturalWidth) return false;
      try {
        var f = document.createElement("canvas"); f.width = IW; f.height = IH; var fg = f.getContext("2d", { willReadFrequently: true }); fg.drawImage(im, 0, 0, IW, IH);
        var B = BANDERA, orig = fg.getImageData(B.x, B.y, B.w, B.h).data, L = fg.getImageData(B.ax, B.y, 1, B.h).data, Rt = fg.getImageData(B.bx, B.y, 1, B.h).data, fondo = new Uint8ClampedArray(B.w * B.h * 4);
        for (var y = 0; y < B.h; y++) for (var x = 0; x < B.w; x++) { var u = x / (B.w - 1), k = (y * B.w + x) * 4; for (var c = 0; c < 3; c++) fondo[k + c] = L[y * 4 + c] * (1 - u) + Rt[y * 4 + c] * u; }
        var sal = document.createElement("canvas"); sal.width = B.w; sal.height = B.h; var sg = sal.getContext("2d"); banda = { orig: orig, fondo: fondo, sal: sal, sg: sg, dat: sg.createImageData(B.w, B.h) };
      } catch (e) { banda = { orig: null }; }
      return true;
    }
    function ondear(t) {
      if (!banda && !prepararBandera()) return; if (!banda.orig) return;
      var B = BANDERA, W2 = B.w, H2 = B.h, o = banda.orig, fo = banda.fondo, d = banda.dat.data, w = 2 * Math.PI * 0.85, k = 6.0;
      for (var x = 0; x < W2; x++) {
        var u = x / (W2 - 1), fase = w * t - k * u, dy = 5.5 * Math.pow(u, 1.15) * Math.sin(fase) + 2 * u * Math.sin(2.3 * fase + 1), dx = 3.2 * u * Math.sin(fase + 1.2), sx = Math.max(0, Math.min(W2 - 1, Math.round(x - dx))), luz = 1 + 0.16 * u * Math.cos(fase);
        for (var y = 0; y < H2; y++) {
          var sy = y - dy, y0 = Math.floor(sy), fr = sy - y0, i = (y * W2 + x) * 4, ed = Math.min(1, Math.min(x, W2 - 1 - x, y, H2 - 1 - y) / 7);
          if (y0 < 0 || y0 + 1 > H2 - 1) { for (var c = 0; c < 3; c++) d[i + c] = fo[i + c]; }
          else { var a1 = (y0 * W2 + sx) * 4, a2 = a1 + W2 * 4; for (var c2 = 0; c2 < 3; c2++) d[i + c2] = Math.min(255, (o[a1 + c2] * (1 - fr) + o[a2 + c2] * fr) * luz); }
          d[i + 3] = 255 * ed;
        }
      }
      banda.sg.putImageData(banda.dat, 0, 0); var c0 = p(B.x, B.y); g.drawImage(banda.sal, c0[0], c0[1], B.w * s, B.h * s);
    }
    function dibujar(ahora, dt) {
      var t = (ahora - t0) / 1000, fa = sonido.fase(), fase = fa == null ? t % CICLO : fa, rl = destelloRelampago(fase);
      g.setTransform(DPR, 0, 0, DPR, 0, 0); g.clearRect(0, 0, W, H);
      if (movimiento) ondear(t);
      /* focos y reflejo del sol entre las nubes (se suman a la foto) */
      g.globalCompositeOperation = "screen";
      LUCES.forEach(function (L, i) {
        var c = p(L[0], L[1]), r = L[2] * s * (1 + 0.06 * Math.sin(t * 2 + i)), a = Math.min(1, intensidadLuz(i, t) * L[3] * (i === LUCES.length - 1 ? 0.5 : 1) + rl.luz * 0.1), gr = g.createRadialGradient(c[0], c[1], 0, c[0], c[1], r * 2.6);
        gr.addColorStop(0, "rgba(255,196,110," + (0.78 * a) + ")"); gr.addColorStop(0.28, "rgba(255,170,80," + (0.34 * a) + ")"); gr.addColorStop(1, "rgba(255,150,60,0)");
        g.fillStyle = gr; g.fillRect(c[0] - r * 2.6, c[1] - r * 2.6, r * 5.2, r * 5.2);
      });
      /* reflejos de los focos en el barro mojado del camino */
      var rf = p(1300, 520); var gR = g.createRadialGradient(rf[0], rf[1] + 60 * s, 0, rf[0], rf[1] + 60 * s, 160 * s); var ar = 0.16 * intensidadLuz(2, t);
      gR.addColorStop(0, "rgba(255,185,90," + ar + ")"); gR.addColorStop(1, "rgba(255,170,80,0)"); g.fillStyle = gR; g.fillRect(rf[0] - 200 * s, rf[1] - 100 * s, 400 * s, 360 * s);
      /* relámpago: velo azulado sobre todo el paisaje y los focos del sol se avivan */
      if (rl.luz > 0) { g.fillStyle = "rgba(170,195,255," + (0.36 * rl.luz * Math.min(1, rl.velo / 0.38 + 0.2)) + ")"; g.fillRect(0, 0, W, H); }
      g.globalCompositeOperation = "source-over";
      if (rl.rayo > 0) { rayo({ x: rl.e.x, y0: rl.e.y0, y1: rl.e.y1, tipo: rl.e.tipo, rayo: rl.rayo * (0.8 + 0.2 * rl.luz) }, 31 + rl.i * 17); }
      /* lluvia: capa lejana (fina, más lenta) y cercana (larga, brillante); durante el relámpago se ve más */
      var viento = 0.2, alfaL = 0.16 + rl.luz * 0.22, alfaC = 0.3 + rl.luz * 0.3; g.lineCap = "round";
      function lluvia(lista, ancho, alfa, largo, vel) {
        g.lineWidth = ancho; g.strokeStyle = "rgba(205,225,255," + alfa + ")"; g.beginPath();
        for (var i = 0; i < lista.length; i++) { var q = lista[i], l = largo * q.l * s * 1.1; g.moveTo(q.x, q.y); g.lineTo(q.x + l * viento, q.y + l); q.y += vel * q.v * dt * s * 0.9; q.x += vel * q.v * dt * s * 0.9 * viento; if (q.y > H + 40) { q.y = -40 - R() * 60; q.x = R() * (W + 120) - 60; } if (q.x > W + 60) q.x -= W + 120; }
        g.stroke();
      }
      if (movimiento) { lluvia(lejos, 1, alfaL, 24, 1300); lluvia(cerca, 1.8, alfaC, 52, 2000); } else { lluvia(lejos, 1, alfaL, 24, 0); lluvia(cerca, 1.8, alfaC, 52, 0); }
      if (!movimiento) return;
      /* gotas que rebotan en los impermeables y las mochilas de las personas */
      PERSONAS.forEach(function (P, k) { var n = Math.round(dt * 70 * (k ? 0.7 : 1)); for (var i = 0; i < n; i++) { var u = R(), v = Math.pow(R(), 1.7) * 0.7; salp.push({ x: P[0] + u * P[2], y: P[1] + v * P[3], vx: (R() - 0.5) * 50, vy: -(40 + R() * 80), vida: 0, dur: 0.25 + R() * 0.3 }); } });
      g.fillStyle = "rgba(225,238,255,1)";
      for (var i = salp.length - 1; i >= 0; i--) {
        var d = salp[i]; d.vida += dt; if (d.vida > d.dur) { salp.splice(i, 1); continue; }
        d.x += d.vx * dt; d.y += d.vy * dt; d.vy += 420 * dt; var c = p(d.x, d.y), a = (1 - d.vida / d.dur) * (0.65 + rl.luz * 0.3);
        g.globalAlpha = a; g.beginPath(); g.arc(c[0], c[1], Math.max(0.8, 1.6 * s), 0, 6.2832); g.fill();
      }
      /* destellos de agua sobre los ponchos */
      if (R() < dt * 14) { var P2 = PERSONAS[R() < 0.65 ? 0 : 1]; destellos.push({ x: P2[0] + R() * P2[2], y: P2[1] + R() * P2[3] * 0.8, vida: 0 }); }
      for (var j = destellos.length - 1; j >= 0; j--) { var e = destellos[j]; e.vida += dt; if (e.vida > 0.35) { destellos.splice(j, 1); continue; } var c2 = p(e.x, e.y), a2 = Math.sin(e.vida / 0.35 * Math.PI) * 0.7; g.globalAlpha = a2; var gg = g.createRadialGradient(c2[0], c2[1], 0, c2[0], c2[1], 7 * s); gg.addColorStop(0, "rgba(255,255,255,1)"); gg.addColorStop(1, "rgba(255,230,190,0)"); g.fillStyle = gg; g.fillRect(c2[0] - 8 * s, c2[1] - 8 * s, 16 * s, 16 * s); }
      g.globalAlpha = 1;
      /* ondas de las gotas al caer en el camino mojado */
      var nuevas = Math.round(dt * 60); for (var m = 0; m < nuevas; m++) { var pt = [560 + R() * 830, 505 + R() * 400]; if (dentro(pt, CAMINO)) ondas.push({ x: pt[0], y: pt[1], vida: 0, dur: 0.5 + R() * 0.4, r: 5 + R() * 7 }); }
      g.lineWidth = 1; for (var o = ondas.length - 1; o >= 0; o--) { var w = ondas[o]; w.vida += dt; if (w.vida > w.dur) { ondas.splice(o, 1); continue; } var q = w.vida / w.dur, cc = p(w.x, w.y); g.strokeStyle = "rgba(255,225,185," + (0.55 * (1 - q) + rl.luz * 0.2) + ")"; g.beginPath(); g.ellipse(cc[0], cc[1], w.r * q * s, w.r * q * s * 0.38, 0, 0, 6.2832); g.stroke(); }
    }
    var ult = performance.now();
    function bucle(ahora) {
      if (!activo) return; raf = requestAnimationFrame(bucle);
      if (document.hidden) { ult = ahora; return; }
      var dt = Math.min(0.05, (ahora - ult) / 1000); ult = ahora; dibujar(ahora, dt);
    }
    ajustar(); var aj = function () { ajustar(); if (!movimiento) dibujar(performance.now(), 0.016); }; raiz.addEventListener("resize", aj);
    if (movimiento) raf = requestAnimationFrame(bucle); else dibujar(performance.now(), 0.016);
    return function () { activo = false; cancelAnimationFrame(raf); raiz.removeEventListener("resize", aj); };
  }

  function intro(alAsumir) {
    Array.prototype.forEach.call(document.querySelectorAll("dialog.sr-intro"), function (x) { x.remove(); });
    var d = document.createElement("dialog"); d.className = "sr-intro"; d.setAttribute("aria-labelledby", "srIntroT");
    d.innerHTML = '<div class="sr-intro__escena"><img class="sr-intro__img" src="' + IMG_INTRO + '" alt="" width="1672" height="941" fetchpriority="high"><canvas class="sr-intro__lienzo" aria-hidden="true"></canvas></div><div class="sr-intro__vel"></div>' +
      '<button type="button" class="sr-intro__snd" data-sonido aria-pressed="true">Sonido activado</button>' +
      '<div class="sr-intro__c"><p class="sr-intro__k">Medicina rural y comunitaria</p><h2 id="srIntroT">Tu primer día como serumista</h2>' +
      '<p>Una posta de altura, pocos insumos, un hospital lejos y una comunidad que confía en ti. Cada decisión cuenta.</p><button type="button" class="sr-btn sr-btn--lg" data-asumir>Asumir mi posta</button><button type="button" class="sr-intro__o" data-omitir>Omitir</button>' +
      '<p class="sr-intro__nota">Ilustración generada con IA; el paisaje, el establecimiento y el audio de tormenta son una recreación sintetizada, no registros reales.</p></div>';
    document.body.appendChild(d);
    var sonido = sonidoTormenta(), parar = null, mudo = false, btn = d.querySelector("[data-sonido]");
    function etiqueta(estado) { btn.textContent = estado; btn.setAttribute("aria-pressed", String(!mudo && estado === "Sonido activado")); }
    function arrancar() { sonido.iniciar().then(function (suena) { if (suena) etiqueta(mudo ? "Sonido silenciado" : "Sonido activado"); else { etiqueta("Activar sonido"); btn.setAttribute("aria-pressed", "false"); d.addEventListener("pointerdown", reintento, { once: true }); d.addEventListener("keydown", reintento, { once: true }); } }); }
    function reintento() { if (!mudo) arrancar(); }
    function cerrar(ir) { if (parar) parar(); sonido.detener(); try { d.close(); } catch (e) {} d.remove(); try { sessionStorage.setItem("mqp_serums_intro", "1"); } catch (e) {} if (ir && alAsumir) alAsumir(); }
    btn.addEventListener("click", function () { if (btn.textContent === "Activar sonido") { mudo = false; arrancar(); return; } mudo = !mudo; sonido.silenciar(mudo); etiqueta(mudo ? "Sonido silenciado" : "Sonido activado"); });
    d.querySelector("[data-asumir]").addEventListener("click", function () { cerrar(true); });
    d.querySelector("[data-omitir]").addEventListener("click", function () { cerrar(false); });
    d.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(false); });
    if (d.showModal) d.showModal(); else d.setAttribute("open", ""); d.querySelector("[data-asumir]").focus();
    parar = tormenta(d.querySelector(".sr-intro__escena"), d.querySelector(".sr-intro__lienzo"), sonido); arrancar();
  }
  function introVista() { try { return sessionStorage.getItem("mqp_serums_intro") === "1"; } catch (e) { return false; } }

  /* ---------- portada de la estación ---------- */
  function insumosHtml(inv, ini) {
    return '<table class="sr-tabla"><caption class="sr-sr">Inventario de la posta</caption><thead><tr><th scope="col">Insumo</th><th scope="col">Disponible</th></tr></thead><tbody>' + Object.keys(N().INSUMOS).map(function (k) {
      var v = inv[k] || 0, bajo = ini && ini[k] != null ? v < ini[k] : false;
      return '<tr><th scope="row">' + esc(N().INSUMOS[k]) + '</th><td class="' + (v === 0 ? "sr-cero" : bajo ? "sr-bajo" : "") + '">' + v + (ini && ini[k] != null && ini[k] !== v ? ' <small>(inicio: ' + ini[k] + ')</small>' : "") + '</td></tr>';
    }).join("") + '</tbody></table>';
  }
  function badgeEstado(c) { return '<span class="sr-estado" title="Estado de publicación del caso">' + esc(c.estado_publicacion) + '</span>'; }

  function portada(cont, datos) {
    var casos = datos.casos, prog = progreso(), est = posta(), rec = N().recomendar(casos, prog), res = N().resumenProgreso(prog), N_ = N();
    var hechos = casos.filter(function (c) { return prog.casos[c.id]; }).length;
    var f = datos.evidencia.fuentes, nVig = f.filter(function (x) { return x.estado === "Normativa vigente verificada"; }).length;
    cont.innerHTML = '<div class="sr">' +
      '<nav class="gh-migas" aria-label="Ruta"><a href="#/guardia">Centro de simulación</a><span aria-hidden="true">›</span><span aria-current="page">Misión SERUMS</span></nav>' +
      '<header class="sr-hero"><img class="sr-hero__img" src="' + IMG + '" alt="" width="1280" height="720" fetchpriority="high"><div class="sr-hero__vel"></div><div class="sr-hero__c"><p class="sr-tags"><span class="sr-tag">Medicina rural y comunitaria</span><span class="sr-tag sr-tag--nuevo">Nuevo</span></p>' +
      '<h1>Misión SERUMS<span>Sobrevive a la posta</span></h1><p class="sr-hero__t">Atiende una posta con recursos limitados: decide, usa tu inventario, refiere a tiempo y cuida a tu comunidad. Los diez casos son originales y se apoyan en normativa peruana verificada; lo que aún falta validar está declarado.</p>' +
      '<p class="sr-hero__b"><a class="sr-btn" href="#srCasos" data-ir="srCasos">Ver los casos</a><button type="button" class="sr-btn sr-btn--claro" id="srVerIntro">▶ Ver la introducción</button></p></div></header>' +
      '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
      '<div class="sr-cols"><section class="sr-izq" id="srCasos" aria-labelledby="srCasosT" tabindex="-1"><h2 id="srCasosT">Diez casos de la posta</h2><ul class="sr-casos">' + casos.map(function (c) {
        var r = prog.casos[c.id], rc = rec && rec.caso === c.id;
        return '<li class="sr-caso' + (rc ? " is-rec" : "") + '"><p class="sr-caso__n">Caso ' + c.numero + ' · ' + esc(c.tema) + (rc ? ' · <b>Recomendado</b>' : "") + '</p><h3>' + esc(c.titulo) + '</h3><p>' + esc(c.resumen) + '</p>' +
          '<p class="sr-caso__m">' + badgeEstado(c) + '<span>≈ ' + c.duracion_min + ' min · ' + c.momentos.length + ' decisiones</span>' + (r ? '<span>Mejor: <b>' + r.mejor + ' %</b> · Intentos: ' + r.intentos + '</span>' : "") + '</p>' +
          (rc ? '<p class="sr-caso__r">' + esc(rec.motivo) + '</p>' : "") + '<a class="sr-btn sr-btn--sm" href="#/serums/' + esc(c.id) + '">' + (sesion(c.id) ? "Continuar el caso" : r ? "Reintentar" : "Comenzar el caso") + '</a></li>';
      }).join("") + '</ul></section>' +
      '<aside class="sr-der" aria-label="Panel de la posta y progreso">' +
      '<section class="sr-panel" aria-labelledby="srPostaT"><h2 id="srPostaT">Tu posta</h2><p class="sr-pz">Establecimiento ficticio configurable. Los cambios se guardan en este navegador.</p>' +
      '<form id="srForm" class="sr-form"><label>Nombre<input name="nombre" maxlength="60" value="' + esc(est.nombre) + '"></label>' +
      '<div class="sr-f2"><label>Categoría<select name="categoria">' + ["I-1", "I-2", "I-3", "I-4"].map(function (x) { return '<option' + (x === est.categoria ? " selected" : "") + '>' + x + '</option>'; }).join("") + '</select></label>' +
      '<label>Ámbito<select name="ambito">' + [["sierra", "Sierra"], ["selva", "Selva"], ["costa", "Costa rural"]].map(function (x) { return '<option value="' + x[0] + '"' + (x[0] === est.ambito ? " selected" : "") + '>' + x[1] + '</option>'; }).join("") + '</select></label></div>' +
      '<div class="sr-f2"><label>Minutos al hospital<input name="distancia_min" type="number" min="10" max="900" value="' + est.distancia_min + '"></label>' +
      '<label>Comunicación<select name="comunicacion">' + [["radio", "Radio"], ["telefono", "Teléfono"], ["ninguna", "Sin comunicación"]].map(function (x) { return '<option value="' + x[0] + '"' + (x[0] === est.comunicacion ? " selected" : "") + '>' + x[1] + '</option>'; }).join("") + '</select></label></div>' +
      '<label class="sr-chk"><input type="checkbox" name="ambulancia"' + (est.ambulancia ? " checked" : "") + '> Cuenta con ambulancia</label>' +
      '<p class="sr-form__b"><button class="sr-btn sr-btn--sm" type="submit">Guardar la posta</button><button class="sr-btn sr-btn--claro sr-btn--sm" type="button" id="srRepo">Reponer almacén</button></p><p class="sr-ok" id="srOk" role="status"></p></form>' +
      '<details class="sr-det"><summary>Inventario persistente</summary>' + insumosHtml(est.inventario) + '<p class="sr-pz">Lo que consumes en un caso se descuenta del almacén en los siguientes. «Reponer almacén» restablece las cantidades iniciales.</p></details></section>' +
      '<section class="sr-panel" aria-labelledby="srProgT"><h2 id="srProgT">Mi progreso como serumista</h2>' +
      (res.intentos ? '<p><b>' + hechos + ' de ' + casos.length + '</b> casos intentados · ' + res.intentos + ' intentos · ' + res.criticos + ' errores críticos</p><ul class="sr-ejes">' + Object.keys(N_.EJES).map(function (k) { var v = res.medias[k]; return '<li><span>' + esc(N_.EJES[k]) + '</span><span class="sr-bar" role="img" aria-label="' + (v == null ? "sin datos" : v + " %") + '"><i style="width:' + (v || 0) + '%"></i></span><b>' + (v == null ? "—" : v + " %") + '</b></li>'; }).join("") + '</ul>' + (res.eje_flojo ? '<p class="sr-pz">Eje por reforzar: <b>' + esc(N_.EJES[res.eje_flojo]) + '</b>.</p>' : "")
        : '<p class="sr-pz">Aún no has completado ningún caso. Tu progreso se calcula solo con tus intentos reales.</p>') + '</section>' +
      '<section class="sr-panel" aria-labelledby="srCampT"><h2 id="srCampT">30 días como serumista</h2><p>La campaña de 30 días usa este mismo motor: el inventario y la reputación pasan de un día al siguiente. <b>Aún no está disponible</b>: la estructura técnica y sus pruebas están listas, pero faltan los guiones de los días, que deben pasar revisión clínica.</p></section>' +
      '<section class="sr-panel" aria-labelledby="srEvT"><h2 id="srEvT">Fuentes y vigencia</h2><p>' + f.length + ' fuentes registradas: <b>' + nVig + '</b> con normativa vigente verificada, ' + (f.length - nVig) + ' en revisión o históricas. Última revisión: ' + esc(datos.evidencia.revision.ultima) + '.</p><button class="sr-btn sr-btn--claro sr-btn--sm" type="button" id="srFuentes">Ver el registro de evidencia</button></section></aside></div></div>';
    cont.querySelector("#srVerIntro").addEventListener("click", function () { intro(); });
    cont.querySelector("[data-ir]").addEventListener("click", function (ev) { ev.preventDefault(); var t = cont.querySelector("#srCasos"); t.scrollIntoView({ behavior: "smooth", block: "start" }); t.focus({ preventScroll: true }); });
    cont.querySelector("#srFuentes").addEventListener("click", function (ev) { registro(datos.evidencia, ev.currentTarget); });
    var form = cont.querySelector("#srForm");
    form.addEventListener("submit", function (ev) {
      ev.preventDefault(); var fd = new FormData(form), act = posta();
      var nuevo = N().establecimiento({ nombre: fd.get("nombre"), categoria: fd.get("categoria"), ambito: fd.get("ambito"), distancia_min: fd.get("distancia_min"), comunicacion: fd.get("comunicacion"), ambulancia: !!fd.get("ambulancia"), inventario: act.inventario });
      guardarPosta(nuevo); cont.querySelector("#srOk").textContent = "Posta guardada.";
    });
    cont.querySelector("#srRepo").addEventListener("click", function () { var act = posta(); act.inventario = JSON.parse(JSON.stringify(N().ESTABLECIMIENTO_BASE.inventario)); guardarPosta(act); portada(cont, datos); var o = cont.querySelector("#srOk"); if (o) o.textContent = "Almacén repuesto."; });
  }

  function registro(ev, disparador) {
    var fila = function (x) {
      var cls = x.estado === "Normativa vigente verificada" ? "ok" : x.estado === "Documento en revisión" ? "rev" : "hist";
      return '<li class="sr-fu"><p class="sr-fu__e sr-fu__e--' + cls + '">' + esc(x.estado) + '</p><h3>' + esc(x.titulo) + '</h3><p>' + esc(x.organismo) + ' · ' + esc(x.numero) + (x.fecha ? ' · ' + esc(x.fecha) : "") + '</p>' +
        (x.nota ? '<p class="sr-pz">' + esc(x.nota) + '</p>' : "") + '<p class="sr-pz">Verificado el ' + esc(x.verificado) + (x.indexada ? ' · texto indexado con página' : ' · texto no indexado') + (x.url ? ' · <a href="' + esc(x.url) + '" target="_blank" rel="noopener noreferrer">Abrir en el portal oficial</a>' : "") + '</p></li>';
    };
    var h = '<p class="gd-aviso" role="note">' + esc(ev.aviso) + '</p><p><b>Revisión periódica:</b> ' + esc(ev.revision.frecuencia) + '. Última: ' + esc(ev.revision.ultima) + '. ' + esc(ev.revision.regla) + '</p><ul class="sr-fus">' + ev.fuentes.map(fila).join("") + '</ul>' +
      '<h3 class="gd-h3">Historial de cambios</h3><ul>' + ev.historial.map(function (x) { return '<li>' + esc(x.fecha) + ': ' + esc(x.cambio) + '</li>'; }).join("") + '</ul>';
    GD().dialogo("Registro de evidencia de la Misión SERUMS", h, "gd-dlg--lab", disparador);
  }

  /* ---------- una atención ---------- */
  function jugar(cont, caso, datos) {
    var Nn = N();
    if (detener) detener();
    var guard = sesion(caso.id), e = guard && guard.estado && !guard.estado.fin ? guard.estado : null, tab = "paciente", ultimo = null, aviso = "";
    if (e) e.ultimo = Date.now(); else { e = Nn.iniciar(caso, posta(), Date.now()); persistir(); }
    function persistir() { GD().ls(K_SES + ":" + caso.id, JSON.stringify({ v: 1, caso: caso.id, estado: e })); }
    function salir() { if (!e.fin) persistir(); window.removeEventListener("hashchange", alIrse); GD().cerrarDialogo(); if (detener === salir) detener = null; }
    function alIrse() { if (location.hash.indexOf("#/serums/" + caso.id) !== 0) salir(); }
    detener = salir; window.addEventListener("hashchange", alIrse);

    function pintar(enfocar) {
      if (e.fin) return informe();
      var m = Nn.momentoActual(caso, e), idx = caso.momentos.indexOf(m) + 1;
      cont.innerHTML = '<div class="sr sr--caso"><nav class="gh-migas" aria-label="Ruta"><a href="#/guardia">Centro de simulación</a><span aria-hidden="true">›</span><a href="#/serums">Misión SERUMS</a><span aria-hidden="true">›</span><span aria-current="page">Caso ' + caso.numero + '</span></nav>' +
        '<header class="sr-top"><div><h1>' + esc(caso.titulo) + '</h1><p class="sr-pz">' + esc(e.establecimiento.nombre) + ' · categoría ' + esc(e.establecimiento.categoria) + ' · ' + badgeEstado(caso) + '</p></div>' +
        '<p class="sr-reloj" role="status"><span><small>Reloj de simulación</small><b id="srSim">' + reloj(e.t_sim) + '</b></span><span><small>Tiempo real</small><b id="srReal">' + seg(e.t_real) + '</b></span><span><small>Estado clínico</small><b class="sr-g sr-g--' + e.gravedad + '">' + esc(Nn.GRAVEDAD[e.gravedad]) + '</b></span></p></header>' +
        '<p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        '<div class="sr-juego"><section class="sr-ficha" aria-label="Ficha clínica"><div class="sr-tabs" role="tablist" aria-label="Ficha clínica">' + TABS.map(function (t) { return '<button role="tab" type="button" id="srT_' + t[0] + '" aria-selected="' + (t[0] === tab) + '" aria-controls="srP" tabindex="' + (t[0] === tab ? 0 : -1) + '" data-tab="' + t[0] + '">' + t[1] + '</button>'; }).join("") + '</div><div class="sr-tabp" role="tabpanel" id="srP" aria-labelledby="srT_' + tab + '" tabindex="0">' + panel(tab) + '</div></section>' +
        '<section class="sr-decision" aria-labelledby="srDecT"><p class="sr-paso">Decisión ' + idx + ' de ' + caso.momentos.length + ' · ' + esc(Nn.EJES[m.eje]) + '</p><h2 id="srDecT" tabindex="-1">' + esc(m.titulo) + '</h2><p>' + esc(m.texto) + '</p>' +
        (aviso ? '<p class="sr-aviso" role="status">' + aviso + '</p>' : "") +
        '<fieldset class="sr-ops"><legend class="sr-sr">Alternativas</legend>' + m.opciones.map(function (o) {
          var d = Nn.disponibilidad(o, e), tx = (o.cons ? Object.keys(o.cons).map(function (k) { return o.cons[k] + " × " + Nn.INSUMOS[k]; }).join(", ") : "");
          return '<label class="sr-op' + (d.ok ? "" : " is-off") + '"><input type="radio" name="op" value="' + esc(o.id) + '"' + (d.ok ? "" : " disabled") + '><span><b>' + esc(o.id.toUpperCase()) + '.</b> ' + esc(o.texto) + (tx ? '<small>Usa: ' + esc(tx) + '</small>' : "") + (d.ok ? "" : '<small class="sr-bloq">' + esc(d.motivo) + '</small>') + '</span></label>';
        }).join("") + '</fieldset><p class="sr-pz">Tu respuesta se registra sin corregirla: la explicación completa aparece en el informe final.</p><p><button type="button" class="sr-btn" id="srDecidir" disabled>Registrar decisión</button></p></section></div></div>';
      var tabs = cont.querySelectorAll("[data-tab]");
      Array.prototype.forEach.call(tabs, function (b, i) {
        b.addEventListener("click", function () { tab = b.getAttribute("data-tab"); pintar(); cont.querySelector("#srT_" + tab).focus(); });
        b.addEventListener("keydown", function (ev) { var j = ev.key === "ArrowRight" ? i + 1 : ev.key === "ArrowLeft" ? i - 1 : ev.key === "Home" ? 0 : ev.key === "End" ? tabs.length - 1 : -1; if (j < 0) return; ev.preventDefault(); tab = tabs[(j + tabs.length) % tabs.length].getAttribute("data-tab"); pintar(); cont.querySelector("#srT_" + tab).focus(); });
      });
      var rad = cont.querySelectorAll('input[name="op"]'), bt = cont.querySelector("#srDecidir");
      Array.prototype.forEach.call(rad, function (r) { r.addEventListener("change", function () { bt.disabled = false; }); });
      bt.addEventListener("click", function () {
        var sel = cont.querySelector('input[name="op"]:checked'); if (!sel) return;
        var antes = e, r = Nn.decidir(caso, e, sel.value, Date.now()); if (!r.ok) { aviso = esc(r.motivo); pintar(); return; }
        e = r.estado; aviso = consecuencia(antes, e, r.opcion); persistir(); if (e.fin) { finalizar(); return; }
        pintar(); var h = cont.querySelector("#srDecT"); if (h) h.focus();
      });
      var pr = cont.querySelectorAll("[data-prueba]");
      Array.prototype.forEach.call(pr, function (b) { b.addEventListener("click", function () {
        var r = Nn.solicitarPrueba(caso, e, b.getAttribute("data-prueba"), Date.now()); if (!r.ok) { aviso = esc(r.motivo); } else { e = r.estado; aviso = "Prueba solicitada. Pasaron " + (por(caso.pruebas, b.getAttribute("data-prueba")).min || 0) + " min de simulación."; persistir(); }
        pintar(); cont.querySelector("#srT_pruebas").focus(); }); });
      var sup = cont.querySelector("#srSup"); if (sup) sup.addEventListener("submit", function (ev) { ev.preventDefault(); supervisor(cont.querySelector("#srQ").value, cont.querySelector("#srRes"), caso, datos); });
    }

    /* describe lo que cambió en el mundo sin revelar si la decisión fue buena */
    function consecuencia(a, b, o) {
      var p = ["Decisión registrada. Pasaron " + (b.t_sim - a.t_sim) + " min de simulación."], g = {}; Object.keys(o.cons || {}).forEach(function (k) { if (a.inventario[k] !== b.inventario[k]) g[k] = a.inventario[k] - b.inventario[k]; });
      var gasto = Object.keys(g).map(function (k) { return g[k] + " × " + N().INSUMOS[k]; }); if (gasto.length) p.push("Se usó: " + gasto.join(", ") + ".");
      b.historial.slice(a.historial.length).filter(function (h) { return h.tipo === "evento"; }).forEach(function (h) { p.push("<b>Evento:</b> " + esc(h.texto)); });
      return p.map(function (x) { return x.charAt(0) === "<" ? x : esc(x); }).join(" ");
    }

    function panel(t) {
      var P = caso.paciente, v = e.vitales, h = '';
      if (t === "paciente") {
        h = '<h3>' + esc(P.titulo) + '</h3><p>' + esc(P.motivo) + '</p>' + vitales(v) + '<p class="sr-pz">Estado clínico actual: <b>' + esc(N().GRAVEDAD[e.gravedad]) + '</b>. Cambia según tus decisiones y el paso del tiempo simulado.</p>';
      } else if (t === "historia") {
        h = '<dl class="sr-dl">' + caso.historia.map(function (x) { return '<dt>' + esc(x.rotulo) + '</dt><dd>' + esc(x.texto) + '</dd>'; }).join("") + '</dl>';
      } else if (t === "examen") {
        h = (caso.examen.length ? '<dl class="sr-dl">' + caso.examen.map(function (x) { return '<dt>' + esc(x.rotulo) + '</dt><dd>' + esc(x.texto) + '</dd>'; }).join("") + '</dl>' : '<p class="sr-pz">Este caso no tiene un examen físico individual: la valoración es de la jornada.</p>') + vitales(v);
      } else if (t === "pruebas") {
        h = caso.pruebas.length ? '<ul class="sr-pruebas">' + caso.pruebas.map(function (p) {
          var hecha = e.pruebas.indexOf(p.id) >= 0, falta = p.insumo && (e.inventario[p.insumo] || 0) < 1;
          return '<li><b>' + esc(p.nombre) + '</b><small>' + p.min + ' min' + (p.insumo ? ' · usa ' + esc(N().INSUMOS[p.insumo]) : "") + '</small>' + (hecha ? '<p class="sr-res">Resultado: ' + esc(p.resultado) + '</p>' : '<button type="button" class="sr-btn sr-btn--sm sr-btn--claro" data-prueba="' + esc(p.id) + '"' + (falta ? " disabled" : "") + '>Solicitar</button>' + (falta ? '<small class="sr-bloq">Insumo insuficiente</small>' : "")) + '</li>';
        }).join("") + '</ul>' : '<p class="sr-pz">En este caso no hay pruebas disponibles en la posta.</p>';
      } else if (t === "inventario") {
        h = insumosHtml(e.inventario, e.inventario_inicial);
      } else if (t === "referencia") {
        var R = e.referencia, est = e.establecimiento, bloq = e.flags.indexOf("via_bloqueada") >= 0;
        h = '<dl class="sr-dl"><dt>Distancia al hospital</dt><dd>' + est.distancia_min + ' min por carretera</dd><dt>Ambulancia</dt><dd>' + (est.ambulancia ? "Disponible" : "No disponible: el traslado se demora más") + '</dd><dt>Comunicación</dt><dd>' + esc({ radio: "Radio", telefono: "Teléfono", ninguna: "Sin comunicación" }[est.comunicacion]) + '</dd><dt>Estado de la vía</dt><dd>' + (bloq ? "<b>Bloqueada</b>" : "Transitable") + '</dd>' +
          '<dt>Tiempo estimado de traslado</dt><dd>' + reloj(N().tiempoReferencia(e)) + '</dd><dt>Estado de la referencia</dt><dd>' + esc({ ninguna: "Sin referencia", solicitada: "Referencia de emergencia solicitada", programada: "Referencia programada", rechazada: "Referencia no realizada" }[R.estado]) + '</dd></dl><p class="sr-pz">La referencia transfiere la responsabilidad a un establecimiento de mayor capacidad; la contrarreferencia devuelve al paciente con indicaciones. Lo que decidas en el caso se evalúa con el eje «Referencia y comunicación».</p>';
      } else if (t === "normativa") {
        h = fuentesCaso() + '<form id="srSup" class="sr-sup"><label for="srQ"><b>Consultar al supervisor</b></label><p class="sr-pz">Búsqueda documental en las fuentes indexadas de este caso. No es una IA: te muestra fragmentos reales con su página.</p><div class="sr-sup__f"><input id="srQ" type="search" placeholder="Ej.: criterios de severidad" autocomplete="off" required><button class="sr-btn sr-btn--sm" type="submit">Buscar</button></div></form><div id="srRes" aria-live="polite"></div>';
      } else {
        var lin = e.historial;
        h = lin.length ? '<ol class="sr-evo">' + lin.map(function (x) {
          if (x.tipo === "evento") return '<li class="sr-evo__e"><b>Minuto ' + x.t_sim + ' · Evento.</b> ' + esc(x.texto) + '</li>';
          if (x.tipo === "prueba") return '<li><b>Minuto ' + x.t_sim + ' · Prueba solicitada.</b> ' + esc(x.texto) + '</li>';
          var m = por(caso.momentos, x.momento), o = por(m.opciones, x.opcion);
          return '<li><b>Minuto ' + x.t_sim + ' · ' + esc(m.titulo) + '.</b> Elegiste: ' + esc(o.texto) + '</li>';
        }).join("") + '</ol>' : '<p class="sr-pz">Aún no hay acciones registradas.</p>';
      }
      return h;
    }
    function vitales(v) {
      var L = { fc: ["Frecuencia cardiaca", "lpm"], fr: ["Frecuencia respiratoria", "rpm"], sat: ["Saturación de oxígeno", "%"], temp: ["Temperatura", "°C"], pas: ["PA sistólica", "mm Hg"], pad: ["PA diastólica", "mm Hg"] };
      var k = Object.keys(v).filter(function (x) { return L[x]; }); if (!k.length) return "";
      return '<ul class="sr-vit">' + k.map(function (x) { return '<li><small>' + L[x][0] + '</small><b>' + v[x] + '</b> ' + L[x][1] + '</li>'; }).join("") + '</ul>';
    }
    function fuentesCaso() {
      var ids = caso.evidencia || [], f = datos.evidencia.fuentes;
      var h = ids.length ? '<h3>Fuentes de este caso</h3><ul class="sr-fus">' + ids.map(function (id) { var x = por(f, id); return x ? '<li class="sr-fu"><p class="sr-fu__e sr-fu__e--ok">' + esc(x.estado) + '</p><h4>' + esc(x.titulo) + '</h4><p class="sr-pz">' + esc(x.numero) + ' · ' + esc(x.fecha) + '</p></li>' : ""; }).join("") + '</ul>' : '<p class="sr-pz">Este caso aún no tiene una fuente documental indexada.</p>';
      return h + '<div class="sr-pend"><b>Pendiente de validación científica</b><ul>' + caso.pendientes.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join("") + '</ul></div>';
    }

    function finalizar() {
      var ev = Nn.evaluar(caso, e), p = Nn.registrarIntento(progreso(), caso, ev, Date.now()); guardarProgreso(p);
      var pst = posta(); Object.keys(ev.consumo).forEach(function (k) { pst.inventario[k] = Math.max(0, (pst.inventario[k] || 0) - ev.consumo[k]); }); if (!caso.inventario_ajuste) guardarPosta(pst);
      GD().ls(K_SES + ":" + caso.id, null); informe(ev);
    }

    function informe(ev) {
      ev = ev || Nn.evaluar(caso, e); var Nm = Nn, dec = e.historial.filter(function (h) { return h.tipo === "decision"; }), f = datos.evidencia.fuentes, rec = Nm.recomendar(datos.casos, progreso()), flojo = ev.ejes.filter(function (x) { return x.pct != null; }).sort(function (a, b) { return a.pct - b.pct; })[0];
      var sec = function (l, t, c) { return '<section class="sr-sec" aria-labelledby="srS' + l + '"><h2 id="srS' + l + '"><span>' + l + '</span>' + esc(t) + '</h2>' + c + '</section>'; };
      var A = '<p class="sr-nota sr-nota--' + (ev.total >= 75 ? "ok" : ev.total >= 60 ? "med" : "mal") + '"><b>' + ev.total + ' / 100</b> · ' + esc(ev.banda) + '</p>' + (ev.topado_por_error_critico ? '<p class="sr-alerta" role="alert">Cometiste al menos un error crítico de seguridad: el puntaje máximo posible queda limitado a ' + Nm.TOPE_CRITICO + '.</p>' : "") +
        '<ul class="sr-ejes">' + ev.ejes.map(function (x) { return '<li><span>' + esc(x.nombre) + ' <small>(' + x.peso + ' pts)</small></span><span class="sr-bar" role="img" aria-label="' + (x.pct == null ? "no aplica" : x.pct + " %") + '"><i style="width:' + (x.pct || 0) + '%"></i></span><b>' + (x.pct == null ? "No aplica" : x.pct + " %") + '</b></li>'; }).join("") + '</ul><p><b>Desenlace:</b> ' + esc(ev.desenlace_texto) + '</p>';
      var B = '<ol class="sr-dec">' + dec.map(function (x) {
        var m = por(caso.momentos, x.momento), o = por(m.opciones, x.opcion), mejor = m.opciones.filter(function (q) { return q.calidad === "optima"; })[0];
        return '<li class="sr-dec__i sr-dec__i--' + o.calidad + '"><h3>' + esc(m.titulo) + '</h3><p>Elegiste: <b>' + esc(o.texto) + '</b></p><p class="sr-q">' + esc(CALIDAD[o.calidad]) + (o.error ? ' · ' + esc(Nm.ERRORES[o.error]) : "") + '</p><p>' + esc(o.retro) + '</p>' +
          (o.calidad !== "optima" ? '<p><b>Mejor opción:</b> ' + esc(mejor.texto) + '. ' + esc(mejor.retro) + '</p>' : "") +
          ((o.ref || []).length ? '<p class="sr-pz">Fuente: ' + o.ref.map(function (r) { var d = por(f, r.doc); return esc(d ? d.numero : r.doc) + ', p. ' + r.pag; }).join("; ") + '</p>' : '<p class="sr-pz">Sin cita documental verificada: <b>pendiente de validación científica</b>.</p>') + '</li>';
      }).join("") + '</ol>';
      var ek = Object.keys(ev.errores), C = ek.length ? '<ul>' + ek.map(function (k) { return '<li>' + esc(Nm.ERRORES[k]) + ': <b>' + ev.errores[k] + '</b></li>'; }).join("") + '</ul>' : '<p>No cometiste errores clasificados en este intento.</p>';
      var ck = Object.keys(ev.consumo), D = ck.length ? '<ul>' + ck.map(function (k) { return '<li>' + esc(Nm.INSUMOS[k]) + ': <b>' + ev.consumo[k] + '</b> usados</li>'; }).join("") + '</ul><p class="sr-pz">Se descontaron de tu almacén persistente.</p>' : '<p>No consumiste insumos.</p>';
      var E = '<ul><li>Tiempo de simulación: <b>' + reloj(ev.t_sim) + '</b></li><li>Tiempo real: <b>' + seg(ev.t_real) + '</b></li><li>Referencia: <b>' + esc({ ninguna: "no hubo", solicitada: "de emergencia", programada: "programada", rechazada: "no realizada" }[ev.referencia.estado]) + '</b></li><li>Traslado estimado: <b>' + reloj(Nm.tiempoReferencia(e)) + '</b>' + (e.flags.indexOf("via_bloqueada") >= 0 ? ' (vía bloqueada)' : "") + '</li></ul><p class="sr-pz">El tiempo simulado mide cuánto tardó el paciente en recibir cada acción; el tiempo real, cuánto pensaste.</p>';
      var F = fuentesCaso();
      var G = (flojo ? '<p>Tu eje más bajo en este caso fue «' + esc(flojo.nombre) + '» (' + flojo.pct + ' %). Repasa las decisiones de ese eje en la sección B.</p>' : "") + (rec ? '<p>Siguiente caso sugerido: <a href="#/serums/' + esc(rec.caso) + '">' + esc(por(datos.casos, rec.caso).titulo) + '</a>. ' + esc(rec.motivo) + '</p>' : "");
      var H = '<p>Estado de publicación: <b>' + esc(caso.estado_publicacion) + '</b>. Este caso no ha sido validado por un especialista; trátalo como material de estudio y confirma siempre con la norma vigente.</p>';
      cont.innerHTML = '<div class="sr sr--informe"><nav class="gh-migas" aria-label="Ruta"><a href="#/serums">Misión SERUMS</a><span aria-hidden="true">›</span><span aria-current="page">Informe del caso ' + caso.numero + '</span></nav><h1 tabindex="-1" id="srInf">Informe: ' + esc(caso.titulo) + '</h1><p class="gd-aviso" role="note">' + esc(AVISO) + '</p>' +
        sec("A", "Resultado", A) + sec("B", "Tus decisiones", B) + sec("C", "Errores por tipo", C) + sec("D", "Recursos e inventario", D) + sec("E", "Referencia y tiempos", E) + sec("F", "Normativa y vigencia", F) + sec("G", "Cómo mejorar", G) + sec("H", "Estado de validación", H) +
        '<p class="sr-fin"><a class="sr-btn" href="#/serums">Volver a la posta</a><button class="sr-btn sr-btn--claro" type="button" id="srRei">Reintentar el caso</button></p></div>';
      cont.querySelector("#srRei").addEventListener("click", function () { GD().ls(K_SES + ":" + caso.id, null); e = Nn.iniciar(caso, posta(), Date.now()); persistir(); aviso = ""; tab = "paciente"; pintar(); });
      var h = cont.querySelector("#srInf"); if (h) h.focus();
    }
    pintar();
  }

  function supervisor(q, salida, caso, datos) {
    salida.innerHTML = '<p class="sr-pz">Buscando…</p>';
    cargarIndice().then(function (ind) {
      var docs = (caso.evidencia || []).length ? caso.evidencia : null;
      if (!docs) { salida.innerHTML = '<p class="sr-pz">Este caso no tiene fuentes indexadas. No puedo citar documentos para esta consulta.</p>'; return; }
      var r = N().buscar(ind, q, 3, docs);
      if (!r.length) { salida.innerHTML = '<p>No encontré fragmentos relacionados en las fuentes de este caso. Prueba con otras palabras.</p>'; return; }
      salida.innerHTML = '<ul class="sr-fus">' + r.map(function (x) {
        var d = por(datos.evidencia.fuentes, x.doc);
        return '<li class="sr-fu"><p class="sr-fu__e sr-fu__e--ok">' + esc(d ? d.estado : "") + '</p><h4>' + esc(d ? d.numero : x.doc) + ' · página ' + x.pagina + '</h4><blockquote>' + esc(x.texto) + '</blockquote></li>';
      }).join("") + '</ul><p class="sr-pz">Fragmentos textuales del documento; confirma el contexto en la fuente completa.</p>';
    }).catch(function () { salida.innerHTML = '<p class="sr-pz">No se pudo cargar el índice documental. Revisa tu conexión.</p>'; });
  }

  /* ---------- entrada ---------- */
  function montar(cont, arg) {
    cont.innerHTML = '<div class="app-loading" role="status"><span>Cargando la Misión SERUMS…</span></div>';
    asegurarDatos().then(function () {
      var datos = raiz.MQP_SERUMS;
      if (arg) {
        var c = por(datos.casos, arg);
        if (!c) { cont.innerHTML = '<p>No se encontró el caso. <a href="#/serums">Volver a la posta</a></p>'; return; }
        jugar(cont, c, datos);
      } else {
        if (detener) detener();
        portada(cont, datos);
        if (!introVista()) intro();
      }
    }, function () { cont.innerHTML = '<p class="muted">No se pudo cargar la Misión SERUMS. Revisa tu conexión e inténtalo de nuevo.</p>'; });
  }

  M.serums = { montar: montar, asegurarDatos: asegurarDatos, intro: intro, AVISO: AVISO };
})(typeof window !== "undefined" ? window : this);
