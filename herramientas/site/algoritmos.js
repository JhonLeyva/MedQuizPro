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
  },
  "HEM-029": {
    titulo: "Sangrado con tiempos prolongados en la sepsis",
    imagen: "flujogramas/sepsis-biliar-sangrado-fibrinogeno-bajo-cid.svg",
    alt: "Flujograma: Sangrado con tiempos prolongados en la sepsis"
  },
  "GIN-146": {
    titulo: "Cesárea previa y trabajo de parto",
    imagen: "flujogramas/cesarea-corporal-previa-trabajo-parto-sangrado.svg",
    alt: "Flujograma: Cesárea previa y trabajo de parto"
  },
  "INF-078": {
    titulo: "Meningitis en el paciente con VIH",
    imagen: "flujogramas/vih-cefalea-subaguda-rigidez-tinta-china.svg",
    alt: "Flujograma: Meningitis en el paciente con VIH"
  },
  "END-043": {
    titulo: "Insuficiencia suprarrenal primaria",
    imagen: "flujogramas/hiperpigmentacion-hipotension-hiperkalemia-addison.svg",
    alt: "Flujograma: Insuficiencia suprarrenal primaria"
  },
  "TRA-033": {
    titulo: "Trauma cervical: primer paso",
    imagen: "flujogramas/trauma-cervical-alto-inmovilizar-collarin.svg",
    alt: "Flujograma: Trauma cervical: primer paso"
  },
  "SP-109": {
    titulo: "Promoción de la salud",
    imagen: "flujogramas/distrito-desnutricion-accion-comunitaria.svg",
    alt: "Flujograma: Promoción de la salud"
  },
  "SP-110": {
    titulo: "Errores en la prueba de hipótesis",
    imagen: "flujogramas/rechazar-hipotesis-nula-verdadera-error-alfa.svg",
    alt: "Flujograma: Errores en la prueba de hipótesis"
  },
  "NEF-067": {
    titulo: "Oliguria: ¿prerrenal o renal?",
    imagen: "flujogramas/diarrea-oliguria-fena-bajo-reto-fluidos.svg",
    alt: "Flujograma: Oliguria: ¿prerrenal o renal?"
  },
  "REU-044": {
    titulo: "Dolor lumbar inflamatorio",
    imagen: "flujogramas/dolor-gluteo-nocturno-schober-espondiloartritis.svg",
    alt: "Flujograma: Dolor lumbar inflamatorio"
  },
  "SP-111": {
    titulo: "Bocio endémico en la sierra",
    imagen: "flujogramas/bocio-difuso-huancavelica-sal-yodada.svg",
    alt: "Flujograma: Bocio endémico en la sierra"
  },
  "CB-055": {
    titulo: "Déficit de vitaminas en el alcohólico",
    imagen: "flujogramas/alcoholico-gingivorragia-petequias-escorbuto.svg",
    alt: "Flujograma: Déficit de vitaminas en el alcohólico"
  },
  "CAR-053": {
    titulo: "Riesgo cardiovascular y LDL",
    imagen: "flujogramas/coronario-diabetico-ldl-120-estatina.svg",
    alt: "Flujograma: Riesgo cardiovascular y LDL"
  },
  "END-044": {
    titulo: "Dieta en la hipertrigliceridemia",
    imagen: "flujogramas/trigliceridos-400-dieta-pescado-azul.svg",
    alt: "Flujograma: Dieta en la hipertrigliceridemia"
  },
  "SP-112": {
    titulo: "Tipos de variables",
    imagen: "flujogramas/musica-de-fondo-analgesicos-variables.svg",
    alt: "Flujograma: Tipos de variables"
  },
  "SP-113": {
    titulo: "Qué mide cada análisis",
    imagen: "flujogramas/insomnio-covid-analisis-correlacion.svg",
    alt: "Flujograma: Qué mide cada análisis"
  },
  "CB-056": {
    titulo: "Mordedura o picadura en el campo",
    imagen: "flujogramas/dolor-lanceta-rigidez-abdominal-sudoracion-latrodectismo.svg",
    alt: "Flujograma: Mordedura o picadura en el campo"
  },
  "HEM-030": {
    titulo: "Anemia en la gestante",
    imagen: "flujogramas/gestante-hb-8-microcitica-reticulocitos-bajos.svg",
    alt: "Flujograma: Anemia en la gestante"
  },
  "SP-114": {
    titulo: "¿Es enfermedad profesional?",
    imagen: "flujogramas/personal-salud-enfermedad-profesional-biologica.svg",
    alt: "Flujograma: ¿Es enfermedad profesional?"
  },
  "GIN-147": {
    titulo: "Parto gemelar: ¿vaginal o cesárea?",
    imagen: "flujogramas/embarazo-gemelar-termino-presentacion-via-parto.svg",
    alt: "Flujograma: Parto gemelar: ¿vaginal o cesárea?"
  },
  "GIN-148": {
    titulo: "Corioamnionitis: qué dar y qué no",
    imagen: "flujogramas/fiebre-31-semanas-taquicardia-fetal-no-tocolisis.svg",
    alt: "Flujograma: Corioamnionitis: qué dar y qué no"
  },
  "GIN-149": {
    titulo: "Fases del trabajo de parto",
    imagen: "flujogramas/primigesta-3-cm-fase-latente-deambular.svg",
    alt: "Flujograma: Fases del trabajo de parto"
  },
  "END-045": {
    titulo: "Hipoglucemia: gravedad",
    imagen: "flujogramas/insulina-glucosa-38-desorientado-dextrosa-33.svg",
    alt: "Flujograma: Hipoglucemia: gravedad"
  },
  "GIN-150": {
    titulo: "Obesidad y embarazo",
    imagen: "flujogramas/obesidad-pregestacional-diabetes-macrosomia.svg",
    alt: "Flujograma: Obesidad y embarazo"
  },
  "GIN-151": {
    titulo: "Anticoncepción en el lupus",
    imagen: "flujogramas/lupus-antifosfolipidos-anticoncepcion-diu-cobre.svg",
    alt: "Flujograma: Anticoncepción en el lupus"
  },
  "CB-057": {
    titulo: "Receptores del gusto",
    imagen: "flujogramas/covid-perdida-gusto-celulas-neuroepiteliales.svg",
    alt: "Flujograma: Receptores del gusto"
  },
  "NRL-042": {
    titulo: "Placa neuromuscular: dónde falla",
    imagen: "flujogramas/ptosis-diplopia-placa-mioneural-receptor-acetilcolina.svg",
    alt: "Flujograma: Placa neuromuscular: dónde falla"
  },
  "GIN-152": {
    titulo: "Antihipertensivos en el embarazo",
    imagen: "flujogramas/hta-cronica-gestante-captopril-metildopa.svg",
    alt: "Flujograma: Antihipertensivos en el embarazo"
  },
  "GIN-153": {
    titulo: "Riesgos del embarazo adolescente",
    imagen: "flujogramas/gestante-16-anos-riesgo-menor-diabetes.svg",
    alt: "Flujograma: Riesgos del embarazo adolescente"
  },
  "CIR-087": {
    titulo: "Enfermedad arterial periférica",
    imagen: "flujogramas/dolor-pantorrillas-al-caminar-cede-reposo-claudicacion.svg",
    alt: "Flujograma: Enfermedad arterial periférica"
  },
  "NEF-068": {
    titulo: "Cáncer de próstata localizado",
    imagen: "flujogramas/psa-11-gleason-bajo-localizado-prostatectomia.svg",
    alt: "Flujograma: Cáncer de próstata localizado"
  },
  "CIR-088": {
    titulo: "Hernia estrangulada que se reduce",
    imagen: "flujogramas/hernia-crural-estrangulada-reducida-anestesia-laparotomia.svg",
    alt: "Flujograma: Hernia estrangulada que se reduce"
  },
  "CIR-089": {
    titulo: "Trauma torácico penetrante con choque",
    imagen: "flujogramas/herida-precordial-triada-beck-taponamiento.svg",
    alt: "Flujograma: Trauma torácico penetrante con choque"
  },
  "NRL-043": {
    titulo: "Hemorragia de fosa posterior",
    imagen: "flujogramas/hemorragia-fosa-posterior-compresion-tronco.svg",
    alt: "Flujograma: Hemorragia de fosa posterior"
  },
  "CB-058": {
    titulo: "Coma tóxico en una adolescente",
    imagen: "flujogramas/coma-bradipnea-flumazenilo-ineficaz-barbituricos.svg",
    alt: "Flujograma: Coma tóxico en una adolescente"
  },
  "NEU-041": {
    titulo: "Disnea súbita en el hospitalizado",
    imagen: "flujogramas/hospitalizado-disnea-subita-hipoxemia-rx-normal-tep.svg",
    alt: "Flujograma: Disnea súbita en el hospitalizado"
  },
  "CAR-054": {
    titulo: "Hipertensión en el joven",
    imagen: "flujogramas/hta-brazos-pulso-femoral-debil-coartacion.svg",
    alt: "Flujograma: Hipertensión en el joven"
  },
  "HEM-031": {
    titulo: "Pierna hinchada tras estar en cama",
    imagen: "flujogramas/encamada-2-semanas-pierna-edematosa-tvp.svg",
    alt: "Flujograma: Pierna hinchada tras estar en cama"
  },
  "CAR-055": {
    titulo: "Tos seca en el hipertenso",
    imagen: "flujogramas/hipertenso-captopril-tos-seca-retirar-ieca.svg",
    alt: "Flujograma: Tos seca en el hipertenso"
  },
  "HEM-032": {
    titulo: "Pancitopenia: qué preguntar",
    imagen: "flujogramas/pancitopenia-fiebre-equimosis-farmacos-mielotoxicos.svg",
    alt: "Flujograma: Pancitopenia: qué preguntar"
  },
  "CAR-056": {
    titulo: "Fiebre, soplo y déficit neurológico",
    imagen: "flujogramas/fiebre-2-meses-soplo-mitral-hemiparesia-endocarditis.svg",
    alt: "Flujograma: Fiebre, soplo y déficit neurológico"
  },
  "INF-079": {
    titulo: "Fiebre y adenopatías: ¿cómo se contagió?",
    imagen: "flujogramas/odinofagia-adenopatias-linfocitos-atipicos-mononucleosis.svg",
    alt: "Flujograma: Fiebre y adenopatías: ¿cómo se contagió?"
  },
  "GAS-055": {
    titulo: "De reflujo a cáncer",
    imagen: "flujogramas/metaplasia-intestinal-esofago-distal-adenocarcinoma.svg",
    alt: "Flujograma: De reflujo a cáncer"
  },
  "NEU-042": {
    titulo: "TEP: ¿qué examen pedir?",
    imagen: "flujogramas/postictus-disnea-subita-dimero-d-angiotem.svg",
    alt: "Flujograma: TEP: ¿qué examen pedir?"
  },
  "PED-149": {
    titulo: "Tuberculosis: qué muestra la Rx",
    imagen: "flujogramas/nino-contacto-tb-estridor-adenopatias-hiliares.svg",
    alt: "Flujograma: Tuberculosis: qué muestra la Rx"
  },
  "NEU-043": {
    titulo: "Neumotórax: ¿qué lo causó?",
    imagen: "flujogramas/joven-sano-disnea-subita-tubo-aire-bullas.svg",
    alt: "Flujograma: Neumotórax: ¿qué lo causó?"
  },
  "INF-080": {
    titulo: "Larvas en heces y esputo",
    imagen: "flujogramas/htlv1-diarrea-tos-larvas-rabditoides-estrongiloidosis.svg",
    alt: "Flujograma: Larvas en heces y esputo"
  },
  "INF-081": {
    titulo: "Leptospirosis: gravedad",
    imagen: "flujogramas/campesino-ictericia-sufusion-conjuntival-penicilina.svg",
    alt: "Flujograma: Leptospirosis: gravedad"
  },
  "INF-082": {
    titulo: "Ojo hinchado en un niño del sur",
    imagen: "flujogramas/edema-bipalpebral-unilateral-romana-chagas.svg",
    alt: "Flujograma: Ojo hinchado en un niño del sur"
  },
  "SP-115": {
    titulo: "Medir discapacidad prematura",
    imagen: "flujogramas/discapacidad-prematura-carga-enfermedad-avad.svg",
    alt: "Flujograma: Medir discapacidad prematura"
  },
  "PED-150": {
    titulo: "BCG sin cicatriz",
    imagen: "flujogramas/lactante-sin-cicatriz-bcg-no-revacunar.svg",
    alt: "Flujograma: BCG sin cicatriz"
  },
  "PED-151": {
    titulo: "Fiebre en el niño hospitalizado",
    imagen: "flujogramas/nina-pci-sonda-vesical-fiebre-urocultivo.svg",
    alt: "Flujograma: Fiebre en el niño hospitalizado"
  },
  "SP-116": {
    titulo: "Vigilancia del sarampión",
    imagen: "flujogramas/viajero-exantema-igm-sarampion-importado.svg",
    alt: "Flujograma: Vigilancia del sarampión"
  },
  "PED-152": {
    titulo: "Hipoglucemia neonatal",
    imagen: "flujogramas/prematuro-34-sem-glucosa-40-tremores-bolo-ev.svg",
    alt: "Flujograma: Hipoglucemia neonatal"
  },
  "GIN-154": {
    titulo: "Suplementos en el embarazo",
    imagen: "flujogramas/gestante-calcio-desde-20-semanas.svg",
    alt: "Flujograma: Suplementos en el embarazo"
  },
  "PED-153": {
    titulo: "Controles de CRED",
    imagen: "flujogramas/cred-primer-ano-controles-mensuales.svg",
    alt: "Flujograma: Controles de CRED"
  },
  "SP-117": {
    titulo: "Medidas de frecuencia y asociación",
    imagen: "flujogramas/45-casos-nuevos-1000-personas-incidencia.svg",
    alt: "Flujograma: Medidas de frecuencia y asociación"
  },
  "CB-059": {
    titulo: "Tipos de inmunidad",
    imagen: "flujogramas/vacuna-induce-inmunidad-activa-artificial.svg",
    alt: "Flujograma: Tipos de inmunidad"
  },
  "SP-118": {
    titulo: "Mecanismos de transmisión",
    imagen: "flujogramas/agua-hospital-pseudomonas-transmision-vehiculo.svg",
    alt: "Flujograma: Mecanismos de transmisión"
  },
  "SP-119": {
    titulo: "Acreditación de establecimientos",
    imagen: "flujogramas/acreditacion-evaluacion-personal-propio-autoevaluacion.svg",
    alt: "Flujograma: Acreditación de establecimientos"
  },
  "REU-045": {
    titulo: "Escabiosis: tratamiento por edad",
    imagen: "flujogramas/lactante-surcos-prurito-palmas-plantas-permetrina.svg",
    alt: "Flujograma: Escabiosis: tratamiento por edad"
  },
  "NEU-044": {
    titulo: "Factores de muerte por asma",
    imagen: "flujogramas/asma-mortalidad-resistencia-corticoides.svg",
    alt: "Flujograma: Factores de muerte por asma"
  },
  "REU-046": {
    titulo: "Ampollas en el lactante",
    imagen: "flujogramas/lactante-fiebre-ampollas-flacidas-nikolsky-ritter.svg",
    alt: "Flujograma: Ampollas en el lactante"
  },
  "REU-047": {
    titulo: "Uña engrosada del pie",
    imagen: "flujogramas/deportista-una-blanquecina-engrosada-onicomicosis.svg",
    alt: "Flujograma: Uña engrosada del pie"
  },
  "OFT-034": {
    titulo: "Reflejo pupilar ausente en un niño",
    imagen: "flujogramas/nino-2-anos-estrabismo-sin-reflejo-retinoblastoma.svg",
    alt: "Flujograma: Reflejo pupilar ausente en un niño"
  },
  "SP-120": {
    titulo: "¿Qué hace falta para un brote de dengue?",
    imagen: "flujogramas/brote-dengue-susceptibles-enfermo-mosquito.svg",
    alt: "Flujograma: ¿Qué hace falta para un brote de dengue?"
  },
  "PED-154": {
    titulo: "Complicaciones del prematuro",
    imagen: "flujogramas/rn-muy-bajo-peso-complicacion-inmediata-respiratoria.svg",
    alt: "Flujograma: Complicaciones del prematuro"
  },
  "PED-155": {
    titulo: "Sospecha de sepsis neonatal",
    imagen: "flujogramas/rn-rpm-18-horas-fiebre-succion-debil-hemocultivo.svg",
    alt: "Flujograma: Sospecha de sepsis neonatal"
  },
  "TRA-034": {
    titulo: "Actitud de la pierna tras una caída",
    imagen: "flujogramas/anciana-caida-pierna-acortada-rotacion-externa-cadera.svg",
    alt: "Flujograma: Actitud de la pierna tras una caída"
  },
  "CIR-090": {
    titulo: "Choque obstructivo en el trauma",
    imagen: "flujogramas/trauma-hipotension-yugulares-timpanismo-neumotorax-tension.svg",
    alt: "Flujograma: Choque obstructivo en el trauma"
  },
  "CIR-091": {
    titulo: "Choque hemorrágico",
    imagen: "flujogramas/trauma-abdominal-choque-no-responde-sangre-o-negativo.svg",
    alt: "Flujograma: Choque hemorrágico"
  },
  "CAR-057": {
    titulo: "Ritmo en el paro cardiaco",
    imagen: "flujogramas/rcp-monitor-fibrilacion-ventricular-desfibrilar.svg",
    alt: "Flujograma: Ritmo en el paro cardiaco"
  },
  "GIN-155": {
    titulo: "Dilatación sin contracciones",
    imagen: "flujogramas/18-semanas-dilatacion-sin-contracciones-incompetencia-cervical.svg",
    alt: "Flujograma: Dilatación sin contracciones"
  },
  "NEU-045": {
    titulo: "Antituberculosos en el embarazo",
    imagen: "flujogramas/gestante-tuberculosis-estreptomicina-ototoxica.svg",
    alt: "Flujograma: Antituberculosos en el embarazo"
  },
  "GIN-156": {
    titulo: "Profilaxis anti-D después del parto",
    imagen: "flujogramas/madre-rh-negativo-rn-rh-negativo-sin-anti-d.svg",
    alt: "Flujograma: Profilaxis anti-D después del parto"
  },
  "GIN-157": {
    titulo: "Embarazo prolongado: ¿inducir o madurar?",
    imagen: "flujogramas/embarazo-42-semanas-bishop-4-misoprostol.svg",
    alt: "Flujograma: Embarazo prolongado: ¿inducir o madurar?"
  },
  "GIN-158": {
    titulo: "Fórmula obstétrica",
    imagen: "flujogramas/formula-obstetrica-aborto-ectopico-g4p1021.svg",
    alt: "Flujograma: Fórmula obstétrica"
  },
  "REU-048": {
    titulo: "Artritis séptica: qué se ve en el Gram",
    imagen: "flujogramas/mujer-joven-leucorrea-artritis-diplococos-gram-negativos.svg",
    alt: "Flujograma: Artritis séptica: qué se ve en el Gram"
  },
  "REU-049": {
    titulo: "Enfermedad multisistémica en la mujer joven",
    imagen: "flujogramas/eritema-malar-derrame-cilindros-plaquetopenia-lupus.svg",
    alt: "Flujograma: Enfermedad multisistémica en la mujer joven"
  },
  "END-046": {
    titulo: "Hipertiroidismo en el embarazo",
    imagen: "flujogramas/gestante-10-semanas-graves-propiltiouracilo.svg",
    alt: "Flujograma: Hipertiroidismo en el embarazo"
  },
  "END-047": {
    titulo: "Tirotoxicosis: ¿qué la causa?",
    imagen: "flujogramas/cuello-doloroso-postviral-tiroiditis-subaguda-aine.svg",
    alt: "Flujograma: Tirotoxicosis: ¿qué la causa?"
  },
  "END-048": {
    titulo: "Diabetes tipo 2 descompensada",
    imagen: "flujogramas/hba1c-9-5-glucosa-450-creatinina-alta-insulina.svg",
    alt: "Flujograma: Diabetes tipo 2 descompensada"
  },
  "NRL-044": {
    titulo: "Síndromes lobares",
    imagen: "flujogramas/desinhibicion-euforia-descuido-sindrome-prefrontal.svg",
    alt: "Flujograma: Síndromes lobares"
  },
  "NRL-045": {
    titulo: "Cefaleas primarias",
    imagen: "flujogramas/cefalea-en-banda-semanal-cede-aine-tensional.svg",
    alt: "Flujograma: Cefaleas primarias"
  },
  "NRL-046": {
    titulo: "Déficit súbito con TC normal",
    imagen: "flujogramas/fibrilacion-auricular-afasia-hemiparesia-tac-normal.svg",
    alt: "Flujograma: Déficit súbito con TC normal"
  },
  "REU-050": {
    titulo: "Placas descamativas",
    imagen: "flujogramas/placas-escamas-nacaradas-una-en-dedal-psoriasis.svg",
    alt: "Flujograma: Placas descamativas"
  },
  "PED-156": {
    titulo: "Faringitis: ¿bacteriana?",
    imagen: "flujogramas/escolar-amigdalas-pus-petequias-paladar-estreptococo.svg",
    alt: "Flujograma: Faringitis: ¿bacteriana?"
  },
  "SP-121": {
    titulo: "¿Qué es la variable dependiente?",
    imagen: "flujogramas/experimento-variable-dependiente-se-observan-cambios.svg",
    alt: "Flujograma: ¿Qué es la variable dependiente?"
  },
  "PSI-031": {
    titulo: "Abstinencia alcohólica en el hospital",
    imagen: "flujogramas/postoperado-alucinaciones-zoopsias-temblor-delirium-tremens.svg",
    alt: "Flujograma: Abstinencia alcohólica en el hospital"
  },
  "REU-051": {
    titulo: "Reacción alérgica en la piel",
    imagen: "flujogramas/preescolar-citricos-habones-urticaria-aguda.svg",
    alt: "Flujograma: Reacción alérgica en la piel"
  },
  "GIN-159": {
    titulo: "Antibiótico en la endometritis puerperal",
    imagen: "flujogramas/puerpera-endometritis-clindamicina-gentamicina.svg",
    alt: "Flujograma: Antibiótico en la endometritis puerperal"
  },
  "REU-052": {
    titulo: "Vesículas que dejan costras amarillas",
    imagen: "flujogramas/vesiculas-rascado-costras-mielicericas-impetigo.svg",
    alt: "Flujograma: Vesículas que dejan costras amarillas"
  },
  "GIN-160": {
    titulo: "Nutrientes en el embarazo",
    imagen: "flujogramas/gestante-aumentar-proteinas-necesidad-materno-fetal.svg",
    alt: "Flujograma: Nutrientes en el embarazo"
  },
  "OFT-035": {
    titulo: "Dolor de garganta con trismus",
    imagen: "flujogramas/odinofagia-trismus-otalgia-absceso-periamigdalino.svg",
    alt: "Flujograma: Dolor de garganta con trismus"
  },
  "CIR-092": {
    titulo: "Superficie corporal quemada",
    imagen: "flujogramas/escaldadura-brazos-tronco-anterior-36-por-ciento.svg",
    alt: "Flujograma: Superficie corporal quemada"
  },
  "GAS-056": {
    titulo: "Falla hepática aguda",
    imagen: "flujogramas/ictericia-flapping-sangrado-hipoglucemia-falla-hepatica-aguda.svg",
    alt: "Flujograma: Falla hepática aguda"
  },
  "GAS-057": {
    titulo: "Tipos de shock",
    imagen: "flujogramas/melena-hematemesis-hipotension-shock-hipovolemico.svg",
    alt: "Flujograma: Tipos de shock"
  },
  "CB-060": {
    titulo: "Células del alvéolo",
    imagen: "flujogramas/covid-hipoxemia-neumocito-tipo-ii-ace2.svg",
    alt: "Flujograma: Células del alvéolo"
  },
  "NEF-069": {
    titulo: "Criptorquidia: evolución",
    imagen: "flujogramas/criptorquidia-bilateral-no-tratada-azoospermia.svg",
    alt: "Flujograma: Criptorquidia: evolución"
  },
  "GIN-161": {
    titulo: "Hipertensión en la gestante",
    imagen: "flujogramas/primigesta-37-sem-pa-140-proteinuria-preeclampsia.svg",
    alt: "Flujograma: Hipertensión en la gestante"
  },
  "GIN-162": {
    titulo: "Atención de la violencia sexual",
    imagen: "flujogramas/agresion-sexual-profilaxis-gonorrea-chlamydia.svg",
    alt: "Flujograma: Atención de la violencia sexual"
  },
  "PED-157": {
    titulo: "Recién nacido que no elimina meconio",
    imagen: "flujogramas/rn-distension-sin-meconio-fistula-uretral-ano-imperforado.svg",
    alt: "Flujograma: Recién nacido que no elimina meconio"
  },
  "CIR-093": {
    titulo: "Fontaine: del síntoma a la necrosis",
    imagen: "flujogramas/diabetica-claudicacion-necrosis-quinto-dedo-fontaine-iv.svg",
    alt: "Flujograma: Fontaine: del síntoma a la necrosis"
  },
  "OFT-036": {
    titulo: "Conjuntivitis: tipo y tratamiento",
    imagen: "flujogramas/conjuntivitis-folicular-papilar-otalgia-chlamydia-doxiciclina.svg",
    alt: "Flujograma: Conjuntivitis: tipo y tratamiento"
  },
  "CIR-094": {
    titulo: "Escroto agudo",
    imagen: "flujogramas/adolescente-dolor-escrotal-subito-detorsion-orquidopexia.svg",
    alt: "Flujograma: Escroto agudo"
  },
  "CIR-095": {
    titulo: "Trauma abdominal penetrante",
    imagen: "flujogramas/herida-bala-mesogastrio-taquicardia-laparotomia.svg",
    alt: "Flujograma: Trauma abdominal penetrante"
  },
  "GAS-058": {
    titulo: "¿A dónde metastatiza cada cáncer?",
    imagen: "flujogramas/cancer-colorrectal-metastasis-higado-via-portal.svg",
    alt: "Flujograma: ¿A dónde metastatiza cada cáncer?"
  },
  "OFT-037": {
    titulo: "Trauma ocular cerrado",
    imagen: "flujogramas/golpe-ocular-pupila-deformada-hifema-proteger-derivar.svg",
    alt: "Flujograma: Trauma ocular cerrado"
  },
  "CB-061": {
    titulo: "Toxíndromes y antídotos",
    imagen: "flujogramas/agricultor-sialorrea-bradicardia-fasciculaciones-atropina.svg",
    alt: "Flujograma: Toxíndromes y antídotos"
  },
  "CAR-058": {
    titulo: "Infarto con hipotensión",
    imagen: "flujogramas/st-elevado-v2-v6-hipotension-shock-cardiogenico.svg",
    alt: "Flujograma: Infarto con hipotensión"
  },
  "INF-083": {
    titulo: "Micosis invasiva facial",
    imagen: "flujogramas/diabetica-escara-necrotica-destruccion-maxilar-mucormicosis.svg",
    alt: "Flujograma: Micosis invasiva facial"
  },
  "CAR-059": {
    titulo: "Insuficiencia cardiaca congestiva",
    imagen: "flujogramas/ortopnea-edema-crepitantes-insuficiencia-cardiaca-furosemida.svg",
    alt: "Flujograma: Insuficiencia cardiaca congestiva"
  },
  "PED-158": {
    titulo: "Hitos del desarrollo a los 6 meses",
    imagen: "flujogramas/lactante-6-meses-se-sienta-balbucea-no-gatea-normal.svg",
    alt: "Flujograma: Hitos del desarrollo a los 6 meses"
  },
  "GIN-163": {
    titulo: "Desgarros perineales",
    imagen: "flujogramas/macrosomico-desgarro-hasta-esfinter-anal-tercer-grado.svg",
    alt: "Flujograma: Desgarros perineales"
  },
  "PED-159": {
    titulo: "Shock por deshidratación",
    imagen: "flujogramas/nino-diarrea-llenado-capilar-lento-hipotension-bolo-20.svg",
    alt: "Flujograma: Shock por deshidratación"
  },
  "PED-160": {
    titulo: "Ombligo que no cicatriza",
    imagen: "flujogramas/neonato-tejido-carnoso-umbilical-nitrato-plata.svg",
    alt: "Flujograma: Ombligo que no cicatriza"
  },
  "TRA-035": {
    titulo: "Revisión primaria del trauma",
    imagen: "flujogramas/politrauma-coma-sato2-84-oxigenoterapia.svg",
    alt: "Flujograma: Revisión primaria del trauma"
  },
  "PED-161": {
    titulo: "Dosis de dextrosa en el neonato",
    imagen: "flujogramas/neonato-3900-g-glucosa-40-dextrosa-8-ml.svg",
    alt: "Flujograma: Dosis de dextrosa en el neonato"
  },
  "PED-162": {
    titulo: "Hemograma según el germen",
    imagen: "flujogramas/neonato-rpm-fiebre-infiltrado-leucocitosis-neutrofilia.svg",
    alt: "Flujograma: Hemograma según el germen"
  },
  "SP-122": {
    titulo: "Las 4C de las ITS",
    imagen: "flujogramas/manejo-its-cuatro-c-no-calidad.svg",
    alt: "Flujograma: Las 4C de las ITS"
  },
  "OFT-038": {
    titulo: "Cuerpo extraño en el oído",
    imagen: "flujogramas/nino-pila-boton-oido-extraccion-pinza.svg",
    alt: "Flujograma: Cuerpo extraño en el oído"
  },
  "SP-123": {
    titulo: "¿Qué indicador responde a cada pregunta?",
    imagen: "flujogramas/hipertenso-fumador-probabilidad-5-anos-incidencia-acumulada.svg",
    alt: "Flujograma: ¿Qué indicador responde a cada pregunta?"
  },
  "SP-124": {
    titulo: "Ciclo vital familiar",
    imagen: "flujogramas/hijos-dejan-hogar-ciclo-vital-dispersion.svg",
    alt: "Flujograma: Ciclo vital familiar"
  },
  "SP-125": {
    titulo: "Valoración integral por etapa de vida",
    imagen: "flujogramas/valoracion-cognitiva-afectiva-sociofamiliar-adulto-mayor.svg",
    alt: "Flujograma: Valoración integral por etapa de vida"
  },
  "PED-163": {
    titulo: "Cardiopatías acianóticas",
    imagen: "flujogramas/prematuro-cardiopatia-acianotica-ductus-permeable.svg",
    alt: "Flujograma: Cardiopatías acianóticas"
  },
  "END-049": {
    titulo: "Tirotoxicosis grave en la gestante",
    imagen: "flujogramas/gestante-fiebre-taquicardia-150-confusa-tormenta-tiroidea.svg",
    alt: "Flujograma: Tirotoxicosis grave en la gestante"
  },
  "PED-164": {
    titulo: "Del evento hipóxico a la secuela",
    imagen: "flujogramas/rn-apgar-bajo-ph-7-deficit-base-asfixia.svg",
    alt: "Flujograma: Del evento hipóxico a la secuela"
  },
  "GAS-059": {
    titulo: "Ictericia obstructiva con baja de peso",
    imagen: "flujogramas/fumador-ictericia-acolia-masa-epigastrica-ca199-pancreas.svg",
    alt: "Flujograma: Ictericia obstructiva con baja de peso"
  },
  "PED-165": {
    titulo: "Diarrea acuosa en el lactante",
    imagen: "flujogramas/lactante-diarrea-acuosa-explosiva-ecet.svg",
    alt: "Flujograma: Diarrea acuosa en el lactante"
  },
  "PED-166": {
    titulo: "Atención integral del niño",
    imagen: "flujogramas/intervencion-individual-potenciar-desarrollo-estimulacion-temprana.svg",
    alt: "Flujograma: Atención integral del niño"
  },
  "NEF-070": {
    titulo: "Marcadores del cáncer de testículo",
    imagen: "flujogramas/tumor-testicular-no-seminoma-alfafetoproteina.svg",
    alt: "Flujograma: Marcadores del cáncer de testículo"
  },
  "NEF-071": {
    titulo: "Síndrome nefrítico en el niño",
    imagen: "flujogramas/nino-impetigo-previo-hematuria-edema-c3-bajo-gnpe.svg",
    alt: "Flujograma: Síndrome nefrítico en el niño"
  },
  "PED-167": {
    titulo: "¿Qué urocultivo confirma la ITU?",
    imagen: "flujogramas/nina-fiebre-dolor-flanco-disuria-urocultivo.svg",
    alt: "Flujograma: ¿Qué urocultivo confirma la ITU?"
  },
  "TRA-036": {
    titulo: "Politraumatizado con Glasgow 10",
    imagen: "flujogramas/atropello-glasgow-10-via-aerea-proteccion-cervical.svg",
    alt: "Flujograma: Politraumatizado con Glasgow 10"
  },
  "PSI-032": {
    titulo: "Atracones y purgas",
    imagen: "flujogramas/atracones-purgas-compensatorias-bulimia.svg",
    alt: "Flujograma: Atracones y purgas"
  },
  "END-050": {
    titulo: "Debilidad tras yodo radiactivo",
    imagen: "flujogramas/yodo-radiactivo-debilidad-cpk-alta-hipotiroidismo.svg",
    alt: "Flujograma: Debilidad tras yodo radiactivo"
  },
  "PSI-033": {
    titulo: "Crisis convulsiva tras una discusión",
    imagen: "flujogramas/adolescente-discusion-opistotonos-crisis-psicogena.svg",
    alt: "Flujograma: Crisis convulsiva tras una discusión"
  },
  "GAS-060": {
    titulo: "Pancreatitis crónica con signos de alarma",
    imagen: "flujogramas/pancreatitis-cronica-baja-peso-dolor-tomografia.svg",
    alt: "Flujograma: Pancreatitis crónica con signos de alarma"
  },
  "NEU-046": {
    titulo: "¿Cuándo ventilar?",
    imagen: "flujogramas/maratonista-altura-deterioro-hipercapnia-ventilacion.svg",
    alt: "Flujograma: ¿Cuándo ventilar?"
  },
  "CAR-060": {
    titulo: "Paro en la emergencia",
    imagen: "flujogramas/paro-intrahospitalario-soporte-basico-monitor-desfibrilador.svg",
    alt: "Flujograma: Paro en la emergencia"
  },
  "NEU-047": {
    titulo: "Asma y hora del día",
    imagen: "flujogramas/asma-ritmo-circadiano-crisis-madrugada.svg",
    alt: "Flujograma: Asma y hora del día"
  },
  "INF-084": {
    titulo: "Fiebre en el dengue: qué dar",
    imagen: "flujogramas/gestante-fiebre-retroocular-tumbes-dengue-paracetamol.svg",
    alt: "Flujograma: Fiebre en el dengue: qué dar"
  },
  "INF-085": {
    titulo: "Infección odontógena que progresa",
    imagen: "flujogramas/diabetica-celulitis-facial-odontogena-vancomicina-clindamicina.svg",
    alt: "Flujograma: Infección odontógena que progresa"
  },
  "NEU-048": {
    titulo: "Reacciones adversas a antituberculosos",
    imagen: "flujogramas/tbc-pleural-podagra-acido-urico-retirar-pirazinamida.svg",
    alt: "Flujograma: Reacciones adversas a antituberculosos"
  },
  "NEU-049": {
    titulo: "Derrame pleural linfocítico",
    imagen: "flujogramas/derrame-linfocitico-exudado-joven-ada-tuberculosis.svg",
    alt: "Flujograma: Derrame pleural linfocítico"
  },
  "CAR-061": {
    titulo: "¿De qué muere el infartado y cuándo?",
    imagen: "flujogramas/infarto-muerte-prehospitalaria-fibrilacion-ventricular.svg",
    alt: "Flujograma: ¿De qué muere el infartado y cuándo?"
  },
  "HEM-033": {
    titulo: "Neutropenia grave",
    imagen: "flujogramas/neutropenia-menor-500-causa-farmacologica.svg",
    alt: "Flujograma: Neutropenia grave"
  },
  "NEU-050": {
    titulo: "EPOC en una mujer que no fuma",
    imagen: "flujogramas/viuda-esposo-fumador-epoc-tabaquismo-pasivo.svg",
    alt: "Flujograma: EPOC en una mujer que no fuma"
  },
  "NEU-051": {
    titulo: "Complicaciones de la neumonía nosocomial",
    imagen: "flujogramas/neumonia-nosocomial-complicacion-insuficiencia-respiratoria.svg",
    alt: "Flujograma: Complicaciones de la neumonía nosocomial"
  },
  "PED-168": {
    titulo: "Meningitis neonatal: el Gram orienta",
    imagen: "flujogramas/neonato-meningitis-bacilos-gram-positivos-listeria.svg",
    alt: "Flujograma: Meningitis neonatal: el Gram orienta"
  },
  "PED-169": {
    titulo: "Diarrea con sangre en el lactante",
    imagen: "flujogramas/lactante-disenteria-deshidratado-somnoliento-ceftriaxona.svg",
    alt: "Flujograma: Diarrea con sangre en el lactante"
  },
  "PED-170": {
    titulo: "Ictericia con bilirrubina directa alta",
    imagen: "flujogramas/rn-2-dias-ictericia-bilirrubina-directa-leucopenia-sepsis.svg",
    alt: "Flujograma: Ictericia con bilirrubina directa alta"
  },
  "PED-171": {
    titulo: "Dificultad respiratoria del recién nacido",
    imagen: "flujogramas/prematuro-33-sem-quejido-aleteo-silverman-8.svg",
    alt: "Flujograma: Dificultad respiratoria del recién nacido"
  },
  "SP-126": {
    titulo: "Cirugía urgente sin familiares",
    imagen: "flujogramas/nino-hematoma-epidural-sin-familia-jefe-guardia-autoriza.svg",
    alt: "Flujograma: Cirugía urgente sin familiares"
  },
  "PED-172": {
    titulo: "Etapas de la tos ferina",
    imagen: "flujogramas/lactante-no-vacunado-tos-paroxistica-gallo-tos-ferina.svg",
    alt: "Flujograma: Etapas de la tos ferina"
  },
  "PSI-034": {
    titulo: "Riesgo suicida en el adolescente",
    imagen: "flujogramas/adolescente-bipolar-riesgo-suicida-agresion-sexual.svg",
    alt: "Flujograma: Riesgo suicida en el adolescente"
  },
  "NEF-072": {
    titulo: "Dolor cólico con hematuria en un niño",
    imagen: "flujogramas/nino-colico-hematuria-sin-fiebre-litiasis.svg",
    alt: "Flujograma: Dolor cólico con hematuria en un niño"
  },
  "REU-053": {
    titulo: "Pediculosis: plan de tratamiento",
    imagen: "flujogramas/escolar-liendres-hermano-prurito-permetrina.svg",
    alt: "Flujograma: Pediculosis: plan de tratamiento"
  },
  "PED-173": {
    titulo: "Grupos de estreptococos",
    imagen: "flujogramas/escolar-faringitis-estreptococo-grupo-a.svg",
    alt: "Flujograma: Grupos de estreptococos"
  },
  "PED-174": {
    titulo: "Vacunas atrasadas",
    imagen: "flujogramas/lactante-9-meses-pentavalente-pendiente-rotavirus-fuera-edad.svg",
    alt: "Flujograma: Vacunas atrasadas"
  },
  "HEM-034": {
    titulo: "Anemia: ¿se destruye o no se produce?",
    imagen: "flujogramas/nino-palidez-reticulocitos-altos-haptoglobina-baja-hemolisis.svg",
    alt: "Flujograma: Anemia: ¿se destruye o no se produce?"
  },
  "PED-175": {
    titulo: "Meningitis: antibiótico según la edad",
    imagen: "flujogramas/rn-6-dias-fiebre-fontanela-abombada-ampicilina-gentamicina.svg",
    alt: "Flujograma: Meningitis: antibiótico según la edad"
  },
  "PED-176": {
    titulo: "Recién nacido que se ahoga al comer",
    imagen: "flujogramas/rn-salivacion-sonda-no-pasa-sin-gas-atresia-esofago.svg",
    alt: "Flujograma: Recién nacido que se ahoga al comer"
  },
  "TRA-037": {
    titulo: "Fractura expuesta",
    imagen: "flujogramas/alud-fractura-conminuta-tibia-expuesta-tierra-desbridamiento.svg",
    alt: "Flujograma: Fractura expuesta"
  },
  "TRA-038": {
    titulo: "Esguince de tobillo",
    imagen: "flujogramas/torcedura-tobillo-equimosis-inestabilidad-esguince-grado-2.svg",
    alt: "Flujograma: Esguince de tobillo"
  },
  "CIR-096": {
    titulo: "Profundidad de las quemaduras",
    imagen: "flujogramas/quemadura-sin-dolor-tercer-grado.svg",
    alt: "Flujograma: Profundidad de las quemaduras"
  },
  "CIR-097": {
    titulo: "Ictericia después de la colecistectomía",
    imagen: "flujogramas/poscolecistectomia-ictericia-via-dilatada-colangioresonancia.svg",
    alt: "Flujograma: Ictericia después de la colecistectomía"
  },
  "CIR-098": {
    titulo: "Colecistitis en un paciente frágil",
    imagen: "flujogramas/anciano-87-colecistitis-sin-mejoria-colecistostomia-percutanea.svg",
    alt: "Flujograma: Colecistitis en un paciente frágil"
  },
  "GAS-061": {
    titulo: "Vesícula palpable con ictericia",
    imagen: "flujogramas/anciana-ictericia-vesicula-palpable-sin-calculos-tomografia.svg",
    alt: "Flujograma: Vesícula palpable con ictericia"
  },
  "OFT-039": {
    titulo: "Infecciones del oído",
    imagen: "flujogramas/nadador-otalgia-traccion-pabellon-pseudomonas.svg",
    alt: "Flujograma: Infecciones del oído"
  },
  "GIN-164": {
    titulo: "Contracciones en el pretérmino",
    imagen: "flujogramas/34-semanas-contracciones-sin-cambios-cervicales-observar.svg",
    alt: "Flujograma: Contracciones en el pretérmino"
  },
  "GIN-165": {
    titulo: "¿Funciona la reposición de volumen?",
    imagen: "flujogramas/hemorragia-posparto-choque-reposicion-diuresis.svg",
    alt: "Flujograma: ¿Funciona la reposición de volumen?"
  },
  "GIN-166": {
    titulo: "Glucosa alta en la gestante",
    imagen: "flujogramas/gestante-glucosa-ayunas-130-y-128-diabetes-confirmada.svg",
    alt: "Flujograma: Glucosa alta en la gestante"
  },
  "GIN-167": {
    titulo: "Antecedentes que obligan a buscar diabetes",
    imagen: "flujogramas/abortos-previos-macrosomico-descartar-diabetes.svg",
    alt: "Flujograma: Antecedentes que obligan a buscar diabetes"
  },
  "GIN-168": {
    titulo: "Desaceleraciones de la frecuencia fetal",
    imagen: "flujogramas/desaceleraciones-variables-compresion-cordon.svg",
    alt: "Flujograma: Desaceleraciones de la frecuencia fetal"
  },
  "GIN-169": {
    titulo: "Cómo preparar la oxitocina",
    imagen: "flujogramas/estimular-parto-10-ui-oxitocina-litro.svg",
    alt: "Flujograma: Cómo preparar la oxitocina"
  },
  "GIN-170": {
    titulo: "Feto pequeño: ¿PEG o RCIU?",
    imagen: "flujogramas/32-semanas-peso-p10-doppler-normal-control-2-semanas.svg",
    alt: "Flujograma: Feto pequeño: ¿PEG o RCIU?"
  },
  "GIN-171": {
    titulo: "¿Cómo se fecha el embarazo?",
    imagen: "flujogramas/42-semanas-fur-incierta-ecografia-primer-trimestre.svg",
    alt: "Flujograma: ¿Cómo se fecha el embarazo?"
  },
  "GIN-172": {
    titulo: "Exámenes del primer control prenatal",
    imagen: "flujogramas/primer-control-8-semanas-no-tolerancia-glucosa.svg",
    alt: "Flujograma: Exámenes del primer control prenatal"
  },
  "GIN-173": {
    titulo: "¿Se desprendió la placenta?",
    imagen: "flujogramas/alumbramiento-retrasado-kustner-cordon-asciende.svg",
    alt: "Flujograma: ¿Se desprendió la placenta?"
  },
  "GIN-174": {
    titulo: "Complicaciones según la corionicidad",
    imagen: "flujogramas/gemelos-dicigoticos-no-transfusion-feto-fetal.svg",
    alt: "Flujograma: Complicaciones según la corionicidad"
  },
  "GIN-175": {
    titulo: "Exámenes en el embarazo ya confirmado",
    imagen: "flujogramas/gestante-10-semanas-confirmada-beta-hcg-innecesaria.svg",
    alt: "Flujograma: Exámenes en el embarazo ya confirmado"
  },
  "GIN-176": {
    titulo: "Rotura prematura de membranas",
    imagen: "flujogramas/31-semanas-perdida-liquido-claro-rpm-corticoides-antibioticos.svg",
    alt: "Flujograma: Rotura prematura de membranas"
  },
  "GIN-177": {
    titulo: "Amenorrea secundaria",
    imagen: "flujogramas/amenorrea-7-semanas-beta-hcg-ecografia.svg",
    alt: "Flujograma: Amenorrea secundaria"
  },
  "GIN-178": {
    titulo: "Prolapso según el compartimento",
    imagen: "flujogramas/bulto-vaginal-polaquiuria-cistocele-colporrafia-anterior.svg",
    alt: "Flujograma: Prolapso según el compartimento"
  },
  "INF-086": {
    titulo: "Tratamiento de la meningitis tuberculosa",
    imagen: "flujogramas/meningitis-tuberculosa-esquema-hrze.svg",
    alt: "Flujograma: Tratamiento de la meningitis tuberculosa"
  },
  "PSI-035": {
    titulo: "Trastornos del aprendizaje",
    imagen: "flujogramas/dislexia-dificultad-para-leer.svg",
    alt: "Flujograma: Trastornos del aprendizaje"
  },
  "NEU-052": {
    titulo: "¿De qué muere el paciente con TEP?",
    imagen: "flujogramas/tep-masivo-muerte-falla-ventricular-derecha.svg",
    alt: "Flujograma: ¿De qué muere el paciente con TEP?"
  },
  "SP-127": {
    titulo: "Medidas de tendencia central",
    imagen: "flujogramas/glicemia-media-95-mediana-90-mitad-debajo.svg",
    alt: "Flujograma: Medidas de tendencia central"
  },
  "SP-128": {
    titulo: "Tasas con los datos del distrito",
    imagen: "flujogramas/300-muertes-covid-20000-habitantes-tasa-especifica-15.svg",
    alt: "Flujograma: Tasas con los datos del distrito"
  },
  "SP-129": {
    titulo: "Razón, proporción y tasa",
    imagen: "flujogramas/hombres-entre-mujeres-razon.svg",
    alt: "Flujograma: Razón, proporción y tasa"
  },
  "CB-062": {
    titulo: "Relaciones del hilio pulmonar",
    imagen: "flujogramas/hilio-pulmonar-bronquio-detras-derecho-debajo-izquierdo.svg",
    alt: "Flujograma: Relaciones del hilio pulmonar"
  },
  "CB-063": {
    titulo: "Lóbulos pulmonares",
    imagen: "flujogramas/tumor-lingula-pulmon-izquierdo.svg",
    alt: "Flujograma: Lóbulos pulmonares"
  },
  "CB-064": {
    titulo: "Control químico de la respiración",
    imagen: "flujogramas/co2-estimula-respiracion-quimiorreceptores-bulbo.svg",
    alt: "Flujograma: Control químico de la respiración"
  },
  "CB-065": {
    titulo: "Volúmenes y ventilación",
    imagen: "flujogramas/aire-que-no-participa-hematosis-espacio-muerto.svg",
    alt: "Flujograma: Volúmenes y ventilación"
  },
  "CB-066": {
    titulo: "Capacidad vital: cómo se suma",
    imagen: "flujogramas/capacidad-vital-volumen-corriente-reservas.svg",
    alt: "Flujograma: Capacidad vital: cómo se suma"
  },
  "CB-067": {
    titulo: "Difusión de O₂ y CO₂",
    imagen: "flujogramas/difusion-oxigeno-menor-que-co2-solubilidad.svg",
    alt: "Flujograma: Difusión de O₂ y CO₂"
  },
  "INF-087": {
    titulo: "Pruebas en tuberculosis",
    imagen: "flujogramas/quantiferon-infeccion-tb-sin-interferencia-bcg.svg",
    alt: "Flujograma: Pruebas en tuberculosis"
  },
  "SP-130": {
    titulo: "Conflicto entre principios éticos",
    imagen: "flujogramas/covid-sale-a-trabajar-autonomia-no-maleficencia.svg",
    alt: "Flujograma: Conflicto entre principios éticos"
  },
  "INF-088": {
    titulo: "Prevención de la neumonía asociada al ventilador",
    imagen: "flujogramas/ventilador-cabecera-45-grados-previene-neumonia.svg",
    alt: "Flujograma: Prevención de la neumonía asociada al ventilador"
  },
  "SP-131": {
    titulo: "Qué hacer ante un brote de dengue",
    imagen: "flujogramas/febriles-aedes-aegypti-control-focos-extramural.svg",
    alt: "Flujograma: Qué hacer ante un brote de dengue"
  },
  "NEF-073": {
    titulo: "Testículo que se achica tras una cirugía",
    imagen: "flujogramas/cirugia-pelvica-atrofia-testicular-arteria-testicular.svg",
    alt: "Flujograma: Testículo que se achica tras una cirugía"
  },
  "GIN-179": {
    titulo: "Prevención de la preeclampsia",
    imagen: "flujogramas/preeclampsia-previa-lupus-aspirina-dosis-baja.svg",
    alt: "Flujograma: Prevención de la preeclampsia"
  },
  "TRA-039": {
    titulo: "Luxación de cadera: el tiempo importa",
    imagen: "flujogramas/luxacion-posterior-cadera-reducida-72-h-necrosis-avascular.svg",
    alt: "Flujograma: Luxación de cadera: el tiempo importa"
  },
  "SP-132": {
    titulo: "Muerte encefálica y retiro del soporte",
    imagen: "flujogramas/muerte-encefalica-retirar-soporte-ningun-valor-vulnerado.svg",
    alt: "Flujograma: Muerte encefálica y retiro del soporte"
  },
  "GIN-180": {
    titulo: "Amenaza de parto pretérmino",
    imagen: "flujogramas/32-semanas-contracciones-regulares-1-cm-maduracion-tocolisis.svg",
    alt: "Flujograma: Amenaza de parto pretérmino"
  },
  "GIN-181": {
    titulo: "Embarazo con DIU",
    imagen: "flujogramas/usuaria-diu-test-positivo-hilos-visibles-retirar.svg",
    alt: "Flujograma: Embarazo con DIU"
  },
  "REU-054": {
    titulo: "Artritis con placas en la piel",
    imagen: "flujogramas/placas-codos-artritis-interfalangicas-distales-psoriasica.svg",
    alt: "Flujograma: Artritis con placas en la piel"
  },
  "PSI-036": {
    titulo: "Depresión con alucinaciones",
    imagen: "flujogramas/tristeza-ideas-suicidas-alucinaciones-depresion-psicotica.svg",
    alt: "Flujograma: Depresión con alucinaciones"
  },
  "END-051": {
    titulo: "Compensación de la acidosis metabólica",
    imagen: "flujogramas/cetoacidosis-kussmaul-compensacion-renal-bicarbonato.svg",
    alt: "Flujograma: Compensación de la acidosis metabólica"
  },
  "PED-177": {
    titulo: "Invaginación intestinal",
    imagen: "flujogramas/nino-2-anos-invaginacion-liquido-libre-laparotomia.svg",
    alt: "Flujograma: Invaginación intestinal"
  },
  "PED-178": {
    titulo: "Xeroftalmía",
    imagen: "flujogramas/nino-ceguera-nocturna-manchas-bitot-vitamina-a.svg",
    alt: "Flujograma: Xeroftalmía"
  },
  "NRL-047": {
    titulo: "Presión arterial en el ACV agudo",
    imagen: "flujogramas/acv-pa-208-bajar-menos-185-antes-trombolisis.svg",
    alt: "Flujograma: Presión arterial en el ACV agudo"
  },
  "CAR-062": {
    titulo: "Secuencia de la reanimación",
    imagen: "flujogramas/deja-de-respirar-sin-pulso-compresiones-toracicas.svg",
    alt: "Flujograma: Secuencia de la reanimación"
  },
  "SP-133": {
    titulo: "Comunicación para la salud",
    imagen: "flujogramas/covid-mascarilla-lavado-manos-medios-masivos.svg",
    alt: "Flujograma: Comunicación para la salud"
  },
  "NEF-074": {
    titulo: "Debilidad en un paciente con tiazida",
    imagen: "flujogramas/tiazida-debilidad-hiporreflexia-hipokalemia-ecg.svg",
    alt: "Flujograma: Debilidad en un paciente con tiazida"
  },
  "TRA-040": {
    titulo: "Cadera asimétrica en la lactante",
    imagen: "flujogramas/lactante-podalica-pliegues-asimetricos-galeazzi-ddc.svg",
    alt: "Flujograma: Cadera asimétrica en la lactante"
  },
  "END-052": {
    titulo: "Dolor neuropático diabético",
    imagen: "flujogramas/diabetica-parestesias-dolor-mmii-gabapentina.svg",
    alt: "Flujograma: Dolor neuropático diabético"
  },
  "GIN-182": {
    titulo: "Contracciones antes del término",
    imagen: "flujogramas/28-semanas-dilatacion-4-cm-borramiento-80-parto-pretermino.svg",
    alt: "Flujograma: Contracciones antes del término"
  },
  "GAS-062": {
    titulo: "Sospecha de cáncer gástrico avanzado",
    imagen: "flujogramas/saciedad-precoz-ganglio-virchow-ascitis-endoscopia.svg",
    alt: "Flujograma: Sospecha de cáncer gástrico avanzado"
  },
  "TRA-041": {
    titulo: "Artritis séptica en el adolescente",
    imagen: "flujogramas/adolescente-rodilla-fiebre-leucocitosis-artritis-septica-aureus.svg",
    alt: "Flujograma: Artritis séptica en el adolescente"
  },
  "GIN-183": {
    titulo: "Sangrado del tercer trimestre",
    imagen: "flujogramas/33-semanas-sangrado-sin-dolor-presentacion-flotante-no-tacto.svg",
    alt: "Flujograma: Sangrado del tercer trimestre"
  },
  "OFT-040": {
    titulo: "Epistaxis grave en el anciano",
    imagen: "flujogramas/anciano-epistaxis-fosa-y-boca-taponamiento-posterior.svg",
    alt: "Flujograma: Epistaxis grave en el anciano"
  },
  "CB-068": {
    titulo: "Recorrido del espermatozoide",
    imagen: "flujogramas/infertilidad-maduracion-espermatica-epididimo.svg",
    alt: "Flujograma: Recorrido del espermatozoide"
  },
  "GIN-184": {
    titulo: "Placenta baja en trabajo de parto",
    imagen: "flujogramas/placenta-baja-sangrado-escaso-7-cm-amniotomia-parto-vaginal.svg",
    alt: "Flujograma: Placenta baja en trabajo de parto"
  },
  "PED-179": {
    titulo: "Hepatitis A en el niño",
    imagen: "flujogramas/escolar-ictericia-transaminasas-altas-hepatitis-a-sintomaticos.svg",
    alt: "Flujograma: Hepatitis A en el niño"
  },
  "SP-134": {
    titulo: "Partes del protocolo de investigación",
    imagen: "flujogramas/cuarentena-estado-nutricional-marco-conceptual-estilos-vida.svg",
    alt: "Flujograma: Partes del protocolo de investigación"
  },
  "PED-180": {
    titulo: "Convulsión con fiebre en el lactante",
    imagen: "flujogramas/lactante-rigidez-fiebre-38-convulsion-febril-simple.svg",
    alt: "Flujograma: Convulsión con fiebre en el lactante"
  },
  "INF-089": {
    titulo: "Clasificación del caso de leptospirosis",
    imagen: "flujogramas/agricultor-fiebre-mialgia-pantorrillas-canales-leptospirosis-sospechoso.svg",
    alt: "Flujograma: Clasificación del caso de leptospirosis"
  },
  "HEM-035": {
    titulo: "Eritrocitosis en la altura",
    imagen: "flujogramas/cerro-de-pasco-hb-22-cianosis-mal-de-montana-cronico.svg",
    alt: "Flujograma: Eritrocitosis en la altura"
  },
  "INF-090": {
    titulo: "Secreción uretral",
    imagen: "flujogramas/uretritis-mucopurulenta-contacto-casual-ceftriaxona-azitromicina.svg",
    alt: "Flujograma: Secreción uretral"
  },
  "CB-069": {
    titulo: "Metronidazol y alcohol",
    imagen: "flujogramas/metronidazol-alcohol-palpitaciones-efecto-antabus.svg",
    alt: "Flujograma: Metronidazol y alcohol"
  },
  "PED-181": {
    titulo: "Caída del cordón umbilical",
    imagen: "flujogramas/neonato-14-dias-cordon-sin-signos-retraso-sin-patologia.svg",
    alt: "Flujograma: Caída del cordón umbilical"
  },
  "REU-055": {
    titulo: "Artritis séptica por estafilococo",
    imagen: "flujogramas/gram-cocos-racimos-liquido-sinovial-drenaje-antibioticos.svg",
    alt: "Flujograma: Artritis séptica por estafilococo"
  },
  "NRL-048": {
    titulo: "Migraña: ¿cuándo prevenir?",
    imagen: "flujogramas/migrana-mas-4-episodios-mes-profilaxis-propranolol.svg",
    alt: "Flujograma: Migraña: ¿cuándo prevenir?"
  },
  "CB-070": {
    titulo: "Déficit de vitaminas del complejo B",
    imagen: "flujogramas/preescolar-pobreza-edema-hiporreflexia-tiamina.svg",
    alt: "Flujograma: Déficit de vitaminas del complejo B"
  },
  "END-053": {
    titulo: "Tratamiento de la obesidad",
    imagen: "flujogramas/obeso-imc-38-orlistat-agregar-ejercicio-aerobico.svg",
    alt: "Flujograma: Tratamiento de la obesidad"
  },
  "OFT-041": {
    titulo: "Insecto vivo en el oído",
    imagen: "flujogramas/nino-insecto-vivo-oido-aceite-mineral.svg",
    alt: "Flujograma: Insecto vivo en el oído"
  },
  "GAS-063": {
    titulo: "Dolor abdominal con cambio del hábito",
    imagen: "flujogramas/dolor-colico-cede-defecar-diarrea-estrenimiento-intestino-irritable.svg",
    alt: "Flujograma: Dolor abdominal con cambio del hábito"
  },
  "SP-135": {
    titulo: "Intervención ante obesidad escolar",
    imagen: "flujogramas/colegio-80-sobrepeso-comunicacion-educativa-grupal.svg",
    alt: "Flujograma: Intervención ante obesidad escolar"
  },
  "GIN-185": {
    titulo: "Quiste de ovario en la mujer joven",
    imagen: "flujogramas/quiste-ovarico-simple-4-cm-observacion.svg",
    alt: "Flujograma: Quiste de ovario en la mujer joven"
  },
  "OFT-042": {
    titulo: "Trauma ocular penetrante",
    imagen: "flujogramas/amoladora-cuerpo-extrano-penetrante-analgesia-ev.svg",
    alt: "Flujograma: Trauma ocular penetrante"
  },
  "CIR-099": {
    titulo: "Trauma en el hipocondrio izquierdo",
    imagen: "flujogramas/fracturas-costales-9-10-izquierdas-liquido-libre-bazo.svg",
    alt: "Flujograma: Trauma en el hipocondrio izquierdo"
  },
  "CB-071": {
    titulo: "Hormonas de la lactancia",
    imagen: "flujogramas/lactancia-succion-aumenta-oxitocina.svg",
    alt: "Flujograma: Hormonas de la lactancia"
  },
  "GIN-186": {
    titulo: "VIH y vía del parto",
    imagen: "flujogramas/vih-carga-viral-1500-37-semanas-evitar-parto-vaginal.svg",
    alt: "Flujograma: VIH y vía del parto"
  },
  "CIR-100": {
    titulo: "Isquemia aguda de la pierna",
    imagen: "flujogramas/pie-frio-sin-pulsos-paralisis-embolia-arterial.svg",
    alt: "Flujograma: Isquemia aguda de la pierna"
  },
  "NEF-075": {
    titulo: "Piuria con urocultivo negativo",
    imagen: "flujogramas/piuria-esteril-urocultivo-negativo-tuberculosis-urogenital.svg",
    alt: "Flujograma: Piuria con urocultivo negativo"
  },
  "TRA-042": {
    titulo: "Dolor de muñeca tras una caída",
    imagen: "flujogramas/caida-mano-extendida-dolor-tabaquera-escafoides.svg",
    alt: "Flujograma: Dolor de muñeca tras una caída"
  },
  "PED-182": {
    titulo: "Diarrea aguda en el lactante",
    imagen: "flujogramas/lactante-6-meses-diarrea-vomitos-deshidratacion-rotavirus.svg",
    alt: "Flujograma: Diarrea aguda en el lactante"
  },
  "GAS-064": {
    titulo: "Criterios de Ranson al ingreso",
    imagen: "flujogramas/pancreatitis-alcoholica-60-anos-ranson-edad.svg",
    alt: "Flujograma: Criterios de Ranson al ingreso"
  },
  "SP-136": {
    titulo: "Esterilización en una persona incapaz",
    imagen: "flujogramas/incapacidad-mental-ligadura-evaluacion-psiquiatrica-judicial.svg",
    alt: "Flujograma: Esterilización en una persona incapaz"
  },
  "CIR-101": {
    titulo: "Trauma abdominal cerrado en el niño",
    imagen: "flujogramas/nino-golpe-abdominal-hipocalcemia-pancreas.svg",
    alt: "Flujograma: Trauma abdominal cerrado en el niño"
  },
  "CIR-102": {
    titulo: "Dolor en fosa ilíaca derecha en la mujer joven",
    imagen: "flujogramas/mujer-30-dolor-fid-fiebre-leucocitosis-alvarado-ecografia.svg",
    alt: "Flujograma: Dolor en fosa ilíaca derecha en la mujer joven"
  },
  "CIR-103": {
    titulo: "Insuficiencia venosa crónica",
    imagen: "flujogramas/varices-pesadez-vespertina-perthes-terapia-compresiva.svg",
    alt: "Flujograma: Insuficiencia venosa crónica"
  },
  "GIN-187": {
    titulo: "Lupus: ¿cuándo embarazarse?",
    imagen: "flujogramas/lupus-preconcepcional-seis-meses-inactivo.svg",
    alt: "Flujograma: Lupus: ¿cuándo embarazarse?"
  },
  "SP-137": {
    titulo: "Cómo leer el riesgo relativo",
    imagen: "flujogramas/riesgo-relativo-igual-a-uno-sin-asociacion.svg",
    alt: "Flujograma: Cómo leer el riesgo relativo"
  },
  "END-054": {
    titulo: "Estupor e hipotermia tras la cirugía",
    imagen: "flujogramas/posoperada-estupor-hipotermia-cicatriz-cuello-coma-mixedematoso.svg",
    alt: "Flujograma: Estupor e hipotermia tras la cirugía"
  },
  "PED-183": {
    titulo: "Dolor cólico con heces en jalea",
    imagen: "flujogramas/nino-3-anos-heces-jalea-masa-hipocondrio-enema.svg",
    alt: "Flujograma: Dolor cólico con heces en jalea"
  },
  "CB-072": {
    titulo: "Acidosis con visión borrosa",
    imagen: "flujogramas/bebedor-vision-borrosa-anion-gap-alto-metanol.svg",
    alt: "Flujograma: Acidosis con visión borrosa"
  },
  "CB-073": {
    titulo: "Gases tóxicos",
    imagen: "flujogramas/limpieza-pozo-septico-desmayo-acido-sulfhidrico.svg",
    alt: "Flujograma: Gases tóxicos"
  },
  "PED-184": {
    titulo: "Síndrome nefrótico según el curso",
    imagen: "flujogramas/nefrotico-recae-al-bajar-corticoides-corticodependencia.svg",
    alt: "Flujograma: Síndrome nefrótico según el curso"
  },
  "PED-185": {
    titulo: "Fracturas a repetición en el niño",
    imagen: "flujogramas/fracturas-repeticion-escleras-azules-osteogenesis-imperfecta.svg",
    alt: "Flujograma: Fracturas a repetición en el niño"
  },
  "GIN-188": {
    titulo: "Tamizaje prenatal por edad gestacional",
    imagen: "flujogramas/hijo-down-translucencia-nucal-11-14-semanas.svg",
    alt: "Flujograma: Tamizaje prenatal por edad gestacional"
  },
  "REU-056": {
    titulo: "Monoartritis aguda con ácido úrico alto",
    imagen: "flujogramas/obeso-joven-monoartritis-rodilla-acido-urico-liquido-sinovial.svg",
    alt: "Flujograma: Monoartritis aguda con ácido úrico alto"
  },
  "PED-186": {
    titulo: "Enterocolitis necrotizante",
    imagen: "flujogramas/prematuro-1200-g-distension-neumatosis-enterocolitis.svg",
    alt: "Flujograma: Enterocolitis necrotizante"
  },
  "INF-091": {
    titulo: "Intoxicación alimentaria: tiempo de incubación",
    imagen: "flujogramas/brote-escolar-mayonesa-6-horas-bacillus-cereus.svg",
    alt: "Flujograma: Intoxicación alimentaria: tiempo de incubación"
  },
  "TRA-043": {
    titulo: "Complicaciones del arnés de Pavlik",
    imagen: "flujogramas/pavlik-abduccion-excesiva-necrosis-avascular-cabeza-femoral.svg",
    alt: "Flujograma: Complicaciones del arnés de Pavlik"
  },
  "SP-138": {
    titulo: "¿Qué diseño es?",
    imagen: "flujogramas/cancer-mama-emparejadas-lactancia-casos-controles.svg",
    alt: "Flujograma: ¿Qué diseño es?"
  },
  "TRA-044": {
    titulo: "Bulto detrás de la rodilla en una niña",
    imagen: "flujogramas/nina-bolita-popliteo-indolora-ganglion.svg",
    alt: "Flujograma: Bulto detrás de la rodilla en una niña"
  },
  "NRL-049": {
    titulo: "Parásitos que llegan al cerebro",
    imagen: "flujogramas/adolescente-rural-convulsiones-calcificaciones-taenia-solium.svg",
    alt: "Flujograma: Parásitos que llegan al cerebro"
  },
  "NEF-076": {
    titulo: "Síndrome nefrótico con inflamación crónica",
    imagen: "flujogramas/osteomielitis-cronica-anasarca-proteinuria-amiloidosis.svg",
    alt: "Flujograma: Síndrome nefrótico con inflamación crónica"
  },
  "OFT-043": {
    titulo: "Otitis media tras amoxicilina reciente",
    imagen: "flujogramas/otitis-media-recurrente-amoxicilina-previa-amoxicilina-clavulanico.svg",
    alt: "Flujograma: Otitis media tras amoxicilina reciente"
  },
  "SP-139": {
    titulo: "Participación de un niño en un ensayo clínico",
    imagen: "flujogramas/nino-9-anos-ensayo-asentimiento-madre-firma.svg",
    alt: "Flujograma: Participación de un niño en un ensayo clínico"
  },
  "SP-140": {
    titulo: "Indicadores de logro",
    imagen: "flujogramas/sulfato-ferroso-entregado-no-administrado-efectividad.svg",
    alt: "Flujograma: Indicadores de logro"
  },
  "SP-141": {
    titulo: "Garantizar la atención de la discapacidad",
    imagen: "flujogramas/centro-i4-discapacidad-sin-acceso-upss-rehabilitacion.svg",
    alt: "Flujograma: Garantizar la atención de la discapacidad"
  },
  "PED-187": {
    titulo: "Neumonía en el preescolar",
    imagen: "flujogramas/preescolar-fiebre-polipnea-tirajes-crepitantes-rx-torax.svg",
    alt: "Flujograma: Neumonía en el preescolar"
  },
  "GIN-189": {
    titulo: "Masa en la episiotomía",
    imagen: "flujogramas/puerpera-hematoma-3-cm-episiotomia-observacion.svg",
    alt: "Flujograma: Masa en la episiotomía"
  },
  "END-055": {
    titulo: "Hipoglucemia por antidiabéticos",
    imagen: "flujogramas/anciano-falla-renal-glucosa-50-glibenclamida.svg",
    alt: "Flujograma: Hipoglucemia por antidiabéticos"
  },
  "NEF-077": {
    titulo: "Hematuria recurrente en el joven",
    imagen: "flujogramas/hematuria-tras-infeccion-respiratoria-nefropatia-iga.svg",
    alt: "Flujograma: Hematuria recurrente en el joven"
  },
  "CAR-063": {
    titulo: "Soplos y valvulopatías",
    imagen: "flujogramas/angina-sincope-disnea-pulso-parvus-estenosis-aortica.svg",
    alt: "Flujograma: Soplos y valvulopatías"
  },
  "END-056": {
    titulo: "¿Cuándo referir al diabético?",
    imagen: "flujogramas/dm2-establecimiento-i4-albuminuria-300-referir.svg",
    alt: "Flujograma: ¿Cuándo referir al diabético?"
  },
  "GIN-190": {
    titulo: "Tipos de incontinencia urinaria",
    imagen: "flujogramas/urgencia-miccional-residuo-150-urodinamia.svg",
    alt: "Flujograma: Tipos de incontinencia urinaria"
  },
  "SP-142": {
    titulo: "Seguimiento de casos y contactos",
    imagen: "flujogramas/centro-i3-seguimiento-casos-contactos-equipos-intervencion.svg",
    alt: "Flujograma: Seguimiento de casos y contactos"
  },
  "INF-092": {
    titulo: "Prolapso rectal con anemia en el niño",
    imagen: "flujogramas/nino-prolapso-rectal-hematoquezia-anemia-tricocefalo.svg",
    alt: "Flujograma: Prolapso rectal con anemia en el niño"
  },
  "GIN-191": {
    titulo: "Podálica en periodo expulsivo",
    imagen: "flujogramas/multipara-nalgas-puras-expulsivo-parto-vaginal.svg",
    alt: "Flujograma: Podálica en periodo expulsivo"
  },
  "NEU-053": {
    titulo: "COVID-19: ¿qué soporte de oxígeno?",
    imagen: "flujogramas/covid-pafi-305-oxigenoterapia-convencional.svg",
    alt: "Flujograma: COVID-19: ¿qué soporte de oxígeno?"
  },
  "CAR-064": {
    titulo: "Ritmos del paro y su manejo",
    imagen: "flujogramas/monitor-asistolia-adrenalina-rcp.svg",
    alt: "Flujograma: Ritmos del paro y su manejo"
  },
  "HEM-036": {
    titulo: "Forma del eritrocito y enfermedad",
    imagen: "flujogramas/afrodescendiente-anemia-ictericia-reticulocitos-0-drepanocitos.svg",
    alt: "Flujograma: Forma del eritrocito y enfermedad"
  },
  "PED-188": {
    titulo: "Hierro preventivo según el peso al nacer",
    imagen: "flujogramas/bajo-peso-2100-g-hierro-desde-el-primer-mes.svg",
    alt: "Flujograma: Hierro preventivo según el peso al nacer"
  },
  "CIR-104": {
    titulo: "Dolor abdominal grave en el anciano vascular",
    imagen: "flujogramas/anciano-melena-dolor-difuso-neumatosis-ldh-isquemia-mesenterica.svg",
    alt: "Flujograma: Dolor abdominal grave en el anciano vascular"
  },
  "GIN-192": {
    titulo: "Perforación uterina durante el legrado",
    imagen: "flujogramas/legrado-perforacion-histerometro-sin-sangrado-observar.svg",
    alt: "Flujograma: Perforación uterina durante el legrado"
  },
  "NEU-054": {
    titulo: "Lactancia en la madre con tuberculosis",
    imagen: "flujogramas/puerpera-tb-en-tratamiento-lactancia-con-mascarilla.svg",
    alt: "Flujograma: Lactancia en la madre con tuberculosis"
  },
  "PED-189": {
    titulo: "Hemorragia por falta de vitamina K",
    imagen: "flujogramas/lactante-1-mes-parto-domiciliario-sangrado-vitamina-k.svg",
    alt: "Flujograma: Hemorragia por falta de vitamina K"
  },
  "NRL-050": {
    titulo: "Tipos de temblor",
    imagen: "flujogramas/anciano-temblor-reposo-reemergente-bradicinesia-parkinsoniano.svg",
    alt: "Flujograma: Tipos de temblor"
  },
  "SP-143": {
    titulo: "Niveles del cuidado de la salud",
    imagen: "flujogramas/obesidad-escolar-campo-deportivo-cuidado-comunitario.svg",
    alt: "Flujograma: Niveles del cuidado de la salud"
  },
  "OFT-044": {
    titulo: "Hipoacusia súbita tras limpiarse el oído",
    imagen: "flujogramas/hisopo-hipoacusia-tinnitus-tapon-cerumen.svg",
    alt: "Flujograma: Hipoacusia súbita tras limpiarse el oído"
  },
  "INF-093": {
    titulo: "Infección tuberculosa latente en la gestante con VIH",
    imagen: "flujogramas/gestante-vih-ppd-6-mm-isoniacida-6-meses.svg",
    alt: "Flujograma: Infección tuberculosa latente en la gestante con VIH"
  },
  "HEM-037": {
    titulo: "Anemia macrocítica con alteración mental",
    imagen: "flujogramas/anciana-deterioro-cognitivo-vcm-105-pancitopenia-b12.svg",
    alt: "Flujograma: Anemia macrocítica con alteración mental"
  },
  "SP-144": {
    titulo: "Características del monitoreo",
    imagen: "flujogramas/monitoreo-desempeno-evidencias-verificables-objetivo.svg",
    alt: "Flujograma: Características del monitoreo"
  },
  "PED-190": {
    titulo: "Malformación anorrectal alta",
    imagen: "flujogramas/rn-perine-plano-sin-orificio-anal-colostomia.svg",
    alt: "Flujograma: Malformación anorrectal alta"
  },
  "PSI-037": {
    titulo: "Despertares nocturnos en el niño",
    imagen: "flujogramas/nino-4-anos-despierta-panico-sin-recuerdo-terror-nocturno.svg",
    alt: "Flujograma: Despertares nocturnos en el niño"
  },
  "END-057": {
    titulo: "Parestesias tras la tiroidectomía",
    imagen: "flujogramas/postiroidectomia-parestesias-chvostek-calcio-serico.svg",
    alt: "Flujograma: Parestesias tras la tiroidectomía"
  },
  "TRA-045": {
    titulo: "Infección de la pierna que no termina de curar",
    imagen: "flujogramas/escolar-herida-pierna-fiebre-dolor-persistente-radiografia.svg",
    alt: "Flujograma: Infección de la pierna que no termina de curar"
  },
  "GIN-193": {
    titulo: "Distocias del cordón",
    imagen: "flujogramas/multipara-cabeza-flotante-amniotomia-prolapso-cordon.svg",
    alt: "Flujograma: Distocias del cordón"
  },
  "INF-094": {
    titulo: "Lesiones infiltradas con anestesia",
    imagen: "flujogramas/adolescente-infiltracion-orejas-atrofia-tenar-baar-mitsuda-negativo.svg",
    alt: "Flujograma: Lesiones infiltradas con anestesia"
  },
  "GIN-194": {
    titulo: "Situación transversa en trabajo de parto",
    imagen: "flujogramas/primigesta-7-cm-situacion-transversa-cesarea.svg",
    alt: "Flujograma: Situación transversa en trabajo de parto"
  },
  "GAS-065": {
    titulo: "Infección del líquido ascítico",
    imagen: "flujogramas/cirrotico-fiebre-dolor-pmn-500-peritonitis-espontanea.svg",
    alt: "Flujograma: Infección del líquido ascítico"
  },
  "SP-145": {
    titulo: "¿Experimento o cuasiexperimento?",
    imagen: "flujogramas/micronutrientes-colegio-control-cuasiexperimental.svg",
    alt: "Flujograma: ¿Experimento o cuasiexperimento?"
  },
  "INF-095": {
    titulo: "Pierna roja y caliente con fiebre",
    imagen: "flujogramas/obeso-placa-eritematosa-pantorrilla-fiebre-celulitis.svg",
    alt: "Flujograma: Pierna roja y caliente con fiebre"
  },
  "PED-191": {
    titulo: "Deshidratación con sodio alto",
    imagen: "flujogramas/preescolar-diarrea-sodio-160-calcular-deficit.svg",
    alt: "Flujograma: Deshidratación con sodio alto"
  },
  "SP-146": {
    titulo: "Niveles de prevención",
    imagen: "flujogramas/busqueda-activa-sintomaticos-respiratorios-prevencion-secundaria.svg",
    alt: "Flujograma: Niveles de prevención"
  },
  "CIR-105": {
    titulo: "¿Cuándo trasladar a un quemado?",
    imagen: "flujogramas/quemadura-tercer-grado-mayor-20-unidad-quemados.svg",
    alt: "Flujograma: ¿Cuándo trasladar a un quemado?"
  },
  "NEF-078": {
    titulo: "Fármacos para la hiperplasia de próstata",
    imagen: "flujogramas/hiperplasia-prostatica-pilar-medico-alfa-bloqueador.svg",
    alt: "Flujograma: Fármacos para la hiperplasia de próstata"
  },
  "PED-192": {
    titulo: "Grado de deshidratación",
    imagen: "flujogramas/lactante-ojos-hundidos-sed-pliegue-rehidratacion-oral.svg",
    alt: "Flujograma: Grado de deshidratación"
  },
  "GIN-195": {
    titulo: "Riesgo de preeclampsia en el lupus",
    imagen: "flujogramas/primigesta-lupus-riesgo-alto-trastorno-hipertensivo.svg",
    alt: "Flujograma: Riesgo de preeclampsia en el lupus"
  },
  "END-058": {
    titulo: "Formas de vitamina D y fármacos del hueso",
    imagen: "flujogramas/anciano-fracturas-suplemento-vitamina-d-colecalciferol.svg",
    alt: "Flujograma: Formas de vitamina D y fármacos del hueso"
  },
  "REU-057": {
    titulo: "Acné: tratamiento por gravedad",
    imagen: "flujogramas/adolescente-acne-rostro-tronco-retinoide-topico.svg",
    alt: "Flujograma: Acné: tratamiento por gravedad"
  },
  "OFT-045": {
    titulo: "Úlceras corneales infecciosas",
    imagen: "flujogramas/rama-arbusto-ulcera-corneal-satelites-aspergillus.svg",
    alt: "Flujograma: Úlceras corneales infecciosas"
  },
  "NRL-051": {
    titulo: "Guillain-Barré con compromiso respiratorio",
    imagen: "flujogramas/guillain-barre-disnea-sato2-89-soporte-ventilatorio.svg",
    alt: "Flujograma: Guillain-Barré con compromiso respiratorio"
  },
  "NEF-079": {
    titulo: "¿Qué diálisis para el paciente crítico?",
    imagen: "flujogramas/uci-shock-falla-renal-hemodialisis-continua.svg",
    alt: "Flujograma: ¿Qué diálisis para el paciente crítico?"
  },
  "SP-147": {
    titulo: "Principios de la bioética",
    imagen: "flujogramas/madre-niega-puncion-lumbar-autonomia.svg",
    alt: "Flujograma: Principios de la bioética"
  },
  "GIN-196": {
    titulo: "Fase activa que no avanza",
    imagen: "flujogramas/6-cm-cuatro-horas-dinamica-debil-oxitocina.svg",
    alt: "Flujograma: Fase activa que no avanza"
  },
  "CAR-065": {
    titulo: "Marcadores de laboratorio",
    imagen: "flujogramas/shock-hipoperfusion-lactato-serico.svg",
    alt: "Flujograma: Marcadores de laboratorio"
  },
  "SP-148": {
    titulo: "Proceso administrativo",
    imagen: "flujogramas/director-demanda-proyectada-metas-recursos-prevision.svg",
    alt: "Flujograma: Proceso administrativo"
  },
  "GIN-197": {
    titulo: "Flujo vaginal: ¿qué tratamiento?",
    imagen: "flujogramas/flujo-grisaceo-aminas-positivo-vaginosis-metronidazol.svg",
    alt: "Flujograma: Flujo vaginal: ¿qué tratamiento?"
  },
  "SP-149": {
    titulo: "Atención primaria de salud renovada",
    imagen: "flujogramas/reorientar-sistemas-aps-promocion-prevencion.svg",
    alt: "Flujograma: Atención primaria de salud renovada"
  },
  "REU-058": {
    titulo: "Costras extensas poco pruriginosas",
    imagen: "flujogramas/htlv1-lesiones-hiperqueratosicas-costrosas-sarna-noruega.svg",
    alt: "Flujograma: Costras extensas poco pruriginosas"
  },
  "NRL-052": {
    titulo: "Intervalo lúcido tras un golpe",
    imagen: "flujogramas/golpe-ladrillo-intervalo-lucido-midriasis-hematoma-epidural.svg",
    alt: "Flujograma: Intervalo lúcido tras un golpe"
  },
  "NEU-055": {
    titulo: "Neumonía: ¿casa u hospital?",
    imagen: "flujogramas/neumonia-hipotension-fr-32-66-anos-curb65-hospitalizar.svg",
    alt: "Flujograma: Neumonía: ¿casa u hospital?"
  },
  "NEU-056": {
    titulo: "¿Qué criterio manda referir?",
    imagen: "flujogramas/covid-disnea-musculos-accesorios-criterio-clinico-referencia.svg",
    alt: "Flujograma: ¿Qué criterio manda referir?"
  },
  "CB-074": {
    titulo: "Intoxicación por monóxido de carbono",
    imagen: "flujogramas/nino-inhalacion-humo-monoxido-carbono-oxigeno-100.svg",
    alt: "Flujograma: Intoxicación por monóxido de carbono"
  },
  "END-059": {
    titulo: "Manejo de la cetoacidosis diabética",
    imagen: "flujogramas/cetoacidosis-debut-hipotension-no-via-oral.svg",
    alt: "Flujograma: Manejo de la cetoacidosis diabética"
  },
  "HEM-038": {
    titulo: "Anemia hemolítica: ¿cuál es el tipo?",
    imagen: "flujogramas/hemolisis-esplenomegalia-sin-esquistocitos-coombs.svg",
    alt: "Flujograma: Anemia hemolítica: ¿cuál es el tipo?"
  },
  "GIN-198": {
    titulo: "Mastitis y lactancia",
    imagen: "flujogramas/puerpera-mama-roja-dolorosa-fiebre-continuar-lactancia.svg",
    alt: "Flujograma: Mastitis y lactancia"
  },
  "PED-193": {
    titulo: "Diarrea prolongada en el preescolar",
    imagen: "flujogramas/preescolar-diarrea-acuosa-distension-desnutricion-giardiasis.svg",
    alt: "Flujograma: Diarrea prolongada en el preescolar"
  },
  "SP-150": {
    titulo: "Funciones esenciales de salud pública",
    imagen: "flujogramas/funcion-esencial-salud-publica-aps-promocion.svg",
    alt: "Flujograma: Funciones esenciales de salud pública"
  },
  "SP-151": {
    titulo: "Ventajas y desventajas de los diseños",
    imagen: "flujogramas/casos-controles-desventaja-sesgo-seleccion.svg",
    alt: "Flujograma: Ventajas y desventajas de los diseños"
  },
  "NEF-080": {
    titulo: "Hiperpotasemia grave",
    imagen: "flujogramas/falla-renal-k-8-bradiarritmia-corregir-hiperkalemia.svg",
    alt: "Flujograma: Hiperpotasemia grave"
  },
  "GIN-199": {
    titulo: "Tipos de aborto",
    imagen: "flujogramas/8-semanas-cervix-abierto-membranas-protruyen-aborto-inminente.svg",
    alt: "Flujograma: Tipos de aborto"
  },
  "NEU-057": {
    titulo: "Infección tuberculosa latente en la gestante",
    imagen: "flujogramas/gestante-33-semanas-ppd-positivo-tratar-postparto.svg",
    alt: "Flujograma: Infección tuberculosa latente en la gestante"
  },
  "INF-096": {
    titulo: "Ciclo de Ascaris",
    imagen: "flujogramas/nino-tos-hemoptoica-eosinofilia-ascaris-loeffler.svg",
    alt: "Flujograma: Ciclo de Ascaris"
  },
  "OFT-046": {
    titulo: "Rinorrea clara con prurito",
    imagen: "flujogramas/adolescente-rinorrea-prurito-nasal-ocular-prick-test.svg",
    alt: "Flujograma: Rinorrea clara con prurito"
  },
  "GIN-200": {
    titulo: "¿Cuándo estudiar la infertilidad?",
    imagen: "flujogramas/mujer-38-seis-meses-sin-embarazo-estudio-infertilidad.svg",
    alt: "Flujograma: ¿Cuándo estudiar la infertilidad?"
  },
  "PSI-038": {
    titulo: "Autolesiones e inestabilidad",
    imagen: "flujogramas/autolesiones-miedo-abandono-relaciones-inestables-limite.svg",
    alt: "Flujograma: Autolesiones e inestabilidad"
  },
  "GIN-201": {
    titulo: "Calendario de la profilaxis anti-D",
    imagen: "flujogramas/rh-negativo-coombs-negativo-anti-d-28-semanas.svg",
    alt: "Flujograma: Calendario de la profilaxis anti-D"
  },
  "CIR-106": {
    titulo: "Estudios en la obstrucción intestinal",
    imagen: "flujogramas/cesarea-previa-distension-vomitos-bridas-rx-de-pie.svg",
    alt: "Flujograma: Estudios en la obstrucción intestinal"
  },
  "NEU-058": {
    titulo: "EPOC con neumonía e hipoxemia",
    imagen: "flujogramas/epoc-neumonia-sato2-86-oxigenoterapia-controlada.svg",
    alt: "Flujograma: EPOC con neumonía e hipoxemia"
  },
  "NEU-059": {
    titulo: "Oxígeno domiciliario en la EPOC",
    imagen: "flujogramas/epoc-sato2-85-oxigeno-domiciliario-permanente.svg",
    alt: "Flujograma: Oxígeno domiciliario en la EPOC"
  },
  "GIN-202": {
    titulo: "RPM a término sin trabajo de parto",
    imagen: "flujogramas/rpm-39-semanas-12-horas-bishop-favorable-induccion.svg",
    alt: "Flujograma: RPM a término sin trabajo de parto"
  },
  "GAS-066": {
    titulo: "Anemia con sangre oculta en heces",
    imagen: "flujogramas/anciano-anemia-thevenon-positivo-colonoscopia.svg",
    alt: "Flujograma: Anemia con sangre oculta en heces"
  },
  "GIN-203": {
    titulo: "Fiebre con RPM en el primer nivel",
    imagen: "flujogramas/rpm-2-dias-fiebre-liquido-purulento-antibiotico-referir.svg",
    alt: "Flujograma: Fiebre con RPM en el primer nivel"
  },
  "GIN-204": {
    titulo: "¿Cómo calcular la edad gestacional?",
    imagen: "flujogramas/sin-fur-test-positivo-ecografia-transvaginal-edad-gestacional.svg",
    alt: "Flujograma: ¿Cómo calcular la edad gestacional?"
  },
  "PED-194": {
    titulo: "Estado nutricional por peso para la talla",
    imagen: "flujogramas/menor-5-anos-peso-talla-mas-3-de-obesidad.svg",
    alt: "Flujograma: Estado nutricional por peso para la talla"
  },
  "INF-097": {
    titulo: "Fiebre ondulante con artralgias",
    imagen: "flujogramas/ganadero-fiebre-ondulante-rosa-bengala-doxiciclina-rifampicina.svg",
    alt: "Flujograma: Fiebre ondulante con artralgias"
  },
  "PSI-039": {
    titulo: "Intoxicación aguda por cocaína",
    imagen: "flujogramas/adolescente-cocaina-agitacion-taquicardia-diazepam.svg",
    alt: "Flujograma: Intoxicación aguda por cocaína"
  },
  "INF-098": {
    titulo: "Neumonía en el paciente con catéter",
    imagen: "flujogramas/dialisis-cateter-postoperado-neumonia-staphylococcus-aureus.svg",
    alt: "Flujograma: Neumonía en el paciente con catéter"
  },
  "HEM-039": {
    titulo: "Sangrado articular en el varón joven",
    imagen: "flujogramas/adolescente-hemartrosis-ttpa-prolongado-hemofilia-a.svg",
    alt: "Flujograma: Sangrado articular en el varón joven"
  },
  "PED-195": {
    titulo: "Dosis de hierro en el lactante",
    imagen: "flujogramas/lactante-5-meses-hb-11-5-hierro-2-mg-kg.svg",
    alt: "Flujograma: Dosis de hierro en el lactante"
  },
  "GIN-205": {
    titulo: "Embarazo ectópico: ¿metotrexato o cirugía?",
    imagen: "flujogramas/ectopico-no-roto-25-mm-bhcg-3500-metotrexato.svg",
    alt: "Flujograma: Embarazo ectópico: ¿metotrexato o cirugía?"
  },
  "NEF-081": {
    titulo: "Intoxicación por magnesio",
    imagen: "flujogramas/nefropatia-magnesio-naturista-hiporreflexia-hemodialisis.svg",
    alt: "Flujograma: Intoxicación por magnesio"
  },
  "PED-196": {
    titulo: "Urticaria con dificultad respiratoria",
    imagen: "flujogramas/nino-urticaria-ronquera-cianosis-anafilaxia-adrenalina.svg",
    alt: "Flujograma: Urticaria con dificultad respiratoria"
  },
  "GIN-206": {
    titulo: "DIU que no se ve",
    imagen: "flujogramas/diu-hilos-no-visibles-eco-sin-diu-rx-abdomen.svg",
    alt: "Flujograma: DIU que no se ve"
  },
  "NEU-060": {
    titulo: "Signos de gravedad en la crisis asmática",
    imagen: "flujogramas/asmatico-disnea-severa-murmullo-ausente-torax-silente.svg",
    alt: "Flujograma: Signos de gravedad en la crisis asmática"
  },
  "GIN-207": {
    titulo: "Contracciones con cuello largo",
    imagen: "flujogramas/31-semanas-contracciones-cervix-35-mm-fibronectina-negativa.svg",
    alt: "Flujograma: Contracciones con cuello largo"
  },
  "CIR-107": {
    titulo: "Lesiones del duodeno por trauma",
    imagen: "flujogramas/golpe-timon-hematoma-pared-duodenal-observacion.svg",
    alt: "Flujograma: Lesiones del duodeno por trauma"
  },
  "SP-152": {
    titulo: "Términos epidemiológicos",
    imagen: "flujogramas/piura-peste-roedores-muertos-epizootia.svg",
    alt: "Flujograma: Términos epidemiológicos"
  },
  "GIN-208": {
    titulo: "Altura uterina y edad gestacional",
    imagen: "flujogramas/au-21-cm-fur-27-semanas-eg-clinica-21.svg",
    alt: "Flujograma: Altura uterina y edad gestacional"
  },
  "GIN-209": {
    titulo: "Embarazo prolongado con oligohidramnios",
    imagen: "flujogramas/41-semanas-oligohidramnios-bishop-2-misoprostol.svg",
    alt: "Flujograma: Embarazo prolongado con oligohidramnios"
  },
  "HEM-040": {
    titulo: "Sangrado por warfarina",
    imagen: "flujogramas/warfarina-inr-7-hematemesis-plasma-fresco.svg",
    alt: "Flujograma: Sangrado por warfarina"
  },
  "REU-059": {
    titulo: "Micosis superficiales",
    imagen: "flujogramas/manchas-hipo-hiperpigmentadas-koh-espagueti-albondigas-malassezia.svg",
    alt: "Flujograma: Micosis superficiales"
  },
  "SP-153": {
    titulo: "Elementos de la APS",
    imagen: "flujogramas/dengue-pacientes-no-atendidos-letalidad-cobertura.svg",
    alt: "Flujograma: Elementos de la APS"
  },
  "CIR-108": {
    titulo: "Infección del sitio quirúrgico",
    imagen: "flujogramas/apendicectomia-fiebre-herida-infectada-drenaje-cultivo.svg",
    alt: "Flujograma: Infección del sitio quirúrgico"
  },
  "REU-060": {
    titulo: "Poliartritis de manos",
    imagen: "flujogramas/poliartritis-manos-anti-ccp-erosiones-artritis-reumatoide.svg",
    alt: "Flujograma: Poliartritis de manos"
  },
  "PED-197": {
    titulo: "Indicadores antropométricos",
    imagen: "flujogramas/24-meses-talla-78-peso-10-desnutricion-cronica.svg",
    alt: "Flujograma: Indicadores antropométricos"
  },
  "SP-154": {
    titulo: "Componentes del ASIS local",
    imagen: "flujogramas/asis-local-analisis-determinantes-sociales.svg",
    alt: "Flujograma: Componentes del ASIS local"
  },
  "CB-075": {
    titulo: "Fases de la cicatrización",
    imagen: "flujogramas/cicatrizacion-miofibroblastos-actina-miosina.svg",
    alt: "Flujograma: Fases de la cicatrización"
  },
  "PED-198": {
    titulo: "Trisomías autosómicas",
    imagen: "flujogramas/neonato-holoprosencefalia-polidactilia-labio-leporino-trisomia-13.svg",
    alt: "Flujograma: Trisomías autosómicas"
  },
  "GIN-210": {
    titulo: "Corioamnionitis en trabajo de parto avanzado",
    imagen: "flujogramas/35-semanas-rpm-fiebre-8-cm-antibiotico-parto-vaginal.svg",
    alt: "Flujograma: Corioamnionitis en trabajo de parto avanzado"
  },
  "CAR-066": {
    titulo: "Ritmos del paro cardiaco",
    imagen: "flujogramas/dea-actividad-electrica-no-desfibrilable-aesp.svg",
    alt: "Flujograma: Ritmos del paro cardiaco"
  },
  "SP-155": {
    titulo: "Herramientas del primer nivel",
    imagen: "flujogramas/control-prenatal-primer-nivel-radar-gestantes.svg",
    alt: "Flujograma: Herramientas del primer nivel"
  },
  "OFT-047": {
    titulo: "Causas de epistaxis anterior",
    imagen: "flujogramas/epistaxis-anterior-causa-rinitis-seca.svg",
    alt: "Flujograma: Causas de epistaxis anterior"
  },
  "PED-199": {
    titulo: "Fenotipos de sibilancias (Tucson)",
    imagen: "flujogramas/nina-sibilancias-desde-4-anos-atopia-inicio-tardio.svg",
    alt: "Flujograma: Fenotipos de sibilancias (Tucson)"
  },
  "GIN-211": {
    titulo: "Duración del sulfato de magnesio",
    imagen: "flujogramas/preeclampsia-severa-sulfato-magnesio-24-h-posparto.svg",
    alt: "Flujograma: Duración del sulfato de magnesio"
  },
  "NEU-061": {
    titulo: "Efectos adversos del esquema antituberculoso",
    imagen: "flujogramas/tratamiento-tb-fiebre-escalofrios-mialgia-rifampicina.svg",
    alt: "Flujograma: Efectos adversos del esquema antituberculoso"
  },
  "PED-200": {
    titulo: "Bronquiolitis: ¿casa u hospital?",
    imagen: "flujogramas/lactante-2-meses-bronquiolitis-tirajes-hospitalizar.svg",
    alt: "Flujograma: Bronquiolitis: ¿casa u hospital?"
  },
  "END-060": {
    titulo: "Dolor óseo con debilidad proximal",
    imagen: "flujogramas/trabajo-uci-sin-sol-calcio-fosforo-bajos-fa-alta-vitamina-d.svg",
    alt: "Flujograma: Dolor óseo con debilidad proximal"
  },
  "NEU-062": {
    titulo: "Antibiótico según dónde se trata la neumonía",
    imagen: "flujogramas/neumonia-confusa-fr-28-ceftriaxona-azitromicina.svg",
    alt: "Flujograma: Antibiótico según dónde se trata la neumonía"
  },
  "CIR-109": {
    titulo: "Abdomen agudo tras la colecistectomía",
    imagen: "flujogramas/colecistectomia-24-h-fiebre-rebote-peritonitis-biliar.svg",
    alt: "Flujograma: Abdomen agudo tras la colecistectomía"
  },
  "PED-201": {
    titulo: "Dolor abdominal en el escolar",
    imagen: "flujogramas/nino-7-anos-dolor-migra-fid-rebote-leucocitosis-apendicitis.svg",
    alt: "Flujograma: Dolor abdominal en el escolar"
  },
  "CIR-110": {
    titulo: "Quemadura de la vía aérea",
    imagen: "flujogramas/explosion-cocina-voz-ronca-esputo-carbonaceo-intubacion.svg",
    alt: "Flujograma: Quemadura de la vía aérea"
  },
  "GIN-212": {
    titulo: "Pelvimetría clínica",
    imagen: "flujogramas/pelvimetria-conjugado-10-5-pelvis-estrecha-cesarea.svg",
    alt: "Flujograma: Pelvimetría clínica"
  },
  "PSI-040": {
    titulo: "Maltrato psicológico infantil",
    imagen: "flujogramas/nino-humillado-insultado-por-padre-comunicar-autoridad.svg",
    alt: "Flujograma: Maltrato psicológico infantil"
  },
  "NEF-082": {
    titulo: "Falla renal con masa en hipogastrio",
    imagen: "flujogramas/colico-renal-previo-globo-vesical-oliguria-posrenal.svg",
    alt: "Flujograma: Falla renal con masa en hipogastrio"
  },
  "REU-061": {
    titulo: "Debilidad proximal con lesiones en los dedos",
    imagen: "flujogramas/debilidad-proximal-gottron-cpk-34000-biopsia-muscular.svg",
    alt: "Flujograma: Debilidad proximal con lesiones en los dedos"
  },
  "CIR-111": {
    titulo: "Trauma abdominal cerrado con peritonitis",
    imagen: "flujogramas/trauma-cerrado-hipotension-jobert-peritonitis-laparotomia.svg",
    alt: "Flujograma: Trauma abdominal cerrado con peritonitis"
  },
  "OFT-048": {
    titulo: "Tamizaje de retinopatía del prematuro",
    imagen: "flujogramas/prematura-32-semanas-oxigeno-retinopatia-primer-examen-4-semanas.svg",
    alt: "Flujograma: Tamizaje de retinopatía del prematuro"
  },
  "PED-202": {
    titulo: "Desdoblamiento fijo del segundo ruido",
    imagen: "flujogramas/nino-4-anos-acianotico-segundo-ruido-desdoblado-fijo-cia.svg",
    alt: "Flujograma: Desdoblamiento fijo del segundo ruido"
  },
  "GIN-213": {
    titulo: "FUR y ecografía no coinciden",
    imagen: "flujogramas/fur-42-eco-temprana-38-continuar-control-prenatal.svg",
    alt: "Flujograma: FUR y ecografía no coinciden"
  },
  "SP-156": {
    titulo: "Etapas de la planificación",
    imagen: "flujogramas/nuevo-director-presupuesto-planificacion-diagnostico.svg",
    alt: "Flujograma: Etapas de la planificación"
  },
  "SP-157": {
    titulo: "Prevenir el embarazo adolescente",
    imagen: "flujogramas/muerte-materna-adolescentes-educacion-sexual-colegios.svg",
    alt: "Flujograma: Prevenir el embarazo adolescente"
  },
  "PED-203": {
    titulo: "Tos con roncantes en el preescolar",
    imagen: "flujogramas/preescolar-tos-productiva-roncantes-bronquitis-aguda.svg",
    alt: "Flujograma: Tos con roncantes en el preescolar"
  },
  "NEF-083": {
    titulo: "Hipokalemia con ondas U",
    imagen: "flujogramas/mujer-baja-peso-debilidad-onda-u-laxantes-hipokalemia.svg",
    alt: "Flujograma: Hipokalemia con ondas U"
  },
  "GIN-214": {
    titulo: "Vacunas en la gestante",
    imagen: "flujogramas/gestante-20-semanas-vacuna-sarampion-contraindicada.svg",
    alt: "Flujograma: Vacunas en la gestante"
  },
  "OFT-049": {
    titulo: "Quemadura química ocular",
    imagen: "flujogramas/nino-lejia-ojo-queratitis-irrigacion-abundante.svg",
    alt: "Flujograma: Quemadura química ocular"
  },
  "GAS-067": {
    titulo: "Evaluación de la hepatitis C",
    imagen: "flujogramas/enfermera-pinchazo-vhc-arn-positivo-histologia-severidad.svg",
    alt: "Flujograma: Evaluación de la hepatitis C"
  },
  "PED-204": {
    titulo: "Recién nacido que empeora con la ventilación",
    imagen: "flujogramas/neonato-abdomen-excavado-empeora-con-ambu-intubar.svg",
    alt: "Flujograma: Recién nacido que empeora con la ventilación"
  },
  "SP-158": {
    titulo: "Salud ocupacional del personal nuevo",
    imagen: "flujogramas/personal-nuevo-hospital-capacitacion-control-infeccion-tb.svg",
    alt: "Flujograma: Salud ocupacional del personal nuevo"
  },
  "GIN-215": {
    titulo: "Tras una pielonefritis en el embarazo",
    imagen: "flujogramas/gestante-pielonefritis-previa-urocultivo-negativo-mensual.svg",
    alt: "Flujograma: Tras una pielonefritis en el embarazo"
  },
  "PED-205": {
    titulo: "Qué favorece y qué frena el surfactante",
    imagen: "flujogramas/prematuro-membrana-hialina-hipovolemia-inhibe-surfactante.svg",
    alt: "Flujograma: Qué favorece y qué frena el surfactante"
  },
  "CIR-112": {
    titulo: "Hemotórax traumático",
    imagen: "flujogramas/trauma-toracico-fracturas-costales-radiopacidad-hemotorax-drenaje.svg",
    alt: "Flujograma: Hemotórax traumático"
  },
  "GIN-216": {
    titulo: "Lactancia en la madre con VIH",
    imagen: "flujogramas/vih-escenario-3-cesarea-suprimir-lactancia-cabergolina.svg",
    alt: "Flujograma: Lactancia en la madre con VIH"
  },
  "NEU-063": {
    titulo: "Fiebre con opacidad pulmonar",
    imagen: "flujogramas/fiebre-tos-disnea-crepitantes-opacidad-neumonia.svg",
    alt: "Flujograma: Fiebre con opacidad pulmonar"
  },
  "PED-206": {
    titulo: "Plan C en el menor de 12 meses",
    imagen: "flujogramas/lactante-7-meses-deshidratacion-grave-plan-c-30-70.svg",
    alt: "Flujograma: Plan C en el menor de 12 meses"
  },
  "GIN-217": {
    titulo: "Pérdida gestacional temprana",
    imagen: "flujogramas/saco-29-mm-embrion-8-mm-sin-latido-misoprostol.svg",
    alt: "Flujograma: Pérdida gestacional temprana"
  },
  "CIR-113": {
    titulo: "Colecistitis aguda en la joven",
    imagen: "flujogramas/murphy-positivo-calculo-bacinete-colecistectomia-laparoscopica.svg",
    alt: "Flujograma: Colecistitis aguda en la joven"
  },
  "TRA-046": {
    titulo: "Deformidad del hombro tras una caída",
    imagen: "flujogramas/caida-mano-extendida-signo-charretera-luxacion-hombro.svg",
    alt: "Flujograma: Deformidad del hombro tras una caída"
  },
  "CAR-067": {
    titulo: "Compresiones de calidad",
    imagen: "flujogramas/rcp-calidad-5-cm-100-120-por-minuto.svg",
    alt: "Flujograma: Compresiones de calidad"
  },
  "GIN-218": {
    titulo: "Movimientos cardinales del parto",
    imagen: "flujogramas/dilatacion-completa-occipitoanterior-siguiente-extension.svg",
    alt: "Flujograma: Movimientos cardinales del parto"
  },
  "NRL-053": {
    titulo: "Escala de coma de Glasgow",
    imagen: "flujogramas/caida-4-piso-abre-ojos-dolor-flexion-sonidos-glasgow-7.svg",
    alt: "Flujograma: Escala de coma de Glasgow"
  },
  "SP-159": {
    titulo: "Tipos de mala praxis",
    imagen: "flujogramas/cesarea-medico-no-especialista-perfora-vejiga-impericia.svg",
    alt: "Flujograma: Tipos de mala praxis"
  },
  "CB-076": {
    titulo: "Energía durante el ejercicio prolongado",
    imagen: "flujogramas/maratonista-ejercicio-prolongado-gluconeogenesis-hepatica.svg",
    alt: "Flujograma: Energía durante el ejercicio prolongado"
  },
  "TRA-047": {
    titulo: "Qué hace el cuerpo ante la hemorragia",
    imagen: "flujogramas/hemorragia-activa-primer-signo-taquicardia.svg",
    alt: "Flujograma: Qué hace el cuerpo ante la hemorragia"
  },
  "PED-207": {
    titulo: "Lactante con VIH",
    imagen: "flujogramas/lactante-2-meses-vih-iniciar-tar-precoz.svg",
    alt: "Flujograma: Lactante con VIH"
  },
  "GAS-068": {
    titulo: "Ascitis con nódulos peritoneales",
    imagen: "flujogramas/ascitis-fiebre-nodulos-mijo-granulomas-caseosos-tb-peritoneal.svg",
    alt: "Flujograma: Ascitis con nódulos peritoneales"
  },
  "CB-077": {
    titulo: "Nervios del antebrazo",
    imagen: "flujogramas/fisicoculturista-debilidad-pronacion-nervio-mediano.svg",
    alt: "Flujograma: Nervios del antebrazo"
  },
  "NEU-064": {
    titulo: "Hipoxemia grave con infiltrados bilaterales",
    imagen: "flujogramas/infiltrados-bilaterales-sato2-78-sdra-shunt.svg",
    alt: "Flujograma: Hipoxemia grave con infiltrados bilaterales"
  },
  "PED-208": {
    titulo: "Duración del antibiótico en la meningitis neonatal",
    imagen: "flujogramas/neonato-meningitis-e-coli-21-dias.svg",
    alt: "Flujograma: Duración del antibiótico en la meningitis neonatal"
  },
  "GAS-069": {
    titulo: "Epigastralgia intensa en el alcohólico",
    imagen: "flujogramas/alcoholico-dolor-dorso-lipasa-alta-cullen-pancreatitis.svg",
    alt: "Flujograma: Epigastralgia intensa en el alcohólico"
  },
  "GIN-219": {
    titulo: "Interpretar el test estresante",
    imagen: "flujogramas/test-estresante-tres-contracciones-sin-desaceleraciones-negativo.svg",
    alt: "Flujograma: Interpretar el test estresante"
  },
  "NRL-054": {
    titulo: "Meningitis subaguda con pares craneales",
    imagen: "flujogramas/meningitis-subaguda-vi-par-lcr-linfocitico-glucosa-baja-tb.svg",
    alt: "Flujograma: Meningitis subaguda con pares craneales"
  },
  "SP-160": {
    titulo: "Rol de la comunidad frente al sarampión",
    imagen: "flujogramas/organizacion-comunal-sarampion-mensajes-educativos.svg",
    alt: "Flujograma: Rol de la comunidad frente al sarampión"
  },
  "GIN-220": {
    titulo: "Corticoides prenatales según las semanas",
    imagen: "flujogramas/amenaza-parto-pretermino-corticoides-24-36-semanas.svg",
    alt: "Flujograma: Corticoides prenatales según las semanas"
  },
  "PED-209": {
    titulo: "Ventana de la hipotermia terapéutica",
    imagen: "flujogramas/encefalopatia-hipoxica-moderada-hipotermia-antes-6-horas.svg",
    alt: "Flujograma: Ventana de la hipotermia terapéutica"
  },
  "GIN-221": {
    titulo: "Hierro y ácido fólico en la gestante",
    imagen: "flujogramas/gestante-14-semanas-hb-11-hierro-60-folico-400.svg",
    alt: "Flujograma: Hierro y ácido fólico en la gestante"
  },
  "CB-078": {
    titulo: "Digestión de las proteínas",
    imagen: "flujogramas/digestion-proteinas-inicia-pepsina.svg",
    alt: "Flujograma: Digestión de las proteínas"
  },
  "NEU-065": {
    titulo: "Neumoconiosis",
    imagen: "flujogramas/obrero-construccion-placas-pleurales-asbesto.svg",
    alt: "Flujograma: Neumoconiosis"
  },
  "OFT-050": {
    titulo: "Factores de riesgo del glaucoma",
    imagen: "flujogramas/glaucoma-factor-riesgo-presion-intraocular.svg",
    alt: "Flujograma: Factores de riesgo del glaucoma"
  },
  "HEM-041": {
    titulo: "¿Cómo se controla cada anticoagulante?",
    imagen: "flujogramas/control-warfarina-inr.svg",
    alt: "Flujograma: ¿Cómo se controla cada anticoagulante?"
  },
  "PED-210": {
    titulo: "Confirmar la anemia ferropénica",
    imagen: "flujogramas/lactante-12-meses-hb-9-7-ferritina-serica.svg",
    alt: "Flujograma: Confirmar la anemia ferropénica"
  },
  "INF-099": {
    titulo: "Recién nacido de madre con hepatitis B",
    imagen: "flujogramas/rn-madre-hbsag-positivo-vacuna-inmunoglobulina-12-h.svg",
    alt: "Flujograma: Recién nacido de madre con hepatitis B"
  },
  "CAR-068": {
    titulo: "Localización del infarto en el ECG",
    imagen: "flujogramas/st-elevado-dii-diii-avf-infarto-inferior.svg",
    alt: "Flujograma: Localización del infarto en el ECG"
  },
  "TRA-048": {
    titulo: "Pierna tensa tras un accidente",
    imagen: "flujogramas/pierna-dolor-extension-dedos-edema-pulso-debil-compartimental.svg",
    alt: "Flujograma: Pierna tensa tras un accidente"
  },
  "SP-161": {
    titulo: "Documentos de gestión",
    imagen: "flujogramas/microrred-morbimortalidad-priorizacion-asis.svg",
    alt: "Flujograma: Documentos de gestión"
  },
  "GAS-070": {
    titulo: "Pancreatitis biliar: primer paso",
    imagen: "flujogramas/litiasis-dolor-epigastrio-espalda-ictericia-hidratacion-ev.svg",
    alt: "Flujograma: Pancreatitis biliar: primer paso"
  },
  "NEF-084": {
    titulo: "Edema y orina espumosa en el lupus",
    imagen: "flujogramas/lupus-edema-orina-espumosa-proteinuria-24-horas.svg",
    alt: "Flujograma: Edema y orina espumosa en el lupus"
  },
  "REU-062": {
    titulo: "Placa inicial y erupción en árbol de navidad",
    imagen: "flujogramas/nino-medallon-heraldico-arbol-de-navidad-pitiriasis-rosada.svg",
    alt: "Flujograma: Placa inicial y erupción en árbol de navidad"
  },
  "GIN-222": {
    titulo: "Mioma pequeño y sin síntomas",
    imagen: "flujogramas/mioma-25-mm-asintomatico-perimenopausia-observacion.svg",
    alt: "Flujograma: Mioma pequeño y sin síntomas"
  },
  "INF-100": {
    titulo: "Úlceras genitales",
    imagen: "flujogramas/ulcera-vulvar-indolora-limpia-chancro-sifilis.svg",
    alt: "Flujograma: Úlceras genitales"
  },
  "NEU-066": {
    titulo: "Prueba broncodilatadora positiva",
    imagen: "flujogramas/espirometria-reversibilidad-vef1-12-200-ml.svg",
    alt: "Flujograma: Prueba broncodilatadora positiva"
  },
  "NRL-055": {
    titulo: "Deterioro cognitivo progresivo",
    imagen: "flujogramas/anciana-olvidos-se-pierde-no-reconoce-familia-demencia.svg",
    alt: "Flujograma: Deterioro cognitivo progresivo"
  },
  "PED-211": {
    titulo: "Cardiopatías con cianosis o sin ella",
    imagen: "flujogramas/rn-cianosis-al-llanto-corazon-en-bota-fallot.svg",
    alt: "Flujograma: Cardiopatías con cianosis o sin ella"
  },
  "SP-162": {
    titulo: "Indicadores de consulta externa",
    imagen: "flujogramas/9000-atendidos-18000-atenciones-concentracion-2.svg",
    alt: "Flujograma: Indicadores de consulta externa"
  },
  "PED-212": {
    titulo: "ITU febril en el lactante pequeño",
    imagen: "flujogramas/lactante-1-mes-itu-febril-ampicilina-amikacina.svg",
    alt: "Flujograma: ITU febril en el lactante pequeño"
  },
  "PED-213": {
    titulo: "Infecciones respiratorias y heces grasosas",
    imagen: "flujogramas/lactante-infecciones-repeticion-esteatorrea-fibrosis-quistica.svg",
    alt: "Flujograma: Infecciones respiratorias y heces grasosas"
  },
  "PED-214": {
    titulo: "Hemorragia intraventricular del prematuro",
    imagen: "flujogramas/prematuro-26-semanas-palidez-fontanela-hemorragia-intraventricular.svg",
    alt: "Flujograma: Hemorragia intraventricular del prematuro"
  },
  "NEF-085": {
    titulo: "Tratamiento de la hiperpotasemia",
    imagen: "flujogramas/falla-renal-t-picudas-qrs-ancho-gluconato-calcio.svg",
    alt: "Flujograma: Tratamiento de la hiperpotasemia"
  },
  "PED-215": {
    titulo: "Neumonía con derrame en el lactante",
    imagen: "flujogramas/lactante-neumonia-derrame-pleural-neumococo.svg",
    alt: "Flujograma: Neumonía con derrame en el lactante"
  },
  "SP-163": {
    titulo: "Pérdidas de seguimiento y potencia",
    imagen: "flujogramas/perdidas-seguimiento-menor-muestra-mas-error-beta.svg",
    alt: "Flujograma: Pérdidas de seguimiento y potencia"
  },
  "NRL-056": {
    titulo: "Parálisis facial tras un golpe temporal",
    imagen: "flujogramas/otorragia-hematoma-temporal-hemicara-flacida-vii-par.svg",
    alt: "Flujograma: Parálisis facial tras un golpe temporal"
  },
  "CAR-069": {
    titulo: "Tratamiento que reduce mortalidad en la IC",
    imagen: "flujogramas/icc-fevi-35-ieca-reduce-mortalidad.svg",
    alt: "Flujograma: Tratamiento que reduce mortalidad en la IC"
  },
  "TRA-049": {
    titulo: "Espalda asimétrica en la adolescente",
    imagen: "flujogramas/adolescente-hombros-desiguales-adams-escoliosis.svg",
    alt: "Flujograma: Espalda asimétrica en la adolescente"
  },
  "PSI-041": {
    titulo: "Tipos de psicosis",
    imagen: "flujogramas/joven-cree-hermanos-envian-ruido-envenenamiento-paranoide.svg",
    alt: "Flujograma: Tipos de psicosis"
  },
  "SP-164": {
    titulo: "Tasas de la población infantil",
    imagen: "flujogramas/30-muertes-menores-1-ano-600-nacidos-tmi-50.svg",
    alt: "Flujograma: Tasas de la población infantil"
  },
  "PED-216": {
    titulo: "Convulsión febril que no es simple",
    imagen: "flujogramas/lactante-convulsion-20-min-antibiotico-previo-puncion-lumbar.svg",
    alt: "Flujograma: Convulsión febril que no es simple"
  },
  "GIN-223": {
    titulo: "Estadificación POP-Q",
    imagen: "flujogramas/prolapso-ba-mas-5-lvt-6-popq-estadio-iv.svg",
    alt: "Flujograma: Estadificación POP-Q"
  },
  "GIN-224": {
    titulo: "Distocia de hombros",
    imagen: "flujogramas/macrosomico-diabetica-signo-tortuga-distocia-hombros.svg",
    alt: "Flujograma: Distocia de hombros"
  },
  "CAR-070": {
    titulo: "Efecto de los fármacos sobre la frecuencia",
    imagen: "flujogramas/taquicardia-supraventricular-cronotropico-negativo-bisoprolol.svg",
    alt: "Flujograma: Efecto de los fármacos sobre la frecuencia"
  },
  "REU-063": {
    titulo: "Escalones de tratamiento en la artritis reumatoide",
    imagen: "flujogramas/artritis-reumatoide-persiste-con-aine-metotrexato.svg",
    alt: "Flujograma: Escalones de tratamiento en la artritis reumatoide"
  },
  "GAS-071": {
    titulo: "Pancreatitis con suero lechoso",
    imagen: "flujogramas/suero-lechoso-dolor-epigastrico-hipertrigliceridemia-lipasa.svg",
    alt: "Flujograma: Pancreatitis con suero lechoso"
  },
  "INF-101": {
    titulo: "¿En qué TB se agregan corticoides?",
    imagen: "flujogramas/tuberculosis-meningea-corticoides-adyuvantes.svg",
    alt: "Flujograma: ¿En qué TB se agregan corticoides?"
  },
  "PED-217": {
    titulo: "Jarabes para la tos en lactantes",
    imagen: "flujogramas/lactante-jarabe-tos-somnolencia-depresion-respiratoria-codeina.svg",
    alt: "Flujograma: Jarabes para la tos en lactantes"
  },
  "GIN-225": {
    titulo: "Prevención del parto pretérmino",
    imagen: "flujogramas/parto-pretermino-previo-cervix-corto-progesterona.svg",
    alt: "Flujograma: Prevención del parto pretérmino"
  },
  "SP-165": {
    titulo: "Niveles de intervención",
    imagen: "flujogramas/lactancia-exclusiva-disminuye-promocion-salud.svg",
    alt: "Flujograma: Niveles de intervención"
  },
  "SP-166": {
    titulo: "Estrategias en la visita domiciliaria",
    imagen: "flujogramas/visita-domiciliaria-tb-mascarilla-ventilacion-educacion-salud.svg",
    alt: "Flujograma: Estrategias en la visita domiciliaria"
  },
  "NEU-067": {
    titulo: "Evolución del derrame infectado",
    imagen: "flujogramas/empiema-drenado-pulmon-no-reexpande-decorticacion.svg",
    alt: "Flujograma: Evolución del derrame infectado"
  },
  "SP-167": {
    titulo: "Desarrollo de un equipo (Tuckman)",
    imagen: "flujogramas/equipo-conflictos-lucha-control-tormenta.svg",
    alt: "Flujograma: Desarrollo de un equipo (Tuckman)"
  },
  "GIN-226": {
    titulo: "Shock séptico tras maniobras abortivas",
    imagen: "flujogramas/aborto-septico-hipotension-lactato-6-cristaloides.svg",
    alt: "Flujograma: Shock séptico tras maniobras abortivas"
  },
  "CAR-071": {
    titulo: "Confirmar el taponamiento",
    imagen: "flujogramas/herida-precordial-beck-ecocardiograma-taponamiento.svg",
    alt: "Flujograma: Confirmar el taponamiento"
  },
  "INF-102": {
    titulo: "Infección de piel con gas",
    imagen: "flujogramas/diabetico-pierna-crepitacion-gas-tc-fascitis-necrosante.svg",
    alt: "Flujograma: Infección de piel con gas"
  },
  "GIN-227": {
    titulo: "¿Cuándo dejar el tamizaje de cáncer de cuello?",
    imagen: "flujogramas/mujer-67-cotest-negativos-descontinuar-tamizaje-cervical.svg",
    alt: "Flujograma: ¿Cuándo dejar el tamizaje de cáncer de cuello?"
  },
  "GAS-072": {
    titulo: "Dolor recurrente en fosa ilíaca izquierda",
    imagen: "flujogramas/anciana-estrenida-dolor-fii-recurrente-tc-diverticulitis.svg",
    alt: "Flujograma: Dolor recurrente en fosa ilíaca izquierda"
  },
  "REU-064": {
    titulo: "Dolor generalizado con exámenes normales",
    imagen: "flujogramas/mujer-mialgias-generalizadas-fatiga-laboratorio-normal-fibromialgia.svg",
    alt: "Flujograma: Dolor generalizado con exámenes normales"
  },
  "NRL-057": {
    titulo: "ACV isquémico dentro de la ventana",
    imagen: "flujogramas/afasia-hemiparesia-1-hora-tc-normal-alteplasa.svg",
    alt: "Flujograma: ACV isquémico dentro de la ventana"
  },
  "SP-168": {
    titulo: "Pirámide de la evidencia",
    imagen: "flujogramas/revision-sistematica-metaanalisis-integra-estudios.svg",
    alt: "Flujograma: Pirámide de la evidencia"
  },
  "GIN-228": {
    titulo: "Tuberculosis mal tratada en el embarazo",
    imagen: "flujogramas/gestante-tb-pleural-tratamiento-irregular-bajo-peso.svg",
    alt: "Flujograma: Tuberculosis mal tratada en el embarazo"
  },
  "REU-065": {
    titulo: "Monoartritis del primer dedo",
    imagen: "flujogramas/podagra-tras-comida-alcohol-artritis-gotosa.svg",
    alt: "Flujograma: Monoartritis del primer dedo"
  },
  "GIN-229": {
    titulo: "Amenorrea: prueba con estrógenos y progestágenos",
    imagen: "flujogramas/amenorrea-sin-sangrado-tras-estrogenos-progestagenos-utero.svg",
    alt: "Flujograma: Amenorrea: prueba con estrógenos y progestágenos"
  },
  "END-061": {
    titulo: "Palpitaciones con un producto para adelgazar",
    imagen: "flujogramas/producto-adelgazar-taquicardia-temblor-sin-bocio-hormona-tiroidea.svg",
    alt: "Flujograma: Palpitaciones con un producto para adelgazar"
  },
  "GIN-230": {
    titulo: "Amenorrea primaria con talla baja",
    imagen: "flujogramas/amenorrea-primaria-talla-baja-cuello-alado-turner.svg",
    alt: "Flujograma: Amenorrea primaria con talla baja"
  },
  "INF-103": {
    titulo: "Diarrea tras antibióticos",
    imagen: "flujogramas/hospitalizada-ceftriaxona-clindamicina-diarrea-clostridioides.svg",
    alt: "Flujograma: Diarrea tras antibióticos"
  },
  "PED-218": {
    titulo: "Tipos de shock en el lactante",
    imagen: "flujogramas/lactante-fiebre-piel-moteada-pulso-debil-shock-distributivo.svg",
    alt: "Flujograma: Tipos de shock en el lactante"
  },
  "NEF-086": {
    titulo: "Tipo de lesión renal aguda",
    imagen: "flujogramas/diarrea-oliguria-fena-menor-1-cilindros-hialinos-prerrenal.svg",
    alt: "Flujograma: Tipo de lesión renal aguda"
  },
  "GIN-231": {
    titulo: "Vigilancia fetal a las 41 semanas",
    imagen: "flujogramas/41-semanas-expectante-nst-liquido-amniotico.svg",
    alt: "Flujograma: Vigilancia fetal a las 41 semanas"
  },
  "GIN-232": {
    titulo: "Masa vulvar dolorosa con fiebre",
    imagen: "flujogramas/fiebre-masa-vulvar-dolorosa-labio-mayor-absceso-bartolino.svg",
    alt: "Flujograma: Masa vulvar dolorosa con fiebre"
  },
  "END-062": {
    titulo: "Choque refractario en la puérpera",
    imagen: "flujogramas/puerpera-hemorragia-agalactia-choque-refractario-hidrocortisona.svg",
    alt: "Flujograma: Choque refractario en la puérpera"
  },
  "OFT-051": {
    titulo: "Ojo hinchado con fiebre",
    imagen: "flujogramas/picadura-parpado-fiebre-proptosis-diplopia-celulitis-orbitaria.svg",
    alt: "Flujograma: Ojo hinchado con fiebre"
  },
  "PED-219": {
    titulo: "Neonato que pierde mucho peso",
    imagen: "flujogramas/neonato-10-dias-perdida-12-sodio-158-deshidratacion-hipernatremica.svg",
    alt: "Flujograma: Neonato que pierde mucho peso"
  },
  "SP-169": {
    titulo: "Llegar a la población dispersa",
    imagen: "flujogramas/poblado-rural-disperso-cobertura-10-brigadas-itinerantes.svg",
    alt: "Flujograma: Llegar a la población dispersa"
  },
  "OFT-052": {
    titulo: "Destellos y cortina en el campo visual",
    imagen: "flujogramas/miope-destellos-moscas-cortina-desprendimiento-retina.svg",
    alt: "Flujograma: Destellos y cortina en el campo visual"
  },
  "GIN-233": {
    titulo: "Altura del útero según las semanas",
    imagen: "flujogramas/12-semanas-utero-borde-superior-pubis.svg",
    alt: "Flujograma: Altura del útero según las semanas"
  },
  "INF-104": {
    titulo: "Lectura del PPD según el paciente",
    imagen: "flujogramas/nino-vih-tuberculina-4-mm-negativa.svg",
    alt: "Flujograma: Lectura del PPD según el paciente"
  },
  "REU-066": {
    titulo: "Gravedad del acné",
    imagen: "flujogramas/adolescente-nodulos-quisticos-espalda-acne-grave.svg",
    alt: "Flujograma: Gravedad del acné"
  },
  "GAS-073": {
    titulo: "Antibiótico en la peritonitis bacteriana espontánea",
    imagen: "flujogramas/cirrotico-alergia-ceftriaxona-pbe-quinolona.svg",
    alt: "Flujograma: Antibiótico en la peritonitis bacteriana espontánea"
  },
  "CB-079": {
    titulo: "Enzimas de óxido-reducción",
    imagen: "flujogramas/catalasa-peroxidasa-peroxido-hidrogeno-antioxidante.svg",
    alt: "Flujograma: Enzimas de óxido-reducción"
  },
  "PED-220": {
    titulo: "Parásito con dos núcleos en heces",
    imagen: "flujogramas/trofozoito-dos-nucleos-diarrea-grasa-metronidazol.svg",
    alt: "Flujograma: Parásito con dos núcleos en heces"
  },
  "GIN-234": {
    titulo: "Saco gestacional sin embrión",
    imagen: "flujogramas/amenorrea-5-semanas-saco-10-mm-sin-embrion-control.svg",
    alt: "Flujograma: Saco gestacional sin embrión"
  },
  "TRA-050": {
    titulo: "Luxación de cadera y nervios",
    imagen: "flujogramas/luxacion-posterior-cadera-pie-caido-nervio-ciatico.svg",
    alt: "Flujograma: Luxación de cadera y nervios"
  },
  "CB-080": {
    titulo: "Fases de la cicatrización",
    imagen: "flujogramas/herida-cortante-proliferacion-fibroblasto-colageno.svg",
    alt: "Flujograma: Fases de la cicatrización"
  },
  "CB-081": {
    titulo: "Toxicidad por anestésicos locales",
    imagen: "flujogramas/lidocaina-parestesia-peribucal-desorientacion-oxigeno.svg",
    alt: "Flujograma: Toxicidad por anestésicos locales"
  },
  "NRL-058": {
    titulo: "Escala de coma de Glasgow",
    imagen: "flujogramas/motociclista-ojos-al-dolor-sonidos-retira-glasgow-8.svg",
    alt: "Flujograma: Escala de coma de Glasgow"
  },
  "PED-221": {
    titulo: "Estadios de Sarnat",
    imagen: "flujogramas/dpp-neonato-sarnat-iii-ph-6-5-hipotermia.svg",
    alt: "Flujograma: Estadios de Sarnat"
  },
  "PED-222": {
    titulo: "Anemia microcítica en el lactante",
    imagen: "flujogramas/lactante-11-meses-hb-9-ferritina-baja-hierro.svg",
    alt: "Flujograma: Anemia microcítica en el lactante"
  },
  "PED-223": {
    titulo: "Lesiones del síndrome nefrótico",
    imagen: "flujogramas/sindrome-nefrotico-nino-podocitos-cambios-minimos.svg",
    alt: "Flujograma: Lesiones del síndrome nefrótico"
  },
  "SP-170": {
    titulo: "Principios bioéticos",
    imagen: "flujogramas/irc-avanzada-gestante-junta-medica-aborto-terapeutico.svg",
    alt: "Flujograma: Principios bioéticos"
  },
  "SP-171": {
    titulo: "Parto con pertinencia cultural",
    imagen: "flujogramas/parto-andino-pertinencia-cultural-entrega-placenta.svg",
    alt: "Flujograma: Parto con pertinencia cultural"
  },
  "CB-082": {
    titulo: "Antibióticos y efectos adversos",
    imagen: "flujogramas/insuficiencia-renal-pielonefritis-convulsiones-imipenem.svg",
    alt: "Flujograma: Antibióticos y efectos adversos"
  },
  "SP-172": {
    titulo: "Fases del ensayo clínico",
    imagen: "flujogramas/ensayo-clinico-poscomercializacion-farmacovigilancia-fase-iv.svg",
    alt: "Flujograma: Fases del ensayo clínico"
  },
  "SP-173": {
    titulo: "Enfoques del cuidado integral",
    imagen: "flujogramas/modelo-cuidado-integral-enfoques-interculturalidad.svg",
    alt: "Flujograma: Enfoques del cuidado integral"
  },
  "GIN-235": {
    titulo: "Compartimentos del prolapso",
    imagen: "flujogramas/histerectomia-vaginal-previa-punto-c-mas-6-cupula.svg",
    alt: "Flujograma: Compartimentos del prolapso"
  },
  "SP-174": {
    titulo: "Principios de la bioética",
    imagen: "flujogramas/cirujano-curacion-sin-guantes-no-maleficencia.svg",
    alt: "Flujograma: Principios de la bioética"
  },
  "CB-083": {
    titulo: "Tipos de hipersensibilidad",
    imagen: "flujogramas/amoxicilina-30-minutos-habones-hipersensibilidad-tipo-i.svg",
    alt: "Flujograma: Tipos de hipersensibilidad"
  },
  "PSI-042": {
    titulo: "Alteraciones por vómitos",
    imagen: "flujogramas/atracones-vomitos-autoprovocados-arritmia-hipopotasemia.svg",
    alt: "Flujograma: Alteraciones por vómitos"
  },
  "CIR-114": {
    titulo: "Accesos arteriales percutáneos",
    imagen: "flujogramas/injerto-arterial-acceso-percutaneo-femoral-comun.svg",
    alt: "Flujograma: Accesos arteriales percutáneos"
  },
  "NEF-087": {
    titulo: "Masa testicular sólida",
    imagen: "flujogramas/criptorquidia-operada-masa-testicular-solida-bhcg.svg",
    alt: "Flujograma: Masa testicular sólida"
  },
  "SP-175": {
    titulo: "Consentimiento informado",
    imagen: "flujogramas/codigo-etica-riesgo-mayor-consentimiento-escrito.svg",
    alt: "Flujograma: Consentimiento informado"
  },
  "INF-105": {
    titulo: "Accidente con material cortante",
    imagen: "flujogramas/interno-corte-palma-emergencia-exposicion-ocupacional.svg",
    alt: "Flujograma: Accidente con material cortante"
  },
  "INF-106": {
    titulo: "Etapas de la sífilis",
    imagen: "flujogramas/chancro-curado-papulas-palmares-rpr-1-320-benzatinica.svg",
    alt: "Flujograma: Etapas de la sífilis"
  },
  "GIN-236": {
    titulo: "Preeclampsia con signos de severidad",
    imagen: "flujogramas/gestante-36-semanas-epigastralgia-i3-magnesio-referencia.svg",
    alt: "Flujograma: Preeclampsia con signos de severidad"
  },
  "NEF-088": {
    titulo: "Manejo del cólico renal",
    imagen: "flujogramas/colico-lumbar-irradiado-genitales-analgesia-aine.svg",
    alt: "Flujograma: Manejo del cólico renal"
  },
  "TRA-051": {
    titulo: "Tiempos en la fractura abierta",
    imagen: "flujogramas/fractura-expuesta-antibiotico-primera-hora.svg",
    alt: "Flujograma: Tiempos en la fractura abierta"
  },
  "NEF-089": {
    titulo: "Pielonefritis que no mejora",
    imagen: "flujogramas/pielonefritis-10-dias-persiste-fiebre-absceso-renal.svg",
    alt: "Flujograma: Pielonefritis que no mejora"
  },
  "NEU-068": {
    titulo: "Neumonía típica y atípica",
    imagen: "flujogramas/neumonia-atipica-mycoplasma-sin-pared-azitromicina.svg",
    alt: "Flujograma: Neumonía típica y atípica"
  },
  "SP-176": {
    titulo: "Categorías del primer nivel",
    imagen: "flujogramas/establecimiento-i4-upss-obligatoria-patologia-clinica.svg",
    alt: "Flujograma: Categorías del primer nivel"
  },
  "CB-084": {
    titulo: "Evolución del loxoscelismo",
    imagen: "flujogramas/jardin-lesion-necrotica-hemolisis-anuria-loxosceles.svg",
    alt: "Flujograma: Evolución del loxoscelismo"
  },
  "TRA-052": {
    titulo: "Fractura supracondílea en el adulto mayor",
    imagen: "flujogramas/anciana-caida-codo-supracondilea-no-desplazada-ferula-90.svg",
    alt: "Flujograma: Fractura supracondílea en el adulto mayor"
  },
  "CB-085": {
    titulo: "Células del hueso y la médula",
    imagen: "flujogramas/medula-osea-celula-gigante-multinucleada-resorcion.svg",
    alt: "Flujograma: Células del hueso y la médula"
  },
  "SP-177": {
    titulo: "Intervenciones contra el dengue",
    imagen: "flujogramas/asentamientos-sin-agua-potable-dengue-determinantes.svg",
    alt: "Flujograma: Intervenciones contra el dengue"
  },
  "REU-067": {
    titulo: "Riesgo de cáncer de piel",
    imagen: "flujogramas/militares-jovenes-sol-cancer-piel-ultravioleta.svg",
    alt: "Flujograma: Riesgo de cáncer de piel"
  },
  "END-063": {
    titulo: "¿Cuándo iniciar con insulina?",
    imagen: "flujogramas/poliuria-baja-12-kg-glucosa-472-hba1c-12-insulina.svg",
    alt: "Flujograma: ¿Cuándo iniciar con insulina?"
  },
  "INF-107": {
    titulo: "Vacuna antiamarílica",
    imagen: "flujogramas/serumista-chanchamayo-vacuna-amarilla-10-dias.svg",
    alt: "Flujograma: Vacuna antiamarílica"
  },
  "PED-224": {
    titulo: "Diarrea con sangre en el niño",
    imagen: "flujogramas/hamburguesa-disenteria-anemia-plaquetopenia-e-coli.svg",
    alt: "Flujograma: Diarrea con sangre en el niño"
  },
  "GIN-237": {
    titulo: "Test no estresante",
    imagen: "flujogramas/nst-20-minutos-aceleraciones-sin-desaceleraciones-reactivo.svg",
    alt: "Flujograma: Test no estresante"
  },
  "GIN-238": {
    titulo: "Puntos del POP-Q",
    imagen: "flujogramas/popq-punto-aa-union-uretrovesical.svg",
    alt: "Flujograma: Puntos del POP-Q"
  },
  "CIR-115": {
    titulo: "Gravedad de la trombosis venosa",
    imagen: "flujogramas/postrado-pierna-blanca-edema-masivo-flegmasia-alba.svg",
    alt: "Flujograma: Gravedad de la trombosis venosa"
  },
  "PED-225": {
    titulo: "Duración del antibiótico en la otitis",
    imagen: "flujogramas/lactante-18-meses-oma-amoxicilina-10-dias.svg",
    alt: "Flujograma: Duración del antibiótico en la otitis"
  },
  "GIN-239": {
    titulo: "Complicaciones del HELLP",
    imagen: "flujogramas/preeclampsia-hellp-plaquetas-80000-desprendimiento.svg",
    alt: "Flujograma: Complicaciones del HELLP"
  },
  "INF-108": {
    titulo: "Proctitis de transmisión sexual",
    imagen: "flujogramas/coito-anal-receptivo-tenesmo-secrecion-gonococo.svg",
    alt: "Flujograma: Proctitis de transmisión sexual"
  },
  "SP-178": {
    titulo: "Educación escolar en dengue",
    imagen: "flujogramas/colegio-programa-escolar-dengue-eliminar-criaderos.svg",
    alt: "Flujograma: Educación escolar en dengue"
  },
  "NEU-069": {
    titulo: "Hemoptisis en el fumador",
    imagen: "flujogramas/albanil-fumador-hemoptisis-sibilancia-unilateral-tac.svg",
    alt: "Flujograma: Hemoptisis en el fumador"
  },
  "CB-086": {
    titulo: "Orina roja tras un antídoto",
    imagen: "flujogramas/bombero-humo-plasticos-hidroxicobalamina-orina-roja.svg",
    alt: "Flujograma: Orina roja tras un antídoto"
  },
  "TRA-053": {
    titulo: "Fractura de pelvis con shock",
    imagen: "flujogramas/atropello-pelvis-inestable-shock-faja-pelvica.svg",
    alt: "Flujograma: Fractura de pelvis con shock"
  },
  "GIN-240": {
    titulo: "Control de la diabetes gestacional",
    imagen: "flujogramas/diabetes-gestacional-ayunas-130-insulina.svg",
    alt: "Flujograma: Control de la diabetes gestacional"
  },
  "INF-109": {
    titulo: "Evolución del tratamiento de TB",
    imagen: "flujogramas/tb-sensible-cuarto-mes-bk-positiva-fracaso.svg",
    alt: "Flujograma: Evolución del tratamiento de TB"
  },
  "CIR-116": {
    titulo: "Dolor perianal con fiebre",
    imagen: "flujogramas/chofer-dolor-perianal-fiebre-masa-fluctuante-drenaje.svg",
    alt: "Flujograma: Dolor perianal con fiebre"
  },
  "END-064": {
    titulo: "Diagnóstico de diabetes",
    imagen: "flujogramas/obeso-glucemias-153-146-diabetes-metformina.svg",
    alt: "Flujograma: Diagnóstico de diabetes"
  },
  "PED-226": {
    titulo: "Hipoglucemia del hijo de madre diabética",
    imagen: "flujogramas/hijo-madre-diabetica-hiperinsulinismo-hipoglucemia.svg",
    alt: "Flujograma: Hipoglucemia del hijo de madre diabética"
  },
  "NEU-070": {
    titulo: "Gravedad de la exacerbación de EPOC",
    imagen: "flujogramas/epoc-ph-7-29-pco2-65-oxigeno-controlado.svg",
    alt: "Flujograma: Gravedad de la exacerbación de EPOC"
  },
  "NEF-090": {
    titulo: "Dónde se detienen los cálculos",
    imagen: "flujogramas/estrechamientos-ureter-calculo-union-ureterovesical.svg",
    alt: "Flujograma: Dónde se detienen los cálculos"
  },
  "PED-227": {
    titulo: "Cardiopatías congénitas",
    imagen: "flujogramas/cia-civ-pca-hiperflujo-pulmonar-qp-qs.svg",
    alt: "Flujograma: Cardiopatías congénitas"
  },
  "PED-228": {
    titulo: "Reacción tras la primera fórmula",
    imagen: "flujogramas/lactante-40-dias-formula-urticaria-sibilancias-aplv.svg",
    alt: "Flujograma: Reacción tras la primera fórmula"
  },
  "OFT-053": {
    titulo: "Tipos de conjuntivitis",
    imagen: "flujogramas/piscina-cloro-ardor-ojo-rojo-conjuntivitis-quimica.svg",
    alt: "Flujograma: Tipos de conjuntivitis"
  },
  "PED-229": {
    titulo: "Regurgitación y falla de crecimiento",
    imagen: "flujogramas/lactante-regurgitacion-asfixia-pico-de-pajaro-acalasia.svg",
    alt: "Flujograma: Regurgitación y falla de crecimiento"
  },
  "SP-179": {
    titulo: "Estilos de liderazgo",
    imagen: "flujogramas/jefe-impone-ordenes-sin-opinion-autoritario.svg",
    alt: "Flujograma: Estilos de liderazgo"
  },
  "CIR-117": {
    titulo: "Trombosis hemorroidal según el tiempo",
    imagen: "flujogramas/dolor-anal-subito-nodulo-purpura-trombectomia.svg",
    alt: "Flujograma: Trombosis hemorroidal según el tiempo"
  },
  "CAR-072": {
    titulo: "Hipovolemia por diurético",
    imagen: "flujogramas/insuficiencia-cardiaca-mareo-lengua-seca-suspender-furosemida.svg",
    alt: "Flujograma: Hipovolemia por diurético"
  },
  "SP-180": {
    titulo: "Mortalidad materna rural",
    imagen: "flujogramas/poblado-rural-300-habitantes-mortalidad-materna-vigilancia.svg",
    alt: "Flujograma: Mortalidad materna rural"
  },
  "GIN-241": {
    titulo: "Tipos de aborto",
    imagen: "flujogramas/embrion-8-mm-sin-latido-cuello-cerrado-aborto-retenido.svg",
    alt: "Flujograma: Tipos de aborto"
  },
  "PED-230": {
    titulo: "Gravedad del escorpionismo",
    imagen: "flujogramas/alacran-sialorrea-nistagmo-dificultad-respiratoria-faboterapia.svg",
    alt: "Flujograma: Gravedad del escorpionismo"
  },
  "CIR-118": {
    titulo: "Evolución de la apendicitis complicada",
    imagen: "flujogramas/plastron-apendicular-7-dias-sin-absceso-conservador.svg",
    alt: "Flujograma: Evolución de la apendicitis complicada"
  },
  "CB-087": {
    titulo: "Intoxicación con depresión respiratoria",
    imagen: "flujogramas/alprazolam-licor-glasgow-10-fr-8-via-aerea.svg",
    alt: "Flujograma: Intoxicación con depresión respiratoria"
  },
  "NEF-091": {
    titulo: "Alteraciones de la ERC avanzada",
    imagen: "flujogramas/pielonefritis-repeticion-fg-12-hiperpotasemia-acidosis.svg",
    alt: "Flujograma: Alteraciones de la ERC avanzada"
  },
  "END-065": {
    titulo: "Potasio e insulina en la cetoacidosis",
    imagen: "flujogramas/cetoacidosis-potasio-3-2-reponer-antes-insulina.svg",
    alt: "Flujograma: Potasio e insulina en la cetoacidosis"
  },
  "OFT-054": {
    titulo: "Tipos de glaucoma",
    imagen: "flujogramas/corticoide-topico-prolongado-glaucoma-secundario.svg",
    alt: "Flujograma: Tipos de glaucoma"
  },
  "CB-088": {
    titulo: "Efectos adversos de antibióticos",
    imagen: "flujogramas/itu-anciano-ambos-aquiles-dolor-ciprofloxacino.svg",
    alt: "Flujograma: Efectos adversos de antibióticos"
  },
  "CB-089": {
    titulo: "Mecanismo de los anticoagulantes",
    imagen: "flujogramas/fibrilacion-auricular-apixaban-factor-xa.svg",
    alt: "Flujograma: Mecanismo de los anticoagulantes"
  },
  "REU-068": {
    titulo: "Artritis por cristales",
    imagen: "flujogramas/rodilla-cristales-romboides-condrocalcinosis-pseudogota.svg",
    alt: "Flujograma: Artritis por cristales"
  },
  "SP-181": {
    titulo: "Determinantes en la adolescente",
    imagen: "flujogramas/inmigrante-13-anos-llanto-abandono-paterno-familia.svg",
    alt: "Flujograma: Determinantes en la adolescente"
  },
  "NRL-059": {
    titulo: "Neurotransmisor del Parkinson",
    imagen: "flujogramas/parkinson-recaidas-perdida-neuronas-dopaminergicas.svg",
    alt: "Flujograma: Neurotransmisor del Parkinson"
  },
  "GIN-242": {
    titulo: "Después del metotrexato",
    imagen: "flujogramas/ectopico-metotrexato-exitoso-esperar-3-meses.svg",
    alt: "Flujograma: Después del metotrexato"
  },
  "GAS-074": {
    titulo: "Criterios del síndrome hepatorrenal",
    imagen: "flujogramas/cirrosis-hda-creatinina-1-6-sodio-urinario-8-hepatorrenal.svg",
    alt: "Flujograma: Criterios del síndrome hepatorrenal"
  },
  "END-066": {
    titulo: "Mecanismo de los antidiabéticos",
    imagen: "flujogramas/diabetico-gliflozina-sglt2-glucosuria.svg",
    alt: "Flujograma: Mecanismo de los antidiabéticos"
  },
  "NEF-092": {
    titulo: "Coma por hipernatremia",
    imagen: "flujogramas/liposuccion-sodio-187-convulsiones-deshidratacion-neuronal.svg",
    alt: "Flujograma: Coma por hipernatremia"
  },
  "SP-182": {
    titulo: "Intervención ante la mala adherencia",
    imagen: "flujogramas/diabetes-30-por-ciento-sin-adherencia-programa-educativo.svg",
    alt: "Flujograma: Intervención ante la mala adherencia"
  },
  "CAR-073": {
    titulo: "Dolor torácico con infradesnivel del ST",
    imagen: "flujogramas/fumador-dolor-reposo-infradesnivel-st-scasest.svg",
    alt: "Flujograma: Dolor torácico con infradesnivel del ST"
  },
  "PED-231": {
    titulo: "Diagnóstico de VIH en el lactante",
    imagen: "flujogramas/lactante-expuesto-vih-pcr-positiva-dos-veces-tar.svg",
    alt: "Flujograma: Diagnóstico de VIH en el lactante"
  },
  "INF-110": {
    titulo: "Úlceras genitales y adenopatías",
    imagen: "flujogramas/hsh-papula-indolora-bubones-fistulas-linfogranuloma.svg",
    alt: "Flujograma: Úlceras genitales y adenopatías"
  },
  "GAS-075": {
    titulo: "Estudio del líquido ascítico",
    imagen: "flujogramas/ascitis-gasa-1-4-hipertension-portal.svg",
    alt: "Flujograma: Estudio del líquido ascítico"
  },
  "CIR-119": {
    titulo: "Escala AIR en la apendicitis",
    imagen: "flujogramas/dolor-migratorio-blumberg-air-9-cirugia.svg",
    alt: "Flujograma: Escala AIR en la apendicitis"
  },
  "CIR-120": {
    titulo: "Maniobras vasculares",
    imagen: "flujogramas/prueba-trendelenburg-torniquete-varices.svg",
    alt: "Flujograma: Maniobras vasculares"
  },
  "SP-183": {
    titulo: "Prevención de la obesidad infantil",
    imagen: "flujogramas/periurbano-ultraprocesados-obesidad-infantil-regular-publicidad.svg",
    alt: "Flujograma: Prevención de la obesidad infantil"
  },
  "INF-111": {
    titulo: "Tratamiento de la disentería",
    imagen: "flujogramas/adulto-disenteria-fiebre-leucocitos-fecales-ciprofloxacino.svg",
    alt: "Flujograma: Tratamiento de la disentería"
  },
  "NEF-093": {
    titulo: "Riesgo de nefropatía por contraste",
    imagen: "flujogramas/cateterismo-diabetico-erc-contraste-lesion-renal.svg",
    alt: "Flujograma: Riesgo de nefropatía por contraste"
  },
  "CB-090": {
    titulo: "Qué pasa en el ayuno",
    imagen: "flujogramas/deficit-mcad-ayuno-movimientos-hipoglucemia.svg",
    alt: "Flujograma: Qué pasa en el ayuno"
  },
  "PED-232": {
    titulo: "Ictericia en el neonato sano",
    imagen: "flujogramas/neonato-8-dias-lactancia-bilirrubina-12-observacion.svg",
    alt: "Flujograma: Ictericia en el neonato sano"
  },
  "GIN-243": {
    titulo: "Tocolíticos y contraindicaciones",
    imagen: "flujogramas/amenaza-parto-pretermino-nifedipino-insuficiencia-cardiaca.svg",
    alt: "Flujograma: Tocolíticos y contraindicaciones"
  },
  "SP-184": {
    titulo: "Técnicas de control en gestión",
    imagen: "flujogramas/inmunizaciones-visita-acta-reunion-mejora-supervision.svg",
    alt: "Flujograma: Técnicas de control en gestión"
  },
  "GAS-076": {
    titulo: "Probabilidad de coledocolitiasis",
    imagen: "flujogramas/pancreatitis-previas-ictericia-bilirrubina-4-2-coledocolitiasis.svg",
    alt: "Flujograma: Probabilidad de coledocolitiasis"
  },
  "PED-233": {
    titulo: "Signos del raquitismo",
    imagen: "flujogramas/lactancia-sin-suplemento-rosario-costal-raquitismo.svg",
    alt: "Flujograma: Signos del raquitismo"
  },
  "GIN-244": {
    titulo: "Causa materna de macrosomía",
    imagen: "flujogramas/distocia-hombros-macrosomia-diabetes-gestacional.svg",
    alt: "Flujograma: Causa materna de macrosomía"
  },
  "PED-234": {
    titulo: "Escala de Westley",
    imagen: "flujogramas/tos-perruna-estridor-solo-al-llanto-crup-leve.svg",
    alt: "Flujograma: Escala de Westley"
  },
  "SP-185": {
    titulo: "Tipos de factores de salud",
    imagen: "flujogramas/quechuahablante-obesa-hipertensa-nivel-socioeconomico.svg",
    alt: "Flujograma: Tipos de factores de salud"
  },
  "CB-091": {
    titulo: "Neurodesarrollo embrionario",
    imagen: "flujogramas/embrion-8-semanas-movimientos-primeros-tractos-nerviosos.svg",
    alt: "Flujograma: Neurodesarrollo embrionario"
  },
  "END-067": {
    titulo: "Causa del síndrome de Cushing",
    imagen: "flujogramas/grasa-centripeta-acne-hirsutismo-dexametasona-cushing.svg",
    alt: "Flujograma: Causa del síndrome de Cushing"
  },
  "INF-112": {
    titulo: "Estadios del cisticerco",
    imagen: "flujogramas/huancayo-convulsion-quistes-viables-albendazol.svg",
    alt: "Flujograma: Estadios del cisticerco"
  },
  "PED-235": {
    titulo: "Cianosis tras los pasos iniciales",
    imagen: "flujogramas/neonato-fc-110-respira-bien-cianosis-oxigeno.svg",
    alt: "Flujograma: Cianosis tras los pasos iniciales"
  },
  "SP-186": {
    titulo: "Mitos y verdades de la promoción",
    imagen: "flujogramas/promocion-salud-mito-impone-estilos-de-vida.svg",
    alt: "Flujograma: Mitos y verdades de la promoción"
  },
  "GIN-245": {
    titulo: "Puntaje de Bishop",
    imagen: "flujogramas/bishop-posicion-media-borramiento-50-dilatacion-2.svg",
    alt: "Flujograma: Puntaje de Bishop"
  },
  "CIR-121": {
    titulo: "Úlcera anal fuera de la línea media",
    imagen: "flujogramas/tb-pulmonar-ulcera-anal-lateral-tuberculosa.svg",
    alt: "Flujograma: Úlcera anal fuera de la línea media"
  },
  "SP-187": {
    titulo: "Estrategias en comunidades aisladas",
    imagen: "flujogramas/comunidad-indigena-24-horas-rio-agentes-comunitarios-lactancia.svg",
    alt: "Flujograma: Estrategias en comunidades aisladas"
  },
  "CB-092": {
    titulo: "Tipos de insulina",
    imagen: "flujogramas/dm2-severa-dos-insulinas-velocidad-absorcion.svg",
    alt: "Flujograma: Tipos de insulina"
  },
  "GAS-077": {
    titulo: "Tipos de hepatitis autoinmune",
    imagen: "flujogramas/dm1-hipotiroidismo-hepatitis-ana-sma-autoinmune-tipo-1.svg",
    alt: "Flujograma: Tipos de hepatitis autoinmune"
  },
  "CAR-074": {
    titulo: "Clase funcional NYHA",
    imagen: "flujogramas/hipertensa-disnea-segundo-piso-nyha-clase-ii.svg",
    alt: "Flujograma: Clase funcional NYHA"
  },
  "CIR-122": {
    titulo: "Hernia umbilical encarcelada",
    imagen: "flujogramas/hernia-umbilical-4-cm-reducida-sin-isquemia-electiva.svg",
    alt: "Flujograma: Hernia umbilical encarcelada"
  },
  "PED-236": {
    titulo: "Varicela complicada",
    imagen: "flujogramas/varicela-sato2-89-crepitos-aciclovir-ev.svg",
    alt: "Flujograma: Varicela complicada"
  },
  "CIR-123": {
    titulo: "Gérmenes de la vía biliar",
    imagen: "flujogramas/colecistitis-complicada-leucocitosis-gramnegativos-anaerobios.svg",
    alt: "Flujograma: Gérmenes de la vía biliar"
  },
  "GAS-078": {
    titulo: "Cómo se produce la pancreatitis",
    imagen: "flujogramas/calculo-ampolla-vater-tripsinogeno-activado-pancreatitis.svg",
    alt: "Flujograma: Cómo se produce la pancreatitis"
  },
  "SP-188": {
    titulo: "Asignación de recursos escasos",
    imagen: "flujogramas/pandemia-dos-ventiladores-cuatro-pacientes-pronostico.svg",
    alt: "Flujograma: Asignación de recursos escasos"
  },
  "PED-237": {
    titulo: "Tratamiento de la oxiuriasis",
    imagen: "flujogramas/prurito-anal-nocturno-graham-positivo-albendazol.svg",
    alt: "Flujograma: Tratamiento de la oxiuriasis"
  },
  "PED-238": {
    titulo: "Exantemas del lactante",
    imagen: "flujogramas/lactante-10-meses-exantema-al-ceder-fiebre-roseola.svg",
    alt: "Flujograma: Exantemas del lactante"
  },
  "SP-189": {
    titulo: "Niveles de investigación",
    imagen: "flujogramas/objetivo-evaluar-controlar-calibrar-nivel-aplicativo.svg",
    alt: "Flujograma: Niveles de investigación"
  },
  "NRL-060": {
    titulo: "Efectos adversos antiparkinsonianos",
    imagen: "flujogramas/parkinson-77-anos-confusion-memoria-biperideno.svg",
    alt: "Flujograma: Efectos adversos antiparkinsonianos"
  },
  "SP-190": {
    titulo: "Promoción contra la anemia",
    imagen: "flujogramas/comunidad-agricola-anemia-sesiones-demostrativas.svg",
    alt: "Flujograma: Promoción contra la anemia"
  },
  "CIR-124": {
    titulo: "Trauma hepático en el niño",
    imagen: "flujogramas/nino-transito-hematoma-subcapsular-hepatico-2-cm-observacion.svg",
    alt: "Flujograma: Trauma hepático en el niño"
  },
  "PED-239": {
    titulo: "Riesgo de displasia broncopulmonar",
    imagen: "flujogramas/prematuro-27-semanas-oxigeno-28-dias-displasia.svg",
    alt: "Flujograma: Riesgo de displasia broncopulmonar"
  },
  "GIN-246": {
    titulo: "Actividad uterina",
    imagen: "flujogramas/trabajo-parto-6-7-contracciones-10-minutos-taquisistolia.svg",
    alt: "Flujograma: Actividad uterina"
  },
  "GIN-247": {
    titulo: "Prueba de tolerancia a la glucosa",
    imagen: "flujogramas/ptgo-90-160-140-gestante-no-diabetica.svg",
    alt: "Flujograma: Prueba de tolerancia a la glucosa"
  },
  "PED-240": {
    titulo: "Signos de un buen agarre",
    imagen: "flujogramas/puerpera-pezones-agrietados-labios-no-evertidos-agarre.svg",
    alt: "Flujograma: Signos de un buen agarre"
  },
  "INF-113": {
    titulo: "Clasificación del caso de dengue",
    imagen: "flujogramas/fiebre-retroocular-dengue-sin-viajes-aedes-autoctono.svg",
    alt: "Flujograma: Clasificación del caso de dengue"
  },
  "NRL-061": {
    titulo: "Parálisis oculomotoras",
    imagen: "flujogramas/fractura-base-craneo-midriasis-ojo-abajo-afuera-iii-par.svg",
    alt: "Flujograma: Parálisis oculomotoras"
  },
  "OFT-055": {
    titulo: "Cuerpo extraño ocular",
    imagen: "flujogramas/soldador-esquirla-corneal-retiro-antibiotico.svg",
    alt: "Flujograma: Cuerpo extraño ocular"
  },
  "SP-191": {
    titulo: "Elegir la prueba estadística",
    imagen: "flujogramas/leishmaniasis-ocupacion-forma-clinica-chi-cuadrado.svg",
    alt: "Flujograma: Elegir la prueba estadística"
  },
  "INF-114": {
    titulo: "Contacto con PPD positivo",
    imagen: "flujogramas/contacto-bacilifero-ppd-22-rx-normal-isoniazida.svg",
    alt: "Flujograma: Contacto con PPD positivo"
  },
  "END-068": {
    titulo: "Riesgo de agranulocitosis",
    imagen: "flujogramas/graves-tiamazol-fiebre-odinofagia-hemograma-urgente.svg",
    alt: "Flujograma: Riesgo de agranulocitosis"
  },
  "SP-192": {
    titulo: "Ante la falta ética de un colega",
    imagen: "flujogramas/medico-obliga-grabar-agradecimientos-consejo-regional.svg",
    alt: "Flujograma: Ante la falta ética de un colega"
  },
  "PED-241": {
    titulo: "Polihidramnios y deglución fetal",
    imagen: "flujogramas/polihidramnios-hospital-nivel-iii-atresia-esofago.svg",
    alt: "Flujograma: Polihidramnios y deglución fetal"
  },
  "CB-093": {
    titulo: "Barbitúricos según su duración",
    imagen: "flujogramas/barbituricos-tiopental-accion-ultracorta-redistribucion.svg",
    alt: "Flujograma: Barbitúricos según su duración"
  },
  "CB-094": {
    titulo: "Antineoplásicos: verdadero o falso",
    imagen: "flujogramas/antineoplasicos-verdadero-falso-asparaginasa-cisplatino.svg",
    alt: "Flujograma: Antineoplásicos: verdadero o falso"
  },
  "CB-095": {
    titulo: "Superfamilia de las inmunoglobulinas",
    imagen: "flujogramas/superfamilia-inmunoglobulinas-tcr-mhc-clase-i-ii.svg",
    alt: "Flujograma: Superfamilia de las inmunoglobulinas"
  },
  "CB-096": {
    titulo: "Reacciones anormales a fármacos",
    imagen: "flujogramas/intolerancia-idiosincrasia-tolerancia-definiciones.svg",
    alt: "Flujograma: Reacciones anormales a fármacos"
  },
  "CB-097": {
    titulo: "Tipos de hipersensibilidad",
    imagen: "flujogramas/hipersensibilidad-gell-coombs-goodpasture-tuberculosis.svg",
    alt: "Flujograma: Tipos de hipersensibilidad"
  },
  "CB-098": {
    titulo: "Inmunodeficiencia sin leucocitos",
    imagen: "flujogramas/disgenesia-reticular-scid-sin-linfocitos-ni-neutrofilos.svg",
    alt: "Flujograma: Inmunodeficiencia sin leucocitos"
  },
  "CB-099": {
    titulo: "Orificios del diafragma",
    imagen: "flujogramas/orificios-diafragma-vena-cava-t8-centro-tendinoso.svg",
    alt: "Flujograma: Orificios del diafragma"
  },
  "CB-100": {
    titulo: "Cuerda del tímpano",
    imagen: "flujogramas/cuerda-del-timpano-facial-gusto-lingual.svg",
    alt: "Flujograma: Cuerda del tímpano"
  },
  "CB-101": {
    titulo: "Niveles vertebrales del cuello",
    imagen: "flujogramas/bifurcacion-carotida-comun-borde-superior-tiroides-c4.svg",
    alt: "Flujograma: Niveles vertebrales del cuello"
  },
  "CB-102": {
    titulo: "Músculos del hioides",
    imagen: "flujogramas/musculos-infrahioideos-omohioideo-en-cinta.svg",
    alt: "Flujograma: Músculos del hioides"
  },
  "CB-103": {
    titulo: "Contenido del periné profundo",
    imagen: "flujogramas/espacio-perineal-profundo-glandulas-bulbouretrales-cowper.svg",
    alt: "Flujograma: Contenido del periné profundo"
  },
  "CB-104": {
    titulo: "Tinciones en histología",
    imagen: "flujogramas/tecnicas-histologicas-he-orceina-pas-sustancia-fundamental.svg",
    alt: "Flujograma: Tinciones en histología"
  },
  "CB-105": {
    titulo: "Síntesis de la pared bacteriana",
    imagen: "flujogramas/penicilina-pbp-transpeptidasa-pared-peptidoglucano.svg",
    alt: "Flujograma: Síntesis de la pared bacteriana"
  },
  "CB-106": {
    titulo: "Mecanismo de los antituberculosos",
    imagen: "flujogramas/rifampicina-arn-polimerasa-rpob-tuberculosis.svg",
    alt: "Flujograma: Mecanismo de los antituberculosos"
  },
  "CB-107": {
    titulo: "Sitios de la hematopoyesis",
    imagen: "flujogramas/hematopoyesis-embrionaria-saco-vitelino-higado-medula.svg",
    alt: "Flujograma: Sitios de la hematopoyesis"
  },
  "CB-108": {
    titulo: "Triángulo de Calot",
    imagen: "flujogramas/triangulo-calot-cistico-hepatico-comun-arteria-cistica.svg",
    alt: "Flujograma: Triángulo de Calot"
  },
  "CB-109": {
    titulo: "Irrigación del estómago",
    imagen: "flujogramas/curvatura-menor-gastrica-izquierda-derecha-pilorica.svg",
    alt: "Flujograma: Irrigación del estómago"
  },
  "CB-110": {
    titulo: "Enunciado incorrecto en embriología genital",
    imagen: "flujogramas/diferenciacion-gonadal-sry-no-hormona-antimulleriana.svg",
    alt: "Flujograma: Enunciado incorrecto en embriología genital"
  },
  "CB-111": {
    titulo: "Nutrientes antioxidantes",
    imagen: "flujogramas/antioxidantes-vitamina-c-e-carotenos-cobre-cofactor.svg",
    alt: "Flujograma: Nutrientes antioxidantes"
  },
  "CB-112": {
    titulo: "Tratamiento del angioedema",
    imagen: "flujogramas/angioedema-alergico-via-aerea-adrenalina-intramuscular.svg",
    alt: "Flujograma: Tratamiento del angioedema"
  },
  "CB-113": {
    titulo: "Inervación de los músculos oculares",
    imagen: "flujogramas/oblicuo-superior-nervio-patetico-troclear-iv-par.svg",
    alt: "Flujograma: Inervación de los músculos oculares"
  },
  "CB-114": {
    titulo: "Dónde ocurre cada vía",
    imagen: "flujogramas/ciclo-krebs-matriz-mitocondrial-nadh-fadh2.svg",
    alt: "Flujograma: Dónde ocurre cada vía"
  },
  "CB-115": {
    titulo: "Antibióticos contra Pseudomonas",
    imagen: "flujogramas/pseudomonas-ceftriaxona-sin-actividad-ceftazidima.svg",
    alt: "Flujograma: Antibióticos contra Pseudomonas"
  },
  "CB-116": {
    titulo: "Fármacos contra Bacteroides fragilis",
    imagen: "flujogramas/bacteroides-fragilis-vancomicina-sin-actividad-metronidazol.svg",
    alt: "Flujograma: Fármacos contra Bacteroides fragilis"
  },
  "CB-117": {
    titulo: "Duración del antibiótico en infecciones",
    imagen: "flujogramas/osteomielitis-antibiotico-seis-semanas-staphylococcus.svg",
    alt: "Flujograma: Duración del antibiótico en infecciones"
  },
  "CB-118": {
    titulo: "Efectos adversos de los diuréticos",
    imagen: "flujogramas/diureticos-efectos-adversos-ginecomastia-no-anemia-hemolitica.svg",
    alt: "Flujograma: Efectos adversos de los diuréticos"
  },
  "CB-119": {
    titulo: "Pie caído",
    imagen: "flujogramas/pie-caido-equino-nervio-peroneo-profundo-tibial-anterior.svg",
    alt: "Flujograma: Pie caído"
  },
  "CB-120": {
    titulo: "Inhibición de la anhidrasa carbónica",
    imagen: "flujogramas/anhidrasa-carbonica-acetazolamida-perdida-bicarbonato.svg",
    alt: "Flujograma: Inhibición de la anhidrasa carbónica"
  },
  "CB-121": {
    titulo: "Raíces del nervio frénico",
    imagen: "flujogramas/diafragma-nervio-frenico-c3-c4-c5.svg",
    alt: "Flujograma: Raíces del nervio frénico"
  },
  "CB-122": {
    titulo: "Sodio de las soluciones salinas",
    imagen: "flujogramas/suero-fisiologico-nacl-09-154-meq-sodio.svg",
    alt: "Flujograma: Sodio de las soluciones salinas"
  },
  "CB-123": {
    titulo: "Antimicóticos sistémicos y tópicos",
    imagen: "flujogramas/econazol-antimicotico-topico-no-sistemico.svg",
    alt: "Flujograma: Antimicóticos sistémicos y tópicos"
  },
  "CB-124": {
    titulo: "Reacciones cutáneas por antibióticos",
    imagen: "flujogramas/reacciones-cutaneas-antibioticos-betalactamicos-mas-frecuentes.svg",
    alt: "Flujograma: Reacciones cutáneas por antibióticos"
  },
  "CB-125": {
    titulo: "Indicaciones de profilaxis antibiótica",
    imagen: "flujogramas/profilaxis-antibiotica-indicaciones-no-gastroenteritis.svg",
    alt: "Flujograma: Indicaciones de profilaxis antibiótica"
  },
  "CB-126": {
    titulo: "Agenesia mülleriana",
    imagen: "flujogramas/agenesia-mulleriana-rokitansky-malformacion-renal.svg",
    alt: "Flujograma: Agenesia mülleriana"
  },
  "CB-127": {
    titulo: "Venas del miembro superior",
    imagen: "flujogramas/surco-deltopectoral-vena-cefalica-flebotomia.svg",
    alt: "Flujograma: Venas del miembro superior"
  },
  "CB-128": {
    titulo: "Tipos de articulación sinovial",
    imagen: "flujogramas/articulacion-radiocarpiana-condilea-elipsoidea-biaxial.svg",
    alt: "Flujograma: Tipos de articulación sinovial"
  },
  "CB-129": {
    titulo: "Huesos del carpo",
    imagen: "flujogramas/fila-proximal-carpo-pisiforme-piramidal-semilunar-escafoides.svg",
    alt: "Flujograma: Huesos del carpo"
  },
  "CB-130": {
    titulo: "Dónde está el sodio del cuerpo",
    imagen: "flujogramas/sodio-corporal-total-hueso-reserva.svg",
    alt: "Flujograma: Dónde está el sodio del cuerpo"
  },
  "CB-131": {
    titulo: "Colecistocinina y cólico biliar",
    imagen: "flujogramas/comida-grasa-colecistocinina-colico-biliar.svg",
    alt: "Flujograma: Colecistocinina y cólico biliar"
  },
  "CB-132": {
    titulo: "Compartimentos líquidos",
    imagen: "flujogramas/sodio-liquido-intersticial-mayor-volumen-extracelular.svg",
    alt: "Flujograma: Compartimentos líquidos"
  },
  "CB-133": {
    titulo: "Agua corporal según la edad",
    imagen: "flujogramas/agua-corporal-total-nino-3-anos-65-por-ciento.svg",
    alt: "Flujograma: Agua corporal según la edad"
  },
  "CB-134": {
    titulo: "Cierre del tubo neural",
    imagen: "flujogramas/anencefalia-neuroporo-anterior-cuarta-semana.svg",
    alt: "Flujograma: Cierre del tubo neural"
  },
  "CB-135": {
    titulo: "Acciones de los diuréticos de asa",
    imagen: "flujogramas/furosemida-venodilatacion-precarga-edema-pulmonar.svg",
    alt: "Flujograma: Acciones de los diuréticos de asa"
  },
  "CB-136": {
    titulo: "Glucólisis sin oxígeno",
    imagen: "flujogramas/musculo-anaerobio-lactato-deshidrogenasa-ciclo-cori.svg",
    alt: "Flujograma: Glucólisis sin oxígeno"
  },
  "CB-137": {
    titulo: "Efectos adversos de los antituberculosos",
    imagen: "flujogramas/etambutol-neuritis-optica-rojo-verde-suspender.svg",
    alt: "Flujograma: Efectos adversos de los antituberculosos"
  },
  "CB-138": {
    titulo: "Sodio del suero hipertónico al 3 %",
    imagen: "flujogramas/cloruro-sodio-3-por-ciento-05-meq-ml-hiponatremia.svg",
    alt: "Flujograma: Sodio del suero hipertónico al 3 %"
  },
  "CB-139": {
    titulo: "Mecanismo de los antibióticos",
    imagen: "flujogramas/quinolonas-adn-girasa-topoisomerasa-iv.svg",
    alt: "Flujograma: Mecanismo de los antibióticos"
  },
  "CB-140": {
    titulo: "Apoptosis frente a necrosis",
    imagen: "flujogramas/apoptosis-sin-inflamacion-cuerpos-apoptoticos-necrosis.svg",
    alt: "Flujograma: Apoptosis frente a necrosis"
  },
  "CB-141": {
    titulo: "Células germinales del testículo",
    imagen: "flujogramas/testiculo-nacimiento-espermatogonias-sertoli-pubertad.svg",
    alt: "Flujograma: Células germinales del testículo"
  },
  "CB-142": {
    titulo: "Homologías de los genitales externos",
    imagen: "flujogramas/homologias-genitales-labio-mayor-escroto.svg",
    alt: "Flujograma: Homologías de los genitales externos"
  },
  "CB-143": {
    titulo: "Cariotipos del síndrome de Down",
    imagen: "flujogramas/sindrome-down-trisomia-21-libre-no-disyuncion.svg",
    alt: "Flujograma: Cariotipos del síndrome de Down"
  },
  "CB-144": {
    titulo: "Histamina",
    imagen: "flujogramas/histamina-mastocitos-histidina-granulos.svg",
    alt: "Flujograma: Histamina"
  },
  "CB-145": {
    titulo: "Tipos de epitelio",
    imagen: "flujogramas/epitelio-plano-estratificado-queratinizado-epidermis.svg",
    alt: "Flujograma: Tipos de epitelio"
  },
  "CB-146": {
    titulo: "Contracción de la herida",
    imagen: "flujogramas/contraccion-herida-miofibroblasto-segunda-intencion.svg",
    alt: "Flujograma: Contracción de la herida"
  },
  "CB-147": {
    titulo: "Capacidad de regeneración",
    imagen: "flujogramas/celulas-permanentes-cardiomiocito-neurona-labiles-estables.svg",
    alt: "Flujograma: Capacidad de regeneración"
  },
  "CB-148": {
    titulo: "pH de las secreciones digestivas",
    imagen: "flujogramas/ph-secreciones-digestivas-jugo-pancreatico-alcalino.svg",
    alt: "Flujograma: pH de las secreciones digestivas"
  },
  "CB-149": {
    titulo: "Atropinización en organofosforados",
    imagen: "flujogramas/organofosforado-atropinizacion-midriasis-signos.svg",
    alt: "Flujograma: Atropinización en organofosforados"
  },
  "CB-150": {
    titulo: "Hormonas que regulan el riñón",
    imagen: "flujogramas/aldosterona-reabsorcion-sodio-colector-enac.svg",
    alt: "Flujograma: Hormonas que regulan el riñón"
  },
  "CB-151": {
    titulo: "Dosis tóxica de paracetamol",
    imagen: "flujogramas/intoxicacion-paracetamol-10-gramos-n-acetilcisteina.svg",
    alt: "Flujograma: Dosis tóxica de paracetamol"
  },
  "CB-152": {
    titulo: "Corpúsculos de Hassall",
    imagen: "flujogramas/corpusculos-hassall-medula-timo.svg",
    alt: "Flujograma: Corpúsculos de Hassall"
  },
  "CB-153": {
    titulo: "Rasgos de las vértebras",
    imagen: "flujogramas/vertebras-cervicales-agujero-transverso-espinosa-bifida.svg",
    alt: "Flujograma: Rasgos de las vértebras"
  },
  "CB-154": {
    titulo: "Sensibilidad del pie",
    imagen: "flujogramas/sensibilidad-planta-pie-nervio-tibial-plantares.svg",
    alt: "Flujograma: Sensibilidad del pie"
  },
  "CB-155": {
    titulo: "Control de la prolactina",
    imagen: "flujogramas/prolactina-dopamina-hipotalamo-inhibicion.svg",
    alt: "Flujograma: Control de la prolactina"
  },
  "CB-156": {
    titulo: "Irrigación del pie",
    imagen: "flujogramas/arteria-tibial-posterior-planta-pie-plantares.svg",
    alt: "Flujograma: Irrigación del pie"
  },
  "CB-157": {
    titulo: "Proteínas del plasma",
    imagen: "flujogramas/albumina-proteina-mas-abundante-plasma.svg",
    alt: "Flujograma: Proteínas del plasma"
  },
  "CB-158": {
    titulo: "Progresión de la xeroftalmía",
    imagen: "flujogramas/manchas-bitot-xeroftalmia-deficit-vitamina-a.svg",
    alt: "Flujograma: Progresión de la xeroftalmía"
  },
  "CB-159": {
    titulo: "Toxicidad típica de los antibióticos",
    imagen: "flujogramas/aminoglucosidos-ototoxicidad-nefrotoxicidad.svg",
    alt: "Flujograma: Toxicidad típica de los antibióticos"
  },
  "CB-160": {
    titulo: "Hueso sin inserciones musculares",
    imagen: "flujogramas/astragalo-sin-inserciones-musculares-necrosis.svg",
    alt: "Flujograma: Hueso sin inserciones musculares"
  },
  "CB-161": {
    titulo: "Núcleos profundos del cerebelo",
    imagen: "flujogramas/nucleo-fastigio-cerebelo-presion-arterial.svg",
    alt: "Flujograma: Núcleos profundos del cerebelo"
  },
  "CB-162": {
    titulo: "Síntesis de glucógeno",
    imagen: "flujogramas/glucogenogenesis-glucosa-udp-glucosa-glucogeno-sintasa.svg",
    alt: "Flujograma: Síntesis de glucógeno"
  },
  "CB-163": {
    titulo: "Transporte de la glucosa",
    imagen: "flujogramas/glucosa-difusion-facilitada-glut-sglt.svg",
    alt: "Flujograma: Transporte de la glucosa"
  },
  "CB-164": {
    titulo: "Color de la piel",
    imagen: "flujogramas/melanina-melanocitos-tirosinasa-color-piel.svg",
    alt: "Flujograma: Color de la piel"
  },
  "CB-165": {
    titulo: "Micosis sistémicas",
    imagen: "flujogramas/blastomyces-dermatitidis-micosis-sistemica.svg",
    alt: "Flujograma: Micosis sistémicas"
  },
  "CB-166": {
    titulo: "Sustratos de la síntesis de ácidos nucleicos",
    imagen: "flujogramas/sintesis-arn-ribonucleotidos-trifosfato-arn-polimerasa.svg",
    alt: "Flujograma: Sustratos de la síntesis de ácidos nucleicos"
  },
  "CB-167": {
    titulo: "Absorción de la vitamina B12",
    imagen: "flujogramas/vitamina-b12-factor-intrinseco-ileon-terminal.svg",
    alt: "Flujograma: Absorción de la vitamina B12"
  },
  "CB-168": {
    titulo: "Virus asociados a cáncer",
    imagen: "flujogramas/linfoma-burkitt-epstein-barr-c-myc.svg",
    alt: "Flujograma: Virus asociados a cáncer"
  },
  "CB-169": {
    titulo: "Jerarquía de los marcapasos",
    imagen: "flujogramas/nodo-auriculoventricular-segundo-marcapasos-40-60.svg",
    alt: "Flujograma: Jerarquía de los marcapasos"
  },
  "CB-170": {
    titulo: "La glucosa en la nefrona",
    imagen: "flujogramas/glucosa-glomerulo-ultrafiltracion-sglt2-proximal.svg",
    alt: "Flujograma: La glucosa en la nefrona"
  },
  "CB-171": {
    titulo: "Reabsorción de agua en la nefrona",
    imagen: "flujogramas/reabsorcion-agua-tubulo-proximal-65-por-ciento.svg",
    alt: "Flujograma: Reabsorción de agua en la nefrona"
  },
  "CB-172": {
    titulo: "Agente del kala-azar",
    imagen: "flujogramas/kala-azar-leishmania-donovani-esplenomegalia.svg",
    alt: "Flujograma: Agente del kala-azar"
  },
  "CB-173": {
    titulo: "Cianosis central y periférica",
    imagen: "flujogramas/cianosis-central-lengua-mucosas-periferica-lechos.svg",
    alt: "Flujograma: Cianosis central y periférica"
  },
  "CB-174": {
    titulo: "Mecanismos de las aneuploidías",
    imagen: "flujogramas/mosaicismo-error-mitotico-post-cigoto.svg",
    alt: "Flujograma: Mecanismos de las aneuploidías"
  },
  "CB-175": {
    titulo: "Biodisponibilidad de un fármaco",
    imagen: "flujogramas/biodisponibilidad-90-por-ciento-circulacion-sistemica.svg",
    alt: "Flujograma: Biodisponibilidad de un fármaco"
  },
  "CB-176": {
    titulo: "Rasgos de los aminoglucósidos",
    imagen: "flujogramas/aminoglucosidos-no-penetran-snc-meningitis.svg",
    alt: "Flujograma: Rasgos de los aminoglucósidos"
  },
  "CB-177": {
    titulo: "Generaciones de cefalosporinas",
    imagen: "flujogramas/cefazolina-primera-generacion-profilaxis-quirurgica.svg",
    alt: "Flujograma: Generaciones de cefalosporinas"
  },
  "CB-178": {
    titulo: "Clasificación ASA",
    imagen: "flujogramas/asa-iv-angina-inestable-riesgo-anestesico.svg",
    alt: "Flujograma: Clasificación ASA"
  },
  "CB-179": {
    titulo: "Fibras que conducen el dolor",
    imagen: "flujogramas/fibras-dolor-a-delta-c-rapido-lento.svg",
    alt: "Flujograma: Fibras que conducen el dolor"
  },
  "CB-180": {
    titulo: "Tipos de dolor",
    imagen: "flujogramas/dolor-postoperatorio-nociceptivo-analgesia-multimodal.svg",
    alt: "Flujograma: Tipos de dolor"
  },
  "CB-181": {
    titulo: "Escala APACHE II",
    imagen: "flujogramas/apache-ii-puntaje-alto-mayor-mortalidad.svg",
    alt: "Flujograma: Escala APACHE II"
  },
  "CB-182": {
    titulo: "Ramas del tronco celíaco",
    imagen: "flujogramas/tronco-celiaco-ramas-gastrica-izquierda-curvatura-menor.svg",
    alt: "Flujograma: Ramas del tronco celíaco"
  },
  "CB-183": {
    titulo: "Estaciones ganglionares gástricas",
    imagen: "flujogramas/ganglios-gastricos-grupo-11-arteria-esplenica.svg",
    alt: "Flujograma: Estaciones ganglionares gástricas"
  },
  "CB-184": {
    titulo: "Mecanismo de los glucocorticoides",
    imagen: "flujogramas/glucocorticoides-receptor-intracelular-transcripcion.svg",
    alt: "Flujograma: Mecanismo de los glucocorticoides"
  },
  "CB-185": {
    titulo: "Marcapaso intestinal",
    imagen: "flujogramas/celulas-intersticiales-cajal-ondas-lentas-marcapaso.svg",
    alt: "Flujograma: Marcapaso intestinal"
  },
  "CB-186": {
    titulo: "Acciones de la secretina",
    imagen: "flujogramas/secretina-inhibe-acido-estimula-bicarbonato.svg",
    alt: "Flujograma: Acciones de la secretina"
  },
  "CB-187": {
    titulo: "Volumen de las secreciones digestivas",
    imagen: "flujogramas/volumen-diario-secreciones-digestivas-gastrica-1500.svg",
    alt: "Flujograma: Volumen de las secreciones digestivas"
  },
  "CB-188": {
    titulo: "Células de la mucosa gástrica",
    imagen: "flujogramas/celula-parietal-acido-clorhidrico-factor-intrinseco.svg",
    alt: "Flujograma: Células de la mucosa gástrica"
  },
  "CB-189": {
    titulo: "Irrigación del páncreas",
    imagen: "flujogramas/pancreatoduodenal-superior-rama-gastroduodenal.svg",
    alt: "Flujograma: Irrigación del páncreas"
  },
  "CB-190": {
    titulo: "Derivados del conducto de Wolff",
    imagen: "flujogramas/conducto-wolff-derivados-no-tubulos-seminiferos.svg",
    alt: "Flujograma: Derivados del conducto de Wolff"
  },
  "CB-191": {
    titulo: "Efectos muscarínicos y nicotínicos",
    imagen: "flujogramas/efecto-muscarinico-hipotension-no-hipertension.svg",
    alt: "Flujograma: Efectos muscarínicos y nicotínicos"
  },
  "CB-192": {
    titulo: "Diagnóstico del síndrome colinérgico",
    imagen: "flujogramas/adolescente-soporoso-convulsiones-fasciculaciones-organofosforado.svg",
    alt: "Flujograma: Diagnóstico del síndrome colinérgico"
  },
  "CB-193": {
    titulo: "Patógenos y su contexto",
    imagen: "flujogramas/acinetobacter-baumannii-hospitalario-multirresistente.svg",
    alt: "Flujograma: Patógenos y su contexto"
  },
  "CB-194": {
    titulo: "Antídotos específicos",
    imagen: "flujogramas/antidotos-paracetamol-n-acetilcisteina-flumazenil-naloxona.svg",
    alt: "Flujograma: Antídotos específicos"
  },
  "CB-195": {
    titulo: "Reacción de Jarisch-Herxheimer",
    imagen: "flujogramas/jarisch-herxheimer-penicilina-sifilis-secundaria.svg",
    alt: "Flujograma: Reacción de Jarisch-Herxheimer"
  },
  "CB-196": {
    titulo: "Signos de la insuficiencia cardíaca derecha",
    imagen: "flujogramas/insuficiencia-cardiaca-derecha-edema-signo-tardio.svg",
    alt: "Flujograma: Signos de la insuficiencia cardíaca derecha"
  },
  "CB-197": {
    titulo: "Nervios de la mano",
    imagen: "flujogramas/oponente-pulgar-nervio-mediano-rama-recurrente.svg",
    alt: "Flujograma: Nervios de la mano"
  },
  "CB-198": {
    titulo: "Reposición en el shock hemorrágico",
    imagen: "flujogramas/politrauma-shock-hematocrito-20-paquete-globular.svg",
    alt: "Flujograma: Reposición en el shock hemorrágico"
  },
  "CB-199": {
    titulo: "Toxíndromes",
    imagen: "flujogramas/nino-sustancia-desconocida-toxindrome-colinergico.svg",
    alt: "Flujograma: Toxíndromes"
  },
  "CB-200": {
    titulo: "Fármacos en la gota",
    imagen: "flujogramas/alopurinol-xantina-oxidasa-uricemia.svg",
    alt: "Flujograma: Fármacos en la gota"
  },
  "CB-201": {
    titulo: "Cuándo no hacer lavado gástrico",
    imagen: "flujogramas/lavado-gastrico-contraindicado-caustico-alcali.svg",
    alt: "Flujograma: Cuándo no hacer lavado gástrico"
  },
  "CB-202": {
    titulo: "Diagnóstico ante miosis y bradicardia",
    imagen: "flujogramas/bradicardia-50-miosis-sudoracion-peristaltismo-organofosforado.svg",
    alt: "Flujograma: Diagnóstico ante miosis y bradicardia"
  },
  "CB-203": {
    titulo: "Efectos de los macrólidos",
    imagen: "flujogramas/eritromicina-qt-largo-canales-herg-torsades.svg",
    alt: "Flujograma: Efectos de los macrólidos"
  },
  "CB-204": {
    titulo: "Ingesta de hidrocarburos",
    imagen: "flujogramas/nino-kerosene-asintomatico-observar-6-horas-radiografia.svg",
    alt: "Flujograma: Ingesta de hidrocarburos"
  },
  "CB-205": {
    titulo: "Nervios según el nivel de fractura",
    imagen: "flujogramas/fractura-diafisis-humero-canal-torsion-nervio-radial.svg",
    alt: "Flujograma: Nervios según el nivel de fractura"
  },
  "CB-206": {
    titulo: "Nervios del codo",
    imagen: "flujogramas/canal-epitrocleo-olecraniano-nervio-cubital-tunel.svg",
    alt: "Flujograma: Nervios del codo"
  },
  "CB-207": {
    titulo: "Intoxicación por raticidas cumarínicos",
    imagen: "flujogramas/raticida-hidroxicumarina-fitomenadiona-vitamina-k1.svg",
    alt: "Flujograma: Intoxicación por raticidas cumarínicos"
  },
  "CB-208": {
    titulo: "Gases tóxicos",
    imagen: "flujogramas/pozo-septico-acido-sulfhidrico-knockdown.svg",
    alt: "Flujograma: Gases tóxicos"
  },
  "CB-209": {
    titulo: "Gravedad de la intoxicación colinérgica",
    imagen: "flujogramas/nino-3-anos-miosis-sialorrea-roncantes-atropina-ev.svg",
    alt: "Flujograma: Gravedad de la intoxicación colinérgica"
  },
  "CB-210": {
    titulo: "Parálisis del «sábado por la noche»",
    imagen: "flujogramas/embriaguez-brazo-sobre-mesa-mano-caida-radial.svg",
    alt: "Flujograma: Parálisis del «sábado por la noche»"
  },
  "CB-211": {
    titulo: "Origen del aparato genital femenino",
    imagen: "flujogramas/vagina-proximal-conductos-muller-seno-urogenital.svg",
    alt: "Flujograma: Origen del aparato genital femenino"
  },
  "CB-212": {
    titulo: "Antibiótico en la neumonía estafilocócica",
    imagen: "flujogramas/nino-neumonia-sarm-teicoplanina-vancomicina.svg",
    alt: "Flujograma: Antibiótico en la neumonía estafilocócica"
  },
  "CB-213": {
    titulo: "PaCO2 normal",
    imagen: "flujogramas/paco2-normal-40-mmhg-tec-hipertension-endocraneana.svg",
    alt: "Flujograma: PaCO2 normal"
  },
  "CB-214": {
    titulo: "Sustancia en el síndrome colinérgico",
    imagen: "flujogramas/nino-8-anos-sudoracion-tos-productiva-plaguicida.svg",
    alt: "Flujograma: Sustancia en el síndrome colinérgico"
  },
  "CB-215": {
    titulo: "Tratamiento del síndrome colinérgico",
    imagen: "flujogramas/depresion-ingesta-miosis-fasciculaciones-atropinizacion.svg",
    alt: "Flujograma: Tratamiento del síndrome colinérgico"
  },
  "CB-216": {
    titulo: "Efectos crónicos de los antiepilépticos",
    imagen: "flujogramas/fenitoina-hiperplasia-gingival-uso-cronico.svg",
    alt: "Flujograma: Efectos crónicos de los antiepilépticos"
  },
  "CB-217": {
    titulo: "Descenso del testículo",
    imagen: "flujogramas/descenso-testicular-conducto-inguinal-semana-28.svg",
    alt: "Flujograma: Descenso del testículo"
  },
  "CB-218": {
    titulo: "Ejes de las articulaciones",
    imagen: "flujogramas/enartrosis-esfericas-movimiento-poliaxial-cadera.svg",
    alt: "Flujograma: Ejes de las articulaciones"
  },
  "CB-219": {
    titulo: "Capacidad vital",
    imagen: "flujogramas/capacidad-vital-volumen-reserva-espirometria.svg",
    alt: "Flujograma: Capacidad vital"
  },
  "CB-220": {
    titulo: "Barrera de filtración glomerular",
    imagen: "flujogramas/adolescente-albuminuria-masiva-podocitos-diafragma.svg",
    alt: "Flujograma: Barrera de filtración glomerular"
  },
  "CB-221": {
    titulo: "Territorios arteriales digestivos",
    imagen: "flujogramas/trombosis-tronco-celiaco-intestino-mesenterica-superior.svg",
    alt: "Flujograma: Territorios arteriales digestivos"
  },
  "CB-222": {
    titulo: "Infartos blancos y rojos",
    imagen: "flujogramas/infarto-blanco-bazo-circulacion-terminal.svg",
    alt: "Flujograma: Infartos blancos y rojos"
  },
  "CB-223": {
    titulo: "Ictericia tras antipiréticos",
    imagen: "flujogramas/nino-antipireticos-antigripales-ictericia-paracetamol.svg",
    alt: "Flujograma: Ictericia tras antipiréticos"
  },
  "CB-224": {
    titulo: "Desarrollo del corazón",
    imagen: "flujogramas/cordones-angioblasticos-corazon-tercera-semana.svg",
    alt: "Flujograma: Desarrollo del corazón"
  },
  "CB-225": {
    titulo: "Metales en zonas mineras",
    imagen: "flujogramas/nino-centro-minero-colico-encefalopatia-plomo.svg",
    alt: "Flujograma: Metales en zonas mineras"
  },
  "CB-226": {
    titulo: "Origen embriológico de los órganos",
    imagen: "flujogramas/corteza-suprarrenal-mesodermo-medula-cresta-neural.svg",
    alt: "Flujograma: Origen embriológico de los órganos"
  },
  "CB-227": {
    titulo: "Funciones de la célula de Sertoli",
    imagen: "flujogramas/sertoli-hormona-antimulleriana-inhibe-no-estimula.svg",
    alt: "Flujograma: Funciones de la célula de Sertoli"
  },
  "CB-228": {
    titulo: "Interpretación de la ferritina",
    imagen: "flujogramas/ferritina-deposito-hierro-vitamina-c-absorcion.svg",
    alt: "Flujograma: Interpretación de la ferritina"
  },
  "CB-229": {
    titulo: "Acoplamiento excitación-contracción",
    imagen: "flujogramas/acoplamiento-excitacion-contraccion-calcio-troponina-c.svg",
    alt: "Flujograma: Acoplamiento excitación-contracción"
  },
  "CB-230": {
    titulo: "Control nervioso del intestino",
    imagen: "flujogramas/noradrenalina-inhibe-motilidad-intestinal-simpatico.svg",
    alt: "Flujograma: Control nervioso del intestino"
  },
  "CB-231": {
    titulo: "Epitelio de la tráquea",
    imagen: "flujogramas/traquea-epitelio-pseudoestratificado-ciliado-caliciformes.svg",
    alt: "Flujograma: Epitelio de la tráquea"
  },
  "CB-232": {
    titulo: "Desarrollo de las extremidades",
    imagen: "flujogramas/esbozos-extremidades-cuarta-semana-cresta-apical.svg",
    alt: "Flujograma: Desarrollo de las extremidades"
  },
  "CB-233": {
    titulo: "Tipos de receptores hormonales",
    imagen: "flujogramas/hormona-luteinizante-receptor-proteina-g-ampc.svg",
    alt: "Flujograma: Tipos de receptores hormonales"
  },
  "CB-234": {
    titulo: "Flujo sanguíneo renal",
    imagen: "flujogramas/flujo-sanguineo-renal-1100-ml-min-gasto-cardiaco.svg",
    alt: "Flujograma: Flujo sanguíneo renal"
  },
  "CB-235": {
    titulo: "Clindamicina",
    imagen: "flujogramas/clindamicina-colitis-pseudomembranosa-clostridioides.svg",
    alt: "Flujograma: Clindamicina"
  },
  "CB-236": {
    titulo: "Bases del ADN y del ARN",
    imagen: "flujogramas/uracilo-arn-timina-adn-bases-nitrogenadas.svg",
    alt: "Flujograma: Bases del ADN y del ARN"
  },
  "CB-237": {
    titulo: "Transporte de iones en el intestino",
    imagen: "flujogramas/ileon-colon-intercambio-bicarbonato-cloro-diarrea.svg",
    alt: "Flujograma: Transporte de iones en el intestino"
  },
  "CB-238": {
    titulo: "Parásitos hematófagos",
    imagen: "flujogramas/trichuris-trichiura-hematofago-anemia-prolapso.svg",
    alt: "Flujograma: Parásitos hematófagos"
  },
  "CB-239": {
    titulo: "Electrolitos en la desnutrición grave",
    imagen: "flujogramas/desnutricion-cronica-hiponatremia-sodio-total-aumentado.svg",
    alt: "Flujograma: Electrolitos en la desnutrición grave"
  },
  "CB-240": {
    titulo: "Hepatitis por eritromicina estolato",
    imagen: "flujogramas/faringitis-eritromicina-estolato-hepatitis-colestasica.svg",
    alt: "Flujograma: Hepatitis por eritromicina estolato"
  },
  "CB-241": {
    titulo: "Eje hipófisis-testículo",
    imagen: "flujogramas/lh-celulas-leydig-testosterona-fsh-sertoli.svg",
    alt: "Flujograma: Eje hipófisis-testículo"
  },
  "CB-242": {
    titulo: "Hormonas de la lactancia",
    imagen: "flujogramas/succion-pezon-oxitocina-eyeccion-leche.svg",
    alt: "Flujograma: Hormonas de la lactancia"
  },
  "CB-243": {
    titulo: "Causa de la anemia perniciosa",
    imagen: "flujogramas/anemia-macrocitica-gastritis-atrofica-celulas-parietales.svg",
    alt: "Flujograma: Causa de la anemia perniciosa"
  },
  "CB-244": {
    titulo: "Células del islote de Langerhans",
    imagen: "flujogramas/celulas-alfa-islote-glucagon-beta-insulina.svg",
    alt: "Flujograma: Células del islote de Langerhans"
  },
  "CB-245": {
    titulo: "Cuándo se considera el lavado gástrico",
    imagen: "flujogramas/lavado-gastrico-indicado-organofosforados-recientes.svg",
    alt: "Flujograma: Cuándo se considera el lavado gástrico"
  },
  "CB-246": {
    titulo: "Nervio espinal accesorio",
    imagen: "flujogramas/nervio-espinal-accesorio-trapecio-ecm-lesion-cervical.svg",
    alt: "Flujograma: Nervio espinal accesorio"
  },
  "CB-247": {
    titulo: "Efectos tras la atropina",
    imagen: "flujogramas/intento-suicida-atropina-midriasis-bloqueador-colinergico.svg",
    alt: "Flujograma: Efectos tras la atropina"
  },
  "CB-248": {
    titulo: "Alteraciones cromosómicas estructurales",
    imagen: "flujogramas/translocacion-cromosomica-robertsoniana-reciproca.svg",
    alt: "Flujograma: Alteraciones cromosómicas estructurales"
  },
  "CB-249": {
    titulo: "Herencia de los errores innatos",
    imagen: "flujogramas/errores-innatos-metabolismo-autosomica-recesiva.svg",
    alt: "Flujograma: Herencia de los errores innatos"
  },
  "CB-250": {
    titulo: "Fisiopatología de la acalasia",
    imagen: "flujogramas/acalasia-arequipa-vip-oxido-nitrico-esfinter.svg",
    alt: "Flujograma: Fisiopatología de la acalasia"
  },
  "CB-251": {
    titulo: "Biodisponibilidad según la vía",
    imagen: "flujogramas/biodisponibilidad-via-oral-menor-primer-paso.svg",
    alt: "Flujograma: Biodisponibilidad según la vía"
  },
  "CB-252": {
    titulo: "Grados de proteinuria",
    imagen: "flujogramas/perdida-cargas-membrana-basal-proteinuria-masiva.svg",
    alt: "Flujograma: Grados de proteinuria"
  },
  "CB-253": {
    titulo: "Epitelio del tubo digestivo",
    imagen: "flujogramas/esofago-epitelio-plano-estratificado-no-queratinizado.svg",
    alt: "Flujograma: Epitelio del tubo digestivo"
  },
  "CB-254": {
    titulo: "Sistema de conducción",
    imagen: "flujogramas/haz-de-his-unica-via-auriculoventricular.svg",
    alt: "Flujograma: Sistema de conducción"
  },
  "CB-255": {
    titulo: "Clasificación de las articulaciones",
    imagen: "flujogramas/rodilla-diartrosis-sinovial-bicondilea.svg",
    alt: "Flujograma: Clasificación de las articulaciones"
  },
  "CB-256": {
    titulo: "Efectos adversos de las tetraciclinas",
    imagen: "flujogramas/tetraciclinas-diarrea-efecto-mas-frecuente.svg",
    alt: "Flujograma: Efectos adversos de las tetraciclinas"
  },
  "CB-257": {
    titulo: "Líquido inicial en el shock",
    imagen: "flujogramas/shock-reanimacion-cristaloide-isotonico-suero-fisiologico.svg",
    alt: "Flujograma: Líquido inicial en el shock"
  },
  "CB-258": {
    titulo: "Sitio de acción de los diuréticos",
    imagen: "flujogramas/diureticos-de-asa-rama-ascendente-gruesa-nkcc2.svg",
    alt: "Flujograma: Sitio de acción de los diuréticos"
  },
  "CB-259": {
    titulo: "Fármacos del asma",
    imagen: "flujogramas/cromoglicato-sodico-estabilizador-mastocitos-asma.svg",
    alt: "Flujograma: Fármacos del asma"
  },
  "CB-260": {
    titulo: "Carbamatos y organofosforados",
    imagen: "flujogramas/mujer-joven-miosis-fasciculaciones-carbamatos.svg",
    alt: "Flujograma: Carbamatos y organofosforados"
  },
  "CB-261": {
    titulo: "Células del hígado",
    imagen: "flujogramas/celulas-kupffer-macrofagos-sinusoides-hepaticos.svg",
    alt: "Flujograma: Células del hígado"
  },
  "CB-262": {
    titulo: "Aclimatación a la altura",
    imagen: "flujogramas/aclimatacion-altura-3800-hiperventilacion-inmediata.svg",
    alt: "Flujograma: Aclimatación a la altura"
  },
  "CB-263": {
    titulo: "Prevención del mal de altura",
    imagen: "flujogramas/acetazolamida-mal-de-altura-anhidrasa-carbonica.svg",
    alt: "Flujograma: Prevención del mal de altura"
  },
  "CB-264": {
    titulo: "Fármacos en el glaucoma",
    imagen: "flujogramas/glaucoma-angulo-cerrado-anticolinergicos-contraindicados.svg",
    alt: "Flujograma: Fármacos en el glaucoma"
  },
  "CB-265": {
    titulo: "Interacciones del ketoconazol",
    imagen: "flujogramas/ketoconazol-rifampicina-induccion-cyp3a4-fracaso.svg",
    alt: "Flujograma: Interacciones del ketoconazol"
  },
  "CB-266": {
    titulo: "Isoinmunización Rh",
    imagen: "flujogramas/madre-rh-negativa-igg-anti-d-hemolisis-fetal.svg",
    alt: "Flujograma: Isoinmunización Rh"
  },
  "CB-267": {
    titulo: "Piel amarilla sin ictericia",
    imagen: "flujogramas/piel-amarilla-escleras-blancas-carotenemia.svg",
    alt: "Flujograma: Piel amarilla sin ictericia"
  },
  "CB-268": {
    titulo: "Déficit de zinc",
    imagen: "flujogramas/deficit-zinc-acrodermatitis-alopecia-diarrea.svg",
    alt: "Flujograma: Déficit de zinc"
  },
  "CB-269": {
    titulo: "Profundidad del cáncer gástrico",
    imagen: "flujogramas/cancer-gastrico-precoz-mucosa-submucosa-t1.svg",
    alt: "Flujograma: Profundidad del cáncer gástrico"
  },
  "CB-270": {
    titulo: "Absorción de nutrientes",
    imagen: "flujogramas/hierro-absorcion-forma-ferrosa-no-ferrica.svg",
    alt: "Flujograma: Absorción de nutrientes"
  },
  "CB-271": {
    titulo: "Pelagra",
    imagen: "flujogramas/pelagra-niacina-dermatitis-diarrea-demencia.svg",
    alt: "Flujograma: Pelagra"
  },
  "CB-272": {
    titulo: "Coma con secreciones",
    imagen: "flujogramas/mujer-soporosa-sialorrea-sibilantes-taquicardia-organofosforado.svg",
    alt: "Flujograma: Coma con secreciones"
  },
  "CB-273": {
    titulo: "Síntesis del colesterol",
    imagen: "flujogramas/hmg-coa-reductasa-enzima-limitante-colesterol-estatinas.svg",
    alt: "Flujograma: Síntesis del colesterol"
  },
  "CB-274": {
    titulo: "Heparinas y su control",
    imagen: "flujogramas/hbpm-control-anti-xa-no-ttpa-heparina.svg",
    alt: "Flujograma: Heparinas y su control"
  },
  "CB-275": {
    titulo: "Potencial de acción ventricular",
    imagen: "flujogramas/fase-0-potencial-accion-ventricular-canales-sodio.svg",
    alt: "Flujograma: Potencial de acción ventricular"
  },
  "CB-276": {
    titulo: "Meseta del potencial cardíaco",
    imagen: "flujogramas/meseta-calcio-tipo-l-contractilidad-miocardio.svg",
    alt: "Flujograma: Meseta del potencial cardíaco"
  },
  "CB-277": {
    titulo: "Fórmula de Winter",
    imagen: "flujogramas/ph-720-bicarbonato-15-pco2-30-formula-winter.svg",
    alt: "Flujograma: Fórmula de Winter"
  },
  "CB-278": {
    titulo: "Acidosis metabólica según el anión gap",
    imagen: "flujogramas/anion-gap-elevado-salicilatos-mudpiles.svg",
    alt: "Flujograma: Acidosis metabólica según el anión gap"
  },
  "CB-279": {
    titulo: "Diuréticos e hiponatremia",
    imagen: "flujogramas/hidroclorotiazida-hiponatremia-adulta-mayor.svg",
    alt: "Flujograma: Diuréticos e hiponatremia"
  },
  "CB-280": {
    titulo: "Tabique nasal",
    imagen: "flujogramas/tabique-nasal-lamina-perpendicular-etmoides-vomer.svg",
    alt: "Flujograma: Tabique nasal"
  },
  "CB-281": {
    titulo: "Tipos de secreción glandular",
    imagen: "flujogramas/glandulas-sebaceas-secrecion-holocrina.svg",
    alt: "Flujograma: Tipos de secreción glandular"
  },
  "CB-282": {
    titulo: "Defectos de las extremidades",
    imagen: "flujogramas/meromelia-ausencia-parcial-manos-pies-focomelia.svg",
    alt: "Flujograma: Defectos de las extremidades"
  },
  "CB-283": {
    titulo: "Dermatomas de referencia",
    imagen: "flujogramas/dermatoma-ombligo-t10-pezon-t4.svg",
    alt: "Flujograma: Dermatomas de referencia"
  },
  "CB-284": {
    titulo: "Irrigación de la vagina",
    imagen: "flujogramas/vagina-tercio-superior-arteria-uterina-cervicovaginal.svg",
    alt: "Flujograma: Irrigación de la vagina"
  },
  "CB-285": {
    titulo: "Maduración del espermatozoide",
    imagen: "flujogramas/sertoli-sosten-espermatogenesis-epididimo-maduracion.svg",
    alt: "Flujograma: Maduración del espermatozoide"
  },
  "CB-286": {
    titulo: "Síndrome del hombre rojo",
    imagen: "flujogramas/vancomicina-infusion-rapida-sindrome-hombre-rojo.svg",
    alt: "Flujograma: Síndrome del hombre rojo"
  },
  "CB-287": {
    titulo: "Síndrome anticolinérgico en el campo",
    imagen: "flujogramas/agricultor-midriasis-piel-seca-euforia-floripondio.svg",
    alt: "Flujograma: Síndrome anticolinérgico en el campo"
  },
  "CB-288": {
    titulo: "Antituberculosos en el embarazo",
    imagen: "flujogramas/gestante-tuberculosis-estreptomicina-sordera-congenita.svg",
    alt: "Flujograma: Antituberculosos en el embarazo"
  },
  "CB-289": {
    titulo: "Tratamiento empírico de Pseudomonas",
    imagen: "flujogramas/pseudomonas-grave-betalactamico-mas-aminoglucosido.svg",
    alt: "Flujograma: Tratamiento empírico de Pseudomonas"
  },
  "CB-290": {
    titulo: "Receptores sensitivos de la piel",
    imagen: "flujogramas/nociceptores-terminaciones-nerviosas-libres.svg",
    alt: "Flujograma: Receptores sensitivos de la piel"
  },
  "CB-291": {
    titulo: "Quimiorreceptores",
    imagen: "flujogramas/quimiorreceptores-centrales-paco2-perifericos-hipoxemia.svg",
    alt: "Flujograma: Quimiorreceptores"
  },
  "CB-292": {
    titulo: "Drenaje de las venas gonadales",
    imagen: "flujogramas/vena-gonadal-izquierda-renal-varicocele-izquierdo.svg",
    alt: "Flujograma: Drenaje de las venas gonadales"
  },
  "CB-293": {
    titulo: "Qué falta en la agenesia mülleriana",
    imagen: "flujogramas/agenesia-conductos-muller-ausencia-utero-ovarios-normales.svg",
    alt: "Flujograma: Qué falta en la agenesia mülleriana"
  },
  "CB-294": {
    titulo: "Intoxicación por antihistamínicos",
    imagen: "flujogramas/nino-clorfenamina-5-horas-soporte-anticolinergico.svg",
    alt: "Flujograma: Intoxicación por antihistamínicos"
  },
  "CB-295": {
    titulo: "Articulaciones cartilaginosas",
    imagen: "flujogramas/sinfisis-pubis-fibrocartilago-articulacion-cartilaginosa.svg",
    alt: "Flujograma: Articulaciones cartilaginosas"
  },
  "CB-296": {
    titulo: "Recorrido de los espermatozoides",
    imagen: "flujogramas/espermatozoides-almacen-cola-epididimo.svg",
    alt: "Flujograma: Recorrido de los espermatozoides"
  },
  "CB-297": {
    titulo: "Distonía aguda por metoclopramida",
    imagen: "flujogramas/colico-antiemetico-blefaroespasmo-metoclopramida.svg",
    alt: "Flujograma: Distonía aguda por metoclopramida"
  },
  "CB-298": {
    titulo: "Ramas del cayado aórtico",
    imagen: "flujogramas/carotida-comun-derecha-tronco-braquiocefalico.svg",
    alt: "Flujograma: Ramas del cayado aórtico"
  },
  "CB-299": {
    titulo: "Espermatograma según la OMS",
    imagen: "flujogramas/espermatograma-oligozoospermia-concentracion-baja.svg",
    alt: "Flujograma: Espermatograma según la OMS"
  },
  "CB-300": {
    titulo: "Ramas del trigémino",
    imagen: "flujogramas/masetero-nervio-mandibular-v3-masticacion.svg",
    alt: "Flujograma: Ramas del trigémino"
  },
  "CB-301": {
    titulo: "Polígono de Willis",
    imagen: "flujogramas/poligono-willis-cerebrales-anteriores-posteriores.svg",
    alt: "Flujograma: Polígono de Willis"
  },
  "CB-302": {
    titulo: "Núcleos del cerebelo",
    imagen: "flujogramas/nucleos-profundos-cerebelo-fastigio-globoso-emboliforme-dentado.svg",
    alt: "Flujograma: Núcleos del cerebelo"
  },
  "CB-303": {
    titulo: "Ramos de los nervios raquídeos",
    imagen: "flujogramas/plexo-cervical-ramos-anteriores-c1-c4.svg",
    alt: "Flujograma: Ramos de los nervios raquídeos"
  },
  "CB-304": {
    titulo: "Vesículas encefálicas",
    imagen: "flujogramas/diencefalo-prosencefalo-vesiculas-encefalicas.svg",
    alt: "Flujograma: Vesículas encefálicas"
  },
  "CB-305": {
    titulo: "Triángulos de la espalda",
    imagen: "flujogramas/triangulo-auscultacion-trapecio-borde-medial-escapula.svg",
    alt: "Flujograma: Triángulos de la espalda"
  },
  "CB-306": {
    titulo: "Nervios en la tiroidectomía",
    imagen: "flujogramas/hemitiroidectomia-izquierda-disfonia-laringeo-recurrente.svg",
    alt: "Flujograma: Nervios en la tiroidectomía"
  },
  "CB-307": {
    titulo: "Trayecto del esófago",
    imagen: "flujogramas/esofago-toracico-mediastino-superior-posterior.svg",
    alt: "Flujograma: Trayecto del esófago"
  },
  "CB-308": {
    titulo: "Estrecheces del esófago",
    imagen: "flujogramas/estrecheces-esofago-cayado-aortico-cuerpos-extranos.svg",
    alt: "Flujograma: Estrecheces del esófago"
  },
  "CB-309": {
    titulo: "Cartílagos de la laringe",
    imagen: "flujogramas/cartilagos-impares-laringe-cricoides-tiroides-epiglotis.svg",
    alt: "Flujograma: Cartílagos de la laringe"
  },
  "CB-310": {
    titulo: "Lóbulos pulmonares",
    imagen: "flujogramas/lingula-lobulo-superior-izquierdo-silueta-cardiaca.svg",
    alt: "Flujograma: Lóbulos pulmonares"
  },
  "CB-311": {
    titulo: "Plexo cardíaco",
    imagen: "flujogramas/plexo-cardiaco-vago-simpatico-cervical.svg",
    alt: "Flujograma: Plexo cardíaco"
  },
  "CB-312": {
    titulo: "Doble circulación pulmonar",
    imagen: "flujogramas/circulacion-bronquial-venas-bronquiales-drenaje-parcial.svg",
    alt: "Flujograma: Doble circulación pulmonar"
  },
  "CB-313": {
    titulo: "Relaciones de las arterias pulmonares",
    imagen: "flujogramas/arteria-pulmonar-derecha-posterior-aorta-ascendente.svg",
    alt: "Flujograma: Relaciones de las arterias pulmonares"
  },
  "CB-314": {
    titulo: "Territorios coronarios",
    imagen: "flujogramas/coronaria-derecha-nodo-sinusal-av-infarto-inferior.svg",
    alt: "Flujograma: Territorios coronarios"
  },
  "CB-315": {
    titulo: "Inervación de la laringe",
    imagen: "flujogramas/cuerdas-vocales-laringeo-recurrente-cricoaritenoideo-posterior.svg",
    alt: "Flujograma: Inervación de la laringe"
  },
  "CB-316": {
    titulo: "Contenido del mediastino",
    imagen: "flujogramas/mediastino-posterior-aorta-descendente-contenido.svg",
    alt: "Flujograma: Contenido del mediastino"
  },
  "CB-317": {
    titulo: "Irrigación del colon",
    imagen: "flujogramas/colon-ascendente-mesenterica-superior-ileocolica.svg",
    alt: "Flujograma: Irrigación del colon"
  },
  "CB-318": {
    titulo: "Región inguinal",
    imagen: "flujogramas/ligamento-inguinal-poupart-aponeurosis-oblicuo-mayor.svg",
    alt: "Flujograma: Región inguinal"
  },
  "CB-319": {
    titulo: "Tríada portal",
    imagen: "flujogramas/triada-portal-vena-porta-arteria-hepatica-conducto-biliar.svg",
    alt: "Flujograma: Tríada portal"
  },
  "CB-320": {
    titulo: "Partes del páncreas",
    imagen: "flujogramas/cabeza-pancreas-marco-duodenal-courvoisier.svg",
    alt: "Flujograma: Partes del páncreas"
  },
  "CB-321": {
    titulo: "Irrigación del apéndice",
    imagen: "flujogramas/arteria-apendicular-ileocolica-mesenterica-superior.svg",
    alt: "Flujograma: Irrigación del apéndice"
  },
  "CB-322": {
    titulo: "Niveles de sostén del útero",
    imagen: "flujogramas/sosten-utero-ligamentos-cardinales-uterosacros-delancey.svg",
    alt: "Flujograma: Niveles de sostén del útero"
  },
  "CB-323": {
    titulo: "Músculos del piso pélvico",
    imagen: "flujogramas/elevador-ano-pubococcigeo-puborrectal-iliococcigeo.svg",
    alt: "Flujograma: Músculos del piso pélvico"
  },
  "CB-324": {
    titulo: "Arterias de la pierna al pie",
    imagen: "flujogramas/arteria-pedia-continuacion-tibial-anterior.svg",
    alt: "Flujograma: Arterias de la pierna al pie"
  },
  "CB-325": {
    titulo: "Canal del pulso",
    imagen: "flujogramas/canal-del-pulso-supinador-largo-palmar-mayor.svg",
    alt: "Flujograma: Canal del pulso"
  },
  "CB-326": {
    titulo: "Complejo articular del hombro",
    imagen: "flujogramas/hombro-cinco-articulaciones-escapulotoracica-funcional.svg",
    alt: "Flujograma: Complejo articular del hombro"
  },
  "CB-327": {
    titulo: "Tamaño de las articulaciones sinoviales",
    imagen: "flujogramas/rodilla-mayor-articulacion-sinovial-bursa.svg",
    alt: "Flujograma: Tamaño de las articulaciones sinoviales"
  },
  "CB-328": {
    titulo: "Músculos de la pantorrilla",
    imagen: "flujogramas/gastrocnemio-biarticular-flexion-rodilla-plantar.svg",
    alt: "Flujograma: Músculos de la pantorrilla"
  },
  "CB-329": {
    titulo: "¿Qué articulación es sinovial?",
    imagen: "flujogramas/coxofemoral-articulacion-sinovial-diartrosis.svg",
    alt: "Flujograma: ¿Qué articulación es sinovial?"
  },
  "CB-330": {
    titulo: "Condiciones del metabolismo basal",
    imagen: "flujogramas/metabolismo-basal-ayuno-12-horas-calorimetria.svg",
    alt: "Flujograma: Condiciones del metabolismo basal"
  },
  "CB-331": {
    titulo: "Absorción de los monosacáridos",
    imagen: "flujogramas/fructosa-glut5-difusion-facilitada-enterocito.svg",
    alt: "Flujograma: Absorción de los monosacáridos"
  },
  "CB-332": {
    titulo: "Componentes del gasto energético",
    imagen: "flujogramas/metabolismo-basal-60-por-ciento-gasto-energetico.svg",
    alt: "Flujograma: Componentes del gasto energético"
  },
  "CB-333": {
    titulo: "Órganos de la gluconeogénesis",
    imagen: "flujogramas/gluconeogenesis-higado-rinon-glucosa-6-fosfatasa.svg",
    alt: "Flujograma: Órganos de la gluconeogénesis"
  },
  "CB-334": {
    titulo: "Reabsorción renal de glucosa",
    imagen: "flujogramas/sglt2-tubulo-proximal-reabsorcion-glucosa-gliflozinas.svg",
    alt: "Flujograma: Reabsorción renal de glucosa"
  },
  "CB-335": {
    titulo: "Disacáridos y sus monosacáridos",
    imagen: "flujogramas/lactosa-glucosa-galactosa-deficit-lactasa-nino.svg",
    alt: "Flujograma: Disacáridos y sus monosacáridos"
  },
  "CB-336": {
    titulo: "Transporte de lípidos en la sangre",
    imagen: "flujogramas/acidos-grasos-libres-albumina-transporte-plasma.svg",
    alt: "Flujograma: Transporte de lípidos en la sangre"
  },
  "CB-337": {
    titulo: "Familias de ácidos grasos",
    imagen: "flujogramas/aceite-pescado-omega-3-epa-dha-anchoveta.svg",
    alt: "Flujograma: Familias de ácidos grasos"
  },
  "CB-338": {
    titulo: "Transporte reverso del colesterol",
    imagen: "flujogramas/hdl-transporte-reverso-colesterol-abca1-lcat.svg",
    alt: "Flujograma: Transporte reverso del colesterol"
  },
  "CB-339": {
    titulo: "Reservas de energía del cuerpo",
    imagen: "flujogramas/trigliceridos-tejido-adiposo-mayor-reserva-energia.svg",
    alt: "Flujograma: Reservas de energía del cuerpo"
  },
  "CB-340": {
    titulo: "Leptina",
    imagen: "flujogramas/leptina-adipocito-hipotalamo-saciedad.svg",
    alt: "Flujograma: Leptina"
  },
  "CB-341": {
    titulo: "Longitud de los ácidos grasos",
    imagen: "flujogramas/dieta-acidos-grasos-cadena-corta-media-escasos.svg",
    alt: "Flujograma: Longitud de los ácidos grasos"
  },
  "CB-342": {
    titulo: "Metabolismo en ayuno y tras comer",
    imagen: "flujogramas/ayuno-prolongado-oxidacion-acidos-grasos-cetogenesis.svg",
    alt: "Flujograma: Metabolismo en ayuno y tras comer"
  },
  "CB-343": {
    titulo: "Destinos del triptófano",
    imagen: "flujogramas/triptofano-serotonina-hidroxilacion-descarboxilacion.svg",
    alt: "Flujograma: Destinos del triptófano"
  },
  "CB-344": {
    titulo: "Síntesis del óxido nítrico",
    imagen: "flujogramas/l-arginina-oxido-nitrico-sintasa-gmpc.svg",
    alt: "Flujograma: Síntesis del óxido nítrico"
  },
  "CB-345": {
    titulo: "Neurotransmisores excitadores e inhibidores",
    imagen: "flujogramas/gaba-principal-neurotransmisor-inhibidor-encefalo.svg",
    alt: "Flujograma: Neurotransmisores excitadores e inhibidores"
  },
  "CB-346": {
    titulo: "Glándula que produce melatonina",
    imagen: "flujogramas/melatonina-glandula-pineal-epifisis-ritmo-circadiano.svg",
    alt: "Flujograma: Glándula que produce melatonina"
  },
  "CB-347": {
    titulo: "Eliminación del nitrógeno",
    imagen: "flujogramas/higado-ciclo-urea-amoniaco-desaminacion.svg",
    alt: "Flujograma: Eliminación del nitrógeno"
  },
  "CB-348": {
    titulo: "Vitamina del beriberi",
    imagen: "flujogramas/beriberi-deficit-tiamina-vitamina-b1.svg",
    alt: "Flujograma: Vitamina del beriberi"
  },
  "CB-349": {
    titulo: "Oligoelemento deficiente",
    imagen: "flujogramas/deficit-cobre-anemia-neutropenia-osteoporosis-hipopigmentacion.svg",
    alt: "Flujograma: Oligoelemento deficiente"
  },
  "CB-350": {
    titulo: "Síntesis de colágeno",
    imagen: "flujogramas/vitamina-c-hidroxilacion-prolina-colageno-escorbuto.svg",
    alt: "Flujograma: Síntesis de colágeno"
  },
  "CB-351": {
    titulo: "Wernicke-Korsakoff",
    imagen: "flujogramas/alcoholico-wernicke-korsakoff-tiamina-antes-glucosa.svg",
    alt: "Flujograma: Wernicke-Korsakoff"
  },
  "CB-352": {
    titulo: "Clasificación de la xeroftalmía",
    imagen: "flujogramas/xeroftalmia-manchas-bitot-signo-nino-pequeno.svg",
    alt: "Flujograma: Clasificación de la xeroftalmía"
  },
  "CB-353": {
    titulo: "Proteínas transportadoras del plasma",
    imagen: "flujogramas/ceruloplasmina-cobre-wilson-proteinas-transportadoras.svg",
    alt: "Flujograma: Proteínas transportadoras del plasma"
  },
  "CB-354": {
    titulo: "Vitaminas liposolubles",
    imagen: "flujogramas/vitamina-e-antioxidante-liposoluble-membranas.svg",
    alt: "Flujograma: Vitaminas liposolubles"
  },
  "CB-355": {
    titulo: "Mecanismo de absorción de la B12",
    imagen: "flujogramas/vitamina-b12-transporte-activo-factor-intrinseco-cubilina.svg",
    alt: "Flujograma: Mecanismo de absorción de la B12"
  },
  "CB-356": {
    titulo: "Beriberi seco y húmedo",
    imagen: "flujogramas/beriberi-humedo-edema-insuficiencia-alto-gasto.svg",
    alt: "Flujograma: Beriberi seco y húmedo"
  },
  "CB-357": {
    titulo: "Ácido fólico preconcepcional",
    imagen: "flujogramas/mielomeningocele-acido-folico-periconcepcional-dosis.svg",
    alt: "Flujograma: Ácido fólico preconcepcional"
  },
  "CB-358": {
    titulo: "Minerales esenciales y no esenciales",
    imagen: "flujogramas/fluor-no-esencial-efecto-caries-fluorosis.svg",
    alt: "Flujograma: Minerales esenciales y no esenciales"
  },
  "CB-359": {
    titulo: "Vitamina K",
    imagen: "flujogramas/vitamina-k-carboxilacion-factores-coagulacion.svg",
    alt: "Flujograma: Vitamina K"
  },
  "CB-360": {
    titulo: "Activación de la vitamina D",
    imagen: "flujogramas/vitamina-d-calcitriol-receptor-nuclear-esteroide.svg",
    alt: "Flujograma: Activación de la vitamina D"
  },
  "CB-361": {
    titulo: "Segundos mensajeros",
    imagen: "flujogramas/segundo-mensajero-ampc-ip3-intracelular.svg",
    alt: "Flujograma: Segundos mensajeros"
  },
  "CB-362": {
    titulo: "Cicatrización con corticoides",
    imagen: "flujogramas/corticoides-cicatrizacion-lenta-vitamina-a-revierte.svg",
    alt: "Flujograma: Cicatrización con corticoides"
  },
  "CB-363": {
    titulo: "Déficit de riboflavina",
    imagen: "flujogramas/riboflavina-b2-glositis-queilitis-papilas-linguales.svg",
    alt: "Flujograma: Déficit de riboflavina"
  },
  "CB-364": {
    titulo: "Barreras en la fecundación",
    imagen: "flujogramas/zona-pelucida-enzimas-acrosomicas-acrosina.svg",
    alt: "Flujograma: Barreras en la fecundación"
  },
  "CB-365": {
    titulo: "Composición del semen",
    imagen: "flujogramas/vesicula-seminal-fructosa-60-por-ciento-semen.svg",
    alt: "Flujograma: Composición del semen"
  },
  "CB-366": {
    titulo: "Momento de la reacción acrosómica",
    imagen: "flujogramas/reaccion-acrosomica-union-zp3-zona-pelucida.svg",
    alt: "Flujograma: Momento de la reacción acrosómica"
  },
  "CB-367": {
    titulo: "Etapas del desarrollo inicial",
    imagen: "flujogramas/blastulacion-cavitacion-blastocisto-implantacion.svg",
    alt: "Flujograma: Etapas del desarrollo inicial"
  },
  "CB-368": {
    titulo: "Tipos de defectos congénitos",
    imagen: "flujogramas/bridas-amnioticas-amputacion-dedos-disrupcion.svg",
    alt: "Flujograma: Tipos de defectos congénitos"
  },
  "CB-369": {
    titulo: "Derivados del trofoblasto",
    imagen: "flujogramas/trofoblasto-placenta-corion-sincitiotrofoblasto.svg",
    alt: "Flujograma: Derivados del trofoblasto"
  },
  "CB-370": {
    titulo: "Eritropoyetina fetal",
    imagen: "flujogramas/eritropoyetina-fetal-higado-rinon-hif.svg",
    alt: "Flujograma: Eritropoyetina fetal"
  },
  "CB-371": {
    titulo: "Quistes de la vagina y la vulva",
    imagen: "flujogramas/quiste-conducto-gartner-resto-wolff-pared-vaginal.svg",
    alt: "Flujograma: Quistes de la vagina y la vulva"
  },
  "CB-372": {
    titulo: "Cronología de los genitales externos",
    imagen: "flujogramas/genitales-externos-diferenciacion-completa-semana-12.svg",
    alt: "Flujograma: Cronología de los genitales externos"
  },
  "CB-373": {
    titulo: "Inicio de la testosterona fetal",
    imagen: "flujogramas/testosterona-fetal-leydig-semana-7-8-hcg.svg",
    alt: "Flujograma: Inicio de la testosterona fetal"
  },
  "CB-374": {
    titulo: "Cortocircuitos fetales",
    imagen: "flujogramas/circulacion-fetal-cortocircuitos-derecha-izquierda.svg",
    alt: "Flujograma: Cortocircuitos fetales"
  },
  "CB-375": {
    titulo: "Del gameto al embrión",
    imagen: "flujogramas/fecundacion-pronucleos-femenino-masculino.svg",
    alt: "Flujograma: Del gameto al embrión"
  },
  "CB-376": {
    titulo: "Etapas del desarrollo pulmonar",
    imagen: "flujogramas/pulmon-fetal-canalicular-surfactante-20-24-semanas.svg",
    alt: "Flujograma: Etapas del desarrollo pulmonar"
  },
  "CB-377": {
    titulo: "Funciones del conducto de Wolff",
    imagen: "flujogramas/agenesia-conducto-wolff-rinon-ureter-vesicula-seminal.svg",
    alt: "Flujograma: Funciones del conducto de Wolff"
  },
  "CB-378": {
    titulo: "Órgano que define la madurez fetal",
    imagen: "flujogramas/madurez-fetal-pulmon-surfactante-organo-limitante.svg",
    alt: "Flujograma: Órgano que define la madurez fetal"
  },
  "CB-379": {
    titulo: "Sistemas renales del embrión",
    imagen: "flujogramas/metanefros-rinon-definitivo-quinta-semana.svg",
    alt: "Flujograma: Sistemas renales del embrión"
  },
  "CB-380": {
    titulo: "Trisomías y síndromes",
    imagen: "flujogramas/sindrome-patau-trisomia-13-holoprosencefalia.svg",
    alt: "Flujograma: Trisomías y síndromes"
  },
  "CB-381": {
    titulo: "Síndrome con polidactilia y onfalocele",
    imagen: "flujogramas/polidactilia-onfalocele-hipotonia-retraso-patau.svg",
    alt: "Flujograma: Síndrome con polidactilia y onfalocele"
  },
  "CB-382": {
    titulo: "Vida media de un fármaco",
    imagen: "flujogramas/vida-media-50-por-ciento-concentracion-plasmatica.svg",
    alt: "Flujograma: Vida media de un fármaco"
  },
  "CB-383": {
    titulo: "Inductores e inhibidores enzimáticos",
    imagen: "flujogramas/fenitoina-inductor-enzimatico-valproato-inhibidor.svg",
    alt: "Flujograma: Inductores e inhibidores enzimáticos"
  },
  "CB-384": {
    titulo: "Unión neuromuscular",
    imagen: "flujogramas/union-neuromuscular-acetilcolina-receptor-nicotinico.svg",
    alt: "Flujograma: Unión neuromuscular"
  },
  "CB-385": {
    titulo: "Generaciones de cefalosporinas",
    imagen: "flujogramas/cefuroxima-cefepima-ceftazidima-cefadroxilo-generaciones.svg",
    alt: "Flujograma: Generaciones de cefalosporinas"
  },
  "CB-386": {
    titulo: "Fármacos y colestasis",
    imagen: "flujogramas/colestasis-farmacos-clorpromazina-paracetamol-hepatocelular.svg",
    alt: "Flujograma: Fármacos y colestasis"
  },
  "CB-387": {
    titulo: "Cefalosporina contra anaerobios",
    imagen: "flujogramas/cefoxitina-bacteroides-fragilis-cefamicina.svg",
    alt: "Flujograma: Cefalosporina contra anaerobios"
  },
  "CB-388": {
    titulo: "Sitio de acción de los antibióticos",
    imagen: "flujogramas/polimixina-membrana-no-sintesis-proteica.svg",
    alt: "Flujograma: Sitio de acción de los antibióticos"
  },
  "CB-389": {
    titulo: "Esquema de la lepra multibacilar",
    imagen: "flujogramas/lepra-lepromatosa-dapsona-rifampicina-clofazimina.svg",
    alt: "Flujograma: Esquema de la lepra multibacilar"
  },
  "CB-390": {
    titulo: "Antibiótico en quemado con Pseudomonas",
    imagen: "flujogramas/quemado-tercer-grado-pseudomonas-ceftazidima.svg",
    alt: "Flujograma: Antibiótico en quemado con Pseudomonas"
  },
  "CB-391": {
    titulo: "Antibiótico en alergia grave a penicilina",
    imagen: "flujogramas/anafilaxia-penicilina-pseudomonas-aztreonam.svg",
    alt: "Flujograma: Antibiótico en alergia grave a penicilina"
  },
  "CB-392": {
    titulo: "Cobertura intraabdominal nosocomial",
    imagen: "flujogramas/infeccion-abdominal-nosocomial-piperacilina-tazobactam.svg",
    alt: "Flujograma: Cobertura intraabdominal nosocomial"
  },
  "CB-393": {
    titulo: "Antibióticos según su blanco",
    imagen: "flujogramas/claritromicina-no-actua-pared-ribosoma-50s.svg",
    alt: "Flujograma: Antibióticos según su blanco"
  },
  "CB-394": {
    titulo: "Diarrea por Campylobacter",
    imagen: "flujogramas/campylobacter-jejuni-azitromicina-resistencia-quinolonas.svg",
    alt: "Flujograma: Diarrea por Campylobacter"
  },
  "CB-395": {
    titulo: "Cefalosporinas y Pseudomonas",
    imagen: "flujogramas/ceftazidima-cefalosporina-antipseudomonas-avibactam.svg",
    alt: "Flujograma: Cefalosporinas y Pseudomonas"
  },
  "CB-396": {
    titulo: "Corticoides en la tuberculosis",
    imagen: "flujogramas/meningitis-tuberculosa-dexametasona-corticoides.svg",
    alt: "Flujograma: Corticoides en la tuberculosis"
  },
  "CB-397": {
    titulo: "Ototoxicidad de los aminoglucósidos",
    imagen: "flujogramas/aminoglucosidos-viii-par-vestibular-coclear.svg",
    alt: "Flujograma: Ototoxicidad de los aminoglucósidos"
  },
  "CB-398": {
    titulo: "Ajuste renal de los antibióticos",
    imagen: "flujogramas/azitromicina-sin-ajuste-renal-eliminacion-biliar.svg",
    alt: "Flujograma: Ajuste renal de los antibióticos"
  },
  "CB-399": {
    titulo: "Vía del folato bacteriano",
    imagen: "flujogramas/sulfonamidas-dihidropteroato-sintasa-paba-trimetoprima.svg",
    alt: "Flujograma: Vía del folato bacteriano"
  },
  "CB-400": {
    titulo: "Intoxicación por plantas en niñas",
    imagen: "flujogramas/ninas-licuado-flores-alucinaciones-midriasis-atropinicos.svg",
    alt: "Flujograma: Intoxicación por plantas en niñas"
  },
  "CB-401": {
    titulo: "Toxicidad del metanol",
    imagen: "flujogramas/alcoholico-metanol-vision-etanol-fomepizol.svg",
    alt: "Flujograma: Toxicidad del metanol"
  },
  "CB-402": {
    titulo: "Fases de la intoxicación por hierro",
    imagen: "flujogramas/nino-hierro-vomitos-diarrea-sangre-deferoxamina.svg",
    alt: "Flujograma: Fases de la intoxicación por hierro"
  },
  "CB-403": {
    titulo: "Inicio del potencial muscular",
    imagen: "flujogramas/potencial-accion-musculo-esqueletico-acetilcolina-placa.svg",
    alt: "Flujograma: Inicio del potencial muscular"
  },
  "CB-404": {
    titulo: "Broncodilatadores",
    imagen: "flujogramas/ipratropio-antagonista-muscarinico-broncodilatador.svg",
    alt: "Flujograma: Broncodilatadores"
  },
  "CB-405": {
    titulo: "Mecanismo de los AINE",
    imagen: "flujogramas/artritis-reumatoide-diclofenaco-cox-prostaglandinas.svg",
    alt: "Flujograma: Mecanismo de los AINE"
  },
  "CB-406": {
    titulo: "Cocaína: verdadero o falso",
    imagen: "flujogramas/cocaina-vasoconstrictora-ester-recaptacion-vvvf.svg",
    alt: "Flujograma: Cocaína: verdadero o falso"
  },
  "CB-407": {
    titulo: "Estimulantes del SNC",
    imagen: "flujogramas/anfetamina-libera-noradrenalina-dopamina-serotonina.svg",
    alt: "Flujograma: Estimulantes del SNC"
  },
  "CB-408": {
    titulo: "Tos crónica en un hipertenso",
    imagen: "flujogramas/hipertenso-captopril-tos-seca-bk-negativo-ieca.svg",
    alt: "Flujograma: Tos crónica en un hipertenso"
  },
  "CB-409": {
    titulo: "Efectos de la adrenalina según la dosis",
    imagen: "flujogramas/adrenalina-dosis-alta-alfa-1-vasoconstriccion.svg",
    alt: "Flujograma: Efectos de la adrenalina según la dosis"
  },
  "CB-410": {
    titulo: "Gota por fármacos",
    imagen: "flujogramas/adulto-mayor-podagra-hidroclorotiazida-hiperuricemia.svg",
    alt: "Flujograma: Gota por fármacos"
  },
  "CB-411": {
    titulo: "Acción de la naloxona",
    imagen: "flujogramas/naloxona-revierte-depresion-respiratoria-opioides.svg",
    alt: "Flujograma: Acción de la naloxona"
  },
  "CB-412": {
    titulo: "Analgésico que causa convulsiones",
    imagen: "flujogramas/postoperatorio-analgesico-convulsiones-tramadol.svg",
    alt: "Flujograma: Analgésico que causa convulsiones"
  },
  "CB-413": {
    titulo: "Fármaco que causa melena",
    imagen: "flujogramas/lumbalgia-aine-cuarto-dia-melena-indometacina.svg",
    alt: "Flujograma: Fármaco que causa melena"
  },
  "CB-414": {
    titulo: "Umbral del dolor",
    imagen: "flujogramas/analgesicos-aumentan-umbral-doloroso.svg",
    alt: "Flujograma: Umbral del dolor"
  },
  "CB-415": {
    titulo: "Por qué los AINE dañan el estómago",
    imagen: "flujogramas/aine-gastropatia-cox1-prostaglandinas-protectoras.svg",
    alt: "Flujograma: Por qué los AINE dañan el estómago"
  },
  "CB-416": {
    titulo: "Duración del efecto de la aspirina",
    imagen: "flujogramas/aspirina-antiagregacion-irreversible-vida-plaqueta.svg",
    alt: "Flujograma: Duración del efecto de la aspirina"
  },
  "CB-417": {
    titulo: "Control de los anticoagulantes",
    imagen: "flujogramas/heparina-no-fraccionada-ttpa-monitoreo-tvp.svg",
    alt: "Flujograma: Control de los anticoagulantes"
  },
  "CB-418": {
    titulo: "Control de la warfarina",
    imagen: "flujogramas/fibrilacion-auricular-warfarina-equimosis-inr.svg",
    alt: "Flujograma: Control de la warfarina"
  },
  "CB-419": {
    titulo: "Generaciones de antihistamínicos",
    imagen: "flujogramas/prometazina-antihistaminico-primera-generacion-sedante.svg",
    alt: "Flujograma: Generaciones de antihistamínicos"
  },
  "CB-420": {
    titulo: "Relajantes neuromusculares",
    imagen: "flujogramas/succinilcolina-despolarizante-pseudocolinesterasa.svg",
    alt: "Flujograma: Relajantes neuromusculares"
  },
  "CB-421": {
    titulo: "Misoprostol",
    imagen: "flujogramas/misoprostol-prevencion-dano-mucoso-aine.svg",
    alt: "Flujograma: Misoprostol"
  },
  "CB-422": {
    titulo: "Tratamiento de parasitosis intestinales",
    imagen: "flujogramas/giardiasis-metronidazol-tinidazol-tratamiento.svg",
    alt: "Flujograma: Tratamiento de parasitosis intestinales"
  },
  "CB-423": {
    titulo: "Falsa crisis asmática",
    imagen: "flujogramas/nina-broncorrea-sin-mejoria-nebulizaciones-miosis-colinesterasa.svg",
    alt: "Flujograma: Falsa crisis asmática"
  },
  "CB-424": {
    titulo: "Efectos adversos de los corticoides",
    imagen: "flujogramas/corticoides-cronicos-osteoporosis-colapso-vertebral.svg",
    alt: "Flujograma: Efectos adversos de los corticoides"
  },
  "CB-425": {
    titulo: "Sedación de los antidepresivos",
    imagen: "flujogramas/fluoxetina-menor-sedacion-antidepresivos.svg",
    alt: "Flujograma: Sedación de los antidepresivos"
  },
  "CB-426": {
    titulo: "Mecanismo de los antihelmínticos",
    imagen: "flujogramas/pamoato-pirantel-colinesterasa-paralisis-espastica.svg",
    alt: "Flujograma: Mecanismo de los antihelmínticos"
  },
  "CB-427": {
    titulo: "Tipos de hipoxia",
    imagen: "flujogramas/monoxido-carbono-hipoxia-citotoxica-carboxihemoglobina.svg",
    alt: "Flujograma: Tipos de hipoxia"
  },
  "CB-428": {
    titulo: "Clases de antineoplásicos",
    imagen: "flujogramas/cisplatino-alquilante-platino-enlaces-cruzados.svg",
    alt: "Flujograma: Clases de antineoplásicos"
  },
  "CB-429": {
    titulo: "Activación de la ciclofosfamida",
    imagen: "flujogramas/ciclofosfamida-profarmaco-mostaza-alquilacion-adn.svg",
    alt: "Flujograma: Activación de la ciclofosfamida"
  },
  "CB-430": {
    titulo: "Tratamiento del dolor neuropático",
    imagen: "flujogramas/antidepresivos-dolor-neuropatico-diabetico.svg",
    alt: "Flujograma: Tratamiento del dolor neuropático"
  },
  "CB-431": {
    titulo: "Sobredosis de benzodiacepinas",
    imagen: "flujogramas/sobredosis-clonazepam-flumazenilo-cautela.svg",
    alt: "Flujograma: Sobredosis de benzodiacepinas"
  },
  "CB-432": {
    titulo: "Anticonvulsivante tricíclico",
    imagen: "flujogramas/carbamazepina-estructura-triciclica-anticonvulsivante.svg",
    alt: "Flujograma: Anticonvulsivante tricíclico"
  },
  "CB-433": {
    titulo: "Fármacos para la neuropatía diabética",
    imagen: "flujogramas/duloxetina-irsn-neuropatia-diabetica.svg",
    alt: "Flujograma: Fármacos para la neuropatía diabética"
  },
  "CB-434": {
    titulo: "Efectos de los corticoides en dosis altas",
    imagen: "flujogramas/lupus-corticoides-dosis-altas-linfopenia-t.svg",
    alt: "Flujograma: Efectos de los corticoides en dosis altas"
  },
  "CB-435": {
    titulo: "Duración de los anestésicos locales",
    imagen: "flujogramas/lidocaina-duracion-60-180-minutos-adrenalina.svg",
    alt: "Flujograma: Duración de los anestésicos locales"
  },
  "CB-436": {
    titulo: "Neuropatía por fármacos",
    imagen: "flujogramas/erc-infecciones-urinarias-neuropatia-nitrofurantoina.svg",
    alt: "Flujograma: Neuropatía por fármacos"
  },
  "CB-437": {
    titulo: "Anticonvulsivantes e hiponatremia",
    imagen: "flujogramas/carbamazepina-oxcarbazepina-hiponatremia-siadh.svg",
    alt: "Flujograma: Anticonvulsivantes e hiponatremia"
  },
  "CB-438": {
    titulo: "De la metaplasia al cáncer",
    imagen: "flujogramas/metaplasia-cambio-reversible-tipo-celular-adulto.svg",
    alt: "Flujograma: De la metaplasia al cáncer"
  },
  "CB-439": {
    titulo: "Adaptaciones celulares",
    imagen: "flujogramas/adaptaciones-celulares-metaplasia-hipertrofia-atrofia.svg",
    alt: "Flujograma: Adaptaciones celulares"
  },
  "CB-440": {
    titulo: "Rasgo de las células malignas",
    imagen: "flujogramas/anaplasia-celulas-malignas-pleomorfismo.svg",
    alt: "Flujograma: Rasgo de las células malignas"
  },
  "CB-441": {
    titulo: "Progresión del cáncer de piel escamoso",
    imagen: "flujogramas/enfermedad-bowen-carcinoma-epidermoide-in-situ.svg",
    alt: "Flujograma: Progresión del cáncer de piel escamoso"
  },
  "CB-442": {
    titulo: "Epitelio del folículo tiroideo",
    imagen: "flujogramas/foliculo-tiroideo-epitelio-simple-cubico-actividad.svg",
    alt: "Flujograma: Epitelio del folículo tiroideo"
  },
  "CB-443": {
    titulo: "Del epitelio bronquial al cáncer",
    imagen: "flujogramas/fumador-metaplasia-escamosa-carcinoma-epidermoide.svg",
    alt: "Flujograma: Del epitelio bronquial al cáncer"
  },
  "CB-444": {
    titulo: "Tipos de cartílago",
    imagen: "flujogramas/cartilago-avascular-difusion-condrocitos.svg",
    alt: "Flujograma: Tipos de cartílago"
  },
  "CB-445": {
    titulo: "Barrera hematoencefálica",
    imagen: "flujogramas/barrera-hematoencefalica-astrocitos-uniones-estrechas.svg",
    alt: "Flujograma: Barrera hematoencefálica"
  },
  "CB-446": {
    titulo: "Músculo liso y sistema autónomo",
    imagen: "flujogramas/musculo-pilomotor-alfa-1-noradrenalina.svg",
    alt: "Flujograma: Músculo liso y sistema autónomo"
  },
  "CB-447": {
    titulo: "Neuroglia",
    imagen: "flujogramas/tec-detritos-neuronales-microglia-fagocitosis.svg",
    alt: "Flujograma: Neuroglia"
  },
  "CB-448": {
    titulo: "Inmunidad de la mucosa intestinal",
    imagen: "flujogramas/celulas-m-placas-peyer-transcitosis-antigenos.svg",
    alt: "Flujograma: Inmunidad de la mucosa intestinal"
  },
  "CB-449": {
    titulo: "Estructura de las válvulas cardíacas",
    imagen: "flujogramas/valvula-cardiaca-conectivo-denso-endocardio.svg",
    alt: "Flujograma: Estructura de las válvulas cardíacas"
  },
  "CB-450": {
    titulo: "Nutrición de la pared vascular",
    imagen: "flujogramas/vasa-vasorum-adventicia-media-externa-aortitis.svg",
    alt: "Flujograma: Nutrición de la pared vascular"
  },
  "CB-451": {
    titulo: "Células del testículo",
    imagen: "flujogramas/inhibina-b-celulas-sertoli-fsh-varon.svg",
    alt: "Flujograma: Células del testículo"
  },
  "CB-452": {
    titulo: "Origen de los componentes del semen",
    imagen: "flujogramas/prostaglandinas-semen-vesiculas-seminales.svg",
    alt: "Flujograma: Origen de los componentes del semen"
  },
  "CB-453": {
    titulo: "Células productoras de hormonas",
    imagen: "flujogramas/testosterona-celulas-leydig-intersticio-lh.svg",
    alt: "Flujograma: Células productoras de hormonas"
  },
  "CB-454": {
    titulo: "Tipos de glándulas exocrinas",
    imagen: "flujogramas/pancreas-exocrino-acinos-serosos-zimogeno.svg",
    alt: "Flujograma: Tipos de glándulas exocrinas"
  },
  "CB-455": {
    titulo: "Epitelio de la vesícula biliar",
    imagen: "flujogramas/vesicula-biliar-epitelio-cilindrico-simple-rokitansky.svg",
    alt: "Flujograma: Epitelio de la vesícula biliar"
  },
  "CB-456": {
    titulo: "Drenaje de los ganglios inguinales",
    imagen: "flujogramas/adenopatia-inguinal-carcinoma-escamoso-canal-anal.svg",
    alt: "Flujograma: Drenaje de los ganglios inguinales"
  },
  "CB-457": {
    titulo: "Reacción leucemoide",
    imagen: "flujogramas/reaccion-leucemoide-neutrofilica-hemorragia-hemolisis.svg",
    alt: "Flujograma: Reacción leucemoide"
  },
  "CB-458": {
    titulo: "Espectro de la infección",
    imagen: "flujogramas/infeccion-subclinica-seroconversion-titulos-anticuerpos.svg",
    alt: "Flujograma: Espectro de la infección"
  },
  "CB-459": {
    titulo: "Componentes de la inmunidad innata",
    imagen: "flujogramas/macrofago-inmunidad-innata-fagocitosis-citocinas.svg",
    alt: "Flujograma: Componentes de la inmunidad innata"
  },
  "CB-460": {
    titulo: "Tamaño del bazo",
    imagen: "flujogramas/esplenomegalia-masiva-linfomas-lmc-mielofibrosis.svg",
    alt: "Flujograma: Tamaño del bazo"
  },
  "CB-461": {
    titulo: "Clases de inmunoglobulinas",
    imagen: "flujogramas/ige-anafilaxia-atopia-mastocitos-fceri.svg",
    alt: "Flujograma: Clases de inmunoglobulinas"
  },
  "CB-462": {
    titulo: "Virulencia de Bacteroides fragilis",
    imagen: "flujogramas/bacteroides-fragilis-capsula-zwitterionica-abscesos.svg",
    alt: "Flujograma: Virulencia de Bacteroides fragilis"
  },
  "CB-463": {
    titulo: "Meningitis neonatal según el Gram",
    imagen: "flujogramas/neonato-meningitis-cocobacilos-grampositivos-listeria.svg",
    alt: "Flujograma: Meningitis neonatal según el Gram"
  },
  "CB-464": {
    titulo: "Meningitis infantil según el Gram",
    imagen: "flujogramas/nino-3-anos-meningitis-cocobacilos-gramnegativos-hib.svg",
    alt: "Flujograma: Meningitis infantil según el Gram"
  },
  "CB-465": {
    titulo: "Mecanismo de la toxina colérica",
    imagen: "flujogramas/vibrio-cholerae-toxina-gangliosido-gm1-ampc.svg",
    alt: "Flujograma: Mecanismo de la toxina colérica"
  },
  "CB-466": {
    titulo: "Patrones del LCR",
    imagen: "flujogramas/lcr-linfocitario-hipoglucorraquia-meningitis-tuberculosa.svg",
    alt: "Flujograma: Patrones del LCR"
  },
  "CB-467": {
    titulo: "Toxina del shock tóxico",
    imagen: "flujogramas/shock-toxico-estafilococico-tsst1-superantigeno.svg",
    alt: "Flujograma: Toxina del shock tóxico"
  },
  "CB-468": {
    titulo: "Flora del colon",
    imagen: "flujogramas/flora-colonica-anaerobios-bacteroides-predominante.svg",
    alt: "Flujograma: Flora del colon"
  },
  "CB-469": {
    titulo: "Factores de virulencia de S. aureus",
    imagen: "flujogramas/staphylococcus-aureus-capsula-antifagocitica-virulencia.svg",
    alt: "Flujograma: Factores de virulencia de S. aureus"
  },
  "CB-470": {
    titulo: "Campylobacter y Guillain-Barré",
    imagen: "flujogramas/campylobacter-jejuni-guillain-barre-mimetismo.svg",
    alt: "Flujograma: Campylobacter y Guillain-Barré"
  },
  "CB-471": {
    titulo: "Estreptolisinas O y S",
    imagen: "flujogramas/estreptolisina-s-no-inmunogena-o-aso.svg",
    alt: "Flujograma: Estreptolisinas O y S"
  },
  "CB-472": {
    titulo: "Virulencia de Helicobacter pylori",
    imagen: "flujogramas/helicobacter-pylori-ureasa-amoniaco-virulencia.svg",
    alt: "Flujograma: Virulencia de Helicobacter pylori"
  },
  "CB-473": {
    titulo: "Pruebas para Legionella",
    imagen: "flujogramas/legionella-antigeno-urinario-serogrupo-1.svg",
    alt: "Flujograma: Pruebas para Legionella"
  },
  "CB-474": {
    titulo: "Especies de Clostridium",
    imagen: "flujogramas/clostridium-botulinum-neurotoxina-paralisis-flacida.svg",
    alt: "Flujograma: Especies de Clostridium"
  },
  "CB-475": {
    titulo: "Anaerobios según el sitio",
    imagen: "flujogramas/anaerobios-poco-frecuentes-infeccion-urinaria.svg",
    alt: "Flujograma: Anaerobios según el sitio"
  },
  "CB-476": {
    titulo: "Tratamiento de C. difficile",
    imagen: "flujogramas/clostridioides-difficile-vancomicina-oral-fidaxomicina.svg",
    alt: "Flujograma: Tratamiento de C. difficile"
  },
  "CB-477": {
    titulo: "Ciclos de los vectores",
    imagen: "flujogramas/anopheles-metamorfosis-completa-sin-ninfa.svg",
    alt: "Flujograma: Ciclos de los vectores"
  },
  "CB-478": {
    titulo: "Ciclo de Strongyloides",
    imagen: "flujogramas/strongyloides-larva-filariforme-penetra-piel-autoinfeccion.svg",
    alt: "Flujograma: Ciclo de Strongyloides"
  },
  "CB-479": {
    titulo: "Muestras para Pneumocystis",
    imagen: "flujogramas/sida-pneumocystis-muestras-hemocultivo-inutil.svg",
    alt: "Flujograma: Muestras para Pneumocystis"
  },
  "CB-480": {
    titulo: "Inclusiones virales",
    imagen: "flujogramas/cuerpos-negri-rabia-inclusion-intracitoplasmatica.svg",
    alt: "Flujograma: Inclusiones virales"
  },
  "CB-481": {
    titulo: "Parotiditis epidémica",
    imagen: "flujogramas/parotiditis-paperas-paramyxovirus-orquitis.svg",
    alt: "Flujograma: Parotiditis epidémica"
  },
  "CB-482": {
    titulo: "Helmintos con ciclo pulmonar",
    imagen: "flujogramas/ciclo-pulmonar-ascaris-necator-strongyloides-loeffler.svg",
    alt: "Flujograma: Helmintos con ciclo pulmonar"
  },
  "CB-483": {
    titulo: "Vías de infección parasitaria",
    imagen: "flujogramas/strongyloides-penetracion-cutanea-no-fecalismo.svg",
    alt: "Flujograma: Vías de infección parasitaria"
  },
  "CB-484": {
    titulo: "Protozoos intestinales",
    imagen: "flujogramas/blastocystis-no-acido-alcohol-resistente-coccidias.svg",
    alt: "Flujograma: Protozoos intestinales"
  },
  "CB-485": {
    titulo: "Parasitosis transmitidas por el suelo",
    imagen: "flujogramas/geohelmintiasis-ascaris-trichuris-maduran-suelo.svg",
    alt: "Flujograma: Parasitosis transmitidas por el suelo"
  }
};
