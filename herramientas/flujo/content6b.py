"""Bloque 6 · parte B."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"

# PED-095 · embudo
V("embudo", "PED-095", "neonato-pulsos-femorales-debiles-coartacion", "Pulsos femorales débiles en el neonato",
  "PEDIATRÍA ENAM: COARTACIÓN DE AORTA", "PEDIATRÍA",
  ("Coartación de aorta", ["Estrechez de la aorta, casi siempre junto al ductus",
   "Pulsos femorales débiles o retrasados frente a los del brazo derecho"]),
  ("Neonato de 18 horas, activo y rosado", ["Ruidos cardiacos normales", "Pulsos femorales más débiles que el braquial derecho"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Neonato con diferencia de pulsos",
   "candidatos": ["Coartación de aorta", "VI hipoplásico", "CIV", "CIA", "PCA"],
   "pasos": [("Pulsos femorales menores que los braquiales", ["CIV", "CIA", "PCA"]),
             ("Rosado, activo y bien perfundido", ["VI hipoplásico"])],
   "final": ("COARTACIÓN DE AORTA", ["Medir PA en 4 extremidades", "Ecocardiograma; PGE1 si hay choque"]),
   "nota": "Puede pasar inadvertida hasta que se cierra el ductus: se presenta con choque a los 7-10 días."},
  ["Diferencia de PA sistólica brazo-pierna > 10 mmHg apoya el diagnóstico.",
   "Se asocia a válvula aórtica bicúspide y síndrome de Turner.",
   "Tratamiento: angioplastia o resección con anastomosis."],
  "AHA – Neonatal and pediatric congenital heart disease statement (2023) · " + NELSON)

# PED-096 · termómetro
V("termometro", "PED-096", "neonato-pletorico-hto-70-exanguinotransfusion", "Policitemia neonatal",
  "PEDIATRÍA ENAM: POLICITEMIA NEONATAL", "PEDIATRÍA",
  ("Policitemia neonatal", ["Hematocrito venoso ≥ 65%: la sangre se vuelve viscosa",
   "Letargia, mala succión, plétora e hipoglucemia son síntomas de hiperviscosidad"]),
  ("RN de 6 horas pletórico y letárgico", ["Mala succión · piel apergaminada", "Hematocrito 70%"]),
  {"rotulo": "Hematocrito venoso",
   "niveles": [("< 65%", "Normal", ["Sin intervención"]),
               ("65-70%", "Asintomática", ["Hidratar y controlar"]),
               ("≥ 65% sínt.", "Sintomática", ["EXANGUINOTRANSFUSIÓN", "Parcial con suero salino"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "EXANGUINOTRANSFUSIÓN PARCIAL", ["Reemplazar sangre por suero salino"], True),
             (2, "Controlar glucosa", ["La hipoglucemia es frecuente"], False),
             (3, "Vigilar ictericia y enterocolitis", ["Complicaciones"], False)]},
  ["Causas: hijo de madre diabética, restricción del crecimiento, transfusión feto-fetal, pinzamiento tardío.",
   "Volumen a recambiar = volemia × (Hto real − Hto deseado) / Hto real.",
   "La hidratación sola no corrige la hiperviscosidad sintomática."],
  NELSON + " · Cloherty and Stark's Manual of Neonatal Care 9.ª ed. (2023)")

# END-022 · tarjetas
V("tarjetas", "END-022", "hipertiroidismo-mujer-joven-metimazol", "Tratamiento del hipertiroidismo",
  "ENDOCRINOLOGÍA ENAM: HIPERTIROIDISMO", "ENDOCRINOLOGÍA",
  ("Tratamiento del hipertiroidismo", ["TSH baja y T4 libre alta = hipertiroidismo primario",
   "Primera elección: metimazol (+ betabloqueante para los síntomas)"]),
  ("Mujer de 25 años con pérdida de peso y calor", ["Temblor, taquicardia, amenorrea", "TSH baja · T4 libre alta · β-hCG negativa"]),
  {"rotulo": "¿Qué tratamiento?", "ans": 0, "cards": [
      {"titulo": "METIMAZOL", "datos": [
          ("Uso", "Primera elección", True), ("Cuándo", "Casi todos los casos", True),
          ("Riesgo", "Agranulocitosis", False)],
       "pie": "+ propranolol para síntomas"},
      {"titulo": "Propiltiouracilo", "datos": [
          ("Uso", "Alternativa", False), ("Cuándo", "1.er trimestre, tormenta", False),
          ("Riesgo", "Hepatotoxicidad", False)],
       "pie": "Bloquea T4 → T3"},
      {"titulo": "Yodo radiactivo", "datos": [
          ("Uso", "Definitivo", False), ("Cuándo", "Recaída, bocio nodular", False),
          ("Riesgo", "Hipotiroidismo", False)],
       "pie": "Contraindicado en embarazo"},
      {"titulo": "Tiroidectomía", "datos": [
          ("Uso", "Definitivo", False), ("Cuándo", "Bocio grande, sospecha de cáncer", False),
          ("Riesgo", "Hipocalcemia, recurrente", False)],
       "pie": "Tras eutiroidismo"}]},
  ["Levotiroxina es para el hipotiroidismo; corticoides solo en tormenta u oftalmopatía.",
   "Pedir hemograma si aparece fiebre o dolor de garganta (agranulocitosis).",
   "Enfermedad de Graves: causa más frecuente en mujeres jóvenes."],
  "ATA – Guidelines for the diagnosis and management of hyperthyroidism (Thyroid 2016) · ETA – Graves' hyperthyroidism guideline (2018)")

# REU-025 · termómetro
V("termometro", "REU-025", "abscesos-axilares-trayectos-hidradenitis", "Hidradenitis supurativa: estadios de Hurley",
  "DERMATOLOGÍA ENAM: HIDRADENITIS SUPURATIVA", "DERMATOLOGÍA",
  ("Hidradenitis supurativa", ["Nódulos y abscesos dolorosos recurrentes en axilas, ingles y glúteos",
   "Drenan pus y dejan trayectos y cicatrices"]),
  ("Estibador de 48 años con un mes de lesiones", ["Tumoraciones axilares dolorosas de 1 cm", "Algunas drenan pus, otras con cicatrices"]),
  {"rotulo": "Estadio de Hurley",
   "niveles": [("I", "Leve", ["Abscesos sin trayectos"]),
               ("II", "Moderada", ["ABSCESOS RECURRENTES", "Trayectos y cicatrices separados"]),
               ("III", "Grave", ["Trayectos interconectados", "Toda la zona afectada"])],
   "caso_nivel": 1, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Tetraciclina oral por semanas", ["Doxiciclina; clindamicina tópica"], True),
             (2, "Clindamicina + rifampicina", ["Si no responde"], False),
             (3, "Adalimumab o cirugía", ["Enfermedad grave"], False)]},
  ["Oclusión del folículo piloso, no de la glándula sudorípara.",
   "Obesidad y tabaco son factores de riesgo modificables.",
   "Forúnculo: lesión única y aguda; no deja trayectos."],
  "EADV/EHSF – European S2k guidelines for hidradenitis suppurativa (2024)")

# PED-097 · fases
V("fases", "PED-097", "prematuro-flacido-apnea-pasos-iniciales", "Reanimación neonatal: el minuto de oro",
  "PEDIATRÍA ENAM: REANIMACIÓN NEONATAL", "PEDIATRÍA",
  ("Reanimación neonatal", ["Todo RN que no respira empieza con los pasos iniciales",
   "Calor, secar, posicionar la vía aérea y aspirar si es necesario"]),
  ("RN de 34 semanas, flácido y sin esfuerzo respiratorio", ["Se pinza el cordón", "¿Qué hacer inmediatamente?"]),
  {"rotulo": "Secuencia de la reanimación", "ans": 0,
   "fases": [("Iniciales", "0-30 s", "CALOR, SECAR, VÍA AÉREA", ["Aspirar si hay secreciones", "Estimular"]),
             ("VPP", "30-60 s", "Ventilación", ["Si apnea o FC < 100"]),
             ("Compresiones", "FC < 60", "Masaje + VPP", ["3:1 con O₂ al 100%"]),
             ("Adrenalina", "FC < 60", "Fármacos", ["Vía umbilical"])],
   "curvas": [],
   "chips_titulo": "Primer paso · marcado el correcto",
   "chips": [("Calor, secar, posicionar", True), ("VPP inmediata", False), ("Ventilación mecánica", False), ("O₂ por cánula", False)]},
  ["En prematuros < 32 semanas: bolsa de polietileno sin secar.",
   "Si tras los pasos iniciales sigue en apnea: VPP en el primer minuto.",
   "La VPP es la intervención más importante de la reanimación neonatal."],
  "AHA/AAP – Neonatal resuscitation guidelines (Circulation 2020; actualización 2025) · NRP 8.ª ed. (2021)")

# GIN-085 · árbol
A("GIN-085", "sulfato-magnesio-oliguria-bradipnea-suspender", "Vigilancia del sulfato de magnesio",
  "OBSTETRICIA ENAM: TOXICIDAD POR SULFATO DE MAGNESIO", "OBSTETRICIA",
  ("Sulfato de magnesio", ["Se vigilan reflejos, frecuencia respiratoria y diuresis",
   "FR < 12, reflejos abolidos u oliguria = toxicidad: suspender"]),
  ("Gestante de 32 semanas con preeclampsia severa", ["Recibe nifedipino y sulfato de magnesio", "Diuresis 10 mL/h · FR 10 x'"]),
  Q("¿Signos de toxicidad?", [
      L("No", "Continuar", ["Vigilar cada hora"]),
      L("Sí: FR < 12, oliguria", "SUSPENDER EL MAGNESIO", ["Gluconato de calcio 1 g EV", "Magnesemia y soporte"], path=True),
      L("Paro respiratorio", "Ventilar + calcio", ["Soporte vital"])], path=True),
  ("Magnesemia y efectos", [("Terapéutico", False), ("Tóxico", True), ("Grave", False)], [
      ("mg/dL", ["4.8-8.4", "> 9: reflejos abolidos", "> 12: paro respiratorio"]),
      ("Vigilar", ["Reflejo patelar", "FR y diuresis", "ECG"])]),
  ["El magnesio se elimina por el riñón: la oliguria lo acumula.",
   "Diuresis mínima segura: 25-30 mL/h.",
   "No suspender el nifedipino: la toxicidad es del magnesio."],
  "ACOG – Practice Bulletin N.° 222: Gestational hypertension and preeclampsia (2020) · " + WILLIAMS)

# INF-041 · radial
V("radial", "INF-041", "nina-prurito-vulvar-perianal-nocturno-oxiuros", "Prurito vulvar en la niña",
  "INFECTOLOGÍA ENAM: OXIURIASIS", "INFECTOLOGÍA",
  ("Vulvovaginitis en niñas prepúberes", ["La mayoría es inespecífica o por parásitos",
   "Prurito perianal y vulvar nocturno = Enterobius vermicularis"]),
  ("Niña de 4 años con 8 días de prurito vaginal y perianal", ["Irritabilidad nocturna", "Secreción en la ropa interior"]),
  {"rotulo": "Mapa del tema", "centro": "PRURITO VULVAR", "centro_sub": "Niña prepúber", "ans": 0,
   "items": [("ENTEROBIUS", ["Prurito nocturno perianal", "Test de Graham"]),
             ("Inespecífica", ["Higiene, irritantes", "La más frecuente"]),
             ("Candida", ["Rara antes de la pubertad", "Pañal, diabetes"]),
             ("Trichomonas", ["Es de transmisión sexual", "Sospechar abuso"]),
             ("Cuerpo extraño", ["Secreción fétida", "Con sangre"])],
   "ruta": ["Prurito perianal y vulvar", "Empeora de noche", "Irritabilidad", "ENTEROBIUS"]},
  ["Albendazol dosis única y repetir a las 2 semanas; tratar a toda la familia.",
   "La hembra migra de noche a la zona perianal a poner huevos.",
   "Una ITS en una niña obliga a descartar abuso sexual."],
  "CDC – Enterobiasis: clinical care (2024) · " + NELSON)

# GIN-086 · fases
V("fases", "GIN-086", "parto-domiciliario-placenta-retenida-sangrado", "Alumbramiento y retención placentaria",
  "OBSTETRICIA ENAM: RETENCIÓN PLACENTARIA", "OBSTETRICIA",
  ("Tercer período del parto", ["Con manejo activo la placenta sale en menos de 30 minutos",
   "Retención con sangrado activo = extracción manual inmediata"]),
  ("Puérpera de parto domiciliario, en SERUMS", ["Placenta no expulsada tras 1 hora", "Sangrado profuso, cordón sin descenso"]),
  {"rotulo": "Evolución del alumbramiento", "ans": 2,
   "fases": [("Manejo activo", "0-30 min", "Oxitocina 10 UI IM", ["Tracción controlada"]),
             ("Retención", "> 30 min", "Placenta retenida", ["Sin sangrado: esperar/referir"]),
             ("Hemorragia", "Ahora", "EXTRACCIÓN MANUAL", ["Con analgesia, antibiótico"]),
             ("Si falla", "Después", "Acretismo", ["Referir para cirugía"])],
   "curvas": [("Sangrado", ROSE, [0.1, 0.15, 0.25, 0.5, 0.9, 0.7, 0.4])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("Extracción manual", True), ("Manejo expectante", False), ("Solo oxitocina", False), ("Legrado uterino", False)]},
  ["Tras extraer la placenta: masaje uterino y uterotónicos.",
   "El legrado se usa para restos, no para la placenta completa retenida.",
   "Si no hay plano de despegamiento, sospechar acretismo y no forzar."],
  "OMS – Recommendations for the prevention and treatment of postpartum haemorrhage (2023) · " + WILLIAMS)

# GAS-033 · termómetro
V("termometro", "GAS-033", "pancreatitis-grave-choque-fluidoterapia", "Pancreatitis aguda: gravedad",
  "GASTROENTEROLOGÍA ENAM: PANCREATITIS AGUDA GRAVE", "GASTROENTEROLOGÍA",
  ("Gravedad de la pancreatitis (Atlanta revisada)", ["Grave = falla orgánica persistente > 48 h",
   "Con choque, lo primero es reponer volumen"]),
  ("Mujer de 52 años obesa con dolor en cinturón", ["PA 65/40, soporosa", "TC: páncreas aumentado y líquido peripancreático"]),
  {"rotulo": "Clasificación de Atlanta",
   "niveles": [("Leve", "Leve", ["Sin falla orgánica"]),
               ("Moderada", "Moderada", ["Falla < 48 h o complicación local"]),
               ("Grave", "Grave", ["FALLA ORGÁNICA > 48 H", "Choque, insuficiencia respiratoria"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "FLUIDOTERAPIA INTENSIVA", ["Ringer lactato guiado por metas"], True),
             (2, "Nutrición enteral precoz", ["No parenteral de rutina"], False),
             (3, "Sin antibiótico profiláctico", ["Solo si hay necrosis infectada"], False)]},
  ["Metas: PAM ≥ 65, diuresis ≥ 0.5 mL/kg/h; evitar la sobrecarga.",
   "Los inhibidores de proteasas no tienen utilidad.",
   "La necrosis infectada se sospecha por gas en la TC o deterioro tras la primera semana."],
  "ACG – Guideline: Management of acute pancreatitis (Am J Gastroenterol 2024) · Atlanta revisada (Gut 2013)")

# NEF-035 · matriz
V("matriz", "NEF-035", "infeccion-respiratoria-previa-hematuria-gn-postinfecciosa", "Glomerulonefritis con hematuria",
  "NEFROLOGÍA ENAM: GLOMERULONEFRITIS AGUDA POSTINFECCIOSA", "NEFROLOGÍA",
  ("Síndrome nefrítico", ["Hematuria con cilindros hemáticos, edema e hipertensión",
   "Latencia de 1-3 semanas tras una infección = postinfecciosa"]),
  ("Varón de 18 años con infección respiratoria hace 2 semanas", ["Edema y hematuria · PA 150/100", "Cilindros hemáticos · proteinuria 1.2 g/24 h"]),
  {"rotulo": "Glomerulopatías", "eje_x": "Rasgo", "eje_y": "Causa",
   "cols": ["Relación con la infección", "Complemento C3"], "rows": ["Postinfecciosa", "Nefropatía IgA", "Membrano proliferativa", "Lesiones mínimas"], "caso": (0, 0),
   "cells": [[("1-3 SEMANAS DESPUÉS", ["Faringe o piel"]), ("Bajo", ["Se normaliza en 8 semanas"])],
             [("1-3 días (simultánea)", []), ("Normal", [])],
             [("Variable", []), ("Bajo persistente", [])],
             [("Nefrótico, no nefrítico", []), ("Normal", [])]]},
  ["El ASO elevado apoya el origen estreptocócico.",
   "Tratamiento de soporte: restricción de sal, diurético y antihipertensivo.",
   "Si el C3 sigue bajo más de 8 semanas: biopsia."],
  "KDIGO – Clinical practice guideline for the management of glomerular diseases (2021) · Brenner and Rector's The Kidney 11.ª ed. (2020)")

# SP-057 · fases
V("fases", "SP-057", "ciclo-violencia-pareja-acumulacion-tension", "Ciclo de la violencia",
  "SALUD PÚBLICA ENAM: CICLO DE LA VIOLENCIA", "SALUD PÚBLICA",
  ("Ciclo de la violencia (Walker)", ["Tres fases que se repiten y se acortan con el tiempo",
   "Primero, pequeños incidentes y roces que aumentan la tensión"]),
  ("Pregunta de concepto", ["Fase con sucesión de pequeños episodios", "y roces permanentes en la pareja"]),
  {"rotulo": "Fases del ciclo", "ans": 0,
   "fases": [("Tensión", "Fase 1", "ACUMULACIÓN DE TENSIÓN", ["Roces, insultos, control"]),
             ("Explosión", "Fase 2", "Agresión aguda", ["Violencia física o sexual"]),
             ("Calma", "Fase 3", "Arrepentimiento", ["Luna de miel, promesas"])],
   "curvas": [("Tensión", ROSE, [0.2, 0.4, 0.6, 0.95, 0.3, 0.15, 0.3])],
   "chips_titulo": "Fase del caso · marcada la correcta",
   "chips": [("Acumulación de tensión", True), ("Violencia aguda", False), ("Arrepentimiento", False), ("Reconciliación", False)]},
  ["Con el tiempo la fase de calma se acorta y la violencia se intensifica.",
   "La reconciliación mantiene a la víctima en la relación.",
   "Detectar e intervenir en la fase de tensión puede prevenir la agresión."],
  "Walker LE – The Battered Woman Syndrome 4.ª ed. (2017) · MINSA – Guía técnica para la atención de personas afectadas por violencia")

# CB-028 · árbol
A("CB-028", "licor-adulterado-convulsiones-acidosis-metanol", "Intoxicación por metanol",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR METANOL", "CIENCIAS BÁSICAS",
  ("Intoxicación por metanol", ["Licor adulterado: acidosis metabólica grave con anión gap alto",
   "El ácido fórmico daña la retina y el cerebro"]),
  ("Mujer de 20 años tras beber licor de dudosa procedencia", ["Convulsiones, Glasgow 7, PA 80/50", "pH 7.00 · HCO₃⁻ 5 · lactato 8"]),
  Q("¿Acidosis grave, coma o daño visual?", [
      L("Sí", "HEMODIÁLISIS URGENTE", ["+ soporte y fomepizol o etanol", "Bicarbonato y ácido fólico"], path=True),
      L("No", "Bloquear la alcohol deshidrogenasa", ["Fomepizol o etanol", "Vigilar gases"])], path=True),
  ("Alcoholes tóxicos", [("Metanol", True), ("Etilenglicol", False)], [
      ("Metabolito", ["Ácido fórmico", "Oxalato"]),
      ("Daño", ["Ceguera, ganglios basales", "Insuficiencia renal"]),
      ("Clave", ["Visión en «nieve»", "Cristales de oxalato en orina"])]),
  ["Indicaciones de diálisis: pH < 7.15-7.25, coma, convulsiones, alteración visual o falla renal.",
   "El lavado gástrico no sirve: el metanol se absorbe en minutos.",
   "Los diuréticos no eliminan el metanol."],
  "EXTRIP – Extracorporeal treatment for methanol poisoning (Crit Care Med 2015) · Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# SP-058 · radial
V("radial", "SP-058", "diresa-espacios-concertacion-participacion-ciudadana", "Estrategias de salud pública",
  "SALUD PÚBLICA ENAM: PARTICIPACIÓN CIUDADANA", "SALUD PÚBLICA",
  ("Participación ciudadana en salud", ["Espacios donde la población delibera, concerta y vigila compromisos",
   "Parte del Modelo de Atención Integral basado en familia y comunidad"]),
  ("Director de una DIRESA", ["Promueve espacios de deliberación y concertación", "Y evaluación de compromisos de todos los actores"]),
  {"rotulo": "Mapa del tema", "centro": "ESTRATEGIAS", "centro_sub": "Salud pública", "ans": 0,
   "items": [("PARTICIPACIÓN CIUDADANA", ["Deliberar, concertar, vigilar", "Rendición de cuentas"]),
             ("Promoción de la salud", ["Estilos de vida, entornos"]),
             ("Intersectorialidad", ["Salud con otros sectores"]),
             ("Descentralización", ["Transferir funciones"]),
             ("Vigilancia epidemiológica", ["Datos para decidir"])],
   "ruta": ["Espacios de deliberación", "Todos los actores", "Evalúan compromisos", "PARTICIPACIÓN CIUDADANA"]},
  ["Ejemplos: comités de salud, CLAS, presupuesto participativo.",
   "La participación ciudadana incluye la vigilancia social de los servicios.",
   "Concertación política es solo una parte del proceso."],
  "MINSA – Modelo de Cuidado Integral de Salud por Curso de Vida (MCI, 2020) · OPS – Participación social en salud")

# INF-042 · tarjetas
V("tarjetas", "INF-042", "jardinero-espina-rosa-nodulos-linfaticos-esporotricosis", "Úlcera con nódulos en cadena",
  "INFECTOLOGÍA ENAM: ESPOROTRICOSIS", "INFECTOLOGÍA",
  ("Lesiones cutáneas con nódulos a lo largo de linfáticos", ["Inoculación con espina o tierra + nódulos en trayecto linfático",
   "Esporotricosis: Sporothrix, «enfermedad del jardinero»"]),
  ("Jardinero de 28 años, espina de rosa hace 4 semanas", ["Pápula indolora que se ulcera", "Nódulos que siguen el drenaje linfático"]),
  {"rotulo": "¿Qué infección es?", "ans": 0, "cards": [
      {"titulo": "ESPOROTRICOSIS", "datos": [
          ("Exposición", "Espinas, tierra, gatos", True), ("Lesión", "Nódulos linfangíticos", True),
          ("Tratamiento", "Itraconazol", False)],
       "pie": "Yoduro de potasio (alternativa)"},
      {"titulo": "Leishmaniasis", "datos": [
          ("Exposición", "Picadura de Lutzomyia", False), ("Lesión", "Úlcera de bordes elevados", False),
          ("Tratamiento", "Antimoniales", False)],
       "pie": "Zonas andinas y selva"},
      {"titulo": "Blastomicosis", "datos": [
          ("Exposición", "Inhalación (EE. UU.)", False), ("Lesión", "Verrugosa, pulmonar", False),
          ("Tratamiento", "Itraconazol", False)],
       "pie": "Sistémica"},
      {"titulo": "Micosis fungoide", "datos": [
          ("Exposición", "Ninguna", False), ("Lesión", "Placas crónicas", False),
          ("Tratamiento", "Oncológico", False)],
       "pie": "Linfoma T cutáneo"}]},
  ["Patrón linfocutáneo «esporotricoide» también en Nocardia y micobacterias atípicas.",
   "El cultivo en agar Sabouraud confirma el diagnóstico.",
   "Tratamiento 3-6 meses con itraconazol."],
  "IDSA – Clinical practice guidelines for sporotrichosis (Clin Infect Dis 2007) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# GIN-087 · embudo
V("embudo", "GIN-087", "puerpera-vih-tar-anticoncepcion-diu", "Anticoncepción en puérpera con VIH",
  "GINECOLOGÍA ENAM: ANTICONCEPCIÓN EN VIH", "GINECOLOGÍA",
  ("Anticoncepción en mujeres con VIH en TAR", ["Algunos antirretrovirales reducen la eficacia de las hormonas",
   "Los DIU no interactúan con el TAR"]),
  ("Puérpera mediata con VIH en TAR", ["No desea otro embarazo"]),
  {"rotulo": "Embudo de elección",
   "inicio": "Puérpera con VIH en TAR",
   "candidatos": ["DIU", "Implante", "Píldora combinada", "Parche", "Inyectable mensual"],
   "pasos": [("Puerperio: evitar estrógenos (trombosis)", ["Píldora combinada", "Parche", "Inyectable mensual"]),
             ("Sin interacción con el TAR y de larga duración", ["Implante"])],
   "final": ("DIU (COBRE O LEVONORGESTREL)", ["Sin interacciones", "Colocar posparto o a las 6 semanas"]),
   "nota": "El efavirenz reduce la eficacia del implante; con dolutegravir el implante sigue siendo útil."},
  ["Usar siempre preservativo además del método (doble protección).",
   "El VIH no contraindica el DIU (categoría OMS 2 en quienes están clínicamente bien).",
   "Los estrógenos se evitan en las primeras semanas posparto."],
  "OMS – Medical eligibility criteria for contraceptive use 6.ª ed. (2025) · MINSA – Norma técnica de planificación familiar")

# PED-098 · tarjetas
V("tarjetas", "PED-098", "lactante-emaciado-piel-flacida-marasmo", "Desnutrición grave en el lactante",
  "PEDIATRÍA ENAM: MARASMO", "PEDIATRÍA",
  ("Desnutrición aguda grave", ["Marasmo: emaciación extrema sin edema",
   "Kwashiorkor: edema con relativa conservación de la grasa"]),
  ("Lactante de 15 meses de una comunidad nativa", ["Peso 7 kg, talla 64 cm", "Piel flácida y arrugada, cara de viejo, emaciación en glúteos"]),
  {"rotulo": "¿Qué tipo de desnutrición?", "ans": 0, "cards": [
      {"titulo": "MARASMO", "datos": [
          ("Edema", "No", True), ("Músculo y grasa", "Muy consumidos", True),
          ("Cara", "De anciano (simiesca)", True), ("Piel", "Flácida, arrugada", True)],
       "pie": "Déficit calórico global"},
      {"titulo": "Kwashiorkor", "datos": [
          ("Edema", "Sí, con fóvea", False), ("Músculo y grasa", "Grasa conservada", False),
          ("Cara", "Luna llena", False), ("Piel", "Dermatosis en «pintura»", False)],
       "pie": "Déficit proteico"},
      {"titulo": "Mixta", "datos": [
          ("Edema", "Sí", False), ("Músculo y grasa", "Consumidos", False),
          ("Cara", "Variable", False), ("Piel", "Lesiones", False)],
       "pie": "Marasmo-kwashiorkor"},
      {"titulo": "Desnutrición crónica", "datos": [
          ("Edema", "No", False), ("Músculo y grasa", "Proporcionados", False),
          ("Cara", "Normal", False), ("Piel", "Normal", False)],
       "pie": "Talla baja para la edad"}]},
  ["Manejo en 10 pasos de la OMS: hipoglucemia, hipotermia, deshidratación, infecciones…",
   "Fase inicial con F-75 y luego F-100; cuidado con el síndrome de realimentación.",
   "Rehidratar con ReSoMal, no con SRO estándar."],
  "OMS – Guideline: updates on the management of severe acute malnutrition in infants and children (2013; actualización 2023) · " + NELSON)

# PED-099 · puntaje
V("puntaje", "PED-099", "diarrea-con-moco-sin-deshidratacion-plan-a", "Diarrea: evaluar la deshidratación",
  "PEDIATRÍA ENAM: DIARREA AGUDA SIN DESHIDRATACIÓN", "PEDIATRÍA",
  ("Evaluación de la deshidratación (AIEPI)", ["Se buscan 4 signos: estado general, ojos, sed y pliegue",
   "Sin signos: plan A en casa con sales de rehidratación oral"]),
  ("Niño de 6 años con 2 días de diarrea con moco", ["5 deposiciones al día, fiebre 38 °C", "Sin vómitos ni signos de deshidratación"]),
  {"rotulo": "Signos de deshidratación en el caso", "escala": "AIEPI", "total": 0, "max": 4,
   "total_label": "Signos presentes",
   "interpreta": "Sin deshidratación: plan A",
   "items": [("Letárgico o irritable", "1", False), ("Ojos hundidos", "1", False),
             ("Bebe ávidamente o no puede beber", "1", False), ("Pliegue cutáneo lento", "1", False)],
   "bandas": [("0-1", "Sin deshidratación", "PLAN A: SRO en casa, seguir comiendo", True),
              ("≥ 2", "Algún grado", "Plan B: SRO 75 mL/kg en 4 h", False),
              ("≥ 2 graves", "Grave", "Plan C: EV", False)]},
  ["Plan A: más líquidos, SRO tras cada deposición, zinc y alimentación continua.",
   "Adsorbentes y antisecretores no se recomiendan en niños.",
   "Sin sangre en heces no se indica antibiótico."],
  "OMS/OPS – AIEPI: tratamiento de la diarrea · MINSA – Guía de práctica clínica de enfermedad diarreica aguda en la niña y el niño")

# HEM-017 · árbol
A("HEM-017", "ttpa-prolongado-prueba-mezcla-no-corrige", "TTPa prolongado: prueba de mezcla",
  "HEMATOLOGÍA ENAM: INHIBIDORES DE LOS FACTORES", "HEMATOLOGÍA",
  ("TTPa prolongado", ["La prueba de mezcla con plasma normal distingue déficit de inhibidor",
   "Si no corrige: hay un anticuerpo (inhibidor)"]),
  ("Mujer de 58 años con diátesis hemorrágica", ["Sin antecedentes de sangrado", "TTPa prolongado que no corrige en la mezcla"]),
  Q("¿Corrige con plasma normal?", [
      L("Sí", "Déficit de factor", ["Hemofilia A, B, von Willebrand"]),
      Q("¿Hay sangrado?", [
          L("Sí", "INHIBIDOR DE FACTOR", ["Hemofilia adquirida (anti-FVIII)", "Autoinmune, posparto, cáncer"], path=True),
          L("No, trombosis", "Anticoagulante lúpico", ["Síndrome antifosfolípido"])],
        edge="No: INHIBIDOR", path=True)], path=True),
  ("Prueba de mezcla", [("No corrige", True), ("Corrige", False)], [
      ("Significa", ["Anticuerpo inhibidor", "Falta un factor"]),
      ("Ejemplo", ["Hemofilia adquirida", "Hemofilia congénita"]),
      ("Tratamiento", ["Agentes de bypass + inmunosupresión", "Reponer el factor"])]),
  ["La hemofilia adquirida afecta adultos mayores sin historia previa de sangrado.",
   "El anticoagulante lúpico alarga el TTPa pero causa trombosis, no hemorragia.",
   "Déficit de antitrombina y mutación de protrombina no alargan el TTPa."],
  "ISTH/Tiede – International recommendations on acquired hemophilia A (Haematologica 2020)")

# HEM-018 · radial
V("radial", "HEM-018", "anticonceptivos-combinados-tvp-factores-coagulacion", "Estrógenos y trombosis",
  "HEMATOLOGÍA ENAM: ANTICONCEPTIVOS COMBINADOS Y TROMBOSIS", "HEMATOLOGÍA",
  ("Estrógenos y coagulación", ["Aumentan la síntesis hepática de factores de coagulación",
   "El tabaco suma riesgo trombótico"]),
  ("Mujer de 34 años con edema y dolor en el tobillo", ["Toma anticonceptivos combinados", "Fuma ocasionalmente"]),
  {"rotulo": "Mapa del tema", "centro": "ESTRÓGENOS", "centro_sub": "Efecto procoagulante", "ans": 0,
   "items": [("AUMENTO DE FACTORES", ["Fibrinógeno, II, VII, VIII, X", "Síntesis hepática"]),
             ("Menos proteína S", ["Menor anticoagulación"]),
             ("Resistencia a proteína C", ["Adquirida"]),
             ("Menos antitrombina", ["Leve descenso"]),
             ("Tabaco", ["Suma riesgo"])],
   "ruta": ["Anticonceptivo combinado", "Hígado sintetiza más factores", "Estado protrombótico", "AUMENTO DE FACTORES"]},
  ["Riesgo mayor en el primer año de uso y con factor V Leiden.",
   "Fumadoras > 35 años: contraindicados los combinados.",
   "Los métodos solo de progestina no aumentan el riesgo de forma relevante."],
  "OMS – Medical eligibility criteria for contraceptive use 6.ª ed. (2025) · Williams Hematology 10.ª ed. (2021)")

# NEF-036 · matriz
V("matriz", "NEF-036", "fiebre-disuria-dolor-perineal-prostatitis", "Fiebre con síntomas urinarios en el varón",
  "NEFROLOGÍA ENAM: PROSTATITIS AGUDA", "NEFROLOGÍA",
  ("Infección urinaria en el varón", ["Fiebre + disuria + dolor perineal + próstata dolorosa = prostatitis aguda",
   "El tacto rectal debe ser suave (no masajear)"]),
  ("Varón de 24 años con 3 días de fiebre y disuria", ["Retardo miccional y dolor perineal", "Puño percusión negativa · próstata dolorosa"]),
  {"rotulo": "Diferencial", "eje_x": "Rasgo", "eje_y": "Diagnóstico",
   "cols": ["Dolor", "Examen clave"], "rows": ["Prostatitis aguda", "Pielonefritis", "Uretritis", "Epididimitis"], "caso": (0, 1),
   "cells": [[("Perineal", ["Retención"]), ("PRÓSTATA DOLOROSA", ["Tacto suave"])],
             [("Lumbar", []), ("Puño percusión (+)", [])],
             [("Uretral", ["Sin fiebre"]), ("Secreción uretral", [])],
             [("Escrotal", []), ("Epidídimo aumentado", ["Prehn (+)"])]]},
  ["Gérmenes: E. coli y enterobacterias; en jóvenes con riesgo sexual, gonococo y clamidia.",
   "Tratamiento: fluoroquinolona o cotrimoxazol por 2-4 semanas.",
   "Si hay retención: sonda suprapúbica."],
  "EAU – Guidelines on urological infections (2024)")

# INF-043 · fases
V("fases", "INF-043", "reinfeccion-dengue-choque-mediadores-vasoactivos", "Dengue grave por reinfección",
  "INFECTOLOGÍA ENAM: DENGUE GRAVE", "INFECTOLOGÍA",
  ("Dengue secundario", ["Una segunda infección por otro serotipo es más grave",
   "Anticuerpos facilitadores y liberación de mediadores vasoactivos causan fuga plasmática"]),
  ("Mujer de 30 años con dengue hace un mes", ["Pérdida de conciencia, PA 80/50", "Epistaxis y petequias, fiebre 39 °C"]),
  {"rotulo": "Cómo se produce el choque", "ans": 2,
   "fases": [("1.ª infección", "Antes", "Anticuerpos", ["Contra un serotipo"]),
             ("Reinfección", "Otro serotipo", "Facilitación", ["Más células infectadas"]),
             ("Tormenta", "Horas", "MEDIADORES VASOACTIVOS", ["Citocinas, histamina"]),
             ("Choque", "Fase crítica", "Fuga plasmática", ["Hipotensión, sangrado"])],
   "curvas": [("Carga", ROSE, [0.2, 0.5, 0.8, 0.9, 0.6, 0.3, 0.2]),
              ("Fuga", AMBER, [0.05, 0.1, 0.3, 0.6, 0.9, 0.95, 0.5])],
   "chips_titulo": "Mecanismo · marcado el correcto",
   "chips": [("Mediadores vasoactivos", True), ("Menor carga viral", False), ("Menos granulocitos", False), ("Menos mediadores", False)]},
  ["El choque por dengue es por fuga capilar, no por hemorragia en primer lugar.",
   "Tratamiento: cristaloides en bolos según evolución.",
   "Hematocrito en ascenso con plaquetas en descenso anuncia la fase crítica."],
  "OPS – Directrices para el diagnóstico clínico y el tratamiento del dengue, chikungunya y zika (2022)")

# NRL-023 · matriz
V("matriz", "NRL-023", "anciano-tec-leve-semanas-deterioro-subdural-cronico", "Hematomas intracraneales",
  "NEUROLOGÍA ENAM: HEMATOMA SUBDURAL CRÓNICO", "NEUROLOGÍA",
  ("Hematomas traumáticos", ["En el anciano, un TEC leve puede romper venas puente",
   "Semanas después: cefalea, confusión o deterioro cognitivo"]),
  ("Varón de 80 años con TEC leve hace 3 semanas", ["Cefalea persistente", "Deterioro cognitivo y de la conducta"]),
  {"rotulo": "Tipos de hematoma", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Vaso y tiempo", "Tomografía"], "rows": ["Epidural", "Subdural agudo", "Subdural crónico"], "caso": (2, 0),
   "cells": [[("Arteria meníngea media", ["Horas, intervalo lúcido"]), ("Biconvexo", ["Hiperdenso"])],
             [("Venas puente", ["Horas, TEC grave"]), ("Semiluna hiperdensa", [])],
             [("VENAS PUENTE, SEMANAS", ["Anciano, alcohol, anticoagulado"]), ("Semiluna hipodensa", [])]]},
  ["Atrofia cerebral estira las venas puente: más riesgo en ancianos y alcohólicos.",
   "Puede simular demencia: es una causa tratable.",
   "Tratamiento: drenaje por trépano si es sintomático."],
  "Youmans and Winn Neurological Surgery 8.ª ed. (2022) · NICE – Head injury: assessment and early management (2023)")

# GIN-088 · radial
V("radial", "GIN-088", "parto-instrumentado-macrosomico-utero-contraido-desgarro", "Hemorragia posparto: las 4 T",
  "OBSTETRICIA ENAM: HEMORRAGIA POR LESIÓN DEL CANAL DEL PARTO", "OBSTETRICIA",
  ("Causas de hemorragia posparto", ["Tono, Trauma, Tejido y Trombina",
   "Útero contraído con sangrado rojo rutilante = trauma del canal del parto"]),
  ("Puérpera de parto instrumentado, RN de 4100 g", ["Sangrado abundante rojo rutilante", "PA 80/50 · útero contraído"]),
  {"rotulo": "Mapa del tema", "centro": "4 T", "centro_sub": "Hemorragia posparto", "ans": 1,
   "items": [("Tono", ["Atonía: 70%", "Útero blando"]),
             ("TRAUMA", ["Desgarros del canal", "Útero contraído"]),
             ("Tejido", ["Restos, acretismo"]),
             ("Trombina", ["Coagulopatía"]),
             ("Inversión uterina", ["Masa en vagina"])],
   "ruta": ["Parto instrumentado, feto grande", "Útero contraído", "Sangrado rojo rutilante", "TRAUMA"]},
  ["Revisar cérvix, vagina y periné con buena luz y suturar.",
   "Si el útero está contraído, la atonía queda descartada.",
   "Considerar hematomas si hay dolor intenso y sangrado externo escaso."],
  "OMS – Recommendations for the prevention and treatment of postpartum haemorrhage (2023) · " + WILLIAMS)

# NRL-024 · embudo
V("embudo", "NRL-024", "cefalea-trueno-anisocoria-ptosis-hsa", "Cefalea súbita con compromiso del III par",
  "NEUROLOGÍA ENAM: HEMORRAGIA SUBARACNOIDEA", "NEUROLOGÍA",
  ("Hemorragia subaracnoidea", ["Cefalea en trueno, vómitos, convulsiones y rigidez de nuca",
   "III par (midriasis + ptosis) sugiere aneurisma de la comunicante posterior"]),
  ("Mujer de 35 años con cefalea súbita 9/10", ["Convulsión, Glasgow 10 · rigidez de nuca", "Pupila derecha 5 mm con ptosis"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Cefalea súbita con convulsión",
   "candidatos": ["Hemorragia subaracnoidea", "Meningitis", "Subdural", "Cerebelosa", "Migraña"],
   "pasos": [("Inicio en trueno y sin fiebre", ["Meningitis", "Migraña"]),
             ("Rigidez de nuca + III par, sin trauma", ["Subdural", "Cerebelosa"])],
   "final": ("HEMORRAGIA SUBARACNOIDEA", ["Aneurisma de comunicante posterior", "TC sin contraste y angio-TC"]),
   "nota": "Si la TC es normal y la sospecha persiste: punción lumbar (xantocromía)."},
  ["Nimodipino para prevenir el vasoespasmo.",
   "Asegurar el aneurisma precozmente (endovascular o clipaje).",
   "Complicaciones: resangrado, vasoespasmo, hidrocefalia, hiponatremia."],
  "AHA/ASA – Guideline for the management of aneurysmal subarachnoid hemorrhage (Stroke 2023)")

# END-023 · tarjetas
V("tarjetas", "END-023", "crisis-adrenergicas-hta-refractaria-metanefrinas", "Hipertensión secundaria endocrina",
  "ENDOCRINOLOGÍA ENAM: FEOCROMOCITOMA", "ENDOCRINOLOGÍA",
  ("Hipertensión endocrina", ["Crisis de cefalea, sudoración y palpitaciones con HTA resistente",
   "Metanefrinas elevadas = feocromocitoma"]),
  ("Varón de 28 años con 6 meses de crisis", ["Cefalea, sudoración, palpitaciones, palidez", "PA 190/95 con 3 fármacos · metanefrinas altas"]),
  {"rotulo": "¿Qué causa la hipertensión?", "ans": 0, "cards": [
      {"titulo": "FEOCROMOCITOMA", "datos": [
          ("Clínica", "Crisis adrenérgicas", True), ("Laboratorio", "Metanefrinas altas", True),
          ("Potasio", "Normal", False), ("Imagen", "Masa suprarrenal", False)],
       "pie": "Alfabloqueo y cirugía"},
      {"titulo": "Hiperaldosteronismo", "datos": [
          ("Clínica", "HTA resistente", False), ("Laboratorio", "Aldosterona/renina alta", False),
          ("Potasio", "Bajo", False), ("Imagen", "Adenoma", False)],
       "pie": "Espironolactona"},
      {"titulo": "Cushing", "datos": [
          ("Clínica", "Obesidad central, estrías", False), ("Laboratorio", "Cortisol libre alto", False),
          ("Potasio", "Normal o bajo", False), ("Imagen", "Hipófisis o suprarrenal", False)],
       "pie": "Según causa"},
      {"titulo": "Hipertiroidismo", "datos": [
          ("Clínica", "Continua, no en crisis", False), ("Laboratorio", "TSH baja", False),
          ("Potasio", "Normal", False), ("Imagen", "Tiroides", False)],
       "pie": "HTA sistólica"}]},
  ["Antes de operar: alfabloqueo (fenoxibenzamina o doxazosina) y luego betabloqueo.",
   "Nunca betabloquear primero: crisis hipertensiva por alfa sin oposición.",
   "Regla del 10%: bilateral, maligno, extraadrenal, familiar."],
  "Endocrine Society – Pheochromocytoma and paraganglioma guideline (2014; actualización 2024)")

# CIR-054 · árbol
A("CIR-054", "trauma-abdominal-cerrado-sin-peritonitis-estable", "Trauma abdominal cerrado",
  "CIRUGÍA ENAM: MANEJO NO OPERATORIO DEL TRAUMA ABDOMINAL", "CIRUGÍA",
  ("Trauma abdominal cerrado", ["La estabilidad hemodinámica decide entre cirugía inmediata y estudio",
   "Estable y sin peritonitis: TC con contraste y manejo no operatorio"]),
  ("Varón de 30 años, accidente hace 1 hora", ["Sin peritonitis ni otras indicaciones de laparotomía"]),
  Q("¿Hemodinámicamente estable?", [
      L("No", "FAST y laparotomía", ["Si FAST (+): quirófano"]),
      Q("¿Peritonitis o neumoperitoneo?", [
          L("No", "MANEJO NO OPERATORIO", ["TC con contraste", "Observación seriada"], path=True),
          L("Sí", "Laparotomía", ["Víscera hueca"])],
        edge="Sí: ESTABLE", path=True)], path=True),
  ("Decisión en trauma abdominal", [("Estable", True), ("Inestable", False)], [
      ("Estudio", ["TC con contraste", "FAST en la sala"]),
      ("Conducta", ["No operatorio si es posible", "Laparotomía"]),
      ("Órganos", ["Bazo e hígado en su mayoría", "Sangrado activo"])]),
  ["El manejo no operatorio del bazo y el hígado es estándar en el paciente estable.",
   "La hemoglobina inicial puede ser normal pese a sangrado activo.",
   "Reevaluar con examen seriado: cualquier inestabilidad cambia la conducta."],
  ATLS + " · WSES – Liver and spleen trauma guidelines (World J Emerg Surg 2020)")

# END-024 · árbol
A("END-024", "calor-nerviosismo-polimenorrea-tsh-t4l", "Estudio de la función tiroidea",
  "ENDOCRINOLOGÍA ENAM: DIAGNÓSTICO DEL HIPERTIROIDISMO", "ENDOCRINOLOGÍA",
  ("Sospecha de disfunción tiroidea", ["La TSH es la mejor prueba inicial; se acompaña de T4 libre",
   "TSH baja con T4 libre alta = hipertiroidismo primario"]),
  ("Mujer de 45 años con calor y nerviosismo", ["Polimenorrea, caída de cabello", "FC 110, piel caliente"]),
  Q("TSH + T4 libre: ¿cómo está la TSH?", [
      Q("¿T4 libre?", [
          L("Alta", "HIPERTIROIDISMO PRIMARIO", ["Graves, bocio tóxico, tiroiditis"], path=True),
          L("Normal", "T3 o subclínico", ["Medir T3"])],
        edge="Baja", path=True),
      L("Alta", "Hipotiroidismo", ["O TSH-oma si T4L alta"]),
      L("Normal", "Eutiroidea", ["Otra causa"])], path=True),
  ("Pruebas tiroideas", [("TSH", True), ("T4 libre", False), ("T3", False)], [
      ("Utilidad", ["Tamizaje: la más sensible", "Confirma y gradúa", "T3 toxicosis"]),
      ("Cuándo", ["Siempre", "Siempre con la TSH", "Si T4L normal"])]),
  ["GnRH, LH y FSH no evalúan la tiroides.",
   "Luego de confirmar: anticuerpos TRAb o gammagrafía para la causa.",
   "El hipertiroidismo causa oligomenorrea más a menudo; también puede alterar el ciclo."],
  "ATA – Guidelines for the diagnosis and management of hyperthyroidism (Thyroid 2016)")

# HEM-019 · embudo
V("embudo", "HEM-019", "nino-dolor-oseo-nocturno-petequias-lla", "Niño con citopenias y dolor óseo",
  "HEMATOLOGÍA ENAM: LEUCEMIA LINFOBLÁSTICA AGUDA", "HEMATOLOGÍA",
  ("Leucemia en el niño", ["Palidez, petequias, fiebre, dolor óseo y visceromegalias",
   "La leucemia linfoblástica aguda es el cáncer más frecuente en niños (pico 2-5 años)"]),
  ("Niño de 4 años con un mes de cansancio y febrícula", ["Dolor en piernas que lo despierta", "Palidez, petequias, hepatoesplenomegalia · plaquetas 80 000"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Niño con anemia y petequias",
   "candidatos": ["LLA", "LMA", "Anemia aplásica", "Rabdomiosarcoma", "Artritis juvenil"],
   "pasos": [("Hepatoesplenomegalia: no es aplasia", ["Anemia aplásica"]),
             ("Citopenias con dolor óseo nocturno", ["Rabdomiosarcoma", "Artritis juvenil"]),
             ("4 años: pico de edad de la LLA", ["LMA"])],
   "final": ("LEUCEMIA LINFOBLÁSTICA AGUDA", ["Frotis y mielograma (≥ 20% blastos)", "Inmunofenotipo"]),
   "nota": "Dolor óseo nocturno + citopenias en un niño: no dar corticoides antes del mielograma."},
  ["La LMA es más frecuente en adultos.",
   "Pronóstico favorable entre 1 y 10 años con leucocitos < 50 000.",
   "Riesgo de síndrome de lisis tumoral al iniciar quimioterapia."],
  NELSON + " · NCCN – Pediatric acute lymphoblastic leukemia (2025)")

# NRL-025 · tarjetas
V("tarjetas", "NRL-025", "masa-realce-anillo-necrosis-glioblastoma", "Lesión con realce en anillo",
  "NEUROLOGÍA ENAM: GLIOBLASTOMA", "NEUROLOGÍA",
  ("Lesiones cerebrales con realce en anillo", ["Masa única, necrosis central y edema en un adulto mayor",
   "El tumor primario maligno más frecuente del adulto es el glioblastoma"]),
  ("Mujer de 78 años con 8 meses de cefalea y confusión", ["Apraxia del vestir, hemianopsia izquierda", "TC: masa parietal derecha con realce en anillo y necrosis"]),
  {"rotulo": "¿Qué lesión es?", "ans": 0, "cards": [
      {"titulo": "GLIOBLASTOMA", "datos": [
          ("Terreno", "Adulto mayor", True), ("Número", "Única", True),
          ("TC", "Anillo irregular, necrosis", True)],
       "pie": "Cirugía + radio-quimioterapia"},
      {"titulo": "Metástasis", "datos": [
          ("Terreno", "Cáncer conocido", False), ("Número", "Múltiples", False),
          ("TC", "Unión sustancia gris-blanca", False)],
       "pie": "Pulmón, mama, melanoma"},
      {"titulo": "Absceso", "datos": [
          ("Terreno", "Fiebre, foco infeccioso", False), ("Número", "Única o varias", False),
          ("TC", "Anillo fino, liso", False)],
       "pie": "Restricción en difusión"},
      {"titulo": "Linfoma / toxoplasma", "datos": [
          ("Terreno", "VIH", False), ("Número", "Varias", False),
          ("TC", "Periventricular / ganglios basales", False)],
       "pie": "Según CD4"}]},
  ["Meningioma: extraaxial, con cola dural, crecimiento lento.",
   "La biopsia confirma: astrocitoma grado 4 IDH-nativo.",
   "Sobrevida media de 15 meses con tratamiento."],
  "EANO – Guideline on the diagnosis and management of glioma (Nat Rev Clin Oncol 2021) · OMS – Clasificación de tumores del SNC 5.ª ed. (2021)")

# REU-026 · puntaje
V("puntaje", "REU-026", "debilidad-proximal-heliotropo-dermatomiositis", "Dermatomiositis: criterios",
  "REUMATOLOGÍA ENAM: DERMATOMIOSITIS", "REUMATOLOGÍA",
  ("Dermatomiositis", ["Debilidad proximal simétrica + lesiones cutáneas típicas",
   "Eritema en heliotropo, pápulas de Gottron y signo del chal o del escote"]),
  ("Mujer de 53 años con 2 meses de debilidad proximal", ["Exantema violáceo en párpados", "Exantema en cuello y pecho"]),
  {"rotulo": "Criterios de Bohan y Peter en el caso", "escala": "Bohan y Peter", "total": 2, "max": 5,
   "total_label": "Criterios presentes",
   "interpreta": "Clínica típica: completar CK, EMG y biopsia",
   "items": [("Lesiones cutáneas típicas", "1", True), ("Debilidad proximal simétrica", "1", True),
             ("CK elevada", "1", False), ("EMG miopática", "1", False), ("Biopsia con inflamación", "1", False)],
   "bandas": [("Piel + 1", "Posible", "Completar estudio", True),
              ("Piel + 2", "Probable", "Corticoides", False),
              ("Piel + 3", "Definida", "Corticoides + ahorrador", False)]},
  ["En adultos buscar cáncer asociado (ovario, pulmón, gástrico).",
   "Tratamiento: prednisona + metotrexato o azatioprina.",
   "Lupus discoide y esclerodermia no causan miopatía proximal marcada."],
  "EULAR/ACR – Classification criteria for idiopathic inflammatory myopathies (Ann Rheum Dis 2017)")

# SP-059 · termómetro
V("termometro", "SP-059", "covid-casos-esperados-vacunados-endemia", "Niveles de ocurrencia de una enfermedad",
  "SALUD PÚBLICA ENAM: ENDEMIA", "SALUD PÚBLICA",
  ("Niveles de ocurrencia", ["Endemia: casos presentes de forma constante y dentro de lo esperado",
   "Epidemia: casos por encima de lo esperado"]),
  ("DIRIS con > 95% de vacunados contra COVID-19", ["Siguen casos leves a moderados", "Dentro de la incidencia esperada"]),
  {"rotulo": "Frecuencia frente a lo esperado",
   "niveles": [("Aislados", "Esporádico", ["Casos sin patrón"]),
               ("Esperado", "Endémico", ["ENDEMIA", "Constante, predecible"]),
               ("> esperado", "Epidémico", ["Brote o epidemia"]),
               ("Mundial", "Pandémico", ["Varios continentes"])],
   "caso_nivel": 1, "ruta_titulo": "Cómo se reconoce", "paso_label": "PASO",
   "pasos": [(1, "Comparar con el canal endémico", ["Casos dentro de lo esperado"], True),
             (2, "Si supera el umbral: epidemia", ["Activar acciones"], False),
             (3, "Mantener vigilancia", ["Notificación semanal"], False)]},
  ["El canal endémico usa los datos de 5-7 años previos.",
   "La OMS terminó la emergencia internacional por COVID-19 en mayo de 2023.",
   "Brote: dos o más casos relacionados en tiempo y lugar."],
  "OPS – Módulos de principios de epidemiología para el control de enfermedades (MOPECE, 2.ª ed.)")

# GIN-089 · radial
V("radial", "GIN-089", "hiperemesis-confusion-ataxia-nistagmo-tiamina", "Complicaciones de la hiperémesis",
  "OBSTETRICIA ENAM: ENCEFALOPATÍA DE WERNICKE EN LA HIPERÉMESIS", "OBSTETRICIA",
  ("Hiperémesis gravídica complicada", ["Vómitos prolongados agotan la tiamina",
   "Confusión + ataxia + alteración ocular = encefalopatía de Wernicke"]),
  ("Gestante de 12 semanas con 5 días de vómitos", ["Confusión y ataxia", "Movimientos oculares involuntarios"]),
  {"rotulo": "Mapa del tema", "centro": "HIPERÉMESIS", "centro_sub": "Complicaciones", "ans": 0,
   "items": [("WERNICKE", ["Déficit de tiamina", "Confusión, ataxia, nistagmo"]),
             ("Hipokalemia", ["Alcalosis metabólica"]),
             ("Hiponatremia", ["Corrección lenta"]),
             ("Mallory-Weiss", ["Hematemesis"]),
             ("Pérdida de peso", ["> 5% del peso"])],
   "ruta": ["Vómitos persistentes", "Agotamiento de tiamina", "Confusión, ataxia y nistagmo", "WERNICKE"]},
  ["Dar tiamina ANTES de la glucosa EV.",
   "Tiamina 100 mg EV diarios en toda hiperémesis prolongada.",
   "Sin tratamiento evoluciona a psicosis de Korsakoff."],
  "RCOG – Green-top Guideline N.° 69: Nausea, vomiting and hyperemesis gravidarum (2024)")

# END-025 · fases
V("fases", "END-025", "hipotiroidismo-tsh-52-levotiroxina", "Hipotiroidismo: iniciar levotiroxina",
  "ENDOCRINOLOGÍA ENAM: HIPOTIROIDISMO PRIMARIO", "ENDOCRINOLOGÍA",
  ("Tratamiento del hipotiroidismo", ["TSH alta + T4 libre baja = hipotiroidismo primario",
   "Se trata con levotiroxina (T4) y se ajusta según la TSH"]),
  ("Mujer de 58 años con fatiga y estreñimiento", ["Facies edematosa, piel seca, reflejo lento", "TSH 52 · T4 libre 0.3"]),
  {"rotulo": "Plan de tratamiento", "ans": 0,
   "fases": [("Inicio", "Día 1", "LEVOTIROXINA", ["1.6 µg/kg/día", "Menos en ancianos o cardiópatas"]),
             ("Control", "6-8 sem", "Medir TSH", ["Ajustar 12.5-25 µg"]),
             ("Meta", "Meses", "TSH normal", ["0.5-4 mU/L"]),
             ("Seguimiento", "Anual", "TSH", ["Dosis estable"])],
   "curvas": [("TSH", ROSE, [0.95, 0.8, 0.55, 0.35, 0.25, 0.2, 0.2])],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Levotiroxina (T4)", True), ("Triyodotironina", False), ("T4 + T3", False), ("Tiroglobulina", False)]},
  ["Tomar en ayunas, 30-60 minutos antes del desayuno.",
   "La T3 sola tiene vida media corta y no se recomienda.",
   "En cardiopatía isquémica: empezar con 12.5-25 µg."],
  "ATA – Guidelines for the treatment of hypothyroidism (Thyroid 2014)")

# END-026 · matriz
V("matriz", "END-026", "sincope-ortostatico-hiperpigmentacion-hiperkalemia-addison", "Insuficiencia suprarrenal",
  "ENDOCRINOLOGÍA ENAM: INSUFICIENCIA SUPRARRENAL PRIMARIA", "ENDOCRINOLOGÍA",
  ("Insuficiencia suprarrenal", ["Primaria (Addison): falta cortisol y aldosterona",
   "Hiperpigmentación + hiponatremia + hiperkalemia + hipotensión"]),
  ("Mujer de 24 años con 3 síncopes", ["Antecedente de TB · hipotensión ortostática", "Hiperpigmentación · Na 130, K 6.3"]),
  {"rotulo": "Primaria vs secundaria", "eje_x": "Tipo", "eje_y": "Rasgo",
   "cols": ["Primaria (Addison)", "Secundaria"], "rows": ["Hiperpigmentación", "Potasio", "ACTH", "Causa"], "caso": (1, 0),
   "cells": [[("Sí", ["ACTH alta"]), ("No", [])],
             [("ALTO", ["Falta aldosterona"]), ("Normal", [])],
             [("Alta", []), ("Baja", [])],
             [("Autoinmune, TB", []), ("Corticoides, hipófisis", [])]]},
  ["En el Perú la tuberculosis suprarrenal sigue siendo causa frecuente.",
   "Confirmar con cortisol basal bajo y prueba de ACTH.",
   "Tratamiento: hidrocortisona + fludrocortisona."],
  "Endocrine Society – Diagnosis and treatment of primary adrenal insufficiency (J Clin Endocrinol Metab 2016)")

# SP-060 · radial
V("radial", "SP-060", "salud-trabajadores-medicina-ocupacional", "Salud ocupacional",
  "SALUD PÚBLICA ENAM: MEDICINA OCUPACIONAL", "SALUD PÚBLICA",
  ("Disciplinas de la salud ocupacional", ["La medicina ocupacional gestiona promoción, prevención y control de la salud del trabajador",
   "Las demás se enfocan en el ambiente o los accidentes"]),
  ("Pregunta de concepto", ["Disciplina que gestiona promoción, prevención", "y control de la salud de quienes trabajan"]),
  {"rotulo": "Mapa del tema", "centro": "SALUD OCUPACIONAL", "centro_sub": "Disciplinas", "ans": 0,
   "items": [("MEDICINA OCUPACIONAL", ["Salud del trabajador", "Exámenes, vigilancia"]),
             ("Higiene industrial", ["Agentes del ambiente", "Ruido, polvo, químicos"]),
             ("Seguridad ocupacional", ["Prevenir accidentes"]),
             ("Ergonomía", ["Adaptar el puesto"]),
             ("Psicología laboral", ["Riesgos psicosociales"])],
   "ruta": ["Promoción y prevención", "Control de la salud", "De las personas que trabajan", "MEDICINA OCUPACIONAL"]},
  ["La Ley 29783 regula la seguridad y salud en el trabajo en el Perú.",
   "Exámenes médicos ocupacionales: preempleo, periódicos y de retiro.",
   "La higiene industrial mide y controla los agentes ambientales."],
  "Ley N.° 29783 – Ley de seguridad y salud en el trabajo · OMS – Salud ocupacional")

# CAR-036 · fases
V("fases", "CAR-036", "centro-comercial-paro-dea-desfibrilacion", "Cadena de supervivencia",
  "CARDIOLOGÍA ENAM: DESFIBRILACIÓN PRECOZ", "CARDIOLOGÍA",
  ("Paro cardiaco extrahospitalario", ["En adultos con cardiopatía, el ritmo inicial suele ser fibrilación ventricular",
   "Con un DEA disponible: RCP y descarga lo antes posible"]),
  ("Varón de 55 años coronario en un centro comercial", ["Dolor torácico y pérdida súbita de conciencia", "Hay DEA disponible"]),
  {"rotulo": "Eslabones de la cadena", "ans": 2,
   "fases": [("Reconocer", "Segundos", "Llamar a emergencia", ["No responde, no respira"]),
             ("RCP", "Inmediata", "Compresiones", ["100-120/min, 5-6 cm"]),
             ("DEA", "< 3-5 min", "DESFIBRILAR", ["Descarga si ritmo desfibrilable"]),
             ("Avanzado", "Ambulancia", "Soporte vital", ["Posparo"])],
   "curvas": [("Sobrevida", SKY, [0.95, 0.85, 0.7, 0.55, 0.4, 0.28, 0.18])],
   "chips_titulo": "Medida inmediata · marcada la correcta",
   "chips": [("Desfibrilar con DEA", True), ("Solo masaje", False), ("Boca a boca", False), ("Esperar ambulancia", False)]},
  ["Cada minuto sin desfibrilación reduce la sobrevida un 7-10%.",
   "Minimizar pausas: reiniciar compresiones justo después de la descarga.",
   "Los testigos no entrenados pueden hacer solo compresiones."],
  "AHA – Guidelines for cardiopulmonary resuscitation and emergency cardiovascular care (2025) · ERC Guidelines (2021)")
