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

  /* ---------- filtro de bancos ---------- */
  safe("filtro", function () {
    var chips = document.querySelectorAll(".chip[data-filter]");
    var tarjetas = document.querySelectorAll(".bank[data-exam]");
    var vacio = document.getElementById("banksEmpty");
    if (!chips.length || !tarjetas.length) return;

    function aplicar(filtro) {
      var visibles = 0;
      for (var k = 0; k < tarjetas.length; k++) {
        var ok = filtro === "todos" || tarjetas[k].getAttribute("data-exam") === filtro;
        tarjetas[k].hidden = !ok;
        if (ok) visibles++;
      }
      if (vacio) vacio.hidden = visibles > 0;
    }

    for (var j = 0; j < chips.length; j++) {
      (function (chip) {
        chip.addEventListener("click", function () {
          for (var m = 0; m < chips.length; m++) chips[m].setAttribute("aria-pressed", "false");
          chip.setAttribute("aria-pressed", "true");
          aplicar(chip.getAttribute("data-filter"));
        });
      })(chips[j]);
    }

    var activo = document.querySelector('.chip[aria-pressed="true"]');
    aplicar(activo ? activo.getAttribute("data-filter") : "todos");
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
})();
