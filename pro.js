/* MedQuizPlus — capa de movimiento y escenografía del hero (aditiva, sin dependencias, sin listeners de scroll). */
(function () {
  "use strict";
  function safe(n, f) { try { f(); } catch (e) { if (window.console) console.warn("[pro] " + n, e); } }
  var reduced = false, fine = false;
  try { reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  try { fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}

  safe("chrome", function () {
    var bar = document.createElement("div"); bar.className = "fx-progress"; bar.setAttribute("aria-hidden", "true"); document.body.appendChild(bar);
    var header = document.getElementById("siteHeader");
    if (!header || !("IntersectionObserver" in window)) return;
    var s = document.createElement("div"); s.className = "fx-sentinel"; s.setAttribute("aria-hidden", "true"); document.body.insertBefore(s, document.body.firstChild);
    new IntersectionObserver(function (e) { header.classList.toggle("is-scrolled", !e[0].isIntersecting); }).observe(s);
  });

  safe("hero", function () {
    var hero = document.querySelector(".hero"); if (!hero) return;
    var d = "M0 55 H120"; for (var x = 0; x < 1600; x += 400) d += " H" + (x + 140) + " l14 0 l10 -20 l12 52 l12 -76 l14 44 l14 0 l14 -10 l14 10 H" + (x + 400);
    hero.insertAdjacentHTML("afterbegin",
      '<div class="hero__glow" aria-hidden="true"></div>' +
      '<svg class="hero__ecg" viewBox="0 0 1600 110" preserveAspectRatio="none" aria-hidden="true"><path class="base" d="' + d + '"/><path class="pulse" d="' + d + '"/></svg>');
    var demo = hero.querySelector(".hero-demo");
    if (demo) {
      demo.insertAdjacentHTML("afterbegin", '<div class="orbit" aria-hidden="true"><i></i><i></i><i></i></div>');
      /* leve paralaje de los anillos con el mouse (solo transform, vía rAF) */
      var orbit = demo.querySelector(".orbit");
      if (fine && !reduced && orbit) {
        var tx = 0, ty = 0, cx = 0, cy = 0, raf = 0;
        function step() { cx += (tx - cx) * .08; cy += (ty - cy) * .08; orbit.style.transform = "translate3d(" + cx.toFixed(1) + "px," + cy.toFixed(1) + "px,0)"; raf = (Math.abs(tx - cx) + Math.abs(ty - cy) > .1) ? requestAnimationFrame(step) : 0; }
        hero.addEventListener("pointermove", function (e) {
          if (orbit.classList.contains("has-3d")) return;
          var r = hero.getBoundingClientRect();
          tx = ((e.clientX - r.left) / r.width - .5) * -36; ty = ((e.clientY - r.top) / r.height - .5) * -24;
          if (!raf) raf = requestAnimationFrame(step);
        }, { passive: true });
      }
    }
  });

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


  /* títulos de sección: palabras que suben al entrar (el .reveal existente dispara .is-in) */
  safe("headings", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".sec-head h2, .signup h2, .final-cta h2"), function (h) {
      if (!h.closest(".reveal")) return;
      var i = 0;
      (function walk(node) {
        Array.prototype.slice.call(node.childNodes).forEach(function (c) {
          if (c.nodeType === 3) {
            var frag = document.createDocumentFragment();
            c.textContent.split(/(\s+)/).forEach(function (p) {
              if (!p) return;
              if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(" ")); return; }
              var w = document.createElement("span"), s = document.createElement("span");
              w.className = "wd"; s.textContent = p; s.style.setProperty("--i", i++); w.appendChild(s); frag.appendChild(w);
            });
            node.replaceChild(frag, c);
          } else if (c.nodeType === 1) walk(c);
        });
      })(h);
    });
  });

  /* navegación lateral por secciones (la página es larga) */
  safe("dots", function () {
    if (!("IntersectionObserver" in window)) return;
    var map = [["top", "Inicio"], ["examenes", "Exámenes"], ["bancos", "Bancos"], ["simulacros", "Simuladores"], ["como-funciona", "Cómo funciona"],
      ["ventajas", "Ventajas"], ["plataforma", "Plataforma"], ["precios", "Planes"], ["registro", "Registro"], ["faq", "Preguntas"]];
    var ul = document.createElement("ul"); ul.className = "fx-dots"; ul.setAttribute("aria-label", "Secciones de la página");
    var links = {}, els = [];
    map.forEach(function (m) {
      var el = document.getElementById(m[0]); if (!el) return;
      var li = document.createElement("li"), a = document.createElement("a");
      a.href = "#" + m[0]; a.setAttribute("aria-label", m[1]); a.innerHTML = "<span>" + m[1] + "</span>";
      li.appendChild(a); ul.appendChild(li); links[m[0]] = a; els.push(el);
    });
    document.body.appendChild(ul);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        Object.keys(links).forEach(function (k) { links[k].classList.toggle("is-active", k === e.target.id); });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    els.forEach(function (el) { io.observe(el); });
  });


  /* cinta de palabras clave (todo el texto sale de la propia página) */
  safe("marquee", function () {
    var hero = document.querySelector(".hero"); if (!hero) return;
    var words = ["ENAM", "Residentado Médico", "EsSalud", "Preguntas comentadas", "Simuladores cronometrados", "Flujogramas clínicos", "Active Recall", "Tutor clínico de IA", "Progreso por especialidad"];
    var row = "<span>" + words.join("</span><span>") + "</span>";
    var m = document.createElement("div"); m.className = "fx-marquee"; m.setAttribute("aria-hidden", "true");
    m.innerHTML = '<div class="fx-marquee__track">' + row + row + "</div>";
    hero.parentNode.insertBefore(m, hero.nextSibling);
  });

  /* foco de luz que sigue al mouse en el hero */
  safe("spot", function () {
    var hero = document.querySelector(".hero"); if (!hero || !fine || reduced) return;
    var spot = document.createElement("div"); spot.className = "hero__spot"; spot.setAttribute("aria-hidden", "true"); hero.appendChild(spot);
    var x = 0, y = 0, cx = 0, cy = 0, raf = 0;
    function step() { cx += (x - cx) * .12; cy += (y - cy) * .12; spot.style.transform = "translate3d(" + cx.toFixed(1) + "px," + cy.toFixed(1) + "px,0)"; raf = (Math.abs(x - cx) + Math.abs(y - cy) > .5) ? requestAnimationFrame(step) : 0; }
    hero.addEventListener("pointermove", function (e) { var r = hero.getBoundingClientRect(); x = e.clientX - r.left; y = e.clientY - r.top; hero.classList.add("is-hover"); if (!raf) raf = requestAnimationFrame(step); }, { passive: true });
    hero.addEventListener("pointerleave", function () { hero.classList.remove("is-hover"); });
  });

  /* íconos: se dibujan al entrar (normaliza la longitud del trazo) */
  safe("icons", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".feature__icon svg, .sim-tile__icon svg"), function (svg) {
      Array.prototype.forEach.call(svg.querySelectorAll("path, circle, rect, line"), function (el) { el.setAttribute("pathLength", "1"); });
    });
  });

  /* onda al pulsar botones */
  safe("ripple", function () {
    document.addEventListener("pointerdown", function (e) {
      var b = e.target && e.target.closest && e.target.closest(".btn--primary, .btn--ghost"); if (!b || reduced) return;
      var r = b.getBoundingClientRect(), d = Math.max(r.width, r.height) * 2, el = document.createElement("span");
      el.className = "fx-ripple"; el.style.width = el.style.height = d + "px"; el.style.left = (e.clientX - r.left - d / 2) + "px"; el.style.top = (e.clientY - r.top - d / 2) + "px";
      b.appendChild(el); setTimeout(function () { el.remove(); }, 650);
    }, { passive: true });
  });

  /* acierto en el quiz del hero: destello + pulso del anillo */
  safe("burst", function () {
    var fb = document.getElementById("qFeedback"), verdict = document.getElementById("qVerdict"), ring = document.getElementById("qRing");
    if (!fb || !window.MutationObserver || reduced) return;
    new MutationObserver(function () {
      if (fb.hidden || !/correct/i.test(verdict ? verdict.textContent : "") || /incorrect/i.test(verdict ? verdict.textContent : "")) return;
      if (ring) { ring.classList.remove("fx-pop"); void ring.offsetWidth; ring.classList.add("fx-pop"); }
      window.dispatchEvent(new CustomEvent("fx:correct"));
      if (!fb.animate) return;
      for (var i = 0; i < 14; i++) {
        var p = document.createElement("i"); p.className = "fx-burst"; p.style.left = "22px"; p.style.top = "12px"; if (i % 3 === 0) p.style.background = "#fff";
        fb.appendChild(p);
        var a = Math.random() * Math.PI * 2, d = 38 + Math.random() * 56;
        p.animate([{ transform: "translate(0,0) scale(1)", opacity: 1 }, { transform: "translate(" + (Math.cos(a) * d).toFixed(0) + "px," + (Math.sin(a) * d).toFixed(0) + "px) scale(.2)", opacity: 0 }],
          { duration: 650 + Math.random() * 250, easing: "cubic-bezier(.23,1,.32,1)" }).onfinish = (function (n) { return function () { n.remove(); }; })(p);
      }
    }).observe(fb, { attributes: true, attributeFilter: ["hidden"] });
  });

  /* icono de tema: giro */
  safe("themespin", function () {
    var t = document.getElementById("themeToggle"); if (!t || reduced) return;
    t.addEventListener("click", function () { t.classList.remove("fx-spin"); void t.offsetWidth; t.classList.add("fx-spin"); });
  });

  safe("quiz", function () {
    var demo = document.getElementById("quiz"), stem = document.getElementById("qStem"); if (!demo || !stem || !window.MutationObserver) return;
    new MutationObserver(function () { demo.classList.remove("fx-swap"); void demo.offsetWidth; demo.classList.add("fx-swap"); })
      .observe(stem, { childList: true, characterData: true, subtree: true });
  });

  safe("stagger", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".exams, .features, .steps, .sims, .plans, .modes, .metrics__grid"), function (g) {
      Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty("--fx-d", Math.min(i, 5) * 70 + "ms"); });
    });
  });

  safe("glow", function () {
    if (!fine || reduced) return;
    document.addEventListener("pointermove", function (e) {
      var el = e.target && e.target.closest && e.target.closest(".exam, .feature, .sim-tile, .plan, .spec"); if (!el) return;
      var r = el.getBoundingClientRect();
      el.style.setProperty("--mx", (e.clientX - r.left) + "px"); el.style.setProperty("--my", (e.clientY - r.top) + "px");
    }, { passive: true });
  });
})();
