/* Tarjeta 2 · Gineco-obstetricia / Hemorragia del tercer trimestre · Banco ENAM, Pregunta 654 (ENAM 2021 Extraordinario II)
 * Tipo de pregunta: diagnóstico diferencial + reconocimiento de gravedad. Ruta de razonamiento obstétrica.
 * Las variaciones «¿Y si…?» y la tabla comparativa se apoyan en otras preguntas reales del banco (P163, P377, P800, P1039).
 * ✎ = complemento editorial que no está en los comentarios fuente (pendiente de revisión médica). */
MQPFeedback.register({
  id: "p0654",
  numero: 654,
  examen: "ENAM 2021 Extraordinario II",
  especialidad: "Gineco-obstetricia",
  tema: "Hemorragia del tercer trimestre · DPP",
  tipo: "diagnóstico",

  enunciado:
    "Gestante de {{c1|34 semanas}} que ingresa a la emergencia con {{g1|trastorno del sensorio}}, {{d1|dolor intenso en abdomen}}. Al examen físico: {{g1|soporosa}}, afebril. {{c2|PA: 120/70 mmHg}}, {{g1|FC: 100 x’}}. {{c3|Altura uterina: 36 cm}}. {{d1|Útero con contracción sostenida}}. {{g2|No se auscultan latidos fetales}}. Genitales externos con evidencia de {{d1|sangrado rojo oscuro}} en {{c2|escasa cantidad}}. ¿Cuál es el diagnóstico?",

  alternativas: [
    {
      letra: "A", texto: "Desprendimiento prematuro de placenta",
      porQue: "Explica a la vez el dolor intenso, el útero en contracción sostenida y el sangrado oscuro."
    },
    {
      letra: "B", texto: "Placenta previa",
      porQue: "Produce sangrado **rojo brillante e indoloro** con útero blando. Aquí hay dolor intenso e hipertonía.",
      error: { inferido: true, texto: "Te guiaste por el sangrado del tercer trimestre, pero no integraste el **dolor intenso** ni el **útero en contracción sostenida**. La placenta previa sangra sin dolor y con útero blando." }
    },
    {
      letra: "C", texto: "Vasa previa",
      porQue: "También cursa con **sangrado indoloro** (comentario de P377). No explica el útero hipertónico.",
      error: { inferido: false, texto: "la vasa previa cursa con sangrado indoloro y no produce un útero en contracción sostenida ni dolor intenso." }
    },
    {
      letra: "D", texto: "Rotura uterina",
      porQue: "Da dolor y compromiso fetal, pero el útero **pierde su contorno** y el sangrado suele ser más masivo. Aquí el útero conserva su forma (contracción sostenida).",
      error: { inferido: true, texto: "Reconociste la gravedad (madre soporosa, feto sin latidos), pero ese dato no distingue el DPP de la rotura uterina. Lo que los distingue es **la forma del útero**: aquí está en contracción sostenida, sin pérdida de contorno ni partes fetales palpables." }
    },
    {
      letra: "E", texto: "Ceftriaxona",
      porQue: "Es un antibiótico, no un diagnóstico.",
      error: { inferido: false, texto: "es un fármaco, no un diagnóstico, y la paciente está afebril." }
    }
  ],
  correcta: "A",

  evalua: ["Diagnóstico diferencial del sangrado del 3.er trimestre", "Reconocimiento de gravedad materno-fetal"],
  aciertoClave: "lo que define el DPP es la combinación **dolor + útero hipertónico + sangrado oscuro**. La falta de latidos fetales indica gravedad, no el diagnóstico.",

  pistas: [
    { k: "d1", tipo: "decisivo", dato: "Dolor intenso + útero en contracción sostenida + sangrado rojo oscuro", significa: "Hemorragia **dolorosa con útero hipertónico**: DPP." },
    { k: "g1", tipo: "gravedad", dato: "Trastorno del sensorio, soporosa, FC 100 x’", significa: "**Compromiso materno.**" },
    { k: "g2", tipo: "gravedad", dato: "No se auscultan latidos fetales", significa: "Sufrimiento fetal severo o muerte fetal. Marca **gravedad**, no cambia el diagnóstico." },
    { k: "d1", tipo: "descarta", dato: "Útero con contracción sostenida", significa: "El útero conserva su forma: va contra la rotura uterina. Y el dolor va contra la placenta previa." },
    { k: "c2", tipo: "contexto", dato: "Sangrado escaso · PA 120/70 mmHg", significa: "**No tranquilizan.** El sangrado externo puede subestimar la pérdida real y la PA puede estar compensada." },
    { k: "c1", tipo: "contexto", dato: "34 semanas", significa: "Sangrado del tercer trimestre: DPP, placenta previa, vasa previa o rotura uterina." },
    { k: "c3", tipo: "contexto", dato: "Altura uterina 36 cm", significa: "No es el dato que decide. El comentario fuente no lo interpreta." }
  ],

  razonamiento: {
    ruta: "Gineco-obstetricia: contexto → diagnóstico → gravedad → estado materno y fetal",
    pasos: [
      { q: "Contexto", a: "Gestante de 34 semanas que sangra: **hemorragia del tercer trimestre**." },
      { q: "¿Duele? ¿Cómo está el útero?", a: "Dolor intenso y útero en contracción sostenida: **hemorragia dolorosa**. Queda entre DPP y rotura uterina." },
      { q: "¿El útero conserva su forma?", a: "Sí: contracción sostenida, sin partes fetales palpables. **DPP.**" },
      { q: "¿Qué tan grave es?", a: "Madre soporosa y feto sin latidos: **DPP grave**, emergencia obstétrica." }
    ],
    regla: {
      veo: "Sangrado oscuro + dolor + útero duro",
      pienso: "DPP. La forma del útero lo separa de la rotura",
      hago: "Valorar la gravedad por el estado materno y fetal"
    }
  },

  algoritmo: {
    titulo: "Sangrado vaginal en el tercer trimestre",
    nodes: [
      { id: "m1", row: 0, col: 0, kind: "start", lines: ["Sangrado vaginal", "3.er trimestre"], ruta: true, evidencia: ["34 semanas, sangrado", "rojo oscuro"] },
      { id: "m2", row: 1, col: 0, kind: "decision", lines: ["¿Dolor + útero", "hipertónico?"], ruta: true, evidencia: ["Dolor intenso,", "contracción sostenida"] },
      { id: "m2b", row: 1, col: 1, kind: "dx", lines: ["Indoloro, útero blando:", "placenta previa", "o vasa previa"], opciones: ["B", "C"] },
      { id: "m3", row: 2, col: 0, kind: "decision", lines: ["¿Útero sin contorno", "o partes fetales", "palpables?"], ruta: true, evidencia: ["Útero en contracción", "sostenida, forma conservada"] },
      { id: "m3b", row: 2, col: 1, kind: "dx", lines: ["Rotura uterina"], opciones: ["D"] },
      { id: "m4", row: 3, col: 0, kind: "dx", lines: ["Desprendimiento", "prematuro de placenta"], ruta: true, opciones: ["A"] },
      { id: "m5", row: 4, col: 0, kind: "decision", lines: ["¿Compromiso", "materno o fetal?"], ruta: true, evidencia: ["Soporosa, FC 100 x’,", "sin latidos fetales"] },
      { id: "m5b", row: 4, col: 1, kind: "action", lines: ["Feto sin compromiso por", "ahora: situación de", "riesgo, vigilar"] },
      { id: "m6", row: 5, col: 0, kind: "action", lines: ["DPP grave:", "emergencia obstétrica"], ruta: true, final: true }
    ],
    edges: [
      { from: "m1", to: "m2", label: "", ruta: true },
      { from: "m2", to: "m2b", label: "NO" },
      { from: "m2", to: "m3", label: "SÍ", ruta: true },
      { from: "m3", to: "m3b", label: "SÍ" },
      { from: "m3", to: "m4", label: "NO", ruta: true },
      { from: "m4", to: "m5", label: "", ruta: true },
      { from: "m5", to: "m5b", label: "NO" },
      { from: "m5", to: "m6", label: "SÍ", ruta: true }
    ],
    nota: "La pregunta pide el diagnóstico; el algoritmo termina en la gravedad. La conducta específica del DPP queda fuera de esta tarjeta porque el comentario fuente no la detalla."
  },

  porQueCorrecta: {
    resumen: "Es el único diagnóstico que explica **dolor intenso, útero en contracción sostenida y sangrado oscuro** a la vez.",
    texto: "El DPP produce una hemorragia dolorosa con útero hipertónico, y el sangrado oscuro y escaso es típico. La ausencia de latidos fetales y el sensorio alterado no apuntan a otro diagnóstico: indican que este DPP es grave. Según el comentario fuente, el compromiso de conciencia materno puede deberse a hipoperfusión o a dolor extremo."
  },

  trampas: [
    "**El sangrado escaso no excluye un DPP importante.** Parte de la sangre puede quedar retenida detrás de la placenta.✎",
    "**Una PA normal no descarta gravedad:** puede estar compensada al inicio (comentario de P377)."
  ],

  noConfundir: {
    titulo: "placenta previa y rotura uterina",
    columnas: ["Dolor", "Útero", "Sangrado", "Dato clave"],
    filas: [
      { dx: "DPP", esEste: true, celdas: ["Intenso", "Hipertónico, contracción sostenida", "Oscuro, puede ser escaso", "Dolor + útero duro"] },
      { dx: "Placenta previa", celdas: ["Ausente", "Blando, no doloroso", "Rojo brillante", "Sangrado indoloro"] },
      { dx: "Rotura uterina", celdas: ["Súbito, intenso", "Pierde su contorno; partes fetales palpables", "Más masivo", "Cesárea previa, pérdida de la forma uterina"] }
    ],
    nota: "Fuentes de la tabla: comentarios de P163, P654, P800 y P1039. La vasa previa también sangra sin dolor (comentario de P377)."
  },

  ySi: {
    original: { dato: "Dolor intenso + útero en contracción sostenida + sangrado oscuro", resultado: "DPP (A)" },
    variaciones: [
      {
        chip: "no doliera",
        cambio: "Sangrado **rojo brillante, indoloro**, con útero blando.",
        resultado: "Placenta previa",
        fuente: "Así lo describen los comentarios de P163 y P1039 del banco."
      },
      {
        chip: "se palparan partes fetales",
        cambio: "Cesárea previa, dolor súbito, **partes fetales palpables en el abdomen** y bradicardia fetal.",
        resultado: "Rotura uterina",
        fuente: "Es el caso de P800 del banco (ENAM 2021 Ordinario I)."
      },
      {
        chip: "hubiera latidos normales",
        cambio: "Útero persistentemente contraído y doloroso, pero **FCF 140 x’**.",
        resultado: "Sigue siendo DPP. El feto no está comprometido por ahora, pero la situación es de riesgo.",
        fuente: "Es el caso de P1039 del banco, cuya clave el banco marca como «verificar»."
      }
    ],
    variable: "el **dolor y el tono uterino** separan los grupos; la **forma del útero** separa el DPP de la rotura; el **estado materno y fetal** define la gravedad."
  },

  fisiopatologia: {
    titulo: "Hematoma retroplacentario",
    texto: [
      "La placenta se separa de la pared uterina antes del parto y se forma un hematoma entre ambas.✎",
      "Parte de la sangre queda retenida detrás de la placenta, así que el sangrado externo puede ser escaso aunque la pérdida sea importante. La irritación del miometrio explica el dolor y el útero hipertónico.✎",
      "Al separarse la placenta se pierde superficie de intercambio con el feto: de ahí el sufrimiento fetal y, si la separación es extensa, la muerte fetal.✎"
    ],
    figura: "dpp",
    pie: "Esquema. Morado: placenta. Rojo: sangre. En el DPP gran parte de la sangre queda oculta; en la placenta previa la placenta cubre el cuello."
  },

  recuerda: [
    "Sangrado + dolor + útero hipertónico = **DPP** hasta demostrar lo contrario.",
    "**Sangrado escaso y PA normal** no descartan gravedad.",
    "La **forma del útero** separa el DPP de la rotura uterina."
  ],

  comprueba: {
    pregunta: "En el mismo caso, ¿cuál de estos datos añadidos te haría **cambiar el diagnóstico** de DPP a rotura uterina?",
    opciones: [
      { letra: "A", texto: "Sangrado vaginal escaso" },
      { letra: "B", texto: "PA 120/70 mmHg" },
      { letra: "C", texto: "Partes fetales palpables en el abdomen y antecedente de cesárea" },
      { letra: "D", texto: "Ausencia de latidos fetales" }
    ],
    correcta: "C",
    explicacion: "La forma del útero es lo que separa el DPP de la rotura uterina (P800). A y B no descartan un DPP: son las trampas de este tema. D puede aparecer en ambos cuadros: marca gravedad, no diagnóstico."
  },

  fuenteCorta: "Fuente: Banco ENAM – Respuestas resaltadas, Pregunta 654 (ENAM 2021 Extraordinario II): enunciado, clave y comentario. Variaciones y tabla: P163, P377, P800 y P1039 del mismo banco.",
  fuentes: [
    "Banco ENAM – Respuestas resaltadas, **Pregunta 654** (ENAM 2021 Extraordinario II): enunciado, alternativas, clave A y comentario. Base de las pistas, el razonamiento, la explicación y los motivos de B y D.",
    "**Pregunta 163** (ENAM 2020 Extraordinario I): placenta previa con sangrado rojo brillante y sin dolor.",
    "**Pregunta 377** (ENAM 2021 Extraordinario I): la PA normal no descarta gravedad; placenta previa y vasa previa cursan con sangrado indoloro.",
    "**Pregunta 800** (ENAM 2021 Ordinario I): rotura uterina con partes fetales palpables, cesárea previa y pérdida de la forma uterina.",
    "**Pregunta 1039** (ENAM 2022 Extraordinario I): DPP con FCF 140 x’ y útero blando en la placenta previa."
  ],
  revision: [
    "El comentario de P654 dice «dolor abdominal súbito», pero la viñeta solo dice «dolor intenso». La tarjeta no usa «súbito».",
    "La alternativa E («Ceftriaxona») no es un diagnóstico. Parece un distractor de relleno: el banco indica que se añadió una opción E.",
    "La altura uterina (36 cm a las 34 semanas) no se interpreta en el comentario. Se muestra como dato no decisivo.",
    "La variación «latidos normales» se apoya en P1039, que el banco marca «⚠ Verificar» (clave inferida con ambigüedad).",
    "El mecanismo del sangrado oculto y de la hipertonía (✎) es complemento editorial: revisar con bibliografía obstétrica antes de publicar."
  ],
  qa: [
    { t: "Pregunta original visible, con la respuesta del estudiante y la correcta" },
    { t: "Clave A coherente con el comentario fuente" },
    { t: "Pistas separadas: diagnóstico (dolor + hipertonía) frente a gravedad (madre y feto)" },
    { t: "Razonamiento adaptado a obstetricia: contexto → diagnóstico → gravedad" },
    { t: "Ruta del paciente resaltada; B, C y D ubicadas en el algoritmo" },
    { t: "Variaciones «¿Y si…?» tomadas de preguntas reales del banco" },
    { t: "Error inferido solo en B y D; C y E con explicación neutra" },
    { t: "Esquema solo en «¿Por qué ocurre?»; la viñeta no trae imagen" },
    { t: "Mini comprobación de transferencia, no de memoria literal" },
    { t: "Inconsistencia del comentario («súbito») y opción E marcadas", flag: true }
  ]
});
