/* Tarjeta 1 · Cirugía / Trauma torácico · Banco ENAM, Pregunta 8 (ENAM 2020 Extraordinario I)
 * Tipo de pregunta: conducta (manejo inicial). Ruta de razonamiento quirúrgica.
 * ✎ = complemento editorial que no está en el comentario fuente (pendiente de revisión médica). */
MQPFeedback.register({
  id: "p0008",
  numero: 8,
  examen: "ENAM 2020 Extraordinario I",
  especialidad: "Cirugía",
  tema: "Trauma torácico · Tórax inestable",
  tipo: "conducta",

  enunciado:
    "Mujer de 34 años por accidente de tránsito presenta {{k5|contusión en hemitórax izquierdo}}. Al examen: {{k1|disneica}}, {{k4|FC: 105 x’}}, {{k1|FR: 27 x’}}, {{k4|PA: 110/60 mmHg}}, dolor a la palpación en pared costal y {{k1|disminución en murmullo vesicular en HTI}}. Radiografía de tórax muestra {{k2|2 trazos de fractura del 2° al 6° arco costal izquierdo}} con {{k3|ángulos costofrénicos libres}}. ¿Cuál es el manejo inicial?",

  alternativas: [
    {
      letra: "A", texto: "Tomografía torácica contrastada",
      porQue: "Es un estudio diagnóstico. Con compromiso ventilatorio, primero se asegura la vía aérea y la ventilación; los estudios vienen después.✎",
      error: { inferido: true, texto: "Priorizaste completar el diagnóstico. En trauma, la vía aérea y la ventilación se estabilizan antes de llevar a la paciente a un estudio.✎" }
    },
    {
      letra: "B", texto: "Drenaje quirúrgico torácico",
      porQue: "Se indica si hay hemotórax o neumotórax. La Rx muestra **ángulos costofrénicos libres** y no describe ocupación pleural.",
      error: { inferido: true, texto: "Interpretaste la disminución del murmullo vesicular como líquido o aire en la pleura. Pero la Rx muestra ángulos costofrénicos libres: aquí la ↓MV se explica por **hipoventilación**." }
    },
    {
      letra: "C", texto: "Analgesia óptima",
      porQue: "Es la base del manejo de las fracturas costales y también se usa aquí, pero **no basta**: ya hay insuficiencia respiratoria.",
      error: { inferido: true, texto: "Reconociste las fracturas costales y elegiste su tratamiento base. Lo que faltó fue darle peso a los signos de **insuficiencia respiratoria** (disnea, FR 27 x’, ↓MV): son ellos los que cambian la conducta." }
    },
    {
      letra: "D", texto: "Intubación orotraqueal",
      porQue: "Hay tórax inestable con compromiso ventilatorio: asegurar la vía aérea y la ventilación es la prioridad."
    },
    {
      letra: "E", texto: "Lavado quirúrgico",
      porQue: "No hay herida ni contaminación descrita: no corresponde a un trauma torácico cerrado.",
      error: { inferido: false, texto: "no hay herida abierta ni contaminación que lavar en un trauma torácico cerrado. El problema que amenaza la vida aquí es ventilatorio." }
    }
  ],
  correcta: "D",

  evalua: ["Elección del manejo inicial", "Identificación de gravedad"],
  aciertoClave: "el dato que decide **no es el número de costillas**, sino la **insuficiencia respiratoria**.",

  pistas: [
    { k: "k2", tipo: "decisivo", etiqueta: "Dato decisivo · diagnóstico", dato: "2 trazos de fractura del 2.° al 6.° arco", significa: "5 costillas contiguas rotas en 2 sitios: **tórax inestable**." },
    { k: "k1", tipo: "decisivo", etiqueta: "Dato decisivo · conducta", dato: "Disnea + FR 27 x’ + ↓MV en HTI", significa: "**Compromiso ventilatorio.** Es el dato que indica intubar." },
    { k: "k3", tipo: "descarta", dato: "Ángulos costofrénicos libres", significa: "Sin hemotórax ni derrame en la Rx: descarta el drenaje (B)." },
    { k: "k4", tipo: "contexto", dato: "PA 110/60 mmHg · FC 105 x’", significa: "Presión conservada: la viñeta pone el foco en la ventilación, no en la volemia." },
    { k: "k5", tipo: "contexto", dato: "Accidente de tránsito, contusión en HTI", significa: "Trauma torácico cerrado." }
  ],

  razonamiento: {
    ruta: "Cirugía: caso → estabilidad → diagnóstico → indicación → conducta",
    pasos: [
      { q: "¿Qué tiene?", a: "**Tórax inestable**: 5 arcos costales con 2 trazos de fractura." },
      { q: "¿Qué tan grave es?", a: "**Compromiso ventilatorio**: disnea, FR 27 x’ y ↓MV en el lado afectado." },
      { q: "¿Qué dato cambia la conducta?", a: "La **insuficiencia respiratoria**. Las fracturas definen el diagnóstico; la respiración define la conducta." },
      { q: "¿Qué hago?", a: "Asegurar vía aérea y ventilación: **intubación orotraqueal** y soporte ventilatorio." }
    ],
    regla: {
      veo: "Tórax inestable + disnea, taquipnea y ↓MV",
      pienso: "Falla ventilatoria por pared inestable, dolor y fatiga",
      hago: "Intubación orotraqueal + ventilación mecánica"
    }
  },

  algoritmo: {
    titulo: "Fracturas costales en trauma torácico cerrado",
    nodes: [
      { id: "n1", row: 0, col: 0, kind: "start", lines: ["Trauma torácico cerrado"], ruta: true, evidencia: ["Accidente de tránsito,", "contusión en HTI"] },
      { id: "n2", row: 1, col: 0, kind: "decision", lines: ["¿≥2 costillas contiguas", "fracturadas en ≥2 sitios?"], ruta: true, evidencia: ["Rx: 2 trazos de fractura", "del 2.° al 6.° arco"] },
      { id: "n2b", row: 1, col: 1, kind: "action", lines: ["Fracturas costales simples:", "analgesia y vigilancia"] },
      { id: "n3", row: 2, col: 0, kind: "dx", lines: ["Tórax inestable"], ruta: true },
      { id: "n4", row: 3, col: 0, kind: "decision", lines: ["¿Hemotórax o", "neumotórax en la Rx?"], ruta: true, evidencia: ["Ángulos costofrénicos", "libres"] },
      { id: "n4b", row: 3, col: 1, kind: "action", lines: ["Drenaje torácico", "y reevaluar"], opciones: ["B"] },
      { id: "n5", row: 4, col: 0, kind: "decision", lines: ["¿Insuficiencia", "respiratoria?"], ruta: true, evidencia: ["Disnea, FR 27 x’,", "↓MV en HTI"] },
      { id: "n5b", row: 4, col: 1, kind: "action", lines: ["O₂ + analgesia óptima", "y vigilancia estrecha"], opciones: ["C"] },
      { id: "n6", row: 5, col: 0, kind: "action", lines: ["Intubación orotraqueal", "+ ventilación mecánica"], ruta: true, final: true, opciones: ["D"] }
    ],
    edges: [
      { from: "n1", to: "n2", label: "", ruta: true },
      { from: "n2", to: "n2b", label: "NO" },
      { from: "n2", to: "n3", label: "SÍ", ruta: true },
      { from: "n3", to: "n4", label: "", ruta: true },
      { from: "n4", to: "n4b", label: "SÍ" },
      { from: "n4", to: "n5", label: "NO", ruta: true },
      { from: "n5", to: "n5b", label: "NO" },
      { from: "n5", to: "n6", label: "SÍ", ruta: true }
    ],
    nota: "A (TAC) y E (lavado) no aparecen en la ruta: ninguna rama de este algoritmo lleva a ellas en un paciente con compromiso ventilatorio. Esquema simplificado para este caso.✎"
  },

  porQueCorrecta: {
    resumen: "Hay **tórax inestable con insuficiencia respiratoria**: lo urgente es asegurar la ventilación.",
    texto: "La pared torácica inestable y el dolor producen hipoventilación y fatiga respiratoria, y la viñeta ya muestra los signos: disnea, FR 27 x’ y ↓MV. La intubación orotraqueal controla la vía aérea, mejora la oxigenación y, con ventilación a presión positiva, estabiliza mecánicamente el segmento inestable."
  },

  trampas: [
    "**Tórax inestable no significa intubación automática.** Lo que indica la intubación es la insuficiencia respiratoria, no el número de costillas fracturadas.",
    "**↓MV no siempre es líquido o aire en la pleura.** Con ángulos costofrénicos libres, aquí refleja hipoventilación."
  ],

  ySi: {
    original: { dato: "Tórax inestable + disnea, FR 27 x’, ↓MV", resultado: "Intubación orotraqueal (D)" },
    variaciones: [
      {
        chip: "respira bien",
        cambio: "Mismo tórax inestable, pero **eupneica, FR normal y buena oxigenación**.",
        resultado: "O₂ + analgesia óptima + vigilancia estrecha. La opción C pasa a ser razonable.✎"
      },
      {
        chip: "la Rx muestra hemotórax",
        cambio: "Ángulo costofrénico **velado** en la Rx.",
        resultado: "Hay ocupación pleural: el drenaje torácico (B) entra en la conducta, además de manejar la ventilación.✎"
      }
    ],
    variable: "el **estado respiratorio**. El mismo tórax inestable puede manejarse con analgesia u oxígeno, o con intubación, según cómo respire la paciente."
  },

  fisiopatologia: {
    titulo: "Movimiento paradójico",
    texto: [
      "Cuando varias costillas contiguas se rompen en dos sitios, queda un segmento de pared que ya no está unido al resto.✎",
      "En la inspiración, la presión negativa lo **hunde**; en la espiración, **protruye**. El segmento se mueve al revés que el resto del tórax, y la ventilación pierde eficacia. El dolor limita además la respiración profunda, lo que favorece la hipoventilación y la fatiga.✎",
      "La ventilación con presión positiva empuja el segmento hacia afuera desde dentro y lo estabiliza: por eso la intubación también trata la mecánica, no solo la oxigenación."
    ],
    figura: "flail",
    pie: "Esquema en corte transversal. Naranja: segmento inestable. Rojo: su movimiento. Gris: el resto de la pared."
  },

  recuerda: [
    "Tórax inestable = **≥2 costillas contiguas fracturadas en ≥2 sitios**.✎",
    "La conducta la decide la **función respiratoria**, no el número de fracturas.",
    "Ángulos costofrénicos libres = la Rx **no muestra hemotórax**: no hay indicación de drenaje por ese motivo."
  ],

  comprueba: {
    pregunta: "Otro paciente con el mismo mecanismo tiene fracturas del 3.° al 6.° arco, cada una en dos sitios. Está **eupneico, FR 16 x’, SatO₂ 97 %**, y la Rx no muestra ocupación pleural. ¿Cuál es la conducta inicial más adecuada?",
    opciones: [
      { letra: "A", texto: "Intubación orotraqueal, porque tiene tórax inestable" },
      { letra: "B", texto: "O₂, analgesia óptima y vigilancia estrecha" },
      { letra: "C", texto: "Drenaje torácico" },
      { letra: "D", texto: "Tomografía antes de cualquier medida" }
    ],
    correcta: "B",
    explicacion: "El diagnóstico es el mismo (tórax inestable), pero falta la variable que indicaba intubar: la insuficiencia respiratoria. Sin ocupación pleural no hay indicación de drenaje. Si el paciente empeora, se reevalúa la ventilación.✎"
  },

  fuenteCorta: "Fuente: Banco ENAM – Respuestas resaltadas, Pregunta 8 (ENAM 2020 Extraordinario I): enunciado, clave y comentario.",
  fuentes: [
    "Banco ENAM – Respuestas resaltadas, **Pregunta 8** (ENAM 2020 Extraordinario I): enunciado, alternativas, clave D y comentario. Base de la explicación, las pistas, el razonamiento y los motivos de B y C.",
    "Los complementos marcados con ✎ (definición de tórax inestable, mecanismo paradójico, prioridad de la vía aérea frente a la TAC, variaciones del caso) no están en el comentario fuente."
  ],
  revision: [
    "La viñeta no reporta SatO₂ ni gasometría. La insuficiencia respiratoria se infiere de disnea, FR 27 x’ y ↓MV, igual que en el comentario fuente.",
    "El comentario descarta hemotórax y derrame por los ángulos libres, pero no menciona neumotórax. La rama «no drenaje» asume una Rx sin neumotórax.",
    "La alternativa E («Lavado quirúrgico») no guarda relación con el caso. Parece un distractor de relleno: el banco indica que se añadió una opción E.",
    "Revisar con bibliografía de trauma (p. ej., ATLS) los complementos ✎ antes de publicar."
  ],
  qa: [
    { t: "Pregunta original visible, con la respuesta del estudiante y la correcta" },
    { t: "Clave D coherente con el comentario fuente" },
    { t: "Pistas separadas en diagnóstico (fracturas) y conducta (respiración)" },
    { t: "Razonamiento datos → diagnóstico → gravedad → conducta" },
    { t: "Ruta del paciente resaltada; las otras opciones ubicadas en el algoritmo" },
    { t: "Cada alternativa incorrecta justificada" },
    { t: "Error del estudiante solo inferido cuando la opción lo permite (E: explicación neutra)" },
    { t: "Esquema solo en «¿Por qué ocurre?»; la viñeta no trae imagen" },
    { t: "Mini comprobación con una variable cambiada, no la misma pregunta" },
    { t: "Complementos ✎ y datos faltantes marcados para revisión", flag: true }
  ]
});
