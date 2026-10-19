"""Bloque 6 · parte K."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
GUYTON = "Guyton y Hall – Tratado de fisiología médica 14.ª ed. (2021)"
GOLDFRANK = "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)"

# PED-134 · fases
V("fases", "PED-134", "prematuro-31-semanas-membrana-hialina-ductus", "Membrana hialina y ductus",
  "PEDIATRÍA ENAM: DUCTUS ARTERIOSO EN EL PREMATURO", "PEDIATRÍA",
  ("Membrana hialina y ductus arterioso", ["El ductus persistente es la cardiopatía más asociada",
   "Al mejorar el pulmón cae la resistencia pulmonar y el ductus se abre más"]),
  ("RN de 31 semanas y 1600 g", ["Quejido, aleteo, SatO₂ 90% con FiO₂ 100%", "Rx: vidrio esmerilado con broncograma aéreo"]),
  {"rotulo": "Evolución del prematuro", "ans": 1,
   "fases": [("Nacimiento", "0-6 h", "Membrana hialina", ["Falta de surfactante"]),
             ("Días 3-5", "Mejora el pulmón", "DUCTUS PERSISTENTE", ["Soplo, pulsos saltones"]),
             ("Semanas", "Si persiste", "Cierre", ["Ibuprofeno o paracetamol"])],
   "curvas": [("RVP", SKY, [0.95, 0.8, 0.55, 0.4, 0.3, 0.25, 0.2]),
              ("Shunt", ROSE, [0.1, 0.2, 0.5, 0.75, 0.8, 0.6, 0.3])],
   "chips_titulo": "Cardiopatía · marcada la correcta",
   "chips": [("Ductus arterioso", True), ("CIA", False), ("CIV", False), ("Canal AV", False)]},
  ["El ductus del prematuro se cierra menos por inmadurez.",
   "Con surfactante el pulmón mejora rápido y aparece el cortocircuito.",
   "Signos: soplo continuo, precordio hiperactivo, pulsos saltones."],
  "European Consensus Guidelines on RDS (2022) · " + NELSON)

# END-039 · árbol
A("END-039", "hipoglucemia-insulina-alta-nodulo-pancreatico-reseccion", "Insulinoma",
  "ENDOCRINOLOGÍA ENAM: INSULINOMA", "ENDOCRINOLOGÍA",
  ("Insulinoma", ["Tumor neuroendocrino del páncreas que secreta insulina",
   "Casi siempre benigno y único: la cirugía lo cura"]),
  ("Mujer de 50 años con pérdidas de conciencia", ["Diaforesis, piel fría, desorientación", "Insulina alta · nódulo pancreático de 2 cm"]),
  Q("¿Tumor localizado y resecable?", [
      L("Sí", "RESECCIÓN QUIRÚRGICA", ["Enucleación o pancreatectomía parcial"], path=True),
      L("No, metastásico", "Tratamiento médico", ["Diazóxido, análogos de somatostatina"])], path=True),
  ("Tríada de Whipple", [("Criterio", True)], [
      ("1", ["Síntomas de hipoglucemia"]),
      ("2", ["Glucosa baja documentada"]),
      ("3", ["Mejoría al dar glucosa"])]),
  ["Prueba de ayuno de 72 h: glucosa baja con insulina y péptido C altos.",
   "Péptido C bajo con insulina alta: insulina exógena.",
   "Descartar MEN 1 si hay otros tumores endocrinos."],
  "Endocrine Society – Evaluation and management of adult hypoglycemic disorders (2009, act. 2023) · NANETS – Pancreatic NET guidelines (2020)")

# SP-093 · fases
V("fases", "SP-093", "adolescentes-hb-mayor-12-hierro-acido-folico", "Suplementación en adolescentes",
  "SALUD PÚBLICA ENAM: SUPLEMENTACIÓN PREVENTIVA", "SALUD PÚBLICA",
  ("Suplementación preventiva en adolescentes", ["Mujeres adolescentes sin anemia: hierro + ácido fólico",
   "Previene anemia y defectos del tubo neural futuros"]),
  ("Campaña de salud en un colegio", ["Alumnas con Hb > 12 g/dL", "¿Qué suplemento preventivo?"]),
  {"rotulo": "Plan en la adolescente", "ans": 1,
   "fases": [("Tamizaje", "Campaña", "Hemoglobina", ["> 12: sin anemia"]),
             ("Prevención", "Semanal", "HIERRO + ÁCIDO FÓLICO", ["60 mg + 400 µg, 3 meses"]),
             ("Si hay anemia", "Diario", "Tratamiento", ["Dosis terapéutica"])],
   "curvas": [],
   "chips_titulo": "Suplemento · marcado el correcto",
   "chips": [("Hierro + ácido fólico", True), ("Fólico + cobre", False), ("B12 + zinc", False), ("Complejo B + zinc", False)]},
  ["La adolescencia aumenta las necesidades de hierro (crecimiento y menstruación).",
   "Ajustar la Hb por altitud en zonas altas.",
   "Acompañar con consejería en alimentación rica en hierro."],
  "MINSA – NTS N.° 213-MINSA/DGIESP-2024 (Prevención y control de la anemia) · OMS – Suplementación intermitente con hierro y ácido fólico (2011)")

# NEF-057 · fases
V("fases", "NEF-057", "tc-contraste-diabetico-creatinina-25-hidratacion", "Nefropatía por contraste",
  "NEFROLOGÍA ENAM: NEFROPATÍA POR CONTRASTE", "NEFROLOGÍA",
  ("Lesión renal por contraste", ["Sube la creatinina 24-72 h después del contraste yodado",
   "Tratamiento: hidratación EV isotónica y evitar nefrotóxicos"]),
  ("Varón de 56 años diabético e hipertenso", ["2 días tras TC con contraste: oliguria", "Creatinina 2.5 · cilindros granulosos"]),
  {"rotulo": "Evolución", "ans": 2,
   "fases": [("Contraste", "Día 0", "TC con contraste", ["Diabetes = riesgo"]),
             ("Lesión", "24-72 h", "↑ Creatinina", ["Oliguria, cilindros"]),
             ("Manejo", "Inicio", "HIDRATACIÓN EV", ["Suero isotónico"]),
             ("Recupera", "7-14 días", "Vuelve a la basal", ["La mayoría"])],
   "curvas": [("Creat.", ROSE, [0.2, 0.5, 0.8, 0.9, 0.7, 0.45, 0.25])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Hidratación EV", True), ("Diálisis urgente", False), ("N-acetilcisteína", False), ("Diuréticos", False)]},
  ["Prevención: hidratar antes y después del contraste en pacientes de riesgo.",
   "La N-acetilcisteína no ha demostrado beneficio.",
   "Diálisis solo si hay indicaciones urgentes."],
  "KDIGO – Clinical practice guideline for acute kidney injury (2012) · ACR/NKF – Consensus on IV contrast in CKD (2020)")

# INF-065 · tarjetas
V("tarjetas", "INF-065", "vih-inicio-tar-respuesta-carga-viral", "Pruebas de VIH y su uso",
  "INFECTOLOGÍA ENAM: SEGUIMIENTO DEL TAR", "INFECTOLOGÍA",
  ("Eficacia del TAR", ["Se mide con la carga viral en plasma",
   "Meta: indetectable (< 50 copias) a los 6 meses"]),
  ("Varón de 37 años con VIH confirmado", ["Diarrea crónica y consunción", "Inicia TAR: ¿cómo evaluar su eficacia?"]),
  {"rotulo": "¿Para qué sirve cada prueba?", "ans": 0, "cards": [
      {"titulo": "CARGA VIRAL", "datos": [
          ("Uso", "Eficacia del TAR", True), ("Cuándo", "1-3 meses, luego c/6 m", True),
          ("Meta", "< 50 copias/mL", True)],
       "pie": "Detecta la falla virológica"},
      {"titulo": "ELISA", "datos": [
          ("Uso", "Tamizaje", False), ("Cuándo", "Diagnóstico", False),
          ("Meta", "No aplica", False)],
       "pie": "Siempre positivo tras la infección"},
      {"titulo": "Western blot", "datos": [
          ("Uso", "Confirmación", False), ("Cuándo", "Diagnóstico", False),
          ("Meta", "No aplica", False)],
       "pie": "Hoy reemplazado"},
      {"titulo": "Antígeno p24", "datos": [
          ("Uso", "Diagnóstico temprano", False), ("Cuándo", "2-3 semanas", False),
          ("Meta", "No aplica", False)],
       "pie": "Incluido en ELISA 4.ª gen."}]},
  ["El CD4 mide la inmunidad y guía las profilaxis.",
   "Carga viral > 200 copias tras 6 meses: falla virológica.",
   "Revisar adherencia antes de cambiar el esquema."],
  "MINSA – NTS N.° 204-MINSA/DGIESP-2023 (VIH) · DHHS – Adult and adolescent ARV guidelines (2024)")

# NEU-035 · matriz
V("matriz", "NEU-035", "epoc-ph-732-pco2-60-ventilacion-no-invasiva", "Soporte ventilatorio en EPOC",
  "NEUMOLOGÍA ENAM: VENTILACIÓN NO INVASIVA", "NEUMOLOGÍA",
  ("Ventilación no invasiva en EPOC", ["Acidosis respiratoria (pH 7.25-7.35, PaCO₂ > 45)",
   "Reduce la intubación y la mortalidad"]),
  ("Varón de 72 años con EPOC", ["Trastorno del sensorio", "pH 7.32, PaCO₂ 60, PaO₂ 52"]),
  {"rotulo": "Opciones de soporte", "eje_x": "Aspecto", "eje_y": "Soporte",
   "cols": ["Cuándo", "Riesgo en EPOC"], "rows": ["Cánula binasal", "Reservorio", "VNI", "Intubación"], "caso": (2, 0),
   "cells": [[("Hipoxemia leve", []), ("Poco control de FiO₂", [])],
             [("Hipoxemia grave", []), ("Hipercapnia por O₂ alto", [])],
             [("pH 7.25-7.35", ["PaCO₂ > 45"]), ("Vigilar tolerancia", [])],
             [("pH < 7.25 o falla de VNI", []), ("Neumonía, destete difícil", [])]]},
  ["Meta de SatO₂ en EPOC: 88-92%.",
   "Contraindicaciones de VNI: paro, vómitos, no protege la vía aérea.",
   "Reevaluar gases 1-2 horas después de iniciar VNI."],
  "GOLD – Global Strategy for COPD (2025) · ERS/ATS – Noninvasive ventilation for acute respiratory failure (2017)")

# PSI-026 · puntaje
V("puntaje", "PSI-026", "agitacion-paranoia-midriasis-tabique-perforado-cocaina", "Toxíndrome por cocaína",
  "PSIQUIATRÍA ENAM: INTOXICACIÓN POR COCAÍNA", "PSIQUIATRÍA",
  ("Intoxicación por cocaína", ["Toxíndrome simpaticomimético + psicosis paranoide",
   "Perforación del tabique nasal: consumo inhalado crónico"]),
  ("Varón de 32 años muy agitado", ["«Me persiguen unos sicarios» · movimientos estereotipados", "PA 165/95, FC 115, T 38.5 °C, midriasis · tabique perforado"]),
  {"rotulo": "Hallazgos en el caso", "escala": "Simpaticomimético", "total": 6, "max": 7,
   "total_label": "Hallazgos presentes",
   "interpreta": "Intoxicación por cocaína",
   "items": [("Hipertensión", "1", True), ("Taquicardia", "1", True), ("Hipertermia", "1", True),
             ("Midriasis", "1", True), ("Agitación y paranoia", "1", True),
             ("Tabique nasal perforado", "1", True), ("Diaforesis", "1", False)],
   "bandas": [("0-2", "Poco probable", "Buscar otra causa", False),
              ("≥ 3", "Cocaína", "Benzodiacepinas; enfriar; evitar betabloqueantes", True)]},
  ["Anticolinérgico: piel seca; simpaticomimético: piel sudorosa.",
   "Fentanilo: miosis y depresión respiratoria.",
   "Descartar IAM y disección aórtica si hay dolor torácico."],
  GOLDFRANK)

# CIR-070 · embudo
V("embudo", "CIR-070", "alto-voltaje-mano-ruidos-arritmicos-ecg", "Quemadura eléctrica",
  "CIRUGÍA ENAM: QUEMADURA ELÉCTRICA", "CIRUGÍA",
  ("Quemadura eléctrica de alto voltaje", ["La corriente atraviesa el cuerpo: riesgo de arritmias",
   "Primer examen: ECG y monitoreo cardiaco"]),
  ("Varón de 20 años con cable de alto voltaje", ["Heridas profundas en la mano derecha", "Ruidos cardiacos arrítmicos, pulsos presentes"]),
  {"rotulo": "Embudo de exámenes",
   "inicio": "Quemadura eléctrica con arritmia",
   "candidatos": ["Electrocardiograma", "Rx de mano", "Eco Doppler", "Electromiografía", "TC cerebral"],
   "pasos": [("Ruidos arrítmicos: riesgo de muerte súbita", ["Rx de mano", "Electromiografía"]),
             ("Pulsos presentes y sin trauma craneal", ["Eco Doppler", "TC cerebral"])],
   "final": ("ELECTROCARDIOGRAMA", ["Monitoreo 24 h si es anormal", "CPK y orina: rabdomiólisis"]),
   "nota": "La lesión de piel subestima el daño profundo: vigilar síndrome compartimental."},
  ["Rabdomiólisis: hidratar para diuresis de 1-1.5 mL/kg/h.",
   "Puede requerir fasciotomía.",
   "Las fórmulas de hidratación por SCQ subestiman la necesidad."],
  "ABA – Advanced Burn Life Support Course (2022) · " + ATLS)

# NEF-058 · termómetro
V("termometro", "NEF-058", "calculo-ureteral-distal-menor-6-mm-terapia-expulsiva", "Litiasis ureteral según tamaño",
  "NEFROLOGÍA ENAM: TERAPIA EXPULSIVA", "NEFROLOGÍA",
  ("Litiasis ureteral distal pequeña", ["Cálculos < 6 mm suelen expulsarse solos",
   "Tratamiento médico: analgesia + tamsulosina"]),
  ("Mujer de 45 años con cólico que cedió", ["TC: cálculo < 6 mm", "Tercio inferior del uréter"]),
  {"rotulo": "Tamaño del cálculo",
   "niveles": [("≤ 6 mm", "Probable expulsión", ["~ 70-90%"]),
               ("6-10 mm", "Posible", ["~ 50%"]),
               ("> 10 mm", "Improbable", ["Requiere intervención"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "TRATAMIENTO MÉDICO", ["AINE + tamsulosina"], True),
             (2, "Control en 4-6 semanas", ["Imagen para confirmar expulsión"], False),
             (3, "Intervenir si falla", ["Ureteroscopia o LEOC"], False)]},
  ["Drenaje urgente (doble J o nefrostomía) solo si hay infección, monorreno o falla renal.",
   "Filtrar la orina para analizar el cálculo.",
   "Beber 2-3 litros al día previene recurrencias."],
  "EAU – Guidelines on urolithiasis (2024) · AUA – Medical management of kidney stones (2019)")

# INF-066 · matriz
V("matriz", "INF-066", "herida-fierro-oxidado-vacuna-9-anos-toxoide", "Profilaxis antitetánica",
  "INFECTOLOGÍA ENAM: PROFILAXIS DEL TÉTANOS", "INFECTOLOGÍA",
  ("Profilaxis antitetánica", ["Depende del tipo de herida y de las dosis previas",
   "Herida sucia con última dosis hace > 5 años: toxoide"]),
  ("Varón de 30 años con herida por fierro oxidado", ["Herida de 5 × 2 cm con secreción", "Esquema completo, última dosis hace 9 años"]),
  {"rotulo": "Según vacunación y herida", "eje_x": "Herida", "eje_y": "Vacunación",
   "cols": ["Limpia", "Sucia o tetanígena"], "rows": ["< 3 dosis o no sabe", "3 dosis, < 5 años", "3 dosis, 5-10 años", "3 dosis, > 10 años"], "caso": (2, 1),
   "cells": [[("Toxoide", []), ("Toxoide + IgT", ["Inmunoglobulina humana"])],
             [("Nada", []), ("Nada", [])],
             [("Nada", []), ("TOXOIDE", ["Refuerzo"])],
             [("Toxoide", []), ("Toxoide", [])]]},
  ["Limpiar y desbridar la herida es fundamental.",
   "La inmunoglobulina humana es la de elección (no la equina).",
   "Adultos: refuerzo con dT cada 10 años."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 (Esquema Nacional de Vacunación) · CDC – Tetanus prophylaxis in wound management (2024)")

# PED-135 · radial
V("radial", "PED-135", "parto-vaginal-contacto-piel-a-piel-primera-hora", "Contacto piel a piel",
  "PEDIATRÍA ENAM: CONTACTO PIEL A PIEL", "PEDIATRÍA",
  ("Contacto precoz piel a piel", ["Inmediatamente al nacer y durante la primera hora",
   "Si madre y bebé están estables"]),
  ("Pregunta de concepto", ["Parto vaginal sin complicaciones", "¿Cuándo el contacto piel a piel?"]),
  {"rotulo": "Mapa del tema", "centro": "PIEL A PIEL", "centro_sub": "Recién nacido", "ans": 0,
   "items": [("PRIMERA HORA", ["Inmediato al nacer", "Al menos 1 hora sin interrupción"]),
             ("Temperatura", ["Previene la hipotermia"]),
             ("Lactancia", ["Inicio precoz"]),
             ("Glucosa", ["Más estable"]),
             ("Vínculo", ["Apego madre-bebé"])],
   "ruta": ["Parto sin complicaciones", "Secar y evaluar", "Sobre el pecho de la madre", "PRIMERA HORA"]},
  ["Pinzamiento tardío del cordón (1-3 min) en el RN vigoroso.",
   "Pesar y medir después de la primera hora.",
   "También se promueve tras la cesárea si es posible."],
  "OMS – Recomendaciones sobre cuidados intraparto (2018) · MINSA – NTS de atención integral del recién nacido")

# HEM-025 · termómetro
V("termometro", "HEM-025", "nino-gingivorragia-plaquetas-12000-inmunoglobulina", "PTI en el niño",
  "HEMATOLOGÍA ENAM: PÚRPURA TROMBOCITOPÉNICA INMUNE", "HEMATOLOGÍA",
  ("Púrpura trombocitopénica inmune", ["Plaquetas bajas aisladas en un niño sano, a menudo tras un virus",
   "Tratar si hay sangrado mucoso: inmunoglobulina o corticoide"]),
  ("Preescolar de 3 años con gingivorragia", ["Petequias en piel y mucosas, sin visceromegalias", "Plaquetas 12 000 · TP y TTPa normales"]),
  {"rotulo": "Sangrado y plaquetas",
   "niveles": [("> 30 000", "Sin sangrado", ["Observar"]),
               ("< 30 000", "Solo piel", ["Observar en casa"]),
               ("< 20 000", "Sangrado mucoso", ["Tratar"])],
   "caso_nivel": 2, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "INMUNOGLOBULINA EV", ["Subida rápida de plaquetas"], True),
             (2, "Corticoide", ["Alternativa"], False),
             (3, "Transfundir plaquetas", ["Solo sangrado grave"], False)]},
  ["El tratamiento se decide por el sangrado, no solo por el número.",
   "Plasma y crioprecipitado no sirven: no hay coagulopatía.",
   "80% se resuelve en 6-12 meses."],
  "ASH – Guidelines for immune thrombocytopenia (2019) · " + NELSON)

# CB-047 · puntaje
V("puntaje", "CB-047", "reciclador-baterias-cefalea-diarrea-plomo", "Intoxicación crónica por plomo",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR PLOMO", "CIENCIAS BÁSICAS",
  ("Saturnismo", ["Exposición laboral (baterías, fundición, pintura)",
   "Cefalea, fatiga, cólico, artralgias, anemia y neuropatía"]),
  ("Varón de 35 años reciclador de baterías", ["3 meses de cefalea, diarrea, fatiga", "Dolores articulares"]),
  {"rotulo": "Hallazgos de sospecha", "escala": "Saturnismo", "total": 4, "max": 6,
   "total_label": "Hallazgos presentes",
   "interpreta": "Sospecha de intoxicación por plomo",
   "items": [("Exposición a baterías", "1", True), ("Cefalea y fatiga", "1", True),
             ("Síntomas digestivos", "1", True), ("Artralgias", "1", True),
             ("Anemia con punteado basófilo", "1", False), ("Neuropatía (muñeca caída)", "1", False)],
   "bandas": [("0-1", "Poco probable", "Buscar otra causa", False),
              ("≥ 2", "Probable", "Plumbemia; retirar la exposición; quelación si es alta", True)]},
  ["Ribete de Burton: línea gris azulada en las encías.",
   "Inhibe la síntesis del hem: protoporfirina alta.",
   "Quelantes: EDTA cálcico, succímero (DMSA)."],
  GOLDFRANK + " · CDC/NIOSH – Adult blood lead epidemiology and surveillance (2024)")

# CIR-071 · termómetro
V("termometro", "CIR-071", "agua-caliente-ampollas-blanquea-espesor-parcial-superficial", "Profundidad de la quemadura",
  "CIRUGÍA ENAM: QUEMADURA DE ESPESOR PARCIAL", "CIRUGÍA",
  ("Quemadura de espesor parcial superficial", ["Afecta epidermis y dermis superficial",
   "Ampollas, roja, blanquea a la presión y muy dolorosa"]),
  ("Mujer de 40 años quemada con agua caliente", ["Antebrazo derecho, hace 1 hora", "Eritema que blanquea y ampollas"]),
  {"rotulo": "Profundidad",
   "niveles": [("Epidermis", "Superficial", ["Eritema, sin ampollas"]),
               ("Dermis sup.", "Parcial superficial", ["Ampollas, blanquea"]),
               ("Dermis prof.", "Parcial profunda", ["No blanquea, menos dolor"]),
               ("Total", "Espesor total", ["Blanca, acartonada, indolora"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Agua corriente 20 min", ["Tibia, no hielo"], False),
             (2, "CURACIÓN Y APÓSITO", ["Cicatriza en 2-3 semanas"], True),
             (3, "Injerto", ["Si es profunda o total"], False)]},
  ["Parcial superficial: cicatriza sin injerto en < 3 semanas.",
   "La profunda puede requerir escisión e injerto.",
   "Vacuna antitetánica según antecedentes."],
  "ABA – Advanced Burn Life Support Course (2022) · ISBI – Practice guidelines for burn care (2016)")

# CB-048 · puntaje
V("puntaje", "CB-048", "organofosforado-atropina-piel-seca-midriasis-anticolinergico", "Toxíndrome anticolinérgico",
  "CIENCIAS BÁSICAS ENAM: TOXICIDAD ANTICOLINÉRGICA", "CIENCIAS BÁSICAS",
  ("Toxicidad anticolinérgica", ["Exceso de atropina al tratar el organofosforado",
   "Piel roja, caliente y seca, midriasis, delirio, íleo y retención urinaria"]),
  ("Varón de 27 años tratado por pesticida", ["Tras revertir los síntomas: agitado, FC 130, T 38.5 °C", "Piel seca y roja, midriasis, íleo, globo vesical"]),
  {"rotulo": "Signos en el caso", "escala": "Anticolinérgico", "total": 8, "max": 8,
   "total_label": "Signos presentes",
   "interpreta": "Toxíndrome anticolinérgico completo",
   "items": [("Piel rubicunda", "1", True), ("Hipertermia", "1", True), ("Piel seca", "1", True),
             ("Delirio y agitación", "1", True), ("Midriasis y visión borrosa", "1", True),
             ("Taquicardia", "1", True), ("Íleo", "1", True), ("Retención urinaria", "1", True)],
   "bandas": [("0-2", "Poco probable", "Buscar otra causa", False),
              ("≥ 3", "Anticolinérgico", "Suspender atropina; benzodiacepina; sonda vesical", True)]},
  ["«Rojo como tomate, seco como hueso, loco como cabra».",
   "La crisis colinérgica tiene piel húmeda, miosis y broncorrea.",
   "Fisostigmina solo en casos graves y con monitoreo."],
  GOLDFRANK)

# SP-094 · embudo
V("embudo", "SP-094", "oncologia-acupuntura-medicina-complementaria", "Tipos de medicina no convencional",
  "SALUD PÚBLICA ENAM: MEDICINA COMPLEMENTARIA", "SALUD PÚBLICA",
  ("Medicina complementaria", ["Se usa junto con la medicina convencional, no la reemplaza",
   "Ej.: acupuntura para síntomas de la quimioterapia"]),
  ("Servicio de oncología de un hospital de Lima", ["Quimioterapia con efectos adversos", "Se asocia acupuntura"]),
  {"rotulo": "Embudo de conceptos",
   "inicio": "Acupuntura junto a la quimioterapia",
   "candidatos": ["Complementaria", "Alternativa", "Tradicional", "Ayurvédica", "Trofoterapia"],
   "pasos": [("Se suma al tratamiento, no lo reemplaza", ["Alternativa"]),
             ("No es la medicina ancestral local", ["Tradicional"]),
             ("No es sistema indio ni terapia con dieta", ["Ayurvédica", "Trofoterapia"])],
   "final": ("COMPLEMENTARIA", ["Acompaña a la convencional", "EsSalud: Medicina Complementaria"]),
   "nota": "Alternativa: se usa en lugar de la convencional."},
  ["Medicina tradicional: saberes de los pueblos (p. ej., andina, amazónica).",
   "Integrativa: combina ambas con evidencia.",
   "La acupuntura reduce náuseas y dolor en algunos pacientes."],
  "OMS – Estrategia sobre medicina tradicional 2014-2023 · EsSalud – Programa de Medicina Complementaria")

# CIR-072 · puntaje
V("puntaje", "CIR-072", "hiperresonancia-desviacion-traqueal-hipotension-aguja", "Neumotórax a tensión",
  "CIRUGÍA ENAM: NEUMOTÓRAX A TENSIÓN", "CIRUGÍA",
  ("Neumotórax a tensión", ["Diagnóstico clínico: no esperar la radiografía",
   "Descompresión inmediata con aguja y luego tubo de tórax"]),
  ("Varón de 35 años tras accidente de tránsito", ["PA 80/50, FC 132, SatO₂ 82%", "Hiperresonancia, MV abolido, tráquea desviada, enfisema"]),
  {"rotulo": "Signos en el caso", "escala": "Neumotórax a tensión", "total": 5, "max": 6,
   "total_label": "Signos presentes",
   "interpreta": "Neumotórax a tensión",
   "items": [("Hipotensión (80/50)", "1", True), ("Tráquea desviada al otro lado", "1", True),
             ("Hiperresonancia", "1", True), ("MV abolido", "1", True),
             ("Enfisema subcutáneo", "1", True), ("Ingurgitación yugular", "1", False)],
   "bandas": [("0-2", "Poco probable", "Rx de tórax", False),
              ("≥ 3", "A tensión", "DESCOMPRESIÓN CON AGUJA inmediata; luego tubo", True)]},
  ["Aguja en el 4.º-5.º espacio intercostal, línea axilar media (adultos).",
   "Intubar sin descomprimir empeora el neumotórax.",
   "Puede no haber IY si hay hipovolemia."],
  ATLS)

# REU-037 · puntaje
V("puntaje", "REU-037", "prurito-pliegues-asma-piel-seca-dermatitis-atopica", "Dermatitis atópica: criterios",
  "DERMATOLOGÍA ENAM: DERMATITIS ATÓPICA", "DERMATOLOGÍA",
  ("Dermatitis atópica", ["Eccema crónico y pruriginoso en pliegues",
   "Asociada a asma y rinitis; piel seca"]),
  ("Mujer de 19 años con 6 años de prurito", ["Pliegues de rodillas, codos, cuello, muñecas", "Asma · piel seca con fisuras · biopsia: espongiosis"]),
  {"rotulo": "Criterios del Reino Unido en el caso", "escala": "UK Working Party", "total": 5, "max": 6,
   "total_label": "Criterios presentes",
   "interpreta": "Dermatitis atópica",
   "items": [("Prurito (obligatorio)", "1", True), ("Pliegues afectados", "1", True),
             ("Asma o rinitis personal", "1", True), ("Piel seca generalizada", "1", True),
             ("Inicio antes de los 2 años", "1", False), ("Eccema flexural visible", "1", True)],
   "bandas": [("< 4", "No cumple", "Buscar otra dermatosis", False),
              ("≥ 4", "Atópica", "Emolientes + corticoide tópico", True)]},
  ["Prurito + ≥ 3 criterios menores.",
   "Brotes: corticoide tópico; mantenimiento: emolientes diarios.",
   "Tacrolimus tópico para cara y pliegues."],
  "UK Working Party – Diagnostic criteria for atopic dermatitis (1994) · AAD – Guidelines of care for atopic dermatitis (2023)")

# NEF-059 · puntaje
V("puntaje", "NEF-059", "mujer-joven-disuria-sin-fiebre-cistitis-no-complicada", "Cistitis: ¿complicada?",
  "NEFROLOGÍA ENAM: CISTITIS NO COMPLICADA", "NEFROLOGÍA",
  ("Cistitis no complicada", ["Mujer no gestante, sin fiebre, dolor lumbar ni anomalías",
   "Antibiótico oral empírico, sin urocultivo obligatorio"]),
  ("Mujer de 23 años", ["Disuria, polaquiuria, dolor perineal", "Sin fiebre ni vómitos · usa inyectable trimestral"]),
  {"rotulo": "Datos de complicación en el caso", "escala": "ITU complicada", "total": 0, "max": 5,
   "total_label": "Datos presentes",
   "interpreta": "Cistitis no complicada",
   "items": [("Fiebre o dolor lumbar", "1", False), ("Embarazo", "1", False),
             ("Varón", "1", False), ("Anomalía urinaria o sonda", "1", False),
             ("Inmunosupresión", "1", False)],
   "bandas": [("0", "No complicada", "Antibiótico oral empírico (nitrofurantoína)", True),
              ("≥ 1", "Complicada", "Urocultivo y tratamiento más largo", False)]},
  ["Nitrofurantoína 5 días o fosfomicina dosis única.",
   "Ciprofloxacino no es de primera línea para cistitis simple.",
   "Carbapenem y ceftriaxona EV son excesivos."],
  "IDSA/ESCMID – Uncomplicated cystitis and pyelonephritis in women (2011) · EAU – Urological infections (2024)")

# END-040 · radial
V("radial", "END-040", "galactorrea-amenorrea-hiperprolactinemia", "Galactorrea y amenorrea",
  "ENDOCRINOLOGÍA ENAM: HIPERPROLACTINEMIA", "ENDOCRINOLOGÍA",
  ("Hiperprolactinemia", ["La prolactina alta inhibe la GnRH",
   "Galactorrea + amenorrea (o infertilidad)"]),
  ("Mujer de 28 años", ["Secreción láctea a la presión del pezón", "Amenorrea de 3 meses"]),
  {"rotulo": "Mapa del tema", "centro": "PROLACTINA", "centro_sub": "Causas y efectos", "ans": 0,
   "items": [("PROLACTINA ALTA", ["Inhibe la GnRH", "Galactorrea + amenorrea"]),
             ("Embarazo", ["Descartar primero"]),
             ("Fármacos", ["Antipsicóticos, metoclopramida"]),
             ("Prolactinoma", ["RM de silla turca"]),
             ("Hipotiroidismo", ["La TRH estimula prolactina"])],
   "ruta": ["Galactorrea + amenorrea", "Descartar embarazo", "Medir prolactina", "HIPERPROLACTINEMIA"]},
  ["Prolactinoma: cabergolina es el tratamiento de elección.",
   "Macroprolactinoma: defecto del campo visual (hemianopsia bitemporal).",
   "Pedir TSH y β-hCG en toda amenorrea."],
  "Endocrine Society – Diagnosis and treatment of hyperprolactinemia (2011) · Pituitary Society – Prolactinoma consensus (2023)")

# CB-049 · tarjetas
V("tarjetas", "CB-049", "nino-dolor-muslo-espasmos-diaforesis-latrodectus", "Arácnidos venenosos del Perú",
  "CIENCIAS BÁSICAS ENAM: LATRODECTISMO", "CIENCIAS BÁSICAS",
  ("Latrodectismo (viuda negra)", ["Neurotoxina que libera acetilcolina y noradrenalina",
   "Dolor, espasmos musculares, diaforesis, HTA y taquicardia"]),
  ("Escolar de 8 años de zona rural", ["Dolor punzante en el muslo · luego espasmos dolorosos", "HTA, taquicardia, diaforesis · punto blanco con halo"]),
  {"rotulo": "¿Qué animal fue?", "ans": 0, "cards": [
      {"titulo": "LATRODECTUS MACTANS", "datos": [
          ("Veneno", "Neurotóxico", True), ("Local", "Punto blanco, halo rojo", True),
          ("Sistémico", "Espasmos, HTA, sudor", True)],
       "pie": "Analgesia, benzodiacepinas, antiveneno"},
      {"titulo": "Loxosceles laeta", "datos": [
          ("Veneno", "Necrotizante", False), ("Local", "Placa livedoide, necrosis", False),
          ("Sistémico", "Hemólisis, falla renal", False)],
       "pie": "Araña de los rincones"},
      {"titulo": "Tityus", "datos": [
          ("Veneno", "Neurotóxico (escorpión)", False), ("Local", "Dolor", False),
          ("Sistémico", "Edema pulmonar, choque", False)],
       "pie": "Grave en niños"},
      {"titulo": "Hadruroides (chamuco)", "datos": [
          ("Veneno", "Poco tóxico", False), ("Local", "Dolor, parestesia", False),
          ("Sistémico", "Raro", False)],
       "pie": "Escorpión de la costa"}]},
  ["Abdomen en tabla: puede simular abdomen agudo.",
   "Gluconato de calcio ya no se recomienda de rutina.",
   "Loxoscelismo: la forma cutánea es la más frecuente."],
  "MINSA – Norma técnica de accidentes por animales ponzoñosos · " + GOLDFRANK)

# GIN-132 · matriz
V("matriz", "GIN-132", "incompatibilidad-rh-anemia-fetal-cerebral-media", "Doppler obstétrico",
  "OBSTETRICIA ENAM: ANEMIA FETAL", "OBSTETRICIA",
  ("Anemia fetal", ["La sangre anémica es menos viscosa y fluye más rápido",
   "Pico sistólico de la arteria cerebral media > 1.5 MoM: anemia moderada-grave"]),
  ("Gestante de 30 semanas", ["Incompatibilidad Rh confirmada", "Doppler para estimar anemia fetal"]),
  {"rotulo": "¿Qué evalúa cada vaso?", "eje_x": "Aspecto", "eje_y": "Arteria",
   "cols": ["Evalúa", "Uso"], "rows": ["Cerebral media", "Umbilical", "Uterina", "Ductus venoso"], "caso": (0, 0),
   "cells": [[("ANEMIA FETAL", ["Pico sistólico"]), ("Isoinmunización", ["> 1.5 MoM: transfundir"])],
             [("Resistencia placentaria", []), ("RCIU", ["Flujo ausente o reverso"])],
             [("Circulación materna", []), ("Riesgo de preeclampsia", [])],
             [("Función cardiaca fetal", []), ("RCIU avanzado", [])]]},
  ["Anemia grave: transfusión intrauterina por cordocentesis.",
   "Prevención: inmunoglobulina anti-D a las 28 semanas y posparto.",
   "Reemplaza a la amniocentesis seriada."],
  "SMFM – Clinical Guideline N.° 8: Fetal anemia (2015) · " + WILLIAMS)

# NEF-060 · fases
V("fases", "NEF-060", "neumonia-hipotension-fena-04-vasoconstriccion-eferente", "Compensación renal en la hipoperfusión",
  "NEFROLOGÍA ENAM: LESIÓN RENAL PRERRENAL", "NEFROLOGÍA",
  ("Reacción renal a la hipoperfusión", ["La angiotensina II contrae la arteriola eferente",
   "Así se mantiene la presión glomerular y la filtración"]),
  ("Varón de 64 años con neumonía y choque", ["PA 80/50 · oliguria", "Na urinario 8, FeNa 0.4%, osmolalidad 700"]),
  {"rotulo": "Secuencia compensatoria", "ans": 2,
   "fases": [("Hipotensión", "Minutos", "↓ Flujo renal", ["Sepsis"]),
             ("SRAA", "Minutos", "Renina", ["Angiotensina II"]),
             ("Glomérulo", "Minutos", "CONTRAE LA EFERENTE", ["Sostiene la TFG"]),
             ("Túbulo", "Horas", "Retiene Na y agua", ["Na urinario bajo"])],
   "curvas": [],
   "chips_titulo": "Mecanismo · marcado el correcto",
   "chips": [("Contrae la eferente", True), ("Aumenta la TFG", False), ("Excreta más sodio", False), ("Dilata la aferente", False)]},
  ["Por eso los IECA/ARA II bajan la TFG en la hipoperfusión.",
   "Los AINE bloquean las prostaglandinas y empeoran la lesión.",
   "FeNa < 1% y orina concentrada: prerrenal."],
  GUYTON + " · KDIGO – Acute kidney injury (2012)")

# REU-038 · embudo
V("embudo", "REU-038", "fibromialgia-insomnio-persistente-amitriptilina", "Fibromialgia: fármaco a agregar",
  "REUMATOLOGÍA ENAM: FIBROMIALGIA", "REUMATOLOGÍA",
  ("Fibromialgia", ["Dolor difuso crónico, fatiga e insomnio sin inflamación",
   "Si falla la terapia física y conductual: amitriptilina en dosis baja"]),
  ("Mujer de 45 años con fibromialgia", ["Terapia física y conductual", "Persisten dolor muscular e insomnio"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Dolor e insomnio que persisten",
   "candidatos": ["Amitriptilina", "Codeína", "Ibuprofeno", "Dexametasona", "Tramadol crónico"],
   "pasos": [("Opioides: sin beneficio y con dependencia", ["Codeína", "Tramadol crónico"]),
             ("No es una enfermedad inflamatoria", ["Ibuprofeno", "Dexametasona"])],
   "final": ("AMITRIPTILINA", ["Dosis baja en la noche", "Mejora el sueño y el dolor"]),
   "nota": "Alternativas: duloxetina o pregabalina."},
  ["El ejercicio aeróbico es la medida más eficaz.",
   "Pruebas de laboratorio normales.",
   "Criterios ACR 2016: índice de dolor + gravedad de síntomas."],
  "EULAR – Revised recommendations for the management of fibromyalgia (2017) · ACR – Fibromyalgia criteria (2016)")

# NEU-036 · puntaje
V("puntaje", "NEU-036", "ronca-apneas-imc-35-acv-polisomnografia", "Apnea obstructiva del sueño",
  "NEUMOLOGÍA ENAM: APNEA OBSTRUCTIVA DEL SUEÑO", "NEUMOLOGÍA",
  ("Apnea obstructiva del sueño", ["Ronquido, pausas respiratorias, obesidad; riesgo de HTA y ACV",
   "Diagnóstico: polisomnografía nocturna"]),
  ("Varón de 47 años con ACV isquémico reciente", ["Ronca y deja de respirar de noche desde hace 7 años", "IMC 35"]),
  {"rotulo": "STOP-BANG en el caso", "escala": "STOP-BANG", "total": 4, "max": 8,
   "total_label": "Puntaje del caso",
   "interpreta": "Riesgo intermedio: confirmar con polisomnografía",
   "items": [("Ronquido", "1", True), ("Cansancio diurno", "1", False), ("Apneas observadas", "1", True),
             ("Hipertensión", "1", False), ("IMC ≥ 35", "1", True), ("Edad > 50 años", "1", False),
             ("Cuello > 40 cm", "1", False), ("Sexo masculino", "1", True)],
   "bandas": [("0-2", "Bajo", "Poco probable", False),
              ("3-4", "Intermedio", "POLISOMNOGRAFÍA", True),
              ("5-8", "Alto", "Polisomnografía", False)]},
  ["Índice apnea-hipopnea ≥ 5 con síntomas o ≥ 15 confirma AOS.",
   "La oximetría nocturna sola no basta para el diagnóstico.",
   "Tratamiento: CPAP y bajar de peso."],
  "AASM – Clinical practice guideline for diagnostic testing for adult OSA (2017) · AHA – OSA and cardiovascular disease (2021)")

# CIR-073 · embudo
V("embudo", "CIR-073", "diabetico-perine-escroto-necrosis-crepitacion-fournier", "Infección necrotizante del periné",
  "CIRUGÍA ENAM: GANGRENA DE FOURNIER", "CIRUGÍA",
  ("Gangrena de Fournier", ["Fascitis necrotizante del periné y genitales",
   "Diabetes y alcoholismo; necrosis, crepitación y sepsis"]),
  ("Varón de 75 años diabético y alcohólico", ["4 días de celulitis perineal y dolor escrotal", "T 39 °C · necrosis y crepitación en periné y escroto"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Infección perineal en diabético",
   "candidatos": ["Fascitis necrotizante", "Celulitis", "Hidradenitis", "Absceso isquiorrectal", "Fístula anal"],
   "pasos": [("Necrosis y crepitación", ["Celulitis", "Hidradenitis"]),
             ("Se extiende al escroto con sepsis", ["Absceso isquiorrectal", "Fístula anal"])],
   "final": ("FASCITIS NECROTIZANTE", ["Gangrena de Fournier", "Desbridamiento urgente + antibióticos"]),
   "nota": "Es una emergencia: cada hora de retraso aumenta la mortalidad."},
  ["Antibióticos de amplio espectro: cubrir anaerobios y gramnegativos.",
   "Suele requerir varios desbridamientos.",
   "El dolor es desproporcionado a lo que se ve."],
  "WSES/SIS-E – Consensus on skin and soft-tissue infections (2022) · EAU – Urological infections (2024)")

# GIN-133 · árbol
A("GIN-133", "puerpera-vih-tar-desea-lactar-contraindicar", "Lactancia en madre con VIH",
  "OBSTETRICIA ENAM: VIH Y LACTANCIA", "OBSTETRICIA",
  ("VIH y lactancia materna", ["La leche transmite el VIH aunque la madre reciba TAR",
   "En el Perú se contraindica y se entrega sucedáneo"]),
  ("Puérpera inmediata con VIH", ["Diagnóstico 2 meses antes del parto, en TAR", "Desea dar de lactar"]),
  Q("¿Hay acceso seguro a fórmula?", [
      L("Sí (norma peruana)", "CONTRAINDICAR LA LACTANCIA", ["Sucedáneo gratuito", "Continuar el TAR"], path=True),
      L("No (OMS, escasos recursos)", "Lactancia exclusiva + TAR", ["Carga viral suprimida"])], path=True),
  ("Cuidados del binomio", [("Hacer", True), ("No hacer", False)], [
      ("Madre", ["Continuar TAR", "Suspender antirretrovirales"]),
      ("Recién nacido", ["Profilaxis ARV y sucedáneo", "Separarlo de la madre"])]),
  ["Inhibir la lactancia (cabergolina).",
   "El RN se estudia con PCR de ADN/ARN viral.",
   "No se aísla al niño de la madre."],
  "MINSA – NTS N.° 159-MINSA/2019/DGIESP (Transmisión materno-infantil) · OMS – Infant feeding in areas of HIV (2016)")

# GIN-134 · árbol
A("GIN-134", "podalica-primigesta-talla-150-trabajo-parto-cesarea", "Presentación podálica en trabajo de parto",
  "OBSTETRICIA ENAM: PRESENTACIÓN PODÁLICA", "OBSTETRICIA",
  ("Presentación podálica", ["En trabajo de parto sin condiciones favorables: cesárea",
   "La versión externa se hace antes de la labor, desde las 37 semanas"]),
  ("Gestante de 20 años, talla 1.50 m", ["36 semanas, podálico confirmado", "AU 36 cm · inicio de trabajo de parto"]),
  Q("¿Ya está en trabajo de parto?", [
      L("No, ≥ 37 sem", "Versión cefálica externa", ["Si no hay contraindicación"]),
      Q("¿Condiciones para parto vaginal?", [
          L("No: talla baja, feto grande", "CESÁREA", ["Urgente"], path=True),
          L("Sí y hay experto", "Parto vaginal asistido", ["Casos seleccionados"])],
        edge="Sí", path=True)], path=True),
  ("Contra el parto podálico vaginal", [("Factor", True)], [
      ("Madre", ["Talla baja, pelvis estrecha"]),
      ("Feto", ["Grande (AU 36 cm), pies"]),
      ("Equipo", ["Sin experiencia"])]),
  ["La amniotomía en podálico arriesga prolapso de cordón.",
   "El prematuro podálico tiene más riesgo de retención de la cabeza.",
   "Cesárea programada a las 39 semanas si persiste podálico."],
  "RCOG – Green-top Guideline N.° 20b: Management of breech presentation (2017) · " + WILLIAMS)

# SP-095 · tarjetas
V("tarjetas", "SP-095", "neumonia-meses-frios-variacion-estacional", "Tendencias en el tiempo",
  "SALUD PÚBLICA ENAM: VARIACIÓN ESTACIONAL", "SALUD PÚBLICA",
  ("Variación estacional", ["Aumento que se repite cada año en la misma época",
   "Neumonías en los meses fríos (friaje, heladas)"]),
  ("Niños < 3 años del distrito Brillante", ["Neumonías en 5 años", "Más casos en los meses de menor temperatura"]),
  {"rotulo": "¿Qué patrón es?", "ans": 0, "cards": [
      {"titulo": "ESTACIONAL", "datos": [
          ("Periodo", "Cada año", True), ("Patrón", "Misma época del año", True),
          ("Ejemplo", "Neumonía en invierno", True)],
       "pie": "Ligado al clima"},
      {"titulo": "Cíclico", "datos": [
          ("Periodo", "Cada varios años", False), ("Patrón", "Ondas regulares", False),
          ("Ejemplo", "Sarampión, dengue", False)],
       "pie": "Por susceptibles acumulados"},
      {"titulo": "Secular", "datos": [
          ("Periodo", "Décadas", False), ("Patrón", "Sube o baja", False),
          ("Ejemplo", "Obesidad en aumento", False)],
       "pie": "Tendencia a largo plazo"},
      {"titulo": "Irregular", "datos": [
          ("Periodo", "Impredecible", False), ("Patrón", "Brotes", False),
          ("Ejemplo", "Epidemia puntual", False)],
       "pie": "Aleatorio"}]},
  ["Se analiza con series de tiempo y corredores endémicos.",
   "Plan multisectorial ante heladas y friaje.",
   "Vacunar contra neumococo e influenza antes del invierno."],
  "OPS – MOPECE · MINSA – Plan multisectorial ante heladas y friaje")

# TRA-025 · radial
V("radial", "TRA-025", "anciano-fractura-cadera-postrado-tvp", "Complicaciones de la fractura de cadera",
  "TRAUMATOLOGÍA ENAM: FRACTURA DE CADERA", "TRAUMATOLOGÍA",
  ("Fractura de cadera en el anciano", ["La inmovilización favorece la trombosis venosa profunda",
   "Profilaxis con HBPM y cirugía temprana (< 48 h)"]),
  ("Pregunta de concepto", ["Anciano postrado", "con fractura de cadera"]),
  {"rotulo": "Mapa del tema", "centro": "FRACTURA DE CADERA", "centro_sub": "Anciano postrado", "ans": 0,
   "items": [("TVP / TEP", ["La complicación más probable", "Profilaxis con HBPM"]),
             ("Úlceras por presión", ["Cambios de posición"]),
             ("Neumonía", ["Por inmovilidad"]),
             ("Delirium", ["Frecuente"]),
             ("Infección urinaria", ["Por sonda"])],
   "ruta": ["Fractura de cadera", "Inmovilización", "Estasis venosa (Virchow)", "TVP"]},
  ["Operar en las primeras 48 horas reduce complicaciones y mortalidad.",
   "Movilizar lo antes posible después de la cirugía.",
   "La TEP es causa importante de muerte."],
  "AAOS – Management of hip fractures in older adults (2021) · ACCP – Prevention of VTE in orthopedic surgery (2012)")

# GIN-135 · termómetro
V("termometro", "GIN-135", "borde-placentario-1-cm-oci-implantacion-baja", "Placenta y orificio cervical",
  "OBSTETRICIA ENAM: PLACENTA DE IMPLANTACIÓN BAJA", "OBSTETRICIA",
  ("Placenta de implantación baja", ["El borde queda a menos de 2 cm del orificio cervical interno, sin cubrirlo",
   "Placenta previa: cubre el OCI"]),
  ("Primigesta de 34 semanas", ["Sangrado vaginal indoloro escaso", "Borde placentario a 1 cm del OCI"]),
  {"rotulo": "Distancia al OCI",
   "niveles": [("> 2 cm", "Normal", ["Normoinserta"]),
               ("< 2 cm", "Implantación baja", ["No cubre el OCI"]),
               ("Cubre el OCI", "Placenta previa", ["Total o parcial"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "EVITAR EL TACTO VAGINAL", ["Especuloscopía y ecografía"], True),
             (2, "Ecografía TV de control", ["La placenta puede «migrar»"], False),
             (3, "Vía del parto", ["Según distancia y sangrado"], False)]},
  ["La clasificación actual solo usa «previa» o «de inserción baja».",
   "Corticoides si el sangrado exige parto antes de las 34 semanas.",
   "Con cesárea previa: descartar acretismo."],
  "RCOG – Green-top Guideline N.° 27a: Placenta praevia and accreta (2018) · " + WILLIAMS)

# NEF-061 · termómetro
V("termometro", "NEF-061", "psa-59-libre-total-11-biopsia", "PSA en zona gris",
  "NEFROLOGÍA ENAM: PSA LIBRE / TOTAL", "NEFROLOGÍA",
  ("PSA en zona gris (4-10 ng/mL)", ["El cociente libre/total ayuda: si es bajo, más riesgo de cáncer",
   "Próstata dura + cociente bajo: biopsia ecodirigida"]),
  ("Varón de 49 años con síntomas urinarios", ["Próstata aumentada de consistencia", "PSA 5.9 · libre/total 11%"]),
  {"rotulo": "Cociente PSA libre/total",
   "niveles": [("> 25%", "Riesgo bajo", ["Probable HBP"]),
               ("10-25%", "Intermedio", ["Evaluar biopsia"]),
               ("< 10%", "Riesgo alto", ["Cáncer probable"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "BIOPSIA ECODIRIGIDA", ["Tacto anormal + cociente 11%"], True),
             (2, "Si es cáncer: estadificar", ["RM, gammagrafía"], False),
             (3, "Si es negativa: vigilar", ["PSA y RM"], False)]},
  ["El finasteride baja el PSA a la mitad: no iniciarlo antes de estudiar.",
   "Los análogos de LHRH son para cáncer avanzado confirmado.",
   "La ecografía sola no diagnostica cáncer."],
  "EAU – Guidelines on prostate cancer (2024) · AUA/SUO – Early detection of prostate cancer (2023)")

# GAS-048 · radial
V("radial", "GAS-048", "lacteos-distension-diarrea-lactasa", "Disacaridasas intestinales",
  "GASTROENTEROLOGÍA ENAM: INTOLERANCIA A LA LACTOSA", "GASTROENTEROLOGÍA",
  ("Intolerancia a la lactosa", ["Déficit de lactasa del borde en cepillo",
   "La lactosa no absorbida fermenta: gases, distensión y diarrea osmótica"]),
  ("Niño de 6 años", ["Náuseas, distensión, diarrea y flatulencia", "Después de tomar lácteos"]),
  {"rotulo": "Mapa del tema", "centro": "BORDE EN CEPILLO", "centro_sub": "Disacaridasas", "ans": 0,
   "items": [("LACTASA", ["Lactosa → glucosa + galactosa", "Déficit: intolerancia"]),
             ("Sacarasa", ["Sacarosa"]),
             ("Maltasa", ["Maltosa"]),
             ("Amilasa", ["Almidón (páncreas y saliva)"]),
             ("Trehalasa", ["Trehalosa (hongos)"])],
   "ruta": ["Toma lácteos", "Lactosa sin digerir", "Fermenta en el colon", "DÉFICIT DE LACTASA"]},
  ["Prueba de hidrógeno espirado: confirma el diagnóstico.",
   "Heces ácidas con sustancias reductoras.",
   "Reducir lactosa o usar lactasa oral; no eliminar el calcio."],
  "NASPGHAN – Lactose intolerance in infants, children and adolescents (Pediatrics 2006) · " + GUYTON)

# INF-067 · fases
V("fases", "INF-067", "satipo-fiebre-amarilla-ictericia-gravedad", "Fiebre amarilla: fases",
  "INFECTOLOGÍA ENAM: FIEBRE AMARILLA GRAVE", "INFECTOLOGÍA",
  ("Fiebre amarilla", ["Fase de infección → remisión → intoxicación",
   "La ictericia marca la fase tóxica: hepatitis, hemorragia y falla renal"]),
  ("Enfermero serumista en Satipo", ["Vacunado solo 6 días antes del viaje", "Fiebre, mialgias · ictericia · ELISA (+)"]),
  {"rotulo": "Curso de la enfermedad", "ans": 2,
   "fases": [("Infección", "Días 3-6", "Fiebre, mialgias", ["Viremia"]),
             ("Remisión", "Horas-2 días", "Mejoría", ["La mayoría se cura"]),
             ("Tóxica", "15-25%", "ICTERICIA", ["Hemorragia, falla renal"])],
   "curvas": [("Fiebre", ROSE, [0.3, 0.9, 0.8, 0.3, 0.2, 0.7, 0.8]),
              ("Bilirr.", AMBER, [0.0, 0.1, 0.1, 0.1, 0.2, 0.7, 0.95])],
   "chips_titulo": "Signo de gravedad · marcado el correcto",
   "chips": [("Ictericia", True), ("Náuseas", False), ("Cefalea", False), ("Fiebre", False)]},
  ["La vacuna protege desde los 10 días: 6 días no bastaban.",
   "Signo de Faget: fiebre alta con bradicardia relativa.",
   "Mortalidad de la fase tóxica: 20-50%."],
  "MINSA – NTS de vigilancia de fiebre amarilla · OMS – Fiebre amarilla: nota descriptiva (2023)")

# PED-136 · árbol
A("PED-136", "varicela-placa-fluctuante-sobreinfeccion-oxacilina", "Varicela con sobreinfección",
  "PEDIATRÍA ENAM: VARICELA COMPLICADA", "PEDIATRÍA",
  ("Sobreinfección bacteriana de la varicela", ["Complicación más frecuente: S. aureus y estreptococo del grupo A",
   "Fiebre nueva, lesión roja, caliente y fluctuante: oxacilina ± drenaje"]),
  ("Preescolar de 3 años con varicela de 5 días", ["Placa eritematosa fluctuante y dolorosa en el tórax", "T 39 °C · leucocitos 18 300 · PCR 24"]),
  Q("¿Signos de infección bacteriana?", [
      L("No", "Tratamiento sintomático", ["Paracetamol, cortar uñas"]),
      Q("¿Absceso fluctuante?", [
          L("Sí", "OXACILINA + DRENAJE", ["Cubre S. aureus y estreptococo"], path=True),
          L("Fascitis, toxicidad", "Cirugía + clindamicina", ["Urgencia"])],
        edge="Sí: fiebre, placa roja", path=True)], path=True),
  ("Complicaciones de la varicela", [("Germen o causa", True)], [
      ("Piel", ["S. aureus, S. pyogenes"]),
      ("Neumonía", ["Viral (adultos)"]),
      ("SNC", ["Ataxia cerebelosa"])]),
  ["Nunca aspirina: síndrome de Reye.",
   "Aciclovir en inmunosuprimidos, adolescentes y adultos.",
   "Si hay SAMR comunitario: clindamicina o vancomicina."],
  "AAP – Red Book: Varicella-zoster infections (2024) · IDSA – Skin and soft tissue infections (2014)")

# SP-096 · matriz
V("matriz", "SP-096", "balanzas-descalibradas-sobreestiman-peso-error-sistematico", "Tipos de error en la medición",
  "SALUD PÚBLICA ENAM: ERROR SISTEMÁTICO", "SALUD PÚBLICA",
  ("Error sistemático (sesgo)", ["Desvía todas las mediciones en la misma dirección",
   "Balanzas descalibradas: sesgo de medición"]),
  ("Estudio de desnutrición en niños de 2 a 5 años", ["Balanzas con fallas de calibración", "Sobreestiman el peso"]),
  {"rotulo": "Sistemático vs aleatorio", "eje_x": "Aspecto", "eje_y": "Error",
   "cols": ["Afecta a", "Se corrige con"], "rows": ["Sistemático", "Aleatorio"], "caso": (0, 0),
   "cells": [[("VALIDEZ", ["Siempre en un sentido"]), ("Calibrar, buen diseño", ["No se corrige aumentando n"])],
             [("Precisión", ["Al azar, en ambos sentidos"]), ("Mayor tamaño de muestra", [])]]},
  ["Sesgos: de selección, de medición (información) y de confusión.",
   "Un estudio puede ser preciso pero sesgado.",
   "Estandarizar y calibrar los instrumentos antes de medir."],
  "Gordis – Epidemiology 6.ª ed. (2019) · Rothman – Modern Epidemiology 4.ª ed. (2021)")
