/* MedQuizPlus — capa de datos compartida entre la web pública (index.html) y la
 * plataforma (app/index.html). Script clásico, sin dependencias.
 *
 * Expone window.MQP con:
 *   MQP.base            ruta a la raíz del sitio ("" en la raíz, "../" desde app/)
 *   MQP.examenes        ENAM, Residentado Médico y EsSalud
 *   MQP.areas           agrupación de las especialidades para navegar
 *   MQP.especialidades  los 17 bancos de bancos/<archivo>.json
 *   MQP.simuladores     simulacros armados SOLO con preguntas reales de los bancos
 *   MQP.cargarBanco()   lee y normaliza un banco
 *   MQP.cargarTodo()    lee todos los bancos
 *   MQP.filtrar()       selecciona preguntas por examen, especialidad, estado…
 *   MQP.progreso        progreso del estudiante (hoy: localStorage del navegador)
 *
 * Para añadir contenido no hace falta tocar el diseño:
 *   - Nueva pregunta: se agrega a su bancos/<archivo>.json. El campo "examen_origen"
 *     decide a qué examen pertenece (empieza por "ENAM", "Residentado" o "EsSalud").
 *   - Nueva especialidad: se crea el .json y se añade una línea en ESPECIALIDADES.
 *   - Residentado / EsSalud con banco propio: basta con cargar preguntas con ese
 *     "examen_origen" y cambiar su estado a "disponible" en EXAMENES.
 *   - Categorías (materias) dentro de una especialidad: se listan en "categorias: [...]"
 *     y cada pregunta de ese banco lleva el campo "categoria" con uno de esos nombres.
 *     Con la lista llena, la tarjeta y el armador del banco dejan elegir una materia o
 *     todas. Hoy la usa Ciencias Básicas; las demás tienen "categorias: []".
 */
(function () {
  "use strict";

  /* ---------- raíz del sitio, deducida de dónde se cargó este archivo ---------- */
  var base = "";
  try {
    var s = document.currentScript && document.currentScript.getAttribute("src");
    if (s) base = s.replace(/[?#].*$/, "").replace(/catalogo\.js$/, "");
  } catch (e) { base = ""; }

  /* ---------- iconos (trazos SVG 24×24) ---------- */
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
    matraz: '<path d="M9 3h6M10 3v6.2L5 18a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 18l-5-8.8V3"/><path d="M7.4 15h9.2"/>',
    /* iconos de interfaz */
    libro: '<path d="M4 19.5V5a2 2 0 0 1 2-2h13v15H6a2 2 0 0 0-2 2z"/><path d="M8 7h7M8 11h5"/>',
    reloj: '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M9.5 2.5h5"/>',
    rayo: '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    diana: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    casa: '<path d="M4 10.5 12 4l8 6.5V20a1 1 0 0 1-1 1h-4.5v-6h-5v6H5a1 1 0 0 1-1-1z"/>',
    capas: '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    cruz: '<path d="M6 6l12 12M18 6L6 18"/>',
    estrella: '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/>',
    usuario: '<circle cx="12" cy="8" r="4"/><path d="M4 20.5c1.4-3.6 4.4-5.5 8-5.5s6.6 1.9 8 5.5"/>',
    flujo: '<rect x="9" y="2.5" width="6" height="5" rx="1"/><rect x="3" y="16.5" width="6" height="5" rx="1"/><rect x="15" y="16.5" width="6" height="5" rx="1"/><path d="M12 7.5v4M6 16.5V14h12v2.5M12 11.5V14"/>',
    chat: '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-3.6-.7L3 21l1.9-5.1A8.4 8.4 0 0 1 4.1 11a8.4 8.4 0 0 1 8.4-8.4h.5A8.4 8.4 0 0 1 21 11v.5z"/>',
    flecha: '<path d="M5 12h14M13 6l6 6-6 6"/>',
    check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    candado: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'
  };
  function icono(nombre, clase) {
    return '<svg' + (clase ? ' class="' + clase + '"' : "") + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (ICONOS[nombre] || "") + "</svg>";
  }

  /* ---------- exámenes ----------
     estado: "disponible" | "proximamente". "coincide" decide qué preguntas son de
     cada examen a partir del campo examen_origen del banco. */
  var EXAMENES = [
    { id: "enam", nombre: "ENAM", nombreLargo: "Examen Nacional de Medicina", estado: "disponible",
      coincide: /^ENAM/i, titulo: "Preparación ENAM",
      lema: "Entrena por especialidad, resuelve preguntas comentadas y mide tu progreso." },
    { id: "residentado", nombre: "Residentado Médico", nombreLargo: "Residentado Médico", estado: "proximamente",
      coincide: /^Residentado/i, titulo: "Preparación para Residentado Médico",
      lema: "El banco por especialidad para el Residentado está en construcción." },
    { id: "essalud", nombre: "EsSalud", nombreLargo: "EsSalud", estado: "proximamente",
      coincide: /^EsSalud/i, titulo: "Preparación para EsSalud",
      lema: "El banco por especialidad para EsSalud está en construcción." }
  ];

  /* ---------- áreas: solo agrupan especialidades que ya existen ---------- */
  var AREAS = [
    { id: "medicina", nombre: "Medicina Interna" },
    { id: "cirugia", nombre: "Cirugía" },
    { id: "pediatria", nombre: "Pediatría" },
    { id: "gineco", nombre: "Ginecología y Obstetricia" },
    { id: "salud_publica", nombre: "Salud Pública" },
    { id: "basicas", nombre: "Ciencias Básicas" }
  ];

  /* ---------- especialidades: un banco = un archivo en bancos/ ---------- */
  var ESPECIALIDADES = [
    { nombre: "Cardiología", archivo: "cardiologia", icono: "corazon", area: "medicina", categorias: [] },
    { nombre: "Neumología", archivo: "neumologia", icono: "pulmones", area: "medicina", categorias: [] },
    { nombre: "Gastroenterología", archivo: "gastroenterologia", icono: "estomago", area: "medicina", categorias: [] },
    { nombre: "Nefrología y Urología", archivo: "nefrologia", icono: "rinon", area: "medicina", categorias: [] },
    { nombre: "Endocrinología", archivo: "endocrinologia", icono: "tiroides", area: "medicina", categorias: [] },
    { nombre: "Infectología", archivo: "infectologia", icono: "virus", area: "medicina", categorias: [] },
    { nombre: "Neurología", archivo: "neurologia", icono: "cerebro", area: "medicina", categorias: [] },
    { nombre: "Hematología", archivo: "hematologia", icono: "gota", area: "medicina", categorias: [] },
    { nombre: "Reumatología y Dermatología", archivo: "reumatologia", icono: "articulacion", area: "medicina", categorias: [] },
    { nombre: "Pediatría y Neonatología", archivo: "pediatria", icono: "bebe", area: "pediatria", categorias: [] },
    { nombre: "Ginecología y Obstetricia", archivo: "ginecologia", icono: "femenino", area: "gineco", categorias: [] },
    { nombre: "Cirugía General y Digestiva", archivo: "cirugia", icono: "bisturi", area: "cirugia", categorias: [] },
    { nombre: "Traumatología y Ortopedia", archivo: "traumatologia", icono: "hueso", area: "cirugia", categorias: [] },
    { nombre: "Oftalmología y Otorrinolaringología", archivo: "oftalmo_orl", icono: "ojo", area: "cirugia", categorias: [] },
    { nombre: "Psiquiatría", archivo: "psiquiatria", icono: "mente", area: "medicina", categorias: [] },
    { nombre: "Salud Pública, Gestión y Epidemiología", archivo: "salud_publica", icono: "grafico", area: "salud_publica", categorias: [] },
    { nombre: "Ciencias Básicas", archivo: "ciencias_basicas", icono: "matraz", area: "basicas",
      categorias: ["Anatomía", "Histología y Biología Celular", "Embriología", "Fisiología",
        "Bioquímica y Genética", "Microbiología e Inmunología", "Farmacología básica y autonómica",
        "Patología general", "Epidemiología y Bioestadística"] }
  ];

  /* ---------- simuladores ----------
     Todos se arman con preguntas reales. segundosPorPregunta: 60, el mismo ritmo
     que usa la barra de tiempo del banco. Los "proximamente" no se pueden iniciar. */
  var SIMULADORES = [
    { id: "enam-2020", examen: "enam", estado: "disponible", icono: "diana",
      titulo: "Simulacro ENAM 2020",
      descripcion: "Las preguntas oficiales del ENAM 2020 publicadas en el banco, en un solo bloque cronometrado.",
      origen: /ENAM 2020/i, cantidad: null, orden: "secuencial", segundosPorPregunta: 60 },
    { id: "enam-rapido", examen: "enam", estado: "disponible", icono: "rayo",
      titulo: "Simulacro rápido ENAM",
      descripcion: "Preguntas ENAM al azar de todas las especialidades para medir tu ritmo en poco tiempo.",
      cantidad: 20, orden: "aleatorio", segundosPorPregunta: 60 },
    { id: "enam-especialidad", examen: "enam", estado: "disponible", icono: "capas",
      titulo: "Simulacro por especialidad",
      descripcion: "Eliges la especialidad y resuelves sus preguntas ENAM contra el reloj.",
      cantidad: 10, orden: "aleatorio", segundosPorPregunta: 60, eligeEspecialidad: true },
    { id: "residentado", examen: "residentado", estado: "proximamente", icono: "reloj",
      titulo: "Simulacro Residentado Médico",
      descripcion: "Se habilitará cuando el banco de Residentado esté completo." },
    { id: "essalud", examen: "essalud", estado: "proximamente", icono: "reloj",
      titulo: "Simulacro EsSalud",
      descripcion: "Se habilitará cuando el banco de EsSalud esté completo." }
  ];

  function buscar(lista, clave, valor) {
    for (var k = 0; k < lista.length; k++) if (lista[k][clave] === valor) return lista[k];
    return null;
  }

  function examenDe(origen) {
    for (var k = 0; k < EXAMENES.length; k++) if (EXAMENES[k].coincide.test(origen || "")) return EXAMENES[k].id;
    return "";
  }

  /* ---------- carga de bancos ----------
     Formato: { especialidad, preguntas: [ { id, especialidad, examen_origen, enunciado,
     opciones: { A: "…" } o [ "…" ], clave_correcta: "B", comentario, tema?, categoria?, año? } ] }.
     Si la página es un solo archivo (artifact.html), los bancos vienen en window.MQP_BANCOS. */
  function normalizar(datos, archivo) {
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
      var origen = p.examen_origen || "";
      salida.push({
        id: p.id, especialidad: p.especialidad, archivo: archivo, examen: origen,
        examenId: examenDe(origen), oficial: /oficial/i.test(origen),
        tema: p.tema ? String(p.tema) : "", categoria: p.categoria ? String(p.categoria) : "", anio: p["año"] || p.anio || null,
        enunciado: String(p.enunciado), opciones: ops,
        clave: String(p.clave_correcta || "").trim().toUpperCase(),
        comentario: p.comentario ? String(p.comentario) : ""
      });
    }
    return salida;
  }

  var cache = {};
  function cargarBanco(archivo) {
    if (cache[archivo]) return cache[archivo];
    var incrustado = window.MQP_BANCOS && window.MQP_BANCOS[archivo];
    var promesa = incrustado
      ? Promise.resolve(incrustado)
      : fetch(base + "bancos/" + archivo + ".json", { cache: "no-cache" }).then(function (res) {
          if (!res.ok) throw new Error("http " + res.status);
          return res.json();   // si el servidor devuelve HTML (404 reescrito), esto falla y cae al catch
        });
    cache[archivo] = promesa.then(function (d) { return normalizar(d, archivo); });
    cache[archivo].catch(function () { delete cache[archivo]; });  // permite reintentar
    return cache[archivo];
  }

  /* Carga todos los bancos; un banco que falla no tumba a los demás. */
  var todo = null;
  function cargarTodo() {
    if (todo) return todo;
    todo = Promise.all(ESPECIALIDADES.map(function (esp) {
      return cargarBanco(esp.archivo).then(
        function (ps) { return { archivo: esp.archivo, ok: true, preguntas: ps }; },
        function () { return { archivo: esp.archivo, ok: false, preguntas: [] }; }
      );
    })).then(function (res) {
      var porArchivo = {}, preguntas = [], fallos = 0;
      for (var k = 0; k < res.length; k++) {
        porArchivo[res[k].archivo] = res[k];
        if (!res[k].ok) fallos++;
        preguntas = preguntas.concat(res[k].preguntas);
      }
      if (fallos) todo = null;   // reintenta la próxima vez
      return { preguntas: preguntas, porArchivo: porArchivo, fallos: fallos };
    });
    return todo;
  }

  /* ---------- selección de preguntas ----------
     opciones: { examen, archivos: [], origen: RegExp, filtro: "todas" | "no-respondidas"
     | "falladas" | "favoritas", ids: [], categorias: [] (o categoria: "…") }.
     "categorias" solo recorta las especialidades que tienen materias; las demás pasan igual. */
  function filtrar(preguntas, o) {
    o = o || {};
    var archivos = o.archivos && o.archivos.length ? o.archivos : null;
    var ids = o.ids && o.ids.length ? o.ids : null;
    var estado = o.filtro && o.filtro !== "todas" ? progreso.leer() : null;
    var cats = o.categorias && o.categorias.length ? o.categorias : (o.categoria ? [o.categoria] : null);
    var salida = [];
    for (var k = 0; k < preguntas.length; k++) {
      var q = preguntas[k];
      if (ids && ids.indexOf(q.id) < 0) continue;
      if (o.examen && q.examenId !== o.examen) continue;
      if (archivos && archivos.indexOf(q.archivo) < 0) continue;
      if (o.origen && !o.origen.test(q.examen)) continue;
      if (cats && tieneCategorias(q.archivo) && cats.indexOf(q.categoria) < 0) continue;
      if (estado) {
        var r = estado.respuestas[q.id];
        if (o.filtro === "no-respondidas" && r) continue;
        if (o.filtro === "falladas" && !(r && !r.ok)) continue;
        if (o.filtro === "favoritas" && !estado.favoritos[q.id]) continue;
      }
      salida.push(q);
    }
    if (ids) salida.sort(function (a, b) { return ids.indexOf(a.id) - ids.indexOf(b.id); });
    return salida;
  }

  function tieneCategorias(archivo) {
    for (var k = 0; k < ESPECIALIDADES.length; k++)
      if (ESPECIALIDADES[k].archivo === archivo) return ESPECIALIDADES[k].categorias.length > 0;
    return false;
  }

  /* Cuántas preguntas hay de cada materia: { "Anatomía": 70, … }. */
  function contarCategorias(preguntas) {
    var c = {};
    for (var k = 0; k < preguntas.length; k++) {
      var n = preguntas[k].categoria;
      if (n) c[n] = (c[n] || 0) + 1;
    }
    return c;
  }

  function barajar(lista) {
    var a = lista.slice();
    for (var k = a.length - 1; k > 0; k--) {
      var j = Math.floor(Math.random() * (k + 1));
      var t = a[k]; a[k] = a[j]; a[j] = t;
    }
    return a;
  }

  /* ======================================================================
     Progreso del estudiante
     Hoy vive en localStorage de este navegador (clave mqp_progreso_v1): son datos
     reales de lo que el estudiante resolvió aquí, nunca cifras de ejemplo.
     Cuando exista backend con cuentas, basta con reimplementar leer() y escribir()
     contra la API; el resto de la plataforma no cambia.
     ====================================================================== */
  var CLAVE = "mqp_progreso_v1";
  var MAX_SESIONES = 40;

  function vacio() {
    return { v: 1, respuestas: {}, favoritos: {}, sesiones: [], ultima: null, preferencias: {} };
  }
  var memoria = null;   // copia en memoria si localStorage no está disponible

  function leer() {
    try {
      var crudo = localStorage.getItem(CLAVE);
      if (crudo) {
        var d = JSON.parse(crudo);
        if (d && d.v === 1) {
          d.respuestas = d.respuestas || {}; d.favoritos = d.favoritos || {};
          d.sesiones = d.sesiones || []; d.preferencias = d.preferencias || {};
          return d;
        }
      }
    } catch (e) { if (memoria) return memoria; }
    return memoria || vacio();
  }
  function escribir(d) {
    memoria = d;
    try { localStorage.setItem(CLAVE, JSON.stringify(d)); } catch (e) {}
    try { window.dispatchEvent(new CustomEvent("mqp:progreso")); } catch (e) {}
  }

  var progreso = {
    leer: leer,
    /* guarda el último intento de cada pregunta */
    registrar: function (q, letra) {
      if (!q || !q.id || !letra) return;
      var d = leer();
      var previo = d.respuestas[q.id];
      d.respuestas[q.id] = { l: letra, ok: letra === q.clave, t: Date.now(), a: q.archivo, x: q.examenId, n: (previo ? previo.n || 1 : 0) + 1 };
      escribir(d);
    },
    registrarVarias: function (lista) {
      var d = leer(), ahora = Date.now();
      for (var k = 0; k < lista.length; k++) {
        var q = lista[k].q, letra = lista[k].letra;
        if (!q || !q.id || !letra) continue;
        var previo = d.respuestas[q.id];
        d.respuestas[q.id] = { l: letra, ok: letra === q.clave, t: ahora, a: q.archivo, x: q.examenId, n: (previo ? previo.n || 1 : 0) + 1 };
      }
      escribir(d);
    },
    esFavorita: function (id) { return !!leer().favoritos[id]; },
    alternarFavorita: function (id) {
      var d = leer();
      if (d.favoritos[id]) delete d.favoritos[id]; else d.favoritos[id] = Date.now();
      escribir(d);
      return !!d.favoritos[id];
    },
    agregarSesion: function (s) {
      var d = leer();
      s.t = s.t || Date.now();
      d.sesiones.unshift(s);
      if (d.sesiones.length > MAX_SESIONES) d.sesiones.length = MAX_SESIONES;
      escribir(d);
    },
    guardarUltima: function (u) { var d = leer(); d.ultima = u; escribir(d); },
    limpiarUltima: function () { var d = leer(); if (d.ultima) { d.ultima = null; escribir(d); } },
    preferencia: function (clave, valor) {
      var d = leer();
      if (arguments.length < 2) return d.preferencias[clave];
      d.preferencias[clave] = valor; escribir(d);
      return valor;
    },
    borrar: function () { memoria = null; try { localStorage.removeItem(CLAVE); } catch (e) {} escribir(vacio()); },
    /* resumen calculado, opcionalmente limitado a un examen */
    resumen: function (examen) {
      var d = leer(), total = 0, bien = 0, porArchivo = {};
      for (var id in d.respuestas) {
        if (!Object.prototype.hasOwnProperty.call(d.respuestas, id)) continue;
        var r = d.respuestas[id];
        if (examen && r.x && r.x !== examen) continue;
        total++; if (r.ok) bien++;
        var a = porArchivo[r.a] || (porArchivo[r.a] = { respondidas: 0, correctas: 0 });
        a.respondidas++; if (r.ok) a.correctas++;
      }
      return { respondidas: total, correctas: bien, porcentaje: total ? Math.round(bien / total * 100) : null, porArchivo: porArchivo };
    }
  };

  /* ---------- utilidades de presentación ---------- */
  function miles(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
  function plural(n, uno, varios) { return n + " " + (n === 1 ? uno : varios); }
  function duracion(seg) {
    seg = Math.max(0, Math.round(seg));
    var h = Math.floor(seg / 3600), m = Math.floor(seg % 3600 / 60);
    if (seg < 60) return seg + " s";
    if (h) return h + " h" + (m ? " " + m + " min" : "");
    return m + " min";
  }

  window.MQP = {
    base: base,
    iconos: ICONOS,
    icono: icono,
    examenes: EXAMENES,
    areas: AREAS,
    especialidades: ESPECIALIDADES,
    simuladores: SIMULADORES,
    examen: function (id) { return buscar(EXAMENES, "id", id); },
    area: function (id) { return buscar(AREAS, "id", id); },
    especialidad: function (archivo) { return buscar(ESPECIALIDADES, "archivo", archivo); },
    simulador: function (id) { return buscar(SIMULADORES, "id", id); },
    examenDe: examenDe,
    cargarBanco: cargarBanco,
    cargarTodo: cargarTodo,
    filtrar: filtrar,
    contarCategorias: contarCategorias,
    barajar: barajar,
    progreso: progreso,
    miles: miles,
    plural: plural,
    duracion: duracion
  };
})();
