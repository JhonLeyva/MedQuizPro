const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const nuevos = JSON.parse(require('fs').readFileSync('nuevos26.json','utf8'));
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1300, height: 950 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('response', r => { if (r.status()>=400) errs.push(r.status()+' '+r.url()); });
  await p.goto('http://localhost:8790/index.html'); await p.waitForTimeout(800);
  const ids = nuevos.map(n=>n.id);
  const r = await p.evaluate(async (ids) => {
    const d = await MQP.cargarTodo();
    const all = d.preguntas; const byId = {}; all.forEach(q=>byId[q.id]=q);
    const bad=[]; const seen=new Set();
    for (const q of all){ if (seen.has(q.id)) bad.push('dup '+q.id); seen.add(q.id);
      if (!q.opciones.some(o=>o.letra===q.clave)) bad.push('clave '+q.id); }
    const enam = MQP.filtrar(all,{examen:'enam'});
    const enamIds = new Set(enam.map(q=>q.id));
    const faltan = ids.filter(i=>!byId[i]); const noEnam = ids.filter(i=>byId[i] && !enamIds.has(i));
    const cb = MQP.contarCategorias ? MQP.contarCategorias(all.filter(q=>q.archivo==='ciencias_basicas'),'ciencias_basicas') : null;
    const q4 = ids.filter(i=>byId[i] && byId[i].opciones.length!==4);
    return {total: all.length, fallos: d.fallos, enam: enam.length, faltan: faltan.length, noEnam, bad: bad.slice(0,5), q4: q4.length, cb};
  }, ids);
  console.log(JSON.stringify(r));
  // abrir práctica con una pregunta nueva y responder
  await p.evaluate((id)=>{ MQP.practica ? 0 : 0; }, ids[0]);
  const ok = await p.evaluate(async (id)=>{
    if (!window.MQP || !MQP.practica) return 'sin practica';
    MQP.practica.abrir({ titulo:'prueba', ids:[id], examen:'enam' }); return 'abierta';
  }, ids[0]);
  await p.waitForTimeout(800);
  console.log('practica', ok);
  const txt = await p.evaluate(()=>{ const e=document.querySelector('[data-mqp-practica]'); return e? e.innerText.slice(0,400):''; });
  console.log(txt.replace(/\n+/g,' | '));
  const opt = p.locator('[data-mqp-practica] .opt').first();
  if (await opt.count()) { await opt.click(); await p.waitForTimeout(300);
    const fb = await p.evaluate(()=>{ const e=document.querySelector('[data-mqp-practica]'); return e.innerText; });
    console.log('tras responder:', fb.includes(nuevos[0].comentario.slice(0,40)) ? 'comentario visible' : fb.slice(0,300)); }
  await p.screenshot({path:'test26.png'});
  console.log('errores', JSON.stringify(errs.slice(0,5)));
  await b.close();
})();
