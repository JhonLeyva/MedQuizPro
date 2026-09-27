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
  }
};
