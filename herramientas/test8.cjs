const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const nuevos = JSON.parse(require('fs').readFileSync('nuevos8.json','utf8'));
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1400, height: 950 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('response', r => { if (r.status()>=400) errs.push(r.status()+' '+r.url()); });
  await p.goto('http://localhost:8766/index.html'); await p.waitForTimeout(800);
  const r = await p.evaluate(async () => {
    const files = ['cardiologia','neumologia','gastroenterologia','nefrologia','endocrinologia','infectologia','neurologia','hematologia','reumatologia','pediatria','ginecologia','cirugia','traumatologia','oftalmo_orl','psiquiatria','salud_publica','ciencias_basicas'];
    let total=0; const ids=new Set(); const bad=[];
    for (const f of files) { const j = await (await fetch('bancos/'+f+'.json',{cache:'no-store'})).json();
      for (const q of j.preguntas) { total++; if (ids.has(q.id)) bad.push('dup '+q.id); ids.add(q.id);
        if (!Array.isArray(q.opciones)||q.opciones.length!==5||q.opciones.some(o=>!o||!o.trim())) bad.push('ops '+q.id);
        if (!(q.correcta>=0&&q.correcta<5)) bad.push('corr '+q.id);
        if (q.clave_correcta && 'ABCDE'[q.correcta]!==q.clave_correcta) bad.push('clave '+q.id);
        if (!q.enunciado||!q.explicacion) bad.push('txt '+q.id); } }
    return {total, bad};
  });
  console.log(JSON.stringify(r));
  const want = new Set(nuevos.filter(n=>n.archivo==='pediatria').map(n=>n.id));
  await p.locator('#specs button[aria-label*="Pediatr"]').first().click(); await p.waitForTimeout(600);
  const seen=new Set(); let shot=false;
  for (let i=0;i<260;i++){
    await p.locator('#svOptions .opt').first().click(); await p.waitForTimeout(40);
    await p.click('#svAlgo'); await p.waitForTimeout(120);
    const sub = await p.textContent('#algoSub'); const m = sub.match(/[A-Z]+-\d{3}/);
    if (m){ seen.add(m[0]); if (!shot && want.has(m[0])) { await p.screenshot({path:'test8-'+m[0]+'.png'}); shot=true; console.log('nueva vista:',m[0],'|',(await p.textContent('#algoBody')).slice(0,90)); } }
    await p.keyboard.press('Escape'); await p.waitForTimeout(60);
    const nx = p.locator('#svNext'); if (await nx.isDisabled()) break; await nx.click(); await p.waitForTimeout(60);
  }
  const hits=[...seen].filter(x=>want.has(x));
  console.log('vistas',seen.size,'nuevas de pediatría vistas',hits.length,'de',want.size);
  console.log('errores',JSON.stringify(errs.slice(0,5)));
  await b.close();
})();
