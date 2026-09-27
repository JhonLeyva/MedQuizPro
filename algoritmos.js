/* MedQuizPlus — registro de algoritmos / flujogramas del simulador.
 *
 * El botón "Ver algoritmo / Flujograma" busca aquí, en este orden:
 *   1. el id de la pregunta     (p. ej. "CAR-001")
 *   2. el nombre de la especialidad tal como viene en el banco (p. ej. "Cardiología")
 * Si no encuentra nada, el modal muestra un esquema de ejemplo.
 *
 * Cada entrada admite cualquier combinación de:
 *   titulo  — encabezado del modal
 *   imagen  — ruta a una imagen (p. ej. "algoritmos/car-001.webp"); alt — texto alternativo
 *   pasos   — flujograma dibujado en HTML: [{ texto, tipo }], tipo = inicio | decision | accion | fin
 *   nota    — perla clínica en texto
 *
 * Para añadir uno nuevo, copia el bloque de ejemplo y cambia la clave.
 */
window.MQP_ALGORITMOS = {
  "CAR-001": {
    titulo: "Infarto inferior con compromiso del ventrículo derecho",
    pasos: [
      { texto: "IAM inferior (ST↑ en DII, DIII, aVF) + hipotensión", tipo: "inicio" },
      { texto: "¿ST↑ en V4R · ingurgitación yugular · pulmones limpios?", tipo: "decision" },
      { texto: "Infarto de VD: suspender nitratos y diuréticos", tipo: "accion" },
      { texto: "Expansión de volumen con cristaloides", tipo: "accion" },
      { texto: "Reperfusión urgente (angioplastia primaria o fibrinólisis)", tipo: "fin" }
    ],
    nota: "El VD infartado depende de la precarga: todo lo que la reduce (nitratos, diuréticos, morfina) puede precipitar el shock."
  },

  /* ---------- ENAM 2020 · preguntas oficiales ---------- */

  "OFT-002": {
    titulo: "Quemadura química ocular aguda",
    imagen: "flujogramas/quemadura-quimica-ocular-aguda.svg",
    alt: "Flujograma de manejo de la quemadura química ocular aguda"
  },
  "PED-003": {
    titulo: "Dismorfología y cardiopatías en la trisomía 21",
    imagen: "flujogramas/dismorfologia-cardiopatias-trisomia-21.svg",
    alt: "Flujograma de rasgos dismórficos y cardiopatías asociadas a la trisomía 21"
  },
  "CIR-003": {
    titulo: "Trauma torácico cerrado",
    imagen: "flujogramas/trauma-toracico-cerrado.svg",
    alt: "Flujograma de manejo inicial del trauma torácico cerrado"
  },
  "INF-002": {
    titulo: "Virología: virus respiratorios",
    imagen: "flujogramas/virologia-virus-respiratorios.svg",
    alt: "Flujograma de clasificación de los virus respiratorios"
  },
  "GIN-003": {
    titulo: "Distocia en fase activa con compromiso fetal",
    imagen: "flujogramas/distocia-fase-activa-compromiso-fetal.svg",
    alt: "Flujograma de manejo de la distocia en fase activa con compromiso fetal"
  },
  "CIR-002": {
    titulo: "Abdomen agudo en pediatría",
    imagen: "flujogramas/abdomen-agudo-pediatria.svg",
    alt: "Flujograma diagnóstico del abdomen agudo en pediatría"
  },
  "PED-002": {
    titulo: "Monoartritis aguda en pediatría",
    imagen: "flujogramas/monoartritis-aguda-pediatria.svg",
    alt: "Flujograma diagnóstico de la monoartritis aguda en pediatría"
  },
  "NRL-002": {
    titulo: "Cefalea súbita: hemorragia subaracnoidea",
    imagen: "flujogramas/cefalea-subita-hemorragia-subaracnoidea.svg",
    alt: "Flujograma de estudio de la cefalea súbita y la hemorragia subaracnoidea"
  },
  "REU-002": {
    titulo: "Diagnóstico diferencial de la ictericia",
    imagen: "flujogramas/diagnostico-diferencial-ictericia.svg",
    alt: "Flujograma de diagnóstico diferencial de la ictericia y la coloración amarillenta de la piel"
  },
  "GIN-002": {
    titulo: "Rotura prematura de membranas",
    imagen: "flujogramas/rotura-prematura-membranas.svg",
    alt: "Flujograma de manejo de la rotura prematura de membranas"
  }
};
