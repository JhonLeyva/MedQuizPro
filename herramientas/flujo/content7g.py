"""Bloque 7 · parte G."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GUYTON = "Guyton y Hall. Tratado de fisiología médica 14.ª ed. (2021)"

# END-052 · radial
V("radial", "END-052", "diabetica-parestesias-dolor-mmii-gabapentina", "Dolor neuropático diabético",
  "ENDOCRINOLOGÍA ENAM: NEUROPATÍA DIABÉTICA DOLOROSA", "ENDOCRINOLOGÍA",
  ("Neuropatía diabética periférica", ["Polineuropatía distal en 'guante y calcetín' con dolor y parestesias",
   "Fármacos de primera línea: gabapentinoides, duloxetina o amitriptilina"]),
  ("Mujer de 50 años con 15 años de DM2 mal controlada", ["Un año de dolor y parestesias en miembros inferiores", "Pérdida de la sensibilidad dolorosa"]),
  {"rotulo": "Mapa del tema", "centro": "DOLOR NEUROPÁTICO", "centro_sub": "Opciones", "ans": 0,
   "items": [("GABAPENTINA / PREGABALINA", ["Primera línea", "Modulan canales de calcio"]),
             ("Duloxetina", ["Primera línea, IRSN"]),
             ("Amitriptilina", ["Barata; evitar en ancianos"]),
             ("Tramadol", ["Solo de rescate"]),
             ("Tiamina", ["Útil solo si hay déficit"])],
   "ruta": ["Diabetes de larga data", "Dolor y parestesias", "Neuropatía periférica", "GABAPENTINA"]},
  ["El mejor tratamiento de fondo es el control glucémico.",
   "Revisar los pies en cada consulta: riesgo de úlcera.",
   "El propranolol no trata el dolor neuropático."],
  "ADA – Diabetic neuropathy: position statement (Diabetes Care 2017) · ADA – Standards of Care 2025")

# GIN-182 · termómetro
V("termometro", "GIN-182", "28-semanas-dilatacion-4-cm-borramiento-80-parto-pretermino", "Contracciones antes del término",
  "OBSTETRICIA ENAM: TRABAJO DE PARTO PRETÉRMINO", "OBSTETRICIA",
  ("Parto pretérmino", ["Amenaza: contracciones con cambios cervicales leves",
   "Trabajo de parto establecido: dilatación ≥ 3-4 cm con borramiento ≥ 80 %"]),
  ("Segundigesta de 28 semanas", ["Contracciones desde hace 12 horas · 2 en 10 min", "Dilatación 4 cm · borramiento 80 %"]),
  {"rotulo": "Grado del cuadro",
   "niveles": [("Pródromos", "Sin cambios cervicales", ["Contracciones irregulares"]),
               ("Amenaza", "Cambios leves", ["< 3 cm, borramiento < 80 %"]),
               ("Trabajo", "Establecido", ["4 CM Y 80 %", "Parto pretérmino en curso"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Hospitalizar y preparar el parto", ["Sulfato de Mg (neuroprotección < 32 sem)", "Corticoides si da tiempo"], True),
             (2, "Profilaxis contra estreptococo B", ["Ampicilina o penicilina"], False),
             (3, "Neonatología presente", ["RN de 28 semanas"], False)]},
  ["Con 4 cm y 80 % la tocólisis rara vez detiene el parto.",
   "La incompetencia cervical dilata sin contracciones.",
   "Cesárea previa: no contraindica el parto vaginal si la incisión fue segmentaria."],
  "ACOG – Practice Bulletin 171: Management of preterm labor (2016) · " + WILLIAMS)

# GAS-062 · árbol
A("GAS-062", "saciedad-precoz-ganglio-virchow-ascitis-endoscopia", "Sospecha de cáncer gástrico avanzado",
  "GASTROENTEROLOGÍA ENAM: CÁNCER GÁSTRICO", "GASTROENTEROLOGÍA",
  ("Cáncer gástrico", ["Signos de alarma: baja de peso, saciedad precoz, anemia, masa",
   "El diagnóstico se hace con endoscopia y biopsia"]),
  ("Varón de 65 años con 8 semanas de llenura precoz", ["Baja de peso, anemia microcítica, ascitis", "Ganglio supraclavicular izquierdo pétreo (Virchow)"]),
  Q("¿Dispepsia con signos de alarma?", [
      L("Sí", "ENDOSCOPIA ALTA + BIOPSIA", ["Confirma el tipo histológico", "Luego TC para estadificar"], path=True),
      L("No, < 60 años", "Test y tratar H. pylori", ["O IBP de prueba"])], path=True),
  ("Signos de enfermedad avanzada", [("Signo", True), ("Significa", False)], [
      ("Ganglio de Virchow", ["Supraclavicular izquierdo", "Metástasis linfática"]),
      ("Ascitis", ["Carcinomatosis peritoneal", "Irresecable"]),
      ("Hermana María José", ["Nódulo umbilical", "Siembra peritoneal"])]),
  ["La biopsia del ganglio confirma metástasis, pero no el tumor primario.",
   "El adenocarcinoma es el tipo más frecuente.",
   "En el Perú el cáncer gástrico es de los más letales."],
  "NCCN – Gastric cancer (2025) · ESMO – Gastric cancer guideline (2022)")

# TRA-041 · puntaje
V("puntaje", "TRA-041", "adolescente-rodilla-fiebre-leucocitosis-artritis-septica-aureus", "Artritis séptica en el adolescente",
  "TRAUMATOLOGÍA ENAM: ARTRITIS SÉPTICA", "TRAUMATOLOGÍA",
  ("Artritis séptica", ["Monoartritis aguda con fiebre: urgencia",
   "Germen más frecuente a toda edad: Staphylococcus aureus"]),
  ("Varón de 13 años con 3 días de dolor en la rodilla", ["No puede caminar · fiebre 38,5 °C", "Rodilla inflamada · leucocitos 25 000, 10 % abastonados"]),
  {"rotulo": "Criterios de Kocher", "escala": "Kocher (probabilidad)", "total": 3, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Probabilidad de artritis séptica ~93 %",
   "items": [("Fiebre > 38,5 °C", "1", True), ("No puede apoyar la pierna", "1", True),
             ("Leucocitos > 12 000", "1", True), ("VSG > 40 mm/h", "1", False)],
   "bandas": [("0-1", "Baja", "Pensar en sinovitis transitoria", False),
              ("2", "Intermedia", "Artrocentesis", False),
              ("3-4", "Alta", "Artrocentesis, drenaje y antibiótico", True)]},
  ["Germen: S. aureus; cubrir con oxacilina o cefazolina (vancomicina si hay SARM).",
   "Adolescente sexualmente activo: pensar también en gonococo.",
   "H. influenzae casi desapareció por la vacuna."],
  "Kocher MS (J Bone Joint Surg 1999) · PIDS/IDSA – Guideline on acute bacterial arthritis in children (2023)")

# GIN-183 · matriz
V("matriz", "GIN-183", "33-semanas-sangrado-sin-dolor-presentacion-flotante-no-tacto", "Sangrado del tercer trimestre",
  "OBSTETRICIA ENAM: SOSPECHA DE PLACENTA PREVIA", "OBSTETRICIA",
  ("Placenta previa", ["Sangrado rojo, indoloro, sin contracciones; presentación alta",
   "El tacto vaginal puede desencadenar una hemorragia masiva"]),
  ("Gestante de 33 semanas sin control prenatal", ["Sangrado vaginal sin otras molestias · cesárea previa", "Presentación flotante · sin contracciones"]),
  {"rotulo": "¿Qué examen se permite?", "eje_x": "Rasgo", "eje_y": "Examen",
   "cols": ["¿Se hace?", "Motivo"], "rows": ["Tacto vaginal", "Especuloscopía", "Ecografía abdominal", "Ecografía transvaginal"], "caso": (0, 0),
   "cells": [[("EVITAR", []), ("Puede desprender la placenta", ["Hemorragia masiva"])],
             [("Sí, con cuidado", []), ("Ver origen del sangrado", [])],
             [("Sí", []), ("Ubica la placenta", [])],
             [("Sí", []), ("Segura y más exacta", ["La sonda no entra al cuello"])]]},
  ["Cesárea previa + placenta previa: descartar acretismo.",
   "El desprendimiento de placenta duele y el útero está hipertónico.",
   "Hospitalizar, vía EV, grupo y Rh, corticoides si < 34 semanas."],
  "RCOG – Green-top Guideline 27a: Placenta praevia and placenta accreta (2018) · " + WILLIAMS)

# OFT-040 · árbol
A("OFT-040", "anciano-epistaxis-fosa-y-boca-taponamiento-posterior", "Epistaxis grave en el anciano",
  "OTORRINOLARINGOLOGÍA ENAM: EPISTAXIS POSTERIOR", "OTORRINOLARINGOLOGÍA",
  ("Epistaxis", ["Anterior: plexo de Kiesselbach, frecuente en niños, cede con compresión",
   "Posterior: arteria esfenopalatina, ancianos, sangra hacia la faringe"]),
  ("Varón de 83 años", ["Sangrado nasal severo por la fosa derecha y por la boca", "Estable, palidez leve"]),
  Q("¿El sangrado cae a la faringe o no se ve el punto?", [
      L("Sí: posterior", "TAPONAMIENTO POSTERIOR", ["Sonda con balón o gasa posterior", "Hospitalizar"], path=True),
      Q("Anterior: ¿cede con compresión?", [
          L("No", "Cauterizar o taponamiento anterior", ["Nitrato de plata"]),
          L("Sí", "Observación", ["Humidificar la mucosa"])], edge="No")], path=True),
  ("Epistaxis anterior vs posterior", [("Posterior", True), ("Anterior", False)], [
      ("Origen", ["Esfenopalatina", "Kiesselbach"]),
      ("Paciente", ["Anciano, hipertenso", "Niño, adulto joven"]),
      ("Manejo", ["Taponamiento posterior", "Compresión, cauterio"])]),
  ["La compresión externa no alcanza el sangrado posterior.",
   "Si el taponamiento falla: ligadura o embolización de la esfenopalatina.",
   "Controlar la presión arterial y la anticoagulación."],
  "AAO-HNS – Clinical practice guideline: Nosebleed (epistaxis) (2020)")

# CB-068 · fases
V("fases", "CB-068", "infertilidad-maduracion-espermatica-epididimo", "Recorrido del espermatozoide",
  "CIENCIAS BÁSICAS ENAM: EPIDÍDIMO", "CIENCIAS BÁSICAS",
  ("Maduración espermática", ["Se forman en los túbulos seminíferos, pero salen inmóviles",
   "En el epidídimo adquieren movilidad y capacidad fecundante (10-14 días)"]),
  ("Varón de 25 años con infertilidad", ["Problema de maduración de los espermatozoides", "Estudios de la esposa normales"]),
  {"rotulo": "Estaciones del espermatozoide", "ans": 1,
   "fases": [("Túbulos", "Testículo", "Formación", ["Espermatogénesis, 64-74 días"]),
             ("Epidídimo", "Cabeza, cuerpo, cola", "MADURACIÓN", ["Movilidad y fecundidad"]),
             ("Deferente", "Transporte", "Conducción", ["Peristaltismo"]),
             ("Vesículas", "Glándulas", "Líquido seminal", ["Fructosa, 60 %"]),
             ("Eyaculador", "Próstata", "Salida", ["A la uretra"])],
   "curvas": [],
   "chips_titulo": "Estructura afectada · marcada la correcta",
   "chips": [("Cuerpo del epidídimo", True), ("Conducto eyaculador", False), ("Vesícula seminal", False), ("Conducto deferente", False)]},
  ["La cola del epidídimo almacena los espermatozoides maduros.",
   "La capacitación final ocurre en el tracto genital femenino.",
   "Fructosa baja en el semen: obstrucción de conductos eyaculadores."],
  GUYTON)

# GIN-184 · árbol
A("GIN-184", "placenta-baja-sangrado-escaso-7-cm-amniotomia-parto-vaginal", "Placenta baja en trabajo de parto",
  "OBSTETRICIA ENAM: PLACENTA DE INSERCIÓN BAJA", "OBSTETRICIA",
  ("Placenta de inserción baja", ["No cubre el orificio: el parto vaginal es posible si el sangrado es escaso",
   "La amniotomía hace que la presentación comprima el borde placentario"]),
  ("Multípara de 41 semanas", ["Contracciones 3 en 10 min · dilatación 7 cm, −1", "Placenta baja con sangrado escaso · LCF 148"]),
  Q("¿La placenta cubre el orificio cervical?", [
      L("Sí: previa total", "Cesárea", ["Nunca parto vaginal"]),
      Q("¿Sangrado abundante o sufrimiento fetal?", [
          L("Sí", "Cesárea", ["Urgente"]),
          L("No", "VÍA EV + AMNIOTOMÍA", ["Esperar el parto vaginal", "Vigilancia estrecha"], path=True)],
        edge="No: inserción baja", path=True)], path=True),
  ("Tipo de placenta y vía de parto", [("Baja", True), ("Marginal", False), ("Total", False)], [
      ("Relación con el orificio", ["A < 2 cm, no lo toca", "Llega al borde", "Lo cubre"]),
      ("Vía", ["Vaginal posible", "Según sangrado", "Cesárea"])]),
  ["La oxitocina no se usa para acelerar si la dinámica ya es adecuada.",
   "Tener sangre cruzada y quirófano disponible.",
   "Con 7 cm en una multípara el parto está cerca."],
  "RCOG – Green-top Guideline 27a: Placenta praevia (2018) · " + WILLIAMS)

# PED-179 · fases
V("fases", "PED-179", "escolar-ictericia-transaminasas-altas-hepatitis-a-sintomaticos", "Hepatitis A en el niño",
  "PEDIATRÍA ENAM: HEPATITIS A", "PEDIATRÍA",
  ("Hepatitis A", ["Transmisión fecal-oral: alimentos o agua contaminados",
   "Autolimitada: solo tratamiento de soporte si no hay falla hepática"]),
  ("Niño de 10 años que come en el quiosco escolar", ["4 días de fiebre, dolor abdominal, vómitos y coluria", "Ictericia · TGO 740 · TGP 1020 · TP normal"]),
  {"rotulo": "Curso de la enfermedad", "ans": 2,
   "fases": [("Incubación", "2-6 semanas", "Asintomática", ["Ya contagia"]),
             ("Prodrómica", "Días", "Fiebre, vómitos", ["Malestar, anorexia"]),
             ("Ictérica", "1-3 semanas", "HIDRATAR Y SINTOMÁTICOS", ["TP normal: sin falla hepática"]),
             ("Convalecencia", "Semanas", "Recuperación", ["Inmunidad de por vida"])],
   "curvas": [("Transaminasas", ROSE, [0.05, 0.1, 0.4, 0.95, 0.7, 0.3, 0.1]),
              ("Bilirrubina", AMBER, [0.0, 0.05, 0.3, 0.8, 0.85, 0.4, 0.1])],
   "chips_titulo": "Manejo · marcado el correcto",
   "chips": [("Hidratación y sintomáticos", True), ("Gammaglobulina", False), ("Hepatoprotectores", False), ("Interferón", False)]},
  ["El TP prolongado sería signo de falla hepática aguda: hospitalizar.",
   "Evitar paracetamol en dosis altas.",
   "Vacuna contra hepatitis A a los 15 meses (MINSA)."],
  "CDC – Hepatitis A: clinical overview (2024) · " + NELSON)

# SP-134 · radial
V("radial", "SP-134", "cuarentena-estado-nutricional-marco-conceptual-estilos-vida", "Partes del protocolo de investigación",
  "SALUD PÚBLICA ENAM: MARCO CONCEPTUAL", "SALUD PÚBLICA",
  ("Marco conceptual", ["Define los conceptos y variables centrales del estudio",
   "Si se estudia el estado nutricional, debe incluir estilos de vida saludable"]),
  ("Investigación en estudiantes de medicina", ["Impacto de la cuarentena por COVID-19", "En su estado nutricional"]),
  {"rotulo": "Mapa del tema", "centro": "PROTOCOLO", "centro_sub": "¿Qué va en cada parte?", "ans": 0,
   "items": [("MARCO CONCEPTUAL", ["Estilos de vida saludable", "Variables del estudio"]),
             ("Problema", ["Qué se quiere saber"]),
             ("Objetivos", ["Qué se medirá"]),
             ("Hipótesis", ["Explicación tentativa"]),
             ("Metodología", ["Diseño, muestra, análisis"])],
   "ruta": ["Cuarentena", "Estado nutricional", "Estilos de vida", "MARCO CONCEPTUAL"]},
  ["Conectividad y estrés no son las variables del estudio.",
   "El marco teórico revisa antecedentes; el conceptual define términos.",
   "Cada concepto debe poder medirse."],
  "Hernández-Sampieri. Metodología de la investigación 7.ª ed. (2023)")

# PED-180 · puntaje
V("puntaje", "PED-180", "lactante-rigidez-fiebre-38-convulsion-febril-simple", "Convulsión con fiebre en el lactante",
  "PEDIATRÍA ENAM: CONVULSIÓN FEBRIL SIMPLE", "PEDIATRÍA",
  ("Convulsión febril", ["La más frecuente de la infancia (6 meses a 5 años)",
   "Simple: generalizada, < 15 minutos, única en 24 h, sin déficit posterior"]),
  ("Lactante de 1 año sin antecedentes", ["Rigidez con relajación de esfínteres por unos minutos", "T 38 °C · despierto · sin signos meníngeos · examen normal"]),
  {"rotulo": "Criterios de convulsión febril simple", "escala": "Criterios", "total": 5, "max": 5,
   "total_label": "Criterios cumplidos",
   "interpreta": "Convulsión febril simple",
   "items": [("Edad 6 meses a 5 años", "✓", True), ("Crisis generalizada", "✓", True),
             ("Duración < 15 minutos", "✓", True), ("Única en 24 horas", "✓", True),
             ("Sin déficit ni signos meníngeos", "✓", True)],
   "bandas": [("5 de 5", "Simple", "Bajar la fiebre y tranquilizar", True),
              ("< 5", "Compleja", "Estudio: punción, EEG, imagen", False)]},
  ["No requiere anticonvulsivantes ni EEG.",
   "Los antipiréticos alivian, pero no previenen la recurrencia.",
   "Riesgo de recurrencia ~30 %; el de epilepsia es bajo."],
  "AAP – Clinical practice guideline: febrile seizures (2008, 2011) · " + NELSON)

# INF-089 · fases
V("fases", "INF-089", "agricultor-fiebre-mialgia-pantorrillas-canales-leptospirosis-sospechoso", "Clasificación del caso de leptospirosis",
  "INFECTOLOGÍA ENAM: CASO SOSPECHOSO DE LEPTOSPIROSIS", "INFECTOLOGÍA",
  ("Vigilancia de leptospirosis", ["Sospechoso: fiebre + cefalea + mialgias (pantorrillas) + exposición a agua o animales",
   "Se confirma con laboratorio (ELISA IgM, MAT, PCR)"]),
  ("Agricultor de 40 años", ["4 días de fiebre, cefalea, artralgias, mialgias en pantorrillas", "Expuesto a canales de regadío el último mes"]),
  {"rotulo": "Clasificación del caso", "ans": 0,
   "fases": [("Sospechoso", "Clínica + exposición", "CASO SOSPECHOSO", ["Notificar", "Iniciar tratamiento"]),
             ("Probable", "Prueba rápida", "IgM reactiva", ["O nexo epidemiológico"]),
             ("Confirmado", "Laboratorio", "MAT o PCR", ["Seroconversión"]),
             ("Descartado", "Laboratorio", "Negativo", ["Buscar otra causa"])],
   "curvas": [],
   "chips_titulo": "Clasificación · marcada la correcta",
   "chips": [("Sospechoso de leptospirosis", True), ("Confirmado de dengue", False), ("Sospecha de peste", False), ("Contacto de fiebre amarilla", False)]},
  ["No se espera al laboratorio para tratar: doxiciclina o amoxicilina si es leve.",
   "Mialgia en pantorrillas y sufusión conjuntival orientan a leptospirosis.",
   "Es de notificación obligatoria."],
  "MINSA – NTS de vigilancia epidemiológica de la leptospirosis · OPS – Leptospirosis humana: guía para el diagnóstico (2008)")

# HEM-035 · embudo
V("embudo", "HEM-035", "cerro-de-pasco-hb-22-cianosis-mal-de-montana-cronico", "Eritrocitosis en la altura",
  "HEMATOLOGÍA ENAM: MAL DE MONTAÑA CRÓNICO", "HEMATOLOGÍA",
  ("Mal de montaña crónico (enfermedad de Monge)", ["Eritrocitosis excesiva en residentes de altura: Hb ≥ 21 g/dl en varones",
   "Hipoxemia, cefalea, mareos, acúfenos, cianosis y conjuntivas rojas"]),
  ("Varón de 60 años de Cerro de Pasco", ["2 años de cefalea, mareos y acúfenos", "Cianosis · Hb 22 · Hto 66 % · SatO₂ 88 %"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hemoglobina muy alta con síntomas",
   "candidatos": ["Mal de montaña crónico", "Policitemia vera", "Policitemia fisiológica", "Hipoxemia refractaria"],
   "pasos": [("Vive en la altura, sin esplenomegalia ni leucocitosis", ["Policitemia vera"]),
             ("Hb ≥ 21 con síntomas: supera lo fisiológico", ["Policitemia fisiológica", "Hipoxemia refractaria"])],
   "final": ("MAL DE MONTAÑA CRÓNICO", ["Bajar a menor altura", "Flebotomía, acetazolamida"]),
   "nota": "Cerro de Pasco está a más de 4300 m: una de las ciudades más altas del mundo."},
  ["La policitemia vera tiene EPO baja y mutación JAK2.",
   "Riesgo de trombosis por hiperviscosidad.",
   "Puede evolucionar a hipertensión pulmonar."],
  "Consenso de Qinghai – Chronic mountain sickness (High Alt Med Biol 2005) · Villafuerte y León-Velarde (2023)")

# INF-090 · árbol
A("INF-090", "uretritis-mucopurulenta-contacto-casual-ceftriaxona-azitromicina", "Secreción uretral",
  "INFECTOLOGÍA ENAM: SÍNDROME DE DESCARGA URETRAL", "INFECTOLOGÍA",
  ("Uretritis", ["Principales causas: gonococo y Chlamydia, a menudo juntos",
   "Manejo sindrómico: cubrir ambos en la primera consulta"]),
  ("Varón de 24 años", ["Contacto sexual casual sin protección hace 4 días", "Secreción uretral mucopurulenta y disuria"]),
  Q("¿Secreción uretral confirmada?", [
      L("Sí", "CEFTRIAXONA + AZITROMICINA", ["Ceftriaxona 500 mg IM dosis única", "Azitromicina 1 g o doxiciclina 7 días"], path=True),
      L("No: solo disuria", "Examen de orina", ["Descartar ITU"])], path=True),
  ("Gérmenes de la uretritis", [("Gonococo", True), ("Chlamydia", True)], [
      ("Secreción", ["Purulenta, abundante", "Mucosa, escasa"]),
      ("Incubación", ["2-5 días", "1-3 semanas"]),
      ("Fármaco", ["Ceftriaxona", "Azitromicina o doxiciclina"])]),
  ["Tratar a las parejas de los últimos 60 días.",
   "Ofrecer VIH, sífilis y hepatitis B.",
   "Abstinencia sexual 7 días tras el tratamiento."],
  "MINSA – NTS 077: Manejo de infecciones de transmisión sexual · CDC – STI treatment guidelines (2021)")

# CB-069 · fases
V("fases", "CB-069", "metronidazol-alcohol-palpitaciones-efecto-antabus", "Metronidazol y alcohol",
  "CIENCIAS BÁSICAS ENAM: EFECTO ANTABÚS", "CIENCIAS BÁSICAS",
  ("Reacción tipo disulfiram", ["El metronidazol inhibe la aldehído deshidrogenasa",
   "Se acumula acetaldehído: rubor, náuseas, vómitos, palpitaciones, disnea"]),
  ("Varón de 32 años con giardiasis", ["4.º día de metronidazol 500 mg c/12 h", "Tras beber licor: disnea, vómitos, palpitaciones, agitación"]),
  {"rotulo": "Metabolismo del alcohol", "ans": 1,
   "fases": [("Etanol", "Ingestión", "Alcohol deshidrogenasa", ["Hígado"]),
             ("Acetaldehído", "Se acumula", "TÓXICO: EFECTO ANTABÚS", ["Metronidazol bloquea su paso"]),
             ("Acetato", "Normal", "Aldehído deshidrogenasa", ["Enzima inhibida"]),
             ("CO₂ y agua", "Final", "Eliminación", [])],
   "curvas": [("Acetaldehído", ROSE, [0.05, 0.3, 0.8, 0.95, 0.7, 0.35, 0.1])],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Efecto antabús", True), ("Sobredosis de metronidazol", False), ("Intoxicación alcohólica", False), ("Comida grasa", False)]},
  ["Evitar alcohol durante el tratamiento y 72 h después.",
   "Otros fármacos con este efecto: disulfiram, tinidazol, algunas cefalosporinas.",
   "Tratamiento de soporte; suele ceder en horas."],
  "Goodman & Gilman. Bases farmacológicas de la terapéutica 14.ª ed. (2023)")

# PED-181 · termómetro
V("termometro", "PED-181", "neonato-14-dias-cordon-sin-signos-retraso-sin-patologia", "Caída del cordón umbilical",
  "PEDIATRÍA ENAM: RETRASO EN LA CAÍDA DEL CORDÓN", "PEDIATRÍA",
  ("Caída del cordón", ["Suele caer entre los 5 y 15 días",
   "Solo preocupa si pasa de 3-4 semanas con infecciones o leucocitosis"]),
  ("Neonato de 14 días en control de niño sano", ["Buen estado, sin fiebre", "Cordón sin mal olor ni secreción · examen normal"]),
  {"rotulo": "Días de vida",
   "niveles": [("≤ 15 días", "Normal", ["BUEN ESTADO, SIN SIGNOS", "Retraso sin patología"]),
               ("> 3 sem", "Retraso", ["Revisar uraco, infección"]),
               ("> 30 días", "Sospechoso", ["Con leucocitosis: déficit de adhesión"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Observar y cuidado seco", ["Limpiar con agua y secar"], True),
             (2, "Control en 1-2 semanas", ["Educar sobre signos de alarma"], False),
             (3, "Estudiar si hay signos", ["Onfalitis, fiebre, secreción"], False)]},
  ["El déficit de adhesión leucocitaria da infecciones sin pus y leucocitosis.",
   "Orina por el ombligo: uraco persistente.",
   "El alcohol en el cordón puede retrasar su caída."],
  NELSON + " · OMS – Recomendaciones sobre la atención postnatal (2022)")

# REU-055 · tarjetas
V("tarjetas", "REU-055", "gram-cocos-racimos-liquido-sinovial-drenaje-antibioticos", "Artritis séptica por estafilococo",
  "REUMATOLOGÍA ENAM: TRATAMIENTO DE LA ARTRITIS SÉPTICA", "REUMATOLOGÍA",
  ("Artritis séptica", ["Cocos grampositivos en racimos = Staphylococcus aureus",
   "El pus destruye el cartílago: drenar + antibiótico EV"]),
  ("Mujer de 35 años con artritis de rodilla", ["Gram del líquido sinovial: cocos grampositivos en racimos"]),
  {"rotulo": "¿Qué conducta es la correcta?", "ans": 0, "cards": [
      {"titulo": "DRENAJE + ANTIBIÓTICO EV", "datos": [
          ("Foco", "Se evacúa", True), ("Germen", "Se trata", True),
          ("Cartílago", "Se protege", True)],
       "pie": "Oxacilina o cefazolina"},
      {"titulo": "Antibiótico + AINE", "datos": [
          ("Foco", "Queda el pus", False), ("Germen", "Se trata", False),
          ("Cartílago", "Se daña", False)],
       "pie": "Insuficiente"},
      {"titulo": "Drenaje + AINE", "datos": [
          ("Foco", "Se evacúa", False), ("Germen", "Sin tratar", False),
          ("Cartílago", "Sigue en riesgo", False)],
       "pie": "Insuficiente"},
      {"titulo": "Lavado continuo", "datos": [
          ("Foco", "Parcial", False), ("Germen", "Sin antibiótico", False),
          ("Cartílago", "En riesgo", False)],
       "pie": "No es estándar"}]},
  ["El drenaje puede ser por aspiraciones repetidas o artroscopia.",
   "Si hay riesgo de SARM, iniciar vancomicina.",
   "Duración: 2-4 semanas, parte EV y parte oral."],
  "BSR – Guideline for the management of the hot swollen joint (2006, actualización) · " + HARRISON)

# NRL-048 · termómetro
V("termometro", "NRL-048", "migrana-mas-4-episodios-mes-profilaxis-propranolol", "Migraña: ¿cuándo prevenir?",
  "NEUROLOGÍA ENAM: PROFILAXIS DE LA MIGRAÑA", "NEUROLOGÍA",
  ("Tratamiento de la migraña", ["Crisis: AINE o triptanes",
   "Con ≥ 4 días de migraña al mes o crisis incapacitantes: profilaxis diaria"]),
  ("Mujer de 25 años con migraña", ["Más de 4 episodios al mes", "¿Qué evita las recurrencias?"]),
  {"rotulo": "Frecuencia de crisis",
   "niveles": [("< 4 / mes", "Episódica baja", ["Solo tratar las crisis"]),
               ("≥ 4 / mes", "Frecuente", ["> 4 CRISIS AL MES", "Iniciar profilaxis"]),
               ("≥ 15 / mes", "Crónica", ["Profilaxis + evitar abuso de analgésicos"])],
   "caso_nivel": 1, "ruta_titulo": "Profilaxis", "paso_label": "PASO",
   "pasos": [(1, "Propranolol", ["40-160 mg/día; evitar en asma"], True),
             (2, "Alternativas", ["Topiramato, amitriptilina, flunarizina"], False),
             (3, "Evaluar a los 2-3 meses", ["Meta: reducir 50 % las crisis"], False)]},
  ["El sumatriptán y el ibuprofeno tratan la crisis, no la previenen.",
   "Llevar un diario de cefaleas para medir el efecto del tratamiento.",
   "El tramadol no se recomienda en migraña."],
  "AHS – Consensus statement on integrating new migraine treatments (Headache 2021) · EHF (2022)")

# CB-070 · tarjetas
V("tarjetas", "CB-070", "preescolar-pobreza-edema-hiporreflexia-tiamina", "Déficit de vitaminas del complejo B",
  "CIENCIAS BÁSICAS ENAM: DÉFICIT DE TIAMINA (BERIBERI)", "CIENCIAS BÁSICAS",
  ("Beriberi", ["La tiamina (B1) es cofactor del metabolismo de la glucosa",
   "Seco: neuropatía, hiporreflexia · Húmedo: edema e insuficiencia cardiaca"]),
  ("Preescolar de 3 años en pobreza extrema", ["Fatiga, anorexia, diarrea, calambres", "Adelgazado, edematoso, pálido, reflejos muy disminuidos"]),
  {"rotulo": "¿Qué vitamina falta?", "ans": 0, "cards": [
      {"titulo": "TIAMINA (B1)", "datos": [
          ("Nervio", "Hiporreflexia", True), ("Corazón", "Edema, falla", True),
          ("Piel", "Normal", False), ("Otro", "Calambres", True)],
       "pie": "Beriberi"},
      {"titulo": "Niacina (B3)", "datos": [
          ("Nervio", "Demencia", False), ("Corazón", "Normal", False),
          ("Piel", "Dermatitis expuesta", False), ("Otro", "Diarrea", False)],
       "pie": "Pelagra: 3 D"},
      {"titulo": "Riboflavina (B2)", "datos": [
          ("Nervio", "Normal", False), ("Corazón", "Normal", False),
          ("Piel", "Queilitis, glositis", False), ("Otro", "Conjuntivitis", False)],
       "pie": "Boca y ojos"},
      {"titulo": "Piridoxina (B6)", "datos": [
          ("Nervio", "Neuropatía, convulsiones", False), ("Corazón", "Normal", False),
          ("Piel", "Dermatitis", False), ("Otro", "Anemia", False)],
       "pie": "Isoniacida"}]},
  ["Fuentes de tiamina: carnes, legumbres, cereales integrales.",
   "La falta de lactancia materna y la dieta pobre favorecen el déficit.",
   "Responde rápido a la tiamina oral o parenteral."],
  "OMS – Thiamine deficiency and its prevention (1999) · " + NELSON)

# END-053 · radial
V("radial", "END-053", "obeso-imc-38-orlistat-agregar-ejercicio-aerobico", "Tratamiento de la obesidad",
  "ENDOCRINOLOGÍA ENAM: OBESIDAD", "ENDOCRINOLOGÍA",
  ("Obesidad", ["El tratamiento se basa en dieta, actividad física y cambio de conducta",
   "Los fármacos y la cirugía se suman a esa base, no la reemplazan"]),
  ("Varón de 38 años con IMC 38", ["Obeso desde los 17 años, rebotes de peso", "Se automedica con orlistat"]),
  {"rotulo": "Mapa del tema", "centro": "OBESIDAD", "centro_sub": "Pilares", "ans": 0,
   "items": [("EJERCICIO AERÓBICO", ["150-300 min por semana", "Mantiene el peso perdido"]),
             ("Dieta hipocalórica", ["Déficit de 500-750 kcal/día"]),
             ("Terapia conductual", ["Hábitos, apoyo"]),
             ("Fármacos", ["Orlistat, arGLP-1"]),
             ("Cirugía bariátrica", ["IMC ≥ 40 o ≥ 35 con comorbilidad"])],
   "ruta": ["IMC 38", "Solo fármaco", "Falta actividad física", "EJERCICIO AERÓBICO"]},
  ["La metformina no es un tratamiento de la obesidad.",
   "Ninguna dieta 'de moda' supera a la hipocalórica sostenida.",
   "Con IMC 38 y comorbilidad podría ser candidato a cirugía."],
  "AACE – Clinical practice guideline for obesity (2016; actualización 2023) · USPSTF (2018)")

# OFT-041 · fases
V("fases", "OFT-041", "nino-insecto-vivo-oido-aceite-mineral", "Insecto vivo en el oído",
  "OTORRINOLARINGOLOGÍA ENAM: CUERPO EXTRAÑO ANIMADO", "OTORRINOLARINGOLOGÍA",
  ("Insecto en el conducto auditivo", ["El insecto vivo se mueve, duele y puede lesionar el tímpano",
   "Primero se inmoviliza con aceite; luego se extrae"]),
  ("Niño de 6 años", ["3 horas de dolor de oído", "Otoscopia: insecto vivo que se mueve"]),
  {"rotulo": "Pasos", "ans": 0,
   "fases": [("Inmovilizar", "Primero", "ACEITE MINERAL", ["O lidocaína", "Ahoga al insecto"]),
             ("Extraer", "Después", "Pinza o lavado", ["Bajo visión directa"]),
             ("Revisar", "Final", "Otoscopia", ["Integridad del tímpano"])],
   "curvas": [],
   "chips_titulo": "Manejo inicial · marcado el correcto",
   "chips": [("Aceite mineral", True), ("Lavado con salino", False), ("Pinza directa", False), ("Agua oxigenada", False)]},
  ["Intentar sacarlo vivo lo hace moverse más y lesionar el conducto.",
   "No usar agua oxigenada: irrita y puede dañar si hay perforación.",
   "Si no sale fácil: otorrinolaringólogo con microscopio."],
  "AAFP – Removal of foreign bodies from the ear and nose (2007, actualización 2022) · Cummings Otolaryngology 7.ª ed. (2020)")

# GAS-063 · puntaje
V("puntaje", "GAS-063", "dolor-colico-cede-defecar-diarrea-estrenimiento-intestino-irritable", "Dolor abdominal con cambio del hábito",
  "GASTROENTEROLOGÍA ENAM: SÍNDROME DE INTESTINO IRRITABLE", "GASTROENTEROLOGÍA",
  ("Síndrome de intestino irritable", ["Trastorno funcional: dolor abdominal recurrente ligado a la defecación",
   "Criterios de Roma IV: dolor + ≥ 2 de 3 criterios asociados"]),
  ("Mujer de 35 años, vendedora", ["1 año de dolor cólico y borborigmos que ceden al defecar", "Distensión, diarrea que alterna con estreñimiento · examen normal"]),
  {"rotulo": "Criterios de Roma IV", "escala": "Roma IV (con dolor recurrente)", "total": 3, "max": 3,
   "total_label": "Criterios asociados",
   "interpreta": "Cumple: intestino irritable mixto",
   "items": [("Relacionado con la defecación", "1", True), ("Cambio en la frecuencia de las heces", "1", True),
             ("Cambio en la forma de las heces", "1", True)],
   "bandas": [("0-1", "No cumple", "Buscar otra causa", False),
              ("≥ 2", "Intestino irritable", "Dieta, fibra soluble, antiespasmódico", True)]},
  ["Signos de alarma: sangrado, baja de peso, inicio > 50 años, anemia, síntomas nocturnos.",
   "Dispepsia funcional: dolor epigástrico, no ligado a la defecación.",
   "Dieta baja en FODMAP y manejo del estrés ayudan."],
  "Rome Foundation – Rome IV criteria (2016) · ACG – Clinical guideline: management of IBS (2021)")

# SP-135 · matriz
V("matriz", "SP-135", "colegio-80-sobrepeso-comunicacion-educativa-grupal", "Intervención ante obesidad escolar",
  "SALUD PÚBLICA ENAM: COMUNICACIÓN EDUCATIVA", "SALUD PÚBLICA",
  ("Promoción de la salud en la escuela", ["Con un grupo definido y un problema común: educación grupal",
   "Rápida, participativa y dirigida a esa población"]),
  ("Colegio secundario", ["80 % de alumnos de último año con sobrepeso u obesidad", "Médico responsable de la estrategia de no transmisibles"]),
  {"rotulo": "Intervención y alcance", "eje_x": "Rasgo", "eje_y": "Intervención",
   "cols": ["Alcance", "¿Inmediata y viable?"], "rows": ["Comunicación educativa grupal", "Consultas nutricionales", "Clausura del quiosco", "Difusión radial"], "caso": (0, 1),
   "cells": [[("Todo el grupo afectado", ["Participativa"]), ("SÍ: PRIORITARIA", [])],
             [("Uno por uno", []), ("Lenta para el 80 %", [])],
             [("Entorno escolar", []), ("No es competencia del médico", [])],
             [("Población general", []), ("Poco dirigida", [])]]},
  ["Luego se trabaja con la escuela para un quiosco saludable (Ley 30021).",
   "Involucrar a padres y docentes.",
   "Medir peso y talla para seguir el efecto."],
  "Ley N.° 30021 – Promoción de la alimentación saludable para niños, niñas y adolescentes · MINSA – Lineamientos de promoción de la salud")

# GIN-185 · termómetro
V("termometro", "GIN-185", "quiste-ovarico-simple-4-cm-observacion", "Quiste de ovario en la mujer joven",
  "GINECOLOGÍA ENAM: QUISTE OVÁRICO SIMPLE", "GINECOLOGÍA",
  ("Quiste ovárico simple", ["Unilocular, pared fina, sin tabiques ni partes sólidas",
   "En edad fértil suele ser funcional y desaparece solo"]),
  ("Mujer de 25 años asintomática", ["Ecografía de rutina", "Quiste unilocular de 4 cm en ovario derecho, sin tabiques"]),
  {"rotulo": "Tamaño y aspecto",
   "niveles": [("≤ 5 cm", "Simple pequeño", ["4 CM, UNILOCULAR", "Funcional"]),
               ("5-7 cm", "Simple mayor", ["Control ecográfico"]),
               ("> 7 cm", "Grande o complejo", ["RM o cirugía"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Observación", ["No requiere tratamiento"], True),
             (2, "Eco de control si persiste", ["En 6-12 semanas o si hay síntomas"], False),
             (3, "Cirugía si hay signos de riesgo", ["Tabiques, sólido, ascitis, dolor"], False)]},
  ["Los anticonceptivos no aceleran la resolución del quiste.",
   "La AFP se pide en tumores sólidos de células germinales.",
   "Dolor súbito con quiste: descartar torsión."],
  "ACOG – Practice Bulletin 174: Evaluation and management of adnexal masses (2016) · SRU consensus (2019)")

# OFT-042 · matriz
V("matriz", "OFT-042", "amoladora-cuerpo-extrano-penetrante-analgesia-ev", "Trauma ocular penetrante",
  "OFTALMOLOGÍA ENAM: GLOBO OCULAR ABIERTO", "OFTALMOLOGÍA",
  ("Globo abierto", ["El ojo no se toca ni se presiona: riesgo de salida del contenido",
   "Analgesia y antiemético EV, escudo rígido y cirugía urgente"]),
  ("Varón de 38 años con amoladora, sin protector", ["Dolor intenso, lagrimeo, ojo rojo", "Cuerpo metálico que atraviesa córnea, iris y cristalino"]),
  {"rotulo": "¿Qué se hace y qué no?", "eje_x": "Rasgo", "eje_y": "Medida",
   "cols": ["¿Se hace?", "Motivo"], "rows": ["Analgesia EV", "Escudo rígido", "Parche compresivo", "Colirio o tonometría"], "caso": (0, 0),
   "cells": [[("SÍ: INICIAL", ["Con antiemético"]), ("Evita pujar y vomitar", [])],
             [("Sí", []), ("Protege sin presionar", [])],
             [("NO", []), ("Expulsa el contenido", [])],
             [("NO", []), ("Presiona o contamina", [])]]},
  ["No retirar el cuerpo extraño fuera del quirófano.",
   "Profilaxis antitetánica y antibiótico sistémico.",
   "TC de órbitas (nunca RM con cuerpo metálico)."],
  "AAO – Open globe injury management (EyeWiki 2024) · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# CIR-099 · embudo
V("embudo", "CIR-099", "fracturas-costales-9-10-izquierdas-liquido-libre-bazo", "Trauma en el hipocondrio izquierdo",
  "CIRUGÍA ENAM: TRAUMA ESPLÉNICO", "CIRUGÍA",
  ("Lesión esplénica", ["Fracturas de las costillas izquierdas bajas (9.ª-11.ª) orientan al bazo",
   "Es el órgano que más sangra en el trauma cerrado"]),
  ("Varón de 45 años tras accidente de tránsito", ["Equimosis y crepitación en 9.ª-10.ª costillas izquierdas", "FAST: ~300 ml de líquido libre"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hemoperitoneo con fracturas costales izquierdas",
   "candidatos": ["Bazo", "Cola de páncreas", "Fondo gástrico", "Ángulo esplénico"],
   "pasos": [("Sangre libre: órgano sólido", ["Fondo gástrico", "Ángulo esplénico"]),
             ("El páncreas es retroperitoneal: poco hemoperitoneo", ["Cola de páncreas"])],
   "final": ("LESIÓN DEL BAZO", ["Estable: TC y manejo no operatorio", "Inestable: laparotomía"]),
   "nota": "Signo de Kehr: dolor en el hombro izquierdo por irritación del diafragma."},
  ["El manejo no operatorio se usa en pacientes estables.",
   "Tras esplenectomía: vacunas contra neumococo, meningococo y Haemophilus.",
   "Rotura en dos tiempos: sangrado días después del trauma."],
  ATLS + " · WSES – Splenic trauma guidelines (2017)")

# CB-071 · matriz
V("matriz", "CB-071", "lactancia-succion-aumenta-oxitocina", "Hormonas de la lactancia",
  "CIENCIAS BÁSICAS ENAM: REFLEJO DE EYECCIÓN", "CIENCIAS BÁSICAS",
  ("Reflejo de succión", ["La succión del pezón estimula el hipotálamo",
   "Neurohipófisis: oxitocina (eyección) · adenohipófisis: prolactina (producción)"]),
  ("Mujer de 30 años amamantando", ["¿Qué cambio hormonal se espera?"]),
  {"rotulo": "Hormona y efecto", "eje_x": "Rasgo", "eje_y": "Hormona",
   "cols": ["Cambio", "Efecto"], "rows": ["Oxitocina", "Prolactina", "FSH y LH", "Vasopresina"], "caso": (0, 0),
   "cells": [[("AUMENTA", ["Neurohipófisis"]), ("Eyección de leche", ["Contrae mioepitelio y útero"])],
             [("Aumenta", []), ("Produce la leche", [])],
             [("Disminuyen", []), ("Amenorrea de la lactancia", [])],
             [("Sin cambio relevante", []), ("Agua corporal", [])]]},
  ["La oxitocina también contrae el útero: menos sangrado posparto.",
   "El estrés inhibe el reflejo de eyección.",
   "Método MELA: lactancia exclusiva + amenorrea + < 6 meses."],
  GUYTON)

# GIN-186 · termómetro
V("termometro", "GIN-186", "vih-carga-viral-1500-37-semanas-evitar-parto-vaginal", "VIH y vía del parto",
  "OBSTETRICIA ENAM: VIH EN EL EMBARAZO", "OBSTETRICIA",
  ("Prevención de la transmisión vertical", ["La vía del parto depende de la carga viral al final del embarazo",
   "Con > 1000 copias/ml el parto vaginal aumenta el riesgo para el RN"]),
  ("Gestante de 37 semanas con TARGA", ["Carga viral 1500 copias/ml", "1 cm, −1, borramiento 100 %, membranas íntegras"]),
  {"rotulo": "Carga viral cerca del parto",
   "niveles": [("< 50", "Indetectable", ["Parto vaginal permitido"]),
               ("50-999", "Baja", ["Individualizar"]),
               ("≥ 1000", "Alta", ["1500 COPIAS/ML", "Parto vaginal: la conducta más riesgosa"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Cesárea", ["Idealmente antes de romper membranas"], True),
             (2, "Zidovudina EV intraparto", ["Desde 3 h antes de la cesárea"], False),
             (3, "Continuar TARGA + profilaxis al RN", ["Sin lactancia materna"], False)]},
  ["La cesárea protege más si se hace antes del trabajo de parto y con membranas íntegras.",
   "Evitar amniotomía, episiotomía y fórceps.",
   "El RN recibe antirretrovirales desde las primeras horas."],
  "MINSA – NTS 159: Prevención de la transmisión materno infantil del VIH, sífilis y hepatitis B · NIH – Perinatal HIV guidelines (2024)")

# CIR-100 · tarjetas
V("tarjetas", "CIR-100", "pie-frio-sin-pulsos-paralisis-embolia-arterial", "Isquemia aguda de la pierna",
  "CIRUGÍA ENAM: EMBOLIA ARTERIAL", "CIRUGÍA",
  ("Isquemia arterial aguda", ["Las 6 P: dolor, palidez, sin pulso, parestesia, parálisis, frialdad",
   "Inicio súbito sin enfermedad vascular previa = embolia (origen cardiaco)"]),
  ("Mujer de 60 años sin vasculopatía previa", ["Dolor en pie y pantorrilla derechos", "Sin pulso pedio ni poplíteo · fría · hipoestesia · no mueve"]),
  {"rotulo": "¿Qué la causa?", "ans": 0, "cards": [
      {"titulo": "EMBOLIA ARTERIAL", "datos": [
          ("Inicio", "Súbito", True), ("Antes", "Sin claudicación", True),
          ("Otra pierna", "Pulsos normales", False), ("Fuente", "FA, IMA", False)],
       "pie": "Heparina + embolectomía urgente"},
      {"titulo": "Trombosis aterosclerótica", "datos": [
          ("Inicio", "Progresivo", False), ("Antes", "Claudicación", False),
          ("Otra pierna", "Pulsos débiles", False), ("Fuente", "Placa", False)],
       "pie": "Colaterales: menos grave"},
      {"titulo": "TVP", "datos": [
          ("Inicio", "Días", False), ("Antes", "Inmovilización", False),
          ("Otra pierna", "Normal", False), ("Fuente", "Venosa", False)],
       "pie": "Pierna caliente y edematosa"},
      {"titulo": "Espasmo arterial", "datos": [
          ("Inicio", "Transitorio", False), ("Antes", "Fármacos, frío", False),
          ("Otra pierna", "Normal", False), ("Fuente", "Vasoconstricción", False)],
       "pie": "Cede solo"}]},
  ["Parálisis y pérdida sensitiva = isquemia que amenaza la extremidad.",
   "Tiempo crítico: 6 horas para revascularizar.",
   "Buscar fibrilación auricular con ECG."],
  "ESVS – Clinical practice guidelines on acute limb ischaemia (2020)")

# NEF-075 · embudo
V("embudo", "NEF-075", "piuria-esteril-urocultivo-negativo-tuberculosis-urogenital", "Piuria con urocultivo negativo",
  "NEFROLOGÍA ENAM: TUBERCULOSIS UROGENITAL", "NEFROLOGÍA",
  ("Piuria estéril", ["Leucocitos en orina con urocultivo negativo y pH ácido",
   "Causa clásica: tuberculosis urogenital"]),
  ("Mujer de 30 años", ["5 meses de molestias urinarias recurrentes", "pH ácido · 60 leucocitos/campo · urocultivo negativo"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Síntomas urinarios crónicos con piuria",
   "candidatos": ["TB urogenital", "Cistitis crónica", "Pielonefritis crónica", "Absceso perirrenal"],
   "pasos": [("Urocultivo común negativo", ["Cistitis crónica", "Pielonefritis crónica"]),
             ("Sin fiebre alta, masa ni dolor lumbar intenso", ["Absceso perirrenal"])],
   "final": ("TUBERCULOSIS UROGENITAL", ["Baciloscopía y cultivo en 3 orinas de la mañana", "GeneXpert en orina"]),
   "nota": "La TB renal viene de siembra hematógena años después de la infección pulmonar."},
  ["Otras causas de piuria estéril: clamidia, litiasis, uso previo de antibióticos.",
   "Puede causar estenosis ureteral y vejiga pequeña.",
   "Tratamiento con el esquema antituberculoso estándar."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · Campbell-Walsh-Wein Urology 12.ª ed. (2020)")

# TRA-042 · tarjetas
V("tarjetas", "TRA-042", "caida-mano-extendida-dolor-tabaquera-escafoides", "Dolor de muñeca tras una caída",
  "TRAUMATOLOGÍA ENAM: FRACTURA DE ESCAFOIDES", "TRAUMATOLOGÍA",
  ("Fractura de escafoides", ["Caída sobre la mano en hiperextensión",
   "Dolor en la tabaquera anatómica: tratar como fractura aunque la Rx sea normal"]),
  ("Varón de 32 años", ["Caída con apoyo de la mano izquierda en hiperextensión", "Dolor a la palpación de la tabaquera anatómica"]),
  {"rotulo": "¿Qué lesión es?", "ans": 0, "cards": [
      {"titulo": "FRACTURA DE ESCAFOIDES", "datos": [
          ("Dolor", "Tabaquera anatómica", True), ("Mecanismo", "Hiperextensión", True),
          ("Rx", "A veces normal al inicio", False), ("Riesgo", "Necrosis, seudoartrosis", False)],
       "pie": "Inmovilizar con férula del pulgar"},
      {"titulo": "Luxación del semilunar", "datos": [
          ("Dolor", "Centro de la muñeca", False), ("Mecanismo", "Hiperextensión fuerte", False),
          ("Rx", "Signo de la taza", False), ("Riesgo", "Compresión del mediano", False)],
       "pie": "Reducción urgente"},
      {"titulo": "Fractura de Colles", "datos": [
          ("Dolor", "Radio distal", False), ("Mecanismo", "Caída, anciana", False),
          ("Rx", "Dorso de tenedor", False), ("Riesgo", "Consolidación viciosa", False)],
       "pie": "Reducción y yeso"},
      {"titulo": "Ganchoso", "datos": [
          ("Dolor", "Eminencia hipotenar", False), ("Mecanismo", "Golpe con raqueta", False),
          ("Rx", "Proyección túnel carpiano", False), ("Riesgo", "Nervio cubital", False)],
       "pie": "Poco frecuente"}]},
  ["Si la Rx inicial es normal: inmovilizar y repetir en 10-14 días o hacer TC/RM.",
   "El polo proximal tiene irrigación retrógrada: riesgo de necrosis avascular.",
   "Es el hueso del carpo que más se fractura."],
  "AAOS – Scaphoid fractures (OrthoInfo 2023) · Rockwood and Green's Fractures in Adults 10.ª ed. (2024)")

# PED-182 · matriz
V("matriz", "PED-182", "lactante-6-meses-diarrea-vomitos-deshidratacion-rotavirus", "Diarrea aguda en el lactante",
  "PEDIATRÍA ENAM: GASTROENTERITIS POR ROTAVIRUS", "PEDIATRÍA",
  ("Rotavirus", ["Principal causa de diarrea grave en menores de 2 años",
   "Vómitos al inicio + diarrea acuosa abundante, a menudo con deshidratación"]),
  ("Lactante de 6 meses con lactancia exclusiva", ["8 h: 6 deposiciones líquidas y 2 vómitos · afebril", "Pierde 1,1 kg · labios secos, ojos hundidos"]),
  {"rotulo": "Agente y rasgos", "eje_x": "Rasgo", "eje_y": "Agente",
   "cols": ["Heces", "Paciente típico"], "rows": ["Rotavirus", "Giardia", "Campylobacter", "Shigella"], "caso": (0, 0),
   "cells": [[("ACUOSAS + VÓMITOS", ["Sin sangre"]), ("Lactante < 2 años", ["Deshidratación rápida"])],
             [("Grasosas, fétidas", []), ("Preescolar, curso crónico", [])],
             [("Con sangre", ["Dolor intenso"]), ("Contacto con aves", [])],
             [("Disentería", ["Fiebre alta"]), ("Preescolar, guardería", [])]]},
  ["Deshidratación con ~14 % de pérdida de peso: plan de rehidratación EV.",
   "Vacuna contra rotavirus a los 2 y 4 meses.",
   "No usar antibióticos en la diarrea acuosa viral."],
  "OMS – Tratamiento de la diarrea: manual para médicos (2005) · " + NELSON)

# GAS-064 · puntaje
V("puntaje", "GAS-064", "pancreatitis-alcoholica-60-anos-ranson-edad", "Criterios de Ranson al ingreso",
  "GASTROENTEROLOGÍA ENAM: PRONÓSTICO DE LA PANCREATITIS", "GASTROENTEROLOGÍA",
  ("Criterios de Ranson", ["Cinco al ingreso y seis a las 48 horas",
   "Cada criterio suma un punto; ≥ 3 predice pancreatitis grave"]),
  ("Varón de 60 años, alcohólico crónico", ["Dolor en faja de 24 horas · amilasa y lipasa altas", "Leucocitos 11 000 · AST 100 · bilirrubina 2"]),
  {"rotulo": "Ranson al ingreso (no biliar)", "escala": "Ranson al ingreso", "total": 1, "max": 5,
   "total_label": "Criterios cumplidos",
   "interpreta": "Solo cumple la edad",
   "items": [("Edad > 55 años", "1", True), ("Leucocitos > 16 000", "1", False),
             ("Glucosa > 200 mg/dl", "1", False), ("LDH > 350 UI/L", "1", False),
             ("AST > 250 UI/L", "1", False)],
   "bandas": [("0-2", "Leve", "Mortalidad baja", True),
              ("3-5", "Grave", "Mortalidad 10-20 %", False),
              ("≥ 6", "Muy grave", "Mortalidad > 50 %", False)]},
  ["La bilirrubina no forma parte de los criterios de Ranson.",
   "A las 48 h: caída del Hto, BUN, calcio, PaO₂, déficit de base, secuestro de líquidos.",
   "Hoy se prefieren BISAP y la falla orgánica persistente (Atlanta)."],
  "Ranson JH (Surg Gynecol Obstet 1974) · ACG – Guideline: Management of acute pancreatitis (2024)")

# SP-136 · árbol
A("SP-136", "incapacidad-mental-ligadura-evaluacion-psiquiatrica-judicial", "Esterilización en una persona incapaz",
  "SALUD PÚBLICA ENAM: ANTICONCEPCIÓN QUIRÚRGICA Y CONSENTIMIENTO", "SALUD PÚBLICA",
  ("Consentimiento para la esterilización", ["Es un método definitivo: requiere consentimiento libre de la propia persona",
   "Si no puede darlo, deciden un psiquiatra y un juez, no la familia"]),
  ("Mujer en edad reproductiva con alteración mental severa", ["Los familiares piden una ligadura de trompas"]),
  Q("¿Puede dar consentimiento informado?", [
      L("Sí", "Consentimiento propio", ["Con consejería y plazo de reflexión"]),
      L("No", "PSIQUIATRÍA + JUEZ", ["Evaluación psiquiátrica", "Autorización judicial"], path=True)], path=True),
  ("¿Quién puede autorizar?", [("Juez", True), ("Familia", False), ("Junta médica", False)], [
      ("Valor legal", ["Sí, con informe psiquiátrico", "No basta", "No basta"]),
      ("Motivo", ["Protege derechos", "Conflicto de intereses", "No sustituye al juez"])]),
  ["La esterilización forzada vulnera derechos humanos.",
   "Considerar primero métodos reversibles de larga duración.",
   "Toda decisión se documenta en la historia clínica."],
  "MINSA – Norma técnica de planificación familiar · Código Civil peruano (curatela) · Ley N.° 29889 (salud mental)")

# CIR-101 · radial
V("radial", "CIR-101", "nino-golpe-abdominal-hipocalcemia-pancreas", "Trauma abdominal cerrado en el niño",
  "CIRUGÍA ENAM: TRAUMA PANCREÁTICO", "CIRUGÍA",
  ("Lesión pancreática", ["Golpe epigástrico (manubrio, pelota) comprime el páncreas contra la columna",
   "Puede manifestarse días después; la hipocalcemia apoya la pancreatitis traumática"]),
  ("Niño de 12 años", ["Golpe jugando baloncesto hace 3 días", "Dolor abdominal, palidez · leucocitos 18 000 · Hb 10 · Ca 6"]),
  {"rotulo": "Mapa del tema", "centro": "TRAUMA CERRADO", "centro_sub": "¿Qué órgano?", "ans": 0,
   "items": [("PÁNCREAS", ["Síntomas tardíos, hipocalcemia", "Amilasa y lipasa altas"]),
             ("Bazo", ["Hemoperitoneo precoz"]),
             ("Hígado", ["Transaminasas altas"]),
             ("Intestino", ["Neumoperitoneo, peritonitis"]),
             ("Riñón", ["Hematuria"])],
   "ruta": ["Golpe epigástrico", "3 días después", "Calcio 6", "PÁNCREAS"]},
  ["La TC con contraste evalúa el conducto pancreático.",
   "El calcio se consume en la necrosis grasa (saponificación).",
   "Lesión del conducto: puede requerir cirugía o CPRE."],
  ATLS + " · " + NELSON)

# CIR-102 · puntaje
V("puntaje", "CIR-102", "mujer-30-dolor-fid-fiebre-leucocitosis-alvarado-ecografia", "Dolor en fosa ilíaca derecha en la mujer joven",
  "CIRUGÍA ENAM: APENDICITIS AGUDA EN LA MUJER", "CIRUGÍA",
  ("Apendicitis aguda", ["La escala de Alvarado estima la probabilidad",
   "En la mujer joven la ecografía descarta causas ginecológicas"]),
  ("Mujer de 30 años con 18 h de dolor en FID", ["Náuseas y vómitos · T 38 °C", "Leucocitos 12 000 con 8 % de abastonados"]),
  {"rotulo": "Escala de Alvarado en el caso", "escala": "Alvarado", "total": 7, "max": 10,
   "total_label": "Puntaje del caso",
   "interpreta": "Probable apendicitis: confirmar con ecografía",
   "items": [("Dolor en fosa ilíaca derecha", "2", True), ("Leucocitos > 10 000", "2", True),
             ("Náuseas o vómitos", "1", True), ("Fiebre ≥ 37,3 °C", "1", True),
             ("Desviación a la izquierda", "1", True), ("Dolor que migra a FID", "1", False),
             ("Anorexia", "1", False), ("Rebote", "1", False)],
   "bandas": [("1-4", "Poco probable", "Observar", False),
              ("5-6", "Posible", "Imagen y reevaluar", False),
              ("7-10", "Probable", "Ecografía y cirujano", True)]},
  ["Ecografía: apéndice > 6 mm, no compresible; además ve ovarios y trompas.",
   "Test de embarazo en toda mujer en edad fértil con dolor abdominal.",
   "La Rx simple y el tránsito no diagnostican apendicitis."],
  "WSES – Jerusalem guidelines on acute appendicitis (2020) · SAGES (2023)")
