// node tests/guardia_test.js — valida que cada caso sea un grafo de decisiones coherente (sin ciclos, con desenlaces y fuentes)
global.window = {}; const CASOS = require('../guardia_casos.js'); let f = 0, n = 0;
const ok = (c, m) => { n++; if (!c) { f++; console.log('FALLA:', m); } };
const PUNTOS = { optima: 10, aceptable: 5, incorrecta: 0, peligrosa: 0 };
ok(CASOS.length >= 5, 'hay al menos 5 casos');
const ids = new Set(CASOS.map(c => c.id)); ok(ids.size === CASOS.length, 'ids únicos');
for (const c of CASOS) {
  const t = c.id + ': ';
  ok(c.fuentes && c.fuentes.length > 0, t + 'tiene fuentes');
  ok(c.nodos[c.inicio], t + 'nodo inicial existe');
  if (c.requiere) ok(ids.has(c.requiere.caso) && c.requiere.caso !== c.id, t + 'requisito válido');
  const vis = new Set(), pila = new Set(); let ciclo = false;
  const maximo = {};                                  // puntaje máximo desde cada nodo (camino óptimo)
  function dfs(id) {
    const nodo = c.nodos[id]; ok(!!nodo, t + 'nodo ' + id + ' existe'); if (!nodo) return 0;
    if (pila.has(id)) { ciclo = true; return 0; } if (maximo[id] !== undefined) return maximo[id];
    pila.add(id); vis.add(id);
    let mx = 0;
    if (nodo.final) { ok(['bueno', 'regular', 'adverso'].includes(nodo.final.tipo) && nodo.final.titulo && nodo.final.mensaje, t + id + ' final completo'); }
    else {
      ok(nodo.estado && nodo.estado.length > 40, t + id + ' tiene estado clínico');
      ok(nodo.vitales && Object.keys(nodo.vitales).length >= 3, t + id + ' tiene signos/datos');
      ok([0, 1, 2].includes(nodo.gravedad), t + id + ' gravedad válida');
      ok(nodo.decisiones.length >= 2, t + id + ' ≥2 decisiones');
      ok(nodo.decisiones.filter(d => d.calidad === 'optima').length === 1, t + id + ' exactamente una decisión óptima');
      const dids = new Set();
      for (const d of nodo.decisiones) {
        ok(PUNTOS[d.calidad] !== undefined, t + id + '/' + d.id + ' calidad válida'); ok(!dids.has(d.id), t + id + ' ids de decisión únicos'); dids.add(d.id);
        ok(d.explicacion && d.explicacion.length > 30, t + id + '/' + d.id + ' explicada'); ok(d.tema, t + id + '/' + d.id + ' con tema');
        mx = Math.max(mx, PUNTOS[d.calidad] + dfs(d.siguiente));
      }
    }
    pila.delete(id); maximo[id] = mx; return mx;
  }
  const max = dfs(c.inicio);
  ok(!ciclo, t + 'sin ciclos'); ok(max > 0, t + 'puntaje máximo > 0 (=' + max + ')');
  ok(Object.keys(c.nodos).every(k => vis.has(k)), t + 'todos los nodos son alcanzables');
  // la decisión óptima de cada nodo debe llevar al mejor desenlace posible desde ahí (nunca a uno "adverso")
  function mejorFinal(id) { const nd = c.nodos[id]; if (nd.final) return nd.final.tipo; return mejorFinal(nd.decisiones.find(d => d.calidad === 'optima').siguiente); }
  ok(mejorFinal(c.inicio) === 'bueno', t + 'seguir siempre lo óptimo termina en buen desenlace');
}
// motor
const E = require('../guardia.js');
const asma = CASOS.find(c => c.id === 'asma'), eda = CASOS.find(c => c.id === 'eda');
ok(E.maximo(asma, asma.inicio) === 30, 'asma: máximo 30 puntos (3 decisiones óptimas de 10)');
ok(E.porcentaje(asma, 30) === 100 && E.porcentaje(asma, 15) === 50 && E.porcentaje(asma, 0) === 0, 'porcentaje');
ok(E.desbloqueado(asma, { casos: {} }) === true, 'nivel 1 libre');
ok(E.desbloqueado(eda, { casos: {} }) === false, 'nivel 2 bloqueado sin requisito');
ok(E.desbloqueado(eda, { casos: { asma: { mejor: 59 } } }) === false && E.desbloqueado(eda, { casos: { asma: { mejor: 60 } } }) === true, 'umbral de desbloqueo = 60 %');
let g = E.registrar({ casos: {} }, asma, { pct: 50, tipo: 'regular' }, 1); g = E.registrar(g, asma, { pct: 30, tipo: 'adverso' }, 2);
ok(g.casos.asma.mejor === 50 && g.casos.asma.intentos === 2 && g.casos.asma.ultimo === 30, 'registrar conserva el mejor y cuenta intentos');
ok(JSON.stringify(E.registrar(g, asma, { pct: 10, tipo: 'x' })).length > 0 && g.casos.asma.intentos === 2, 'registrar no muta el original');
console.log(f ? f + ' de ' + n + ' pruebas fallaron' : 'OK: ' + n + ' pruebas pasaron'); process.exit(f ? 1 : 0);
