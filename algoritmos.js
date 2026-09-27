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
  },

  /* ---------- ENAM 2020 · preguntas 32 a 51 ---------- */

  "END-002": {
    titulo: "Hipotiroidismo subclínico: diagnóstico",
    imagen: "flujogramas/hipotiroidismo-subclinico-diagnostico.svg",
    alt: "Flujograma diagnóstico del hipotiroidismo subclínico"
  },
  "GIN-006": {
    titulo: "Mastitis puerperal: manejo",
    imagen: "flujogramas/mastitis-puerperal-manejo.svg",
    alt: "Flujograma de manejo de la mastitis puerperal"
  },
  "GAS-002": {
    titulo: "Diarrea disentérica: antibioticoterapia",
    imagen: "flujogramas/diarrea-disenterica-antibioticoterapia.svg",
    alt: "Flujograma de manejo antibiótico de la diarrea disentérica"
  },
  "SP-003": {
    titulo: "Consejería nutricional en la gestante",
    imagen: "flujogramas/consejeria-nutricional-gestante.svg",
    alt: "Flujograma de consejería nutricional en la gestante"
  },
  "PED-006": {
    titulo: "Diarrea invasiva por Campylobacter en el lactante",
    imagen: "flujogramas/diarrea-invasiva-campylobacter-lactante.svg",
    alt: "Flujograma de la diarrea invasiva por Campylobacter en el lactante"
  },
  "GIN-007": {
    titulo: "Pielonefritis aguda en la gestación",
    imagen: "flujogramas/pielonefritis-aguda-gestacion.svg",
    alt: "Flujograma de manejo de la pielonefritis aguda en la gestación"
  },
  "OFT-003": {
    titulo: "Glaucoma congénito: goniotomía",
    imagen: "flujogramas/glaucoma-congenito-goniotomia.svg",
    alt: "Flujograma diagnóstico y terapéutico del glaucoma congénito"
  },
  "INF-004": {
    titulo: "Chancro luético: sífilis primaria",
    imagen: "flujogramas/chancro-luetico-sifilis-primaria.svg",
    alt: "Flujograma diagnóstico del chancro luético en la sífilis primaria"
  },
  "END-003": {
    titulo: "Tormenta tiroidea: crisis tirotóxica",
    imagen: "flujogramas/tormenta-tiroidea-crisis-tirotoxica.svg",
    alt: "Flujograma de manejo de la tormenta tiroidea"
  },
  "GAS-003": {
    titulo: "Pancreatitis crónica: bloqueo celíaco",
    imagen: "flujogramas/pancreatitis-cronica-bloqueo-celiaco.svg",
    alt: "Flujograma de manejo del dolor en la pancreatitis crónica con bloqueo celíaco"
  },
  "PED-007": {
    titulo: "Vacunación neonatal: BCG y HvB",
    imagen: "flujogramas/vacunacion-neonatal-bcg-hvb.svg",
    alt: "Flujograma de vacunación neonatal con BCG y hepatitis B"
  },
  "PSI-002": {
    titulo: "Trastorno de pánico: crisis de ansiedad",
    imagen: "flujogramas/trastorno-de-panico-crisis-ansiedad.svg",
    alt: "Flujograma diagnóstico del trastorno de pánico"
  },
  "PED-008": {
    titulo: "Obstrucción neonatal: tapón meconial",
    imagen: "flujogramas/obstruccion-neonatal-tapon-meconial.svg",
    alt: "Flujograma diagnóstico de la obstrucción intestinal neonatal por tapón meconial"
  },
  "NEF-003": {
    titulo: "Pielonefritis aguda: diagnóstico clínico",
    imagen: "flujogramas/pielonefritis-aguda-diagnostico-clinico.svg",
    alt: "Flujograma de diagnóstico clínico de la pielonefritis aguda"
  },
  "END-004": {
    titulo: "Tolerancia oral a la glucosa y secreción de insulina",
    imagen: "flujogramas/tolerancia-oral-glucosa-secrecion-insulina.svg",
    alt: "Flujograma de la prueba de tolerancia oral a la glucosa para valorar la secreción de insulina"
  },
  "PED-009": {
    titulo: "Otitis media aguda en el lactante",
    imagen: "flujogramas/otitis-media-aguda-lactante.svg",
    alt: "Flujograma diagnóstico de la otitis media aguda en el lactante"
  },
  "NEU-002": {
    titulo: "Tromboembolismo pulmonar: alteplase",
    imagen: "flujogramas/tromboembolismo-pulmonar-alteplase.svg",
    alt: "Flujograma de manejo del tromboembolismo pulmonar masivo con alteplase"
  },
  "SP-004": {
    titulo: "Vulneración del principio de autonomía: confidencialidad",
    imagen: "flujogramas/vulneracion-principio-autonomia-confidencialidad.svg",
    alt: "Flujograma sobre la vulneración de la autonomía y la confidencialidad del paciente"
  },
  "PED-010": {
    titulo: "Bronquitis aguda pediátrica",
    imagen: "flujogramas/bronquitis-aguda-pediatrica.svg",
    alt: "Flujograma diagnóstico de la bronquitis aguda en pediatría"
  },
  "REU-004": {
    titulo: "Urticaria aguda y angioedema",
    imagen: "flujogramas/urticaria-aguda-angioedema.svg",
    alt: "Flujograma de manejo de la urticaria aguda con angioedema"
  }
};
