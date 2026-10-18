/* MedQuizPlus — universidades del Perú que ofrecen Medicina Humana.
 *
 * Fuente única para los formularios de registro (landing y app). Para agregar o quitar una, edita solo esta lista:
 * cada línea es [nombre completo, siglas, tipo]. El orden es alfabético dentro de cada grupo.
 *
 * Revisión pendiente: esta lista se armó con información pública general, no con el registro oficial. Antes de darla por
 * definitiva contrástala con el listado de licenciamiento de la SUNEDU (sunedu.gob.pe) y con la lista de facultades
 * miembros de ASPEFAM (aspefam.org.pe), que cambian cada año.
 */
(function () {
  "use strict";
  var PUBLICAS = [
    ["Universidad Nacional Daniel Alcides Carrión", "UNDAC", "Pasco"],
    ["Universidad Nacional de Cajamarca", "UNC", "Cajamarca"],
    ["Universidad Nacional de la Amazonía Peruana", "UNAP", "Iquitos"],
    ["Universidad Nacional de Moquegua", "UNAM", "Moquegua"],
    ["Universidad Nacional de Piura", "UNP", "Piura"],
    ["Universidad Nacional de San Agustín de Arequipa", "UNSA", "Arequipa"],
    ["Universidad Nacional de San Antonio Abad del Cusco", "UNSAAC", "Cusco"],
    ["Universidad Nacional de San Cristóbal de Huamanga", "UNSCH", "Ayacucho"],
    ["Universidad Nacional de San Martín", "UNSM", "Tarapoto"],
    ["Universidad Nacional de Trujillo", "UNT", "Trujillo"],
    ["Universidad Nacional de Tumbes", "UNTUMBES", "Tumbes"],
    ["Universidad Nacional de Ucayali", "UNU", "Pucallpa"],
    ["Universidad Nacional del Altiplano", "UNA Puno", "Puno"],
    ["Universidad Nacional del Centro del Perú", "UNCP", "Huancayo"],
    ["Universidad Nacional Federico Villarreal", "UNFV", "Lima"],
    ["Universidad Nacional Hermilio Valdizán", "UNHEVAL", "Huánuco"],
    ["Universidad Nacional Jorge Basadre Grohmann", "UNJBG", "Tacna"],
    ["Universidad Nacional José Faustino Sánchez Carrión", "UNJFSC", "Huacho"],
    ["Universidad Nacional Mayor de San Marcos", "UNMSM", "Lima"],
    ["Universidad Nacional Pedro Ruiz Gallo", "UNPRG", "Lambayeque"],
    ["Universidad Nacional San Luis Gonzaga", "UNICA", "Ica"]
  ];
  var PRIVADAS = [
    ["Universidad Alas Peruanas", "UAP", ""],
    ["Universidad Andina del Cusco", "UAC", "Cusco"],
    ["Universidad Andina Néstor Cáceres Velásquez", "UANCV", "Juliaca"],
    ["Universidad Católica de Santa María", "UCSM", "Arequipa"],
    ["Universidad Católica Los Ángeles de Chimbote", "ULADECH", "Chimbote"],
    ["Universidad Católica Santo Toribio de Mogrovejo", "USAT", "Chiclayo"],
    ["Universidad Científica del Sur", "UCSUR", "Lima"],
    ["Universidad Continental", "UC", "Huancayo / Lima"],
    ["Universidad de Ciencias y Humanidades", "UCH", "Lima"],
    ["Universidad de Piura", "UDEP", "Piura / Lima"],
    ["Universidad de San Martín de Porres", "USMP", "Lima"],
    ["Universidad Norbert Wiener", "UNW", "Lima"],
    ["Universidad Peruana Cayetano Heredia", "UPCH", "Lima"],
    ["Universidad Peruana de Ciencias Aplicadas", "UPC", "Lima"],
    ["Universidad Peruana Los Andes", "UPLA", "Huancayo"],
    ["Universidad Peruana Unión", "UPeU", "Lima"],
    ["Universidad Privada Antenor Orrego", "UPAO", "Trujillo"],
    ["Universidad Privada Antonio Guillermo Urrelo", "UPAGU", "Cajamarca"],
    ["Universidad Privada de Tacna", "UPT", "Tacna"],
    ["Universidad Privada San Juan Bautista", "UPSJB", "Lima / Ica"],
    ["Universidad Ricardo Palma", "URP", "Lima"],
    ["Universidad San Ignacio de Loyola", "USIL", "Lima"],
    ["Universidad San Pedro", "USP", "Chimbote"],
    ["Universidad Señor de Sipán", "USS", "Chiclayo"],
    ["Universidad Tecnológica del Perú", "UTP", "Lima"],
    ["Universidad César Vallejo", "UCV", "Trujillo / Lima"]
  ];
  function fila(u) { return { nombre: u[0], siglas: u[1], sede: u[2] }; }
  var cmp = function (a, b) { return a[0].localeCompare(b[0], "es"); };
  window.MQP_UNIVERSIDADES = {
    publicas: PUBLICAS.slice().sort(cmp).map(fila),
    privadas: PRIVADAS.slice().sort(cmp).map(fila),
    otras: ["Otra universidad del Perú", "Universidad del extranjero", "Ya soy médico(a) / egresado(a)"],
    /* devuelve <option>…</option> agrupadas, listas para meter en un <select> */
    opciones: function (seleccionada) {
      function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;"); }
      function grupo(t, L) { return '<optgroup label="' + t + '">' + L.map(function (u) { var v = u.nombre + (u.siglas ? " (" + u.siglas + ")" : ""); return '<option value="' + esc(v) + '"' + (v === seleccionada ? " selected" : "") + ">" + esc(v) + "</option>"; }).join("") + "</optgroup>"; }
      return '<option value="">Selecciona tu universidad</option>' + grupo("Universidades públicas", this.publicas) + grupo("Universidades privadas", this.privadas) +
        '<optgroup label="Otras">' + this.otras.map(function (o) { return '<option value="' + esc(o) + '">' + esc(o) + "</option>"; }).join("") + "</optgroup>";
    }
  };
  /* si la página trae <select data-universidades>, se llena sola */
  function llenar() { var s = document.querySelectorAll("select[data-universidades]"); for (var i = 0; i < s.length; i++) s[i].innerHTML = window.MQP_UNIVERSIDADES.opciones(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", llenar); else llenar();
})();
