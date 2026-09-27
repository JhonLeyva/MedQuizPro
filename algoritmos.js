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
  },

  /* ---------- ENAM 2020 · preguntas 22 a 31 ---------- */

  "PED-004": {
    titulo: "Membrana hialina (SDR neonatal)",
    imagen: "flujogramas/membrana-hialina-sdra-neonatal.svg",
    alt: "Flujograma diagnóstico de la enfermedad de membrana hialina o síndrome de dificultad respiratoria neonatal"
  },
  "HEM-002": {
    titulo: "Anemia ferropénica: perfil de hierro",
    imagen: "flujogramas/anemia-ferropenica-perfil-hierro.svg",
    alt: "Flujograma de interpretación del perfil de hierro en la anemia ferropénica"
  },
  "NEF-002": {
    titulo: "Hiperpotasemia: manejo de urgencia",
    imagen: "flujogramas/hiperpotasemia-manejo-urgencia.svg",
    alt: "Flujograma de manejo de urgencia de la hiperpotasemia"
  },
  "GIN-004": {
    titulo: "Hipertensión gestacional: diagnóstico",
    imagen: "flujogramas/hipertension-gestacional-diagnostico.svg",
    alt: "Flujograma diagnóstico de la hipertensión gestacional"
  },
  "SP-002": {
    titulo: "Parto humanizado con enfoque intercultural",
    imagen: "flujogramas/parto-humanizado-intercultural.svg",
    alt: "Flujograma de atención del parto humanizado con enfoque intercultural"
  },
  "GIN-005": {
    titulo: "Preeclampsia con criterios de severidad",
    imagen: "flujogramas/preeclampsia-con-criterios-severidad.svg",
    alt: "Flujograma de criterios de severidad de la preeclampsia"
  },
  "NRL-003": {
    titulo: "Hematoma epidural de fosa posterior",
    imagen: "flujogramas/hematoma-epidural-fosa-posterior.svg",
    alt: "Flujograma de manejo del hematoma epidural de fosa posterior"
  },
  "REU-003": {
    titulo: "Artritis reumatoide: anticuerpos anti-CCP",
    imagen: "flujogramas/artritis-reumatoide-anticuerpos-anti-ccp.svg",
    alt: "Flujograma diagnóstico de la artritis reumatoide con anticuerpos anti-CCP"
  },
  "INF-003": {
    titulo: "Mononucleosis infecciosa (virus de Epstein-Barr)",
    imagen: "flujogramas/mononucleosis-infecciosa-veb.svg",
    alt: "Flujograma diagnóstico de la mononucleosis infecciosa por virus de Epstein-Barr"
  },
  "PED-005": {
    titulo: "Rubéola: diagnóstico exantemático",
    imagen: "flujogramas/rubeola-diagnostico-exantematico.svg",
    alt: "Flujograma de diagnóstico diferencial de exantemas y rubéola"
  }
};
