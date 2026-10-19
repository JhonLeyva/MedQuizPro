/* MedQuizPlus · Atlas de anatomía 3D: «Human Atlas» de Ashe Magalhaes (código MIT) con la anatomía de BodyParts3D 4.0
   (CC BY 4.0), alojado en esta misma plataforma (carpeta atlas3d/): sin cuentas, sin pagos y para todos los estudiantes.
   Dos usos: la página «Atlas de anatomía» (#/anatomia) y el botón «Ver en el atlas» de las preguntas de anatomía, que abre el
   mismo atlas en una ventana sobre la pregunta (así no se pierde el avance del simulador).
   Si el tema de la pregunta coincide con una estructura de la lista ES_EN, el atlas la abre ya seleccionada (?q=nombre en inglés). */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var CFG = {
    base: "../atlas3d/",   // carpeta del atlas, relativa a app/index.html
    nombre: "Human Atlas",
    externo: "https://browser.anatomylearning.com/"   // atlas externo (versión gratuita limitada), opcional
  };
  /* Tema de la pregunta (español) → nombre de la estructura en el atlas (inglés, de BodyParts3D). Solo van nombres que existen en el atlas. */
  var ES_EN = [
    [/coraz[oó]n|cardi|coronari/i, "heart"], [/h[ií]gado|hep[aá]tic/i, "liver"], [/ri[nñ][oó]n|renal|nefr/i, "kidney"],
    [/pulm[oó]n|pulmonar|bronquio/i, "lung"], [/est[oó]mago|g[aá]strico/i, "stomach"], [/p[aá]ncreas|pancre[aá]tic/i, "pancreas"],
    [/bazo|espl[eé]n/i, "spleen"], [/vejiga/i, "urinary bladder"], [/tr[aá]quea/i, "trachea"], [/cerebelo/i, "cerebellum"],
    [/cerebr|enc[eé]falo|cerebro/i, "brain"], [/f[eé]mur|femoral/i, "femur"], [/h[uú]mero/i, "humerus"], [/es[oó]fag/i, "esophagus"],
    [/intestino delgado/i, "small intestine"], [/colon|intestino grueso/i, "large intestine"], [/duodeno/i, "duodenum"], [/yeyuno/i, "jejunum"],
    [/[ií]leon|ileal/i, "ileum"], [/ciego/i, "cecum"], [/\brecto\b|rectal/i, "rectum"], [/ap[eé]ndice|apendic/i, "appendix"],
    [/ves[ií]cula|biliar|colecist/i, "gallbladder"], [/v[ií]a biliar|col[eé]doco/i, "bile duct"], [/pr[oó]stata|prost[aá]tic/i, "prostate"],
    [/test[ií]cul/i, "testis"], [/aorta|a[oó]rtic/i, "aorta"], [/vena cava/i, "inferior vena cava"], [/vena porta|sistema porta/i, "portal vein"],
    [/car[oó]tida/i, "common carotid artery"], [/poplítea|popl[ií]tea/i, "popliteal artery"], [/braquial/i, "brachial artery"],
    [/columna|raqu[ií]d|vertebral/i, "vertebral column"], [/lumbar/i, "lumbar vertebra"], [/cervical/i, "cervical vertebra"], [/dorsal|tor[aá]cica/i, "thoracic vertebra"],
    [/disco intervertebral/i, "intervertebral disk"], [/sacro/i, "sacrum"], [/m[eé]dula/i, "spinal cord"], [/cr[aá]neo/i, "skull"],
    [/mand[ií]bula/i, "mandible"], [/maxilar/i, "maxilla"], [/temporal/i, "temporal bone"], [/esfenoid/i, "sphenoid bone"], [/occipital/i, "occipital bone"],
    [/frontal/i, "frontal bone"], [/parietal/i, "parietal bone"], [/esc[aá]pula|escapular/i, "scapula"], [/clav[ií]cula/i, "clavicle"],
    [/esternón|esternon/i, "sternum"], [/tibia/i, "tibia"], [/peron[eé]|f[ií]bula/i, "fibula"], [/r[oó]tula|patela/i, "patella"],
    [/cadera|coxal|ilíaco|iliaco/i, "hip bone"], [/pelvis|p[eé]lvic/i, "pelvis"], [/radio\b/i, "radius"], [/cubit|ulna/i, "ulna"],
    [/escafoid/i, "scaphoid"], [/astr[aá]galo|talo/i, "talus"], [/calc[aá]neo/i, "calcaneus"], [/diafragma/i, "diaphragm"],
    [/\bojo\b|ocular|globo ocular/i, "eyeball"], [/lengua/i, "tongue"], [/hip[oó]fisis|pituitaria/i, "pituitary gland"], [/suprarrenal|adrenal/i, "adrenal gland"],
    [/t[aá]lamo/i, "thalamus"], [/hipot[aá]lamo/i, "hypothalamus"], [/supraespinoso|manguito/i, "supraspinatus"], [/infraespinoso/i, "infraspinatus"],
    [/subescapular/i, "subscapularis"], [/gl[uú]teo|gl[uú]tea/i, "gluteus maximus"], [/psoas/i, "psoas major"], [/s[oó]leo/i, "soleus"],
    [/aquiles/i, "calcaneal tendon"], [/b[ií]ceps/i, "biceps brachii"], [/tr[ií]ceps/i, "triceps brachii"], [/deltoid/i, "deltoid"],
    [/trapecio/i, "trapezius"], [/pectoral/i, "pectoralis major"], [/gemelo|gastrocnemio/i, "gastrocnemius"], [/cu[aá]driceps/i, "quadriceps femoris"],
    [/v[aá]lvula mitral|mitral/i, "mitral valve"], [/v[aá]lvula a[oó]rtica/i, "aortic valve"], [/ventr[ií]culo izquierdo/i, "left ventricle"], [/aur[ií]cula derecha/i, "right atrium"]
  ];
  var panel = null, previo = null;

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function disponible() { return true; }
  /* ¿La pregunta es de anatomía? Se mira la categoría, el tema y la especialidad. */
  function esAnatomia(q) {
    if (!q) return false;
    return /anatom/i.test([q.categoria, q.tema, q.especialidad].join(" "));
  }
  function estructuraPara(tema) {
    var t = String(tema || "");
    for (var i = 0; i < ES_EN.length; i++) if (ES_EN[i][0].test(t)) return ES_EN[i][1];
    return "";
  }
  function credito() {
    return '<p class="an-credito">Atlas 3D <b>Human Atlas</b> de Ashe Magalhaes (código MIT) · anatomía de adulto varón de ' +
      '<a href="https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html" target="_blank" rel="noopener noreferrer">BodyParts3D 4.0</a> © The Database Center for Life Science, ' +
      '<a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a>. ' +
      'Los nombres de las estructuras están en inglés. Material educativo; no sustituye el diagnóstico médico.' +
      (CFG.externo ? ' · <a href="' + esc(CFG.externo) + '" target="_blank" rel="noopener noreferrer">Otro atlas (Anatomy Learning)</a>' : "") + '</p>';
  }
  function src(estructura) { return CFG.base + (estructura ? "?q=" + encodeURIComponent(estructura) : ""); }
  function marco(clase, estructura) {
    return '<iframe class="an-marco ' + (clase || "") + '" src="' + esc(src(estructura)) + '" title="Atlas 3D de anatomía (' + esc(CFG.nombre) + ')" loading="lazy" ' +
      'allow="fullscreen" allowfullscreen></iframe>' + credito();
  }

  /* Página aparte dentro del simulador: #/anatomia */
  function pagina(par) {
    var est = estructuraPara(par && par.tema);
    var pista = par && par.tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(par.tema) + '</b>' + (est ? " (en inglés: " + esc(est) + ")" : "") + '</p>' : "";
    return '<header class="page-head"><p class="kicker">Anatomía</p><h1 class="page-head__title">Atlas de anatomía en 3D</h1>' +
      '<p class="page-head__lead">Explora más de 2 200 estructuras: arrastra para rotar, usa la rueda o pellizca para acercar, toca una estructura para ver su nombre, busca con «Find a structure» y separa las piezas con «Explode anatomy».</p></header>' + pista +
      '<div class="an-pagina">' + marco("an-marco--pagina", est) + '</div>';
  }

  function cerrar() { if (!panel) return; if (panel.close) panel.close(); panel.remove(); panel = null; if (previo && previo.focus) previo.focus(); }

  /* Ventana sobre la pregunta: el atlas aparece grande y, al cerrarla, sigues donde estabas. */
  function abrir(q, disparador) {
    if (!disponible()) return;
    previo = disparador || document.activeElement; cerrar(); previo = disparador || previo;
    var tema = q && (q.tema || q.categoria) ? String(q.tema || q.categoria) : "";
    panel = document.createElement("dialog"); panel.className = "fc-dlg an-dlg"; panel.setAttribute("aria-labelledby", "anT");
    panel.innerHTML = '<div class="fc-form an-form"><header class="fc-head"><h2 id="anT">Atlas de anatomía</h2>' +
      '<a class="btn btn--ghost btn--sm" href="#/anatomia' + (tema ? "?tema=" + encodeURIComponent(tema) : "") + '" data-x>Abrir en pantalla completa</a>' +
      '<button type="button" class="fc-x" aria-label="Cerrar" data-x>✕</button></header>' +
      (tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(tema) + '</b></p>' : "") + marco("an-marco--ventana", estructuraPara(tema)) + '</div>';
    document.body.appendChild(panel);
    panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) cerrar(); });
    panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
    if (panel.showModal) panel.showModal(); else panel.setAttribute("open", "");
    var x = panel.querySelector(".fc-x"); if (x && x.focus) x.focus();
  }

  function mostrarMenu() { var n = document.getElementById("navAna"); if (n) n.hidden = !disponible(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mostrarMenu); else mostrarMenu();

  M.anatomia = { disponible: disponible, esAnatomia: esAnatomia, abrir: abrir, cerrar: cerrar, pagina: pagina, config: CFG };
})();
