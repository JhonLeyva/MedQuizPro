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
  },

  /* ---------- ENAM 2020 · preguntas 52 a 71 ---------- */

  "SP-005": {
    titulo: "Prevención del embarazo adolescente: educación",
    imagen: "flujogramas/prevencion-embarazo-adolescente-educacion.svg",
    alt: "Flujograma de intervención educativa para la prevención del embarazo adolescente"
  },
  "GAS-004": {
    titulo: "Enfermedad por reflujo gastroesofágico (ERGE)",
    imagen: "flujogramas/enfermedad-reflujo-gastroesofagico-erge.svg",
    alt: "Flujograma diagnóstico y terapéutico de la enfermedad por reflujo gastroesofágico"
  },
  "INF-005": {
    titulo: "Neumonía por Pneumocystis jirovecii en VIH",
    imagen: "flujogramas/neumonia-pneumocystis-jirovecii-vih.svg",
    alt: "Flujograma diagnóstico de la neumonía por Pneumocystis jirovecii en el paciente con VIH"
  },
  "CIR-004": {
    titulo: "Neumotórax a tensión: toracocentesis",
    imagen: "flujogramas/neumotorax-a-tension-toracocentesis.svg",
    alt: "Flujograma de manejo del neumotórax a tensión con descompresión por toracocentesis"
  },
  "GIN-008": {
    titulo: "Maduración cervical en el embarazo prolongado",
    imagen: "flujogramas/maduracion-cervical-embarazo-prolongado.svg",
    alt: "Flujograma de maduración cervical e inducción en el embarazo prolongado"
  },
  "SP-006": {
    titulo: "Conflicto de intereses en bioética",
    imagen: "flujogramas/conflicto-de-intereses-bioetica.svg",
    alt: "Flujograma sobre el conflicto de intereses en bioética e integridad científica"
  },
  "GIN-009": {
    titulo: "Embarazo ectópico: ecografía transvaginal",
    imagen: "flujogramas/embarazo-ectopico-ecografia-transvaginal.svg",
    alt: "Flujograma de estudio del embarazo ectópico con ecografía transvaginal"
  },
  "REU-005": {
    titulo: "Acarosis (escabiosis) en el lactante: permetrina",
    imagen: "flujogramas/acarosis-escabiosis-lactante-permetrina.svg",
    alt: "Flujograma diagnóstico y terapéutico de la escabiosis en el lactante con permetrina"
  },
  "GAS-005": {
    titulo: "Screening de cáncer colorrectal: colonoscopia",
    imagen: "flujogramas/screening-cancer-colorrectal-colonoscopia.svg",
    alt: "Flujograma de tamizaje del cáncer colorrectal con colonoscopia"
  },
  "CIR-005": {
    titulo: "Quemaduras: irrigación con agua a temperatura ambiente",
    imagen: "flujogramas/quemaduras-irrigacion-agua-ambiente.svg",
    alt: "Flujograma de manejo inicial de las quemaduras con irrigación de agua a temperatura ambiente"
  },
  "CAR-004": {
    titulo: "Hipertensión arterial grado 2: tratamiento",
    imagen: "flujogramas/hipertension-arterial-grado-2-tratamiento.svg",
    alt: "Flujograma de tratamiento de la hipertensión arterial grado 2 con daño de órgano blanco"
  },
  "NRL-004": {
    titulo: "Déficit de vitamina B12: degeneración cordonal",
    imagen: "flujogramas/deficit-vitamina-b12-degeneracion-cordonal.svg",
    alt: "Flujograma del déficit de vitamina B12 con degeneración combinada subaguda de cordones medulares"
  },
  "GIN-010": {
    titulo: "Parto podálico: referencia quirúrgica",
    imagen: "flujogramas/parto-podalico-referencia-quirurgica.svg",
    alt: "Flujograma de manejo y referencia del parto en presentación podálica"
  },
  "CAR-005": {
    titulo: "Transposición de grandes arterias (TGA)",
    imagen: "flujogramas/transposicion-de-grandes-arterias-tga.svg",
    alt: "Flujograma diagnóstico de la transposición de grandes arterias"
  },
  "SP-007": {
    titulo: "Diseño cuasi experimental en epidemiología",
    imagen: "flujogramas/diseno-cuasi-experimental-epidemiologia.svg",
    alt: "Flujograma de clasificación de diseños de investigación y el diseño cuasi experimental"
  },
  "PSI-003": {
    titulo: "Hiperventilación: alcalosis respiratoria y bolsa de papel",
    imagen: "flujogramas/hiperventilacion-alcalosis-respiratoria-bolsa.svg",
    alt: "Flujograma de manejo de la alcalosis respiratoria por hiperventilación con reinhalación en bolsa"
  },
  "TRA-002": {
    titulo: "Displasia del desarrollo de la cadera: ecografía",
    imagen: "flujogramas/displasia-desarrollo-cadera-ecografia.svg",
    alt: "Flujograma diagnóstico de la displasia del desarrollo de la cadera con ecografía"
  },
  "PED-011": {
    titulo: "Hipoglicemia neonatal en hijo de madre diabética",
    imagen: "flujogramas/hipoglicemia-neonatal-hijo-madre-diabetica.svg",
    alt: "Flujograma de la hipoglicemia neonatal en el recién nacido macrosómico hijo de madre diabética"
  },
  "PED-012": {
    titulo: "Desnutrición aguda: emaciación y antropometría",
    imagen: "flujogramas/desnutricion-aguda-emaciacion-antropometria.svg",
    alt: "Flujograma de clasificación antropométrica de la desnutrición aguda"
  },
  "SP-008": {
    titulo: "Plan Nacional contra la Anemia: equipo de salud",
    imagen: "flujogramas/plan-nacional-anemia-equipo-salud.svg",
    alt: "Flujograma de responsabilidades del equipo de salud en el Plan Nacional contra la Anemia"
  },

  /* ---------- ENAM 2020 · bloque 2 (preguntas 72 a 122) ---------- */

  "CAR-006": {
    titulo: "Infarto agudo de miocardio inferior",
    imagen: "flujogramas/infarto-agudo-miocardio-inferior.svg",
    alt: "Flujograma diagnóstico del infarto agudo de miocardio de cara inferior"
  },
  "CB-002": {
    titulo: "Mialgias por estatinas y gemfibrozilo",
    imagen: "flujogramas/mialgias-estatinas-gemfibrozilo.svg",
    alt: "Flujograma de la miopatía por la asociación de estatinas y gemfibrozilo"
  },
  "CB-003": {
    titulo: "Intoxicación por organofosforados: atropina",
    imagen: "flujogramas/intoxicacion-organofosforados-atropina.svg",
    alt: "Flujograma de manejo de la intoxicación por organofosforados con atropina"
  },
  "CIR-006": {
    titulo: "Telangiectasias: escleroterapia",
    imagen: "flujogramas/telangiectasias-escleroterapia.svg",
    alt: "Flujograma de manejo de las telangiectasias con escleroterapia"
  },
  "CIR-007": {
    titulo: "Regla de los nueves en quemaduras",
    imagen: "flujogramas/regla-de-los-nueves-quemaduras.svg",
    alt: "Flujograma de cálculo de la superficie corporal quemada con la regla de los nueves"
  },
  "CIR-008": {
    titulo: "Injuria inhalatoria: intubación precoz",
    imagen: "flujogramas/injuria-inhalatoria-intubacion-precoz.svg",
    alt: "Flujograma de manejo de la injuria inhalatoria con intubación precoz"
  },
  "END-005": {
    titulo: "Hipotiroidismo primario: levotiroxina",
    imagen: "flujogramas/hipotiroidismo-primario-levotiroxina.svg",
    alt: "Flujograma diagnóstico y terapéutico del hipotiroidismo primario con levotiroxina"
  },
  "GIN-011": {
    titulo: "Embarazo postérmino: cesárea de emergencia",
    imagen: "flujogramas/embarazo-postermino-cesarea-emergencia.svg",
    alt: "Flujograma de manejo del embarazo postérmino con compromiso fetal y cesárea de emergencia"
  },
  "GIN-012": {
    titulo: "Maduración pulmonar fetal: betametasona",
    imagen: "flujogramas/maduracion-pulmonar-fetal-betametasona.svg",
    alt: "Flujograma de maduración pulmonar fetal con betametasona en el parto pretérmino"
  },
  "GIN-013": {
    titulo: "Enfermedad pélvica inflamatoria: signo de Frenkel",
    imagen: "flujogramas/enfermedad-pelvica-inflamatoria-frenkel.svg",
    alt: "Flujograma diagnóstico de la enfermedad pélvica inflamatoria"
  },
  "HEM-003": {
    titulo: "Anemia megaloblástica por resección del íleon",
    imagen: "flujogramas/anemia-megaloblastica-reseccion-ileon.svg",
    alt: "Flujograma de la anemia megaloblástica por malabsorción de vitamina B12 tras resección ileal"
  },
  "NEF-004": {
    titulo: "Glomerulonefritis postestreptocócica: C3",
    imagen: "flujogramas/glomerulonefritis-postestreptococica-c3.svg",
    alt: "Flujograma diagnóstico de la glomerulonefritis postestreptocócica con complemento C3 bajo"
  },
  "PED-013": {
    titulo: "Sepsis neonatal temprana: ampicilina + amikacina",
    imagen: "flujogramas/sepsis-neonatal-temprana-ampicilina-amikacina.svg",
    alt: "Flujograma de manejo de la sepsis neonatal temprana con ampicilina y amikacina"
  },
  "PED-014": {
    titulo: "Varicela: diagnóstico clínico",
    imagen: "flujogramas/varicela-diagnostico-clinico.svg",
    alt: "Flujograma de diagnóstico clínico de la varicela"
  },
  "PED-015": {
    titulo: "Estenosis hipertrófica de píloro: rehidratación",
    imagen: "flujogramas/estenosis-hipertrofica-piloro-rehidratacion.svg",
    alt: "Flujograma de manejo inicial de la estenosis hipertrófica de píloro con rehidratación"
  },
  "PED-016": {
    titulo: "Laringotraqueítis (crup): estridor",
    imagen: "flujogramas/laringotraqueitis-crup-estridor.svg",
    alt: "Flujograma diagnóstico y terapéutico de la laringotraqueítis o crup"
  },
  "PED-017": {
    titulo: "Otitis media aguda: amoxicilina",
    imagen: "flujogramas/otitis-media-aguda-amoxicilina.svg",
    alt: "Flujograma de tratamiento de la otitis media aguda con amoxicilina"
  },
  "REU-006": {
    titulo: "Foliculitis estafilocócica: dicloxacilina",
    imagen: "flujogramas/foliculitis-estafilococica-dicloxacilina.svg",
    alt: "Flujograma de manejo de la foliculitis estafilocócica con dicloxacilina"
  },
  "SP-009": {
    titulo: "Menor que rechaza tratamiento: aviso a la fiscalía",
    imagen: "flujogramas/rechazo-tratamiento-menor-fiscalia.svg",
    alt: "Flujograma de actuación ante el rechazo de tratamiento en un menor de edad"
  },
  "SP-010": {
    titulo: "Prevención secundaria: diabetes y obesidad",
    imagen: "flujogramas/prevencion-secundaria-diabetes-obesidad.svg",
    alt: "Flujograma de los niveles de prevención aplicados a la diabetes y la obesidad"
  },
  "SP-011": {
    titulo: "Captación precoz en el control prenatal",
    imagen: "flujogramas/captacion-precoz-control-prenatal.svg",
    alt: "Flujograma de captación precoz y seguimiento de la gestante en el control prenatal"
  },
  "SP-012": {
    titulo: "Población asegurada de EsSalud",
    imagen: "flujogramas/poblacion-asegurada-essalud.svg",
    alt: "Flujograma de la población usuaria del Seguro Social de Salud (EsSalud)"
  },
  "SP-013": {
    titulo: "Definición epidemiológica de brote",
    imagen: "flujogramas/definicion-epidemiologica-brote.svg",
    alt: "Flujograma de la definición epidemiológica de brote en vigilancia"
  },
  "TRA-003": {
    titulo: "Sección del tendón palmar menor",
    imagen: "flujogramas/seccion-tendon-palmar-menor.svg",
    alt: "Flujograma de evaluación de la sección del tendón palmar menor"
  },
  "TRA-004": {
    titulo: "Síndrome compartimental: fasciotomía",
    imagen: "flujogramas/sindrome-compartimental-fasciotomia.svg",
    alt: "Flujograma de manejo del síndrome compartimental con fasciotomía"
  },

  /* ---------- ENAM 2020 · bloque 3 (preguntas 123 a 172) ---------- */

  "INF-008": {
    titulo: "Neumonía asociada al ventilador: meropenem + vancomicina",
    imagen: "flujogramas/neumonia-asociada-ventilador-meropenem-vancomicina.svg",
    alt: "Flujograma de tratamiento empírico de la neumonía asociada a ventilación mecánica"
  },
  "TRA-005": {
    titulo: "Escoliosis estructural: test de Adams",
    imagen: "flujogramas/escoliosis-estructural-test-adams.svg",
    alt: "Flujograma diagnóstico de la escoliosis estructural con el test de Adams"
  },
  "PED-022": {
    titulo: "Shock hipovolémico por deshidratación neonatal",
    imagen: "flujogramas/shock-hipovolemico-deshidratacion-neonatal.svg",
    alt: "Flujograma de manejo del shock hipovolémico por deshidratación en el neonato"
  },
  "GIN-016": {
    titulo: "Gestación anembrionada (huevo huero)",
    imagen: "flujogramas/gestacion-anembrionada-huevo-huero.svg",
    alt: "Flujograma diagnóstico ecográfico de la gestación anembrionada"
  },
  "PED-023": {
    titulo: "Tos ferina: reacción leucemoide",
    imagen: "flujogramas/tos-ferina-reaccion-leucemoide.svg",
    alt: "Flujograma de factores pronósticos de la tos ferina con reacción leucemoide"
  },
  "PED-024": {
    titulo: "Intususcepción (invaginación intestinal) en pediatría",
    imagen: "flujogramas/intususcepcion-invaginacion-intestinal-pediatria.svg",
    alt: "Flujograma diagnóstico de la intususcepción intestinal en el lactante"
  },
  "INF-009": {
    titulo: "Meningitis tuberculosa: ADA en LCR",
    imagen: "flujogramas/meningitis-tuberculosa-ada-lcr.svg",
    alt: "Flujograma diagnóstico de la meningitis tuberculosa con ADA en líquido cefalorraquídeo"
  },
  "PED-025": {
    titulo: "Intoxicación por organofosforados en pediatría",
    imagen: "flujogramas/intoxicacion-organofosforados-pediatria.svg",
    alt: "Flujograma de la intoxicación por organofosforados en el niño"
  },
  "SP-017": {
    titulo: "Determinantes sociales: saneamiento y desnutrición",
    imagen: "flujogramas/determinantes-sociales-saneamiento-desnutricion.svg",
    alt: "Flujograma de determinantes sociales de la salud, saneamiento básico y desnutrición"
  },
  "CB-004": {
    titulo: "Intoxicación por metanol: acidosis y amaurosis",
    imagen: "flujogramas/intoxicacion-metanol-acidosis-amaurosis.svg",
    alt: "Flujograma de la intoxicación por metanol con acidosis metabólica y amaurosis"
  },
  "PED-026": {
    titulo: "Crisis convulsiva: diazepam",
    imagen: "flujogramas/convulsion-febril-status-diazepam.svg",
    alt: "Flujograma de manejo inmediato de la crisis convulsiva pediátrica con diazepam"
  },
  "NEF-008": {
    titulo: "Cólico renoureteral: UroTAC",
    imagen: "flujogramas/colico-renoureteral-urotac-urotem.svg",
    alt: "Flujograma diagnóstico del cólico renoureteral con UroTAC"
  },
  "PED-027": {
    titulo: "Neumonía bacteriana: consolidación alveolar",
    imagen: "flujogramas/neumonia-bacteriana-consolidacion-alveolar.svg",
    alt: "Flujograma de la neumonía bacteriana pediátrica con consolidación alveolar"
  },
  "GIN-017": {
    titulo: "Candidiasis vulvovaginal",
    imagen: "flujogramas/candidiasis-vulvovaginal-micotica.svg",
    alt: "Flujograma diagnóstico de la vaginitis micótica o candidiasis vulvovaginal"
  },
  "GIN-018": {
    titulo: "Atonía uterina: palpación bimanual",
    imagen: "flujogramas/atonia-uterina-palpacion-bimanual.svg",
    alt: "Flujograma de evaluación de la hemorragia posparto por atonía uterina"
  },
  "REU-007": {
    titulo: "Vasculitis leucocitoclástica: púrpura palpable",
    imagen: "flujogramas/vasculitis-leucocitoclastica-purpura-palpable.svg",
    alt: "Flujograma diagnóstico de la vasculitis con púrpura palpable"
  },
  "GIN-019": {
    titulo: "VIH intraparto: cesárea de emergencia",
    imagen: "flujogramas/vih-intraparto-cesarea-emergencia.svg",
    alt: "Flujograma de manejo del parto en la gestante con VIH diagnosticado intraparto"
  },
  "CB-005": {
    titulo: "Anafilaxia: mastocitos e hipersensibilidad tipo I",
    imagen: "flujogramas/anafilaxia-mastocitos-hipersensibilidad-tipo-i.svg",
    alt: "Flujograma de la anafilaxia mediada por IgE y la degranulación de mastocitos"
  },
  "NEU-004": {
    titulo: "Pleuresía tuberculosa: ADA y exudado",
    imagen: "flujogramas/pleuresia-tuberculosa-ada-exudado.svg",
    alt: "Flujograma diagnóstico de la pleuresía tuberculosa con exudado linfocitario y ADA elevada"
  },
  "PED-028": {
    titulo: "Púrpura trombocitopénica inmune postvacunal",
    imagen: "flujogramas/purpura-trombocitopenica-inmune-postvacunal.svg",
    alt: "Flujograma diagnóstico de la púrpura trombocitopénica inmune posterior a vacunación"
  },
  "PED-029": {
    titulo: "Urocultivo falso negativo por antibióticos",
    imagen: "flujogramas/urocultivo-falso-negativo-antibioticos.svg",
    alt: "Flujograma de causas de urocultivo falso negativo"
  },
  "PED-030": {
    titulo: "Rinitis alérgica y asma atópica",
    imagen: "flujogramas/rinitis-alergica-asma-atopica.svg",
    alt: "Flujograma diagnóstico de la rinitis alérgica en el paciente atópico"
  },
  "NRL-005": {
    titulo: "Accidente isquémico transitorio (AIT)",
    imagen: "flujogramas/accidente-isquemico-transitorio-ait.svg",
    alt: "Flujograma diagnóstico del accidente isquémico transitorio"
  },
  "NRL-006": {
    titulo: "Hematoma epidural: arteria meníngea media",
    imagen: "flujogramas/hematoma-epidural-arteria-meningea-media.svg",
    alt: "Flujograma diagnóstico del hematoma epidural por lesión de la arteria meníngea media"
  },
  "PSI-006": {
    titulo: "Trastorno de personalidad límite (borderline)",
    imagen: "flujogramas/trastorno-personalidad-limite-borderline.svg",
    alt: "Flujograma diagnóstico del trastorno límite de la personalidad"
  },
  "CIR-013": {
    titulo: "Hernia crural (femoral) complicada",
    imagen: "flujogramas/hernia-crural-femoral-complicada.svg",
    alt: "Flujograma diagnóstico de la hernia crural complicada"
  },
  "SP-018": {
    titulo: "Tuberculosis: control ambiental y ventilación",
    imagen: "flujogramas/tuberculosis-control-ambiental-ventilacion.svg",
    alt: "Flujograma de medidas de control ambiental de la tuberculosis en establecimientos de salud"
  },
  "CB-006": {
    titulo: "Anfetaminas: vasoconstricción y resistencia periférica",
    imagen: "flujogramas/anfetaminas-resistencia-periferica-vasoconstriccion.svg",
    alt: "Flujograma del mecanismo hipertensivo de las anfetaminas por aumento de la resistencia periférica"
  },
  "GIN-020": {
    titulo: "Hipodinamia uterina: estimulación con oxitocina",
    imagen: "flujogramas/hipodinamia-uterina-estimulacion-oxitocina.svg",
    alt: "Flujograma de manejo de la hipodinamia uterina con oxitocina"
  },
  "GIN-021": {
    titulo: "Síndrome de ovario poliquístico: factor ovárico",
    imagen: "flujogramas/sindrome-ovario-poliquistico-factor-ovarico.svg",
    alt: "Flujograma de la amenorrea anovulatoria por síndrome de ovario poliquístico"
  },
  "PED-031": {
    titulo: "Saturnismo: intoxicación crónica por plomo",
    imagen: "flujogramas/saturnismo-intoxicacion-cronica-plomo.svg",
    alt: "Flujograma diagnóstico de la intoxicación crónica por plomo en el niño"
  },
  "GIN-022": {
    titulo: "Hipertensión severa en la gestación: referencia",
    imagen: "flujogramas/hipertension-severa-gestacion-referencia.svg",
    alt: "Flujograma de referencia de la gestante con hipertensión severa"
  },
  "GIN-023": {
    titulo: "Prolapso genital con úlceras: estrógenos tópicos",
    imagen: "flujogramas/prolapso-genital-ulceras-estrogenos-topicos.svg",
    alt: "Flujograma de preparación del prolapso genital ulcerado con estrógenos tópicos"
  },
  "OFT-005": {
    titulo: "Conjuntivitis alérgica: prurito bilateral",
    imagen: "flujogramas/conjuntivitis-alergica-prurito-bilateral.svg",
    alt: "Flujograma diagnóstico de la conjuntivitis alérgica"
  },
  "SP-019": {
    titulo: "Dengue: control vectorial del Aedes",
    imagen: "flujogramas/dengue-control-vectorial-aedes.svg",
    alt: "Flujograma de control vectorial del Aedes aegypti ante un caso importado de dengue"
  },
  "CAR-009": {
    titulo: "Paro cardiorrespiratorio: compresiones torácicas",
    imagen: "flujogramas/paro-cardiorrespiratorio-compresiones-toracicas.svg",
    alt: "Flujograma de reanimación cardiopulmonar con inicio de compresiones torácicas"
  },
  "REU-008": {
    titulo: "Tinea capitis: dermatofitosis del cuero cabelludo",
    imagen: "flujogramas/tinea-capitis-dermatofitosis-cuero-cabelludo.svg",
    alt: "Flujograma diagnóstico de la tiña de la cabeza"
  },
  "NRL-007": {
    titulo: "Síndrome de cola de caballo tras anestesia raquídea",
    imagen: "flujogramas/sindrome-cola-caballo-anestesia-raquidea.svg",
    alt: "Flujograma del síndrome de cola de caballo como complicación de la anestesia raquídea"
  },
  "NEF-009": {
    titulo: "Torsión testicular: reflejo cremastérico",
    imagen: "flujogramas/torsion-testicular-reflejo-cremasterico.svg",
    alt: "Flujograma diagnóstico del escroto agudo y la torsión testicular"
  },
  "GIN-024": {
    titulo: "Desprendimiento prematuro de placenta: hipertonía",
    imagen: "flujogramas/desprendimiento-prematuro-placenta-hipertonia.svg",
    alt: "Flujograma diagnóstico del desprendimiento prematuro de placenta"
  },
  "GIN-025": {
    titulo: "Metrorragia posmenopáusica: biopsia de endometrio",
    imagen: "flujogramas/metrorragia-posmenopausica-biopsia-endometrio.svg",
    alt: "Flujograma de estudio de la metrorragia posmenopáusica con biopsia de endometrio"
  },
  "CAR-010": {
    titulo: "Endocarditis infecciosa: ecocardiografía transesofágica",
    imagen: "flujogramas/endocarditis-infecciosa-ecocardiografia-transesofagica.svg",
    alt: "Flujograma diagnóstico de la endocarditis infecciosa con ecocardiografía transesofágica"
  },
  "GIN-026": {
    titulo: "Altura uterina: 12 semanas en la sínfisis del pubis",
    imagen: "flujogramas/altura-uterina-12-semanas-sinfisis-pubis.svg",
    alt: "Flujograma de estimación de la edad gestacional por altura uterina"
  },
  "PED-032": {
    titulo: "Hepatitis A: coluria en el escolar",
    imagen: "flujogramas/hepatitis-a-coluria-escolar.svg",
    alt: "Flujograma diagnóstico de la hepatitis A en el escolar"
  },
  "GIN-027": {
    titulo: "Amenaza de parto pretérmino",
    imagen: "flujogramas/amenaza-parto-pretermino-cervix-cerrado.svg",
    alt: "Flujograma diagnóstico de la amenaza de parto pretérmino"
  },
  "INF-010": {
    titulo: "Dengue con signos de alarma",
    imagen: "flujogramas/dengue-con-signos-alarma-madre-de-dios.svg",
    alt: "Flujograma diagnóstico del dengue con signos de alarma"
  },
  "CAR-011": {
    titulo: "Insuficiencia cardíaca aguda: furosemida",
    imagen: "flujogramas/insuficiencia-cardiaca-aguda-furosemida-diureticos.svg",
    alt: "Flujograma de manejo de la insuficiencia cardíaca aguda congestiva con diuréticos"
  },
  "NEU-005": {
    titulo: "Enfermedad pulmonar intersticial: crepitantes",
    imagen: "flujogramas/enfermedad-pulmonar-intersticial-crepitantes.svg",
    alt: "Flujograma diagnóstico de la enfermedad pulmonar intersticial difusa"
  },
  "GIN-028": {
    titulo: "Metrorragia del primer trimestre: ecografía transvaginal",
    imagen: "flujogramas/metrorragia-primer-trimestre-ecografia-transvaginal.svg",
    alt: "Flujograma de estudio del sangrado del primer trimestre con ecografía transvaginal"
  },

  /* ---------- ENAM 2020 · bloque 2 (preguntas pendientes) ---------- */

  "CAR-007": {
    titulo: "Estenosis mitral reumática y fibrilación auricular",
    imagen: "flujogramas/estenosis-mitral-fibrilacion-auricular-warfarina.svg",
    alt: "Flujograma: estenosis mitral reumática y fibrilación auricular"
  },
  "CAR-008": {
    titulo: "Miocardiopatía chagásica y arritmias",
    imagen: "flujogramas/miocardiopatia-chagasica-taquicardia-ventricular-amiodarona.svg",
    alt: "Flujograma: miocardiopatía chagásica y arritmias"
  },
  "CIR-009": {
    titulo: "Isquemia arterial aguda: clasificación de Rutherford",
    imagen: "flujogramas/isquemia-arterial-aguda-rutherford-amputacion.svg",
    alt: "Flujograma: isquemia arterial aguda: clasificación de Rutherford"
  },
  "CIR-010": {
    titulo: "Complicaciones de la hernioplastia inguinal",
    imagen: "flujogramas/orquitis-isquemica-post-hernioplastia.svg",
    alt: "Flujograma: complicaciones de la hernioplastia inguinal"
  },
  "CIR-011": {
    titulo: "Trauma abdominal cerrado",
    imagen: "flujogramas/trauma-abdominal-cerrado-fast.svg",
    alt: "Flujograma: trauma abdominal cerrado"
  },
  "CIR-012": {
    titulo: "Fístula perianal",
    imagen: "flujogramas/fistula-perianal-goodsall.svg",
    alt: "Flujograma: fístula perianal"
  },
  "GAS-006": {
    titulo: "Hemorragia digestiva alta por úlcera péptica",
    imagen: "flujogramas/hemorragia-digestiva-alta-ulcera-peptica.svg",
    alt: "Flujograma: hemorragia digestiva alta por úlcera péptica"
  },
  "GAS-007": {
    titulo: "Hemorragia por várices esofágicas",
    imagen: "flujogramas/hemorragia-variceal-hipertension-portal.svg",
    alt: "Flujograma: hemorragia por várices esofágicas"
  },
  "GIN-014": {
    titulo: "Hemorragia de la primera mitad del embarazo",
    imagen: "flujogramas/amenaza-de-aborto-primer-trimestre.svg",
    alt: "Flujograma: hemorragia de la primera mitad del embarazo"
  },
  "GIN-015": {
    titulo: "Miomatosis uterina submucosa",
    imagen: "flujogramas/mioma-submucoso-miomectomia-histeroscopica.svg",
    alt: "Flujograma: miomatosis uterina submucosa"
  },
  "INF-006": {
    titulo: "Leishmaniasis cutánea",
    imagen: "flujogramas/leishmaniasis-cutanea-antimonial-pentavalente.svg",
    alt: "Flujograma: leishmaniasis cutánea"
  },
  "INF-007": {
    titulo: "Malaria: diagnóstico y gravedad",
    imagen: "flujogramas/malaria-diagnostico-gravedad-amazonia.svg",
    alt: "Flujograma: malaria: diagnóstico y gravedad"
  },
  "NEF-005": {
    titulo: "Síndrome nefrótico vs. nefrítico",
    imagen: "flujogramas/sindrome-nefrotico-pediatrico-cambios-minimos.svg",
    alt: "Flujograma: síndrome nefrótico vs. nefrítico"
  },
  "NEF-006": {
    titulo: "Rabdomiólisis por aplastamiento",
    imagen: "flujogramas/rabdomiolisis-aplastamiento-lesion-renal.svg",
    alt: "Flujograma: rabdomiólisis por aplastamiento"
  },
  "NEF-007": {
    titulo: "Síndrome nefrótico del adulto",
    imagen: "flujogramas/sindrome-nefrotico-adulto-proteinuria.svg",
    alt: "Flujograma: síndrome nefrótico del adulto"
  },
  "NEU-003": {
    titulo: "Asma: escalonamiento del tratamiento",
    imagen: "flujogramas/asma-escalonamiento-corticoide-inhalado.svg",
    alt: "Flujograma: asma: escalonamiento del tratamiento"
  },
  "OFT-004": {
    titulo: "Epistaxis posterior",
    imagen: "flujogramas/epistaxis-posterior-taponamiento.svg",
    alt: "Flujograma: epistaxis posterior"
  },
  "PED-018": {
    titulo: "Giardiasis",
    imagen: "flujogramas/giardiasis-diarrea-cronica-escolar.svg",
    alt: "Flujograma: giardiasis"
  },
  "PED-019": {
    titulo: "Atresia intestinal",
    imagen: "flujogramas/atresia-intestinal-prematuros.svg",
    alt: "Flujograma: atresia intestinal"
  },
  "PED-020": {
    titulo: "Meningitis neonatal",
    imagen: "flujogramas/meningitis-neonatal-sepsis-temprana.svg",
    alt: "Flujograma: meningitis neonatal"
  },
  "PED-021": {
    titulo: "Conjuntivitis neonatal",
    imagen: "flujogramas/conjuntivitis-neonatal-gonococica.svg",
    alt: "Flujograma: conjuntivitis neonatal"
  },
  "PSI-004": {
    titulo: "Intoxicación por benzodiacepinas",
    imagen: "flujogramas/intoxicacion-benzodiacepinas-flumazenilo.svg",
    alt: "Flujograma: intoxicación por benzodiacepinas"
  },
  "PSI-005": {
    titulo: "Conducta suicida: clasificación",
    imagen: "flujogramas/gesto-suicida-conducta-suicida.svg",
    alt: "Flujograma: conducta suicida: clasificación"
  },
  "SP-014": {
    titulo: "Coinfección TB-VIH",
    imagen: "flujogramas/coinfeccion-tb-vih-terapia-preventiva.svg",
    alt: "Flujograma: coinfección TB-VIH"
  },
  "SP-015": {
    titulo: "Veracidad en la relación médico-paciente",
    imagen: "flujogramas/veracidad-informacion-adolescente-bioetica.svg",
    alt: "Flujograma: veracidad en la relación médico-paciente"
  },
  "SP-016": {
    titulo: "Violencia contra la mujer",
    imagen: "flujogramas/violencia-familiar-ley-30364.svg",
    alt: "Flujograma: violencia contra la mujer"
  }
};
