(async () => {
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const dir = process.argv[2] || 'out/flujogramas';
const files = fs.readdirSync(dir).sort();
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
let bad = 0;
for (const f of files) {
  const svg = fs.readFileSync(`${dir}/${f}`, 'utf8').replace(/^<\?xml[^>]*>\s*/, '')
    .replace('font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif"', 'font-family="Arial"');
  await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
  const r = await p.evaluate(() => {
    const out = [];
    for (const t of document.querySelectorAll('text[data-max]')) {
      const max = +t.getAttribute('data-max'); if (!max) continue;
      for (const s of t.querySelectorAll('tspan')) {
        const w = s.getComputedTextLength();
        if (w > max + 1) out.push([s.textContent.slice(0, 50), Math.round(w), max]);
      }
    }
    return out;
  });
  if (r.length) { bad++; console.log(f, JSON.stringify(r)); }
  const el = await p.$('svg');
  await el.screenshot({ path: (process.argv[3]||'shots') + `/${f.replace('.svg', '.png')}` });
}
console.log('archivos con desborde:', bad, '/', files.length);
await b.close();
})();
