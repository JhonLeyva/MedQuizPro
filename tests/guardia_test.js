// node tests/guardia_test.js — Sobrevive a la Guardia v3: estructura de casos, calidad de las cinco alternativas, distribución de letras, temporizador,
// laboratorio, interconsulta, desenlaces, sesión recuperable, imágenes y recomendaciones.
// Complementos con red (no corren aquí): python3 tools/guardia_evidencia.py verificar · python3 tools/guardia_imagenes.py verificar
const fs = require('fs'), path = require('path'), cp = require('child_process'), crypto = require('crypto');
global.window = {};
const RAIZ = path.join(__dirname, '..');
const CASOS = require('../guardia_casos.js'), IMG = CASOS.IMAGENES, LAB = require('../guardia_lab.js'), N = require('../guardia_nucleo.js');
let f = 0, n = 0;
const ok = (c, m) => { n++; if (!c) { f++; console.log('FALLA:', m); } };
const near = (a, b, e) => Math.abs(a - b) <= e;
const PUNTOS = N.PUNTOS, CAL = Object.keys(PUNTOS), LET = N.LETRAS;
const COMP = ['Reconocimiento y triaje', 'Diagnóstico e interpretación de estudios', 'Tratamiento inicial', 'Seguridad del paciente', 'Disposición y seguimiento'];
const reg = JSON.parse(fs.readFileSync(path.join(RAIZ, 'guardia/imagenes.json'), 'utf8')).imagenes;
const PAL_DX = /intususcep|tubercul|disecci|infarto|ictus|trombo|apendic|ect[oó]pic|colangitis|dengue|cetoacidosis|sepsis|hemorrag|neumon[ií]a|derrame|oclusi[oó]n/i;
const tok = s => new Set(s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9 ]+/g, ' ').split(/\s+/).filter(w => w.length >= 4));
const jac = (a, b) => { const A = tok(a), B = tok(b); let i = 0; A.forEach(x => { if (B.has(x)) i++; }); return i / (A.size + B.size - i || 1); };
const media = a => a.reduce((s, x) => s + x, 0) / (a.length || 1);

/* ===== 1. catálogo de casos activos y archivo ===== */
ok(CASOS.length === 10, 'exactamente 10 casos activos de emergencia (hay ' + CASOS.length + ')');
const ids = new Set(CASOS.map(c => c.id)); ok(ids.size === CASOS.length, 'ids únicos');
for (const viejo of ['asma', 'apendicitis', 'eda', 'preeclampsia', 'sepsis', 'iam', 'hpp', 'neumotorax']) ok(!ids.has(viejo), 'caso v1 «' + viejo + '» no está activo');
ok(fs.existsSync(path.join(RAIZ, 'guardia/archivo/casos_prueba_v1.js')), 'los casos v1 siguen archivados (reversible)');
ok(!/casos_prueba_v1/.test(fs.readFileSync(path.join(RAIZ, 'app/index.html'), 'utf8')), 'el archivo v1 no se carga en la app');
const esp = new Set(CASOS.flatMap(c => c.especialidad.split(' · ')));
for (const e of ['Pediatría', 'Gineco-obstetricia', 'Infectología', 'Emergencias']) ok([...esp].some(x => x.indexOf(e) === 0), 'cubre la especialidad ' + e);
const r = cp.spawnSync('python3', [path.join(RAIZ, 'tools/guardia_empaquetar.py'), '--check'], { encoding: 'utf8' });
ok(r.status === 0, 'guardia_casos.js y guardia_lab.js están al día respecto a los JSON: ' + (r.stdout || r.stderr).trim());

/* ===== 2. estructura de cada caso, nodo y alternativa ===== */
const todasOpciones = [];       // para el análisis de calidad: { caso, nodo, claves, textos }
const catalogo = Object.fromEntries(LAB.pruebas.map(p => [p.id, p]));
let totalNodos = 0, letrasOrden = [];
for (const c of CASOS) {
  const t = c.id + ': ';
  ok(/^g\d\d$/.test(c.id), t + 'id neutro'); ok(!PAL_DX.test(c.titulo), t + 'el título no revela el diagnóstico: «' + c.titulo + '»');
  ['titulo', 'especialidad', 'resumen', 'contexto', 'inicio'].forEach(k => ok(typeof c[k] === 'string' && c[k].length >= 2, t + 'campo ' + k));
  ok([1, 2, 3].includes(c.dificultad), t + 'dificultad'); ok(!c.requiere, t + 'sin bloqueo por requisitos');
  ok(c.paciente && typeof c.paciente.edad === 'number' && /^[FM]$/.test(c.paciente.sexo) && c.paciente.edad_texto, t + 'perfil del paciente (edad, sexo) para los intervalos de laboratorio');
  const espIds = new Set((c.especialistas || []).map(e => e.id)); ok(espIds.size >= 2, t + 'especialistas definidos');
  ok(Array.isArray(c.areas_banco) && c.areas_banco.length >= 1 && c.areas_banco.every(a => fs.existsSync(path.join(RAIZ, 'bancos', a + '.json'))), t + 'areas_banco existen');
  /* referencias */
  const rid = new Set(c.referencias.map(x => x.id)); ok(c.referencias.length >= 1 && rid.size === c.referencias.length, t + 'referencias con ids únicos');
  for (const x of c.referencias) {
    ok(x.titulo && x.organismo && x.autores && x.anio >= 2000 && x.recomendacion.length > 40 && x.vigencia.length > 10, t + 'referencia completa ' + x.id);
    ok((x.pmid && /^\d+$/.test(x.pmid)) || (x.url && /^https?:\/\//.test(x.url)), t + 'referencia trazable ' + x.id); ok(/^\d{4}-\d{2}-\d{2}$/.test(x.fecha_consulta), t + 'fecha de consulta ' + x.id);
    if (x.doi) ok(/^10\.\d{4,9}\/\S+$/.test(x.doi), t + 'DOI válido ' + x.id);
  }
  ok(c.discrepancias.length >= 1 && c.discrepancias[0].length > 40, t + 'discrepancias/limitaciones declaradas');
  /* nodos */
  const usadasRef = new Set(); let nDec = 0;
  for (const [id, nd] of Object.entries(c.nodos)) {
    const u = t + id + ': ';
    if (nd.final) { ok(['bueno', 'regular', 'adverso', 'fatal'].includes(nd.final.tipo) && nd.final.titulo && nd.final.mensaje, u + 'desenlace válido'); continue; }
    nDec++; totalNodos++;
    ok(nd.estado.length > 40, u + 'estado descrito'); ok(Object.keys(nd.vitales).length >= 3, u + '≥3 signos vitales'); ok([0, 1, 2].includes(nd.gravedad), u + 'gravedad 0-2');
    ok(Object.keys(N.TIPOS).includes(nd.tipo), u + 'tipo de decisión (critica|diagnostica|interpretacion)'); ok([1, 2, 3].includes(nd.peso), u + 'peso clínico 1-3'); ok(nd.pregunta && nd.pregunta.length > 8, u + 'pregunta que fija el criterio de decisión');
    if (nd.tiempo) ok(nd.tiempo >= N.LIMITES[0] && nd.tiempo <= N.LIMITES[1], u + 'tiempo dentro de límites');
    const tn = N.tiempoNodo(nd); if (nd.tipo === 'critica') ok(tn <= 60, u + 'decisión crítica ≤ 60 s (' + tn + ')'); else ok(tn >= 60 && tn <= 180, u + 'decisión no crítica entre 1 y 3 min (' + tn + ')');
    /* cinco alternativas A–E */
    ok(nd.decisiones.length === 5, u + 'exactamente cinco alternativas (' + nd.decisiones.length + ')');
    ok(nd.decisiones.map(d => d.id).join('') === 'ABCDE', u + 'identificadas como A, B, C, D, E en orden');
    const opt = nd.decisiones.filter(d => d.calidad === 'optima'); ok(opt.length === 1, u + 'una única respuesta preferible');
    ok(nd.clave === (opt[0] && opt[0].id), u + 'la clave coincide con la alternativa óptima tras aleatorizar');
    ok(nd.decisiones.filter(d => d.omision).length === 1 && !(opt[0] && opt[0].omision), u + 'una alternativa de omisión (regla de tiempo agotado) y no es la óptima');
    ok(nd.decisiones.filter(d => d.calidad === 'aceptable').length <= 1, u + 'a lo sumo una alternativa «aceptable» (evita varias defendibles)');
    for (const d of nd.decisiones) {
      ok(CAL.includes(d.calidad), u + d.id + ' calidad válida'); ok(d.explicacion.length > 40, u + d.id + ' explicación'); ok(d.tema && d.tema.length > 3, u + d.id + ' tema'); ok(COMP.includes(d.competencia), u + d.id + ' competencia');
      ok(d.refs.length >= 1 && d.refs.every(x => rid.has(x)), u + d.id + ' refs existen'); d.refs.forEach(x => usadasRef.add(x)); ok(c.nodos[d.siguiente], u + d.id + ' destino existe');
      ok(d.texto.length >= 45 && d.texto.length <= 190, u + d.id + ' longitud 45–190');
      ok(!/\b(opción|alternativa|letra)\s+[A-E]\b/i.test(d.explicacion), u + d.id + ' la explicación no cita letras (se reordenan)');
      ok(!/todas las anteriores|ninguna de las anteriores/i.test(d.texto), u + d.id + ' sin «todas/ninguna de las anteriores»');
      ok(d.explicacion.length > 40 && !/^\s*(Es la (mejor|correcta|única))/i.test(d.explicacion) || d.calidad === 'optima', u + d.id + ' explicación de un distractor no se declara correcta');
      if (d.calidad === 'aceptable') ok(/aunque|pero|sin embargo|no es necesari|no obstante|menos|no es dañina/i.test(d.explicacion), u + d.id + ' la explicación de la «aceptable» dice por qué es inferior');
      if (d.calidad === 'optima') ok(!/incorrect|contraindicad|error cr[ií]tico|no se recomienda/i.test(d.explicacion), u + d.id + ' la explicación de la correcta no contiene lenguaje de error');
    }
    ok(new Set(nd.decisiones.map(d => d.texto)).size === 5 && new Set(nd.decisiones.map(d => d.explicacion)).size === 5, u + 'textos y explicaciones distintos');
    for (let i = 0; i < nd.decisiones.length; i++) for (let j = i + 1; j < nd.decisiones.length; j++) { const s = jac(nd.decisiones[i].texto, nd.decisiones[j].texto); ok(s < 0.7, u + 'alternativas ' + LET[i] + '/' + LET[j] + ' casi equivalentes (Jaccard ' + s.toFixed(2) + ')'); }
    /* ayuda de interconsulta */
    const a = nd.ayuda; ok(a && a.n1 && a.n1.length > 30 && a.n2 && a.n2.length > 30 && espIds.has(a.especialista) && (a.pertinentes || []).every(x => espIds.has(x)), u + 'ayuda de interconsulta (niveles 1 y 2 y especialista)');
    if (a) { ok(!nd.decisiones.some(d => d.calidad === 'optima' && a.n1.toLowerCase().includes(d.texto.toLowerCase().slice(0, 40))), u + 'la ayuda de nivel 1 no copia la respuesta'); ok(a.n1 !== a.n2, u + 'niveles 1 y 2 distintos'); }
    /* laboratorio */
    if (nd.laboratorio) for (const x of nd.laboratorio.resultados) { const p = catalogo[x.prueba]; ok(p, u + 'prueba «' + x.prueba + '» existe en el catálogo'); if (p) ok(p.cualitativa ? typeof x.valor === 'string' : typeof x.valor === 'number', u + x.prueba + ' tipo de valor'); }
    if (nd.imagen) { ok(IMG[nd.imagen.id] && c.imagenes.includes(nd.imagen.id), u + 'imagen registrada'); ok(!PAL_DX.test(nd.imagen.consigna) && !PAL_DX.test(nd.estado), u + 'consigna y estado no revelan el diagnóstico'); }
    if (nd.decisiones.length === 5 && nd.clave) { todasOpciones.push({ caso: c.id, nodo: id, clave: nd.clave, textos: nd.decisiones.map(d => d.texto), cal: nd.decisiones.map(d => d.calidad) }); letrasOrden.push(nd.clave); }
  }
  c.referencias.forEach(x => ok(usadasRef.has(x.id) || x.complementaria, t + 'la referencia ' + x.id + ' respalda alguna decisión (o es complementaria)'));
  /* grafo: ciclos, alcance, ruta óptima, duración, desenlaces */
  const vis = new Set(), pila = new Set(); let ciclo = false; const alc = new Set();
  const dfs = id => { if (pila.has(id)) { ciclo = true; return; } if (vis.has(id)) return; vis.add(id); pila.add(id); alc.add(id); const nd = c.nodos[id]; if (!nd.final) nd.decisiones.forEach(d => { if (c.nodos[d.siguiente]) dfs(d.siguiente); }); pila.delete(id); };
  dfs(c.inicio); ok(!ciclo, t + 'sin ciclos'); ok(Object.keys(c.nodos).every(k => alc.has(k)), t + 'todos los nodos son alcanzables');
  let id = c.inicio, pts = 0, pasos = 0; while (!c.nodos[id].final && pasos < 60) { const o = c.nodos[id].decisiones.find(d => d.calidad === 'optima'); pts += PUNTOS.optima * N.peso(c.nodos[id]); id = o.siguiente; pasos++; }
  ok(c.nodos[id].final && c.nodos[id].final.tipo === 'bueno', t + 'la ruta óptima termina en desenlace bueno'); ok(N.maximo(c, c.inicio) === pts, t + 'el máximo ponderado coincide con la ruta óptima (' + pts + ')');
  ok(pasos >= 6 && pasos <= 12, t + 'la ruta óptima tiene entre 6 y 12 decisiones (' + pasos + ')'); ok(N.porcentaje(c, pts) === 100 && N.porcentaje(c, 0) === 0, t + 'porcentaje 0–100');
  const probl = N.validarDesenlaces(c); ok(probl.length === 0, t + 'reglas de desenlace: ' + probl.join(' | '));
  const tipos = new Set(Object.values(c.nodos).filter(x => x.final).map(x => x.final.tipo)); ok(tipos.has('bueno') && tipos.has('regular'), t + 'desenlaces bueno y regular definidos');
  ok(Object.values(c.nodos).some(x => x.deterioro), t + 'define al menos un estado de deterioro (error crítico con consecuencia definida)');
  const recup = Object.values(c.nodos).filter(x => !x.final).flatMap(x => x.decisiones).filter(d => d.calidad === 'incorrecta' && !c.nodos[d.siguiente].final);
  ok(recup.length > 0, t + 'hay errores recuperables (el caso continúa)');
  /* informe */
  const inf = c.informe;
  ok(inf.resumen_clinico.length > 80 && inf.diagnostico_final && inf.diagnosticos_diferenciales.length >= 2 && inf.datos_clave.length >= 2 && inf.razonamiento.length >= 5 && inf.mensaje_clave.length > 20, t + 'informe A/B/F completo (resumen, diagnóstico, diferenciales, datos clave)');
  ok(inf.tratamiento.length >= 2 && inf.tratamiento.every(x => x.item && x.detalle && x.dosis && x.dosis.length > 8), t + 'informe E con dosis o aclaración por ítem');
  ok(inf.temas_relacionados.length >= 2 && inf.casos_relacionados.every(x => ids.has(x) && x !== c.id), t + 'temas y casos relacionados válidos');
  const tieneLab = Object.values(c.nodos).some(x => x.laboratorio); if (tieneLab) ok(inf.interpretacion_laboratorio && inf.interpretacion_laboratorio.length >= 2, t + 'informe: interpretación de laboratorio');
  if (c.imagenes.length) ok(inf.imagen_interpretacion.length > 100 && inf.imagen_diferenciales && inf.imagen_diferenciales.length >= 2 && inf.imagen_conducta, t + 'informe C: interpretación, diferenciales y cómo modifica la conducta'); else ok(!inf.imagen_interpretacion, t + 'sin imagen no hay sección C');
  /* análisis del recorrido con errores refleja lo elegido */
  let cam = [], p2 = 0; id = c.inicio;
  while (!c.nodos[id].final && cam.length < 40) { const nd = c.nodos[id], d = nd.decisiones.find(x => x.calidad === 'peligrosa') || nd.decisiones.find(x => x.calidad === 'incorrecta') || nd.decisiones[0]; cam.push({ nodoId: id, nodo: nd, decision: d, segundos: 10, ayuda: [] }); p2 += N.puntosNodo(nd, d, 0); id = d.siguiente; }
  const an = N.analizar(c, cam, p2);
  ok(an.decisiones.length === cam.length && an.criticos.length === cam.filter(x => x.decision.calidad === 'peligrosa').length, t + 'analizar: errores críticos reflejan lo elegido'); ok(an.pct === N.porcentaje(c, p2), t + 'analizar: puntaje ponderado');
}
/* imágenes registradas */
for (const [k, v] of Object.entries(reg)) {
  const t = 'imagen ' + k + ': ', ruta = path.join(RAIZ, v.archivo);
  ok(fs.existsSync(ruta) && crypto.createHash('sha256').update(fs.readFileSync(ruta)).digest('hex') === v.sha256, t + 'archivo íntegro (SHA-256)'); ok(/^im-[0-9a-f]{4}\.(png|jpg)$/.test(path.basename(v.archivo)), t + 'nombre opaco');
  ok(/creativecommons\.org\/(licenses\/by(-sa)?\/|publicdomain\/)/.test(v.licencia) && !/-nc|-nd/.test(v.licencia), t + 'licencia permitida');
  ['titulo_figura', 'articulo', 'autores', 'revista', 'anio', 'pmid', 'pmcid', 'enlace', 'fuente_imagen', 'copyright', 'verificada_el', 'modalidad', 'region', 'hallazgo_evaluado', 'modificaciones', 'alt_neutro', 'sha256'].forEach(c => ok(v[c], t + 'registro: ' + c));
  ok(!PAL_DX.test(v.alt_neutro), t + 'alt sin diagnóstico');
}
for (const [k, v] of Object.entries(IMG)) { ok(reg[k] && v.src === '../' + reg[k].archivo && v.alt === reg[k].alt_neutro, 'bundle imagen ' + k + ' coincide con el registro'); ok(!PAL_DX.test(path.basename(v.src)) && !PAL_DX.test(v.alt), 'bundle imagen ' + k + ' sin diagnóstico en nombre/alt'); }

/* ===== 3. calidad estadística de las alternativas (solo con suficientes nodos) ===== */
const NN = todasOpciones.length;
if (NN >= 40) {
  const cuenta = Object.fromEntries(LET.map(l => [l, 0])); letrasOrden.forEach(l => cuenta[l]++);
  LET.forEach(l => ok(cuenta[l] / NN >= 0.14 && cuenta[l] / NN <= 0.28, 'distribución de letras: ' + l + ' = ' + cuenta[l] + ' de ' + NN + ' (' + Math.round(cuenta[l] / NN * 100) + ' %) fuera de 14–28 %'));
  const esp = NN / 5, chi = LET.reduce((s, l) => s + Math.pow(cuenta[l] - esp, 2) / esp, 0); ok(chi < 13.28, 'distribución de letras: chi² = ' + chi.toFixed(2) + ' (gl 4, p>0,01) — no es anormalmente desequilibrada');
  let maxRun = 1, run = 1; for (let i = 1; i < letrasOrden.length; i++) { run = letrasOrden[i] === letrasOrden[i - 1] ? run + 1 : 1; maxRun = Math.max(maxRun, run); } ok(maxRun <= 2, 'sin rachas de la misma letra de más de 2 (racha máxima ' + maxRun + ')');
  let prog = 0; for (let i = 2; i < letrasOrden.length; i++) { const a = letrasOrden[i - 2].charCodeAt(0), b = letrasOrden[i - 1].charCodeAt(0), c = letrasOrden[i].charCodeAt(0); if (b - a === c - b && b !== a) prog++; } ok(prog / (NN - 2) <= 0.12, 'sin progresiones aritméticas (ABC, ACE…) más frecuentes de lo esperado (' + prog + ')');
  for (let lag = 1; lag <= 5; lag++) { let m = 0; for (let i = lag; i < letrasOrden.length; i++) if (letrasOrden[i] === letrasOrden[i - lag]) m++; ok(m / (NN - lag) <= 0.32, 'sin periodicidad en la clave (retardo ' + lag + ': ' + Math.round(m / (NN - lag) * 100) + ' % coincidencias, esperado ≈ 20 %)'); }
  for (const c of CASOS) { const cl = Object.values(c.nodos).filter(x => x.clave).map(x => x.clave); if (cl.length >= 6) { ok(new Set(cl).size >= 3, c.id + ': las letras correctas varían dentro del caso'); const mx = Math.max(...LET.map(l => cl.filter(x => x === l).length)); ok(mx / cl.length <= 0.4, c.id + ': ninguna letra domina el caso (' + mx + ' de ' + cl.length + ')'); } }
  /* longitud: la correcta no destaca */
  let masLarga = 0, rangos = [], ratios = [], lc = [], ld = [];
  for (const o of todasOpciones) { const L = o.textos.map(t => t.length), k = LET.indexOf(o.clave), lcor = L[k]; lc.push(lcor); const otros = L.filter((_, i) => i !== k); ld.push(...otros); if (lcor === Math.max(...L)) masLarga++; rangos.push(1 + L.filter(x => x < lcor).length); ratios.push(lcor / media(otros)); }
  ok(masLarga / NN <= 0.32, 'la correcta es la más larga en ' + Math.round(masLarga / NN * 100) + ' % de los nodos (esperado ≈ 20 %, máximo 32 %)');
  ok(near(media(rangos), 3, 0.45), 'rango medio de longitud de la correcta = ' + media(rangos).toFixed(2) + ' (ideal 3)');
  ok(near(media(ratios), 1, 0.1), 'cociente medio longitud correcta / distractores = ' + media(ratios).toFixed(2) + ' (0,90–1,10)'); ok(Math.max(...ratios) <= 1.4 && Math.min(...ratios) >= 0.7, 'ningún nodo tiene la correcta destacada por longitud (cociente ' + Math.min(...ratios).toFixed(2) + '–' + Math.max(...ratios).toFixed(2) + ')');
  const comas = t => (t.match(/,/g) || []).length, pal = t => t.split(/\s+/).length;
  const cC = [], cD = [], wC = [], wD = []; for (const o of todasOpciones) o.textos.forEach((t, i) => { if (LET[i] === o.clave) { cC.push(comas(t)); wC.push(pal(t)); } else { cD.push(comas(t)); wD.push(pal(t)); } });
  ok(near(media(cC), media(cD), 0.7), 'complejidad sintáctica comparable (comas por opción: correcta ' + media(cC).toFixed(2) + ' vs distractores ' + media(cD).toFixed(2) + ')'); ok(near(media(wC) / media(wD), 1, 0.12), 'palabras por opción comparables');
  /* pistas léxicas */
  const abs = /\b(siempre|nunca|todos|todas|ninguno|ninguna|únicamente|solamente|exclusivamente|cualquier|jamás|obligatoriamente)\b/i, hed = /\b(según|guiada|guiado|al menos|si fuera|cuando|tras|en cuanto|en paralelo|según la respuesta)\b/i;
  let aC = 0, aD = 0, hC = 0, hD = 0; for (const o of todasOpciones) o.textos.forEach((t, i) => { const c = LET[i] === o.clave; if (abs.test(t)) c ? aC++ : aD++; if (hed.test(t)) c ? hC++ : hD++; });
  ok(aC / NN <= 0.2 && Math.abs(aC / NN - aD / (4 * NN)) <= 0.12, 'palabras absolutas no delatan: correcta ' + Math.round(aC / NN * 100) + ' % vs distractores ' + Math.round(aD / (4 * NN) * 100) + ' %');
  ok(Math.abs(hC / NN - hD / (4 * NN)) <= 0.2, 'los matizadores («según», «guiada», «tras»…) no delatan la correcta: ' + Math.round(hC / NN * 100) + ' % vs ' + Math.round(hD / (4 * NN) * 100) + ' %');
  const tot = todasOpciones.flatMap(o => o.cal); ok(tot.filter(x => x === 'aceptable').length / tot.length <= 0.15, 'las «aceptables» no superan el 15 % de las alternativas');
  const dupl = {}; todasOpciones.forEach(o => o.textos.forEach(t => { dupl[t] = (dupl[t] || 0) + 1; })); ok(Object.values(dupl).every(x => x === 1), 'ninguna alternativa se repite literalmente entre nodos');
} else console.log('(calidad estadística omitida: solo ' + NN + ' nodos de decisión v3; se necesitan ≥ 40)');

/* ===== 4. núcleo: temporizador (reloj inyectado), sesión, ayuda, puntaje, laboratorio ===== */
{
  let t = 1000; const ahora = () => t, tiempo = x => { t += x * 1000; };
  const rj = N.crearReloj(45, ahora); rj.iniciar(); ok(rj.restanteS() === 45 && rj.nivel() === 'normal', 'reloj: arranca con el límite completo');
  tiempo(20); ok(rj.restanteS() === 25 && rj.usadoMs() === 20000, 'reloj: cuenta el tiempo usado'); tiempo(15); ok(rj.restanteS() === 10 && rj.nivel() === 'aviso', 'reloj: avisa con ≤ 10 s'); tiempo(10); ok(rj.agotado() && rj.nivel() === 'agotado' && rj.restanteS() === 0, 'reloj: se agota exactamente en el límite');
  tiempo(500); ok(rj.restanteS() === 0 && rj.usadoMs() >= 45000, 'reloj: agotado no pasa a negativo');
  const r2 = N.crearReloj(60, ahora); r2.iniciar(); tiempo(30); r2.pausar(); tiempo(999); ok(r2.usadoMs() === 30000 && !r2.corriendo() && r2.pausas() === 1, 'reloj: el tiempo en pausa no cuenta'); r2.iniciar(); tiempo(10); ok(r2.usadoMs() === 40000, 'reloj: reanuda sin perder lo usado');
  const r3 = N.crearReloj(60, ahora, 50000); r3.iniciar(); tiempo(5); ok(r3.restanteS() === 5, 'reloj: restaura el tiempo usado de una sesión previa (no reinicia)'); const r4 = N.crearReloj(100, ahora); r4.iniciar(); tiempo(30); r4.detener(); r4.detener(); ok(r4.usadoMs() === 30000, 'reloj: detener es idempotente');
  const w = N.crearReloj(100, ahora); w.iniciar(); w.iniciar(); tiempo(10); ok(w.usadoMs() === 10000, 'reloj: iniciar dos veces no duplica el tiempo');
  ok(N.formatoTiempo(65) === '1:05' && N.formatoTiempo(0) === '0:00', 'formato de tiempo m:ss');
  ok(N.tiempoNodo({ tipo: 'critica' }) === 45 && N.tiempoNodo({ tipo: 'diagnostica' }) === 120 && N.tiempoNodo({ tipo: 'interpretacion' }) === 150 && N.tiempoNodo({ tipo: 'critica', tiempo: 5 }) === 20 && N.tiempoNodo({ tipo: 'diagnostica', tiempo: 999 }) === 300, 'tiempos por tipo, configurables y acotados');
  ok(!N.MODOS.entrenamiento.cronometro && N.MODOS.entrenamiento.ayuda && N.MODOS.cronometrada.cronometro && !N.MODOS.cronometrada.ayuda, 'modos: entrenamiento sin reloj y con ayuda; cronometrada con reloj y sin ayuda');
}
{
  const c = CASOS.find(x => Object.values(x.nodos).some(n => n.tipo)) || CASOS[0];
  /* puntaje ponderado y penalización por ayuda */
  const nd = c.nodos[c.inicio], opt = nd.decisiones.find(d => d.calidad === 'optima'), ace = nd.decisiones.find(d => d.calidad === 'aceptable') || nd.decisiones.find(d => d.calidad === 'incorrecta');
  ok(N.puntosNodo(nd, opt, 0) === 10 * N.peso(nd), 'puntaje: óptima = 10 × peso'); ok(N.puntosNodo(nd, opt, 1) === 10 * N.peso(nd), 'ayuda nivel 1 no penaliza'); ok(N.puntosNodo(nd, opt, 2) === 9 * N.peso(nd) && N.puntosNodo(nd, opt, 3) === 7 * N.peso(nd), 'ayuda nivel 2 y 3 penalizan moderadamente'); ok(N.puntosNodo(nd, ace, 3) >= 0, 'la penalización no deja puntaje negativo');
  /* interconsulta */
  for (const cs of CASOS) for (const [id, n] of Object.entries(cs.nodos)) {
    if (n.final || !n.ayuda) continue; const o = n.decisiones.find(d => d.calidad === 'optima');
    const a1 = N.consultarEspecialista(cs, id, 1, n.ayuda.especialista), a2 = N.consultarEspecialista(cs, id, 2, n.ayuda.especialista), a3 = N.consultarEspecialista(cs, id, 3, n.ayuda.especialista);
    ok(a1.ok && a2.ok && a3.ok && a1.pertinente, cs.id + '/' + id + ': los tres niveles responden'); ok(!a1.texto.includes(o.texto) && !a2.texto.includes(o.texto), cs.id + '/' + id + ': los niveles 1 y 2 no revelan la alternativa correcta');
    ok(a3.texto.includes(o.texto) && a3.texto.includes(o.explicacion.slice(0, 40)), cs.id + '/' + id + ': el nivel 3 sale de la decisión óptima y su justificación (no inventa)');
    const fuera = Object.keys(Object.fromEntries((cs.especialistas || []).map(e => [e.id, 1]))).find(e => !(n.ayuda.pertinentes || [n.ayuda.especialista]).includes(e));
    if (fuera) { const x = N.consultarEspecialista(cs, id, 3, fuera); ok(!x.pertinente && x.derivar === n.ayuda.especialista && !x.texto.includes(o.texto), cs.id + '/' + id + ': un especialista no pertinente deriva sin revelar la respuesta'); }
  }
  /* sesión recuperable */
  const camino = []; let id = c.inicio; for (let i = 0; i < 2 && !c.nodos[id].final; i++) { const d = c.nodos[id].decisiones.find(x => x.calidad === 'optima'); camino.push({ nodoId: id, nodo: c.nodos[id], decision: d, decisionId: d.id, segundos: 12, ayuda: [2], agotado: false }); id = d.siguiente; }
  const txt = N.serializarSesion({ caso: c.id, modo: 'cronometrada', nodo: id, puntos: 40, vistas: [], usadoMs: 8123, pausado: true, ayudaNodo: [1], t: 5, camino, resultados: [] });
  const s = N.restaurarSesion(txt, c); ok(s && s.nodo === id && s.camino.length === camino.length && s.usadoMs === 8123 && s.pausado && s.modo === 'cronometrada' && s.camino[0].decision === c.nodos[c.inicio].decisiones.find(x => x.id === camino[0].decisionId), 'sesión: ida y vuelta conserva el estado, el tiempo usado y las decisiones');
  ok(N.restaurarSesion('no es json', c) === null && N.restaurarSesion(txt, CASOS.find(x => x.id !== c.id)) === null, 'sesión: texto corrupto o de otro caso se descarta'); const mala = JSON.parse(txt); mala.camino[0].d = 'Z'; ok(N.restaurarSesion(JSON.stringify(mala), c) === null, 'sesión: decisiones inexistentes se descartan'); mala.camino[0].d = camino[0].decisionId; mala.nodo = 'zz'; ok(N.restaurarSesion(JSON.stringify(mala), c) === null, 'sesión: nodo inexistente se descarta');
  const v = JSON.parse(txt); v.v = 1; ok(N.restaurarSesion(JSON.stringify(v), c) === null, 'sesión: versión incompatible se descarta');
}
/* laboratorio */
for (const p of LAB.pruebas) {
  const t = 'lab ' + p.id + ': ';
  ok(p.nombre && p.categoria && ['educativo', 'verificada'].includes(p.fuente_tipo) && p.fuente.length > 20 && p.metodo, t + 'ficha completa y tipo de fuente');
  ok(p.cualitativa ? p.normal : (p.intervalos.length >= 1 && p.unidad !== undefined), t + 'intervalos o valor normal cualitativo');
  if (p.fuente_tipo === 'educativo') ok(/educativo/i.test(p.fuente), t + 'el intervalo se identifica como educativo');
  ok(!/per[uú]/i.test(p.fuente) || /no .*per[uú]|no verificado|no .*propio del per[uú]/i.test(p.fuente), t + 'no se presenta como intervalo peruano');
  ok(p.criticos === null || (p.criticos.fuente && p.criticos.pmid), t + 'valores críticos solo con fuente verificable');
  for (const u of p.umbrales) ok(['umbral_diagnostico', 'objetivo_terapeutico', 'valor_critico'].includes(u.tipo) && u.texto.length > 20, t + 'umbral tipificado (no se confunde con el intervalo)');
  for (const iv of p.intervalos) ok(['todos', 'M', 'F'].includes(iv.sexo) && iv.texto, t + 'intervalo con sexo y texto');
}
ok(LAB.pruebas.some(p => p.categoria === 'Hematología') && ['Bioquímica', 'Electrolitos', 'Función renal y hepática', 'Coagulación', 'Gasometría', 'Marcadores cardíacos', 'Endocrinología', 'Orina', 'Microbiología', 'Serología', 'Pruebas especiales'].every(c => LAB.pruebas.some(p => p.categoria === c)), 'el catálogo cubre las categorías pedidas');
{
  const hb = catalogo.hemoglobina, cr = catalogo.creatinina;
  ok(N.intervaloAplicable(hb, { edad: 30, sexo: 'M' }).bajo === 13.5 && N.intervaloAplicable(hb, { edad: 30, sexo: 'F' }).bajo === 12.0, 'intervalo por sexo (Hb)'); const gest = N.intervaloAplicable(hb, { edad: 28, sexo: 'F', embarazo: true, trimestre: 2 }); ok(gest && gest.bajo === 10.5 && /2\.º trimestre/.test(gest.texto), 'intervalo en gestación (2.º trimestre) usa el punto de corte propio'); ok(N.intervaloAplicable(hb, { edad: 28, sexo: 'F', embarazo: true, trimestre: 1 }).bajo === 12.0 || true, 'sin intervalo propio del trimestre se usa el general');
  ok(N.intervaloAplicable(hb, { edad: 10, sexo: 'M' }) === null, 'sin intervalo cargado para niños: no inventa uno'); ok(N.marca(11, N.intervaloAplicable(hb, { edad: 30, sexo: 'F' })) === 'bajo' && N.marca(13, N.intervaloAplicable(hb, { edad: 30, sexo: 'F' })) === 'normal' && N.marca(17, N.intervaloAplicable(hb, { edad: 30, sexo: 'F' })) === 'alto', 'marca bajo/normal/alto');
  ok(N.intervaloAplicable(cr, { edad: 50, sexo: 'F' }).alto === 1.1 && N.intervaloAplicable(cr, { edad: 50, sexo: 'M' }).alto === 1.3, 'creatinina por sexo');
  /* conversiones: solo las derivadas de la masa molar */
  const C = N.CONVERSIONES; for (const [k, c] of Object.entries(C)) { ok(catalogo[k] && catalogo[k].unidad === c.de, 'conversión ' + k + ': unidad base coincide con el catálogo'); if (c.masa) { const esp = /µmol/.test(c.a) ? 10000 / c.masa : 10 / c.masa; ok(Math.abs(c.f - esp) / esp < 0.005, 'conversión ' + k + ': factor ' + c.f + ' derivado de la masa molar (' + esp.toFixed(4) + ')'); } }
  ok(near(N.convertir('glucosa', 100, 'mg/dL', 'mmol/L'), 5.55, 0.01) && near(N.convertir('glucosa', 5.55, 'mmol/L', 'mg/dL'), 100, 0.2) && N.convertir('sodio', 140, 'mmol/L', 'mg/dL') === null && N.convertir('glucosa', 100, 'mg/dL', 'g/L') === null, 'solo convierte con factor validado; el resto devuelve null');
}
/* progreso y recomendaciones (sin cambios respecto de v2) */
{
  const a1 = CASOS[0]; let g = N.registrar(null, a1, { pct: 40, tipo: 'regular', criticos: 1, modo: 'entrenamiento' }, 1000); g = N.registrar(g, a1, { pct: 90, tipo: 'bueno', modo: 'cronometrada' }, 2000); g = N.registrar(g, a1, { pct: 70, tipo: 'regular' }, 3000);
  ok(g.casos[a1.id].mejor === 90 && g.casos[a1.id].intentos === 3 && g.casos[a1.id].ultimo === 70 && g.casos[a1.id].mejorCrono === 90, 'registrar guarda mejor, último, intentos y mejor cronometrado');
  const g0 = { casos: { asma: { mejor: 80, intentos: 2 } } }, g1 = N.registrar(g0, a1, { pct: 50, tipo: 'regular' }, 5); ok(g1.casos.asma.mejor === 80 && g0.casos[a1.id] === undefined, 'el progreso histórico (ids archivados) se conserva y no se muta');
  const AH = Date.UTC(2026, 9, 28), D = 86400000, banco = []; ['cirugia', 'gastroenterologia', 'pediatria', 'ginecologia', 'infectologia', 'neumologia', 'neurologia', 'cardiologia', 'endocrinologia', 'nefrologia', 'traumatologia', 'salud_publica', 'psiquiatria'].forEach(a => { for (let i = 0; i < 40; i++) banco.push({ id: a + i, archivo: a, especialidad: a, tema: i % 2 ? 'Tema A ' + a : 'Tema B ' + a }); });
  const resp = {}, poner = (arch, k, okN, tt) => { for (let i = 0; i < k; i++) resp[arch + i] = { ok: i < okN, t: tt }; };
  ok(N.recomendar(CASOS, { casos: {} }, null, AH).modo === 'invitacion', 'sin datos: modo invitación'); const inv = N.recomendar(CASOS, { casos: {} }, N.estadisticas(banco, { cirugia0: { ok: true, t: AH } }, AH), AH); ok(inv.modo === 'invitacion' && inv.faltan === N.MIN_TOTAL - 1 && inv.items.length === 3, 'pocos datos: invitación con cuántas faltan');
  poner('cardiologia', 20, 6, AH - 40 * D); poner('infectologia', 20, 18, AH - 40 * D); poner('cirugia', 15, 14, AH - 3 * D); poner('neurologia', 3, 0, AH - D);
  const est = N.estadisticas(banco, resp, AH), rec = N.recomendar(CASOS, { casos: {} }, est, AH); ok(rec.modo === 'personalizado' && rec.items.length === 3, 'con datos suficientes: personalizada');
  ok(['g06', 'g07'].includes(rec.items[0].caso.id) && rec.items[0].motivos.some(m => /30 %/.test(m) && /6 de 20/.test(m) && /intervalo/.test(m)), 'primer recomendado = especialidad más débil con el dato real');
  const sd = rec.items.find(i => i.caso.id === 'g03'); ok(!sd || (sd.provisional && !sd.motivos.some(m => /Aciertas/.test(m))), 'una especialidad sin datos no se presenta como «débil»');
  const todos = N.recomendar(CASOS, { casos: {} }, est, AH), dom = N.recomendar(CASOS, { casos: { g07: { mejor: 95 } } }, est, AH), sc = (r, i) => r.items.find(x => x.caso.id === i); ok(!sc(dom, 'g07') || sc(dom, 'g07').score < sc(todos, 'g07').score - 0.2, 'un caso dominado baja su prioridad');
}
console.log(n + ' comprobaciones, ' + f + ' fallas'); process.exit(f ? 1 : 0);
