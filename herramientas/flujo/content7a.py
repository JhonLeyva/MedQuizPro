"""Bloque 7 · parte A."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"

# HEM-029 · embudo
V("embudo", "HEM-029", "sepsis-biliar-sangrado-fibrinogeno-bajo-cid", "Sangrado con tiempos prolongados en la sepsis",
  "HEMATOLOGÍA ENAM: COAGULACIÓN INTRAVASCULAR DISEMINADA", "HEMATOLOGÍA",
  ("Coagulopatía de consumo", ["La sepsis activa la coagulación en todo el organismo y consume factores y plaquetas",
   "TP, TTPa y TT prolongados + fibrinógeno bajo + plaquetas bajas = CID"]),
  ("Varón de 48 años con piocolecisto y sepsis", ["Hematuria y púrpura en miembros inferiores", "Plaquetas 75 000 · TP, TTPa, TT largos · fibrinógeno bajo"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Sangrado con plaquetas bajas y tiempos prolongados",
   "candidatos": ["CID", "Déficit de vitamina K", "Hemofilia A", "PTI"],
   "pasos": [("Plaquetas bajas y TP + TTPa alterados a la vez", ["PTI", "Hemofilia A"]),
             ("Fibrinógeno bajo y TT prolongado en un séptico", ["Déficit de vitamina K"])],
   "final": ("COAGULACIÓN INTRAVASCULAR DISEMINADA", ["Tratar la causa: antibióticos y drenar el foco", "Plaquetas, plasma o crioprecipitado si sangra"]),
   "nota": "El déficit de vitamina K alarga TP y TTPa, pero no baja el fibrinógeno ni las plaquetas."},
  ["El pilar del tratamiento es controlar la sepsis y su foco.",
   "El dímero D elevado y los esquistocitos apoyan el diagnóstico.",
   "La PTI solo baja plaquetas; la hemofilia A solo alarga el TTPa."],
  "ISTH – Guidance for the diagnosis and management of DIC (J Thromb Haemost 2023) · " + HARRISON)

# GIN-146 · árbol
A("GIN-146", "cesarea-corporal-previa-trabajo-parto-sangrado", "Cesárea previa y trabajo de parto",
  "OBSTETRICIA ENAM: CESÁREA CORPORAL PREVIA", "OBSTETRICIA",
  ("Parto después de una cesárea", ["El tipo de incisión uterina previa decide si se permite el parto vaginal",
   "Incisión corporal (clásica) = alto riesgo de rotura: cesárea siempre"]),
  ("Gestante de 42 años, a término", ["Cesárea anterior con incisión corporal", "Inicia trabajo de parto con sangrado vaginal moderado"]),
  Q("¿Qué incisión uterina tuvo?", [
      L("Segmentaria transversa", "Prueba de trabajo de parto", ["Si hay una sola cesárea y la pelvis es adecuada", "Monitoreo continuo"]),
      Q("¿Ya inició trabajo de parto o sangra?", [
          L("No", "Cesárea programada", ["A las 36-37 semanas"]),
          L("Sí", "CESÁREA DE EMERGENCIA", ["Riesgo inminente de rotura uterina", "Sangrado: posible rotura en curso"], path=True)],
        edge="Corporal o en T", path=True)], path=True),
  ("Riesgo de rotura uterina", [("Corporal", True), ("Segmentaria", False)], [
      ("Rotura en trabajo de parto", ["4-9 %", "0,5-1 %"]),
      ("Parto vaginal", ["Contraindicado", "Permitido (PTP)"]),
      ("Momento de la cesárea", ["36-37 semanas o al iniciar parto", "Según evolución"])]),
  ["La inducción con prostaglandinas está contraindicada con cesárea previa.",
   "Signos de rotura: dolor súbito, pérdida de la dinámica, sangrado y bradicardia fetal.",
   "El grupo y Rh se piden, pero no retrasan la cesárea."],
  "ACOG – Practice Bulletin 205: Vaginal birth after cesarean delivery (2019) · " + WILLIAMS)

# INF-078 · tarjetas
V("tarjetas", "INF-078", "vih-cefalea-subaguda-rigidez-tinta-china", "Meningitis en el paciente con VIH",
  "INFECTOLOGÍA ENAM: MENINGITIS CRIPTOCÓCICA", "INFECTOLOGÍA",
  ("Meningitis subaguda en VIH", ["Cefalea progresiva de semanas en un VIH avanzado = criptococo hasta demostrar lo contrario",
   "Se confirma en el LCR: tinta china y antígeno criptocócico"]),
  ("Varón de 32 años con VIH hace 5 años", ["Cefalea de 20 días, cada vez más intensa", "Rigidez de nuca, sin focalización"]),
  {"rotulo": "¿Qué germen y cómo se confirma?", "ans": 0, "cards": [
      {"titulo": "CRIPTOCOCO", "datos": [
          ("Curso", "Subagudo, semanas", True), ("Focalidad", "Rara", True),
          ("LCR", "Presión de apertura alta", False), ("Prueba", "TINTA CHINA / antígeno", True)],
       "pie": "Anfotericina B + flucitosina"},
      {"titulo": "Tuberculosis", "datos": [
          ("Curso", "Subagudo", False), ("Focalidad", "Pares craneales", False),
          ("LCR", "Glucosa muy baja, ADA", False), ("Prueba", "GeneXpert en LCR", False)],
       "pie": "Esquema antituberculoso + corticoide"},
      {"titulo": "Toxoplasmosis", "datos": [
          ("Curso", "Días a semanas", False), ("Focalidad", "Frecuente", False),
          ("LCR", "Poco útil", False), ("Prueba", "TC: lesiones en anillo", False)],
       "pie": "Pirimetamina + sulfadiazina"},
      {"titulo": "Bacteriana aguda", "datos": [
          ("Curso", "Horas", False), ("Focalidad", "Poco frecuente", False),
          ("LCR", "Neutrófilos, glucosa baja", False), ("Prueba", "Gram y cultivo", False)],
       "pie": "Ceftriaxona + vancomicina"}]},
  ["El antígeno criptocócico en LCR o sangre es más sensible que la tinta china.",
   "Hay que controlar la hipertensión intracraneal con punciones evacuadoras.",
   "El TAR se inicia 4-6 semanas después del antifúngico."],
  "OMS – Guidelines for diagnosing, preventing and managing cryptococcal disease among adults with HIV (2022)")

# END-043 · radial
V("radial", "END-043", "hiperpigmentacion-hipotension-hiperkalemia-addison", "Insuficiencia suprarrenal primaria",
  "ENDOCRINOLOGÍA ENAM: ENFERMEDAD DE ADDISON", "ENDOCRINOLOGÍA",
  ("Insuficiencia suprarrenal", ["Primaria: faltan cortisol y aldosterona", "La ACTH alta oscurece la piel (efecto MSH)"]),
  ("Mujer de 35 años con 5 meses de astenia", ["Diarrea, baja de peso, PA 85/60, hiperpigmentación", "Na bajo · K alto · glucosa baja"]),
  {"rotulo": "Mapa del tema", "centro": "HIPOTENSIÓN Y ELECTROLITOS", "centro_sub": "¿Qué glándula falla?", "ans": 0,
   "items": [("ADDISON", ["Hiperpigmentación, K alto, Na bajo", "Falta cortisol y aldosterona"]),
             ("Insuficiencia secundaria", ["Sin hiperpigmentación", "Potasio normal"]),
             ("Hiperaldosteronismo", ["HTA con K bajo"]),
             ("Feocromocitoma", ["HTA paroxística, sudoración"]),
             ("Hipotiroidismo primario", ["Bradicardia, piel seca, frío"])],
   "ruta": ["Astenia, hipotensión, baja de peso", "Piel oscura", "Na bajo, K alto, glucosa baja", "ADDISON"]},
  ["Confirmación: cortisol matutino bajo con ACTH alta o prueba de estímulo con ACTH.",
   "Causa más frecuente: autoinmune; en nuestro medio, también tuberculosis.",
   "Tratamiento: hidrocortisona + fludrocortisona; duplicar dosis en estrés."],
  "Endocrine Society – Diagnosis and treatment of primary adrenal insufficiency (JCEM 2016) · " + HARRISON)

# TRA-033 · fases
V("fases", "TRA-033", "trauma-cervical-alto-inmovilizar-collarin", "Trauma cervical: primer paso",
  "TRAUMATOLOGÍA ENAM: TRAUMATISMO CERVICAL", "TRAUMATOLOGÍA",
  ("Lesión de columna cervical", ["Todo trauma con mecanismo de riesgo se trata como lesión cervical",
   "La restricción del movimiento con collarín evita el daño medular secundario"]),
  ("Paciente con traumatismo cervical alto", ["Se pregunta la primera indicación"]),
  {"rotulo": "Secuencia de atención", "ans": 0,
   "fases": [("Inmovilizar", "Al primer contacto", "COLLARÍN CERVICAL", ["Junto con la vía aérea (A)", "Tabla y bloques"]),
             ("Evaluar", "Revisión primaria", "ABCDE", ["Ventilación, choque neurogénico"]),
             ("Imagen", "Revisión secundaria", "TC cervical", ["Criterios NEXUS o canadienses"]),
             ("Definitivo", "Especialista", "Neurocirugía", ["Fijación si es inestable"])],
   "curvas": [],
   "chips_titulo": "Indicación inicial · marcada la correcta",
   "chips": [("Collarín", True), ("Corticoides", False), ("Vasopresores", False), ("Antibióticos", False)]},
  ["La metilprednisolona ya no se recomienda en el trauma medular.",
   "Choque neurogénico: hipotensión con bradicardia; se usan vasopresores solo tras reponer volumen.",
   "Una lesión alta (C3-C5) puede comprometer el diafragma."],
  ATLS + " · AANS/CNS – Guidelines for the management of acute cervical spine and spinal cord injuries (2013)")

# SP-109 · radial
V("radial", "SP-109", "distrito-desnutricion-accion-comunitaria", "Promoción de la salud",
  "SALUD PÚBLICA ENAM: PROMOCIÓN DE LA SALUD", "SALUD PÚBLICA",
  ("Carta de Ottawa", ["Cinco líneas de acción para mejorar la salud de la población",
   "Frente a un problema local como la desnutrición: participación de la comunidad"]),
  ("Distrito del norte del Perú", ["Aumenta el índice de desnutrición", "¿Qué prioriza el equipo de salud?"]),
  {"rotulo": "Mapa del tema", "centro": "PROMOCIÓN DE LA SALUD", "centro_sub": "Carta de Ottawa", "ans": 0,
   "items": [("ACCIÓN COMUNITARIA", ["La población identifica y resuelve", "Lo que hace el equipo local"]),
             ("Políticas públicas saludables", ["Decisión del Estado"]),
             ("Entornos saludables", ["Escuelas, municipios"]),
             ("Habilidades personales", ["Educación para la salud"]),
             ("Reorientar los servicios", ["De curar a prevenir"])],
   "ruta": ["Desnutrición en aumento", "Problema local y social", "Movilizar a la comunidad", "ACCIÓN COMUNITARIA"]},
  ["Aprobar políticas no está en manos del equipo de salud local.",
   "Ejemplos: comedores, vigilancia comunal del crecimiento, huertos familiares.",
   "La vigilancia de no transmisibles no responde a la desnutrición."],
  "OMS – Carta de Ottawa para la promoción de la salud (1986) · MINSA – Lineamientos de política de promoción de la salud (2017)")

# SP-110 · matriz
V("matriz", "SP-110", "rechazar-hipotesis-nula-verdadera-error-alfa", "Errores en la prueba de hipótesis",
  "SALUD PÚBLICA ENAM: ERROR TIPO I", "SALUD PÚBLICA",
  ("Errores de la prueba de hipótesis", ["Tipo I (α): rechazar H0 cuando es verdadera · falso positivo",
   "Tipo II (β): no rechazar H0 cuando es falsa · falso negativo"]),
  ("Investigación", ["Se concluye que H0 es falsa", "Pero en realidad era verdadera"]),
  {"rotulo": "Decisión frente a la realidad", "eje_x": "Realidad", "eje_y": "Decisión",
   "cols": ["H0 verdadera", "H0 falsa"], "rows": ["Se rechaza H0", "No se rechaza H0"], "caso": (0, 0),
   "cells": [[("ERROR TIPO I (α)", ["Falso positivo", "Se fija en 0,05"]), ("Acierto", ["Potencia = 1 − β"])],
             [("Acierto", ["1 − α"]), ("Error tipo II (β)", ["Falso negativo", "Muestra pequeña"])]]},
  ["El valor p se compara con α: si p < 0,05 se rechaza H0.",
   "Aumentar el tamaño de muestra reduce el error β y sube la potencia.",
   "Los errores aleatorios no son sesgos de diseño."],
  "Gordis. Epidemiología 6.ª ed. (2019) · Hulley. Diseño de investigaciones clínicas 5.ª ed. (2022)")

# NEF-067 · árbol
A("NEF-067", "diarrea-oliguria-fena-bajo-reto-fluidos", "Oliguria: ¿prerrenal o renal?",
  "NEFROLOGÍA ENAM: LESIÓN RENAL AGUDA PRERRENAL", "NEFROLOGÍA",
  ("Lesión renal aguda", ["Los índices urinarios distinguen la causa prerrenal de la necrosis tubular",
   "Na urinario < 20 y FENa < 1 % = el túbulo funciona y retiene sodio"]),
  ("Varón de 48 años con diarrea de alto flujo", ["Diuresis de 200 ml en 24 h · creatinina 1,8", "Na urinario < 20 · FENa < 1 % · Cr orina/plasma > 40"]),
  Q("¿Cómo están los índices urinarios?", [
      L("FENa < 1 %, NaU < 20", "PRERRENAL: RETO DE FLUIDOS", ["Cristaloides EV y medir diuresis", "Hipovolemia por diarrea"], path=True),
      L("FENa > 2 %, NaU > 40", "Necrosis tubular aguda", ["Cilindros granulosos", "Evitar sobrecarga"]),
      L("Hidronefrosis en ecografía", "Posrenal", ["Desobstruir la vía"])], path=True),
  ("Índices urinarios", [("Prerrenal", True), ("NTA", False)], [
      ("Na urinario", ["< 20 mEq/L", "> 40 mEq/L"]),
      ("FENa", ["< 1 %", "> 2 %"]),
      ("Cr orina/plasma", ["> 40", "< 20"]),
      ("Sedimento", ["Cilindros hialinos", "Cilindros granulosos"])]),
  ["Los diuréticos no se usan en la LRA prerrenal: empeoran la hipovolemia.",
   "La dopamina a dosis renal no protege el riñón.",
   "Si no se corrige a tiempo, la prerrenal evoluciona a necrosis tubular."],
  "KDIGO – Clinical practice guideline for acute kidney injury (2012; actualización en curso) · " + HARRISON)

# REU-044 · puntaje
V("puntaje", "REU-044", "dolor-gluteo-nocturno-schober-espondiloartritis", "Dolor lumbar inflamatorio",
  "REUMATOLOGÍA ENAM: ESPONDILOARTRITIS AXIAL", "REUMATOLOGÍA",
  ("Dolor lumbar inflamatorio", ["Dolor nocturno que mejora con el movimiento y no con el reposo",
   "Con PCR alta y Schöber limitado orienta a espondiloartritis"]),
  ("Varón de 51 años con dolor glúteo de > 5 años", ["Nocturno, lo despierta, mejora al moverse", "Schöber (+) · PCR 20,5 mg/dl"]),
  {"rotulo": "Criterios ASAS de dolor inflamatorio", "escala": "ASAS (dolor lumbar > 3 meses)", "total": 4, "max": 5,
   "total_label": "Criterios que cumple el caso",
   "interpreta": "Dolor inflamatorio: buscar espondiloartritis",
   "items": [("Inicio insidioso", "1", True), ("Mejora con el ejercicio", "1", True), ("No mejora con el reposo", "1", True),
             ("Dolor nocturno que mejora al levantarse", "1", True), ("Edad de inicio < 40 años", "1", False)],
   "bandas": [("0-3", "No inflamatorio", "Pensar en causa mecánica", False),
              ("4-5", "Inflamatorio", "Rx o RM sacroilíaca, HLA-B27", True)]},
  ["La espondiloartritis es seronegativa: el factor reumatoide es negativo.",
   "La osteoartritis empeora con el movimiento y mejora con el reposo.",
   "Primera línea: AINE y ejercicio; si no responde, anti-TNF."],
  "ASAS-EULAR – Recommendations for the management of axial spondyloarthritis (Ann Rheum Dis 2023)")

# SP-111 · termómetro
V("termometro", "SP-111", "bocio-difuso-huancavelica-sal-yodada", "Bocio endémico en la sierra",
  "SALUD PÚBLICA ENAM: DEFICIENCIA DE YODO", "SALUD PÚBLICA",
  ("Bocio endémico", ["La falta de yodo en suelos altoandinos agranda la tiroides",
   "Estrategia poblacional: yodación universal de la sal"]),
  ("Agricultor de 50 años de Huancavelica", ["Aumento de volumen cervical blando, sin nódulos", "No es un caso aislado en la zona"]),
  {"rotulo": "Grado del bocio (OMS)",
   "niveles": [("Grado 0", "Sin bocio", ["No palpable ni visible"]),
               ("Grado 1", "Palpable", ["No visible con cuello normal"]),
               ("Grado 2", "Visible", ["BOCIO VISIBLE", "Aumento de volumen evidente"])],
   "caso_nivel": 2, "ruta_titulo": "Acción de salud pública", "paso_label": "PASO",
   "pasos": [(1, "Promocionar la sal yodada", ["Medida sostenible para toda la población"], True),
             (2, "Aceite yodado", ["Solo donde no llega la sal yodada"], False),
             (3, "Vigilar la yoduria", ["Indicador del programa"], False)]},
  ["El Perú tiene la yodación de la sal como estrategia nacional desde los años 80.",
   "El déficit de yodo en el embarazo causa cretinismo.",
   "Retirar bociógenos no corrige el déficit de yodo."],
  "OMS – Assessment of iodine deficiency disorders and monitoring their elimination (2007) · MINSA – Lineamientos de nutrición materno infantil")

# CB-055 · tarjetas
V("tarjetas", "CB-055", "alcoholico-gingivorragia-petequias-escorbuto", "Déficit de vitaminas en el alcohólico",
  "CIENCIAS BÁSICAS ENAM: ESCORBUTO", "CIENCIAS BÁSICAS",
  ("Vitamina C y colágeno", ["Sin vitamina C falla la hidroxilación del colágeno",
   "Vasos frágiles: encías que sangran, petequias perifoliculares, equimosis y dolor óseo"]),
  ("Varón alcohólico de 55 años", ["Epistaxis, gingivorragia, equimosis y petequias", "Dolor en la cadera · adelgazado"]),
  {"rotulo": "¿Qué vitamina falta?", "ans": 0, "cards": [
      {"titulo": "VITAMINA C", "datos": [
          ("Encías", "Sangran, hipertróficas", True), ("Piel", "Petequias, equimosis", True),
          ("Hueso", "Dolor, hemartrosis", True), ("Coagulación", "Normal", False)],
       "pie": "Escorbuto"},
      {"titulo": "Vitamina K", "datos": [
          ("Encías", "Pueden sangrar", False), ("Piel", "Equimosis", False),
          ("Hueso", "Sin dolor", False), ("Coagulación", "TP prolongado", False)],
       "pie": "Colestasis, antibióticos"},
      {"titulo": "Vitamina B1", "datos": [
          ("Encías", "Normales", False), ("Piel", "Normal", False),
          ("Hueso", "Sin dolor", False), ("Coagulación", "Normal", False)],
       "pie": "Wernicke, beriberi"},
      {"titulo": "Vitamina B6", "datos": [
          ("Encías", "Queilitis", False), ("Piel", "Dermatitis", False),
          ("Hueso", "Sin dolor", False), ("Coagulación", "Normal", False)],
       "pie": "Neuropatía, anemia sideroblástica"}]},
  ["Con déficit de vitamina C los tiempos de coagulación son normales.",
   "Se trata con ácido ascórbico oral; mejora en días.",
   "En el alcohólico suele coexistir el déficit de varias vitaminas."],
  "Harper. Bioquímica ilustrada 32.ª ed. (2023) · " + HARRISON)

# CAR-053 · termómetro
V("termometro", "CAR-053", "coronario-diabetico-ldl-120-estatina", "Riesgo cardiovascular y LDL",
  "CARDIOLOGÍA ENAM: DISLIPIDEMIA EN EL CORONARIO", "CARDIOLOGÍA",
  ("Tratamiento según riesgo", ["Cuanto mayor el riesgo, más baja la meta de LDL",
   "Enfermedad coronaria establecida = riesgo muy alto: estatina siempre"]),
  ("Varón de 56 años coronario y diabético", ["LDL 120 · HDL 35 · TG 245 mg/dl", "¿Qué fármaco indicar?"]),
  {"rotulo": "Categoría de riesgo",
   "niveles": [("Bajo", "Riesgo bajo", ["LDL < 116"]),
               ("Moderado", "Riesgo moderado", ["LDL < 100"]),
               ("Alto", "Riesgo alto", ["DM sin daño de órgano · LDL < 70"]),
               ("Muy alto", "Riesgo muy alto", ["CORONARIO + DIABÉTICO", "Meta LDL < 55 y bajar ≥ 50 %"])],
   "caso_nivel": 3, "ruta_titulo": "Escalón terapéutico", "paso_label": "PASO",
   "pasos": [(1, "Estatina de alta intensidad", ["Atorvastatina 40-80 o rosuvastatina 20-40 mg"], True),
             (2, "Agregar ezetimiba", ["Si no llega a la meta en 4-6 semanas"], False),
             (3, "Inhibidor de PCSK9", ["Si aún no llega a la meta"], False)]},
  ["La estatina reduce eventos aunque el LDL no esté muy alto.",
   "Los triglicéridos de 245 no justifican fibrato como primera opción.",
   "Controlar transaminasas y CPK si hay síntomas."],
  "ESC/EAS – Guidelines for the management of dyslipidaemias (2019; actualización 2025)")

# END-044 · matriz
V("matriz", "END-044", "trigliceridos-400-dieta-pescado-azul", "Dieta en la hipertrigliceridemia",
  "ENDOCRINOLOGÍA ENAM: HIPERTRIGLICERIDEMIA", "ENDOCRINOLOGÍA",
  ("Grasas de la dieta", ["Los omega-3 del pescado azul bajan los triglicéridos",
   "Las grasas saturadas y los azúcares los suben"]),
  ("Paciente obeso", ["TG 400 · colesterol 210 · HDL 35 · LDL 95", "¿En qué basar la dieta?"]),
  {"rotulo": "Tipo de grasa y efecto", "eje_x": "Rasgo", "eje_y": "Grasa",
   "cols": ["Efecto en triglicéridos", "Ejemplos"], "rows": ["Omega-3", "Monoinsaturada", "Saturada", "Colesterol dietario"], "caso": (0, 0),
   "cells": [[("LOS BAJA", ["20-30 %"]), ("Pescado azul", ["Jurel, caballa, anchoveta"])],
             [("Neutra", ["Mejora el HDL"]), ("Aceite de oliva", ["Aceitunas, palta"])],
             [("Los sube", ["Y sube el LDL"]), ("Coco, manteca", [])],
             [("Sube el LDL", []), ("Vísceras", ["Hígado de pollo"])]]},
  ["Además: bajar de peso, evitar alcohol y azúcares simples.",
   "Con TG ≥ 500 hay riesgo de pancreatitis: fibrato.",
   "El aceite de coco es rico en grasas saturadas."],
  "AHA – Triglycerides and cardiovascular disease scientific statement (Circulation 2021)")

# SP-112 · tarjetas
V("tarjetas", "SP-112", "musica-de-fondo-analgesicos-variables", "Tipos de variables",
  "SALUD PÚBLICA ENAM: VARIABLES DE INVESTIGACIÓN", "SALUD PÚBLICA",
  ("Variables de un estudio", ["Independiente: la que se manipula o expone (causa)",
   "Dependiente: la que se mide como efecto"]),
  ("Estudio en una emergencia ruidosa", ["¿La música de fondo reduce el uso de analgésicos?"]),
  {"rotulo": "¿Qué papel cumple cada variable?", "ans": 0, "cards": [
      {"titulo": "INDEPENDIENTE", "datos": [
          ("Papel", "Causa, se manipula", True), ("En el caso", "MÚSICA DE FONDO", True),
          ("Eje", "Eje X", False)],
       "pie": "El investigador la controla"},
      {"titulo": "Dependiente", "datos": [
          ("Papel", "Efecto, se mide", False), ("En el caso", "Uso de analgésicos", True),
          ("Eje", "Eje Y", False)],
       "pie": "Cambia según la independiente"},
      {"titulo": "Interviniente", "datos": [
          ("Papel", "Puede confundir", False), ("En el caso", "Ruido ambiental", False),
          ("Eje", "Se controla", False)],
       "pie": "Se ajusta en el análisis"},
      {"titulo": "De control", "datos": [
          ("Papel", "Se mantiene fija", False), ("En el caso", "Tipo de dolor", False),
          ("Eje", "Igual en grupos", False)],
       "pie": "Evita sesgos"}]},
  ["Pregunta clave: ¿qué se cambia? (independiente) y ¿qué se mide? (dependiente).",
   "El ruido es una condición del ambiente, no la variable de estudio.",
   "En un ensayo, la intervención siempre es la variable independiente."],
  "Hernández-Sampieri. Metodología de la investigación 7.ª ed. (2023)")

# SP-113 · radial
V("radial", "SP-113", "insomnio-covid-analisis-correlacion", "Qué mide cada análisis",
  "SALUD PÚBLICA ENAM: CORRELACIÓN", "SALUD PÚBLICA",
  ("Análisis estadístico", ["La correlación mide la fuerza y dirección de la asociación entre dos variables",
   "No demuestra causalidad"]),
  ("Aumento de insomnio en una comunidad", ["Tras la muerte de 3 comuneros por COVID-19", "Se usará análisis de correlación"]),
  {"rotulo": "Mapa del tema", "centro": "ANÁLISIS", "centro_sub": "¿Qué identifica?", "ans": 0,
   "items": [("CORRELACIÓN → ASOCIACIÓN", ["Coeficiente r de −1 a +1", "Fuerza y dirección"]),
             ("Regresión → predicción", ["Estima Y a partir de X"]),
             ("t de Student → diferencia", ["Compara 2 medias"]),
             ("ANOVA → diferencia", ["Compara ≥ 3 medias"]),
             ("Desviación estándar", ["Mide la variación"])],
   "ruta": ["Dos variables cuantitativas", "¿Van juntas?", "Coeficiente r", "ASOCIACIÓN"]},
  ["r = 0: no hay asociación lineal; ±1: asociación perfecta.",
   "Pearson para datos normales; Spearman para no normales u ordinales.",
   "Asociación no es causalidad."],
  "Gordis. Epidemiología 6.ª ed. (2019)")

# CB-056 · embudo
V("embudo", "CB-056", "dolor-lanceta-rigidez-abdominal-sudoracion-latrodectismo", "Mordedura o picadura en el campo",
  "CIENCIAS BÁSICAS ENAM: LATRODECTISMO", "CIENCIAS BÁSICAS",
  ("Emponzoñamientos en el Perú", ["Latrodectus (viuda negra): neurotoxina que libera acetilcolina y noradrenalina",
   "Dolor intenso, rigidez muscular y abdominal, sudoración y sialorrea"]),
  ("Niño de 10 años que volvió del campo", ["Dolor urente en lanceta en la pierna; a las 2 h, mialgias y temblor", "Sudoración, sialorrea, rigidez abdominal · lesión rojiza"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dolor local intenso tras estar en el campo",
   "candidatos": ["Latrodectismo", "Loxocelismo", "Escorpionismo", "Leptospirosis"],
   "pasos": [("Sin placa livedoide ni necrosis; cuadro en horas", ["Loxocelismo", "Leptospirosis"]),
             ("Rigidez abdominal y contracturas generalizadas", ["Escorpionismo"])],
   "final": ("LATRODECTISMO", ["Analgesia, gluconato de calcio o benzodiacepina", "Suero antilatrodectus si es grave"]),
   "nota": "La rigidez abdominal simula un abdomen agudo: es típica de la viuda negra."},
  ["Loxocelismo: dolor leve inicial, placa livedoide y posible hemólisis.",
   "Leptospirosis: fiebre, mialgias en pantorrillas, sufusión conjuntival.",
   "Los niños tienen más riesgo de cuadros graves."],
  "MINSA – Norma técnica para la prevención y tratamiento de accidentes por animales ponzoñosos (2004) · Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# HEM-030 · árbol
A("HEM-030", "gestante-hb-8-microcitica-reticulocitos-bajos", "Anemia en la gestante",
  "HEMATOLOGÍA ENAM: ANEMIA FERROPÉNICA", "HEMATOLOGÍA",
  ("Clasificación de las anemias", ["El VCM y los reticulocitos orientan la causa",
   "Microcítica, hipocrómica, anisocitosis y reticulocitos bajos = ferropénica"]),
  ("Gestante de 6 meses con palidez", ["Hb 8 g/dl · constantes corpusculares bajas", "Anisocitosis, hipocromía, microcitos, reticulocitos bajos"]),
  Q("¿Cómo está el VCM?", [
      L("Bajo (< 80 fl)", "FERROPÉNICA", ["Ferritina baja, ADE alto", "Hierro oral + ácido fólico"], path=True),
      L("Normal, reticulocitos altos", "Hemolítica", ["LDH y bilirrubina altas"]),
      L("Normal, reticulocitos bajos", "Aplásica", ["Pancitopenia"]),
      L("Alto (> 100 fl)", "Megaloblástica", ["B12 (perniciosa) o folato"])], path=True),
  ("Anemias microcíticas", [("Ferropénica", True), ("Talasemia", False)], [
      ("Ferritina", ["Baja", "Normal o alta"]),
      ("ADE", ["Alto", "Normal"]),
      ("Glóbulos rojos", ["Bajos", "Normales o altos"])]),
  ["En la gestación la anemia es Hb < 11 g/dl; con 8 g/dl es moderada.",
   "MINSA: suplementar hierro + ácido fólico desde la semana 14.",
   "La causa más frecuente de anemia en la gestante es la ferropénica."],
  "MINSA – NTS 213: Prevención y control de la anemia por deficiencia de hierro (2024) · " + WILLIAMS)

# SP-114 · árbol
A("SP-114", "personal-salud-enfermedad-profesional-biologica", "¿Es enfermedad profesional?",
  "SALUD PÚBLICA ENAM: ENFERMEDADES PROFESIONALES EN SALUD", "SALUD PÚBLICA",
  ("Enfermedad profesional", ["Se adquiere como consecuencia directa del trabajo o de su ambiente",
   "En salud: riesgo biológico por sangre, fluidos y aerosoles"]),
  ("Personal de salud", ["¿Qué infecciones se consideran profesionales?"]),
  Q("¿Se adquiere por la tarea asistencial?", [
      L("Sí: sangre, fluidos o aerosoles", "PROFESIONALES", ["Hepatitis B y C, VIH", "Tuberculosis, COVID-19"], path=True),
      L("No: vector o comunidad", "Enfermedad común", ["Dengue, malaria", "Fiebre amarilla"])], path=True),
  ("Riesgo biológico", [("Hepatitis/VIH", True), ("TB/COVID-19", True), ("Dengue/malaria", False)], [
      ("Vía", ["Pinchazo, salpicadura", "Aérea, gotas", "Mosquito"]),
      ("Prevención", ["Vacuna VHB, bioseguridad", "N95, ventilación", "Control vectorial"])]),
  ["La vacuna contra hepatitis B es obligatoria para el personal de salud.",
   "Tras un pinchazo con VIH: profilaxis en las primeras 72 h (ideal < 2 h).",
   "El trabajador con TB o COVID-19 adquiridos en servicio tiene cobertura del seguro."],
  "MINSA – Documento técnico: Lineamientos de salud ocupacional para trabajadores de salud · DS 009-97-SA (SCTR)")

# GIN-147 · árbol
A("GIN-147", "embarazo-gemelar-termino-presentacion-via-parto", "Parto gemelar: ¿vaginal o cesárea?",
  "OBSTETRICIA ENAM: EMBARAZO MÚLTIPLE", "OBSTETRICIA",
  ("Vía del parto gemelar", ["La presentación de los fetos define el manejo intraparto",
   "Cefálico-cefálico: parto vaginal posible"]),
  ("Embarazo múltiple a término", ["¿Qué determina el manejo intraparto?"]),
  Q("¿Monoamniótico?", [
      L("Sí", "Cesárea", ["Riesgo de entrelazamiento de cordones"]),
      Q("¿Presentación del primer gemelo?", [
          L("Cefálico-cefálico", "PARTO VAGINAL", ["Monitoreo de ambos fetos"], path=True),
          L("Cefálico-no cefálico", "Vaginal o cesárea", ["Según experiencia y peso"]),
          L("Primero no cefálico", "Cesárea", ["Riesgo de enganche"])],
        edge="No", path=True)], path=True),
  ("Tipos de gemelos", [("Bicorial", False), ("Monocorial", False), ("Monoamniótico", False)], [
      ("Riesgo", ["El menor", "Transfusión feto-fetal", "Cordones"]),
      ("Parto", ["37-38 semanas", "36-37 semanas", "32-34 semanas, cesárea"])]),
  ["El tamaño de los gemelos importa, pero la presentación es lo que define la vía.",
   "Tras nacer el primer gemelo, el segundo puede cambiar de posición.",
   "El intervalo entre ambos nacimientos debe ser corto."],
  "ACOG – Practice Bulletin 231: Multifetal gestations (2021) · " + WILLIAMS)

# GIN-148 · matriz
V("matriz", "GIN-148", "fiebre-31-semanas-taquicardia-fetal-no-tocolisis", "Corioamnionitis: qué dar y qué no",
  "OBSTETRICIA ENAM: CORIOAMNIONITIS", "OBSTETRICIA",
  ("Infección intraamniótica", ["Fiebre materna + taquicardia fetal = corioamnionitis",
   "Hay que terminar el embarazo: la tocólisis está contraindicada"]),
  ("Gestante de 31 semanas con fiebre de 39 °C", ["Contracciones esporádicas", "Latidos fetales 165/min"]),
  {"rotulo": "Fármacos en este caso", "eje_x": "Rasgo", "eje_y": "Fármaco",
   "cols": ["¿Se indica?", "Motivo"], "rows": ["Tocolíticos", "Antibióticos", "Corticoides", "Sulfato de magnesio"], "caso": (0, 0),
   "cells": [[("NO: CONTRAINDICADO", []), ("Prolongan la infección", ["Sepsis materna y fetal"])],
             [("Sí", []), ("Ampicilina + gentamicina", [])],
             [("Sí", ["< 34 semanas"]), ("Maduración pulmonar", [])],
             [("Sí", ["< 32 semanas"]), ("Neuroprotección fetal", [])]]},
  ["La corioamnionitis se trata con antibióticos y parto, no con cesárea obligada.",
   "Signos: fiebre, taquicardia materna y fetal, útero doloroso, líquido fétido.",
   "Tras el parto vaginal no se requiere seguir antibióticos."],
  "ACOG – Committee Opinion 712: Intrapartum management of intraamniotic infection (2017) · " + WILLIAMS)

# GIN-149 · fases
V("fases", "GIN-149", "primigesta-3-cm-fase-latente-deambular", "Fases del trabajo de parto",
  "OBSTETRICIA ENAM: FASE LATENTE DEL TRABAJO DE PARTO", "OBSTETRICIA",
  ("Trabajo de parto", ["Fase latente: hasta 5 cm, lenta y variable", "Fase activa: desde 6 cm (OMS 2018)"]),
  ("Primigesta de 39 semanas", ["Dinámica adecuada · 3 cm · presentación en −2", "Pelvis adecuada · feto 140/min"]),
  {"rotulo": "Curso del trabajo de parto", "ans": 0,
   "fases": [("Latente", "0-5 cm", "DEAMBULAR Y ESPERAR", ["No hospitalizar aún", "Control de LCF"]),
             ("Activa", "6-10 cm", "Hospitalizar", ["Partograma"]),
             ("Expulsivo", "10 cm → parto", "Pujos", ["Hasta 3 h en primípara"]),
             ("Alumbramiento", "Placenta", "Manejo activo", ["Oxitocina 10 UI"])],
   "curvas": [("Dilatación", VIOLET, [0.05, 0.12, 0.2, 0.3, 0.55, 0.8, 0.95, 1.0, 1.0])],
   "chips_titulo": "Indicación · marcada la correcta",
   "chips": [("Deambular hasta fase activa", True), ("Cesárea", False), ("Oxitocina", False), ("Hospitalizar e hidratar", False)]},
  ["Hospitalizar en fase latente aumenta intervenciones innecesarias.",
   "La estimulación con oxitocina no se usa en una fase latente normal.",
   "Conjugado diagonal de 12,5 cm: pelvis adecuada."],
  "OMS – Recomendaciones para los cuidados durante el parto (2018) · " + WILLIAMS)

# END-045 · termómetro
V("termometro", "END-045", "insulina-glucosa-38-desorientado-dextrosa-33", "Hipoglucemia: gravedad",
  "ENDOCRINOLOGÍA ENAM: HIPOGLUCEMIA GRAVE", "ENDOCRINOLOGÍA",
  ("Hipoglucemia en el diabético", ["Se clasifica por glucosa y por el estado mental",
   "Con desorientación no puede tomar azúcar oral: glucosa EV"]),
  ("Varón de 59 años con insulina", ["3 h después de la dosis: sudoración, palidez, desorientación", "Glucosa capilar 38 mg/dl"]),
  {"rotulo": "Nivel de hipoglucemia",
   "niveles": [("< 70", "Nivel 1", ["Alerta, síntomas leves"]),
               ("< 54", "Nivel 2", ["Neuroglucopenia"]),
               ("Grave", "Nivel 3", ["DESORIENTADO: necesita ayuda", "Cualquier cifra con alteración mental"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Dextrosa al 33 % EV", ["En bolo; si no hay vía: glucagón IM"], True),
             (2, "Infusión de dextrosa al 10 %", ["Evita la recaída"], False),
             (3, "Buscar la causa", ["Dosis, comida omitida, función renal"], False)]},
  ["Consciente y capaz de tragar: 15-20 g de glucosa oral (regla 15-15).",
   "Dextrosa al 5 % aporta muy poca glucosa para una emergencia.",
   "Con sulfonilureas la hipoglucemia puede durar horas: observar."],
  "ADA – Standards of Care in Diabetes 2025: Glycemic goals and hypoglycemia")

# GIN-150 · radial
V("radial", "GIN-150", "obesidad-pregestacional-diabetes-macrosomia", "Obesidad y embarazo",
  "OBSTETRICIA ENAM: OBESIDAD PREGESTACIONAL", "OBSTETRICIA",
  ("Obesidad antes del embarazo", ["La resistencia a la insulina favorece la diabetes gestacional",
   "La hiperglucemia materna produce hiperinsulinismo fetal y macrosomía"]),
  ("Pregunta de riesgo", ["Obesidad no corregida antes de gestar"]),
  {"rotulo": "Mapa del tema", "centro": "OBESIDAD MATERNA", "centro_sub": "Complicaciones", "ans": 0,
   "items": [("DIABETES Y MACROSOMÍA", ["La asociación más típica", "Hiperinsulinismo fetal"]),
             ("Preeclampsia", ["Riesgo 2-3 veces mayor"]),
             ("Defectos del tubo neural", ["Ácido fólico 4 mg"]),
             ("Cesárea e infección", ["Más partos operatorios"]),
             ("Muerte fetal", ["Mayor riesgo al término"])],
   "ruta": ["IMC ≥ 30 antes de gestar", "Resistencia a la insulina", "Hiperglucemia materna", "DIABETES Y MACROSOMÍA"]},
  ["La RCIU no es la complicación típica de la obesidad.",
   "Tamizar diabetes en la primera consulta si hay obesidad.",
   "Ideal: bajar de peso antes de embarazarse."],
  "ACOG – Practice Bulletin 230: Obesity in pregnancy (2021) · " + WILLIAMS)

# GIN-151 · tarjetas
V("tarjetas", "GIN-151", "lupus-antifosfolipidos-anticoncepcion-diu-cobre", "Anticoncepción en el lupus",
  "GINECOLOGÍA ENAM: ANTICONCEPCIÓN EN LES", "GINECOLOGÍA",
  ("Criterios de elegibilidad de la OMS", ["Con anticuerpos antifosfolípidos, los estrógenos están prohibidos (categoría 4)",
   "El DIU de cobre no tiene hormonas: categoría 1"]),
  ("Mujer de 27 años, nulípara", ["Lupus con anticuerpos antifosfolípidos", "Pide un método anticonceptivo"]),
  {"rotulo": "¿Qué método le conviene?", "ans": 0, "cards": [
      {"titulo": "DIU T DE COBRE", "datos": [
          ("Hormonas", "Ninguna", True), ("Trombosis", "Sin riesgo", True),
          ("OMS con AAF", "Categoría 1", True), ("Reversible", "Sí", True)],
       "pie": "Eficaz 10-12 años"},
      {"titulo": "AOC", "datos": [
          ("Hormonas", "Estrógeno + progestágeno", False), ("Trombosis", "Aumenta", False),
          ("OMS con AAF", "Categoría 4", False), ("Reversible", "Sí", False)],
       "pie": "Contraindicado"},
      {"titulo": "Minipíldora", "datos": [
          ("Hormonas", "Solo progestágeno", False), ("Trombosis", "Riesgo teórico", False),
          ("OMS con AAF", "Categoría 3", False), ("Reversible", "Sí", False)],
       "pie": "Menos eficaz, horario estricto"},
      {"titulo": "Ligadura tubárica", "datos": [
          ("Hormonas", "Ninguna", False), ("Trombosis", "Sin riesgo", False),
          ("OMS con AAF", "Categoría 1", False), ("Reversible", "No", False)],
       "pie": "No ideal en nulípara joven"}]},
  ["Todos los métodos de solo progestágeno son categoría 3 con AAF positivos.",
   "El lupus sin AAF permite progestágenos y DIU hormonal.",
   "El embarazo en el LES debe planificarse con la enfermedad inactiva."],
  "OMS – Criterios médicos de elegibilidad para el uso de anticonceptivos 5.ª ed. (2015) · CDC – US MEC (2024)")

# CB-057 · radial
V("radial", "CB-057", "covid-perdida-gusto-celulas-neuroepiteliales", "Receptores del gusto",
  "CIENCIAS BÁSICAS ENAM: CÉLULAS GUSTATIVAS", "CIENCIAS BÁSICAS",
  ("Botón gustativo", ["Las células receptoras del gusto son neuroepiteliales",
   "Hacen sinapsis con fibras de los pares VII, IX y X"]),
  ("Paciente con COVID-19", ["Pierde el sentido del gusto", "¿Qué células tienen los receptores?"]),
  {"rotulo": "Mapa del tema", "centro": "BOTÓN GUSTATIVO", "centro_sub": "Tipos de células", "ans": 0,
   "items": [("NEUROEPITELIALES", ["Células receptoras (tipo II y III)", "Captan las moléculas del sabor"]),
             ("Células de sostén", ["Tipo I, rodean a las receptoras"]),
             ("Células basales", ["Madre: renuevan cada 10 días"]),
             ("Fibras nerviosas", ["VII (2/3 ant.), IX (1/3 post.), X"]),
             ("Neuroblastos", ["Precursor embrionario"])],
   "ruta": ["Molécula del sabor", "Poro gustativo", "Receptor en la célula", "NEUROEPITELIAL"]},
  ["El olfato también usa células neuroepiteliales (neuronas olfatorias bipolares).",
   "En la COVID-19 se afectan sobre todo las células de sostén del epitelio olfatorio.",
   "El gusto se renueva constantemente gracias a las células basales."],
  "Ross. Histología: texto y atlas 8.ª ed. (2020) · Guyton y Hall. Fisiología médica 14.ª ed. (2021)")

# NRL-042 · tarjetas
V("tarjetas", "NRL-042", "ptosis-diplopia-placa-mioneural-receptor-acetilcolina", "Placa neuromuscular: dónde falla",
  "NEUROLOGÍA ENAM: MIASTENIA GRAVIS", "NEUROLOGÍA",
  ("Unión neuromuscular", ["Miastenia gravis: anticuerpos que destruyen los receptores de acetilcolina",
   "Debilidad fluctuante que empeora con el esfuerzo: ptosis y diplopía"]),
  ("Mujer de 56 años", ["Caída progresiva de párpados y visión doble", "Enfermedad autoinmune de la placa"]),
  {"rotulo": "¿Qué defecto molecular?", "ans": 0, "cards": [
      {"titulo": "MIASTENIA GRAVIS", "datos": [
          ("Sitio", "Postsináptico", True), ("Defecto", "Receptor de ACh", True),
          ("Esfuerzo", "Empeora", True), ("Reflejos", "Normales", False)],
       "pie": "Piridostigmina, timectomía"},
      {"titulo": "Lambert-Eaton", "datos": [
          ("Sitio", "Presináptico", False), ("Defecto", "Canal de calcio", False),
          ("Esfuerzo", "Mejora al inicio", False), ("Reflejos", "Disminuidos", False)],
       "pie": "Buscar cáncer de pulmón"},
      {"titulo": "Botulismo", "datos": [
          ("Sitio", "Presináptico", False), ("Defecto", "Liberación de ACh", False),
          ("Esfuerzo", "Parálisis descendente", False), ("Reflejos", "Disminuidos", False)],
       "pie": "Antitoxina"},
      {"titulo": "Organofosforados", "datos": [
          ("Sitio", "Hendidura", False), ("Defecto", "Inhiben colinesterasa", False),
          ("Esfuerzo", "Fasciculaciones", False), ("Reflejos", "Variables", False)],
       "pie": "Atropina + pralidoxima"}]},
  ["El 85 % tiene anticuerpos anti-receptor de acetilcolina.",
   "Buscar timoma con TC de tórax.",
   "Crisis miasténica: insuficiencia respiratoria; plasmaféresis o inmunoglobulina."],
  "AAN/MGFA – International consensus guidance for management of myasthenia gravis (Neurology 2021)")

# GIN-152 · matriz
V("matriz", "GIN-152", "hta-cronica-gestante-captopril-metildopa", "Antihipertensivos en el embarazo",
  "OBSTETRICIA ENAM: HIPERTENSIÓN CRÓNICA EN LA GESTANTE", "OBSTETRICIA",
  ("Hipertensión crónica", ["PA ≥ 140/90 antes de las 20 semanas", "Los IECA son teratógenos: cambiar al saber del embarazo"]),
  ("Gestante de 39 años, 10 semanas", ["PA 150/95 · usaba captopril", "¿Qué antihipertensivo es más seguro?"]),
  {"rotulo": "Fármaco y uso en la gestación", "eje_x": "Rasgo", "eje_y": "Fármaco",
   "cols": ["Uso en el embarazo", "Nota"], "rows": ["Metildopa", "Nifedipino", "Hidralazina", "Captopril"], "caso": (0, 0),
   "cells": [[("PRIMERA LÍNEA ORAL", ["Tratamiento crónico"]), ("Más experiencia", ["Seguridad fetal"])],
             [("Alternativa oral", ["Acción prolongada"]), ("También en crisis", [])],
             [("Solo en crisis", ["Vía EV"]), ("No es de uso crónico", [])],
             [("CONTRAINDICADO", []), ("Oligohidramnios", ["Daño renal fetal"])]]},
  ["Labetalol y nifedipino también son de primera línea en guías internacionales.",
   "Iniciar aspirina 100 mg desde las 12 semanas para prevenir preeclampsia.",
   "Suspender IECA y ARA II apenas se confirma el embarazo."],
  "MINSA – Guía de práctica clínica de trastornos hipertensivos del embarazo · ACOG – Practice Bulletin 203: Chronic hypertension in pregnancy (2019)")

# GIN-153 · matriz
V("matriz", "GIN-153", "gestante-16-anos-riesgo-menor-diabetes", "Riesgos del embarazo adolescente",
  "OBSTETRICIA ENAM: EMBARAZO ADOLESCENTE", "OBSTETRICIA",
  ("Embarazo en la adolescencia", ["Más anemia, preeclampsia, parto pretérmino y bajo peso",
   "La diabetes gestacional es menos frecuente que en mayores"]),
  ("Gestante de 16 años, 15 semanas", ["¿A qué complicación está menos expuesta?"]),
  {"rotulo": "Riesgo en la adolescente", "eje_x": "Rasgo", "eje_y": "Complicación",
   "cols": ["Riesgo", "Por qué"], "rows": ["Diabetes", "Anemia", "Preeclampsia", "Parto pretérmino"], "caso": (0, 0),
   "cells": [[("MENOR", []), ("Menos resistencia a la insulina", ["Aumenta con la edad"])],
             [("Mayor", []), ("Dieta pobre, crecimiento", [])],
             [("Mayor", []), ("Primigesta joven", [])],
             [("Mayor", []), ("Inmadurez, control tardío", [])]]},
  ["Los extremos de la vida reproductiva tienen más riesgos, pero distintos.",
   "La edad avanzada se asocia a diabetes, HTA y cromosomopatías.",
   "Iniciar control prenatal y suplemento de hierro temprano."],
  "OMS – Embarazo en la adolescencia: nota descriptiva (2024) · " + WILLIAMS)

# CIR-087 · termómetro
V("termometro", "CIR-087", "dolor-pantorrillas-al-caminar-cede-reposo-claudicacion", "Enfermedad arterial periférica",
  "CIRUGÍA ENAM: CLAUDICACIÓN INTERMITENTE", "CIRUGÍA",
  ("Isquemia crónica de miembros inferiores", ["Dolor al caminar que cede de inmediato al reposo = claudicación",
   "Clasificación de Fontaine según síntomas"]),
  ("Varón de 74 años, diabético e hipertenso", ["Dolor de pantorrillas al andar que calma al detenerse", "Pulso pedio disminuido · estenosis < 50 %"]),
  {"rotulo": "Estadio de Fontaine",
   "niveles": [("I", "Asintomático", ["Pulsos disminuidos"]),
               ("II", "Claudicación", ["CLAUDICACIÓN INTERMITENTE", "IIa > 200 m · IIb < 200 m"]),
               ("III", "Dolor en reposo", ["Nocturno, alivia colgando la pierna"]),
               ("IV", "Úlcera o gangrena", ["Isquemia crítica"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Ejercicio supervisado + riesgo vascular", ["Dejar de fumar, estatina, antiagregante", "Cilostazol si limita"], True),
             (2, "Índice tobillo-brazo", ["< 0,9 confirma"], False),
             (3, "Revascularizar", ["En III-IV o claudicación invalidante"], False)]},
  ["Claudicación venosa: dolor que no cede rápido, mejora al elevar la pierna.",
   "El síndrome compartimental crónico es de deportistas jóvenes.",
   "En diabéticos el ITB puede salir falsamente alto por calcificación."],
  "ESC – Guidelines for the management of peripheral arterial and aortic diseases (2024)")

# NEF-068 · árbol
A("NEF-068", "psa-11-gleason-bajo-localizado-prostatectomia", "Cáncer de próstata localizado",
  "UROLOGÍA ENAM: CÁNCER DE PRÓSTATA", "UROLOGÍA",
  ("Tratamiento del cáncer de próstata", ["Depende de la extensión, el riesgo y la expectativa de vida",
   "Localizado con buena expectativa de vida: prostatectomía radical"]),
  ("Varón de 65 años con padre fallecido por cáncer de próstata", ["Próstata indurada · PSA 11,5 · Gleason bajo", "TC: sin extensión fuera de la próstata"]),
  Q("¿Está confinado a la próstata?", [
      Q("¿Expectativa de vida > 10 años?", [
          L("Sí", "PROSTATECTOMÍA RADICAL", ["O radioterapia radical", "Intención curativa"], path=True),
          L("No", "Vigilancia o radioterapia", ["Según síntomas"])],
        edge="Sí", path=True),
      L("Localmente avanzado", "Radioterapia + hormonas", ["Bloqueo androgénico"]),
      L("Metastásico", "Terapia hormonal", ["± quimioterapia"])], path=True),
  ("Grupos de riesgo (D'Amico)", [("Bajo", False), ("Intermedio", True), ("Alto", False)], [
      ("PSA", ["< 10", "10-20", "> 20"]),
      ("Gleason", ["≤ 6", "7", "≥ 8"]),
      ("Tacto", ["T1-T2a", "T2b", "T2c-T3"])]),
  ["La orquidectomía y la quimioterapia son para enfermedad avanzada.",
   "El antecedente de padre con cáncer duplica el riesgo.",
   "Riesgo muy bajo y mayor edad: la vigilancia activa es opción."],
  "EAU – Guidelines on prostate cancer (2025) · NCCN – Prostate cancer (2025)")

# CIR-088 · fases
V("fases", "CIR-088", "hernia-crural-estrangulada-reducida-anestesia-laparotomia", "Hernia estrangulada que se reduce",
  "CIRUGÍA ENAM: HERNIA CRURAL ESTRANGULADA", "CIRUGÍA",
  ("Hernia crural complicada", ["Es la que más se estrangula", "Si se reduce sola en la anestesia, hay que revisar el asa dentro del abdomen"]),
  ("Mujer de 38 años", ["Hernia crural derecha probablemente estrangulada", "Se reduce sin querer al inducir la anestesia"]),
  {"rotulo": "Secuencia quirúrgica", "ans": 1,
   "fases": [("Sospecha", "Preoperatorio", "Estrangulación", ["Dolor, irreductible, obstrucción"]),
             ("Reducción", "Anestesia", "LAPAROTOMÍA MEDIANA", ["El asa entró sin revisar", "Explorar toda la cavidad"]),
             ("Viabilidad", "Intraoperatorio", "Revisar el asa", ["Resecar si está necrótica"]),
             ("Reparación", "Final", "Cierre del orificio", ["Sin malla si hay contaminación"])],
   "curvas": [],
   "chips_titulo": "Abordaje · marcado el correcto",
   "chips": [("Laparotomía mediana", True), ("Inguinal derecha", False), ("Paramediana", False), ("Posterior", False)]},
  ["El riesgo es dejar un asa necrótica dentro del abdomen: peritonitis.",
   "La mediana permite revisar todo el intestino; la laparoscopia es alternativa.",
   "La hernia crural es más frecuente en mujeres y siempre se opera."],
  "HerniaSurge Group – International guidelines for groin hernia management (Hernia 2018; actualización 2023) · WSES – Guidelines for emergency repair of complicated abdominal wall hernias (2017)")

# CIR-089 · embudo
V("embudo", "CIR-089", "herida-precordial-triada-beck-taponamiento", "Trauma torácico penetrante con choque",
  "CIRUGÍA ENAM: TAPONAMIENTO CARDIACO", "CIRUGÍA",
  ("Choque obstructivo en trauma", ["Herida precordial + tríada de Beck = taponamiento",
   "Beck: hipotensión, yugulares ingurgitadas, ruidos cardiacos apagados"]),
  ("Varón de 27 años con herida punzopenetrante precordial", ["Pálido, disneico e hipotenso", "Yugulares ingurgitadas · ruidos cardiacos apagados"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Herida torácica con hipotensión",
   "candidatos": ["Taponamiento", "Neumotórax a tensión", "Hemotórax", "Neumotórax simple"],
   "pasos": [("Yugulares ingurgitadas (choque obstructivo)", ["Hemotórax", "Neumotórax simple"]),
             ("Ruidos apagados; murmullo y percusión conservados", ["Neumotórax a tensión"])],
   "final": ("TAPONAMIENTO CARDIACO", ["FAST pericárdico", "Toracotomía; pericardiocentesis como puente"]),
   "nota": "El hemotórax masivo da yugulares planas; el neumotórax a tensión, hiperresonancia y desviación traqueal."},
  ["Con 50-100 ml de sangre rápida en el pericardio basta para el choque.",
   "El pulso paradójico apoya el diagnóstico.",
   "Reponer volumen solo mientras se prepara la descompresión."],
  ATLS)

# NRL-043 · termómetro
V("termometro", "NRL-043", "hemorragia-fosa-posterior-compresion-tronco", "Hemorragia de fosa posterior",
  "NEUROLOGÍA ENAM: HEMORRAGIA CEREBELOSA", "NEUROLOGÍA",
  ("Hemorragia de la fosa posterior", ["La fosa posterior es pequeña: poco sangrado comprime el tronco y bloquea el LCR",
   "Deterioro o compresión del tronco = cirugía urgente"]),
  ("Varón de 65 años", ["Hemorragia en fosa posterior con compresión del tronco", "Agitación, obnubilación progresiva, hipertensión endocraneana"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "< 3 cm, sin compresión", ["Vigilancia en UCI"]),
               ("Moderada", "Hidrocefalia", ["Ventriculostomía"]),
               ("Grave", "Compresión del tronco", ["COMPRESIÓN + DETERIORO", "Emergencia neuroquirúrgica"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Ventriculostomía + craniectomía suboccipital", ["Descomprime el tronco y drena el LCR"], True),
             (2, "Soporte en UCI", ["Vía aérea, control de PA"], False),
             (3, "Manitol o hiperventilación", ["Solo como puente breve"], False)]},
  ["Hematoma cerebeloso > 3 cm, compresión del tronco o hidrocefalia: cirugía.",
   "La ventriculostomía sola puede causar herniación hacia arriba.",
   "La angiografía se reserva si se sospecha malformación vascular."],
  "AHA/ASA – Guideline for the management of spontaneous intracerebral hemorrhage (Stroke 2022)")

# CB-058 · embudo
V("embudo", "CB-058", "coma-bradipnea-flumazenilo-ineficaz-barbituricos", "Coma tóxico en una adolescente",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR BARBITÚRICOS", "CIENCIAS BÁSICAS",
  ("Depresión del SNC por fármacos", ["Barbitúricos: coma profundo, hipotermia, depresión respiratoria",
   "No responden a flumazenilo, que solo revierte benzodiacepinas"]),
  ("Mujer de 19 años hallada en su cuarto tras una discusión", ["Piel fría, coma profundo, miosis, bradipnea y cianosis", "Sin mejoría con flumazenilo"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Coma con depresión respiratoria",
   "candidatos": ["Barbitúricos", "Benzodiacepinas", "Carbamatos", "Fenitoína"],
   "pasos": [("Sin sialorrea, broncorrea ni fasciculaciones", ["Carbamatos"]),
             ("Sin mejoría con flumazenilo", ["Benzodiacepinas"]),
             ("Coma profundo con apnea: no es típico de fenitoína", ["Fenitoína"])],
   "final": ("BARBITÚRICOS", ["Vía aérea y ventilación", "Carbón activado; alcalinizar orina (fenobarbital)"]),
   "nota": "Las benzodiacepinas solas rara vez causan coma profundo con apnea."},
  ["No hay antídoto para barbitúricos: el soporte es el tratamiento.",
   "Fenitoína: nistagmo, ataxia, disartria.",
   "Carbamatos y organofosforados: síndrome colinérgico con miosis y secreciones."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# NEU-041 · puntaje
V("puntaje", "NEU-041", "hospitalizado-disnea-subita-hipoxemia-rx-normal-tep", "Disnea súbita en el hospitalizado",
  "NEUMOLOGÍA ENAM: TROMBOEMBOLISMO PULMONAR", "NEUMOLOGÍA",
  ("Tromboembolismo pulmonar", ["Disnea súbita + hipoxemia + Rx normal = sospechar TEP",
   "La escala de Wells estima la probabilidad"]),
  ("Paciente hospitalizado", ["Disnea súbita e hipoxemia", "Se descarta problema coronario · Rx normal"]),
  {"rotulo": "Escala de Wells en el caso", "escala": "Wells para TEP", "total": 4.5, "max": 12.5,
   "total_label": "Puntaje del caso",
   "interpreta": "TEP probable: angio-TC",
   "items": [("TEP es el diagnóstico más probable", "3", True), ("Inmovilización o cirugía reciente", "1,5", True),
             ("Signos de trombosis venosa profunda", "3", False), ("FC > 100 lpm", "1,5", False),
             ("TEP o TVP previa", "1,5", False), ("Hemoptisis", "1", False), ("Cáncer activo", "1", False)],
   "bandas": [("≤ 4", "Improbable", "Dímero D; si es negativo, se descarta", False),
              ("> 4", "Probable", "Angio-TC de tórax", True)]},
  ["Una Rx normal con hipoxemia marcada es muy sugestiva de TEP.",
   "Si hay inestabilidad hemodinámica: ecocardiograma y trombólisis.",
   "Anticoagular mientras se confirma si la sospecha es alta."],
  "ESC – Guidelines for the diagnosis and management of acute pulmonary embolism (2019)")

# CAR-054 · embudo
V("embudo", "CAR-054", "hta-brazos-pulso-femoral-debil-coartacion", "Hipertensión en el joven",
  "CARDIOLOGÍA ENAM: COARTACIÓN DE AORTA", "CARDIOLOGÍA",
  ("Hipertensión secundaria en el joven", ["HTA en brazos con pulsos femorales débiles = coartación",
   "Soplo sistólico que se irradia a la espalda"]),
  ("Varón de 28 años en evaluación prequirúrgica", ["PA 200/135 en brazos · pulso femoral pequeño", "Soplo sistólico II/VI irradiado a la espalda"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "HTA grave en un adulto joven",
   "candidatos": ["Coartación", "Estenosis aórtica", "Takayasu", "HTA esencial", "Estenosis mitral"],
   "pasos": [("Pulso femoral débil: diferencia brazos-piernas", ["HTA esencial", "Estenosis mitral"]),
             ("Soplo a la espalda, varón sin síntomas sistémicos", ["Estenosis aórtica", "Takayasu"])],
   "final": ("COARTACIÓN DE AORTA", ["Angio-TC o RM confirma", "Stent o cirugía"]),
   "nota": "En la Rx: muescas costales (signo de Roesler) y signo del 3."},
  ["Medir PA en las cuatro extremidades en todo joven hipertenso.",
   "Se asocia a válvula aórtica bicúspide y síndrome de Turner.",
   "Takayasu: mujer joven con pulsos débiles en los brazos."],
  "ESC – Guidelines for the management of adult congenital heart disease (2020)")
