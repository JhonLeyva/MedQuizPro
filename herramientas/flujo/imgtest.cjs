const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
  const dir = process.argv[2];
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.svg'))) {
    const data = 'data:image/svg+xml;base64,' + fs.readFileSync(path.join(dir, f)).toString('base64');
    await p.setContent(`<img id=i src="${data}" style="width:1000px">`);
    await p.waitForFunction(() => document.getElementById('i').complete);
    const w = await p.evaluate(() => document.getElementById('i').naturalWidth);
    await p.locator('#i').screenshot({ path: process.argv[3] + '/' + f.replace('.svg', '.png') });
    console.log(f, 'naturalWidth', w);
  }
  await b.close();
})();
