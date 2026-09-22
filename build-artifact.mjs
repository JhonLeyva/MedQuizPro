/**
 * Genera artifact.html: la misma página en un solo archivo, con el CSS y el JS
 * incrustados, para publicarla donde solo se admite una página.
 *
 *   node build-artifact.mjs
 *
 * El widget de chat se excluye a propósito: necesita api.php (PHP) para hablar
 * con la IA, y un archivo suelto no tiene servidor detrás.
 *
 * Los bancos de bancos/*.json se incrustan en window.MQP_BANCOS, porque un
 * archivo suelto tampoco puede pedirlos con fetch.
 */
import { readFileSync, readdirSync, writeFileSync } from "node:fs";

const html = readFileSync("index.html", "utf8");
const css = readFileSync("styles.css", "utf8");
const js = readFileSync("main.js", "utf8");

const bancos = {};
for (const nombre of readdirSync("bancos").filter((n) => n.endsWith(".json")).sort()) {
  bancos[nombre.slice(0, -5)] = JSON.parse(readFileSync(`bancos/${nombre}`, "utf8"));
}
// "<" escapado para que ningún texto pueda cerrar la etiqueta <script>
const bancosJs = JSON.stringify(bancos).replace(/</g, "\\u003c");

const cuerpo = html
  .slice(html.indexOf("<body>") + "<body>".length, html.lastIndexOf("</body>"))
  .replace(/<!-- chat:inicio[\s\S]*?<!-- chat:fin -->\n?/, "")
  .replace(/<script[^>]*src="main\.js[^"]*"[^>]*><\/script>\n?/, "")
  .trim();

const fuentes = (html.match(/<link rel="stylesheet" href="https:\/\/fonts\.googleapis\.com[^"]*">/) || [""])[0];

const artifact = `<title>MedQuizPro</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
${fuentes}
<style>
${css.trim()}
</style>

${cuerpo}
<script>
window.MQP_BANCOS = ${bancosJs};
${js.trim()}
</script>
`;

writeFileSync("artifact.html", artifact);
console.log(`artifact.html generado (${(artifact.length / 1024).toFixed(1)} kB)`);
