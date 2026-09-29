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
  },

  /* ---------- Casos de práctica (preguntas tipo) ---------- */

  "CAR-002": {
    titulo: "Fibrilación auricular no valvular",
    imagen: "flujogramas/fibrilacion-auricular-no-valvular-anticoagulacion.svg",
    alt: "Flujograma: fibrilación auricular no valvular"
  },
  "CAR-003": {
    titulo: "Soplos sistólicos: estenosis aórtica",
    imagen: "flujogramas/estenosis-aortica-severa-sincope.svg",
    alt: "Flujograma: soplos sistólicos: estenosis aórtica"
  },
  "CB-001": {
    titulo: "Fenilcetonuria",
    imagen: "flujogramas/fenilcetonuria-fenilalanina-hidroxilasa.svg",
    alt: "Flujograma: fenilcetonuria"
  },
  "CIR-001": {
    titulo: "Apendicitis aguda",
    imagen: "flujogramas/apendicitis-aguda-apendicectomia.svg",
    alt: "Flujograma: apendicitis aguda"
  },
  "END-001": {
    titulo: "Cetoacidosis diabética",
    imagen: "flujogramas/cetoacidosis-diabetica-hidratacion.svg",
    alt: "Flujograma: cetoacidosis diabética"
  },
  "GAS-001": {
    titulo: "Sangrado variceal: tratamiento inicial",
    imagen: "flujogramas/hemorragia-variceal-vasoactivos.svg",
    alt: "Flujograma: sangrado variceal: tratamiento inicial"
  },
  "GIN-001": {
    titulo: "Hemorragia posparto por atonía uterina",
    imagen: "flujogramas/hemorragia-posparto-atonia-oxitocina.svg",
    alt: "Flujograma: hemorragia posparto por atonía uterina"
  },
  "HEM-001": {
    titulo: "Anemia microcítica",
    imagen: "flujogramas/anemia-microcitica-ferritina.svg",
    alt: "Flujograma: anemia microcítica"
  },
  "INF-001": {
    titulo: "Malaria por Plasmodium vivax",
    imagen: "flujogramas/malaria-vivax-cloroquina-primaquina.svg",
    alt: "Flujograma: malaria por Plasmodium vivax"
  },
  "NEF-001": {
    titulo: "Hiperpotasemia con cambios en el ECG",
    imagen: "flujogramas/hiperpotasemia-gluconato-de-calcio.svg",
    alt: "Flujograma: hiperpotasemia con cambios en el ECG"
  },
  "NEU-001": {
    titulo: "Derrame pleural: enfoque diagnóstico",
    imagen: "flujogramas/derrame-pleural-enfoque-tuberculosis.svg",
    alt: "Flujograma: derrame pleural, enfoque diagnóstico"
  },
  "NRL-001": {
    titulo: "Ictus agudo: primer examen",
    imagen: "flujogramas/acv-agudo-tomografia-sin-contraste.svg",
    alt: "Flujograma: ictus agudo: primer examen"
  },
  "OFT-001": {
    titulo: "Glaucoma agudo de ángulo cerrado",
    imagen: "flujogramas/glaucoma-agudo-angulo-cerrado.svg",
    alt: "Flujograma: glaucoma agudo de ángulo cerrado"
  },
  "PED-001": {
    titulo: "Ictericia neonatal",
    imagen: "flujogramas/ictericia-neonatal-incompatibilidad-abo.svg",
    alt: "Flujograma: ictericia neonatal"
  },
  "PSI-001": {
    titulo: "Episodio depresivo mayor",
    imagen: "flujogramas/depresion-mayor-isrs.svg",
    alt: "Flujograma: episodio depresivo mayor"
  },
  "REU-001": {
    titulo: "Artritis por cristales",
    imagen: "flujogramas/gota-cristales-urato-monosodico.svg",
    alt: "Flujograma: artritis por cristales"
  },
  "SP-001": {
    titulo: "Validez de una prueba diagnóstica",
    imagen: "flujogramas/sensibilidad-especificidad-tabla-2x2.svg",
    alt: "Flujograma: validez de una prueba diagnóstica"
  },
  "TRA-001": {
    titulo: "Fractura de escafoides",
    imagen: "flujogramas/fractura-escafoides-tabaquera-anatomica.svg",
    alt: "Flujograma: fractura de escafoides"
  },

  /* ---------- ENAM 2020 · bloque 2 (preguntas 174-259 del banco PDF) ---------- */

  "CIR-014": {
    titulo: "Fisura anal",
    imagen: "flujogramas/fisura-anal-esfinter-hipertonico.svg",
    alt: "Flujograma: Fisura anal"
  },
  "NEU-006": {
    titulo: "Tuberculosis pulmonar: diagnóstico",
    imagen: "flujogramas/tuberculosis-pulmonar-baciloscopia-diagnostico.svg",
    alt: "Flujograma: Tuberculosis pulmonar: diagnóstico"
  },
  "INF-011": {
    titulo: "Uretritis gonocócica",
    imagen: "flujogramas/uretritis-gonococica-ceftriaxona.svg",
    alt: "Flujograma: Uretritis gonocócica"
  },
  "REU-009": {
    titulo: "Dermatitis atópica del lactante",
    imagen: "flujogramas/dermatitis-atopica-lactante-diferencial.svg",
    alt: "Flujograma: Dermatitis atópica del lactante"
  },
  "GIN-029": {
    titulo: "Trabajo de parto prolongado",
    imagen: "flujogramas/trabajo-parto-prolongado-cesarea.svg",
    alt: "Flujograma: Trabajo de parto prolongado"
  },
  "CIR-015": {
    titulo: "Plastrón apendicular",
    imagen: "flujogramas/plastron-apendicular-manejo-conservador.svg",
    alt: "Flujograma: Plastrón apendicular"
  },
  "END-006": {
    titulo: "Hipotiroidismo primario",
    imagen: "flujogramas/hipotiroidismo-mixedema-tsh-levotiroxina.svg",
    alt: "Flujograma: Hipotiroidismo primario"
  },
  "CB-007": {
    titulo: "Beta oxidación de ácidos grasos",
    imagen: "flujogramas/deficit-mcad-beta-oxidacion.svg",
    alt: "Flujograma: Beta oxidación de ácidos grasos"
  },
  "NRL-008": {
    titulo: "Enfermedad de Parkinson",
    imagen: "flujogramas/enfermedad-parkinson-levodopa.svg",
    alt: "Flujograma: Enfermedad de Parkinson"
  },
  "PSI-007": {
    titulo: "Duelo y riesgo suicida en adolescentes",
    imagen: "flujogramas/duelo-adolescente-riesgo-suicida.svg",
    alt: "Flujograma: Duelo y riesgo suicida en adolescentes"
  },
  "PSI-008": {
    titulo: "Trastorno obsesivo-compulsivo",
    imagen: "flujogramas/trastorno-obsesivo-compulsivo-contaminacion.svg",
    alt: "Flujograma: Trastorno obsesivo-compulsivo"
  },
  "PSI-009": {
    titulo: "Esquizofrenia paranoide",
    imagen: "flujogramas/esquizofrenia-paranoide-diferencial.svg",
    alt: "Flujograma: Esquizofrenia paranoide"
  },
  "PSI-010": {
    titulo: "Episodio depresivo mayor",
    imagen: "flujogramas/episodio-depresivo-mayor-adolescente.svg",
    alt: "Flujograma: Episodio depresivo mayor"
  },
  "PSI-011": {
    titulo: "Ataque de pánico",
    imagen: "flujogramas/ataque-de-panico-evolucion.svg",
    alt: "Flujograma: Ataque de pánico"
  },
  "SP-020": {
    titulo: "Objeción de conciencia",
    imagen: "flujogramas/objecion-de-conciencia-derivacion.svg",
    alt: "Flujograma: Objeción de conciencia"
  },
  "PED-033": {
    titulo: "Intoxicación por organofosforados",
    imagen: "flujogramas/organofosforados-atropina-pediatria.svg",
    alt: "Flujograma: Intoxicación por organofosforados"
  },
  "NEF-010": {
    titulo: "Anemia en enfermedad renal crónica",
    imagen: "flujogramas/anemia-erc-hierro-eritropoyetina.svg",
    alt: "Flujograma: Anemia en enfermedad renal crónica"
  },
  "NEF-011": {
    titulo: "Rabdomiólisis y lesión renal aguda",
    imagen: "flujogramas/rabdomiolisis-aplastamiento-lra.svg",
    alt: "Flujograma: Rabdomiólisis y lesión renal aguda"
  },
  "CB-008": {
    titulo: "Farmacología del paracetamol",
    imagen: "flujogramas/paracetamol-farmacologia-cox.svg",
    alt: "Flujograma: Farmacología del paracetamol"
  },
  "NEF-012": {
    titulo: "Nefropatía diabética",
    imagen: "flujogramas/nefropatia-diabetica-ieca.svg",
    alt: "Flujograma: Nefropatía diabética"
  },
  "CIR-016": {
    titulo: "Politraumatizado en shock: manejo inicial",
    imagen: "flujogramas/politraumatizado-shock-xabcde.svg",
    alt: "Flujograma: Politraumatizado en shock: manejo inicial"
  },
  "GIN-030": {
    titulo: "Presentación podálica",
    imagen: "flujogramas/presentacion-podalica-cesarea.svg",
    alt: "Flujograma: Presentación podálica"
  },
  "GIN-031": {
    titulo: "Endometritis puerperal",
    imagen: "flujogramas/endometritis-puerperal-fiebre-posparto.svg",
    alt: "Flujograma: Endometritis puerperal"
  },
  "CB-009": {
    titulo: "Embriología: implantación",
    imagen: "flujogramas/implantacion-blastocisto-embriologia.svg",
    alt: "Flujograma: Embriología: implantación"
  },
  "GIN-032": {
    titulo: "Corioamnionitis",
    imagen: "flujogramas/corioamnionitis-fiebre-intraparto.svg",
    alt: "Flujograma: Corioamnionitis"
  },
  "GIN-033": {
    titulo: "Desprendimiento prematuro de placenta",
    imagen: "flujogramas/desprendimiento-placenta-hemorragia-tercer-trimestre.svg",
    alt: "Flujograma: Desprendimiento prematuro de placenta"
  },
  "GIN-034": {
    titulo: "Placenta previa",
    imagen: "flujogramas/placenta-previa-hospitalizacion-ecografia.svg",
    alt: "Flujograma: Placenta previa"
  },
  "CIR-017": {
    titulo: "Quemaduras: manejo prehospitalario",
    imagen: "flujogramas/quemaduras-manejo-prehospitalario.svg",
    alt: "Flujograma: Quemaduras: manejo prehospitalario"
  },
  "CAR-012": {
    titulo: "QT prolongado por fármacos",
    imagen: "flujogramas/qt-prolongado-cloroquina.svg",
    alt: "Flujograma: QT prolongado por fármacos"
  },
  "CB-010": {
    titulo: "Anafilaxia e hipersensibilidad",
    imagen: "flujogramas/anafilaxia-picadura-adrenalina.svg",
    alt: "Flujograma: Anafilaxia e hipersensibilidad"
  },
  "NEF-013": {
    titulo: "Intoxicación por metanol y acidosis metabólica",
    imagen: "flujogramas/intoxicacion-metanol-licor-adulterado.svg",
    alt: "Flujograma: Intoxicación por metanol y acidosis metabólica"
  },
  "TRA-006": {
    titulo: "Trauma cervical por latigazo",
    imagen: "flujogramas/trauma-cervical-latigazo-impacto-posterior.svg",
    alt: "Flujograma: Trauma cervical por latigazo"
  },
  "GIN-035": {
    titulo: "Tamizaje de diabetes gestacional",
    imagen: "flujogramas/tamizaje-diabetes-gestacional-ptog.svg",
    alt: "Flujograma: Tamizaje de diabetes gestacional"
  },
  "INF-012": {
    titulo: "Tuberculosis y lactancia materna",
    imagen: "flujogramas/tuberculosis-lactancia-materna.svg",
    alt: "Flujograma: Tuberculosis y lactancia materna"
  },
  "PED-034": {
    titulo: "Displasia broncopulmonar",
    imagen: "flujogramas/displasia-broncopulmonar-prematuro.svg",
    alt: "Flujograma: Displasia broncopulmonar"
  },
  "GIN-036": {
    titulo: "Inmunoprofilaxis anti-D",
    imagen: "flujogramas/inmunoprofilaxis-anti-d-puerpera.svg",
    alt: "Flujograma: Inmunoprofilaxis anti-D"
  },
  "GAS-008": {
    titulo: "Encefalopatía hepática",
    imagen: "flujogramas/encefalopatia-hepatica-west-haven.svg",
    alt: "Flujograma: Encefalopatía hepática"
  },
  "CAR-013": {
    titulo: "Reanimación cardiopulmonar básica",
    imagen: "flujogramas/rcp-basica-adulto-compresiones.svg",
    alt: "Flujograma: Reanimación cardiopulmonar básica"
  },
  "GIN-037": {
    titulo: "Gestante Rh negativa: Coombs indirecto",
    imagen: "flujogramas/gestante-rh-negativo-coombs-indirecto.svg",
    alt: "Flujograma: Gestante Rh negativa: Coombs indirecto"
  },
  "GIN-038": {
    titulo: "Restricción del crecimiento intrauterino",
    imagen: "flujogramas/restriccion-crecimiento-intrauterino-doppler.svg",
    alt: "Flujograma: Restricción del crecimiento intrauterino"
  },
  "SP-021": {
    titulo: "Salud ocupacional: aislamiento por COVID-19",
    imagen: "flujogramas/trabajador-covid-asintomatico-aislamiento.svg",
    alt: "Flujograma: Salud ocupacional: aislamiento por COVID-19"
  },
  "INF-013": {
    titulo: "VIH y vía del parto",
    imagen: "flujogramas/vih-gestante-carga-viral-via-parto.svg",
    alt: "Flujograma: VIH y vía del parto"
  },
  "GIN-039": {
    titulo: "Enfermedad inflamatoria pélvica",
    imagen: "flujogramas/enfermedad-inflamatoria-pelvica-instrumentacion.svg",
    alt: "Flujograma: Enfermedad inflamatoria pélvica"
  },
  "HEM-004": {
    titulo: "Anemia perniciosa",
    imagen: "flujogramas/anemia-perniciosa-factor-intrinseco.svg",
    alt: "Flujograma: Anemia perniciosa"
  },
  "GIN-040": {
    titulo: "Mola hidatiforme",
    imagen: "flujogramas/mola-hidatiforme-diferencial.svg",
    alt: "Flujograma: Mola hidatiforme"
  },
  "GIN-041": {
    titulo: "Aborto inevitable",
    imagen: "flujogramas/aborto-inevitable-clasificacion.svg",
    alt: "Flujograma: Aborto inevitable"
  },
  "PED-035": {
    titulo: "Intususcepción intestinal",
    imagen: "flujogramas/intususcepcion-reduccion-enema.svg",
    alt: "Flujograma: Intususcepción intestinal"
  },
  "CAR-014": {
    titulo: "Trombosis venosa profunda",
    imagen: "flujogramas/trombosis-venosa-profunda-eco-duplex.svg",
    alt: "Flujograma: Trombosis venosa profunda"
  },
  "NEF-014": {
    titulo: "Hidrocele",
    imagen: "flujogramas/hidrocele-transiluminacion-escroto.svg",
    alt: "Flujograma: Hidrocele"
  },
  "NEF-015": {
    titulo: "Litiasis coraliforme de estruvita",
    imagen: "flujogramas/litiasis-coraliforme-estruvita.svg",
    alt: "Flujograma: Litiasis coraliforme de estruvita"
  },

  /* ---------- Bloque 3 (preguntas 262-360 del banco PDF): tema general + ruta del caso ---------- */

  "CIR-018": {
    titulo: "Heridas traumáticas: manejo antibiótico",
    imagen: "flujogramas/heridas-traumaticas-antibioticoterapia.svg",
    alt: "Flujograma: Heridas traumáticas: manejo antibiótico"
  },
  "TRA-007": {
    titulo: "Fracturas expuestas: Gustilo-Anderson",
    imagen: "flujogramas/fractura-expuesta-gustilo-anderson.svg",
    alt: "Flujograma: Fracturas expuestas: Gustilo-Anderson"
  },
  "CIR-019": {
    titulo: "Infecciones necrotizantes de partes blandas",
    imagen: "flujogramas/infecciones-necrotizantes-gangrena-gaseosa.svg",
    alt: "Flujograma: Infecciones necrotizantes de partes blandas"
  },
  "OFT-006": {
    titulo: "Epistaxis: manejo escalonado",
    imagen: "flujogramas/epistaxis-manejo-escalonado.svg",
    alt: "Flujograma: Epistaxis: manejo escalonado"
  },
  "CB-011": {
    titulo: "Anestésicos locales: clasificación y duración",
    imagen: "flujogramas/anestesicos-locales-clasificacion-duracion.svg",
    alt: "Flujograma: Anestésicos locales: clasificación y duración"
  },
  "CIR-020": {
    titulo: "Trauma torácico con amenaza vital",
    imagen: "flujogramas/trauma-toracico-neumotorax-tension.svg",
    alt: "Flujograma: Trauma torácico con amenaza vital"
  },
  "NEF-016": {
    titulo: "Masa escrotal en el adulto",
    imagen: "flujogramas/masa-escrotal-cancer-testicular.svg",
    alt: "Flujograma: Masa escrotal en el adulto"
  },
  "CIR-021": {
    titulo: "Complicaciones de la hernioplastia inguinal",
    imagen: "flujogramas/complicaciones-hernioplastia-inguinal.svg",
    alt: "Flujograma: Complicaciones de la hernioplastia inguinal"
  },
  "NRL-009": {
    titulo: "Traumatismo craneal: lesiones según su localización",
    imagen: "flujogramas/tec-lesiones-fractura-base-craneo.svg",
    alt: "Flujograma: Traumatismo craneal: lesiones según su localización"
  },
  "INF-014": {
    titulo: "Fiebre tifoidea: evolución y complicaciones",
    imagen: "flujogramas/fiebre-tifoidea-complicaciones.svg",
    alt: "Flujograma: Fiebre tifoidea: evolución y complicaciones"
  },
  "CAR-015": {
    titulo: "Dolor torácico con troponina elevada",
    imagen: "flujogramas/dolor-toracico-troponina-takotsubo.svg",
    alt: "Flujograma: Dolor torácico con troponina elevada"
  },
  "CAR-016": {
    titulo: "Síndrome aórtico agudo",
    imagen: "flujogramas/sindrome-aortico-agudo-diseccion.svg",
    alt: "Flujograma: Síndrome aórtico agudo"
  },
  "NEU-007": {
    titulo: "Insuficiencia respiratoria aguda: soporte",
    imagen: "flujogramas/insuficiencia-respiratoria-soporte-ventilatorio.svg",
    alt: "Flujograma: Insuficiencia respiratoria aguda: soporte"
  },
  "CAR-017": {
    titulo: "Pericarditis: enfoque etiológico",
    imagen: "flujogramas/pericarditis-enfoque-etiologico-tuberculosa.svg",
    alt: "Flujograma: Pericarditis: enfoque etiológico"
  },
  "INF-015": {
    titulo: "Úlcera genital y sífilis",
    imagen: "flujogramas/ulcera-genital-sifilis-histopatologia.svg",
    alt: "Flujograma: Úlcera genital y sífilis"
  },
  "GAS-009": {
    titulo: "Colitis ulcerosa y sus complicaciones",
    imagen: "flujogramas/colitis-ulcerosa-cancer-colorrectal.svg",
    alt: "Flujograma: Colitis ulcerosa y sus complicaciones"
  },
  "GAS-010": {
    titulo: "Enfermedad de Crohn: complicaciones",
    imagen: "flujogramas/enfermedad-crohn-fistulas.svg",
    alt: "Flujograma: Enfermedad de Crohn: complicaciones"
  },
  "GAS-011": {
    titulo: "Diarrea crónica: enfoque por tipo",
    imagen: "flujogramas/diarrea-cronica-malabsorcion-esteatorrea.svg",
    alt: "Flujograma: Diarrea crónica: enfoque por tipo"
  },
  "CIR-022": {
    titulo: "Isquemia mesentérica aguda",
    imagen: "flujogramas/isquemia-mesenterica-aguda-etiologia.svg",
    alt: "Flujograma: Isquemia mesentérica aguda"
  },
  "CAR-018": {
    titulo: "Muerte súbita en el joven deportista",
    imagen: "flujogramas/muerte-subita-joven-miocardiopatia-hipertrofica.svg",
    alt: "Flujograma: Muerte súbita en el joven deportista"
  },
  "NEU-008": {
    titulo: "Derrame pleural: criterios de Light",
    imagen: "flujogramas/derrame-pleural-trasudado-light.svg",
    alt: "Flujograma: Derrame pleural: criterios de Light"
  },
  "INF-016": {
    titulo: "Enfermedades metaxénicas y sus vectores",
    imagen: "flujogramas/metaxenicas-vectores-peru-dengue.svg",
    alt: "Flujograma: Enfermedades metaxénicas y sus vectores"
  },
  "SP-022": {
    titulo: "Adecuación del esfuerzo terapéutico",
    imagen: "flujogramas/adecuacion-esfuerzo-terapeutico-paliativos.svg",
    alt: "Flujograma: Adecuación del esfuerzo terapéutico"
  },
  "SP-023": {
    titulo: "Certificado de defunción y muerte violenta",
    imagen: "flujogramas/certificado-defuncion-muerte-violenta.svg",
    alt: "Flujograma: Certificado de defunción y muerte violenta"
  },
  "END-007": {
    titulo: "Tirotoxicosis: enfoque diagnóstico",
    imagen: "flujogramas/tirotoxicosis-enfoque-tormenta-tiroidea.svg",
    alt: "Flujograma: Tirotoxicosis: enfoque diagnóstico"
  },
  "PED-036": {
    titulo: "ITU en el niño: estudio por imágenes",
    imagen: "flujogramas/itu-pediatrica-imagenes-reflujo.svg",
    alt: "Flujograma: ITU en el niño: estudio por imágenes"
  },
  "PED-037": {
    titulo: "Neumonía en menores de 5 años",
    imagen: "flujogramas/neumonia-menor-5-anos-clasificacion.svg",
    alt: "Flujograma: Neumonía en menores de 5 años"
  },
  "PED-038": {
    titulo: "Reanimación neonatal",
    imagen: "flujogramas/reanimacion-neonatal-algoritmo.svg",
    alt: "Flujograma: Reanimación neonatal"
  },
  "SP-024": {
    titulo: "Diseños de estudios epidemiológicos",
    imagen: "flujogramas/disenos-estudio-epidemiologico-ecologico.svg",
    alt: "Flujograma: Diseños de estudios epidemiológicos"
  },
  "OFT-007": {
    titulo: "Rinitis: clasificación",
    imagen: "flujogramas/rinitis-clasificacion-vasomotora.svg",
    alt: "Flujograma: Rinitis: clasificación"
  },
  "SP-025": {
    titulo: "Niveles de prevención",
    imagen: "flujogramas/niveles-prevencion-tuberculosis.svg",
    alt: "Flujograma: Niveles de prevención"
  },
  "SP-026": {
    titulo: "Peste: formas clínicas y contactos",
    imagen: "flujogramas/peste-formas-clinicas-contactos.svg",
    alt: "Flujograma: Peste: formas clínicas y contactos"
  },
  "PED-040": {
    titulo: "Sepsis neonatal: temprana y tardía",
    imagen: "flujogramas/sepsis-neonatal-temprana-tardia.svg",
    alt: "Flujograma: Sepsis neonatal: temprana y tardía"
  },
  "PED-041": {
    titulo: "Insuficiencia cardiaca en el lactante",
    imagen: "flujogramas/insuficiencia-cardiaca-lactante-furosemida.svg",
    alt: "Flujograma: Insuficiencia cardiaca en el lactante"
  },
  "SP-027": {
    titulo: "Calidad de atención: dimensiones SERVQUAL",
    imagen: "flujogramas/calidad-servqual-dimensiones.svg",
    alt: "Flujograma: Calidad de atención: dimensiones SERVQUAL"
  },
  "REU-010": {
    titulo: "Dermatosis pruriginosas del lactante",
    imagen: "flujogramas/dermatitis-atopica-lactante-diferencial-prurito.svg",
    alt: "Flujograma: Dermatosis pruriginosas del lactante"
  },
  "PED-042": {
    titulo: "Neumonía en el niño: típica, atípica y viral",
    imagen: "flujogramas/neumonia-nino-tipica-atipica-viral.svg",
    alt: "Flujograma: Neumonía en el niño: típica, atípica y viral"
  },
  "TRA-008": {
    titulo: "Tumores óseos en niños y adolescentes",
    imagen: "flujogramas/tumores-oseos-osteosarcoma.svg",
    alt: "Flujograma: Tumores óseos en niños y adolescentes"
  },
  "NRL-010": {
    titulo: "Debilidad aguda de miembros inferiores",
    imagen: "flujogramas/debilidad-aguda-mielitis-transversa.svg",
    alt: "Flujograma: Debilidad aguda de miembros inferiores"
  },
  "PED-043": {
    titulo: "Síndrome nefrítico en el niño",
    imagen: "flujogramas/sindrome-nefritico-glomerulonefritis-postestreptococica.svg",
    alt: "Flujograma: Síndrome nefrítico en el niño"
  },
  "INF-017": {
    titulo: "Síndrome de secreción uretral",
    imagen: "flujogramas/secrecion-uretral-manejo-sindromico.svg",
    alt: "Flujograma: Síndrome de secreción uretral"
  },
  "INF-018": {
    titulo: "Meningitis bacteriana según la edad",
    imagen: "flujogramas/meningitis-bacteriana-edad-meningococo.svg",
    alt: "Flujograma: Meningitis bacteriana según la edad"
  },
  "GAS-012": {
    titulo: "Hepatitis viral aguda: serología",
    imagen: "flujogramas/hepatitis-viral-aguda-serologia.svg",
    alt: "Flujograma: Hepatitis viral aguda: serología"
  },
  "NEF-017": {
    titulo: "Escroto agudo en el niño",
    imagen: "flujogramas/escroto-agudo-torsion-testicular.svg",
    alt: "Flujograma: Escroto agudo en el niño"
  },
  "PED-044": {
    titulo: "Lesiones del plexo braquial en el RN",
    imagen: "flujogramas/plexo-braquial-erb-duchenne.svg",
    alt: "Flujograma: Lesiones del plexo braquial en el RN"
  },
  "PED-045": {
    titulo: "Convulsiones neonatales",
    imagen: "flujogramas/convulsiones-neonatales-tipos.svg",
    alt: "Flujograma: Convulsiones neonatales"
  },
  "PED-046": {
    titulo: "Ictericia neonatal indirecta",
    imagen: "flujogramas/ictericia-neonatal-indirecta-policitemia.svg",
    alt: "Flujograma: Ictericia neonatal indirecta"
  },
  "NRL-011": {
    titulo: "TEC: indicaciones de TC",
    imagen: "flujogramas/tec-indicaciones-tomografia.svg",
    alt: "Flujograma: TEC: indicaciones de TC"
  },
  "HEM-005": {
    titulo: "Anemia microcítica: enfoque diagnóstico",
    imagen: "flujogramas/anemia-microcitica-enfoque-diagnostico.svg",
    alt: "Flujograma: Anemia microcítica: enfoque diagnóstico"
  },
  "PED-039": {
    titulo: "Edema en el niño: síndrome nefrótico y nefrítico",
    imagen: "flujogramas/edema-renal-nino-nefrotico-nefritico.svg",
    alt: "Flujograma: Edema en el niño: síndrome nefrótico y nefrítico"
  },
  /* ── Bloque 4: 100 flujogramas (diseños árbol, radial, fases, termómetro y tarjetas) ── */
  "TRA-009": {
    titulo: "Lesiones nerviosas en fracturas del miembro superior",
    imagen: "flujogramas/fractura-humero-lesion-nervio-radial.svg",
    alt: "Flujograma: Lesiones nerviosas en fracturas del miembro superior"
  },
  "CIR-023": {
    titulo: "Obstrucción intestinal: diagnóstico y causa",
    imagen: "flujogramas/obstruccion-intestinal-bridas.svg",
    alt: "Flujograma: Obstrucción intestinal: diagnóstico y causa"
  },
  "SP-028": {
    titulo: "Principios de la bioética",
    imagen: "flujogramas/principios-bioetica-justicia.svg",
    alt: "Flujograma: Principios de la bioética"
  },
  "SP-029": {
    titulo: "Diseños de investigación",
    imagen: "flujogramas/disenos-investigacion-transversal.svg",
    alt: "Flujograma: Diseños de investigación"
  },
  "CIR-024": {
    titulo: "Hernias de la región inguinal",
    imagen: "flujogramas/hernias-ingle-directa.svg",
    alt: "Flujograma: Hernias de la región inguinal"
  },
  "SP-030": {
    titulo: "COVID-19: definiciones operativas",
    imagen: "flujogramas/covid-definicion-contacto-directo.svg",
    alt: "Flujograma: COVID-19: definiciones operativas"
  },
  "CIR-025": {
    titulo: "Shock séptico: control del foco",
    imagen: "flujogramas/shock-septico-control-foco.svg",
    alt: "Flujograma: Shock séptico: control del foco"
  },
  "CAR-019": {
    titulo: "Paro cardiorrespiratorio: primeros minutos",
    imagen: "flujogramas/paro-cardiorrespiratorio-rcp-monitor.svg",
    alt: "Flujograma: Paro cardiorrespiratorio: primeros minutos"
  },
  "CB-012": {
    titulo: "Citocromo P450 e interacciones",
    imagen: "flujogramas/citocromo-p450-interacciones.svg",
    alt: "Flujograma: Citocromo P450 e interacciones"
  },
  "GIN-042": {
    titulo: "Hemorragias de la segunda mitad del embarazo",
    imagen: "flujogramas/hemorragia-tercer-trimestre-dpp.svg",
    alt: "Flujograma: Hemorragias de la segunda mitad del embarazo"
  },
  "GIN-043": {
    titulo: "Dolor abdominal agudo en la gestante",
    imagen: "flujogramas/dolor-abdominal-gestante-apendicitis.svg",
    alt: "Flujograma: Dolor abdominal agudo en la gestante"
  },
  "GIN-044": {
    titulo: "Parto podálico: tiempos y maniobras",
    imagen: "flujogramas/parto-podalico-maniobras.svg",
    alt: "Flujograma: Parto podálico: tiempos y maniobras"
  },
  "CB-013": {
    titulo: "Surfactante pulmonar",
    imagen: "flujogramas/surfactante-pulmonar-lecitina.svg",
    alt: "Flujograma: Surfactante pulmonar"
  },
  "GIN-045": {
    titulo: "Candidiasis vulvovaginal",
    imagen: "flujogramas/candidiasis-vulvovaginal-recurrente.svg",
    alt: "Flujograma: Candidiasis vulvovaginal"
  },
  "REU-011": {
    titulo: "Dolor musculoesquelético difuso",
    imagen: "flujogramas/fibromialgia-diagnostico-diferencial.svg",
    alt: "Flujograma: Dolor musculoesquelético difuso"
  },
  "NRL-012": {
    titulo: "Déficit de tiamina: Wernicke y Korsakoff",
    imagen: "flujogramas/deficit-tiamina-wernicke-korsakoff.svg",
    alt: "Flujograma: Déficit de tiamina: Wernicke y Korsakoff"
  },
  "INF-019": {
    titulo: "Infecciones del SNC en el paciente con VIH",
    imagen: "flujogramas/vih-infecciones-snc-criptococo.svg",
    alt: "Flujograma: Infecciones del SNC en el paciente con VIH"
  },
  "CIR-026": {
    titulo: "Mordeduras: manejo inicial",
    imagen: "flujogramas/mordeduras-humana-animal-manejo.svg",
    alt: "Flujograma: Mordeduras: manejo inicial"
  },
  "SP-031": {
    titulo: "Decisiones al final de la vida",
    imagen: "flujogramas/final-vida-obstinacion-terapeutica.svg",
    alt: "Flujograma: Decisiones al final de la vida"
  },
  "SP-032": {
    titulo: "Violencia contra la mujer: conducta del médico",
    imagen: "flujogramas/violencia-mujer-denuncia-ley-30364.svg",
    alt: "Flujograma: Violencia contra la mujer: conducta del médico"
  },
  "REU-012": {
    titulo: "Urticaria: clasificación y tratamiento",
    imagen: "flujogramas/urticaria-antihistaminico-escalera.svg",
    alt: "Flujograma: Urticaria: clasificación y tratamiento"
  },
  "NEF-018": {
    titulo: "Síndrome nefrótico del adulto: biopsia renal",
    imagen: "flujogramas/sindrome-nefrotico-amiloidosis-aa.svg",
    alt: "Flujograma: Síndrome nefrótico del adulto: biopsia renal"
  },
  "NEF-019": {
    titulo: "Indicaciones de diálisis urgente",
    imagen: "flujogramas/dialisis-urgente-pericarditis-uremica.svg",
    alt: "Flujograma: Indicaciones de diálisis urgente"
  },
  "NEF-020": {
    titulo: "Lesión renal aguda intrínseca",
    imagen: "flujogramas/lesion-renal-intrinseca-nefritis-intersticial.svg",
    alt: "Flujograma: Lesión renal aguda intrínseca"
  },
  "REU-013": {
    titulo: "Escabiosis: diagnóstico y tratamiento",
    imagen: "flujogramas/escabiosis-lactante-permetrina.svg",
    alt: "Flujograma: Escabiosis: diagnóstico y tratamiento"
  },
  "CIR-027": {
    titulo: "Quemadura con lesión por inhalación",
    imagen: "flujogramas/quemadura-lesion-inhalatoria-oxigeno.svg",
    alt: "Flujograma: Quemadura con lesión por inhalación"
  },
  "PED-047": {
    titulo: "Vómitos en el neonato y el lactante",
    imagen: "flujogramas/vomitos-neonato-estenosis-piloro.svg",
    alt: "Flujograma: Vómitos en el neonato y el lactante"
  },
  "PED-048": {
    titulo: "Sibilancias en el niño",
    imagen: "flujogramas/sibilancias-nino-asma.svg",
    alt: "Flujograma: Sibilancias en el niño"
  },
  "PED-049": {
    titulo: "Neumonía en el niño",
    imagen: "flujogramas/neumonia-nino-hospitalizado-ceftriaxona.svg",
    alt: "Flujograma: Neumonía en el niño"
  },
  "CB-014": {
    titulo: "Aterosclerosis: capa afectada y evolución",
    imagen: "flujogramas/aterosclerosis-capa-intima.svg",
    alt: "Flujograma: Aterosclerosis: capa afectada y evolución"
  },
  "CIR-028": {
    titulo: "Enfermedad arterial periférica",
    imagen: "flujogramas/enfermedad-arterial-periferica-bypass.svg",
    alt: "Flujograma: Enfermedad arterial periférica"
  },
  "PED-050": {
    titulo: "Dificultad respiratoria quirúrgica del recién nacido",
    imagen: "flujogramas/hernia-diafragmatica-congenita-rx.svg",
    alt: "Flujograma: Dificultad respiratoria quirúrgica del recién nacido"
  },
  "SP-033": {
    titulo: "Derechos de los usuarios de salud",
    imagen: "flujogramas/derechos-usuario-salud-informacion.svg",
    alt: "Flujograma: Derechos de los usuarios de salud"
  },
  "HEM-006": {
    titulo: "Reacciones transfusionales agudas",
    imagen: "flujogramas/reacciones-transfusionales-trali.svg",
    alt: "Flujograma: Reacciones transfusionales agudas"
  },
  "CAR-020": {
    titulo: "Shock con ingurgitación yugular",
    imagen: "flujogramas/shock-obstructivo-taponamiento-cardiaco.svg",
    alt: "Flujograma: Shock con ingurgitación yugular"
  },
  "HEM-007": {
    titulo: "Anemia microcítica: estudio",
    imagen: "flujogramas/anemia-microcitica-estudio-ferritina.svg",
    alt: "Flujograma: Anemia microcítica: estudio"
  },
  "CAR-021": {
    titulo: "Valvulopatías: cómo reconocerlas",
    imagen: "flujogramas/valvulopatias-estenosis-mitral.svg",
    alt: "Flujograma: Valvulopatías: cómo reconocerlas"
  },
  "CAR-022": {
    titulo: "Taquicardias: enfoque inicial",
    imagen: "flujogramas/taquicardias-fibrilacion-auricular.svg",
    alt: "Flujograma: Taquicardias: enfoque inicial"
  },
  "GAS-013": {
    titulo: "Colitis crónicas: diagnóstico diferencial",
    imagen: "flujogramas/colitis-ulcerosa-espondiloartritis.svg",
    alt: "Flujograma: Colitis crónicas: diagnóstico diferencial"
  },
  "GAS-014": {
    titulo: "Tumores gástricos",
    imagen: "flujogramas/tumores-gastricos-adenocarcinoma.svg",
    alt: "Flujograma: Tumores gástricos"
  },
  "NEU-009": {
    titulo: "Lesiones pulmonares cavitadas: agente",
    imagen: "flujogramas/neumonia-cavitada-tuberculosis.svg",
    alt: "Flujograma: Lesiones pulmonares cavitadas: agente"
  },
  "NEU-010": {
    titulo: "Enfermedad pulmonar intersticial difusa",
    imagen: "flujogramas/epid-fibrosis-pulmonar-idiopatica.svg",
    alt: "Flujograma: Enfermedad pulmonar intersticial difusa"
  },
  "CAR-023": {
    titulo: "Miocardiopatías",
    imagen: "flujogramas/miocardiopatias-dilatada-alcoholica.svg",
    alt: "Flujograma: Miocardiopatías"
  },
  "PED-051": {
    titulo: "Fracturas en el niño: ¿accidente o maltrato?",
    imagen: "flujogramas/maltrato-infantil-fracturas.svg",
    alt: "Flujograma: Fracturas en el niño: ¿accidente o maltrato?"
  },
  "INF-020": {
    titulo: "Líquido cefalorraquídeo en las meningitis",
    imagen: "flujogramas/lcr-meningitis-bacteriana.svg",
    alt: "Flujograma: Líquido cefalorraquídeo en las meningitis"
  },
  "PED-052": {
    titulo: "Atresia de esófago",
    imagen: "flujogramas/atresia-esofagica-rx-torax.svg",
    alt: "Flujograma: Atresia de esófago"
  },
  "INF-021": {
    titulo: "Giardiasis: ciclo y formas",
    imagen: "flujogramas/giardiasis-ciclo-trofozoitos.svg",
    alt: "Flujograma: Giardiasis: ciclo y formas"
  },
  "PED-053": {
    titulo: "Deshidratación por diarrea: planes A, B y C",
    imagen: "flujogramas/deshidratacion-plan-c-rehidratacion.svg",
    alt: "Flujograma: Deshidratación por diarrea: planes A, B y C"
  },
  "GIN-046": {
    titulo: "Hiperémesis grave: clínica y ética",
    imagen: "flujogramas/hiperemesis-gravidica-autonomia.svg",
    alt: "Flujograma: Hiperémesis grave: clínica y ética"
  },
  "PED-054": {
    titulo: "Neonato febril: estudio",
    imagen: "flujogramas/neonato-febril-meningitis-lcr.svg",
    alt: "Flujograma: Neonato febril: estudio"
  },
  "INF-022": {
    titulo: "Dengue: fases clínicas y clasificación",
    imagen: "flujogramas/dengue-fases-clasificacion.svg",
    alt: "Flujograma: Dengue: fases clínicas y clasificación"
  },
  "SP-034": {
    titulo: "Atención primaria de salud",
    imagen: "flujogramas/atencion-primaria-salud-alma-ata.svg",
    alt: "Flujograma: Atención primaria de salud"
  },
  "SP-035": {
    titulo: "Primer nivel de atención en pandemia",
    imagen: "flujogramas/primer-nivel-pandemia-salud-mental.svg",
    alt: "Flujograma: Primer nivel de atención en pandemia"
  },
  "OFT-008": {
    titulo: "Otitis media aguda",
    imagen: "flujogramas/otitis-media-aguda-edad-gravedad.svg",
    alt: "Flujograma: Otitis media aguda"
  },
  "PED-055": {
    titulo: "Rubéola congénita",
    imagen: "flujogramas/rubeola-congenita-catarata.svg",
    alt: "Flujograma: Rubéola congénita"
  },
  "SP-036": {
    titulo: "MAIS-BFC: componentes",
    imagen: "flujogramas/mais-bfc-componente-organizacion.svg",
    alt: "Flujograma: MAIS-BFC: componentes"
  },
  "END-008": {
    titulo: "Diabetes mellitus: diagnóstico",
    imagen: "flujogramas/diabetes-diagnostico-glucemia-ayunas.svg",
    alt: "Flujograma: Diabetes mellitus: diagnóstico"
  },
  "NEF-021": {
    titulo: "Hiperplasia benigna de próstata",
    imagen: "flujogramas/hiperplasia-prostatica-alfabloqueador.svg",
    alt: "Flujograma: Hiperplasia benigna de próstata"
  },
  "END-009": {
    titulo: "Hipotensión refractaria: crisis suprarrenal",
    imagen: "flujogramas/crisis-suprarrenal-retiro-corticoides.svg",
    alt: "Flujograma: Hipotensión refractaria: crisis suprarrenal"
  },
  "SP-037": {
    titulo: "Clasificación de la persona adulta mayor",
    imagen: "flujogramas/adulto-mayor-fragil-clasificacion.svg",
    alt: "Flujograma: Clasificación de la persona adulta mayor"
  },
  "GAS-015": {
    titulo: "Dispepsia: enfoque",
    imagen: "flujogramas/dispepsia-funcional-roma-iv.svg",
    alt: "Flujograma: Dispepsia: enfoque"
  },
  "GAS-016": {
    titulo: "Hemorragia por várices esofágicas",
    imagen: "flujogramas/hemorragia-variceal-ligadura.svg",
    alt: "Flujograma: Hemorragia por várices esofágicas"
  },
  "SP-038": {
    titulo: "Evaluaciones económicas en salud",
    imagen: "flujogramas/evaluacion-economica-minimizacion-costos.svg",
    alt: "Flujograma: Evaluaciones económicas en salud"
  },
  "NEU-011": {
    titulo: "Neumoconiosis",
    imagen: "flujogramas/neumoconiosis-silicosis.svg",
    alt: "Flujograma: Neumoconiosis"
  },
  "OFT-009": {
    titulo: "Rinitis: tipos",
    imagen: "flujogramas/rinitis-alergica-diagnostico.svg",
    alt: "Flujograma: Rinitis: tipos"
  },
  "CIR-029": {
    titulo: "Colecistitis aguda",
    imagen: "flujogramas/colecistitis-aguda-tokyo.svg",
    alt: "Flujograma: Colecistitis aguda"
  },
  "NEF-022": {
    titulo: "Hiperpotasemia: cambios en el ECG",
    imagen: "flujogramas/hiperpotasemia-cambios-electrocardiograma.svg",
    alt: "Flujograma: Hiperpotasemia: cambios en el ECG"
  },
  "INF-023": {
    titulo: "Diarrea aguda: agente según la clínica",
    imagen: "flujogramas/diarrea-disenterica-shigella.svg",
    alt: "Flujograma: Diarrea aguda: agente según la clínica"
  },
  "GAS-017": {
    titulo: "Pruebas hepáticas: qué mide cada una",
    imagen: "flujogramas/pruebas-hepaticas-transaminasas-nino.svg",
    alt: "Flujograma: Pruebas hepáticas: qué mide cada una"
  },
  "GAS-018": {
    titulo: "Dolor epigástrico agudo intenso",
    imagen: "flujogramas/dolor-epigastrico-pancreatitis-aguda.svg",
    alt: "Flujograma: Dolor epigástrico agudo intenso"
  },
  "CIR-030": {
    titulo: "Shock en el paciente traumatizado",
    imagen: "flujogramas/shock-trauma-hemorragia-intraabdominal.svg",
    alt: "Flujograma: Shock en el paciente traumatizado"
  },
  "INF-024": {
    titulo: "Síndrome febril en zona tropical",
    imagen: "flujogramas/sindrome-febril-malaria-gestante.svg",
    alt: "Flujograma: Síndrome febril en zona tropical"
  },
  "GIN-047": {
    titulo: "Masa ovárica en el embarazo",
    imagen: "flujogramas/masa-ovarica-embarazo-cirugia.svg",
    alt: "Flujograma: Masa ovárica en el embarazo"
  },
  "PSI-012": {
    titulo: "Trastornos del ánimo: ¿depresión o bipolar?",
    imagen: "flujogramas/trastorno-bipolar-depresion.svg",
    alt: "Flujograma: Trastornos del ánimo: ¿depresión o bipolar?"
  },
  "HEM-008": {
    titulo: "Lesiones óseas líticas: diagnóstico",
    imagen: "flujogramas/mieloma-multiple-crab.svg",
    alt: "Flujograma: Lesiones óseas líticas: diagnóstico"
  },
  "HEM-009": {
    titulo: "Microangiopatías trombóticas",
    imagen: "flujogramas/microangiopatia-trombotica-ptt-plasma.svg",
    alt: "Flujograma: Microangiopatías trombóticas"
  },
  "HEM-010": {
    titulo: "Déficit de hierro: etapas",
    imagen: "flujogramas/ferropenia-etapas-anemia.svg",
    alt: "Flujograma: Déficit de hierro: etapas"
  },
  "NEU-012": {
    titulo: "Acidosis respiratoria aguda: hipoventilación",
    imagen: "flujogramas/hipoventilacion-benzodiacepinas-soporte.svg",
    alt: "Flujograma: Acidosis respiratoria aguda: hipoventilación"
  },
  "NEF-023": {
    titulo: "Lesión renal aguda: estadios y manejo",
    imagen: "flujogramas/lesion-renal-aguda-postoperatoria-volumen.svg",
    alt: "Flujograma: Lesión renal aguda: estadios y manejo"
  },
  "END-010": {
    titulo: "Hipotiroidismo y bocio",
    imagen: "flujogramas/hipotiroidismo-tiroiditis-hashimoto.svg",
    alt: "Flujograma: Hipotiroidismo y bocio"
  },
  "END-011": {
    titulo: "Emergencias glucémicas en el diabético",
    imagen: "flujogramas/emergencias-glucemicas-hiperosmolar.svg",
    alt: "Flujograma: Emergencias glucémicas en el diabético"
  },
  "END-012": {
    titulo: "Hipoglucemia en el diabético",
    imagen: "flujogramas/hipoglucemia-grave-glucosa-ev.svg",
    alt: "Flujograma: Hipoglucemia en el diabético"
  },
  "GAS-019": {
    titulo: "Ascitis con confusión: ¿qué falla?",
    imagen: "flujogramas/ascitis-confusion-falla-hepatica-cronica.svg",
    alt: "Flujograma: Ascitis con confusión: ¿qué falla?"
  },
  "NRL-013": {
    titulo: "Coma de causa desconocida: primeras medidas",
    imagen: "flujogramas/coma-alcoholico-tiamina-ev.svg",
    alt: "Flujograma: Coma de causa desconocida: primeras medidas"
  },
  "NEU-013": {
    titulo: "Exacerbación de la EPOC",
    imagen: "flujogramas/exacerbacion-epoc-antibiotico.svg",
    alt: "Flujograma: Exacerbación de la EPOC"
  },
  "INF-025": {
    titulo: "Parásitos intestinales: vías de ingreso",
    imagen: "flujogramas/parasitos-via-ingreso-penetracion-cutanea.svg",
    alt: "Flujograma: Parásitos intestinales: vías de ingreso"
  },
  "INF-026": {
    titulo: "Infecciones granulomatosas de zona rural",
    imagen: "flujogramas/micosis-endemicas-paracoccidioidomicosis.svg",
    alt: "Flujograma: Infecciones granulomatosas de zona rural"
  },
  "NEU-014": {
    titulo: "Neumonía típica y atípica",
    imagen: "flujogramas/neumonia-atipica-mycoplasma.svg",
    alt: "Flujograma: Neumonía típica y atípica"
  },
  "NEU-015": {
    titulo: "Neumonía adquirida en la comunidad: tratamiento",
    imagen: "flujogramas/neumonia-comunidad-curb65-tratamiento.svg",
    alt: "Flujograma: Neumonía adquirida en la comunidad: tratamiento"
  },
  "CAR-024": {
    titulo: "Insuficiencia cardiaca aguda: perfiles",
    imagen: "flujogramas/insuficiencia-cardiaca-aguda-perfiles.svg",
    alt: "Flujograma: Insuficiencia cardiaca aguda: perfiles"
  },
  "CAR-025": {
    titulo: "Criterios de Framingham",
    imagen: "flujogramas/criterios-framingham-insuficiencia-cardiaca.svg",
    alt: "Flujograma: Criterios de Framingham"
  },
  "CAR-026": {
    titulo: "Infarto con ST elevado: objetivo del tratamiento",
    imagen: "flujogramas/infarto-st-elevado-limitar-necrosis.svg",
    alt: "Flujograma: Infarto con ST elevado: objetivo del tratamiento"
  },
  "GAS-020": {
    titulo: "Derrame pleural: estudio del líquido",
    imagen: "flujogramas/derrame-pleural-pancreatico-amilasa.svg",
    alt: "Flujograma: Derrame pleural: estudio del líquido"
  },
  "NRL-014": {
    titulo: "Dolor neuropático diabético",
    imagen: "flujogramas/dolor-neuropatico-diabetico-gabapentina.svg",
    alt: "Flujograma: Dolor neuropático diabético"
  },
  "END-013": {
    titulo: "Hipocalcemia tras tiroidectomía",
    imagen: "flujogramas/hipocalcemia-postiroidectomia-calcio-ionico.svg",
    alt: "Flujograma: Hipocalcemia tras tiroidectomía"
  },
  "NEF-024": {
    titulo: "Alteración de conciencia en el hospitalizado",
    imagen: "flujogramas/hiponatremia-hospitalaria-dosaje-sodio.svg",
    alt: "Flujograma: Alteración de conciencia en el hospitalizado"
  },
  "NEF-025": {
    titulo: "Hiperpotasemia: gravedad y manejo",
    imagen: "flujogramas/hiperpotasemia-gravedad-manejo.svg",
    alt: "Flujograma: Hiperpotasemia: gravedad y manejo"
  },
  "REU-014": {
    titulo: "Inflamación del pliegue ungueal",
    imagen: "flujogramas/paroniquia-cronica-candidiasica.svg",
    alt: "Flujograma: Inflamación del pliegue ungueal"
  },
  "HEM-011": {
    titulo: "Anemias microcíticas: perfil de hierro",
    imagen: "flujogramas/anemia-enfermedad-cronica-perfil-hierro.svg",
    alt: "Flujograma: Anemias microcíticas: perfil de hierro"
  },
  "CIR-031": {
    titulo: "Ritmos de paro cardiaco",
    imagen: "flujogramas/ritmos-paro-disociacion-electromecanica.svg",
    alt: "Flujograma: Ritmos de paro cardiaco"
  },
  "CB-015": {
    titulo: "Shock hipovolémico: mecanismos compensadores",
    imagen: "flujogramas/shock-hipovolemico-compensacion-taquicardia.svg",
    alt: "Flujograma: Shock hipovolémico: mecanismos compensadores"
  },
  "REU-015": {
    titulo: "Anafilaxia: gravedad y tratamiento",
    imagen: "flujogramas/anafilaxia-grados-adrenalina.svg",
    alt: "Flujograma: Anafilaxia: gravedad y tratamiento"
  },
  "NEU-016": {
    titulo: "Tromboembolismo pulmonar: probabilidad clínica",
    imagen: "flujogramas/tromboembolismo-pulmonar-wells.svg",
    alt: "Flujograma: Tromboembolismo pulmonar: probabilidad clínica"
  },
  "NEF-026": {
    titulo: "Síndrome de aplastamiento y rabdomiólisis",
    imagen: "flujogramas/sindrome-aplastamiento-rabdomiolisis-renal.svg",
    alt: "Flujograma: Síndrome de aplastamiento y rabdomiólisis"
  },
  "CB-016": {
    titulo: "Toxíndromes: reconocerlos al pie de la cama",
    imagen: "flujogramas/toxindromes-colinergico-organofosforados.svg",
    alt: "Flujograma: Toxíndromes: reconocerlos al pie de la cama"
  },
  "NEU-017": {
    titulo: "Derrame pleural linfocítico",
    imagen: "flujogramas/derrame-pleural-linfocitico-ada-tuberculosis.svg",
    alt: "Flujograma: Derrame pleural linfocítico"
  },
  "CIR-032": {
    titulo: "Enfermedad arterial periférica: índice tobillo-brazo",
    imagen: "flujogramas/claudicacion-indice-tobillo-brazo.svg",
    alt: "Flujograma: Enfermedad arterial periférica: índice tobillo-brazo"
  },
  "CAR-027": {
    titulo: "Angioedema: ¿por qué fármaco?",
    imagen: "flujogramas/angioedema-ieca-bradicinina.svg",
    alt: "Flujograma: Angioedema: ¿por qué fármaco?"
  },
  "PED-056": {
    titulo: "Anemia del prematuro",
    imagen: "flujogramas/anemia-prematuro-nadir-hemoglobina.svg",
    alt: "Flujograma: Anemia del prematuro"
  },
  "PED-057": {
    titulo: "Edema en el niño: nefrótico o nefrítico",
    imagen: "flujogramas/edema-nino-sindrome-nefrotico.svg",
    alt: "Flujograma: Edema en el niño: nefrótico o nefrítico"
  },
  "END-014": {
    titulo: "Pubertad precoz",
    imagen: "flujogramas/pubertad-precoz-prueba-gnrh.svg",
    alt: "Flujograma: Pubertad precoz"
  },
  "PED-058": {
    titulo: "Convulsiones neonatales por asfixia",
    imagen: "flujogramas/encefalopatia-hipoxica-convulsiones-fenobarbital.svg",
    alt: "Flujograma: Convulsiones neonatales por asfixia"
  },
  "PED-059": {
    titulo: "Invaginación intestinal",
    imagen: "flujogramas/invaginacion-intestinal-lactante.svg",
    alt: "Flujograma: Invaginación intestinal"
  },
  "PED-060": {
    titulo: "Lactante con sospecha de meningitis",
    imagen: "flujogramas/meningitis-lactante-estudio-lcr.svg",
    alt: "Flujograma: Lactante con sospecha de meningitis"
  },
  "PED-061": {
    titulo: "Infección respiratoria alta en el lactante",
    imagen: "flujogramas/resfrio-comun-lactante.svg",
    alt: "Flujograma: Infección respiratoria alta en el lactante"
  },
  "INF-027": {
    titulo: "Síndrome de Löffler",
    imagen: "flujogramas/sindrome-loffler-ascaris-albendazol.svg",
    alt: "Flujograma: Síndrome de Löffler"
  },
  "PED-062": {
    titulo: "Deshidratación: clasificación clínica",
    imagen: "flujogramas/deshidratacion-clasificacion-algun-grado.svg",
    alt: "Flujograma: Deshidratación: clasificación clínica"
  },
  "PED-063": {
    titulo: "Síndrome urémico hemolítico",
    imagen: "flujogramas/sindrome-uremico-hemolitico-nino.svg",
    alt: "Flujograma: Síndrome urémico hemolítico"
  },
  "PED-064": {
    titulo: "Crup: gravedad con la escala de Westley",
    imagen: "flujogramas/crup-laringotraqueitis-westley.svg",
    alt: "Flujograma: Crup: gravedad con la escala de Westley"
  },
  "REU-016": {
    titulo: "Lesiones vesículo-costrosas en el niño",
    imagen: "flujogramas/impetigo-costras-melicericas.svg",
    alt: "Flujograma: Lesiones vesículo-costrosas en el niño"
  },
  "REU-017": {
    titulo: "Alopecia en placas en el niño",
    imagen: "flujogramas/alopecia-nino-tina-capitis.svg",
    alt: "Flujograma: Alopecia en placas en el niño"
  },
  "HEM-012": {
    titulo: "Recuento absoluto de neutrófilos",
    imagen: "flujogramas/recuento-absoluto-neutrofilos-calculo.svg",
    alt: "Flujograma: Recuento absoluto de neutrófilos"
  },
  "CIR-033": {
    titulo: "Apendicitis: escala de Alvarado",
    imagen: "flujogramas/apendicitis-escala-alvarado.svg",
    alt: "Flujograma: Apendicitis: escala de Alvarado"
  },
  "CIR-034": {
    titulo: "Lesiones vasculares tardías tras un trauma",
    imagen: "flujogramas/fistula-arteriovenosa-traumatica.svg",
    alt: "Flujograma: Lesiones vasculares tardías tras un trauma"
  },
  "CIR-035": {
    titulo: "Insuficiencia venosa crónica",
    imagen: "flujogramas/insuficiencia-venosa-cronica-ceap.svg",
    alt: "Flujograma: Insuficiencia venosa crónica"
  },
  "CIR-036": {
    titulo: "Hemotórax traumático",
    imagen: "flujogramas/hemotorax-masivo-toracotomia.svg",
    alt: "Flujograma: Hemotórax traumático"
  },
  "OFT-010": {
    titulo: "Fracturas de la órbita",
    imagen: "flujogramas/fractura-orbita-blow-out-piso.svg",
    alt: "Flujograma: Fracturas de la órbita"
  },
  "OFT-011": {
    titulo: "Ojo rojo: tipos de conjuntivitis",
    imagen: "flujogramas/conjuntivitis-adenovirus-queratoconjuntivitis.svg",
    alt: "Flujograma: Ojo rojo: tipos de conjuntivitis"
  },
  "NEF-027": {
    titulo: "Masa testicular indolora",
    imagen: "flujogramas/masa-testicular-indolora-cancer.svg",
    alt: "Flujograma: Masa testicular indolora"
  },
  "NEF-028": {
    titulo: "Litiasis urinaria: qué imagen pedir",
    imagen: "flujogramas/colico-renal-imagenes-tomografia.svg",
    alt: "Flujograma: Litiasis urinaria: qué imagen pedir"
  },
  "TRA-010": {
    titulo: "Síndrome compartimental agudo",
    imagen: "flujogramas/sindrome-compartimental-fractura-tibia.svg",
    alt: "Flujograma: Síndrome compartimental agudo"
  },
  "TRA-011": {
    titulo: "Síndrome de embolia grasa",
    imagen: "flujogramas/embolia-grasa-schonfeld.svg",
    alt: "Flujograma: Síndrome de embolia grasa"
  },
  "CIR-037": {
    titulo: "Dolor perianal agudo",
    imagen: "flujogramas/dolor-perianal-absceso.svg",
    alt: "Flujograma: Dolor perianal agudo"
  },
  "CIR-038": {
    titulo: "Masa que sale por el ano",
    imagen: "flujogramas/masa-anal-prolapso-rectal.svg",
    alt: "Flujograma: Masa que sale por el ano"
  },
  "OFT-012": {
    titulo: "Rinitis crónica: alérgica o no alérgica",
    imagen: "flujogramas/rinitis-alergica-eosinofilica-diferencial.svg",
    alt: "Flujograma: Rinitis crónica: alérgica o no alérgica"
  },
  "OFT-013": {
    titulo: "Epistaxis: medidas según el caso",
    imagen: "flujogramas/epistaxis-traumatica-taponamiento-anterior.svg",
    alt: "Flujograma: Epistaxis: medidas según el caso"
  },
  "NRL-015": {
    titulo: "Hallazgos en la TC cerebral",
    imagen: "flujogramas/hipertension-endocraneana-lesion-anillo.svg",
    alt: "Flujograma: Hallazgos en la TC cerebral"
  },
  "NRL-016": {
    titulo: "TEC con intervalo lúcido",
    imagen: "flujogramas/tec-intervalo-lucido-hematoma-epidural.svg",
    alt: "Flujograma: TEC con intervalo lúcido"
  },
  "PED-065": {
    titulo: "Dificultad respiratoria neonatal con abdomen excavado",
    imagen: "flujogramas/distres-neonatal-hernia-diafragmatica-clinica.svg",
    alt: "Flujograma: Dificultad respiratoria neonatal con abdomen excavado"
  },
  "SP-039": {
    titulo: "Principios bioéticos en la práctica",
    imagen: "flujogramas/autonomia-anticoncepcion-emergencia-violacion.svg",
    alt: "Flujograma: Principios bioéticos en la práctica"
  },
  "GIN-048": {
    titulo: "Desprendimiento prematuro de placenta: gravedad",
    imagen: "flujogramas/desprendimiento-placenta-grado-obito.svg",
    alt: "Flujograma: Desprendimiento prematuro de placenta: gravedad"
  },
  "GIN-049": {
    titulo: "Fiebre en el puerperio",
    imagen: "flujogramas/fiebre-puerperal-endometritis.svg",
    alt: "Flujograma: Fiebre en el puerperio"
  },
  "GIN-050": {
    titulo: "Fiebre en la gestante con membranas rotas",
    imagen: "flujogramas/fiebre-gestante-rpm-corioamnionitis.svg",
    alt: "Flujograma: Fiebre en la gestante con membranas rotas"
  },
  "GIN-051": {
    titulo: "Infección urinaria en el embarazo: antibiótico",
    imagen: "flujogramas/pielonefritis-gestante-antibiotico.svg",
    alt: "Flujograma: Infección urinaria en el embarazo: antibiótico"
  },
  "GIN-052": {
    titulo: "Embarazo prolongado: índice de Bishop",
    imagen: "flujogramas/embarazo-prolongado-bishop-induccion.svg",
    alt: "Flujograma: Embarazo prolongado: índice de Bishop"
  },
  "GIN-053": {
    titulo: "Distocia de hombros: secuencia de maniobras",
    imagen: "flujogramas/distocia-hombros-mcroberts.svg",
    alt: "Flujograma: Distocia de hombros: secuencia de maniobras"
  },
  "GIN-054": {
    titulo: "Sangrado posmenopáusico",
    imagen: "flujogramas/sangrado-posmenopausico-biopsia-endometrio.svg",
    alt: "Flujograma: Sangrado posmenopáusico"
  },
  "GIN-055": {
    titulo: "Flujo vaginal: tipos de vaginitis",
    imagen: "flujogramas/vaginitis-mixta-metronidazol-clotrimazol.svg",
    alt: "Flujograma: Flujo vaginal: tipos de vaginitis"
  },
  "GIN-056": {
    titulo: "Tumores de ovario según la edad",
    imagen: "flujogramas/tumores-ovaricos-nina-celulas-germinales.svg",
    alt: "Flujograma: Tumores de ovario según la edad"
  },
  "PED-066": {
    titulo: "Niño de 6 años sin vacunas",
    imagen: "flujogramas/vacunacion-tardia-seis-anos-hib.svg",
    alt: "Flujograma: Niño de 6 años sin vacunas"
  },
  "CB-017": {
    titulo: "Apoptosis",
    imagen: "flujogramas/apoptosis-dano-adn-p53.svg",
    alt: "Flujograma: Apoptosis"
  },
  "CB-018": {
    titulo: "Eficacia, efectividad y eficiencia",
    imagen: "flujogramas/eficacia-efectividad-eficiencia.svg",
    alt: "Flujograma: Eficacia, efectividad y eficiencia"
  },
  "CB-019": {
    titulo: "Mialgias tras iniciar un hipolipemiante",
    imagen: "flujogramas/mialgias-estatinas-reaccion-adversa.svg",
    alt: "Flujograma: Mialgias tras iniciar un hipolipemiante"
  },
  "CB-020": {
    titulo: "Músculos intrínsecos de la laringe",
    imagen: "flujogramas/musculos-laringe-cricoaritenoideo-posterior.svg",
    alt: "Flujograma: Músculos intrínsecos de la laringe"
  },
  "GIN-057": {
    titulo: "Claves obstétricas",
    imagen: "flujogramas/claves-obstetricas-roja-azul-amarilla.svg",
    alt: "Flujograma: Claves obstétricas"
  },
  "NEU-018": {
    titulo: "Dolor de hombro en un fumador",
    imagen: "flujogramas/dolor-hombro-fumador-pancoast.svg",
    alt: "Flujograma: Dolor de hombro en un fumador"
  },
  "SP-040": {
    titulo: "Determinantes sociales de la salud",
    imagen: "flujogramas/determinantes-sociales-estructurales-etnia.svg",
    alt: "Flujograma: Determinantes sociales de la salud"
  },
  "SP-041": {
    titulo: "Diseños de estudio: cómo elegir",
    imagen: "flujogramas/disenos-estudio-cohorte-matriz.svg",
    alt: "Flujograma: Diseños de estudio: cómo elegir"
  },
  "CB-021": {
    titulo: "Antídotos de uso frecuente",
    imagen: "flujogramas/antidotos-sarin-atropina.svg",
    alt: "Flujograma: Antídotos de uso frecuente"
  },
  "SP-042": {
    titulo: "Ética en la investigación con personas",
    imagen: "flujogramas/etica-investigacion-helsinki-comite.svg",
    alt: "Flujograma: Ética en la investigación con personas"
  },
  "PED-067": {
    titulo: "Lactante con tos y sibilancias",
    imagen: "flujogramas/lactante-sibilancias-bronquiolitis.svg",
    alt: "Flujograma: Lactante con tos y sibilancias"
  },
  "END-015": {
    titulo: "Hipercolesterolemia familiar",
    imagen: "flujogramas/hipercolesterolemia-familiar-dutch-lipid.svg",
    alt: "Flujograma: Hipercolesterolemia familiar"
  },
  "GIN-058": {
    titulo: "Flujo espumoso con colpitis en fresa",
    imagen: "flujogramas/flujo-espumoso-colpitis-fresa-tricomonas.svg",
    alt: "Flujograma: Flujo espumoso con colpitis en fresa"
  },
  "CB-022": {
    titulo: "Coma de origen tóxico",
    imagen: "flujogramas/coma-toxico-benzodiacepinas-flumazenil.svg",
    alt: "Flujograma: Coma de origen tóxico"
  },
  "HEM-013": {
    titulo: "Adenopatías: cuándo biopsiar",
    imagen: "flujogramas/adenopatias-generalizadas-biopsia-linfoma.svg",
    alt: "Flujograma: Adenopatías: cuándo biopsiar"
  },
  "SP-043": {
    titulo: "Estudio experimental",
    imagen: "flujogramas/piramide-evidencia-estudio-experimental.svg",
    alt: "Flujograma: Estudio experimental"
  },
  "OFT-014": {
    titulo: "Lactante febril: qué explorar",
    imagen: "flujogramas/lactante-otalgia-otoscopia.svg",
    alt: "Flujograma: Lactante febril: qué explorar"
  },
  "NRL-017": {
    titulo: "Síndromes medulares incompletos",
    imagen: "flujogramas/sindromes-medulares-brown-sequard.svg",
    alt: "Flujograma: Síndromes medulares incompletos"
  },
  "PED-068": {
    titulo: "Lesiones en piel de distinta antigüedad",
    imagen: "flujogramas/lactante-equimosis-patron-maltrato.svg",
    alt: "Flujograma: Lesiones en piel de distinta antigüedad"
  },
  "PED-069": {
    titulo: "Sepsis neonatal: temprana y tardía",
    imagen: "flujogramas/sepsis-neonatal-temprana-tardia-matriz.svg",
    alt: "Flujograma: Sepsis neonatal: temprana y tardía"
  },
  "SP-044": {
    titulo: "Habilidades de gestión en salud",
    imagen: "flujogramas/gestion-salud-liderazgo-vacunacion.svg",
    alt: "Flujograma: Habilidades de gestión en salud"
  },
  "SP-045": {
    titulo: "Mordeduras por perros callejeros: coordinación",
    imagen: "flujogramas/mordeduras-perros-callejeros-municipalidad.svg",
    alt: "Flujograma: Mordeduras por perros callejeros: coordinación"
  },
  "GIN-059": {
    titulo: "Hemorragia posparto: las 4 T",
    imagen: "flujogramas/hemorragia-posparto-atonia-uterina.svg",
    alt: "Flujograma: Hemorragia posparto: las 4 T"
  },
  "PED-070": {
    titulo: "Alimentación complementaria y anemia",
    imagen: "flujogramas/alimentacion-complementaria-hierro-anemia.svg",
    alt: "Flujograma: Alimentación complementaria y anemia"
  },
  "REU-018": {
    titulo: "Líquido sinovial: clasificación",
    imagen: "flujogramas/liquido-sinovial-clasificacion.svg",
    alt: "Flujograma: Líquido sinovial: clasificación"
  },
  "NEF-029": {
    titulo: "Oliguria tras aplastamiento: qué pedir",
    imagen: "flujogramas/aplastamiento-oliguria-cpk.svg",
    alt: "Flujograma: Oliguria tras aplastamiento: qué pedir"
  },
  "OFT-015": {
    titulo: "Glaucoma agudo: elegir el fármaco",
    imagen: "flujogramas/glaucoma-agudo-asma-alergia-sulfas-manitol.svg",
    alt: "Flujograma: Glaucoma agudo: elegir el fármaco"
  },
  "GIN-060": {
    titulo: "Infección urinaria en el embarazo",
    imagen: "flujogramas/itu-embarazo-profilaxis-nitrofurantoina.svg",
    alt: "Flujograma: Infección urinaria en el embarazo"
  },
  "NRL-018": {
    titulo: "Ataque isquémico transitorio: riesgo",
    imagen: "flujogramas/ataque-isquemico-transitorio-abcd2.svg",
    alt: "Flujograma: Ataque isquémico transitorio: riesgo"
  },
  "CIR-039": {
    titulo: "Politraumatizado: escala de Glasgow",
    imagen: "flujogramas/politraumatizado-glasgow-intubacion.svg",
    alt: "Flujograma: Politraumatizado: escala de Glasgow"
  },
  "NEU-019": {
    titulo: "Masa pulmonar: cómo obtener la biopsia",
    imagen: "flujogramas/masa-pulmonar-central-broncofibroscopia.svg",
    alt: "Flujograma: Masa pulmonar: cómo obtener la biopsia"
  },
  "PSI-013": {
    titulo: "Síntomas emocionales tras un cambio de vida",
    imagen: "flujogramas/migracion-trastorno-adaptacion.svg",
    alt: "Flujograma: Síntomas emocionales tras un cambio de vida"
  },
  "PED-071": {
    titulo: "Vómito bilioso en el recién nacido",
    imagen: "flujogramas/vomito-bilioso-down-atresia-duodenal.svg",
    alt: "Flujograma: Vómito bilioso en el recién nacido"
  },
  "PED-072": {
    titulo: "Sarampión: evolución clínica",
    imagen: "flujogramas/sarampion-fases-vacunacion.svg",
    alt: "Flujograma: Sarampión: evolución clínica"
  },
  "PED-073": {
    titulo: "Intoxicación por insecticidas",
    imagen: "flujogramas/intoxicacion-insecticida-cosecha.svg",
    alt: "Flujograma: Intoxicación por insecticidas"
  },
  "SP-046": {
    titulo: "Análisis de situación de salud (ASIS)",
    imagen: "flujogramas/asis-analisis-del-entorno.svg",
    alt: "Flujograma: Análisis de situación de salud (ASIS)"
  },
  "REU-019": {
    titulo: "Arteritis de células gigantes",
    imagen: "flujogramas/arteritis-celulas-gigantes-corticoide.svg",
    alt: "Flujograma: Arteritis de células gigantes"
  },
  "END-016": {
    titulo: "Síndrome hipermetabólico",
    imagen: "flujogramas/hipermetabolismo-hipertiroidismo.svg",
    alt: "Flujograma: Síndrome hipermetabólico"
  },
  "GIN-061": {
    titulo: "Mama dolorosa en el puerperio",
    imagen: "flujogramas/mama-dolorosa-puerperio-mastitis.svg",
    alt: "Flujograma: Mama dolorosa en el puerperio"
  },
  "GIN-062": {
    titulo: "Sangrado en el tercer trimestre: dolor y origen",
    imagen: "flujogramas/sangrado-tercer-trimestre-rotura-uterina.svg",
    alt: "Flujograma: Sangrado en el tercer trimestre: dolor y origen"
  },
  "SP-047": {
    titulo: "Aumento de tuberculosis: ¿qué influye más?",
    imagen: "flujogramas/tuberculosis-hacinamiento-determinantes.svg",
    alt: "Flujograma: Aumento de tuberculosis: ¿qué influye más?"
  },
  "NEF-030": {
    titulo: "Dolor lumbar agudo con hematuria",
    imagen: "flujogramas/dolor-lumbar-agudo-litiasis-renal.svg",
    alt: "Flujograma: Dolor lumbar agudo con hematuria"
  },
  "PED-074": {
    titulo: "Crecimiento del lactante",
    imagen: "flujogramas/ganancia-peso-insuficiente-visita-domiciliaria.svg",
    alt: "Flujograma: Crecimiento del lactante"
  },
  "CB-023": {
    titulo: "Intoxicación por monóxido de carbono",
    imagen: "flujogramas/monoxido-carbono-estufa-oxigeno.svg",
    alt: "Flujograma: Intoxicación por monóxido de carbono"
  },
  "REU-020": {
    titulo: "Acné: formas de gravedad",
    imagen: "flujogramas/acne-fulminante-fiebre-artralgias.svg",
    alt: "Flujograma: Acné: formas de gravedad"
  },
  "GAS-021": {
    titulo: "Pancreatitis aguda: primeras 72 horas",
    imagen: "flujogramas/pancreatitis-hipertrigliceridemia-hidratacion.svg",
    alt: "Flujograma: Pancreatitis aguda: primeras 72 horas"
  },
  "PED-075": {
    titulo: "Vómitos en el lactante pequeño",
    imagen: "flujogramas/vomitos-lactante-hipertrofia-piloro.svg",
    alt: "Flujograma: Vómitos en el lactante pequeño"
  },
  "PED-076": {
    titulo: "Neumonía en el niño: tipos",
    imagen: "flujogramas/neumonia-nino-tipos-comunidad.svg",
    alt: "Flujograma: Neumonía en el niño: tipos"
  },
  "CIR-040": {
    titulo: "Herida precordial con shock",
    imagen: "flujogramas/herida-precordial-taponamiento-pericardiocentesis.svg",
    alt: "Flujograma: Herida precordial con shock"
  },
  "SP-048": {
    titulo: "Voluntades anticipadas",
    imagen: "flujogramas/voluntad-anticipada-autonomia-ventilacion.svg",
    alt: "Flujograma: Voluntades anticipadas"
  },
  "TRA-012": {
    titulo: "Fracturas del brazo y nervio afectado",
    imagen: "flujogramas/fractura-humero-nervios-mano-pendula.svg",
    alt: "Flujograma: Fracturas del brazo y nervio afectado"
  },
  "PSI-014": {
    titulo: "Crisis de pánico",
    imagen: "flujogramas/crisis-panico-curso-sintomas.svg",
    alt: "Flujograma: Crisis de pánico"
  },
  "GAS-022": {
    titulo: "Esteatorrea en el alcohólico",
    imagen: "flujogramas/esteatorrea-pancreatitis-cronica-insuficiencia.svg",
    alt: "Flujograma: Esteatorrea en el alcohólico"
  },
  "END-017": {
    titulo: "Hipertensión secundaria: causas endocrinas",
    imagen: "flujogramas/hipertension-paroxistica-feocromocitoma.svg",
    alt: "Flujograma: Hipertensión secundaria: causas endocrinas"
  },
  "PED-077": {
    titulo: "Convulsión febril: simple o compleja",
    imagen: "flujogramas/convulsion-febril-compleja-criterios.svg",
    alt: "Flujograma: Convulsión febril: simple o compleja"
  },
  "GIN-063": {
    titulo: "Rotura prematura de membranas: manejo según semanas",
    imagen: "flujogramas/rotura-membranas-pretermino-manejo.svg",
    alt: "Flujograma: Rotura prematura de membranas: manejo según semanas"
  },
  "NEU-020": {
    titulo: "Mecanismos de hipoxemia",
    imagen: "flujogramas/mecanismos-hipoxemia-epoc-vq.svg",
    alt: "Flujograma: Mecanismos de hipoxemia"
  },
  "PED-078": {
    titulo: "Lactante que suda y se cansa al lactar",
    imagen: "flujogramas/lactante-sudoracion-lactancia-insuficiencia-cardiaca.svg",
    alt: "Flujograma: Lactante que suda y se cansa al lactar"
  },
  "CIR-041": {
    titulo: "Quemado con compromiso de la vía aérea",
    imagen: "flujogramas/quemadura-facial-estridor-intubacion.svg",
    alt: "Flujograma: Quemado con compromiso de la vía aérea"
  },
  "CAR-028": {
    titulo: "Arritmias: con pulso o sin pulso",
    imagen: "flujogramas/arritmias-pulso-desfibrilacion-cardioversion.svg",
    alt: "Flujograma: Arritmias: con pulso o sin pulso"
  },
  "GAS-023": {
    titulo: "Megacolon tóxico",
    imagen: "flujogramas/megacolon-toxico-criterios-jalan.svg",
    alt: "Flujograma: Megacolon tóxico"
  },
  "GIN-064": {
    titulo: "Diabetes gestacional: cuándo tamizar",
    imagen: "flujogramas/diabetes-gestacional-tamizaje-24-28.svg",
    alt: "Flujograma: Diabetes gestacional: cuándo tamizar"
  },
  "GIN-065": {
    titulo: "Prevención de la endometritis puerperal",
    imagen: "flujogramas/prevencion-endometritis-tactos-vaginales.svg",
    alt: "Flujograma: Prevención de la endometritis puerperal"
  },
  "REU-021": {
    titulo: "Dermatitis atópica: tratamiento escalonado",
    imagen: "flujogramas/dermatitis-atopica-escalera-emolientes.svg",
    alt: "Flujograma: Dermatitis atópica: tratamiento escalonado"
  },
  "INF-028": {
    titulo: "SARS-CoV-2: ciclo de replicación",
    imagen: "flujogramas/sars-cov-2-ciclo-ace2.svg",
    alt: "Flujograma: SARS-CoV-2: ciclo de replicación"
  },
  "CIR-042": {
    titulo: "Taponamiento traumático: qué hacer",
    imagen: "flujogramas/taponamiento-traumatico-toracotomia.svg",
    alt: "Flujograma: Taponamiento traumático: qué hacer"
  },
  "CIR-043": {
    titulo: "Coledocolitiasis: conducta según probabilidad",
    imagen: "flujogramas/coledocolitiasis-cpre-papilotomia.svg",
    alt: "Flujograma: Coledocolitiasis: conducta según probabilidad"
  },
  "GIN-066": {
    titulo: "Prurito vulvar en la posmenopausia",
    imagen: "flujogramas/prurito-vulvar-posmenopausia-atrofia.svg",
    alt: "Flujograma: Prurito vulvar en la posmenopausia"
  },
  "HEM-014": {
    titulo: "Niña con palidez, dolor óseo y visceromegalia",
    imagen: "flujogramas/nina-citopenias-hepatoesplenomegalia-lla.svg",
    alt: "Flujograma: Niña con palidez, dolor óseo y visceromegalia"
  },
  "CIR-044": {
    titulo: "Infecciones de partes blandas: gravedad",
    imagen: "flujogramas/infeccion-partes-blandas-fascitis-necrotizante.svg",
    alt: "Flujograma: Infecciones de partes blandas: gravedad"
  },
  "GIN-067": {
    titulo: "Tipos de shock en obstetricia",
    imagen: "flujogramas/shock-obstetrico-tipos-hipovolemico.svg",
    alt: "Flujograma: Tipos de shock en obstetricia"
  },
  "PED-079": {
    titulo: "Tos ferina",
    imagen: "flujogramas/tos-ferina-fases-azitromicina.svg",
    alt: "Flujograma: Tos ferina"
  },
  "CIR-045": {
    titulo: "Obstrucción de colon en la altura",
    imagen: "flujogramas/obstruccion-colon-altura-volvulo-sigmoides.svg",
    alt: "Flujograma: Obstrucción de colon en la altura"
  },
  "NEU-021": {
    titulo: "Disnea crónica con acropaquias",
    imagen: "flujogramas/disnea-cronica-crepitantes-epid.svg",
    alt: "Flujograma: Disnea crónica con acropaquias"
  },
  "CAR-029": {
    titulo: "Cuidados posparo: metas ventilatorias",
    imagen: "flujogramas/cuidados-posparo-paco2-ventilacion.svg",
    alt: "Flujograma: Cuidados posparo: metas ventilatorias"
  },
  "CIR-046": {
    titulo: "Fiebre posoperatoria según el día",
    imagen: "flujogramas/fiebre-postoperatoria-atelectasia.svg",
    alt: "Flujograma: Fiebre posoperatoria según el día"
  },
  "INF-029": {
    titulo: "Fiebre prolongada en zona tropical",
    imagen: "flujogramas/fiebre-escalofrios-esplenomegalia-malaria.svg",
    alt: "Flujograma: Fiebre prolongada en zona tropical"
  },
  "CIR-047": {
    titulo: "Tipos de cierre de heridas",
    imagen: "flujogramas/cicatrizacion-cierre-tercera-intencion.svg",
    alt: "Flujograma: Tipos de cierre de heridas"
  },
  "SP-049": {
    titulo: "Medidas de asociación y diseños",
    imagen: "flujogramas/medidas-asociacion-odds-ratio-casos-controles.svg",
    alt: "Flujograma: Medidas de asociación y diseños"
  },
  "NRL-019": {
    titulo: "Corea de Sydenham: criterios de Jones",
    imagen: "flujogramas/corea-sydenham-criterios-jones.svg",
    alt: "Flujograma: Corea de Sydenham: criterios de Jones"
  },
  "HEM-015": {
    titulo: "Células de la mucosa gástrica",
    imagen: "flujogramas/celulas-gastricas-anemia-perniciosa.svg",
    alt: "Flujograma: Células de la mucosa gástrica"
  },
  "GIN-068": {
    titulo: "Tamizaje de diabetes gestacional en dos pasos",
    imagen: "flujogramas/test-osullivan-positivo-ptog.svg",
    alt: "Flujograma: Tamizaje de diabetes gestacional en dos pasos"
  },
  "PED-080": {
    titulo: "Fenilcetonuria en el tamizaje neonatal",
    imagen: "flujogramas/tamizaje-neonatal-fenilcetonuria-dieta.svg",
    alt: "Flujograma: Fenilcetonuria en el tamizaje neonatal"
  },
  "OFT-016": {
    titulo: "Epistaxis anterior: manejo escalonado",
    imagen: "flujogramas/epistaxis-anterior-hipertenso-compresion.svg",
    alt: "Flujograma: Epistaxis anterior: manejo escalonado"
  },
  "NRL-020": {
    titulo: "Déficit neurológico que se recupera",
    imagen: "flujogramas/deficit-focal-transitorio-anciano-ait.svg",
    alt: "Flujograma: Déficit neurológico que se recupera"
  },
  "HEM-016": {
    titulo: "Leucocitosis con esplenomegalia",
    imagen: "flujogramas/leucocitosis-esplenomegalia-leucemia-mieloide-cronica.svg",
    alt: "Flujograma: Leucocitosis con esplenomegalia"
  },
  "INF-030": {
    titulo: "Vectores de enfermedades en el Perú",
    imagen: "flujogramas/vectores-peru-chagas-triatoma.svg",
    alt: "Flujograma: Vectores de enfermedades en el Perú"
  },
  "GIN-069": {
    titulo: "Tipos de aborto",
    imagen: "flujogramas/aborto-terapeutico-lupus-nefropatia.svg",
    alt: "Flujograma: Tipos de aborto"
  },
  "INF-031": {
    titulo: "Malaria: especies de Plasmodium",
    imagen: "flujogramas/plasmodium-especies-falciparum-grave.svg",
    alt: "Flujograma: Malaria: especies de Plasmodium"
  },
  "PED-081": {
    titulo: "Niño nefrótico con fiebre y dolor abdominal",
    imagen: "flujogramas/nefrotico-nino-dolor-abdominal-peritonitis-primaria.svg",
    alt: "Flujograma: Niño nefrótico con fiebre y dolor abdominal"
  },
  "GIN-070": {
    titulo: "Sangrado indoloro en el tercer trimestre",
    imagen: "flujogramas/sangrado-indoloro-tercer-trimestre-placenta-previa.svg",
    alt: "Flujograma: Sangrado indoloro en el tercer trimestre"
  },
  "GIN-071": {
    titulo: "Síndromes de cáncer hereditario",
    imagen: "flujogramas/cancer-hereditario-brca1-mama.svg",
    alt: "Flujograma: Síndromes de cáncer hereditario"
  },
  "PED-082": {
    titulo: "Anemia en el lactante: el frotis",
    imagen: "flujogramas/lactante-prematuro-anemia-ferropenica.svg",
    alt: "Flujograma: Anemia en el lactante: el frotis"
  },
  "CIR-048": {
    titulo: "Tumoración sacrococcígea supurada",
    imagen: "flujogramas/masa-sacra-supurada-quiste-pilonidal.svg",
    alt: "Flujograma: Tumoración sacrococcígea supurada"
  },
  "CB-024": {
    titulo: "Síndrome colinérgico",
    imagen: "flujogramas/sindrome-colinergico-carbamatos.svg",
    alt: "Flujograma: Síndrome colinérgico"
  },
  "END-018": {
    titulo: "Hipertrigliceridemia: niveles y riesgo",
    imagen: "flujogramas/hipertrigliceridemia-xantomas-eruptivos-pancreatitis.svg",
    alt: "Flujograma: Hipertrigliceridemia: niveles y riesgo"
  },
  "GAS-024": {
    titulo: "Ictericia obstructiva indolora",
    imagen: "flujogramas/ictericia-obstructiva-colangiocarcinoma.svg",
    alt: "Flujograma: Ictericia obstructiva indolora"
  },
  "PED-083": {
    titulo: "Bronquiolitis: gravedad y manejo",
    imagen: "flujogramas/bronquiolitis-gravedad-manejo.svg",
    alt: "Flujograma: Bronquiolitis: gravedad y manejo"
  },
  "PED-084": {
    titulo: "Distrés en el RN a término con meconio",
    imagen: "flujogramas/rn-termino-liquido-meconial-aspiracion.svg",
    alt: "Flujograma: Distrés en el RN a término con meconio"
  },
  "GAS-025": {
    titulo: "Hematemesis: causas",
    imagen: "flujogramas/hematemesis-vomitos-alcohol-mallory-weiss.svg",
    alt: "Flujograma: Hematemesis: causas"
  },
  "PED-085": {
    titulo: "Intoxicación por plaguicida en un niño",
    imagen: "flujogramas/nino-campo-fumigado-descontaminacion.svg",
    alt: "Flujograma: Intoxicación por plaguicida en un niño"
  },
  "GIN-072": {
    titulo: "Tamizaje de cáncer de cuello uterino",
    imagen: "flujogramas/papanicolaou-histerectomia-total-benigna.svg",
    alt: "Flujograma: Tamizaje de cáncer de cuello uterino"
  },
  "CIR-049": {
    titulo: "Masa femoral dolorosa e irreductible",
    imagen: "flujogramas/masa-femoral-irreductible-hernia-crural-estrangulada.svg",
    alt: "Flujograma: Masa femoral dolorosa e irreductible"
  },
  "NEU-022": {
    titulo: "Disnea súbita en el posoperatorio",
    imagen: "flujogramas/disnea-subita-postoperatorio-cadera-tep.svg",
    alt: "Flujograma: Disnea súbita en el posoperatorio"
  },
  "END-019": {
    titulo: "Nefropatía diabética: detección precoz",
    imagen: "flujogramas/nefropatia-diabetica-albuminuria-cociente.svg",
    alt: "Flujograma: Nefropatía diabética: detección precoz"
  },
  "PED-086": {
    titulo: "Niño contacto de tuberculosis",
    imagen: "flujogramas/contacto-tuberculosis-nino-terapia-preventiva.svg",
    alt: "Flujograma: Niño contacto de tuberculosis"
  },
  "SP-050": {
    titulo: "Faltas a la integridad en investigación",
    imagen: "flujogramas/integridad-investigacion-conflicto-intereses.svg",
    alt: "Flujograma: Faltas a la integridad en investigación"
  },
  "INF-032": {
    titulo: "LCR turbio con neutrófilos",
    imagen: "flujogramas/lcr-turbio-neutrofilos-meningitis-bacteriana.svg",
    alt: "Flujograma: LCR turbio con neutrófilos"
  },
  "SP-051": {
    titulo: "Factores de riesgo de la diabetes tipo 2",
    imagen: "flujogramas/promocion-salud-diabetes-sedentarismo.svg",
    alt: "Flujograma: Factores de riesgo de la diabetes tipo 2"
  },
  "INF-033": {
    titulo: "Lesiones cerebrales en el paciente con VIH",
    imagen: "flujogramas/vih-lesiones-cerebrales-toxoplasmosis.svg",
    alt: "Flujograma: Lesiones cerebrales en el paciente con VIH"
  },
  "GIN-073": {
    titulo: "Enfermedad inflamatoria pélvica: dónde tratar",
    imagen: "flujogramas/epi-falla-ambulatoria-hospitalizar.svg",
    alt: "Flujograma: Enfermedad inflamatoria pélvica: dónde tratar"
  },
  "PED-087": {
    titulo: "Lactante con polipnea y mala ganancia de peso",
    imagen: "flujogramas/lactante-sudoracion-hepatomegalia-icc.svg",
    alt: "Flujograma: Lactante con polipnea y mala ganancia de peso"
  },
  "INF-034": {
    titulo: "Diarrea parasitaria en el niño",
    imagen: "flujogramas/diarrea-grasosa-agua-cruda-giardia.svg",
    alt: "Flujograma: Diarrea parasitaria en el niño"
  },
  "PED-088": {
    titulo: "Neonato con tos y cianosis al lactar",
    imagen: "flujogramas/neonato-sonda-no-pasa-atresia-esofagica.svg",
    alt: "Flujograma: Neonato con tos y cianosis al lactar"
  },
  "INF-035": {
    titulo: "Recién nacido expuesto al VIH",
    imagen: "flujogramas/recien-nacido-expuesto-vih-zidovudina.svg",
    alt: "Flujograma: Recién nacido expuesto al VIH"
  },
  "CIR-050": {
    titulo: "Hemotórax: criterios de toracotomía",
    imagen: "flujogramas/hemotorax-drenaje-200-hora-toracotomia.svg",
    alt: "Flujograma: Hemotórax: criterios de toracotomía"
  },
  "CAR-030": {
    titulo: "Endocarditis infecciosa: signos",
    imagen: "flujogramas/fiebre-soplo-nuevo-roth-endocarditis.svg",
    alt: "Flujograma: Endocarditis infecciosa: signos"
  },
  "PED-089": {
    titulo: "Anemia ferropénica: qué debe comer",
    imagen: "flujogramas/anemia-ferropenica-nino-alimentos-hierro-hemo.svg",
    alt: "Flujograma: Anemia ferropénica: qué debe comer"
  },
  "OFT-017": {
    titulo: "Odinofagia con trismus",
    imagen: "flujogramas/odinofagia-trismus-absceso-periamigdalino-drenaje.svg",
    alt: "Flujograma: Odinofagia con trismus"
  },
  "GAS-026": {
    titulo: "HDA en el cirrótico: reanimación",
    imagen: "flujogramas/hematemesis-cirrotico-choque-cristaloides.svg",
    alt: "Flujograma: HDA en el cirrótico: reanimación"
  },
  "TRA-013": {
    titulo: "Cadera deformada tras un choque",
    imagen: "flujogramas/impacto-frontal-aduccion-rotacion-interna-luxacion-posterior-cadera.svg",
    alt: "Flujograma: Cadera deformada tras un choque"
  },
  "NEF-031": {
    titulo: "Lesión renal aguda: prerrenal o NTA",
    imagen: "flujogramas/oligoanuria-choque-hemorragico-necrosis-tubular-aguda.svg",
    alt: "Flujograma: Lesión renal aguda: prerrenal o NTA"
  },
  "INF-036": {
    titulo: "Úlcera genital: qué agente",
    imagen: "flujogramas/ulcera-genital-indolora-indurada-sifilis-primaria.svg",
    alt: "Flujograma: Úlcera genital: qué agente"
  },
  "GAS-027": {
    titulo: "Fiebre, ictericia y dolor biliar",
    imagen: "flujogramas/fiebre-ictericia-dolor-colangitis-charcot.svg",
    alt: "Flujograma: Fiebre, ictericia y dolor biliar"
  },
  "SP-052": {
    titulo: "Propiedades del agente infeccioso",
    imagen: "flujogramas/omicron-contagios-transmisibilidad-agente.svg",
    alt: "Flujograma: Propiedades del agente infeccioso"
  },
  "GAS-028": {
    titulo: "Pólipo de colon en la colonoscopia",
    imagen: "flujogramas/sangrado-rectal-polipo-pediculado-polipectomia.svg",
    alt: "Flujograma: Pólipo de colon en la colonoscopia"
  },
  "CAR-031": {
    titulo: "Hipertensión: consultorio frente a MAPA",
    imagen: "flujogramas/hipertension-bata-blanca-mapa.svg",
    alt: "Flujograma: Hipertensión: consultorio frente a MAPA"
  },
  "CAR-032": {
    titulo: "Edema facial y en esclavina",
    imagen: "flujogramas/edema-esclavina-sindrome-vena-cava-superior.svg",
    alt: "Flujograma: Edema facial y en esclavina"
  },
  "GIN-074": {
    titulo: "Masa anexial: qué es",
    imagen: "flujogramas/dolor-pelvico-masa-anexial-endometrioma.svg",
    alt: "Flujograma: Masa anexial: qué es"
  },
  "END-020": {
    titulo: "Amenorrea primaria con talla baja",
    imagen: "flujogramas/amenorrea-primaria-talla-baja-turner-cariotipo.svg",
    alt: "Flujograma: Amenorrea primaria con talla baja"
  },
  "PED-090": {
    titulo: "Intoxicación por paracetamol",
    imagen: "flujogramas/sobredosis-paracetamol-nino-acetilcisteina.svg",
    alt: "Flujograma: Intoxicación por paracetamol"
  },
  "GIN-075": {
    titulo: "Urocultivo con Lactobacillus en la gestante",
    imagen: "flujogramas/gestante-urocultivo-lactobacillus-repetir.svg",
    alt: "Flujograma: Urocultivo con Lactobacillus en la gestante"
  },
  "REU-022": {
    titulo: "Urticaria tras el ejercicio",
    imagen: "flujogramas/ronchas-ejercicio-ducha-caliente-urticaria-colinergica.svg",
    alt: "Flujograma: Urticaria tras el ejercicio"
  },
  "NRL-021": {
    titulo: "TEC: gravedad según Glasgow",
    imagen: "flujogramas/trauma-craneal-glasgow-12-tomografia.svg",
    alt: "Flujograma: TEC: gravedad según Glasgow"
  },
  "NEF-032": {
    titulo: "Hipermagnesemia por laxantes",
    imagen: "flujogramas/adulta-mayor-laxantes-salinos-hipermagnesemia.svg",
    alt: "Flujograma: Hipermagnesemia por laxantes"
  },
  "GIN-076": {
    titulo: "Imagen en la gestante con dolor en FID",
    imagen: "flujogramas/gestante-dolor-fid-apendicitis-ecografia.svg",
    alt: "Flujograma: Imagen en la gestante con dolor en FID"
  },
  "SP-053": {
    titulo: "Derechos de los usuarios de salud",
    imagen: "flujogramas/examen-unico-nacional-derecho-calidad-atencion.svg",
    alt: "Flujograma: Derechos de los usuarios de salud"
  },
  "CB-025": {
    titulo: "Genes de las dislipidemias",
    imagen: "flujogramas/hipercolesterolemia-familiar-xantomas-receptor-ldl.svg",
    alt: "Flujograma: Genes de las dislipidemias"
  },
  "PED-091": {
    titulo: "Estenosis pilórica: el trastorno ácido-base",
    imagen: "flujogramas/vomitos-proyectil-lactante-alcalosis-hipocloremica.svg",
    alt: "Flujograma: Estenosis pilórica: el trastorno ácido-base"
  },
  "CIR-051": {
    titulo: "Obstrucción intestinal: delgado o colon",
    imagen: "flujogramas/laparotomia-previa-obstruccion-intestinal-bridas.svg",
    alt: "Flujograma: Obstrucción intestinal: delgado o colon"
  },
  "CAR-033": {
    titulo: "Derrame pericárdico: cuándo drenar",
    imagen: "flujogramas/lupus-pulso-paradojico-taponamiento-pericardiocentesis.svg",
    alt: "Flujograma: Derrame pericárdico: cuándo drenar"
  },
  "REU-023": {
    titulo: "Manchas hipocrómicas en el tronco",
    imagen: "flujogramas/manchas-hipocromicas-tronco-pitiriasis-versicolor.svg",
    alt: "Flujograma: Manchas hipocrómicas en el tronco"
  },
  "SP-054": {
    titulo: "Principios de la bioética",
    imagen: "flujogramas/farmacos-sin-evidencia-pandemia-no-maleficencia.svg",
    alt: "Flujograma: Principios de la bioética"
  },
  "CAR-034": {
    titulo: "Trauma torácico cerrado con arritmia",
    imagen: "flujogramas/trauma-precordial-arritmia-contusion-miocardica-ecg.svg",
    alt: "Flujograma: Trauma torácico cerrado con arritmia"
  },
  "TRA-014": {
    titulo: "Manguito de los rotadores",
    imagen: "flujogramas/hombro-abduccion-dolorosa-supraespinoso.svg",
    alt: "Flujograma: Manguito de los rotadores"
  },
  "GIN-077": {
    titulo: "Presentación de cara",
    imagen: "flujogramas/presentacion-cara-mentoposterior-cesarea.svg",
    alt: "Flujograma: Presentación de cara"
  },
  "GIN-078": {
    titulo: "Datación del embarazo",
    imagen: "flujogramas/primer-control-edad-gestacional-ecografia-lcn.svg",
    alt: "Flujograma: Datación del embarazo"
  },
  "GAS-029": {
    titulo: "Hepatitis viral aguda: fases",
    imagen: "flujogramas/prodromo-ictericia-hepatitis-viral-aguda.svg",
    alt: "Flujograma: Hepatitis viral aguda: fases"
  },
  "GIN-079": {
    titulo: "Preeclampsia: criterios de severidad",
    imagen: "flujogramas/preeclampsia-severa-36-semanas-sulfato-magnesio.svg",
    alt: "Flujograma: Preeclampsia: criterios de severidad"
  },
  "INF-037": {
    titulo: "Clasificación del dengue",
    imagen: "flujogramas/fiebre-dolor-abdominal-vomitos-dengue-signos-alarma.svg",
    alt: "Flujograma: Clasificación del dengue"
  },
  "NEU-023": {
    titulo: "Crisis asmática: gravedad",
    imagen: "flujogramas/crisis-asmatica-torax-silente-gravedad.svg",
    alt: "Flujograma: Crisis asmática: gravedad"
  },
  "GAS-030": {
    titulo: "Úlcera péptica: por qué se produce",
    imagen: "flujogramas/ulcera-gastrica-agresion-defensa-mucosa.svg",
    alt: "Flujograma: Úlcera péptica: por qué se produce"
  },
  "CIR-052": {
    titulo: "Apendicitis: escala de Alvarado",
    imagen: "flujogramas/dolor-periumbilical-migratorio-alvarado-nino.svg",
    alt: "Flujograma: Apendicitis: escala de Alvarado"
  },
  "INF-038": {
    titulo: "Helmintos intestinales: tratamiento",
    imagen: "flujogramas/strongyloides-heces-ivermectina.svg",
    alt: "Flujograma: Helmintos intestinales: tratamiento"
  },
  "NEU-024": {
    titulo: "Disnea súbita en el EPOC",
    imagen: "flujogramas/epoc-disnea-subita-hiperresonancia-neumotorax.svg",
    alt: "Flujograma: Disnea súbita en el EPOC"
  },
  "SP-055": {
    titulo: "Víctima de violencia: a dónde referir",
    imagen: "flujogramas/tamizaje-violencia-familiar-csmc.svg",
    alt: "Flujograma: Víctima de violencia: a dónde referir"
  },
  "GAS-031": {
    titulo: "Pancreatitis: amilasa o lipasa",
    imagen: "flujogramas/dolor-epigastrico-7-dias-lipasa.svg",
    alt: "Flujograma: Pancreatitis: amilasa o lipasa"
  },
  "CIR-053": {
    titulo: "Hernias de la pared abdominal",
    imagen: "flujogramas/tumoracion-inguinoescrotal-hernia-indirecta.svg",
    alt: "Flujograma: Hernias de la pared abdominal"
  },
  "INF-039": {
    titulo: "Dengue: fases de la enfermedad",
    imagen: "flujogramas/fiebre-iquitos-prueba-lazo-dengue.svg",
    alt: "Flujograma: Dengue: fases de la enfermedad"
  },
  "OFT-018": {
    titulo: "Rinosinusitis: según duración",
    imagen: "flujogramas/cefalea-tos-nocturna-rinosinusitis-subaguda.svg",
    alt: "Flujograma: Rinosinusitis: según duración"
  },
  "REU-024": {
    titulo: "Lesiones vesiculares",
    imagen: "flujogramas/vesiculas-dermatoma-vih-herpes-zoster.svg",
    alt: "Flujograma: Lesiones vesiculares"
  },
  "GIN-080": {
    titulo: "Fiebre en el puerperio",
    imagen: "flujogramas/fiebre-poscesarea-utero-doloroso-endometritis.svg",
    alt: "Flujograma: Fiebre en el puerperio"
  },
  "SP-056": {
    titulo: "Planificación: por dónde empezar",
    imagen: "flujogramas/serumista-plan-operativo-anual-problemas.svg",
    alt: "Flujograma: Planificación: por dónde empezar"
  },
  "PSI-015": {
    titulo: "Conductas purgativas y medio interno",
    imagen: "flujogramas/vomitos-autoprovocados-adolescente-alcalosis.svg",
    alt: "Flujograma: Conductas purgativas y medio interno"
  },
  "PED-092": {
    titulo: "Cianosis neonatal que no mejora con O₂",
    imagen: "flujogramas/cianosis-neonatal-no-mejora-oxigeno.svg",
    alt: "Flujograma: Cianosis neonatal que no mejora con O₂"
  },
  "PSI-016": {
    titulo: "Psicosis con delirios",
    imagen: "flujogramas/delirios-grandeza-persecucion-esquizofrenia.svg",
    alt: "Flujograma: Psicosis con delirios"
  },
  "OFT-019": {
    titulo: "Alteraciones pupilares",
    imagen: "flujogramas/midriasis-bilateral-tras-fondo-de-ojo.svg",
    alt: "Flujograma: Alteraciones pupilares"
  },
  "GAS-032": {
    titulo: "Dolor epigástrico urente",
    imagen: "flujogramas/dolor-epigastrico-nocturno-ulcera-duodenal.svg",
    alt: "Flujograma: Dolor epigástrico urente"
  },
  "PED-093": {
    titulo: "Dificultad respiratoria neonatal",
    imagen: "flujogramas/rpm-prolongada-hipotermia-neumonia-neonatal.svg",
    alt: "Flujograma: Dificultad respiratoria neonatal"
  },
  "NEU-025": {
    titulo: "Contacto de tuberculosis",
    imagen: "flujogramas/gestante-contacto-tb-ppd-positivo-isoniacida.svg",
    alt: "Flujograma: Contacto de tuberculosis"
  },
  "END-021": {
    titulo: "Perfil tiroideo en el enfermo grave",
    imagen: "flujogramas/colitis-grave-t3-baja-eutiroideo-enfermo.svg",
    alt: "Flujograma: Perfil tiroideo en el enfermo grave"
  },
  "GIN-081": {
    titulo: "Sangrado del primer trimestre",
    imagen: "flujogramas/amenorrea-9-semanas-sangrado-escaso-ecografia.svg",
    alt: "Flujograma: Sangrado del primer trimestre"
  },
  "NRL-022": {
    titulo: "Hipertensión endocraneana: escalones",
    imagen: "flujogramas/tec-edema-papila-glasgow-descenso-salino-hipertonico.svg",
    alt: "Flujograma: Hipertensión endocraneana: escalones"
  },
  "GIN-082": {
    titulo: "Dolor en FID en mujer fértil",
    imagen: "flujogramas/dolor-fid-masa-anexial-hipotension-bhcg.svg",
    alt: "Flujograma: Dolor en FID en mujer fértil"
  },
  "CB-026": {
    titulo: "Toxíndromes",
    imagen: "flujogramas/bebidas-energizantes-agitacion-toxindrome-simpatico.svg",
    alt: "Flujograma: Toxíndromes"
  },
  "OFT-020": {
    titulo: "Cuerpo extraño en el oído",
    imagen: "flujogramas/semilla-conducto-auditivo-extraccion.svg",
    alt: "Flujograma: Cuerpo extraño en el oído"
  },
  "CAR-035": {
    titulo: "Endocarditis: criterios de Duke",
    imagen: "flujogramas/dialisis-cateter-fiebre-janeway-endocarditis.svg",
    alt: "Flujograma: Endocarditis: criterios de Duke"
  },
  "INF-040": {
    titulo: "Contacto de meningococo",
    imagen: "flujogramas/meningococcemia-contacto-personal-salud-rifampicina.svg",
    alt: "Flujograma: Contacto de meningococo"
  },
  "CB-027": {
    titulo: "Monóxido de carbono y oxigenación",
    imagen: "flujogramas/incendio-sotano-monoxido-po2-alta-hipoxia-tisular.svg",
    alt: "Flujograma: Monóxido de carbono y oxigenación"
  },
  "TRA-015": {
    titulo: "Ligamentos del tobillo",
    imagen: "flujogramas/futbolista-esguince-inversion-calcaneoperoneo.svg",
    alt: "Flujograma: Ligamentos del tobillo"
  },
  "GIN-083": {
    titulo: "Sangrado del tercer trimestre en el primer nivel",
    imagen: "flujogramas/sangrado-tercer-trimestre-establecimiento-i2-referencia.svg",
    alt: "Flujograma: Sangrado del tercer trimestre en el primer nivel"
  },
  "PED-094": {
    titulo: "Tos ferina: fases",
    imagen: "flujogramas/tos-paroxistica-vomito-cianosis-tos-ferina.svg",
    alt: "Flujograma: Tos ferina: fases"
  },
  "NEF-033": {
    titulo: "Urocultivo: cuándo es significativo",
    imagen: "flujogramas/urocultivo-umbral-100000-ufc.svg",
    alt: "Flujograma: Urocultivo: cuándo es significativo"
  },
  "NEF-034": {
    titulo: "Tipos de cálculo urinario",
    imagen: "flujogramas/calculo-radiopaco-calcio-normal-oxalato.svg",
    alt: "Flujograma: Tipos de cálculo urinario"
  },
  "NEU-026": {
    titulo: "Neumonía según el lugar de adquisición",
    imagen: "flujogramas/acv-hospitalizado-dia-8-neumonia-gramnegativos.svg",
    alt: "Flujograma: Neumonía según el lugar de adquisición"
  },
  "GIN-084": {
    titulo: "Amenorrea secundaria",
    imagen: "flujogramas/amenorrea-secundaria-test-progesterona-anovulacion.svg",
    alt: "Flujograma: Amenorrea secundaria"
  },
  "PED-095": {
    titulo: "Pulsos femorales débiles en el neonato",
    imagen: "flujogramas/neonato-pulsos-femorales-debiles-coartacion.svg",
    alt: "Flujograma: Pulsos femorales débiles en el neonato"
  },
  "PED-096": {
    titulo: "Policitemia neonatal",
    imagen: "flujogramas/neonato-pletorico-hto-70-exanguinotransfusion.svg",
    alt: "Flujograma: Policitemia neonatal"
  },
  "END-022": {
    titulo: "Tratamiento del hipertiroidismo",
    imagen: "flujogramas/hipertiroidismo-mujer-joven-metimazol.svg",
    alt: "Flujograma: Tratamiento del hipertiroidismo"
  },
  "REU-025": {
    titulo: "Hidradenitis supurativa: estadios de Hurley",
    imagen: "flujogramas/abscesos-axilares-trayectos-hidradenitis.svg",
    alt: "Flujograma: Hidradenitis supurativa: estadios de Hurley"
  },
  "PED-097": {
    titulo: "Reanimación neonatal: el minuto de oro",
    imagen: "flujogramas/prematuro-flacido-apnea-pasos-iniciales.svg",
    alt: "Flujograma: Reanimación neonatal: el minuto de oro"
  },
  "GIN-085": {
    titulo: "Vigilancia del sulfato de magnesio",
    imagen: "flujogramas/sulfato-magnesio-oliguria-bradipnea-suspender.svg",
    alt: "Flujograma: Vigilancia del sulfato de magnesio"
  },
  "INF-041": {
    titulo: "Prurito vulvar en la niña",
    imagen: "flujogramas/nina-prurito-vulvar-perianal-nocturno-oxiuros.svg",
    alt: "Flujograma: Prurito vulvar en la niña"
  },
  "GIN-086": {
    titulo: "Alumbramiento y retención placentaria",
    imagen: "flujogramas/parto-domiciliario-placenta-retenida-sangrado.svg",
    alt: "Flujograma: Alumbramiento y retención placentaria"
  },
  "GAS-033": {
    titulo: "Pancreatitis aguda: gravedad",
    imagen: "flujogramas/pancreatitis-grave-choque-fluidoterapia.svg",
    alt: "Flujograma: Pancreatitis aguda: gravedad"
  },
  "NEF-035": {
    titulo: "Glomerulonefritis con hematuria",
    imagen: "flujogramas/infeccion-respiratoria-previa-hematuria-gn-postinfecciosa.svg",
    alt: "Flujograma: Glomerulonefritis con hematuria"
  },
  "SP-057": {
    titulo: "Ciclo de la violencia",
    imagen: "flujogramas/ciclo-violencia-pareja-acumulacion-tension.svg",
    alt: "Flujograma: Ciclo de la violencia"
  },
  "CB-028": {
    titulo: "Intoxicación por metanol",
    imagen: "flujogramas/licor-adulterado-convulsiones-acidosis-metanol.svg",
    alt: "Flujograma: Intoxicación por metanol"
  },
  "SP-058": {
    titulo: "Estrategias de salud pública",
    imagen: "flujogramas/diresa-espacios-concertacion-participacion-ciudadana.svg",
    alt: "Flujograma: Estrategias de salud pública"
  },
  "INF-042": {
    titulo: "Úlcera con nódulos en cadena",
    imagen: "flujogramas/jardinero-espina-rosa-nodulos-linfaticos-esporotricosis.svg",
    alt: "Flujograma: Úlcera con nódulos en cadena"
  },
  "GIN-087": {
    titulo: "Anticoncepción en puérpera con VIH",
    imagen: "flujogramas/puerpera-vih-tar-anticoncepcion-diu.svg",
    alt: "Flujograma: Anticoncepción en puérpera con VIH"
  },
  "PED-098": {
    titulo: "Desnutrición grave en el lactante",
    imagen: "flujogramas/lactante-emaciado-piel-flacida-marasmo.svg",
    alt: "Flujograma: Desnutrición grave en el lactante"
  },
  "PED-099": {
    titulo: "Diarrea: evaluar la deshidratación",
    imagen: "flujogramas/diarrea-con-moco-sin-deshidratacion-plan-a.svg",
    alt: "Flujograma: Diarrea: evaluar la deshidratación"
  },
  "HEM-017": {
    titulo: "TTPa prolongado: prueba de mezcla",
    imagen: "flujogramas/ttpa-prolongado-prueba-mezcla-no-corrige.svg",
    alt: "Flujograma: TTPa prolongado: prueba de mezcla"
  },
  "HEM-018": {
    titulo: "Estrógenos y trombosis",
    imagen: "flujogramas/anticonceptivos-combinados-tvp-factores-coagulacion.svg",
    alt: "Flujograma: Estrógenos y trombosis"
  },
  "NEF-036": {
    titulo: "Fiebre con síntomas urinarios en el varón",
    imagen: "flujogramas/fiebre-disuria-dolor-perineal-prostatitis.svg",
    alt: "Flujograma: Fiebre con síntomas urinarios en el varón"
  },
  "INF-043": {
    titulo: "Dengue grave por reinfección",
    imagen: "flujogramas/reinfeccion-dengue-choque-mediadores-vasoactivos.svg",
    alt: "Flujograma: Dengue grave por reinfección"
  },
  "NRL-023": {
    titulo: "Hematomas intracraneales",
    imagen: "flujogramas/anciano-tec-leve-semanas-deterioro-subdural-cronico.svg",
    alt: "Flujograma: Hematomas intracraneales"
  },
  "GIN-088": {
    titulo: "Hemorragia posparto: las 4 T",
    imagen: "flujogramas/parto-instrumentado-macrosomico-utero-contraido-desgarro.svg",
    alt: "Flujograma: Hemorragia posparto: las 4 T"
  },
  "NRL-024": {
    titulo: "Cefalea súbita con compromiso del III par",
    imagen: "flujogramas/cefalea-trueno-anisocoria-ptosis-hsa.svg",
    alt: "Flujograma: Cefalea súbita con compromiso del III par"
  },
  "END-023": {
    titulo: "Hipertensión secundaria endocrina",
    imagen: "flujogramas/crisis-adrenergicas-hta-refractaria-metanefrinas.svg",
    alt: "Flujograma: Hipertensión secundaria endocrina"
  },
  "CIR-054": {
    titulo: "Trauma abdominal cerrado",
    imagen: "flujogramas/trauma-abdominal-cerrado-sin-peritonitis-estable.svg",
    alt: "Flujograma: Trauma abdominal cerrado"
  },
  "END-024": {
    titulo: "Estudio de la función tiroidea",
    imagen: "flujogramas/calor-nerviosismo-polimenorrea-tsh-t4l.svg",
    alt: "Flujograma: Estudio de la función tiroidea"
  },
  "HEM-019": {
    titulo: "Niño con citopenias y dolor óseo",
    imagen: "flujogramas/nino-dolor-oseo-nocturno-petequias-lla.svg",
    alt: "Flujograma: Niño con citopenias y dolor óseo"
  },
  "NRL-025": {
    titulo: "Lesión con realce en anillo",
    imagen: "flujogramas/masa-realce-anillo-necrosis-glioblastoma.svg",
    alt: "Flujograma: Lesión con realce en anillo"
  },
  "REU-026": {
    titulo: "Dermatomiositis: criterios",
    imagen: "flujogramas/debilidad-proximal-heliotropo-dermatomiositis.svg",
    alt: "Flujograma: Dermatomiositis: criterios"
  },
  "SP-059": {
    titulo: "Niveles de ocurrencia de una enfermedad",
    imagen: "flujogramas/covid-casos-esperados-vacunados-endemia.svg",
    alt: "Flujograma: Niveles de ocurrencia de una enfermedad"
  },
  "GIN-089": {
    titulo: "Complicaciones de la hiperémesis",
    imagen: "flujogramas/hiperemesis-confusion-ataxia-nistagmo-tiamina.svg",
    alt: "Flujograma: Complicaciones de la hiperémesis"
  },
  "END-025": {
    titulo: "Hipotiroidismo: iniciar levotiroxina",
    imagen: "flujogramas/hipotiroidismo-tsh-52-levotiroxina.svg",
    alt: "Flujograma: Hipotiroidismo: iniciar levotiroxina"
  },
  "END-026": {
    titulo: "Insuficiencia suprarrenal",
    imagen: "flujogramas/sincope-ortostatico-hiperpigmentacion-hiperkalemia-addison.svg",
    alt: "Flujograma: Insuficiencia suprarrenal"
  },
  "SP-060": {
    titulo: "Salud ocupacional",
    imagen: "flujogramas/salud-trabajadores-medicina-ocupacional.svg",
    alt: "Flujograma: Salud ocupacional"
  },
  "CAR-036": {
    titulo: "Cadena de supervivencia",
    imagen: "flujogramas/centro-comercial-paro-dea-desfibrilacion.svg",
    alt: "Flujograma: Cadena de supervivencia"
  },
  "SP-061": {
    titulo: "Enfoques del modelo de cuidado integral",
    imagen: "flujogramas/pertinencia-cultural-servicios-interculturalidad.svg",
    alt: "Flujograma: Enfoques del modelo de cuidado integral"
  },
  "PED-100": {
    titulo: "Malformaciones anorrectales",
    imagen: "flujogramas/ano-imperforado-nina-fistula-rectovestibular.svg",
    alt: "Flujograma: Malformaciones anorrectales"
  },
  "PED-101": {
    titulo: "Deterioro neurológico en el prematuro",
    imagen: "flujogramas/prematuro-32-semanas-letargia-fontanela-llena-hiv.svg",
    alt: "Flujograma: Deterioro neurológico en el prematuro"
  },
  "GAS-034": {
    titulo: "Hepatitis A: serología",
    imagen: "flujogramas/adolescente-ictericia-igm-anti-vha.svg",
    alt: "Flujograma: Hepatitis A: serología"
  },
  "OFT-021": {
    titulo: "Maculopatía en paciente con lupus",
    imagen: "flujogramas/lupus-hidroxicloroquina-maculopatia-bilateral.svg",
    alt: "Flujograma: Maculopatía en paciente con lupus"
  },
  "INF-044": {
    titulo: "Análisis del líquido ascítico",
    imagen: "flujogramas/ascitis-exudado-linfocitos-peritonitis-tuberculosa.svg",
    alt: "Flujograma: Análisis del líquido ascítico"
  },
  "GIN-090": {
    titulo: "Enfermedad trofoblástica gestacional",
    imagen: "flujogramas/tormenta-de-nieve-utero-grande-mola-evacuacion.svg",
    alt: "Flujograma: Enfermedad trofoblástica gestacional"
  },
  "TRA-016": {
    titulo: "Displasia de cadera: estudio según la edad",
    imagen: "flujogramas/recien-nacido-cadera-ecografia-graf.svg",
    alt: "Flujograma: Displasia de cadera: estudio según la edad"
  },
  "SP-062": {
    titulo: "Principios de gestión",
    imagen: "flujogramas/asis-uso-racional-recursos-eficiencia.svg",
    alt: "Flujograma: Principios de gestión"
  },
  "PED-102": {
    titulo: "Neonato de 9 días decaído",
    imagen: "flujogramas/neonato-9-dias-ictericia-oliguria-hipoactivo-sepsis-tardia.svg",
    alt: "Flujograma: Neonato de 9 días decaído"
  },
  "PSI-017": {
    titulo: "Episodio depresivo: criterios",
    imagen: "flujogramas/tristeza-seis-semanas-ideas-suicidas-episodio-depresivo.svg",
    alt: "Flujograma: Episodio depresivo: criterios"
  },
  "CB-029": {
    titulo: "Biotransformación hepática",
    imagen: "flujogramas/higado-xenobioticos-fase-1-hidroxilacion.svg",
    alt: "Flujograma: Biotransformación hepática"
  },
  "CIR-055": {
    titulo: "Obstrucción por cáncer colorrectal",
    imagen: "flujogramas/anciano-obstruccion-masa-rectal-colostomia.svg",
    alt: "Flujograma: Obstrucción por cáncer colorrectal"
  },
  "CAR-037": {
    titulo: "Chagas crónico",
    imagen: "flujogramas/arequipa-cardiomegalia-megaesofago-megacolon-chagas.svg",
    alt: "Flujograma: Chagas crónico"
  },
  "CIR-056": {
    titulo: "Politraumatizado: ABCDE",
    imagen: "flujogramas/motociclista-sin-casco-glasgow-8-intubacion.svg",
    alt: "Flujograma: Politraumatizado: ABCDE"
  },
  "NRL-026": {
    titulo: "Tipos de demencia",
    imagen: "flujogramas/deterioro-atencional-alucinaciones-parkinsonismo-lewy.svg",
    alt: "Flujograma: Tipos de demencia"
  },
  "OFT-022": {
    titulo: "Trauma del pabellón auricular",
    imagen: "flujogramas/golpe-pabellon-auricular-hematoma-subpericondrico.svg",
    alt: "Flujograma: Trauma del pabellón auricular"
  },
  "PED-103": {
    titulo: "Síndrome nefrótico: proteinuria en el niño",
    imagen: "flujogramas/nino-edema-proteinuria-rango-nefrotico-pediatrico.svg",
    alt: "Flujograma: Síndrome nefrótico: proteinuria en el niño"
  },
  "HEM-020": {
    titulo: "Trombocitopenia por heparina: 4T",
    imagen: "flujogramas/heparina-dia-8-plaquetas-27000-trombocitopenia.svg",
    alt: "Flujograma: Trombocitopenia por heparina: 4T"
  },
  "GAS-035": {
    titulo: "Hiperbilirrubinemias",
    imagen: "flujogramas/ictericia-ayuno-bilirrubina-indirecta-gilbert.svg",
    alt: "Flujograma: Hiperbilirrubinemias"
  },
  "HEM-021": {
    titulo: "Petequias en la niña tras una infección",
    imagen: "flujogramas/nina-petequias-gingivorragia-postviral-pti.svg",
    alt: "Flujograma: Petequias en la niña tras una infección"
  },
  "CB-030": {
    titulo: "Fármacos para la disfunción eréctil",
    imagen: "flujogramas/disfuncion-erectil-vision-azulada-sildenafilo.svg",
    alt: "Flujograma: Fármacos para la disfunción eréctil"
  },
  "GIN-091": {
    titulo: "Contracciones antes de término",
    imagen: "flujogramas/32-semanas-contracciones-cervix-35-fibronectina-negativa.svg",
    alt: "Flujograma: Contracciones antes de término"
  },
  "INF-045": {
    titulo: "Efectos adversos de los antituberculosos",
    imagen: "flujogramas/esquema-1-vision-colores-verde-etambutol.svg",
    alt: "Flujograma: Efectos adversos de los antituberculosos"
  },
  "CAR-038": {
    titulo: "Soplos valvulares",
    imagen: "flujogramas/pulso-salton-soplo-diastolico-austin-flint.svg",
    alt: "Flujograma: Soplos valvulares"
  },
  "PED-104": {
    titulo: "Ictericia colestásica neonatal",
    imagen: "flujogramas/rn-20-dias-acolia-bilirrubina-directa-atresia.svg",
    alt: "Flujograma: Ictericia colestásica neonatal"
  },
  "GIN-092": {
    titulo: "Hemostasia del lecho placentario",
    imagen: "flujogramas/pinard-miometrio-hemostasia-posparto.svg",
    alt: "Flujograma: Hemostasia del lecho placentario"
  },
  "INF-046": {
    titulo: "Artritis séptica según el Gram",
    imagen: "flujogramas/rodilla-diplococos-gramnegativos-artritis-gonococica.svg",
    alt: "Flujograma: Artritis séptica según el Gram"
  },
  "INF-047": {
    titulo: "Lesiones violáceas en VIH",
    imagen: "flujogramas/vih-cd4-bajo-nodulos-violaceos-kaposi.svg",
    alt: "Flujograma: Lesiones violáceas en VIH"
  },
  "CB-031": {
    titulo: "Fármacos usados en COVID-19 y sus riesgos",
    imagen: "flujogramas/automedicacion-covid-qt-largo-azitromicina.svg",
    alt: "Flujograma: Fármacos usados en COVID-19 y sus riesgos"
  },
  "NEU-027": {
    titulo: "Neumoconiosis",
    imagen: "flujogramas/asbesto-30-anos-panal-cuerpos-ferruginosos.svg",
    alt: "Flujograma: Neumoconiosis"
  },
  "NEF-037": {
    titulo: "Albuminuria en la diabetes",
    imagen: "flujogramas/diabetico-albuminuria-1g-ieca.svg",
    alt: "Flujograma: Albuminuria en la diabetes"
  },
  "SP-063": {
    titulo: "Carta de Ottawa",
    imagen: "flujogramas/lactancia-exclusiva-comunicacion-educativa-habilidades.svg",
    alt: "Flujograma: Carta de Ottawa"
  },
  "INF-048": {
    titulo: "Diarrea acuosa profusa",
    imagen: "flujogramas/diarrea-agua-de-arroz-calambres-colera.svg",
    alt: "Flujograma: Diarrea acuosa profusa"
  },
  "SP-064": {
    titulo: "Diseños de estudio",
    imagen: "flujogramas/encuesta-escolares-embarazo-estudio-transversal.svg",
    alt: "Flujograma: Diseños de estudio"
  },
  "OFT-023": {
    titulo: "Tipos de glaucoma",
    imagen: "flujogramas/glaucoma-mas-frecuente-angulo-abierto.svg",
    alt: "Flujograma: Tipos de glaucoma"
  },
  "GIN-093": {
    titulo: "Vasa previa: momento del parto",
    imagen: "flujogramas/vasa-previa-cesarea-34-35-semanas.svg",
    alt: "Flujograma: Vasa previa: momento del parto"
  },
  "PED-105": {
    titulo: "Ingesta de cáusticos en el niño",
    imagen: "flujogramas/lejia-estridor-sialorrea-intubacion.svg",
    alt: "Flujograma: Ingesta de cáusticos en el niño"
  },
  "PSI-018": {
    titulo: "Mujer joven que oye voces",
    imagen: "flujogramas/voces-le-quieren-hacer-dano-psicosis.svg",
    alt: "Flujograma: Mujer joven que oye voces"
  },
  "NEF-038": {
    titulo: "Uropatía obstructiva por HBP",
    imagen: "flujogramas/hbp-residuo-vesical-creatinina-rtu.svg",
    alt: "Flujograma: Uropatía obstructiva por HBP"
  },
  "NEF-039": {
    titulo: "Pielonefritis obstructiva",
    imagen: "flujogramas/calculo-enclavado-fiebre-hipotension-doble-j.svg",
    alt: "Flujograma: Pielonefritis obstructiva"
  },
  "INF-049": {
    titulo: "Vacuna contra la fiebre amarilla",
    imagen: "flujogramas/serumista-selva-vacuna-fiebre-amarilla-dosis-unica.svg",
    alt: "Flujograma: Vacuna contra la fiebre amarilla"
  },
  "CAR-039": {
    titulo: "Infarto con elevación del ST",
    imagen: "flujogramas/st-elevado-anterolateral-angioplastia-primaria.svg",
    alt: "Flujograma: Infarto con elevación del ST"
  },
  "GIN-094": {
    titulo: "Náuseas y vómitos del embarazo",
    imagen: "flujogramas/nauseas-8-semanas-doxilamina-piridoxina.svg",
    alt: "Flujograma: Náuseas y vómitos del embarazo"
  },
  "PED-106": {
    titulo: "Cardiopatía con cianosis y corazón en bota",
    imagen: "flujogramas/cianosis-corazon-en-bota-tetralogia-fallot.svg",
    alt: "Flujograma: Cardiopatía con cianosis y corazón en bota"
  },
  "NRL-027": {
    titulo: "Hidrocefalia aguda: medidas iniciales",
    imagen: "flujogramas/hidrocefalia-aguda-cabecera-30-grados.svg",
    alt: "Flujograma: Hidrocefalia aguda: medidas iniciales"
  },
  "GIN-095": {
    titulo: "Antiepilépticos en el embarazo",
    imagen: "flujogramas/epilepsia-gestante-levetiracetam.svg",
    alt: "Flujograma: Antiepilépticos en el embarazo"
  },
  "CAR-040": {
    titulo: "Infarto con choque cardiogénico",
    imagen: "flujogramas/infarto-24-horas-hipotension-crepitantes-inotropicos.svg",
    alt: "Flujograma: Infarto con choque cardiogénico"
  },
  "SP-065": {
    titulo: "Escenarios de la promoción de la salud",
    imagen: "flujogramas/vih-adolescentes-comunicacion-educativa-colegio.svg",
    alt: "Flujograma: Escenarios de la promoción de la salud"
  },
  "GAS-036": {
    titulo: "Falla hepática por paracetamol",
    imagen: "flujogramas/paracetamol-inr-6-asterixis-n-acetilcisteina.svg",
    alt: "Flujograma: Falla hepática por paracetamol"
  },
  "PED-107": {
    titulo: "Faringoamigdalitis estreptocócica",
    imagen: "flujogramas/exudado-petequias-paladar-amoxicilina-10-dias.svg",
    alt: "Flujograma: Faringoamigdalitis estreptocócica"
  },
  "INF-050": {
    titulo: "Meningitis: análisis del LCR",
    imagen: "flujogramas/lcr-linfocitos-glucosa-baja-miliar-meningitis-tb.svg",
    alt: "Flujograma: Meningitis: análisis del LCR"
  },
  "PED-108": {
    titulo: "Contraindicación de la vacuna contra influenza",
    imagen: "flujogramas/vacuna-influenza-contraindicacion-menor-6-meses.svg",
    alt: "Flujograma: Contraindicación de la vacuna contra influenza"
  },
  "PSI-019": {
    titulo: "Síndrome neuroléptico maligno",
    imagen: "flujogramas/haloperidol-rigidez-fiebre-cpk-neuroleptico-maligno.svg",
    alt: "Flujograma: Síndrome neuroléptico maligno"
  },
  "GIN-096": {
    titulo: "Sangrado uterino anormal",
    imagen: "flujogramas/sangrado-uterino-endometrio-24-mm-biopsia.svg",
    alt: "Flujograma: Sangrado uterino anormal"
  },
  "SP-066": {
    titulo: "Coberturas de vacunación VPH en descenso",
    imagen: "flujogramas/vph-escolares-coordinacion-intersectorial.svg",
    alt: "Flujograma: Coberturas de vacunación VPH en descenso"
  },
  "GIN-097": {
    titulo: "Diabetes en el embarazo: tratamiento",
    imagen: "flujogramas/diabetes-pregestacional-macrosomia-insulina.svg",
    alt: "Flujograma: Diabetes en el embarazo: tratamiento"
  },
  "TRA-017": {
    titulo: "Escoliosis: ángulo de Cobb",
    imagen: "flujogramas/angulo-cobb-30-escoliosis-moderada.svg",
    alt: "Flujograma: Escoliosis: ángulo de Cobb"
  },
  "GIN-098": {
    titulo: "Prolapso genital: estadios POP-Q",
    imagen: "flujogramas/popq-ba-menos-1-asintomatica-kegel.svg",
    alt: "Flujograma: Prolapso genital: estadios POP-Q"
  },
  "SP-067": {
    titulo: "Principios de la bioética",
    imagen: "flujogramas/paciente-lucido-delega-decision-hijo-autonomia.svg",
    alt: "Flujograma: Principios de la bioética"
  },
  "SP-068": {
    titulo: "Valores de la atención primaria",
    imagen: "flujogramas/anemia-55-vs-5-distritos-equidad.svg",
    alt: "Flujograma: Valores de la atención primaria"
  },
  "PED-109": {
    titulo: "Urocultivo en el lactante",
    imagen: "flujogramas/lactante-pielonefritis-urocultivo-sondaje.svg",
    alt: "Flujograma: Urocultivo en el lactante"
  },
  "TRA-018": {
    titulo: "Displasia de cadera: tratamiento por edad",
    imagen: "flujogramas/ortolani-positivo-2-meses-arnes-pavlik.svg",
    alt: "Flujograma: Displasia de cadera: tratamiento por edad"
  },
  "INF-051": {
    titulo: "Convulsión y quiste cerebral",
    imagen: "flujogramas/ayacucho-convulsion-quiste-escolex-neurocisticercosis.svg",
    alt: "Flujograma: Convulsión y quiste cerebral"
  },
  "GAS-037": {
    titulo: "Peritonitis bacteriana espontánea",
    imagen: "flujogramas/ascitis-pmn-7000-peritonitis-espontanea-ceftriaxona.svg",
    alt: "Flujograma: Peritonitis bacteriana espontánea"
  },
  "SP-069": {
    titulo: "Prevalencia, incidencia y letalidad",
    imagen: "flujogramas/letalidad-cero-casos-nuevos-prevalencia-aumenta.svg",
    alt: "Flujograma: Prevalencia, incidencia y letalidad"
  },
  "NRL-028": {
    titulo: "Sospecha de hemorragia subaracnoidea",
    imagen: "flujogramas/cefalea-subita-rigidez-nuca-tem-cerebral.svg",
    alt: "Flujograma: Sospecha de hemorragia subaracnoidea"
  },
  "CAR-041": {
    titulo: "Daño de órgano blanco por HTA",
    imagen: "flujogramas/hta-galope-retinopatia-iv-cardiopatia-hipertensiva.svg",
    alt: "Flujograma: Daño de órgano blanco por HTA"
  },
  "GIN-099": {
    titulo: "Tóxicos en el embarazo",
    imagen: "flujogramas/gestante-fuma-15-cigarrillos-rciu.svg",
    alt: "Flujograma: Tóxicos en el embarazo"
  },
  "GIN-100": {
    titulo: "Salpingitis: criterios diagnósticos",
    imagen: "flujogramas/hidrosonografia-dolor-anexial-salpingitis.svg",
    alt: "Flujograma: Salpingitis: criterios diagnósticos"
  },
  "SP-070": {
    titulo: "Niveles de prevención",
    imagen: "flujogramas/campana-deteccion-vih-prevencion-secundaria.svg",
    alt: "Flujograma: Niveles de prevención"
  },
  "CIR-057": {
    titulo: "Hernia inguinal: tipos",
    imagen: "flujogramas/tumoracion-inguinal-irreductible-distension-hernia-complicada.svg",
    alt: "Flujograma: Hernia inguinal: tipos"
  },
  "INF-052": {
    titulo: "Serología de la hepatitis B",
    imagen: "flujogramas/estudiante-medicina-anti-hbs-inmunidad.svg",
    alt: "Flujograma: Serología de la hepatitis B"
  },
  "CAR-042": {
    titulo: "Soporte vital básico: primeros pasos",
    imagen: "flujogramas/persona-se-desploma-calle-escena-segura.svg",
    alt: "Flujograma: Soporte vital básico: primeros pasos"
  },
  "GAS-038": {
    titulo: "Ictericia tras una transfusión",
    imagen: "flujogramas/nino-transfusion-7-semanas-ictericia-hepatitis-b.svg",
    alt: "Flujograma: Ictericia tras una transfusión"
  },
  "NRL-029": {
    titulo: "Hemorragia hipertensiva: ¿dónde está?",
    imagen: "flujogramas/hipertenso-coma-pupilas-puntiformes-protuberancia.svg",
    alt: "Flujograma: Hemorragia hipertensiva: ¿dónde está?"
  },
  "END-027": {
    titulo: "Amenorrea tras hemorragia posparto",
    imagen: "flujogramas/hemorragia-posparto-no-lacto-amenorrea-sheehan.svg",
    alt: "Flujograma: Amenorrea tras hemorragia posparto"
  },
  "INF-053": {
    titulo: "Fiebre, ictericia y mialgias",
    imagen: "flujogramas/ribera-rimac-mialgia-pantorrillas-sufusion-leptospirosis.svg",
    alt: "Flujograma: Fiebre, ictericia y mialgias"
  },
  "SP-071": {
    titulo: "Obesidad escolar: factores de riesgo",
    imagen: "flujogramas/escolares-imc-mayor-25-sedentarismo.svg",
    alt: "Flujograma: Obesidad escolar: factores de riesgo"
  },
  "CB-032": {
    titulo: "Triángulo femoral: relaciones",
    imagen: "flujogramas/acceso-vena-femoral-medial-arteria.svg",
    alt: "Flujograma: Triángulo femoral: relaciones"
  },
  "CIR-058": {
    titulo: "Hemotórax traumático",
    imagen: "flujogramas/trauma-timon-matidez-hemotorax-tubo-toracico.svg",
    alt: "Flujograma: Hemotórax traumático"
  },
  "GAS-039": {
    titulo: "Pancreatitis: buscar la causa",
    imagen: "flujogramas/pancreatitis-ictericia-bilirrubina-directa-colangiorresonancia.svg",
    alt: "Flujograma: Pancreatitis: buscar la causa"
  },
  "REU-027": {
    titulo: "Análisis del líquido sinovial",
    imagen: "flujogramas/rodilla-80000-leucocitos-artritis-septica.svg",
    alt: "Flujograma: Análisis del líquido sinovial"
  },
  "TRA-019": {
    titulo: "Fractura expuesta de tibia",
    imagen: "flujogramas/atropello-fractura-expuesta-conminuta-tibia-fijacion-externa.svg",
    alt: "Flujograma: Fractura expuesta de tibia"
  },
  "SP-072": {
    titulo: "Triada epidemiológica",
    imagen: "flujogramas/malaria-vivax-lima-sin-vector-ambiente.svg",
    alt: "Flujograma: Triada epidemiológica"
  },
  "SP-073": {
    titulo: "Población y muestra",
    imagen: "flujogramas/club-adulto-mayor-encuesta-100-poblacion.svg",
    alt: "Flujograma: Población y muestra"
  },
  "CAR-043": {
    titulo: "Trauma precordial con hipotensión",
    imagen: "flujogramas/golpe-precordial-ruidos-apagados-iy-ecocardiograma.svg",
    alt: "Flujograma: Trauma precordial con hipotensión"
  },
  "PED-110": {
    titulo: "Deshidratación grave con choque",
    imagen: "flujogramas/lactante-diarrea-soporoso-llenado-5-seg-bolo.svg",
    alt: "Flujograma: Deshidratación grave con choque"
  },
  "HEM-022": {
    titulo: "Anemia macrocítica con parestesias",
    imagen: "flujogramas/vcm-110-hipersegmentados-parestesias-megaloblastica.svg",
    alt: "Flujograma: Anemia macrocítica con parestesias"
  },
  "REU-028": {
    titulo: "Prurito nocturno en el niño",
    imagen: "flujogramas/prurito-nocturno-interdigital-escabiosis.svg",
    alt: "Flujograma: Prurito nocturno en el niño"
  },
  "OFT-024": {
    titulo: "Otorrea con prurito del conducto",
    imagen: "flujogramas/prurito-conducto-otorrea-otitis-externa.svg",
    alt: "Flujograma: Otorrea con prurito del conducto"
  },
  "NEF-040": {
    titulo: "Hiponatremia por tiazidas",
    imagen: "flujogramas/anciana-sopor-sodio-115-tiazida.svg",
    alt: "Flujograma: Hiponatremia por tiazidas"
  },
  "CB-033": {
    titulo: "Células del riñón y sus funciones",
    imagen: "flujogramas/aldosterona-celulas-principales-tubulo-colector.svg",
    alt: "Flujograma: Células del riñón y sus funciones"
  },
  "SP-074": {
    titulo: "Decisiones en el menor de edad",
    imagen: "flujogramas/nino-10-anos-acepta-procedimiento-asentimiento.svg",
    alt: "Flujograma: Decisiones en el menor de edad"
  },
  "CB-034": {
    titulo: "Antiácidos y sus efectos",
    imagen: "flujogramas/antiacido-hidroxido-aluminio-hipofosfatemia.svg",
    alt: "Flujograma: Antiácidos y sus efectos"
  },
  "SP-075": {
    titulo: "Prevención de dengue autóctono",
    imagen: "flujogramas/dengue-importado-aedes-participacion-comunitaria.svg",
    alt: "Flujograma: Prevención de dengue autóctono"
  },
  "REU-029": {
    titulo: "Acné: grados de severidad",
    imagen: "flujogramas/nina-12-anos-30-comedones-acne-leve.svg",
    alt: "Flujograma: Acné: grados de severidad"
  },
  "OFT-025": {
    titulo: "Tipos de conjuntivitis",
    imagen: "flujogramas/leganas-mucopurulentas-bilateral-conjuntivitis.svg",
    alt: "Flujograma: Tipos de conjuntivitis"
  },
  "INF-054": {
    titulo: "Meningitis: germen según la edad",
    imagen: "flujogramas/adulta-cefalea-rigidez-nuca-neumococo.svg",
    alt: "Flujograma: Meningitis: germen según la edad"
  },
  "GAS-040": {
    titulo: "ERGE con síntomas extraesofágicos",
    imagen: "flujogramas/obeso-pirosis-asma-nocturna-ibp.svg",
    alt: "Flujograma: ERGE con síntomas extraesofágicos"
  },
  "END-028": {
    titulo: "SIADH frente a deshidratación",
    imagen: "flujogramas/siadh-vs-privacion-agua-osmolaridad-plasmatica.svg",
    alt: "Flujograma: SIADH frente a deshidratación"
  },
  "GAS-041": {
    titulo: "Necrosis pancreática: cuándo drenar",
    imagen: "flujogramas/necrosis-pancreatica-drenaje-3-4-semanas.svg",
    alt: "Flujograma: Necrosis pancreática: cuándo drenar"
  },
  "GIN-101": {
    titulo: "VIH diagnosticado en el trabajo de parto",
    imagen: "flujogramas/vih-prueba-rapida-8-cm-zidovudina-parto-vaginal.svg",
    alt: "Flujograma: VIH diagnosticado en el trabajo de parto"
  },
  "PSI-020": {
    titulo: "Depresión: tratamiento por gravedad",
    imagen: "flujogramas/desempleo-animo-decaido-ideas-suicidas-sertralina.svg",
    alt: "Flujograma: Depresión: tratamiento por gravedad"
  },
  "GIN-102": {
    titulo: "Restricción del crecimiento fetal",
    imagen: "flujogramas/rciu-percentil-2-flujo-diastolico-invertido-terminar.svg",
    alt: "Flujograma: Restricción del crecimiento fetal"
  },
  "PED-111": {
    titulo: "Neumonía: ¿Rx de control?",
    imagen: "flujogramas/neumonia-lactante-mejoria-sin-rx-control.svg",
    alt: "Flujograma: Neumonía: ¿Rx de control?"
  },
  "TRA-020": {
    titulo: "Trauma cervical: criterios NEXUS",
    imagen: "flujogramas/volcadura-dolor-cervical-deficit-manos-collarin.svg",
    alt: "Flujograma: Trauma cervical: criterios NEXUS"
  },
  "PED-112": {
    titulo: "Rubéola congénita",
    imagen: "flujogramas/rubeola-materna-pulsos-saltones-ductus.svg",
    alt: "Flujograma: Rubéola congénita"
  },
  "END-029": {
    titulo: "Tipos de bocio",
    imagen: "flujogramas/brazos-elevados-congestion-cuello-pemberton.svg",
    alt: "Flujograma: Tipos de bocio"
  },
  "GIN-103": {
    titulo: "Manejo activo del alumbramiento",
    imagen: "flujogramas/alumbramiento-dirigido-preeclampsia-oxitocina.svg",
    alt: "Flujograma: Manejo activo del alumbramiento"
  },
  "REU-030": {
    titulo: "Placas descamativas y uñas alteradas",
    imagen: "flujogramas/placas-escama-nacarada-piqueteado-ungueal-psoriasis.svg",
    alt: "Flujograma: Placas descamativas y uñas alteradas"
  },
  "INF-055": {
    titulo: "Dengue: clasificación del caso",
    imagen: "flujogramas/viaje-zona-endemica-ns1-positivo-caso-confirmado.svg",
    alt: "Flujograma: Dengue: clasificación del caso"
  },
  "PED-113": {
    titulo: "Testículo fuera del escroto",
    imagen: "flujogramas/escroto-vacio-testiculo-perineal-ectopia.svg",
    alt: "Flujograma: Testículo fuera del escroto"
  },
  "NEU-028": {
    titulo: "Crisis de asma casi fatal",
    imagen: "flujogramas/asma-somnoliento-silencio-auscultatorio-intubacion.svg",
    alt: "Flujograma: Crisis de asma casi fatal"
  },
  "CB-035": {
    titulo: "Intoxicación por isoniazida",
    imagen: "flujogramas/sobredosis-isoniazida-acidosis-piridoxina.svg",
    alt: "Flujograma: Intoxicación por isoniazida"
  },
  "GAS-042": {
    titulo: "Cirrótico con fiebre y dolor abdominal",
    imagen: "flujogramas/cirrotico-fiebre-dolor-confusion-paracentesis.svg",
    alt: "Flujograma: Cirrótico con fiebre y dolor abdominal"
  },
  "PED-114": {
    titulo: "Hemorragia intraventricular: estudio",
    imagen: "flujogramas/prematuro-1100-g-apnea-palidez-eco-transfontanelar.svg",
    alt: "Flujograma: Hemorragia intraventricular: estudio"
  },
  "GAS-043": {
    titulo: "Falla hepática: clasificación temporal",
    imagen: "flujogramas/ictericia-8-dias-encefalopatia-falla-hepatica-aguda.svg",
    alt: "Flujograma: Falla hepática: clasificación temporal"
  },
  "GIN-104": {
    titulo: "Anticoncepción con carbamazepina",
    imagen: "flujogramas/carbamazepina-anticonceptivo-oral-menos-efectivo.svg",
    alt: "Flujograma: Anticoncepción con carbamazepina"
  },
  "GAS-044": {
    titulo: "Várices esofágicas: profilaxis primaria",
    imagen: "flujogramas/varices-grandes-profilaxis-primaria-betabloqueante.svg",
    alt: "Flujograma: Várices esofágicas: profilaxis primaria"
  },
  "REU-031": {
    titulo: "Debilidad proximal progresiva",
    imagen: "flujogramas/debilidad-proximal-simetrica-sin-piel-polimiositis.svg",
    alt: "Flujograma: Debilidad proximal progresiva"
  },
  "GIN-105": {
    titulo: "Hipertensión en la gestante",
    imagen: "flujogramas/metildopa-desde-8-semanas-pa-controlada-hta-cronica.svg",
    alt: "Flujograma: Hipertensión en la gestante"
  },
  "NEU-029": {
    titulo: "Exacerbación de EPOC con acidosis",
    imagen: "flujogramas/epoc-exacerbado-ph-708-confusion-intubacion.svg",
    alt: "Flujograma: Exacerbación de EPOC con acidosis"
  },
  "CIR-059": {
    titulo: "Obstrucción intestinal con masa inguinal",
    imagen: "flujogramas/anciana-masa-bajo-pliegue-inguinal-obstruccion-femoral.svg",
    alt: "Flujograma: Obstrucción intestinal con masa inguinal"
  },
  "PED-115": {
    titulo: "Sarampión: etapas",
    imagen: "flujogramas/fiebre-tos-coriza-conjuntivitis-koplik-sarampion.svg",
    alt: "Flujograma: Sarampión: etapas"
  },
  "NRL-030": {
    titulo: "Tipos de demencia",
    imagen: "flujogramas/anciana-deja-cocina-prendida-deambula-alzheimer.svg",
    alt: "Flujograma: Tipos de demencia"
  },
  "CAR-044": {
    titulo: "Ritmos de paro cardiaco",
    imagen: "flujogramas/paro-piscina-dea-descarga-fibrilacion-ventricular.svg",
    alt: "Flujograma: Ritmos de paro cardiaco"
  },
  "SP-076": {
    titulo: "Estilos de liderazgo",
    imagen: "flujogramas/director-comite-distrital-dengue-liderazgo-democratico.svg",
    alt: "Flujograma: Estilos de liderazgo"
  },
  "NRL-031": {
    titulo: "Espasmos de la mano al escribir",
    imagen: "flujogramas/espasmos-mano-al-escribir-distonia-focal.svg",
    alt: "Flujograma: Espasmos de la mano al escribir"
  },
  "CB-036": {
    titulo: "Adaptación a la altura",
    imagen: "flujogramas/lima-puno-cefalea-nauseas-alcalosis-respiratoria.svg",
    alt: "Flujograma: Adaptación a la altura"
  },
  "SP-077": {
    titulo: "Tipos de indicadores",
    imagen: "flujogramas/porcentaje-tb-visita-domiciliaria-indicador-proceso.svg",
    alt: "Flujograma: Tipos de indicadores"
  },
  "CB-037": {
    titulo: "Receptores adrenérgicos",
    imagen: "flujogramas/hbp-simpaticolitico-hipotension-ortostatica-alfa1.svg",
    alt: "Flujograma: Receptores adrenérgicos"
  },
  "GIN-106": {
    titulo: "Tamizaje temprano de diabetes en la gestante",
    imagen: "flujogramas/imc-34-macrosomia-familiar-dm-tamizaje-inmediato.svg",
    alt: "Flujograma: Tamizaje temprano de diabetes en la gestante"
  },
  "GIN-107": {
    titulo: "Amenorrea secundaria: ¿dónde falla?",
    imagen: "flujogramas/amenorrea-19-anos-fsh-lh-altas-falla-ovarica.svg",
    alt: "Flujograma: Amenorrea secundaria: ¿dónde falla?"
  },
  "PED-116": {
    titulo: "Reanimación neonatal",
    imagen: "flujogramas/rn-apnea-fc-90-vpp-aire-ambiente.svg",
    alt: "Flujograma: Reanimación neonatal"
  },
  "GIN-108": {
    titulo: "Lesión vaginal en prolapso total",
    imagen: "flujogramas/prolapso-total-lesion-vaginal-ulcera-decubito.svg",
    alt: "Flujograma: Lesión vaginal en prolapso total"
  },
  "CB-038": {
    titulo: "Efectos de los antimuscarínicos",
    imagen: "flujogramas/asmatico-ipratropio-retencion-urinaria.svg",
    alt: "Flujograma: Efectos de los antimuscarínicos"
  },
  "SP-078": {
    titulo: "Tipos de variables",
    imagen: "flujogramas/temperatura-ambiental-variable-continua.svg",
    alt: "Flujograma: Tipos de variables"
  },
  "OFT-026": {
    titulo: "Otitis media según el tiempo",
    imagen: "flujogramas/timpano-perforado-otorrea-fetida-otitis-media-cronica.svg",
    alt: "Flujograma: Otitis media según el tiempo"
  },
  "NEF-041": {
    titulo: "Sospecha de HTA renovascular",
    imagen: "flujogramas/mujer-joven-hta-refractaria-soplo-flanco-estenosis-renal.svg",
    alt: "Flujograma: Sospecha de HTA renovascular"
  },
  "CIR-060": {
    titulo: "Trauma abdominal con choque",
    imagen: "flujogramas/accidente-transito-choque-abdomen-doloroso-fast.svg",
    alt: "Flujograma: Trauma abdominal con choque"
  },
  "PED-117": {
    titulo: "Enfermedad de membrana hialina",
    imagen: "flujogramas/membrana-hialina-diabetes-materna.svg",
    alt: "Flujograma: Enfermedad de membrana hialina"
  },
  "NEF-042": {
    titulo: "Retención urinaria aguda",
    imagen: "flujogramas/globo-vesical-creatinina-potasio-sonda.svg",
    alt: "Flujograma: Retención urinaria aguda"
  },
  "NEU-030": {
    titulo: "Semiología del tórax",
    imagen: "flujogramas/matidez-abolicion-mv-egofonia-derrame-pleural.svg",
    alt: "Flujograma: Semiología del tórax"
  },
  "NRL-032": {
    titulo: "Hemorragia intracerebral: control de la PA",
    imagen: "flujogramas/hemorragia-intraparenquimal-pa-180-antihipertensivo.svg",
    alt: "Flujograma: Hemorragia intracerebral: control de la PA"
  },
  "CAR-045": {
    titulo: "IC: ¿qué fármaco prolonga la vida?",
    imagen: "flujogramas/insuficiencia-cardiaca-enalapril-sobrevida.svg",
    alt: "Flujograma: IC: ¿qué fármaco prolonga la vida?"
  },
  "OFT-027": {
    titulo: "Tapón de cerumen",
    imagen: "flujogramas/tapon-cerumen-irrigacion-salino-tibio.svg",
    alt: "Flujograma: Tapón de cerumen"
  },
  "PED-118": {
    titulo: "Tumefacciones del cuero cabelludo del RN",
    imagen: "flujogramas/rn-tumoracion-parietal-no-cruza-sutura-cefalohematoma.svg",
    alt: "Flujograma: Tumefacciones del cuero cabelludo del RN"
  },
  "REU-032": {
    titulo: "Poliarteritis nudosa: criterios",
    imagen: "flujogramas/hepatitis-b-livedo-dolor-testicular-poliarteritis-nudosa.svg",
    alt: "Flujograma: Poliarteritis nudosa: criterios"
  },
  "SP-079": {
    titulo: "Decisiones al final de la vida",
    imagen: "flujogramas/cancer-metastasico-oxigeno-analgesia-ortotanasia.svg",
    alt: "Flujograma: Decisiones al final de la vida"
  },
  "NRL-033": {
    titulo: "Lesiones cerebrales múltiples con anillo",
    imagen: "flujogramas/fumador-convulsion-dos-lesiones-anillo-metastasis.svg",
    alt: "Flujograma: Lesiones cerebrales múltiples con anillo"
  },
  "PED-119": {
    titulo: "Laboratorio en sepsis neonatal",
    imagen: "flujogramas/corioamnionitis-hipotermia-indice-it-sepsis.svg",
    alt: "Flujograma: Laboratorio en sepsis neonatal"
  },
  "PED-120": {
    titulo: "Convulsiones tras varicela",
    imagen: "flujogramas/varicela-aspirina-convulsion-hepatomegalia-reye.svg",
    alt: "Flujograma: Convulsiones tras varicela"
  },
  "NEF-043": {
    titulo: "Lesión renal: prerrenal vs necrosis tubular",
    imagen: "flujogramas/secuestro-sin-agua-oliguria-sodio-urinario-bajo.svg",
    alt: "Flujograma: Lesión renal: prerrenal vs necrosis tubular"
  },
  "SP-080": {
    titulo: "Propiedades del agente infeccioso",
    imagen: "flujogramas/capacidad-producir-enfermedad-patogenicidad.svg",
    alt: "Flujograma: Propiedades del agente infeccioso"
  },
  "GIN-109": {
    titulo: "Presentación de cara",
    imagen: "flujogramas/presentacion-cara-mentoanterior-parto-vaginal.svg",
    alt: "Flujograma: Presentación de cara"
  },
  "CIR-061": {
    titulo: "Quemadura circunferencial",
    imagen: "flujogramas/quemadura-circunferencial-pierna-sin-pulso-escarotomia.svg",
    alt: "Flujograma: Quemadura circunferencial"
  },
  "NEF-044": {
    titulo: "Infección renal crónica con macrófagos espumosos",
    imagen: "flujogramas/litiasis-itu-repeticion-macrofagos-espumosos-xantogranulomatosa.svg",
    alt: "Flujograma: Infección renal crónica con macrófagos espumosos"
  },
  "END-030": {
    titulo: "Actividad física en la diabetes",
    imagen: "flujogramas/diabetes-actividad-fisica-150-minutos.svg",
    alt: "Flujograma: Actividad física en la diabetes"
  },
  "PED-121": {
    titulo: "Colestasis del lactante",
    imagen: "flujogramas/lactante-4-semanas-acolia-bilirrubina-directa-ecografia.svg",
    alt: "Flujograma: Colestasis del lactante"
  },
  "GIN-110": {
    titulo: "PAP con lesión de alto grado",
    imagen: "flujogramas/pap-lesion-alto-grado-colposcopia-biopsia.svg",
    alt: "Flujograma: PAP con lesión de alto grado"
  },
  "REU-033": {
    titulo: "Lupus: criterios EULAR/ACR",
    imagen: "flujogramas/eritema-facial-proteinuria-derrame-pleural-lupus.svg",
    alt: "Flujograma: Lupus: criterios EULAR/ACR"
  },
  "CAR-046": {
    titulo: "Encefalopatía hipertensiva",
    imagen: "flujogramas/papiledema-confusion-pa-190-120-labetalol.svg",
    alt: "Flujograma: Encefalopatía hipertensiva"
  },
  "END-031": {
    titulo: "Tirotoxicosis: origen",
    imagen: "flujogramas/pastillas-adelgazar-tsh-indetectable-tiroides-no-palpable-facticia.svg",
    alt: "Flujograma: Tirotoxicosis: origen"
  },
  "SP-081": {
    titulo: "Tipos de muestreo",
    imagen: "flujogramas/150-casos-no-aleatorio-muestreo-conveniencia.svg",
    alt: "Flujograma: Tipos de muestreo"
  },
  "END-032": {
    titulo: "Hipertiroidismo con exoftalmos",
    imagen: "flujogramas/bocio-exoftalmos-mixedema-pretibial-graves.svg",
    alt: "Flujograma: Hipertiroidismo con exoftalmos"
  },
  "TRA-021": {
    titulo: "Pie equinovaro: método Ponseti",
    imagen: "flujogramas/lactante-pie-equinovaro-referir-ortopedista.svg",
    alt: "Flujograma: Pie equinovaro: método Ponseti"
  },
  "GIN-111": {
    titulo: "VIH: vía del parto según carga viral",
    imagen: "flujogramas/vih-tar-carga-viral-500-parto-vaginal.svg",
    alt: "Flujograma: VIH: vía del parto según carga viral"
  },
  "CB-039": {
    titulo: "Intoxicación por opioides",
    imagen: "flujogramas/miosis-bradipnea-sopor-venopunturas-naloxona.svg",
    alt: "Flujograma: Intoxicación por opioides"
  },
  "SP-082": {
    titulo: "TB en población migrante",
    imagen: "flujogramas/tb-asentamiento-migrante-comunicacion-educativa.svg",
    alt: "Flujograma: TB en población migrante"
  },
  "TRA-022": {
    titulo: "Fractura diafisaria de húmero",
    imagen: "flujogramas/fractura-diafisis-humero-no-desplazada-ortesis.svg",
    alt: "Flujograma: Fractura diafisaria de húmero"
  },
  "NEF-045": {
    titulo: "Dolor agudo en flanco",
    imagen: "flujogramas/dolor-flanco-irradia-testiculo-sin-postura-colico-renal.svg",
    alt: "Flujograma: Dolor agudo en flanco"
  },
  "PED-122": {
    titulo: "Infección del cordón umbilical",
    imagen: "flujogramas/onfalitis-celulitis-periumbilical-antibiotico-sistemico.svg",
    alt: "Flujograma: Infección del cordón umbilical"
  },
  "NEF-046": {
    titulo: "Neuropatía autonómica diabética",
    imagen: "flujogramas/diabetico-30-anos-goteo-globo-vesical-vejiga-neurogenica.svg",
    alt: "Flujograma: Neuropatía autonómica diabética"
  },
  "INF-056": {
    titulo: "Brucelosis",
    imagen: "flujogramas/veterinario-fiebre-ondulante-rosa-bengala-brucelosis.svg",
    alt: "Flujograma: Brucelosis"
  },
  "REU-034": {
    titulo: "Prurito del cuero cabelludo",
    imagen: "flujogramas/nina-prurito-cuero-cabelludo-liendres-pediculosis.svg",
    alt: "Flujograma: Prurito del cuero cabelludo"
  },
  "INF-057": {
    titulo: "VIH: periodo de ventana",
    imagen: "flujogramas/relacion-riesgo-20-dias-elisa-cuarta-generacion.svg",
    alt: "Flujograma: VIH: periodo de ventana"
  },
  "GIN-112": {
    titulo: "Amenaza de parto pretérmino",
    imagen: "flujogramas/32-semanas-contracciones-cervix-15-mm-corticoides-tocolisis.svg",
    alt: "Flujograma: Amenaza de parto pretérmino"
  },
  "GIN-113": {
    titulo: "Vaginosis bacteriana: criterios de Amsel",
    imagen: "flujogramas/flujo-gris-fetido-celulas-clave-gardnerella.svg",
    alt: "Flujograma: Vaginosis bacteriana: criterios de Amsel"
  },
  "OFT-028": {
    titulo: "Cuerpo extraño ocular",
    imagen: "flujogramas/cuerpo-extrano-incrustado-perforacion-no-retirar.svg",
    alt: "Flujograma: Cuerpo extraño ocular"
  },
  "GIN-114": {
    titulo: "Anticoncepción tras enfermedad molar",
    imagen: "flujogramas/mola-evacuada-vigilancia-implante-progestina.svg",
    alt: "Flujograma: Anticoncepción tras enfermedad molar"
  },
  "PED-123": {
    titulo: "Hipoglucemia neonatal",
    imagen: "flujogramas/prematuro-2200-g-temblores-hipoactivo-hipoglucemia.svg",
    alt: "Flujograma: Hipoglucemia neonatal"
  },
  "INF-058": {
    titulo: "Adenopatías cervicales crónicas",
    imagen: "flujogramas/adenopatias-cervicales-fistula-caseosa-tb-ganglionar.svg",
    alt: "Flujograma: Adenopatías cervicales crónicas"
  },
  "NEU-031": {
    titulo: "Asma: clasificación por gravedad",
    imagen: "flujogramas/sintomas-2-dias-semana-2-noches-mes-asma-intermitente.svg",
    alt: "Flujograma: Asma: clasificación por gravedad"
  },
  "REU-035": {
    titulo: "Lesión en pliegues inguinales",
    imagen: "flujogramas/obesa-diabetica-pliegues-inguinales-candida.svg",
    alt: "Flujograma: Lesión en pliegues inguinales"
  },
  "NRL-034": {
    titulo: "Miastenia gravis: unión neuromuscular",
    imagen: "flujogramas/ptosis-diplopia-fatiga-receptor-nicotinico.svg",
    alt: "Flujograma: Miastenia gravis: unión neuromuscular"
  },
  "INF-059": {
    titulo: "Endocarditis: germen según el contexto",
    imagen: "flujogramas/drogas-ev-janeway-soplo-mitral-staphylococcus.svg",
    alt: "Flujograma: Endocarditis: germen según el contexto"
  },
  "PED-124": {
    titulo: "Eventos centinela intraparto",
    imagen: "flujogramas/evento-centinela-encefalopatia-hipoxica-dpp.svg",
    alt: "Flujograma: Eventos centinela intraparto"
  },
  "CB-040": {
    titulo: "Músculos de la lengua",
    imagen: "flujogramas/sacar-lengua-musculo-geniogloso.svg",
    alt: "Flujograma: Músculos de la lengua"
  },
  "INF-060": {
    titulo: "Dengue: examen según el día",
    imagen: "flujogramas/piura-fiebre-2-dias-leucopenia-ns1.svg",
    alt: "Flujograma: Dengue: examen según el día"
  },
  "GIN-115": {
    titulo: "Hemorragia posparto con útero contraído",
    imagen: "flujogramas/cesarea-14-meses-sangrado-utero-contraido-dehiscencia.svg",
    alt: "Flujograma: Hemorragia posparto con útero contraído"
  },
  "GIN-116": {
    titulo: "VIH en la gestante",
    imagen: "flujogramas/gestante-14-semanas-vih-confirmado-tar-inmediato.svg",
    alt: "Flujograma: VIH en la gestante"
  },
  "SP-083": {
    titulo: "Decisiones ante el pedido de morir",
    imagen: "flujogramas/terminal-pide-morir-medico-omite-medidas-eutanasia-pasiva.svg",
    alt: "Flujograma: Decisiones ante el pedido de morir"
  },
  "GIN-117": {
    titulo: "Hemorragia del tercer trimestre",
    imagen: "flujogramas/dos-cesareas-dolor-choque-latidos-ausentes-rotura-uterina.svg",
    alt: "Flujograma: Hemorragia del tercer trimestre"
  },
  "GAS-045": {
    titulo: "Encefalopatía hepática",
    imagen: "flujogramas/cirrotico-estrenimiento-flapping-lactulosa.svg",
    alt: "Flujograma: Encefalopatía hepática"
  },
  "NRL-035": {
    titulo: "Hemorragia cerebelosa",
    imagen: "flujogramas/hematoma-cerebeloso-35-cm-cuarto-ventriculo-cirugia.svg",
    alt: "Flujograma: Hemorragia cerebelosa"
  },
  "CB-041": {
    titulo: "Efectos adversos de las quinolonas",
    imagen: "flujogramas/epilepsia-pielonefritis-levofloxacino-convulsiones.svg",
    alt: "Flujograma: Efectos adversos de las quinolonas"
  },
  "SP-084": {
    titulo: "Comisión por recetar",
    imagen: "flujogramas/visitador-medico-comision-receta-conflicto-interes.svg",
    alt: "Flujograma: Comisión por recetar"
  },
  "PED-125": {
    titulo: "Osteomielitis: germen según el paciente",
    imagen: "flujogramas/osteomielitis-aguda-nino-staphylococcus-aureus.svg",
    alt: "Flujograma: Osteomielitis: germen según el paciente"
  },
  "CIR-062": {
    titulo: "Trauma pancreático",
    imagen: "flujogramas/golpe-timon-fast-negativo-dolor-epigastrico-pancreas.svg",
    alt: "Flujograma: Trauma pancreático"
  },
  "CAR-047": {
    titulo: "Toxicidad por amiodarona",
    imagen: "flujogramas/fa-antiarritmico-5-anos-tos-disnea-amiodarona.svg",
    alt: "Flujograma: Toxicidad por amiodarona"
  },
  "PED-126": {
    titulo: "Neumonía afebril del lactante",
    imagen: "flujogramas/lactante-2-meses-afebril-conjuntivitis-chlamydia.svg",
    alt: "Flujograma: Neumonía afebril del lactante"
  },
  "SP-085": {
    titulo: "Monitoreo fetal y beneficencia",
    imagen: "flujogramas/categoria-iii-meconio-espera-parto-beneficencia.svg",
    alt: "Flujograma: Monitoreo fetal y beneficencia"
  },
  "INF-061": {
    titulo: "Niño contacto de TB",
    imagen: "flujogramas/nino-3-anos-padre-bk-positivo-ppd-8-terapia-preventiva.svg",
    alt: "Flujograma: Niño contacto de TB"
  },
  "GIN-118": {
    titulo: "Antihipertensivos en el embarazo",
    imagen: "flujogramas/enalapril-embarazo-oligohidramnios-ieca.svg",
    alt: "Flujograma: Antihipertensivos en el embarazo"
  },
  "NEF-047": {
    titulo: "Alcalosis metabólica",
    imagen: "flujogramas/tiazida-antiacidos-hco3-32-k-28-alcalosis-metabolica.svg",
    alt: "Flujograma: Alcalosis metabólica"
  },
  "REU-036": {
    titulo: "Dermatitis del pañal",
    imagen: "flujogramas/lactante-panal-placa-brillante-pliegues-econazol.svg",
    alt: "Flujograma: Dermatitis del pañal"
  },
  "CIR-063": {
    titulo: "Colecistitis enfisematosa: gravedad",
    imagen: "flujogramas/murphy-aire-pared-vesicular-colecistitis-enfisematosa.svg",
    alt: "Flujograma: Colecistitis enfisematosa: gravedad"
  },
  "OFT-029": {
    titulo: "Hipema traumático",
    imagen: "flujogramas/golpe-ojo-futbol-nivel-sangre-camara-hipema.svg",
    alt: "Flujograma: Hipema traumático"
  },
  "CIR-064": {
    titulo: "Quemado: superficie corporal",
    imagen: "flujogramas/escaldadura-brazos-tronco-54-scq-sabana-limpia.svg",
    alt: "Flujograma: Quemado: superficie corporal"
  },
  "GIN-119": {
    titulo: "Ganancia de peso en el embarazo",
    imagen: "flujogramas/sobrepeso-ganancia-peso-gestacional-7-115-kg.svg",
    alt: "Flujograma: Ganancia de peso en el embarazo"
  },
  "CB-042": {
    titulo: "Pelagra: las «3 D»",
    imagen: "flujogramas/alcoholico-collar-casal-diarrea-demencia-niacina.svg",
    alt: "Flujograma: Pelagra: las «3 D»"
  },
  "NEF-048": {
    titulo: "Anuria en usuario de sonda vesical",
    imagen: "flujogramas/paraplejico-sonda-anuria-hidronefrosis-cambio-cateter.svg",
    alt: "Flujograma: Anuria en usuario de sonda vesical"
  },
  "GIN-120": {
    titulo: "Acné en el embarazo",
    imagen: "flujogramas/gestante-6-semanas-acne-retinoides-contraindicados.svg",
    alt: "Flujograma: Acné en el embarazo"
  },
  "END-033": {
    titulo: "Poliuria: diabetes insípida",
    imagen: "flujogramas/poliuria-polidipsia-orina-diluida-hipernatremia-diabetes-insipida.svg",
    alt: "Flujograma: Poliuria: diabetes insípida"
  },
  "INF-062": {
    titulo: "Neumonía por Pneumocystis",
    imagen: "flujogramas/vih-pneumocystis-cotrimoxazol.svg",
    alt: "Flujograma: Neumonía por Pneumocystis"
  },
  "GIN-121": {
    titulo: "Choque en mujer con amenorrea",
    imagen: "flujogramas/amenorrea-6-semanas-choque-culdocentesis-ectopico-roto.svg",
    alt: "Flujograma: Choque en mujer con amenorrea"
  },
  "SP-086": {
    titulo: "Niveles de prevención",
    imagen: "flujogramas/autoexamen-mama-prevencion-secundaria.svg",
    alt: "Flujograma: Niveles de prevención"
  },
  "CB-043": {
    titulo: "Nervios del miembro inferior",
    imagen: "flujogramas/pielolitotomia-hipoestesia-muslo-anterior-nervio-femoral.svg",
    alt: "Flujograma: Nervios del miembro inferior"
  },
  "END-034": {
    titulo: "Insuficiencia suprarrenal por ketoconazol",
    imagen: "flujogramas/ketoconazol-hiperpigmentacion-hiponatremia-cortisol-bajo.svg",
    alt: "Flujograma: Insuficiencia suprarrenal por ketoconazol"
  },
  "CAR-048": {
    titulo: "Hemodinamia de los tipos de choque",
    imagen: "flujogramas/infarto-hipotension-iy-crepitantes-precarga-alta.svg",
    alt: "Flujograma: Hemodinamia de los tipos de choque"
  },
  "SP-087": {
    titulo: "Violencia contra la persona adulta mayor",
    imagen: "flujogramas/adulta-mayor-hijo-agresor-amenaza-denuncia.svg",
    alt: "Flujograma: Violencia contra la persona adulta mayor"
  },
  "PED-127": {
    titulo: "Neonato febril",
    imagen: "flujogramas/neonato-febril-puncion-fallida-antibiotico-parenteral.svg",
    alt: "Flujograma: Neonato febril"
  },
  "SP-088": {
    titulo: "Principios de la APS",
    imagen: "flujogramas/escenario-iii-dengue-alcalde-intersectorialidad.svg",
    alt: "Flujograma: Principios de la APS"
  },
  "END-035": {
    titulo: "Tiroides dolorosa con tirotoxicosis",
    imagen: "flujogramas/cervicalgia-post-faringitis-vsg-58-de-quervain.svg",
    alt: "Flujograma: Tiroides dolorosa con tirotoxicosis"
  },
  "PSI-021": {
    titulo: "Trastornos del ánimo en el puerperio",
    imagen: "flujogramas/puerpera-22-dias-tristeza-autolesion-depresion-posparto.svg",
    alt: "Flujograma: Trastornos del ánimo en el puerperio"
  },
  "NEF-049": {
    titulo: "Litiasis vesical: tratamiento",
    imagen: "flujogramas/litiasis-vesical-grande-cistolitotricia-laser.svg",
    alt: "Flujograma: Litiasis vesical: tratamiento"
  },
  "GIN-122": {
    titulo: "Hiperémesis gravídica",
    imagen: "flujogramas/vomitos-incoercibles-cetonuria-hiponatremia-hiperemesis.svg",
    alt: "Flujograma: Hiperémesis gravídica"
  },
  "OFT-030": {
    titulo: "Sangrado al pasar una sonda nasal",
    imagen: "flujogramas/sonda-nasogastrica-sangrado-tabique-anterior-kiesselbach.svg",
    alt: "Flujograma: Sangrado al pasar una sonda nasal"
  },
  "PED-128": {
    titulo: "Otitis media en niño alérgico a amoxicilina",
    imagen: "flujogramas/otitis-media-alergia-leve-amoxicilina-cefdinir.svg",
    alt: "Flujograma: Otitis media en niño alérgico a amoxicilina"
  },
  "TRA-023": {
    titulo: "Fractura de escafoides",
    imagen: "flujogramas/caida-mano-extendida-escafoides-arteria-radial.svg",
    alt: "Flujograma: Fractura de escafoides"
  },
  "NEF-050": {
    titulo: "¿Falla renal aguda o crónica?",
    imagen: "flujogramas/creatinina-5-anemia-8-meses-enfermedad-renal-cronica.svg",
    alt: "Flujograma: ¿Falla renal aguda o crónica?"
  },
  "GAS-046": {
    titulo: "Serología de la hepatitis B",
    imagen: "flujogramas/hbsag-igm-antihbc-positivos-hepatitis-b-aguda.svg",
    alt: "Flujograma: Serología de la hepatitis B"
  },
  "CAR-049": {
    titulo: "Fibrilación auricular inestable",
    imagen: "flujogramas/fa-pa-70-30-dolor-toracico-cardioversion-electrica.svg",
    alt: "Flujograma: Fibrilación auricular inestable"
  },
  "PSI-022": {
    titulo: "Ataque de pánico: criterios",
    imagen: "flujogramas/palpitaciones-ahogo-muerte-inminente-ataque-panico.svg",
    alt: "Flujograma: Ataque de pánico: criterios"
  },
  "NEU-032": {
    titulo: "Tromboembolia pulmonar: Wells",
    imagen: "flujogramas/quimioterapia-disnea-subita-hemoptisis-tromboembolia.svg",
    alt: "Flujograma: Tromboembolia pulmonar: Wells"
  },
  "OFT-031": {
    titulo: "Fármacos para el glaucoma",
    imagen: "flujogramas/glaucoma-betabloqueante-topico-timolol.svg",
    alt: "Flujograma: Fármacos para el glaucoma"
  },
  "NEF-051": {
    titulo: "Glomerulonefritis postestreptocócica",
    imagen: "flujogramas/orina-lavado-carne-amigdalitis-edema-furosemida.svg",
    alt: "Flujograma: Glomerulonefritis postestreptocócica"
  },
  "SP-089": {
    titulo: "Atributos de la atención primaria",
    imagen: "flujogramas/hipertensa-mismo-medico-5-anos-longitudinalidad.svg",
    alt: "Flujograma: Atributos de la atención primaria"
  },
  "GIN-123": {
    titulo: "Bacteriuria asintomática en la gestante",
    imagen: "flujogramas/gestante-8-semanas-bacteriuria-asintomatica-nitrofurantoina.svg",
    alt: "Flujograma: Bacteriuria asintomática en la gestante"
  },
  "CIR-065": {
    titulo: "Tórax inestable",
    imagen: "flujogramas/fracturas-costales-dobles-movimiento-paradojal-intubacion.svg",
    alt: "Flujograma: Tórax inestable"
  },
  "PSI-023": {
    titulo: "Intoxicación por litio",
    imagen: "flujogramas/litio-6-convulsiones-hemodialisis.svg",
    alt: "Flujograma: Intoxicación por litio"
  },
  "SP-090": {
    titulo: "Tipos de causa",
    imagen: "flujogramas/ppd-11-mm-sano-causa-necesaria-no-suficiente.svg",
    alt: "Flujograma: Tipos de causa"
  },
  "GIN-124": {
    titulo: "Feto pequeño: PEG o RCIU",
    imagen: "flujogramas/29-semanas-percentil-8-doppler-umbilical-rciu-temprano.svg",
    alt: "Flujograma: Feto pequeño: PEG o RCIU"
  },
  "NEF-052": {
    titulo: "Falla renal tras automedicación",
    imagen: "flujogramas/ibuprofeno-oliguria-creatinina-3-nefropatia-toxica.svg",
    alt: "Flujograma: Falla renal tras automedicación"
  },
  "TRA-024": {
    titulo: "Complicaciones de la fractura abierta",
    imagen: "flujogramas/fractura-abierta-complicacion-infeccion.svg",
    alt: "Flujograma: Complicaciones de la fractura abierta"
  },
  "GIN-125": {
    titulo: "Bradicardia fetal con meconio espeso",
    imagen: "flujogramas/meconio-espeso-lcf-100-cesarea-emergencia.svg",
    alt: "Flujograma: Bradicardia fetal con meconio espeso"
  },
  "NEU-033": {
    titulo: "Edema pulmonar de altura",
    imagen: "flujogramas/alpinista-esputo-espumoso-sato2-75-oxigeno.svg",
    alt: "Flujograma: Edema pulmonar de altura"
  },
  "CIR-066": {
    titulo: "Tipos de choque en trauma",
    imagen: "flujogramas/motociclista-hipotension-fc-72-sin-sangrado-neurogenico.svg",
    alt: "Flujograma: Tipos de choque en trauma"
  },
  "PED-129": {
    titulo: "Disentería en el niño",
    imagen: "flujogramas/crianza-aves-disenteria-bacilo-curvo-campylobacter-azitromicina.svg",
    alt: "Flujograma: Disentería en el niño"
  },
  "CB-044": {
    titulo: "Respuesta al estrés agudo",
    imagen: "flujogramas/discusion-taquicardia-hipertension-catecolaminas.svg",
    alt: "Flujograma: Respuesta al estrés agudo"
  },
  "NEU-034": {
    titulo: "Tuberculosis: antes de tratar",
    imagen: "flujogramas/tb-bk-positivo-perfil-hepatico-antes-tratamiento.svg",
    alt: "Flujograma: Tuberculosis: antes de tratar"
  },
  "SP-091": {
    titulo: "Tipos de caso en vigilancia",
    imagen: "flujogramas/primer-caso-identificado-servicio-caso-indice.svg",
    alt: "Flujograma: Tipos de caso en vigilancia"
  },
  "OFT-032": {
    titulo: "Reflejo pupilar blanco",
    imagen: "flujogramas/lactante-leucocoria-estrabismo-retinoblastoma.svg",
    alt: "Flujograma: Reflejo pupilar blanco"
  },
  "GIN-126": {
    titulo: "Síndrome HELLP",
    imagen: "flujogramas/pa-160-110-plaquetas-90000-dhl-700-hellp.svg",
    alt: "Flujograma: Síndrome HELLP"
  },
  "INF-063": {
    titulo: "PCP con hipoxemia: corticoides",
    imagen: "flujogramas/vih-cd4-100-pao2-60-pneumocystis-prednisona.svg",
    alt: "Flujograma: PCP con hipoxemia: corticoides"
  },
  "PED-130": {
    titulo: "Vacunas en el lactante con VIH",
    imagen: "flujogramas/lactante-vih-sintomatico-rotavirus-prescripcion.svg",
    alt: "Flujograma: Vacunas en el lactante con VIH"
  },
  "CIR-067": {
    titulo: "Tumor en la base del apéndice",
    imagen: "flujogramas/tumor-base-apendicular-2-cm-mesenterio-hemicolectomia.svg",
    alt: "Flujograma: Tumor en la base del apéndice"
  },
  "PSI-024": {
    titulo: "Efectos extrapiramidales",
    imagen: "flujogramas/haloperidol-no-puede-estar-quieto-acatisia-propranolol.svg",
    alt: "Flujograma: Efectos extrapiramidales"
  },
  "CIR-068": {
    titulo: "Hemorroides internas: grados",
    imagen: "flujogramas/sangrado-defecar-no-prolapsa-coagulacion-infrarroja.svg",
    alt: "Flujograma: Hemorroides internas: grados"
  },
  "END-036": {
    titulo: "Choque refractario: insuficiencia suprarrenal",
    imagen: "flujogramas/choque-septico-refractario-cortisol-bajo-acth-alta.svg",
    alt: "Flujograma: Choque refractario: insuficiencia suprarrenal"
  },
  "CIR-069": {
    titulo: "Fisura anal: tratamiento escalonado",
    imagen: "flujogramas/dolor-intenso-defecar-desgarro-posterior-fisura-anal.svg",
    alt: "Flujograma: Fisura anal: tratamiento escalonado"
  },
  "NRL-036": {
    titulo: "Posturas en el coma",
    imagen: "flujogramas/tec-grave-coma-rigidez-decorticacion-hemisferios.svg",
    alt: "Flujograma: Posturas en el coma"
  },
  "PED-131": {
    titulo: "ITU por E. coli BLEE",
    imagen: "flujogramas/preescolar-itu-ecoli-blee-meropenem.svg",
    alt: "Flujograma: ITU por E. coli BLEE"
  },
  "INF-064": {
    titulo: "Fiebre paroxística de la selva",
    imagen: "flujogramas/selva-fiebre-cuartana-esplenomegalia-malaria.svg",
    alt: "Flujograma: Fiebre paroxística de la selva"
  },
  "CAR-050": {
    titulo: "Pericarditis aguda: criterios",
    imagen: "flujogramas/dolor-pleuritico-alivia-inclinado-frote-pericarditis.svg",
    alt: "Flujograma: Pericarditis aguda: criterios"
  },
  "HEM-023": {
    titulo: "Neutropenia grave",
    imagen: "flujogramas/leucocitos-400-fiebre-aislamiento-inverso.svg",
    alt: "Flujograma: Neutropenia grave"
  },
  "NEF-053": {
    titulo: "Sospecha de cáncer de próstata",
    imagen: "flujogramas/prostata-indurada-psa-8-biopsia-transrectal.svg",
    alt: "Flujograma: Sospecha de cáncer de próstata"
  },
  "CB-045": {
    titulo: "Efectos de la hormona tiroidea",
    imagen: "flujogramas/hipertiroidismo-metabolismo-basal-aumentado.svg",
    alt: "Flujograma: Efectos de la hormona tiroidea"
  },
  "NRL-037": {
    titulo: "Tipos de dolor",
    imagen: "flujogramas/dolor-roce-ropa-electrico-neuropatico.svg",
    alt: "Flujograma: Tipos de dolor"
  },
  "GIN-127": {
    titulo: "Ganancia de peso según IMC",
    imagen: "flujogramas/obesa-imc-32-gano-125-kg-excesiva.svg",
    alt: "Flujograma: Ganancia de peso según IMC"
  },
  "GAS-047": {
    titulo: "Ictericia tras un hematoma",
    imagen: "flujogramas/hematoma-retroperitoneal-bilirrubina-indirecta-reabsorcion.svg",
    alt: "Flujograma: Ictericia tras un hematoma"
  },
  "GIN-128": {
    titulo: "Vacunas en la gestación",
    imagen: "flujogramas/primer-control-vacuna-tdap-27-36-semanas.svg",
    alt: "Flujograma: Vacunas en la gestación"
  },
  "PED-132": {
    titulo: "Displasia broncopulmonar",
    imagen: "flujogramas/displasia-broncopulmonar-hipertension-pulmonar.svg",
    alt: "Flujograma: Displasia broncopulmonar"
  },
  "NEF-054": {
    titulo: "Masa en flanco con historia familiar",
    imagen: "flujogramas/hermano-erc-masa-flanco-creatinina-poliquistosis.svg",
    alt: "Flujograma: Masa en flanco con historia familiar"
  },
  "CB-046": {
    titulo: "Desarrollo del riñón",
    imagen: "flujogramas/agenesia-renal-unilateral-metanefros.svg",
    alt: "Flujograma: Desarrollo del riñón"
  },
  "HEM-024": {
    titulo: "Eritrocitosis: ¿primaria o secundaria?",
    imagen: "flujogramas/hb-186-eritropoyetina-baja-plaquetas-policitemia-vera.svg",
    alt: "Flujograma: Eritrocitosis: ¿primaria o secundaria?"
  },
  "END-037": {
    titulo: "Diabético con acidosis grave",
    imagen: "flujogramas/dm1-lactato-10-cetonas-negativas-acidosis-lactica.svg",
    alt: "Flujograma: Diabético con acidosis grave"
  },
  "NRL-038": {
    titulo: "Distrofia muscular de Duchenne",
    imagen: "flujogramas/duchenne-distrofina-ausente.svg",
    alt: "Flujograma: Distrofia muscular de Duchenne"
  },
  "END-038": {
    titulo: "Metformina: riesgo de acidosis láctica",
    imagen: "flujogramas/metformina-insuficiencia-renal-acidosis-lactica.svg",
    alt: "Flujograma: Metformina: riesgo de acidosis láctica"
  },
  "NEF-055": {
    titulo: "Vasectomía: cuándo es segura",
    imagen: "flujogramas/vasectomia-esterilidad-tres-meses.svg",
    alt: "Flujograma: Vasectomía: cuándo es segura"
  },
  "SP-092": {
    titulo: "Tipos de intervención sanitaria",
    imagen: "flujogramas/colegio-educacion-autocuidado-tuberculosis-promocion.svg",
    alt: "Flujograma: Tipos de intervención sanitaria"
  },
  "GIN-129": {
    titulo: "Fórmula obstétrica",
    imagen: "flujogramas/gemelar-34-ectopico-mola-41-semanas-formula-obstetrica.svg",
    alt: "Flujograma: Fórmula obstétrica"
  },
  "NEF-056": {
    titulo: "Anemia de la ERC con ferropenia",
    imagen: "flujogramas/erc-hemodialisis-ferritina-56-ist-10-hierro-mantener-epo.svg",
    alt: "Flujograma: Anemia de la ERC con ferropenia"
  },
  "PED-133": {
    titulo: "Picadura de escorpión en el niño",
    imagen: "flujogramas/lactante-picadura-escorpion-falla-cardiorrespiratoria.svg",
    alt: "Flujograma: Picadura de escorpión en el niño"
  },
  "GIN-130": {
    titulo: "Progreso del trabajo de parto",
    imagen: "flujogramas/dilatacion-6-a-8-en-2-horas-continuar-trabajo-parto.svg",
    alt: "Flujograma: Progreso del trabajo de parto"
  },
  "PSI-025": {
    titulo: "Ansiedad generalizada: criterios",
    imagen: "flujogramas/preocupacion-12-meses-tension-insomnio-ansiedad-generalizada.svg",
    alt: "Flujograma: Ansiedad generalizada: criterios"
  },
  "GIN-131": {
    titulo: "Sangrado tras la amniotomía",
    imagen: "flujogramas/amniotomia-sangrado-profuso-bradicardia-vasa-previa-cesarea.svg",
    alt: "Flujograma: Sangrado tras la amniotomía"
  },
  "PED-134": {
    titulo: "Membrana hialina y ductus",
    imagen: "flujogramas/prematuro-31-semanas-membrana-hialina-ductus.svg",
    alt: "Flujograma: Membrana hialina y ductus"
  },
  "END-039": {
    titulo: "Insulinoma",
    imagen: "flujogramas/hipoglucemia-insulina-alta-nodulo-pancreatico-reseccion.svg",
    alt: "Flujograma: Insulinoma"
  },
  "SP-093": {
    titulo: "Suplementación en adolescentes",
    imagen: "flujogramas/adolescentes-hb-mayor-12-hierro-acido-folico.svg",
    alt: "Flujograma: Suplementación en adolescentes"
  },
  "NEF-057": {
    titulo: "Nefropatía por contraste",
    imagen: "flujogramas/tc-contraste-diabetico-creatinina-25-hidratacion.svg",
    alt: "Flujograma: Nefropatía por contraste"
  },
  "INF-065": {
    titulo: "Pruebas de VIH y su uso",
    imagen: "flujogramas/vih-inicio-tar-respuesta-carga-viral.svg",
    alt: "Flujograma: Pruebas de VIH y su uso"
  },
  "NEU-035": {
    titulo: "Soporte ventilatorio en EPOC",
    imagen: "flujogramas/epoc-ph-732-pco2-60-ventilacion-no-invasiva.svg",
    alt: "Flujograma: Soporte ventilatorio en EPOC"
  },
  "PSI-026": {
    titulo: "Toxíndrome por cocaína",
    imagen: "flujogramas/agitacion-paranoia-midriasis-tabique-perforado-cocaina.svg",
    alt: "Flujograma: Toxíndrome por cocaína"
  },
  "CIR-070": {
    titulo: "Quemadura eléctrica",
    imagen: "flujogramas/alto-voltaje-mano-ruidos-arritmicos-ecg.svg",
    alt: "Flujograma: Quemadura eléctrica"
  },
  "NEF-058": {
    titulo: "Litiasis ureteral según tamaño",
    imagen: "flujogramas/calculo-ureteral-distal-menor-6-mm-terapia-expulsiva.svg",
    alt: "Flujograma: Litiasis ureteral según tamaño"
  },
  "INF-066": {
    titulo: "Profilaxis antitetánica",
    imagen: "flujogramas/herida-fierro-oxidado-vacuna-9-anos-toxoide.svg",
    alt: "Flujograma: Profilaxis antitetánica"
  },
  "PED-135": {
    titulo: "Contacto piel a piel",
    imagen: "flujogramas/parto-vaginal-contacto-piel-a-piel-primera-hora.svg",
    alt: "Flujograma: Contacto piel a piel"
  },
  "HEM-025": {
    titulo: "PTI en el niño",
    imagen: "flujogramas/nino-gingivorragia-plaquetas-12000-inmunoglobulina.svg",
    alt: "Flujograma: PTI en el niño"
  },
  "CB-047": {
    titulo: "Intoxicación crónica por plomo",
    imagen: "flujogramas/reciclador-baterias-cefalea-diarrea-plomo.svg",
    alt: "Flujograma: Intoxicación crónica por plomo"
  },
  "CIR-071": {
    titulo: "Profundidad de la quemadura",
    imagen: "flujogramas/agua-caliente-ampollas-blanquea-espesor-parcial-superficial.svg",
    alt: "Flujograma: Profundidad de la quemadura"
  },
  "CB-048": {
    titulo: "Toxíndrome anticolinérgico",
    imagen: "flujogramas/organofosforado-atropina-piel-seca-midriasis-anticolinergico.svg",
    alt: "Flujograma: Toxíndrome anticolinérgico"
  },
  "SP-094": {
    titulo: "Tipos de medicina no convencional",
    imagen: "flujogramas/oncologia-acupuntura-medicina-complementaria.svg",
    alt: "Flujograma: Tipos de medicina no convencional"
  },
  "CIR-072": {
    titulo: "Neumotórax a tensión",
    imagen: "flujogramas/hiperresonancia-desviacion-traqueal-hipotension-aguja.svg",
    alt: "Flujograma: Neumotórax a tensión"
  },
  "REU-037": {
    titulo: "Dermatitis atópica: criterios",
    imagen: "flujogramas/prurito-pliegues-asma-piel-seca-dermatitis-atopica.svg",
    alt: "Flujograma: Dermatitis atópica: criterios"
  },
  "NEF-059": {
    titulo: "Cistitis: ¿complicada?",
    imagen: "flujogramas/mujer-joven-disuria-sin-fiebre-cistitis-no-complicada.svg",
    alt: "Flujograma: Cistitis: ¿complicada?"
  },
  "END-040": {
    titulo: "Galactorrea y amenorrea",
    imagen: "flujogramas/galactorrea-amenorrea-hiperprolactinemia.svg",
    alt: "Flujograma: Galactorrea y amenorrea"
  },
  "CB-049": {
    titulo: "Arácnidos venenosos del Perú",
    imagen: "flujogramas/nino-dolor-muslo-espasmos-diaforesis-latrodectus.svg",
    alt: "Flujograma: Arácnidos venenosos del Perú"
  },
  "GIN-132": {
    titulo: "Doppler obstétrico",
    imagen: "flujogramas/incompatibilidad-rh-anemia-fetal-cerebral-media.svg",
    alt: "Flujograma: Doppler obstétrico"
  },
  "NEF-060": {
    titulo: "Compensación renal en la hipoperfusión",
    imagen: "flujogramas/neumonia-hipotension-fena-04-vasoconstriccion-eferente.svg",
    alt: "Flujograma: Compensación renal en la hipoperfusión"
  },
  "REU-038": {
    titulo: "Fibromialgia: fármaco a agregar",
    imagen: "flujogramas/fibromialgia-insomnio-persistente-amitriptilina.svg",
    alt: "Flujograma: Fibromialgia: fármaco a agregar"
  },
  "NEU-036": {
    titulo: "Apnea obstructiva del sueño",
    imagen: "flujogramas/ronca-apneas-imc-35-acv-polisomnografia.svg",
    alt: "Flujograma: Apnea obstructiva del sueño"
  },
  "CIR-073": {
    titulo: "Infección necrotizante del periné",
    imagen: "flujogramas/diabetico-perine-escroto-necrosis-crepitacion-fournier.svg",
    alt: "Flujograma: Infección necrotizante del periné"
  },
  "GIN-133": {
    titulo: "Lactancia en madre con VIH",
    imagen: "flujogramas/puerpera-vih-tar-desea-lactar-contraindicar.svg",
    alt: "Flujograma: Lactancia en madre con VIH"
  },
  "GIN-134": {
    titulo: "Presentación podálica en trabajo de parto",
    imagen: "flujogramas/podalica-primigesta-talla-150-trabajo-parto-cesarea.svg",
    alt: "Flujograma: Presentación podálica en trabajo de parto"
  },
  "SP-095": {
    titulo: "Tendencias en el tiempo",
    imagen: "flujogramas/neumonia-meses-frios-variacion-estacional.svg",
    alt: "Flujograma: Tendencias en el tiempo"
  },
  "TRA-025": {
    titulo: "Complicaciones de la fractura de cadera",
    imagen: "flujogramas/anciano-fractura-cadera-postrado-tvp.svg",
    alt: "Flujograma: Complicaciones de la fractura de cadera"
  },
  "GIN-135": {
    titulo: "Placenta y orificio cervical",
    imagen: "flujogramas/borde-placentario-1-cm-oci-implantacion-baja.svg",
    alt: "Flujograma: Placenta y orificio cervical"
  },
  "NEF-061": {
    titulo: "PSA en zona gris",
    imagen: "flujogramas/psa-59-libre-total-11-biopsia.svg",
    alt: "Flujograma: PSA en zona gris"
  },
  "GAS-048": {
    titulo: "Disacaridasas intestinales",
    imagen: "flujogramas/lacteos-distension-diarrea-lactasa.svg",
    alt: "Flujograma: Disacaridasas intestinales"
  },
  "INF-067": {
    titulo: "Fiebre amarilla: fases",
    imagen: "flujogramas/satipo-fiebre-amarilla-ictericia-gravedad.svg",
    alt: "Flujograma: Fiebre amarilla: fases"
  },
  "PED-136": {
    titulo: "Varicela con sobreinfección",
    imagen: "flujogramas/varicela-placa-fluctuante-sobreinfeccion-oxacilina.svg",
    alt: "Flujograma: Varicela con sobreinfección"
  },
  "SP-096": {
    titulo: "Tipos de error en la medición",
    imagen: "flujogramas/balanzas-descalibradas-sobreestiman-peso-error-sistematico.svg",
    alt: "Flujograma: Tipos de error en la medición"
  },
  "INF-068": {
    titulo: "Síndrome de reconstitución inmune",
    imagen: "flujogramas/vih-tar-3-semanas-fiebre-adenopatias-reconstitucion-inmune.svg",
    alt: "Flujograma: Síndrome de reconstitución inmune"
  },
  "NEU-037": {
    titulo: "Neumonía: CURB-65",
    imagen: "flujogramas/neumonia-69-anos-fr-32-curb65-2-hospitalizar.svg",
    alt: "Flujograma: Neumonía: CURB-65"
  },
  "TRA-026": {
    titulo: "Nervios de la pierna",
    imagen: "flujogramas/herida-compartimento-anterior-pie-caido-peroneo.svg",
    alt: "Flujograma: Nervios de la pierna"
  },
  "GIN-136": {
    titulo: "Síndrome antifosfolípido",
    imagen: "flujogramas/tres-abortos-tvp-anti-b2-glicoproteina.svg",
    alt: "Flujograma: Síndrome antifosfolípido"
  },
  "GIN-137": {
    titulo: "Síndrome de ovario poliquístico",
    imagen: "flujogramas/oligomenorrea-acne-acantosis-hirsutismo-ovario-poliquistico.svg",
    alt: "Flujograma: Síndrome de ovario poliquístico"
  },
  "PED-137": {
    titulo: "Lactante prematuro dependiente de oxígeno",
    imagen: "flujogramas/prematuro-27-semanas-oxigeno-3-meses-displasia.svg",
    alt: "Flujograma: Lactante prematuro dependiente de oxígeno"
  },
  "HEM-026": {
    titulo: "Síndrome de Down: riesgos",
    imagen: "flujogramas/nino-cromosomopatia-leucemia-sindrome-down.svg",
    alt: "Flujograma: Síndrome de Down: riesgos"
  },
  "REU-039": {
    titulo: "Úlcera crónica del labio",
    imagen: "flujogramas/obrero-ulcera-labio-inferior-infiltrada-espinocelular.svg",
    alt: "Flujograma: Úlcera crónica del labio"
  },
  "CIR-074": {
    titulo: "Herida abdominal por arma blanca",
    imagen: "flujogramas/arma-blanca-periumbilical-estable-exploracion-local.svg",
    alt: "Flujograma: Herida abdominal por arma blanca"
  },
  "PED-138": {
    titulo: "Virus respiratorios en el niño",
    imagen: "flujogramas/tos-perruna-signo-campanario-parainfluenza.svg",
    alt: "Flujograma: Virus respiratorios en el niño"
  },
  "SP-097": {
    titulo: "Tipos de culpa médica",
    imagen: "flujogramas/internista-omite-interconsulta-negligencia.svg",
    alt: "Flujograma: Tipos de culpa médica"
  },
  "PSI-027": {
    titulo: "Complicaciones de la anorexia",
    imagen: "flujogramas/anorexia-adolescente-qt-largo.svg",
    alt: "Flujograma: Complicaciones de la anorexia"
  },
  "GIN-138": {
    titulo: "Esterilización en portadora de BRCA",
    imagen: "flujogramas/brca-paridad-satisfecha-salpinguectomia-bilateral.svg",
    alt: "Flujograma: Esterilización en portadora de BRCA"
  },
  "INF-069": {
    titulo: "Diarrea del viajero",
    imagen: "flujogramas/viaje-agua-no-embotellada-diarrea-acuosa-hidratacion.svg",
    alt: "Flujograma: Diarrea del viajero"
  },
  "PED-139": {
    titulo: "Empiema en el niño",
    imagen: "flujogramas/neumonia-fiebre-persistente-toracocentesis-pus-tubo-fibrinoliticos.svg",
    alt: "Flujograma: Empiema en el niño"
  },
  "NRL-039": {
    titulo: "Ictus isquémico a las 6 horas",
    imagen: "flujogramas/hemiparesia-afasia-6-horas-trombectomia.svg",
    alt: "Flujograma: Ictus isquémico a las 6 horas"
  },
  "GIN-139": {
    titulo: "Hemorragia posparto refractaria",
    imagen: "flujogramas/hemorragia-posparto-atonia-refractaria-balon.svg",
    alt: "Flujograma: Hemorragia posparto refractaria"
  },
  "NEU-038": {
    titulo: "Neumonía con derrame pleural",
    imagen: "flujogramas/neumonia-derrame-pleural-toracocentesis.svg",
    alt: "Flujograma: Neumonía con derrame pleural"
  },
  "CAR-051": {
    titulo: "HTA no controlada: siguiente paso",
    imagen: "flujogramas/losartan-hctz-pa-150-90-amlodipino.svg",
    alt: "Flujograma: HTA no controlada: siguiente paso"
  },
  "PED-140": {
    titulo: "Fiebre sin foco en el lactante",
    imagen: "flujogramas/lactante-fimosis-fiebre-3-dias-urocultivo.svg",
    alt: "Flujograma: Fiebre sin foco en el lactante"
  },
  "CIR-075": {
    titulo: "Mordedura humana en el puño",
    imagen: "flujogramas/punetazo-boca-nudillo-tendon-capsula-lavado-quirurgico.svg",
    alt: "Flujograma: Mordedura humana en el puño"
  },
  "GIN-140": {
    titulo: "Seguimiento tras NIC 3",
    imagen: "flujogramas/cono-nic3-seguir-tamizaje-20-anos.svg",
    alt: "Flujograma: Seguimiento tras NIC 3"
  },
  "CB-050": {
    titulo: "Periodos del desarrollo",
    imagen: "flujogramas/semanas-2-a-8-organogenesis-periodo-embrionario.svg",
    alt: "Flujograma: Periodos del desarrollo"
  },
  "PED-141": {
    titulo: "Pérdida de peso en el neonato",
    imagen: "flujogramas/neonato-48-h-pezones-planos-perdida-peso-hipernatremia.svg",
    alt: "Flujograma: Pérdida de peso en el neonato"
  },
  "CIR-076": {
    titulo: "Quemaduras: grado y manejo",
    imagen: "flujogramas/agua-hirviendo-manos-eritema-sin-ampollas-analgesia.svg",
    alt: "Flujograma: Quemaduras: grado y manejo"
  },
  "TRA-027": {
    titulo: "Pie plano en el niño",
    imagen: "flujogramas/escolar-pie-plano-flexible-sin-dolor-no-tratar.svg",
    alt: "Flujograma: Pie plano en el niño"
  },
  "CIR-077": {
    titulo: "Grado de las hemorroides",
    imagen: "flujogramas/prolapso-hemorroidal-reduccion-manual-tercer-grado.svg",
    alt: "Flujograma: Grado de las hemorroides"
  },
  "CIR-078": {
    titulo: "Anestesia en paciente de alto riesgo",
    imagen: "flujogramas/epoc-coronario-fractura-radio-bloqueo-periferico.svg",
    alt: "Flujograma: Anestesia en paciente de alto riesgo"
  },
  "GAS-049": {
    titulo: "Cirrosis: Child-Pugh",
    imagen: "flujogramas/hepatitis-c-ascitis-albumina-24-inr-17-cirrosis-descompensada.svg",
    alt: "Flujograma: Cirrosis: Child-Pugh"
  },
  "SP-098": {
    titulo: "Análisis FODA",
    imagen: "flujogramas/foda-baja-calidad-sin-recursos-debilidades.svg",
    alt: "Flujograma: Análisis FODA"
  },
  "PED-142": {
    titulo: "Retinopatía del prematuro",
    imagen: "flujogramas/prematuro-28-semanas-rop-saturacion-90-95.svg",
    alt: "Flujograma: Retinopatía del prematuro"
  },
  "GAS-050": {
    titulo: "Hematemesis tras vómitos",
    imagen: "flujogramas/vomitos-alcohol-hematemesis-mallory-weiss.svg",
    alt: "Flujograma: Hematemesis tras vómitos"
  },
  "HEM-027": {
    titulo: "Pronóstico en leucemia mieloide aguda",
    imagen: "flujogramas/lma-pronostico-citogenetica.svg",
    alt: "Flujograma: Pronóstico en leucemia mieloide aguda"
  },
  "CIR-079": {
    titulo: "Respuesta metabólica al gran quemado",
    imagen: "flujogramas/quemado-50-taquicardia-fiebre-catabolismo-hipermetabolismo.svg",
    alt: "Flujograma: Respuesta metabólica al gran quemado"
  },
  "GAS-051": {
    titulo: "Sospecha de cáncer colorrectal",
    imagen: "flujogramas/anciano-perdida-peso-hematoquecia-anemia-colonoscopia.svg",
    alt: "Flujograma: Sospecha de cáncer colorrectal"
  },
  "PSI-028": {
    titulo: "Anorexia nerviosa: criterios",
    imagen: "flujogramas/adolescente-miedo-engordar-distorsion-restriccion-anorexia.svg",
    alt: "Flujograma: Anorexia nerviosa: criterios"
  },
  "SP-099": {
    titulo: "Modelos de intervención en salud",
    imagen: "flujogramas/parasitosis-sin-saneamiento-solo-medicamento-biomedico.svg",
    alt: "Flujograma: Modelos de intervención en salud"
  },
  "SP-100": {
    titulo: "Atención a víctima de violencia sexual",
    imagen: "flujogramas/victima-violencia-sexual-atencion-medica-primero.svg",
    alt: "Flujograma: Atención a víctima de violencia sexual"
  },
  "INF-070": {
    titulo: "Mordedura de perro",
    imagen: "flujogramas/mordedura-perro-mano-desgarrante-lavado.svg",
    alt: "Flujograma: Mordedura de perro"
  },
  "CB-051": {
    titulo: "Toxíndrome simpaticomimético",
    imagen: "flujogramas/discoteca-agitacion-diaforesis-midriasis-benzodiacepinas.svg",
    alt: "Flujograma: Toxíndrome simpaticomimético"
  },
  "SP-101": {
    titulo: "Muestreo sistemático",
    imagen: "flujogramas/uno-de-cada-3-inicio-azar-muestreo-sistematico.svg",
    alt: "Flujograma: Muestreo sistemático"
  },
  "TRA-028": {
    titulo: "Osteoporosis: ¿pedir densitometría?",
    imagen: "flujogramas/fractura-vertebral-caida-menopausia-precoz-densitometria.svg",
    alt: "Flujograma: Osteoporosis: ¿pedir densitometría?"
  },
  "INF-071": {
    titulo: "Neurosífilis",
    imagen: "flujogramas/vih-rpr-lcr-vdrl-neurosifilis-penicilina-g-sodica.svg",
    alt: "Flujograma: Neurosífilis"
  },
  "CIR-080": {
    titulo: "Diverticulitis complicada",
    imagen: "flujogramas/diverticulitis-absceso-pericolico-5-cm-drenaje-percutaneo.svg",
    alt: "Flujograma: Diverticulitis complicada"
  },
  "CIR-081": {
    titulo: "Neumoperitoneo",
    imagen: "flujogramas/anciano-dolor-distension-neumoperitoneo-laparotomia.svg",
    alt: "Flujograma: Neumoperitoneo"
  },
  "SP-102": {
    titulo: "Partes del protocolo de investigación",
    imagen: "flujogramas/protocolo-sustento-hipotesis-marco-teorico.svg",
    alt: "Flujograma: Partes del protocolo de investigación"
  },
  "PSI-029": {
    titulo: "Uso de los ISRS",
    imagen: "flujogramas/isrs-depresion-retiro-gradual.svg",
    alt: "Flujograma: Uso de los ISRS"
  },
  "TRA-029": {
    titulo: "Gonartrosis: criterios",
    imagen: "flujogramas/rodillas-crepitacion-rigidez-breve-gonartrosis.svg",
    alt: "Flujograma: Gonartrosis: criterios"
  },
  "SP-103": {
    titulo: "Documentos de gestión",
    imagen: "flujogramas/documento-estructura-organica-funciones-rof.svg",
    alt: "Flujograma: Documentos de gestión"
  },
  "CB-052": {
    titulo: "Toxicidad de la quimioterapia",
    imagen: "flujogramas/antraciclinas-cardiotoxicidad.svg",
    alt: "Flujograma: Toxicidad de la quimioterapia"
  },
  "NEF-062": {
    titulo: "Síntomas prostáticos: primer paso",
    imagen: "flujogramas/chorro-debil-esfuerzo-miccional-tacto-rectal.svg",
    alt: "Flujograma: Síntomas prostáticos: primer paso"
  },
  "GIN-141": {
    titulo: "Tipos de vaginitis",
    imagen: "flujogramas/flujo-maloliente-cervix-petequial-tricomonas.svg",
    alt: "Flujograma: Tipos de vaginitis"
  },
  "INF-072": {
    titulo: "Úlcera crónica de la selva",
    imagen: "flujogramas/loreto-ulcera-indolora-bordes-indurados-leishmaniasis.svg",
    alt: "Flujograma: Úlcera crónica de la selva"
  },
  "GIN-142": {
    titulo: "Causas de hemorragia posparto",
    imagen: "flujogramas/falta-cotiledon-sangrado-revision-uterina.svg",
    alt: "Flujograma: Causas de hemorragia posparto"
  },
  "CAR-052": {
    titulo: "Disnea con tos rosada",
    imagen: "flujogramas/hipertensa-tos-rosada-crepitantes-edema-agudo-pulmon.svg",
    alt: "Flujograma: Disnea con tos rosada"
  },
  "NEF-063": {
    titulo: "Síndrome nefrótico con disnea súbita",
    imagen: "flujogramas/nefrotico-membranosa-albumina-18-disnea-tep.svg",
    alt: "Flujograma: Síndrome nefrótico con disnea súbita"
  },
  "INF-073": {
    titulo: "Meningitis: LCR y tratamiento",
    imagen: "flujogramas/lcr-linfocitos-glucosa-normal-meningitis-viral.svg",
    alt: "Flujograma: Meningitis: LCR y tratamiento"
  },
  "TRA-030": {
    titulo: "Nervios de la mano",
    imagen: "flujogramas/trauma-muneca-4-5-dedo-canal-guyon.svg",
    alt: "Flujograma: Nervios de la mano"
  },
  "SP-104": {
    titulo: "Tasa de ataque",
    imagen: "flujogramas/comedor-200-comensales-80-enfermos-tasa-ataque.svg",
    alt: "Flujograma: Tasa de ataque"
  },
  "SP-105": {
    titulo: "Redes Integradas de Salud",
    imagen: "flujogramas/conjunto-organizaciones-articulacion-redes-integradas.svg",
    alt: "Flujograma: Redes Integradas de Salud"
  },
  "END-041": {
    titulo: "Obesidad infantil y acantosis",
    imagen: "flujogramas/adolescente-imc-3-de-acantosis-resistencia-insulina.svg",
    alt: "Flujograma: Obesidad infantil y acantosis"
  },
  "CIR-082": {
    titulo: "Íleo posoperatorio",
    imagen: "flujogramas/posoperatorio-dia-3-distension-sin-rha-opioides.svg",
    alt: "Flujograma: Íleo posoperatorio"
  },
  "GAS-052": {
    titulo: "Marcadores tumorales",
    imagen: "flujogramas/adenocarcinoma-pancreas-ca-19-9.svg",
    alt: "Flujograma: Marcadores tumorales"
  },
  "CIR-083": {
    titulo: "Dolor en FID tras apendicectomía",
    imagen: "flujogramas/apendicectomia-previa-dolor-fid-munon-inflamado.svg",
    alt: "Flujograma: Dolor en FID tras apendicectomía"
  },
  "INF-074": {
    titulo: "Herpes genital: diagnóstico",
    imagen: "flujogramas/vesiculas-labio-mayor-herpes-genital-pcr-lesion.svg",
    alt: "Flujograma: Herpes genital: diagnóstico"
  },
  "NEF-064": {
    titulo: "Nervios pélvicos y función sexual",
    imagen: "flujogramas/prostatectomia-radical-preservar-nervios-cavernosos.svg",
    alt: "Flujograma: Nervios pélvicos y función sexual"
  },
  "END-042": {
    titulo: "Nefropatía diabética: detección precoz",
    imagen: "flujogramas/dm2-10-anos-cociente-albumina-creatinina.svg",
    alt: "Flujograma: Nefropatía diabética: detección precoz"
  },
  "CB-053": {
    titulo: "Paso por la barrera hematoencefálica",
    imagen: "flujogramas/anestesico-liposoluble-barrera-hematoencefalica.svg",
    alt: "Flujograma: Paso por la barrera hematoencefálica"
  },
  "GAS-053": {
    titulo: "Hipoxemia en la pancreatitis",
    imagen: "flujogramas/pancreatitis-disnea-hipoxemia-alteracion-vq.svg",
    alt: "Flujograma: Hipoxemia en la pancreatitis"
  },
  "INF-075": {
    titulo: "Esofagitis en SIDA",
    imagen: "flujogramas/sida-cd4-30-ulceras-esofagicas-inclusiones-cmv-ganciclovir.svg",
    alt: "Flujograma: Esofagitis en SIDA"
  },
  "NEU-039": {
    titulo: "Sospecha de TB en la gestante",
    imagen: "flujogramas/gestante-tos-perdida-peso-abuela-tos-tuberculosis.svg",
    alt: "Flujograma: Sospecha de TB en la gestante"
  },
  "GIN-143": {
    titulo: "Oxitocina e hipertonía uterina",
    imagen: "flujogramas/bolo-oxitocina-bradicardia-fetal-hipertonia.svg",
    alt: "Flujograma: Oxitocina e hipertonía uterina"
  },
  "HEM-028": {
    titulo: "Trastornos de la hemostasia primaria",
    imagen: "flujogramas/sangrado-mucocutaneo-ristocetina-baja-von-willebrand.svg",
    alt: "Flujograma: Trastornos de la hemostasia primaria"
  },
  "CIR-084": {
    titulo: "Apendicectomía laparoscópica",
    imagen: "flujogramas/apendicitis-obesa-laparoscopia-menos-infeccion-herida.svg",
    alt: "Flujograma: Apendicectomía laparoscópica"
  },
  "CIR-085": {
    titulo: "Tumoración supraumbilical",
    imagen: "flujogramas/tumoracion-supraumbilical-reductible-hernia-epigastrica.svg",
    alt: "Flujograma: Tumoración supraumbilical"
  },
  "INF-076": {
    titulo: "Amebiasis intestinal",
    imagen: "flujogramas/trofozoitos-entamoeba-metronidazol-paromomicina.svg",
    alt: "Flujograma: Amebiasis intestinal"
  },
  "GIN-144": {
    titulo: "Mecanismo del parto",
    imagen: "flujogramas/salida-cabeza-rotacion-externa.svg",
    alt: "Flujograma: Mecanismo del parto"
  },
  "NRL-040": {
    titulo: "Migraña: criterios",
    imagen: "flujogramas/cefalea-hemicraneal-pulsatil-48-h-fotofobia-migrana.svg",
    alt: "Flujograma: Migraña: criterios"
  },
  "SP-106": {
    titulo: "Prevención de la leptospirosis",
    imagen: "flujogramas/leptospirosis-rural-calzado-agua-segura.svg",
    alt: "Flujograma: Prevención de la leptospirosis"
  },
  "NEU-040": {
    titulo: "Gravedad de la crisis asmática",
    imagen: "flujogramas/habla-entrecortada-sato2-93-pef-66-crisis-moderada.svg",
    alt: "Flujograma: Gravedad de la crisis asmática"
  },
  "PSI-030": {
    titulo: "Síntomas de embarazo sin gestación",
    imagen: "flujogramas/amenorrea-sintomas-embarazo-hcg-negativa-pseudociesis.svg",
    alt: "Flujograma: Síntomas de embarazo sin gestación"
  },
  "REU-040": {
    titulo: "Tumores de piel de la cara",
    imagen: "flujogramas/nodulo-perlado-telangiectasias-cara-basocelular.svg",
    alt: "Flujograma: Tumores de piel de la cara"
  },
  "SP-107": {
    titulo: "Jerarquía de controles",
    imagen: "flujogramas/formaldehido-planta-alimentos-eliminar-fuente.svg",
    alt: "Flujograma: Jerarquía de controles"
  },
  "SP-108": {
    titulo: "Medicinas no convencionales",
    imagen: "flujogramas/similitud-diluciones-homeopatia.svg",
    alt: "Flujograma: Medicinas no convencionales"
  },
  "PED-143": {
    titulo: "Convulsiones neonatales",
    imagen: "flujogramas/rn-bradicardia-fetal-convulsion-2-horas-fenobarbital.svg",
    alt: "Flujograma: Convulsiones neonatales"
  },
  "NEF-065": {
    titulo: "HBP: tratamiento escalonado",
    imagen: "flujogramas/anciano-sintomas-prostaticos-alfa-bloqueante.svg",
    alt: "Flujograma: HBP: tratamiento escalonado"
  },
  "OFT-033": {
    titulo: "Glaucoma agudo de ángulo cerrado",
    imagen: "flujogramas/dolor-ocular-halos-midriasis-media-acetazolamida.svg",
    alt: "Flujograma: Glaucoma agudo de ángulo cerrado"
  },
  "REU-041": {
    titulo: "Impétigo: tratamiento",
    imagen: "flujogramas/costras-mielicericas-boca-antebrazos-mupirocina.svg",
    alt: "Flujograma: Impétigo: tratamiento"
  },
  "NRL-041": {
    titulo: "Hematomas intracraneales",
    imagen: "flujogramas/caida-escaleras-intervalo-lucido-midriasis-epidural.svg",
    alt: "Flujograma: Hematomas intracraneales"
  },
  "CIR-086": {
    titulo: "Colecistitis aguda: criterios de Tokio",
    imagen: "flujogramas/litiasis-dolor-hcd-fiebre-masa-colecistitis.svg",
    alt: "Flujograma: Colecistitis aguda: criterios de Tokio"
  },
  "INF-077": {
    titulo: "Mononucleosis infecciosa",
    imagen: "flujogramas/adolescente-amigdalas-exudativas-hepatoesplenomegalia-mononucleosis.svg",
    alt: "Flujograma: Mononucleosis infecciosa"
  },
  "TRA-031": {
    titulo: "Nervios en las fracturas de húmero",
    imagen: "flujogramas/fractura-tercio-medio-humero-mano-pendula-radial.svg",
    alt: "Flujograma: Nervios en las fracturas de húmero"
  },
  "NEF-066": {
    titulo: "Torsión testicular",
    imagen: "flujogramas/adolescente-dolor-testicular-subito-testiculo-alto-torsion.svg",
    alt: "Flujograma: Torsión testicular"
  },
  "REU-042": {
    titulo: "Artritis reumatoide: criterios",
    imagen: "flujogramas/poliartritis-simetrica-manos-rigidez-anti-ccp.svg",
    alt: "Flujograma: Artritis reumatoide: criterios"
  },
  "PED-144": {
    titulo: "Dificultad respiratoria del prematuro",
    imagen: "flujogramas/prematuro-32-semanas-quejido-broncograma-membrana-hialina.svg",
    alt: "Flujograma: Dificultad respiratoria del prematuro"
  },
  "GAS-054": {
    titulo: "Colangitis aguda",
    imagen: "flujogramas/fiebre-ictericia-dolor-coledoco-15-mm-colangitis.svg",
    alt: "Flujograma: Colangitis aguda"
  },
  "REU-043": {
    titulo: "Anafilaxia por picadura de abejas",
    imagen: "flujogramas/picadura-abejas-estridor-hipotension-adrenalina.svg",
    alt: "Flujograma: Anafilaxia por picadura de abejas"
  },
  "GIN-145": {
    titulo: "Pielonefritis en la gestante",
    imagen: "flujogramas/gestante-28-semanas-fiebre-puno-percusion-ceftriaxona.svg",
    alt: "Flujograma: Pielonefritis en la gestante"
  },
  "TRA-032": {
    titulo: "Síndrome compartimental",
    imagen: "flujogramas/aplastamiento-dolor-refractario-palidez-sin-pulso-compartimental.svg",
    alt: "Flujograma: Síndrome compartimental"
  },
  "CB-054": {
    titulo: "Intoxicaciones y antídotos",
    imagen: "flujogramas/discoteca-trago-flumazenilo-despierta-benzodiacepina.svg",
    alt: "Flujograma: Intoxicaciones y antídotos"
  },
  "PED-145": {
    titulo: "Estenosis hipertrófica del píloro",
    imagen: "flujogramas/neonato-10-dias-vomitos-explosivos-oliva-ecografia.svg",
    alt: "Flujograma: Estenosis hipertrófica del píloro"
  },
  "PED-146": {
    titulo: "Atresia esofágica",
    imagen: "flujogramas/rn-tos-asfixia-lactar-sonda-enrollada-atresia-esofagica.svg",
    alt: "Flujograma: Atresia esofágica"
  },
  "PED-147": {
    titulo: "Exantema vesicular en el niño",
    imagen: "flujogramas/vesiculas-costras-papulas-distintos-estadios-varicela.svg",
    alt: "Flujograma: Exantema vesicular en el niño"
  },
  "PED-148": {
    titulo: "Rinorrea en el preescolar",
    imagen: "flujogramas/preescolar-rinorrea-afebril-faringe-normal-resfrio-comun.svg",
    alt: "Flujograma: Rinorrea en el preescolar"
  }
};
