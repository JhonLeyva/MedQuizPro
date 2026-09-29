const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
(async () => {
const dir = process.argv[2] || 'out/flujogramas';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
let bad = 0;
for (const f of fs.readdirSync(dir).sort()) {
  const svg = fs.readFileSync(`${dir}/${f}`, 'utf8').replace(/^<\?xml[^>]*>\s*/, '').replace(/font-family="[^"]*"/, 'font-family="Arial"');
  await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
  const r = await p.evaluate(() => {
    const rects = [...document.querySelectorAll('rect')].filter(r => r.getAttribute('fill') !== 'none' || r.getAttribute('stroke') !== 'none')
      .map(r => r.getBBox()).filter(b => b.width > 30 && b.height > 15);
    const out = [];
    for (const t of document.querySelectorAll('text')) {
      const tb = t.getBBox(); const cx = tb.x + tb.width / 2, cy = tb.y + tb.height / 2;
      const cont = rects.filter(r => cx >= r.x && cx <= r.x + r.width && cy >= r.y && cy <= r.y + r.height)
        .sort((a, b) => a.width * a.height - b.width * b.height)[0];
      if (!cont || cont.width > 990) continue;
      const tol = 2;
      if (tb.y < cont.y - tol || tb.y + tb.height > cont.y + cont.height + tol || tb.x < cont.x - tol || tb.x + tb.width > cont.x + cont.width + tol)
        out.push(t.textContent.slice(0, 40));
    }
    return out;
  });
  if (r.length) { bad++; console.log(f, JSON.stringify(r)); }
}
console.log('archivos con texto fuera de caja:', bad);
await b.close();
})();
