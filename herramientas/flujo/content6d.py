"""Bloque 6 · parte D."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"

# GIN-093 · fases
V("fases", "GIN-093", "vasa-previa-cesarea-34-35-semanas", "Vasa previa: momento del parto",
  "OBSTETRICIA ENAM: VASA PREVIA", "OBSTETRICIA",
  ("Vasa previa", ["Vasos fetales sin protección cruzan sobre el orificio cervical interno",
   "Si se rompen, sangra el feto: se programa cesárea antes del trabajo de parto"]),
  ("Primigesta de 24 semanas", ["Gestación única, placenta fúndica posterior", "Ecografía: vasa previa"]),
  {"rotulo": "Plan según la edad gestacional", "ans": 2,
   "fases": [("Diagnóstico", "2.º trim.", "Eco Doppler TV", ["Vasos sobre el OCI"]),
             ("Vigilancia", "28-34 sem", "Corticoides", ["Hospitalizar a las 30-34 sem"]),
             ("Parto", "34-35 sem", "CESÁREA PROGRAMADA", ["Antes de la labor de parto"]),
             ("Urgencia", "Si sangra", "Cesárea inmediata", ["Sangre fetal: alta mortalidad"])],
   "curvas": [("Riesgo", ROSE, [0.05, 0.1, 0.2, 0.35, 0.55, 0.75, 0.9])],
   "chips_titulo": "Momento del parto · marcado el correcto",
   "chips": [("Cesárea 34-35 sem", True), ("Cesárea 38 sem", False), ("Inducir a las 37 sem", False), ("Esperar labor", False)]},
  ["El riesgo es la rotura de membranas: desgarra los vasos y el feto se desangra.",
   "No se hacen tactos vaginales ni amniotomía.",
   "Placenta baja, bilobulada o inserción velamentosa aumentan el riesgo."],
  "SMFM – Consult Series N.° 37: Diagnosis and management of vasa previa (2015) · " + WILLIAMS)

# PED-105 · fases
V("fases", "PED-105", "lejia-estridor-sialorrea-intubacion", "Ingesta de cáusticos en el niño",
  "PEDIATRÍA ENAM: INGESTA DE CÁUSTICOS", "PEDIATRÍA",
  ("Ingesta de cáusticos", ["Lo primero es la vía aérea: el estridor anuncia edema laríngeo",
   "No se provoca vómito, no se lava ni se da carbón activado"]),
  ("Niño de 3 años que ingirió lejía hace 20 minutos", ["Estridor, sialorrea, mucosa oral eritematosa", "FR 40 · SatO₂ 91%"]),
  {"rotulo": "Evolución y manejo", "ans": 0,
   "fases": [("Ingreso", "0-6 h", "VÍA AÉREA", ["Estridor: intubar"]),
             ("Evaluación", "12-48 h", "Endoscopia", ["Clasificación de Zargar"]),
             ("Cicatriza", "Semanas", "Vigilar estenosis", ["Dilataciones"]),
             ("Secuela", "Años", "Riesgo de cáncer", ["Carcinoma escamoso"])],
   "curvas": [],
   "chips_titulo": "Tratamiento inicial · marcado el correcto",
   "chips": [("Intubación", True), ("Carbón activado", False), ("Lavado gástrico", False), ("Corticoides EV", False)]},
  ["Intubación bajo visión directa: nunca a ciegas.",
   "El carbón no adsorbe cáusticos y oscurece la endoscopia.",
   "Álcalis (lejía, soda): necrosis por licuefacción, más daño esofágico."],
  NELSON + " · ESPGHAN – Position paper on caustic ingestion in children (JPGN 2021)")

# PSI-018 · embudo
V("embudo", "PSI-018", "voces-le-quieren-hacer-dano-psicosis", "Mujer joven que oye voces",
  "PSIQUIATRÍA ENAM: PSICOSIS", "PSIQUIATRÍA",
  ("Psicosis", ["Pérdida del juicio de realidad: delirios y alucinaciones",
   "La conciencia y la orientación suelen estar conservadas"]),
  ("Mujer de 24 años con 4 meses de evolución", ["Falta al trabajo, descuida su aseo", "Cree que le quieren hacer daño · escucha voces"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Joven que deja de trabajar y oye voces",
   "candidatos": ["Psicosis", "Depresión", "Fobia social", "Burnout", "Delirium"],
   "pasos": [("Orientada: conciencia clara", ["Delirium"]),
             ("Oye voces y cree que la quieren dañar", ["Fobia social", "Burnout"]),
             ("No hay ánimo triste que lo explique", ["Depresión"])],
   "final": ("PSICOSIS", ["Delirio persecutorio + alucinaciones", "4 meses: t. esquizofreniforme"]),
   "nota": "Descartar consumo de sustancias y causas orgánicas; iniciar antipsicótico y referir."},
  ["Esquizofrenia: síntomas por más de 6 meses (DSM-5).",
   "Trastorno esquizofreniforme: 1 a 6 meses.",
   "Trastorno psicótico breve: menos de 1 mes."],
  "APA – DSM-5-TR (2022) · MINSA – Guía de práctica clínica de psicosis en el primer nivel de atención")

# NEF-038 · fases
V("fases", "NEF-038", "hbp-residuo-vesical-creatinina-rtu", "Uropatía obstructiva por HBP",
  "NEFROLOGÍA ENAM: UROPATÍA OBSTRUCTIVA", "NEFROLOGÍA",
  ("Uropatía obstructiva baja", ["Hiperplasia prostática con gran residuo: falla renal posrenal",
   "Primero se desobstruye; el tratamiento definitivo es quirúrgico"]),
  ("Varón de 70 años con 3 años de chorro débil", ["Náuseas, vómitos, palidez terrosa", "Creatinina 3.5 · Hb 9 · gran residuo vesical"]),
  {"rotulo": "Etapas del manejo", "ans": 3,
   "fases": [("Desobstruir", "Día 0", "Sonda vesical", ["Alivia la retención"]),
             ("Poliuria", "24-72 h", "Vigilar electrolitos", ["Diuresis posobstructiva"]),
             ("Recupera", "1-2 sem", "Baja la creatinina", ["Corregir anemia y uremia"]),
             ("Definitivo", "Programado", "RTU DE PRÓSTATA", ["Resuelve la obstrucción"])],
   "curvas": [("Creat.", ROSE, [0.9, 0.85, 0.7, 0.5, 0.4, 0.35, 0.3]),
              ("Residuo", SKY, [0.95, 0.2, 0.25, 0.3, 0.3, 0.1, 0.05])],
   "chips_titulo": "Tratamiento definitivo · marcado el correcto",
   "chips": [("RTU prostática", True), ("Sonda intermitente", False), ("Diálisis", False), ("Transfusión", False)]},
  ["Indicaciones de cirugía en HBP: retención recurrente, falla renal, litiasis, ITU o hematuria recurrentes.",
   "La diálisis no es necesaria si la función mejora al desobstruir.",
   "Ecografía: hidronefrosis bilateral y residuo posmiccional alto."],
  "EAU – Guidelines on management of non-neurogenic male LUTS (2024) · Campbell-Walsh-Wein Urology 12.ª ed. (2020)")

# NEF-039 · árbol
A("NEF-039", "calculo-enclavado-fiebre-hipotension-doble-j", "Pielonefritis obstructiva",
  "NEFROLOGÍA ENAM: PIELONEFRITIS OBSTRUCTIVA", "NEFROLOGÍA",
  ("Pielonefritis obstructiva", ["Infección sobre un uréter obstruido: el antibiótico solo no basta",
   "Urgencia urológica: descomprimir la vía urinaria"]),
  ("Varón de 30 años con litiasis renal", ["T 39.5 °C, PA 90/60 · PPL derecho (++)", "Cálculo enclavado con dilatación · no mejora con antibióticos"]),
  Q("¿Pielonefritis con el uréter obstruido?", [
      L("No obstruida", "Antibiótico EV", ["Estudiar el cálculo después"]),
      Q("¿Cómo drenar?", [
          L("Vía retrógrada", "ENDOPRÓTESIS URETERAL", ["Catéter doble J por cistoscopia", "+ antibiótico de amplio espectro"], path=True),
          L("Si no pasa el uréter", "Nefrostomía percutánea", ["Guiada por ecografía"])],
        edge="Sí: urgencia", path=True)], path=True),
  ("Drenaje urgente", [("Doble J", True), ("Nefrostomía", False)], [
      ("Vía", ["Cistoscopia retrógrada", "Percutánea"]),
      ("Ventaja", ["Sin catéter externo", "Útil si el uréter no pasa"]),
      ("Cálculo", ["Se trata en frío", "Se trata en frío"])]),
  ["Nunca litotricia ni ureteroscopia con infección activa: riesgo de sepsis.",
   "Tomar urocultivo y hemocultivos antes del antibiótico.",
   "El cálculo se resuelve cuando cede la infección."],
  "EAU – Guidelines on urolithiasis (2024) · AUA – Surgical management of stones (2016)")

# INF-049 · radial
V("radial", "INF-049", "serumista-selva-vacuna-fiebre-amarilla-dosis-unica", "Vacuna contra la fiebre amarilla",
  "INFECTOLOGÍA ENAM: VACUNA ANTIAMARÍLICA", "INFECTOLOGÍA",
  ("Vacuna antiamarílica", ["Virus vivo atenuado (17D)",
   "Una sola dosis protege de por vida: no necesita refuerzo"]),
  ("Médico serumista que viajará a la selva", ["Zona endémica de fiebre amarilla", "Vacunado hace 2 años"]),
  {"rotulo": "Mapa del tema", "centro": "FIEBRE AMARILLA", "centro_sub": "Vacuna 17D atenuada", "ans": 0,
   "items": [("DOSIS ÚNICA", ["Protege de por vida", "Sin refuerzos (OMS 2013)"]),
             ("Esquema MINSA", ["A los 15 meses de edad"]),
             ("Viajeros", ["10 días antes del viaje"]),
             ("Contraindicación", ["< 6 meses, inmunosupresión"]),
             ("Precaución", ["≥ 60 años, gestantes"])],
   "ruta": ["Vacunado hace 2 años", "Dosis única vigente", "Viaja a zona endémica", "NO REVACUNAR"]},
  ["La protección empieza a los 10 días de la vacuna.",
   "Contraindicada en alergia al huevo grave y enfermedad del timo.",
   "Transmisión por Haemagogus (selvática) y Aedes aegypti (urbana)."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 (Esquema Nacional de Vacunación) · OMS – Vacunas contra la fiebre amarilla: documento de posición (2013)")

# CAR-039 · árbol
A("CAR-039", "st-elevado-anterolateral-angioplastia-primaria", "Infarto con elevación del ST",
  "CARDIOLOGÍA ENAM: IAM CON ELEVACIÓN DEL ST", "CARDIOLOGÍA",
  ("Infarto con elevación del ST", ["La arteria está ocluida: el objetivo es reperfundir lo antes posible",
   "De elección: angioplastia primaria si llega en < 120 minutos"]),
  ("Varón de 59 años con 30 minutos de dolor opresivo", ["Diabético, hipertenso, fumador", "ST elevado 5 mm anterolateral · troponina alta"]),
  Q("¿Dolor < 12 h con ST elevado?", [
      L("> 12 h y estable", "Estrategia invasiva", ["Coronariografía en < 24 h"]),
      Q("¿Angioplastia posible en < 120 min?", [
          L("Sí", "ANGIOPLASTIA PRIMARIA", ["Stent en la arteria culpable", "+ doble antiagregación"], path=True),
          L("No", "Fibrinólisis en < 10 min", ["Luego coronariografía 2-24 h"])],
        edge="Sí", path=True)], path=True),
  ("Tratamiento inicial", [("Dar", True), ("Evitar", False)], [
      ("Antiagregación", ["AAS + ticagrelor o clopidogrel", "AINE"]),
      ("Oxígeno", ["Solo si SatO₂ < 90%", "De rutina"]),
      ("Anticoagulante", ["Heparina durante la ICP", "Solo, sin reperfusión"])]),
  ["«Tiempo es músculo»: puerta-balón < 90 minutos.",
   "El bypass se reserva para anatomía no apta para angioplastia.",
   "Trombolíticos: tenecteplasa o alteplasa si no hay ICP disponible."],
  "ESC – Guidelines for the management of acute coronary syndromes (2023)")

# GIN-094 · termómetro
V("termometro", "GIN-094", "nauseas-8-semanas-doxilamina-piridoxina", "Náuseas y vómitos del embarazo",
  "OBSTETRICIA ENAM: NÁUSEAS Y VÓMITOS DEL EMBARAZO", "OBSTETRICIA",
  ("Náuseas y vómitos del embarazo", ["Frecuentes en el primer trimestre (pico a las 9 semanas)",
   "Primera línea farmacológica: doxilamina + piridoxina"]),
  ("Gestante de 8 semanas", ["Náuseas, vómitos y ligeros mareos", "Funciones vitales y orina normales"]),
  {"rotulo": "Gravedad (escala PUQE)",
   "niveles": [("PUQE ≤ 6", "Leve", ["Tolera la vía oral"]),
               ("PUQE 7-11", "Moderada", ["Sin deshidratación"]),
               ("PUQE ≥ 12", "Hiperémesis", ["Cetonuria, pérdida de peso > 5%"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento escalonado", "paso_label": "PASO",
   "pasos": [(1, "Medidas higiénico-dietéticas", ["Comidas pequeñas y frecuentes"], False),
             (2, "DOXILAMINA + PIRIDOXINA", ["Primera línea farmacológica"], True),
             (3, "Antieméticos u hospitalización", ["Metoclopramida, ondansetrón", "Hiperémesis: fluidos + tiamina"], False)]},
  ["El jengibre es una opción no farmacológica útil.",
   "Hiperémesis: descartar embarazo molar, múltiple e hipertiroidismo.",
   "La tiamina se da antes de la dextrosa para evitar la encefalopatía de Wernicke."],
  "ACOG – Practice Bulletin N.° 189: Nausea and vomiting of pregnancy (2018) · " + WILLIAMS)

# PED-106 · tarjetas
V("tarjetas", "PED-106", "cianosis-corazon-en-bota-tetralogia-fallot", "Cardiopatía con cianosis y corazón en bota",
  "PEDIATRÍA ENAM: TETRALOGÍA DE FALLOT", "PEDIATRÍA",
  ("Tetralogía de Fallot", ["CIV + estenosis pulmonar + aorta cabalgada + hipertrofia del VD",
   "La cardiopatía cianótica más frecuente después del periodo neonatal"]),
  ("Lactante de 1 mes con cianosis al llanto", ["Rx: corazón en «bota»", "Eco: estenosis subpulmonar, aorta cabalgada, CIV"]),
  {"rotulo": "¿Qué cardiopatía es?", "ans": 0, "cards": [
      {"titulo": "TETRALOGÍA DE FALLOT", "datos": [
          ("Tipo", "Cianótica", True), ("Rx", "Corazón en «bota»", True),
          ("Eco", "CIV + EP + aorta cabalgada", True)],
       "pie": "+ hipertrofia del VD"},
      {"titulo": "Comunicación interauricular", "datos": [
          ("Tipo", "Acianótica", False), ("Rx", "Hiperflujo pulmonar", False),
          ("Eco", "Defecto auricular", False)],
       "pie": "Desdoblamiento fijo del S2"},
      {"titulo": "Coartación de aorta", "datos": [
          ("Tipo", "Acianótica", False), ("Rx", "Muescas costales", False),
          ("Eco", "Estrechez aórtica", False)],
       "pie": "Pulsos femorales débiles"},
      {"titulo": "Ductus arterioso persistente", "datos": [
          ("Tipo", "Acianótico", False), ("Rx", "Hiperflujo pulmonar", False),
          ("Eco", "Aorta y pulmonar unidas", False)],
       "pie": "Soplo continuo en maquinaria"}]},
  ["Crisis hipoxémica: posición genupectoral, oxígeno, morfina y fluidos.",
   "La cianosis depende del grado de estenosis pulmonar.",
   "Corrección quirúrgica completa entre los 3 y 6 meses."],
  NELSON + " · Moss & Adams' Heart Disease in Infants, Children and Adolescents 10.ª ed. (2021)")

# NRL-027 · radial
V("radial", "NRL-027", "hidrocefalia-aguda-cabecera-30-grados", "Hidrocefalia aguda: medidas iniciales",
  "NEUROLOGÍA ENAM: HIPERTENSIÓN ENDOCRANEANA", "NEUROLOGÍA",
  ("Hipertensión endocraneana", ["La hidrocefalia aguda eleva la presión intracraneal",
   "Medidas generales mientras se prepara la derivación ventricular"]),
  ("Pregunta de concepto", ["Manejo inicial del paciente", "con hidrocefalia aguda"]),
  {"rotulo": "Mapa del tema", "centro": "HTE", "centro_sub": "Medidas generales", "ans": 0,
   "items": [("CABECERA A 30°", ["Mejora el drenaje venoso", "Cuello en posición neutra"]),
             ("Normocapnia", ["PaCO₂ 35-40 mmHg"]),
             ("Suero isotónico", ["Evitar soluciones hipotónicas"]),
             ("Osmoterapia", ["Manitol o salino hipertónico"]),
             ("Derivación", ["Ventriculostomía externa"])],
   "ruta": ["Hidrocefalia aguda", "↑ Presión intracraneal", "Medidas generales", "CABECERA A 30°"]},
  ["Dextrosa al 5% y sueros hipotónicos aumentan el edema cerebral.",
   "La hiperventilación solo es un puente breve ante herniación.",
   "Evitar fiebre, hipoxia, hipotensión e hiperglucemia."],
  "Brain Trauma Foundation – Guidelines for severe TBI 4.ª ed. (2016) · Greenberg's Handbook of Neurosurgery 10.ª ed. (2023)")

# GIN-095 · matriz
V("matriz", "GIN-095", "epilepsia-gestante-levetiracetam", "Antiepilépticos en el embarazo",
  "OBSTETRICIA ENAM: EPILEPSIA Y EMBARAZO", "OBSTETRICIA",
  ("Epilepsia en el embarazo", ["Se prefiere el fármaco con menor riesgo de malformaciones",
   "Levetiracetam y lamotrigina son los más seguros"]),
  ("Primigesta de 24 semanas con epilepsia", ["Primer control prenatal", "Pregunta el fármaco de elección"]),
  {"rotulo": "Riesgo de cada fármaco", "eje_x": "Aspecto", "eje_y": "Fármaco",
   "cols": ["Malformaciones", "En el embarazo"], "rows": ["Levetiracetam", "Lamotrigina", "Carbamazepina", "Ác. valproico"], "caso": (0, 1),
   "cells": [[("Riesgo bajo", ["~ 1-2%"]), ("DE ELECCIÓN", ["+ ácido fólico"])],
             [("Riesgo bajo", ["~ 2%"]), ("Alternativa", ["Medir niveles"])],
             [("Riesgo medio", ["Tubo neural"]), ("Evitar si se puede", [])],
             [("Riesgo alto", ["~ 10%, neurodesarrollo"]), ("Contraindicado", [])]]},
  ["Fenobarbital: malformaciones cardiacas y sedación neonatal.",
   "Ácido fólico desde antes de la concepción.",
   "No suspender bruscamente: las crisis también dañan al feto."],
  "ILAE/AAN – Teratogenesis, perinatal and neurodevelopmental outcomes after in utero ASM exposure (Neurology 2024)")

# CAR-040 · termómetro
V("termometro", "CAR-040", "infarto-24-horas-hipotension-crepitantes-inotropicos", "Infarto con choque cardiogénico",
  "CARDIOLOGÍA ENAM: CHOQUE CARDIOGÉNICO", "CARDIOLOGÍA",
  ("Choque cardiogénico", ["Falla de bomba: hipotensión + congestión + hipoperfusión",
   "Inótropos para mejorar el gasto; no forzar la diuresis"]),
  ("Varón de 52 años con infarto de 24 horas", ["PA 90/60, FC 100 · IY (+), crepitantes", "Na urinario < 20, FeNa < 1%: hipoperfusión renal"]),
  {"rotulo": "Clasificación de Killip",
   "niveles": [("Killip I", "Sin congestión", ["Mortalidad ~ 5%"]),
               ("Killip II", "Crepitantes, S3", ["Congestión leve"]),
               ("Killip III", "Edema pulmonar", ["Congestión franca"]),
               ("Killip IV", "Choque cardiogénico", ["Hipotensión + hipoperfusión"])],
   "caso_nivel": 3, "ruta_titulo": "Manejo del choque", "paso_label": "PASO",
   "pasos": [(1, "Monitoreo y oxígeno", ["Si SatO₂ < 90%"], False),
             (2, "INÓTROPOS", ["Dobutamina ± noradrenalina"], True),
             (3, "Revascularización urgente", ["Angioplastia aun después de 12 h"], False)]},
  ["La trombólisis ya no se indica a las 24 horas.",
   "FeNa < 1%: la oliguria es por bajo gasto, no por daño renal.",
   "Descartar complicaciones mecánicas con ecocardiografía."],
  "ESC – Guidelines for the management of acute coronary syndromes (2023) · AHA – Contemporary management of cardiogenic shock (Circulation 2017)")

# SP-065 · radial
V("radial", "SP-065", "vih-adolescentes-comunicacion-educativa-colegio", "Escenarios de la promoción de la salud",
  "SALUD PÚBLICA ENAM: ESCENARIOS SALUDABLES", "SALUD PÚBLICA",
  ("Promoción de la salud por escenarios", ["La intervención se lleva al lugar donde está la población objetivo",
   "Adolescentes: la institución educativa"]),
  ("Aumento de VIH en adolescentes de un distrito", ["Plan de comunicación educativa", "Prevención y control de la transmisión"]),
  {"rotulo": "Mapa del tema", "centro": "ESCENARIOS", "centro_sub": "Promoción de la salud", "ans": 0,
   "items": [("COLEGIO", ["Donde están los adolescentes", "Educación sexual integral"]),
             ("Familia", ["Primer espacio de crianza"]),
             ("Comunidad", ["Organizaciones y líderes"]),
             ("Municipio", ["Gobierno local"]),
             ("Centro laboral", ["Población adulta"])],
   "ruta": ["VIH en adolescentes", "Comunicación educativa", "Llegar a la mayoría", "COLEGIO"]},
  ["Programa de Instituciones Educativas Saludables: Salud + Educación.",
   "El portador y el hospital son ámbitos de atención, no de prevención masiva.",
   "Mensajes: postergar el inicio sexual, condón y prueba de VIH."],
  "MINSA – Lineamientos de política de promoción de la salud (2017) · MINSA – Programa de Instituciones Educativas Saludables")

# GAS-036 · puntaje
V("puntaje", "GAS-036", "paracetamol-inr-6-asterixis-n-acetilcisteina", "Falla hepática por paracetamol",
  "GASTROENTEROLOGÍA ENAM: FALLA HEPÁTICA AGUDA POR PARACETAMOL", "GASTROENTEROLOGÍA",
  ("Falla hepática aguda por paracetamol", ["Coagulopatía + encefalopatía en un hígado previamente sano",
   "La N-acetilcisteína sirve incluso si se da tarde"]),
  ("Varón de 27 años que se automedicó con paracetamol", ["Ictericia, asterixis, desorientado", "INR 6 · pH 7.32 · creatinina 1.9"]),
  {"rotulo": "Criterios del King's College en el caso", "escala": "King's College", "total": 0, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Aún no cumple para trasplante",
   "items": [("pH < 7.30 tras reanimar", "1", False), ("INR > 6.5", "1", False),
             ("Creatinina > 3.4 mg/dL", "1", False), ("Encefalopatía grado III-IV", "1", False)],
   "bandas": [("No", "No cumple", "N-acetilcisteína EV + UCI", True),
              ("Sí", "Cumple criterios", "Lista urgente de trasplante hepático", False)]},
  ["Cumple King's si pH < 7.30, o si tiene los otros tres juntos.",
   "El lavado gástrico sirve solo en la primera hora.",
   "La vitamina K no corrige la falla de síntesis hepática."],
  "AASLD – Position paper: management of acute liver failure (2011, act. 2022) · EASL – Clinical practice guidelines on acute liver failure (2017)")

# PED-107 · tarjetas
V("tarjetas", "PED-107", "exudado-petequias-paladar-amoxicilina-10-dias", "Faringoamigdalitis estreptocócica",
  "PEDIATRÍA ENAM: FARINGOAMIGDALITIS ESTREPTOCÓCICA", "PEDIATRÍA",
  ("Faringoamigdalitis por estreptococo del grupo A", ["Fiebre, exudado y petequias en el paladar, sin tos ni rinorrea",
   "Tratamiento de 10 días para prevenir la fiebre reumática"]),
  ("Niño de 7 años con fiebre y disfagia", ["T 38.5 °C", "Exudado purulento y petequias en el paladar"]),
  {"rotulo": "¿Qué antibiótico?", "ans": 0, "cards": [
      {"titulo": "AMOXICILINA", "datos": [
          ("Dosis", "50 mg/kg/día (máx. 1 g)", True), ("Duración", "10 días", True),
          ("Uso", "Primera elección", True)],
       "pie": "Erradica el estreptococo"},
      {"titulo": "Penicilina benzatínica", "datos": [
          ("Dosis", "600 000 UI si < 27 kg", False), ("Duración", "Dosis única IM", False),
          ("Uso", "Si no cumple la vía oral", False)],
       "pie": "También de primera línea"},
      {"titulo": "Azitromicina", "datos": [
          ("Dosis", "12 mg/kg/día", False), ("Duración", "5 días", False),
          ("Uso", "Alergia a penicilina", False)],
       "pie": "Resistencia creciente"},
      {"titulo": "Cefalexina", "datos": [
          ("Dosis", "40 mg/kg/día", False), ("Duración", "10 días", False),
          ("Uso", "Alergia no anafiláctica", False)],
       "pie": "Cefalosporina de 1.ª generación"}]},
  ["Cursos de 5 días de amoxicilina no bastan para erradicar el estreptococo.",
   "Confirmar con prueba rápida o cultivo cuando esté disponible.",
   "Complicaciones: absceso periamigdalino, fiebre reumática, glomerulonefritis."],
  "IDSA – Clinical practice guideline for group A streptococcal pharyngitis (2012) · " + NELSON)

# INF-050 · matriz
V("matriz", "INF-050", "lcr-linfocitos-glucosa-baja-miliar-meningitis-tb", "Meningitis: análisis del LCR",
  "INFECTOLOGÍA ENAM: MENINGITIS TUBERCULOSA", "INFECTOLOGÍA",
  ("Meningitis tuberculosa", ["Curso subagudo (> 1-2 semanas) con LCR linfocitario y glucosa baja",
   "Un patrón miliar en la Rx de tórax apoya el origen tuberculoso"]),
  ("Mujer de 22 años con 14 días de cefalea y vómitos", ["Fiebre, rigidez de nuca, fotofobia", "LCR: 200 linfocitos, proteínas 90, glucosa baja · Rx miliar"]),
  {"rotulo": "Patrones del LCR", "eje_x": "Hallazgo", "eje_y": "Meningitis",
   "cols": ["Células", "Glucosa"], "rows": ["Tuberculosa", "Bacteriana", "Viral", "Criptococo"], "caso": (0, 0),
   "cells": [[("LINFOCITOS", ["100-500 · proteínas altas"]), ("Baja", ["ADA elevado"])],
             [("Neutrófilos", ["> 1000"]), ("Muy baja", [])],
             [("Linfocitos", ["< 300"]), ("Normal", [])],
             [("Linfocitos", ["Tinta china"]), ("Baja", ["VIH con CD4 < 100"])]]},
  ["Tratamiento: esquema antituberculoso prolongado + dexametasona.",
   "Compromete pares craneales y causa hidrocefalia e infartos.",
   "Listeria: neonatos, ancianos e inmunosuprimidos."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · IDSA/ATS/CDC – Treatment of drug-susceptible tuberculosis (2016)")

# PED-108 · embudo
V("embudo", "PED-108", "vacuna-influenza-contraindicacion-menor-6-meses", "Contraindicación de la vacuna contra influenza",
  "PEDIATRÍA ENAM: VACUNA CONTRA INFLUENZA", "PEDIATRÍA",
  ("Vacuna contra influenza", ["Virus inactivado: se aplica desde los 6 meses",
   "Antes de esa edad no genera respuesta adecuada"]),
  ("Pregunta de concepto", ["Contraindicación absoluta", "de la vacuna contra influenza en niños"]),
  {"rotulo": "Embudo de opciones",
   "inicio": "Niño que acude a vacunarse",
   "candidatos": ["Menor de 6 meses", "Neoplasia", "Inmunosupresión", "COVID-19 severa previa", "Alergia al huevo"],
   "pasos": [("Inmunosuprimidos y con cáncer: grupo prioritario", ["Neoplasia", "Inmunosupresión"]),
             ("El COVID-19 previo no contraindica", ["COVID-19 severa previa"]),
             ("Alergia al huevo: se vacuna con vigilancia", ["Alergia al huevo"])],
   "final": ("MENOR DE 6 MESES", ["No responde a la vacuna", "Se protege vacunando a la gestante"]),
   "nota": "La otra contraindicación absoluta es la anafilaxia a una dosis previa."},
  ["Esquema MINSA: 6 y 7 meses (2 dosis) y luego dosis anual.",
   "La vacuna inactivada es segura en inmunosuprimidos.",
   "Vacunar a la gestante protege al lactante en sus primeros meses."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 (Esquema Nacional de Vacunación) · CDC/ACIP – Prevention and control of seasonal influenza (2024-25)")

# PSI-019 · puntaje
V("puntaje", "PSI-019", "haloperidol-rigidez-fiebre-cpk-neuroleptico-maligno", "Síndrome neuroléptico maligno",
  "PSIQUIATRÍA ENAM: SÍNDROME NEUROLÉPTICO MALIGNO", "PSIQUIATRÍA",
  ("Síndrome neuroléptico maligno", ["Antipsicótico + fiebre + rigidez «en tubo de plomo» + disautonomía",
   "CPK elevada y riesgo de falla renal por rabdomiólisis"]),
  ("Varón de 73 años con demencia", ["Haloperidol EV desde hace 3 días", "Rigidez, diaforesis, T 39.2 °C · CPK 2220"]),
  {"rotulo": "Criterios del consenso en el caso", "escala": "Consenso internacional", "total": 75, "max": 100,
   "total_label": "Puntaje del caso",
   "interpreta": "≥ 74: síndrome neuroléptico maligno",
   "items": [("Antipsicótico en las últimas 72 h", "20", True), ("Hipertermia > 38 °C", "18", True),
             ("Rigidez muscular", "17", True), ("Alteración del estado mental", "13", False),
             ("CPK ≥ 4 veces lo normal", "10", True), ("Labilidad autonómica, diaforesis", "10", True),
             ("Taquicardia + taquipnea", "5", False), ("Estudio negativo para otra causa", "7", False)],
   "bandas": [("< 74", "Poco probable", "Buscar otra causa", False),
              ("≥ 74", "SNM probable", "Suspender haloperidol; UCI, hidratación, dantroleno", True)]},
  ["Síndrome serotoninérgico: clonus e hiperreflexia en vez de rigidez.",
   "Acatisia: inquietud motora, sin fiebre ni CPK alta.",
   "Bromocriptina o dantroleno en casos graves."],
  "Gurrera – International consensus criteria for NMS (J Clin Psychiatry 2011) · APA – DSM-5-TR (2022)")

# GIN-096 · árbol
A("GIN-096", "sangrado-uterino-endometrio-24-mm-biopsia", "Sangrado uterino anormal",
  "GINECOLOGÍA ENAM: SANGRADO UTERINO ANORMAL", "GINECOLOGÍA",
  ("Sangrado uterino anormal", ["Se estudia la causa con PALM-COEIN",
   "Biopsia si hay riesgo de hiperplasia o cáncer de endometrio"]),
  ("Mujer de 28 años con 6 meses de menstruaciones abundantes", ["Ciclos regulares, examen normal, test negativo", "Eco TV: endometrio de 24 mm"]),
  Q("¿Edad ≥ 45 años?", [
      L("Sí", "Biopsia de endometrio", ["Siempre"]),
      Q("¿SUA persistente, estrógenos sin oposición o endometrio engrosado?", [
          L("Sí", "BIOPSIA DE ENDOMETRIO", ["Aspiración en consultorio", "Endometrio de 24 mm"], path=True),
          L("No", "Tratamiento médico", ["Según la causa"])],
        edge="No", path=True)], path=True),
  ("Clasificación PALM-COEIN", [("PALM: estructural", True), ("COEIN: no estructural", False)], [
      ("1", ["Pólipo", "Coagulopatía"]),
      ("2", ["Adenomiosis", "Ovulatoria"]),
      ("3", ["Leiomioma", "Endometrial"]),
      ("4", ["Malignidad e hiperplasia", "Iatrogénica, no clasificada"])]),
  ["El legrado ya no es de primera línea: se prefiere la biopsia por aspiración.",
   "Obesidad, SOP y anovulación favorecen la hiperplasia en jóvenes.",
   "La histeroscopia se usa si la biopsia no es concluyente o hay lesión focal."],
  "ACOG – Practice Bulletin N.° 128: Diagnosis of AUB in reproductive-aged women (2012, reafirmado 2024) · FIGO – PALM-COEIN (2018)")

# SP-066 · embudo
V("embudo", "SP-066", "vph-escolares-coordinacion-intersectorial", "Coberturas de vacunación VPH en descenso",
  "SALUD PÚBLICA ENAM: INTERSECTORIALIDAD", "SALUD PÚBLICA",
  ("Intersectorialidad", ["Salud trabaja con otros sectores para llegar a la población",
   "Vacunación VPH: alianza Salud-Educación en las escuelas"]),
  ("Médico jefe de un establecimiento", ["Cobertura de VPH en descenso", "Vacunan casa por casa, pero los niños están en la escuela"]),
  {"rotulo": "Embudo de estrategias",
   "inicio": "Cobertura baja de vacuna VPH",
   "candidatos": ["Coordinar con Educación", "Casa por casa", "Notificar a los padres", "Agentes comunitarios", "Avisar al municipio"],
   "pasos": [("Los niños no están en casa: están en la escuela", ["Casa por casa"]),
             ("Los agentes comunitarios no vacunan", ["Agentes comunitarios"]),
             ("Informar no lleva la vacuna al colegio", ["Notificar a los padres", "Avisar al municipio"])],
   "final": ("COORDINACIÓN INTERSECTORIAL", ["Salud + Educación", "Vacunación en las instituciones educativas"]),
   "nota": "La vacunación escolar es la estrategia con mayor cobertura de VPH en el Perú."},
  ["Esquema MINSA: niñas y niños de 9 a 18 años, dosis única.",
   "La intersectorialidad es un eje de la promoción de la salud.",
   "El consentimiento informado de los padres se gestiona con el colegio."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 y modificatorias (VPH dosis única, 2024) · OPS – Salud en todas las políticas")

# GIN-097 · matriz
V("matriz", "GIN-097", "diabetes-pregestacional-macrosomia-insulina", "Diabetes en el embarazo: tratamiento",
  "OBSTETRICIA ENAM: DIABETES PREGESTACIONAL", "OBSTETRICIA",
  ("Diabetes pregestacional", ["La insulina es el tratamiento de elección en el embarazo",
   "Se suspenden los antidiabéticos orales"]),
  ("Gestante con diabetes previa al embarazo", ["Dos partos macrosómicos previos", "Pregunta el tratamiento más adecuado"]),
  {"rotulo": "Tratamiento según el tipo", "eje_x": "Paso", "eje_y": "Diabetes",
   "cols": ["Primera línea", "Si no llega a la meta"], "rows": ["Pregestacional", "Gestacional"], "caso": (0, 0),
   "cells": [[("INSULINA", ["Suspender orales"]), ("Ajustar insulina", ["Esquema basal-bolo"])],
             [("Dieta y ejercicio", ["1-2 semanas"]), ("Insulina", ["Metformina: alternativa"])]]},
  ["Metas: ayunas < 95, 1 h < 140 y 2 h < 120 mg/dL.",
   "HbA1c < 6.5% antes de concebir reduce malformaciones.",
   "Glibenclamida: cruza la placenta, hipoglucemia y macrosomía."],
  "ADA – Standards of Care in Diabetes: Management of diabetes in pregnancy (2025) · " + WILLIAMS)

# TRA-017 · termómetro
V("termometro", "TRA-017", "angulo-cobb-30-escoliosis-moderada", "Escoliosis: ángulo de Cobb",
  "TRAUMATOLOGÍA ENAM: ESCOLIOSIS", "TRAUMATOLOGÍA",
  ("Ángulo de Cobb", ["Se mide en la Rx de columna de pie, entre las vértebras más inclinadas",
   "Escoliosis: curva ≥ 10°; la gravedad guía el tratamiento"]),
  ("Niño de 4 años en estudio por escoliosis", ["Radiografía de columna", "Ángulo de Cobb de 30°"]),
  {"rotulo": "Gravedad según Cobb",
   "niveles": [("10-20°", "Leve", ["Observación y Rx seriadas"]),
               ("20-40°", "Moderada", ["Corsé si aún crece"]),
               ("40-50°", "Severa", ["Cirugía (artrodesis)"]),
               ("> 50°", "Muy severa", ["Riesgo cardiopulmonar"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Medir el ángulo de Cobb", ["Rx de columna de pie"], False),
             (2, "CORSÉ O YESOS SERIADOS", ["Curva moderada en crecimiento"], True),
             (3, "Cirugía", ["Curva > 40-50° o que progresa"], False)]},
  ["Test de Adams: giba costal al flexionar el tronco.",
   "Inicio antes de los 10 años (temprana): mayor riesgo de progresión.",
   "El riesgo de progresión depende del crecimiento restante (Risser)."],
  "SRS – Scoliosis Research Society: terminology and treatment · Lovell and Winter's Pediatric Orthopaedics 8.ª ed. (2020)")

# GIN-098 · termómetro
V("termometro", "GIN-098", "popq-ba-menos-1-asintomatica-kegel", "Prolapso genital: estadios POP-Q",
  "GINECOLOGÍA ENAM: PROLAPSO DE ÓRGANOS PÉLVICOS", "GINECOLOGÍA",
  ("Prolapso de órganos pélvicos", ["Se estadifica con el sistema POP-Q, tomando el himen como punto 0",
   "Si es asintomático no se opera: entrenamiento del piso pélvico"]),
  ("Mujer de 55 años, asintomática", ["Control ginecológico", "POP-Q: Ba −1 · útero normal"]),
  {"rotulo": "Estadio POP-Q",
   "niveles": [("0-I", "Arriba del himen", ["Punto más bajo < −1 cm"]),
               ("II", "Cerca del himen", ["Entre −1 y +1 cm"]),
               ("III", "Pasa el himen", ["> +1 cm, no total"]),
               ("IV", "Eversión total", ["Procidencia"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "¿Tiene síntomas?", ["Bulto, presión, disfunción urinaria"], False),
             (2, "ASINTOMÁTICA: KEGEL", ["Entrenamiento del piso pélvico"], True),
             (3, "Sintomática: pesario o cirugía", ["Según deseo y estadio"], False)]},
  ["Ba es el punto más declive de la pared vaginal anterior.",
   "Factores de riesgo: partos vaginales, edad, obesidad, estreñimiento.",
   "La cirugía se reserva para prolapso sintomático."],
  "ACOG – Practice Bulletin N.° 214: Pelvic organ prolapse (2019) · Williams Gynecology 4.ª ed. (2020)")

# SP-067 · radial
V("radial", "SP-067", "paciente-lucido-delega-decision-hijo-autonomia", "Principios de la bioética",
  "SALUD PÚBLICA ENAM: AUTONOMÍA", "SALUD PÚBLICA",
  ("Autonomía", ["El paciente capaz decide sobre su salud",
   "Incluye decidir quién recibe la información y toma las decisiones"]),
  ("Varón de 77 años con cáncer de próstata metastásico", ["Examen mental normal", "Pide que su hijo mayor decida sobre su manejo"]),
  {"rotulo": "Mapa del tema", "centro": "BIOÉTICA", "centro_sub": "Principios", "ans": 0,
   "items": [("AUTONOMÍA", ["El paciente capaz decide", "Puede delegar en quien elija"]),
             ("Beneficencia", ["Hacer el bien"]),
             ("No maleficencia", ["No dañar"]),
             ("Justicia", ["Distribución equitativa"]),
             ("Consentimiento", ["Expresión de la autonomía"])],
   "ruta": ["Paciente lúcido", "Elige que decida su hijo", "El médico lo respeta", "AUTONOMÍA"]},
  ["Respetar la decisión de delegar también es respetar la autonomía.",
   "Si pierde la capacidad, decide el representante que él eligió.",
   "Ley N.° 29414: derechos de las personas usuarias de los servicios de salud."],
  "Beauchamp y Childress – Principles of Biomedical Ethics 8.ª ed. (2019) · Ley N.° 29414 y su reglamento (2015)")

# SP-068 · tarjetas
V("tarjetas", "SP-068", "anemia-55-vs-5-distritos-equidad", "Valores de la atención primaria",
  "SALUD PÚBLICA ENAM: EQUIDAD", "SALUD PÚBLICA",
  ("Equidad en salud", ["Ausencia de diferencias injustas y evitables entre grupos",
   "Valor central de la atención primaria de salud renovada"]),
  ("ASIS 2022: anemia en menores de 5 años", ["Distrito A: 55%", "Distrito B: 5%"]),
  {"rotulo": "¿Qué valor está afectado?", "ans": 0, "cards": [
      {"titulo": "EQUIDAD", "datos": [
          ("Significa", "Sin diferencias injustas", True), ("Ejemplo", "Anemia 55% vs 5%", True),
          ("Se corrige", "Según necesidad", True)],
       "pie": "Valor de la APS"},
      {"titulo": "Participación", "datos": [
          ("Significa", "La comunidad decide", False), ("Ejemplo", "Comités de salud", False),
          ("Se corrige", "Involucrando a la gente", False)],
       "pie": "Principio de la APS"},
      {"titulo": "Sostenibilidad", "datos": [
          ("Significa", "Continuidad en el tiempo", False), ("Ejemplo", "Financiamiento estable", False),
          ("Se corrige", "Planificación", False)],
       "pie": "Principio de la APS"},
      {"titulo": "Calidad", "datos": [
          ("Significa", "Atención segura y efectiva", False), ("Ejemplo", "Normas y auditoría", False),
          ("Se corrige", "Mejora continua", False)],
       "pie": "Principio de la APS"}]},
  ["Valores de la APS renovada: derecho a la salud, equidad y solidaridad.",
   "Igualdad da lo mismo a todos; equidad da más a quien más necesita.",
   "La diferencia entre distritos refleja determinantes sociales."],
  "OPS/OMS – La renovación de la atención primaria de salud en las Américas (2007) · OPS – Estrategia para el acceso universal a la salud (2014)")

# PED-109 · tarjetas
V("tarjetas", "PED-109", "lactante-pielonefritis-urocultivo-sondaje", "Urocultivo en el lactante",
  "PEDIATRÍA ENAM: INFECCIÓN URINARIA EN EL LACTANTE", "PEDIATRÍA",
  ("Recolección de orina en el lactante", ["Sin control de esfínteres: sondaje vesical o punción suprapúbica",
   "La bolsa colectora se contamina: no sirve para cultivo"]),
  ("Lactante de 6 meses", ["Sospecha de pielonefritis aguda", "Madre con escabiosis, lesiones maculares en el niño"]),
  {"rotulo": "¿Cómo tomar la muestra?", "ans": 0, "cards": [
      {"titulo": "SONDAJE VESICAL", "datos": [
          ("Uso", "Lactante sin control", True), ("Contaminación", "Baja", True),
          ("Positivo", "≥ 50 000 UFC/mL", True)],
       "pie": "De elección en el lactante"},
      {"titulo": "Punción suprapúbica", "datos": [
          ("Uso", "Si falla la sonda", False), ("Contaminación", "Mínima", False),
          ("Positivo", "Cualquier recuento", False)],
       "pie": "Más invasiva, guiada por eco"},
      {"titulo": "Bolsa colectora", "datos": [
          ("Uso", "Solo tamizaje", False), ("Contaminación", "Muy alta", False),
          ("Positivo", "Solo vale si es negativa", False)],
       "pie": "No sirve para cultivo"},
      {"titulo": "Chorro medio", "datos": [
          ("Uso", "Niño con control", False), ("Contaminación", "Moderada", False),
          ("Positivo", "≥ 100 000 UFC/mL", False)],
       "pie": "Requiere continencia"}]},
  ["La punción suprapúbica es el patrón de referencia, pero más invasiva.",
   "Las lesiones de escabiosis en la zona perineal contaminan la bolsa.",
   "Urocultivo antes de iniciar el antibiótico."],
  "AAP – UTI: clinical practice guideline, 2-24 months (Pediatrics 2011, reafirmado 2016) · " + NELSON)

# TRA-018 · fases
V("fases", "TRA-018", "ortolani-positivo-2-meses-arnes-pavlik", "Displasia de cadera: tratamiento por edad",
  "TRAUMATOLOGÍA ENAM: DISPLASIA DEL DESARROLLO DE LA CADERA", "TRAUMATOLOGÍA",
  ("Displasia del desarrollo de la cadera", ["El tratamiento depende de la edad al diagnóstico",
   "Menores de 6 meses: arnés de Pavlik"]),
  ("Lactante de 2 meses, sexo femenino, parto podálico", ["Pliegues glúteos y de muslos asimétricos", "Ortolani (+)"]),
  {"rotulo": "Tratamiento según la edad", "ans": 0,
   "fases": [("Lactante", "0-6 m", "ARNÉS DE PAVLIK", ["Flexión y abducción"]),
             ("Lact. mayor", "6-18 m", "Reducción cerrada", ["+ yeso pelvipédico"]),
             ("Preescolar", "18 m-8 a", "Reducción abierta", ["± osteotomía"]),
             ("Escolar", "> 8 años", "Osteotomía", ["Cirugía de salvamento"])],
   "curvas": [("Éxito", SKY, [0.95, 0.9, 0.75, 0.55, 0.4, 0.25, 0.15])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Arnés de Pavlik", True), ("Ortesis de abducción", False), ("Osteotomía", False), ("Fijación interna", False)]},
  ["Control ecográfico: si no se reduce en 3-4 semanas, retirar el arnés.",
   "Complicación del arnés: necrosis avascular de la cabeza femoral.",
   "Factores de riesgo: niña, primogénita, podálica, antecedente familiar."],
  "AAOS – Detection and nonoperative management of pediatric DDH in infants up to 6 months (2022) · Lovell and Winter's Pediatric Orthopaedics 8.ª ed. (2020)")

# INF-051 · embudo
V("embudo", "INF-051", "ayacucho-convulsion-quiste-escolex-neurocisticercosis", "Convulsión y quiste cerebral",
  "INFECTOLOGÍA ENAM: NEUROCISTICERCOSIS", "INFECTOLOGÍA",
  ("Neurocisticercosis", ["Larva de Taenia solium en el cerebro",
   "Primera causa de epilepsia adquirida en la sierra del Perú"]),
  ("Niño de 10 años de Ayacucho", ["Convulsiones tónico-clónicas generalizadas", "RM: quiste con escólex + calcificaciones"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Niño con convulsiones y lesión quística",
   "candidatos": ["Neurocisticercosis", "Toxoplasmosis", "Tuberculoma", "Absceso cerebral", "Tumor cerebral"],
   "pasos": [("Niño inmunocompetente", ["Toxoplasmosis"]),
             ("Sin fiebre ni foco séptico", ["Absceso cerebral"]),
             ("Escólex dentro del quiste + calcificaciones", ["Tuberculoma", "Tumor cerebral"])],
   "final": ("NEUROCISTICERCOSIS", ["Quiste con escólex: patognomónico", "Procede de zona endémica"]),
   "nota": "Tratamiento: antiepiléptico; albendazol + corticoide si hay quistes viables."},
  ["Las calcificaciones son quistes muertos: no reciben antiparasitario.",
   "Con hidrocefalia, primero la derivación y luego el antiparasitario.",
   "Se contagia por huevos (fecal-oral) de un portador de tenia."],
  "IDSA/ASTMH – Clinical practice guidelines for neurocysticercosis (2017) · MINSA – Guía de práctica clínica de neurocisticercosis")

# GAS-037 · árbol
A("GAS-037", "ascitis-pmn-7000-peritonitis-espontanea-ceftriaxona", "Peritonitis bacteriana espontánea",
  "GASTROENTEROLOGÍA ENAM: PERITONITIS BACTERIANA ESPONTÁNEA", "GASTROENTEROLOGÍA",
  ("Peritonitis bacteriana espontánea", ["Cirrótico con ascitis: PMN ≥ 250/mm³ en el líquido ascítico",
   "Tratamiento: cefalosporina de 3.ª generación + albúmina"]),
  ("Varón de 52 años, alcohólico, con encefalopatía", ["Fiebre, dolor abdominal, ascitis", "Líquido: 7000 leucocitos, neutrófilos · proteínas 5 g/L"]),
  Q("¿PMN ≥ 250/mm³ en el líquido?", [
      L("No", "Sin PBE", ["Si el cultivo es +: repetir paracentesis"]),
      L("Sí", "CEFTRIAXONA O CEFOTAXIMA EV", ["+ albúmina días 1 y 3", "5-7 días"], path=True)], path=True),
  ("Antibióticos en el cirrótico", [("PBE", True), ("Profilaxis", False)], [
      ("Fármaco", ["Ceftriaxona o cefotaxima", "Ciprofloxacino, norfloxacino"]),
      ("Vía", ["EV", "Oral"]),
      ("Cuándo", ["PMN ≥ 250", "PBE previa, HDA, proteínas bajas"])]),
  ["Albúmina 1.5 g/kg el día 1 y 1 g/kg el día 3: previene el síndrome hepatorrenal.",
   "Más de un germen o PMN muy altos: pensar en peritonitis secundaria.",
   "Tras el primer episodio: profilaxis indefinida."],
  "AASLD – Diagnosis, evaluation and management of ascites, SBP and HRS (Hepatology 2021) · EASL – Decompensated cirrhosis (2018)")

# SP-069 · embudo
V("embudo", "SP-069", "letalidad-cero-casos-nuevos-prevalencia-aumenta", "Prevalencia, incidencia y letalidad",
  "SALUD PÚBLICA ENAM: PREVALENCIA", "SALUD PÚBLICA",
  ("Prevalencia ≈ incidencia × duración", ["Aumenta si entran casos nuevos o si se alarga la vida con la enfermedad",
   "Disminuye si los enfermos se curan o mueren"]),
  ("Distrito Z con nuevo programa de insulina", ["Letalidad 0 este año", "Se notifican casos nuevos de diabetes"]),
  {"rotulo": "Embudo de razonamiento",
   "inicio": "Programa que evita muertes por diabetes",
   "candidatos": ["Incrementada", "Disminuida", "Nula", "Estancada", "Igual a la incidencia"],
   "pasos": [("Hay casos nuevos: entran enfermos", ["Nula"]),
             ("Nadie muere y la diabetes no se cura", ["Disminuida"]),
             ("Entran casos y no sale ninguno", ["Estancada", "Igual a la incidencia"])],
   "final": ("INCREMENTADA", ["P ≈ I × D", "Más casos que viven más tiempo"]),
   "nota": "Un tratamiento que prolonga la vida sin curar aumenta la prevalencia."},
  ["Letalidad = muertes por la enfermedad / enfermos.",
   "Incidencia: casos nuevos en un periodo; prevalencia: todos los casos.",
   "Una cura o una epidemia mortal reducen la prevalencia."],
  "Gordis – Epidemiology 6.ª ed. (2019) · OPS – Módulos de principios de epidemiología para el control de enfermedades (MOPECE)")

# NRL-028 · árbol
A("NRL-028", "cefalea-subita-rigidez-nuca-tem-cerebral", "Sospecha de hemorragia subaracnoidea",
  "NEUROLOGÍA ENAM: HEMORRAGIA SUBARACNOIDEA", "NEUROLOGÍA",
  ("Hemorragia subaracnoidea", ["Cefalea súbita «la peor de la vida» + vómitos + rigidez de nuca",
   "Primer examen: TEM cerebral sin contraste"]),
  ("Mujer de 30 años con cefalea intensa de 3 horas", ["Cefalea centinela hace una semana", "Rigidez de nuca, diplopía, Babinski (+)"]),
  Q("¿Cefalea súbita con signos meníngeos?", [
      L("No", "Estudio de la cefalea", ["Buscar signos de alarma"]),
      Q("TEM CEREBRAL SIN CONTRASTE", [
          L("Sangre", "HSA confirmada", ["AngioTC y nimodipino"], path=True),
          L("Normal", "Punción lumbar", ["Xantocromía, eritrocitos"])],
        edge="Sí", path=True)], path=True),
  ("Estudios en sospecha de HSA", [("TEM", True), ("Punción lumbar", False), ("Arteriografía", False)], [
      ("Momento", ["Primero", "Si la TEM es normal", "Tras confirmar"]),
      ("Busca", ["Sangre subaracnoidea", "Xantocromía", "Aneurisma"])]),
  ["La TEM en las primeras 6 horas tiene sensibilidad cercana al 100%.",
   "La causa más frecuente no traumática es la rotura de un aneurisma.",
   "Nimodipino para prevenir el vasoespasmo."],
  "AHA/ASA – Guideline for the management of aneurysmal subarachnoid hemorrhage (2023)")

# CAR-041 · radial
V("radial", "CAR-041", "hta-galope-retinopatia-iv-cardiopatia-hipertensiva", "Daño de órgano blanco por HTA",
  "CARDIOLOGÍA ENAM: CARDIOPATÍA HIPERTENSIVA", "CARDIOLOGÍA",
  ("Cardiopatía hipertensiva", ["La HTA crónica produce hipertrofia del VI e insuficiencia cardiaca",
   "La retinopatía grado IV revela HTA grave y de larga data"]),
  ("Varón de 60 años con disnea progresiva de 1 año", ["Ortopnea, galope, crepitantes · PA 150/90", "Fondo de ojo: retinopatía grado IV · cardiomegalia"]),
  {"rotulo": "Mapa del tema", "centro": "HTA", "centro_sub": "Daño de órgano blanco", "ans": 0,
   "items": [("CORAZÓN", ["Hipertrofia del VI", "Insuficiencia cardiaca"]),
             ("Retina", ["Grado IV: papiledema"]),
             ("Riñón", ["Nefroesclerosis, albuminuria"]),
             ("Cerebro", ["ACV, encefalopatía"]),
             ("Arterias", ["Aneurisma, enfermedad arterial"])],
   "ruta": ["HTA crónica", "Hipertrofia del VI", "IC + retinopatía IV", "CARDIOPATÍA HIPERTENSIVA"]},
  ["Tabaquismo leve y de corto tiempo no explica esta cardiopatía.",
   "Ecocardiograma: hipertrofia concéntrica y disfunción diastólica.",
   "IECA o ARA II reducen la hipertrofia ventricular."],
  "ESC/ESH – Guidelines for the management of arterial hypertension (2023) · " + HARRISON)

# GIN-099 · matriz
V("matriz", "GIN-099", "gestante-fuma-15-cigarrillos-rciu", "Tóxicos en el embarazo",
  "OBSTETRICIA ENAM: TABAQUISMO EN EL EMBARAZO", "OBSTETRICIA",
  ("Tabaco en el embarazo", ["La nicotina y el monóxido de carbono reducen el flujo placentario",
   "Principal efecto: restricción del crecimiento intrauterino"]),
  ("Primigesta de 6 semanas, asintomática", ["Embrión de 7 mm, LCF 155", "Fuma 15 cigarrillos al día"]),
  {"rotulo": "Efectos según el tóxico", "eje_x": "Efecto", "eje_y": "Tóxico",
   "cols": ["Efecto fetal", "Otros riesgos"], "rows": ["Tabaco", "Alcohol", "Cocaína"], "caso": (0, 0),
   "cells": [[("RCIU", ["Bajo peso al nacer"]), ("DPP, prematuridad", ["Muerte súbita del lactante"])],
             [("Alcohol fetal", ["Fisura palpebral corta", "Hipoplasia nasal, filtrum liso"]), ("Déficit intelectual", [])],
             [("Vasoconstricción", ["RCIU, infarto cerebral"]), ("DPP", [])]]},
  ["Dejar de fumar en cualquier momento del embarazo mejora el peso al nacer.",
   "Fisura palpebral corta e hipoplasia nasal son del síndrome alcohólico fetal.",
   "Consejería en cada control prenatal."],
  "ACOG – Committee Opinion N.° 807: Tobacco and nicotine cessation during pregnancy (2020) · " + WILLIAMS)

# GIN-100 · puntaje
V("puntaje", "GIN-100", "hidrosonografia-dolor-anexial-salpingitis", "Salpingitis: criterios diagnósticos",
  "GINECOLOGÍA ENAM: ENFERMEDAD PÉLVICA INFLAMATORIA", "GINECOLOGÍA",
  ("Enfermedad pélvica inflamatoria", ["Infección ascendente: endometritis, salpingitis, absceso tuboovárico",
   "La instrumentación uterina reciente es un factor de riesgo"]),
  ("Mujer de 30 años con dolor en fosa ilíaca derecha", ["Hidrosonografía hace 5 días · FUR hace una semana", "Dolor a la movilización cervical y del anexo derecho"]),
  {"rotulo": "Criterios mínimos CDC en el caso", "escala": "EPI (CDC)", "total": 2, "max": 3,
   "total_label": "Criterios mínimos presentes",
   "interpreta": "Basta uno con dolor pélvico: tratar",
   "items": [("Dolor a la movilización cervical", "1", True), ("Dolor anexial", "1", True),
             ("Dolor uterino", "1", False)],
   "bandas": [("0", "No cumple", "Buscar otra causa", False),
              ("≥ 1", "EPI probable", "Ceftriaxona + doxiciclina + metronidazol", True)]},
  ["Criterios adicionales: fiebre > 38.3 °C, flujo mucopurulento, PCR o VSG altas.",
   "FUR hace una semana hace improbable el embarazo ectópico (pedir β-hCG igual).",
   "Absceso tuboovárico: hospitalizar y drenar si no mejora."],
  "CDC – Sexually transmitted infections treatment guidelines: PID (2021) · MINSA – Guía nacional de manejo de ITS (2018)")

# SP-070 · fases
V("fases", "SP-070", "campana-deteccion-vih-prevencion-secundaria", "Niveles de prevención",
  "SALUD PÚBLICA ENAM: PREVENCIÓN SECUNDARIA", "SALUD PÚBLICA",
  ("Niveles de prevención", ["Secundaria: detección precoz en personas sin síntomas (tamizaje)",
   "Busca tratar antes de que la enfermedad avance"]),
  ("Campaña en un centro de salud", ["Población de 18 a 29 años", "Detección de infección por VIH"]),
  {"rotulo": "Historia natural y prevención", "ans": 1,
   "fases": [("Primaria", "Sano", "Evitar la infección", ["Condón, PrEP"]),
             ("Secundaria", "Sin síntomas", "TAMIZAJE DE VIH", ["Detección precoz"]),
             ("Terciaria", "Enfermedad", "TAR y rehabilitación", ["Evitar complicaciones"]),
             ("Cuaternaria", "Toda etapa", "Evitar iatrogenia", ["Sobremedicalización"])],
   "curvas": [],
   "chips_titulo": "Nivel de prevención · marcado el correcto",
   "chips": [("Primario", False), ("Secundario", True), ("Terciario", False), ("Cuaternario", False)]},
  ["Prevención primaria: antes de que ocurra la enfermedad (vacunas, condón).",
   "Tamizaje = prevención secundaria.",
   "El TAR también es prevención: indetectable = intransmisible."],
  "Leavell y Clark – Niveles de prevención · MINSA – NTS N.° 204-MINSA/DGIESP-2023 (VIH)")

# CIR-057 · matriz
V("matriz", "CIR-057", "tumoracion-inguinal-irreductible-distension-hernia-complicada", "Hernia inguinal: tipos",
  "CIRUGÍA ENAM: HERNIA INGUINAL COMPLICADA", "CIRUGÍA",
  ("Hernia inguinal complicada", ["Incarcerada (irreductible) o estrangulada (con isquemia)",
   "Puede causar obstrucción intestinal: cirugía urgente"]),
  ("Varón de 30 años con 4 horas de dolor y distensión", ["Hernia inguinal derecha de 1 año", "Irreductible, dolorosa · leucocitos 12 000"]),
  {"rotulo": "Clasificación clínica", "eje_x": "Aspecto", "eje_y": "Hernia",
   "cols": ["Clínica", "Conducta"], "rows": ["Reductible", "Incarcerada", "Estrangulada"], "caso": (1, 0),
   "cells": [[("Entra y sale", ["Molestia al esfuerzo"]), ("Cirugía electiva", ["Hernioplastia"])],
             [("IRREDUCTIBLE", ["± obstrucción intestinal"]), ("Cirugía urgente", [])],
             [("Isquemia", ["Fiebre, piel roja, SIRS"]), ("Cirugía inmediata", ["± resección intestinal"])]]},
  ["Hernia complicada = incarcerada o estrangulada.",
   "No reducir a la fuerza si hay signos de estrangulación.",
   "La torsión testicular da dolor escrotal, no distensión abdominal."],
  "HerniaSurge – International guidelines for groin hernia management (Hernia 2018, act. 2023) · Sabiston Textbook of Surgery 21.ª ed. (2021)")
