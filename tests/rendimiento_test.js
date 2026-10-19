// node tests/rendimiento_test.js
const R = require('../rendimiento.js'); let f = 0, n = 0;
const ok = (c, m) => { n++; if (!c) { f++; console.log('FALLA:', m); } };
const q = (id, a, t) => ({ id, archivo: a, especialidad: a.toUpperCase(), tema: t });
const pregs = []; for (let i = 0; i < 40; i++) pregs.push(q('A' + i, 'a', i % 2 ? 'T1' : 'T2')); for (let i = 0; i < 10; i++) pregs.push(q('B' + i, 'b', 'T3'));
const now = 1e12, d = 86400000;

// Wilson
let w = R.wilson(0, 0); ok(w.p === null && w.lo === 0 && w.hi === 1, 'sin datos: intervalo total');
w = R.wilson(8, 10); ok(w.lo > 0.4 && w.hi < 0.97 && w.lo < 0.8 && w.hi > 0.8, 'wilson 8/10 razonable');
ok(R.wilson(50, 100).hi - R.wilson(50, 100).lo < R.wilson(5, 10).hi - R.wilson(5, 10).lo, 'más datos → intervalo más estrecho');

// sin datos suficientes: NO hay estimación
const resp = {}; for (let i = 0; i < 20; i++) resp['A' + i] = { ok: i < 5, t: now - 20 * d };
let r = R.calcular(pregs, resp, [], now);
ok(!r.estimacion.suficiente && r.estimacion.faltan.length === 2 && r.estimacion.rango === undefined, 'sin datos suficientes no se estima');
ok(r.global.n === 20 && r.global.ok === 5 && r.global.pct === 25, 'global descriptivo real');
ok(r.areas[0].archivo === 'a', 'prioriza la especialidad débil, grande y sin practicar hace tiempo');
ok(r.areas.find(a => a.archivo === 'b').n === 0 && r.areas.find(a => a.archivo === 'b').motivos[0] === 'Aún no la has practicado', 'especialidad sin datos: lo dice');
ok(r.areas[0].motivos.some(m => /Hace 20 días/.test(m)), 'explica la antigüedad');
ok(r.areas[0].temas.length > 0 && r.areas[0].temas[0].falladas.length > 0, 'temas concretos con falladas');
ok(!/\bnota\b/i.test(JSON.stringify(r.estimacion)), 'no habla de nota');

// con datos suficientes
const resp2 = {}; for (let i = 0; i < 40; i++) resp2['A' + i] = { ok: i % 4 !== 0, t: now - d }; for (let i = 0; i < 10; i++) resp2['B' + i] = { ok: i % 2 === 0, t: now - d };
for (let i = 0; i < 60; i++) { /* repetir intentos no infla: respuestas guarda el último */ }
const ses = [{ tipo: 'simulacro', total: 30, respondidas: 30, correctas: 15, t: 1 }, { tipo: 'simulacro', total: 30, respondidas: 30, correctas: 21, t: 2 }, { tipo: 'estudio', total: 50, respondidas: 50, correctas: 50, t: 3 }];
r = R.calcular(pregs.concat(Array.from({ length: 60 }, (_, i) => q('C' + i, 'c', 'T4'))), Object.assign(resp2, Object.fromEntries(Array.from({ length: 60 }, (_, i) => ['C' + i, { ok: true, t: now }]))), ses, now);
ok(r.estimacion.suficiente && r.estimacion.rango[0] < r.estimacion.centro && r.estimacion.centro < r.estimacion.rango[1], 'estimación con intervalo');
ok(r.simulacros.length === 2, 'solo simulacros cuentan (no las sesiones de estudio)');
ok(r.estimacion.tendencia === 20, 'tendencia = mejora entre mitades (50 → 70)');
const corto = R.calcular(pregs, resp2, [{ tipo: 'simulacro', total: 5, respondidas: 5, correctas: 5, t: 1 }], now); ok(corto.simulacros.length === 0, 'simulacros muy cortos no cuentan');
r = R.calcular([], {}, [], now); ok(r.global.pct === null && r.plan.length === 0, 'vacío no revienta');
console.log(f ? f + ' de ' + n + ' pruebas fallaron' : 'OK: ' + n + ' pruebas pasaron'); process.exit(f ? 1 : 0);
