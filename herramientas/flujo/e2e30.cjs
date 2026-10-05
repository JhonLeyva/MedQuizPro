const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const ids = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8')).map(o => o[0]);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8767/index.html');
  await p.waitForTimeout(800);
  const r = await p.evaluate(async (ids) => {
    const files = ['cardiologia','neumologia','gastroenterologia','nefrologia','endocrinologia','infectologia','neurologia','hematologia','reumatologia','pediatria','ginecologia','cirugia','traumatologia','oftalmo_orl','psiquiatria','salud_publica','ciencias_basicas'];
    const bank = new Set();
    for (const f of files) { const j = await (await fetch('bancos/' + f + '.json', { cache: 'no-store' })).json(); (Array.isArray(j) ? j : j.preguntas || []).forEach(q => bank.add(q.id)); }
    const A = window.MQP_ALGORITMOS || {};
    const load = src => new Promise(res => { const i = new Image(); i.onload = () => res(i.naturalWidth); i.onerror = () => res(0); i.src = src; });
    const out = { total: Object.keys(A).length, sinBanco: [], sinEntrada: [], noCarga: [] };
    for (const id of ids) {
      if (!bank.has(id)) out.sinBanco.push(id);
      if (!A[id]) { out.sinEntrada.push(id); continue; }
      if (!(await load(A[id].imagen))) out.noCarga.push(id);
    }
    return out;
  }, ids);
  console.log(JSON.stringify(r));
  for (const [esp, target] of [['Pediatr', 'PED-160'], ['Gineco', 'GIN-155']]) {
    await p.goto('http://localhost:8767/index.html');
    await p.locator('#specs button[aria-label*="' + esp + '"]').first().click();
    await p.waitForTimeout(600);
    let found = false;
    for (let i = 0; i < 1500 && !found; i++) {
      await p.locator('#svOptions .opt').first().click();
      await p.waitForTimeout(80);
      await p.click('#svAlgo');
      await p.waitForTimeout(200);
      const sub = await p.textContent('#algoSub');
      if (sub.includes(target)) {
        found = true;
        await p.waitForTimeout(500);
        await p.locator('#algoModal').screenshot({ path: `/tmp/claude-0/-home-user-MedQuizPro/b4e61b17-1e2c-50ad-9a1b-a6f675ffa5de/scratchpad/e2e30-${target}.png` });
        const img = await p.$eval('#algoBody', el => { const i = el.querySelector('img'); return i ? [i.getAttribute('src'), i.naturalWidth] : el.textContent.slice(0, 80); });
        console.log(target, 'modal:', sub, '| img:', JSON.stringify(img));
      }
      await p.click('#algoClose'); await p.waitForTimeout(80);
      if (!found) await p.click('#svNext');
    }
    if (!found) console.log(target, 'NO ENCONTRADA');
  }
  console.log('errores JS:', errs);
  await b.close();
})();
