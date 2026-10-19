"""Bloque 8 · parte C."""
from c8 import F8, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
ADA = "ADA – Standards of Care in Diabetes (2025)"
GG = "Goodman & Gilman. Bases farmacológicas 14.ª ed. (2023)"

# CB-087 · árbol
A("CB-087", "alprazolam-licor-glasgow-10-fr-8-via-aerea", "Intoxicación con depresión respiratoria",
  "CIENCIAS BÁSICAS ENAM: BENZODIACEPINAS Y ALCOHOL", "CIENCIAS BÁSICAS",
  ("Intoxicación por depresores del SNC", ["Benzodiacepinas + alcohol potencian la depresión respiratoria",
   "Primero la vía aérea y la ventilación (ABC)"]),
  ("Varón de 42 años, alcohólico", ["Blísteres de alprazolam y licor vacíos", "Glasgow 10 · FR 8 · SatO₂ 89 %"]),
  Q("¿Hipoventilación o vía aérea en riesgo?", [
      L("Sí", "PROTEGER LA VÍA AÉREA", ["Oxígeno, posición, aspirar", "Intubar si no mejora"], path=True),
      L("No", "Observación y soporte", ["Monitoreo, hemoglucotest"])], path=True),
  ("Flumazenil", [("Evitar", True), ("Podría usarse", False)], [
      ("Cuándo", ["Mezcla o uso crónico", "Sobredosis pura, sin dependencia"]),
      ("Riesgo", ["Convulsiones por abstinencia", "Bajo"])]),
  ["Después: hemoglucotest y tiamina en alcohólicos.",
   "El carbón activado no se da si no protege la vía aérea.",
   "Evaluar por psiquiatría: intento suicida."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# NEF-091 · puntaje
V("puntaje", "NEF-091", "pielonefritis-repeticion-fg-12-hiperpotasemia-acidosis", "Alteraciones de la ERC avanzada",
  "NEFROLOGÍA ENAM: ENFERMEDAD RENAL CRÓNICA", "NEFROLOGÍA",
  ("ERC estadio 5", ["Filtrado < 15 mL/min: el riñón no regula electrolitos ni ácidos",
   "Hiperpotasemia, hiperfosfatemia, hipocalcemia y acidosis metabólica"]),
  ("Mujer de 28 años con pielonefritis a repetición", ["Palidez terrosa · Hb 8,2", "FG 12 · riñones sin diferenciación córtico-medular"]),
  {"rotulo": "Alteraciones esperadas", "escala": "Alteraciones", "total": 4, "max": 4,
   "total_label": "Presentes en la ERC 5",
   "interpreta": "Patrón de la ERC avanzada",
   "items": [("Hiperpotasemia", "1", True), ("Hiperfosfatemia", "1", True),
             ("Hipocalcemia", "1", True), ("Acidosis metabólica", "1", True)],
   "bandas": [("Parcial", "Otro patrón", "Revisar opciones", False),
              ("4 de 4", "ERC avanzada", "Preparar diálisis", True)]},
  ["Falta calcitriol: baja el calcio y sube la PTH.",
   "Anemia por déficit de eritropoyetina.",
   "Diálisis si hay uremia o hiperpotasemia refractaria."],
  "KDIGO – CKD guideline (2024) · " + HARRISON)

# END-065 · termómetro
V("termometro", "END-065", "cetoacidosis-potasio-3-2-reponer-antes-insulina", "Potasio e insulina en la cetoacidosis",
  "ENDOCRINOLOGÍA ENAM: CETOACIDOSIS DIABÉTICA", "ENDOCRINOLOGÍA",
  ("Cetoacidosis diabética", ["Líquidos, potasio e insulina, en ese orden",
   "La insulina mete potasio a las células: no iniciar si K < 3,3"]),
  ("Mujer de 18 años con CAD", ["pH 7,12 · HCO₃⁻ 8 · glucosa 480 · cetonuria", "K 3,2 tras hidratación con salino"]),
  {"rotulo": "Potasio sérico",
   "niveles": [("< 3,3", "Bajo", ["REPONER K PRIMERO", "Diferir insulina"]),
               ("3,3-5,2", "Normal", ["Insulina + K EV"]),
               ("> 5,2", "Alto", ["Insulina sin K"])],
   "caso_nivel": 0, "ruta_titulo": "Orden en este caso", "paso_label": "PASO",
   "pasos": [(1, "Reponer potasio", ["20-30 mEq/h EV"], True),
             (2, "Insulina cuando K ≥ 3,3", ["0,1 U/kg/h"], False),
             (3, "Dextrosa si glucosa < 250", ["Hasta cerrar el anión gap"], False)]},
  ["Bicarbonato solo si pH < 6,9.",
   "Controlar potasio cada 2 horas.",
   "Buscar el desencadenante (infección, abandono)."],
  ADA + " · Kitabchi AE. Diabetes Care (2009)")

# OFT-054 · tarjetas
V("tarjetas", "OFT-054", "corticoide-topico-prolongado-glaucoma-secundario", "Tipos de glaucoma",
  "OFTALMOLOGÍA ENAM: GLAUCOMA CORTISÓNICO", "OFTALMOLOGÍA",
  ("Glaucoma por corticoides", ["Aumentan la resistencia en la malla trabecular",
   "Tiene causa conocida: glaucoma secundario de ángulo abierto"]),
  ("Mujer de 60 años", ["Glaucoma por uso prolongado de corticoides tópicos"]),
  {"rotulo": "¿Qué tipo es?", "ans": 0, "cards": [
      {"titulo": "SECUNDARIO ABIERTO", "datos": [
          ("Causa", "Corticoides", True), ("Ángulo", "Abierto", True),
          ("Curso", "Crónico", True)],
       "pie": "Suspender el corticoide"},
      {"titulo": "Primario abierto", "datos": [
          ("Causa", "Desconocida", False), ("Ángulo", "Abierto", False),
          ("Curso", "Crónico", False)],
       "pie": "El más frecuente"},
      {"titulo": "Facogénico", "datos": [
          ("Causa", "Cristalino", False), ("Ángulo", "Variable", False),
          ("Curso", "Agudo", False)],
       "pie": "Catarata madura"},
      {"titulo": "Neovascular", "datos": [
          ("Causa", "Isquemia retinal", False), ("Ángulo", "Cerrado por vasos", False),
          ("Curso", "Grave", False)],
       "pie": "Diabetes, oclusión venosa"}]},
  ["Medir la presión ocular en usuarios crónicos de corticoides.",
   "Suele mejorar al suspender el fármaco.",
   "Si persiste: tratar como glaucoma crónico."],
  "AAO – Preferred Practice Pattern: Primary open-angle glaucoma (2020)")

# CB-088 · radial
V("radial", "CB-088", "itu-anciano-ambos-aquiles-dolor-ciprofloxacino", "Efectos adversos de antibióticos",
  "CIENCIAS BÁSICAS ENAM: FLUOROQUINOLONAS", "CIENCIAS BÁSICAS",
  ("Fluoroquinolonas", ["Pueden causar tendinitis y rotura del tendón de Aquiles",
   "Mayor riesgo: > 60 años, corticoides, trasplante"]),
  ("Varón de 65 años con infección urinaria", ["A la semana del antibiótico", "Dolor y tumefacción de ambos tendones aquíleos"]),
  {"rotulo": "Mapa del tema", "centro": "ANTIBIÓTICO", "centro_sub": "Efecto adverso", "ans": 0,
   "items": [("CIPROFLOXACINO", ["Tendinitis aquílea", "QT largo"]),
             ("Gentamicina", ["Nefro y ototoxicidad"]),
             ("Cotrimoxazol", ["Stevens-Johnson"]),
             ("Ceftriaxona", ["Barro biliar"]),
             ("Nitrofurantoína", ["Fibrosis pulmonar"])],
   "ruta": ["Quinolona", "Daño del colágeno", "Tendón de Aquiles", "CIPROFLOXACINO"]},
  ["Suspender la quinolona ante dolor tendinoso.",
   "Evitarlas si hay alternativas en mayores.",
   "También: neuropatía y aneurisma aórtico."],
  GG + " · FDA – Fluoroquinolone safety (2018)")

# CB-089 · matriz
V("matriz", "CB-089", "fibrilacion-auricular-apixaban-factor-xa", "Mecanismo de los anticoagulantes",
  "CIENCIAS BÁSICAS ENAM: ANTICOAGULANTES ORALES DIRECTOS", "CIENCIAS BÁSICAS",
  ("Anticoagulantes orales directos", ["Apixabán y rivaroxabán inhiben el factor Xa",
   "Dabigatrán inhibe la trombina; no necesitan INR"]),
  ("Mujer de 68 años con FA crónica", ["Recibe apixabán para prevenir embolias", "¿Cuál es su mecanismo?"]),
  {"rotulo": "Fármaco y blanco", "eje_x": "Dato", "eje_y": "Fármaco",
   "cols": ["Blanco", "Antídoto"], "rows": ["Warfarina", "Heparina", "Apixabán", "Dabigatrán"], "caso": (2, 0),
   "cells": [[("Vitamina K", ["II, VII, IX, X"]), ("Vitamina K", ["Plasma, CCP"])],
             [("Antitrombina", []), ("Protamina", [])],
             [("FACTOR Xa", ["Directo"]), ("Andexanet", [])],
             [("Trombina", ["Directo"]), ("Idarucizumab", [])]]},
  ["Ajustar la dosis según edad, peso y creatinina.",
   "No usar en válvulas mecánicas.",
   "Menos hemorragia intracraneal que la warfarina."],
  GG + " · ESC – Atrial fibrillation guidelines (2024)")

# REU-068 · tarjetas
V("tarjetas", "REU-068", "rodilla-cristales-romboides-condrocalcinosis-pseudogota", "Artritis por cristales",
  "REUMATOLOGÍA ENAM: PSEUDOGOTA", "REUMATOLOGÍA",
  ("Pseudogota", ["Cristales de pirofosfato cálcico: romboidales, birrefringencia positiva débil",
   "Condrocalcinosis en la radiografía, típica en rodilla del adulto mayor"]),
  ("Mujer de 66 años", ["Monoartritis de rodilla izquierda", "Cristales romboides · condrocalcinosis"]),
  {"rotulo": "¿Qué artritis es?", "ans": 0, "cards": [
      {"titulo": "PSEUDOGOTA", "datos": [
          ("Cristal", "Romboidal", True), ("Birrefringencia", "Positiva débil", True),
          ("Rx", "Condrocalcinosis", True)],
       "pie": "Pirofosfato cálcico"},
      {"titulo": "Gota", "datos": [
          ("Cristal", "En aguja", False), ("Birrefringencia", "Negativa intensa", False),
          ("Rx", "Erosiones en sacabocado", False)],
       "pie": "Urato monosódico"},
      {"titulo": "Artrosis", "datos": [
          ("Cristal", "No", False), ("Birrefringencia", "—", False),
          ("Rx", "Osteofitos", False)],
       "pie": "Líquido no inflamatorio"},
      {"titulo": "Séptica", "datos": [
          ("Cristal", "No", False), ("Birrefringencia", "—", False),
          ("Rx", "Normal al inicio", False)],
       "pie": "Gram y cultivo"}]},
  ["Asociada a hiperparatiroidismo, hemocromatosis e hipomagnesemia.",
   "Tratamiento: AINE, colchicina o corticoide intraarticular.",
   "Descartar siempre infección en el líquido."],
  "EULAR – Calcium pyrophosphate deposition (2023) · " + HARRISON)

# SP-181 · radial
V("radial", "SP-181", "inmigrante-13-anos-llanto-abandono-paterno-familia", "Determinantes en la adolescente",
  "SALUD PÚBLICA ENAM: DETERMINANTES SOCIALES", "SALUD PÚBLICA",
  ("Determinantes sociales de la salud", ["La familia es un determinante clave en la salud mental",
   "El abandono paterno desestructura el soporte familiar"]),
  ("Adolescente inmigrante de 13 años", ["Llanto frecuente y desinterés escolar", "Abandono paterno"]),
  {"rotulo": "Mapa del tema", "centro": "DETERMINANTE", "centro_sub": "¿Cuál priorizar?", "ans": 0,
   "items": [("FAMILIA", ["Desestructuración familiar", "Abandono paterno"]),
             ("Socioeconómico", ["No descrito"]),
             ("Acceso a salud", ["No es el problema"]),
             ("Hormonal", ["Es biológico"])],
   "ruta": ["Abandono paterno", "Sin soporte", "Síntomas depresivos", "FAMILIA"]},
  ["Tamizar depresión y riesgo suicida.",
   "Coordinar con el colegio y servicios sociales.",
   "Derivar a un centro de salud mental comunitario."],
  "OMS – Salud mental del adolescente (2024) · MINSA – Plan de salud mental (2021)")

# NRL-059 · embudo
V("embudo", "NRL-059", "parkinson-recaidas-perdida-neuronas-dopaminergicas", "Neurotransmisor del Parkinson",
  "NEUROLOGÍA ENAM: ENFERMEDAD DE PARKINSON", "NEUROLOGÍA",
  ("Enfermedad de Parkinson", ["Pérdida de neuronas dopaminérgicas de la sustancia negra",
   "Falta dopamina en el estriado: temblor, rigidez, bradicinesia"]),
  ("Varón de 70 años con Parkinson", ["Recaídas periódicas pese al tratamiento", "¿Qué neurotransmisor está implicado?"]),
  {"rotulo": "Embudo del mecanismo",
   "inicio": "Síntomas motores del Parkinson",
   "candidatos": ["Dopamina", "Serotonina", "GABA", "Glutamato"],
   "pasos": [("Vía nigroestriada afectada", ["Serotonina"]),
             ("El tratamiento repone este mensajero", ["GABA", "Glutamato"])],
   "final": ("DOPAMINA", ["Levodopa + carbidopa", "Fluctuaciones con los años"]),
   "nota": "Las recaídas («fenómeno on-off») se deben a la pérdida progresiva de neuronas."},
  ["Los anticolinérgicos equilibran el exceso de acetilcolina.",
   "Agonistas dopaminérgicos en jóvenes.",
   "Evitar antipsicóticos típicos."],
  HARRISON)

# GIN-242 · fases
V("fases", "GIN-242", "ectopico-metotrexato-exitoso-esperar-3-meses", "Después del metotrexato",
  "OBSTETRICIA ENAM: EMBARAZO ECTÓPICO", "OBSTETRICIA",
  ("Metotrexato en el ectópico", ["Antagonista del folato con potencial teratógeno",
   "Esperar al menos 3 meses antes de un nuevo embarazo"]),
  ("Nulípara de 35 años", ["Ectópico tratado con éxito con metotrexato", "¿Cuándo puede volver a gestar?"]),
  {"rotulo": "Tiempo tras el tratamiento", "ans": 2,
   "fases": [("Días 4-7", "β-hCG", "Control", ["Debe bajar ≥ 15 %"]),
             ("Semanas", "β-hCG negativa", "Resuelto", ["Anticoncepción"]),
             ("3 meses", "Nuevo embarazo", "ESPERAR 3 MESES", ["Eliminar el fármaco", "Reponer folato"])],
   "curvas": [("β-hCG", ROSE, [0.9, 0.95, 0.7, 0.4, 0.15, 0.05, 0.02])],
   "chips_titulo": "Meses de espera · marcado el correcto",
   "chips": [("3", True), ("1", False), ("2", False), ("6", False)]},
  ["Dar ácido fólico antes del nuevo embarazo.",
   "Ecografía precoz: riesgo de otro ectópico.",
   "Evitar AINE y alcohol durante el tratamiento."],
  "ACOG Practice Bulletin 193: Tubal ectopic pregnancy (2018)")

# GAS-074 · puntaje
V("puntaje", "GAS-074", "cirrosis-hda-creatinina-1-6-sodio-urinario-8-hepatorrenal", "Criterios del síndrome hepatorrenal",
  "GASTROENTEROLOGÍA ENAM: SÍNDROME HEPATORRENAL", "GASTROENTEROLOGÍA",
  ("Síndrome hepatorrenal", ["Lesión renal funcional en cirrosis con ascitis",
   "No mejora con albúmina; sodio urinario muy bajo"]),
  ("Mujer de 58 años con cirrosis", ["Hemorragia digestiva, ascitis a tensión", "Creatinina 1,6 pese a albúmina · Na urinario 8"]),
  {"rotulo": "Criterios en el caso", "escala": "Criterios", "total": 5, "max": 5,
   "total_label": "Criterios cumplidos",
   "interpreta": "Síndrome hepatorrenal",
   "items": [("Cirrosis con ascitis", "1", True), ("Lesión renal aguda", "1", True),
             ("Sin mejoría con albúmina", "1", True), ("Sin shock ni nefrotóxicos", "1", True),
             ("Sin daño renal estructural", "1", True)],
   "bandas": [("< 5", "Otra causa", "Prerrenal o NTA", False),
              ("5 de 5", "SHR", "Terlipresina + albúmina", True)]},
  ["El lactato normal descarta un shock.",
   "Suspender diuréticos y betabloqueadores.",
   "El trasplante hepático es el tratamiento definitivo."],
  "ICA/EASL – Acute kidney injury in cirrhosis (2024)")

# END-066 · matriz
V("matriz", "END-066", "diabetico-gliflozina-sglt2-glucosuria", "Mecanismo de los antidiabéticos",
  "ENDOCRINOLOGÍA ENAM: INHIBIDORES DE SGLT2", "ENDOCRINOLOGÍA",
  ("Inhibidores de SGLT2", ["Bloquean la reabsorción de glucosa en el túbulo proximal",
   "Aumentan la glucosuria; protegen corazón y riñón"]),
  ("Varón de 50 años con diabetes", ["Inicia una gliflozina", "¿Qué efecto tiene en el riñón?"]),
  {"rotulo": "Fármaco y acción", "eje_x": "Dato", "eje_y": "Fármaco",
   "cols": ["Sitio", "Efecto"], "rows": ["Metformina", "SGLT2", "Sulfonilurea", "GLP-1"], "caso": (1, 1),
   "cells": [[("Hígado", []), ("Menos gluconeogénesis", [])],
             [("Túbulo proximal", []), ("MÁS GLUCOSURIA", ["Pierde glucosa en orina"])],
             [("Célula beta", []), ("Libera insulina", ["Hipoglucemia"])],
             [("Páncreas, cerebro", []), ("Insulina y saciedad", [])]]},
  ["Efectos adversos: infecciones genitales y micóticas.",
   "Riesgo de cetoacidosis euglucémica.",
   "Útiles en insuficiencia cardiaca y ERC."],
  ADA)

# NEF-092 · embudo
V("embudo", "NEF-092", "liposuccion-sodio-187-convulsiones-deshidratacion-neuronal", "Coma por hipernatremia",
  "NEFROLOGÍA ENAM: HIPERNATREMIA GRAVE", "NEFROLOGÍA",
  ("Hipernatremia grave", ["La osmolaridad plasmática alta saca agua de las neuronas",
   "El cerebro se deshidrata: convulsiones y coma"]),
  ("Varón de 30 años tras liposucción", ["Deterioro de conciencia, convulsiones y coma", "Na 187 mEq/L"]),
  {"rotulo": "Embudo del mecanismo",
   "inicio": "Coma tras una cirugía",
   "candidatos": ["Gradiente osmótico", "Anestésicos", "Meningoencefalitis", "Embolia grasa"],
   "pasos": [("Na 187: trastorno osmolar evidente", ["Anestésicos", "Embolia grasa"]),
             ("Sin fiebre ni signos meníngeos", ["Meningoencefalitis"])],
   "final": ("GRADIENTE OSMÓTICO", ["Deshidratación neuronal", "Riesgo de hemorragia por tracción"]),
   "nota": "Corregir lento: no más de 10-12 mEq/L en 24 horas."},
  ["Calcular el déficit de agua libre.",
   "La corrección rápida causa edema cerebral.",
   "Buscar la causa: pérdidas o sodio iatrogénico."],
  HARRISON + " · Adrogué HJ. NEJM (2000)")

# SP-182 · radial
V("radial", "SP-182", "diabetes-30-por-ciento-sin-adherencia-programa-educativo", "Intervención ante la mala adherencia",
  "SALUD PÚBLICA ENAM: ADHERENCIA EN DIABETES", "SALUD PÚBLICA",
  ("Adherencia al tratamiento crónico", ["La educación en autocuidado mejora la adherencia",
   "Debe ser continua y estructurada"]),
  ("Reporte del endocrinólogo", ["> 30 % de diabéticos no son adherentes", "Tras más de un año de tratamiento"]),
  {"rotulo": "Mapa del tema", "centro": "ADHERENCIA", "centro_sub": "¿Qué hacer?", "ans": 0,
   "items": [("EDUCACIÓN", ["Programa continuo", "Autocuidado"]),
             ("Domiciliario", ["No cambia conducta"]),
             ("Psiquiatría", ["Solo casos puntuales"]),
             ("Actividad física", ["Es un componente"])],
   "ruta": ["Mala adherencia", "Falta de comprensión", "Aprender y practicar", "EDUCACIÓN"]},
  ["Incluir a la familia en la educación.",
   "Simplificar el esquema de fármacos.",
   "Grupos de apoyo de pacientes."],
  ADA + " · OMS – Adherencia a los tratamientos a largo plazo (2003)")

# CAR-073 · árbol
A("CAR-073", "fumador-dolor-reposo-infradesnivel-st-scasest", "Dolor torácico con infradesnivel del ST",
  "CARDIOLOGÍA ENAM: SÍNDROME CORONARIO SIN ELEVACIÓN DEL ST", "CARDIOLOGÍA",
  ("SCA sin elevación del ST", ["Angina inestable o infarto sin elevación",
   "Manejo inicial: antiagregación doble, anticoagulación y nitratos"]),
  ("Varón de 48 años, gran fumador", ["Dolor opresivo en reposo de 30 min", "Infradesnivel ST inferior y lateral · troponina normal"]),
  Q("¿Elevación persistente del ST?", [
      L("Sí", "Reperfusión urgente", ["Angioplastia primaria"]),
      Q("¿Dolor isquémico con cambios del ST?", [
          L("Sí", "SCASEST", ["Aspirina + P2Y12, heparina", "Nitroglicerina; troponinas seriadas"], path=True),
          L("No", "Otro diagnóstico", ["Seguir estudiando"])],
        edge="No", path=True)], path=True),
  ("Conducta", [("Hacer", True), ("No hacer", False)], [
      ("Fármacos", ["Doble antiagregación", "Solo AINE"]),
      ("Estudios", ["Troponinas seriadas", "Prueba de esfuerzo aguda"])]),
  ["Troponina normal inicial no descarta infarto.",
   "Estratificar el riesgo (GRACE) para la coronariografía.",
   "Estatina de alta intensidad desde el inicio."],
  "ESC – Acute coronary syndromes guidelines (2023)")

# PED-231 · fases
V("fases", "PED-231", "lactante-expuesto-vih-pcr-positiva-dos-veces-tar", "Diagnóstico de VIH en el lactante",
  "PEDIATRÍA ENAM: VIH EN EL LACTANTE", "PEDIATRÍA",
  ("VIH en el lactante", ["En < 18 meses se diagnostica con PCR (no con ELISA)",
   "Dos PCR positivas confirman: TAR inmediato"]),
  ("Lactante de 2 meses expuesto al VIH", ["Madre diagnosticada en el parto", "PCR positiva al 1.º y al 2.º mes"]),
  {"rotulo": "Seguimiento del expuesto", "ans": 2,
   "fases": [("Al nacer", "Profilaxis", "AZT + 3TC + NVP", ["Por el riesgo alto"]),
             ("1.º mes", "PCR", "Positiva", ["Repetir"]),
             ("2.º mes", "PCR", "TAR INMEDIATO", ["Infección confirmada", "Sin esperar CD4"])],
   "curvas": [("Carga viral", ROSE, [0.1, 0.3, 0.6, 0.8, 0.9, 0.9, 0.9])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("TAR de inmediato", True), ("Esperar 12 meses", False), ("Según síntomas", False), ("Según CD4", False)]},
  ["Los anticuerpos maternos persisten hasta 18 meses.",
   "Suspender la lactancia materna en el Perú.",
   "Cotrimoxazol profiláctico desde las 6 semanas."],
  "MINSA – NTS 216: Transmisión materno infantil del VIH (2024) · OMS (2021)")

# INF-110 · matriz
V("matriz", "INF-110", "hsh-papula-indolora-bubones-fistulas-linfogranuloma", "Úlceras genitales y adenopatías",
  "INFECTOLOGÍA ENAM: LINFOGRANULOMA VENÉREO", "INFECTOLOGÍA",
  ("Linfogranuloma venéreo", ["Chlamydia trachomatis serotipos L1-L3",
   "Pápula indolora fugaz y luego bubones que fistulizan"]),
  ("Varón de 24 años, HSH", ["Pápula indolora que curó sola", "Bubones inguinales con fístulas"]),
  {"rotulo": "Agente y hallazgos", "eje_x": "Rasgo", "eje_y": "Agente",
   "cols": ["Úlcera", "Adenopatía"], "rows": ["Chlamydia L1-L3", "H. ducreyi", "Treponema", "Herpes"], "caso": (0, 1),
   "cells": [[("Pápula fugaz", ["Indolora"]), ("BUBONES", ["Fistulizan"])],
             [("Dolorosa, sucia", []), ("Dolorosa, supura", [])],
             [("Indolora, limpia", []), ("Firme, indolora", [])],
             [("Vesículas", ["Dolorosas"]), ("Dolorosa", [])]]},
  ["Tratamiento: doxiciclina 100 mg c/12 h por 21 días.",
   "Signo del surco: ganglios arriba y abajo del ligamento inguinal.",
   "Descartar VIH y sífilis."],
  "CDC – STI Treatment Guidelines (2021) · MINSA – NTS de ITS (2023)")

# GAS-075 · árbol
A("GAS-075", "ascitis-gasa-1-4-hipertension-portal", "Estudio del líquido ascítico",
  "GASTROENTEROLOGÍA ENAM: GRADIENTE ALBÚMINA SUERO-ASCITIS", "GASTROENTEROLOGÍA",
  ("Gradiente albúmina suero-ascitis (GASA)", ["Albúmina sérica menos la del líquido ascítico",
   "≥ 1,1 g/dL: hipertensión portal"]),
  ("Mujer de 55 años", ["Aumento del perímetro abdominal y llenura precoz", "Matidez en flancos · GASA 1,4 g/dL"]),
  Q("¿GASA ≥ 1,1 g/dL?", [
      Q("¿Proteínas en ascitis < 2,5 g/dL?", [
          L("Sí", "HIPERTENSIÓN PORTAL", ["Cirrosis (la más frecuente)"], path=True),
          L("No", "Portal poshepática", ["Falla cardiaca, Budd-Chiari"])],
        edge="Sí", path=True),
      L("No", "Causa peritoneal", ["Carcinomatosis, TB, pancreatitis"])], path=True),
  ("GASA", [("≥ 1,1", True), ("< 1,1", False)], [
      ("Mecanismo", ["Presión portal alta", "Inflamación o tumor peritoneal"]),
      ("Ejemplos", ["Cirrosis, falla cardiaca", "TB peritoneal, carcinomatosis"])]),
  ["Siempre pedir recuento celular y cultivo.",
   "El síndrome de Meigs suele tener GASA alto.",
   "Citología si se sospecha cáncer."],
  "AASLD – Management of ascites (2021) · " + HARRISON)

# CIR-119 · puntaje
V("puntaje", "CIR-119", "dolor-migratorio-blumberg-air-9-cirugia", "Escala AIR en la apendicitis",
  "CIRUGÍA ENAM: APENDICITIS AGUDA", "CIRUGÍA",
  ("Escala AIR", ["Clínica y laboratorio, de 0 a 12 puntos",
   "9-12: probabilidad alta, operar sin más estudios"]),
  ("Mujer de 27 años", ["Dolor de epigastrio a flanco derecho · Blumberg (+)", "Ecografía no concluyente, sin TAC · AIR 9"]),
  {"rotulo": "AIR del caso", "escala": "AIR", "total": 9, "max": 12,
   "total_label": "Puntaje del caso",
   "interpreta": "Probabilidad alta",
   "items": [("Dolor en fosa ilíaca derecha", "1", True), ("Rebote (Blumberg)", "1-3", True),
             ("Vómito, fiebre, leucocitos, PCR", "Resto", True)],
   "bandas": [("0-4", "Bajo", "Observación ambulatoria", False),
              ("5-8", "Intermedio", "Observar e imágenes", False),
              ("9-12", "Alto", "Cirugía", True)]},
  ["Colonoscopía no tiene lugar en la sospecha aguda.",
   "Retrasar la cirugía aumenta la perforación.",
   "En mujeres jóvenes, descartar causa ginecológica."],
  "WSES – Jerusalem guidelines for acute appendicitis (2020) · Andersson M. World J Surg (2008)")

# CIR-120 · tarjetas
V("tarjetas", "CIR-120", "prueba-trendelenburg-torniquete-varices", "Maniobras vasculares",
  "CIRUGÍA ENAM: INSUFICIENCIA VENOSA", "CIRUGÍA",
  ("Prueba de Trendelenburg", ["Vaciar las venas, colocar torniquete y poner de pie",
   "Valora la insuficiencia venosa (safenofemoral y perforantes)"]),
  ("Pregunta de semiología", ["¿Qué valora la prueba de Trendelenburg?"]),
  {"rotulo": "¿Qué evalúa cada maniobra?", "ans": 0, "cards": [
      {"titulo": "TRENDELENBURG", "datos": [
          ("Sistema", "Venoso", True), ("Evalúa", "Válvulas", True),
          ("Uso", "Várices", True)],
       "pie": "Insuficiencia venosa"},
      {"titulo": "Perthes", "datos": [
          ("Sistema", "Venoso profundo", False), ("Evalúa", "Permeabilidad", False),
          ("Uso", "Antes de cirugía", False)],
       "pie": "Caminar con torniquete"},
      {"titulo": "Buerger", "datos": [
          ("Sistema", "Arterial", False), ("Evalúa", "Isquemia", False),
          ("Uso", "Claudicación", False)],
       "pie": "Palidez al elevar"},
      {"titulo": "Índice tobillo-brazo", "datos": [
          ("Sistema", "Arterial", False), ("Evalúa", "Obstrucción", False),
          ("Uso", "Enfermedad arterial", False)],
       "pie": "< 0,9 anormal"}]},
  ["Llenado rápido desde arriba: safena incompetente.",
   "Llenado con torniquete: perforantes incompetentes.",
   "Hoy se confirma con eco Doppler."],
  "Rutherford's Vascular Surgery 10.ª ed. (2022)")

# SP-183 · radial
V("radial", "SP-183", "periurbano-ultraprocesados-obesidad-infantil-regular-publicidad", "Prevención de la obesidad infantil",
  "SALUD PÚBLICA ENAM: OBESIDAD INFANTIL", "SALUD PÚBLICA",
  ("Entornos obesogénicos", ["Acceso fácil a ultraprocesados y poco espacio para el ejercicio",
   "Las políticas públicas logran la prevención más sostenida"]),
  ("Distrito periurbano", ["Escuelas sin alimentación saludable", "Mucho acceso a ultraprocesados"]),
  {"rotulo": "Mapa del tema", "centro": "OBESIDAD", "centro_sub": "¿Qué priorizar?", "ans": 0,
   "items": [("POLÍTICAS", ["Regular publicidad y venta", "Actúa sobre el entorno"]),
             ("Talleres", ["Alcance limitado"]),
             ("Suplementos", ["No corresponde"]),
             ("Controles de peso", ["Detectan, no previenen"])],
   "ruta": ["Ultraprocesados", "Entorno obesogénico", "Cambiar el entorno", "POLÍTICAS"]},
  ["Ley 30021 de alimentación saludable (octógonos).",
   "Kioscos escolares saludables.",
   "Espacios públicos para actividad física."],
  "OMS – Acabar con la obesidad infantil (2016) · Ley 30021 (Perú)")

# INF-111 · embudo
V("embudo", "INF-111", "adulto-disenteria-fiebre-leucocitos-fecales-ciprofloxacino", "Tratamiento de la disentería",
  "INFECTOLOGÍA ENAM: DIARREA DISENTÉRICA", "INFECTOLOGÍA",
  ("Diarrea disentérica", ["Sangre y leucocitos en heces con fiebre: bacteria invasiva",
   "En el adulto: rehidratación y ciprofloxacino"]),
  ("Varón de 20 años", ["5 días de cólico y 4-6 deposiciones con sangre", "Fiebre · leucocitos y sangre oculta en heces"]),
  {"rotulo": "Embudo del tratamiento",
   "inicio": "Disentería febril",
   "candidatos": ["Ciprofloxacino", "Metronidazol", "Loperamida", "Cotrimoxazol"],
   "pasos": [("Loperamida contraindicada con sangre", ["Loperamida"]),
             ("Bacteria invasiva, no ameba; alta resistencia", ["Metronidazol", "Cotrimoxazol"])],
   "final": ("CIPROFLOXACINO", ["3-5 días", "Azitromicina si hay resistencia"]),
   "nota": "Si se ven trofozoítos de Entamoeba, el tratamiento es metronidazol."},
  ["Shigella, Campylobacter y Salmonella son las causas.",
   "Coprocultivo si es grave o persistente.",
   "Hidratación oral en todos los casos."],
  "IDSA – Infectious diarrhea guidelines (2017) · OMS (2023)")

# NEF-093 · puntaje
V("puntaje", "NEF-093", "cateterismo-diabetico-erc-contraste-lesion-renal", "Riesgo de nefropatía por contraste",
  "NEFROLOGÍA ENAM: NEFROPATÍA POR CONTRASTE", "NEFROLOGÍA",
  ("Nefropatía por contraste", ["Lesión renal 48-72 h después del contraste yodado",
   "Mayor riesgo: ERC previa y diabetes"]),
  ("Varón de 57 años", ["Diabetes y ERC (creatinina 1,8)", "Cateterismo por infarto · lesión renal aguda"]),
  {"rotulo": "Factores de riesgo en el caso", "escala": "Factores", "total": 3, "max": 5,
   "total_label": "Factores presentes",
   "interpreta": "Riesgo alto",
   "items": [("ERC previa", "1", True), ("Diabetes", "1", True), ("Contraste intraarterial urgente", "1", True),
             ("Deshidratación", "?", False), ("Edad > 75 años", "0", False)],
   "bandas": [("0-1", "Bajo", "Hidratar si es posible", False),
              ("≥ 2", "Alto", "Suero salino antes y después", True)]},
  ["Sedimento: cilindros granulosos, no leucocitarios.",
   "La FENa suele ser baja al inicio.",
   "Suspender metformina y AINE."],
  "KDIGO – AKI guideline (2012) · ACR Manual on Contrast Media (2024)")

# CB-090 · fases
V("fases", "CB-090", "deficit-mcad-ayuno-movimientos-hipoglucemia", "Qué pasa en el ayuno",
  "CIENCIAS BÁSICAS ENAM: DÉFICIT DE MCAD", "CIENCIAS BÁSICAS",
  ("Déficit de MCAD", ["Falla la beta-oxidación de ácidos grasos de cadena media",
   "En ayuno: hipoglucemia sin cetonas (hipocetósica)"]),
  ("Lactante de 10 días con déficit de MCAD", ["Movimientos involuntarios tras horas de ayuno", "¿Cómo estará la glucemia?"]),
  {"rotulo": "Horas de ayuno", "ans": 2,
   "fases": [("0-4 h", "Glucógeno", "Glucosa normal", ["Reserva hepática"]),
             ("4-12 h", "Grasas", "Beta-oxidación falla", ["Sin cetonas"]),
             ("> 12 h", "Sin energía", "GLUCOSA BAJA", ["Convulsiones", "Letargia"])],
   "curvas": [("Glucosa", ROSE, [0.8, 0.75, 0.6, 0.4, 0.25, 0.15, 0.1]),
              ("Cetonas", VIOLET, [0.1, 0.1, 0.12, 0.12, 0.13, 0.13, 0.14])],
   "chips_titulo": "Glucemia · marcada la correcta",
   "chips": [("Disminuida", True), ("Normal", False), ("Aumento moderado", False), ("Marcado aumento", False)]},
  ["Evitar ayunos prolongados.",
   "En crisis: dextrosa EV.",
   "Se detecta en el tamizaje neonatal ampliado."],
  "Harper. Bioquímica ilustrada 32.ª ed. (2023) · " + NELSON)

# PED-232 · termómetro
V("termometro", "PED-232", "neonato-8-dias-lactancia-bilirrubina-12-observacion", "Ictericia en el neonato sano",
  "PEDIATRÍA ENAM: ICTERICIA POR LECHE MATERNA", "PEDIATRÍA",
  ("Ictericia asociada a la lactancia", ["Bilirrubina indirecta en neonato sano que lacta bien",
   "Por debajo del umbral de fototerapia: observar y seguir lactando"]),
  ("Neonato a término de 8 días", ["Ictericia hasta los muslos", "Bilirrubina 12 · activo, lacta bien"]),
  {"rotulo": "Bilirrubina a término (> 72 h)",
   "niveles": [("< 15", "Bajo umbral", ["OBSERVAR", "Seguir lactando"]),
               ("15-20", "Fototerapia", ["Según factores de riesgo"]),
               ("20-25", "Intensiva", ["Fototerapia intensiva"]),
               ("> 25", "Exanguino", ["Si no responde"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta en este caso", "paso_label": "PASO",
   "pasos": [(1, "Observación", ["Control clínico"], True),
             (2, "Lactancia frecuente", ["8-12 veces al día"], False),
             (3, "Descartar colestasis", ["Si dura > 2-3 semanas"], False)]},
  ["No suspender la lactancia materna.",
   "Bilirrubina directa alta: no es fisiológica.",
   "Usar las curvas de la AAP según horas de vida."],
  "AAP – Hyperbilirubinemia guideline (2022) · " + NELSON)

# GIN-243 · tarjetas
V("tarjetas", "GIN-243", "amenaza-parto-pretermino-nifedipino-insuficiencia-cardiaca", "Tocolíticos y contraindicaciones",
  "OBSTETRICIA ENAM: TOCÓLISIS", "OBSTETRICIA",
  ("Tocolíticos", ["Retrasan el parto 48 h para dar corticoides",
   "Nifedipino: evitar en cardiopatía o hipotensión"]),
  ("Primigesta de 29 semanas", ["Amenaza de parto pretérmino", "Se indica nifedipino: ¿cuándo está contraindicado?"]),
  {"rotulo": "¿Cuál es la contraindicación?", "ans": 0, "cards": [
      {"titulo": "NIFEDIPINO", "datos": [
          ("Tipo", "Bloqueador de calcio", True), ("Evitar en", "Insuficiencia cardiaca", True),
          ("Efecto", "Hipotensión", True)],
       "pie": "Primera línea"},
      {"titulo": "Indometacina", "datos": [
          ("Tipo", "AINE", False), ("Evitar en", "> 32 semanas", False),
          ("Efecto", "Cierra el ductus", False)],
       "pie": "Oligohidramnios"},
      {"titulo": "Atosibán", "datos": [
          ("Tipo", "Antagonista oxitocina", False), ("Evitar en", "Pocas", False),
          ("Efecto", "Bien tolerado", False)],
       "pie": "Costoso"},
      {"titulo": "Betamiméticos", "datos": [
          ("Tipo", "Agonista β2", False), ("Evitar en", "Diabetes, cardiopatía", False),
          ("Efecto", "Hiperglucemia", False)],
       "pie": "En desuso"}]},
  ["No asociar nifedipino con sulfato de magnesio.",
   "Corticoides entre las 24 y 34 semanas.",
   "No se tocoliza si hay corioamnionitis."],
  WILLIAMS + " · ACOG Practice Bulletin 171 (2016)")

# SP-184 · matriz
V("matriz", "SP-184", "inmunizaciones-visita-acta-reunion-mejora-supervision", "Técnicas de control en gestión",
  "SALUD PÚBLICA ENAM: SUPERVISIÓN", "SALUD PÚBLICA",
  ("Técnicas de control", ["Monitoreo, supervisión, evaluación e inspección",
   "Supervisión: verificar y acompañar al equipo para mejorar"]),
  ("Responsable de inmunizaciones", ["Visita, revisa metas y levanta un acta", "Reúne al equipo y propone mejoras"]),
  {"rotulo": "Técnica y rasgos", "eje_x": "Rasgo", "eje_y": "Técnica",
   "cols": ["Cómo", "Incluye"], "rows": ["Monitoreo", "Supervisión", "Evaluación", "Inspección"], "caso": (1, 1),
   "cells": [[("Continuo", ["Indicadores"]), ("Seguir avances", [])],
             [("Visita en sitio", []), ("ASISTENCIA TÉCNICA", ["Acta y mejora"])],
             [("Al final", []), ("Medir resultados", [])],
             [("Verificación", []), ("Cumplir normas", ["Sin asesoría"])]]},
  ["La supervisión es capacitante, no punitiva.",
   "El monitoreo usa indicadores periódicos.",
   "La evaluación compara resultados con metas."],
  "MINSA – Lineamientos de supervisión integral (2016)")

# GAS-076 · puntaje
V("puntaje", "GAS-076", "pancreatitis-previas-ictericia-bilirrubina-4-2-coledocolitiasis", "Probabilidad de coledocolitiasis",
  "GASTROENTEROLOGÍA ENAM: COLEDOCOLITIASIS", "GASTROENTEROLOGÍA",
  ("Coledocolitiasis", ["Cálculo en el colédoco: ictericia y patrón colestásico",
   "Bilirrubina > 4 con litiasis: probabilidad alta"]),
  ("Mujer de 40 años con pancreatitis previas", ["Dolor tras comida grasa, coluria, ictericia", "BT 4,2 · FA 250 · GGT 200"]),
  {"rotulo": "Predictores en el caso", "escala": "Predictores", "total": 3, "max": 4,
   "total_label": "Predictores presentes",
   "interpreta": "Probabilidad alta",
   "items": [("Bilirrubina > 4 mg/dL", "Muy fuerte", True), ("FA y GGT elevadas", "Fuerte", True),
             ("Pancreatitis biliar previa", "Fuerte", True), ("Edad > 55 años", "Moderado", False)],
   "bandas": [("Bajo", "Improbable", "Colecistectomía", False),
              ("Alto", "Coledocolitiasis", "CPRE o colangio-RM", True)]},
  ["Colangitis: agrega fiebre (tríada de Charcot).",
   "Colecistitis: Murphy sin gran ictericia.",
   "Luego colecistectomía."],
  "ASGE – Choledocholithiasis guideline (2019)")

# PED-233 · radial
V("radial", "PED-233", "lactancia-sin-suplemento-rosario-costal-raquitismo", "Signos del raquitismo",
  "PEDIATRÍA ENAM: RAQUITISMO CARENCIAL", "PEDIATRÍA",
  ("Raquitismo carencial", ["Déficit de vitamina D: falla la mineralización del cartílago de crecimiento",
   "Lactancia exclusiva sin suplemento es un factor de riesgo"]),
  ("Lactante de 10 meses", ["Lactancia exclusiva sin suplementos", "Retraso motor · rosario costal"]),
  {"rotulo": "Mapa del tema", "centro": "RAQUITISMO", "centro_sub": "Signos", "ans": 0,
   "items": [("ROSARIO COSTAL", ["Uniones condrocostales", "Signo del caso"]),
             ("Craneotabes", ["Cráneo blando"]),
             ("Muñecas anchas", ["Metáfisis"]),
             ("Piernas arqueadas", ["Al caminar"]),
             ("Fontanela", ["Cierre tardío"])],
   "ruta": ["Poca vitamina D", "Hueso mal mineralizado", "Cartílago crece", "ROSARIO COSTAL"]},
  ["Suplemento: 400 UI/día de vitamina D.",
   "Laboratorio: fosfatasa alcalina alta.",
   "En el escorbuto duele y sangran las encías."],
  NELSON)

# GIN-244 · embudo
V("embudo", "GIN-244", "distocia-hombros-macrosomia-diabetes-gestacional", "Causa materna de macrosomía",
  "OBSTETRICIA ENAM: MACROSOMÍA FETAL", "OBSTETRICIA",
  ("Macrosomía fetal", ["Peso > 4000 g: riesgo de distocia de hombros",
   "La causa materna más frecuente es la diabetes gestacional"]),
  ("Primigesta de 34 años", ["Parto disfuncional y distocia de hombros", "Feto macrosómico"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Macrosomía fetal",
   "candidatos": ["Diabetes gestacional", "Preeclampsia", "Infección urinaria", "RPM"],
   "pasos": [("La preeclampsia restringe el crecimiento", ["Preeclampsia"]),
             ("ITU y RPM no dan macrosomía", ["Infección urinaria", "RPM"])],
   "final": ("DIABETES GESTACIONAL", ["Hiperinsulinismo fetal", "Crecen hombros y tronco"]),
   "nota": "Otros factores: obesidad materna y embarazo prolongado."},
  ["Tamizaje con PTGO entre las 24 y 28 semanas.",
   "Distocia de hombros: maniobra de McRoberts.",
   "Riesgo neonatal: lesión del plexo braquial."],
  WILLIAMS + " · ACOG Practice Bulletin 216 (2020)")

# PED-234 · puntaje
V("puntaje", "PED-234", "tos-perruna-estridor-solo-al-llanto-crup-leve", "Escala de Westley",
  "PEDIATRÍA ENAM: CRUP LEVE", "PEDIATRÍA",
  ("Crup (laringotraqueítis)", ["Tos perruna, disfonía y estridor inspiratorio",
   "Leve: estridor solo al llanto → dexametasona oral y casa"]),
  ("Lactante de 18 meses", ["Tos perruna y disfonía tras un resfrío", "Estridor solo con el llanto"]),
  {"rotulo": "Westley del caso", "escala": "Westley", "total": 1, "max": 17,
   "total_label": "Puntaje del caso",
   "interpreta": "Crup leve",
   "items": [("Estridor solo al agitarse", "1", True), ("Retracciones", "0", False),
             ("Entrada de aire normal", "0", False), ("Sin cianosis", "0", False),
             ("Conciencia normal", "0", False)],
   "bandas": [("≤ 2", "Leve", "Dexametasona oral, casa", True),
              ("3-7", "Moderado", "Dexametasona y observar", False),
              ("≥ 8", "Grave", "Adrenalina nebulizada", False)]},
  ["Dexametasona 0,15-0,6 mg/kg dosis única.",
   "Signos de alarma: estridor en reposo, tiraje.",
   "Causa más frecuente: virus parainfluenza."],
  "AAP / Cochrane – Glucocorticoids for croup (2023) · " + NELSON)

# SP-185 · matriz
V("matriz", "SP-185", "quechuahablante-obesa-hipertensa-nivel-socioeconomico", "Tipos de factores de salud",
  "SALUD PÚBLICA ENAM: DETERMINANTES SOCIALES", "SALUD PÚBLICA",
  ("Determinantes sociales", ["Condiciones en que las personas viven y trabajan",
   "El nivel socioeconómico limita alimentación, educación y acceso"]),
  ("Mujer de 52 años, obesa e hipertensa", ["Poco acceso a alimentos saludables, sedentaria", "Quechuahablante: le cuesta seguir indicaciones"]),
  {"rotulo": "Factor y tipo", "eje_x": "Dato", "eje_y": "Factor",
   "cols": ["Tipo", "Se modifica con"], "rows": ["Nivel socioeconómico", "Edad", "Herencia", "Tecnología"], "caso": (0, 0),
   "cells": [[("DETERMINANTE SOCIAL", []), ("Políticas", ["Ingresos, educación"])],
             [("Biológico", []), ("No se modifica", [])],
             [("Biológico", []), ("No se modifica", [])],
             [("Sistema de salud", []), ("Inversión", [])]]},
  ["Atender en su idioma mejora la adherencia.",
   "Enfoque intercultural en la consejería.",
   "Coordinar con programas sociales."],
  "OMS – Determinantes sociales de la salud (2008) · MINSA – Política de interculturalidad (2016)")

# CB-091 · fases
V("fases", "CB-091", "embrion-8-semanas-movimientos-primeros-tractos-nerviosos", "Neurodesarrollo embrionario",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA DEL SISTEMA NERVIOSO", "CIENCIAS BÁSICAS",
  ("Movimientos embrionarios", ["Se ven por ecografía desde las 8 semanas",
   "Se deben a la aparición de los primeros tractos nerviosos"]),
  ("Pregunta de embriología", ["¿Con qué se relacionan los movimientos a las 8 semanas?"]),
  {"rotulo": "Semanas de gestación", "ans": 1,
   "fases": [("3-4 sem", "Neurulación", "Tubo neural", ["Se cierra"]),
             ("8 sem", "Movimientos", "PRIMEROS TRACTOS", ["Arcos reflejos", "Espontáneos"]),
             ("> 20 sem", "Maduración", "Mielinización", ["Continúa tras nacer"])],
   "curvas": [("Conexiones nerviosas", SKY, [0.05, 0.2, 0.4, 0.55, 0.7, 0.85, 0.95])],
   "chips_titulo": "Relación · marcada la correcta",
   "chips": [("Primeros tractos", True), ("Tractos motores", False), ("Mielinización", False), ("Corticoespinal", False)]},
  ["La mielinización empieza en el segundo trimestre.",
   "Los tractos corticoespinales maduran después.",
   "Déficit de folato: defectos del tubo neural."],
  "Langman. Embriología médica 15.ª ed. (2023) · Moore. Embriología clínica 11.ª ed.")
