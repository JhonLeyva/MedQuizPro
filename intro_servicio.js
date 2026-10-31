/* MedQuizPlus · introducciones cinematográficas de los servicios de «Sobrevive a la Guardia»: Emergencias, UCI y Consulta externa.
   Cada una es una foto a pantalla completa con un lienzo encima que dibuja, en las coordenadas de la imagen (1536×1024, «cover»), lo que se mueve:
   · Emergencias: el monitor y el desfibrilador muestran una fibrilación auricular con respuesta ventricular rápida, constante, con sus signos vitales; el pitido suena en cada onda R.
   · UCI: el monitor (ECG, pletismografía, respiración y capnografía, con sus cifras) y la pantalla del ventilador siguen el pitido del monitor y la respiración del audio.
   · Consulta: luz de la ventana, brillo del negatoscopio y motas de polvo (no hay monitores en la imagen).
   El tema de 30 s de cada servicio (guardia/audio/*.mp3, generado con tools/guardia_audio.py) es sintético y periódico: se repite sin cortes y las animaciones usan los mismos instantes.
   Con «reducir movimiento» solo se dibuja un fotograma. Las imágenes son ilustraciones generadas con IA; los monitores y la música son decorativos, sin valor clínico. */
(function (raiz) {
  "use strict";
  var M = raiz.MQP || (raiz.MQP = {});
  var SRC = (document.currentScript && document.currentScript.src) || "", BASE = SRC.replace(/intro_servicio\.js(\?.*)?$/, ""), VER = (SRC.split("?")[1] || "");
  var IW = 1536, IH = 1024, CICLO = 30;
  var SERVICIOS = {
    emergencias: { imagen: "guardia/portadas/intro-emergencias.webp", audio: "guardia/audio/emergencias.mp3", foco: 0.72, tono: "rojo", kicker: "Emergencias", titulo: "Cada segundo cuenta", boton: "Entrar a la guardia",
      texto: "La guardia no espera: reconoce, prioriza y actúa. Toma decisiones bajo presión y aprende de cada una con un informe completo.",
      nota: "Ilustración generada con IA. Los monitores y la música son decorativos y no tienen valor clínico." },
    uci: { imagen: "guardia/portadas/intro-uci.webp", audio: "guardia/audio/uci.mp3", foco: 0.72, tono: "indigo", kicker: "Cuidados críticos", titulo: "Piensa antes de cada ajuste", boton: "Pasar a la UCI",
      texto: "Ventilador, monitores y fármacos: cada decisión cambia el rumbo de un paciente crítico. Razona, decide y revisa tu razonamiento.",
      nota: "Ilustración generada con IA. Los monitores y la música son decorativos y no tienen valor clínico." },
    consulta: { imagen: "guardia/portadas/intro-consulta.webp", audio: "guardia/audio/consulta.mp3", foco: 0.5, tono: "azul", kicker: "Consulta externa", titulo: "Escucha, examina, razona", boton: "Comenzar la consulta",
      texto: "Una buena consulta empieza con una buena historia clínica. Pregunta, explora, pide solo lo necesario y decide con tu paciente.",
      nota: "Ilustración generada con IA. La música es decorativa y no tiene valor clínico." }
  };

  /* ---------- funciones de onda (tiempo en segundos del ciclo de 30 s) ---------- */
  function G(x, s) { return Math.exp(-(x / s) * (x / s)); }
  function mod(a, b) { return ((a % b) + b) % b; }
  function ruidoRapido(t) { var x = Math.sin(t * 91.7) * 43758.5453; return (x - Math.floor(x)) * 2 - 1; }
  function qrs(d) { return 0.13 * G(d + 0.16, 0.03) - 0.12 * G(d + 0.025, 0.008) + 1.0 * G(d, 0.011) - 0.22 * G(d - 0.025, 0.009) + 0.26 * G(d - 0.22, 0.05); }   // d: segundos desde el latido
  function sinusal(tt, periodo, t0) { var d = mod(tt - t0 + periodo / 2, periodo) - periodo / 2; return qrs(d); }
  /* Emergencias: fibrilación auricular con respuesta ventricular rápida, constante. Rasgos electrocardiográficos (guías ESC 2020 y ACC/AHA/ACCP/HRS 2023): intervalos R-R irregularmente
     irregulares, ausencia de ondas P definidas y actividad auricular caótica (ondas f de 350–600 /min, de baja amplitud); QRS estrecho; en el pulso, amplitud variable (déficit de pulso:
     los latidos con R-R corto bombean menos). Los R-R son los de tools/guardia_audio.py (RR_FA, 72 latidos que suman 30 s, media 144 /min) y el pitido suena en cada onda R. */
  var RR_FA = [0.321, 0.363, 0.414, 0.282, 0.609, 0.295, 0.422, 0.438, 0.303, 0.34, 0.375, 0.514, 0.282, 0.288, 0.42, 0.262, 0.577, 0.467, 0.347, 0.515, 0.608, 0.412, 0.417, 0.396, 0.507, 0.311, 0.498, 0.316, 0.281, 0.569, 0.429, 0.446, 0.445, 0.321, 0.432, 0.576, 0.569, 0.31, 0.395, 0.52, 0.31, 0.589, 0.336, 0.302, 0.304, 0.288, 0.401, 0.545, 0.361, 0.443, 0.596, 0.575, 0.27, 0.342, 0.465, 0.396, 0.345, 0.561, 0.556, 0.445, 0.495, 0.288, 0.35, 0.326, 0.447, 0.466, 0.527, 0.443, 0.307, 0.399, 0.522, 0.408];
  var TR = (function () { var a = [0], c = 0; for (var i = 0; i < RR_FA.length - 1; i++) { c += RR_FA[i]; a.push(c); } return a; })();   // instante de cada onda R
  function latidoCerca(t) {   // índice del latido más cercano y distancia (s) con signo
    t = mod(t, CICLO); var lo = 0, hi = TR.length - 1; while (lo < hi) { var m = (lo + hi + 1) >> 1; if (TR[m] <= t) lo = m; else hi = m - 1; }
    var k2 = (lo + 1) % TR.length, t2 = lo + 1 >= TR.length ? CICLO + TR[0] : TR[k2], d1 = t - TR[lo], d2 = t - t2; return Math.abs(d1) <= Math.abs(d2) ? { k: lo, d: d1 } : { k: k2, d: d2 };
  }
  var FREC_F = [[5.9, 0.045, 0.3], [7.3, 0.04, 1.7], [8.1, 0.035, 2.9], [9.2, 0.03, 4.4], [6.6, 0.04, 5.6]];   // frecuencias enteras en 30 s: la onda es periódica
  function ondaFA(t) {
    var h = latidoCerca(t), amp = 0.82 + 0.22 * mod(Math.sin(h.k * 12.9898) * 43758.5453, 1), d = h.d, y = amp * (1.0 * G(d, 0.010) - 0.16 * G(d + 0.018, 0.007) - 0.22 * G(d - 0.02, 0.008)) + 0.1 * G(d - 0.17, 0.045);
    var f = 0; for (var i = 0; i < FREC_F.length; i++) f += FREC_F[i][1] * Math.sin(2 * Math.PI * FREC_F[i][0] * t + FREC_F[i][2]);
    return y + f * (0.8 + 0.4 * Math.sin(2 * Math.PI * 0.7 * t));
  }
  function ondaPletFA(t) {
    var y = 0, h = latidoCerca(t); for (var j = -1; j <= 1; j++) { var k = (h.k + j + TR.length) % TR.length, rr = RR_FA[(k - 1 + RR_FA.length) % RR_FA.length], a = Math.max(0.25, Math.min(1, 0.25 + (rr - 0.27) * 2.2)), d = h.d - (j === 1 ? RR_FA[h.k] : j === -1 ? -RR_FA[(h.k - 1 + RR_FA.length) % RR_FA.length] : 0); y += a * (0.9 * G(d - 0.2, 0.07) + 0.2 * G(d - 0.36, 0.08)); }
    return y - 0.25;
  }
  function frecuenciaFA(t) { var k = latidoCerca(t).k, s6 = 0; for (var i = 0; i < 6; i++) s6 += RR_FA[(k - i + 72 * 3) % RR_FA.length]; return Math.round(60 / (s6 / 6)); }
  function ondaRespFA(t) { return Math.sin(2 * Math.PI * t / 2.5); }

  /* UCI: latido cada 60/78 s, respiración cada 30/9 s */
  var LAT = 60 / 78, RESP = 30 / 9;
  function ondaEcgUci(t) { return sinusal(t, LAT, 0); }
  function ondaPleth(t) { var d = mod(t + LAT / 2, LAT) - LAT / 2; return 0.9 * G(d - 0.26, 0.1) + 0.28 * G(d - 0.5, 0.09) - 0.15; }
  function ondaResp(t) { var x = mod(t, RESP) / RESP; return x < 0.39 ? Math.sin(Math.PI / 2 * x / 0.39) : Math.exp(-(x - 0.39) / 0.2); }
  function ondaCapno(t) { var x = mod(t, RESP) / RESP; if (x < 0.42) return 0.02; if (x < 0.5) return (x - 0.42) / 0.08 * 0.9; return x < 0.93 ? 0.9 + (x - 0.5) * 0.12 : Math.max(0.02, 0.95 * (1 - (x - 0.93) / 0.05)); }
  function ondaFlujo(t) { var x = mod(t, RESP) / RESP; return x < 0.39 ? 0.8 * Math.sin(Math.PI * x / 0.39) : -0.55 * Math.exp(-(x - 0.39) / 0.12) * (x < 0.8 ? 1 : 0); }

  /* ---------- sonido: reproduce el tema en bucle sin cortes (el audio es periódico, cualquier ventana de 30 s enlaza) ---------- */
  function sonido(url) {
    var AC = raiz.AudioContext || raiz.webkitAudioContext, ctx = null, gan = null, fuente = null, buf = null, inicio = 0, mudo = false, vivo = true, carga = null;
    function asegurar() {
      if (!AC) return Promise.reject(new Error("sin audio"));
      if (!ctx) { ctx = new AC(); gan = ctx.createGain(); gan.gain.value = 0; gan.connect(ctx.destination); }
      if (buf) return Promise.resolve();
      if (!carga) carga = fetch(BASE + url + (VER ? "?" + VER : "")).then(function (r) { if (!r.ok) throw new Error("audio"); return r.arrayBuffer(); }).then(function (b) { return new Promise(function (ok, mal) { ctx.decodeAudioData(b, ok, mal); }); }).then(function (b) { buf = b; }).catch(function (e) { carga = null; throw e; });
      return carga;
    }
    function nivel(v, seg) { gan.gain.cancelScheduledValues(ctx.currentTime); gan.gain.setValueAtTime(gan.gain.value, ctx.currentTime); gan.gain.linearRampToValueAtTime(v, ctx.currentTime + seg); }
    return {
      iniciar: function () {
        return asegurar().then(function () {
          if (!vivo) return false;
          return (ctx.state === "running" ? Promise.resolve() : ctx.resume()).then(function () {
            if (ctx.state !== "running" || !vivo) return false;
            if (!fuente) { fuente = ctx.createBufferSource(); fuente.buffer = buf; fuente.loop = true; fuente.loopStart = 0; fuente.loopEnd = Math.min(CICLO, buf.duration); fuente.connect(gan); inicio = ctx.currentTime; fuente.start(0); }
            nivel(mudo ? 0 : 0.8, 1.2); return true;
          });
        }).catch(function () { return false; });
      },
      fase: function () { return ctx && fuente && ctx.state === "running" ? (ctx.currentTime - inicio) % CICLO : null; },
      silenciar: function (m) { mudo = m; if (ctx && gan) nivel(m ? 0 : 0.8, 0.4); },
      detener: function () { vivo = false; if (!ctx) return; try { nivel(0, 0.4); } catch (e) {} var c = ctx; setTimeout(function () { try { if (fuente) fuente.stop(); c.close(); } catch (e) {} }, 550); }
    };
  }

  /* ---------- escena: lienzo sobre la foto, en coordenadas de la imagen ---------- */
  function escena(clave, caja, lienzo, snd) {
    var S = SERVICIOS[clave], g = lienzo.getContext("2d"), W = 0, H = 0, s = 1, ox = 0, oy = 0, DPR = Math.min(1.5, raiz.devicePixelRatio || 1), mov = true, t0 = performance.now(), activo = true, raf = 0, ult = performance.now(), motas = [];
    try { mov = !raiz.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
    function ajustar() {
      W = caja.clientWidth; H = caja.clientHeight; lienzo.width = Math.round(W * DPR); lienzo.height = Math.round(H * DPR);
      s = Math.max(W / IW, H / IH); ox = (W - IW * s) * S.foco; oy = (H - IH * s) * 0.5;
      if (clave === "consulta" && !motas.length) for (var i = 0; i < 70; i++) motas.push({ x: Math.random() * IW, y: Math.random() * IH, r: 0.8 + Math.random() * 2, v: 4 + Math.random() * 10, a: 0.2 + Math.random() * 0.5, f: Math.random() * 6 });
    }
    function p(x, y) { return [ox + x * s, oy + y * s]; }
    function caja2(x0, y0, x1, y1, color) { var a = p(x0, y0), b = p(x1, y1); g.fillStyle = color; g.fillRect(a[0], a[1], b[0] - a[0], b[1] - a[1]); }
    function linea(fn, t, x0, x1, yc, amp, ventana, color, ancho, muestras, brillo) {
      g.beginPath(); for (var i = 0; i <= muestras; i++) { var u = i / muestras, c = p(x0 + (x1 - x0) * u, yc - fn(t - ventana + ventana * u) * amp); i ? g.lineTo(c[0], c[1]) : g.moveTo(c[0], c[1]); }
      g.lineJoin = "round"; g.lineWidth = Math.max(1, ancho * s); g.strokeStyle = color; if (brillo) { g.shadowColor = color; g.shadowBlur = brillo * s; } g.stroke(); g.shadowBlur = 0;
    }
    function texto(txt, x, y, tam, color, alin, peso) { var c = p(x, y); g.font = (peso || "700") + " " + Math.max(6, tam * s) + "px Arial, Helvetica, sans-serif"; g.fillStyle = color; g.textAlign = alin || "left"; g.textBaseline = "middle"; g.fillText(txt, c[0], c[1]); }
    function borde(x0, y0, x1, y1, color, ancho) { var a = p(x0, y0), b = p(x1, y1); g.lineWidth = ancho * s; g.strokeStyle = color; g.strokeRect(a[0], a[1], b[0] - a[0], b[1] - a[1]); }

    /* ---- Emergencias ----
       Todo el monitor se dibuja sobre el cuadrilátero del cristal (en perspectiva), con la misma correspondencia bilineal que la UCI. */
    var QE = [[1262, 157], [1495, 150], [1491, 316], [1261, 317]];   // TL, TR, BR, BL del cristal del monitor, en píxeles de la imagen
    function dibujarEmerg(t) {
      var alarma = mod(t, 1) < 0.5 ? 1 : 0, hr = frecuenciaFA(t);
      g.globalCompositeOperation = "source-over";
      function poli(Q, uv, color) { g.beginPath(); uv.forEach(function (q, i) { var c = pq(Q, q[0], q[1]); i ? g.lineTo(c[0], c[1]) : g.moveTo(c[0], c[1]); }); g.closePath(); g.fillStyle = color; g.fill(); }
      poli(QE, [[0.003, 0.006], [0.997, 0.006], [0.997, 0.994], [0.003, 0.994]], "#03060d");                                      // cristal
      var gh = g.createLinearGradient.apply(g, pq(QE, 0, 0).concat(pq(QE, 1, 0))); gh.addColorStop(0, "#2a68c4"); gh.addColorStop(1, "#0e2d66");
      poli(QE, [[0.003, 0.006], [0.997, 0.006], [0.997, 0.092], [0.003, 0.092]], gh);                                              // barra superior
      textoQ(QE, "CAMA 4", 0.025, 0.05, 8.5, "#ffffff", "left"); textoQ(QE, "21:47", 0.975, 0.05, 8.5, "#ffffff", "right");
      if (alarma) { poli(QE, [[0.28, 0.012], [0.70, 0.012], [0.70, 0.082], [0.28, 0.082]], "#d62828"); textoQ(QE, "FC ALTA", 0.49, 0.047, 9.5, "#ffffff", "center", "800"); }
      var U0 = 0.03, U1 = 0.715;
      [0.47, 0.70].forEach(function (v) { var a1 = pq(QE, U0, v), b1 = pq(QE, U1, v); g.beginPath(); g.moveTo(a1[0], a1[1]); g.lineTo(b1[0], b1[1]); g.lineWidth = Math.max(0.6, 0.7 * s); g.strokeStyle = "rgba(160,190,230,.16)"; g.stroke(); });
      trazoQ(QE, ondaFA, t, U0, U1, 0.285, 0.13, 3.4, "#4dff91", 1.7, 330, 5);
      trazoQ(QE, ondaPletFA, t, U0, U1, 0.64, 0.12, 3.4, "#5fd0ff", 1.6, 330, 4);
      trazoQ(QE, ondaRespFA, t, U0, U1, 0.81, 0.07, 6.0, "#ffffff", 1.4, 200, 3);
      textoQ(QE, "II", 0.04, 0.125, 8.5, "#4dff91", "left"); textoQ(QE, "Pleth", 0.04, 0.495, 8.5, "#5fd0ff", "left"); textoQ(QE, "Resp", 0.04, 0.725, 8.5, "#ffffff", "left");
      textoQ(QE, "FC", 0.745, 0.15, 8, "#4dff91", "left"); textoQ(QE, String(hr), 0.885, 0.25, 34, "#4dff91", "center", "800");
      textoQ(QE, "SpO₂", 0.745, 0.395, 8, "#5fd0ff", "left"); textoQ(QE, "93", 0.885, 0.475, 28, "#5fd0ff", "center", "800");
      textoQ(QE, "PNI", 0.745, 0.60, 8, "#ffffff", "left"); textoQ(QE, "96/58", 0.9, 0.655, 16, "#ffffff", "center", "700"); textoQ(QE, "(71)", 0.9, 0.735, 10, "#ffffff", "center", "600");
      textoQ(QE, "FR", 0.745, 0.835, 8, "#ffffff", "left"); textoQ(QE, "24", 0.885, 0.845, 18, "#ffffff", "center", "700");
      poli(QE, [[0.003, 0.925], [0.997, 0.925], [0.997, 0.994], [0.003, 0.994]], "#0d3a8e");                                       // barra inferior
      [0.04, 0.14, 0.24, 0.34, 0.44, 0.9].forEach(function (u) { poli(QE, [[u, 0.94], [u + 0.065, 0.94], [u + 0.065, 0.98], [u, 0.98]], "rgba(215,230,255,.55)"); });
      if (alarma) { g.beginPath(); [[0.003, 0.006], [0.997, 0.006], [0.997, 0.994], [0.003, 0.994]].forEach(function (uv, i) { var c = pq(QE, uv[0], uv[1]); i ? g.lineTo(c[0], c[1]) : g.moveTo(c[0], c[1]); }); g.closePath(); g.lineWidth = 2.2 * s; g.strokeStyle = "rgba(255,70,70,.8)"; g.stroke(); }
      /* desfibrilador (pantalla pequeña a la izquierda): misma fibrilación con marcas de sincronía sobre cada R (cardioversión sincronizada) */
      caja2(78, 290, 174, 346, "#050a0c");
      linea(ondaFA, t, 82, 170, 320, 15, 3.0, "#7dffb0", 1.3, 120, 3);
      for (var i = 0; i < TR.length; i++) { var dt = mod(t - TR[i] + CICLO / 2, CICLO) - CICLO / 2; if (dt >= 0 && dt <= 3.0) { var c2 = p(82 + (170 - 82) * (1 - dt / 3.0), 300); g.fillStyle = "#ffffff"; g.beginPath(); g.moveTo(c2[0], c2[1] - 3 * s); g.lineTo(c2[0] - 2.4 * s, c2[1] - 7 * s); g.lineTo(c2[0] + 2.4 * s, c2[1] - 7 * s); g.closePath(); g.fill(); } }
      texto("SINC", 126, 296, 7.5, "#ffd35a", "center"); texto("FA", 90, 342, 7, "#9fb2d6", "left");
      g.globalCompositeOperation = "screen";
      if (alarma) { g.fillStyle = "rgba(255,40,40,0.035)"; g.fillRect(0, 0, W, H); }
      g.globalCompositeOperation = "source-over";
    }

    /* ---- UCI ----
       La pantalla del monitor es un cuadrilátero en perspectiva (el borde superior sube hacia la derecha): se dibuja con una correspondencia bilineal (u, v) → imagen
       y los textos con la base local en cada punto, para que todo quede dentro del cristal y siga su inclinación. */
    var QM = [[1140, 142], [1376, 96], [1377, 317], [1144, 332]];   // TL, TR, BR, BL del cristal del monitor, en píxeles de la imagen
    function bil(Q, u, v) { var a = Q[0], b2 = Q[1], c = Q[2], d = Q[3]; return [(1 - u) * (1 - v) * a[0] + u * (1 - v) * b2[0] + u * v * c[0] + (1 - u) * v * d[0], (1 - u) * (1 - v) * a[1] + u * (1 - v) * b2[1] + u * v * c[1] + (1 - u) * v * d[1]]; }
    function pq(Q, u, v) { var q = bil(Q, u, v); return p(q[0], q[1]); }
    function trazoQ(Q, fn, t, u0, u1, vc, amp, ventana, color, ancho, muestras, brillo, base) {
      g.beginPath(); for (var i = 0; i <= muestras; i++) { var u = u0 + (u1 - u0) * i / muestras, y = fn(t - ventana + ventana * (u - u0) / (u1 - u0)), c = pq(Q, u, base ? vc - y * amp : vc - y * amp); i ? g.lineTo(c[0], c[1]) : g.moveTo(c[0], c[1]); }
      g.lineJoin = "round"; g.lineWidth = Math.max(1, ancho * s); g.strokeStyle = color; if (brillo) { g.shadowColor = color; g.shadowBlur = brillo * s; } g.stroke(); g.shadowBlur = 0;
    }
    function textoQ(Q, txt, u, v, tam, color, alin, peso) {
      var C = pq(Q, u, v), A = pq(Q, u + 0.01, v), B = pq(Q, u, v + 0.01), W0 = Math.hypot(Q[1][0] - Q[0][0], Q[1][1] - Q[0][1]), H0 = Math.hypot(Q[3][0] - Q[0][0], Q[3][1] - Q[0][1]);
      g.save(); g.transform((A[0] - C[0]) * 100 / W0, (A[1] - C[1]) * 100 / W0, (B[0] - C[0]) * 100 / H0, (B[1] - C[1]) * 100 / H0, C[0], C[1]);
      g.font = (peso || "700") + " " + tam + "px Arial, Helvetica, sans-serif"; g.fillStyle = color; g.textAlign = alin || "left"; g.textBaseline = "middle"; g.fillText(txt, 0, 0); g.restore();
    }
    function dibujarUci(t) {
      var latido = Math.exp(-mod(t, LAT) * 5);
      g.globalCompositeOperation = "source-over";
      g.beginPath(); [[0.004, 0.012], [0.996, 0.012], [0.996, 0.988], [0.004, 0.988]].forEach(function (uv, i) { var c = pq(QM, uv[0], uv[1]); i ? g.lineTo(c[0], c[1]) : g.moveTo(c[0], c[1]); }); g.closePath(); g.fillStyle = "#030813"; g.fill();   // cristal
      var U0 = 0.035, U1 = 0.655;
      trazoQ(QM, ondaEcgUci, t, U0, U1, 0.20, 0.085, 4.2, "#3be26f", 1.7, 200, 5);
      trazoQ(QM, ondaPleth, t, U0, U1, 0.45, 0.07, 4.2, "#ecd44a", 1.6, 200, 4);
      trazoQ(QM, ondaResp, t, U0, U1, 0.66, 0.062, 7.0, "#4aa6ff", 1.6, 200, 4);
      trazoQ(QM, function (x) { return ondaCapno(x); }, t, U0, U1, 0.935, 0.085, 7.0, "#5fd0ff", 1.5, 200, 4);
      g.fillStyle = "rgba(160,190,230,.18)"; [0.37, 0.57, 0.77].forEach(function (v) { var a = pq(QM, U0, v), b2 = pq(QM, U1, v); g.beginPath(); g.moveTo(a[0], a[1]); g.lineTo(b2[0], b2[1]); g.lineWidth = Math.max(0.6, 0.7 * s); g.strokeStyle = "rgba(160,190,230,.18)"; g.stroke(); });
      textoQ(QM, "II", 0.04, 0.065, 9, "#3be26f", "left"); textoQ(QM, "Pleth", 0.04, 0.325, 9, "#ecd44a", "left"); textoQ(QM, "Resp", 0.04, 0.545, 9, "#4aa6ff", "left"); textoQ(QM, "CO₂", 0.04, 0.775, 9, "#5fd0ff", "left");
      textoQ(QM, "FC", 0.685, 0.065, 9, "#3be26f", "left"); textoQ(QM, "78", 0.84, 0.165, 44, "#3be26f", "center", "800");
      textoQ(QM, "SpO₂", 0.685, 0.31, 9, "#ff4d4d", "left"); textoQ(QM, mod(t, 20) < 14 ? "96" : "97", 0.84, 0.41, 40, "#ff4d4d", "center", "800");
      textoQ(QM, "FR", 0.685, 0.555, 9, "#ffd84a", "left"); textoQ(QM, "18", 0.84, 0.645, 36, "#ffd84a", "center", "800");
      textoQ(QM, "105/62", 0.84, 0.825, 19, "#ffffff", "center", "700"); textoQ(QM, "(76)", 0.84, 0.925, 13, "#ffffff", "center", "600");
      /* pantalla del ventilador: afín al paralelogramo de la imagen */
      var A = p(1427.5, 427.5), B = p(1517.5, 425), C = p(1417.5, 532.5);
      g.save(); g.transform((B[0] - A[0]) / 300, (B[1] - A[1]) / 300, (C[0] - A[0]) / 200, (C[1] - A[1]) / 200, A[0], A[1]);
      g.fillStyle = "#061236"; g.fillRect(0, 0, 300, 200);
      function onda(fn, y0, alto, color, ventana) { g.beginPath(); for (var k = 0; k <= 160; k++) { var uu = k / 160, vv = y0 - fn(t - ventana + ventana * uu) * alto; k ? g.lineTo(uu * 280 + 10, vv) : g.moveTo(uu * 280 + 10, vv); } g.lineWidth = 3.2; g.lineJoin = "round"; g.strokeStyle = color; g.shadowColor = color; g.shadowBlur = 6; g.stroke(); g.shadowBlur = 0; }
      onda(ondaResp, 88, 56, "#58b4ff", 10); onda(ondaFlujo, 150, 34, "#8fd0ff", 10);
      g.strokeStyle = "rgba(160,200,255,.35)"; g.lineWidth = 1.2; g.beginPath(); g.moveTo(10, 90); g.lineTo(290, 90); g.moveTo(10, 150); g.lineTo(290, 150); g.stroke();
      g.restore();
      g.globalCompositeOperation = "screen";
      var c0 = p(1262, 210), r0 = 150 * s, gr0 = g.createRadialGradient(c0[0], c0[1], 0, c0[0], c0[1], r0); gr0.addColorStop(0, "rgba(70,230,130," + (0.05 + 0.08 * latido) + ")"); gr0.addColorStop(1, "rgba(70,230,130,0)"); g.fillStyle = gr0; g.fillRect(c0[0] - r0, c0[1] - r0, r0 * 2, r0 * 2);
      g.globalCompositeOperation = "source-over";
    }

    /* ---- Consulta ---- */
    function dibujarConsulta(t, dt) {
      g.globalCompositeOperation = "screen";
      var pul = 0.5 + 0.5 * Math.sin(t * 2 * Math.PI / 7.5), c = p(180, 290), r = 260 * s, gr = g.createRadialGradient(c[0], c[1], 0, c[0], c[1], r);   // negatoscopio
      gr.addColorStop(0, "rgba(190,225,255," + (0.12 + 0.12 * pul) + ")"); gr.addColorStop(1, "rgba(190,225,255,0)"); g.fillStyle = gr; g.fillRect(c[0] - r, c[1] - r, r * 2, r * 2);
      for (var k = 0; k < 3; k++) {                                                                                                  // haces de luz de la ventana
        var a = p(520 + k * 36, 60), b = p(380 + k * 90, 640), gh = g.createLinearGradient(a[0], a[1], b[0], b[1]), al = 0.05 + 0.05 * Math.sin(t * 0.8 + k * 1.7); gh.addColorStop(0, "rgba(255,240,200," + al + ")"); gh.addColorStop(1, "rgba(255,240,200,0)");
        g.fillStyle = gh; g.beginPath(); var q1 = p(500 + k * 36, 60), q2 = p(590 + k * 36, 60), q3 = p(480 + k * 90, 700), q4 = p(300 + k * 90, 700); g.moveTo(q1[0], q1[1]); g.lineTo(q2[0], q2[1]); g.lineTo(q3[0], q3[1]); g.lineTo(q4[0], q4[1]); g.closePath(); g.fill();
      }
      for (var i = 0; i < motas.length; i++) { var m = motas[i]; m.y -= m.v * dt; m.x += Math.sin(t * 0.7 + m.f) * 6 * dt; if (m.y < -10) { m.y = IH + 10; m.x = Math.random() * IW; } var q = p(m.x, m.y); g.fillStyle = "rgba(255,244,220," + (m.a * (0.6 + 0.4 * Math.sin(t * 1.3 + m.f))) + ")"; g.beginPath(); g.arc(q[0], q[1], m.r * s, 0, 6.2832); g.fill(); }
      g.globalCompositeOperation = "source-over";
    }

    function dibujar(t, dt) { g.setTransform(DPR, 0, 0, DPR, 0, 0); g.clearRect(0, 0, W, H); if (clave === "emergencias") dibujarEmerg(t, dt); else if (clave === "uci") dibujarUci(t, dt); else dibujarConsulta(t, dt); }
    function fase() { var f = snd.fase(); return f == null ? mod((performance.now() - t0) / 1000, CICLO) : f; }
    function bucle(ahora) { if (!activo) return; raf = requestAnimationFrame(bucle); if (document.hidden) { ult = ahora; return; } var dt = Math.min(0.05, (ahora - ult) / 1000); ult = ahora; dibujar(fase(), dt); }
    ajustar(); var aj = function () { ajustar(); if (!mov) dibujar(clave === "emergencias" ? 20 : 5, 0.016); }; raiz.addEventListener("resize", aj);
    if (mov) raf = requestAnimationFrame(bucle); else dibujar(clave === "emergencias" ? 20 : 5, 0.016);
    return function () { activo = false; cancelAnimationFrame(raf); raiz.removeEventListener("resize", aj); };
  }

  /* botón de sonido + reproducción en bucle para otra introducción (p. ej. la principal de «Sobrevive a la Guardia»); devuelve { detener } */
  function anexarSonido(caja, url, clase) {
    var snd = sonido(url), mudo = false, btn = document.createElement("button"); btn.type = "button"; btn.className = clase || "is-intro__snd"; btn.setAttribute("data-sonido", ""); btn.setAttribute("aria-pressed", "true"); btn.textContent = "Sonido activado"; caja.appendChild(btn);
    function etiqueta(txt) { btn.textContent = txt; btn.setAttribute("aria-pressed", String(!mudo && txt === "Sonido activado")); }
    function arrancar() { snd.iniciar().then(function (suena) { if (suena) etiqueta(mudo ? "Sonido silenciado" : "Sonido activado"); else { etiqueta("Activar sonido"); caja.addEventListener("pointerdown", reintento, { once: true }); caja.addEventListener("keydown", reintento, { once: true }); } }); }
    function reintento() { if (!mudo) arrancar(); }
    btn.addEventListener("click", function (ev) { ev.stopPropagation(); if (btn.textContent === "Activar sonido") { mudo = false; arrancar(); return; } mudo = !mudo; snd.silenciar(mudo); etiqueta(mudo ? "Sonido silenciado" : "Sonido activado"); });
    arrancar(); return { detener: function () { snd.detener(); if (btn.parentNode) btn.parentNode.removeChild(btn); } };
  }
  function esc(t) { return String(t).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  var VISTAS = {};   // respaldo en memoria si sessionStorage no está disponible
  /* Se muestra la primera vez que se abre cada módulo en la sesión del navegador (sessionStorage: sobrevive a recargar y a moverse por la plataforma). Vuelve a mostrarse al cerrar la
     ventana o la pestaña, y al cerrar sesión (app.js borra estas marcas). */
  function vista(clave) { try { return sessionStorage.getItem("mqp_intro_" + clave) === "1"; } catch (e) { return !!VISTAS[clave]; } }
  function marcar(clave) { VISTAS[clave] = true; try { sessionStorage.setItem("mqp_intro_" + clave, "1"); } catch (e) {} }

  function mostrar(clave, opc) {
    var S = SERVICIOS[clave]; if (!S) return;
    Array.prototype.forEach.call(document.querySelectorAll("dialog.is-intro"), function (x) { x.remove(); });
    var d = document.createElement("dialog"); d.className = "is-intro is-intro--" + S.tono; d.setAttribute("aria-labelledby", "isT"); d.setAttribute("data-servicio", clave);
    d.innerHTML = '<div class="is-intro__escena"><img class="is-intro__img" src="' + BASE + S.imagen + '" alt="" width="1536" height="1024" fetchpriority="high" style="object-position:' + Math.round(S.foco * 100) + '% 50%"><canvas class="is-intro__lienzo" aria-hidden="true"></canvas></div><div class="is-intro__vel"></div>' +
      '<button type="button" class="is-intro__snd" data-sonido aria-pressed="true">Sonido activado</button>' +
      '<div class="is-intro__c"><p class="is-intro__k">' + esc(S.kicker) + '</p><h2 id="isT">' + esc(S.titulo) + '</h2><p>' + esc(S.texto) + '</p><button type="button" class="is-btn" data-entrar>' + esc(S.boton) + '</button><button type="button" class="is-intro__o" data-omitir>Omitir</button><p class="is-intro__nota">' + esc(S.nota) + '</p></div>';
    document.body.appendChild(d);
    var snd = sonido(S.audio), parar = null, mudo = false, btn = d.querySelector("[data-sonido]");
    function etiqueta(txt) { btn.textContent = txt; btn.setAttribute("aria-pressed", String(!mudo && txt === "Sonido activado")); }
    function arrancar() { snd.iniciar().then(function (suena) { if (suena) etiqueta(mudo ? "Sonido silenciado" : "Sonido activado"); else { etiqueta("Activar sonido"); btn.setAttribute("aria-pressed", "false"); d.addEventListener("pointerdown", reintento, { once: true }); d.addEventListener("keydown", reintento, { once: true }); } }); }
    function reintento() { if (!mudo) arrancar(); }
    function cerrar(entrar) { if (parar) parar(); snd.detener(); try { d.close(); } catch (e) {} d.remove(); marcar(clave); if (opc && opc.alCerrar) opc.alCerrar(entrar); }
    btn.addEventListener("click", function () { if (btn.textContent === "Activar sonido") { mudo = false; arrancar(); return; } mudo = !mudo; snd.silenciar(mudo); etiqueta(mudo ? "Sonido silenciado" : "Sonido activado"); });
    d.querySelector("[data-entrar]").addEventListener("click", function () { cerrar(true); });
    d.querySelector("[data-omitir]").addEventListener("click", function () { cerrar(false); });
    d.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(false); });
    if (d.showModal) d.showModal(); else d.setAttribute("open", ""); d.querySelector("[data-entrar]").focus();
    parar = escena(clave, d.querySelector(".is-intro__escena"), d.querySelector(".is-intro__lienzo"), snd); arrancar();
  }
  /* aparece la primera vez que se abre cada servicio en la sesión del navegador; «Omitir» no guarda ninguna preferencia. La clave de localStorage solo la usan las pruebas automáticas. */
  function auto(clave) {
    var omitir = false; try { omitir = localStorage.getItem("mqp_guardia_intro_v1") === "omitir"; } catch (e) {}
    if (omitir || vista(clave) || document.querySelector("dialog.is-intro")) return;
    mostrar(clave);
  }
  M.introServicio = { mostrar: mostrar, auto: auto, vista: vista, marcar: marcar, anexarSonido: anexarSonido, SERVICIOS: SERVICIOS };
})(typeof window !== "undefined" ? window : this);
