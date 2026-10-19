"""Bloque 7 · parte K."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"

# GIN-206 · árbol
A("GIN-206", "diu-hilos-no-visibles-eco-sin-diu-rx-abdomen", "DIU que no se ve",
  "GINECOLOGÍA ENAM: DIU CON HILOS NO VISIBLES", "GINECOLOGÍA",
  ("Hilos del DIU no visibles", ["Primero ecografía: ¿está en el útero?",
   "Si no está, Rx de abdomen: separa la expulsión de la migración"]),
  ("Usuaria de T de cobre en control", ["No se ven los hilos", "La eco transvaginal no muestra el DIU"]),
  Q("¿La ecografía muestra el DIU en el útero?", [
      L("Sí", "DIU en su lugar", ["Hilos ascendidos: seguir o retirar con pinza"]),
      Q("Rx de abdomen: ¿aparece el DIU?", [
          L("Sí", "Migrado a la cavidad", ["Extraer por laparoscopía"]),
          L("No", "Expulsado", ["Nuevo método anticonceptivo"])],
        edge="No: RX DE ABDOMEN", path=True)], path=True),
  ("DIU no visible", [("Paso", True), ("Qué define", False)], [
      ("1. Ecografía", ["¿Está en el útero?", "Descarta embarazo también"]),
      ("2. Rx de abdomen", ["¿Está en el cuerpo?", "Migrado o expulsado"]),
      ("3. Laparoscopía", ["Si migró", "Extraerlo"])]),
  ["Descartar embarazo con β-hCG.",
   "No asumir la expulsión sin la Rx.",
   "La TC solo si la Rx no aclara la ubicación."],
  "FSRH – Clinical guideline: Intrauterine contraception (2023)")

# NEU-060 · termómetro
V("termometro", "NEU-060", "asmatico-disnea-severa-murmullo-ausente-torax-silente", "Signos de gravedad en la crisis asmática",
  "NEUMOLOGÍA ENAM: CRISIS ASMÁTICA DE RIESGO VITAL", "NEUMOLOGÍA",
  ("Gravedad de la crisis de asma", ["El tórax silente indica que casi no pasa aire",
   "Es signo de riesgo vital, más grave que la taquicardia o la SatO₂ de 91 %"]),
  ("Varón de 27 años asmático", ["Disnea severa a pequeños esfuerzos", "FC 110 · FR 22 · SatO₂ 91 % · murmullo ausente en ambos hemitórax"]),
  {"rotulo": "Nivel de gravedad",
   "niveles": [("Leve", "Leve-moderada", ["Habla en frases", "SatO₂ 90-95 %"]),
               ("Grave", "Grave", ["Habla con palabras, FC > 120"]),
               ("Vital", "Riesgo vital", ["TÓRAX SILENTE", "Cianosis, confusión, agotamiento"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "O₂, SABA + ipratropio continuos", ["Corticoide sistémico"], True),
             (2, "Sulfato de magnesio EV", ["Si no responde"], False),
             (3, "UCI, valorar intubación", ["Agotamiento, PaCO₂ normal o alta"], False)]},
  ["Con tórax silente, la ausencia de sibilancias no es mejoría.",
   "FC 110 y FR 22 aún no son criterios de gravedad por sí solos.",
   "Vigilar la PaCO₂: si sube, el paciente se agota."],
  "GINA – Global Strategy for Asthma Management and Prevention (2025)")

# GIN-207 · árbol
A("GIN-207", "31-semanas-contracciones-cervix-35-mm-fibronectina-negativa", "Contracciones con cuello largo",
  "OBSTETRICIA ENAM: PREDICCIÓN DEL PARTO PRETÉRMINO", "OBSTETRICIA",
  ("Riesgo real de parto pretérmino", ["Cervicometría ≥ 30 mm y fibronectina negativa: riesgo muy bajo",
   "No se tocoliza ni se dan corticoides de rutina"]),
  ("Gestante de 31 semanas", ["Contracciones cada 5 minutos", "Cuello cerrado, 20 %, −4 · cervicometría 35 mm · fibronectina (−)"]),
  Q("¿Cervicometría < 20-25 mm o fibronectina positiva?", [
      L("Sí", "Alto riesgo", ["Corticoides, tocólisis, sulfato de Mg"]),
      L("No: 35 mm y FNf (−)", "OBSERVACIÓN", ["Parto en 7 días < 1 %", "Alta con signos de alarma"], path=True)], path=True),
  ("Pruebas predictoras", [("Resultado del caso", True), ("Significado", False)], [
      ("Cervicometría", ["35 mm", "Cuello largo: bajo riesgo"]),
      ("Fibronectina fetal", ["Negativa", "Alto valor predictivo negativo"])]),
  ["La progesterona y el cerclaje se indican con cuello corto, no en este caso.",
   "Evita hospitalizaciones y fármacos innecesarios.",
   "Buscar infección urinaria como causa de contracciones."],
  "ACOG – Practice Bulletin 234: Prediction and prevention of spontaneous preterm birth (2021)")

# CIR-107 · tarjetas
V("tarjetas", "CIR-107", "golpe-timon-hematoma-pared-duodenal-observacion", "Lesiones del duodeno por trauma",
  "CIRUGÍA ENAM: HEMATOMA DUODENAL", "CIRUGÍA",
  ("Hematoma duodenal", ["Golpe epigástrico (timón, manubrio) contra la columna",
   "En un paciente estable y sin perforación: manejo conservador"]),
  ("Chofer de 24 años, golpe con el timón hace 1 h", ["PA 110/70 · FC 84 · dolor epigástrico", "TC: hematoma de 3 cm en la pared de la 1.ª porción duodenal"]),
  {"rotulo": "¿Qué lesión y qué conducta?", "ans": 0, "cards": [
      {"titulo": "HEMATOMA DUODENAL", "datos": [
          ("Estado", "Estable", True), ("TC", "Hematoma en la pared", True),
          ("Conducta", "Observación continua", True)],
       "pie": "SNG, ayuno, nutrición parenteral"},
      {"titulo": "Perforación duodenal", "datos": [
          ("Estado", "Peritonitis", False), ("TC", "Aire retroperitoneal", False),
          ("Conducta", "Laparotomía", False)],
       "pie": "Reparación primaria"},
      {"titulo": "Lesión pancreática", "datos": [
          ("Estado", "Dolor tardío", False), ("TC", "Laceración, líquido", False),
          ("Conducta", "Según el conducto", False)],
       "pie": "Amilasa alta"},
      {"titulo": "Hemoperitoneo", "datos": [
          ("Estado", "Inestable", False), ("TC", "Líquido libre", False),
          ("Conducta", "Cirugía", False)],
       "pie": "Bazo, hígado"}]},
  ["El hematoma suele resolverse en 1-3 semanas.",
   "Si la obstrucción persiste > 2 semanas: evacuación quirúrgica.",
   "Frecuente en niños por el manubrio de la bicicleta."],
  "EAST – Guideline on duodenal injury management (2019) · " + ATLS)

# SP-152 · radial
V("radial", "SP-152", "piura-peste-roedores-muertos-epizootia", "Términos epidemiológicos",
  "SALUD PÚBLICA ENAM: EPIZOOTIA", "SALUD PÚBLICA",
  ("Epizootia", ["Aumento inusual de una enfermedad en animales",
   "En la peste, la muerte masiva de roedores anuncia casos humanos"]),
  ("Alerta de peste en Piura", ["Un agente comunitario ve muchos roedores muertos", "¿Cómo se notifica?"]),
  {"rotulo": "Mapa del tema", "centro": "TÉRMINOS", "centro_sub": "¿En quién y cuántos?", "ans": 0,
   "items": [("EPIZOOTIA", ["Muchos casos en animales", "Roedores muertos"]),
             ("Epidemia", ["Casos humanos por encima de lo esperado"]),
             ("Brote", ["Epidemia localizada, casos relacionados"]),
             ("Endemia", ["Presencia constante en una zona"]),
             ("Enzootia", ["Presencia constante en animales"])],
   "ruta": ["Alerta de peste", "Roedores muertos", "Enfermedad en animales", "EPIZOOTIA"]},
  ["Tras la muerte de roedores, las pulgas buscan humanos: riesgo alto.",
   "Notificar de inmediato y controlar pulgas antes que roedores.",
   "Piura, Lambayeque y Cajamarca tienen focos de peste."],
  "MINSA – NTS para la vigilancia y control de la peste · OMS – Plague manual (1999)")

# GIN-208 · fases
V("fases", "GIN-208", "au-21-cm-fur-27-semanas-eg-clinica-21", "Altura uterina y edad gestacional",
  "OBSTETRICIA ENAM: ALTURA UTERINA", "OBSTETRICIA",
  ("Altura uterina", ["Entre las 20 y 32 semanas, la altura uterina en cm ≈ semanas de gestación",
   "Si no coincide con la FUR, se sospecha error de fecha o alteración del crecimiento"]),
  ("Mujer de 32 años en su primer control", ["Dice tener 27 semanas por FUR", "AU 21 cm · sintió movimientos por primera vez hace una semana"]),
  {"rotulo": "Dónde está el fondo uterino", "ans": 2,
   "fases": [("12 sem", "Sínfisis", "Se palpa sobre el pubis", []),
             ("16 sem", "Entre pubis y ombligo", "Mitad del camino", []),
             ("20-21 sem", "Ombligo", "AU 21 CM ≈ 21 SEM", ["Coincide con primeros movimientos"]),
             ("36 sem", "Apéndice xifoides", "Máxima altura", []),
             ("40 sem", "Desciende", "Encajamiento", [])],
   "curvas": [("Altura uterina", VIOLET, [0.1, 0.3, 0.5, 0.65, 0.85, 1.0, 0.9])],
   "chips_titulo": "Semanas por clínica · marcadas las correctas",
   "chips": [("21", True), ("25", False), ("27", False), ("17", False)]},
  ["La primípara percibe movimientos hacia las 18-20 semanas.",
   "Confirmar con ecografía y ajustar la FUR si es dudosa.",
   "AU menor para la FUR real: descartar restricción del crecimiento."],
  WILLIAMS)

# GIN-209 · puntaje
V("puntaje", "GIN-209", "41-semanas-oligohidramnios-bishop-2-misoprostol", "Embarazo prolongado con oligohidramnios",
  "OBSTETRICIA ENAM: MADURACIÓN CERVICAL CON MISOPROSTOL", "OBSTETRICIA",
  ("Terminar la gestación", ["41 semanas con oligohidramnios y menos movimientos: no se espera",
   "Cuello desfavorable (Bishop bajo): madurar con misoprostol"]),
  ("Primigesta de 41 semanas 3 días", ["Menos movimientos fetales, oligohidramnios · test estresante negativo", "0 cm, 20 %, −2, consistencia intermedia, posterior"]),
  {"rotulo": "Índice de Bishop en el caso", "escala": "Bishop", "total": 2, "max": 13,
   "total_label": "Puntaje del cuello",
   "interpreta": "Muy desfavorable: madurar primero",
   "items": [("Estación −2", "1", True), ("Consistencia intermedia", "1", True),
             ("Dilatación 0 cm", "0", False), ("Borramiento 20 %", "0", False), ("Posición posterior", "0", False)],
   "bandas": [("≤ 6", "Desfavorable", "Misoprostol 25 µg vaginal", True),
              ("≥ 8", "Favorable", "Oxitocina", False)]},
  ["Test estresante negativo: el feto tolera las contracciones.",
   "Monitoreo fetal continuo durante la maduración.",
   "Esperar el parto espontáneo con oligohidramnios aumenta el riesgo fetal."],
  "ACOG – Practice Bulletin 146: Late-term and postterm pregnancies (2014) · OMS – Inducción del trabajo de parto (2022)")

# HEM-040 · termómetro
V("termometro", "HEM-040", "warfarina-inr-7-hematemesis-plasma-fresco", "Sangrado por warfarina",
  "HEMATOLOGÍA ENAM: REVERSIÓN DE LA WARFARINA", "HEMATOLOGÍA",
  ("Sobreanticoagulación con warfarina", ["La conducta depende del INR y de si hay sangrado",
   "Sangrado importante: revertir ya con plasma (o complejo protrombínico) + vitamina K EV"]),
  ("Varón de 67 años con FA en warfarina", ["Hematemesis desde ayer, más abundante hoy", "Equimosis · INR 7 · Hb 10"]),
  {"rotulo": "INR y sangrado",
   "niveles": [("INR alto", "Sin sangrado", ["Suspender dosis, vigilar"]),
               ("INR > 10", "Sin sangrado", ["Vitamina K oral"]),
               ("Sangrado", "Mayor, cualquier INR", ["HEMATEMESIS + INR 7", "Revertir de inmediato"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Plasma fresco congelado", ["O concentrado de complejo protrombínico"], True),
             (2, "Vitamina K 10 mg EV", ["Efecto en 6-24 h"], False),
             (3, "Endoscopia", ["Buscar y tratar la lesión"], False)]},
  ["La vitamina K sola tarda horas: no basta con sangrado activo.",
   "Las plaquetas no corrigen el efecto de la warfarina.",
   "Transfundir glóbulos rojos solo si Hb < 7-8 o inestabilidad."],
  "ACCP – Antithrombotic therapy guidelines (2012; actualización) · ACC – Expert consensus on management of bleeding on anticoagulants (2020)")

# REU-059 · tarjetas
V("tarjetas", "REU-059", "manchas-hipo-hiperpigmentadas-koh-espagueti-albondigas-malassezia", "Micosis superficiales",
  "DERMATOLOGÍA ENAM: PITIRIASIS VERSICOLOR", "DERMATOLOGÍA",
  ("Pitiriasis versicolor", ["Malassezia, levadura de la piel, prolifera con calor y sudor",
   "KOH: hifas cortas y levaduras en 'espagueti con albóndigas'"]),
  ("Niño de 8 años", ["Máculas hipo e hiperpigmentadas, descamativas, en el tronco", "KOH: hifas anguladas y levaduras (espagueti y albóndigas)"]),
  {"rotulo": "¿Qué hongo es?", "ans": 0, "cards": [
      {"titulo": "MALASSEZIA", "datos": [
          ("Lesión", "Máculas del tronco", True), ("KOH", "Espagueti y albóndigas", True),
          ("Luz de Wood", "Amarillo-verdoso", False), ("Tratamiento", "Ketoconazol, selenio", False)],
       "pie": "Pitiriasis versicolor"},
      {"titulo": "Trichophyton tonsurans", "datos": [
          ("Lesión", "Tiña de la cabeza", False), ("KOH", "Hifas septadas", False),
          ("Luz de Wood", "Negativa", False), ("Tratamiento", "Griseofulvina oral", False)],
       "pie": "Placas alopécicas"},
      {"titulo": "Hortaea werneckii", "datos": [
          ("Lesión", "Mancha negra palmar", False), ("KOH", "Hifas pigmentadas", False),
          ("Luz de Wood", "Negativa", False), ("Tratamiento", "Queratolíticos", False)],
       "pie": "Tiña negra"},
      {"titulo": "Candida albicans", "datos": [
          ("Lesión", "Pliegues, satélites", False), ("KOH", "Seudohifas", False),
          ("Luz de Wood", "Negativa", False), ("Tratamiento", "Nistatina, azoles", False)],
       "pie": "Intertrigo"}]},
  ["Las manchas hipocrómicas pueden tardar meses en repigmentar.",
   "Recurre con frecuencia en clima cálido.",
   "Signo de la uñada: descamación al rascar."],
  "Fitzpatrick's Dermatology 9.ª ed. (2019) · AAD – Tinea versicolor (2023)")

# SP-153 · matriz
V("matriz", "SP-153", "dengue-pacientes-no-atendidos-letalidad-cobertura", "Elementos de la APS",
  "SALUD PÚBLICA ENAM: COBERTURA", "SALUD PÚBLICA",
  ("Cobertura y acceso universal", ["Que toda la población pueda recibir la atención que necesita",
   "Si los pacientes no logran ser atendidos, falla la cobertura"]),
  ("Brote de dengue en varias provincias", ["Muchos pacientes no lograron atención", "Subió la letalidad"]),
  {"rotulo": "Elemento y qué significa", "eje_x": "Rasgo", "eje_y": "Elemento",
   "cols": ["Significa", "¿Falló aquí?"], "rows": ["Cobertura", "Sostenibilidad", "Solidaridad", "Longitudinalidad"], "caso": (0, 1),
   "cells": [[("Todos reciben atención", []), ("SÍ: SIN ATENCIÓN", ["Sube la letalidad"])],
             [("Recursos en el tiempo", []), ("No es lo central", [])],
             [("Aporta quien puede", []), ("No se describe", [])],
             [("Mismo equipo a lo largo del tiempo", []), ("No se describe", [])]]},
  ["Ampliar oferta en brotes: unidades febriles y reorganizar servicios.",
   "La letalidad del dengue baja con atención oportuna.",
   "Cobertura incluye acceso geográfico, económico y cultural."],
  "OPS – La renovación de la APS en las Américas (2007) · OPS – Estrategia para el acceso universal a la salud (2014)")

# CIR-108 · termómetro
V("termometro", "CIR-108", "apendicectomia-fiebre-herida-infectada-drenaje-cultivo", "Infección del sitio quirúrgico",
  "CIRUGÍA ENAM: INFECCIÓN DE HERIDA OPERATORIA", "CIRUGÍA",
  ("Infección del sitio quirúrgico", ["Aparece al 4.º-7.º día: fiebre, dolor, eritema y secreción",
   "El tratamiento principal es abrir y drenar; se cultiva la secreción"]),
  ("Varón de 25 años, 5 días tras apendicectomía abierta", ["Fiebre y dolor en la herida transversa"]),
  {"rotulo": "Profundidad de la infección",
   "niveles": [("Superficial", "Piel y subcutáneo", ["HERIDA DE 5 DÍAS", "Abrir, drenar, cultivar"]),
               ("Profunda", "Fascia y músculo", ["Desbridamiento"]),
               ("Órgano", "Absceso intraabdominal", ["Drenaje percutáneo o cirugía"])],
   "caso_nivel": 0, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Drenaje + cultivo", ["Retirar puntos, lavar, cierre por segunda intención"], True),
             (2, "Antibiótico si hay celulitis", ["O signos sistémicos"], False),
             (3, "Buscar absceso profundo", ["Si la fiebre persiste: ecografía o TC"], False)]},
  ["Los antibióticos sin drenaje no curan la herida infectada.",
   "El lavado quirúrgico en sala es para infecciones profundas.",
   "Prevención: profilaxis antibiótica y técnica aséptica."],
  "CDC – Guideline for prevention of surgical site infection (2017) · IDSA – SSTI guidelines (2014)")

# REU-060 · puntaje
V("puntaje", "REU-060", "poliartritis-manos-anti-ccp-erosiones-artritis-reumatoide", "Poliartritis de manos",
  "REUMATOLOGÍA ENAM: ARTRITIS REUMATOIDE", "REUMATOLOGÍA",
  ("Artritis reumatoide", ["Poliartritis simétrica de pequeñas articulaciones con rigidez matutina",
   "Criterios ACR/EULAR 2010: ≥ 6 puntos"]),
  ("Mujer de 35 años con 4 meses de dolor articular", ["Rigidez matutina · tumefacción de manos y muñecas", "Anti-CCP (+) · ANA (+) · Rx: osteopenia periarticular y erosiones"]),
  {"rotulo": "Criterios ACR/EULAR 2010", "escala": "ACR/EULAR 2010", "total": 6, "max": 10,
   "total_label": "Puntaje del caso",
   "interpreta": "Cumple artritis reumatoide",
   "items": [("4-10 articulaciones pequeñas", "3", True), ("Anti-CCP positivo (título bajo)", "2", True),
             ("Duración ≥ 6 semanas", "1", True), ("PCR o VSG alteradas", "1", False)],
   "bandas": [("< 6", "No clasifica", "Reevaluar en el tiempo", False),
              ("≥ 6", "Artritis reumatoide", "Metotrexato precoz", True)]},
  ["Con erosiones típicas ya se puede clasificar como AR.",
   "El anti-CCP es muy específico (> 95 %).",
   "La artrosis afecta interfalángicas distales y no da erosiones de este tipo."],
  "ACR/EULAR – Rheumatoid arthritis classification criteria (2010) · ACR – RA treatment guideline (2021)")

# PED-197 · matriz
V("matriz", "PED-197", "24-meses-talla-78-peso-10-desnutricion-cronica", "Indicadores antropométricos",
  "PEDIATRÍA ENAM: DESNUTRICIÓN CRÓNICA", "PEDIATRÍA",
  ("Desnutrición crónica", ["Talla para la edad < −2 DE: retraso del crecimiento",
   "El peso para la talla puede ser normal"]),
  ("Niño de 24 meses, prematuro y de bajo peso al nacer", ["Hiporexia, irritabilidad · peso 10 kg, talla 78 cm", "Sin edemas · Hb 10"]),
  {"rotulo": "Indicador y lo que mide", "eje_x": "Rasgo", "eje_y": "Indicador",
   "cols": ["Mide", "En el caso"], "rows": ["Talla para la edad", "Peso para la talla", "Peso para la edad"], "caso": (0, 1),
   "cells": [[("Desnutrición crónica", ["< −2 DE"]), ("78 CM: < −2 DE", ["Mediana ~87 cm"])],
             [("Desnutrición aguda", ["Emaciación"]), ("Normal para 78 cm", [])],
             [("Desnutrición global", []), ("Bajo", ["Por la talla baja"])]]},
  ["Marasmo: emaciación grave; kwashiorkor: edemas.",
   "La desnutrición crónica refleja carencias prolongadas.",
   "Tratar también la anemia (Hb 10)."],
  "OMS – Patrones de crecimiento infantil (2006) · MINSA – NTS 537 (2017)")

# SP-154 · radial
V("radial", "SP-154", "asis-local-analisis-determinantes-sociales", "Componentes del ASIS local",
  "SALUD PÚBLICA ENAM: ANÁLISIS DE SITUACIÓN DE SALUD", "SALUD PÚBLICA",
  ("ASIS local", ["Describe y explica la situación de salud de una población",
   "Incluye el análisis de los determinantes sociales de la salud"]),
  ("Pregunta de salud pública", ["¿Qué componente forma parte del ASIS local?"]),
  {"rotulo": "Mapa del tema", "centro": "ASIS LOCAL", "centro_sub": "Componentes", "ans": 0,
   "items": [("DETERMINANTES SOCIALES", ["Ambientales, económicos, culturales"]),
             ("Problemas de salud", ["Morbilidad y mortalidad"]),
             ("Oferta de servicios", ["Recursos y cobertura"]),
             ("Priorización", ["Problemas y territorios"]),
             ("Participación", ["Actores locales"])],
   "ruta": ["Población local", "¿Qué la enferma?", "Condiciones de vida", "DETERMINANTES SOCIALES"]},
  ["El plan de atención individual y el EEDP son herramientas clínicas, no del ASIS.",
   "La razón de riesgo es una medida, no un componente del ASIS.",
   "El ASIS alimenta el plan local de salud."],
  "MINSA – Documento técnico: Metodología para el análisis de situación de salud local (2015)")

# CB-075 · fases
V("fases", "CB-075", "cicatrizacion-miofibroblastos-actina-miosina", "Fases de la cicatrización",
  "CIENCIAS BÁSICAS ENAM: MIOFIBROBLASTOS", "CIENCIAS BÁSICAS",
  ("Miofibroblastos", ["Fibroblastos que adquieren actina (α-SMA) y miosina",
   "Contraen la herida y reducen su tamaño"]),
  ("Reparación de las heridas", ["¿En qué se diferencian de los fibroblastos?"]),
  {"rotulo": "Fases de la reparación", "ans": 1,
   "fases": [("Inflamatoria", "Días 1-4", "Neutrófilos, macrófagos", ["Limpia la herida"]),
             ("Proliferativa", "Días 4-21", "MIOFIBROBLASTOS", ["Actina y miosina: contracción", "Tejido de granulación"]),
             ("Remodelación", "Semanas-meses", "Colágeno I", ["Gana fuerza"])],
   "curvas": [("Contracción de la herida", ROSE, [0.05, 0.2, 0.6, 0.85, 0.7, 0.5, 0.4])],
   "chips_titulo": "Proteínas que los distinguen · marcadas",
   "chips": [("Actina y miosina", True), ("Desmina y distrofina", False), ("Cromogranina y vimentina", False), ("Citoqueratina", False)]},
  ["Su exceso causa contracturas y cicatrices retráctiles.",
   "La cicatriz alcanza ~80 % de la fuerza original.",
   "Desmina: músculo; citoqueratina: epitelio; cromogranina: neuroendocrino."],
  "Robbins y Cotran. Patología estructural y funcional 10.ª ed. (2021)")

# PED-198 · tarjetas
V("tarjetas", "PED-198", "neonato-holoprosencefalia-polidactilia-labio-leporino-trisomia-13", "Trisomías autosómicas",
  "PEDIATRÍA ENAM: SÍNDROME DE PATAU", "PEDIATRÍA",
  ("Trisomía 13 (Patau)", ["Defectos de la línea media: holoprosencefalia, labio y paladar hendido",
   "Polidactilia, cardiopatía, onfalocele; muy mal pronóstico"]),
  ("Neonato en mal estado y bajo peso", ["Hipotelorismo, polidactilia, onfalocele, labio y paladar hendido", "Soplo · eco prenatal: holoprosencefalia"]),
  {"rotulo": "¿Qué trisomía es?", "ans": 0, "cards": [
      {"titulo": "TRISOMÍA 13", "datos": [
          ("Cara", "Hendiduras, hipotelorismo", True), ("Cerebro", "Holoprosencefalia", True),
          ("Manos", "Polidactilia", True), ("Sobrevida", "Meses", False)],
       "pie": "Síndrome de Patau"},
      {"titulo": "Trisomía 18", "datos": [
          ("Cara", "Micrognatia", False), ("Cerebro", "Retraso grave", False),
          ("Manos", "Puños cerrados", False), ("Sobrevida", "Meses", False)],
       "pie": "Edwards: pies en mecedora"},
      {"titulo": "Trisomía 21", "datos": [
          ("Cara", "Hendiduras oblicuas", False), ("Cerebro", "Discapacidad variable", False),
          ("Manos", "Pliegue único", False), ("Sobrevida", "Adultez", False)],
       "pie": "Down: canal AV"},
      {"titulo": "Trisomía 8", "datos": [
          ("Cara", "Leve", False), ("Cerebro", "Variable", False),
          ("Manos", "Surcos palmares profundos", False), ("Sobrevida", "Normal (mosaico)", False)],
       "pie": "Casi siempre en mosaico"}]},
  ["Confirmar con cariotipo.",
   "Riesgo mayor con edad materna avanzada.",
   "Cuidados paliativos según decisión de la familia."],
  NELSON + " · Thompson & Thompson Genetics in Medicine 8.ª ed. (2016)")

# GIN-210 · árbol
A("GIN-210", "35-semanas-rpm-fiebre-8-cm-antibiotico-parto-vaginal", "Corioamnionitis en trabajo de parto avanzado",
  "OBSTETRICIA ENAM: CORIOAMNIONITIS INTRAPARTO", "OBSTETRICIA",
  ("Corioamnionitis", ["Se tratan con antibióticos y se termina la gestación",
   "La vía la decide la obstetricia: la infección sola no indica cesárea"]),
  ("Segundigesta de 35 semanas", ["RPM de 15 h con fiebre de 38,7 °C · LCF 180", "8 cm, 80 %, +1 · líquido con mal olor"]),
  Q("¿Parto vaginal próximo y sin otra indicación de cesárea?", [
      L("Sí: 8 cm, +1", "ANTIBIÓTICOS + PARTO VAGINAL", ["Ampicilina + gentamicina", "Vigilancia fetal continua"], path=True),
      L("No: lejos del parto o sufrimiento fetal", "Antibióticos + cesárea", ["Agregar clindamicina"])], path=True),
  ("Qué no hacer", [("Evitar", True), ("Motivo", False)], [
      ("Corticoides", ["A las 35 semanas y con infección", "No aportan"]),
      ("Tocolíticos", ["Contraindicados", "Prolongan la infección"]),
      ("Cesárea de rutina", ["Sin indicación obstétrica", "Más riesgo materno"])]),
  ["El RN debe evaluarse por sepsis.",
   "Tras el parto vaginal no se siguen antibióticos de rutina.",
   "Antipiréticos para la fiebre materna."],
  "ACOG – Committee Opinion 712: Intraamniotic infection (2017) · " + WILLIAMS)

# CAR-066 · matriz
V("matriz", "CAR-066", "dea-actividad-electrica-no-desfibrilable-aesp", "Ritmos del paro cardiaco",
  "CARDIOLOGÍA ENAM: ACTIVIDAD ELÉCTRICA SIN PULSO", "CARDIOLOGÍA",
  ("Ritmos de paro", ["Desfibrilables: FV y TV sin pulso",
   "No desfibrilables: asistolia y actividad eléctrica sin pulso (AESP)"]),
  ("Mujer de 71 años que cae de pronto", ["Se inician compresiones", "El DEA muestra actividad eléctrica, pero no indica descarga"]),
  {"rotulo": "Ritmo y conducta", "eje_x": "Rasgo", "eje_y": "Ritmo",
   "cols": ["Monitor", "¿Descarga?"], "rows": ["AESP", "Asistolia", "Fibrilación ventricular", "TV sin pulso"], "caso": (0, 0),
   "cells": [[("ACTIVIDAD ORGANIZADA SIN PULSO", []), ("No", ["RCP + adrenalina"])],
             [("Línea plana", []), ("No", ["RCP + adrenalina"])],
             [("Caótico", []), ("Sí", [])],
             [("QRS ancho regular", []), ("Sí", [])]]},
  ["En la AESP buscar causas reversibles: 5 H y 5 T.",
   "Hipovolemia, hipoxia, taponamiento, neumotórax y TEP son las más frecuentes.",
   "Adrenalina 1 mg cada 3-5 minutos."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2025)")

# SP-155 · tarjetas
V("tarjetas", "SP-155", "control-prenatal-primer-nivel-radar-gestantes", "Herramientas del primer nivel",
  "SALUD PÚBLICA ENAM: RADAR DE GESTANTES", "SALUD PÚBLICA",
  ("Radar de gestantes", ["Registro y mapa de todas las gestantes del ámbito",
   "Permite ubicarlas, clasificar su riesgo y hacer seguimiento"]),
  ("Servicio de control prenatal del primer nivel", ["¿Qué instrumento sirve para vigilar y seguir a las gestantes?"]),
  {"rotulo": "¿Para qué sirve cada herramienta?", "ans": 0, "cards": [
      {"titulo": "RADAR DE GESTANTES", "datos": [
          ("Para", "Seguir a cada gestante", True), ("Quién", "Establecimiento", False),
          ("Uso", "Visitas a inasistentes", True)],
       "pie": "Mapa + padrón nominal"},
      {"titulo": "Claves roja, amarilla, azul", "datos": [
          ("Para", "Emergencias obstétricas", False), ("Quién", "Equipo de guardia", False),
          ("Uso", "Hemorragia, preeclampsia, sepsis", False)],
       "pie": "Kits de acción rápida"},
      {"titulo": "Camino del buen crecimiento", "datos": [
          ("Para", "Niño menor de 5 años", False), ("Quién", "CRED", False),
          ("Uso", "Educación a padres", False)],
       "pie": "No es de gestantes"},
      {"titulo": "Folletos de alarma", "datos": [
          ("Para", "Educar a la gestante", False), ("Quién", "Consultorio", False),
          ("Uso", "Reconocer signos", False)],
       "pie": "No hacen seguimiento"}]},
  ["Se actualiza con cada nueva captación de gestante.",
   "Permite identificar a quienes no acuden a su control.",
   "Articula con agentes comunitarios y casas de espera."],
  "MINSA – NTS 105: Atención integral de salud materna · MINSA – Guía del radar de gestantes")

# OFT-047 · radial
V("radial", "OFT-047", "epistaxis-anterior-causa-rinitis-seca", "Causas de epistaxis anterior",
  "OTORRINOLARINGOLOGÍA ENAM: EPISTAXIS ANTERIOR", "OTORRINOLARINGOLOGÍA",
  ("Epistaxis anterior", ["Más del 90 % de las epistaxis: plexo de Kiesselbach",
   "La causa más frecuente es la sequedad de la mucosa (rinitis seca anterior)"]),
  ("Pregunta de otorrinolaringología", ["¿Causa más frecuente de epistaxis anterior?"]),
  {"rotulo": "Mapa del tema", "centro": "KIESSELBACH", "centro_sub": "Causas", "ans": 0,
   "items": [("RINITIS SECA ANTERIOR", ["Mucosa seca que se fisura", "Aire seco, frío"]),
             ("Trauma digital", ["Rascado, niños"]),
             ("Traumatismo nasal", ["Golpes, fracturas"]),
             ("Perforación septal", ["Cocaína, cirugía"]),
             ("Barotrauma", ["Buceo, vuelos"])],
   "ruta": ["Mucosa anterior seca", "Costras y fisuras", "Rotura de vasos", "RINITIS SECA"]},
  ["Manejo: comprimir las alas nasales 10-15 minutos con la cabeza hacia adelante.",
   "Prevención: humidificar y lubricar la mucosa.",
   "Recurrente y unilateral en adolescente varón: descartar angiofibroma."],
  "AAO-HNS – Clinical practice guideline: Nosebleed (2020)")

# PED-199 · fases
V("fases", "PED-199", "nina-sibilancias-desde-4-anos-atopia-inicio-tardio", "Fenotipos de sibilancias (Tucson)",
  "PEDIATRÍA ENAM: SIBILANCIAS DE INICIO TARDÍO", "PEDIATRÍA",
  ("Fenotipos de sibilancias", ["Se clasifican por la edad de inicio y si persisten",
   "Inicio tardío (después de los 3 años) + atopia = mayor probabilidad de asma"]),
  ("Niña de 6 años", ["Sibilancias recurrentes desde los 4 años", "Dermatitis atópica · mejora con salbutamol · prick (+) a ácaros"]),
  {"rotulo": "Edad de las sibilancias", "ans": 2,
   "fases": [("Transitorio", "0-3 años", "Precoces", ["Desaparecen hacia los 6", "Pulmón pequeño, tabaco materno"]),
             ("Persistente", "Antes de 3 y siguen", "Precoz persistente", ["Mayor riesgo de asma"]),
             ("Tardío", "Después de 3 años", "INICIO TARDÍO", ["Atopia, ácaros", "Asma alérgica"])],
   "curvas": [("Transitorio", SKY, [0.8, 0.6, 0.3, 0.1, 0.05, 0.0, 0.0]),
              ("Tardío", ROSE, [0.0, 0.0, 0.1, 0.4, 0.7, 0.85, 0.9])],
   "chips_titulo": "Fenotipo del caso · marcado el correcto",
   "chips": [("Inicio tardío", True), ("Transitorio precoz", False), ("Persistente", False), ("Inicio intermedio", False)]},
  ["La atopia personal o familiar predice asma.",
   "Tratamiento de control: corticoide inhalado.",
   "Controlar el ambiente: ácaros en colchones y peluches."],
  "Martinez FD et al. – Tucson Children's Respiratory Study (NEJM 1995) · GINA (2025)")

# GIN-211 · fases
V("fases", "GIN-211", "preeclampsia-severa-sulfato-magnesio-24-h-posparto", "Duración del sulfato de magnesio",
  "OBSTETRICIA ENAM: SULFATO DE MAGNESIO", "OBSTETRICIA",
  ("Sulfato de magnesio", ["Previene la eclampsia en la preeclampsia con criterios de severidad",
   "El riesgo sigue tras el parto: se mantiene 24 horas posparto"]),
  ("Puérpera inmediata", ["Preeclampsia con criterios de severidad", "Recibe sulfato de magnesio"]),
  {"rotulo": "Cuándo se da", "ans": 2,
   "fases": [("Diagnóstico", "Anteparto", "Dosis de carga", ["4-6 g EV en 20 min"]),
             ("Parto", "Intraparto", "Mantenimiento", ["1-2 g/h"]),
             ("Posparto", "Primeras 24 h", "CONTINUAR 24 H", ["Riesgo de eclampsia"]),
             ("Suspender", "Tras 24 h", "Vigilar PA", ["Control de síntomas"])],
   "curvas": [("Riesgo de convulsión", ROSE, [0.5, 0.65, 0.8, 0.6, 0.35, 0.15, 0.1])],
   "chips_titulo": "Hasta cuándo · marcado el correcto",
   "chips": [("24 h después del parto", True), ("Al terminar el parto", False), ("72 h posparto", False), ("24 h del diagnóstico", False)]},
  ["Vigilar reflejos, diuresis y frecuencia respiratoria.",
   "Antídoto: gluconato de calcio 1 g EV.",
   "Un tercio de las eclampsias ocurre en el posparto."],
  "ACOG – Practice Bulletin 222 (2020) · MINSA – Guía de trastornos hipertensivos del embarazo")

# NEU-061 · matriz
V("matriz", "NEU-061", "tratamiento-tb-fiebre-escalofrios-mialgia-rifampicina", "Efectos adversos del esquema antituberculoso",
  "NEUMOLOGÍA ENAM: SÍNDROME PSEUDOGRIPAL POR RIFAMPICINA", "NEUMOLOGÍA",
  ("Síndrome pseudogripal", ["Reacción inmune a la rifampicina, más con dosis intermitentes",
   "Fiebre, escalofríos, mialgias y malestar"]),
  ("Varón de 48 años", ["Un mes de tratamiento antituberculoso", "Fiebre, escalofríos y mialgias"]),
  {"rotulo": "Fármaco y efecto típico", "eje_x": "Rasgo", "eje_y": "Fármaco",
   "cols": ["Efecto adverso", "Clave"], "rows": ["Rifampicina", "Isoniacida", "Pirazinamida", "Etambutol"], "caso": (0, 0),
   "cells": [[("PSEUDOGRIPAL", ["Fiebre, mialgias"]), ("Orina naranja", ["Interacciones"])],
             [("Neuropatía, hepatitis", []), ("Piridoxina", [])],
             [("Gota, hepatitis", []), ("Ácido úrico alto", [])],
             [("Neuritis óptica", []), ("Colores rojo-verde", [])]]},
  ["Descartar TB resistente o infección concomitante.",
   "Si es grave, puede acompañarse de trombocitopenia o falla renal: suspender.",
   "Reportar la reacción adversa a farmacovigilancia."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · OMS – TB drug-resistant and adverse events (2024)")

# PED-200 · puntaje
V("puntaje", "PED-200", "lactante-2-meses-bronquiolitis-tirajes-hospitalizar", "Bronquiolitis: ¿casa u hospital?",
  "PEDIATRÍA ENAM: BRONQUIOLITIS", "PEDIATRÍA",
  ("Bronquiolitis", ["Primer episodio de sibilancias por virus (VSR) en menores de 2 años",
   "El tratamiento es de soporte: hidratar, oxígeno si falta y vigilar"]),
  ("Lactante de 2 meses", ["4 días de congestión nasal y tos", "SatO₂ 97 % · aleteo, tirajes subcostales e intercostales · sibilantes"]),
  {"rotulo": "Criterios de hospitalización", "escala": "Criterios del caso", "total": 2, "max": 5,
   "total_label": "Criterios presentes",
   "interpreta": "Hospitalizar para vigilar e hidratar",
   "items": [("Edad < 3 meses", "✓", True), ("Dificultad respiratoria (tirajes, aleteo)", "✓", True),
             ("SatO₂ < 92 %", "—", False), ("Apneas", "—", False), ("No puede alimentarse", "—", False)],
   "bandas": [("0", "Leve", "Manejo en casa con signos de alarma", False),
              ("≥ 1", "Moderada-grave", "Hospitalizar: monitoreo e hidratación", True)]},
  ["Salbutamol y corticoides no se recomiendan en la bronquiolitis.",
   "Antibióticos solo si hay infección bacteriana demostrada.",
   "Aspiración nasal y posición semisentada."],
  "AAP – Clinical practice guideline: bronchiolitis (2014) · NICE NG9 (2021)")

# END-060 · embudo
V("embudo", "END-060", "trabajo-uci-sin-sol-calcio-fosforo-bajos-fa-alta-vitamina-d", "Dolor óseo con debilidad proximal",
  "ENDOCRINOLOGÍA ENAM: OSTEOMALACIA", "ENDOCRINOLOGÍA",
  ("Osteomalacia", ["Falta de vitamina D: el hueso no se mineraliza",
   "Calcio y fósforo bajos, fosfatasa alcalina y PTH altas"]),
  ("Enfermero de 34 años con jornadas largas en UCI", ["Dolores óseos y debilidad proximal crecientes", "Ca y P bajos · FA alta · PTH 100 · osteopenia"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dolor óseo con laboratorio alterado",
   "candidatos": ["Osteomalacia", "Osteoporosis", "Hiperparatiroidismo primario", "Miopatía"],
   "pasos": [("Calcio bajo (no alto)", ["Hiperparatiroidismo primario"]),
             ("Fosfatasa alcalina alta y fósforo bajo", ["Osteoporosis", "Miopatía"])],
   "final": ("OSTEOMALACIA: VITAMINA D", ["Colecalciferol + calcio", "Exposición solar"]),
   "nota": "En la osteoporosis el calcio, el fósforo y la fosfatasa alcalina son normales."},
  ["La PTH sube de forma secundaria para compensar el calcio bajo.",
   "Rx: pseudofracturas (zonas de Looser).",
   "Poca exposición solar es la causa más común."],
  "Endocrine Society – Vitamin D guideline (2024) · " + HARRISON)

# NEU-062 · termómetro
V("termometro", "NEU-062", "neumonia-confusa-fr-28-ceftriaxona-azitromicina", "Antibiótico según dónde se trata la neumonía",
  "NEUMOLOGÍA ENAM: TRATAMIENTO DE LA NEUMONÍA COMUNITARIA", "NEUMOLOGÍA",
  ("Neumonía adquirida en la comunidad", ["El esquema depende de la gravedad y el lugar de tratamiento",
   "Hospitalizada: betalactámico + macrólido"]),
  ("Mujer de 53 años", ["2 días de tos amarilla y fiebre · confusa", "FR 28 · SatO₂ 94 % · opacidad basal izquierda · desviación izquierda"]),
  {"rotulo": "Lugar de tratamiento",
   "niveles": [("Casa", "Ambulatoria", ["Amoxicilina o macrólido"]),
               ("Sala", "Hospitalizada", ["CONFUSA: HOSPITALIZAR", "Ceftriaxona + azitromicina"]),
               ("UCI", "Grave", ["Ceftriaxona + azitromicina o levofloxacino"])],
   "caso_nivel": 1, "ruta_titulo": "Esquema", "paso_label": "PASO",
   "pasos": [(1, "Ceftriaxona + azitromicina", ["Cubre neumococo y atípicos"], True),
             (2, "Alternativa: levofloxacino", ["Si hay alergia a betalactámicos"], False),
             (3, "Cubrir Pseudomonas o SARM", ["Solo con factores de riesgo"], False)]},
  ["Meropenem y vancomicina se reservan para riesgo de gérmenes resistentes.",
   "La confusión es un criterio de gravedad (CURB-65).",
   "Pasar a vía oral cuando esté estable."],
  "ATS/IDSA – Diagnosis and treatment of adults with community-acquired pneumonia (2019)")

# CIR-109 · embudo
V("embudo", "CIR-109", "colecistectomia-24-h-fiebre-rebote-peritonitis-biliar", "Abdomen agudo tras la colecistectomía",
  "CIRUGÍA ENAM: PERITONITIS BILIAR", "CIRUGÍA",
  ("Peritonitis biliar posoperatoria", ["Fuga de bilis (conducto cístico o lecho) al peritoneo",
   "Dolor, contractura, rebote y sepsis en las primeras horas o días"]),
  ("Mujer de 60 años colecistectomizada hace 24 h", ["Dolor y contractura abdominal, rebote (+)", "T 39 °C · PA 90/60 · FC 100 · leucocitos 14 000"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Fiebre y dolor el día después de la cirugía",
   "candidatos": ["Peritonitis biliar", "Colangitis", "Neumonía basal", "Pancreatitis"],
   "pasos": [("Signos peritoneales: contractura y rebote", ["Neumonía basal"]),
             ("Sin ictericia ni triada de Charcot", ["Colangitis"]),
             ("Tras cirugía de vesícula, sin cálculo en la vía", ["Pancreatitis"])],
   "final": ("PERITONITIS BILIAR", ["Reanimación y antibióticos", "Ecografía o TC, drenaje y control de la fuga"]),
   "nota": "Una fuga pequeña se trata con drenaje + CPRE con stent; la peritonitis difusa, con cirugía."},
  ["Fuga del muñón cístico: la causa más frecuente.",
   "Descartar lesión de la vía biliar.",
   "La sepsis abdominal requiere control del foco."],
  "WSES – Guidelines for bile duct injury (2020) · Tokyo Guidelines (2018)")

# PED-201 · puntaje
V("puntaje", "PED-201", "nino-7-anos-dolor-migra-fid-rebote-leucocitosis-apendicitis", "Dolor abdominal en el escolar",
  "PEDIATRÍA ENAM: APENDICITIS AGUDA", "PEDIATRÍA",
  ("Apendicitis en el niño", ["Dolor periumbilical que migra a FID, anorexia, vómitos y fiebre",
   "El Pediatric Appendicitis Score (PAS) estima la probabilidad"]),
  ("Niño de 7 años con 8 horas de dolor", ["Fiebre 38,5 °C, hiporexia, náuseas y vómitos", "Dolor que migra a FID, rebote (+) · leucocitos 12 000, PMN 8500"]),
  {"rotulo": "Pediatric Appendicitis Score", "escala": "PAS", "total": 8, "max": 10,
   "total_label": "Puntaje del caso",
   "interpreta": "Alta probabilidad: apendicitis",
   "items": [("Dolor en FID a la palpación", "2", True), ("Migración del dolor", "1", True),
             ("Anorexia", "1", True), ("Náuseas o vómitos", "1", True), ("Fiebre ≥ 38 °C", "1", True),
             ("Leucocitos > 10 000", "1", True), ("Neutrófilos > 7500", "1", True),
             ("Dolor en FID al toser o saltar", "2", False)],
   "bandas": [("≤ 3", "Baja", "Observar, otra causa", False),
              ("4-6", "Intermedia", "Ecografía", False),
              ("≥ 7", "Alta", "Cirujano pediatra", True)]},
  ["Adenitis mesentérica: fiebre, virosis previa, dolor más difuso.",
   "En varones descartar torsión testicular.",
   "La ecografía es el primer estudio de imagen en niños."],
  "Samuel M (J Pediatr Surg 2002) · WSES – Jerusalem guidelines (2020)")

# CIR-110 · puntaje
V("puntaje", "CIR-110", "explosion-cocina-voz-ronca-esputo-carbonaceo-intubacion", "Quemadura de la vía aérea",
  "CIRUGÍA ENAM: LESIÓN POR INHALACIÓN", "CIRUGÍA",
  ("Lesión por inhalación", ["El edema de la vía aérea progresa en horas y puede cerrarla",
   "Con signos de inhalación y dificultad respiratoria: intubar temprano"]),
  ("Varón de 37 años, explosión en la cocina hace 10 h", ["Voz ronca, esputo negruzco, dificultad respiratoria", "FR 34 · SatO₂ 92 % · vibrisas quemadas, edema orofaríngeo con hollín"]),
  {"rotulo": "Signos de lesión por inhalación", "escala": "Signos del caso", "total": 6, "max": 7,
   "total_label": "Signos presentes",
   "interpreta": "Riesgo de obstrucción: intubar ya",
   "items": [("Ronquera o cambio de voz", "✓", True), ("Esputo carbonáceo", "✓", True),
             ("Vibrisas nasales quemadas", "✓", True), ("Edema y hollín en orofaringe", "✓", True),
             ("Dificultad respiratoria (FR 34)", "✓", True), ("Explosión en espacio cerrado", "✓", True),
             ("Estridor", "—", False)],
   "bandas": [("Leve", "Sin compromiso", "O₂ humidificado y vigilar", False),
              ("Signos + disnea", "Vía aérea en riesgo", "Intubación endotraqueal temprana", True)]},
  ["Usar un tubo grueso: después será difícil de intubar.",
   "Medir carboxihemoglobina y pensar en cianuro.",
   "Los corticoides no previenen el edema."],
  ATLS + " · ABA – Advanced Burn Life Support (2022)")

# GIN-212 · matriz
V("matriz", "GIN-212", "pelvimetria-conjugado-10-5-pelvis-estrecha-cesarea", "Pelvimetría clínica",
  "OBSTETRICIA ENAM: DESPROPORCIÓN POR PELVIS ESTRECHA", "OBSTETRICIA",
  ("Pelvimetría clínica", ["Evalúa si la pelvis permite el paso del feto",
   "Conjugado diagonal < 11,5 cm = estrechez del estrecho superior"]),
  ("Gestante de 39 semanas con contracciones", ["0 cm, 0 %, −4 · cabeza sin encajar", "Conjugado diagonal 10,5 · biciático 10 · biisquiático 8 · ángulo > 90°"]),
  {"rotulo": "Diámetro, normal y caso", "eje_x": "Rasgo", "eje_y": "Diámetro",
   "cols": ["Normal", "Caso"], "rows": ["Conjugado diagonal", "Biciático", "Biisquiático", "Ángulo subpúbico"], "caso": (0, 1),
   "cells": [[("≥ 11,5-12 cm", ["Estrecho superior"]), ("10,5 CM: ESTRECHO", ["Cabeza no encaja"])],
             [("≥ 10 cm", ["Estrecho medio"]), ("10 cm: límite", [])],
             [("≥ 8 cm", ["Estrecho inferior"]), ("8 cm: normal", [])],
             [("≥ 90°", []), ("> 90°: normal", [])]]},
  ["Estrecho superior reducido: el feto no puede descender → cesárea.",
   "La inducción o maduración no corrige una pelvis estrecha.",
   "Presentación en −4 a término en una primigesta es signo de alerta."],
  WILLIAMS)

# PSI-040 · árbol
A("PSI-040", "nino-humillado-insultado-por-padre-comunicar-autoridad", "Maltrato psicológico infantil",
  "PSIQUIATRÍA ENAM: MALTRATO INFANTIL", "PSIQUIATRÍA",
  ("Maltrato psicológico", ["Humillar, insultar y culpar de forma repetida es violencia",
   "El médico tiene la obligación legal de comunicarlo a la autoridad"]),
  ("Niño de 8 años traído por su tía por cefalea", ["Facies triste", "El padre lo culpa, lo humilla y lo insulta; la madre se fue hace un año"]),
  Q("¿Hay sospecha de maltrato?", [
      L("Sí", "INFORMAR A LA AUTORIDAD", ["DEMUNA, Fiscalía o Policía", "Registrar en la historia"], path=True),
      L("No", "Seguimiento habitual", ["Orientación a la familia"])], path=True),
  ("Después de comunicar", [("Acción", True), ("Quién", False)], [
      ("Protección", ["Medidas para el niño", "Autoridad competente"]),
      ("Salud mental", ["Evaluación y terapia", "Psicología"]),
      ("Apoyo social", ["Red familiar", "Asistencia social"])]),
  ["Hablar con el padre no reemplaza la comunicación a la autoridad.",
   "La interconsulta a psicología es complementaria.",
   "Indagar también por maltrato físico o sexual."],
  "Código de los Niños y Adolescentes (Ley 27337) · Ley N.° 30364 · MINSA – Guía técnica de atención integral del maltrato infantil")

# NEF-082 · embudo
V("embudo", "NEF-082", "colico-renal-previo-globo-vesical-oliguria-posrenal", "Falla renal con masa en hipogastrio",
  "UROLOGÍA ENAM: LESIÓN RENAL AGUDA POSRENAL", "UROLOGÍA",
  ("Lesión renal aguda posrenal", ["Obstrucción de la salida de la orina",
   "Globo vesical, oliguria y creatinina que sube"]),
  ("Varón de 24 años", ["Hace 3 días cólico lumbar derecho a testículo con hematuria", "Hoy dolor suprapúbico, poca orina, masa en hipogastrio · Cr 2,8 · K 5,6"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Lesión renal aguda en un joven",
   "candidatos": ["Posrenal", "Prerrenal", "Renal intrínseca"],
   "pasos": [("Sin pérdidas de volumen ni hipotensión", ["Prerrenal"]),
             ("Globo vesical tras un cólico: obstrucción", ["Renal intrínseca"])],
   "final": ("LESIÓN RENAL POSRENAL", ["Sonda vesical inmediata", "Ecografía: cálculo en uretra o vejiga"]),
   "nota": "Tras desobstruir puede haber poliuria: vigilar líquidos y potasio."},
  ["La masa hipogástrica es la vejiga distendida (globo).",
   "Una obstrucción unilateral no causa falla si el otro riñón es normal.",
   "Corregir rápido evita el daño renal permanente."],
  "KDIGO – AKI guideline (2012) · EAU – Guidelines on urolithiasis (2025)")

# REU-061 · puntaje
V("puntaje", "REU-061", "debilidad-proximal-gottron-cpk-34000-biopsia-muscular", "Debilidad proximal con lesiones en los dedos",
  "REUMATOLOGÍA ENAM: DERMATOMIOSITIS", "REUMATOLOGÍA",
  ("Dermatomiositis", ["Miopatía inflamatoria con lesiones cutáneas típicas",
   "Pápulas de Gottron, heliotropo; la biopsia muscular confirma"]),
  ("Mujer de 40 años con 3 meses de debilidad", ["No puede levantarse de la silla ni subir al micro", "Pápulas eritematosas en el dorso de los dedos · dolor muscular · CPK 34 000"]),
  {"rotulo": "Criterios de Bohan y Peter", "escala": "Bohan y Peter", "total": 3, "max": 5,
   "total_label": "Criterios presentes",
   "interpreta": "Probable: confirmar con biopsia",
   "items": [("Lesiones cutáneas (Gottron)", "✓", True), ("Debilidad proximal simétrica", "✓", True),
             ("CPK elevada", "✓", True), ("EMG miopática", "?", False), ("Biopsia muscular compatible", "?", False)],
   "bandas": [("Piel + 2", "Probable", "Biopsia muscular", True),
              ("Piel + 3", "Definida", "Corticoides e inmunosupresor", False)]},
  ["Buscar cáncer en adultos (ovario, pulmón, digestivo).",
   "La RM guía el sitio de la biopsia.",
   "Tratamiento: prednisona + metotrexato o azatioprina."],
  "Bohan A, Peter JB (NEJM 1975) · EULAR/ACR – Classification criteria for IIM (2017)")

# CIR-111 · termómetro
V("termometro", "CIR-111", "trauma-cerrado-hipotension-jobert-peritonitis-laparotomia", "Trauma abdominal cerrado con peritonitis",
  "CIRUGÍA ENAM: LAPAROTOMÍA EN EL TRAUMA CERRADO", "CIRUGÍA",
  ("Indicaciones de laparotomía", ["Peritonitis, neumoperitoneo o inestabilidad = cirugía",
   "Signo de Jobert: timpanismo en área hepática por aire libre"]),
  ("Chofer de 50 años, accidente hace 6 h", ["PA 90/50 · FC 100 · equimosis en abdomen superior", "Dolor epigástrico, RHA disminuidos, Jobert (+), reacción peritoneal"]),
  {"rotulo": "Situación del paciente",
   "niveles": [("Estable", "Sin peritonitis", ["TC con contraste"]),
               ("Dudoso", "Hallazgos equívocos", ["FAST, observación seriada"]),
               ("Quirúrgico", "Peritonitis o aire libre", ["JOBERT + PERITONITIS", "Hipotenso"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Laparotomía exploradora", ["Reparar la víscera perforada"], True),
             (2, "Reanimación en paralelo", ["2 vías, cristaloide limitado, sangre"], False),
             (3, "Antibióticos", ["Cubrir flora intestinal"], False)]},
  ["La ecografía o la RM retrasan una cirugía ya indicada.",
   "El lavado peritoneal diagnóstico casi no se usa hoy.",
   "Cinturón de seguridad: lesiones de intestino y mesenterio."],
  ATLS)

# OFT-048 · fases
V("fases", "OFT-048", "prematura-32-semanas-oxigeno-retinopatia-primer-examen-4-semanas", "Tamizaje de retinopatía del prematuro",
  "OFTALMOLOGÍA ENAM: RETINOPATÍA DEL PREMATURO", "OFTALMOLOGÍA",
  ("Retinopatía del prematuro", ["Vascularización anormal de la retina inmadura; el oxígeno la favorece",
   "Primer fondo de ojo a las 4 semanas de vida (o 31 semanas corregidas)"]),
  ("Recién nacida de 32 semanas", ["Ventilación mecánica con FiO₂ 40 % varios días", "Riesgo de retinopatía"]),
  {"rotulo": "Calendario del tamizaje", "ans": 1,
   "fases": [("Nacimiento", "Semana 0", "Identificar riesgo", ["≤ 1500 g, ≤ 30 sem o curso inestable"]),
             ("4 semanas", "Primer examen", "FONDO DE OJO", ["Con midriasis"]),
             ("Seguimiento", "Cada 1-2 sem", "Según hallazgos", ["Hasta vascularizar"]),
             ("Tratamiento", "Si hay enfermedad", "Láser o anti-VEGF", ["En 48-72 h"])],
   "curvas": [],
   "chips_titulo": "Primer examen · marcado el correcto",
   "chips": [("4 semanas", True), ("2 semanas", False), ("8 semanas", False), ("10 semanas", False)]},
  ["Controlar la saturación objetivo evita el exceso de oxígeno.",
   "Es una causa prevenible de ceguera infantil.",
   "El examen lo hace un oftalmólogo entrenado."],
  "AAP/AAO – Screening examination of premature infants for ROP (Pediatrics 2018) · MINSA – GPC de retinopatía de la prematuridad")

# PED-202 · embudo
V("embudo", "PED-202", "nino-4-anos-acianotico-segundo-ruido-desdoblado-fijo-cia", "Desdoblamiento fijo del segundo ruido",
  "PEDIATRÍA ENAM: COMUNICACIÓN INTERAURICULAR", "PEDIATRÍA",
  ("Comunicación interauricular", ["Acianótica, a menudo asintomática en la infancia",
   "Signo clave: desdoblamiento fijo del segundo ruido"]),
  ("Niño de 4 años en control de niño sano", ["Peso y talla en percentil 75, acianótico", "Segundo ruido desdoblado y fijo"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hallazgo cardiaco en un niño sano",
   "candidatos": ["CIA", "Fallot", "Transposición", "Atresia pulmonar"],
   "pasos": [("Acianótico, buen crecimiento", ["Fallot", "Transposición", "Atresia pulmonar"])],
   "final": ("COMUNICACIÓN INTERAURICULAR", ["Ecocardiograma", "Cierre con dispositivo o cirugía si es grande"]),
   "nota": "El flujo extra por la aurícula derecha retrasa el cierre pulmonar en todo el ciclo: el desdoblamiento no varía con la respiración."},
  ["Suele haber un soplo sistólico suave en foco pulmonar.",
   "Ostium secundum es el tipo más frecuente.",
   "Sin tratar puede dar hipertensión pulmonar en la adultez."],
  NELSON + " · AHA/ACC – Guideline for adults with congenital heart disease (2018)")
