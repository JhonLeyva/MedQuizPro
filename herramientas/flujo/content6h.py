"""Bloque 6 · parte H."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
GOODMAN = "Goodman & Gilman – Las bases farmacológicas de la terapéutica 14.ª ed. (2023)"

# GIN-114 · tarjetas
V("tarjetas", "GIN-114", "mola-evacuada-vigilancia-implante-progestina", "Anticoncepción tras enfermedad molar",
  "GINECOLOGÍA ENAM: ANTICONCEPCIÓN TRAS MOLA", "GINECOLOGÍA",
  ("Anticoncepción en la vigilancia posmolar", ["Un embarazo impediría interpretar la β-hCG",
   "Métodos hormonales eficaces; evitar los intrauterinos mientras la β-hCG esté alta"]),
  ("Tercigesta con mola evacuada", ["Cesareada anterior", "En vigilancia con β-hCG"]),
  {"rotulo": "¿Qué método conviene?", "ans": 0, "cards": [
      {"titulo": "IMPLANTE DE PROGESTINA", "datos": [
          ("Tipo", "Hormonal subdérmico", True), ("Con β-hCG alta", "Permitido", True),
          ("Eficacia", "Muy alta (> 99%)", True)],
       "pie": "No altera el seguimiento"},
      {"titulo": "DIU con levonorgestrel", "datos": [
          ("Tipo", "Intrauterino", False), ("Con β-hCG alta", "Evitar: perforación", False),
          ("Eficacia", "Muy alta", False)],
       "pie": "Cuando la β-hCG se normalice"},
      {"titulo": "T de cobre", "datos": [
          ("Tipo", "Intrauterino", False), ("Con β-hCG alta", "Evitar: perforación", False),
          ("Eficacia", "Muy alta", False)],
       "pie": "Cuando la β-hCG se normalice"},
      {"titulo": "Preservativo", "datos": [
          ("Tipo", "Barrera", False), ("Con β-hCG alta", "Permitido", False),
          ("Eficacia", "Baja con uso típico", False)],
       "pie": "Falla alrededor del 13%"}]},
  ["Vigilancia: β-hCG semanal hasta negativizar y luego mensual.",
   "Los anticonceptivos orales también son válidos.",
   "No embarazarse durante el seguimiento (6-12 meses)."],
  "OMS – Criterios médicos de elegibilidad para el uso de anticonceptivos 5.ª ed. (2015) · FIGO – GTD update (2021)")

# PED-123 · termómetro
V("termometro", "PED-123", "prematuro-2200-g-temblores-hipoactivo-hipoglucemia", "Hipoglucemia neonatal",
  "PEDIATRÍA ENAM: HIPOGLUCEMIA NEONATAL", "PEDIATRÍA",
  ("Hipoglucemia neonatal", ["Riesgo: prematuro tardío, bajo peso, hijo de madre diabética o con preeclampsia",
   "Síntomas: temblores, hipoactividad, succión débil, apneas"]),
  ("RN de 35 semanas y 2200 g", ["Cesárea por preeclampsia · Apgar 7 y 8", "A las 3 horas: hipoactividad y temblores"]),
  {"rotulo": "Glucemia en las primeras horas",
   "niveles": [("≥ 45", "Normal", ["Alimentar a libre demanda"]),
               ("25-44", "Baja sin síntomas", ["Alimentar y repetir en 1 h"]),
               ("Síntomas", "Hipoglucemia sintomática", ["Temblor, hipoactividad"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Glucemia capilar inmediata", ["Confirmar la sospecha"], False),
             (2, "DEXTROSA 10% 2 mL/kg EV", ["Si hay síntomas"], True),
             (3, "Infusión 4-6 mg/kg/min", ["Controles seriados"], False)]},
  ["Tamizar glucosa en todo RN de riesgo en las primeras horas.",
   "La hipoglucemia sostenida daña el cerebro (región occipital).",
   "Sepsis y asfixia: menos probables con buen Apgar y sin factores de infección."],
  "AAP – Postnatal glucose homeostasis in late-preterm and term infants (2011) · " + NELSON)

# INF-058 · embudo
V("embudo", "INF-058", "adenopatias-cervicales-fistula-caseosa-tb-ganglionar", "Adenopatías cervicales crónicas",
  "INFECTOLOGÍA ENAM: TUBERCULOSIS GANGLIONAR", "INFECTOLOGÍA",
  ("Tuberculosis ganglionar (escrófula)", ["Adenopatías cervicales indoloras que se fistulizan",
   "Es la forma extrapulmonar más frecuente"]),
  ("Varón de 22 años con 3 meses de adenopatías", ["Cervicales bilaterales, sin flogosis · fiebre", "Una drena material blanquecino grumoso"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Adenopatías cervicales de 3 meses",
   "candidatos": ["TB ganglionar", "Linfoma", "Linfadenitis reactiva", "Sarcoidosis", "Arañazo de gato"],
   "pasos": [("3 meses, bilateral, sin flogosis", ["Linfadenitis reactiva"]),
             ("Fístula con material caseoso", ["Linfoma", "Sarcoidosis"]),
             ("Eritema indurado previo: tubercúlide", ["Arañazo de gato"])],
   "final": ("TUBERCULOSIS GANGLIONAR", ["Escrófula", "PAAF o biopsia + cultivo y prueba molecular"]),
   "nota": "Tratamiento: esquema para TB sensible por 6 meses (2HRZE/4HR)."},
  ["Eritema indurado de Bazin: nódulos en piernas asociados a TB.",
   "Descartar VIH en todo paciente con TB.",
   "No extirpar sin diagnóstico: riesgo de fístula crónica."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · ATS/CDC/IDSA – Extrapulmonary TB")

# NEU-031 · termómetro
V("termometro", "NEU-031", "sintomas-2-dias-semana-2-noches-mes-asma-intermitente", "Asma: clasificación por gravedad",
  "NEUMOLOGÍA ENAM: ASMA INTERMITENTE", "NEUMOLOGÍA",
  ("Clasificación del asma", ["Según frecuencia de síntomas diurnos y nocturnos",
   "Intermitente: síntomas ≤ 2 días por semana y ≤ 2 noches al mes"]),
  ("Paciente con asma", ["Disnea y broncoespasmo 2 días por semana", "Síntomas nocturnos 2 veces al mes"]),
  {"rotulo": "Gravedad",
   "niveles": [("≤ 2 d/sem", "Intermitente", ["Noches ≤ 2 al mes"]),
               ("> 2 d/sem", "Persistente leve", ["Noches > 2 al mes"]),
               ("Diario", "Persistente moderada", ["Noches > 1 por semana"]),
               ("Continuo", "Persistente grave", ["Noches frecuentes"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento (GINA)", "paso_label": "PASO",
   "pasos": [(1, "CI-FORMOTEROL A DEMANDA", ["No usar SABA solo"], True),
             (2, "CI a dosis baja diaria", ["Persistente leve"], False),
             (3, "CI + LABA", ["Moderada o grave"], False)]},
  ["GINA ya no recomienda SABA sin corticoide inhalado.",
   "Revisar técnica inhalatoria y adherencia antes de subir de paso.",
   "El control se evalúa en las últimas 4 semanas."],
  "GINA – Global Strategy for Asthma Management and Prevention (2024)")

# REU-035 · tarjetas
V("tarjetas", "REU-035", "obesa-diabetica-pliegues-inguinales-candida", "Lesión en pliegues inguinales",
  "DERMATOLOGÍA ENAM: INTERTRIGO CANDIDIÁSICO", "DERMATOLOGÍA",
  ("Intertrigo candidiásico", ["Pliegues húmedos en obesos y diabéticos",
   "Placa roja húmeda que llega al fondo del pliegue, con lesiones satélite"]),
  ("Mujer de 50 años, obesa y diabética", ["Prurito y dolor inguinal de 15 días", "Placas eritematosas y descamativas en ambos pliegues"]),
  {"rotulo": "¿Qué agente es?", "ans": 0, "cards": [
      {"titulo": "CANDIDA ALBICANS", "datos": [
          ("Lesión", "Roja, húmeda, satélites", True), ("Pliegue", "Afecta el fondo", True),
          ("Terreno", "Diabetes, obesidad", True)],
       "pie": "Azoles tópicos, secar la zona"},
      {"titulo": "Trichophyton rubrum", "datos": [
          ("Lesión", "Borde activo, centro claro", False), ("Pliegue", "Respeta el fondo", False),
          ("Terreno", "Tiña crural", False)],
       "pie": "Terbinafina"},
      {"titulo": "Malassezia furfur", "datos": [
          ("Lesión", "Máculas hipo o hiper", False), ("Pliegue", "Tronco, no ingle", False),
          ("Terreno", "Pitiriasis versicolor", False)],
       "pie": "Azoles o sulfuro de selenio"},
      {"titulo": "Pityrosporum ovale", "datos": [
          ("Lesión", "Escama grasa", False), ("Pliegue", "Cara, cuero cabelludo", False),
          ("Terreno", "Dermatitis seborreica", False)],
       "pie": "Ketoconazol champú"}]},
  ["Controlar la glucemia y mantener los pliegues secos.",
   "Los corticoides tópicos solos empeoran la candidiasis.",
   "Eritrasma: color pardo y fluorescencia rojo coral con luz de Wood."],
  "IDSA – Clinical practice guideline for candidiasis (2016) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# NRL-034 · fases
V("fases", "NRL-034", "ptosis-diplopia-fatiga-receptor-nicotinico", "Miastenia gravis: unión neuromuscular",
  "NEUROLOGÍA ENAM: MIASTENIA GRAVIS", "NEUROLOGÍA",
  ("Miastenia gravis", ["Anticuerpos contra el receptor nicotínico de acetilcolina",
   "Debilidad fatigable: empeora con el esfuerzo y mejora con el reposo"]),
  ("Mujer de 30 años con LES", ["Ptosis y diplopía", "Debilidad que empeora con la actividad"]),
  {"rotulo": "Transmisión neuromuscular", "ans": 1,
   "fases": [("Nervio", "Terminal", "Libera acetilcolina", ["Por el calcio"]),
             ("Placa", "Sinapsis", "RECEPTOR NICOTÍNICO", ["Bloqueado por anti-AChR"]),
             ("Músculo", "Fibra", "Contracción", ["Falla con la repetición"])],
   "curvas": [],
   "chips_titulo": "Receptor · marcado el correcto",
   "chips": [("Nicotínicos", True), ("GABA", False), ("Adrenérgicos", False), ("Dopaminérgicos", False)]},
  ["Diagnóstico: anti-AChR, EMG con estimulación repetitiva.",
   "Tratamiento: piridostigmina e inmunosupresión; timectomía si hay timoma.",
   "Se asocia a otras enfermedades autoinmunes como el LES."],
  "MGFA – International consensus guidance for management of myasthenia gravis (2020 update) · " + HARRISON)

# INF-059 · matriz
V("matriz", "INF-059", "drogas-ev-janeway-soplo-mitral-staphylococcus", "Endocarditis: germen según el contexto",
  "INFECTOLOGÍA ENAM: ENDOCARDITIS INFECCIOSA", "INFECTOLOGÍA",
  ("Endocarditis en usuario de drogas EV", ["Staphylococcus aureus: curso agudo, destructivo, con embolias",
   "Lesiones de Janeway: máculas indoloras en palmas y plantas"]),
  ("Varón de 48 años usuario de drogas EV", ["Fiebre y disnea de 1 semana", "Lesiones de Janeway · soplo mitral III/VI"]),
  {"rotulo": "Germen según el contexto", "eje_x": "Aspecto", "eje_y": "Contexto",
   "cols": ["Germen", "Válvula"], "rows": ["Drogas EV", "Válvula nativa", "Prótesis < 1 año", "Cáncer de colon"], "caso": (0, 0),
   "cells": [[("S. AUREUS", ["Agudo, embolias"]), ("Tricúspide", ["Aquí: mitral"])],
             [("S. viridans", ["Tras manipulación dental"]), ("Mitral", ["Subaguda"])],
             [("S. epidermidis", []), ("Protésica", [])],
             [("S. gallolyticus", ["Buscar el cáncer"]), ("Cualquiera", [])]]},
  ["Tomar 3 hemocultivos antes del antibiótico.",
   "Ecocardiograma transesofágico si el transtorácico es normal.",
   "Nódulos de Osler: dolorosos (inmunológicos); Janeway: indoloros (embólicos)."],
  "ESC – Guidelines for the management of endocarditis (2023)")

# PED-124 · radial
V("radial", "PED-124", "evento-centinela-encefalopatia-hipoxica-dpp", "Eventos centinela intraparto",
  "PEDIATRÍA ENAM: ENCEFALOPATÍA HIPÓXICO-ISQUÉMICA", "PEDIATRÍA",
  ("Evento centinela", ["Suceso agudo intraparto que corta el oxígeno al feto",
   "Se asocia a encefalopatía hipóxico-isquémica"]),
  ("Pregunta de concepto", ["¿Qué condición del trabajo de parto", "es un evento centinela?"]),
  {"rotulo": "Mapa del tema", "centro": "EVENTO CENTINELA", "centro_sub": "Hipoxia aguda intraparto", "ans": 0,
   "items": [("DPP", ["Desprendimiento de placenta", "Corta el intercambio"]),
             ("Rotura uterina", ["Feto en el abdomen"]),
             ("Prolapso de cordón", ["Compresión del cordón"]),
             ("Embolia de LA", ["Colapso materno"]),
             ("Paro materno", ["Sin perfusión placentaria"])],
   "ruta": ["Evento agudo intraparto", "Hipoxia fetal súbita", "Encefalopatía neonatal", "DPP"]},
  ["Las desaceleraciones variables suelen ser por compresión del cordón y no son centinela.",
   "Hipotermia terapéutica en EHI moderada o grave dentro de 6 horas.",
   "Apgar bajo y acidosis de cordón apoyan el diagnóstico."],
  "ACOG/AAP – Neonatal encephalopathy and neurologic outcome 2.ª ed. (2014, reafirmado 2019)")

# CB-040 · radial
V("radial", "CB-040", "sacar-lengua-musculo-geniogloso", "Músculos de la lengua",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA DE LA LENGUA", "CIENCIAS BÁSICAS",
  ("Músculo geniogloso", ["Protruye la lengua (la lleva hacia adelante)",
   "Inervado por el hipogloso (XII)"]),
  ("Evaluación clínica", ["Se pide al paciente", "que lleve la lengua hacia adelante"]),
  {"rotulo": "Mapa del tema", "centro": "LENGUA", "centro_sub": "Músculos extrínsecos", "ans": 0,
   "items": [("GENIOGLOSO", ["Protruye la lengua", "Lesión del XII: se desvía al lado dañado"]),
             ("Hiogloso", ["Deprime la lengua"]),
             ("Estilogloso", ["Retrae y eleva"]),
             ("Palatogloso", ["Eleva la raíz; nervio vago"]),
             ("Intrínsecos", ["Cambian su forma"])],
   "ruta": ["Sacar la lengua", "Músculo extrínseco", "Nervio hipogloso (XII)", "GENIOGLOSO"]},
  ["Todos los músculos de la lengua los inerva el XII, salvo el palatogloso (X).",
   "Lesión del XII: la lengua se desvía hacia el lado lesionado.",
   "El geniogloso evita que la lengua caiga atrás en el inconsciente."],
  "Moore – Anatomía con orientación clínica 9.ª ed. (2022)")

# INF-060 · fases
V("fases", "INF-060", "piura-fiebre-2-dias-leucopenia-ns1", "Dengue: examen según el día",
  "INFECTOLOGÍA ENAM: DIAGNÓSTICO DE DENGUE", "INFECTOLOGÍA",
  ("Diagnóstico de dengue", ["Primeros 5 días de fiebre: antígeno NS1 o RT-PCR",
   "Desde el día 5-6: IgM"]),
  ("Varón de 27 años de Piura", ["Fiebre de 2 días, mialgias, cefalea, epistaxis", "Leucocitos 2200 · plaquetas 150 000"]),
  {"rotulo": "Marcadores según los días", "ans": 0,
   "fases": [("Febril", "Días 1-5", "ANTÍGENO NS1", ["O RT-PCR"]),
             ("Crítica", "Días 4-7", "IgM", ["Signos de alarma"]),
             ("Recupera", "> Día 7", "IgG", ["Infección previa"])],
   "curvas": [("NS1", ROSE, [0.9, 0.95, 0.7, 0.3, 0.1, 0.05, 0.0]),
              ("IgM", AMBER, [0.0, 0.1, 0.5, 0.9, 0.8, 0.5, 0.3]),
              ("IgG", SKY, [0.0, 0.0, 0.1, 0.4, 0.7, 0.9, 1.0])],
   "chips_titulo": "Examen · marcado el correcto",
   "chips": [("Antígeno NS1", True), ("IgM dengue", False), ("IgG dengue", False), ("Inhibición-hemaglutinación", False)]},
  ["Una IgM negativa en los primeros días no descarta dengue.",
   "Epistaxis sola no es signo de alarma; vigilar dolor abdominal y vómitos.",
   "Paracetamol; evitar AINE y aspirina."],
  "MINSA – NTS N.° 211-MINSA/DGIESP-2024 (Atención del dengue) · OPS – Dengue: guías para la atención (2022)")

# GIN-115 · embudo
V("embudo", "GIN-115", "cesarea-14-meses-sangrado-utero-contraido-dehiscencia", "Hemorragia posparto con útero contraído",
  "OBSTETRICIA ENAM: DEHISCENCIA DE CICATRIZ UTERINA", "OBSTETRICIA",
  ("Dehiscencia de cicatriz uterina", ["Periodo intergenésico corto (< 18 meses) tras cesárea",
   "Sangrado, dolor intenso y choque con útero contraído"]),
  ("Segundigesta de 39 semanas", ["Cesárea hace 14 meses · parto vaginal", "Tras el alumbramiento: sangrado, dolor, PA 80/50"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hemorragia y choque tras el alumbramiento",
   "candidatos": ["Dehiscencia de cicatriz", "Atonía uterina", "Retención placentaria", "Laceración vaginal", "Hematoma perineal"],
   "pasos": [("Útero contraído", ["Atonía uterina"]),
             ("Placenta ya expulsada", ["Retención placentaria"]),
             ("Dolor abdominal intenso con cesárea reciente", ["Laceración vaginal", "Hematoma perineal"])],
   "final": ("DEHISCENCIA DE CICATRIZ", ["Periodo intergenésico de 14 meses", "Laparotomía y reparación"]),
   "nota": "Tras una cesárea, esperar al menos 18 meses antes de otro embarazo."},
  ["Reanimar con cristaloides y sangre mientras se prepara la cirugía.",
   "Revisar el segmento uterino si hay sangrado con útero contraído.",
   "Las «4 T»: tono, trauma, tejido, trombina."],
  WILLIAMS + " · MINSA – Guía de práctica clínica de hemorragia posparto")

# GIN-116 · fases
V("fases", "GIN-116", "gestante-14-semanas-vih-confirmado-tar-inmediato", "VIH en la gestante",
  "OBSTETRICIA ENAM: VIH EN EL EMBARAZO", "OBSTETRICIA",
  ("VIH en el embarazo", ["Iniciar TAR apenas se confirma, en cualquier edad gestacional",
   "No esperar CD4 ni carga viral"]),
  ("Gestante de 27 años de 14 semanas", ["Prueba rápida (+)", "Prueba confirmatoria (+)"]),
  {"rotulo": "Plan en el embarazo", "ans": 0,
   "fases": [("Diagnóstico", "14 sem", "INICIAR TAR YA", ["Sin esperar CD4"]),
             ("Control", "+ 4 sem", "Carga viral", ["Adherencia"]),
             ("Preparto", "34-36 sem", "Carga viral", ["Define la vía del parto"]),
             ("Parto", "38 sem", "Según carga viral", ["Profilaxis al RN"])],
   "curvas": [("Carga", ROSE, [1.0, 0.6, 0.3, 0.1, 0.05, 0.03, 0.02])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("Iniciar TAR", True), ("Esperar 20 semanas", False), ("CD4 previo", False), ("Referir a I-2", False)]},
  ["Esquema preferido: dolutegravir + tenofovir + lamivudina o emtricitabina.",
   "Mientras más temprano el TAR, menor la transmisión.",
   "Tamizar también sífilis y hepatitis B."],
  "MINSA – NTS N.° 159-MINSA/2019/DGIESP (Transmisión materno-infantil) · OMS – Consolidated HIV guidelines (2021)")

# SP-083 · embudo
V("embudo", "SP-083", "terminal-pide-morir-medico-omite-medidas-eutanasia-pasiva", "Decisiones ante el pedido de morir",
  "SALUD PÚBLICA ENAM: EUTANASIA PASIVA", "SALUD PÚBLICA",
  ("Eutanasia pasiva", ["El médico omite o retira medidas para causar la muerte a pedido del paciente",
   "Activa: el médico actúa (p. ej., fármaco letal)"]),
  ("Paciente con enfermedad terminal", ["Pide al médico terminar con su vida", "El médico omite medidas que prolongarían la vida"]),
  {"rotulo": "Embudo de conceptos",
   "inicio": "El médico omite medidas a pedido del paciente",
   "candidatos": ["Eutanasia pasiva", "Eutanasia activa", "Suicidio asistido", "Ortotanasia", "Distanasia"],
   "pasos": [("El médico omite, no actúa", ["Eutanasia activa", "Suicidio asistido"]),
             ("La intención es terminar la vida", ["Ortotanasia"]),
             ("No prolonga la agonía", ["Distanasia"])],
   "final": ("EUTANASIA PASIVA", ["Omisión con intención de morir", "Es delito en el Perú"]),
   "nota": "Retirar un tratamiento fútil sin intención de matar es limitación del esfuerzo terapéutico, no eutanasia."},
  ["Ortotanasia: dejar que la muerte llegue a su tiempo, con alivio.",
   "Distanasia: prolongar la agonía con medidas fútiles.",
   "Código Penal peruano, art. 112: homicidio piadoso."],
  "Beauchamp y Childress – Principles of Biomedical Ethics 8.ª ed. (2019) · CMP – Código de Ética y Deontología (2023)")

# GIN-117 · tarjetas
V("tarjetas", "GIN-117", "dos-cesareas-dolor-choque-latidos-ausentes-rotura-uterina", "Hemorragia del tercer trimestre",
  "OBSTETRICIA ENAM: ROTURA UTERINA", "OBSTETRICIA",
  ("Rotura uterina", ["Dolor intenso súbito, cese de contracciones y choque",
   "Pérdida de latidos fetales; mayor riesgo con cesáreas previas"]),
  ("Gestante de 38 semanas con 2 cesáreas", ["Dolor intenso tras contracciones, sangrado", "PA 80/40, FC 128 · latidos fetales ausentes"]),
  {"rotulo": "¿Qué ocurrió?", "ans": 0, "cards": [
      {"titulo": "ROTURA UTERINA", "datos": [
          ("Dolor", "Súbito, cesan contracciones", True), ("Feto", "Latidos ausentes", True),
          ("Clave", "Cesáreas previas", True)],
       "pie": "Laparotomía inmediata"},
      {"titulo": "Desprendimiento de placenta", "datos": [
          ("Dolor", "Útero leñoso", False), ("Feto", "Sufrimiento fetal", False),
          ("Clave", "HTA, trauma, cocaína", False)],
       "pie": "Sangre oscura"},
      {"titulo": "Placenta previa", "datos": [
          ("Dolor", "Indoloro", False), ("Feto", "Suele estar bien", False),
          ("Clave", "Sangrado rojo rutilante", False)],
       "pie": "No hacer tacto vaginal"},
      {"titulo": "Acretismo placentario", "datos": [
          ("Dolor", "Sin dolor previo", False), ("Feto", "Normal", False),
          ("Clave", "La placenta no sale", False)],
       "pie": "Cesárea-histerectomía"}]},
  ["Signos: partes fetales palpables en el abdomen y ascenso de la presentación.",
   "Riesgo mayor con incisión corporal previa.",
   "Reanimar y operar: no esperar estudios."],
  WILLIAMS + " · MINSA – Guía de atención de emergencias obstétricas")

# GAS-045 · termómetro
V("termometro", "GAS-045", "cirrotico-estrenimiento-flapping-lactulosa", "Encefalopatía hepática",
  "GASTROENTEROLOGÍA ENAM: ENCEFALOPATÍA HEPÁTICA", "GASTROENTEROLOGÍA",
  ("Encefalopatía hepática", ["Precipitantes: estreñimiento, proteínas, infección, sangrado",
   "Tratamiento inicial: lactulosa + corregir el desencadenante"]),
  ("Varón de 48 años con cirrosis", ["Somnolencia y confusión progresiva · flapping", "Estreñimiento y dieta no cumplida"]),
  {"rotulo": "Grados de West Haven",
   "niveles": [("Grado I", "Leve", ["Atención corta, euforia"]),
               ("Grado II", "Letargo", ["Desorientación, asterixis"]),
               ("Grado III", "Somnolencia", ["Estupor, confusión marcada"]),
               ("Grado IV", "Coma", ["No responde"])],
   "caso_nivel": 1, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Buscar el desencadenante", ["Estreñimiento, infección, sangrado"], False),
             (2, "LACTULOSA", ["2-3 deposiciones blandas al día"], True),
             (3, "+ Rifaximina", ["Si recurre"], False)]},
  ["La lactulosa acidifica el colon y atrapa el amonio.",
   "No restringir proteínas en exceso: empeora la desnutrición.",
   "Descartar PBE con paracentesis si hay ascitis."],
  "AASLD/EASL – Hepatic encephalopathy in chronic liver disease (2014) · EASL – Decompensated cirrhosis (2018)")

# NRL-035 · árbol
A("NRL-035", "hematoma-cerebeloso-35-cm-cuarto-ventriculo-cirugia", "Hemorragia cerebelosa",
  "NEUROLOGÍA ENAM: HEMATOMA CEREBELOSO", "NEUROLOGÍA",
  ("Hemorragia cerebelosa", ["Ataxia, vómitos, nistagmo y cefalea súbita",
   "> 3 cm, deterioro o compresión del IV ventrículo: cirugía urgente"]),
  ("Varón de 58 años hipertenso", ["Letárgico, ataxia, disartria, nistagmo", "Hematoma de 3.5 cm que comprime el IV ventrículo"]),
  Q("¿> 3 cm, deterioro o comprime el IV?", [
      L("Sí", "DESCOMPRESIÓN QUIRÚRGICA", ["Evacuación del hematoma", "± drenaje ventricular"], path=True),
      L("No", "Manejo médico en UCI", ["PA, cabecera 30°, vigilar"])], path=True),
  ("Cerebelosa vs supratentorial", [("Cerebelosa", True), ("Supratentorial", False)], [
      ("Cirugía", ["> 3 cm o comprime el IV", "Casos seleccionados"]),
      ("Riesgo", ["Compresión del tronco", "Herniación"])]),
  ["El drenaje ventricular solo, sin evacuar, puede herniar hacia arriba.",
   "Los corticoides no sirven en la hemorragia cerebral.",
   "Controlar la PA como en toda hemorragia intracerebral."],
  "AHA/ASA – Guideline for the management of spontaneous intracerebral hemorrhage (2022)")

# CB-041 · radial
V("radial", "CB-041", "epilepsia-pielonefritis-levofloxacino-convulsiones", "Efectos adversos de las quinolonas",
  "CIENCIAS BÁSICAS ENAM: FLUOROQUINOLONAS", "CIENCIAS BÁSICAS",
  ("Fluoroquinolonas y convulsiones", ["Antagonizan el receptor GABA-A",
   "Bajan el umbral convulsivo: evitar en epilepsia"]),
  ("Mujer de 30 años con epilepsia mal controlada", ["Pielonefritis por E. coli sensible", "¿Qué antibiótico da más convulsiones?"]),
  {"rotulo": "Mapa del tema", "centro": "QUINOLONAS", "centro_sub": "Efectos adversos", "ans": 0,
   "items": [("CONVULSIONES", ["Antagonizan el GABA", "Evitar en epilepsia"]),
             ("Tendones", ["Rotura del Aquiles"]),
             ("QT largo", ["Arritmias"]),
             ("Glucosa", ["Hipo o hiperglucemia"]),
             ("Aorta", ["Aneurisma, disección"])],
   "ruta": ["Epilepsia + pielonefritis", "Elegir antibiótico", "Quinolona baja el umbral", "LEVOFLOXACINO"]},
  ["Los carbapenémicos (imipenem) también bajan el umbral.",
   "Nitrofurantoína no sirve para pielonefritis.",
   "Alternativa: ceftriaxona si el germen es sensible."],
  GOODMAN + " · FDA – Fluoroquinolone safety communications (2016-2018)")

# SP-084 · embudo
V("embudo", "SP-084", "visitador-medico-comision-receta-conflicto-interes", "Comisión por recetar",
  "SALUD PÚBLICA ENAM: CONFLICTO DE INTERÉS", "SALUD PÚBLICA",
  ("Conflicto de interés", ["Un interés secundario (dinero) puede influir en la decisión clínica",
   "Prescribir por comisión vulnera la ética médica"]),
  ("Visita de un representante farmacéutico", ["Ofrece comisión por cada receta", "Desacredita a los genéricos"]),
  {"rotulo": "Embudo de conceptos",
   "inicio": "Comisión económica por recetar",
   "candidatos": ["Conflicto de interés", "Objeción de conciencia", "Uso responsable", "Libertad terapéutica", "Publicidad médica"],
   "pasos": [("Recibe dinero por receta: interés secundario", ["Uso responsable", "Libertad terapéutica"]),
             ("No hay conflicto de valores religiosos o morales", ["Objeción de conciencia"]),
             ("No se trata de informar sobre el producto", ["Publicidad médica"])],
   "final": ("CONFLICTO DE INTERÉS", ["El interés económico influye", "Rechazar y prescribir por DCI"]),
   "nota": "El Código de Ética del CMP prohíbe recibir beneficios por prescribir."},
  ["Prescribir por Denominación Común Internacional (genérico).",
   "Los genéricos aprobados por DIGEMID son equivalentes.",
   "Declarar conflictos de interés en investigación y docencia."],
  "CMP – Código de Ética y Deontología (2023) · Ley N.° 29459 de productos farmacéuticos")

# PED-125 · matriz
V("matriz", "PED-125", "osteomielitis-aguda-nino-staphylococcus-aureus", "Osteomielitis: germen según el paciente",
  "PEDIATRÍA ENAM: OSTEOMIELITIS AGUDA", "PEDIATRÍA",
  ("Osteomielitis aguda en el niño", ["Hematógena, en la metáfisis de huesos largos",
   "Germen más frecuente a toda edad: Staphylococcus aureus"]),
  ("Pregunta de concepto", ["Patógeno más asociado", "a osteomielitis aguda en niños"]),
  {"rotulo": "Germen según el paciente", "eje_x": "Aspecto", "eje_y": "Paciente",
   "cols": ["Germen", "Tratamiento"], "rows": ["Neonato", "Niño > 1 mes", "Drepanocitosis", "Herida plantar"], "caso": (1, 0),
   "cells": [[("SGB, S. aureus", ["Gramnegativos"]), ("Oxacilina + cefotaxima", [])],
             [("S. AUREUS", ["Kingella < 4 años"]), ("Cefazolina u oxacilina", ["Clindamicina si SAMR"])],
             [("Salmonella", []), ("Cefalosporina 3.ª", [])],
             [("Pseudomonas", ["Por la zapatilla"]), ("Ceftazidima", [])]]},
  ["La RM es el estudio más sensible; la Rx tarda 10-14 días.",
   "PCR y VSG sirven para seguir la respuesta.",
   "Antibiótico EV corto y paso a vía oral al mejorar."],
  "PIDS/IDSA – Guideline on acute hematogenous osteomyelitis in children (2021) · " + NELSON)

# CIR-062 · fases
V("fases", "CIR-062", "golpe-timon-fast-negativo-dolor-epigastrico-pancreas", "Trauma pancreático",
  "CIRUGÍA ENAM: TRAUMA PANCREÁTICO", "CIRUGÍA",
  ("Trauma pancreático", ["Golpe epigástrico (timón) contra la columna",
   "Retroperitoneal: el FAST suele ser negativo; el dolor aumenta con los días"]),
  ("Chofer de 42 años con choque frontal", ["Golpe con el timón · estable", "FAST negativo · día 2: dolor epigástrico en aumento"]),
  {"rotulo": "Evolución", "ans": 2,
   "fases": [("Ingreso", "Hora 1", "FAST negativo", ["No ve el retroperitoneo"]),
             ("Observa", "24-48 h", "Dolor epigástrico ↑", ["Amilasa en ascenso"]),
             ("Diagnóstico", "Día 2", "TRAUMA PANCREÁTICO", ["TEM con contraste"]),
             ("Tardío", "Semanas", "Seudoquiste o fístula", ["Si no se trata"])],
   "curvas": [("Dolor", ROSE, [0.3, 0.35, 0.5, 0.7, 0.85, 0.9, 0.9]),
              ("Amilasa", AMBER, [0.1, 0.2, 0.4, 0.7, 0.8, 0.7, 0.6])],
   "chips_titulo": "Sospecha · marcada la correcta",
   "chips": [("Pancreático", True), ("Esplénico", False), ("Hepático", False), ("Vesical", False)]},
  ["La lesión del conducto de Wirsung define la cirugía.",
   "CPRE o colangio-RM para evaluar el conducto.",
   "Bazo e hígado sangran temprano y dan FAST positivo."],
  ATLS + " · EAST – Management of pancreatic injuries (2017)")

# CAR-047 · radial
V("radial", "CAR-047", "fa-antiarritmico-5-anos-tos-disnea-amiodarona", "Toxicidad por amiodarona",
  "CARDIOLOGÍA ENAM: TOXICIDAD POR AMIODARONA", "CARDIOLOGÍA",
  ("Toxicidad pulmonar por amiodarona", ["Neumonitis intersticial o fibrosis con uso prolongado",
   "Tos seca, disnea progresiva y pérdida de peso"]),
  ("Varón de 70 años con FA crónica", ["Antiarrítmico desde hace 5 años", "Disnea a mínimos esfuerzos, tos seca, baja de peso"]),
  {"rotulo": "Mapa del tema", "centro": "AMIODARONA", "centro_sub": "Toxicidad", "ans": 0,
   "items": [("PULMÓN", ["Neumonitis, fibrosis", "Tos seca y disnea"]),
             ("Tiroides", ["Hipo o hipertiroidismo"]),
             ("Hígado", ["Transaminasas altas"]),
             ("Piel", ["Fotosensibilidad, color gris"]),
             ("Ojo", ["Depósitos corneales"])],
   "ruta": ["FA crónica", "Antiarrítmico 5 años", "Tos seca y disnea", "AMIODARONA"]},
  ["Controlar TSH, pruebas hepáticas y Rx de tórax periódicamente.",
   "Tratamiento: suspender el fármaco y corticoides.",
   "Contiene yodo y tiene vida media muy larga."],
  "ACC/AHA/HRS – Atrial fibrillation guideline (2023) · " + GOODMAN)

# PED-126 · embudo
V("embudo", "PED-126", "lactante-2-meses-afebril-conjuntivitis-chlamydia", "Neumonía afebril del lactante",
  "PEDIATRÍA ENAM: NEUMONÍA POR CHLAMYDIA", "PEDIATRÍA",
  ("Neumonía afebril del lactante", ["Chlamydia trachomatis: 1-3 meses, sin fiebre, tos en staccato",
   "Antecedente de conjuntivitis neonatal; infiltrado intersticial"]),
  ("Lactante de 2 meses", ["Tos, secreción nasal, sin fiebre · antecedente de conjuntivitis", "FR 62, SatO₂ 91% · Rx: hiperinsuflación e intersticial"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Lactante de 2 meses con neumonía",
   "candidatos": ["Chlamydia trachomatis", "SGB", "Hib", "Neumococo", "VSR"],
   "pasos": [("Más de 3 semanas de vida", ["SGB"]),
             ("Sin fiebre, curso subagudo, intersticial", ["Neumococo", "Hib"]),
             ("Conjuntivitis neonatal previa", ["VSR"])],
   "final": ("CHLAMYDIA TRACHOMATIS", ["Transmisión en el parto", "Azitromicina o eritromicina"]),
   "nota": "Tratar también a la madre y a su pareja."},
  ["Puede haber eosinofilia periférica.",
   "Eritromicina en menores de 6 semanas: riesgo de estenosis pilórica.",
   "Tamizaje de clamidia en la gestante lo previene."],
  "CDC – STI treatment guidelines: Chlamydial infections in infants (2021) · " + NELSON)

# SP-085 · termómetro
V("termometro", "SP-085", "categoria-iii-meconio-espera-parto-beneficencia", "Monitoreo fetal y beneficencia",
  "SALUD PÚBLICA ENAM: BENEFICENCIA", "SALUD PÚBLICA",
  ("Beneficencia", ["Actuar en el mejor interés del paciente",
   "Esperar un parto vaginal con patrón fetal categoría III expone al feto a daño"]),
  ("Primigesta de 41 semanas al final del turno", ["LCF 109, meconio espeso, 4 cm", "Monitoreo: categoría III · el médico decide esperar"]),
  {"rotulo": "Categoría del monitoreo fetal",
   "niveles": [("Cat. I", "Normal", ["FCF 110-160, variabilidad normal"]),
               ("Cat. II", "Indeterminado", ["Vigilar y reanimar"]),
               ("Cat. III", "Anormal", ["Bradicardia o sin variabilidad"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta correcta", "paso_label": "PASO",
   "pasos": [(1, "Reanimación intrauterina", ["O₂, decúbito lateral, sin oxitocina"], False),
             (2, "PARTO INMEDIATO", ["Cesárea si el parto no es inminente"], True),
             (3, "Neonatólogo en sala", ["Meconio espeso"], False)]},
  ["La omisión por comodidad (fin del turno) vulnera la beneficencia.",
   "No maleficencia: no causar daño; beneficencia: actuar a favor.",
   "Registrar en la historia la decisión y su fundamento."],
  "ACOG – Practice Bulletin N.° 106: Intrapartum fetal heart rate monitoring (2009, reafirmado 2021) · Beauchamp y Childress (2019)")

# INF-061 · árbol
A("INF-061", "nino-3-anos-padre-bk-positivo-ppd-8-terapia-preventiva", "Niño contacto de TB",
  "INFECTOLOGÍA ENAM: TERAPIA PREVENTIVA DE TB", "INFECTOLOGÍA",
  ("Contacto menor de 5 años", ["Alto riesgo de TB grave (meníngea, miliar)",
   "Descartada la TB activa: terapia preventiva, sin importar el PPD"]),
  ("Niño de 3 años", ["Padre con TB pulmonar BK (+)", "PPD 8 mm"]),
  Q("¿Síntomas o Rx anormal?", [
      L("Sí", "Estudiar TB activa", ["Tratamiento completo si se confirma"]),
      L("No", "TERAPIA PREVENTIVA DE TB", ["Independiente del PPD", "Isoniazida 6 meses o 3HP"], path=True)], path=True),
  ("Terapia preventiva", [("Isoniazida", True), ("3HP", False)], [
      ("Duración", ["6 meses diarios", "12 dosis semanales"]),
      ("Fármacos", ["Isoniazida + B6", "Isoniazida + rifapentina"]),
      ("Edad", ["Cualquiera", "≥ 2 años"])]),
  ["El PPD ≥ 5 mm es positivo en contactos.",
   "Todos los contactos se evalúan con clínica y Rx de tórax.",
   "No se aísla al niño; el caso índice inicia tratamiento."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · OMS – TB preventive treatment guidelines (2024)")

# GIN-118 · tarjetas
V("tarjetas", "GIN-118", "enalapril-embarazo-oligohidramnios-ieca", "Antihipertensivos en el embarazo",
  "OBSTETRICIA ENAM: IECA EN EL EMBARAZO", "OBSTETRICIA",
  ("IECA en el embarazo", ["Dañan el riñón fetal: oligohidramnios, hipoplasia pulmonar, falla renal",
   "Contraindicados: cambiar a metildopa, nifedipino o labetalol"]),
  ("Primigesta de 31 semanas sin controles", ["HTA crónica tratada con enalapril", "Oligohidramnios · feto sin malformaciones"]),
  {"rotulo": "¿Qué causó el oligohidramnios?", "ans": 0, "cards": [
      {"titulo": "IECA (ENALAPRIL)", "datos": [
          ("¿Seguro?", "No", True), ("Riesgo fetal", "Oligohidramnios", True),
          ("Uso", "Suspender", True)],
       "pie": "Cambiar a metildopa o nifedipino"},
      {"titulo": "Metildopa", "datos": [
          ("¿Seguro?", "Sí", False), ("Riesgo fetal", "Ninguno relevante", False),
          ("Uso", "Primera línea", False)],
       "pie": "Somnolencia materna"},
      {"titulo": "Nifedipino", "datos": [
          ("¿Seguro?", "Sí", False), ("Riesgo fetal", "Ninguno relevante", False),
          ("Uso", "Primera línea", False)],
       "pie": "Cefalea, rubor"},
      {"titulo": "Labetalol", "datos": [
          ("¿Seguro?", "Sí", False), ("Riesgo fetal", "Bradicardia leve", False),
          ("Uso", "Primera línea", False)],
       "pie": "Evitar en asmáticas"}]},
  ["Los ARA II tienen el mismo riesgo que los IECA.",
   "Diabetes gestacional suele dar polihidramnios, no oligohidramnios.",
   "Evaluar función renal fetal y crecimiento con ecografía."],
  "ACOG – Practice Bulletin N.° 203: Chronic hypertension in pregnancy (2019) · " + WILLIAMS)

# NEF-047 · árbol
A("NEF-047", "tiazida-antiacidos-hco3-32-k-28-alcalosis-metabolica", "Alcalosis metabólica",
  "NEFROLOGÍA ENAM: ALCALOSIS METABÓLICA", "NEFROLOGÍA",
  ("Alcalosis metabólica", ["HCO₃⁻ alto con hipopotasemia e hipocloremia",
   "Causas: diuréticos, vómitos, antiácidos alcalinos"]),
  ("Mujer de 45 años con HTA", ["Hidroclorotiazida + antiácidos", "K 2.8, Cl 88, HCO₃⁻ 32, Ca 10.2"]),
  Q("¿HCO₃⁻ > 26 mEq/L?", [
      L("No", "Otro trastorno", ["Revisar pH y PaCO₂"]),
      Q("¿Cloro urinario?", [
          L("< 20 mEq/L", "Salino-sensible", ["Vómitos, diurético pasado"]),
          L("> 20 mEq/L", "ALCALOSIS METABÓLICA", ["Tiazida activa + antiácidos", "K bajo mantiene la alcalosis"], path=True)],
        edge="Sí", path=True)], path=True),
  ("Datos del caso", [("Valor", True), ("Significa", False)], [
      ("HCO₃⁻ 32", ["Alto", "Alcalosis metabólica"]),
      ("K 2.8 · Cl 88", ["Bajos", "Pérdida renal por tiazida"]),
      ("PaCO₂ esperada", ["0.7 × HCO₃⁻ + 21", "~ 43 mmHg"])]),
  ["Corregir el potasio con KCl: también corrige la alcalosis.",
   "Las tiazidas pueden subir el calcio.",
   "Síndrome leche-álcali: calcio + antiácidos alcalinos."],
  HARRISON + " · KDIGO – Controversies in electrolyte disorders (2020)")

# REU-036 · matriz
V("matriz", "REU-036", "lactante-panal-placa-brillante-pliegues-econazol", "Dermatitis del pañal",
  "DERMATOLOGÍA ENAM: DERMATITIS DEL PAÑAL CANDIDIÁSICA", "DERMATOLOGÍA",
  ("Dermatitis del pañal candidiásica", ["Placa roja brillante que afecta los pliegues, con satélites",
   "Tratamiento: antifúngico tópico (econazol, clotrimazol, nistatina)"]),
  ("Lactante de 9 meses", ["Lesión de 2 semanas en la zona del pañal", "Placa roja brillante en pliegues inguinales y perianal"]),
  {"rotulo": "Tipos de dermatitis del pañal", "eje_x": "Aspecto", "eje_y": "Tipo",
   "cols": ["Pliegues", "Tratamiento"], "rows": ["Irritativa", "Candidiásica", "Seborreica"], "caso": (1, 1),
   "cells": [[("Respetados", ["Zonas convexas"]), ("Óxido de zinc", ["Cambios frecuentes"])],
             [("AFECTADOS", ["Lesiones satélite"]), ("ECONAZOL 1% CREMA", ["o clotrimazol, nistatina"])],
             [("Afectados", ["Escama amarillenta"]), ("Emolientes", ["También cuero cabelludo"])]]},
  ["Una dermatitis irritativa de más de 3 días suele sobreinfectarse con Candida.",
   "Mupirocina es para impétigo (costras melicéricas).",
   "Evitar corticoides potentes en la zona del pañal."],
  "AAP – Diaper dermatitis (Pediatr Rev 2021) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# CIR-063 · puntaje
V("puntaje", "CIR-063", "murphy-aire-pared-vesicular-colecistitis-enfisematosa", "Colecistitis enfisematosa: gravedad",
  "CIRUGÍA ENAM: COLECISTITIS ENFISEMATOSA", "CIRUGÍA",
  ("Colecistitis enfisematosa", ["Gas en la pared de la vesícula por gérmenes anaerobios",
   "Alto riesgo de gangrena y perforación: colecistectomía de emergencia"]),
  ("Varón de 25 años tras comida grasa", ["Dolor en HCD, vómitos, alza térmica · Murphy (++)", "TC: aire en la pared vesicular"]),
  {"rotulo": "Gravedad según Tokio 2018", "escala": "Tokio 2018", "total": 1, "max": 4,
   "total_label": "Criterios de grado II",
   "interpreta": "Colecistitis moderada (grado II)",
   "items": [("Inflamación local marcada (enfisematosa)", "1", True), ("Leucocitos > 18 000", "1", False),
             ("Masa palpable en HCD", "1", False), ("Síntomas > 72 h", "1", False)],
   "bandas": [("0", "Grado I (leve)", "Colecistectomía temprana", False),
              ("≥ 1", "Grado II", "Antibiótico + COLECISTECTOMÍA DE EMERGENCIA", True),
              ("Falla", "Grado III (grave)", "Soporte; drenaje si no tolera cirugía", False)]},
  ["Gérmenes: Clostridium y gramnegativos; cubrir anaerobios.",
   "Más frecuente en varones diabéticos, pero puede verse en jóvenes.",
   "Colecistostomía percutánea solo si el riesgo quirúrgico es prohibitivo."],
  "Tokyo Guidelines – TG18: Diagnostic criteria and severity grading of acute cholecystitis (2018) · WSES – Acute calculous cholecystitis (2020)")

# OFT-029 · termómetro
V("termometro", "OFT-029", "golpe-ojo-futbol-nivel-sangre-camara-hipema", "Hipema traumático",
  "OFTALMOLOGÍA ENAM: HIPEMA", "OFTALMOLOGÍA",
  ("Hipema", ["Sangre en la cámara anterior tras un trauma contuso",
   "Forma un nivel líquido por gravedad"]),
  ("Varón de 18 años golpeado jugando fútbol", ["Dolor, fotofobia, visión borrosa", "Sangre en la cámara anterior con nivel"]),
  {"rotulo": "Grados del hipema",
   "niveles": [("< 1/3", "Grado I", ["Nivel en la cámara"]),
               ("1/3-1/2", "Grado II", ["Más riesgo de resangrado"]),
               ("> 1/2", "Grado III", ["Riesgo de PIO alta"]),
               ("Total", "Grado IV", ["«Bola de ocho»"])],
   "caso_nivel": 0, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "REPOSO Y CABECERA A 30-45°", ["Protector ocular rígido"], True),
             (2, "Ciclopléjico + corticoide tópico", ["Evitar AINE y aspirina"], False),
             (3, "Lavado quirúrgico", ["Si la PIO no cede o grado IV"], False)]},
  ["Riesgo de resangrado entre los días 2 y 5.",
   "Vigilar la presión intraocular.",
   "Descartar drepanocitosis: mayor riesgo de daño del nervio óptico."],
  "AAO – Traumatic hyphema (EyeWiki 2024) · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# CIR-064 · puntaje
V("puntaje", "CIR-064", "escaldadura-brazos-tronco-54-scq-sabana-limpia", "Quemado: superficie corporal",
  "CIRUGÍA ENAM: GRAN QUEMADO", "CIRUGÍA",
  ("Manejo inicial del gran quemado", ["Detener la quemadura y cubrir con sábana limpia y seca",
   "Evitar la hipotermia; calcular la superficie quemada"]),
  ("Varón de 30 años quemado con agua hirviendo", ["2.º grado en ambos brazos y tronco anterior y posterior", "PA 100/70, FC 96"]),
  {"rotulo": "Regla de los 9 en el caso", "escala": "Regla de los 9", "total": 54, "max": 100,
   "total_label": "% de superficie quemada",
   "interpreta": "Gran quemado: 54% de SCQ",
   "items": [("Brazo derecho", "9", True), ("Brazo izquierdo", "9", True),
             ("Tronco anterior", "18", True), ("Tronco posterior", "18", True),
             ("Cabeza y cuello", "9", False), ("Miembros inferiores", "36", False),
             ("Periné", "1", False)],
   "bandas": [("< 20%", "Menor", "Curación y analgesia oral", False),
              ("≥ 20%", "Gran quemado", "Sábana limpia y seca; Parkland y referir", True)]},
  ["Parkland: 4 mL × kg × %SCQ; la mitad en las primeras 8 h.",
   "Apósitos húmedos en áreas extensas causan hipotermia.",
   "Opioides EV, no IM (absorción errática)."],
  "ABA – Advanced Burn Life Support Course (2022) · " + ATLS)

# GIN-119 · termómetro
V("termometro", "GIN-119", "sobrepeso-ganancia-peso-gestacional-7-115-kg", "Ganancia de peso en el embarazo",
  "OBSTETRICIA ENAM: GANANCIA DE PESO GESTACIONAL", "OBSTETRICIA",
  ("Ganancia de peso gestacional (IOM)", ["Depende del IMC antes del embarazo",
   "Sobrepeso (IMC 25-29.9): 7 a 11.5 kg"]),
  ("Pregunta de concepto", ["Gestación única", "Mujer con sobrepeso (IMC 26-29)"]),
  {"rotulo": "IMC pregestacional",
   "niveles": [("< 18.5", "Bajo peso", ["12.5-18 kg"]),
               ("18.5-24.9", "Normal", ["11.5-16 kg"]),
               ("25-29.9", "Sobrepeso", ["7-11.5 kg"]),
               ("≥ 30", "Obesidad", ["5-9 kg"])],
   "caso_nivel": 2, "ruta_titulo": "Control prenatal", "paso_label": "PASO",
   "pasos": [(1, "IMC pregestacional", ["Peso y talla al inicio"], False),
             (2, "GANAR 7-11.5 KG", ["~ 0.28 kg por semana desde el 2.º trimestre"], True),
             (3, "Vigilar en cada control", ["Curva de ganancia de peso"], False)]},
  ["Ganancia excesiva: macrosomía, diabetes gestacional, cesárea.",
   "Ganancia insuficiente: bajo peso al nacer.",
   "Gemelares tienen metas mayores."],
  "IOM – Weight gain during pregnancy: reexamining the guidelines (2009) · MINSA – Guía técnica de valoración nutricional de la gestante")

# CB-042 · puntaje
V("puntaje", "CB-042", "alcoholico-collar-casal-diarrea-demencia-niacina", "Pelagra: las «3 D»",
  "CIENCIAS BÁSICAS ENAM: PELAGRA", "CIENCIAS BÁSICAS",
  ("Pelagra", ["Déficit de niacina (vitamina B3)",
   "Dermatitis fotosensible, diarrea y demencia; sin tratamiento, muerte"]),
  ("Varón de 50 años alcohólico y gastrectomizado", ["Dermatitis en zonas expuestas, collar de Casal", "Diarrea, pérdida de memoria, glositis"]),
  {"rotulo": "Las «4 D» en el caso", "escala": "Pelagra", "total": 3, "max": 4,
   "total_label": "Elementos presentes",
   "interpreta": "Pelagra clásica",
   "items": [("Dermatitis fotosensible (collar de Casal)", "1", True), ("Diarrea", "1", True),
             ("Demencia (pérdida de memoria)", "1", True), ("Muerte (sin tratamiento)", "1", False)],
   "bandas": [("0-1", "Poco probable", "Buscar otra causa", False),
              ("≥ 2", "Pelagra", "NIACINA (nicotinamida) oral", True)]},
  ["Causas: alcoholismo, malabsorción, isoniazida, síndrome carcinoide.",
   "Escorbuto (vitamina C): encías sangrantes, pelos en sacacorchos.",
   "Zinc: acrodermatitis en zonas periorificiales."],
  HARRISON + " · OMS – Pellagra and its prevention and control in major emergencies (2000)")

# NEF-048 · árbol
A("NEF-048", "paraplejico-sonda-anuria-hidronefrosis-cambio-cateter", "Anuria en usuario de sonda vesical",
  "NEFROLOGÍA ENAM: OBSTRUCCIÓN DEL CATÉTER VESICAL", "NEFROLOGÍA",
  ("Anuria en usuario de sonda", ["Lo primero es descartar que la sonda esté obstruida",
   "Cambiar el catéter resuelve la mayoría de casos"]),
  ("Varón de 58 años parapléjico y monorreno", ["Usa catéter vesical · anuria", "Creatinina 3, K 5.8 · hidronefrosis"]),
  Q("¿La sonda drena al irrigarla?", [
      L("No: obstruida", "CAMBIO DE CATÉTER VESICAL", ["Resuelve la obstrucción", "Vigilar poliuria posobstructiva"], path=True),
      L("Sí, sin orina", "Obstrucción alta", ["Nefrostomía percutánea"])], path=True),
  ("Pasos", [("Primero", True), ("Después", False)], [
      ("Acción", ["Cambiar la sonda", "Ecografía de control"]),
      ("Si no drena", ["Lavado vesical", "Nefrostomía"])]),
  ["La litotricia y la cistoscopia no son la urgencia.",
   "Con K 5.8: ECG y control estrecho.",
   "Cambiar el catéter crónico de forma programada."],
  "EAU – Guidelines on neuro-urology (2024) · IDSA – Catheter-associated UTI (2009)")

# GIN-120 · tarjetas
V("tarjetas", "GIN-120", "gestante-6-semanas-acne-retinoides-contraindicados", "Acné en el embarazo",
  "OBSTETRICIA ENAM: RETINOIDES EN EL EMBARAZO", "OBSTETRICIA",
  ("Retinoides en el embarazo", ["Muy teratogénicos: SNC, cara, oído y corazón",
   "Contraindicados durante toda la gestación"]),
  ("Primigesta de 6 semanas con acné", ["Asintomática", "El dermatólogo quiere iniciar retinoides"]),
  {"rotulo": "¿Qué se puede usar?", "ans": 0, "cards": [
      {"titulo": "RETINOIDES", "datos": [
          ("En el embarazo", "Contraindicados", True), ("Riesgo", "Embriopatía grave", True),
          ("Uso", "Nunca en la gestación", True)],
       "pie": "Isotretinoína, tretinoína, adapaleno"},
      {"titulo": "Peróxido de benzoilo", "datos": [
          ("En el embarazo", "Permitido", False), ("Riesgo", "Mínimo", False),
          ("Uso", "Primera línea", False)],
       "pie": "Tópico"},
      {"titulo": "Ácido azelaico", "datos": [
          ("En el embarazo", "Permitido", False), ("Riesgo", "Mínimo", False),
          ("Uso", "Alternativa", False)],
       "pie": "Tópico"},
      {"titulo": "Eritromicina tópica", "datos": [
          ("En el embarazo", "Permitida", False), ("Riesgo", "Mínimo", False),
          ("Uso", "Con peróxido", False)],
       "pie": "Evitar tetraciclinas"}]},
  ["La isotretinoína exige dos métodos anticonceptivos en mujeres fértiles.",
   "Las tetraciclinas tiñen los dientes y afectan el hueso fetal.",
   "No hay una «dosis segura» de retinoides en la gestación."],
  "AAD – Guidelines of care for acne vulgaris (2024) · " + WILLIAMS)

# END-033 · matriz
V("matriz", "END-033", "poliuria-polidipsia-orina-diluida-hipernatremia-diabetes-insipida", "Poliuria: diabetes insípida",
  "ENDOCRINOLOGÍA ENAM: DIABETES INSÍPIDA", "ENDOCRINOLOGÍA",
  ("Diabetes insípida", ["Falta ADH (central) o no actúa en el riñón (nefrogénica)",
   "Poliuria con orina diluida (densidad baja) e hipernatremia"]),
  ("Varón de 20 años con 6 meses de síntomas", ["Poliuria y polidipsia", "Cefalea global"]),
  {"rotulo": "Causas de poliuria acuosa", "eje_x": "Hallazgo", "eje_y": "Causa",
   "cols": ["Orina", "Na sérico", "Desmopresina"], "rows": ["DI central", "DI nefrogénica", "Polidipsia primaria"], "caso": (0, 0),
   "cells": [[("DILUIDA", ["Densidad < 1005"]), ("Alto", ["Hipernatremia"]), ("Concentra", ["Responde"])],
             [("Diluida", []), ("Alto", []), ("No responde", ["Litio, calcio alto"])],
             [("Diluida", []), ("Bajo o normal", ["Bebe en exceso"]), ("Riesgo de hiponatremia", [])]]},
  ["Prueba de restricción hídrica y luego desmopresina.",
   "Cefalea + DI central: buscar tumor hipotálamo-hipofisario (RM).",
   "La copeptina ayuda a diferenciar los tipos."],
  "Endocrine Society – Diagnosis and management of arginine vasopressin deficiency (2023) · " + HARRISON)

# INF-062 · árbol
A("INF-062", "vih-pneumocystis-cotrimoxazol", "Neumonía por Pneumocystis",
  "INFECTOLOGÍA ENAM: NEUMONÍA POR PNEUMOCYSTIS", "INFECTOLOGÍA",
  ("Neumonía por Pneumocystis jirovecii", ["VIH con CD4 < 200: disnea progresiva, tos seca, hipoxemia",
   "Tratamiento de elección: cotrimoxazol por 21 días"]),
  ("Varón de 35 años con VIH", ["Diagnóstico de neumonía por Pneumocystis", "¿Tratamiento inicial?"]),
  Q("¿Alergia a sulfas?", [
      L("No", "COTRIMOXAZOL 21 DÍAS", ["+ prednisona si PaO₂ < 70"], path=True),
      L("Sí", "Primaquina + clindamicina", ["O pentamidina EV"])], path=True),
  ("PCP en VIH", [("Tratamiento", True), ("Profilaxis", False)], [
      ("Fármaco", ["Cotrimoxazol 21 días", "Cotrimoxazol diario"]),
      ("Cuándo", ["Neumonía confirmada", "CD4 < 200"]),
      ("Extra", ["Prednisona si PaO₂ < 70", "Hasta CD4 > 200 por 3 m"])]),
  ["Iniciar TAR dentro de las 2 semanas del tratamiento.",
   "LDH elevada y Rx con infiltrado intersticial bilateral.",
   "Diagnóstico: inmunofluorescencia o PCR en esputo inducido o LBA."],
  "NIH/CDC/IDSA – Guidelines for opportunistic infections in adults with HIV: Pneumocystis (2024)")
