/* MedQuizPlus — capa de movimiento (aditiva, sin dependencias, sin listeners de scroll). */
(function () {
  "use strict";
  function safe(n, f) { try { f(); } catch (e) { if (window.console) console.warn("[fx] " + n, e); } }
  var reduced = false, fine = false;
  try { reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}

  /* barra de lectura (CSS) y centinela para el header */
  safe("chrome", function () {
    var bar = document.createElement("div"); bar.className = "fx-progress"; bar.setAttribute("aria-hidden", "true"); document.body.appendChild(bar);
    var header = document.getElementById("siteHeader");
    if (!header || !("IntersectionObserver" in window)) return;
    var s = document.createElement("div"); s.className = "fx-sentinel"; s.setAttribute("aria-hidden", "true"); document.body.insertBefore(s, document.body.firstChild);
    new IntersectionObserver(function (e) { header.classList.toggle("is-scrolled", !e[0].isIntersecting); }).observe(s);
  });

  /* hero: halos + ECG (decorativos) */
  safe("hero", function () {
    var hero = document.querySelector(".hero"); if (!hero) return;
    var d = "M0 55 H120"; for (var x = 0; x < 1600; x += 400) d += " H" + (x + 140) + " l14 0 l10 -20 l12 52 l12 -76 l14 44 l14 0 l14 -10 l14 10 H" + (x + 400);
    hero.insertAdjacentHTML("afterbegin",
      '<div class="hero__glow" aria-hidden="true"></div>' +
      '<svg class="hero__ecg" viewBox="0 0 1600 110" preserveAspectRatio="none" aria-hidden="true"><path class="base" d="' + d + '"/><path class="pulse" d="' + d + '"/></svg>');
  });

  /* título del hero: palabras que suben */
  safe("title", function () {
    var t = document.getElementById("heroTitle"); if (!t) return;
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          var frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function (p) {
            if (!p) return;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(" ")); return; }
            var w = document.createElement("span"), s = document.createElement("span");
            w.className = "fx-word"; s.textContent = p; s.style.setProperty("--i", i++); w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, c);
        } else if (c.nodeType === 1) walk(c);
      });
    })(t);
  });

  /* quiz del hero: entrada breve de cada pregunta nueva */
  safe("quiz", function () {
    var demo = document.getElementById("quiz"), stem = document.getElementById("qStem"); if (!demo || !stem || !window.MutationObserver) return;
    new MutationObserver(function () { demo.classList.remove("fx-swap"); void demo.offsetWidth; demo.classList.add("fx-swap"); })
      .observe(stem, { childList: true, characterData: true, subtree: true });
  });

  /* escalonado corto entre hermanos .reveal */
  safe("stagger", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".exams, .features, .steps, .sims, .plans, .modes, .metrics__grid"), function (g) {
      Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty("--fx-d", Math.min(i, 5) * 60 + "ms"); });
    });
  });

  /* brillo que sigue al cursor (solo mouse, sin movimiento si hay reduced-motion) */
  safe("glow", function () {
    if (!fine || reduced) return;
    Array.prototype.forEach.call(document.querySelectorAll(".exam, .feature, .sim-tile, .plan"), function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty("--mx", (e.clientX - r.left) + "px"); el.style.setProperty("--my", (e.clientY - r.top) + "px");
      }, { passive: true });
    });
  });
})();
