// Verificador de encaje. Uso: node check27.cjs <dir_svg> <dir_png> [patrón]
// Revisa: 1) texto que se sale de su ancho, 2) marcas o rótulos que se salen de su imagen (data-box),
// 3) insignias (círculos rellenos) que no caben enteras en su recuadro, 4) texto que se sale de su recuadro,
// 5) textos que se pisan entre sí. Además saca un PNG de cada flujograma.
(async () => {
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [dir, out, pat] = process.argv.slice(2);
fs.mkdirSync(out, { recursive: true });
const files = fs.readdirSync(dir).filter(f => f.endsWith('.svg') && (!pat || new RegExp(pat).test(f))).sort();
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
let bad = 0;
for (const f of files) {
  const svg = fs.readFileSync(`${dir}/${f}`, 'utf8').replace(/^<\?xml[^>]*>\s*/, '')
    .replace('font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif"', 'font-family="Arial"');
  await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
  const r = await p.evaluate(() => {
    const o = [];
    const root = document.querySelector('svg');
    const R0 = root.getBoundingClientRect();
    const bb = e => { const q = e.getBoundingClientRect(); return { x0: q.left - R0.left, y0: q.top - R0.top, x1: q.right - R0.left, y1: q.bottom - R0.top }; };
    const inBox = e => e.closest('g[data-box]');
    const cut = s => s.slice(0, 40);
    // 1) desborde de ancho
    for (const t of document.querySelectorAll('text[data-max]')) {
      const max = +t.getAttribute('data-max'); if (!max) continue;
      for (const s of t.querySelectorAll('tspan')) {
        const w = s.getComputedTextLength();
        if (w > max + 1) o.push(['ancho', cut(s.textContent), Math.round(w), max]);
      }
    }
    // 2) todo lo de una imagen dentro de su recuadro
    for (const g of document.querySelectorAll('g[data-box]')) {
      const [x, y, w, h] = g.getAttribute('data-box').split(' ').map(Number);
      for (const e of g.querySelectorAll('rect,circle,line,polygon,path,text,ellipse,polyline,image')) {
        if (e.closest('defs')) continue;
        const q = bb(e);
        if (q.x1 - q.x0 === 0 && q.y1 - q.y0 === 0) continue;
        if (q.x0 < x - 1 || q.y0 < y - 1 || q.x1 > x + w + 1 || q.y1 > y + h + 1)
          o.push(['fuera de imagen', e.tagName, cut(e.textContent || ''), [q.x0, q.y0, q.x1, q.y1].map(Math.round), [x, y, x + w, y + h]]);
      }
    }
    // recuadros fuera de las imágenes (sin el fondo de la página)
    const rects = [...document.querySelectorAll('rect')].slice(1)
      .filter(e => !inBox(e) && !e.closest('defs') && e.getAttribute('fill') !== 'none')
      .map(e => ({ e, ...bb(e) })).filter(q => (q.x1 - q.x0) > 4 && (q.y1 - q.y0) > 4);
    const menor = (cx, cy) => {
      let best = null;
      for (const q of rects) if (cx >= q.x0 && cx <= q.x1 && cy >= q.y0 && cy <= q.y1) {
        const a = (q.x1 - q.x0) * (q.y1 - q.y0);
        if (!best || a < best.a) best = { ...q, a };
      }
      return best;
    };
    // 3) insignias enteras dentro de su recuadro
    for (const c of document.querySelectorAll('circle')) {
      if (inBox(c) || c.getAttribute('fill') === 'none' || +c.getAttribute('r') > 14) continue;
      const q = bb(c), cx = (q.x0 + q.x1) / 2, cy = (q.y0 + q.y1) / 2;
      const m = menor(cx, cy);
      if (!m) continue;
      // Una insignia centrada sobre el borde o la esquina es parte del diseño; la que está casi
      // dentro y asoma un poco por un lado (como la «2» recortada) es un error.
      const r_ = (q.x1 - q.x0) / 2;
      const asoma = [[cx - m.x0, q.x0 < m.x0 - 0.5], [m.x1 - cx, q.x1 > m.x1 + 0.5],
                     [cy - m.y0, q.y0 < m.y0 - 0.5], [m.y1 - cy, q.y1 > m.y1 + 0.5]]
        .some(([d, sale]) => sale && d > 3);
      if (asoma)
        o.push(['insignia sale', [q.x0, q.y0, q.x1, q.y1].map(Math.round), [m.x0, m.y0, m.x1, m.y1].map(Math.round)]);
    }
    // 4) y 5) texto dentro de su recuadro y sin pisarse
    const tsp = [];
    for (const t of document.querySelectorAll('text')) {
      if (inBox(t)) continue;
      const fs_ = +t.getAttribute('font-size') || 12;
      for (const s of (t.querySelectorAll('tspan').length ? t.querySelectorAll('tspan') : [t])) {
        if (!s.textContent.trim()) continue;
        const q = bb(s);
        // caja de glifos: se recorta el interlineado que agrega el navegador
        const pad = fs_ * 0.18;
        tsp.push({ t, s, x0: q.x0, x1: q.x1, y0: q.y0 + pad, y1: q.y1 - pad });
      }
    }
    const badges = [...document.querySelectorAll('circle')].filter(c => !inBox(c) && c.getAttribute('fill') !== 'none' && +c.getAttribute('r') <= 14).map(bb);
    for (const q of tsp) {
      const tx = (q.x0 + q.x1) / 2, ty = (q.y0 + q.y1) / 2;
      if (badges.some(c => tx >= c.x0 && tx <= c.x1 && ty >= c.y0 && ty <= c.y1)) continue;  // número de una insignia
      const m = menor((q.x0 + q.x1) / 2, (q.y0 + q.y1) / 2);
      if (m && (q.x0 < m.x0 - 1 || q.x1 > m.x1 + 1 || q.y0 < m.y0 - 1 || q.y1 > m.y1 + 1))
        o.push(['texto sale de recuadro', cut(q.s.textContent), [q.x0, q.y0, q.x1, q.y1].map(Math.round), [m.x0, m.y0, m.x1, m.y1].map(Math.round)]);
    }
    // 6) líneas que atraviesan un texto (fuera de las imágenes)
    const cruza = (x1, y1, x2, y2, q) => {
      // recorte de Liang-Barsky del segmento contra la caja del texto
      let t0 = 0, t1 = 1; const dx = x2 - x1, dy = y2 - y1;
      for (const [p, qq] of [[-dx, x1 - q.x0], [dx, q.x1 - x1], [-dy, y1 - q.y0], [dy, q.y1 - y1]]) {
        if (p === 0) { if (qq < 0) return false; continue; }
        const r = qq / p;
        if (p < 0) { if (r > t1) return false; if (r > t0) t0 = r; } else { if (r < t0) return false; if (r < t1) t1 = r; }
      }
      return t1 - t0 > 1e-6;
    };
    const opaca = e => { const f = e.getAttribute('fill'); return f && f !== 'none' && !e.getAttribute('opacity'); };
    // ¿hay un recuadro opaco dibujado después de la línea que tapa el texto? (etiqueta sobre un conector)
    const tapado = (ln, q) => rects.some(r => opaca(r.e) && (ln.compareDocumentPosition(r.e) & Node.DOCUMENT_POSITION_FOLLOWING)
      && r.x0 <= q.x0 + 1 && r.x1 >= q.x1 - 1 && r.y0 <= q.y0 + 1 && r.y1 >= q.y1 - 1);
    for (const ln of document.querySelectorAll('line')) {
      if (inBox(ln)) continue;
      const st = (ln.getAttribute('stroke') || '').toLowerCase();
      if (st === '#e2e8f0' || st === '#f1f5f9') continue;   // cuadrícula de fondo de un gráfico
      const m = ln.getScreenCTM(), P = (x, y) => { const p = root.createSVGPoint(); p.x = x; p.y = y; const r = p.matrixTransform(m); return [r.x - R0.left, r.y - R0.top]; };
      const [x1, y1] = P(+ln.getAttribute('x1'), +ln.getAttribute('y1')), [x2, y2] = P(+ln.getAttribute('x2'), +ln.getAttribute('y2'));
      for (const q of tsp) {
        const qi = { x0: q.x0 + 1, x1: q.x1 - 1, y0: q.y0 + 1, y1: q.y1 - 1 };
        if (!(qi.x1 > qi.x0 && qi.y1 > qi.y0 && cruza(x1, y1, x2, y2, qi))) continue;
        // tachado: línea horizontal a media altura del propio texto (opción descartada)
        if (Math.abs(y1 - y2) < 0.5 && y1 > q.y0 && y1 < q.y1 && Math.min(x1, x2) >= q.x0 - 16 && Math.max(x1, x2) <= q.x1 + 16
            && Math.abs(x2 - x1) >= 0.5 * (q.x1 - q.x0)) continue;
        if (tapado(ln, q)) continue;
        o.push(['línea cruza texto', cut(q.s.textContent)]);
      }
    }
    for (let i = 0; i < tsp.length; i++) for (let j = i + 1; j < tsp.length; j++) {
      const a = tsp[i], c = tsp[j];
      if (a.t === c.t) continue;
      // el mismo texto dibujado dos veces (halo blanco debajo) no es una superposición
      if (a.s.textContent === c.s.textContent && Math.abs(a.x0 - c.x0) < 2 && Math.abs(a.y0 - c.y0) < 2) continue;
      const ox = Math.min(a.x1, c.x1) - Math.max(a.x0, c.x0), oy = Math.min(a.y1, c.y1) - Math.max(a.y0, c.y0);
      if (ox > 1 && oy > 1) o.push(['textos se pisan', cut(a.s.textContent), cut(c.s.textContent)]);
    }
    return o;
  });
  if (r.length) { bad++; console.log(f); for (const x of r) console.log('   ', JSON.stringify(x)); }
  if (out !== '-') await (await p.$('svg')).screenshot({ path: `${out}/${f.replace('.svg', '.png')}` });
}
console.log('archivos con problemas:', bad, '/', files.length);
await b.close();
})();
