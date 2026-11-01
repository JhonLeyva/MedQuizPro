// node tests/intro_servicio_e2e.js — introducciones de Emergencias, UCI y Consulta externa en un navegador real: aparecen la primera vez de cada visita (se repiten al recargar), se pueden volver a ver,
// dibujan los monitores en movimiento (emergencias y UCI), cargan su tema musical de 30 s, silencian, se cierran con Escape/Omitir sin guardar preferencias,
// respetan «reducir movimiento», no desbordan en móvil y pasan axe en claro y oscuro. Variables: AXE_PATH, CHROMIUM.
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), os = require("os"), path = require("path"), net = require("net"), { spawn, spawnSync } = require("child_process");
const RAIZ = path.resolve(__dirname, ".."); let fallos = 0, total = 0;
const ok = (c, m) => { total++; if (!c) { fallos++; console.log("FALLA:", m); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const libre = () => new Promise(r => { const s = net.createServer().listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });
const AXE = process.env.AXE_PATH && fs.existsSync(process.env.AXE_PATH) ? fs.readFileSync(process.env.AXE_PATH, "utf8") : null;
const SERV = [["emergencias", "guardia/emergencias", "Cada segundo cuenta", "Entrar a la guardia", true], ["uci", "guardia/uci", "Piensa antes de cada ajuste", "Pasar a la UCI", true], ["consulta", "consulta", "Escucha, examina, razona", "Comenzar la consulta", false]];

/* los instantes del audio y de la animación son los mismos */
{ const js = fs.readFileSync(path.join(RAIZ, "intro_servicio.js"), "utf8"), py = fs.readFileSync(path.join(RAIZ, "tools/guardia_audio.py"), "utf8");
  const pr = spawnSync("python3", ["-c", "import importlib.util,json;s=importlib.util.spec_from_file_location('ga','" + path.join(RAIZ, "tools/guardia_audio.py") + "');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(json.dumps(m.RR_FA))"]);
  const rrPy = JSON.parse(String(pr.stdout)), rrJs = JSON.parse(js.match(/var RR_FA = (\[[^\]]+\]);/)[1]);
  ok(rrJs.length === 72 && JSON.stringify(rrPy) === JSON.stringify(rrJs), "emergencias: los 72 intervalos R-R de la fibrilación auricular son los mismos en el audio y en la animación");
  ok(Math.abs(rrJs.reduce((a, x) => a + x, 0) - 30) < 1e-9 && Math.abs(60 / (30 / 72) - 144) < 1e-9, "emergencias: suman exactamente 30 s (el ciclo se repite sin salto) y la frecuencia media es 144 /min");
  const cv = new Set(rrJs).size / rrJs.length, rmin = Math.min(...rrJs), rmax = Math.max(...rrJs); ok(cv > 0.8 && rmin > 0.2 && rmax < 0.7 && rmax / rmin > 1.8, "emergencias: ritmo irregularmente irregular (intervalos variables entre " + rmin + " y " + rmax + " s, sin repetirse)");
  ok(/TIEMPOS_FA/.test(py) && /for t0 in TIEMPOS_FA: add\(b, t0, seno\(1000/.test(py), "emergencias: el pitido del monitor suena en cada onda R");
  ok(/LAT = 60 \/ 78, RESP = 30 \/ 9/.test(js) && /lat = 60 \/ 78; resp = 30 \/ 9/.test(py), "uci: latido a 78 /min y respiración a 18 /min coinciden en el audio y la animación");
  const u = py.slice(py.indexOf("def uci():"), py.indexOf("def consulta():")); ok(!/murmullo|pluck|sierra\(f/.test(u), "uci: solo sonidos de equipos (sin voces ni música)"); }
for (const s of ["emergencias", "uci", "consulta", "hospital"]) { const f = path.join(RAIZ, "guardia/audio/" + s + ".mp3"); ok(fs.existsSync(f) && fs.statSync(f).size > 100000 && fs.statSync(f).size < 700000, s + ": existe el tema musical");
  const pr = spawnSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]); if (pr.status === 0) { const d = parseFloat(String(pr.stdout)); ok(d >= 30 && d < 30.2, s + ": el tema dura 30 s (" + d + ")"); }
  if (s !== "hospital") { const im = path.join(RAIZ, "guardia/portadas/intro-" + s + ".webp"); ok(fs.existsSync(im) && fs.statSync(im).size < 130000, s + ": imagen de la introducción optimizada"); } }

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "is-e2e-")); for (const f of fs.readdirSync(RAIZ)) { const p = path.join(RAIZ, f); if (fs.statSync(p).isFile() && /\.(php|js|css|html)$/.test(f)) fs.copyFileSync(p, path.join(tmp, f)); }
  for (const d of ["app", "guardia", "serums", "consulta"]) fs.cpSync(path.join(RAIZ, d), path.join(tmp, d), { recursive: true }); for (const d of ["bancos", "flujogramas"]) fs.symlinkSync(path.join(RAIZ, d), path.join(tmp, d));
  fs.mkdirSync(path.join(tmp, "t")); const puerto = await libre(), base = `http://127.0.0.1:${puerto}/`;
  const php = spawn("php", ["-S", `127.0.0.1:${puerto}`, "-t", tmp], { stdio: "ignore", env: { ...process.env, PHP_CLI_SERVER_WORKERS: "4", TMPDIR: path.join(tmp, "t") } }); await dormir(1200);
  const navegador = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined, args: ["--autoplay-policy=no-user-gesture-required"] }), errores = [], externas = [];
  const nueva = async ctx => { const p = await ctx.newPage(); p.on("pageerror", e => errores.push(String(e))); p.on("console", m => { if (m.type() === "error" && !/Failed to load resource/.test(m.text())) errores.push(m.text()); }); p.on("request", r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !/fonts\.(googleapis|gstatic)\.com/.test(r.url())) externas.push(r.url()); }); return p; };
  const pix = p => p.evaluate(() => { const c = document.querySelector(".is-intro__lienzo"), x = c.getContext("2d").getImageData(0, 0, c.width, c.height).data; let n = 0; for (let i = 3; i < x.length; i += 4) if (x[i] > 0) n++; return n; });
  const huella = p => p.evaluate(() => { const c = document.querySelector(".is-intro__lienzo"), u = c.toDataURL(); return u.length + ":" + u.slice(-80); });
  try {
    const ctx = await navegador.newContext({ viewport: { width: 1280, height: 800 } }); const p = await nueva(ctx), pedidos = []; p.on("response", r => { if (/guardia\/audio\//.test(r.url())) pedidos.push([r.url(), r.status()]); });
    for (const [clave, ruta, titulo, boton, monitores] of SERV) {
      await p.goto(base + "app/#/" + ruta); await p.waitForSelector("dialog.is-intro[data-servicio=" + clave + "]");
      ok(new RegExp(titulo, "i").test(await p.innerText(".is-intro h2")) && new RegExp(boton, "i").test(await p.innerText("[data-entrar]")), clave + ": título y botón");
      ok(await p.evaluate(() => document.activeElement && document.activeElement.hasAttribute("data-entrar")), clave + ": el foco inicial está en el botón de entrada");
      ok(/serums|intro-/.test(await p.getAttribute(".is-intro__img", "src")) && new RegExp("intro-" + clave).test(await p.getAttribute(".is-intro__img", "src")), clave + ": usa su imagen");
      await dormir(700); ok(await pix(p) > 300, clave + ": el lienzo dibuja"); const h1 = await huella(p); await dormir(350); ok(h1 !== await huella(p), clave + ": la animación avanza" + (monitores ? " (monitores en movimiento)" : ""));
      ok(pedidos.some(x => new RegExp(clave + "\\.mp3").test(x[0]) && x[1] === 200), clave + ": se carga su tema musical");
      const sn = await p.innerText(".is-intro__snd"); ok(/Sonido activado|Activar sonido/.test(sn), clave + ": control de sonido (" + sn + ")");
      if (/activado/.test(sn)) { await p.click(".is-intro__snd"); ok(/silenciado/.test(await p.innerText(".is-intro__snd")), clave + ": silencia"); await p.click(".is-intro__snd"); ok(/activado/.test(await p.innerText(".is-intro__snd")), clave + ": reactiva"); }
      await p.keyboard.press("Escape"); await dormir(150); ok(await p.locator("dialog.is-intro").count() === 0, clave + ": Escape cierra la introducción");
      ok(await p.evaluate(() => !Object.keys(localStorage).some(k => /intro/i.test(k) && localStorage.getItem(k) === "omitir")), clave + ": «Omitir» no guarda ninguna preferencia");
    }
    /* una vez por sesión y se puede volver a ver */
    for (const [clave, ruta] of SERV) { await p.goto(base + "app/#/inicio"); await p.waitForSelector("#vista .page"); await p.goto(base + "app/#/" + ruta); await dormir(700); ok(await p.locator("dialog.is-intro").count() === 0, clave + ": no se repite al volver dentro de la sesión"); }
    for (const [clave, ruta] of SERV) { await p.goto(base + "app/#/" + ruta); await p.reload(); await dormir(1200); ok(await p.locator("dialog.is-intro").count() === 0, clave + ": recargar la página no repite la introducción (misma sesión del navegador)"); }
    { const nc = await navegador.newContext({ viewport: { width: 1280, height: 800 } }); const np = await nueva(nc); for (const [clave, ruta] of SERV) { await np.goto(base + "app/#/" + ruta); await np.waitForSelector("dialog.is-intro[data-servicio=" + clave + "]", { state: "attached" }); ok(true, clave + ": en una ventana nueva (sesión nueva) la introducción se abre"); await np.keyboard.press("Escape"); await dormir(100); }
      ok(await np.evaluate(() => Object.keys(sessionStorage).filter(k => /^mqp_intro_/.test(k)).length) === 3, "las marcas viven en sessionStorage (3 servicios)"); await np.evaluate(() => window.MQP.olvidarIntros()); ok(await np.evaluate(() => Object.keys(sessionStorage).filter(k => /^mqp_(intro_|serums_intro)/.test(k)).length) === 0, "cerrar sesión borra las marcas");
      await np.goto(base + "app/#/inicio"); await np.waitForSelector("#vista .page"); await np.goto(base + "app/#/guardia/uci"); await np.waitForSelector("dialog.is-intro[data-servicio=uci]", { state: "attached" }); ok(true, "uci: tras cerrar sesión la introducción vuelve a abrirse"); await nc.close(); }
    ok(/olvidarIntros\(\); location\.hash = "#\/inicio"/.test(fs.readFileSync(path.join(RAIZ, "app/app.js"), "utf8")), "app.js borra las marcas al cerrar sesión");
    await p.goto(base + "app/#/guardia/uci"); await dormir(900); if (await p.locator("dialog.is-intro").count()) { await p.keyboard.press("Escape"); await dormir(150); } await p.waitForSelector("#gdVerIntro"); await p.click("#gdVerIntro"); await dormir(500); await p.waitForSelector("dialog.is-intro[data-servicio=uci]", { state: "attached" }); ok(true, "uci: «Ver la introducción» la vuelve a abrir"); await p.click("[data-omitir]"); await dormir(100);
    await p.goto(base + "app/#/guardia/emergencias"); await dormir(900); if (await p.locator("dialog.is-intro").count()) { await p.keyboard.press("Escape"); await dormir(150); } await p.waitForSelector("#gdVerIntro"); await p.click("#gdVerIntro"); await p.waitForSelector("dialog.is-intro[data-servicio=emergencias]"); ok(true, "emergencias: «Ver la introducción» la vuelve a abrir"); await p.click("[data-entrar]"); await dormir(100); ok(await p.locator(".gd-caso").count() === 10, "emergencias: el botón de entrada deja ver los casos");
    await p.goto(base + "app/#/consulta"); await dormir(900); if (await p.locator("dialog.is-intro").count()) { await p.keyboard.press("Escape"); await dormir(150); } await p.waitForSelector("#cqVerIntro"); await p.click("#cqVerIntro"); await p.waitForSelector("dialog.is-intro[data-servicio=consulta]"); ok(true, "consulta: «Ver la introducción» la vuelve a abrir"); await p.click("[data-entrar]");
    /* monitores: trazos y cifras dentro del cristal (emergencias y uci) */
    { const ce = await navegador.newContext({ viewport: { width: 1600, height: 900 } }); const e = await nueva(ce); await e.goto(base + "app/#/guardia/emergencias"); await e.waitForSelector("dialog.is-intro canvas"); await dormir(900);
      const col = await e.evaluate(() => { const c = document.querySelector(".is-intro__lienzo"), x = c.getContext("2d").getImageData(0, 0, c.width, c.height).data; let v = 0, a = 0, b = 0, w = 0, l = 0, r = 0; for (let i = 0; i < x.length; i += 4) { if (x[i + 3] < 200) continue; if (x[i + 2] > 230 && x[i + 1] > 190 && x[i] > 120 && x[i] < 200) l++; if (x[i] > 200 && x[i + 1] < 80) r++; } return [0, 0, 0, 0, l, r]; });
      ok(col[4] > 150 && col[5] < 15, "emergencias: solo se dibuja la línea del ECG sobre el monitor, sin interfaz repintada (" + col.join("/") + ")"); await ce.close(); }
    const cm = await navegador.newContext({ viewport: { width: 1600, height: 900 } }); const q = await nueva(cm);
    await q.goto(base + "app/#/guardia/uci"); await q.waitForSelector("dialog.is-intro canvas"); await dormir(900);
    const verde = await q.evaluate(() => { const c = document.querySelector(".is-intro__lienzo"), x = c.getContext("2d").getImageData(0, 0, c.width, c.height).data; let v = 0, r = 0, a = 0; for (let i = 0; i < x.length; i += 4) { if (x[i + 3] < 200) continue; if (x[i + 1] > 180 && x[i] < 120) v++; if (x[i] > 200 && x[i + 1] < 120) r++; if (x[i] > 200 && x[i + 1] > 180 && x[i + 2] < 120) a++; } return [v, r, a]; });
    ok(verde[0] > 80 && verde[1] > 40 && verde[2] > 40, "uci: el monitor dibuja el ECG verde, la saturación roja y la pletismografía/frecuencia amarillas (" + verde.join("/") + ")");
    await cm.close();
    /* reducir movimiento: un fotograma estático */
    const cr = await navegador.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion: "reduce" }); const r = await nueva(cr); await r.goto(base + "app/#/guardia/emergencias"); await r.waitForSelector("dialog.is-intro canvas"); await dormir(500);
    const a1 = await huella(r); await dormir(600); ok(a1 === await huella(r) && await pix(r) > 300, "reducir movimiento: se dibuja un fotograma sin animación"); await cr.close();
    /* móvil */
    const mv = await navegador.newContext({ viewport: { width: 390, height: 800 }, isMobile: true }); const m = await nueva(mv);
    for (const [clave, ruta] of SERV) { await m.goto(base + "app/#/" + ruta); await m.waitForSelector("dialog.is-intro[data-servicio=" + clave + "]"); await dormir(300); const o = await m.evaluate(() => { const d = document.querySelector("dialog.is-intro"); return [d.scrollWidth - d.clientWidth, document.querySelector("[data-entrar]").getBoundingClientRect().bottom <= innerHeight]; }); ok(o[0] <= 1 && o[1], "móvil " + clave + ": sin desbordamiento y con el botón visible"); await m.click("[data-omitir]"); await dormir(80); }
    await mv.close();
    /* accesibilidad */
    if (AXE) for (const esq of ["light", "dark"]) { const cx = await navegador.newContext({ viewport: { width: 1280, height: 800 }, colorScheme: esq }); const a = await nueva(cx);
      for (const [clave, ruta] of SERV) { await a.goto(base + "app/#/" + ruta); await a.waitForSelector("dialog.is-intro[data-servicio=" + clave + "]"); await dormir(1300); await a.evaluate(AXE); const res = await a.evaluate(() => axe.run(document, { runOnly: ["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"] })); const v = res.violations.filter(x => x.impact !== "minor"); if (v.length) console.log(esq, clave, v.map(x => x.id + ": " + x.nodes.slice(0, 2).map(n => n.target.join(" ")).join(";")).join(" | ")); ok(v.length === 0, "axe " + esq + " · " + clave); await a.keyboard.press("Escape"); await dormir(150); }
      await cx.close(); } else console.log("(axe omitido: define AXE_PATH)");
    ok(errores.length === 0, "sin errores de consola: " + errores.slice(0, 3).join(" | ")); ok(externas.length === 0, "sin peticiones externas: " + externas.slice(0, 3).join(" | "));
  } finally { await navegador.close(); php.kill(); fs.rmSync(tmp, { recursive: true, force: true }); }
  console.log(`intro_servicio_e2e: ${total - fallos}/${total} comprobaciones correctas`); process.exit(fallos ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
