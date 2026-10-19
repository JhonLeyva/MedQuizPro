"""Bloque 7 · parte L."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GUYTON = "Guyton y Hall. Tratado de fisiología médica 14.ª ed. (2021)"

# GIN-213 · árbol
A("GIN-213", "fur-42-eco-temprana-38-continuar-control-prenatal", "FUR y ecografía no coinciden",
  "OBSTETRICIA ENAM: DATACIÓN POR ECOGRAFÍA TEMPRANA", "OBSTETRICIA",
  ("Discordancia de edad gestacional", ["Si la FUR y la eco del primer trimestre difieren > 7 días, manda la ecografía",
   "No es embarazo prolongado: tiene 38 semanas"]),
  ("Gestante", ["42 semanas por FUR", "38 semanas por ecografía del primer trimestre"]),
  Q("¿Diferencia > 7 días con la eco del 1.er trimestre?", [
      L("Sí", "USAR LA ECO: 38 SEMANAS", ["Continuar el control prenatal", "Sin inducir ni operar"], path=True),
      L("No", "Mantener la FUR", ["Fecha confirmada"])], path=True),
  ("Edad gestacional del caso", [("Por eco", True), ("Por FUR", False)], [
      ("Semanas", ["38", "42"]),
      ("Conducta", ["Control prenatal", "Terminar gestación (error)"])]),
  ["Inducir o hacer cesárea por una FUR errónea causa prematuridad iatrogénica.",
   "Las pruebas de bienestar fetal no se indican solo por esta discordancia.",
   "La fecha probable de parto se fija con la eco temprana y no se cambia."],
  "ACOG – Committee Opinion 700: Methods for estimating the due date (2017)")

# SP-156 · radial
V("radial", "SP-156", "nuevo-director-presupuesto-planificacion-diagnostico", "Etapas de la planificación",
  "SALUD PÚBLICA ENAM: PLANIFICACIÓN SANITARIA", "SALUD PÚBLICA",
  ("Planificación", ["Todo plan empieza con el diagnóstico de la situación",
   "Sin conocer los problemas, el presupuesto no se asigna bien"]),
  ("Nuevo director de un ámbito sanitario", ["Podría tener 50 % más de presupuesto en 2025", "¿Qué etapa aborda primero?"]),
  {"rotulo": "Mapa del tema", "centro": "PLANIFICACIÓN", "centro_sub": "Etapas", "ans": 0,
   "items": [("DIAGNÓSTICO", ["Primer paso: ASIS", "Problemas y prioridades"]),
             ("Estrategias", ["Cómo resolverlos"]),
             ("Responsables", ["Quién lo hará"]),
             ("Ejecución presupuestal", ["Gastar lo planificado"]),
             ("Evaluación", ["Medir resultados"])],
   "ruta": ["Más presupuesto", "¿Para qué problemas?", "Conocer la situación", "DIAGNÓSTICO"]},
  ["Diagnóstico → objetivos → estrategias → ejecución → evaluación.",
   "El ASIS es la base del diagnóstico sanitario.",
   "Priorizar por magnitud, gravedad y factibilidad."],
  "MINSA – Documento técnico: Metodología para el ASIS local (2015) · CEPLAN – Guía para el planeamiento institucional (2023)")

# SP-157 · matriz
V("matriz", "SP-157", "muerte-materna-adolescentes-educacion-sexual-colegios", "Prevenir el embarazo adolescente",
  "SALUD PÚBLICA ENAM: SALUD SEXUAL EN ADOLESCENTES", "SALUD PÚBLICA",
  ("Embarazo adolescente", ["Aumenta la muerte materna en menores de 18 años",
   "Para evitar el embarazo hay que actuar antes: educación sexual en la escuela"]),
  ("Región con más muertes maternas de 13-17 años", ["¿Qué acción disminuye el embarazo adolescente?"]),
  {"rotulo": "Intervención y efecto", "eje_x": "Rasgo", "eje_y": "Intervención",
   "cols": ["Actúa sobre", "¿Reduce embarazos?"], "rows": ["Educación sexual en colegios", "Atención prenatal reenfocada", "Funciones obstétricas esenciales", "Acceso al parto"], "caso": (0, 1),
   "cells": [[("Antes del embarazo", []), ("SÍ", ["Prevención primaria"])],
             [("Gestante ya embarazada", []), ("No", ["Reduce complicaciones"])],
             [("Emergencias obstétricas", []), ("No", ["Reduce muertes"])],
             [("Parto institucional", []), ("No", [])]]},
  ["Incluir acceso a anticoncepción y servicios diferenciados para adolescentes.",
   "Las otras medidas bajan la mortalidad, pero no evitan el embarazo.",
   "Trabajar con familias, docentes y la comunidad."],
  "MINSA – Plan multisectorial para la prevención del embarazo en adolescentes 2012-2021 · UNESCO – Educación integral en sexualidad (2018)")

# PED-203 · embudo
V("embudo", "PED-203", "preescolar-tos-productiva-roncantes-bronquitis-aguda", "Tos con roncantes en el preescolar",
  "PEDIATRÍA ENAM: BRONQUITIS AGUDA", "PEDIATRÍA",
  ("Bronquitis aguda", ["Inflamación viral de los bronquios tras un resfrío",
   "Tos productiva y roncantes difusos, sin taquipnea ni crepitantes"]),
  ("Niño de 3 años", ["4 días de congestión nasal, malestar, tos productiva; luego vómitos", "T 38,2 °C · FR 24 · roncantes difusos, sin crepitantes"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Tos con fiebre en un niño de 3 años",
   "candidatos": ["Bronquitis aguda", "Neumonía viral", "Bronquiolitis", "Asma"],
   "pasos": [("FR normal, sin tirajes ni crepitantes", ["Neumonía viral"]),
             ("No es lactante y no hay sibilancias recurrentes", ["Bronquiolitis", "Asma"])],
   "final": ("BRONQUITIS AGUDA", ["Tratamiento sintomático", "Hidratación y antipirético"]),
   "nota": "Los roncantes cambian con la tos: son secreciones en bronquios grandes."},
  ["No necesita antibióticos: es viral.",
   "Los vómitos suelen ser por la tos y las flemas.",
   "Consultar si aparece taquipnea, tirajes o fiebre persistente."],
  NELSON + " · NICE NG120: Cough (acute) (2019)")

# NEF-083 · embudo
V("embudo", "NEF-083", "mujer-baja-peso-debilidad-onda-u-laxantes-hipokalemia", "Hipokalemia con ondas U",
  "NEFROLOGÍA ENAM: HIPOPOTASEMIA POR LAXANTES", "NEFROLOGÍA",
  ("Hipopotasemia", ["Debilidad, calambres, hiporreflexia; ECG con T plana y ondas U",
   "Pérdida digestiva por abuso de laxantes es una causa frecuente"]),
  ("Mujer de 29 años", ["5 días de debilidad y calambres · bajó 8 kg en 3 semanas", "PA 90/60 · mucosas secas · ROT bajos · ECG: ondas U, T aplanada"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hipopotasemia con deshidratación",
   "candidatos": ["Abuso de laxantes", "Espironolactona", "Vitamina B6", "Liotironina"],
   "pasos": [("La espironolactona sube el potasio", ["Espironolactona"]),
             ("B6 y hormona tiroidea no causan hipokalemia con deshidratación", ["Vitamina B6", "Liotironina"])],
   "final": ("ABUSO DE LAXANTES (PEG)", ["Potasio EV u oral según gravedad", "Evaluar trastorno alimentario"]),
   "nota": "Baja de peso rápida en mujer joven: pensar en conductas purgativas."},
  ["El abuso de laxantes da acidosis metabólica; el vómito, alcalosis.",
   "Reponer magnesio si está bajo.",
   "Monitoreo ECG si K < 2,5 o hay arritmias."],
  HARRISON + " · APA – Practice guideline for eating disorders (2023)")

# GIN-214 · tarjetas
V("tarjetas", "GIN-214", "gestante-20-semanas-vacuna-sarampion-contraindicada", "Vacunas en la gestante",
  "OBSTETRICIA ENAM: VACUNACIÓN EN EL EMBARAZO", "OBSTETRICIA",
  ("Vacunas en el embarazo", ["Las de virus vivos atenuados están contraindicadas",
   "Sarampión (SPR), varicela, fiebre amarilla (salvo riesgo alto)"]),
  ("Gestante de 20 semanas en control", ["¿Qué vacuna no está indicada?"]),
  {"rotulo": "¿Se puede aplicar?", "ans": 0, "cards": [
      {"titulo": "SARAMPIÓN (SPR)", "datos": [
          ("Tipo", "Virus vivo", True), ("Gestación", "CONTRAINDICADA", True),
          ("Cuándo", "Antes o después", False)],
       "pie": "Evitar embarazo 1 mes tras la vacuna"},
      {"titulo": "dTpa (pertussis)", "datos": [
          ("Tipo", "Toxoide + acelular", False), ("Gestación", "Indicada", False),
          ("Cuándo", "27-36 semanas", False)],
       "pie": "Protege al RN de tos ferina"},
      {"titulo": "Antitetánica", "datos": [
          ("Tipo", "Toxoide", False), ("Gestación", "Indicada", False),
          ("Cuándo", "Según esquema", False)],
       "pie": "Previene tétanos neonatal"},
      {"titulo": "COVID-19 e influenza", "datos": [
          ("Tipo", "ARNm o inactivada", False), ("Gestación", "Indicadas", False),
          ("Cuándo", "Cualquier trimestre", False)],
       "pie": "Reducen formas graves"}]},
  ["Vacunar SPR por error en el embarazo no indica interrumpirlo.",
   "Revisar el estado de rubéola en la consulta preconcepcional.",
   "Hepatitis B se puede aplicar si hay riesgo."],
  "MINSA – NTS 196: Esquema nacional de vacunación (2022) · CDC – Guidelines for vaccinating pregnant women (2024)")

# OFT-049 · termómetro
V("termometro", "OFT-049", "nino-lejia-ojo-queratitis-irrigacion-abundante", "Quemadura química ocular",
  "OFTALMOLOGÍA ENAM: QUEMADURA POR ÁLCALI", "OFTALMOLOGÍA",
  ("Quemadura química del ojo", ["Los álcalis (lejía) penetran rápido y son más graves que los ácidos",
   "Lo primero es irrigar sin demora"]),
  ("Niño de 12 años", ["Quemadura ocular con lejía", "Queratitis"]),
  {"rotulo": "Gravedad (Roper-Hall)",
   "niveles": [("I", "Epitelio", ["Buen pronóstico"]),
               ("II", "Córnea turbia", ["Iris visible"]),
               ("III", "Pérdida del epitelio", ["Iris poco visible"]),
               ("IV", "Córnea opaca", ["Isquemia límbica > 50 %"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Irrigación abundante", ["Suero fisiológico 30 min o más", "Hasta pH neutro (7-7,5)"], True),
             (2, "Retirar partículas", ["Evertir el párpado"], False),
             (3, "Oftalmología urgente", ["Antibiótico, ciclopléjico"], False)]},
  ["No esperar a medir el pH para empezar a irrigar.",
   "El anestésico tópico solo facilita la irrigación, no es el tratamiento.",
   "No usar parche ni neutralizar con ácidos."],
  "AAO – Chemical injury of the eye (EyeWiki 2024) · Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# GAS-067 · tarjetas
V("tarjetas", "GAS-067", "enfermera-pinchazo-vhc-arn-positivo-histologia-severidad", "Evaluación de la hepatitis C",
  "GASTROENTEROLOGÍA ENAM: HEPATITIS C", "GASTROENTEROLOGÍA",
  ("Hepatitis C", ["Anti-VHC y ARN-VHC confirman la infección",
   "La biopsia hepática (histología) mide la inflamación y la fibrosis: la gravedad"]),
  ("Enfermera de 32 años con pinchazo hace 7 meses", ["Malestar, náuseas, ictericia", "TGP 3360 · bilirrubina 7 · anti-VHC y ARN-VHC (+)"]),
  {"rotulo": "¿Qué informa cada estudio?", "ans": 0, "cards": [
      {"titulo": "ESTUDIO HISTOLÓGICO", "datos": [
          ("Mide", "Inflamación y fibrosis", True), ("Escala", "METAVIR", True),
          ("Papel", "Gravedad", True)],
       "pie": "Hoy se prefiere elastografía"},
      {"titulo": "Genotipo", "datos": [
          ("Mide", "Tipo de virus", False), ("Escala", "1 a 6", False),
          ("Papel", "Elegir tratamiento", False)],
       "pie": "No mide gravedad"},
      {"titulo": "Ecografía", "datos": [
          ("Mide", "Tamaño, forma", False), ("Escala", "—", False),
          ("Papel", "Cirrosis avanzada", False)],
       "pie": "Tamizaje de hepatocarcinoma"},
      {"titulo": "TC / RM", "datos": [
          ("Mide", "Lesiones focales", False), ("Escala", "—", False),
          ("Papel", "Masas", False)],
       "pie": "No gradúa fibrosis"}]},
  ["Tratamiento: antivirales de acción directa, curan > 95 %.",
   "Tras un pinchazo: seguimiento con ARN-VHC y transaminasas.",
   "Elastografía (FibroScan): alternativa no invasiva."],
  "AASLD/IDSA – HCV guidance (2023) · EASL – Recommendations on treatment of hepatitis C (2020)")

# PED-204 · árbol
A("PED-204", "neonato-abdomen-excavado-empeora-con-ambu-intubar", "Recién nacido que empeora con la ventilación",
  "PEDIATRÍA ENAM: HERNIA DIAFRAGMÁTICA CONGÉNITA", "PEDIATRÍA",
  ("Hernia diafragmática congénita", ["Las vísceras pasan al tórax y comprimen el pulmón",
   "Abdomen excavado + dificultad respiratoria; la bolsa-máscara infla el intestino y empeora"]),
  ("Neonato a término en sala de partos", ["Abdomen excavado", "Se deteriora pese a la ventilación a presión positiva"]),
  Q("¿Abdomen excavado con dificultad respiratoria?", [
      L("Sí", "INTUBACIÓN ENDOTRAQUEAL", ["No usar bolsa-máscara", "Sonda orogástrica para descomprimir"], path=True),
      L("No", "Reanimación habitual", ["Algoritmo neonatal"])], path=True),
  ("Hernia diafragmática", [("Dato", True), ("Detalle", False)], [
      ("Lado", ["Izquierdo (Bochdalek)", "85 %"]),
      ("Signos", ["Ruidos cardiacos a la derecha", "Ruidos intestinales en tórax"]),
      ("Problema", ["Hipoplasia pulmonar", "Hipertensión pulmonar"])]),
  ["La cirugía se hace tras estabilizar, no de emergencia.",
   "Diagnóstico prenatal por ecografía en la mayoría.",
   "Evitar presiones altas: riesgo de neumotórax."],
  "AHA/AAP – Neonatal resuscitation guidelines (2025) · CDH EURO Consortium (2015)")

# SP-158 · radial
V("radial", "SP-158", "personal-nuevo-hospital-capacitacion-control-infeccion-tb", "Salud ocupacional del personal nuevo",
  "SALUD PÚBLICA ENAM: CONTROL DE INFECCIONES POR TUBERCULOSIS", "SALUD PÚBLICA",
  ("Control de infecciones de TB", ["El personal de salud tiene más riesgo de infectarse",
   "Lo primero con quien ingresa: capacitarlo en medidas de control"]),
  ("Profesionales recién incorporados a un hospital", ["Programa de salud ocupacional", "¿Qué actividad es prioritaria?"]),
  {"rotulo": "Mapa del tema", "centro": "PERSONAL NUEVO", "centro_sub": "Prioridades", "ans": 0,
   "items": [("CAPACITACIÓN EN CONTROL", ["Administrativo, ambiental y respiradores", "Protege desde el primer día"]),
             ("Tamizaje basal", ["Síntomas, PPD o IGRA"]),
             ("Terapia preventiva", ["Solo si hay TB latente"]),
             ("Prueba molecular", ["En pacientes sintomáticos"]),
             ("Reacciones adversas", ["Tema de pacientes en tratamiento"])],
   "ruta": ["Ingresa al hospital", "Riesgo de exposición", "Conocer las medidas", "CAPACITACIÓN"]},
  ["Tres niveles de control: administrativo, ambiental y protección respiratoria.",
   "El respirador N95 para el personal; la mascarilla para el paciente.",
   "La TB en personal de salud es enfermedad ocupacional."],
  "MINSA – NTS 200 (2023) · OMS – Guidelines on tuberculosis infection prevention and control (2019)")

# GIN-215 · árbol
A("GIN-215", "gestante-pielonefritis-previa-urocultivo-negativo-mensual", "Tras una pielonefritis en el embarazo",
  "OBSTETRICIA ENAM: SEGUIMIENTO DE LA PIELONEFRITIS", "OBSTETRICIA",
  ("Pielonefritis en la gestación", ["Recurre en un 20 % si no se vigila",
   "Tras tratarla: urocultivo mensual hasta el parto"]),
  ("Gestante de 24 semanas", ["Hospitalizada por pielonefritis hace 15 días", "Urocultivo actual negativo"]),
  Q("¿Urocultivo de control positivo?", [
      L("Sí", "Tratar y profilaxis", ["Nitrofurantoína nocturna"]),
      L("No", "UROCULTIVO MENSUAL", ["Hasta el final del embarazo"], path=True)], path=True),
  ("Opciones de seguimiento", [("Urocultivo mensual", True), ("Profilaxis", False)], [
      ("Cuándo", ["Tras cualquier pielonefritis", "Si recurre la bacteriuria"]),
      ("Fármaco", ["—", "Nitrofurantoína o cefalexina"])]),
  ["Las quinolonas están contraindicadas en el embarazo.",
   "Los acidificantes urinarios no previenen la recurrencia.",
   "La bacteriuria asintomática también se trata en la gestante."],
  "ACOG – Clinical consensus: urinary tract infections in pregnant individuals (2023) · " + WILLIAMS)

# PED-205 · matriz
V("matriz", "PED-205", "prematuro-membrana-hialina-hipovolemia-inhibe-surfactante", "Qué favorece y qué frena el surfactante",
  "PEDIATRÍA ENAM: SURFACTANTE PULMONAR", "PEDIATRÍA",
  ("Surfactante", ["Producido por neumocitos tipo II; reduce la tensión superficial",
   "La hipovolemia, la hipoxia, la acidosis y el frío frenan su síntesis"]),
  ("RN de 28 semanas con membrana hialina", ["¿Qué situación inhibe la síntesis de surfactante?"]),
  {"rotulo": "Efecto sobre el surfactante", "eje_x": "Efecto", "eje_y": "Factor",
   "cols": ["Lo frena", "Lo favorece"], "rows": ["Circulación", "Hormonas", "Ambiente"], "caso": (0, 0),
   "cells": [[("HIPOVOLEMIA", ["Hipoperfusión, acidosis"]), ("Buena perfusión", [])],
             [("Hiperinsulinismo", ["Madre diabética"]), ("Corticoides prenatales", ["Hormona tiroidea"])],
             [("Hipotermia", ["Frío"]), ("Estrés fetal crónico", ["RPM prolongada"])]]},
  ["El calor ambiental adecuado protege; el frío empeora la enfermedad.",
   "Los corticoides prenatales (24-34 semanas) aceleran la maduración pulmonar.",
   "Surfactante exógeno por tubo endotraqueal en la membrana hialina."],
  NELSON + " · European Consensus Guidelines on RDS (2022)")

# CIR-112 · termómetro
V("termometro", "CIR-112", "trauma-toracico-fracturas-costales-radiopacidad-hemotorax-drenaje", "Hemotórax traumático",
  "CIRUGÍA ENAM: HEMOTÓRAX", "CIRUGÍA",
  ("Hemotórax", ["Sangre en la pleura: matidez y murmullo abolido",
   "Tratamiento inicial: tubo de drenaje pleural; toracotomía si el sangrado es masivo"]),
  ("Mujer de 25 años tras accidente", ["PA 90/60 · FC 112 · SatO₂ 90 % · pálida, sudorosa", "Crepitación costal 5.º-6.º derechos · MV abolido · 2/3 inferiores radiopacos"]),
  {"rotulo": "Volumen del hemotórax",
   "niveles": [("Pequeño", "< 300 ml", ["Observar"]),
               ("Moderado", "Opacidad amplia", ["2/3 DEL HEMITÓRAX", "Tubo de drenaje"]),
               ("Masivo", "> 1500 ml o > 200 ml/h", ["Toracotomía"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Drenaje pleural", ["Tubo 28-32 Fr en 5.º espacio, línea axilar media"], True),
             (2, "Medir el débito", ["Inicial y por hora"], False),
             (3, "Toracotomía si es masivo", ["O sangrado persistente"], False)]},
  ["Reponer volumen y preparar sangre.",
   "La pericardiocentesis es para taponamiento, no para hemotórax.",
   "Hemotórax retenido: videotoracoscopía."],
  ATLS)

# GIN-216 · tarjetas
V("tarjetas", "GIN-216", "vih-escenario-3-cesarea-suprimir-lactancia-cabergolina", "Lactancia en la madre con VIH",
  "OBSTETRICIA ENAM: SUPRESIÓN DE LA LACTANCIA EN VIH", "OBSTETRICIA",
  ("Transmisión del VIH por la leche", ["En el Perú se contraindica la lactancia materna en madres con VIH",
   "Se suprime con cabergolina y vendaje de mamas tras el parto"]),
  ("Puérpera inmediata por cesárea", ["VIH diagnosticado en esta gestación, escenario 3", "¿Qué hacer con la lactancia?"]),
  {"rotulo": "¿Qué conducta es la correcta?", "ans": 0, "cards": [
      {"titulo": "CABERGOLINA + VENDAJE", "datos": [
          ("Cuándo", "Tras el parto", True), ("Efecto", "Inhibe prolactina", True),
          ("RN", "Fórmula láctea", False)],
       "pie": "Cabergolina 1 mg dosis única"},
      {"titulo": "Lactancia materna", "datos": [
          ("Cuándo", "—", False), ("Efecto", "Transmite el VIH", False),
          ("RN", "Riesgo de infección", False)],
       "pie": "Contraindicada en el Perú"},
      {"titulo": "Medroxiprogesterona", "datos": [
          ("Cuándo", "72 h", False), ("Efecto", "Anticonceptivo", False),
          ("RN", "No suprime la leche", False)],
       "pie": "No es el método"},
      {"titulo": "Mifepristona", "datos": [
          ("Cuándo", "48 h", False), ("Efecto", "Antiprogestágeno", False),
          ("RN", "No indicado", False)],
       "pie": "Sin papel aquí"}]},
  ["El RN recibe profilaxis antirretroviral y fórmula gratuita.",
   "La madre continúa TAR de por vida.",
   "Escenario 3: diagnóstico en el trabajo de parto o sin control previo."],
  "MINSA – NTS 159: Prevención de la transmisión materno infantil del VIH, sífilis y hepatitis B (2019)")

# NEU-063 · embudo
V("embudo", "NEU-063", "fiebre-tos-disnea-crepitantes-opacidad-neumonia", "Fiebre con opacidad pulmonar",
  "NEUMOLOGÍA ENAM: NEUMONÍA ADQUIRIDA EN LA COMUNIDAD", "NEUMOLOGÍA",
  ("Neumonía", ["Fiebre + tos + disnea + crepitantes + opacidad nueva en la Rx",
   "Infección aguda del parénquima pulmonar"]),
  ("Mujer de 45 años con 6 días de síntomas", ["Fiebre, tos, dificultad respiratoria · FR 28", "Crepitantes en hemitórax izquierdo · opacidad en la Rx"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Fiebre, tos y opacidad en la Rx",
   "candidatos": ["Neumonía", "Empiema", "Tuberculosis", "Atelectasia"],
   "pasos": [("Crepitantes (no matidez con MV abolido)", ["Empiema", "Atelectasia"]),
             ("Cuadro agudo de 6 días", ["Tuberculosis"])],
   "final": ("NEUMONÍA", ["Evaluar gravedad con CURB-65", "Antibiótico según lugar de manejo"]),
   "nota": "La atelectasia no da fiebre por sí sola y desplaza estructuras hacia el lado afectado."},
  ["Germen más frecuente: neumococo.",
   "Si hay derrame, puncionarlo para descartar empiema.",
   "TB: tos > 2-3 semanas, baja de peso, sudoración nocturna."],
  "ATS/IDSA – Community-acquired pneumonia guideline (2019)")

# PED-206 · fases
V("fases", "PED-206", "lactante-7-meses-deshidratacion-grave-plan-c-30-70", "Plan C en el menor de 12 meses",
  "PEDIATRÍA ENAM: DESHIDRATACIÓN GRAVE (PLAN C)", "PEDIATRÍA",
  ("Plan C de rehidratación", ["Deshidratación grave: 100 ml/kg EV de Ringer lactato",
   "Menor de 12 meses: 30 ml/kg en 1 h y 70 ml/kg en 5 h"]),
  ("Lactante de 7 meses con 2 días de diarrea y vómitos", ["Letárgico, succión pobre", "Ojos muy hundidos, pliegue que regresa muy lento"]),
  {"rotulo": "Rehidratación EV según la edad", "ans": 1,
   "fases": [("Shock", "Si existe", "Bolos 20 ml/kg", ["Tratar primero"]),
             ("1.ª fase", "< 12 m: 1 h", "RINGER 30 ML/KG", ["≥ 12 m: en 30 min"]),
             ("2.ª fase", "< 12 m: 5 h", "RINGER 70 ML/KG", ["≥ 12 m: en 2,5 h"]),
             ("Reevaluar", "Cada 1-2 h", "Pasar a plan B o A", ["SRO en cuanto beba"])],
   "curvas": [("Hidratación", SKY, [0.1, 0.35, 0.55, 0.7, 0.85, 0.9, 0.95])],
   "chips_titulo": "Indicación · marcada la correcta",
   "chips": [("Ringer 30 ml/kg en 1 h y 70 ml/kg en 5 h", True), ("Ringer 30 en 0,5 h y 70 en 2,5 h", False), ("NaCl 70 en 1 h y 30 en 3 h", False)]},
  ["El esquema rápido (30 min + 2,5 h) es para ≥ 12 meses.",
   "Si no hay vía EV: sonda nasogástrica o intraósea.",
   "Iniciar SRO (5 ml/kg/h) cuando pueda beber."],
  "OMS – Tratamiento de la diarrea (2005) · MINSA – GPC de enfermedad diarreica aguda en niños")

# GIN-217 · puntaje
V("puntaje", "GIN-217", "saco-29-mm-embrion-8-mm-sin-latido-misoprostol", "Pérdida gestacional temprana",
  "OBSTETRICIA ENAM: ABORTO RETENIDO", "OBSTETRICIA",
  ("Diagnóstico ecográfico de pérdida", ["Embrión ≥ 7 mm sin latido o saco medio ≥ 25 mm sin embrión",
   "Con un criterio ya se confirma: no hace falta repetir la ecografía"]),
  ("Gestante de 35 años con 7 semanas de amenorrea", ["Dolor pélvico, sangrado escaso, cuello cerrado", "Saco medio 29 mm · embrión de 8 mm sin latido"]),
  {"rotulo": "Criterios de pérdida gestacional", "escala": "Criterios ecográficos", "total": 1, "max": 2,
   "total_label": "Criterios cumplidos",
   "interpreta": "Pérdida confirmada: evacuar",
   "items": [("Embrión ≥ 7 mm sin latido", "✓", True), ("Saco medio ≥ 25 mm sin embrión", "—", False)],
   "bandas": [("0", "Dudoso", "Repetir ecografía en 7-10 días", False),
              ("≥ 1", "Confirmado", "Misoprostol, AMEU o expectante", True)]},
  ["Misoprostol 800 µg vaginal (con o sin mifepristona previa).",
   "AMEU si hay sangrado abundante, infección o preferencia.",
   "Anti-D si la madre es Rh negativo."],
  "SRU – Consensus: diagnostic criteria for nonviable pregnancy (NEJM 2013) · ACOG – Practice Bulletin 200 (2018)")

# CIR-113 · puntaje
V("puntaje", "CIR-113", "murphy-positivo-calculo-bacinete-colecistectomia-laparoscopica", "Colecistitis aguda en la joven",
  "CIRUGÍA ENAM: COLECISTITIS AGUDA", "CIRUGÍA",
  ("Colecistitis aguda litiásica", ["Criterios de Tokio: signo local + signo sistémico + imagen",
   "Grado I en paciente joven: colecistectomía laparoscópica temprana"]),
  ("Mujer de 25 años con manga gástrica previa", ["48 h de dolor tras comer, náuseas, vómitos", "Murphy (+) · pared gruesa, cálculo en bacinete · leucocitos 12 000"]),
  {"rotulo": "Criterios de Tokio 2018", "escala": "Tokio (A + B + C)", "total": 3, "max": 3,
   "total_label": "Grupos cumplidos",
   "interpreta": "Colecistitis aguda confirmada",
   "items": [("A. Local: Murphy o dolor en HCD", "✓", True), ("B. Sistémico: leucocitos > 10 000", "✓", True),
             ("C. Imagen: pared gruesa, cálculo enclavado", "✓", True)],
   "bandas": [("A + B", "Sospecha", "Imagen para confirmar", False),
              ("A + B + C", "Definitiva", "Colecistectomía laparoscópica temprana", True)]},
  ["Ideal dentro de las 72 horas (hasta 7-10 días).",
   "La colecistostomía es para pacientes de alto riesgo.",
   "La pérdida rápida de peso tras cirugía bariátrica favorece los cálculos."],
  "Tokyo Guidelines 2018 (J Hepatobiliary Pancreat Sci) · WSES – Acute calculous cholecystitis (2020)")

# TRA-046 · tarjetas
V("tarjetas", "TRA-046", "caida-mano-extendida-signo-charretera-luxacion-hombro", "Deformidad del hombro tras una caída",
  "TRAUMATOLOGÍA ENAM: LUXACIÓN ANTERIOR DE HOMBRO", "TRAUMATOLOGÍA",
  ("Luxación anterior del hombro", ["La más frecuente de las luxaciones grandes",
   "Signo de la charretera: el acromion resalta porque la cabeza humeral salió hacia adelante"]),
  ("Varón de 20 años que cae sobre la mano extendida", ["Dolor e impotencia funcional del hombro", "Relieve angulado bajo la piel (charretera)"]),
  {"rotulo": "¿Qué lesión y qué tratamiento?", "ans": 0, "cards": [
      {"titulo": "LUXACIÓN ANTERIOR", "datos": [
          ("Signo", "Charretera", True), ("Mecanismo", "Abducción + rotación externa", False),
          ("Tratamiento", "Reducción por tracción", True), ("Revisar", "Nervio axilar", False)],
       "pie": "Luego inmovilizar 2-3 semanas"},
      {"titulo": "Luxación posterior", "datos": [
          ("Signo", "Brazo en rotación interna", False), ("Mecanismo", "Convulsión, electrocución", False),
          ("Tratamiento", "Reducción", False), ("Revisar", "Rx axilar", False)],
       "pie": "Se pasa por alto"},
      {"titulo": "Fractura de clavícula", "datos": [
          ("Signo", "Deformidad en la clavícula", False), ("Mecanismo", "Caída sobre el hombro", False),
          ("Tratamiento", "Cabestrillo o vendaje en 8", False), ("Revisar", "Piel, vasos", False)],
       "pie": "Tercio medio"},
      {"titulo": "Fractura del húmero proximal", "datos": [
          ("Signo", "Equimosis braquial", False), ("Mecanismo", "Anciano con osteoporosis", False),
          ("Tratamiento", "Cabestrillo o placas", False), ("Revisar", "Nervio axilar", False)],
       "pie": "Anciana"}]},
  ["Rx antes y después de reducir para descartar fractura.",
   "Técnicas: tracción-contratracción, rotación externa, Milch.",
   "En jóvenes la recidiva es frecuente."],
  "AAOS – Shoulder dislocation (OrthoInfo 2023) · Rockwood and Green's Fractures in Adults 10.ª ed. (2024)")

# CAR-067 · matriz
V("matriz", "CAR-067", "rcp-calidad-5-cm-100-120-por-minuto", "Compresiones de calidad",
  "CARDIOLOGÍA ENAM: RCP DE ALTA CALIDAD", "CARDIOLOGÍA",
  ("RCP de alta calidad", ["Profundidad de 5-6 cm y frecuencia de 100-120 por minuto en el adulto",
   "Dejar que el tórax se reexpanda y minimizar las pausas"]),
  ("Varón de 50 años en trauma shock", ["Deja de respirar, no responde, sin pulso", "Se inicia RCP"]),
  {"rotulo": "Parámetros por edad", "eje_x": "Edad", "eje_y": "Parámetro",
   "cols": ["Adulto", "Niño"], "rows": ["Profundidad", "Frecuencia", "Relación sin vía avanzada"], "caso": (0, 0),
   "cells": [[("5-6 CM", ["No más de 6"]), ("~5 cm", ["1/3 del tórax"])],
             [("100-120 POR MINUTO", []), ("100-120 por minuto", [])],
             [("30:2", []), ("30:2 (15:2 con 2 rescatadores)", [])]]},
  ["Cambiar de compresor cada 2 minutos para evitar la fatiga.",
   "Pausas de menos de 10 segundos.",
   "Evitar hiperventilar."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2025)")

# GIN-218 · fases
V("fases", "GIN-218", "dilatacion-completa-occipitoanterior-siguiente-extension", "Movimientos cardinales del parto",
  "OBSTETRICIA ENAM: MECANISMO DEL PARTO", "OBSTETRICIA",
  ("Mecanismo del parto (occipitoanterior)", ["Encajamiento, descenso, flexión, rotación interna, extensión, rotación externa, expulsión",
   "Con el occipucio ya en anterior y en +3, sigue la extensión"]),
  ("Primigesta de 39 semanas", ["Dilatación completa, 100 %, +3", "Occipitoanterior, membranas rotas"]),
  {"rotulo": "Secuencia", "ans": 2,
   "fases": [("Descenso", "Con flexión", "Encaja y baja", ["Mentón al tórax"]),
             ("Rot. interna", "Ya ocurrió", "Occipucio adelante", ["Occipitoanterior"]),
             ("Extensión", "Siguiente", "EXTENSIÓN", ["La cabeza sale bajo el pubis"]),
             ("Rot. externa", "Restitución", "Hombros rotan", ["Cabeza gira"]),
             ("Expulsión", "Final", "Hombros y cuerpo", [])],
   "curvas": [],
   "chips_titulo": "Siguiente movimiento · marcado el correcto",
   "chips": [("Extensión", True), ("Rotación interna", False), ("Rotación externa", False), ("Restitución", False)]},
  ["La rotación externa y la restitución ocurren después de salir la cabeza.",
   "Proteger el periné durante la extensión.",
   "Las variedades posteriores tardan más en rotar."],
  WILLIAMS)

# NRL-053 · puntaje
V("puntaje", "NRL-053", "caida-4-piso-abre-ojos-dolor-flexion-sonidos-glasgow-7", "Escala de coma de Glasgow",
  "NEUROLOGÍA ENAM: ESCALA DE GLASGOW", "NEUROLOGÍA",
  ("Escala de Glasgow", ["Suma apertura ocular (1-4), verbal (1-5) y motora (1-6)",
   "≤ 8 = TEC grave: asegurar la vía aérea"]),
  ("Varón de 33 años que cayó de un 4.º piso", ["Abre los ojos al dolor", "Postura en flexión · sonidos incomprensibles"]),
  {"rotulo": "Glasgow en el caso", "escala": "Glasgow", "total": 7, "max": 15,
   "total_label": "Puntaje del caso",
   "interpreta": "TEC grave: intubar",
   "items": [("Ocular: abre al dolor", "2", True), ("Verbal: sonidos incomprensibles", "2", True),
             ("Motor: flexión anormal (decorticación)", "3", True)],
   "bandas": [("13-15", "Leve", "Observación, TC según riesgo", False),
              ("9-12", "Moderado", "TC y vigilancia", False),
              ("3-8", "Grave", "Intubación y neurocirugía", True)]},
  ["Retirada al dolor = 4; flexión anormal = 3; extensión = 2.",
   "Registrar el mejor puntaje motor.",
   "Evitar hipotensión e hipoxia: empeoran el daño cerebral."],
  "Teasdale G, Jennett B (Lancet 1974; actualización 2014) · " + ATLS)

# SP-159 · tarjetas
V("tarjetas", "SP-159", "cesarea-medico-no-especialista-perfora-vejiga-impericia", "Tipos de mala praxis",
  "SALUD PÚBLICA ENAM: IMPERICIA", "SALUD PÚBLICA",
  ("Mala praxis", ["Impericia: hacer algo sin la preparación o destreza necesaria",
   "Un no especialista que opera y perfora la vejiga"]),
  ("Cesárea electiva por un médico no especialista", ["Se perfora la vejiga durante la cirugía"]),
  {"rotulo": "¿Qué tipo de falta es?", "ans": 0, "cards": [
      {"titulo": "IMPERICIA", "datos": [
          ("Qué es", "Falta de saber o destreza", True), ("En el caso", "No especialista opera", True),
          ("Ejemplo", "Lesión por técnica", False)],
       "pie": "Saber hacer"},
      {"titulo": "Imprudencia", "datos": [
          ("Qué es", "Actuar con temeridad", False), ("En el caso", "—", False),
          ("Ejemplo", "Operar sin exámenes", False)],
       "pie": "Hacer de más"},
      {"titulo": "Negligencia", "datos": [
          ("Qué es", "Omitir el deber", False), ("En el caso", "—", False),
          ("Ejemplo", "No vigilar al paciente", False)],
       "pie": "Hacer de menos"},
      {"titulo": "Inobservancia", "datos": [
          ("Qué es", "No cumplir normas", False), ("En el caso", "—", False),
          ("Ejemplo", "Omitir protocolos", False)],
       "pie": "Reglamentos"}]},
  ["Las cuatro pueden generar responsabilidad civil y penal.",
   "Actuar dentro de la propia competencia protege al paciente y al médico.",
   "Informar y registrar toda complicación."],
  "Código Penal peruano (art. 111 y 124) · Colegio Médico del Perú – Código de ética y deontología")

# CB-076 · fases
V("fases", "CB-076", "maratonista-ejercicio-prolongado-gluconeogenesis-hepatica", "Energía durante el ejercicio prolongado",
  "CIENCIAS BÁSICAS ENAM: GLUCONEOGÉNESIS", "CIENCIAS BÁSICAS",
  ("Metabolismo en el ejercicio", ["Primero se usa el glucógeno; cuando se agota, el hígado fabrica glucosa",
   "Gluconeogénesis a partir de lactato, glicerol y alanina"]),
  ("Maratonista", ["Ejercicio aeróbico prolongado", "¿Qué pasa en el hígado?"]),
  {"rotulo": "Fuente de glucosa según el tiempo", "ans": 2,
   "fases": [("Minutos", "Inicio", "Glucógeno muscular", ["Energía inmediata"]),
             ("< 90 min", "Temprano", "Glucogenólisis hepática", ["Glucagón, adrenalina"]),
             ("> 90 min", "Prolongado", "GLUCONEOGÉNESIS", ["Lactato, glicerol, alanina"]),
             ("Horas", "Final", "Lipólisis y cetonas", ["Grasa como combustible"])],
   "curvas": [("Glucógeno", SKY, [1.0, 0.85, 0.6, 0.35, 0.15, 0.1, 0.05]),
              ("Glucosa nueva", ROSE, [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95])],
   "chips_titulo": "Cambio en el hígado · marcado el correcto",
   "chips": [("Activa la gluconeogénesis", True), ("Activa la glucogenosíntesis", False), ("Reduce la glucogenólisis", False)]},
  ["Hormonas: glucagón, cortisol y catecolaminas suben; la insulina baja.",
   "El ciclo de Cori recicla el lactato muscular en el hígado.",
   "La glucogenosíntesis ocurre en reposo tras comer."],
  GUYTON + " · Harper. Bioquímica ilustrada 32.ª ed. (2023)")

# TRA-047 · fases
V("fases", "TRA-047", "hemorragia-activa-primer-signo-taquicardia", "Qué hace el cuerpo ante la hemorragia",
  "TRAUMATOLOGÍA ENAM: COMPENSACIÓN DE LA HEMORRAGIA", "TRAUMATOLOGÍA",
  ("Compensación de la hemorragia", ["El simpático reacciona primero: sube la frecuencia cardiaca",
   "Luego vasoconstricción, presión de pulso estrecha, menos diuresis e hipotensión"]),
  ("Varón de 33 años tras accidente de tránsito", ["Despierto, confuso · laceraciones y hematomas", "Sangrado de miembros inferiores que no cede a la presión"]),
  {"rotulo": "Orden de los signos", "ans": 0,
   "fases": [("1.º", "Inmediato", "TAQUICARDIA", ["Descarga simpática"]),
             ("2.º", "Vasoconstricción", "Presión de pulso estrecha", ["Llenado capilar lento"]),
             ("3.º", "Riñón", "Diuresis baja", ["Menos perfusión"]),
             ("4.º", "Tardío", "Hipotensión", ["Pérdida > 30 %"])],
   "curvas": [("FC", ROSE, [0.3, 0.55, 0.7, 0.8, 0.9, 0.95, 0.95]),
              ("PA", SKY, [0.8, 0.8, 0.75, 0.7, 0.5, 0.3, 0.2])],
   "chips_titulo": "Primer signo · marcado el correcto",
   "chips": [("Aumento de la frecuencia cardiaca", True), ("Aumento de la presión de pulso", False), ("Llenado capilar lento", False), ("Menos diuresis", False)]},
  ["La presión de pulso se estrecha, no se amplía.",
   "La hipotensión aparece tarde: no esperarla para tratar.",
   "Controlar el sangrado con torniquete si la presión directa falla."],
  ATLS)

# PED-207 · radial
V("radial", "PED-207", "lactante-2-meses-vih-iniciar-tar-precoz", "Lactante con VIH",
  "PEDIATRÍA ENAM: TRATAMIENTO ANTIRRETROVIRAL EN EL LACTANTE", "PEDIATRÍA",
  ("VIH en el lactante", ["Progresa muy rápido: alta mortalidad en el primer año sin tratamiento",
   "Todo niño con VIH inicia TAR de inmediato, sin esperar CD4 ni síntomas"]),
  ("Lactante de 2 meses", ["Diagnóstico reciente de VIH", "Derivación a infectología pediátrica"]),
  {"rotulo": "Mapa del tema", "centro": "LACTANTE CON VIH", "centro_sub": "¿Cuándo tratar?", "ans": 0,
   "items": [("TAR PRECOZ", ["Apenas se confirma", "Reduce la mortalidad"]),
             ("Esperar CD4", ["Retrasa sin beneficio"]),
             ("Solo si hay síntomas", ["Riesgo de muerte"]),
             ("Al año de edad", ["Demasiado tarde"]),
             ("Profilaxis con cotrimoxazol", ["Se suma al TAR"])],
   "ruta": ["VIH confirmado", "2 meses de edad", "Alto riesgo de progresión", "TAR YA"]},
  ["El diagnóstico en < 18 meses se hace con PCR (no con anticuerpos).",
   "Vacunas: evitar BCG si ya tiene VIH sintomático.",
   "Seguimiento del crecimiento y desarrollo."],
  "OMS – Consolidated guidelines on HIV prevention, testing, treatment (2021) · MINSA – NTS de atención integral del niño con VIH")

# GAS-068 · embudo
V("embudo", "GAS-068", "ascitis-fiebre-nodulos-mijo-granulomas-caseosos-tb-peritoneal", "Ascitis con nódulos peritoneales",
  "GASTROENTEROLOGÍA ENAM: TUBERCULOSIS PERITONEAL", "GASTROENTEROLOGÍA",
  ("Tuberculosis peritoneal", ["Fiebre prolongada, ascitis, dolor abdominal",
   "Laparoscopía: nódulos en 'granos de mijo'; biopsia con granulomas caseosos"]),
  ("Mujer de 26 años con 6 meses de fiebre", ["Diarrea, dolor en fosa ilíaca derecha, ascitis", "Nódulos < 5 mm · granulomas caseosos con células de Langhans"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Ascitis con nódulos peritoneales",
   "candidatos": ["TB peritoneal", "Linfomatosis peritoneal", "Carcinomatosis", "Actinomicosis"],
   "pasos": [("Granulomas con necrosis caseosa", ["Linfomatosis peritoneal", "Carcinomatosis"]),
             ("Sin gránulos de azufre ni fístulas", ["Actinomicosis"])],
   "final": ("TUBERCULOSIS PERITONEAL", ["Esquema antituberculoso", "ADA alto en líquido ascítico"]),
   "nota": "El ADA en líquido ascítico > 39 U/L apoya el diagnóstico sin biopsia."},
  ["Líquido ascítico: exudado linfocitario.",
   "La baciloscopía del líquido casi siempre es negativa.",
   "Puede asociarse a TB intestinal ileocecal."],
  "MINSA – NTS 200 (2023) · " + HARRISON)

# CB-077 · radial
V("radial", "CB-077", "fisicoculturista-debilidad-pronacion-nervio-mediano", "Nervios del antebrazo",
  "CIENCIAS BÁSICAS ENAM: NERVIO MEDIANO", "CIENCIAS BÁSICAS",
  ("Nervio mediano", ["Inerva los pronadores (redondo y cuadrado) y los flexores del antebrazo",
   "Su compresión en el pronador redondo da dolor y debilidad para pronar"]),
  ("Fisicoculturista de 30 años", ["Dolor en el antebrazo y debilidad a la pronación", "Prueba de pronación (+)"]),
  {"rotulo": "Mapa del tema", "centro": "ANTEBRAZO", "centro_sub": "¿Qué nervio?", "ans": 0,
   "items": [("MEDIANO", ["Pronación, flexión de dedos", "Oposición del pulgar"]),
             ("Radial", ["Extensión de muñeca y dedos"]),
             ("Cubital", ["Músculos intrínsecos de la mano"]),
             ("Musculocutáneo", ["Flexión del codo, supinación"]),
             ("Axilar", ["Abducción del hombro"])],
   "ruta": ["Hipertrofia muscular", "Compresión en el antebrazo", "Pronación débil", "NERVIO MEDIANO"]},
  ["Síndrome del pronador: parestesias en la palma sin Tinel en la muñeca.",
   "Lesión alta del mediano: mano de predicador.",
   "Túnel carpiano: compresión distal del mismo nervio."],
  "Moore. Anatomía con orientación clínica 9.ª ed. (2022)")

# NEU-064 · puntaje
V("puntaje", "NEU-064", "infiltrados-bilaterales-sato2-78-sdra-shunt", "Hipoxemia grave con infiltrados bilaterales",
  "NEUMOLOGÍA ENAM: SÍNDROME DE DISTRÉS RESPIRATORIO AGUDO", "NEUMOLOGÍA",
  ("SDRA", ["Alvéolos llenos de líquido inflamatorio: perfundidos pero no ventilados",
   "El mecanismo de la hipoxemia es el shunt intrapulmonar: responde poco al oxígeno"]),
  ("Varón de 29 años tras una semana de síntomas respiratorios", ["Dolor torácico, disnea, T 39,5 °C, confuso", "SatO₂ 78 % · crépitos bilaterales · opacidades bilaterales"]),
  {"rotulo": "Criterios de Berlín", "escala": "Berlín (SDRA)", "total": 4, "max": 4,
   "total_label": "Criterios cumplidos",
   "interpreta": "SDRA: hipoxemia por shunt",
   "items": [("Inicio < 1 semana tras la agresión", "✓", True), ("Opacidades bilaterales", "✓", True),
             ("No explicado por falla cardiaca", "✓", True), ("PaO₂/FiO₂ ≤ 300", "✓", True)],
   "bandas": [("< 4", "No es SDRA", "Buscar otra causa", False),
              ("4 de 4", "SDRA", "Ventilación protectora con PEEP", True)]},
  ["Shunt: la sangre pasa por alvéolos sin aire; subir la FiO₂ no corrige bien.",
   "Ventilación protectora: volumen corriente 6 ml/kg de peso ideal.",
   "PEEP para reclutar alvéolos."],
  "ARDS Definition Task Force – Berlin definition (JAMA 2012) · ATS/ESICM – ARDS guideline (2024)")

# PED-208 · termómetro
V("termometro", "PED-208", "neonato-meningitis-e-coli-21-dias", "Duración del antibiótico en la meningitis neonatal",
  "PEDIATRÍA ENAM: MENINGITIS NEONATAL POR E. COLI", "PEDIATRÍA",
  ("Meningitis neonatal", ["La duración depende del germen",
   "Gramnegativos (E. coli): 21 días (o 14 tras LCR estéril)"]),
  ("Neonato con LCR positivo a E. coli", ["Tratado según sensibilidad", "Buena evolución"]),
  {"rotulo": "Germen",
   "niveles": [("SGB", "Estreptococo B", ["14 días"]),
               ("Listeria", "Bacilo grampositivo", ["14-21 días"]),
               ("Gramneg.", "E. coli, Klebsiella", ["E. COLI: 21 DÍAS", "Riesgo de abscesos"])],
   "caso_nivel": 2, "ruta_titulo": "Plan", "paso_label": "PASO",
   "pasos": [(1, "Antibiótico por 21 días", ["Cefotaxima o según antibiograma"], True),
             (2, "Repetir punción lumbar", ["A las 48-72 h: debe ser estéril"], False),
             (3, "Neuroimagen y audición", ["Buscar complicaciones y secuelas"], False)]},
  ["Acortar el tratamiento aumenta las recaídas.",
   "Las cefalosporinas no cubren Listeria.",
   "Seguimiento del neurodesarrollo."],
  "AAP – Red Book (2024) · " + NELSON)

# GAS-069 · puntaje
V("puntaje", "GAS-069", "alcoholico-dolor-dorso-lipasa-alta-cullen-pancreatitis", "Epigastralgia intensa en el alcohólico",
  "GASTROENTEROLOGÍA ENAM: PANCREATITIS AGUDA GRAVE", "GASTROENTEROLOGÍA",
  ("Pancreatitis aguda", ["Diagnóstico: 2 de 3 criterios de Atlanta",
   "Cullen (equimosis periumbilical) indica sangrado retroperitoneal: forma grave"]),
  ("Varón de 38 años alcohólico", ["Epigastralgia intensa al dorso · PA 90/55 · FC 135 · T 38,5", "Cullen (+) · amilasa 370 · lipasa 620 · leucocitosis"]),
  {"rotulo": "Criterios de Atlanta", "escala": "Atlanta (2 de 3)", "total": 2, "max": 3,
   "total_label": "Criterios cumplidos",
   "interpreta": "Pancreatitis aguda confirmada",
   "items": [("Dolor epigástrico típico al dorso", "✓", True), ("Lipasa o amilasa ≥ 3 veces lo normal", "✓", True),
             ("Imagen compatible (TC, eco)", "—", False)],
   "bandas": [("< 2", "No confirma", "Buscar otra causa", False),
              ("≥ 2", "Pancreatitis", "Líquidos EV, analgesia, UCI si hay falla", True)]},
  ["Hipotensión y taquicardia con SIRS: riesgo de falla orgánica.",
   "Grey Turner: equimosis en flancos; Cullen: periumbilical.",
   "La TC se pide si hay duda o a las 72 h si no mejora."],
  "Revised Atlanta classification (Gut 2013) · ACG – Management of acute pancreatitis (2024)")

# GIN-219 · matriz
V("matriz", "GIN-219", "test-estresante-tres-contracciones-sin-desaceleraciones-negativo", "Interpretar el test estresante",
  "OBSTETRICIA ENAM: TEST ESTRESANTE", "OBSTETRICIA",
  ("Prueba de tolerancia a las contracciones", ["Se necesitan 3 contracciones en 10 minutos",
   "Sin desaceleraciones tardías ni variables = negativa (feto tolera)"]),
  ("Gestante de 41 semanas con Bishop favorable", ["3 contracciones en 10 min de buena intensidad", "Sin desaceleraciones tardías ni variables"]),
  {"rotulo": "Resultado y criterio", "eje_x": "Rasgo", "eje_y": "Resultado",
   "cols": ["Criterio", "Conducta"], "rows": ["Negativa", "Positiva", "Equívoca", "Insatisfactoria"], "caso": (0, 0),
   "cells": [[("SIN DESACELERACIONES", ["Con 3 en 10 min"]), ("Parto vaginal posible", [])],
             [("Tardías en ≥ 50 %", []), ("Cesárea", [])],
             [("Tardías o variables ocasionales", []), ("Repetir o más pruebas", [])],
             [("< 3 contracciones", []), ("Repetir", [])]]},
  ["Negativo es buen resultado: el feto tiene reserva.",
   "Contraindicado en placenta previa y cesárea corporal previa.",
   "Hoy se usa más el perfil biofísico."],
  "ACOG – Practice Bulletin 145: Antepartum fetal surveillance (2014; 2021) · " + WILLIAMS)

# NRL-054 · puntaje
V("puntaje", "NRL-054", "meningitis-subaguda-vi-par-lcr-linfocitico-glucosa-baja-tb", "Meningitis subaguda con pares craneales",
  "NEUROLOGÍA ENAM: MENINGITIS TUBERCULOSA", "NEUROLOGÍA",
  ("Meningitis tuberculosa", ["Curso de semanas, pares craneales (VI), LCR linfocitario",
   "Proteínas muy altas y glucosa baja"]),
  ("Varón de 50 años con 3 semanas de febrícula y cefalea", ["Confuso, signos meníngeos, paresia bilateral del VI par", "LCR: 250 células, 80 % linfocitos, proteínas 200, glucosa 20"]),
  {"rotulo": "Puntaje de Thwaites", "escala": "Thwaites", "total": -3, "max": 13,
   "total_label": "Puntaje del caso",
   "interpreta": "≤ 4: meningitis tuberculosa",
   "items": [("Edad ≥ 36 años", "+2", True), ("Síntomas ≥ 6 días", "−5", True),
             ("Leucocitos en sangre ≥ 15 000", "+4", False), ("Células en LCR ≥ 900", "+3", False),
             ("Neutrófilos en LCR ≥ 75 %", "+4", False)],
   "bandas": [("≤ 4", "Tuberculosa", "HRZE + dexametasona", True),
              ("> 4", "Bacteriana", "Ceftriaxona + vancomicina", False)]},
  ["GeneXpert y ADA en LCR ayudan a confirmar.",
   "Criptococo: pensar en VIH; tinta china y antígeno.",
   "La viral tiene glucosa normal."],
  "Thwaites GE et al. (Lancet 2002) · MINSA – NTS 200 (2023)")

# SP-160 · radial
V("radial", "SP-160", "organizacion-comunal-sarampion-mensajes-educativos", "Rol de la comunidad frente al sarampión",
  "SALUD PÚBLICA ENAM: COMUNICACIÓN EDUCATIVA", "SALUD PÚBLICA",
  ("Participación comunitaria", ["La organización comunal no vacuna ni hace triaje",
   "Sí puede difundir mensajes clave: vacunarse, reconocer síntomas, acudir a tiempo"]),
  ("Riesgo de transmisión de sarampión en el Perú", ["¿Qué actividad puede hacer la organización comunal?"]),
  {"rotulo": "Mapa del tema", "centro": "ORGANIZACIÓN COMUNAL", "centro_sub": "¿Qué le corresponde?", "ans": 0,
   "items": [("MENSAJES EDUCATIVOS", ["Vacunación, signos de alarma", "Llega a cada familia"]),
             ("Triaje de eruptivas", ["Del establecimiento"]),
             ("Vacunación SPR", ["Del personal de salud"]),
             ("Vigilancia de ESAVI", ["Del sistema de salud"]),
             ("Búsqueda de casos", ["Apoyo con el equipo de salud"])],
   "ruta": ["Líderes comunales", "Conocen a su población", "Informan y motivan", "MENSAJES CLAVE"]},
  ["Mensaje clave: fiebre + erupción = acudir al establecimiento.",
   "La vacuna SPR se aplica a los 12 y 18 meses.",
   "Los agentes comunitarios ayudan a ubicar a no vacunados."],
  "MINSA – Plan nacional de mantenimiento de la eliminación del sarampión · OPS – Comunicación de riesgos (2019)")

# GIN-220 · termómetro
V("termometro", "GIN-220", "amenaza-parto-pretermino-corticoides-24-36-semanas", "Corticoides prenatales según las semanas",
  "OBSTETRICIA ENAM: MADURACIÓN PULMONAR FETAL", "OBSTETRICIA",
  ("Corticoides prenatales", ["Reducen membrana hialina, hemorragia intraventricular y muerte neonatal",
   "Se indican entre las 24 y las 34-36 semanas con riesgo de parto pretérmino"]),
  ("Amenaza de parto prematuro", ["¿En qué edad gestacional se dan corticoides?"]),
  {"rotulo": "Edad gestacional",
   "niveles": [("< 24", "Periviable", ["Individualizar"]),
               ("24-34", "Pretérmino", ["INDICADOS", "Máximo beneficio"]),
               ("34-36", "Pretérmino tardío", ["Considerar si no recibió antes"]),
               ("≥ 37", "A término", ["No indicados"])],
   "caso_nivel": 1, "ruta_titulo": "Esquema", "paso_label": "PASO",
   "pasos": [(1, "Betametasona 12 mg IM", ["2 dosis cada 24 h"], True),
             (2, "O dexametasona 6 mg IM", ["4 dosis cada 12 h"], False),
             (3, "Efecto máximo", ["Entre 24 h y 7 días"], False)]},
  ["En la diabética pretérmino tardía, vigilar hipoglucemia neonatal.",
   "Un solo ciclo de rescate si pasaron > 14 días.",
   "No retrasan un parto indicado por urgencia materna o fetal."],
  "ACOG – Committee Opinion 713: Antenatal corticosteroid therapy (2017; 2021) · OMS (2022)")

# PED-209 · fases
V("fases", "PED-209", "encefalopatia-hipoxica-moderada-hipotermia-antes-6-horas", "Ventana de la hipotermia terapéutica",
  "PEDIATRÍA ENAM: HIPOTERMIA TERAPÉUTICA", "PEDIATRÍA",
  ("Hipotermia terapéutica", ["Reduce muerte y discapacidad en la encefalopatía hipóxico-isquémica",
   "Debe iniciarse en las primeras 6 horas de vida"]),
  ("RN a término que requirió reanimación avanzada", ["Encefalopatía hipóxico-isquémica moderada", "Será transferido para hipotermia"]),
  {"rotulo": "Tiempo desde el nacimiento", "ans": 0,
   "fases": [("0-6 h", "Ventana", "INICIAR HIPOTERMIA", ["33,5 °C, cuerpo entero"]),
             ("72 h", "Mantener", "Enfriamiento", ["Monitoreo continuo"]),
             ("Recalentar", "0,5 °C por hora", "Lento", ["Vigilar convulsiones"]),
             ("Seguimiento", "Meses", "Neurodesarrollo", ["RM al final"])],
   "curvas": [("Beneficio", SKY, [0.95, 0.85, 0.5, 0.3, 0.2, 0.15, 0.1])],
   "chips_titulo": "Ventana · marcada la correcta",
   "chips": [("6 horas", True), ("12 horas", False), ("18 horas", False), ("24 horas", False)]},
  ["Durante el traslado: apagar la fuente de calor (enfriamiento pasivo) con control de temperatura.",
   "Criterios: ≥ 36 semanas, acidosis o Apgar bajo y encefalopatía moderada-grave.",
   "Evitar la hipertermia: empeora el daño."],
  "AAP – Hypothermia and neonatal encephalopathy (Pediatrics 2014) · ILCOR (2025)")
