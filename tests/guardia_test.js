// node tests/guardia_test.js — valida los 10 casos piloto (v2): grafo de decisiones, esquema, referencias, imágenes, informe, motor y recomendaciones.
// Complementos que requieren red (no corren aquí): python3 tools/guardia_evidencia.py verificar · python3 tools/guardia_imagenes.py verificar
const fs = require('fs'), path = require('path'), cp = require('child_process');
global.window = {};
const RAIZ = path.join(__dirname, '..');
const CASOS = require('../guardia_casos.js'), IMG = CASOS.IMAGENES, G = require('../guardia.js');
let f = 0, n = 0;
const ok = (c, m) => { n++; if (!c) { f++; console.log('FALLA:', m); } };
const reg = JSON.parse(fs.readFileSync(path.join(RAIZ, 'guardia/imagenes.json'), 'utf8')).imagenes;
const PUNTOS = G.PUNTOS, CAL = Object.keys(PUNTOS);
const COMP = ['Reconocimiento y triaje', 'Diagnóstico e interpretación de estudios', 'Tratamiento inicial', 'Seguridad del paciente', 'Disposición y seguimiento'];

/* ---- el módulo muestra exactamente 10 casos activos; los de prueba v1 están archivados y no se cargan ---- */
ok(CASOS.length === 10, 'exactamente 10 casos activos (hay ' + CASOS.length + ')');
const ids = new Set(CASOS.map(c => c.id)); ok(ids.size === CASOS.length, 'ids únicos');
for (const viejo of ['asma', 'apendicitis', 'eda', 'preeclampsia', 'sepsis', 'iam', 'hpp', 'neumotorax']) ok(!ids.has(viejo), 'caso v1 «' + viejo + '» no está activo');
ok(fs.existsSync(path.join(RAIZ, 'guardia/archivo/casos_prueba_v1.js')), 'los casos v1 siguen archivados (reversible)');
ok(!/casos_prueba_v1/.test(fs.readFileSync(path.join(RAIZ, 'app/index.html'), 'utf8')), 'el archivo v1 no se carga en la app');
ok(!fs.existsSync(path.join(RAIZ, 'guardia_casos_v1.js')), 'sin copia v1 junto al código');
const esp = new Set(CASOS.flatMap(c => c.especialidad.split(' · ')));
for (const e of ['Pediatría', 'Gineco-obstetricia', 'Infectología', 'Emergencias']) ok([...esp].some(x => x.indexOf(e) === 0), 'cubre la especialidad ' + e);
ok([...esp].some(x => /Cirugía/.test(x)) && [...esp].some(x => /Medicina interna/.test(x)), 'cubre cirugía y medicina interna');

/* ---- el artefacto generado coincide con los JSON fuente ---- */
const r = cp.spawnSync('python3', [path.join(RAIZ, 'tools/guardia_empaquetar.py'), '--check'], { encoding: 'utf8' });
ok(r.status === 0, 'guardia_casos.js está al día respecto a guardia/casos/*.json: ' + (r.stdout || r.stderr).trim());

const PALABRAS_DX = /intususcep|tubercul|disecci|infarto|ictus|trombo|apendic|ect[oó]pic|colangitis|dengue|cetoacidosis|sepsis|hemorrag|neumon[ií]a|derrame|oclusi[oó]n/i;
const totalImgUsadas = new Set();
for (const c of CASOS) {
  const t = c.id + ': ';
  ok(/^g\d\d$/.test(c.id), t + 'id neutro (no revela el diagnóstico)');
  ['titulo', 'especialidad', 'resumen', 'contexto'].forEach(k => ok(typeof c[k] === 'string' && c[k].length > 5, t + 'campo ' + k)); ok(typeof c.inicio === 'string', t + 'campo inicio');
  ok([1, 2, 3].includes(c.dificultad), t + 'dificultad 1-3'); ok(!c.requiere, t + 'sin bloqueo por requisitos');
  ok(Array.isArray(c.areas_banco) && c.areas_banco.length >= 1 && c.areas_banco.every(a => fs.existsSync(path.join(RAIZ, 'bancos', a + '.json'))), t + 'areas_banco existen en el banco');
  ok(!PALABRAS_DX.test(c.titulo), t + 'el título no revela el diagnóstico: «' + c.titulo + '»');
  /* referencias: cada una trazable (PMID, o url + fecha) con recomendación, vigencia y fecha de consulta */
  ok(c.referencias.length >= 1, t + 'tiene referencias'); const rid = new Set(c.referencias.map(x => x.id)); ok(rid.size === c.referencias.length, t + 'ids de referencia únicos');
  for (const x of c.referencias) {
    ok(x.titulo && x.organismo && x.autores && x.anio >= 2000 && x.recomendacion.length > 40 && x.vigencia.length > 10, t + 'referencia completa ' + x.id);
    ok((x.pmid && /^\d+$/.test(x.pmid)) || (x.url && /^https?:\/\//.test(x.url) && x.fecha_consulta), t + 'referencia trazable ' + x.id);
    ok(/^\d{4}-\d{2}-\d{2}$/.test(x.fecha_consulta), t + 'fecha de consulta ' + x.id);
    if (x.doi) ok(/^10\.\d{4,9}\/\S+$/.test(x.doi), t + 'DOI con formato válido ' + x.id);
  }
  ok(Array.isArray(c.discrepancias) && c.discrepancias.length >= 1 && c.discrepancias[0].length > 40, t + 'discrepancias/limitaciones declaradas');
  /* grafo */
  ok(c.nodos[c.inicio], t + 'nodo inicial existe');
  const vis = new Set(), pila = new Set(); let ciclo = false, alc = new Set();
  const dfs = id => { if (pila.has(id)) { ciclo = true; return; } if (vis.has(id)) return; vis.add(id); pila.add(id); alc.add(id); const nd = c.nodos[id]; if (!nd.final) nd.decisiones.forEach(d => { ok(c.nodos[d.siguiente], t + id + ' → destino «' + d.siguiente + '» existe'); if (c.nodos[d.siguiente]) dfs(d.siguiente); }); pila.delete(id); };
  dfs(c.inicio); ok(!ciclo, t + 'sin ciclos'); ok(Object.keys(c.nodos).every(k => alc.has(k)), t + 'todos los nodos son alcanzables');
  const usadasRef = new Set();
  for (const [id, nd] of Object.entries(c.nodos)) {
    const u = t + id + ': ';
    if (nd.final) { ok(['bueno', 'regular', 'adverso'].includes(nd.final.tipo) && nd.final.titulo && nd.final.mensaje, u + 'desenlace válido'); continue; }
    ok(nd.estado.length > 40, u + 'estado descrito'); ok(Object.keys(nd.vitales).length >= 3, u + '≥3 signos vitales'); ok([0, 1, 2].includes(nd.gravedad), u + 'gravedad 0-2');
    ok(nd.decisiones.length >= 2 && nd.decisiones.length <= 5, u + '2-5 decisiones'); ok(new Set(nd.decisiones.map(d => d.id)).size === nd.decisiones.length, u + 'ids de decisión únicos');
    ok(nd.decisiones.filter(d => d.calidad === 'optima').length === 1, u + 'exactamente una óptima');
    for (const d of nd.decisiones) {
      ok(CAL.includes(d.calidad), u + 'calidad válida'); ok(d.explicacion.length > 30, u + d.id + ' explicación'); ok(d.tema && d.tema.length > 3, u + d.id + ' tema'); ok(COMP.includes(d.competencia), u + d.id + ' competencia válida');
      ok(d.refs.length >= 1 && d.refs.every(x => rid.has(x)), u + d.id + ' refs existen en el caso'); d.refs.forEach(x => usadasRef.add(x));
    }
    if (nd.imagen) {
      ok(IMG[nd.imagen.id] && c.imagenes.includes(nd.imagen.id), u + 'imagen declarada y registrada'); ok(!PALABRAS_DX.test(nd.imagen.consigna), u + 'la consigna de la imagen no revela el diagnóstico');
      /* la imagen se muestra ANTES de las opciones y el nodo no puede revelar el diagnóstico en su estado */
      ok(!PALABRAS_DX.test(nd.estado), u + 'el estado del nodo con imagen no revela el diagnóstico');
    }
  }
  c.referencias.forEach(x => ok(usadasRef.has(x.id) || x.complementaria, t + 'la referencia ' + x.id + ' respalda alguna decisión (o está marcada como complementaria)'));
  /* camino óptimo termina bien; cada decisión peligrosa lleva a deterioro o desenlace malo, y los errores no llevan automáticamente a un desenlace grave */
  let id = c.inicio, pts = 0, pasos = 0; while (!c.nodos[id].final && pasos++ < 50) { const o = c.nodos[id].decisiones.find(d => d.calidad === 'optima'); pts += PUNTOS.optima; id = o.siguiente; }
  ok(c.nodos[id].final && c.nodos[id].final.tipo === 'bueno', t + 'el camino óptimo termina en desenlace bueno'); ok(G.maximo(c, c.inicio) === pts, t + 'el máximo calculado coincide con el camino óptimo (' + pts + ')');
  ok(G.porcentaje(c, pts) === 100 && G.porcentaje(c, 0) === 0, t + 'porcentaje 0-100');
  const mal = Object.values(c.nodos).filter(x => !x.final).flatMap(x => x.decisiones).filter(d => d.calidad === 'incorrecta' && !c.nodos[d.siguiente].final);
  ok(mal.length > 0, t + 'hay errores «incorrectos» que no provocan de inmediato una complicación grave (tienen continuación)');
  /* informe */
  const inf = c.informe;
  ok(inf.resumen_clinico.length > 80 && inf.razonamiento.length >= 4 && inf.mensaje_clave.length > 20, t + 'informe A/B/F completo');
  ok(inf.tratamiento.length >= 2 && inf.tratamiento.every(x => x.item && x.detalle && x.dosis && x.dosis.length > 8), t + 'informe E con dosis o aclaración por ítem');
  ok(inf.temas_relacionados.length >= 2 && inf.casos_relacionados.every(x => ids.has(x) && x !== c.id), t + 'temas y casos relacionados válidos');
  if (c.imagenes.length) ok(inf.imagen_interpretacion && inf.imagen_interpretacion.length > 100, t + 'informe C con interpretación de imagen'); else ok(!inf.imagen_interpretacion, t + 'sin imagen: no hay sección C');
  /* un recorrido con errores produce un análisis coherente con lo que realmente eligió el alumno */
  let cam = [], p2 = 0; id = c.inicio;
  while (!c.nodos[id].final) { const nd = c.nodos[id], d = nd.decisiones.find(x => x.calidad === 'peligrosa') || nd.decisiones.find(x => x.calidad === 'incorrecta') || nd.decisiones[0]; cam.push({ nodo: nd, decision: d }); p2 += PUNTOS[d.calidad]; id = d.siguiente; if (cam.length > 40) break; }
  const an = G.analizar(c, cam, p2);
  ok(an.decisiones.length === cam.length && an.criticos.length === cam.filter(x => x.decision.calidad === 'peligrosa').length, t + 'analizar: errores críticos reflejan lo elegido');
  ok(an.decisiones.every((x, i) => x.elegida === cam[i].decision && x.optima.calidad === 'optima'), t + 'analizar: tu respuesta y la preferible');
  ok(an.competencias.every(x => x.pct >= 0 && x.pct <= 100), t + 'competencias 0-100');
  ok(an.pct === G.porcentaje(c, p2), t + 'analizar: puntaje');
  c.imagenes.forEach(i => totalImgUsadas.add(i));
}

/* ---- imágenes: registro completo, archivo íntegro, licencia permitida, sin diagnóstico en nombre ni alt ---- */
const crypto = require('crypto');
ok(totalImgUsadas.size >= 4, 'al menos 4 imágenes reales usadas');
for (const [k, v] of Object.entries(reg)) {
  const t = 'imagen ' + k + ': ', ruta = path.join(RAIZ, v.archivo);
  ok(fs.existsSync(ruta) && crypto.createHash('sha256').update(fs.readFileSync(ruta)).digest('hex') === v.sha256, t + 'archivo íntegro (SHA-256)');
  ok(/^im-[0-9a-f]{4}\.(png|jpg)$/.test(path.basename(v.archivo)), t + 'nombre de archivo opaco (sin diagnóstico)');
  ok(/creativecommons\.org\/(licenses\/by(-sa)?\/|publicdomain\/)/.test(v.licencia) && !/-nc|-nd/.test(v.licencia), t + 'licencia permitida (CC BY/BY-SA/CC0, sin NC/ND)');
  ['titulo_figura', 'articulo', 'autores', 'revista', 'anio', 'pmid', 'pmcid', 'enlace', 'fuente_imagen', 'copyright', 'verificada_el', 'modalidad', 'region', 'hallazgo_evaluado', 'modificaciones', 'alt_neutro', 'sha256'].forEach(c => ok(v[c], t + 'registro: ' + c));
  ok(!PALABRAS_DX.test(v.alt_neutro), t + 'alt sin diagnóstico: «' + v.alt_neutro + '»'); ok(v.ancho > 0 && v.original && v.original.ancho > 0, t + 'dimensiones registradas');
}
for (const [k, v] of Object.entries(IMG)) { ok(reg[k] && v.src === '../' + reg[k].archivo && v.alt === reg[k].alt_neutro, 'bundle imagen ' + k + ' coincide con el registro'); ok(!PALABRAS_DX.test(path.basename(v.src)) && !PALABRAS_DX.test(v.alt), 'bundle imagen ' + k + ' sin diagnóstico en nombre/alt'); }
ok(Object.keys(IMG).every(k => totalImgUsadas.has(k)), 'el bundle no incluye imágenes sin usar');

/* ---- motor ---- */
const a1 = CASOS[0];
let g = G.registrar(null, a1, { pct: 40, tipo: 'regular', criticos: 1 }, 1000); g = G.registrar(g, a1, { pct: 90, tipo: 'bueno' }, 2000); g = G.registrar(g, a1, { pct: 70, tipo: 'regular' }, 3000);
ok(g.casos[a1.id].mejor === 90 && g.casos[a1.id].intentos === 3 && g.casos[a1.id].ultimo === 70, 'registrar guarda el mejor puntaje, el último y los intentos');
const g0 = { casos: { asma: { mejor: 80, intentos: 2 } } }, g1 = G.registrar(g0, a1, { pct: 50, tipo: 'regular' }, 5);
ok(g1.casos.asma.mejor === 80 && g1.casos.asma.intentos === 2 && g1.casos[a1.id].mejor === 50 && g0.casos[a1.id] === undefined, 'el progreso histórico (ids archivados) se conserva y no se muta la entrada');
ok(G.desbloqueado(a1, null) && G.desbloqueado(CASOS[9], { casos: {} }), 'ningún caso está bloqueado');

/* ---- recomendaciones ---- */
const AH = Date.UTC(2026, 9, 28), D = 86400000;
const banco = []; ['cirugia', 'gastroenterologia', 'pediatria', 'ginecologia', 'infectologia', 'neumologia', 'neurologia', 'cardiologia', 'endocrinologia', 'nefrologia', 'traumatologia', 'salud_publica', 'psiquiatria'].forEach(a => { for (let i = 0; i < 40; i++) banco.push({ id: a + i, archivo: a, especialidad: a, tema: i % 2 ? 'Tema A ' + a : 'Tema B ' + a }); });
const resp = {}; const poner = (arch, k, okN, t) => { for (let i = 0; i < k; i++) resp[arch + i] = { ok: i < okN, t }; };
ok(G.recomendar(CASOS, { casos: {} }, null, AH).modo === 'invitacion', 'sin datos: modo invitación (no inventa recomendaciones)');
const inv = G.recomendar(CASOS, { casos: {} }, G.estadisticas(banco, { cirugia0: { ok: true, t: AH } }, AH), AH);
ok(inv.modo === 'invitacion' && inv.faltan === G.MIN_TOTAL - 1 && inv.items.length === 3 && inv.items.every(i => i.provisional), 'pocos datos: invitación con cuántas respuestas faltan');
poner('cardiologia', 20, 6, AH - 40 * D); poner('infectologia', 20, 18, AH - 40 * D); poner('cirugia', 15, 14, AH - 3 * D); poner('neurologia', 3, 0, AH - D);
const est = G.estadisticas(banco, resp, AH), rec = G.recomendar(CASOS, { casos: {} }, est, AH);
ok(rec.modo === 'personalizado' && rec.items.length === 3, 'con datos suficientes: recomendación personalizada de 3 casos');
ok(['g06', 'g07'].includes(rec.items[0].caso.id), 'el primer recomendado corresponde a la especialidad más débil (cardiología 30 %): ' + rec.items[0].caso.id);
ok(rec.items[0].motivos.some(m => /30 %/.test(m) && /6 de 20/.test(m) && /intervalo/.test(m)), 'el motivo muestra el dato real y su intervalo');
const sd = rec.items.find(i => i.caso.id === 'g03'); ok(!sd || (sd.provisional && !sd.motivos.some(m => /Aciertas/.test(m))), 'una especialidad sin datos no se presenta como «débil»: queda provisional y sin cifras inventadas');
const est2 = G.estadisticas(banco, resp, AH); ok(est2.areas.cardiologia.n === 20 && est2.areas.neurologia.n === 3, 'estadísticas por especialidad correctas');
const dom = G.recomendar(CASOS, { casos: { g07: { mejor: 95 }, g06: { mejor: 90 } } }, est, AH);
const sc = (r, id) => r.items.find(i => i.caso.id === id); const todos = G.recomendar(CASOS, { casos: {} }, est, AH), todosDom = G.recomendar(CASOS, { casos: { g07: { mejor: 95 } } }, est, AH); ok(!sc(todosDom, 'g07') || sc(todosDom, 'g07').score < sc(todos, 'g07').score - 0.2, 'un caso ya dominado baja claramente su prioridad');
/* tendencia: bien hace 40 días, mal en los últimos 14 */
const r2 = {}; for (let i = 0; i < 12; i++) r2['endocrinologia' + i] = { ok: true, t: AH - 40 * D }; for (let i = 12; i < 24; i++) r2['endocrinologia' + i] = { ok: i < 14, t: AH - 2 * D };
for (let i = 0; i < 20; i++) r2['pediatria' + i] = { ok: i < 18, t: AH - D };
const rt = G.recomendar(CASOS, { casos: {} }, G.estadisticas(banco, r2, AH), AH);
ok(rt.items[0].caso.id === 'g09' && rt.items[0].motivos.some(m => /reciente/.test(m)), 'detecta que el rendimiento reciente cayó frente al histórico');
const prov = G.recomendar(CASOS, { casos: {} }, G.estadisticas(banco, (() => { const x = {}; for (let i = 0; i < 31; i++) x['psiquiatria' + (i % 40)] = { ok: true, t: AH }; return x; })(), AH), AH);
ok(prov.modo === 'provisional' || prov.modo === 'invitacion', 'si ningún área de los casos tiene datos suficientes, la recomendación es provisional');

console.log(n + ' comprobaciones, ' + f + ' fallas'); process.exit(f ? 1 : 0);
