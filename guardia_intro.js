/* MedQuizPlus · «Sobrevive a la Guardia»: introducción cinematográfica.
   Escena dibujada en SVG/CSS (no es una foto): si existe app/assets/guardia-hospital.jpg se usa como fondo; si no, queda la escena vectorial.
   No contiene casos clínicos. Con "reducir movimiento" se muestra todo de golpe y sin animaciones. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var CLAVE = "mqp_guardia_intro_v1";
  var FOTO = "assets/guardia-hospital.jpg";

  /* Preferencia "omitir en futuras visitas": M.progreso.preferencia (se sincroniza con la cuenta) + respaldo local por si falla el almacenamiento */
  function omitida() {
    try { if (M.progreso && M.progreso.preferencia("guardiaIntro") === "omitir") return true; } catch (e) {}
    try { return localStorage.getItem(CLAVE) === "omitir"; } catch (e) { return false; }
  }
  function guardarOmitir(si) {
    try { if (M.progreso) M.progreso.preferencia("guardiaIntro", si ? "omitir" : "ver"); } catch (e) {}
    try { if (si) localStorage.setItem(CLAVE, "omitir"); else localStorage.removeItem(CLAVE); } catch (e) {}
  }
  function reducido() { try { return matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) { return false; } }

  var ESCENA =
    '<svg class="gi-svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">' +
    '<defs>' +
      '<linearGradient id="giPared" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#06141a"/><stop offset=".55" stop-color="#0b2229"/><stop offset="1" stop-color="#040b0e"/></linearGradient>' +
      '<linearGradient id="giPiso" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#102a31"/><stop offset="1" stop-color="#03090c"/></linearGradient>' +
      '<radialGradient id="giLuz" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#d9fbf4" stop-opacity=".85"/><stop offset="1" stop-color="#d9fbf4" stop-opacity="0"/></radialGradient>' +
      '<radialGradient id="giFondo" cx=".5" cy=".42" r=".5"><stop offset="0" stop-color="#7fe8d6" stop-opacity=".55"/><stop offset="1" stop-color="#7fe8d6" stop-opacity="0"/></radialGradient>' +
    '</defs>' +
    '<rect width="1600" height="900" fill="url(#giPared)"/>' +
    /* pasillo en perspectiva: punto de fuga en (800, 400) */
    '<polygon points="0,0 1600,0 1050,330 550,330" fill="#07181e"/>' +
    '<polygon points="0,900 1600,900 1050,470 550,470" fill="url(#giPiso)"/>' +
    '<polygon points="0,0 550,330 550,470 0,900" fill="#0a1f26"/>' +
    '<polygon points="1600,0 1050,330 1050,470 1600,900" fill="#091c22"/>' +
    '<rect x="550" y="330" width="500" height="140" fill="#10343b"/>' +
    '<ellipse cx="800" cy="400" rx="330" ry="150" fill="url(#giFondo)" class="gi-puerta"/>' +
    '<rect x="745" y="352" width="110" height="96" rx="4" fill="#cdeee8" opacity=".14"/><line x1="800" y1="352" x2="800" y2="448" stroke="#06141a" stroke-width="3"/>' +
    '<rect x="760" y="318" width="80" height="16" rx="3" fill="#2b0c10"/><rect x="764" y="322" width="72" height="8" rx="2" fill="#d4343f" class="gi-letrero"/>' +
    /* luces del techo */
    '<g class="gi-luces">' +
      '<ellipse cx="800" cy="70" rx="260" ry="40" fill="url(#giLuz)" opacity=".55"/><rect x="620" y="52" width="360" height="22" rx="6" fill="#e8fffb" opacity=".8"/>' +
      '<ellipse cx="800" cy="205" rx="160" ry="26" fill="url(#giLuz)" opacity=".45"/><rect x="705" y="195" width="190" height="14" rx="5" fill="#e8fffb" opacity=".7"/>' +
      '<ellipse cx="800" cy="290" rx="90" ry="14" fill="url(#giLuz)" opacity=".35"/><rect x="750" y="284" width="100" height="8" rx="3" fill="#e8fffb" opacity=".6"/>' +
    '</g>' +
    /* líneas guía del piso y zócalo */
    '<g stroke="#5ad6c4" stroke-opacity=".16" stroke-width="2"><line x1="640" y1="900" x2="780" y2="470"/><line x1="960" y1="900" x2="820" y2="470"/></g>' +
    '<g stroke="#9ff0e2" stroke-opacity=".10" stroke-width="2"><line x1="0" y1="640" x2="550" y2="400"/><line x1="1600" y1="640" x2="1050" y2="400"/></g>' +
    /* camilla en primer plano, a la izquierda */
    '<g class="gi-camilla" opacity=".9"><rect x="150" y="610" width="430" height="26" rx="8" fill="#0a171b"/><rect x="170" y="570" width="380" height="42" rx="14" fill="#13262c"/>' +
      '<rect x="170" y="560" width="120" height="30" rx="14" fill="#1b3840"/><line x1="200" y1="636" x2="200" y2="720" stroke="#0a171b" stroke-width="10"/><line x1="530" y1="636" x2="530" y2="720" stroke="#0a171b" stroke-width="10"/>' +
      '<circle cx="200" cy="728" r="14" fill="#0a171b"/><circle cx="530" cy="728" r="14" fill="#0a171b"/></g>' +
    /* monitor con trazo ECG, a la derecha */
    '<g class="gi-monitor"><rect x="1090" y="420" width="300" height="190" rx="14" fill="#050e11" stroke="#1f4a52" stroke-width="3"/>' +
      '<rect x="1106" y="436" width="268" height="158" rx="8" fill="#03090b"/>' +
      '<polyline class="gi-ecg" fill="none" stroke="#5be6cf" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" points="1112,520 1150,520 1166,520 1180,490 1194,552 1208,520 1250,520 1280,520 1296,520 1310,482 1324,560 1338,520 1368,520"/>' +
      '<text x="1118" y="462" fill="#5be6cf" font-size="15" font-family="monospace" opacity=".8">FC  ––</text><text x="1118" y="580" fill="#8fb8bd" font-size="13" font-family="monospace" opacity=".6">SpO₂  ––</text>' +
      '<line x1="1240" y1="610" x2="1240" y2="760" stroke="#0b1b20" stroke-width="12"/></g>' +
    '<rect width="1600" height="900" fill="#02080a" opacity=".1"/>' +
    '</svg>';

  function mostrar(opciones) {
    var o = opciones || {}, rm = reducido();
    var el = document.createElement("section");
    el.className = "gi" + (rm ? " gi--rm" : ""); el.setAttribute("role", "dialog"); el.setAttribute("aria-modal", "true"); el.setAttribute("aria-label", "Introducción a Sobrevive a la Guardia");
    el.innerHTML =
      '<div class="gi-fondo" aria-hidden="true"><div class="gi-cam">' + ESCENA + '<div class="gi-foto" id="giFoto"><div class="gi-lienzo"><img class="gi-img" alt="" decoding="async"><span class="gi-derrame"></span><span class="gi-neon"></span></div></div></div></div>' +
      '<div class="gi-vineta" aria-hidden="true"></div><div class="gi-grano" aria-hidden="true"></div>' +
      '<p class="gi-marca" id="giMarca">MEDQUIZPRO · SIMULACIÓN CLÍNICA</p>' +
      '<div class="gi-texto" aria-live="polite">' +
        '<div class="gi-msg"><h1 class="gi-t1" id="giT1">La guardia no espera.</h1>' +
        '<p class="gi-t2" id="giT2">Tu paciente ha llegado. Tus decisiones importan.</p>' +
        '<p class="gi-t3" id="giT3">No basta con saber la respuesta. Debes reconocer el peligro, priorizar y actuar.</p></div>' +
        '<div class="gi-fin" id="giFin"><h2 class="gi-t4">¿Estás listo para la guardia?</h2><p class="gi-t5">Cada decisión cuenta. Cada caso te prepara.</p>' +
        '<button type="button" class="gi-ini" id="giIniciar">INICIAR GUARDIA <span aria-hidden="true">→</span></button></div>' +
      '</div>' +
      '<button type="button" class="gi-omitir" id="giOmitir">Omitir introducción</button>' +
      '<p class="gi-aviso">Simulación educativa. No sirve para dirigir la atención de pacientes reales. Puedes omitirla (botón o Esc); volverá a aparecer cuando recargues la página o vuelvas a entrar tras salir de ella. El sonido de fondo es sintético y decorativo.</p>';
    document.body.appendChild(el); document.body.classList.add("gi-abierta");
    var prev = document.activeElement, timers = [], cerrado = false, sonidoIntro = M.introServicio && M.introServicio.anexarSonido ? M.introServicio.anexarSonido(el, "guardia/audio/hospital.mp3", "gi-snd") : null;   // ambiente de hospital

    /* fotografía opcional (se usa solo si el archivo existe) */
    var im = new Image(); im.onload = function () { var f = el.querySelector(".gi-img"); if (f) { f.src = FOTO; el.classList.add("gi--foto"); } }; im.src = FOTO;

    function T(ms, fn) { timers.push(setTimeout(fn, ms)); }
    function clase(c) { el.classList.add(c); }
    function cerrar(tipo) {
      if (cerrado) return; cerrado = true; timers.forEach(clearTimeout); if (sonidoIntro) sonidoIntro.detener();
      document.removeEventListener("keydown", tecla); window.removeEventListener("hashchange", alIrse);
      /* «Omitir» cierra solo esta vez: la introducción vuelve a aparecer cada vez que se entra a «Sobrevive a la Guardia» */
      el.classList.add("gi--salida");
      var fin = function () { el.remove(); document.body.classList.remove("gi-abierta"); if (typeof o.alTerminar === "function" && tipo !== "salir") o.alTerminar(tipo); };
      if (rm || tipo === "salir") fin(); else setTimeout(fin, 520);
    }
    function final() { timers.forEach(clearTimeout); ["gi--e1", "gi--e2", "gi--e3", "gi--e4"].forEach(clase); var b = el.querySelector("#giIniciar"); if (b && !cerrado) b.focus(); }
    function alIrse() { if (!/^#\/guardia/.test(location.hash)) cerrar("salir"); }    // si navega a otra sección, la introducción se desmonta sin dejar nada colgado
    window.addEventListener("hashchange", alIrse);
    function tecla(ev) {
      if (ev.key === "Tab") {                                  // el foco no se escapa a la plataforma que queda detrás
        var f = [].filter.call(el.querySelectorAll("button"), function (b) { return b.offsetParent !== null && getComputedStyle(b).visibility !== "hidden"; });
        if (!f.length) return; var i = f.indexOf(document.activeElement);
        if (ev.shiftKey && i <= 0) { ev.preventDefault(); f[f.length - 1].focus(); } else if (!ev.shiftKey && i === f.length - 1) { ev.preventDefault(); f[0].focus(); } else if (i < 0) { ev.preventDefault(); f[0].focus(); }
        return;
      }
      if (ev.key === "Escape") { ev.preventDefault(); cerrar("omitir"); }
      else if ((ev.key === " " || ev.key === "Enter") && !(ev.target.closest && ev.target.closest("button")) && !el.classList.contains("gi--e4")) { ev.preventDefault(); final(); }
    }
    document.addEventListener("keydown", tecla);
    el.querySelector("#giIniciar").addEventListener("click", function () { cerrar("iniciar"); });
    el.querySelector("#giOmitir").addEventListener("click", function () { cerrar("omitir"); });
    el.addEventListener("click", function (ev) { if (!ev.target.closest("button") && !el.classList.contains("gi--e4")) final(); });

    el.style.outline = "none";
    if (rm) { final(); }
    else {                 /* una sola línea de tiempo continua: cada escena se suma a la anterior, que se atenúa */
      T(150, function () { clase("gi--e1"); });      // hospital + marca
      T(1900, function () { clase("gi--e2"); });     // «La guardia no espera.» y subtítulo
      T(6200, function () { clase("gi--e3"); });     // el desafío
      T(10800, function () { clase("gi--e4"); var b = el.querySelector("#giIniciar"); if (b) b.focus({ preventScroll: true }); });
    }
    el.tabIndex = -1; el.focus({ preventScroll: true }); T(80, function () { if (!el.contains(document.activeElement)) el.focus({ preventScroll: true }); });   // el enrutador de la app también mueve el foco al montar: se lo devolvemos          // el foco empieza en la propia introducción: Espacio/Intro adelantan, no omiten por accidente
    return { cerrar: cerrar, elemento: el, anterior: prev };
  }

  M.guardiaIntro = { mostrar: mostrar, omitida: omitida, reactivar: function () { guardarOmitir(false); } };
})();
