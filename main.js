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
