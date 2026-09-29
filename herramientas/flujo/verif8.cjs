const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8766/verificar-flujogramas.html');
  for (let i = 0; i < 120; i++) { await p.waitForTimeout(1000); const t = await p.textContent('body'); if (/revisados/i.test(t) && !/Revisando/i.test(t)) break; }
  const t = (await p.textContent('body')).replace(/\s+/g, ' ');
  console.log(t.slice(0, 500));
  console.log('errores JS:', errs);
  await b.close();
})();
