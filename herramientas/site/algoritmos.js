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
    titulo: "Ácido en el ojo: irrigar de inmediato, antes de cualquier otra cosa",
    imagen: "flujogramas/quemadura-quimica-ocular-aguda.svg",
    alt: "Flujograma: Ácido en el ojo: irrigar de inmediato, antes de cualquier otra cosa"
  },
  "PED-003": {
    titulo: "Nariz plana, epicanto, manchas de Brushfield y soplo: trisomía 21",
    imagen: "flujogramas/dismorfologia-cardiopatias-trisomia-21.svg",
    alt: "Flujograma: Nariz plana, epicanto, manchas de Brushfield y soplo: trisomía 21"
  },
  "CIR-003": {
    titulo: "Fracturas costales dobles del 2.º al 6.º arco con dificultad respiratoria: tórax inestable",
    imagen: "flujogramas/trauma-toracico-cerrado.svg",
    alt: "Flujograma: Fracturas costales dobles del 2.º al 6.º arco con dificultad respiratoria: tórax inestable"
  },
  "INF-002": {
    titulo: "Fiebre, cefalea, estornudos y tos de 2 días: coronavirus (virus ARN)",
    imagen: "flujogramas/virologia-virus-respiratorios.svg",
    alt: "Flujograma: Fiebre, cefalea, estornudos y tos de 2 días: coronavirus (virus ARN)"
  },
  "GIN-003": {
    titulo: "Fase activa detenida 6 horas en 6 cm con desaceleraciones: cesárea",
    imagen: "flujogramas/distocia-fase-activa-compromiso-fetal.svg",
    alt: "Flujograma: Fase activa detenida 6 horas en 6 cm con desaceleraciones: cesárea"
  },
  "CIR-002": {
    titulo: "Escolar con dolor periumbilical que baja a fosa ilíaca derecha, vómitos y rebote: apendicitis aguda",
    imagen: "flujogramas/abdomen-agudo-pediatria.svg",
    alt: "Flujograma: Escolar con dolor periumbilical que baja a fosa ilíaca derecha, vómitos y rebote: apendicitis aguda"
  },
  "PED-002": {
    titulo: "Niño con fiebre y rodilla roja, caliente e inflamada: artritis séptica",
    imagen: "flujogramas/monoartritis-aguda-pediatria.svg",
    alt: "Flujograma: Niño con fiebre y rodilla roja, caliente e inflamada: artritis séptica"
  },
  "NRL-002": {
    titulo: "Cefalea súbita «la peor de su vida», vómitos, pérdida de conciencia y rigidez de nuca: hemorragia subaracnoidea",
    imagen: "flujogramas/cefalea-subita-hemorragia-subaracnoidea.svg",
    alt: "Flujograma: Cefalea súbita «la peor de su vida», vómitos, pérdida de conciencia y rigidez de nuca: hemorragia subaracnoidea"
  },
  "REU-002": {
    titulo: "Piel amarilla con escleras limpias en una vegana: carotinemia",
    imagen: "flujogramas/diagnostico-diferencial-ictericia.svg",
    alt: "Flujograma: Piel amarilla con escleras limpias en una vegana: carotinemia"
  },
  "GIN-002": {
    titulo: "Rotura prematura de membranas a las 32 semanas confirmada con el test del helecho: antibióticos",
    imagen: "flujogramas/rotura-prematura-membranas.svg",
    alt: "Flujograma: Rotura prematura de membranas a las 32 semanas confirmada con el test del helecho: antibióticos"
  },

  /* ---------- ENAM 2020 · preguntas 22 a 31 ---------- */

  "PED-004": {
    titulo: "Prematuro con dificultad respiratoria y pulmones en vidrio esmerilado: enfermedad de membrana hialina",
    imagen: "flujogramas/membrana-hialina-sdra-neonatal.svg",
    alt: "Flujograma: Prematuro con dificultad respiratoria y pulmones en vidrio esmerilado: enfermedad de membrana hialina"
  },
  "HEM-002": {
    titulo: "Hemoglobina baja, VCM bajo y ferritina baja: anemia ferropénica",
    imagen: "flujogramas/anemia-ferropenica-perfil-hierro.svg",
    alt: "Flujograma: Hemoglobina baja, VCM bajo y ferritina baja: anemia ferropénica"
  },
  "NEF-002": {
    titulo: "Insuficiencia renal oligúrica con ondas T picudas: hiperpotasemia",
    imagen: "flujogramas/hiperpotasemia-manejo-urgencia.svg",
    alt: "Flujograma: Insuficiencia renal oligúrica con ondas T picudas: hiperpotasemia"
  },
  "GIN-004": {
    titulo: "PA 145/90 a las 38 semanas sin proteinuria ni daño de órganos: hipertensión gestacional",
    imagen: "flujogramas/hipertension-gestacional-diagnostico.svg",
    alt: "Flujograma: PA 145/90 a las 38 semanas sin proteinuria ni daño de órganos: hipertensión gestacional"
  },
  "SP-002": {
    titulo: "Gestante que no habla castellano y teme dar a luz con «extraños»: parto con adecuación intercultural y acompañante",
    imagen: "flujogramas/parto-humanizado-intercultural.svg",
    alt: "Flujograma: Gestante que no habla castellano y teme dar a luz con «extraños»: parto con adecuación intercultural y acompañante"
  },
  "GIN-005": {
    titulo: "Gestante de 35 semanas con PA 150/98, transaminasas altas y creatinina 1,3: preeclampsia con severidad",
    imagen: "flujogramas/preeclampsia-con-criterios-severidad.svg",
    alt: "Flujograma: Gestante de 35 semanas con PA 150/98, transaminasas altas y creatinina 1,3: preeclampsia con severidad"
  },
  "NRL-003": {
    titulo: "Hematoma epidural de fosa posterior: cirugía inmediata",
    imagen: "flujogramas/hematoma-epidural-fosa-posterior.svg",
    alt: "Flujograma: Hematoma epidural de fosa posterior: cirugía inmediata"
  },
  "REU-003": {
    titulo: "Poliartritis de manos y muñecas con rigidez matutina: el anticuerpo más específico es el anti-CCP",
    imagen: "flujogramas/artritis-reumatoide-anticuerpos-anti-ccp.svg",
    alt: "Flujograma: Poliartritis de manos y muñecas con rigidez matutina: el anticuerpo más específico es el anti-CCP"
  },
  "INF-003": {
    titulo: "Fiebre, faringitis, adenopatías cervicales posteriores y esplenomegalia: mononucleosis infecciosa",
    imagen: "flujogramas/mononucleosis-infecciosa-veb.svg",
    alt: "Flujograma: Fiebre, faringitis, adenopatías cervicales posteriores y esplenomegalia: mononucleosis infecciosa"
  },
  "PED-005": {
    titulo: "Lactante con fiebre, adenopatías retroauriculares dolorosas y exantema que baja de la cara al tronco: rubéola",
    imagen: "flujogramas/rubeola-diagnostico-exantematico.svg",
    alt: "Flujograma: Lactante con fiebre, adenopatías retroauriculares dolorosas y exantema que baja de la cara al tronco: rubéola"
  },

  /* ---------- ENAM 2020 · preguntas 32 a 51 ---------- */

  "END-002": {
    titulo: "TSH alta con T4 libre normal: hipotiroidismo subclínico",
    imagen: "flujogramas/hipotiroidismo-subclinico-diagnostico.svg",
    alt: "Flujograma: TSH alta con T4 libre normal: hipotiroidismo subclínico"
  },
  "GIN-006": {
    titulo: "Puérpera con fiebre y zona roja, dura y caliente en la mama: mastitis, dicloxacilina sin suspender la lactancia",
    imagen: "flujogramas/mastitis-puerperal-manejo.svg",
    alt: "Flujograma: Puérpera con fiebre y zona roja, dura y caliente en la mama: mastitis, dicloxacilina sin suspender la lactancia"
  },
  "GAS-002": {
    titulo: "Diarrea con sangre, fiebre y leucocitos en heces tras comer en la calle: antibióticos",
    imagen: "flujogramas/diarrea-disenterica-antibioticoterapia.svg",
    alt: "Flujograma: Diarrea con sangre, fiebre y leucocitos en heces tras comer en la calle: antibióticos"
  },
  "SP-003": {
    titulo: "Suegra que prohíbe carne y sangrecita a la gestante: consejería nutricional a la familia",
    imagen: "flujogramas/consejeria-nutricional-gestante.svg",
    alt: "Flujograma: Suegra que prohíbe carne y sangrecita a la gestante: consejería nutricional a la familia"
  },
  "PED-006": {
    titulo: "Lactante de 11 meses con diarrea con moco y sangre y fiebre de 39 °C: Campylobacter",
    imagen: "flujogramas/diarrea-invasiva-campylobacter-lactante.svg",
    alt: "Flujograma: Lactante de 11 meses con diarrea con moco y sangre y fiebre de 39 °C: Campylobacter"
  },
  "GIN-007": {
    titulo: "Gestante de 30 semanas con fiebre, vómitos y puño percusión lumbar positiva: pielonefritis aguda",
    imagen: "flujogramas/pielonefritis-aguda-gestacion.svg",
    alt: "Flujograma: Gestante de 30 semanas con fiebre, vómitos y puño percusión lumbar positiva: pielonefritis aguda"
  },
  "OFT-003": {
    titulo: "Recién nacido con epífora, fotofobia, córnea opaca y presión ocular alta: glaucoma congénito, goniotomía",
    imagen: "flujogramas/glaucoma-congenito-goniotomia.svg",
    alt: "Flujograma: Recién nacido con epífora, fotofobia, córnea opaca y presión ocular alta: glaucoma congénito, goniotomía"
  },
  "INF-004": {
    titulo: "Úlcera genital única e indolora de 7 días con RPR negativo: chancro sifilítico",
    imagen: "flujogramas/chancro-luetico-sifilis-primaria.svg",
    alt: "Flujograma: Úlcera genital única e indolora de 7 días con RPR negativo: chancro sifilítico"
  },
  "END-003": {
    titulo: "Hipertiroidea con fiebre de 39,5 °C, FC 130 y confusión: tormenta tiroidea",
    imagen: "flujogramas/tormenta-tiroidea-crisis-tirotoxica.svg",
    alt: "Flujograma: Hipertiroidea con fiebre de 39,5 °C, FC 130 y confusión: tormenta tiroidea"
  },
  "GAS-003": {
    titulo: "Pancreatitis crónica con dolor continuo que no cede a analgésicos: bloqueo del plexo celíaco",
    imagen: "flujogramas/pancreatitis-cronica-bloqueo-celiaco.svg",
    alt: "Flujograma: Pancreatitis crónica con dolor continuo que no cede a analgésicos: bloqueo del plexo celíaco"
  },
  "PED-007": {
    titulo: "Recién nacido sano de 2700 g nacido en casa: vacunas BCG y hepatitis B",
    imagen: "flujogramas/vacunacion-neonatal-bcg-hvb.svg",
    alt: "Flujograma: Recién nacido sano de 2700 g nacido en casa: vacunas BCG y hepatitis B"
  },
  "PSI-002": {
    titulo: "Seis crisis súbitas en 2 meses de palpitaciones, disnea, temblor y miedo a morir con ECG normal: trastorno de pánico",
    imagen: "flujogramas/trastorno-de-panico-crisis-ansiedad.svg",
    alt: "Flujograma: Seis crisis súbitas en 2 meses de palpitaciones, disnea, temblor y miedo a morir con ECG normal: trastorno de pánico"
  },
  "PED-008": {
    titulo: "Recién nacido de 24 horas sin meconio, distensión leve y ano permeable: tapón meconial",
    imagen: "flujogramas/obstruccion-neonatal-tapon-meconial.svg",
    alt: "Flujograma: Recién nacido de 24 horas sin meconio, distensión leve y ano permeable: tapón meconial"
  },
  "NEF-003": {
    titulo: "Fiebre, escalofríos, dolor lumbar derecho y nitritos positivos: pielonefritis aguda",
    imagen: "flujogramas/pielonefritis-aguda-diagnostico-clinico.svg",
    alt: "Flujograma: Fiebre, escalofríos, dolor lumbar derecho y nitritos positivos: pielonefritis aguda"
  },
  "END-004": {
    titulo: "Obesa con poliuria, polifagia y padres diabéticos: la prueba de tolerancia oral a la glucosa evalúa la secreción de insulina",
    imagen: "flujogramas/tolerancia-oral-glucosa-secrecion-insulina.svg",
    alt: "Flujograma: Obesa con poliuria, polifagia y padres diabéticos: la prueba de tolerancia oral a la glucosa evalúa la secreción de insulina"
  },
  "PED-009": {
    titulo: "Lactante con resfrío que a los 3 días llora, está irritable y se coge la oreja: otitis media aguda",
    imagen: "flujogramas/otitis-media-aguda-lactante.svg",
    alt: "Flujograma: Lactante con resfrío que a los 3 días llora, está irritable y se coge la oreja: otitis media aguda"
  },
  "NEU-002": {
    titulo: "Obeso tras un viaje largo con disnea súbita, hipotensión y Homans positivo: TEP de alto riesgo, trombólisis con alteplasa",
    imagen: "flujogramas/tromboembolismo-pulmonar-alteplase.svg",
    alt: "Flujograma: Obeso tras un viaje largo con disnea súbita, hipotensión y Homans positivo: TEP de alto riesgo, trombólisis con alteplasa"
  },
  "SP-004": {
    titulo: "Publicar la foto de un paciente sin su consentimiento vulnera la autonomía (confidencialidad)",
    imagen: "flujogramas/vulneracion-principio-autonomia-confidencialidad.svg",
    alt: "Flujograma: Publicar la foto de un paciente sin su consentimiento vulnera la autonomía (confidencialidad)"
  },
  "PED-010": {
    titulo: "Escolar con tos y fiebre de 4 días, roncantes difusos y sin dificultad respiratoria: bronquitis aguda",
    imagen: "flujogramas/bronquitis-aguda-pediatrica.svg",
    alt: "Flujograma: Escolar con tos y fiebre de 4 días, roncantes difusos y sin dificultad respiratoria: bronquitis aguda"
  },
  "REU-004": {
    titulo: "Primera vez con ronchas fugaces que pican en todo el cuerpo y edema de cara: urticaria aguda",
    imagen: "flujogramas/urticaria-aguda-angioedema.svg",
    alt: "Flujograma: Primera vez con ronchas fugaces que pican en todo el cuerpo y edema de cara: urticaria aguda"
  },

  /* ---------- ENAM 2020 · preguntas 52 a 71 ---------- */

  "SP-005": {
    titulo: "Deserción escolar por embarazo adolescente: intervención educativa continua en el colegio",
    imagen: "flujogramas/prevencion-embarazo-adolescente-educacion.svg",
    alt: "Flujograma: Deserción escolar por embarazo adolescente: intervención educativa continua en el colegio"
  },
  "GAS-004": {
    titulo: "Pirosis y regurgitación que empeoran con café en un obeso, sin disfagia ni baja de peso: ERGE",
    imagen: "flujogramas/enfermedad-reflujo-gastroesofagico-erge.svg",
    alt: "Flujograma: Pirosis y regurgitación que empeoran con café en un obeso, sin disfagia ni baja de peso: ERGE"
  },
  "INF-005": {
    titulo: "VIH sin tratamiento con disnea progresiva, tos seca, infiltrado intersticial y DHL alta: neumonía por Pneumocystis",
    imagen: "flujogramas/neumonia-pneumocystis-jirovecii-vih.svg",
    alt: "Flujograma: VIH sin tratamiento con disnea progresiva, tos seca, infiltrado intersticial y DHL alta: neumonía por Pneumocystis"
  },
  "CIR-004": {
    titulo: "Puñalada infraclavicular con hipotensión, yugulares llenas, timpanismo y murmullo ausente: neumotórax a tensión",
    imagen: "flujogramas/neumotorax-a-tension-toracocentesis.svg",
    alt: "Flujograma: Puñalada infraclavicular con hipotensión, yugulares llenas, timpanismo y murmullo ausente: neumotórax a tensión"
  },
  "GIN-008": {
    titulo: "41 semanas con cuello posterior, largo, cerrado y duro (Bishop desfavorable): maduración cervical",
    imagen: "flujogramas/maduracion-cervical-embarazo-prolongado.svg",
    alt: "Flujograma: 41 semanas con cuello posterior, largo, cerrado y duro (Bishop desfavorable): maduración cervical"
  },
  "SP-006": {
    titulo: "Expertos que recomiendan un fármaco sin declarar que el laboratorio los financió: conflicto de intereses",
    imagen: "flujogramas/conflicto-de-intereses-bioetica.svg",
    alt: "Flujograma: Expertos que recomiendan un fármaco sin declarar que el laboratorio los financió: conflicto de intereses"
  },
  "GIN-009": {
    titulo: "Atraso de 2 días con β-hCG positiva y ectópico previo: ecografía transvaginal",
    imagen: "flujogramas/embarazo-ectopico-ecografia-transvaginal.svg",
    alt: "Flujograma: Atraso de 2 días con β-hCG positiva y ectópico previo: ecografía transvaginal"
  },
  "REU-005": {
    titulo: "Lactante con prurito nocturno, pápulas y vesículas en palmas y plantas y madre igual: escabiosis",
    imagen: "flujogramas/acarosis-escabiosis-lactante-permetrina.svg",
    alt: "Flujograma: Lactante con prurito nocturno, pápulas y vesículas en palmas y plantas y madre igual: escabiosis"
  },
  "GAS-005": {
    titulo: "Mujer de 52 años con cambio del ritmo defecatorio y madre con poliposis adenomatosa familiar: colonoscopia",
    imagen: "flujogramas/screening-cancer-colorrectal-colonoscopia.svg",
    alt: "Flujograma: Mujer de 52 años con cambio del ritmo defecatorio y madre con poliposis adenomatosa familiar: colonoscopia"
  },
  "CIR-005": {
    titulo: "Quemadura en los primeros minutos: enfriar con agua a temperatura ambiente para frenar la profundidad",
    imagen: "flujogramas/quemaduras-irrigacion-agua-ambiente.svg",
    alt: "Flujograma: Quemadura en los primeros minutos: enfriar con agua a temperatura ambiente para frenar la profundidad"
  },
  "CAR-004": {
    titulo: "PA 160/100 confirmada con choque de punta desplazado (hipertrofia del VI): iniciar antihipertensivo y estudiar",
    imagen: "flujogramas/hipertension-arterial-grado-2-tratamiento.svg",
    alt: "Flujograma: PA 160/100 confirmada con choque de punta desplazado (hipertrofia del VI): iniciar antihipertensivo y estudiar"
  },
  "NRL-004": {
    titulo: "Alcohólico con anemia macrocítica (VCM 120), parestesias y paraparesia espástica: déficit de vitamina B12",
    imagen: "flujogramas/deficit-vitamina-b12-degeneracion-cordonal.svg",
    alt: "Flujograma: Alcohólico con anemia macrocítica (VCM 120), parestesias y paraparesia espástica: déficit de vitamina B12"
  },
  "GIN-010": {
    titulo: "Gestante de 36 semanas en nalgas con contracciones en un centro de salud: referir a un establecimiento de mayor nivel",
    imagen: "flujogramas/parto-podalico-referencia-quirurgica.svg",
    alt: "Flujograma: Gestante de 36 semanas en nalgas con contracciones en un centro de salud: referir a un establecimiento de mayor nivel"
  },
  "CAR-005": {
    titulo: "Neonato de 15 días con cianosis, polipnea y corazón «en huevo» con pedículo estrecho: transposición de grandes arterias",
    imagen: "flujogramas/transposicion-de-grandes-arterias-tga.svg",
    alt: "Flujograma: Neonato de 15 días con cianosis, polipnea y corazón «en huevo» con pedículo estrecho: transposición de grandes arterias"
  },
  "SP-007": {
    titulo: "El investigador asigna la intervención por conveniencia (sin azar): diseño cuasi experimental",
    imagen: "flujogramas/diseno-cuasi-experimental-epidemiologia.svg",
    alt: "Flujograma: El investigador asigna la intervención por conveniencia (sin azar): diseño cuasi experimental"
  },
  "PSI-003": {
    titulo: "Adolescente que hiperventila tras una discusión, con parestesias, espasmo carpopedal y alcalosis respiratoria: reinhalar CO₂",
    imagen: "flujogramas/hiperventilacion-alcalosis-respiratoria-bolsa.svg",
    alt: "Flujograma: Adolescente que hiperventila tras una discusión, con parestesias, espasmo carpopedal y alcalosis respiratoria: reinhalar CO₂"
  },
  "TRA-002": {
    titulo: "Lactante de 2 meses con aductores tensos y asimetría de miembros: ecografía de cadera",
    imagen: "flujogramas/displasia-desarrollo-cadera-ecografia.svg",
    alt: "Flujograma: Lactante de 2 meses con aductores tensos y asimetría de miembros: ecografía de cadera"
  },
  "PED-011": {
    titulo: "Recién nacido macrosómico de 24 horas hipoactivo sin signos de sepsis: hipoglucemia",
    imagen: "flujogramas/hipoglicemia-neonatal-hijo-madre-diabetica.svg",
    alt: "Flujograma: Recién nacido macrosómico de 24 horas hipoactivo sin signos de sepsis: hipoglucemia"
  },
  "PED-012": {
    titulo: "Niño de 8 años con peso para la talla bajo y talla para la edad normal: desnutrición aguda",
    imagen: "flujogramas/desnutricion-aguda-emaciacion-antropometria.svg",
    alt: "Flujograma: Niño de 8 años con peso para la talla bajo y talla para la edad normal: desnutrición aguda"
  },
  "SP-008": {
    titulo: "El monitoreo de la prevención y el tratamiento de la anemia infantil es responsabilidad de todo el personal de salud",
    imagen: "flujogramas/plan-nacional-anemia-equipo-salud.svg",
    alt: "Flujograma: El monitoreo de la prevención y el tratamiento de la anemia infantil es responsabilidad de todo el personal de salud"
  },

  /* ---------- ENAM 2020 · bloque 2 (preguntas 72 a 122) ---------- */

  "CAR-006": {
    titulo: "Dolor retroesternal de 2 horas con ST elevado en II, III y aVF: infarto agudo de miocardio inferior",
    imagen: "flujogramas/infarto-agudo-miocardio-inferior.svg",
    alt: "Flujograma: Dolor retroesternal de 2 horas con ST elevado en II, III y aVF: infarto agudo de miocardio inferior"
  },
  "CB-002": {
    titulo: "Diabético con atorvastatina + gemfibrozilo y dolor muscular en las piernas: mialgias por medicamentos",
    imagen: "flujogramas/mialgias-estatinas-gemfibrozilo.svg",
    alt: "Flujograma: Diabético con atorvastatina + gemfibrozilo y dolor muscular en las piernas: mialgias por medicamentos"
  },
  "CB-003": {
    titulo: "Trabajadora de invernadero con miosis, sialorrea, sudoración, roncantes y bradicardia: organofosforados, atropina",
    imagen: "flujogramas/intoxicacion-organofosforados-atropina.svg",
    alt: "Flujograma: Trabajadora de invernadero con miosis, sialorrea, sudoración, roncantes y bradicardia: organofosforados, atropina"
  },
  "CIR-006": {
    titulo: "Telangiectasias en muslos y piernas sin edema ni cambios de piel (CEAP C1): escleroterapia",
    imagen: "flujogramas/telangiectasias-escleroterapia.svg",
    alt: "Flujograma: Telangiectasias en muslos y piernas sin edema ni cambios de piel (CEAP C1): escleroterapia"
  },
  "CIR-007": {
    titulo: "Quemadura de la cara anterior del tronco y todo el miembro superior derecho: 27 % por la regla de los 9",
    imagen: "flujogramas/regla-de-los-nueves-quemaduras.svg",
    alt: "Flujograma: Quemadura de la cara anterior del tronco y todo el miembro superior derecho: 27 % por la regla de los 9"
  },
  "CIR-008": {
    titulo: "Quemado de cara por explosión con dificultad respiratoria y tirajes: intubación orotraqueal inmediata",
    imagen: "flujogramas/injuria-inhalatoria-intubacion-precoz.svg",
    alt: "Flujograma: Quemado de cara por explosión con dificultad respiratoria y tirajes: intubación orotraqueal inmediata"
  },
  "END-005": {
    titulo: "Frío, estreñimiento y piel seca con TSH alta, T4 libre baja y dislipidemia: levotiroxina",
    imagen: "flujogramas/hipotiroidismo-primario-levotiroxina.svg",
    alt: "Flujograma: Frío, estreñimiento y piel seca con TSH alta, T4 libre baja y dislipidemia: levotiroxina"
  },
  "GIN-011": {
    titulo: "42 semanas con menos movimientos, oligoamnios severo y desaceleraciones repetidas: cesárea inmediata",
    imagen: "flujogramas/embarazo-postermino-cesarea-emergencia.svg",
    alt: "Flujograma: 42 semanas con menos movimientos, oligoamnios severo y desaceleraciones repetidas: cesárea inmediata"
  },
  "GIN-012": {
    titulo: "Amenaza de parto pretérmino a las 32 semanas: maduración pulmonar con betametasona",
    imagen: "flujogramas/maduracion-pulmonar-fetal-betametasona.svg",
    alt: "Flujograma: Amenaza de parto pretérmino a las 32 semanas: maduración pulmonar con betametasona"
  },
  "GIN-013": {
    titulo: "Dolor hipogástrico, sangrado irregular, varias parejas y dolor a la movilización del cuello: enfermedad pélvica inflamatoria",
    imagen: "flujogramas/enfermedad-pelvica-inflamatoria-frenkel.svg",
    alt: "Flujograma: Dolor hipogástrico, sangrado irregular, varias parejas y dolor a la movilización del cuello: enfermedad pélvica inflamatoria"
  },
  "HEM-003": {
    titulo: "Resección del íleon terminal con palidez, glositis e ictericia: anemia megaloblástica por falta de B12",
    imagen: "flujogramas/anemia-megaloblastica-reseccion-ileon.svg",
    alt: "Flujograma: Resección del íleon terminal con palidez, glositis e ictericia: anemia megaloblástica por falta de B12"
  },
  "NEF-004": {
    titulo: "Escolar con hematuria, edema palpebral, hipertensión y C3 bajo 10 días después de una faringitis: glomerulonefritis",
    imagen: "flujogramas/glomerulonefritis-postestreptococica-c3.svg",
    alt: "Flujograma: Escolar con hematuria, edema palpebral, hipertensión y C3 bajo 10 días después de una faringitis: glomerulonefritis"
  },
  "PED-013": {
    titulo: "Neonato de 3 días hijo de RPM de 72 horas con taquipnea, leucocitosis e infiltrado bilateral: ampicilina + amikacina",
    imagen: "flujogramas/sepsis-neonatal-temprana-ampicilina-amikacina.svg",
    alt: "Flujograma: Neonato de 3 días hijo de RPM de 72 horas con taquipnea, leucocitosis e infiltrado bilateral: ampicilina + amikacina"
  },
  "PED-014": {
    titulo: "Preescolar con fiebre y lesiones muy pruriginosas en distintos estadios en cuero cabelludo, cara y tronco: varicela",
    imagen: "flujogramas/varicela-diagnostico-clinico.svg",
    alt: "Flujograma: Preescolar con fiebre y lesiones muy pruriginosas en distintos estadios en cuero cabelludo, cara y tronco: varicela"
  },
  "PED-015": {
    titulo: "Lactante con estenosis hipertrófica del píloro: antes de operar, rehidratar y corregir electrolitos",
    imagen: "flujogramas/estenosis-hipertrofica-piloro-rehidratacion.svg",
    alt: "Flujograma: Lactante con estenosis hipertrófica del píloro: antes de operar, rehidratar y corregir electrolitos"
  },
  "PED-016": {
    titulo: "Disfonía y fiebre seguidas de estridor inspiratorio y tos perruna de noche: laringotraqueítis (crup)",
    imagen: "flujogramas/laringotraqueitis-crup-estridor.svg",
    alt: "Flujograma: Disfonía y fiebre seguidas de estridor inspiratorio y tos perruna de noche: laringotraqueítis (crup)"
  },
  "PED-017": {
    titulo: "Niño de 3 años con resfrío, fiebre, irritabilidad y tímpano congestivo y abombado: amoxicilina",
    imagen: "flujogramas/otitis-media-aguda-amoxicilina.svg",
    alt: "Flujograma: Niño de 3 años con resfrío, fiebre, irritabilidad y tímpano congestivo y abombado: amoxicilina"
  },
  "REU-006": {
    titulo: "Pústulas dolorosas recurrentes alrededor de los folículos de la barba: foliculitis estafilocócica, dicloxacilina",
    imagen: "flujogramas/foliculitis-estafilococica-dicloxacilina.svg",
    alt: "Flujograma: Pústulas dolorosas recurrentes alrededor de los folículos de la barba: foliculitis estafilocócica, dicloxacilina"
  },
  "SP-009": {
    titulo: "Padres de un adolescente de 15 años rechazan un procedimiento diagnóstico necesario: comunicar a la fiscalía",
    imagen: "flujogramas/rechazo-tratamiento-menor-fiscalia.svg",
    alt: "Flujograma: Padres de un adolescente de 15 años rechazan un procedimiento diagnóstico necesario: comunicar a la fiscalía"
  },
  "SP-010": {
    titulo: "Obeso con glucemia de 150 que inicia tratamiento y educación estructurada: prevención secundaria",
    imagen: "flujogramas/prevencion-secundaria-diabetes-obesidad.svg",
    alt: "Flujograma: Obeso con glucemia de 150 que inicia tratamiento y educación estructurada: prevención secundaria"
  },
  "SP-011": {
    titulo: "Gestantes que llegan a término sin ningún control prenatal: captación y seguimiento",
    imagen: "flujogramas/captacion-precoz-control-prenatal.svg",
    alt: "Flujograma: Gestantes que llegan a término sin ningún control prenatal: captación y seguimiento"
  },
  "SP-012": {
    titulo: "EsSalud atiende a los trabajadores del sector formal y a sus derechohabientes",
    imagen: "flujogramas/poblacion-asegurada-essalud.svg",
    alt: "Flujograma: EsSalud atiende a los trabajadores del sector formal y a sus derechohabientes"
  },
  "SP-013": {
    titulo: "De 2-3 casos semanales a 100 en una semana y luego de vuelta a 2: brote",
    imagen: "flujogramas/definicion-epidemiologica-brote.svg",
    alt: "Flujograma: De 2-3 casos semanales a 100 en una semana y luego de vuelta a 2: brote"
  },
  "TRA-003": {
    titulo: "Herida cortante en la palma que impide cerrar el puño: lesión de los tendones flexores (flexor superficial)",
    imagen: "flujogramas/seccion-tendon-palmar-menor.svg",
    alt: "Flujograma: Herida cortante en la palma que impide cerrar el puño: lesión de los tendones flexores (flexor superficial)"
  },
  "TRA-004": {
    titulo: "Muslo muy hinchado tras accidente con dolor a la extensión, parestesias y sin pulsos distales: fasciotomía",
    imagen: "flujogramas/sindrome-compartimental-fasciotomia.svg",
    alt: "Flujograma: Muslo muy hinchado tras accidente con dolor a la extensión, parestesias y sin pulsos distales: fasciotomía"
  },

  /* ---------- ENAM 2020 · bloque 3 (preguntas 123 a 172) ---------- */

  "INF-008": {
    titulo: "Neumonía al 5.º día de ventilación mecánica con choque: meropenem + vancomicina + amikacina",
    imagen: "flujogramas/neumonia-asociada-ventilador-meropenem-vancomicina.svg",
    alt: "Flujograma: Neumonía al 5.º día de ventilación mecánica con choque: meropenem + vancomicina + amikacina"
  },
  "TRA-005": {
    titulo: "Niño de 12 años con giba en la prueba de Adams y curva lateral en la Rx: escoliosis estructural",
    imagen: "flujogramas/escoliosis-estructural-test-adams.svg",
    alt: "Flujograma: Niño de 12 años con giba en la prueba de Adams y curva lateral en la Rx: escoliosis estructural"
  },
  "PED-022": {
    titulo: "Recién nacido de 3 días con vómitos, deshidratación severa, hipotensión y llenado lento sin signos de infección: choque hipovolémico",
    imagen: "flujogramas/shock-hipovolemico-deshidratacion-neonatal.svg",
    alt: "Flujograma: Recién nacido de 3 días con vómitos, deshidratación severa, hipotensión y llenado lento sin signos de infección: choque hipovolémico"
  },
  "GIN-016": {
    titulo: "Saco gestacional de 20 mm sin embrión a las 6 semanas: gestación anembrionada probable",
    imagen: "flujogramas/gestacion-anembrionada-huevo-huero.svg",
    alt: "Flujograma: Saco gestacional de 20 mm sin embrión a las 6 semanas: gestación anembrionada probable"
  },
  "PED-023": {
    titulo: "Lactante de 45 días con tos ferina: la leucocitosis extrema (> 50 000) es el factor de peor pronóstico",
    imagen: "flujogramas/tos-ferina-reaccion-leucemoide.svg",
    alt: "Flujograma: Lactante de 45 días con tos ferina: la leucocitosis extrema (> 50 000) es el factor de peor pronóstico"
  },
  "PED-024": {
    titulo: "Lactante de 9 meses con llanto intermitente, letargia, heces con moco y sangre y masa en el abdomen: invaginación intestinal",
    imagen: "flujogramas/intususcepcion-invaginacion-intestinal-pediatria.svg",
    alt: "Flujograma: Lactante de 9 meses con llanto intermitente, letargia, heces con moco y sangre y masa en el abdomen: invaginación intestinal"
  },
  "INF-009": {
    titulo: "3 semanas de febrícula y sudor nocturno con cefalea, vómitos, somnolencia y signos meníngeos: meningitis tuberculosa, ADA en LCR",
    imagen: "flujogramas/meningitis-tuberculosa-ada-lcr.svg",
    alt: "Flujograma: 3 semanas de febrícula y sudor nocturno con cefalea, vómitos, somnolencia y signos meníngeos: meningitis tuberculosa, ADA en LCR"
  },
  "PED-025": {
    titulo: "Preescolar tras paseo agrícola con sialorrea, broncorrea, diarrea, sudoración y fasciculaciones: organofosforados",
    imagen: "flujogramas/intoxicacion-organofosforados-pediatria.svg",
    alt: "Flujograma: Preescolar tras paseo agrícola con sialorrea, broncorrea, diarrea, sudoración y fasciculaciones: organofosforados"
  },
  "SP-017": {
    titulo: "Niño con diarreas repetidas y talla baja que vive con piso de tierra, sin agua ni desagüe: vivienda y servicios básicos",
    imagen: "flujogramas/determinantes-sociales-saneamiento-desnutricion.svg",
    alt: "Flujograma: Niño con diarreas repetidas y talla baja que vive con piso de tierra, sin agua ni desagüe: vivienda y servicios básicos"
  },
  "CB-004": {
    titulo: "Alcohólico confuso con respiración de Kussmaul, ceguera y acidosis metabólica (pH 7,20): intoxicación por metanol",
    imagen: "flujogramas/intoxicacion-metanol-acidosis-amaurosis.svg",
    alt: "Flujograma: Alcohólico confuso con respiración de Kussmaul, ceguera y acidosis metabólica (pH 7,20): intoxicación por metanol"
  },
  "PED-026": {
    titulo: "Preescolar de 2 años convulsionando en emergencia: diazepam (benzodiacepina) de inmediato",
    imagen: "flujogramas/convulsion-febril-status-diazepam.svg",
    alt: "Flujograma: Preescolar de 2 años convulsionando en emergencia: diazepam (benzodiacepina) de inmediato"
  },
  "NEF-008": {
    titulo: "Cólico lumbar derecho irradiado al testículo en un obeso: tomografía sin contraste (UroTAC)",
    imagen: "flujogramas/colico-renoureteral-urotac-urotem.svg",
    alt: "Flujograma: Cólico lumbar derecho irradiado al testículo en un obeso: tomografía sin contraste (UroTAC)"
  },
  "PED-027": {
    titulo: "Fiebre de 40 °C de 24 horas con taquipnea y crepitantes en la base derecha: infiltrado alveolar en el hemitórax derecho inferior",
    imagen: "flujogramas/neumonia-bacteriana-consolidacion-alveolar.svg",
    alt: "Flujograma: Fiebre de 40 °C de 24 horas con taquipnea y crepitantes en la base derecha: infiltrado alveolar en el hemitórax derecho inferior"
  },
  "GIN-017": {
    titulo: "Flujo blanco grumoso con prurito vaginal: vaginitis micótica (candidiasis)",
    imagen: "flujogramas/candidiasis-vulvovaginal-micotica.svg",
    alt: "Flujograma: Flujo blanco grumoso con prurito vaginal: vaginitis micótica (candidiasis)"
  },
  "GIN-018": {
    titulo: "Gran multípara con sangrado abundante tras el parto e hipotensión: palpar el tono del útero primero",
    imagen: "flujogramas/atonia-uterina-palpacion-bimanual.svg",
    alt: "Flujograma: Gran multípara con sangrado abundante tras el parto e hipotensión: palpar el tono del útero primero"
  },
  "REU-007": {
    titulo: "Joven con artralgias, febrícula, púrpura palpable y livedo: vasculitis",
    imagen: "flujogramas/vasculitis-leucocitoclastica-purpura-palpable.svg",
    alt: "Flujograma: Joven con artralgias, febrícula, púrpura palpable y livedo: vasculitis"
  },
  "GIN-019": {
    titulo: "Prueba rápida de VIH positiva en trabajo de parto inicial con membranas íntegras y sin TAR: cesárea",
    imagen: "flujogramas/vih-intraparto-cesarea-emergencia.svg",
    alt: "Flujograma: Prueba rápida de VIH positiva en trabajo de parto inicial con membranas íntegras y sin TAR: cesárea"
  },
  "CB-005": {
    titulo: "Dificultad respiratoria e hipotensión tras penicilina IM (hipersensibilidad tipo I): el mastocito",
    imagen: "flujogramas/anafilaxia-mastocitos-hipersensibilidad-tipo-i.svg",
    alt: "Flujograma: Dificultad respiratoria e hipotensión tras penicilina IM (hipersensibilidad tipo I): el mastocito"
  },
  "NEU-004": {
    titulo: "Exudado pleural linfocítico con ADA de 55 U/L en un joven con tos de 2 meses: tuberculosis pleural",
    imagen: "flujogramas/pleuresia-tuberculosa-ada-exudado.svg",
    alt: "Flujograma: Exudado pleural linfocítico con ADA de 55 U/L en un joven con tos de 2 meses: tuberculosis pleural"
  },
  "PED-028": {
    titulo: "Niño de 15 meses con petequias, equimosis y epistaxis 2 semanas tras la vacuna, plaquetas 20 000 y resto normal: PTI",
    imagen: "flujogramas/purpura-trombocitopenica-inmune-postvacunal.svg",
    alt: "Flujograma: Niño de 15 meses con petequias, equimosis y epistaxis 2 semanas tras la vacuna, plaquetas 20 000 y resto normal: PTI"
  },
  "PED-029": {
    titulo: "Urocultivo negativo en un niño con fiebre y síntomas urinarios: lo más probable es que haya recibido antibiótico",
    imagen: "flujogramas/urocultivo-falso-negativo-antibioticos.svg",
    alt: "Flujograma: Urocultivo negativo en un niño con fiebre y síntomas urinarios: lo más probable es que haya recibido antibiótico"
  },
  "PED-030": {
    titulo: "Adolescente asmático con años de congestión, prurito y secreción nasal y pérdida del olfato: rinitis alérgica",
    imagen: "flujogramas/rinitis-alergica-asma-atopica.svg",
    alt: "Flujograma: Adolescente asmático con años de congestión, prurito y secreción nasal y pérdida del olfato: rinitis alérgica"
  },
  "NRL-005": {
    titulo: "Disartria y dificultad para caminar súbitas que desaparecen en 30 minutos: ataque isquémico transitorio",
    imagen: "flujogramas/accidente-isquemico-transitorio-ait.svg",
    alt: "Flujograma: Disartria y dificultad para caminar súbitas que desaparecen en 30 minutos: ataque isquémico transitorio"
  },
  "NRL-006": {
    titulo: "Accidente de tránsito hace 6 horas con Glasgow 10 y TC cerebral: hematoma epidural",
    imagen: "flujogramas/hematoma-epidural-arteria-meningea-media.svg",
    alt: "Flujograma: Accidente de tránsito hace 6 horas con Glasgow 10 y TC cerebral: hematoma epidural"
  },
  "PSI-006": {
    titulo: "Autoagresiones, impulsividad, promiscuidad, consumo de sustancias y relaciones caóticas: personalidad límite",
    imagen: "flujogramas/trastorno-personalidad-limite-borderline.svg",
    alt: "Flujograma: Autoagresiones, impulsividad, promiscuidad, consumo de sustancias y relaciones caóticas: personalidad límite"
  },
  "CIR-013": {
    titulo: "Mujer mayor con dolor y masa dolorosa debajo del pliegue inguinal, vómitos y distensión: hernia crural complicada",
    imagen: "flujogramas/hernia-crural-femoral-complicada.svg",
    alt: "Flujograma: Mujer mayor con dolor y masa dolorosa debajo del pliegue inguinal, vómitos y distensión: hernia crural complicada"
  },
  "SP-018": {
    titulo: "Trabajadores con tuberculosis tras remodelar consultorios: maximizar la ventilación natural (control ambiental)",
    imagen: "flujogramas/tuberculosis-control-ambiental-ventilacion.svg",
    alt: "Flujograma: Trabajadores con tuberculosis tras remodelar consultorios: maximizar la ventilación natural (control ambiental)"
  },
  "CB-006": {
    titulo: "Consumidor de anfetaminas con cefalea, agitación y PA 140/110: sube la resistencia periférica",
    imagen: "flujogramas/anfetaminas-resistencia-periferica-vasoconstriccion.svg",
    alt: "Flujograma: Consumidor de anfetaminas con cefalea, agitación y PA 140/110: sube la resistencia periférica"
  },
  "GIN-020": {
    titulo: "Fase activa con 6 cm y contracciones débiles (3 en 10 minutos de 30 segundos): conducción con oxitocina",
    imagen: "flujogramas/hipodinamia-uterina-estimulacion-oxitocina.svg",
    alt: "Flujograma: Fase activa con 6 cm y contracciones débiles (3 en 10 minutos de 30 segundos): conducción con oxitocina"
  },
  "GIN-021": {
    titulo: "Amenorrea que responde a progesterona, infertilidad, obesidad, acné y seborrea: factor ovárico (SOP)",
    imagen: "flujogramas/sindrome-ovario-poliquistico-factor-ovarico.svg",
    alt: "Flujograma: Amenorrea que responde a progesterona, infertilidad, obesidad, acné y seborrea: factor ovárico (SOP)"
  },
  "PED-031": {
    titulo: "Niño de Cerro de Pasco con dolor abdominal, hiperactividad, talla baja y anemia microcítica: intoxicación por plomo",
    imagen: "flujogramas/saturnismo-intoxicacion-cronica-plomo.svg",
    alt: "Flujograma: Niño de Cerro de Pasco con dolor abdominal, hiperactividad, talla baja y anemia microcítica: intoxicación por plomo"
  },
  "GIN-022": {
    titulo: "Primigesta de 25 semanas con cefalea y PA 160/110 en un centro de salud I-3: referir a un establecimiento obstétrico de mayor nivel",
    imagen: "flujogramas/hipertension-severa-gestacion-referencia.svg",
    alt: "Flujograma: Primigesta de 25 semanas con cefalea y PA 160/110 en un centro de salud I-3: referir a un establecimiento obstétrico de mayor nivel"
  },
  "GIN-023": {
    titulo: "Prolapso uterino total con úlceras sangrantes en una mujer de 62 años: estrógenos tópicos antes de operar",
    imagen: "flujogramas/prolapso-genital-ulceras-estrogenos-topicos.svg",
    alt: "Flujograma: Prolapso uterino total con úlceras sangrantes en una mujer de 62 años: estrógenos tópicos antes de operar"
  },
  "OFT-005": {
    titulo: "Escolar con prurito ocular intenso bilateral, secreción mucoide, lagrimeo y ojo rojo: conjuntivitis alérgica",
    imagen: "flujogramas/conjuntivitis-alergica-prurito-bilateral.svg",
    alt: "Flujograma: Escolar con prurito ocular intenso bilateral, secreción mucoide, lagrimeo y ojo rojo: conjuntivitis alérgica"
  },
  "SP-019": {
    titulo: "Caso febril de Piura atendido en Lima con aumento de mosquitos: priorizar el control vectorial",
    imagen: "flujogramas/dengue-control-vectorial-aedes.svg",
    alt: "Flujograma: Caso febril de Piura atendido en Lima con aumento de mosquitos: priorizar el control vectorial"
  },
  "CAR-009": {
    titulo: "Pérdida súbita de conciencia, respiración agónica y sin pulso: iniciar compresiones torácicas",
    imagen: "flujogramas/paro-cardiorrespiratorio-compresiones-toracicas.svg",
    alt: "Flujograma: Pérdida súbita de conciencia, respiración agónica y sin pulso: iniciar compresiones torácicas"
  },
  "REU-008": {
    titulo: "Escolar con placas descamativas que crecen en anillo, pelo frágil y zonas sin pelo en el cuero cabelludo: tiña capitis",
    imagen: "flujogramas/tinea-capitis-dermatofitosis-cuero-cabelludo.svg",
    alt: "Flujograma: Escolar con placas descamativas que crecen en anillo, pelo frágil y zonas sin pelo en el cuero cabelludo: tiña capitis"
  },
  "NRL-007": {
    titulo: "Tras raquianestesia: pérdida motora y sensitiva de piernas con disfunción vesical e intestinal: síndrome de cola de caballo",
    imagen: "flujogramas/sindrome-cola-caballo-anestesia-raquidea.svg",
    alt: "Flujograma: Tras raquianestesia: pérdida motora y sensitiva de piernas con disfunción vesical e intestinal: síndrome de cola de caballo"
  },
  "NEF-009": {
    titulo: "Adolescente con dolor testicular de 6 horas, testículo horizontal y reflejo cremastérico ausente: torsión testicular",
    imagen: "flujogramas/torsion-testicular-reflejo-cremasterico.svg",
    alt: "Flujograma: Adolescente con dolor testicular de 6 horas, testículo horizontal y reflejo cremastérico ausente: torsión testicular"
  },
  "GIN-024": {
    titulo: "Multípara de 37 semanas con contracciones dolorosas, útero hipertónico y sangrado oscuro: desprendimiento prematuro de placenta",
    imagen: "flujogramas/desprendimiento-prematuro-placenta-hipertonia.svg",
    alt: "Flujograma: Multípara de 37 semanas con contracciones dolorosas, útero hipertónico y sangrado oscuro: desprendimiento prematuro de placenta"
  },
  "GIN-025": {
    titulo: "Sangrado en la posmenopausia con endometrio de 8 mm: biopsia de endometrio",
    imagen: "flujogramas/metrorragia-posmenopausica-biopsia-endometrio.svg",
    alt: "Flujograma: Sangrado en la posmenopausia con endometrio de 8 mm: biopsia de endometrio"
  },
  "CAR-010": {
    titulo: "Fiebre de 6 semanas, fiebre reumática previa, extracción dental, soplo mitral y hemiparesia: endocarditis, eco transesofágico",
    imagen: "flujogramas/endocarditis-infecciosa-ecocardiografia-transesofagica.svg",
    alt: "Flujograma: Fiebre de 6 semanas, fiebre reumática previa, extracción dental, soplo mitral y hemiparesia: endocarditis, eco transesofágico"
  },
  "GIN-026": {
    titulo: "Fondo uterino en el borde superior del pubis: 12 semanas de gestación",
    imagen: "flujogramas/altura-uterina-12-semanas-sinfisis-pubis.svg",
    alt: "Flujograma: Fondo uterino en el borde superior del pubis: 12 semanas de gestación"
  },
  "PED-032": {
    titulo: "Escolar con malos hábitos de higiene, agua sin hervir, fiebre, dolor abdominal y coluria: hepatitis A",
    imagen: "flujogramas/hepatitis-a-coluria-escolar.svg",
    alt: "Flujograma: Escolar con malos hábitos de higiene, agua sin hervir, fiebre, dolor abdominal y coluria: hepatitis A"
  },
  "GIN-027": {
    titulo: "33 semanas con contracciones cada 10-15 minutos, pérdida del tapón y cuello blando de 1 cm sin dilatación: amenaza de parto pretérmino",
    imagen: "flujogramas/amenaza-parto-pretermino-cervix-cerrado.svg",
    alt: "Flujograma: 33 semanas con contracciones cada 10-15 minutos, pérdida del tapón y cuello blando de 1 cm sin dilatación: amenaza de parto pretérmino"
  },
  "INF-010": {
    titulo: "Fiebre, dolor retroocular, epistaxis y petequias en Madre de Dios: dengue con signos de alarma",
    imagen: "flujogramas/dengue-con-signos-alarma-madre-de-dios.svg",
    alt: "Flujograma: Fiebre, dolor retroocular, epistaxis y petequias en Madre de Dios: dengue con signos de alarma"
  },
  "CAR-011": {
    titulo: "Disnea paroxística nocturna, ortopnea, crepitantes, ingurgitación yugular y edemas con PA conservada: furosemida",
    imagen: "flujogramas/insuficiencia-cardiaca-aguda-furosemida-diureticos.svg",
    alt: "Flujograma: Disnea paroxística nocturna, ortopnea, crepitantes, ingurgitación yugular y edemas con PA conservada: furosemida"
  },
  "NEU-005": {
    titulo: "Disnea progresiva y tos seca de un año con crepitantes en las bases sin exposición a polvos: enfermedad pulmonar intersticial",
    imagen: "flujogramas/enfermedad-pulmonar-intersticial-crepitantes.svg",
    alt: "Flujograma: Disnea progresiva y tos seca de un año con crepitantes en las bases sin exposición a polvos: enfermedad pulmonar intersticial"
  },
  "GIN-028": {
    titulo: "Atraso de 2 semanas con sangrado escaso, útero de 8 cm y cuello cerrado: ecografía transvaginal",
    imagen: "flujogramas/metrorragia-primer-trimestre-ecografia-transvaginal.svg",
    alt: "Flujograma: Atraso de 2 semanas con sangrado escaso, útero de 8 cm y cuello cerrado: ecografía transvaginal"
  },

  /* ---------- ENAM 2020 · bloque 2 (preguntas pendientes) ---------- */

  "CAR-007": {
    titulo: "Estenosis mitral reumática con pulso deficitario (fibrilación auricular): anticoagular con warfarina",
    imagen: "flujogramas/estenosis-mitral-fibrilacion-auricular-warfarina.svg",
    alt: "Flujograma: Estenosis mitral reumática con pulso deficitario (fibrilación auricular): anticoagular con warfarina"
  },
  "CAR-008": {
    titulo: "Síncope con taquicardia ventricular no sostenida y bloqueo de rama derecha en el sur del Perú: miocardiopatía chagásica, amiodarona",
    imagen: "flujogramas/miocardiopatia-chagasica-taquicardia-ventricular-amiodarona.svg",
    alt: "Flujograma: Síncope con taquicardia ventricular no sostenida y bloqueo de rama derecha en el sur del Perú: miocardiopatía chagásica, amiodarona"
  },
  "CIR-009": {
    titulo: "Anciana con fibrilación auricular y pie frío, cianótico, necrosado, sin pulsos ni movilidad: amputación primaria",
    imagen: "flujogramas/isquemia-arterial-aguda-rutherford-amputacion.svg",
    alt: "Flujograma: Anciana con fibrilación auricular y pie frío, cianótico, necrosado, sin pulsos ni movilidad: amputación primaria"
  },
  "CIR-010": {
    titulo: "Dolor testicular y aumento de volumen al 4.º día de una hernioplastia inguinal: orquitis isquémica",
    imagen: "flujogramas/orquitis-isquemica-post-hernioplastia.svg",
    alt: "Flujograma: Dolor testicular y aumento de volumen al 4.º día de una hernioplastia inguinal: orquitis isquémica"
  },
  "CIR-011": {
    titulo: "Accidente de tránsito con abdomen distendido, doloroso y sin ruidos intestinales: traumatismo abdominal cerrado",
    imagen: "flujogramas/trauma-abdominal-cerrado-fast.svg",
    alt: "Flujograma: Accidente de tránsito con abdomen distendido, doloroso y sin ruidos intestinales: traumatismo abdominal cerrado"
  },
  "CIR-012": {
    titulo: "Orificio perianal que drena pus 4 meses después del drenaje de un absceso: fístula perianal",
    imagen: "flujogramas/fistula-perianal-goodsall.svg",
    alt: "Flujograma: Orificio perianal que drena pus 4 meses después del drenaje de un absceso: fístula perianal"
  },
  "GAS-006": {
    titulo: "Epigastralgia que calma con alimentos y antiácidos y luego melena: úlcera gastroduodenal sangrante",
    imagen: "flujogramas/hemorragia-digestiva-alta-ulcera-peptica.svg",
    alt: "Flujograma: Epigastralgia que calma con alimentos y antiácidos y luego melena: úlcera gastroduodenal sangrante"
  },
  "GAS-007": {
    titulo: "Alcohólico con hematemesis de 1200 mL, hipotensión, palmas hepáticas, ictericia y esplenomegalia: várices esofágicas sangrantes",
    imagen: "flujogramas/hemorragia-variceal-hipertension-portal.svg",
    alt: "Flujograma: Alcohólico con hematemesis de 1200 mL, hipotensión, palmas hepáticas, ictericia y esplenomegalia: várices esofágicas sangrantes"
  },
  "GIN-014": {
    titulo: "9 semanas con dolor leve, sangrado escaso, cuello cerrado y embrión con latido: amenaza de aborto",
    imagen: "flujogramas/amenaza-de-aborto-primer-trimestre.svg",
    alt: "Flujograma: 9 semanas con dolor leve, sangrado escaso, cuello cerrado y embrión con latido: amenaza de aborto"
  },
  "GIN-015": {
    titulo: "Hipermenorrea con anemia (Hb 8) por mioma submucoso de 38 mm en mujer que desea fertilidad: miomectomía histeroscópica",
    imagen: "flujogramas/mioma-submucoso-miomectomia-histeroscopica.svg",
    alt: "Flujograma: Hipermenorrea con anemia (Hb 8) por mioma submucoso de 38 mm en mujer que desea fertilidad: miomectomía histeroscópica"
  },
  "INF-006": {
    titulo: "Úlcera de bordes elevados y duros con base limpia tras picadura de flebótomo en la selva: leishmaniasis cutánea, antimoniales",
    imagen: "flujogramas/leishmaniasis-cutanea-antimonial-pentavalente.svg",
    alt: "Flujograma: Úlcera de bordes elevados y duros con base limpia tras picadura de flebótomo en la selva: leishmaniasis cutánea, antimoniales"
  },
  "INF-007": {
    titulo: "Fiebre alta con escalofríos, ictericia, esplenomegalia y Hb 7 en un paciente de Iquitos: malaria",
    imagen: "flujogramas/malaria-diagnostico-gravedad-amazonia.svg",
    alt: "Flujograma: Fiebre alta con escalofríos, ictericia, esplenomegalia y Hb 7 en un paciente de Iquitos: malaria"
  },
  "NEF-005": {
    titulo: "Niño de 6 años con edema, proteinuria +++ y albúmina de 2 g/dL con función renal normal: síndrome nefrótico",
    imagen: "flujogramas/sindrome-nefrotico-pediatrico-cambios-minimos.svg",
    alt: "Flujograma: Niño de 6 años con edema, proteinuria +++ y albúmina de 2 g/dL con función renal normal: síndrome nefrótico"
  },
  "NEF-006": {
    titulo: "Aplastamiento con oliguria de 200 mL en 24 h, creatinina 2,4 y CPK alta: insuficiencia renal por rabdomiólisis",
    imagen: "flujogramas/rabdomiolisis-aplastamiento-lesion-renal.svg",
    alt: "Flujograma: Aplastamiento con oliguria de 200 mL en 24 h, creatinina 2,4 y CPK alta: insuficiencia renal por rabdomiólisis"
  },
  "NEF-007": {
    titulo: "Edema progresivo, orina espumosa, proteinuria de 3,9 g/día, albúmina 2,9 e hipertrigliceridemia: síndrome nefrótico",
    imagen: "flujogramas/sindrome-nefrotico-adulto-proteinuria.svg",
    alt: "Flujograma: Edema progresivo, orina espumosa, proteinuria de 3,9 g/día, albúmina 2,9 e hipertrigliceridemia: síndrome nefrótico"
  },
  "NEU-003": {
    titulo: "Asmático con exacerbaciones frecuentes usando solo salbutamol: agregar corticoide inhalado",
    imagen: "flujogramas/asma-escalonamiento-corticoide-inhalado.svg",
    alt: "Flujograma: Asmático con exacerbaciones frecuentes usando solo salbutamol: agregar corticoide inhalado"
  },
  "OFT-004": {
    titulo: "Epistaxis tras un golpe que sigue con vómitos de sangre pese al taponamiento anterior: taponamiento posterior por el especialista",
    imagen: "flujogramas/epistaxis-posterior-taponamiento.svg",
    alt: "Flujograma: Epistaxis tras un golpe que sigue con vómitos de sangre pese al taponamiento anterior: taponamiento posterior por el especialista"
  },
  "PED-018": {
    titulo: "Escolar con diarrea intermitente de un mes sin moco ni sangre, distensión y flatulencia: giardiasis",
    imagen: "flujogramas/giardiasis-diarrea-cronica-escolar.svg",
    alt: "Flujograma: Escolar con diarrea intermitente de un mes sin moco ni sangre, distensión y flatulencia: giardiasis"
  },
  "PED-019": {
    titulo: "La atresia intestinal (yeyunoileal) es más frecuente en recién nacidos prematuros",
    imagen: "flujogramas/atresia-intestinal-prematuros.svg",
    alt: "Flujograma: La atresia intestinal (yeyunoileal) es más frecuente en recién nacidos prematuros"
  },
  "PED-020": {
    titulo: "Prematuro de 36 horas, madre febril y RPM de 19 h, con irritabilidad, hipotermia y fontanela abombada: meningoencefalitis",
    imagen: "flujogramas/meningitis-neonatal-sepsis-temprana.svg",
    alt: "Flujograma: Prematuro de 36 horas, madre febril y RPM de 19 h, con irritabilidad, hipotermia y fontanela abombada: meningoencefalitis"
  },
  "PED-021": {
    titulo: "Neonato de 3 días con conjuntivitis purulenta intensa y madre con uretritis: Neisseria gonorrhoeae",
    imagen: "flujogramas/conjuntivitis-neonatal-gonococica.svg",
    alt: "Flujograma: Neonato de 3 días con conjuntivitis purulenta intensa y madre con uretritis: Neisseria gonorrhoeae"
  },
  "PSI-004": {
    titulo: "Adolescente deprimida que pierde la conciencia con bradipnea, y madre que toma ansiolíticos: flumazenilo",
    imagen: "flujogramas/intoxicacion-benzodiacepinas-flumazenilo.svg",
    alt: "Flujograma: Adolescente deprimida que pierde la conciencia con bradipnea, y madre que toma ansiolíticos: flumazenilo"
  },
  "PSI-005": {
    titulo: "Cortes autoinfligidos tras una ruptura «para que su enamorada regrese», con episodios previos parecidos: gesto suicida",
    imagen: "flujogramas/gesto-suicida-conducta-suicida.svg",
    alt: "Flujograma: Cortes autoinfligidos tras una ruptura «para que su enamorada regrese», con episodios previos parecidos: gesto suicida"
  },
  "SP-014": {
    titulo: "Aumento del VIH con poca terapia preventiva de TB en zona endémica: la coinfección TB-VIH aumentará",
    imagen: "flujogramas/coinfeccion-tb-vih-terapia-preventiva.svg",
    alt: "Flujograma: Aumento del VIH con poca terapia preventiva de TB en zona endémica: la coinfección TB-VIH aumentará"
  },
  "SP-015": {
    titulo: "Adolescente operada por embarazo ectópico cuyos padres preguntan el diagnóstico: informar con veracidad",
    imagen: "flujogramas/veracidad-informacion-adolescente-bioetica.svg",
    alt: "Flujograma: Adolescente operada por embarazo ectópico cuyos padres preguntan el diagnóstico: informar con veracidad"
  },
  "SP-016": {
    titulo: "Mujer conviviente con equimosis por golpes, dolor orofaríngeo, ansiedad y labilidad emocional: violencia familiar",
    imagen: "flujogramas/violencia-familiar-ley-30364.svg",
    alt: "Flujograma: Mujer conviviente con equimosis por golpes, dolor orofaríngeo, ansiedad y labilidad emocional: violencia familiar"
  },

  /* ---------- Casos de práctica (preguntas tipo) ---------- */

  "CAR-002": {
    titulo: "Mujer de 72 años hipertensa con fibrilación auricular sin estenosis mitral: anticoagulación oral",
    imagen: "flujogramas/fibrilacion-auricular-no-valvular-anticoagulacion.svg",
    alt: "Flujograma: Mujer de 72 años hipertensa con fibrilación auricular sin estenosis mitral: anticoagulación oral"
  },
  "CAR-003": {
    titulo: "Anciano con síncope de esfuerzo, disnea, pulso parvus et tardus y soplo eyectivo aórtico irradiado a carótidas: estenosis aórtica severa",
    imagen: "flujogramas/estenosis-aortica-severa-sincope.svg",
    alt: "Flujograma: Anciano con síncope de esfuerzo, disnea, pulso parvus et tardus y soplo eyectivo aórtico irradiado a carótidas: estenosis aórtica severa"
  },
  "CB-001": {
    titulo: "Lactante sin tamizaje con retraso del desarrollo, piel y pelo claros, eccema y olor a ratón: déficit de fenilalanina hidroxilasa",
    imagen: "flujogramas/fenilcetonuria-fenilalanina-hidroxilasa.svg",
    alt: "Flujograma: Lactante sin tamizaje con retraso del desarrollo, piel y pelo claros, eccema y olor a ratón: déficit de fenilalanina hidroxilasa"
  },
  "CIR-001": {
    titulo: "Dolor que migra de epigastrio a fosa ilíaca derecha, fiebre, rebote y leucocitosis con desviación: apendicectomía",
    imagen: "flujogramas/apendicitis-aguda-apendicectomia.svg",
    alt: "Flujograma: Dolor que migra de epigastrio a fosa ilíaca derecha, fiebre, rebote y leucocitosis con desviación: apendicectomía"
  },
  "END-001": {
    titulo: "Diabética tipo 1 con glucosa 520, pH 7,08, bicarbonato 8 y cetonas positivas: primero suero fisiológico",
    imagen: "flujogramas/cetoacidosis-diabetica-hidratacion.svg",
    alt: "Flujograma: Diabética tipo 1 con glucosa 520, pH 7,08, bicarbonato 8 y cetonas positivas: primero suero fisiológico"
  },
  "GAS-001": {
    titulo: "Cirrótico con hematemesis abundante e hipotensión, mientras se prepara la endoscopia: terlipresina u octreotide",
    imagen: "flujogramas/hemorragia-variceal-vasoactivos.svg",
    alt: "Flujograma: Cirrótico con hematemesis abundante e hipotensión, mientras se prepara la endoscopia: terlipresina u octreotide"
  },
  "GIN-001": {
    titulo: "Hemorragia posparto con útero blando por encima del ombligo y placenta completa: oxitocina endovenosa",
    imagen: "flujogramas/hemorragia-posparto-atonia-oxitocina.svg",
    alt: "Flujograma: Hemorragia posparto con útero blando por encima del ombligo y placenta completa: oxitocina endovenosa"
  },
  "HEM-001": {
    titulo: "Menstruaciones abundantes con Hb 8,9, VCM 70 y RDW alto: la ferritina baja confirma la ferropenia",
    imagen: "flujogramas/anemia-microcitica-ferritina.svg",
    alt: "Flujograma: Menstruaciones abundantes con Hb 8,9, VCM 70 y RDW alto: la ferritina baja confirma la ferropenia"
  },
  "INF-001": {
    titulo: "Agricultor de Loreto con fiebre y escalofríos, gota gruesa con P. vivax, sin gravedad y G6PD normal: cloroquina + primaquina",
    imagen: "flujogramas/malaria-vivax-cloroquina-primaquina.svg",
    alt: "Flujograma: Agricultor de Loreto con fiebre y escalofríos, gota gruesa con P. vivax, sin gravedad y G6PD normal: cloroquina + primaquina"
  },
  "NEF-001": {
    titulo: "ERC estadio 4 con enalapril y espironolactona, K⁺ 7,2 con T picudas y QRS ancho: gluconato de calcio EV",
    imagen: "flujogramas/hiperpotasemia-gluconato-de-calcio.svg",
    alt: "Flujograma: ERC estadio 4 con enalapril y espironolactona, K⁺ 7,2 con T picudas y QRS ancho: gluconato de calcio EV"
  },
  "NEU-001": {
    titulo: "Joven con fiebre vespertina y derrame: exudado linfocítico con ADA de 78 U/L: tuberculosis pleural",
    imagen: "flujogramas/derrame-pleural-enfoque-tuberculosis.svg",
    alt: "Flujograma: Joven con fiebre vespertina y derrame: exudado linfocítico con ADA de 78 U/L: tuberculosis pleural"
  },
  "NRL-001": {
    titulo: "Hemiparesia derecha y afasia súbitas hace 90 minutos: TC cerebral sin contraste primero",
    imagen: "flujogramas/acv-agudo-tomografia-sin-contraste.svg",
    alt: "Flujograma: Hemiparesia derecha y afasia súbitas hace 90 minutos: TC cerebral sin contraste primero"
  },
  "OFT-001": {
    titulo: "Hipermétrope con dolor ocular intenso al anochecer, halos, vómitos, córnea turbia y pupila media fija: glaucoma agudo de ángulo cerrado",
    imagen: "flujogramas/glaucoma-agudo-angulo-cerrado.svg",
    alt: "Flujograma: Hipermétrope con dolor ocular intenso al anochecer, halos, vómitos, córnea turbia y pupila media fija: glaucoma agudo de ángulo cerrado"
  },
  "PED-001": {
    titulo: "Ictericia hasta el abdomen a las 18 horas en hijo A de madre O: enfermedad hemolítica por incompatibilidad ABO",
    imagen: "flujogramas/ictericia-neonatal-incompatibilidad-abo.svg",
    alt: "Flujograma: Ictericia hasta el abdomen a las 18 horas en hijo A de madre O: enfermedad hemolítica por incompatibilidad ABO"
  },
  "PSI-001": {
    titulo: "Seis semanas de ánimo deprimido, anhedonia, insomnio, baja de peso, culpa y mala concentración: ISRS (sertralina)",
    imagen: "flujogramas/depresion-mayor-isrs.svg",
    alt: "Flujograma: Seis semanas de ánimo deprimido, anhedonia, insomnio, baja de peso, culpa y mala concentración: ISRS (sertralina)"
  },
  "REU-001": {
    titulo: "Podagra tras comida abundante con alcohol y cristales en aguja con birrefringencia negativa: urato monosódico",
    imagen: "flujogramas/gota-cristales-urato-monosodico.svg",
    alt: "Flujograma: Podagra tras comida abundante con alcohol y cristales en aguja con birrefringencia negativa: urato monosódico"
  },
  "SP-001": {
    titulo: "100 enfermos (80 positivos) y 200 sanos (180 negativos): especificidad de 90 %",
    imagen: "flujogramas/sensibilidad-especificidad-tabla-2x2.svg",
    alt: "Flujograma: 100 enfermos (80 positivos) y 200 sanos (180 negativos): especificidad de 90 %"
  },
  "TRA-001": {
    titulo: "Caída sobre la mano extendida con dolor en la tabaquera anatómica y Rx normal: férula con pulgar y reevaluar en 10-14 días",
    imagen: "flujogramas/fractura-escafoides-tabaquera-anatomica.svg",
    alt: "Flujograma: Caída sobre la mano extendida con dolor en la tabaquera anatómica y Rx normal: férula con pulgar y reevaluar en 10-14 días"
  },

  /* ---------- ENAM 2020 · bloque 2 (preguntas 174-259 del banco PDF) ---------- */

  "CIR-014": {
    titulo: "Dolor intenso al defecar que dura horas, sangre roja al limpiarse y esfínter hipertónico: fisura anal",
    imagen: "flujogramas/fisura-anal-esfinter-hipertonico.svg",
    alt: "Flujograma: Dolor intenso al defecar que dura horas, sangre roja al limpiarse y esfínter hipertónico: fisura anal"
  },
  "NEU-006": {
    titulo: "Tres semanas de tos, fiebre, baja de peso y crepitantes apicales: confirmar con baciloscopía (BK) en esputo",
    imagen: "flujogramas/tuberculosis-pulmonar-baciloscopia-diagnostico.svg",
    alt: "Flujograma: Tres semanas de tos, fiebre, baja de peso y crepitantes apicales: confirmar con baciloscopía (BK) en esputo"
  },
  "INF-011": {
    titulo: "Disuria y secreción uretral purulenta con diplococos gramnegativos intracelulares: gonorrea, ceftriaxona",
    imagen: "flujogramas/uretritis-gonococica-ceftriaxona.svg",
    alt: "Flujograma: Disuria y secreción uretral purulenta con diplococos gramnegativos intracelulares: gonorrea, ceftriaxona"
  },
  "REU-009": {
    titulo: "Lactante de 8 meses con placas eccematosas muy pruriginosas en forma de moneda en tórax y brazos: dermatitis atópica",
    imagen: "flujogramas/dermatitis-atopica-lactante-diferencial.svg",
    alt: "Flujograma: Lactante de 8 meses con placas eccematosas muy pruriginosas en forma de moneda en tórax y brazos: dermatitis atópica"
  },
  "GIN-029": {
    titulo: "Parto prolongado con agotamiento materno y latidos fetales con poca variabilidad: cesárea",
    imagen: "flujogramas/trabajo-parto-prolongado-cesarea.svg",
    alt: "Flujograma: Parto prolongado con agotamiento materno y latidos fetales con poca variabilidad: cesárea"
  },
  "CIR-015": {
    titulo: "Dolor de 7 días que migró a la fosa ilíaca derecha, automedicada, con masa dolorosa: plastrón apendicular",
    imagen: "flujogramas/plastron-apendicular-manejo-conservador.svg",
    alt: "Flujograma: Dolor de 7 días que migró a la fosa ilíaca derecha, automedicada, con masa dolorosa: plastrón apendicular"
  },
  "END-006": {
    titulo: "Astenia, estreñimiento, bradicardia, hipotermia, cara edematosa y piel seca con hipocaptación: hipotiroidismo, levotiroxina",
    imagen: "flujogramas/hipotiroidismo-mixedema-tsh-levotiroxina.svg",
    alt: "Flujograma: Astenia, estreñimiento, bradicardia, hipotermia, cara edematosa y piel seca con hipocaptación: hipotiroidismo, levotiroxina"
  },
  "CB-007": {
    titulo: "Niño de 1 año con vómitos, hepatomegalia e hipoglucemia sin cetonas y aciduria dicarboxílica: defecto de la β-oxidación (MCAD)",
    imagen: "flujogramas/deficit-mcad-beta-oxidacion.svg",
    alt: "Flujograma: Niño de 1 año con vómitos, hepatomegalia e hipoglucemia sin cetonas y aciduria dicarboxílica: defecto de la β-oxidación (MCAD)"
  },
  "NRL-008": {
    titulo: "Anciano con temblor de reposo en ambas manos, facies inexpresiva y lentitud para moverse: Parkinson, levodopa",
    imagen: "flujogramas/enfermedad-parkinson-levodopa.svg",
    alt: "Flujograma: Anciano con temblor de reposo en ambas manos, facies inexpresiva y lentitud para moverse: Parkinson, levodopa"
  },
  "PSI-007": {
    titulo: "Adolescente que perdió a su madre, con culpa, insomnio y aislamiento: el riesgo más frecuente es el suicidio",
    imagen: "flujogramas/duelo-adolescente-riesgo-suicida.svg",
    alt: "Flujograma: Adolescente que perdió a su madre, con culpa, insomnio y aislamiento: el riesgo más frecuente es el suicidio"
  },
  "PSI-008": {
    titulo: "Lavado de manos excesivo y desinfección constante por miedo a la contaminación, reconociendo que es exagerado: TOC",
    imagen: "flujogramas/trastorno-obsesivo-compulsivo-contaminacion.svg",
    alt: "Flujograma: Lavado de manos excesivo y desinfección constante por miedo a la contaminación, reconociendo que es exagerado: TOC"
  },
  "PSI-009": {
    titulo: "Mujer de 58 años con 4 meses de alucinaciones auditivas y cenestésicas y delirio de perjuicio: esquizofrenia paranoide",
    imagen: "flujogramas/esquizofrenia-paranoide-diferencial.svg",
    alt: "Flujograma: Mujer de 58 años con 4 meses de alucinaciones auditivas y cenestésicas y delirio de perjuicio: esquizofrenia paranoide"
  },
  "PSI-010": {
    titulo: "Adolescente con 3 meses de hiporexia, insomnio, irritabilidad, bajo rendimiento, aislamiento e ideas de muerte: episodio depresivo mayor",
    imagen: "flujogramas/episodio-depresivo-mayor-adolescente.svg",
    alt: "Flujograma: Adolescente con 3 meses de hiporexia, insomnio, irritabilidad, bajo rendimiento, aislamiento e ideas de muerte: episodio depresivo mayor"
  },
  "PSI-011": {
    titulo: "Mujer aislada que siente que va a morir, con falta de aire, palpitaciones, temblor y sudor, que se calma tras la atención: ataque de pánico",
    imagen: "flujogramas/ataque-de-panico-evolucion.svg",
    alt: "Flujograma: Mujer aislada que siente que va a morir, con falta de aire, palpitaciones, temblor y sudor, que se calma tras la atención: ataque de pánico"
  },
  "SP-020": {
    titulo: "Médico que se opone por religión a colocar un DIU que la paciente pide: derivarla a otro colega",
    imagen: "flujogramas/objecion-de-conciencia-derivacion.svg",
    alt: "Flujograma: Médico que se opone por religión a colocar un DIU que la paciente pide: derivarla a otro colega"
  },
  "PED-033": {
    titulo: "Preescolar del campo con sialorrea, vómitos, bradicardia, miosis, confusión y fasciculaciones: atropina",
    imagen: "flujogramas/organofosforados-atropina-pediatria.svg",
    alt: "Flujograma: Preescolar del campo con sialorrea, vómitos, bradicardia, miosis, confusión y fasciculaciones: atropina"
  },
  "NEF-010": {
    titulo: "Anemia de ERC con eritropoyetina, ferritina 56 y saturación de transferrina 12 %: dar hierro y mantener la EPO",
    imagen: "flujogramas/anemia-erc-hierro-eritropoyetina.svg",
    alt: "Flujograma: Anemia de ERC con eritropoyetina, ferritina 56 y saturación de transferrina 12 %: dar hierro y mantener la EPO"
  },
  "NEF-011": {
    titulo: "Obrero aplastado 36 horas con urea 200, creatinina 6, ácido úrico 10 y CPK alta: falla renal aguda por rabdomiólisis",
    imagen: "flujogramas/rabdomiolisis-aplastamiento-lra.svg",
    alt: "Flujograma: Obrero aplastado 36 horas con urea 200, creatinina 6, ácido úrico 10 y CPK alta: falla renal aguda por rabdomiólisis"
  },
  "CB-008": {
    titulo: "Alérgica a AINE que necesita un analgésico con poca acción antiinflamatoria: paracetamol (acetaminofén)",
    imagen: "flujogramas/paracetamol-farmacologia-cox.svg",
    alt: "Flujograma: Alérgica a AINE que necesita un analgésico con poca acción antiinflamatoria: paracetamol (acetaminofén)"
  },
  "NEF-012": {
    titulo: "Glomeruloesclerosis nodular con anasarca, PA 160/90 y proteinuria de 4 g/día: IECA (captopril)",
    imagen: "flujogramas/nefropatia-diabetica-ieca.svg",
    alt: "Flujograma: Glomeruloesclerosis nodular con anasarca, PA 160/90 y proteinuria de 4 g/día: IECA (captopril)"
  },
  "CIR-016": {
    titulo: "Politraumatizado en coma con PA 80/50 y FC 118: reponer volumen (solución salina) mientras se asegura la vía aérea",
    imagen: "flujogramas/politraumatizado-shock-xabcde.svg",
    alt: "Flujograma: Politraumatizado en coma con PA 80/50 y FC 118: reponer volumen (solución salina) mientras se asegura la vía aérea"
  },
  "GIN-030": {
    titulo: "39 semanas en podálica completa con 3 cm y feto de 3500 g: cesárea",
    imagen: "flujogramas/presentacion-podalica-cesarea.svg",
    alt: "Flujograma: 39 semanas en podálica completa con 3 cm y feto de 3500 g: cesárea"
  },
  "GIN-031": {
    titulo: "Puérpera de 3 días con fiebre, útero subinvolucionado y doloroso y loquios fétidos: endometritis puerperal",
    imagen: "flujogramas/endometritis-puerperal-fiebre-posparto.svg",
    alt: "Flujograma: Puérpera de 3 días con fiebre, útero subinvolucionado y doloroso y loquios fétidos: endometritis puerperal"
  },
  "CB-009": {
    titulo: "La implantación en el endometrio ocurre en la etapa de blastocisto (días 6-7)",
    imagen: "flujogramas/implantacion-blastocisto-embriologia.svg",
    alt: "Flujograma: La implantación en el endometrio ocurre en la etapa de blastocisto (días 6-7)"
  },
  "GIN-032": {
    titulo: "Fiebre de 39 °C en el parto con taquicardia fetal de 165: corioamnionitis",
    imagen: "flujogramas/corioamnionitis-fiebre-intraparto.svg",
    alt: "Flujograma: Fiebre de 39 °C en el parto con taquicardia fetal de 165: corioamnionitis"
  },
  "GIN-033": {
    titulo: "38 semanas con dolor epigástrico, sangrado rojo vinoso, PA 140/90 y útero contraído: desprendimiento prematuro de placenta",
    imagen: "flujogramas/desprendimiento-placenta-hemorragia-tercer-trimestre.svg",
    alt: "Flujograma: 38 semanas con dolor epigástrico, sangrado rojo vinoso, PA 140/90 y útero contraído: desprendimiento prematuro de placenta"
  },
  "GIN-034": {
    titulo: "35 semanas con sangrado vaginal escaso, indoloro y sin contracciones: hospitalizar y pedir ecografía",
    imagen: "flujogramas/placenta-previa-hospitalizacion-ecografia.svg",
    alt: "Flujograma: 35 semanas con sangrado vaginal escaso, indoloro y sin contracciones: hospitalizar y pedir ecografía"
  },
  "CIR-017": {
    titulo: "Quemadura extensa y profunda antes de llegar al hospital: cubrir con apósitos secos y limpios",
    imagen: "flujogramas/quemaduras-manejo-prehospitalario.svg",
    alt: "Flujograma: Quemadura extensa y profunda antes de llegar al hospital: cubrir con apósitos secos y limpios"
  },
  "CAR-012": {
    titulo: "Paciente con COVID-19 automedicado, palpitaciones, QT prolongado y potasio de 3: sobredosis de cloroquina",
    imagen: "flujogramas/qt-prolongado-cloroquina.svg",
    alt: "Flujograma: Paciente con COVID-19 automedicado, palpitaciones, QT prolongado y potasio de 3: sobredosis de cloroquina"
  },
  "CB-010": {
    titulo: "Disnea, prurito generalizado, sibilancias y SatO₂ 90 % tras una picadura: anafilaxia, adrenalina",
    imagen: "flujogramas/anafilaxia-picadura-adrenalina.svg",
    alt: "Flujograma: Disnea, prurito generalizado, sibilancias y SatO₂ 90 % tras una picadura: anafilaxia, adrenalina"
  },
  "NEF-013": {
    titulo: "Tras una fiesta con licor: visión borrosa, coma, respiración profunda y pH 6,8 con HCO₃ 7: intoxicación por metanol",
    imagen: "flujogramas/intoxicacion-metanol-licor-adulterado.svg",
    alt: "Flujograma: Tras una fiesta con licor: visión borrosa, coma, respiración profunda y pH 6,8 con HCO₃ 7: intoxicación por metanol"
  },
  "TRA-006": {
    titulo: "Conductor de un auto chocado por detrás: sospechar lesión cervical (latigazo)",
    imagen: "flujogramas/trauma-cervical-latigazo-impacto-posterior.svg",
    alt: "Flujograma: Conductor de un auto chocado por detrás: sospechar lesión cervical (latigazo)"
  },
  "GIN-035": {
    titulo: "Gestante de 12 semanas con IMC 30 y glucemia en ayunas de 90: prueba de tolerancia oral a la glucosa a las 24-28 semanas",
    imagen: "flujogramas/tamizaje-diabetes-gestacional-ptog.svg",
    alt: "Flujograma: Gestante de 12 semanas con IMC 30 y glucemia en ayunas de 90: prueba de tolerancia oral a la glucosa a las 24-28 semanas"
  },
  "INF-012": {
    titulo: "Puérpera en la segunda fase del tratamiento antituberculoso: continuar la lactancia sin restricción",
    imagen: "flujogramas/tuberculosis-lactancia-materna.svg",
    alt: "Flujograma: Puérpera en la segunda fase del tratamiento antituberculoso: continuar la lactancia sin restricción"
  },
  "PED-034": {
    titulo: "Prematuro de 34 semanas, ventilado 30 días, que a los 2 meses sigue con oxígeno 3 L/min: displasia broncopulmonar",
    imagen: "flujogramas/displasia-broncopulmonar-prematuro.svg",
    alt: "Flujograma: Prematuro de 34 semanas, ventilado 30 días, que a los 2 meses sigue con oxígeno 3 L/min: displasia broncopulmonar"
  },
  "GIN-036": {
    titulo: "Puérpera Rh negativa: la inmunoprofilaxis anti-D no sirve si ya tiene anticuerpos anti-D",
    imagen: "flujogramas/inmunoprofilaxis-anti-d-puerpera.svg",
    alt: "Flujograma: Puérpera Rh negativa: la inmunoprofilaxis anti-D no sirve si ya tiene anticuerpos anti-D"
  },
  "GAS-008": {
    titulo: "Alcohólico con ascitis, eritema palmar, temblor, desorientación y lentitud al hablar: encefalopatía hepática grado II",
    imagen: "flujogramas/encefalopatia-hepatica-west-haven.svg",
    alt: "Flujograma: Alcohólico con ascitis, eritema palmar, temblor, desorientación y lentitud al hablar: encefalopatía hepática grado II"
  },
  "CAR-013": {
    titulo: "Adulto que colapsa en un centro comercial sin riesgo para el reanimador: reconocer el paro, pedir ayuda y empezar 30 compresiones",
    imagen: "flujogramas/rcp-basica-adulto-compresiones.svg",
    alt: "Flujograma: Adulto que colapsa en un centro comercial sin riesgo para el reanimador: reconocer el paro, pedir ayuda y empezar 30 compresiones"
  },
  "GIN-037": {
    titulo: "Primigesta Rh negativa de 27 semanas en su primer control: pedir Coombs indirecto",
    imagen: "flujogramas/gestante-rh-negativo-coombs-indirecto.svg",
    alt: "Flujograma: Primigesta Rh negativa de 27 semanas en su primer control: pedir Coombs indirecto"
  },
  "GIN-038": {
    titulo: "34 semanas con altura uterina baja y circunferencia abdominal de 29 semanas: Doppler fetal",
    imagen: "flujogramas/restriccion-crecimiento-intrauterino-doppler.svg",
    alt: "Flujograma: 34 semanas con altura uterina baja y circunferencia abdominal de 29 semanas: Doppler fetal"
  },
  "SP-021": {
    titulo: "Trabajador asintomático con prueba positiva para COVID-19 y familiares enfermos: aislamiento y monitoreo",
    imagen: "flujogramas/trabajador-covid-asintomatico-aislamiento.svg",
    alt: "Flujograma: Trabajador asintomático con prueba positiva para COVID-19 y familiares enfermos: aislamiento y monitoreo"
  },
  "INF-013": {
    titulo: "Gestante con VIH en tratamiento y en trabajo de parto: el parto vaginal depende de que la carga viral sea < 1000 copias/mL",
    imagen: "flujogramas/vih-gestante-carga-viral-via-parto.svg",
    alt: "Flujograma: Gestante con VIH en tratamiento y en trabajo de parto: el parto vaginal depende de que la carga viral sea < 1000 copias/mL"
  },
  "GIN-039": {
    titulo: "Dolor en ambas fosas ilíacas 4 días después de una hidrosonografía con dolor a la movilización cervical y anexial: EPI",
    imagen: "flujogramas/enfermedad-inflamatoria-pelvica-instrumentacion.svg",
    alt: "Flujograma: Dolor en ambas fosas ilíacas 4 días después de una hidrosonografía con dolor a la movilización cervical y anexial: EPI"
  },
  "HEM-004": {
    titulo: "Anemia macrocítica con B12 baja, folato normal y gastritis atrófica fúndica: falta factor intrínseco (anemia perniciosa)",
    imagen: "flujogramas/anemia-perniciosa-factor-intrinseco.svg",
    alt: "Flujograma: Anemia macrocítica con B12 baja, folato normal y gastritis atrófica fúndica: falta factor intrínseco (anemia perniciosa)"
  },
  "GIN-040": {
    titulo: "15 semanas con sangrado, vómitos excesivos, útero de 19 cm y sin latidos fetales: mola hidatiforme",
    imagen: "flujogramas/mola-hidatiforme-diferencial.svg",
    alt: "Flujograma: 15 semanas con sangrado, vómitos excesivos, útero de 19 cm y sin latidos fetales: mola hidatiforme"
  },
  "GIN-041": {
    titulo: "15 semanas con dolor, sangrado, pérdida de líquido amniótico y orificios abiertos: aborto inevitable",
    imagen: "flujogramas/aborto-inevitable-clasificacion.svg",
    alt: "Flujograma: 15 semanas con dolor, sangrado, pérdida de líquido amniótico y orificios abiertos: aborto inevitable"
  },
  "PED-035": {
    titulo: "Niño de 2 años con dolor cólico, vómitos, deposiciones con moco y sangre y masa alargada: intususcepción",
    imagen: "flujogramas/intususcepcion-reduccion-enema.svg",
    alt: "Flujograma: Niño de 2 años con dolor cólico, vómitos, deposiciones con moco y sangre y masa alargada: intususcepción"
  },
  "CAR-014": {
    titulo: "Pierna derecha hinchada y dolorosa en una mujer obesa que toma anticonceptivos: ecografía dúplex para confirmar la TVP",
    imagen: "flujogramas/trombosis-venosa-profunda-eco-duplex.svg",
    alt: "Flujograma: Pierna derecha hinchada y dolorosa en una mujer obesa que toma anticonceptivos: ecografía dúplex para confirmar la TVP"
  },
  "NEF-014": {
    titulo: "Adolescente con escroto aumentado y transiluminación positiva: hidrocele",
    imagen: "flujogramas/hidrocele-transiluminacion-escroto.svg",
    alt: "Flujograma: Adolescente con escroto aumentado y transiluminación positiva: hidrocele"
  },
  "NEF-015": {
    titulo: "Infecciones urinarias a repetición por Proteus y cálculo coraliforme: estruvita",
    imagen: "flujogramas/litiasis-coraliforme-estruvita.svg",
    alt: "Flujograma: Infecciones urinarias a repetición por Proteus y cálculo coraliforme: estruvita"
  },

  /* ---------- Bloque 3 (preguntas 262-360 del banco PDF): tema general + ruta del caso ---------- */

  "CIR-018": {
    titulo: "Herida de 6 horas con tierra y piedras tras un accidente: ceftriaxona + metronidazol",
    imagen: "flujogramas/heridas-traumaticas-antibioticoterapia.svg",
    alt: "Flujograma: Herida de 6 horas con tierra y piedras tras un accidente: ceftriaxona + metronidazol"
  },
  "TRA-007": {
    titulo: "Fractura expuesta con herida de 12 cm, hueso expuesto y contaminación severa: lavado y desbridamiento",
    imagen: "flujogramas/fractura-expuesta-gustilo-anderson.svg",
    alt: "Flujograma: Fractura expuesta con herida de 12 cm, hueso expuesto y contaminación severa: lavado y desbridamiento"
  },
  "CIR-019": {
    titulo: "Herida punzante de 3 días con piel oscura, ampollas de líquido vinoso y crepitación: gangrena gaseosa",
    imagen: "flujogramas/infecciones-necrotizantes-gangrena-gaseosa.svg",
    alt: "Flujograma: Herida punzante de 3 días con piel oscura, ampollas de líquido vinoso y crepitación: gangrena gaseosa"
  },
  "OFT-006": {
    titulo: "Epistaxis justo después de retirar una sonda nasogástrica: taponamiento nasal anterior",
    imagen: "flujogramas/epistaxis-manejo-escalonado.svg",
    alt: "Flujograma: Epistaxis justo después de retirar una sonda nasogástrica: taponamiento nasal anterior"
  },
  "CB-011": {
    titulo: "Bloqueo del plexo braquial que debe durar al menos 2 horas: bupivacaína",
    imagen: "flujogramas/anestesicos-locales-clasificacion-duracion.svg",
    alt: "Flujograma: Bloqueo del plexo braquial que debe durar al menos 2 horas: bupivacaína"
  },
  "CIR-020": {
    titulo: "Atropellado con insuficiencia respiratoria, hipotensión, yugulares ingurgitadas e hipersonoridad: neumotórax a tensión",
    imagen: "flujogramas/trauma-toracico-neumotorax-tension.svg",
    alt: "Flujograma: Atropellado con insuficiencia respiratoria, hipotensión, yugulares ingurgitadas e hipersonoridad: neumotórax a tensión"
  },
  "NEF-016": {
    titulo: "Masa testicular indolora de 3 cm en un adulto joven operado de criptorquidia: cáncer testicular",
    imagen: "flujogramas/masa-escrotal-cancer-testicular.svg",
    alt: "Flujograma: Masa testicular indolora de 3 cm en un adulto joven operado de criptorquidia: cáncer testicular"
  },
  "CIR-021": {
    titulo: "Fiebre, dolor y testículo aumentado 5 días después de una hernioplastia inguinal: orquitis",
    imagen: "flujogramas/complicaciones-hernioplastia-inguinal.svg",
    alt: "Flujograma: Fiebre, dolor y testículo aumentado 5 días después de una hernioplastia inguinal: orquitis"
  },
  "NRL-009": {
    titulo: "Caída de un 2.º piso con ojos de mapache, rinorraquia y otorragia: fractura de base de cráneo",
    imagen: "flujogramas/tec-lesiones-fractura-base-craneo.svg",
    alt: "Flujograma: Caída de un 2.º piso con ojos de mapache, rinorraquia y otorragia: fractura de base de cráneo"
  },
  "INF-014": {
    titulo: "Fiebre de 3 semanas con cefalea, diarrea, hematoquecia y PA 70/40: fiebre tifoidea con choque por hemorragia",
    imagen: "flujogramas/fiebre-tifoidea-complicaciones.svg",
    alt: "Flujograma: Fiebre de 3 semanas con cefalea, diarrea, hematoquecia y PA 70/40: fiebre tifoidea con choque por hemorragia"
  },
  "CAR-015": {
    titulo: "Dolor torácico con ST alterado y enzimas altas tras perder a un ser querido, con recuperación total en 7 días: Takotsubo",
    imagen: "flujogramas/dolor-toracico-troponina-takotsubo.svg",
    alt: "Flujograma: Dolor torácico con ST alterado y enzimas altas tras perder a un ser querido, con recuperación total en 7 días: Takotsubo"
  },
  "CAR-016": {
    titulo: "Marfan con dolor torácico desgarrante, PA distinta entre brazos y mediastino ensanchado: disección aórtica, betabloqueador",
    imagen: "flujogramas/sindrome-aortico-agudo-diseccion.svg",
    alt: "Flujograma: Marfan con dolor torácico desgarrante, PA distinta entre brazos y mediastino ensanchado: disección aórtica, betabloqueador"
  },
  "NEU-007": {
    titulo: "Disnea que empeora, agotamiento, diaforesis, PaO₂ 50 y SatO₂ 78 %: ventilación mecánica",
    imagen: "flujogramas/insuficiencia-respiratoria-soporte-ventilatorio.svg",
    alt: "Flujograma: Disnea que empeora, agotamiento, diaforesis, PaO₂ 50 y SatO₂ 78 %: ventilación mecánica"
  },
  "CAR-017": {
    titulo: "Tos y baja de peso de 2 meses con dolor pleurítico, ruidos cardiacos apagados y cardiomegalia: pericarditis tuberculosa",
    imagen: "flujogramas/pericarditis-enfoque-etiologico-tuberculosa.svg",
    alt: "Flujograma: Tos y baja de peso de 2 meses con dolor pleurítico, ruidos cardiacos apagados y cardiomegalia: pericarditis tuberculosa"
  },
  "INF-015": {
    titulo: "Úlcera genital indolora de base firme con espiroquetas: chancro sifilítico, inflamación perivascular con plasmocitos",
    imagen: "flujogramas/ulcera-genital-sifilis-histopatologia.svg",
    alt: "Flujograma: Úlcera genital indolora de base firme con espiroquetas: chancro sifilítico, inflamación perivascular con plasmocitos"
  },
  "GAS-009": {
    titulo: "Colitis ulcerosa de 20 años desde el recto hasta el colon ascendente: el riesgo es el adenocarcinoma de colon",
    imagen: "flujogramas/colitis-ulcerosa-cancer-colorrectal.svg",
    alt: "Flujograma: Colitis ulcerosa de 20 años desde el recto hasta el colon ascendente: el riesgo es el adenocarcinoma de colon"
  },
  "GAS-010": {
    titulo: "Íleon terminal resecado con inflamación transmural y granulomas: enfermedad de Crohn, riesgo de fístulas",
    imagen: "flujogramas/enfermedad-crohn-fistulas.svg",
    alt: "Flujograma: Íleon terminal resecado con inflamación transmural y granulomas: enfermedad de Crohn, riesgo de fístulas"
  },
  "GAS-011": {
    titulo: "Heces voluminosas y malolientes con flatulencia y baja de peso de 1 año: malabsorción, grasa en heces",
    imagen: "flujogramas/diarrea-cronica-malabsorcion-esteatorrea.svg",
    alt: "Flujograma: Heces voluminosas y malolientes con flatulencia y baja de peso de 1 año: malabsorción, grasa en heces"
  },
  "CIR-022": {
    titulo: "Infarto reciente, dolor abdominal, diarrea con sangre, ruidos ausentes e hipotensión: infarto intestinal",
    imagen: "flujogramas/isquemia-mesenterica-aguda-etiologia.svg",
    alt: "Flujograma: Infarto reciente, dolor abdominal, diarrea con sangre, ruidos ausentes e hipotensión: infarto intestinal"
  },
  "CAR-018": {
    titulo: "Joven deportista con muerte súbita y padre muerto de forma súbita a temprana edad: miocardiopatía hipertrófica",
    imagen: "flujogramas/muerte-subita-joven-miocardiopatia-hipertrofica.svg",
    alt: "Flujograma: Joven deportista con muerte súbita y padre muerto de forma súbita a temprana edad: miocardiopatía hipertrófica"
  },
  "NEU-008": {
    titulo: "Derrame pleural con proteína 0,38, LDH 0,46 y LDH 125 UI: transudado, insuficiencia cardiaca",
    imagen: "flujogramas/derrame-pleural-trasudado-light.svg",
    alt: "Flujograma: Derrame pleural con proteína 0,38, LDH 0,46 y LDH 125 UI: transudado, insuficiencia cardiaca"
  },
  "INF-016": {
    titulo: "Fiebre, cefalea, dolor retroocular, artralgias y mialgias tras viajar a Piura: dengue, transmitido por Aedes aegypti",
    imagen: "flujogramas/metaxenicas-vectores-peru-dengue.svg",
    alt: "Flujograma: Fiebre, cefalea, dolor retroocular, artralgias y mialgias tras viajar a Piura: dengue, transmitido por Aedes aegypti"
  },
  "SP-022": {
    titulo: "Paciente en ventilación mecánica tras una hemorragia cerebral, con sepsis que no mejora y pronóstico muy malo: cuidados paliativos",
    imagen: "flujogramas/adecuacion-esfuerzo-terapeutico-paliativos.svg",
    alt: "Flujograma: Paciente en ventilación mecánica tras una hemorragia cerebral, con sepsis que no mejora y pronóstico muy malo: cuidados paliativos"
  },
  "SP-023": {
    titulo: "Muerte por caída de un árbol sin testigos: no dar el certificado, comunicar al Ministerio Público",
    imagen: "flujogramas/certificado-defuncion-muerte-violenta.svg",
    alt: "Flujograma: Muerte por caída de un árbol sin testigos: no dar el certificado, comunicar al Ministerio Público"
  },
  "END-007": {
    titulo: "Hipertiroidea con fiebre de 39 °C, taquiarritmia, desorientación e insuficiencia cardiaca: tormenta tiroidea",
    imagen: "flujogramas/tirotoxicosis-enfoque-tormenta-tiroidea.svg",
    alt: "Flujograma: Hipertiroidea con fiebre de 39 °C, taquiarritmia, desorientación e insuficiencia cardiaca: tormenta tiroidea"
  },
  "PED-036": {
    titulo: "Niño de 2 años con ITU febril recurrente, ecografía alterada y antecedente familiar de reflujo: cistouretrografía miccional",
    imagen: "flujogramas/itu-pediatrica-imagenes-reflujo.svg",
    alt: "Flujograma: Niño de 2 años con ITU febril recurrente, ecografía alterada y antecedente familiar de reflujo: cistouretrografía miccional"
  },
  "PED-037": {
    titulo: "Lactante de 6 meses con FR 60, tiraje subcostal, cianosis y crepitantes bilaterales: neumonía grave, ceftriaxona",
    imagen: "flujogramas/neumonia-menor-5-anos-clasificacion.svg",
    alt: "Flujograma: Lactante de 6 meses con FR 60, tiraje subcostal, cianosis y crepitantes bilaterales: neumonía grave, ceftriaxona"
  },
  "PED-038": {
    titulo: "Recién nacido en apnea con FC 90 que no mejora con secar, aspirar y estimular: ventilación a presión positiva",
    imagen: "flujogramas/reanimacion-neonatal-algoritmo.svg",
    alt: "Flujograma: Recién nacido en apnea con FC 90 que no mejora con secar, aspirar y estimular: ventilación a presión positiva"
  },
  "SP-024": {
    titulo: "Relacionar la calidad del agua con la diarrea usando solo datos por localidad: estudio ecológico",
    imagen: "flujogramas/disenos-estudio-epidemiologico-ecologico.svg",
    alt: "Flujograma: Relacionar la calidad del agua con la diarrea usando solo datos por localidad: estudio ecológico"
  },
  "OFT-007": {
    titulo: "Rinorrea y congestión con los cambios de temperatura, pruebas cutáneas negativas y sin IgE ni eosinofilia: rinitis vasomotora",
    imagen: "flujogramas/rinitis-clasificacion-vasomotora.svg",
    alt: "Flujograma: Rinorrea y congestión con los cambios de temperatura, pruebas cutáneas negativas y sin IgE ni eosinofilia: rinitis vasomotora"
  },
  "SP-025": {
    titulo: "Mascarilla y cubrirse al toser para no transmitir la tuberculosis: prevención primaria",
    imagen: "flujogramas/niveles-prevencion-tuberculosis.svg",
    alt: "Flujograma: Mascarilla y cubrirse al toser para no transmitir la tuberculosis: prevención primaria"
  },
  "SP-026": {
    titulo: "Peste neumónica en el norte del Perú: contacto cercano es quien estuvo a menos de 2 metros del enfermo",
    imagen: "flujogramas/peste-formas-clinicas-contactos.svg",
    alt: "Flujograma: Peste neumónica en el norte del Perú: contacto cercano es quien estuvo a menos de 2 metros del enfermo"
  },
  "PED-040": {
    titulo: "Recién nacido de 2 horas, madre sin control y RPM de 20 horas, con intolerancia oral y distensión: sepsis neonatal temprana",
    imagen: "flujogramas/sepsis-neonatal-temprana-tardia.svg",
    alt: "Flujograma: Recién nacido de 2 horas, madre sin control y RPM de 20 horas, con intolerancia oral y distensión: sepsis neonatal temprana"
  },
  "PED-041": {
    titulo: "Lactante de 10 meses que suda al lactar, con taquipnea, retracciones, hepatomegalia y soplo sistólico: insuficiencia cardiaca, furosemida",
    imagen: "flujogramas/insuficiencia-cardiaca-lactante-furosemida.svg",
    alt: "Flujograma: Lactante de 10 meses que suda al lactar, con taquipnea, retracciones, hepatomegalia y soplo sistólico: insuficiencia cardiaca, furosemida"
  },
  "SP-027": {
    titulo: "Instalaciones, equipos, personal y materiales de comunicación: dimensión de aspectos tangibles",
    imagen: "flujogramas/calidad-servqual-dimensiones.svg",
    alt: "Flujograma: Instalaciones, equipos, personal y materiales de comunicación: dimensión de aspectos tangibles"
  },
  "REU-010": {
    titulo: "Lactante con prurito nocturno y eccema exudativo en cuero cabelludo, cara y extensoras: dermatitis atópica",
    imagen: "flujogramas/dermatitis-atopica-lactante-diferencial-prurito.svg",
    alt: "Flujograma: Lactante con prurito nocturno y eccema exudativo en cuero cabelludo, cara y extensoras: dermatitis atópica"
  },
  "PED-042": {
    titulo: "Lactante con fiebre de 39 °C, polipnea, tiraje, crepitantes focales, neutrofilia e infiltrado en base derecha: neumonía típica",
    imagen: "flujogramas/neumonia-nino-tipica-atipica-viral.svg",
    alt: "Flujograma: Lactante con fiebre de 39 °C, polipnea, tiraje, crepitantes focales, neutrofilia e infiltrado en base derecha: neumonía típica"
  },
  "TRA-008": {
    titulo: "Adolescente con dolor nocturno en el fémur distal que no cede con analgésicos y Rx con destrucción esclerótica: osteosarcoma",
    imagen: "flujogramas/tumores-oseos-osteosarcoma.svg",
    alt: "Flujograma: Adolescente con dolor nocturno en el fémur distal que no cede con analgésicos y Rx con destrucción esclerótica: osteosarcoma"
  },
  "NRL-010": {
    titulo: "Niño con debilidad flácida de las piernas y nivel sensitivo torácico tras una virosis: mielitis transversa",
    imagen: "flujogramas/debilidad-aguda-mielitis-transversa.svg",
    alt: "Flujograma: Niño con debilidad flácida de las piernas y nivel sensitivo torácico tras una virosis: mielitis transversa"
  },
  "PED-043": {
    titulo: "Niño con hematuria, edema y PA elevada 7 días después de una faringoamigdalitis: glomerulonefritis postestreptocócica",
    imagen: "flujogramas/sindrome-nefritico-glomerulonefritis-postestreptococica.svg",
    alt: "Flujograma: Niño con hematuria, edema y PA elevada 7 días después de una faringoamigdalitis: glomerulonefritis postestreptocócica"
  },
  "INF-017": {
    titulo: "Secreción uretral purulenta y disuria 5 días después de una relación casual: ceftriaxona + azitromicina",
    imagen: "flujogramas/secrecion-uretral-manejo-sindromico.svg",
    alt: "Flujograma: Secreción uretral purulenta y disuria 5 días después de una relación casual: ceftriaxona + azitromicina"
  },
  "INF-018": {
    titulo: "Escolar con fiebre, cefalea, vómitos, rigidez de nuca, Brudzinski y petequias y equimosis: Neisseria meningitidis",
    imagen: "flujogramas/meningitis-bacteriana-edad-meningococo.svg",
    alt: "Flujograma: Escolar con fiebre, cefalea, vómitos, rigidez de nuca, Brudzinski y petequias y equimosis: Neisseria meningitidis"
  },
  "GAS-012": {
    titulo: "Niño de 3 años con fiebre, vómitos, coluria, acolia, ictericia y hepatomegalia: IgM anti-VHA confirma hepatitis A",
    imagen: "flujogramas/hepatitis-viral-aguda-serologia.svg",
    alt: "Flujograma: Niño de 3 años con fiebre, vómitos, coluria, acolia, ictericia y hepatomegalia: IgM anti-VHA confirma hepatitis A"
  },
  "NEF-017": {
    titulo: "Escolar con dolor testicular brusco, tumefacción y reflejo cremastérico ausente: torsión testicular",
    imagen: "flujogramas/escroto-agudo-torsion-testicular.svg",
    alt: "Flujograma: Escolar con dolor testicular brusco, tumefacción y reflejo cremastérico ausente: torsión testicular"
  },
  "PED-044": {
    titulo: "Recién nacido macrosómico con brazo en aducción, rotación interna y antebrazo en pronación: parálisis de Erb-Duchenne",
    imagen: "flujogramas/plexo-braquial-erb-duchenne.svg",
    alt: "Flujograma: Recién nacido macrosómico con brazo en aducción, rotación interna y antebrazo en pronación: parálisis de Erb-Duchenne"
  },
  "PED-045": {
    titulo: "Prematuro con asfixia que a la hora presenta mirada fija y masticación con protrusión de la lengua: convulsiones sutiles",
    imagen: "flujogramas/convulsiones-neonatales-tipos.svg",
    alt: "Flujograma: Prematuro con asfixia que a la hora presenta mirada fija y masticación con protrusión de la lengua: convulsiones sutiles"
  },
  "PED-046": {
    titulo: "Ictericia neonatal por aumento de producción con reticulocitos normales: policitemia",
    imagen: "flujogramas/ictericia-neonatal-indirecta-policitemia.svg",
    alt: "Flujograma: Ictericia neonatal por aumento de producción con reticulocitos normales: policitemia"
  },
  "NRL-011": {
    titulo: "TEC: la TC cerebral se pide si el Glasgow es menor de 14 (o hay otro criterio de riesgo)",
    imagen: "flujogramas/tec-indicaciones-tomografia.svg",
    alt: "Flujograma: TEC: la TC cerebral se pide si el Glasgow es menor de 14 (o hay otro criterio de riesgo)"
  },
  "HEM-005": {
    titulo: "Microcitosis con ferritina normal y HbA2 de 5,8 %: β-talasemia menor",
    imagen: "flujogramas/anemia-microcitica-enfoque-diagnostico.svg",
    alt: "Flujograma: Microcitosis con ferritina normal y HbA2 de 5,8 %: β-talasemia menor"
  },
  "PED-039": {
    titulo: "Niño de 2 años con edema palpebral matutino y orina espumosa sin infección previa: síndrome nefrótico",
    imagen: "flujogramas/edema-renal-nino-nefrotico-nefritico.svg",
    alt: "Flujograma: Niño de 2 años con edema palpebral matutino y orina espumosa sin infección previa: síndrome nefrótico"
  },
  /* ── Bloque 4: 100 flujogramas (diseños árbol, radial, fases, termómetro y tarjetas) ── */
  "TRA-009": {
    titulo: "Caída sobre la mano con deformidad del tercio medio del brazo y mano caída: fractura de la diáfisis humeral con lesión radial",
    imagen: "flujogramas/fractura-humero-lesion-nervio-radial.svg",
    alt: "Flujograma: Caída sobre la mano con deformidad del tercio medio del brazo y mano caída: fractura de la diáfisis humeral con lesión radial"
  },
  "CIR-023": {
    titulo: "Dolor, vómitos y estreñimiento con niveles hidroaéreos y sin gas en el recto tras una apendicectomía complicada: obstrucción intestinal",
    imagen: "flujogramas/obstruccion-intestinal-bridas.svg",
    alt: "Flujograma: Dolor, vómitos y estreñimiento con niveles hidroaéreos y sin gas en el recto tras una apendicectomía complicada: obstrucción intestinal"
  },
  "SP-028": {
    titulo: "Exigir al Estado un estándar mínimo de salud para quien lo necesite: principio de justicia",
    imagen: "flujogramas/principios-bioetica-justicia.svg",
    alt: "Flujograma: Exigir al Estado un estándar mínimo de salud para quien lo necesite: principio de justicia"
  },
  "SP-029": {
    titulo: "Impacto de la pandemia en la salud mental de los trabajadores de salud: estudio correlacional transversal",
    imagen: "flujogramas/disenos-investigacion-transversal.svg",
    alt: "Flujograma: Impacto de la pandemia en la salud mental de los trabajadores de salud: estudio correlacional transversal"
  },
  "CIR-024": {
    titulo: "Hernia inguinal esférica por encima del pliegue que sale con el esfuerzo y Landívar positivo: hernia inguinal directa",
    imagen: "flujogramas/hernias-ingle-directa.svg",
    alt: "Flujograma: Hernia inguinal esférica por encima del pliegue que sale con el esfuerzo y Landívar positivo: hernia inguinal directa"
  },
  "SP-030": {
    titulo: "Estar a menos de 1 metro por más de 15 minutos antes de los síntomas del enfermo: contacto directo",
    imagen: "flujogramas/covid-definicion-contacto-directo.svg",
    alt: "Flujograma: Estar a menos de 1 metro por más de 15 minutos antes de los síntomas del enfermo: contacto directo"
  },
  "CIR-025": {
    titulo: "Choque séptico de origen abdominal con foco abordable: controlar el foco lo más pronto posible",
    imagen: "flujogramas/shock-septico-control-foco.svg",
    alt: "Flujograma: Choque séptico de origen abdominal con foco abordable: controlar el foco lo más pronto posible"
  },
  "CAR-019": {
    titulo: "Adulto en paro con RCP básica iniciada: a la vez, oxígeno y conectar el monitor/desfibrilador",
    imagen: "flujogramas/paro-cardiorrespiratorio-rcp-monitor.svg",
    alt: "Flujograma: Adulto en paro con RCP básica iniciada: a la vez, oxígeno y conectar el monitor/desfibrilador"
  },
  "CB-012": {
    titulo: "Con ciprofloxacino, el café le estimula más: la cafeína es metabolizada por el citocromo P450 (CYP1A2)",
    imagen: "flujogramas/citocromo-p450-interacciones.svg",
    alt: "Flujograma: Con ciprofloxacino, el café le estimula más: la cafeína es metabolizada por el citocromo P450 (CYP1A2)"
  },
  "GIN-042": {
    titulo: "Gestante de 31 semanas con dolor desde un choque, útero hipertónico y sangrado oscuro escaso: desprendimiento prematuro de placenta",
    imagen: "flujogramas/hemorragia-tercer-trimestre-dpp.svg",
    alt: "Flujograma: Gestante de 31 semanas con dolor desde un choque, útero hipertónico y sangrado oscuro escaso: desprendimiento prematuro de placenta"
  },
  "GIN-043": {
    titulo: "Gestante de 14 semanas con fiebre, dolor en fosa ilíaca derecha y leucocitosis con desviación: apendicitis",
    imagen: "flujogramas/dolor-abdominal-gestante-apendicitis.svg",
    alt: "Flujograma: Gestante de 14 semanas con fiebre, dolor en fosa ilíaca derecha y leucocitosis con desviación: apendicitis"
  },
  "GIN-044": {
    titulo: "Parto podálico: se empieza a maniobrar cuando aparece el borde inferior de los omoplatos",
    imagen: "flujogramas/parto-podalico-maniobras.svg",
    alt: "Flujograma: Parto podálico: se empieza a maniobrar cuando aparece el borde inferior de los omoplatos"
  },
  "CB-013": {
    titulo: "El componente principal del surfactante pulmonar es la lecitina (dipalmitoilfosfatidilcolina)",
    imagen: "flujogramas/surfactante-pulmonar-lecitina.svg",
    alt: "Flujograma: El componente principal del surfactante pulmonar es la lecitina (dipalmitoilfosfatidilcolina)"
  },
  "GIN-045": {
    titulo: "Tres episodios de candidiasis vulvovaginal en tres meses: fluconazol de mantenimiento por seis meses",
    imagen: "flujogramas/candidiasis-vulvovaginal-recurrente.svg",
    alt: "Flujograma: Tres episodios de candidiasis vulvovaginal en tres meses: fluconazol de mantenimiento por seis meses"
  },
  "REU-011": {
    titulo: "Dolor muscular generalizado de 9 meses que no mejora con AINE, insomnio y VSG normal: fibromialgia",
    imagen: "flujogramas/fibromialgia-diagnostico-diferencial.svg",
    alt: "Flujograma: Dolor muscular generalizado de 9 meses que no mejora con AINE, insomnio y VSG normal: fibromialgia"
  },
  "NRL-012": {
    titulo: "Alcohólico con confusión, nistagmo, oftalmoplejía y ataxia: encefalopatía de Wernicke, tiamina",
    imagen: "flujogramas/deficit-tiamina-wernicke-korsakoff.svg",
    alt: "Flujograma: Alcohólico con confusión, nistagmo, oftalmoplejía y ataxia: encefalopatía de Wernicke, tiamina"
  },
  "INF-019": {
    titulo: "Paciente con VIH sin TAR, cefalea de 16 días, fiebre, rigidez de nuca y tinta china positiva: meningitis criptocócica, anfotericina B",
    imagen: "flujogramas/vih-infecciones-snc-criptococo.svg",
    alt: "Flujograma: Paciente con VIH sin TAR, cefalea de 16 días, fiebre, rigidez de nuca y tinta china positiva: meningitis criptocócica, anfotericina B"
  },
  "CIR-026": {
    titulo: "Niño mordido por su hermano, con marcas de dientes y sin sangrado: lavar con agua y jabón",
    imagen: "flujogramas/mordeduras-humana-animal-manejo.svg",
    alt: "Flujograma: Niño mordido por su hermano, con marcas de dientes y sin sangrado: lavar con agua y jabón"
  },
  "SP-031": {
    titulo: "Niño con cáncer terminal reanimado una y otra vez, intubado y con quimioterapia reiniciada estando en coma: obstinación terapéutica",
    imagen: "flujogramas/final-vida-obstinacion-terapeutica.svg",
    alt: "Flujograma: Niño con cáncer terminal reanimado una y otra vez, intubado y con quimioterapia reiniciada estando en coma: obstinación terapéutica"
  },
  "SP-032": {
    titulo: "Mujer con equimosis por objetos externos y ansiedad en la que se sospecha violencia familiar: denunciar ante las autoridades",
    imagen: "flujogramas/violencia-mujer-denuncia-ley-30364.svg",
    alt: "Flujograma: Mujer con equimosis por objetos externos y ansiedad en la que se sospecha violencia familiar: denunciar ante las autoridades"
  },
  "REU-012": {
    titulo: "Habones pruriginosos en todo el cuerpo desde hace 2 días: urticaria aguda, antihistamínico",
    imagen: "flujogramas/urticaria-antihistaminico-escalera.svg",
    alt: "Flujograma: Habones pruriginosos en todo el cuerpo desde hace 2 días: urticaria aguda, antihistamínico"
  },
  "NEF-018": {
    titulo: "Artritis reumatoide de 27 años con síndrome nefrótico y biopsia con rojo Congo positivo: amiloidosis secundaria (AA)",
    imagen: "flujogramas/sindrome-nefrotico-amiloidosis-aa.svg",
    alt: "Flujograma: Artritis reumatoide de 27 años con síndrome nefrótico y biopsia con rojo Congo positivo: amiloidosis secundaria (AA)"
  },
  "NEF-019": {
    titulo: "Insuficiencia renal crónica con dolor pleurítico, ruidos apagados y frote pericárdico: pericarditis urémica, hemodiálisis",
    imagen: "flujogramas/dialisis-urgente-pericarditis-uremica.svg",
    alt: "Flujograma: Insuficiencia renal crónica con dolor pleurítico, ruidos apagados y frote pericárdico: pericarditis urémica, hemodiálisis"
  },
  "NEF-020": {
    titulo: "Falla renal con eosinófilos en orina y complemento normal días después de iniciar ceftazidima: nefritis intersticial aguda",
    imagen: "flujogramas/lesion-renal-intrinseca-nefritis-intersticial.svg",
    alt: "Flujograma: Falla renal con eosinófilos en orina y complemento normal días después de iniciar ceftazidima: nefritis intersticial aguda"
  },
  "REU-013": {
    titulo: "Lactante con pápulas pruriginosas en axilas, cara, cuero cabelludo, palmas y plantas, y madre con lesiones iguales: escabiosis, permetrina",
    imagen: "flujogramas/escabiosis-lactante-permetrina.svg",
    alt: "Flujograma: Lactante con pápulas pruriginosas en axilas, cara, cuero cabelludo, palmas y plantas, y madre con lesiones iguales: escabiosis, permetrina"
  },
  "CIR-027": {
    titulo: "Quemado en un ambiente cerrado con humo, ronquera, esputo gris y quemaduras faciales: oxígeno por mascarilla de inmediato",
    imagen: "flujogramas/quemadura-lesion-inhalatoria-oxigeno.svg",
    alt: "Flujograma: Quemado en un ambiente cerrado con humo, ronquera, esputo gris y quemaduras faciales: oxígeno por mascarilla de inmediato"
  },
  "PED-047": {
    titulo: "Recién nacido de 15 días con vómitos explosivos no biliosos, masa palpable y píloro engrosado en la ecografía: estenosis hipertrófica del píloro",
    imagen: "flujogramas/vomitos-neonato-estenosis-piloro.svg",
    alt: "Flujograma: Recién nacido de 15 días con vómitos explosivos no biliosos, masa palpable y píloro engrosado en la ecografía: estenosis hipertrófica del píloro"
  },
  "PED-048": {
    titulo: "Niña de 4 años con dificultad respiratoria aguda y sibilancias bilaterales tras un resfriado: crisis de asma",
    imagen: "flujogramas/sibilancias-nino-asma.svg",
    alt: "Flujograma: Niña de 4 años con dificultad respiratoria aguda y sibilancias bilaterales tras un resfriado: crisis de asma"
  },
  "PED-049": {
    titulo: "Niña de 4 años hospitalizada con fiebre, tos, crepitantes bilaterales y leucocitosis con desviación: ceftriaxona",
    imagen: "flujogramas/neumonia-nino-hospitalizado-ceftriaxona.svg",
    alt: "Flujograma: Niña de 4 años hospitalizada con fiebre, tos, crepitantes bilaterales y leucocitosis con desviación: ceftriaxona"
  },
  "CB-014": {
    titulo: "LDL muy alto y obstrucción coronaria: la aterosclerosis compromete la capa íntima",
    imagen: "flujogramas/aterosclerosis-capa-intima.svg",
    alt: "Flujograma: LDL muy alto y obstrucción coronaria: la aterosclerosis compromete la capa íntima"
  },
  "CIR-028": {
    titulo: "Claudicación limitante pese al tratamiento médico con oclusión larga de la femoral superficial: bypass femoropoplíteo con safena",
    imagen: "flujogramas/enfermedad-arterial-periferica-bypass.svg",
    alt: "Flujograma: Claudicación limitante pese al tratamiento médico con oclusión larga de la femoral superficial: bypass femoropoplíteo con safena"
  },
  "PED-050": {
    titulo: "Recién nacido con sospecha de hernia diafragmática: la radiografía de tórax confirma",
    imagen: "flujogramas/hernia-diafragmatica-congenita-rx.svg",
    alt: "Flujograma: Recién nacido con sospecha de hernia diafragmática: la radiografía de tórax confirma"
  },
  "SP-033": {
    titulo: "Complicación de una hernioplastia que no le advirtieron a la paciente: se vulneró el derecho a ser informado",
    imagen: "flujogramas/derechos-usuario-salud-informacion.svg",
    alt: "Flujograma: Complicación de una hernioplastia que no le advirtieron a la paciente: se vulneró el derecho a ser informado"
  },
  "HEM-006": {
    titulo: "Edema pulmonar bilateral durante la transfusión de plasma en una paciente séptica: TRALI por anticuerpos contra granulocitos",
    imagen: "flujogramas/reacciones-transfusionales-trali.svg",
    alt: "Flujograma: Edema pulmonar bilateral durante la transfusión de plasma en una paciente séptica: TRALI por anticuerpos contra granulocitos"
  },
  "CAR-020": {
    titulo: "Hipotensión, yugulares ingurgitadas, ruidos apagados, pulso paradójico y alternancia eléctrica: taponamiento cardiaco, pericardiocentesis",
    imagen: "flujogramas/shock-obstructivo-taponamiento-cardiaco.svg",
    alt: "Flujograma: Hipotensión, yugulares ingurgitadas, ruidos apagados, pulso paradójico y alternancia eléctrica: taponamiento cardiaco, pericardiocentesis"
  },
  "HEM-007": {
    titulo: "Varón de 54 años con cansancio, Hb 10,7 y VCM 73: pedir ferritina para precisar la anemia",
    imagen: "flujogramas/anemia-microcitica-estudio-ferritina.svg",
    alt: "Flujograma: Varón de 54 años con cansancio, Hb 10,7 y VCM 73: pedir ferritina para precisar la anemia"
  },
  "CAR-021": {
    titulo: "Disnea, hemoptisis, soplo diastólico en el ápex, fibrilación auricular y crepitantes: estenosis mitral",
    imagen: "flujogramas/valvulopatias-estenosis-mitral.svg",
    alt: "Flujograma: Disnea, hemoptisis, soplo diastólico en el ápex, fibrilación auricular y crepitantes: estenosis mitral"
  },
  "CAR-022": {
    titulo: "Palpitaciones bruscas con ritmo irregular, FC 120 y pulso deficitario en una joven sin cardiopatía: fibrilación auricular",
    imagen: "flujogramas/taquicardias-fibrilacion-auricular.svg",
    alt: "Flujograma: Palpitaciones bruscas con ritmo irregular, FC 120 y pulso deficitario en una joven sin cardiopatía: fibrilación auricular"
  },
  "GAS-013": {
    titulo: "Lumbalgia con sacroilitis, sangre oculta y colon con mucosa granular, úlceras difusas y seudopólipos: colitis ulcerosa",
    imagen: "flujogramas/colitis-ulcerosa-espondiloartritis.svg",
    alt: "Flujograma: Lumbalgia con sacroilitis, sangre oculta y colon con mucosa granular, úlceras difusas y seudopólipos: colitis ulcerosa"
  },
  "GAS-014": {
    titulo: "Tumor ulcerado del píloro con obstrucción de la salida gástrica y H. pylori positivo: adenocarcinoma gástrico",
    imagen: "flujogramas/tumores-gastricos-adenocarcinoma.svg",
    alt: "Flujograma: Tumor ulcerado del píloro con obstrucción de la salida gástrica y H. pylori positivo: adenocarcinoma gástrico"
  },
  "NEU-009": {
    titulo: "Fiebre, sudoración nocturna, baja de peso y hemoptisis con cavitación en el lóbulo superior: Mycobacterium tuberculosis",
    imagen: "flujogramas/neumonia-cavitada-tuberculosis.svg",
    alt: "Flujograma: Fiebre, sudoración nocturna, baja de peso y hemoptisis con cavitación en el lóbulo superior: Mycobacterium tuberculosis"
  },
  "NEU-010": {
    titulo: "Disnea progresiva y tos seca de 14 meses, panal de abeja y autoanticuerpos negativos: fibrosis pulmonar idiopática",
    imagen: "flujogramas/epid-fibrosis-pulmonar-idiopatica.svg",
    alt: "Flujograma: Disnea progresiva y tos seca de 14 meses, panal de abeja y autoanticuerpos negativos: fibrosis pulmonar idiopática"
  },
  "CAR-023": {
    titulo: "Alcohol por 20 años e insuficiencia cardiaca descompensada: miocardiopatía dilatada",
    imagen: "flujogramas/miocardiopatias-dilatada-alcoholica.svg",
    alt: "Flujograma: Alcohol por 20 años e insuficiencia cardiaca descompensada: miocardiopatía dilatada"
  },
  "PED-051": {
    titulo: "Niño desnutrido con fractura, relato que no explica la lesión y cicatrices antiguas: sospechar maltrato infantil",
    imagen: "flujogramas/maltrato-infantil-fracturas.svg",
    alt: "Flujograma: Niño desnutrido con fractura, relato que no explica la lesión y cicatrices antiguas: sospechar maltrato infantil"
  },
  "INF-020": {
    titulo: "LCR con glucosa 40, proteínas 300 y 5000 leucocitos con 60 % de polimorfonucleares: meningitis bacteriana",
    imagen: "flujogramas/lcr-meningitis-bacteriana.svg",
    alt: "Flujograma: LCR con glucosa 40, proteínas 300 y 5000 leucocitos con 60 % de polimorfonucleares: meningitis bacteriana"
  },
  "PED-052": {
    titulo: "Recién nacido con salivación excesiva, dificultad respiratoria y sonda orogástrica que no pasa: radiografía de tórax para confirmar atresia esofágica",
    imagen: "flujogramas/atresia-esofagica-rx-torax.svg",
    alt: "Flujograma: Recién nacido con salivación excesiva, dificultad respiratoria y sonda orogástrica que no pasa: radiografía de tórax para confirmar atresia esofágica"
  },
  "INF-021": {
    titulo: "Diarrea aguda por Giardia: en las heces diarreicas se encuentran trofozoítos",
    imagen: "flujogramas/giardiasis-ciclo-trofozoitos.svg",
    alt: "Flujograma: Diarrea aguda por Giardia: en las heces diarreicas se encuentran trofozoítos"
  },
  "PED-053": {
    titulo: "Niño con diarrea, pliegue muy lento, llenado capilar lento, ojos hundidos y mucosas muy secas: plan C con solución isotónica",
    imagen: "flujogramas/deshidratacion-plan-c-rehidratacion.svg",
    alt: "Flujograma: Niño con diarrea, pliegue muy lento, llenado capilar lento, ojos hundidos y mucosas muy secas: plan C con solución isotónica"
  },
  "GIN-046": {
    titulo: "Gestante con ERC e hiperémesis grave que rechaza el aborto terapéutico: tratar la hiperémesis y la enfermedad de fondo",
    imagen: "flujogramas/hiperemesis-gravidica-autonomia.svg",
    alt: "Flujograma: Gestante con ERC e hiperémesis grave que rechaza el aborto terapéutico: tratar la hiperémesis y la enfermedad de fondo"
  },
  "PED-054": {
    titulo: "Neonato de 10 días con fiebre, mala succión, somnolencia y fontanela abombada: estudio del LCR",
    imagen: "flujogramas/neonato-febril-meningitis-lcr.svg",
    alt: "Flujograma: Neonato de 10 días con fiebre, mala succión, somnolencia y fontanela abombada: estudio del LCR"
  },
  "INF-022": {
    titulo: "Dengue con dolor abdominal intenso, vómitos persistentes, sangrado de mucosas, letargia, hepatomegalia y hematocrito de 50 %: dengue con signos de alarma",
    imagen: "flujogramas/dengue-fases-clasificacion.svg",
    alt: "Flujograma: Dengue con dolor abdominal intenso, vómitos persistentes, sangrado de mucosas, letargia, hepatomegalia y hematocrito de 50 %: dengue con signos de alarma"
  },
  "SP-034": {
    titulo: "«Asistencia sanitaria esencial, accesible a todos y núcleo del sistema de salud»: atención primaria de salud",
    imagen: "flujogramas/atencion-primaria-salud-alma-ata.svg",
    alt: "Flujograma: «Asistencia sanitaria esencial, accesible a todos y núcleo del sistema de salud»: atención primaria de salud"
  },
  "SP-035": {
    titulo: "Autocuidado y promoción en el primer nivel durante la pandemia: incorporar el cuidado de la salud mental",
    imagen: "flujogramas/primer-nivel-pandemia-salud-mental.svg",
    alt: "Flujograma: Autocuidado y promoción en el primer nivel durante la pandemia: incorporar el cuidado de la salud mental"
  },
  "OFT-008": {
    titulo: "Preescolar con otalgia aguda, tímpano abombado y otorrea purulenta: otitis media aguda, amoxicilina",
    imagen: "flujogramas/otitis-media-aguda-edad-gravedad.svg",
    alt: "Flujograma: Preescolar con otalgia aguda, tímpano abombado y otorrea purulenta: otitis media aguda, amoxicilina"
  },
  "PED-055": {
    titulo: "Lactante cuya madre tuvo fiebre con exantema a las 10 semanas de gestación: rubéola congénita, buscar catarata",
    imagen: "flujogramas/rubeola-congenita-catarata.svg",
    alt: "Flujograma: Lactante cuya madre tuvo fiebre con exantema a las 10 semanas de gestación: rubéola congénita, buscar catarata"
  },
  "SP-036": {
    titulo: "El registro y la categorización de los establecimientos de salud pertenecen al componente de organización del MAIS-BFC",
    imagen: "flujogramas/mais-bfc-componente-organizacion.svg",
    alt: "Flujograma: El registro y la categorización de los establecimientos de salud pertenecen al componente de organización del MAIS-BFC"
  },
  "END-008": {
    titulo: "Obeso con poliuria, nicturia, polidipsia y padres diabéticos: glucemia en ayunas en el primer nivel",
    imagen: "flujogramas/diabetes-diagnostico-glucemia-ayunas.svg",
    alt: "Flujograma: Obeso con poliuria, nicturia, polidipsia y padres diabéticos: glucemia en ayunas en el primer nivel"
  },
  "NEF-021": {
    titulo: "Hiperplasia benigna de próstata sintomática: alfabloqueadores e inhibidores de la 5-alfa reductasa",
    imagen: "flujogramas/hiperplasia-prostatica-alfabloqueador.svg",
    alt: "Flujograma: Hiperplasia benigna de próstata sintomática: alfabloqueadores e inhibidores de la 5-alfa reductasa"
  },
  "END-009": {
    titulo: "Choque refractario a líquidos con hiponatremia e hipoglucemia tras suspender 20 días de corticoides: hidrocortisona",
    imagen: "flujogramas/crisis-suprarrenal-retiro-corticoides.svg",
    alt: "Flujograma: Choque refractario a líquidos con hiponatremia e hipoglucemia tras suspender 20 días de corticoides: hidrocortisona"
  },
  "SP-037": {
    titulo: "Adulto mayor de 85 años con deterioro cognitivo leve, dependencia parcial, caídas y depresión: adulto mayor frágil",
    imagen: "flujogramas/adulto-mayor-fragil-clasificacion.svg",
    alt: "Flujograma: Adulto mayor de 85 años con deterioro cognitivo leve, dependencia parcial, caídas y depresión: adulto mayor frágil"
  },
  "GAS-015": {
    titulo: "Dolor epigástrico, náuseas y llenura de 3 meses con laboratorio y endoscopia normales: dispepsia funcional",
    imagen: "flujogramas/dispepsia-funcional-roma-iv.svg",
    alt: "Flujograma: Dolor epigástrico, náuseas y llenura de 3 meses con laboratorio y endoscopia normales: dispepsia funcional"
  },
  "GAS-016": {
    titulo: "Cirrótico estable con hematemesis y várices esofágicas sangrantes en la endoscopia: ligadura",
    imagen: "flujogramas/hemorragia-variceal-ligadura.svg",
    alt: "Flujograma: Cirrótico estable con hematemesis y várices esofágicas sangrantes en la endoscopia: ligadura"
  },
  "SP-038": {
    titulo: "Si las alternativas tienen el mismo efecto, solo se comparan costos: análisis de minimización de costos",
    imagen: "flujogramas/evaluacion-economica-minimizacion-costos.svg",
    alt: "Flujograma: Si las alternativas tienen el mismo efecto, solo se comparan costos: análisis de minimización de costos"
  },
  "NEU-011": {
    titulo: "Minero con tos crónica, disnea, nódulos apicales y adenopatías hiliares con calcificación en «cáscara de huevo»: silicosis",
    imagen: "flujogramas/neumoconiosis-silicosis.svg",
    alt: "Flujograma: Minero con tos crónica, disnea, nódulos apicales y adenopatías hiliares con calcificación en «cáscara de huevo»: silicosis"
  },
  "OFT-009": {
    titulo: "Escolar con estornudos, rinorrea, prurito nasal, ojeras, respiración bucal, pliegue nasal transverso e IgE alta: rinitis alérgica",
    imagen: "flujogramas/rinitis-alergica-diagnostico.svg",
    alt: "Flujograma: Escolar con estornudos, rinorrea, prurito nasal, ojeras, respiración bucal, pliegue nasal transverso e IgE alta: rinitis alérgica"
  },
  "CIR-029": {
    titulo: "Dolor en hipocondrio derecho tras comida grasa, leucocitosis, pared vesicular de 5 mm y cálculo fijo en el bacinete: colecistitis aguda",
    imagen: "flujogramas/colecistitis-aguda-tokyo.svg",
    alt: "Flujograma: Dolor en hipocondrio derecho tras comida grasa, leucocitosis, pared vesicular de 5 mm y cálculo fijo en el bacinete: colecistitis aguda"
  },
  "NEF-022": {
    titulo: "QRS ancho con ondas T altas, delgadas y puntiagudas: hiperpotasemia",
    imagen: "flujogramas/hiperpotasemia-cambios-electrocardiograma.svg",
    alt: "Flujograma: QRS ancho con ondas T altas, delgadas y puntiagudas: hiperpotasemia"
  },
  "INF-023": {
    titulo: "Diarrea con moco y poca sangre, fiebre de 38,5 °C, vómitos y comida en la calle: Shigella",
    imagen: "flujogramas/diarrea-disenterica-shigella.svg",
    alt: "Flujograma: Diarrea con moco y poca sangre, fiebre de 38,5 °C, vómitos y comida en la calle: Shigella"
  },
  "GAS-017": {
    titulo: "Niña con fiebre, vómitos, dolor en hipocondrio derecho y hepatomegalia sin ictericia: transaminasas para ver inflamación del hígado",
    imagen: "flujogramas/pruebas-hepaticas-transaminasas-nino.svg",
    alt: "Flujograma: Niña con fiebre, vómitos, dolor en hipocondrio derecho y hepatomegalia sin ictericia: transaminasas para ver inflamación del hígado"
  },
  "GAS-018": {
    titulo: "Dolor epigástrico terebrante irradiado a la espalda tras beber licor, con vómitos y signo de Cullen: pancreatitis aguda",
    imagen: "flujogramas/dolor-epigastrico-pancreatitis-aguda.svg",
    alt: "Flujograma: Dolor epigástrico terebrante irradiado a la espalda tras beber licor, con vómitos y signo de Cullen: pancreatitis aguda"
  },
  "CIR-030": {
    titulo: "Politraumatizado con PA 70/40, FC 156, palidez, yugulares colapsadas y tórax normal: hemorragia intraabdominal",
    imagen: "flujogramas/shock-trauma-hemorragia-intraabdominal.svg",
    alt: "Flujograma: Politraumatizado con PA 70/40, FC 156, palidez, yugulares colapsadas y tórax normal: hemorragia intraabdominal"
  },
  "INF-024": {
    titulo: "Gestante de Tumbes con fiebre cíclica, escalofríos y sudoración profusa: paludismo (malaria)",
    imagen: "flujogramas/sindrome-febril-malaria-gestante.svg",
    alt: "Flujograma: Gestante de Tumbes con fiebre cíclica, escalofríos y sudoración profusa: paludismo (malaria)"
  },
  "GIN-047": {
    titulo: "Quiste ovárico simple de 8 cm en una gestante de 8 semanas: operar entre las 12 y 20 semanas si persiste",
    imagen: "flujogramas/masa-ovarica-embarazo-cirugia.svg",
    alt: "Flujograma: Quiste ovárico simple de 8 cm en una gestante de 8 semanas: operar entre las 12 y 20 semanas si persiste"
  },
  "PSI-012": {
    titulo: "Joven deprimido y aislado tras un fracaso que antes estaba hiperactivo, verborreico y muy autosuficiente: trastorno bipolar",
    imagen: "flujogramas/trastorno-bipolar-depresion.svg",
    alt: "Flujograma: Joven deprimido y aislado tras un fracaso que antes estaba hiperactivo, verborreico y muy autosuficiente: trastorno bipolar"
  },
  "HEM-008": {
    titulo: "Dolor de espalda, pérdida de estatura, anemia, hipercalcemia y lesiones líticas en cráneo y pelvis: mieloma múltiple",
    imagen: "flujogramas/mieloma-multiple-crab.svg",
    alt: "Flujograma: Dolor de espalda, pérdida de estatura, anemia, hipercalcemia y lesiones líticas en cráneo y pelvis: mieloma múltiple"
  },
  "HEM-009": {
    titulo: "Puérpera con anemia, esquistocitos, fiebre, déficit neurológico y oliguria: PTT, dar plasma",
    imagen: "flujogramas/microangiopatia-trombotica-ptt-plasma.svg",
    alt: "Flujograma: Puérpera con anemia, esquistocitos, fiebre, déficit neurológico y oliguria: PTT, dar plasma"
  },
  "HEM-010": {
    titulo: "Mujer joven con cansancio y palpitaciones, microcitosis, hipocromía y ferritina baja: anemia ferropénica",
    imagen: "flujogramas/ferropenia-etapas-anemia.svg",
    alt: "Flujograma: Mujer joven con cansancio y palpitaciones, microcitosis, hipocromía y ferritina baja: anemia ferropénica"
  },
  "NEU-012": {
    titulo: "Obeso que tras diazepam EV queda con Glasgow 9, pH 7,24 y CO₂ 70: soporte ventilatorio",
    imagen: "flujogramas/hipoventilacion-benzodiacepinas-soporte.svg",
    alt: "Flujograma: Obeso que tras diazepam EV queda con Glasgow 9, pH 7,24 y CO₂ 70: soporte ventilatorio"
  },
  "NEF-023": {
    titulo: "Hipotensión y hematuria tras una prostatectomía, oligoanuria y creatinina que se duplica: mantener el volumen arterial efectivo",
    imagen: "flujogramas/lesion-renal-aguda-postoperatoria-volumen.svg",
    alt: "Flujograma: Hipotensión y hematuria tras una prostatectomía, oligoanuria y creatinina que se duplica: mantener el volumen arterial efectivo"
  },
  "END-010": {
    titulo: "Bocio difuso, firme e indoloro con T4 libre baja, TSH alta y captación suprimida: tiroiditis de Hashimoto",
    imagen: "flujogramas/hipotiroidismo-tiroiditis-hashimoto.svg",
    alt: "Flujograma: Bocio difuso, firme e indoloro con T4 libre baja, TSH alta y captación suprimida: tiroiditis de Hashimoto"
  },
  "END-011": {
    titulo: "Diabética tipo 2 de 71 años con poliuria, deshidratación, coma y glucosa de 800 sin cetonas: estado hiperosmolar",
    imagen: "flujogramas/emergencias-glucemicas-hiperosmolar.svg",
    alt: "Flujograma: Diabética tipo 2 de 71 años con poliuria, deshidratación, coma y glucosa de 800 sin cetonas: estado hiperosmolar"
  },
  "END-012": {
    titulo: "Diabético insulinodependiente con conciencia alterada, sudoración profusa y palpitaciones: medir glucosa y dar glucosa EV",
    imagen: "flujogramas/hipoglucemia-grave-glucosa-ev.svg",
    alt: "Flujograma: Diabético insulinodependiente con conciencia alterada, sudoración profusa y palpitaciones: medir glucosa y dar glucosa EV"
  },
  "GAS-019": {
    titulo: "Desorientación progresiva con ascitis, edema y taquicardia: falla hepática crónica con encefalopatía",
    imagen: "flujogramas/ascitis-confusion-falla-hepatica-cronica.svg",
    alt: "Flujograma: Desorientación progresiva con ascitis, edema y taquicardia: falla hepática crónica con encefalopatía"
  },
  "NRL-013": {
    titulo: "Alcohólico crónico en sopor: tiamina endovenosa primero",
    imagen: "flujogramas/coma-alcoholico-tiamina-ev.svg",
    alt: "Flujograma: Alcohólico crónico en sopor: tiamina endovenosa primero"
  },
  "NEU-013": {
    titulo: "Enfisematoso con más tos y disnea y fiebre de 38 °C sin neumonía en la Rx: antibiótico",
    imagen: "flujogramas/exacerbacion-epoc-antibiotico.svg",
    alt: "Flujograma: Enfisematoso con más tos y disnea y fiebre de 38 °C sin neumonía en la Rx: antibiótico"
  },
  "INF-025": {
    titulo: "Parasitosis que se adquieren por contacto con el suelo (la larva atraviesa la piel): uncinariasis y estrongiloidiasis",
    imagen: "flujogramas/parasitos-via-ingreso-penetracion-cutanea.svg",
    alt: "Flujograma: Parasitosis que se adquieren por contacto con el suelo (la larva atraviesa la piel): uncinariasis y estrongiloidiasis"
  },
  "INF-026": {
    titulo: "Agricultor de selva con tos, hemoptisis, dientes flojos y levaduras de gemación múltiple de 20 µm: paracoccidioidomicosis",
    imagen: "flujogramas/micosis-endemicas-paracoccidioidomicosis.svg",
    alt: "Flujograma: Agricultor de selva con tos, hemoptisis, dientes flojos y levaduras de gemación múltiple de 20 µm: paracoccidioidomicosis"
  },
  "NEU-014": {
    titulo: "Joven con febrícula, tos seca persistente, artromialgias, hermanos con lo mismo e infiltrado intersticial: Mycoplasma pneumoniae",
    imagen: "flujogramas/neumonia-atipica-mycoplasma.svg",
    alt: "Flujograma: Joven con febrícula, tos seca persistente, artromialgias, hermanos con lo mismo e infiltrado intersticial: Mycoplasma pneumoniae"
  },
  "NEU-015": {
    titulo: "Neumonía con esputo herrumbroso, soplo tubario y SatO₂ 90 %: cefalosporina de 3.ª generación + macrólido",
    imagen: "flujogramas/neumonia-comunidad-curb65-tratamiento.svg",
    alt: "Flujograma: Neumonía con esputo herrumbroso, soplo tubario y SatO₂ 90 %: cefalosporina de 3.ª generación + macrólido"
  },
  "CAR-024": {
    titulo: "Coronario con disnea, ortopnea, crepitantes bilaterales y galope: insuficiencia cardiaca aguda, furosemida",
    imagen: "flujogramas/insuficiencia-cardiaca-aguda-perfiles.svg",
    alt: "Flujograma: Coronario con disnea, ortopnea, crepitantes bilaterales y galope: insuficiencia cardiaca aguda, furosemida"
  },
  "CAR-025": {
    titulo: "Criterios de Framingham: la disnea paroxística nocturna es un criterio mayor",
    imagen: "flujogramas/criterios-framingham-insuficiencia-cardiaca.svg",
    alt: "Flujograma: Criterios de Framingham: la disnea paroxística nocturna es un criterio mayor"
  },
  "CAR-026": {
    titulo: "Dolor retroesternal de 3 horas con ST elevado en I, aVL y V6: infarto lateral, el objetivo es limitar el área infartada",
    imagen: "flujogramas/infarto-st-elevado-limitar-necrosis.svg",
    alt: "Flujograma: Dolor retroesternal de 3 horas con ST elevado en I, aVL y V6: infarto lateral, el objetivo es limitar el área infartada"
  },
  "GAS-020": {
    titulo: "Derrame pleural izquierdo exudativo días después de una pancreatitis: pedir amilasa en el líquido pleural",
    imagen: "flujogramas/derrame-pleural-pancreatico-amilasa.svg",
    alt: "Flujograma: Derrame pleural izquierdo exudativo días después de una pancreatitis: pedir amilasa en el líquido pleural"
  },
  "NRL-014": {
    titulo: "Diabético mal controlado con dolor en bota, parestesias e hiperalgesia y crisis epilépticas raras: gabapentina",
    imagen: "flujogramas/dolor-neuropatico-diabetico-gabapentina.svg",
    alt: "Flujograma: Diabético mal controlado con dolor en bota, parestesias e hiperalgesia y crisis epilépticas raras: gabapentina"
  },
  "END-013": {
    titulo: "Calambres, dificultad respiratoria, convulsiones y arritmias 24 horas después de una tiroidectomía: medir calcio iónico",
    imagen: "flujogramas/hipocalcemia-postiroidectomia-calcio-ionico.svg",
    alt: "Flujograma: Calambres, dificultad respiratoria, convulsiones y arritmias 24 horas después de una tiroidectomía: medir calcio iónico"
  },
  "NEF-024": {
    titulo: "Anciano con diarrea que recibe solo dextrosa al 5 % y agua libre y cae en coma: medir el sodio",
    imagen: "flujogramas/hiponatremia-hospitalaria-dosaje-sodio.svg",
    alt: "Flujograma: Anciano con diarrea que recibe solo dextrosa al 5 % y agua libre y cae en coma: medir el sodio"
  },
  "NEF-025": {
    titulo: "ERC estadio 4 con K⁺ 7, cambios en la onda T y sensorio alterado: gluconato de calcio EV primero",
    imagen: "flujogramas/hiperpotasemia-gravedad-manejo.svg",
    alt: "Flujograma: ERC estadio 4 con K⁺ 7, cambios en la onda T y sensorio alterado: gluconato de calcio EV primero"
  },
  "REU-014": {
    titulo: "Ama de casa con pliegues ungueales rojos en varios dedos por años y supuración ocasional: paroniquia candidiásica (crónica)",
    imagen: "flujogramas/paroniquia-cronica-candidiasica.svg",
    alt: "Flujograma: Ama de casa con pliegues ungueales rojos en varios dedos por años y supuración ocasional: paroniquia candidiásica (crónica)"
  },
  "HEM-011": {
    titulo: "Artritis reumatoide con anemia microcítica, hierro bajo y ferritina de 520: anemia de enfermedad crónica",
    imagen: "flujogramas/anemia-enfermedad-cronica-perfil-hierro.svg",
    alt: "Flujograma: Artritis reumatoide con anemia microcítica, hierro bajo y ferritina de 520: anemia de enfermedad crónica"
  },
  "CIR-031": {
    titulo: "Paro con actividad eléctrica organizada pero sin pulso en un neumotórax a tensión: disociación electromecánica (AESP)",
    imagen: "flujogramas/ritmos-paro-disociacion-electromecanica.svg",
    alt: "Flujograma: Paro con actividad eléctrica organizada pero sin pulso en un neumotórax a tensión: disociación electromecánica (AESP)"
  },
  "CB-015": {
    titulo: "Ante la caída de la PA en el choque hipovolémico, lo primero es la taquicardia (barorreceptores)",
    imagen: "flujogramas/shock-hipovolemico-compensacion-taquicardia.svg",
    alt: "Flujograma: Ante la caída de la PA en el choque hipovolémico, lo primero es la taquicardia (barorreceptores)"
  },
  "REU-015": {
    titulo: "Picadura de abeja con urticaria, estridor, sibilancias y choque: anafilaxia, adrenalina",
    imagen: "flujogramas/anafilaxia-grados-adrenalina.svg",
    alt: "Flujograma: Picadura de abeja con urticaria, estridor, sibilancias y choque: anafilaxia, adrenalina"
  },
  "NEU-016": {
    titulo: "Primer día tras cirugía de colon: dolor torácico, disnea brusca, PA 70/30 y T negativas en V1-V4: tromboembolismo pulmonar",
    imagen: "flujogramas/tromboembolismo-pulmonar-wells.svg",
    alt: "Flujograma: Primer día tras cirugía de colon: dolor torácico, disnea brusca, PA 70/30 y T negativas en V1-V4: tromboembolismo pulmonar"
  },
  "NEF-026": {
    titulo: "Aplastado por una pared en un sismo, con urea 200, creatinina 6 y CPK alta a las 72 horas: falla renal aguda por rabdomiólisis",
    imagen: "flujogramas/sindrome-aplastamiento-rabdomiolisis-renal.svg",
    alt: "Flujograma: Aplastado por una pared en un sismo, con urea 200, creatinina 6 y CPK alta a las 72 horas: falla renal aguda por rabdomiólisis"
  },
  "CB-016": {
    titulo: "Jardinero en coma con miosis que responde de forma fugaz a un antídoto EV: intoxicación por organofosforados",
    imagen: "flujogramas/toxindromes-colinergico-organofosforados.svg",
    alt: "Flujograma: Jardinero en coma con miosis que responde de forma fugaz a un antídoto EV: intoxicación por organofosforados"
  },
  "NEU-017": {
    titulo: "Derrame exudativo con 98 % de linfocitos, pocas células mesoteliales y ADA de 67 U/L: tuberculosis pleural",
    imagen: "flujogramas/derrame-pleural-linfocitico-ada-tuberculosis.svg",
    alt: "Flujograma: Derrame exudativo con 98 % de linfocitos, pocas células mesoteliales y ADA de 67 U/L: tuberculosis pleural"
  },
  "CIR-032": {
    titulo: "Diabético fumador con claudicación de la pantorrilla a los 100 metros: índice tobillo-brazo como prueba inicial",
    imagen: "flujogramas/claudicacion-indice-tobillo-brazo.svg",
    alt: "Flujograma: Diabético fumador con claudicación de la pantorrilla a los 100 metros: índice tobillo-brazo como prueba inicial"
  },
  "CAR-027": {
    titulo: "Angioedema orolingual sin alergias previas en un paciente que toma enalapril: angioedema por IECA",
    imagen: "flujogramas/angioedema-ieca-bradicinina.svg",
    alt: "Flujograma: Angioedema orolingual sin alergias previas en un paciente que toma enalapril: angioedema por IECA"
  },
  "PED-056": {
    titulo: "En la anemia del prematuro, la hemoglobina mínima es más baja (y más temprana) que en el recién nacido a término",
    imagen: "flujogramas/anemia-prematuro-nadir-hemoglobina.svg",
    alt: "Flujograma: En la anemia del prematuro, la hemoglobina mínima es más baja (y más temprana) que en el recién nacido a término"
  },
  "PED-057": {
    titulo: "Niño de 3 años con edema, proteinuria de 40 mg/m²/h, albúmina 2 y colesterol 300, PA y C3 normales: síndrome nefrótico",
    imagen: "flujogramas/edema-nino-sindrome-nefrotico.svg",
    alt: "Flujograma: Niño de 3 años con edema, proteinuria de 40 mg/m²/h, albúmina 2 y colesterol 300, PA y C3 normales: síndrome nefrótico"
  },
  "END-014": {
    titulo: "Niña de 7 años con telarquia, pubarquia, talla alta, edad ósea de 9 años y útero aumentado: prueba de GnRH para ver si es central",
    imagen: "flujogramas/pubertad-precoz-prueba-gnrh.svg",
    alt: "Flujograma: Niña de 7 años con telarquia, pubarquia, talla alta, edad ósea de 9 años y útero aumentado: prueba de GnRH para ver si es central"
  },
  "PED-058": {
    titulo: "Recién nacido asfixiado (Apgar 2 y 4) con convulsiones tónicas e hipertonía y glucemia normal: fenobarbital EV",
    imagen: "flujogramas/encefalopatia-hipoxica-convulsiones-fenobarbital.svg",
    alt: "Flujograma: Recién nacido asfixiado (Apgar 2 y 4) con convulsiones tónicas e hipertonía y glucemia normal: fenobarbital EV"
  },
  "PED-059": {
    titulo: "Lactante de 6 meses con cólico intermitente, vómitos, heces en jalea de grosella y masa en fosa ilíaca derecha: invaginación intestinal",
    imagen: "flujogramas/invaginacion-intestinal-lactante.svg",
    alt: "Flujograma: Lactante de 6 meses con cólico intermitente, vómitos, heces en jalea de grosella y masa en fosa ilíaca derecha: invaginación intestinal"
  },
  "PED-060": {
    titulo: "Lactante con fiebre, convulsiones, somnolencia, rigidez de nuca y fontanela abombada con fondo de ojo normal: estudio de LCR",
    imagen: "flujogramas/meningitis-lactante-estudio-lcr.svg",
    alt: "Flujograma: Lactante con fiebre, convulsiones, somnolencia, rigidez de nuca y fontanela abombada con fondo de ojo normal: estudio de LCR"
  },
  "PED-061": {
    titulo: "Lactante con fiebre de 38 °C, rinorrea transparente, faringe congestiva y madre resfriada: resfrío común",
    imagen: "flujogramas/resfrio-comun-lactante.svg",
    alt: "Flujograma: Lactante con fiebre de 38 °C, rinorrea transparente, faringe congestiva y madre resfriada: resfrío común"
  },
  "INF-027": {
    titulo: "Escolar con molestias digestivas, tos con sangre, sibilancias y eosinofilia en el esputo: síndrome de Löffler por Ascaris, albendazol",
    imagen: "flujogramas/sindrome-loffler-ascaris-albendazol.svg",
    alt: "Flujograma: Escolar con molestias digestivas, tos con sangre, sibilancias y eosinofilia en el esputo: síndrome de Löffler por Ascaris, albendazol"
  },
  "PED-062": {
    titulo: "Lactante con diarrea, irritable, sediento, con pliegue lento y mucosa seca: deshidratación moderada (algún grado)",
    imagen: "flujogramas/deshidratacion-clasificacion-algun-grado.svg",
    alt: "Flujograma: Lactante con diarrea, irritable, sediento, con pliegue lento y mucosa seca: deshidratación moderada (algún grado)"
  },
  "PED-063": {
    titulo: "Niña con diarrea 5 días antes, palidez, petequias, Hb 6, plaquetas 25 000 y creatinina 4: síndrome urémico hemolítico",
    imagen: "flujogramas/sindrome-uremico-hemolitico-nino.svg",
    alt: "Flujograma: Niña con diarrea 5 días antes, palidez, petequias, Hb 6, plaquetas 25 000 y creatinina 4: síndrome urémico hemolítico"
  },
  "PED-064": {
    titulo: "Lactante de 18 meses con catarro, disfonía, estridor inspiratorio que empeora con el llanto y tiraje: laringotraqueítis aguda",
    imagen: "flujogramas/crup-laringotraqueitis-westley.svg",
    alt: "Flujograma: Lactante de 18 meses con catarro, disfonía, estridor inspiratorio que empeora con el llanto y tiraje: laringotraqueítis aguda"
  },
  "REU-016": {
    titulo: "Niño de 2 años con vesículas alrededor de la nariz que se rompen y forman costras color miel: impétigo",
    imagen: "flujogramas/impetigo-costras-melicericas.svg",
    alt: "Flujograma: Niño de 2 años con vesículas alrededor de la nariz que se rompen y forman costras color miel: impétigo"
  },
  "REU-017": {
    titulo: "Escolar con placa circular de alopecia con escamas, pelos rotos y adenopatía retroauricular: tiña de la cabeza",
    imagen: "flujogramas/alopecia-nino-tina-capitis.svg",
    alt: "Flujograma: Escolar con placa circular de alopecia con escamas, pelos rotos y adenopatía retroauricular: tiña de la cabeza"
  },
  "HEM-012": {
    titulo: "Leucocitos 10 000 con 35 % de segmentados y 5 % de abastonados: recuento absoluto de neutrófilos de 4000/mm³",
    imagen: "flujogramas/recuento-absoluto-neutrofilos-calculo.svg",
    alt: "Flujograma: Leucocitos 10 000 con 35 % de segmentados y 5 % de abastonados: recuento absoluto de neutrófilos de 4000/mm³"
  },
  "CIR-033": {
    titulo: "Adolescente con 2 días de dolor, anorexia, vómitos, fiebre de 39 °C y contractura en fosa ilíaca derecha: apendicitis aguda",
    imagen: "flujogramas/apendicitis-escala-alvarado.svg",
    alt: "Flujograma: Adolescente con 2 días de dolor, anorexia, vómitos, fiebre de 39 °C y contractura en fosa ilíaca derecha: apendicitis aguda"
  },
  "CIR-034": {
    titulo: "Herida de bala en el muslo hace un año con hinchazón, frémito y soplo en la cicatriz y pulsos distales bajos: fístula arteriovenosa",
    imagen: "flujogramas/fistula-arteriovenosa-traumatica.svg",
    alt: "Flujograma: Herida de bala en el muslo hace un año con hinchazón, frémito y soplo en la cicatriz y pulsos distales bajos: fístula arteriovenosa"
  },
  "CIR-035": {
    titulo: "Pesadez vespertina de ambas piernas con hiperpigmentación de la pantorrilla y pulsos presentes: insuficiencia venosa crónica",
    imagen: "flujogramas/insuficiencia-venosa-cronica-ceap.svg",
    alt: "Flujograma: Pesadez vespertina de ambas piernas con hiperpigmentación de la pantorrilla y pulsos presentes: insuficiencia venosa crónica"
  },
  "CIR-036": {
    titulo: "Hemotórax con más de 1500 mL al colocar el tubo y PA < 60 pese a transfundir: toracotomía",
    imagen: "flujogramas/hemotorax-masivo-toracotomia.svg",
    alt: "Flujograma: Hemotórax con más de 1500 mL al colocar el tubo y PA < 60 pese a transfundir: toracotomía"
  },
  "OFT-010": {
    titulo: "Golpe con una piedra en el ojo con diplopía y enoftalmos: fractura del piso (pared inferior) de la órbita",
    imagen: "flujogramas/fractura-orbita-blow-out-piso.svg",
    alt: "Flujograma: Golpe con una piedra en el ojo con diplopía y enoftalmos: fractura del piso (pared inferior) de la órbita"
  },
  "OFT-011": {
    titulo: "Ojo rojo bilateral con lagrimeo, hemorragias conjuntivales, opacidades corneales y ganglio preauricular doloroso: adenovirus",
    imagen: "flujogramas/conjuntivitis-adenovirus-queratoconjuntivitis.svg",
    alt: "Flujograma: Ojo rojo bilateral con lagrimeo, hemorragias conjuntivales, opacidades corneales y ganglio preauricular doloroso: adenovirus"
  },
  "NEF-027": {
    titulo: "Adolescente con testículo aumentado, duro, indoloro y transiluminación negativa: cáncer de testículo",
    imagen: "flujogramas/masa-testicular-indolora-cancer.svg",
    alt: "Flujograma: Adolescente con testículo aumentado, duro, indoloro y transiluminación negativa: cáncer de testículo"
  },
  "NEF-028": {
    titulo: "Cólico lumbar derecho irradiado a genitales con puñopercusión positiva: tomografía helicoidal sin contraste",
    imagen: "flujogramas/colico-renal-imagenes-tomografia.svg",
    alt: "Flujograma: Cólico lumbar derecho irradiado a genitales con puñopercusión positiva: tomografía helicoidal sin contraste"
  },
  "TRA-010": {
    titulo: "Fractura de tibia con pierna tensa, brillante y pulso pedio ausente: síndrome compartimental, fasciotomía",
    imagen: "flujogramas/sindrome-compartimental-fractura-tibia.svg",
    alt: "Flujograma: Fractura de tibia con pierna tensa, brillante y pulso pedio ausente: síndrome compartimental, fasciotomía"
  },
  "TRA-011": {
    titulo: "Tres días después de una fractura de fémur: confusión, disnea, petequias en el pecho y PaO₂ 50 con pulmón normal: embolia grasa",
    imagen: "flujogramas/embolia-grasa-schonfeld.svg",
    alt: "Flujograma: Tres días después de una fractura de fémur: confusión, disnea, petequias en el pecho y PaO₂ 50 con pulmón normal: embolia grasa"
  },
  "CIR-037": {
    titulo: "Diabético con dolor perianal, fiebre y tumefacción con flogosis: absceso perianal",
    imagen: "flujogramas/dolor-perianal-absceso.svg",
    alt: "Flujograma: Diabético con dolor perianal, fiebre y tumefacción con flogosis: absceso perianal"
  },
  "CIR-038": {
    titulo: "Mujer de 65 años con estreñimiento crónico y una masa que sale por el ano al pujar y se reintroduce: prolapso rectal",
    imagen: "flujogramas/masa-anal-prolapso-rectal.svg",
    alt: "Flujograma: Mujer de 65 años con estreñimiento crónico y una masa que sale por el ano al pujar y se reintroduce: prolapso rectal"
  },
  "OFT-012": {
    titulo: "Rinorrea acuosa, estornudos en salva, mucosa pálida y cornetes edematosos con IgE nasal alta: rinitis alérgica",
    imagen: "flujogramas/rinitis-alergica-eosinofilica-diferencial.svg",
    alt: "Flujograma: Rinorrea acuosa, estornudos en salva, mucosa pálida y cornetes edematosos con IgE nasal alta: rinitis alérgica"
  },
  "OFT-013": {
    titulo: "Sangrado nasal por traumatismo: taponamiento nasal anterior como acción inmediata",
    imagen: "flujogramas/epistaxis-traumatica-taponamiento-anterior.svg",
    alt: "Flujograma: Sangrado nasal por traumatismo: taponamiento nasal anterior como acción inmediata"
  },
  "NRL-015": {
    titulo: "Cefalea, convulsiones, hemiplejia, cambios de personalidad y papiledema de 6 meses: tumor con realce en anillo, edema y efecto de masa",
    imagen: "flujogramas/hipertension-endocraneana-lesion-anillo.svg",
    alt: "Flujograma: Cefalea, convulsiones, hemiplejia, cambios de personalidad y papiledema de 6 meses: tumor con realce en anillo, edema y efecto de masa"
  },
  "NRL-016": {
    titulo: "Caída con pérdida de conciencia, intervalo lúcido, midriasis derecha y hemiparesia izquierda: hematoma epidural",
    imagen: "flujogramas/tec-intervalo-lucido-hematoma-epidural.svg",
    alt: "Flujograma: Caída con pérdida de conciencia, intervalo lúcido, midriasis derecha y hemiparesia izquierda: hematoma epidural"
  },
  "PED-065": {
    titulo: "Recién nacido con dificultad respiratoria, murmullo bajo a la izquierda, ruidos cardiacos a la derecha y abdomen escafoide: hernia diafragmática",
    imagen: "flujogramas/distres-neonatal-hernia-diafragmatica-clinica.svg",
    alt: "Flujograma: Recién nacido con dificultad respiratoria, murmullo bajo a la izquierda, ruidos cardiacos a la derecha y abdomen escafoide: hernia diafragmática"
  },
  "SP-039": {
    titulo: "Víctima de violación a la que el médico, por motivos religiosos, niega la anticoncepción de emergencia: se vulnera su autonomía",
    imagen: "flujogramas/autonomia-anticoncepcion-emergencia-violacion.svg",
    alt: "Flujograma: Víctima de violación a la que el médico, por motivos religiosos, niega la anticoncepción de emergencia: se vulnera su autonomía"
  },
  "GIN-048": {
    titulo: "34 semanas con dolor intenso, útero en contracción sostenida, sangrado oscuro escaso y sin latidos fetales: desprendimiento prematuro de placenta",
    imagen: "flujogramas/desprendimiento-placenta-grado-obito.svg",
    alt: "Flujograma: 34 semanas con dolor intenso, útero en contracción sostenida, sangrado oscuro escaso y sin latidos fetales: desprendimiento prematuro de placenta"
  },
  "GIN-049": {
    titulo: "Puérpera de un parto complicado con fiebre y loquios fétidos a las 36 horas y endometrio de 7 mm: endometritis puerperal",
    imagen: "flujogramas/fiebre-puerperal-endometritis.svg",
    alt: "Flujograma: Puérpera de un parto complicado con fiebre y loquios fétidos a las 36 horas y endometrio de 7 mm: endometritis puerperal"
  },
  "GIN-050": {
    titulo: "34 semanas con fiebre de 39 °C, taquicardia fetal de 165 y nitrazina y helecho positivos: corioamnionitis",
    imagen: "flujogramas/fiebre-gestante-rpm-corioamnionitis.svg",
    alt: "Flujograma: 34 semanas con fiebre de 39 °C, taquicardia fetal de 165 y nitrazina y helecho positivos: corioamnionitis"
  },
  "GIN-051": {
    titulo: "Gestante de 36 semanas con fiebre de 39 °C y puñopercusión lumbar derecha muy positiva: pielonefritis, ceftriaxona",
    imagen: "flujogramas/pielonefritis-gestante-antibiotico.svg",
    alt: "Flujograma: Gestante de 36 semanas con fiebre de 39 °C y puñopercusión lumbar derecha muy positiva: pielonefritis, ceftriaxona"
  },
  "GIN-052": {
    titulo: "42 semanas con bienestar fetal normal y cuello blando, anterior, borrado 80 %, 1 cm y estación 0: inducción con oxitocina",
    imagen: "flujogramas/embarazo-prolongado-bishop-induccion.svg",
    alt: "Flujograma: 42 semanas con bienestar fetal normal y cuello blando, anterior, borrado 80 %, 1 cm y estación 0: inducción con oxitocina"
  },
  "GIN-053": {
    titulo: "Distocia de hombros en un feto grande: hiperflexión de los muslos de la madre (maniobra de McRoberts)",
    imagen: "flujogramas/distocia-hombros-mcroberts.svg",
    alt: "Flujograma: Distocia de hombros en un feto grande: hiperflexión de los muslos de la madre (maniobra de McRoberts)"
  },
  "GIN-054": {
    titulo: "Posmenopáusica nulípara, hipertensa y diabética con ginecorragia y endometrio de 12 mm: biopsia de endometrio",
    imagen: "flujogramas/sangrado-posmenopausico-biopsia-endometrio.svg",
    alt: "Flujograma: Posmenopáusica nulípara, hipertensa y diabética con ginecorragia y endometrio de 12 mm: biopsia de endometrio"
  },
  "GIN-055": {
    titulo: "Flujo maloliente que empeora tras el coito y el jabón, más prurito y eritema vulvar: vaginitis mixta, metronidazol + clotrimazol",
    imagen: "flujogramas/vaginitis-mixta-metronidazol-clotrimazol.svg",
    alt: "Flujograma: Flujo maloliente que empeora tras el coito y el jabón, más prurito y eritema vulvar: vaginitis mixta, metronidazol + clotrimazol"
  },
  "GIN-056": {
    titulo: "Niña de 7 años con dolor en fosa ilíaca y neoplasia ovárica: tumor de células germinales",
    imagen: "flujogramas/tumores-ovaricos-nina-celulas-germinales.svg",
    alt: "Flujograma: Niña de 7 años con dolor en fosa ilíaca y neoplasia ovárica: tumor de células germinales"
  },
  "PED-066": {
    titulo: "Niño de 6 años sin ninguna vacuna: la vacuna contra Haemophilus influenzae tipo b ya no es necesaria",
    imagen: "flujogramas/vacunacion-tardia-seis-anos-hib.svg",
    alt: "Flujograma: Niño de 6 años sin ninguna vacuna: la vacuna contra Haemophilus influenzae tipo b ya no es necesaria"
  },
  "CB-017": {
    titulo: "La apoptosis se desencadena cuando la célula sufre un daño irreversible de su ADN",
    imagen: "flujogramas/apoptosis-dano-adn-p53.svg",
    alt: "Flujograma: La apoptosis se desencadena cuando la célula sufre un daño irreversible de su ADN"
  },
  "CB-018": {
    titulo: "Capacidad de un medicamento de producir el efecto deseado en condiciones ideales: eficacia",
    imagen: "flujogramas/eficacia-efectividad-eficiencia.svg",
    alt: "Flujograma: Capacidad de un medicamento de producir el efecto deseado en condiciones ideales: eficacia"
  },
  "CB-019": {
    titulo: "Hipotiroidea que inicia tratamiento de dislipidemia y a la semana tiene mialgias: atorvastatina",
    imagen: "flujogramas/mialgias-estatinas-reaccion-adversa.svg",
    alt: "Flujograma: Hipotiroidea que inicia tratamiento de dislipidemia y a la semana tiene mialgias: atorvastatina"
  },
  "CB-020": {
    titulo: "Tras cirugía de una fístula traqueal, la glotis no se abre bien: lesión del músculo cricoaritenoideo posterior",
    imagen: "flujogramas/musculos-laringe-cricoaritenoideo-posterior.svg",
    alt: "Flujograma: Tras cirugía de una fístula traqueal, la glotis no se abre bien: lesión del músculo cricoaritenoideo posterior"
  },
  "GIN-057": {
    titulo: "La clave roja de las emergencias obstétricas se activa en las hemorragias",
    imagen: "flujogramas/claves-obstetricas-roja-azul-amarilla.svg",
    alt: "Flujograma: La clave roja de las emergencias obstétricas se activa en las hemorragias"
  },
  "NEU-018": {
    titulo: "Fumador con dolor de hombro que baja por el borde cubital: tumor de Pancoast",
    imagen: "flujogramas/dolor-hombro-fumador-pancoast.svg",
    alt: "Flujograma: Fumador con dolor de hombro que baja por el borde cubital: tumor de Pancoast"
  },
  "SP-040": {
    titulo: "Determinantes sociales de la salud: la etnia o raza es un determinante estructural",
    imagen: "flujogramas/determinantes-sociales-estructurales-etnia.svg",
    alt: "Flujograma: Determinantes sociales de la salud: la etnia o raza es un determinante estructural"
  },
  "SP-041": {
    titulo: "Para determinar qué factores preceden a la aparición de casos de Zika: estudio de cohorte",
    imagen: "flujogramas/disenos-estudio-cohorte-matriz.svg",
    alt: "Flujograma: Para determinar qué factores preceden a la aparición de casos de Zika: estudio de cohorte"
  },
  "CB-021": {
    titulo: "Ataque con gas sarín (inhibidor de la colinesterasa) con sobreestimulación colinérgica: atropina EV",
    imagen: "flujogramas/antidotos-sarin-atropina.svg",
    alt: "Flujograma: Ataque con gas sarín (inhibidor de la colinesterasa) con sobreestimulación colinérgica: atropina EV"
  },
  "SP-042": {
    titulo: "Estudio en pacientes hospitalizados iniciado en secreto, sin consentimiento ni aprobación ética: incumple la Declaración de Helsinki",
    imagen: "flujogramas/etica-investigacion-helsinki-comite.svg",
    alt: "Flujograma: Estudio en pacientes hospitalizados iniciado en secreto, sin consentimiento ni aprobación ética: incumple la Declaración de Helsinki"
  },
  "PED-067": {
    titulo: "Lactante de 6 meses con catarro y fiebre que al tercer día tiene taquipnea, tiraje y sibilancias: bronquiolitis",
    imagen: "flujogramas/lactante-sibilancias-bronquiolitis.svg",
    alt: "Flujograma: Lactante de 6 meses con catarro y fiebre que al tercer día tiene taquipnea, tiraje y sibilancias: bronquiolitis"
  },
  "END-015": {
    titulo: "Joven con LDL 320, xantomas tendinosos y padre y hermana con colesterol muy alto: hipercolesterolemia familiar",
    imagen: "flujogramas/hipercolesterolemia-familiar-dutch-lipid.svg",
    alt: "Flujograma: Joven con LDL 320, xantomas tendinosos y padre y hermana con colesterol muy alto: hipercolesterolemia familiar"
  },
  "GIN-058": {
    titulo: "Flujo amarillento, espumoso y maloliente con prurito y cérvix en fresa: Trichomonas vaginalis",
    imagen: "flujogramas/flujo-espumoso-colpitis-fresa-tricomonas.svg",
    alt: "Flujograma: Flujo amarillento, espumoso y maloliente con prurito y cérvix en fresa: Trichomonas vaginalis"
  },
  "CB-022": {
    titulo: "Paciente soporoso, con FR 12, pupilas reactivas e hipotermia leve que despierta con flumazenil: benzodiacepinas",
    imagen: "flujogramas/coma-toxico-benzodiacepinas-flumazenil.svg",
    alt: "Flujograma: Paciente soporoso, con FR 12, pupilas reactivas e hipotermia leve que despierta con flumazenil: benzodiacepinas"
  },
  "HEM-013": {
    titulo: "Adenopatías cervicales y axilares indoloras, elásticas, con fiebre: biopsia escisional de un ganglio",
    imagen: "flujogramas/adenopatias-generalizadas-biopsia-linfoma.svg",
    alt: "Flujograma: Adenopatías cervicales y axilares indoloras, elásticas, con fiebre: biopsia escisional de un ganglio"
  },
  "SP-043": {
    titulo: "Comparar el efecto de preguntas de 3 frente a 5 alternativas asignadas por el investigador: estudio experimental",
    imagen: "flujogramas/piramide-evidencia-estudio-experimental.svg",
    alt: "Flujograma: Comparar el efecto de preguntas de 3 frente a 5 alternativas asignadas por el investigador: estudio experimental"
  },
  "OFT-014": {
    titulo: "Lactante con catarro que llora, rechaza el alimento y se golpea las orejas: otoscopia para confirmar otitis media aguda",
    imagen: "flujogramas/lactante-otalgia-otoscopia.svg",
    alt: "Flujograma: Lactante con catarro que llora, rechaza el alimento y se golpea las orejas: otoscopia para confirmar otitis media aguda"
  },
  "NRL-017": {
    titulo: "Herida por arma blanca en la nuca con parálisis del hemicuerpo derecho y alteración sensitiva del lado opuesto: Brown-Séquard, RM cervical",
    imagen: "flujogramas/sindromes-medulares-brown-sequard.svg",
    alt: "Flujograma: Herida por arma blanca en la nuca con parálisis del hemicuerpo derecho y alteración sensitiva del lado opuesto: Brown-Séquard, RM cervical"
  },
  "PED-068": {
    titulo: "Lactante desnutrido con cefalohematoma, marcas curvas en las piernas y equimosis en muslos y escroto: maltrato infantil",
    imagen: "flujogramas/lactante-equimosis-patron-maltrato.svg",
    alt: "Flujograma: Lactante desnutrido con cefalohematoma, marcas curvas en las piernas y equimosis en muslos y escroto: maltrato infantil"
  },
  "PED-069": {
    titulo: "Recién nacido con hipotermia, mala succión, dificultad respiratoria, leucopenia e índice I/T de 0,3: sepsis, ampicilina + amikacina",
    imagen: "flujogramas/sepsis-neonatal-temprana-tardia-matriz.svg",
    alt: "Flujograma: Recién nacido con hipotermia, mala succión, dificultad respiratoria, leucopenia e índice I/T de 0,3: sepsis, ampicilina + amikacina"
  },
  "SP-044": {
    titulo: "El médico jefe moviliza al personal en brigadas a domicilio y logra la cobertura de la tercera dosis: liderazgo",
    imagen: "flujogramas/gestion-salud-liderazgo-vacunacion.svg",
    alt: "Flujograma: El médico jefe moviliza al personal en brigadas a domicilio y logra la cobertura de la tercera dosis: liderazgo"
  },
  "SP-045": {
    titulo: "Varias mordeduras por perros callejeros que no se pueden capturar: coordinar con la municipalidad",
    imagen: "flujogramas/mordeduras-perros-callejeros-municipalidad.svg",
    alt: "Flujograma: Varias mordeduras por perros callejeros que no se pueden capturar: coordinar con la municipalidad"
  },
  "GIN-059": {
    titulo: "Hemorragia posparto masiva tras un feto de 4100 g con útero blando a nivel del ombligo y choque: atonía uterina",
    imagen: "flujogramas/hemorragia-posparto-atonia-uterina.svg",
    alt: "Flujograma: Hemorragia posparto masiva tras un feto de 4100 g con útero blando a nivel del ombligo y choque: atonía uterina"
  },
  "PED-070": {
    titulo: "Para prevenir la anemia al iniciar la alimentación complementaria: incluir a diario alimentos de origen animal",
    imagen: "flujogramas/alimentacion-complementaria-hierro-anemia.svg",
    alt: "Flujograma: Para prevenir la anemia al iniciar la alimentación complementaria: incluir a diario alimentos de origen animal"
  },
  "REU-018": {
    titulo: "Rodilla dolorosa y aumentada de volumen con 12 000 leucocitos en el líquido sinovial: líquido inflamatorio",
    imagen: "flujogramas/liquido-sinovial-clasificacion.svg",
    alt: "Flujograma: Rodilla dolorosa y aumentada de volumen con 12 000 leucocitos en el líquido sinovial: líquido inflamatorio"
  },
  "NEF-029": {
    titulo: "Ambos miembros inferiores aplastados por una pared y oligoanuria horas después: CPK total para diagnosticar rabdomiólisis",
    imagen: "flujogramas/aplastamiento-oliguria-cpk.svg",
    alt: "Flujograma: Ambos miembros inferiores aplastados por una pared y oligoanuria horas después: CPK total para diagnosticar rabdomiólisis"
  },
  "OFT-015": {
    titulo: "Asmática alérgica a sulfas con dolor y pérdida brusca de visión, edema corneal y ángulo cerrado: glaucoma agudo, manitol",
    imagen: "flujogramas/glaucoma-agudo-asma-alergia-sulfas-manitol.svg",
    alt: "Flujograma: Asmática alérgica a sulfas con dolor y pérdida brusca de visión, edema corneal y ángulo cerrado: glaucoma agudo, manitol"
  },
  "GIN-060": {
    titulo: "Gestante de 28 semanas con pielonefritis en resolución: nitrofurantoína diaria para prevenir la recurrencia",
    imagen: "flujogramas/itu-embarazo-profilaxis-nitrofurantoina.svg",
    alt: "Flujograma: Gestante de 28 semanas con pielonefritis en resolución: nitrofurantoína diaria para prevenir la recurrencia"
  },
  "NRL-018": {
    titulo: "Hipertensa con hemiplejia derecha y afasia que revierten en 15 minutos y TC normal: ataque isquémico transitorio",
    imagen: "flujogramas/ataque-isquemico-transitorio-abcd2.svg",
    alt: "Flujograma: Hipertensa con hemiplejia derecha y afasia que revierten en 15 minutos y TC normal: ataque isquémico transitorio"
  },
  "CIR-039": {
    titulo: "Politraumatizado que abre los ojos al dolor, emite sonidos incomprensibles y cae en sopor: intubación orotraqueal",
    imagen: "flujogramas/politraumatizado-glasgow-intubacion.svg",
    alt: "Flujograma: Politraumatizado que abre los ojos al dolor, emite sonidos incomprensibles y cae en sopor: intubación orotraqueal"
  },
  "NEU-019": {
    titulo: "Fumador con hemoptisis, baja de peso, BK negativo y masa suprahiliar de 5 cm: broncofibroscopia con biopsia",
    imagen: "flujogramas/masa-pulmonar-central-broncofibroscopia.svg",
    alt: "Flujograma: Fumador con hemoptisis, baja de peso, BK negativo y masa suprahiliar de 5 cm: broncofibroscopia con biopsia"
  },
  "PSI-013": {
    titulo: "Migrante a Lima hace 3 meses con insomnio, irritabilidad y desconfianza que sigue funcionando en el trabajo: trastorno de adaptación",
    imagen: "flujogramas/migracion-trastorno-adaptacion.svg",
    alt: "Flujograma: Migrante a Lima hace 3 meses con insomnio, irritabilidad y desconfianza que sigue funcionando en el trabajo: trastorno de adaptación"
  },
  "PED-071": {
    titulo: "Neonato con síndrome de Down, vómitos biliosos y distensión en el 2.º día: atresia duodenal",
    imagen: "flujogramas/vomito-bilioso-down-atresia-duodenal.svg",
    alt: "Flujograma: Neonato con síndrome de Down, vómitos biliosos y distensión en el 2.º día: atresia duodenal"
  },
  "PED-072": {
    titulo: "Niña con fiebre, catarro intenso, conjuntivitis, manchas en la mucosa yugal y exantema morbiliforme confluente: sarampión, preguntar por la vacuna",
    imagen: "flujogramas/sarampion-fases-vacunacion.svg",
    alt: "Flujograma: Niña con fiebre, catarro intenso, conjuntivitis, manchas en la mucosa yugal y exantema morbiliforme confluente: sarampión, preguntar por la vacuna"
  },
  "PED-073": {
    titulo: "Adolescente que ayuda en la cosecha de uvas con cólicos, vómitos, diarrea y fasciculaciones: intoxicación por insecticidas",
    imagen: "flujogramas/intoxicacion-insecticida-cosecha.svg",
    alt: "Flujograma: Adolescente que ayuda en la cosecha de uvas con cólicos, vómitos, diarrea y fasciculaciones: intoxicación por insecticidas"
  },
  "SP-046": {
    titulo: "Describir cuántos adultos mayores hay, su sexo, su pobreza y su seguro: fase de análisis del entorno del ASIS",
    imagen: "flujogramas/asis-analisis-del-entorno.svg",
    alt: "Flujograma: Describir cuántos adultos mayores hay, su sexo, su pobreza y su seguro: fase de análisis del entorno del ASIS"
  },
  "REU-019": {
    titulo: "Mayor con cefalea, dolor temporal, claudicación mandibular, amaurosis y VSG de 150: arteritis de células gigantes, corticoides",
    imagen: "flujogramas/arteritis-celulas-gigantes-corticoide.svg",
    alt: "Flujograma: Mayor con cefalea, dolor temporal, claudicación mandibular, amaurosis y VSG de 150: arteritis de células gigantes, corticoides"
  },
  "END-016": {
    titulo: "Baja de peso con apetito aumentado, intolerancia al calor, sudoración, taquicardia y PA diferencial amplia: hipertiroidismo",
    imagen: "flujogramas/hipermetabolismo-hipertiroidismo.svg",
    alt: "Flujograma: Baja de peso con apetito aumentado, intolerancia al calor, sudoración, taquicardia y PA diferencial amplia: hipertiroidismo"
  },
  "GIN-061": {
    titulo: "Puérpera de 2 semanas con fiebre y mama derecha roja, dolorosa e indurada: mastitis, antibiótico y seguimiento",
    imagen: "flujogramas/mama-dolorosa-puerperio-mastitis.svg",
    alt: "Flujograma: Puérpera de 2 semanas con fiebre y mama derecha roja, dolorosa e indurada: mastitis, antibiótico y seguimiento"
  },
  "GIN-062": {
    titulo: "Cesareada anterior en trabajo de parto con dolor súbito, sangrado, partes fetales palpables y bradicardia fetal: rotura uterina",
    imagen: "flujogramas/sangrado-tercer-trimestre-rotura-uterina.svg",
    alt: "Flujograma: Cesareada anterior en trabajo de parto con dolor súbito, sangrado, partes fetales palpables y bradicardia fetal: rotura uterina"
  },
  "SP-047": {
    titulo: "Aumento de tuberculosis con hacinamiento y desempleo en el ámbito: la mayor influencia son los determinantes sociales",
    imagen: "flujogramas/tuberculosis-hacinamiento-determinantes.svg",
    alt: "Flujograma: Aumento de tuberculosis con hacinamiento y desempleo en el ámbito: la mayor influencia son los determinantes sociales"
  },
  "NEF-030": {
    titulo: "Dolor lumbar izquierdo súbito irradiado a la ingle, puñopercusión positiva, hematuria y cristales de oxalato: litiasis renal",
    imagen: "flujogramas/dolor-lumbar-agudo-litiasis-renal.svg",
    alt: "Flujograma: Dolor lumbar izquierdo súbito irradiado a la ingle, puñopercusión positiva, hematuria y cristales de oxalato: litiasis renal"
  },
  "PED-074": {
    titulo: "Lactante de 5 meses con ganancia de peso insuficiente que dejó de acudir a sus controles: visita domiciliaria",
    imagen: "flujogramas/ganancia-peso-insuficiente-visita-domiciliaria.svg",
    alt: "Flujograma: Lactante de 5 meses con ganancia de peso insuficiente que dejó de acudir a sus controles: visita domiciliaria"
  },
  "CB-023": {
    titulo: "Cefalea, náuseas y confusión repetidas en una casa cerrada con estufa de gas y SatO₂ normal: monóxido de carbono, oxígeno al 100 %",
    imagen: "flujogramas/monoxido-carbono-estufa-oxigeno.svg",
    alt: "Flujograma: Cefalea, náuseas y confusión repetidas en una casa cerrada con estufa de gas y SatO₂ normal: monóxido de carbono, oxígeno al 100 %"
  },
  "REU-020": {
    titulo: "Varón joven con acné grave y cicatricial en cara y tórax, fiebre, artralgias y leucocitosis: acné fulminante",
    imagen: "flujogramas/acne-fulminante-fiebre-artralgias.svg",
    alt: "Flujograma: Varón joven con acné grave y cicatricial en cara y tórax, fiebre, artralgias y leucocitosis: acné fulminante"
  },
  "GAS-021": {
    titulo: "Obeso con dolor epigástrico a la espalda, vómitos, choque, sopor, triglicéridos altos y amilasa normal: pancreatitis, hidratación EV",
    imagen: "flujogramas/pancreatitis-hipertrigliceridemia-hidratacion.svg",
    alt: "Flujograma: Obeso con dolor epigástrico a la espalda, vómitos, choque, sopor, triglicéridos altos y amilasa normal: pancreatitis, hidratación EV"
  },
  "PED-075": {
    titulo: "Primogénito de un mes con vómitos en proyectil no biliosos, deshidratación y oliva epigástrica: hipertrofia del píloro",
    imagen: "flujogramas/vomitos-lactante-hipertrofia-piloro.svg",
    alt: "Flujograma: Primogénito de un mes con vómitos en proyectil no biliosos, deshidratación y oliva epigástrica: hipertrofia del píloro"
  },
  "PED-076": {
    titulo: "Niño de 2 años con tos, fiebre de 40 °C, FR 50, tiraje y crepitantes con murmullo disminuido a la derecha: neumonía adquirida en la comunidad",
    imagen: "flujogramas/neumonia-nino-tipos-comunidad.svg",
    alt: "Flujograma: Niño de 2 años con tos, fiebre de 40 °C, FR 50, tiraje y crepitantes con murmullo disminuido a la derecha: neumonía adquirida en la comunidad"
  },
  "CIR-040": {
    titulo: "Herida precordial con PA 90/60, PVC 16, yugulares ingurgitadas y ruidos apagados: taponamiento cardiaco, pericardiocentesis",
    imagen: "flujogramas/herida-precordial-taponamiento-pericardiocentesis.svg",
    alt: "Flujograma: Herida precordial con PA 90/60, PVC 16, yugulares ingurgitadas y ruidos apagados: taponamiento cardiaco, pericardiocentesis"
  },
  "SP-048": {
    titulo: "Intubar a un adulto que dejó por escrito su deseo de no ser intubado: se vulnera su autonomía",
    imagen: "flujogramas/voluntad-anticipada-autonomia-ventilacion.svg",
    alt: "Flujograma: Intubar a un adulto que dejó por escrito su deseo de no ser intubado: se vulnera su autonomía"
  },
  "TRA-012": {
    titulo: "Fractura del tercio medio de la diáfisis del húmero: se espera mano péndula (lesión del nervio radial)",
    imagen: "flujogramas/fractura-humero-nervios-mano-pendula.svg",
    alt: "Flujograma: Fractura del tercio medio de la diáfisis del húmero: se espera mano péndula (lesión del nervio radial)"
  },
  "PSI-014": {
    titulo: "Joven con falta de aire, sudoración, palpitaciones, dolor torácico, temblor y miedo a morir que ceden solos ante el estrés: crisis de pánico",
    imagen: "flujogramas/crisis-panico-curso-sintomas.svg",
    alt: "Flujograma: Joven con falta de aire, sudoración, palpitaciones, dolor torácico, temblor y miedo a morir que ceden solos ante el estrés: crisis de pánico"
  },
  "GAS-022": {
    titulo: "Pancreatitis crónica alcohólica con heces pálidas, brillantes y untuosas: insuficiencia pancreática exocrina",
    imagen: "flujogramas/esteatorrea-pancreatitis-cronica-insuficiencia.svg",
    alt: "Flujograma: Pancreatitis crónica alcohólica con heces pálidas, brillantes y untuosas: insuficiencia pancreática exocrina"
  },
  "END-017": {
    titulo: "Crisis de palpitaciones, cefalea y sudoración con PA 180/120 y metanefrinas urinarias altas: feocromocitoma",
    imagen: "flujogramas/hipertension-paroxistica-feocromocitoma.svg",
    alt: "Flujograma: Crisis de palpitaciones, cefalea y sudoración con PA 180/120 y metanefrinas urinarias altas: feocromocitoma"
  },
  "PED-077": {
    titulo: "Lactante febril con crisis generalizada de 30 minutos y sueño posterior: convulsión febril compleja",
    imagen: "flujogramas/convulsion-febril-compleja-criterios.svg",
    alt: "Flujograma: Lactante febril con crisis generalizada de 30 minutos y sueño posterior: convulsión febril compleja"
  },
  "GIN-063": {
    titulo: "33 semanas con pérdida de líquido claro hace 8 horas, sin contracciones ni infección, en un centro de salud: maduración pulmonar, antibiótico y referencia",
    imagen: "flujogramas/rotura-membranas-pretermino-manejo.svg",
    alt: "Flujograma: 33 semanas con pérdida de líquido claro hace 8 horas, sin contracciones ni infección, en un centro de salud: maduración pulmonar, antibiótico y referencia"
  },
  "NEU-020": {
    titulo: "Exacerbación de EPOC con PaO₂ 62 sin opacidades focales: la hipoxemia se debe al desequilibrio ventilación-perfusión",
    imagen: "flujogramas/mecanismos-hipoxemia-epoc-vq.svg",
    alt: "Flujograma: Exacerbación de EPOC con PaO₂ 62 sin opacidades focales: la hipoxemia se debe al desequilibrio ventilación-perfusión"
  },
  "PED-078": {
    titulo: "Lactante de 5 meses con poca ganancia de peso, taquipnea y sudor al lactar, taquicardia, soplo y hepatomegalia: insuficiencia cardiaca",
    imagen: "flujogramas/lactante-sudoracion-lactancia-insuficiencia-cardiaca.svg",
    alt: "Flujograma: Lactante de 5 meses con poca ganancia de peso, taquipnea y sudor al lactar, taquicardia, soplo y hepatomegalia: insuficiencia cardiaca"
  },
  "CIR-041": {
    titulo: "Quemaduras de cara y cuello con edema oral, esputo negro, hollín en boca y nariz, estridor y cianosis: intubación endotraqueal",
    imagen: "flujogramas/quemadura-facial-estridor-intubacion.svg",
    alt: "Flujograma: Quemaduras de cara y cuello con edema oral, esputo negro, hollín en boca y nariz, estridor y cianosis: intubación endotraqueal"
  },
  "CAR-028": {
    titulo: "Pérdida súbita de conciencia sin pulso ni respiración con ritmo acelerado en el monitor: desfibrilación",
    imagen: "flujogramas/arritmias-pulso-desfibrilacion-cardioversion.svg",
    alt: "Flujograma: Pérdida súbita de conciencia sin pulso ni respiración con ritmo acelerado en el monitor: desfibrilación"
  },
  "GAS-023": {
    titulo: "Colitis ulcerosa con diarrea tratada con loperamida, fiebre, taquicardia, distensión y RHA ausentes: megacolon tóxico",
    imagen: "flujogramas/megacolon-toxico-criterios-jalan.svg",
    alt: "Flujograma: Colitis ulcerosa con diarrea tratada con loperamida, fiebre, taquicardia, distensión y RHA ausentes: megacolon tóxico"
  },
  "GIN-064": {
    titulo: "Gestante de 14 semanas con sobrepeso e hijo previo de 4400 g y tamizaje negativo: repetir la prueba a las 24-28 semanas",
    imagen: "flujogramas/diabetes-gestacional-tamizaje-24-28.svg",
    alt: "Flujograma: Gestante de 14 semanas con sobrepeso e hijo previo de 4400 g y tamizaje negativo: repetir la prueba a las 24-28 semanas"
  },
  "GIN-065": {
    titulo: "Para prevenir la endometritis puerperal: disminuir los tactos vaginales innecesarios",
    imagen: "flujogramas/prevencion-endometritis-tactos-vaginales.svg",
    alt: "Flujograma: Para prevenir la endometritis puerperal: disminuir los tactos vaginales innecesarios"
  },
  "REU-021": {
    titulo: "Adolescente atópico con dermatitis atópica: la terapia tópica de base son los emolientes e hidratantes",
    imagen: "flujogramas/dermatitis-atopica-escalera-emolientes.svg",
    alt: "Flujograma: Adolescente atópico con dermatitis atópica: la terapia tópica de base son los emolientes e hidratantes"
  },
  "INF-028": {
    titulo: "COVID-19: el SARS-CoV-2 se une al receptor ACE2 mediante la proteína S (espiga)",
    imagen: "flujogramas/sars-cov-2-ciclo-ace2.svg",
    alt: "Flujograma: COVID-19: el SARS-CoV-2 se une al receptor ACE2 mediante la proteína S (espiga)"
  },
  "CIR-042": {
    titulo: "Contusión toracoabdominal con choque, yugulares ingurgitadas, ruidos apagados, bajo voltaje y pericardiocentesis fallida: toracotomía",
    imagen: "flujogramas/taponamiento-traumatico-toracotomia.svg",
    alt: "Flujograma: Contusión toracoabdominal con choque, yugulares ingurgitadas, ruidos apagados, bajo voltaje y pericardiocentesis fallida: toracotomía"
  },
  "CIR-043": {
    titulo: "Ictericia tras cólico biliar con colangiorresonancia que muestra cálculos en el colédoco, uno impactado de 1,3 cm: papilotomía endoscópica",
    imagen: "flujogramas/coledocolitiasis-cpre-papilotomia.svg",
    alt: "Flujograma: Ictericia tras cólico biliar con colangiorresonancia que muestra cálculos en el colédoco, uno impactado de 1,3 cm: papilotomía endoscópica"
  },
  "GIN-066": {
    titulo: "Mujer de 60 años con prurito vulvar, poco flujo y mucosa roja y seca: vaginitis atrófica",
    imagen: "flujogramas/prurito-vulvar-posmenopausia-atrofia.svg",
    alt: "Flujograma: Mujer de 60 años con prurito vulvar, poco flujo y mucosa roja y seca: vaginitis atrófica"
  },
  "HEM-014": {
    titulo: "Niña de 4 años con palidez, dolor óseo, hepatoesplenomegalia, anemia, plaquetas 20 000 y linfoblastos en sangre: aspirado de médula ósea",
    imagen: "flujogramas/nina-citopenias-hepatoesplenomegalia-lla.svg",
    alt: "Flujograma: Niña de 4 años con palidez, dolor óseo, hepatoesplenomegalia, anemia, plaquetas 20 000 y linfoblastos en sangre: aspirado de médula ósea"
  },
  "CIR-044": {
    titulo: "Herida en el muslo con dolor intenso, fiebre, ampollas marrones y secreción en «agua de lavar carne»: fascitis necrotizante",
    imagen: "flujogramas/infeccion-partes-blandas-fascitis-necrotizante.svg",
    alt: "Flujograma: Herida en el muslo con dolor intenso, fiebre, ampollas marrones y secreción en «agua de lavar carne»: fascitis necrotizante"
  },
  "GIN-067": {
    titulo: "Puérpera poscesárea con PA 60/40, FC 120 y palidez creciente: choque hipovolémico (de contenido)",
    imagen: "flujogramas/shock-obstetrico-tipos-hipovolemico.svg",
    alt: "Flujograma: Puérpera poscesárea con PA 60/40, FC 120 y palidez creciente: choque hipovolémico (de contenido)"
  },
  "PED-079": {
    titulo: "Lactante de 1 mes con tos paroxística, estridor y ahogo y hermano con lo mismo: tos ferina, azitromicina",
    imagen: "flujogramas/tos-ferina-fases-azitromicina.svg",
    alt: "Flujograma: Lactante de 1 mes con tos paroxística, estridor y ahogo y hermano con lo mismo: tos ferina, azitromicina"
  },
  "CIR-045": {
    titulo: "Adulto mayor andino con dolor, gran distensión y vómitos fecaloideos con Rx en «grano de café»: vólvulo de sigmoides",
    imagen: "flujogramas/obstruccion-colon-altura-volvulo-sigmoides.svg",
    alt: "Flujograma: Adulto mayor andino con dolor, gran distensión y vómitos fecaloideos con Rx en «grano de café»: vólvulo de sigmoides"
  },
  "NEU-021": {
    titulo: "Obrero expuesto a polvo con disnea, acropaquias, crepitantes «tipo velcro» y pulmones pequeños reticulares: enfermedad pulmonar intersticial",
    imagen: "flujogramas/disnea-cronica-crepitantes-epid.svg",
    alt: "Flujograma: Obrero expuesto a polvo con disnea, acropaquias, crepitantes «tipo velcro» y pulmones pequeños reticulares: enfermedad pulmonar intersticial"
  },
  "CAR-029": {
    titulo: "Tras recuperar la circulación, intubado con 14 ventilaciones por minuto y PaCO₂ 30: hiperventila, hay que bajar la frecuencia",
    imagen: "flujogramas/cuidados-posparo-paco2-ventilacion.svg",
    alt: "Flujograma: Tras recuperar la circulación, intubado con 14 ventilaciones por minuto y PaCO₂ 30: hiperventila, hay que bajar la frecuencia"
  },
  "CIR-046": {
    titulo: "Fiebre en los primeros días tras una laparotomía con murmullo disminuido en la base derecha: atelectasia",
    imagen: "flujogramas/fiebre-postoperatoria-atelectasia.svg",
    alt: "Flujograma: Fiebre en los primeros días tras una laparotomía con murmullo disminuido en la base derecha: atelectasia"
  },
  "INF-029": {
    titulo: "Fiebre de 2 semanas con escalofríos, sudoración profusa, palidez y bazo palpable en zona tropical: malaria",
    imagen: "flujogramas/fiebre-escalofrios-esplenomegalia-malaria.svg",
    alt: "Flujograma: Fiebre de 2 semanas con escalofríos, sudoración profusa, palidez y bazo palpable en zona tropical: malaria"
  },
  "CIR-047": {
    titulo: "Herida de laparotomía por bala que se deja abierta 5 días y luego se sutura: cierre por tercera intención (primario diferido)",
    imagen: "flujogramas/cicatrizacion-cierre-tercera-intencion.svg",
    alt: "Flujograma: Herida de laparotomía por bala que se deja abierta 5 días y luego se sutura: cierre por tercera intención (primario diferido)"
  },
  "SP-049": {
    titulo: "Buscar factores asociados a morir por COVID-19 y calcular el odds ratio: estudio de casos y controles",
    imagen: "flujogramas/medidas-asociacion-odds-ratio-casos-controles.svg",
    alt: "Flujograma: Buscar factores asociados a morir por COVID-19 y calcular el odds ratio: estudio de casos y controles"
  },
  "NRL-019": {
    titulo: "Adolescente con faringoamigdalitis previa, movimientos rápidos involuntarios de cara y manos y soplo mitral: corea de Sydenham",
    imagen: "flujogramas/corea-sydenham-criterios-jones.svg",
    alt: "Flujograma: Adolescente con faringoamigdalitis previa, movimientos rápidos involuntarios de cara y manos y soplo mitral: corea de Sydenham"
  },
  "HEM-015": {
    titulo: "Anemia macrocítica con neutrófilos hipersegmentados y gastritis atrófica: faltan las células parietales (anemia perniciosa)",
    imagen: "flujogramas/celulas-gastricas-anemia-perniciosa.svg",
    alt: "Flujograma: Anemia macrocítica con neutrófilos hipersegmentados y gastritis atrófica: faltan las células parietales (anemia perniciosa)"
  },
  "GIN-068": {
    titulo: "Gestante de 25 semanas con O'Sullivan de 150 mg/dL (tamizaje positivo): hacer la prueba de tolerancia oral a la glucosa",
    imagen: "flujogramas/test-osullivan-positivo-ptog.svg",
    alt: "Flujograma: Gestante de 25 semanas con O'Sullivan de 150 mg/dL (tamizaje positivo): hacer la prueba de tolerancia oral a la glucosa"
  },
  "PED-080": {
    titulo: "Recién nacido con fenilpiruvato alto en el tamizaje: fenilcetonuria, dieta con restricción de fenilalanina",
    imagen: "flujogramas/tamizaje-neonatal-fenilcetonuria-dieta.svg",
    alt: "Flujograma: Recién nacido con fenilpiruvato alto en el tamizaje: fenilcetonuria, dieta con restricción de fenilalanina"
  },
  "OFT-016": {
    titulo: "Hipertenso con epistaxis anterior profusa: el primer paso es la compresión digital firme de la nariz",
    imagen: "flujogramas/epistaxis-anterior-hipertenso-compresion.svg",
    alt: "Flujograma: Hipertenso con epistaxis anterior profusa: el primer paso es la compresión digital firme de la nariz"
  },
  "NRL-020": {
    titulo: "Anciano hipertenso con déficit focal súbito que se recupera solo en una hora y glucosa normal: ataque isquémico transitorio",
    imagen: "flujogramas/deficit-focal-transitorio-anciano-ait.svg",
    alt: "Flujograma: Anciano hipertenso con déficit focal súbito que se recupera solo en una hora y glucosa normal: ataque isquémico transitorio"
  },
  "HEM-016": {
    titulo: "Adulto con esplenomegalia, leucocitosis de 43 000 con todas las formas mieloides y trombocitosis: leucemia mieloide crónica",
    imagen: "flujogramas/leucocitosis-esplenomegalia-leucemia-mieloide-cronica.svg",
    alt: "Flujograma: Adulto con esplenomegalia, leucocitosis de 43 000 con todas las formas mieloides y trombocitosis: leucemia mieloide crónica"
  },
  "INF-030": {
    titulo: "Joven de Arequipa con edema palpebral, fiebre, adenopatía y hepatoesplenomegalia: Chagas agudo, vector Triatoma infestans",
    imagen: "flujogramas/vectores-peru-chagas-triatoma.svg",
    alt: "Flujograma: Joven de Arequipa con edema palpebral, fiebre, adenopatía y hepatoesplenomegalia: Chagas agudo, vector Triatoma infestans"
  },
  "GIN-069": {
    titulo: "Gestante con lupus y daño renal severo cuyo embarazo pone en riesgo su vida: el aborto se plantea como terapéutico",
    imagen: "flujogramas/aborto-terapeutico-lupus-nefropatia.svg",
    alt: "Flujograma: Gestante con lupus y daño renal severo cuyo embarazo pone en riesgo su vida: el aborto se plantea como terapéutico"
  },
  "INF-031": {
    titulo: "Paciente de la selva con fiebre alta, anemia severa, ictericia y postración: malaria grave por Plasmodium falciparum",
    imagen: "flujogramas/plasmodium-especies-falciparum-grave.svg",
    alt: "Flujograma: Paciente de la selva con fiebre alta, anemia severa, ictericia y postración: malaria grave por Plasmodium falciparum"
  },
  "PED-081": {
    titulo: "Niño con síndrome nefrótico y ascitis que hace fiebre, dolor abdominal y rebote: peritonitis primaria",
    imagen: "flujogramas/nefrotico-nino-dolor-abdominal-peritonitis-primaria.svg",
    alt: "Flujograma: Niño con síndrome nefrótico y ascitis que hace fiebre, dolor abdominal y rebote: peritonitis primaria"
  },
  "GIN-070": {
    titulo: "Gestante de 36 semanas con 3 cesáreas previas y sangrado indoloro con útero blando: placenta previa",
    imagen: "flujogramas/sangrado-indoloro-tercer-trimestre-placenta-previa.svg",
    alt: "Flujograma: Gestante de 36 semanas con 3 cesáreas previas y sangrado indoloro con útero blando: placenta previa"
  },
  "GIN-071": {
    titulo: "Mujer joven con mutación de BRCA1: predisposición sobre todo al cáncer de mama (y de ovario)",
    imagen: "flujogramas/cancer-hereditario-brca1-mama.svg",
    alt: "Flujograma: Mujer joven con mutación de BRCA1: predisposición sobre todo al cáncer de mama (y de ovario)"
  },
  "PED-082": {
    titulo: "Lactante de 8 meses, exprematuro, pálido e inapetente con hematíes microcíticos e hipocrómicos: anemia ferropénica",
    imagen: "flujogramas/lactante-prematuro-anemia-ferropenica.svg",
    alt: "Flujograma: Lactante de 8 meses, exprematuro, pálido e inapetente con hematíes microcíticos e hipocrómicos: anemia ferropénica"
  },
  "CIR-048": {
    titulo: "Chofer con dolor sacro, fiebre y bulto interglúteo inflamado con pus y pelos: absceso pilonidal",
    imagen: "flujogramas/masa-sacra-supurada-quiste-pilonidal.svg",
    alt: "Flujograma: Chofer con dolor sacro, fiebre y bulto interglúteo inflamado con pus y pelos: absceso pilonidal"
  },
  "CB-024": {
    titulo: "Adolescente inconsciente con miosis, sialorrea, relajación de esfínteres, dificultad respiratoria y fasciculaciones: carbamato",
    imagen: "flujogramas/sindrome-colinergico-carbamatos.svg",
    alt: "Flujograma: Adolescente inconsciente con miosis, sialorrea, relajación de esfínteres, dificultad respiratoria y fasciculaciones: carbamato"
  },
  "END-018": {
    titulo: "Joven con xantomas eruptivos, triglicéridos de 1000 mg/dL y suero lechoso: el mayor riesgo es la pancreatitis aguda",
    imagen: "flujogramas/hipertrigliceridemia-xantomas-eruptivos-pancreatitis.svg",
    alt: "Flujograma: Joven con xantomas eruptivos, triglicéridos de 1000 mg/dL y suero lechoso: el mayor riesgo es la pancreatitis aguda"
  },
  "GAS-024": {
    titulo: "Adulto mayor con baja de peso, ictericia marcada, prurito y vía biliar intrahepática dilatada: carcinoma de vías biliares",
    imagen: "flujogramas/ictericia-obstructiva-colangiocarcinoma.svg",
    alt: "Flujograma: Adulto mayor con baja de peso, ictericia marcada, prurito y vía biliar intrahepática dilatada: carcinoma de vías biliares"
  },
  "PED-083": {
    titulo: "Lactante de 7 meses con 3 días de catarro que pasa a dificultad respiratoria con sibilantes difusos e hiperinsuflación: bronquiolitis",
    imagen: "flujogramas/bronquiolitis-gravedad-manejo.svg",
    alt: "Flujograma: Lactante de 7 meses con 3 días de catarro que pasa a dificultad respiratoria con sibilantes difusos e hiperinsuflación: bronquiolitis"
  },
  "PED-084": {
    titulo: "Recién nacido a término de parto prolongado con líquido meconial, taquipnea, quejido y tirajes: síndrome de aspiración meconial",
    imagen: "flujogramas/rn-termino-liquido-meconial-aspiracion.svg",
    alt: "Flujograma: Recién nacido a término de parto prolongado con líquido meconial, taquipnea, quejido y tirajes: síndrome de aspiración meconial"
  },
  "GAS-025": {
    titulo: "Mujer joven que tras beber alcohol vomita con fuerza y luego vomita sangre: síndrome de Mallory-Weiss",
    imagen: "flujogramas/hematemesis-vomitos-alcohol-mallory-weiss.svg",
    alt: "Flujograma: Mujer joven que tras beber alcohol vomita con fuerza y luego vomita sangre: síndrome de Mallory-Weiss"
  },
  "PED-085": {
    titulo: "Niño que recoge fruta en un campo fumigado y presenta vómitos, disnea y temblores: lo primero es quitar la ropa y bañarlo",
    imagen: "flujogramas/nino-campo-fumigado-descontaminacion.svg",
    alt: "Flujograma: Niño que recoge fruta en un campo fumigado y presenta vómitos, disnea y temblores: lo primero es quitar la ropa y bañarlo"
  },
  "GIN-072": {
    titulo: "Mujer con histerectomía total por miomas, sin lesiones cervicales previas: ya no necesita Papanicolaou",
    imagen: "flujogramas/papanicolaou-histerectomia-total-benigna.svg",
    alt: "Flujograma: Mujer con histerectomía total por miomas, sin lesiones cervicales previas: ya no necesita Papanicolaou"
  },
  "CIR-049": {
    titulo: "Mujer de 70 años con cólicos y vómitos y un bulto femoral violáceo, irreductible y doloroso: hernia crural estrangulada",
    imagen: "flujogramas/masa-femoral-irreductible-hernia-crural-estrangulada.svg",
    alt: "Flujograma: Mujer de 70 años con cólicos y vómitos y un bulto femoral violáceo, irreductible y doloroso: hernia crural estrangulada"
  },
  "NEU-022": {
    titulo: "Posoperada de cadera con disnea súbita, dolor pleurítico, taquicardia e hipotensión: tromboembolismo pulmonar de alto riesgo",
    imagen: "flujogramas/disnea-subita-postoperatorio-cadera-tep.svg",
    alt: "Flujograma: Posoperada de cadera con disnea súbita, dolor pleurítico, taquicardia e hipotensión: tromboembolismo pulmonar de alto riesgo"
  },
  "END-019": {
    titulo: "Diabética de 10 años con retinopatía: para detectar la nefropatía temprana se mide la albuminuria (antes «microalbuminuria»)",
    imagen: "flujogramas/nefropatia-diabetica-albuminuria-cociente.svg",
    alt: "Flujograma: Diabética de 10 años con retinopatía: para detectar la nefropatía temprana se mide la albuminuria (antes «microalbuminuria»)"
  },
  "PED-086": {
    titulo: "Escolar contacto de TB en casa, asintomático, con Rx normal y PPD de 10 mm: infección latente, terapia preventiva",
    imagen: "flujogramas/contacto-tuberculosis-nino-terapia-preventiva.svg",
    alt: "Flujograma: Escolar contacto de TB en casa, asintomático, con Rx normal y PPD de 10 mm: infección latente, terapia preventiva"
  },
  "SP-050": {
    titulo: "Investigador al que un laboratorio le paga extra para que su estudio concluya que su fármaco es mejor: conflicto de intereses",
    imagen: "flujogramas/integridad-investigacion-conflicto-intereses.svg",
    alt: "Flujograma: Investigador al que un laboratorio le paga extra para que su estudio concluya que su fármaco es mejor: conflicto de intereses"
  },
  "INF-032": {
    titulo: "Fiebre, cefalea intensa y vómitos con LCR turbio, 12 000 células con neutrófilos, glucosa baja y proteínas altas: meningitis bacteriana",
    imagen: "flujogramas/lcr-turbio-neutrofilos-meningitis-bacteriana.svg",
    alt: "Flujograma: Fiebre, cefalea intensa y vómitos con LCR turbio, 12 000 células con neutrófilos, glucosa baja y proteínas altas: meningitis bacteriana"
  },
  "SP-051": {
    titulo: "En un I-2, el tema de estilo de vida que se prioriza con personas en riesgo o con diabetes tipo 2 es el sedentarismo",
    imagen: "flujogramas/promocion-salud-diabetes-sedentarismo.svg",
    alt: "Flujograma: En un I-2, el tema de estilo de vida que se prioriza con personas en riesgo o con diabetes tipo 2 es el sedentarismo"
  },
  "INF-033": {
    titulo: "Paciente con VIH y CD4 102 con convulsiones, hemiparesia y varias lesiones que captan en anillo: toxoplasmosis cerebral",
    imagen: "flujogramas/vih-lesiones-cerebrales-toxoplasmosis.svg",
    alt: "Flujograma: Paciente con VIH y CD4 102 con convulsiones, hemiparesia y varias lesiones que captan en anillo: toxoplasmosis cerebral"
  },
  "GIN-073": {
    titulo: "Enfermedad pélvica inflamatoria sin mejoría a las 72 horas de tratamiento oral: hospitalizar para antibiótico endovenoso",
    imagen: "flujogramas/epi-falla-ambulatoria-hospitalizar.svg",
    alt: "Flujograma: Enfermedad pélvica inflamatoria sin mejoría a las 72 horas de tratamiento oral: hospitalizar para antibiótico endovenoso"
  },
  "PED-087": {
    titulo: "Lactante de 4 meses con mala ganancia de peso, sudoración al lactar, polipnea, taquicardia y hepatomegalia: insuficiencia cardiaca congestiva",
    imagen: "flujogramas/lactante-sudoracion-hepatomegalia-icc.svg",
    alt: "Flujograma: Lactante de 4 meses con mala ganancia de peso, sudoración al lactar, polipnea, taquicardia y hepatomegalia: insuficiencia cardiaca congestiva"
  },
  "INF-034": {
    titulo: "Niña con diarrea clara y grasosa, epigastralgia, náuseas y baja de peso por tomar agua cruda, sin fiebre: Giardia lamblia",
    imagen: "flujogramas/diarrea-grasosa-agua-cruda-giardia.svg",
    alt: "Flujograma: Niña con diarrea clara y grasosa, epigastralgia, náuseas y baja de peso por tomar agua cruda, sin fiebre: Giardia lamblia"
  },
  "PED-088": {
    titulo: "Recién nacido que se atora, tose y se pone cianótico al lactar, con abdomen distendido y sonda que no pasa al estómago: atresia esofágica",
    imagen: "flujogramas/neonato-sonda-no-pasa-atresia-esofagica.svg",
    alt: "Flujograma: Recién nacido que se atora, tose y se pone cianótico al lactar, con abdomen distendido y sonda que no pasa al estómago: atresia esofágica"
  },
  "INF-035": {
    titulo: "Recién nacido de madre con VIH en tratamiento desde las 12 semanas: profilaxis con zidovudina",
    imagen: "flujogramas/recien-nacido-expuesto-vih-zidovudina.svg",
    alt: "Flujograma: Recién nacido de madre con VIH en tratamiento desde las 12 semanas: profilaxis con zidovudina"
  },
  "CIR-050": {
    titulo: "Herida torácica con hemotórax drenado que sigue sangrando 200 mL por hora durante 3 horas: toracotomía de urgencia",
    imagen: "flujogramas/hemotorax-drenaje-200-hora-toracotomia.svg",
    alt: "Flujograma: Herida torácica con hemotórax drenado que sigue sangrando 200 mL por hora durante 3 horas: toracotomía de urgencia"
  },
  "CAR-030": {
    titulo: "Fiebre tras un procedimiento dental, soplo mitral que cambia y manchas de Roth: endocarditis infecciosa",
    imagen: "flujogramas/fiebre-soplo-nuevo-roth-endocarditis.svg",
    alt: "Flujograma: Fiebre tras un procedimiento dental, soplo mitral que cambia y manchas de Roth: endocarditis infecciosa"
  },
  "PED-089": {
    titulo: "Niño de 3 años con anemia ferropénica (Hb 8): los alimentos que más ayudan son las carnes y vísceras (hierro hem)",
    imagen: "flujogramas/anemia-ferropenica-nino-alimentos-hierro-hemo.svg",
    alt: "Flujograma: Niño de 3 años con anemia ferropénica (Hb 8): los alimentos que más ayudan son las carnes y vísceras (hierro hem)"
  },
  "OFT-017": {
    titulo: "Adolescente con odinofagia, fiebre, trismus y úvula desviada al lado opuesto: absceso periamigdalino, punción y drenaje",
    imagen: "flujogramas/odinofagia-trismus-absceso-periamigdalino-drenaje.svg",
    alt: "Flujograma: Adolescente con odinofagia, fiebre, trismus y úvula desviada al lado opuesto: absceso periamigdalino, punción y drenaje"
  },
  "GAS-026": {
    titulo: "Cirrótico con hematemesis, melena e hipotensión con frialdad distal: lo primero es reponer volumen con cristaloides",
    imagen: "flujogramas/hematemesis-cirrotico-choque-cristaloides.svg",
    alt: "Flujograma: Cirrótico con hematemesis, melena e hipotensión con frialdad distal: lo primero es reponer volumen con cristaloides"
  },
  "TRA-013": {
    titulo: "Chofer con choque frontal y miembro inferior en aducción y rotación interna: luxación posterior de cadera",
    imagen: "flujogramas/impacto-frontal-aduccion-rotacion-interna-luxacion-posterior-cadera.svg",
    alt: "Flujograma: Chofer con choque frontal y miembro inferior en aducción y rotación interna: luxación posterior de cadera"
  },
  "NEF-031": {
    titulo: "Tras un choque hemorrágico, oligoanuria con creatinina 2,9 y sodio urinario de 45: necrosis tubular aguda",
    imagen: "flujogramas/oligoanuria-choque-hemorragico-necrosis-tubular-aguda.svg",
    alt: "Flujograma: Tras un choque hemorrágico, oligoanuria con creatinina 2,9 y sodio urinario de 45: necrosis tubular aguda"
  },
  "INF-036": {
    titulo: "Úlcera genital única, indurada e indolora tras una relación sin protección: chancro de sífilis primaria (Treponema pallidum)",
    imagen: "flujogramas/ulcera-genital-indolora-indurada-sifilis-primaria.svg",
    alt: "Flujograma: Úlcera genital única, indurada e indolora tras una relación sin protección: chancro de sífilis primaria (Treponema pallidum)"
  },
  "GAS-027": {
    titulo: "Cólico biliar seguido de ictericia, fiebre y escalofríos con bilirrubina directa y fosfatasa alcalina altas: colangitis aguda",
    imagen: "flujogramas/fiebre-ictericia-dolor-colangitis-charcot.svg",
    alt: "Flujograma: Cólico biliar seguido de ictericia, fiebre y escalofríos con bilirrubina directa y fosfatasa alcalina altas: colangitis aguda"
  },
  "SP-052": {
    titulo: "Que ómicron triplique los contagios por persona infectada respecto a Delta describe su transmisibilidad",
    imagen: "flujogramas/omicron-contagios-transmisibilidad-agente.svg",
    alt: "Flujograma: Que ómicron triplique los contagios por persona infectada respecto a Delta describe su transmisibilidad"
  },
  "GAS-028": {
    titulo: "Pólipos pediculados de 2 cm en el colon con sangrado: extirpación endoscópica y estudio histopatológico",
    imagen: "flujogramas/sangrado-rectal-polipo-pediculado-polipectomia.svg",
    alt: "Flujograma: Pólipos pediculados de 2 cm en el colon con sangrado: extirpación endoscópica y estudio histopatológico"
  },
  "CAR-031": {
    titulo: "PA alta en el consultorio (145/95) con MAPA normal: hipertensión de bata blanca",
    imagen: "flujogramas/hipertension-bata-blanca-mapa.svg",
    alt: "Flujograma: PA alta en el consultorio (145/95) con MAPA normal: hipertensión de bata blanca"
  },
  "CAR-032": {
    titulo: "Edema facial y «en esclavina» que pasa a los brazos, plétora e ingurgitación yugular: síndrome de vena cava superior",
    imagen: "flujogramas/edema-esclavina-sindrome-vena-cava-superior.svg",
    alt: "Flujograma: Edema facial y «en esclavina» que pasa a los brazos, plétora e ingurgitación yugular: síndrome de vena cava superior"
  },
  "GIN-074": {
    titulo: "Dolor pélvico que empeora con la regla, el sexo y la defecación y masa anexial fija «en vidrio esmerilado»: endometrioma",
    imagen: "flujogramas/dolor-pelvico-masa-anexial-endometrioma.svg",
    alt: "Flujograma: Dolor pélvico que empeora con la regla, el sexo y la defecación y masa anexial fija «en vidrio esmerilado»: endometrioma"
  },
  "END-020": {
    titulo: "Adolescente de 16 años sin menarquia, talla baja, cuello ancho, pezones separados y Tanner I: síndrome de Turner, pedir cariotipo",
    imagen: "flujogramas/amenorrea-primaria-talla-baja-turner-cariotipo.svg",
    alt: "Flujograma: Adolescente de 16 años sin menarquia, talla baja, cuello ancho, pezones separados y Tanner I: síndrome de Turner, pedir cariotipo"
  },
  "PED-090": {
    titulo: "Niña que ingirió una sobredosis de paracetamol hace 24 horas, con náuseas, anorexia y dolor en hipocondrio derecho: N-acetilcisteína",
    imagen: "flujogramas/sobredosis-paracetamol-nino-acetilcisteina.svg",
    alt: "Flujograma: Niña que ingirió una sobredosis de paracetamol hace 24 horas, con náuseas, anorexia y dolor en hipocondrio derecho: N-acetilcisteína"
  },
  "GIN-075": {
    titulo: "Gestante con urocultivo positivo a Lactobacillus (flora vaginal): contaminación, repetir el urocultivo",
    imagen: "flujogramas/gestante-urocultivo-lactobacillus-repetir.svg",
    alt: "Flujograma: Gestante con urocultivo positivo a Lactobacillus (flora vaginal): contaminación, repetir el urocultivo"
  },
  "REU-022": {
    titulo: "Habones pequeños muy pruriginosos que salen con el ejercicio o la ducha caliente y desaparecen en 2 horas: urticaria colinérgica",
    imagen: "flujogramas/ronchas-ejercicio-ducha-caliente-urticaria-colinergica.svg",
    alt: "Flujograma: Habones pequeños muy pruriginosos que salen con el ejercicio o la ducha caliente y desaparecen en 2 horas: urticaria colinérgica"
  },
  "NRL-021": {
    titulo: "Golpe frontal contra el parabrisas con Glasgow 12 y desorientación: TEC moderado, pedir tomografía cerebral",
    imagen: "flujogramas/trauma-craneal-glasgow-12-tomografia.svg",
    alt: "Flujograma: Golpe frontal contra el parabrisas con Glasgow 12 y desorientación: TEC moderado, pedir tomografía cerebral"
  },
  "NEF-032": {
    titulo: "Anciana con laxantes salinos, hiporreflexia, bradicardia, hipotensión, rubor y PR largo con QRS ancho: hipermagnesemia",
    imagen: "flujogramas/adulta-mayor-laxantes-salinos-hipermagnesemia.svg",
    alt: "Flujograma: Anciana con laxantes salinos, hiporreflexia, bradicardia, hipotensión, rubor y PR largo con QRS ancho: hipermagnesemia"
  },
  "GIN-076": {
    titulo: "Gestante de 24 semanas con dolor en FID, fiebre, rebote y leucocitosis con desviación izquierda: ecografía para confirmar apendicitis",
    imagen: "flujogramas/gestante-dolor-fid-apendicitis-ecografia.svg",
    alt: "Flujograma: Gestante de 24 semanas con dolor en FID, fiebre, rebote y leucocitosis con desviación izquierda: ecografía para confirmar apendicitis"
  },
  "SP-053": {
    titulo: "Eliminar un examen nacional que verifica la formación de los futuros médicos vulnera el derecho a una atención de calidad",
    imagen: "flujogramas/examen-unico-nacional-derecho-calidad-atencion.svg",
    alt: "Flujograma: Eliminar un examen nacional que verifica la formación de los futuros médicos vulnera el derecho a una atención de calidad"
  },
  "CB-025": {
    titulo: "Joven con colesterol 390, xantomas en el tendón de Aquiles y familiares con cifras parecidas: hipercolesterolemia familiar (receptor de LDL)",
    imagen: "flujogramas/hipercolesterolemia-familiar-xantomas-receptor-ldl.svg",
    alt: "Flujograma: Joven con colesterol 390, xantomas en el tendón de Aquiles y familiares con cifras parecidas: hipercolesterolemia familiar (receptor de LDL)"
  },
  "PED-091": {
    titulo: "Lactante de 2 semanas con vómitos en proyectil cada vez más frecuentes y deshidratación: estenosis pilórica con alcalosis metabólica hipoclorémica",
    imagen: "flujogramas/vomitos-proyectil-lactante-alcalosis-hipocloremica.svg",
    alt: "Flujograma: Lactante de 2 semanas con vómitos en proyectil cada vez más frecuentes y deshidratación: estenosis pilórica con alcalosis metabólica hipoclorémica"
  },
  "CIR-051": {
    titulo: "Laparotomía previa con dolor difuso, sin flatos, distensión y ruidos metálicos: obstrucción intestinal por bridas",
    imagen: "flujogramas/laparotomia-previa-obstruccion-intestinal-bridas.svg",
    alt: "Flujograma: Laparotomía previa con dolor difuso, sin flatos, distensión y ruidos metálicos: obstrucción intestinal por bridas"
  },
  "CAR-033": {
    titulo: "Lupus con disnea, hipotensión, taquicardia, pulso paradójico, yugulares ingurgitadas y QRS de bajo voltaje: taponamiento, pericardiocentesis",
    imagen: "flujogramas/lupus-pulso-paradojico-taponamiento-pericardiocentesis.svg",
    alt: "Flujograma: Lupus con disnea, hipotensión, taquicardia, pulso paradójico, yugulares ingurgitadas y QRS de bajo voltaje: taponamiento, pericardiocentesis"
  },
  "REU-023": {
    titulo: "Adolescente con manchas hipopigmentadas en tórax y espalda sin prurito: pitiriasis versicolor, sulfuro de selenio",
    imagen: "flujogramas/manchas-hipocromicas-tronco-pitiriasis-versicolor.svg",
    alt: "Flujograma: Adolescente con manchas hipopigmentadas en tórax y espalda sin prurito: pitiriasis versicolor, sulfuro de selenio"
  },
  "SP-054": {
    titulo: "Indicar fármacos con efectos adversos frecuentes y sin evidencia de beneficio contra la COVID-19 vulnera la no maleficencia",
    imagen: "flujogramas/farmacos-sin-evidencia-pandemia-no-maleficencia.svg",
    alt: "Flujograma: Indicar fármacos con efectos adversos frecuentes y sin evidencia de beneficio contra la COVID-19 vulnera la no maleficencia"
  },
  "CAR-034": {
    titulo: "Golpe precordial en un choque con dolor, sudoración fría y ruidos arrítmicos: ECG seriado (y troponina) para la contusión miocárdica",
    imagen: "flujogramas/trauma-precordial-arritmia-contusion-miocardica-ecg.svg",
    alt: "Flujograma: Golpe precordial en un choque con dolor, sudoración fría y ruidos arrítmicos: ECG seriado (y troponina) para la contusión miocárdica"
  },
  "TRA-014": {
    titulo: "Trauma de hombro con dolor a la abducción y lesión del manguito rotador: el músculo más afectado es el supraespinoso",
    imagen: "flujogramas/hombro-abduccion-dolorosa-supraespinoso.svg",
    alt: "Flujograma: Trauma de hombro con dolor a la abducción y lesión del manguito rotador: el músculo más afectado es el supraespinoso"
  },
  "GIN-077": {
    titulo: "Primigesta de 41 semanas con presentación de cara mentoposterior: no puede nacer por vía vaginal, cesárea",
    imagen: "flujogramas/presentacion-cara-mentoposterior-cesarea.svg",
    alt: "Flujograma: Primigesta de 41 semanas con presentación de cara mentoposterior: no puede nacer por vía vaginal, cesárea"
  },
  "GIN-078": {
    titulo: "Primer control a las 11 semanas por FUR con LCN de 11 semanas: la edad gestacional real se define con la ecografía transvaginal",
    imagen: "flujogramas/primer-control-edad-gestacional-ecografia-lcn.svg",
    alt: "Flujograma: Primer control a las 11 semanas por FUR con LCN de 11 semanas: la edad gestacional real se define con la ecografía transvaginal"
  },
  "GAS-029": {
    titulo: "Joven con pródromo de fiebre, náuseas y astenia que luego hace ictericia y dolor en hipocondrio derecho mientras cede la fiebre: hepatitis viral aguda",
    imagen: "flujogramas/prodromo-ictericia-hepatitis-viral-aguda.svg",
    alt: "Flujograma: Joven con pródromo de fiebre, náuseas y astenia que luego hace ictericia y dolor en hipocondrio derecho mientras cede la fiebre: hepatitis viral aguda"
  },
  "GIN-079": {
    titulo: "Gestante de 36 semanas con cefalea, escotomas, epigastralgia, PA 170/110 y proteinuria: preeclampsia con signos de severidad, sulfato de magnesio y terminar la gestación",
    imagen: "flujogramas/preeclampsia-severa-36-semanas-sulfato-magnesio.svg",
    alt: "Flujograma: Gestante de 36 semanas con cefalea, escotomas, epigastralgia, PA 170/110 y proteinuria: preeclampsia con signos de severidad, sulfato de magnesio y terminar la gestación"
  },
  "INF-037": {
    titulo: "Paciente de zona endémica con fiebre, dolor retroocular, dolor abdominal intenso y vómitos: probable dengue con signos de alarma",
    imagen: "flujogramas/fiebre-dolor-abdominal-vomitos-dengue-signos-alarma.svg",
    alt: "Flujograma: Paciente de zona endémica con fiebre, dolor retroocular, dolor abdominal intenso y vómitos: probable dengue con signos de alarma"
  },
  "NEU-023": {
    titulo: "Asmático en crisis con taquicardia, polipnea, tirajes y silencio auscultatorio: el silencio indica riesgo vital",
    imagen: "flujogramas/crisis-asmatica-torax-silente-gravedad.svg",
    alt: "Flujograma: Asmático en crisis con taquicardia, polipnea, tirajes y silencio auscultatorio: el silencio indica riesgo vital"
  },
  "GAS-030": {
    titulo: "Úlcera en la curvatura menor cerca del antro: se produce por el desequilibrio entre la agresión ácido-péptica y la defensa de la mucosa",
    imagen: "flujogramas/ulcera-gastrica-agresion-defensa-mucosa.svg",
    alt: "Flujograma: Úlcera en la curvatura menor cerca del antro: se produce por el desequilibrio entre la agresión ácido-péptica y la defensa de la mucosa"
  },
  "CIR-052": {
    titulo: "Escolar con anorexia, dolor periumbilical que pasa a la fosa ilíaca derecha y vómitos, sin diarrea: apendicitis aguda",
    imagen: "flujogramas/dolor-periumbilical-migratorio-alvarado-nino.svg",
    alt: "Flujograma: Escolar con anorexia, dolor periumbilical que pasa a la fosa ilíaca derecha y vómitos, sin diarrea: apendicitis aguda"
  },
  "INF-038": {
    titulo: "Strongyloides stercoralis en las heces: el tratamiento de elección es la ivermectina",
    imagen: "flujogramas/strongyloides-heces-ivermectina.svg",
    alt: "Flujograma: Strongyloides stercoralis en las heces: el tratamiento de elección es la ivermectina"
  },
  "NEU-024": {
    titulo: "EPOC con dolor torácico y disnea súbitos, SatO₂ 86 % e hiperresonancia en un hemitórax: neumotórax espontáneo secundario",
    imagen: "flujogramas/epoc-disnea-subita-hiperresonancia-neumotorax.svg",
    alt: "Flujograma: EPOC con dolor torácico y disnea súbitos, SatO₂ 86 % e hiperresonancia en un hemitórax: neumotórax espontáneo secundario"
  },
  "SP-055": {
    titulo: "Víctimas de violencia familiar detectadas en el tamizaje que necesitan atención integral especializada: Centro de Salud Mental Comunitario",
    imagen: "flujogramas/tamizaje-violencia-familiar-csmc.svg",
    alt: "Flujograma: Víctimas de violencia familiar detectadas en el tamizaje que necesitan atención integral especializada: Centro de Salud Mental Comunitario"
  },
  "GAS-031": {
    titulo: "Alcohólico con dolor epigástrico en cinturón de 7 días: para confirmar la pancreatitis aguda se pide lipasa (sigue alta más días que la amilasa)",
    imagen: "flujogramas/dolor-epigastrico-7-dias-lipasa.svg",
    alt: "Flujograma: Alcohólico con dolor epigástrico en cinturón de 7 días: para confirmar la pancreatitis aguda se pide lipasa (sigue alta más días que la amilasa)"
  },
  "CIR-053": {
    titulo: "Albañil con hernia inguinoescrotal izquierda blanda y reductible que aumenta con Valsalva: hernia inguinal indirecta",
    imagen: "flujogramas/tumoracion-inguinoescrotal-hernia-indirecta.svg",
    alt: "Flujograma: Albañil con hernia inguinoescrotal izquierda blanda y reductible que aumenta con Valsalva: hernia inguinal indirecta"
  },
  "INF-039": {
    titulo: "Fiebre, cefalea y mialgias 9 días después de visitar Iquitos, con petequias al tomar la presión: dengue (prueba del lazo positiva)",
    imagen: "flujogramas/fiebre-iquitos-prueba-lazo-dengue.svg",
    alt: "Flujograma: Fiebre, cefalea y mialgias 9 días después de visitar Iquitos, con petequias al tomar la presión: dengue (prueba del lazo positiva)"
  },
  "OFT-018": {
    titulo: "Adolescente con 1 mes de cefalea, tos nocturna, rinorrea y goteo posnasal purulento: sinusitis subaguda",
    imagen: "flujogramas/cefalea-tos-nocturna-rinosinusitis-subaguda.svg",
    alt: "Flujograma: Adolescente con 1 mes de cefalea, tos nocturna, rinorrea y goteo posnasal purulento: sinusitis subaguda"
  },
  "REU-024": {
    titulo: "Paciente con VIH con dolor urente y luego vesículas en un dermatoma del tórax, Tzanck con células gigantes: herpes zóster",
    imagen: "flujogramas/vesiculas-dermatoma-vih-herpes-zoster.svg",
    alt: "Flujograma: Paciente con VIH con dolor urente y luego vesículas en un dermatoma del tórax, Tzanck con células gigantes: herpes zóster"
  },
  "GIN-080": {
    titulo: "Puérpera de 3 días poscesárea con fiebre de 38,5 °C, útero doloroso y secreción purulenta: endometritis, iniciar antibióticos",
    imagen: "flujogramas/fiebre-poscesarea-utero-doloroso-endometritis.svg",
    alt: "Flujograma: Puérpera de 3 días poscesárea con fiebre de 38,5 °C, útero doloroso y secreción purulenta: endometritis, iniciar antibióticos"
  },
  "SP-056": {
    titulo: "Para elaborar el plan operativo anual de un establecimiento I-4 se empieza por identificar los problemas sanitarios",
    imagen: "flujogramas/serumista-plan-operativo-anual-problemas.svg",
    alt: "Flujograma: Para elaborar el plan operativo anual de un establecimiento I-4 se empieza por identificar los problemas sanitarios"
  },
  "PSI-015": {
    titulo: "Adolescente con IMC 15 que se provoca vómitos: alcalosis metabólica hipoclorémica",
    imagen: "flujogramas/vomitos-autoprovocados-adolescente-alcalosis.svg",
    alt: "Flujograma: Adolescente con IMC 15 que se provoca vómitos: alcalosis metabólica hipoclorémica"
  },
  "PED-092": {
    titulo: "Recién nacido con cianosis a las 3 horas que no mejora con oxígeno: cardiopatía cianótica (de las opciones, la estenosis pulmonar)",
    imagen: "flujogramas/cianosis-neonatal-no-mejora-oxigeno.svg",
    alt: "Flujograma: Recién nacido con cianosis a las 3 horas que no mejora con oxígeno: cardiopatía cianótica (de las opciones, la estenosis pulmonar)"
  },
  "PSI-016": {
    titulo: "Médico con 3 meses de aislamiento, ideas delirantes de grandeza y persecución y desaseo: esquizofrenia (tipo paranoide)",
    imagen: "flujogramas/delirios-grandeza-persecucion-esquizofrenia.svg",
    alt: "Flujograma: Médico con 3 meses de aislamiento, ideas delirantes de grandeza y persecución y desaseo: esquizofrenia (tipo paranoide)"
  },
  "OFT-019": {
    titulo: "Midriasis bilateral arreactiva con fotofobia tras un examen de retina, sin otros signos: midriasis farmacológica",
    imagen: "flujogramas/midriasis-bilateral-tras-fondo-de-ojo.svg",
    alt: "Flujograma: Midriasis bilateral arreactiva con fotofobia tras un examen de retina, sin otros signos: midriasis farmacológica"
  },
  "GAS-032": {
    titulo: "Dolor urente en el epigastrio 5-6 horas después de comer que lo despierta de noche, sin baja de peso ni disfagia: úlcera péptica (duodenal)",
    imagen: "flujogramas/dolor-epigastrico-nocturno-ulcera-duodenal.svg",
    alt: "Flujograma: Dolor urente en el epigastrio 5-6 horas después de comer que lo despierta de noche, sin baja de peso ni disfagia: úlcera péptica (duodenal)"
  },
  "PED-093": {
    titulo: "Recién nacido de 36 semanas con dificultad respiratoria leve e hipotermia, madre con RPM > 18 horas: neumonía neonatal (sepsis precoz)",
    imagen: "flujogramas/rpm-prolongada-hipotermia-neumonia-neonatal.svg",
    alt: "Flujograma: Recién nacido de 36 semanas con dificultad respiratoria leve e hipotermia, madre con RPM > 18 horas: neumonía neonatal (sepsis precoz)"
  },
  "NEU-025": {
    titulo: "Gestante asintomática con PPD positivo y Rx normal cuyo esposo tiene TB bacilífera: terapia preventiva con isoniacida",
    imagen: "flujogramas/gestante-contacto-tb-ppd-positivo-isoniacida.svg",
    alt: "Flujograma: Gestante asintomática con PPD positivo y Rx normal cuyo esposo tiene TB bacilífera: terapia preventiva con isoniacida"
  },
  "END-021": {
    titulo: "Paciente con colitis ulcerosa grave con T3 baja y T4 libre y TSH normales: síndrome del eutiroideo enfermo",
    imagen: "flujogramas/colitis-grave-t3-baja-eutiroideo-enfermo.svg",
    alt: "Flujograma: Paciente con colitis ulcerosa grave con T3 baja y T4 libre y TSH normales: síndrome del eutiroideo enfermo"
  },
  "GIN-081": {
    titulo: "Amenorrea de 9 semanas con cólico y sangrado escaso, cuello cerrado y estable: amenaza de aborto, pedir ecografía transvaginal",
    imagen: "flujogramas/amenorrea-9-semanas-sangrado-escaso-ecografia.svg",
    alt: "Flujograma: Amenorrea de 9 semanas con cólico y sangrado escaso, cuello cerrado y estable: amenaza de aborto, pedir ecografía transvaginal"
  },
  "NRL-022": {
    titulo: "TEC con cefalea, vómitos explosivos, papiledema y Glasgow 10 que desciende: hipertensión endocraneana, solución salina hipertónica",
    imagen: "flujogramas/tec-edema-papila-glasgow-descenso-salino-hipertonico.svg",
    alt: "Flujograma: TEC con cefalea, vómitos explosivos, papiledema y Glasgow 10 que desciende: hipertensión endocraneana, solución salina hipertónica"
  },
  "GIN-082": {
    titulo: "Mujer joven con ciclos irregulares, dolor súbito en FID, hipotensión, Blumberg (+) y masa anexial: pedir β-hCG (sospecha de ectópico roto)",
    imagen: "flujogramas/dolor-fid-masa-anexial-hipotension-bhcg.svg",
    alt: "Flujograma: Mujer joven con ciclos irregulares, dolor súbito en FID, hipotensión, Blumberg (+) y masa anexial: pedir β-hCG (sospecha de ectópico roto)"
  },
  "CB-026": {
    titulo: "Estudiante que tomó 4 bebidas energizantes con agitación, HTA, taquicardia arrítmica y alteración del sensorio: sobredosis de cafeína",
    imagen: "flujogramas/bebidas-energizantes-agitacion-toxindrome-simpatico.svg",
    alt: "Flujograma: Estudiante que tomó 4 bebidas energizantes con agitación, HTA, taquicardia arrítmica y alteración del sensorio: sobredosis de cafeína"
  },
  "OFT-020": {
    titulo: "Niño con una semilla en el conducto auditivo: extracción instrumentada (no irrigar, la semilla se hincha)",
    imagen: "flujogramas/semilla-conducto-auditivo-extraccion.svg",
    alt: "Flujograma: Niño con una semilla en el conducto auditivo: extracción instrumentada (no irrigar, la semilla se hincha)"
  },
  "CAR-035": {
    titulo: "Paciente en hemodiálisis por catéter con fiebre, lesiones de Janeway y soplo nuevo: lo primero son los hemocultivos",
    imagen: "flujogramas/dialisis-cateter-fiebre-janeway-endocarditis.svg",
    alt: "Flujograma: Paciente en hemodiálisis por catéter con fiebre, lesiones de Janeway y soplo nuevo: lo primero son los hemocultivos"
  },
  "INF-040": {
    titulo: "Contacto del personal de salud con un caso de meningococcemia (púrpura, rigidez de nuca): quimioprofilaxis con rifampicina",
    imagen: "flujogramas/meningococcemia-contacto-personal-salud-rifampicina.svg",
    alt: "Flujograma: Contacto del personal de salud con un caso de meningococcemia (púrpura, rigidez de nuca): quimioprofilaxis con rifampicina"
  },
  "CB-027": {
    titulo: "Víctima de incendio intubada con PaO₂ 400, saturación del gasómetro 99 % pero lactato 6 e hipotensión: hiperoxemia con hipoxia tisular (monóxido de carbono)",
    imagen: "flujogramas/incendio-sotano-monoxido-po2-alta-hipoxia-tisular.svg",
    alt: "Flujograma: Víctima de incendio intubada con PaO₂ 400, saturación del gasómetro 99 % pero lactato 6 e hipotensión: hiperoxemia con hipoxia tisular (monóxido de carbono)"
  },
  "TRA-015": {
    titulo: "Futbolista con esguince del tobillo por inversión y dolor lateral: se lesiona el complejo lateral (peroneoastragalino anterior y calcaneoperoneo)",
    imagen: "flujogramas/futbolista-esguince-inversion-calcaneoperoneo.svg",
    alt: "Flujograma: Futbolista con esguince del tobillo por inversión y dolor lateral: se lesiona el complejo lateral (peroneoastragalino anterior y calcaneoperoneo)"
  },
  "GIN-083": {
    titulo: "Gestante a término sin control prenatal con sangrado continuo en un centro I-2: no hacer tacto vaginal y referir a mayor complejidad",
    imagen: "flujogramas/sangrado-tercer-trimestre-establecimiento-i2-referencia.svg",
    alt: "Flujograma: Gestante a término sin control prenatal con sangrado continuo en un centro I-2: no hacer tacto vaginal y referir a mayor complejidad"
  },
  "PED-094": {
    titulo: "Lactante con catarro que pasa a tos en accesos que termina en vómito y cianosis, y queda bien entre accesos: tos ferina",
    imagen: "flujogramas/tos-paroxistica-vomito-cianosis-tos-ferina.svg",
    alt: "Flujograma: Lactante con catarro que pasa a tos en accesos que termina en vómito y cianosis, y queda bien entre accesos: tos ferina"
  },
  "NEF-033": {
    titulo: "El umbral clásico de urocultivo positivo en la muestra de chorro medio es 100 000 UFC/mL de un solo germen",
    imagen: "flujogramas/urocultivo-umbral-100000-ufc.svg",
    alt: "Flujograma: El umbral clásico de urocultivo positivo en la muestra de chorro medio es 100 000 UFC/mL de un solo germen"
  },
  "NEF-034": {
    titulo: "Cólico renal con hematuria, cálculo radiopaco, calcio y fósforo normales y urocultivo negativo: cálculo de oxalato de calcio",
    imagen: "flujogramas/calculo-radiopaco-calcio-normal-oxalato.svg",
    alt: "Flujograma: Cólico renal con hematuria, cálculo radiopaco, calcio y fósforo normales y urocultivo negativo: cálculo de oxalato de calcio"
  },
  "NEU-026": {
    titulo: "Paciente hospitalizado por ACV que al 8.º día hace consolidación basal derecha: neumonía intrahospitalaria por bacilos gramnegativos",
    imagen: "flujogramas/acv-hospitalizado-dia-8-neumonia-gramnegativos.svg",
    alt: "Flujograma: Paciente hospitalizado por ACV que al 8.º día hace consolidación basal derecha: neumonía intrahospitalaria por bacilos gramnegativos"
  },
  "GIN-084": {
    titulo: "Amenorrea secundaria con β-hCG, FSH, LH, prolactina y TSH normales que menstrúa con progesterona: causa anovulatoria",
    imagen: "flujogramas/amenorrea-secundaria-test-progesterona-anovulacion.svg",
    alt: "Flujograma: Amenorrea secundaria con β-hCG, FSH, LH, prolactina y TSH normales que menstrúa con progesterona: causa anovulatoria"
  },
  "PED-095": {
    titulo: "Neonato de 18 horas con pulsos femorales más débiles que los del brazo derecho: coartación de aorta",
    imagen: "flujogramas/neonato-pulsos-femorales-debiles-coartacion.svg",
    alt: "Flujograma: Neonato de 18 horas con pulsos femorales más débiles que los del brazo derecho: coartación de aorta"
  },
  "PED-096": {
    titulo: "Recién nacido pletórico, letárgico y con mala succión con hematocrito de 70 %: policitemia sintomática, exanguinotransfusión parcial",
    imagen: "flujogramas/neonato-pletorico-hto-70-exanguinotransfusion.svg",
    alt: "Flujograma: Recién nacido pletórico, letárgico y con mala succión con hematocrito de 70 %: policitemia sintomática, exanguinotransfusión parcial"
  },
  "END-022": {
    titulo: "Mujer joven con baja de peso, intolerancia al calor, temblor, taquicardia y amenorrea con TSH baja y T4 libre alta: hipertiroidismo, metimazol",
    imagen: "flujogramas/hipertiroidismo-mujer-joven-metimazol.svg",
    alt: "Flujograma: Mujer joven con baja de peso, intolerancia al calor, temblor, taquicardia y amenorrea con TSH baja y T4 libre alta: hipertiroidismo, metimazol"
  },
  "REU-025": {
    titulo: "Nódulos dolorosos axilares que supuran y dejan cicatrices: hidradenitis supurativa",
    imagen: "flujogramas/abscesos-axilares-trayectos-hidradenitis.svg",
    alt: "Flujograma: Nódulos dolorosos axilares que supuran y dejan cicatrices: hidradenitis supurativa"
  },
  "PED-097": {
    titulo: "Prematuro de 34 semanas que nace flácido y sin respirar: primero calor, secar, posicionar la vía aérea y aspirar si hace falta",
    imagen: "flujogramas/prematuro-flacido-apnea-pasos-iniciales.svg",
    alt: "Flujograma: Prematuro de 34 semanas que nace flácido y sin respirar: primero calor, secar, posicionar la vía aérea y aspirar si hace falta"
  },
  "GIN-085": {
    titulo: "Preeclámptica con sulfato de magnesio que tiene diuresis de 10 mL/h y FR 10: toxicidad por magnesio, suspender la infusión",
    imagen: "flujogramas/sulfato-magnesio-oliguria-bradipnea-suspender.svg",
    alt: "Flujograma: Preeclámptica con sulfato de magnesio que tiene diuresis de 10 mL/h y FR 10: toxicidad por magnesio, suspender la infusión"
  },
  "INF-041": {
    titulo: "Niña con prurito perianal y vulvar de predominio nocturno e irritabilidad: oxiuros (Enterobius vermicularis)",
    imagen: "flujogramas/nina-prurito-vulvar-perianal-nocturno-oxiuros.svg",
    alt: "Flujograma: Niña con prurito perianal y vulvar de predominio nocturno e irritabilidad: oxiuros (Enterobius vermicularis)"
  },
  "GIN-086": {
    titulo: "Puérpera de parto domiciliario que no expulsa la placenta en 1 hora y sangra mucho: extracción manual de la placenta",
    imagen: "flujogramas/parto-domiciliario-placenta-retenida-sangrado.svg",
    alt: "Flujograma: Puérpera de parto domiciliario que no expulsa la placenta en 1 hora y sangra mucho: extracción manual de la placenta"
  },
  "GAS-033": {
    titulo: "Pancreatitis aguda con PA 65/40, sopor y TC con páncreas agrandado y líquido: pancreatitis grave en choque, lo primero es reponer volumen",
    imagen: "flujogramas/pancreatitis-grave-choque-fluidoterapia.svg",
    alt: "Flujograma: Pancreatitis aguda con PA 65/40, sopor y TC con páncreas agrandado y líquido: pancreatitis grave en choque, lo primero es reponer volumen"
  },
  "NEF-035": {
    titulo: "Joven con hematuria, edema e HTA 2 semanas después de una infección respiratoria, con cilindros hemáticos: glomerulonefritis aguda postinfecciosa",
    imagen: "flujogramas/infeccion-respiratoria-previa-hematuria-gn-postinfecciosa.svg",
    alt: "Flujograma: Joven con hematuria, edema e HTA 2 semanas después de una infección respiratoria, con cilindros hemáticos: glomerulonefritis aguda postinfecciosa"
  },
  "SP-057": {
    titulo: "En el ciclo de la violencia, la fase de pequeños episodios y roces permanentes es la acumulación de tensión",
    imagen: "flujogramas/ciclo-violencia-pareja-acumulacion-tension.svg",
    alt: "Flujograma: En el ciclo de la violencia, la fase de pequeños episodios y roces permanentes es la acumulación de tensión"
  },
  "CB-028": {
    titulo: "Licor adulterado con coma, convulsiones y acidosis metabólica grave (pH 7,0, HCO₃ 5): intoxicación por metanol, soporte y hemodiálisis urgente",
    imagen: "flujogramas/licor-adulterado-convulsiones-acidosis-metanol.svg",
    alt: "Flujograma: Licor adulterado con coma, convulsiones y acidosis metabólica grave (pH 7,0, HCO₃ 5): intoxicación por metanol, soporte y hemodiálisis urgente"
  },
  "SP-058": {
    titulo: "Crear espacios de deliberación, concertación y vigilancia de compromisos con todos los actores es participación ciudadana",
    imagen: "flujogramas/diresa-espacios-concertacion-participacion-ciudadana.svg",
    alt: "Flujograma: Crear espacios de deliberación, concertación y vigilancia de compromisos con todos los actores es participación ciudadana"
  },
  "INF-042": {
    titulo: "Jardinero que se pinchó con una rosa y tiene una úlcera indolora con nódulos que siguen el trayecto linfático: esporotricosis",
    imagen: "flujogramas/jardinero-espina-rosa-nodulos-linfaticos-esporotricosis.svg",
    alt: "Flujograma: Jardinero que se pinchó con una rosa y tiene una úlcera indolora con nódulos que siguen el trayecto linfático: esporotricosis"
  },
  "GIN-087": {
    titulo: "Puérpera con VIH en TAR que no quiere embarazarse: DIU (los métodos combinados con estrógeno no se usan en el puerperio temprano)",
    imagen: "flujogramas/puerpera-vih-tar-anticoncepcion-diu.svg",
    alt: "Flujograma: Puérpera con VIH en TAR que no quiere embarazarse: DIU (los métodos combinados con estrógeno no se usan en el puerperio temprano)"
  },
  "PED-098": {
    titulo: "Lactante de comunidad nativa muy adelgazado, piel flácida y arrugada, cara de viejo, cabello quebradizo y emaciación de glúteos y muslos: marasmo",
    imagen: "flujogramas/lactante-emaciado-piel-flacida-marasmo.svg",
    alt: "Flujograma: Lactante de comunidad nativa muy adelgazado, piel flácida y arrugada, cara de viejo, cabello quebradizo y emaciación de glúteos y muslos: marasmo"
  },
  "PED-099": {
    titulo: "Niño con 2 días de diarrea con moco sin sangre, fiebre y dolor, sin vómitos: tratamiento inicial con hidratación oral",
    imagen: "flujogramas/diarrea-con-moco-sin-deshidratacion-plan-a.svg",
    alt: "Flujograma: Niño con 2 días de diarrea con moco sin sangre, fiebre y dolor, sin vómitos: tratamiento inicial con hidratación oral"
  },
  "HEM-017": {
    titulo: "Mujer de 58 años con sangrado sin antecedentes, TTPa prolongado que no corrige con la mezcla: inhibidor de un factor (hemofilia adquirida)",
    imagen: "flujogramas/ttpa-prolongado-prueba-mezcla-no-corrige.svg",
    alt: "Flujograma: Mujer de 58 años con sangrado sin antecedentes, TTPa prolongado que no corrige con la mezcla: inhibidor de un factor (hemofilia adquirida)"
  },
  "HEM-018": {
    titulo: "Mujer que toma anticonceptivos combinados y fuma con edema y dolor en la pierna: trombosis por aumento de la síntesis de factores de coagulación",
    imagen: "flujogramas/anticonceptivos-combinados-tvp-factores-coagulacion.svg",
    alt: "Flujograma: Mujer que toma anticonceptivos combinados y fuma con edema y dolor en la pierna: trombosis por aumento de la síntesis de factores de coagulación"
  },
  "NEF-036": {
    titulo: "Varón joven con fiebre, disuria, polaquiuria, retardo miccional, dolor perineal y próstata dolorosa: prostatitis aguda",
    imagen: "flujogramas/fiebre-disuria-dolor-perineal-prostatitis.svg",
    alt: "Flujograma: Varón joven con fiebre, disuria, polaquiuria, retardo miccional, dolor perineal y próstata dolorosa: prostatitis aguda"
  },
  "INF-043": {
    titulo: "Mujer con dengue previo hace un mes que ahora tiene choque, epistaxis y petequias: dengue grave por reinfección, por aumento de mediadores vasoactivos",
    imagen: "flujogramas/reinfeccion-dengue-choque-mediadores-vasoactivos.svg",
    alt: "Flujograma: Mujer con dengue previo hace un mes que ahora tiene choque, epistaxis y petequias: dengue grave por reinfección, por aumento de mediadores vasoactivos"
  },
  "NRL-023": {
    titulo: "Anciano con TEC leve hace 3 semanas que luego tiene cefalea y deterioro cognitivo progresivo: hematoma subdural crónico",
    imagen: "flujogramas/anciano-tec-leve-semanas-deterioro-subdural-cronico.svg",
    alt: "Flujograma: Anciano con TEC leve hace 3 semanas que luego tiene cefalea y deterioro cognitivo progresivo: hematoma subdural crónico"
  },
  "GIN-088": {
    titulo: "Sangrado rojo rutilante tras parto instrumentado de un bebé de 4100 g con útero bien contraído: lesión del canal del parto",
    imagen: "flujogramas/parto-instrumentado-macrosomico-utero-contraido-desgarro.svg",
    alt: "Flujograma: Sangrado rojo rutilante tras parto instrumentado de un bebé de 4100 g con útero bien contraído: lesión del canal del parto"
  },
  "NRL-024": {
    titulo: "Cefalea súbita en trueno con vómitos, convulsión, rigidez de nuca, Glasgow 10 y midriasis con ptosis derecha: hemorragia subaracnoidea (aneurisma)",
    imagen: "flujogramas/cefalea-trueno-anisocoria-ptosis-hsa.svg",
    alt: "Flujograma: Cefalea súbita en trueno con vómitos, convulsión, rigidez de nuca, Glasgow 10 y midriasis con ptosis derecha: hemorragia subaracnoidea (aneurisma)"
  },
  "END-023": {
    titulo: "Joven con crisis de cefalea, sudoración, palpitaciones y palidez, HTA resistente y metanefrinas altas: feocromocitoma",
    imagen: "flujogramas/crisis-adrenergicas-hta-refractaria-metanefrinas.svg",
    alt: "Flujograma: Joven con crisis de cefalea, sudoración, palpitaciones y palidez, HTA resistente y metanefrinas altas: feocromocitoma"
  },
  "CIR-054": {
    titulo: "Trauma abdominal cerrado sin peritonitis ni otra indicación de laparotomía: lo que decide diferir la cirugía es la estabilidad hemodinámica",
    imagen: "flujogramas/trauma-abdominal-cerrado-sin-peritonitis-estable.svg",
    alt: "Flujograma: Trauma abdominal cerrado sin peritonitis ni otra indicación de laparotomía: lo que decide diferir la cirugía es la estabilidad hemodinámica"
  },
  "END-024": {
    titulo: "Mujer con calor, nerviosismo, polimenorrea, caída del cabello, taquicardia y piel caliente: pedir TSH y T4 libre",
    imagen: "flujogramas/calor-nerviosismo-polimenorrea-tsh-t4l.svg",
    alt: "Flujograma: Mujer con calor, nerviosismo, polimenorrea, caída del cabello, taquicardia y piel caliente: pedir TSH y T4 libre"
  },
  "HEM-019": {
    titulo: "Niño de 4 años con cansancio, febrícula, dolor óseo nocturno, palidez, petequias y hepatoesplenomegalia con citopenias: leucemia linfoblástica aguda",
    imagen: "flujogramas/nino-dolor-oseo-nocturno-petequias-lla.svg",
    alt: "Flujograma: Niño de 4 años con cansancio, febrícula, dolor óseo nocturno, palidez, petequias y hepatoesplenomegalia con citopenias: leucemia linfoblástica aguda"
  },
  "NRL-025": {
    titulo: "Anciana con cefalea y confusión progresivas, apraxia del vestido y hemianopsia con masa parietal en anillo, necrosis central y edema: glioblastoma",
    imagen: "flujogramas/masa-realce-anillo-necrosis-glioblastoma.svg",
    alt: "Flujograma: Anciana con cefalea y confusión progresivas, apraxia del vestido y hemianopsia con masa parietal en anillo, necrosis central y edema: glioblastoma"
  },
  "REU-026": {
    titulo: "Debilidad muscular proximal con eritema violáceo de párpados (heliotropo) y eritema en el escote: dermatomiositis",
    imagen: "flujogramas/debilidad-proximal-heliotropo-dermatomiositis.svg",
    alt: "Flujograma: Debilidad muscular proximal con eritema violáceo de párpados (heliotropo) y eritema en el escote: dermatomiositis"
  },
  "SP-059": {
    titulo: "Casos de COVID-19 leves que siguen apareciendo dentro de la incidencia esperada pese a la vacunación: comportamiento endémico",
    imagen: "flujogramas/covid-casos-esperados-vacunados-endemia.svg",
    alt: "Flujograma: Casos de COVID-19 leves que siguen apareciendo dentro de la incidencia esperada pese a la vacunación: comportamiento endémico"
  },
  "GIN-089": {
    titulo: "Gestante con vómitos persistentes que hace confusión, ataxia y movimientos oculares anormales: encefalopatía de Wernicke, dar tiamina",
    imagen: "flujogramas/hiperemesis-confusion-ataxia-nistagmo-tiamina.svg",
    alt: "Flujograma: Gestante con vómitos persistentes que hace confusión, ataxia y movimientos oculares anormales: encefalopatía de Wernicke, dar tiamina"
  },
  "END-025": {
    titulo: "Mujer con fatiga, aumento de peso, estreñimiento, piel seca, reflejo aquíleo lento, TSH 52 y T4L baja: hipotiroidismo primario, levotiroxina",
    imagen: "flujogramas/hipotiroidismo-tsh-52-levotiroxina.svg",
    alt: "Flujograma: Mujer con fatiga, aumento de peso, estreñimiento, piel seca, reflejo aquíleo lento, TSH 52 y T4L baja: hipotiroidismo primario, levotiroxina"
  },
  "END-026": {
    titulo: "Joven con TB previa, síncopes por hipotensión ortostática, hiperpigmentación, hiponatremia e hiperpotasemia: insuficiencia suprarrenal primaria (Addison)",
    imagen: "flujogramas/sincope-ortostatico-hiperpigmentacion-hiperkalemia-addison.svg",
    alt: "Flujograma: Joven con TB previa, síncopes por hipotensión ortostática, hiperpigmentación, hiponatremia e hiperpotasemia: insuficiencia suprarrenal primaria (Addison)"
  },
  "SP-060": {
    titulo: "La disciplina que gestiona la promoción, prevención y control de la salud de los trabajadores es la medicina ocupacional",
    imagen: "flujogramas/salud-trabajadores-medicina-ocupacional.svg",
    alt: "Flujograma: La disciplina que gestiona la promoción, prevención y control de la salud de los trabajadores es la medicina ocupacional"
  },
  "CAR-036": {
    titulo: "Paro cardiaco presenciado en un centro comercial con DEA disponible: lo inmediato es desfibrilar con el DEA",
    imagen: "flujogramas/centro-comercial-paro-dea-desfibrilacion.svg",
    alt: "Flujograma: Paro cardiaco presenciado en un centro comercial con DEA disponible: lo inmediato es desfibrilar con el DEA"
  },
  "SP-061": {
    titulo: "Capacitar al personal para respetar las culturas y adecuar los servicios con pertinencia cultural es el enfoque intercultural",
    imagen: "flujogramas/pertinencia-cultural-servicios-interculturalidad.svg",
    alt: "Flujograma: Capacitar al personal para respetar las culturas y adecuar los servicios con pertinencia cultural es el enfoque intercultural"
  },
  "PED-100": {
    titulo: "En la recién nacida con ano imperforado, el defecto más frecuente es la fístula rectovestibular",
    imagen: "flujogramas/ano-imperforado-nina-fistula-rectovestibular.svg",
    alt: "Flujograma: En la recién nacida con ano imperforado, el defecto más frecuente es la fístula rectovestibular"
  },
  "PED-101": {
    titulo: "Prematuro de 32 semanas con letargia, apneas, bradicardia, fontanela llena y perímetro cefálico que crece: hemorragia intraventricular",
    imagen: "flujogramas/prematuro-32-semanas-letargia-fontanela-llena-hiv.svg",
    alt: "Flujograma: Prematuro de 32 semanas con letargia, apneas, bradicardia, fontanela llena y perímetro cefálico que crece: hemorragia intraventricular"
  },
  "GAS-034": {
    titulo: "Adolescente con pródromo, ictericia y hepatomegalia: la IgM anti-VHA confirma la hepatitis A aguda",
    imagen: "flujogramas/adolescente-ictericia-igm-anti-vha.svg",
    alt: "Flujograma: Adolescente con pródromo, ictericia y hepatomegalia: la IgM anti-VHA confirma la hepatitis A aguda"
  },
  "OFT-021": {
    titulo: "Lúpica en tratamiento crónico con hidroxicloroquina con pérdida visual progresiva y maculopatía bilateral: toxicidad por hidroxicloroquina",
    imagen: "flujogramas/lupus-hidroxicloroquina-maculopatia-bilateral.svg",
    alt: "Flujograma: Lúpica en tratamiento crónico con hidroxicloroquina con pérdida visual progresiva y maculopatía bilateral: toxicidad por hidroxicloroquina"
  },
  "INF-044": {
    titulo: "Joven con 3 semanas de fiebre, sudoración nocturna, baja de peso, ascitis y abdomen «en tablero de ajedrez» con exudado linfocítico: peritonitis tuberculosa",
    imagen: "flujogramas/ascitis-exudado-linfocitos-peritonitis-tuberculosa.svg",
    alt: "Flujograma: Joven con 3 semanas de fiebre, sudoración nocturna, baja de peso, ascitis y abdomen «en tablero de ajedrez» con exudado linfocítico: peritonitis tuberculosa"
  },
  "GIN-090": {
    titulo: "Sangrado a las 8 semanas con útero grande para la edad y ecografía «en tormenta de nieve»: mola hidatiforme, evacuación por aspiración",
    imagen: "flujogramas/tormenta-de-nieve-utero-grande-mola-evacuacion.svg",
    alt: "Flujograma: Sangrado a las 8 semanas con útero grande para la edad y ecografía «en tormenta de nieve»: mola hidatiforme, evacuación por aspiración"
  },
  "TRA-016": {
    titulo: "Para el tamizaje de la displasia del desarrollo de la cadera en el recién nacido, el estudio de elección es la ecografía",
    imagen: "flujogramas/recien-nacido-cadera-ecografia-graf.svg",
    alt: "Flujograma: Para el tamizaje de la displasia del desarrollo de la cadera en el recién nacido, el estudio de elección es la ecografía"
  },
  "SP-062": {
    titulo: "Usar racionalmente los recursos disponibles para alcanzar metas predeterminadas es el principio de eficiencia",
    imagen: "flujogramas/asis-uso-racional-recursos-eficiencia.svg",
    alt: "Flujograma: Usar racionalmente los recursos disponibles para alcanzar metas predeterminadas es el principio de eficiencia"
  },
  "PED-102": {
    titulo: "Neonato de 9 días con ictericia hasta el abdomen (Kramer 3), succión débil, poca orina, hipoactivo y bradicárdico: sepsis neonatal tardía, referir",
    imagen: "flujogramas/neonato-9-dias-ictericia-oliguria-hipoactivo-sepsis-tardia.svg",
    alt: "Flujograma: Neonato de 9 días con ictericia hasta el abdomen (Kramer 3), succión débil, poca orina, hipoactivo y bradicárdico: sepsis neonatal tardía, referir"
  },
  "PSI-017": {
    titulo: "Varón con 6 semanas de tristeza, vacío, insomnio, falta de energía, poca atención e ideas suicidas recurrentes: episodio depresivo",
    imagen: "flujogramas/tristeza-seis-semanas-ideas-suicidas-episodio-depresivo.svg",
    alt: "Flujograma: Varón con 6 semanas de tristeza, vacío, insomnio, falta de energía, poca atención e ideas suicidas recurrentes: episodio depresivo"
  },
  "CB-029": {
    titulo: "La principal función del hígado con los xenobióticos es transformarlos, empezando por la hidroxilación enzimática (fase I, citocromo P450)",
    imagen: "flujogramas/higado-xenobioticos-fase-1-hidroxilacion.svg",
    alt: "Flujograma: La principal función del hígado con los xenobióticos es transformarlos, empezando por la hidroxilación enzimática (fase I, citocromo P450)"
  },
  "CIR-055": {
    titulo: "Adulto mayor con baja de peso, hematoquecia y obstrucción intestinal baja con masa rectal y fiebre: cáncer obstructivo, colostomía",
    imagen: "flujogramas/anciano-obstruccion-masa-rectal-colostomia.svg",
    alt: "Flujograma: Adulto mayor con baja de peso, hematoquecia y obstrucción intestinal baja con masa rectal y fiebre: cáncer obstructivo, colostomía"
  },
  "CAR-037": {
    titulo: "Mujer de Arequipa rural con insuficiencia cardiaca, fibrilación auricular, cardiomegalia, megaesófago y megacolon: enfermedad de Chagas crónica",
    imagen: "flujogramas/arequipa-cardiomegalia-megaesofago-megacolon-chagas.svg",
    alt: "Flujograma: Mujer de Arequipa rural con insuficiencia cardiaca, fibrilación auricular, cardiomegalia, megaesófago y megacolon: enfermedad de Chagas crónica"
  },
  "CIR-056": {
    titulo: "Motociclista sin casco con Glasgow 8, SatO₂ 90 % e hipotensión: lo primero es asegurar la vía aérea con intubación orotraqueal",
    imagen: "flujogramas/motociclista-sin-casco-glasgow-8-intubacion.svg",
    alt: "Flujograma: Motociclista sin casco con Glasgow 8, SatO₂ 90 % e hipotensión: lo primero es asegurar la vía aérea con intubación orotraqueal"
  },
  "NRL-026": {
    titulo: "Deterioro cognitivo con fallas de atención, alucinaciones visuales bien formadas y parkinsonismo: demencia con cuerpos de Lewy",
    imagen: "flujogramas/deterioro-atencional-alucinaciones-parkinsonismo-lewy.svg",
    alt: "Flujograma: Deterioro cognitivo con fallas de atención, alucinaciones visuales bien formadas y parkinsonismo: demencia con cuerpos de Lewy"
  },
  "OFT-022": {
    titulo: "Golpe en la oreja hace 2 horas con aumento de volumen fluctuante del pabellón: hematoma subpericóndrico, drenar",
    imagen: "flujogramas/golpe-pabellon-auricular-hematoma-subpericondrico.svg",
    alt: "Flujograma: Golpe en la oreja hace 2 horas con aumento de volumen fluctuante del pabellón: hematoma subpericóndrico, drenar"
  },
  "PED-103": {
    titulo: "Niño con edema palpebral y de piernas y proteinuria: el síndrome nefrótico se confirma con proteinuria ≥ 40 mg/m²/h",
    imagen: "flujogramas/nino-edema-proteinuria-rango-nefrotico-pediatrico.svg",
    alt: "Flujograma: Niño con edema palpebral y de piernas y proteinuria: el síndrome nefrótico se confirma con proteinuria ≥ 40 mg/m²/h"
  },
  "HEM-020": {
    titulo: "Al 8.º día de heparina no fraccionada, las plaquetas caen a 27 000 con petequias: trombocitopenia inducida por heparina",
    imagen: "flujogramas/heparina-dia-8-plaquetas-27000-trombocitopenia.svg",
    alt: "Flujograma: Al 8.º día de heparina no fraccionada, las plaquetas caen a 27 000 con petequias: trombocitopenia inducida por heparina"
  },
  "GAS-035": {
    titulo: "Joven con ictericia leve que aparece con el ayuno, bilirrubina indirecta alta y todo lo demás normal (sin hemólisis): síndrome de Gilbert",
    imagen: "flujogramas/ictericia-ayuno-bilirrubina-indirecta-gilbert.svg",
    alt: "Flujograma: Joven con ictericia leve que aparece con el ayuno, bilirrubina indirecta alta y todo lo demás normal (sin hemólisis): síndrome de Gilbert"
  },
  "HEM-021": {
    titulo: "Niña de 3 años con petequias y gingivorragia 2 semanas después de un resfrío, plaquetas 8500 y el resto normal: trombocitopenia inmune primaria",
    imagen: "flujogramas/nina-petequias-gingivorragia-postviral-pti.svg",
    alt: "Flujograma: Niña de 3 años con petequias y gingivorragia 2 semanas después de un resfrío, plaquetas 8500 y el resto normal: trombocitopenia inmune primaria"
  },
  "CB-030": {
    titulo: "Hombre tratado por disfunción eréctil con cefalea, rubor y visión azulada transitoria: efecto del sildenafilo",
    imagen: "flujogramas/disfuncion-erectil-vision-azulada-sildenafilo.svg",
    alt: "Flujograma: Hombre tratado por disfunción eréctil con cefalea, rubor y visión azulada transitoria: efecto del sildenafilo"
  },
  "GIN-091": {
    titulo: "Gestante de 32 semanas con contracciones, cuello de 35 mm y fibronectina negativa: falso trabajo de parto, manejo expectante",
    imagen: "flujogramas/32-semanas-contracciones-cervix-35-fibronectina-negativa.svg",
    alt: "Flujograma: Gestante de 32 semanas con contracciones, cuello de 35 mm y fibronectina negativa: falso trabajo de parto, manejo expectante"
  },
  "INF-045": {
    titulo: "Paciente con TB en esquema 1 que al mes pierde agudeza visual y no distingue el verde: neuritis óptica por etambutol",
    imagen: "flujogramas/esquema-1-vision-colores-verde-etambutol.svg",
    alt: "Flujograma: Paciente con TB en esquema 1 que al mes pierde agudeza visual y no distingue el verde: neuritis óptica por etambutol"
  },
  "CAR-038": {
    titulo: "Soplo diastólico decreciente en el borde esternal izquierdo, pulso saltón y soplo mesodiastólico mitral de Austin Flint: insuficiencia aórtica",
    imagen: "flujogramas/pulso-salton-soplo-diastolico-austin-flint.svg",
    alt: "Flujograma: Soplo diastólico decreciente en el borde esternal izquierdo, pulso saltón y soplo mesodiastólico mitral de Austin Flint: insuficiencia aórtica"
  },
  "PED-104": {
    titulo: "Neonato de 20 días con ictericia, heces blanquecinas, orina oscura y bilirrubina directa alta: atresia de vías biliares",
    imagen: "flujogramas/rn-20-dias-acolia-bilirrubina-directa-atresia.svg",
    alt: "Flujograma: Neonato de 20 días con ictericia, heces blanquecinas, orina oscura y bilirrubina directa alta: atresia de vías biliares"
  },
  "GIN-092": {
    titulo: "Las fibras musculares entrecruzadas del útero (ligaduras vivientes de Pinard) controlan el sangrado después del parto",
    imagen: "flujogramas/pinard-miometrio-hemostasia-posparto.svg",
    alt: "Flujograma: Las fibras musculares entrecruzadas del útero (ligaduras vivientes de Pinard) controlan el sangrado después del parto"
  },
  "INF-046": {
    titulo: "Joven sexualmente activo con monoartritis de rodilla y diplococos gramnegativos en el líquido: artritis gonocócica, ceftriaxona EV",
    imagen: "flujogramas/rodilla-diplococos-gramnegativos-artritis-gonococica.svg",
    alt: "Flujograma: Joven sexualmente activo con monoartritis de rodilla y diplococos gramnegativos en el líquido: artritis gonocócica, ceftriaxona EV"
  },
  "INF-047": {
    titulo: "Paciente con VIH y CD4 < 200 con nódulos rojo vinosos que no palidecen en piel y boca: sarcoma de Kaposi",
    imagen: "flujogramas/vih-cd4-bajo-nodulos-violaceos-kaposi.svg",
    alt: "Flujograma: Paciente con VIH y CD4 < 200 con nódulos rojo vinosos que no palidecen en piel y boca: sarcoma de Kaposi"
  },
  "CB-031": {
    titulo: "Adulto mayor que se automedicó «para el COVID» y presenta QT largo y taquicardia ventricular: azitromicina",
    imagen: "flujogramas/automedicacion-covid-qt-largo-azitromicina.svg",
    alt: "Flujograma: Adulto mayor que se automedicó «para el COVID» y presenta QT largo y taquicardia ventricular: azitromicina"
  },
  "NEU-027": {
    titulo: "Trabajador expuesto 30 años al asbesto con disnea, placas pleurales y fibrosis reticular en panal: asbestosis, cuerpos ferruginosos en la biopsia",
    imagen: "flujogramas/asbesto-30-anos-panal-cuerpos-ferruginosos.svg",
    alt: "Flujograma: Trabajador expuesto 30 años al asbesto con disnea, placas pleurales y fibrosis reticular en panal: asbestosis, cuerpos ferruginosos en la biopsia"
  },
  "NEF-037": {
    titulo: "Diabético con HTA, filtración de 45 mL/min y albuminuria de 1 g/día: el fármaco para bajar la proteinuria es un IECA (o ARA II)",
    imagen: "flujogramas/diabetico-albuminuria-1g-ieca.svg",
    alt: "Flujograma: Diabético con HTA, filtración de 45 mL/min y albuminuria de 1 g/día: el fármaco para bajar la proteinuria es un IECA (o ARA II)"
  },
  "SP-063": {
    titulo: "Educar a las gestantes para mejorar la lactancia materna es la acción de la Carta de Ottawa «desarrollar habilidades personales»",
    imagen: "flujogramas/lactancia-exclusiva-comunicacion-educativa-habilidades.svg",
    alt: "Flujograma: Educar a las gestantes para mejorar la lactancia materna es la acción de la Carta de Ottawa «desarrollar habilidades personales»"
  },
  "INF-048": {
    titulo: "Joven con diarrea acuosa profusa «en agua de arroz», vómitos, calambres y deshidratación, sin sangre ni inflamación: cólera",
    imagen: "flujogramas/diarrea-agua-de-arroz-calambres-colera.svg",
    alt: "Flujograma: Joven con diarrea acuosa profusa «en agua de arroz», vómitos, calambres y deshidratación, sin sangre ni inflamación: cólera"
  },
  "SP-064": {
    titulo: "Encuestar a todos los alumnos una sola vez sobre sus características y conocimientos: estudio transversal",
    imagen: "flujogramas/encuesta-escolares-embarazo-estudio-transversal.svg",
    alt: "Flujograma: Encuestar a todos los alumnos una sola vez sobre sus características y conocimientos: estudio transversal"
  },
  "OFT-023": {
    titulo: "La forma más frecuente de glaucoma es el primario de ángulo abierto",
    imagen: "flujogramas/glaucoma-mas-frecuente-angulo-abierto.svg",
    alt: "Flujograma: La forma más frecuente de glaucoma es el primario de ángulo abierto"
  },
  "GIN-093": {
    titulo: "Vasa previa diagnosticada en la ecografía: cesárea programada entre las 34 y 35 semanas",
    imagen: "flujogramas/vasa-previa-cesarea-34-35-semanas.svg",
    alt: "Flujograma: Vasa previa diagnosticada en la ecografía: cesárea programada entre las 34 y 35 semanas"
  },
  "PED-105": {
    titulo: "Niño que ingirió lejía hace 20 minutos con estridor, sialorrea y SatO₂ 91 %: lo primero es asegurar la vía aérea (intubación)",
    imagen: "flujogramas/lejia-estridor-sialorrea-intubacion.svg",
    alt: "Flujograma: Niño que ingirió lejía hace 20 minutos con estridor, sialorrea y SatO₂ 91 %: lo primero es asegurar la vía aérea (intubación)"
  },
  "PSI-018": {
    titulo: "Joven con 4 meses de ideas de daño, voces que le advierten y descuido del aseo: psicosis",
    imagen: "flujogramas/voces-le-quieren-hacer-dano-psicosis.svg",
    alt: "Flujograma: Joven con 4 meses de ideas de daño, voces que le advierten y descuido del aseo: psicosis"
  },
  "NEF-038": {
    titulo: "Adulto mayor con síntomas prostáticos de años, gran residuo vesical, anemia y creatinina 3,5: uropatía obstructiva, tratamiento definitivo RTU",
    imagen: "flujogramas/hbp-residuo-vesical-creatinina-rtu.svg",
    alt: "Flujograma: Adulto mayor con síntomas prostáticos de años, gran residuo vesical, anemia y creatinina 3,5: uropatía obstructiva, tratamiento definitivo RTU"
  },
  "NEF-039": {
    titulo: "Pielonefritis con cálculo enclavado e hidronefrosis que no mejora con antibióticos e hipotensión: derivar la orina (catéter doble J o nefrostomía)",
    imagen: "flujogramas/calculo-enclavado-fiebre-hipotension-doble-j.svg",
    alt: "Flujograma: Pielonefritis con cálculo enclavado e hidronefrosis que no mejora con antibióticos e hipotensión: derivar la orina (catéter doble J o nefrostomía)"
  },
  "INF-049": {
    titulo: "Médico vacunado contra la fiebre amarilla hace 2 años que irá a zona endémica: no necesita revacunarse (una dosis protege de por vida)",
    imagen: "flujogramas/serumista-selva-vacuna-fiebre-amarilla-dosis-unica.svg",
    alt: "Flujograma: Médico vacunado contra la fiebre amarilla hace 2 años que irá a zona endémica: no necesita revacunarse (una dosis protege de por vida)"
  },
  "CAR-039": {
    titulo: "Dolor opresivo de 30 minutos con ST elevado 5 mm en la cara anterolateral y troponina alta, estable: angioplastia coronaria primaria",
    imagen: "flujogramas/st-elevado-anterolateral-angioplastia-primaria.svg",
    alt: "Flujograma: Dolor opresivo de 30 minutos con ST elevado 5 mm en la cara anterolateral y troponina alta, estable: angioplastia coronaria primaria"
  },
  "GIN-094": {
    titulo: "Gestante de 8 semanas con náuseas y vómitos leves y estable: además de las medidas dietéticas, doxilamina + piridoxina",
    imagen: "flujogramas/nauseas-8-semanas-doxilamina-piridoxina.svg",
    alt: "Flujograma: Gestante de 8 semanas con náuseas y vómitos leves y estable: además de las medidas dietéticas, doxilamina + piridoxina"
  },
  "PED-106": {
    titulo: "Lactante con cianosis al llanto, corazón en bota y eco con CIV, aorta cabalgante y estenosis subpulmonar: tetralogía de Fallot",
    imagen: "flujogramas/cianosis-corazon-en-bota-tetralogia-fallot.svg",
    alt: "Flujograma: Lactante con cianosis al llanto, corazón en bota y eco con CIV, aorta cabalgante y estenosis subpulmonar: tetralogía de Fallot"
  },
  "NRL-027": {
    titulo: "En la hidrocefalia aguda, la medida inicial de soporte es elevar la cabecera a 30° (mientras se prepara el drenaje)",
    imagen: "flujogramas/hidrocefalia-aguda-cabecera-30-grados.svg",
    alt: "Flujograma: En la hidrocefalia aguda, la medida inicial de soporte es elevar la cabecera a 30° (mientras se prepara el drenaje)"
  },
  "GIN-095": {
    titulo: "Gestante con epilepsia: el fármaco de elección por su seguridad fetal es el levetiracetam (o lamotrigina)",
    imagen: "flujogramas/epilepsia-gestante-levetiracetam.svg",
    alt: "Flujograma: Gestante con epilepsia: el fármaco de elección por su seguridad fetal es el levetiracetam (o lamotrigina)"
  },
  "CAR-040": {
    titulo: "Infarto de 24 horas con PA 90/60, ingurgitación yugular y crepitantes en ambas bases: choque cardiogénico, inotrópicos",
    imagen: "flujogramas/infarto-24-horas-hipotension-crepitantes-inotropicos.svg",
    alt: "Flujograma: Infarto de 24 horas con PA 90/60, ingurgitación yugular y crepitantes en ambas bases: choque cardiogénico, inotrópicos"
  },
  "SP-065": {
    titulo: "Para un plan educativo de prevención del VIH en adolescentes, el ámbito priorizado es el colegio",
    imagen: "flujogramas/vih-adolescentes-comunicacion-educativa-colegio.svg",
    alt: "Flujograma: Para un plan educativo de prevención del VIH en adolescentes, el ámbito priorizado es el colegio"
  },
  "GAS-036": {
    titulo: "Joven que se automedicó con paracetamol y presenta ictericia, encefalopatía con asterixis, INR 6 e hipoglucemia: falla hepática aguda, N-acetilcisteína",
    imagen: "flujogramas/paracetamol-inr-6-asterixis-n-acetilcisteina.svg",
    alt: "Flujograma: Joven que se automedicó con paracetamol y presenta ictericia, encefalopatía con asterixis, INR 6 e hipoglucemia: falla hepática aguda, N-acetilcisteína"
  },
  "PED-107": {
    titulo: "Escolar con fiebre, exudado amigdalino y petequias en el paladar: faringitis estreptocócica, amoxicilina por 10 días",
    imagen: "flujogramas/exudado-petequias-paladar-amoxicilina-10-dias.svg",
    alt: "Flujograma: Escolar con fiebre, exudado amigdalino y petequias en el paladar: faringitis estreptocócica, amoxicilina por 10 días"
  },
  "INF-050": {
    titulo: "Joven con 2 semanas de cefalea y meningismo, LCR con linfocitos, proteínas altas y glucosa baja, y Rx miliar: meningitis tuberculosa",
    imagen: "flujogramas/lcr-linfocitos-glucosa-baja-miliar-meningitis-tb.svg",
    alt: "Flujograma: Joven con 2 semanas de cefalea y meningismo, LCR con linfocitos, proteínas altas y glucosa baja, y Rx miliar: meningitis tuberculosa"
  },
  "PED-108": {
    titulo: "La vacuna contra la influenza no se aplica antes de los 6 meses de edad: es su contraindicación por edad",
    imagen: "flujogramas/vacuna-influenza-contraindicacion-menor-6-meses.svg",
    alt: "Flujograma: La vacuna contra la influenza no se aplica antes de los 6 meses de edad: es su contraindicación por edad"
  },
  "PSI-019": {
    titulo: "Anciano que recibe haloperidol EV a dosis altas con fiebre, rigidez, diaforesis, inestabilidad y CPK alta: síndrome neuroléptico maligno",
    imagen: "flujogramas/haloperidol-rigidez-fiebre-cpk-neuroleptico-maligno.svg",
    alt: "Flujograma: Anciano que recibe haloperidol EV a dosis altas con fiebre, rigidez, diaforesis, inestabilidad y CPK alta: síndrome neuroléptico maligno"
  },
  "GIN-096": {
    titulo: "Mujer joven con sangrado menstrual abundante y endometrio de 24 mm en la ecografía: biopsia de endometrio",
    imagen: "flujogramas/sangrado-uterino-endometrio-24-mm-biopsia.svg",
    alt: "Flujograma: Mujer joven con sangrado menstrual abundante y endometrio de 24 mm en la ecografía: biopsia de endometrio"
  },
  "SP-066": {
    titulo: "Si los niños a vacunar están en la escuela, se coordina con el sector educación para vacunar allí: coordinación intersectorial",
    imagen: "flujogramas/vph-escolares-coordinacion-intersectorial.svg",
    alt: "Flujograma: Si los niños a vacunar están en la escuela, se coordina con el sector educación para vacunar allí: coordinación intersectorial"
  },
  "GIN-097": {
    titulo: "Gestante con diabetes previa al embarazo y macrosomía en partos anteriores: el tratamiento es insulina",
    imagen: "flujogramas/diabetes-pregestacional-macrosomia-insulina.svg",
    alt: "Flujograma: Gestante con diabetes previa al embarazo y macrosomía en partos anteriores: el tratamiento es insulina"
  },
  "TRA-017": {
    titulo: "Niño con escoliosis y ángulo de Cobb de 30°: escoliosis moderada",
    imagen: "flujogramas/angulo-cobb-30-escoliosis-moderada.svg",
    alt: "Flujograma: Niño con escoliosis y ángulo de Cobb de 30°: escoliosis moderada"
  },
  "GIN-098": {
    titulo: "Mujer asintomática con prolapso de la pared anterior en estadio II (Ba −1): ejercicios de Kegel",
    imagen: "flujogramas/popq-ba-menos-1-asintomatica-kegel.svg",
    alt: "Flujograma: Mujer asintomática con prolapso de la pared anterior en estadio II (Ba −1): ejercicios de Kegel"
  },
  "SP-067": {
    titulo: "Paciente lúcido que pide que las decisiones se traten con su hijo: respetarlo es el principio de autonomía",
    imagen: "flujogramas/paciente-lucido-delega-decision-hijo-autonomia.svg",
    alt: "Flujograma: Paciente lúcido que pide que las decisiones se traten con su hijo: respetarlo es el principio de autonomía"
  },
  "SP-068": {
    titulo: "Anemia infantil de 55 % en un distrito y 5 % en otro: diferencia injusta y evitable, falta de equidad",
    imagen: "flujogramas/anemia-55-vs-5-distritos-equidad.svg",
    alt: "Flujograma: Anemia infantil de 55 % en un distrito y 5 % en otro: diferencia injusta y evitable, falta de equidad"
  },
  "PED-109": {
    titulo: "Lactante de 6 meses con sospecha de pielonefritis: la orina para cultivo se obtiene por sondaje vesical",
    imagen: "flujogramas/lactante-pielonefritis-urocultivo-sondaje.svg",
    alt: "Flujograma: Lactante de 6 meses con sospecha de pielonefritis: la orina para cultivo se obtiene por sondaje vesical"
  },
  "TRA-018": {
    titulo: "Lactante de 2 meses, niña, de parto podálico, con Ortolani positivo: displasia de cadera, arnés de Pavlik",
    imagen: "flujogramas/ortolani-positivo-2-meses-arnes-pavlik.svg",
    alt: "Flujograma: Lactante de 2 meses, niña, de parto podálico, con Ortolani positivo: displasia de cadera, arnés de Pavlik"
  },
  "INF-051": {
    titulo: "Niño de la sierra con convulsiones y quiste con escólex más calcificaciones en la imagen: neurocisticercosis",
    imagen: "flujogramas/ayacucho-convulsion-quiste-escolex-neurocisticercosis.svg",
    alt: "Flujograma: Niño de la sierra con convulsiones y quiste con escólex más calcificaciones en la imagen: neurocisticercosis"
  },
  "GAS-037": {
    titulo: "Cirrótico con ascitis, fiebre, dolor abdominal y encefalopatía, con neutrófilos altos en el líquido ascítico: PBE, ceftriaxona",
    imagen: "flujogramas/ascitis-pmn-7000-peritonitis-espontanea-ceftriaxona.svg",
    alt: "Flujograma: Cirrótico con ascitis, fiebre, dolor abdominal y encefalopatía, con neutrófilos altos en el líquido ascítico: PBE, ceftriaxona"
  },
  "SP-069": {
    titulo: "Si nadie muere de la enfermedad y siguen apareciendo casos nuevos, la prevalencia aumenta",
    imagen: "flujogramas/letalidad-cero-casos-nuevos-prevalencia-aumenta.svg",
    alt: "Flujograma: Si nadie muere de la enfermedad y siguen apareciendo casos nuevos, la prevalencia aumenta"
  },
  "NRL-028": {
    titulo: "Cefalea súbita intensa con vómitos, rigidez de nuca y cefalea centinela previa: sospecha de hemorragia subaracnoidea, TC sin contraste",
    imagen: "flujogramas/cefalea-subita-rigidez-nuca-tem-cerebral.svg",
    alt: "Flujograma: Cefalea súbita intensa con vómitos, rigidez de nuca y cefalea centinela previa: sospecha de hemorragia subaracnoidea, TC sin contraste"
  },
  "CAR-041": {
    titulo: "Hipertenso con insuficiencia cardíaca, galope y retinopatía grado IV: cardiopatía hipertensiva",
    imagen: "flujogramas/hta-galope-retinopatia-iv-cardiopatia-hipertensiva.svg",
    alt: "Flujograma: Hipertenso con insuficiencia cardíaca, galope y retinopatía grado IV: cardiopatía hipertensiva"
  },
  "GIN-099": {
    titulo: "Gestante que fuma 15 cigarrillos diarios: el riesgo neonatal principal es la restricción del crecimiento intrauterino",
    imagen: "flujogramas/gestante-fuma-15-cigarrillos-rciu.svg",
    alt: "Flujograma: Gestante que fuma 15 cigarrillos diarios: el riesgo neonatal principal es la restricción del crecimiento intrauterino"
  },
  "GIN-100": {
    titulo: "Dolor en la FID días después de instrumentar el útero, con dolor a la movilización cervical y anexial: salpingitis",
    imagen: "flujogramas/hidrosonografia-dolor-anexial-salpingitis.svg",
    alt: "Flujograma: Dolor en la FID días después de instrumentar el útero, con dolor a la movilización cervical y anexial: salpingitis"
  },
  "SP-070": {
    titulo: "Campaña de detección de VIH en jóvenes: diagnóstico precoz, es prevención secundaria",
    imagen: "flujogramas/campana-deteccion-vih-prevencion-secundaria.svg",
    alt: "Flujograma: Campaña de detección de VIH en jóvenes: diagnóstico precoz, es prevención secundaria"
  },
  "CIR-057": {
    titulo: "Hernia inguinal de un año que se vuelve irreductible, dolorosa y con distensión abdominal: hernia inguinal complicada",
    imagen: "flujogramas/tumoracion-inguinal-irreductible-distension-hernia-complicada.svg",
    alt: "Flujograma: Hernia inguinal de un año que se vuelve irreductible, dolorosa y con distensión abdominal: hernia inguinal complicada"
  },
  "INF-052": {
    titulo: "Estudiante de medicina que quiere saber si está protegido contra la hepatitis B: pedir anti-HBs",
    imagen: "flujogramas/estudiante-medicina-anti-hbs-inmunidad.svg",
    alt: "Flujograma: Estudiante de medicina que quiere saber si está protegido contra la hepatitis B: pedir anti-HBs"
  },
  "CAR-042": {
    titulo: "Persona que se desploma en la calle: lo primero es comprobar que la escena sea segura",
    imagen: "flujogramas/persona-se-desploma-calle-escena-segura.svg",
    alt: "Flujograma: Persona que se desploma en la calle: lo primero es comprobar que la escena sea segura"
  },
  "GAS-038": {
    titulo: "Niño con ictericia, urticaria y púrpura 7 semanas después de una transfusión: hepatitis B aguda",
    imagen: "flujogramas/nino-transfusion-7-semanas-ictericia-hepatitis-b.svg",
    alt: "Flujograma: Niño con ictericia, urticaria y púrpura 7 semanas después de una transfusión: hepatitis B aguda"
  },
  "NRL-029": {
    titulo: "Hipertenso en coma súbito con Glasgow 4, respiración irregular y pupilas puntiformes: hemorragia en la protuberancia",
    imagen: "flujogramas/hipertenso-coma-pupilas-puntiformes-protuberancia.svg",
    alt: "Flujograma: Hipertenso en coma súbito con Glasgow 4, respiración irregular y pupilas puntiformes: hemorragia en la protuberancia"
  },
  "END-027": {
    titulo: "Mujer con amenorrea y que no pudo dar de lactar tras una hemorragia posparto con choque: síndrome de Sheehan",
    imagen: "flujogramas/hemorragia-posparto-no-lacto-amenorrea-sheehan.svg",
    alt: "Flujograma: Mujer con amenorrea y que no pudo dar de lactar tras una hemorragia posparto con choque: síndrome de Sheehan"
  },
  "INF-053": {
    titulo: "Vecino de la ribera de un río con fiebre súbita, dolor de pantorrillas, ictericia y sufusión conjuntival: leptospirosis",
    imagen: "flujogramas/ribera-rimac-mialgia-pantorrillas-sufusion-leptospirosis.svg",
    alt: "Flujograma: Vecino de la ribera de un río con fiebre súbita, dolor de pantorrillas, ictericia y sufusión conjuntival: leptospirosis"
  },
  "SP-071": {
    titulo: "Colegio urbano con 35 % de escolares con sobrepeso y 8 % con obesidad: el factor modificable principal es el sedentarismo",
    imagen: "flujogramas/escolares-imc-mayor-25-sedentarismo.svg",
    alt: "Flujograma: Colegio urbano con 35 % de escolares con sobrepeso y 8 % con obesidad: el factor modificable principal es el sedentarismo"
  },
  "CB-032": {
    titulo: "Para canalizar la vena femoral se palpa el pulso de la arteria: la vena está justo medial a ella",
    imagen: "flujogramas/acceso-vena-femoral-medial-arteria.svg",
    alt: "Flujograma: Para canalizar la vena femoral se palpa el pulso de la arteria: la vena está justo medial a ella"
  },
  "CIR-058": {
    titulo: "Trauma de tórax con choque, murmullo ausente y matidez en la mitad inferior derecha: hemotórax, tubo de drenaje torácico",
    imagen: "flujogramas/trauma-timon-matidez-hemotorax-tubo-toracico.svg",
    alt: "Flujograma: Trauma de tórax con choque, murmullo ausente y matidez en la mitad inferior derecha: hemotórax, tubo de drenaje torácico"
  },
  "GAS-039": {
    titulo: "Pancreatitis aguda con ictericia de bilirrubina directa: sospecha de causa biliar, colangiorresonancia para buscar cálculos en el colédoco",
    imagen: "flujogramas/pancreatitis-ictericia-bilirrubina-directa-colangiorresonancia.svg",
    alt: "Flujograma: Pancreatitis aguda con ictericia de bilirrubina directa: sospecha de causa biliar, colangiorresonancia para buscar cálculos en el colédoco"
  },
  "REU-027": {
    titulo: "Monoartritis aguda de rodilla con líquido sinovial de más de 80 000 leucocitos y 80 % de neutrófilos: artritis séptica",
    imagen: "flujogramas/rodilla-80000-leucocitos-artritis-septica.svg",
    alt: "Flujograma: Monoartritis aguda de rodilla con líquido sinovial de más de 80 000 leucocitos y 80 % de neutrófilos: artritis séptica"
  },
  "TRA-019": {
    titulo: "Joven atropellado con herida abierta y fractura conminuta de tibia: fractura expuesta, fijación externa",
    imagen: "flujogramas/atropello-fractura-expuesta-conminuta-tibia-fijacion-externa.svg",
    alt: "Flujograma: Joven atropellado con herida abierta y fractura conminuta de tibia: fractura expuesta, fijación externa"
  },
  "SP-072": {
    titulo: "Caso de malaria en Lima, donde no hay Anopheles: el ambiente no favorece la transmisión",
    imagen: "flujogramas/malaria-vivax-lima-sin-vector-ambiente.svg",
    alt: "Flujograma: Caso de malaria en Lima, donde no hay Anopheles: el ambiente no favorece la transmisión"
  },
  "SP-073": {
    titulo: "Encuesta aplicada al 100 % de los integrantes del club: los participantes son la población, no una muestra",
    imagen: "flujogramas/club-adulto-mayor-encuesta-100-poblacion.svg",
    alt: "Flujograma: Encuesta aplicada al 100 % de los integrantes del club: los participantes son la población, no una muestra"
  },
  "CAR-043": {
    titulo: "Golpe en el precordio con hipotensión, ruidos apagados, yugulares ingurgitadas y troponina alta: ECG y ecocardiograma inmediatos",
    imagen: "flujogramas/golpe-precordial-ruidos-apagados-iy-ecocardiograma.svg",
    alt: "Flujograma: Golpe en el precordio con hipotensión, ruidos apagados, yugulares ingurgitadas y troponina alta: ECG y ecocardiograma inmediatos"
  },
  "PED-110": {
    titulo: "Lactante con diarrea y vómitos, soporoso, ojos muy hundidos, pliegue (+), piel fría y llenado de 5 s: choque hipovolémico, bolo de SSN 20 mL/kg",
    imagen: "flujogramas/lactante-diarrea-soporoso-llenado-5-seg-bolo.svg",
    alt: "Flujograma: Lactante con diarrea y vómitos, soporoso, ojos muy hundidos, pliegue (+), piel fría y llenado de 5 s: choque hipovolémico, bolo de SSN 20 mL/kg"
  },
  "HEM-022": {
    titulo: "Anciano con anemia macrocítica, parestesias, pérdida de la sensibilidad vibratoria y neutrófilos hipersegmentados: anemia megaloblástica por déficit de B12",
    imagen: "flujogramas/vcm-110-hipersegmentados-parestesias-megaloblastica.svg",
    alt: "Flujograma: Anciano con anemia macrocítica, parestesias, pérdida de la sensibilidad vibratoria y neutrófilos hipersegmentados: anemia megaloblástica por déficit de B12"
  },
  "REU-028": {
    titulo: "Niño con prurito intenso nocturno y pápulas en espacios interdigitales, muñecas, axilas, glúteos y genitales, sin tocar la cara: escabiosis",
    imagen: "flujogramas/prurito-nocturno-interdigital-escabiosis.svg",
    alt: "Flujograma: Niño con prurito intenso nocturno y pápulas en espacios interdigitales, muñecas, axilas, glúteos y genitales, sin tocar la cara: escabiosis"
  },
  "OFT-024": {
    titulo: "Adolescente con prurito en el conducto auditivo, otorrea purulenta, hipoacusia, fiebre y adenopatía retroauricular: otitis externa",
    imagen: "flujogramas/prurito-conducto-otorrea-otitis-externa.svg",
    alt: "Flujograma: Adolescente con prurito en el conducto auditivo, otorrea purulenta, hipoacusia, fiebre y adenopatía retroauricular: otitis externa"
  },
  "NEF-040": {
    titulo: "Anciana que toma hidroclorotiazida con desorientación y sopor, y sodio de 115: hiponatremia grave por tiazida",
    imagen: "flujogramas/anciana-sopor-sodio-115-tiazida.svg",
    alt: "Flujograma: Anciana que toma hidroclorotiazida con desorientación y sopor, y sodio de 115: hiponatremia grave por tiazida"
  },
  "CB-033": {
    titulo: "La aldosterona actúa sobre las células principales del túbulo colector para reabsorber sodio y secretar potasio",
    imagen: "flujogramas/aldosterona-celulas-principales-tubulo-colector.svg",
    alt: "Flujograma: La aldosterona actúa sobre las células principales del túbulo colector para reabsorber sodio y secretar potasio"
  },
  "SP-074": {
    titulo: "Un niño de 10 años expresa su aceptación o rechazo a un procedimiento o estudio mediante el asentimiento informado",
    imagen: "flujogramas/nino-10-anos-acepta-procedimiento-asentimiento.svg",
    alt: "Flujograma: Un niño de 10 años expresa su aceptación o rechazo a un procedimiento o estudio mediante el asentimiento informado"
  },
  "CB-034": {
    titulo: "El uso crónico de antiácidos con hidróxido de aluminio atrapa el fosfato en el intestino: hipofosfatemia",
    imagen: "flujogramas/antiacido-hidroxido-aluminio-hipofosfatemia.svg",
    alt: "Flujograma: El uso crónico de antiácidos con hidróxido de aluminio atrapa el fosfato en el intestino: hipofosfatemia"
  },
  "SP-075": {
    titulo: "Casos importados de dengue y presencia de Aedes aegypti: para evitar casos autóctonos se prioriza la participación comunitaria contra los criaderos",
    imagen: "flujogramas/dengue-importado-aedes-participacion-comunitaria.svg",
    alt: "Flujograma: Casos importados de dengue y presencia de Aedes aegypti: para evitar casos autóctonos se prioriza la participación comunitaria contra los criaderos"
  },
  "REU-029": {
    titulo: "Niña de 12 años con acné formado solo por comedones, sin lesiones inflamatorias: acné comedoniano, leve",
    imagen: "flujogramas/nina-12-anos-30-comedones-acne-leve.svg",
    alt: "Flujograma: Niña de 12 años con acné formado solo por comedones, sin lesiones inflamatorias: acné comedoniano, leve"
  },
  "OFT-025": {
    titulo: "Adolescente con secreción mucopurulenta y legañas en ambos ojos, sin dolor ni baja visual: conjuntivitis bacteriana",
    imagen: "flujogramas/leganas-mucopurulentas-bilateral-conjuntivitis.svg",
    alt: "Flujograma: Adolescente con secreción mucopurulenta y legañas en ambos ojos, sin dolor ni baja visual: conjuntivitis bacteriana"
  },
  "INF-054": {
    titulo: "Mujer joven con fiebre, cefalea, vómitos, somnolencia y rigidez de nuca tras un resfriado: meningitis bacteriana por neumococo",
    imagen: "flujogramas/adulta-cefalea-rigidez-nuca-neumococo.svg",
    alt: "Flujograma: Mujer joven con fiebre, cefalea, vómitos, somnolencia y rigidez de nuca tras un resfriado: meningitis bacteriana por neumococo"
  },
  "GAS-040": {
    titulo: "Obeso con pirosis, dolor retroesternal y síntomas respiratorios nocturnos: ERGE con manifestaciones extraesofágicas, iniciar IBP",
    imagen: "flujogramas/obeso-pirosis-asma-nocturna-ibp.svg",
    alt: "Flujograma: Obeso con pirosis, dolor retroesternal y síntomas respiratorios nocturnos: ERGE con manifestaciones extraesofágicas, iniciar IBP"
  },
  "END-028": {
    titulo: "Privación de agua y SIADH tienen ADH alta y orina concentrada; los separa la osmolaridad plasmática (alta en la deshidratación, baja en el SIADH)",
    imagen: "flujogramas/siadh-vs-privacion-agua-osmolaridad-plasmatica.svg",
    alt: "Flujograma: Privación de agua y SIADH tienen ADH alta y orina concentrada; los separa la osmolaridad plasmática (alta en la deshidratación, baja en el SIADH)"
  },
  "GAS-041": {
    titulo: "Pancreatitis grave con necrosis que necesita intervención: drenar cuando la necrosis se encapsula, a las 3-4 semanas",
    imagen: "flujogramas/necrosis-pancreatica-drenaje-3-4-semanas.svg",
    alt: "Flujograma: Pancreatitis grave con necrosis que necesita intervención: drenar cuando la necrosis se encapsula, a las 3-4 semanas"
  },
  "GIN-101": {
    titulo: "Gestante a término sin controles, con VIH detectado en trabajo de parto y 8 cm de dilatación: zidovudina EV y parto vaginal",
    imagen: "flujogramas/vih-prueba-rapida-8-cm-zidovudina-parto-vaginal.svg",
    alt: "Flujograma: Gestante a término sin controles, con VIH detectado en trabajo de parto y 8 cm de dilatación: zidovudina EV y parto vaginal"
  },
  "PSI-020": {
    titulo: "Varón con ánimo deprimido, insomnio e ideas de quitarse la vida tras perder el trabajo: episodio depresivo, sertralina con apoyo psicológico",
    imagen: "flujogramas/desempleo-animo-decaido-ideas-suicidas-sertralina.svg",
    alt: "Flujograma: Varón con ánimo deprimido, insomnio e ideas de quitarse la vida tras perder el trabajo: episodio depresivo, sertralina con apoyo psicológico"
  },
  "GIN-102": {
    titulo: "Gestante de 36 semanas con feto en percentil 2, oligohidramnios y flujo diastólico invertido en la arteria umbilical: terminar la gestación",
    imagen: "flujogramas/rciu-percentil-2-flujo-diastolico-invertido-terminar.svg",
    alt: "Flujograma: Gestante de 36 semanas con feto en percentil 2, oligohidramnios y flujo diastólico invertido en la arteria umbilical: terminar la gestación"
  },
  "PED-111": {
    titulo: "Lactante con neumonía que mejora claramente con el antibiótico: no necesita radiografía de control",
    imagen: "flujogramas/neumonia-lactante-mejoria-sin-rx-control.svg",
    alt: "Flujograma: Lactante con neumonía que mejora claramente con el antibiótico: no necesita radiografía de control"
  },
  "TRA-020": {
    titulo: "Volcadura con dolor cervical y debilidad de brazos a predominio de manos: posible lesión medular, inmovilizar con collar rígido",
    imagen: "flujogramas/volcadura-dolor-cervical-deficit-manos-collarin.svg",
    alt: "Flujograma: Volcadura con dolor cervical y debilidad de brazos a predominio de manos: posible lesión medular, inmovilizar con collar rígido"
  },
  "PED-112": {
    titulo: "Lactante prematura, hija de madre con rubéola, con insuficiencia cardíaca, pulsos saltones y soplo: persistencia del conducto arterioso",
    imagen: "flujogramas/rubeola-materna-pulsos-saltones-ductus.svg",
    alt: "Flujograma: Lactante prematura, hija de madre con rubéola, con insuficiencia cardíaca, pulsos saltones y soplo: persistencia del conducto arterioso"
  },
  "END-029": {
    titulo: "Al levantar ambos brazos aparecen ingurgitación del cuello y dificultad respiratoria (signo de Pemberton): bocio sumergido",
    imagen: "flujogramas/brazos-elevados-congestion-cuello-pemberton.svg",
    alt: "Flujograma: Al levantar ambos brazos aparecen ingurgitación del cuello y dificultad respiratoria (signo de Pemberton): bocio sumergido"
  },
  "GIN-103": {
    titulo: "Manejo activo del alumbramiento en una preeclámptica: oxitocina 10 UI IM al primer minuto (la metilergometrina está contraindicada)",
    imagen: "flujogramas/alumbramiento-dirigido-preeclampsia-oxitocina.svg",
    alt: "Flujograma: Manejo activo del alumbramiento en una preeclámptica: oxitocina 10 UI IM al primer minuto (la metilergometrina está contraindicada)"
  },
  "REU-030": {
    titulo: "Placas eritematosas bien delimitadas con escamas nacaradas en piel y cuero cabelludo, con piqueteado ungueal y onicólisis: psoriasis",
    imagen: "flujogramas/placas-escama-nacarada-piqueteado-ungueal-psoriasis.svg",
    alt: "Flujograma: Placas eritematosas bien delimitadas con escamas nacaradas en piel y cuero cabelludo, con piqueteado ungueal y onicólisis: psoriasis"
  },
  "INF-055": {
    titulo: "Fiebre con mialgias tras viajar a zona endémica y NS1 positivo, en un lugar sin vector: caso confirmado de dengue (importado)",
    imagen: "flujogramas/viaje-zona-endemica-ns1-positivo-caso-confirmado.svg",
    alt: "Flujograma: Fiebre con mialgias tras viajar a zona endémica y NS1 positivo, en un lugar sin vector: caso confirmado de dengue (importado)"
  },
  "PED-113": {
    titulo: "Lactante con escroto derecho vacío y el testículo palpable en el periné: ectopia testicular",
    imagen: "flujogramas/escroto-vacio-testiculo-perineal-ectopia.svg",
    alt: "Flujograma: Lactante con escroto derecho vacío y el testículo palpable en el periné: ectopia testicular"
  },
  "NEU-028": {
    titulo: "Asmático somnoliento, que no puede hablar, con tórax silente, SatO₂ 85 % y bradicardia: crisis de riesgo vital, intubar",
    imagen: "flujogramas/asma-somnoliento-silencio-auscultatorio-intubacion.svg",
    alt: "Flujograma: Asmático somnoliento, que no puede hablar, con tórax silente, SatO₂ 85 % y bradicardia: crisis de riesgo vital, intubar"
  },
  "CB-035": {
    titulo: "Paciente con TB que tomó dosis extra de su tratamiento y presenta confusión y acidosis metabólica grave: intoxicación por isoniazida, piridoxina",
    imagen: "flujogramas/sobredosis-isoniazida-acidosis-piridoxina.svg",
    alt: "Flujograma: Paciente con TB que tomó dosis extra de su tratamiento y presenta confusión y acidosis metabólica grave: intoxicación por isoniazida, piridoxina"
  },
  "GAS-042": {
    titulo: "Cirrótico con ascitis, fiebre, dolor abdominal y encefalopatía: hacer paracentesis diagnóstica para descartar peritonitis bacteriana espontánea",
    imagen: "flujogramas/cirrotico-fiebre-dolor-confusion-paracentesis.svg",
    alt: "Flujograma: Cirrótico con ascitis, fiebre, dolor abdominal y encefalopatía: hacer paracentesis diagnóstica para descartar peritonitis bacteriana espontánea"
  },
  "PED-114": {
    titulo: "Prematuro de 32 semanas y 1100 g que requirió reanimación, con apnea y palidez a las 24 horas: sospecha de hemorragia intraventricular, ecografía transfontanelar",
    imagen: "flujogramas/prematuro-1100-g-apnea-palidez-eco-transfontanelar.svg",
    alt: "Flujograma: Prematuro de 32 semanas y 1100 g que requirió reanimación, con apnea y palidez a las 24 horas: sospecha de hemorragia intraventricular, ecografía transfontanelar"
  },
  "GAS-043": {
    titulo: "Ictericia que en 8 días se acompaña de encefalopatía e INR 6, sin hepatopatía previa: insuficiencia hepática aguda",
    imagen: "flujogramas/ictericia-8-dias-encefalopatia-falla-hepatica-aguda.svg",
    alt: "Flujograma: Ictericia que en 8 días se acompaña de encefalopatía e INR 6, sin hepatopatía previa: insuficiencia hepática aguda"
  },
  "GIN-104": {
    titulo: "Mujer que toma carbamazepina: los anticonceptivos orales combinados son los menos eficaces por la inducción enzimática",
    imagen: "flujogramas/carbamazepina-anticonceptivo-oral-menos-efectivo.svg",
    alt: "Flujograma: Mujer que toma carbamazepina: los anticonceptivos orales combinados son los menos eficaces por la inducción enzimática"
  },
  "GAS-044": {
    titulo: "Cirrótico alcohólico con várices esofágicas grandes que nunca sangraron: betabloqueante no cardioselectivo como profilaxis primaria",
    imagen: "flujogramas/varices-grandes-profilaxis-primaria-betabloqueante.svg",
    alt: "Flujograma: Cirrótico alcohólico con várices esofágicas grandes que nunca sangraron: betabloqueante no cardioselectivo como profilaxis primaria"
  },
  "REU-031": {
    titulo: "Mujer con 6 meses de debilidad proximal simétrica (escaleras, silla, peinarse) sin lesiones de piel: polimiositis",
    imagen: "flujogramas/debilidad-proximal-simetrica-sin-piel-polimiositis.svg",
    alt: "Flujograma: Mujer con 6 meses de debilidad proximal simétrica (escaleras, silla, peinarse) sin lesiones de piel: polimiositis"
  },
  "GIN-105": {
    titulo: "Gestante hipertensa desde antes de las 20 semanas, bien controlada con metildopa, con PA 130/80 y cefalea tras una discusión: hipertensión crónica",
    imagen: "flujogramas/metildopa-desde-8-semanas-pa-controlada-hta-cronica.svg",
    alt: "Flujograma: Gestante hipertensa desde antes de las 20 semanas, bien controlada con metildopa, con PA 130/80 y cefalea tras una discusión: hipertensión crónica"
  },
  "NEU-029": {
    titulo: "EPOC exacerbado con confusión, pH 7,08 y PaCO₂ 60 pese al oxígeno: intubación orotraqueal",
    imagen: "flujogramas/epoc-exacerbado-ph-708-confusion-intubacion.svg",
    alt: "Flujograma: EPOC exacerbado con confusión, pH 7,08 y PaCO₂ 60 pese al oxígeno: intubación orotraqueal"
  },
  "CIR-059": {
    titulo: "Anciana con obstrucción intestinal y masa dolorosa por debajo del pliegue inguinal: hernia femoral (crural) estrangulada",
    imagen: "flujogramas/anciana-masa-bajo-pliegue-inguinal-obstruccion-femoral.svg",
    alt: "Flujograma: Anciana con obstrucción intestinal y masa dolorosa por debajo del pliegue inguinal: hernia femoral (crural) estrangulada"
  },
  "PED-115": {
    titulo: "Niño con tos, coriza y conjuntivitis, luego exantema maculopapular y manchas blancas en la mucosa de las mejillas: sarampión",
    imagen: "flujogramas/fiebre-tos-coriza-conjuntivitis-koplik-sarampion.svg",
    alt: "Flujograma: Niño con tos, coriza y conjuntivitis, luego exantema maculopapular y manchas blancas en la mucosa de las mejillas: sarampión"
  },
  "NRL-030": {
    titulo: "Anciana con olvidos peligrosos (deja la cocina prendida), que no reconoce a familiares, deambula sin rumbo y cambia de ánimo: enfermedad de Alzheimer",
    imagen: "flujogramas/anciana-deja-cocina-prendida-deambula-alzheimer.svg",
    alt: "Flujograma: Anciana con olvidos peligrosos (deja la cocina prendida), que no reconoce a familiares, deambula sin rumbo y cambia de ánimo: enfermedad de Alzheimer"
  },
  "CAR-044": {
    titulo: "Paro cardíaco que revierte con la descarga de un DEA: el ritmo era desfibrilable, fibrilación ventricular",
    imagen: "flujogramas/paro-piscina-dea-descarga-fibrilacion-ventricular.svg",
    alt: "Flujograma: Paro cardíaco que revierte con la descarga de un DEA: el ritmo era desfibrilable, fibrilación ventricular"
  },
  "SP-076": {
    titulo: "El director expone el problema y pide que cada integrante del comité asuma responsabilidades según sus funciones: liderazgo democrático",
    imagen: "flujogramas/director-comite-distrital-dengue-liderazgo-democratico.svg",
    alt: "Flujograma: El director expone el problema y pide que cada integrante del comité asuma responsabilidades según sus funciones: liderazgo democrático"
  },
  "NRL-031": {
    titulo: "Adulto con espasmos de mano y antebrazo solo al escribir, examen normal: distonía focal (calambre del escribiente)",
    imagen: "flujogramas/espasmos-mano-al-escribir-distonia-focal.svg",
    alt: "Flujograma: Adulto con espasmos de mano y antebrazo solo al escribir, examen normal: distonía focal (calambre del escribiente)"
  },
  "CB-036": {
    titulo: "Limeño que llega a Puno con cefalea, fatiga, náuseas y vómitos: mal agudo de montaña; la hipoxia lo hace hiperventilar, alcalosis respiratoria",
    imagen: "flujogramas/lima-puno-cefalea-nauseas-alcalosis-respiratoria.svg",
    alt: "Flujograma: Limeño que llega a Puno con cefalea, fatiga, náuseas y vómitos: mal agudo de montaña; la hipoxia lo hace hiperventilar, alcalosis respiratoria"
  },
  "SP-077": {
    titulo: "Porcentaje de pacientes con TB que recibieron visita domiciliaria: mide una actividad realizada, es un indicador de proceso",
    imagen: "flujogramas/porcentaje-tb-visita-domiciliaria-indicador-proceso.svg",
    alt: "Flujograma: Porcentaje de pacientes con TB que recibieron visita domiciliaria: mide una actividad realizada, es un indicador de proceso"
  },
  "CB-037": {
    titulo: "Anciano con hiperplasia prostática tratado con un alfabloqueador (tamsulosina, doxazosina) que hace hipotensión ortostática: bloqueo alfa-1",
    imagen: "flujogramas/hbp-simpaticolitico-hipotension-ortostatica-alfa1.svg",
    alt: "Flujograma: Anciano con hiperplasia prostática tratado con un alfabloqueador (tamsulosina, doxazosina) que hace hipotensión ortostática: bloqueo alfa-1"
  },
  "GIN-106": {
    titulo: "Gestante de 10 semanas con obesidad, hijo previo macrosómico y hermana diabética: buscar diabetes de inmediato, en el primer control",
    imagen: "flujogramas/imc-34-macrosomia-familiar-dm-tamizaje-inmediato.svg",
    alt: "Flujograma: Gestante de 10 semanas con obesidad, hijo previo macrosómico y hermana diabética: buscar diabetes de inmediato, en el primer control"
  },
  "GIN-107": {
    titulo: "Joven con amenorrea de 7 meses, caracteres sexuales normales, útero y ovarios presentes, y FSH/LH altas: insuficiencia ovárica prematura",
    imagen: "flujogramas/amenorrea-19-anos-fsh-lh-altas-falla-ovarica.svg",
    alt: "Flujograma: Joven con amenorrea de 7 meses, caracteres sexuales normales, útero y ovarios presentes, y FSH/LH altas: insuficiencia ovárica prematura"
  },
  "PED-116": {
    titulo: "Recién nacido a término que sigue en apnea con FC 90 tras los pasos iniciales: ventilación a presión positiva con FiO₂ 21 %",
    imagen: "flujogramas/rn-apnea-fc-90-vpp-aire-ambiente.svg",
    alt: "Flujograma: Recién nacido a término que sigue en apnea con FC 90 tras los pasos iniciales: ventilación a presión positiva con FiO₂ 21 %"
  },
  "GIN-108": {
    titulo: "Anciana con prolapso genital total, vagina seca y úlcera de bordes regulares con PAP negativo y endometrio atrófico: úlcera de decúbito",
    imagen: "flujogramas/prolapso-total-lesion-vaginal-ulcera-decubito.svg",
    alt: "Flujograma: Anciana con prolapso genital total, vagina seca y úlcera de bordes regulares con PAP negativo y endometrio atrófico: úlcera de decúbito"
  },
  "CB-038": {
    titulo: "Anciano asmático que hace retención urinaria aguda: efecto anticolinérgico del bromuro de ipratropio",
    imagen: "flujogramas/asmatico-ipratropio-retencion-urinaria.svg",
    alt: "Flujograma: Anciano asmático que hace retención urinaria aguda: efecto anticolinérgico del bromuro de ipratropio"
  },
  "SP-078": {
    titulo: "La temperatura ambiental puede tomar cualquier valor dentro de un rango (con decimales): es una variable cuantitativa continua",
    imagen: "flujogramas/temperatura-ambiental-variable-continua.svg",
    alt: "Flujograma: La temperatura ambiental puede tomar cualquier valor dentro de un rango (con decimales): es una variable cuantitativa continua"
  },
  "OFT-026": {
    titulo: "Niño con bajo rendimiento escolar, tímpano perforado y otorrea maloliente: otitis media crónica",
    imagen: "flujogramas/timpano-perforado-otorrea-fetida-otitis-media-cronica.svg",
    alt: "Flujograma: Niño con bajo rendimiento escolar, tímpano perforado y otorrea maloliente: otitis media crónica"
  },
  "NEF-041": {
    titulo: "Mujer joven con HTA de inicio súbito, 190/100 pese a tres fármacos y soplo en el flanco: estenosis de la arteria renal",
    imagen: "flujogramas/mujer-joven-hta-refractaria-soplo-flanco-estenosis-renal.svg",
    alt: "Flujograma: Mujer joven con HTA de inicio súbito, 190/100 pese a tres fármacos y soplo en el flanco: estenosis de la arteria renal"
  },
  "CIR-060": {
    titulo: "Politraumatizada con signos de choque y abdomen doloroso sin heridas: ecografía FAST para buscar sangre en el abdomen",
    imagen: "flujogramas/accidente-transito-choque-abdomen-doloroso-fast.svg",
    alt: "Flujograma: Politraumatizada con signos de choque y abdomen doloroso sin heridas: ecografía FAST para buscar sangre en el abdomen"
  },
  "PED-117": {
    titulo: "La diabetes materna aumenta el riesgo de enfermedad de membrana hialina: la insulina fetal alta retrasa la maduración del surfactante",
    imagen: "flujogramas/membrana-hialina-diabetes-materna.svg",
    alt: "Flujograma: La diabetes materna aumenta el riesgo de enfermedad de membrana hialina: la insulina fetal alta retrasa la maduración del surfactante"
  },
  "NEF-042": {
    titulo: "Anciano con dolor hipogástrico, globo vesical, creatinina 2,8 y potasio 6: retención urinaria con falla renal posrenal, sondaje vesical inmediato",
    imagen: "flujogramas/globo-vesical-creatinina-potasio-sonda.svg",
    alt: "Flujograma: Anciano con dolor hipogástrico, globo vesical, creatinina 2,8 y potasio 6: retención urinaria con falla renal posrenal, sondaje vesical inmediato"
  },
  "NEU-030": {
    titulo: "Hemitórax derecho abombado con matidez, murmullo abolido y egofonía: derrame pleural",
    imagen: "flujogramas/matidez-abolicion-mv-egofonia-derrame-pleural.svg",
    alt: "Flujograma: Hemitórax derecho abombado con matidez, murmullo abolido y egofonía: derrame pleural"
  },
  "NRL-032": {
    titulo: "Hipertenso con hemorragia intraparenquimal izquierda, Glasgow 10 y PA 180/90: control de la presión arterial",
    imagen: "flujogramas/hemorragia-intraparenquimal-pa-180-antihipertensivo.svg",
    alt: "Flujograma: Hipertenso con hemorragia intraparenquimal izquierda, Glasgow 10 y PA 180/90: control de la presión arterial"
  },
  "CAR-045": {
    titulo: "Insuficiencia cardíaca con fibrilación auricular tratada con enalapril, digoxina, furosemida y rivaroxabán: el que mejora la sobrevida es el enalapril",
    imagen: "flujogramas/insuficiencia-cardiaca-enalapril-sobrevida.svg",
    alt: "Flujograma: Insuficiencia cardíaca con fibrilación auricular tratada con enalapril, digoxina, furosemida y rivaroxabán: el que mejora la sobrevida es el enalapril"
  },
  "OFT-027": {
    titulo: "Adolescente con hipoacusia y conducto ocupado por cerumen: irrigación con suero o agua tibia (a temperatura corporal)",
    imagen: "flujogramas/tapon-cerumen-irrigacion-salino-tibio.svg",
    alt: "Flujograma: Adolescente con hipoacusia y conducto ocupado por cerumen: irrigación con suero o agua tibia (a temperatura corporal)"
  },
  "PED-118": {
    titulo: "Recién nacido con masa blanda y fluctuante limitada al parietal derecho, que no cruza las suturas: cefalohematoma",
    imagen: "flujogramas/rn-tumoracion-parietal-no-cruza-sutura-cefalohematoma.svg",
    alt: "Flujograma: Recién nacido con masa blanda y fluctuante limitada al parietal derecho, que no cruza las suturas: cefalohematoma"
  },
  "REU-032": {
    titulo: "Adulto con hepatitis B, fiebre, pérdida de peso, dolor testicular, livedo, mononeuritis y vasculitis necrotizante de arterias medianas: poliarteritis nudosa",
    imagen: "flujogramas/hepatitis-b-livedo-dolor-testicular-poliarteritis-nudosa.svg",
    alt: "Flujograma: Adulto con hepatitis B, fiebre, pérdida de peso, dolor testicular, livedo, mononeuritis y vasculitis necrotizante de arterias medianas: poliarteritis nudosa"
  },
  "SP-079": {
    titulo: "Paciente con cáncer metastásico tratado en casa solo con oxígeno y analgésicos para su confort: ortotanasia",
    imagen: "flujogramas/cancer-metastasico-oxigeno-analgesia-ortotanasia.svg",
    alt: "Flujograma: Paciente con cáncer metastásico tratado en casa solo con oxígeno y analgésicos para su confort: ortotanasia"
  },
  "NRL-033": {
    titulo: "Fumador con tos crónica, convulsiones y dos lesiones cerebrales redondas con realce en anillo y mucho edema: metástasis cerebrales",
    imagen: "flujogramas/fumador-convulsion-dos-lesiones-anillo-metastasis.svg",
    alt: "Flujograma: Fumador con tos crónica, convulsiones y dos lesiones cerebrales redondas con realce en anillo y mucho edema: metástasis cerebrales"
  },
  "PED-119": {
    titulo: "Recién nacido de madre con corioamnionitis, con hipotermia e intolerancia oral a las 16 horas: sospecha de sepsis temprana, el índice I/T > 0,2 la apoya",
    imagen: "flujogramas/corioamnionitis-hipotermia-indice-it-sepsis.svg",
    alt: "Flujograma: Recién nacido de madre con corioamnionitis, con hipotermia e intolerancia oral a las 16 horas: sospecha de sepsis temprana, el índice I/T > 0,2 la apoya"
  },
  "PED-120": {
    titulo: "Niño con varicela que recibió aspirina y presenta convulsiones, hepatomegalia y LCR normal: síndrome de Reye",
    imagen: "flujogramas/varicela-aspirina-convulsion-hepatomegalia-reye.svg",
    alt: "Flujograma: Niño con varicela que recibió aspirina y presenta convulsiones, hepatomegalia y LCR normal: síndrome de Reye"
  },
  "NEF-043": {
    titulo: "Varón sin beber ni comer por día y medio, con oliguria, hipotensión, taquicardia y mucosas secas: lesión renal prerrenal, sodio urinario bajo",
    imagen: "flujogramas/secuestro-sin-agua-oliguria-sodio-urinario-bajo.svg",
    alt: "Flujograma: Varón sin beber ni comer por día y medio, con oliguria, hipotensión, taquicardia y mucosas secas: lesión renal prerrenal, sodio urinario bajo"
  },
  "SP-080": {
    titulo: "La capacidad de un agente infeccioso de producir enfermedad en el infectado se llama patogenicidad",
    imagen: "flujogramas/capacidad-producir-enfermedad-patogenicidad.svg",
    alt: "Flujograma: La capacidad de un agente infeccioso de producir enfermedad en el infectado se llama patogenicidad"
  },
  "GIN-109": {
    titulo: "Multigesta en trabajo de parto avanzado con presentación de cara mentoanterior: parto vaginal espontáneo",
    imagen: "flujogramas/presentacion-cara-mentoanterior-parto-vaginal.svg",
    alt: "Flujograma: Multigesta en trabajo de parto avanzado con presentación de cara mentoanterior: parto vaginal espontáneo"
  },
  "CIR-061": {
    titulo: "Quemadura de tercer grado que rodea toda la pierna y sin pulso pedio: escarotomía",
    imagen: "flujogramas/quemadura-circunferencial-pierna-sin-pulso-escarotomia.svg",
    alt: "Flujograma: Quemadura de tercer grado que rodea toda la pierna y sin pulso pedio: escarotomía"
  },
  "NEF-044": {
    titulo: "Mujer con litiasis e infecciones urinarias repetidas, fiebre y dolor lumbar de un mes, anemia y macrófagos espumosos en la orina: pielonefritis xantogranulomatosa",
    imagen: "flujogramas/litiasis-itu-repeticion-macrofagos-espumosos-xantogranulomatosa.svg",
    alt: "Flujograma: Mujer con litiasis e infecciones urinarias repetidas, fiebre y dolor lumbar de un mes, anemia y macrófagos espumosos en la orina: pielonefritis xantogranulomatosa"
  },
  "END-030": {
    titulo: "En la diabetes tipo 2, el adulto de 18 a 64 años debe hacer al menos 150 minutos semanales de actividad aeróbica moderada",
    imagen: "flujogramas/diabetes-actividad-fisica-150-minutos.svg",
    alt: "Flujograma: En la diabetes tipo 2, el adulto de 18 a 64 años debe hacer al menos 150 minutos semanales de actividad aeróbica moderada"
  },
  "PED-121": {
    titulo: "Lactante de 4 semanas con ictericia verdínica, coluria, heces pálidas y bilirrubina directa de 12: colestasis, la ecografía abdominal es el primer examen",
    imagen: "flujogramas/lactante-4-semanas-acolia-bilirrubina-directa-ecografia.svg",
    alt: "Flujograma: Lactante de 4 semanas con ictericia verdínica, coluria, heces pálidas y bilirrubina directa de 12: colestasis, la ecografía abdominal es el primer examen"
  },
  "GIN-110": {
    titulo: "PAP con lesión intraepitelial de alto grado en una mujer de 32 años: colposcopía y biopsia",
    imagen: "flujogramas/pap-lesion-alto-grado-colposcopia-biopsia.svg",
    alt: "Flujograma: PAP con lesión intraepitelial de alto grado en una mujer de 32 años: colposcopía y biopsia"
  },
  "REU-033": {
    titulo: "Mujer joven con edema y orina espumosa, artralgias, fotosensibilidad, eritema facial y derrame pleural bilateral: lupus eritematoso sistémico",
    imagen: "flujogramas/eritema-facial-proteinuria-derrame-pleural-lupus.svg",
    alt: "Flujograma: Mujer joven con edema y orina espumosa, artralgias, fotosensibilidad, eritema facial y derrame pleural bilateral: lupus eritematoso sistémico"
  },
  "CAR-046": {
    titulo: "Hipertenso con PA 190/120, cefalea, vómitos, papiledema y confusión sin focalidad: encefalopatía hipertensiva, labetalol EV",
    imagen: "flujogramas/papiledema-confusion-pa-190-120-labetalol.svg",
    alt: "Flujograma: Hipertenso con PA 190/120, cefalea, vómitos, papiledema y confusión sin focalidad: encefalopatía hipertensiva, labetalol EV"
  },
  "END-031": {
    titulo: "Mujer que toma pastillas para adelgazar con hipertiroidismo, tiroides no palpable y TSH suprimida: tirotoxicosis facticia",
    imagen: "flujogramas/pastillas-adelgazar-tsh-indetectable-tiroides-no-palpable-facticia.svg",
    alt: "Flujograma: Mujer que toma pastillas para adelgazar con hipertiroidismo, tiroides no palpable y TSH suprimida: tirotoxicosis facticia"
  },
  "SP-081": {
    titulo: "Tomar 150 casos de forma no aleatoria entre los que ingresaron al hospital: muestreo por conveniencia",
    imagen: "flujogramas/150-casos-no-aleatorio-muestreo-conveniencia.svg",
    alt: "Flujograma: Tomar 150 casos de forma no aleatoria entre los que ingresaron al hospital: muestreo por conveniencia"
  },
  "END-032": {
    titulo: "Mujer joven con hipertiroidismo, bocio difuso, exoftalmos bilateral y mixedema pretibial: enfermedad de Graves",
    imagen: "flujogramas/bocio-exoftalmos-mixedema-pretibial-graves.svg",
    alt: "Flujograma: Mujer joven con hipertiroidismo, bocio difuso, exoftalmos bilateral y mixedema pretibial: enfermedad de Graves"
  },
  "TRA-021": {
    titulo: "Lactante de 1 mes con pie equinovaro: referir al ortopedista infantil para tratamiento de Ponseti",
    imagen: "flujogramas/lactante-pie-equinovaro-referir-ortopedista.svg",
    alt: "Flujograma: Lactante de 1 mes con pie equinovaro: referir al ortopedista infantil para tratamiento de Ponseti"
  },
  "GIN-111": {
    titulo: "Gestante con VIH en TAR y carga viral de 500 copias a las 38 semanas: puede tener parto vaginal",
    imagen: "flujogramas/vih-tar-carga-viral-500-parto-vaginal.svg",
    alt: "Flujograma: Gestante con VIH en TAR y carga viral de 500 copias a las 38 semanas: puede tener parto vaginal"
  },
  "CB-039": {
    titulo: "Veterinario somnoliento con miosis, bradipnea, hipoxemia, hipercapnia y venopunturas: intoxicación por opioides, naloxona",
    imagen: "flujogramas/miosis-bradipnea-sopor-venopunturas-naloxona.svg",
    alt: "Flujograma: Veterinario somnoliento con miosis, bradipnea, hipoxemia, hipercapnia y venopunturas: intoxicación por opioides, naloxona"
  },
  "SP-082": {
    titulo: "Aumento de TB en un asentamiento de migrantes rurales: el equipo de promoción debe hacer comunicación educativa para reconocer pronto los síntomas",
    imagen: "flujogramas/tb-asentamiento-migrante-comunicacion-educativa.svg",
    alt: "Flujograma: Aumento de TB en un asentamiento de migrantes rurales: el equipo de promoción debe hacer comunicación educativa para reconocer pronto los síntomas"
  },
  "TRA-022": {
    titulo: "Fractura cerrada de la diáfisis del húmero, no desplazada y sin lesión del nervio radial: tratamiento con ortesis funcional",
    imagen: "flujogramas/fractura-diafisis-humero-no-desplazada-ortesis.svg",
    alt: "Flujograma: Fractura cerrada de la diáfisis del húmero, no desplazada y sin lesión del nervio radial: tratamiento con ortesis funcional"
  },
  "NEF-045": {
    titulo: "Dolor cólico intenso en flanco y región lumbar derecha que irradia a ingle y testículo, con vómitos y sin peritonismo: cólico renal",
    imagen: "flujogramas/dolor-flanco-irradia-testiculo-sin-postura-colico-renal.svg",
    alt: "Flujograma: Dolor cólico intenso en flanco y región lumbar derecha que irradia a ingle y testículo, con vómitos y sin peritonismo: cólico renal"
  },
  "PED-122": {
    titulo: "Recién nacido con infección del muñón umbilical y celulitis alrededor: onfalitis, antibiótico sistémico inmediato",
    imagen: "flujogramas/onfalitis-celulitis-periumbilical-antibiotico-sistemico.svg",
    alt: "Flujograma: Recién nacido con infección del muñón umbilical y celulitis alrededor: onfalitis, antibiótico sistémico inmediato"
  },
  "NEF-046": {
    titulo: "Diabético de 30 años de evolución con goteo urinario y globo vesical doloroso: vejiga neurogénica con retención por rebosamiento",
    imagen: "flujogramas/diabetico-30-anos-goteo-globo-vesical-vejiga-neurogenica.svg",
    alt: "Flujograma: Diabético de 30 años de evolución con goteo urinario y globo vesical doloroso: vejiga neurogénica con retención por rebosamiento"
  },
  "INF-056": {
    titulo: "Veterinario con fiebre ondulante de un mes, dolor lumbar, compromiso de la cadera y Rosa de Bengala positiva: brucelosis",
    imagen: "flujogramas/veterinario-fiebre-ondulante-rosa-bengala-brucelosis.svg",
    alt: "Flujograma: Veterinario con fiebre ondulante de un mes, dolor lumbar, compromiso de la cadera y Rosa de Bengala positiva: brucelosis"
  },
  "REU-034": {
    titulo: "Escolar con prurito del cuero cabelludo, lesiones de rascado, puntos blanco nacarados pegados al pelo y adenopatías occipitales: pediculosis",
    imagen: "flujogramas/nina-prurito-cuero-cabelludo-liendres-pediculosis.svg",
    alt: "Flujograma: Escolar con prurito del cuero cabelludo, lesiones de rascado, puntos blanco nacarados pegados al pelo y adenopatías occipitales: pediculosis"
  },
  "INF-057": {
    titulo: "Exposición sexual de riesgo hace 20 días: la prueba que detecta antes el VIH es el ELISA de cuarta generación (antígeno p24 + anticuerpos)",
    imagen: "flujogramas/relacion-riesgo-20-dias-elisa-cuarta-generacion.svg",
    alt: "Flujograma: Exposición sexual de riesgo hace 20 días: la prueba que detecta antes el VIH es el ELISA de cuarta generación (antígeno p24 + anticuerpos)"
  },
  "GIN-112": {
    titulo: "Gestante de 32 semanas con contracciones y cérvix de 15 mm: amenaza de parto pretérmino, corticoides y tocolíticos",
    imagen: "flujogramas/32-semanas-contracciones-cervix-15-mm-corticoides-tocolisis.svg",
    alt: "Flujograma: Gestante de 32 semanas con contracciones y cérvix de 15 mm: amenaza de parto pretérmino, corticoides y tocolíticos"
  },
  "GIN-113": {
    titulo: "Flujo blanco grisáceo y fétido con mucosa normal y células clave en el frotis: vaginosis bacteriana por Gardnerella",
    imagen: "flujogramas/flujo-gris-fetido-celulas-clave-gardnerella.svg",
    alt: "Flujograma: Flujo blanco grisáceo y fétido con mucosa normal y células clave en el frotis: vaginosis bacteriana por Gardnerella"
  },
  "OFT-028": {
    titulo: "Cuerpo extraño incrustado en el ojo con perforación, en un establecimiento del primer nivel: no intentar retirarlo",
    imagen: "flujogramas/cuerpo-extrano-incrustado-perforacion-no-retirar.svg",
    alt: "Flujograma: Cuerpo extraño incrustado en el ojo con perforación, en un establecimiento del primer nivel: no intentar retirarlo"
  },
  "GIN-114": {
    titulo: "Durante el seguimiento con β-hCG tras evacuar una mola se recomienda un anticonceptivo hormonal eficaz, como el implante",
    imagen: "flujogramas/mola-evacuada-vigilancia-implante-progestina.svg",
    alt: "Flujograma: Durante el seguimiento con β-hCG tras evacuar una mola se recomienda un anticonceptivo hormonal eficaz, como el implante"
  },
  "PED-123": {
    titulo: "Prematuro tardío de bajo peso, hijo de madre preeclámptica, con hipoactividad y temblores a las 3 horas: hipoglucemia neonatal",
    imagen: "flujogramas/prematuro-2200-g-temblores-hipoactivo-hipoglucemia.svg",
    alt: "Flujograma: Prematuro tardío de bajo peso, hijo de madre preeclámptica, con hipoactividad y temblores a las 3 horas: hipoglucemia neonatal"
  },
  "INF-058": {
    titulo: "Joven con adenopatías cervicales que crecen en meses, no dolorosas, una que fistuliza con material grumoso, y eritema indurado previo: tuberculosis ganglionar",
    imagen: "flujogramas/adenopatias-cervicales-fistula-caseosa-tb-ganglionar.svg",
    alt: "Flujograma: Joven con adenopatías cervicales que crecen en meses, no dolorosas, una que fistuliza con material grumoso, y eritema indurado previo: tuberculosis ganglionar"
  },
  "NEU-031": {
    titulo: "Síntomas 2 días por semana y despertares nocturnos 2 veces al mes: asma intermitente",
    imagen: "flujogramas/sintomas-2-dias-semana-2-noches-mes-asma-intermitente.svg",
    alt: "Flujograma: Síntomas 2 días por semana y despertares nocturnos 2 veces al mes: asma intermitente"
  },
  "REU-035": {
    titulo: "Mujer obesa y diabética con lesiones rojas, húmedas y descamativas en ambos pliegues inguinales que no mejoran con cremas: intertrigo por Candida",
    imagen: "flujogramas/obesa-diabetica-pliegues-inguinales-candida.svg",
    alt: "Flujograma: Mujer obesa y diabética con lesiones rojas, húmedas y descamativas en ambos pliegues inguinales que no mejoran con cremas: intertrigo por Candida"
  },
  "NRL-034": {
    titulo: "Mujer joven con ptosis, diplopía y debilidad que empeora con el esfuerzo y mejora con el reposo: miastenia gravis, anticuerpos contra el receptor nicotínico",
    imagen: "flujogramas/ptosis-diplopia-fatiga-receptor-nicotinico.svg",
    alt: "Flujograma: Mujer joven con ptosis, diplopía y debilidad que empeora con el esfuerzo y mejora con el reposo: miastenia gravis, anticuerpos contra el receptor nicotínico"
  },
  "INF-059": {
    titulo: "Usuario de drogas EV con fiebre, disnea, soplo nuevo y manchas rojas indoloras en palmas y plantas (Janeway): endocarditis por Staphylococcus aureus",
    imagen: "flujogramas/drogas-ev-janeway-soplo-mitral-staphylococcus.svg",
    alt: "Flujograma: Usuario de drogas EV con fiebre, disnea, soplo nuevo y manchas rojas indoloras en palmas y plantas (Janeway): endocarditis por Staphylococcus aureus"
  },
  "PED-124": {
    titulo: "El desprendimiento de placenta es un evento centinela en el parto para la encefalopatía hipóxico-isquémica",
    imagen: "flujogramas/evento-centinela-encefalopatia-hipoxica-dpp.svg",
    alt: "Flujograma: El desprendimiento de placenta es un evento centinela en el parto para la encefalopatía hipóxico-isquémica"
  },
  "CB-040": {
    titulo: "Sacar la lengua hacia adelante (protrusión) depende del músculo geniogloso, inervado por el XII par",
    imagen: "flujogramas/sacar-lengua-musculo-geniogloso.svg",
    alt: "Flujograma: Sacar la lengua hacia adelante (protrusión) depende del músculo geniogloso, inervado por el XII par"
  },
  "INF-060": {
    titulo: "Joven de Piura con 2 días de fiebre, mialgias, cefalea, epistaxis y leucopenia: sospecha de dengue en fase febril, pedir antígeno NS1",
    imagen: "flujogramas/piura-fiebre-2-dias-leucopenia-ns1.svg",
    alt: "Flujograma: Joven de Piura con 2 días de fiebre, mialgias, cefalea, epistaxis y leucopenia: sospecha de dengue en fase febril, pedir antígeno NS1"
  },
  "GIN-115": {
    titulo: "Cesareada hace 14 meses con sangrado profuso, dolor intenso e hipotensión tras el alumbramiento, con útero contraído: dehiscencia de la cicatriz uterina",
    imagen: "flujogramas/cesarea-14-meses-sangrado-utero-contraido-dehiscencia.svg",
    alt: "Flujograma: Cesareada hace 14 meses con sangrado profuso, dolor intenso e hipotensión tras el alumbramiento, con útero contraído: dehiscencia de la cicatriz uterina"
  },
  "GIN-116": {
    titulo: "Gestante de 14 semanas con VIH confirmado: iniciar el tratamiento antirretroviral de inmediato",
    imagen: "flujogramas/gestante-14-semanas-vih-confirmado-tar-inmediato.svg",
    alt: "Flujograma: Gestante de 14 semanas con VIH confirmado: iniciar el tratamiento antirretroviral de inmediato"
  },
  "SP-083": {
    titulo: "Paciente terminal que pide morir y el médico omite medidas que podrían prolongar su vida: eutanasia pasiva",
    imagen: "flujogramas/terminal-pide-morir-medico-omite-medidas-eutanasia-pasiva.svg",
    alt: "Flujograma: Paciente terminal que pide morir y el médico omite medidas que podrían prolongar su vida: eutanasia pasiva"
  },
  "GIN-117": {
    titulo: "Gestante con dos cesáreas que tras contracciones presenta dolor intenso, sangrado, choque y latidos fetales ausentes: rotura uterina",
    imagen: "flujogramas/dos-cesareas-dolor-choque-latidos-ausentes-rotura-uterina.svg",
    alt: "Flujograma: Gestante con dos cesáreas que tras contracciones presenta dolor intenso, sangrado, choque y latidos fetales ausentes: rotura uterina"
  },
  "GAS-045": {
    titulo: "Cirrótico con estreñimiento y mala dieta que presenta somnolencia, confusión y asterixis: encefalopatía hepática, lactulosa",
    imagen: "flujogramas/cirrotico-estrenimiento-flapping-lactulosa.svg",
    alt: "Flujograma: Cirrótico con estreñimiento y mala dieta que presenta somnolencia, confusión y asterixis: encefalopatía hepática, lactulosa"
  },
  "NRL-035": {
    titulo: "Hipertenso con hematoma cerebeloso de 3,5 cm que comprime el cuarto ventrículo y está letárgico: descompresión quirúrgica",
    imagen: "flujogramas/hematoma-cerebeloso-35-cm-cuarto-ventriculo-cirugia.svg",
    alt: "Flujograma: Hipertenso con hematoma cerebeloso de 3,5 cm que comprime el cuarto ventrículo y está letárgico: descompresión quirúrgica"
  },
  "CB-041": {
    titulo: "Mujer epiléptica con pielonefritis: entre los antibióticos, la levofloxacina es la que más baja el umbral convulsivo",
    imagen: "flujogramas/epilepsia-pielonefritis-levofloxacino-convulsiones.svg",
    alt: "Flujograma: Mujer epiléptica con pielonefritis: entre los antibióticos, la levofloxacina es la que más baja el umbral convulsivo"
  },
  "SP-084": {
    titulo: "Un laboratorio ofrece al médico una comisión por cada receta de su producto: conflicto de interés",
    imagen: "flujogramas/visitador-medico-comision-receta-conflicto-interes.svg",
    alt: "Flujograma: Un laboratorio ofrece al médico una comisión por cada receta de su producto: conflicto de interés"
  },
  "PED-125": {
    titulo: "El germen más común de la osteomielitis aguda en niños es Staphylococcus aureus",
    imagen: "flujogramas/osteomielitis-aguda-nino-staphylococcus-aureus.svg",
    alt: "Flujograma: El germen más común de la osteomielitis aguda en niños es Staphylococcus aureus"
  },
  "CIR-062": {
    titulo: "Choque contra el timón con dolor epigástrico que aumenta al segundo día pese a FAST negativa: trauma pancreático",
    imagen: "flujogramas/golpe-timon-fast-negativo-dolor-epigastrico-pancreas.svg",
    alt: "Flujograma: Choque contra el timón con dolor epigástrico que aumenta al segundo día pese a FAST negativa: trauma pancreático"
  },
  "CAR-047": {
    titulo: "Anciano con fibrilación auricular tratado 5 años con un antiarrítmico, con disnea progresiva, tos seca y pérdida de peso: toxicidad pulmonar por amiodarona",
    imagen: "flujogramas/fa-antiarritmico-5-anos-tos-disnea-amiodarona.svg",
    alt: "Flujograma: Anciano con fibrilación auricular tratado 5 años con un antiarrítmico, con disnea progresiva, tos seca y pérdida de peso: toxicidad pulmonar por amiodarona"
  },
  "PED-126": {
    titulo: "Lactante de 2 meses con conjuntivitis previa, tos, taquipnea sin fiebre e infiltrados intersticiales con hiperinsuflación: neumonía por Chlamydia trachomatis",
    imagen: "flujogramas/lactante-2-meses-afebril-conjuntivitis-chlamydia.svg",
    alt: "Flujograma: Lactante de 2 meses con conjuntivitis previa, tos, taquipnea sin fiebre e infiltrados intersticiales con hiperinsuflación: neumonía por Chlamydia trachomatis"
  },
  "SP-085": {
    titulo: "Obstetra que decide esperar un parto vaginal pese a bradicardia fetal, meconio espeso y patrón de categoría III: falta al principio de beneficencia",
    imagen: "flujogramas/categoria-iii-meconio-espera-parto-beneficencia.svg",
    alt: "Flujograma: Obstetra que decide esperar un parto vaginal pese a bradicardia fetal, meconio espeso y patrón de categoría III: falta al principio de beneficencia"
  },
  "INF-061": {
    titulo: "Niño de 3 años, contacto de su padre con TB pulmonar BK (+), con PPD de 8 mm: descartar TB activa e iniciar terapia preventiva",
    imagen: "flujogramas/nino-3-anos-padre-bk-positivo-ppd-8-terapia-preventiva.svg",
    alt: "Flujograma: Niño de 3 años, contacto de su padre con TB pulmonar BK (+), con PPD de 8 mm: descartar TB activa e iniciar terapia preventiva"
  },
  "GIN-118": {
    titulo: "Gestante hipertensa que siguió tomando enalapril y tiene oligohidramnios con feto sin malformaciones: efecto del IECA",
    imagen: "flujogramas/enalapril-embarazo-oligohidramnios-ieca.svg",
    alt: "Flujograma: Gestante hipertensa que siguió tomando enalapril y tiene oligohidramnios con feto sin malformaciones: efecto del IECA"
  },
  "NEF-047": {
    titulo: "Hipertensa con hidroclorotiazida y antiácidos, con K 2,8, Cl 88 y HCO₃ 32: alcalosis metabólica",
    imagen: "flujogramas/tiazida-antiacidos-hco3-32-k-28-alcalosis-metabolica.svg",
    alt: "Flujograma: Hipertensa con hidroclorotiazida y antiácidos, con K 2,8, Cl 88 y HCO₃ 32: alcalosis metabólica"
  },
  "REU-036": {
    titulo: "Lactante con placa roja brillante y bien delimitada en la zona del pañal que toma los pliegues: dermatitis del pañal por Candida, antifúngico tópico",
    imagen: "flujogramas/lactante-panal-placa-brillante-pliegues-econazol.svg",
    alt: "Flujograma: Lactante con placa roja brillante y bien delimitada en la zona del pañal que toma los pliegues: dermatitis del pañal por Candida, antifúngico tópico"
  },
  "CIR-063": {
    titulo: "Colecistitis aguda con Murphy (++) y aire en la pared de la vesícula en la TC: colecistitis enfisematosa, colecistectomía de emergencia",
    imagen: "flujogramas/murphy-aire-pared-vesicular-colecistitis-enfisematosa.svg",
    alt: "Flujograma: Colecistitis aguda con Murphy (++) y aire en la pared de la vesícula en la TC: colecistitis enfisematosa, colecistectomía de emergencia"
  },
  "OFT-029": {
    titulo: "Golpe en el ojo con dolor, fotofobia, visión borrosa y sangre con nivel en la cámara anterior: hipema",
    imagen: "flujogramas/golpe-ojo-futbol-nivel-sangre-camara-hipema.svg",
    alt: "Flujograma: Golpe en el ojo con dolor, fotofobia, visión borrosa y sangre con nivel en la cámara anterior: hipema"
  },
  "CIR-064": {
    titulo: "Quemadura de 2.º grado por agua hirviendo en ambos brazos y el tronco (más del 50 %): la medida inmediata es cubrirlo con una sábana limpia y seca",
    imagen: "flujogramas/escaldadura-brazos-tronco-54-scq-sabana-limpia.svg",
    alt: "Flujograma: Quemadura de 2.º grado por agua hirviendo en ambos brazos y el tronco (más del 50 %): la medida inmediata es cubrirlo con una sábana limpia y seca"
  },
  "GIN-119": {
    titulo: "Gestante con sobrepeso (IMC 25-29,9) y embarazo único: ganancia de peso recomendada de 7 a 11,5 kg",
    imagen: "flujogramas/sobrepeso-ganancia-peso-gestacional-7-115-kg.svg",
    alt: "Flujograma: Gestante con sobrepeso (IMC 25-29,9) y embarazo único: ganancia de peso recomendada de 7 a 11,5 kg"
  },
  "CB-042": {
    titulo: "Alcohólico gastrectomizado con dermatitis en zonas expuestas al sol (collar de Casal), diarrea y pérdida de memoria: pelagra por déficit de niacina",
    imagen: "flujogramas/alcoholico-collar-casal-diarrea-demencia-niacina.svg",
    alt: "Flujograma: Alcohólico gastrectomizado con dermatitis en zonas expuestas al sol (collar de Casal), diarrea y pérdida de memoria: pelagra por déficit de niacina"
  },
  "NEF-048": {
    titulo: "Parapléjico monorreno con sonda vesical permanente, anuria, hidronefrosis, creatinina 3 y K 5,8: sonda obstruida, cambiar el catéter vesical",
    imagen: "flujogramas/paraplejico-sonda-anuria-hidronefrosis-cambio-cateter.svg",
    alt: "Flujograma: Parapléjico monorreno con sonda vesical permanente, anuria, hidronefrosis, creatinina 3 y K 5,8: sonda obstruida, cambiar el catéter vesical"
  },
  "GIN-120": {
    titulo: "Gestante de 6 semanas con acné a quien quieren dar retinoides: están contraindicados durante todo el embarazo",
    imagen: "flujogramas/gestante-6-semanas-acne-retinoides-contraindicados.svg",
    alt: "Flujograma: Gestante de 6 semanas con acné a quien quieren dar retinoides: están contraindicados durante todo el embarazo"
  },
  "END-033": {
    titulo: "Joven con poliuria, polidipsia y cefalea: la diabetes insípida se reconoce por poliuria con orina diluida (densidad baja) y sodio alto",
    imagen: "flujogramas/poliuria-polidipsia-orina-diluida-hipernatremia-diabetes-insipida.svg",
    alt: "Flujograma: Joven con poliuria, polidipsia y cefalea: la diabetes insípida se reconoce por poliuria con orina diluida (densidad baja) y sodio alto"
  },
  "INF-062": {
    titulo: "Paciente con VIH y neumonía por Pneumocystis jirovecii: el tratamiento de elección es cotrimoxazol",
    imagen: "flujogramas/vih-pneumocystis-cotrimoxazol.svg",
    alt: "Flujograma: Paciente con VIH y neumonía por Pneumocystis jirovecii: el tratamiento de elección es cotrimoxazol"
  },
  "GIN-121": {
    titulo: "Mujer con 6 semanas de amenorrea, síncope, hipotensión, taquicardia y culdocentesis positiva: embarazo ectópico roto",
    imagen: "flujogramas/amenorrea-6-semanas-choque-culdocentesis-ectopico-roto.svg",
    alt: "Flujograma: Mujer con 6 semanas de amenorrea, síncope, hipotensión, taquicardia y culdocentesis positiva: embarazo ectópico roto"
  },
  "SP-086": {
    titulo: "El autoexamen de mama busca detectar temprano una lesión: es prevención secundaria",
    imagen: "flujogramas/autoexamen-mama-prevencion-secundaria.svg",
    alt: "Flujograma: El autoexamen de mama busca detectar temprano una lesión: es prevención secundaria"
  },
  "CB-043": {
    titulo: "Hipoestesia en la cara anterior del muslo y medial de la pierna tras una cirugía renal retroperitoneal: lesión del nervio femoral",
    imagen: "flujogramas/pielolitotomia-hipoestesia-muslo-anterior-nervio-femoral.svg",
    alt: "Flujograma: Hipoestesia en la cara anterior del muslo y medial de la pierna tras una cirugía renal retroperitoneal: lesión del nervio femoral"
  },
  "END-034": {
    titulo: "Paciente con ketoconazol prolongado, debilidad, vómitos, hipotensión ortostática, hiperpigmentación, hiponatremia, hipoglucemia y cortisol que no sube con ACTH: cortisol bajo",
    imagen: "flujogramas/ketoconazol-hiperpigmentacion-hiponatremia-cortisol-bajo.svg",
    alt: "Flujograma: Paciente con ketoconazol prolongado, debilidad, vómitos, hipotensión ortostática, hiperpigmentación, hiponatremia, hipoglucemia y cortisol que no sube con ACTH: cortisol bajo"
  },
  "CAR-048": {
    titulo: "Infarto con hipotensión, piel fría, llenado lento, crepitantes e ingurgitación yugular: choque cardiogénico con precarga alta (frío y húmedo)",
    imagen: "flujogramas/infarto-hipotension-iy-crepitantes-precarga-alta.svg",
    alt: "Flujograma: Infarto con hipotensión, piel fría, llenado lento, crepitantes e ingurgitación yugular: choque cardiogénico con precarga alta (frío y húmedo)"
  },
  "SP-087": {
    titulo: "Adulta mayor agredida física y amenazada de muerte por su hijo: la conducta urgente es denunciar a las autoridades",
    imagen: "flujogramas/adulta-mayor-hijo-agresor-amenaza-denuncia.svg",
    alt: "Flujograma: Adulta mayor agredida física y amenazada de muerte por su hijo: la conducta urgente es denunciar a las autoridades"
  },
  "PED-127": {
    titulo: "Neonato de 2 semanas con fiebre, irritabilidad y succión débil en quien no se logra la punción lumbar: iniciar antibióticos parenterales sin esperar",
    imagen: "flujogramas/neonato-febril-puncion-fallida-antibiotico-parenteral.svg",
    alt: "Flujograma: Neonato de 2 semanas con fiebre, irritabilidad y succión débil en quien no se logra la punción lumbar: iniciar antibióticos parenterales sin esperar"
  },
  "SP-088": {
    titulo: "Ante transmisión de dengue, el médico jefe convoca al alcalde y a instituciones públicas y privadas: intersectorialidad",
    imagen: "flujogramas/escenario-iii-dengue-alcalde-intersectorialidad.svg",
    alt: "Flujograma: Ante transmisión de dengue, el médico jefe convoca al alcalde y a instituciones públicas y privadas: intersectorialidad"
  },
  "END-035": {
    titulo: "Mujer con dolor cervical que aumenta al tragar, tirotoxicosis, tiroides dolorosa, VSG alta y anticuerpos negativos tras una faringitis: tiroiditis subaguda de De Quervain",
    imagen: "flujogramas/cervicalgia-post-faringitis-vsg-58-de-quervain.svg",
    alt: "Flujograma: Mujer con dolor cervical que aumenta al tragar, tirotoxicosis, tiroides dolorosa, VSG alta y anticuerpos negativos tras una faringitis: tiroiditis subaguda de De Quervain"
  },
  "PSI-021": {
    titulo: "Puérpera de 22 días con tristeza, llanto, miedo, sensación de no poder cuidar a su bebé e ideas de autolesión: depresión posparto",
    imagen: "flujogramas/puerpera-22-dias-tristeza-autolesion-depresion-posparto.svg",
    alt: "Flujograma: Puérpera de 22 días con tristeza, llanto, miedo, sensación de no poder cuidar a su bebé e ideas de autolesión: depresión posparto"
  },
  "NEF-049": {
    titulo: "Cálculo vesical grande y sintomático que no responde a medidas conservadoras: cistoscopía con litotricia láser",
    imagen: "flujogramas/litiasis-vesical-grande-cistolitotricia-laser.svg",
    alt: "Flujograma: Cálculo vesical grande y sintomático que no responde a medidas conservadoras: cistoscopía con litotricia láser"
  },
  "GIN-122": {
    titulo: "Gestante de 11 semanas con vómitos incoercibles, pérdida de peso, deshidratación, cetonuria e hiponatremia: hiperémesis gravídica",
    imagen: "flujogramas/vomitos-incoercibles-cetonuria-hiponatremia-hiperemesis.svg",
    alt: "Flujograma: Gestante de 11 semanas con vómitos incoercibles, pérdida de peso, deshidratación, cetonuria e hiponatremia: hiperémesis gravídica"
  },
  "OFT-030": {
    titulo: "Al pasar una sonda nasogástrica, lo que más sangra es el tabique nasal anterior (plexo de Kiesselbach)",
    imagen: "flujogramas/sonda-nasogastrica-sangrado-tabique-anterior-kiesselbach.svg",
    alt: "Flujograma: Al pasar una sonda nasogástrica, lo que más sangra es el tabique nasal anterior (plexo de Kiesselbach)"
  },
  "PED-128": {
    titulo: "Niño con otitis media aguda que no mejoró con azitromicina y antecedente de urticaria leve con amoxicilina: cefdinir",
    imagen: "flujogramas/otitis-media-alergia-leve-amoxicilina-cefdinir.svg",
    alt: "Flujograma: Niño con otitis media aguda que no mejoró con azitromicina y antecedente de urticaria leve con amoxicilina: cefdinir"
  },
  "TRA-023": {
    titulo: "Caída sobre la mano extendida con fractura del escafoides: su irrigación viene de la arteria radial, por eso puede necrosarse",
    imagen: "flujogramas/caida-mano-extendida-escafoides-arteria-radial.svg",
    alt: "Flujograma: Caída sobre la mano extendida con fractura del escafoides: su irrigación viene de la arteria radial, por eso puede necrosarse"
  },
  "NEF-050": {
    titulo: "Mujer con 8 meses de cansancio, HTA, anemia de 7,8, edema y creatinina de 5: enfermedad renal crónica",
    imagen: "flujogramas/creatinina-5-anemia-8-meses-enfermedad-renal-cronica.svg",
    alt: "Flujograma: Mujer con 8 meses de cansancio, HTA, anemia de 7,8, edema y creatinina de 5: enfermedad renal crónica"
  },
  "GAS-046": {
    titulo: "HBsAg (+), IgM anti-HBc (+), anti-HBc total (+) y anti-HBs (−): hepatitis B aguda",
    imagen: "flujogramas/hbsag-igm-antihbc-positivos-hepatitis-b-aguda.svg",
    alt: "Flujograma: HBsAg (+), IgM anti-HBc (+), anti-HBc total (+) y anti-HBs (−): hepatitis B aguda"
  },
  "CAR-049": {
    titulo: "Fibrilación auricular a 187 por minuto con PA 70/30, dolor torácico y diaforesis: inestable, cardioversión eléctrica sincronizada",
    imagen: "flujogramas/fa-pa-70-30-dolor-toracico-cardioversion-electrica.svg",
    alt: "Flujograma: Fibrilación auricular a 187 por minuto con PA 70/30, dolor torácico y diaforesis: inestable, cardioversión eléctrica sincronizada"
  },
  "PSI-022": {
    titulo: "Mujer con episodios bruscos de palpitaciones, ahogo, sudor y miedo a morir, sin causa aparente: ataque de pánico",
    imagen: "flujogramas/palpitaciones-ahogo-muerte-inminente-ataque-panico.svg",
    alt: "Flujograma: Mujer con episodios bruscos de palpitaciones, ahogo, sudor y miedo a morir, sin causa aparente: ataque de pánico"
  },
  "NEU-032": {
    titulo: "Mujer en quimioterapia con disnea súbita, dolor torácico, hemoptisis, taquicardia y signos de sobrecarga del ventrículo derecho: tromboembolia pulmonar",
    imagen: "flujogramas/quimioterapia-disnea-subita-hemoptisis-tromboembolia.svg",
    alt: "Flujograma: Mujer en quimioterapia con disnea súbita, dolor torácico, hemoptisis, taquicardia y signos de sobrecarga del ventrículo derecho: tromboembolia pulmonar"
  },
  "OFT-031": {
    titulo: "Para bajar la presión intraocular en el glaucoma se usan betabloqueantes tópicos como el timolol",
    imagen: "flujogramas/glaucoma-betabloqueante-topico-timolol.svg",
    alt: "Flujograma: Para bajar la presión intraocular en el glaucoma se usan betabloqueantes tópicos como el timolol"
  },
  "NEF-051": {
    titulo: "Adolescente con hematuria «agua de lavado de carne», oliguria, HTA y edema 3 semanas tras una amigdalitis: glomerulonefritis postestreptocócica, furosemida",
    imagen: "flujogramas/orina-lavado-carne-amigdalitis-edema-furosemida.svg",
    alt: "Flujograma: Adolescente con hematuria «agua de lavado de carne», oliguria, HTA y edema 3 semanas tras una amigdalitis: glomerulonefritis postestreptocócica, furosemida"
  },
  "SP-089": {
    titulo: "Adulta mayor hipertensa atendida cada 3 meses por el mismo médico durante años: atributo de longitudinalidad de la atención primaria",
    imagen: "flujogramas/hipertensa-mismo-medico-5-anos-longitudinalidad.svg",
    alt: "Flujograma: Adulta mayor hipertensa atendida cada 3 meses por el mismo médico durante años: atributo de longitudinalidad de la atención primaria"
  },
  "GIN-123": {
    titulo: "Gestante asintomática con urocultivo de E. coli > 100 000 UFC/mL: bacteriuria asintomática, tratar con nitrofurantoína",
    imagen: "flujogramas/gestante-8-semanas-bacteriuria-asintomatica-nitrofurantoina.svg",
    alt: "Flujograma: Gestante asintomática con urocultivo de E. coli > 100 000 UFC/mL: bacteriuria asintomática, tratar con nitrofurantoína"
  },
  "CIR-065": {
    titulo: "Anciana con 4 costillas fracturadas en dos sitios, movimiento paradójico, FR 30 y SatO₂ 90 %: tórax inestable con falla respiratoria, intubar y ventilar",
    imagen: "flujogramas/fracturas-costales-dobles-movimiento-paradojal-intubacion.svg",
    alt: "Flujograma: Anciana con 4 costillas fracturadas en dos sitios, movimiento paradójico, FR 30 y SatO₂ 90 %: tórax inestable con falla respiratoria, intubar y ventilar"
  },
  "PSI-023": {
    titulo: "Paciente bipolar con litio de 6 mEq/L, convulsiones, alteración de conciencia, ataxia, arritmia y creatinina alta: intoxicación grave, hemodiálisis",
    imagen: "flujogramas/litio-6-convulsiones-hemodialisis.svg",
    alt: "Flujograma: Paciente bipolar con litio de 6 mEq/L, convulsiones, alteración de conciencia, ataxia, arritmia y creatinina alta: intoxicación grave, hemodiálisis"
  },
  "SP-090": {
    titulo: "Persona sana con PPD positivo: el bacilo de la TB es causa necesaria (sin él no hay TB) pero no suficiente (infectado no es lo mismo que enfermo)",
    imagen: "flujogramas/ppd-11-mm-sano-causa-necesaria-no-suficiente.svg",
    alt: "Flujograma: Persona sana con PPD positivo: el bacilo de la TB es causa necesaria (sin él no hay TB) pero no suficiente (infectado no es lo mismo que enfermo)"
  },
  "GIN-124": {
    titulo: "Feto de 29 semanas con peso en percentil 8 y Doppler umbilical alterado: restricción del crecimiento temprana",
    imagen: "flujogramas/29-semanas-percentil-8-doppler-umbilical-rciu-temprano.svg",
    alt: "Flujograma: Feto de 29 semanas con peso en percentil 8 y Doppler umbilical alterado: restricción del crecimiento temprana"
  },
  "NEF-052": {
    titulo: "Anciana hipertensa que toma ibuprofeno 10 días y presenta oliguria, creatinina 3, K 6 y cilindros granulosos: lesión renal por AINE (nefropatía tóxica)",
    imagen: "flujogramas/ibuprofeno-oliguria-creatinina-3-nefropatia-toxica.svg",
    alt: "Flujograma: Anciana hipertensa que toma ibuprofeno 10 días y presenta oliguria, creatinina 3, K 6 y cilindros granulosos: lesión renal por AINE (nefropatía tóxica)"
  },
  "TRA-024": {
    titulo: "La complicación más común de las fracturas abiertas es la infección",
    imagen: "flujogramas/fractura-abierta-complicacion-infeccion.svg",
    alt: "Flujograma: La complicación más común de las fracturas abiertas es la infección"
  },
  "GIN-125": {
    titulo: "Gestante a término en fase latente con líquido meconial espeso y latidos fetales de 100: sufrimiento fetal, cesárea de emergencia",
    imagen: "flujogramas/meconio-espeso-lcf-100-cesarea-emergencia.svg",
    alt: "Flujograma: Gestante a término en fase latente con líquido meconial espeso y latidos fetales de 100: sufrimiento fetal, cesárea de emergencia"
  },
  "NEU-033": {
    titulo: "Alpinista bajado de 5530 m a Huaraz con disnea, esputo espumoso, SatO₂ 75 % e infiltrados alveolares sin cardiomegalia: edema pulmonar de altura, oxígeno",
    imagen: "flujogramas/alpinista-esputo-espumoso-sato2-75-oxigeno.svg",
    alt: "Flujograma: Alpinista bajado de 5530 m a Huaraz con disnea, esputo espumoso, SatO₂ 75 % e infiltrados alveolares sin cardiomegalia: edema pulmonar de altura, oxígeno"
  },
  "CIR-066": {
    titulo: "Politraumatizado con hipotensión, FC normal, pulsos buenos, FAST negativa y que no mejora con cristaloides: choque neurogénico",
    imagen: "flujogramas/motociclista-hipotension-fc-72-sin-sangrado-neurogenico.svg",
    alt: "Flujograma: Politraumatizado con hipotensión, FC normal, pulsos buenos, FAST negativa y que no mejora con cristaloides: choque neurogénico"
  },
  "PED-129": {
    titulo: "Lactante que convive con aves, con diarrea con moco y sangre, fiebre, deshidratación y bacilo curvo gramnegativo: disentería por Campylobacter, SRO y azitromicina",
    imagen: "flujogramas/crianza-aves-disenteria-bacilo-curvo-campylobacter-azitromicina.svg",
    alt: "Flujograma: Lactante que convive con aves, con diarrea con moco y sangre, fiebre, deshidratación y bacilo curvo gramnegativo: disentería por Campylobacter, SRO y azitromicina"
  },
  "CB-044": {
    titulo: "Tras una discusión aparecen taquicardia y presión alta: reacción simpática de lucha o huida mediada por noradrenalina y adrenalina",
    imagen: "flujogramas/discusion-taquicardia-hipertension-catecolaminas.svg",
    alt: "Flujograma: Tras una discusión aparecen taquicardia y presión alta: reacción simpática de lucha o huida mediada por noradrenalina y adrenalina"
  },
  "NEU-034": {
    titulo: "Paciente con TB pulmonar BK (+++) que va a iniciar tratamiento: pedir perfil hepático basal (además del tamizaje de VIH)",
    imagen: "flujogramas/tb-bk-positivo-perfil-hepatico-antes-tratamiento.svg",
    alt: "Flujograma: Paciente con TB pulmonar BK (+++) que va a iniciar tratamiento: pedir perfil hepático basal (además del tamizaje de VIH)"
  },
  "SP-091": {
    titulo: "El primer caso de un problema bajo vigilancia que identifica el servicio de salud se llama caso índice",
    imagen: "flujogramas/primer-caso-identificado-servicio-caso-indice.svg",
    alt: "Flujograma: El primer caso de un problema bajo vigilancia que identifica el servicio de salud se llama caso índice"
  },
  "OFT-032": {
    titulo: "Lactante de 18 meses con reflejo pupilar blanco (leucocoria) y estrabismo: retinoblastoma hasta demostrar lo contrario",
    imagen: "flujogramas/lactante-leucocoria-estrabismo-retinoblastoma.svg",
    alt: "Flujograma: Lactante de 18 meses con reflejo pupilar blanco (leucocoria) y estrabismo: retinoblastoma hasta demostrar lo contrario"
  },
  "GIN-126": {
    titulo: "Gestante a término con PA 160/110, dolor en hipocondrio derecho, plaquetas 90 000, transaminasas y DHL altas: síndrome HELLP",
    imagen: "flujogramas/pa-160-110-plaquetas-90000-dhl-700-hellp.svg",
    alt: "Flujograma: Gestante a término con PA 160/110, dolor en hipocondrio derecho, plaquetas 90 000, transaminasas y DHL altas: síndrome HELLP"
  },
  "INF-063": {
    titulo: "Paciente con VIH, CD4 100 y neumonía por Pneumocystis con PaO₂ 60 mmHg: además del cotrimoxazol, prednisona",
    imagen: "flujogramas/vih-cd4-100-pao2-60-pneumocystis-prednisona.svg",
    alt: "Flujograma: Paciente con VIH, CD4 100 y neumonía por Pneumocystis con PaO₂ 60 mmHg: además del cotrimoxazol, prednisona"
  },
  "PED-130": {
    titulo: "Lactante con VIH sintomático: las vacunas inactivadas se aplican normalmente; las de virus vivos (como rotavirus) requieren evaluación médica, y la BCG no se aplica",
    imagen: "flujogramas/lactante-vih-sintomatico-rotavirus-prescripcion.svg",
    alt: "Flujograma: Lactante con VIH sintomático: las vacunas inactivadas se aplican normalmente; las de virus vivos (como rotavirus) requieren evaluación médica, y la BCG no se aplica"
  },
  "CIR-067": {
    titulo: "Hallazgo en apendicectomía de un tumor de 2 cm en la base del apéndice que compromete el mesenterio: hemicolectomía derecha",
    imagen: "flujogramas/tumor-base-apendicular-2-cm-mesenterio-hemicolectomia.svg",
    alt: "Flujograma: Hallazgo en apendicectomía de un tumor de 2 cm en la base del apéndice que compromete el mesenterio: hemicolectomía derecha"
  },
  "PSI-024": {
    titulo: "Paciente con haloperidol que no puede quedarse quieto y camina todo el tiempo: acatisia, tratar con propranolol",
    imagen: "flujogramas/haloperidol-no-puede-estar-quieto-acatisia-propranolol.svg",
    alt: "Flujograma: Paciente con haloperidol que no puede quedarse quieto y camina todo el tiempo: acatisia, tratar con propranolol"
  },
  "CIR-068": {
    titulo: "Sangrado al defecar por hemorroides internas que no salen del ano (grado I), que no mejoran con el manejo médico: coagulación infrarroja",
    imagen: "flujogramas/sangrado-defecar-no-prolapsa-coagulacion-infrarroja.svg",
    alt: "Flujograma: Sangrado al defecar por hemorroides internas que no salen del ano (grado I), que no mejoran con el manejo médico: coagulación infrarroja"
  },
  "END-036": {
    titulo: "Choque séptico que no responde a líquidos ni vasopresores, con cortisol bajo, ACTH alta e hiponatremia: insuficiencia suprarrenal primaria",
    imagen: "flujogramas/choque-septico-refractario-cortisol-bajo-acth-alta.svg",
    alt: "Flujograma: Choque séptico que no responde a líquidos ni vasopresores, con cortisol bajo, ACTH alta e hiponatremia: insuficiencia suprarrenal primaria"
  },
  "CIR-069": {
    titulo: "Dolor anal intenso al defecar con sangrado, espasmo y desgarro en la línea media posterior: fisura anal aguda, ablandadores y baños de asiento",
    imagen: "flujogramas/dolor-intenso-defecar-desgarro-posterior-fisura-anal.svg",
    alt: "Flujograma: Dolor anal intenso al defecar con sangrado, espasmo y desgarro en la línea media posterior: fisura anal aguda, ablandadores y baños de asiento"
  },
  "NRL-036": {
    titulo: "TEC grave en coma con rigidez de decorticación (brazos flexionados, piernas extendidas): lesión por encima del mesencéfalo (hemisferios cerebrales)",
    imagen: "flujogramas/tec-grave-coma-rigidez-decorticacion-hemisferios.svg",
    alt: "Flujograma: TEC grave en coma con rigidez de decorticación (brazos flexionados, piernas extendidas): lesión por encima del mesencéfalo (hemisferios cerebrales)"
  },
  "PED-131": {
    titulo: "Preescolar con fiebre, disuria y polaquiuria con urocultivo de E. coli BLEE: el antibiótico indicado es un carbapenem (meropenem)",
    imagen: "flujogramas/preescolar-itu-ecoli-blee-meropenem.svg",
    alt: "Flujograma: Preescolar con fiebre, disuria y polaquiuria con urocultivo de E. coli BLEE: el antibiótico indicado es un carbapenem (meropenem)"
  },
  "INF-064": {
    titulo: "Adolescente de la selva con fiebre paroxística cuartana, escalofríos, sudoración, anemia y hepatoesplenomegalia: malaria",
    imagen: "flujogramas/selva-fiebre-cuartana-esplenomegalia-malaria.svg",
    alt: "Flujograma: Adolescente de la selva con fiebre paroxística cuartana, escalofríos, sudoración, anemia y hepatoesplenomegalia: malaria"
  },
  "CAR-050": {
    titulo: "Joven con dolor torácico que aumenta al inspirar, mejora inclinado hacia adelante, irradia al trapecio, con frote y ST elevado difuso: pericarditis aguda",
    imagen: "flujogramas/dolor-pleuritico-alivia-inclinado-frote-pericarditis.svg",
    alt: "Flujograma: Joven con dolor torácico que aumenta al inspirar, mejora inclinado hacia adelante, irradia al trapecio, con frote y ST elevado difuso: pericarditis aguda"
  },
  "HEM-023": {
    titulo: "Paciente con leucocitos 400, Hb 5 y plaquetas 3000 (neutropenia profunda): aislamiento inverso (protector) para no contagiarla",
    imagen: "flujogramas/leucocitos-400-fiebre-aislamiento-inverso.svg",
    alt: "Flujograma: Paciente con leucocitos 400, Hb 5 y plaquetas 3000 (neutropenia profunda): aislamiento inverso (protector) para no contagiarla"
  },
  "NEF-053": {
    titulo: "Anciano fumador con síntomas urinarios, dolor óseo en caderas, próstata indurada e irregular y PSA 8: sospecha de cáncer de próstata, biopsia",
    imagen: "flujogramas/prostata-indurada-psa-8-biopsia-transrectal.svg",
    alt: "Flujograma: Anciano fumador con síntomas urinarios, dolor óseo en caderas, próstata indurada e irregular y PSA 8: sospecha de cáncer de próstata, biopsia"
  },
  "CB-045": {
    titulo: "En el hipertiroidismo sube el metabolismo basal: más consumo de oxígeno y de calorías, calor, taquicardia y pérdida de peso",
    imagen: "flujogramas/hipertiroidismo-metabolismo-basal-aumentado.svg",
    alt: "Flujograma: En el hipertiroidismo sube el metabolismo basal: más consumo de oxígeno y de calorías, calor, taquicardia y pérdida de peso"
  },
  "NRL-037": {
    titulo: "Dolor al roce de la ropa (alodinia), sensación eléctrica y adormecimiento: dolor neuropático",
    imagen: "flujogramas/dolor-roce-ropa-electrico-neuropatico.svg",
    alt: "Flujograma: Dolor al roce de la ropa (alodinia), sensación eléctrica y adormecimiento: dolor neuropático"
  },
  "GIN-127": {
    titulo: "Gestante con IMC previo de 32 (obesidad) que ganó 12,5 kg: ganancia de peso excesiva (lo recomendado es 5 a 9 kg)",
    imagen: "flujogramas/obesa-imc-32-gano-125-kg-excesiva.svg",
    alt: "Flujograma: Gestante con IMC previo de 32 (obesidad) que ganó 12,5 kg: ganancia de peso excesiva (lo recomendado es 5 a 9 kg)"
  },
  "GAS-047": {
    titulo: "Posoperado con 7 transfusiones y hematoma retroperitoneal en resolución que hace ictericia con bilirrubina indirecta: reabsorción del hematoma",
    imagen: "flujogramas/hematoma-retroperitoneal-bilirrubina-indirecta-reabsorcion.svg",
    alt: "Flujograma: Posoperado con 7 transfusiones y hematoma retroperitoneal en resolución que hace ictericia con bilirrubina indirecta: reabsorción del hematoma"
  },
  "GIN-128": {
    titulo: "La vacuna Tdap se aplica en cada embarazo, de preferencia entre las semanas 27 y 36",
    imagen: "flujogramas/primer-control-vacuna-tdap-27-36-semanas.svg",
    alt: "Flujograma: La vacuna Tdap se aplica en cada embarazo, de preferencia entre las semanas 27 y 36"
  },
  "PED-132": {
    titulo: "La complicación más frecuente de la displasia broncopulmonar del prematuro es la hipertensión pulmonar",
    imagen: "flujogramas/displasia-broncopulmonar-hipertension-pulmonar.svg",
    alt: "Flujograma: La complicación más frecuente de la displasia broncopulmonar del prematuro es la hipertensión pulmonar"
  },
  "NEF-054": {
    titulo: "Adulto con dolor en flanco, masa palpable, creatinina alta y hermano con ERC: poliquistosis renal autosómica dominante",
    imagen: "flujogramas/hermano-erc-masa-flanco-creatinina-poliquistosis.svg",
    alt: "Flujograma: Adulto con dolor en flanco, masa palpable, creatinina alta y hermano con ERC: poliquistosis renal autosómica dominante"
  },
  "CB-046": {
    titulo: "La agenesia renal se origina por falla del metanefros (o de la yema ureteral que lo induce)",
    imagen: "flujogramas/agenesia-renal-unilateral-metanefros.svg",
    alt: "Flujograma: La agenesia renal se origina por falla del metanefros (o de la yema ureteral que lo induce)"
  },
  "HEM-024": {
    titulo: "Hemoglobina 18,6, hematocrito 58 %, trombocitosis y eritropoyetina BAJA: policitemia vera (la poliglobulia secundaria tiene EPO alta)",
    imagen: "flujogramas/hb-186-eritropoyetina-baja-plaquetas-policitemia-vera.svg",
    alt: "Flujograma: Hemoglobina 18,6, hematocrito 58 %, trombocitosis y eritropoyetina BAJA: policitemia vera (la poliglobulia secundaria tiene EPO alta)"
  },
  "END-037": {
    titulo: "Diabético en choque con acidosis metabólica de anión gap alto, lactato 10 y cetonas negativas: acidosis láctica",
    imagen: "flujogramas/dm1-lactato-10-cetonas-negativas-acidosis-lactica.svg",
    alt: "Flujograma: Diabético en choque con acidosis metabólica de anión gap alto, lactato 10 y cetonas negativas: acidosis láctica"
  },
  "NRL-038": {
    titulo: "En la distrofia muscular de Duchenne falta la distrofina, proteína que une el citoesqueleto del músculo a la membrana",
    imagen: "flujogramas/duchenne-distrofina-ausente.svg",
    alt: "Flujograma: En la distrofia muscular de Duchenne falta la distrofina, proteína que une el citoesqueleto del músculo a la membrana"
  },
  "END-038": {
    titulo: "Anciana con insuficiencia renal que toma metformina y presenta debilidad, náuseas, vómitos y disnea: acidosis láctica por metformina",
    imagen: "flujogramas/metformina-insuficiencia-renal-acidosis-lactica.svg",
    alt: "Flujograma: Anciana con insuficiencia renal que toma metformina y presenta debilidad, náuseas, vómitos y disnea: acidosis láctica por metformina"
  },
  "NEF-055": {
    titulo: "Tras la vasectomía quedan espermatozoides en la vía seminal: la esterilidad se confirma a los 3 meses con un espermatograma",
    imagen: "flujogramas/vasectomia-esterilidad-tres-meses.svg",
    alt: "Flujograma: Tras la vasectomía quedan espermatozoides en la vía seminal: la esterilidad se confirma a los 3 meses con un espermatograma"
  },
  "SP-092": {
    titulo: "Actividades educativas en la escuela sobre autocuidado y reconocimiento de la TB: promoción de la salud",
    imagen: "flujogramas/colegio-educacion-autocuidado-tuberculosis-promocion.svg",
    alt: "Flujograma: Actividades educativas en la escuela sobre autocuidado y reconocimiento de la TB: promoción de la salud"
  },
  "GIN-129": {
    titulo: "4 embarazos: un gemelar a las 34 semanas, un ectópico, una mola y uno a término, con 3 hijos vivos: G4P1223 según la clave",
    imagen: "flujogramas/gemelar-34-ectopico-mola-41-semanas-formula-obstetrica.svg",
    alt: "Flujograma: 4 embarazos: un gemelar a las 34 semanas, un ectópico, una mola y uno a término, con 3 hijos vivos: G4P1223 según la clave"
  },
  "NEF-056": {
    titulo: "Paciente en diálisis con eritropoyetina y Hb 8,7, ferritina 56 y saturación de transferrina 10 %: falta hierro, darlo y mantener la eritropoyetina",
    imagen: "flujogramas/erc-hemodialisis-ferritina-56-ist-10-hierro-mantener-epo.svg",
    alt: "Flujograma: Paciente en diálisis con eritropoyetina y Hb 8,7, ferritina 56 y saturación de transferrina 10 %: falta hierro, darlo y mantener la eritropoyetina"
  },
  "PED-133": {
    titulo: "Lactante picado por escorpión: la complicación principal es la falla cardiorrespiratoria (miocarditis y edema pulmonar)",
    imagen: "flujogramas/lactante-picadura-escorpion-falla-cardiorrespiratoria.svg",
    alt: "Flujograma: Lactante picado por escorpión: la complicación principal es la falla cardiorrespiratoria (miocarditis y edema pulmonar)"
  },
  "GIN-130": {
    titulo: "Primigesta en fase activa que pasa de 6 a 8 cm en 2 horas con descenso de la presentación: progresión adecuada, continuar el trabajo de parto",
    imagen: "flujogramas/dilatacion-6-a-8-en-2-horas-continuar-trabajo-parto.svg",
    alt: "Flujograma: Primigesta en fase activa que pasa de 6 a 8 cm en 2 horas con descenso de la presentación: progresión adecuada, continuar el trabajo de parto"
  },
  "PSI-025": {
    titulo: "12 meses de preocupación excesiva por todo, inquietud, irritabilidad, falta de concentración, tensión muscular e insomnio: trastorno de ansiedad generalizada",
    imagen: "flujogramas/preocupacion-12-meses-tension-insomnio-ansiedad-generalizada.svg",
    alt: "Flujograma: 12 meses de preocupación excesiva por todo, inquietud, irritabilidad, falta de concentración, tensión muscular e insomnio: trastorno de ansiedad generalizada"
  },
  "GIN-131": {
    titulo: "Al romper las membranas aparece sangrado profuso con caída rápida de los latidos fetales: rotura de vasa previa, cesárea de emergencia",
    imagen: "flujogramas/amniotomia-sangrado-profuso-bradicardia-vasa-previa-cesarea.svg",
    alt: "Flujograma: Al romper las membranas aparece sangrado profuso con caída rápida de los latidos fetales: rotura de vasa previa, cesárea de emergencia"
  },
  "PED-134": {
    titulo: "Prematuro de 31 semanas con dificultad respiratoria y Rx en vidrio esmerilado con broncograma: membrana hialina; la cardiopatía más asociada es el ductus arterioso persistente",
    imagen: "flujogramas/prematuro-31-semanas-membrana-hialina-ductus.svg",
    alt: "Flujograma: Prematuro de 31 semanas con dificultad respiratoria y Rx en vidrio esmerilado con broncograma: membrana hialina; la cardiopatía más asociada es el ductus arterioso persistente"
  },
  "END-039": {
    titulo: "Mujer con desmayos repetidos, sudor y confusión, glucosa baja con insulina alta y nódulo pancreático de 2 cm: insulinoma, resección quirúrgica",
    imagen: "flujogramas/hipoglucemia-insulina-alta-nodulo-pancreatico-reseccion.svg",
    alt: "Flujograma: Mujer con desmayos repetidos, sudor y confusión, glucosa baja con insulina alta y nódulo pancreático de 2 cm: insulinoma, resección quirúrgica"
  },
  "SP-093": {
    titulo: "Adolescentes mujeres con Hb > 12 g/dL en el colegio: suplementación preventiva con hierro y ácido fólico",
    imagen: "flujogramas/adolescentes-hb-mayor-12-hierro-acido-folico.svg",
    alt: "Flujograma: Adolescentes mujeres con Hb > 12 g/dL en el colegio: suplementación preventiva con hierro y ácido fólico"
  },
  "NEF-057": {
    titulo: "Diabético hipertenso con caída de la diuresis y creatinina de 2,5 dos días después de una TC con contraste: lesión renal por contraste, hidratación EV",
    imagen: "flujogramas/tc-contraste-diabetico-creatinina-25-hidratacion.svg",
    alt: "Flujograma: Diabético hipertenso con caída de la diuresis y creatinina de 2,5 dos días después de una TC con contraste: lesión renal por contraste, hidratación EV"
  },
  "INF-065": {
    titulo: "Paciente con VIH que inicia el tratamiento antirretroviral: la eficacia se controla con la carga viral en plasma",
    imagen: "flujogramas/vih-inicio-tar-respuesta-carga-viral.svg",
    alt: "Flujograma: Paciente con VIH que inicia el tratamiento antirretroviral: la eficacia se controla con la carga viral en plasma"
  },
  "NEU-035": {
    titulo: "EPOC descompensado con pH 7,32 y pCO₂ 60 (acidosis respiratoria moderada): ventilación no invasiva",
    imagen: "flujogramas/epoc-ph-732-pco2-60-ventilacion-no-invasiva.svg",
    alt: "Flujograma: EPOC descompensado con pH 7,32 y pCO₂ 60 (acidosis respiratoria moderada): ventilación no invasiva"
  },
  "PSI-026": {
    titulo: "Joven agitado con ideas de persecución, hipertensión, taquicardia, fiebre, midriasis y perforación del tabique nasal: intoxicación por cocaína",
    imagen: "flujogramas/agitacion-paranoia-midriasis-tabique-perforado-cocaina.svg",
    alt: "Flujograma: Joven agitado con ideas de persecución, hipertensión, taquicardia, fiebre, midriasis y perforación del tabique nasal: intoxicación por cocaína"
  },
  "CIR-070": {
    titulo: "Quemadura por alto voltaje con ruidos cardíacos arrítmicos: el primer examen es el electrocardiograma",
    imagen: "flujogramas/alto-voltaje-mano-ruidos-arritmicos-ecg.svg",
    alt: "Flujograma: Quemadura por alto voltaje con ruidos cardíacos arrítmicos: el primer examen es el electrocardiograma"
  },
  "NEF-058": {
    titulo: "Cólico renal que cede con cálculo menor de 6 mm en el uréter distal: tratamiento médico expulsivo",
    imagen: "flujogramas/calculo-ureteral-distal-menor-6-mm-terapia-expulsiva.svg",
    alt: "Flujograma: Cólico renal que cede con cálculo menor de 6 mm en el uréter distal: tratamiento médico expulsivo"
  },
  "INF-066": {
    titulo: "Herida sucia por fierro oxidado en un adulto con vacunación completa hace 9 años: aplicar toxoide (refuerzo), sin inmunoglobulina",
    imagen: "flujogramas/herida-fierro-oxidado-vacuna-9-anos-toxoide.svg",
    alt: "Flujograma: Herida sucia por fierro oxidado en un adulto con vacunación completa hace 9 años: aplicar toxoide (refuerzo), sin inmunoglobulina"
  },
  "PED-135": {
    titulo: "En el parto sin complicaciones, el contacto piel a piel se inicia de inmediato, dentro de la primera hora",
    imagen: "flujogramas/parto-vaginal-contacto-piel-a-piel-primera-hora.svg",
    alt: "Flujograma: En el parto sin complicaciones, el contacto piel a piel se inicia de inmediato, dentro de la primera hora"
  },
  "HEM-025": {
    titulo: "Preescolar con gingivorragia, petequias en piel y boca, plaquetas 12 000 y lo demás normal: PTI con sangrado mucoso, inmunoglobulina",
    imagen: "flujogramas/nino-gingivorragia-plaquetas-12000-inmunoglobulina.svg",
    alt: "Flujograma: Preescolar con gingivorragia, petequias en piel y boca, plaquetas 12 000 y lo demás normal: PTI con sangrado mucoso, inmunoglobulina"
  },
  "CB-047": {
    titulo: "Reciclador de baterías con meses de cefalea, diarrea, fatiga y artralgias: intoxicación crónica por plomo",
    imagen: "flujogramas/reciclador-baterias-cefalea-diarrea-plomo.svg",
    alt: "Flujograma: Reciclador de baterías con meses de cefalea, diarrea, fatiga y artralgias: intoxicación crónica por plomo"
  },
  "CIR-071": {
    titulo: "Quemadura por agua caliente con piel roja que se blanquea al presionar y ampollas: espesor parcial superficial (2.º grado superficial)",
    imagen: "flujogramas/agua-caliente-ampollas-blanquea-espesor-parcial-superficial.svg",
    alt: "Flujograma: Quemadura por agua caliente con piel roja que se blanquea al presionar y ampollas: espesor parcial superficial (2.º grado superficial)"
  },
  "CB-048": {
    titulo: "Tras tratar con mucha atropina una intoxicación por organofosforados aparecen piel roja, caliente y seca, midriasis, taquicardia, íleo, globo vesical y agitación: toxicidad anticolinérgica",
    imagen: "flujogramas/organofosforado-atropina-piel-seca-midriasis-anticolinergico.svg",
    alt: "Flujograma: Tras tratar con mucha atropina una intoxicación por organofosforados aparecen piel roja, caliente y seca, midriasis, taquicardia, íleo, globo vesical y agitación: toxicidad anticolinérgica"
  },
  "SP-094": {
    titulo: "Acupuntura asociada a la quimioterapia para aliviar efectos adversos: medicina complementaria",
    imagen: "flujogramas/oncologia-acupuntura-medicina-complementaria.svg",
    alt: "Flujograma: Acupuntura asociada a la quimioterapia para aliviar efectos adversos: medicina complementaria"
  },
  "CIR-072": {
    titulo: "Trauma con hipotensión, hiperresonancia, murmullo abolido y tráquea desviada al lado opuesto: neumotórax a tensión, descompresión inmediata con aguja",
    imagen: "flujogramas/hiperresonancia-desviacion-traqueal-hipotension-aguja.svg",
    alt: "Flujograma: Trauma con hipotensión, hiperresonancia, murmullo abolido y tráquea desviada al lado opuesto: neumotórax a tensión, descompresión inmediata con aguja"
  },
  "REU-037": {
    titulo: "Joven asmática con años de prurito y piel seca, descamada y fisurada en pliegues de codos, rodillas, cuello y muñecas: dermatitis atópica",
    imagen: "flujogramas/prurito-pliegues-asma-piel-seca-dermatitis-atopica.svg",
    alt: "Flujograma: Joven asmática con años de prurito y piel seca, descamada y fisurada en pliegues de codos, rodillas, cuello y muñecas: dermatitis atópica"
  },
  "NEF-059": {
    titulo: "Mujer joven no gestante con disuria, polaquiuria y dolor perineal, sin fiebre: cistitis no complicada, antibiótico oral empírico",
    imagen: "flujogramas/mujer-joven-disuria-sin-fiebre-cistitis-no-complicada.svg",
    alt: "Flujograma: Mujer joven no gestante con disuria, polaquiuria y dolor perineal, sin fiebre: cistitis no complicada, antibiótico oral empírico"
  },
  "END-040": {
    titulo: "Mujer joven con galactorrea y amenorrea de 3 meses: hiperprolactinemia",
    imagen: "flujogramas/galactorrea-amenorrea-hiperprolactinemia.svg",
    alt: "Flujograma: Mujer joven con galactorrea y amenorrea de 3 meses: hiperprolactinemia"
  },
  "CB-049": {
    titulo: "Niño picado en el campo con dolor local, piloerección, punto blanco con halo rojo y luego espasmos musculares dolorosos, sudor, taquicardia e HTA: latrodectismo (viuda negra)",
    imagen: "flujogramas/nino-dolor-muslo-espasmos-diaforesis-latrodectus.svg",
    alt: "Flujograma: Niño picado en el campo con dolor local, piloerección, punto blanco con halo rojo y luego espasmos musculares dolorosos, sudor, taquicardia e HTA: latrodectismo (viuda negra)"
  },
  "GIN-132": {
    titulo: "Gestante Rh negativa sensibilizada: la anemia fetal se busca con el pico sistólico de la arteria cerebral media en el Doppler",
    imagen: "flujogramas/incompatibilidad-rh-anemia-fetal-cerebral-media.svg",
    alt: "Flujograma: Gestante Rh negativa sensibilizada: la anemia fetal se busca con el pico sistólico de la arteria cerebral media en el Doppler"
  },
  "NEF-060": {
    titulo: "Paciente séptico e hipotenso con oliguria, sodio urinario 8, FeNa 0,4 % y orina concentrada: lesión prerrenal; el riñón se defiende contrayendo la arteriola eferente",
    imagen: "flujogramas/neumonia-hipotension-fena-04-vasoconstriccion-eferente.svg",
    alt: "Flujograma: Paciente séptico e hipotenso con oliguria, sodio urinario 8, FeNa 0,4 % y orina concentrada: lesión prerrenal; el riñón se defiende contrayendo la arteriola eferente"
  },
  "REU-038": {
    titulo: "Fibromialgia con dolor e insomnio que persisten pese a terapia física y conductual: agregar amitriptilina",
    imagen: "flujogramas/fibromialgia-insomnio-persistente-amitriptilina.svg",
    alt: "Flujograma: Fibromialgia con dolor e insomnio que persisten pese a terapia física y conductual: agregar amitriptilina"
  },
  "NEU-036": {
    titulo: "Obeso con ronquido y pausas respiratorias nocturnas por años que hace un ictus: apnea obstructiva del sueño, polisomnografía",
    imagen: "flujogramas/ronca-apneas-imc-35-acv-polisomnografia.svg",
    alt: "Flujograma: Obeso con ronquido y pausas respiratorias nocturnas por años que hace un ictus: apnea obstructiva del sueño, polisomnografía"
  },
  "CIR-073": {
    titulo: "Anciano diabético y alcohólico con celulitis perineal y escrotal, necrosis, crepitación y fiebre: fascitis necrotizante del periné (gangrena de Fournier)",
    imagen: "flujogramas/diabetico-perine-escroto-necrosis-crepitacion-fournier.svg",
    alt: "Flujograma: Anciano diabético y alcohólico con celulitis perineal y escrotal, necrosis, crepitación y fiebre: fascitis necrotizante del periné (gangrena de Fournier)"
  },
  "GIN-133": {
    titulo: "Puérpera con VIH en TAR que desea lactar: en el Perú la norma contraindica la lactancia materna y da fórmula",
    imagen: "flujogramas/puerpera-vih-tar-desea-lactar-contraindicar.svg",
    alt: "Flujograma: Puérpera con VIH en TAR que desea lactar: en el Perú la norma contraindica la lactancia materna y da fórmula"
  },
  "GIN-134": {
    titulo: "Gestante de talla baja, primigesta joven, a las 36 semanas en inicio de trabajo de parto con feto en podálica: cesárea",
    imagen: "flujogramas/podalica-primigesta-talla-150-trabajo-parto-cesarea.svg",
    alt: "Flujograma: Gestante de talla baja, primigesta joven, a las 36 semanas en inicio de trabajo de parto con feto en podálica: cesárea"
  },
  "SP-095": {
    titulo: "Neumonías infantiles que aumentan cada año en los meses fríos: variación estacional",
    imagen: "flujogramas/neumonia-meses-frios-variacion-estacional.svg",
    alt: "Flujograma: Neumonías infantiles que aumentan cada año en los meses fríos: variación estacional"
  },
  "TRA-025": {
    titulo: "Anciano postrado con fractura de cadera: la complicación más probable es la trombosis venosa profunda",
    imagen: "flujogramas/anciano-fractura-cadera-postrado-tvp.svg",
    alt: "Flujograma: Anciano postrado con fractura de cadera: la complicación más probable es la trombosis venosa profunda"
  },
  "GIN-135": {
    titulo: "Sangrado vaginal indoloro a las 34 semanas con el borde de la placenta a 1 cm del OCI, sin cubrirlo: placenta de implantación baja",
    imagen: "flujogramas/borde-placentario-1-cm-oci-implantacion-baja.svg",
    alt: "Flujograma: Sangrado vaginal indoloro a las 34 semanas con el borde de la placenta a 1 cm del OCI, sin cubrirlo: placenta de implantación baja"
  },
  "NEF-061": {
    titulo: "Varón de 49 años con síntomas urinarios, PSA 5,9 y cociente PSA libre/total de 11 %: alto riesgo de cáncer, biopsia guiada por ecografía",
    imagen: "flujogramas/psa-59-libre-total-11-biopsia.svg",
    alt: "Flujograma: Varón de 49 años con síntomas urinarios, PSA 5,9 y cociente PSA libre/total de 11 %: alto riesgo de cáncer, biopsia guiada por ecografía"
  },
  "GAS-048": {
    titulo: "Niño con náuseas, distensión, diarrea y gases tras tomar lácteos: intolerancia a la lactosa por déficit de lactasa",
    imagen: "flujogramas/lacteos-distension-diarrea-lactasa.svg",
    alt: "Flujograma: Niño con náuseas, distensión, diarrea y gases tras tomar lácteos: intolerancia a la lactosa por déficit de lactasa"
  },
  "INF-067": {
    titulo: "Fiebre amarilla confirmada con fiebre, cefalea, mialgias, náuseas e ictericia: la ictericia indica la fase tóxica, grave",
    imagen: "flujogramas/satipo-fiebre-amarilla-ictericia-gravedad.svg",
    alt: "Flujograma: Fiebre amarilla confirmada con fiebre, cefalea, mialgias, náuseas e ictericia: la ictericia indica la fase tóxica, grave"
  },
  "PED-136": {
    titulo: "Niño con varicela que desarrolla una placa roja, caliente, fluctuante y dolorosa con leucocitosis: sobreinfección bacteriana (celulitis o absceso), oxacilina",
    imagen: "flujogramas/varicela-placa-fluctuante-sobreinfeccion-oxacilina.svg",
    alt: "Flujograma: Niño con varicela que desarrolla una placa roja, caliente, fluctuante y dolorosa con leucocitosis: sobreinfección bacteriana (celulitis o absceso), oxacilina"
  },
  "SP-096": {
    titulo: "Balanzas mal calibradas que sobreestiman el peso en todos los niños: error sistemático (sesgo de medición)",
    imagen: "flujogramas/balanzas-descalibradas-sobreestiman-peso-error-sistematico.svg",
    alt: "Flujograma: Balanzas mal calibradas que sobreestiman el peso en todos los niños: error sistemático (sesgo de medición)"
  },
  "INF-068": {
    titulo: "Paciente con VIH avanzado que 3 semanas después de iniciar TAR (CD4 suben, carga viral baja) hace fiebre y adenopatías: síndrome de reconstitución inmune",
    imagen: "flujogramas/vih-tar-3-semanas-fiebre-adenopatias-reconstitucion-inmune.svg",
    alt: "Flujograma: Paciente con VIH avanzado que 3 semanas después de iniciar TAR (CD4 suben, carga viral baja) hace fiebre y adenopatías: síndrome de reconstitución inmune"
  },
  "NEU-037": {
    titulo: "Anciano con neumonía del lóbulo medio, FR 32, orientado y PA normal: CURB-65 de 2, hospitalizar en sala de medicina",
    imagen: "flujogramas/neumonia-69-anos-fr-32-curb65-2-hospitalizar.svg",
    alt: "Flujograma: Anciano con neumonía del lóbulo medio, FR 32, orientado y PA normal: CURB-65 de 2, hospitalizar en sala de medicina"
  },
  "TRA-026": {
    titulo: "Herida en el compartimento anterior de la pierna con parestesias y pie caído: lesión del nervio peroneo (profundo)",
    imagen: "flujogramas/herida-compartimento-anterior-pie-caido-peroneo.svg",
    alt: "Flujograma: Herida en el compartimento anterior de la pierna con parestesias y pie caído: lesión del nervio peroneo (profundo)"
  },
  "GIN-136": {
    titulo: "Gestante con tres abortos precoces seguidos y una trombosis venosa previa: síndrome antifosfolípido, pedir anticuerpos (anti-β2 glicoproteína I)",
    imagen: "flujogramas/tres-abortos-tvp-anti-b2-glicoproteina.svg",
    alt: "Flujograma: Gestante con tres abortos precoces seguidos y una trombosis venosa previa: síndrome antifosfolípido, pedir anticuerpos (anti-β2 glicoproteína I)"
  },
  "GIN-137": {
    titulo: "Mujer obesa con oligomenorrea desde la menarquia, acné, hirsutismo y acantosis nigricans que no logra embarazarse: síndrome de ovario poliquístico (hiperandrogénico)",
    imagen: "flujogramas/oligomenorrea-acne-acantosis-hirsutismo-ovario-poliquistico.svg",
    alt: "Flujograma: Mujer obesa con oligomenorrea desde la menarquia, acné, hirsutismo y acantosis nigricans que no logra embarazarse: síndrome de ovario poliquístico (hiperandrogénico)"
  },
  "PED-137": {
    titulo: "Lactante que nació a las 27 semanas, tuvo ventilación prolongada y a los 3 meses sigue con oxígeno, sibilancias y Rx con atrapamiento aéreo: displasia broncopulmonar",
    imagen: "flujogramas/prematuro-27-semanas-oxigeno-3-meses-displasia.svg",
    alt: "Flujograma: Lactante que nació a las 27 semanas, tuvo ventilación prolongada y a los 3 meses sigue con oxígeno, sibilancias y Rx con atrapamiento aéreo: displasia broncopulmonar"
  },
  "HEM-026": {
    titulo: "Niño de 3 años con una cromosomopatía y leucemia: el síndrome de Down es el que más se asocia a leucemia",
    imagen: "flujogramas/nino-cromosomopatia-leucemia-sindrome-down.svg",
    alt: "Flujograma: Niño de 3 años con una cromosomopatía y leucemia: el síndrome de Down es el que más se asocia a leucemia"
  },
  "REU-039": {
    titulo: "Obrero con úlcera de 2 cm en el labio inferior, de un año, bordes netos, base infiltrada y costra sanguinolenta: carcinoma espinocelular",
    imagen: "flujogramas/obrero-ulcera-labio-inferior-infiltrada-espinocelular.svg",
    alt: "Flujograma: Obrero con úlcera de 2 cm en el labio inferior, de un año, bordes netos, base infiltrada y costra sanguinolenta: carcinoma espinocelular"
  },
  "CIR-074": {
    titulo: "Herida de arma blanca periumbilical en un paciente estable, sin contractura y con leve reacción peritoneal: exploración local de la herida",
    imagen: "flujogramas/arma-blanca-periumbilical-estable-exploracion-local.svg",
    alt: "Flujograma: Herida de arma blanca periumbilical en un paciente estable, sin contractura y con leve reacción peritoneal: exploración local de la herida"
  },
  "PED-138": {
    titulo: "Preescolar con rinorrea, fiebre, tos perruna, tirajes y signo del campanario en la Rx: crup (laringotraqueítis) por virus parainfluenza",
    imagen: "flujogramas/tos-perruna-signo-campanario-parainfluenza.svg",
    alt: "Flujograma: Preescolar con rinorrea, fiebre, tos perruna, tirajes y signo del campanario en la Rx: crup (laringotraqueítis) por virus parainfluenza"
  },
  "SP-097": {
    titulo: "Internista que no pide interconsulta a psiquiatría antes de dar corticoides en dosis altas porque «se van a demorar»: negligencia (omisión)",
    imagen: "flujogramas/internista-omite-interconsulta-negligencia.svg",
    alt: "Flujograma: Internista que no pide interconsulta a psiquiatría antes de dar corticoides en dosis altas porque «se van a demorar»: negligencia (omisión)"
  },
  "PSI-027": {
    titulo: "Adolescente con un año de rechazo a comer y miedo intenso a engordar: anorexia nerviosa; la alteración del ECG buscada es el QT largo",
    imagen: "flujogramas/anorexia-adolescente-qt-largo.svg",
    alt: "Flujograma: Adolescente con un año de rechazo a comer y miedo intenso a engordar: anorexia nerviosa; la alteración del ECG buscada es el QT largo"
  },
  "GIN-138": {
    titulo: "Portadora de mutación BRCA de 35 años con paridad satisfecha que pide anticoncepción definitiva: salpinguectomía bilateral",
    imagen: "flujogramas/brca-paridad-satisfecha-salpinguectomia-bilateral.svg",
    alt: "Flujograma: Portadora de mutación BRCA de 35 años con paridad satisfecha que pide anticoncepción definitiva: salpinguectomía bilateral"
  },
  "INF-069": {
    titulo: "Joven con 5 días de diarrea acuosa sin sangre tras beber agua no embotellada en un viaje, que no le impide sus actividades: diarrea del viajero leve, hidratación oral",
    imagen: "flujogramas/viaje-agua-no-embotellada-diarrea-acuosa-hidratacion.svg",
    alt: "Flujograma: Joven con 5 días de diarrea acuosa sin sangre tras beber agua no embotellada en un viaje, que no le impide sus actividades: diarrea del viajero leve, hidratación oral"
  },
  "PED-139": {
    titulo: "Escolar con neumonía que sigue febril tras 5 días de ceftriaxona y toracocentesis con pus: empiema, drenaje con tubo de tórax y fibrinolíticos",
    imagen: "flujogramas/neumonia-fiebre-persistente-toracocentesis-pus-tubo-fibrinoliticos.svg",
    alt: "Flujograma: Escolar con neumonía que sigue febril tras 5 días de ceftriaxona y toracocentesis con pus: empiema, drenaje con tubo de tórax y fibrinolíticos"
  },
  "NRL-039": {
    titulo: "Ictus con afasia y hemiparesia derecha de 6 horas, NIHSS 10, sin infarto extenso y estenosis carotídea del 80 %: trombectomía mecánica (± angioplastia carotídea)",
    imagen: "flujogramas/hemiparesia-afasia-6-horas-trombectomia.svg",
    alt: "Flujograma: Ictus con afasia y hemiparesia derecha de 6 horas, NIHSS 10, sin infarto extenso y estenosis carotídea del 80 %: trombectomía mecánica (± angioplastia carotídea)"
  },
  "GIN-139": {
    titulo: "Hemorragia posparto por atonía que no cede con masaje, oxitocina, ergometrina ni misoprostol: taponamiento con balón intrauterino",
    imagen: "flujogramas/hemorragia-posparto-atonia-refractaria-balon.svg",
    alt: "Flujograma: Hemorragia posparto por atonía que no cede con masaje, oxitocina, ergometrina ni misoprostol: taponamiento con balón intrauterino"
  },
  "NEU-038": {
    titulo: "Anciano con neumonía del lóbulo inferior izquierdo y derrame pleural: tras iniciar antibiótico, toracocentesis para estudiar el líquido",
    imagen: "flujogramas/neumonia-derrame-pleural-toracocentesis.svg",
    alt: "Flujograma: Anciano con neumonía del lóbulo inferior izquierdo y derrame pleural: tras iniciar antibiótico, toracocentesis para estudiar el líquido"
  },
  "CAR-051": {
    titulo: "Hipertensa con 150/90 pese a losartán e hidroclorotiazida a dosis plenas y buena adherencia: añadir amlodipino",
    imagen: "flujogramas/losartan-hctz-pa-150-90-amlodipino.svg",
    alt: "Flujograma: Hipertensa con 150/90 pese a losartán e hidroclorotiazida a dosis plenas y buena adherencia: añadir amlodipino"
  },
  "PED-140": {
    titulo: "Lactante varón de 11 meses con fimosis, 3 días de fiebre de 39,5 °C y vómitos, sin otro foco: sospecha de ITU, pedir urocultivo",
    imagen: "flujogramas/lactante-fimosis-fiebre-3-dias-urocultivo.svg",
    alt: "Flujograma: Lactante varón de 11 meses con fimosis, 3 días de fiebre de 39,5 °C y vómitos, sin otro foco: sospecha de ITU, pedir urocultivo"
  },
  "CIR-075": {
    titulo: "Joven que se hirió el nudillo al golpear la boca de otra persona, con lesión del tendón extensor y la cápsula articular: exploración quirúrgica y lavado",
    imagen: "flujogramas/punetazo-boca-nudillo-tendon-capsula-lavado-quirurgico.svg",
    alt: "Flujograma: Joven que se hirió el nudillo al golpear la boca de otra persona, con lesión del tendón extensor y la cápsula articular: exploración quirúrgica y lavado"
  },
  "GIN-140": {
    titulo: "Mujer de 55 años tratada con cono por NIC 3: debe seguir con tamizaje por muchos años (la clave dice 20; las guías actuales, 25), aunque pase los 65",
    imagen: "flujogramas/cono-nic3-seguir-tamizaje-20-anos.svg",
    alt: "Flujograma: Mujer de 55 años tratada con cono por NIC 3: debe seguir con tamizaje por muchos años (la clave dice 20; las guías actuales, 25), aunque pase los 65"
  },
  "CB-050": {
    titulo: "Del inicio de la gastrulación a la semana 8 tras la concepción se forman los órganos: período embrionario, el más sensible a malformaciones",
    imagen: "flujogramas/semanas-2-a-8-organogenesis-periodo-embrionario.svg",
    alt: "Flujograma: Del inicio de la gastrulación a la semana 8 tras la concepción se forman los órganos: período embrionario, el más sensible a malformaciones"
  },
  "PED-141": {
    titulo: "Recién nacido de 48 horas, madre primeriza con pezones planos, ictericia, irritable o letárgico, poca orina y pérdida de peso > 10 %: deshidratación hipernatrémica",
    imagen: "flujogramas/neonato-48-h-pezones-planos-perdida-peso-hipernatremia.svg",
    alt: "Flujograma: Recién nacido de 48 horas, madre primeriza con pezones planos, ictericia, irritable o letárgico, poca orina y pérdida de peso > 10 %: deshidratación hipernatrémica"
  },
  "CIR-076": {
    titulo: "Quemadura por agua hirviendo en las manos con piel roja, sin flictenas ni ampollas: quemadura de primer grado (epidérmica), analgésicos orales",
    imagen: "flujogramas/agua-hirviendo-manos-eritema-sin-ampollas-analgesia.svg",
    alt: "Flujograma: Quemadura por agua hirviendo en las manos con piel roja, sin flictenas ni ampollas: quemadura de primer grado (epidérmica), analgésicos orales"
  },
  "TRA-027": {
    titulo: "Niño de 6 años con pie plano flexible, sin dolor ni limitación: variante normal, no requiere tratamiento",
    imagen: "flujogramas/escolar-pie-plano-flexible-sin-dolor-no-tratar.svg",
    alt: "Flujograma: Niño de 6 años con pie plano flexible, sin dolor ni limitación: variante normal, no requiere tratamiento"
  },
  "CIR-077": {
    titulo: "Joven estreñido con sangrado y una masa que sale por el ano y que él mismo vuelve a meter con la mano: hemorroides internas de grado III",
    imagen: "flujogramas/prolapso-hemorroidal-reduccion-manual-tercer-grado.svg",
    alt: "Flujograma: Joven estreñido con sangrado y una masa que sale por el ano y que él mismo vuelve a meter con la mano: hemorroides internas de grado III"
  },
  "CIR-078": {
    titulo: "Anciano con EPOC sin tratamiento y enfermedad coronaria, operado de urgencia por fractura expuesta del radio: bloqueo de nervio periférico (plexo braquial)",
    imagen: "flujogramas/epoc-coronario-fractura-radio-bloqueo-periferico.svg",
    alt: "Flujograma: Anciano con EPOC sin tratamiento y enfermedad coronaria, operado de urgencia por fractura expuesta del radio: bloqueo de nervio periférico (plexo braquial)"
  },
  "GAS-049": {
    titulo: "Hepatitis C crónica con ascitis, ictericia, circulación colateral, albúmina 2,4, INR 1,7 y plaquetas 85 000: cirrosis hepática descompensada (Child-Pugh C)",
    imagen: "flujogramas/hepatitis-c-ascitis-albumina-24-inr-17-cirrosis-descompensada.svg",
    alt: "Flujograma: Hepatitis C crónica con ascitis, ictericia, circulación colateral, albúmina 2,4, INR 1,7 y plaquetas 85 000: cirrosis hepática descompensada (Child-Pugh C)"
  },
  "SP-098": {
    titulo: "Establecimiento con servicios de baja calidad y sin recursos financieros: en el análisis FODA es una debilidad (factor interno desfavorable)",
    imagen: "flujogramas/foda-baja-calidad-sin-recursos-debilidades.svg",
    alt: "Flujograma: Establecimiento con servicios de baja calidad y sin recursos financieros: en el análisis FODA es una debilidad (factor interno desfavorable)"
  },
  "PED-142": {
    titulo: "Prematuro de 28 semanas y 1200 g con retinopatía del prematuro que progresa: SatO₂ estable en 90-95 % y no cortar los exámenes de fondo de ojo",
    imagen: "flujogramas/prematuro-28-semanas-rop-saturacion-90-95.svg",
    alt: "Flujograma: Prematuro de 28 semanas y 1200 g con retinopatía del prematuro que progresa: SatO₂ estable en 90-95 % y no cortar los exámenes de fondo de ojo"
  },
  "GAS-050": {
    titulo: "Joven que vomitó muchas veces tras beber alcohol y luego tiene hematemesis, estable y sin hepatopatía: desgarro de Mallory-Weiss",
    imagen: "flujogramas/vomitos-alcohol-hematemesis-mallory-weiss.svg",
    alt: "Flujograma: Joven que vomitó muchas veces tras beber alcohol y luego tiene hematemesis, estable y sin hepatopatía: desgarro de Mallory-Weiss"
  },
  "HEM-027": {
    titulo: "En la leucemia mieloide aguda, el factor pronóstico más importante al diagnóstico son las alteraciones citogenéticas y moleculares (riesgo ELN 2022)",
    imagen: "flujogramas/lma-pronostico-citogenetica.svg",
    alt: "Flujograma: En la leucemia mieloide aguda, el factor pronóstico más importante al diagnóstico son las alteraciones citogenéticas y moleculares (riesgo ELN 2022)"
  },
  "CIR-079": {
    titulo: "Gran quemado del 50 % a las 24 horas con taquicardia, fiebre, hiperglucemia y catabolismo de proteínas: estado hipermetabólico posquemadura",
    imagen: "flujogramas/quemado-50-taquicardia-fiebre-catabolismo-hipermetabolismo.svg",
    alt: "Flujograma: Gran quemado del 50 % a las 24 horas con taquicardia, fiebre, hiperglucemia y catabolismo de proteínas: estado hipermetabólico posquemadura"
  },
  "GAS-051": {
    titulo: "Varón de 64 años con pérdida de 10 kg, estreñimiento, hematoquecia y palidez con taquicardia: sospecha de cáncer colorrectal, pedir colonoscopía",
    imagen: "flujogramas/anciano-perdida-peso-hematoquecia-anemia-colonoscopia.svg",
    alt: "Flujograma: Varón de 64 años con pérdida de 10 kg, estreñimiento, hematoquecia y palidez con taquicardia: sospecha de cáncer colorrectal, pedir colonoscopía"
  },
  "PSI-028": {
    titulo: "Adolescente de 13 años con miedo intenso a ganar peso, imagen corporal distorsionada y restricción de la ingesta: anorexia nerviosa",
    imagen: "flujogramas/adolescente-miedo-engordar-distorsion-restriccion-anorexia.svg",
    alt: "Flujograma: Adolescente de 13 años con miedo intenso a ganar peso, imagen corporal distorsionada y restricción de la ingesta: anorexia nerviosa"
  },
  "SP-099": {
    titulo: "Comunidad sin agua ni desagüe con parasitosis infantil: solo se indica el antiparasitario sin tocar el saneamiento = modelo biomédico",
    imagen: "flujogramas/parasitosis-sin-saneamiento-solo-medicamento-biomedico.svg",
    alt: "Flujograma: Comunidad sin agua ni desagüe con parasitosis infantil: solo se indica el antiparasitario sin tocar el saneamiento = modelo biomédico"
  },
  "SP-100": {
    titulo: "Mujer víctima de violencia sexual con lesiones genitales y crisis emocional: la primera obligación es la atención médica y la estabilización",
    imagen: "flujogramas/victima-violencia-sexual-atencion-medica-primero.svg",
    alt: "Flujograma: Mujer víctima de violencia sexual con lesiones genitales y crisis emocional: la primera obligación es la atención médica y la estabilización"
  },
  "INF-070": {
    titulo: "Mordedura de perro en la mano hace 2 horas, herida desgarrante profunda: lo primero en el primer nivel es el lavado profuso con agua, jabón y suero",
    imagen: "flujogramas/mordedura-perro-mano-desgarrante-lavado.svg",
    alt: "Flujograma: Mordedura de perro en la mano hace 2 horas, herida desgarrante profunda: lo primero en el primer nivel es el lavado profuso con agua, jabón y suero"
  },
  "CB-051": {
    titulo: "Joven agitado a la salida de una discoteca con PA 190/100, FC 132, T 38,8 °C, sudoración y pupilas de 7,5 mm: toxíndrome simpaticomimético, benzodiacepinas",
    imagen: "flujogramas/discoteca-agitacion-diaforesis-midriasis-benzodiacepinas.svg",
    alt: "Flujograma: Joven agitado a la salida de una discoteca con PA 190/100, FC 132, T 38,8 °C, sudoración y pupilas de 7,5 mm: toxíndrome simpaticomimético, benzodiacepinas"
  },
  "SP-101": {
    titulo: "Del total de pacientes se elige el primero al azar y luego 1 de cada 3: muestreo sistemático",
    imagen: "flujogramas/uno-de-cada-3-inicio-azar-muestreo-sistematico.svg",
    alt: "Flujograma: Del total de pacientes se elige el primero al azar y luego 1 de cada 3: muestreo sistemático"
  },
  "TRA-028": {
    titulo: "Mujer de 60 años con menopausia precoz y fractura en cuña de L4 tras caer de su propia altura: confirmar osteoporosis con densitometría (DXA)",
    imagen: "flujogramas/fractura-vertebral-caida-menopausia-precoz-densitometria.svg",
    alt: "Flujograma: Mujer de 60 años con menopausia precoz y fractura en cuña de L4 tras caer de su propia altura: confirmar osteoporosis con densitometría (DXA)"
  },
  "INF-071": {
    titulo: "Paciente con VIH sin TAR, meningitis con LCR linfocitario y VDRL positivo en LCR: neurosífilis, tratar con penicilina G sódica EV",
    imagen: "flujogramas/vih-rpr-lcr-vdrl-neurosifilis-penicilina-g-sodica.svg",
    alt: "Flujograma: Paciente con VIH sin TAR, meningitis con LCR linfocitario y VDRL positivo en LCR: neurosífilis, tratar con penicilina G sódica EV"
  },
  "CIR-080": {
    titulo: "Anciana con fiebre, masa en fosa ilíaca izquierda y absceso pericólico de 5 cm en la TC: Hinchey Ib, drenaje percutáneo + antibióticos",
    imagen: "flujogramas/diverticulitis-absceso-pericolico-5-cm-drenaje-percutaneo.svg",
    alt: "Flujograma: Anciana con fiebre, masa en fosa ilíaca izquierda y absceso pericólico de 5 cm en la TC: Hinchey Ib, drenaje percutáneo + antibióticos"
  },
  "CIR-081": {
    titulo: "Anciano con dolor y distensión abdominal, vómitos y Rx de pie con aire libre bajo el diafragma: neumoperitoneo por perforación, laparotomía exploratoria",
    imagen: "flujogramas/anciano-dolor-distension-neumoperitoneo-laparotomia.svg",
    alt: "Flujograma: Anciano con dolor y distensión abdominal, vómitos y Rx de pie con aire libre bajo el diafragma: neumoperitoneo por perforación, laparotomía exploratoria"
  },
  "SP-102": {
    titulo: "La parte del protocolo que sustenta la hipótesis con argumentos de plausibilidad y estudios previos es el marco teórico",
    imagen: "flujogramas/protocolo-sustento-hipotesis-marco-teorico.svg",
    alt: "Flujograma: La parte del protocolo que sustenta la hipótesis con argumentos de plausibilidad y estudios previos es el marco teórico"
  },
  "PSI-029": {
    titulo: "Al indicar un ISRS para la depresión hay que explicar que su retiro debe ser gradual y supervisado (síndrome de discontinuación)",
    imagen: "flujogramas/isrs-depresion-retiro-gradual.svg",
    alt: "Flujograma: Al indicar un ISRS para la depresión hay que explicar que su retiro debe ser gradual y supervisado (síndrome de discontinuación)"
  },
  "TRA-029": {
    titulo: "Varón de 66 años con dolor en ambas rodillas que cede tras moverse, crepitación y sin hinchazón: gonartrosis",
    imagen: "flujogramas/rodillas-crepitacion-rigidez-breve-gonartrosis.svg",
    alt: "Flujograma: Varón de 66 años con dolor en ambas rodillas que cede tras moverse, crepitación y sin hinchazón: gonartrosis"
  },
  "SP-103": {
    titulo: "El documento de gestión que fija la estructura orgánica y formaliza las competencias y funciones de cada área es el Reglamento de Organización y Funciones (ROF)",
    imagen: "flujogramas/documento-estructura-organica-funciones-rof.svg",
    alt: "Flujograma: El documento de gestión que fija la estructura orgánica y formaliza las competencias y funciones de cada área es el Reglamento de Organización y Funciones (ROF)"
  },
  "CB-052": {
    titulo: "La relación correcta entre quimioterápico y toxicidad característica es antraciclinas (doxorrubicina) y cardiotoxicidad",
    imagen: "flujogramas/antraciclinas-cardiotoxicidad.svg",
    alt: "Flujograma: La relación correcta entre quimioterápico y toxicidad característica es antraciclinas (doxorrubicina) y cardiotoxicidad"
  },
  "NEF-062": {
    titulo: "Varón de 63 años con dificultad para iniciar la micción, chorro débil y pujo: el primer paso es el tacto rectal",
    imagen: "flujogramas/chorro-debil-esfuerzo-miccional-tacto-rectal.svg",
    alt: "Flujograma: Varón de 63 años con dificultad para iniciar la micción, chorro débil y pujo: el primer paso es el tacto rectal"
  },
  "GIN-141": {
    titulo: "Flujo abundante y maloliente con prurito, vulva inflamada y petequias en el cuello uterino («cérvix en fresa»): Trichomonas vaginalis",
    imagen: "flujogramas/flujo-maloliente-cervix-petequial-tricomonas.svg",
    alt: "Flujograma: Flujo abundante y maloliente con prurito, vulva inflamada y petequias en el cuello uterino («cérvix en fresa»): Trichomonas vaginalis"
  },
  "INF-072": {
    titulo: "Joven de Loreto con úlcera única de 3 meses en la pierna, de bordes elevados e indurados, fondo granuloso e indolora: leishmaniasis cutánea",
    imagen: "flujogramas/loreto-ulcera-indolora-bordes-indurados-leishmaniasis.svg",
    alt: "Flujograma: Joven de Loreto con úlcera única de 3 meses en la pierna, de bordes elevados e indurados, fondo granuloso e indolora: leishmaniasis cutánea"
  },
  "GIN-142": {
    titulo: "Puérpera inmediata que sangra y a cuya placenta le falta un cotiledón: alumbramiento incompleto, revisión uterina instrumental",
    imagen: "flujogramas/falta-cotiledon-sangrado-revision-uterina.svg",
    alt: "Flujograma: Puérpera inmediata que sangra y a cuya placenta le falta un cotiledón: alumbramiento incompleto, revisión uterina instrumental"
  },
  "CAR-052": {
    titulo: "Hipertensa mal tratada con disnea, tos rosada, diaforesis, PA 195/105 y crepitantes difusos: edema agudo de pulmón hipertensivo (caliente y húmedo)",
    imagen: "flujogramas/hipertensa-tos-rosada-crepitantes-edema-agudo-pulmon.svg",
    alt: "Flujograma: Hipertensa mal tratada con disnea, tos rosada, diaforesis, PA 195/105 y crepitantes difusos: edema agudo de pulmón hipertensivo (caliente y húmedo)"
  },
  "NEF-063": {
    titulo: "Nefropatía membranosa con proteinuria de 8 g y albúmina 1,8 que presenta disnea súbita, dolor pleurítico y SatO₂ 88 %: tromboembolismo pulmonar",
    imagen: "flujogramas/nefrotico-membranosa-albumina-18-disnea-tep.svg",
    alt: "Flujograma: Nefropatía membranosa con proteinuria de 8 g y albúmina 1,8 que presenta disnea súbita, dolor pleurítico y SatO₂ 88 %: tromboembolismo pulmonar"
  },
  "INF-073": {
    titulo: "Fiebre, cefalea y rigidez de nuca con LCR de 90 linfocitos, glucosa normal y proteínas 80: meningitis viral (aséptica), tratamiento sintomático",
    imagen: "flujogramas/lcr-linfocitos-glucosa-normal-meningitis-viral.svg",
    alt: "Flujograma: Fiebre, cefalea y rigidez de nuca con LCR de 90 linfocitos, glucosa normal y proteínas 80: meningitis viral (aséptica), tratamiento sintomático"
  },
  "TRA-030": {
    titulo: "Trauma de muñeca hace 3 meses y ahora adormecimiento del 4.º y 5.º dedo: compromiso del nervio cubital en el canal de Guyon",
    imagen: "flujogramas/trauma-muneca-4-5-dedo-canal-guyon.svg",
    alt: "Flujograma: Trauma de muñeca hace 3 meses y ahora adormecimiento del 4.º y 5.º dedo: compromiso del nervio cubital en el canal de Guyon"
  },
  "SP-104": {
    titulo: "200 comieron en un comedor y 80 enfermaron en 24 horas: la tasa de ataque (40 %) es el riesgo de un expuesto de enfermar durante el brote",
    imagen: "flujogramas/comedor-200-comensales-80-enfermos-tasa-ataque.svg",
    alt: "Flujograma: 200 comieron en un comedor y 80 enfermaron en 24 horas: la tasa de ataque (40 %) es el riesgo de un expuesto de enfermar durante el brote"
  },
  "SP-105": {
    titulo: "Organizaciones que atienden de forma equitativa e integral a una población definida, articuladas y que rinden cuentas por sus resultados: Redes Integradas de Salud",
    imagen: "flujogramas/conjunto-organizaciones-articulacion-redes-integradas.svg",
    alt: "Flujograma: Organizaciones que atienden de forma equitativa e integral a una población definida, articuladas y que rinden cuentas por sus resultados: Redes Integradas de Salud"
  },
  "END-041": {
    titulo: "Escolar de 12 años con IMC sobre +3 DE y manchas aterciopeladas oscuras en cuello y axilas: obesidad con resistencia a la insulina",
    imagen: "flujogramas/adolescente-imc-3-de-acantosis-resistencia-insulina.svg",
    alt: "Flujograma: Escolar de 12 años con IMC sobre +3 DE y manchas aterciopeladas oscuras en cuello y axilas: obesidad con resistencia a la insulina"
  },
  "CIR-082": {
    titulo: "Tercer día después de una resección intestinal con distensión y sin ruidos intestinales: íleo posoperatorio, cuya causa iatrogénica más frecuente son los opioides",
    imagen: "flujogramas/posoperatorio-dia-3-distension-sin-rha-opioides.svg",
    alt: "Flujograma: Tercer día después de una resección intestinal con distensión y sin ruidos intestinales: íleo posoperatorio, cuya causa iatrogénica más frecuente son los opioides"
  },
  "GAS-052": {
    titulo: "El marcador tumoral más útil en el adenocarcinoma de páncreas es el CA 19-9 (sirve para seguimiento, no para tamizaje)",
    imagen: "flujogramas/adenocarcinoma-pancreas-ca-19-9.svg",
    alt: "Flujograma: El marcador tumoral más útil en el adenocarcinoma de páncreas es el CA 19-9 (sirve para seguimiento, no para tamizaje)"
  },
  "CIR-083": {
    titulo: "Dolor en fosa ilíaca derecha con signos peritoneales 6 meses después de una apendicectomía y TC con estructura tubular inflamada en el ciego: apendicitis del muñón",
    imagen: "flujogramas/apendicectomia-previa-dolor-fid-munon-inflamado.svg",
    alt: "Flujograma: Dolor en fosa ilíaca derecha con signos peritoneales 6 meses después de una apendicectomía y TC con estructura tubular inflamada en el ciego: apendicitis del muñón"
  },
  "INF-074": {
    titulo: "Vesículas dolorosas en el labio mayor desde hace 2 días: para confirmar herpes genital se hacen pruebas virológicas de la lesión (PCR)",
    imagen: "flujogramas/vesiculas-labio-mayor-herpes-genital-pcr-lesion.svg",
    alt: "Flujograma: Vesículas dolorosas en el labio mayor desde hace 2 días: para confirmar herpes genital se hacen pruebas virológicas de la lesión (PCR)"
  },
  "NEF-064": {
    titulo: "En la prostatectomía radical hay que identificar y preservar los nervios cavernosos (bandeletas neurovasculares) para evitar la disfunción eréctil",
    imagen: "flujogramas/prostatectomia-radical-preservar-nervios-cavernosos.svg",
    alt: "Flujograma: En la prostatectomía radical hay que identificar y preservar los nervios cavernosos (bandeletas neurovasculares) para evitar la disfunción eréctil"
  },
  "END-042": {
    titulo: "Diabética tipo 2 de 10 años con creatinina normal: para detectar daño renal precoz se pide la relación albúmina/creatinina en orina aislada",
    imagen: "flujogramas/dm2-10-anos-cociente-albumina-creatinina.svg",
    alt: "Flujograma: Diabética tipo 2 de 10 años con creatinina normal: para detectar daño renal precoz se pide la relación albúmina/creatinina en orina aislada"
  },
  "CB-053": {
    titulo: "Para atravesar con facilidad la barrera hematoencefálica, un anestésico debe ser muy liposoluble (y pequeño, no ionizado)",
    imagen: "flujogramas/anestesico-liposoluble-barrera-hematoencefalica.svg",
    alt: "Flujograma: Para atravesar con facilidad la barrera hematoencefálica, un anestésico debe ser muy liposoluble (y pequeño, no ionizado)"
  },
  "GAS-053": {
    titulo: "Pancreatitis aguda moderada con taquipnea y SatO₂ 92 %: la hipoxemia se debe a alteración ventilación/perfusión por atelectasias y derrame pleural",
    imagen: "flujogramas/pancreatitis-disnea-hipoxemia-alteracion-vq.svg",
    alt: "Flujograma: Pancreatitis aguda moderada con taquipnea y SatO₂ 92 %: la hipoxemia se debe a alteración ventilación/perfusión por atelectasias y derrame pleural"
  },
  "INF-075": {
    titulo: "SIDA con CD4 30, odinofagia y úlceras serpiginosas en el esófago distal con inclusiones en células grandes: esofagitis por citomegalovirus, ganciclovir",
    imagen: "flujogramas/sida-cd4-30-ulceras-esofagicas-inclusiones-cmv-ganciclovir.svg",
    alt: "Flujograma: SIDA con CD4 30, odinofagia y úlceras serpiginosas en el esófago distal con inclusiones en células grandes: esofagitis por citomegalovirus, ganciclovir"
  },
  "NEU-039": {
    titulo: "Gestante de 20 semanas con tos de más de 2 semanas, febrícula, pérdida de peso y contacto familiar: tuberculosis pulmonar",
    imagen: "flujogramas/gestante-tos-perdida-peso-abuela-tos-tuberculosis.svg",
    alt: "Flujograma: Gestante de 20 semanas con tos de más de 2 semanas, febrícula, pérdida de peso y contacto familiar: tuberculosis pulmonar"
  },
  "GIN-143": {
    titulo: "Bolo de oxitocina en el expulsivo seguido de taquicardia y luego bradicardia fetal: hipertonía uterina que corta el flujo a la placenta",
    imagen: "flujogramas/bolo-oxitocina-bradicardia-fetal-hipertonia.svg",
    alt: "Flujograma: Bolo de oxitocina en el expulsivo seguido de taquicardia y luego bradicardia fetal: hipertonía uterina que corta el flujo a la placenta"
  },
  "HEM-028": {
    titulo: "Sangrados de piel y mucosas propios y familiares, tiempo de sangría prolongado, factor VIII bajo y agregación con ristocetina disminuida: enfermedad de von Willebrand",
    imagen: "flujogramas/sangrado-mucocutaneo-ristocetina-baja-von-willebrand.svg",
    alt: "Flujograma: Sangrados de piel y mucosas propios y familiares, tiempo de sangría prolongado, factor VIII bajo y agregación con ristocetina disminuida: enfermedad de von Willebrand"
  },
  "CIR-084": {
    titulo: "En la apendicitis no complicada de una paciente obesa, la ventaja de la vía laparoscópica sobre la abierta es la menor infección de la herida",
    imagen: "flujogramas/apendicitis-obesa-laparoscopia-menos-infeccion-herida.svg",
    alt: "Flujograma: En la apendicitis no complicada de una paciente obesa, la ventaja de la vía laparoscópica sobre la abierta es la menor infección de la herida"
  },
  "CIR-085": {
    titulo: "Tumoración blanda en la línea media sobre el ombligo que aparece de pie y desaparece acostado: hernia epigástrica",
    imagen: "flujogramas/tumoracion-supraumbilical-reductible-hernia-epigastrica.svg",
    alt: "Flujograma: Tumoración blanda en la línea media sobre el ombligo que aparece de pie y desaparece acostado: hernia epigástrica"
  },
  "INF-076": {
    titulo: "Diarrea intermitente con pérdida de peso y trofozoítos de Entamoeba histolytica en heces: metronidazol y luego un amebicida luminal (paromomicina)",
    imagen: "flujogramas/trofozoitos-entamoeba-metronidazol-paromomicina.svg",
    alt: "Flujograma: Diarrea intermitente con pérdida de peso y trofozoítos de Entamoeba histolytica en heces: metronidazol y luego un amebicida luminal (paromomicina)"
  },
  "GIN-144": {
    titulo: "Tras la salida de la cabeza fetal, el siguiente movimiento cardinal es la rotación externa (restitución), que alinea los hombros",
    imagen: "flujogramas/salida-cabeza-rotacion-externa.svg",
    alt: "Flujograma: Tras la salida de la cabeza fetal, el siguiente movimiento cardinal es la rotación externa (restitución), que alinea los hombros"
  },
  "NRL-040": {
    titulo: "Adolescente con cefalea hemicraneal pulsátil de 48 horas, fotofobia, náuseas y vómitos, examen y TC normales: migraña",
    imagen: "flujogramas/cefalea-hemicraneal-pulsatil-48-h-fotofobia-migrana.svg",
    alt: "Flujograma: Adolescente con cefalea hemicraneal pulsátil de 48 horas, fotofobia, náuseas y vómitos, examen y TC normales: migraña"
  },
  "SP-106": {
    titulo: "Para reducir la leptospirosis en zonas rurales pobres con mal saneamiento, la estrategia comunitaria más efectiva es promover calzado y agua segura",
    imagen: "flujogramas/leptospirosis-rural-calzado-agua-segura.svg",
    alt: "Flujograma: Para reducir la leptospirosis en zonas rurales pobres con mal saneamiento, la estrategia comunitaria más efectiva es promover calzado y agua segura"
  },
  "NEU-040": {
    titulo: "Asmático con 6 días de disnea, habla entrecortada, FR 24, SatO₂ 93 %, músculos accesorios y PEF 66 %: crisis asmática moderada",
    imagen: "flujogramas/habla-entrecortada-sato2-93-pef-66-crisis-moderada.svg",
    alt: "Flujograma: Asmático con 6 días de disnea, habla entrecortada, FR 24, SatO₂ 93 %, músculos accesorios y PEF 66 %: crisis asmática moderada"
  },
  "PSI-030": {
    titulo: "Amenorrea de 24 semanas, náuseas, mamas congestionadas y «movimientos fetales» con útero vacío y β-hCG 0,1: pseudociesis",
    imagen: "flujogramas/amenorrea-sintomas-embarazo-hcg-negativa-pseudociesis.svg",
    alt: "Flujograma: Amenorrea de 24 semanas, náuseas, mamas congestionadas y «movimientos fetales» con útero vacío y β-hCG 0,1: pseudociesis"
  },
  "REU-040": {
    titulo: "Anciano con nódulo perlado en la cara, de crecimiento lento, telangiectasias y ulceración central: carcinoma basocelular",
    imagen: "flujogramas/nodulo-perlado-telangiectasias-cara-basocelular.svg",
    alt: "Flujograma: Anciano con nódulo perlado en la cara, de crecimiento lento, telangiectasias y ulceración central: carcinoma basocelular"
  },
  "SP-107": {
    titulo: "Planta con trabajadores irritados por formaldehído, sin protección y con mala ventilación: la medida prioritaria es eliminar o reducir la fuente",
    imagen: "flujogramas/formaldehido-planta-alimentos-eliminar-fuente.svg",
    alt: "Flujograma: Planta con trabajadores irritados por formaldehído, sin protección y con mala ventilación: la medida prioritaria es eliminar o reducir la fuente"
  },
  "SP-108": {
    titulo: "La terapia que se basa en el principio de similitud («lo similar cura lo similar») y usa sustancias muy diluidas es la homeopatía",
    imagen: "flujogramas/similitud-diluciones-homeopatia.svg",
    alt: "Flujograma: La terapia que se basa en el principio de similitud («lo similar cura lo similar») y usa sustancias muy diluidas es la homeopatía"
  },
  "PED-143": {
    titulo: "Recién nacido con bradicardia fetal previa que convulsiona a las 2 horas de vida: encefalopatía hipóxico-isquémica, el anticonvulsivante de elección es el fenobarbital",
    imagen: "flujogramas/rn-bradicardia-fetal-convulsion-2-horas-fenobarbital.svg",
    alt: "Flujograma: Recién nacido con bradicardia fetal previa que convulsiona a las 2 horas de vida: encefalopatía hipóxico-isquémica, el anticonvulsivante de elección es el fenobarbital"
  },
  "NEF-065": {
    titulo: "Anciano con síntomas urinarios de llenado y vaciado de 1 año, próstata grande y lisa y PSA 5: hiperplasia benigna, iniciar alfabloqueador",
    imagen: "flujogramas/anciano-sintomas-prostaticos-alfa-bloqueante.svg",
    alt: "Flujograma: Anciano con síntomas urinarios de llenado y vaciado de 1 año, próstata grande y lisa y PSA 5: hiperplasia benigna, iniciar alfabloqueador"
  },
  "OFT-033": {
    titulo: "Mujer con dolor ocular intenso, halos, visión borrosa, náuseas, ojo rojo, pupila en midriasis media fija y ojo duro: glaucoma agudo, acetazolamida 500 mg",
    imagen: "flujogramas/dolor-ocular-halos-midriasis-media-acetazolamida.svg",
    alt: "Flujograma: Mujer con dolor ocular intenso, halos, visión borrosa, náuseas, ojo rojo, pupila en midriasis media fija y ojo duro: glaucoma agudo, acetazolamida 500 mg"
  },
  "REU-041": {
    titulo: "Adolescente con vesículas y costras color miel en antebrazos y alrededor de la boca, hermano con lo mismo y sin compromiso general: impétigo localizado, mupirocina tópica",
    imagen: "flujogramas/costras-mielicericas-boca-antebrazos-mupirocina.svg",
    alt: "Flujograma: Adolescente con vesículas y costras color miel en antebrazos y alrededor de la boca, hermano con lo mismo y sin compromiso general: impétigo localizado, mupirocina tópica"
  },
  "NRL-041": {
    titulo: "Caída con pérdida de conciencia, intervalo lúcido, deterioro, Glasgow 10 y midriasis fija del lado de la herida: hematoma epidural",
    imagen: "flujogramas/caida-escaleras-intervalo-lucido-midriasis-epidural.svg",
    alt: "Flujograma: Caída con pérdida de conciencia, intervalo lúcido, deterioro, Glasgow 10 y midriasis fija del lado de la herida: hematoma epidural"
  },
  "CIR-086": {
    titulo: "Dolor de 20 horas en hipocondrio derecho, vómitos, fiebre, taquicardia, masa dolorosa subcostal y litiasis conocida: colecistitis aguda",
    imagen: "flujogramas/litiasis-dolor-hcd-fiebre-masa-colecistitis.svg",
    alt: "Flujograma: Dolor de 20 horas en hipocondrio derecho, vómitos, fiebre, taquicardia, masa dolorosa subcostal y litiasis conocida: colecistitis aguda"
  },
  "INF-077": {
    titulo: "Escolar con 10 días de odinofagia, amígdalas exudativas, adenopatías cervicales grandes, hepatoesplenomegalia y exantema: mononucleosis infecciosa",
    imagen: "flujogramas/adolescente-amigdalas-exudativas-hepatoesplenomegalia-mononucleosis.svg",
    alt: "Flujograma: Escolar con 10 días de odinofagia, amígdalas exudativas, adenopatías cervicales grandes, hepatoesplenomegalia y exantema: mononucleosis infecciosa"
  },
  "TRA-031": {
    titulo: "Joven con fractura del tercio medio del húmero tras un accidente y mano caída (no extiende muñeca ni dedos): lesión del nervio radial",
    imagen: "flujogramas/fractura-tercio-medio-humero-mano-pendula-radial.svg",
    alt: "Flujograma: Joven con fractura del tercio medio del húmero tras un accidente y mano caída (no extiende muñeca ni dedos): lesión del nervio radial"
  },
  "NEF-066": {
    titulo: "Adolescente con dolor testicular súbito e intenso de 3 horas y testículo derecho alto y aumentado: torsión testicular, cirugía urgente",
    imagen: "flujogramas/adolescente-dolor-testicular-subito-testiculo-alto-torsion.svg",
    alt: "Flujograma: Adolescente con dolor testicular súbito e intenso de 3 horas y testículo derecho alto y aumentado: torsión testicular, cirugía urgente"
  },
  "REU-042": {
    titulo: "Joven con poliartritis simétrica de manos, muñecas y rodillas por 3 meses y rigidez matinal prolongada: pedir anticuerpos anti-péptido citrulinado (anti-CCP)",
    imagen: "flujogramas/poliartritis-simetrica-manos-rigidez-anti-ccp.svg",
    alt: "Flujograma: Joven con poliartritis simétrica de manos, muñecas y rodillas por 3 meses y rigidez matinal prolongada: pedir anticuerpos anti-péptido citrulinado (anti-CCP)"
  },
  "PED-144": {
    titulo: "Prematuro de 32 semanas con quejido, aleteo, tiraje y Rx con patrón reticular fino y broncograma aéreo: enfermedad de membrana hialina",
    imagen: "flujogramas/prematuro-32-semanas-quejido-broncograma-membrana-hialina.svg",
    alt: "Flujograma: Prematuro de 32 semanas con quejido, aleteo, tiraje y Rx con patrón reticular fino y broncograma aéreo: enfermedad de membrana hialina"
  },
  "GAS-054": {
    titulo: "Mujer con ictericias previas, dolor cólico en hipocondrio derecho, fiebre de 39 °C, ictericia y colédoco de 15 mm: colangitis aguda",
    imagen: "flujogramas/fiebre-ictericia-dolor-coledoco-15-mm-colangitis.svg",
    alt: "Flujograma: Mujer con ictericias previas, dolor cólico en hipocondrio derecho, fiebre de 39 °C, ictericia y colédoco de 15 mm: colangitis aguda"
  },
  "REU-043": {
    titulo: "Joven con picaduras de abejas, disnea, estridor, sibilancias, cianosis y PA 80/50: anafilaxia, el tratamiento es adrenalina intramuscular",
    imagen: "flujogramas/picadura-abejas-estridor-hipotension-adrenalina.svg",
    alt: "Flujograma: Joven con picaduras de abejas, disnea, estridor, sibilancias, cianosis y PA 80/50: anafilaxia, el tratamiento es adrenalina intramuscular"
  },
  "GIN-145": {
    titulo: "Gestante de 28 semanas con fiebre de 39 °C, escalofríos, dolor lumbar y puño-percusión positiva: pielonefritis, ceftriaxona EV",
    imagen: "flujogramas/gestante-28-semanas-fiebre-puno-percusion-ceftriaxona.svg",
    alt: "Flujograma: Gestante de 28 semanas con fiebre de 39 °C, escalofríos, dolor lumbar y puño-percusión positiva: pielonefritis, ceftriaxona EV"
  },
  "TRA-032": {
    titulo: "Aplastamiento de piernas hace 2 horas con dolor que no cede con analgésicos, parestesias, palidez, tumefacción y pulso pedio ausente: síndrome compartimental",
    imagen: "flujogramas/aplastamiento-dolor-refractario-palidez-sin-pulso-compartimental.svg",
    alt: "Flujograma: Aplastamiento de piernas hace 2 horas con dolor que no cede con analgésicos, parestesias, palidez, tumefacción y pulso pedio ausente: síndrome compartimental"
  },
  "CB-054": {
    titulo: "Joven sedado tras un trago ofrecido en una discoteca, con disartria, ataxia e hipotonía, que despierta con flumazenilo: le dieron una benzodiacepina (diazepam)",
    imagen: "flujogramas/discoteca-trago-flumazenilo-despierta-benzodiacepina.svg",
    alt: "Flujograma: Joven sedado tras un trago ofrecido en una discoteca, con disartria, ataxia e hipotonía, que despierta con flumazenilo: le dieron una benzodiacepina (diazepam)"
  },
  "PED-145": {
    titulo: "Lactante varón de 10 días con vómitos explosivos tras lactar y masa en el epigastrio: estenosis hipertrófica del píloro, pedir ecografía",
    imagen: "flujogramas/neonato-10-dias-vomitos-explosivos-oliva-ecografia.svg",
    alt: "Flujograma: Lactante varón de 10 días con vómitos explosivos tras lactar y masa en el epigastrio: estenosis hipertrófica del píloro, pedir ecografía"
  },
  "PED-146": {
    titulo: "Recién nacido que se ahoga y tose al lactar, con crepitantes y una sonda que se enrolla en el esófago proximal: atresia de esófago",
    imagen: "flujogramas/rn-tos-asfixia-lactar-sonda-enrollada-atresia-esofagica.svg",
    alt: "Flujograma: Recién nacido que se ahoga y tose al lactar, con crepitantes y una sonda que se enrolla en el esófago proximal: atresia de esófago"
  },
  "PED-147": {
    titulo: "Niño de 5 años con fiebre y lesiones que pican en distintos estadios (pápulas, vesículas y costras) en piel, cuero cabelludo y boca: varicela",
    imagen: "flujogramas/vesiculas-costras-papulas-distintos-estadios-varicela.svg",
    alt: "Flujograma: Niño de 5 años con fiebre y lesiones que pican en distintos estadios (pápulas, vesículas y costras) en piel, cuero cabelludo y boca: varicela"
  },
  "PED-148": {
    titulo: "Niño de 3 años con dolor de garganta, congestión y rinorrea, afebril y con faringe sin inflamación: resfrío común",
    imagen: "flujogramas/preescolar-rinorrea-afebril-faringe-normal-resfrio-comun.svg",
    alt: "Flujograma: Niño de 3 años con dolor de garganta, congestión y rinorrea, afebril y con faringe sin inflamación: resfrío común"
  },
  "HEM-029": {
    titulo: "Séptico por piocolecisto con hematuria, púrpura, plaquetas 75 000, tiempos de coagulación prolongados y fibrinógeno bajo: coagulación intravascular diseminada",
    imagen: "flujogramas/sepsis-biliar-sangrado-fibrinogeno-bajo-cid.svg",
    alt: "Flujograma: Séptico por piocolecisto con hematuria, púrpura, plaquetas 75 000, tiempos de coagulación prolongados y fibrinógeno bajo: coagulación intravascular diseminada"
  },
  "GIN-146": {
    titulo: "Gestante a término con cesárea previa de incisión corporal (clásica) que inicia trabajo de parto con sangrado: cesárea de emergencia",
    imagen: "flujogramas/cesarea-corporal-previa-trabajo-parto-sangrado.svg",
    alt: "Flujograma: Gestante a término con cesárea previa de incisión corporal (clásica) que inicia trabajo de parto con sangrado: cesárea de emergencia"
  },
  "INF-078": {
    titulo: "Paciente con VIH, cefalea de 20 días que se vuelve insoportable y rigidez de nuca: meningitis criptocócica, se confirma con tinta china en el LCR",
    imagen: "flujogramas/vih-cefalea-subaguda-rigidez-tinta-china.svg",
    alt: "Flujograma: Paciente con VIH, cefalea de 20 días que se vuelve insoportable y rigidez de nuca: meningitis criptocócica, se confirma con tinta china en el LCR"
  },
  "END-043": {
    titulo: "Mujer con 5 meses de astenia, diarrea y pérdida de peso, hipotensa, con piel hiperpigmentada, hiperpotasemia, hiponatremia e hipoglucemia: enfermedad de Addison",
    imagen: "flujogramas/hiperpigmentacion-hipotension-hiperkalemia-addison.svg",
    alt: "Flujograma: Mujer con 5 meses de astenia, diarrea y pérdida de peso, hipotensa, con piel hiperpigmentada, hiperpotasemia, hiponatremia e hipoglucemia: enfermedad de Addison"
  },
  "TRA-033": {
    titulo: "Ante un traumatismo cervical alto, lo primero es inmovilizar la columna con collarín (restricción del movimiento) mientras se asegura la vía aérea",
    imagen: "flujogramas/trauma-cervical-alto-inmovilizar-collarin.svg",
    alt: "Flujograma: Ante un traumatismo cervical alto, lo primero es inmovilizar la columna con collarín (restricción del movimiento) mientras se asegura la vía aérea"
  },
  "SP-109": {
    titulo: "Distrito con desnutrición en aumento: el equipo de salud debe priorizar fortalecer la acción comunitaria para la salud",
    imagen: "flujogramas/distrito-desnutricion-accion-comunitaria.svg",
    alt: "Flujograma: Distrito con desnutrición en aumento: el equipo de salud debe priorizar fortalecer la acción comunitaria para la salud"
  },
  "SP-110": {
    titulo: "Rechazar la hipótesis nula cuando en realidad es verdadera (decir que hay efecto cuando no lo hay) es el error tipo I o alfa",
    imagen: "flujogramas/rechazar-hipotesis-nula-verdadera-error-alfa.svg",
    alt: "Flujograma: Rechazar la hipótesis nula cuando en realidad es verdadera (decir que hay efecto cuando no lo hay) es el error tipo I o alfa"
  },
  "NEF-067": {
    titulo: "Diarrea de alto flujo con diuresis de 200 mL en 24 h, sodio urinario < 20, FENa < 1 % y creatinina 1,8: lesión renal prerrenal, reto de fluidos",
    imagen: "flujogramas/diarrea-oliguria-fena-bajo-reto-fluidos.svg",
    alt: "Flujograma: Diarrea de alto flujo con diuresis de 200 mL en 24 h, sodio urinario < 20, FENa < 1 % y creatinina 1,8: lesión renal prerrenal, reto de fluidos"
  },
  "REU-044": {
    titulo: "Varón con años de dolor glúteo nocturno que mejora al moverse, Schober positivo y PCR alta: espondiloartritis axial (seronegativa)",
    imagen: "flujogramas/dolor-gluteo-nocturno-schober-espondiloartritis.svg",
    alt: "Flujograma: Varón con años de dolor glúteo nocturno que mejora al moverse, Schober positivo y PCR alta: espondiloartritis axial (seronegativa)"
  },
  "SP-111": {
    titulo: "Bocio difuso en un agricultor de Huancavelica, no aislado: el programa de salud pública es promover la sal yodada",
    imagen: "flujogramas/bocio-difuso-huancavelica-sal-yodada.svg",
    alt: "Flujograma: Bocio difuso en un agricultor de Huancavelica, no aislado: el programa de salud pública es promover la sal yodada"
  },
  "CB-055": {
    titulo: "Alcohólico desnutrido con epistaxis, encías que sangran, equimosis, petequias y dolor óseo: escorbuto por déficit de vitamina C",
    imagen: "flujogramas/alcoholico-gingivorragia-petequias-escorbuto.svg",
    alt: "Flujograma: Alcohólico desnutrido con epistaxis, encías que sangran, equimosis, petequias y dolor óseo: escorbuto por déficit de vitamina C"
  },
  "CAR-053": {
    titulo: "Coronario y diabético con LDL 120, HDL 35 y triglicéridos 245: el tratamiento indicado es una estatina de alta intensidad",
    imagen: "flujogramas/coronario-diabetico-ldl-120-estatina.svg",
    alt: "Flujograma: Coronario y diabético con LDL 120, HDL 35 y triglicéridos 245: el tratamiento indicado es una estatina de alta intensidad"
  },
  "END-044": {
    titulo: "Obeso con triglicéridos de 400 y HDL bajo: en la dieta se recomienda pescado azul (omega-3) y evitar grasas saturadas",
    imagen: "flujogramas/trigliceridos-400-dieta-pescado-azul.svg",
    alt: "Flujograma: Obeso con triglicéridos de 400 y HDL bajo: en la dieta se recomienda pescado azul (omega-3) y evitar grasas saturadas"
  },
  "SP-112": {
    titulo: "Estudio del efecto de la música de fondo sobre el uso de analgésicos: la música es la variable independiente y el uso de analgésicos la dependiente",
    imagen: "flujogramas/musica-de-fondo-analgesicos-variables.svg",
    alt: "Flujograma: Estudio del efecto de la música de fondo sobre el uso de analgésicos: la música es la variable independiente y el uso de analgésicos la dependiente"
  },
  "SP-113": {
    titulo: "El análisis de correlación permite identificar la asociación (fuerza y dirección de la relación) entre dos variables, no la causa",
    imagen: "flujogramas/insomnio-covid-analisis-correlacion.svg",
    alt: "Flujograma: El análisis de correlación permite identificar la asociación (fuerza y dirección de la relación) entre dos variables, no la causa"
  },
  "CB-056": {
    titulo: "Niño que vuelve del campo con dolor urente que se extiende, temblores, sudoración profusa, sialorrea y abdomen rígido: latrodectismo (viuda negra)",
    imagen: "flujogramas/dolor-lanceta-rigidez-abdominal-sudoracion-latrodectismo.svg",
    alt: "Flujograma: Niño que vuelve del campo con dolor urente que se extiende, temblores, sudoración profusa, sialorrea y abdomen rígido: latrodectismo (viuda negra)"
  },
  "HEM-030": {
    titulo: "Gestante de 6 meses con Hb 8, índices corpusculares bajos, anisocitosis, hipocromía, microcitos y reticulocitos bajos: anemia ferropénica",
    imagen: "flujogramas/gestante-hb-8-microcitica-reticulocitos-bajos.svg",
    alt: "Flujograma: Gestante de 6 meses con Hb 8, índices corpusculares bajos, anisocitosis, hipocromía, microcitos y reticulocitos bajos: anemia ferropénica"
  },
  "SP-114": {
    titulo: "En el personal de salud se consideran enfermedades profesionales la hepatitis, el VIH, la tuberculosis y la COVID-19 (riesgo biológico)",
    imagen: "flujogramas/personal-salud-enfermedad-profesional-biologica.svg",
    alt: "Flujograma: En el personal de salud se consideran enfermedades profesionales la hepatitis, el VIH, la tuberculosis y la COVID-19 (riesgo biológico)"
  },
  "GIN-147": {
    titulo: "En el embarazo gemelar a término, el manejo intraparto y la vía del parto los define la presentación de los gemelos (sobre todo la del primero)",
    imagen: "flujogramas/embarazo-gemelar-termino-presentacion-via-parto.svg",
    alt: "Flujograma: En el embarazo gemelar a término, el manejo intraparto y la vía del parto los define la presentación de los gemelos (sobre todo la del primero)"
  },
  "GIN-148": {
    titulo: "Gestante de 31 semanas con fiebre de 39 °C, contracciones y FCF 165: infección intraamniótica, los tocolíticos están contraindicados",
    imagen: "flujogramas/fiebre-31-semanas-taquicardia-fetal-no-tocolisis.svg",
    alt: "Flujograma: Gestante de 31 semanas con fiebre de 39 °C, contracciones y FCF 165: infección intraamniótica, los tocolíticos están contraindicados"
  },
  "GIN-149": {
    titulo: "Primigesta de 39 semanas con 3 cm de dilatación, buena dinámica y pelvis adecuada: está en fase latente, que deambule hasta la fase activa",
    imagen: "flujogramas/primigesta-3-cm-fase-latente-deambular.svg",
    alt: "Flujograma: Primigesta de 39 semanas con 3 cm de dilatación, buena dinámica y pelvis adecuada: está en fase latente, que deambule hasta la fase activa"
  },
  "END-045": {
    titulo: "Diabético insulinodependiente con diaforesis, palidez y desorientación 3 horas tras la insulina y glucosa de 38: hipoglucemia grave, dextrosa al 33 % EV",
    imagen: "flujogramas/insulina-glucosa-38-desorientado-dextrosa-33.svg",
    alt: "Flujograma: Diabético insulinodependiente con diaforesis, palidez y desorientación 3 horas tras la insulina y glucosa de 38: hipoglucemia grave, dextrosa al 33 % EV"
  },
  "GIN-150": {
    titulo: "La obesidad previa al embarazo no corregida se asocia a diabetes gestacional y a feto macrosómico",
    imagen: "flujogramas/obesidad-pregestacional-diabetes-macrosomia.svg",
    alt: "Flujograma: La obesidad previa al embarazo no corregida se asocia a diabetes gestacional y a feto macrosómico"
  },
  "GIN-151": {
    titulo: "Mujer con lupus y anticuerpos antifosfolípidos que pide anticoncepción: DIU de cobre (los estrógenos están contraindicados por riesgo de trombosis)",
    imagen: "flujogramas/lupus-antifosfolipidos-anticoncepcion-diu-cobre.svg",
    alt: "Flujograma: Mujer con lupus y anticuerpos antifosfolípidos que pide anticoncepción: DIU de cobre (los estrógenos están contraindicados por riesgo de trombosis)"
  },
  "CB-057": {
    titulo: "Los receptores del sabor están en las células neuroepiteliales (células receptoras) de los botones gustativos de la lengua",
    imagen: "flujogramas/covid-perdida-gusto-celulas-neuroepiteliales.svg",
    alt: "Flujograma: Los receptores del sabor están en las células neuroepiteliales (células receptoras) de los botones gustativos de la lengua"
  },
  "NRL-042": {
    titulo: "Mujer con ptosis y diplopía que empeoran con el esfuerzo por una enfermedad autoinmune de la placa: miastenia gravis, destrucción de los receptores de acetilcolina",
    imagen: "flujogramas/ptosis-diplopia-placa-mioneural-receptor-acetilcolina.svg",
    alt: "Flujograma: Mujer con ptosis y diplopía que empeoran con el esfuerzo por una enfermedad autoinmune de la placa: miastenia gravis, destrucción de los receptores de acetilcolina"
  },
  "GIN-152": {
    titulo: "Gestante de 10 semanas con hipertensión crónica que usa captopril: suspender el IECA y cambiar a metildopa (seguro en el embarazo)",
    imagen: "flujogramas/hta-cronica-gestante-captopril-metildopa.svg",
    alt: "Flujograma: Gestante de 10 semanas con hipertensión crónica que usa captopril: suspender el IECA y cambiar a metildopa (seguro en el embarazo)"
  },
  "GIN-153": {
    titulo: "La gestante adolescente tiene más riesgo de anemia, preeclampsia y parto pretérmino; la complicación a la que está menos expuesta por su edad es la diabetes",
    imagen: "flujogramas/gestante-16-anos-riesgo-menor-diabetes.svg",
    alt: "Flujograma: La gestante adolescente tiene más riesgo de anemia, preeclampsia y parto pretérmino; la complicación a la que está menos expuesta por su edad es la diabetes"
  },
  "CIR-087": {
    titulo: "Diabético e hipertenso de 74 años con dolor de pantorrillas al caminar que cede al reposo y pulso pedio disminuido: claudicación intermitente por enfermedad arterial periférica",
    imagen: "flujogramas/dolor-pantorrillas-al-caminar-cede-reposo-claudicacion.svg",
    alt: "Flujograma: Diabético e hipertenso de 74 años con dolor de pantorrillas al caminar que cede al reposo y pulso pedio disminuido: claudicación intermitente por enfermedad arterial periférica"
  },
  "NEF-068": {
    titulo: "Varón de 65 años con antecedente familiar, próstata indurada, PSA 11,5, Gleason bajo y sin extensión: cáncer de próstata localizado, prostatectomía radical",
    imagen: "flujogramas/psa-11-gleason-bajo-localizado-prostatectomia.svg",
    alt: "Flujograma: Varón de 65 años con antecedente familiar, próstata indurada, PSA 11,5, Gleason bajo y sin extensión: cáncer de próstata localizado, prostatectomía radical"
  },
  "CIR-088": {
    titulo: "Hernia crural con probable estrangulación que se reduce sola al inducir la anestesia: explorar el intestino por laparotomía mediana",
    imagen: "flujogramas/hernia-crural-estrangulada-reducida-anestesia-laparotomia.svg",
    alt: "Flujograma: Hernia crural con probable estrangulación que se reduce sola al inducir la anestesia: explorar el intestino por laparotomía mediana"
  },
  "CIR-089": {
    titulo: "Herida punzopenetrante precordial con hipotensión, ingurgitación yugular y ruidos cardíacos apagados (tríada de Beck): taponamiento cardíaco",
    imagen: "flujogramas/herida-precordial-triada-beck-taponamiento.svg",
    alt: "Flujograma: Herida punzopenetrante precordial con hipotensión, ingurgitación yugular y ruidos cardíacos apagados (tríada de Beck): taponamiento cardíaco"
  },
  "NRL-043": {
    titulo: "Hemorragia de fosa posterior que comprime el tronco con obnubilación progresiva e hipertensión endocraneana: ventriculostomía y craniectomía suboccipital",
    imagen: "flujogramas/hemorragia-fosa-posterior-compresion-tronco.svg",
    alt: "Flujograma: Hemorragia de fosa posterior que comprime el tronco con obnubilación progresiva e hipertensión endocraneana: ventriculostomía y craniectomía suboccipital"
  },
  "CB-058": {
    titulo: "Joven en coma profundo con piel fría, miosis, bradipnea y cianosis que no responde al flumazenilo: intoxicación por barbitúricos",
    imagen: "flujogramas/coma-bradipnea-flumazenilo-ineficaz-barbituricos.svg",
    alt: "Flujograma: Joven en coma profundo con piel fría, miosis, bradipnea y cianosis que no responde al flumazenilo: intoxicación por barbitúricos"
  },
  "NEU-041": {
    titulo: "Paciente hospitalizado con disnea súbita e hipoxemia, sin causa coronaria y con Rx de tórax normal: tromboembolismo pulmonar",
    imagen: "flujogramas/hospitalizado-disnea-subita-hipoxemia-rx-normal-tep.svg",
    alt: "Flujograma: Paciente hospitalizado con disnea súbita e hipoxemia, sin causa coronaria y con Rx de tórax normal: tromboembolismo pulmonar"
  },
  "CAR-054": {
    titulo: "Joven de 28 años con PA 200/135 en brazos, soplo sistólico que se irradia a la espalda y pulsos femorales pequeños: coartación de aorta",
    imagen: "flujogramas/hta-brazos-pulso-femoral-debil-coartacion.svg",
    alt: "Flujograma: Joven de 28 años con PA 200/135 en brazos, soplo sistólico que se irradia a la espalda y pulsos femorales pequeños: coartación de aorta"
  },
  "HEM-031": {
    titulo: "Mujer de 69 años en cama 2 semanas por neumonía con edema y dolor de la pierna derecha: trombosis venosa profunda",
    imagen: "flujogramas/encamada-2-semanas-pierna-edematosa-tvp.svg",
    alt: "Flujograma: Mujer de 69 años en cama 2 semanas por neumonía con edema y dolor de la pierna derecha: trombosis venosa profunda"
  },
  "CAR-055": {
    titulo: "Hipertenso con captopril y amlodipino que tiene tos seca sin causa respiratoria ni de ORL: retirar el captopril (tos por IECA)",
    imagen: "flujogramas/hipertenso-captopril-tos-seca-retirar-ieca.svg",
    alt: "Flujograma: Hipertenso con captopril y amlodipino que tiene tos seca sin causa respiratoria ni de ORL: retirar el captopril (tos por IECA)"
  },
  "HEM-032": {
    titulo: "Mujer con equimosis, fiebre y neumonía con leucocitos 1400, Hb 7,2 y plaquetas 35 000: pancitopenia, lo primero es preguntar por medicamentos mielotóxicos",
    imagen: "flujogramas/pancitopenia-fiebre-equimosis-farmacos-mielotoxicos.svg",
    alt: "Flujograma: Mujer con equimosis, fiebre y neumonía con leucocitos 1400, Hb 7,2 y plaquetas 35 000: pancitopenia, lo primero es preguntar por medicamentos mielotóxicos"
  },
  "CAR-056": {
    titulo: "Joven con fiebre de 2 meses, baja de peso, soplo de insuficiencia mitral por fiebre reumática y hemiparesia súbita: endocarditis infecciosa con embolia cerebral",
    imagen: "flujogramas/fiebre-2-meses-soplo-mitral-hemiparesia-endocarditis.svg",
    alt: "Flujograma: Joven con fiebre de 2 meses, baja de peso, soplo de insuficiencia mitral por fiebre reumática y hemiparesia súbita: endocarditis infecciosa con embolia cerebral"
  },
  "INF-079": {
    titulo: "Joven con febrícula, odinofagia, adenopatías generalizadas y linfocitos atípicos: mononucleosis, el factor de riesgo es el contacto estrecho por saliva (besos)",
    imagen: "flujogramas/odinofagia-adenopatias-linfocitos-atipicos-mononucleosis.svg",
    alt: "Flujograma: Joven con febrícula, odinofagia, adenopatías generalizadas y linfocitos atípicos: mononucleosis, el factor de riesgo es el contacto estrecho por saliva (besos)"
  },
  "GAS-055": {
    titulo: "Disfagia con mucosa roja 3 cm por encima de la línea Z y biopsia con epitelio cilíndrico con células caliciformes: esófago de Barrett, su complicación es el adenocarcinoma",
    imagen: "flujogramas/metaplasia-intestinal-esofago-distal-adenocarcinoma.svg",
    alt: "Flujograma: Disfagia con mucosa roja 3 cm por encima de la línea Z y biopsia con epitelio cilíndrico con células caliciformes: esófago de Barrett, su complicación es el adenocarcinoma"
  },
  "NEU-042": {
    titulo: "Hospitalizada tras un infarto cerebral que al caminar presenta disnea súbita grave, dolor torácico y dímero D alto: el siguiente examen es la angio-TC pulmonar",
    imagen: "flujogramas/postictus-disnea-subita-dimero-d-angiotem.svg",
    alt: "Flujograma: Hospitalizada tras un infarto cerebral que al caminar presenta disnea súbita grave, dolor torácico y dímero D alto: el siguiente examen es la angio-TC pulmonar"
  },
  "PED-149": {
    titulo: "Escolar con padre bacilífero, fiebre, tos seca, estridor, PPD positivo y auscultación normal: TB primaria, la Rx mostrará adenopatías hiliares",
    imagen: "flujogramas/nino-contacto-tb-estridor-adenopatias-hiliares.svg",
    alt: "Flujograma: Escolar con padre bacilífero, fiebre, tos seca, estridor, PPD positivo y auscultación normal: TB primaria, la Rx mostrará adenopatías hiliares"
  },
  "NEU-043": {
    titulo: "Joven sano con disnea súbita, murmullo abolido en el hemitórax derecho y desviación del mediastino que mejora con tubo: neumotórax espontáneo por rotura de bullas (enfisema acinar distal)",
    imagen: "flujogramas/joven-sano-disnea-subita-tubo-aire-bullas.svg",
    alt: "Flujograma: Joven sano con disnea súbita, murmullo abolido en el hemitórax derecho y desviación del mediastino que mejora con tubo: neumotórax espontáneo por rotura de bullas (enfisema acinar distal)"
  },
  "INF-080": {
    titulo: "Portadora de HTLV-1 con diarrea profusa, tos, eosinofilia y larvas rabditoides en heces y esputo: estrongiloidosis (hiperinfección)",
    imagen: "flujogramas/htlv1-diarrea-tos-larvas-rabditoides-estrongiloidosis.svg",
    alt: "Flujograma: Portadora de HTLV-1 con diarrea profusa, tos, eosinofilia y larvas rabditoides en heces y esputo: estrongiloidosis (hiperinfección)"
  },
  "INF-081": {
    titulo: "Campesino de Lurín con 7 días de fiebre, cefalea, mialgias intensas, ictericia e inyección conjuntival: leptospirosis (forma ictérica), penicilina EV",
    imagen: "flujogramas/campesino-ictericia-sufusion-conjuntival-penicilina.svg",
    alt: "Flujograma: Campesino de Lurín con 7 días de fiebre, cefalea, mialgias intensas, ictericia e inyección conjuntival: leptospirosis (forma ictérica), penicilina EV"
  },
  "INF-082": {
    titulo: "Escolar del sur del Perú con edema bipalpebral unilateral indoloro, conjuntivitis y adenopatía preauricular (signo de Romaña): enfermedad de Chagas aguda",
    imagen: "flujogramas/edema-bipalpebral-unilateral-romana-chagas.svg",
    alt: "Flujograma: Escolar del sur del Perú con edema bipalpebral unilateral indoloro, conjuntivitis y adenopatía preauricular (signo de Romaña): enfermedad de Chagas aguda"
  },
  "SP-115": {
    titulo: "Para saber qué regiones redujeron la discapacidad y la muerte prematura con una intervención, se usa el estudio de carga de enfermedad (AVAD)",
    imagen: "flujogramas/discapacidad-prematura-carga-enfermedad-avad.svg",
    alt: "Flujograma: Para saber qué regiones redujeron la discapacidad y la muerte prematura con una intervención, se usa el estudio de carga de enfermedad (AVAD)"
  },
  "PED-150": {
    titulo: "Lactante de 4 meses vacunado con BCG (con carné) que no tiene cicatriz ni nódulo: no requiere revacunación",
    imagen: "flujogramas/lactante-sin-cicatriz-bcg-no-revacunar.svg",
    alt: "Flujograma: Lactante de 4 meses vacunado con BCG (con carné) que no tiene cicatriz ni nódulo: no requiere revacunación"
  },
  "PED-151": {
    titulo: "Niña hospitalizada con sonda vesical que a los 2 días hace fiebre de 39 °C: sospechar infección urinaria asociada a catéter, pedir urocultivo con antibiograma",
    imagen: "flujogramas/nina-pci-sonda-vesical-fiebre-urocultivo.svg",
    alt: "Flujograma: Niña hospitalizada con sonda vesical que a los 2 días hace fiebre de 39 °C: sospechar infección urinaria asociada a catéter, pedir urocultivo con antibiograma"
  },
  "SP-116": {
    titulo: "Joven que estuvo hace 15 días en un país con sarampión, con fiebre, exantema maculopapular e IgM positiva: caso confirmado importado",
    imagen: "flujogramas/viajero-exantema-igm-sarampion-importado.svg",
    alt: "Flujograma: Joven que estuvo hace 15 días en un país con sarampión, con fiebre, exantema maculopapular e IgM positiva: caso confirmado importado"
  },
  "PED-152": {
    titulo: "Prematuro de 34 semanas con 48 horas, hipoactivo, con temblores y glucosa de 40 mg/dL: hipoglucemia sintomática, bolo de glucosa EV 200 mg/kg",
    imagen: "flujogramas/prematuro-34-sem-glucosa-40-tremores-bolo-ev.svg",
    alt: "Flujograma: Prematuro de 34 semanas con 48 horas, hipoactivo, con temblores y glucosa de 40 mg/dL: hipoglucemia sintomática, bolo de glucosa EV 200 mg/kg"
  },
  "GIN-154": {
    titulo: "La suplementación profiláctica de calcio en la gestante se da desde las 20 semanas hasta el término (previene la preeclampsia en poblaciones con poca ingesta)",
    imagen: "flujogramas/gestante-calcio-desde-20-semanas.svg",
    alt: "Flujograma: La suplementación profiláctica de calcio en la gestante se da desde las 20 semanas hasta el término (previene la preeclampsia en poblaciones con poca ingesta)"
  },
  "PED-153": {
    titulo: "En el control de crecimiento y desarrollo (CRED) del MINSA, el primer año tiene 4 controles en el primer mes y luego uno cada mes",
    imagen: "flujogramas/cred-primer-ano-controles-mensuales.svg",
    alt: "Flujograma: En el control de crecimiento y desarrollo (CRED) del MINSA, el primer año tiene 4 controles en el primer mes y luego uno cada mes"
  },
  "SP-117": {
    titulo: "En 1000 personas aparecen 45 casos nuevos de una enfermedad: la incidencia acumulada es 45 por 1000",
    imagen: "flujogramas/45-casos-nuevos-1000-personas-incidencia.svg",
    alt: "Flujograma: En 1000 personas aparecen 45 casos nuevos de una enfermedad: la incidencia acumulada es 45 por 1000"
  },
  "CB-059": {
    titulo: "Al administrar una vacuna se induce inmunidad activa artificial: el propio organismo produce anticuerpos y memoria",
    imagen: "flujogramas/vacuna-induce-inmunidad-activa-artificial.svg",
    alt: "Flujograma: Al administrar una vacuna se induce inmunidad activa artificial: el propio organismo produce anticuerpos y memoria"
  },
  "SP-118": {
    titulo: "Pseudomonas y otros gramnegativos en el agua potable del hospital: transmisión por vehículo (objeto o sustancia inanimada)",
    imagen: "flujogramas/agua-hospital-pseudomonas-transmision-vehiculo.svg",
    alt: "Flujograma: Pseudomonas y otros gramnegativos en el agua potable del hospital: transmisión por vehículo (objeto o sustancia inanimada)"
  },
  "SP-119": {
    titulo: "En la acreditación de los establecimientos de salud, la valoración que hace el propio personal de la institución es la autoevaluación",
    imagen: "flujogramas/acreditacion-evaluacion-personal-propio-autoevaluacion.svg",
    alt: "Flujograma: En la acreditación de los establecimientos de salud, la valoración que hace el propio personal de la institución es la autoevaluación"
  },
  "REU-045": {
    titulo: "Lactante de 18 meses con prurito, surcos y pápulas en muñecas, espacios interdigitales, palmas, plantas, tronco y cara: escabiosis, permetrina al 5 %",
    imagen: "flujogramas/lactante-surcos-prurito-palmas-plantas-permetrina.svg",
    alt: "Flujograma: Lactante de 18 meses con prurito, surcos y pápulas en muñecas, espacios interdigitales, palmas, plantas, tronco y cara: escabiosis, permetrina al 5 %"
  },
  "NEU-044": {
    titulo: "Entre los factores de riesgo de muerte por asma, el biológico es la resistencia a los corticoides (no mejora con ellos)",
    imagen: "flujogramas/asma-mortalidad-resistencia-corticoides.svg",
    alt: "Flujograma: Entre los factores de riesgo de muerte por asma, el biológico es la resistencia a los corticoides (no mejora con ellos)"
  },
  "REU-046": {
    titulo: "Lactante con fiebre de 39 °C, irritable, eritema difuso alrededor de los orificios y en pliegues con ampollas fláccidas y Nikolsky (+): síndrome de piel escaldada (Ritter)",
    imagen: "flujogramas/lactante-fiebre-ampollas-flacidas-nikolsky-ritter.svg",
    alt: "Flujograma: Lactante con fiebre de 39 °C, irritable, eritema difuso alrededor de los orificios y en pliegues con ampollas fláccidas y Nikolsky (+): síndrome de piel escaldada (Ritter)"
  },
  "REU-047": {
    titulo: "Adolescente deportista con uñas de ambos primeros dedos de los pies blanquecinas, engrosadas y despegadas del lecho: onicomicosis",
    imagen: "flujogramas/deportista-una-blanquecina-engrosada-onicomicosis.svg",
    alt: "Flujograma: Adolescente deportista con uñas de ambos primeros dedos de los pies blanquecinas, engrosadas y despegadas del lecho: onicomicosis"
  },
  "OFT-034": {
    titulo: "Niño de 2 años con desviación del ojo derecho hacia adentro y ausencia del reflejo rojo pupilar: retinoblastoma",
    imagen: "flujogramas/nino-2-anos-estrabismo-sin-reflejo-retinoblastoma.svg",
    alt: "Flujograma: Niño de 2 años con desviación del ojo derecho hacia adentro y ausencia del reflejo rojo pupilar: retinoblastoma"
  },
  "SP-120": {
    titulo: "Para que se produzca un brote de dengue se necesitan susceptibles, una persona enferma (con virus en la sangre) y el mosquito Aedes aegypti",
    imagen: "flujogramas/brote-dengue-susceptibles-enfermo-mosquito.svg",
    alt: "Flujograma: Para que se produzca un brote de dengue se necesitan susceptibles, una persona enferma (con virus en la sangre) y el mosquito Aedes aegypti"
  },
  "PED-154": {
    titulo: "La complicación inmediata más frecuente del recién nacido de muy bajo peso es la insuficiencia respiratoria (falta de surfactante)",
    imagen: "flujogramas/rn-muy-bajo-peso-complicacion-inmediata-respiratoria.svg",
    alt: "Flujograma: La complicación inmediata más frecuente del recién nacido de muy bajo peso es la insuficiencia respiratoria (falta de surfactante)"
  },
  "PED-155": {
    titulo: "Recién nacido de 5 horas con RPM de 18 horas, fiebre de 38 °C y succión débil: sospecha de sepsis precoz, el examen que confirma es el hemocultivo",
    imagen: "flujogramas/rn-rpm-18-horas-fiebre-succion-debil-hemocultivo.svg",
    alt: "Flujograma: Recién nacido de 5 horas con RPM de 18 horas, fiebre de 38 °C y succión débil: sospecha de sepsis precoz, el examen que confirma es el hemocultivo"
  },
  "TRA-034": {
    titulo: "Anciana diabética que se cae con dolor intenso, no puede mover la pierna y la tiene acortada y en rotación externa: fractura de cadera",
    imagen: "flujogramas/anciana-caida-pierna-acortada-rotacion-externa-cadera.svg",
    alt: "Flujograma: Anciana diabética que se cae con dolor intenso, no puede mover la pierna y la tiene acortada y en rotación externa: fractura de cadera"
  },
  "CIR-090": {
    titulo: "Politraumatizado con hipotensión, taquipnea, ingurgitación yugular, murmullo abolido y timpanismo en el hemitórax derecho: neumotórax a tensión",
    imagen: "flujogramas/trauma-hipotension-yugulares-timpanismo-neumotorax-tension.svg",
    alt: "Flujograma: Politraumatizado con hipotensión, taquipnea, ingurgitación yugular, murmullo abolido y timpanismo en el hemitórax derecho: neumotórax a tensión"
  },
  "CIR-091": {
    titulo: "Politraumatizado en choque que no responde a cristaloides, con abdomen que se distiende, hipotensión y bradicardia: transfundir de inmediato sangre O Rh negativo",
    imagen: "flujogramas/trauma-abdominal-choque-no-responde-sangre-o-negativo.svg",
    alt: "Flujograma: Politraumatizado en choque que no responde a cristaloides, con abdomen que se distiende, hipotensión y bradicardia: transfundir de inmediato sangre O Rh negativo"
  },
  "CAR-057": {
    titulo: "Durante la RCP el monitor muestra fibrilación ventricular: desfibrilar de inmediato y reanudar las compresiones sin esperar",
    imagen: "flujogramas/rcp-monitor-fibrilacion-ventricular-desfibrilar.svg",
    alt: "Flujograma: Durante la RCP el monitor muestra fibrilación ventricular: desfibrilar de inmediato y reanudar las compresiones sin esperar"
  },
  "GIN-155": {
    titulo: "Gestante de 18 semanas con pesadez pélvica, sin contracciones, con antecedentes de partos inmaduros tras RPM y cuello dilatado 5 cm: incompetencia cervical",
    imagen: "flujogramas/18-semanas-dilatacion-sin-contracciones-incompetencia-cervical.svg",
    alt: "Flujograma: Gestante de 18 semanas con pesadez pélvica, sin contracciones, con antecedentes de partos inmaduros tras RPM y cuello dilatado 5 cm: incompetencia cervical"
  },
  "NEU-045": {
    titulo: "El antituberculoso contraindicado en la gestante es la estreptomicina (aminoglucósido ototóxico para el feto)",
    imagen: "flujogramas/gestante-tuberculosis-estreptomicina-ototoxica.svg",
    alt: "Flujograma: El antituberculoso contraindicado en la gestante es la estreptomicina (aminoglucósido ototóxico para el feto)"
  },
  "GIN-156": {
    titulo: "Madre Rh negativo cuyo recién nacido también es Rh negativo: no se indica la inmunoglobulina anti-D (no hay riesgo de sensibilización)",
    imagen: "flujogramas/madre-rh-negativo-rn-rh-negativo-sin-anti-d.svg",
    alt: "Flujograma: Madre Rh negativo cuyo recién nacido también es Rh negativo: no se indica la inmunoglobulina anti-D (no hay riesgo de sensibilización)"
  },
  "GIN-157": {
    titulo: "Gestante de 42 semanas con monitoreo normal y Bishop desfavorable (4): madurar el cuello con misoprostol antes de inducir",
    imagen: "flujogramas/embarazo-42-semanas-bishop-4-misoprostol.svg",
    alt: "Flujograma: Gestante de 42 semanas con monitoreo normal y Bishop desfavorable (4): madurar el cuello con misoprostol antes de inducir"
  },
  "GIN-158": {
    titulo: "Gestante actual con antecedentes de un aborto, un ectópico, un parto a término y un hijo vivo: G4 P1021",
    imagen: "flujogramas/formula-obstetrica-aborto-ectopico-g4p1021.svg",
    alt: "Flujograma: Gestante actual con antecedentes de un aborto, un ectópico, un parto a término y un hijo vivo: G4 P1021"
  },
  "REU-048": {
    titulo: "Mujer joven con fiebre, artralgias de muñecas y monoartritis de rodilla con leucorrea: artritis gonocócica, el Gram del líquido muestra diplococos gramnegativos",
    imagen: "flujogramas/mujer-joven-leucorrea-artritis-diplococos-gram-negativos.svg",
    alt: "Flujograma: Mujer joven con fiebre, artralgias de muñecas y monoartritis de rodilla con leucorrea: artritis gonocócica, el Gram del líquido muestra diplococos gramnegativos"
  },
  "REU-049": {
    titulo: "Mujer joven con artritis, eritema malar, alopecia, derrame pleural, anemia, plaquetopenia y sedimento activo con cilindros: lupus eritematoso sistémico",
    imagen: "flujogramas/eritema-malar-derrame-cilindros-plaquetopenia-lupus.svg",
    alt: "Flujograma: Mujer joven con artritis, eritema malar, alopecia, derrame pleural, anemia, plaquetopenia y sedimento activo con cilindros: lupus eritematoso sistémico"
  },
  "END-046": {
    titulo: "Gestante de 10 semanas con hipertiroidismo por enfermedad de Graves (exoftalmos, mixedema pretibial, bocio, TSH suprimida): propiltiouracilo en el primer trimestre",
    imagen: "flujogramas/gestante-10-semanas-graves-propiltiouracilo.svg",
    alt: "Flujograma: Gestante de 10 semanas con hipertiroidismo por enfermedad de Graves (exoftalmos, mixedema pretibial, bocio, TSH suprimida): propiltiouracilo en el primer trimestre"
  },
  "END-047": {
    titulo: "Dolor cervical y tirotoxicosis 10 días después de una infección respiratoria, con tiroides dolorosa y TSH baja: tiroiditis subaguda de De Quervain, AINE y propranolol",
    imagen: "flujogramas/cuello-doloroso-postviral-tiroiditis-subaguda-aine.svg",
    alt: "Flujograma: Dolor cervical y tirotoxicosis 10 días después de una infección respiratoria, con tiroides dolorosa y TSH baja: tiroiditis subaguda de De Quervain, AINE y propranolol"
  },
  "END-048": {
    titulo: "Diabético tipo 2 con HbA1c 9,5 %, glucosa 450 y creatinina 2,3 que toma metformina: iniciar insulina",
    imagen: "flujogramas/hba1c-9-5-glucosa-450-creatinina-alta-insulina.svg",
    alt: "Flujograma: Diabético tipo 2 con HbA1c 9,5 %, glucosa 450 y creatinina 2,3 que toma metformina: iniciar insulina"
  },
  "NRL-044": {
    titulo: "Varón con 7 meses de euforia, irritabilidad, desinhibición (se orina y desnuda en público), descuido personal y mal juicio: síndrome prefrontal",
    imagen: "flujogramas/desinhibicion-euforia-descuido-sindrome-prefrontal.svg",
    alt: "Flujograma: Varón con 7 meses de euforia, irritabilidad, desinhibición (se orina y desnuda en público), descuido personal y mal juicio: síndrome prefrontal"
  },
  "NRL-045": {
    titulo: "Mujer con cefalea semanal opresiva «en banda» de 2-6 horas que cede con AINE y contractura cervical: cefalea tensional",
    imagen: "flujogramas/cefalea-en-banda-semanal-cede-aine-tensional.svg",
    alt: "Flujograma: Mujer con cefalea semanal opresiva «en banda» de 2-6 horas que cede con AINE y contractura cervical: cefalea tensional"
  },
  "NRL-046": {
    titulo: "Anciano con fibrilación auricular sin anticoagular que en 2 horas desarrolla afasia y hemiparesia derecha, con TC normal: ACV isquémico (cardioembólico)",
    imagen: "flujogramas/fibrilacion-auricular-afasia-hemiparesia-tac-normal.svg",
    alt: "Flujograma: Anciano con fibrilación auricular sin anticoagular que en 2 horas desarrolla afasia y hemiparesia derecha, con TC normal: ACV isquémico (cardioembólico)"
  },
  "REU-050": {
    titulo: "Varón con eritrodermia, uñas en dedal y placas eritematosas con escamas nacaradas en codos, rodillas y cuero cabelludo: psoriasis",
    imagen: "flujogramas/placas-escamas-nacaradas-una-en-dedal-psoriasis.svg",
    alt: "Flujograma: Varón con eritrodermia, uñas en dedal y placas eritematosas con escamas nacaradas en codos, rodillas y cuero cabelludo: psoriasis"
  },
  "PED-156": {
    titulo: "Escolar con fiebre, odinofagia, amígdalas con pus, petequias en el paladar, vómitos y dolor abdominal: faringoamigdalitis estreptocócica",
    imagen: "flujogramas/escolar-amigdalas-pus-petequias-paladar-estreptococo.svg",
    alt: "Flujograma: Escolar con fiebre, odinofagia, amígdalas con pus, petequias en el paladar, vómitos y dolor abdominal: faringoamigdalitis estreptocócica"
  },
  "SP-121": {
    titulo: "En un experimento, la variable dependiente es aquella en la que se observan los cambios (el efecto que se mide)",
    imagen: "flujogramas/experimento-variable-dependiente-se-observan-cambios.svg",
    alt: "Flujograma: En un experimento, la variable dependiente es aquella en la que se observan los cambios (el efecto que se mide)"
  },
  "PSI-031": {
    titulo: "Bebedor fuerte al 2.º día de una operación con confusión, zoopsias, fiebre, taquicardia, midriasis, temblor y sudoración: síndrome de abstinencia alcohólica (delirium tremens)",
    imagen: "flujogramas/postoperado-alucinaciones-zoopsias-temblor-delirium-tremens.svg",
    alt: "Flujograma: Bebedor fuerte al 2.º día de una operación con confusión, zoopsias, fiebre, taquicardia, midriasis, temblor y sudoración: síndrome de abstinencia alcohólica (delirium tremens)"
  },
  "REU-051": {
    titulo: "Preescolar que tras comer cítricos presenta ronchas de distintos tamaños, rojas con centro pálido y muy pruriginosas: urticaria aguda",
    imagen: "flujogramas/preescolar-citricos-habones-urticaria-aguda.svg",
    alt: "Flujograma: Preescolar que tras comer cítricos presenta ronchas de distintos tamaños, rojas con centro pálido y muy pruriginosas: urticaria aguda"
  },
  "GIN-159": {
    titulo: "Para la endometritis puerperal el tratamiento antibiótico de elección es clindamicina + gentamicina EV",
    imagen: "flujogramas/puerpera-endometritis-clindamicina-gentamicina.svg",
    alt: "Flujograma: Para la endometritis puerperal el tratamiento antibiótico de elección es clindamicina + gentamicina EV"
  },
  "REU-052": {
    titulo: "Niño con urticaria previa que presenta vesículas sobre zonas de rascado que se rompen y dejan erosiones con costras melicéricas: piodermitis (impétigo)",
    imagen: "flujogramas/vesiculas-rascado-costras-mielicericas-impetigo.svg",
    alt: "Flujograma: Niño con urticaria previa que presenta vesículas sobre zonas de rascado que se rompen y dejan erosiones con costras melicéricas: piodermitis (impétigo)"
  },
  "GIN-160": {
    titulo: "El objetivo de aumentar las proteínas en el embarazo es cubrir las necesidades de la madre y del feto",
    imagen: "flujogramas/gestante-aumentar-proteinas-necesidad-materno-fetal.svg",
    alt: "Flujograma: El objetivo de aumentar las proteínas en el embarazo es cubrir las necesidades de la madre y del feto"
  },
  "OFT-035": {
    titulo: "Joven con 5 días de odinofagia, fiebre, otalgia derecha, trismus y amígdala derecha abombada con pus: absceso periamigdalino",
    imagen: "flujogramas/odinofagia-trismus-otalgia-absceso-periamigdalino.svg",
    alt: "Flujograma: Joven con 5 días de odinofagia, fiebre, otalgia derecha, trismus y amígdala derecha abombada con pus: absceso periamigdalino"
  },
  "CIR-092": {
    titulo: "Quemadura con agua hirviendo en ambas caras de los dos miembros superiores y la cara anterior del tronco: 36 % de superficie corporal (regla de los 9)",
    imagen: "flujogramas/escaldadura-brazos-tronco-anterior-36-por-ciento.svg",
    alt: "Flujograma: Quemadura con agua hirviendo en ambas caras de los dos miembros superiores y la cara anterior del tronco: 36 % de superficie corporal (regla de los 9)"
  },
  "GAS-056": {
    titulo: "Joven con ictericia de una semana, luego vómitos y desorientación, flapping, equimosis y glucosa de 55: insuficiencia hepática aguda",
    imagen: "flujogramas/ictericia-flapping-sangrado-hipoglucemia-falla-hepatica-aguda.svg",
    alt: "Flujograma: Joven con ictericia de una semana, luego vómitos y desorientación, flapping, equimosis y glucosa de 55: insuficiencia hepática aguda"
  },
  "GAS-057": {
    titulo: "Mujer con úlcera péptica mal tratada con melena, hematemesis abundante, PA 80/40 y FC 118: choque hipovolémico por hemorragia digestiva alta",
    imagen: "flujogramas/melena-hematemesis-hipotension-shock-hipovolemico.svg",
    alt: "Flujograma: Mujer con úlcera péptica mal tratada con melena, hematemesis abundante, PA 80/40 y FC 118: choque hipovolémico por hemorragia digestiva alta"
  },
  "CB-060": {
    titulo: "El SARS-CoV-2 infecta directamente a los neumocitos tipo II, que tienen el receptor ACE2",
    imagen: "flujogramas/covid-hipoxemia-neumocito-tipo-ii-ace2.svg",
    alt: "Flujograma: El SARS-CoV-2 infecta directamente a los neumocitos tipo II, que tienen el receptor ACE2"
  },
  "NEF-069": {
    titulo: "Criptorquidia bilateral no corregida: el calor del abdomen destruye la espermatogénesis y lleva a la azoospermia (infertilidad)",
    imagen: "flujogramas/criptorquidia-bilateral-no-tratada-azoospermia.svg",
    alt: "Flujograma: Criptorquidia bilateral no corregida: el calor del abdomen destruye la espermatogénesis y lleva a la azoospermia (infertilidad)"
  },
  "GIN-161": {
    titulo: "Primigesta de 37 semanas con PA 140/90, cefalea, alteraciones visuales y proteinuria de 500 mg/24 h: preeclampsia",
    imagen: "flujogramas/primigesta-37-sem-pa-140-proteinuria-preeclampsia.svg",
    alt: "Flujograma: Primigesta de 37 semanas con PA 140/90, cefalea, alteraciones visuales y proteinuria de 500 mg/24 h: preeclampsia"
  },
  "GIN-162": {
    titulo: "Mujer agredida sexualmente hace 3 horas: la profilaxis antibiótica específica cubre Chlamydia y gonorrea (más tricomonas)",
    imagen: "flujogramas/agresion-sexual-profilaxis-gonorrea-chlamydia.svg",
    alt: "Flujograma: Mujer agredida sexualmente hace 3 horas: la profilaxis antibiótica específica cubre Chlamydia y gonorrea (más tricomonas)"
  },
  "PED-157": {
    titulo: "Recién nacido de madre diabética sin meconio, con distensión, fístula uretral y periné hipotrófico: ano imperforado (malformación anorrectal alta)",
    imagen: "flujogramas/rn-distension-sin-meconio-fistula-uretral-ano-imperforado.svg",
    alt: "Flujograma: Recién nacido de madre diabética sin meconio, con distensión, fístula uretral y periné hipotrófico: ano imperforado (malformación anorrectal alta)"
  },
  "CIR-093": {
    titulo: "Diabética de 67 años con claudicación desde hace 9 meses y necrosis del 5.º dedo del pie: enfermedad arterial periférica, Fontaine estadio IV",
    imagen: "flujogramas/diabetica-claudicacion-necrosis-quinto-dedo-fontaine-iv.svg",
    alt: "Flujograma: Diabética de 67 años con claudicación desde hace 9 meses y necrosis del 5.º dedo del pie: enfermedad arterial periférica, Fontaine estadio IV"
  },
  "OFT-036": {
    titulo: "Mujer joven con ojo rojo, secreción y conjuntiva con folículos y papilas: conjuntivitis de inclusión por Chlamydia, el antibiótico es la doxiciclina oral",
    imagen: "flujogramas/conjuntivitis-folicular-papilar-otalgia-chlamydia-doxiciclina.svg",
    alt: "Flujograma: Mujer joven con ojo rojo, secreción y conjuntiva con folículos y papilas: conjuntivitis de inclusión por Chlamydia, el antibiótico es la doxiciclina oral"
  },
  "CIR-094": {
    titulo: "Adolescente con dolor escrotal súbito de 2 horas, testículo derecho doloroso y transiluminación negativa: torsión testicular, detorsión y orquidopexia bilateral",
    imagen: "flujogramas/adolescente-dolor-escrotal-subito-detorsion-orquidopexia.svg",
    alt: "Flujograma: Adolescente con dolor escrotal súbito de 2 horas, testículo derecho doloroso y transiluminación negativa: torsión testicular, detorsión y orquidopexia bilateral"
  },
  "CIR-095": {
    titulo: "Herida por bala en el mesogastrio con taquicardia, diaforesis y dolor abdominal difuso: laparotomía exploratoria",
    imagen: "flujogramas/herida-bala-mesogastrio-taquicardia-laparotomia.svg",
    alt: "Flujograma: Herida por bala en el mesogastrio con taquicardia, diaforesis y dolor abdominal difuso: laparotomía exploratoria"
  },
  "GAS-058": {
    titulo: "El cáncer colorrectal da metástasis sobre todo en el hígado, porque su sangre venosa drena por la vena porta",
    imagen: "flujogramas/cancer-colorrectal-metastasis-higado-via-portal.svg",
    alt: "Flujograma: El cáncer colorrectal da metástasis sobre todo en el hígado, porque su sangre venosa drena por la vena porta"
  },
  "OFT-037": {
    titulo: "Golpe con un palo en el ojo con pupila deformada, hemorragia subconjuntival e hifema: proteger el ojo con escudo rígido y derivar al oftalmólogo",
    imagen: "flujogramas/golpe-ocular-pupila-deformada-hifema-proteger-derivar.svg",
    alt: "Flujograma: Golpe con un palo en el ojo con pupila deformada, hemorragia subconjuntival e hifema: proteger el ojo con escudo rígido y derivar al oftalmólogo"
  },
  "CB-061": {
    titulo: "Agricultor con sialorrea, vómitos, bradicardia, roncantes y fasciculaciones: intoxicación por organofosforados, atropina",
    imagen: "flujogramas/agricultor-sialorrea-bradicardia-fasciculaciones-atropina.svg",
    alt: "Flujograma: Agricultor con sialorrea, vómitos, bradicardia, roncantes y fasciculaciones: intoxicación por organofosforados, atropina"
  },
  "CAR-058": {
    titulo: "ST elevado de V2 a V6 con PA 70/40, taquicardia, desaturación y crepitantes: infarto anterior extenso con choque cardiogénico",
    imagen: "flujogramas/st-elevado-v2-v6-hipotension-shock-cardiogenico.svg",
    alt: "Flujograma: ST elevado de V2 a V6 con PA 70/40, taquicardia, desaturación y crepitantes: infarto anterior extenso con choque cardiogénico"
  },
  "INF-083": {
    titulo: "Diabética mal controlada con dolor facial, escara necrótica negra y destrucción ósea del seno maxilar: mucormicosis rinocerebral",
    imagen: "flujogramas/diabetica-escara-necrotica-destruccion-maxilar-mucormicosis.svg",
    alt: "Flujograma: Diabética mal controlada con dolor facial, escara necrótica negra y destrucción ósea del seno maxilar: mucormicosis rinocerebral"
  },
  "CAR-059": {
    titulo: "Mujer de 65 años con disnea a pequeños esfuerzos, ortopnea, edema 4+ y crepitantes en dos tercios de ambos pulmones con PA normal: insuficiencia cardiaca descompensada, furosemida",
    imagen: "flujogramas/ortopnea-edema-crepitantes-insuficiencia-cardiaca-furosemida.svg",
    alt: "Flujograma: Mujer de 65 años con disnea a pequeños esfuerzos, ortopnea, edema 4+ y crepitantes en dos tercios de ambos pulmones con PA normal: insuficiencia cardiaca descompensada, furosemida"
  },
  "PED-158": {
    titulo: "Lactante de 6 meses que balbucea, sonríe, se sienta sin apoyo y pasa un cubo de mano a mano, pero aún no gatea: desarrollo normal",
    imagen: "flujogramas/lactante-6-meses-se-sienta-balbucea-no-gatea-normal.svg",
    alt: "Flujograma: Lactante de 6 meses que balbucea, sonríe, se sienta sin apoyo y pasa un cubo de mano a mano, pero aún no gatea: desarrollo normal"
  },
  "GIN-163": {
    titulo: "Parto de un feto de 4200 g con desgarro que llega al esfínter anal: desgarro perineal de III grado, reparación en sala de operaciones",
    imagen: "flujogramas/macrosomico-desgarro-hasta-esfinter-anal-tercer-grado.svg",
    alt: "Flujograma: Parto de un feto de 4200 g con desgarro que llega al esfínter anal: desgarro perineal de III grado, reparación en sala de operaciones"
  },
  "PED-159": {
    titulo: "Niño de 3 años con diarrea y vómitos, llenado capilar > 3 s, pulsos débiles, acrocianosis e hipotensión: shock hipovolémico, bolo de cloruro de sodio 0,9 % a 20 mL/kg",
    imagen: "flujogramas/nino-diarrea-llenado-capilar-lento-hipotension-bolo-20.svg",
    alt: "Flujograma: Niño de 3 años con diarrea y vómitos, llenado capilar > 3 s, pulsos débiles, acrocianosis e hipotensión: shock hipovolémico, bolo de cloruro de sodio 0,9 % a 20 mL/kg"
  },
  "PED-160": {
    titulo: "Neonato con tejido carnoso que crece en el ombligo tras caer el cordón, con secreción amarillenta: granuloma umbilical, nitrato de plata",
    imagen: "flujogramas/neonato-tejido-carnoso-umbilical-nitrato-plata.svg",
    alt: "Flujograma: Neonato con tejido carnoso que crece en el ombligo tras caer el cordón, con secreción amarillenta: granuloma umbilical, nitrato de plata"
  },
  "TRA-035": {
    titulo: "Politraumatizado en coma con SatO₂ 84 %: lo primero es la vía aérea con control cervical y el oxígeno",
    imagen: "flujogramas/politrauma-coma-sato2-84-oxigenoterapia.svg",
    alt: "Flujograma: Politraumatizado en coma con SatO₂ 84 %: lo primero es la vía aérea con control cervical y el oxígeno"
  },
  "PED-161": {
    titulo: "Neonato postérmino de 3,9 kg, hipoactivo y con pobre succión, glucosa 40 mg/dL: hipoglucemia sintomática, bolo de dextrosa al 10 % 2 mL/kg (≈ 8 mL) EV",
    imagen: "flujogramas/neonato-3900-g-glucosa-40-dextrosa-8-ml.svg",
    alt: "Flujograma: Neonato postérmino de 3,9 kg, hipoactivo y con pobre succión, glucosa 40 mg/dL: hipoglucemia sintomática, bolo de dextrosa al 10 % 2 mL/kg (≈ 8 mL) EV"
  },
  "PED-162": {
    titulo: "Neonato de 36 horas con fiebre, Silverman 6, subcrepitantes e infiltrado bilateral tras rotura prematura de membranas: neumonía neonatal, la leucocitosis con neutrofilia apoya la infección bacteriana",
    imagen: "flujogramas/neonato-rpm-fiebre-infiltrado-leucocitosis-neutrofilia.svg",
    alt: "Flujograma: Neonato de 36 horas con fiebre, Silverman 6, subcrepitantes e infiltrado bilateral tras rotura prematura de membranas: neumonía neonatal, la leucocitosis con neutrofilia apoya la infección bacteriana"
  },
  "SP-122": {
    titulo: "Las 4C del manejo de las ITS son consejería, condones, cumplimiento del tratamiento y contactos; la «calidad de atención» no es una de ellas",
    imagen: "flujogramas/manejo-its-cuatro-c-no-calidad.svg",
    alt: "Flujograma: Las 4C del manejo de las ITS son consejería, condones, cumplimiento del tratamiento y contactos; la «calidad de atención» no es una de ellas"
  },
  "OFT-038": {
    titulo: "Niño con una pila de botón en el conducto auditivo desde hace 1 hora: extracción inmediata con pinza bajo visión directa, sin lavados",
    imagen: "flujogramas/nino-pila-boton-oido-extraccion-pinza.svg",
    alt: "Flujograma: Niño con una pila de botón en el conducto auditivo desde hace 1 hora: extracción inmediata con pinza bajo visión directa, sin lavados"
  },
  "SP-123": {
    titulo: "Para conocer la probabilidad de que un hipertenso fumador tenga cardiopatía isquémica en 5 años se usa la incidencia acumulada de ese grupo",
    imagen: "flujogramas/hipertenso-fumador-probabilidad-5-anos-incidencia-acumulada.svg",
    alt: "Flujograma: Para conocer la probabilidad de que un hipertenso fumador tenga cardiopatía isquémica en 5 años se usa la incidencia acumulada de ese grupo"
  },
  "SP-124": {
    titulo: "La familia cuyos hijos se van a estudiar, trabajar o vivir en pareja está en la fase de dispersión del ciclo vital familiar",
    imagen: "flujogramas/hijos-dejan-hogar-ciclo-vital-dispersion.svg",
    alt: "Flujograma: La familia cuyos hijos se van a estudiar, trabajar o vivir en pareja está en la fase de dispersión del ciclo vital familiar"
  },
  "SP-125": {
    titulo: "Evaluar el estado cognitivo, afectivo y sociofamiliar es parte de la valoración clínica integral del adulto mayor (VACAM / valoración geriátrica integral)",
    imagen: "flujogramas/valoracion-cognitiva-afectiva-sociofamiliar-adulto-mayor.svg",
    alt: "Flujograma: Evaluar el estado cognitivo, afectivo y sociofamiliar es parte de la valoración clínica integral del adulto mayor (VACAM / valoración geriátrica integral)"
  },
  "PED-163": {
    titulo: "En el recién nacido pretérmino la cardiopatía congénita acianótica más frecuente es la persistencia del conducto arterioso",
    imagen: "flujogramas/prematuro-cardiopatia-acianotica-ductus-permeable.svg",
    alt: "Flujograma: En el recién nacido pretérmino la cardiopatía congénita acianótica más frecuente es la persistencia del conducto arterioso"
  },
  "END-049": {
    titulo: "Gestante de 20 semanas con fiebre de 39,8 °C, FC 150, confusión, diarrea, exoftalmos, bocio e ingurgitación yugular: tormenta tiroidea",
    imagen: "flujogramas/gestante-fiebre-taquicardia-150-confusa-tormenta-tiroidea.svg",
    alt: "Flujograma: Gestante de 20 semanas con fiebre de 39,8 °C, FC 150, confusión, diarrea, exoftalmos, bocio e ingurgitación yugular: tormenta tiroidea"
  },
  "PED-164": {
    titulo: "Recién nacido a término con Apgar 3 al minuto y 4 a los 5, 10 y 15 minutos, y acidosis metabólica (pH 7,0, déficit de base −10): asfixia perinatal",
    imagen: "flujogramas/rn-apgar-bajo-ph-7-deficit-base-asfixia.svg",
    alt: "Flujograma: Recién nacido a término con Apgar 3 al minuto y 4 a los 5, 10 y 15 minutos, y acidosis metabólica (pH 7,0, déficit de base −10): asfixia perinatal"
  },
  "GAS-059": {
    titulo: "Fumador de 67 años con ictericia, acolia, dolor epigástrico irradiado a la espalda, baja de 10 kg, masa epigástrica y CA 19-9 elevado: cáncer de cabeza de páncreas",
    imagen: "flujogramas/fumador-ictericia-acolia-masa-epigastrica-ca199-pancreas.svg",
    alt: "Flujograma: Fumador de 67 años con ictericia, acolia, dolor epigástrico irradiado a la espalda, baja de 10 kg, masa epigástrica y CA 19-9 elevado: cáncer de cabeza de páncreas"
  },
  "PED-165": {
    titulo: "Lactante con diarrea acuosa explosiva de inicio brusco, sin moco ni sangre, febrícula y dolor abdominal: diarrea secretora por E. coli enterotoxigénica",
    imagen: "flujogramas/lactante-diarrea-acuosa-explosiva-ecet.svg",
    alt: "Flujograma: Lactante con diarrea acuosa explosiva de inicio brusco, sin moco ni sangre, febrícula y dolor abdominal: diarrea secretora por E. coli enterotoxigénica"
  },
  "PED-166": {
    titulo: "La intervención individual que potencia las habilidades del niño para su desarrollo integral es la estimulación temprana",
    imagen: "flujogramas/intervencion-individual-potenciar-desarrollo-estimulacion-temprana.svg",
    alt: "Flujograma: La intervención individual que potencia las habilidades del niño para su desarrollo integral es la estimulación temprana"
  },
  "NEF-070": {
    titulo: "Joven con cáncer testicular no seminomatoso: el marcador para el seguimiento es la alfafetoproteína (junto a hCG y LDH)",
    imagen: "flujogramas/tumor-testicular-no-seminoma-alfafetoproteina.svg",
    alt: "Flujograma: Joven con cáncer testicular no seminomatoso: el marcador para el seguimiento es la alfafetoproteína (junto a hCG y LDH)"
  },
  "NEF-071": {
    titulo: "Niño con impétigo hace 3 semanas que presenta oliguria, hematuria, edema periorbitario, PA 140/90 y C3 bajo: glomerulonefritis postestreptocócica",
    imagen: "flujogramas/nino-impetigo-previo-hematuria-edema-c3-bajo-gnpe.svg",
    alt: "Flujograma: Niño con impétigo hace 3 semanas que presenta oliguria, hematuria, edema periorbitario, PA 140/90 y C3 bajo: glomerulonefritis postestreptocócica"
  },
  "PED-167": {
    titulo: "Niña de 4 años con fiebre, dolor en flancos, vómitos, disuria, polaquiuria y enuresis: pielonefritis; se confirma con urocultivo de chorro medio > 100 000 UFC/mL",
    imagen: "flujogramas/nina-fiebre-dolor-flanco-disuria-urocultivo.svg",
    alt: "Flujograma: Niña de 4 años con fiebre, dolor en flancos, vómitos, disuria, polaquiuria y enuresis: pielonefritis; se confirma con urocultivo de chorro medio > 100 000 UFC/mL"
  },
  "TRA-036": {
    titulo: "Atropellado con Glasgow 10, FR 34, herida de cuero cabelludo y deformidad del muslo: lo primero es despejar la vía aérea y proteger el cuello",
    imagen: "flujogramas/atropello-glasgow-10-via-aerea-proteccion-cervical.svg",
    alt: "Flujograma: Atropellado con Glasgow 10, FR 34, herida de cuero cabelludo y deformidad del muslo: lo primero es despejar la vía aérea y proteger el cuello"
  },
  "PSI-032": {
    titulo: "Mujer joven con atracones recurrentes seguidos de purgas para no subir de peso: bulimia nerviosa",
    imagen: "flujogramas/atracones-purgas-compensatorias-bulimia.svg",
    alt: "Flujograma: Mujer joven con atracones recurrentes seguidos de purgas para no subir de peso: bulimia nerviosa"
  },
  "END-050": {
    titulo: "Mujer tratada con yodo radiactivo hace 6 meses que presenta debilidad muscular con CPK y mioglobina altas: miopatía por hipotiroidismo",
    imagen: "flujogramas/yodo-radiactivo-debilidad-cpk-alta-hipotiroidismo.svg",
    alt: "Flujograma: Mujer tratada con yodo radiactivo hace 6 meses que presenta debilidad muscular con CPK y mioglobina altas: miopatía por hipotiroidismo"
  },
  "PSI-033": {
    titulo: "Adolescente que tras una discusión presenta desconexión, opistótonos y movimientos rotatorios en la cama, con recuperación inmediata y sin antecedentes: crisis psicógena no epiléptica",
    imagen: "flujogramas/adolescente-discusion-opistotonos-crisis-psicogena.svg",
    alt: "Flujograma: Adolescente que tras una discusión presenta desconexión, opistótonos y movimientos rotatorios en la cama, con recuperación inmediata y sin antecedentes: crisis psicógena no epiléptica"
  },
  "GAS-060": {
    titulo: "Pancreatitis crónica alcohólica con dolor nuevo y baja de 5 kg en 2 meses: pedir tomografía de abdomen para descartar cáncer de páncreas",
    imagen: "flujogramas/pancreatitis-cronica-baja-peso-dolor-tomografia.svg",
    alt: "Flujograma: Pancreatitis crónica alcohólica con dolor nuevo y baja de 5 kg en 2 meses: pedir tomografía de abdomen para descartar cáncer de páncreas"
  },
  "NEU-046": {
    titulo: "Deportista con deterioro grave tras esfuerzo en la altura: la ventilación mecánica se indica por hipercapnia severa (falla de la ventilación)",
    imagen: "flujogramas/maratonista-altura-deterioro-hipercapnia-ventilacion.svg",
    alt: "Flujograma: Deportista con deterioro grave tras esfuerzo en la altura: la ventilación mecánica se indica por hipercapnia severa (falla de la ventilación)"
  },
  "CAR-060": {
    titulo: "Paciente que hace paro dentro de emergencia y no responde al soporte básico: lo siguiente es conectar el monitor desfibrilador para ver el ritmo",
    imagen: "flujogramas/paro-intrahospitalario-soporte-basico-monitor-desfibrilador.svg",
    alt: "Flujograma: Paciente que hace paro dentro de emergencia y no responde al soporte básico: lo siguiente es conectar el monitor desfibrilador para ver el ritmo"
  },
  "NEU-047": {
    titulo: "Por el ritmo circadiano, las crisis de asma son más frecuentes de madrugada, entre las 4 y las 6 de la mañana",
    imagen: "flujogramas/asma-ritmo-circadiano-crisis-madrugada.svg",
    alt: "Flujograma: Por el ritmo circadiano, las crisis de asma son más frecuentes de madrugada, entre las 4 y las 6 de la mañana"
  },
  "INF-084": {
    titulo: "Gestante con fiebre de 39 °C, mialgias y dolor retroocular tras viajar a Tumbes: dengue; para la fiebre y el dolor solo paracetamol",
    imagen: "flujogramas/gestante-fiebre-retroocular-tumbes-dengue-paracetamol.svg",
    alt: "Flujograma: Gestante con fiebre de 39 °C, mialgias y dolor retroocular tras viajar a Tumbes: dengue; para la fiebre y el dolor solo paracetamol"
  },
  "INF-085": {
    titulo: "Diabética con absceso dental que empeora pese a penicilina y ciprofloxacino, con fiebre y celulitis facial: hospitalizar con antibióticos EV de amplio espectro (vancomicina + clindamicina en esta pregunta) y drenar",
    imagen: "flujogramas/diabetica-celulitis-facial-odontogena-vancomicina-clindamicina.svg",
    alt: "Flujograma: Diabética con absceso dental que empeora pese a penicilina y ciprofloxacino, con fiebre y celulitis facial: hospitalizar con antibióticos EV de amplio espectro (vancomicina + clindamicina en esta pregunta) y drenar"
  },
  "NEU-048": {
    titulo: "Paciente en tratamiento antituberculoso con artritis del primer ortejo y ácido úrico de 12: gota por pirazinamida, retirarla",
    imagen: "flujogramas/tbc-pleural-podagra-acido-urico-retirar-pirazinamida.svg",
    alt: "Flujograma: Paciente en tratamiento antituberculoso con artritis del primer ortejo y ácido úrico de 12: gota por pirazinamida, retirarla"
  },
  "NEU-049": {
    titulo: "Joven con un mes de fiebre, tos y dolor pleurítico, con derrame exudativo linfocítico y glucosa normal: tuberculosis pleural, pedir ADA en el líquido",
    imagen: "flujogramas/derrame-linfocitico-exudado-joven-ada-tuberculosis.svg",
    alt: "Flujograma: Joven con un mes de fiebre, tos y dolor pleurítico, con derrame exudativo linfocítico y glucosa normal: tuberculosis pleural, pedir ADA en el líquido"
  },
  "CAR-061": {
    titulo: "La causa más frecuente de muerte por infarto antes de llegar al hospital es la fibrilación ventricular",
    imagen: "flujogramas/infarto-muerte-prehospitalaria-fibrilacion-ventricular.svg",
    alt: "Flujograma: La causa más frecuente de muerte por infarto antes de llegar al hospital es la fibrilación ventricular"
  },
  "HEM-033": {
    titulo: "La causa más frecuente de neutropenia grave (< 500/µL) es la inducida por medicamentos",
    imagen: "flujogramas/neutropenia-menor-500-causa-farmacologica.svg",
    alt: "Flujograma: La causa más frecuente de neutropenia grave (< 500/µL) es la inducida por medicamentos"
  },
  "NEU-050": {
    titulo: "Mujer con EPOC que nunca fumó pero convivió 35 años con un fumador pesado: la causa es el tabaquismo pasivo",
    imagen: "flujogramas/viuda-esposo-fumador-epoc-tabaquismo-pasivo.svg",
    alt: "Flujograma: Mujer con EPOC que nunca fumó pero convivió 35 años con un fumador pesado: la causa es el tabaquismo pasivo"
  },
  "NEU-051": {
    titulo: "La complicación más frecuente de la neumonía nosocomial es la insuficiencia respiratoria",
    imagen: "flujogramas/neumonia-nosocomial-complicacion-insuficiencia-respiratoria.svg",
    alt: "Flujograma: La complicación más frecuente de la neumonía nosocomial es la insuficiencia respiratoria"
  },
  "PED-168": {
    titulo: "Neonato de 7 días con fiebre, fontanela abombada y convulsiones, con bacilos grampositivos en el LCR: meningitis por Listeria monocytogenes",
    imagen: "flujogramas/neonato-meningitis-bacilos-gram-positivos-listeria.svg",
    alt: "Flujograma: Neonato de 7 días con fiebre, fontanela abombada y convulsiones, con bacilos grampositivos en el LCR: meningitis por Listeria monocytogenes"
  },
  "PED-169": {
    titulo: "Lactante de 9 meses con disentería, deshidratación moderada, somnolencia y distensión abdominal: hospitalizar y ceftriaxona EV",
    imagen: "flujogramas/lactante-disenteria-deshidratado-somnoliento-ceftriaxona.svg",
    alt: "Flujograma: Lactante de 9 meses con disentería, deshidratación moderada, somnolencia y distensión abdominal: hospitalizar y ceftriaxona EV"
  },
  "PED-170": {
    titulo: "Recién nacido de 2 días, nacido en casa sin control prenatal, con pobre succión, hipotonía, somnolencia, ictericia hasta la ingle, leucopenia y bilirrubina directa alta: sepsis neonatal",
    imagen: "flujogramas/rn-2-dias-ictericia-bilirrubina-directa-leucopenia-sepsis.svg",
    alt: "Flujograma: Recién nacido de 2 días, nacido en casa sin control prenatal, con pobre succión, hipotonía, somnolencia, ictericia hasta la ingle, leucopenia y bilirrubina directa alta: sepsis neonatal"
  },
  "PED-171": {
    titulo: "Prematuro de 33 semanas con quejido audible, aleteo intenso, tiraje intercostal, retracción xifoidea leve y disociación toracoabdominal: Silverman-Andersen de 8 (dificultad grave)",
    imagen: "flujogramas/prematuro-33-sem-quejido-aleteo-silverman-8.svg",
    alt: "Flujograma: Prematuro de 33 semanas con quejido audible, aleteo intenso, tiraje intercostal, retracción xifoidea leve y disociación toracoabdominal: Silverman-Andersen de 8 (dificultad grave)"
  },
  "SP-126": {
    titulo: "Niño en coma por hematoma epidural que necesita cirugía de emergencia sin familiares presentes: el jefe de guardia autoriza dejando constancia en la historia clínica",
    imagen: "flujogramas/nino-hematoma-epidural-sin-familia-jefe-guardia-autoriza.svg",
    alt: "Flujograma: Niño en coma por hematoma epidural que necesita cirugía de emergencia sin familiares presentes: el jefe de guardia autoriza dejando constancia en la historia clínica"
  },
  "PED-172": {
    titulo: "Niño de 12 meses no vacunado con accesos de tos, estridor inspiratorio en «gallo», sofocación y cianosis: tos ferina (fase paroxística)",
    imagen: "flujogramas/lactante-no-vacunado-tos-paroxistica-gallo-tos-ferina.svg",
    alt: "Flujograma: Niño de 12 meses no vacunado con accesos de tos, estridor inspiratorio en «gallo», sofocación y cianosis: tos ferina (fase paroxística)"
  },
  "PSI-034": {
    titulo: "Adolescente con cambios bruscos del ánimo (impulsividad y depresión): la agresión sexual es el factor que más aumenta el riesgo suicida",
    imagen: "flujogramas/adolescente-bipolar-riesgo-suicida-agresion-sexual.svg",
    alt: "Flujograma: Adolescente con cambios bruscos del ánimo (impulsividad y depresión): la agresión sexual es el factor que más aumenta el riesgo suicida"
  },
  "NEF-072": {
    titulo: "Niño con dolor cólico abdominal intenso de inicio agudo, polaquiuria, tenesmo vesical y hematuria abundante sin fiebre: litiasis urinaria",
    imagen: "flujogramas/nino-colico-hematuria-sin-fiebre-litiasis.svg",
    alt: "Flujograma: Niño con dolor cólico abdominal intenso de inicio agudo, polaquiuria, tenesmo vesical y hematuria abundante sin fiebre: litiasis urinaria"
  },
  "REU-053": {
    titulo: "Niño con prurito del cuero cabelludo y liendres pegadas al pelo, con un hermano igual: pediculosis de la cabeza, permetrina al 1 %",
    imagen: "flujogramas/escolar-liendres-hermano-prurito-permetrina.svg",
    alt: "Flujograma: Niño con prurito del cuero cabelludo y liendres pegadas al pelo, con un hermano igual: pediculosis de la cabeza, permetrina al 1 %"
  },
  "PED-173": {
    titulo: "La faringitis estreptocócica del escolar la causa el estreptococo beta-hemolítico del grupo A (Streptococcus pyogenes)",
    imagen: "flujogramas/escolar-faringitis-estreptococo-grupo-a.svg",
    alt: "Flujograma: La faringitis estreptocócica del escolar la causa el estreptococo beta-hemolítico del grupo A (Streptococcus pyogenes)"
  },
  "PED-174": {
    titulo: "Lactante de 9 meses al que le falta la 3.ª dosis de pentavalente y la 2.ª de rotavirus: solo se aplica la pentavalente, porque la edad del rotavirus ya pasó",
    imagen: "flujogramas/lactante-9-meses-pentavalente-pendiente-rotavirus-fuera-edad.svg",
    alt: "Flujograma: Lactante de 9 meses al que le falta la 3.ª dosis de pentavalente y la 2.ª de rotavirus: solo se aplica la pentavalente, porque la edad del rotavirus ya pasó"
  },
  "HEM-034": {
    titulo: "Niño con palidez, bilirrubina indirecta alta, reticulocitos altos y haptoglobina baja: anemia por hemólisis",
    imagen: "flujogramas/nino-palidez-reticulocitos-altos-haptoglobina-baja-hemolisis.svg",
    alt: "Flujograma: Niño con palidez, bilirrubina indirecta alta, reticulocitos altos y haptoglobina baja: anemia por hemólisis"
  },
  "PED-175": {
    titulo: "Neonato de 6 días con fiebre, irritabilidad, fontanela abombada, leucocitosis y plaquetopenia: sepsis con meningitis neonatal, ampicilina + gentamicina empíricas",
    imagen: "flujogramas/rn-6-dias-fiebre-fontanela-abombada-ampicilina-gentamicina.svg",
    alt: "Flujograma: Neonato de 6 días con fiebre, irritabilidad, fontanela abombada, leucocitosis y plaquetopenia: sepsis con meningitis neonatal, ampicilina + gentamicina empíricas"
  },
  "PED-176": {
    titulo: "Recién nacido con salivación excesiva, tos y ahogo al alimentarse, polihidramnios, sonda que no pasa y sin gas abdominal: atresia de esófago, suspender la vía oral",
    imagen: "flujogramas/rn-salivacion-sonda-no-pasa-sin-gas-atresia-esofago.svg",
    alt: "Flujograma: Recién nacido con salivación excesiva, tos y ahogo al alimentarse, polihidramnios, sonda que no pasa y sin gas abdominal: atresia de esófago, suspender la vía oral"
  },
  "TRA-037": {
    titulo: "Minero con fractura expuesta conminuta de tibia, músculo y hueso expuestos y tierra en la herida: lo prioritario es la irrigación y el desbridamiento",
    imagen: "flujogramas/alud-fractura-conminuta-tibia-expuesta-tierra-desbridamiento.svg",
    alt: "Flujograma: Minero con fractura expuesta conminuta de tibia, músculo y hueso expuestos y tierra en la herida: lo prioritario es la irrigación y el desbridamiento"
  },
  "TRA-038": {
    titulo: "Torcedura de tobillo con edema, equimosis lateral, dolor a la inversión e inestabilidad moderada: esguince de tobillo grado 2",
    imagen: "flujogramas/torcedura-tobillo-equimosis-inestabilidad-esguince-grado-2.svg",
    alt: "Flujograma: Torcedura de tobillo con edema, equimosis lateral, dolor a la inversión e inestabilidad moderada: esguince de tobillo grado 2"
  },
  "CIR-096": {
    titulo: "La quemadura de tercer grado (espesor total) no duele porque destruye las terminaciones nerviosas de la dermis",
    imagen: "flujogramas/quemadura-sin-dolor-tercer-grado.svg",
    alt: "Flujograma: La quemadura de tercer grado (espesor total) no duele porque destruye las terminaciones nerviosas de la dermis"
  },
  "CIR-097": {
    titulo: "Mujer con ictericia, coluria y vía biliar dilatada 2 meses después de una colecistectomía: pedir colangiorresonancia",
    imagen: "flujogramas/poscolecistectomia-ictericia-via-dilatada-colangioresonancia.svg",
    alt: "Flujograma: Mujer con ictericia, coluria y vía biliar dilatada 2 meses después de una colecistectomía: pedir colangiorresonancia"
  },
  "CIR-098": {
    titulo: "Anciano de 87 años con EPOC e insuficiencia cardiaca descompensada, con colecistitis aguda que no mejora tras 4 días: colecistostomía percutánea",
    imagen: "flujogramas/anciano-87-colecistitis-sin-mejoria-colecistostomia-percutanea.svg",
    alt: "Flujograma: Anciano de 87 años con EPOC e insuficiencia cardiaca descompensada, con colecistitis aguda que no mejora tras 4 días: colecistostomía percutánea"
  },
  "GAS-061": {
    titulo: "Anciana con ictericia, prurito, baja de peso y vesícula grande palpable sin cálculos: sospecha de tumor periampular, pedir TC de abdomen",
    imagen: "flujogramas/anciana-ictericia-vesicula-palpable-sin-calculos-tomografia.svg",
    alt: "Flujograma: Anciana con ictericia, prurito, baja de peso y vesícula grande palpable sin cálculos: sospecha de tumor periampular, pedir TC de abdomen"
  },
  "OFT-039": {
    titulo: "Adolescente que nada en piscina con otalgia, secreción, dolor al traccionar el pabellón y conducto edematoso: otitis externa aguda por Pseudomonas aeruginosa",
    imagen: "flujogramas/nadador-otalgia-traccion-pabellon-pseudomonas.svg",
    alt: "Flujograma: Adolescente que nada en piscina con otalgia, secreción, dolor al traccionar el pabellón y conducto edematoso: otitis externa aguda por Pseudomonas aeruginosa"
  },
  "GIN-164": {
    titulo: "Gestante de 34 semanas con contracciones esporádicas y cuello sin cambios (0 cm, 0 % borramiento): no es trabajo de parto, reposo y observación por unas horas",
    imagen: "flujogramas/34-semanas-contracciones-sin-cambios-cervicales-observar.svg",
    alt: "Flujograma: Gestante de 34 semanas con contracciones esporádicas y cuello sin cambios (0 cm, 0 % borramiento): no es trabajo de parto, reposo y observación por unas horas"
  },
  "GIN-165": {
    titulo: "Puérpera en choque hipovolémico por hemorragia que recibe líquidos: el mejor signo de reposición exitosa es la recuperación de la diuresis",
    imagen: "flujogramas/hemorragia-posparto-choque-reposicion-diuresis.svg",
    alt: "Flujograma: Puérpera en choque hipovolémico por hemorragia que recibe líquidos: el mejor signo de reposición exitosa es la recuperación de la diuresis"
  },
  "GIN-166": {
    titulo: "Gestante con glucosa en ayunas de 130 y 128 mg/dL: ya tiene el diagnóstico (diabetes franca en el embarazo), no requiere otra prueba",
    imagen: "flujogramas/gestante-glucosa-ayunas-130-y-128-diabetes-confirmada.svg",
    alt: "Flujograma: Gestante con glucosa en ayunas de 130 y 128 mg/dL: ya tiene el diagnóstico (diabetes franca en el embarazo), no requiere otra prueba"
  },
  "GIN-167": {
    titulo: "Gestante con dos abortos y un hijo macrosómico: en el próximo control hay que descartar diabetes mellitus",
    imagen: "flujogramas/abortos-previos-macrosomico-descartar-diabetes.svg",
    alt: "Flujograma: Gestante con dos abortos y un hijo macrosómico: en el próximo control hay que descartar diabetes mellitus"
  },
  "GIN-168": {
    titulo: "Desaceleraciones variables de la frecuencia cardiaca fetal, sin relación con las contracciones: compresión del cordón umbilical",
    imagen: "flujogramas/desaceleraciones-variables-compresion-cordon.svg",
    alt: "Flujograma: Desaceleraciones variables de la frecuencia cardiaca fetal, sin relación con las contracciones: compresión del cordón umbilical"
  },
  "GIN-169": {
    titulo: "Para estimular un trabajo de parto con dinámica inadecuada se diluyen 10 UI de oxitocina en 1 litro de solución salina (10 mUI/mL)",
    imagen: "flujogramas/estimular-parto-10-ui-oxitocina-litro.svg",
    alt: "Flujograma: Para estimular un trabajo de parto con dinámica inadecuada se diluyen 10 UI de oxitocina en 1 litro de solución salina (10 mUI/mL)"
  },
  "GIN-170": {
    titulo: "Gestante de 32 semanas con feto bajo el percentil 10, líquido amniótico y Doppler umbilical normales: feto pequeño para la edad, control en dos semanas",
    imagen: "flujogramas/32-semanas-peso-p10-doppler-normal-control-2-semanas.svg",
    alt: "Flujograma: Gestante de 32 semanas con feto bajo el percentil 10, líquido amniótico y Doppler umbilical normales: feto pequeño para la edad, control en dos semanas"
  },
  "GIN-171": {
    titulo: "Gestante «de 42 semanas» que no recuerda bien su FUR: la edad gestacional se confirma con la ecografía del primer trimestre",
    imagen: "flujogramas/42-semanas-fur-incierta-ecografia-primer-trimestre.svg",
    alt: "Flujograma: Gestante «de 42 semanas» que no recuerda bien su FUR: la edad gestacional se confirma con la ecografía del primer trimestre"
  },
  "GIN-172": {
    titulo: "En el primer control a las 8 semanas, si solo se pueden pedir tres exámenes, el que se descarta es la tolerancia a la glucosa (se hace a las 24-28 semanas)",
    imagen: "flujogramas/primer-control-8-semanas-no-tolerancia-glucosa.svg",
    alt: "Flujograma: En el primer control a las 8 semanas, si solo se pueden pedir tres exámenes, el que se descarta es la tolerancia a la glucosa (se hace a las 24-28 semanas)"
  },
  "GIN-173": {
    titulo: "Diez minutos después del parto la placenta no se ha desprendido: al presionar sobre el pubis el cordón sube (signo de Küstner positivo)",
    imagen: "flujogramas/alumbramiento-retrasado-kustner-cordon-asciende.svg",
    alt: "Flujograma: Diez minutos después del parto la placenta no se ha desprendido: al presionar sobre el pubis el cordón sube (signo de Küstner positivo)"
  },
  "GIN-174": {
    titulo: "En un embarazo gemelar dicigótico (bicorial) la complicación menos esperable es la transfusión feto-fetal, propia de los monocoriales",
    imagen: "flujogramas/gemelos-dicigoticos-no-transfusion-feto-fetal.svg",
    alt: "Flujograma: En un embarazo gemelar dicigótico (bicorial) la complicación menos esperable es la transfusión feto-fetal, propia de los monocoriales"
  },
  "GIN-175": {
    titulo: "Gestante de 10 semanas con útero acorde y sin dolor ni masas: la beta-hCG no es necesaria, el embarazo ya está confirmado",
    imagen: "flujogramas/gestante-10-semanas-confirmada-beta-hcg-innecesaria.svg",
    alt: "Flujograma: Gestante de 10 semanas con útero acorde y sin dolor ni masas: la beta-hCG no es necesaria, el embarazo ya está confirmado"
  },
  "GIN-176": {
    titulo: "Gestante de 31 semanas con pérdida de líquido claro y cuello sin cambios: rotura prematura de membranas pretérmino, hospitalizar con corticoides y antibióticos",
    imagen: "flujogramas/31-semanas-perdida-liquido-claro-rpm-corticoides-antibioticos.svg",
    alt: "Flujograma: Gestante de 31 semanas con pérdida de líquido claro y cuello sin cambios: rotura prematura de membranas pretérmino, hospitalizar con corticoides y antibióticos"
  },
  "GIN-177": {
    titulo: "Mujer joven con 7 semanas de amenorrea secundaria: lo primero es descartar embarazo con beta-hCG y ecografía transvaginal",
    imagen: "flujogramas/amenorrea-7-semanas-beta-hcg-ecografia.svg",
    alt: "Flujograma: Mujer joven con 7 semanas de amenorrea secundaria: lo primero es descartar embarazo con beta-hCG y ecografía transvaginal"
  },
  "GIN-178": {
    titulo: "Mujer de 52 años con polaquiuria y bulto vaginal por prolapso del compartimento anterior (cistocele): colporrafia anterior",
    imagen: "flujogramas/bulto-vaginal-polaquiuria-cistocele-colporrafia-anterior.svg",
    alt: "Flujograma: Mujer de 52 años con polaquiuria y bulto vaginal por prolapso del compartimento anterior (cistocele): colporrafia anterior"
  },
  "INF-086": {
    titulo: "El tratamiento inicial de la meningitis tuberculosa es isoniazida, rifampicina, pirazinamida y etambutol (fase intensiva), con corticoide",
    imagen: "flujogramas/meningitis-tuberculosa-esquema-hrze.svg",
    alt: "Flujograma: El tratamiento inicial de la meningitis tuberculosa es isoniazida, rifampicina, pirazinamida y etambutol (fase intensiva), con corticoide"
  },
  "PSI-035": {
    titulo: "La dislexia es un trastorno del neurodesarrollo que afecta el aprendizaje de la lectura",
    imagen: "flujogramas/dislexia-dificultad-para-leer.svg",
    alt: "Flujograma: La dislexia es un trastorno del neurodesarrollo que afecta el aprendizaje de la lectura"
  },
  "NEU-052": {
    titulo: "La muerte por embolia pulmonar masiva se debe a la falla aguda del ventrículo derecho con choque (cardiogénico/obstructivo)",
    imagen: "flujogramas/tep-masivo-muerte-falla-ventricular-derecha.svg",
    alt: "Flujograma: La muerte por embolia pulmonar masiva se debe a la falla aguda del ventrículo derecho con choque (cardiogénico/obstructivo)"
  },
  "SP-127": {
    titulo: "Si la glucemia tiene media 95 y mediana 90, la mitad de los sujetos tiene valores menores de 90 mg/dL (distribución con cola a la derecha)",
    imagen: "flujogramas/glicemia-media-95-mediana-90-mitad-debajo.svg",
    alt: "Flujograma: Si la glucemia tiene media 95 y mediana 90, la mitad de los sujetos tiene valores menores de 90 mg/dL (distribución con cola a la derecha)"
  },
  "SP-128": {
    titulo: "Tasa específica de mortalidad por COVID = 300 muertes ÷ 20 000 habitantes × 1000 = 15 por mil",
    imagen: "flujogramas/300-muertes-covid-20000-habitantes-tasa-especifica-15.svg",
    alt: "Flujograma: Tasa específica de mortalidad por COVID = 300 muertes ÷ 20 000 habitantes × 1000 = 15 por mil"
  },
  "SP-129": {
    titulo: "Número de hombres dividido entre número de mujeres es una razón (el numerador no está incluido en el denominador)",
    imagen: "flujogramas/hombres-entre-mujeres-razon.svg",
    alt: "Flujograma: Número de hombres dividido entre número de mujeres es una razón (el numerador no está incluido en el denominador)"
  },
  "CB-062": {
    titulo: "En el hilio derecho el bronquio está detrás de la arteria pulmonar y en el izquierdo está debajo de ella",
    imagen: "flujogramas/hilio-pulmonar-bronquio-detras-derecho-debajo-izquierdo.svg",
    alt: "Flujograma: En el hilio derecho el bronquio está detrás de la arteria pulmonar y en el izquierdo está debajo de ella"
  },
  "CB-063": {
    titulo: "La língula es parte del lóbulo superior del pulmón izquierdo (equivale al lóbulo medio derecho)",
    imagen: "flujogramas/tumor-lingula-pulmon-izquierdo.svg",
    alt: "Flujograma: La língula es parte del lóbulo superior del pulmón izquierdo (equivale al lóbulo medio derecho)"
  },
  "CB-064": {
    titulo: "El aumento de la PaCO₂ estimula la respiración sobre todo a través de los quimiorreceptores centrales del bulbo raquídeo",
    imagen: "flujogramas/co2-estimula-respiracion-quimiorreceptores-bulbo.svg",
    alt: "Flujograma: El aumento de la PaCO₂ estimula la respiración sobre todo a través de los quimiorreceptores centrales del bulbo raquídeo"
  },
  "CB-065": {
    titulo: "El aire inspirado que no participa en la hematosis es el espacio muerto (vías de conducción y alvéolos sin sangre)",
    imagen: "flujogramas/aire-que-no-participa-hematosis-espacio-muerto.svg",
    alt: "Flujograma: El aire inspirado que no participa en la hematosis es el espacio muerto (vías de conducción y alvéolos sin sangre)"
  },
  "CB-066": {
    titulo: "La capacidad vital es el volumen corriente más el volumen de reserva inspiratoria y el de reserva espiratoria (no incluye el volumen residual)",
    imagen: "flujogramas/capacidad-vital-volumen-corriente-reservas.svg",
    alt: "Flujograma: La capacidad vital es el volumen corriente más el volumen de reserva inspiratoria y el de reserva espiratoria (no incluye el volumen residual)"
  },
  "CB-067": {
    titulo: "El oxígeno difunde unas 20 veces menos que el CO₂ porque es mucho menos soluble en agua",
    imagen: "flujogramas/difusion-oxigeno-menor-que-co2-solubilidad.svg",
    alt: "Flujograma: El oxígeno difunde unas 20 veces menos que el CO₂ porque es mucho menos soluble en agua"
  },
  "INF-087": {
    titulo: "El Quantiferon (IGRA) detecta infección tuberculosa sin dar falsos positivos por la vacuna BCG",
    imagen: "flujogramas/quantiferon-infeccion-tb-sin-interferencia-bcg.svg",
    alt: "Flujograma: El Quantiferon (IGRA) detecta infección tuberculosa sin dar falsos positivos por la vacuna BCG"
  },
  "SP-130": {
    titulo: "Paciente con COVID-19 que sale a trabajar sin avisar invocando su autonomía: predomina el principio de no maleficencia (no dañar a terceros)",
    imagen: "flujogramas/covid-sale-a-trabajar-autonomia-no-maleficencia.svg",
    alt: "Flujograma: Paciente con COVID-19 que sale a trabajar sin avisar invocando su autonomía: predomina el principio de no maleficencia (no dañar a terceros)"
  },
  "INF-088": {
    titulo: "Elevar la cabecera de la cama 30-45° reduce la neumonía asociada al ventilador (evita la aspiración)",
    imagen: "flujogramas/ventilador-cabecera-45-grados-previene-neumonia.svg",
    alt: "Flujograma: Elevar la cabecera de la cama 30-45° reduce la neumonía asociada al ventilador (evita la aspiración)"
  },
  "SP-131": {
    titulo: "Aumento de febriles con Aedes aegypti en el territorio: los equipos extramurales priorizan el control de fuentes de infección (criaderos) y contactos",
    imagen: "flujogramas/febriles-aedes-aegypti-control-focos-extramural.svg",
    alt: "Flujograma: Aumento de febriles con Aedes aegypti en el territorio: los equipos extramurales priorizan el control de fuentes de infección (criaderos) y contactos"
  },
  "NEF-073": {
    titulo: "Varón con disminución del tamaño testicular un año después de una cirugía pélvica: atrofia por ligadura de la arteria testicular",
    imagen: "flujogramas/cirugia-pelvica-atrofia-testicular-arteria-testicular.svg",
    alt: "Flujograma: Varón con disminución del tamaño testicular un año después de una cirugía pélvica: atrofia por ligadura de la arteria testicular"
  },
  "GIN-179": {
    titulo: "Gestante de 12 semanas con preeclampsia severa previa, lupus y sobrepeso: alto riesgo de preeclampsia, la profilaxis más efectiva es aspirina a dosis bajas",
    imagen: "flujogramas/preeclampsia-previa-lupus-aspirina-dosis-baja.svg",
    alt: "Flujograma: Gestante de 12 semanas con preeclampsia severa previa, lupus y sobrepeso: alto riesgo de preeclampsia, la profilaxis más efectiva es aspirina a dosis bajas"
  },
  "TRA-039": {
    titulo: "Luxación posterior de cadera reducida a las 72 horas: la complicación ósea a mediano y largo plazo es la necrosis avascular de la cabeza femoral",
    imagen: "flujogramas/luxacion-posterior-cadera-reducida-72-h-necrosis-avascular.svg",
    alt: "Flujograma: Luxación posterior de cadera reducida a las 72 horas: la complicación ósea a mediano y largo plazo es la necrosis avascular de la cabeza femoral"
  },
  "SP-132": {
    titulo: "Paciente con muerte encefálica establecida al que se le retira el soporte ventilatorio: no se vulnera ningún principio ético (ya está fallecido)",
    imagen: "flujogramas/muerte-encefalica-retirar-soporte-ningun-valor-vulnerado.svg",
    alt: "Flujograma: Paciente con muerte encefálica establecida al que se le retira el soporte ventilatorio: no se vulnera ningún principio ético (ya está fallecido)"
  },
  "GIN-180": {
    titulo: "Primigesta de 32 semanas con contracciones cada 4 minutos, 1 cm de dilatación y membranas íntegras: amenaza de parto pretérmino, maduración pulmonar y tocólisis",
    imagen: "flujogramas/32-semanas-contracciones-regulares-1-cm-maduracion-tocolisis.svg",
    alt: "Flujograma: Primigesta de 32 semanas con contracciones cada 4 minutos, 1 cm de dilatación y membranas íntegras: amenaza de parto pretérmino, maduración pulmonar y tocólisis"
  },
  "GIN-181": {
    titulo: "Usuaria de DIU con prueba de embarazo positiva y hilos visibles: retirar el dispositivo",
    imagen: "flujogramas/usuaria-diu-test-positivo-hilos-visibles-retirar.svg",
    alt: "Flujograma: Usuaria de DIU con prueba de embarazo positiva y hilos visibles: retirar el dispositivo"
  },
  "REU-054": {
    titulo: "Placas eritematodescamativas en los codos, artritis con erosiones de interfalángicas distales y factor reumatoide negativo: artritis psoriásica",
    imagen: "flujogramas/placas-codos-artritis-interfalangicas-distales-psoriasica.svg",
    alt: "Flujograma: Placas eritematodescamativas en los codos, artritis con erosiones de interfalángicas distales y factor reumatoide negativo: artritis psoriásica"
  },
  "PSI-036": {
    titulo: "Mujer con tristeza persistente, desesperanza, ideas suicidas y alucinaciones auditivas y visuales: depresión mayor con síntomas psicóticos",
    imagen: "flujogramas/tristeza-ideas-suicidas-alucinaciones-depresion-psicotica.svg",
    alt: "Flujograma: Mujer con tristeza persistente, desesperanza, ideas suicidas y alucinaciones auditivas y visuales: depresión mayor con síntomas psicóticos"
  },
  "END-051": {
    titulo: "En la cetoacidosis diabética el riñón compensa reabsorbiendo todo el bicarbonato (disminuye su excreción) y eliminando más ácido como amonio",
    imagen: "flujogramas/cetoacidosis-kussmaul-compensacion-renal-bicarbonato.svg",
    alt: "Flujograma: En la cetoacidosis diabética el riñón compensa reabsorbiendo todo el bicarbonato (disminuye su excreción) y eliminando más ácido como amonio"
  },
  "PED-177": {
    titulo: "Niño de 2 años con 24 horas de cólicos, vómitos, masa abdominal, obstrucción intestinal y líquido libre: invaginación complicada, laparotomía exploratoria",
    imagen: "flujogramas/nino-2-anos-invaginacion-liquido-libre-laparotomia.svg",
    alt: "Flujograma: Niño de 2 años con 24 horas de cólicos, vómitos, masa abdominal, obstrucción intestinal y líquido libre: invaginación complicada, laparotomía exploratoria"
  },
  "PED-178": {
    titulo: "Niño de 2 años con ceguera nocturna, fotofobia, xerosis conjuntival y manchas de Bitot: déficit de vitamina A (xeroftalmía)",
    imagen: "flujogramas/nino-ceguera-nocturna-manchas-bitot-vitamina-a.svg",
    alt: "Flujograma: Niño de 2 años con ceguera nocturna, fotofobia, xerosis conjuntival y manchas de Bitot: déficit de vitamina A (xeroftalmía)"
  },
  "NRL-047": {
    titulo: "Mujer con ACV isquémico agudo (afasia y hemiparesia) y PA 208/108: lo primero es bajar la PA a < 185/110 para poder trombolizar",
    imagen: "flujogramas/acv-pa-208-bajar-menos-185-antes-trombolisis.svg",
    alt: "Flujograma: Mujer con ACV isquémico agudo (afasia y hemiparesia) y PA 208/108: lo primero es bajar la PA a < 185/110 para poder trombolizar"
  },
  "CAR-062": {
    titulo: "Paciente que deja de respirar, no responde y no tiene pulso: lo primero es iniciar compresiones torácicas",
    imagen: "flujogramas/deja-de-respirar-sin-pulso-compresiones-toracicas.svg",
    alt: "Flujograma: Paciente que deja de respirar, no responde y no tiene pulso: lo primero es iniciar compresiones torácicas"
  },
  "SP-133": {
    titulo: "Para que toda la población use mascarilla, se lave las manos y guarde distancia al inicio de la pandemia, la intervención clave fueron los medios masivos de comunicación",
    imagen: "flujogramas/covid-mascarilla-lavado-manos-medios-masivos.svg",
    alt: "Flujograma: Para que toda la población use mascarilla, se lave las manos y guarde distancia al inicio de la pandemia, la intervención clave fueron los medios masivos de comunicación"
  },
  "NEF-074": {
    titulo: "Anciano con hidroclorotiazida, debilidad muscular, caídas e hiporreflexia: sospecha de hipopotasemia, lo inicial es el electrocardiograma",
    imagen: "flujogramas/tiazida-debilidad-hiporreflexia-hipokalemia-ecg.svg",
    alt: "Flujograma: Anciano con hidroclorotiazida, debilidad muscular, caídas e hiporreflexia: sospecha de hipopotasemia, lo inicial es el electrocardiograma"
  },
  "TRA-040": {
    titulo: "Lactante de 11 meses, nacida en podálica, con pliegues glúteos asimétricos y signo de Galeazzi positivo: displasia del desarrollo de la cadera",
    imagen: "flujogramas/lactante-podalica-pliegues-asimetricos-galeazzi-ddc.svg",
    alt: "Flujograma: Lactante de 11 meses, nacida en podálica, con pliegues glúteos asimétricos y signo de Galeazzi positivo: displasia del desarrollo de la cadera"
  },
  "END-052": {
    titulo: "Diabética con dolor y parestesias en las piernas y pérdida de sensibilidad: neuropatía diabética dolorosa, tratar con gabapentinoides (gabapentina o pregabalina)",
    imagen: "flujogramas/diabetica-parestesias-dolor-mmii-gabapentina.svg",
    alt: "Flujograma: Diabética con dolor y parestesias en las piernas y pérdida de sensibilidad: neuropatía diabética dolorosa, tratar con gabapentinoides (gabapentina o pregabalina)"
  },
  "GIN-182": {
    titulo: "Gestante de 28 semanas con contracciones regulares, 4 cm de dilatación y 80 % de borramiento: trabajo de parto pretérmino establecido",
    imagen: "flujogramas/28-semanas-dilatacion-4-cm-borramiento-80-parto-pretermino.svg",
    alt: "Flujograma: Gestante de 28 semanas con contracciones regulares, 4 cm de dilatación y 80 % de borramiento: trabajo de parto pretérmino establecido"
  },
  "GAS-062": {
    titulo: "Varón con saciedad precoz, baja de peso, anemia microcítica, ascitis y ganglio supraclavicular izquierdo pétreo (Virchow): cáncer gástrico avanzado, endoscopia con biopsia",
    imagen: "flujogramas/saciedad-precoz-ganglio-virchow-ascitis-endoscopia.svg",
    alt: "Flujograma: Varón con saciedad precoz, baja de peso, anemia microcítica, ascitis y ganglio supraclavicular izquierdo pétreo (Virchow): cáncer gástrico avanzado, endoscopia con biopsia"
  },
  "TRA-041": {
    titulo: "Adolescente con fiebre, monoartritis aguda de rodilla y leucocitosis con desviación izquierda: artritis séptica, el germen más probable es Staphylococcus aureus",
    imagen: "flujogramas/adolescente-rodilla-fiebre-leucocitosis-artritis-septica-aureus.svg",
    alt: "Flujograma: Adolescente con fiebre, monoartritis aguda de rodilla y leucocitosis con desviación izquierda: artritis séptica, el germen más probable es Staphylococcus aureus"
  },
  "GIN-183": {
    titulo: "Gestante de 33 semanas con cesárea previa, sangrado indoloro y presentación flotante: sospecha de placenta previa, se debe evitar el tacto vaginal",
    imagen: "flujogramas/33-semanas-sangrado-sin-dolor-presentacion-flotante-no-tacto.svg",
    alt: "Flujograma: Gestante de 33 semanas con cesárea previa, sangrado indoloro y presentación flotante: sospecha de placenta previa, se debe evitar el tacto vaginal"
  },
  "OFT-040": {
    titulo: "Anciano con epistaxis severa que sangra por la fosa nasal y por la boca: epistaxis posterior, taponamiento posterior",
    imagen: "flujogramas/anciano-epistaxis-fosa-y-boca-taponamiento-posterior.svg",
    alt: "Flujograma: Anciano con epistaxis severa que sangra por la fosa nasal y por la boca: epistaxis posterior, taponamiento posterior"
  },
  "CB-068": {
    titulo: "Infertilidad masculina por falla en la maduración de los espermatozoides: el problema está en el epidídimo (cuerpo)",
    imagen: "flujogramas/infertilidad-maduracion-espermatica-epididimo.svg",
    alt: "Flujograma: Infertilidad masculina por falla en la maduración de los espermatozoides: el problema está en el epidídimo (cuerpo)"
  },
  "GIN-184": {
    titulo: "Multípara a término en fase activa avanzada (7 cm, −1) con placenta de inserción baja y sangrado escaso: vía EV, amniotomía y esperar el parto vaginal",
    imagen: "flujogramas/placenta-baja-sangrado-escaso-7-cm-amniotomia-parto-vaginal.svg",
    alt: "Flujograma: Multípara a término en fase activa avanzada (7 cm, −1) con placenta de inserción baja y sangrado escaso: vía EV, amniotomía y esperar el parto vaginal"
  },
  "PED-179": {
    titulo: "Escolar con fiebre, vómitos, coluria, ictericia y transaminasas altas con tiempo de protrombina normal: hepatitis A aguda, hidratación y sintomáticos",
    imagen: "flujogramas/escolar-ictericia-transaminasas-altas-hepatitis-a-sintomaticos.svg",
    alt: "Flujograma: Escolar con fiebre, vómitos, coluria, ictericia y transaminasas altas con tiempo de protrombina normal: hepatitis A aguda, hidratación y sintomáticos"
  },
  "SP-134": {
    titulo: "En un estudio sobre cuarentena y estado nutricional de estudiantes, el marco conceptual debe incluir prioritariamente los criterios de estilos de vida saludable en adultos jóvenes",
    imagen: "flujogramas/cuarentena-estado-nutricional-marco-conceptual-estilos-vida.svg",
    alt: "Flujograma: En un estudio sobre cuarentena y estado nutricional de estudiantes, el marco conceptual debe incluir prioritariamente los criterios de estilos de vida saludable en adultos jóvenes"
  },
  "PED-180": {
    titulo: "Lactante de 1 año con una crisis tónica generalizada de pocos minutos con fiebre, despierto y sin signos meníngeos ni focales: convulsión febril simple, bajar la temperatura",
    imagen: "flujogramas/lactante-rigidez-fiebre-38-convulsion-febril-simple.svg",
    alt: "Flujograma: Lactante de 1 año con una crisis tónica generalizada de pocos minutos con fiebre, despierto y sin signos meníngeos ni focales: convulsión febril simple, bajar la temperatura"
  },
  "INF-089": {
    titulo: "Agricultor con fiebre, cefalea, artralgias y mialgias en pantorrillas tras exposición a canales de regadío: caso sospechoso de leptospirosis",
    imagen: "flujogramas/agricultor-fiebre-mialgia-pantorrillas-canales-leptospirosis-sospechoso.svg",
    alt: "Flujograma: Agricultor con fiebre, cefalea, artralgias y mialgias en pantorrillas tras exposición a canales de regadío: caso sospechoso de leptospirosis"
  },
  "HEM-035": {
    titulo: "Residente de Cerro de Pasco con cefalea, mareos, acúfenos, cianosis, Hb 22, Hto 66 % y SatO₂ 88 %: mal de montaña crónico (enfermedad de Monge)",
    imagen: "flujogramas/cerro-de-pasco-hb-22-cianosis-mal-de-montana-cronico.svg",
    alt: "Flujograma: Residente de Cerro de Pasco con cefalea, mareos, acúfenos, cianosis, Hb 22, Hto 66 % y SatO₂ 88 %: mal de montaña crónico (enfermedad de Monge)"
  },
  "INF-090": {
    titulo: "Varón joven con secreción uretral mucopurulenta y disuria tras sexo sin protección: uretritis, tratamiento empírico con ceftriaxona + azitromicina (cubre gonococo y clamidia)",
    imagen: "flujogramas/uretritis-mucopurulenta-contacto-casual-ceftriaxona-azitromicina.svg",
    alt: "Flujograma: Varón joven con secreción uretral mucopurulenta y disuria tras sexo sin protección: uretritis, tratamiento empírico con ceftriaxona + azitromicina (cubre gonococo y clamidia)"
  },
  "CB-069": {
    titulo: "Paciente con metronidazol que bebe alcohol y presenta náuseas, vómitos, palpitaciones, disnea y agitación: reacción tipo disulfiram (efecto antabús)",
    imagen: "flujogramas/metronidazol-alcohol-palpitaciones-efecto-antabus.svg",
    alt: "Flujograma: Paciente con metronidazol que bebe alcohol y presenta náuseas, vómitos, palpitaciones, disnea y agitación: reacción tipo disulfiram (efecto antabús)"
  },
  "PED-181": {
    titulo: "Neonato de 14 días sano, sin fiebre, con cordón limpio que aún no cae: retraso de la caída del cordón sin patología asociada",
    imagen: "flujogramas/neonato-14-dias-cordon-sin-signos-retraso-sin-patologia.svg",
    alt: "Flujograma: Neonato de 14 días sano, sin fiebre, con cordón limpio que aún no cae: retraso de la caída del cordón sin patología asociada"
  },
  "REU-055": {
    titulo: "Artritis de rodilla con cocos grampositivos en racimos en el líquido sinovial: artritis séptica por S. aureus, drenaje articular y antibióticos parenterales",
    imagen: "flujogramas/gram-cocos-racimos-liquido-sinovial-drenaje-antibioticos.svg",
    alt: "Flujograma: Artritis de rodilla con cocos grampositivos en racimos en el líquido sinovial: artritis séptica por S. aureus, drenaje articular y antibióticos parenterales"
  },
  "NRL-048": {
    titulo: "Mujer joven con más de 4 crisis de migraña al mes: necesita profilaxis, y el propranolol es de primera línea",
    imagen: "flujogramas/migrana-mas-4-episodios-mes-profilaxis-propranolol.svg",
    alt: "Flujograma: Mujer joven con más de 4 crisis de migraña al mes: necesita profilaxis, y el propranolol es de primera línea"
  },
  "CB-070": {
    titulo: "Preescolar muy pobre y desnutrido con fatiga, anorexia, diarrea, calambres, edema y reflejos disminuidos: déficit de tiamina (beriberi)",
    imagen: "flujogramas/preescolar-pobreza-edema-hiporreflexia-tiamina.svg",
    alt: "Flujograma: Preescolar muy pobre y desnutrido con fatiga, anorexia, diarrea, calambres, edema y reflejos disminuidos: déficit de tiamina (beriberi)"
  },
  "END-053": {
    titulo: "Obeso con IMC 38 que usa orlistat y recupera peso: lo que se debe añadir es actividad física (ejercicio aeróbico) dentro de un cambio de estilo de vida",
    imagen: "flujogramas/obeso-imc-38-orlistat-agregar-ejercicio-aerobico.svg",
    alt: "Flujograma: Obeso con IMC 38 que usa orlistat y recupera peso: lo que se debe añadir es actividad física (ejercicio aeróbico) dentro de un cambio de estilo de vida"
  },
  "OFT-041": {
    titulo: "Niño con un insecto vivo moviéndose en el conducto auditivo: primero inmovilizarlo instilando aceite mineral, luego extraerlo",
    imagen: "flujogramas/nino-insecto-vivo-oido-aceite-mineral.svg",
    alt: "Flujograma: Niño con un insecto vivo moviéndose en el conducto auditivo: primero inmovilizarlo instilando aceite mineral, luego extraerlo"
  },
  "GAS-063": {
    titulo: "Mujer joven con un año de dolor cólico que cede con la defecación, distensión y alternancia de diarrea y estreñimiento, con examen normal: síndrome de intestino irritable",
    imagen: "flujogramas/dolor-colico-cede-defecar-diarrea-estrenimiento-intestino-irritable.svg",
    alt: "Flujograma: Mujer joven con un año de dolor cólico que cede con la defecación, distensión y alternancia de diarrea y estreñimiento, con examen normal: síndrome de intestino irritable"
  },
  "SP-135": {
    titulo: "Colegio con 80 % de alumnos con sobrepeso u obesidad: la intervención inmediata prioritaria es la comunicación educativa grupal",
    imagen: "flujogramas/colegio-80-sobrepeso-comunicacion-educativa-grupal.svg",
    alt: "Flujograma: Colegio con 80 % de alumnos con sobrepeso u obesidad: la intervención inmediata prioritaria es la comunicación educativa grupal"
  },
  "GIN-185": {
    titulo: "Mujer de 25 años asintomática con quiste ovárico unilocular de 4 cm sin tabiques ni excrecencias: quiste simple, observación",
    imagen: "flujogramas/quiste-ovarico-simple-4-cm-observacion.svg",
    alt: "Flujograma: Mujer de 25 años asintomática con quiste ovárico unilocular de 4 cm sin tabiques ni excrecencias: quiste simple, observación"
  },
  "OFT-042": {
    titulo: "Cuerpo extraño metálico que atraviesa córnea, iris y cristalino (globo abierto): analgesia endovenosa sin manipular el ojo y derivar",
    imagen: "flujogramas/amoladora-cuerpo-extrano-penetrante-analgesia-ev.svg",
    alt: "Flujograma: Cuerpo extraño metálico que atraviesa córnea, iris y cristalino (globo abierto): analgesia endovenosa sin manipular el ojo y derivar"
  },
  "CIR-099": {
    titulo: "Fracturas de las costillas 9 y 10 izquierdas con líquido libre en el FAST: el órgano probablemente lesionado es el bazo",
    imagen: "flujogramas/fracturas-costales-9-10-izquierdas-liquido-libre-bazo.svg",
    alt: "Flujograma: Fracturas de las costillas 9 y 10 izquierdas con líquido libre en el FAST: el órgano probablemente lesionado es el bazo"
  },
  "CB-071": {
    titulo: "Al amamantar, la succión del pezón aumenta la secreción de oxitocina (reflejo de eyección de la leche)",
    imagen: "flujogramas/lactancia-succion-aumenta-oxitocina.svg",
    alt: "Flujograma: Al amamantar, la succión del pezón aumenta la secreción de oxitocina (reflejo de eyección de la leche)"
  },
  "GIN-186": {
    titulo: "Gestante con VIH en TARGA y carga viral de 1500 copias/mL al término: la conducta más riesgosa para el recién nacido es el parto vaginal",
    imagen: "flujogramas/vih-carga-viral-1500-37-semanas-evitar-parto-vaginal.svg",
    alt: "Flujograma: Gestante con VIH en TARGA y carga viral de 1500 copias/mL al término: la conducta más riesgosa para el recién nacido es el parto vaginal"
  },
  "CIR-100": {
    titulo: "Mujer sin enfermedad vascular previa con dolor súbito, frialdad, sin pulsos poplíteo ni pedio, con pérdida de sensibilidad y de movimiento: embolia arterial aguda",
    imagen: "flujogramas/pie-frio-sin-pulsos-paralisis-embolia-arterial.svg",
    alt: "Flujograma: Mujer sin enfermedad vascular previa con dolor súbito, frialdad, sin pulsos poplíteo ni pedio, con pérdida de sensibilidad y de movimiento: embolia arterial aguda"
  },
  "NEF-075": {
    titulo: "Mujer con 5 meses de molestias urinarias, piuria marcada, orina ácida y urocultivo negativo (piuria estéril): sospechar tuberculosis urogenital",
    imagen: "flujogramas/piuria-esteril-urocultivo-negativo-tuberculosis-urogenital.svg",
    alt: "Flujograma: Mujer con 5 meses de molestias urinarias, piuria marcada, orina ácida y urocultivo negativo (piuria estéril): sospechar tuberculosis urogenital"
  },
  "TRA-042": {
    titulo: "Caída sobre la mano extendida con dolor en la tabaquera anatómica: fractura de escafoides",
    imagen: "flujogramas/caida-mano-extendida-dolor-tabaquera-escafoides.svg",
    alt: "Flujograma: Caída sobre la mano extendida con dolor en la tabaquera anatómica: fractura de escafoides"
  },
  "PED-182": {
    titulo: "Lactante de 6 meses con diarrea acuosa abundante y vómitos de inicio brusco, sin fiebre ni sangre, y deshidratación: gastroenteritis por rotavirus",
    imagen: "flujogramas/lactante-6-meses-diarrea-vomitos-deshidratacion-rotavirus.svg",
    alt: "Flujograma: Lactante de 6 meses con diarrea acuosa abundante y vómitos de inicio brusco, sin fiebre ni sangre, y deshidratación: gastroenteritis por rotavirus"
  },
  "GAS-064": {
    titulo: "Alcohólico de 60 años con pancreatitis aguda: de los criterios de Ranson al ingreso solo cumple la edad (> 55 años)",
    imagen: "flujogramas/pancreatitis-alcoholica-60-anos-ranson-edad.svg",
    alt: "Flujograma: Alcohólico de 60 años con pancreatitis aguda: de los criterios de Ranson al ingreso solo cumple la edad (> 55 años)"
  },
  "SP-136": {
    titulo: "Familiares piden ligar las trompas de una mujer con alteración mental severa: se requiere evaluación psiquiátrica y autorización judicial",
    imagen: "flujogramas/incapacidad-mental-ligadura-evaluacion-psiquiatrica-judicial.svg",
    alt: "Flujograma: Familiares piden ligar las trompas de una mujer con alteración mental severa: se requiere evaluación psiquiátrica y autorización judicial"
  },
  "CIR-101": {
    titulo: "Niño con dolor abdominal, palidez y náuseas 3 días después de un golpe en el abdomen, con leucocitosis, anemia e hipocalcemia: lesión del páncreas",
    imagen: "flujogramas/nino-golpe-abdominal-hipocalcemia-pancreas.svg",
    alt: "Flujograma: Niño con dolor abdominal, palidez y náuseas 3 días después de un golpe en el abdomen, con leucocitosis, anemia e hipocalcemia: lesión del páncreas"
  },
  "CIR-102": {
    titulo: "Mujer de 30 años con 18 horas de dolor en fosa ilíaca derecha, fiebre, vómitos y leucocitosis con desviación: sospecha de apendicitis, pedir ecografía",
    imagen: "flujogramas/mujer-30-dolor-fid-fiebre-leucocitosis-alvarado-ecografia.svg",
    alt: "Flujograma: Mujer de 30 años con 18 horas de dolor en fosa ilíaca derecha, fiebre, vómitos y leucocitosis con desviación: sospecha de apendicitis, pedir ecografía"
  },
  "CIR-103": {
    titulo: "Mujer de 65 años con pesadez, prurito y ardor vespertino en las piernas y várices que aumentan de pie: insuficiencia venosa crónica, terapia compresiva",
    imagen: "flujogramas/varices-pesadez-vespertina-perthes-terapia-compresiva.svg",
    alt: "Flujograma: Mujer de 65 años con pesadez, prurito y ardor vespertino en las piernas y várices que aumentan de pie: insuficiencia venosa crónica, terapia compresiva"
  },
  "GIN-187": {
    titulo: "Paciente con lupus que desea embarazarse: debe tener al menos 6 meses de enfermedad inactiva antes de concebir (manteniendo hidroxicloroquina)",
    imagen: "flujogramas/lupus-preconcepcional-seis-meses-inactivo.svg",
    alt: "Flujograma: Paciente con lupus que desea embarazarse: debe tener al menos 6 meses de enfermedad inactiva antes de concebir (manteniendo hidroxicloroquina)"
  },
  "SP-137": {
    titulo: "Un riesgo relativo igual a 1 significa que no hay asociación entre el factor y la enfermedad",
    imagen: "flujogramas/riesgo-relativo-igual-a-uno-sin-asociacion.svg",
    alt: "Flujograma: Un riesgo relativo igual a 1 significa que no hay asociación entre el factor y la enfermedad"
  },
  "END-054": {
    titulo: "Anciana estuporosa tras una cirugía, con cicatriz de tiroidectomía, hipotermia de 32 °C, hipoventilación e hiponatremia: coma mixedematoso",
    imagen: "flujogramas/posoperada-estupor-hipotermia-cicatriz-cuello-coma-mixedematoso.svg",
    alt: "Flujograma: Anciana estuporosa tras una cirugía, con cicatriz de tiroidectomía, hipotermia de 32 °C, hipoventilación e hiponatremia: coma mixedematoso"
  },
  "PED-183": {
    titulo: "Niño de 3 años con cólicos y vómitos intermitentes, heces en «jalea de grosella» y masa en hipocondrio derecho, sin peritonitis: invaginación intestinal, enema con aire o contraste",
    imagen: "flujogramas/nino-3-anos-heces-jalea-masa-hipocondrio-enema.svg",
    alt: "Flujograma: Niño de 3 años con cólicos y vómitos intermitentes, heces en «jalea de grosella» y masa en hipocondrio derecho, sin peritonitis: invaginación intestinal, enema con aire o contraste"
  },
  "CB-072": {
    titulo: "Bebedor con vómitos, visión borrosa, somnolencia, taquipnea y acidosis metabólica con anión gap alto: intoxicación por metanol",
    imagen: "flujogramas/bebedor-vision-borrosa-anion-gap-alto-metanol.svg",
    alt: "Flujograma: Bebedor con vómitos, visión borrosa, somnolencia, taquipnea y acidosis metabólica con anión gap alto: intoxicación por metanol"
  },
  "CB-073": {
    titulo: "Trabajador que se desmaya limpiando un pozo séptico, con irritación ocular, tos y disnea: intoxicación por ácido sulfhídrico (H₂S)",
    imagen: "flujogramas/limpieza-pozo-septico-desmayo-acido-sulfhidrico.svg",
    alt: "Flujograma: Trabajador que se desmaya limpiando un pozo séptico, con irritación ocular, tos y disnea: intoxicación por ácido sulfhídrico (H₂S)"
  },
  "PED-184": {
    titulo: "Niño con síndrome nefrótico por cambios mínimos cuya proteinuria reaparece al bajar la dosis de corticoides: síndrome nefrótico corticodependiente",
    imagen: "flujogramas/nefrotico-recae-al-bajar-corticoides-corticodependencia.svg",
    alt: "Flujograma: Niño con síndrome nefrótico por cambios mínimos cuya proteinuria reaparece al bajar la dosis de corticoides: síndrome nefrótico corticodependiente"
  },
  "PED-185": {
    titulo: "Niño con fracturas a repetición, escleróticas azules, huesos largos cortos y arqueados e hipomineralización: osteogénesis imperfecta",
    imagen: "flujogramas/fracturas-repeticion-escleras-azules-osteogenesis-imperfecta.svg",
    alt: "Flujograma: Niño con fracturas a repetición, escleróticas azules, huesos largos cortos y arqueados e hipomineralización: osteogénesis imperfecta"
  },
  "GIN-188": {
    titulo: "Para tamizar síndrome de Down por ecografía, la translucencia nucal se mide entre las semanas 11 y 14",
    imagen: "flujogramas/hijo-down-translucencia-nucal-11-14-semanas.svg",
    alt: "Flujograma: Para tamizar síndrome de Down por ecografía, la translucencia nucal se mide entre las semanas 11 y 14"
  },
  "REU-056": {
    titulo: "Joven obeso con primera monoartritis aguda de rodilla y ácido úrico de 9: para confirmar gota se estudia el líquido sinovial (cristales de urato)",
    imagen: "flujogramas/obeso-joven-monoartritis-rodilla-acido-urico-liquido-sinovial.svg",
    alt: "Flujograma: Joven obeso con primera monoartritis aguda de rodilla y ácido úrico de 9: para confirmar gota se estudia el líquido sinovial (cristales de urato)"
  },
  "PED-186": {
    titulo: "Prematuro de 32 semanas y 1200 g que a los 5 días deja de tolerar, con vómitos, distensión y aire en la pared intestinal: enterocolitis necrotizante",
    imagen: "flujogramas/prematuro-1200-g-distension-neumatosis-enterocolitis.svg",
    alt: "Flujograma: Prematuro de 32 semanas y 1200 g que a los 5 días deja de tolerar, con vómitos, distensión y aire en la pared intestinal: enterocolitis necrotizante"
  },
  "INF-091": {
    titulo: "Brote escolar de vómitos, dolor abdominal y diarrea acuosa 6 horas después de comer ensalada con mayonesa: toxina preformada, Bacillus cereus",
    imagen: "flujogramas/brote-escolar-mayonesa-6-horas-bacillus-cereus.svg",
    alt: "Flujograma: Brote escolar de vómitos, dolor abdominal y diarrea acuosa 6 horas después de comer ensalada con mayonesa: toxina preformada, Bacillus cereus"
  },
  "TRA-043": {
    titulo: "Lactante con displasia de cadera tratada con arnés de Pavlik en abducción excesiva: la complicación es la necrosis avascular de la cabeza femoral",
    imagen: "flujogramas/pavlik-abduccion-excesiva-necrosis-avascular-cabeza-femoral.svg",
    alt: "Flujograma: Lactante con displasia de cadera tratada con arnés de Pavlik en abducción excesiva: la complicación es la necrosis avascular de la cabeza femoral"
  },
  "SP-138": {
    titulo: "Se comparan 30 mujeres con cáncer de mama y 30 sin él, emparejadas, preguntando por su lactancia: estudio de casos y controles (apareado)",
    imagen: "flujogramas/cancer-mama-emparejadas-lactancia-casos-controles.svg",
    alt: "Flujograma: Se comparan 30 mujeres con cáncer de mama y 30 sin él, emparejadas, preguntando por su lactancia: estudio de casos y controles (apareado)"
  },
  "TRA-044": {
    titulo: "Niña con una masa quística firme, indolora, de 3 cm en la cara posterointerna de la rodilla, sin limitación funcional: quiste benigno (ganglión/quiste poplíteo)",
    imagen: "flujogramas/nina-bolita-popliteo-indolora-ganglion.svg",
    alt: "Flujograma: Niña con una masa quística firme, indolora, de 3 cm en la cara posterointerna de la rodilla, sin limitación funcional: quiste benigno (ganglión/quiste poplíteo)"
  },
  "NRL-049": {
    titulo: "Adolescente rural con cefalea recurrente, convulsiones y calcificaciones cerebrales múltiples: neurocisticercosis por Taenia solium",
    imagen: "flujogramas/adolescente-rural-convulsiones-calcificaciones-taenia-solium.svg",
    alt: "Flujograma: Adolescente rural con cefalea recurrente, convulsiones y calcificaciones cerebrales múltiples: neurocisticercosis por Taenia solium"
  },
  "NEF-076": {
    titulo: "Varón con 20 años de osteomielitis que desarrolla síndrome nefrótico (proteinuria 7 g/24 h, albúmina 2,1) y falla renal: amiloidosis renal secundaria (AA)",
    imagen: "flujogramas/osteomielitis-cronica-anasarca-proteinuria-amiloidosis.svg",
    alt: "Flujograma: Varón con 20 años de osteomielitis que desarrolla síndrome nefrótico (proteinuria 7 g/24 h, albúmina 2,1) y falla renal: amiloidosis renal secundaria (AA)"
  },
  "OFT-043": {
    titulo: "Niño con otitis media aguda que recibió amoxicilina hace un mes: el antibiótico de elección es amoxicilina con ácido clavulánico",
    imagen: "flujogramas/otitis-media-recurrente-amoxicilina-previa-amoxicilina-clavulanico.svg",
    alt: "Flujograma: Niño con otitis media aguda que recibió amoxicilina hace un mes: el antibiótico de elección es amoxicilina con ácido clavulánico"
  },
  "SP-139": {
    titulo: "Niño de 9 años elegido para un ensayo clínico: además de su asentimiento, la madre debe firmar el consentimiento informado (en un idioma que entienda)",
    imagen: "flujogramas/nino-9-anos-ensayo-asentimiento-madre-firma.svg",
    alt: "Flujograma: Niño de 9 años elegido para un ensayo clínico: además de su asentimiento, la madre debe firmar el consentimiento informado (en un idioma que entienda)"
  },
  "SP-140": {
    titulo: "Se entregó sulfato ferroso pero 1 de cada 10 madres no lo da: el indicador comprometido es la efectividad (el resultado en condiciones reales)",
    imagen: "flujogramas/sulfato-ferroso-entregado-no-administrado-efectividad.svg",
    alt: "Flujograma: Se entregó sulfato ferroso pero 1 de cada 10 madres no lo da: el indicador comprometido es la efectividad (el resultado en condiciones reales)"
  },
  "SP-141": {
    titulo: "Un centro de salud I-4 identifica población con discapacidad sin acceso: la solución que garantiza la atención es implementar una UPSS de medicina de rehabilitación",
    imagen: "flujogramas/centro-i4-discapacidad-sin-acceso-upss-rehabilitacion.svg",
    alt: "Flujograma: Un centro de salud I-4 identifica población con discapacidad sin acceso: la solución que garantiza la atención es implementar una UPSS de medicina de rehabilitación"
  },
  "PED-187": {
    titulo: "Niña de 4 años con 3 días de rinitis, tos y fiebre que luego presenta aleteo nasal, polipnea, tiraje y crepitantes: neumonía grave, Rx de tórax para confirmar",
    imagen: "flujogramas/preescolar-fiebre-polipnea-tirajes-crepitantes-rx-torax.svg",
    alt: "Flujograma: Niña de 4 años con 3 días de rinitis, tos y fiebre que luego presenta aleteo nasal, polipnea, tiraje y crepitantes: neumonía grave, Rx de tórax para confirmar"
  },
  "GIN-189": {
    titulo: "Puérpera de 6 días con una tumoración de 3 cm en la episiotomía, sin signos de inflamación: hematoma pequeño estable, analgésicos y observación",
    imagen: "flujogramas/puerpera-hematoma-3-cm-episiotomia-observacion.svg",
    alt: "Flujograma: Puérpera de 6 días con una tumoración de 3 cm en la episiotomía, sin signos de inflamación: hematoma pequeño estable, analgésicos y observación"
  },
  "END-055": {
    titulo: "Anciano diabético con confusión, conducta bizarra y glucosa de 50 con creatinina de 1,8: hipoglucemia por glibenclamida (se acumula en la falla renal)",
    imagen: "flujogramas/anciano-falla-renal-glucosa-50-glibenclamida.svg",
    alt: "Flujograma: Anciano diabético con confusión, conducta bizarra y glucosa de 50 con creatinina de 1,8: hipoglucemia por glibenclamida (se acumula en la falla renal)"
  },
  "NEF-077": {
    titulo: "Joven con hematuria macroscópica recurrente a los pocos días de infecciones respiratorias, hematíes dismórficos y proteinuria leve: nefropatía por IgA",
    imagen: "flujogramas/hematuria-tras-infeccion-respiratoria-nefropatia-iga.svg",
    alt: "Flujograma: Joven con hematuria macroscópica recurrente a los pocos días de infecciones respiratorias, hematíes dismórficos y proteinuria leve: nefropatía por IgA"
  },
  "CAR-063": {
    titulo: "Varón de 60 años con angina, síncope de esfuerzo y disnea, pulso parvus y soplo sistólico eyectivo: estenosis aórtica grave",
    imagen: "flujogramas/angina-sincope-disnea-pulso-parvus-estenosis-aortica.svg",
    alt: "Flujograma: Varón de 60 años con angina, síncope de esfuerzo y disnea, pulso parvus y soplo sistólico eyectivo: estenosis aórtica grave"
  },
  "END-056": {
    titulo: "Diabético atendido en un I-4: la albuminuria mayor de 300 mg/24 h (nefropatía establecida) es criterio para referirlo al siguiente nivel",
    imagen: "flujogramas/dm2-establecimiento-i4-albuminuria-300-referir.svg",
    alt: "Flujograma: Diabético atendido en un I-4: la albuminuria mayor de 300 mg/24 h (nefropatía establecida) es criterio para referirlo al siguiente nivel"
  },
  "GIN-190": {
    titulo: "Mujer con incontinencia de urgencia, sin escape al Valsalva, cistocele leve y residuo posmiccional de 150 mL: pedir urodinamia",
    imagen: "flujogramas/urgencia-miccional-residuo-150-urodinamia.svg",
    alt: "Flujograma: Mujer con incontinencia de urgencia, sin escape al Valsalva, cistocele leve y residuo posmiccional de 150 mL: pedir urodinamia"
  },
  "SP-142": {
    titulo: "Para implementar el seguimiento de pacientes y contactos en un centro I-3, la prioridad 1 (MINSA) es organizar los equipos de intervención integral",
    imagen: "flujogramas/centro-i3-seguimiento-casos-contactos-equipos-intervencion.svg",
    alt: "Flujograma: Para implementar el seguimiento de pacientes y contactos en un centro I-3, la prioridad 1 (MINSA) es organizar los equipos de intervención integral"
  },
  "INF-092": {
    titulo: "Niño con hematoquecia, tenesmo, prolapso rectal y anemia grave (Hb 5): tricocefalosis masiva por Trichuris trichiura",
    imagen: "flujogramas/nino-prolapso-rectal-hematoquezia-anemia-tricocefalo.svg",
    alt: "Flujograma: Niño con hematoquecia, tenesmo, prolapso rectal y anemia grave (Hb 5): tricocefalosis masiva por Trichuris trichiura"
  },
  "GIN-191": {
    titulo: "Multípara de 39 semanas en expulsivo (dilatación completa) con presentación de nalgas puras y partos vaginales previos: atención del parto vaginal",
    imagen: "flujogramas/multipara-nalgas-puras-expulsivo-parto-vaginal.svg",
    alt: "Flujograma: Multípara de 39 semanas en expulsivo (dilatación completa) con presentación de nalgas puras y partos vaginales previos: atención del parto vaginal"
  },
  "NEU-053": {
    titulo: "Obeso con COVID-19, SatO₂ 90 %, PaO₂ 64, FR 26 y PaO₂/FiO₂ de 305: falla respiratoria leve, oxigenoterapia convencional no invasiva (cánula o mascarilla)",
    imagen: "flujogramas/covid-pafi-305-oxigenoterapia-convencional.svg",
    alt: "Flujograma: Obeso con COVID-19, SatO₂ 90 %, PaO₂ 64, FR 26 y PaO₂/FiO₂ de 305: falla respiratoria leve, oxigenoterapia convencional no invasiva (cánula o mascarilla)"
  },
  "CAR-064": {
    titulo: "Paciente monitorizada que pierde la conciencia con asistolia en el monitor: ritmo no desfibrilable, RCP y adrenalina lo antes posible",
    imagen: "flujogramas/monitor-asistolia-adrenalina-rcp.svg",
    alt: "Flujograma: Paciente monitorizada que pierde la conciencia con asistolia en el monitor: ritmo no desfibrilable, RCP y adrenalina lo antes posible"
  },
  "HEM-036": {
    titulo: "Joven afrodescendiente con anemia, ictericia indirecta, reticulocitos en 0 % y banda anormal en la electroforesis: drepanocitosis (con crisis aplásica); en el frotis hay drepanocitos",
    imagen: "flujogramas/afrodescendiente-anemia-ictericia-reticulocitos-0-drepanocitos.svg",
    alt: "Flujograma: Joven afrodescendiente con anemia, ictericia indirecta, reticulocitos en 0 % y banda anormal en la electroforesis: drepanocitosis (con crisis aplásica); en el frotis hay drepanocitos"
  },
  "PED-188": {
    titulo: "Niño con peso al nacer de 2100 g (bajo peso): la suplementación preventiva con hierro empieza al mes de vida",
    imagen: "flujogramas/bajo-peso-2100-g-hierro-desde-el-primer-mes.svg",
    alt: "Flujograma: Niño con peso al nacer de 2100 g (bajo peso): la suplementación preventiva con hierro empieza al mes de vida"
  },
  "CIR-104": {
    titulo: "Anciano hipertenso con dolor abdominal desproporcionado que se generaliza, melena, irritación peritoneal, leucocitosis, LDH alta y neumatosis: isquemia mesentérica aguda",
    imagen: "flujogramas/anciano-melena-dolor-difuso-neumatosis-ldh-isquemia-mesenterica.svg",
    alt: "Flujograma: Anciano hipertenso con dolor abdominal desproporcionado que se generaliza, melena, irritación peritoneal, leucocitosis, LDH alta y neumatosis: isquemia mesentérica aguda"
  },
  "GIN-192": {
    titulo: "Perforación uterina con el histerómetro durante un legrado, sin sangrado activo: observación con control de funciones vitales",
    imagen: "flujogramas/legrado-perforacion-histerometro-sin-sangrado-observar.svg",
    alt: "Flujograma: Perforación uterina con el histerómetro durante un legrado, sin sangrado activo: observación con control de funciones vitales"
  },
  "NEU-054": {
    titulo: "Puérpera con tuberculosis sensible en tratamiento desde el tercer trimestre: puede dar de lactar usando mascarilla",
    imagen: "flujogramas/puerpera-tb-en-tratamiento-lactancia-con-mascarilla.svg",
    alt: "Flujograma: Puérpera con tuberculosis sensible en tratamiento desde el tercer trimestre: puede dar de lactar usando mascarilla"
  },
  "PED-189": {
    titulo: "Lactante de 1 mes, nacida en casa (sin vitamina K) y con lactancia exclusiva, con sangrado de mucosas, hematemesis, palidez e irritabilidad: enfermedad hemorrágica tardía por déficit de vitamina K",
    imagen: "flujogramas/lactante-1-mes-parto-domiciliario-sangrado-vitamina-k.svg",
    alt: "Flujograma: Lactante de 1 mes, nacida en casa (sin vitamina K) y con lactancia exclusiva, con sangrado de mucosas, hematemesis, palidez e irritabilidad: enfermedad hemorrágica tardía por déficit de vitamina K"
  },
  "NRL-050": {
    titulo: "Anciano con temblor de manos que desaparece al iniciar el movimiento y reaparece al llegar a la boca, con bradicinesia: temblor parkinsoniano (de reposo)",
    imagen: "flujogramas/anciano-temblor-reposo-reemergente-bradicinesia-parkinsoniano.svg",
    alt: "Flujograma: Anciano con temblor de manos que desaparece al iniciar el movimiento y reaparece al llegar a la boca, con bradicinesia: temblor parkinsoniano (de reposo)"
  },
  "SP-143": {
    titulo: "Ante el aumento de obesidad en escolares por falta de actividad física, promover un campo deportivo en el distrito es cuidado comunitario de la salud",
    imagen: "flujogramas/obesidad-escolar-campo-deportivo-cuidado-comunitario.svg",
    alt: "Flujograma: Ante el aumento de obesidad en escolares por falta de actividad física, promover un campo deportivo en el distrito es cuidado comunitario de la salud"
  },
  "OFT-044": {
    titulo: "Adulto mayor que se limpia los oídos con hisopo y presenta hipoacusia y tinnitus de inicio reciente: tapón de cerumen",
    imagen: "flujogramas/hisopo-hipoacusia-tinnitus-tapon-cerumen.svg",
    alt: "Flujograma: Adulto mayor que se limpia los oídos con hisopo y presenta hipoacusia y tinnitus de inicio reciente: tapón de cerumen"
  },
  "INF-093": {
    titulo: "Gestante de 14 semanas con VIH, asintomática y PPD de más de 5 mm: infección tuberculosa latente, terapia preventiva con isoniazida por 6 meses",
    imagen: "flujogramas/gestante-vih-ppd-6-mm-isoniacida-6-meses.svg",
    alt: "Flujograma: Gestante de 14 semanas con VIH, asintomática y PPD de más de 5 mm: infección tuberculosa latente, terapia preventiva con isoniazida por 6 meses"
  },
  "HEM-037": {
    titulo: "Anciana con deterioro cognitivo, anorexia, palidez y pancitopenia con macrocitosis (VCM 105): anemia megaloblástica por déficit de B12, tratar con cianocobalamina",
    imagen: "flujogramas/anciana-deterioro-cognitivo-vcm-105-pancitopenia-b12.svg",
    alt: "Flujograma: Anciana con deterioro cognitivo, anorexia, palidez y pancitopenia con macrocitosis (VCM 105): anemia megaloblástica por déficit de B12, tratar con cianocobalamina"
  },
  "SP-144": {
    titulo: "El monitoreo del desempeño de los establecimientos debe basarse en evidencias verificables: tiene que ser objetivo",
    imagen: "flujogramas/monitoreo-desempeno-evidencias-verificables-objetivo.svg",
    alt: "Flujograma: El monitoreo del desempeño de los establecimientos debe basarse en evidencias verificables: tiene que ser objetivo"
  },
  "PED-190": {
    titulo: "Recién nacido de 16 horas con distensión, vómitos biliosos, sin ano, periné plano y pliegue glúteo poco visible: malformación anorrectal alta, colostomía inicial",
    imagen: "flujogramas/rn-perine-plano-sin-orificio-anal-colostomia.svg",
    alt: "Flujograma: Recién nacido de 16 horas con distensión, vómitos biliosos, sin ano, periné plano y pliegue glúteo poco visible: malformación anorrectal alta, colostomía inicial"
  },
  "PSI-037": {
    titulo: "Niño de 4 años que despierta bruscamente en pánico, se sienta en la cama y no recuerda nada a la mañana, con desarrollo normal: terrores nocturnos, explicar que se autolimitan",
    imagen: "flujogramas/nino-4-anos-despierta-panico-sin-recuerdo-terror-nocturno.svg",
    alt: "Flujograma: Niño de 4 años que despierta bruscamente en pánico, se sienta en la cama y no recuerda nada a la mañana, con desarrollo normal: terrores nocturnos, explicar que se autolimitan"
  },
  "END-057": {
    titulo: "Posoperada de tiroidectomía con parestesias peribucales, calambres y signo de Chvostek: hipocalcemia por lesión de las paratiroides, pedir calcio sérico",
    imagen: "flujogramas/postiroidectomia-parestesias-chvostek-calcio-serico.svg",
    alt: "Flujograma: Posoperada de tiroidectomía con parestesias peribucales, calambres y signo de Chvostek: hipocalcemia por lesión de las paratiroides, pedir calcio sérico"
  },
  "TRA-045": {
    titulo: "Niño con herida en la pierna que luego tiene celulitis, fiebre y cojera, y tras antibiótico persiste el dolor: sospecha de osteomielitis, Rx de pierna para el seguimiento",
    imagen: "flujogramas/escolar-herida-pierna-fiebre-dolor-persistente-radiografia.svg",
    alt: "Flujograma: Niño con herida en la pierna que luego tiene celulitis, fiebre y cojera, y tras antibiótico persiste el dolor: sospecha de osteomielitis, Rx de pierna para el seguimiento"
  },
  "GIN-193": {
    titulo: "Gran multípara con presentación cefálica flotante: si se rompen las membranas, el riesgo más frecuente es el prolapso de cordón",
    imagen: "flujogramas/multipara-cabeza-flotante-amniotomia-prolapso-cordon.svg",
    alt: "Flujograma: Gran multípara con presentación cefálica flotante: si se rompen las membranas, el riesgo más frecuente es el prolapso de cordón"
  },
  "INF-094": {
    titulo: "Adolescente de zona tropical con lesiones infiltradas en frente, pómulos y orejas, pérdida de sensibilidad, atrofia de manos, baciloscopía positiva y Mitsuda negativo: lepra lepromatosa",
    imagen: "flujogramas/adolescente-infiltracion-orejas-atrofia-tenar-baar-mitsuda-negativo.svg",
    alt: "Flujograma: Adolescente de zona tropical con lesiones infiltradas en frente, pómulos y orejas, pérdida de sensibilidad, atrofia de manos, baciloscopía positiva y Mitsuda negativo: lepra lepromatosa"
  },
  "GIN-194": {
    titulo: "Primigesta a término en trabajo de parto (7 cm) con feto en situación transversa y membranas rotas: cesárea",
    imagen: "flujogramas/primigesta-7-cm-situacion-transversa-cesarea.svg",
    alt: "Flujograma: Primigesta a término en trabajo de parto (7 cm) con feto en situación transversa y membranas rotas: cesárea"
  },
  "GAS-065": {
    titulo: "Cirrótico con ascitis, fiebre, dolor abdominal difuso y somnolencia, con 500 polimorfonucleares/µL en el líquido ascítico: peritonitis bacteriana espontánea",
    imagen: "flujogramas/cirrotico-fiebre-dolor-pmn-500-peritonitis-espontanea.svg",
    alt: "Flujograma: Cirrótico con ascitis, fiebre, dolor abdominal difuso y somnolencia, con 500 polimorfonucleares/µL en el líquido ascítico: peritonitis bacteriana espontánea"
  },
  "SP-145": {
    titulo: "Comparar un colegio que recibe más micronutrientes con otro colegio de control, sin asignación al azar, es un diseño cuasiexperimental",
    imagen: "flujogramas/micronutrientes-colegio-control-cuasiexperimental.svg",
    alt: "Flujograma: Comparar un colegio que recibe más micronutrientes con otro colegio de control, sin asignación al azar, es un diseño cuasiexperimental"
  },
  "INF-095": {
    titulo: "Obeso con fiebre y placa eritematosa caliente de bordes irregulares en la pantorrilla, sin signos de trombosis: celulitis (S. aureus o estreptococo)",
    imagen: "flujogramas/obeso-placa-eritematosa-pantorrilla-fiebre-celulitis.svg",
    alt: "Flujograma: Obeso con fiebre y placa eritematosa caliente de bordes irregulares en la pantorrilla, sin signos de trombosis: celulitis (S. aureus o estreptococo)"
  },
  "PED-191": {
    titulo: "Preescolar con diarrea, deshidratación moderada y sodio de 160: deshidratación hipernatrémica, calcular el déficit y reponerlo lentamente (≥ 48 h)",
    imagen: "flujogramas/preescolar-diarrea-sodio-160-calcular-deficit.svg",
    alt: "Flujograma: Preescolar con diarrea, deshidratación moderada y sodio de 160: deshidratación hipernatrémica, calcular el déficit y reponerlo lentamente (≥ 48 h)"
  },
  "SP-146": {
    titulo: "La búsqueda activa y captación de sintomáticos respiratorios para detectar tuberculosis es prevención secundaria (diagnóstico precoz)",
    imagen: "flujogramas/busqueda-activa-sintomaticos-respiratorios-prevencion-secundaria.svg",
    alt: "Flujograma: La búsqueda activa y captación de sintomáticos respiratorios para detectar tuberculosis es prevención secundaria (diagnóstico precoz)"
  },
  "CIR-105": {
    titulo: "Paciente quemado con quemaduras de tercer grado en más del 20 % de la superficie corporal: requiere traslado a una unidad especializada",
    imagen: "flujogramas/quemadura-tercer-grado-mayor-20-unidad-quemados.svg",
    alt: "Flujograma: Paciente quemado con quemaduras de tercer grado en más del 20 % de la superficie corporal: requiere traslado a una unidad especializada"
  },
  "NEF-078": {
    titulo: "El pilar del tratamiento no quirúrgico de la hiperplasia benigna de próstata son los bloqueadores alfa-1 (tamsulosina), que alivian rápido los síntomas",
    imagen: "flujogramas/hiperplasia-prostatica-pilar-medico-alfa-bloqueador.svg",
    alt: "Flujograma: El pilar del tratamiento no quirúrgico de la hiperplasia benigna de próstata son los bloqueadores alfa-1 (tamsulosina), que alivian rápido los síntomas"
  },
  "PED-192": {
    titulo: "Lactante con diarrea, sed, irritabilidad, ojos hundidos, mucosa seca y pliegue positivo, pero con llenado capilar < 2 s: deshidratación (plan B), rehidratación oral",
    imagen: "flujogramas/lactante-ojos-hundidos-sed-pliegue-rehidratacion-oral.svg",
    alt: "Flujograma: Lactante con diarrea, sed, irritabilidad, ojos hundidos, mucosa seca y pliegue positivo, pero con llenado capilar < 2 s: deshidratación (plan B), rehidratación oral"
  },
  "GIN-195": {
    titulo: "Primigesta con lupus eritematoso sistémico: su riesgo de trastorno hipertensivo del embarazo es alto (indica aspirina a dosis baja)",
    imagen: "flujogramas/primigesta-lupus-riesgo-alto-trastorno-hipertensivo.svg",
    alt: "Flujograma: Primigesta con lupus eritematoso sistémico: su riesgo de trastorno hipertensivo del embarazo es alto (indica aspirina a dosis baja)"
  },
  "END-058": {
    titulo: "Para suplementar vitamina D en un anciano con dolores musculares y fracturas, la forma adecuada es el colecalciferol (vitamina D3)",
    imagen: "flujogramas/anciano-fracturas-suplemento-vitamina-d-colecalciferol.svg",
    alt: "Flujograma: Para suplementar vitamina D en un anciano con dolores musculares y fracturas, la forma adecuada es el colecalciferol (vitamina D3)"
  },
  "REU-057": {
    titulo: "Adolescente con acné vulgar en cara y tronco: el tratamiento de primera elección son los retinoides tópicos",
    imagen: "flujogramas/adolescente-acne-rostro-tronco-retinoide-topico.svg",
    alt: "Flujograma: Adolescente con acné vulgar en cara y tronco: el tratamiento de primera elección son los retinoides tópicos"
  },
  "OFT-045": {
    titulo: "Úlcera corneal grisácea con lesiones satélites una semana después de un trauma con una rama: queratitis micótica (Aspergillus o Fusarium)",
    imagen: "flujogramas/rama-arbusto-ulcera-corneal-satelites-aspergillus.svg",
    alt: "Flujograma: Úlcera corneal grisácea con lesiones satélites una semana después de un trauma con una rama: queratitis micótica (Aspergillus o Fusarium)"
  },
  "NRL-051": {
    titulo: "Mujer con debilidad ascendente tras diarrea, arreflexia, FR 28, SatO₂ 89 %, cianosis y somnolencia: Guillain-Barré con insuficiencia respiratoria, soporte ventilatorio inmediato",
    imagen: "flujogramas/guillain-barre-disnea-sato2-89-soporte-ventilatorio.svg",
    alt: "Flujograma: Mujer con debilidad ascendente tras diarrea, arreflexia, FR 28, SatO₂ 89 %, cianosis y somnolencia: Guillain-Barré con insuficiencia respiratoria, soporte ventilatorio inmediato"
  },
  "NEF-079": {
    titulo: "Paciente en UCI con shock, falla multiorgánica y lesión renal aguda: la mejor terapia de reemplazo es la hemodiálisis continua (TRRC)",
    imagen: "flujogramas/uci-shock-falla-renal-hemodialisis-continua.svg",
    alt: "Flujograma: Paciente en UCI con shock, falla multiorgánica y lesión renal aguda: la mejor terapia de reemplazo es la hemodiálisis continua (TRRC)"
  },
  "SP-147": {
    titulo: "La madre se niega a firmar el consentimiento para la punción lumbar de su hijo: se está respetando el principio de autonomía (decisión informada del representante)",
    imagen: "flujogramas/madre-niega-puncion-lumbar-autonomia.svg",
    alt: "Flujograma: La madre se niega a firmar el consentimiento para la punción lumbar de su hijo: se está respetando el principio de autonomía (decisión informada del representante)"
  },
  "GIN-196": {
    titulo: "Gestante a término detenida en 6 cm por 4 horas con contracciones de intensidad leve y pelvis ginecoide: dinámica uterina insuficiente, estimular con oxitocina",
    imagen: "flujogramas/6-cm-cuatro-horas-dinamica-debil-oxitocina.svg",
    alt: "Flujograma: Gestante a término detenida en 6 cm por 4 horas con contracciones de intensidad leve y pelvis ginecoide: dinámica uterina insuficiente, estimular con oxitocina"
  },
  "CAR-065": {
    titulo: "El examen que mejor valora la hipoperfusión tisular en el shock es el lactato sérico",
    imagen: "flujogramas/shock-hipoperfusion-lactato-serico.svg",
    alt: "Flujograma: El examen que mejor valora la hipoperfusión tisular en el shock es el lactato sérico"
  },
  "SP-148": {
    titulo: "Evaluar la demanda, proyectar la oferta, programar metas para el próximo año y asignar recursos corresponde a la etapa de previsión (planificación) del proceso administrativo",
    imagen: "flujogramas/director-demanda-proyectada-metas-recursos-prevision.svg",
    alt: "Flujograma: Evaluar la demanda, proyectar la oferta, programar metas para el próximo año y asignar recursos corresponde a la etapa de previsión (planificación) del proceso administrativo"
  },
  "GIN-197": {
    titulo: "Mujer con flujo grisáceo, abundante y maloliente, sin inflamación y test de aminas positivo: vaginosis bacteriana, metronidazol 500 mg c/12 h por 7 días",
    imagen: "flujogramas/flujo-grisaceo-aminas-positivo-vaginosis-metronidazol.svg",
    alt: "Flujograma: Mujer con flujo grisáceo, abundante y maloliente, sin inflamación y test de aminas positivo: vaginosis bacteriana, metronidazol 500 mg c/12 h por 7 días"
  },
  "SP-149": {
    titulo: "Reorientar los sistemas de salud hacia la atención primaria exige más énfasis en la promoción de la salud y la prevención de la enfermedad",
    imagen: "flujogramas/reorientar-sistemas-aps-promocion-prevencion.svg",
    alt: "Flujograma: Reorientar los sistemas de salud hacia la atención primaria exige más énfasis en la promoción de la salud y la prevención de la enfermedad"
  },
  "REU-058": {
    titulo: "Paciente con HTLV-1 y dos años de placas hiperqueratósicas y costrosas diseminadas, poco pruriginosas, con surcos acarinos: sarna noruega (costrosa)",
    imagen: "flujogramas/htlv1-lesiones-hiperqueratosicas-costrosas-sarna-noruega.svg",
    alt: "Flujograma: Paciente con HTLV-1 y dos años de placas hiperqueratósicas y costrosas diseminadas, poco pruriginosas, con surcos acarinos: sarna noruega (costrosa)"
  },
  "NRL-052": {
    titulo: "Adolescente golpeado en la cabeza, lúcido 2 horas y luego estuporoso, con midriasis derecha, hemiparesia izquierda, bradicardia e hipertensión: hematoma epidural con herniación, TC cerebral",
    imagen: "flujogramas/golpe-ladrillo-intervalo-lucido-midriasis-hematoma-epidural.svg",
    alt: "Flujograma: Adolescente golpeado en la cabeza, lúcido 2 horas y luego estuporoso, con midriasis derecha, hemiparesia izquierda, bradicardia e hipertensión: hematoma epidural con herniación, TC cerebral"
  },
  "NEU-055": {
    titulo: "Varón de 66 años con neumonía, PA 85/55, FR 32 y taquicardia: CURB-65 de 3, hospitalizar",
    imagen: "flujogramas/neumonia-hipotension-fr-32-66-anos-curb65-hospitalizar.svg",
    alt: "Flujograma: Varón de 66 años con neumonía, PA 85/55, FR 32 y taquicardia: CURB-65 de 3, hospitalizar"
  },
  "NEU-056": {
    titulo: "Paciente con COVID-19, oxígeno domiciliario con requerimiento creciente, FR 28 y uso de músculos accesorios aunque la SatO₂ sea 92 %: referir por criterio clínico",
    imagen: "flujogramas/covid-disnea-musculos-accesorios-criterio-clinico-referencia.svg",
    alt: "Flujograma: Paciente con COVID-19, oxígeno domiciliario con requerimiento creciente, FR 28 y uso de músculos accesorios aunque la SatO₂ sea 92 %: referir por criterio clínico"
  },
  "CB-074": {
    titulo: "Niño intoxicado por monóxido de carbono al inhalar humo: el tratamiento inicial es oxígeno al 100 % (acorta la vida media de la carboxihemoglobina)",
    imagen: "flujogramas/nino-inhalacion-humo-monoxido-carbono-oxigeno-100.svg",
    alt: "Flujograma: Niño intoxicado por monóxido de carbono al inhalar humo: el tratamiento inicial es oxígeno al 100 % (acorta la vida media de la carboxihemoglobina)"
  },
  "END-059": {
    titulo: "Debut diabético en cetoacidosis con PA 80/60 y FC 130 en UCI: lo que NO se debe hacer es dar líquidos por vía oral",
    imagen: "flujogramas/cetoacidosis-debut-hipotension-no-via-oral.svg",
    alt: "Flujograma: Debut diabético en cetoacidosis con PA 80/60 y FC 130 en UCI: lo que NO se debe hacer es dar líquidos por vía oral"
  },
  "HEM-038": {
    titulo: "Mujer joven con anemia, ictericia, esplenomegalia, reticulocitos 11 %, bilirrubina indirecta alta y haptoglobina indetectable, sin esquistocitos: hemólisis extravascular, el Coombs directo confirma si es autoinmune",
    imagen: "flujogramas/hemolisis-esplenomegalia-sin-esquistocitos-coombs.svg",
    alt: "Flujograma: Mujer joven con anemia, ictericia, esplenomegalia, reticulocitos 11 %, bilirrubina indirecta alta y haptoglobina indetectable, sin esquistocitos: hemólisis extravascular, el Coombs directo confirma si es autoinmune"
  },
  "GIN-198": {
    titulo: "Puérpera con fiebre y mama congestiva, indurada, roja y caliente sin masa: mastitis puerperal, antibiótico y continuar la lactancia",
    imagen: "flujogramas/puerpera-mama-roja-dolorosa-fiebre-continuar-lactancia.svg",
    alt: "Flujograma: Puérpera con fiebre y mama congestiva, indurada, roja y caliente sin masa: mastitis puerperal, antibiótico y continuar la lactancia"
  },
  "PED-193": {
    titulo: "Preescolar con 15 días de dolor posprandial, distensión y diarrea acuosa sin sangre ni fiebre, con desnutrición: giardiasis",
    imagen: "flujogramas/preescolar-diarrea-acuosa-distension-desnutricion-giardiasis.svg",
    alt: "Flujograma: Preescolar con 15 días de dolor posprandial, distensión y diarrea acuosa sin sangre ni fiebre, con desnutrición: giardiasis"
  },
  "SP-150": {
    titulo: "Entre las funciones esenciales de la salud pública renovadas, la más ligada a la atención primaria es la promoción de la salud",
    imagen: "flujogramas/funcion-esencial-salud-publica-aps-promocion.svg",
    alt: "Flujograma: Entre las funciones esenciales de la salud pública renovadas, la más ligada a la atención primaria es la promoción de la salud"
  },
  "SP-151": {
    titulo: "Una desventaja de los estudios de casos y controles es su mayor riesgo de sesgo de selección (y de memoria)",
    imagen: "flujogramas/casos-controles-desventaja-sesgo-seleccion.svg",
    alt: "Flujograma: Una desventaja de los estudios de casos y controles es su mayor riesgo de sesgo de selección (y de memoria)"
  },
  "NEF-080": {
    titulo: "Falla renal aguda con potasio de 8 y bradiarritmia con bloqueo AV de 2.º grado: la prioridad es corregir la hiperpotasemia (calcio EV primero)",
    imagen: "flujogramas/falla-renal-k-8-bradiarritmia-corregir-hiperkalemia.svg",
    alt: "Flujograma: Falla renal aguda con potasio de 8 y bradiarritmia con bloqueo AV de 2.º grado: la prioridad es corregir la hiperpotasemia (calcio EV primero)"
  },
  "GIN-199": {
    titulo: "Gestante de 8 semanas con sangrado, dolor, cuello abierto con membranas protruyendo y embrión vivo: aborto inminente",
    imagen: "flujogramas/8-semanas-cervix-abierto-membranas-protruyen-aborto-inminente.svg",
    alt: "Flujograma: Gestante de 8 semanas con sangrado, dolor, cuello abierto con membranas protruyendo y embrión vivo: aborto inminente"
  },
  "NEU-057": {
    titulo: "Gestante de 33 semanas con PPD positivo sin tuberculosis activa: infección latente, la terapia preventiva puede iniciarse a los 3 meses posparto (salvo alto riesgo)",
    imagen: "flujogramas/gestante-33-semanas-ppd-positivo-tratar-postparto.svg",
    alt: "Flujograma: Gestante de 33 semanas con PPD positivo sin tuberculosis activa: infección latente, la terapia preventiva puede iniciarse a los 3 meses posparto (salvo alto riesgo)"
  },
  "INF-096": {
    titulo: "Niño con molestias digestivas, tos con esputo hemoptoico y eosinofilia: ascariasis en fase de migración pulmonar (síndrome de Löffler)",
    imagen: "flujogramas/nino-tos-hemoptoica-eosinofilia-ascaris-loeffler.svg",
    alt: "Flujograma: Niño con molestias digestivas, tos con esputo hemoptoico y eosinofilia: ascariasis en fase de migración pulmonar (síndrome de Löffler)"
  },
  "OFT-046": {
    titulo: "Adolescente con rinorrea acuosa, prurito nasal y ocular y mucosa nasal edematosa: rinitis alérgica, la prueba cutánea (prick test) confirma la sensibilización",
    imagen: "flujogramas/adolescente-rinorrea-prurito-nasal-ocular-prick-test.svg",
    alt: "Flujograma: Adolescente con rinorrea acuosa, prurito nasal y ocular y mucosa nasal edematosa: rinitis alérgica, la prueba cutánea (prick test) confirma la sensibilización"
  },
  "GIN-200": {
    titulo: "Pareja que busca embarazo hace 6 meses con mujer de 38 años: iniciar el estudio de infertilidad (no esperar al año)",
    imagen: "flujogramas/mujer-38-seis-meses-sin-embarazo-estudio-infertilidad.svg",
    alt: "Flujograma: Pareja que busca embarazo hace 6 meses con mujer de 38 años: iniciar el estudio de infertilidad (no esperar al año)"
  },
  "PSI-038": {
    titulo: "Mujer con relaciones inestables, autolesiones, amenazas suicidas, impulsividad, consumo de drogas y miedo intenso al abandono: trastorno límite de la personalidad",
    imagen: "flujogramas/autolesiones-miedo-abandono-relaciones-inestables-limite.svg",
    alt: "Flujograma: Mujer con relaciones inestables, autolesiones, amenazas suicidas, impulsividad, consumo de drogas y miedo intenso al abandono: trastorno límite de la personalidad"
  },
  "GIN-201": {
    titulo: "Primigesta Rh negativo con Coombs indirecto negativo a las 13 semanas: la inmunoglobulina anti-D profiláctica se aplica a las 28 semanas (y en las 72 h posparto si el RN es Rh positivo)",
    imagen: "flujogramas/rh-negativo-coombs-negativo-anti-d-28-semanas.svg",
    alt: "Flujograma: Primigesta Rh negativo con Coombs indirecto negativo a las 13 semanas: la inmunoglobulina anti-D profiláctica se aplica a las 28 semanas (y en las 72 h posparto si el RN es Rh positivo)"
  },
  "CIR-106": {
    titulo: "Mujer con cesárea previa y 2 días de dolor, distensión, vómitos y estreñimiento: obstrucción intestinal (probables bridas), Rx simple de abdomen de pie",
    imagen: "flujogramas/cesarea-previa-distension-vomitos-bridas-rx-de-pie.svg",
    alt: "Flujograma: Mujer con cesárea previa y 2 días de dolor, distensión, vómitos y estreñimiento: obstrucción intestinal (probables bridas), Rx simple de abdomen de pie"
  },
  "NEU-058": {
    titulo: "EPOC con neumonía, SatO₂ 86 % y acidosis respiratoria leve: oxigenoterapia controlada (meta 88-92 %) de inmediato",
    imagen: "flujogramas/epoc-neumonia-sato2-86-oxigenoterapia-controlada.svg",
    alt: "Flujograma: EPOC con neumonía, SatO₂ 86 % y acidosis respiratoria leve: oxigenoterapia controlada (meta 88-92 %) de inmediato"
  },
  "NEU-059": {
    titulo: "EPOC con SatO₂ de 85 % en reposo y hematocrito de 49 %: el oxígeno domiciliario se usa de forma continua (≥ 15 h/día) porque aumenta la supervivencia",
    imagen: "flujogramas/epoc-sato2-85-oxigeno-domiciliario-permanente.svg",
    alt: "Flujograma: EPOC con SatO₂ de 85 % en reposo y hematocrito de 49 %: el oxígeno domiciliario se usa de forma continua (≥ 15 h/día) porque aumenta la supervivencia"
  },
  "GIN-202": {
    titulo: "Primigesta de 39 semanas con 12 horas de rotura de membranas, sin trabajo de parto, feto bien y cuello favorable: inducir el trabajo de parto",
    imagen: "flujogramas/rpm-39-semanas-12-horas-bishop-favorable-induccion.svg",
    alt: "Flujograma: Primigesta de 39 semanas con 12 horas de rotura de membranas, sin trabajo de parto, feto bien y cuello favorable: inducir el trabajo de parto"
  },
  "GAS-066": {
    titulo: "Varón de 68 años con anemia leve y sangre oculta en heces positiva: colonoscopía completa (descartar cáncer colorrectal)",
    imagen: "flujogramas/anciano-anemia-thevenon-positivo-colonoscopia.svg",
    alt: "Flujograma: Varón de 68 años con anemia leve y sangre oculta en heces positiva: colonoscopía completa (descartar cáncer colorrectal)"
  },
  "GIN-203": {
    titulo: "Gestante de 37 semanas con 2 días de rotura de membranas, fiebre de 39 °C, taquicardia fetal, útero doloroso y líquido purulento: corioamnionitis, antibiótico y traslado al hospital",
    imagen: "flujogramas/rpm-2-dias-fiebre-liquido-purulento-antibiotico-referir.svg",
    alt: "Flujograma: Gestante de 37 semanas con 2 días de rotura de membranas, fiebre de 39 °C, taquicardia fetal, útero doloroso y líquido purulento: corioamnionitis, antibiótico y traslado al hospital"
  },
  "GIN-204": {
    titulo: "Gestante que no recuerda su FUR: el método más exacto para saber la edad gestacional es la ecografía transvaginal temprana",
    imagen: "flujogramas/sin-fur-test-positivo-ecografia-transvaginal-edad-gestacional.svg",
    alt: "Flujograma: Gestante que no recuerda su FUR: el método más exacto para saber la edad gestacional es la ecografía transvaginal temprana"
  },
  "PED-194": {
    titulo: "En menores de 5 años, la obesidad se define por un peso para la talla por encima de +3 desviaciones estándar (OMS)",
    imagen: "flujogramas/menor-5-anos-peso-talla-mas-3-de-obesidad.svg",
    alt: "Flujograma: En menores de 5 años, la obesidad se define por un peso para la talla por encima de +3 desviaciones estándar (OMS)"
  },
  "INF-097": {
    titulo: "Trabajador ganadero con 8 meses de poliartralgias, fiebre ondulante y sudoración, con Rosa de Bengala positivo: brucelosis, doxiciclina + rifampicina por 6 semanas",
    imagen: "flujogramas/ganadero-fiebre-ondulante-rosa-bengala-doxiciclina-rifampicina.svg",
    alt: "Flujograma: Trabajador ganadero con 8 meses de poliartralgias, fiebre ondulante y sudoración, con Rosa de Bengala positivo: brucelosis, doxiciclina + rifampicina por 6 semanas"
  },
  "PSI-039": {
    titulo: "Adolescente con agitación, taquicardia, palpitaciones y sensación de muerte tras consumir cocaína: intoxicación simpaticomimética, diazepam",
    imagen: "flujogramas/adolescente-cocaina-agitacion-taquicardia-diazepam.svg",
    alt: "Flujograma: Adolescente con agitación, taquicardia, palpitaciones y sensación de muerte tras consumir cocaína: intoxicación simpaticomimética, diazepam"
  },
  "INF-098": {
    titulo: "Paciente en diálisis por catéter central, en el 6.º día posoperatorio, con fiebre, infiltrado alveolar y leucocitosis: neumonía nosocomial, germen más probable S. aureus",
    imagen: "flujogramas/dialisis-cateter-postoperado-neumonia-staphylococcus-aureus.svg",
    alt: "Flujograma: Paciente en diálisis por catéter central, en el 6.º día posoperatorio, con fiebre, infiltrado alveolar y leucocitosis: neumonía nosocomial, germen más probable S. aureus"
  },
  "HEM-039": {
    titulo: "Adolescente varón con hemartrosis tras un trauma, TTPa prolongado, plaquetas y agregación normales: hemofilia A (la más frecuente)",
    imagen: "flujogramas/adolescente-hemartrosis-ttpa-prolongado-hemofilia-a.svg",
    alt: "Flujograma: Adolescente varón con hemartrosis tras un trauma, TTPa prolongado, plaquetas y agregación normales: hemofilia A (la más frecuente)"
  },
  "PED-195": {
    titulo: "Lactante de 5 meses con lactancia exclusiva y Hb 11,5 (sin anemia): suplementación preventiva con hierro a 2 mg/kg/día",
    imagen: "flujogramas/lactante-5-meses-hb-11-5-hierro-2-mg-kg.svg",
    alt: "Flujograma: Lactante de 5 meses con lactancia exclusiva y Hb 11,5 (sin anemia): suplementación preventiva con hierro a 2 mg/kg/día"
  },
  "GIN-205": {
    titulo: "Mujer estable con amenorrea, útero vacío, masa anexial de 25 mm y beta-hCG de 3500 sin rotura: embarazo ectópico no roto, metotrexato",
    imagen: "flujogramas/ectopico-no-roto-25-mm-bhcg-3500-metotrexato.svg",
    alt: "Flujograma: Mujer estable con amenorrea, útero vacío, masa anexial de 25 mm y beta-hCG de 3500 sin rotura: embarazo ectópico no roto, metotrexato"
  },
  "NEF-081": {
    titulo: "Diabética con nefropatía que toma magnesio y presenta debilidad, hiporreflexia, somnolencia, hipotensión, bradicardia y Mg 4,2 mmol/L: hipermagnesemia grave, hemodiálisis",
    imagen: "flujogramas/nefropatia-magnesio-naturista-hiporreflexia-hemodialisis.svg",
    alt: "Flujograma: Diabética con nefropatía que toma magnesio y presenta debilidad, hiporreflexia, somnolencia, hipotensión, bradicardia y Mg 4,2 mmol/L: hipermagnesemia grave, hemodiálisis"
  },
  "PED-196": {
    titulo: "Niño con urticaria que en 30 minutos presenta ronquera, dificultad respiratoria y cianosis: anafilaxia con edema laríngeo, adrenalina IM",
    imagen: "flujogramas/nino-urticaria-ronquera-cianosis-anafilaxia-adrenalina.svg",
    alt: "Flujograma: Niño con urticaria que en 30 minutos presenta ronquera, dificultad respiratoria y cianosis: anafilaxia con edema laríngeo, adrenalina IM"
  },
  "GIN-206": {
    titulo: "Usuaria de T de cobre sin hilos visibles y sin DIU en la ecografía transvaginal: Rx simple de abdomen (descartar migración)",
    imagen: "flujogramas/diu-hilos-no-visibles-eco-sin-diu-rx-abdomen.svg",
    alt: "Flujograma: Usuaria de T de cobre sin hilos visibles y sin DIU en la ecografía transvaginal: Rx simple de abdomen (descartar migración)"
  },
  "NEU-060": {
    titulo: "Asmático con disnea grave y murmullo vesicular ausente en ambos hemitórax: el tórax silente es criterio de crisis con riesgo vital",
    imagen: "flujogramas/asmatico-disnea-severa-murmullo-ausente-torax-silente.svg",
    alt: "Flujograma: Asmático con disnea grave y murmullo vesicular ausente en ambos hemitórax: el tórax silente es criterio de crisis con riesgo vital"
  },
  "GIN-207": {
    titulo: "Gestante de 31 semanas con contracciones pero cérvix cerrado, cervicometría de 35 mm y fibronectina negativa: bajo riesgo de parto pretérmino, observación",
    imagen: "flujogramas/31-semanas-contracciones-cervix-35-mm-fibronectina-negativa.svg",
    alt: "Flujograma: Gestante de 31 semanas con contracciones pero cérvix cerrado, cervicometría de 35 mm y fibronectina negativa: bajo riesgo de parto pretérmino, observación"
  },
  "CIR-107": {
    titulo: "Conductor con golpe en el epigastrio contra el timón, estable, con hematoma de 3 cm en la pared duodenal en la TC: manejo conservador con observación",
    imagen: "flujogramas/golpe-timon-hematoma-pared-duodenal-observacion.svg",
    alt: "Flujograma: Conductor con golpe en el epigastrio contra el timón, estable, con hematoma de 3 cm en la pared duodenal en la TC: manejo conservador con observación"
  },
  "SP-152": {
    titulo: "Gran cantidad de roedores muertos en zonas agrícolas durante una alerta de peste: se notifica como epizootia",
    imagen: "flujogramas/piura-peste-roedores-muertos-epizootia.svg",
    alt: "Flujograma: Gran cantidad de roedores muertos en zonas agrícolas durante una alerta de peste: se notifica como epizootia"
  },
  "GIN-208": {
    titulo: "Gestante con altura uterina de 21 cm y movimientos fetales recién percibidos: por el examen clínico tiene unas 21 semanas (la FUR de 27 semanas no coincide)",
    imagen: "flujogramas/au-21-cm-fur-27-semanas-eg-clinica-21.svg",
    alt: "Flujograma: Gestante con altura uterina de 21 cm y movimientos fetales recién percibidos: por el examen clínico tiene unas 21 semanas (la FUR de 27 semanas no coincide)"
  },
  "GIN-209": {
    titulo: "Primigesta de 41+3 semanas con menos movimientos fetales, oligohidramnios, test estresante negativo y cuello desfavorable: madurar el cuello con misoprostol e inducir",
    imagen: "flujogramas/41-semanas-oligohidramnios-bishop-2-misoprostol.svg",
    alt: "Flujograma: Primigesta de 41+3 semanas con menos movimientos fetales, oligohidramnios, test estresante negativo y cuello desfavorable: madurar el cuello con misoprostol e inducir"
  },
  "HEM-040": {
    titulo: "Anticoagulado con warfarina, INR 7 y hematemesis (sangrado mayor): revertir de inmediato reponiendo factores (plasma fresco o, mejor, concentrado de complejo protrombínico) más vitamina K EV",
    imagen: "flujogramas/warfarina-inr-7-hematemesis-plasma-fresco.svg",
    alt: "Flujograma: Anticoagulado con warfarina, INR 7 y hematemesis (sangrado mayor): revertir de inmediato reponiendo factores (plasma fresco o, mejor, concentrado de complejo protrombínico) más vitamina K EV"
  },
  "REU-059": {
    titulo: "Niño con máculas hipo e hiperpigmentadas descamativas en el tronco y KOH con hifas cortas y levaduras («espaguetis con albóndigas»): pitiriasis versicolor por Malassezia globosa",
    imagen: "flujogramas/manchas-hipo-hiperpigmentadas-koh-espagueti-albondigas-malassezia.svg",
    alt: "Flujograma: Niño con máculas hipo e hiperpigmentadas descamativas en el tronco y KOH con hifas cortas y levaduras («espaguetis con albóndigas»): pitiriasis versicolor por Malassezia globosa"
  },
  "SP-153": {
    titulo: "En una epidemia de dengue muchos pacientes no pudieron ser atendidos y subió la letalidad: el elemento de la APS que debe mejorar es la cobertura (y el acceso) universal",
    imagen: "flujogramas/dengue-pacientes-no-atendidos-letalidad-cobertura.svg",
    alt: "Flujograma: En una epidemia de dengue muchos pacientes no pudieron ser atendidos y subió la letalidad: el elemento de la APS que debe mejorar es la cobertura (y el acceso) universal"
  },
  "CIR-108": {
    titulo: "Apendicectomizado al 5.º día con fiebre y dolor en la herida: infección de herida operatoria, abrir, drenar y cultivar",
    imagen: "flujogramas/apendicectomia-fiebre-herida-infectada-drenaje-cultivo.svg",
    alt: "Flujograma: Apendicectomizado al 5.º día con fiebre y dolor en la herida: infección de herida operatoria, abrir, drenar y cultivar"
  },
  "REU-060": {
    titulo: "Mujer de 35 años con 4 meses de poliartritis de manos y muñecas, rigidez matutina, anti-CCP positivo y erosiones: artritis reumatoide",
    imagen: "flujogramas/poliartritis-manos-anti-ccp-erosiones-artritis-reumatoide.svg",
    alt: "Flujograma: Mujer de 35 años con 4 meses de poliartritis de manos y muñecas, rigidez matutina, anti-CCP positivo y erosiones: artritis reumatoide"
  },
  "PED-197": {
    titulo: "Niño de 24 meses con 10 kg y 78 cm (talla muy baja para la edad con peso adecuado para la talla), prematuro y bajo peso al nacer: desnutrición crónica",
    imagen: "flujogramas/24-meses-talla-78-peso-10-desnutricion-cronica.svg",
    alt: "Flujograma: Niño de 24 meses con 10 kg y 78 cm (talla muy baja para la edad con peso adecuado para la talla), prematuro y bajo peso al nacer: desnutrición crónica"
  },
  "SP-154": {
    titulo: "Un componente para elaborar el ASIS local es el análisis de los determinantes sociales de la salud",
    imagen: "flujogramas/asis-local-analisis-determinantes-sociales.svg",
    alt: "Flujograma: Un componente para elaborar el ASIS local es el análisis de los determinantes sociales de la salud"
  },
  "CB-075": {
    titulo: "Los miofibroblastos de la cicatrización se diferencian de los fibroblastos por tener más actina y miosina (contraen la herida)",
    imagen: "flujogramas/cicatrizacion-miofibroblastos-actina-miosina.svg",
    alt: "Flujograma: Los miofibroblastos de la cicatrización se diferencian de los fibroblastos por tener más actina y miosina (contraen la herida)"
  },
  "PED-198": {
    titulo: "Neonato con holoprosencefalia, hipotelorismo, labio y paladar hendido, polidactilia, onfalocele y cardiopatía: trisomía 13 (síndrome de Patau)",
    imagen: "flujogramas/neonato-holoprosencefalia-polidactilia-labio-leporino-trisomia-13.svg",
    alt: "Flujograma: Neonato con holoprosencefalia, hipotelorismo, labio y paladar hendido, polidactilia, onfalocele y cardiopatía: trisomía 13 (síndrome de Patau)"
  },
  "GIN-210": {
    titulo: "Gestante de 35 semanas con corioamnionitis (fiebre, taquicardia fetal, líquido fétido) y 8 cm de dilatación con presentación en +1: antibióticos y parto vaginal",
    imagen: "flujogramas/35-semanas-rpm-fiebre-8-cm-antibiotico-parto-vaginal.svg",
    alt: "Flujograma: Gestante de 35 semanas con corioamnionitis (fiebre, taquicardia fetal, líquido fétido) y 8 cm de dilatación con presentación en +1: antibióticos y parto vaginal"
  },
  "CAR-066": {
    titulo: "Paciente en paro con actividad eléctrica en el monitor pero ritmo no desfibrilable: actividad eléctrica sin pulso",
    imagen: "flujogramas/dea-actividad-electrica-no-desfibrilable-aesp.svg",
    alt: "Flujograma: Paciente en paro con actividad eléctrica en el monitor pero ritmo no desfibrilable: actividad eléctrica sin pulso"
  },
  "SP-155": {
    titulo: "El instrumento del primer nivel para vigilar y hacer seguimiento a las gestantes es el radar de gestantes",
    imagen: "flujogramas/control-prenatal-primer-nivel-radar-gestantes.svg",
    alt: "Flujograma: El instrumento del primer nivel para vigilar y hacer seguimiento a las gestantes es el radar de gestantes"
  },
  "OFT-047": {
    titulo: "La causa más frecuente de epistaxis anterior es la rinitis seca anterior (mucosa seca y costras en el plexo de Kiesselbach)",
    imagen: "flujogramas/epistaxis-anterior-causa-rinitis-seca.svg",
    alt: "Flujograma: La causa más frecuente de epistaxis anterior es la rinitis seca anterior (mucosa seca y costras en el plexo de Kiesselbach)"
  },
  "PED-199": {
    titulo: "Niña de 6 años con sibilancias desde los 4 años, dermatitis atópica y sensibilización a ácaros: fenotipo de sibilancias de inicio tardío (atópico)",
    imagen: "flujogramas/nina-sibilancias-desde-4-anos-atopia-inicio-tardio.svg",
    alt: "Flujograma: Niña de 6 años con sibilancias desde los 4 años, dermatitis atópica y sensibilización a ácaros: fenotipo de sibilancias de inicio tardío (atópico)"
  },
  "GIN-211": {
    titulo: "Puérpera con preeclampsia severa en tratamiento con sulfato de magnesio: se mantiene hasta 24 horas después del parto",
    imagen: "flujogramas/preeclampsia-severa-sulfato-magnesio-24-h-posparto.svg",
    alt: "Flujograma: Puérpera con preeclampsia severa en tratamiento con sulfato de magnesio: se mantiene hasta 24 horas después del parto"
  },
  "NEU-061": {
    titulo: "Paciente con un mes de tratamiento antituberculoso que presenta fiebre, escalofríos y mialgias: síndrome seudogripal por rifampicina",
    imagen: "flujogramas/tratamiento-tb-fiebre-escalofrios-mialgia-rifampicina.svg",
    alt: "Flujograma: Paciente con un mes de tratamiento antituberculoso que presenta fiebre, escalofríos y mialgias: síndrome seudogripal por rifampicina"
  },
  "PED-200": {
    titulo: "Lactante de 2 meses con bronquiolitis (congestión, tos, sibilantes) y aleteo nasal con tiraje: hospitalizar para monitoreo e hidratación",
    imagen: "flujogramas/lactante-2-meses-bronquiolitis-tirajes-hospitalizar.svg",
    alt: "Flujograma: Lactante de 2 meses con bronquiolitis (congestión, tos, sibilantes) y aleteo nasal con tiraje: hospitalizar para monitoreo e hidratación"
  },
  "END-060": {
    titulo: "Adulto con poco sol, dolores óseos, debilidad proximal, calcio y fósforo bajos, fosfatasa alcalina y PTH altas: osteomalacia por déficit de vitamina D",
    imagen: "flujogramas/trabajo-uci-sin-sol-calcio-fosforo-bajos-fa-alta-vitamina-d.svg",
    alt: "Flujograma: Adulto con poco sol, dolores óseos, debilidad proximal, calcio y fósforo bajos, fosfatasa alcalina y PTH altas: osteomalacia por déficit de vitamina D"
  },
  "NEU-062": {
    titulo: "Mujer con neumonía, FR 28 y confusión (CURB-65 ≥ 1 con confusión): hospitalizar y tratar con ceftriaxona + azitromicina",
    imagen: "flujogramas/neumonia-confusa-fr-28-ceftriaxona-azitromicina.svg",
    alt: "Flujograma: Mujer con neumonía, FR 28 y confusión (CURB-65 ≥ 1 con confusión): hospitalizar y tratar con ceftriaxona + azitromicina"
  },
  "CIR-109": {
    titulo: "Paciente a las 24 horas de una colecistectomía con fiebre, hipotensión, taquicardia y abdomen con contractura y rebote: peritonitis biliar (fuga biliar)",
    imagen: "flujogramas/colecistectomia-24-h-fiebre-rebote-peritonitis-biliar.svg",
    alt: "Flujograma: Paciente a las 24 horas de una colecistectomía con fiebre, hipotensión, taquicardia y abdomen con contractura y rebote: peritonitis biliar (fuga biliar)"
  },
  "PED-201": {
    titulo: "Niño de 7 años con dolor periumbilical que migra a fosa ilíaca derecha, fiebre, vómitos, rebote y leucocitosis: apendicitis aguda",
    imagen: "flujogramas/nino-7-anos-dolor-migra-fid-rebote-leucocitosis-apendicitis.svg",
    alt: "Flujograma: Niño de 7 años con dolor periumbilical que migra a fosa ilíaca derecha, fiebre, vómitos, rebote y leucocitosis: apendicitis aguda"
  },
  "CIR-110": {
    titulo: "Explosión en la cocina con voz ronca, esputo carbonáceo, vellos nasales quemados, edema de orofaringe y dificultad respiratoria: lesión por inhalación, intubación temprana",
    imagen: "flujogramas/explosion-cocina-voz-ronca-esputo-carbonaceo-intubacion.svg",
    alt: "Flujograma: Explosión en la cocina con voz ronca, esputo carbonáceo, vellos nasales quemados, edema de orofaringe y dificultad respiratoria: lesión por inhalación, intubación temprana"
  },
  "GIN-212": {
    titulo: "Gestante a término con conjugado diagonal de 10,5 cm y diámetro biisquiático de 8 cm: pelvis estrecha (superior e inferior), cesárea",
    imagen: "flujogramas/pelvimetria-conjugado-10-5-pelvis-estrecha-cesarea.svg",
    alt: "Flujograma: Gestante a término con conjugado diagonal de 10,5 cm y diámetro biisquiático de 8 cm: pelvis estrecha (superior e inferior), cesárea"
  },
  "PSI-040": {
    titulo: "Niño con tristeza cuyo padre lo culpa, humilla e insulta constantemente: maltrato psicológico, informar a la autoridad competente",
    imagen: "flujogramas/nino-humillado-insultado-por-padre-comunicar-autoridad.svg",
    alt: "Flujograma: Niño con tristeza cuyo padre lo culpa, humilla e insulta constantemente: maltrato psicológico, informar a la autoridad competente"
  },
  "NEF-082": {
    titulo: "Joven con cólico renal y hematuria que luego tiene dolor suprapúbico, oliguria, masa en hipogastrio (globo vesical), creatinina 2,8 y K 5,6: lesión renal aguda posrenal",
    imagen: "flujogramas/colico-renal-previo-globo-vesical-oliguria-posrenal.svg",
    alt: "Flujograma: Joven con cólico renal y hematuria que luego tiene dolor suprapúbico, oliguria, masa en hipogastrio (globo vesical), creatinina 2,8 y K 5,6: lesión renal aguda posrenal"
  },
  "REU-061": {
    titulo: "Mujer con debilidad proximal progresiva, pápulas de Gottron, dolor muscular y CPK de 34 000: dermatomiositis, la biopsia muscular confirma",
    imagen: "flujogramas/debilidad-proximal-gottron-cpk-34000-biopsia-muscular.svg",
    alt: "Flujograma: Mujer con debilidad proximal progresiva, pápulas de Gottron, dolor muscular y CPK de 34 000: dermatomiositis, la biopsia muscular confirma"
  },
  "CIR-111": {
    titulo: "Conductor con trauma abdominal cerrado, hipotensión, taquicardia, peritonitis y signo de Jobert (neumoperitoneo): laparotomía exploradora",
    imagen: "flujogramas/trauma-cerrado-hipotension-jobert-peritonitis-laparotomia.svg",
    alt: "Flujograma: Conductor con trauma abdominal cerrado, hipotensión, taquicardia, peritonitis y signo de Jobert (neumoperitoneo): laparotomía exploradora"
  },
  "OFT-048": {
    titulo: "Prematura de 32 semanas con ventilación y oxígeno: el primer examen de retinopatía del prematuro se hace a las 4 semanas de vida (o a las 31 semanas posmenstruales)",
    imagen: "flujogramas/prematura-32-semanas-oxigeno-retinopatia-primer-examen-4-semanas.svg",
    alt: "Flujograma: Prematura de 32 semanas con ventilación y oxígeno: el primer examen de retinopatía del prematuro se hace a las 4 semanas de vida (o a las 31 semanas posmenstruales)"
  },
  "PED-202": {
    titulo: "Niño acianótico y eutrófico con segundo ruido desdoblado y fijo: comunicación interauricular",
    imagen: "flujogramas/nino-4-anos-acianotico-segundo-ruido-desdoblado-fijo-cia.svg",
    alt: "Flujograma: Niño acianótico y eutrófico con segundo ruido desdoblado y fijo: comunicación interauricular"
  },
  "GIN-213": {
    titulo: "Gestante con 42 semanas por FUR pero 38 por ecografía del primer trimestre: manda la ecografía (38 semanas), continuar el control prenatal",
    imagen: "flujogramas/fur-42-eco-temprana-38-continuar-control-prenatal.svg",
    alt: "Flujograma: Gestante con 42 semanas por FUR pero 38 por ecografía del primer trimestre: manda la ecografía (38 semanas), continuar el control prenatal"
  },
  "SP-156": {
    titulo: "Nuevo director con más presupuesto para los problemas sanitarios: la primera etapa de la planificación es elaborar el diagnóstico",
    imagen: "flujogramas/nuevo-director-presupuesto-planificacion-diagnostico.svg",
    alt: "Flujograma: Nuevo director con más presupuesto para los problemas sanitarios: la primera etapa de la planificación es elaborar el diagnóstico"
  },
  "SP-157": {
    titulo: "Aumento de la muerte materna en adolescentes de 13 a 17 años: para reducir el embarazo adolescente se prioriza la educación en salud sexual y reproductiva en los colegios",
    imagen: "flujogramas/muerte-materna-adolescentes-educacion-sexual-colegios.svg",
    alt: "Flujograma: Aumento de la muerte materna en adolescentes de 13 a 17 años: para reducir el embarazo adolescente se prioriza la educación en salud sexual y reproductiva en los colegios"
  },
  "PED-203": {
    titulo: "Niño de 3 años con resfrío, fiebre, tos productiva y roncantes difusos sin taquipnea ni crepitantes: bronquitis aguda",
    imagen: "flujogramas/preescolar-tos-productiva-roncantes-bronquitis-aguda.svg",
    alt: "Flujograma: Niño de 3 años con resfrío, fiebre, tos productiva y roncantes difusos sin taquipnea ni crepitantes: bronquitis aguda"
  },
  "NEF-083": {
    titulo: "Mujer delgada con debilidad, calambres, hipotensión, ROT disminuidos y ondas U con T aplanada: hipopotasemia por mal uso de laxantes (polietilenglicol)",
    imagen: "flujogramas/mujer-baja-peso-debilidad-onda-u-laxantes-hipokalemia.svg",
    alt: "Flujograma: Mujer delgada con debilidad, calambres, hipotensión, ROT disminuidos y ondas U con T aplanada: hipopotasemia por mal uso de laxantes (polietilenglicol)"
  },
  "GIN-214": {
    titulo: "En la gestante no se indica la vacuna contra el sarampión porque es de virus vivos atenuados",
    imagen: "flujogramas/gestante-20-semanas-vacuna-sarampion-contraindicada.svg",
    alt: "Flujograma: En la gestante no se indica la vacuna contra el sarampión porque es de virus vivos atenuados"
  },
  "OFT-049": {
    titulo: "Niño con quemadura ocular por lejía (álcali) y queratitis: lo primero es la irrigación abundante con suero fisiológico",
    imagen: "flujogramas/nino-lejia-ojo-queratitis-irrigacion-abundante.svg",
    alt: "Flujograma: Niño con quemadura ocular por lejía (álcali) y queratitis: lo primero es la irrigación abundante con suero fisiológico"
  },
  "GAS-067": {
    titulo: "Enfermera con hepatitis C (anti-VHC y ARN positivos): la gravedad de la enfermedad hepática se identifica con el estudio histológico (inflamación y fibrosis)",
    imagen: "flujogramas/enfermera-pinchazo-vhc-arn-positivo-histologia-severidad.svg",
    alt: "Flujograma: Enfermera con hepatitis C (anti-VHC y ARN positivos): la gravedad de la enfermedad hepática se identifica con el estudio histológico (inflamación y fibrosis)"
  },
  "PED-204": {
    titulo: "Neonato a término con abdomen excavado que empeora con la ventilación a presión positiva: hernia diafragmática congénita, intubación endotraqueal inmediata",
    imagen: "flujogramas/neonato-abdomen-excavado-empeora-con-ambu-intubar.svg",
    alt: "Flujograma: Neonato a término con abdomen excavado que empeora con la ventilación a presión positiva: hernia diafragmática congénita, intubación endotraqueal inmediata"
  },
  "SP-158": {
    titulo: "Profesionales recién incorporados a un hospital: la actividad prioritaria es capacitarlos en el control de infecciones respiratorias por tuberculosis",
    imagen: "flujogramas/personal-nuevo-hospital-capacitacion-control-infeccion-tb.svg",
    alt: "Flujograma: Profesionales recién incorporados a un hospital: la actividad prioritaria es capacitarlos en el control de infecciones respiratorias por tuberculosis"
  },
  "GIN-215": {
    titulo: "Gestante de 24 semanas con pielonefritis hace 15 días y urocultivo actual negativo: urocultivo mensual hasta el final del embarazo",
    imagen: "flujogramas/gestante-pielonefritis-previa-urocultivo-negativo-mensual.svg",
    alt: "Flujograma: Gestante de 24 semanas con pielonefritis hace 15 días y urocultivo actual negativo: urocultivo mensual hasta el final del embarazo"
  },
  "PED-205": {
    titulo: "Prematuro de 28 semanas con enfermedad de membrana hialina: la hipovolemia inhibe la síntesis de surfactante",
    imagen: "flujogramas/prematuro-membrana-hialina-hipovolemia-inhibe-surfactante.svg",
    alt: "Flujograma: Prematuro de 28 semanas con enfermedad de membrana hialina: la hipovolemia inhibe la síntesis de surfactante"
  },
  "CIR-112": {
    titulo: "Accidente con fracturas costales derechas, MV abolido y Rx con opacidad de 2/3 del hemitórax derecho: hemotórax, drenaje pleural",
    imagen: "flujogramas/trauma-toracico-fracturas-costales-radiopacidad-hemotorax-drenaje.svg",
    alt: "Flujograma: Accidente con fracturas costales derechas, MV abolido y Rx con opacidad de 2/3 del hemitórax derecho: hemotórax, drenaje pleural"
  },
  "GIN-216": {
    titulo: "Puérpera por cesárea con VIH diagnosticado en esta gestación (escenario 3): suprimir la lactancia con cabergolina y vendaje de mamas inmediatamente",
    imagen: "flujogramas/vih-escenario-3-cesarea-suprimir-lactancia-cabergolina.svg",
    alt: "Flujograma: Puérpera por cesárea con VIH diagnosticado en esta gestación (escenario 3): suprimir la lactancia con cabergolina y vendaje de mamas inmediatamente"
  },
  "NEU-063": {
    titulo: "Fiebre, tos y disnea de 6 días con crepitantes y opacidad en el hemitórax izquierdo: neumonía adquirida en la comunidad",
    imagen: "flujogramas/fiebre-tos-disnea-crepitantes-opacidad-neumonia.svg",
    alt: "Flujograma: Fiebre, tos y disnea de 6 días con crepitantes y opacidad en el hemitórax izquierdo: neumonía adquirida en la comunidad"
  },
  "PED-206": {
    titulo: "Lactante de 7 meses con deshidratación grave por diarrea, después de tratar el shock: Lactato de Ringer 30 mL/kg en 1 hora y 70 mL/kg en 5 horas",
    imagen: "flujogramas/lactante-7-meses-deshidratacion-grave-plan-c-30-70.svg",
    alt: "Flujograma: Lactante de 7 meses con deshidratación grave por diarrea, después de tratar el shock: Lactato de Ringer 30 mL/kg en 1 hora y 70 mL/kg en 5 horas"
  },
  "GIN-217": {
    titulo: "Ecografía con embrión de 8 mm sin latido y saco de 29 mm: pérdida gestacional temprana (aborto retenido), tratamiento con misoprostol",
    imagen: "flujogramas/saco-29-mm-embrion-8-mm-sin-latido-misoprostol.svg",
    alt: "Flujograma: Ecografía con embrión de 8 mm sin latido y saco de 29 mm: pérdida gestacional temprana (aborto retenido), tratamiento con misoprostol"
  },
  "CIR-113": {
    titulo: "Joven con dolor en HCD de 48 h, Murphy positivo, leucocitosis y eco con pared gruesa y cálculo en el bacinete: colecistitis aguda, colecistectomía laparoscópica",
    imagen: "flujogramas/murphy-positivo-calculo-bacinete-colecistectomia-laparoscopica.svg",
    alt: "Flujograma: Joven con dolor en HCD de 48 h, Murphy positivo, leucocitosis y eco con pared gruesa y cálculo en el bacinete: colecistitis aguda, colecistectomía laparoscópica"
  },
  "TRA-046": {
    titulo: "Joven con caída sobre la mano, dolor, impotencia funcional y signo de la charretera: luxación anterior de hombro, reducción cerrada por tracción",
    imagen: "flujogramas/caida-mano-extendida-signo-charretera-luxacion-hombro.svg",
    alt: "Flujograma: Joven con caída sobre la mano, dolor, impotencia funcional y signo de la charretera: luxación anterior de hombro, reducción cerrada por tracción"
  },
  "CAR-067": {
    titulo: "Paciente en paro sin pulso: las compresiones de calidad son de al menos 5 cm (sin pasar de 6) y a 100-120 por minuto",
    imagen: "flujogramas/rcp-calidad-5-cm-100-120-por-minuto.svg",
    alt: "Flujograma: Paciente en paro sin pulso: las compresiones de calidad son de al menos 5 cm (sin pasar de 6) y a 100-120 por minuto"
  },
  "GIN-218": {
    titulo: "Dilatación completa, presentación en +3 y occipucio ya anterior: la rotación interna ocurrió y el siguiente movimiento cardinal es la extensión",
    imagen: "flujogramas/dilatacion-completa-occipitoanterior-siguiente-extension.svg",
    alt: "Flujograma: Dilatación completa, presentación en +3 y occipucio ya anterior: la rotación interna ocurrió y el siguiente movimiento cardinal es la extensión"
  },
  "NRL-053": {
    titulo: "Caída de un 4.º piso: abre los ojos al dolor (2), sonidos incomprensibles (2) y flexión anormal (3): Glasgow 7, TEC grave",
    imagen: "flujogramas/caida-4-piso-abre-ojos-dolor-flexion-sonidos-glasgow-7.svg",
    alt: "Flujograma: Caída de un 4.º piso: abre los ojos al dolor (2), sonidos incomprensibles (2) y flexión anormal (3): Glasgow 7, TEC grave"
  },
  "SP-159": {
    titulo: "Médico no especialista que en una cesárea electiva perfora la vejiga: mala praxis por impericia",
    imagen: "flujogramas/cesarea-medico-no-especialista-perfora-vejiga-impericia.svg",
    alt: "Flujograma: Médico no especialista que en una cesárea electiva perfora la vejiga: mala praxis por impericia"
  },
  "CB-076": {
    titulo: "Maratonista en ejercicio aeróbico prolongado: en el hígado se activa la gluconeogénesis cuando se agota el glucógeno",
    imagen: "flujogramas/maratonista-ejercicio-prolongado-gluconeogenesis-hepatica.svg",
    alt: "Flujograma: Maratonista en ejercicio aeróbico prolongado: en el hígado se activa la gluconeogénesis cuando se agota el glucógeno"
  },
  "TRA-047": {
    titulo: "Politraumatizado con sangrado activo en las piernas: la primera alteración fisiológica de la hemorragia es el aumento de la frecuencia cardiaca",
    imagen: "flujogramas/hemorragia-activa-primer-signo-taquicardia.svg",
    alt: "Flujograma: Politraumatizado con sangrado activo en las piernas: la primera alteración fisiológica de la hemorragia es el aumento de la frecuencia cardiaca"
  },
  "PED-207": {
    titulo: "Lactante de 2 meses con VIH recién diagnosticado: iniciar terapia antirretroviral de inmediato, sin esperar síntomas ni CD4",
    imagen: "flujogramas/lactante-2-meses-vih-iniciar-tar-precoz.svg",
    alt: "Flujograma: Lactante de 2 meses con VIH recién diagnosticado: iniciar terapia antirretroviral de inmediato, sin esperar síntomas ni CD4"
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
  },
  "CIR-133": { titulo: "Quemadura del 30 %: cálculo de Parkland paso a paso", imagen: "flujogramas/quemado-parkland-regla-de-los-nueve.svg", alt: "Flujograma: Quemadura del 30 %: cálculo de Parkland paso a paso" },
  "CIR-158": { titulo: "Hernia obturatriz: dónde sale cada hernia de la ingle", imagen: "flujogramas/hernia-obturatriz-mapa-pelvico-howship-romberg.svg", alt: "Flujograma: Hernia obturatriz: dónde sale cada hernia de la ingle" },
  "CIR-150": { titulo: "Vólvulo de sigmoides: el semáforo de la isquemia decide la conducta", imagen: "flujogramas/volvulo-sigmoides-semaforo-devolvulacion.svg", alt: "Flujograma: Vólvulo de sigmoides: el semáforo de la isquemia decide la conducta" },
  "GIN-274": { titulo: "Translucencia nucal aumentada: qué detecta cada prueba prenatal", imagen: "flujogramas/translucencia-nucal-cronologia-tamizaje-prenatal.svg", alt: "Flujograma: Translucencia nucal aumentada: qué detecta cada prueba prenatal" },
  "CIR-136": { titulo: "Neumotórax traumático derecho: de la Rx al tubo de tórax", imagen: "flujogramas/neumotorax-traumatico-rx-antes-despues-toracostomia.svg", alt: "Flujograma: Neumotórax traumático derecho: de la Rx al tubo de tórax" },
  "CAR-079": { titulo: "TSV con inestabilidad: salto directo a la cardioversión sincronizada", imagen: "flujogramas/taquicardia-supraventricular-inestable-ecg-escalera-cardioversion.svg", alt: "Flujograma: TSV con inestabilidad: salto directo a la cardioversión sincronizada" },
  "PED-247": { titulo: "Sarampión: los signos en orden y dónde aparecen", imagen: "flujogramas/sarampion-mapa-corporal-exantema-cefalocaudal-koplik.svg", alt: "Flujograma: Sarampión: los signos en orden y dónde aparecen" },
  "TRA-057": { titulo: "Displasia de cadera a los 9 meses: la Rx de pelvis y cómo leerla", imagen: "flujogramas/displasia-cadera-lactante-9-meses-rx-pelvis-hilgenreiner-perkins.svg", alt: "Flujograma: Displasia de cadera a los 9 meses: la Rx de pelvis y cómo leerla" },
  "SP-193": { titulo: "Ciclo de políticas de la OPS: evaluar, formular, asignar recursos y dar acceso", imagen: "flujogramas/funciones-esenciales-salud-publica-ciclo-politicas-anemia-infantil.svg", alt: "Flujograma: Ciclo de políticas de la OPS: evaluar, formular, asignar recursos y dar acceso" },
  "PED-242": { titulo: "Tamizaje de cardiopatía congénita crítica en la altura: zona intermedia, repetir en 1 hora", imagen: "flujogramas/tamizaje-cardiopatia-critica-altura-la-oroya-repetir-oximetria.svg", alt: "Flujograma: Tamizaje de cardiopatía congénita crítica en la altura: zona intermedia, repetir en 1 hora" },
  "CIR-125": { titulo: "Íleo biliar: la tríada de Rigler en la Rx y la TC", imagen: "flujogramas/ileo-biliar-triada-rigler-rx-tc-enterolitotomia.svg", alt: "Flujograma: Íleo biliar: la tríada de Rigler en la Rx y la TC" },
  "PED-243": { titulo: "Lactante con riesgo y sin tamizaje auditivo: referir para otoemisiones o potenciales", imagen: "flujogramas/lactante-2-meses-sifilis-materna-sin-tamizaje-auditivo-otoemisiones.svg", alt: "Flujograma: Lactante con riesgo y sin tamizaje auditivo: referir para otoemisiones o potenciales" },
  "CB-486": { titulo: "Víctima de incendio en coma que no mejora con oxígeno al 100 %: cianuro, hidroxocobalamina", imagen: "flujogramas/incendio-cerrado-coma-sin-mejoria-oxigeno-cianuro-hidroxocobalamina.svg", alt: "Flujograma: Víctima de incendio en coma que no mejora con oxígeno al 100 %: cianuro, hidroxocobalamina" },
  "OFT-056": { titulo: "Otitis media aguda en un niño de 2 años: el abombamiento del tímpano justifica el antibiótico", imagen: "flujogramas/nino-2-anos-otitis-media-aguda-timpano-abombado-antibiotico.svg", alt: "Flujograma: Otitis media aguda en un niño de 2 años: el abombamiento del tímpano justifica el antibiótico" },
  "NEF-094": { titulo: "Criptorquidia operada en la infancia: el riesgo de cáncer testicular sigue siendo mayor", imagen: "flujogramas/criptorquidia-orquidopexia-5-anos-riesgo-cancer-testicular-autoexamen.svg", alt: "Flujograma: Criptorquidia operada en la infancia: el riesgo de cáncer testicular sigue siendo mayor" },
  "PED-244": { titulo: "Quejido y crepitantes finos difusos: compromiso alveolointersticial", imagen: "flujogramas/lactante-quejido-crepitantes-finos-compromiso-alveolointersticial.svg", alt: "Flujograma: Quejido y crepitantes finos difusos: compromiso alveolointersticial" },
  "CIR-126": { titulo: "Herida abdominal por arma blanca con evisceración: laparotomía", imagen: "flujogramas/herida-arma-blanca-evisceracion-epiplon-laparotomia.svg", alt: "Flujograma: Herida abdominal por arma blanca con evisceración: laparotomía" },
  "CIR-127": { titulo: "Quemadura de 2.º grado en manos en un adulto mayor: primeros cuidados y referencia", imagen: "flujogramas/quemadura-segundo-grado-manos-adulto-mayor-lavar-referir.svg", alt: "Flujograma: Quemadura de 2.º grado en manos en un adulto mayor: primeros cuidados y referencia" },
  "CB-487": { titulo: "Estatina más fibrato: aumenta el riesgo de miopatía y rabdomiólisis", imagen: "flujogramas/dislipidemia-mixta-estatina-mas-fibrato-riesgo-rabdomiolisis.svg", alt: "Flujograma: Estatina más fibrato: aumenta el riesgo de miopatía y rabdomiólisis" },
  "INF-115": { titulo: "Diarrea con moco y sangre, fiebre y más de 100 leucocitos por campo: Shigella", imagen: "flujogramas/disenteria-fiebre-leucocitos-mas-100-campo-shigella.svg", alt: "Flujograma: Diarrea con moco y sangre, fiebre y más de 100 leucocitos por campo: Shigella" },
  "GIN-248": { titulo: "Prurito en palmas y plantas a las 34 semanas: colestasis intrahepática gestacional", imagen: "flujogramas/prurito-palmoplantar-nocturno-34-semanas-colestasis-intrahepatica.svg", alt: "Flujograma: Prurito en palmas y plantas a las 34 semanas: colestasis intrahepática gestacional" },
  "SP-194": { titulo: "Datos muy asimétricos: la mediana describe mejor el valor típico", imagen: "flujogramas/tasas-mortalidad-covid-asimetricas-mediana-tendencia-central.svg", alt: "Flujograma: Datos muy asimétricos: la mediana describe mejor el valor típico" },
  "PSI-043": { titulo: "Síntomas neurológicos sin causa orgánica tras un duelo: trastorno de conversión", imagen: "flujogramas/perdida-gestacional-debilidad-disfagia-examenes-normales-trastorno-conversion.svg", alt: "Flujograma: Síntomas neurológicos sin causa orgánica tras un duelo: trastorno de conversión" },
  "PED-245": { titulo: "Raquitismo carencial: sin calcitriol no se absorbe calcio ni fósforo", imagen: "flujogramas/raquitismo-carencial-deficit-calcitriol-mineralizacion-osea.svg", alt: "Flujograma: Raquitismo carencial: sin calcitriol no se absorbe calcio ni fósforo" },
  "GIN-249": { titulo: "Corticoides prenatales en RPM de 32 semanas: menos membrana hialina", imagen: "flujogramas/rpm-32-semanas-corticoides-prenatales-membrana-hialina.svg", alt: "Flujograma: Corticoides prenatales en RPM de 32 semanas: menos membrana hialina" },
  "SP-195": { titulo: "Foto de un paciente publicada en redes sin su permiso: violación de la confidencialidad", imagen: "flujogramas/estudiante-publica-foto-paciente-redes-sociales-violacion-confidencialidad.svg", alt: "Flujograma: Foto de un paciente publicada en redes sin su permiso: violación de la confidencialidad" },
  "PED-246": { titulo: "Escala de Bierman y Pierson: este lactante suma 8 (moderada)", imagen: "flujogramas/escala-bierman-pierson-8-puntos-obstruccion-bronquial-moderada.svg", alt: "Flujograma: Escala de Bierman y Pierson: este lactante suma 8 (moderada)" },
  "GIN-250": { titulo: "Mastitis que no mejora y masa fluctuante: absceso mamario, drenaje", imagen: "flujogramas/mastitis-puerperal-sin-mejoria-absceso-5-cm-drenaje.svg", alt: "Flujograma: Mastitis que no mejora y masa fluctuante: absceso mamario, drenaje" },
  "CAR-075": { titulo: "Pierna hinchada, roja y dolorosa de inicio súbito hasta el muslo: trombosis venosa profunda", imagen: "flujogramas/pierna-derecha-hinchada-hasta-muslo-dolor-pantorrilla-trombosis-venosa-profunda.svg", alt: "Flujograma: Pierna hinchada, roja y dolorosa de inicio súbito hasta el muslo: trombosis venosa profunda" },
  "REU-069": { titulo: "Máculas blanco tiza en cara, manos y genitales con hipotiroidismo autoinmune: vitíligo", imagen: "flujogramas/maculas-acromicas-blanco-tiza-cara-manos-hipotiroidismo-autoinmune-vitiligo.svg", alt: "Flujograma: Máculas blanco tiza en cara, manos y genitales con hipotiroidismo autoinmune: vitíligo" },
  "NEF-095": { titulo: "Trauma lumbar con hematuria macroscópica en paciente estable: TC con contraste", imagen: "flujogramas/atropello-dolor-flanco-hematuria-macroscopica-estable-tc-contraste.svg", alt: "Flujograma: Trauma lumbar con hematuria macroscópica en paciente estable: TC con contraste" },
  "REU-070": { titulo: "Piel endurecida en manos y cara con esófago distal dilatado y sin peristalsis: esclerodermia", imagen: "flujogramas/piel-dura-manos-cara-disfagia-esofago-sin-peristalsis-esclerodermia.svg", alt: "Flujograma: Piel endurecida en manos y cara con esófago distal dilatado y sin peristalsis: esclerodermia" },
  "CIR-128": { titulo: "Fisura anal crónica: por qué la esfinterotomía lateral interna", imagen: "flujogramas/fisura-anal-cronica-hipertonia-esfinterotomia-lateral-interna.svg", alt: "Flujograma: Fisura anal crónica: por qué la esfinterotomía lateral interna" },
  "TRA-054": { titulo: "Corte palmar con lesión del flexor profundo en el primer nivel: limpiar, cubrir y derivar", imagen: "flujogramas/corte-palmar-indice-flexor-profundo-limpiar-derivar-cirugia-mano.svg", alt: "Flujograma: Corte palmar con lesión del flexor profundo en el primer nivel: limpiar, cubrir y derivar" },
  "SP-196": { titulo: "Profesor con hepatitis B aguda muy replicativa: tamizar y vacunar a los contactos no inmunizados, con confidencialidad", imagen: "flujogramas/profesor-rural-hepatitis-b-aguda-hbeag-tamizaje-vacunacion-contactos.svg", alt: "Flujograma: Profesor con hepatitis B aguda muy replicativa: tamizar y vacunar a los contactos no inmunizados, con confidencialidad" },
  "CIR-129": { titulo: "Diverticulitis no complicada: cuándo se trata en casa", imagen: "flujogramas/diverticulitis-sigmoidea-no-complicada-manejo-ambulatorio.svg", alt: "Flujograma: Diverticulitis no complicada: cuándo se trata en casa" },
  "CAR-076": { titulo: "Mujer mayor hipertensa con ortopnea, crepitantes y proBNP alto: insuficiencia cardiaca con FEVI preservada", imagen: "flujogramas/mujer-hipertensa-ortopnea-crepitantes-probnp-alto-ic-fevi-preservada.svg", alt: "Flujograma: Mujer mayor hipertensa con ortopnea, crepitantes y proBNP alto: insuficiencia cardiaca con FEVI preservada" },
  "SP-197": { titulo: "Instrumento que define las prestaciones según oferta y demanda: programa médico funcional", imagen: "flujogramas/planificacion-establecimiento-oferta-demanda-programa-medico-funcional.svg", alt: "Flujograma: Instrumento que define las prestaciones según oferta y demanda: programa médico funcional" },
  "NRL-062": { titulo: "Caída de un árbol con Glasgow 9 en un centro sin TC: asegurar la vía aérea y referir", imagen: "flujogramas/caida-arbol-glasgow-9-tec-moderado-sin-tc-via-aerea-referir.svg", alt: "Flujograma: Caída de un árbol con Glasgow 9 en un centro sin TC: asegurar la vía aérea y referir" },
  "REU-071": { titulo: "Ampollas con Nikolsky positivo y mucosas erosionadas en < 10 % de la superficie tras carbamazepina: Stevens-Johnson", imagen: "flujogramas/carbamazepina-ampollas-nikolsky-mucosas-menos-10-stevens-johnson.svg", alt: "Flujograma: Ampollas con Nikolsky positivo y mucosas erosionadas en < 10 % de la superficie tras carbamazepina: Stevens-Johnson" },
  "GIN-251": { titulo: "Sangrado intermenstrual con endometrio de 18 mm: biopsia endometrial", imagen: "flujogramas/sangrado-intermenstrual-endometrio-18-mm-biopsia-endometrial.svg", alt: "Flujograma: Sangrado intermenstrual con endometrio de 18 mm: biopsia endometrial" },
  "GIN-252": { titulo: "Eclampsia a las 35 semanas: estabilizar y terminar la gestación", imagen: "flujogramas/eclampsia-35-semanas-sulfato-magnesio-culminar-gestacion.svg", alt: "Flujograma: Eclampsia a las 35 semanas: estabilizar y terminar la gestación" },
  "SP-198": { titulo: "¿Se pueden aplicar los resultados a otros hospitales y regiones? Validez externa", imagen: "flujogramas/cohorte-hospital-lima-generalizar-resultados-validez-externa.svg", alt: "Flujograma: ¿Se pueden aplicar los resultados a otros hospitales y regiones? Validez externa" },
  "GAS-079": { titulo: "Pancreatitis aguda: la hipotensión que no responde a líquidos marca el mal pronóstico", imagen: "flujogramas/pancreatitis-aguda-hipotension-persistente-falla-organica-pronostico.svg", alt: "Flujograma: Pancreatitis aguda: la hipotensión que no responde a líquidos marca el mal pronóstico" },
  "NEF-096": { titulo: "Dolor cólico del flanco que baja al muslo con hematuria microscópica: litiasis ureteral", imagen: "flujogramas/dolor-colico-flanco-irradiado-muslo-hematuria-litiasis-ureteral.svg", alt: "Flujograma: Dolor cólico del flanco que baja al muslo con hematuria microscópica: litiasis ureteral" },
  "GIN-253": { titulo: "Masa anexial de 8 cm con dolor cólico y β-hCG negativa: torsión anexial", imagen: "flujogramas/masa-anexial-8-cm-dolor-colico-bhcg-negativa-torsion.svg", alt: "Flujograma: Masa anexial de 8 cm con dolor cólico y β-hCG negativa: torsión anexial" },
  "GIN-254": { titulo: "Defecto paravaginal: se desinserta el arco tendinoso de la fascia pélvica", imagen: "flujogramas/cistocele-defecto-paravaginal-arco-tendinoso-fascia-pelvica.svg", alt: "Flujograma: Defecto paravaginal: se desinserta el arco tendinoso de la fascia pélvica" },
  "INF-116": { titulo: "Fiebre y dolor en hipocondrio derecho tras una disentería: absceso hepático amebiano", imagen: "flujogramas/fiebre-dolor-hipocondrio-derecho-disenteria-previa-absceso-hepatico-amebiano.svg", alt: "Flujograma: Fiebre y dolor en hipocondrio derecho tras una disentería: absceso hepático amebiano" },
  "NEF-097": { titulo: "Varón de 55 años que pide «todos los exámenes» de próstata: decisión compartida", imagen: "flujogramas/varon-55-anos-padre-cancer-prostata-decision-compartida-psa.svg", alt: "Flujograma: Varón de 55 años que pide «todos los exámenes» de próstata: decisión compartida" },
  "INF-117": { titulo: "Pápulas umbilicadas múltiples en una mujer con VIH: molusco contagioso, crioterapia y reforzar el TAR", imagen: "flujogramas/mujer-vih-papulas-umbilicadas-vulva-muslos-molusco-crioterapia-tar.svg", alt: "Flujograma: Pápulas umbilicadas múltiples en una mujer con VIH: molusco contagioso, crioterapia y reforzar el TAR" },
  "PED-248": { titulo: "Sepsis neonatal precoz con RPM > 18 h: estreptococo del grupo B", imagen: "flujogramas/sepsis-neonatal-precoz-rpm-20-horas-estreptococo-grupo-b.svg", alt: "Flujograma: Sepsis neonatal precoz con RPM > 18 h: estreptococo del grupo B" },
  "NRL-063": { titulo: "Debilidad simétrica ascendente con arreflexia tras una diarrea: síndrome de Guillain-Barré", imagen: "flujogramas/debilidad-ascendente-arreflexia-diarrea-previa-guillain-barre.svg", alt: "Flujograma: Debilidad simétrica ascendente con arreflexia tras una diarrea: síndrome de Guillain-Barré" },
  "SP-199": { titulo: "Desde la exposición hasta que la persona puede transmitir: período de latencia", imagen: "flujogramas/dengue-tiempo-exposicion-hasta-poder-transmitir-periodo-latencia.svg", alt: "Flujograma: Desde la exposición hasta que la persona puede transmitir: período de latencia" },
  "CAR-077": { titulo: "Fibrilación ventricular que sigue tras la tercera descarga: amiodarona 300 mg EV", imagen: "flujogramas/fibrilacion-ventricular-tras-tercera-descarga-amiodarona-300-mg.svg", alt: "Flujograma: Fibrilación ventricular que sigue tras la tercera descarga: amiodarona 300 mg EV" },
  "CIR-130": { titulo: "Absceso apendicular: drenaje percutáneo más antibiótico", imagen: "flujogramas/absceso-apendicular-3-cm-drenaje-percutaneo-antibiotico.svg", alt: "Flujograma: Absceso apendicular: drenaje percutáneo más antibiótico" },
  "CB-488": { titulo: "Mordedura de araña con necrosis, ictericia e hipotensión: suero antiloxoscélico e hidratación EV", imagen: "flujogramas/mordedura-arana-30-horas-necrosis-ictericia-hipotension-suero-antiloxoscelico.svg", alt: "Flujograma: Mordedura de araña con necrosis, ictericia e hipotensión: suero antiloxoscélico e hidratación EV" },
  "CIR-131": { titulo: "Colecistitis aguda: colecistectomía laparoscópica temprana", imagen: "flujogramas/colecistitis-aguda-tokio-colecistectomia-temprana-72-horas.svg", alt: "Flujograma: Colecistitis aguda: colecistectomía laparoscópica temprana" },
  "CB-489": { titulo: "Dilatación de la aorta descendente: en el mediastino posterior, junto al esófago", imagen: "flujogramas/aorta-descendente-dilatada-mediastino-posterior-esofago.svg", alt: "Flujograma: Dilatación de la aorta descendente: en el mediastino posterior, junto al esófago" },
  "INF-118": { titulo: "EIA de 4.ª generación reactivo con prueba de diferenciación negativa: ARN de VIH (NAT)", imagen: "flujogramas/eia-cuarta-generacion-reactivo-diferenciacion-negativa-vih-agudo-nat.svg", alt: "Flujograma: EIA de 4.ª generación reactivo con prueba de diferenciación negativa: ARN de VIH (NAT)" },
  "NEF-098": { titulo: "Diabético de larga data con uremia y albuminuria alta: ERC por nefropatía diabética; buscar retinopatía", imagen: "flujogramas/diabetico-15-anos-creatinina-5-8-albuminuria-erc-retinopatia-diabetica.svg", alt: "Flujograma: Diabético de larga data con uremia y albuminuria alta: ERC por nefropatía diabética; buscar retinopatía" },
  "REU-072": { titulo: "Dolor mecánico en manos con nódulos interfalángicos, osteofitos y VSG normal: osteoartritis", imagen: "flujogramas/dolor-mecanico-manos-nodulos-interfalangicos-osteofitos-vsg-normal-osteoartritis.svg", alt: "Flujograma: Dolor mecánico en manos con nódulos interfalángicos, osteofitos y VSG normal: osteoartritis" },
  "SP-200": { titulo: "Cientos de pacientes en varios hospitales comparando con el tratamiento estándar: ensayo fase III", imagen: "flujogramas/farmaco-hipertension-cientos-pacientes-multicentrico-vs-estandar-fase-iii.svg", alt: "Flujograma: Cientos de pacientes en varios hospitales comparando con el tratamiento estándar: ensayo fase III" },
  "HEM-042": { titulo: "Drepanocitosis con dolor óseo intenso tras ejercicio: crisis vasooclusiva", imagen: "flujogramas/adolescente-drepanocitosis-dolor-oseo-tras-ejercicio-crisis-vasooclusiva.svg", alt: "Flujograma: Drepanocitosis con dolor óseo intenso tras ejercicio: crisis vasooclusiva" },
  "NRL-064": { titulo: "Hipertenso con deterioro cognitivo y síndrome pseudobulbar: infartos lacunares múltiples", imagen: "flujogramas/hipertenso-74-anos-sindrome-pseudobulbar-hachinski-infartos-lacunares.svg", alt: "Flujograma: Hipertenso con deterioro cognitivo y síndrome pseudobulbar: infartos lacunares múltiples" },
  "GIN-255": { titulo: "Desprendimiento prematuro de placenta grave: cesárea de emergencia", imagen: "flujogramas/desprendimiento-placenta-utero-hipertonico-coagulopatia-cesarea.svg", alt: "Flujograma: Desprendimiento prematuro de placenta grave: cesárea de emergencia" },
  "INF-119": { titulo: "Dengue con choque por fuga capilar: bolo rápido de cristaloides", imagen: "flujogramas/dengue-dia-5-pa-80-40-derrame-bilateral-choque-bolo-cristaloides.svg", alt: "Flujograma: Dengue con choque por fuga capilar: bolo rápido de cristaloides" },
  "PED-249": { titulo: "Sodio de 162 en lactante con tomas espaciadas: deshidratación por lactancia ineficaz", imagen: "flujogramas/lactante-sodio-162-tomas-espaciadas-lactancia-ineficaz.svg", alt: "Flujograma: Sodio de 162 en lactante con tomas espaciadas: deshidratación por lactancia ineficaz" },
  "GAS-080": { titulo: "Lesiones precursoras de cáncer gástrico: la displasia exige vigilar más de cerca", imagen: "flujogramas/gastritis-atrofica-metaplasia-displasia-bajo-grado-vigilancia.svg", alt: "Flujograma: Lesiones precursoras de cáncer gástrico: la displasia exige vigilar más de cerca" },
  "SP-201": { titulo: "Brote de dengue en la comunidad: la medida prioritaria es eliminar los criaderos de Aedes aegypti", imagen: "flujogramas/brote-dengue-selva-intervencion-comunitaria-eliminar-criaderos-aedes.svg", alt: "Flujograma: Brote de dengue en la comunidad: la medida prioritaria es eliminar los criaderos de Aedes aegypti" },
  "CB-490": { titulo: "Disfonía con parálisis de una cuerda vocal tras tiroidectomía: lesión del laríngeo recurrente", imagen: "flujogramas/disfonia-post-tiroidectomia-paralisis-cuerda-vocal-laringeo-recurrente.svg", alt: "Flujograma: Disfonía con parálisis de una cuerda vocal tras tiroidectomía: lesión del laríngeo recurrente" },
  "CB-491": { titulo: "Tras extraer un tercer molar: sin tacto en 2/3 anteriores de la lengua pero con gusto: nervio lingual", imagen: "flujogramas/extraccion-tercer-molar-perdida-sensibilidad-lengua-gusto-conservado-nervio-lingual.svg", alt: "Flujograma: Tras extraer un tercer molar: sin tacto en 2/3 anteriores de la lengua pero con gusto: nervio lingual" },
  "CAR-078": { titulo: "PA 150/50, pulsos saltones, Musset y Quincke con soplo diastólico: insuficiencia aórtica crónica", imagen: "flujogramas/pa-150-50-pulsos-saltones-musset-quincke-insuficiencia-aortica-reumatica.svg", alt: "Flujograma: PA 150/50, pulsos saltones, Musset y Quincke con soplo diastólico: insuficiencia aórtica crónica" },
  "CIR-132": { titulo: "Hernia estrangulada: cuándo el asa ya no es viable", imagen: "flujogramas/hernia-estrangulada-asa-negra-sin-pulso-reseccion-intestinal.svg", alt: "Flujograma: Hernia estrangulada: cuándo el asa ya no es viable" },
  "OFT-057": { titulo: "La quemadura química del ojo es una urgencia verdadera: lavar en minutos", imagen: "flujogramas/urgencias-oftalmologicas-quemadura-quimica-lavado-inmediato.svg", alt: "Flujograma: La quemadura química del ojo es una urgencia verdadera: lavar en minutos" },
  "TRA-055": { titulo: "Artritis reumatoide con dolor cervical y parestesias al flexionar: Rx dinámica en flexión y extensión", imagen: "flujogramas/artritis-reumatoide-dolor-cervical-parestesias-flexion-rx-dinamica-c1-c2.svg", alt: "Flujograma: Artritis reumatoide con dolor cervical y parestesias al flexionar: Rx dinámica en flexión y extensión" },
  "SP-202": { titulo: "TB bacilífera que rechaza el tratamiento y pide secreto: informar a la autoridad sanitaria", imagen: "flujogramas/tb-bacilifera-rechaza-tratamiento-convivientes-notificar-autoridad-sanitaria.svg", alt: "Flujograma: TB bacilífera que rechaza el tratamiento y pide secreto: informar a la autoridad sanitaria" },
  "PED-250": { titulo: "Vasculitis por IgA sin compromiso renal ni abdominal grave: reposo y AINE", imagen: "flujogramas/purpura-palpable-piernas-artritis-rodillas-vasculitis-iga-sintomatico.svg", alt: "Flujograma: Vasculitis por IgA sin compromiso renal ni abdominal grave: reposo y AINE" },
  "PED-251": { titulo: "Calcificaciones periventriculares con microcefalia: citomegalovirus congénito", imagen: "flujogramas/calcificaciones-periventriculares-microcefalia-citomegalovirus-congenito.svg", alt: "Flujograma: Calcificaciones periventriculares con microcefalia: citomegalovirus congénito" },
  "CIR-134": { titulo: "Adenocarcinoma sobre Barrett T1b: esofagectomía con linfadenectomía", imagen: "flujogramas/barrett-adenocarcinoma-t1b-submucosa-esofagectomia.svg", alt: "Flujograma: Adenocarcinoma sobre Barrett T1b: esofagectomía con linfadenectomía" },
  "REU-073": { titulo: "Dolor generalizado con fatiga, sueño no reparador y alodinia: fibromialgia, amitriptilina nocturna", imagen: "flujogramas/dolor-generalizado-fatiga-sueno-no-reparador-alodinia-fibromialgia-amitriptilina.svg", alt: "Flujograma: Dolor generalizado con fatiga, sueño no reparador y alodinia: fibromialgia, amitriptilina nocturna" },
  "INF-120": { titulo: "Úlceras genitales dolorosas, blandas, con ganglio inguinal doloroso: chancroide, azitromicina", imagen: "flujogramas/ulceras-genitales-dolorosas-base-blanda-adenitis-supurada-chancroide-azitromicina.svg", alt: "Flujograma: Úlceras genitales dolorosas, blandas, con ganglio inguinal doloroso: chancroide, azitromicina" },
  "SP-203": { titulo: "Eclampsia que termina en hemorragia intracerebral: la causa básica es la eclampsia", imagen: "flujogramas/eclampsia-muerte-por-hemorragia-intracerebral-causa-basica-muerte-materna.svg", alt: "Flujograma: Eclampsia que termina en hemorragia intracerebral: la causa básica es la eclampsia" },
  "NRL-065": { titulo: "Temblor postural bilateral que mejora con alcohol y es familiar: temblor esencial", imagen: "flujogramas/temblor-postural-bilateral-mejora-alcohol-familia-temblor-esencial.svg", alt: "Flujograma: Temblor postural bilateral que mejora con alcohol y es familiar: temblor esencial" },
  "CIR-135": { titulo: "Mallampati I: se espera una intubación fácil", imagen: "flujogramas/mallampati-clase-1-intubacion-facil-evaluacion-preanestesica.svg", alt: "Flujograma: Mallampati I: se espera una intubación fácil" },
  "SP-204": { titulo: "Fármacos vencidos en un establecimiento: residuos especiales", imagen: "flujogramas/productos-farmaceuticos-vencidos-residuos-solidos-especiales.svg", alt: "Flujograma: Fármacos vencidos en un establecimiento: residuos especiales" },
  "CIR-137": { titulo: "Mordedura de perro en el muslo, limpia y reciente: cierre primario", imagen: "flujogramas/mordedura-perro-propio-herida-limpia-cierre-primario.svg", alt: "Flujograma: Mordedura de perro en el muslo, limpia y reciente: cierre primario" },
  "CB-492": { titulo: "Sobredosis de amitriptilina con QRS de 140 ms e hipotensión: bicarbonato de sodio EV", imagen: "flujogramas/sobredosis-amitriptilina-qrs-140-hipotension-bicarbonato-sodio.svg", alt: "Flujograma: Sobredosis de amitriptilina con QRS de 140 ms e hipotensión: bicarbonato de sodio EV" },
  "SP-205": { titulo: "La ergonomía adapta el puesto, las herramientas y las tareas a la persona", imagen: "flujogramas/ergonomia-adaptar-puesto-trabajo-herramientas-a-la-persona.svg", alt: "Flujograma: La ergonomía adapta el puesto, las herramientas y las tareas a la persona" },
  "NRL-066": { titulo: "TEC grave con midriasis arreactiva tras estabilizar: TC de cráneo urgente para decidir cirugía", imagen: "flujogramas/tec-glasgow-8-midriasis-izquierda-bradicardia-tc-urgente-neurocirugia.svg", alt: "Flujograma: TEC grave con midriasis arreactiva tras estabilizar: TC de cráneo urgente para decidir cirugía" },
  "NRL-067": { titulo: "TEC grave con Glasgow 6 y SatO₂ 86 % antes de un traslado de 40 min: intubar con secuencia rápida", imagen: "flujogramas/tec-glasgow-6-fractura-base-craneo-sato2-86-intubar-antes-traslado.svg", alt: "Flujograma: TEC grave con Glasgow 6 y SatO₂ 86 % antes de un traslado de 40 min: intubar con secuencia rápida" },
  "TRA-056": { titulo: "Niña de 13 meses con cadera luxada alta (Tönnis III) sin reducir: reducción abierta", imagen: "flujogramas/nina-13-meses-luxacion-cadera-tonnis-iii-reduccion-abierta.svg", alt: "Flujograma: Niña de 13 meses con cadera luxada alta (Tönnis III) sin reducir: reducción abierta" },
  "CB-493": { titulo: "Los inhibidores de la bomba de protones actúan en las células parietales del cuerpo gástrico", imagen: "flujogramas/reflujo-ibp-bomba-h-k-atpasa-celulas-parietales.svg", alt: "Flujograma: Los inhibidores de la bomba de protones actúan en las células parietales del cuerpo gástrico" },
  "PED-252": { titulo: "Ingesta de álcali: necrosis de licuefacción del esófago y el estómago", imagen: "flujogramas/ingesta-hidroxido-sodio-alcali-necrosis-licuefaccion.svg", alt: "Flujograma: Ingesta de álcali: necrosis de licuefacción del esófago y el estómago" },
  "PSI-044": { titulo: "Dependencia de heroína con recaídas: mantenimiento con metadona", imagen: "flujogramas/heroina-endovenosa-recaidas-abstinencia-mantenimiento-metadona.svg", alt: "Flujograma: Dependencia de heroína con recaídas: mantenimiento con metadona" },
  "NEF-099": { titulo: "Diabética con proteinuria nefrótica, complemento bajo y sin retinopatía: biopsia renal", imagen: "flujogramas/diabetica-proteinuria-nefrotica-complemento-bajo-sin-retinopatia-biopsia-renal.svg", alt: "Flujograma: Diabética con proteinuria nefrótica, complemento bajo y sin retinopatía: biopsia renal" },
  "PED-253": { titulo: "Lactante con dificultad respiratoria grave en el primer nivel: oxígeno y referencia asistida", imagen: "flujogramas/lactante-dificultad-respiratoria-grave-primer-nivel-oxigeno-referencia.svg", alt: "Flujograma: Lactante con dificultad respiratoria grave en el primer nivel: oxígeno y referencia asistida" },
  "GIN-256": { titulo: "Insuficiencia cervical por historia: cerclaje profiláctico", imagen: "flujogramas/insuficiencia-cervical-dos-perdidas-indoloras-cerclaje.svg", alt: "Flujograma: Insuficiencia cervical por historia: cerclaje profiláctico" },
  "SP-206": { titulo: "Zika en las Américas desde 2015 con microcefalia: enfermedad emergente", imagen: "flujogramas/zika-brasil-2015-microcefalia-propagacion-americas-enfermedad-emergente.svg", alt: "Flujograma: Zika en las Américas desde 2015 con microcefalia: enfermedad emergente" },
  "CIR-138": { titulo: "Cáncer de colon ascendente sin metástasis: resección oncológica", imagen: "flujogramas/adenocarcinoma-colon-ascendente-sin-metastasis-hemicolectomia.svg", alt: "Flujograma: Cáncer de colon ascendente sin metástasis: resección oncológica" },
  "GIN-257": { titulo: "Patrón sinusoidal con bradicardia y fiebre: terminar la gestación", imagen: "flujogramas/rpm-24-horas-fiebre-patron-sinusoidal-bradicardia-terminar.svg", alt: "Flujograma: Patrón sinusoidal con bradicardia y fiebre: terminar la gestación" },
  "SP-207": { titulo: "Baja cobertura de promoción y prevención: es una debilidad organizacional", imagen: "flujogramas/baja-cobertura-promocion-prevencion-problema-priorizado-debilidad-organizacional.svg", alt: "Flujograma: Baja cobertura de promoción y prevención: es una debilidad organizacional" },
  "GIN-258": { titulo: "Cistocele y rectocele con periné amplio: colporrafia anterior, posterior y perineorrafia", imagen: "flujogramas/cistocele-rectocele-perine-amplio-colporrafia-perineorrafia.svg", alt: "Flujograma: Cistocele y rectocele con periné amplio: colporrafia anterior, posterior y perineorrafia" },
  "SP-208": { titulo: "Referencia difícil entre MINSA, FF. AA. y EsSalud pese a convenios: fragmentación del sistema", imagen: "flujogramas/referencia-entre-iafas-dificultades-convenio-fragmentacion-sistema-salud.svg", alt: "Flujograma: Referencia difícil entre MINSA, FF. AA. y EsSalud pese a convenios: fragmentación del sistema" },
  "NEF-100": { titulo: "Convulsión tras una RTU de próstata con irrigación hipotónica: hiponatremia", imagen: "flujogramas/postoperatorio-rtu-prostata-irrigacion-hipotonica-convulsion-hiponatremia.svg", alt: "Flujograma: Convulsión tras una RTU de próstata con irrigación hipotónica: hiponatremia" },
  "GAS-081": { titulo: "H. pylori con resistencia alta a claritromicina: cuádruple con bismuto", imagen: "flujogramas/helicobacter-pylori-resistencia-claritromicina-cuadruple-bismuto.svg", alt: "Flujograma: H. pylori con resistencia alta a claritromicina: cuádruple con bismuto" },
  "GIN-259": { titulo: "Primer control prenatal a las 22 semanas: el inicio tardío es el principal riesgo", imagen: "flujogramas/primigesta-19-anos-primer-control-22-semanas-inicio-tardio.svg", alt: "Flujograma: Primer control prenatal a las 22 semanas: el inicio tardío es el principal riesgo" },
  "PED-254": { titulo: "Fibrosis quística que pierde sal por el sudor: salino 0,9 % en bolo", imagen: "flujogramas/fibrosis-quistica-sudor-hiponatremia-hipovolemica-salino-09.svg", alt: "Flujograma: Fibrosis quística que pierde sal por el sudor: salino 0,9 % en bolo" },
  "SP-209": { titulo: "Programa de mejora del primer nivel: priorizar el centro de salud I-3", imagen: "flujogramas/direccion-regional-priorizar-primer-nivel-centro-salud-i-3-puerta-entrada.svg", alt: "Flujograma: Programa de mejora del primer nivel: priorizar el centro de salud I-3" },
  "NEF-101": { titulo: "Hipopotasemia con alcalosis y sodio y potasio urinarios altos en quien toma «pastillas para adelgazar»: diurético de asa", imagen: "flujogramas/preparado-para-bajar-peso-potasio-2-6-alcalosis-diuretico-de-asa.svg", alt: "Flujograma: Hipopotasemia con alcalosis y sodio y potasio urinarios altos en quien toma «pastillas para adelgazar»: diurético de asa" },
  "GIN-260": { titulo: "Embarazo logrado con clomifeno: la causa era ovulatoria", imagen: "flujogramas/infertilidad-embarazo-con-clomifeno-factor-ovulatorio.svg", alt: "Flujograma: Embarazo logrado con clomifeno: la causa era ovulatoria" },
  "CB-494": { titulo: "Herida quirúrgica a las 36 horas: fase inflamatoria de la cicatrización", imagen: "flujogramas/herida-quirurgica-36-horas-edema-eritema-exudado-fase-inflamatoria.svg", alt: "Flujograma: Herida quirúrgica a las 36 horas: fase inflamatoria de la cicatrización" },
  "GAS-082": { titulo: "Falla hepática aguda con hipertensión intracraneal: manitol", imagen: "flujogramas/falla-hepatica-aguda-paracetamol-edema-cerebral-manitol.svg", alt: "Flujograma: Falla hepática aguda con hipertensión intracraneal: manitol" },
  "PED-255": { titulo: "Estado epiléptico: más consumo de oxígeno y peor ventilación", imagen: "flujogramas/estado-epileptico-hipoxemia-acidosis-lactica-consumo-oxigeno.svg", alt: "Flujograma: Estado epiléptico: más consumo de oxígeno y peor ventilación" },
  "SP-210": { titulo: "Consumo de alcohol en adolescentes con varios determinantes: programa integral educativo, comunitario y regulatorio", imagen: "flujogramas/adolescentes-consumo-alcohol-programa-integral-educativo-comunitario-regulatorio.svg", alt: "Flujograma: Consumo de alcohol en adolescentes con varios determinantes: programa integral educativo, comunitario y regulatorio" },
  "CIR-139": { titulo: "Quemado con lesión inhalatoria: primero asegurar la vía aérea", imagen: "flujogramas/quemadura-incendio-cerrado-estridor-hollin-intubacion-precoz.svg", alt: "Flujograma: Quemado con lesión inhalatoria: primero asegurar la vía aérea" },
  "GIN-261": { titulo: "Sangrado posmenopáusico en usuaria de tamoxifeno: primero ecografía transvaginal", imagen: "flujogramas/tamoxifeno-sangrado-posmenopausico-ecografia-transvaginal.svg", alt: "Flujograma: Sangrado posmenopáusico en usuaria de tamoxifeno: primero ecografía transvaginal" },
  "GIN-262": { titulo: "Signo de la T: gestación monocoriónica biamniótica", imagen: "flujogramas/gemelar-una-placenta-membrana-fina-signo-t-monocorial-biamniotica.svg", alt: "Flujograma: Signo de la T: gestación monocoriónica biamniótica" },
  "PED-256": { titulo: "Displasia broncopulmonar en evolución: lo fundamental es un buen aporte calórico-proteico", imagen: "flujogramas/prematuro-28-semanas-cpap-displasia-broncopulmonar-aporte-calorico.svg", alt: "Flujograma: Displasia broncopulmonar en evolución: lo fundamental es un buen aporte calórico-proteico" },
  "GIN-263": { titulo: "Fiebre a las 9 horas del parto sin foco: pirógenos endógenos", imagen: "flujogramas/puerpera-9-horas-fiebre-sin-foco-pirogenos-endogenos.svg", alt: "Flujograma: Fiebre a las 9 horas del parto sin foco: pirógenos endógenos" },
  "CAR-080": { titulo: "Edema agudo de pulmón con sobrecarga de volumen: furosemida EV", imagen: "flujogramas/mujer-80-anos-edema-agudo-pulmon-hipertensa-furosemida-ev.svg", alt: "Flujograma: Edema agudo de pulmón con sobrecarga de volumen: furosemida EV" },
  "CIR-140": { titulo: "Escala de Alvarado: este caso suma 8 puntos", imagen: "flujogramas/escala-alvarado-8-puntos-apendicitis-probable.svg", alt: "Flujograma: Escala de Alvarado: este caso suma 8 puntos" },
  "PED-257": { titulo: "Lactante de 3 meses con factores de riesgo de anemia: hierro profiláctico desde ahora", imagen: "flujogramas/lactante-3-meses-corte-precoz-cordon-hierro-profilactico-inmediato.svg", alt: "Flujograma: Lactante de 3 meses con factores de riesgo de anemia: hierro profiláctico desde ahora" },
  "REU-074": { titulo: "Parches y placas pruriginosas de años con linfocitos T CD4 atípicos en la epidermis: micosis fungoide", imagen: "flujogramas/parches-placas-pruriginosas-anos-cd4-epidermotropismo-micosis-fungoide-linfoma.svg", alt: "Flujograma: Parches y placas pruriginosas de años con linfocitos T CD4 atípicos en la epidermis: micosis fungoide" },
  "SP-211": { titulo: "Infecciones intrahospitalarias que bajan de 8 % a 2 %: reducción relativa del riesgo del 75 %", imagen: "flujogramas/infecciones-intrahospitalarias-8-a-2-por-ciento-reduccion-relativa-riesgo-75.svg", alt: "Flujograma: Infecciones intrahospitalarias que bajan de 8 % a 2 %: reducción relativa del riesgo del 75 %" },
  "GAS-083": { titulo: "Cálculos pigmentarios marrones: se forman en la vía biliar infectada", imagen: "flujogramas/calculos-pigmentarios-marrones-coledoco-estasis-infeccion.svg", alt: "Flujograma: Cálculos pigmentarios marrones: se forman en la vía biliar infectada" },
  "NEF-102": { titulo: "Nefritis lúpica clase IV con creatinina alta que no mejora con corticoide: ciclofosfamida", imagen: "flujogramas/lupus-creatinina-3-1-cilindros-hematicos-nefritis-clase-iv-ciclofosfamida.svg", alt: "Flujograma: Nefritis lúpica clase IV con creatinina alta que no mejora con corticoide: ciclofosfamida" },
  "PED-258": { titulo: "Lactante con infección urinaria febril, vómitos y mal estado: antibiótico EV y ecografía renal", imagen: "flujogramas/lactante-6-meses-itu-febril-vomitos-antibiotico-ev-ecografia-renal.svg", alt: "Flujograma: Lactante con infección urinaria febril, vómitos y mal estado: antibiótico EV y ecografía renal" },
  "PED-259": { titulo: "Hipotonía al nacer y luego hiperfagia con obesidad e hipogonadismo: síndrome de Prader-Willi", imagen: "flujogramas/hipotonia-neonatal-hiperfagia-obesidad-hipogonadismo-prader-willi.svg", alt: "Flujograma: Hipotonía al nacer y luego hiperfagia con obesidad e hipogonadismo: síndrome de Prader-Willi" },
  "PED-260": { titulo: "Sepsis neonatal con fontanela abombada: hemocultivo y cultivo de líquido cefalorraquídeo", imagen: "flujogramas/sepsis-neonatal-fontanela-abombada-hemocultivo-cultivo-lcr.svg", alt: "Flujograma: Sepsis neonatal con fontanela abombada: hemocultivo y cultivo de líquido cefalorraquídeo" },
  "HEM-043": { titulo: "Leucocitosis con todas las etapas mieloides y esplenomegalia: leucemia mieloide crónica, BCR-ABL1", imagen: "flujogramas/leucocitosis-130000-mielocitos-esplenomegalia-leucemia-mieloide-cronica-bcr-abl1.svg", alt: "Flujograma: Leucocitosis con todas las etapas mieloides y esplenomegalia: leucemia mieloide crónica, BCR-ABL1" },
  "SP-212": { titulo: "Coordinar a distintos sectores para mejorar los determinantes de la salud: acción intersectorial", imagen: "flujogramas/carta-ottawa-articulacion-coordinacion-sectores-comunicacion-intersectorial.svg", alt: "Flujograma: Coordinar a distintos sectores para mejorar los determinantes de la salud: acción intersectorial" },
  "PED-261": { titulo: "Policitemia neonatal asintomática (hematocrito 68 %): hidratación EV y control del hematocrito", imagen: "flujogramas/recien-nacido-41-semanas-hematocrito-68-asintomatico-hidratacion.svg", alt: "Flujograma: Policitemia neonatal asintomática (hematocrito 68 %): hidratación EV y control del hematocrito" },
  "INF-121": { titulo: "Fiebre prolongada, hepatoesplenomegalia y pancitopenia con rK39 positiva: leishmaniasis visceral", imagen: "flujogramas/vih-loreto-fiebre-hepatoesplenomegalia-pancitopenia-rk39-leishmaniasis-visceral.svg", alt: "Flujograma: Fiebre prolongada, hepatoesplenomegalia y pancitopenia con rK39 positiva: leishmaniasis visceral" },
  "NEU-071": { titulo: "Fumador con FEV1/FVC < 0,7 sin reversibilidad y FEV1 45 %: EPOC moderada-grave", imagen: "flujogramas/fumador-fev1-fvc-menor-07-fev1-45-epoc-gold-3.svg", alt: "Flujograma: Fumador con FEV1/FVC < 0,7 sin reversibilidad y FEV1 45 %: EPOC moderada-grave" },
  "INF-122": { titulo: "Malaria vivax tratada: antes de la primaquina, descartar déficit de G6PD", imagen: "flujogramas/malaria-vivax-cloroquina-cura-radical-primaquina-descartar-deficit-g6pd.svg", alt: "Flujograma: Malaria vivax tratada: antes de la primaquina, descartar déficit de G6PD" },
  "SP-213": { titulo: "Doble chequeo y alertas antes de dispensar: estrategia proactiva de seguridad del paciente", imagen: "flujogramas/doble-chequeo-alertas-informaticas-medicacion-seguridad-paciente-proactiva.svg", alt: "Flujograma: Doble chequeo y alertas antes de dispensar: estrategia proactiva de seguridad del paciente" },
  "PED-262": { titulo: "Escolar sano: evitar las bebidas azucaradas y tomar agua simple", imagen: "flujogramas/escolar-8-anos-evitar-bebidas-azucaradas-agua-simple.svg", alt: "Flujograma: Escolar sano: evitar las bebidas azucaradas y tomar agua simple" },
  "HEM-044": { titulo: "Sangrado mucoso con plaquetas, TP y TTPa normales e historia familiar: cofactor de ristocetina", imagen: "flujogramas/sangrado-dental-menorragia-familia-plaquetas-tp-ttpa-normales-cofactor-ristocetina.svg", alt: "Flujograma: Sangrado mucoso con plaquetas, TP y TTPa normales e historia familiar: cofactor de ristocetina" },
  "CIR-141": { titulo: "Hernia incisional estrangulada: laparotomía de urgencia", imagen: "flujogramas/hernia-incisional-estrangulada-obstruccion-laparotomia-urgente.svg", alt: "Flujograma: Hernia incisional estrangulada: laparotomía de urgencia" },
  "HEM-045": { titulo: "Anemia hemolítica con Coombs directo positivo: corticoide como tratamiento inicial", imagen: "flujogramas/hb-7-reticulocitos-coombs-directo-positivo-anemia-hemolitica-autoinmune-corticoide.svg", alt: "Flujograma: Anemia hemolítica con Coombs directo positivo: corticoide como tratamiento inicial" },
  "GAS-084": { titulo: "Peritonitis bacteriana espontánea con daño renal: cefotaxima y albúmina", imagen: "flujogramas/peritonitis-bacteriana-espontanea-cefotaxima-albumina.svg", alt: "Flujograma: Peritonitis bacteriana espontánea con daño renal: cefotaxima y albúmina" },
  "PED-263": { titulo: "Niño de 12 kg que tomó 500 mg de paracetamol: 42 mg/kg, dosis no tóxica, alta", imagen: "flujogramas/nino-12-kg-paracetamol-500-mg-dosis-no-toxica-alta.svg", alt: "Flujograma: Niño de 12 kg que tomó 500 mg de paracetamol: 42 mg/kg, dosis no tóxica, alta" },
  "END-069": { titulo: "Tirotoxicosis con bocio difuso y exoftalmos: los TRAb confirman la enfermedad de Graves", imagen: "flujogramas/mujer-25-anos-tirotoxicosis-bocio-difuso-exoftalmos-trab-graves.svg", alt: "Flujograma: Tirotoxicosis con bocio difuso y exoftalmos: los TRAb confirman la enfermedad de Graves" },
  "PED-264": { titulo: "Hipotiroidismo congénito a las 3 semanas: levotiroxina de inmediato", imagen: "flujogramas/recien-nacido-3-semanas-macroglosia-hernia-umbilical-levotiroxina.svg", alt: "Flujograma: Hipotiroidismo congénito a las 3 semanas: levotiroxina de inmediato" },
  "PED-265": { titulo: "Recién nacido sin ano: antes de operar, buscar malformaciones asociadas (VACTERL)", imagen: "flujogramas/recien-nacido-sin-ano-sin-meconio-vacterl-estudios-imagen.svg", alt: "Flujograma: Recién nacido sin ano: antes de operar, buscar malformaciones asociadas (VACTERL)" },
  "SP-214": { titulo: "Anemia alta en una comunidad quechua con barreras culturales: capacitar líderes comunitarios como promotores", imagen: "flujogramas/comunidad-quechua-anemia-barreras-culturales-lideres-comunitarios-promotores.svg", alt: "Flujograma: Anemia alta en una comunidad quechua con barreras culturales: capacitar líderes comunitarios como promotores" },
  "CB-495": { titulo: "Calambres en una carrera intensa: más lactato por glucólisis anaerobia", imagen: "flujogramas/carrera-intensa-calambres-gemelos-glucolisis-anaerobia-lactato.svg", alt: "Flujograma: Calambres en una carrera intensa: más lactato por glucólisis anaerobia" },
  "GIN-264": { titulo: "RPM pretérmino a las 29 semanas sin infección: manejo expectante", imagen: "flujogramas/rpm-pretermino-29-semanas-sin-infeccion-manejo-expectante.svg", alt: "Flujograma: RPM pretérmino a las 29 semanas sin infección: manejo expectante" },
  "GAS-085": { titulo: "Del cólico biliar a la pancreatitis biliar: el dolor cambió de patrón", imagen: "flujogramas/colico-biliar-cambia-a-dolor-en-cinturon-pancreatitis-biliar.svg", alt: "Flujograma: Del cólico biliar a la pancreatitis biliar: el dolor cambió de patrón" },
  "GIN-265": { titulo: "Proteinuria de 1+ en gestante con fiebre: probablemente transitoria, repetir", imagen: "flujogramas/gestante-febril-proteinuria-1-cruz-transitoria-repetir-examen.svg", alt: "Flujograma: Proteinuria de 1+ en gestante con fiebre: probablemente transitoria, repetir" },
  "PED-266": { titulo: "ITU febril con cicatrices renales en lactantes: reflujo vesicoureteral", imagen: "flujogramas/itu-febril-lactante-cicatriz-renal-reflujo-vesicoureteral.svg", alt: "Flujograma: ITU febril con cicatrices renales en lactantes: reflujo vesicoureteral" },
  "CIR-142": { titulo: "Cáncer gástrico con metástasis hepáticas: quimioterapia sistémica", imagen: "flujogramas/cancer-gastrico-estadio-iv-metastasis-hepaticas-quimioterapia.svg", alt: "Flujograma: Cáncer gástrico con metástasis hepáticas: quimioterapia sistémica" },
  "PED-267": { titulo: "Anemia microcítica e hipocrómica con dieta pobre en carnes: deficiencia de hierro", imagen: "flujogramas/nino-2-anos-zona-andina-anemia-microcitica-deficiencia-hierro.svg", alt: "Flujograma: Anemia microcítica e hipocrómica con dieta pobre en carnes: deficiencia de hierro" },
  "GAS-086": { titulo: "Ictericia obstructiva: la enzima que sube es la fosfatasa alcalina", imagen: "flujogramas/ictericia-obstructiva-bilirrubina-directa-fosfatasa-alcalina.svg", alt: "Flujograma: Ictericia obstructiva: la enzima que sube es la fosfatasa alcalina" },
  "SP-215": { titulo: "Atenciones por hora de trabajo médico: rendimiento hora médico", imagen: "flujogramas/productividad-consulta-externa-atenciones-por-hora-rendimiento-hora-medico.svg", alt: "Flujograma: Atenciones por hora de trabajo médico: rendimiento hora médico" },
  "PED-268": { titulo: "Tamizaje nutricional del escolar: índice de masa corporal para la edad", imagen: "flujogramas/escolar-9-anos-aumento-peso-tamizaje-indice-masa-corporal.svg", alt: "Flujograma: Tamizaje nutricional del escolar: índice de masa corporal para la edad" },
  "PED-269": { titulo: "Lactante deshidratado con íleo: solución polielectrolítica por vía EV", imagen: "flujogramas/lactante-deshidratacion-ileo-rha-ausentes-solucion-polielectrolitica-ev.svg", alt: "Flujograma: Lactante deshidratado con íleo: solución polielectrolítica por vía EV" },
  "END-070": { titulo: "Graves que no cede con metimazol, bocio que comprime la tráquea y oftalmopatía activa: tiroidectomía total", imagen: "flujogramas/graves-refractario-bocio-compresivo-oftalmopatia-tiroidectomia-total.svg", alt: "Flujograma: Graves que no cede con metimazol, bocio que comprime la tráquea y oftalmopatía activa: tiroidectomía total" },
  "SP-216": { titulo: "Aumento inusual de diarreas por posible agua contaminada: notificar y tomar muestras de agua y heces", imagen: "flujogramas/aumento-diarreas-7-dias-brote-agua-notificar-muestras-agua-heces.svg", alt: "Flujograma: Aumento inusual de diarreas por posible agua contaminada: notificar y tomar muestras de agua y heces" },
  "CB-496": { titulo: "Anestésico local con más cardiotoxicidad: bupivacaína", imagen: "flujogramas/anestesicos-locales-intravascular-colapso-cardiovascular-bupivacaina.svg", alt: "Flujograma: Anestésico local con más cardiotoxicidad: bupivacaína" },
  "SP-217": { titulo: "Revisiones sistemáticas como antecedentes: fuente secundaria", imagen: "flujogramas/busqueda-antecedentes-revisiones-sistematicas-fuente-secundaria.svg", alt: "Flujograma: Revisiones sistemáticas como antecedentes: fuente secundaria" },
  "PED-270": { titulo: "Asfixia al nacer y convulsiones sutiles a las 12 horas: encefalopatía hipóxico-isquémica", imagen: "flujogramas/neonato-apgar-3-5-convulsiones-sutiles-encefalopatia-hipoxico-isquemica.svg", alt: "Flujograma: Asfixia al nacer y convulsiones sutiles a las 12 horas: encefalopatía hipóxico-isquémica" },
  "GIN-266": { titulo: "Feto pequeño con oligohidramnios a las 39 semanas: inducir el parto", imagen: "flujogramas/feto-pequeno-percentil-8-oligohidramnios-39-semanas-induccion.svg", alt: "Flujograma: Feto pequeño con oligohidramnios a las 39 semanas: inducir el parto" },
  "CIR-143": { titulo: "Quemadura eléctrica: el daño mayor está en el músculo pegado al hueso", imagen: "flujogramas/quemadura-electrica-alto-voltaje-necrosis-muscular-perioseo.svg", alt: "Flujograma: Quemadura eléctrica: el daño mayor está en el músculo pegado al hueso" },
  "CIR-144": { titulo: "Neumotórax abierto: apósito oclusivo fijado en tres lados", imagen: "flujogramas/neumotorax-abierto-aposito-oclusivo-tres-lados-valvula.svg", alt: "Flujograma: Neumotórax abierto: apósito oclusivo fijado en tres lados" },
  "CIR-145": { titulo: "Úlcera perforada sellada en paciente de alto riesgo: manejo no operatorio", imagen: "flujogramas/ulcera-perforada-sellada-anciana-alto-riesgo-manejo-conservador.svg", alt: "Flujograma: Úlcera perforada sellada en paciente de alto riesgo: manejo no operatorio" },
  "GIN-267": { titulo: "Prolapso de cúpula vaginal en mujer sexualmente activa: colposacropexia", imagen: "flujogramas/prolapso-cupula-vaginal-sexualmente-activa-colposacropexia.svg", alt: "Flujograma: Prolapso de cúpula vaginal en mujer sexualmente activa: colposacropexia" },
  "NEF-103": { titulo: "Masa testicular sólida e indolora: marcadores tumorales y orquiectomía radical inguinal", imagen: "flujogramas/masa-testicular-solida-indolora-marcadores-orquiectomia-radical-inguinal.svg", alt: "Flujograma: Masa testicular sólida e indolora: marcadores tumorales y orquiectomía radical inguinal" },
  "CIR-146": { titulo: "Shock hemorrágico clase III por trauma de bazo: cristaloides y sangre", imagen: "flujogramas/shock-hemorragico-clase-3-trauma-esplenico-transfusion.svg", alt: "Flujograma: Shock hemorrágico clase III por trauma de bazo: cristaloides y sangre" },
  "GIN-268": { titulo: "Prolapso uterino con úlcera cervical: primero biopsia, luego colpocleisis", imagen: "flujogramas/prolapso-uterino-estadio-4-ulcera-cervical-biopsia-colpocleisis.svg", alt: "Flujograma: Prolapso uterino con úlcera cervical: primero biopsia, luego colpocleisis" },
  "PSI-045": { titulo: "Tortícolis, ojos hacia arriba y lengua afuera tras iniciar haloperidol: distonía aguda, biperideno", imagen: "flujogramas/haloperidol-tres-dias-torticolis-crisis-oculogira-distonia-aguda-biperideno.svg", alt: "Flujograma: Tortícolis, ojos hacia arriba y lengua afuera tras iniciar haloperidol: distonía aguda, biperideno" },
  "INF-123": { titulo: "TB y VIH con carga viral alta pese a buena adherencia: la rifampicina baja el antirretroviral", imagen: "flujogramas/tb-vih-carga-viral-alta-pese-adherencia-rifampicina-induccion-enzimatica.svg", alt: "Flujograma: TB y VIH con carga viral alta pese a buena adherencia: la rifampicina baja el antirretroviral" },
  "SP-218": { titulo: "Monitorear el mantenimiento preventivo de equipos: menos fallas, menos tiempo inactivo, sin interrupciones", imagen: "flujogramas/monitoreo-mantenimiento-preventivo-equipos-biomedicos-menos-fallas.svg", alt: "Flujograma: Monitorear el mantenimiento preventivo de equipos: menos fallas, menos tiempo inactivo, sin interrupciones" },
  "PED-271": { titulo: "Neumonía afebril del lactante de 2 meses con madre con leucorrea: Chlamydia, azitromicina", imagen: "flujogramas/lactante-2-meses-neumonia-afebril-chlamydia-trachomatis-azitromicina.svg", alt: "Flujograma: Neumonía afebril del lactante de 2 meses con madre con leucorrea: Chlamydia, azitromicina" },
  "CIR-147": { titulo: "Hemorroides que hay que reducir con la mano: ligadura con banda", imagen: "flujogramas/hemorroides-grado-3-reduccion-manual-ligadura-banda-elastica.svg", alt: "Flujograma: Hemorroides que hay que reducir con la mano: ligadura con banda" },
  "CIR-148": { titulo: "Nódulo perianal violáceo y muy doloroso: trombosis hemorroidal externa", imagen: "flujogramas/nodulo-violaceo-perianal-doloroso-trombosis-hemorroidal-externa.svg", alt: "Flujograma: Nódulo perianal violáceo y muy doloroso: trombosis hemorroidal externa" },
  "SP-219": { titulo: "Tamizaje de hemoglobina en el CRED: acción de prevención (detección temprana)", imagen: "flujogramas/cred-lactante-4-meses-tamizaje-hemoglobina-accion-prevencion.svg", alt: "Flujograma: Tamizaje de hemoglobina en el CRED: acción de prevención (detección temprana)" },
  "PED-272": { titulo: "Pronóstico del estado epiléptico: lo que más pesa es la causa", imagen: "flujogramas/estado-epileptico-pronostico-neurologico-etiologia-subyacente.svg", alt: "Flujograma: Pronóstico del estado epiléptico: lo que más pesa es la causa" },
  "NRL-068": { titulo: "Hemianopsia homónima derecha con prosopagnosia por embolia: infarto cortical occipitotemporal", imagen: "flujogramas/fibrilacion-auricular-hemianopsia-derecha-prosopagnosia-infarto-occipitotemporal.svg", alt: "Flujograma: Hemianopsia homónima derecha con prosopagnosia por embolia: infarto cortical occipitotemporal" },
  "NEU-072": { titulo: "Neumonía que aparece al séptimo día de hospitalización: neumonía intrahospitalaria", imagen: "flujogramas/hospitalizada-7-dias-fiebre-esputo-purulento-neumonia-intrahospitalaria.svg", alt: "Flujograma: Neumonía que aparece al séptimo día de hospitalización: neumonía intrahospitalaria" },
  "GIN-269": { titulo: "Fórmula obstétrica con mola y cesárea pretérmino: G3 P1112", imagen: "flujogramas/formula-obstetrica-mola-cesarea-36-semanas-g3-p1112.svg", alt: "Flujograma: Fórmula obstétrica con mola y cesárea pretérmino: G3 P1112" },
  "NEU-073": { titulo: "Fibrosis pulmonar con PaO₂ 50 y PaCO₂ 38: insuficiencia respiratoria tipo I y TC de alta resolución", imagen: "flujogramas/fibrosis-pulmonar-pao2-50-paco2-38-insuficiencia-tipo-1-tcar.svg", alt: "Flujograma: Fibrosis pulmonar con PaO₂ 50 y PaCO₂ 38: insuficiencia respiratoria tipo I y TC de alta resolución" },
  "GIN-270": { titulo: "Dolor súbito con masa anexial al día 7 del ciclo: quiste a pedículo torcido", imagen: "flujogramas/dolor-subito-fosa-iliaca-izquierda-dia-7-ciclo-quiste-torcido.svg", alt: "Flujograma: Dolor súbito con masa anexial al día 7 del ciclo: quiste a pedículo torcido" },
  "GIN-271": { titulo: "Útero grande, globuloso y blando con dismenorrea progresiva: adenomiosis", imagen: "flujogramas/utero-globuloso-blando-menorragia-dismenorrea-progresiva-adenomiosis.svg", alt: "Flujograma: Útero grande, globuloso y blando con dismenorrea progresiva: adenomiosis" },
  "CAR-081": { titulo: "Embolia pulmonar con hipotensión y VD dilatado: trombólisis sistémica", imagen: "flujogramas/tep-alto-riesgo-hipotension-vd-dilatado-trombolisis-sistemica.svg", alt: "Flujograma: Embolia pulmonar con hipotensión y VD dilatado: trombólisis sistémica" },
  "CAR-082": { titulo: "LDL de 195 con historia familiar de infarto precoz: estatina de alta intensidad", imagen: "flujogramas/ldl-195-antecedente-familiar-infarto-estatina-alta-intensidad.svg", alt: "Flujograma: LDL de 195 con historia familiar de infarto precoz: estatina de alta intensidad" },
  "GIN-272": { titulo: "Anticoncepción para quien olvida pastillas y tiene riesgo de ITS: implante + condón", imagen: "flujogramas/anticoncepcion-no-puede-tomar-pastillas-riesgo-its-implante.svg", alt: "Flujograma: Anticoncepción para quien olvida pastillas y tiene riesgo de ITS: implante + condón" },
  "GIN-273": { titulo: "Dolor púbico intenso tras parto de 4 200 g: diástasis de la sínfisis del pubis", imagen: "flujogramas/puerpera-parto-macrosomico-dolor-pubico-diastasis-sinfisis.svg", alt: "Flujograma: Dolor púbico intenso tras parto de 4 200 g: diástasis de la sínfisis del pubis" },
  "SP-220": { titulo: "Describir y explicar la salud de una población y sus determinantes: análisis de situación de salud (ASIS)", imagen: "flujogramas/describir-explicar-estado-salud-determinantes-analisis-situacion-salud.svg", alt: "Flujograma: Describir y explicar la salud de una población y sus determinantes: análisis de situación de salud (ASIS)" },
  "SP-221": { titulo: "El equipo sale a buscar casos revisando registros y llamando: vigilancia activa", imagen: "flujogramas/red-salud-visita-establecimientos-revisa-registros-vigilancia-activa.svg", alt: "Flujograma: El equipo sale a buscar casos revisando registros y llamando: vigilancia activa" },
  "CB-497": { titulo: "SDRA por sepsis: daño alveolar difuso con membranas hialinas", imagen: "flujogramas/shock-septico-sdra-dano-alveolar-difuso-membranas-hialinas.svg", alt: "Flujograma: SDRA por sepsis: daño alveolar difuso con membranas hialinas" },
  "HEM-046": { titulo: "Esferocitos con Coombs negativo y fragilidad osmótica positiva: esferocitosis hereditaria, esplenectomía", imagen: "flujogramas/esferocitos-coombs-negativo-fragilidad-osmotica-esferocitosis-esplenectomia.svg", alt: "Flujograma: Esferocitos con Coombs negativo y fragilidad osmótica positiva: esferocitosis hereditaria, esplenectomía" },
  "CB-498": { titulo: "El antiepiléptico más teratógeno en el embarazo: ácido valproico", imagen: "flujogramas/antiepilepticos-embarazo-acido-valproico-mas-teratogeno-tubo-neural.svg", alt: "Flujograma: El antiepiléptico más teratógeno en el embarazo: ácido valproico" },
  "CB-499": { titulo: "Sangre que coagula en un tubo de vidrio: la vía intrínseca empieza con el factor XII", imagen: "flujogramas/sangre-tubo-vidrio-activacion-contacto-via-intrinseca-factor-xii.svg", alt: "Flujograma: Sangre que coagula en un tubo de vidrio: la vía intrínseca empieza con el factor XII" },
  "REU-075": { titulo: "Varias foliculitis que se unen en una placa indurada con múltiples bocas de pus: ántrax", imagen: "flujogramas/foliculitis-coalescentes-placa-indurada-varios-puntos-pus-antrax-estafilococico.svg", alt: "Flujograma: Varias foliculitis que se unen en una placa indurada con múltiples bocas de pus: ántrax" },
  "SP-222": { titulo: "Mortalidad infantil de 40 rural frente a 15 urbana por pobreza y falta de servicios: inequidad en salud", imagen: "flujogramas/mortalidad-infantil-rural-40-urbana-15-determinantes-inequidad-salud.svg", alt: "Flujograma: Mortalidad infantil de 40 rural frente a 15 urbana por pobreza y falta de servicios: inequidad en salud" },
  "NEF-104": { titulo: "Nefropatía membranosa en fumador de 64 años que baja de peso: buscar un cáncer oculto", imagen: "flujogramas/fumador-64-anos-baja-peso-nefropatia-membranosa-buscar-neoplasia.svg", alt: "Flujograma: Nefropatía membranosa en fumador de 64 años que baja de peso: buscar un cáncer oculto" },
  "END-071": { titulo: "Adulto mayor con TSH 22, T4 libre baja y anti-TPO positivos: levotiroxina a dosis ajustada", imagen: "flujogramas/varon-70-anos-tsh-22-t4-baja-anti-tpo-hashimoto-levotiroxina.svg", alt: "Flujograma: Adulto mayor con TSH 22, T4 libre baja y anti-TPO positivos: levotiroxina a dosis ajustada" },
  "PED-273": { titulo: "Prematuro de 29 semanas en sala de partos: ventilar con pieza en T y presiones definidas", imagen: "flujogramas/prematuro-29-semanas-sala-partos-pieza-t-presiones-definidas.svg", alt: "Flujograma: Prematuro de 29 semanas en sala de partos: ventilar con pieza en T y presiones definidas" },
  "CB-500": { titulo: "Agonistas del GLP-1: frenan el glucagón y el hígado produce menos glucosa", imagen: "flujogramas/diabetes-obesidad-agonista-glp1-supresion-glucagon.svg", alt: "Flujograma: Agonistas del GLP-1: frenan el glucagón y el hígado produce menos glucosa" },
  "SP-223": { titulo: "Posición económica, género y etnia: determinantes estructurales de la salud", imagen: "flujogramas/marco-oms-determinantes-estructurales-posicion-economica-genero-etnia.svg", alt: "Flujograma: Posición económica, género y etnia: determinantes estructurales de la salud" },
  "CIR-149": { titulo: "XABCDE: la hemorragia que desangra va antes que la vía aérea", imagen: "flujogramas/politrauma-hemorragia-exanguinante-muslo-xabcde-torniquete.svg", alt: "Flujograma: XABCDE: la hemorragia que desangra va antes que la vía aérea" },
  "NEF-105": { titulo: "ERC estadio 4 con anemia normocítica y hierro normal: falta de eritropoyetina", imagen: "flujogramas/erc-estadio-4-anemia-normocitica-ferritina-normal-deficit-eritropoyetina.svg", alt: "Flujograma: ERC estadio 4 con anemia normocítica y hierro normal: falta de eritropoyetina" },
  "PED-274": { titulo: "Disentería en niña con desnutrición y cardiopatía: coprocultivo e iniciar antibiótico", imagen: "flujogramas/disenteria-nina-desnutrida-cardiopatia-coprocultivo-antibiotico.svg", alt: "Flujograma: Disentería en niña con desnutrición y cardiopatía: coprocultivo e iniciar antibiótico" },
  "CB-501": { titulo: "Célula cancerosa que no muere pese al ADN dañado: pérdida de función de TP53", imagen: "flujogramas/cancer-evasion-apoptosis-dano-adn-perdida-funcion-tp53.svg", alt: "Flujograma: Célula cancerosa que no muere pese al ADN dañado: pérdida de función de TP53" },
  "NEU-074": { titulo: "Absceso pulmonar que no mejora tras 3 semanas de antibiótico: broncoscopía", imagen: "flujogramas/absceso-pulmonar-sin-mejoria-tras-3-semanas-antibiotico-broncoscopia.svg", alt: "Flujograma: Absceso pulmonar que no mejora tras 3 semanas de antibiótico: broncoscopía" },
  "NEU-075": { titulo: "Criador de palomas con vidrio esmerilado y mosaico: neumonitis por hipersensibilidad, prednisona oral", imagen: "flujogramas/criador-palomas-vidrio-esmerilado-mosaico-neumonitis-hipersensibilidad-prednisona.svg", alt: "Flujograma: Criador de palomas con vidrio esmerilado y mosaico: neumonitis por hipersensibilidad, prednisona oral" },
  "NEF-106": { titulo: "Diabético con metformina y TFGe 40 que recibirá contraste: hidratar con salino y suspender metformina", imagen: "flujogramas/diabetico-metformina-tfge-40-tc-contraste-salino-suspender-metformina.svg", alt: "Flujograma: Diabético con metformina y TFGe 40 que recibirá contraste: hidratar con salino y suspender metformina" },
  "PED-275": { titulo: "Placa violácea con centro negro y hemólisis: loxoscelismo cutáneo-visceral", imagen: "flujogramas/placa-livida-centro-necrotico-hemolisis-orina-oscura-loxoscelismo.svg", alt: "Flujograma: Placa violácea con centro negro y hemólisis: loxoscelismo cutáneo-visceral" },
  "SP-224": { titulo: "Categoría mínima con camas de internamiento general: II-1", imagen: "flujogramas/norma-tecnica-categoria-minima-internamiento-general-ii-1.svg", alt: "Flujograma: Categoría mínima con camas de internamiento general: II-1" },
  "PED-276": { titulo: "Ictericia prolongada con hernia umbilical, hipotonía y fontanela grande: hipotiroidismo congénito", imagen: "flujogramas/neonato-15-dias-postermino-ictericia-prolongada-hernia-umbilical-hipotiroidismo.svg", alt: "Flujograma: Ictericia prolongada con hernia umbilical, hipotonía y fontanela grande: hipotiroidismo congénito" },
  "PED-277": { titulo: "Exantema en distintas etapas y luego placa roja dolorosa: varicela complicada con celulitis", imagen: "flujogramas/escolar-exantema-polimorfo-placa-eritematosa-dolorosa-varicela-celulitis.svg", alt: "Flujograma: Exantema en distintas etapas y luego placa roja dolorosa: varicela complicada con celulitis" },
  "CAR-083": { titulo: "Paro cardiaco en el primer nivel: compresiones de alta calidad y DEA cuanto antes", imagen: "flujogramas/paro-cardiaco-primer-nivel-compresiones-alta-calidad-dea.svg", alt: "Flujograma: Paro cardiaco en el primer nivel: compresiones de alta calidad y DEA cuanto antes" },
  "GIN-275": { titulo: "Úlcera genital indolora no tratada en la madre: sífilis congénita en el niño", imagen: "flujogramas/chancro-materno-no-tratado-sifilis-congenita-nariz-silla-montar.svg", alt: "Flujograma: Úlcera genital indolora no tratada en la madre: sífilis congénita en el niño" },
  "CAR-084": { titulo: "Triglicéridos altos que no bajan con dieta y ejercicio: fenofibrato", imagen: "flujogramas/hipertrigliceridemia-persistente-pese-estilo-vida-fenofibrato.svg", alt: "Flujograma: Triglicéridos altos que no bajan con dieta y ejercicio: fenofibrato" },
  "INF-124": { titulo: "Disnea con crepitantes 48 h después de la defervescencia: edema pulmonar por sobrecarga de fluidos", imagen: "flujogramas/dengue-grave-48-horas-defervescencia-disnea-crepitantes-sobrecarga-fluidos.svg", alt: "Flujograma: Disnea con crepitantes 48 h después de la defervescencia: edema pulmonar por sobrecarga de fluidos" },
  "REU-076": { titulo: "Lupus con síntomas B, adenopatías indoloras, LDH alta y complemento normal: descartar linfoma no Hodgkin", imagen: "flujogramas/lupus-fiebre-sudoracion-baja-peso-adenopatias-ldh-alta-complemento-normal-linfoma.svg", alt: "Flujograma: Lupus con síntomas B, adenopatías indoloras, LDH alta y complemento normal: descartar linfoma no Hodgkin" },
  "CIR-151": { titulo: "Absceso perianal en diabética: drenaje quirúrgico inmediato", imagen: "flujogramas/absceso-perianal-diabetica-fluctuante-drenaje-quirurgico-inmediato.svg", alt: "Flujograma: Absceso perianal en diabética: drenaje quirúrgico inmediato" },
  "SP-225": { titulo: "Modificar a propósito los resultados para complacer al financiador: mala conducta científica", imagen: "flujogramas/investigador-modifica-resultados-financiador-mala-conducta-cientifica.svg", alt: "Flujograma: Modificar a propósito los resultados para complacer al financiador: mala conducta científica" },
  "PED-278": { titulo: "Síntomas más de 2 veces por semana, pero no diarios y sin despertares: asma persistente leve", imagen: "flujogramas/nina-7-anos-sibilancias-mas-2-veces-semana-sin-despertares-asma-persistente-leve.svg", alt: "Flujograma: Síntomas más de 2 veces por semana, pero no diarios y sin despertares: asma persistente leve" },
  "NEF-107": { titulo: "Cólico nefrítico sin signos de infección: AINE EV y ecografía renal", imagen: "flujogramas/dolor-lumbar-irradiado-testiculo-hematuria-sin-infeccion-aine-ev-ecografia.svg", alt: "Flujograma: Cólico nefrítico sin signos de infección: AINE EV y ecografía renal" },
  "GAS-087": { titulo: "Masa epigástrica semanas después de una pancreatitis: seudoquiste", imagen: "flujogramas/seudoquiste-pancreatico-masa-epigastrica-semanas-despues.svg", alt: "Flujograma: Masa epigástrica semanas después de una pancreatitis: seudoquiste" },
  "PED-279": { titulo: "Primera convulsión sin fiebre ni focalidad en un lactante: buscar un trastorno hidroelectrolítico", imagen: "flujogramas/lactante-8-meses-primera-convulsion-afebril-sin-focalidad-trastorno-hidroelectrolitico.svg", alt: "Flujograma: Primera convulsión sin fiebre ni focalidad en un lactante: buscar un trastorno hidroelectrolítico" },
  "GAS-088": { titulo: "Enfermedad de Crohn: salteada, transmural y con granulomas", imagen: "flujogramas/crohn-empedrado-ileon-terminal-granulomas-no-caseificantes.svg", alt: "Flujograma: Enfermedad de Crohn: salteada, transmural y con granulomas" },
  "GIN-276": { titulo: "6 cm durante 4 horas con buenas contracciones: detención de la fase activa", imagen: "flujogramas/trabajo-parto-6-cm-4-horas-sin-cambio-detencion-fase-activa.svg", alt: "Flujograma: 6 cm durante 4 horas con buenas contracciones: detención de la fase activa" },
  "PED-280": { titulo: "Ocho resfríos al año en un niño que va a guardería: es normal", imagen: "flujogramas/nino-2-anos-guarderia-8-resfrios-al-ano-variante-normal.svg", alt: "Flujograma: Ocho resfríos al año en un niño que va a guardería: es normal" },
  "GIN-277": { titulo: "Hierro profiláctico en la gestante: desde las 14 semanas", imagen: "flujogramas/suplementacion-hierro-gestante-desde-14-semanas-minsa.svg", alt: "Flujograma: Hierro profiláctico en la gestante: desde las 14 semanas" },
  "CIR-152": { titulo: "Sangrado hepático incontrolable: maniobra de Pringle", imagen: "flujogramas/herida-bala-sangrado-hepatico-incontrolable-maniobra-pringle.svg", alt: "Flujograma: Sangrado hepático incontrolable: maniobra de Pringle" },
  "SP-226": { titulo: "Cartera de servicios: prestaciones que ofrece el establecimiento según las necesidades y prioridades de su población", imagen: "flujogramas/definicion-cartera-servicios-prestaciones-necesidades-poblacion.svg", alt: "Flujograma: Cartera de servicios: prestaciones que ofrece el establecimiento según las necesidades y prioridades de su población" },
  "CB-502": { titulo: "E. coli se fija al urotelio con fimbrias tipo I", imagen: "flujogramas/itu-baja-escherichia-coli-adhesion-fimbrias-tipo-1-urotelio.svg", alt: "Flujograma: E. coli se fija al urotelio con fimbrias tipo I" },
  "PED-281": { titulo: "Hoyuelo con mechón de pelo lumbosacro y examen normal: espina bífida oculta", imagen: "flujogramas/lactante-2-meses-hoyuelo-mechon-pelo-lumbosacro-espina-bifida-oculta.svg", alt: "Flujograma: Hoyuelo con mechón de pelo lumbosacro y examen normal: espina bífida oculta" },
  "GIN-278": { titulo: "Lupus con tres óbitos fetales: buscar anticuerpos antifosfolípido", imagen: "flujogramas/lupus-tres-obitos-fetales-sindrome-antifosfolipido-anticardiolipina.svg", alt: "Flujograma: Lupus con tres óbitos fetales: buscar anticuerpos antifosfolípido" },
  "REU-077": { titulo: "Dolor mecánico de rodilla con osteofitos y líquido sinovial no inflamatorio: osteoartritis", imagen: "flujogramas/dolor-mecanico-rodilla-osteofitos-liquido-1800-leucocitos-osteoartritis.svg", alt: "Flujograma: Dolor mecánico de rodilla con osteofitos y líquido sinovial no inflamatorio: osteoartritis" },
  "PED-282": { titulo: "Dengue con dolor abdominal y vómitos persistentes: signos de alarma, hospitalizar en sala", imagen: "flujogramas/nina-7-anos-dengue-dolor-abdominal-vomitos-persistentes-hospitalizacion-sala.svg", alt: "Flujograma: Dengue con dolor abdominal y vómitos persistentes: signos de alarma, hospitalizar en sala" },
  "NEF-108": { titulo: "Atrapado 8 horas bajo un muro con orina oscura: necrosis tubular aguda por mioglobina", imagen: "flujogramas/aplastamiento-8-horas-orina-oscura-rabdomiolisis-necrosis-tubular-mioglobina.svg", alt: "Flujograma: Atrapado 8 horas bajo un muro con orina oscura: necrosis tubular aguda por mioglobina" },
  "HEM-047": { titulo: "Blastos con gránulos azurófilos: los bastones de Auer confirman el linaje mieloide", imagen: "flujogramas/blastos-granulos-azurofilos-medula-leucemia-mieloide-aguda-bastones-auer.svg", alt: "Flujograma: Blastos con gránulos azurófilos: los bastones de Auer confirman el linaje mieloide" },
  "PED-283": { titulo: "Neonato de 3 días que perdió 7 % y orina bien: reforzar la lactancia y vigilar el peso", imagen: "flujogramas/neonato-3-dias-perdida-7-peso-diuresis-adecuada-reforzar-lactancia.svg", alt: "Flujograma: Neonato de 3 días que perdió 7 % y orina bien: reforzar la lactancia y vigilar el peso" },
  "GIN-279": { titulo: "Secreción con sangre por un solo pezón y sin masa: papiloma intraductal", imagen: "flujogramas/telorragia-espontanea-unilateral-sin-masa-papiloma-intraductal.svg", alt: "Flujograma: Secreción con sangre por un solo pezón y sin masa: papiloma intraductal" },
  "REU-078": { titulo: "Vitíligo localizado (5 % de superficie): corticoide tópico de potencia media-alta", imagen: "flujogramas/vitiligo-localizado-5-por-ciento-cara-manos-corticoide-topico.svg", alt: "Flujograma: Vitíligo localizado (5 % de superficie): corticoide tópico de potencia media-alta" },
  "GIN-280": { titulo: "Von Willebrand en trabajo de parto: vía vaginal con concentrados de FvW/FVIII", imagen: "flujogramas/von-willebrand-tipo-1-trabajo-parto-via-vaginal-concentrados.svg", alt: "Flujograma: Von Willebrand en trabajo de parto: vía vaginal con concentrados de FvW/FVIII" },
  "NEF-109": { titulo: "Diarrea y vómitos con anuria, urea 130 y creatinina 2,5: lesión renal prerrenal, solución salina", imagen: "flujogramas/diarrea-vomitos-anuria-urea-130-creatinina-2-5-prerrenal-salino.svg", alt: "Flujograma: Diarrea y vómitos con anuria, urea 130 y creatinina 2,5: lesión renal prerrenal, solución salina" },
  "GIN-281": { titulo: "Mastitis en puérpera con VIH: suspender la lactancia de ambos senos", imagen: "flujogramas/puerpera-vih-mastitis-suspender-lactancia-ambos-senos.svg", alt: "Flujograma: Mastitis en puérpera con VIH: suspender la lactancia de ambos senos" },
  "CIR-153": { titulo: "Quemadura seca, coriácea e indolora: espesor total y desbridamiento temprano", imagen: "flujogramas/quemadura-espesor-total-coriacea-indolora-desbridamiento-temprano.svg", alt: "Flujograma: Quemadura seca, coriácea e indolora: espesor total y desbridamiento temprano" },
  "PED-284": { titulo: "Lactante sacado de un canal de agua fría, en paro y sin signos de muerte: iniciar RCP ya", imagen: "flujogramas/lactante-ahogamiento-agua-fria-paro-sin-signos-muerte-iniciar-rcp.svg", alt: "Flujograma: Lactante sacado de un canal de agua fría, en paro y sin signos de muerte: iniciar RCP ya" },
  "GAS-089": { titulo: "Cáncer gástrico temprano: la ecoendoscopía mide la profundidad", imagen: "flujogramas/cancer-gastrico-temprano-ecoendoscopia-profundidad-capas.svg", alt: "Flujograma: Cáncer gástrico temprano: la ecoendoscopía mide la profundidad" },
  "SP-227": { titulo: "Describir a todos los pacientes con una enfermedad rara sin grupo de comparación: serie de casos", imagen: "flujogramas/pacientes-enfermedad-rara-descripcion-sin-grupo-comparacion-serie-casos.svg", alt: "Flujograma: Describir a todos los pacientes con una enfermedad rara sin grupo de comparación: serie de casos" },
  "PED-285": { titulo: "Síndrome nefrótico sin remisión tras 8 semanas de prednisona: biopsia renal", imagen: "flujogramas/sindrome-nefrotico-sin-remision-8-semanas-prednisona-biopsia-renal.svg", alt: "Flujograma: Síndrome nefrótico sin remisión tras 8 semanas de prednisona: biopsia renal" },
  "PED-286": { titulo: "Objetivo del CRED: vigilar de forma integral el crecimiento y desarrollo para actuar a tiempo", imagen: "flujogramas/control-crecimiento-desarrollo-cred-objetivo-vigilancia-integral.svg", alt: "Flujograma: Objetivo del CRED: vigilar de forma integral el crecimiento y desarrollo para actuar a tiempo" },
  "CIR-154": { titulo: "Apendicitis en un establecimiento del primer nivel: estabilizar y referir", imagen: "flujogramas/apendicitis-aguda-primer-nivel-hidratacion-antibiotico-referencia.svg", alt: "Flujograma: Apendicitis en un establecimiento del primer nivel: estabilizar y referir" },
  "REU-079": { titulo: "Osteoporosis con fractura por fragilidad y T -2,7: alendronato semanal con calcio y vitamina D", imagen: "flujogramas/posmenopausica-fractura-radio-t-score-menos-2-7-alendronato-calcio-vitamina-d.svg", alt: "Flujograma: Osteoporosis con fractura por fragilidad y T -2,7: alendronato semanal con calcio y vitamina D" },
  "GIN-282": { titulo: "Preeclampsia con criterios de severidad a las 35 semanas: estabilizar y terminar", imagen: "flujogramas/preeclampsia-severa-35-semanas-plaquetopenia-finalizar-gestacion.svg", alt: "Flujograma: Preeclampsia con criterios de severidad a las 35 semanas: estabilizar y terminar" },
  "GIN-283": { titulo: "Dolor súbito, cese de contracciones y bradicardia tras cesárea previa: rotura uterina", imagen: "flujogramas/prueba-trabajo-parto-cesarea-previa-rotura-uterina-cesarea-emergencia.svg", alt: "Flujograma: Dolor súbito, cese de contracciones y bradicardia tras cesárea previa: rotura uterina" },
  "GAS-090": { titulo: "Colección pancreática con gas: necrosis infectada", imagen: "flujogramas/pancreatitis-coleccion-con-gas-necrosis-pancreatica-infectada.svg", alt: "Flujograma: Colección pancreática con gas: necrosis infectada" },
  "CIR-155": { titulo: "Fístula perianal transesfinteriana baja: fistulotomía", imagen: "flujogramas/fistula-perianal-transesfinteriana-baja-fistulotomia.svg", alt: "Flujograma: Fístula perianal transesfinteriana baja: fistulotomía" },
  "PED-287": { titulo: "PTI con epistaxis que no cede: prednisona 2 mg/kg/día", imagen: "flujogramas/nina-3-anos-plaquetas-25000-epistaxis-persistente-pti-prednisona.svg", alt: "Flujograma: PTI con epistaxis que no cede: prednisona 2 mg/kg/día" },
  "SP-228": { titulo: "Dotación mínima de médicos en un establecimiento I-3: dos médicos generales", imagen: "flujogramas/norma-tecnica-establecimiento-i-3-dotacion-minima-dos-medicos-generales.svg", alt: "Flujograma: Dotación mínima de médicos en un establecimiento I-3: dos médicos generales" },
  "PED-288": { titulo: "Recién nacido de madre con sífilis no tratada: penicilina G sódica EV por 10 días", imagen: "flujogramas/recien-nacido-madre-vdrl-sin-tratamiento-sifilis-congenita-penicilina-g-sodica.svg", alt: "Flujograma: Recién nacido de madre con sífilis no tratada: penicilina G sódica EV por 10 días" },
  "INF-125": { titulo: "Sida con CD4 < 50 y retinitis necrosante con hemorragias («pizza»): citomegalovirus", imagen: "flujogramas/sida-cd4-menor-50-retinitis-necrosante-hemorragias-pizza-citomegalovirus.svg", alt: "Flujograma: Sida con CD4 < 50 y retinitis necrosante con hemorragias («pizza»): citomegalovirus" },
  "CIR-156": { titulo: "Politrauma en shock lejos del hospital: reanimar y controlar el sangrado antes de trasladar", imagen: "flujogramas/politrauma-shock-hemorragico-fractura-femur-reanimar-antes-de-referir.svg", alt: "Flujograma: Politrauma en shock lejos del hospital: reanimar y controlar el sangrado antes de trasladar" },
  "END-072": { titulo: "Glucosa 360, pH 7,02, bicarbonato 9 y cetonas: cetoacidosis diabética con anión gap alto", imagen: "flujogramas/glucosa-360-ph-7-02-bicarbonato-9-cetonas-cetoacidosis-diabetica.svg", alt: "Flujograma: Glucosa 360, pH 7,02, bicarbonato 9 y cetonas: cetoacidosis diabética con anión gap alto" },
  "REU-080": { titulo: "Habones tras comer mariscos sin síntomas respiratorios ni hipotensión: antihistamínico oral", imagen: "flujogramas/habones-tras-mariscos-sin-dificultad-respiratoria-urticaria-antihistaminico.svg", alt: "Flujograma: Habones tras comer mariscos sin síntomas respiratorios ni hipotensión: antihistamínico oral" },
  "CAR-085": { titulo: "Ginecomastia por espironolactona en insuficiencia cardiaca: cambiar a eplerenona", imagen: "flujogramas/insuficiencia-cardiaca-ginecomastia-espironolactona-cambiar-eplerenona.svg", alt: "Flujograma: Ginecomastia por espironolactona en insuficiencia cardiaca: cambiar a eplerenona" },
  "CIR-157": { titulo: "Cáncer gástrico: la invasión hasta la serosa (T4a) es lo que más pesa", imagen: "flujogramas/cancer-gastrico-t4a-serosa-pronostico-adyuvancia.svg", alt: "Flujograma: Cáncer gástrico: la invasión hasta la serosa (T4a) es lo que más pesa" },
  "SP-229": { titulo: "El proceso salud-enfermedad es dinámico, continuo y biopsicosocial", imagen: "flujogramas/proceso-salud-enfermedad-dinamico-continuo-biopsicosocial.svg", alt: "Flujograma: El proceso salud-enfermedad es dinámico, continuo y biopsicosocial" },
  "GIN-284": { titulo: "Taquisistolia con desaceleraciones tardías: reanimación intrauterina", imagen: "flujogramas/induccion-oxitocina-taquisistolia-desaceleraciones-tardias-reanimacion.svg", alt: "Flujograma: Taquisistolia con desaceleraciones tardías: reanimación intrauterina" },
  "NRL-069": { titulo: "Primera convulsión en un agricultor de zona endémica de cisticercosis: TC cerebral", imagen: "flujogramas/agricultor-sierra-primera-convulsion-cerdo-neurocisticercosis-tc-cerebral.svg", alt: "Flujograma: Primera convulsión en un agricultor de zona endémica de cisticercosis: TC cerebral" },
  "GIN-285": { titulo: "Parto pretérmino inminente a las 29 semanas: sulfato de magnesio para proteger el cerebro fetal", imagen: "flujogramas/parto-pretermino-29-semanas-sulfato-magnesio-neuroproteccion.svg", alt: "Flujograma: Parto pretérmino inminente a las 29 semanas: sulfato de magnesio para proteger el cerebro fetal" },
  "NRL-070": { titulo: "Ausencias típicas en una niña: etosuximida como primera elección", imagen: "flujogramas/nina-7-anos-desconexiones-breves-hiperventilacion-ausencias-etosuximida.svg", alt: "Flujograma: Ausencias típicas en una niña: etosuximida como primera elección" },
  "GIN-286": { titulo: "Aborto previo: cuenta como gestación pero no como parto (nulípara)", imagen: "flujogramas/aborto-previo-8-semanas-segundigesta-nulipara.svg", alt: "Flujograma: Aborto previo: cuenta como gestación pero no como parto (nulípara)" },
  "GIN-287": { titulo: "Colestasis del embarazo con ácidos biliares de 110: ácido ursodesoxicólico", imagen: "flujogramas/colestasis-embarazo-acidos-biliares-110-ursodesoxicolico.svg", alt: "Flujograma: Colestasis del embarazo con ácidos biliares de 110: ácido ursodesoxicólico" },
  "NEU-076": { titulo: "TB pulmonar confirmada por Xpert, sensible a rifampicina: iniciar RHZE y notificar", imagen: "flujogramas/tos-3-meses-cavidad-xpert-positivo-sin-resistencia-rhze-notificar.svg", alt: "Flujograma: TB pulmonar confirmada por Xpert, sensible a rifampicina: iniciar RHZE y notificar" },
  "CB-503": { titulo: "Fármaco muy hidrofílico, irritante digestivo y que necesita niveles rápidos: vía endovenosa en infusión", imagen: "flujogramas/farmaco-hidrofilico-irritante-gastrointestinal-via-endovenosa-infusion.svg", alt: "Flujograma: Fármaco muy hidrofílico, irritante digestivo y que necesita niveles rápidos: vía endovenosa en infusión" },
  "SP-230": { titulo: "Comparar el IMC promedio de dos grupos independientes con datos normales: t de Student", imagen: "flujogramas/comparar-imc-dos-centros-salud-normal-homocedasticidad-t-student-independientes.svg", alt: "Flujograma: Comparar el IMC promedio de dos grupos independientes con datos normales: t de Student" },
  "PED-289": { titulo: "Tras una infección: citopenias, transaminasas y triglicéridos altos: síndrome hemofagocítico secundario", imagen: "flujogramas/escolar-infeccion-piel-citopenias-transaminasas-trigliceridos-sindrome-hemofagocitico.svg", alt: "Flujograma: Tras una infección: citopenias, transaminasas y triglicéridos altos: síndrome hemofagocítico secundario" },
};
