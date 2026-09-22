/* MedQuizPro — interacciones de la landing. Script clásico + IIFE, sin dependencias. */
(function () {
  "use strict";

  function safe(name, fn) {
    try { fn(); } catch (err) {
      if (window.console && console.warn) console.warn("[MedQuizPro] " + name, err);
    }
  }

  var reduced = false;
  try {
    reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) { reduced = false; }

  /* ---------- menú móvil ---------- */
  safe("nav", function () {
    var toggle = document.getElementById("navToggle");
    var nav = document.getElementById("nav");
    if (!toggle || !nav) return;

    var mq = window.matchMedia("(max-width: 880px)");
    function close() {
      toggle.setAttribute("aria-expanded", "false");
      if (mq.matches) nav.hidden = true;
    }
    function sync() { if (mq.matches) { close(); } else { nav.hidden = false; } }

    sync();
    if (mq.addEventListener) mq.addEventListener("change", sync);
    else if (mq.addListener) mq.addListener(sync);

    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", open ? "false" : "true");
      nav.hidden = open;
    });
    nav.addEventListener("click", function (ev) {
      if (ev.target.tagName === "A") close();
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") close();
    });
  });

  /* ---------- pregunta de muestra ---------- */
  safe("quiz", function () {
    var preguntas = [
      {
        area: "Medicina Interna", examen: "ENAM",
        enunciado: "Varón de 58 años, diabético, acude por dolor torácico opresivo de 40 minutos. El ECG muestra elevación del segmento ST en DII, DIII y aVF. ¿Cuál es la conducta inicial más apropiada?",
        opciones: [
          "Solicitar ecocardiograma y reevaluar en 6 horas",
          "Activar la vía de reperfusión coronaria de inmediato",
          "Iniciar furosemida endovenosa en bolo",
          "Programar prueba de esfuerzo al alta"
        ],
        correcta: 1,
        porque: "La elevación del ST en DII, DIII y aVF define un infarto de cara inferior con elevación del ST. El objetivo es reperfundir cuanto antes (angioplastia primaria o fibrinólisis si no hay disponibilidad); ninguna prueba adicional debe retrasarlo."
      },
      {
        area: "Ginecología y Obstetricia", examen: "ENAM",
        enunciado: "Gestante de 34 semanas con presión arterial de 160/105 mmHg, proteinuria significativa y cefalea persistente que no cede con analgésicos. ¿Qué conducta corresponde?",
        opciones: [
          "Reposo en domicilio y control en 72 horas",
          "Hospitalizar, antihipertensivo de acción rápida y sulfato de magnesio",
          "Dieta hiposódica y repetir la proteinuria en una semana",
          "Cesárea inmediata sin estabilización previa"
        ],
        correcta: 1,
        porque: "El cuadro reúne criterios de severidad de preeclampsia. Corresponde manejo hospitalario: control de la presión con antihipertensivo de acción rápida y sulfato de magnesio como neuroprofilaxis. El momento del parto se decide después de estabilizar a la paciente."
      },
      {
        area: "Pediatría · Salud Pública", examen: "EsSalud",
        enunciado: "Durante un brote de enfermedad diarreica, un niño de 3 años llega con ojos hundidos, bebe con avidez y el pliegue cutáneo se deshace lentamente. Según AIEPI, ¿qué plan de hidratación le corresponde?",
        opciones: [
          "Plan A, con sales de rehidratación en domicilio",
          "Plan B, con sales de rehidratación supervisadas en el establecimiento",
          "Plan C, con fluidos endovenosos",
          "Antibiótico empírico y alta con indicaciones"
        ],
        correcta: 1,
        porque: "Los signos descritos corresponden a deshidratación sin shock. El Plan B indica sales de rehidratación oral supervisadas en el establecimiento durante cuatro horas, con reevaluación al término. El Plan C se reserva para la deshidratación grave."
      }
    ];

    var i = 0, respondida = false;
    var elArea = document.getElementById("qArea");
    var elExam = document.getElementById("qExam");
    var elCount = document.getElementById("qCounter");
    var elStem = document.getElementById("qStem");
    var elOpts = document.getElementById("qOptions");
    var elFb = document.getElementById("qFeedback");
    var elVerdict = document.getElementById("qVerdict");
    var elWhy = document.getElementById("qWhy");
    var elNext = document.getElementById("qNext");
    var elNote = document.getElementById("qNote");
    if (!elOpts || !elStem || !elNext) return;

    var letras = ["A", "B", "C", "D"];

    function pintar() {
      var q = preguntas[i];
      respondida = false;
      elArea.textContent = q.area;
      elExam.textContent = q.examen;
      elCount.textContent = "Pregunta " + (i + 1) + " de " + preguntas.length;
      elStem.textContent = q.enunciado;
      elOpts.innerHTML = "";
      for (var k = 0; k < q.opciones.length; k++) {
        var li = document.createElement("li");
        var b = document.createElement("button");
        b.type = "button";
        b.className = "opt";
        b.setAttribute("data-i", String(k));
        var bub = document.createElement("span");
        bub.className = "opt__bubble";
        bub.textContent = letras[k];
        var txt = document.createElement("span");
        txt.className = "opt__text";
        txt.textContent = q.opciones[k];
        b.appendChild(bub);
        b.appendChild(txt);
        li.appendChild(b);
        elOpts.appendChild(li);
      }
      elFb.hidden = true;
      elNext.hidden = true;
      elNote.hidden = false;
      elNote.textContent = "Marca una alternativa para ver la explicación";
    }

    elOpts.addEventListener("click", function (ev) {
      var btn = ev.target.closest ? ev.target.closest(".opt") : null;
      if (!btn || respondida) return;
      respondida = true;

      var q = preguntas[i];
      var elegida = parseInt(btn.getAttribute("data-i"), 10);
      var acerto = elegida === q.correcta;
      var botones = elOpts.querySelectorAll(".opt");

      for (var k = 0; k < botones.length; k++) {
        botones[k].disabled = true;
        var idx = parseInt(botones[k].getAttribute("data-i"), 10);
        if (idx === q.correcta) botones[k].classList.add("opt--right");
        else if (idx === elegida) botones[k].classList.add("opt--wrong");
      }

      elVerdict.textContent = acerto ? "Respuesta correcta" : "Respuesta incorrecta";
      elVerdict.className = "quiz__verdict " + (acerto ? "quiz__verdict--ok" : "quiz__verdict--bad");
      elWhy.textContent = q.porque;
      elFb.hidden = false;
      elNote.hidden = true;
      elNext.hidden = false;
      elNext.textContent = (i + 1 < preguntas.length) ? "Siguiente pregunta" : "Volver a la primera";
    });

    elNext.addEventListener("click", function () {
      i = (i + 1) % preguntas.length;
      pintar();
    });

    pintar();
  });

  /* ---------- bancos por especialidad + simulador ----------
     Cada especialidad lee su banco de bancos/<archivo>.json con fetch.
     Formato: { especialidad, preguntas: [ { id, especialidad, examen_origen,
     enunciado, opciones: { A: "...", B: "..." }, clave_correcta: "B", comentario } ] }.
     Si la página se sirvió como archivo único (artifact.html), los bancos vienen
     incrustados en window.MQP_BANCOS y no hace falta pedirlos. */
  safe("bancos", function () {
    var grid = document.getElementById("specs");
    var vista = document.getElementById("simView");
    if (!grid || !vista) return;

    var I = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"';
    var ICONOS = {
      corazon: '<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7.1a4.3 4.3 0 0 1 7.5 2.7C19.5 15.4 12 20 12 20z"/><path d="M4.5 12h3.2l1.6-2.6 2.6 5 1.7-2.4h5.9"/>',
      pulmones: '<path d="M12 3v8m0 0-2.5 2.2M12 11l2.5 2.2"/><path d="M9 7.5C6.4 7.5 4 12.4 4 17c0 2 1.2 3 3 3s3-1.1 3-3V9.2"/><path d="M15 7.5c2.6 0 5 4.9 5 9.5 0 2-1.2 3-3 3s-3-1.1-3-3V9.2"/>',
      estomago: '<path d="M9 3v4c0 2-3 3-3 7a6 6 0 0 0 6 6h1.5a5.5 5.5 0 0 0 5.5-5.5c0-3-2.6-4.4-4.8-3.3-1.8.9-3.2-.1-3.2-2.2V3"/>',
      rinon: '<path d="M10 4C6.5 4 4 7.8 4 12s2.5 8 6 8c1.8 0 3-1.6 3-3.4 0-1.2-1-2.3-1-4.6s1-3.4 1-4.6C13 5.6 11.8 4 10 4z"/><path d="M12.5 12H16c2 0 3 1.6 3 3.6V21"/>',
      tiroides: '<path d="M12 7v10"/><path d="M12 9.5C10.4 6.4 5 6.6 5 11.3c0 4.5 4.3 6 7 4.2"/><path d="M12 9.5c1.6-3.1 7-2.9 7 1.8 0 4.5-4.3 6-7 4.2"/>',
      virus: '<circle cx="12" cy="12" r="4.5"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.2 2.2M16.2 16.2l2.2 2.2M5.6 18.4l2.2-2.2M16.2 7.8l2.2-2.2"/>',
      cerebro: '<path d="M11 5.2A3 3 0 0 0 6 6.8a3 3 0 0 0-1.8 5.1A3 3 0 0 0 6.5 17 3 3 0 0 0 11 18.8z"/><path d="M13 5.2a3 3 0 0 1 5 1.6 3 3 0 0 1 1.8 5.1 3 3 0 0 1-2.3 5.1 3 3 0 0 1-4.5 1.8z"/>',
      gota: '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z"/><path d="M9.3 14.3A2.7 2.7 0 0 0 12 17"/>',
      articulacion: '<path d="M8.5 3v5.5a3.5 3.5 0 0 0 7 0V3"/><path d="M8.5 21v-4.5a3.5 3.5 0 0 1 7 0V21"/><path d="M6 12h2M16 12h2"/>',
      bebe: '<circle cx="12" cy="12.5" r="8"/><path d="M9.3 11h.01M14.7 11h.01"/><path d="M10 15a2.6 2.6 0 0 0 4 0"/><path d="M12 4.5c1.4.6 1.6 2 .4 2.6"/>',
      femenino: '<circle cx="12" cy="9" r="5"/><path d="M12 14v7M9 18h6"/>',
      bisturi: '<path d="M4 20l6.2-6.2"/><path d="M10.2 13.8 19 5c.9 3.4-1.1 7-5.4 8.9L12 15.6z"/>',
      hueso: '<path d="M17 10c.7-.7 1.7 0 2.5 0a2.5 2.5 0 1 0 0-5 .5.5 0 0 1-.5-.5 2.5 2.5 0 1 0-5 0c0 .8.7 1.8 0 2.5l-7 7c-.7.7-1.7 0-2.5 0a2.5 2.5 0 0 0 0 5c.3 0 .5.2.5.5a2.5 2.5 0 1 0 5 0c0-.8-.7-1.8 0-2.5z"/>',
      ojo: '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
      mente: '<path d="M13 3a7 7 0 0 0-7 7c0 2 .8 3.6 2 4.8V21h7v-3h2a2 2 0 0 0 2-2v-2.5l1.8-.8-1.8-3A7 7 0 0 0 13 3z"/><path d="M11 10.5a2 2 0 1 1 2 2"/>',
      grafico: '<path d="M4 20V11M10 20V5M16 20v-7M3 20h18"/>',
      matraz: '<path d="M9 3h6M10 3v6.2L5 18a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 18l-5-8.8V3"/><path d="M7.4 15h9.2"/>'
    };

    var CATALOGO = [
      { nombre: "Cardiología", archivo: "cardiologia", icono: "corazon" },
      { nombre: "Neumología", archivo: "neumologia", icono: "pulmones" },
      { nombre: "Gastroenterología", archivo: "gastroenterologia", icono: "estomago" },
      { nombre: "Nefrología y Urología", archivo: "nefrologia", icono: "rinon" },
      { nombre: "Endocrinología", archivo: "endocrinologia", icono: "tiroides" },
      { nombre: "Infectología", archivo: "infectologia", icono: "virus" },
      { nombre: "Neurología", archivo: "neurologia", icono: "cerebro" },
      { nombre: "Hematología", archivo: "hematologia", icono: "gota" },
      { nombre: "Reumatología y Dermatología", archivo: "reumatologia", icono: "articulacion" },
      { nombre: "Pediatría y Neonatología", archivo: "pediatria", icono: "bebe" },
      { nombre: "Ginecología y Obstetricia", archivo: "ginecologia", icono: "femenino" },
      { nombre: "Cirugía General y Digestiva", archivo: "cirugia", icono: "bisturi" },
      { nombre: "Traumatología y Ortopedia", archivo: "traumatologia", icono: "hueso" },
      { nombre: "Oftalmología y Otorrinolaringología", archivo: "oftalmo_orl", icono: "ojo" },
      { nombre: "Psiquiatría", archivo: "psiquiatria", icono: "mente" },
      { nombre: "Salud Pública, Gestión y Epidemiología", archivo: "salud_publica", icono: "grafico" },
      { nombre: "Ciencias Básicas", archivo: "ciencias_basicas", icono: "matraz" }
    ];

    var el = {
      back: document.getElementById("svBack"),
      score: document.getElementById("svScore"),
      area: document.getElementById("svArea"),
      exam: document.getElementById("svExam"),
      counter: document.getElementById("svCounter"),
      status: document.getElementById("svStatus"),
      content: document.getElementById("svContent"),
      stem: document.getElementById("svStem"),
      options: document.getElementById("svOptions"),
      feedback: document.getElementById("svFeedback"),
      verdict: document.getElementById("svVerdict"),
      why: document.getElementById("svWhy"),
      prev: document.getElementById("svPrev"),
      next: document.getElementById("svNext")
    };

    var cache = {};          // archivo -> promesa de preguntas normalizadas
    var estados = {};        // archivo -> nodo de estado de la tarjeta
    var actual = null;       // { esp, preguntas, i, respuestas }
    var turno = 0;           // descarta respuestas de fetch que llegan tarde

    /* Acepta { preguntas: [...] } o directamente [...]; opciones como objeto o arreglo. */
    function normalizar(datos) {
      var lista = Array.isArray(datos) ? datos : (datos && Array.isArray(datos.preguntas) ? datos.preguntas : null);
      if (!lista) throw new Error("formato");
      var salida = [];
      for (var k = 0; k < lista.length; k++) {
        var p = lista[k] || {};
        var ops = [];
        if (Array.isArray(p.opciones)) {
          for (var j = 0; j < p.opciones.length; j++) ops.push({ letra: "ABCDE".charAt(j), texto: String(p.opciones[j]) });
        } else if (p.opciones && typeof p.opciones === "object") {
          var letras = Object.keys(p.opciones).sort();
          for (var m = 0; m < letras.length; m++) ops.push({ letra: letras[m].toUpperCase(), texto: String(p.opciones[letras[m]]) });
        }
        if (!p.enunciado || ops.length < 2) continue;
        salida.push({
          id: p.id, especialidad: p.especialidad, examen: p.examen_origen || "",
          enunciado: String(p.enunciado), opciones: ops,
          clave: String(p.clave_correcta || "").trim().toUpperCase(),
          comentario: p.comentario ? String(p.comentario) : ""
        });
      }
      return salida;
    }

    function cargar(archivo) {
      if (cache[archivo]) return cache[archivo];
      var incrustado = window.MQP_BANCOS && window.MQP_BANCOS[archivo];
      var promesa = incrustado
        ? Promise.resolve(incrustado)
        : fetch("bancos/" + archivo + ".json", { cache: "no-cache" }).then(function (res) {
            if (!res.ok) throw new Error("http " + res.status);
            return res.json();   // si el servidor devuelve HTML (404 reescrito), esto falla y cae al catch
          });
      cache[archivo] = promesa.then(normalizar);
      cache[archivo].catch(function () { delete cache[archivo]; });  // permite reintentar
      return cache[archivo];
    }

    /* ----- cuadrícula ----- */
    function pintarGrid() {
      var frag = document.createDocumentFragment();
      for (var k = 0; k < CATALOGO.length; k++) {
        var esp = CATALOGO[k];
        var card = document.createElement("article");
        card.className = "spec";
        card.innerHTML =
          '<span class="spec__icon"><svg ' + I + '>' + ICONOS[esp.icono] + '</svg></span>' +
          '<h3></h3><span class="spec__status">Banco disponible</span>' +
          '<button class="btn btn--primary" type="button">Iniciar práctica</button>';
        card.querySelector("h3").textContent = esp.nombre;
        estados[esp.archivo] = card.querySelector(".spec__status");
        (function (esp, btn) {
          btn.setAttribute("aria-label", "Iniciar práctica de " + esp.nombre);
          btn.addEventListener("click", function () { abrir(esp); });
        })(esp, card.querySelector("button"));
        frag.appendChild(card);
      }
      grid.appendChild(frag);
    }

    function actualizarEstado(archivo, preguntas, fallo) {
      var nodo = estados[archivo];
      if (!nodo) return;
      if (fallo) {
        nodo.className = "spec__status spec__status--off";
        nodo.textContent = "No disponible por ahora";
      } else if (!preguntas.length) {
        nodo.className = "spec__status";
        nodo.textContent = "Banco en preparación";
      } else {
        nodo.className = "spec__status spec__status--ok";
        nodo.textContent = "Banco disponible · " + preguntas.length + (preguntas.length === 1 ? " pregunta" : " preguntas");
      }
    }

    /* Cuenta las preguntas cuando la sección se acerca a la pantalla, no antes. */
    function contarTodo() {
      for (var k = 0; k < CATALOGO.length; k++) {
        (function (archivo) {
          cargar(archivo).then(
            function (ps) { actualizarEstado(archivo, ps, false); },
            function () { actualizarEstado(archivo, [], true); }
          );
        })(CATALOGO[k].archivo);
      }
    }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entradas) {
        if (entradas[0].isIntersecting) { io.disconnect(); contarTodo(); }
      }, { rootMargin: "300px 0px" });
      io.observe(grid);
    } else {
      contarTodo();
    }

    /* ----- simulador ----- */
    function mostrarVista(simulador) {
      grid.hidden = simulador;
      vista.hidden = !simulador;
      var seccion = document.getElementById("bancos");
      if (seccion && seccion.scrollIntoView) seccion.scrollIntoView({ block: "start", behavior: reduced ? "auto" : "smooth" });
    }

    function mensaje(texto) {
      el.content.hidden = true;
      el.status.hidden = false;
      el.status.textContent = texto;
      el.counter.textContent = "";
      el.exam.hidden = true;
      el.prev.disabled = true;
      el.next.disabled = true;
      el.score.textContent = "";
    }

    function abrir(esp) {
      var mio = ++turno;
      actual = null;
      el.area.textContent = esp.nombre;
      mensaje("Cargando el banco de " + esp.nombre + "…");
      mostrarVista(true);
      cargar(esp.archivo).then(function (preguntas) {
        if (mio !== turno) return;
        actualizarEstado(esp.archivo, preguntas, false);
        if (!preguntas.length) { mensaje("Este banco todavía no tiene preguntas publicadas. Vuelve pronto."); return; }
        actual = { esp: esp, preguntas: preguntas, i: 0, respuestas: [] };
        pintarPregunta();
      }, function () {
        if (mio !== turno) return;
        actualizarEstado(esp.archivo, [], true);
        mensaje("No se pudo cargar el banco de " + esp.nombre + ". Revisa tu conexión e inténtalo de nuevo.");
      });
    }

    function pintarPuntaje() {
      var hechas = 0, bien = 0;
      for (var k = 0; k < actual.preguntas.length; k++) {
        var r = actual.respuestas[k];
        if (r) { hechas++; if (r === actual.preguntas[k].clave) bien++; }
      }
      el.score.textContent = hechas ? ("Aciertos: " + bien + " de " + hechas + " respondidas") : "";
    }

    function pintarPregunta() {
      var q = actual.preguntas[actual.i];
      var total = actual.preguntas.length;
      el.status.hidden = true;
      el.content.hidden = false;
      el.counter.textContent = "Pregunta " + (actual.i + 1) + " de " + total;
      el.exam.hidden = !q.examen;
      el.exam.textContent = q.examen;
      el.stem.textContent = q.enunciado;

      el.options.innerHTML = "";
      for (var k = 0; k < q.opciones.length; k++) {
        var li = document.createElement("li");
        var b = document.createElement("button");
        b.type = "button";
        b.className = "opt";
        b.setAttribute("data-letra", q.opciones[k].letra);
        var bub = document.createElement("span");
        bub.className = "opt__bubble";
        bub.textContent = q.opciones[k].letra;
        var txt = document.createElement("span");
        txt.className = "opt__text";
        txt.textContent = q.opciones[k].texto;
        b.appendChild(bub);
        b.appendChild(txt);
        li.appendChild(b);
        el.options.appendChild(li);
      }

      var previa = actual.respuestas[actual.i];
      if (previa) marcar(previa); else el.feedback.hidden = true;

      el.prev.disabled = actual.i === 0;
      el.next.disabled = actual.i >= total - 1;
      pintarPuntaje();
    }

    function marcar(elegida) {
      var q = actual.preguntas[actual.i];
      var botones = el.options.querySelectorAll(".opt");
      for (var k = 0; k < botones.length; k++) {
        var letra = botones[k].getAttribute("data-letra");
        botones[k].disabled = true;
        if (letra === q.clave) botones[k].classList.add("opt--right");
        else if (letra === elegida) botones[k].classList.add("opt--wrong");
      }
      var acerto = elegida === q.clave;
      el.verdict.textContent = acerto
        ? "Respuesta correcta"
        : "Respuesta incorrecta · la correcta es la " + q.clave;
      el.verdict.className = "quiz__verdict " + (acerto ? "quiz__verdict--ok" : "quiz__verdict--bad");
      el.why.textContent = q.comentario || "Esta pregunta todavía no tiene comentario docente.";
      el.feedback.hidden = false;
    }

    el.options.addEventListener("click", function (ev) {
      var btn = ev.target.closest ? ev.target.closest(".opt") : null;
      if (!btn || !actual || actual.respuestas[actual.i]) return;
      var letra = btn.getAttribute("data-letra");
      actual.respuestas[actual.i] = letra;
      marcar(letra);
      pintarPuntaje();
      if (!el.next.disabled) el.next.focus();
    });

    el.prev.addEventListener("click", function () {
      if (actual && actual.i > 0) { actual.i--; pintarPregunta(); }
    });
    el.next.addEventListener("click", function () {
      if (actual && actual.i < actual.preguntas.length - 1) { actual.i++; pintarPregunta(); }
    });

    function cerrarSimulador() {
      turno++;
      actual = null;
      grid.hidden = false;
      vista.hidden = true;
    }
    el.back.addEventListener("click", function () { cerrarSimulador(); mostrarVista(false); });

    /* "Bancos de preguntas" en el menú o el pie siempre regresa a la cuadrícula. */
    var enlaces = document.querySelectorAll('a[href="#bancos"]');
    for (var j = 0; j < enlaces.length; j++) enlaces[j].addEventListener("click", cerrarSimulador);

    pintarGrid();
  });

  /* ---------- cuenta regresiva al próximo sábado 09:00 ---------- */
  safe("countdown", function () {
    var d = document.getElementById("cdD");
    var h = document.getElementById("cdH");
    var m = document.getElementById("cdM");
    var s = document.getElementById("cdS");
    if (!d || !h || !m || !s) return;

    function dosCifras(n) { return n < 10 ? "0" + n : String(n); }

    function proximoSabado() {
      var ahora = new Date();
      var destino = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate(), 9, 0, 0, 0);
      var faltan = (6 - destino.getDay() + 7) % 7;
      destino.setDate(destino.getDate() + faltan);
      if (destino.getTime() <= ahora.getTime()) destino.setDate(destino.getDate() + 7);
      return destino;
    }

    var destino = proximoSabado();

    function tic() {
      var falta = destino.getTime() - Date.now();
      if (falta <= 0) { destino = proximoSabado(); falta = destino.getTime() - Date.now(); }
      var seg = Math.floor(falta / 1000);
      d.textContent = dosCifras(Math.floor(seg / 86400));
      h.textContent = dosCifras(Math.floor(seg / 3600) % 24);
      m.textContent = dosCifras(Math.floor(seg / 60) % 60);
      s.textContent = dosCifras(seg % 60);
    }

    tic();
    setInterval(tic, 1000);
  });

  /* ---------- contadores ---------- */
  safe("contadores", function () {
    var nodos = document.querySelectorAll("[data-count]");
    if (!nodos.length) return;

    function formatear(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }

    function animar(el) {
      var objetivo = parseInt(el.getAttribute("data-count"), 10);
      if (!objetivo || reduced) return;
      var inicio = null, dur = 1100;
      function paso(t) {
        if (inicio === null) inicio = t;
        var p = Math.min((t - inicio) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = formatear(Math.round(objetivo * eased));
        if (p < 1) requestAnimationFrame(paso);
        else el.textContent = formatear(objetivo);
      }
      requestAnimationFrame(paso);
    }

    if (!("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (entradas) {
      for (var k = 0; k < entradas.length; k++) {
        if (entradas[k].isIntersecting) { animar(entradas[k].target); io.unobserve(entradas[k].target); }
      }
    }, { threshold: 0.05 });
    for (var j = 0; j < nodos.length; j++) io.observe(nodos[j]);
  });

  /* ---------- revelado suave con red de seguridad ---------- */
  safe("reveal", function () {
    var nodos = document.querySelectorAll(".reveal");
    if (!nodos.length || !("IntersectionObserver" in window) || reduced) return;

    document.documentElement.classList.add("js-reveal");

    function mostrarTodo() {
      for (var k = 0; k < nodos.length; k++) nodos[k].classList.add("is-in");
    }
    var red = setTimeout(mostrarTodo, 1800);

    var io = new IntersectionObserver(function (entradas) {
      for (var k = 0; k < entradas.length; k++) {
        if (entradas[k].isIntersecting) {
          entradas[k].target.classList.add("is-in");
          io.unobserve(entradas[k].target);
        }
      }
    }, { threshold: 0.05, rootMargin: "0px 0px -40px 0px" });

    for (var j = 0; j < nodos.length; j++) io.observe(nodos[j]);
    window.addEventListener("pagehide", function () { clearTimeout(red); });
  });

  /* ---------- formulario de registro ---------- */
  safe("formulario", function () {
    var form = document.getElementById("signupForm");
    var exito = document.getElementById("signupSuccess");
    if (!form || !exito) return;

    function error(id, mostrar, campo) {
      var el = document.getElementById(id);
      if (el) el.hidden = !mostrar;
      if (campo) campo.setAttribute("aria-invalid", mostrar ? "true" : "false");
      return !mostrar;
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();

      var nombre = document.getElementById("f-nombre");
      var correo = document.getElementById("f-correo");
      var uni = document.getElementById("f-universidad");
      var examen = form.querySelector('input[name="examen"]:checked');

      var okNombre = error("e-nombre", nombre.value.trim().length < 2, nombre);
      var okCorreo = error("e-correo", !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(correo.value.trim()), correo);
      var okUni = error("e-universidad", uni.value === "", uni);
      var okExamen = error("e-examen", !examen, null);

      if (!(okNombre && okCorreo && okUni && okExamen)) {
        var primero = form.querySelector('[aria-invalid="true"]');
        if (primero && primero.focus) primero.focus();
        return;
      }

      var nombreCorto = nombre.value.trim().split(/\s+/)[0];
      var elNombre = document.getElementById("successName");
      var elMsg = document.getElementById("successMsg");
      if (elNombre) elNombre.textContent = nombreCorto;
      if (elMsg) elMsg.textContent = "Tu cuenta gratuita para el " + examen.value + " quedó lista y te guardamos un lugar en el simulacro del sábado.";

      form.hidden = true;
      exito.hidden = false;
      if (exito.scrollIntoView) exito.scrollIntoView({ block: "center", behavior: reduced ? "auto" : "smooth" });
    });
  });

  /* ---------- año del pie ---------- */
  safe("year", function () {
    var el = document.getElementById("year");
    if (el) el.textContent = String(new Date().getFullYear());
  });
  /* ---------- widget de chat (tutor) ----------
     El navegador solo habla con api.php, que es quien guarda la llave y llama
     al modelo de IA. Aquí no hay ninguna credencial. */
  safe("chat", function () {
    var ENDPOINT = "api.php";          // relativo: funciona también en subcarpetas
    var MAX_TURNOS = 10;               // turnos que se reenvían como contexto
    var ESPERA_MAXIMA = 60000;         // ms antes de rendirse con la petición
    var MEMORIA = "medquizpro_chat";   // clave de sessionStorage
    var ERROR_GENERICO = "Lo siento, no pude procesar tu mensaje. Inténtalo nuevamente.";

    var launcher = document.getElementById("chatLauncher");
    var panel = document.getElementById("chatPanel");
    var log = document.getElementById("chatLog");
    var form = document.getElementById("chatForm");
    var input = document.getElementById("chatInput");
    var enviar = document.getElementById("chatSend");
    var bienvenida = document.getElementById("chatWelcome");
    var btnNuevo = document.getElementById("chatNuevo");
    var btnMinimizar = document.getElementById("chatMinimizar");
    var btnCerrar = document.getElementById("chatClose");
    if (!launcher || !panel || !log || !form || !input || !enviar) return;

    var historial = [];
    var enCurso = false;
    var ultimoFoco = null;

    /* ---- memoria de la sesión (se borra al cerrar la pestaña) ---- */
    function guardar() {
      try { sessionStorage.setItem(MEMORIA, JSON.stringify(historial)); } catch (e) {}
    }
    function recuperar() {
      try {
        var crudo = sessionStorage.getItem(MEMORIA);
        var datos = crudo ? JSON.parse(crudo) : null;
        if (datos && datos.length) {
          historial = datos.slice(-MAX_TURNOS * 2);
          for (var k = 0; k < historial.length; k++) {
            burbuja(historial[k].texto, historial[k].rol === "tutor" ? "bot" : "user");
          }
          ocultarBienvenida(true);
        }
      } catch (e) { historial = []; }
    }
    function olvidar() {
      try { sessionStorage.removeItem(MEMORIA); } catch (e) {}
    }

    /* ---- abrir, minimizar, cerrar ---- */
    function abrir() {
      panel.hidden = false;
      launcher.hidden = true;
      launcher.setAttribute("aria-expanded", "true");
      document.body.classList.add("chat-open");
      ultimoFoco = document.activeElement;
      input.focus();
      log.scrollTop = log.scrollHeight;
    }
    /* minimizar: se guarda la conversación y se puede seguir donde se dejó */
    function minimizar() {
      panel.hidden = true;
      launcher.hidden = false;
      launcher.setAttribute("aria-expanded", "false");
      document.body.classList.remove("chat-open");
      if (ultimoFoco && ultimoFoco.focus) ultimoFoco.focus();
      else launcher.focus();
    }
    /* cerrar: además termina la conversación */
    function cerrar() {
      minimizar();
      nuevaConversacion(false);
    }
    function nuevaConversacion(enfocar) {
      historial = [];
      olvidar();
      var hijos = Array.prototype.slice.call(log.children);
      for (var k = 0; k < hijos.length; k++) {
        if (hijos[k] !== bienvenida) log.removeChild(hijos[k]);
      }
      ocultarBienvenida(false);
      input.value = "";
      ajustarAlto();
      if (enfocar !== false) input.focus();
    }
    function ocultarBienvenida(ocultar) {
      if (bienvenida) bienvenida.hidden = !!ocultar;
    }

    launcher.addEventListener("click", abrir);
    if (btnMinimizar) btnMinimizar.addEventListener("click", minimizar);
    if (btnCerrar) btnCerrar.addEventListener("click", cerrar);
    if (btnNuevo) btnNuevo.addEventListener("click", function () { nuevaConversacion(true); });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !panel.hidden) minimizar();
    });

    /* ---- pintado de mensajes ----
       Todo se inserta con textContent: el texto del modelo nunca se interpreta
       como HTML. Solo se reconocen **negritas** y listas con guion. */
    function conNegritas(nodo, texto) {
      var partes = String(texto).split(/\*\*(.+?)\*\*/g);
      for (var k = 0; k < partes.length; k++) {
        if (!partes[k]) continue;
        if (k % 2 === 1) {
          var fuerte = document.createElement("strong");
          fuerte.textContent = partes[k];
          nodo.appendChild(fuerte);
        } else {
          nodo.appendChild(document.createTextNode(partes[k]));
        }
      }
    }

    function pintarTexto(contenedor, texto) {
      var lineas = String(texto).replace(/\r/g, "").split("\n");
      var parrafo = [];
      var lista = null;

      function cerrarParrafo() {
        if (!parrafo.length) return;
        var p = document.createElement("p");
        conNegritas(p, parrafo.join(" "));
        contenedor.appendChild(p);
        parrafo = [];
      }

      for (var k = 0; k < lineas.length; k++) {
        var linea = lineas[k].trim().replace(/^#{1,6}\s*/, "");
        if (!linea) { cerrarParrafo(); lista = null; continue; }

        var vinneta = linea.match(/^[-*•]\s+(.+)$/);
        var numerada = linea.match(/^\d+[.)]\s+(.+)$/);

        if (vinneta || numerada) {
          cerrarParrafo();
          var etiqueta = vinneta ? "ul" : "ol";
          if (!lista || lista.tagName.toLowerCase() !== etiqueta) {
            lista = document.createElement(etiqueta);
            contenedor.appendChild(lista);
          }
          var li = document.createElement("li");
          conNegritas(li, (vinneta || numerada)[1]);
          lista.appendChild(li);
          continue;
        }

        lista = null;
        parrafo.push(linea);
      }
      cerrarParrafo();

      if (!contenedor.childNodes.length) {
        var p = document.createElement("p");
        p.textContent = String(texto);
        contenedor.appendChild(p);
      }
    }

    function burbuja(texto, tipo) {
      var div = document.createElement("div");
      div.className = "chat-msg chat-msg--" + tipo;
      if (tipo === "user") {
        var p = document.createElement("p");
        p.textContent = String(texto);
        div.appendChild(p);
      } else {
        pintarTexto(div, texto);
      }
      log.appendChild(div);
      log.scrollTop = log.scrollHeight;
      return div;
    }

    function escribiendo(mostrar) {
      var previo = document.getElementById("chatTyping");
      if (previo) previo.parentNode.removeChild(previo);
      if (!mostrar) return;
      var d = document.createElement("div");
      d.className = "chat-typing";
      d.id = "chatTyping";
      d.setAttribute("aria-label", "El tutor está escribiendo");
      for (var k = 0; k < 3; k++) d.appendChild(document.createElement("i"));
      log.appendChild(d);
      log.scrollTop = log.scrollHeight;
    }

    function bloquear(si) {
      enCurso = si;
      enviar.disabled = si;
      input.readOnly = si;
      if (btnNuevo) btnNuevo.disabled = si;
    }

    /* ---- envío al servidor ---- */
    function preguntar(texto) {
      if (enCurso) return;
      texto = String(texto || "").trim();
      if (!texto) return;

      ocultarBienvenida(true);
      burbuja(texto, "user");
      input.value = "";
      ajustarAlto();
      bloquear(true);
      escribiendo(true);

      var contexto = historial.slice(-MAX_TURNOS * 2);
      var aborto = null;
      var reloj = null;
      try {
        aborto = new AbortController();
        reloj = setTimeout(function () { aborto.abort(); }, ESPERA_MAXIMA);
      } catch (e) { aborto = null; }

      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({ mensaje: texto, historial: contexto }),
        signal: aborto ? aborto.signal : undefined
      })
        .then(function (res) {
          /* Si el servidor devuelve HTML (un 404, un aviso de PHP), res.json()
             fallaría: se lee como texto y se intenta interpretar. */
          return res.text().then(function (crudo) {
            var datos = null;
            try { datos = JSON.parse(crudo); } catch (e) { datos = null; }
            return { ok: res.ok, estado: res.status, datos: datos };
          });
        })
        .then(function (r) {
          if (reloj) clearTimeout(reloj);
          escribiendo(false);

          var respuesta = r.datos && (r.datos.respuesta || r.datos.reply);
          if (r.ok && typeof respuesta === "string" && respuesta.trim()) {
            respuesta = respuesta.trim();
            burbuja(respuesta, "bot");
            historial.push({ rol: "usuario", texto: texto });
            historial.push({ rol: "tutor", texto: respuesta });
            if (historial.length > MAX_TURNOS * 2) historial = historial.slice(-MAX_TURNOS * 2);
            guardar();
            return;
          }

          var aviso = r.datos && typeof r.datos.error === "string" && r.datos.error
            ? r.datos.error
            : ERROR_GENERICO;
          burbuja(aviso, "error");
        })
        .catch(function () {
          if (reloj) clearTimeout(reloj);
          escribiendo(false);
          burbuja(ERROR_GENERICO, "error");
        })
        .then(function () {
          bloquear(false);
          input.focus();
        });
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      preguntar(input.value);
    });

    /* Enter envía, Mayús+Enter salta de línea */
    input.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" && !ev.shiftKey) {
        ev.preventDefault();
        preguntar(input.value);
      }
    });

    /* la caja de texto crece con el contenido */
    function ajustarAlto() {
      input.style.height = "auto";
      input.style.height = Math.min(input.scrollHeight, 132) + "px";
    }
    input.addEventListener("input", ajustarAlto);

    /* las sugerencias de la pantalla inicial */
    if (bienvenida) {
      bienvenida.addEventListener("click", function (ev) {
        var idea = ev.target.closest ? ev.target.closest(".chat-idea") : null;
        if (idea) preguntar(idea.getAttribute("data-pregunta") || idea.textContent);
      });
    }

    recuperar();
  });

})();
