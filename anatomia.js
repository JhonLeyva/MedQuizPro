/* MedQuizPlus · Atlas de anatomía 3D (visor abierto del Departamento de Anatomía y Embriología del LUMC, Leiden),
   alojado en esta misma plataforma (carpeta visor3d/): sin cuentas, sin pagos y para todos los estudiantes.
   Dos usos: la página «Atlas de anatomía» (#/anatomia) y el botón «Ver en el atlas» de las preguntas de anatomía, que abre el
   mismo atlas en una ventana sobre la pregunta (así no se pierde el avance del simulador).
   Para agregar un modelo: copiar su .glb a visor3d/3dmodels/<id>/<id>.glb y sumarlo a MODELOS. */
(function () {
  "use strict";
  var M = window.MQP || (window.MQP = {});
  var CFG = {
    base: "../visor3d/",   // carpeta del visor, relativa a app/index.html
    nombre: "Open 3D Model · LUMC",
    externo: "https://browser.anatomylearning.com/"   // atlas externo (versión gratuita limitada), opcional
  };
  /* id = carpeta en visor3d/3dmodels; sub = archivo de estructuras iniciales (opcional); g = grupo del selector;
     clave = palabras que lo relacionan con el tema de una pregunta (se usa la primera coincidencia, de arriba abajo) */
  var MODELOS = [
    { id: "overview-skeleton", g: "Esqueleto y cráneo", nombre: "Esqueleto completo", clave: /esquelet|oste[oó]|articulaciones|tor[aá]x [oó]seo|costill|ester[nó]/i },
    { id: "overview-colored-skull", g: "Esqueleto y cráneo", nombre: "Cráneo", clave: /cr[aá]ne|skull|facial|mand[ií]b|maxil|neurocr/i },
    { id: "colored-skull-base", g: "Esqueleto y cráneo", nombre: "Base del cráneo (agujeros y fosas)", clave: /base del cr[aá]neo|agujero|forame|silla turca|esfenoid|temporal/i },
    { id: "exploded-skull", g: "Esqueleto y cráneo", nombre: "Cráneo desarmado (vista explosionada)", clave: /sutura|huesos del cr[aá]neo/i },
    { id: "vertebrae", g: "Columna y tronco", nombre: "Vértebras típicas", clave: /v[eé]rtebr|columna|raqu|lumbar|cervical|dorsal|sacro|cox[ií]/i },
    { id: "spinal-cord", g: "Columna y tronco", nombre: "Médula espinal y estructuras vecinas", clave: /m[eé]dula|espinal|raqu[ií]d|ra[ií]z|cauda|meninge/i },
    { id: "muscles-thorax-abdomen", g: "Columna y tronco", nombre: "Músculos del tórax, abdomen y espalda", clave: /m[uú]sculo|abdomen|pared|diafragma|recto abdominal|oblicu|trapecio|dorsal ancho|espalda/i },
    { id: "inguinal-canal", g: "Ingle y pelvis", nombre: "Conducto inguinal y femoral, regiones vecinas", clave: /inguinal|femoral|hernia|ingle/i },
    { id: "inguinal-and-femoral-canal-hernia-surgery", g: "Ingle y pelvis", nombre: "Conducto inguinal y femoral: cirugía de hernia", clave: /hernioplast|herniorraf|lichtenstein/i },
    { id: "inguinal-ligament", g: "Ingle y pelvis", sub: "start", nombre: "Ligamento inguinal y estructuras relacionadas", clave: /ligamento inguinal|arco crural/i },
    { id: "pelvicfloor", g: "Ingle y pelvis", nombre: "Suelo pélvico y periné", clave: /pelvis|periné|perine|suelo p[eé]lvico|elevador del ano|prolapso|continencia/i },
    { id: "upper-limb", g: "Miembro superior", nombre: "Miembro superior completo", clave: /miembro superior|brazo|antebrazo|h[uú]mero|axila|radio|cubital/i },
    { id: "zone-shoulder", g: "Miembro superior", nombre: "Hombro", clave: /hombro|escapul|clav[ií]cula|gleno|acromio|deltoid/i },
    { id: "shoulder-and-pectoral-girdle-joints", g: "Miembro superior", sub: "capsules-and-ligaments-hidden", nombre: "Articulaciones del hombro y cintura escapular", clave: /cintura escapular|esternoclavicular|acromioclavicular/i },
    { id: "rotator-cuff", g: "Miembro superior", nombre: "Manguito de los rotadores", clave: /manguito|rotador|supraespinoso|infraespinoso|subescapular|redondo menor/i },
    { id: "upper-limb-scapulohumeral-muscles", g: "Miembro superior", sub: "muscles-and-bursae-and-ligament-parts-hidden", nombre: "Músculos escapulohumerales", clave: /escapulohumeral|redondo mayor/i },
    { id: "upper-limb-axio-appendicular-muscles", g: "Miembro superior", sub: "muscles-and-bursae-and-ligament-parts-hidden", nombre: "Músculos axio-apendiculares", clave: /axio.?apendicular|pectoral|serrato|romboides/i },
    { id: "upper-limb-arm-muscles", g: "Miembro superior", sub: "muscles-and-bursae-and-ligament-parts-hidden", nombre: "Músculos del brazo", clave: /b[ií]ceps|tr[ií]ceps|braquial|coracobraquial/i },
    { id: "zone-elbow", g: "Miembro superior", nombre: "Codo", clave: /codo|olecran|epic[oó]ndilo|supracondíl|supracond[ií]l/i },
    { id: "upper-limb-forearm-anterior-compartment-muscles", g: "Miembro superior", sub: "muscles-and-sheaths-hidden", nombre: "Músculos del compartimento anterior del antebrazo", clave: /antebrazo anterior|flexores del antebrazo|pronador/i },
    { id: "upper-limb-bones-and-cartilages", g: "Miembro superior", sub: "trunk-hidden", nombre: "Huesos y cartílagos del miembro superior", clave: /huesos del miembro superior/i },
    { id: "hand", g: "Mano y muñeca", nombre: "Mano y muñeca (completa)", clave: /mano|mu[nñ]eca|dedo|t[uú]nel|metacarp/i },
    { id: "hand-and-wrist-bones-and-cartilages", g: "Mano y muñeca", nombre: "Mano y muñeca: huesos y cartílagos", clave: /carpo|escafoid|semilunar|ganchoso|huesos de la mano/i },
    { id: "hand-and-wrist-joints", g: "Mano y muñeca", nombre: "Mano y muñeca: articulaciones", clave: /articulaciones de la mano|interfal[aá]ngica/i },
    { id: "brachial-plexus-and-branches", g: "Nervios del miembro superior", nombre: "Plexo braquial y nervios que irriga", clave: /plexo braquial|erb|klumpke|plexopat/i },
    { id: "shoulder-brachial-plexus", g: "Nervios del miembro superior", nombre: "Plexo braquial en el hombro", clave: /troncos del plexo|supraclavicular/i },
    { id: "axillary-nerve", g: "Nervios del miembro superior", nombre: "Nervio axilar", clave: /axilar|circunflejo/i },
    { id: "musculocutaneous-nerve", g: "Nervios del miembro superior", nombre: "Nervio musculocutáneo", clave: /musculocut/i },
    { id: "radial-nerve", g: "Nervios del miembro superior", nombre: "Nervio radial", clave: /nervio radial|ca[ií]da de la mano|saturday/i },
    { id: "median-nerve", g: "Nervios del miembro superior", nombre: "Nervio mediano", clave: /mediano|t[uú]nel del carpo|bendici[oó]n/i },
    { id: "ulnar-nerve", g: "Nervios del miembro superior", nombre: "Nervio cubital (ulnar)", clave: /cubital|ulnar|garra/i },
    { id: "lower-limb", g: "Miembro inferior", nombre: "Miembro inferior completo", clave: /miembro inferior|muslo|f[eé]mur|tibia|peron/i },
    { id: "zone-hip", g: "Miembro inferior", nombre: "Cadera", clave: /cadera|acet[aá]bulo|cuello femoral|coxofemoral|ilio/i },
    { id: "muscles-gluteal-region-abductors-rotators-thigh", g: "Miembro inferior", nombre: "Región glútea: abductores y rotadores del muslo", clave: /gl[uú]te|piriforme|ci[aá]tico|ciático|rotadores del muslo/i },
    { id: "ant-thigh-hip-flexors", g: "Miembro inferior", nombre: "Flexores de la cadera", clave: /flexores de la cadera|psoas|ilíaco|iliaco|sartorio/i },
    { id: "muscles-anterior-thigh-extensors-knee", g: "Miembro inferior", nombre: "Muslo anterior: extensores de la rodilla", clave: /cu[aá]driceps|extensores de la rodilla|rotuliano/i },
    { id: "medial-thigh-adductors-of-thigh", g: "Miembro inferior", nombre: "Muslo medial: aductores", clave: /aductor|gr[aá]cil|conducto de hunter/i },
    { id: "zone-knee", g: "Miembro inferior", nombre: "Rodilla", clave: /rodilla|menisco|cruzado|r[oó]tula|patela/i },
    { id: "muscles-deep-superficial-posterior-comp-leg", g: "Miembro inferior", nombre: "Pierna posterior: músculos superficiales y profundos", clave: /pierna|gemelo|s[oó]leo|aquiles|tibial posterior/i },
    { id: "zone-ankle", g: "Miembro inferior", nombre: "Tobillo y pie", clave: /tobillo|pie\b|astr[aá]galo|calc[aá]neo|esguince|talo/i },
    { id: "insertions-and-origins", g: "Músculos", nombre: "Orígenes e inserciones musculares (esqueleto)", clave: /inserci[oó]n|origen muscular/i }
  ];
  var panel = null, previo = null;

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function disponible() { return MODELOS.length > 0; }
  /* ¿La pregunta es de anatomía? Se mira la categoría, el tema y la especialidad. */
  function esAnatomia(q) {
    if (!q) return false;
    return /anatom/i.test([q.categoria, q.tema, q.especialidad].join(" "));
  }
  function modeloPara(tema) {
    var t = String(tema || "");
    for (var i = 0; i < MODELOS.length; i++) if (MODELOS[i].clave.test(t)) return i;
    return 0;
  }
  function credito() {
    return '<p class="an-credito">Modelo y visor 3D abiertos del Dept. de Anatomía y Embriología del <b>LUMC</b> (Leiden) y universidades de Países Bajos y Bélgica · ' +
      '<a href="https://anatomytool.org/open3dmodel" target="_blank" rel="noopener noreferrer">Open 3D Model</a> · licencia ' +
      '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a> (visor: GPL 3.0). ' +
      'Material educativo; no sustituye el diagnóstico médico.' +
      (CFG.externo ? ' · <a href="' + esc(CFG.externo) + '" target="_blank" rel="noopener noreferrer">Otro atlas (Anatomy Learning)</a>' : "") + '</p>';
  }
  function selector(actual) {
    var grupos = [], html = "";
    MODELOS.forEach(function (m, i) { if (grupos.indexOf(m.g) < 0) grupos.push(m.g); });
    grupos.forEach(function (g) {
      html += '<optgroup label="' + esc(g) + '">';
      MODELOS.forEach(function (m, i) { if (m.g === g) html += '<option value="' + i + '"' + (i === actual ? " selected" : "") + ">" + esc(m.nombre) + "</option>"; });
      html += "</optgroup>";
    });
    return '<label class="an-sel">Región: <select data-an-modelo>' + html + "</select></label>";
  }
  function src(i) { var m = MODELOS[i] || MODELOS[0]; return CFG.base + "?model=" + encodeURIComponent(m.id) + (m.sub ? "&subset=" + encodeURIComponent(m.sub) : ""); }
  function marco(clase, id) {
    return selector(id) + '<iframe class="an-marco ' + (clase || "") + '" src="' + esc(src(id)) + '" title="Atlas 3D de anatomía (' + esc(CFG.nombre) + ')" loading="lazy" ' +
      'allow="fullscreen" allowfullscreen></iframe>' + credito();
  }
  /* Cambiar de región sin recargar la página del simulador. */
  function enlazar(raiz) {
    var sel = raiz.querySelector("[data-an-modelo]"), fr = raiz.querySelector("iframe.an-marco");
    if (sel && fr) sel.addEventListener("change", function () { fr.src = src(+sel.value); });
  }

  /* Página aparte dentro del simulador: #/anatomia */
  function pagina(par) {
    var id = modeloPara(par && par.tema);
    var pista = par && par.tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(par.tema) + '</b></p>' : "";
    setTimeout(function () { var r = document.querySelector(".an-marco--pagina"); if (r) enlazar(r.parentNode); }, 0);
    return '<header class="page-head"><p class="kicker">Anatomía</p><h1 class="page-head__title">Atlas de anatomía en 3D</h1>' +
      '<p class="page-head__lead">Explora las estructuras en 3D: arrastra para rotar, usa la rueda o pellizca para acercar, toca una estructura para ver su nombre y oculta capas con el menú superior.</p></header>' + pista +
      '<div class="an-pagina">' + marco("an-marco--pagina", id) + '</div>';
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
      (tema ? '<p class="an-pista">Para esta pregunta, busca en el atlas: <b>' + esc(tema) + '</b></p>' : "") + marco("an-marco--ventana", modeloPara(tema)) + '</div>';
    document.body.appendChild(panel); enlazar(panel);
    panel.addEventListener("click", function (ev) { if (ev.target === panel || (ev.target.closest && ev.target.closest("[data-x]"))) cerrar(); });
    panel.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
    if (panel.showModal) panel.showModal(); else panel.setAttribute("open", "");
    var x = panel.querySelector(".fc-x"); if (x && x.focus) x.focus();
  }

  function mostrarMenu() { var n = document.getElementById("navAna"); if (n) n.hidden = !disponible(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mostrarMenu); else mostrarMenu();

  M.anatomia = { disponible: disponible, esAnatomia: esAnatomia, abrir: abrir, cerrar: cerrar, pagina: pagina, config: CFG, modelos: MODELOS };
})();
