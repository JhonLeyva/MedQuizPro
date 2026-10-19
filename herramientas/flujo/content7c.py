"""Bloque 7 · parte C."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"

# NEU-045 · tarjetas
V("tarjetas", "NEU-045", "gestante-tuberculosis-estreptomicina-ototoxica", "Antituberculosos en el embarazo",
  "NEUMOLOGÍA ENAM: TUBERCULOSIS EN LA GESTANTE", "NEUMOLOGÍA",
  ("Tuberculosis y embarazo", ["El esquema con isoniacida, rifampicina, pirazinamida y etambutol es seguro",
   "La estreptomicina daña el VIII par del feto: sordera congénita"]),
  ("Pregunta de farmacología", ["¿Qué antituberculoso está contraindicado en la gestante?"]),
  {"rotulo": "¿Es seguro en la gestación?", "ans": 0, "cards": [
      {"titulo": "ESTREPTOMICINA", "datos": [
          ("Grupo", "Aminoglucósido", True), ("Feto", "Ototoxicidad, sordera", True),
          ("Embarazo", "CONTRAINDICADA", True)],
       "pie": "Evitar también amikacina y kanamicina"},
      {"titulo": "Rifampicina", "datos": [
          ("Grupo", "Primera línea", False), ("Feto", "Sin daño probado", False),
          ("Embarazo", "Segura", False)],
       "pie": "Dar vitamina K al RN"},
      {"titulo": "Pirazinamida", "datos": [
          ("Grupo", "Primera línea", False), ("Feto", "Sin daño probado", False),
          ("Embarazo", "Segura (OMS)", False)],
       "pie": "Vigilar hígado"},
      {"titulo": "Etambutol", "datos": [
          ("Grupo", "Primera línea", False), ("Feto", "Sin daño probado", False),
          ("Embarazo", "Segura", False)],
       "pie": "Controlar la visión"}]},
  ["La isoniacida se acompaña de piridoxina en la gestante.",
   "La TB no tratada es mucho más peligrosa que los fármacos de primera línea.",
   "La lactancia no se suspende durante el tratamiento."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · OMS – Consolidated guidelines on tuberculosis, módulo 4 (2025)")

# GIN-156 · árbol
A("GIN-156", "madre-rh-negativo-rn-rh-negativo-sin-anti-d", "Profilaxis anti-D después del parto",
  "OBSTETRICIA ENAM: ISOINMUNIZACIÓN RH", "OBSTETRICIA",
  ("Profilaxis anti-D", ["Solo sirve si la madre Rh(−) puede recibir sangre fetal Rh(+)",
   "Si el recién nacido es Rh(−), no hay riesgo de sensibilización Rh"]),
  ("Madre de 32 años Rh negativo", ["Recién nacido Rh negativo", "Coombs directo positivo"]),
  Q("¿Madre Rh negativo no sensibilizada?", [
      Q("¿Recién nacido Rh positivo?", [
          L("Sí", "Anti-D en 72 h", ["300 µg IM"]),
          L("No", "NO INDICAR PROFILAXIS", ["No hay antígeno D que sensibilice", "Coombs (+): buscar ABO u otros"], path=True)],
        edge="Sí", path=True),
      L("Ya sensibilizada", "Sin utilidad", ["Seguir en la próxima gestación"])], path=True),
  ("Anti-D en la madre Rh(−)", [("Cuándo", True), ("Detalle", False)], [
      ("Prenatal", ["28 semanas", "Si la pareja es Rh(+) o desconocida"]),
      ("Posparto", ["≤ 72 h", "Solo si el RN es Rh(+)"]),
      ("Eventos", ["Aborto, ectópico, amniocentesis", "Sangrado o trauma"])]),
  ["El Coombs directo positivo en un RN Rh(−) orienta a incompatibilidad ABO o de otros grupos.",
   "La inmunoglobulina anti-D no sirve si la madre ya tiene anticuerpos.",
   "Test de Kleihauer-Betke si la hemorragia feto-materna es grande."],
  "ACOG – Practice Bulletin 181: Prevention of Rh D alloimmunization (2017) · " + WILLIAMS)

# GIN-157 · puntaje
V("puntaje", "GIN-157", "embarazo-42-semanas-bishop-4-misoprostol", "Embarazo prolongado: ¿inducir o madurar?",
  "OBSTETRICIA ENAM: MADURACIÓN CERVICAL", "OBSTETRICIA",
  ("Embarazo en vías de prolongación", ["A las 41-42 semanas se termina la gestación",
   "El índice de Bishop decide: cuello desfavorable = madurar primero"]),
  ("Gestante de 42 semanas por ecografía temprana", ["Test no estresante normal", "Cuello posterior, consistencia media, 40 %, −2, 1 cm"]),
  {"rotulo": "Índice de Bishop en el caso", "escala": "Bishop", "total": 4, "max": 13,
   "total_label": "Puntaje del cuello",
   "interpreta": "Cuello desfavorable: madurar",
   "items": [("Dilatación 1 cm", "1", True), ("Borramiento 40 %", "1", True), ("Estación −2", "1", True),
             ("Consistencia media", "1", True), ("Posición posterior", "0", False)],
   "bandas": [("≤ 6", "Desfavorable", "Madurar con misoprostol 25 µg vaginal", True),
              ("≥ 8", "Favorable", "Inducir con oxitocina", False)]},
  ["La oxitocina funciona mal con un cuello inmaduro.",
   "Con cesárea previa no se usa misoprostol.",
   "Pasadas las 42 semanas aumenta la muerte fetal: no se espera."],
  "ACOG – Practice Bulletin 146: Management of late-term and postterm pregnancies (2014) · OMS – Recomendaciones para la inducción del trabajo de parto (2022)")

# GIN-158 · fases
V("fases", "GIN-158", "formula-obstetrica-aborto-ectopico-g4p1021", "Fórmula obstétrica",
  "OBSTETRICIA ENAM: FÓRMULA OBSTÉTRICA", "OBSTETRICIA",
  ("Fórmula G_P abcd", ["G: todas las gestaciones, incluida la actual",
   "a término · b pretérmino · c abortos (el ectópico cuenta aquí) · d hijos vivos"]),
  ("Gestante actual", ["Antecedentes: 1 aborto, 1 ectópico, 1 parto a término", "1 hijo vivo"]),
  {"rotulo": "Cómo se arma la fórmula", "ans": 3,
   "fases": [("G", "Gestas", "4", ["Actual + aborto + ectópico + parto"]),
             ("a", "A término", "1", ["El parto a término"]),
             ("b", "Pretérmino", "0", ["Ninguno"]),
             ("c", "Abortos", "2 (ABORTO + ECTÓPICO)", ["El ectópico se cuenta como aborto"]),
             ("d", "Hijos vivos", "1", ["Un hijo vivo"])],
   "curvas": [],
   "chips_titulo": "Fórmula del caso · marcada la correcta",
   "chips": [("G4 P1021", True), ("G3 P1011", False), ("G3 P1021", False), ("G4 P2021", False)]},
  ["La gestación actual siempre suma a G.",
   "Molas y ectópicos se registran como abortos en la HCP.",
   "Un parto gemelar cuenta como un solo parto, pero dos hijos vivos."],
  "CLAP/OPS – Historia Clínica Perinatal: instructivo de llenado (2017)")

# REU-048 · matriz
V("matriz", "REU-048", "mujer-joven-leucorrea-artritis-diplococos-gram-negativos", "Artritis séptica: qué se ve en el Gram",
  "REUMATOLOGÍA ENAM: ARTRITIS GONOCÓCICA", "REUMATOLOGÍA",
  ("Artritis séptica en el adulto joven", ["Mujer sexualmente activa con leucorrea y artritis = gonococo",
   "Neisseria gonorrhoeae: diplococos gramnegativos"]),
  ("Mujer de 23 años", ["3 días de fiebre, artralgias en muñecas y rodilla", "Leucorrea · rodilla derecha caliente y roja"]),
  {"rotulo": "Germen y tinción", "eje_x": "Rasgo", "eje_y": "Germen",
   "cols": ["Gram o tinción", "Paciente típico"], "rows": ["Gonococo", "S. aureus", "Borrelia", "Candida"], "caso": (0, 0),
   "cells": [[("DIPLOCOCOS GRAMNEGATIVOS", ["Intracelulares"]), ("Joven sexualmente activo", ["Tenosinovitis, pústulas"])],
             [("Cocos grampositivos", ["En racimos"]), ("La causa más frecuente", ["Adultos y niños"])],
             [("Espiroquetas", []), ("Picadura de garrapata", ["Enfermedad de Lyme"])],
             [("Hifas o levaduras", []), ("Inmunodeprimido", [])]]},
  ["El cultivo del líquido articular sale positivo en menos del 50 %: cultivar cérvix y uretra.",
   "Tratamiento: ceftriaxona 1 g EV diario.",
   "Tratar también Chlamydia y a la pareja."],
  "CDC – Sexually transmitted infections treatment guidelines (2021; actualización 2024) · " + HARRISON)

# REU-049 · radial
V("radial", "REU-049", "eritema-malar-derrame-cilindros-plaquetopenia-lupus", "Enfermedad multisistémica en la mujer joven",
  "REUMATOLOGÍA ENAM: LUPUS ERITEMATOSO SISTÉMICO", "REUMATOLOGÍA",
  ("Lupus eritematoso sistémico", ["Afecta piel, articulaciones, serosas, sangre y riñón",
   "Cilindros en la orina = nefritis lúpica activa"]),
  ("Mujer de 25 años", ["Artritis de manos, eritema malar, alopecia, derrame pleural", "Hb 10 · plaquetas 40 000 · hematíes y cilindros en orina"]),
  {"rotulo": "Mapa del tema", "centro": "ARTRITIS + SISTÉMICO", "centro_sub": "Mujer joven", "ans": 0,
   "items": [("LUPUS ERITEMATOSO SISTÉMICO", ["Piel, serosas, sangre y riñón", "ANA y anti-ADN"]),
             ("Artritis reumatoide", ["Poliartritis simétrica, sin nefritis"]),
             ("Dermatomiositis", ["Heliotropo, debilidad proximal"]),
             ("Gota", ["Monoartritis, varón"]),
             ("Esclerosis sistémica", ["Piel dura, Raynaud"])],
   "ruta": ["Artritis + eritema malar", "Derrame pleural", "Plaquetas bajas y cilindros", "LES"]},
  ["Criterios EULAR/ACR 2019: ANA ≥ 1:80 como entrada y suma ≥ 10 puntos.",
   "Anti-ADN y complemento bajo reflejan actividad renal.",
   "Hidroxicloroquina para todos; nefritis: micofenolato o ciclofosfamida."],
  "EULAR/ACR – Classification criteria for SLE (2019) · EULAR – Recommendations for the management of SLE (2023)")

# END-046 · termómetro
V("termometro", "END-046", "gestante-10-semanas-graves-propiltiouracilo", "Hipertiroidismo en el embarazo",
  "ENDOCRINOLOGÍA ENAM: ENFERMEDAD DE GRAVES EN LA GESTANTE", "ENDOCRINOLOGÍA",
  ("Graves y embarazo", ["El antitiroideo cambia según el trimestre",
   "Primer trimestre: propiltiouracilo (el metimazol es teratógeno)"]),
  ("Gestante de 10 semanas", ["Temblor, nervios, baja de peso, intolerancia al calor", "Exoftalmos, mixedema pretibial, bocio · TSH 0,01 · T4L alta"]),
  {"rotulo": "Momento de la gestación",
   "niveles": [("1.er trim.", "Hasta 16 semanas", ["10 SEMANAS", "Propiltiouracilo"]),
               ("2.º-3.er", "Desde 16 semanas", ["Cambiar a metimazol"]),
               ("Lactancia", "Posparto", ["Metimazol a dosis bajas"])],
   "caso_nivel": 0, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Propiltiouracilo", ["Dosis mínima para T4L en el límite alto"], True),
             (2, "Propranolol breve", ["Para temblor y taquicardia"], False),
             (3, "Nunca yodo radiactivo", ["Destruye la tiroides fetal"], False)]},
  ["El metimazol en el primer trimestre produce aplasia cutis y embriopatía.",
   "El PTU es hepatotóxico: por eso se cambia en el segundo trimestre.",
   "La levotiroxina es para el hipotiroidismo, no para Graves."],
  "ATA – Guidelines for the diagnosis and management of thyroid disease during pregnancy and the postpartum (2017)")

# END-047 · matriz
V("matriz", "END-047", "cuello-doloroso-postviral-tiroiditis-subaguda-aine", "Tirotoxicosis: ¿qué la causa?",
  "ENDOCRINOLOGÍA ENAM: TIROIDITIS SUBAGUDA", "ENDOCRINOLOGÍA",
  ("Tiroiditis subaguda (de Quervain)", ["Tiroides dolorosa tras una infección viral",
   "Tirotoxicosis por destrucción: no sirven los antitiroideos"]),
  ("Mujer de 35 años", ["Dolor cervical, nervios y temblor · IRA hace 10 días", "Taquicardia · bocio doloroso · TSH 0,2"]),
  {"rotulo": "Causa, captación y tratamiento", "eje_x": "Rasgo", "eje_y": "Causa",
   "cols": ["Dolor y captación", "Tratamiento"], "rows": ["Tiroiditis subaguda", "Graves", "Tiroiditis silente"], "caso": (0, 1),
   "cells": [[("Dolorosa · captación baja", ["VSG alta"]), ("AINE + PROPRANOLOL", ["Prednisona si es intensa"])],
             [("Indolora · captación alta", ["Exoftalmos"]), ("Metimazol", ["Yodo o cirugía"])],
             [("Indolora · captación baja", ["Posparto"]), ("Propranolol", ["Autolimitada"])]]},
  ["Evoluciona en fases: tirotoxicosis, hipotiroidismo transitorio y recuperación.",
   "Propiltiouracilo y metimazol no actúan: la hormona ya estaba formada.",
   "La levotiroxina solo si el hipotiroidismo posterior da síntomas."],
  "ATA – Guidelines for diagnosis and management of hyperthyroidism and other causes of thyrotoxicosis (2016)")

# END-048 · termómetro
V("termometro", "END-048", "hba1c-9-5-glucosa-450-creatinina-alta-insulina", "Diabetes tipo 2 descompensada",
  "ENDOCRINOLOGÍA ENAM: INSULINIZACIÓN EN LA DIABETES TIPO 2", "ENDOCRINOLOGÍA",
  ("Intensificar el tratamiento", ["Glucosa ≥ 300 o HbA1c > 10 %, o síntomas: iniciar insulina",
   "Con creatinina alta se limitan metformina y sulfonilureas"]),
  ("Varón de 57 años con metformina 2 g/día", ["HbA1c 9,5 % · glucosa 450 mg/dl", "Creatinina 2,3 · visión disminuida"]),
  {"rotulo": "Grado de descontrol",
   "niveles": [("< 7 %", "En meta", ["Mantener"]),
               ("7-9 %", "Descontrol moderado", ["Agregar un segundo fármaco"]),
               ("> 9 %", "Descontrol grave", ["GLUCOSA 450 + FALLA RENAL", "Insulina"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Iniciar insulina", ["Basal 10 U o 0,1-0,2 U/kg", "Ajustar según glucosa en ayunas"], True),
             (2, "Ajustar metformina a la TFG", ["Suspender si TFG < 30"], False),
             (3, "Evitar glibenclamida", ["Hipoglucemia prolongada en falla renal"], False)]},
  ["La insulina es segura en cualquier grado de falla renal.",
   "Los iSGLT2 y arGLP-1 protegen riñón y corazón cuando se estabilice.",
   "La hemodiálisis no trata la hiperglucemia."],
  "ADA – Standards of Care in Diabetes 2025 · KDIGO – Diabetes management in CKD (2022)")

# NRL-044 · radial
V("radial", "NRL-044", "desinhibicion-euforia-descuido-sindrome-prefrontal", "Síndromes lobares",
  "NEUROLOGÍA ENAM: SÍNDROME PREFRONTAL", "NEUROLOGÍA",
  ("Lóbulo frontal", ["La corteza prefrontal controla juicio, conducta y funciones ejecutivas",
   "Su daño da desinhibición, euforia, apatía e incontinencia"]),
  ("Varón de 58 años, 7 meses de conducta inadecuada", ["Euforia, irritable, se orina y se desnuda en la sala", "Descuido personal, no se concentra ni decide"]),
  {"rotulo": "Mapa del tema", "centro": "LÓBULOS CEREBRALES", "centro_sub": "¿Qué función se pierde?", "ans": 0,
   "items": [("PREFRONTAL", ["Desinhibición, euforia, juicio", "Incontinencia sin preocupación"]),
             ("Parietal", ["Negligencia, agnosias, apraxia"]),
             ("Temporal", ["Memoria, afasia de Wernicke"]),
             ("Occipital", ["Hemianopsia, alucinaciones visuales"]),
             ("Cerebelo", ["Ataxia, dismetría"])],
   "ruta": ["Cambio de conducta", "Desinhibición y euforia", "Fallan juicio y decisiones", "PREFRONTAL"]},
  ["Causas: tumor frontal, demencia frontotemporal, trauma.",
   "Pedir RM cerebral ante cambio de personalidad en un adulto.",
   "La incontinencia frontal ocurre sin que el paciente se preocupe."],
  "Adams y Victor. Principios de Neurología 12.ª ed. (2023)")

# NRL-045 · tarjetas
V("tarjetas", "NRL-045", "cefalea-en-banda-semanal-cede-aine-tensional", "Cefaleas primarias",
  "NEUROLOGÍA ENAM: CEFALEA TENSIONAL", "NEUROLOGÍA",
  ("Cefalea tensional", ["La cefalea primaria más frecuente",
   "Bilateral, opresiva 'en vincha', leve a moderada, sin náuseas"]),
  ("Mujer de 29 años con 9 meses de cefalea semanal", ["2-6 horas, como una venda apretada", "Cede con AINE · contractura cervical"]),
  {"rotulo": "¿Qué cefalea es?", "ans": 0, "cards": [
      {"titulo": "TENSIONAL", "datos": [
          ("Localización", "Bilateral", True), ("Carácter", "Opresiva, en banda", True),
          ("Síntomas", "Sin náuseas", False), ("Duración", "30 min a 7 días", True)],
       "pie": "AINE o paracetamol"},
      {"titulo": "Migraña", "datos": [
          ("Localización", "Unilateral", False), ("Carácter", "Pulsátil", False),
          ("Síntomas", "Náuseas, fotofobia", False), ("Duración", "4-72 h", False)],
       "pie": "Triptanes"},
      {"titulo": "En racimos", "datos": [
          ("Localización", "Periocular", False), ("Carácter", "Terebrante", False),
          ("Síntomas", "Lagrimeo, rinorrea", False), ("Duración", "15-180 min", False)],
       "pie": "Oxígeno al 100 %"},
      {"titulo": "Temporomandibular", "datos": [
          ("Localización", "Preauricular", False), ("Carácter", "Al masticar", False),
          ("Síntomas", "Chasquido", False), ("Duración", "Variable", False)],
       "pie": "Férula, odontología"}]},
  ["Evitar abusar de analgésicos: causa cefalea por uso excesivo.",
   "Si es crónica (≥ 15 días/mes): amitriptilina preventiva.",
   "Signos de alarma: inicio súbito, fiebre, déficit focal, > 50 años."],
  "IHS – Clasificación internacional de las cefaleas ICHD-3 (2018)")

# NRL-046 · embudo
V("embudo", "NRL-046", "fibrilacion-auricular-afasia-hemiparesia-tac-normal", "Déficit súbito con TC normal",
  "NEUROLOGÍA ENAM: ACV ISQUÉMICO CARDIOEMBÓLICO", "NEUROLOGÍA",
  ("ACV en la fibrilación auricular", ["La FA sin anticoagular forma trombos en la aurícula que embolizan",
   "En las primeras horas la TC del infarto isquémico es normal"]),
  ("Varón de 72 años con FA sin anticoagulación", ["Hace 2 h: afasia y hemiparesia derecha que aumentan", "TC cerebral sin alteraciones"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Déficit neurológico focal agudo",
   "candidatos": ["ACV isquémico", "Hemorragia intracerebral", "Hemorragia subaracnoidea", "Hematoma epidural"],
   "pasos": [("Sin trauma ni cefalea en trueno", ["Hematoma epidural", "Hemorragia subaracnoidea"]),
             ("TC sin sangre a las 2 horas", ["Hemorragia intracerebral"])],
   "final": ("ACV ISQUÉMICO CARDIOEMBÓLICO", ["Trombólisis EV si < 4,5 h", "Trombectomía si hay oclusión grande"]),
   "nota": "La TC normal no descarta isquemia: descarta sangrado para poder trombolizar."},
  ["Tras el ACV: anticoagular (ACOD) para prevenir recurrencia.",
   "CHA₂DS₂-VASc ≥ 2 en varones indica anticoagulación.",
   "La RM con difusión muestra el infarto en minutos."],
  "AHA/ASA – Guidelines for the early management of acute ischemic stroke (2019) · ESC – Guidelines for atrial fibrillation (2024)")

# REU-050 · matriz
V("matriz", "REU-050", "placas-escamas-nacaradas-una-en-dedal-psoriasis", "Placas descamativas",
  "DERMATOLOGÍA ENAM: PSORIASIS", "DERMATOLOGÍA",
  ("Psoriasis", ["Placas eritematosas con escama nacarada en codos, rodillas y cuero cabelludo",
   "Uñas en dedal (piqueteado); puede llegar a eritrodermia"]),
  ("Varón de 43 años con 1 mes de eritrodermia", ["Placas con escamas nacaradas en codos, rodillas, cuero cabelludo", "Uñas con puntos (en dedal)"]),
  {"rotulo": "Lesión y localización", "eje_x": "Rasgo", "eje_y": "Enfermedad",
   "cols": ["Lesión", "Dónde"], "rows": ["Psoriasis", "Dermatitis atópica", "Linfoma cutáneo", "Celulitis"], "caso": (0, 0),
   "cells": [[("PLACA CON ESCAMA NACARADA", ["Uñas en dedal", "Auspitz (+)"]), ("Extensoras, cuero cabelludo", [])],
             [("Eccema, liquenificación", ["Prurito intenso"]), ("Flexuras", [])],
             [("Placas o tumores", ["Micosis fungoide"]), ("Tronco, zonas no expuestas", [])],
             [("Eritema caliente difuso", ["Fiebre"]), ("Pierna, unilateral", [])]]},
  ["La psoriasis eritrodérmica es grave: vigilar temperatura y líquidos.",
   "Evitar corticoides sistémicos: al retirarlos empeora (rebote).",
   "Formas moderadas-graves: metotrexato o biológicos."],
  "AAD-NPF – Guidelines of care for the management of psoriasis (2019-2020) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# PED-156 · puntaje
V("puntaje", "PED-156", "escolar-amigdalas-pus-petequias-paladar-estreptococo", "Faringitis: ¿bacteriana?",
  "PEDIATRÍA ENAM: FARINGOAMIGDALITIS ESTREPTOCÓCICA", "PEDIATRÍA",
  ("Faringoamigdalitis estreptocócica", ["Fiebre, exudado amigdalino, petequias en paladar y adenopatías",
   "En niños suele dar dolor abdominal y vómitos"]),
  ("Escolar de 8 años con 2 días de fiebre", ["Dolor de garganta, disfagia, vómitos, dolor abdominal", "Amígdalas con pus · petequias en paladar blando"]),
  {"rotulo": "Escala de McIsaac en el caso", "escala": "Centor / McIsaac", "total": 3, "max": 5,
   "total_label": "Puntaje del caso",
   "interpreta": "Probable estreptococo: prueba rápida o cultivo",
   "items": [("Fiebre > 38 °C", "1", True), ("Exudado o hipertrofia amigdalar", "1", True),
             ("Edad 3-14 años", "1", True), ("Adenopatía cervical anterior dolorosa", "1", False),
             ("Ausencia de tos", "1", False)],
   "bandas": [("0-1", "Viral probable", "Sin antibiótico ni prueba", False),
              ("2-3", "Intermedio", "Prueba rápida o cultivo", True),
              ("4-5", "Alto", "Prueba y tratar si es positiva", False)]},
  ["Las petequias en el paladar apoyan mucho el origen estreptocócico.",
   "Tratamiento: amoxicilina 10 días o penicilina benzatínica IM.",
   "Tratar previene la fiebre reumática."],
  "IDSA – Clinical practice guideline for group A streptococcal pharyngitis (2012) · " + NELSON)

# SP-121 · árbol
A("SP-121", "experimento-variable-dependiente-se-observan-cambios", "¿Qué es la variable dependiente?",
  "SALUD PÚBLICA ENAM: VARIABLE DEPENDIENTE", "SALUD PÚBLICA",
  ("Variables en un experimento", ["La independiente se manipula; la dependiente se mide",
   "En la dependiente se observan los cambios (el efecto)"]),
  ("Diseño experimental", ["¿Cómo se define la variable dependiente?"]),
  Q("¿El investigador la manipula?", [
      L("Sí", "Independiente", ["Produce el efecto", "Es la causa"]),
      Q("¿En ella se observan los cambios?", [
          L("Sí", "DEPENDIENTE", ["Es el efecto que se mide", "Resultado del estudio"], path=True),
          L("No", "Interviniente o de control", ["Se controla o ajusta"])],
        edge="No", path=True)], path=True),
  ("Variables del experimento", [("Dependiente", True), ("Independiente", False)], [
      ("Papel", ["Efecto", "Causa"]),
      ("Quién decide su valor", ["Lo que ocurre en el sujeto", "El investigador"]),
      ("En el gráfico", ["Eje Y", "Eje X"])]),
  ["Truco: la dependiente 'depende' de la independiente.",
   "El tipo de investigador no define las variables.",
   "Toda hipótesis relaciona al menos una independiente con una dependiente."],
  "Hernández-Sampieri. Metodología de la investigación 7.ª ed. (2023)")

# PSI-031 · fases
V("fases", "PSI-031", "postoperado-alucinaciones-zoopsias-temblor-delirium-tremens", "Abstinencia alcohólica en el hospital",
  "PSIQUIATRÍA ENAM: DELIRIUM TREMENS", "PSIQUIATRÍA",
  ("Síndrome de abstinencia alcohólica", ["Aparece cuando el bebedor crónico deja de beber, por ejemplo al hospitalizarse",
   "Delirium tremens: confusión, alucinaciones visuales, fiebre y descarga autonómica"]),
  ("Varón de 40 años, 2.º día poscirugía de fémur", ["Bebe > 40 g de alcohol al día", "Confuso, ve serpientes · FC 100, 38 °C, temblor, sudoración"]),
  {"rotulo": "Horas desde la última copa", "ans": 3,
   "fases": [("Temblor", "6-24 h", "Abstinencia leve", ["Ansiedad, temblor, sudor"]),
             ("Alucinosis", "12-48 h", "Alucinaciones", ["Con conciencia clara"]),
             ("Convulsiones", "24-48 h", "Tónico-clónicas", ["Generalizadas"]),
             ("Delirium", "48-96 h", "DELIRIUM TREMENS", ["Confusión + autonómico", "Mortalidad 5 %"])],
   "curvas": [("Riesgo", ROSE, [0.2, 0.35, 0.5, 0.6, 0.75, 0.9, 0.8])],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Síndrome de abstinencia", True), ("Embolia grasa", False), ("Hematoma subdural", False), ("Encefalopatía urémica", False)]},
  ["Tratamiento: benzodiacepinas (diazepam o lorazepam) y tiamina antes de la glucosa.",
   "Embolia grasa: petequias, hipoxemia y confusión a las 24-72 h de una fractura.",
   "Preguntar por consumo de alcohol a todo paciente que se opera."],
  "ASAM – Clinical practice guideline on alcohol withdrawal management (2020)")

# REU-051 · termómetro
V("termometro", "REU-051", "preescolar-citricos-habones-urticaria-aguda", "Reacción alérgica en la piel",
  "DERMATOLOGÍA ENAM: URTICARIA AGUDA", "DERMATOLOGÍA",
  ("Urticaria", ["Habones: pápulas o placas eritematosas con centro pálido, muy pruriginosas y fugaces",
   "Aguda (< 6 semanas): alimentos, infecciones, fármacos"]),
  ("Preescolar", ["Tras comer cítricos", "Pápulas eritematosas de centro pálido, muy pruriginosas"]),
  {"rotulo": "Gravedad de la reacción",
   "niveles": [("Piel", "Urticaria", ["HABONES PRURIGINOSOS", "Sin compromiso respiratorio"]),
               ("Piel +", "Angioedema", ["Labios, párpados"]),
               ("Sistémica", "Anafilaxia", ["Disnea, hipotensión, vómitos"])],
   "caso_nivel": 0, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Antihistamínico H1 de 2.ª generación", ["Cetirizina o loratadina"], True),
             (2, "Evitar el desencadenante", ["Cítricos, en este caso"], False),
             (3, "Adrenalina IM si hay anafilaxia", ["0,01 mg/kg en el muslo"], False)]},
  ["Cada habón dura menos de 24 horas y no deja marca.",
   "La dermatitis no forma habones fugaces; la tiña tiene borde descamativo.",
   "Los corticoides orales solo en cursos cortos si es intensa."],
  "EAACI/GA²LEN/WAO – International guideline for urticaria (Allergy 2022)")

# GIN-159 · tarjetas
V("tarjetas", "GIN-159", "puerpera-endometritis-clindamicina-gentamicina", "Antibiótico en la endometritis puerperal",
  "OBSTETRICIA ENAM: TRATAMIENTO DE LA ENDOMETRITIS", "OBSTETRICIA",
  ("Endometritis puerperal", ["Infección polimicrobiana: aerobios y anaerobios",
   "Esquema de elección: clindamicina + gentamicina EV"]),
  ("Puérpera con endometritis", ["¿Qué antibiótico es de elección?"]),
  {"rotulo": "¿Qué esquema cubre todo?", "ans": 0, "cards": [
      {"titulo": "CLINDAMICINA + GENTAMICINA", "datos": [
          ("Anaerobios", "Sí", True), ("Gramnegativos", "Sí", True),
          ("Eficacia", "Elección", True), ("Hasta", "24-48 h afebril", False)],
       "pie": "No requiere antibiótico oral después"},
      {"titulo": "Ampicilina-sulbactam", "datos": [
          ("Anaerobios", "Sí", False), ("Gramnegativos", "Parcial", False),
          ("Eficacia", "Alternativa", False), ("Hasta", "24-48 h afebril", False)],
       "pie": "Opción en alergia a clindamicina"},
      {"titulo": "Ceftriaxona + amoxicilina", "datos": [
          ("Anaerobios", "Poco", False), ("Gramnegativos", "Sí", False),
          ("Eficacia", "Insuficiente", False), ("Hasta", "—", False)],
       "pie": "No es esquema estándar"},
      {"titulo": "Clindamicina + dicloxacilina", "datos": [
          ("Anaerobios", "Sí", False), ("Gramnegativos", "No", False),
          ("Eficacia", "Insuficiente", False), ("Hasta", "—", False)],
       "pie": "Sin cobertura de gramnegativos"}]},
  ["Si la fiebre sigue a las 72 h: buscar absceso, hematoma o tromboflebitis pélvica.",
   "Agregar ampicilina si no mejora (cubre enterococo).",
   "La cesárea es el principal factor de riesgo."],
  WILLIAMS + " · OMS – Recommendations for prevention and treatment of maternal peripartum infections (2015)")

# REU-052 · embudo
V("embudo", "REU-052", "vesiculas-rascado-costras-mielicericas-impetigo", "Vesículas que dejan costras amarillas",
  "DERMATOLOGÍA ENAM: IMPÉTIGO", "DERMATOLOGÍA",
  ("Piodermitis superficial", ["Impétigo: vesículas que se rompen y dejan costras color miel",
   "Se contagia por rascado sobre piel dañada"]),
  ("Preescolar de 5 años con urticaria previa", ["Vesículas sobre zonas de rascado desde hace 4 días", "Erosiones húmedas con costras mielicéricas que se extienden"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Vesículas y costras en un niño",
   "candidatos": ["Impétigo", "Varicela", "Celulitis", "Erisipela"],
   "pasos": [("Lesión superficial, sin placa indurada ni fiebre", ["Celulitis", "Erisipela"]),
             ("Solo en zonas de rascado, costras color miel", ["Varicela"])],
   "final": ("PIODERMITIS (IMPÉTIGO)", ["Mupirocina o ácido fusídico tópico", "Oral si es extenso: cefalexina"]),
   "nota": "La costra mielicérica es el signo típico del impétigo."},
  ["Agentes: S. aureus y estreptococo del grupo A.",
   "Complicación del estreptocócico: glomerulonefritis posinfecciosa.",
   "Higiene, uñas cortas y no compartir toallas."],
  "IDSA – Practice guidelines for skin and soft tissue infections (2014) · " + NELSON)

# GIN-160 · radial
V("radial", "GIN-160", "gestante-aumentar-proteinas-necesidad-materno-fetal", "Nutrientes en el embarazo",
  "OBSTETRICIA ENAM: NUTRICIÓN EN LA GESTACIÓN", "OBSTETRICIA",
  ("Proteínas en la gestación", ["Se necesitan para el feto, la placenta, el útero, las mamas y la sangre materna",
   "Requerimiento: unos 25 g/día extra en el 2.º y 3.er trimestre"]),
  ("Pregunta de nutrición", ["¿Para qué aumentar las proteínas en el embarazo?"]),
  {"rotulo": "Mapa del tema", "centro": "NUTRIENTES", "centro_sub": "¿Para qué sirve cada uno?", "ans": 0,
   "items": [("PROTEÍNAS", ["Cubrir necesidades maternas y fetales", "Crecimiento de tejidos"]),
             ("Calcio", ["Reduce la preeclampsia"]),
             ("Hierro", ["Aumento de la masa eritrocitaria"]),
             ("Ácido fólico", ["Tubo neural"]),
             ("Energía", ["+300 kcal desde el 2.º trimestre"])],
   "ruta": ["Más tejidos que formar", "Feto, placenta, útero", "Más aminoácidos", "PROTEÍNAS"]},
  ["El volumen sanguíneo aumenta, no disminuye, en la gestación.",
   "El control del peso depende del balance calórico, no de las proteínas.",
   "Fuentes: carnes, huevo, lácteos, menestras."],
  "OMS – Recomendaciones sobre atención prenatal para una experiencia positiva del embarazo (2016) · " + WILLIAMS)

# OFT-035 · embudo
V("embudo", "OFT-035", "odinofagia-trismus-otalgia-absceso-periamigdalino", "Dolor de garganta con trismus",
  "OTORRINOLARINGOLOGÍA ENAM: ABSCESO PERIAMIGDALINO", "OTORRINOLARINGOLOGÍA",
  ("Absceso periamigdalino", ["Complicación de una amigdalitis: pus entre la amígdala y su cápsula",
   "Trismus, voz de 'papa caliente', otalgia refleja y úvula desviada"]),
  ("Varón de 21 años con 5 días de odinofagia y fiebre", ["Otalgia derecha y trismus", "Amígdala derecha abombada con pus"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Odinofagia con fiebre y dolor unilateral",
   "candidatos": ["Absceso amigdaliano", "Absceso submaxilar", "Uvulitis", "Edema de Quincke"],
   "pasos": [("Fiebre y pus: es infeccioso", ["Edema de Quincke"]),
             ("Amígdala abombada con trismus; piso de boca libre", ["Absceso submaxilar", "Uvulitis"])],
   "final": ("ABSCESO PERIAMIGDALINO", ["Punción o drenaje + antibiótico", "Amoxicilina-clavulánico o clindamicina"]),
   "nota": "La otalgia es referida por el IX par; el trismus, por irritación del pterigoideo."},
  ["Complicación grave: extensión al espacio parafaríngeo.",
   "Si recidiva: amigdalectomía.",
   "El absceso submaxilar abomba el piso de la boca (angina de Ludwig)."],
  "Cummings Otolaryngology Head and Neck Surgery 7.ª ed. (2020)")

# CIR-092 · puntaje
V("puntaje", "CIR-092", "escaldadura-brazos-tronco-anterior-36-por-ciento", "Superficie corporal quemada",
  "CIRUGÍA ENAM: REGLA DE LOS NUEVES", "CIRUGÍA",
  ("Regla de los nueves (Wallace)", ["En el adulto cada región vale 9 % o múltiplos",
   "Miembro superior 9 % · tronco anterior 18 % · tronco posterior 18 % · miembro inferior 18 %"]),
  ("Mujer de 20 años con agua hervida", ["Ambas caras de los dos miembros superiores", "Cara anterior del tronco"]),
  {"rotulo": "Suma de regiones del caso", "escala": "Regla de los nueves", "total": 36, "max": 100,
   "total_label": "Superficie corporal quemada (%)",
   "interpreta": "Quemadura extensa: reposición con Parkland",
   "items": [("Miembro superior derecho", "9", True), ("Miembro superior izquierdo", "9", True),
             ("Tronco anterior", "18", True), ("Tronco posterior", "18", False),
             ("Cabeza y cuello", "9", False), ("Miembros inferiores", "18 c/u", False), ("Periné", "1", False)],
   "bandas": [("< 20 %", "Menor", "Líquidos orales o de mantenimiento", False),
              ("≥ 20 %", "Extensa", "Parkland: 2-4 ml × kg × % en 24 h", True)]},
  ["Solo se cuentan quemaduras de 2.º y 3.er grado.",
   "La mitad del volumen de Parkland va en las primeras 8 horas.",
   "En niños la cabeza vale más: usar la tabla de Lund-Browder."],
  ATLS + " · ABA – Advanced Burn Life Support (2022)")

# GAS-056 · termómetro
V("termometro", "GAS-056", "ictericia-flapping-sangrado-hipoglucemia-falla-hepatica-aguda", "Falla hepática aguda",
  "GASTROENTEROLOGÍA ENAM: INSUFICIENCIA HEPÁTICA AGUDA", "GASTROENTEROLOGÍA",
  ("Insuficiencia hepática aguda", ["Ictericia + coagulopatía + encefalopatía en < 26 semanas, sin hepatopatía previa",
   "La hipoglucemia refleja que el hígado no produce glucosa"]),
  ("Mujer de 34 años", ["Ictericia hace 1 semana, luego vómitos y desorientación", "Soporosa, flapping (+), equimosis · glucosa 55"]),
  {"rotulo": "Grado de encefalopatía",
   "niveles": [("I", "Leve", ["Euforia, inversión del sueño"]),
               ("II", "Somnolencia", ["Desorientación, flapping"]),
               ("III", "Estupor", ["SOPOROSA + FLAPPING", "Responde a estímulos"]),
               ("IV", "Coma", ["No responde"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "UCI y centro de trasplante", ["Criterios del King's College"], True),
             (2, "Glucosa EV, proteger vía aérea", ["Corregir hipoglucemia"], False),
             (3, "Buscar la causa", ["Paracetamol: N-acetilcisteína", "Virus A, B, E, fármacos"], False)]},
  ["El INR ≥ 1,5 define la coagulopatía de la falla hepática aguda.",
   "Hipoglucemia sola no explica ictericia ni flapping.",
   "Absceso hepático: fiebre y dolor en hipocondrio derecho."],
  "AASLD – Position paper: management of acute liver failure (2022) · EASL – Clinical practice guidelines on acute liver failure (2017)")

# GAS-057 · radial
V("radial", "GAS-057", "melena-hematemesis-hipotension-shock-hipovolemico", "Tipos de shock",
  "GASTROENTEROLOGÍA ENAM: HEMORRAGIA DIGESTIVA ALTA", "GASTROENTEROLOGÍA",
  ("Shock hipovolémico", ["Pérdida de volumen: la sangre no llena el corazón",
   "Hemorragia digestiva con hipotensión y taquicardia"]),
  ("Mujer de 45 años con úlcera péptica mal tratada", ["Melena y hematemesis (2 tazas)", "PA 80/40 · FC 118 · ansiosa"]),
  {"rotulo": "Mapa del tema", "centro": "SHOCK", "centro_sub": "¿Qué falla?", "ans": 0,
   "items": [("HIPOVOLÉMICO", ["Falta volumen: sangrado, diarrea", "PVC baja, piel fría"]),
             ("Distributivo", ["Vasodilatación: sepsis, anafilaxia"]),
             ("Cardiogénico", ["Falla la bomba: infarto"]),
             ("Obstructivo", ["TEP, taponamiento, neumotórax"]),
             ("Neurogénico", ["Trauma medular, bradicardia"])],
   "ruta": ["Úlcera que sangra", "Melena y hematemesis", "Pierde volumen", "HIPOVOLÉMICO"]},
  ["Dos vías gruesas, cristaloides y transfusión si Hb < 7 g/dl.",
   "IBP en bolo EV y endoscopia en las primeras 24 h.",
   "Escala de Glasgow-Blatchford para decidir el alta o el ingreso."],
  "ACG – Guideline: Upper gastrointestinal and ulcer bleeding (Am J Gastroenterol 2021)")

# CB-060 · tarjetas
V("tarjetas", "CB-060", "covid-hipoxemia-neumocito-tipo-ii-ace2", "Células del alvéolo",
  "CIENCIAS BÁSICAS ENAM: NEUMOCITO TIPO II Y COVID-19", "CIENCIAS BÁSICAS",
  ("SARS-CoV-2 y el alvéolo", ["El virus entra por el receptor ACE2",
   "El neumocito tipo II lo expresa: se daña y cae el surfactante"]),
  ("Diabético de 58 años con sospecha de COVID-19", ["Dificultad respiratoria, SatO₂ 84 %", "Rx: compromiso alveolar marcado"]),
  {"rotulo": "¿Qué célula infecta el virus?", "ans": 0, "cards": [
      {"titulo": "NEUMOCITO TIPO II", "datos": [
          ("Función", "Surfactante, reparación", True), ("ACE2", "Abundante", True),
          ("Forma", "Cúbica", False), ("Cubre", "5 % del alvéolo", False)],
       "pie": "Blanco principal del SARS-CoV-2"},
      {"titulo": "Neumocito tipo I", "datos": [
          ("Función", "Intercambio de gases", False), ("ACE2", "Escaso", False),
          ("Forma", "Plana", False), ("Cubre", "95 % del alvéolo", False)],
       "pie": "No se divide"},
      {"titulo": "Macrófago alveolar", "datos": [
          ("Función", "Fagocitosis", False), ("ACE2", "Escaso", False),
          ("Forma", "Libre en el alvéolo", False), ("Cubre", "—", False)],
       "pie": "Libera citocinas"},
      {"titulo": "Célula en cepillo", "datos": [
          ("Función", "Quimiosensorial", False), ("ACE2", "Escaso", False),
          ("Forma", "Microvellosidades", False), ("Cubre", "Rara", False)],
       "pie": "En la vía aérea"}]},
  ["Sin neumocitos II no hay surfactante ni reparación: daño alveolar difuso.",
   "El neumocito II es la célula madre que regenera a los tipo I.",
   "La diabetes aumenta el riesgo de COVID-19 grave."],
  "Ross. Histología: texto y atlas 8.ª ed. (2020) · Robbins y Cotran. Patología estructural y funcional 10.ª ed. (2021)")

# NEF-069 · fases
V("fases", "NEF-069", "criptorquidia-bilateral-no-tratada-azoospermia", "Criptorquidia: evolución",
  "UROLOGÍA ENAM: CRIPTORQUIDIA BILATERAL", "UROLOGÍA",
  ("Criptorquidia", ["El testículo fuera del escroto sufre por la temperatura abdominal",
   "Bilateral sin tratar: daño de la espermatogénesis y azoospermia"]),
  ("Pregunta de urología", ["Testículos no descendidos en ambos lados", "¿Qué consecuencia tiene?"]),
  {"rotulo": "Evolución del testículo no descendido", "ans": 3,
   "fases": [("Fetal", "28-35 semanas", "Descenso normal", ["Por el conducto inguinal"]),
             ("Hasta 6 meses", "Lactante", "Esperar", ["Puede descender solo"]),
             ("6-18 meses", "Tratamiento", "Orquidopexia", ["Preserva la fertilidad"]),
             ("Sin tratar", "Adulto", "AZOOSPERMIA", ["Bilateral: infertilidad", "Más riesgo de cáncer"])],
   "curvas": [("Daño germinal", ROSE, [0.05, 0.1, 0.2, 0.35, 0.6, 0.85, 0.95])],
   "chips_titulo": "Consecuencia · marcada la correcta",
   "chips": [("Azoospermia", True), ("Teratospermia", False), ("Varicocele", False), ("Hidrocele", False)]},
  ["La orquidopexia antes de los 18 meses mejora la fertilidad, pero no elimina el riesgo de cáncer.",
   "Criptorquidia bilateral no palpable: descartar trastorno del desarrollo sexual.",
   "El seminoma es el tumor más asociado."],
  "AUA – Evaluation and treatment of cryptorchidism (2014; ratificada 2018) · EAU – Guidelines on paediatric urology (2025)")

# GIN-161 · termómetro
V("termometro", "GIN-161", "primigesta-37-sem-pa-140-proteinuria-preeclampsia", "Hipertensión en la gestante",
  "OBSTETRICIA ENAM: PREECLAMPSIA", "OBSTETRICIA",
  ("Trastornos hipertensivos del embarazo", ["Preeclampsia: PA ≥ 140/90 después de las 20 semanas + proteinuria ≥ 300 mg/24 h",
   "El edema ya no es criterio diagnóstico"]),
  ("Primigesta de 18 años, 37 semanas", ["Cefalea leve, alteraciones visuales ocasionales, edema", "PA 140/90 · proteinuria 500 mg/24 h · ROT normales"]),
  {"rotulo": "Espectro de la enfermedad",
   "niveles": [("HTA gest.", "Hipertensión gestacional", ["Sin proteinuria"]),
               ("PE", "Preeclampsia", ["PA 140/90 + PROTEINURIA", "Vigilar signos de severidad"]),
               ("PE grave", "Con criterios de severidad", ["PA ≥ 160/110, síntomas, órganos"]),
               ("Eclampsia", "Convulsiones", ["Sulfato de magnesio"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Terminar la gestación", ["A las 37 semanas se indica el parto"], True),
             (2, "Sulfato de magnesio", ["Si hay criterios de severidad"], False),
             (3, "Antihipertensivo", ["Si PA ≥ 160/110"], False)]},
  ["La cefalea y la visión borrosa persistentes son criterios de severidad.",
   "Hipertensión crónica: antes de las 20 semanas.",
   "Aspirina desde las 12 semanas en gestantes de riesgo previene la preeclampsia."],
  "ACOG – Practice Bulletin 222: Gestational hypertension and preeclampsia (2020) · MINSA – Guía de trastornos hipertensivos del embarazo")

# GIN-162 · radial
V("radial", "GIN-162", "agresion-sexual-profilaxis-gonorrea-chlamydia", "Atención de la violencia sexual",
  "GINECOLOGÍA ENAM: PROFILAXIS TRAS VIOLENCIA SEXUAL", "GINECOLOGÍA",
  ("Kit de emergencia tras violencia sexual", ["Idealmente en las primeras 72 horas",
   "Profilaxis bacteriana contra gonorrea y Chlamydia (± tricomonas)"]),
  ("Mujer de 18 años", ["Agresión sexual por desconocidos hace 3 horas", "¿Contra qué ITS se da antibiótico?"]),
  {"rotulo": "Mapa del tema", "centro": "KIT DE EMERGENCIA", "centro_sub": "< 72 horas", "ans": 0,
   "items": [("GONORREA Y CHLAMYDIA", ["Ceftriaxona + azitromicina", "± metronidazol (tricomonas)"]),
             ("VIH", ["TAR profiláctico 28 días"]),
             ("Embarazo", ["Levonorgestrel 1,5 mg"]),
             ("Hepatitis B", ["Vacuna ± inmunoglobulina"]),
             ("Apoyo y denuncia", ["Psicología, medicina legal"])],
   "ruta": ["Agresión hace 3 h", "Dentro de las 72 h", "Cubrir ITS bacterianas", "GONORREA Y CHLAMYDIA"]},
  ["La sífilis se vigila con serología a las 6 semanas.",
   "La vaginosis bacteriana no es una ITS que requiera profilaxis específica.",
   "Registrar y preservar evidencias con consentimiento."],
  "MINSA – Guía técnica para la atención integral de personas afectadas por violencia sexual · OMS – Responding to children and adolescents who have been sexually abused (2017)")

# PED-157 · embudo
V("embudo", "PED-157", "rn-distension-sin-meconio-fistula-uretral-ano-imperforado", "Recién nacido que no elimina meconio",
  "PEDIATRÍA ENAM: MALFORMACIÓN ANORRECTAL", "PEDIATRÍA",
  ("Obstrucción intestinal neonatal", ["Lo primero es inspeccionar el periné",
   "Ano imperforado: sin orificio anal; puede haber fístula a uretra o periné"]),
  ("RN varón de 20 horas, hijo de madre diabética", ["Distensión abdominal marcada, no elimina meconio", "Fístula uretral · periné posterior hipotrófico"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "RN sin meconio y con distensión",
   "candidatos": ["Ano imperforado", "Hirschsprung", "Íleo meconial", "Malrotación"],
   "pasos": [("Periné anormal con fístula uretral", ["Hirschsprung", "Íleo meconial"]),
             ("Sin vómitos biliosos precoces", ["Malrotación"])],
   "final": ("ANO IMPERFORADO", ["Colostomía y luego anorrectoplastia", "Buscar VACTERL"]),
   "nota": "Meconio en la orina = fístula rectouretral: malformación alta en el varón."},
  ["Asociación VACTERL: vértebras, ano, corazón, tráquea-esófago, riñón, extremidades.",
   "Hirschsprung: ano normal, sin meconio en 48 h; biopsia rectal.",
   "Íleo meconial: fibrosis quística."],
  NELSON + " · Holcomb and Ashcraft's Pediatric Surgery 7.ª ed. (2020)")

# CIR-093 · fases
V("fases", "CIR-093", "diabetica-claudicacion-necrosis-quinto-dedo-fontaine-iv", "Fontaine: del síntoma a la necrosis",
  "CIRUGÍA ENAM: ISQUEMIA CRÍTICA DE MIEMBRO", "CIRUGÍA",
  ("Clasificación de Fontaine", ["Estadios según los síntomas de la isquemia crónica",
   "Úlcera o necrosis = estadio IV (isquemia crítica)"]),
  ("Diabética de 67 años", ["9 meses de claudicación intermitente", "Ahora necrosis del 5.º dedo del pie izquierdo"]),
  {"rotulo": "Progresión de la enfermedad", "ans": 4,
   "fases": [("I", "Asintomático", "Pulsos débiles", ["ITB bajo"]),
             ("IIa", "> 200 m", "Claudicación leve", ["Ejercicio"]),
             ("IIb", "< 200 m", "Claudicación limitante", ["Cilostazol"]),
             ("III", "Reposo", "Dolor nocturno", ["Isquemia crítica"]),
             ("IV", "Lesión", "NECROSIS O ÚLCERA", ["Revascularizar"])],
   "curvas": [("Gravedad", ROSE, [0.05, 0.2, 0.35, 0.55, 0.75, 0.9, 1.0])],
   "chips_titulo": "Estadio del caso · marcado el correcto",
   "chips": [("IV", True), ("III", False), ("IIb", False), ("IIa", False)]},
  ["Estadios III y IV = isquemia crítica: riesgo de amputación.",
   "Tratamiento: revascularización endovascular o bypass.",
   "Controlar diabetes, dejar de fumar, estatina y antiagregante."],
  "ESC – Guidelines for the management of peripheral arterial and aortic diseases (2024) · GVG – Global vascular guidelines on CLTI (2019)")

# OFT-036 · matriz
V("matriz", "OFT-036", "conjuntivitis-folicular-papilar-otalgia-chlamydia-doxiciclina", "Conjuntivitis: tipo y tratamiento",
  "OFTALMOLOGÍA ENAM: CONJUNTIVITIS DE INCLUSIÓN", "OFTALMOLOGÍA",
  ("Conjuntivitis por Chlamydia", ["Adulto joven sexualmente activo con conjuntivitis folicular persistente",
   "Requiere tratamiento sistémico: doxiciclina o azitromicina"]),
  ("Mujer de 22 años", ["Ojo rojo con secreción purulenta moderada", "Folículos y papilas en la conjuntiva · otalgia"]),
  {"rotulo": "Tipo de conjuntivitis", "eje_x": "Rasgo", "eje_y": "Causa",
   "cols": ["Reacción y secreción", "Tratamiento"], "rows": ["Chlamydia", "Bacteriana", "Viral", "Alérgica"], "caso": (0, 1),
   "cells": [[("Folicular + papilar", ["Mucopurulenta, crónica"]), ("DOXICICLINA ORAL", ["O azitromicina 1 g"])],
             [("Papilar", ["Purulenta"]), ("Antibiótico tópico", [])],
             [("Folicular", ["Acuosa, adenopatía"]), ("Sintomático", [])],
             [("Papilar", ["Prurito, mucosa"]), ("Antihistamínico tópico", [])]]},
  ["Tratar también a la pareja y descartar otras ITS.",
   "En el recién nacido se trata con eritromicina oral.",
   "El cloranfenicol tópico no erradica Chlamydia."],
  "AAO – Preferred Practice Pattern: Conjunctivitis (2023) · CDC – STI treatment guidelines (2021)")

# CIR-094 · árbol
A("CIR-094", "adolescente-dolor-escrotal-subito-detorsion-orquidopexia", "Escroto agudo",
  "UROLOGÍA ENAM: TORSIÓN TESTICULAR", "UROLOGÍA",
  ("Escroto agudo en el adolescente", ["Dolor súbito e intenso = torsión hasta demostrar lo contrario",
   "El testículo se salva si se destuerce en menos de 6 horas"]),
  ("Varón de 14 años con 2 horas de dolor", ["Dolor escrotal intenso tras una noche de baile", "Testículo derecho doloroso, edema · transiluminación (−)"]),
  Q("¿Dolor súbito, reflejo cremastérico ausente?", [
      L("Sí", "DETORSIÓN + ORQUIDOPEXIA", ["Cirugía inmediata, < 6 h", "Fijar ambos testículos"], path=True),
      L("Punto azul en el polo superior", "Torsión de hidátide", ["Reposo y AINE"]),
      L("Inicio gradual, fiebre, disuria", "Orquiepididimitis", ["Antibióticos"])], path=True),
  ("Viabilidad según el tiempo", [("< 6 h", True), ("6-12 h", False), ("> 24 h", False)], [
      ("Rescate", ["90-100 %", "~50 %", "< 10 %"]),
      ("Conducta", ["Orquidopexia", "Orquidopexia si es viable", "Orquiectomía"])]),
  ["No esperar la ecografía Doppler si la clínica es clara.",
   "La orquidopexia es bilateral: el otro lado tiene el mismo defecto (badajo de campana).",
   "Prehn: elevar el testículo no alivia en la torsión."],
  "AUA/EAU – Guidelines on paediatric urology: acute scrotum (2025) · " + NELSON)

# CIR-095 · árbol
A("CIR-095", "herida-bala-mesogastrio-taquicardia-laparotomia", "Trauma abdominal penetrante",
  "CIRUGÍA ENAM: HERIDA ABDOMINAL POR ARMA DE FUEGO", "CIRUGÍA",
  ("Herida abdominal por proyectil", ["La bala que penetra el abdomen lesiona vísceras en más del 90 %",
   "Con dolor difuso o inestabilidad: laparotomía exploratoria"]),
  ("Varón de 23 años, balazo en mesogastrio hace 1 h", ["PA 100/60 · FC 110 · diaforético", "Dolor abdominal difuso"]),
  Q("¿Penetró la cavidad o hay peritonitis/choque?", [
      L("Sí", "LAPAROTOMÍA EXPLORATORIA", ["Sin demora en exámenes", "Antibiótico y transfusión según necesidad"], path=True),
      L("No: tangencial y estable", "Observación o TC", ["Solo en centros con experiencia"])], path=True),
  ("Arma blanca vs arma de fuego", [("Fuego", True), ("Blanca", False)], [
      ("Lesión visceral", ["> 90 %", "~30 %"]),
      ("Conducta estándar", ["Laparotomía", "Explorar o manejo selectivo"])]),
  ["No se busca la bala ni se explora la herida para extraerla.",
   "El FAST no cambia la conducta si ya hay indicación de laparotomía.",
   "Observar 12 h es peligroso en un paciente taquicárdico con dolor difuso."],
  ATLS + " · EAST – Practice management guideline for selective nonoperative management of penetrating abdominal trauma (2010)")

# GAS-058 · matriz
V("matriz", "GAS-058", "cancer-colorrectal-metastasis-higado-via-portal", "¿A dónde metastatiza cada cáncer?",
  "GASTROENTEROLOGÍA ENAM: METÁSTASIS DEL CÁNCER COLORRECTAL", "GASTROENTEROLOGÍA",
  ("Cáncer colorrectal", ["La sangre del colon va por la vena porta al hígado",
   "El hígado es el sitio más frecuente de metástasis"]),
  ("Pregunta de oncología", ["¿Dónde metastatiza con más frecuencia el cáncer colorrectal?"]),
  {"rotulo": "Tumor, vía y sitio", "eje_x": "Rasgo", "eje_y": "Tumor",
   "cols": ["Sitio más frecuente", "Vía"], "rows": ["Colon", "Recto bajo", "Próstata", "Mama"], "caso": (0, 0),
   "cells": [[("HÍGADO", ["20-25 % al diagnóstico"]), ("Vena porta", [])],
             [("Pulmón", ["Además de hígado"]), ("Venas hemorroidales → cava", [])],
             [("Hueso", ["Blásticas"]), ("Plexo de Batson", [])],
             [("Hueso", ["Líticas"]), ("Hematógena y linfática", [])]]},
  ["Las metástasis hepáticas resecables pueden curarse con cirugía.",
   "El CEA sirve para el seguimiento, no para el tamizaje.",
   "Tamizaje desde los 45-50 años: colonoscopia o sangre oculta."],
  "NCCN – Colon cancer (2025) · ESMO – Metastatic colorectal cancer guideline (2023)")

# OFT-037 · árbol
A("OFT-037", "golpe-ocular-pupila-deformada-hifema-proteger-derivar", "Trauma ocular cerrado",
  "OFTALMOLOGÍA ENAM: TRAUMA OCULAR CON HIFEMA", "OFTALMOLOGÍA",
  ("Trauma ocular grave", ["Pupila deformada o hifema sugieren lesión del globo",
   "Primero proteger el ojo sin presionar y derivar al oftalmólogo"]),
  ("Mujer de 40 años golpeada con un palo en el ojo", ["Pupila deformada, hematoma subconjuntival", "Hifema"]),
  Q("¿Signos de lesión intraocular?", [
      L("Sí: hifema, pupila irregular", "PROTEGER Y DERIVAR", ["Escudo rígido sin presión", "Cabecera elevada, derivación urgente"], path=True),
      L("No: solo hematoma subconjuntival", "Control ambulatorio", ["Lágrimas artificiales"])], path=True),
  ("Qué no hacer en el trauma ocular grave", [("Evitar", True), ("Por qué", False)], [
      ("Presionar el ojo", ["Parche compresivo", "Salida del contenido"]),
      ("Valsalva, esfuerzo", ["Pujar, toser", "Aumenta el sangrado"]),
      ("Gotas sin evaluar", ["Antibióticos, anestésicos", "Pueden entrar al ojo"])]),
  ["Sospechar globo abierto si la pupila está deformada.",
   "El hifema puede resangrar entre el 2.º y 5.º día.",
   "Evitar AINE y aspirina en el hifema."],
  "AAO – Preferred Practice Pattern: Traumatic hyphema · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# CB-061 · tarjetas
V("tarjetas", "CB-061", "agricultor-sialorrea-bradicardia-fasciculaciones-atropina", "Toxíndromes y antídotos",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR ORGANOFOSFORADOS", "CIENCIAS BÁSICAS",
  ("Síndrome colinérgico", ["Los organofosforados inhiben la acetilcolinesterasa",
   "Muscarínico (secreciones, bradicardia) + nicotínico (fasciculaciones)"]),
  ("Agricultor de 28 años con 8 h de síntomas", ["Dolor abdominal, vómitos, sialorrea", "FC 50 · fasciculaciones · roncantes difusos"]),
  {"rotulo": "¿Qué antídoto corresponde?", "ans": 0, "cards": [
      {"titulo": "ORGANOFOSFORADOS", "datos": [
          ("Pupilas", "Miosis", False), ("Secreciones", "Abundantes", True),
          ("FC", "Bradicardia", True), ("Antídoto", "ATROPINA", True)],
       "pie": "Hasta secar los bronquios · pralidoxima"},
      {"titulo": "Opioides", "datos": [
          ("Pupilas", "Puntiformes", False), ("Secreciones", "Normales", False),
          ("FC", "Normal o baja", False), ("Antídoto", "Naloxona", False)],
       "pie": "Depresión respiratoria"},
      {"titulo": "Benzodiacepinas", "datos": [
          ("Pupilas", "Normales", False), ("Secreciones", "Normales", False),
          ("FC", "Normal", False), ("Antídoto", "Flumazenilo", False)],
       "pie": "Sedación"},
      {"titulo": "Cumarínicos", "datos": [
          ("Pupilas", "Normales", False), ("Secreciones", "Normales", False),
          ("FC", "Normal", False), ("Antídoto", "Vitamina K", False)],
       "pie": "Sangrado, INR alto"}]},
  ["La meta de la atropina es secar las secreciones bronquiales, no la midriasis.",
   "Descontaminar: retirar la ropa y lavar la piel con agua y jabón.",
   "Síndrome intermedio: debilidad proximal a las 24-96 h."],
  "OMS – Clinical management of acute pesticide intoxication (2008) · Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")
