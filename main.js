/* MedQuizPlus — interacciones de la landing. Script clásico + IIFE, sin dependencias. */
(function () {
  "use strict";

  function safe(name, fn) {
    try { fn(); } catch (err) {
      if (window.console && console.warn) console.warn("[MedQuizPlus] " + name, err);
    }
  }

  var reduced = false;
  try {
    reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) { reduced = false; }

  /* ---------- plantillas compartidas ----------
     La web pública y la plataforma usan el mismo simulador y el mismo chat: cada
     página solo coloca <div data-mqp-practica></div> y <div data-mqp-chat></div>
     donde los quiere, y aquí se montan antes de que el resto de módulos los busque. */
  safe("plantillas", function () {
    var PRACTICA = [
      "<div class=\"sim-view\" id=\"simView\" hidden>",
      "  <div class=\"sim-view__bar\">",
      "    <button class=\"btn btn--ghost btn--sm\" type=\"button\" id=\"svBack\">← Volver</button>",
      "    <div class=\"sim-view__head\">",
      "      <span class=\"badge badge--brand\" id=\"svMode\">Modo estudio</span>",
      "      <p class=\"sim-view__title\" id=\"svTitle\"></p>",
      "    </div>",
      "    <span class=\"sim-view__score\" id=\"svScore\" aria-live=\"polite\"></span>",
      "    <span class=\"sim-clock\" id=\"svClock\" role=\"timer\" aria-label=\"Tiempo restante del simulacro\" hidden>",
      "      <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><circle cx=\"12\" cy=\"13\" r=\"8\"/><path d=\"M12 9v4l2.5 2M9.5 2.5h5\"/></svg>",
      "      <b id=\"svClockTime\">0:00</b>",
      "    </span>",
      "    <button class=\"btn btn--primary btn--sm\" type=\"button\" id=\"svFinish\" hidden>Terminar simulacro</button>",
      "  </div>",
      "",
      "  <div class=\"quiz quiz--wide quiz--pro\" id=\"svQuiz\" aria-live=\"polite\">",
      "    <!-- barra de ritmo: 60 s por pregunta, como en el ENAM -->",
      "    <div class=\"pace\" id=\"svPace\" aria-hidden=\"true\"><div class=\"pace__fill\" id=\"svPaceFill\"></div></div>",
      "    <div class=\"quiz__head\">",
      "      <span class=\"tag\" id=\"svArea\">Especialidad</span>",
      "      <span class=\"tag tag--mark\" id=\"svExam\" hidden></span>",
      "      <span class=\"tag tag--tema\" id=\"svTema\" hidden></span>",
      "      <span class=\"pace__time\" id=\"svPaceTime\" title=\"Tiempo en esta pregunta (ideal: 60 s)\">0:00</span>",
      "      <span class=\"quiz__counter\" id=\"svCounter\"></span>",
      "      <button class=\"fav-btn\" type=\"button\" id=\"svFav\" aria-pressed=\"false\" title=\"Guardar en favoritas\" hidden>",
      "        <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z\"/></svg>",
      "        <span class=\"sr-only\">Guardar en favoritas</span>",
      "      </button>",
      "      <button class=\"flag-btn\" type=\"button\" id=\"svFlag\" aria-pressed=\"false\" title=\"Marcar para revisión (F)\">",
      "        <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M5 21V4\"/><path d=\"M5 4h11l-2 4 2 4H5\"/></svg>",
      "        <span class=\"flag-btn__label\">Marcar</span>",
      "      </button>",
      "    </div>",
      "    <div class=\"quiz__body\">",
      "      <p class=\"sim-view__status\" id=\"svStatus\" hidden></p>",
      "      <div id=\"svContent\" hidden>",
      "        <p class=\"quiz__stem\" id=\"svStem\"></p>",
      "        <div class=\"sim-tools\">",
      "          <label class=\"switch\" title=\"Oculta las alternativas hasta que pases el cursor o las toques\">",
      "            <input type=\"checkbox\" id=\"svRecall\" role=\"switch\">",
      "            <span class=\"switch__track\" aria-hidden=\"true\"><span class=\"switch__thumb\"></span></span>",
      "            <span class=\"switch__text\">Active Recall</span>",
      "          </label>",
      "          <span class=\"sim-tools__hint\">Clic derecho sobre una alternativa para tacharla</span>",
      "        </div>",
      "        <ul class=\"quiz__options\" id=\"svOptions\"></ul>",
      "        <div class=\"quiz__feedback\" id=\"svFeedback\" hidden>",
      "          <p class=\"quiz__verdict\" id=\"svVerdict\"></p>",
      "          <p class=\"quiz__label\">Comentario docente</p>",
      "          <p class=\"quiz__why\" id=\"svWhy\"></p>",
      "          <button class=\"btn btn--ghost btn--sm algo-btn\" type=\"button\" id=\"svAlgo\">",
      "            <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><rect x=\"9\" y=\"2.5\" width=\"6\" height=\"5\" rx=\"1\"/><rect x=\"3\" y=\"16.5\" width=\"6\" height=\"5\" rx=\"1\"/><rect x=\"15\" y=\"16.5\" width=\"6\" height=\"5\" rx=\"1\"/><path d=\"M12 7.5v4M6 16.5V14h12v2.5M12 11.5V14\"/></svg>",
      "            Ver algoritmo / Flujograma",
      "          </button>",
      "        </div>",
      "      </div>",
      "      <div class=\"quiz__foot sim-view__nav\">",
      "        <button class=\"btn btn--ghost\" type=\"button\" id=\"svPrev\">← Pregunta anterior</button>",
      "        <button class=\"btn btn--mark\" type=\"button\" id=\"svNext\">Siguiente pregunta →</button>",
      "      </div>",
      "    </div>",
      "  </div>",
      "",
      "  <details class=\"sim-map\" id=\"svMapWrap\" hidden>",
      "    <summary>Mapa de preguntas <span class=\"sim-map__count\" id=\"svMapCount\"></span></summary>",
      "    <ol class=\"sim-map__list\" id=\"svMap\"></ol>",
      "    <p class=\"sim-map__legend\"><span class=\"is-answered\">Respondida</span><span class=\"is-flagged\">Marcada</span><span class=\"is-current\">Actual</span></p>",
      "  </details>",
      "",
      "  <p class=\"kbd-hints\" id=\"svHints\" aria-label=\"Atajos de teclado\">",
      "    <span><kbd>A</kbd>–<kbd>E</kbd> o <kbd>1</kbd>–<kbd>5</kbd> elegir</span>",
      "    <span><kbd>Espacio</kbd> confirmar / siguiente</span>",
      "    <span><kbd>F</kbd> marcar</span>",
      "    <span><kbd>←</kbd> <kbd>→</kbd> navegar</span>",
      "  </p>",
      "",
      "  <section class=\"sim-result\" id=\"svResult\" tabindex=\"-1\" aria-labelledby=\"svResTitle\" hidden>",
      "    <div class=\"sim-result__top\">",
      "      <div class=\"score-ring score-ring--lg\" id=\"svResRing\" aria-hidden=\"true\">",
      "        <svg viewBox=\"0 0 44 44\"><circle class=\"score-ring__track\" cx=\"22\" cy=\"22\" r=\"18\"/><circle class=\"score-ring__value\" cx=\"22\" cy=\"22\" r=\"18\"/></svg>",
      "        <span class=\"score-ring__num\" id=\"svResPct\">–</span>",
      "      </div>",
      "      <div class=\"sim-result__copy\">",
      "        <p class=\"kicker\" id=\"svResKicker\">Resultado</p>",
      "        <h3 class=\"sim-result__title\" id=\"svResTitle\"></h3>",
      "        <p class=\"sim-result__sub\" id=\"svResSub\"></p>",
      "      </div>",
      "    </div>",
      "    <dl class=\"sim-result__kpis\" id=\"svResKpis\"></dl>",
      "    <div class=\"sim-result__areas\">",
      "      <p class=\"panel__title\">Resultado por especialidad</p>",
      "      <ul class=\"bars bars--wide\" id=\"svResBars\"></ul>",
      "    </div>",
      "    <div class=\"sim-result__actions\">",
      "      <button class=\"btn btn--primary\" type=\"button\" id=\"svReview\">Revisar respuestas</button>",
      "      <button class=\"btn btn--ghost\" type=\"button\" id=\"svRepeat\">Repetir simulacro</button>",
      "      <button class=\"btn btn--ghost\" type=\"button\" id=\"svDone\">Terminar</button>",
      "    </div>",
      "  </section>",
      "</div>",
      "",
      "<!-- modal de algoritmos: el contenido real se registra en algoritmos.js -->",
      "<dialog class=\"algo-modal\" id=\"algoModal\" aria-labelledby=\"algoTitle\">",
      "  <div class=\"algo-modal__head\">",
      "    <div>",
      "      <p class=\"kicker\">Perla clínica</p>",
      "      <h3 class=\"algo-modal__title\" id=\"algoTitle\">Algoritmo diagnóstico</h3>",
      "      <p class=\"algo-modal__sub\" id=\"algoSub\"></p>",
      "    </div>",
      "    <button class=\"chat-tool algo-modal__close\" type=\"button\" id=\"algoClose\">",
      "      <span class=\"sr-only\">Cerrar</span>",
      "      <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" aria-hidden=\"true\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg>",
      "    </button>",
      "  </div>",
      "  <div class=\"algo-modal__body\" id=\"algoBody\"></div>",
      "</dialog>"
    ].join("\n");
    var CHAT = [
      "<button class=\"chat-launcher\" id=\"chatLauncher\" type=\"button\" aria-expanded=\"false\" aria-controls=\"chatPanel\">",
      "  <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\">",
      "    <path d=\"M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-3.6-.7L3 21l1.9-5.1A8.4 8.4 0 0 1 4.1 11a8.4 8.4 0 0 1 8.4-8.4h.5A8.4 8.4 0 0 1 21 11v.5z\"/>",
      "  </svg>",
      "  <span class=\"chat-launcher__label\">Pregúntale al tutor</span>",
      "</button>",
      "",
      "<section class=\"chat-panel\" id=\"chatPanel\" role=\"dialog\" aria-modal=\"false\" aria-labelledby=\"chatTitle\" hidden>",
      "  <header class=\"chat-panel__head\">",
      "    <span class=\"chat-panel__avatar\" aria-hidden=\"true\">",
      "      <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 3v3M7.5 6h9a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-9a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3z\"/><path d=\"M9.5 12h.01M14.5 12h.01M9.5 15.5h5\"/></svg>",
      "    </span>",
      "    <div class=\"chat-panel__id\">",
      "      <h2 class=\"chat-panel__title\" id=\"chatTitle\">Tutor MedQuizPlus</h2>",
      "      <p class=\"chat-panel__sub\">ENAM · RM · EsSalud</p>",
      "    </div>",
      "    <div class=\"chat-tools\">",
      "      <button class=\"chat-tool\" id=\"chatNuevo\" type=\"button\" title=\"Nueva conversación\">",
      "        <span class=\"sr-only\">Empezar una conversación nueva</span>",
      "        <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M3 12a9 9 0 0 1 15.3-6.4L21 8\"/><path d=\"M21 3v5h-5\"/><path d=\"M21 12a9 9 0 0 1-15.3 6.4L3 16\"/><path d=\"M3 21v-5h5\"/></svg>",
      "      </button>",
      "      <button class=\"chat-tool\" id=\"chatMinimizar\" type=\"button\" title=\"Minimizar\">",
      "        <span class=\"sr-only\">Minimizar el chat</span>",
      "        <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" aria-hidden=\"true\"><path d=\"M6 18h12\"/></svg>",
      "      </button>",
      "      <button class=\"chat-tool\" id=\"chatClose\" type=\"button\" title=\"Cerrar y terminar la conversación\">",
      "        <span class=\"sr-only\">Cerrar el chat y terminar la conversación</span>",
      "        <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" aria-hidden=\"true\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg>",
      "      </button>",
      "    </div>",
      "  </header>",
      "",
      "  <div class=\"chat-log\" id=\"chatLog\" role=\"log\" aria-live=\"polite\" aria-relevant=\"additions\">",
      "    <div class=\"chat-welcome\" id=\"chatWelcome\">",
      "      <p class=\"chat-welcome__hola\">Hola <span aria-hidden=\"true\">👋</span></p>",
      "      <p class=\"chat-welcome__sub\">¿En qué puedo ayudarte?</p>",
      "      <div class=\"chat-ideas\">",
      "        <button class=\"chat-idea\" type=\"button\" data-pregunta=\"¿Cómo diferencio un shock séptico de uno cardiogénico?\">",
      "          <strong>Pregúntame algo…</strong>",
      "          <span>¿Cómo diferencio un shock séptico de uno cardiogénico?</span>",
      "        </button>",
      "        <button class=\"chat-idea\" type=\"button\" data-pregunta=\"Explícame los criterios de severidad de la preeclampsia.\">",
      "          <strong>Explícame un tema…</strong>",
      "          <span>Criterios de severidad de la preeclampsia</span>",
      "        </button>",
      "        <button class=\"chat-idea\" type=\"button\" data-pregunta=\"Ayúdame a armar un plan de estudio de cuatro semanas para el ENAM.\">",
      "          <strong>Ayúdame a estudiar…</strong>",
      "          <span>Un plan de cuatro semanas para el ENAM</span>",
      "        </button>",
      "      </div>",
      "      <p class=\"chat-welcome__pie\">O escribe tu propia pregunta abajo.</p>",
      "    </div>",
      "  </div>",
      "",
      "  <form class=\"chat-form\" id=\"chatForm\">",
      "    <label class=\"sr-only\" for=\"chatInput\">Escribe tu pregunta</label>",
      "    <textarea id=\"chatInput\" name=\"mensaje\" rows=\"1\" maxlength=\"2000\" placeholder=\"Escribe tu pregunta…\" autocomplete=\"off\"></textarea>",
      "    <button class=\"chat-send\" id=\"chatSend\" type=\"submit\">",
      "      <span class=\"sr-only\">Enviar</span>",
      "      <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M4 12l16-8-6 16-2.5-6.5L4 12z\"/></svg>",
      "    </button>",
      "  </form>",
      "  <p class=\"chat-disclaimer\">Respuestas generadas por IA con fines de estudio. No sustituyen el criterio clínico ni la atención de un paciente real.</p>",
      "</section>"
    ].join("\n");
    function montar(selector, html) {
      var nodo = document.querySelector(selector);
      if (!nodo) return;
      var tmp = document.createElement("div");
      tmp.innerHTML = html;
      while (tmp.firstChild) nodo.parentNode.insertBefore(tmp.firstChild, nodo);
      nodo.parentNode.removeChild(nodo);
    }
    montar("[data-mqp-practica]", PRACTICA);
    montar("[data-mqp-chat]", CHAT);
  });

  /* ---------- cabecera: sombra al hacer scroll ---------- */
  safe("header", function () {
    var header = document.getElementById("siteHeader");
    if (!header) return;
    var pendiente = false;
    function pintar() {
      pendiente = false;
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    }
    window.addEventListener("scroll", function () {
      if (!pendiente) { pendiente = true; window.requestAnimationFrame(pintar); }
    }, { passive: true });
    pintar();
  });

  /* ---------- menú móvil ---------- */
  safe("nav", function () {
    var toggle = document.getElementById("navToggle");
    var nav = document.getElementById("nav");
    if (!toggle || !nav) return;
    var etiqueta = toggle.querySelector(".sr-only");

    var mq = window.matchMedia("(max-width: 880px)");
    function estado(abierto) {
      toggle.setAttribute("aria-expanded", abierto ? "true" : "false");
      if (etiqueta) etiqueta.textContent = abierto ? "Cerrar menú" : "Abrir menú";
      document.body.classList.toggle("nav-open", abierto && mq.matches);
    }
    function close() {
      estado(false);
      if (mq.matches) nav.hidden = true;
    }
    function sync() { if (mq.matches) { close(); } else { estado(false); nav.hidden = false; } }

    sync();
    if (mq.addEventListener) mq.addEventListener("change", sync);
    else if (mq.addListener) mq.addListener(sync);

    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      if (open) { close(); return; }
      nav.hidden = false;
      estado(true);
      var primero = nav.querySelector("a");
      if (primero) primero.focus({ preventScroll: true });
    });
    nav.addEventListener("click", function (ev) {
      if (ev.target.closest && ev.target.closest("a")) close();
    });
    document.addEventListener("click", function (ev) {
      if (!mq.matches || nav.hidden) return;
      if (!nav.contains(ev.target) && !toggle.contains(ev.target)) close();
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key !== "Escape" || toggle.getAttribute("aria-expanded") !== "true") return;
      close();
      toggle.focus();
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
    var elBar = document.getElementById("qBar");
    var elTimer = document.getElementById("qTimer");
    var elRing = document.getElementById("qRing");
    var elPct = document.getElementById("qPct");
    var elScore = document.getElementById("qScoreText");
    if (!elOpts || !elStem || !elNext) return;

    var sesion = { respondidas: 0, correctas: 0 };

    function pintarSesion() {
      if (!elScore) return;
      var n = sesion.respondidas, c = sesion.correctas;
      var pct = n ? Math.round(c / n * 100) : 0;
      if (elRing) elRing.style.setProperty("--p", String(pct));
      if (elPct) elPct.textContent = n ? pct + "%" : "–";
      elScore.textContent = n ? c + " de " + n + (n === 1 ? " correcta" : " correctas") : "Responde para empezar";
    }

    /* tiempo en la pregunta: el mismo ritmo de 60 s que usa el banco real */
    var inicioPregunta = Date.now(), relojDemo = null;
    function ticDemo() {
      if (!elTimer) return;
      var s = Math.floor((Date.now() - inicioPregunta) / 1000);
      elTimer.textContent = Math.floor(s / 60) + ":" + (s % 60 < 10 ? "0" : "") + (s % 60);
    }
    function arrancarDemo() {
      inicioPregunta = Date.now();
      ticDemo();
      if (relojDemo) clearInterval(relojDemo);
      if (elTimer && !reduced) relojDemo = setInterval(ticDemo, 1000);
    }
    window.addEventListener("pagehide", function () { if (relojDemo) clearInterval(relojDemo); });

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
      if (elBar) elBar.style.width = ((i + 1) / preguntas.length * 100) + "%";
      arrancarDemo();
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

      if (relojDemo) { clearInterval(relojDemo); relojDemo = null; }
      sesion.respondidas++;
      if (acerto) sesion.correctas++;
      pintarSesion();
    });

    elNext.addEventListener("click", function () {
      i = (i + 1) % preguntas.length;
      pintar();
    });

    pintar();
  });

  /* ---------- motor de práctica: bancos, sesiones y simulacros ----------
     Una "sesión" es un conjunto de preguntas reales elegidas con estas opciones:
       { titulo, archivos: [...], examen: "enam", origen: /RegExp/, filtro: "todas" |
         "no-respondidas" | "falladas" | "favoritas", ids: [...], cantidad, orden:
         "secuencial" | "aleatorio", modo: "estudio" | "simulacro", tiempo (s),
         volverTexto, i, respuestas, tipo, simulador, alCerrar() }
     Modo estudio: al responder se ve la clave y el comentario docente (como siempre).
     Modo simulacro: reloj global, se puede cambiar la respuesta, la corrección llega
     al terminar con el resultado por especialidad y la revisión pregunta a pregunta.
     Los bancos se leen con MQP.cargarBanco (catalogo.js). La página anfitriona solo
     necesita un <div data-mqp-practica> y llamar a MQP.practica.abrir(opciones). */
  safe("motor", function () {
    var M = window.MQP;
    var vista = document.getElementById("simView");
    if (!M || !vista) return;

    var $ = function (id) { return document.getElementById(id); };
    var el = {
      back: $("svBack"), title: $("svTitle"), mode: $("svMode"), score: $("svScore"),
      clock: $("svClock"), clockTime: $("svClockTime"), finish: $("svFinish"),
      quiz: $("svQuiz"), area: $("svArea"), exam: $("svExam"), tema: $("svTema"),
      counter: $("svCounter"), fav: $("svFav"), status: $("svStatus"), content: $("svContent"),
      stem: $("svStem"), options: $("svOptions"), feedback: $("svFeedback"),
      verdict: $("svVerdict"), why: $("svWhy"), prev: $("svPrev"), next: $("svNext"),
      mapWrap: $("svMapWrap"), map: $("svMap"), mapCount: $("svMapCount"), hints: $("svHints"),
      result: $("svResult"), resKicker: $("svResKicker"), resTitle: $("svResTitle"), resSub: $("svResSub"),
      resRing: $("svResRing"), resPct: $("svResPct"), resKpis: $("svResKpis"), resBars: $("svResBars"),
      review: $("svReview"), repeat: $("svRepeat"), done: $("svDone")
    };

    var actual = null;   // { cfg, preguntas, i, respuestas, modo, fin, inicio, limite, guardada }
    var turno = 0;       // descarta cargas que llegan tarde
    var reloj = null;

    function revelada(i) { return actual.modo === "estudio" ? !!actual.respuestas[i] : actual.fin; }

    /* Avisos para el módulo del modo simulación (tachado, bandera, ritmo, atajos). */
    function avisar(tipo) {
      if (!actual) { vista.dispatchEvent(new CustomEvent("mqp:" + tipo)); return; }
      var i = actual.i;
      vista.dispatchEvent(new CustomEvent("mqp:" + tipo, { detail: {
        pregunta: actual.preguntas[i], i: i, total: actual.preguntas.length,
        respondida: revelada(i) ? (actual.respuestas[i] || "-") : null,
        elegida: actual.respuestas[i] || null, modo: actual.modo, preguntas: actual.preguntas
      } }));
    }

    function mensaje(texto) {
      el.content.hidden = true;
      el.status.hidden = false;
      el.status.textContent = texto;
      el.counter.textContent = "";
      el.exam.hidden = true;
      el.tema.hidden = true;
      el.fav.hidden = true;
      el.prev.disabled = true;
      el.next.disabled = true;
      el.score.textContent = "";
      el.mapWrap.hidden = true;
    }

    function dos(n) { return (n < 10 ? "0" : "") + n; }
    function reloj2(seg) {
      seg = Math.max(0, Math.ceil(seg));
      var h = Math.floor(seg / 3600), m = Math.floor(seg % 3600 / 60), s = seg % 60;
      return (h ? h + ":" + dos(m) : m) + ":" + dos(s);
    }
    function transcurrido() { return (Date.now() - actual.inicio) / 1000; }

    /* ----- abrir una sesión ----- */
    function abrir(cfg) {
      cfg = cfg || {};
      var mio = ++turno;
      pararReloj();
      if (actual) guardarSesionEstudio();
      actual = null;
      el.title.textContent = cfg.titulo || "Práctica";
      el.back.textContent = "← " + (cfg.volverTexto || "Volver");
      el.area.textContent = cfg.etiqueta || cfg.titulo || "Práctica";
      el.mode.textContent = cfg.modo === "simulacro" ? "Simulacro" : "Modo estudio";
      el.mode.className = "badge" + (cfg.modo === "simulacro" ? " badge--mark" : " badge--brand");
      el.result.hidden = true;
      el.quiz.hidden = false;
      el.clock.hidden = true;
      el.finish.hidden = true;
      if (el.hints) el.hints.hidden = false;
      mensaje("Cargando preguntas…");
      vista.hidden = false;
      document.dispatchEvent(new CustomEvent("mqp:sesion-abierta", { detail: cfg }));

      var archivos = cfg.archivos && cfg.archivos.length ? cfg.archivos
        : M.especialidades.map(function (e) { return e.archivo; });
      Promise.all(archivos.map(function (a) {
        return M.cargarBanco(a).then(function (ps) { return { ok: true, ps: ps }; }, function () { return { ok: false, ps: [] }; });
      })).then(function (res) {
        if (mio !== turno) return;
        var todas = [], fallos = 0;
        for (var k = 0; k < res.length; k++) { if (!res[k].ok) fallos++; todas = todas.concat(res[k].ps); }
        if (fallos === res.length) {
          mensaje("No se pudo cargar " + (archivos.length === 1 ? "el banco de " + (cfg.titulo || "esta especialidad") : "el banco de preguntas") + ". Revisa tu conexión e inténtalo de nuevo.");
          return;
        }
        var lista = M.filtrar(todas, { examen: cfg.examen, origen: cfg.origen, filtro: cfg.filtro, ids: cfg.ids });
        if (!cfg.ids) {
          if (cfg.orden === "aleatorio") lista = M.barajar(lista);
          if (cfg.cantidad) lista = lista.slice(0, cfg.cantidad);
        }
        if (!lista.length) {
          mensaje(cfg.vacio || "Este banco todavía no tiene preguntas publicadas para esta selección. Vuelve pronto.");
          return;
        }
        /* copia por sesión: la bandera y el tachado no se arrastran a la siguiente */
        lista = lista.map(function (q) { var c = {}; for (var p in q) c[p] = q[p]; return c; });
        var modo = cfg.modo === "simulacro" ? "simulacro" : "estudio";
        actual = {
          cfg: cfg, preguntas: lista, modo: modo, fin: false, guardada: false,
          i: Math.max(0, Math.min(cfg.i || 0, lista.length - 1)),
          respuestas: (cfg.respuestas || []).slice(0, lista.length),
          inicio: Date.now(),
          limite: modo === "simulacro" ? (cfg.tiempo || lista.length * 60) : null
        };
        el.map.setAttribute("data-sesion", String(mio));
        el.map.innerHTML = "";
        if (modo === "simulacro") { el.clock.hidden = false; el.finish.hidden = false; iniciarReloj(); }
        pintarPregunta();
      });
    }

    /* ----- reloj global del simulacro ----- */
    function iniciarReloj() {
      pararReloj();
      tic();
      reloj = setInterval(tic, 500);
    }
    function pararReloj() { if (reloj) { clearInterval(reloj); reloj = null; } }
    function tic() {
      if (!actual || actual.modo !== "simulacro" || actual.fin) { pararReloj(); return; }
      var queda = actual.limite - transcurrido();
      el.clockTime.textContent = reloj2(queda);
      el.clock.classList.toggle("is-warn", queda <= Math.min(300, actual.limite * 0.15) && queda > 60);
      el.clock.classList.toggle("is-over", queda <= 60);
      if (queda <= 0) terminar(true);
    }

    /* ----- pintado ----- */
    function contar() {
      var hechas = 0, bien = 0;
      for (var k = 0; k < actual.preguntas.length; k++) {
        var r = actual.respuestas[k];
        if (r) { hechas++; if (r === actual.preguntas[k].clave) bien++; }
      }
      return { hechas: hechas, bien: bien, total: actual.preguntas.length };
    }

    function pintarPuntaje() {
      var c = contar();
      if (actual.modo === "simulacro" && !actual.fin) el.score.textContent = "Respondidas: " + c.hechas + " de " + c.total;
      else el.score.textContent = c.hechas ? ("Aciertos: " + c.bien + " de " + c.hechas + " respondidas") : "";
    }

    function pintarMapa() {
      var n = actual.preguntas.length;
      if (el.map.childNodes.length !== n) {
        el.map.innerHTML = "";
        for (var k = 0; k < n; k++) {
          var li = document.createElement("li");
          var b = document.createElement("button");
          b.type = "button";
          b.className = "sim-map__item";
          b.textContent = String(k + 1);
          b.setAttribute("data-i", String(k));
          li.appendChild(b);
          el.map.appendChild(li);
        }
      }
      var botones = el.map.querySelectorAll(".sim-map__item");
      for (var j = 0; j < botones.length; j++) {
        var q = actual.preguntas[j], r = actual.respuestas[j];
        var b2 = botones[j];
        b2.className = "sim-map__item" +
          (j === actual.i ? " is-current" : "") +
          (r ? " is-answered" : "") +
          (r && revelada(j) ? (r === q.clave ? " is-right" : " is-wrong") : "") +
          (q.marcada ? " is-flagged" : "");
        var estado = !r ? "sin responder" : (revelada(j) ? (r === q.clave ? "correcta" : "incorrecta") : "respondida");
        b2.setAttribute("aria-label", "Pregunta " + (j + 1) + ", " + estado + (q.marcada ? ", marcada" : ""));
        if (j === actual.i) b2.setAttribute("aria-current", "true"); else b2.removeAttribute("aria-current");
      }
      var c = contar();
      el.mapCount.textContent = c.hechas + "/" + c.total;
      el.mapWrap.hidden = n < 2;
    }

    function pintarFavorita() {
      var q = actual.preguntas[actual.i];
      var on = M.progreso.esFavorita(q.id);
      el.fav.hidden = !q.id;
      el.fav.setAttribute("aria-pressed", on ? "true" : "false");
      el.fav.title = on ? "Quitar de favoritas" : "Guardar en favoritas";
      el.fav.querySelector(".sr-only").textContent = on ? "Quitar de favoritas" : "Guardar en favoritas";
    }

    function pintarPregunta() {
      var q = actual.preguntas[actual.i];
      var total = actual.preguntas.length;
      el.status.hidden = true;
      el.content.hidden = false;
      el.counter.textContent = "Pregunta " + (actual.i + 1) + " de " + total;
      el.area.textContent = q.especialidad || actual.cfg.titulo || "";
      el.exam.hidden = !q.examen;
      el.exam.textContent = q.examen;
      el.tema.hidden = !q.tema;
      el.tema.textContent = q.tema;
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

      if (revelada(actual.i)) marcar(actual.respuestas[actual.i] || null);
      else { el.feedback.hidden = true; pintarElegida(); }

      el.prev.disabled = actual.i === 0;
      var ultima = actual.i >= total - 1;
      if (ultima && actual.modo === "estudio") {
        el.next.textContent = "Ver resumen →";
        el.next.disabled = !contar().hechas;
      } else if (ultima && actual.modo === "simulacro" && !actual.fin) {
        el.next.textContent = "Terminar simulacro";
        el.next.disabled = false;
      } else if (ultima) {
        el.next.textContent = "Ver resultado →";
        el.next.disabled = false;
      } else {
        el.next.textContent = "Siguiente pregunta →";
        el.next.disabled = false;
      }
      pintarPuntaje();
      pintarFavorita();
      pintarMapa();
      guardarUltima();
      avisar("pregunta");
    }

    function pintarElegida() {
      var elegida = actual.respuestas[actual.i];
      var botones = el.options.querySelectorAll(".opt");
      for (var k = 0; k < botones.length; k++) {
        var on = botones[k].getAttribute("data-letra") === elegida;
        botones[k].classList.toggle("opt--chosen", on);
        botones[k].setAttribute("aria-pressed", on ? "true" : "false");
      }
    }

    function marcar(elegida) {
      var q = actual.preguntas[actual.i];
      var botones = el.options.querySelectorAll(".opt");
      for (var k = 0; k < botones.length; k++) {
        var letra = botones[k].getAttribute("data-letra");
        botones[k].disabled = true;
        botones[k].removeAttribute("aria-pressed");
        if (letra === q.clave) botones[k].classList.add("opt--right");
        else if (letra === elegida) botones[k].classList.add("opt--wrong");
      }
      var acerto = elegida === q.clave;
      el.verdict.textContent = !elegida
        ? "Sin responder · la correcta es la " + q.clave
        : acerto ? "Respuesta correcta" : "Respuesta incorrecta · la correcta es la " + q.clave;
      el.verdict.className = "quiz__verdict " + (acerto ? "quiz__verdict--ok" : "quiz__verdict--bad");
      el.why.textContent = q.comentario || "Esta pregunta todavía no tiene comentario docente.";
      el.feedback.hidden = false;
    }

    /* ----- responder ----- */
    el.options.addEventListener("click", function (ev) {
      var btn = ev.target.closest ? ev.target.closest(".opt") : null;
      if (!btn || !actual || btn.disabled) return;
      var letra = btn.getAttribute("data-letra");
      var q = actual.preguntas[actual.i];
      if (actual.modo === "estudio") {
        if (actual.respuestas[actual.i]) return;
        actual.respuestas[actual.i] = letra;
        marcar(letra);
        M.progreso.registrar(q, letra);
        pintarPuntaje();
        pintarMapa();
        if (actual.i >= actual.preguntas.length - 1) el.next.disabled = false;
        guardarUltima();
        avisar("respondida");
        if (!el.next.disabled) el.next.focus();
      } else {
        if (actual.fin) return;
        actual.respuestas[actual.i] = letra;
        pintarElegida();
        pintarPuntaje();
        pintarMapa();
        avisar("elegida");
      }
    });

    function ir(i) {
      if (!actual || i < 0 || i >= actual.preguntas.length) return;
      actual.i = i;
      pintarPregunta();
    }
    el.prev.addEventListener("click", function () { if (actual) ir(actual.i - 1); });
    el.next.addEventListener("click", function () {
      if (!actual) return;
      if (actual.i < actual.preguntas.length - 1) { ir(actual.i + 1); return; }
      if (actual.modo === "simulacro" && !actual.fin) { pedirTerminar(el.next); return; }
      mostrarResultado();
    });
    el.map.addEventListener("click", function (ev) {
      var b = ev.target.closest ? ev.target.closest(".sim-map__item") : null;
      if (b) ir(parseInt(b.getAttribute("data-i"), 10));
    });
    vista.addEventListener("mqp:marcada", function () { if (actual) pintarMapa(); });

    el.fav.addEventListener("click", function () {
      if (!actual) return;
      M.progreso.alternarFavorita(actual.preguntas[actual.i].id);
      pintarFavorita();
    });

    /* Botones que piden confirmación con un segundo clic (sin diálogos nativos). */
    function enDosPasos(btn, pregunta, accion) {
      if (btn.getAttribute("data-armado") === "1") {
        btn.removeAttribute("data-armado");
        btn.textContent = btn.getAttribute("data-texto") || btn.textContent;
        btn.classList.remove("is-armed");
        accion();
        return;
      }
      btn.setAttribute("data-texto", btn.textContent);
      btn.setAttribute("data-armado", "1");
      btn.classList.add("is-armed");
      btn.textContent = pregunta;
      setTimeout(function () {
        if (btn.getAttribute("data-armado") !== "1") return;
        btn.removeAttribute("data-armado");
        btn.classList.remove("is-armed");
        btn.textContent = btn.getAttribute("data-texto");
      }, 4000);
    }

    function pedirTerminar(btn) {
      if (!actual || actual.fin) return;
      var sin = actual.preguntas.length - contar().hechas;
      if (!sin) { terminar(false); return; }
      enDosPasos(btn, "¿Terminar? " + M.plural(sin, "queda sin responder", "quedan sin responder"), function () { terminar(false); });
    }
    el.finish.addEventListener("click", function () { pedirTerminar(el.finish); });

    /* ----- terminar y resultados ----- */
    function terminar(porTiempo) {
      if (!actual || actual.modo !== "simulacro" || actual.fin) return;
      actual.fin = true;
      actual.duracion = Math.min(transcurrido(), actual.limite);
      actual.porTiempo = !!porTiempo;
      pararReloj();
      el.clock.hidden = true;
      el.finish.hidden = true;
      var lista = [];
      for (var k = 0; k < actual.preguntas.length; k++) {
        if (actual.respuestas[k]) lista.push({ q: actual.preguntas[k], letra: actual.respuestas[k] });
      }
      M.progreso.registrarVarias(lista);
      guardarSesion();
      mostrarResultado();
    }

    function guardarSesion() {
      if (!actual || actual.guardada) return;
      var c = contar();
      if (!c.hechas && actual.modo === "estudio") return;
      actual.guardada = true;
      M.progreso.agregarSesion({
        tipo: actual.modo, titulo: actual.cfg.titulo || "Práctica", simulador: actual.cfg.simulador || null,
        examen: actual.cfg.examen || null, total: c.total, respondidas: c.hechas, correctas: c.bien,
        duracion: Math.round(actual.duracion || transcurrido())
      });
    }
    function guardarSesionEstudio() { if (actual && actual.modo === "estudio") guardarSesion(); }

    function guardarUltima() {
      if (!actual || actual.modo !== "estudio" || actual.cfg.noGuardar) return;
      var c = contar();
      if (c.hechas >= c.total) { M.progreso.limpiarUltima(); return; }
      M.progreso.guardarUltima({
        titulo: actual.cfg.titulo || "Práctica", archivos: actual.cfg.archivos || null,
        ids: actual.preguntas.map(function (q) { return q.id; }), i: actual.i,
        respuestas: actual.respuestas.slice(), total: c.total, respondidas: c.hechas, correctas: c.bien,
        especialidad: actual.preguntas[actual.i].especialidad || "", t: Date.now()
      });
    }

    function mostrarResultado() {
      if (!actual) return;
      if (actual.modo === "estudio") guardarSesion();
      var c = contar();
      var simulacro = actual.modo === "simulacro";
      var pct = c.total ? Math.round(c.bien / c.total * 100) : 0;
      el.resKicker.textContent = simulacro ? "Resultado del simulacro" : "Resumen de la sesión";
      el.resTitle.textContent = actual.cfg.titulo || "Práctica";
      el.resSub.textContent = simulacro
        ? (actual.porTiempo ? "Se acabó el tiempo. " : "") + "Revisa cada pregunta con su comentario docente y su flujograma."
        : "Tus respuestas quedaron guardadas en tu progreso.";
      el.resRing.style.setProperty("--p", String(pct));
      el.resPct.textContent = pct + "%";
      var kpis = [
        ["Correctas", c.bien + " / " + c.total],
        ["Incorrectas", String(c.hechas - c.bien)],
        ["Sin responder", String(c.total - c.hechas)]
      ];
      if (simulacro) kpis.push(["Tiempo usado", M.duracion(actual.duracion) + " de " + M.duracion(actual.limite)]);
      el.resKpis.innerHTML = "";
      for (var k = 0; k < kpis.length; k++) {
        var d = document.createElement("div");
        var dt = document.createElement("dt"); dt.textContent = kpis[k][0];
        var dd = document.createElement("dd"); dd.textContent = kpis[k][1];
        d.appendChild(dt); d.appendChild(dd); el.resKpis.appendChild(d);
      }
      /* resultado por especialidad */
      var grupos = {}, orden = [];
      for (var j = 0; j < actual.preguntas.length; j++) {
        var q = actual.preguntas[j];
        var g = grupos[q.especialidad] || (grupos[q.especialidad] = { total: 0, bien: 0 });
        if (!g.total) orden.push(q.especialidad);
        g.total++;
        if (actual.respuestas[j] === q.clave) g.bien++;
      }
      el.resBars.innerHTML = "";
      for (var m = 0; m < orden.length; m++) {
        var gr = grupos[orden[m]], v = Math.round(gr.bien / gr.total * 100);
        var li = document.createElement("li");
        li.className = "bars__row";
        li.innerHTML = '<span class="bars__label"></span><span class="bars__track"><span class="bars__fill"></span></span><span class="bars__val"></span>';
        li.querySelector(".bars__label").textContent = orden[m];
        li.querySelector(".bars__fill").style.setProperty("--v", String(v));
        li.querySelector(".bars__val").textContent = gr.bien + "/" + gr.total;
        li.title = orden[m] + ": " + gr.bien + " de " + gr.total + " correctas";
        el.resBars.appendChild(li);
      }
      el.review.hidden = !simulacro;
      el.repeat.textContent = simulacro ? "Repetir simulacro" : "Practicar de nuevo";
      el.quiz.hidden = true;
      el.content.hidden = true;   // detiene el reloj de ritmo
      el.mapWrap.hidden = true;
      if (el.hints) el.hints.hidden = true;
      el.result.hidden = false;
      el.score.textContent = "";
      el.result.focus({ preventScroll: true });
      scrollAVista();
      avisar("resultado");
    }

    el.review.addEventListener("click", function () {
      if (!actual) return;
      el.result.hidden = true;
      el.quiz.hidden = false;
      if (el.hints) el.hints.hidden = false;
      ir(0);
      scrollAVista();
    });
    el.repeat.addEventListener("click", function () {
      if (!actual) return;
      var cfg = {};
      for (var p in actual.cfg) cfg[p] = actual.cfg[p];
      delete cfg.i; delete cfg.respuestas;
      if (cfg.repetirIds === false) delete cfg.ids;
      if (cfg.orden === "aleatorio") delete cfg.ids;
      abrir(cfg);
    });
    el.done.addEventListener("click", function () { cerrar(); });

    function scrollAVista() {
      var r = vista.getBoundingClientRect();
      if (r.top < 0 || r.top > window.innerHeight * 0.6) vista.scrollIntoView({ block: "start", behavior: reduced ? "auto" : "smooth" });
    }

    /* ----- cerrar ----- */
    function cerrar() {
      var cfg = actual ? actual.cfg : null;
      guardarSesionEstudio();
      turno++;
      pararReloj();
      actual = null;
      vista.hidden = true;
      avisar("cerrado");
      document.dispatchEvent(new CustomEvent("mqp:sesion-cerrada", { detail: cfg }));
      if (cfg && typeof cfg.alCerrar === "function") cfg.alCerrar();
    }
    el.back.addEventListener("click", function () {
      if (actual && actual.modo === "simulacro" && !actual.fin && contar().hechas) {
        enDosPasos(el.back, "¿Salir? Perderás este simulacro", cerrar);
        return;
      }
      cerrar();
    });

    M.practica = {
      abrir: abrir,
      cerrar: function () { if (!vista.hidden) cerrar(); },
      activa: function () { return !vista.hidden; }
    };
  });

  /* ---------- componentes de interfaz compartidos por la web y la plataforma ---------- */
  safe("ui", function () {
    var M = window.MQP;
    if (!M) return;

    /* Tarjeta de especialidad. info: { estado: "cargando" | "ok" | "vacio" | "error",
       total, respondidas, correctas, tipo } */
    function tarjetaEspecialidad(esp, k, alEntrenar) {
      var area = M.area(esp.area);
      var card = document.createElement("article");
      card.className = "spec";
      card.setAttribute("data-tono", String(k % 6));
      card.style.setProperty("--i", String(k));
      card.innerHTML =
        '<div class="spec__top">' +
          '<span class="spec__icon">' + M.icono(esp.icono) + '</span>' +
          '<span class="spec__status">Verificando</span>' +
        '</div>' +
        '<p class="spec__area"></p>' +
        '<h3 class="spec__name"></h3>' +
        '<p class="spec__meta">' + M.icono("libro") + '<span>Contando preguntas…</span></p>' +
        '<div class="spec__progress" hidden><span class="spec__track"><span class="spec__fill"></span></span><span class="spec__ptext"></span></div>' +
        '<button class="btn spec__cta" type="button"><span class="spec__cta-text">Entrenar</span>' + M.icono("flecha", "btn__arrow") + '</button>';
      card.querySelector(".spec__area").textContent = area ? area.nombre : "";
      card.querySelector(".spec__name").textContent = esp.nombre;
      var pill = card.querySelector(".spec__status");
      var meta = card.querySelector(".spec__meta span");
      var prog = card.querySelector(".spec__progress");
      var btn = card.querySelector(".spec__cta");
      var btnTxt = card.querySelector(".spec__cta-text");
      btn.setAttribute("aria-label", "Entrenar " + esp.nombre);
      btn.addEventListener("click", function () { if (!btn.disabled) alEntrenar(esp); });

      function actualizar(info) {
        info = info || {};
        pill.hidden = false;
        card.classList.remove("spec--soon");
        btn.disabled = false;
        btnTxt.textContent = "Entrenar";
        prog.hidden = true;
        if (info.estado === "cargando") {
          pill.className = "spec__status"; pill.textContent = "Verificando";
          meta.textContent = "Contando preguntas…";
        } else if (info.estado === "error") {
          pill.className = "spec__status spec__status--off"; pill.textContent = "No disponible";
          meta.textContent = "No se pudo cargar por ahora";
        } else if (!info.total) {
          card.classList.add("spec--soon");
          pill.className = "spec__status spec__status--soon"; pill.textContent = "Próximamente";
          pill.hidden = true;   // el botón ya lo dice
          meta.textContent = "Preguntas en preparación";
          btn.disabled = true;
          btnTxt.textContent = "Próximamente";
        } else {
          pill.className = "spec__status spec__status--ok"; pill.textContent = "Disponible";
          pill.hidden = true;   // solo se muestran los estados que informan algo
          meta.textContent = M.plural(info.total, info.tipo ? "pregunta tipo" : "pregunta comentada", info.tipo ? "preguntas tipo" : "preguntas comentadas");
          if (info.respondidas) {
            prog.hidden = false;
            var v = Math.min(100, Math.round(info.respondidas / info.total * 100));
            prog.querySelector(".spec__fill").style.width = v + "%";
            prog.querySelector(".spec__ptext").textContent = info.respondidas + " de " + info.total + " respondidas";
            btnTxt.textContent = "Seguir entrenando";
          }
        }
      }
      actualizar({ estado: "cargando" });
      return { nodo: card, actualizar: actualizar };
    }

    /* Conteo real de preguntas por examen y especialidad a partir de los bancos. */
    function contarPorExamen(datos) {
      var c = {};
      for (var k = 0; k < M.examenes.length; k++) c[M.examenes[k].id] = { total: 0, oficiales: 0, porArchivo: {}, anios: {} };
      for (var j = 0; j < datos.preguntas.length; j++) {
        var q = datos.preguntas[j];
        var e = c[q.examenId];
        if (!e) continue;
        e.total++;
        e.porArchivo[q.archivo] = (e.porArchivo[q.archivo] || 0) + 1;
        if (q.oficial) { e.oficiales++; if (q.anio) e.anios[q.anio] = true; }
      }
      return c;
    }

    /* Respuestas del estudiante limitadas a un examen, por especialidad. */
    function progresoPorArchivo(examen) {
      return M.progreso.resumen(examen).porArchivo;
    }

    M.ui = { tarjetaEspecialidad: tarjetaEspecialidad, contarPorExamen: contarPorExamen, progresoPorArchivo: progresoPorArchivo };
  });

  /* ---------- web pública: explorador de bancos por examen ---------- */
  safe("explorador", function () {
    var M = window.MQP;
    var raiz = document.getElementById("bankExplorer");
    var grid = document.getElementById("specs");
    if (!M || !M.ui || !raiz || !grid) return;

    var tabs = document.querySelectorAll("#examTabs [role=tab]");
    var chipsBox = document.getElementById("areaChips");
    var el = {
      title: document.getElementById("exTitle"), lead: document.getElementById("exLead"),
      stats: document.getElementById("exStats"), soon: document.getElementById("exSoon"),
      soonText: document.getElementById("exSoonText"), soonBtn: document.getElementById("exSoonBtn")
    };
    var examen = "enam", area = "", datos = null, conteo = null, tarjetas = {};

    /* tarjetas: una por especialidad (ordenadas por área), se reutilizan al cambiar de examen */
    var ordenAreas = M.areas.map(function (a) { return a.id; });
    var lista = M.especialidades.slice().sort(function (a, b) { return ordenAreas.indexOf(a.area) - ordenAreas.indexOf(b.area); });
    for (var k = 0; k < lista.length; k++) {
      var t = M.ui.tarjetaEspecialidad(lista[k], k, function (esp) {
        var ex = M.examen(examen);
        M.practica.abrir({
          titulo: esp.nombre + (examen !== "enam" ? " · " + ex.nombre : ""), archivos: [esp.archivo], examen: examen,
          volverTexto: "Volver a especialidades"
        });
      });
      tarjetas[lista[k].archivo] = t;
      t.nodo.setAttribute("data-area", lista[k].area);
      grid.appendChild(t.nodo);
    }

    /* filtros por área */
    function pintarChips() {
      var html = '<button class="chip" type="button" data-area="" aria-pressed="' + (!area) + '">Todas las áreas</button>';
      for (var j = 0; j < M.areas.length; j++) {
        html += '<button class="chip" type="button" data-area="' + M.areas[j].id + '" aria-pressed="' + (area === M.areas[j].id) + '">' + M.areas[j].nombre + "</button>";
      }
      chipsBox.innerHTML = html;
    }
    chipsBox.addEventListener("click", function (ev) {
      var b = ev.target.closest ? ev.target.closest(".chip") : null;
      if (!b) return;
      area = b.getAttribute("data-area");
      pintarChips();
      filtrarArea();
    });
    function filtrarArea() {
      for (var a in tarjetas) tarjetas[a].nodo.hidden = !!area && tarjetas[a].nodo.getAttribute("data-area") !== area;
    }

    function pintar() {
      var ex = M.examen(examen);
      el.title.textContent = ex.titulo;
      el.lead.textContent = ex.lema;
      var info = conteo ? conteo[examen] : null;
      var prog = M.ui.progresoPorArchivo(examen);
      for (var a in tarjetas) {
        if (!datos) { tarjetas[a].actualizar({ estado: "cargando" }); continue; }
        var ok = datos.porArchivo[a] && datos.porArchivo[a].ok;
        var p = prog[a] || {};
        tarjetas[a].actualizar(ok
          ? { estado: "ok", total: info.porArchivo[a] || 0, respondidas: p.respondidas || 0, tipo: ex.estado !== "disponible" }
          : { estado: "error" });
      }
      /* resumen del examen, solo con datos contados */
      el.stats.innerHTML = "";
      if (info) {
        var n = 0;
        for (var b in info.porArchivo) if (info.porArchivo[b]) n++;
        var items = [];
        if (info.total) items.push(M.plural(info.total, ex.estado === "disponible" ? "pregunta comentada" : "pregunta tipo", ex.estado === "disponible" ? "preguntas comentadas" : "preguntas tipo"));
        if (n && ex.estado === "disponible") items.push(M.plural(n, "especialidad", "especialidades"));
        if (info.oficiales) items.push(info.oficiales + " oficiales ENAM " + Object.keys(info.anios).sort().join(", "));
        if (ex.estado === "disponible") items.push("Comentario y flujograma en cada pregunta");
        for (var i = 0; i < items.length; i++) {
          var li = document.createElement("li");
          li.innerHTML = M.icono("check");
          li.appendChild(document.createTextNode(items[i]));
          el.stats.appendChild(li);
        }
      }
      /* Residentado y EsSalud: módulo visible, banco completo próximamente */
      el.soon.hidden = ex.estado === "disponible";
      if (ex.estado !== "disponible") {
        var tipo = info ? info.total : 0;
        el.soonText.textContent = tipo
          ? "Estamos construyendo el banco completo por especialidad. Mientras tanto ya puedes resolver " + M.plural(tipo, "pregunta tipo publicada", "preguntas tipo publicadas") + "."
          : "Estamos construyendo el banco completo por especialidad.";
        el.soonBtn.hidden = !tipo;
        el.soonBtn.textContent = "Practicar " + M.plural(tipo, "pregunta tipo", "preguntas tipo");
      }
    }
    el.soonBtn.addEventListener("click", function () {
      var ex = M.examen(examen);
      M.practica.abrir({ titulo: ex.nombre + " · preguntas tipo", examen: examen, volverTexto: "Volver a especialidades" });
    });

    /* pestañas accesibles (flechas para moverse entre exámenes) */
    function elegir(id, enfocar) {
      examen = M.examen(id) ? id : "enam";
      for (var j = 0; j < tabs.length; j++) {
        var on = tabs[j].getAttribute("data-examen") === examen;
        tabs[j].setAttribute("aria-selected", on ? "true" : "false");
        tabs[j].tabIndex = on ? 0 : -1;
        if (on && enfocar) tabs[j].focus();
      }
      pintar();
    }
    for (var j = 0; j < tabs.length; j++) {
      tabs[j].addEventListener("click", function () { M.practica.cerrar(); elegir(this.getAttribute("data-examen")); });
      tabs[j].addEventListener("keydown", function (ev) {
        var i = Array.prototype.indexOf.call(tabs, this), n = tabs.length;
        if (ev.key === "ArrowRight" || ev.key === "ArrowLeft") {
          ev.preventDefault();
          var sig = tabs[(i + (ev.key === "ArrowRight" ? 1 : n - 1)) % n];
          elegir(sig.getAttribute("data-examen"), true);
        }
      });
    }
    /* "Explorar ENAM / Residentado / EsSalud" desde cualquier parte de la página */
    document.addEventListener("click", function (ev) {
      var a = ev.target.closest ? ev.target.closest("[data-ir-examen]") : null;
      if (!a) return;
      M.practica.cerrar();
      elegir(a.getAttribute("data-ir-examen"));
    });

    /* mientras hay una sesión abierta se oculta el explorador */
    document.addEventListener("mqp:sesion-abierta", function () {
      raiz.hidden = true;
      var sec = document.getElementById("bancos");
      if (sec && sec.scrollIntoView) sec.scrollIntoView({ block: "start", behavior: reduced ? "auto" : "smooth" });
    });
    document.addEventListener("mqp:sesion-cerrada", function () {
      raiz.hidden = false;
      pintar();
      var sec = document.getElementById("bancos");
      if (sec && sec.scrollIntoView) sec.scrollIntoView({ block: "start", behavior: reduced ? "auto" : "smooth" });
    });
    /* "Bancos de preguntas" en el menú o el pie siempre regresa al explorador */
    var enlaces = document.querySelectorAll('a[href="#bancos"]');
    for (var e = 0; e < enlaces.length; e++) enlaces[e].addEventListener("click", function () { M.practica.cerrar(); });

    pintarChips();
    elegir("enam");

    /* cuenta las preguntas cuando la sección se acerca a la pantalla */
    function contar() {
      M.cargarTodo().then(function (d) {
        datos = d;
        conteo = M.ui.contarPorExamen(d);
        pintar();
      });
    }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entradas) {
        if (entradas[0].isIntersecting) { io.disconnect(); contar(); }
      }, { rootMargin: "400px 0px" });
      io.observe(raiz);
    } else {
      contar();
    }
    window.addEventListener("mqp:progreso", function () { if (datos) pintar(); });
  });

  /* ---------- web pública: cifras y simuladores calculados con los bancos ----------
     Nada de números de ejemplo: el HTML trae los valores actuales como respaldo y
     aquí se recalculan con las preguntas que realmente hay publicadas. */
  safe("cifras", function () {
    var M = window.MQP;
    var nodos = document.querySelectorAll("[data-metrica], [data-sim]");
    if (!M || !M.ui || !nodos.length) return;

    function animar(el, n) {
      var antes = parseInt(String(el.textContent).replace(/\D/g, ""), 10);
      if (reduced || !isFinite(antes) || antes === n) { el.textContent = M.miles(n); return; }
      var inicio = null, dur = 700;
      function paso(t) {
        if (inicio === null) inicio = t;
        var p = Math.min((t - inicio) / dur, 1);
        el.textContent = M.miles(Math.round(antes + (n - antes) * (1 - Math.pow(1 - p, 3))));
        if (p < 1) requestAnimationFrame(paso);
      }
      requestAnimationFrame(paso);
    }

    function calcular(d) {
      var conteo = M.ui.contarPorExamen(d);
      var algos = window.MQP_ALGORITMOS || {};
      var flujos = 0, especialidades = 0;
      for (var k = 0; k < d.preguntas.length; k++) {
        var a = algos[d.preguntas[k].id];
        if (a && (a.imagen || (a.pasos && a.pasos.length))) flujos++;
      }
      for (var ar in d.porArchivo) if (d.porArchivo[ar].preguntas.length) especialidades++;
      var enam = conteo.enam;
      var valores = {
        preguntas: d.preguntas.length, especialidades: especialidades, flujogramas: flujos,
        oficiales: enam.oficiales, enam: enam.total
      };
      var met = document.querySelectorAll("[data-metrica]");
      for (var j = 0; j < met.length; j++) {
        var clave = met[j].getAttribute("data-metrica");
        if (clave === "anios") { met[j].textContent = Object.keys(enam.anios).sort().join(", ") || met[j].textContent; continue; }
        if (clave.indexOf("rm") === 0 || clave.indexOf("essalud") === 0) {
          var ex = conteo[clave === "rm" ? "residentado" : "essalud"];
          met[j].textContent = ex ? String(ex.total) : met[j].textContent;
          continue;
        }
        if (valores[clave] != null) animar(met[j], valores[clave]);
      }
      /* tarjetas de simuladores: preguntas y tiempo reales */
      var sims = document.querySelectorAll("[data-sim]");
      for (var s = 0; s < sims.length; s++) {
        var sim = M.simulador(sims[s].getAttribute("data-sim"));
        if (!sim || sim.estado !== "disponible") continue;
        var disponibles = M.filtrar(d.preguntas, { examen: sim.examen, origen: sim.origen });
        var n = sim.cantidad ? Math.min(sim.cantidad, disponibles.length) : disponibles.length;
        var areas = {};
        for (var q = 0; q < disponibles.length; q++) areas[disponibles[q].archivo] = true;
        var nN = sims[s].querySelector("[data-sim-n]"), nT = sims[s].querySelector("[data-sim-t]"), nE = sims[s].querySelector("[data-sim-e]");
        if (nN && !sim.eligeEspecialidad) nN.textContent = String(n);
        if (nT && !sim.eligeEspecialidad) nT.textContent = M.duracion(n * sim.segundosPorPregunta);
        if (nE) nE.textContent = String(Object.keys(areas).length);
      }
    }

    var hecho = false;
    function cargar() { if (hecho) return; hecho = true; M.cargarTodo().then(calcular, function () { hecho = false; }); }
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entradas) {
        for (var k = 0; k < entradas.length; k++) if (entradas[k].isIntersecting) { io.disconnect(); cargar(); return; }
      }, { rootMargin: "200px 0px" });
      for (var j = 0; j < nodos.length; j++) io.observe(nodos[j]);
    } else {
      cargar();
    }
  });

  /* ---------- tema claro / oscuro persistente ----------
     La preferencia se guarda en localStorage ("mqp_tema"). Un script en el <head>
     la aplica antes de pintar; aquí solo se maneja el botón. */
  safe("tema", function () {
    var btn = document.getElementById("themeToggle");
    var raiz = document.documentElement;
    var etiqueta = btn ? btn.querySelector(".theme-btn__label") : null;
    var sistema = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

    function actual() {
      var t = raiz.getAttribute("data-theme");
      if (t === "dark" || t === "light") return t;
      return sistema && sistema.matches ? "dark" : "light";
    }
    function pintar() {
      var oscuro = actual() === "dark";
      if (btn) {
        btn.setAttribute("aria-pressed", oscuro ? "true" : "false");
        if (etiqueta) etiqueta.textContent = oscuro ? "Modo claro" : "Modo oscuro";
        btn.title = oscuro ? "Cambiar a modo claro" : "Cambiar a modo oscuro";
      }
      var metas = document.querySelectorAll('meta[name="theme-color"]');
      for (var k = 0; k < metas.length; k++) metas[k].setAttribute("content", oscuro ? "#0b1220" : "#f8fafc");
    }
    if (btn) {
      btn.addEventListener("click", function () {
        var nuevo = actual() === "dark" ? "light" : "dark";
        raiz.setAttribute("data-theme", nuevo);
        try { localStorage.setItem("mqp_tema", nuevo); } catch (e) {}
        pintar();
      });
    }
    /* sin preferencia guardada, sigue al sistema en vivo */
    if (sistema && sistema.addEventListener) sistema.addEventListener("change", function () {
      var guardado = null;
      try { guardado = localStorage.getItem("mqp_tema"); } catch (e) {}
      if (!guardado) pintar();
    });
    pintar();
  });

  /* ---------- modo simulación hiperrealista ----------
     Se engancha al simulador de bancos mediante los eventos mqp:pregunta,
     mqp:respondida y mqp:cerrado; no toca la carga de bancos/ ni el puntaje.
     Estado por pregunta guardado en el propio objeto de la pregunta:
       pregunta.marcada (bandera) y pregunta.tachadas (letras tachadas). */
  safe("simulacion", function () {
    var vista = document.getElementById("simView");
    var opciones = document.getElementById("svOptions");
    var contenido = document.getElementById("svContent");
    if (!vista || !opciones || !contenido) return;

    var el = {
      tarjeta: document.getElementById("svQuiz"),
      flag: document.getElementById("svFlag"),
      recall: document.getElementById("svRecall"),
      pace: document.getElementById("svPace"),
      paceFill: document.getElementById("svPaceFill"),
      paceTime: document.getElementById("svPaceTime"),
      score: document.getElementById("svScore"),
      next: document.getElementById("svNext"),
      prev: document.getElementById("svPrev"),
      algo: document.getElementById("svAlgo"),
      modal: document.getElementById("algoModal"),
      modalBody: document.getElementById("algoBody"),
      modalTitle: document.getElementById("algoTitle"),
      modalSub: document.getElementById("algoSub"),
      modalClose: document.getElementById("algoClose")
    };
    var estado = null;          // detail del último mqp:pregunta
    var preseleccion = null;    // letra elegida con el teclado, pendiente de confirmar

    function botones() { return opciones.querySelectorAll(".opt"); }
    function boton(letra) { return opciones.querySelector('.opt[data-letra="' + letra + '"]'); }
    function enPantalla() { return !vista.hidden && !contenido.hidden && !!estado; }

    /* ===== 1. tachado de distractores ===== */
    var OJO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16"/><path d="M8 6.5C9.2 5.6 10.5 5 12 5c5 0 8.5 7 8.5 7a15 15 0 0 1-2 2.8M6 8.2A15 15 0 0 0 3.5 12S7 19 12 19c1.5 0 2.8-.5 4-1.2"/></svg>';

    function decorarOpciones() {
      var q = estado && estado.pregunta;
      var lista = botones();
      for (var k = 0; k < lista.length; k++) {
        var b = lista[k];
        var letra = b.getAttribute("data-letra");
        var li = b.parentNode;
        if (!li.querySelector(".opt-strike")) {
          var t = document.createElement("button");
          t.type = "button";
          t.className = "opt-strike";
          t.setAttribute("data-letra", letra);
          t.innerHTML = OJO + '<span class="sr-only">Tachar la alternativa ' + letra + "</span>";
          t.title = "Tachar / destachar (clic derecho sobre la alternativa)";
          li.classList.add("opt-row");
          li.appendChild(t);
        }
        pintarTachado(letra, !!(q && q.tachadas && q.tachadas[letra]));
      }
      bloquearTachado(!!(estado && estado.respondida));
    }
    function bloquearTachado(on) {
      var ts = opciones.querySelectorAll(".opt-strike");
      for (var k = 0; k < ts.length; k++) ts[k].disabled = on;
    }
    function pintarTachado(letra, on) {
      var b = boton(letra);
      if (!b) return;
      b.classList.toggle("opt--struck", on);
      var t = b.parentNode.querySelector(".opt-strike");
      if (t) t.setAttribute("aria-pressed", on ? "true" : "false");
    }
    function tachar(letra) {
      if (!estado) return;
      var q = estado.pregunta;
      q.tachadas = q.tachadas || {};
      q.tachadas[letra] = !q.tachadas[letra];
      if (q.tachadas[letra] && preseleccion === letra) preseleccionar(null);
      pintarTachado(letra, q.tachadas[letra]);
    }
    opciones.addEventListener("contextmenu", function (ev) {
      var b = ev.target.closest ? ev.target.closest(".opt") : null;
      if (!b || b.disabled) return;
      ev.preventDefault();
      tachar(b.getAttribute("data-letra"));
    });
    opciones.addEventListener("click", function (ev) {
      var t = ev.target.closest ? ev.target.closest(".opt-strike") : null;
      if (!t) return;
      if (estado && estado.respondida) return;
      tachar(t.getAttribute("data-letra"));
    });

    /* ===== 2. bandera de revisión ===== */
    function pintarBandera() {
      var on = !!(estado && estado.pregunta.marcada);
      if (el.flag) {
        el.flag.setAttribute("aria-pressed", on ? "true" : "false");
        el.flag.querySelector(".flag-btn__label").textContent = on ? "Marcada" : "Marcar";
      }
      if (el.tarjeta) el.tarjeta.classList.toggle("is-flagged", on);
      pintarMarcadas();
    }
    function pintarMarcadas() {
      if (!el.score || !estado) return;
      var n = 0;
      for (var k = 0; k < estado.preguntas.length; k++) if (estado.preguntas[k].marcada) n++;
      var chip = el.score.parentNode.querySelector(".flag-count");
      if (!chip) {
        chip = document.createElement("span");
        chip.className = "flag-count";
        el.score.parentNode.insertBefore(chip, el.score);
      }
      chip.hidden = !n;
      chip.textContent = n + (n === 1 ? " marcada para revisión" : " marcadas para revisión");
    }
    function alternarBandera() {
      if (!estado) return;
      estado.pregunta.marcada = !estado.pregunta.marcada;
      pintarBandera();
      vista.dispatchEvent(new CustomEvent("mqp:marcada"));
    }
    if (el.flag) el.flag.addEventListener("click", alternarBandera);

    /* ===== 3. active recall ===== */
    var CLAVE_RECALL = "mqp_recall";
    function pintarRecall() {
      var on = !!(el.recall && el.recall.checked);
      opciones.classList.toggle("is-recall", on);
      var lista = botones();
      for (var k = 0; k < lista.length; k++) lista[k].classList.remove("is-revealed");
    }
    if (el.recall) {
      try { el.recall.checked = localStorage.getItem(CLAVE_RECALL) === "1"; } catch (e) {}
      el.recall.addEventListener("change", function () {
        try { localStorage.setItem(CLAVE_RECALL, el.recall.checked ? "1" : "0"); } catch (e) {}
        pintarRecall();
      });
      pintarRecall();
    }
    /* En pantallas táctiles no hay hover: el primer toque revela y el segundo responde.
       Se escucha en captura para frenar el clic antes de que llegue al motor. */
    opciones.addEventListener("click", function (ev) {
      if (!opciones.classList.contains("is-recall")) return;
      var b = ev.target.closest ? ev.target.closest(".opt") : null;
      if (!b || b.disabled || b.classList.contains("is-revealed")) return;
      if (window.matchMedia && window.matchMedia("(hover: hover)").matches) return;
      ev.stopPropagation();
      b.classList.add("is-revealed");
    }, true);

    /* ===== 6. barra de ritmo (60 s por pregunta) ===== */
    var IDEAL = 60, AVISO = 40;
    var inicio = 0, reloj = null;
    function dos(n) { return (n < 10 ? "0" : "") + n; }
    function ticRitmo() {
      var s = (Date.now() - inicio) / 1000;
      var p = Math.min(s / IDEAL, 1);
      if (el.paceFill) el.paceFill.style.transform = "scaleX(" + p + ")";
      if (el.pace) {
        el.pace.classList.toggle("is-warn", s >= AVISO && s < IDEAL);
        el.pace.classList.toggle("is-over", s >= IDEAL);
      }
      if (el.paceTime) {
        var t = Math.floor(s);
        el.paceTime.textContent = Math.floor(t / 60) + ":" + dos(t % 60);
        el.paceTime.classList.toggle("is-warn", s >= AVISO && s < IDEAL);
        el.paceTime.classList.toggle("is-over", s >= IDEAL);
      }
    }
    function pararRitmo() { if (reloj) { clearInterval(reloj); reloj = null; } }
    function iniciarRitmo() {
      pararRitmo();
      if (el.pace) el.pace.classList.remove("is-done");
      inicio = Date.now();
      ticRitmo();
      reloj = setInterval(ticRitmo, 250);
    }
    function congelarRitmo() {
      pararRitmo();
      if (el.pace) el.pace.classList.add("is-done");
    }
    document.addEventListener("visibilitychange", function () {
      /* al volver a la pestaña el tiempo transcurrido sigue siendo real; solo refresca */
      if (!document.hidden && reloj) ticRitmo();
    });

    /* ===== 5. atajos de teclado ===== */
    function preseleccionar(letra) {
      preseleccion = letra;
      var lista = botones();
      for (var k = 0; k < lista.length; k++) lista[k].classList.toggle("is-preselected", lista[k].getAttribute("data-letra") === letra);
      if (letra) { var b = boton(letra); if (b) { b.classList.add("is-revealed"); b.focus({ preventScroll: true }); b.scrollIntoView({ block: "nearest" }); } }
    }
    var espacioManejado = false;
    document.addEventListener("keydown", function (ev) {
      if (!enPantalla() || ev.ctrlKey || ev.metaKey || ev.altKey) return;
      if (el.modal && el.modal.open) return;
      var t = ev.target;
      if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) && t !== el.recall) return;
      if (t && t.closest && t.closest(".chat-panel")) return;

      var k = ev.key;
      var respondida = !!estado.respondida;
      var letra = null;
      if (/^[a-eA-E]$/.test(k)) letra = k.toUpperCase();
      else if (/^[1-5]$/.test(k)) letra = "ABCDE".charAt(parseInt(k, 10) - 1);

      if (letra && !respondida) {
        var b = boton(letra);
        if (!b) return;
        ev.preventDefault();
        preseleccionar(letra);
      } else if (k === " " || k === "Spacebar" || k === "Enter") {
        if (k === "Enter" && t && t.tagName === "BUTTON" && t !== boton(preseleccion)) return;
        ev.preventDefault();
        espacioManejado = true;
        if (!respondida && preseleccion) {
          var elegido = boton(preseleccion);
          if (elegido) elegido.click();
        } else if ((respondida || estado.elegida) && el.next && !el.next.disabled) {
          el.next.click();
        }
      } else if (k === "f" || k === "F") {
        ev.preventDefault();
        alternarBandera();
      } else if (k === "ArrowRight" && el.next && !el.next.disabled) {
        ev.preventDefault(); el.next.click();
      } else if (k === "ArrowLeft" && el.prev && !el.prev.disabled) {
        ev.preventDefault(); el.prev.click();
      }
    });
    /* evita que el Espacio "suelte" un segundo clic sobre el botón enfocado */
    document.addEventListener("keyup", function (ev) {
      if (espacioManejado && (ev.key === " " || ev.key === "Spacebar" || ev.key === "Enter")) { ev.preventDefault(); espacioManejado = false; }
    });

    /* ===== 7. modal de algoritmos ===== */
    function abrirAlgoritmo() {
      if (!el.modal || !estado) return;
      var q = estado.pregunta;
      var registro = window.MQP_ALGORITMOS || {};
      var algo = registro[q.id] || registro[q.especialidad] || null;
      el.modalBody.innerHTML = "";
      el.modalTitle.textContent = algo && algo.titulo ? algo.titulo : "Algoritmo diagnóstico";
      el.modalSub.textContent = (q.especialidad || "") + (q.id ? " · " + q.id : "");
      if (visor) { visor.destruir(); visor = null; }
      el.modal.classList.toggle("algo-modal--visor", !!(algo && algo.imagen));
      if (algo && algo.imagen) {
        var ruta = /^(https?:|\/|data:)/.test(algo.imagen) ? algo.imagen : ((window.MQP && window.MQP.base) || "") + algo.imagen;
        visor = crearVisor(ruta, algo.alt || el.modalTitle.textContent, function (nodo) {
          /* archivo ausente o con otro nombre en flujogramas/: avisa en vez de mostrar una imagen rota */
          var aviso = document.createElement("p");
          aviso.className = "algo-modal__note";
          aviso.textContent = "No se pudo cargar el flujograma (" + algo.imagen + "). Revisa que el archivo exista con ese nombre exacto.";
          if (nodo.parentNode) nodo.parentNode.replaceChild(aviso, nodo);
          if (visor) { visor.destruir(); visor = null; }
        });
        el.modalBody.appendChild(visor.nodo);
      }
      if (algo && algo.pasos && algo.pasos.length) {
        el.modalBody.appendChild(flujograma(algo.pasos));
      }
      if (algo && algo.nota) {
        var p = document.createElement("p");
        p.className = "algo-modal__note";
        p.textContent = algo.nota;
        el.modalBody.appendChild(p);
      }
      if (!algo) el.modalBody.appendChild(placeholder());
      if (typeof el.modal.showModal === "function") el.modal.showModal();
      else el.modal.setAttribute("open", "");
    }
    /* pasos: [{ texto, tipo: "inicio" | "decision" | "accion" | "fin" }] */
    function flujograma(pasos) {
      var ol = document.createElement("ol");
      ol.className = "flow-chart";
      for (var k = 0; k < pasos.length; k++) {
        var li = document.createElement("li");
        li.className = "flow-chart__node flow-chart__node--" + (pasos[k].tipo || "accion");
        li.textContent = pasos[k].texto;
        ol.appendChild(li);
      }
      return ol;
    }
    function placeholder() {
      var box = document.createElement("div");
      box.className = "algo-empty";
      box.appendChild(flujograma([
        { texto: "Presentación clínica", tipo: "inicio" },
        { texto: "¿Criterio de gravedad?", tipo: "decision" },
        { texto: "Conducta inicial", tipo: "accion" },
        { texto: "Tratamiento definitivo", tipo: "fin" }
      ]));
      var p = document.createElement("p");
      p.className = "algo-modal__note";
      p.textContent = "Esquema de ejemplo. El flujograma de esta pregunta todavía no está cargado.";
      box.appendChild(p);
      return box;
    }
    function cerrarAlgoritmo() {
      if (!el.modal) return;
      if (typeof el.modal.close === "function") el.modal.close(); else el.modal.removeAttribute("open");
      if (visor) visor.reiniciar(false);
      if (el.algo) el.algo.focus();
    }

    /* ----- visor con zoom y desplazamiento para los flujogramas en imagen -----
       Rueda del ratón, arrastre, pellizco (dos dedos), doble clic y botones + − ↺ ⛶.
       La imagen vive en un "escenario" con transform translate + scale (origen arriba a la
       izquierda); el contenedor tiene overflow: hidden y el desplazamiento se limita para que
       la imagen nunca deje huecos dentro del marco. */
    var visor = null;
    var ZOOM_MIN = 1, ZOOM_MAX = 4, PASO_BOTON = 1.5;
    function crearVisor(src, alt, alFallar) {
      var ICO = {
        mas: '<path d="M12 5v14M5 12h14"/>',
        menos: '<path d="M5 12h14"/>',
        reset: '<path d="M4 12a8 8 0 1 0 2.3-5.6"/><path d="M4 4v4.5h4.5"/>',
        abrir: '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>'
      };
      function boton(clave, etiqueta) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "algo-zoom__btn";
        b.setAttribute("aria-label", etiqueta);
        b.title = etiqueta;
        b.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ICO[clave] + "</svg>";
        return b;
      }
      var caja = document.createElement("div");
      caja.className = "algo-zoom";
      var marco = document.createElement("div");
      marco.className = "algo-zoom__frame";
      var escena = document.createElement("div");
      escena.className = "algo-zoom__stage";
      var img = document.createElement("img");
      img.src = src;
      img.alt = alt;
      img.className = "algo-modal__img";
      img.draggable = false;
      escena.appendChild(img);
      marco.appendChild(escena);

      var barra = document.createElement("div");
      barra.className = "algo-zoom__tools";
      barra.setAttribute("role", "toolbar");
      barra.setAttribute("aria-label", "Zoom del flujograma");
      var bMenos = boton("menos", "Alejar"), bMas = boton("mas", "Acercar");
      var bReset = boton("reset", "Restablecer zoom"), bAbrir = boton("abrir", "Abrir imagen completa en una pestaña nueva");
      var nivel = document.createElement("span");
      nivel.className = "algo-zoom__level";
      nivel.setAttribute("aria-live", "polite");
      barra.appendChild(bMenos); barra.appendChild(nivel); barra.appendChild(bMas); barra.appendChild(bReset); barra.appendChild(bAbrir);
      marco.appendChild(barra);

      var ayuda = document.createElement("p");
      ayuda.className = "algo-zoom__hint";
      ayuda.textContent = "Rueda del ratón o pellizco para ampliar · arrastra para moverte · doble clic para acercar o volver";
      caja.appendChild(marco);
      caja.appendChild(ayuda);

      var z = { s: 1, x: 0, y: 0 };
      var punteros = {}, arrastre = null, pellizco = null, animarHasta = 0;

      function medidas() { return { w: marco.clientWidth, h: marco.clientHeight }; }
      function limitar() {
        var m = medidas();
        z.s = Math.min(ZOOM_MAX, Math.max(ZOOM_MIN, z.s));
        z.x = Math.min(0, Math.max(m.w - m.w * z.s, z.x));
        z.y = Math.min(0, Math.max(m.h - m.h * z.s, z.y));
      }
      function pintar(animado) {
        limitar();
        escena.classList.toggle("is-animating", !!animado && !reduced);
        if (animado) { animarHasta = Date.now() + 200; setTimeout(function () { if (Date.now() >= animarHasta) escena.classList.remove("is-animating"); }, 210); }
        escena.style.transform = "translate(" + z.x.toFixed(2) + "px," + z.y.toFixed(2) + "px) scale(" + z.s.toFixed(4) + ")";
        var ampliado = z.s > 1.001;
        caja.classList.toggle("is-zoomed", ampliado);
        nivel.textContent = Math.round(z.s * 100) + "%";
        bMenos.disabled = !ampliado;
        bReset.disabled = !ampliado && z.x === 0 && z.y === 0;
        bMas.disabled = z.s >= ZOOM_MAX - 0.001;
      }
      /* acerca o aleja manteniendo fijo el punto (cx, cy) del marco */
      function zoomEn(nueva, cx, cy, animado) {
        nueva = Math.min(ZOOM_MAX, Math.max(ZOOM_MIN, nueva));
        var k = nueva / z.s;
        z.x = cx - (cx - z.x) * k;
        z.y = cy - (cy - z.y) * k;
        z.s = nueva;
        pintar(animado);
      }
      function centro() { var m = medidas(); return { x: m.w / 2, y: m.h / 2 }; }
      function local(ev) { var r = marco.getBoundingClientRect(); return { x: ev.clientX - r.left, y: ev.clientY - r.top }; }
      function reiniciar(animado) { z.s = 1; z.x = 0; z.y = 0; punteros = {}; arrastre = pellizco = null; caja.classList.remove("is-dragging"); pintar(animado); }

      bMas.addEventListener("click", function () { var c = centro(); zoomEn(z.s * PASO_BOTON, c.x, c.y, true); });
      bMenos.addEventListener("click", function () { var c = centro(); zoomEn(z.s / PASO_BOTON, c.x, c.y, true); });
      bReset.addEventListener("click", function () { reiniciar(true); });
      bAbrir.addEventListener("click", function () {
        var w = window.open(img.currentSrc || img.src, "_blank", "noopener");
        if (w) w.opener = null;
      });

      marco.addEventListener("wheel", function (ev) {
        var dy = ev.deltaMode === 1 ? ev.deltaY * 16 : ev.deltaMode === 2 ? ev.deltaY * marco.clientHeight : ev.deltaY;
        /* en 100% y alejando, deja que el modal haga scroll normal */
        if (z.s <= ZOOM_MIN && dy > 0) return;
        ev.preventDefault();
        var p = local(ev);
        zoomEn(z.s * Math.exp(-dy * 0.0022), p.x, p.y, false);
      }, { passive: false });

      function distancia(a, b) { return Math.hypot(a.x - b.x, a.y - b.y); }
      function medio(a, b) { return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 }; }
      function iniciarGesto() {
        var ids = Object.keys(punteros);
        if (ids.length >= 2) {
          var a = punteros[ids[0]], b = punteros[ids[1]];
          pellizco = { d: distancia(a, b) || 1, s: z.s, m: medio(a, b), x: z.x, y: z.y };
          arrastre = null;
        } else if (ids.length === 1) {
          var p = punteros[ids[0]];
          pellizco = null;
          arrastre = { px: p.x, py: p.y, x: z.x, y: z.y };
        } else {
          pellizco = arrastre = null;
        }
        caja.classList.toggle("is-dragging", !!arrastre && z.s > 1.001);
      }
      marco.addEventListener("pointerdown", function (ev) {
        if (ev.target.closest && ev.target.closest(".algo-zoom__tools")) return;
        if (ev.pointerType === "mouse" && ev.button !== 0) return;
        punteros[ev.pointerId] = local(ev);
        try { marco.setPointerCapture(ev.pointerId); } catch (e) {}
        iniciarGesto();
      });
      marco.addEventListener("pointermove", function (ev) {
        if (!punteros[ev.pointerId]) return;
        punteros[ev.pointerId] = local(ev);
        var ids = Object.keys(punteros);
        if (pellizco && ids.length >= 2) {
          ev.preventDefault();
          var a = punteros[ids[0]], b = punteros[ids[1]], m = medio(a, b);
          var nueva = Math.min(ZOOM_MAX, Math.max(ZOOM_MIN, pellizco.s * distancia(a, b) / pellizco.d));
          var k = nueva / pellizco.s;
          /* el punto que estaba bajo el centro del pellizco sigue bajo los dedos */
          z.x = m.x - (pellizco.m.x - pellizco.x) * k;
          z.y = m.y - (pellizco.m.y - pellizco.y) * k;
          z.s = nueva;
          pintar(false);
        } else if (arrastre && z.s > 1.001) {
          ev.preventDefault();
          var p = punteros[ev.pointerId];
          z.x = arrastre.x + (p.x - arrastre.px);
          z.y = arrastre.y + (p.y - arrastre.py);
          pintar(false);
        }
      });
      function soltar(ev) {
        if (!punteros[ev.pointerId]) return;
        delete punteros[ev.pointerId];
        iniciarGesto();
      }
      marco.addEventListener("pointerup", soltar);
      marco.addEventListener("pointercancel", soltar);
      marco.addEventListener("dblclick", function (ev) {
        if (ev.target.closest && ev.target.closest(".algo-zoom__tools")) return;
        var p = local(ev);
        if (z.s > 1.001) reiniciar(true); else zoomEn(2.5, p.x, p.y, true);
      });

      function alTeclado(ev) {
        if (!el.modal.open || ev.ctrlKey || ev.metaKey || ev.altKey) return;
        var c = centro();
        if (ev.key === "+" || ev.key === "=") { ev.preventDefault(); zoomEn(z.s * PASO_BOTON, c.x, c.y, true); }
        else if (ev.key === "-" || ev.key === "_") { ev.preventDefault(); zoomEn(z.s / PASO_BOTON, c.x, c.y, true); }
        else if (ev.key === "0") { ev.preventDefault(); reiniciar(true); }
      }
      el.modal.addEventListener("keydown", alTeclado);
      function alRedimensionar() { pintar(false); }
      window.addEventListener("resize", alRedimensionar);

      img.addEventListener("error", function () { alFallar(caja); });
      img.addEventListener("load", function () { reiniciar(false); });
      pintar(false);

      return {
        nodo: caja,
        reiniciar: reiniciar,
        destruir: function () {
          el.modal.removeEventListener("keydown", alTeclado);
          window.removeEventListener("resize", alRedimensionar);
        }
      };
    }
    if (el.algo) el.algo.addEventListener("click", abrirAlgoritmo);
    if (el.modalClose) el.modalClose.addEventListener("click", cerrarAlgoritmo);
    if (el.modal) el.modal.addEventListener("click", function (ev) {
      if (ev.target === el.modal) cerrarAlgoritmo();   // clic fuera del panel
    });
    /* Esc también cierra el <dialog>: el zoom vuelve a 100 % en cualquier caso */
    if (el.modal) el.modal.addEventListener("close", function () { if (visor) visor.reiniciar(false); });

    /* ===== enganche con el motor ===== */
    vista.addEventListener("mqp:pregunta", function (ev) {
      estado = ev.detail;
      preseleccion = null;
      decorarOpciones();
      pintarRecall();
      pintarBandera();
      if (estado.respondida || estado.elegida) congelarRitmo(); else iniciarRitmo();
    });
    /* modo simulacro: elegir no corrige, pero el ritmo de la pregunta se detiene */
    vista.addEventListener("mqp:elegida", function (ev) {
      estado = ev.detail;
      preseleccion = null;
      var lista = botones();
      for (var k = 0; k < lista.length; k++) lista[k].classList.remove("is-preselected");
      congelarRitmo();
    });
    vista.addEventListener("mqp:respondida", function (ev) {
      estado = ev.detail;
      preseleccion = null;
      var lista = botones();
      for (var k = 0; k < lista.length; k++) lista[k].classList.remove("is-preselected");
      bloquearTachado(true);
      congelarRitmo();
    });
    vista.addEventListener("mqp:cerrado", function () {
      estado = null;
      pararRitmo();
      if (el.modal && el.modal.open) cerrarAlgoritmo();
    });
    /* cargando o con error: no hay pregunta en pantalla, el reloj no corre */
    new MutationObserver(function () { if (contenido.hidden) pararRitmo(); })
      .observe(contenido, { attributes: true, attributeFilter: ["hidden"] });
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
      if (elMsg) elMsg.textContent = "Tu cuenta gratuita para " + (examen.value === "RM" ? "el Residentado" : examen.value === "EsSalud" ? "EsSalud" : "el ENAM") + " quedó lista. Ya puedes entrar a la plataforma y empezar a entrenar.";
      /* solo se recuerda el examen elegido, para abrir la plataforma en ese examen */
      if (window.MQP) window.MQP.progreso.preferencia("examen", examen.value === "RM" ? "residentado" : examen.value === "EsSalud" ? "essalud" : "enam");

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
    var ENDPOINT = ((window.MQP && window.MQP.base) || "") + "api.php";   // relativo a la raíz del sitio
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
