/* MedQuizPlus — capa de animación (aditiva, sin dependencias). */
(function () {
  "use strict";
  function safe(n, f) { try { f(); } catch (e) { if (window.console) console.warn("[fx] " + n, e); } }
  var reduced = false, fine = false;
  try { reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
  if (reduced) return;

  /* barra de lectura + header cristal */
  safe("scroll", function () {
    var bar = document.createElement("div"); bar.className = "fx-progress"; bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);
    var header = document.getElementById("siteHeader"), tick = false;
    function upd() {
      var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
      bar.style.transform = "scaleX(" + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ")";
      if (header) header.classList.toggle("is-scrolled", window.scrollY > 12);
      tick = false;
    }
    window.addEventListener("scroll", function () { if (!tick) { tick = true; requestAnimationFrame(upd); } }, { passive: true });
    upd();
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

  /* hero: halos + línea de ECG */
  safe("hero", function () {
    var hero = document.querySelector(".hero"); if (!hero) return;
    var au = document.createElement("div"); au.className = "hero__aurora"; au.setAttribute("aria-hidden", "true");
    au.innerHTML = "<i></i><i></i>"; hero.insertBefore(au, hero.firstChild);
    var d = "M0 60"; for (var x = 0; x < 1600; x += 400) d += " H" + (x + 140) + " l14 0 l10 -22 l12 54 l12 -80 l14 48 l14 0 l14 -12 l14 12 H" + (x + 400);
    hero.insertAdjacentHTML("afterbegin", '<svg class="hero__ecg" viewBox="0 0 1600 120" preserveAspectRatio="none" aria-hidden="true"><path class="base" d="' + d + '"/><path d="' + d + '"/></svg>');
  });

  /* quiz del hero: anima la entrada de cada pregunta nueva */
  safe("quiz", function () {
    var demo = document.getElementById("quiz"), stem = document.getElementById("qStem"); if (!demo || !stem || !window.MutationObserver) return;
    new MutationObserver(function () {
      demo.classList.remove("fx-swap"); void demo.offsetWidth; demo.classList.add("fx-swap");
    }).observe(stem, { childList: true, characterData: true, subtree: true });
  });

  /* escalonado de los .reveal hermanos */
  safe("stagger", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".exams, .features, .steps, .sims, .plans, .modes, .metrics__grid"), function (g) {
      Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty("--fx-d", Math.min(i, 6) * 80 + "ms"); });
    });
  });

  /* tarjetas: inclinación leve + brillo que sigue al cursor */
  safe("tilt", function () {
    if (!fine) return;
    Array.prototype.forEach.call(document.querySelectorAll(".exam, .feature, .sim-tile, .plan:not(.plan--soon), .step"), function (el) {
      var raf = 0;
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
        if (raf) cancelAnimationFrame(raf);
        raf = requestAnimationFrame(function () {
          el.style.setProperty("--mx", x + "px"); el.style.setProperty("--my", y + "px");
          el.style.transform = "perspective(1000px) rotateX(" + ((y / r.height - .5) * -3.5).toFixed(2) + "deg) rotateY(" + ((x / r.width - .5) * 3.5).toFixed(2) + "deg) translateY(-3px)";
        });
      });
      el.addEventListener("pointerleave", function () { if (raf) cancelAnimationFrame(raf); el.style.transform = ""; });
    });
  });

  /* cambio de tema con fundido */
  safe("theme", function () {
    var t = document.getElementById("themeToggle"); if (!t) return;
    t.addEventListener("click", function () {
      var r = document.documentElement; r.classList.add("fx-theming");
      setTimeout(function () { r.classList.remove("fx-theming"); }, 600);
    });
  });
})();
