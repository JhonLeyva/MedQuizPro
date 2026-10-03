# Feedback clínico visual post-pregunta (prototipo)

Módulo que aparece **después** de que el estudiante responde una pregunta de MedQuizPlus. No es un resumen del tema: se construye alrededor de la pregunta que acaba de responder y de la alternativa que eligió.

Abrir `index.html` en el navegador. No necesita servidor ni build.

## Las 2 tarjetas de ejemplo

| Tarjeta | Pregunta del banco | Tipo | Especialidad | Respuesta simulada |
|---|---|---|---|---|
| `cards/p0008.js` | P8 · ENAM 2020 Ext. I | Conducta (manejo inicial) | Cirugía · trauma torácico | C, incorrecta (muestra el flujo de error) |
| `cards/p0654.js` | P654 · ENAM 2021 Ext. II | Diagnóstico diferencial + gravedad | Gineco-obstetricia · DPP | A, correcta (muestra el flujo de acierto) |

En la demo se puede cambiar la respuesta simulada (A–E o «Sin dato») para ver cómo cambia el módulo con cada alternativa.

## Infografías SVG (formato de las imágenes MedQuizPlus)

`svg/` contiene la versión estática de cada tarjeta, en el mismo estilo que las infografías actuales: 1000 px de ancho, cabecera verde azulado y caja amarilla de puntos clave. Se generan desde los mismos datos de `cards/`:

```bash
node feedback/svg/generar-svg.js              # *-revision.svg: con las marcas ✎ para la revisión médica
node feedback/svg/generar-svg.js --publicar   # *.svg: sin marcas, para estudiantes
```

Como el SVG es estático, no sabe qué letra marcó el estudiante. Por eso la tabla «Opciones de la pregunta» explica cada alternativa y qué revisar si la marcaste. El generador ajusta los textos y el alto de cada caja automáticamente. Se verificó en Chromium que ningún texto supera el ancho de su caja.

## Integración en la plataforma

```html
<link rel="stylesheet" href="mqp-feedback.css">
<script src="mqp-feedback.js"></script>
<script src="cards/p0008.js"></script>
<script>
  const card = MQPFeedback.cards().find(c => c.id === "p0008");
  MQPFeedback.render(document.getElementById("feedback"), card, {
    seleccion: "C",   // letra que eligió el estudiante (null si no se conoce)
    modo: "learn"     // "quick" | "learn" | "check"
  });
</script>
```

## Modos

| Modo | Muestra |
|---|---|
| ⚡ Explicación rápida | Pregunta, resultado, error (si falló), pistas decisivas, regla «si veo → pienso → hago», 3 cosas para recordar |
| 📖 Aprender | Todo. Lo secundario (fisiopatología, diagnóstico diferencial, fuentes) queda plegado |
| 🔄 Comprobar | Oculta pistas, razonamiento y motivos de cada alternativa hasta que el estudiante los pide; la ruta del algoritmo se revela paso a paso |

## Esquema de una tarjeta

| Campo | Contenido |
|---|---|
| `enunciado` | Texto literal del banco. `{{clave\|texto}}` resalta una pista en la viñeta |
| `alternativas[]` | `letra`, `texto`, `porQue` (por qué sí o no) y `error` (qué mostrar si el estudiante la eligió). `error.inferido: false` cuando no hay base para suponer su razonamiento: entonces se muestra «Esta alternativa no es correcta porque…» |
| `pistas[]` | `k` (enlaza con la viñeta), `tipo` (`decisivo`, `gravedad`, `contexto`, `descarta`), `dato`, `significa` |
| `razonamiento` | `ruta` (la secuencia propia de la especialidad), `pasos[]` y `regla` (veo / pienso / hago) |
| `algoritmo` | `nodes[]` (`row`, `col`, `kind`: `start`, `decision`, `action`, `dx`; `ruta`, `evidencia`, `opciones`) y `edges[]`. El SVG se genera solo: la ruta del paciente sale en verde y cada alternativa aparece donde sería correcta |
| `ySi` | Caso original + variaciones de **un** dato + la variable que gobierna el algoritmo |
| `trampas`, `noConfundir`, `fisiopatologia` | Opcionales: solo se incluyen si aportan |
| `recuerda` | 3 a 5 puntos transferibles |
| `comprueba` | Mini pregunta con una variable cambiada |
| `fuentes`, `revision`, `qa` | Trazabilidad y control de calidad |

`✎` dentro de un texto marca un **complemento editorial**: algo que no está en el comentario fuente. Se ve en la tarjeta y debe pasar revisión médica antes de publicar.

## Código de color (fijo en todas las tarjetas)

| Color | Significado |
|---|---|
| Verde | Respuesta correcta, ruta del paciente |
| Rojo | Error del estudiante, dato de gravedad |
| Naranja | Dato decisivo, trampa |
| Azul | Contexto, diagnóstico |
| Morado | Dato que descarta otras opciones, variable que gobierna |

Formas del algoritmo: rombo = decisión, rectángulo = acción, rectángulo discontinuo azul = diagnóstico, cápsula = punto de partida.

## Hallazgos para revisión

Encontrados al construir las dos tarjetas. No se corrigieron en silencio: están marcados dentro de cada tarjeta, en «Fuentes y control de calidad».

1. **Opción E de relleno.** El banco indica que se añadió una opción E, y en varias preguntas no tiene sentido clínico (P654: «Ceftriaxona» como diagnóstico; P8: «Lavado quirúrgico»). Conviene revisar todas las opciones E antes de procesar las 2380 preguntas.
2. **Comentario de P654 frente a la viñeta.** El comentario habla de «dolor abdominal súbito», pero la viñeta solo dice «dolor intenso».
3. **P8 sin SatO₂ ni gasometría.** La insuficiencia respiratoria se infiere de la clínica. El comentario descarta hemotórax, pero no menciona neumotórax.
4. **P1039**, usada en una variación de la tarjeta 2, tiene la clave marcada «⚠ Verificar» en el banco.
5. Los PDF «ENAM COMENTADO 2026» son imágenes escaneadas de material de VillaMedic, sin texto extraíble. Las tarjetas usan solo el banco con texto (`Banco_ENAM_Respuestas_Resaltadas.pdf`).

## Siguiente paso

Validar estas 2 tarjetas. Después, construir las 20 representativas (cirugía, medicina interna, GO, pediatría, cardiología, radiología, dermatología, farmacología, anatomía, laboratorio) con este mismo esquema y revisarlas con las 12 preguntas de validación antes de procesar el banco completo.
