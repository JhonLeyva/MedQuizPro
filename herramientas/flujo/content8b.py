"""Bloque 8 · parte B."""
from c8 import F8, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
ROBBINS = "Robbins y Cotran. Patología estructural y funcional 10.ª ed. (2021)"
ADA = "ADA – Standards of Care in Diabetes (2025)"

# CB-085 · tarjetas
V("tarjetas", "CB-085", "medula-osea-celula-gigante-multinucleada-resorcion", "Células del hueso y la médula",
  "CIENCIAS BÁSICAS ENAM: OSTEOCLASTO", "CIENCIAS BÁSICAS",
  ("Remodelado óseo", ["Los osteoblastos forman hueso y los osteoclastos lo reabsorben",
   "El osteoclasto es gigante, multinucleado y deriva del monocito"]),
  ("Pregunta de histología", ["Médula ósea con células gigantes multinucleadas", "Con signos de resorción"]),
  {"rotulo": "¿Qué célula es?", "ans": 0, "cards": [
      {"titulo": "OSTEOCLASTO", "datos": [
          ("Núcleos", "Muchos", True), ("Origen", "Monocito-macrófago", True),
          ("Función", "Reabsorbe hueso", True)],
       "pie": "Lagunas de Howship"},
      {"titulo": "Megacariocito", "datos": [
          ("Núcleos", "Uno multilobulado", False), ("Origen", "Célula madre mieloide", False),
          ("Función", "Forma plaquetas", False)],
       "pie": "Gigante pero no reabsorbe"},
      {"titulo": "Osteoblasto", "datos": [
          ("Núcleos", "Uno", False), ("Origen", "Mesénquima", False),
          ("Función", "Forma hueso", False)],
       "pie": "Fosfatasa alcalina"},
      {"titulo": "Osteocito", "datos": [
          ("Núcleos", "Uno", False), ("Origen", "Osteoblasto", False),
          ("Función", "Mantiene la matriz", False)],
       "pie": "Dentro de lagunas"}]},
  ["RANKL estimula al osteoclasto; la osteoprotegerina lo frena.",
   "Los bisfosfonatos inhiben a los osteoclastos.",
   "En el mieloma se activan y producen lesiones líticas."],
  ROBBINS)

# SP-177 · radial
V("radial", "SP-177", "asentamientos-sin-agua-potable-dengue-determinantes", "Intervenciones contra el dengue",
  "SALUD PÚBLICA ENAM: DETERMINANTES SOCIALES", "SALUD PÚBLICA",
  ("Determinantes sociales de la salud", ["Condiciones de vida que explican la enfermedad",
   "Sin agua potable se almacena agua y proliferan criaderos"]),
  ("Centro de salud con dengue autóctono", ["Aumento de casos por 3 años", "Nuevos asentamientos sin agua potable"]),
  {"rotulo": "Mapa del tema", "centro": "PRIORIDAD", "centro_sub": "¿Qué intervenir?", "ans": 0,
   "items": [("DETERMINANTES", ["Agua y saneamiento", "Actúa sobre la causa"]),
             ("Emergencia", ["Atiende, no previene"]),
             ("Capacitación", ["No cambia el entorno"]),
             ("Vigilancia", ["Detecta, no reduce"])],
   "ruta": ["Sin agua potable", "Almacenan agua", "Criaderos de Aedes", "DETERMINANTES"]},
  ["Trabajo intersectorial con el municipio.",
   "Participación comunitaria en el recojo de inservibles.",
   "El control vectorial complementa, no reemplaza."],
  "OMS – Comisión sobre determinantes sociales de la salud (2008) · MINSA – NTS de vigilancia de Aedes (2021)")

# REU-067 · embudo
V("embudo", "REU-067", "militares-jovenes-sol-cancer-piel-ultravioleta", "Riesgo de cáncer de piel",
  "DERMATOLOGÍA ENAM: CÁNCER DE PIEL", "DERMATOLOGÍA",
  ("Cáncer de piel", ["Basocelular, espinocelular y melanoma",
   "Principal factor de riesgo: radiación ultravioleta solar"]),
  ("Reporte del INEN", ["Aumento de cáncer de piel en militares jóvenes", "Trabajo prolongado al aire libre"]),
  {"rotulo": "Embudo de factores",
   "inicio": "Cáncer de piel en jóvenes expuestos",
   "candidatos": ["Radiación UV", "Benceno", "Radiación ionizante", "Agua contaminada"],
   "pasos": [("El benceno da leucemia, no piel", ["Benceno"]),
             ("Exposición solar al aire libre", ["Radiación ionizante", "Agua contaminada"])],
   "final": ("RADIACIÓN ULTRAVIOLETA", ["Exposición solar prolongada", "Sin fotoprotección"]),
   "nota": "El Perú tiene índices UV extremos, sobre todo en la sierra."},
  ["Protector solar FPS ≥ 30, sombrero y ropa.",
   "Evitar el sol entre las 10 y las 16 horas.",
   "Autoexamen de lunares con la regla ABCDE."],
  "OMS/IARC – Radiación solar y cáncer de piel (2023) · Fitzpatrick. Dermatología 9.ª ed.")

# END-063 · puntaje
V("puntaje", "END-063", "poliuria-baja-12-kg-glucosa-472-hba1c-12-insulina", "¿Cuándo iniciar con insulina?",
  "ENDOCRINOLOGÍA ENAM: INSULINA DE INICIO", "ENDOCRINOLOGÍA",
  ("Hiperglucemia sintomática grave", ["Glucosa ≥ 300, HbA1c ≥ 10 % o síntomas catabólicos",
   "Se inicia insulina aunque sea diabetes tipo 2"]),
  ("Varón de 63 años, IMC 34", ["Polidipsia, poliuria, polifagia", "Baja 12 kg · glucosa 472 · HbA1c 12,7 %"]),
  {"rotulo": "Criterios de insulina en el caso", "escala": "Criterios", "total": 4, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Iniciar insulina",
   "items": [("Glucosa ≥ 300 mg/dL", "1", True), ("HbA1c ≥ 10 %", "1", True),
             ("Síntomas de hiperglucemia", "1", True), ("Pérdida de peso", "1", True)],
   "bandas": [("0", "Estable", "Metformina y dieta", False),
              ("≥ 1", "Descompensada", "Insulina basal", True)]},
  ["Al controlarse, se puede pasar a antidiabéticos orales.",
   "Agregar metformina si no hay contraindicación.",
   "Descartar cetoacidosis y estado hiperosmolar."],
  ADA)

# INF-107 · fases
V("fases", "INF-107", "serumista-chanchamayo-vacuna-amarilla-10-dias", "Vacuna antiamarílica",
  "INFECTOLOGÍA ENAM: FIEBRE AMARILLA", "INFECTOLOGÍA",
  ("Vacuna contra la fiebre amarilla", ["Virus vivo atenuado, dosis única de por vida",
   "Protege a partir de los 10 días de aplicada"]),
  ("Serumista de 25 años", ["Viajará a Chanchamayo (selva central)", "¿Cuántos días antes debe vacunarse?"]),
  {"rotulo": "Tiempo tras la vacuna", "ans": 1,
   "fases": [("Día 0", "Aplicación", "Vacuna", ["Subcutánea"]),
             ("Día 10", "Inmunidad", "PROTECCIÓN", ["Viajar desde aquí", "Certificado válido"]),
             ("Por vida", "Dosis única", "Sin refuerzo", ["OMS desde 2016"])],
   "curvas": [("Anticuerpos", SKY, [0.0, 0.1, 0.6, 0.9, 0.95, 0.95, 0.95])],
   "chips_titulo": "Días antes del viaje · marcado el correcto",
   "chips": [("10", True), ("5", False), ("20", False), ("30", False)]},
  ["Contraindicada en < 6 meses, embarazo e inmunosupresión.",
   "Precaución en mayores de 60 años.",
   "Obligatoria para zonas endémicas del Perú."],
  "MINSA – NTS 196: Esquema nacional de vacunación (2022) · OMS (2016)")

# PED-224 · matriz
V("matriz", "PED-224", "hamburguesa-disenteria-anemia-plaquetopenia-e-coli", "Diarrea con sangre en el niño",
  "PEDIATRÍA ENAM: SÍNDROME URÉMICO HEMOLÍTICO", "PEDIATRÍA",
  ("Colitis hemorrágica", ["E. coli productora de toxina Shiga (O157:H7) por carne mal cocida",
   "Puede causar síndrome urémico hemolítico: anemia, plaquetopenia, falla renal"]),
  ("Preescolar de 4 años", ["Diarrea con moco y sangre tras comer hamburguesa", "Hb 7,5 · plaquetas 90 000 · leucocitosis"]),
  {"rotulo": "Agente y complicación", "eje_x": "Rasgo", "eje_y": "Agente",
   "cols": ["Fuente", "Complicación"], "rows": ["E. coli O157", "Shigella", "Campylobacter"], "caso": (0, 1),
   "cells": [[("Carne mal cocida", []), ("SHU", ["Anemia y plaquetopenia"])],
             [("Persona a persona", []), ("Convulsiones", ["SHU raro"])],
             [("Aves de corral", []), ("Guillain-Barré", [])]]},
  ["No dar antibióticos ni antidiarreicos: aumentan el riesgo de SHU.",
   "Vigilar diuresis, creatinina y hemograma.",
   "Frotis: esquistocitos."],
  NELSON + " · CDC – E. coli productora de toxina Shiga (2024)")

# GIN-237 · puntaje
V("puntaje", "GIN-237", "nst-20-minutos-aceleraciones-sin-desaceleraciones-reactivo", "Test no estresante",
  "OBSTETRICIA ENAM: MONITOREO FETAL", "OBSTETRICIA",
  ("Test no estresante (NST)", ["Valora la reactividad de la FCF a los movimientos",
   "Reactivo = bienestar fetal"]),
  ("Gestante de 40 semanas", ["NST de 20 minutos", "Movimientos, aceleraciones típicas, sin desaceleraciones"]),
  {"rotulo": "Criterios del NST en el caso", "escala": "NST", "total": 4, "max": 4,
   "total_label": "Criterios cumplidos",
   "interpreta": "NST reactivo",
   "items": [("≥ 2 aceleraciones en 20 min", "1", True), ("Asociadas a movimientos", "1", True),
             ("Variabilidad normal", "1", True), ("Sin desaceleraciones", "1", True)],
   "bandas": [("< 4", "No reactivo", "Prolongar a 40 min o PBF", False),
              ("4 de 4", "Reactivo", "Bienestar fetal", True)]},
  ["Positivo o negativo se usa para el test estresante.",
   "Aceleración: ≥ 15 latidos por ≥ 15 segundos.",
   "No reactivo no es sinónimo de hipoxia."],
  WILLIAMS + " · ACOG Practice Bulletin 229 (2021)")

# GIN-238 · tarjetas
V("tarjetas", "GIN-238", "popq-punto-aa-union-uretrovesical", "Puntos del POP-Q",
  "GINECOLOGÍA ENAM: SISTEMA POP-Q", "GINECOLOGÍA",
  ("Sistema POP-Q", ["Seis puntos vaginales medidos respecto al himen",
   "Aa: pared anterior, 3 cm del meato; equivale a la unión uretrovesical"]),
  ("Pregunta de uroginecología", ["¿A qué corresponde el punto Aa?"]),
  {"rotulo": "¿Qué marca cada punto?", "ans": 0, "cards": [
      {"titulo": "PUNTO Aa", "datos": [
          ("Pared", "Anterior", True), ("Ubicación", "3 cm del meato", True),
          ("Equivale a", "Unión uretrovesical", True)],
       "pie": "Rango -3 a +3"},
      {"titulo": "Punto Ba", "datos": [
          ("Pared", "Anterior", False), ("Ubicación", "Lo más declive", False),
          ("Equivale a", "Resto de pared", False)],
       "pie": "Cistocele"},
      {"titulo": "Punto C", "datos": [
          ("Pared", "Apical", False), ("Ubicación", "Borde cervical", False),
          ("Equivale a", "Cuello o cúpula", False)],
       "pie": "Prolapso uterino"},
      {"titulo": "Punto D", "datos": [
          ("Pared", "Apical", False), ("Ubicación", "Fondo de saco", False),
          ("Equivale a", "Fórnix posterior", False)],
       "pie": "No existe sin útero"}]},
  ["Ap y Bp miden la pared posterior (rectocele).",
   "Negativo: por encima del himen; positivo: por fuera.",
   "Se mide con la paciente pujando."],
  "Bump RC et al. AJOG (1996) · ACOG Practice Bulletin 214 (2019)")

# CIR-115 · termómetro
V("termometro", "CIR-115", "postrado-pierna-blanca-edema-masivo-flegmasia-alba", "Gravedad de la trombosis venosa",
  "CIRUGÍA ENAM: FLEGMASÍA ALBA DOLENS", "CIRUGÍA",
  ("Flegmasía alba dolens", ["TVP iliofemoral masiva: pierna edematosa, dolorosa y blanca",
   "Si progresa a la circulación colateral: flegmasía cerúlea"]),
  ("Varón de 65 años, postrado 6 meses", ["Pierna derecha con edema masivo, dolor y palidez", "Homans (++) · dúplex positivo"]),
  {"rotulo": "Espectro de la TVP",
   "niveles": [("TVP distal", "Pantorrilla", ["Edema leve"]),
               ("Alba dolens", "Iliofemoral", ["PIERNA BLANCA", "Edema masivo"]),
               ("Cerúlea", "Obstrucción total", ["Cianosis, isquemia"]),
               ("Gangrena", "Necrosis venosa", ["Amputación"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo en este caso", "paso_label": "PASO",
   "pasos": [(1, "Anticoagulación inmediata", ["Heparina"], True),
             (2, "Elevar la pierna", ["Vigilar pulsos"], False),
             (3, "Trombólisis dirigida", ["Si progresa"], False)]},
  ["La palidez se debe a espasmo arterial y edema.",
   "Buscar TEP asociado.",
   "Profilaxis en todo paciente postrado."],
  "CHEST – Antithrombotic therapy for VTE (2021) · Rutherford's Vascular Surgery 10.ª ed.")

# PED-225 · matriz
V("matriz", "PED-225", "lactante-18-meses-oma-amoxicilina-10-dias", "Duración del antibiótico en la otitis",
  "PEDIATRÍA ENAM: OTITIS MEDIA AGUDA", "PEDIATRÍA",
  ("Otitis media aguda", ["Amoxicilina a dosis alta (80-90 mg/kg/día)",
   "La duración depende de la edad y la gravedad"]),
  ("Lactante de 18 meses", ["Tos, rinorrea, fiebre, irritabilidad", "Tímpano hiperémico y abombado"]),
  {"rotulo": "Edad y duración", "eje_x": "Dato", "eje_y": "Edad",
   "cols": ["Duración", "Por qué"], "rows": ["< 2 años", "2-5 años", "≥ 6 años"], "caso": (0, 0),
   "cells": [[("10 DÍAS", ["Todos los casos"]), ("Más fracasos", ["Con esquemas cortos"])],
             [("7 días", ["Leve o moderada"]), ("Buena evolución", [])],
             [("5-7 días", []), ("Menor riesgo", [])]]},
  ["Grave u otorrea: 10 días a cualquier edad.",
   "Alergia no grave: cefdinir o cefuroxima.",
   "Sin mejoría en 48-72 h: amoxicilina-clavulánico."],
  "AAP – Clinical practice guideline: acute otitis media (2013) · " + NELSON)

# GIN-239 · radial
V("radial", "GIN-239", "preeclampsia-hellp-plaquetas-80000-desprendimiento", "Complicaciones del HELLP",
  "OBSTETRICIA ENAM: SÍNDROME HELLP", "OBSTETRICIA",
  ("Síndrome HELLP", ["Hemólisis, enzimas hepáticas elevadas y plaquetas bajas",
   "Forma grave de preeclampsia con riesgo de DPP"]),
  ("Primigesta de 38 semanas", ["Cefalea y escotomas · PA 160/100", "Plaquetas 80 000 · TGO 80 · DHL 700"]),
  {"rotulo": "Mapa del tema", "centro": "HELLP", "centro_sub": "Complicaciones", "ans": 0,
   "items": [("DPP", ["Desprendimiento de placenta", "La más probable aquí"]),
             ("CID", ["Coagulopatía"]),
             ("Eclampsia", ["Convulsiones"]),
             ("Hematoma hepático", ["Rotura"]),
             ("Falla renal", ["Oliguria"])],
   "ruta": ["Hipertensión grave", "Daño endotelial", "Vasos placentarios", "DPP"]},
  ["A término: sulfato de magnesio y terminar la gestación.",
   "Placenta previa no se relaciona con la preeclampsia.",
   "Controlar plaquetas, DHL y transaminasas."],
  WILLIAMS + " · ACOG Practice Bulletin 222 (2020)")

# INF-108 · embudo
V("embudo", "INF-108", "coito-anal-receptivo-tenesmo-secrecion-gonococo", "Proctitis de transmisión sexual",
  "INFECTOLOGÍA ENAM: PROCTITIS GONOCÓCICA", "INFECTOLOGÍA",
  ("Proctitis infecciosa", ["Dolor anal, tenesmo y secreción mucopurulenta",
   "Tras coito anal receptivo: gonococo y Chlamydia"]),
  ("Varón de 21 años", ["Coito anal receptivo hace 4 días", "Dolor anal, urgencia defecatoria, secreción purulenta"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Proctitis aguda",
   "candidatos": ["Gonococo", "Treponema", "Yersinia", "Cryptosporidium"],
   "pasos": [("Transmisión sexual, no alimentaria", ["Yersinia", "Cryptosporidium"]),
             ("Secreción purulenta, no chancro", ["Treponema"])],
   "final": ("NEISSERIA GONORRHOEAE", ["Ceftriaxona 500 mg IM", "Más doxiciclina por Chlamydia"]),
   "nota": "Pedir también VIH, sífilis y hepatitis B."},
  ["Incubación corta: 2-7 días.",
   "Tratar a la pareja sexual.",
   "Linfogranuloma venéreo: proctitis grave en HSH."],
  "CDC – STI Treatment Guidelines (2021) · MINSA – NTS de ITS (2023)")

# SP-178 · radial
V("radial", "SP-178", "colegio-programa-escolar-dengue-eliminar-criaderos", "Educación escolar en dengue",
  "SALUD PÚBLICA ENAM: PREVENCIÓN DEL DENGUE", "SALUD PÚBLICA",
  ("Prevención del dengue en la escuela", ["Los escolares llevan prácticas a sus hogares",
   "Prioridad: eliminar criaderos del Aedes aegypti"]),
  ("Colegio en zona de alta incidencia", ["El director coordina con el centro de salud", "¿Qué acción priorizar con los alumnos?"]),
  {"rotulo": "Mapa del tema", "centro": "ESCOLARES", "centro_sub": "¿Qué enseñar?", "ans": 0,
   "items": [("CRIADEROS", ["Tapar, lavar, escobillar", "Eliminar inservibles"]),
             ("Signos de alarma", ["Útil, no previene"]),
             ("Antipiréticos", ["Manejo del enfermo"]),
             ("Laboratorio", ["No es de alumnos"])],
   "ruta": ["Alta incidencia", "Alumnos en casa", "Menos criaderos", "CRIADEROS"]},
  ["Revisar floreros, llantas y tanques cada semana.",
   "Usar repelente y mosquiteros.",
   "Alumnos como agentes de cambio en su familia."],
  "MINSA – Plan nacional de prevención del dengue (2024) · OPS (2023)")

# NEU-069 · árbol
A("NEU-069", "albanil-fumador-hemoptisis-sibilancia-unilateral-tac", "Hemoptisis en el fumador",
  "NEUMOLOGÍA ENAM: SOSPECHA DE CÁNCER DE PULMÓN", "NEUMOLOGÍA",
  ("Sospecha de cáncer de pulmón", ["Fumador > 40 años con hemoptisis o sibilancia localizada",
   "Primer estudio: tomografía de tórax con contraste"]),
  ("Albañil de 55 años, fumador pesado", ["Disnea, tos seca y hemoptisis", "MV disminuido y sibilancias en el lado derecho"]),
  Q("¿Fumador con signos de obstrucción localizada?", [
      Q("¿Tomografía con lesión?", [
          L("Sí", "TC → BRONCOSCOPÍA", ["TC de tórax primero", "Luego biopsia"], path=True),
          L("No", "Broncoscopía igual", ["Si persiste la hemoptisis"])],
        edge="Sí", path=True),
      L("No", "Buscar otra causa", ["TB, bronquiectasias"])], path=True),
  ("Estudios", [("TC de tórax", True), ("PET", False)], [
      ("Cuándo", ["Estudio inicial", "Para estadificar"]),
      ("Aporta", ["Masa y ganglios", "Metástasis"])]),
  ["Sibilancia unilateral fija: obstrucción bronquial.",
   "Descartar tuberculosis con baciloscopía.",
   "La ecografía no evalúa masas centrales."],
  "NCCN – Non-small cell lung cancer (2025) · " + HARRISON)

# CB-086 · embudo
V("embudo", "CB-086", "bombero-humo-plasticos-hidroxicobalamina-orina-roja", "Orina roja tras un antídoto",
  "CIENCIAS BÁSICAS ENAM: HIDROXICOBALAMINA", "CIENCIAS BÁSICAS",
  ("Hidroxicobalamina", ["Antídoto del cianuro en víctimas de humo",
   "Es roja: tiñe orina y piel de rojo sin causar daño"]),
  ("Bombero de 50 años", ["12 h en incendio de plásticos · COHb 30 %", "Tras hidroxicobalamina: mejora y orina roja"]),
  {"rotulo": "Embudo de causas",
   "inicio": "Orina roja tras tratamiento",
   "candidatos": ["Hidroxicobalamina", "Mioglobinuria", "Hematuria", "Porfiria"],
   "pasos": [("Sin trauma muscular ni dolor", ["Mioglobinuria"]),
             ("Aparece tras el antídoto", ["Hematuria", "Porfiria"])],
   "final": ("HIDROXICOBALAMINA", ["Cromaturia benigna", "Dura varios días"]),
   "nota": "Puede alterar pruebas colorimétricas de laboratorio."},
  ["Humo de plásticos: CO y cianuro a la vez.",
   "Lactato alto sugiere intoxicación por cianuro.",
   "Oxígeno al 100 % para el monóxido."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# TRA-053 · árbol
A("TRA-053", "atropello-pelvis-inestable-shock-faja-pelvica", "Fractura de pelvis con shock",
  "TRAUMATOLOGÍA ENAM: FRACTURA DE PELVIS", "TRAUMATOLOGÍA",
  ("Fractura de pelvis inestable", ["Sangrado retroperitoneal masivo",
   "Si hay shock: estabilizar la pelvis de inmediato (faja o sábana)"]),
  ("Varón de 30 años atropellado", ["Hipotenso y taquicárdico pese a los cristaloides", "Pelvis inestable · fractura de ramas"]),
  Q("¿Pelvis inestable con shock?", [
      Q("¿Otra fuente de sangrado?", [
          L("No", "ESTABILIZAR LA PELVIS", ["Faja pélvica o sábana", "Transfusión"], path=True),
          L("Sí: abdomen", "Laparotomía", ["Si FAST positivo"])],
        edge="Sí", path=True),
      L("No", "TC de pelvis", ["Si está estable"])], path=True),
  ("Después de estabilizar", [("Si sigue inestable", True), ("Estable", False)], [
      ("Opción", ["Embolización o empaquetamiento", "TC con contraste"]),
      ("Fijación", ["Externa urgente", "Definitiva luego"])]),
  ["La faja se coloca sobre los trocánteres mayores.",
   "No mover la pelvis repetidamente.",
   "Buscar lesión de uretra antes de la sonda."],
  ATLS + " · WSES – Pelvic trauma guidelines (2017)")

# GIN-240 · termómetro
V("termometro", "GIN-240", "diabetes-gestacional-ayunas-130-insulina", "Control de la diabetes gestacional",
  "OBSTETRICIA ENAM: DIABETES GESTACIONAL", "OBSTETRICIA",
  ("Diabetes gestacional", ["Primero dieta y ejercicio con automonitoreo",
   "Si no se logra la meta: insulina (de elección)"]),
  ("Primigesta de 24 semanas", ["En dieta y ejercicio", "Glucosa en ayunas 130-140 mg/dL"]),
  {"rotulo": "Glucosa en ayunas",
   "niveles": [("< 95", "En meta", ["Seguir con dieta"]),
               ("95-105", "Límite", ["Reforzar dieta"]),
               ("106-129", "Alta", ["Iniciar fármaco"]),
               ("≥ 130", "Muy alta", ["INSULINA", "130-140 mg/dL"])],
   "caso_nivel": 3, "ruta_titulo": "Conducta en este caso", "paso_label": "PASO",
   "pasos": [(1, "Iniciar insulina", ["NPH ± rápida"], True),
             (2, "Automonitoreo", ["Ayunas y posprandial"], False),
             (3, "Control fetal", ["Crecimiento y líquido"], False)]},
  ["Metas: ayunas < 95; 1 h < 140; 2 h < 120 mg/dL.",
   "La metformina cruza la placenta: segunda línea.",
   "Reevaluar con PTGO a las 4-12 semanas posparto."],
  "ACOG Practice Bulletin 190 (2018) · " + ADA)

# INF-109 · fases
V("fases", "INF-109", "tb-sensible-cuarto-mes-bk-positiva-fracaso", "Evolución del tratamiento de TB",
  "INFECTOLOGÍA ENAM: FRACASO DEL TRATAMIENTO", "INFECTOLOGÍA",
  ("Seguimiento del tratamiento de TB", ["Baciloscopía mensual de control",
   "BK positiva desde el cuarto mes: fracaso"]),
  ("Mujer de 34 años con TB sensible", ["Cuarto mes de tratamiento", "La baciloscopía sigue positiva"]),
  {"rotulo": "Meses de tratamiento", "ans": 2,
   "fases": [("Mes 2", "Fin fase 1", "Conversión", ["BK negativa esperada"]),
             ("Mes 3", "Fase 2", "Seguimiento", ["BK mensual"]),
             ("Mes 4", "BK positiva", "FRACASO", ["Prueba de sensibilidad", "Descartar resistencia"])],
   "curvas": [("Bacilos esperados", ROSE, [0.95, 0.6, 0.3, 0.15, 0.1, 0.05, 0.05])],
   "chips_titulo": "Condición de egreso · marcada la correcta",
   "chips": [("Fracaso", True), ("Conversión", False), ("Pérdida de seguimiento", False), ("Reacción adversa", False)]},
  ["Pérdida de seguimiento: interrupción ≥ 30 días.",
   "Pedir prueba molecular y cultivo con sensibilidad.",
   "Ajustar el esquema según el resultado."],
  "MINSA – NTS 200: Atención integral de la tuberculosis (2023)")

# CIR-116 · árbol
A("CIR-116", "chofer-dolor-perianal-fiebre-masa-fluctuante-drenaje", "Dolor perianal con fiebre",
  "CIRUGÍA ENAM: ABSCESO PERIANAL", "CIRUGÍA",
  ("Absceso perianal", ["Infección de las glándulas anales (criptas)",
   "Si hay fluctuación: drenaje quirúrgico inmediato"]),
  ("Chofer de 35 años", ["Dolor perianal agudo y fiebre alta de 48 h", "Masa inflamatoria fluctuante de 2 cm, hora 7"]),
  Q("¿Masa fluctuante?", [
      L("Sí", "DRENAJE QUIRÚRGICO", ["Incisión y desbridamiento", "Antibiótico solo si hay celulitis o diabetes"], path=True),
      L("No: induración", "Antibiótico y control", ["Reevaluar en 24-48 h"])], path=True),
  ("Opciones", [("Drenaje", True), ("Solo antibiótico", False)], [
      ("Resultado", ["Resuelve la colección", "No llega al pus"]),
      ("Riesgo", ["Fístula en 30-50 %", "Extensión y sepsis"])]),
  ["Ser sedentario (chofer) es factor de riesgo.",
   "Descartar gangrena de Fournier en diabéticos.",
   "La punción aspirativa no basta."],
  "ASCRS – Anorectal abscess and fistula guideline (2022)")

# END-064 · puntaje
V("puntaje", "END-064", "obeso-glucemias-153-146-diabetes-metformina", "Diagnóstico de diabetes",
  "ENDOCRINOLOGÍA ENAM: DIABETES TIPO 2", "ENDOCRINOLOGÍA",
  ("Diagnóstico de diabetes", ["Dos glucemias en ayunas ≥ 126 mg/dL en días distintos",
   "En obesos sin descompensación: metformina y estilo de vida"]),
  ("Varón de 54 años, obeso, asintomático", ["Glucemias en ayunas: 153, 115 y 146 mg/dL", "Glucosuria negativa"]),
  {"rotulo": "Glucemias del caso", "escala": "Glucemias", "total": 2, "max": 3,
   "total_label": "Glucemias ≥ 126",
   "interpreta": "Diabetes confirmada",
   "items": [("153 mg/dL", "1", True), ("115 mg/dL", "0", False), ("146 mg/dL", "1", True)],
   "bandas": [("0-1", "No confirmada", "Repetir o PTGO", False),
              ("≥ 2", "Diabetes", "Metformina + estilo de vida", True)]},
  ["100-125 mg/dL: glucosa alterada en ayunas.",
   "HbA1c ≥ 6,5 % también diagnostica.",
   "La insulina se reserva para hiperglucemia grave."],
  ADA)

# PED-226 · fases
V("fases", "PED-226", "hijo-madre-diabetica-hiperinsulinismo-hipoglucemia", "Hipoglucemia del hijo de madre diabética",
  "PEDIATRÍA ENAM: HIJO DE MADRE DIABÉTICA", "PEDIATRÍA",
  ("Hijo de madre diabética", ["La glucosa materna estimula al páncreas fetal",
   "Al nacer persiste el hiperinsulinismo y cae la glucosa"]),
  ("Pregunta de neonatología", ["¿Cuál es la causa de la hipoglucemia neonatal?"]),
  {"rotulo": "Del embarazo al nacimiento", "ans": 2,
   "fases": [("Embarazo", "Hiperglucemia", "Glucosa pasa", ["Por la placenta"]),
             ("Feto", "Células beta", "Hiperplasia", ["Mucha insulina"]),
             ("Nacimiento", "Primeras horas", "HIPERINSULINISMO", ["Sin aporte materno", "Hipoglucemia"])],
   "curvas": [("Insulina", VIOLET, [0.2, 0.5, 0.8, 0.9, 0.9, 0.5, 0.3]),
              ("Glucosa", ROSE, [0.8, 0.8, 0.8, 0.7, 0.2, 0.4, 0.6])],
   "chips_titulo": "Causa · marcada la correcta",
   "chips": [("Hiperinsulinismo fetal", True), ("Hipotrofia beta", False), ("Glucógeno bajo", False), ("Hipoglucemia materna", False)]},
  ["Glucemia seriada desde la primera hora.",
   "Alimentación precoz; dextrosa EV si es sintomática.",
   "También: macrosomía, policitemia, hipocalcemia."],
  NELSON)

# NEU-070 · termómetro
V("termometro", "NEU-070", "epoc-ph-7-29-pco2-65-oxigeno-controlado", "Gravedad de la exacerbación de EPOC",
  "NEUMOLOGÍA ENAM: EXACERBACIÓN DE EPOC", "NEUMOLOGÍA",
  ("Exacerbación de EPOC", ["Broncodilatadores, corticoides y oxígeno controlado",
   "Con acidosis respiratoria: considerar ventilación no invasiva"]),
  ("Varón de 68 años con EPOC", ["Disnea, SatO₂ 86 %, sibilancias difusas", "pH 7,29 · pCO₂ 65 · sin consolidación"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "Ambulatorio", ["Broncodilatador"]),
               ("Moderada", "Hospital", ["Sin acidosis"]),
               ("Grave", "Acidosis", ["pH < 7,35, pCO₂ alta", "HIPERCAPNIA"]),
               ("Crítica", "UCI", ["Intubación"])],
   "caso_nivel": 2, "ruta_titulo": "Tratamiento en este caso", "paso_label": "PASO",
   "pasos": [(1, "BD + corticoide + O₂ controlado", ["Meta SatO₂ 88-92 %"], True),
             (2, "Ventilación no invasiva", ["Si persiste la acidosis"], False),
             (3, "Antibiótico", ["Si el esputo es purulento"], False)]},
  ["El oxígeno a alto flujo empeora la hipercapnia.",
   "Prednisona 40 mg por 5 días.",
   "Los mucolíticos no sirven en la crisis."],
  "GOLD – Global strategy for COPD (2025)")

# NEF-090 · radial
V("radial", "NEF-090", "estrechamientos-ureter-calculo-union-ureterovesical", "Dónde se detienen los cálculos",
  "UROLOGÍA ENAM: LITIASIS URETERAL", "UROLOGÍA",
  ("Estrechamientos del uréter", ["Unión pieloureteral, cruce ilíaco y unión ureterovesical",
   "La unión ureterovesical es la más estrecha"]),
  ("Pregunta de anatomía", ["¿Dónde es más probable que se atasque un cálculo?"]),
  {"rotulo": "Mapa del tema", "centro": "URÉTER", "centro_sub": "Estrechamientos", "ans": 0,
   "items": [("UNIÓN URETEROVESICAL", ["La más estrecha", "Síntomas miccionales"]),
             ("Unión pieloureteral", ["Dolor lumbar"]),
             ("Cruce ilíaco", ["Dolor en flanco"]),
             ("Psoas", ["No es estrechez"])],
   "ruta": ["Cálculo desciende", "Uréter se estrecha", "Pared vesical", "UNIÓN URETEROVESICAL"]},
  ["Cálculo distal: dolor irradiado a genitales.",
   "< 5 mm suelen expulsarse solos.",
   "Tamsulosina ayuda en los distales."],
  "Campbell-Walsh Urology 12.ª ed. · EAU (2024)")

# PED-227 · matriz
V("matriz", "PED-227", "cia-civ-pca-hiperflujo-pulmonar-qp-qs", "Cardiopatías congénitas",
  "PEDIATRÍA ENAM: CORTOCIRCUITO IZQUIERDA-DERECHA", "PEDIATRÍA",
  ("Cardiopatías acianóticas", ["CIA, CIV y PCA: cortocircuito de izquierda a derecha",
   "Más flujo pulmonar que sistémico (Qp/Qs > 1): insuficiencia cardiaca"]),
  ("Pregunta de cardiología pediátrica", ["¿Qué mecanismo explica la insuficiencia cardiaca?"]),
  {"rotulo": "Tipo y fisiología", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Cortocircuito", "Flujo pulmonar"], "rows": ["Acianótica", "Cianótica"], "caso": (0, 1),
   "cells": [[("Izquierda a derecha", ["CIA, CIV, PCA"]), ("QP/QS > 1", ["Hiperflujo"])],
             [("Derecha a izquierda", ["Fallot"]), ("Disminuido", ["Hipoflujo"])]]},
  ["Clínica: taquipnea, sudor al lactar, poca ganancia de peso.",
   "Tratamiento inicial: diuréticos.",
   "Sin cierre: hipertensión pulmonar (Eisenmenger)."],
  NELSON + " · Park's Pediatric Cardiology 7.ª ed.")

# PED-228 · embudo
V("embudo", "PED-228", "lactante-40-dias-formula-urticaria-sibilancias-aplv", "Reacción tras la primera fórmula",
  "PEDIATRÍA ENAM: ALERGIA A LA LECHE DE VACA", "PEDIATRÍA",
  ("Alergia a proteínas de leche de vaca", ["Reacción inmunológica, a menudo mediada por IgE",
   "Urticaria, vómitos, sibilancias tras la fórmula"]),
  ("Lactante de 40 días", ["Con lactancia exclusiva recibe fórmula", "Urticaria generalizada y sibilancias"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Urticaria tras la fórmula",
   "candidatos": ["Alergia a la leche", "Intolerancia a lactosa", "Urticaria infecciosa", "Picadura"],
   "pasos": [("Inmunológica, no digestiva", ["Intolerancia a lactosa"]),
             ("Inmediata tras el alimento", ["Urticaria infecciosa", "Picadura"])],
   "final": ("ALERGIA A LA LECHE DE VACA", ["Suspender la fórmula", "Fórmula extensamente hidrolizada"]),
   "nota": "La intolerancia a la lactosa da diarrea y gases, no habones ni sibilancias."},
  ["Mantener la lactancia materna.",
   "Si hay anafilaxia: adrenalina IM.",
   "Suele tolerarse hacia los 1-3 años."],
  "ESPGHAN – Cow's milk protein allergy guideline (2024) · " + NELSON)

# OFT-053 · tarjetas
V("tarjetas", "OFT-053", "piscina-cloro-ardor-ojo-rojo-conjuntivitis-quimica", "Tipos de conjuntivitis",
  "OFTALMOLOGÍA ENAM: CONJUNTIVITIS QUÍMICA", "OFTALMOLOGÍA",
  ("Conjuntivitis", ["Ojo rojo con visión normal",
   "La causa se orienta por la historia y la secreción"]),
  ("Niño de 10 años", ["Ardor y enrojecimiento tras nadar en piscina", "Hiperemia sin afectación visual"]),
  {"rotulo": "¿Qué tipo es?", "ans": 0, "cards": [
      {"titulo": "QUÍMICA", "datos": [
          ("Causa", "Cloro, irritantes", True), ("Síntoma", "Ardor", True),
          ("Secreción", "Escasa, acuosa", True)],
       "pie": "Lavado y lágrimas"},
      {"titulo": "Alérgica", "datos": [
          ("Causa", "Alérgenos", False), ("Síntoma", "Prurito", False),
          ("Secreción", "Mucosa", False)],
       "pie": "Estacional, atopia"},
      {"titulo": "Bacteriana", "datos": [
          ("Causa", "Bacterias", False), ("Síntoma", "Legañas", False),
          ("Secreción", "Purulenta", False)],
       "pie": "Antibiótico tópico"},
      {"titulo": "Viral", "datos": [
          ("Causa", "Adenovirus", False), ("Síntoma", "Arenilla", False),
          ("Secreción", "Acuosa", False)],
       "pie": "Adenopatía preauricular"}]},
  ["Suele resolver en 24-48 horas.",
   "Usar lentes de natación.",
   "Álcalis o ácidos: irrigación abundante urgente."],
  "AAO – Preferred Practice Pattern: Conjunctivitis (2023)")

# PED-229 · árbol
A("PED-229", "lactante-regurgitacion-asfixia-pico-de-pajaro-acalasia", "Regurgitación y falla de crecimiento",
  "PEDIATRÍA ENAM: ACALASIA", "PEDIATRÍA",
  ("Acalasia", ["El esfínter esofágico inferior no se relaja y falta la peristalsis",
   "Esofagograma: dilatación con «pico de pájaro»"]),
  ("Lactante de 1 mes", ["Regurgitaciones, asfixia y retraso del crecimiento", "Esofagograma: sin peristaltismo, pico de pájaro"]),
  Q("¿Esofagograma alterado?", [
      Q("¿Estrechez distal lisa con dilatación?", [
          L("Sí", "ACALASIA", ["Manometría confirma", "Dilatación o miotomía"], path=True),
          L("No", "Estenosis o esofagitis", ["Endoscopía"])],
        edge="Sí", path=True),
      L("No", "Reflujo fisiológico", ["Medidas posturales"])], path=True),
  ("Diferencias", [("Acalasia", True), ("Atresia", False)], [
      ("Clínica", ["Regurgitación progresiva", "Desde la primera toma"]),
      ("Estudio", ["Pico de pájaro", "Sonda no pasa"])]),
  ["Rara en lactantes; más común en adultos.",
   "Tratamiento: miotomía de Heller o dilatación.",
   "Riesgo de aspiración y neumonías."],
  NELSON)

# SP-179 · tarjetas
V("tarjetas", "SP-179", "jefe-impone-ordenes-sin-opinion-autoritario", "Estilos de liderazgo",
  "SALUD PÚBLICA ENAM: LIDERAZGO AUTORITARIO", "SALUD PÚBLICA",
  ("Estilos de liderazgo", ["Autoritario, democrático, ausente y transformacional",
   "Autoritario: decide solo y exige obediencia"]),
  ("Jefe de un establecimiento", ["Exige cumplir órdenes", "No escucha la opinión del equipo"]),
  {"rotulo": "¿Qué estilo ejerce?", "ans": 0, "cards": [
      {"titulo": "AUTORITARIO", "datos": [
          ("Decisión", "Solo el jefe", True), ("Equipo", "Obedece", True),
          ("Útil en", "Emergencias", False)],
       "pie": "Baja motivación"},
      {"titulo": "Democrático", "datos": [
          ("Decisión", "Compartida", False), ("Equipo", "Participa", False),
          ("Útil en", "Planificación", False)],
       "pie": "Más compromiso"},
      {"titulo": "Ausente", "datos": [
          ("Decisión", "Nadie decide", False), ("Equipo", "Sin guía", False),
          ("Útil en", "Nunca", False)],
       "pie": "Laissez-faire"},
      {"titulo": "Transformacional", "datos": [
          ("Decisión", "Visión común", False), ("Equipo", "Inspirado", False),
          ("Útil en", "Cambios", False)],
       "pie": "Motiva e innova"}]},
  ["El estilo se adapta a la situación (liderazgo situacional).",
   "El autoritario sirve en crisis breves.",
   "El democrático mejora el clima laboral."],
  "OPS – Liderazgo en salud pública (2019)")

# CIR-117 · fases
V("fases", "CIR-117", "dolor-anal-subito-nodulo-purpura-trombectomia", "Trombosis hemorroidal según el tiempo",
  "CIRUGÍA ENAM: TROMBOSIS HEMORROIDAL", "CIRUGÍA",
  ("Trombosis hemorroidal externa", ["Nódulo violáceo y muy doloroso tras un esfuerzo",
   "Antes de 72 h: trombectomía con anestesia local"]),
  ("Mujer de 45 años", ["Dolor anal súbito tras subir escaleras", "Tumor púrpura de 1 cm a hora 5"]),
  {"rotulo": "Horas desde el inicio", "ans": 0,
   "fases": [("< 72 horas", "Dolor máximo", "TROMBECTOMÍA", ["Escisión con anestesia local"]),
             ("> 72 horas", "Dolor cede", "Conservador", ["Baños de asiento, AINE"]),
             ("Semanas", "Reabsorción", "Pliegue cutáneo", ["Plicoma"])],
   "curvas": [("Dolor", ROSE, [0.9, 0.95, 0.8, 0.5, 0.3, 0.15, 0.05])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Trombectomía", True), ("Escleroterapia", False), ("Esfinterotomía", False), ("Hospitalización", False)]},
  ["La escleroterapia es para hemorroides internas.",
   "La esfinterotomía trata la fisura anal.",
   "Laxantes y fibra para evitar el esfuerzo."],
  "ASCRS – Hemorrhoids guideline (2024)")

# CAR-072 · puntaje
V("puntaje", "CAR-072", "insuficiencia-cardiaca-mareo-lengua-seca-suspender-furosemida", "Hipovolemia por diurético",
  "CARDIOLOGÍA ENAM: INSUFICIENCIA CARDIACA", "CARDIOLOGÍA",
  ("Insuficiencia cardiaca crónica", ["IECA, betabloqueador y espironolactona mejoran la supervivencia",
   "La furosemida solo trata la congestión: se ajusta al estado de volumen"]),
  ("Varón de 69 años con IC", ["Mareo por 48 h · PA 100/60 · lengua seca", "Sin crepitantes · laboratorio normal"]),
  {"rotulo": "Signos de hipovolemia en el caso", "escala": "Signos", "total": 4, "max": 4,
   "total_label": "Signos presentes",
   "interpreta": "Exceso de diurético",
   "items": [("Mareo", "1", True), ("PA baja-normal", "1", True),
             ("Lengua seca", "1", True), ("Sin congestión pulmonar", "1", True)],
   "bandas": [("Congestión", "Sobrecarga", "Subir furosemida", False),
              ("Hipovolemia", "Deshidratado", "Suspender furosemida", True)]},
  ["No suspender fármacos que mejoran la supervivencia.",
   "Reiniciar el diurético si reaparece la congestión.",
   "Enseñar a pesarse a diario."],
  "ESC – Heart failure guidelines (2021, actualización 2023)")

# SP-180 · embudo
V("embudo", "SP-180", "poblado-rural-300-habitantes-mortalidad-materna-vigilancia", "Mortalidad materna rural",
  "SALUD PÚBLICA ENAM: VIGILANCIA COMUNITARIA", "SALUD PÚBLICA",
  ("Vigilancia comunitaria", ["Agentes comunitarios identifican gestantes y signos de alarma",
   "Acerca la vigilancia a poblaciones pequeñas y dispersas"]),
  ("Ámbito sanitario rural", ["Mortalidad materna elevada", "Casos en un poblado de < 300 habitantes"]),
  {"rotulo": "Embudo de intervenciones",
   "inicio": "Muertes maternas rurales",
   "candidatos": ["Vigilancia comunitaria", "Hospital", "Ginecobstetras", "Banco de sangre"],
   "pasos": [("No factible en < 300 habitantes", ["Hospital", "Banco de sangre"]),
             ("El problema es el acceso", ["Ginecobstetras"])],
   "final": ("VIGILANCIA COMUNITARIA", ["Censo de gestantes", "Referencia oportuna"]),
   "nota": "Se complementa con la casa de espera materna."},
  ["Las demoras en decidir y llegar causan muertes.",
   "Plan de parto con la familia.",
   "Sistema de transporte comunal."],
  "MINSA – Plan estratégico para reducir la mortalidad materna (2023)")

# GIN-241 · matriz
V("matriz", "GIN-241", "embrion-8-mm-sin-latido-cuello-cerrado-aborto-retenido", "Tipos de aborto",
  "OBSTETRICIA ENAM: ABORTO RETENIDO", "OBSTETRICIA",
  ("Aborto retenido", ["Embrión muerto que no se expulsa",
   "Embrión ≥ 7 mm sin latido confirma la muerte"]),
  ("Multípara de 8 semanas", ["Dolor pélvico y sangrado · cuello cerrado", "Embrión de 8 mm sin actividad cardiaca"]),
  {"rotulo": "Tipo de aborto", "eje_x": "Dato", "eje_y": "Tipo",
   "cols": ["Cuello", "Embrión"], "rows": ["Amenaza", "Retenido", "Completo"], "caso": (1, 1),
   "cells": [[("Cerrado", []), ("Vivo", ["Con latido"])],
             [("Cerrado", []), ("SIN LATIDO", ["Embrión 8 mm"])],
             [("Cerrado", []), ("Útero vacío", ["Ya expulsado"])]]},
  ["Manejo: misoprostol, AMEU o expectante.",
   "Aborto séptico: fiebre y dolor uterino.",
   "Inevitable: cuello abierto con sangrado."],
  "ACOG Practice Bulletin 200 (2018) · MINSA – Guía de emergencias obstétricas (2023)")

# PED-230 · termómetro
V("termometro", "PED-230", "alacran-sialorrea-nistagmo-dificultad-respiratoria-faboterapia", "Gravedad del escorpionismo",
  "PEDIATRÍA ENAM: ESCORPIONISMO", "PEDIATRÍA",
  ("Escorpionismo", ["La toxina libera neurotransmisores autonómicos",
   "Con síntomas sistémicos: faboterapia (antiveneno)"]),
  ("Escolar de 5 años de zona rural", ["Tras picadura de alacrán: tos y dificultad respiratoria", "Sialorrea, nistagmo, debilidad de piernas"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "Local", ["Dolor, parestesia"]),
               ("Moderado", "Sistémico", ["Vómitos, sudor, taquicardia"]),
               ("Grave", "Compromiso vital", ["RESPIRATORIO", "Sialorrea, nistagmo"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta en este caso", "paso_label": "PASO",
   "pasos": [(1, "Faboterapia precoz", ["Antiveneno EV"], True),
             (2, "Soporte y monitoreo", ["Oxígeno, vía EV"], False),
             (3, "Referir a hospital", ["UCI si hay edema pulmonar"], False)]},
  ["Niños: más graves por menor peso.",
   "No usar atropina de rutina.",
   "Analgesia y frío local en los leves."],
  "MINSA – NTS 129: Manejo de accidentes por animales ponzoñosos (2016)")

# CIR-118 · fases
V("fases", "CIR-118", "plastron-apendicular-7-dias-sin-absceso-conservador", "Evolución de la apendicitis complicada",
  "CIRUGÍA ENAM: PLASTRÓN APENDICULAR", "CIRUGÍA",
  ("Plastrón apendicular", ["Masa inflamatoria que bloquea al apéndice",
   "Si está estable y sin absceso: manejo conservador"]),
  ("Varón de 25 años, 7 días de plastrón", ["Estable, con antibióticos", "Masa de 3 cm · sin absceso en la ecografía"]),
  {"rotulo": "Etapas y conducta", "ans": 1,
   "fases": [("< 72 horas", "Apendicitis", "Cirugía", ["Apendicectomía"]),
             ("Plastrón", "Masa estable", "CONSERVADOR", ["Antibiótico y observar"]),
             ("Absceso", "Colección", "Drenaje", ["Percutáneo"]),
             ("6-8 semanas", "Resuelto", "Diferida", ["Si hay recurrencia"])],
   "curvas": [("Inflamación", ROSE, [0.5, 0.9, 0.8, 0.6, 0.4, 0.2, 0.1])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("Observación", True), ("Laparotomía", False), ("Apendicectomía abierta", False), ("Laparoscopía", False)]},
  ["Operar un plastrón formado lesiona asas.",
   "Si empeora o hay peritonitis: cirugía.",
   "Mayores de 40 años: colonoscopía para descartar cáncer."],
  "WSES – Jerusalem guidelines for acute appendicitis (2020)")
