"""Bloque 7 · parte E."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"

# CAR-061 · fases
V("fases", "CAR-061", "infarto-muerte-prehospitalaria-fibrilacion-ventricular", "¿De qué muere el infartado y cuándo?",
  "CARDIOLOGÍA ENAM: MUERTE PREHOSPITALARIA EN EL INFARTO", "CARDIOLOGÍA",
  ("Complicaciones del infarto", ["Cada complicación tiene su momento típico",
   "En la primera hora, antes del hospital, mata la fibrilación ventricular"]),
  ("Pregunta de cardiología", ["¿Causa más frecuente de muerte por infarto antes de llegar al hospital?"]),
  {"rotulo": "Tiempo desde el inicio del infarto", "ans": 0,
   "fases": [("1.ª hora", "Prehospital", "FIBRILACIÓN VENTRICULAR", ["Muerte súbita", "Desfibrilador precoz"]),
             ("Horas-días", "Hospital", "Shock cardiogénico", ["Infarto extenso"]),
             ("3-7 días", "Pared necrótica", "Rotura cardiaca", ["Pared libre, septo, músculo papilar"]),
             ("Semanas", "Cicatriz", "Aneurisma, pericarditis", ["Dressler"])],
   "curvas": [("Riesgo de arritmia", ROSE, [1.0, 0.7, 0.4, 0.25, 0.2, 0.15, 0.1])],
   "chips_titulo": "Causa prehospitalaria · marcada la correcta",
   "chips": [("Fibrilación ventricular", True), ("Shock cardiogénico", False), ("Rotura cardiaca", False), ("Infarto del VD", False)]},
  ["La mitad de las muertes por infarto ocurre antes de llegar al hospital.",
   "Los desfibriladores públicos y la RCP por testigos salvan vidas.",
   "En el hospital, la principal causa de muerte es el shock cardiogénico."],
  "AHA – Heart disease and stroke statistics (2025) · ESC – Guidelines for acute coronary syndromes (2023)")

# HEM-033 · termómetro
V("termometro", "HEM-033", "neutropenia-menor-500-causa-farmacologica", "Neutropenia grave",
  "HEMATOLOGÍA ENAM: NEUTROPENIA GRAVE", "HEMATOLOGÍA",
  ("Neutropenia", ["Se gradúa por el recuento absoluto de neutrófilos",
   "Grave (< 500/µl): la causa adquirida más frecuente es un fármaco"]),
  ("Pregunta de hematología", ["¿Causa más frecuente de neutropenia < 500/µl?"]),
  {"rotulo": "Recuento absoluto de neutrófilos",
   "niveles": [("1000-1500", "Leve", ["Riesgo bajo de infección"]),
               ("500-1000", "Moderada", ["Riesgo moderado"]),
               ("< 500", "Grave", ["CAUSA: FÁRMACOS", "Agranulocitosis"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Buscar y suspender el fármaco", ["Metamizol, antitiroideos, clozapina", "Sulfas, quimioterapia"], True),
             (2, "Si hay fiebre: antibiótico EV", ["Neutropenia febril = emergencia"], False),
             (3, "Estudiar otras causas", ["Frotis, B12, autoinmune, médula"], False)]},
  ["El metamizol y los antitiroideos causan agranulocitosis idiosincrática.",
   "Suele recuperarse en 1-3 semanas tras suspender el fármaco.",
   "Factor estimulante de colonias en casos graves."],
  "British Society for Haematology – Guideline on the investigation of neutropenia (2023) · " + HARRISON)

# NEU-050 · radial
V("radial", "NEU-050", "viuda-esposo-fumador-epoc-tabaquismo-pasivo", "EPOC en una mujer que no fuma",
  "NEUMOLOGÍA ENAM: EPOC POR TABAQUISMO PASIVO", "NEUMOLOGÍA",
  ("Causas de EPOC", ["El tabaco es la principal, también el humo ajeno",
   "Otras: humo de leña (biomasa), exposición laboral, déficit de alfa-1 antitripsina"]),
  ("Mujer de 62 años, ama de casa, con EPOC", ["35 años casada con un fumador pesado", "Asma en la infancia que desapareció"]),
  {"rotulo": "Mapa del tema", "centro": "EPOC", "centro_sub": "¿De dónde viene?", "ans": 0,
   "items": [("FUMADORA PASIVA", ["35 años de humo en casa", "Exposición crónica"]),
             ("Tabaquismo activo", ["Causa principal en el mundo"]),
             ("Humo de biomasa", ["Leña, cocinas sin chimenea"]),
             ("Exposición laboral", ["Polvos, gases, minería"]),
             ("Déficit de alfa-1 antitripsina", ["Joven, enfisema basal"])],
   "ruta": ["No fuma", "Esposo fumador pesado", "35 años de exposición", "FUMADORA PASIVA"]},
  ["El asma infantil resuelta no explica una EPOC en la adultez.",
   "Preguntar siempre por humo de leña en mujeres rurales.",
   "Confirmación: espirometría con VEF₁/CVF < 0,7 posbroncodilatador."],
  "GOLD – Global Strategy for the Diagnosis, Management and Prevention of COPD (2025)")

# NEU-051 · tarjetas
V("tarjetas", "NEU-051", "neumonia-nosocomial-complicacion-insuficiencia-respiratoria", "Complicaciones de la neumonía nosocomial",
  "NEUMOLOGÍA ENAM: NEUMONÍA INTRAHOSPITALARIA", "NEUMOLOGÍA",
  ("Neumonía nosocomial", ["Aparece ≥ 48 h tras el ingreso, con gérmenes más resistentes",
   "Lo más frecuente es que evolucione a insuficiencia respiratoria"]),
  ("Pregunta de neumología", ["¿Complicación y secuela más frecuente?"]),
  {"rotulo": "¿Cuál es la más frecuente?", "ans": 0, "cards": [
      {"titulo": "INSUFICIENCIA RESPIRATORIA", "datos": [
          ("Frecuencia", "La más frecuente", True), ("Causa", "Daño alveolar extenso", True),
          ("Manejo", "O₂, VNI, ventilación", False)],
       "pie": "Principal causa de muerte"},
      {"titulo": "Empiema", "datos": [
          ("Frecuencia", "Menos frecuente", False), ("Causa", "Pus en la pleura", False),
          ("Manejo", "Tubo de drenaje", False)],
       "pie": "Derrame con pH < 7,2"},
      {"titulo": "Absceso pulmonar", "datos": [
          ("Frecuencia", "Poco frecuente", False), ("Causa", "Necrosis con cavidad", False),
          ("Manejo", "Antibiótico prolongado", False)],
       "pie": "Anaerobios, S. aureus"},
      {"titulo": "Hemotórax", "datos": [
          ("Frecuencia", "Rara", False), ("Causa", "Trauma o procedimiento", False),
          ("Manejo", "Tubo de tórax", False)],
       "pie": "No es complicación típica"}]},
  ["Gérmenes: Pseudomonas, S. aureus (SARM), Klebsiella, Acinetobacter.",
   "Cubrir según la flora del hospital y el riesgo de multirresistencia.",
   "Prevención: cabecera a 30-45°, higiene de manos y oral."],
  "IDSA/ATS – Management of hospital-acquired and ventilator-associated pneumonia (2016)")

# PED-168 · tarjetas
V("tarjetas", "PED-168", "neonato-meningitis-bacilos-gram-positivos-listeria", "Meningitis neonatal: el Gram orienta",
  "PEDIATRÍA ENAM: MENINGITIS NEONATAL POR LISTERIA", "PEDIATRÍA",
  ("Meningitis neonatal", ["Gérmenes: estreptococo del grupo B, E. coli y Listeria",
   "Bacilos grampositivos en el LCR = Listeria monocytogenes"]),
  ("Neonato de 7 días", ["Fiebre, pobre succión, fontanela abombada", "Convulsiona · LCR con bacilos grampositivos"]),
  {"rotulo": "¿Qué germen tiene esa forma?", "ans": 0, "cards": [
      {"titulo": "LISTERIA", "datos": [
          ("Gram", "BACILO GRAMPOSITIVO", True), ("Fuente", "Lácteos, embutidos", False),
          ("Cubre", "Ampicilina", False)],
       "pie": "Resiste a cefalosporinas"},
      {"titulo": "S. agalactiae", "datos": [
          ("Gram", "Coco + en cadenas", False), ("Fuente", "Canal de parto", False),
          ("Cubre", "Ampicilina", False)],
       "pie": "El más frecuente"},
      {"titulo": "E. coli", "datos": [
          ("Gram", "Bacilo negativo", False), ("Fuente", "Canal de parto", False),
          ("Cubre", "Gentamicina, cefotaxima", False)],
       "pie": "Cápsula K1"},
      {"titulo": "Meningococo", "datos": [
          ("Gram", "Diplococo negativo", False), ("Fuente", "Vía aérea", False),
          ("Cubre", "Ceftriaxona", False)],
       "pie": "Raro en el neonato"}]},
  ["Por Listeria, el esquema neonatal siempre incluye ampicilina.",
   "Listeria se asocia a madres que consumieron lácteos no pasteurizados.",
   "Las cefalosporinas solas no cubren Listeria."],
  "AAP – Red Book: Report of the Committee on Infectious Diseases (2024) · " + NELSON)

# PED-169 · árbol
A("PED-169", "lactante-disenteria-deshidratado-somnoliento-ceftriaxona", "Diarrea con sangre en el lactante",
  "PEDIATRÍA ENAM: DISENTERÍA CON COMPROMISO SISTÉMICO", "PEDIATRÍA",
  ("Disentería en el niño", ["Diarrea con moco y sangre, fiebre, pujo y tenesmo: bacteria invasiva",
   "Lactante con compromiso sistémico: hospitalizar y antibiótico EV"]),
  ("Lactante de 9 meses con 4 días de fiebre", ["Deposiciones con moco y sangre, pujo y tenesmo", "Deshidratación moderada, somnoliento, abdomen distendido"]),
  Q("¿Compromiso sistémico o menor de 1 año grave?", [
      L("Sí", "CEFTRIAXONA EV", ["Hospitalizar e hidratar", "Coprocultivo antes"], path=True),
      L("No", "Antibiótico oral", ["Azitromicina o ciprofloxacino", "3-5 días"])], path=True),
  ("Antibióticos en la disentería", [("Ceftriaxona", True), ("Ampicilina", False), ("Cloranfenicol", False)], [
      ("Shigella", ["Sensible", "Alta resistencia", "Resistencia y toxicidad"]),
      ("Uso actual", ["Grave, hospitalizado", "No recomendada", "No recomendado"])]),
  ["Shigella es la causa principal de disentería en niños.",
   "No usar antidiarreicos ni loperamida en la disentería.",
   "Reevaluar a las 48 h: si no mejora, ajustar según antibiograma."],
  "OMS – Tratamiento de la diarrea: manual para médicos (2005) · " + NELSON)

# PED-170 · embudo
V("embudo", "PED-170", "rn-2-dias-ictericia-bilirrubina-directa-leucopenia-sepsis", "Ictericia con bilirrubina directa alta",
  "PEDIATRÍA ENAM: SEPSIS NEONATAL CON COLESTASIS", "PEDIATRÍA",
  ("Ictericia neonatal patológica", ["Bilirrubina directa > 1-2 mg/dl nunca es fisiológica",
   "Con hipotonía, succión pobre y leucopenia: sepsis"]),
  ("RN de 2 días, parto domiciliario, sin control prenatal", ["Succión pobre, somnoliento, hipotónico", "Ictericia hasta ingle · leucocitos 5000 · BD 6 mg/dl"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Ictericia en un recién nacido de 2 días",
   "candidatos": ["Sepsis neonatal", "Ictericia fisiológica", "Por lactancia materna", "Hepatitis neonatal"],
   "pasos": [("Bilirrubina directa alta (colestasis)", ["Ictericia fisiológica", "Por lactancia materna"]),
             ("Hipotonía, somnolencia, leucopenia a los 2 días", ["Hepatitis neonatal"])],
   "final": ("SEPSIS NEONATAL", ["Hemocultivo, PCR, hemograma", "Ampicilina + gentamicina"]),
   "nota": "La leucopenia (< 5000) en el neonato es un signo de infección grave."},
  ["La ictericia fisiológica es de bilirrubina indirecta y aparece después de 24 h.",
   "Parto domiciliario sin control prenatal: alto riesgo de infección.",
   "Descartar también infección urinaria y TORCH."],
  NELSON + " · AAP – Management of neonates with suspected early-onset sepsis (2018)")

# PED-171 · puntaje
V("puntaje", "PED-171", "prematuro-33-sem-quejido-aleteo-silverman-8", "Dificultad respiratoria del recién nacido",
  "PEDIATRÍA ENAM: ESCALA DE SILVERMAN-ANDERSEN", "PEDIATRÍA",
  ("Escala de Silverman-Andersen", ["Cinco signos, cada uno de 0 a 2 puntos",
   "A más puntaje, más dificultad respiratoria"]),
  ("RN de 33 semanas a la hora de vida", ["FR 90 · quejido audible sin estetoscopio · aleteo intenso", "Tiraje intercostal, retracción xifoidea leve, disociación toracoabdominal"]),
  {"rotulo": "Silverman en el caso", "escala": "Silverman-Andersen", "total": 8, "max": 10,
   "total_label": "Puntaje del caso",
   "interpreta": "Dificultad respiratoria grave",
   "items": [("Quejido audible sin estetoscopio", "2", True), ("Aleteo nasal intenso", "2", True),
             ("Disociación toracoabdominal", "2", True), ("Tiraje intercostal apenas visible", "1", True),
             ("Retracción xifoidea leve", "1", True)],
   "bandas": [("0", "Sin dificultad", "Observación", False),
              ("1-3", "Leve", "Oxígeno", False),
              ("4-6", "Moderada", "CPAP", False),
              ("7-10", "Grave", "Ventilación y surfactante", True)]},
  ["La frecuencia respiratoria no forma parte de la escala.",
   "Causa probable en un prematuro de 33 semanas: membrana hialina.",
   "Evaluar la escala en forma seriada para ver la evolución."],
  "Silverman WA, Andersen DH (Pediatrics 1956) · European Consensus Guidelines on the management of RDS (2022)")

# SP-126 · árbol
A("SP-126", "nino-hematoma-epidural-sin-familia-jefe-guardia-autoriza", "Cirugía urgente sin familiares",
  "SALUD PÚBLICA ENAM: CONSENTIMIENTO EN LA EMERGENCIA", "SALUD PÚBLICA",
  ("Consentimiento informado en la emergencia", ["Si hay riesgo de muerte y no hay quién autorice, no se espera",
   "El jefe de guardia autoriza y lo deja escrito en la historia clínica"]),
  ("Niño de 12 años en coma", ["Hematoma epidural por accidente de tránsito", "Necesita cirugía urgente · no hay familiares"]),
  Q("¿Hay riesgo inminente para la vida?", [
      Q("¿Hay familiar o representante?", [
          L("Sí", "Consentimiento del representante", ["Padres o tutor"]),
          L("No", "JEFE DE GUARDIA AUTORIZA", ["Consta en la historia clínica", "Operar sin demora"], path=True)],
        edge="Sí", path=True),
      L("No", "Esperar el consentimiento", ["Ubicar a los padres"])], path=True),
  ("¿Quién decide?", [("Jefe de guardia", True), ("Fiscal", False), ("Cirujano solo", False)], [
      ("Papel", ["Autoriza y registra", "No autoriza cirugías", "Ejecuta, no autoriza solo"]),
      ("Base", ["Ley General de Salud, art. 4", "Interviene después si hay delito", "Necesita respaldo institucional"])]),
  ["El hematoma epidural puede matar en horas: la demora no es aceptable.",
   "Se informa a la familia apenas llegue.",
   "La emergencia es una excepción legal al consentimiento."],
  "Ley N.° 26842 – Ley General de Salud (art. 4 y 40) · Ley N.° 29414 – Derechos de los usuarios de los servicios de salud")

# PED-172 · fases
V("fases", "PED-172", "lactante-no-vacunado-tos-paroxistica-gallo-tos-ferina", "Etapas de la tos ferina",
  "PEDIATRÍA ENAM: TOS FERINA", "PEDIATRÍA",
  ("Tos ferina (Bordetella pertussis)", ["Accesos de tos, estridor inspiratorio 'de gallo', cianosis y vómitos",
   "Más grave en niños no vacunados y lactantes pequeños"]),
  ("Niño de 12 meses sin vacunas", ["Una semana de accesos de tos", "Ruido inspiratorio como de gallo, sofocación y cianosis"]),
  {"rotulo": "Curso de la enfermedad", "ans": 1,
   "fases": [("Catarral", "1-2 semanas", "Resfrío", ["La más contagiosa"]),
             ("Paroxística", "2-6 semanas", "ACCESOS + GALLO", ["Cianosis, vómitos", "Apneas en lactantes"]),
             ("Convalecencia", "Semanas-meses", "La tos disminuye", ["Puede recaer con virus"])],
   "curvas": [("Intensidad de la tos", ROSE, [0.15, 0.25, 0.7, 0.95, 0.8, 0.45, 0.2]),
              ("Contagio", AMBER, [0.9, 0.8, 0.5, 0.3, 0.15, 0.05, 0.0])],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Tos ferina", True), ("Bronquiolitis", False), ("Neumonía", False), ("Faringolaringitis", False)]},
  ["Tratamiento: azitromicina, y también a los contactos.",
   "Hemograma: leucocitosis con linfocitosis marcada.",
   "Prevención: pentavalente y vacuna dTpa en la gestante."],
  "CDC – Pertussis: clinical overview (2024) · MINSA – NTS de vigilancia de tos ferina · " + NELSON)

# PSI-034 · radial
V("radial", "PSI-034", "adolescente-bipolar-riesgo-suicida-agresion-sexual", "Riesgo suicida en el adolescente",
  "PSIQUIATRÍA ENAM: FACTORES DE RIESGO SUICIDA", "PSIQUIATRÍA",
  ("Suicidio en adolescentes", ["Se suman el trastorno mental y los eventos traumáticos",
   "El abuso o la agresión sexual es de los factores más potentes"]),
  ("Adolescente con cambios bipolares del ánimo", ["Pasa de impulsivo y agresivo a depresión intensa", "¿Qué factor aumenta más su riesgo?"]),
  {"rotulo": "Mapa del tema", "centro": "RIESGO SUICIDA", "centro_sub": "Adolescente", "ans": 0,
   "items": [("AGRESIÓN SEXUAL", ["Trauma grave, vergüenza", "Multiplica el riesgo"]),
             ("Intento previo", ["El predictor más fuerte"]),
             ("Trastorno afectivo", ["Depresión, bipolaridad"]),
             ("Consumo de sustancias", ["Alcohol, drogas"]),
             ("Acoso escolar", ["Aislamiento, humillación"])],
   "ruta": ["Trastorno bipolar", "Impulsividad y depresión", "Trauma sexual", "RIESGO MÁXIMO"]},
  ["Pertenecer a un grupo religioso es un factor protector.",
   "Preguntar directamente por ideas suicidas no aumenta el riesgo.",
   "Riesgo alto: no dejarlo solo y derivar a psiquiatría."],
  "OMS – LIVE LIFE: guía para la prevención del suicidio (2021) · AACAP – Practice parameter on suicidal behavior")

# NEF-072 · embudo
V("embudo", "NEF-072", "nino-colico-hematuria-sin-fiebre-litiasis", "Dolor cólico con hematuria en un niño",
  "UROLOGÍA ENAM: LITIASIS URINARIA EN EL NIÑO", "UROLOGÍA",
  ("Litiasis urinaria", ["Dolor cólico intenso + hematuria, sin fiebre",
   "En niños el dolor puede ser abdominal difuso"]),
  ("Niño de 9 años", ["Dolor cólico agudo e intenso en todo el abdomen", "Polaquiuria, tenesmo · sin fiebre · muchos hematíes"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dolor abdominal con síntomas urinarios",
   "candidatos": ["Litiasis renal", "Pielonefritis", "Cistitis", "Uretritis"],
   "pasos": [("Sin fiebre", ["Pielonefritis"]),
             ("Dolor cólico intenso con hematuria abundante", ["Cistitis", "Uretritis"])],
   "final": ("LITIASIS URINARIA", ["Ecografía renal y vesical", "Analgesia, hidratación, estudio metabólico"]),
   "nota": "Los síntomas bajos (polaquiuria, tenesmo) aparecen cuando el cálculo llega a la unión vesical."},
  ["En niños siempre buscar causa metabólica o malformación.",
   "La TC sin contraste se reserva si la ecografía no aclara.",
   "Cálculos < 5 mm suelen expulsarse solos."],
  "EAU – Guidelines on paediatric urology: urolithiasis (2025) · " + NELSON)

# REU-053 · fases
V("fases", "REU-053", "escolar-liendres-hermano-prurito-permetrina", "Pediculosis: plan de tratamiento",
  "DERMATOLOGÍA ENAM: PEDICULOSIS DE LA CABEZA", "DERMATOLOGÍA",
  ("Pediculosis capitis", ["Prurito del cuero cabelludo + liendres adheridas al pelo",
   "Contagio por contacto directo: tratar a toda la familia afectada"]),
  ("Escolar que se rasca la cabeza", ["Cuerpos ovoides blanquecinos pegados al cabello", "El hermano menor tiene lo mismo"]),
  {"rotulo": "Esquema de tratamiento", "ans": 0,
   "fases": [("Día 1", "Aplicar", "PERMETRINA 1 %", ["Loción en pelo seco, 10 min", "Luego enjuagar"]),
             ("Día 1-2", "Mecánico", "Peine fino", ["Retirar liendres"]),
             ("Día 7-10", "Repetir", "2.ª aplicación", ["Mata las ninfas nuevas"]),
             ("Familia", "Contactos", "Revisar a todos", ["Tratar solo a los infestados"])],
   "curvas": [],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Permetrina", True), ("Vinagre", False), ("Violeta de genciana", False), ("Sulfuro de selenio", False)]},
  ["El vinagre ayuda a soltar liendres, pero no mata piojos.",
   "Si falla: malatión o ivermectina.",
   "No hace falta cortar el pelo ni fumigar la casa."],
  "AAP – Clinical report: Head lice (Pediatrics 2022) · CDC – Head lice treatment (2024)")

# PED-173 · tarjetas
V("tarjetas", "PED-173", "escolar-faringitis-estreptococo-grupo-a", "Grupos de estreptococos",
  "PEDIATRÍA ENAM: ESTREPTOCOCO DEL GRUPO A", "PEDIATRÍA",
  ("Estreptococos beta-hemolíticos", ["Se agrupan por Lancefield según el carbohidrato de su pared",
   "Faringitis bacteriana del escolar: grupo A (S. pyogenes)"]),
  ("Escolar con faringitis estreptocócica", ["¿Qué grupo es el más frecuente?"]),
  {"rotulo": "¿Qué grupo causa qué?", "ans": 0, "cards": [
      {"titulo": "GRUPO A", "datos": [
          ("Especie", "S. pyogenes", True), ("Cuadro", "FARINGITIS, IMPÉTIGO", True),
          ("Secuela", "Fiebre reumática, GN", False)],
       "pie": "Penicilina o amoxicilina"},
      {"titulo": "Grupo B", "datos": [
          ("Especie", "S. agalactiae", False), ("Cuadro", "Sepsis neonatal", False),
          ("Secuela", "Meningitis", False)],
       "pie": "Tamizaje en la gestante"},
      {"titulo": "Grupos C y G", "datos": [
          ("Especie", "S. dysgalactiae", False), ("Cuadro", "Faringitis ocasional", False),
          ("Secuela", "Sin fiebre reumática", False)],
       "pie": "Adolescentes y adultos"},
      {"titulo": "Grupo D", "datos": [
          ("Especie", "Enterococo, S. bovis", False), ("Cuadro", "ITU, endocarditis", False),
          ("Secuela", "Cáncer de colon (bovis)", False)],
       "pie": "No causa faringitis"}]},
  ["Solo el grupo A se asocia a fiebre reumática.",
   "La glomerulonefritis puede seguir a faringitis o impétigo.",
   "Tratar 10 días previene la fiebre reumática."],
  "IDSA – Clinical practice guideline for group A streptococcal pharyngitis (2012) · " + NELSON)

# PED-174 · árbol
A("PED-174", "lactante-9-meses-pentavalente-pendiente-rotavirus-fuera-edad", "Vacunas atrasadas",
  "PEDIATRÍA ENAM: VACUNACIÓN ATRASADA", "PEDIATRÍA",
  ("Esquema atrasado", ["No se reinicia: se completa lo que falta",
   "La vacuna de rotavirus tiene edad límite; pasada esa edad no se aplica"]),
  ("Lactante de 9 meses", ["Le falta la 3.ª dosis de pentavalente", "Solo recibió 1 dosis de rotavirus"]),
  Q("¿La vacuna tiene edad límite superada?", [
      L("Sí: rotavirus", "No aplicar rotavirus", ["Riesgo de invaginación en mayores", "Pasó la edad máxima"]),
      L("No: pentavalente", "SOLO 3.ª DOSIS DE PENTAVALENTE", ["Completar sin reiniciar", "Dosis aplicadas siguen válidas"], path=True)], path=True),
  ("Vacunas del caso", [("Pentavalente", True), ("Rotavirus", False)], [
      ("Edad límite", ["Hasta los 4 años", "Menor de 8 meses"]),
      ("Conducta", ["Completar", "No aplicar"])]),
  ["'Dosis puesta, dosis que cuenta': nunca reiniciar el esquema.",
   "El rotavirus se aplica a los 2 y 4 meses.",
   "Aprovechar toda consulta para poner las vacunas pendientes."],
  "MINSA – NTS 196: Esquema nacional de vacunación (2022) · OMS – Position paper on rotavirus vaccines (2021)")

# HEM-034 · matriz
V("matriz", "HEM-034", "nino-palidez-reticulocitos-altos-haptoglobina-baja-hemolisis", "Anemia: ¿se destruye o no se produce?",
  "HEMATOLOGÍA ENAM: ANEMIA HEMOLÍTICA", "HEMATOLOGÍA",
  ("Anemia hemolítica", ["La médula responde: reticulocitos altos",
   "La destrucción libera hemoglobina: bilirrubina indirecta y LDH altas, haptoglobina baja"]),
  ("Niño de 10 años con palidez marcada", ["Bilirrubina indirecta alta", "Reticulocitos altos · haptoglobina baja"]),
  {"rotulo": "Causa y laboratorio", "eje_x": "Rasgo", "eje_y": "Causa",
   "cols": ["Reticulocitos", "Bilirrubina y haptoglobina"], "rows": ["Hemólisis", "Insuficiencia renal", "Déficit nutricional", "Falla medular"], "caso": (0, 0),
   "cells": [[("ALTOS", ["La médula compensa"]), ("BI alta, haptoglobina baja", [])],
             [("Bajos", ["Falta eritropoyetina"]), ("Normales", [])],
             [("Bajos", ["Hierro, B12, folato"]), ("Normales", [])],
             [("Bajos", ["Aplasia, infiltración"]), ("Normales", [])]]},
  ["En niños: esferocitosis, déficit de G6PD, drepanocitosis y autoinmune.",
   "Coombs directo positivo = hemólisis autoinmune.",
   "El frotis orienta: esferocitos, esquistocitos, drepanocitos."],
  NELSON + " · British Society for Haematology – Guideline on autoimmune haemolytic anaemia (2017)")

# PED-175 · termómetro
V("termometro", "PED-175", "rn-6-dias-fiebre-fontanela-abombada-ampicilina-gentamicina", "Meningitis: antibiótico según la edad",
  "PEDIATRÍA ENAM: MENINGITIS NEONATAL", "PEDIATRÍA",
  ("Meningitis en el recién nacido", ["Gérmenes: estreptococo B, E. coli y Listeria",
   "Esquema empírico: ampicilina + gentamicina (o cefotaxima)"]),
  ("RN de 6 días sin control prenatal", ["4 días de fiebre, irritable, fontanela abombada", "Leucocitos 25 000 · plaquetas 80 000 · PCR alta"]),
  {"rotulo": "Edad del paciente",
   "niveles": [("< 1 mes", "Neonato", ["RN DE 6 DÍAS", "SGB, E. coli, Listeria"]),
               ("1-3 meses", "Lactante pequeño", ["Mezcla neonatal y neumococo"]),
               ("> 3 meses", "Niño", ["Neumococo, meningococo"])],
   "caso_nivel": 0, "ruta_titulo": "Esquema empírico", "paso_label": "PASO",
   "pasos": [(1, "Ampicilina + gentamicina", ["O ampicilina + cefotaxima si hay meningitis clara"], True),
             (2, "1-3 meses: ampicilina + cefotaxima", ["Cubre Listeria y neumococo"], False),
             (3, "> 3 meses: ceftriaxona + vancomicina", ["Neumococo resistente"], False)]},
  ["La ampicilina es clave: cubre Listeria, que resiste a las cefalosporinas.",
   "La ceftriaxona se evita en neonatos ictéricos.",
   "Punción lumbar para confirmar y ajustar la duración."],
  NELSON + " · IDSA – Practice guidelines for bacterial meningitis (2004; actualización 2024)")

# PED-176 · embudo
V("embudo", "PED-176", "rn-salivacion-sonda-no-pasa-sin-gas-atresia-esofago", "Recién nacido que se ahoga al comer",
  "PEDIATRÍA ENAM: ATRESIA DE ESÓFAGO", "PEDIATRÍA",
  ("Atresia de esófago", ["Polihidramnios, salivación excesiva, tos y ahogo con la primera toma",
   "La sonda no pasa; sin gas abdominal = sin fístula distal"]),
  ("Lactante en un centro del primer nivel", ["Salivación, tos y ahogo al tomar leche", "Madre con polihidramnios · no pasa la sonda · sin gas abdominal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Ahogo y salivación con la alimentación",
   "candidatos": ["Atresia de esófago", "Reflujo gastroesofágico", "Fístula en H", "Trastorno de deglución"],
   "pasos": [("La sonda nasogástrica no pasa", ["Reflujo gastroesofágico", "Fístula en H", "Trastorno de deglución"])],
   "final": ("ATRESIA DE ESÓFAGO SIN FÍSTULA DISTAL", ["Suspender la vía oral", "Sonda de aspiración, cabecera elevada, referir"]),
   "nota": "Con gas en el abdomen hay fístula traqueoesofágica distal (la forma más común)."},
  ["Dar leche aumenta el riesgo de neumonía aspirativa.",
   "Buscar asociación VACTERL.",
   "La cirugía se hace en un centro con cirugía pediátrica."],
  NELSON + " · Holcomb and Ashcraft's Pediatric Surgery 7.ª ed. (2020)")

# TRA-037 · termómetro
V("termometro", "TRA-037", "alud-fractura-conminuta-tibia-expuesta-tierra-desbridamiento", "Fractura expuesta",
  "TRAUMATOLOGÍA ENAM: FRACTURA EXPUESTA DE TIBIA", "TRAUMATOLOGÍA",
  ("Fracturas expuestas", ["Clasificación de Gustilo según herida, contaminación y daño de tejidos",
   "Prioridad: evitar la infección con lavado y desbridamiento"]),
  ("Minero de 24 años tras un alud de piedras", ["Herida de todo el tercio medio de la pierna", "Músculo y hueso expuestos con tierra · fractura conminuta"]),
  {"rotulo": "Tipo de Gustilo",
   "niveles": [("I", "Herida < 1 cm", ["Limpia"]),
               ("II", "Herida 1-10 cm", ["Daño moderado de partes blandas"]),
               ("III", "Herida > 10 cm", ["CONTAMINADA, CONMINUTA", "Alto riesgo de infección"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Irrigación y desbridamiento", ["En quirófano, en las primeras horas", "Con antibiótico EV y antitetánica"], True),
             (2, "Estabilizar la fractura", ["Fijador externo"], False),
             (3, "Cobertura de partes blandas", ["Colgajos o injertos"], False)]},
  ["Antibiótico: cefazolina; en tipo III agregar gentamicina.",
   "El yeso cerrado sobre una herida contaminada está contraindicado.",
   "Revisar pulsos y nervios: el IIIC tiene lesión arterial."],
  "BOAST 4 – The management of severe open lower limb fractures (2017) · " + ATLS)

# TRA-038 · termómetro
V("termometro", "TRA-038", "torcedura-tobillo-equimosis-inestabilidad-esguince-grado-2", "Esguince de tobillo",
  "TRAUMATOLOGÍA ENAM: ESGUINCE DE TOBILLO", "TRAUMATOLOGÍA",
  ("Esguince lateral del tobillo", ["Mecanismo de inversión: se lesiona el peroneoastragalino anterior",
   "El grado depende de la rotura y la estabilidad"]),
  ("Varón de 23 años tras una torcedura", ["Dolor y dificultad para caminar", "Edema, equimosis lateral, inestabilidad moderada"]),
  {"rotulo": "Grado del esguince",
   "niveles": [("I", "Distensión", ["Sin inestabilidad, camina"]),
               ("II", "Rotura parcial", ["EQUIMOSIS + INESTABILIDAD MODERADA", "Le cuesta caminar"]),
               ("III", "Rotura completa", ["Inestable, no apoya"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Reposo relativo, hielo, compresión, elevación", ["Ortesis o vendaje funcional", "AINE"], True),
             (2, "Carga progresiva", ["Según tolere"], False),
             (3, "Rehabilitación propioceptiva", ["Evita recaídas"], False)]},
  ["Reglas de Ottawa: Rx si no puede apoyar o duele el borde posterior de los maléolos.",
   "La inmovilización rígida prolongada retrasa la recuperación.",
   "Fractura de escafoides es de la muñeca, no del tobillo."],
  "KNGF – Clinical practice guideline for ankle sprain (Br J Sports Med 2018)")

# CIR-096 · matriz
V("matriz", "CIR-096", "quemadura-sin-dolor-tercer-grado", "Profundidad de las quemaduras",
  "CIRUGÍA ENAM: QUEMADURA DE TERCER GRADO", "CIRUGÍA",
  ("Quemadura de espesor total", ["Destruye epidermis, dermis y terminaciones nerviosas",
   "Por eso es indolora, blanca o acartonada"]),
  ("Pregunta de cirugía", ["¿Qué quemadura no duele?"]),
  {"rotulo": "Grado y características", "eje_x": "Rasgo", "eje_y": "Grado",
   "cols": ["Aspecto", "Dolor"], "rows": ["Primer grado", "Segundo superficial", "Segundo profundo", "Tercer grado"], "caso": (3, 1),
   "cells": [[("Eritema", ["Sin ampollas"]), ("Doloroso", [])],
             [("Ampollas, rosado húmedo", []), ("Muy doloroso", [])],
             [("Blanco-rojizo, seco", []), ("Hipoestesia", [])],
             [("Blanco o negro, acartonado", ["Escara"]), ("INDOLORO", ["Nervios destruidos"])]]},
  ["El tercer grado necesita injerto: no cicatriza solo.",
   "Los bordes de una quemadura de tercer grado sí duelen (son de menor grado).",
   "Escarotomía si una escara circular compromete la circulación o la respiración."],
  ATLS + " · ABA – Advanced Burn Life Support (2022)")

# CIR-097 · fases
V("fases", "CIR-097", "poscolecistectomia-ictericia-via-dilatada-colangioresonancia", "Ictericia después de la colecistectomía",
  "CIRUGÍA ENAM: LESIÓN O LITIASIS RESIDUAL DE LA VÍA BILIAR", "CIRUGÍA",
  ("Ictericia poscolecistectomía", ["Causas: cálculo residual, estenosis o lesión de la vía biliar",
   "Se estudia primero con un método no invasivo: colangio-RM"]),
  ("Mujer de 23 años operada hace 2 meses", ["Dolor en hipocondrio derecho, coluria, ictericia", "Ecografía: vías biliares dilatadas"]),
  {"rotulo": "Secuencia de estudio", "ans": 1,
   "fases": [("Ecografía", "Primer paso", "Vía dilatada", ["Confirma obstrucción"]),
             ("Colangio-RM", "Diagnóstico", "MAPA DE LA VÍA BILIAR", ["No invasiva", "Cálculo, estenosis o lesión"]),
             ("CPRE", "Terapéutica", "Extraer o colocar stent", ["Solo si hay algo que tratar"]),
             ("Cirugía", "Si hace falta", "Hepaticoyeyunostomía", ["Lesiones complejas"])],
   "curvas": [],
   "chips_titulo": "Indicación · marcada la correcta",
   "chips": [("Colangiorresonancia", True), ("CPRE directa", False), ("Explorar la vía", False), ("Laparoscopia", False)]},
  ["La CPRE tiene riesgo de pancreatitis: se usa cuando ya se sabe qué tratar.",
   "Coledocolitiasis residual: cálculo que quedó en el colédoco.",
   "Lesión de la vía biliar: complicación grave de la colecistectomía."],
  "ASGE – Guideline on the role of endoscopy in the evaluation and management of choledocholithiasis (2019)")

# CIR-098 · tarjetas
V("tarjetas", "CIR-098", "anciano-87-colecistitis-sin-mejoria-colecistostomia-percutanea", "Colecistitis en un paciente frágil",
  "CIRUGÍA ENAM: COLECISTITIS AGUDA DE ALTO RIESGO", "CIRUGÍA",
  ("Colecistitis en alto riesgo quirúrgico", ["Si no mejora con antibióticos y no tolera la cirugía:",
   "drenaje percutáneo de la vesícula (colecistostomía)"]),
  ("Varón de 87 años con bronquitis crónica e ICC descompensada", ["Colecistitis aguda litiásica infectada", "4 días de tratamiento: sigue con fiebre, dolor y leucocitosis"]),
  {"rotulo": "¿Qué conducta conviene?", "ans": 0, "cards": [
      {"titulo": "COLECISTOSTOMÍA PERCUTÁNEA", "datos": [
          ("Riesgo", "Bajo, anestesia local", True), ("Controla", "El foco séptico", True),
          ("Para quién", "Alto riesgo quirúrgico", True)],
       "pie": "Colecistectomía diferida si mejora"},
      {"titulo": "Colecistectomía urgente", "datos": [
          ("Riesgo", "Muy alto aquí", False), ("Controla", "Definitivo", False),
          ("Para quién", "Paciente apto", False)],
       "pie": "Ideal en bajo riesgo"},
      {"titulo": "Cambiar antibiótico", "datos": [
          ("Riesgo", "Bajo", False), ("Controla", "No drena el pus", False),
          ("Para quién", "Complemento", False)],
       "pie": "Insuficiente solo"},
      {"titulo": "Seguir igual", "datos": [
          ("Riesgo", "Perforación", False), ("Controla", "No", False),
          ("Para quién", "Nadie en este caso", False)],
       "pie": "Ya fracasó"}]},
  ["Guías de Tokio: grado III o comorbilidad grave = drenaje de la vesícula.",
   "Se mantiene el antibiótico junto con el drenaje.",
   "Alternativa: drenaje endoscópico por ecoendoscopia."],
  "Tokyo Guidelines 2018 – Management of acute cholecystitis (J Hepatobiliary Pancreat Sci 2018)")

# GAS-061 · embudo
V("embudo", "GAS-061", "anciana-ictericia-vesicula-palpable-sin-calculos-tomografia", "Vesícula palpable con ictericia",
  "GASTROENTEROLOGÍA ENAM: SIGNO DE COURVOISIER", "GASTROENTEROLOGÍA",
  ("Ictericia obstructiva no litiásica", ["Vesícula grande y palpable + ictericia = obstrucción distal lenta (Courvoisier)",
   "Sugiere tumor periampular: se confirma con TC"]),
  ("Mujer de 78 años", ["Dolor, anorexia, baja de peso, prurito, ictericia", "Masa en hipocondrio derecho · eco: vesícula grande sin cálculos"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Ictericia con vesícula distendida",
   "candidatos": ["Tumor periampular", "Coledocolitiasis", "Colecistitis aguda", "Hepatitis"],
   "pasos": [("Vesícula sin cálculos", ["Coledocolitiasis", "Colecistitis aguda"]),
             ("Vesícula grande, baja de peso en una anciana", ["Hepatitis"])],
   "final": ("TUMOR PERIAMPULAR", ["TC de abdomen con contraste", "Páncreas, colédoco distal, ampolla"]),
   "nota": "En la litiasis la vesícula suele estar fibrosada y no se distiende."},
  ["La TC estadifica y define si es resecable.",
   "La colangio-RM y la CPRE vienen después, según lo que muestre la TC.",
   "La gammagrafía HIDA sirve para colecistitis aguda."],
  "NCCN – Pancreatic adenocarcinoma (2025) · ACG – Guideline: evaluation of abnormal liver chemistries (2017)")

# OFT-039 · radial
V("radial", "OFT-039", "nadador-otalgia-traccion-pabellon-pseudomonas", "Infecciones del oído",
  "OTORRINOLARINGOLOGÍA ENAM: OTITIS EXTERNA AGUDA", "OTORRINOLARINGOLOGÍA",
  ("Otitis externa ('del nadador')", ["La humedad macera el conducto y entra Pseudomonas aeruginosa",
   "Dolor al traccionar el pabellón o presionar el trago"]),
  ("Varón de 17 años tras nadar en piscina", ["Otalgia, secreción seropurulenta e hipoacusia", "Dolor al jalar la oreja · conducto edematoso"]),
  {"rotulo": "Mapa del tema", "centro": "OTALGIA", "centro_sub": "¿Qué oído y qué germen?", "ans": 0,
   "items": [("OTITIS EXTERNA AGUDA", ["Pseudomonas aeruginosa", "Tracción del pabellón dolorosa"]),
             ("Forunculosis del conducto", ["S. aureus, lesión localizada"]),
             ("Otitis media aguda", ["Neumococo, H. influenzae"]),
             ("Otomicosis", ["Aspergillus, prurito"]),
             ("Otitis externa maligna", ["Diabético anciano, Pseudomonas"])],
   "ruta": ["Piscina", "Conducto húmedo e inflamado", "Tracción dolorosa", "PSEUDOMONAS"]},
  ["Tratamiento: gotas de ciprofloxacino ± corticoide; mantener seco.",
   "Si el edema impide el paso de las gotas: colocar una mecha.",
   "Diabético con dolor intenso y granulación: descartar otitis externa maligna."],
  "AAO-HNS – Clinical practice guideline: acute otitis externa (2014)")

# GIN-164 · embudo
V("embudo", "GIN-164", "34-semanas-contracciones-sin-cambios-cervicales-observar", "Contracciones en el pretérmino",
  "OBSTETRICIA ENAM: FALSO TRABAJO DE PARTO", "OBSTETRICIA",
  ("Contracciones antes del término", ["Si el cuello no cambia no hay trabajo de parto",
   "Se observa y se reevalúa antes de dar tocolíticos o corticoides"]),
  ("Gestante de 34 semanas", ["Dolor y contracciones cada 10 minutos, esporádicas", "Afebril · cuello: 0 cm, 0 %, presentación flotante"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Contracciones a las 34 semanas",
   "candidatos": ["Contracciones sin cambio cervical", "Trabajo de parto pretérmino", "Corioamnionitis", "Desprendimiento"],
   "pasos": [("Afebril, sin sangrado ni dolor continuo", ["Corioamnionitis", "Desprendimiento"]),
             ("Cuello sin dilatación ni borramiento", ["Trabajo de parto pretérmino"])],
   "final": ("CONTRACCIONES SIN CAMBIO CERVICAL", ["Reposo y observación por 2-3 horas", "Reevaluar el cuello"]),
   "nota": "Trabajo de parto pretérmino = contracciones regulares + cambios cervicales."},
  ["A las 34 semanas ya no se usan corticoides de rutina ni tocólisis.",
   "Sin infección no se indican antibióticos.",
   "Si el cuello cambia: manejo de parto pretérmino."],
  "ACOG – Practice Bulletin 171: Management of preterm labor (2016) · " + WILLIAMS)

# GIN-165 · radial
V("radial", "GIN-165", "hemorragia-posparto-choque-reposicion-diuresis", "¿Funciona la reposición de volumen?",
  "OBSTETRICIA ENAM: REANIMACIÓN EN LA HEMORRAGIA POSPARTO", "OBSTETRICIA",
  ("Metas de la reanimación", ["La diuresis refleja la perfusión de los órganos",
   "Meta: ≥ 0,5 ml/kg/h (con sonda vesical)"]),
  ("Puérpera inmediata en choque hipovolémico", ["Hemorragia profusa", "Se inicia hidratación agresiva"]),
  {"rotulo": "Mapa del tema", "centro": "REPOSICIÓN", "centro_sub": "¿Cómo se evalúa?", "ans": 0,
   "items": [("DIURESIS ≥ 0,5 ML/KG/H", ["Mejor signo de perfusión", "Medir con sonda Foley"]),
             ("Presión arterial", ["Puede normalizarse tarde"]),
             ("Frecuencia cardiaca", ["Tiende a bajar"]),
             ("Estado de conciencia", ["Mejora al perfundir"]),
             ("Lactato", ["Desciende si hay perfusión"])],
   "ruta": ["Choque hemorrágico", "Líquidos y sangre", "Riñón perfundido", "DIURESIS RECUPERADA"]},
  ["Detener el sangrado es el objetivo, pero no mide la reposición.",
   "La SatO₂ puede ser normal en el choque.",
   "Colocar sonda vesical al iniciar la reanimación."],
  "OMS – Recomendaciones para el tratamiento de la hemorragia posparto (2023) · " + WILLIAMS)

# GIN-166 · árbol
A("GIN-166", "gestante-glucosa-ayunas-130-y-128-diabetes-confirmada", "Glucosa alta en la gestante",
  "OBSTETRICIA ENAM: DIAGNÓSTICO DE DIABETES EN EL EMBARAZO", "OBSTETRICIA",
  ("Diabetes en la gestación", ["Dos glucosas en ayunas ≥ 126 mg/dl ya hacen el diagnóstico",
   "No se necesita curva de tolerancia"]),
  ("Gestante", ["Glucosa en ayunas 130 mg/dl", "Repetida a los 3 días: 128 mg/dl"]),
  Q("¿Glucosa en ayunas ≥ 126 en dos ocasiones?", [
      L("Sí", "DIAGNÓSTICO HECHO", ["No requiere otra prueba", "Diabetes manifiesta"], path=True),
      Q("¿92-125 mg/dl?", [
          L("Sí", "Diabetes gestacional", ["Criterio IADPSG"]),
          L("No", "Curva de 75 g", ["A las 24-28 semanas"])], edge="No")], path=True),
  ("Valores diagnósticos en la gestante", [("Diabetes manifiesta", True), ("Diabetes gestacional", False)], [
      ("Ayunas", ["≥ 126 mg/dl", "92-125 mg/dl"]),
      ("Curva 75 g (2 h)", ["≥ 200 mg/dl", "≥ 153 mg/dl"]),
      ("HbA1c", ["≥ 6,5 %", "No se usa"])]),
  ["Hacer una curva con glucosa diagnóstica expone a hiperglucemia innecesaria.",
   "Iniciar dieta, control glucémico e insulina si no se logran metas.",
   "La prueba de 50 g es solo tamizaje (esquema en dos pasos)."],
  "ADA – Standards of Care in Diabetes 2025: Management of diabetes in pregnancy · IADPSG (2010)")

# GIN-167 · puntaje
V("puntaje", "GIN-167", "abortos-previos-macrosomico-descartar-diabetes", "Antecedentes que obligan a buscar diabetes",
  "OBSTETRICIA ENAM: FACTORES DE RIESGO DE DIABETES", "OBSTETRICIA",
  ("Tamizaje temprano de diabetes", ["Ciertos antecedentes obligan a buscar diabetes desde el primer control",
   "Macrosomía y pérdidas previas sugieren hiperglucemia no detectada"]),
  ("Gestante joven", ["Antecedente de dos abortos", "Un hijo macrosómico"]),
  {"rotulo": "Factores de riesgo presentes", "escala": "Riesgo de diabetes", "total": 2, "max": 6,
   "total_label": "Factores del caso",
   "interpreta": "Alto riesgo: tamizar en el primer control",
   "items": [("Hijo macrosómico (≥ 4000 g)", "1", True), ("Abortos o muerte fetal previos", "1", True),
             ("Obesidad (IMC ≥ 30)", "1", False), ("Diabetes gestacional previa", "1", False),
             ("Familiar de primer grado con diabetes", "1", False), ("Síndrome de ovario poliquístico", "1", False)],
   "bandas": [("0", "Riesgo habitual", "Tamizaje a las 24-28 semanas", False),
              ("≥ 1", "Alto riesgo", "Glucosa en el primer control", True)]},
  ["La hiperglucemia temprana aumenta abortos y malformaciones.",
   "Si el tamizaje temprano es normal, se repite a las 24-28 semanas.",
   "El lupus y los trastornos genéticos no explican la macrosomía."],
  "ADA – Standards of Care in Diabetes 2025 · ACOG – Practice Bulletin 190: Gestational diabetes (2018)")

# GIN-168 · tarjetas
V("tarjetas", "GIN-168", "desaceleraciones-variables-compresion-cordon", "Desaceleraciones de la frecuencia fetal",
  "OBSTETRICIA ENAM: DESACELERACIONES VARIABLES", "OBSTETRICIA",
  ("Monitoreo fetal", ["Cada tipo de desaceleración tiene su mecanismo",
   "Variables (forma y momento irregulares) = compresión del cordón"]),
  ("Gestante en trabajo de parto", ["Desaceleraciones variables", "Sin relación con las contracciones"]),
  {"rotulo": "¿Qué mecanismo explica cada una?", "ans": 0, "cards": [
      {"titulo": "VARIABLES", "datos": [
          ("Forma", "En V o U, irregular", True), ("Momento", "Sin relación fija", True),
          ("Causa", "COMPRESIÓN DEL CORDÓN", True), ("Gravedad", "Según duración", False)],
       "pie": "Cambiar de posición, amnioinfusión"},
      {"titulo": "Tempranas (DIP I)", "datos": [
          ("Forma", "Espejo de la contracción", False), ("Momento", "Coinciden", False),
          ("Causa", "Compresión cefálica", False), ("Gravedad", "Benignas", False)],
       "pie": "No requieren acción"},
      {"titulo": "Tardías (DIP II)", "datos": [
          ("Forma", "Lenta y simétrica", False), ("Momento", "Después del pico", False),
          ("Causa", "Insuficiencia placentaria", False), ("Gravedad", "Hipoxia", False)],
       "pie": "Reanimación intrauterina"},
      {"titulo": "Bradicardia prolongada", "datos": [
          ("Forma", "Sostenida", False), ("Momento", "> 10 minutos", False),
          ("Causa", "Prolapso, rotura, DPP", False), ("Gravedad", "Emergencia", False)],
       "pie": "Parto inmediato"}]},
  ["Las variables son las desaceleraciones más frecuentes en el trabajo de parto.",
   "Circular de cordón y oligohidramnios las favorecen.",
   "Tacto vaginal para descartar prolapso de cordón."],
  "ACOG – Practice Bulletin 106: Intrapartum fetal heart rate monitoring (2009) · " + WILLIAMS)

# GIN-169 · fases
V("fases", "GIN-169", "estimular-parto-10-ui-oxitocina-litro", "Cómo preparar la oxitocina",
  "OBSTETRICIA ENAM: CONDUCCIÓN DEL TRABAJO DE PARTO", "OBSTETRICIA",
  ("Conducción con oxitocina", ["Dilución estándar: 10 UI en 1000 ml de solución salina",
   "Queda 10 mUI/ml; se inicia a dosis baja y se sube poco a poco"]),
  ("Centro de salud rural", ["Dinámica uterina inadecuada", "Se decide estimular el parto"]),
  {"rotulo": "Pasos de la conducción", "ans": 0,
   "fases": [("Preparar", "Dilución", "10 UI EN 1 LITRO", ["10 mUI por ml"]),
             ("Iniciar", "Dosis baja", "1-2 mUI/min", ["Bomba o goteo contado"]),
             ("Aumentar", "Cada 30-40 min", "+1-2 mUI/min", ["Hasta 3-5 contracciones en 10 min"]),
             ("Vigilar", "Siempre", "LCF y dinámica", ["Suspender si hay taquisistolia"])],
   "curvas": [("Dosis", VIOLET, [0.1, 0.1, 0.25, 0.4, 0.55, 0.65, 0.65])],
   "chips_titulo": "Unidades en 1 litro · marcada la correcta",
   "chips": [("10 UI", True), ("20 UI", False), ("30 UI", False), ("40 UI", False)]},
  ["Taquisistolia: más de 5 contracciones en 10 minutos; suspender la oxitocina.",
   "Descartar desproporción cefalopélvica antes de estimular.",
   "Dosis altas o en bolo: riesgo de rotura uterina e intoxicación hídrica."],
  "MINSA – Guía técnica de atención del parto · OMS – Recomendaciones sobre conducción del trabajo de parto (2014)")

# GIN-170 · árbol
A("GIN-170", "32-semanas-peso-p10-doppler-normal-control-2-semanas", "Feto pequeño: ¿PEG o RCIU?",
  "OBSTETRICIA ENAM: FETO PEQUEÑO PARA LA EDAD GESTACIONAL", "OBSTETRICIA",
  ("Feto pequeño", ["Peso < p10: se define con el Doppler y el líquido amniótico",
   "Doppler umbilical y líquido normales = pequeño constitucional (PEG)"]),
  ("Gestante de 32 semanas", ["Altura uterina menor que la esperada", "Peso fetal < p10 · líquido normal · Doppler umbilical normal"]),
  Q("¿Doppler umbilical alterado o peso < p3?", [
      L("Sí", "RCIU", ["Vigilancia estrecha", "Terminar según gravedad"]),
      L("No", "CONTROL EN DOS SEMANAS", ["Biometría y Doppler seriados", "Probable PEG constitucional"], path=True)], path=True),
  ("PEG vs RCIU", [("PEG", True), ("RCIU", False)], [
      ("Doppler", ["Normal", "Alterado"]),
      ("Líquido amniótico", ["Normal", "Oligohidramnios"]),
      ("Conducta", ["Control cada 2 semanas", "Controles frecuentes, parto antes"])]),
  ["No se termina la gestación ni se dan corticoides si el Doppler es normal.",
   "Confirmar la edad gestacional con la ecografía temprana.",
   "Doppler con flujo ausente o reverso = alto riesgo."],
  "ACOG – Practice Bulletin 227: Fetal growth restriction (2021) · ISUOG – Practice guidelines on FGR (2020)")

# GIN-171 · matriz
V("matriz", "GIN-171", "42-semanas-fur-incierta-ecografia-primer-trimestre", "¿Cómo se fecha el embarazo?",
  "OBSTETRICIA ENAM: EDAD GESTACIONAL", "OBSTETRICIA",
  ("Edad gestacional", ["La ecografía del primer trimestre (LCN) es la más exacta",
   "Si la FUR es dudosa, esa ecografía define si realmente es un embarazo prolongado"]),
  ("Gestante referida a las 42 semanas", ["No recuerda bien su FUR", "¿Qué evaluar antes de hospitalizar?"]),
  {"rotulo": "Método y precisión", "eje_x": "Rasgo", "eje_y": "Método",
   "cols": ["Error", "Uso"], "rows": ["Eco de 1.er trimestre", "FUR segura", "Eco de 2.º trimestre", "Eco de 3.er trimestre"], "caso": (0, 0),
   "cells": [[("± 5-7 DÍAS", ["Longitud craneocaudal"]), ("La referencia", [])],
             [("± 1-2 semanas", ["Ciclos irregulares"]), ("Si coincide con la eco", [])],
             [("± 10-14 días", []), ("Si no hubo eco temprana", [])],
             [("± 3-4 semanas", []), ("No sirve para fechar", [])]]},
  ["Una ecografía actual solo muestra el tamaño, no la edad.",
   "El perfil biofísico y el NST evalúan bienestar, no edad gestacional.",
   "Si no hay eco temprana, se combina FUR con la primera ecografía disponible."],
  "ACOG – Committee Opinion 700: Methods for estimating the due date (2017)")

# GIN-172 · radial
V("radial", "GIN-172", "primer-control-8-semanas-no-tolerancia-glucosa", "Exámenes del primer control prenatal",
  "OBSTETRICIA ENAM: PRIMER CONTROL PRENATAL", "OBSTETRICIA",
  ("Primer control prenatal", ["Se piden exámenes basales: hemograma, grupo y Rh, orina, glucosa, serologías",
   "La curva de tolerancia a la glucosa se hace a las 24-28 semanas"]),
  ("Gestante de 8 semanas", ["Solo puede pedir 3 análisis", "¿Cuál descarta?"]),
  {"rotulo": "Mapa del tema", "centro": "PRIMER CONTROL", "centro_sub": "8 semanas", "ans": 0,
   "items": [("TOLERANCIA A LA GLUCOSA", ["NO en el primer control", "Va a las 24-28 semanas"]),
             ("Hemograma", ["Anemia"]),
             ("Urocultivo", ["Bacteriuria asintomática"]),
             ("Urea y creatinina", ["Función renal basal"]),
             ("Serologías", ["VIH, sífilis, hepatitis B"])],
   "ruta": ["8 semanas", "Exámenes basales", "La curva aún no toca", "DESCARTAR TOLERANCIA"]},
  ["En el primer control sí se pide glucosa en ayunas.",
   "La bacteriuria asintomática se trata siempre en la gestante.",
   "Grupo y Rh para planificar la profilaxis anti-D."],
  "MINSA – NTS de atención integral de salud materna · OMS – Recomendaciones sobre atención prenatal (2016)")

# GIN-173 · matriz
V("matriz", "GIN-173", "alumbramiento-retrasado-kustner-cordon-asciende", "¿Se desprendió la placenta?",
  "OBSTETRICIA ENAM: SIGNOS DE DESPRENDIMIENTO PLACENTARIO", "OBSTETRICIA",
  ("Alumbramiento", ["Hay maniobras y signos que indican si la placenta ya se desprendió",
   "Küstner: al presionar sobre el pubis, si el cordón sube, la placenta sigue adherida"]),
  ("Parto atendido", ["Retraso del alumbramiento", "A los 10 minutos la placenta no se ha desprendido"]),
  {"rotulo": "Signo y significado", "eje_x": "Rasgo", "eje_y": "Signo",
   "cols": ["Qué se hace u observa", "Significa"], "rows": ["Küstner", "Ahlfeld", "Schröder", "Sangrado"], "caso": (0, 1),
   "cells": [[("Presión suprapúbica", ["Se observa el cordón"]), ("SI EL CORDÓN SUBE: NO DESPRENDIDA", [])],
             [("Pinza en el cordón", []), ("Si desciende: desprendida", [])],
             [("Forma del útero", []), ("Globular y alto: desprendida", [])],
             [("Salida brusca de sangre", []), ("Desprendimiento", [])]]},
  ["Manejo activo: oxitocina 10 UI IM, tracción controlada y masaje uterino.",
   "Si a los 30 minutos no sale: retención placentaria, extracción manual.",
   "Nunca traccionar el cordón sin contratracción del útero."],
  WILLIAMS + " · OMS – Recomendaciones para la prevención de la hemorragia posparto (2018)")

# GIN-174 · matriz
V("matriz", "GIN-174", "gemelos-dicigoticos-no-transfusion-feto-fetal", "Complicaciones según la corionicidad",
  "OBSTETRICIA ENAM: EMBARAZO GEMELAR DICIGÓTICO", "OBSTETRICIA",
  ("Gemelos dicigóticos", ["Siempre bicoriales: cada uno tiene su placenta",
   "La transfusión feto-fetal requiere placenta compartida (monocorial)"]),
  ("Gestante añosa con gemelos dicigóticos", ["Controles cada 15 días", "¿Qué complicación es la menos esperable?"]),
  {"rotulo": "Complicación y tipo de placenta", "eje_x": "Placenta", "eje_y": "Complicación",
   "cols": ["Bicorial (dicigóticos)", "Monocorial"], "rows": ["Transfusión feto-fetal", "Preeclampsia", "Parto pretérmino", "Hemorragia posparto"], "caso": (0, 0),
   "cells": [[("NO OCURRE", ["No hay vasos compartidos"]), ("10-15 %", ["Anastomosis vasculares"])],
             [("Aumentada", []), ("Aumentada", [])],
             [("Aumentado", []), ("Más aumentado", [])],
             [("Aumentada", ["Útero sobredistendido"]), ("Aumentada", [])]]},
  ["Todo dicigótico es bicorial; los monocigóticos pueden ser mono o bicoriales.",
   "La corionicidad se define por ecografía en el primer trimestre (signo lambda o T).",
   "Edad materna avanzada aumenta los gemelos dicigóticos."],
  "ACOG – Practice Bulletin 231: Multifetal gestations (2021) · ISUOG – Guideline on twin pregnancy (2025)")
