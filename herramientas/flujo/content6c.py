"""Bloque 6 · parte C."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"

# SP-061 · radial
V("radial", "SP-061", "pertinencia-cultural-servicios-interculturalidad", "Enfoques del modelo de cuidado integral",
  "SALUD PÚBLICA ENAM: ENFOQUE INTERCULTURAL", "SALUD PÚBLICA",
  ("Enfoques del Modelo de Cuidado Integral", ["Interculturalidad: servicios con pertinencia cultural",
   "Respeto y diálogo entre la cultura del usuario y la del sistema de salud"]),
  ("Capacitación al equipo de salud", ["Respeto a las culturas y servicios con pertinencia cultural", "Comunicación que derriba barreras culturales"]),
  {"rotulo": "Mapa del tema", "centro": "ENFOQUES DEL MCI", "centro_sub": "Modelo de cuidado integral", "ans": 0,
   "items": [("INTERCULTURALIDAD", ["Pertinencia cultural", "Diálogo de saberes"]),
             ("Derechos humanos", ["Salud como derecho"]),
             ("Género", ["Equidad entre hombres y mujeres"]),
             ("Territorialidad", ["Según el espacio geográfico"]),
             ("Curso de vida", ["Etapas de la vida"])],
   "ruta": ["Respeto a las culturas", "Servicios con pertinencia cultural", "Inclusión social", "INTERCULTURALIDAD"]},
  ["Ejemplo: parto vertical y casas de espera materna en zonas andinas.",
   "Pluriculturalidad describe la coexistencia de culturas; interculturalidad, su diálogo.",
   "Incluye intérpretes y material en lenguas originarias."],
  "MINSA – Política sectorial de salud intercultural (DS N.° 016-2016-SA) · MINSA – Modelo de Cuidado Integral de Salud por Curso de Vida (2020)")

# PED-100 · matriz
V("matriz", "PED-100", "ano-imperforado-nina-fistula-rectovestibular", "Malformaciones anorrectales",
  "PEDIATRÍA ENAM: MALFORMACIÓN ANORRECTAL", "PEDIATRÍA",
  ("Ano imperforado", ["El recto suele abrirse en una fístula",
   "Niñas: fístula rectovestibular · niños: fístula rectouretral"]),
  ("Pregunta de concepto", ["Defecto más frecuente asociado a ano imperforado", "en recién nacidas"]),
  {"rotulo": "Fístula según el sexo", "eje_x": "Frecuencia", "eje_y": "Sexo",
   "cols": ["Más frecuente", "Otras"], "rows": ["Mujer", "Varón"], "caso": (0, 0),
   "cells": [[("RECTOVESTIBULAR", ["Detrás del himen"]), ("Perineal, cloaca", ["Cloaca: la más compleja"])],
             [("Rectouretral", ["Meconio en la orina"]), ("Perineal, rectovesical", [])]]},
  ["Buscar asociación VACTERL: vertebral, anal, cardíaca, traqueoesofágica, renal y extremidades.",
   "Fístula perineal visible: reparación sin colostomía.",
   "Esperar 16-24 h para que el meconio muestre la fístula."],
  "Holcomb and Ashcraft's Pediatric Surgery 7.ª ed. (2019) · " + NELSON)

# PED-101 · tarjetas
V("tarjetas", "PED-101", "prematuro-32-semanas-letargia-fontanela-llena-hiv", "Deterioro neurológico en el prematuro",
  "PEDIATRÍA ENAM: HEMORRAGIA INTRAVENTRICULAR", "PEDIATRÍA",
  ("Hemorragia intraventricular del prematuro", ["Sangrado de la matriz germinal en los primeros 3 días de vida",
   "Letargia, apneas, fontanela llena y caída del hematocrito"]),
  ("RN de 32 semanas y 1400 g, día 2 de vida", ["Letargia, hipoactividad, apneas", "Fontanela llena · perímetro cefálico en aumento"]),
  {"rotulo": "¿Qué ocurre?", "ans": 0, "cards": [
      {"titulo": "HEMORRAGIA INTRAVENTRICULAR", "datos": [
          ("Terreno", "Prematuro < 32 sem", True), ("Momento", "Primeros 3 días", True),
          ("Estudio", "Ecografía transfontanelar", False)],
       "pie": "Grados I a IV (Papile)"},
      {"titulo": "Hemorragia intraparenquimal", "datos": [
          ("Terreno", "Grado IV, infarto venoso", False), ("Momento", "Tras la HIV", False),
          ("Estudio", "Ecografía", False)],
       "pie": "Secuela motora"},
      {"titulo": "Hemorragia subaracnoidea", "datos": [
          ("Terreno", "RN a término", False), ("Momento", "Parto traumático", False),
          ("Estudio", "TC", False)],
       "pie": "Suele ser benigna"},
      {"titulo": "Hidrocefalia", "datos": [
          ("Terreno", "Secuela de la HIV", False), ("Momento", "Semanas después", False),
          ("Estudio", "Ecografía seriada", False)],
       "pie": "Derivación si progresa"}]},
  ["La matriz germinal es frágil hasta las 32-34 semanas.",
   "Tamizaje con ecografía transfontanelar en todo < 32 semanas.",
   "Prevención: corticoides antenatales y evitar fluctuaciones de presión."],
  NELSON + " · Volpe's Neurology of the Newborn 7.ª ed. (2024)")

# GAS-034 · fases
V("fases", "GAS-034", "adolescente-ictericia-igm-anti-vha", "Hepatitis A: serología",
  "GASTROENTEROLOGÍA ENAM: HEPATITIS A", "GASTROENTEROLOGÍA",
  ("Hepatitis A aguda", ["Pródromo con fiebre y vómitos, luego ictericia",
   "La IgM anti-VHA confirma la infección aguda; la IgG indica infección pasada o vacuna"]),
  ("Adolescente con 5 días de fiebre y vómitos", ["Prurito, ictericia y hepatomegalia", "Mucosas secas"]),
  {"rotulo": "Curso y anticuerpos", "ans": 2,
   "fases": [("Incubación", "2-6 sem", "Sin síntomas", ["Virus en heces"]),
             ("Pródromo", "Días", "Fiebre, vómitos", ["Muy contagioso"]),
             ("Ictérica", "1-4 sem", "IgM ANTI-VHA (+)", ["Confirma el diagnóstico"]),
             ("Recuperación", "Meses", "IgG anti-VHA", ["Inmunidad de por vida"])],
   "curvas": [("IgM", ROSE, [0.05, 0.3, 0.9, 0.95, 0.6, 0.25, 0.05]),
              ("IgG", SKY, [0.02, 0.05, 0.3, 0.6, 0.8, 0.9, 0.95])],
   "chips_titulo": "Examen · marcado el correcto",
   "chips": [("IgM anti-VHA", True), ("IgG anti-VHA", False), ("IgG anti-VHB", False), ("IgM anti-VHB", False)]},
  ["Transmisión fecal-oral; no se cronifica.",
   "Tratamiento de soporte; vigilar el TP (falla hepática aguda es rara).",
   "Vacuna incluida en el esquema nacional a los 15 meses."],
  "CDC – Hepatitis A: clinical overview (2024) · Harrison's Principles of Internal Medicine 22.ª ed. (2025)")

# OFT-021 · tarjetas
V("tarjetas", "OFT-021", "lupus-hidroxicloroquina-maculopatia-bilateral", "Maculopatía en paciente con lupus",
  "OFTALMOLOGÍA ENAM: TOXICIDAD RETINIANA POR HIDROXICLOROQUINA", "OFTALMOLOGÍA",
  ("Toxicidad por hidroxicloroquina", ["Uso prolongado: maculopatía bilateral en «ojo de buey»",
   "Irreversible: por eso se hace tamizaje oftalmológico"]),
  ("Mujer de 27 años con LES y nefritis lúpica severa", ["Hidroxicloroquina y corticoides permanentes", "Pérdida visual progresiva · maculopatía bilateral severa"]),
  {"rotulo": "¿Qué dañó la retina?", "ans": 0, "cards": [
      {"titulo": "HIDROXICLOROQUINA", "datos": [
          ("Fondo de ojo", "Maculopatía en «ojo de buey»", True), ("Lado", "Bilateral, simétrica", True),
          ("Riesgo", "Dosis alta, falla renal", True)],
       "pie": "Suspender; es irreversible"},
      {"titulo": "Retinopatía hipertensiva", "datos": [
          ("Fondo de ojo", "Hemorragias en llama, exudados", False), ("Lado", "Bilateral", False),
          ("Riesgo", "PA muy alta", False)],
       "pie": "Controlar la PA"},
      {"titulo": "Vasculitis lúpica", "datos": [
          ("Fondo de ojo", "Exudados algodonosos", False), ("Lado", "Variable", False),
          ("Riesgo", "Lupus activo", False)],
       "pie": "Inmunosupresión"},
      {"titulo": "Corticoides", "datos": [
          ("Fondo de ojo", "Normal", False), ("Lado", "Bilateral", False),
          ("Riesgo", "Catarata, glaucoma", False)],
       "pie": "Catarata subcapsular posterior"}]},
  ["Dosis segura: ≤ 5 mg/kg/día de peso real.",
   "Tamizaje basal y anual desde los 5 años de uso (antes si hay falla renal).",
   "La insuficiencia renal de la nefritis lúpica aumenta la toxicidad."],
  "AAO – Recommendations on screening for chloroquine and hydroxychloroquine retinopathy (Ophthalmology 2016)")

# INF-044 · matriz
V("matriz", "INF-044", "ascitis-exudado-linfocitos-peritonitis-tuberculosa", "Análisis del líquido ascítico",
  "INFECTOLOGÍA ENAM: PERITONITIS TUBERCULOSA", "INFECTOLOGÍA",
  ("Líquido ascítico", ["Exudado con predominio de linfocitos + síntomas constitucionales = TB peritoneal",
   "El ADA > 39 U/L apoya el diagnóstico"]),
  ("Varón de 25 años con 3 semanas de fiebre y baja de peso", ["Abdomen en «tablero de ajedrez», ascitis", "Exudado rico en proteínas con linfocitos"]),
  {"rotulo": "Tipos de ascitis", "eje_x": "Hallazgo", "eje_y": "Causa",
   "cols": ["Tipo", "Células"], "rows": ["TB peritoneal", "Peritonitis bacteriana", "Cirrosis", "Carcinomatosis"], "caso": (0, 1),
   "cells": [[("Exudado", ["GASA < 1.1"]), ("LINFOCITOS", ["ADA alto"])],
             [("Trasudado en cirrótico", []), ("PMN ≥ 250", [])],
             [("Trasudado", ["GASA ≥ 1.1"]), ("Pocas células", [])],
             [("Exudado", []), ("Células malignas", ["Citología"])]]},
  ["El cultivo es lento y poco sensible: la laparoscopia con biopsia es la más útil.",
   "Tratamiento con esquema antituberculoso estándar.",
   "Crohn y colitis ulcerosa no producen ascitis exudativa linfocitaria."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · Sleisenger and Fordtran's Gastrointestinal and Liver Disease 11.ª ed. (2021)")

# GIN-090 · árbol
A("GIN-090", "tormenta-de-nieve-utero-grande-mola-evacuacion", "Enfermedad trofoblástica gestacional",
  "OBSTETRICIA ENAM: MOLA HIDATIFORME", "OBSTETRICIA",
  ("Mola hidatiforme", ["Útero mayor que la amenorrea + sangrado + imagen en «tormenta de nieve»",
   "Tratamiento: evacuación por aspiración y seguimiento con β-hCG"]),
  ("Mujer de 32 años, nulípara, 8 semanas de amenorrea", ["Sangrado vaginal moderado", "Útero de 12 cm · ecografía en «tormenta de nieve»"]),
  Q("¿Desea preservar la fertilidad?", [
      L("Sí o nulípara", "EVACUACIÓN POR ASPIRACIÓN", ["AMEU o aspiración eléctrica", "Oxitocina tras dilatar"], path=True),
      L("No, > 40 años", "Histerectomía", ["Con la mola in situ"])], path=True),
  ("Mola completa vs parcial", [("Completa", True), ("Parcial", False)], [
      ("Cariotipo", ["46,XX (paterno)", "69,XXY (triploide)"]),
      ("Feto", ["No", "Sí, anómalo"]),
      ("Neoplasia posterior", ["15-20%", "1-5%"])]),
  ["Seguimiento con β-hCG semanal hasta negativizar y luego mensual.",
   "Anticoncepción eficaz durante el seguimiento.",
   "La quimioterapia es para la neoplasia trofoblástica, no para la mola."],
  "FIGO – Update on the diagnosis and management of gestational trophoblastic disease (Int J Gynaecol Obstet 2021) · " + WILLIAMS)

# TRA-016 · termómetro
V("termometro", "TRA-016", "recien-nacido-cadera-ecografia-graf", "Displasia de cadera: estudio según la edad",
  "TRAUMATOLOGÍA ENAM: DISPLASIA DEL DESARROLLO DE LA CADERA", "TRAUMATOLOGÍA",
  ("Estudio de la displasia de cadera", ["En el recién nacido la cabeza femoral es cartilaginosa: no se ve en Rx",
   "Antes de los 4-6 meses se usa la ecografía (Graf)"]),
  ("Pregunta de concepto", ["Estudio de referencia para el tamizaje", "de displasia de cadera en el recién nacido"]),
  {"rotulo": "Edad del niño",
   "niveles": [("0-4 m", "Recién nacido", ["ECOGRAFÍA (Graf)", "Cabeza cartilaginosa"]),
               ("4-6 m", "Transición", ["Ecografía o Rx"]),
               ("> 6 m", "Lactante mayor", ["Radiografía de pelvis", "Núcleo de osificación visible"])],
   "caso_nivel": 0, "ruta_titulo": "Tamizaje", "paso_label": "PASO",
   "pasos": [(1, "Ortolani y Barlow al nacer", ["Examen clínico a todo RN"], False),
             (2, "ECOGRAFÍA DE CADERA", ["A las 4-6 semanas si hay riesgo"], True),
             (3, "Arnés de Pavlik si es displásica", ["Menores de 6 meses"], False)]},
  ["Factores de riesgo: sexo femenino, presentación podálica, antecedente familiar.",
   "La ecografía antes de las 4 semanas da falsos positivos (laxitud fisiológica).",
   "TC y RM no se usan para el tamizaje."],
  "AAOS – Detection and nonoperative management of pediatric DDH in infants up to 6 months (2022)")

# SP-062 · radial
V("radial", "SP-062", "asis-uso-racional-recursos-eficiencia", "Principios de gestión",
  "SALUD PÚBLICA ENAM: EFICIENCIA", "SALUD PÚBLICA",
  ("Principios de gestión", ["Eficiencia: lograr los objetivos con el mejor uso de los recursos",
   "Eficacia: lograr el objetivo, sin importar el costo"]),
  ("Jefe de un establecimiento de salud", ["Usa el ASIS para priorizar problemas", "Promueve el uso racional de los recursos para sus metas"]),
  {"rotulo": "Mapa del tema", "centro": "GESTIÓN", "centro_sub": "Principios", "ans": 0,
   "items": [("EFICIENCIA", ["Objetivos con uso racional", "de recursos"]),
             ("Eficacia", ["Lograr el objetivo", "En condiciones ideales"]),
             ("Efectividad", ["Resultado en la vida real"]),
             ("Equidad", ["Según necesidad"]),
             ("Integralidad", ["Atención completa"])],
   "ruta": ["ASIS y prioridades", "Planifica actividades", "Uso racional de recursos", "EFICIENCIA"]},
  ["Eficiencia = resultados / recursos usados.",
   "Una intervención puede ser eficaz pero ineficiente si es muy costosa.",
   "La equidad reparte según necesidades, no por igual."],
  "OPS – Funciones esenciales de salud pública renovadas (2020) · MINSA – Gestión en salud")

# PED-102 · embudo
V("embudo", "PED-102", "neonato-9-dias-ictericia-oliguria-hipoactivo-sepsis-tardia", "Neonato de 9 días decaído",
  "PEDIATRÍA ENAM: SEPSIS NEONATAL TARDÍA", "PEDIATRÍA",
  ("Sepsis neonatal", ["Temprana < 72 h (gérmenes maternos) · tardía > 72 h (ambiente u hospital)",
   "Signos inespecíficos: succión débil, hipoactividad, ictericia, oliguria"]),
  ("Neonato de 9 días", ["Ictericia (Kramer 3), succión débil", "Moja poco el pañal · hipoactivo, FC 110"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Neonato con ictericia y decaimiento",
   "candidatos": ["Sepsis tardía", "Sepsis temprana", "Ictericia fisiológica", "Insuficiencia renal", "Hipoalimentación"],
   "pasos": [("Tiene 9 días: más de 72 horas", ["Sepsis temprana"]),
             ("Hipoactivo, succión débil y bradicardia: está enfermo", ["Ictericia fisiológica", "Hipoalimentación"]),
             ("La oliguria es consecuencia, no causa", ["Insuficiencia renal"])],
   "final": ("SEPSIS NEONATAL TARDÍA", ["Referir: hemocultivo, antibióticos", "Buscar meningitis e infección urinaria"]),
   "nota": "Todo neonato hipoactivo que no lacta bien es un signo de peligro: referencia inmediata."},
  ["Gérmenes: S. aureus, estafilococo coagulasa negativo, gramnegativos, SGB tardío.",
   "La ictericia que aparece o reaparece tras la primera semana puede ser infecciosa.",
   "Signos de peligro AIEPI: no puede lactar, letargia, convulsiones, hipotermia o fiebre."],
  NELSON + " · OMS/OPS – AIEPI neonatal")

# PSI-017 · puntaje
V("puntaje", "PSI-017", "tristeza-seis-semanas-ideas-suicidas-episodio-depresivo", "Episodio depresivo: criterios",
  "PSIQUIATRÍA ENAM: EPISODIO DEPRESIVO", "PSIQUIATRÍA",
  ("Episodio depresivo mayor (DSM-5)", ["≥ 5 de 9 síntomas por ≥ 2 semanas, uno debe ser ánimo triste o anhedonia",
   "La ideación suicida obliga a evaluar el riesgo"]),
  ("Varón de 58 años con 6 semanas de tristeza", ["Vacío, insomnio, sin ganas de levantarse", "Falla en la atención · ideas suicidas recurrentes"]),
  {"rotulo": "Criterios DSM-5 en el caso", "escala": "Episodio depresivo", "total": 5, "max": 9,
   "total_label": "Síntomas presentes (≥ 2 semanas)",
   "interpreta": "Cumple episodio depresivo mayor",
   "items": [("Ánimo triste o vacío", "1", True), ("Anhedonia, sin ganas", "1", True), ("Insomnio", "1", True),
             ("Dificultad de concentración", "1", True), ("Ideas de muerte o suicidio", "1", True),
             ("Fatiga", "1", False), ("Cambio de peso o apetito", "1", False), ("Culpa o inutilidad", "1", False),
             ("Enlentecimiento o agitación", "1", False)],
   "bandas": [("< 5", "No cumple", "Otros diagnósticos", False),
              ("≥ 5", "Episodio depresivo", "Evaluar riesgo suicida; ISRS + psicoterapia", True)]},
  ["Con ideación suicida recurrente: evaluar plan, medios e intentos previos.",
   "Seudodemencia: depresión en ancianos que simula deterioro cognitivo.",
   "Descartar hipotiroidismo y consumo de sustancias."],
  "APA – DSM-5-TR (2022) · NICE – Depression in adults: treatment and management (2022)")

# CB-029 · fases
V("fases", "CB-029", "higado-xenobioticos-fase-1-hidroxilacion", "Biotransformación hepática",
  "CIENCIAS BÁSICAS ENAM: METABOLISMO DE XENOBIÓTICOS", "CIENCIAS BÁSICAS",
  ("Biotransformación de xenobióticos", ["El hígado convierte sustancias liposolubles en hidrosolubles para excretarlas",
   "Fase I: oxidación (hidroxilación) por el citocromo P450"]),
  ("Pregunta de concepto", ["Función principal del hígado en el metabolismo", "de xenobióticos de los alimentos"]),
  {"rotulo": "Fases del metabolismo", "ans": 0,
   "fases": [("Fase I", "Primero", "HIDROXILACIÓN", ["Citocromo P450", "Añade un grupo polar"]),
             ("Fase II", "Después", "Conjugación", ["Glucurónido, sulfato, glutatión"]),
             ("Fase III", "Final", "Excreción", ["Bilis u orina"])],
   "curvas": [("Liposol.", ROSE, [0.95, 0.85, 0.6, 0.4, 0.25, 0.15, 0.1])],
   "chips_titulo": "Función principal · marcada la correcta",
   "chips": [("Hidroxilación enzimática", True), ("Hidrólisis a apolares", False), ("Conjugación con nucleótidos", False), ("Esterificación", False)]},
  ["Inductores del P450: rifampicina, carbamazepina, fenitoína, alcohol crónico.",
   "Inhibidores: macrólidos, azoles, jugo de toronja.",
   "La fase I puede generar metabolitos tóxicos (NAPQI del paracetamol)."],
  "Goodman & Gilman's The Pharmacological Basis of Therapeutics 14.ª ed. (2023)")

# CIR-055 · árbol
A("CIR-055", "anciano-obstruccion-masa-rectal-colostomia", "Obstrucción por cáncer colorrectal",
  "CIRUGÍA ENAM: OBSTRUCCIÓN INTESTINAL POR CÁNCER DE COLON", "CIRUGÍA",
  ("Obstrucción de colon por tumor", ["Adulto mayor con baja de peso, hematoquecia y obstrucción baja",
   "En recto o colon izquierdo en mal estado: colostomía descompresiva"]),
  ("Varón de 80 años con 2 días de distensión y sin flatos", ["Baja de 8 kg, hematoquecia · fiebre 39 °C", "Tacto rectal: masa dura con coágulos"]),
  Q("¿Dónde está el tumor?", [
      L("Colon derecho", "Hemicolectomía derecha", ["Anastomosis primaria"]),
      Q("¿Puede resecarse con seguridad?", [
          L("No: anciano, fiebre", "COLOSTOMÍA DESCOMPRESIVA", ["Derivar primero", "Estudiar y tratar después"], path=True),
          L("Sí", "Resección (Hartmann)", ["O stent como puente"])],
        edge="Recto o colon izquierdo", path=True)], path=True),
  ("Obstrucción baja", [("Cáncer", True), ("Vólvulo", False)], [
      ("Clínica", ["Progresiva, baja de peso", "Súbita, gran distensión"]),
      ("Rx", ["Corte de colon", "Grano de café"]),
      ("Manejo", ["Colostomía o resección", "Desvolvular por endoscopia"])]),
  ["La ileostomía no descomprime un colon obstruido con válvula ileocecal competente.",
   "Obstrucción en asa cerrada: riesgo de perforación del ciego (> 12 cm).",
   "La colonoscopia no se hace con una obstrucción completa aguda."],
  "WSES – Obstructive left colon carcinoma guidelines (World J Emerg Surg 2018) · Sabiston Textbook of Surgery 21.ª ed. (2021)")

# CAR-037 · radial
V("radial", "CAR-037", "arequipa-cardiomegalia-megaesofago-megacolon-chagas", "Chagas crónico",
  "CARDIOLOGÍA ENAM: ENFERMEDAD DE CHAGAS CRÓNICA", "CARDIOLOGÍA",
  ("Enfermedad de Chagas crónica", ["Trypanosoma cruzi transmitido por la chirimacha (sur del Perú)",
   "Miocardiopatía dilatada con arritmias + megaesófago + megacolon"]),
  ("Mujer de 36 años de zona rural de Arequipa", ["Disnea 2 años, galope, FA · gran cardiomegalia", "Disfagia, estreñimiento · megaesófago y megacolon"]),
  {"rotulo": "Mapa del tema", "centro": "CHAGAS CRÓNICO", "centro_sub": "Trypanosoma cruzi", "ans": 0,
   "items": [("MIOCARDIOPATÍA", ["Dilatada, arritmias", "Bloqueo de rama derecha"]),
             ("Megaesófago", ["Disfagia, simula acalasia"]),
             ("Megacolon", ["Estreñimiento crónico"]),
             ("Tromboembolias", ["Aneurisma apical"]),
             ("Forma indeterminada", ["Serología (+), sin síntomas"])],
   "ruta": ["Procede de Arequipa rural", "Cardiomegalia + FA", "Megaesófago y megacolon", "ENFERMEDAD DE CHAGAS"]},
  ["Diagnóstico en fase crónica: dos serologías distintas positivas.",
   "Beriberi húmedo: alcohol y déficit de tiamina, sin megavísceras.",
   "Benznidazol sirve más en fase aguda y en jóvenes."],
  "OPS – Guía para el diagnóstico y el tratamiento de la enfermedad de Chagas (2018) · MINSA – NTS de prevención y control de la enfermedad de Chagas")

# CIR-056 · fases
V("fases", "CIR-056", "motociclista-sin-casco-glasgow-8-intubacion", "Politraumatizado: ABCDE",
  "CIRUGÍA ENAM: VÍA AÉREA EN EL POLITRAUMATIZADO", "CIRUGÍA",
  ("Evaluación primaria del trauma", ["Se atiende en orden: A, B, C, D, E",
   "Glasgow ≤ 8 = no protege la vía aérea: intubación orotraqueal"]),
  ("Motociclista de 35 años sin casco", ["PA 80/60 · FC 110 · SatO₂ 90%", "Glasgow 8"]),
  {"rotulo": "Evaluación primaria", "ans": 0,
   "fases": [("A", "Primero", "VÍA AÉREA", ["IOT si Glasgow ≤ 8", "Proteger columna cervical"]),
             ("B", "Segundo", "Ventilación", ["Neumotórax, hemotórax"]),
             ("C", "Tercero", "Circulación", ["Controlar sangrado, fluidos"]),
             ("D", "Cuarto", "Neurológico", ["Glasgow, pupilas"])],
   "curvas": [],
   "chips_titulo": "Medida inicial · marcada la correcta",
   "chips": [("Intubación orotraqueal", True), ("Manitol", False), ("TC cerebral", False), ("Analgésicos", False)]},
  ["La TC se hace después de estabilizar ABC.",
   "Hipotensión e hipoxia duplican la mortalidad del TEC.",
   "El manitol no se usa en un paciente hipotenso."],
  ATLS + " · Brain Trauma Foundation – Guidelines for the management of severe TBI 4.ª ed. (2016)")

# NRL-026 · tarjetas
V("tarjetas", "NRL-026", "deterioro-atencional-alucinaciones-parkinsonismo-lewy", "Tipos de demencia",
  "NEUROLOGÍA ENAM: DEMENCIA CON CUERPOS DE LEWY", "NEUROLOGÍA",
  ("Demencia con cuerpos de Lewy", ["Deterioro cognitivo fluctuante + alucinaciones visuales + parkinsonismo",
   "Hipersensibilidad grave a los antipsicóticos"]),
  ("Varón de 62 años con deterioro progresivo", ["Pérdida de atención, «ve personas que lo vigilan»", "Facies inexpresiva, temblor, rigidez, bradicinesia"]),
  {"rotulo": "¿Qué demencia es?", "ans": 0, "cards": [
      {"titulo": "CUERPOS DE LEWY", "datos": [
          ("Inicio", "Atención fluctuante", True), ("Clave", "Alucinaciones visuales", True),
          ("Motor", "Parkinsonismo", True)],
       "pie": "Evitar haloperidol"},
      {"titulo": "Alzheimer", "datos": [
          ("Inicio", "Memoria reciente", False), ("Clave", "Progresión lenta", False),
          ("Motor", "Normal al inicio", False)],
       "pie": "La más frecuente"},
      {"titulo": "Frontotemporal", "datos": [
          ("Inicio", "Conducta, lenguaje", False), ("Clave", "Desinhibición", False),
          ("Motor", "Normal", False)],
       "pie": "Inicio < 65 años"},
      {"titulo": "Seudodemencia", "datos": [
          ("Inicio", "Brusco, con depresión", False), ("Clave", "«No sé», se queja", False),
          ("Motor", "Normal", False)],
       "pie": "Mejora con antidepresivo"}]},
  ["Si el parkinsonismo precede a la demencia más de un año: demencia de la enfermedad de Parkinson.",
   "Trastorno de conducta del sueño REM es otro rasgo central.",
   "Tratamiento: inhibidores de colinesterasa (rivastigmina)."],
  "McKeith IG et al. – Diagnosis and management of dementia with Lewy bodies: fourth consensus (Neurology 2017)")

# OFT-022 · árbol
A("OFT-022", "golpe-pabellon-auricular-hematoma-subpericondrico", "Trauma del pabellón auricular",
  "OTORRINOLARINGOLOGÍA ENAM: HEMATOMA SUBPERICÓNDRICO", "OTORRINOLARINGOLOGÍA",
  ("Trauma del pabellón auricular", ["La sangre se acumula entre el cartílago y el pericondrio",
   "Sin drenaje, el cartílago se necrosa: oreja en coliflor"]),
  ("Niño de 10 años con golpe en la oreja hace 2 horas", ["Edema y nódulo en el pabellón auricular"]),
  Q("¿Colección tras el trauma?", [
      L("Sí, aguda", "HEMATOMA SUBPERICÓNDRICO", ["Drenaje y vendaje compresivo", "Antes de 7 días"], path=True),
      L("Días después, fiebre", "Pericondritis o absceso", ["Antibiótico antipseudomona"]),
      L("No", "Contusión", ["Frío y analgesia"])], path=True),
  ("Trastornos del pabellón", [("Hematoma", True), ("Pericondritis", False)], [
      ("Inicio", ["Tras el golpe", "Días, tras piercing o herida"]),
      ("Signos", ["Masa fluctuante", "Eritema, dolor, fiebre"]),
      ("Complicación", ["Oreja en coliflor", "Deformidad del cartílago"])]),
  ["Frecuente en luchadores y rugbistas.",
   "El vendaje compresivo evita que se reacumule.",
   "La pericondritis respeta el lóbulo (no tiene cartílago)."],
  "Cummings Otolaryngology – Head and Neck Surgery 7.ª ed. (2021)")

# PED-103 · termómetro
V("termometro", "PED-103", "nino-edema-proteinuria-rango-nefrotico-pediatrico", "Síndrome nefrótico: proteinuria en el niño",
  "PEDIATRÍA ENAM: SÍNDROME NEFRÓTICO", "PEDIATRÍA",
  ("Síndrome nefrótico en el niño", ["Proteinuria nefrótica ≥ 40 mg/m²/h (o cociente prot/creat ≥ 2 mg/mg)",
   "+ hipoalbuminemia < 2.5 g/dL y edema"]),
  ("Niño de 5 años con edema palpebral y de piernas", ["3 días de evolución · PA normal", "Proteínas en orina ++/+++"]),
  {"rotulo": "Proteinuria (mg/m²/h)",
   "niveles": [("< 4", "Normal", ["Fisiológica"]),
               ("4-39", "Patológica", ["No nefrótica"]),
               ("≥ 40", "Nefrótica", ["SÍNDROME NEFRÓTICO", "Con edema e hipoalbuminemia"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Confirmar proteinuria ≥ 40", ["Orina de 12-24 h o cociente"], True),
             (2, "Prednisona 60 mg/m²/día", ["4-6 semanas y luego días alternos"], False),
             (3, "Biopsia solo si no responde", ["Corticorresistente"], False)]},
  ["En el adulto el umbral es > 3.5 g/24 h.",
   "La causa más frecuente en niños es la enfermedad de cambios mínimos.",
   "Complicaciones: infecciones (peritonitis), trombosis, hipovolemia."],
  "IPNA – Clinical practice recommendations for steroid-sensitive nephrotic syndrome (Pediatr Nephrol 2023) · " + NELSON)

# HEM-020 · puntaje
V("puntaje", "HEM-020", "heparina-dia-8-plaquetas-27000-trombocitopenia", "Trombocitopenia por heparina: 4T",
  "HEMATOLOGÍA ENAM: TROMBOCITOPENIA INDUCIDA POR HEPARINA", "HEMATOLOGÍA",
  ("Trombocitopenia inducida por heparina (TIH)", ["Anticuerpos contra el complejo heparina-PF4, a los 5-10 días",
   "Aunque bajan las plaquetas, el riesgo es de trombosis"]),
  ("Mujer de 71 años con TEP tras prótesis de cadera", ["Día 8 de heparina no fraccionada", "Petequias · plaquetas 27 200 · TP y TTPa normales"]),
  {"rotulo": "Escala 4T en el caso", "escala": "4T", "total": 6, "max": 8,
   "total_label": "Puntaje 4T",
   "interpreta": "Probabilidad alta de TIH",
   "items": [("Caída > 50% (nadir ≥ 20 000)", "2", True), ("Inicio a los 5-10 días", "2", True),
             ("Trombosis nueva", "2", False), ("Sin otra causa evidente", "2", True)],
   "bandas": [("0-3", "Baja", "Buscar otra causa", False),
              ("4-5", "Intermedia", "Pedir anticuerpos anti-PF4", False),
              ("6-8", "Alta", "Suspender heparina; argatrobán o fondaparinux", True)]},
  ["No transfundir plaquetas salvo sangrado grave: favorecen la trombosis.",
   "No pasar a warfarina hasta que las plaquetas se recuperen.",
   "CID: TP y TTPa alargados y fibrinógeno bajo (aquí son normales)."],
  "ASH – Guidelines for management of heparin-induced thrombocytopenia (Blood Adv 2018)")

# GAS-035 · matriz
V("matriz", "GAS-035", "ictericia-ayuno-bilirrubina-indirecta-gilbert", "Hiperbilirrubinemias",
  "GASTROENTEROLOGÍA ENAM: SÍNDROME DE GILBERT", "GASTROENTEROLOGÍA",
  ("Hiperbilirrubinemia no conjugada aislada", ["Ictericia leve con ayuno o estrés, sin hemólisis ni daño hepático",
   "Gilbert: menor actividad de la glucuroniltransferasa (UGT1A1)"]),
  ("Varón de 23 años con ictericia al ayunar", ["Cede en 2 días, sin coluria ni acolia", "BT 3.1 · BD 0.3 · enzimas, DHL y haptoglobina normales"]),
  {"rotulo": "Causas de hiperbilirrubinemia", "eje_x": "Dato", "eje_y": "Causa",
   "cols": ["Bilirrubina", "Otras pruebas"], "rows": ["Gilbert", "Hemólisis", "Crigler-Najjar", "Dubin-Johnson"], "caso": (0, 1),
   "cells": [[("Indirecta < 4", ["Con ayuno"]), ("TODO NORMAL", ["Hb, DHL, haptoglobina"])],
             [("Indirecta", []), ("DHL alta, haptoglobina baja", ["Anemia"])],
             [("Indirecta muy alta", ["Neonatos"]), ("Kernícterus (tipo I)", [])],
             [("Directa", []), ("Hígado negro", ["Coluria"])]]},
  ["Es benigno: no requiere tratamiento ni seguimiento.",
   "Afecta al 5-10% de la población.",
   "Puede aumentar la toxicidad del irinotecán."],
  "EASL – Clinical practice guidelines on the management of liver chemistry abnormalities · Harrison's Principles of Internal Medicine 22.ª ed. (2025)")

# HEM-021 · embudo
V("embudo", "HEM-021", "nina-petequias-gingivorragia-postviral-pti", "Petequias en la niña tras una infección",
  "HEMATOLOGÍA ENAM: TROMBOCITOPENIA INMUNE PRIMARIA", "HEMATOLOGÍA",
  ("Trombocitopenia inmune primaria (PTI)", ["Niño sano, 2-4 semanas tras una infección viral",
   "Petequias y sangrado mucoso con plaquetas aisladamente bajas"]),
  ("Niña de 3 años, rinofaringitis hace 2 semanas", ["Petequias y gingivorragia", "Plaquetas 8 500 · leucocitos y Hb casi normales · creatinina normal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Niña con petequias y gingivorragia",
   "candidatos": ["PTI", "Leucemia", "Anemia aplásica", "SUH", "von Willebrand"],
   "pasos": [("Solo bajan las plaquetas; sin visceromegalias", ["Leucemia", "Anemia aplásica"]),
             ("Riñón y orina normales", ["SUH"]),
             ("Plaquetas 8 500: el problema es de número", ["von Willebrand"])],
   "final": ("TROMBOCITOPENIA INMUNE PRIMARIA", ["Frotis: plaquetas grandes, sin blastos", "Observación si solo hay petequias"]),
   "nota": "Tratar (IgIV o corticoide) si hay sangrado mucoso importante, no solo por la cifra."},
  ["En niños el 80% remite espontáneamente en 6 meses.",
   "Evitar AINE y deportes de contacto.",
   "Mielograma solo si hay datos atípicos o antes de corticoides si se duda."],
  "ASH – Guidelines for immune thrombocytopenia (Blood Adv 2019) · " + NELSON)

# CB-030 · radial
V("radial", "CB-030", "disfuncion-erectil-vision-azulada-sildenafilo", "Fármacos para la disfunción eréctil",
  "CIENCIAS BÁSICAS ENAM: EFECTOS ADVERSOS DEL SILDENAFILO", "CIENCIAS BÁSICAS",
  ("Inhibidores de la fosfodiesterasa 5", ["El sildenafilo también inhibe algo la PDE6 de la retina",
   "Visión azulada, cefalea y rubor facial son efectos típicos"]),
  ("Varón de 42 años en tratamiento para disfunción eréctil", ["Cefalea y visión azul-verdosa pasajera", "Eritema facial"]),
  {"rotulo": "Mapa del tema", "centro": "DISFUNCIÓN ERÉCTIL", "centro_sub": "Fármacos", "ans": 0,
   "items": [("SILDENAFILO", ["Inhibe PDE5 (y PDE6)", "Visión azul, cefalea, rubor"]),
             ("Tadalafilo", ["Más duradero", "Dolor lumbar"]),
             ("Alprostadilo", ["Intracavernoso", "Priapismo, dolor"]),
             ("Testosterona", ["Solo si hay hipogonadismo"]),
             ("Yohimbina", ["Alfa-2 bloqueante", "Ansiedad, taquicardia"])],
   "ruta": ["Tratamiento para disfunción eréctil", "Visión azulada transitoria", "Inhibición de PDE6 retiniana", "SILDENAFILO"]},
  ["Contraindicado con nitratos: hipotensión grave.",
   "Neuropatía óptica isquémica anterior no arterítica: efecto raro y grave.",
   "Precaución con alfabloqueadores."],
  "Goodman & Gilman's The Pharmacological Basis of Therapeutics 14.ª ed. (2023) · AUA – Erectile dysfunction guideline (2018)")

# GIN-091 · árbol
A("GIN-091", "32-semanas-contracciones-cervix-35-fibronectina-negativa", "Contracciones antes de término",
  "OBSTETRICIA ENAM: FALSO TRABAJO DE PARTO PRETÉRMINO", "OBSTETRICIA",
  ("Contracciones pretérmino", ["La cervicometría y la fibronectina fetal definen el riesgo real",
   "Cérvix ≥ 30 mm y fibronectina negativa = riesgo muy bajo de parto en 7 días"]),
  ("Primigesta de 32 semanas", ["2 contracciones en 20 minutos", "Cérvix 35 mm · fibronectina fetal negativa"]),
  Q("¿Cérvix < 25 mm o fibronectina positiva?", [
      L("No: cérvix ≥ 30, FFN −", "MANEJO EXPECTANTE", ["Falso trabajo de parto", "Alta con signos de alarma"], path=True),
      L("Sí", "Amenaza de parto pretérmino", ["Corticoides + tocólisis", "Sulfato de Mg si < 32 sem"])], path=True),
  ("Contracciones pretérmino", [("Falso trabajo de parto", True), ("Amenaza real", False)], [
      ("Cérvix", ["≥ 30 mm", "< 25 mm o cambios"]),
      ("Fibronectina", ["Negativa", "Positiva"]),
      ("Conducta", ["Observar y alta", "Corticoides, tocólisis"])]),
  ["La tocólisis sin cambios cervicales no está indicada.",
   "El valor de la fibronectina está en su alto valor predictivo negativo.",
   "Descartar infección urinaria como causa de contracciones."],
  "ACOG – Practice Bulletin N.° 171: Management of preterm labor (2016, reafirmado) · " + WILLIAMS)

# INF-045 · matriz
V("matriz", "INF-045", "esquema-1-vision-colores-verde-etambutol", "Efectos adversos de los antituberculosos",
  "INFECTOLOGÍA ENAM: TOXICIDAD DEL ETAMBUTOL", "INFECTOLOGÍA",
  ("Reacciones adversas a fármacos antituberculosos", ["Cada fármaco tiene un efecto adverso típico",
   "Pérdida de agudeza visual y del color verde-rojo = neuritis óptica por etambutol"]),
  ("Paciente con TB pulmonar en esquema 1", ["Al mes: baja agudeza visual", "No distingue el color verde"]),
  {"rotulo": "Fármaco y efecto adverso", "eje_x": "Aspecto", "eje_y": "Fármaco",
   "cols": ["Efecto típico", "Manejo"], "rows": ["Etambutol", "Isoniacida", "Rifampicina", "Pirazinamida"], "caso": (0, 0),
   "cells": [[("NEURITIS ÓPTICA", ["Discromatopsia verde-rojo"]), ("Suspender", ["Evaluar agudeza visual"])],
             [("Neuropatía periférica", ["Hepatitis"]), ("Piridoxina", [])],
             [("Orina naranja", ["Interacciones, hepatitis"]), ("Avisar al paciente", [])],
             [("Hiperuricemia", ["Artralgias, hepatitis"]), ("AINE, vigilar", [])]]},
  ["El etambutol se ajusta en insuficiencia renal.",
   "En niños pequeños la agudeza visual es difícil de evaluar.",
   "La hepatotoxicidad la causan isoniacida, rifampicina y pirazinamida."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · OMS – Consolidated guidelines on tuberculosis, Module 4: Treatment (2022)")

# CAR-038 · tarjetas
V("tarjetas", "CAR-038", "pulso-salton-soplo-diastolico-austin-flint", "Soplos valvulares",
  "CARDIOLOGÍA ENAM: INSUFICIENCIA AÓRTICA", "CARDIOLOGÍA",
  ("Insuficiencia aórtica", ["Soplo diastólico decreciente en borde esternal izquierdo + pulso saltón",
   "Austin Flint: soplo mesodiastólico mitral por el chorro regurgitante"]),
  ("Varón de 60 años con disnea y palpitaciones", ["Pulso saltón · soplo protodiastólico decreciente", "Soplo de Austin Flint en foco mitral"]),
  {"rotulo": "¿Qué valvulopatía?", "ans": 0, "cards": [
      {"titulo": "INSUFICIENCIA AÓRTICA", "datos": [
          ("Soplo", "Diastólico decreciente", True), ("Foco", "Borde esternal izquierdo", True),
          ("Pulso", "Saltón (Corrigan)", True), ("Signo", "Austin Flint", True)],
       "pie": "Presión diferencial amplia"},
      {"titulo": "Estenosis aórtica", "datos": [
          ("Soplo", "Sistólico eyectivo", False), ("Foco", "Aórtico → carótidas", False),
          ("Pulso", "Parvus et tardus", False), ("Signo", "Angina, síncope, disnea", False)],
       "pie": "Anciano"},
      {"titulo": "Insuficiencia mitral", "datos": [
          ("Soplo", "Holosistólico", False), ("Foco", "Ápex → axila", False),
          ("Pulso", "Normal", False), ("Signo", "Tercer ruido", False)],
       "pie": "Dilatación del VI"},
      {"titulo": "Estenosis mitral", "datos": [
          ("Soplo", "Diastólico con chasquido", False), ("Foco", "Ápex", False),
          ("Pulso", "Normal o FA", False), ("Signo", "Fiebre reumática", False)],
       "pie": "Retumbo diastólico"}]},
  ["El Austin Flint se diferencia de la estenosis mitral porque no tiene chasquido.",
   "Cirugía si hay síntomas o disfunción del VI (FE ≤ 55%).",
   "Causas: válvula bicúspide, dilatación de la raíz aórtica, fiebre reumática."],
  "ESC/EACTS – Guidelines for the management of valvular heart disease (2025)")

# PED-104 · embudo
V("embudo", "PED-104", "rn-20-dias-acolia-bilirrubina-directa-atresia", "Ictericia colestásica neonatal",
  "PEDIATRÍA ENAM: ATRESIA DE VÍAS BILIARES", "PEDIATRÍA",
  ("Colestasis neonatal", ["Ictericia después de 2 semanas con bilirrubina directa alta",
   "Heces acólicas persistentes en un niño que crece bien = atresia de vías biliares"]),
  ("RN de 20 días con ictericia", ["Heces blanquecinas y orina oscura", "BT 12 · BD 8.1 · buen peso"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "RN de 20 días con ictericia",
   "candidatos": ["Atresia biliar", "Ictericia por leche", "Hemólisis", "Hepatitis neonatal", "Hipotiroidismo"],
   "pasos": [("Bilirrubina directa alta: colestasis", ["Ictericia por leche", "Hemólisis"]),
             ("Acolia persistente, buen estado y ganancia de peso", ["Hepatitis neonatal", "Hipotiroidismo"])],
   "final": ("ATRESIA DE VÍAS BILIARES", ["Ecografía: signo del cordón triangular", "Portoenterostomía de Kasai < 60 días"]),
   "nota": "Bilirrubina directa > 1 mg/dL en un RN siempre es patológica: estudiar ya."},
  ["Cuanto antes el Kasai, mejor pronóstico.",
   "Causa más frecuente de trasplante hepático pediátrico.",
   "Tarjeta de color de heces para detección precoz."],
  "NASPGHAN/ESPGHAN – Guideline for the evaluation of cholestatic jaundice in infants (J Pediatr Gastroenterol Nutr 2017) · " + NELSON)

# GIN-092 · radial
V("radial", "GIN-092", "pinard-miometrio-hemostasia-posparto", "Hemostasia del lecho placentario",
  "OBSTETRICIA ENAM: LIGADURAS VIVIENTES DE PINARD", "OBSTETRICIA",
  ("Hemostasia tras el alumbramiento", ["Las fibras miometriales entrecruzadas comprimen los vasos al contraerse",
   "Son las ligaduras vivientes de Pinard"]),
  ("Pregunta de concepto", ["Función principal de las ligaduras de Pinard", "en el útero gestante"]),
  {"rotulo": "Mapa del tema", "centro": "HEMOSTASIA POSPARTO", "centro_sub": "Cómo se detiene el sangrado", "ans": 0,
   "items": [("LIGADURAS DE PINARD", ["Fibras que comprimen vasos", "Controlan el sangrado"]),
             ("Globo de seguridad", ["Útero contraído bajo el ombligo"]),
             ("Trombosis del lecho", ["Coagulación local"]),
             ("Oxitocina", ["Mantiene la contracción"]),
             ("Retracción uterina", ["Reduce el tamaño"])],
   "ruta": ["Sale la placenta", "El miometrio se contrae", "Las fibras cierran los vasos", "LIGADURAS DE PINARD"]},
  ["Si el útero no se contrae (atonía), las ligaduras no funcionan.",
   "Por eso el masaje y los uterotónicos son la base del manejo.",
   "La atonía causa cerca del 70% de las hemorragias posparto."],
  WILLIAMS + " · OMS – Recommendations for the prevention and treatment of postpartum haemorrhage (2023)")

# INF-046 · árbol
A("INF-046", "rodilla-diplococos-gramnegativos-artritis-gonococica", "Artritis séptica según el Gram",
  "INFECTOLOGÍA ENAM: ARTRITIS GONOCÓCICA", "INFECTOLOGÍA",
  ("Artritis séptica", ["El Gram del líquido sinovial orienta el antibiótico",
   "Diplococos gramnegativos en adulto joven sexualmente activo = gonococo"]),
  ("Varón de 25 años, soltero", ["4 días de rodilla dolorosa, eritematosa e inflamada", "Frotis: diplococos gramnegativos"]),
  Q("¿Qué muestra el Gram del líquido?", [
      L("Cocos gram (+)", "S. aureus", ["Oxacilina o vancomicina", "+ lavado articular"]),
      L("Diplococos gram (−)", "GONOCOCO", ["CEFTRIAXONA EV", "+ tratar clamidia"], path=True),
      L("Negativo", "Empírico", ["Vancomicina + ceftriaxona"])], path=True),
  ("Artritis séptica", [("Gonocócica", True), ("No gonocócica", False)], [
      ("Paciente", ["Joven sexualmente activo", "Niño, anciano, prótesis"]),
      ("Clínica", ["Poliartralgia, tenosinovitis, pústulas", "Monoartritis grave"]),
      ("Tratamiento", ["Ceftriaxona 1 g/día", "Antibiótico + drenaje"])]),
  ["Cultivo del líquido sinovial a menudo negativo en el gonococo: cultivar uretra, cérvix, faringe.",
   "La penicilina ya no es de elección por resistencias.",
   "Estudiar VIH y sífilis."],
  "CDC – Sexually Transmitted Infections Treatment Guidelines (2021)")

# INF-047 · tarjetas
V("tarjetas", "INF-047", "vih-cd4-bajo-nodulos-violaceos-kaposi", "Lesiones violáceas en VIH",
  "INFECTOLOGÍA ENAM: SARCOMA DE KAPOSI", "INFECTOLOGÍA",
  ("Sarcoma de Kaposi", ["Tumor vascular asociado al herpesvirus 8 (HHV-8)",
   "Nódulos rojo-violáceos que no palidecen, en piel y mucosa oral"]),
  ("Varón de 28 años con VIH, TAR irregular, CD4 < 200", ["3 meses de nódulos rojo vinosos", "Tórax, piernas y boca"]),
  {"rotulo": "¿Qué lesión es?", "ans": 0, "cards": [
      {"titulo": "SARCOMA DE KAPOSI", "datos": [
          ("Agente", "HHV-8", True), ("Lesión", "Nódulos violáceos", True),
          ("Palidece", "No", True), ("Tratamiento", "TAR ± quimioterapia", False)],
       "pie": "Puede afectar pulmón y tubo digestivo"},
      {"titulo": "Angiomatosis bacilar", "datos": [
          ("Agente", "Bartonella", False), ("Lesión", "Pápulas vasculares", False),
          ("Palidece", "Sí, sangra", False), ("Tratamiento", "Azitromicina", False)],
       "pie": "Fiebre"},
      {"titulo": "Molusco contagioso", "datos": [
          ("Agente", "Poxvirus", False), ("Lesión", "Pápulas umbilicadas", False),
          ("Palidece", "Color piel", False), ("Tratamiento", "Curetaje", False)],
       "pie": "Perlado"},
      {"titulo": "Foliculitis eosinofílica", "datos": [
          ("Agente", "Inflamatoria", False), ("Lesión", "Pápulas pruriginosas", False),
          ("Palidece", "Eritematosa", False), ("Tratamiento", "Corticoide tópico", False)],
       "pie": "CD4 < 250"}]},
  ["Es una enfermedad definitoria de sida.",
   "Mejora con el TAR (reconstitución inmune).",
   "La biopsia confirma: proliferación de células fusiformes."],
  "NIH/CDC/IDSA – Guidelines for the prevention and treatment of opportunistic infections in adults with HIV (2024)")

# CB-031 · matriz
V("matriz", "CB-031", "automedicacion-covid-qt-largo-azitromicina", "Fármacos usados en COVID-19 y sus riesgos",
  "CIENCIAS BÁSICAS ENAM: PROLONGACIÓN DEL QT POR AZITROMICINA", "CIENCIAS BÁSICAS",
  ("Fármacos que prolongan el QT", ["Macrólidos, hidroxicloroquina, quinolonas, antipsicóticos",
   "QT largo puede degenerar en torsade de pointes"]),
  ("Varón de 72 años automedicado por COVID-19", ["Mareos y dolor precordial", "ECG: QT largo, taquicardia ventricular"]),
  {"rotulo": "Fármaco y riesgo", "eje_x": "Aspecto", "eje_y": "Fármaco",
   "cols": ["Efecto adverso clave", "Riesgo arrítmico"], "rows": ["Azitromicina", "Ivermectina", "Dexametasona", "Paracetamol"], "caso": (0, 1),
   "cells": [[("Prolonga el QT", []), ("ALTO", ["Torsade de pointes"])],
             [("Neurotoxicidad", ["Dosis altas"]), ("Bajo", [])],
             [("Hiperglucemia", ["Infecciones"]), ("Bajo", [])],
             [("Hepatotoxicidad", ["Sobredosis"]), ("Bajo", [])]]},
  ["Tratamiento de torsade: sulfato de magnesio EV; desfibrilar si es inestable.",
   "Suspender todos los fármacos que prolonguen el QT; corregir K y Mg.",
   "Riesgo mayor en ancianos, mujeres y con hipokalemia."],
  "AHA – Drug-induced arrhythmias scientific statement (Circulation 2020) · CredibleMeds – QTdrugs list (2025)")

# NEU-027 · tarjetas
V("tarjetas", "NEU-027", "asbesto-30-anos-panal-cuerpos-ferruginosos", "Neumoconiosis",
  "NEUMOLOGÍA ENAM: ASBESTOSIS", "NEUMOLOGÍA",
  ("Asbestosis", ["Fibrosis de bases pulmonares y placas pleurales tras años de exposición",
   "La biopsia muestra cuerpos ferruginosos (fibras recubiertas de hierro)"]),
  ("Varón de 76 años, 30 años expuesto a asbesto", ["Disnea progresiva de 4 años", "Engrosamiento pleural · patrón en panal de abeja"]),
  {"rotulo": "¿Qué neumoconiosis?", "ans": 0, "cards": [
      {"titulo": "ASBESTOSIS", "datos": [
          ("Exposición", "Construcción, frenos", True), ("Rx", "Bases, placas pleurales", True),
          ("Biopsia", "Cuerpos ferruginosos", True)],
       "pie": "Mesotelioma y cáncer de pulmón"},
      {"titulo": "Silicosis", "datos": [
          ("Exposición", "Minería, canteras", False), ("Rx", "Lóbulos superiores, nódulos", False),
          ("Biopsia", "Nódulos silicóticos", False)],
       "pie": "Riesgo de tuberculosis"},
      {"titulo": "Neumoconiosis del carbón", "datos": [
          ("Exposición", "Minas de carbón", False), ("Rx", "Nódulos superiores", False),
          ("Biopsia", "Máculas de carbón", False)],
       "pie": "Síndrome de Caplan con AR"},
      {"titulo": "Beriliosis", "datos": [
          ("Exposición", "Aeroespacial, electrónica", False), ("Rx", "Adenopatías hiliares", False),
          ("Biopsia", "Granulomas", False)],
       "pie": "Simula sarcoidosis"}]},
  ["El tabaco multiplica el riesgo de cáncer de pulmón en expuestos al asbesto.",
   "Las placas pleurales calcificadas son marcador de exposición.",
   "El mesotelioma aparece 20-40 años después."],
  "ATS – Diagnosis of nonmalignant diseases related to asbestos (Am J Respir Crit Care Med 2004) · Murray & Nadel's Textbook of Respiratory Medicine 7.ª ed. (2022)")

# NEF-037 · termómetro
V("termometro", "NEF-037", "diabetico-albuminuria-1g-ieca", "Albuminuria en la diabetes",
  "NEFROLOGÍA ENAM: NEFROPATÍA DIABÉTICA", "NEFROLOGÍA",
  ("Enfermedad renal diabética", ["La albuminuria marca el daño y el riesgo de progresión",
   "IECA o ARA II a dosis máxima tolerada reducen la proteinuria"]),
  ("Varón de 58 años diabético", ["PA 140/90, edema · depuración 45 mL/min", "Albuminuria 1 g/24 h · K 4.5"]),
  {"rotulo": "Albuminuria (mg/24 h)",
   "niveles": [("< 30", "A1", ["Normal"]),
               ("30-300", "A2", ["Moderadamente aumentada"]),
               ("> 300", "A3", ["MUY AUMENTADA", "Riesgo alto de progresión"])],
   "caso_nivel": 2, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "IECA o ARA II", ["Dosis máxima tolerada; controlar K y creatinina"], True),
             (2, "Inhibidor de SGLT2", ["Si TFG ≥ 20 mL/min"], False),
             (3, "Finerenona", ["Si persiste la albuminuria"], False)]},
  ["No combinar IECA y ARA II: más hiperkalemia y falla renal.",
   "Meta de PA < 130/80 mmHg.",
   "Las estatinas reducen el riesgo cardiovascular, no la proteinuria."],
  "KDIGO – Clinical practice guideline for diabetes management in CKD (Kidney Int 2022) · ADA – Standards of Care in Diabetes (2025)")

# SP-063 · radial
V("radial", "SP-063", "lactancia-exclusiva-comunicacion-educativa-habilidades", "Carta de Ottawa",
  "SALUD PÚBLICA ENAM: DESARROLLO DE HABILIDADES PERSONALES", "SALUD PÚBLICA",
  ("Carta de Ottawa (1986)", ["Cinco áreas de acción de la promoción de la salud",
   "Educar para que las personas tomen mejores decisiones = habilidades personales"]),
  ("Distrito con lactancia materna exclusiva < 50%", ["Plan de comunicación educativa", "Dirigido a las gestantes"]),
  {"rotulo": "Mapa del tema", "centro": "CARTA DE OTTAWA", "centro_sub": "Áreas de acción", "ans": 0,
   "items": [("HABILIDADES PERSONALES", ["Educación e información", "Decidir mejor"]),
             ("Políticas públicas", ["Leyes saludables"]),
             ("Entornos favorables", ["Espacios que protegen"]),
             ("Acción comunitaria", ["Participación de la comunidad"]),
             ("Reorientar servicios", ["Más allá de curar"])],
   "ruta": ["Lactancia exclusiva baja", "Comunicación educativa", "A las gestantes", "HABILIDADES PERSONALES"]},
  ["Ejemplo de entorno favorable: lactarios en los centros de trabajo.",
   "Ejemplo de política pública: licencia por maternidad.",
   "La Carta de Ottawa define la promoción como capacitar a la gente para controlar su salud."],
  "OMS – Carta de Ottawa para la Promoción de la Salud (1986)")

# INF-048 · embudo
V("embudo", "INF-048", "diarrea-agua-de-arroz-calambres-colera", "Diarrea acuosa profusa",
  "INFECTOLOGÍA ENAM: CÓLERA", "INFECTOLOGÍA",
  ("Cólera", ["Diarrea acuosa masiva en «agua de arroz», sin fiebre ni sangre",
   "La toxina colérica activa la adenilato ciclasa: secreción de agua y cloro"]),
  ("Varón de 18 años con 24 h de vómitos y diarrea", ["Heces en agua de arroz, calambres y oliguria", "Reacción inflamatoria en heces negativa"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Diarrea acuosa con deshidratación",
   "candidatos": ["Vibrio cholerae", "E. coli", "Rotavirus", "Shigella", "Amebiasis"],
   "pasos": [("Sin sangre ni leucocitos en heces", ["Shigella", "Amebiasis"]),
             ("Adulto con «agua de arroz» y deshidratación rápida", ["E. coli", "Rotavirus"])],
   "final": ("VIBRIO CHOLERAE", ["Rehidratación: SRO o Ringer lactato", "Doxiciclina o azitromicina"]),
   "nota": "La rehidratación salva la vida; el antibiótico solo acorta la diarrea."},
  ["Notificación inmediata: enfermedad de vigilancia internacional.",
   "Coprocultivo en TCBS o prueba rápida.",
   "Perú tuvo una gran epidemia en 1991."],
  "OMS – Cholera: clinical management (2024) · MINSA – Vigilancia epidemiológica del cólera")

# SP-064 · matriz
V("matriz", "SP-064", "encuesta-escolares-embarazo-estudio-transversal", "Diseños de estudio",
  "SALUD PÚBLICA ENAM: ESTUDIO TRANSVERSAL", "SALUD PÚBLICA",
  ("Diseños de investigación", ["Una encuesta en un solo momento mide exposición y efecto a la vez",
   "Eso es un estudio transversal (de prevalencia)"]),
  ("Colegio con abandono escolar por embarazo", ["Encuesta a todos los alumnos", "Características y conocimientos en salud sexual"]),
  {"rotulo": "Tipos de estudio", "eje_x": "Aspecto", "eje_y": "Diseño",
   "cols": ["Tiempo", "Qué mide"], "rows": ["Transversal", "Casos y controles", "Cohorte", "Ensayo clínico"], "caso": (0, 0),
   "cells": [[("UN SOLO MOMENTO", ["Encuesta"]), ("Prevalencia", [])],
             [("Hacia atrás", []), ("Odds ratio", [])],
             [("Hacia adelante", []), ("Incidencia, riesgo relativo", [])],
             [("Hacia adelante", ["Intervención asignada"]), ("Eficacia", [])]]},
  ["El transversal no establece causalidad (no sabe qué vino primero).",
   "Es rápido y barato: útil para diagnósticos situacionales.",
   "En el ensayo clínico el investigador asigna la exposición."],
  "Gordis Epidemiology 6.ª ed. (2019) · OPS – MOPECE 2.ª ed.")

# OFT-023 · tarjetas
V("tarjetas", "OFT-023", "glaucoma-mas-frecuente-angulo-abierto", "Tipos de glaucoma",
  "OFTALMOLOGÍA ENAM: GLAUCOMA PRIMARIO DE ÁNGULO ABIERTO", "OFTALMOLOGÍA",
  ("Glaucoma", ["Neuropatía óptica progresiva con pérdida del campo visual",
   "La forma más frecuente es el primario de ángulo abierto (asintomático)"]),
  ("Pregunta de concepto", ["¿Cuál es la forma de glaucoma más frecuente?"]),
  {"rotulo": "¿Qué glaucoma?", "ans": 0, "cards": [
      {"titulo": "PRIMARIO DE ÁNGULO ABIERTO", "datos": [
          ("Frecuencia", "70-90%", True), ("Síntomas", "Ninguno al inicio", True),
          ("Tratamiento", "Colirios, láser", False)],
       "pie": "Tamizaje > 40 años"},
      {"titulo": "Ángulo cerrado agudo", "datos": [
          ("Frecuencia", "Menos frecuente", False), ("Síntomas", "Dolor, halos, vómitos", False),
          ("Tratamiento", "Acetazolamida, iridotomía", False)],
       "pie": "Urgencia"},
      {"titulo": "Congénito", "datos": [
          ("Frecuencia", "Raro", False), ("Síntomas", "Ojos grandes, lagrimeo", False),
          ("Tratamiento", "Goniotomía", False)],
       "pie": "Buftalmos"},
      {"titulo": "Secundario", "datos": [
          ("Frecuencia", "Variable", False), ("Síntomas", "Según la causa", False),
          ("Tratamiento", "Tratar la causa", False)],
       "pie": "Corticoides, uveítis, trauma"}]},
  ["Factores de riesgo: PIO alta, edad, raza negra, antecedente familiar, miopía.",
   "La pérdida visual empieza por la periferia y es irreversible.",
   "Primera línea: análogos de prostaglandinas o betabloqueadores tópicos."],
  "AAO – Primary open-angle glaucoma Preferred Practice Pattern (2020) · EGS – Terminology and guidelines for glaucoma 5.ª ed. (2021)")
