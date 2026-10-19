/* MedQuizPlus · Rendimiento y plan de estudio
   Estadística descriptiva transparente sobre los resultados REALES del alumno. No hay modelo entrenado ni conversión a "nota ENAM":
   la escala del examen no está validada contra datos, así que solo se muestran % de aciertos, intervalos y prioridades explicadas. */
(function (raiz) {
  "use strict";

  var MIN_RESPUESTAS = 100;      // para hablar de una estimación a futuro
  var MIN_SIMULACROS = 2;
  var MIN_PREG_SIMULACRO = 20;   // un simulacro "cuenta" si tuvo al menos estas preguntas
  var DIA = 86400000;

  /* intervalo de Wilson al 95 % para una proporción */
  function wilson(ok, n) {
    if (!n) return { p: null, lo: 0, hi: 1 };
    var z = 1.96, p = ok / n, z2 = z * z, d = 1 + z2 / n;
    var c = (p + z2 / (2 * n)) / d, h = z * Math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / d;
    return { p: p, lo: Math.max(0, c - h), hi: Math.min(1, c + h) };
  }
  function pct(x) { return Math.round(x * 100); }

  /* preguntas: [{id, archivo, especialidad, tema}] · respuestas: {id: {ok, t}} · sesiones: [{tipo,total,respondidas,correctas,t}] */
  function calcular(preguntas, respuestas, sesiones, ahora) {
    ahora = ahora || Date.now();
    var porId = {}, areas = {}, totalBanco = 0;
    preguntas.forEach(function (q) {
      porId[q.id] = q; totalBanco++;
      var a = areas[q.archivo] || (areas[q.archivo] = { archivo: q.archivo, nombre: q.especialidad, total: 0, n: 0, ok: 0, ultimo: 0, temas: {} });
      a.total++;
    });
    var okG = 0, nG = 0;
    Object.keys(respuestas || {}).forEach(function (id) {
      var r = respuestas[id], q = porId[id]; if (!r || !q) return;
      var a = areas[q.archivo]; a.n++; nG++; if (r.ok) { a.ok++; okG++; }
      if (r.t > a.ultimo) a.ultimo = r.t;
      if (!r.ok) { var tm = q.tema || "(sin tema)"; var t = a.temas[tm] || (a.temas[tm] = { tema: tm, falladas: [], total: 0 }); t.falladas.push(id); }
    });
    preguntas.forEach(function (q) { var a = areas[q.archivo]; var tm = q.tema || "(sin tema)"; if (a.temas[tm]) a.temas[tm].total++; });

    var maxTam = 0; Object.keys(areas).forEach(function (k) { if (areas[k].total > maxTam) maxTam = areas[k].total; });
    var lista = Object.keys(areas).map(function (k) {
      var a = areas[k], w = wilson(a.ok, a.n);
      var media = (a.ok + 1) / (a.n + 2);                      // proporción con prior Beta(1,1): con pocos datos tiende a 50 %
      var dias = a.n ? (ahora - a.ultimo) / DIA : null;
      var need = 1 - media, relev = maxTam ? a.total / maxTam : 0, incert = w.hi - w.lo, rec = a.n ? Math.min(1, dias / 30) : 1;
      var score = 0.5 * need + 0.2 * relev + 0.15 * incert + 0.15 * rec;
      var motivos = [];
      if (a.n) motivos.push("Aciertas " + pct(a.ok / a.n) + " % (" + a.ok + " de " + a.n + ")" + (a.n < 10 ? ", con pocos datos todavía" : ""));
      else motivos.push("Aún no la has practicado");
      motivos.push("Pesa " + pct(a.total / totalBanco) + " % del banco (" + a.total + " preguntas)");
      if (a.n && dias >= 14) motivos.push("Hace " + Math.round(dias) + " días que no practicas esta especialidad");
      var temas = Object.keys(a.temas).map(function (t) { return a.temas[t]; }).filter(function (t) { return t.falladas.length; })
        .sort(function (x, y) { return y.falladas.length - x.falladas.length; }).slice(0, 3);
      var meta = a.n >= 5 && a.ok / a.n < 0.7
        ? "Meta: llegar a 70 % en tus próximas 10 respuestas de esta especialidad."
        : a.n ? "Meta: mantener 70 % o más y cubrir lo que falta (" + (a.total - a.n) + " preguntas sin responder)." : "Meta: responder tus primeras 10 preguntas para medir tu nivel.";
      return { archivo: a.archivo, nombre: a.nombre, total: a.total, n: a.n, ok: a.ok, pct: a.n ? pct(a.ok / a.n) : null, lo: pct(w.lo), hi: pct(w.hi),
        score: score, motivos: motivos, temas: temas, meta: meta, falladas: Object.keys(a.temas).reduce(function (s, t) { return s.concat(a.temas[t].falladas); }, []), ultimo: a.ultimo };
    }).sort(function (x, y) { return y.score - x.score; });

    /* simulacros: sesiones terminadas de tipo simulacro con suficientes preguntas */
    var sims = (sesiones || []).filter(function (s) { return s.tipo === "simulacro" && s.total >= MIN_PREG_SIMULACRO && s.respondidas > 0; })
      .sort(function (x, y) { return x.t - y.t; }).map(function (s) { return { t: s.t, titulo: s.titulo, total: s.total, ok: s.correctas, pct: pct(s.correctas / s.total) }; });
    var sOk = 0, sN = 0; sims.forEach(function (s) { sOk += s.ok; sN += s.total; });

    var suficiente = nG >= MIN_RESPUESTAS && sims.length >= MIN_SIMULACROS;
    var est = { suficiente: suficiente, faltan: [] };
    if (!suficiente) {
      if (nG < MIN_RESPUESTAS) est.faltan.push("responder " + (MIN_RESPUESTAS - nG) + " preguntas más (llevas " + nG + " de " + MIN_RESPUESTAS + ")");
      if (sims.length < MIN_SIMULACROS) est.faltan.push("terminar " + (MIN_SIMULACROS - sims.length) + " simulacro" + (MIN_SIMULACROS - sims.length === 1 ? "" : "s") + " más de al menos " + MIN_PREG_SIMULACRO + " preguntas");
    } else {
      var w2 = wilson(sOk, sN), mitad = Math.floor(sims.length / 2) || 1;
      var prom = function (a) { return a.reduce(function (s, x) { return s + x.pct; }, 0) / a.length; };
      est.rango = [pct(w2.lo), pct(w2.hi)]; est.centro = pct(w2.p);
      est.tendencia = Math.round(prom(sims.slice(-mitad)) - prom(sims.slice(0, mitad)));
    }
    var wg = wilson(okG, nG);
    return {
      global: { n: nG, ok: okG, pct: nG ? pct(okG / nG) : null, lo: pct(wg.lo), hi: pct(wg.hi), cobertura: totalBanco ? pct(nG / totalBanco) : 0 },
      simulacros: sims, estimacion: est, areas: lista, plan: lista.slice(0, 5)
    };
  }

  var API = { calcular: calcular, wilson: wilson, MIN_RESPUESTAS: MIN_RESPUESTAS, MIN_SIMULACROS: MIN_SIMULACROS };
  if (typeof module !== "undefined" && module.exports) module.exports = API;
  else (raiz.MQP = raiz.MQP || {}).rendimiento = API;
})(typeof window !== "undefined" ? window : this);
