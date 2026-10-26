/* MedQuizPlus · Tutor Feynman IA — voz del navegador (dictado y lectura en voz alta).
   Arquitectura por turnos: este módulo solo captura/lee; el texto transcrito vuelve al estudiante para que lo revise antes de enviarlo.
   Para voz en tiempo real (bidireccional) bastaría reemplazar crearEscucha()/crearHabla() por adaptadores con la misma interfaz.
   PRIVACIDAD: el dictado usa el reconocimiento de voz del navegador. En Chrome/Edge el audio se envía al servicio de voz del fabricante
   del navegador; MedQuizPlus no recibe ni guarda audio (solo el texto que el estudiante decide enviar). Sin soporte, se escribe.
   Módulo UMD (se prueba con Node y objetos simulados del navegador en tests/feynman_ui_test.js). */
(function (raiz, fabrica) {
  if (typeof module === "object" && module.exports) module.exports = fabrica();
  else { var M = raiz.MQP || (raiz.MQP = {}); M.feynmanVoz = fabrica(); }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var MENSAJES = {
    no_soportado: "Tu navegador no permite dictar por voz. Escribe tu respuesta; el resto del tutor funciona igual.",
    permiso_denegado: "El navegador no tiene permiso para usar el micrófono. Actívalo desde el candado de la barra de direcciones (Permisos → Micrófono) y vuelve a intentarlo, o escribe tu respuesta.",
    sin_microfono: "No se detectó ningún micrófono. Conéctalo o escribe tu respuesta.",
    sin_voz: "No escuché nada. Acércate al micrófono e inténtalo de nuevo, o escribe tu respuesta.",
    red: "El servicio de reconocimiento de voz del navegador no está disponible ahora. Escribe tu respuesta o inténtalo más tarde.",
    otro: "No se pudo usar el dictado por voz. Puedes escribir tu respuesta."
  };
  function claseError(codigo) {
    if (codigo === "not-allowed" || codigo === "service-not-allowed") return "permiso_denegado";
    if (codigo === "audio-capture") return "sin_microfono";
    if (codigo === "no-speech") return "sin_voz";
    if (codigo === "network") return "red";
    if (codigo === "language-not-supported") return "no_soportado";
    return "otro";
  }
  function constructorSR(win) { return win && (win.SpeechRecognition || win.webkitSpeechRecognition) || null; }
  function soporteEscucha(win) { return !!constructorSR(win); }
  function soporteHabla(win) { return !!(win && win.speechSynthesis && win.SpeechSynthesisUtterance); }

  /* ---------- dictado ----------
     op: { lang, maxMs, onEstado('escuchando'), onTexto({final, interino}), onFin(texto, {confianza}), onCancelado(), onError({codigo, mensaje}) }
     Garantías: un solo reconocimiento a la vez; «escuchando» se informa SOLO cuando el navegador confirma que el micrófono está abierto;
     onFin/onCancelado/onError se llaman exactamente una vez por intento. */
  function crearEscucha(win, op) {
    var SR = constructorSR(win), rec = null, activo = false, cancelado = false, huboError = false, texto = "", minConf = 1, temporizador = null, gen = 0;
    function limpiarTemp() { if (temporizador) { win.clearTimeout(temporizador); temporizador = null; } }
    function fallar(codigo) { if (huboError) return; huboError = true; op.onError({ codigo: codigo, mensaje: MENSAJES[codigo] || MENSAJES.otro }); }
    function iniciar() {
      if (!SR) { fallar("no_soportado"); return false; }
      if (activo) return false;                        // doble clic o doble inicio: se ignora
      var mi = ++gen; texto = ""; minConf = 1; cancelado = false; huboError = false; activo = true;
      try {
        rec = new SR(); rec.lang = op.lang || "es-PE"; rec.continuous = true; rec.interimResults = true; rec.maxAlternatives = 1;
      } catch (e) { activo = false; fallar("otro"); return false; }
      rec.onstart = function () {
        if (mi !== gen) return;
        op.onEstado("escuchando");
        limpiarTemp(); temporizador = win.setTimeout(function () { if (mi === gen && activo) detener(); }, op.maxMs || 120000);
      };
      rec.onresult = function (ev) {
        if (mi !== gen) return;
        var interino = "";
        for (var i = ev.resultIndex; i < ev.results.length; i++) {
          var r = ev.results[i];
          if (r.isFinal) { texto += r[0].transcript + " "; if (typeof r[0].confidence === "number" && r[0].confidence > 0) minConf = Math.min(minConf, r[0].confidence); }
          else interino += r[0].transcript;
        }
        if (op.onTexto) op.onTexto({ final: texto.trim(), interino: interino });
      };
      rec.onerror = function (ev) { if (mi !== gen) return; if (ev.error === "aborted") return; fallar(claseError(ev.error)); };
      rec.onend = function () {
        if (mi !== gen) return;
        limpiarTemp(); var fin = texto.trim(), fueCancelado = cancelado; activo = false; rec = null;
        if (huboError) return;
        if (fueCancelado) { if (op.onCancelado) op.onCancelado(); return; }
        op.onFin(fin, { confianza: minConf });
      };
      try { rec.start(); } catch (e) { activo = false; rec = null; fallar("otro"); return false; }
      return true;
    }
    function detener() { if (rec && activo) { try { rec.stop(); } catch (e) { /* ya detenido */ } } }
    function cancelar() { if (rec && activo) { cancelado = true; try { rec.abort(); } catch (e) { /* ya detenido */ } } }
    return { disponible: function () { return !!SR; }, iniciar: iniciar, detener: detener, cancelar: cancelar, activo: function () { return activo; } };
  }

  /* ---------- lectura en voz alta ----------
     op: { onEstado('hablando'|'pausado'|'fin'|'detenido'|'error', detalle), velocidad }
     Garantías: una sola locución a la vez (hablar() cancela la anterior); los eventos de una locución cancelada se ignoran (token);
     el texto se trocea por frases para esquivar el corte de ~15 s de Chrome; pausa/reanudar/detener reflejan el estado real. */
  function trocear(t, max) {
    t = String(t || "").replace(/\*\*|__|`|#+\s/g, "").replace(/\[G\d+\]/g, "").replace(/\s+/g, " ").trim();
    if (!t) return [];
    var frases = t.match(/[^.!?¿?:;\n]+[.!?:;]*/g) || [t], out = [], cur = "";
    frases.forEach(function (f) {
      f = f.trim(); if (!f) return;
      if ((cur + " " + f).length > max && cur) { out.push(cur); cur = f; } else cur = cur ? cur + " " + f : f;
      while (cur.length > max * 1.5) { var corte = cur.lastIndexOf(" ", max); if (corte < 20) corte = max; out.push(cur.slice(0, corte)); cur = cur.slice(corte).trim(); }
    });
    if (cur) out.push(cur);
    return out;
  }
  function elegirVoz(win) {
    var vs = []; try { vs = win.speechSynthesis.getVoices() || []; } catch (e) { return null; }
    var pref = ["es-PE", "es-419", "es-MX", "es-US", "es-CO", "es-AR", "es-ES"];
    for (var i = 0; i < pref.length; i++) for (var j = 0; j < vs.length; j++) if (String(vs[j].lang).replace("_", "-") === pref[i]) return vs[j];
    for (var k = 0; k < vs.length; k++) if (/^es/i.test(vs[k].lang)) return vs[k];
    return null;
  }
  function crearHabla(win, op) {
    var S = win && win.speechSynthesis, U = win && win.SpeechSynthesisUtterance, token = 0, cola = [], i = 0, hablando = false, pausado = false, velocidad = op.velocidad || 1, guardian = null;
    function limpiarGuardian() { if (guardian) { win.clearTimeout(guardian); guardian = null; } }
    function emitir(e, d) { if (op.onEstado) op.onEstado(e, d); }
    function siguiente(mi) {
      if (mi !== token) return;
      if (i >= cola.length) { hablando = false; pausado = false; limpiarGuardian(); emitir("fin"); return; }
      var u = new U(cola[i]), voz = elegirVoz(win);
      u.lang = voz ? voz.lang : "es-PE"; if (voz) u.voice = voz; u.rate = velocidad;
      u.onstart = function () { if (mi === token) limpiarGuardian(); };
      u.onend = function () { if (mi !== token) return; i++; siguiente(mi); };
      u.onerror = function (ev) {
        if (mi !== token) return;
        if (ev && (ev.error === "interrupted" || ev.error === "canceled")) return;
        hablando = false; pausado = false; limpiarGuardian(); emitir("error", ev && ev.error);
      };
      /* si el navegador nunca empieza (voces sin cargar, política de reproducción), se informa en vez de aparentar que habla */
      if (i === 0) { limpiarGuardian(); guardian = win.setTimeout(function () { if (mi === token && hablando) { hablando = false; try { S.cancel(); } catch (e) {} token++; emitir("error", "no_inicio"); } }, op.esperaMs || 6000); }
      try { S.speak(u); } catch (e) { hablando = false; limpiarGuardian(); emitir("error", "excepcion"); }
    }
    function detener(silencioso) {
      var estaba = hablando; token++; hablando = false; pausado = false; cola = []; limpiarGuardian();
      if (S) { try { S.cancel(); } catch (e) { /* nada */ } }
      if (estaba && !silencioso) emitir("detenido");
    }
    return {
      disponible: function () { return !!(S && U); },
      hablar: function (texto) {
        if (!S || !U) return false;
        var partes = trocear(texto, 180); if (!partes.length) return false;
        detener(true); var mi = ++token; cola = partes; i = 0; hablando = true; pausado = false; emitir("hablando"); siguiente(mi); return true;
      },
      pausar: function () { if (hablando && !pausado) { try { S.pause(); } catch (e) {} pausado = true; emitir("pausado"); } },
      reanudar: function () { if (hablando && pausado) { try { S.resume(); } catch (e) {} pausado = false; emitir("hablando"); } },
      detener: function () { detener(false); },
      velocidad: function (v) { velocidad = Math.max(0.6, Math.min(1.6, Number(v) || 1)); },
      hablando: function () { return hablando; }, pausado: function () { return pausado; }
    };
  }
  return { MENSAJES: MENSAJES, soporteEscucha: soporteEscucha, soporteHabla: soporteHabla, crearEscucha: crearEscucha, crearHabla: crearHabla, trocear: trocear, elegirVoz: elegirVoz };
});
