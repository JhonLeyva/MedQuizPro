"""Bloque 7 · parte H."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"

# CIR-103 · termómetro
V("termometro", "CIR-103", "varices-pesadez-vespertina-perthes-terapia-compresiva", "Insuficiencia venosa crónica",
  "CIRUGÍA ENAM: INSUFICIENCIA VENOSA CRÓNICA", "CIRUGÍA",
  ("Insuficiencia venosa crónica", ["Pesadez, prurito y dolor que empeoran de pie y al final del día",
   "Base del tratamiento: medias de compresión graduada"]),
  ("Mujer de 65 años con 5 meses de síntomas", ["Pesadez, prurito y ardor que le impiden caminar", "Várices en la cara interna de ambas piernas · Perthes (+)"]),
  {"rotulo": "Clasificación CEAP (clínica)",
   "niveles": [("C1", "Telangiectasias", ["Arañas vasculares"]),
               ("C2", "Várices", ["VÁRICES SINTOMÁTICAS", "Pesadez y ardor"]),
               ("C3-C4", "Edema, cambios de piel", ["Pigmentación, eccema"]),
               ("C5-C6", "Úlcera", ["Cicatrizada o activa"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Terapia compresiva", ["Medias de 20-30 mmHg", "Elevar piernas, caminar"], True),
             (2, "Flebotónicos", ["Alivian síntomas"], False),
             (3, "Ablación o cirugía", ["Si persisten síntomas o hay complicaciones"], False)]},
  ["La prueba de Perthes evalúa si el sistema venoso profundo está permeable.",
   "La escleroterapia se usa en telangiectasias y várices pequeñas.",
   "La fibrinólisis es para trombosis aguda, no para várices."],
  "ESVS – Clinical practice guidelines on the management of chronic venous disease (2022)")

# GIN-187 · fases
V("fases", "GIN-187", "lupus-preconcepcional-seis-meses-inactivo", "Lupus: ¿cuándo embarazarse?",
  "OBSTETRICIA ENAM: LUPUS Y EMBARAZO", "OBSTETRICIA",
  ("Consulta preconcepcional en el LES", ["El embarazo con lupus activo aumenta brotes, preeclampsia y pérdidas",
   "Se recomienda al menos 6 meses de enfermedad inactiva antes de gestar"]),
  ("Paciente con LES en tratamiento", ["Sin complicaciones sistémicas", "Desea embarazarse"]),
  {"rotulo": "Plan preconcepcional", "ans": 2,
   "fases": [("Activa", "Brote", "Controlar", ["Anticoncepción eficaz"]),
             ("Ajustar", "Fármacos", "Cambiar teratógenos", ["Micofenolato → azatioprina", "Seguir hidroxicloroquina"]),
             ("Inactiva", "≥ 6 meses", "YA PUEDE GESTAR", ["Menos brotes y pérdidas"]),
             ("Embarazo", "Control", "Alto riesgo", ["Aspirina desde 12 semanas"])],
   "curvas": [("Actividad del lupus", ROSE, [0.9, 0.7, 0.4, 0.2, 0.15, 0.15, 0.2])],
   "chips_titulo": "Recomendación · marcada la correcta",
   "chips": [("6 meses de enfermedad inactiva", True), ("Suspender hidroxicloroquina", False), ("Subir corticoides", False), ("No embarazarse", False)]},
  ["Suspender la hidroxicloroquina aumenta el riesgo de brote.",
   "Medir anti-Ro/La (bloqueo cardiaco fetal) y antifosfolípidos.",
   "Nefritis activa: el embarazo debe postergarse."],
  "EULAR – Recommendations for women's health and family planning in SLE/APS (2017) · ACR – Reproductive health guideline (2020)")

# SP-137 · termómetro
V("termometro", "SP-137", "riesgo-relativo-igual-a-uno-sin-asociacion", "Cómo leer el riesgo relativo",
  "SALUD PÚBLICA ENAM: RIESGO RELATIVO", "SALUD PÚBLICA",
  ("Riesgo relativo", ["RR = incidencia en expuestos / incidencia en no expuestos",
   "RR = 1: igual riesgo en ambos grupos → no hay asociación"]),
  ("Estudio de una enfermedad", ["El riesgo relativo resultó igual a 1"]),
  {"rotulo": "Valor del RR",
   "niveles": [("< 1", "Protector", ["Menos riesgo en expuestos"]),
               ("= 1", "Sin asociación", ["RR = 1", "El factor no cambia el riesgo"]),
               ("> 1", "Factor de riesgo", ["Más riesgo en expuestos"])],
   "caso_nivel": 1, "ruta_titulo": "Interpretación", "paso_label": "PASO",
   "pasos": [(1, "Ausencia de asociación", ["Expuestos y no expuestos enferman igual"], True),
             (2, "Revisar el IC 95 %", ["Si incluye el 1: no significativo"], False),
             (3, "Buscar sesgos o confusión", ["Pueden ocultar una asociación"], False)]},
  ["El RR se obtiene de estudios de cohorte.",
   "En casos y controles se usa el odds ratio, con la misma lectura.",
   "RR = 2: los expuestos tienen el doble de riesgo."],
  GORDIS)

# END-054 · puntaje
V("puntaje", "END-054", "posoperada-estupor-hipotermia-cicatriz-cuello-coma-mixedematoso", "Estupor e hipotermia tras la cirugía",
  "ENDOCRINOLOGÍA ENAM: COMA MIXEDEMATOSO", "ENDOCRINOLOGÍA",
  ("Coma mixedematoso", ["Hipotiroidismo grave descompensado por un estrés (cirugía, infección, frío)",
   "Hipotermia, estupor, hipoventilación e hiponatremia"]),
  ("Mujer de 76 años operada de abdomen agudo", ["Sigue estuporosa · ventilación mecánica por hipercapnia", "Cicatriz en la base del cuello · T 32 °C · Na 127"]),
  {"rotulo": "Puntaje de Popoveniuc", "escala": "Coma mixedematoso", "total": 65, "max": 130,
   "total_label": "Puntaje del caso",
   "interpreta": "≥ 60: muy sugestivo",
   "items": [("SNC: estupor", "25", True), ("Temperatura 32-35 °C", "10", True),
             ("Evento precipitante (cirugía)", "10", True), ("Hiponatremia", "10", True),
             ("Hipercapnia", "10", True), ("Bradicardia", "10-30", False)],
   "bandas": [("< 25", "Improbable", "Buscar otra causa", False),
              ("25-59", "Sugestivo", "Tratar si la clínica apoya", False),
              ("≥ 60", "Muy sugestivo", "Levotiroxina EV + hidrocortisona", True)]},
  ["Dar hidrocortisona antes que la levotiroxina: puede haber insuficiencia suprarrenal.",
   "Recalentar de forma pasiva; soporte ventilatorio.",
   "La cicatriz cervical sugiere tiroidectomía previa sin reemplazo adecuado."],
  "Popoveniuc G et al. (Endocr Pract 2014) · ATA – Guidelines for the treatment of hypothyroidism (2014)")

# PED-183 · embudo
V("embudo", "PED-183", "nino-3-anos-heces-jalea-masa-hipocondrio-enema", "Dolor cólico con heces en jalea",
  "PEDIATRÍA ENAM: INVAGINACIÓN INTESTINAL", "PEDIATRÍA",
  ("Invaginación intestinal", ["Un segmento se mete en el siguiente (ileocólica)",
   "Dolor cólico intermitente, vómitos, masa y heces en 'jalea de grosella'"]),
  ("Niño de 3 años tras un resfrío", ["Dolor abdominal y vómitos intermitentes · heces tipo gelatina rosada", "Masa dolorosa en cuadrante superior derecho · sin peritonitis"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dolor cólico con sangre en heces",
   "candidatos": ["Invaginación", "Gastroenteritis", "Divertículo de Meckel", "Apendicitis"],
   "pasos": [("Masa palpable en salchicha y sin aire en colon izquierdo", ["Gastroenteritis", "Apendicitis"]),
             ("Dolor intermitente con vómitos tras virosis", ["Divertículo de Meckel"])],
   "final": ("INVAGINACIÓN INTESTINAL", ["Enema con aire o contraste", "Diagnostica y reduce a la vez"]),
   "nota": "La ecografía (imagen en diana) es hoy el estudio inicial preferido; el enema confirma y trata."},
  ["El enema está contraindicado si hay peritonitis o perforación.",
   "Tras una virosis, la hiperplasia de placas de Peyer actúa como cabeza.",
   "Recurrencia en ~10 % de los casos."],
  "ESPR – Guidelines for imaging and reduction of intussusception (2016) · " + NELSON)

# CB-072 · embudo
V("embudo", "CB-072", "bebedor-vision-borrosa-anion-gap-alto-metanol", "Acidosis con visión borrosa",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR METANOL", "CIENCIAS BÁSICAS",
  ("Intoxicación por metanol", ["Alcohol adulterado: el metanol se convierte en ácido fórmico",
   "Acidosis metabólica con anión gap alto + visión borrosa ('ver bultos')"]),
  ("Diabético de 68 años, bebedor habitual", ["Mareos, vómitos, visión borrosa · somnoliento", "FR 35 · PA 90/60 · acidosis con anión gap alto"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Acidosis metabólica con anión gap alto",
   "candidatos": ["Metanol", "Cetoacidosis diabética", "Acidosis por metformina", "Acidosis láctica"],
   "pasos": [("Alteración visual precoz ('ver bultos')", ["Acidosis por metformina", "Acidosis láctica"]),
             ("Bebedor de licor, sin hiperglucemia descrita", ["Cetoacidosis diabética"])],
   "final": ("INTOXICACIÓN POR METANOL", ["Fomepizol o etanol + bicarbonato", "Hemodiálisis si es grave"]),
   "nota": "El ácido fórmico daña la retina y el nervio óptico: puede dejar ceguera."},
  ["Brecha osmolar alta al inicio apoya el diagnóstico.",
   "El etanol compite por la alcohol deshidrogenasa.",
   "Sospechar en brotes por licor adulterado."],
  "AACT – Guidelines on the treatment of methanol poisoning (2002) · Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# CB-073 · tarjetas
V("tarjetas", "CB-073", "limpieza-pozo-septico-desmayo-acido-sulfhidrico", "Gases tóxicos",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR ÁCIDO SULFHÍDRICO", "CIENCIAS BÁSICAS",
  ("Ácido sulfhídrico (H₂S)", ["Se libera por la descomposición de materia orgánica: pozos, desagües",
   "Olor a huevo podrido, irrita ojos y vías aéreas y bloquea la respiración celular"]),
  ("Varón de 25 años limpiando un pozo séptico", ["Hallado desmayado · desorientado, disneico", "Congestión ocular, tos, cianosis leve"]),
  {"rotulo": "¿Qué gas es?", "ans": 0, "cards": [
      {"titulo": "ÁCIDO SULFHÍDRICO", "datos": [
          ("Fuente", "Pozo séptico, desagüe", True), ("Olor", "Huevo podrido", False),
          ("Signo", "Ojos rojos, tos", True), ("Manejo", "Retirar, O₂ 100 %", False)],
       "pie": "Fatiga olfatoria: deja de olerse"},
      {"titulo": "Monóxido de carbono", "datos": [
          ("Fuente", "Combustión, braseros", False), ("Olor", "Inodoro", False),
          ("Signo", "Cefalea, color cereza", False), ("Manejo", "O₂ 100 %, hiperbárica", False)],
       "pie": "Carboxihemoglobina"},
      {"titulo": "Cianuro", "datos": [
          ("Fuente", "Incendios, minería", False), ("Olor", "Almendras amargas", False),
          ("Signo", "Acidosis láctica", False), ("Manejo", "Hidroxocobalamina", False)],
       "pie": "Bloquea citocromo oxidasa"},
      {"titulo": "Ácido fluorhídrico", "datos": [
          ("Fuente", "Industria, vidrio", False), ("Olor", "Irritante", False),
          ("Signo", "Hipocalcemia", False), ("Manejo", "Gluconato de calcio", False)],
       "pie": "Quemaduras profundas"}]},
  ["El rescatista sin protección también puede intoxicarse.",
   "H₂S y cianuro inhiben la citocromo oxidasa.",
   "Vigilar edema pulmonar tardío."],
  "NIOSH – Hydrogen sulfide: emergency response (2024) · Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# PED-184 · matriz
V("matriz", "PED-184", "nefrotico-recae-al-bajar-corticoides-corticodependencia", "Síndrome nefrótico según el curso",
  "PEDIATRÍA ENAM: SÍNDROME NEFRÓTICO CORTICODEPENDIENTE", "PEDIATRÍA",
  ("Síndrome nefrótico idiopático", ["Se clasifica según cómo evoluciona con la prednisona",
   "Corticodependiente: recae mientras se baja la dosis o poco después de suspender"]),
  ("Escolar de 6 años con cambios mínimos", ["Sube la proteinuria mientras se reduce el corticoide"]),
  {"rotulo": "Tipo y definición", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Definición", "Manejo"], "rows": ["Corticodependiente", "Recaída frecuente", "Corticorresistente", "Corticosensible"], "caso": (0, 0),
   "cells": [[("RECAE AL BAJAR LA DOSIS", ["O < 2 sem tras suspender"]), ("Ahorradores de corticoide", ["Levamisol, MMF, rituximab"])],
             [("≥ 2 en 6 meses", ["O ≥ 4 en 1 año"]), ("Similar", [])],
             [("Sin remisión a las 4-6 sem", []), ("Biopsia renal", ["Pensar en GEFS"])],
             [("Remite con prednisona", []), ("Bajar gradual", [])]]},
  ["Los cambios mínimos son la causa más frecuente en niños de 2 a 8 años.",
   "La recaída se define con proteinuria ≥ 3+ en tira por 3 días.",
   "Vigilar efectos del corticoide: talla, presión, ojos."],
  "KDIGO – Clinical practice guideline for glomerular diseases (2021) · IPNA – Recommendations for steroid-sensitive nephrotic syndrome (2023)")

# PED-185 · radial
V("radial", "PED-185", "fracturas-repeticion-escleras-azules-osteogenesis-imperfecta", "Fracturas a repetición en el niño",
  "PEDIATRÍA ENAM: OSTEOGÉNESIS IMPERFECTA", "PEDIATRÍA",
  ("Osteogénesis imperfecta", ["Defecto del colágeno tipo I: huesos frágiles",
   "Escleróticas azules, fracturas repetidas, huesos arqueados, sordera"]),
  ("Niño de 3 años referido", ["Fracturas a repetición · escleróticas azules", "Huesos largos cortos y arqueados · Rx con hipomineralización"]),
  {"rotulo": "Mapa del tema", "centro": "TEJIDO CONECTIVO", "centro_sub": "¿Qué enfermedad?", "ans": 0,
   "items": [("OSTEOGÉNESIS IMPERFECTA", ["Colágeno tipo I", "Escleras azules, fracturas"]),
             ("Ehlers-Danlos", ["Piel elástica, articulaciones laxas"]),
             ("Marfan", ["Alto, aracnodactilia, aorta"]),
             ("Artrogriposis", ["Contracturas congénitas"]),
             ("Maltrato infantil", ["Descartar siempre"])],
   "ruta": ["Fracturas repetidas", "Escleras azules", "Huesos arqueados", "OSTEOGÉNESIS IMPERFECTA"]},
  ["Tratamiento: bisfosfonatos, fisioterapia y cirugía ortopédica.",
   "Herencia autosómica dominante en la mayoría (COL1A1, COL1A2).",
   "Ante fracturas múltiples en un niño, descartar maltrato."],
  NELSON + " · Marom R et al. (Am J Med Genet 2016)")

# GIN-188 · fases
V("fases", "GIN-188", "hijo-down-translucencia-nucal-11-14-semanas", "Tamizaje prenatal por edad gestacional",
  "OBSTETRICIA ENAM: TRANSLUCENCIA NUCAL", "OBSTETRICIA",
  ("Tamizaje de aneuploidías", ["La translucencia nucal se mide entre las semanas 11 y 13+6",
   "Combinada con β-hCG libre y PAPP-A detecta ~90 % de trisomía 21"]),
  ("Segundigesta de 8 semanas", ["Tiene un hijo con síndrome de Down", "Quiere una ecografía para descartarlo"]),
  {"rotulo": "Estudios según las semanas", "ans": 1,
   "fases": [("7-10 sem", "Datación", "Longitud craneocaudal", ["Edad gestacional exacta"]),
             ("11-14 sem", "Tamizaje", "TRANSLUCENCIA NUCAL", ["+ hueso nasal, ductus venoso", "+ β-hCG y PAPP-A"]),
             ("15-20 sem", "Bioquímico", "Triple o cuádruple", ["Si no hubo 1.er trimestre"]),
             ("20-24 sem", "Morfológica", "Anatomía fetal", ["Malformaciones"])],
   "curvas": [],
   "chips_titulo": "Semanas ideales · marcadas las correctas",
   "chips": [("11 a 14", True), ("7 a 10", False), ("15 a 18", False), ("22 a 25", False)]},
  ["Con hijo previo con Down: ofrecer ADN fetal libre o prueba diagnóstica.",
   "Diagnóstico definitivo: biopsia de vellosidades (11-14 sem) o amniocentesis (≥ 15 sem).",
   "TN aumentada también sugiere cardiopatía congénita."],
  "ISUOG – Practice guidelines: performance of 11-14-week ultrasound scan (2023) · ACOG – Practice Bulletin 226 (2020)")

# REU-056 · embudo
V("embudo", "REU-056", "obeso-joven-monoartritis-rodilla-acido-urico-liquido-sinovial", "Monoartritis aguda con ácido úrico alto",
  "REUMATOLOGÍA ENAM: DIAGNÓSTICO DE GOTA", "REUMATOLOGÍA",
  ("Monoartritis aguda", ["La hiperuricemia no prueba que la artritis sea gota",
   "El diagnóstico se confirma viendo cristales en el líquido sinovial"]),
  ("Varón de 23 años obeso", ["Primer episodio de rodilla muy inflamada y dolorosa", "Ácido úrico 9 mg/dl"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Monoartritis aguda de rodilla",
   "candidatos": ["Gota", "Artritis séptica", "Pseudogota", "Traumática"],
   "pasos": [("Sin trauma previo", ["Traumática"]),
             ("Solo el líquido separa cristales de infección", ["Artritis séptica", "Pseudogota"])],
   "final": ("ESTUDIO DEL LÍQUIDO SINOVIAL", ["Cristales de urato: agujas, birrefringencia negativa", "Gram, cultivo y recuento celular"]),
   "nota": "Durante la crisis el ácido úrico sérico puede incluso estar normal."},
  ["Pseudogota: pirofosfato cálcico, romboides con birrefringencia positiva.",
   "Siempre descartar infección: puede coexistir con gota.",
   "Tratamiento de la crisis: colchicina, AINE o corticoide."],
  "ACR – Guideline for the management of gout (2020) · EULAR – Gout diagnosis recommendations (2018)")

# PED-186 · termómetro
V("termometro", "PED-186", "prematuro-1200-g-distension-neumatosis-enterocolitis", "Enterocolitis necrotizante",
  "PEDIATRÍA ENAM: ENTEROCOLITIS NECROTIZANTE", "PEDIATRÍA",
  ("Enterocolitis necrotizante", ["Necrosis intestinal del prematuro alimentado",
   "Signo radiológico clave: neumatosis intestinal (aire en la pared)"]),
  ("RN de 32 semanas, 1200 g, Apgar 3-6", ["Día 5: intolerancia, residuo lácteo, vómitos, distensión", "Rx: asas dilatadas, pared gruesa, aire intramural"]),
  {"rotulo": "Estadio de Bell",
   "niveles": [("I", "Sospecha", ["Residuo, distensión leve"]),
               ("II", "Confirmada", ["NEUMATOSIS INTESTINAL", "Enterocolitis definida"]),
               ("III", "Avanzada", ["Perforación, choque"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Ayuno, sonda y antibióticos EV", ["7-14 días · ampicilina, gentamicina, metronidazol"], True),
             (2, "Rx seriadas", ["Buscar neumoperitoneo"], False),
             (3, "Cirugía si perfora", ["Laparotomía o drenaje peritoneal"], False)]},
  ["Factores: prematuridad, bajo peso, asfixia, fórmula.",
   "La leche materna es el mejor factor protector.",
   "Gas en la vena porta: signo de gravedad."],
  NELSON + " · Bell MJ (Ann Surg 1978), modificada por Walsh y Kliegman")

# INF-091 · fases
V("fases", "INF-091", "brote-escolar-mayonesa-6-horas-bacillus-cereus", "Intoxicación alimentaria: tiempo de incubación",
  "INFECTOLOGÍA ENAM: TOXIINFECCIÓN ALIMENTARIA", "INFECTOLOGÍA",
  ("Brote de enfermedad transmitida por alimentos", ["El tiempo entre comer y enfermar orienta al agente",
   "Pocas horas = toxina preformada (B. cereus, S. aureus)"]),
  ("40 escolares de 10-11 años", ["6 horas después de ensalada con mayonesa", "Fiebre, vómitos, dolor abdominal, diarrea sin sangre"]),
  {"rotulo": "Horas desde la comida", "ans": 0,
   "fases": [("1-6 h", "Toxina preformada", "B. CEREUS, S. AUREUS", ["Vómitos predominan", "Arroz, mayonesa, cremas"]),
             ("8-16 h", "Toxina en intestino", "C. perfringens", ["Diarrea, cólicos"]),
             ("16-72 h", "Invasivos", "Salmonella, Shigella", ["Fiebre, a veces sangre"]),
             ("1-3 días", "Toxina colérica", "V. cholerae", ["Agua de arroz"])],
   "curvas": [],
   "chips_titulo": "Agente probable · marcado el correcto",
   "chips": [("Bacillus cereus", True), ("Shigella", False), ("Salmonella", False), ("Vibrio cholerae", False)]},
  ["El tratamiento es hidratación; no se usan antibióticos.",
   "Notificar el brote y tomar muestras del alimento.",
   "Salmonella también se asocia a mayonesa casera, pero tarda más de 12 horas."],
  "CDC – Foodborne illness: diagnosis and management (MMWR 2004; actualizado) · OMS – Foodborne disease outbreaks: guidelines (2008)")

# TRA-043 · matriz
V("matriz", "TRA-043", "pavlik-abduccion-excesiva-necrosis-avascular-cabeza-femoral", "Complicaciones del arnés de Pavlik",
  "TRAUMATOLOGÍA ENAM: ARNÉS DE PAVLIK", "TRAUMATOLOGÍA",
  ("Arnés de Pavlik", ["Mantiene la cadera en flexión y abducción moderada",
   "La abducción excesiva comprime los vasos: necrosis avascular de la cabeza femoral"]),
  ("Lactante de 2 meses con Ortolani y Barlow (+)", ["Arnés de Pavlik", "A las 2 semanas: irritable, abducción excesiva"]),
  {"rotulo": "Posición y complicación", "eje_x": "Rasgo", "eje_y": "Posición",
   "cols": ["Complicación", "Prevención"], "rows": ["Abducción forzada", "Hiperflexión", "Flexión insuficiente"], "caso": (0, 0),
   "cells": [[("NECROSIS AVASCULAR", ["De la cabeza femoral"]), ("Abducción < 60°", ["Zona segura"])],
             [("Parálisis del nervio femoral", []), ("Flexión 90-110°", [])],
             [("No reduce la cadera", []), ("Ajustar las correas", [])]]},
  ["Controles semanales con ecografía al inicio.",
   "Si no se reduce en 3-4 semanas: cambiar de estrategia.",
   "La epifisiólisis es de adolescentes; la sinovitis transitoria, de 3-10 años."],
  "AAOS – Detection and nonoperative management of DDH in infants up to 6 months (2014) · " + NELSON)

# SP-138 · árbol
A("SP-138", "cancer-mama-emparejadas-lactancia-casos-controles", "¿Qué diseño es?",
  "SALUD PÚBLICA ENAM: ESTUDIO DE CASOS Y CONTROLES", "SALUD PÚBLICA",
  ("Casos y controles", ["Se parte de la enfermedad y se busca hacia atrás la exposición",
   "Pareado: cada caso tiene un control similar en edad y otras variables"]),
  ("30 mujeres con cáncer de mama y 30 con mamografía normal", ["Se les pregunta por la lactancia", "Cada caso emparejado con un control"]),
  Q("¿El investigador asigna la exposición?", [
      L("Sí", "Experimental", ["Ensayo clínico"]),
      Q("¿Se parte de la enfermedad?", [
          L("Sí", "CASOS Y CONTROLES", ["Con y sin cáncer", "Exposición pasada: lactancia"], path=True),
          L("No: de la exposición", "Cohorte", ["Se sigue hacia adelante"])],
        edge="No: observacional", path=True)], path=True),
  ("Diseños observacionales", [("Casos y controles", True), ("Cohorte", False), ("Transversal", False)], [
      ("Punto de partida", ["Enfermedad", "Exposición", "Ambas a la vez"]),
      ("Medida", ["Odds ratio", "Riesgo relativo", "Prevalencia"])]),
  ["El pareo controla factores de confusión.",
   "Útil para enfermedades raras.",
   "Riesgo de sesgo de memoria."],
  GORDIS)

# TRA-044 · embudo
V("embudo", "TRA-044", "nina-bolita-popliteo-indolora-ganglion", "Bulto detrás de la rodilla en una niña",
  "TRAUMATOLOGÍA ENAM: QUISTE POPLÍTEO (GANGLIÓN)", "TRAUMATOLOGÍA",
  ("Quiste poplíteo en el niño", ["Masa quística en la cara posterointerna de la rodilla",
   "En niños suele ser benigno, indoloro y desaparece solo"]),
  ("Niña de 7 años", ["'Bolita' detrás de la rodilla que no molesta", "Quiste de 3 cm, firme, no doloroso, movilidad normal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Masa poplítea en un niño",
   "candidatos": ["Ganglión", "Adenomegalia", "Absceso", "Lipoma"],
   "pasos": [("Sin dolor, calor ni fiebre", ["Absceso"]),
             ("Quística, única, posterointerna", ["Adenomegalia", "Lipoma"])],
   "final": ("GANGLIÓN (QUISTE POPLÍTEO)", ["Explicar que es benigno", "Ecografía si hay dudas; observar"]),
   "nota": "En el niño no se asocia a lesión intraarticular, a diferencia del adulto."},
  ["La mayoría involuciona en 1-2 años.",
   "Cirugía solo si duele o crece mucho.",
   "Signos de alarma: crecimiento rápido, dolor nocturno, masa dura fija."],
  NELSON + " · AAOS – Popliteal (Baker's) cyst (OrthoInfo 2022)")

# NRL-049 · radial
V("radial", "NRL-049", "adolescente-rural-convulsiones-calcificaciones-taenia-solium", "Parásitos que llegan al cerebro",
  "NEUROLOGÍA ENAM: NEUROCISTICERCOSIS", "NEUROLOGÍA",
  ("Neurocisticercosis", ["Larvas de Taenia solium en el cerebro por ingerir huevos (fecal-oral)",
   "Principal causa de epilepsia adquirida en zonas rurales"]),
  ("Adolescente de 13 años de zona rural", ["6 meses de cefalea y dos convulsiones", "TC: múltiples calcificaciones"]),
  {"rotulo": "Mapa del tema", "centro": "CESTODOS", "centro_sub": "¿Cuál afecta el cerebro?", "ans": 0,
   "items": [("TAENIA SOLIUM", ["Cisticercos en el cerebro", "Huevos por vía fecal-oral"]),
             ("Taenia saginata", ["Solo intestinal (vaca)"]),
             ("Hymenolepis nana", ["Intestinal, niños"]),
             ("Echinococcus", ["Quiste hidatídico hepático o pulmonar"]),
             ("Diphyllobothrium", ["Pescado crudo, déficit de B12"])],
   "ruta": ["Zona rural", "Convulsiones", "Calcificaciones múltiples", "TAENIA SOLIUM"]},
  ["Calcificaciones = quistes muertos: antiepilépticos, sin antiparasitarios.",
   "Quistes viables: albendazol ± praziquantel con corticoide.",
   "El cerdo es huésped intermediario; la persona con tenia contagia."],
  "IDSA/ASTMH – Guidelines for the diagnosis and treatment of neurocysticercosis (2018)")

# NEF-076 · radial
V("radial", "NEF-076", "osteomielitis-cronica-anasarca-proteinuria-amiloidosis", "Síndrome nefrótico con inflamación crónica",
  "NEFROLOGÍA ENAM: AMILOIDOSIS RENAL SECUNDARIA", "NEFROLOGÍA",
  ("Amiloidosis AA", ["Inflamación crónica (osteomielitis, AR, TB) produce proteína amiloide A",
   "Se deposita en el riñón: síndrome nefrótico y falla renal"]),
  ("Varón de 66 años con 20 años de osteomielitis", ["8 meses de edema hasta anasarca", "Proteinuria 7 g · albúmina 2,1 · creatinina 3,5 · HbA1c 6 %"]),
  {"rotulo": "Mapa del tema", "centro": "SÍNDROME NEFRÓTICO", "centro_sub": "Adulto", "ans": 0,
   "items": [("AMILOIDOSIS SECUNDARIA", ["Inflamación crónica", "Rojo Congo: birrefringencia verde"]),
             ("Nefropatía diabética", ["HbA1c 6 %: poco probable"]),
             ("Glomerulonefritis membranosa", ["Anti-PLA2R"]),
             ("Nefropatía hipertensiva", ["Proteinuria menor"]),
             ("Glomerulonefritis postinfecciosa", ["Nefrítico, C3 bajo"])],
   "ruta": ["Osteomielitis de 20 años", "Nefrótico", "Falla renal", "AMILOIDOSIS AA"]},
  ["Biopsia de grasa abdominal o renal con rojo Congo.",
   "Tratar la causa inflamatoria frena la progresión.",
   "Riñones grandes en la ecografía pese a la falla renal."],
  "KDIGO – Glomerular diseases guideline (2021) · " + HARRISON)

# OFT-043 · árbol
A("OFT-043", "otitis-media-recurrente-amoxicilina-previa-amoxicilina-clavulanico", "Otitis media tras amoxicilina reciente",
  "OTORRINOLARINGOLOGÍA ENAM: OTITIS MEDIA AGUDA", "OTORRINOLARINGOLOGÍA",
  ("Otitis media aguda", ["Primera elección: amoxicilina a dosis alta (80-90 mg/kg/día)",
   "Si recibió amoxicilina en los últimos 30 días: amoxicilina-clavulánico"]),
  ("Niño de 3 años con 2 días de otalgia y fiebre", ["Hace un mes: otitis tratada con amoxicilina 40 mg/kg/día", "T 38,5 °C · tímpano abombado e hiperémico"]),
  Q("¿Amoxicilina en los últimos 30 días?", [
      L("Sí", "AMOXICILINA-CLAVULÁNICO", ["90 mg/kg/día de amoxicilina", "Cubre H. influenzae y Moraxella productores de betalactamasa"], path=True),
      L("No", "Amoxicilina dosis alta", ["80-90 mg/kg/día"])], path=True),
  ("Otitis media aguda", [("Clave", True), ("Detalle", False)], [
      ("Gérmenes", ["Neumococo", "H. influenzae, Moraxella"]),
      ("Alergia a penicilina", ["Cefuroxima o cefdinir", "Macrólido si es grave"]),
      ("Duración", ["10 días en < 2 años", "5-7 días en mayores"])]),
  ["La dosis previa (40 mg/kg/día) fue baja para neumococo resistente.",
   "Recurrente: ≥ 3 episodios en 6 meses o ≥ 4 en 1 año.",
   "Si falla a las 48-72 h: ceftriaxona IM."],
  "AAP – Clinical practice guideline: diagnosis and management of acute otitis media (2013)")

# SP-139 · árbol
A("SP-139", "nino-9-anos-ensayo-asentimiento-madre-firma", "Participación de un niño en un ensayo clínico",
  "SALUD PÚBLICA ENAM: ASENTIMIENTO INFORMADO", "SALUD PÚBLICA",
  ("Investigación en menores", ["El niño da su asentimiento (acepta) si puede entender",
   "El consentimiento legal lo firma el padre, la madre o el tutor"]),
  ("Escolar de 9 años bilingüe", ["Madre quechuahablante", "Se le explica el ensayo en castellano"]),
  Q("¿Es menor de edad?", [
      L("Sí", "ASENTIMIENTO + FIRMA DE LA MADRE", ["El niño acepta", "La madre consiente (en su idioma)"], path=True),
      L("No", "Consentimiento propio", ["Mayor de edad y capaz"])], path=True),
  ("Asentimiento y consentimiento", [("Niño", True), ("Madre", True)], [
      ("Documento", ["Asentimiento", "Consentimiento informado"]),
      ("Idioma", ["El que comprende", "Quechua, con traductor si hace falta"])]),
  ["La firma del niño sola no basta, aunque tenga 9 años.",
   "No se requiere autoridad judicial para un ensayo clínico.",
   "El niño puede negarse aunque la madre acepte."],
  "INS – Reglamento de ensayos clínicos del Perú (DS 021-2017-SA) · CIOMS – Pautas éticas internacionales (2016)")

# SP-140 · matriz
V("matriz", "SP-140", "sulfato-ferroso-entregado-no-administrado-efectividad", "Indicadores de logro",
  "SALUD PÚBLICA ENAM: EFECTIVIDAD", "SALUD PÚBLICA",
  ("Eficacia, efectividad y eficiencia", ["Eficacia: funciona en condiciones ideales",
   "Efectividad: funciona en la vida real (si la madre no lo da, falla)"]),
  ("Visitas domiciliarias", ["Se entregó sulfato ferroso para prevenir anemia", "En 1 de cada 10 casas la madre no lo administra"]),
  {"rotulo": "Indicador y pregunta", "eje_x": "Rasgo", "eje_y": "Indicador",
   "cols": ["Pregunta", "En este caso"], "rows": ["Efectividad", "Eficacia", "Eficiencia", "Cobertura"], "caso": (0, 1),
   "cells": [[("¿Funciona en la realidad?", []), ("COMPROMETIDA", ["El hierro no llega al niño"])],
             [("¿Funciona en condiciones ideales?", []), ("No se mide aquí", [])],
             [("¿A qué costo?", []), ("No se mide aquí", [])],
             [("¿A cuántos llegó?", []), ("Se entregó a todos", [])]]},
  ["La adherencia es el punto débil de la suplementación.",
   "Consejería y visitas mejoran el cumplimiento.",
   "La equidad se refiere a la justicia en el acceso."],
  "MINSA – NTS 213: Prevención y control de la anemia (2024) · OPS – Indicadores de salud (2018)")

# SP-141 · radial
V("radial", "SP-141", "centro-i4-discapacidad-sin-acceso-upss-rehabilitacion", "Garantizar la atención de la discapacidad",
  "SALUD PÚBLICA ENAM: OFERTA DE SERVICIOS DE REHABILITACIÓN", "SALUD PÚBLICA",
  ("Brecha de oferta", ["Si la población no accede a un servicio, se crea la oferta cerca de ella",
   "El I-4 puede implementar una UPSS de medicina de rehabilitación"]),
  ("Centro de salud I-4", ["El ASIS identifica población con discapacidad sin acceso"]),
  {"rotulo": "Mapa del tema", "centro": "ACCESO", "centro_sub": "Opciones del equipo", "ans": 0,
   "items": [("UPSS DE REHABILITACIÓN", ["Oferta en el propio I-4", "Solución sostenible"]),
             ("Censar y referir", ["No resuelve el acceso"]),
             ("Hospitalizar en el INR", ["Desproporcionado"]),
             ("Recategorizar a nivel II", ["No corresponde"]),
             ("Rehabilitación basada en la comunidad", ["Complementa la UPSS"])],
   "ruta": ["ASIS", "Brecha de acceso", "Crear la oferta", "UPSS DE REHABILITACIÓN"]},
  ["UPSS: unidad productora de servicios de salud.",
   "Ley 29973: derecho de las personas con discapacidad a la rehabilitación.",
   "La categoría depende de la capacidad resolutiva, no de una sola necesidad."],
  "MINSA – NTS 021: Categorías de establecimientos del sector salud · Ley N.° 29973 – Ley general de la persona con discapacidad")

# PED-187 · puntaje
V("puntaje", "PED-187", "preescolar-fiebre-polipnea-tirajes-crepitantes-rx-torax", "Neumonía en el preescolar",
  "PEDIATRÍA ENAM: NEUMONÍA ADQUIRIDA EN LA COMUNIDAD", "PEDIATRÍA",
  ("Neumonía en el niño", ["Fiebre + taquipnea + tirajes + crepitantes",
   "Con signos de gravedad: hospitalizar y confirmar con Rx de tórax"]),
  ("Niña de 4 años", ["3 días de rinitis, tos y fiebre; al 4.º día dificultad respiratoria", "Aleteo, polipnea, tirajes · crepitantes y sibilantes"]),
  {"rotulo": "Signos de neumonía grave (OMS/AIEPI)", "escala": "Signos del caso", "total": 4, "max": 5,
   "total_label": "Signos presentes",
   "interpreta": "Neumonía grave: hospitalizar",
   "items": [("Taquipnea (≥ 40 en 1-5 años)", "✓", True), ("Tiraje subcostal", "✓", True),
             ("Aleteo nasal", "✓", True), ("Crepitantes", "✓", True),
             ("Saturación < 92 % o cianosis", "—", False)],
   "bandas": [("Sin tiraje", "Neumonía", "Amoxicilina oral en casa", False),
              ("Con tiraje", "Neumonía grave", "Rx de tórax, O₂, antibiótico EV", True)]},
  ["La Rx confirma y muestra complicaciones (derrame).",
   "Los sibilantes pueden aparecer en neumonías virales o por Mycoplasma.",
   "Hemograma y hemocultivo apoyan, pero no son el examen inicial."],
  "OMS – Pocket book of hospital care for children (2013) · BTS – Guidelines for CAP in children (2011)")

# GIN-189 · termómetro
V("termometro", "GIN-189", "puerpera-hematoma-3-cm-episiotomia-observacion", "Masa en la episiotomía",
  "OBSTETRICIA ENAM: HEMATOMA DE EPISIOTOMÍA", "OBSTETRICIA",
  ("Hematoma perineal", ["Pequeño, estable y sin infección: tratamiento conservador",
   "Grande o que crece: drenaje y hemostasia"]),
  ("Puérpera de 6 días con dolor vulvar", ["Tumoración de 3 cm en la episiotomía", "Sin signos de inflamación"]),
  {"rotulo": "Tamaño y evolución",
   "niveles": [("< 5 cm", "Pequeño y estable", ["3 CM, SIN FLOGOSIS", "Conservador"]),
               ("> 5 cm", "Grande o creciente", ["Drenaje en sala"]),
               ("Infectado", "Absceso", ["Abrir, drenar, antibiótico"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Analgésicos y observación", ["Hielo, reposo, control"], True),
             (2, "Reevaluar en 24-48 h", ["Tamaño, dolor, fiebre"], False),
             (3, "Drenar si crece o se infecta", ["En sala, con hemostasia"], False)]},
  ["Punzar con aguja un hematoma arriesga infectarlo.",
   "Los antibióticos no se necesitan sin signos de infección.",
   "Se reabsorbe en días a semanas."],
  WILLIAMS)

# END-055 · tarjetas
V("tarjetas", "END-055", "anciano-falla-renal-glucosa-50-glibenclamida", "Hipoglucemia por antidiabéticos",
  "ENDOCRINOLOGÍA ENAM: HIPOGLUCEMIA POR SULFONILUREAS", "ENDOCRINOLOGÍA",
  ("Hipoglucemia por glibenclamida", ["Las sulfonilureas liberan insulina aunque la glucosa esté baja",
   "La falla renal prolonga su efecto: hipoglucemia grave y duradera en ancianos"]),
  ("Diabético de 78 años", ["Conducta bizarra, ideas paranoides, confusión, visión borrosa", "Creatinina 1,8 · glucosa 50 mg/dl"]),
  {"rotulo": "¿Qué fármaco la produce?", "ans": 0, "cards": [
      {"titulo": "GLIBENCLAMIDA", "datos": [
          ("Mecanismo", "Secreta insulina", True), ("Hipoglucemia", "Frecuente, larga", True),
          ("Falla renal", "Se acumula", True), ("Anciano", "Evitar", False)],
       "pie": "Sulfonilurea de acción larga"},
      {"titulo": "Metformina", "datos": [
          ("Mecanismo", "Baja producción hepática", False), ("Hipoglucemia", "No sola", False),
          ("Falla renal", "Acidosis láctica", False), ("Anciano", "Ajustar dosis", False)],
       "pie": "Primera línea"},
      {"titulo": "Pioglitazona", "datos": [
          ("Mecanismo", "Sensibiliza", False), ("Hipoglucemia", "No sola", False),
          ("Falla renal", "Retiene líquido", False), ("Anciano", "Cuidado con ICC", False)],
       "pie": "Tiazolidinediona"},
      {"titulo": "Acarbosa", "datos": [
          ("Mecanismo", "Frena absorción", False), ("Hipoglucemia", "No sola", False),
          ("Falla renal", "Evitar si grave", False), ("Anciano", "Gases", False)],
       "pie": "Inhibe alfa-glucosidasa"}]},
  ["Hospitalizar: la hipoglucemia puede recurrir por 24-72 h.",
   "Tratamiento: dextrosa EV y octreótido si recurre.",
   "Neuroglucopenia en ancianos puede simular psicosis o ACV."],
  "ADA – Standards of Care 2025: Older adults · Beers Criteria (AGS 2023)")

# NEF-077 · embudo
V("embudo", "NEF-077", "hematuria-tras-infeccion-respiratoria-nefropatia-iga", "Hematuria recurrente en el joven",
  "NEFROLOGÍA ENAM: NEFROPATÍA POR IgA", "NEFROLOGÍA",
  ("Nefropatía por IgA (Berger)", ["Hematuria macroscópica 1-2 días después de una infección respiratoria",
   "Episodios recurrentes; C3 normal; la glomerulonefritis más frecuente del mundo"]),
  ("Varón de 24 años con orina roja", ["5 años de hematuria tras infecciones respiratorias", "80 % hematíes dismórficos · creatinina 1 · proteinuria 0,8 g/24 h"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hematuria glomerular recurrente",
   "candidatos": ["Nefropatía por IgA", "Membranosa", "Cambios mínimos", "GEFS primaria"],
   "pasos": [("Proteinuria < 3,5 g: no es nefrótico", ["Membranosa", "Cambios mínimos"]),
             ("Hematuria macroscópica sinfaringítica recurrente", ["GEFS primaria"])],
   "final": ("NEFROPATÍA POR IgA", ["Biopsia: depósitos mesangiales de IgA", "IECA o ARA II si hay proteinuria"]),
   "nota": "En la GN postestreptocócica la hematuria aparece 2-3 semanas después, no a los 1-2 días."},
  ["Controlar presión y proteinuria: marcan el pronóstico.",
   "Hasta 30 % progresa a enfermedad renal crónica en 20 años.",
   "Púrpura de Henoch-Schönlein: la forma sistémica de la IgA."],
  "KDIGO – Clinical practice guideline for IgA nephropathy (2025)")

# CAR-063 · tarjetas
V("tarjetas", "CAR-063", "angina-sincope-disnea-pulso-parvus-estenosis-aortica", "Soplos y valvulopatías",
  "CARDIOLOGÍA ENAM: ESTENOSIS AÓRTICA", "CARDIOLOGÍA",
  ("Estenosis aórtica", ["Tríada: angina, síncope de esfuerzo y disnea",
   "Pulso parvus et tardus y soplo sistólico eyectivo"]),
  ("Varón de 60 años", ["Dolor torácico, síncopes de esfuerzo, disnea", "Pulso parvus · choque de punta desplazado · soplo sistólico eyectivo"]),
  {"rotulo": "¿Qué válvula falla?", "ans": 0, "cards": [
      {"titulo": "ESTENOSIS AÓRTICA", "datos": [
          ("Soplo", "Sistólico eyectivo", True), ("Pulso", "Parvus et tardus", True),
          ("Síntomas", "Angina, síncope, disnea", True), ("Irradia", "Carótidas", False)],
       "pie": "Recambio valvular (cirugía o TAVI)"},
      {"titulo": "Insuficiencia aórtica", "datos": [
          ("Soplo", "Diastólico", False), ("Pulso", "Saltón (Corrigan)", False),
          ("Síntomas", "Disnea", False), ("Irradia", "Borde esternal", False)],
       "pie": "Presión diferencial amplia"},
      {"titulo": "Estenosis mitral", "datos": [
          ("Soplo", "Retumbo diastólico", False), ("Pulso", "FA frecuente", False),
          ("Síntomas", "Disnea, hemoptisis", False), ("Irradia", "No", False)],
       "pie": "Fiebre reumática"},
      {"titulo": "Insuficiencia mitral", "datos": [
          ("Soplo", "Holosistólico", False), ("Pulso", "Normal", False),
          ("Síntomas", "Disnea", False), ("Irradia", "Axila", False)],
       "pie": "Prolapso, isquemia"}]},
  ["Con síntomas la sobrevida sin cirugía es de 2-5 años.",
   "Evitar vasodilatadores potentes: pueden causar síncope.",
   "Ecocardiograma: área < 1 cm² = estenosis grave."],
  "ESC/EACTS – Guidelines for the management of valvular heart disease (2021; actualización 2025)")

# END-056 · puntaje
V("puntaje", "END-056", "dm2-establecimiento-i4-albuminuria-300-referir", "¿Cuándo referir al diabético?",
  "ENDOCRINOLOGÍA ENAM: REFERENCIA EN DIABETES TIPO 2", "ENDOCRINOLOGÍA",
  ("Diabetes en el primer nivel", ["El I-4 maneja la diabetes no complicada",
   "Daño de órgano blanco (albuminuria > 300 mg/día) exige referencia"]),
  ("Varón de 45 años con DM2 recién diagnosticada", ["Establecimiento I-4", "Consulta por sed excesiva"]),
  {"rotulo": "Criterios de referencia", "escala": "Criterio presente", "total": 1, "max": 6,
   "total_label": "Criterios del caso",
   "interpreta": "Un criterio basta para referir",
   "items": [("Albuminuria > 300 mg/24 h", "✓", True), ("TFG < 45 ml/min", "—", False),
             ("Retinopatía", "—", False), ("Pie diabético", "—", False),
             ("Hipoglucemias graves", "—", False), ("Descompensación aguda (CAD, EHH)", "—", False)],
   "bandas": [("0", "Primer nivel", "Seguir en el I-4", False),
              ("≥ 1", "Referir", "A endocrinología o nefrología", True)]},
  ["Creatinina de 1,2 no es por sí sola criterio de referencia.",
   "La falta de adherencia se trabaja en el primer nivel.",
   "El diagnóstico de diabetes no necesita confirmación por especialista."],
  "MINSA – GPC para el diagnóstico, manejo y control de la DM2 en el primer nivel de atención (2016)")

# GIN-190 · tarjetas
V("tarjetas", "GIN-190", "urgencia-miccional-residuo-150-urodinamia", "Tipos de incontinencia urinaria",
  "GINECOLOGÍA ENAM: INCONTINENCIA DE URGENCIA", "GINECOLOGÍA",
  ("Incontinencia urinaria", ["De esfuerzo: al toser o pujar · De urgencia: no llega al baño",
   "Con residuo posmiccional alto hay que estudiar la vejiga con urodinamia"]),
  ("Mujer de 35 años", ["Pierde orina cuando siente urgencia · no con Valsalva", "Cistocele grado 1 · residuo posmiccional 150 ml"]),
  {"rotulo": "¿Qué tipo es y qué se pide?", "ans": 0, "cards": [
      {"titulo": "URGENCIA + RESIDUO ALTO", "datos": [
          ("Escape", "Con urgencia", True), ("Valsalva", "Negativo", True),
          ("Residuo", "150 ml (alto)", True), ("Estudio", "Urodinamia", False)],
       "pie": "Separa vejiga hiperactiva de obstrucción"},
      {"titulo": "De esfuerzo", "datos": [
          ("Escape", "Al toser o saltar", False), ("Valsalva", "Positivo", False),
          ("Residuo", "Normal", False), ("Estudio", "Clínico", False)],
       "pie": "Ejercicios de Kegel"},
      {"titulo": "Por rebosamiento", "datos": [
          ("Escape", "Goteo continuo", False), ("Valsalva", "Variable", False),
          ("Residuo", "Muy alto", False), ("Estudio", "Urodinamia", False)],
       "pie": "Obstrucción o vejiga hipoactiva"},
      {"titulo": "Mixta", "datos": [
          ("Escape", "Esfuerzo + urgencia", False), ("Valsalva", "Positivo", False),
          ("Residuo", "Normal", False), ("Estudio", "Según predominio", False)],
       "pie": "Tratar lo que predomine"}]},
  ["Residuo > 100 ml es anormal.",
   "Antes de fármacos antimuscarínicos, descartar retención.",
   "Descartar infección urinaria con examen de orina."],
  "AUA/SUFU – Guideline on overactive bladder (2024) · ACOG – Practice Bulletin 155: Urinary incontinence in women (2015)")

# SP-142 · fases
V("fases", "SP-142", "centro-i3-seguimiento-casos-contactos-equipos-intervencion", "Seguimiento de casos y contactos",
  "SALUD PÚBLICA ENAM: EQUIPOS DE INTERVENCIÓN INTEGRAL", "SALUD PÚBLICA",
  ("Seguimiento comunitario", ["Lo primero es tener quién haga el seguimiento",
   "Equipos de intervención integral: visitan, monitorean y refieren"]),
  ("Centro de salud I-3", ["Hay que implementar el seguimiento de pacientes y contactos", "¿Qué es prioridad 1 según MINSA?"]),
  {"rotulo": "Orden de implementación", "ans": 0,
   "fases": [("1", "Prioridad 1", "EQUIPOS INTEGRALES", ["Organizarlos y capacitarlos"]),
             ("2", "Operar", "Seguimiento", ["Visitas y llamadas"]),
             ("3", "Insumos", "Oxímetros, EPP", ["Para los equipos"]),
             ("4", "Red", "Referencia", ["Hospitales y clínicas"])],
   "curvas": [],
   "chips_titulo": "Prioridad 1 · marcada la correcta",
   "chips": [("Equipos de intervención integral", True), ("Internamiento", False), ("Clínicas locales", False), ("Oxímetros", False)]},
  ["Un I-3 no hospitaliza: refiere.",
   "Sin equipos, los insumos no sirven.",
   "El seguimiento temprano detecta a quien necesita oxígeno."],
  "MINSA – RM 193-2020-MINSA: Prevención, diagnóstico y tratamiento de personas afectadas por COVID-19")

# INF-092 · embudo
V("embudo", "INF-092", "nino-prolapso-rectal-hematoquezia-anemia-tricocefalo", "Prolapso rectal con anemia en el niño",
  "INFECTOLOGÍA ENAM: TRICOCEFALOSIS", "INFECTOLOGÍA",
  ("Tricocefalosis (Trichuris trichiura)", ["Gusano látigo que se fija en colon y recto",
   "Infección masiva: disentería, tenesmo, prolapso rectal y anemia"]),
  ("Niño de 4 años", ["Hematoquezia, tenesmo y prolapso rectal", "Leucocitos 12 300 · Hb 5 g/dl"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Sangrado rectal con anemia grave",
   "candidatos": ["Trichuris trichiura", "Uncinarias", "C. difficile", "Fasciola hepática"],
   "pasos": [("Prolapso rectal y tenesmo: colon distal", ["Uncinarias", "Fasciola hepática"]),
             ("Niño sin antibióticos ni hospitalización", ["C. difficile"])],
   "final": ("TRICOCEFALOSIS MASIVA", ["Huevos en 'barril' en heces", "Albendazol o mebendazol + hierro"]),
   "nota": "Al reducir el prolapso a veces se ven los gusanos adheridos a la mucosa."},
  ["Uncinarias: anemia ferropénica sin prolapso, en duodeno.",
   "Fasciola: dolor en hipocondrio derecho y eosinofilia.",
   "Prevención: lavado de manos, agua segura, desparasitación."],
  "OMS – Soil-transmitted helminth infections: fact sheet (2023) · " + NELSON)

# GIN-191 · árbol
A("GIN-191", "multipara-nalgas-puras-expulsivo-parto-vaginal", "Podálica en periodo expulsivo",
  "OBSTETRICIA ENAM: PARTO EN PODÁLICA", "OBSTETRICIA",
  ("Presentación podálica", ["Lo habitual es cesárea programada",
   "Pero en el expulsivo, multípara con feto pequeño y nalgas puras: parto vaginal asistido"]),
  ("Multigesta de 39 semanas", ["Dilatación completa, nalgas puras", "AU 29 cm · 2 partos vaginales previos de 3200 g"]),
  Q("¿Llega en periodo expulsivo?", [
      Q("¿Condiciones favorables?", [
          L("Sí: multípara, feto pequeño, nalgas puras", "PARTO VAGINAL ASISTIDO", ["Maniobra de Bracht", "Personal con experiencia"], path=True),
          L("No", "Cesárea", ["Feto grande, pies, pelvis dudosa"])],
        edge="Sí", path=True),
      L("No: antes del parto", "Versión externa o cesárea", ["A las 36-37 semanas"])], path=True),
  ("Opciones en la podálica", [("Vaginal", True), ("Cesárea", False)], [
      ("Cuándo", ["Expulsivo, condiciones favorables", "Resto de casos"]),
      ("Riesgo", ["Retención de cabeza", "Quirúrgico materno"])]),
  ["La oxitocina no se usa para inducir en podálica.",
   "El fórceps en podálica solo para la cabeza última.",
   "AU de 29 cm a término sugiere feto pequeño."],
  "ACOG – Committee Opinion 745: Mode of term singleton breech delivery (2018) · " + WILLIAMS)

# NEU-053 · termómetro
V("termometro", "NEU-053", "covid-pafi-305-oxigenoterapia-convencional", "COVID-19: ¿qué soporte de oxígeno?",
  "NEUMOLOGÍA ENAM: OXIGENOTERAPIA EN COVID-19", "NEUMOLOGÍA",
  ("Soporte respiratorio escalonado", ["El PaO₂/FiO₂ (PaFi) mide la gravedad de la hipoxemia",
   "PaFi > 300 con SatO₂ baja: oxígeno convencional"]),
  ("Varón obeso de 55 años con COVID-19", ["Afebril · FR 26 · FC 100", "PaFi 305 · PaO₂ 64 · SatO₂ 90 %"]),
  {"rotulo": "PaO₂/FiO₂",
   "niveles": [("> 300", "Hipoxemia leve", ["PAFI 305", "Cánula o máscara"]),
               ("200-300", "Moderada", ["Alto flujo o VNI"]),
               ("< 200", "Grave", ["Intubación y ventilación"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Oxigenoterapia convencional", ["Meta SatO₂ 92-96 %"], True),
             (2, "Alto flujo si empeora", ["FR alta o SatO₂ que no sube"], False),
             (3, "Ventilación mecánica", ["Agotamiento o PaFi muy baja"], False)]},
  ["Posición prona despierto puede mejorar la oxigenación.",
   "Dexametasona si necesita oxígeno.",
   "Vigilar signos de fatiga: FR > 30, uso de accesorios."],
  "OMS – Clinical management of COVID-19: living guideline (2023) · NIH – COVID-19 treatment guidelines (2024)")

# CAR-064 · tarjetas
V("tarjetas", "CAR-064", "monitor-asistolia-adrenalina-rcp", "Ritmos del paro y su manejo",
  "CARDIOLOGÍA ENAM: ASISTOLIA", "CARDIOLOGÍA",
  ("Asistolia", ["Ritmo no desfibrilable: la descarga no sirve",
   "RCP continua + adrenalina 1 mg lo antes posible"]),
  ("Mujer de 58 años con IMA sin ST elevado", ["Monitorizada en shock trauma", "Pierde la conciencia · monitor: asistolia"]),
  {"rotulo": "¿Qué ritmo y qué hacer?", "ans": 0, "cards": [
      {"titulo": "ASISTOLIA", "datos": [
          ("Desfibrilar", "No", True), ("Fármaco", "ADRENALINA YA", True),
          ("Clave", "Revisar cables", False)],
       "pie": "RCP + adrenalina cada 3-5 min"},
      {"titulo": "FV / TV sin pulso", "datos": [
          ("Desfibrilar", "Sí, inmediato", False), ("Fármaco", "Tras la 2.ª descarga", False),
          ("Clave", "Amiodarona", False)],
       "pie": "Descarga + RCP"},
      {"titulo": "AESP", "datos": [
          ("Desfibrilar", "No", False), ("Fármaco", "Adrenalina ya", False),
          ("Clave", "Causas reversibles", False)],
       "pie": "5 H y 5 T"},
      {"titulo": "TV con pulso", "datos": [
          ("Desfibrilar", "Cardioversión", False), ("Fármaco", "Amiodarona", False),
          ("Clave", "No es paro", False)],
       "pie": "Si inestable: sincronizada"}]},
  ["El golpe precordial no se recomienda.",
   "La intubación no debe retrasar compresiones ni adrenalina.",
   "Confirmar la asistolia en dos derivaciones."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2025)")

# HEM-036 · matriz
V("matriz", "HEM-036", "afrodescendiente-anemia-ictericia-reticulocitos-0-drepanocitos", "Forma del eritrocito y enfermedad",
  "HEMATOLOGÍA ENAM: DREPANOCITOSIS", "HEMATOLOGÍA",
  ("Anemia de células falciformes", ["Hemoglobina S: el hematíe se deforma en hoz (drepanocito)",
   "Reticulocitos 0 % sugiere crisis aplásica (parvovirus B19)"]),
  ("Varón afropanameño de 25 años", ["Anemia e ictericia · Hb 8 · reticulocitos 0 %", "Bilirrubina indirecta alta · banda anormal en electroforesis"]),
  {"rotulo": "Célula en el frotis", "eje_x": "Rasgo", "eje_y": "Célula",
   "cols": ["Enfermedad", "Pista"], "rows": ["Drepanocito", "Dianocito", "Eliptocito", "Microcito"], "caso": (0, 0),
   "cells": [[("DREPANOCITOSIS (HbS)", []), ("Electroforesis: HbS", ["Afrodescendiente"])],
             [("Talasemia, hepatopatía", []), ("HbA2 alta", [])],
             [("Eliptocitosis hereditaria", []), ("Membrana", [])],
             [("Ferropenia, talasemia", []), ("VCM bajo", [])]]},
  ["Crisis aplásica: transfusión y aislar (parvovirus es contagioso).",
   "Hidroxiurea reduce crisis dolorosas.",
   "Asplenia funcional: vacunas y profilaxis con penicilina en niños."],
  "NHLBI – Evidence-based management of sickle cell disease (2014) · ASH – Guidelines for SCD (2020)")

# PED-188 · fases
V("fases", "PED-188", "bajo-peso-2100-g-hierro-desde-el-primer-mes", "Hierro preventivo según el peso al nacer",
  "PEDIATRÍA ENAM: SUPLEMENTACIÓN DE HIERRO", "PEDIATRÍA",
  ("Suplementación preventiva de hierro", ["Prematuros y bajo peso nacen con menos reservas",
   "Por eso empiezan antes: desde los 30 días de vida"]),
  ("Recién nacido de 2100 g", ["Bajo peso al nacer", "¿Desde qué mes se da hierro?"]),
  {"rotulo": "Inicio según el peso al nacer", "ans": 1,
   "fases": [("Nacimiento", "Día 0", "Clampaje tardío", ["2-3 minutos: más reservas"]),
             ("1 mes", "Bajo peso o prematuro", "INICIAR HIERRO", ["Gotas 2 mg/kg/día", "Hasta los 6 meses"]),
             ("4 meses", "A término, peso normal", "Iniciar hierro", ["Gotas 2 mg/kg/día"]),
             ("6 meses", "Todos", "Tamizaje de Hb", ["Y alimentación rica en hierro"])],
   "curvas": [("Reservas de hierro", SKY, [0.9, 0.7, 0.45, 0.3, 0.2, 0.15, 0.1])],
   "chips_titulo": "Mes de inicio · marcado el correcto",
   "chips": [("Uno", True), ("Dos", False), ("Tres", False), ("Cuatro", False)]},
  ["Bajo peso al nacer: < 2500 g.",
   "Continuar con micronutrientes o hierro hasta el año.",
   "El clampaje tardío del cordón también previene la anemia."],
  "MINSA – NTS 213: Prevención y control de la anemia por deficiencia de hierro (2024)")
