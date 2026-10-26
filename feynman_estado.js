/* MedQuizPlus · Tutor Feynman IA — máquina de estados de la conversación por voz/texto.
   Una sola fuente de verdad para lo que la interfaz muestra. Reglas que protege:
   - «escuchando» solo se alcanza desde un estado en el que el micrófono puede abrirse (nunca mientras la IA habla o piensa);
   - «analizando» solo existe desde que la intervención SE ENVIÓ al servidor;
   - «reproduciendo» solo mientras suena la voz de la IA.
   Es un módulo UMD sin dependencias: se prueba con Node (tests/feynman_ui_test.js). */
(function (raiz, fabrica) {
  if (typeof module === "object" && module.exports) module.exports = fabrica();
  else { var M = raiz.MQP || (raiz.MQP = {}); M.feynmanEstado = fabrica(); }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  var ETIQUETAS = {
    listo: "Preparado para escuchar",
    escuchando: "Escuchando… habla con calma",
    procesando_audio: "Procesando el audio…",
    analizando: "Analizando tu respuesta y preparando la del tutor…",
    reproduciendo: "El tutor está hablando",
    esperando: "Tu turno: explica con tus palabras",
    error: "Hubo un problema (puedes reintentar)",
    completada: "Sesión completada"
  };
  /* de → a */
  var PERMITIDAS = {
    listo:            ["escuchando", "analizando", "reproduciendo", "esperando", "error", "completada"],
    esperando:        ["escuchando", "analizando", "reproduciendo", "listo", "error", "completada"],
    escuchando:       ["procesando_audio", "esperando", "error"],
    procesando_audio: ["esperando", "error"],
    analizando:       ["reproduciendo", "esperando", "error", "completada"],
    reproduciendo:    ["esperando", "error", "completada"],
    error:            ["listo", "esperando", "escuchando", "analizando", "completada"],
    completada:       ["analizando", "esperando", "listo", "reproduciendo"]
  };
  function crear(alCambiar) {
    var actual = "listo", detalle = null;
    return {
      estado: function () { return actual; },
      detalle: function () { return detalle; },
      etiqueta: function () { return ETIQUETAS[actual]; },
      puede: function (a) { return (PERMITIDAS[actual] || []).indexOf(a) >= 0; },
      /* devuelve false (y no cambia nada) si la transición no es válida */
      ir: function (a, info) {
        if (a === actual) { detalle = info || detalle; return true; }
        if (!this.puede(a)) return false;
        var previo = actual; actual = a; detalle = info || null;
        if (alCambiar) alCambiar(a, previo, detalle);
        return true;
      },
      /* el micrófono puede abrirse y se puede enviar solo en estos estados */
      puedeEscuchar: function () { return this.puede("escuchando"); },
      puedeEnviar: function () { return this.puede("analizando"); }
    };
  }
  return { crear: crear, ETIQUETAS: ETIQUETAS, PERMITIDAS: PERMITIDAS };
});
