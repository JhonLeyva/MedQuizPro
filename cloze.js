/* MedQuizPlus · tarjetas Cloze (completar el hueco). Funciones puras, sin DOM: se prueban con Node (tests/cloze_test.js).
   Formato (compatible con Anki):  texto con {{c1::respuesta}} y, si se quiere, {{c1::respuesta::pista}}.
   NADA se inventa: la propuesta automática sale de una frase del comentario docente del banco que contiene la respuesta correcta de la pregunta;
   si no la encuentra, no propone nada y el estudiante marca los huecos él mismo («Ocultar selección»). */
(function (raiz, fabrica) {
  if (typeof module === "object" && module.exports) module.exports = fabrica();
  else { var M = raiz.MQP || (raiz.MQP = {}); M.cloze = fabrica(); }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  var RE = /\{\{c(\d{1,2})::([\s\S]*?)(?:::([\s\S]*?))?\}\}/g;
  var STOP = ["para", "como", "pero", "sino", "entre", "desde", "hasta", "sobre", "cuando", "donde", "porque", "tambien", "solo", "esta", "este", "estos", "estas", "otro", "otra", "cada", "mas", "muy", "con", "sin", "por", "del", "los", "las", "una", "uno", "que"];
  var MIN_CONTEXTO = 15, MAX_OCULTO = 0.7;

  function norm(t) { return String(t || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function copia() { return new RegExp(RE.source, "g"); }
  function esCloze(t) { return copia().test(String(t || "")); }
  /* texto con los huecos tapados: «[…]» o «[pista]» */
  function mascara(t) { return String(t || "").replace(copia(), function (_, n, r, p) { return "[" + (p ? p : "…") + "]"; }); }
  /* texto completo, sin marcas */
  function completo(t) { return String(t || "").replace(copia(), function (_, n, r) { return r; }); }
  function respuestas(t) { var o = [], m, re = copia(); while ((m = re.exec(String(t || "")))) o.push(m[2]); return o; }

  function validar(t) {
    t = String(t || "");
    var llaves = (t.match(/\{\{|\}\}/g) || []).length, m, re = copia(), n = 0, oculto = 0;
    while ((m = re.exec(t))) { n++; if (!m[2].trim()) return { ok: false, error: "Hay un hueco vacío." }; if (/\{\{|\}\}/.test(m[2])) return { ok: false, error: "No se pueden anidar huecos." }; oculto += m[2].length; }
    if (!n) return { ok: false, error: "Marca al menos un hueco: selecciona la palabra y pulsa «Ocultar selección»." };
    if (llaves !== n * 2) return { ok: false, error: "Hay llaves {{ }} sin cerrar o fuera de un hueco." };
    var visible = completo(t).length - oculto;
    if (visible < MIN_CONTEXTO) return { ok: false, error: "Queda muy poco texto visible: la tarjeta perdería sentido." };
    if (oculto / completo(t).length > MAX_OCULTO) return { ok: false, error: "Ocultas demasiado texto: deja más contexto visible." };
    return { ok: true };
  }

  /* envuelve [ini, fin) en un hueco nuevo (c1, c2…); null si la selección es vacía o toca un hueco existente */
  function ocultar(t, ini, fin) {
    t = String(t || ""); if (!(fin > ini) || ini < 0 || fin > t.length) return null;
    var sel = t.slice(ini, fin); if (!sel.trim() || /\{\{|\}\}/.test(sel)) return null;
    var m, re = copia(), max = 0;
    while ((m = re.exec(t))) { var a = m.index, b = a + m[0].length; if (ini < b && fin > a) return null; max = Math.max(max, +m[1]); }
    var ajusta = sel.match(/^(\s*)([\s\S]*?)(\s*)$/);       // no tapa los espacios de los bordes
    var i2 = ini + ajusta[1].length, f2 = fin - ajusta[3].length;
    return t.slice(0, i2) + "{{c" + (max + 1) + "::" + t.slice(i2, f2) + "}}" + t.slice(f2);
  }

  /* Propuesta desde una pregunta del banco: {frente, dorso} o null. q = { opciones: [{letra, texto}], clave, comentario } */
  function construir(q) {
    if (!q || !q.comentario || !q.opciones) return null;
    var op = q.opciones.filter(function (o) { return o.letra === q.clave; })[0]; if (!op) return null;
    var claves = {}, nClaves = 0;
    norm(op.texto).split(/[^a-z0-9]+/).forEach(function (w) { if (w.length >= 4 && STOP.indexOf(w) < 0 && !claves[w]) { claves[w] = 1; nClaves++; } });
    if (!nClaves) return null;
    var frases = String(q.comentario).replace(/\s+/g, " ").match(/[^.!?]+[.!?]+(?:\s|$)|[^.!?]+$/g) || [];
    var mejor = null;
    frases.forEach(function (f) {
      f = f.trim(); if (f.length < 30 || f.length > 320) return;
      if (/\b(?:alternativa|opci[oó]n|opciones)\s+[A-E]\b/i.test(f)) return;      // una tarjeta no debe depender de las letras de un examen concreto
      var palabras = [], re = /[\p{L}\p{N}]+/gu, m, hallados = {};
      while ((m = re.exec(f))) { var n = norm(m[0]), marca = !!claves[n]; if (marca) hallados[n] = 1; palabras.push({ ini: m.index, fin: m.index + m[0].length, marca: marca, corta: n.length <= 3 }); }
      var distintos = Object.keys(hallados).length; if (distintos < Math.max(1, Math.ceil(nClaves * 0.6))) return;
      /* tramo más largo de palabras marcadas; solo lo separan palabras cortas (de, al, en…) */
      var run = null, cur = null;
      palabras.forEach(function (p, k) {
        if (p.marca) { if (!cur) cur = { ini: p.ini, fin: p.fin, n: 1, ult: k }; else if (k - cur.ult <= 2 && palabras.slice(cur.ult + 1, k).every(function (x) { return x.corta; })) { cur.fin = p.fin; cur.n++; cur.ult = k; } else { if (!run || cur.n > run.n) run = cur; cur = { ini: p.ini, fin: p.fin, n: 1, ult: k }; } }
      });
      if (cur && (!run || cur.n > run.n)) run = cur;
      if (!run) return;
      var texto = f.slice(0, run.ini) + "{{c1::" + f.slice(run.ini, run.fin) + "}}" + f.slice(run.fin);
      if (!validar(texto).ok) return;
      if (!mejor || distintos > mejor.d) mejor = { d: distintos, texto: texto };
    });
    if (!mejor) return null;
    return { frente: mejor.texto, dorso: dorso(mejor.texto) };
  }
  /* el dorso se arma solo: las respuestas y la frase completa */
  function dorso(t) { return "Respuesta: " + respuestas(t).join("; ") + "\n\n" + completo(t); }

  return { esCloze: esCloze, mascara: mascara, completo: completo, respuestas: respuestas, validar: validar, ocultar: ocultar, construir: construir, dorso: dorso };
});
