"""Bloque 6 · parte F."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
GOODMAN = "Goodman & Gilman – Las bases farmacológicas de la terapéutica 14.ª ed. (2023)"

# END-029 · tarjetas
V("tarjetas", "END-029", "brazos-elevados-congestion-cuello-pemberton", "Tipos de bocio",
  "ENDOCRINOLOGÍA ENAM: BOCIO SUMERGIDO", "ENDOCRINOLOGÍA",
  ("Bocio sumergido (retroesternal)", ["Crece hacia el tórax y comprime venas y tráquea",
   "Signo de Pemberton: al elevar los brazos, congestión facial y disnea"]),
  ("Hallazgo del examen físico", ["Al elevar ambos brazos: distensión venosa del cuello", "Y dificultad respiratoria"]),
  {"rotulo": "¿Qué bocio es?", "ans": 0, "cards": [
      {"titulo": "SUMERGIDO", "datos": [
          ("Clave", "Pemberton (+)", True), ("Examen", "Polo inferior no palpable", True),
          ("Estudio", "TEM cervicotorácica", True)],
       "pie": "Comprime vía aérea y venas"},
      {"titulo": "Hiperfuncionante", "datos": [
          ("Clave", "Tirotoxicosis", False), ("Examen", "Nódulos autónomos", False),
          ("Estudio", "TSH baja, gammagrafía", False)],
       "pie": "Bocio tóxico"},
      {"titulo": "Endémico", "datos": [
          ("Clave", "Déficit de yodo", False), ("Examen", "Difuso o multinodular", False),
          ("Estudio", "Yoduria", False)],
       "pie": "Prevención: sal yodada"},
      {"titulo": "Abscedado", "datos": [
          ("Clave", "Fiebre y dolor", False), ("Examen", "Masa fluctuante", False),
          ("Estudio", "Ecografía y punción", False)],
       "pie": "Tiroiditis supurativa"}]},
  ["Tratamiento del bocio compresivo: tiroidectomía (casi siempre por vía cervical).",
   "Pemberton (+) indica obstrucción del estrecho torácico superior.",
   "Espirometría: curva flujo-volumen con obstrucción de vía aérea superior."],
  "ATA – Guidelines for adult patients with thyroid nodules (2015) · Williams Textbook of Endocrinology 15.ª ed. (2024)")

# GIN-103 · fases
V("fases", "GIN-103", "alumbramiento-dirigido-preeclampsia-oxitocina", "Manejo activo del alumbramiento",
  "OBSTETRICIA ENAM: ALUMBRAMIENTO DIRIGIDO", "OBSTETRICIA",
  ("Manejo activo del tercer periodo", ["Oxitocina 10 UI IM al minuto del parto",
   "En la preeclampsia no se usa metilergometrina (sube la PA)"]),
  ("Gestante con preeclampsia", ["Se decide alumbramiento dirigido", "¿Qué uterotónico al minuto del parto?"]),
  {"rotulo": "Tercer periodo del parto", "ans": 1,
   "fases": [("Expulsivo", "Parto", "Nace el bebé", ["Descartar otro feto"]),
             ("Minuto 1", "Uterotónico", "OXITOCINA 10 UI IM", ["Primera elección"]),
             ("Tracción", "2-3 min", "Tracción del cordón", ["Con contratracción"]),
             ("Masaje", "Postplacenta", "Masaje uterino", ["Vigilar el tono"])],
   "curvas": [],
   "chips_titulo": "Uterotónico · marcado el correcto",
   "chips": [("Oxitocina", True), ("Metilergometrina", False), ("Ácido tranexámico", False), ("Atosibán", False)]},
  ["Metilergometrina contraindicada en HTA y preeclampsia.",
   "El ácido tranexámico trata la hemorragia; no es el uterotónico.",
   "Atosibán es tocolítico: relaja el útero."],
  "OMS – Recomendaciones sobre uterotónicos para la prevención de la HPP (2018) · MINSA – Guía de atención de emergencias obstétricas")

# REU-030 · embudo
V("embudo", "REU-030", "placas-escama-nacarada-piqueteado-ungueal-psoriasis", "Placas descamativas y uñas alteradas",
  "DERMATOLOGÍA ENAM: PSORIASIS", "DERMATOLOGÍA",
  ("Psoriasis", ["Placas eritematosas bien delimitadas con escama blanca nacarada",
   "Uñas: piqueteado, onicólisis y «mancha de aceite»"]),
  ("Varón de 40 años", ["Placas con escama nacarada en piel y cuero cabelludo", "Onicólisis y piqueteado ungueal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Placas descamativas en piel y cuero cabelludo",
   "candidatos": ["Psoriasis", "Dermatitis atópica", "Ictiosis", "Dermatitis seborreica", "Linfoma cutáneo"],
   "pasos": [("Placas bien delimitadas con escama nacarada", ["Dermatitis atópica", "Ictiosis"]),
             ("Piqueteado ungueal y onicólisis", ["Dermatitis seborreica"]),
             ("Placas típicas, sin infiltración ni tumores", ["Linfoma cutáneo"])],
   "final": ("PSORIASIS", ["Escama nacarada + uñas", "Signo de Auspitz y Koebner"]),
   "nota": "Preguntar por dolor articular: hasta un 30% desarrolla artritis psoriásica."},
  ["Leve: corticoide tópico + análogo de vitamina D.",
   "Moderada a grave: fototerapia, metotrexato o biológicos.",
   "Asociada a síndrome metabólico y riesgo cardiovascular."],
  "AAD/NPF – Guidelines of care for the management of psoriasis (2019-2021) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# INF-055 · árbol
A("INF-055", "viaje-zona-endemica-ns1-positivo-caso-confirmado", "Dengue: clasificación del caso",
  "INFECTOLOGÍA ENAM: DENGUE IMPORTADO", "INFECTOLOGÍA",
  ("Clasificación de casos de dengue", ["Confirmado: prueba de laboratorio positiva (NS1, RT-PCR, IgM)",
   "Por procedencia: importado si se contagió fuera del ámbito local"]),
  ("Mujer de 29 años con 3 días de fiebre", ["Mialgias, cefalea, artralgias · NS1 positivo", "Viajó a zona endémica; aquí no hay vector"]),
  Q("¿Fiebre y estuvo en zona con dengue?", [
      L("No", "No es caso de dengue", ["Otro diagnóstico"]),
      Q("¿Laboratorio positivo?", [
          L("Sí: NS1 +", "CASO CONFIRMADO", ["Importado", "Notificación inmediata"], path=True),
          L("Pendiente", "Caso probable", ["Hasta el resultado"]),
          L("Negativo", "Descartado", ["Con prueba adecuada"])],
        edge="Sí: caso probable", path=True)], path=True),
  ("Clasificación por procedencia", [("Importado", True), ("Autóctono", False)], [
      ("Contagio", ["Fuera del ámbito", "En el ámbito local"]),
      ("Este caso", ["Viajó a zona endémica", "No hay vector local"])]),
  ["NS1 y RT-PCR sirven en los primeros 5 días; IgM después.",
   "Un caso importado en zona con Aedes obliga a control vectorial inmediato.",
   "Signos de alarma: dolor abdominal, vómitos persistentes, sangrado, letargia."],
  "MINSA – NTS N.° 211-MINSA/DGIESP-2024 (Atención del dengue) · CDC-MINSA – Directiva de vigilancia de dengue")

# PED-113 · tarjetas
V("tarjetas", "PED-113", "escroto-vacio-testiculo-perineal-ectopia", "Testículo fuera del escroto",
  "PEDIATRÍA ENAM: ECTOPIA TESTICULAR", "PEDIATRÍA",
  ("Ectopia testicular", ["El testículo sale del trayecto normal de descenso",
   "Sitios: periné, muslo, pubis, base del pene"]),
  ("Lactante de 30 días", ["Escroto derecho vacío desde el nacimiento", "Masa ovoidea no dolorosa en el periné"]),
  {"rotulo": "¿Qué pasa con el testículo?", "ans": 0, "cards": [
      {"titulo": "ECTOPIA TESTICULAR", "datos": [
          ("Dónde", "Fuera del trayecto: periné", True), ("Al examen", "Palpable fuera del escroto", True),
          ("Conducta", "Orquidopexia", True)],
       "pie": "Periné, muslo, pubis"},
      {"titulo": "Criptorquidia", "datos": [
          ("Dónde", "En el trayecto inguinal", False), ("Al examen", "No baja al escroto", False),
          ("Conducta", "Orquidopexia 6-18 m", False)],
       "pie": "La más frecuente"},
      {"titulo": "Testículo retráctil", "datos": [
          ("Dónde", "Sube por el cremáster", False), ("Al examen", "Baja y se queda", False),
          ("Conducta", "Observar", False)],
       "pie": "Variante normal"},
      {"titulo": "Agenesia", "datos": [
          ("Dónde", "No existe", False), ("Al examen", "No se palpa", False),
          ("Conducta", "Imagen y laparoscopia", False)],
       "pie": "Descartar testículo abdominal"}]},
  ["El testículo ectópico no desciende solo: necesita cirugía.",
   "Orquidopexia antes de los 18 meses: protege la fertilidad.",
   "Testículo no descendido aumenta el riesgo de cáncer testicular."],
  "AUA – Evaluation and treatment of cryptorchidism (2014, act. 2018) · " + NELSON)

# NEU-028 · termómetro
V("termometro", "NEU-028", "asma-somnoliento-silencio-auscultatorio-intubacion", "Crisis de asma casi fatal",
  "NEUMOLOGÍA ENAM: ASMA CASI FATAL", "NEUMOLOGÍA",
  ("Crisis asmática con riesgo vital", ["Somnolencia, silencio auscultatorio y bradicardia",
   "Paro respiratorio inminente: intubación orotraqueal"]),
  ("Varón de 32 años con asma", ["Somnoliento, no puede hablar · SatO₂ 85%", "FC 62, FR 18 · silencio auscultatorio"]),
  {"rotulo": "Gravedad de la crisis",
   "niveles": [("Leve-mod.", "Habla frases", ["FR < 30, SatO₂ 90-95%"]),
               ("Grave", "Habla palabras", ["FR > 30, FC > 120, SatO₂ < 90%"]),
               ("Vital", "Somnoliento, confuso", ["Silencio, bradicardia"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "O₂ + salbutamol + ipratropio", ["Nebulizado o inhalador"], False),
             (2, "Corticoide sistémico + MgSO₄", ["En crisis grave"], False),
             (3, "INTUBACIÓN OROTRAQUEAL", ["Y ventilación mecánica"], True)]},
  ["FR y FC «normales» con somnolencia indican agotamiento, no mejoría.",
   "La VNI no se usa en paciente somnoliento.",
   "Ventilar con FR baja y espiración larga (evitar atrapamiento)."],
  "GINA – Global Strategy for Asthma Management and Prevention (2024)")

# CB-035 · puntaje
V("puntaje", "CB-035", "sobredosis-isoniazida-acidosis-piridoxina", "Intoxicación por isoniazida",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR ISONIAZIDA", "CIENCIAS BÁSICAS",
  ("Intoxicación por isoniazida", ["Agota la piridoxina y baja el GABA",
   "Tríada: convulsiones refractarias, acidosis metabólica y coma"]),
  ("Varón de 35 años en tratamiento de TB", ["Tomó varias dosis · confuso, Glasgow 12", "pH 7.22, HCO₃ 10 · hiperreflexia"]),
  {"rotulo": "Tríada tóxica en el caso", "escala": "Isoniazida", "total": 2, "max": 3,
   "total_label": "Elementos presentes",
   "interpreta": "Toxicidad por isoniazida",
   "items": [("Convulsiones refractarias", "1", False), ("Acidosis metabólica (HCO₃ 10)", "1", True),
             ("Alteración de la conciencia", "1", True)],
   "bandas": [("0-1", "Poco probable", "Buscar otra causa", False),
              ("≥ 2", "Intoxicación INH", "PIRIDOXINA EV: 1 g por cada g de INH", True)]},
  ["Si no se conoce la dosis: 5 g de piridoxina EV.",
   "Las benzodiacepinas funcionan mejor junto con la piridoxina.",
   "La piridoxina diaria (vitamina B6) previene la neuropatía por INH."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019) · MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis)")

# GAS-042 · árbol
A("GAS-042", "cirrotico-fiebre-dolor-confusion-paracentesis", "Cirrótico con fiebre y dolor abdominal",
  "GASTROENTEROLOGÍA ENAM: PARACENTESIS DIAGNÓSTICA", "GASTROENTEROLOGÍA",
  ("Paracentesis diagnóstica", ["Todo cirrótico con ascitis que empeora, tiene fiebre o encefalopatía",
   "Descarta peritonitis bacteriana espontánea"]),
  ("Varón de 60 años con cirrosis alcohólica", ["Fiebre 38.5 °C, confusión, asterixis", "Ascitis y dolor abdominal difuso"]),
  Q("¿Ascitis con fiebre, dolor o encefalopatía?", [
      L("No", "Control ambulatorio", ["Restricción de sodio y diuréticos"]),
      Q("PARACENTESIS DIAGNÓSTICA", [
          L("PMN ≥ 250", "PBE", ["Cefotaxima + albúmina"], path=True),
          L("PMN < 250", "Buscar otra causa", ["Cultivo del líquido"])],
        edge="Sí", path=True)], path=True),
  ("Estudio del líquido", [("Qué", True), ("Para qué", False)], [
      ("PMN", ["Recuento celular", "PBE si ≥ 250"]),
      ("Cultivo", ["En frascos de hemocultivo", "Germen"]),
      ("GASA", ["Albúmina sérica − ascítica", "≥ 1.1: hipertensión portal"])]),
  ["La coagulopatía no contraindica la paracentesis.",
   "No dar antiespasmódicos ni esperar: la PBE puede ser mortal.",
   "Varios gérmenes o proteínas altas: pensar en peritonitis secundaria."],
  "AASLD – Diagnosis, evaluation and management of ascites, SBP and HRS (Hepatology 2021)")

# PED-114 · matriz
V("matriz", "PED-114", "prematuro-1100-g-apnea-palidez-eco-transfontanelar", "Hemorragia intraventricular: estudio",
  "PEDIATRÍA ENAM: HEMORRAGIA INTRAVENTRICULAR", "PEDIATRÍA",
  ("Hemorragia intraventricular", ["Prematuros < 32 semanas en los primeros días de vida",
   "Se diagnostica con ecografía transfontanelar en la cuna"]),
  ("RN de 32 semanas y 1100 g", ["Asfixia al nacer (Apgar 3 y 7)", "A las 24 h: apnea y palidez marcada"]),
  {"rotulo": "Estudios posibles", "eje_x": "Aspecto", "eje_y": "Estudio",
   "cols": ["Ventaja", "Uso en el RN"], "rows": ["Eco transfontanelar", "TC cerebral", "RM cerebral", "Punción lumbar"], "caso": (0, 1),
   "cells": [[("En la cuna", ["Sin radiación"]), ("DE ELECCIÓN", ["Tamizaje < 32 sem"])],
             [("Rápida", ["Radiación, traslado"]), ("Poco usada", [])],
             [("Mayor detalle", ["Traslado, sedación"]), ("Pronóstico", ["A término corregido"])],
             [("LCR hemorrágico", []), ("No indicada", ["Riesgo en inestable"])]]},
  ["Clasificación de Papile: grados I a IV.",
   "Factores: prematuridad, asfixia, fluctuaciones de presión.",
   "Seguir con ecografías para detectar hidrocefalia."],
  NELSON + " · Volpe's Neurology of the Newborn 7.ª ed. (2024)")

# GAS-043 · termómetro
V("termometro", "GAS-043", "ictericia-8-dias-encefalopatia-falla-hepatica-aguda", "Falla hepática: clasificación temporal",
  "GASTROENTEROLOGÍA ENAM: FALLA HEPÁTICA AGUDA", "GASTROENTEROLOGÍA",
  ("Insuficiencia hepática aguda", ["Coagulopatía (INR ≥ 1.5) + encefalopatía sin hepatopatía previa",
   "Se clasifica por los días entre ictericia y encefalopatía (O'Grady)"]),
  ("Varón de 45 años con fiebre hace 2 semanas", ["Ictericia desde el día 6 · encefalopatía en 24 h", "Bilirrubina 19.6 · INR 6"]),
  {"rotulo": "Ictericia → encefalopatía",
   "niveles": [("≤ 7 días", "Hiperaguda", ["Paracetamol", "Mucho edema cerebral"]),
               ("8-28 días", "Aguda", ["Hepatitis viral"]),
               ("5-12 sem", "Subaguda", ["Peor pronóstico sin trasplante"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Contar los días", ["Ictericia a encefalopatía: ~ 8"], False),
             (2, "FALLA HEPÁTICA AGUDA", ["Entre 8 y 28 días"], True),
             (3, "UCI y centro de trasplante", ["Criterios del King's College"], False)]},
  ["La hiperaguda tiene más edema cerebral pero mejor sobrevida espontánea.",
   "Buscar la causa: virus, fármacos, autoinmune, Wilson.",
   "Vigilar glucosa: la hipoglucemia es frecuente."],
  "EASL – Clinical practice guidelines on acute liver failure (2017) · AASLD – Acute liver failure (2011, act. 2022)")

# GIN-104 · tarjetas
V("tarjetas", "GIN-104", "carbamazepina-anticonceptivo-oral-menos-efectivo", "Anticoncepción con carbamazepina",
  "GINECOLOGÍA ENAM: INTERACCIONES DE ANTICONCEPTIVOS", "GINECOLOGÍA",
  ("Inductores enzimáticos y anticoncepción", ["La carbamazepina induce el CYP3A4 y acelera la eliminación de las hormonas",
   "Los anticonceptivos orales combinados pierden eficacia"]),
  ("Mujer de 28 años con epilepsia", ["Usa carbamazepina", "Desea un método anticonceptivo"]),
  {"rotulo": "¿Qué método pierde eficacia?", "ans": 0, "cards": [
      {"titulo": "COMBINADOS ORALES", "datos": [
          ("Interacción", "Sí: CYP3A4", True), ("Eficacia", "Disminuye", True),
          ("Uso", "Evitar", True)],
       "pie": "Criterios OMS: categoría 3"},
      {"titulo": "AMPD trimestral", "datos": [
          ("Interacción", "Mínima", False), ("Eficacia", "Se mantiene", False),
          ("Uso", "Adecuado", False)],
       "pie": "Dosis alta de progestágeno"},
      {"titulo": "T de cobre", "datos": [
          ("Interacción", "No hormonal", False), ("Eficacia", "Se mantiene", False),
          ("Uso", "Muy adecuado", False)],
       "pie": "Dura 10-12 años"},
      {"titulo": "DIU con levonorgestrel", "datos": [
          ("Interacción", "Acción local", False), ("Eficacia", "Se mantiene", False),
          ("Uso", "Muy adecuado", False)],
       "pie": "Dura 5-8 años"}]},
  ["Implante y píldora de progestágeno también pierden eficacia con inductores.",
   "Otros inductores: fenitoína, fenobarbital, rifampicina.",
   "La lamotrigina baja sus niveles con los estrógenos."],
  "OMS – Criterios médicos de elegibilidad para el uso de anticonceptivos 5.ª ed. (2015) · MINSA – NTS N.° 124-2016 (Planificación familiar)")

# GAS-044 · árbol
A("GAS-044", "varices-grandes-profilaxis-primaria-betabloqueante", "Várices esofágicas: profilaxis primaria",
  "GASTROENTEROLOGÍA ENAM: VÁRICES ESOFÁGICAS", "GASTROENTEROLOGÍA",
  ("Profilaxis primaria de sangrado variceal", ["Várices grandes que nunca sangraron",
   "Betabloqueante no cardioselectivo o ligadura endoscópica"]),
  ("Varón de 62 años, alcohólico", ["Endoscopia: várices esofágicas grandes", "Lúcido, sin ascitis ni asterixis"]),
  Q("¿Várices grandes o con signos rojos?", [
      L("No, pequeñas", "Vigilancia", ["Endoscopia cada 1-2 años"]),
      Q("¿Tolera betabloqueante?", [
          L("Sí", "BETABLOQUEANTE NO CARDIOSELECTIVO", ["Propranolol, nadolol o carvedilol"], path=True),
          L("No", "Ligadura endoscópica", ["Cada 2-4 semanas"])],
        edge="Sí", path=True)], path=True),
  ("Profilaxis vs sangrado agudo", [("Profilaxis primaria", True), ("Sangrado agudo", False)], [
      ("Fármaco", ["Propranolol, carvedilol", "Octreotida o terlipresina"]),
      ("Endoscopia", ["Ligadura si no tolera", "Ligadura en < 12 h"]),
      ("Antibiótico", ["No", "Ceftriaxona profiláctica"])]),
  ["Meta del betabloqueante: FC ~ 55-60 por minuto.",
   "La somatostatina es para el sangrado agudo, no para prevenir.",
   "El TIPS se reserva para sangrado refractario o de alto riesgo."],
  "Baveno VII – Renewing consensus in portal hypertension (J Hepatol 2022) · AASLD – Portal hypertensive bleeding (2017)")

# REU-031 · embudo
V("embudo", "REU-031", "debilidad-proximal-simetrica-sin-piel-polimiositis", "Debilidad proximal progresiva",
  "REUMATOLOGÍA ENAM: POLIMIOSITIS", "REUMATOLOGÍA",
  ("Polimiositis", ["Miopatía inflamatoria: debilidad proximal simétrica, progresiva",
   "Sin lesiones cutáneas (si las hay: dermatomiositis)"]),
  ("Mujer de 50 años con 6 meses de debilidad", ["Le cuesta subir escaleras, levantarse y peinarse", "Sin artralgias ni lesiones de piel"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Debilidad de cinturas de 6 meses",
   "candidatos": ["Polimiositis", "Dermatomiositis", "Miastenia gravis", "Guillain-Barré", "Mielitis"],
   "pasos": [("6 meses de evolución progresiva", ["Guillain-Barré"]),
             ("Sin nivel sensitivo ni esfínteres", ["Mielitis"]),
             ("Sin lesiones cutáneas ni fatigabilidad", ["Dermatomiositis", "Miastenia gravis"])],
   "final": ("POLIMIOSITIS", ["Debilidad proximal simétrica", "Pedir CPK, EMG y biopsia"]),
   "nota": "Buscar cáncer asociado y enfermedad pulmonar intersticial (anti-Jo-1)."},
  ["Tratamiento: corticoides + metotrexato o azatioprina.",
   "La CPK suele estar muy elevada.",
   "Miastenia: ptosis, diplopía y debilidad que empeora con el esfuerzo."],
  "EULAR/ACR – Classification criteria for idiopathic inflammatory myopathies (2017) · " + HARRISON)

# GIN-105 · árbol
A("GIN-105", "metildopa-desde-8-semanas-pa-controlada-hta-cronica", "Hipertensión en la gestante",
  "OBSTETRICIA ENAM: HIPERTENSIÓN CRÓNICA", "OBSTETRICIA",
  ("Hipertensión crónica en el embarazo", ["HTA previa o diagnosticada antes de las 20 semanas",
   "Si aparece proteinuria o daño de órgano: preeclampsia sobreagregada"]),
  ("Tercigesta de 36 semanas", ["Metildopa desde las 8 semanas, bien controlada", "Cefalea tras una discusión · PA 130/80"]),
  Q("¿HTA antes de las 20 semanas?", [
      Q("¿Proteinuria o daño de órgano nuevo?", [
          L("Sí", "Preeclampsia sobreagregada", ["Hospitalizar"]),
          L("No", "HIPERTENSIÓN CRÓNICA", ["Continuar metildopa"], path=True)],
        edge="Sí", path=True),
      Q("¿Proteinuria o daño de órgano?", [
          L("Sí", "Preeclampsia", []),
          L("No", "HTA gestacional", [])],
        edge="No, después")], path=True),
  ("Trastornos hipertensivos", [("Inicio", True), ("Proteinuria o daño", False)], [
      ("HTA crónica", ["Previa o < 20 sem", "No"]),
      ("Gestacional", ["≥ 20 semanas", "No"]),
      ("Preeclampsia", ["≥ 20 semanas", "Sí"])]),
  ["La cefalea aislada con PA normal no hace preeclampsia.",
   "Preeclampsia severa: PA ≥ 160/110 o daño de órgano.",
   "Antihipertensivos seguros: metildopa, nifedipino, labetalol."],
  "ACOG – Practice Bulletin N.° 203: Chronic hypertension in pregnancy (2019) · " + WILLIAMS)

# NEU-029 · termómetro
V("termometro", "NEU-029", "epoc-exacerbado-ph-708-confusion-intubacion", "Exacerbación de EPOC con acidosis",
  "NEUMOLOGÍA ENAM: EXACERBACIÓN DE EPOC", "NEUMOLOGÍA",
  ("Exacerbación de EPOC", ["La acidosis respiratoria guía el soporte ventilatorio",
   "pH < 7.25 con confusión: intubación orotraqueal"]),
  ("Varón de 63 años con bronquitis crónica", ["Esputo purulento, disnea y confusión", "pH 7.08, PaCO₂ 60, PaO₂ 50"]),
  {"rotulo": "Según el pH arterial",
   "niveles": [("≥ 7.35", "Sin acidosis", ["O₂ controlado"]),
               ("7.25-7.34", "Acidosis moderada", ["VNI de elección"]),
               ("< 7.25", "Acidosis grave", ["Con confusión: intubar"])],
   "caso_nivel": 2, "ruta_titulo": "Soporte ventilatorio", "paso_label": "PASO",
   "pasos": [(1, "O₂ controlado", ["SatO₂ 88-92%, Venturi"], False),
             (2, "Ventilación no invasiva", ["pH 7.25-7.35"], False),
             (3, "INTUBACIÓN OROTRAQUEAL", ["pH < 7.25 y confusión"], True)]},
  ["El oxígeno a alto flujo puede empeorar la hipercapnia.",
   "Además: broncodilatadores, corticoide y antibiótico (esputo purulento).",
   "El diazepam deprime la respiración."],
  "GOLD – Global Strategy for COPD (2025) · ERS/ATS – Noninvasive ventilation for acute respiratory failure (2017)")

# CIR-059 · embudo
V("embudo", "CIR-059", "anciana-masa-bajo-pliegue-inguinal-obstruccion-femoral", "Obstrucción intestinal con masa inguinal",
  "CIRUGÍA ENAM: HERNIA FEMORAL ESTRANGULADA", "CIRUGÍA",
  ("Hernia femoral", ["Por debajo del ligamento inguinal, medial a la vena femoral",
   "Más frecuente en mujeres mayores; es la que más se estrangula"]),
  ("Mujer de 74 años con 1 día de dolor y vómitos", ["Sin flatos · masa dolorosa bajo el pliegue inguinal", "Rx: «pila de monedas», sin gas en el recto"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Obstrucción intestinal con masa en la ingle",
   "candidatos": ["Hernia femoral", "Hernia inguinal", "Eventración", "Íleo adinámico", "Adenopatía inguinal"],
   "pasos": [("Obstrucción mecánica: sin gas en el recto", ["Íleo adinámico", "Adenopatía inguinal"]),
             ("Masa por debajo del pliegue inguinal", ["Hernia inguinal"]),
             ("Lejos de la cicatriz de la cesárea", ["Eventración"])],
   "final": ("HERNIA FEMORAL ESTRANGULADA", ["Cuello estrecho", "Cirugía urgente"]),
   "nota": "La hernia femoral se opera siempre, aun asintomática, por su alto riesgo de estrangulación."},
  ["La hernia inguinal está por encima del ligamento inguinal.",
   "En la cirugía, revisar la viabilidad del asa y resecar si está necrótica.",
   "Signos de estrangulación: dolor intenso, fiebre, leucocitosis."],
  "HerniaSurge – International guidelines for groin hernia management (Hernia 2018, act. 2023) · Sabiston Textbook of Surgery 21.ª ed. (2021)")

# PED-115 · fases
V("fases", "PED-115", "fiebre-tos-coriza-conjuntivitis-koplik-sarampion", "Sarampión: etapas",
  "PEDIATRÍA ENAM: SARAMPIÓN", "PEDIATRÍA",
  ("Sarampión", ["Pródromo con tos, coriza y conjuntivitis («3 C»)",
   "Manchas de Koplik antes del exantema maculopapular cefalocaudal"]),
  ("Niño de 5 años con fiebre, tos y coriza", ["Fotofobia, conjuntivas rojas", "Exantema generalizado · manchas blancas en mejillas"]),
  {"rotulo": "Curso de la enfermedad", "ans": 2,
   "fases": [("Incubación", "10-12 días", "Sin síntomas", ["Ya contagia al final"]),
             ("Pródromo", "3-4 días", "Fiebre y «3 C»", ["Tos, coriza, conjuntivitis"]),
             ("Exantema", "Día 4-5", "EXANTEMA + KOPLIK", ["Cefalocaudal, confluente"]),
             ("Resolución", "1 semana", "Descamación fina", ["Riesgo de neumonía"])],
   "curvas": [("Fiebre", ROSE, [0.1, 0.5, 0.7, 0.95, 0.8, 0.4, 0.15]),
              ("Exantema", AMBER, [0.0, 0.0, 0.1, 0.8, 0.95, 0.5, 0.1])],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Sarampión", True), ("Kawasaki", False), ("Varicela", False), ("Eritema infeccioso", False)]},
  ["Notificación inmediata: enfermedad en eliminación.",
   "Vitamina A a todo niño con sarampión.",
   "Complicación más frecuente de muerte: neumonía."],
  "MINSA – NTS de vigilancia de sarampión y rubéola · OMS – Measles fact sheet (2024) · " + NELSON)

# NRL-030 · matriz
V("matriz", "NRL-030", "anciana-deja-cocina-prendida-deambula-alzheimer", "Tipos de demencia",
  "NEUROLOGÍA ENAM: ENFERMEDAD DE ALZHEIMER", "NEUROLOGÍA",
  ("Enfermedad de Alzheimer", ["La demencia más frecuente: empieza con fallas de memoria reciente",
   "Luego desorientación, deambulación y cambios de conducta"]),
  ("Mujer de 73 años traída por su hija", ["Deja la cocina prendida, no reconoce a familiares", "Deambula sin rumbo · cambios del ánimo"]),
  {"rotulo": "Rasgos de cada demencia", "eje_x": "Rasgo", "eje_y": "Demencia",
   "cols": ["Primer síntoma", "Otros datos"], "rows": ["Alzheimer", "Cuerpos de Lewy", "Frontotemporal", "Huntington"], "caso": (0, 0),
   "cells": [[("MEMORIA", ["Olvidos, se pierde"]), ("> 65 años", ["Progresión lenta"])],
             [("Fluctuaciones", ["Alucinaciones visuales"]), ("Parkinsonismo", ["Sensible a neurolépticos"])],
             [("Conducta", ["Desinhibición, apatía"]), ("< 65 años", ["Memoria respetada al inicio"])],
             [("Corea", ["Autosómica dominante"]), ("30-50 años", ["Repeticiones CAG"])]]},
  ["Tratamiento: inhibidores de colinesterasa (donepezilo) y memantina.",
   "Descartar causas reversibles: hipotiroidismo, déficit de B12, depresión.",
   "Asesorar a la familia sobre seguridad en casa."],
  "NIA-AA – Revised criteria for diagnosis and staging of Alzheimer's disease (2024) · " + HARRISON)

# CAR-044 · matriz
V("matriz", "CAR-044", "paro-piscina-dea-descarga-fibrilacion-ventricular", "Ritmos de paro cardiaco",
  "CARDIOLOGÍA ENAM: FIBRILACIÓN VENTRICULAR", "CARDIOLOGÍA",
  ("Ritmos desfibrilables", ["Fibrilación ventricular y TV sin pulso responden a la descarga",
   "Si el DEA descargó y volvió el pulso: era FV (o TV sin pulso)"]),
  ("Mujer de 50 años en clase de natación", ["Paro cardiaco, RCP por el instructor", "DEA: descarga y retorno de la circulación"]),
  {"rotulo": "Ritmos de paro", "eje_x": "Aspecto", "eje_y": "Ritmo",
   "cols": ["¿Desfibrilable?", "Tratamiento"], "rows": ["FV", "TV sin pulso", "Asistolia", "AESP"], "caso": (0, 0),
   "cells": [[("SÍ", ["Ritmo caótico"]), ("Descarga + RCP", ["Adrenalina tras la 2.ª descarga"])],
             [("Sí", []), ("Descarga + RCP", ["Amiodarona tras la 3.ª"])],
             [("No", ["Línea plana"]), ("RCP + adrenalina", ["Lo antes posible"])],
             [("No", ["Actividad sin pulso"]), ("RCP + adrenalina", ["Buscar 5H y 5T"])]]},
  ["La FV es el ritmo inicial más frecuente del paro súbito del adulto.",
   "Cada minuto sin desfibrilar baja la sobrevida ~ 10%.",
   "La fibrilación auricular no causa paro por sí sola."],
  "AHA – Guidelines for CPR and ECC (2020, act. 2025) · ERC – Guidelines (2025)")

# SP-076 · radial
V("radial", "SP-076", "director-comite-distrital-dengue-liderazgo-democratico", "Estilos de liderazgo",
  "SALUD PÚBLICA ENAM: LIDERAZGO DEMOCRÁTICO", "SALUD PÚBLICA",
  ("Liderazgo democrático", ["El líder informa, consulta y reparte responsabilidades",
   "Cada integrante asume tareas según sus funciones"]),
  ("Director de un ámbito sanitario", ["Presenta al comité el aumento de dengue", "Pide que cada integrante asuma responsabilidades"]),
  {"rotulo": "Mapa del tema", "centro": "LIDERAZGO", "centro_sub": "Estilos", "ans": 0,
   "items": [("DEMOCRÁTICO", ["Comparte decisiones", "Delega según funciones"]),
             ("Autocrático", ["Decide solo"]),
             ("Liberal", ["Deja hacer"]),
             ("Paternalista", ["Decide «por el bien» de otros"]),
             ("Situacional", ["Se adapta al grupo"])],
   "ruta": ["Presenta el problema", "Expone actividades", "Cada uno asume su rol", "DEMOCRÁTICO"]},
  ["El autocrático sirve en emergencias que exigen decisiones rápidas.",
   "El liberal (laissez-faire) delega todo y no conduce.",
   "El comité distrital es un espacio de trabajo intersectorial."],
  "OPS – Liderazgo en salud pública · MINSA – Documento técnico de gestión en salud")

# NRL-031 · embudo
V("embudo", "NRL-031", "espasmos-mano-al-escribir-distonia-focal", "Espasmos de la mano al escribir",
  "NEUROLOGÍA ENAM: DISTONÍA FOCAL", "NEUROLOGÍA",
  ("Distonía focal de tarea específica", ["Contracciones involuntarias que aparecen al hacer una tarea",
   "Calambre del escribiente: solo al escribir; empeora con ansiedad"]),
  ("Varón de 49 años con 1 año de síntomas", ["Dificultad para sostener el lápiz", "Espasmos de mano y antebrazo solo al escribir"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Espasmos de la mano al escribir",
   "candidatos": ["Distonía focal", "Temblor esencial", "Parkinson", "Túnel carpiano", "De Quervain"],
   "pasos": [("Espasmos solo al escribir: tarea específica", ["Temblor esencial", "Parkinson"]),
             ("Sin parestesias nocturnas ni Tinel", ["Túnel carpiano"]),
             ("Sin dolor en el borde radial de la muñeca", ["De Quervain"])],
   "final": ("DISTONÍA FOCAL", ["Calambre del escribiente", "Toxina botulínica"]),
   "nota": "Empeora con el estrés y mejora con «trucos sensitivos»."},
  ["El examen neurológico en reposo es normal.",
   "Temblor esencial: temblor postural y de acción, mejora con alcohol.",
   "Toxina botulínica en los músculos afectados: tratamiento de elección."],
  "MDS – Consensus update on the phenomenology and classification of dystonia (2013) · Adams and Victor's Principles of Neurology 12.ª ed. (2023)")

# CB-036 · fases
V("fases", "CB-036", "lima-puno-cefalea-nauseas-alcalosis-respiratoria", "Adaptación a la altura",
  "CIENCIAS BÁSICAS ENAM: FISIOLOGÍA DE LA ALTURA", "CIENCIAS BÁSICAS",
  ("Adaptación a la altura", ["La hipoxia estimula la hiperventilación",
   "Baja la PaCO₂: alcalosis respiratoria, luego compensada por el riñón"]),
  ("Varón de 45 años de Lima que viaja a Puno", ["Al llegar: cefalea, fatiga", "Náuseas y vómitos"]),
  {"rotulo": "Aclimatación", "ans": 0,
   "fases": [("Llegada", "Horas", "HIPERVENTILACIÓN", ["Alcalosis respiratoria"]),
             ("Compensa", "2-3 días", "Riñón elimina HCO₃⁻", ["El pH se normaliza"]),
             ("Aclimata", "Semanas", "↑ Eritropoyetina", ["Poliglobulia"])],
   "curvas": [("pH", ROSE, [0.5, 0.9, 0.85, 0.7, 0.6, 0.55, 0.5]),
              ("PaCO₂", SKY, [0.7, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])],
   "chips_titulo": "Gasometría · marcada la correcta",
   "chips": [("Alcalosis respiratoria", True), ("Acidosis respiratoria", False), ("Acidosis metabólica", False), ("Alcalosis metabólica", False)]},
  ["Mal de altura agudo: cefalea + náuseas, fatiga o mareo.",
   "Acetazolamida: acelera la compensación (acidosis metabólica).",
   "Signos graves: edema pulmonar o cerebral de altura: descender."],
  "Guyton y Hall – Tratado de fisiología médica 14.ª ed. (2021) · Wilderness Medical Society – Acute altitude illness (2024)")

# SP-077 · fases
V("fases", "SP-077", "porcentaje-tb-visita-domiciliaria-indicador-proceso", "Tipos de indicadores",
  "SALUD PÚBLICA ENAM: INDICADORES DE PROCESO", "SALUD PÚBLICA",
  ("Indicadores de gestión (Donabedian)", ["Estructura → proceso → resultado → impacto",
   "Proceso: mide las actividades que se realizan"]),
  ("Informe de los jefes de centros de salud", ["Porcentaje de personas con TB", "que recibieron visita domiciliaria"]),
  {"rotulo": "Cadena de indicadores", "ans": 1,
   "fases": [("Estructura", "Recursos", "Personal, insumos", ["Lo que se tiene"]),
             ("Proceso", "Actividades", "% TB CON VISITA", ["Lo que se hace"]),
             ("Resultado", "Corto plazo", "Curación, adherencia", ["Lo que se logra"]),
             ("Impacto", "Largo plazo", "↓ Incidencia y muertes", ["Cambio en la población"])],
   "curvas": [],
   "chips_titulo": "Tipo de indicador · marcado el correcto",
   "chips": [("Proceso", True), ("Resultado", False), ("Impacto", False), ("Estructura", False)]},
  ["Visitas, controles y consejerías realizadas: proceso.",
   "Tasa de curación o abandono: resultado.",
   "Reducción de la incidencia o mortalidad: impacto."],
  "Donabedian – Evaluating the quality of medical care (1966, reed. 2005) · MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis)")

# CB-037 · radial
V("radial", "CB-037", "hbp-simpaticolitico-hipotension-ortostatica-alfa1", "Receptores adrenérgicos",
  "CIENCIAS BÁSICAS ENAM: BLOQUEADORES ALFA-1", "CIENCIAS BÁSICAS",
  ("Bloqueadores alfa-1", ["Relajan el músculo liso de la próstata y de los vasos",
   "Efecto adverso típico: hipotensión ortostática (primera dosis)"]),
  ("Varón de 65 años con HBP", ["Toma un simpaticolítico", "Presenta hipotensión ortostática"]),
  {"rotulo": "Mapa del tema", "centro": "RECEPTORES", "centro_sub": "Adrenérgicos", "ans": 0,
   "items": [("ALFA-1", ["Vasoconstricción, próstata", "Bloqueo: hipotensión ortostática"]),
             ("Alfa-2", ["Inhibe la liberación de NA"]),
             ("Beta-1", ["Corazón: FC y contractilidad"]),
             ("Beta-2", ["Broncodilatación"]),
             ("Beta-3", ["Lipólisis, relaja la vejiga"])],
   "ruta": ["HBP", "Tamsulosina o doxazosina", "Vasodilatación", "BLOQUEO ALFA-1"]},
  ["Dar la primera dosis en la noche, acostado.",
   "Tamsulosina es más selectiva (α-1A): menos hipotensión.",
   "Precaución en cirugía de catarata: iris flácido."],
  GOODMAN)

# GIN-106 · puntaje
V("puntaje", "GIN-106", "imc-34-macrosomia-familiar-dm-tamizaje-inmediato", "Tamizaje temprano de diabetes en la gestante",
  "OBSTETRICIA ENAM: TAMIZAJE DE DIABETES", "OBSTETRICIA",
  ("Tamizaje de diabetes en el embarazo", ["Alto riesgo: glucosa en la primera consulta",
   "Riesgo habitual: a las 24-28 semanas"]),
  ("Multigesta de 10 semanas, primer control", ["IMC 34 · hijo previo de 4700 g", "Hermana con diabetes tipo 2"]),
  {"rotulo": "Factores de riesgo en el caso", "escala": "Riesgo de diabetes", "total": 3, "max": 5,
   "total_label": "Factores presentes",
   "interpreta": "Alto riesgo: tamizaje inmediato",
   "items": [("IMC ≥ 30", "1", True), ("Hijo previo ≥ 4000 g", "1", True),
             ("Familiar de 1.er grado con DM2", "1", True), ("Diabetes gestacional previa", "1", False),
             ("SOP o hipertensión", "1", False)],
   "bandas": [("0", "Riesgo habitual", "Tamizaje a las 24-28 semanas", False),
              ("≥ 1", "Alto riesgo", "Glucosa en la 1.ª consulta: INMEDIATAMENTE", True)]},
  ["Glucosa en ayunas ≥ 126 o HbA1c ≥ 6.5% al inicio: diabetes pregestacional.",
   "Si el tamizaje temprano es normal, repetir a las 24-28 semanas.",
   "PTOG de 75 g: ayunas ≥ 92, 1 h ≥ 180, 2 h ≥ 153 mg/dL."],
  "ADA – Standards of Care in Diabetes: Diabetes in pregnancy (2025) · ACOG – Practice Bulletin N.° 190 (2018)")

# GIN-107 · tarjetas
V("tarjetas", "GIN-107", "amenorrea-19-anos-fsh-lh-altas-falla-ovarica", "Amenorrea secundaria: ¿dónde falla?",
  "GINECOLOGÍA ENAM: INSUFICIENCIA OVÁRICA PREMATURA", "GINECOLOGÍA",
  ("Insuficiencia ovárica prematura", ["Pérdida de la función ovárica antes de los 40 años",
   "FSH y LH altas con estrógenos bajos (hipogonadismo hipergonadotrópico)"]),
  ("Mujer de 19 años con 7 meses de amenorrea", ["Caracteres sexuales presentes · útero y ovarios", "FSH y LH elevadas"]),
  {"rotulo": "¿Dónde está la falla?", "ans": 0, "cards": [
      {"titulo": "FALLA OVÁRICA PREMATURA", "datos": [
          ("FSH/LH", "Altas", True), ("Estrógenos", "Bajos", True),
          ("Clave", "Menor de 40 años", True)],
       "pie": "Pedir cariotipo y X frágil"},
      {"titulo": "Amenorrea hipotalámica", "datos": [
          ("FSH/LH", "Bajas", False), ("Estrógenos", "Bajos", False),
          ("Clave", "Estrés, ejercicio, bajo peso", False)],
       "pie": "Funcional, reversible"},
      {"titulo": "Amenorrea hipofisaria", "datos": [
          ("FSH/LH", "Bajas", False), ("Estrógenos", "Bajos", False),
          ("Clave", "Tumor, Sheehan", False)],
       "pie": "RM de silla turca"},
      {"titulo": "Ovario poliquístico", "datos": [
          ("FSH/LH", "LH alta, FSH normal", False), ("Estrógenos", "Normales", False),
          ("Clave", "Hiperandrogenismo", False)],
       "pie": "Ovarios multifoliculares"}]},
  ["Confirmar con FSH > 25 UI/L en dos mediciones separadas por 4 semanas.",
   "Tratamiento: terapia hormonal hasta la edad de la menopausia.",
   "Riesgo de osteoporosis y enfermedad cardiovascular."],
  "ESHRE – Guideline: Management of premature ovarian insufficiency (2024)")

# PED-116 · termómetro
V("termometro", "PED-116", "rn-apnea-fc-90-vpp-aire-ambiente", "Reanimación neonatal",
  "PEDIATRÍA ENAM: REANIMACIÓN NEONATAL", "PEDIATRÍA",
  ("Reanimación neonatal", ["Tras los pasos iniciales, si hay apnea o FC < 100: VPP",
   "En el RN a término se inicia con aire ambiente (FiO₂ 21%)"]),
  ("RN a término que no llora ni respira", ["Hipotónico", "Tras los pasos iniciales: apnea y FC 90"]),
  {"rotulo": "Según la frecuencia cardiaca",
   "niveles": [("FC > 100", "Respira bien", ["Cuidados de rutina"]),
               ("FC < 100", "Apnea o boqueo", ["Ventilar"]),
               ("FC < 60", "Tras 30 s de VPP eficaz", ["Compresiones + O₂ 100%"])],
   "caso_nivel": 1, "ruta_titulo": "Secuencia", "paso_label": "PASO",
   "pasos": [(1, "Pasos iniciales", ["Calentar, secar, estimular, posicionar"], False),
             (2, "VPP CON FiO₂ 21%", ["En el primer minuto de vida"], True),
             (3, "Compresiones si FC < 60", ["3:1 con O₂ al 100%"], False)]},
  ["Prematuros < 35 semanas: iniciar con FiO₂ 21-30%.",
   "La VPP eficaz es la intervención más importante.",
   "Oxígeno a flujo libre solo si respira pero con cianosis persistente."],
  "AAP/AHA – Neonatal Resuscitation Program 8.ª ed. (2021) · ILCOR – CoSTR neonatal (2025)")

# GIN-108 · embudo
V("embudo", "GIN-108", "prolapso-total-lesion-vaginal-ulcera-decubito", "Lesión vaginal en prolapso total",
  "GINECOLOGÍA ENAM: ÚLCERA DE DECÚBITO", "GINECOLOGÍA",
  ("Úlcera de decúbito vaginal", ["En el prolapso total la mucosa atrófica roza y se ulcera",
   "Bordes regulares, sangrado escaso"]),
  ("Mujer de 65 años con prolapso genital total", ["Lesión vaginal de 2 cm, bordes regulares", "Endometrio de 2 mm · PAP negativo"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Lesión vaginal en prolapso total",
   "candidatos": ["Úlcera de decúbito", "Ca de cérvix", "Ca de endometrio", "Cervicitis crónica", "Ca de vagina"],
   "pasos": [("Endometrio de 2 mm, atrófico", ["Ca de endometrio"]),
             ("PAP negativo", ["Ca de cérvix", "Cervicitis crónica"]),
             ("Bordes regulares en la zona de roce", ["Ca de vagina"])],
   "final": ("ÚLCERA DE DECÚBITO", ["Por roce y atrofia", "Estrógenos locales y reducir"]),
   "nota": "Si no cicatriza con estrógenos y reducción del prolapso: biopsia."},
  ["Tratamiento: estrógeno vaginal y pesario o reducción.",
   "Luego corrección quirúrgica del prolapso.",
   "Bordes irregulares o indurados: sospechar cáncer."],
  "ACOG – Practice Bulletin N.° 214: Pelvic organ prolapse (2019) · Williams Gynecology 4.ª ed. (2020)")

# CB-038 · radial
V("radial", "CB-038", "asmatico-ipratropio-retencion-urinaria", "Efectos de los antimuscarínicos",
  "CIENCIAS BÁSICAS ENAM: EFECTOS DEL IPRATROPIO", "CIENCIAS BÁSICAS",
  ("Bromuro de ipratropio", ["Antagonista muscarínico: broncodilata",
   "En ancianos con HBP puede causar retención urinaria"]),
  ("Varón de 70 años con asma en tratamiento", ["Retención urinaria brusca", "¿Qué fármaco la causa?"]),
  {"rotulo": "Mapa del tema", "centro": "ANTIMUSCARÍNICOS", "centro_sub": "Efectos adversos", "ans": 0,
   "items": [("RETENCIÓN URINARIA", ["Relaja el detrusor", "Riesgo en HBP"]),
             ("Boca seca", ["Menos saliva"]),
             ("Glaucoma agudo", ["Ángulo cerrado"]),
             ("Visión borrosa", ["Midriasis, cicloplejía"]),
             ("Estreñimiento", ["Menor motilidad"])],
   "ruta": ["Asmático de 70 años", "Bromuro de ipratropio", "Bloqueo muscarínico", "RETENCIÓN URINARIA"]},
  ["Fenoterol (β2): temblor, taquicardia, hipopotasemia.",
   "Fluticasona inhalada: candidiasis oral y disfonía.",
   "Prednisona: hiperglucemia, osteoporosis."],
  GOODMAN)

# SP-078 · árbol
A("SP-078", "temperatura-ambiental-variable-continua", "Tipos de variables",
  "SALUD PÚBLICA ENAM: VARIABLES", "SALUD PÚBLICA",
  ("Variable cuantitativa continua", ["Puede tomar cualquier valor, con decimales, entre dos números",
   "Ej.: temperatura, peso, talla, presión arterial"]),
  ("Pregunta de concepto", ["Variable «temperatura ambiental»", "¿Qué tipo es?"]),
  Q("¿Se expresa con números?", [
      Q("¿Admite decimales entre dos valores?", [
          L("Sí", "CONTINUA", ["Temperatura, peso, talla"], path=True),
          L("No, solo enteros", "Discreta", ["N.° de hijos"])],
        edge="Sí: cuantitativa", path=True),
      Q("¿Tiene orden?", [
          L("Sí", "Ordinal", ["Estadio, grado"]),
          L("No", "Nominal", ["Sexo, grupo sanguíneo"])],
        edge="No: cualitativa")], path=True),
  ("Tipos de variable", [("Cuantitativa", True), ("Cualitativa", False)], [
      ("Ejemplo 1", ["Continua: temperatura", "Nominal: sexo"]),
      ("Ejemplo 2", ["Discreta: n.° de hijos", "Ordinal: estadio"])]),
  ["Cualitativa = categórica.",
   "Continua: se resume con media o mediana.",
   "Discreta: conteos."],
  "Hernández-Sampieri – Metodología de la investigación 7.ª ed. (2023) · Dawson-Trapp – Bioestadística médica")

# OFT-026 · fases
V("fases", "OFT-026", "timpano-perforado-otorrea-fetida-otitis-media-cronica", "Otitis media según el tiempo",
  "OTORRINOLARINGOLOGÍA ENAM: OTITIS MEDIA CRÓNICA", "OTORRINOLARINGOLOGÍA",
  ("Otitis media crónica", ["Perforación timpánica con otorrea de más de 12 semanas",
   "Hipoacusia de conducción: bajo rendimiento escolar"]),
  ("Niño de 6 años con bajo rendimiento escolar", ["Pobre ganancia de peso y talla", "Tímpano perforado · otorrea maloliente"]),
  {"rotulo": "Evolución de la otitis media", "ans": 2,
   "fases": [("Aguda", "< 3 sem", "Tímpano abombado", ["Otalgia, fiebre"]),
             ("Subaguda", "3-12 sem", "Efusión persistente", ["Hipoacusia"]),
             ("Crónica", "> 12 sem", "PERFORACIÓN + OTORREA", ["Otorrea maloliente"]),
             ("Complicada", "Variable", "Colesteatoma", ["Mastoiditis, absceso"])],
   "curvas": [],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Otitis media crónica", True), ("Otitis media aguda", False), ("Mastoiditis", False), ("Cuerpo extraño", False)]},
  ["Tratamiento: limpieza y gotas de quinolona; cirugía (timpanoplastia).",
   "Otorrea fétida persistente: descartar colesteatoma.",
   "Evaluar audición: la hipoacusia afecta el aprendizaje."],
  "WHO – Chronic suppurative otitis media: burden of illness (2004) · Cummings Otolaryngology 7.ª ed. (2021)")

# NEF-041 · puntaje
V("puntaje", "NEF-041", "mujer-joven-hta-refractaria-soplo-flanco-estenosis-renal", "Sospecha de HTA renovascular",
  "NEFROLOGÍA ENAM: ESTENOSIS DE LA ARTERIA RENAL", "NEFROLOGÍA",
  ("Hipertensión renovascular", ["Estenosis de la arteria renal que activa el eje renina-angiotensina",
   "Mujer joven: displasia fibromuscular · mayor: aterosclerosis"]),
  ("Mujer de 28 años con HTA de inicio súbito", ["PA 190/100 refractaria a 3 fármacos", "Soplo en el flanco derecho"]),
  {"rotulo": "Pistas clínicas en el caso", "escala": "HTA renovascular", "total": 3, "max": 5,
   "total_label": "Pistas presentes",
   "interpreta": "Alta sospecha de estenosis de la arteria renal",
   "items": [("Inicio < 30 años o > 55 años", "1", True), ("Resistente a 3 fármacos", "1", True),
             ("Soplo abdominal o en flanco", "1", True), ("Creatinina sube con IECA o ARA II", "1", False),
             ("Edema pulmonar súbito", "1", False)],
   "bandas": [("0", "Baja", "HTA esencial probable", False),
              ("1-2", "Sospecha", "Doppler de arterias renales", False),
              ("≥ 3", "Alta sospecha", "Angio-TC o angio-RM; angioplastia si es fibromuscular", True)]},
  ["Displasia fibromuscular: imagen en «collar de cuentas».",
   "Coartación: diferencia de PA entre brazos y piernas.",
   "Feocromocitoma: crisis de cefalea, sudoración y palpitaciones."],
  "AHA – Resistant hypertension: detection, evaluation and management (2018) · ESC/ESH – Hypertension guidelines (2023)")

# CIR-060 · termómetro
V("termometro", "CIR-060", "accidente-transito-choque-abdomen-doloroso-fast", "Trauma abdominal con choque",
  "CIRUGÍA ENAM: ECOGRAFÍA FAST", "CIRUGÍA",
  ("Trauma abdominal cerrado inestable", ["Choque sin causa torácica: buscar sangre en el abdomen",
   "Estudio inicial en la sala de trauma: ecografía FAST"]),
  ("Mujer de 18 años, accidente hace 30 minutos", ["Agitada, taquicárdica, sudor frío, pulsos débiles", "Pulmones normales · abdomen doloroso"]),
  {"rotulo": "Clase de choque hemorrágico",
   "niveles": [("< 15%", "Clase I", ["Signos normales"]),
               ("15-30%", "Clase II", ["Taquicardia, ansiedad"]),
               ("31-40%", "Clase III", ["PA baja, confusión, sudor frío"]),
               ("> 40%", "Clase IV", ["Letargo, pulsos ausentes"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "ABC + 2 vías + sangre", ["Reanimación de control de daños"], False),
             (2, "ECOGRAFÍA FAST", ["En la sala de trauma"], True),
             (3, "FAST (+): laparotomía", ["Inestable: no ir a la TEM"], False)]},
  ["La TEM solo en pacientes estables.",
   "FAST evalúa Morison, esplenorrenal, pelvis y pericardio.",
   "Rx de abdomen y RM no tienen lugar en el trauma inestable."],
  ATLS)

# PED-117 · radial
V("radial", "PED-117", "membrana-hialina-diabetes-materna", "Enfermedad de membrana hialina",
  "PEDIATRÍA ENAM: MEMBRANA HIALINA", "PEDIATRÍA",
  ("Enfermedad de membrana hialina", ["Déficit de surfactante en el pretérmino",
   "La hiperinsulinemia fetal (madre diabética) retrasa su producción"]),
  ("Pregunta de concepto", ["Antecedente que aumenta el riesgo", "de membrana hialina en el pretérmino"]),
  {"rotulo": "Mapa del tema", "centro": "MEMBRANA HIALINA", "centro_sub": "Factores de riesgo", "ans": 0,
   "items": [("DIABETES MATERNA", ["Hiperinsulinemia fetal", "Retrasa el surfactante"]),
             ("Prematuridad", ["Principal factor"]),
             ("Sexo masculino", ["Maduración más lenta"]),
             ("Cesárea sin labor", ["Sin estrés del parto"]),
             ("Protectores", ["Corticoides, heroína, RPM"])],
   "ruta": ["Pretérmino", "Madre diabética", "Menos surfactante", "DIABETES MATERNA"]},
  ["Corticoides prenatales entre 24 y 34 semanas reducen el riesgo.",
   "Rx: vidrio esmerilado y broncograma aéreo.",
   "Tratamiento: CPAP y surfactante."],
  NELSON + " · European Consensus Guidelines on RDS (2022)")

# NEF-042 · tarjetas
V("tarjetas", "NEF-042", "globo-vesical-creatinina-potasio-sonda", "Retención urinaria aguda",
  "NEFROLOGÍA ENAM: RETENCIÓN URINARIA AGUDA", "NEFROLOGÍA",
  ("Retención urinaria aguda", ["Globo vesical doloroso con falla renal posrenal",
   "Conducta inmediata: cateterizar la vejiga"]),
  ("Varón de 78 años con dolor hipogástrico", ["Masa redondeada bajo el ombligo", "Creatinina 2.8 · potasio 6"]),
  {"rotulo": "¿Qué hacer primero?", "ans": 0, "cards": [
      {"titulo": "CATETERIZACIÓN VESICAL", "datos": [
          ("Qué hace", "Desobstruye la vejiga", True), ("Momento", "Inmediato", True),
          ("En el caso", "Globo vesical, K 6", True)],
       "pie": "Vigilar poliuria posobstructiva"},
      {"titulo": "TC abdominal", "datos": [
          ("Qué hace", "Estudia la causa", False), ("Momento", "Después", False),
          ("En el caso", "No es urgente", False)],
       "pie": "Si hay duda diagnóstica"},
      {"titulo": "Cistoscopia", "datos": [
          ("Qué hace", "Ve uretra y vejiga", False), ("Momento", "Diferido", False),
          ("En el caso", "No en retención aguda", False)],
       "pie": "Estudio electivo"},
      {"titulo": "Hemodiálisis", "datos": [
          ("Qué hace", "Depura K y urea", False), ("Momento", "Si no mejora", False),
          ("En el caso", "Falla posrenal reversible", False)],
       "pie": "Solo si persiste la hiperpotasemia"}]},
  ["Con K 6: pedir ECG; gluconato de calcio si hay cambios.",
   "Si la sonda uretral no pasa: cistostomía suprapúbica.",
   "Causa más frecuente en el varón mayor: HBP."],
  "EAU – Guidelines on management of non-neurogenic male LUTS (2024) · Campbell-Walsh-Wein Urology 12.ª ed. (2020)")

# NEU-030 · matriz
V("matriz", "NEU-030", "matidez-abolicion-mv-egofonia-derrame-pleural", "Semiología del tórax",
  "NEUMOLOGÍA ENAM: DERRAME PLEURAL", "NEUMOLOGÍA",
  ("Síndrome de derrame pleural", ["Matidez, murmullo abolido y vibraciones vocales abolidas",
   "Egofonía en el borde superior; si es grande, abomba el hemitórax"]),
  ("Varón de 46 años con 5 días de tos y fiebre", ["Abombamiento del hemitórax derecho", "Matidez, MV abolido, egofonía en la base"]),
  {"rotulo": "Síndromes pulmonares", "eje_x": "Signo", "eje_y": "Síndrome",
   "cols": ["Percusión", "Vibraciones", "Mediastino"], "rows": ["Derrame", "Consolidación", "Neumotórax", "Atelectasia"], "caso": (0, 0),
   "cells": [[("MATIDEZ", ["MV abolido, egofonía"]), ("Abolidas", []), ("Se aleja", [])],
             [("Matidez", ["Soplo tubárico"]), ("Aumentadas", []), ("Central", [])],
             [("Timpanismo", ["MV abolido"]), ("Abolidas", []), ("Se aleja", ["Si es a tensión"])],
             [("Matidez", ["MV disminuido"]), ("Disminuidas", []), ("Se acerca", [])]]},
  ["Con fiebre y tos: pensar en derrame paraneumónico; hacer toracocentesis.",
   "Criterios de Light para diferenciar exudado y trasudado.",
   "pH < 7.2 o pus: empiema, requiere drenaje."],
  "BTS – Guideline for pleural disease (2023) · Argente-Álvarez – Semiología médica 3.ª ed. (2021)")
