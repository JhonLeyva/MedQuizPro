"""Bloque 6 · parte G."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"

# NRL-032 · termómetro
V("termometro", "NRL-032", "hemorragia-intraparenquimal-pa-180-antihipertensivo", "Hemorragia intracerebral: control de la PA",
  "NEUROLOGÍA ENAM: HEMORRAGIA INTRAPARENQUIMAL", "NEUROLOGÍA",
  ("Hemorragia intracerebral hipertensiva", ["La PA alta hace crecer el hematoma",
   "Bajar la PAS a ~140 mmHg en las primeras horas"]),
  ("Varón de 65 años hipertenso mal controlado", ["Glasgow 10, hemiparesia derecha · PA 180/90", "TC: hemorragia intraparenquimal izquierda"]),
  {"rotulo": "Presión sistólica",
   "niveles": [("< 150", "Aceptable", ["Vigilar"]),
               ("150-220", "Bajar a ~ 140", ["Descenso rápido y seguro"]),
               ("> 220", "Muy alta", ["Descenso continuo y monitoreado"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta inicial", "paso_label": "PASO",
   "pasos": [(1, "ABC y cabecera a 30°", ["Glasgow 10: protege su vía aérea"], False),
             (2, "ANTIHIPERTENSIVO EV", ["Labetalol o nicardipino"], True),
             (3, "Revertir anticoagulantes", ["Neurocirugía si es cerebelosa o hay hidrocefalia"], False)]},
  ["Evitar bajar la PAS de 130 mmHg.",
   "Intubar si Glasgow ≤ 8 o no protege la vía aérea.",
   "El drenaje de LCR es para hidrocefalia, no de rutina."],
  "AHA/ASA – Guideline for the management of spontaneous intracerebral hemorrhage (2022)")

# CAR-045 · tarjetas
V("tarjetas", "CAR-045", "insuficiencia-cardiaca-enalapril-sobrevida", "IC: ¿qué fármaco prolonga la vida?",
  "CARDIOLOGÍA ENAM: INSUFICIENCIA CARDIACA", "CARDIOLOGÍA",
  ("Insuficiencia cardiaca con FE reducida", ["Mejoran la sobrevida: IECA/ARNI, betabloqueante, antialdosterónico e iSGLT2",
   "Diuréticos y digoxina solo alivian síntomas"]),
  ("Varón de 64 años con cardiopatía isquémica", ["Disnea, ortopnea, edema · FA", "Toma enalapril, digoxina, furosemida y rivaroxabán"]),
  {"rotulo": "¿Qué aporta cada fármaco?", "ans": 0, "cards": [
      {"titulo": "ENALAPRIL", "datos": [
          ("Efecto", "Bloquea el eje RAA", True), ("¿Sobrevida?", "Sí, la mejora", True),
          ("Para qué", "Remodelado cardiaco", True)],
       "pie": "Pilar del tratamiento"},
      {"titulo": "Digoxina", "datos": [
          ("Efecto", "Inotrópico, frena el NAV", False), ("¿Sobrevida?", "No", False),
          ("Para qué", "Menos hospitalizaciones", False)],
       "pie": "Controla la FC en la FA"},
      {"titulo": "Furosemida", "datos": [
          ("Efecto", "Diurético de asa", False), ("¿Sobrevida?", "No", False),
          ("Para qué", "Alivia la congestión", False)],
       "pie": "Síntomas"},
      {"titulo": "Rivaroxabán", "datos": [
          ("Efecto", "Anticoagulante", False), ("¿Sobrevida?", "No en la IC", False),
          ("Para qué", "Evita embolias en la FA", False)],
       "pie": "Previene el ACV"}]},
  ["Los «4 pilares»: IECA/ARNI, betabloqueante, espironolactona, iSGLT2.",
   "Agregar un betabloqueante también ayuda a controlar la FC de la FA.",
   "Suspender IECA si se inicia sacubitrilo-valsartán (36 h antes)."],
  "ESC – Guidelines for the diagnosis and treatment of heart failure (2021, act. 2023) · AHA/ACC/HFSA – Heart failure guideline (2022)")

# OFT-027 · fases
V("fases", "OFT-027", "tapon-cerumen-irrigacion-salino-tibio", "Tapón de cerumen",
  "OTORRINOLARINGOLOGÍA ENAM: TAPÓN DE CERUMEN", "OTORRINOLARINGOLOGÍA",
  ("Tapón de cerumen", ["Hipoacusia, plenitud, prurito o acúfeno",
   "Irrigación con agua o suero a temperatura corporal (37 °C)"]),
  ("Adolescente de 16 años", ["Hipoacusia, prurito y zumbido", "Conducto ocluido por cerumen"]),
  {"rotulo": "Extracción del tapón", "ans": 1,
   "fases": [("Ablandar", "2-5 días", "Ceruminolíticos", ["Si el tapón es duro"]),
             ("Irrigar", "Consulta", "SALINO TIBIO", ["A 37 °C: sin vértigo"]),
             ("Control", "Al terminar", "Otoscopia", ["Tímpano íntegro"])],
   "curvas": [],
   "chips_titulo": "Solución · marcada la correcta",
   "chips": [("Salina tibia", True), ("Agua helada", False), ("Agua oxigenada", False), ("Glicerina", False)]},
  ["El agua fría o caliente estimula el laberinto: vértigo y náuseas.",
   "No irrigar si hay perforación timpánica o cirugía previa del oído.",
   "Los hisopos empujan el cerumen y forman el tapón."],
  "AAO-HNS – Clinical practice guideline: Earwax (cerumen impaction) update (2017)")

# PED-118 · matriz
V("matriz", "PED-118", "rn-tumoracion-parietal-no-cruza-sutura-cefalohematoma", "Tumefacciones del cuero cabelludo del RN",
  "PEDIATRÍA ENAM: CEFALOHEMATOMA", "PEDIATRÍA",
  ("Cefalohematoma", ["Sangrado subperióstico: no cruza las suturas",
   "Aparece horas después del parto y desaparece en semanas"]),
  ("RN de 2 días, parto eutócico", ["Tumoración fluctuante de 4 × 4 cm", "Limitada al parietal derecho, no cruza suturas"]),
  {"rotulo": "Según la capa afectada", "eje_x": "Aspecto", "eje_y": "Lesión",
   "cols": ["¿Cruza suturas?", "Riesgo"], "rows": ["Caput succedaneum", "Cefalohematoma", "Hemorragia subgaleal"], "caso": (1, 0),
   "cells": [[("Sí", ["Edema, presente al nacer"]), ("Benigno", ["Se va en días"])],
             [("NO", ["Subperióstico"]), ("Ictericia", ["Calcificación rara"])],
             [("Sí", ["Todo el cráneo"]), ("Choque", ["Urgencia"])]]},
  ["No se punciona: riesgo de infección.",
   "Puede aumentar la bilirrubina al reabsorberse.",
   "Hemorragia subgaleal: asociada a vacuum; vigilar hematocrito."],
  NELSON + " · MINSA – Guía técnica de atención del recién nacido")

# REU-032 · puntaje
V("puntaje", "REU-032", "hepatitis-b-livedo-dolor-testicular-poliarteritis-nudosa", "Poliarteritis nudosa: criterios",
  "REUMATOLOGÍA ENAM: POLIARTERITIS NUDOSA", "REUMATOLOGÍA",
  ("Poliarteritis nudosa", ["Vasculitis necrotizante de arterias de mediano calibre",
   "Asociada a hepatitis B; respeta el pulmón y no tiene ANCA"]),
  ("Varón de 59 años con hepatitis B", ["Fiebre, baja de peso, dolor testicular, livedo", "Polineuropatía · biopsia: vasculitis necrotizante"]),
  {"rotulo": "Criterios ACR 1990 en el caso", "escala": "ACR 1990 (PAN)", "total": 7, "max": 10,
   "total_label": "Criterios presentes",
   "interpreta": "Cumple poliarteritis nudosa (≥ 3)",
   "items": [("Pérdida de peso ≥ 4 kg", "1", True), ("Livedo reticularis", "1", True),
             ("Dolor testicular", "1", True), ("Mialgias o debilidad", "1", True),
             ("Mono o polineuropatía", "1", True), ("PA diastólica > 90", "1", False),
             ("Urea o creatinina altas", "1", False), ("Virus de hepatitis B", "1", True),
             ("Arteriografía con aneurismas", "1", False), ("Biopsia con vasculitis", "1", True)],
   "bandas": [("< 3", "No cumple", "Buscar otra vasculitis", False),
              ("≥ 3", "PAN", "Antiviral + corticoide ± recambio plasmático", True)]},
  ["Aneurismas renales y mesentéricos en la angiografía.",
   "Sin glomerulonefritis: la HTA es por isquemia renal.",
   "En PAN por VHB no se usa inmunosupresión prolongada."],
  "ACR – Criteria for the classification of polyarteritis nodosa (1990) · ACR/VF – Guideline for PAN (2021)")

# SP-079 · tarjetas
V("tarjetas", "SP-079", "cancer-metastasico-oxigeno-analgesia-ortotanasia", "Decisiones al final de la vida",
  "SALUD PÚBLICA ENAM: ORTOTANASIA", "SALUD PÚBLICA",
  ("Ortotanasia", ["Permitir la muerte a su tiempo, con alivio de síntomas",
   "Sin acelerarla ni prolongarla de forma fútil"]),
  ("Mujer de 80 años con cáncer de mama metastásico", ["Atendida en su domicilio", "Recibe oxígeno y analgésicos"]),
  {"rotulo": "¿Cómo se llama la práctica?", "ans": 0, "cards": [
      {"titulo": "ORTOTANASIA", "datos": [
          ("Qué es", "Muerte a su tiempo, sin dolor", True), ("Ejemplo", "O₂ y analgesia en casa", True),
          ("¿Aceptable?", "Sí: buena práctica", True)],
       "pie": "Cuidados paliativos"},
      {"titulo": "Eutanasia", "datos": [
          ("Qué es", "Provocar la muerte", False), ("Ejemplo", "Fármaco letal a pedido", False),
          ("¿Aceptable?", "Delito en el Perú", False)],
       "pie": "Acorta la vida"},
      {"titulo": "Distanasia", "datos": [
          ("Qué es", "Prolongar la agonía", False), ("Ejemplo", "Soporte fútil", False),
          ("¿Aceptable?", "No", False)],
       "pie": "Encarnizamiento terapéutico"},
      {"titulo": "Adistanasia", "datos": [
          ("Qué es", "No iniciar lo fútil", False), ("Ejemplo", "Retirar medidas extraordinarias", False),
          ("¿Aceptable?", "Sí", False)],
       "pie": "Limitación del esfuerzo"}]},
  ["Los cuidados paliativos no aceleran ni retrasan la muerte.",
   "Ley N.° 30846: cuidados paliativos en pacientes oncológicos.",
   "La sedación paliativa busca aliviar, no causar la muerte."],
  "OMS – Cuidados paliativos (2020) · Ley N.° 30846 (2018) · Beauchamp y Childress 8.ª ed. (2019)")

# NRL-033 · embudo
V("embudo", "NRL-033", "fumador-convulsion-dos-lesiones-anillo-metastasis", "Lesiones cerebrales múltiples con anillo",
  "NEUROLOGÍA ENAM: METÁSTASIS CEREBRALES", "NEUROLOGÍA",
  ("Metástasis cerebrales", ["El tumor intracraneal más frecuente del adulto",
   "Lesiones múltiples, redondas, en la unión córtico-subcortical, con mucho edema"]),
  ("Varón de 65 años, fumador severo", ["Convulsiones · tos y cefalea de 4 meses", "TC: dos lesiones con anillo y edema digitiforme"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Fumador con convulsiones y dos lesiones",
   "candidatos": ["Metástasis", "Glioblastoma", "Meningioma", "Neurocisticercosis", "Absceso cerebral"],
   "pasos": [("Lesiones múltiples en ambos hemisferios", ["Glioblastoma", "Meningioma"]),
             ("Sin fiebre ni foco séptico", ["Absceso cerebral"]),
             ("Fumador con tos: primario pulmonar probable", ["Neurocisticercosis"])],
   "final": ("METÁSTASIS CEREBRAL", ["Primario más frecuente: pulmón", "Buscar el tumor con TEM de tórax"]),
   "nota": "Dexametasona para el edema y antiepiléptico por las convulsiones."},
  ["Otros primarios: mama, melanoma, riñón y colon.",
   "La RM con gadolinio detecta más lesiones que la TC.",
   "Glioblastoma: lesión única que cruza el cuerpo calloso."],
  "ASCO/SNO/ASTRO – Treatment for brain metastases (2022) · " + HARRISON)

# PED-119 · matriz
V("matriz", "PED-119", "corioamnionitis-hipotermia-indice-it-sepsis", "Laboratorio en sepsis neonatal",
  "PEDIATRÍA ENAM: SEPSIS NEONATAL TEMPRANA", "PEDIATRÍA",
  ("Sepsis neonatal temprana", ["Primeras 72 h; factor de riesgo: corioamnionitis",
   "El índice I/T > 0.2 es el marcador hematológico más útil"]),
  ("RN a término de 16 horas", ["Madre con corioamnionitis no tratada", "Hipotermia e intolerancia oral"]),
  {"rotulo": "¿Qué apoya la sospecha?", "eje_x": "Aspecto", "eje_y": "Examen",
   "cols": ["Valor anormal", "Utilidad"], "rows": ["Índice I/T", "Leucocitos", "Plaquetas", "PCR"], "caso": (0, 1),
   "cells": [[("> 0.2", ["Inmaduros / totales"]), ("LA MÁS ÚTIL", ["Alta sensibilidad"])],
             [("< 5000 o > 30 000", ["18 000 es normal"]), ("Poco específico", [])],
             [("< 100 000", ["Signo tardío"]), ("Inespecífico", [])],
             [("> 10 mg/L", ["Sube a las 24 h"]), ("Seriada: buen VPN", [])]]},
  ["El hemocultivo es el estándar para confirmar.",
   "La VSG no sirve en el recién nacido.",
   "Tratamiento empírico: ampicilina + gentamicina."],
  NELSON + " · AAP – Management of neonates ≥ 35 weeks with suspected early-onset sepsis (2018)")

# PED-120 · embudo
V("embudo", "PED-120", "varicela-aspirina-convulsion-hepatomegalia-reye", "Convulsiones tras varicela",
  "PEDIATRÍA ENAM: SÍNDROME DE REYE", "PEDIATRÍA",
  ("Síndrome de Reye", ["Encefalopatía aguda + hígado graso tras varicela o influenza",
   "Asociado al uso de aspirina en niños"]),
  ("Niño de 3 años con varicela hace 5 días", ["Recibe aciclovir y aspirina para la fiebre", "Convulsiones · hepatomegalia · LCR normal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Niño con varicela que convulsiona",
   "candidatos": ["Síndrome de Reye", "Encefalitis viral", "Meningitis", "Epilepsia", "Ataxia cerebelosa"],
   "pasos": [("LCR normal", ["Encefalitis viral", "Meningitis"]),
             ("Hepatomegalia: compromiso hepático", ["Epilepsia"]),
             ("Convulsiona, no hay ataxia", ["Ataxia cerebelosa"])],
   "final": ("SÍNDROME DE REYE", ["Aspirina + infección viral", "Transaminasas y amonio altos"]),
   "nota": "Nunca aspirina en menores de 16 años con fiebre: usar paracetamol."},
  ["Sin ictericia; bilirrubina normal o poco elevada.",
   "Hipoglucemia y amonio alto; edema cerebral.",
   "Tratamiento de soporte en UCI."],
  NELSON + " · NINDS – Reye's syndrome information page")

# NEF-043 · matriz
V("matriz", "NEF-043", "secuestro-sin-agua-oliguria-sodio-urinario-bajo", "Lesión renal: prerrenal vs necrosis tubular",
  "NEFROLOGÍA ENAM: LESIÓN RENAL PRERRENAL", "NEFROLOGÍA",
  ("Lesión renal aguda prerrenal", ["Hipovolemia: el riñón sano ahorra sodio y agua",
   "Na urinario < 20, FeNa < 1%, orina concentrada"]),
  ("Varón de 38 años sin agua ni comida 36 horas", ["Oligoanuria · PA 95/60, FC 120", "Piel con turgencia baja, mucosas secas"]),
  {"rotulo": "Índices urinarios", "eje_x": "Índice", "eje_y": "Tipo",
   "cols": ["Na urinario", "FeNa", "Osm. urinaria"], "rows": ["Prerrenal", "Necrosis tubular"], "caso": (0, 0),
   "cells": [[("BAJO (< 20)", ["Ahorra sodio"]), ("< 1%", []), ("> 500", ["Concentrada"])],
             [("Alto (> 40)", ["Pierde sodio"]), ("> 2%", []), ("< 350", ["Isostenuria"])]]},
  ["Sedimento prerrenal: cilindros hialinos.",
   "Necrosis tubular: cilindros granulosos «marrón barroso».",
   "Cilindros eritrocitarios: glomerulonefritis."],
  "KDIGO – Clinical practice guideline for acute kidney injury (2012) · " + HARRISON)

# SP-080 · termómetro
V("termometro", "SP-080", "capacidad-producir-enfermedad-patogenicidad", "Propiedades del agente infeccioso",
  "SALUD PÚBLICA ENAM: PATOGENICIDAD", "SALUD PÚBLICA",
  ("Patogenicidad", ["Capacidad del agente de producir enfermedad en el infectado",
   "Se mide como enfermos / infectados"]),
  ("Pregunta de concepto", ["Capacidad del agente infeccioso", "de producir enfermedad"]),
  {"rotulo": "Del contacto a la gravedad",
   "niveles": [("Infecta", "Infectividad", ["Invade y se multiplica"]),
               ("Enferma", "Patogenicidad", ["Produce enfermedad"]),
               ("Agrava", "Virulencia", ["Casos graves o muerte"])],
   "caso_nivel": 1, "ruta_titulo": "Cómo se calcula", "paso_label": "PASO",
   "pasos": [(1, "Infectividad", ["Infectados / expuestos"], False),
             (2, "PATOGENICIDAD", ["Enfermos / infectados"], True),
             (3, "Virulencia", ["Graves o muertos / enfermos"], False)]},
  ["Letalidad: muertos / enfermos (medida de virulencia).",
   "Sarampión: alta infectividad y alta patogenicidad.",
   "Poliovirus: alta infectividad, baja patogenicidad."],
  "OPS – Módulos de principios de epidemiología para el control de enfermedades (MOPECE) · Gordis – Epidemiology 6.ª ed. (2019)")

# GIN-109 · árbol
A("GIN-109", "presentacion-cara-mentoanterior-parto-vaginal", "Presentación de cara",
  "OBSTETRICIA ENAM: PRESENTACIÓN DE CARA", "OBSTETRICIA",
  ("Presentación de cara", ["Cabeza en deflexión máxima; el punto guía es el mentón",
   "Mentoanterior: puede nacer por vía vaginal"]),
  ("Multigesta de 37 semanas en trabajo de parto", ["9 cm, 100% borrado, membranas rotas", "Cara en mentoanterior · LCF normales"]),
  Q("¿Hacia dónde está el mentón?", [
      L("Mentoanterior", "PARTO VAGINAL ESPONTÁNEO", ["El mentón pasa bajo el pubis"], path=True),
      L("Mentotransverso", "Esperar rotación", ["Si no rota: cesárea"]),
      L("Mentoposterior", "Cesárea", ["No puede nacer vaginal"])], path=True),
  ("Qué evitar", [("Evitar", True), ("Motivo", False)], [
      ("Vacuum", ["Contraindicado", "Trauma facial"]),
      ("Electrodo fetal", ["No en la cara", "Lesión ocular"]),
      ("Fórceps", ["Solo expertos", "Riesgo materno-fetal"])]),
  ["El 60-80% de las presentaciones de cara son mentoanteriores.",
   "La mentoposterior persistente no puede flexionar para salir.",
   "Edema facial del RN: se resuelve en días."],
  WILLIAMS)

# CIR-061 · árbol
A("CIR-061", "quemadura-circunferencial-pierna-sin-pulso-escarotomia", "Quemadura circunferencial",
  "CIRUGÍA ENAM: ESCAROTOMÍA", "CIRUGÍA",
  ("Quemadura circunferencial de espesor total", ["La escara rígida no se expande y comprime vasos",
   "Sin pulso distal: escarotomía"]),
  ("Adolescente de 15 años con quemadura hace 7 días", ["Tercer grado, circunferencial en la pierna", "Pulso pedio ausente"]),
  Q("¿Circunferencial y de espesor total?", [
      L("No", "Curación y vigilancia", ["Apósitos"]),
      Q("¿Compromiso distal (pulso ausente)?", [
          L("Sí", "ESCAROTOMÍA", ["Incisión de la escara hasta tejido sano"], path=True),
          L("Persiste la isquemia", "Fasciotomía", ["Síndrome compartimental"])],
        edge="Sí", path=True)], path=True),
  ("Escarotomía vs fasciotomía", [("Escarotomía", True), ("Fasciotomía", False)], [
      ("Corta", ["Solo la escara", "Piel y fascia"]),
      ("Indicación", ["Quemadura circunferencial", "Compartimental, eléctrica"]),
      ("Anestesia", ["Mínima (escara insensible)", "Quirófano"])]),
  ["En el tórax, la escarotomía mejora la ventilación.",
   "Las quemaduras eléctricas suelen requerir fasciotomía.",
   "Vigilar pulsos con Doppler cada hora."],
  "ABA – Advanced Burn Life Support Course (2022) · " + ATLS)

# NEF-044 · embudo
V("embudo", "NEF-044", "litiasis-itu-repeticion-macrofagos-espumosos-xantogranulomatosa", "Infección renal crónica con macrófagos espumosos",
  "NEFROLOGÍA ENAM: PIELONEFRITIS XANTOGRANULOMATOSA", "NEFROLOGÍA",
  ("Pielonefritis xantogranulomatosa", ["Infección crónica sobre litiasis obstructiva (Proteus, E. coli)",
   "Macrófagos espumosos cargados de lípidos; riñón destruido"]),
  ("Mujer de 62 años con 1 mes de fiebre y dolor lumbar", ["Litiasis e ITU a repetición · Hb 9", "Orina: macrófagos de aspecto espumoso"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Fiebre y dolor lumbar crónicos con litiasis",
   "candidatos": ["P. xantogranulomatosa", "TB renal", "Adenocarcinoma renal", "Absceso renal", "Pionefrosis"],
   "pasos": [("Leucocituria con ITU típicas, no piuria estéril", ["TB renal"]),
             ("Infección crónica sobre litiasis", ["Adenocarcinoma renal"]),
             ("Macrófagos espumosos en la orina", ["Absceso renal", "Pionefrosis"])],
   "final": ("PIELONEFRITIS XANTOGRANULOMATOSA", ["Riñón no funcional con cálculo", "Tratamiento: nefrectomía"]),
   "nota": "En la TEM simula un tumor: signo de la «pata de oso»."},
  ["Más frecuente en mujeres de edad media con litiasis coraliforme.",
   "Anemia y VSG alta por inflamación crónica.",
   "Antibiótico previo a la cirugía."],
  "Campbell-Walsh-Wein Urology 12.ª ed. (2020) · EAU – Guidelines on urological infections (2024)")

# END-030 · radial
V("radial", "END-030", "diabetes-actividad-fisica-150-minutos", "Actividad física en la diabetes",
  "ENDOCRINOLOGÍA ENAM: ACTIVIDAD FÍSICA EN DM2", "ENDOCRINOLOGÍA",
  ("Actividad física en adultos de 18 a 64 años", ["Al menos 150 minutos por semana de intensidad moderada",
   "Mejora la sensibilidad a la insulina y la HbA1c"]),
  ("Pregunta de concepto", ["Actividad física en la diabetes tipo 2", "¿Qué característica debe cumplir?"]),
  {"rotulo": "Mapa del tema", "centro": "ACTIVIDAD FÍSICA", "centro_sub": "Adultos 18-64 años", "ans": 0,
   "items": [("150 MIN/SEMANA", ["Intensidad moderada", "o 75 min vigorosa"]),
             ("Fuerza", ["2 días por semana"]),
             ("Continuidad", ["No más de 2 días sin ejercicio"]),
             ("Sedentarismo", ["Interrumpir lo sentado"]),
             ("Precaución", ["Hipoglucemia con insulina"])],
   "ruta": ["Diabetes tipo 2", "Prevención y tratamiento", "Recomendación OMS/ADA", "150 MIN MODERADA"]},
  ["Moderada: puede hablar pero no cantar (caminar rápido).",
   "No requiere entrenador ni consentimiento de familiares.",
   "La metformina no contraindica el ejercicio."],
  "OMS – Directrices sobre actividad física y hábitos sedentarios (2020) · ADA – Standards of Care in Diabetes (2025)")

# PED-121 · árbol
A("PED-121", "lactante-4-semanas-acolia-bilirrubina-directa-ecografia", "Colestasis del lactante",
  "PEDIATRÍA ENAM: COLESTASIS NEONATAL", "PEDIATRÍA",
  ("Colestasis neonatal", ["Ictericia después de las 2 semanas con bilirrubina directa alta",
   "Primer examen: ecografía abdominal (vesícula, vía biliar, quistes)"]),
  ("Lactante de 4 semanas", ["Ictericia progresiva, orina oscura y heces pálidas", "Bilirrubina conjugada 12 mg/dL"]),
  Q("¿Bilirrubina directa > 1 mg/dL?", [
      L("No", "Ictericia no conjugada", ["Lactancia, hemólisis"]),
      Q("ECOGRAFÍA ABDOMINAL", [
          L("Vesícula ausente, cordón triangular", "Sospecha de atresia", ["Kasai antes de 60 días"], path=True),
          L("Quiste de colédoco", "Cirugía", ["Resección y derivación"])],
        edge="Sí: colestasis", path=True)], path=True),
  ("Estudios de la colestasis", [("Ecografía", True), ("Gammagrafía", False), ("Biopsia", False)], [
      ("Busca", ["Vesícula, vía biliar", "Excreción al intestino", "Proliferación ductal"]),
      ("Momento", ["Primero", "Si hay duda", "Casi siempre"])]),
  ["La colangiografía intraoperatoria confirma la atresia.",
   "Heces acólicas: usar la tarjeta colorimétrica de heces.",
   "Dar vitamina K: la colestasis la reduce."],
  "NASPGHAN/ESPGHAN – Guideline for the evaluation of cholestatic jaundice in infants (2017) · " + NELSON)

# GIN-110 · árbol
A("GIN-110", "pap-lesion-alto-grado-colposcopia-biopsia", "PAP con lesión de alto grado",
  "GINECOLOGÍA ENAM: LESIÓN INTRAEPITELIAL DE ALTO GRADO", "GINECOLOGÍA",
  ("Lesión intraepitelial de alto grado (LIEAG)", ["Riesgo de NIC 2-3 o cáncer",
   "Conducta: colposcopía con biopsia dirigida"]),
  ("Mujer de 32 años nulípara", ["PAP: lesión intraepitelial de alto grado"]),
  Q("¿Qué informa el PAP?", [
      L("ASC-US o bajo grado", "Repetir o prueba VPH", ["Según edad"]),
      L("Alto grado (LIEAG)", "COLPOSCOPÍA Y BIOPSIA", ["NIC 2-3 confirmado: LEEP"], path=True),
      L("Carcinoma", "Biopsia y estadificación", ["Oncología"])], path=True),
  ("Grados de NIC", [("NIC 1", False), ("NIC 2-3", True)], [
      ("Epitelio", ["Tercio inferior", "Dos tercios o todo"]),
      ("Conducta", ["Seguimiento", "LEEP o cono"])]),
  ["El cono o LEEP se hace después de confirmar con biopsia.",
   "Ver y tratar (LEEP inmediato) es opción en zonas de difícil seguimiento.",
   "En nulíparas, cuidar la longitud cervical en la escisión."],
  "MINSA – Guía de práctica clínica para la prevención y manejo del cáncer de cuello uterino (2017) · ASCCP – Risk-based management consensus (2019)")

# REU-033 · puntaje
V("puntaje", "REU-033", "eritema-facial-proteinuria-derrame-pleural-lupus", "Lupus: criterios EULAR/ACR",
  "REUMATOLOGÍA ENAM: LUPUS ERITEMATOSO SISTÉMICO", "REUMATOLOGÍA",
  ("Lupus eritematoso sistémico", ["Mujer joven con compromiso cutáneo, renal, seroso y articular",
   "Criterios EULAR/ACR 2019: ANA ≥ 1:80 + ≥ 10 puntos"]),
  ("Mujer de 25 años", ["Edema y orina espumosa · artralgias, fotosensibilidad", "Eritema facial · MV abolido en ambas bases"]),
  {"rotulo": "Criterios EULAR/ACR 2019 en el caso", "escala": "EULAR/ACR 2019", "total": 15, "max": 23,
   "total_label": "Puntaje del caso",
   "interpreta": "≥ 10: clasifica como LES (con ANA +)",
   "items": [("Lupus cutáneo agudo (eritema malar)", "6", True), ("Artritis (sinovitis ≥ 2)", "6", False),
             ("Serositis: derrame pleural", "5", True), ("Proteinuria > 0.5 g/24 h", "4", True),
             ("Fiebre > 38.3 °C", "2", False)],
   "bandas": [("< 10", "No clasifica", "Buscar otra causa", False),
              ("≥ 10", "LES", "ANA, anti-DNA, complemento; biopsia renal", True)]},
  ["Orina espumosa + edema: nefritis lúpica (síndrome nefrótico).",
   "Hidroxicloroquina para todos los pacientes con LES.",
   "Anti-DNA y complemento bajo se asocian a nefritis."],
  "EULAR/ACR – Classification criteria for SLE (2019) · EULAR – Recommendations for the management of SLE (2023)")

# CAR-046 · fases
V("fases", "CAR-046", "papiledema-confusion-pa-190-120-labetalol", "Encefalopatía hipertensiva",
  "CARDIOLOGÍA ENAM: EMERGENCIA HIPERTENSIVA", "CARDIOLOGÍA",
  ("Encefalopatía hipertensiva", ["Emergencia: PA muy alta + cefalea, vómitos, papiledema, confusión",
   "Labetalol EV; bajar la PAM ≤ 25% en la primera hora"]),
  ("Varón de 48 años con HTA crónica", ["Cefalea, vómitos, papiledema", "PA 190/120 · confuso, sin focalización"]),
  {"rotulo": "Descenso de la PA", "ans": 0,
   "fases": [("Hora 1", "0-1 h", "LABETALOL EV", ["↓ PAM ≤ 25%"]),
             ("Horas 2-6", "2-6 h", "PA ~ 160/100", ["Si tolera"]),
             ("Días 1-2", "24-48 h", "PA normal", ["Pasar a vía oral"])],
   "curvas": [("PA", ROSE, [1.0, 0.75, 0.65, 0.55, 0.5, 0.45, 0.4])],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Labetalol", True), ("Nitroprusiato", False), ("Nifedipino", False), ("Nitroglicerina", False)]},
  ["El nitroprusiato aumenta la presión intracraneal.",
   "Nifedipino sublingual: descenso brusco, riesgo de isquemia.",
   "Alternativas: nicardipino o clevidipino."],
  "ESC/ESH – Hypertension guidelines (2023) · ESC – Position document on hypertensive emergencies (2019)")

# END-031 · matriz
V("matriz", "END-031", "pastillas-adelgazar-tsh-indetectable-tiroides-no-palpable-facticia", "Tirotoxicosis: origen",
  "ENDOCRINOLOGÍA ENAM: TIROTOXICOSIS FACTICIA", "ENDOCRINOLOGÍA",
  ("Tirotoxicosis facticia", ["Ingesta de hormona tiroidea (a veces oculta en productos para adelgazar)",
   "Tiroides pequeña, captación y tiroglobulina bajas"]),
  ("Mujer de 34 años en programa para bajar de peso", ["Toma pastillas desconocidas · FC 122, temblor", "Tiroides no palpable · TSH indetectable"]),
  {"rotulo": "Origen de la tirotoxicosis", "eje_x": "Hallazgo", "eje_y": "Causa",
   "cols": ["Tiroides", "Laboratorio"], "rows": ["Facticia", "Graves", "Tiroiditis subaguda", "Hashimoto"], "caso": (0, 0),
   "cells": [[("NO PALPABLE", ["Atrófica"]), ("Tiroglobulina baja", ["Captación baja"])],
             [("Bocio difuso", ["Exoftalmos"]), ("TRAb +", ["Captación alta"])],
             [("Dolorosa", ["Tras un virus"]), ("VSG alta", ["Captación baja"])],
             [("Bocio firme", []), ("Anti-TPO +", ["Hipotiroidismo luego"])]]},
  ["La tiroglobulina baja distingue la facticia de la tiroiditis.",
   "Amiodarona: tiene yodo y es otra causa, pero no se toma para adelgazar.",
   "Tratamiento: suspender la hormona y betabloqueante."],
  "ATA – Guidelines for diagnosis and management of hyperthyroidism (2016) · Williams Textbook of Endocrinology 15.ª ed. (2024)")

# SP-081 · tarjetas
V("tarjetas", "SP-081", "150-casos-no-aleatorio-muestreo-conveniencia", "Tipos de muestreo",
  "SALUD PÚBLICA ENAM: MUESTREO POR CONVENIENCIA", "SALUD PÚBLICA",
  ("Muestreo por conveniencia", ["No probabilístico: se toman los casos disponibles",
   "Rápido y barato, pero poco representativo"]),
  ("Investigador que necesita 150 casos", ["Los toma de modo no aleatorio", "De los que ingresaron al hospital"]),
  {"rotulo": "¿Qué muestreo es?", "ans": 0, "cards": [
      {"titulo": "CONVENIENCIA", "datos": [
          ("¿Al azar?", "No", True), ("Cómo", "Casos disponibles", True),
          ("Ejemplo", "Los que llegan al hospital", True)],
       "pie": "No probabilístico"},
      {"titulo": "Por cuotas", "datos": [
          ("¿Al azar?", "No", False), ("Cómo", "Cupos por grupo", False),
          ("Ejemplo", "50 varones y 50 mujeres", False)],
       "pie": "No probabilístico"},
      {"titulo": "Redes (bola de nieve)", "datos": [
          ("¿Al azar?", "No", False), ("Cómo", "Uno recluta a otro", False),
          ("Ejemplo", "Poblaciones ocultas", False)],
       "pie": "No probabilístico"},
      {"titulo": "Conglomerados", "datos": [
          ("¿Al azar?", "Sí", False), ("Cómo", "Se sortean grupos", False),
          ("Ejemplo", "Colegios al azar", False)],
       "pie": "Probabilístico"}]},
  ["Probabilístico: todos tienen una probabilidad conocida de ser elegidos.",
   "Los resultados por conveniencia no se generalizan a la población.",
   "Estratificado: se sortea dentro de cada estrato."],
  "Hernández-Sampieri – Metodología de la investigación 7.ª ed. (2023)")

# END-032 · embudo
V("embudo", "END-032", "bocio-exoftalmos-mixedema-pretibial-graves", "Hipertiroidismo con exoftalmos",
  "ENDOCRINOLOGÍA ENAM: ENFERMEDAD DE GRAVES", "ENDOCRINOLOGÍA",
  ("Enfermedad de Graves", ["Anticuerpos que estimulan el receptor de TSH (TRAb)",
   "Bocio difuso + oftalmopatía + mixedema pretibial"]),
  ("Mujer de 26 años con 3 meses de síntomas", ["Baja 12 kg, palpitaciones, intolerancia al calor", "Bocio, exoftalmos bilateral, mixedema pretibial"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Mujer joven con hipertiroidismo y bocio",
   "candidatos": ["Graves", "Bocio multinodular", "Adenoma tóxico", "Tiroiditis de Quervain", "Hashimoto"],
   "pasos": [("Hipertiroidismo franco de 3 meses", ["Hashimoto"]),
             ("Tiroides no dolorosa, sin fiebre", ["Tiroiditis de Quervain"]),
             ("Exoftalmos + mixedema pretibial", ["Bocio multinodular", "Adenoma tóxico"])],
   "final": ("ENFERMEDAD DE GRAVES", ["TRAb positivos", "Captación difusa y alta"]),
   "nota": "Tratamiento: metimazol + propranolol; luego yodo radiactivo o cirugía si recae."},
  ["Oftalmopatía y mixedema pretibial son exclusivos de Graves.",
   "En el embarazo (1.er trimestre): propiltiouracilo.",
   "El tabaco empeora la oftalmopatía."],
  "ATA – Guidelines for hyperthyroidism (2016) · ETA – Guideline for Graves' hyperthyroidism (2018)")

# TRA-021 · fases
V("fases", "TRA-021", "lactante-pie-equinovaro-referir-ortopedista", "Pie equinovaro: método Ponseti",
  "TRAUMATOLOGÍA ENAM: PIE EQUINOVARO CONGÉNITO", "TRAUMATOLOGÍA",
  ("Pie equinovaro congénito", ["Equino, varo, aducto y cavo",
   "Tratamiento precoz con método Ponseti: referir al ortopedista infantil"]),
  ("Lactante de 1 mes en control pediátrico", ["Se diagnostica pie equinovaro"]),
  {"rotulo": "Método Ponseti", "ans": 0,
   "fases": [("Diagnóstico", "Al nacer", "REFERIR", ["Ortopedista infantil"]),
             ("Yesos", "1-2 meses", "Yesos seriados", ["Cambio semanal"]),
             ("Tenotomía", "~ 2 meses", "Aquiles", ["Corrige el equino"]),
             ("Férula", "Hasta 4 años", "Férula de abducción", ["Evita recaídas"])],
   "curvas": [],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("Referir al ortopedista", True), ("TC de pies", False), ("Rx de pies", False), ("Observar 3 meses", False)]},
  ["El diagnóstico es clínico: no necesita Rx ni TC.",
   "Empezar los yesos en las primeras semanas de vida.",
   "Esperar empeora la rigidez del pie."],
  "Ponseti International Association – Clubfoot: Ponseti management 3.ª ed. · Lovell and Winter's Pediatric Orthopaedics 8.ª ed. (2020)")

# GIN-111 · termómetro
V("termometro", "GIN-111", "vih-tar-carga-viral-500-parto-vaginal", "VIH: vía del parto según carga viral",
  "OBSTETRICIA ENAM: VIH Y VÍA DEL PARTO", "OBSTETRICIA",
  ("Vía del parto en gestante con VIH", ["Depende de la carga viral cerca del parto",
   "Carga viral < 1000 copias/mL: parto vaginal"]),
  ("Primigesta de 38 semanas con VIH", ["En TAR desde antes del embarazo", "Carga viral hace 1 semana: 500 copias/mL"]),
  {"rotulo": "Carga viral (copias/mL)",
   "niveles": [("< 50", "Indetectable", ["Parto vaginal"]),
               ("50-999", "Baja", ["Parto vaginal"]),
               ("≥ 1000", "Alta o desconocida", ["Cesárea programada 38 sem"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Continuar el TAR", ["Sin interrupciones"], False),
             (2, "PARTO VAGINAL", ["Carga viral < 1000"], True),
             (3, "Zidovudina EV si ≥ 1000", ["Y cesárea antes de la labor"], False)]},
  ["Evitar amniotomía precoz, episiotomía e instrumentación.",
   "Profilaxis antirretroviral al RN y suspender lactancia materna.",
   "La cesárea de emergencia no reduce la transmisión."],
  "MINSA – NTS N.° 159-MINSA/2019/DGIESP (Transmisión materno-infantil de VIH, sífilis y hepatitis B) · HHS – Perinatal HIV guidelines (2024)")

# CB-039 · puntaje
V("puntaje", "CB-039", "miosis-bradipnea-sopor-venopunturas-naloxona", "Intoxicación por opioides",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR OPIOIDES", "CIENCIAS BÁSICAS",
  ("Toxíndrome opioide", ["Tríada: miosis + depresión respiratoria + depresión de la conciencia",
   "Antídoto: naloxona EV"]),
  ("Veterinario de 45 años", ["Eufórico y luego somnoliento · venopunturas", "Miosis, FR 12, SatO₂ 88% · PaCO₂ 70"]),
  {"rotulo": "Tríada opioide en el caso", "escala": "Opioides", "total": 3, "max": 3,
   "total_label": "Signos presentes",
   "interpreta": "Toxíndrome opioide completo",
   "items": [("Pupilas mióticas", "1", True), ("Depresión respiratoria (PaCO₂ 70)", "1", True),
             ("Depresión de la conciencia", "1", True)],
   "bandas": [("0-1", "Poco probable", "Buscar otra causa", False),
              ("2-3", "Toxíndrome opioide", "NALOXONA EV 0.04-0.4 mg; repetir", True)]},
  ["Ventilar con bolsa-máscara mientras actúa la naloxona.",
   "La naloxona dura menos que muchos opioides: vigilar la re-sedación.",
   "Flumazenilo es para benzodiacepinas."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019) · AHA – Opioid-associated emergencies (2023)")

# SP-082 · embudo
V("embudo", "SP-082", "tb-asentamiento-migrante-comunicacion-educativa", "TB en población migrante",
  "SALUD PÚBLICA ENAM: PROMOCIÓN EN TUBERCULOSIS", "SALUD PÚBLICA",
  ("Promoción de la salud en TB", ["Educar para reconocer síntomas y consultar a tiempo",
   "Sintomático respiratorio: tos con flema por más de 15 días"]),
  ("Aumento de TB en un nuevo asentamiento", ["Población migrante de zona rural", "Equipo de promoción de la salud"]),
  {"rotulo": "Embudo de actividades",
   "inicio": "Más casos de TB en un asentamiento",
   "candidatos": ["Comunicación educativa", "Quimioprofilaxis a niños", "Rx a todos", "Reubicar a la población", "BCG a adultos"],
   "pasos": [("La quimioprofilaxis es para contactos de casos", ["Quimioprofilaxis a niños"]),
             ("Rx masiva y BCG no son promoción", ["Rx a todos", "BCG a adultos"]),
             ("Reubicar vulnera derechos", ["Reubicar a la población"])],
   "final": ("COMUNICACIÓN EDUCATIVA", ["Reconocer precozmente los síntomas", "En su idioma y cultura"]),
   "nota": "La promoción actúa antes de la enfermedad: informa, educa y empodera a la comunidad."},
  ["Captación de sintomáticos respiratorios: baciloscopia o prueba molecular.",
   "Estudio de contactos de cada caso índice.",
   "La BCG protege contra formas graves en niños, no en adultos."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · MINSA – Lineamientos de promoción de la salud (2017)")

# TRA-022 · fases
V("fases", "TRA-022", "fractura-diafisis-humero-no-desplazada-ortesis", "Fractura diafisaria de húmero",
  "TRAUMATOLOGÍA ENAM: FRACTURA DE HÚMERO", "TRAUMATOLOGÍA",
  ("Fractura diafisaria de húmero", ["Mayoría con tratamiento conservador",
   "Ortesis funcional de Sarmiento tras una férula inicial"]),
  ("Mujer de 25 años con golpe directo en el brazo", ["Brazo inestable, doloroso", "Rx: diáfisis humeral no desplazada · radial indemne"]),
  {"rotulo": "Tratamiento conservador", "ans": 1,
   "fases": [("Inicial", "1-2 sem", "Férula en U", ["Cabestrillo"]),
             ("Funcional", "Desde 1-2 sem", "ORTESIS", ["Sarmiento"]),
             ("Consolida", "8-12 sem", "Retirar ortesis", ["Rx de control"])],
   "curvas": [("Callo", SKY, [0.0, 0.1, 0.3, 0.5, 0.7, 0.85, 1.0])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Ortesis", True), ("Yeso", False), ("Enclavijado", False), ("Cerclaje", False)]},
  ["Vigilar el nervio radial: mano caída.",
   "Cirugía si hay fractura abierta, lesión vascular o politrauma.",
   "La ortesis permite mover hombro y codo."],
  "AAOS – Humeral shaft fractures (OrthoInfo 2023) · Rockwood and Green's Fractures in Adults 10.ª ed. (2024)")

# NEF-045 · tarjetas
V("tarjetas", "NEF-045", "dolor-flanco-irradia-testiculo-sin-postura-colico-renal", "Dolor agudo en flanco",
  "NEFROLOGÍA ENAM: CÓLICO RENAL", "NEFROLOGÍA",
  ("Cólico renoureteral", ["Dolor intenso en flanco que irradia a ingle y genitales",
   "Inquieto, no encuentra postura; abdomen blando"]),
  ("Varón de 42 años con dolor EVA 9-10", ["Irradia a ingle y testículo · vómitos y sudor", "Abdomen blando, sin peritonismo · sin leucocitosis"]),
  {"rotulo": "¿Qué explica el dolor?", "ans": 0, "cards": [
      {"titulo": "CÓLICO RENAL", "datos": [
          ("Dolor", "Flanco → ingle y testículo", True), ("Abdomen", "Blando, sin peritonismo", True),
          ("Paciente", "Inquieto, sin postura", True)],
       "pie": "AINE + ecografía o TEM"},
      {"titulo": "Apendicitis", "datos": [
          ("Dolor", "Periumbilical → FID", False), ("Abdomen", "Rebote en FID", False),
          ("Paciente", "Quieto", False)],
       "pie": "Leucocitosis"},
      {"titulo": "Perforación gástrica", "datos": [
          ("Dolor", "Epigastrio súbito", False), ("Abdomen", "En tabla", False),
          ("Paciente", "Inmóvil", False)],
       "pie": "Neumoperitoneo"},
      {"titulo": "Infección urinaria", "datos": [
          ("Dolor", "Suprapúbico o lumbar", False), ("Abdomen", "Blando", False),
          ("Paciente", "Disuria, fiebre", False)],
       "pie": "Leucocituria"}]},
  ["Analgesia de elección: AINE (diclofenaco, ketorolaco).",
   "TEM sin contraste: estudio más sensible para litiasis.",
   "Fiebre + obstrucción: drenaje urgente."],
  "EAU – Guidelines on urolithiasis (2024)")

# PED-122 · termómetro
V("termometro", "PED-122", "onfalitis-celulitis-periumbilical-antibiotico-sistemico", "Infección del cordón umbilical",
  "PEDIATRÍA ENAM: ONFALITIS", "PEDIATRÍA",
  ("Onfalitis", ["Infección del muñón umbilical; puede extenderse a la pared abdominal",
   "Con celulitis: antibiótico sistémico inmediato"]),
  ("Recién nacido", ["Infección del muñón umbilical", "Celulitis alrededor del ombligo"]),
  {"rotulo": "Gravedad",
   "niveles": [("Normal", "Cordón seco", ["Cuidado en seco"]),
               ("Local", "Pus en el ombligo", ["Tópico y control en 2 días"]),
               ("Grave", "Celulitis periumbilical", ["Infección bacteriana grave"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "ANTIBIÓTICO SISTÉMICO", ["Ampicilina + gentamicina ± oxacilina"], True),
             (2, "Referir al hospital", ["Hemocultivo"], False),
             (3, "Vigilar complicaciones", ["Fascitis, sepsis, trombosis portal"], False)]},
  ["Clorhexidina al 4% (7.1% digluconato) previene la onfalitis en zonas de riesgo.",
   "Nitrato de plata: para el granuloma umbilical, no la infección.",
   "Gérmenes: S. aureus, estreptococo y gramnegativos."],
  "OMS/OPS – AIEPI neonatal · " + NELSON)

# NEF-046 · radial
V("radial", "NEF-046", "diabetico-30-anos-goteo-globo-vesical-vejiga-neurogenica", "Neuropatía autonómica diabética",
  "NEFROLOGÍA ENAM: VEJIGA NEUROGÉNICA", "NEFROLOGÍA",
  ("Vejiga neurogénica diabética", ["La neuropatía autonómica debilita el detrusor",
   "Retención con micción por rebosamiento (goteo)"]),
  ("Varón de 60 años con DM de 30 años", ["Tratamiento irregular", "Deseo de orinar, solo gotea · masa suprapúbica"]),
  {"rotulo": "Mapa del tema", "centro": "DIABETES", "centro_sub": "Neuropatía autonómica", "ans": 0,
   "items": [("VEJIGA NEUROGÉNICA", ["Retención con rebosamiento", "Detrusor hipocontráctil"]),
             ("Gastroparesia", ["Saciedad, vómitos"]),
             ("Hipotensión ortostática", ["Mareo al pararse"]),
             ("Disfunción eréctil", ["Frecuente"]),
             ("Taquicardia fija", ["En reposo"])],
   "ruta": ["DM de 30 años", "Neuropatía autonómica", "Detrusor hipocontráctil", "VEJIGA NEUROGÉNICA"]},
  ["Tratamiento: sonda vesical y luego cateterismo intermitente.",
   "Controlar la glucemia para frenar la neuropatía.",
   "Riesgo de ITU y daño renal por residuo alto."],
  "ADA – Standards of Care: Retinopathy, neuropathy and foot care (2025) · EAU – Neuro-urology guidelines (2024)")

# INF-056 · radial
V("radial", "INF-056", "veterinario-fiebre-ondulante-rosa-bengala-brucelosis", "Brucelosis",
  "INFECTOLOGÍA ENAM: BRUCELOSIS", "INFECTOLOGÍA",
  ("Brucelosis", ["Zoonosis por leche cruda o contacto con ganado",
   "Fiebre ondulante + dolor osteoarticular (sacroileítis, espondilitis)"]),
  ("Veterinario de 46 años de Huarochirí", ["1 mes de fiebre ondulante y dolor lumbar", "Compromiso de cadera · Rosa de Bengala (+)"]),
  {"rotulo": "Mapa del tema", "centro": "BRUCELOSIS", "centro_sub": "Zoonosis", "ans": 0,
   "items": [("ROSA DE BENGALA +", ["Tamizaje serológico", "Confirmar: aglutinación, cultivo"]),
             ("Exposición", ["Ganado, leche cruda, queso"]),
             ("Fiebre ondulante", ["Sudor nocturno, malestar"]),
             ("Osteoarticular", ["Sacroileítis, espondilitis"]),
             ("Tratamiento", ["Doxiciclina + rifampicina"])],
   "ruta": ["Veterinario de la sierra", "Fiebre + dolor articular", "Rosa de Bengala (+)", "BRUCELOSIS"]},
  ["Enfermedad ocupacional: veterinarios, ganaderos, matarifes.",
   "Espondilitis: agregar estreptomicina o gentamicina.",
   "Bartonelosis: valles interandinos, anemia hemolítica."],
  "MINSA – NTS de brucelosis humana · OMS – Brucellosis in humans and animals (2006)")

# REU-034 · tarjetas
V("tarjetas", "REU-034", "nina-prurito-cuero-cabelludo-liendres-pediculosis", "Prurito del cuero cabelludo",
  "DERMATOLOGÍA ENAM: PEDICULOSIS", "DERMATOLOGÍA",
  ("Pediculosis capitis", ["Piojos en el cuero cabelludo; liendres adheridas al tallo del pelo",
   "Prurito, lesiones de rascado y adenopatías occipitales"]),
  ("Niña de 7 años con 1 mes de prurito", ["Lesiones de rascado en el cuero cabelludo", "Protuberancias blanco nacaradas en el pelo · adenopatías"]),
  {"rotulo": "¿Qué dermatosis es?", "ans": 0, "cards": [
      {"titulo": "PEDICULOSIS", "datos": [
          ("Lesión", "Liendres en el pelo", True), ("Dónde", "Nuca y retroauricular", True),
          ("Prueba", "No se desprenden", True)],
       "pie": "Permetrina 1%, repetir al día 9"},
      {"titulo": "Impétigo", "datos": [
          ("Lesión", "Costras melicéricas", False), ("Dónde", "Cara, zonas expuestas", False),
          ("Prueba", "Estafilococo, estreptococo", False)],
       "pie": "Puede complicar el rascado"},
      {"titulo": "Eccema atópico", "datos": [
          ("Lesión", "Placas liquenificadas", False), ("Dónde", "Pliegues", False),
          ("Prueba", "Historia de atopia", False)],
       "pie": "Piel seca"},
      {"titulo": "Caspa", "datos": [
          ("Lesión", "Escamas sueltas", False), ("Dónde", "Todo el cuero cabelludo", False),
          ("Prueba", "Se desprenden al soplar", False)],
       "pie": "Dermatitis seborreica"}]},
  ["Revisar y tratar a los contactos del hogar.",
   "Peinar con peine fino en el cabello húmedo.",
   "Ivermectina oral si hay resistencia."],
  "AAP – Head lice clinical report (Pediatrics 2022) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# INF-057 · fases
V("fases", "INF-057", "relacion-riesgo-20-dias-elisa-cuarta-generacion", "VIH: periodo de ventana",
  "INFECTOLOGÍA ENAM: DIAGNÓSTICO TEMPRANO DE VIH", "INFECTOLOGÍA",
  ("Diagnóstico temprano de VIH", ["ELISA de 4.ª generación detecta antígeno p24 + anticuerpos",
   "Acorta la ventana a unas 2-3 semanas"]),
  ("Varón de 46 años", ["Relación sexual sin protección hace 20 días", "Quiere una prueba de VIH"]),
  {"rotulo": "Marcadores tras la exposición", "ans": 1,
   "fases": [("Eclipse", "0-10 días", "Nada detectable", ["Aún puede contagiar"]),
             ("p24", "2-3 sem", "ELISA 4.ª GENERACIÓN", ["Antígeno p24 + anticuerpos"]),
             ("Anticuerpos", "3-4 sem", "Prueba rápida", ["ELISA 3.ª generación"]),
             ("Confirma", "4-6 sem", "Western blot / IFI", ["Hoy: carga viral"])],
   "curvas": [("ARN", ROSE, [0.1, 0.6, 0.95, 0.7, 0.4, 0.35, 0.3]),
              ("p24", AMBER, [0.0, 0.4, 0.8, 0.4, 0.1, 0.05, 0.05]),
              ("Ac", SKY, [0.0, 0.0, 0.2, 0.6, 0.85, 0.95, 1.0])],
   "chips_titulo": "Prueba · marcada la correcta",
   "chips": [("ELISA 4.ª generación", True), ("Western blot", False), ("IFI", False), ("Genotipificación", False)]},
  ["Si es negativo a los 20 días, repetir a las 6 semanas.",
   "La genotipificación estudia resistencia, no diagnostica.",
   "Ofrecer PEP solo dentro de las 72 horas."],
  "MINSA – NTS N.° 204-MINSA/DGIESP-2023 (VIH) · CDC – Laboratory testing for the diagnosis of HIV infection (2014, act. 2018)")

# GIN-112 · termómetro
V("termometro", "GIN-112", "32-semanas-contracciones-cervix-15-mm-corticoides-tocolisis", "Amenaza de parto pretérmino",
  "OBSTETRICIA ENAM: AMENAZA DE PARTO PRETÉRMINO", "OBSTETRICIA",
  ("Amenaza de parto pretérmino", ["Contracciones con cambios cervicales entre 22 y 36 semanas",
   "Cérvix corto: corticoides + tocolíticos"]),
  ("Primigesta de 32 semanas con contracciones", ["2 contracciones en 20 minutos", "Borramiento 50% · cervicometría 15 mm"]),
  {"rotulo": "Longitud cervical",
   "niveles": [("> 30 mm", "Riesgo bajo", ["Alta con indicaciones"]),
               ("16-30 mm", "Riesgo intermedio", ["Observar, fibronectina"]),
               ("≤ 15 mm", "Riesgo alto", ["Parto probable en 7 días"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "CORTICOIDES + TOCOLÍTICO", ["Betametasona · nifedipino 48 h"], True),
             (2, "Sulfato de Mg si < 32 sem", ["Neuroprotección fetal"], False),
             (3, "Cerclaje y progesterona", ["Prevención, no en APP activa"], False)]},
  ["La tocólisis busca ganar 48 h para los corticoides.",
   "Nifedipino o atosibán son los tocolíticos de elección.",
   "No usar tocolíticos si hay corioamnionitis o sufrimiento fetal."],
  "ACOG – Practice Bulletin N.° 171: Management of preterm labor (2016, reafirmado 2020) · " + WILLIAMS)

# GIN-113 · puntaje
V("puntaje", "GIN-113", "flujo-gris-fetido-celulas-clave-gardnerella", "Vaginosis bacteriana: criterios de Amsel",
  "GINECOLOGÍA ENAM: VAGINOSIS BACTERIANA", "GINECOLOGÍA",
  ("Vaginosis bacteriana", ["Desequilibrio de la flora: disminuyen los lactobacilos",
   "Gardnerella vaginalis y anaerobios; células clave en el frotis"]),
  ("Mujer de 21 años con flujo vaginal", ["Leucorrea blanca grisácea y fétida", "Mucosa normal · frotis con células clave"]),
  {"rotulo": "Criterios de Amsel en el caso", "escala": "Amsel", "total": 3, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Vaginosis bacteriana",
   "items": [("Flujo blanco-grisáceo homogéneo", "1", True), ("Olor a pescado (aminas)", "1", True),
             ("Células clave > 20%", "1", True), ("pH vaginal > 4.5", "1", False)],
   "bandas": [("0-2", "No cumple", "Buscar otra causa", False),
              ("≥ 3", "Vaginosis bacteriana", "Metronidazol 500 mg c/12 h por 7 días", True)]},
  ["No es una ITS: no se trata a la pareja.",
   "Candida: flujo grumoso y prurito; Trichomonas: flujo espumoso y cérvix en fresa.",
   "En gestantes con síntomas también se trata."],
  "CDC – Sexually transmitted infections treatment guidelines (2021) · MINSA – Guía nacional de manejo de ITS (2018)")

# OFT-028 · árbol
A("OFT-028", "cuerpo-extrano-incrustado-perforacion-no-retirar", "Cuerpo extraño ocular",
  "OFTALMOLOGÍA ENAM: TRAUMA OCULAR PENETRANTE", "OFTALMOLOGÍA",
  ("Cuerpo extraño ocular penetrante", ["No retirar el objeto: puede salir el contenido del ojo",
   "Proteger sin presionar y referir a oftalmología"]),
  ("Varón de 47 años", ["Cuerpo extraño incrustado en el ojo izquierdo", "Con perforación ocular · primer nivel"]),
  Q("¿Superficial o penetrante?", [
      L("Superficial", "Irrigar con suero", ["Retirar con hisopo"]),
      L("Penetrante o perforación", "NO RETIRARLO", ["Protector rígido sin presión", "Referir a oftalmología"], path=True)], path=True),
  ("En el primer nivel", [("Hacer", True), ("No hacer", False)], [
      ("Ojo", ["Cubrir con protector rígido", "Frotar o presionar"]),
      ("Objeto", ["Estabilizarlo", "Retirarlo"]),
      ("Otros", ["Antiemético, antitetánica", "Colirios o pomadas"])]),
  ["Vomitar o hacer esfuerzo aumenta la presión intraocular.",
   "Se cubren ambos ojos para evitar movimientos conjugados.",
   "TC de órbitas si se sospecha cuerpo extraño intraocular."],
  "AAO – Eye trauma: first aid (2023) · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")
