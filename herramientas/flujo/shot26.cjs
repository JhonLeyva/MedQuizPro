const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'), path=require('path');
(async()=>{ const dir=process.argv[2]; const out=process.argv[3];
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--disable-background-networking']});
 const p=await b.newPage({viewport:{width:1000,height:800}, deviceScaleFactor:1.2});
 for (const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg'))){
   const svg=fs.readFileSync(path.join(dir,f),'utf8').replace(/^<\?xml[^>]*>/,'');
   await p.setContent('<html><body style="margin:0;background:#fff">'+svg+'</body></html>');
   await p.locator('svg').first().screenshot({path: path.join(out,f.replace('.svg','.png')), timeout:60000}); }
 await b.close(); })();
