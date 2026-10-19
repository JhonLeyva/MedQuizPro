"""Bloque 7 · parte I."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"

# CIR-104 · embudo
V("embudo", "CIR-104", "anciano-melena-dolor-difuso-neumatosis-ldh-isquemia-mesenterica", "Dolor abdominal grave en el anciano vascular",
  "CIRUGÍA ENAM: ISQUEMIA MESENTÉRICA AGUDA", "CIRUGÍA",
  ("Isquemia mesentérica aguda", ["Dolor intenso, al inicio desproporcionado al examen, en un anciano vascular",
   "Neumatosis, LDH y lactato altos indican necrosis intestinal"]),
  ("Hipertenso de 81 años", ["Melena y dolor epigástrico que se hace difuso", "Irritación peritoneal · neumatosis · leucocitos 17 000 · LDH 1082"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Abdomen agudo con sangrado en un anciano",
   "candidatos": ["Isquemia mesentérica", "Pancreatitis aguda", "Diverticulitis", "Obstrucción intestinal"],
   "pasos": [("Neumatosis intestinal en la Rx", ["Pancreatitis aguda", "Obstrucción intestinal"]),
             ("Dolor epigástrico difuso con melena, no en FII", ["Diverticulitis"])],
   "final": ("ISQUEMIA MESENTÉRICA AGUDA", ["Angio-TC de abdomen", "Laparotomía: resecar el intestino necrótico"]),
   "nota": "La neumatosis indica que el intestino ya está necrosado: mal pronóstico."},
  ["Causas: embolia (FA), trombosis arterial, trombosis venosa, no oclusiva.",
   "Anticoagular con heparina desde la sospecha.",
   "La mortalidad supera el 50 % si se diagnostica tarde."],
  "ESVS – Clinical practice guidelines on the management of diseases of mesenteric arteries and veins (2017) · WSES (2022)")

# GIN-192 · árbol
A("GIN-192", "legrado-perforacion-histerometro-sin-sangrado-observar", "Perforación uterina durante el legrado",
  "GINECOLOGÍA ENAM: PERFORACIÓN UTERINA", "GINECOLOGÍA",
  ("Perforación uterina", ["Con instrumento romo (histerómetro) y sin sangrado: suele cerrar sola",
   "Con cureta o aspirador, sangrado o inestabilidad: explorar"]),
  ("Legrado por aborto incompleto", ["Perforación con el histerómetro", "Sin sangrado activo externo"]),
  Q("¿Instrumento romo, sin sangrado ni inestabilidad?", [
      L("Sí", "CONTROL DE FUNCIONES VITALES", ["Observar 24 h", "Oxitócico y antibiótico según caso"], path=True),
      L("No: cureta, sangrado o choque", "Laparoscopía o laparotomía", ["Revisar vísceras y suturar"])], path=True),
  ("Riesgo según el instrumento", [("Histerómetro", True), ("Cureta o aspirador", False)], [
      ("Daño a vísceras", ["Raro", "Posible (asa, vejiga)"]),
      ("Conducta", ["Observación", "Exploración quirúrgica"])]),
  ["Signos de alarma: dolor que aumenta, taquicardia, hipotensión, fiebre.",
   "Completar la evacuación bajo control ecográfico o laparoscópico.",
   "No se transfunde sin evidencia de sangrado."],
  WILLIAMS + " · RCOG – Consent advice: surgical management of miscarriage (2018)")

# NEU-054 · árbol
A("NEU-054", "puerpera-tb-en-tratamiento-lactancia-con-mascarilla", "Lactancia en la madre con tuberculosis",
  "NEUMOLOGÍA ENAM: TUBERCULOSIS Y LACTANCIA", "NEUMOLOGÍA",
  ("Madre con tuberculosis", ["La TB no se transmite por la leche",
   "Con tratamiento en curso: dar de lactar usando mascarilla"]),
  ("Puérpera inmediata", ["En tratamiento de TB sensible desde el tercer trimestre", "Pregunta si puede amamantar"]),
  Q("¿Recibe tratamiento antituberculoso?", [
      L("Sí", "LACTANCIA CON MASCARILLA", ["Mascarilla quirúrgica o de tela", "Evaluar al RN y dar terapia preventiva"], path=True),
      L("No: bacilífera sin tratar", "Iniciar tratamiento", ["Leche extraída hasta ser no contagiosa"])], path=True),
  ("Cuidados del recién nacido", [("Medida", True), ("Detalle", False)], [
      ("Descartar TB", ["Clínica y Rx", "Si está sano: prevención"]),
      ("Isoniacida", ["6 meses", "Luego BCG si no la recibió"]),
      ("Lactancia", ["Continuar", "Los fármacos pasan poco a la leche"])]),
  ["El N95 es para el personal de salud, no para la madre.",
   "Los sucedáneos no están indicados: se pierde la protección de la leche.",
   "La madre ventila la habitación y cubre la tos."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · OMS – Breastfeeding and maternal tuberculosis (2008)")

# PED-189 · fases
V("fases", "PED-189", "lactante-1-mes-parto-domiciliario-sangrado-vitamina-k", "Hemorragia por falta de vitamina K",
  "PEDIATRÍA ENAM: ENFERMEDAD HEMORRÁGICA TARDÍA", "PEDIATRÍA",
  ("Sangrado por déficit de vitamina K", ["El RN nace con poca vitamina K y la leche materna aporta poca",
   "Sin profilaxis al nacer: sangrado, incluso intracraneal"]),
  ("Lactante de 1 mes con lactancia exclusiva", ["Parto domiciliario (sin vitamina K)", "Sangrado oral, vómitos con sangre, palidez, llanto persistente"]),
  {"rotulo": "Formas según la edad", "ans": 2,
   "fases": [("Precoz", "< 24 h", "Fármacos maternos", ["Anticonvulsivantes, warfarina"]),
             ("Clásica", "2-7 días", "Sangrado digestivo", ["Ombligo, circuncisión"]),
             ("Tardía", "2-12 semanas", "DÉFICIT DE VITAMINA K", ["Lactancia exclusiva sin profilaxis", "Riesgo de hemorragia cerebral"])],
   "curvas": [],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Déficit de vitamina K", True), ("CID", False), ("Hemofilia", False), ("Déficit de proteína C", False)]},
  ["Prevención: vitamina K 1 mg IM al nacer a todo RN.",
   "Tratamiento: vitamina K EV y plasma si sangra mucho.",
   "El llanto persistente obliga a descartar hemorragia intracraneal (TC)."],
  "AAP – Policy statement: vitamin K and the newborn (2022) · " + NELSON)

# NRL-050 · tarjetas
V("tarjetas", "NRL-050", "anciano-temblor-reposo-reemergente-bradicinesia-parkinsoniano", "Tipos de temblor",
  "NEUROLOGÍA ENAM: TEMBLOR PARKINSONIANO", "NEUROLOGÍA",
  ("Temblor parkinsoniano", ["De reposo, 4-6 Hz; cede al iniciar el movimiento y reaparece al mantener la postura",
   "Acompañado de bradicinesia y rigidez"]),
  ("Varón de 78 años", ["Temblor de manos que cede al levantar la taza y reaparece cerca de la boca", "Bradicinesia"]),
  {"rotulo": "¿Qué temblor es?", "ans": 0, "cards": [
      {"titulo": "PARKINSONIANO", "datos": [
          ("Cuándo", "Reposo, reemergente", True), ("Asociado", "Bradicinesia", True),
          ("Alcohol", "Sin efecto", False), ("Tratamiento", "Levodopa", False)],
       "pie": "Asimétrico al inicio"},
      {"titulo": "Esencial", "datos": [
          ("Cuándo", "Postural y de acción", False), ("Asociado", "Antecedente familiar", False),
          ("Alcohol", "Mejora", False), ("Tratamiento", "Propranolol", False)],
       "pie": "El más frecuente"},
      {"titulo": "Cerebeloso", "datos": [
          ("Cuándo", "Intención, al llegar", False), ("Asociado", "Ataxia, dismetría", False),
          ("Alcohol", "Puede empeorar", False), ("Tratamiento", "Causa", False)],
       "pie": "Lesión cerebelosa"},
      {"titulo": "Fisiológico exagerado", "datos": [
          ("Cuándo", "Postural fino", False), ("Asociado", "Ansiedad, café", False),
          ("Alcohol", "Abstinencia", False), ("Tratamiento", "Retirar causa", False)],
       "pie": "Tiroides, fármacos"}]},
  ["El temblor reemergente es típico del Parkinson.",
   "Diagnóstico clínico: bradicinesia + temblor de reposo o rigidez.",
   "Si mejora claramente con levodopa, se apoya el diagnóstico."],
  "MDS – Clinical diagnostic criteria for Parkinson's disease (2015)")

# SP-143 · matriz
V("matriz", "SP-143", "obesidad-escolar-campo-deportivo-cuidado-comunitario", "Niveles del cuidado de la salud",
  "SALUD PÚBLICA ENAM: CUIDADO COMUNITARIO", "SALUD PÚBLICA",
  ("Cuidado comunitario", ["Intervención sobre un factor de riesgo común de una población",
   "Modifica el entorno: por ejemplo, un campo deportivo en el distrito"]),
  ("Centro de salud", ["Aumenta el sobrepeso en escolares de 5-9 años", "Se promueve un campo deportivo en el distrito"]),
  {"rotulo": "Tipo de cuidado", "eje_x": "Rasgo", "eje_y": "Cuidado",
   "cols": ["A quién", "Ejemplo"], "rows": ["Comunitario", "Familiar", "Individual", "Asistencial"], "caso": (0, 1),
   "cells": [[("Población o comunidad", []), ("CAMPO DEPORTIVO", ["Cambia el entorno"])],
             [("Grupo familiar", []), ("Consejería en casa", [])],
             [("Una persona", []), ("Plan de dieta", [])],
             [("Paciente enfermo", []), ("Tratamiento en consulta", [])]]},
  ["El modelo MAIS-BFC trabaja los tres niveles: persona, familia y comunidad.",
   "Los entornos saludables son una línea de la promoción de la salud.",
   "Involucrar al municipio y a la escuela."],
  "MINSA – Modelo de atención integral de salud basado en familia y comunidad (MAIS-BFC, 2011)")

# OFT-044 · embudo
V("embudo", "OFT-044", "hisopo-hipoacusia-tinnitus-tapon-cerumen", "Hipoacusia súbita tras limpiarse el oído",
  "OTORRINOLARINGOLOGÍA ENAM: TAPÓN DE CERUMEN", "OTORRINOLARINGOLOGÍA",
  ("Tapón de cerumen", ["El hisopo empuja el cerumen hacia dentro y lo compacta",
   "Hipoacusia de conducción, sensación de oído tapado y tinnitus"]),
  ("Varón de 65 años", ["2 días de hipoacusia y tinnitus en el oído derecho", "Se limpia los oídos con hisopo tras el baño"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hipoacusia unilateral reciente",
   "candidatos": ["Tapón de cerumen", "Otitis externa", "Otitis media", "Hipoacusia neurosensorial"],
   "pasos": [("Sin dolor, fiebre ni secreción", ["Otitis externa", "Otitis media"]),
             ("Tras uso de hisopo, de tipo conductivo", ["Hipoacusia neurosensorial"])],
   "final": ("TAPÓN DE CERUMEN", ["Otoscopia confirma", "Gotas ablandadoras y lavado o extracción"]),
   "nota": "Si la hipoacusia súbita es neurosensorial, es una urgencia: corticoides."},
  ["No lavar si hay perforación timpánica conocida.",
   "Desaconsejar los hisopos: el oído se limpia solo.",
   "Weber lateraliza al oído tapado (conducción)."],
  "AAO-HNS – Clinical practice guideline: Earwax (cerumen impaction) (2017)")

# INF-093 · árbol
A("INF-093", "gestante-vih-ppd-6-mm-isoniacida-6-meses", "Infección tuberculosa latente en la gestante con VIH",
  "INFECTOLOGÍA ENAM: TERAPIA PREVENTIVA EN VIH", "INFECTOLOGÍA",
  ("Tuberculosis latente en VIH", ["En VIH el PPD ≥ 5 mm ya es positivo",
   "Sin TB activa: terapia preventiva con isoniacida (también en el embarazo)"]),
  ("Gestante de 14 semanas asintomática", ["VIH positivo", "Tuberculina > 6 mm"]),
  Q("¿Síntomas o Rx sugestivos de TB activa?", [
      L("Sí", "Tratar TB activa", ["Esquema HRZE"]),
      Q("¿PPD ≥ 5 mm (VIH)?", [
          L("Sí", "ISONIACIDA 6 MESES", ["+ piridoxina", "Terapia preventiva"], path=True),
          L("No", "Considerar igual en VIH", ["Según norma MINSA"])], edge="No", path=True)], path=True),
  ("Punto de corte del PPD", [("≥ 5 mm", True), ("≥ 10 mm", False)], [
      ("Para quién", ["VIH, contactos, inmunodeprimidos", "Población general"]),
      ("Conducta", ["Terapia preventiva", "Evaluar riesgo"])]),
  ["La isoniacida es segura en el embarazo; agregar piridoxina.",
   "Descartar siempre TB activa antes de dar monoterapia.",
   "Vigilar hepatotoxicidad, sobre todo en el embarazo y posparto."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · OMS – TB preventive treatment, módulo 1 (2024)")

# HEM-037 · matriz
V("matriz", "HEM-037", "anciana-deterioro-cognitivo-vcm-105-pancitopenia-b12", "Anemia macrocítica con alteración mental",
  "HEMATOLOGÍA ENAM: DÉFICIT DE VITAMINA B12", "HEMATOLOGÍA",
  ("Anemia megaloblástica", ["VCM alto + pancitopenia por falla de la síntesis de ADN",
   "La B12 además daña el sistema nervioso: demencia, neuropatía"]),
  ("Mujer de 71 años", ["2 meses de deterioro mental y anorexia", "Hb 8,5 · VCM 105 · leucocitos 3500 · plaquetas 80 000"]),
  {"rotulo": "B12 vs folato", "eje_x": "Déficit", "eje_y": "Rasgo",
   "cols": ["Vitamina B12", "Ácido fólico"], "rows": ["Síntomas neurológicos", "Causa típica", "Tratamiento"], "caso": (2, 0),
   "cells": [[("Sí: demencia, neuropatía", ["Degeneración combinada"]), ("No", [])],
             [("Anemia perniciosa, edad", ["Metformina, gastrectomía"]), ("Dieta pobre, alcohol", [])],
             [("CIANOCOBALAMINA", ["IM al inicio"]), ("Ácido fólico oral", [])]]},
  ["Dar solo ácido fólico en un déficit de B12 empeora el daño neurológico.",
   "Ácido metilmalónico alto confirma el déficit de B12.",
   "Frotis: macroovalocitos y neutrófilos hipersegmentados."],
  "British Society for Haematology – Guideline for the diagnosis and treatment of cobalamin and folate disorders (2014) · " + HARRISON)

# SP-144 · radial
V("radial", "SP-144", "monitoreo-desempeno-evidencias-verificables-objetivo", "Características del monitoreo",
  "SALUD PÚBLICA ENAM: MONITOREO DE LA GESTIÓN", "SALUD PÚBLICA",
  ("Monitoreo del desempeño", ["Seguimiento de indicadores de gestión",
   "Si se basa en evidencias verificables, es objetivo"]),
  ("Gestión de establecimientos", ["El monitoreo debe sustentarse en evidencias verificables"]),
  {"rotulo": "Mapa del tema", "centro": "MONITOREO", "centro_sub": "Cualidades", "ans": 0,
   "items": [("OBJETIVO", ["Basado en evidencias verificables", "Sin opiniones subjetivas"]),
             ("Permanente", ["Continuo en el tiempo"]),
             ("Dinámico", ["Se adapta a cambios"]),
             ("Analítico", ["Interpreta los datos"]),
             ("Participativo", ["Incluye al equipo"])],
   "ruta": ["Evidencias verificables", "Datos medibles", "Sin sesgo del evaluador", "OBJETIVO"]},
  ["Monitoreo: seguimiento continuo; evaluación: juicio en un momento dado.",
   "Los indicadores deben ser medibles y comparables.",
   "La supervisión añade acompañamiento y capacitación."],
  "MINSA – Directiva de monitoreo y evaluación de la gestión (2019) · OPS – Monitoreo de servicios de salud (2017)")

# PED-190 · fases
V("fases", "PED-190", "rn-perine-plano-sin-orificio-anal-colostomia", "Malformación anorrectal alta",
  "PEDIATRÍA ENAM: MALFORMACIÓN ANORRECTAL", "PEDIATRÍA",
  ("Malformación anorrectal", ["Baja: fístula visible en el periné → anoplastia",
   "Alta (periné plano, sin fístula visible): colostomía primero"]),
  ("RN de 16 horas", ["Distensión, vómitos biliosos, sin deposiciones", "Sin orificio anal · periné plano · pliegue glúteo poco visible"]),
  {"rotulo": "Tratamiento por etapas", "ans": 0,
   "fases": [("1", "Recién nacido", "COLOSTOMÍA SIGMOIDEA", ["Descomprime el intestino", "Periné plano = defecto alto"]),
             ("2", "1-3 meses", "Anorrectoplastia", ["Sagital posterior (Peña)"]),
             ("3", "Semanas después", "Dilataciones", ["Calibrar el ano nuevo"]),
             ("4", "Final", "Cierre de colostomía", ["Tránsito normal"])],
   "curvas": [],
   "chips_titulo": "Conducta inicial · marcada la correcta",
   "chips": [("Colostomía sigmoidea", True), ("Anorrectoplastia inmediata", False), ("Reevaluar en 24 h", False), ("Fistulografía", False)]},
  ["Esperar 24 h permite ver si aparece meconio por una fístula; aquí ya hay obstrucción.",
   "Buscar malformaciones asociadas (VACTERL): eco renal, eco cardiaca, columna.",
   "Periné plano y sacro anormal = peor pronóstico de continencia."],
  "Holcomb and Ashcraft's Pediatric Surgery 7.ª ed. (2020) · " + NELSON)

# PSI-037 · tarjetas
V("tarjetas", "PSI-037", "nino-4-anos-despierta-panico-sin-recuerdo-terror-nocturno", "Despertares nocturnos en el niño",
  "PSIQUIATRÍA ENAM: TERRORES NOCTURNOS", "PSIQUIATRÍA",
  ("Terrores nocturnos", ["Parasomnia del sueño profundo (no REM) en preescolares",
   "Grito o pánico, se sienta, no se consuela y no lo recuerda al día siguiente"]),
  ("Niño de 4 años", ["Una vez por semana despierta de golpe con pánico y se sienta", "No lo recuerda · desarrollo normal"]),
  {"rotulo": "¿Qué parasomnia es?", "ans": 0, "cards": [
      {"titulo": "TERROR NOCTURNO", "datos": [
          ("Sueño", "No REM, 1.er tercio", True), ("Recuerdo", "No lo recuerda", True),
          ("Consuelo", "Difícil", False), ("Manejo", "Explicar, se autolimita", False)],
       "pie": "Desaparece con la edad"},
      {"titulo": "Pesadilla", "datos": [
          ("Sueño", "REM, madrugada", False), ("Recuerdo", "Recuerda el sueño", False),
          ("Consuelo", "Se calma", False), ("Manejo", "Tranquilizar", False)],
       "pie": "Relato del sueño"},
      {"titulo": "Sonambulismo", "datos": [
          ("Sueño", "No REM", False), ("Recuerdo", "No", False),
          ("Consuelo", "Camina dormido", False), ("Manejo", "Seguridad en casa", False)],
       "pie": "Puede coexistir"},
      {"titulo": "Epilepsia nocturna", "datos": [
          ("Sueño", "Cualquier fase", False), ("Recuerdo", "No", False),
          ("Consuelo", "Movimientos estereotipados", False), ("Manejo", "EEG", False)],
       "pie": "Muy frecuentes y repetitivas"}]},
  ["No despertar al niño durante el episodio.",
   "Mantener horarios regulares: la falta de sueño los favorece.",
   "Polisomnografía o EEG solo si son atípicos o muy frecuentes."],
  "AASM – International classification of sleep disorders ICSD-3 (2014) · " + NELSON)

# END-057 · puntaje
V("puntaje", "END-057", "postiroidectomia-parestesias-chvostek-calcio-serico", "Parestesias tras la tiroidectomía",
  "ENDOCRINOLOGÍA ENAM: HIPOCALCEMIA POSTIROIDECTOMÍA", "ENDOCRINOLOGÍA",
  ("Hipocalcemia tras tiroidectomía", ["Lesión o extirpación de las paratiroides: cae la PTH",
   "Parestesias peribucales, calambres, Chvostek y Trousseau"]),
  ("Mujer de 57 años, 2.º día tras tiroidectomía por cáncer", ["Parestesias y calambres en piernas y labios", "Chvostek positivo"]),
  {"rotulo": "Signos de hipocalcemia en el caso", "escala": "Signos de hipocalcemia", "total": 3, "max": 6,
   "total_label": "Signos presentes",
   "interpreta": "Hipocalcemia probable: medir calcio ya",
   "items": [("Parestesias peribucales", "✓", True), ("Calambres musculares", "✓", True),
             ("Signo de Chvostek", "✓", True), ("Signo de Trousseau", "—", False),
             ("Laringoespasmo o convulsión", "—", False), ("QT prolongado en ECG", "—", False)],
   "bandas": [("≥ 1", "Sospecha", "Calcio sérico (iónico) y PTH", True),
              ("Tetania", "Grave", "Gluconato de calcio EV", False)]},
  ["Leve: calcio oral + calcitriol; grave: gluconato de calcio EV.",
   "El potasio no produce Chvostek.",
   "La PTH baja en las primeras horas predice hipocalcemia."],
  "AAES – Guidelines for the definitive surgical management of thyroid disease (2020) · Endocrine Society – Hypoparathyroidism guideline (2022)")

# TRA-045 · fases
V("fases", "TRA-045", "escolar-herida-pierna-fiebre-dolor-persistente-radiografia", "Infección de la pierna que no termina de curar",
  "TRAUMATOLOGÍA ENAM: OSTEOMIELITIS SUBAGUDA", "TRAUMATOLOGÍA",
  ("Osteomielitis", ["Tras una herida o celulitis el germen puede llegar al hueso",
   "El dolor persistente pese a mejorar la fiebre obliga a buscar lesión ósea (Rx)"]),
  ("Escolar de 7 años de zona rural", ["Herida en la pantorrilla al caer de un árbol", "2 semanas después: eritema, fiebre y cojera; mejora con antibiótico, pero sigue el dolor"]),
  {"rotulo": "Evolución de la infección", "ans": 2,
   "fases": [("Herida", "Día 0", "Puerta de entrada", ["Contaminada"]),
             ("Celulitis", "Días", "Partes blandas", ["Eritema, fiebre"]),
             ("Subaguda", "2-6 semanas", "RADIOGRAFÍA", ["Lesión lítica, reacción perióstica", "Absceso de Brodie"]),
             ("Crónica", "Meses", "Secuestro óseo", ["Cirugía"])],
   "curvas": [("Dolor óseo", ROSE, [0.1, 0.3, 0.5, 0.65, 0.7, 0.75, 0.8])],
   "chips_titulo": "Examen de seguimiento · marcado el correcto",
   "chips": [("Radiografía de pierna", True), ("Hemocultivo", False), ("VSG", False), ("Hemograma", False)]},
  ["En la fase aguda la Rx puede ser normal: la RM es más sensible.",
   "Germen más frecuente: S. aureus.",
   "Tratamiento prolongado: 4-6 semanas de antibiótico."],
  "PIDS/IDSA – Guideline on acute hematogenous osteomyelitis in pediatrics (2021) · " + NELSON)

# GIN-193 · matriz
V("matriz", "GIN-193", "multipara-cabeza-flotante-amniotomia-prolapso-cordon", "Distocias del cordón",
  "OBSTETRICIA ENAM: PROLAPSO DE CORDÓN", "OBSTETRICIA",
  ("Prolapso de cordón", ["Al romper membranas con la cabeza alta, el líquido arrastra el cordón",
   "El cordón queda por delante de la presentación: emergencia"]),
  ("Gran multípara de 38 semanas", ["Dilatación 1 cm, cabeza flotante", "Se plantea amniotomía"]),
  {"rotulo": "Posición del cordón", "eje_x": "Rasgo", "eje_y": "Distocia",
   "cols": ["Membranas", "Qué es"], "rows": ["Prolapso", "Procúbito", "Laterocidencia"], "caso": (0, 1),
   "cells": [[("Rotas", []), ("CORDÓN DELANTE DE LA PRESENTACIÓN", ["Riesgo tras amniotomía"])],
             [("Íntegras", []), ("Cordón delante, dentro de la bolsa", [])],
             [("Rotas o íntegras", []), ("Al lado de la presentación", [])]]},
  ["No romper membranas con la cabeza flotante.",
   "Si ocurre: elevar la presentación con la mano y cesárea inmediata.",
   "Factores: multiparidad, polihidramnios, presentación anómala, prematuridad."],
  "RCOG – Green-top Guideline 50: Umbilical cord prolapse (2014) · " + WILLIAMS)

# INF-094 · puntaje
V("puntaje", "INF-094", "adolescente-infiltracion-orejas-atrofia-tenar-baar-mitsuda-negativo", "Lesiones infiltradas con anestesia",
  "INFECTOLOGÍA ENAM: LEPRA LEPROMATOSA", "INFECTOLOGÍA",
  ("Lepra (Mycobacterium leprae)", ["Afecta piel y nervios periféricos",
   "Lepromatosa: sin inmunidad celular (Mitsuda negativo), muchos bacilos"]),
  ("Adolescente de la región tropical", ["Lesiones infiltradas en frente, pómulos y orejas", "Anestesia y atrofia tenar e hipotenar · BAAR (+) · Mitsuda (−)"]),
  {"rotulo": "Datos de lepra multibacilar", "escala": "Hallazgos del caso", "total": 4, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Lepra lepromatosa (multibacilar)",
   "items": [("Baciloscopía positiva", "✓", True), ("Lesiones infiltradas difusas en cara y orejas", "✓", True),
             ("Varios nervios afectados (mediano, cubital)", "✓", True), ("Mitsuda negativo", "✓", True)],
   "bandas": [("Pauci", "Paucibacilar", "≤ 5 lesiones, BAAR (−)", False),
              ("Multi", "Multibacilar", "Rifampicina + clofazimina + dapsona 12 meses", True)]},
  ["Tuberculoide: pocas placas anestésicas, Mitsuda positivo, BAAR negativo.",
   "Facies leonina y madarosis en formas avanzadas.",
   "Es curable con poliquimioterapia gratuita."],
  "OMS – Guidelines for the diagnosis, treatment and prevention of leprosy (2018) · MINSA – NTS de lepra")

# GIN-194 · radial
V("radial", "GIN-194", "primigesta-7-cm-situacion-transversa-cesarea", "Situación transversa en trabajo de parto",
  "OBSTETRICIA ENAM: SITUACIÓN TRANSVERSA", "OBSTETRICIA",
  ("Situación transversa", ["El feto atravesado no puede nacer por vía vaginal",
   "En trabajo de parto con membranas rotas: cesárea"]),
  ("Primigesta de 39 semanas", ["Contracciones cada 3 min · 7 cm, 90 %, −4", "Feto transverso, dorso superior · membranas rotas"]),
  {"rotulo": "Mapa del tema", "centro": "FETO TRANSVERSO", "centro_sub": "¿Qué hacer?", "ans": 0,
   "items": [("CESÁREA", ["Trabajo de parto y bolsa rota", "Sin otra vía segura"]),
             ("Versión externa", ["Solo antes del parto, con bolsa íntegra"]),
             ("Oxitocina", ["Contraindicada: rotura uterina"]),
             ("Evolución espontánea", ["Hombro impactado"]),
             ("Versión interna", ["Solo 2.º gemelo"])],
   "ruta": ["Transverso", "7 cm", "Bolsa rota", "CESÁREA"]},
  ["Riesgos: prolapso de cordón o de brazo y rotura uterina.",
   "Causas: multiparidad, placenta previa, malformaciones uterinas.",
   "Detectarla con Leopold en controles prenatales."],
  WILLIAMS)

# GAS-065 · termómetro
V("termometro", "GAS-065", "cirrotico-fiebre-dolor-pmn-500-peritonitis-espontanea", "Infección del líquido ascítico",
  "GASTROENTEROLOGÍA ENAM: PERITONITIS BACTERIANA ESPONTÁNEA", "GASTROENTEROLOGÍA",
  ("Peritonitis bacteriana espontánea", ["Infección del líquido ascítico sin foco quirúrgico",
   "Diagnóstico: PMN ≥ 250/µl en el líquido"]),
  ("Varón de 62 años con cirrosis grave", ["3 días de fiebre, dolor difuso y somnolencia", "Líquido ascítico: 500 PMN/µl · glucosa 40"]),
  {"rotulo": "PMN en el líquido ascítico",
   "niveles": [("< 250", "Sin PBE", ["Ascitis no infectada"]),
               ("≥ 250", "PBE", ["500 PMN/µL", "Iniciar antibiótico"]),
               ("Muy alto", "Pensar en secundaria", ["Varios gérmenes, perforación"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Cefotaxima o ceftriaxona EV", ["5-7 días"], True),
             (2, "Albúmina EV días 1 y 3", ["Previene el síndrome hepatorrenal"], False),
             (3, "Profilaxis posterior", ["Norfloxacino o ciprofloxacino"], False)]},
  ["Paracentesis diagnóstica a todo cirrótico con ascitis que se hospitaliza.",
   "La somnolencia puede ser encefalopatía precipitada por la infección.",
   "Germen típico: E. coli y Klebsiella."],
  "AASLD – Guidance on ascites, SBP and hepatorenal syndrome (2021) · EASL (2018)")

# SP-145 · árbol
A("SP-145", "micronutrientes-colegio-control-cuasiexperimental", "¿Experimento o cuasiexperimento?",
  "SALUD PÚBLICA ENAM: DISEÑO CUASIEXPERIMENTAL", "SALUD PÚBLICA",
  ("Estudios de intervención", ["Experimental: el investigador interviene y asigna al azar",
   "Cuasiexperimental: interviene, pero sin aleatorizar (grupos ya formados)"]),
  ("Investigación en colegios", ["Más micronutrientes en el almuerzo de un colegio", "Otro colegio sirve de control"]),
  Q("¿El investigador aplica la intervención?", [
      L("No", "Observacional", ["Cohorte, casos y controles"]),
      Q("¿Asignación aleatoria de los sujetos?", [
          L("Sí", "Experimental", ["Ensayo clínico"]),
          L("No: colegios ya formados", "CUASIEXPERIMENTAL", ["Grupo intervención vs control", "Sin azar"], path=True)],
        edge="Sí", path=True)], path=True),
  ("Diseños de intervención", [("Cuasiexperimental", True), ("Experimental", False)], [
      ("Azar", ["No", "Sí"]),
      ("Grupo control", ["Sí, no equivalente", "Sí, equivalente"]),
      ("Validez interna", ["Menor", "Mayor"])]),
  ["Ecológico: compara poblaciones con datos agregados, sin intervenir.",
   "Histórico: revisa hechos pasados.",
   "Medir el estado nutricional antes y después en ambos grupos."],
  "Hernández-Sampieri. Metodología de la investigación 7.ª ed. (2023) · " + GORDIS)

# INF-095 · embudo
V("embudo", "INF-095", "obeso-placa-eritematosa-pantorrilla-fiebre-celulitis", "Pierna roja y caliente con fiebre",
  "INFECTOLOGÍA ENAM: CELULITIS", "INFECTOLOGÍA",
  ("Celulitis", ["Infección de dermis profunda y tejido subcutáneo",
   "Placa eritematosa caliente de bordes mal definidos, con fiebre"]),
  ("Varón de 40 años con IMC 38", ["Fiebre y dolor en la pierna derecha desde ayer", "Placa eritematosa de bordes irregulares · Homans (−)"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Pierna roja, caliente y dolorosa",
   "candidatos": ["Celulitis", "TVP", "Erisipela", "Fascitis necrotizante"],
   "pasos": [("Fiebre con placa inflamatoria, Homans (−)", ["TVP"]),
             ("Bordes irregulares, no sobreelevados", ["Erisipela"]),
             ("Sin dolor desproporcionado, crepitación ni necrosis", ["Fascitis necrotizante"])],
   "final": ("CELULITIS", ["S. aureus o estreptococo", "Cefalexina o cefazolina; elevar la pierna"]),
   "nota": "La obesidad, el edema y el pie de atleta son puertas de entrada frecuentes."},
  ["Erisipela: borde sobreelevado y bien definido (estreptococo).",
   "Marcar el borde para ver si avanza.",
   "Tratar la tiña interdigital para evitar recurrencias."],
  "IDSA – Practice guidelines for skin and soft tissue infections (2014)")

# PED-191 · termómetro
V("termometro", "PED-191", "preescolar-diarrea-sodio-160-calcular-deficit", "Deshidratación con sodio alto",
  "PEDIATRÍA ENAM: DESHIDRATACIÓN HIPERNATRÉMICA", "PEDIATRÍA",
  ("Deshidratación hipernatrémica", ["Se pierde más agua que sodio",
   "Hay que calcular el déficit y corregir lento: el sodio no debe bajar > 10-12 mEq/L al día"]),
  ("Preescolar de 2 años con 3 días de diarrea", ["Irritable, deshidratación moderada", "Na 160 · K 5"]),
  {"rotulo": "Sodio sérico",
   "niveles": [("< 130", "Hiponatrémica", ["Convulsiones si baja rápido"]),
               ("130-150", "Isonatrémica", ["La más frecuente"]),
               ("> 150", "Hipernatrémica", ["NA 160", "Riesgo de edema cerebral al corregir"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Calcular el déficit de agua y sodio", ["Reponer en 48 h o más"], True),
             (2, "SRO si tolera la vía oral", ["Es segura y eficaz"], False),
             (3, "Controlar el sodio cada 4-6 h", ["Bajada ≤ 10-12 mEq/L en 24 h"], False)]},
  ["Corregir rápido causa edema cerebral y convulsiones.",
   "Los diuréticos no tienen lugar: el niño está deshidratado.",
   "No se dan antibióticos en la diarrea acuosa."],
  "OMS – Tratamiento de la diarrea (2005) · " + NELSON)

# SP-146 · termómetro
V("termometro", "SP-146", "busqueda-activa-sintomaticos-respiratorios-prevencion-secundaria", "Niveles de prevención",
  "SALUD PÚBLICA ENAM: PREVENCIÓN SECUNDARIA", "SALUD PÚBLICA",
  ("Prevención secundaria", ["Detectar la enfermedad temprano y tratarla",
   "Buscar sintomáticos respiratorios es diagnóstico precoz de TB"]),
  ("Distrito pobre y hacinado", ["Aumenta la TB pulmonar", "Búsqueda activa de sintomáticos respiratorios"]),
  {"rotulo": "Nivel de prevención",
   "niveles": [("Primaria", "Evitar la enfermedad", ["BCG, ventilación"]),
               ("Secundaria", "Detección precoz", ["BUSCAR SINTOMÁTICOS", "Baciloscopía y tratamiento"]),
               ("Terciaria", "Limitar secuelas", ["Rehabilitación"]),
               ("Cuaternaria", "Evitar sobreintervención", ["Iatrogenia"])],
   "caso_nivel": 1, "ruta_titulo": "Actividad", "paso_label": "PASO",
   "pasos": [(1, "Identificar tosedores ≥ 15 días", ["En la comunidad y en el establecimiento"], True),
             (2, "Baciloscopía o prueba molecular", ["2 muestras de esputo"], False),
             (3, "Tratar y estudiar contactos", ["Corta la cadena de transmisión"], False)]},
  ["Sintomático respiratorio: tos con flema ≥ 15 días.",
   "La terapia preventiva de contactos es prevención primaria.",
   "El hacinamiento y la pobreza son determinantes sociales."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · Leavell y Clark")

# CIR-105 · termómetro
V("termometro", "CIR-105", "quemadura-tercer-grado-mayor-20-unidad-quemados", "¿Cuándo trasladar a un quemado?",
  "CIRUGÍA ENAM: CLASIFICACIÓN DE GRAVEDAD DE LAS QUEMADURAS", "CIRUGÍA",
  ("Gravedad de la quemadura", ["Depende de la extensión, la profundidad y la zona",
   "Quemadura mayor: se atiende en una unidad de quemados"]),
  ("Pregunta de cirugía", ["¿Qué paciente quemado requiere unidad especializada?"]),
  {"rotulo": "Clasificación de gravedad (ABA)",
   "niveles": [("Menor", "Ambulatoria", ["2.º < 15 %, 3.º < 2 %"]),
               ("Moderada", "Hospital general", ["2.º 15-25 %, 3.º 2-10 %"]),
               ("Mayor", "Unidad de quemados", ["3.º GRADO > 20 % SCT", "O 2.º > 25 %, zonas especiales"])],
   "caso_nivel": 2, "ruta_titulo": "Otros criterios de traslado", "paso_label": "PASO",
   "pasos": [(1, "Extensión o profundidad grande", ["3.er grado extenso"], True),
             (2, "Zonas especiales", ["Cara, manos, pies, periné, articulaciones"], False),
             (3, "Inhalación, eléctrica o química", ["Y pacientes con comorbilidad"], False)]},
  ["Un 3.er grado limitado a la cara anterior del muslo es moderado por extensión.",
   "El 2.º grado de antebrazo es menor.",
   "Estabilizar (ABC, líquidos) antes de trasladar."],
  "ABA – Guidelines for burn patient referral (2022) · " + ATLS)

# NEF-078 · radial
V("radial", "NEF-078", "hiperplasia-prostatica-pilar-medico-alfa-bloqueador", "Fármacos para la hiperplasia de próstata",
  "UROLOGÍA ENAM: HIPERPLASIA BENIGNA DE PRÓSTATA", "UROLOGÍA",
  ("Tratamiento médico de la HBP", ["Alfa-1 bloqueadores: relajan el cuello vesical y la próstata",
   "Alivian síntomas en días: son el pilar inicial"]),
  ("Pregunta de urología", ["¿Cuál es el pilar del tratamiento no quirúrgico?"]),
  {"rotulo": "Mapa del tema", "centro": "HBP", "centro_sub": "Tratamiento médico", "ans": 0,
   "items": [("ALFA-1 BLOQUEADORES", ["Tamsulosina, doxazosina", "Efecto rápido"]),
             ("Inhibidores de 5-alfa reductasa", ["Finasterida; próstata > 40 ml"]),
             ("Tadalafilo", ["Si coexiste disfunción eréctil"]),
             ("Antimuscarínicos", ["Si predomina la urgencia"]),
             ("Cirugía (RTU)", ["Retención, fracaso médico"])],
   "ruta": ["Síntomas urinarios", "Obstrucción dinámica", "Relajar músculo liso", "ALFA-1 BLOQUEADOR"]},
  ["Efecto adverso: hipotensión ortostática y eyaculación retrógrada.",
   "La finasterida reduce el tamaño, pero tarda 6 meses.",
   "Los betabloqueadores no tienen papel en la HBP."],
  "AUA – Guideline on management of lower urinary tract symptoms attributed to BPH (2023) · EAU (2025)")

# PED-192 · puntaje
V("puntaje", "PED-192", "lactante-ojos-hundidos-sed-pliegue-rehidratacion-oral", "Grado de deshidratación",
  "PEDIATRÍA ENAM: DESHIDRATACIÓN SIN SHOCK (PLAN B)", "PEDIATRÍA",
  ("Evaluación de la deshidratación (OMS)", ["Dos o más signos = algún grado de deshidratación",
   "Sin shock y bebiendo: rehidratación oral (Plan B)"]),
  ("Lactante de 11 meses con 24 h de diarrea", ["Seis deposiciones líquidas, un vómito, sediento", "Irritable, sin lágrimas, ojos hundidos, pliegue (+) · llenado < 2 s"]),
  {"rotulo": "Signos de deshidratación", "escala": "Signos OMS", "total": 4, "max": 6,
   "total_label": "Signos de 'algún grado'",
   "interpreta": "Deshidratación sin shock: Plan B",
   "items": [("Inquieto, irritable", "✓", True), ("Ojos hundidos", "✓", True),
             ("Bebe con avidez, sediento", "✓", True), ("Pliegue que regresa lentamente", "✓", True),
             ("Letárgico o inconsciente", "—", False), ("Bebe mal o no puede beber", "—", False)],
   "bandas": [("< 2", "Sin deshidratación", "Plan A: en casa", False),
              ("≥ 2", "Algún grado", "Plan B: SRO 75 ml/kg en 4 h", True),
              ("Shock", "Grave", "Plan C: EV", False)]},
  ["El llenado capilar < 2 s y el estar irritable (no letárgico) descartan shock.",
   "Continuar la lactancia durante la rehidratación.",
   "Zinc por 10-14 días."],
  "OMS – Tratamiento de la diarrea: manual para médicos (2005) · MINSA – GPC de enfermedad diarreica aguda en niños")

# GIN-195 · puntaje
V("puntaje", "GIN-195", "primigesta-lupus-riesgo-alto-trastorno-hipertensivo", "Riesgo de preeclampsia en el lupus",
  "OBSTETRICIA ENAM: LUPUS Y PREECLAMPSIA", "OBSTETRICIA",
  ("Lupus y trastornos hipertensivos", ["Las enfermedades autoinmunes son factor de alto riesgo de preeclampsia",
   "Con un solo factor alto se indica aspirina"]),
  ("Primigesta de 14 semanas", ["Antecedente de lupus eritematoso sistémico"]),
  {"rotulo": "Factores de riesgo del caso", "escala": "Factores", "total": 2, "max": 6,
   "total_label": "Factores presentes",
   "interpreta": "Riesgo alto de preeclampsia",
   "items": [("Lupus (autoinmune)", "Alto", True), ("Nuliparidad", "Moderado", True),
             ("HTA crónica", "Alto", False), ("Diabetes", "Alto", False),
             ("Obesidad", "Moderado", False), ("Edad ≥ 35 años", "Moderado", False)],
   "bandas": [("Ninguno", "Bajo", "Control prenatal habitual", False),
              ("≥ 2 moderados", "Moderado", "Considerar aspirina", False),
              ("≥ 1 alto", "Alto", "Aspirina desde 12-16 semanas", True)]},
  ["Los antifosfolípidos elevan todavía más el riesgo.",
   "Vigilar PA, proteinuria y crecimiento fetal.",
   "Diferenciar preeclampsia de brote de nefritis lúpica."],
  "ACOG – Committee Opinion 743 (2018) · USPSTF – Aspirin for preeclampsia prevention (2021)")

# END-058 · matriz
V("matriz", "END-058", "anciano-fracturas-suplemento-vitamina-d-colecalciferol", "Formas de vitamina D y fármacos del hueso",
  "ENDOCRINOLOGÍA ENAM: SUPLEMENTACIÓN DE VITAMINA D", "ENDOCRINOLOGÍA",
  ("Vitamina D", ["Colecalciferol (D3): forma nutricional, el cuerpo la activa según necesite",
   "Calcitriol: forma activa, reservada para falla renal o hipoparatiroidismo"]),
  ("Varón de 76 años", ["Dolores musculares y fracturas patológicas", "Se indica suplemento de vitamina D"]),
  {"rotulo": "Fármaco y uso", "eje_x": "Rasgo", "eje_y": "Fármaco",
   "cols": ["Qué es", "Cuándo"], "rows": ["Colecalciferol", "Calcitriol", "Teriparatida", "Cinacalcet"], "caso": (0, 1),
   "cells": [[("Vitamina D3 inactiva", []), ("DÉFICIT DE VITAMINA D", ["Osteoporosis, ancianos"])],
             [("1,25-OH vitamina D", ["Activa"]), ("Falla renal, hipoparatiroidismo", [])],
             [("Análogo de PTH", []), ("Osteoporosis grave", ["Anabólico"])],
             [("Calcimimético", []), ("Hiperparatiroidismo", [])]]},
  ["El calcitriol tiene más riesgo de hipercalcemia.",
   "Combinar con calcio y prevenir caídas.",
   "Medir 25-OH vitamina D para confirmar el déficit."],
  "Endocrine Society – Vitamin D for the prevention of disease guideline (2024) · AACE – Osteoporosis guideline (2020)")

# REU-057 · termómetro
V("termometro", "REU-057", "adolescente-acne-rostro-tronco-retinoide-topico", "Acné: tratamiento por gravedad",
  "DERMATOLOGÍA ENAM: ACNÉ VULGAR", "DERMATOLOGÍA",
  ("Acné vulgar", ["Obstrucción del folículo, sebo, C. acnes e inflamación",
   "Los retinoides tópicos son la base: actúan sobre el comedón"]),
  ("Adolescente de 16 años", ["Acné vulgar en rostro y tronco"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "Comedónico", ["RETINOIDE TÓPICO", "Adapaleno, tretinoína"]),
               ("Moderado", "Pápulas y pústulas", ["+ peróxido de benzoílo ± antibiótico"]),
               ("Grave", "Nódulos, quistes", ["Isotretinoína oral"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Retinoide tópico", ["Primera elección en casi todas las formas"], True),
             (2, "Peróxido de benzoílo", ["Evita resistencia bacteriana"], False),
             (3, "Antibiótico oral", ["Doxiciclina; nunca solo"], False)]},
  ["No usar antibióticos solos (tópicos ni orales): generan resistencia.",
   "La dieta tiene un papel menor.",
   "Isotretinoína: teratógena, requiere anticoncepción."],
  "AAD – Guidelines of care for the management of acne vulgaris (2024)")

# OFT-045 · tarjetas
V("tarjetas", "OFT-045", "rama-arbusto-ulcera-corneal-satelites-aspergillus", "Úlceras corneales infecciosas",
  "OFTALMOLOGÍA ENAM: QUERATITIS MICÓTICA", "OFTALMOLOGÍA",
  ("Queratitis micótica", ["Traumatismo con material vegetal introduce hongos filamentosos",
   "Úlcera grisácea, bordes plumosos y lesiones satélite"]),
  ("Varón de 30 años", ["Hace una semana se golpeó el ojo con una rama", "Úlcera corneal grisácea con lesiones satélite"]),
  {"rotulo": "¿Qué germen es?", "ans": 0, "cards": [
      {"titulo": "HONGO FILAMENTOSO", "datos": [
          ("Antecedente", "Trauma vegetal", True), ("Úlcera", "Gris, satélites", True),
          ("Germen", "Aspergillus, Fusarium", False), ("Tratamiento", "Natamicina", False)],
       "pie": "Evolución lenta"},
      {"titulo": "Bacteriana", "datos": [
          ("Antecedente", "Lentes de contacto", False), ("Úlcera", "Blanca, secreción", False),
          ("Germen", "Pseudomonas", False), ("Tratamiento", "Colirio fortificado", False)],
       "pie": "Evolución rápida"},
      {"titulo": "Herpética", "datos": [
          ("Antecedente", "Recurrente", False), ("Úlcera", "Dendrítica", False),
          ("Germen", "Herpes simple", False), ("Tratamiento", "Aciclovir", False)],
       "pie": "Sensibilidad corneal baja"},
      {"titulo": "Acanthamoeba", "datos": [
          ("Antecedente", "Lentes + agua", False), ("Úlcera", "Anillo", False),
          ("Germen", "Ameba", False), ("Tratamiento", "PHMB, clorhexidina", False)],
       "pie": "Dolor desproporcionado"}]},
  ["Nunca usar corticoides tópicos si se sospecha hongo.",
   "Raspado corneal para KOH y cultivo.",
   "Candida afecta córneas con enfermedad previa."],
  "AAO – Preferred Practice Pattern: Bacterial keratitis (2023) · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# NRL-051 · puntaje
V("puntaje", "NRL-051", "guillain-barre-disnea-sato2-89-soporte-ventilatorio", "Guillain-Barré con compromiso respiratorio",
  "NEUROLOGÍA ENAM: GUILLAIN-BARRÉ", "NEUROLOGÍA",
  ("Guillain-Barré", ["Debilidad ascendente con arreflexia tras una infección",
   "La falla respiratoria es la principal causa de muerte: vigilar y ventilar a tiempo"]),
  ("Mujer de 26 años, diarrea hace 8 días", ["3 días de debilidad ascendente, cuadriparesia, ROT bajos", "FR 28 · SatO₂ 89 % · cianosis · somnolienta"]),
  {"rotulo": "Signos de falla respiratoria", "escala": "Signos del caso", "total": 4, "max": 6,
   "total_label": "Signos presentes",
   "interpreta": "Falla respiratoria: ventilar",
   "items": [("Taquipnea (FR 28)", "✓", True), ("Hipoxemia (SatO₂ 89 %)", "✓", True),
             ("Cianosis", "✓", True), ("Somnolencia (hipercapnia)", "✓", True),
             ("CVF < 20 ml/kg", "—", False), ("Disfunción bulbar", "—", False)],
   "bandas": [("0", "Estable", "Vigilar CVF cada 4-6 h", False),
              ("≥ 1", "En riesgo", "UCI, preparar intubación", False),
              ("Falla", "Instalada", "Soporte ventilatorio", True)]},
  ["Regla 20/30/40: CVF < 20 ml/kg, PImáx > −30, PEmáx < 40 → intubar.",
   "Luego inmunoglobulina EV o plasmaféresis.",
   "La punción lumbar (disociación albúmino-citológica) no es urgente."],
  "EAN/PNS – Guideline on diagnosis and treatment of Guillain-Barré syndrome (2023)")

# NEF-079 · matriz
V("matriz", "NEF-079", "uci-shock-falla-renal-hemodialisis-continua", "¿Qué diálisis para el paciente crítico?",
  "NEFROLOGÍA ENAM: TERAPIA DE REEMPLAZO RENAL CONTINUA", "NEFROLOGÍA",
  ("Diálisis en la UCI", ["En el paciente inestable la terapia continua extrae líquido lentamente",
   "Mejor tolerancia hemodinámica que la intermitente"]),
  ("Adulto en UCI con neumonía por ventilador", ["Shock con disfunción de órganos", "Falla renal aguda"]),
  {"rotulo": "Modalidad y paciente", "eje_x": "Rasgo", "eje_y": "Modalidad",
   "cols": ["Paciente ideal", "Ventaja"], "rows": ["Continua (CRRT)", "Intermitente", "Diálisis peritoneal"], "caso": (0, 0),
   "cells": [[("SHOCK, INESTABLE", ["Con vasopresores"]), ("Menos hipotensión", ["24 h al día"])],
             [("Estable", []), ("Rápida, eficiente", [])],
             [("Niños, sin acceso vascular", []), ("Sencilla", ["Poco usada en UCI"])]]},
  ["Indicaciones urgentes: acidosis, hiperpotasemia, sobrecarga, uremia (AEIOU).",
   "La interdiaria es para pacientes crónicos estables.",
   "Ajustar la dosis de antibióticos durante la CRRT."],
  "KDIGO – Clinical practice guideline for acute kidney injury (2012)")

# SP-147 · tarjetas
V("tarjetas", "SP-147", "madre-niega-puncion-lumbar-autonomia", "Principios de la bioética",
  "SALUD PÚBLICA ENAM: AUTONOMÍA", "SALUD PÚBLICA",
  ("Autonomía", ["Derecho del paciente (o su representante) a aceptar o rechazar un procedimiento",
   "Respetar la negativa informada es respetar la autonomía"]),
  ("Niño de 12 años con cefalea, fiebre y convulsiones", ["Se indica punción lumbar", "La madre se niega a firmar el consentimiento"]),
  {"rotulo": "¿Qué principio se respeta?", "ans": 0, "cards": [
      {"titulo": "AUTONOMÍA", "datos": [
          ("Qué es", "Decidir informado", True), ("En el caso", "La madre decide", True),
          ("Límite", "Riesgo vital del niño", False)],
       "pie": "Se ejerce a través del representante"},
      {"titulo": "Beneficencia", "datos": [
          ("Qué es", "Hacer el bien", False), ("En el caso", "Indicar la punción", False),
          ("Límite", "Voluntad del paciente", False)],
       "pie": "Lo que busca el médico"},
      {"titulo": "No maleficencia", "datos": [
          ("Qué es", "No dañar", False), ("En el caso", "Evitar riesgos", False),
          ("Límite", "—", False)],
       "pie": "Primum non nocere"},
      {"titulo": "Justicia", "datos": [
          ("Qué es", "Equidad", False), ("En el caso", "No aplica", False),
          ("Límite", "Recursos", False)],
       "pie": "Reparto de recursos"}]},
  ["Explicar de nuevo riesgos y beneficios y dejar constancia de la negativa.",
   "Si hay riesgo vital inminente, el médico puede actuar (Ley General de Salud, art. 4).",
   "Considerar tratar empíricamente la meningitis sin esperar la punción."],
  "Beauchamp y Childress. Principios de ética biomédica 8.ª ed. (2019) · Ley N.° 29414")

# GIN-196 · árbol
A("GIN-196", "6-cm-cuatro-horas-dinamica-debil-oxitocina", "Fase activa que no avanza",
  "OBSTETRICIA ENAM: DETENCIÓN DE LA FASE ACTIVA", "OBSTETRICIA",
  ("Falta de progreso en fase activa", ["Si la dinámica es débil y la pelvis es adecuada: estimular con oxitocina",
   "Si la dinámica es buena y no avanza: pensar en desproporción"]),
  ("Gestante a término", ["6 cm desde hace 4 horas", "3 contracciones en 10 min de intensidad + · pelvis ginecoide · LCF 140"]),
  Q("¿Hay desproporción cefalopélvica o sufrimiento fetal?", [
      L("Sí", "Cesárea", ["Parto obstruido"]),
      Q("¿Dinámica uterina adecuada?", [
          L("No: intensidad baja", "ESTIMULAR CON OXITOCINA", ["Dosis baja y aumentar", "Monitoreo continuo"], path=True),
          L("Sí, pero no avanza", "Reevaluar, amniotomía", ["Cesárea si persiste"])],
        edge="No", path=True)], path=True),
  ("Conducción del parto", [("Oxitocina", True), ("Misoprostol", False)], [
      ("Uso", ["Estimular el trabajo de parto", "Madurar el cuello"]),
      ("En fase activa", ["Sí", "No"])]),
  ["Fase activa: se espera avanzar ≥ 1 cm/h.",
   "Observar 4 horas más sin intervenir prolonga el parto sin motivo.",
   "La intensidad de la contracción importa tanto como la frecuencia."],
  "ACOG/SMFM – Obstetric care consensus: safe prevention of the primary cesarean delivery (2014) · " + WILLIAMS)

# CAR-065 · radial
V("radial", "CAR-065", "shock-hipoperfusion-lactato-serico", "Marcadores de laboratorio",
  "CARDIOLOGÍA ENAM: LACTATO EN EL SHOCK", "CARDIOLOGÍA",
  ("Lactato sérico", ["Sin oxígeno las células pasan a metabolismo anaerobio y producen lactato",
   "Lactato ≥ 2 mmol/L indica hipoperfusión; su descenso guía la reanimación"]),
  ("Pregunta de emergencia", ["¿Qué examen valora la hipoperfusión tisular?"]),
  {"rotulo": "Mapa del tema", "centro": "LABORATORIO", "centro_sub": "¿Qué mide?", "ans": 0,
   "items": [("LACTATO", ["Hipoperfusión tisular", "≥ 4 mmol/L: shock grave"]),
             ("Procalcitonina", ["Infección bacteriana"]),
             ("Proteína C reactiva", ["Inflamación inespecífica"]),
             ("Interleucina-6", ["Inflamación, investigación"]),
             ("Troponina", ["Daño miocárdico"])],
   "ruta": ["Poco oxígeno al tejido", "Metabolismo anaerobio", "Sube el lactato", "LACTATO"]},
  ["Medir de nuevo a las 2-4 horas: debe bajar si la reanimación funciona.",
   "Shock séptico: vasopresor para PAM ≥ 65 y lactato > 2 pese a líquidos.",
   "La metformina y el hígado enfermo también elevan el lactato."],
  "Surviving Sepsis Campaign – International guidelines (2021)")

# SP-148 · fases
V("fases", "SP-148", "director-demanda-proyectada-metas-recursos-prevision", "Proceso administrativo",
  "SALUD PÚBLICA ENAM: PREVISIÓN", "SALUD PÚBLICA",
  ("Etapas del proceso administrativo", ["Previsión (planificación): analizar demanda, fijar metas y recursos",
   "Luego organización, dirección, coordinación y control"]),
  ("Director de hospital con su equipo", ["Evalúa demanda real y potencial, proyecta la oferta", "Programa metas del próximo año y asigna recursos"]),
  {"rotulo": "Etapas", "ans": 0,
   "fases": [("Previsión", "Planear", "METAS Y RECURSOS", ["Demanda proyectada"]),
             ("Organización", "Estructurar", "Quién hace qué", ["Funciones"]),
             ("Dirección", "Conducir", "Liderar", ["Motivar"]),
             ("Coordinación", "Articular", "Armonizar", ["Áreas"]),
             ("Control", "Evaluar", "Comparar con metas", ["Corregir"])],
   "curvas": [],
   "chips_titulo": "Etapa del caso · marcada la correcta",
   "chips": [("Previsión", True), ("Coordinación", False), ("Evaluación", False), ("Dirección", False)]},
  ["Fayol describió estas etapas del proceso administrativo.",
   "La previsión responde a '¿qué queremos lograr y con qué?'.",
   "Evaluar es comparar lo logrado con lo previsto."],
  "Chiavenato. Introducción a la teoría general de la administración 8.ª ed. (2014) · MINSA – Planeamiento hospitalario")

# GIN-197 · tarjetas
V("tarjetas", "GIN-197", "flujo-grisaceo-aminas-positivo-vaginosis-metronidazol", "Flujo vaginal: ¿qué tratamiento?",
  "GINECOLOGÍA ENAM: VAGINOSIS BACTERIANA", "GINECOLOGÍA",
  ("Vaginosis bacteriana", ["Cambio de flora: menos lactobacilos, más Gardnerella y anaerobios",
   "Flujo gris, homogéneo, olor a pescado (aminas +), sin inflamación"]),
  ("Mujer de 25 años con flujo persistente", ["Cuatro parejas este año · método del ritmo", "Flujo grisáceo abundante y maloliente · test de aminas (+)"]),
  {"rotulo": "¿Qué vaginitis es?", "ans": 0, "cards": [
      {"titulo": "VAGINOSIS BACTERIANA", "datos": [
          ("Flujo", "Gris, homogéneo", True), ("Aminas", "Positivo", True),
          ("pH", "> 4,5", False), ("Tratamiento", "METRONIDAZOL 7 DÍAS", True)],
       "pie": "500 mg c/12 h VO"},
      {"titulo": "Candidiasis", "datos": [
          ("Flujo", "Blanco, grumoso", False), ("Aminas", "Negativo", False),
          ("pH", "< 4,5", False), ("Tratamiento", "Fluconazol 150 mg", False)],
       "pie": "Prurito, eritema"},
      {"titulo": "Tricomoniasis", "datos": [
          ("Flujo", "Amarillo-verde espumoso", False), ("Aminas", "A veces", False),
          ("pH", "> 4,5", False), ("Tratamiento", "Metronidazol, tratar pareja", False)],
       "pie": "Cérvix en fresa"},
      {"titulo": "Vaginitis atrófica", "datos": [
          ("Flujo", "Escaso", False), ("Aminas", "Negativo", False),
          ("pH", "> 5", False), ("Tratamiento", "Estrógeno tópico", False)],
       "pie": "Posmenopausia"}]},
  ["Criterios de Amsel: flujo típico, pH > 4,5, aminas (+), células clave (3 de 4).",
   "No es necesario tratar a la pareja masculina.",
   "Evitar alcohol con metronidazol."],
  "CDC – STI treatment guidelines: bacterial vaginosis (2021)")
