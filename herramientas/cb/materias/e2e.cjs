const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const errs = [];
  const shot = process.argv[2];
  for (const vp of [{ width: 1280, height: 900 }, { width: 390, height: 800 }]) {
    const p = await b.newPage({ viewport: vp });
    p.on('pageerror', e => errs.push('pageerror ' + e.message));
    p.on('response', r => { if (r.status() >= 400) errs.push('HTTP ' + r.status() + ' ' + r.url()); });
    // web pública
    await p.goto('http://localhost:8771/index.html'); await p.evaluate(() => document.getElementById('bankExplorer').scrollIntoView());
    await p.waitForFunction(() => { const s = document.querySelector('#specs .spec__materia-select'); return s && s.options.length === 10 && /\(\d+\)/.test(s.options[1].textContent); }, null, { timeout: 20000 });
    const opts = await p.$$eval('#specs .spec__materia-select option', o => o.map(x => x.textContent + (x.disabled ? ' [off]' : '')));
    console.log(vp.width, 'opciones web:', opts.join(' | '));
    const card = p.locator('#specs .spec', { has: p.locator('.spec__materia-select') });
    await card.scrollIntoViewIfNeeded();
    await card.locator('select').selectOption('Anatomía');
    if (vp.width === 1280) await card.screenshot({ path: shot + '_card.png' });
    else await card.screenshot({ path: shot + '_card_movil.png' });
    // el select sigue en Anatomía (no disparó el botón)
    const vis = await p.evaluate(() => { const v = document.querySelector('#svTitle'); return v && v.offsetParent !== null; });
    console.log('sesión abierta tras elegir materia (debe ser false):', vis);
    await card.locator('.spec__cta').click();
    await p.waitForFunction(() => /Pregunta 1 de/.test((document.getElementById('svCounter') || {}).textContent || ''), null, { timeout: 10000 });
    const info = await p.evaluate(() => ({ t: svTitle.textContent, c: svCounter.textContent, tema: svTema.textContent }));
    console.log('sesión web:', JSON.stringify(info));
    await p.close();
  }
  // plataforma
  const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  p.on('pageerror', e => errs.push('app pageerror ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push('app console ' + m.text()); });
  await p.goto('http://localhost:8771/app/index.html#/examenes/enam');
  await p.waitForSelector('[data-area-grid] .spec__materia-select', { timeout: 20000 });
  await p.waitForFunction(() => /\(\d+\)/.test(document.querySelector('[data-area-grid] .spec__materia-select').options[1].textContent));
  const c2 = p.locator('[data-area-grid] .spec', { has: p.locator('.spec__materia-select') });
  await c2.locator('select').selectOption('Microbiología e Inmunología');
  await c2.locator('.spec__cta').click();
  await p.waitForFunction(() => /Pregunta 1 de/.test((document.getElementById('svCounter') || {}).textContent || ''), null, { timeout: 10000 });
  console.log('sesión app:', await p.evaluate(() => svTitle.textContent + ' | ' + svCounter.textContent + ' | ' + svTema.textContent));
  // armador del banco
  await p.goto('http://localhost:8771/app/index.html#/banco');
  await p.waitForSelector('#bEsp');
  console.log('sin CB elegida, hay paso materias:', await p.$('#bCat') !== null);
  await p.click('#bEsp [data-esp="ciencias_basicas"]');
  await p.waitForSelector('#bCat');
  console.log('chips materias:', (await p.$$eval('#bCat .chip', c => c.map(x => x.textContent.trim()))).join(' | '));
  await p.click('#bCat .chip[data-cat="Fisiología"]');
  await p.click('#bCat .chip[data-cat="Embriología"]');
  console.log('pasos:', (await p.$$eval('.builder__step legend', l => l.map(x => x.textContent.trim()))).join(' | '));
  console.log('resumen:', await p.textContent('.builder__sum'));
  await p.click('label.pick:has(input[name="cantidad"][value="0"])');
  console.log('resumen todas:', await p.textContent('.builder__sum'));
  await p.screenshot({ path: shot + '_banco.png', fullPage: true });
  await p.click('[data-accion="comenzar"]');
  await p.waitForFunction(() => /Pregunta 1 de/.test((document.getElementById('svCounter') || {}).textContent || ''), null, { timeout: 10000 });
  console.log('sesión banco:', await p.evaluate(() => svTitle.textContent + ' | ' + svCounter.textContent + ' | ' + svTema.textContent));
  // CB + Cardiología + Anatomía: cardiología no se recorta
  await p.goto('http://localhost:8771/app/index.html#/inicio'); await p.goto('http://localhost:8771/app/index.html#/banco');
  await p.waitForSelector('#bCat');
  await p.click('#bCat .chip[data-cat=""]');
  await p.click('#bEsp [data-esp="cardiologia"]');
  await p.click('#bCat .chip[data-cat="Anatomía"]');
  await p.click('label.pick:has(input[name="cantidad"][value="0"])');
  console.log('CB(Anatomía)+Cardio:', await p.textContent('.builder__sum'), '| pasos:', (await p.$$eval('.builder__step legend', l => l.map(x => x.textContent.trim()))).join(' | '));
  await p.click('#bEsp [data-esp="ciencias_basicas"]');
  console.log('quitando CB, paso materias:', await p.$('#bCat') !== null, '|', await p.textContent('.builder__sum'));
  console.log('ERRORES:', errs.length ? errs : 'ninguno');
  await b.close();
})().catch(e => { console.error('FALLO', e.message); process.exit(1); });
