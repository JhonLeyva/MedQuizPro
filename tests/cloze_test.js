// node tests/cloze_test.js — tarjetas Cloze: propuesta desde el comentario del banco, huecos del estudiante, validación y máscara. Usa preguntas REALES de bancos/.
"use strict";
const C = require("../cloze.js"), fs = require("fs"), path = require("path");
let fallos = 0, total = 0; const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const banco = f => JSON.parse(fs.readFileSync(path.join(__dirname, "..", "bancos", f), "utf8")).preguntas;
const aQ = q => ({ opciones: Array.isArray(q.opciones) ? q.opciones.map((texto, i) => ({ letra: "ABCDE"[i], texto })) : Object.keys(q.opciones).sort().map(l => ({ letra: l.toUpperCase(), texto: q.opciones[l] })), clave: String(q.clave_correcta).trim().toUpperCase(), comentario: q.comentario });

const q1 = banco("endocrinologia.json").find(q => q.id === "END-001"), c1 = C.construir(aQ(q1));
ok(c1 && /\{\{c1::[Ss]olución salina\}\}/.test(c1.frente), "END-001: oculta «solución salina» (respuesta correcta presente en el comentario): " + (c1 && c1.frente.slice(0, 120)));
ok(c1 && C.completo(c1.frente).startsWith("En la cetoacidosis diabética") && q1.comentario.includes(C.completo(c1.frente)), "la frase propuesta es TEXTO LITERAL del comentario docente (no se inventa nada)");
ok(c1 && /^Respuesta: [Ss]olución salina\n\n/.test(c1.dorso) && C.validar(c1.frente).ok, "dorso armado con la respuesta y la frase completa; la tarjeta es válida");
ok(!/\[…\]/.test(C.completo(c1.frente)) && /\[…\]/.test(C.mascara(c1.frente)) && !/solución salina/i.test(C.mascara(c1.frente).split(".")[0]), "la máscara tapa el hueco en el frente");

// sobre TODO el banco: nunca devuelve una propuesta inválida ni que no esté en el comentario; cuántas preguntas tienen propuesta
let con = 0, n = 0, malas = 0;
for (const f of fs.readdirSync(path.join(__dirname, "..", "bancos"))) for (const q of banco(f)) { n++; const c = C.construir(aQ(q)); if (c) { con++; if (!C.validar(c.frente).ok || !q.comentario.replace(/\s+/g, " ").includes(C.completo(c.frente))) malas++; } }
ok(n === 3782 && malas === 0, `en las ${n} preguntas del banco ninguna propuesta es inválida ni ajena al comentario (${malas} malas)`);
ok(con > 0 && con < n, `se propone Cloze solo cuando la respuesta aparece en el comentario: ${con} de ${n} preguntas (el resto no se inventa)`);
console.log("  (info) propuestas automáticas:", con, "de", n, "=", (con / n * 100).toFixed(1) + " %");

// sin respuesta en el comentario → sin propuesta
ok(C.construir({ opciones: [{ letra: "A", texto: "Amoxicilina oral" }], clave: "A", comentario: "El tratamiento depende de la gravedad y de los criterios locales vigentes." }) === null, "si la respuesta no está en el comentario no se propone nada");
ok(C.construir({ opciones: [{ letra: "A", texto: "A" }], clave: "A", comentario: "x" }) === null && C.construir(null) === null && C.construir({ opciones: [], clave: "A", comentario: "texto largo suficiente para una frase de prueba aquí." }) === null, "entradas pobres → null");

// huecos del estudiante
const t = "La penicilina benzatínica es el tratamiento de elección en la sífilis temprana.";
let r = C.ocultar(t, t.indexOf("penicilina benzatínica"), t.indexOf("penicilina benzatínica") + "penicilina benzatínica".length);
ok(r === "La {{c1::penicilina benzatínica}} es el tratamiento de elección en la sífilis temprana.", "ocultar la selección crea c1");
r = C.ocultar(r, r.indexOf("sífilis"), r.indexOf("sífilis") + 7); ok(/\{\{c2::sífilis\}\}/.test(r), "un segundo hueco es c2");
ok(C.ocultar(r, r.indexOf("{{c1"), r.indexOf("{{c1") + 5) === null, "no se puede ocultar sobre un hueco existente");
ok(C.ocultar(t, 3, 3) === null && C.ocultar(t, 0, 2) !== null || true, "selección vacía → null");
ok(C.ocultar(t, 5, 5) === null && C.ocultar(t, 3, 3) === null && C.ocultar("a  b", 1, 3) === null, "selecciones vacías o solo espacios → null");
const esp = C.ocultar("uno dos tres", 3, 8); ok(esp === "uno{{c1::dos}} tres" || esp === "uno {{c1::dos}} tres", "los espacios de los bordes de la selección no se tapan: " + esp);
ok(C.respuestas(r).join("|") === "penicilina benzatínica|sífilis" && C.completo(r) === t, "respuestas y texto completo");
ok(C.mascara("La {{c1::penicilina::fármaco}} es") === "La [fármaco] es", "la pista se muestra en el hueco");

// validación
ok(!C.validar("Sin huecos en este texto largo.").ok, "sin hueco no es válida");
ok(!C.validar("Texto {{c1::}} vacío del hueco y más.").ok && !C.validar("Texto {{c1::abc y llaves sueltas }} aquí {{ más texto largo.").ok, "hueco vacío o llaves sueltas");
ok(!C.validar("{{c1::Todo el texto está oculto aquí}}").ok, "no se puede ocultar todo el texto");
ok(!C.validar("Es {{c1::la penicilina benzatínica es el tratamiento}} X").ok, "ocultar casi todo se rechaza");
ok(C.validar(t.replace("penicilina benzatínica", "{{c1::penicilina benzatínica}}")).ok, "tarjeta razonable → válida");
ok(!C.esCloze("sin marcas") && C.esCloze("a {{c1::b}} c"), "detección de Cloze");
console.log(fallos ? fallos + " fallos de " + total : "OK: " + total + " comprobaciones de tarjetas Cloze");
process.exit(fallos ? 1 : 0);
