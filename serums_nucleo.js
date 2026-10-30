/* MedQuizPlus · Misión SERUMS · núcleo puro (sin DOM, sin azar). Motor de decisiones de la posta:
   estado clínico determinista, reloj simulado (minutos de simulación) separado del tiempo real, inventario con consumo, referencia con restricciones,
   eventos contextuales, taxonomía de errores, puntuación de 100 puntos y validadores de casos. Todo se calcula con los datos del caso: no hay IA ni resultados aleatorios.
   Las funciones no modifican sus argumentos (devuelven estados nuevos). Simulación educativa: no sustituye la norma vigente ni el juicio clínico. */
(function (raiz) {
  "use strict";

  var ESTADOS_PUBLICACION = ["Borrador", "Pendiente de bibliografía", "Pendiente de revisión clínica", "Validado", "Publicado", "Requiere actualización"];
  var CALIDADES = ["optima", "aceptable", "incorrecta", "peligrosa"];
  var PUNTOS = { optima: 1, aceptable: 0.6, incorrecta: 0.15, peligrosa: 0 };
  var EJES = { clinico: "Decisión clínica", seguridad: "Seguridad del paciente", recursos: "Uso de recursos", referencia: "Referencia y comunicación", comunitario: "Enfoque comunitario y cierre" };
  var PESOS = { clinico: 35, seguridad: 25, recursos: 15, referencia: 15, comunitario: 10 };
  var ERRORES = { omision: "Omisión", comision: "Comisión", demora: "Demora", seguridad_paciente: "Seguridad del paciente", recursos: "Recursos", comunicacion: "Comunicación", normativo: "Normativo" };
  var BANDAS = [[90, "Excelente"], [75, "Sólido"], [60, "En desarrollo"], [0, "Necesita reforzar"]];
  var TOPE_CRITICO = 74;
  var GRAVEDAD = ["Estable", "En vigilancia", "Grave", "Crítico"];
  var INSUMOS = {
    oxigeno: "Oxígeno (balones)", sro: "Sales de rehidratación oral (sobres)", suero_salino: "Suero salino 9 ‰ (frascos)", venoclisis: "Equipos de venoclisis",
    sulfato_mg: "Sulfato de magnesio (ampollas)", antihipertensivo: "Antihipertensivo de emergencia (tabletas)", foley: "Sondas Foley", prueba_dengue: "Pruebas rápidas de dengue",
    frasco_bk: "Frascos para esputo", ferula: "Férulas", vendas: "Vendas y apósitos", paquetes_frios: "Paquetes fríos"
  };
  var ESTABLECIMIENTO_BASE = {
    nombre: "Puesto de Salud Santa Esperanza", categoria: "I-2", ambito: "sierra", distancia_min: 180, ambulancia: true, comunicacion: "radio",
    inventario: { oxigeno: 2, sro: 40, suero_salino: 10, venoclisis: 10, sulfato_mg: 10, antihipertensivo: 30, foley: 3, prueba_dengue: 20, frasco_bk: 30, ferula: 4, vendas: 20, paquetes_frios: 8 },
    ficticio: true
  };

  function copia(x) { return JSON.parse(JSON.stringify(x)); }
  function por(l, id) { for (var i = 0; i < (l || []).length; i++) if (l[i].id === id) return l[i]; return null; }
  function entero(n, def) { n = Math.floor(Number(n)); return isFinite(n) && n >= 0 ? n : def; }

  /* establecimiento configurable: se completa con los valores base y se sanea */
  function establecimiento(cfg) {
    var e = copia(ESTABLECIMIENTO_BASE); cfg = cfg || {};
    if (cfg.nombre) e.nombre = String(cfg.nombre).slice(0, 60);
    if (["I-1", "I-2", "I-3", "I-4"].indexOf(cfg.categoria) >= 0) e.categoria = cfg.categoria;
    if (["sierra", "selva", "costa"].indexOf(cfg.ambito) >= 0) e.ambito = cfg.ambito;
    e.distancia_min = entero(cfg.distancia_min, e.distancia_min);
    if (typeof cfg.ambulancia === "boolean") e.ambulancia = cfg.ambulancia;
    if (["radio", "telefono", "ninguna"].indexOf(cfg.comunicacion) >= 0) e.comunicacion = cfg.comunicacion;
    if (cfg.inventario) Object.keys(INSUMOS).forEach(function (k) { if (cfg.inventario[k] != null) e.inventario[k] = entero(cfg.inventario[k], e.inventario[k]); });
    return e;
  }

  /* ---------- estado ---------- */
  function iniciar(caso, est, ahoraMs) {
    est = establecimiento(est); var inv = copia(est.inventario);
    Object.keys(caso.inventario_ajuste || {}).forEach(function (k) { inv[k] = caso.inventario_ajuste[k]; });
    var e = {
      v: 1, caso: caso.id, momento: caso.momentos[0].id, t_sim: 0, t_real: 0, ultimo: ahoraMs || 0, gravedad: caso.gravedad || 0, vitales: copia(caso.vitales || {}),
      inventario: inv, inventario_inicial: copia(inv), flags: [], eventos_vistos: [], historial: [], pruebas: [], referencia: { estado: "ninguna", t_sim: null }, fin: false, establecimiento: est
    };
    return aplicarEventos(caso, e, { momento: e.momento });
  }

  function momentoActual(caso, e) { return e.fin ? null : por(caso.momentos, e.momento); }

  function faltaInsumo(o, e) {
    var req = (o.req && o.req.items) || {}, f = [];
    Object.keys(req).forEach(function (k) { if ((e.inventario[k] || 0) < req[k]) f.push(k); });
    return f;
  }
  /* estado de cada opción: disponible o bloqueada con motivo */
  function disponibilidad(o, e) {
    var falta = faltaInsumo(o, e);
    if (falta.length) return { ok: false, motivo: "Insumo insuficiente: " + falta.map(function (k) { return INSUMOS[k] || k; }).join(", ") };
    var fl = (o.req && o.req.flags) || [];
    for (var i = 0; i < fl.length; i++) if (e.flags.indexOf(fl[i]) < 0) return { ok: false, motivo: "Aún no se cumple la condición necesaria." };
    if (o.bloquea_si && e.flags.indexOf(o.bloquea_si) >= 0) return { ok: false, motivo: "No es posible ahora: la vía está bloqueada y la ambulancia no puede llegar." };
    return { ok: true };
  }

  /* eventos contextuales: por tiempo simulado o al llegar a un momento */
  function aplicarEventos(caso, e, ctx) {
    var n = copia(e);
    (caso.eventos || []).forEach(function (ev, i) {
      var id = "ev" + i; if (n.eventos_vistos.indexOf(id) >= 0) return;
      var c = ev.cuando || {}, dispara = (c.t != null && n.t_sim >= c.t) || (c.momento && ctx && ctx.momento === c.momento);
      if (!dispara) return;
      n.eventos_vistos.push(id);
      (ev.flags || []).forEach(function (f) { if (n.flags.indexOf(f) < 0) n.flags.push(f); });
      Object.keys(ev.inv || {}).forEach(function (k) { n.inventario[k] = Math.max(0, (n.inventario[k] || 0) + ev.inv[k]); });
      if (ev.g) n.gravedad = Math.max(0, Math.min(3, n.gravedad + ev.g));
      n.historial.push({ tipo: "evento", texto: ev.texto, t_sim: n.t_sim });
    });
    return n;
  }

  function siguienteMomento(caso, e, o) {
    if (o.sig) return o.sig === "fin" ? null : o.sig;
    var i = -1; caso.momentos.forEach(function (m, k) { if (m.id === e.momento) i = k; });
    return i + 1 < caso.momentos.length ? caso.momentos[i + 1].id : null;
  }

  /* decide: aplica la opción elegida. Devuelve { ok, estado, motivo } sin modificar el estado recibido */
  function decidir(caso, e, opcionId, ahoraMs) {
    if (e.fin) return { ok: false, motivo: "El caso ya terminó.", estado: e };
    var m = momentoActual(caso, e), o = m && por(m.opciones, opcionId);
    if (!o) return { ok: false, motivo: "Opción no válida.", estado: e };
    var d = disponibilidad(o, e); if (!d.ok) return { ok: false, motivo: d.motivo, estado: e };
    var n = copia(e);
    if (ahoraMs && n.ultimo) { n.t_real += Math.min(600, Math.max(0, (ahoraMs - n.ultimo) / 1000)); }
    if (ahoraMs) n.ultimo = ahoraMs;
    var gasto = {};
    Object.keys(o.cons || {}).forEach(function (k) { n.inventario[k] = Math.max(0, (n.inventario[k] || 0) - o.cons[k]); gasto[k] = o.cons[k]; });
    n.t_sim += o.min || 0;
    n.gravedad = Math.max(0, Math.min(3, n.gravedad + (o.g || 0)));
    (o.flags || []).forEach(function (f) { if (n.flags.indexOf(f) < 0) n.flags.push(f); });
    if (o.referencia) n.referencia = { estado: o.referencia === "emergencia" ? "solicitada" : o.referencia === "rechazada" ? "rechazada" : "programada", t_sim: n.t_sim, momento: m.id };
    n.historial.push({ tipo: "decision", momento: m.id, opcion: o.id, calidad: o.calidad, error: o.error || null, eje: m.eje, t_sim: n.t_sim, t_real: Math.round(n.t_real), gasto: gasto, g: n.gravedad });
    n = aplicarEventos(caso, n, { t: n.t_sim });
    var sig = siguienteMomento(caso, n, o);
    if (sig) { n.momento = sig; n = aplicarEventos(caso, n, { momento: sig }); } else { n.fin = true; n.momento = null; }
    return { ok: true, estado: n, opcion: o, momento: m };
  }


  /* pruebas de la posta: consumen insumo y tiempo simulado; el resultado está predefinido en el caso */
  function solicitarPrueba(caso, e, id, ahoraMs) {
    var p = por(caso.pruebas, id); if (!p) return { ok: false, motivo: "Prueba no válida.", estado: e };
    if (e.fin) return { ok: false, motivo: "El caso ya terminó.", estado: e };
    if (e.pruebas.indexOf(id) >= 0) return { ok: false, motivo: "Ya está solicitada.", estado: e };
    if (p.insumo && (e.inventario[p.insumo] || 0) < 1) return { ok: false, motivo: "Insumo insuficiente: " + (INSUMOS[p.insumo] || p.insumo), estado: e };
    var n = copia(e);
    if (ahoraMs && n.ultimo) n.t_real += Math.min(600, Math.max(0, (ahoraMs - n.ultimo) / 1000)); if (ahoraMs) n.ultimo = ahoraMs;
    if (p.insumo) n.inventario[p.insumo] -= 1;
    n.t_sim += p.min || 0; n.pruebas.push(id);
    n.historial.push({ tipo: "prueba", prueba: id, texto: p.nombre, t_sim: n.t_sim });
    return { ok: true, estado: aplicarEventos(caso, n, { t: n.t_sim }) };
  }

  /* tiempo estimado de llegada a la referencia: depende de la distancia, del medio y de la vía */
  function tiempoReferencia(e) {
    var base = e.establecimiento.distancia_min, f = e.flags.indexOf("via_bloqueada") >= 0 ? 2 : 1, extra = e.establecimiento.ambulancia ? 0 : 60;
    return base * f + extra;
  }

  /* ---------- puntuación ---------- */
  function evaluar(caso, e) {
    var dec = e.historial.filter(function (h) { return h.tipo === "decision"; }), ejes = {}, errores = {}, criticos = [];
    Object.keys(PESOS).forEach(function (k) { ejes[k] = { suma: 0, n: 0 }; });
    dec.forEach(function (h) {
      ejes[h.eje].suma += PUNTOS[h.calidad]; ejes[h.eje].n++;
      if (h.error) errores[h.error] = (errores[h.error] || 0) + 1;
      if (h.calidad === "peligrosa") criticos.push(h);
    });
    var presentes = Object.keys(PESOS).filter(function (k) { return ejes[k].n > 0; }), peso = presentes.reduce(function (a, k) { return a + PESOS[k]; }, 0), total = 0, det = [];
    Object.keys(PESOS).forEach(function (k) {
      var pct = ejes[k].n ? ejes[k].suma / ejes[k].n : null, aporte = pct == null ? 0 : pct * PESOS[k] * 100 / peso;
      total += aporte; det.push({ id: k, nombre: EJES[k], peso: PESOS[k], pct: pct == null ? null : Math.round(pct * 100), puntos: Math.round(aporte * 10) / 10 });
    });
    total = Math.round(total);
    var topado = false; if (criticos.length && total > TOPE_CRITICO) { total = TOPE_CRITICO; topado = true; }
    var banda = BANDAS.filter(function (b) { return total >= b[0]; })[0][1];
    var consumo = {}; Object.keys(e.inventario_inicial).forEach(function (k) { var d = e.inventario_inicial[k] - e.inventario[k]; if (d > 0) consumo[k] = d; });
    var desenlace = criticos.length || e.gravedad >= 3 ? "desfavorable" : e.gravedad === 2 || total < 60 ? "reservado" : "favorable";
    return { total: total, banda: banda, ejes: det, errores: errores, criticos: criticos, topado_por_error_critico: topado, consumo: consumo, desenlace: desenlace,
      desenlace_texto: (caso.desenlaces || {})[desenlace] || "", gravedad_final: e.gravedad, t_sim: e.t_sim, t_real: Math.round(e.t_real),
      referencia: e.referencia, decisiones: dec.length };
  }

  /* ---------- recuperación documental (BM25 simple) para el supervisor: no es IA, solo localiza fragmentos reales con su página ---------- */
  var VACIAS = "de la el en y a los las del un una que con por para al se su es o lo como más pero sus le ya este esta entre cuando muy sin sobre también me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mí antes algunos qué unos yo otro otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo nosotros".split(" ");
  function tokens(t) { return String(t || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").split(/[^a-z0-9]+/).filter(function (w) { return w.length > 2 && VACIAS.indexOf(w) < 0; }); }
  function buscar(indice, consulta, k, docs) {
    var q = tokens(consulta); if (!q.length || !indice) return [];
    var F = indice.fragmentos.filter(function (f) { return !docs || docs.indexOf(f.doc) >= 0; }), N = F.length || 1, df = {};
    var tk = F.map(function (f) { var t = tokens(f.texto), s = {}; t.forEach(function (w) { s[w] = (s[w] || 0) + 1; }); Object.keys(s).forEach(function (w) { df[w] = (df[w] || 0) + 1; }); return { t: t.length, s: s }; });
    var prom = tk.reduce(function (a, x) { return a + x.t; }, 0) / N || 1;
    var res = F.map(function (f, i) {
      var sc = 0; q.forEach(function (w) { var tf = tk[i].s[w] || 0; if (!tf) return; var idf = Math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5)); sc += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * tk[i].t / prom)); });
      return { f: f, score: sc };
    }).filter(function (r) { return r.score > 0; }).sort(function (a, b) { return b.score - a.score; });
    return res.slice(0, k || 3).map(function (r) { return { doc: r.f.doc, pagina: r.f.pagina, texto: r.f.texto, puntaje: Math.round(r.score * 100) / 100 }; });
  }

  /* ---------- validadores (autoría) ---------- */
  var DOSIS = /\b\d+([.,]\d+)?\s?(mg|g|ml|mL|mcg|µg|ug|UI|gotas|ampollas?)\b/;
  function validarCaso(caso, evidencia, indice) {
    var err = [], ids = (evidencia.fuentes || []).map(function (f) { return f.id; });
    function falla(t) { err.push(caso.id + ": " + t); }
    ["id", "titulo", "resumen", "paciente", "momentos", "desenlaces", "estado_publicacion", "pendientes"].forEach(function (k) { if (!caso[k]) falla("falta " + k); });
    if (ESTADOS_PUBLICACION.indexOf(caso.estado_publicacion) < 0) falla("estado de publicación inválido");
    if (!caso.momentos || caso.momentos.length < 5) falla("menos de 5 momentos de decisión");
    var idsM = (caso.momentos || []).map(function (m) { return m.id; });
    (caso.momentos || []).forEach(function (m) {
      if (!EJES[m.eje]) falla(m.id + ": eje inválido");
      var op = m.opciones || [];
      if (op.length < 3) falla(m.id + ": pocas opciones");
      if (!op.some(function (o) { return o.calidad === "optima"; })) falla(m.id + ": sin opción óptima");
      var vistos = {};
      op.forEach(function (o) {
        if (vistos[o.id]) falla(m.id + "/" + o.id + ": id repetido"); vistos[o.id] = 1;
        if (CALIDADES.indexOf(o.calidad) < 0) falla(m.id + "/" + o.id + ": calidad inválida");
        if (o.calidad !== "optima" && !o.error) falla(m.id + "/" + o.id + ": falta tipo de error");
        if (o.error && !ERRORES[o.error]) falla(m.id + "/" + o.id + ": tipo de error inválido");
        if (!o.retro) falla(m.id + "/" + o.id + ": falta explicación");
        if (o.sig && o.sig !== "fin" && idsM.indexOf(o.sig) < 0) falla(m.id + "/" + o.id + ": siguiente inexistente");
        Object.keys(o.cons || {}).forEach(function (k) { if (!INSUMOS[k]) falla(m.id + "/" + o.id + ": insumo desconocido " + k); });
        (o.ref || []).forEach(function (r) {
          if (ids.indexOf(r.doc) < 0) falla(m.id + "/" + o.id + ": fuente " + r.doc + " no está en el registro");
          if (indice) { var ok = indice.fragmentos.some(function (f) { return f.doc === r.doc && f.pagina === r.pag; }); if (!ok) falla(m.id + "/" + o.id + ": la página " + r.pag + " de " + r.doc + " no existe en el índice"); }
        });
        if (DOSIS.test(o.texto + " " + o.retro) && !(o.ref && o.ref.length)) falla(m.id + "/" + o.id + ": hay una cantidad de medicamento sin cita documental");
      });
    });
    (caso.evidencia || []).forEach(function (id) { if (ids.indexOf(id) < 0) falla("evidencia " + id + " no registrada"); });
    return err;
  }

  /* ---------- aprendizaje adaptativo y progreso ---------- */
  function registrarIntento(progreso, caso, ev, ahora) {
    var p = copia(progreso || { intentos: [], casos: {} }); p.intentos = p.intentos || []; p.casos = p.casos || {};
    var r = p.casos[caso.id] || { mejor: 0, intentos: 0 }; r.intentos++; r.mejor = Math.max(r.mejor, ev.total); r.ultimo = ev.total; r.t = ahora || 0; p.casos[caso.id] = r;
    p.intentos.push({ caso: caso.id, t: ahora || 0, total: ev.total, banda: ev.banda, ejes: ev.ejes.map(function (x) { return { id: x.id, pct: x.pct }; }), errores: ev.errores, criticos: ev.criticos.length, t_sim: ev.t_sim, t_real: ev.t_real, consumo: ev.consumo, desenlace: ev.desenlace });
    if (p.intentos.length > 60) p.intentos = p.intentos.slice(-60);
    return p;
  }
  /* promedios por eje y por tipo de error; el eje más flojo orienta qué caso reforzar */
  function resumenProgreso(progreso) {
    var it = (progreso && progreso.intentos) || [], ej = {}, er = {};
    it.forEach(function (x) { x.ejes.forEach(function (e) { if (e.pct == null) return; (ej[e.id] = ej[e.id] || []).push(e.pct); }); Object.keys(x.errores || {}).forEach(function (k) { er[k] = (er[k] || 0) + x.errores[k]; }); });
    var medias = {}; Object.keys(ej).forEach(function (k) { medias[k] = Math.round(ej[k].reduce(function (a, b) { return a + b; }, 0) / ej[k].length); });
    var flojo = Object.keys(medias).sort(function (a, b) { return medias[a] - medias[b]; })[0] || null;
    return { intentos: it.length, medias: medias, errores: er, eje_flojo: flojo, criticos: it.reduce(function (a, x) { return a + (x.criticos || 0); }, 0) };
  }
  function recomendar(casos, progreso) {
    var r = resumenProgreso(progreso), hechos = (progreso && progreso.casos) || {};
    var sin = casos.filter(function (c) { return !hechos[c.id]; });
    if (r.eje_flojo) {
      var con = casos.filter(function (c) { return c.momentos.some(function (m) { return m.eje === r.eje_flojo; }); });
      var ord = con.sort(function (a, b) { return ((hechos[a.id] || { mejor: -1 }).mejor) - ((hechos[b.id] || { mejor: -1 }).mejor); });
      if (ord[0]) return { caso: ord[0].id, motivo: "Tu eje más flojo es «" + EJES[r.eje_flojo] + "»; este caso lo trabaja." };
    }
    return sin[0] ? { caso: sin[0].id, motivo: "Aún no lo has intentado." } : casos[0] ? { caso: casos[0].id, motivo: "Repite para mejorar tu mejor puntaje." } : null;
  }

  /* ---------- campaña «30 días como serumista» (base técnica sobre el mismo motor) ----------
     El inventario y la reputación pasan de un día al siguiente. Aún no hay guion de 30 días: solo la estructura y su prueba. */
  function campanaNueva(est, dias) { return { v: 1, dias: dias || 30, dia: 1, inventario: copia(establecimiento(est).inventario), reputacion: 50, resultados: [] }; }
  function campanaCerrarDia(camp, ev, e) {
    var c = copia(camp); c.inventario = copia(e.inventario);
    c.reputacion = Math.max(0, Math.min(100, c.reputacion + Math.round((ev.total - 60) / 5) - ev.criticos.length * 5));
    c.resultados.push({ dia: c.dia, caso: e.caso, total: ev.total }); c.dia++; return c;
  }

  var API = { ESTADOS_PUBLICACION: ESTADOS_PUBLICACION, CALIDADES: CALIDADES, PUNTOS: PUNTOS, EJES: EJES, PESOS: PESOS, ERRORES: ERRORES, BANDAS: BANDAS, TOPE_CRITICO: TOPE_CRITICO, GRAVEDAD: GRAVEDAD, INSUMOS: INSUMOS,
    ESTABLECIMIENTO_BASE: ESTABLECIMIENTO_BASE, establecimiento: establecimiento, iniciar: iniciar, momentoActual: momentoActual, solicitarPrueba: solicitarPrueba, disponibilidad: disponibilidad, decidir: decidir, tiempoReferencia: tiempoReferencia,
    evaluar: evaluar, buscar: buscar, tokens: tokens, validarCaso: validarCaso, registrarIntento: registrarIntento, resumenProgreso: resumenProgreso, recomendar: recomendar, campanaNueva: campanaNueva, campanaCerrarDia: campanaCerrarDia };
  if (typeof module !== "undefined" && module.exports) module.exports = API; else (raiz.MQP = raiz.MQP || {}).serumsNucleo = API;
})(typeof window !== "undefined" ? window : this);
