// node tests/biblioteca_test.js — Biblioteca de valores de laboratorio: estructura, cobertura por áreas, formato (mayúsculas, unidades de uso en Perú, sin bibliografía),
// coherencia numérica de los intervalos y concordancia con el catálogo que usan los casos (no puede haber dos valores distintos para el mismo análisis).
"use strict";
const cp = require("child_process"), path = require("path");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
global.window = {}; const B = require("../guardia_biblioteca.js"), CAT = require("../guardia_lab.js");
ok(cp.spawnSync("python3", [path.join(RAIZ, "tools/guardia_empaquetar.py"), "--check"]).status === 0, "guardia_biblioteca.js está al día con guardia/biblioteca_lab.json");
const todas = [].concat(...B.areas.map(a => a.pruebas.map(t => ({ a, t }))));
ok(B.areas.length >= 18 && todas.length >= 300, "cobertura amplia: " + B.areas.length + " áreas y " + todas.length + " análisis");
ok(/orientativos/i.test(B.nota) && B.nota.length < 200, "una sola nota breve de que los valores son orientativos");
const nombresArea = B.areas.map(a => a.nombre).join(" | ");
for (const k of ["Hematología", "Coagulación", "Glucosa", "lipídico", "renal", "Hígado", "Electrolitos", "Hierro", "cardíacos", "Gasometría", "Orina", "Heces", "Tiroides", "hormonas sexuales", "inmunología", "Serología", "tumorales", "Líquidos", "Espermatograma", "fármacos"]) ok(nombresArea.includes(k), "área presente: " + k);
ok(new Set(B.areas.map(a => a.id)).size === B.areas.length && B.areas.every(a => /^#[0-9a-f]{6}$/i.test(a.color) && a.icono && a.pruebas.length >= 5), "áreas con id único, color, icono y contenido");
const ini = s => s && (s[0] === s[0].toUpperCase() || /^(pH|β)/.test(s));
const nombres = new Set();
for (const { a, t } of todas) {
  const id = a.nombre + "/" + t.n;
  ok(ini(t.n), id + ": el nombre empieza con mayúscula"); ok(typeof t.u === "string", id + ": unidad (puede estar vacía en pruebas cualitativas)");
  ok(Array.isArray(t.r) && t.r.length >= 1 && t.r.every(x => x.length === 2 && x[1].trim()), id + ": valores de referencia");
  ok(t.r.every(([g, v]) => (!g || ini(g)) && (ini(v) || /^[<≥>≤−\d]/.test(v) || /^(pH)/.test(v))), id + ": grupos y valores con mayúscula o signo inicial");
  ok(!nombres.has(t.n), id + ": nombre único"); nombres.add(t.n);
  ok(!/pmid|doi|http|et al|fuente|bibliograf|referencia:/i.test(JSON.stringify(t)), id + ": sin bibliografía ni enlaces");
  ok(!/mmol\/L|µmol\/L/.test(t.u) || /lactato|β-hidroxibutirato|calcio iónico|fructosamina|homocisteína|cobre|glucosa/i.test(t.n) || /Fructosamina|Homocisteína/.test(t.n), id + ": unidad de uso habitual en Perú (conv. mg/dL, mEq/L…) salvo excepciones propias");
  for (const [g, v] of t.r) { const m = /^(\d[\d ]*(?:\.\d+)?) – (\d[\d ]*(?:\.\d+)?)$/.exec(v); if (m) ok(parseFloat(m[1].replace(/ /g, "")) <= parseFloat(m[2].replace(/ /g, "")), id + " (" + g + "): intervalo " + v + " con límite inferior ≤ superior"); }
}
const T = n => todas.find(x => x.t.n === n);
for (const n of ["Hemoglobina", "Hematocrito", "Leucocitos (recuento total)", "Plaquetas", "Glucosa en ayunas (plasma venoso)", "Hemoglobina glicosilada", "Colesterol total", "Triglicéridos", "Urea", "Creatinina sérica", "Ácido úrico", "Aspartato aminotransferasa", "Alanina aminotransferasa", "Bilirrubina total", "Sodio", "Potasio", "Calcio total", "Hierro sérico", "Ferritina sérica", "Troponina T de alta sensibilidad", "pH arterial", "Presión parcial de O₂ arterial", "Hormona estimulante de tiroides", "Tiroxina libre", "Dímero D", "Proteína C reactiva", "Procalcitonina", "Prueba de VIH (anticuerpos y antígeno p24, 4.ª generación)", "Antígeno prostático específico total", "Líquido cefalorraquídeo: glucosa", "Concentración espermática", "Digoxina", "Gonadotropina coriónica humana subunidad β (sangre)", "Color", "Esterasa leucocitaria (tira reactiva)", "Examen parasitológico seriado", "Sangre oculta en heces (inmunoquímica)"]) ok(!!T(n), "análisis presente: " + n);
/* por edades cuando corresponde */
for (const [n, k] of [["Hemoglobina", 8], ["Hematocrito", 7], ["Creatinina sérica", 6], ["Leucocitos (recuento total)", 6], ["Bilirrubina total", 4], ["Fosfatasa alcalina", 4], ["Sodio", 4], ["Potasio", 4], ["Fósforo", 5], ["Ferritina sérica", 4]]) ok(T(n) && T(n).t.r.length >= k, n + ": valores diferenciados por edad/sexo/gestación (≥ " + k + ")");
ok(T("Hemoglobina").t.r.some(([g]) => /gestante/i.test(g)) && T("Creatinina sérica").t.r.some(([g]) => /Varón/.test(g)) && T("Creatinina sérica").t.r.some(([g]) => /Mujer/.test(g)), "diferencia por sexo y gestación donde corresponde");
/* unidades de uso en Perú */
const U = n => T(n).t.u;
ok(U("Glucosa en ayunas (plasma venoso)") === "mg/dL" && U("Creatinina sérica") === "mg/dL" && U("Urea") === "mg/dL" && U("Colesterol total") === "mg/dL" && U("Sodio") === "mEq/L" && U("Potasio") === "mEq/L" && U("Leucocitos (recuento total)") === "/mm³" && U("Plaquetas") === "/mm³" && U("Hemoglobina") === "g/dL", "unidades convencionales de uso en Perú en los análisis más frecuentes");
/* concordancia con el catálogo que usan los casos */
const cat = id => CAT.pruebas.find(t => t.id === id);
const par = [["hemoglobina", "Hemoglobina", "Varón", "M"], ["hemoglobina", "Hemoglobina", "Mujer", "F"], ["hematocrito", "Hematocrito", "Varón", "M"], ["hematocrito", "Hematocrito", "Mujer", "F"], ["glucosa", "Glucosa en ayunas (plasma venoso)", "Adulto, normal", "todos"], ["creatinina", "Creatinina sérica", "Varón adulto", "M"], ["creatinina", "Creatinina sérica", "Mujer adulta", "F"],
  ["ast", "Aspartato aminotransferasa", "Adulto", "todos"], ["alt", "Alanina aminotransferasa", "Adulto", "todos"], ["fosfatasa_alcalina", "Fosfatasa alcalina", "Adulto", "todos"], ["ggt", "Gamma glutamil transferasa", "Varón", "M"], ["ggt", "Gamma glutamil transferasa", "Mujer", "F"], ["albumina", "Albúmina", "Adulto", "todos"], ["calcio", "Calcio total", "Adulto", "todos"], ["magnesio", "Magnesio", "", "todos"], ["fosforo", "Fósforo", "Adulto", "todos"],
  ["sodio", "Sodio", "Adulto", "todos"], ["potasio", "Potasio", "Adulto", "todos"], ["cloro", "Cloro", "Adulto", "todos"], ["bicarbonato", "Bicarbonato", "", "todos"], ["urea", "Urea", "Adulto", "todos"], ["bilirrubina_total", "Bilirrubina total", "Niño y adulto", "todos"], ["lipasa", "Lipasa sérica", "", "todos"], ["ldh", "Lactato deshidrogenasa", "", "todos"],
  ["tsh", "Hormona estimulante de tiroides", "Adulto", "todos"], ["t4l", "Tiroxina libre", "", "todos"], ["ph", "pH arterial", "", "todos"], ["pco2", "Presión parcial de CO₂ arterial", "", "todos"], ["po2", "Presión parcial de O₂ arterial", "Nivel del mar", "todos"], ["lactato", "Lactato (sangre arterial o venosa)", "", "todos"], ["tp", "Tiempo de protrombina", "", "todos"], ["ttpa", "Tiempo de tromboplastina parcial activada", "", "todos"], ["fibrinogeno", "Fibrinógeno", "", "todos"], ["inr", "Razón normalizada internacional", "Sin anticoagulación", "todos"], ["procalcitonina", "Procalcitonina", "Sin infección bacteriana sistémica probable", "todos"]];
for (const [id, nom, grupo, sexo] of par) {
  const c = cat(id), iv = c && c.intervalos.find(i => i.sexo === sexo && (i.edad_min == null || i.edad_min >= 18) && !i.condicion), t = T(nom), fila = t && t.t.r.find(([g]) => g === grupo);
  const esperado = iv && iv.bajo != null && iv.alto != null ? [iv.bajo, iv.alto] : null, m = fila && /^(\d[\d ]*(?:\.\d+)?) – (\d[\d ]*(?:\.\d+)?)$/.exec(fila[1]);
  if (!esperado) { ok(!!fila || !!c, id + ": sin intervalo numérico comparable en el catálogo"); continue; }
  const k = id === "plaquetas" ? 1000 : id === "leucocitos" ? 1000 : 1, lo = m ? parseFloat(m[1].replace(/ /g, "")) : NaN, hi = m ? parseFloat(m[2].replace(/ /g, "")) : NaN;
  const menor = fila && /^< ([\d.]+)$/.exec(fila[1]);
  if (menor) { ok(esperado[0] === 0 && Math.abs(parseFloat(menor[1]) - esperado[1]) < 1e-9, id + ": la biblioteca (" + fila[1] + ") coincide con el catálogo (" + esperado.join(" – ") + ")"); continue; }
  ok(m && Math.abs(lo - esperado[0] * k) < 1e-9 && Math.abs(hi - esperado[1] * k) < 1e-9, id + ": la biblioteca (" + (fila && fila[1]) + ") coincide con el catálogo de los casos (" + esperado.join(" – ") + ")");
}
const pl = T("Plaquetas").t.r[0][1], le = T("Leucocitos (recuento total)").t.r.find(([g]) => g === "Adulto")[1];
ok(pl === "150 000 – 450 000" && cat("plaquetas").intervalos[0].bajo === 150 && cat("plaquetas").intervalos[0].alto === 450, "plaquetas: biblioteca y catálogo coinciden (150 – 450 ×10³/µL)"); ok(le === "4 500 – 11 000" && cat("leucocitos").intervalos[0].bajo === 4.5 && cat("leucocitos").intervalos[0].alto === 11, "leucocitos: biblioteca y catálogo coinciden");
/* examen completo de orina: todos los parámetros del catálogo de los casos existen */
const ORINA = ["orina_color", "orina_aspecto", "orina_densidad", "orina_ph", "orina_proteinas", "orina_glucosa", "orina_cetonas", "orina_bilirrubina", "orina_urobilinogeno", "orina_sangre", "orina_nitritos", "orina_esterasa", "orina_leucocitos", "orina_hematies", "orina_celulas_epiteliales", "orina_cilindros", "orina_cristales", "orina_bacterias", "orina_levaduras", "orina_mucus"];
ok(ORINA.every(id => !!cat(id)), "el catálogo de los casos tiene los 20 parámetros del examen completo de orina");
console.log(fallos ? "FALLARON " + fallos + " de " + total : "OK: " + total + " comprobaciones de la biblioteca de laboratorio"); process.exit(fallos ? 1 : 0);
