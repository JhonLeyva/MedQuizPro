#!/usr/bin/env node
/* Genera la infografía SVG estática (estilo MedQuizPlus) de cada tarjeta de feedback post-pregunta.
 * Lee los mismos datos que el módulo interactivo (../cards/*.js), así que el contenido no se duplica.
 *
 *   node feedback/svg/generar-svg.js              → incluye las marcas ✎ (para revisión médica)
 *   node feedback/svg/generar-svg.js --publicar   → quita las marcas ✎ (versión para estudiantes)
 */
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.join(__dirname, "..");
const OUT = __dirname;
const PUBLICAR = process.argv.includes("--publicar");

/* ---------- Datos ---------- */

function loadCards() {
  const ctx = {};
  ctx.window = ctx;
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(ROOT, "mqp-feedback.js"), "utf8"), ctx);
  fs.readdirSync(path.join(ROOT, "cards")).filter((f) => f.endsWith(".js")).sort()
    .forEach((f) => vm.runInContext(fs.readFileSync(path.join(ROOT, "cards", f), "utf8"), ctx));
  return ctx.MQPFeedback;
}

/* ---------- Paleta (la misma de las infografías MedQuizPlus) ---------- */

const C = {
  teal: "#0f766e", tealDark: "#134e4a", tealSoft: "#f0fdfa", tealLine: "#99f6e4", tealLight: "#5eead4",
  ink: "#0f172a", text: "#334155", text2: "#475569", muted: "#64748b", faint: "#94a3b8",
  line: "#e2e8f0", line2: "#cbd5e1", bg: "#f8fafc", white: "#ffffff",
  amber: "#f59e0b", amberDark: "#b45309", amberSoft: "#fffbeb", amberText: "#92400e", yellow: "#facc15",
  orange: "#ea580c", orangeDark: "#c2410c", orangeSoft: "#fff7ed", orangeText: "#9a3412",
  green: "#16a34a", greenDark: "#14532d", greenSoft: "#dcfce7", greenSofter: "#f0fdf4", greenText: "#15803d",
  red: "#dc2626", redSoft: "#fef2f2",
  blue: "#2563eb", blueSoft: "#eff6ff",
  purple: "#7c3aed", purpleSoft: "#f5f3ff", purpleLine: "#c4b5fd", purpleText: "#4c1d95"
};
// Significado fijo de cada color de pista (igual que en el módulo interactivo).
const TIPO = {
  decisivo: { color: C.orange, soft: C.orangeSoft, label: "Dato decisivo" },
  gravedad: { color: C.red, soft: C.redSoft, label: "Datos de gravedad" },
  descarta: { color: C.purple, soft: C.purpleSoft, label: "Descarta otras opciones" },
  contexto: { color: C.blue, soft: C.blueSoft, label: "Datos de contexto" }
};
const FONT = "Segoe UI, Roboto, Helvetica, Arial, sans-serif";

/* ---------- Medida de texto (métricas de Helvetica/Arial, la más ancha de la pila) ---------- */

const W_REG = {}, W_BOLD = {};
(function () {
  const up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", lo = "abcdefghijklmnopqrstuvwxyz";
  const upR = [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611];
  const loR = [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500];
  const upB = [722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611];
  const loB = [556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500];
  for (let i = 0; i < 26; i++) { W_REG[up[i]] = upR[i]; W_REG[lo[i]] = loR[i]; W_BOLD[up[i]] = upB[i]; W_BOLD[lo[i]] = loB[i]; }
  for (const d of "0123456789") { W_REG[d] = 556; W_BOLD[d] = 556; }
  const punct = { " ": [278, 278], ".": [278, 278], ",": [278, 278], ":": [278, 333], ";": [278, 333], "(": [333, 333], ")": [333, 333],
    "-": [333, 333], "?": [556, 611], "¿": [611, 611], "!": [278, 333], "¡": [333, 333], "'": [191, 238], "’": [222, 278], "\"": [355, 474],
    "«": [556, 556], "»": [556, 556], "/": [278, 278], "%": [889, 889], "+": [584, 584], "=": [584, 584], "<": [584, 584], ">": [584, 584],
    "≥": [584, 584], "°": [400, 400], "·": [278, 278], "→": [1000, 1000], "↓": [600, 600], "↑": [600, 600], "✓": [800, 800], "✕": [800, 800],
    "◆": [800, 800], "✎": [900, 900], "—": [1000, 1000], "–": [556, 556], "₂": [400, 400], "×": [584, 584], "…": [1000, 1000], "|": [260, 280],
    "[": [278, 333], "]": [278, 333], "&": [667, 722], "*": [389, 389] };
  for (const k in punct) { W_REG[k] = punct[k][0]; W_BOLD[k] = punct[k][1]; }
})();
function measure(str, size, bold) {
  const t = bold ? W_BOLD : W_REG;
  let w = 0;
  for (const ch of str) {
    let v = t[ch];
    if (v == null) { const base = ch.normalize("NFD").replace(/[̀-ͯ]/g, ""); v = t[base]; }
    w += v == null ? 600 : v;
  }
  return (w / 1000) * size * 1.03;
}

/* ---------- Texto enriquecido con ajuste de línea ---------- */

function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

// Marcas admitidas: **negrita**, {{clave|texto}} (color según el mapa `keys`) y ✎.
function parse(str, keys) {
  const segs = [];
  const re = /\{\{(\w+)\|(.+?)\}\}|\*\*(.+?)\*\*|✎/g;
  let last = 0, m;
  while ((m = re.exec(str))) {
    if (m.index > last) segs.push({ t: str.slice(last, m.index) });
    if (m[1]) segs.push({ t: m[2], b: true, c: (keys && keys[m[1]]) || null });
    else if (m[3]) segs.push({ t: m[3], b: true });
    else if (!PUBLICAR) segs.push({ t: "✎", ed: true, glue: true });
    last = re.lastIndex;
  }
  if (last < str.length) segs.push({ t: str.slice(last) });
  const toks = [];
  segs.forEach((s) => {
    if (s.glue) { toks.push({ t: s.t, ed: true, sp: false }); return; }
    const parts = s.t.split(/(\s+)/);
    let sp = false;
    parts.forEach((p) => {
      if (p === "") return;
      if (/^\s+$/.test(p)) { sp = true; return; }
      toks.push({ t: p, b: !!s.b, c: s.c || null, sp: sp });
      sp = false;
    });
    if (sp && toks.length) toks[toks.length - 1].trail = true;
  });
  // Un espacio al final de un segmento separa del siguiente.
  for (let i = 1; i < toks.length; i++) if (toks[i - 1].trail) toks[i].sp = true;
  return toks;
}

function wrap(toks, size, baseBold, maxW) {
  const lines = [[]];
  let w = 0;
  toks.forEach((tk) => {
    const bold = tk.b || baseBold;
    const sz = tk.ed ? size * 0.8 : size;
    const tw = measure(tk.t, sz, bold);
    const sw = tk.sp ? measure(" ", size, bold) : 0;
    const line = lines[lines.length - 1];
    if (line.length && w + sw + tw > maxW && !tk.ed) { lines.push([{ ...tk, sp: false }]); w = tw; }
    else { line.push(line.length ? tk : { ...tk, sp: false }); w += (line.length > 1 ? sw : 0) + tw; }
  });
  return lines;
}

/** Bloque de texto. y = línea base de la primera línea. Devuelve { svg, h (alto ocupado desde la línea base), n } */
function text(x, y, str, o) {
  o = Object.assign({ size: 12, weight: 400, fill: C.text, lh: null, anchor: "start", maxW: 900, italic: false, keys: null }, o);
  const lh = o.lh || Math.round(o.size * 1.42);
  const baseBold = o.weight >= 600;
  const lines = wrap(parse(String(str), o.keys), o.size, baseBold, o.maxW);
  const tsp = lines.map((ln, i) => {
    let inner = "", cur = null, buf = "";
    const flush = () => {
      if (!buf) return;
      if (!cur || (!cur.b && !cur.c && !cur.ed)) inner += esc(buf);
      else {
        const a = [];
        if (cur.b && !baseBold) a.push('font-weight="800"');
        if (cur.c) a.push('fill="' + cur.c + '"');
        if (cur.ed) a.push('fill="' + C.purple + '" font-size="' + (o.size * 0.8).toFixed(1) + '" font-weight="400"');
        inner += "<tspan " + a.join(" ") + ">" + esc(buf) + "</tspan>";
      }
      buf = "";
    };
    ln.forEach((tk) => {
      const key = (tk.b ? "b" : "") + (tk.c || "") + (tk.ed ? "e" : "");
      const curKey = cur ? (cur.b ? "b" : "") + (cur.c || "") + (cur.ed ? "e" : "") : null;
      if (curKey !== key) { flush(); cur = tk; }
      buf += (tk.sp ? " " : "") + tk.t;
    });
    flush();
    return '<tspan x="' + x + '" dy="' + (i === 0 ? 0 : lh) + '">' + inner + "</tspan>";
  }).join("");
  const svg = '<text x="' + x + '" y="' + y + '" font-size="' + o.size + '" font-weight="' + o.weight + '"' +
    (o.italic ? ' font-style="italic"' : "") + ' fill="' + o.fill + '" text-anchor="' + o.anchor + '" xml:space="preserve" data-max="' + Math.round(o.maxW) + '">' + tsp + "</text>";
  return { svg: svg, h: (lines.length - 1) * lh + Math.round(o.size * 0.35), n: lines.length, lh: lh };
}
// Alto de un bloque sin dibujarlo.
function textH(str, o) { return text(0, 0, str, o).h; }

function rect(x, y, w, h, o) {
  o = Object.assign({ rx: 10, fill: C.white, stroke: "none", sw: 1.5, dash: null }, o);
  return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="' + o.rx + '" fill="' + o.fill + '" stroke="' + o.stroke +
    '" stroke-width="' + o.sw + '"' + (o.dash ? ' stroke-dasharray="' + o.dash + '"' : "") + "/>";
}
function pill(x, y, label, o) {
  o = Object.assign({ fill: C.tealSoft, stroke: C.tealLine, color: C.teal, size: 10, h: 18, anchor: "start" }, o);
  const w = measure(label, o.size, true) + 18;
  const x0 = o.anchor === "end" ? x - w : o.anchor === "middle" ? x - w / 2 : x;
  return { w: w, svg: rect(x0, y, w, o.h, { rx: o.h / 2, fill: o.fill, stroke: o.stroke, sw: 1 }) +
    '<text x="' + (x0 + w / 2) + '" y="' + (y + o.h / 2 + o.size * 0.36) + '" font-size="' + o.size + '" font-weight="800" fill="' + o.color + '" text-anchor="middle">' + esc(label) + "</text>" };
}
function label(y, str, right) {
  return '<text x="40" y="' + y + '" font-size="11.5" font-weight="800" fill="' + C.muted + '">' + esc(str.toUpperCase()) + "</text>" +
    (right ? '<text x="960" y="' + y + '" font-size="10.5" font-weight="600" fill="' + C.faint + '" text-anchor="end">' + esc(right) + "</text>" : "");
}
function circleLetter(cx, cy, L, fill, color, r) {
  r = r || 10;
  return '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="' + fill + '"/><text x="' + cx + '" y="' + (cy + 4) + '" font-size="11" font-weight="800" fill="' + (color || C.white) + '" text-anchor="middle">' + esc(L) + "</text>";
}

/* ---------- Secciones ---------- */

const X0 = 40, WIDTH = 920;

function header(card) {
  const tema = card.tema;
  const tw = measure(tema, 11.5, true);
  const p = pill(184 + tw + 18, 32, (card.especialidad + " ENAM").toUpperCase(), { fill: C.tealDark, stroke: "none", color: "#99f6e4", h: 24, size: 10 });
  return rect(16, 16, 968, 56, { fill: C.teal }) +
    '<text x="36" y="51" font-size="20" font-weight="800" fill="#ffffff">MedQuiz<tspan fill="' + C.tealLight + '">Plus</tspan></text>' +
    '<line x1="170" y1="34" x2="170" y2="54" stroke="' + C.tealLight + '" stroke-width="1.5"/>' +
    '<text x="184" y="48" font-size="11.5" font-weight="700" fill="#ffffff">' + esc(tema) + "</text>" + p.svg +
    '<text x="964" y="48" font-size="10.5" font-weight="800" fill="' + C.tealLight + '" text-anchor="end">FEEDBACK POST-PREGUNTA</text>';
}

// A + B + C: la pregunta, la respuesta correcta y qué evaluaba.
function sPregunta(card, y) {
  const keys = {};
  card.pistas.forEach((p) => { if (!keys[p.k]) keys[p.k] = TIPO[p.tipo].color; });
  const LW = 560, RW = 340, LX = X0, RX = X0 + LW + 20;
  let out = "";
  // Izquierda: pregunta con las pistas coloreadas + alternativas
  let ly = y + 12;
  const pl = pill(LX + 16, ly, ("Pregunta " + card.numero + " · " + card.examen).toUpperCase());
  ly += 18 + 26;
  const t1 = text(LX + 18, ly, "¿Por qué esta era la respuesta?", { size: 15, weight: 800, fill: C.tealDark, maxW: LW - 36 });
  ly += t1.h + 20;
  const vg = text(LX + 18, ly, card.enunciado, { size: 12, fill: C.text, lh: 18, maxW: LW - 36, keys: keys });
  ly += vg.h + 14;
  let alts = "";
  card.alternativas.forEach((a) => {
    const ok = a.letra === card.correcta;
    const t = text(LX + 50, ly + 16, a.texto, { size: 11.5, weight: ok ? 800 : 400, fill: ok ? C.greenDark : C.text, maxW: LW - 160 });
    const h = Math.max(24, t.h + 14);
    alts += rect(LX + 16, ly, LW - 32, h, { rx: 8, fill: ok ? C.greenSoft : C.bg, stroke: ok ? C.green : C.line, sw: ok ? 1.5 : 1 }) +
      circleLetter(LX + 31, ly + h / 2, a.letra, ok ? C.green : C.white, ok ? C.white : C.muted, 9) +
      (ok ? "" : '<circle cx="' + (LX + 31) + '" cy="' + (ly + h / 2) + '" r="9" fill="none" stroke="' + C.line2 + '"/>') + t.svg +
      (ok ? '<text x="' + (LX + LW - 28) + '" y="' + (ly + h / 2 + 4) + '" font-size="10.5" font-weight="800" fill="' + C.green + '" text-anchor="end">✓ CORRECTA</text>' : "");
    ly += h + 5;
  });
  const leftH = ly - y + 11;

  // Derecha: respuesta correcta, qué evaluaba, cómo usar la tarjeta si fallaste
  const c = card.alternativas.find((a) => a.letra === card.correcta);
  let ry = y + 25, r = "";
  r += '<text x="' + (RX + 20) + '" y="' + ry + '" font-size="10" font-weight="800" fill="' + C.amberDark + '">RESPUESTA CORRECTA</text>';
  ry += 24;
  const ans = text(RX + 20, ry, c.letra + ". " + c.texto, { size: 14, weight: 800, fill: C.ink, maxW: RW - 40 });
  r += ans.svg; ry += ans.h + 18;
  const rs = text(RX + 20, ry, card.porQueCorrecta.resumen, { size: 11.5, fill: C.text2, lh: 16, maxW: RW - 40 });
  r += rs.svg; ry += rs.h + 18;
  r += '<line x1="' + (RX + 20) + '" y1="' + ry + '" x2="' + (RX + RW - 20) + '" y2="' + ry + '" stroke="' + C.line + '"/>';
  ry += 22;
  r += '<text x="' + (RX + 20) + '" y="' + ry + '" font-size="10" font-weight="800" fill="' + C.amberDark + '">¿QUÉ EVALUABA?</text>';
  ry += 10;
  card.evalua.forEach((e) => { const p = pill(RX + 20, ry, e, { size: 10.5, h: 22 }); r += p.svg; ry += 27; });
  ry += 6;
  r += '<line x1="' + (RX + 20) + '" y1="' + ry + '" x2="' + (RX + RW - 20) + '" y2="' + ry + '" stroke="' + C.line + '"/>';
  ry += 22;
  r += '<text x="' + (RX + 20) + '" y="' + ry + '" font-size="10" font-weight="800" fill="' + C.amberDark + '">¿FALLASTE?</text>';
  ry += 18;
  const fl = text(RX + 20, ry, "Busca tu letra en **«Opciones de la pregunta»**: ahí está dónde suele fallar el razonamiento.", { size: 11, fill: C.text2, lh: 15.5, maxW: RW - 40 });
  r += fl.svg; ry += fl.h + 16;
  const rightH = ry - y;

  const H = Math.max(leftH, rightH);
  out += rect(LX, y, LW, H, { fill: C.white, stroke: C.teal, sw: 2 }) + pl.svg + t1.svg + vg.svg + alts;
  out += rect(RX, y, RW, H, { fill: C.bg, stroke: C.line2 }) + rect(RX + 1, y + 1, 6, H - 2, { rx: 3, fill: C.amber }) + r;
  // Leyenda de colores de la viñeta
  const ly2 = y + H + 24;
  out += legend(ly2);
  return { svg: out, h: H + 32 };
}

function legend(y) {
  let x = X0, s = "";
  [["decisivo", "Dato decisivo"], ["gravedad", "Gravedad"], ["descarta", "Descarta opciones"], ["contexto", "Contexto"]].forEach(([k, l]) => {
    s += rect(x, y - 9, 10, 10, { rx: 2, fill: TIPO[k].color }) + '<text x="' + (x + 15) + '" y="' + y + '" font-size="10.5" font-weight="700" fill="' + C.muted + '">' + l + "</text>";
    x += measure(l, 10.5, true) + 34;
  });
  return s + '<text x="' + x + '" y="' + y + '" font-size="10.5" fill="' + C.muted + '">= color de cada dato en la pregunta</text>';
}

// D: pistas agrupadas por tipo (cada dato decisivo en su propia tarjeta).
function groupPistas(card) {
  const out = [], byType = {};
  card.pistas.forEach((p) => {
    if (p.tipo === "decisivo") out.push({ tipo: "decisivo", etiqueta: p.etiqueta || TIPO.decisivo.label, items: [p] });
    else (byType[p.tipo] = byType[p.tipo] || { tipo: p.tipo, etiqueta: TIPO[p.tipo].label, items: [] }).items.push(p);
  });
  ["gravedad", "descarta", "contexto"].forEach((t) => { if (byType[t]) out.push(byType[t]); });
  return out;
}
function sPistas(card, y) {
  let out = label(y + 12, "Las pistas que debías reconocer", "No todos los datos pesan igual");
  y += 24;
  const groups = groupPistas(card);
  // Contenido primero; el alto de la tarjeta sale de lo que realmente se dibujó.
  // Contenido primero; el alto de la tarjeta sale de lo que realmente se dibujó.
  // ncol > 1 reparte los datos del grupo en columnas (tarjetas a todo el ancho).
  const content = (g, x, yy, w, ncol) => {
    ncol = ncol || 1;
    const t = TIPO[g.tipo], cw = (w - 40 - (ncol - 1) * 24) / ncol;
    let s = '<text x="' + (x + 20) + '" y="' + (yy + 34) + '" font-size="10" font-weight="800" fill="' + t.color + '">' + esc(g.etiqueta.toUpperCase()) + "</text>";
    let iy = yy + 58, rowBottom = iy;
    g.items.forEach((it, i) => {
      const col = i % ncol;
      if (col === 0 && i) iy = rowBottom + 26;
      const ix = x + 20 + col * (cw + 24);
      let cy = iy;
      const d = text(ix, cy, it.dato, { size: 12.5, weight: 800, fill: C.ink, maxW: cw });
      cy += d.h + 18;
      const sg = text(ix, cy, "→ " + it.significa, { size: 11.5, fill: C.text2, lh: 16, maxW: cw });
      s += d.svg + sg.svg;
      rowBottom = Math.max(col === 0 ? 0 : rowBottom, cy + sg.h);
    });
    return { svg: s, h: rowBottom - yy + 18 };
  };
  const frame = (g, x, yy, w, h) => {
    const t = TIPO[g.tipo], dec = g.tipo === "decisivo";
    return rect(x, yy, w, h, { rx: 14, fill: C.white, stroke: dec ? t.color : C.line2, sw: dec ? 2.5 : 1.5 }) + rect(x, yy, w, 8, { rx: 4, fill: t.color }) +
      (dec ? pill(x + w - 18, yy - 7, "◆ DECIDE", { fill: C.orangeSoft, stroke: C.orange, color: C.orangeDark, h: 22, anchor: "end" }).svg : "");
  };
  const CW = (WIDTH - 20) / 2, GAP = 18;
  // Un grupo con 3 o más datos va a todo el ancho, con los datos en columnas.
  const wide = groups.filter((g) => g.items.length >= 3);
  const narrow = groups.filter((g) => g.items.length < 3);
  // Las demás tarjetas en dos columnas: se prueba cada reparto (respetando el orden) y se elige
  // el más equilibrado; la última tarjeta de cada columna se estira hasta el mismo borde.
  const hs = narrow.map((g) => content(g, 0, 0, CW).h);
  let best = null;
  for (let mask = 0; mask < 1 << narrow.length; mask++) {
    const tot = [0, 0];
    narrow.forEach((g, i) => { tot[(mask >> i) & 1] += hs[i] + GAP; });
    const score = Math.max(tot[0], tot[1]) * 10 + Math.abs(tot[0] - tot[1]) + (narrow.length && !(mask & 1) ? 0 : 0.5);
    if (narrow.length > 1 && (tot[0] === 0 || tot[1] === 0)) continue;
    if (!best || score < best.score) best = { mask: mask, score: score };
  }
  const cols = [{ x: X0, y: y, items: [] }, { x: X0 + CW + 20, y: y, items: [] }];
  narrow.forEach((g, i) => {
    const col = cols[best ? (best.mask >> i) & 1 : 0];
    const c = content(g, col.x, col.y, CW);
    col.items.push({ g: g, c: c, y: col.y });
    col.y += c.h + GAP;
  });
  let bottom = Math.max(cols[0].y, cols[1].y) - GAP;
  cols.forEach((col) => col.items.forEach((it, i) => {
    const h = i === col.items.length - 1 ? bottom - it.y : it.c.h;
    out += frame(it.g, col.x, it.y, CW, h) + it.c.svg;
  }));
  y = narrow.length ? bottom + GAP : y;
  wide.forEach((g) => {
    const c = content(g, X0, y, WIDTH, Math.min(3, g.items.length));
    out += frame(g, X0, y, WIDTH, c.h) + c.svg;
    y += c.h + GAP;
  });
  return { svg: out, y: y };
}

// E: razonamiento clínico como cadena + regla «si veo → pienso → hago».
function sRazonamiento(card, y) {
  const r = card.razonamiento;
  let out = label(y + 12, "Razonamiento clínico", r.ruta);
  y += 24;
  const n = r.pasos.length, gap = 26, w = (WIDTH - gap * (n - 1)) / n;
  let h = 0;
  r.pasos.forEach((p) => { h = Math.max(h, 44 + textH(p.a, { size: 11.5, lh: 16, maxW: w - 28 }) + 16); });
  r.pasos.forEach((p, i) => {
    const x = X0 + i * (w + gap), last = i === n - 1;
    out += rect(x, y, w, h, { fill: last ? C.tealSoft : C.bg, stroke: last ? C.teal : C.line, sw: last ? 2 : 1.5 });
    out += '<text x="' + (x + 14) + '" y="' + (y + 24) + '" font-size="10.5" font-weight="800" fill="' + C.teal + '">' + esc(p.q.toUpperCase()) + "</text>";
    out += text(x + 14, y + 46, p.a, { size: 11.5, fill: last ? C.tealDark : C.text, lh: 16, maxW: w - 28 }).svg;
    if (!last) {
      const ax = x + w + 6, ay = y + h / 2;
      out += '<path d="M' + ax + "," + (ay - 7) + " L" + (ax + 12) + "," + ay + " L" + ax + "," + (ay + 7) + ' z" fill="' + C.teal + '"/>';
    }
  });
  y += h + 12;
  const rule = "{{L|SI VEO}}  " + r.regla.veo + "   {{L|→ PIENSO}}  " + r.regla.pienso + "   {{L|→ HAGO}}  " + r.regla.hago;
  const rh = textH(rule, { size: 12, weight: 700, lh: 17, maxW: WIDTH - 36 }) + 36;
  out += rect(X0, y, WIDTH, rh, { rx: 8, fill: C.teal });
  out += text(X0 + 18, y + 23, rule, { size: 12, weight: 700, fill: C.white, lh: 17, maxW: WIDTH - 36, keys: { L: "#99f6e4" } }).svg;
  return { svg: out, y: y + rh + 18 };
}

// F: algoritmo con la ruta del paciente (misma geometría que el módulo interactivo).
const G = { rowH: 112, evX: 196, cols: [340, 620], rectW: [210, 200], dW: 230, dH: 84 };
function sAlgoritmo(card, y) {
  const a = card.algoritmo;
  let out = label(y + 12, "Ruta del paciente en el algoritmo", a.titulo);
  y += 24;
  const ox = X0 + (WIDTH - 760) / 2, top = y + 52;
  const byId = {};
  let maxRow = 0;
  a.nodes.forEach((n) => {
    const cx = ox + G.cols[n.col], cy = top + 42 + n.row * G.rowH;
    n._b = n.kind === "decision" ? { cx, cy, w: G.dW, h: G.dH } : { cx, cy, w: G.rectW[n.col], h: 26 + 16 * n.lines.length };
    byId[n.id] = n; maxRow = Math.max(maxRow, n.row);
  });
  const notaH = a.nota ? textH(a.nota, { size: 11, lh: 15.5, maxW: WIDTH - 40 }) + 18 : 0;
  const boxH = 52 + 42 + maxRow * G.rowH + 42 + 22 + notaH + 8;
  out += rect(X0, y, WIDTH, boxH, { fill: C.white, stroke: C.line2 });
  // Leyenda
  let lx = X0 + 20;
  const ly = y + 26;
  out += '<line x1="' + lx + '" y1="' + (ly - 4) + '" x2="' + (lx + 22) + '" y2="' + (ly - 4) + '" stroke="' + C.green + '" stroke-width="3"/>' +
    '<text x="' + (lx + 30) + '" y="' + ly + '" font-size="10.5" font-weight="700" fill="' + C.muted + '">Ruta de este paciente</text>';
  lx += 30 + measure("Ruta de este paciente", 10.5, true) + 24;
  out += circleLetter(lx + 8, ly - 4, card.correcta, C.green, C.white, 8) + '<text x="' + (lx + 22) + '" y="' + ly + '" font-size="10.5" font-weight="700" fill="' + C.muted + '">Respuesta correcta</text>';
  lx += 22 + measure("Respuesta correcta", 10.5, true) + 24;
  out += circleLetter(lx + 8, ly - 4, "·", C.muted, C.white, 8) + '<text x="' + (lx + 22) + '" y="' + ly + '" font-size="10.5" font-weight="700" fill="' + C.muted + '">Dónde serían correctas las otras opciones</text>';
  out += '<line x1="' + (X0 + 16) + '" y1="' + (y + 40) + '" x2="' + (X0 + WIDTH - 16) + '" y2="' + (y + 40) + '" stroke="' + C.line + '"/>';
  out += '<defs><marker id="arr-ok-' + card.id + '" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="' + C.green + '"/></marker>' +
    '<marker id="arr-mut-' + card.id + '" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="' + C.line2 + '"/></marker></defs>';
  out += '<text x="' + (ox + G.evX) + '" y="' + (top + 2) + '" font-size="10.5" font-weight="800" fill="' + C.green + '" text-anchor="end" letter-spacing="0.8">ESTE PACIENTE</text>';
  a.edges.forEach((e) => {
    const s = byId[e.from]._b, t = byId[e.to]._b;
    let d, lx2, ly2, anchor;
    if (byId[e.from].col === byId[e.to].col) {
      const y1 = s.cy + s.h / 2, y2 = t.cy - t.h / 2 - 2;
      d = "M" + s.cx + "," + y1 + " L" + t.cx + "," + y2; lx2 = s.cx + 10; ly2 = (y1 + y2) / 2 + 4; anchor = "start";
    } else {
      const x1 = s.cx + s.w / 2, x2 = t.cx - t.w / 2 - 2;
      d = "M" + x1 + "," + s.cy + " L" + x2 + "," + t.cy; lx2 = (x1 + x2) / 2; ly2 = s.cy - 8; anchor = "middle";
    }
    out += '<path d="' + d + '" fill="none" stroke="' + (e.ruta ? C.green : C.line2) + '" stroke-width="' + (e.ruta ? 3 : 1.6) + '" marker-end="url(#arr-' + (e.ruta ? "ok" : "mut") + "-" + card.id + ')"/>';
    if (e.label) out += '<text x="' + lx2 + '" y="' + ly2 + '" font-size="11" font-weight="800" fill="' + (e.ruta ? C.green : C.faint) + '" text-anchor="' + anchor + '">' + esc(e.label) + "</text>";
  });
  a.nodes.forEach((n) => {
    const b = n._b, route = !!n.ruta, fin = !!n.final;
    const fill = fin ? C.green : route ? C.greenSofter : C.bg;
    const stroke = route ? C.green : n.kind === "dx" ? C.blue : C.line2;
    const sw = route ? 2.5 : 1.5, dash = !route && n.kind === "dx" ? ' stroke-dasharray="4 3"' : "";
    if (n.kind === "decision") {
      out += '<polygon points="' + b.cx + "," + (b.cy - b.h / 2) + " " + (b.cx + b.w / 2) + "," + b.cy + " " + b.cx + "," + (b.cy + b.h / 2) + " " + (b.cx - b.w / 2) + "," + b.cy +
        '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="' + sw + '"' + dash + "/>";
    } else {
      out += '<rect x="' + (b.cx - b.w / 2) + '" y="' + (b.cy - b.h / 2) + '" width="' + b.w + '" height="' + b.h + '" rx="' + (n.kind === "start" ? b.h / 2 : 7) +
        '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="' + sw + '"' + dash + "/>";
    }
    const fs2 = n.kind === "decision" ? 12.5 : 13, lh = n.kind === "decision" ? 15 : 16;
    const y0 = b.cy - ((n.lines.length - 1) * lh) / 2 + 4.5;
    const maxW = n.kind === "decision" ? 170 : b.w - 16;
    out += '<text font-size="' + fs2 + '" font-weight="' + (route ? 800 : 400) + '" fill="' + (fin ? C.white : route ? C.greenDark : C.muted) + '" text-anchor="middle" data-max="' + maxW + '">' +
      n.lines.map((l, i) => '<tspan x="' + b.cx + '" y="' + (y0 + i * lh) + '">' + esc(l) + "</tspan>").join("") + "</text>";
    if (n.evidencia) {
      const ey0 = b.cy - ((n.evidencia.length - 1) * 15) / 2 + 4;
      out += '<line x1="' + (ox + G.evX + 4) + '" y1="' + b.cy + '" x2="' + (b.cx - b.w / 2 - 4) + '" y2="' + b.cy + '" stroke="' + C.green + '" stroke-dasharray="2 3"/>' +
        '<text font-size="11.5" font-weight="600" fill="' + C.greenText + '" text-anchor="end" data-max="190">' +
        n.evidencia.map((l, i) => '<tspan x="' + (ox + G.evX) + '" y="' + (ey0 + i * 15) + '">' + esc(l) + "</tspan>").join("") + "</text>";
    }
    const nOp = (n.opciones || []).length;
    (n.opciones || []).forEach((L, i) => {
      let bx = b.cx + b.w / 2 - 6 - (nOp - 1 - i) * 26, by = b.cy - b.h / 2 + 2;
      if (n.kind === "decision") { bx = b.cx + 30 + i * 26; by = b.cy - b.h / 2 + 8; }
      const ok = L === card.correcta;
      out += '<circle cx="' + bx + '" cy="' + by + '" r="12" fill="' + C.white + '"/>' + circleLetter(bx, by, L, ok ? C.green : C.muted, C.white, 11);
    });
  });
  if (a.nota) out += text(X0 + 20, y + boxH - notaH + 2, a.nota, { size: 11, fill: C.muted, italic: true, lh: 15.5, maxW: WIDTH - 40 }).svg;
  return { svg: out, y: y + boxH + 18 };
}

// G + I: por qué es la correcta y trampas, lado a lado.
function sCorrectaTrampa(card, y) {
  const c = card.alternativas.find((a) => a.letra === card.correcta);
  const W2 = (WIDTH - 20) / 2;
  const tA = "¿Por qué " + c.letra + " es la correcta?";
  const bx = X0 + W2 + 20;
  const ta = text(X0 + 20, y + 56, card.porQueCorrecta.texto, { size: 12, fill: C.text, lh: 17.5, maxW: W2 - 40 });
  let tb = "", ty = y + 56;
  card.trampas.forEach((t, i) => {
    if (i) ty += 22;
    tb += '<circle cx="' + (bx + 26) + '" cy="' + (ty - 4) + '" r="3" fill="' + C.amberDark + '"/>';
    const tt = text(bx + 38, ty, t, { size: 12, fill: C.amberText, lh: 17.5, maxW: W2 - 56 });
    tb += tt.svg; ty += tt.h;
  });
  const h = Math.max(56 + ta.h, ty - y) + 18;
  let out = rect(X0, y, W2, h, { fill: C.white, stroke: C.teal, sw: 2 }) +
    pill(X0 + 16, y + 14, "✓ " + tA.toUpperCase(), { fill: C.greenSoft, stroke: C.green, color: C.greenDark }).svg + ta.svg;
  out += rect(bx, y, W2, h, { fill: C.amberSoft, stroke: C.amber }) +
    pill(bx + 16, y + 14, "⚠ " + (card.trampas.length > 1 ? "TRAMPAS FRECUENTES" : "TRAMPA FRECUENTE"), { fill: C.white, stroke: C.amber, color: C.amberDark }).svg + tb;
  return { svg: out, y: y + h + 18 };
}

// H + error del estudiante: cada alternativa con su motivo y qué revisar si la marcaste.
function sOpciones(card, y) {
  let out = label(y + 12, "Opciones de la pregunta", "Por qué sí, por qué no y qué revisar si la marcaste");
  y += 24;
  const c1 = 168, c2 = 330, c3 = 330, x1 = X0 + 46, x2 = x1 + c1 + 16, x3 = x2 + c2 + 20;
  out += rect(X0, y, WIDTH, 32, { rx: 8, fill: C.bg, stroke: C.line });
  [["OPCIÓN", x1], ["POR QUÉ SÍ / POR QUÉ NO", x2], ["SI LA MARCASTE", x3]].forEach(([t, x]) => {
    out += '<text x="' + x + '" y="' + (y + 20) + '" font-size="10.5" font-weight="800" fill="' + C.muted + '">' + t + "</text>";
  });
  y += 38;
  card.alternativas.forEach((a) => {
    const ok = a.letra === card.correcta;
    const o1 = { size: 12, weight: 800, fill: ok ? C.greenDark : C.ink, lh: 16, maxW: c1 };
    const o2 = { size: 11.5, fill: ok ? C.greenDark : C.text, lh: 16, maxW: c2 };
    const o3 = { size: 11.5, fill: ok ? C.greenDark : C.text2, lh: 16, maxW: c3 };
    const s3 = ok ? "**✓ Correcta.** Comprueba que fue por la razón correcta: " + card.aciertoClave
      : (a.error && a.error.inferido ? a.error.texto : "No es correcta porque " + (a.error ? a.error.texto : a.porQue));
    const h = Math.max(textH(a.texto, o1), textH(a.porQue, o2), textH(s3, o3)) + 42;
    out += rect(X0, y, WIDTH, h, { rx: 8, fill: ok ? C.greenSofter : C.white, stroke: ok ? C.green : C.line, sw: ok ? 2 : 1 });
    out += circleLetter(X0 + 22, y + 22, a.letra, ok ? C.green : C.white, ok ? C.white : C.muted, 11);
    if (!ok) out += '<circle cx="' + (X0 + 22) + '" cy="' + (y + 22) + '" r="11" fill="none" stroke="' + C.line2 + '"/>';
    out += text(x1, y + 26, a.texto, o1).svg + text(x2, y + 26, a.porQue, o2).svg;
    if (!ok) out += '<line x1="' + (x3 - 12) + '" y1="' + (y + 12) + '" x2="' + (x3 - 12) + '" y2="' + (y + h - 12) + '" stroke="' + C.red + '" stroke-width="2" opacity="0.5"/>';
    out += text(x3, y + 26, s3, o3).svg;
    y += h + 6;
  });
  return { svg: out, y: y + 12 };
}

// J: ¿qué pasaría si cambiamos un dato?
function sYSi(card, y) {
  const ys = card.ySi;
  if (!ys) return { svg: "", y: y };
  let out = label(y + 12, "¿Qué pasaría si cambiamos un dato?", "Un solo dato cambia; mira qué pasa con la respuesta");
  y += 24;
  const items = [{ orig: true, lab: "CASO ORIGINAL", a: ys.original.dato, r: ys.original.resultado }]
    .concat(ys.variaciones.map((v) => ({ lab: "¿Y SI " + v.chip.toUpperCase() + "?", a: v.cambio, r: v.resultado, f: v.fuente })));
  const n = items.length, gap = 16, w = (WIDTH - gap * (n - 1)) / n;
  const labH = (it) => textH(it.lab, { size: 10.5, weight: 800, lh: 14, maxW: w - 28 });
  const lab = Math.max(...items.map(labH));
  const parts = items.map((it, i) => {
    const x = X0 + i * (w + gap);
    let s = text(x + 14, y + 24, it.lab, { size: 10.5, weight: 800, fill: it.orig ? C.teal : C.orangeDark, lh: 14, maxW: w - 28 }).svg;
    let ty = y + 24 + lab + 20;
    const ta = text(x + 14, ty, it.a, { size: 11.5, fill: C.text, lh: 16, maxW: w - 28 });
    s += ta.svg; ty += ta.h + 20;
    const tr = text(x + 14, ty, "→ " + it.r, { size: 12, weight: 800, fill: it.orig ? C.tealDark : C.orangeText, lh: 16.5, maxW: w - 28 });
    s += tr.svg; ty += tr.h;
    if (it.f) { ty += 18; const tf = text(x + 14, ty, it.f, { size: 10.5, fill: C.muted, italic: true, lh: 14.5, maxW: w - 28 }); s += tf.svg; ty += tf.h; }
    return { x: x, svg: s, h: ty - y + 16, orig: it.orig };
  });
  const h = Math.max(...parts.map((p) => p.h));
  parts.forEach((p) => {
    out += rect(p.x, y, w, h, { fill: p.orig ? C.tealSoft : C.orangeSoft, stroke: p.orig ? C.teal : C.orange, sw: p.orig ? 2 : 1.5 }) + p.svg;
  });
  y += h + 10;
  const gs = "{{P|VARIABLE QUE GOBIERNA EL ALGORITMO:}} " + ys.variable;
  const gh = textH(gs, { size: 12, lh: 17, maxW: WIDTH - 36 }) + 36;
  out += rect(X0, y, WIDTH, gh, { rx: 8, fill: C.purpleSoft, stroke: C.purpleLine });
  out += text(X0 + 18, y + 23, gs, { size: 12, fill: C.purpleText, lh: 17, maxW: WIDTH - 36, keys: { P: C.purple } }).svg;
  return { svg: out, y: y + gh + 18 };
}

// No confundir con… (tabla comparativa, con la columna de este caso resaltada).
function sNoConfundir(card, y) {
  const nc = card.noConfundir;
  if (!nc) return { svg: "", y: y };
  let out = label(y + 12, "No confundir con " + nc.titulo);
  y += 24;
  const cw0 = 150, nd = nc.filas.length, cw = (WIDTH - cw0) / nd;
  const rows = nc.columnas.map((col, ci) => ({ col, cells: nc.filas.map((f) => f.celdas[ci]) }));
  const notaH = nc.nota ? textH(nc.nota, { size: 10.5, lh: 15, maxW: WIDTH - 36 }) + 16 : 0;
  const rowH = rows.map((r) => Math.max(...r.cells.map((c, i) => textH(c, { size: 11.5, weight: nc.filas[i].esEste ? 700 : 400, lh: 16, maxW: cw - 28 }))) + 32);
  const boxH = 46 + rowH.reduce((a, b) => a + b, 0) + notaH + 8;
  out += rect(X0, y, WIDTH, boxH, { fill: C.white, stroke: C.line2 });
  nc.filas.forEach((f, i) => {
    const x = X0 + cw0 + i * cw;
    if (f.esEste) {
      out += rect(x + 4, y + 6, cw - 8, boxH - notaH - 12, { rx: 8, fill: C.tealSoft });
      out += rect(x + 8, y + 8, cw - 16, 32, { rx: 8, fill: C.teal });
      out += '<text x="' + (x + cw / 2) + '" y="' + (y + 28) + '" font-size="12.5" font-weight="800" fill="#ffffff" text-anchor="middle">' + esc(f.dx) + " · este caso</text>";
    } else {
      out += '<text x="' + (x + cw / 2) + '" y="' + (y + 28) + '" font-size="12.5" font-weight="800" fill="' + C.ink + '" text-anchor="middle">' + esc(f.dx) + "</text>";
    }
  });
  out += '<text x="' + (X0 + 16) + '" y="' + (y + 28) + '" font-size="10.5" font-weight="800" fill="' + C.muted + '">CRITERIO</text>';
  let ry = y + 46;
  rows.forEach((r, ri) => {
    out += '<line x1="' + (X0 + 12) + '" y1="' + ry + '" x2="' + (X0 + WIDTH - 12) + '" y2="' + ry + '" stroke="' + C.line + '"/>';
    out += '<text x="' + (X0 + 16) + '" y="' + (ry + 20) + '" font-size="11.5" font-weight="800" fill="' + C.ink + '">' + esc(r.col) + "</text>";
    r.cells.forEach((c, i) => {
      const este = nc.filas[i].esEste;
      out += text(X0 + cw0 + i * cw + 14, ry + 20, c, { size: 11.5, weight: este ? 700 : 400, fill: este ? C.tealDark : C.text2, lh: 16, maxW: cw - 28 }).svg;
    });
    ry += rowH[ri];
  });
  if (nc.nota) out += text(X0 + 18, ry + 14, nc.nota, { size: 10.5, fill: C.muted, italic: true, lh: 15, maxW: WIDTH - 36 }).svg;
  return { svg: out, y: y + boxH + 18 };
}

// ¿Por qué ocurre? Esquema + texto.
const FIG_STYLE = {
  "f-stroke": 'stroke="#64748b" fill="none" stroke-width="2"',
  "f-wall": 'stroke="#0f172a" fill="none" stroke-width="3" stroke-linecap="round"',
  "f-seg": 'stroke="#ea580c" fill="none" stroke-width="4" stroke-linecap="round"',
  "f-red": 'fill="#dc2626"',
  "f-redline": 'stroke="#dc2626" stroke-width="2" fill="none"',
  "f-arrow": 'fill="#dc2626"',
  "f-arrow-mut": 'fill="#64748b"',
  "f-plac": 'fill="#ede9fe" stroke="#7c3aed" stroke-width="2"',
  "f-hema": 'fill="#b91c1c" opacity="0.85"',
  "f-uterus": 'fill="#ffffff" stroke="#0f172a" stroke-width="2.5"',
  "f-txt": 'font-size="12" fill="#0f172a"',
  "f-ttl": 'font-size="12" font-weight="700" fill="#64748b" letter-spacing="0.8"'
};
function figura(FIGS, name, x, y, w) {
  const raw = FIGS[name]();
  const vb = raw.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
  const s = w / +vb[1];
  const inner = raw.replace(/^<svg[^>]*>/, "").replace(/<\/svg>$/, "").replace(/class="([\w-]+)"/g, (_, c) => FIG_STYLE[c] || "");
  return { svg: '<g transform="translate(' + x + "," + y + ") scale(" + s.toFixed(4) + ')">' + inner + "</g>", h: +vb[2] * s };
}
function sFisio(card, y, FIGS) {
  const f = card.fisiopatologia;
  if (!f) return { svg: "", y: y };
  let out = label(y + 12, "¿Por qué ocurre? · " + f.titulo);
  y += 24;
  const FW = 450, TX = X0 + FW + 40, TW = WIDTH - FW - 60;
  const fig = f.figura ? figura(FIGS, f.figura, X0 + 22, y + 20, FW - 20) : { svg: "", h: 0 };
  const cap = text(X0 + 22, y + 20 + fig.h + 16, f.pie, { size: 10.5, fill: C.muted, italic: true, lh: 14.5, maxW: FW - 20 });
  let tx = "", ty = y + 36;
  f.texto.forEach((t, i) => { if (i) ty += 24; const tt = text(TX, ty, t, { size: 12, fill: C.text, lh: 17.5, maxW: TW }); tx += tt.svg; ty += tt.h; });
  const h = Math.max(20 + fig.h + 16 + cap.h + 26, ty - y + 22);
  out += rect(X0, y, WIDTH, h, { fill: C.white, stroke: C.line2 });
  out += rect(X0 + 12, y + 12, FW, h - 24, { rx: 10, fill: C.bg, stroke: C.line, sw: 1 });
  out += fig.svg + cap.svg + tx;
  return { svg: out, y: y + h + 18 };
}

// K: si solo recuerdas 3 cosas (formato «Puntos clave ENAM»).
function sRecuerda(card, y) {
  const TW = WIDTH - 76;
  let body = '<text x="' + (X0 + 18) + '" y="' + (y + 28) + '" font-size="12" font-weight="800" fill="' + C.orange + '">SI SOLO RECUERDAS ' + card.recuerda.length + " COSAS:</text>";
  let ty = y + 58;
  card.recuerda.forEach((r, i) => {
    if (i) ty += 24;
    body += circleLetter(X0 + 30, ty - 4, String(i + 1), C.orange, C.white, 10);
    const t = text(X0 + 52, ty, r, { size: 12.5, fill: C.amberText, lh: 18, maxW: TW });
    body += t.svg; ty += t.h;
  });
  const h = ty - y + 18;
  return { svg: rect(X0, y, WIDTH, h, { fill: C.amberSoft, stroke: C.yellow, sw: 2 }) + body, y: y + h + 18 };
}

// L: compruébalo (respuesta separada para leerla después de pensar).
function sComprueba(card, y) {
  const q = card.comprueba;
  const QW = WIDTH - 40, OW = (WIDTH - 40 - 12) / 2;
  const qh = textH(q.pregunta, { size: 12.5, lh: 18, maxW: QW });
  const optH = (o) => textH(o.texto, { size: 11.5, lh: 16, maxW: OW - 50 }) + 20;
  const rowsH = [];
  for (let i = 0; i < q.opciones.length; i += 2) rowsH.push(Math.max(optH(q.opciones[i]), q.opciones[i + 1] ? optH(q.opciones[i + 1]) : 0));
  const ansText = "{{R|RESPUESTA: " + q.correcta + ".}} " + q.explicacion;
  const ah = textH(ansText, { size: 11.5, lh: 16.5, maxW: WIDTH - 76 }) + 34;
  let out = pill(X0 + 16, y + 14, "COMPRUÉBALO · UNA VARIACIÓN DEL CASO, NO LA MISMA PREGUNTA").svg;
  let ty = y + 58;
  const tq = text(X0 + 20, ty, q.pregunta, { size: 12.5, fill: C.ink, lh: 18, maxW: QW });
  out += tq.svg; ty += tq.h + 16;
  q.opciones.forEach((o, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const ox = X0 + 20 + col * (OW + 12);
    const oy = ty + rowsH.slice(0, row).reduce((a, b) => a + b + 8, 0);
    out += rect(ox, oy, OW, rowsH[row], { rx: 8, fill: C.bg, stroke: C.line, sw: 1 });
    out += circleLetter(ox + 18, oy + rowsH[row] / 2, o.letra, C.white, C.muted, 10) + '<circle cx="' + (ox + 18) + '" cy="' + (oy + rowsH[row] / 2) + '" r="10" fill="none" stroke="' + C.line2 + '"/>';
    out += text(ox + 38, oy + rowsH[row] / 2 - (textH(o.texto, { size: 11.5, lh: 16, maxW: OW - 50 }) - 4) / 2 + 4, o.texto, { size: 11.5, fill: C.text, lh: 16, maxW: OW - 50 }).svg;
  });
  ty += rowsH.reduce((a, b) => a + b + 8, 0) + 14;
  out += '<text x="' + (X0 + 20) + '" y="' + ty + '" font-size="10" font-weight="800" fill="' + C.faint + '">PIÉNSALA ANTES DE LEER LA RESPUESTA ↓</text>';
  ty += 10;
  out += rect(X0 + 20, ty, WIDTH - 40, ah, { rx: 8, fill: C.tealDark });
  out += text(X0 + 38, ty + 23, ansText, { size: 11.5, fill: C.white, lh: 16.5, maxW: WIDTH - 76, keys: { R: C.tealLight } }).svg;
  const h = ty + ah - y + 18;
  return { svg: rect(X0, y, WIDTH, h, { fill: C.white, stroke: C.teal, sw: 1.5, dash: "6 4" }) + out, y: y + h + 18 };
}

function footer(card, y) {
  let s = text(X0, y + 12, card.fuenteCorta, { size: 10.5, fill: C.amberDark, italic: true, lh: 15, maxW: WIDTH });
  let out = s.svg, h = s.h + 12;
  if (!PUBLICAR) {
    const t = text(X0, y + 12 + s.h + 16, "✎ = complemento editorial que no está en el comentario fuente: pendiente de revisión médica antes de publicar.", { size: 10.5, fill: C.purple, italic: true, lh: 15, maxW: WIDTH });
    out += t.svg; h += t.h + 16;
  }
  return { svg: out, y: y + h + 22 };
}

/* ---------- Composición ---------- */

function build(card, FIGS) {
  let body = header(card);
  let y = 90;
  const p = sPregunta(card, y); body += p.svg; y += p.h + 22;
  let r;
  r = sPistas(card, y); body += r.svg; y = r.y + 10;
  r = sRazonamiento(card, y); body += r.svg; y = r.y + 10;
  r = sAlgoritmo(card, y); body += r.svg; y = r.y;
  r = sCorrectaTrampa(card, y); body += r.svg; y = r.y + 10;
  r = sOpciones(card, y); body += r.svg; y = r.y + 4;
  r = sYSi(card, y); body += r.svg; y = r.y + 10;
  r = sNoConfundir(card, y); body += r.svg; y = r.svg ? r.y + 10 : y;
  r = sFisio(card, y, FIGS); body += r.svg; y = r.svg ? r.y + 10 : y;
  r = sRecuerda(card, y); body += r.svg; y = r.y;
  r = sComprueba(card, y); body += r.svg; y = r.y;
  r = footer(card, y); body += r.svg; y = r.y;
  const H = Math.ceil(y);
  const titulo = "¿Por qué esta era la respuesta? " + card.tema + " · Pregunta " + card.numero;
  return '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="' + H + '" viewBox="0 0 1000 ' + H +
    '" font-family="' + FONT + '" role="img" aria-label="' + esc(titulo) + '"><title>' + esc(titulo) + "</title>" +
    rect(0.75, 0.75, 998.5, H - 1.5, { rx: 14, fill: C.white, stroke: C.line }) + body + "</svg>\n";
}

const api = loadCards();
api.cards().forEach((card) => {
  const file = path.join(OUT, card.id + "-" + slug(card.tema) + (PUBLICAR ? "" : "-revision") + ".svg");
  fs.writeFileSync(file, build(card, api.figuras));
  console.log("✓", path.relative(process.cwd(), file));
});
function slug(s) {
  return s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}
