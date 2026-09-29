"""Bloque 6 · parte J."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
GUYTON = "Guyton y Hall – Tratado de fisiología médica 14.ª ed. (2021)"

# SP-091 · tarjetas
V("tarjetas", "SP-091", "primer-caso-identificado-servicio-caso-indice", "Tipos de caso en vigilancia",
  "SALUD PÚBLICA ENAM: CASO ÍNDICE", "SALUD PÚBLICA",
  ("Caso índice", ["Primer caso que el servicio de salud identifica",
   "A partir de él se investiga el brote y los contactos"]),
  ("Pregunta de concepto", ["Vigilancia epidemiológica", "Primer caso identificado en el servicio"]),
  {"rotulo": "¿Cómo se llama?", "ans": 0, "cards": [
      {"titulo": "CASO ÍNDICE", "datos": [
          ("Qué es", "Primero detectado", True), ("Momento", "Llega al servicio", True),
          ("Uso", "Inicia la investigación", True)],
       "pie": "Puede no ser el primero en enfermar"},
      {"titulo": "Caso primario", "datos": [
          ("Qué es", "Introduce la enfermedad", False), ("Momento", "Primero en enfermar", False),
          ("Uso", "Se identifica después", False)],
       "pie": "Origen del brote"},
      {"titulo": "Caso sospechoso", "datos": [
          ("Qué es", "Clínica compatible", False), ("Momento", "Sin pruebas", False),
          ("Uso", "Activa la vigilancia", False)],
       "pie": "Definición sensible"},
      {"titulo": "Caso probable", "datos": [
          ("Qué es", "Sospechoso + nexo", False), ("Momento", "Sin confirmación", False),
          ("Uso", "Nexo o prueba parcial", False)],
       "pie": "Pendiente de confirmar"}]},
  ["Caso secundario: se contagia del caso primario.",
   "Caso confirmado: con prueba de laboratorio o nexo según la norma.",
   "Las definiciones de caso las fija el CDC-MINSA."],
  "OPS – Módulos de principios de epidemiología para el control de enfermedades (MOPECE) · CDC-MINSA – Directivas de vigilancia")

# OFT-032 · embudo
V("embudo", "OFT-032", "lactante-leucocoria-estrabismo-retinoblastoma", "Reflejo pupilar blanco",
  "OFTALMOLOGÍA ENAM: RETINOBLASTOMA", "OFTALMOLOGÍA",
  ("Retinoblastoma", ["Tumor intraocular maligno más frecuente en la infancia",
   "Leucocoria y estrabismo son los signos iniciales"]),
  ("Lactante de 18 meses", ["Estrabismo y dolor ocular", "Ojo rojo con reflejo pupilar blanco"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Lactante con leucocoria y estrabismo",
   "candidatos": ["Retinoblastoma", "Catarata congénita", "Uveítis", "Queratitis", "Conjuntivitis viral"],
   "pasos": [("Reflejo pupilar blanco: lesión interna", ["Conjuntivitis viral", "Queratitis"]),
             ("Leucocoria + estrabismo en < 2 años", ["Uveítis"]),
             ("Masa retiniana en fondo de ojo o ecografía", ["Catarata congénita"])],
   "final": ("RETINOBLASTOMA", ["Gen RB1", "Ecografía y RM; no biopsiar"]),
   "nota": "Toda leucocoria requiere referencia urgente a oftalmología."},
  ["El test del reflejo rojo en cada control del niño lo detecta a tiempo.",
   "Bilateral y hereditario en ~40%: riesgo de otros tumores (osteosarcoma).",
   "Calcificaciones intraoculares en la ecografía o TC."],
  "AAP – Red reflex examination in neonates, infants and children (2023) · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# GIN-126 · puntaje
V("puntaje", "GIN-126", "pa-160-110-plaquetas-90000-dhl-700-hellp", "Síndrome HELLP",
  "OBSTETRICIA ENAM: SÍNDROME HELLP", "OBSTETRICIA",
  ("Síndrome HELLP", ["Hemólisis + enzimas hepáticas elevadas + plaquetas bajas",
   "Forma grave de preeclampsia: dolor en hipocondrio derecho"]),
  ("Primigesta de 38 semanas", ["Dolor en hipocondrio derecho · PA 160/110", "Plaquetas 90 000 · TGO 160 · DHL 700"]),
  {"rotulo": "Criterios de Tennessee en el caso", "escala": "Tennessee", "total": 3, "max": 3,
   "total_label": "Criterios presentes",
   "interpreta": "HELLP completo",
   "items": [("Hemólisis: DHL ≥ 600", "1", True), ("TGO ≥ 70 UI/L", "1", True),
             ("Plaquetas < 100 000", "1", True)],
   "bandas": [("0", "Sin HELLP", "Preeclampsia: vigilar", False),
              ("1-2", "HELLP parcial", "Vigilar y repetir exámenes", False),
              ("3", "HELLP completo", "MgSO₄, antihipertensivo y terminar la gestación", True)]},
  ["Complicaciones: hematoma hepático, CID, DPP, falla renal.",
   "Transfundir plaquetas si < 50 000 antes de una cesárea.",
   "PTT: hemólisis y plaquetas bajas sin elevación marcada de enzimas."],
  "ACOG – Practice Bulletin N.° 222: Gestational hypertension and preeclampsia (2020) · " + WILLIAMS)

# INF-063 · puntaje
V("puntaje", "INF-063", "vih-cd4-100-pao2-60-pneumocystis-prednisona", "PCP con hipoxemia: corticoides",
  "INFECTOLOGÍA ENAM: NEUMONÍA POR PNEUMOCYSTIS GRAVE", "INFECTOLOGÍA",
  ("Neumonía por Pneumocystis moderada a grave", ["PaO₂ < 70 mmHg o gradiente A-a ≥ 35",
   "Agregar prednisona al cotrimoxazol: reduce la mortalidad"]),
  ("Varón de 27 años con VIH sin TAR", ["CD4 100 · disnea, tos seca, SatO₂ 87%", "PaO₂ 60, PaCO₂ 22 · infiltrados intersticiales"]),
  {"rotulo": "Criterios para corticoides", "escala": "PCP", "total": 2, "max": 2,
   "total_label": "Criterios presentes",
   "interpreta": "Indicación de prednisona",
   "items": [("PaO₂ < 70 mmHg (60)", "1", True), ("Gradiente A-a ≥ 35 (~ 62)", "1", True)],
   "bandas": [("0", "Leve", "Solo cotrimoxazol", False),
              ("≥ 1", "Moderada-grave", "PREDNISONA 40 mg c/12 h + cotrimoxazol", True)]},
  ["Iniciar los corticoides dentro de las 72 h del tratamiento.",
   "Esquema: 40 mg c/12 h × 5 días, 40 mg/día × 5, 20 mg/día × 11.",
   "Ritonavir y antifúngicos no son coadyuvantes de la PCP."],
  "NIH/CDC/IDSA – Guidelines for opportunistic infections in adults with HIV: Pneumocystis (2024)")

# PED-130 · matriz
V("matriz", "PED-130", "lactante-vih-sintomatico-rotavirus-prescripcion", "Vacunas en el lactante con VIH",
  "PEDIATRÍA ENAM: VACUNAS EN VIH", "PEDIATRÍA",
  ("Vacunación en el niño con VIH", ["Las vacunas inactivadas se aplican según el esquema",
   "Las vivas atenuadas requieren evaluación y prescripción médica"]),
  ("Lactante de 4 meses con VIH sintomático", ["Esquema Nacional de Vacunación MINSA", "¿Cuál requiere prescripción médica?"]),
  {"rotulo": "Vacunas del lactante", "eje_x": "Aspecto", "eje_y": "Vacuna",
   "cols": ["Tipo", "VIH sintomático"], "rows": ["Rotavirus", "BCG", "Pentavalente", "IPV y neumococo"], "caso": (0, 1),
   "cells": [[("Viva atenuada", ["Oral"]), ("BAJO PRESCRIPCIÓN", ["Evaluar inmunidad"])],
             [("Viva atenuada", []), ("Contraindicada", ["Si hay síntomas"])],
             [("Inactivada", []), ("Aplicar", ["Según esquema"])],
             [("Inactivadas", []), ("Aplicar", [])]]},
  ["BCG contraindicada en el niño con VIH sintomático.",
   "SPR y varicela: solo si CD4 ≥ 15%.",
   "Las inactivadas son seguras aunque la respuesta sea menor."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 (Esquema Nacional de Vacunación) y modificatorias · CDC/ACIP – Altered immunocompetence (2024)")

# CIR-067 · árbol
A("CIR-067", "tumor-base-apendicular-2-cm-mesenterio-hemicolectomia", "Tumor en la base del apéndice",
  "CIRUGÍA ENAM: TUMOR NEUROENDOCRINO DEL APÉNDICE", "CIRUGÍA",
  ("Tumor neuroendocrino del apéndice", ["Hallazgo en apendicectomías, casi siempre en la punta",
   "≥ 2 cm, en la base o con ganglios: hemicolectomía derecha"]),
  ("Varón de 27 años operado por «apendicitis»", ["Masa de 2 cm en la base apendicular", "Compromete el mesenterio con lesiones similares"]),
  Q("¿Tamaño y localización?", [
      L("< 1 cm, en la punta", "Apendicectomía", ["Suficiente"]),
      L("1-2 cm", "Según riesgo", ["Mesoapéndice, invasión"]),
      L("≥ 2 cm, base o ganglios", "HEMICOLECTOMÍA DERECHA", ["Con linfadenectomía"], path=True)], path=True),
  ("Tumor neuroendocrino apendicular", [("Dato", True)], [
      ("Frecuencia", ["Tumor apendicular más común"]),
      ("Marcadores", ["Cromogranina A, 5-HIAA"]),
      ("Síndrome carcinoide", ["Si hay metástasis hepáticas"])]),
  ["La apendicectomía sola deja ganglios comprometidos.",
   "La ileostomía no trata el tumor.",
   "Seguimiento con TC y marcadores."],
  "ENETS – Guidance paper for neuroendocrine neoplasms of the appendix (2023) · NCCN – Neuroendocrine tumors (2024)")

# PSI-024 · fases
V("fases", "PSI-024", "haloperidol-no-puede-estar-quieto-acatisia-propranolol", "Efectos extrapiramidales",
  "PSIQUIATRÍA ENAM: ACATISIA", "PSIQUIATRÍA",
  ("Acatisia", ["Inquietud motora: no puede estar quieto, camina todo el tiempo",
   "Tratamiento de elección: propranolol"]),
  ("Varón de 24 años con esquizofrenia", ["Controlado con haloperidol", "No puede estar quieto, camina por toda la casa"]),
  {"rotulo": "Según el tiempo de aparición", "ans": 1,
   "fases": [("Distonía", "Horas-días", "Biperideno", ["Tortícolis, crisis oculógira"]),
             ("Acatisia", "Días-sem", "PROPRANOLOL", ["No puede estar quieto"]),
             ("Parkinsonismo", "Semanas", "Biperideno", ["Rigidez, temblor"]),
             ("Discinesia", "Meses-años", "Cambiar a atípico", ["Movimientos orofaciales"])],
   "curvas": [],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Propranolol", True), ("Bromocriptina", False), ("Benzodiacepina", False), ("Dantroleno", False)]},
  ["También sirve bajar la dosis del antipsicótico.",
   "Las benzodiacepinas son segunda línea.",
   "Bromocriptina y dantroleno son para el síndrome neuroléptico maligno."],
  "APA – Practice guideline for the treatment of schizophrenia (2020) · Stahl's Essential Psychopharmacology 5.ª ed. (2021)")

# CIR-068 · termómetro
V("termometro", "CIR-068", "sangrado-defecar-no-prolapsa-coagulacion-infrarroja", "Hemorroides internas: grados",
  "CIRUGÍA ENAM: HEMORROIDES INTERNAS", "CIRUGÍA",
  ("Hemorroides internas", ["Se clasifican por el prolapso (Goligher)",
   "Grado I-II que no responde al manejo médico: procedimientos en consultorio"]),
  ("Mujer de 40 años multípara", ["Sangrado al defecar por 2 meses, sin respuesta", "Anoscopía: no rebasan el orificio anal"]),
  {"rotulo": "Clasificación de Goligher",
   "niveles": [("Grado I", "No prolapsa", ["Solo sangra"]),
               ("Grado II", "Reduce sola", ["Prolapso al pujar"]),
               ("Grado III", "Reducción manual", ["Prolapso persistente"]),
               ("Grado IV", "Irreductible", ["Riesgo de trombosis"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Fibra, agua, baños de asiento", ["Primera medida"], False),
             (2, "COAGULACIÓN INFRARROJA", ["O ligadura con banda"], True),
             (3, "Hemorroidectomía", ["Grado III-IV"], False)]},
  ["La ligadura con banda es la opción más eficaz en consultorio.",
   "Sangrado rectal en > 40 años: descartar cáncer colorrectal.",
   "La resección anterior baja es cirugía del cáncer de recto."],
  "ASCRS – Clinical practice guidelines for the management of hemorrhoids (2018)")

# END-036 · matriz
V("matriz", "END-036", "choque-septico-refractario-cortisol-bajo-acth-alta", "Choque refractario: insuficiencia suprarrenal",
  "ENDOCRINOLOGÍA ENAM: INSUFICIENCIA SUPRARRENAL PRIMARIA", "ENDOCRINOLOGÍA",
  ("Insuficiencia suprarrenal en el choque séptico", ["Hipotensión que no responde a fluidos ni vasopresores",
   "Cortisol bajo con ACTH alta: falla primaria de la glándula"]),
  ("Mujer de 64 años con sepsis urinaria", ["Hipotensa pese a fluidos y vasopresores", "Na 130 · cortisol bajo · ACTH elevada"]),
  {"rotulo": "Primaria vs secundaria", "eje_x": "Hormona", "eje_y": "Tipo",
   "cols": ["Cortisol", "ACTH", "Aldosterona"], "rows": ["Primaria", "Secundaria"], "caso": (0, 1),
   "cells": [[("Bajo", []), ("ALTA", ["Hiperpigmentación"]), ("Baja", ["Hiperpotasemia"])],
             [("Bajo", []), ("Baja", []), ("Normal", ["K normal"])]]},
  ["Tratamiento: hidrocortisona 200 mg/día EV.",
   "La acidosis láctica es consecuencia del choque, no su causa.",
   "Sin cetonas no hay cetoacidosis."],
  "SSC – Surviving Sepsis Campaign guidelines (2021) · Endocrine Society – Primary adrenal insufficiency (2016)")

# CIR-069 · fases
V("fases", "CIR-069", "dolor-intenso-defecar-desgarro-posterior-fisura-anal", "Fisura anal: tratamiento escalonado",
  "CIRUGÍA ENAM: FISURA ANAL AGUDA", "CIRUGÍA",
  ("Fisura anal", ["Desgarro en la línea media posterior con espasmo del esfínter",
   "Aguda: manejo conservador con fibra, ablandadores y baños de asiento"]),
  ("Mujer de 30 años", ["Dolor muy intenso al defecar y hematoquecia", "Esfínter hipertónico · desgarro posterior"]),
  {"rotulo": "Escalones del tratamiento", "ans": 0,
   "fases": [("Inicial", "0-6 sem", "FIBRA + BAÑOS", ["Ablandadores de heces"]),
             ("Persiste", "6-8 sem", "Nitrato o diltiazem", ["Tópico"]),
             ("Refractaria", "> 8 sem", "Toxina botulínica", ["En el esfínter"]),
             ("Crónica", "Meses", "Esfinterotomía", ["Lateral interna"])],
   "curvas": [],
   "chips_titulo": "Tratamiento inicial · marcado el correcto",
   "chips": [("Ablandadores y baños", True), ("Toxina botulínica", False), ("Esfinterotomía", False), ("Lidocaína + toxina", False)]},
  ["La mayoría de fisuras agudas cicatriza con manejo conservador.",
   "Fisura lateral o múltiple: pensar en Crohn, TB, VIH o cáncer.",
   "Crónica: papila hipertrófica y hemorroide centinela."],
  "ASCRS – Clinical practice guidelines for the management of anal fissures (2017)")

# NRL-036 · termómetro
V("termometro", "NRL-036", "tec-grave-coma-rigidez-decorticacion-hemisferios", "Posturas en el coma",
  "NEUROLOGÍA ENAM: RIGIDEZ DE DECORTICACIÓN", "NEUROLOGÍA",
  ("Rigidez de decorticación", ["Flexión de brazos con extensión de piernas",
   "Lesión por encima del núcleo rojo: hemisferios o cápsula interna"]),
  ("Varón de 20 años con TEC grave", ["Caída de un tercer piso · intubado", "Coma profundo con rigidez de decorticación"]),
  {"rotulo": "Postura y nivel de lesión",
   "niveles": [("Hemisferios", "Decorticación", ["Flexión de brazos"]),
               ("Mesencéfalo", "Descerebración", ["Extensión de las 4 extremidades"]),
               ("Bulbo", "Flacidez", ["Sin respuesta motora"])],
   "caso_nivel": 0, "ruta_titulo": "Glasgow motor", "paso_label": "PASO",
   "pasos": [(1, "MOTOR 3: FLEXIÓN ANORMAL", ["Decorticación"], True),
             (2, "Motor 2: extensión", ["Descerebración"], False),
             (3, "Motor 1: ninguna", ["Peor pronóstico"], False)]},
  ["La descerebración indica lesión más baja y peor pronóstico.",
   "Glasgow ≤ 8: intubar para proteger la vía aérea.",
   "TC cerebral urgente y neurocirugía."],
  "Brain Trauma Foundation – Guidelines for severe TBI 4.ª ed. (2016) · Plum and Posner's Diagnosis of Stupor and Coma 5.ª ed. (2019)")

# PED-131 · árbol
A("PED-131", "preescolar-itu-ecoli-blee-meropenem", "ITU por E. coli BLEE",
  "PEDIATRÍA ENAM: ITU POR BACTERIA BLEE", "PEDIATRÍA",
  ("E. coli productora de BLEE", ["Resiste penicilinas y cefalosporinas",
   "Tratamiento de elección: carbapenémico"]),
  ("Preescolar de 4 años", ["Fiebre, disuria y polaquiuria de 4 días", "Urocultivo: E. coli BLEE (+)"]),
  Q("¿Germen productor de BLEE?", [
      L("No", "Cefalosporina", ["Ceftriaxona o cefuroxima"]),
      L("Sí", "MEROPENEM", ["O ertapenem", "Ajustar al antibiograma"], path=True)], path=True),
  ("Antibiótico en ITU pediátrica", [("Germen habitual", False), ("BLEE", True)], [
      ("Elección", ["Ceftriaxona o cefalosporina oral", "Meropenem o ertapenem"]),
      ("No sirven", ["—", "Cefalosporinas, cotrimoxazol"])]),
  ["Si es sensible, la nitrofurantoína sirve en cistitis (no en ITU febril).",
   "Ciprofloxacino: evitar en niños salvo que no haya alternativa.",
   "Ecografía renal tras la primera ITU febril."],
  "AAP – UTI clinical practice guideline (2011, reafirmado 2016) · IDSA – Guidance on antimicrobial-resistant gram-negative infections (2024)")

# INF-064 · embudo
V("embudo", "INF-064", "selva-fiebre-cuartana-esplenomegalia-malaria", "Fiebre paroxística de la selva",
  "INFECTOLOGÍA ENAM: MALARIA", "INFECTOLOGÍA",
  ("Malaria", ["Fiebre con escalofríos y sudoración en ciclos",
   "Anemia y esplenomegalia; confirmar con gota gruesa"]),
  ("Adolescente de 12 años de la selva", ["Fiebre paroxística cuartana, escalofríos, sudoración", "Palidez, hepatoesplenomegalia · Hb 8"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Fiebre paroxística con anemia",
   "candidatos": ["Malaria", "Fiebre tifoidea", "Dengue", "Brucelosis", "Hepatitis viral"],
   "pasos": [("Fiebre en ciclos con escalofríos", ["Fiebre tifoidea", "Dengue"]),
             ("Procede de la selva, sin contacto con ganado", ["Brucelosis"]),
             ("Anemia y esplenomegalia sin ictericia", ["Hepatitis viral"])],
   "final": ("MALARIA", ["Cuartana: P. malariae", "Gota gruesa"]),
   "nota": "Terciana: P. vivax y P. ovale; P. falciparum: fiebre irregular y grave."},
  ["P. vivax: primaquina para eliminar hipnozoítos.",
   "P. falciparum: artesunato; riesgo de malaria cerebral.",
   "Anemia por hemólisis y secuestro esplénico."],
  "MINSA – NTS de atención de la malaria · OMS – WHO guidelines for malaria (2024)")

# CAR-050 · puntaje
V("puntaje", "CAR-050", "dolor-pleuritico-alivia-inclinado-frote-pericarditis", "Pericarditis aguda: criterios",
  "CARDIOLOGÍA ENAM: PERICARDITIS AGUDA", "CARDIOLOGÍA",
  ("Pericarditis aguda", ["Dolor que aumenta al inspirar y mejora al inclinarse hacia adelante",
   "Frote pericárdico y ST elevado difuso con PR descendido"]),
  ("Varón de 26 años fumador", ["Dolor retroesternal irradiado al trapecio", "Mejora en posición genupectoral · frote · ST elevado"]),
  {"rotulo": "Criterios ESC en el caso", "escala": "ESC 2015", "total": 3, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Pericarditis aguda (≥ 2)",
   "items": [("Dolor pericárdico típico", "1", True), ("Frote pericárdico", "1", True),
             ("ST elevado difuso o PR descendido", "1", True), ("Derrame pericárdico", "1", False)],
   "bandas": [("0-1", "No cumple", "Buscar otra causa", False),
              ("≥ 2", "Pericarditis", "AINE + colchicina", True)]},
  ["Irradiación al trapecio: típica de pericarditis.",
   "Colchicina 3 meses reduce las recurrencias.",
   "Troponina alta: miopericarditis."],
  "ESC – Guidelines for the diagnosis and management of pericardial diseases (2015)")

# HEM-023 · termómetro
V("termometro", "HEM-023", "leucocitos-400-fiebre-aislamiento-inverso", "Neutropenia grave",
  "HEMATOLOGÍA ENAM: NEUTROPENIA GRAVE", "HEMATOLOGÍA",
  ("Neutropenia grave", ["Neutrófilos < 500: alto riesgo de infección",
   "Aislamiento inverso (protector): proteger al paciente del entorno"]),
  ("Mujer de 23 años hospitalizada", ["Fiebre 39 °C, FC 110", "Leucocitos 400 · Hb 5 · plaquetas 3000"]),
  {"rotulo": "Neutrófilos absolutos (/mm³)",
   "niveles": [("1000-1500", "Leve", ["Riesgo bajo"]),
               ("500-999", "Moderada", ["Riesgo intermedio"]),
               ("< 500", "Grave", ["Riesgo alto de sepsis"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "AISLAMIENTO INVERSO", ["Habitación individual, lavado de manos"], True),
             (2, "Antibiótico en < 1 h", ["Cefepime o piperacilina-tazobactam"], False),
             (3, "Transfundir", ["Plaquetas y glóbulos rojos"], False)]},
  ["Neutropenia febril: emergencia oncohematológica.",
   "Evitar flores, frutas crudas y visitas enfermas.",
   "Pancitopenia: estudiar médula ósea."],
  "IDSA – Clinical practice guideline for febrile neutropenia (2010, act. 2018) · CDC – Guideline for isolation precautions (2007, act. 2023)")

# NEF-053 · árbol
A("NEF-053", "prostata-indurada-psa-8-biopsia-transrectal", "Sospecha de cáncer de próstata",
  "NEFROLOGÍA ENAM: CÁNCER DE PRÓSTATA", "NEFROLOGÍA",
  ("Cáncer de próstata", ["Tacto rectal duro e irregular o PSA elevado",
   "Diagnóstico con biopsia transrectal ecodirigida"]),
  ("Varón de 70 años fumador", ["Síntomas urinarios y dolor de caderas", "Próstata indurada e irregular · PSA 8"]),
  Q("¿Tacto sospechoso o PSA elevado?", [
      L("No", "Control según la edad", ["PSA y tacto"]),
      L("Sí: próstata dura, PSA 8", "BIOPSIA TRANSRECTAL", ["Ecodirigida, 10-12 cilindros", "Gleason / ISUP"], path=True)], path=True),
  ("Si se confirma: estadificar", [("Busca", True)], [
      ("Gammagrafía ósea", ["Metástasis (dolor de cadera)"]),
      ("RM pélvica", ["Extensión local"]),
      ("TC", ["Ganglios y vísceras"])]),
  ["La RM multiparamétrica antes de la biopsia mejora la detección.",
   "El PSA sube también en HBP y prostatitis.",
   "Metástasis óseas osteoblásticas: dolor en cadera y columna."],
  "EAU/EANM/ESTRO/ESUR/ISUP/SIOG – Guidelines on prostate cancer (2024)")

# CB-045 · radial
V("radial", "CB-045", "hipertiroidismo-metabolismo-basal-aumentado", "Efectos de la hormona tiroidea",
  "CIENCIAS BÁSICAS ENAM: FISIOLOGÍA TIROIDEA", "CIENCIAS BÁSICAS",
  ("Hormona tiroidea", ["Aumenta el consumo de O₂ y la producción de calor",
   "Hipertiroidismo: metabolismo basal alto"]),
  ("Mujer de 35 años con hipertiroidismo", ["Intolerancia al calor", "Taquicardia, pérdida de peso"]),
  {"rotulo": "Mapa del tema", "centro": "T3 / T4", "centro_sub": "Hipertiroidismo", "ans": 0,
   "items": [("METABOLISMO BASAL ↑", ["Más consumo de O₂", "Calor, pérdida de peso"]),
             ("Corazón", ["↑ FC y gasto cardiaco"]),
             ("Intestino", ["↑ motilidad, diarrea"]),
             ("Lípidos", ["↓ colesterol"]),
             ("Nervioso", ["Temblor, ansiedad"])],
   "ruta": ["Exceso de T3 y T4", "↑ Bomba Na⁺/K⁺ y mitocondrias", "Más calor y consumo", "METABOLISMO BASAL ↑"]},
  ["En el hipotiroidismo: colesterol alto, estreñimiento, bradicardia.",
   "Aumenta los receptores β-adrenérgicos: por eso sirve el propranolol.",
   "Gasto cardiaco alto, no bajo."],
  GUYTON)

# NRL-037 · tarjetas
V("tarjetas", "NRL-037", "dolor-roce-ropa-electrico-neuropatico", "Tipos de dolor",
  "NEUROLOGÍA ENAM: DOLOR NEUROPÁTICO", "NEUROLOGÍA",
  ("Dolor neuropático", ["Por lesión o enfermedad del sistema somatosensorial",
   "Quemante, eléctrico, alodinia (dolor al roce) y adormecimiento"]),
  ("Mujer de 62 años", ["Dolor al roce de la ropa, sensación eléctrica", "Adormecimiento · «le arrancan» el dedo"]),
  {"rotulo": "¿Qué tipo de dolor es?", "ans": 0, "cards": [
      {"titulo": "NEUROPÁTICO", "datos": [
          ("Origen", "Lesión del nervio", True), ("Descripción", "Eléctrico, alodinia", True),
          ("Ejemplo", "Neuropatía diabética", True)],
       "pie": "Pregabalina, amitriptilina"},
      {"titulo": "Somático", "datos": [
          ("Origen", "Piel, músculo, hueso", False), ("Descripción", "Localizado, punzante", False),
          ("Ejemplo", "Fractura", False)],
       "pie": "Nociceptivo"},
      {"titulo": "Visceral", "datos": [
          ("Origen", "Órganos internos", False), ("Descripción", "Difuso, referido", False),
          ("Ejemplo", "Cólico biliar", False)],
       "pie": "Nociceptivo"},
      {"titulo": "Nociplástico", "datos": [
          ("Origen", "Sensibilización central", False), ("Descripción", "Difuso, sin lesión", False),
          ("Ejemplo", "Fibromialgia", False)],
       "pie": "Tercer mecanismo"}]},
  ["Alodinia: dolor ante un estímulo que normalmente no duele.",
   "Hiperalgesia: más dolor ante un estímulo doloroso.",
   "Los AINE y opioides funcionan poco en el dolor neuropático."],
  "IASP – Terminology (2020) · NICE – Neuropathic pain in adults: pharmacological management (2020)")

# GIN-127 · matriz
V("matriz", "GIN-127", "obesa-imc-32-gano-125-kg-excesiva", "Ganancia de peso según IMC",
  "OBSTETRICIA ENAM: GANANCIA DE PESO EXCESIVA", "OBSTETRICIA",
  ("Ganancia de peso en la gestante obesa", ["IMC ≥ 30: ganar solo 5 a 9 kg",
   "12.5 kg supera la meta: ganancia excesiva"]),
  ("Segundigesta de 40 semanas", ["IMC pregestacional 32", "Ganó 12.5 kg en el embarazo"]),
  {"rotulo": "Metas del IOM", "eje_x": "Meta", "eje_y": "IMC",
   "cols": ["Total (kg)", "Semanal (2.º-3.er trim.)"], "rows": ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"], "caso": (3, 0),
   "cells": [[("12.5-18", []), ("~ 0.5 kg", [])],
             [("11.5-16", []), ("~ 0.4 kg", [])],
             [("7-11.5", []), ("~ 0.3 kg", [])],
             [("5-9: EXCESIVA", ["Ganó 12.5 kg"]), ("~ 0.2 kg", [])]]},
  ["Exceso de peso: macrosomía, diabetes, preeclampsia y cesárea.",
   "Retener peso posparto aumenta la obesidad futura.",
   "Consejería nutricional desde el primer control."],
  "IOM – Weight gain during pregnancy (2009) · ACOG – Committee Opinion N.° 548 (2013, reafirmado 2023)")

# GAS-047 · fases
V("fases", "GAS-047", "hematoma-retroperitoneal-bilirrubina-indirecta-reabsorcion", "Ictericia tras un hematoma",
  "GASTROENTEROLOGÍA ENAM: ICTERICIA POR REABSORCIÓN DE HEMATOMA", "GASTROENTEROLOGÍA",
  ("Ictericia por reabsorción de hematoma", ["La hemoglobina del hematoma se degrada a bilirrubina",
   "Aumenta la bilirrubina indirecta con enzimas casi normales"]),
  ("Varón de 36 años operado hace 10 días", ["7 unidades de paquete globular", "BI 3.7, BD 0.2 · hematoma retroperitoneal"]),
  {"rotulo": "Evolución", "ans": 1,
   "fases": [("Hematoma", "Días 1-3", "Sangre acumulada", ["Tras el trauma"]),
             ("Degradación", "Días 5-10", "↑ BILIRRUBINA INDIRECTA", ["Hem → biliverdina → bilirrubina"]),
             ("Resolución", "Semanas", "Se normaliza", ["Al reabsorberse"])],
   "curvas": [("BI", AMBER, [0.1, 0.2, 0.5, 0.8, 0.9, 0.6, 0.3]),
              ("Hb", ROSE, [0.9, 0.6, 0.55, 0.55, 0.6, 0.65, 0.7])],
   "chips_titulo": "Causa · marcada la correcta",
   "chips": [("Reabsorción del hematoma", True), ("Menor conjugación", False), ("Defecto de excreción", False), ("Menor captación", False)]},
  ["Las transfusiones masivas también aportan bilirrubina.",
   "Si sube la directa: pensar en colestasis o lesión biliar.",
   "No requiere tratamiento específico."],
  HARRISON)

# GIN-128 · fases
V("fases", "GIN-128", "primer-control-vacuna-tdap-27-36-semanas", "Vacunas en la gestación",
  "OBSTETRICIA ENAM: VACUNA TDAP", "OBSTETRICIA",
  ("Vacuna Tdap en el embarazo", ["Entre las 27 y 36 semanas en cada embarazo",
   "Pasa anticuerpos contra tos ferina al recién nacido"]),
  ("Primigesta de 8 semanas", ["Primer control prenatal", "Pregunta por la vacuna Tdap"]),
  {"rotulo": "Calendario de la gestante", "ans": 2,
   "fases": [("1.er trim.", "0-13 sem", "Influenza", ["Si es temporada"]),
             ("2.º trim.", "14-26 sem", "dT", ["Si no está protegida"]),
             ("3.er trim.", "27-36 sem", "TDAP", ["Anticuerpos al RN"]),
             ("Término", "37-40 sem", "Muy tarde", ["Poco paso de anticuerpos"])],
   "curvas": [("Ac", SKY, [0.0, 0.05, 0.1, 0.4, 0.8, 0.95, 0.95])],
   "chips_titulo": "Semanas · marcado el correcto",
   "chips": [("27-36", True), ("19-26", False), ("8-18", False), ("37-40", False)]},
  ["La tos ferina es grave en menores de 3 meses.",
   "Se repite en cada embarazo.",
   "Vacunas vivas (SPR, varicela, fiebre amarilla) están contraindicadas."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 (Esquema Nacional de Vacunación) · CDC/ACIP – Tdap in pregnancy (2024)")

# PED-132 · radial
V("radial", "PED-132", "displasia-broncopulmonar-hipertension-pulmonar", "Displasia broncopulmonar",
  "PEDIATRÍA ENAM: DISPLASIA BRONCOPULMONAR", "PEDIATRÍA",
  ("Displasia broncopulmonar", ["Necesidad de O₂ a las 36 semanas corregidas en el prematuro",
   "Complicación más frecuente y grave: hipertensión pulmonar"]),
  ("Pregunta de concepto", ["Complicación más frecuente", "de la displasia broncopulmonar"]),
  {"rotulo": "Mapa del tema", "centro": "DBP", "centro_sub": "Complicaciones", "ans": 0,
   "items": [("HTA PULMONAR", ["La más frecuente y grave", "Tamizar con ecocardiograma"]),
             ("Infecciones", ["VSR: palivizumab"]),
             ("Sibilancias", ["Recurrentes"]),
             ("Crecimiento", ["Retraso pondoestatural"]),
             ("Neurodesarrollo", ["Más riesgo de secuelas"])],
   "ruta": ["Prematuro ventilado", "Daño alveolar y vascular", "Resistencia pulmonar alta", "HTA PULMONAR"]},
  ["Factores: prematuridad, oxígeno, ventilación mecánica, infección.",
   "Prevención: CPAP temprano, cafeína, corticoides prenatales.",
   "La hipertensión pulmonar puede llevar a cor pulmonale."],
  "AHA/ATS – Pediatric pulmonary hypertension guidelines (2015) · " + NELSON)

# NEF-054 · embudo
V("embudo", "NEF-054", "hermano-erc-masa-flanco-creatinina-poliquistosis", "Masa en flanco con historia familiar",
  "NEFROLOGÍA ENAM: POLIQUISTOSIS RENAL", "NEFROLOGÍA",
  ("Poliquistosis renal autosómica dominante", ["Quistes renales bilaterales que agrandan los riñones",
   "Dolor en flanco, HTA, hematuria y ERC progresiva; historia familiar"]),
  ("Varón de 38 años con dolor en flanco", ["Hermano con ERC · masa en flanco derecho", "Creatinina 2.85 · orina normal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Masa en flanco con ERC familiar",
   "candidatos": ["Poliquistosis renal", "Glomerulonefritis", "Amiloidosis", "Absceso renal", "Hidronefrosis"],
   "pasos": [("Hermano con ERC: enfermedad hereditaria", ["Absceso renal"]),
             ("Orina normal: no es glomerular", ["Glomerulonefritis", "Amiloidosis"]),
             ("Riñones grandes con quistes en la ecografía", ["Hidronefrosis"])],
   "final": ("POLIQUISTOSIS RENAL", ["Autosómica dominante (PKD1, PKD2)", "Ecografía: quistes bilaterales"]),
   "nota": "Buscar aneurismas cerebrales si hay antecedente familiar de hemorragia."},
  ["Asociada a quistes hepáticos y prolapso mitral.",
   "Tolvaptán enlentece el crecimiento de los quistes.",
   "Controlar la PA con IECA o ARA II."],
  "KDIGO – Clinical practice guideline for ADPKD (2025)")

# CB-046 · fases
V("fases", "CB-046", "agenesia-renal-unilateral-metanefros", "Desarrollo del riñón",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA RENAL", "CIENCIAS BÁSICAS",
  ("Metanefros", ["Origen del riñón definitivo (desde la semana 5)",
   "Yema ureteral + blastema metanéfrico: si falla, agenesia renal"]),
  ("Primigesta de 35 años", ["Ecografía del segundo trimestre", "Feto con agenesia renal unilateral"]),
  {"rotulo": "Tres riñones embrionarios", "ans": 2,
   "fases": [("Pronefros", "Semana 4", "Involuciona", ["No funciona"]),
             ("Mesonefros", "Semanas 4-8", "Conducto de Wolff", ["Riñón transitorio"]),
             ("Metanefros", "Desde sem 5", "RIÑÓN DEFINITIVO", ["Yema ureteral + blastema"])],
   "curvas": [],
   "chips_titulo": "Estructura · marcada la correcta",
   "chips": [("Metanefros", True), ("Pronefros", False), ("Mesonefros", False), ("Mesodermo", False)]},
  ["La yema ureteral forma uréter, pelvis, cálices y túbulos colectores.",
   "El blastema forma las nefronas.",
   "Agenesia bilateral: oligohidramnios y secuencia de Potter."],
  "Langman – Embriología médica 14.ª ed. (2019) · Moore – The Developing Human 11.ª ed. (2020)")

# HEM-024 · tarjetas
V("tarjetas", "HEM-024", "hb-186-eritropoyetina-baja-plaquetas-policitemia-vera", "Eritrocitosis: ¿primaria o secundaria?",
  "HEMATOLOGÍA ENAM: POLICITEMIA VERA", "HEMATOLOGÍA",
  ("Policitemia vera", ["Neoplasia mieloproliferativa con mutación JAK2",
   "Masa eritrocitaria alta con eritropoyetina baja; a menudo trombocitosis"]),
  ("Varón de 45 años fumador", ["Hb 18.6, Hto 58% · plaquetas 510 000", "Eritropoyetina baja · carboxihemoglobina normal"]),
  {"rotulo": "¿Qué eritrocitosis es?", "ans": 0, "cards": [
      {"titulo": "POLICITEMIA VERA", "datos": [
          ("EPO", "Baja", True), ("Clave", "JAK2 V617F", True),
          ("Plaquetas", "Altas", True)],
       "pie": "Flebotomías + aspirina"},
      {"titulo": "Poliglobulia del fumador", "datos": [
          ("EPO", "Normal o alta", False), ("Clave", "COHb alta", False),
          ("Plaquetas", "Normales", False)],
       "pie": "Dejar de fumar"},
      {"titulo": "Hipernefroma", "datos": [
          ("EPO", "Alta", False), ("Clave", "Masa renal", False),
          ("Plaquetas", "Normales", False)],
       "pie": "EPO ectópica"},
      {"titulo": "Hipoxemia crónica", "datos": [
          ("EPO", "Alta", False), ("Clave", "SatO₂ < 92%", False),
          ("Plaquetas", "Normales", False)],
       "pie": "EPOC, altura"}]},
  ["Meta de hematocrito < 45% con flebotomías.",
   "Prurito acuagénico y eritromelalgia son típicos.",
   "Riesgo de trombosis y de evolución a mielofibrosis."],
  "WHO – Classification of myeloid neoplasms (2022) · ELN – Recommendations for polycythemia vera (2021)")

# END-037 · embudo
V("embudo", "END-037", "dm1-lactato-10-cetonas-negativas-acidosis-lactica", "Diabético con acidosis grave",
  "ENDOCRINOLOGÍA ENAM: ACIDOSIS LÁCTICA", "ENDOCRINOLOGÍA",
  ("Acidosis láctica", ["Acidosis metabólica con anión gap alto y lactato > 4",
   "Por hipoperfusión (choque), sepsis o fármacos"]),
  ("Varón de 22 años con DM1 irregular", ["Choque: PA 80/40, piel fría · Kussmaul", "Glucosa 480, cetonas (−), pH 7.15, lactato 10"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Diabético con acidosis metabólica",
   "candidatos": ["Acidosis láctica", "Cetoacidosis", "Salicilatos", "Metanol", "Estado hiperosmolar"],
   "pasos": [("Cetonas en sangre negativas", ["Cetoacidosis"]),
             ("pH 7.15 con anión gap alto", ["Estado hiperosmolar"]),
             ("Lactato 10 con choque, sin ingesta tóxica", ["Salicilatos", "Metanol"])],
   "final": ("ACIDOSIS LÁCTICA", ["Tipo A: hipoperfusión", "Tratar el choque y la causa"]),
   "nota": "Anión gap = Na − (Cl + HCO₃⁻); normal 8-12."},
  ["Cetoacidosis: cetonas positivas; es lo típico en la DM1.",
   "Salicilatos: alcalosis respiratoria + acidosis metabólica.",
   "Metanol: brecha osmolar alta y alteración visual."],
  HARRISON + " · ADA – Hyperglycemic crises in adults with diabetes: consensus report (2024)")

# NRL-038 · radial
V("radial", "NRL-038", "duchenne-distrofina-ausente", "Distrofia muscular de Duchenne",
  "NEUROLOGÍA ENAM: DISTROFIA DE DUCHENNE", "NEUROLOGÍA",
  ("Distrofia muscular de Duchenne", ["Falta de distrofina por mutación del gen DMD (ligada al X)",
   "Varones de 3-5 años con debilidad proximal y signo de Gowers"]),
  ("Pregunta de concepto", ["Proteína muscular deficiente", "en la distrofia de Duchenne"]),
  {"rotulo": "Mapa del tema", "centro": "DUCHENNE", "centro_sub": "Distrofia muscular", "ans": 0,
   "items": [("DISTROFINA", ["Ausente", "Gen DMD, ligado al X"]),
             ("Signo de Gowers", ["Se levanta trepando"]),
             ("Pantorrillas", ["Seudohipertrofia"]),
             ("CPK", ["Muy elevada"]),
             ("Corazón", ["Miocardiopatía"])],
   "ruta": ["Varón de 3-5 años", "Debilidad proximal", "Genética o biopsia", "SIN DISTROFINA"]},
  ["Becker: distrofina reducida o anormal; más leve y tardía.",
   "Corticoides retrasan la pérdida de la marcha.",
   "Causa de muerte: falla respiratoria o cardiaca."],
  "DMD Care Considerations Working Group – Lancet Neurol (2018) · " + NELSON)

# END-038 · puntaje
V("puntaje", "END-038", "metformina-insuficiencia-renal-acidosis-lactica", "Metformina: riesgo de acidosis láctica",
  "ENDOCRINOLOGÍA ENAM: ACIDOSIS LÁCTICA POR METFORMINA", "ENDOCRINOLOGÍA",
  ("Acidosis láctica por metformina", ["Rara pero grave; se acumula si falla el riñón",
   "Debilidad, náuseas, vómitos y taquipnea"]),
  ("Mujer de 72 años con DM2 e insuficiencia renal", ["Toma metformina; le cambiaron la dosis", "Debilidad, náuseas, vómitos, disnea"]),
  {"rotulo": "Factores de riesgo en el caso", "escala": "Riesgo con metformina", "total": 3, "max": 5,
   "total_label": "Factores presentes",
   "interpreta": "Alto riesgo de acidosis láctica",
   "items": [("Insuficiencia renal", "1", True), ("Edad > 65 años", "1", True),
             ("Aumento reciente de dosis", "1", True), ("Hipoxia, sepsis o IC", "1", False),
             ("Contraste yodado reciente", "1", False)],
   "bandas": [("0", "Riesgo bajo", "Continuar metformina", False),
              ("≥ 1", "Riesgo alto", "Suspender metformina; lactato y gases", True)]},
  ["TFG < 30: metformina contraindicada; 30-45: reducir dosis.",
   "La metformina no causa hipoglucemia sola.",
   "Tratamiento grave: hemodiálisis."],
  "ADA – Standards of Care in Diabetes (2025) · FDA – Metformin in renal impairment (2016)")

# NEF-055 · fases
V("fases", "NEF-055", "vasectomia-esterilidad-tres-meses", "Vasectomía: cuándo es segura",
  "NEFROLOGÍA ENAM: VASECTOMÍA", "NEFROLOGÍA",
  ("Vasectomía", ["Quedan espermatozoides en la vía seminal después de la cirugía",
   "Se considera estéril a los 3 meses con espermatograma sin espermatozoides"]),
  ("Varón recién vasectomizado", ["Pregunta cuándo", "quedará estéril"]),
  {"rotulo": "Después de la cirugía", "ans": 2,
   "fases": [("Cirugía", "Día 0", "Aún fértil", ["Esperma en el conducto"]),
             ("Transición", "1-3 meses", "Otro método", ["~ 20 eyaculaciones"]),
             ("Control", "3 meses", "ESPERMATOGRAMA", ["Azoospermia = estéril"])],
   "curvas": [("Esperma", SKY, [1.0, 0.8, 0.5, 0.3, 0.15, 0.05, 0.0])],
   "chips_titulo": "Tiempo · marcado el correcto",
   "chips": [("3 meses", True), ("Inmediatamente", False), ("1 mes", False), ("2 meses", False)]},
  ["Usar otro método anticonceptivo hasta confirmar la azoospermia.",
   "No afecta la erección ni la eyaculación.",
   "Es un método permanente (reversión difícil)."],
  "AUA – Vasectomy guideline (2012, act. 2015) · MINSA – NTS de planificación familiar")

# SP-092 · tarjetas
V("tarjetas", "SP-092", "colegio-educacion-autocuidado-tuberculosis-promocion", "Tipos de intervención sanitaria",
  "SALUD PÚBLICA ENAM: PROMOCIÓN DE LA SALUD", "SALUD PÚBLICA",
  ("Promoción de la salud", ["Educa y empodera a la población para cuidar su salud",
   "Se hace en escenarios como la escuela"]),
  ("Coordinación con un centro educativo", ["Charlas sobre autocuidado", "Síntomas y transmisión de la TB"]),
  {"rotulo": "¿Qué intervención es?", "ans": 0, "cards": [
      {"titulo": "PROMOCIÓN", "datos": [
          ("Dirigida a", "Población y entornos", True), ("Qué hace", "Educa, autocuidado", True),
          ("Ejemplo", "Charlas en el colegio", True)],
       "pie": "Antes de la enfermedad"},
      {"titulo": "Prevención", "datos": [
          ("Dirigida a", "Grupos en riesgo", False), ("Qué hace", "Evita o detecta", False),
          ("Ejemplo", "BCG, tamizaje", False)],
       "pie": "Primaria, secundaria"},
      {"titulo": "Recuperación", "datos": [
          ("Dirigida a", "Enfermos", False), ("Qué hace", "Diagnostica y trata", False),
          ("Ejemplo", "Tratamiento de TB", False)],
       "pie": "Atención clínica"},
      {"titulo": "Rehabilitación", "datos": [
          ("Dirigida a", "Con secuelas", False), ("Qué hace", "Recupera funciones", False),
          ("Ejemplo", "Terapia respiratoria", False)],
       "pie": "Después del daño"}]},
  ["Promoción: actúa sobre determinantes y estilos de vida.",
   "Instituciones Educativas Saludables: alianza Salud-Educación.",
   "Carta de Ottawa (1986): base de la promoción de la salud."],
  "OMS – Carta de Ottawa para la promoción de la salud (1986) · MINSA – Lineamientos de promoción de la salud (2017)")

# GIN-129 · matriz
V("matriz", "GIN-129", "gemelar-34-ectopico-mola-41-semanas-formula-obstetrica", "Fórmula obstétrica",
  "OBSTETRICIA ENAM: FÓRMULA OBSTÉTRICA", "OBSTETRICIA",
  ("Fórmula obstétrica G_P TPAV", ["T: a término · P: pretérmino · A: abortos · V: hijos vivos",
   "Este caso: G4 P1223"]),
  ("Mujer de 28 años con 4 embarazos", ["Gemelar a las 34 sem · ectópico · mola · 41 sem", "Todos sus hijos viven (3)"]),
  {"rotulo": "Cómo se cuenta cada embarazo", "eje_x": "Aspecto", "eje_y": "Embarazo",
   "cols": ["Cuenta como", "Suma"], "rows": ["Gemelar 34 sem", "Ectópico", "Mola", "41 semanas"], "caso": (0, 1),
   "cells": [[("Pretérmino", ["Dos productos"]), ("P = 2", ["Cada gemelo cuenta"])],
             [("Aborto", ["Pérdida precoz"]), ("A + 1", [])],
             [("Aborto", ["Pérdida precoz"]), ("A = 2", [])],
             [("A término", []), ("T = 1", [])]]},
  ["G cuenta embarazos: el gemelar es una sola gestación.",
   "Vivos: 2 gemelos + 1 = 3.",
   "Ectópico y mola se registran como abortos."],
  "MINSA – Historia clínica materno perinatal (CLAP/SMR-OPS) · " + WILLIAMS)

# NEF-056 · árbol
A("NEF-056", "erc-hemodialisis-ferritina-56-ist-10-hierro-mantener-epo", "Anemia de la ERC con ferropenia",
  "NEFROLOGÍA ENAM: ANEMIA DE LA ENFERMEDAD RENAL CRÓNICA", "NEFROLOGÍA",
  ("Anemia de la ERC", ["La eritropoyetina no funciona sin hierro suficiente",
   "Ferropenia (ferritina < 100, IST < 20%): dar hierro y mantener la EPO"]),
  ("Varón de 56 años en hemodiálisis", ["Recibe eritropoyetina adecuada · disnea", "Hb 8.7 · ferritina 56 · IST 10%"]),
  Q("¿Ferritina < 100 o IST < 20%?", [
      L("Sí", "HIERRO + MANTENER EPO", ["Hierro EV en hemodiálisis"], path=True),
      L("No", "Ajustar la dosis de EPO", ["Buscar otras causas"])], path=True),
  ("Metas en la anemia de la ERC", [("Meta", True)], [
      ("Hemoglobina", ["10-11.5 g/dL"]),
      ("Ferritina", ["> 100 (diálisis > 200)"]),
      ("Saturación de transferrina", ["> 20%"])]),
  ["No suspender la EPO: la anemia empeoraría.",
   "Hb > 13 con EPO aumenta el riesgo de ACV y trombosis.",
   "Descartar sangrado, inflamación y déficit de B12 o folato."],
  "KDIGO – Clinical practice guideline for anemia in CKD (2012, act. 2024)")

# PED-133 · termómetro
V("termometro", "PED-133", "lactante-picadura-escorpion-falla-cardiorrespiratoria", "Picadura de escorpión en el niño",
  "PEDIATRÍA ENAM: ESCORPIONISMO", "PEDIATRÍA",
  ("Escorpionismo", ["La toxina libera catecolaminas y acetilcolina",
   "En lactantes: edema pulmonar, miocarditis y choque"]),
  ("Lactante de 1 año", ["Picadura de escorpión", "Llega 6 horas después"]),
  {"rotulo": "Gravedad",
   "niveles": [("Grado I", "Local", ["Dolor, parestesia"]),
               ("Grado II", "Sistémico leve", ["Sudor, vómitos, taquicardia"]),
               ("Grado III", "Grave", ["Edema pulmonar, choque"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Analgesia y observación", ["6-12 horas mínimo"], False),
             (2, "Antiveneno", ["Si hay signos sistémicos"], False),
             (3, "FALLA CARDIORRESPIRATORIA", ["UCI: soporte y vasoactivos"], True)]},
  ["Los niños pequeños tienen más riesgo por su menor peso.",
   "Anafilaxia y necrosis local son raras.",
   "En el Perú: Tityus en la costa norte y selva."],
  "MINSA – Norma técnica de accidentes por animales ponzoñosos · " + NELSON)

# GIN-130 · árbol
A("GIN-130", "dilatacion-6-a-8-en-2-horas-continuar-trabajo-parto", "Progreso del trabajo de parto",
  "OBSTETRICIA ENAM: TRABAJO DE PARTO NORMAL", "OBSTETRICIA",
  ("Fase activa del trabajo de parto", ["Se espera dilatar alrededor de 1 cm por hora",
   "Si progresa, se deja evolucionar sin intervenir"]),
  ("Primigesta de 39 semanas en trabajo de parto", ["6 cm, AP −3", "2 horas después: 8 cm, AP −2"]),
  Q("¿Dilata ≥ 1 cm por hora?", [
      L("Sí: de 6 a 8 cm en 2 h", "CONTINUAR EL TRABAJO DE PARTO", ["Vigilancia con partograma"], path=True),
      L("No", "Evaluar la causa", ["Dinámica, pelvis, posición"])], path=True),
  ("Partograma", [("Normal", True), ("Anormal", False)], [
      ("Fase activa", ["≥ 1 cm/h", "Sin cambio en 4 h"]),
      ("Descenso", ["Progresivo", "Detenido"])]),
  ["Oxitocina solo si la dinámica es insuficiente.",
   "Misoprostol es para madurar el cérvix, no en fase activa.",
   "Cesárea por detención de la fase activa, no por lentitud leve."],
  "OMS – Recomendaciones sobre cuidados intraparto (2018) · ACOG/SMFM – Safe prevention of the primary cesarean (2014, reafirmado 2024)")

# PSI-025 · puntaje
V("puntaje", "PSI-025", "preocupacion-12-meses-tension-insomnio-ansiedad-generalizada", "Ansiedad generalizada: criterios",
  "PSIQUIATRÍA ENAM: TRASTORNO DE ANSIEDAD GENERALIZADA", "PSIQUIATRÍA",
  ("Trastorno de ansiedad generalizada", ["Preocupación excesiva y difícil de controlar ≥ 6 meses",
   "Con ≥ 3 de 6 síntomas físicos o cognitivos"]),
  ("Mujer de 30 años con 12 meses de síntomas", ["Preocupación intensa por todo", "Inquieta, irritable, tensa, sin concentración, insomnio"]),
  {"rotulo": "Síntomas DSM-5 en el caso", "escala": "DSM-5", "total": 5, "max": 6,
   "total_label": "Síntomas presentes",
   "interpreta": "Trastorno de ansiedad generalizada",
   "items": [("Inquietud", "1", True), ("Fatiga fácil", "1", False),
             ("Dificultad de concentración", "1", True), ("Irritabilidad", "1", True),
             ("Tensión muscular", "1", True), ("Alteración del sueño", "1", True)],
   "bandas": [("< 3", "No cumple", "Buscar otro trastorno", False),
              ("≥ 3", "TAG", "ISRS o IRSN + terapia cognitivo-conductual", True)]},
  ["Duración mínima: 6 meses.",
   "Distimia: ánimo depresivo crónico, no preocupación.",
   "Evitar benzodiacepinas a largo plazo."],
  "APA – DSM-5-TR (2022) · NICE – Generalised anxiety disorder and panic disorder in adults (2020)")

# GIN-131 · embudo
V("embudo", "GIN-131", "amniotomia-sangrado-profuso-bradicardia-vasa-previa-cesarea", "Sangrado tras la amniotomía",
  "OBSTETRICIA ENAM: ROTURA DE VASA PREVIA", "OBSTETRICIA",
  ("Rotura de vasa previa", ["Sangrado al romper membranas con caída brusca de la FCF",
   "La sangre es fetal: cesárea de emergencia"]),
  ("Primigesta de 40 semanas sin controles", ["8 cm, AP −4 · se rompen membranas", "Sangrado profuso y caída rápida de la FCF"]),
  {"rotulo": "Embudo de conductas",
   "inicio": "Sangrado y bradicardia tras la amniotomía",
   "candidatos": ["Cesárea de emergencia", "Vacuum", "Fórceps", "Amniotransfusión", "Esperar el parto"],
   "pasos": [("Cabeza alta (AP −4): no es instrumentable", ["Vacuum", "Fórceps"]),
             ("El feto se desangra en minutos", ["Esperar el parto", "Amniotransfusión"])],
   "final": ("CESÁREA DE EMERGENCIA", ["Extraer al feto de inmediato", "Neonatólogo: transfusión"]),
   "nota": "La volemia fetal es ~ 80-100 mL/kg: pierde poca sangre y ya entra en choque."},
  ["El diagnóstico prenatal (Doppler) permite programar la cesárea.",
   "Prueba de Apt: distingue sangre fetal de materna.",
   "Mortalidad fetal alta si no se diagnostica antes del parto."],
  "SMFM – Consult Series N.° 37: Vasa previa (2015) · " + WILLIAMS)
