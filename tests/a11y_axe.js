const fs=require('fs');const {chromium}=require('playwright');let violaciones=0;
/* Auditoría de accesibilidad (axe-core, WCAG 2.2 AA) sobre las pantallas principales.
   Uso: npm i axe-core playwright && php -S 127.0.0.1:8130 (en la raíz del proyecto) && node tests/a11y_axe.js
   Variables: BASE (por defecto http://127.0.0.1:8130/), AXE_PATH (ruta de axe.min.js), CHROMIUM (ejecutable). Sale con código 1 si hay violaciones. */
const AXE=fs.readFileSync(process.env.AXE_PATH||require.resolve('axe-core/axe.min.js'),'utf8');
(async()=>{const b=await chromium.launch({executablePath:process.env.CHROMIUM||undefined});
const ctx=await b.newContext({viewport:{width:1200,height:900}});const p=await ctx.newPage();
await p.addInitScript(()=>{try{localStorage.setItem('mqp_guardia_intro_v1','omitir')}catch(e){}});
const U=process.env.BASE||'http://127.0.0.1:8130/';
async function auditar(nombre){
  await p.evaluate(AXE);
  const r=await p.evaluate(async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}}));
  const graves=r.violations.map(v=>({id:v.id,impacto:v.impact,n:v.nodes.length,ej:v.nodes[0].target.join(' ').slice(0,80),ayuda:v.help}));
  violaciones+=graves.length;
  console.log('==',nombre,'→',graves.length?graves.length+' tipos de problema':'sin violaciones');graves.forEach(g=>console.log('  ',g.impacto,g.id,'×'+g.n,'|',g.ayuda,'|',g.ej));
}
await p.goto(U+'index.html');await p.waitForTimeout(2500);await auditar('Landing');
await p.goto(U+'terminos.html');await p.waitForTimeout(600);await auditar('Términos');
await p.goto(U+'app/#/registro');await p.waitForTimeout(900);await auditar('App · registro');
await p.fill('#a-nombre','Ax Tester');await p.fill('#a-correo','ax'+Date.now()+'@t.pe');await p.fill('#a-clave','clave12345');await p.check('#a-acepto');await p.click('#authForm button[type=submit]');await p.waitForTimeout(1300);
await p.goto(U+'app/#/inicio');await p.waitForTimeout(1200);await auditar('App · inicio');
await p.goto(U+'app/#/progreso');await p.waitForTimeout(900);await auditar('App · progreso (vacío)');
await p.goto(U+'app/#/guardia');await p.waitForTimeout(900);await auditar('Guardia · lista');
await p.goto(U+'app/#/guardia/asma');await p.waitForTimeout(700);await auditar('Guardia · caso');
await p.click('.gd-op');await p.waitForTimeout(400);await auditar('Guardia · caso con feedback');
await p.goto(U+'app/#/flashcards');await p.waitForTimeout(900);await auditar('Flashcards (vacío)');
await p.goto(U+'app/#/planes');await p.waitForTimeout(900);await auditar('Planes');
await p.goto(U+'app/#/banco/configurar');await p.waitForTimeout(900);await p.click('[data-accion=comenzar]');await p.waitForTimeout(1200);
const o=await p.$$('#svOptions .opt');await o[0].click();await p.waitForTimeout(500);await auditar('Banco · pregunta respondida');
await p.click('#svFlash');await p.waitForTimeout(400);await auditar('Panel «Convertir en flashcard»');await p.keyboard.press('Escape');
await p.click('#svIA');await p.waitForTimeout(500);await auditar('Panel «Preguntar a la IA»');await p.keyboard.press('Escape');
// intro
const c2=await b.newContext({viewport:{width:1200,height:900}});const q=await c2.newPage();
await q.goto(U+'app/#/guardia');await q.waitForTimeout(12500);await q.evaluate(AXE);
const r=await q.evaluate(async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}}));
violaciones+=r.violations.length;
console.log('== Introducción →',r.violations.length?r.violations.map(v=>v.impact+' '+v.id+' ×'+v.nodes.length+' '+v.nodes[0].target.join(' ')).join(' | '):'sin violaciones');
await b.close();process.exit(violaciones?1:0);})();
