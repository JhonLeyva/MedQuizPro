"""Bloque 8 · parte D."""
from c8 import F8, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"
CMP = "Colegio Médico del Perú – Código de Ética y Deontología (2023)"

# END-067 · embudo
V("embudo", "END-067", "grasa-centripeta-acne-hirsutismo-dexametasona-cushing", "Causa del síndrome de Cushing",
  "ENDOCRINOLOGÍA ENAM: CUSHING EXÓGENO", "ENDOCRINOLOGÍA",
  ("Síndrome de Cushing", ["Exceso de glucocorticoides: grasa central, cara de luna, piel fina",
   "La causa más frecuente es exógena (iatrogénica)"]),
  ("Mujer de 29 años", ["Menos grasa en piernas y más en tronco y abdomen", "Edema facial, acné e hirsutismo"]),
  {"rotulo": "Embudo del antecedente",
   "inicio": "Rasgos de Cushing",
   "candidatos": ["Corticoides", "Anticonceptivos", "Obesidad familiar", "Trastorno nutricional"],
   "pasos": [("La obesidad simple no redistribuye la grasa", ["Obesidad familiar", "Trastorno nutricional"]),
             ("Los anticonceptivos no dan hipercortisolismo", ["Anticonceptivos"])],
   "final": ("CORTICOIDES EXÓGENOS", ["Dexametasona a dosis altas", "Retirar en forma gradual"]),
   "nota": "Si no hay corticoides exógenos: cortisol libre urinario o test de supresión."},
  ["No suspender bruscamente: insuficiencia suprarrenal.",
   "Estrías rojo vinosas, debilidad proximal, HTA.",
   "La causa endógena más común es el adenoma hipofisario."],
  "Endocrine Society – Cushing's syndrome guideline (2021) · " + HARRISON)

# INF-112 · termómetro
V("termometro", "INF-112", "huancayo-convulsion-quistes-viables-albendazol", "Estadios del cisticerco",
  "INFECTOLOGÍA ENAM: NEUROCISTICERCOSIS", "INFECTOLOGÍA",
  ("Neurocisticercosis", ["Larva de Taenia solium en el encéfalo",
   "Quistes viables: albendazol con corticoide y antiepiléptico"]),
  ("Varón de 18 años de Huancayo", ["Primera convulsión tónico-clónica", "RM: quistes viables con edema y algunas calcificaciones"]),
  {"rotulo": "Estadio del quiste",
   "niveles": [("Vesicular", "Viable", ["QUISTES VIABLES", "Antiparasitario"]),
               ("Coloidal", "Degenerando", ["Edema, realce"]),
               ("Granular", "Involución", ["Nódulo"]),
               ("Calcificado", "Muerto", ["Sin antiparasitario"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento en este caso", "paso_label": "PASO",
   "pasos": [(1, "Albendazol oral", ["15 mg/kg/día"], True),
             (2, "Corticoide", ["Dexametasona"], False),
             (3, "Antiepiléptico", ["Controla las crisis"], False)]},
  ["Niclosamida y praziquantel oral tratan la tenia intestinal.",
   "No dar antiparasitario si hay hipertensión endocraneana.",
   "Fondo de ojo antes de iniciar."],
  "IDSA/ASTMH – Neurocysticercosis guideline (2018) · MINSA (2023)")

# PED-235 · árbol
A("PED-235", "neonato-fc-110-respira-bien-cianosis-oxigeno", "Cianosis tras los pasos iniciales",
  "PEDIATRÍA ENAM: REANIMACIÓN NEONATAL", "PEDIATRÍA",
  ("Reanimación neonatal", ["Tras los pasos iniciales se evalúan respiración y FC",
   "Respira y FC > 100 pero cianosis central persistente: oxígeno"]),
  ("Neonato a término que nació flácido", ["Tras los pasos iniciales: FC 110", "Respira bien · cianosis perioral persistente"]),
  Q("¿Apnea, boqueo o FC < 100?", [
      L("Sí", "Ventilación a presión positiva", ["Con aire ambiente al inicio"]),
      Q("¿Cianosis o dificultad respiratoria?", [
          L("Sí", "OXÍGENO SUPLEMENTARIO", ["Oxímetro en mano derecha", "CPAP si hay dificultad"], path=True),
          L("No", "Cuidados de rutina", ["Contacto piel a piel"])],
        edge="No", path=True)], path=True),
  ("Saturación objetivo", [("Minuto 5", True), ("Minuto 10", False)], [
      ("SatO₂", ["80-85 %", "85-95 %"]),
      ("Ajuste", ["Subir O₂ si está debajo", "Bajar O₂ si está arriba"])]),
  ["La acrocianosis de manos y pies es normal.",
   "No aumentar la estimulación si ya respira.",
   "Reevaluar cada 30 segundos."],
  "AAP/AHA – Neonatal Resuscitation Program 8.ª ed. (2021)")

# SP-186 · tarjetas
V("tarjetas", "SP-186", "promocion-salud-mito-impone-estilos-de-vida", "Mitos y verdades de la promoción",
  "SALUD PÚBLICA ENAM: PROMOCIÓN DE LA SALUD", "SALUD PÚBLICA",
  ("Promoción de la salud", ["Da a las personas los medios para controlar su salud",
   "No impone conductas: facilita decisiones y entornos saludables"]),
  ("Pregunta de salud pública (OMS/OPS)", ["¿Cuál afirmación es un mito?"]),
  {"rotulo": "¿Cuál es un mito?", "ans": 0, "cards": [
      {"titulo": "IMPONE ESTILOS", "datos": [
          ("Afirmación", "Limita la autonomía", True), ("Es", "MITO", True),
          ("Realidad", "Empodera", True)],
       "pie": "Carta de Ottawa"},
      {"titulo": "Determinantes", "datos": [
          ("Afirmación", "Los reconoce", False), ("Es", "Verdad", False),
          ("Realidad", "Actúa sobre ellos", False)],
       "pie": "Base del enfoque"},
      {"titulo": "Biopsicosocial", "datos": [
          ("Afirmación", "Se articula", False), ("Es", "Verdad", False),
          ("Realidad", "Visión integral", False)],
       "pie": "Persona completa"},
      {"titulo": "Costo-efectiva", "datos": [
          ("Afirmación", "Prioriza población", False), ("Es", "Verdad", False),
          ("Realidad", "Mayor alcance", False)],
       "pie": "Intervenciones masivas"}]},
  ["Carta de Ottawa (1986): cinco áreas de acción.",
   "Incluye políticas públicas y entornos saludables.",
   "La participación comunitaria es central."],
  "OMS – Carta de Ottawa (1986) · OPS – Promoción de la salud (2019)")

# GIN-245 · puntaje
V("puntaje", "GIN-245", "bishop-posicion-media-borramiento-50-dilatacion-2", "Puntaje de Bishop",
  "OBSTETRICIA ENAM: ESCALA DE BISHOP", "OBSTETRICIA",
  ("Escala de Bishop", ["Valora la madurez del cuello antes de inducir",
   "≤ 6 desfavorable: madurar primero; ≥ 8 favorable"]),
  ("Gestante evaluada", ["Posición media, consistencia media", "Borramiento 50 %, dilatación 2 cm, altura -3"]),
  {"rotulo": "Bishop del caso", "escala": "Bishop", "total": 4, "max": 13,
   "total_label": "Puntaje total",
   "interpreta": "Cuello desfavorable",
   "items": [("Posición media", "1", True), ("Consistencia media", "1", True),
             ("Borramiento 50 %", "1", True), ("Dilatación 2 cm", "1", True),
             ("Altura -3", "0", False)],
   "bandas": [("≤ 6", "Desfavorable", "Madurar el cuello", True),
              ("7", "Intermedio", "Individualizar", False),
              ("≥ 8", "Favorable", "Oxitocina", False)]},
  ["Dilatación 1-2 cm = 1 punto; 3-4 cm = 2.",
   "Borramiento 40-50 % = 1 punto.",
   "Altura -3 = 0; -2 = 1; -1/0 = 2."],
  WILLIAMS + " · ACOG Practice Bulletin 107 (2009)")

# CIR-121 · radial
V("radial", "CIR-121", "tb-pulmonar-ulcera-anal-lateral-tuberculosa", "Úlcera anal fuera de la línea media",
  "CIRUGÍA ENAM: ÚLCERA ANAL SECUNDARIA", "CIRUGÍA",
  ("Fisura o úlcera anal atípica", ["La fisura común está en la línea media posterior",
   "Si es lateral: buscar causa secundaria (TB, Crohn, ITS, cáncer)"]),
  ("Mujer de 28 años con TB pulmonar", ["Dolor al defecar · hipertonía del esfínter", "Úlcera de 1 cm en la cara lateral del ano"]),
  {"rotulo": "Mapa del tema", "centro": "ÚLCERA LATERAL", "centro_sub": "Causas", "ans": 0,
   "items": [("TUBERCULOSIS", ["TB pulmonar activa", "Biopsia y BK"]),
             ("Crohn", ["Fisuras múltiples"]),
             ("Sífilis", ["Chancro anal"]),
             ("VIH", ["Úlceras atípicas"]),
             ("Cáncer", ["Bordes duros"])],
   "ruta": ["TB pulmonar", "Siembra intestinal", "Úlcera perianal", "TUBERCULOSIS"]},
  ["Biopsiar toda úlcera anal atípica.",
   "La TB perianal responde al esquema antituberculoso.",
   "Descartar VIH en toda TB."],
  "ASCRS – Anal fissure guideline (2023) · MINSA – NTS 200 (2023)")

# SP-187 · matriz
V("matriz", "SP-187", "comunidad-indigena-24-horas-rio-agentes-comunitarios-lactancia", "Estrategias en comunidades aisladas",
  "SALUD PÚBLICA ENAM: AGENTES COMUNITARIOS", "SALUD PÚBLICA",
  ("Agentes comunitarios de salud", ["Miembros de la comunidad capacitados por el establecimiento",
   "Dan continuidad cuando el equipo solo llega cada tres meses"]),
  ("Comunidad indígena a 24 h por río", ["4 lactantes menores de 6 meses", "El equipo de salud visita cada 3 meses"]),
  {"rotulo": "Estrategia y viabilidad", "eje_x": "Rasgo", "eje_y": "Estrategia",
   "cols": ["Factible", "Continuidad"], "rows": ["Lactario", "Cartillas", "Consulta mensual", "Agentes comunitarios"], "caso": (3, 1),
   "cells": [[("Poco", ["Pocos lactantes"]), ("Baja", [])],
             [("Sí", []), ("Baja", ["Solo informa"])],
             [("No", ["24 h de viaje"]), ("Baja", [])],
             [("Sí", ["Viven allí"]), ("ALTA", ["Visitas mensuales"])]]},
  ["Respetar la lengua y las costumbres.",
   "Supervisarlos en cada visita del equipo.",
   "También sirven para vigilancia comunitaria."],
  "MINSA – Lineamientos de agentes comunitarios de salud (2021) · OMS (2023)")

# CB-092 · matriz
V("matriz", "CB-092", "dm2-severa-dos-insulinas-velocidad-absorcion", "Tipos de insulina",
  "CIENCIAS BÁSICAS ENAM: FARMACOLOGÍA DE LA INSULINA", "CIENCIAS BÁSICAS",
  ("Formulaciones de insulina", ["Misma acción, distinta absorción desde el tejido subcutáneo",
   "Por eso cambian el inicio y la duración del efecto"]),
  ("Varón de 51 años con DM2 grave", ["Usa dos formulaciones de insulina", "¿En qué difieren principalmente?"]),
  {"rotulo": "Insulina y tiempos", "eje_x": "Dato", "eje_y": "Tipo",
   "cols": ["Inicio", "Duración"], "rows": ["Rápida", "Regular", "NPH", "Glargina"], "caso": (2, 0),
   "cells": [[("10-15 min", []), ("3-5 h", [])],
             [("30-60 min", []), ("6-8 h", [])],
             [("ABSORCIÓN LENTA", ["1-2 h (protamina)"]), ("12-16 h", [])],
             [("1-2 h", []), ("24 h", ["Sin pico"])]]},
  ["No tienen biodisponibilidad oral: son proteínas.",
   "La protamina o el zinc retrasan la absorción.",
   "Esquema basal-bolo: basal + rápida en comidas."],
  "Goodman & Gilman. Bases farmacológicas 14.ª ed. (2023) · ADA (2025)")

# GAS-077 · tarjetas
V("tarjetas", "GAS-077", "dm1-hipotiroidismo-hepatitis-ana-sma-autoinmune-tipo-1", "Tipos de hepatitis autoinmune",
  "GASTROENTEROLOGÍA ENAM: HEPATITIS AUTOINMUNE", "GASTROENTEROLOGÍA",
  ("Hepatitis autoinmune", ["Mujeres con otras enfermedades autoinmunes",
   "Tipo 1: ANA y anti-músculo liso; tipo 2: anti-LKM1"]),
  ("Mujer de 38 años con DM1 e hipotiroidismo", ["Ictericia, TGO 1200, TGP 2150", "ANA 1/160 · SMA 1/160 · anti-LKM 1/40"]),
  {"rotulo": "¿Qué tipo es?", "ans": 0, "cards": [
      {"titulo": "TIPO 1", "datos": [
          ("Anticuerpos", "ANA y SMA", True), ("Edad", "Adulta joven", True),
          ("Frecuencia", "La más común", True)],
       "pie": "Corticoides + azatioprina"},
      {"titulo": "Tipo 2", "datos": [
          ("Anticuerpos", "Anti-LKM1 alto", False), ("Edad", "Niñas", False),
          ("Frecuencia", "Rara", False)],
       "pie": "Más agresiva"},
      {"titulo": "Viral", "datos": [
          ("Anticuerpos", "Serología viral", False), ("Edad", "Cualquiera", False),
          ("Frecuencia", "Común", False)],
       "pie": "Sin autoanticuerpos"},
      {"titulo": "Tipo 3", "datos": [
          ("Anticuerpos", "Anti-SLA", False), ("Edad", "Adulta", False),
          ("Frecuencia", "Muy rara", False)],
       "pie": "Se agrupa con la tipo 1"}]},
  ["Confirmar con biopsia: hepatitis de interfase.",
   "IgG elevada apoya el diagnóstico.",
   "Suele mejorar pronto con corticoides."],
  "EASL – Autoimmune hepatitis guideline (2025) · AASLD (2019)")

# CAR-074 · termómetro
V("termometro", "CAR-074", "hipertensa-disnea-segundo-piso-nyha-clase-ii", "Clase funcional NYHA",
  "CARDIOLOGÍA ENAM: CLASIFICACIÓN NYHA", "CARDIOLOGÍA",
  ("Clasificación funcional NYHA", ["Mide cuánto limitan los síntomas la actividad física",
   "Clase II: síntomas con la actividad ordinaria"]),
  ("Mujer de 65 años, hipertensa", ["Disnea y fatiga al subir al segundo piso", "Tos seca y palpitaciones"]),
  {"rotulo": "Clase NYHA",
   "niveles": [("I", "Sin limitación", ["Actividad normal"]),
               ("II", "Limitación leve", ["ACTIVIDAD ORDINARIA", "Subir pisos"]),
               ("III", "Limitación marcada", ["Esfuerzo menor"]),
               ("IV", "En reposo", ["Síntomas constantes"])],
   "caso_nivel": 1, "ruta_titulo": "Qué hacer en este caso", "paso_label": "PASO",
   "pasos": [(1, "Ecocardiograma", ["Medir la FEVI"], True),
             (2, "Controlar la PA", ["IECA o ARA II"], False),
             (3, "Tratar según FEVI", ["Fármacos que dan sobrevida"], False)]},
  ["NYHA es funcional; los estadios A-D son estructurales.",
   "La clase puede mejorar con tratamiento.",
   "Eje -30°: desviación izquierda (HVI)."],
  "ESC – Heart failure guidelines (2021) · AHA/ACC (2022)")

# CIR-122 · árbol
A("CIR-122", "hernia-umbilical-4-cm-reducida-sin-isquemia-electiva", "Hernia umbilical encarcelada",
  "CIRUGÍA ENAM: HERNIA UMBILICAL", "CIRUGÍA",
  ("Hernia encarcelada", ["No se reduce, pero sin compromiso vascular",
   "Si se reduce sin isquemia: programar cirugía electiva"]),
  ("Mujer de 32 años", ["Hernia umbilical de 4 cm dolorosa e irreductible", "TAC sin isquemia · se reduce y cede el dolor"]),
  Q("¿Signos de estrangulación?", [
      L("Sí", "Cirugía de emergencia", ["Isquemia u obstrucción"]),
      Q("¿Se logra reducir?", [
          L("Sí", "CIRUGÍA ELECTIVA", ["Hernioplastía con malla", "Programada"], path=True),
          L("No", "Cirugía urgente", ["Encarcelada persistente"])],
        edge="No", path=True)], path=True),
  ("Tras reducir", [("Hacer", True), ("No hacer", False)], [
      ("Plan", ["Programar hernioplastía", "Solo observar"]),
      ("Alarma", ["Volver si duele o vomita", "Alta sin control"])]),
  ["Hernias > 1-2 cm en adultos: reparar con malla.",
   "No reducir si hay signos de estrangulación.",
   "En niños suelen cerrar antes de los 4-5 años."],
  "European Hernia Society – Umbilical hernia guideline (2020)")

# PED-236 · puntaje
V("puntaje", "PED-236", "varicela-sato2-89-crepitos-aciclovir-ev", "Varicela complicada",
  "PEDIATRÍA ENAM: NEUMONÍA POR VARICELA", "PEDIATRÍA",
  ("Neumonía por varicela", ["Complicación grave, más en adultos e inmunodeprimidos",
   "Tratamiento: aciclovir intravenoso y soporte respiratorio"]),
  ("Escolar de 8 años, previamente sano", ["Vesículas en distintos estadios, fiebre 39 °C", "SatO₂ 89 % · crépitos bibasales"]),
  {"rotulo": "Signos de gravedad en el caso", "escala": "Signos", "total": 3, "max": 4,
   "total_label": "Signos presentes",
   "interpreta": "Neumonía varicelosa",
   "items": [("Hipoxemia (SatO₂ 89 %)", "1", True), ("Crépitos bibasales", "1", True),
             ("Fiebre alta persistente", "1", True), ("Alteración neurológica", "0", False)],
   "bandas": [("0", "No complicada", "Manejo sintomático", False),
              ("≥ 1", "Complicada", "Aciclovir EV + oxígeno", True)]},
  ["Aciclovir 10 mg/kg c/8 h por 7-10 días.",
   "Nunca dar aspirina: síndrome de Reye.",
   "Vacuna: 2 dosis en el esquema."],
  "AAP Red Book (2024) · " + NELSON)

# CIR-123 · radial
V("radial", "CIR-123", "colecistitis-complicada-leucocitosis-gramnegativos-anaerobios", "Gérmenes de la vía biliar",
  "CIRUGÍA ENAM: COLECISTITIS COMPLICADA", "CIRUGÍA",
  ("Colecistitis aguda complicada", ["Infección por flora intestinal",
   "Cubrir gramnegativos entéricos y anaerobios"]),
  ("Mujer de 45 años con litiasis", ["Dolor en hipocondrio derecho y fiebre", "Leucocitos 18 000"]),
  {"rotulo": "Mapa del tema", "centro": "BILIS", "centro_sub": "Gérmenes", "ans": 0,
   "items": [("GRAMNEGATIVOS", ["E. coli, Klebsiella", "Más anaerobios"]),
             ("Anaerobios", ["Bacteroides fragilis"]),
             ("Enterococo", ["Menos frecuente"]),
             ("Grampositivos piel", ["No son la causa"])],
   "ruta": ["Obstrucción del cístico", "Bilis estancada", "Flora intestinal", "GRAMNEGATIVOS"]},
  ["Esquema: ceftriaxona + metronidazol.",
   "Grave: piperacilina-tazobactam.",
   "Colecistectomía temprana."],
  "Tokyo Guidelines (TG18) · IDSA – Intra-abdominal infections (2010)")

# GAS-078 · fases
V("fases", "GAS-078", "calculo-ampolla-vater-tripsinogeno-activado-pancreatitis", "Cómo se produce la pancreatitis",
  "GASTROENTEROLOGÍA ENAM: FISIOPATOLOGÍA DE LA PANCREATITIS", "GASTROENTEROLOGÍA",
  ("Pancreatitis aguda", ["Activación prematura del tripsinógeno dentro del páncreas",
   "La tripsina activa las demás enzimas: autodigestión"]),
  ("Varón de 52 años", ["Cálculo que obstruye la ampolla de Vater", "Pancreatitis aguda biliar"]),
  {"rotulo": "Secuencia de la lesión", "ans": 1,
   "fases": [("Obstrucción", "Ampolla", "Presión alta", ["Reflujo y estasis"]),
             ("Activación", "En el acino", "TRIPSINÓGENO → TRIPSINA", ["Dentro del páncreas"]),
             ("Cascada", "Enzimas", "Autodigestión", ["Elastasa, fosfolipasa"]),
             ("Sistémica", "Citoquinas", "Inflamación", ["SIRS, falla orgánica"])],
   "curvas": [("Daño pancreático", ROSE, [0.1, 0.3, 0.55, 0.75, 0.85, 0.9, 0.9])],
   "chips_titulo": "Evento clave · marcado el correcto",
   "chips": [("Tripsinógeno a tripsina", True), ("Bilis activa enzimas", False), ("Quimotripsinógeno", False), ("Enzimas biliares", False)]},
  ["Normalmente la enteropeptidasa activa la tripsina en el duodeno.",
   "El inhibidor de tripsina (SPINK1) protege al páncreas.",
   "Tratamiento: hidratación, analgesia y dieta precoz."],
  "Robbins y Cotran. Patología estructural y funcional 10.ª ed. (2021)")

# SP-188 · tarjetas
V("tarjetas", "SP-188", "pandemia-dos-ventiladores-cuatro-pacientes-pronostico", "Asignación de recursos escasos",
  "SALUD PÚBLICA ENAM: ÉTICA EN LA PANDEMIA", "SALUD PÚBLICA",
  ("Recursos escasos", ["Justicia distributiva: salvar más vidas",
   "Priorizar a quien tiene mayor probabilidad de sobrevivir"]),
  ("Hospital en pandemia", ["Dos ventiladores y cuatro pacientes", "Dos con buen pronóstico y dos con enfermedad avanzada"]),
  {"rotulo": "¿Qué criterio usar?", "ans": 0, "cards": [
      {"titulo": "PRONÓSTICO", "datos": [
          ("Criterio", "Probabilidad de vivir", True), ("Principio", "Justicia, beneficencia", True),
          ("Aceptado", "Sí", True)],
       "pie": "Triaje con criterios clínicos"},
      {"titulo": "Orden de llegada", "datos": [
          ("Criterio", "Quién llegó antes", False), ("Principio", "Igualdad formal", False),
          ("Aceptado", "No en crisis", False)],
       "pie": "No maximiza vidas"},
      {"titulo": "Azar", "datos": [
          ("Criterio", "Sorteo", False), ("Principio", "Igualdad", False),
          ("Aceptado", "Solo si empatan", False)],
       "pie": "Último recurso"},
      {"titulo": "Recursos económicos", "datos": [
          ("Criterio", "Quién paga", False), ("Principio", "Ninguno", False),
          ("Aceptado", "Nunca", False)],
       "pie": "Discriminatorio"}]},
  ["Usar protocolos de triaje transparentes.",
   "Ofrecer cuidados paliativos a quien no recibe ventilador.",
   "Reevaluar periódicamente."],
  "OMS – Ethics and COVID-19: resource allocation (2020) · " + CMP)

# PED-237 · embudo
V("embudo", "PED-237", "prurito-anal-nocturno-graham-positivo-albendazol", "Tratamiento de la oxiuriasis",
  "PEDIATRÍA ENAM: OXIURIASIS", "PEDIATRÍA",
  ("Oxiuriasis", ["Enterobius vermicularis: prurito anal nocturno",
   "Diagnóstico con cinta adhesiva (test de Graham)"]),
  ("Preescolar de 3 años", ["Prurito perianal nocturno y ardor al orinar", "Urocultivo negativo · Graham positivo"]),
  {"rotulo": "Embudo del tratamiento",
   "inicio": "Graham positivo",
   "candidatos": ["Albendazol", "Metronidazol", "Cefalexina", "Piperazina"],
   "pasos": [("Es un helminto, no bacteria ni protozoo", ["Metronidazol", "Cefalexina"]),
             ("Piperazina: menos eficaz, en desuso", ["Piperazina"])],
   "final": ("ALBENDAZOL", ["400 mg dosis única", "Repetir a las 2 semanas"]),
   "nota": "Tratar a toda la familia y lavar ropa de cama."},
  ["Cortar uñas y lavar manos: evita la reinfección.",
   "Puede causar vulvovaginitis en niñas.",
   "Alternativa: mebendazol."],
  NELSON + " · CDC – Enterobiasis (2024)")

# PED-238 · matriz
V("matriz", "PED-238", "lactante-10-meses-exantema-al-ceder-fiebre-roseola", "Exantemas del lactante",
  "PEDIATRÍA ENAM: EXANTEMA SÚBITO", "PEDIATRÍA",
  ("Exantema súbito (roséola)", ["Herpes virus 6: fiebre alta 3-4 días",
   "El exantema aparece cuando cede la fiebre"]),
  ("Lactante de 10 meses", ["Fiebre y malestar que cedieron", "Luego lesiones morbiliformes en cuello y tronco"]),
  {"rotulo": "Fiebre y exantema", "eje_x": "Rasgo", "eje_y": "Enfermedad",
   "cols": ["Fiebre", "Exantema"], "rows": ["Exantema súbito", "Sarampión", "Varicela", "Kawasaki"], "caso": (0, 1),
   "cells": [[("Alta, 3-4 días", []), ("AL CEDER LA FIEBRE", ["Tronco y cuello"])],
             [("Con el exantema", []), ("Céfalo-caudal", ["Koplik, tos"])],
             [("Moderada", []), ("Vesículas", ["Distintos estadios"])],
             [("≥ 5 días", []), ("Polimorfo", ["Conjuntivitis, labios"])]]},
  ["Puede causar convulsión febril.",
   "Manejo sintomático.",
   "Edad típica: 6 meses a 2 años."],
  NELSON + " · AAP Red Book (2024)")

# SP-189 · termómetro
V("termometro", "SP-189", "objetivo-evaluar-controlar-calibrar-nivel-aplicativo", "Niveles de investigación",
  "SALUD PÚBLICA ENAM: NIVELES DE INVESTIGACIÓN", "SALUD PÚBLICA",
  ("Niveles de investigación", ["Se reconocen por el verbo del objetivo general",
   "Evaluar, controlar o calibrar: nivel aplicativo"]),
  ("Pregunta de metodología", ["Objetivo con verbos evaluar, controlar o calibrar", "¿Qué nivel de investigación es?"]),
  {"rotulo": "Nivel y verbos",
   "niveles": [("Descriptivo", "Describir", ["Caracterizar, medir"]),
               ("Explicativo", "Explicar", ["Causas, relacionar"]),
               ("Predictivo", "Predecir", ["Estimar, anticipar"]),
               ("Aplicativo", "Intervenir", ["EVALUAR, CONTROLAR", "Calibrar"])],
   "caso_nivel": 3, "ruta_titulo": "Rasgos del nivel aplicativo", "paso_label": "RASGO",
   "pasos": [(1, "Resuelve un problema práctico", ["Mejora procedimientos"], True),
             (2, "Parte de conocimiento previo", ["Ya descrito y explicado"], False),
             (3, "Mide su efecto", ["Evalúa resultados"], False)]},
  ["El nivel exploratorio antecede al descriptivo.",
   "El relacional busca asociación sin causalidad.",
   "Clasificación usada en el Perú (Supo)."],
  "Supo J. Niveles y tipos de investigación (2015) · " + GORDIS)

# NRL-060 · tarjetas
V("tarjetas", "NRL-060", "parkinson-77-anos-confusion-memoria-biperideno", "Efectos adversos antiparkinsonianos",
  "NEUROLOGÍA ENAM: ANTICOLINÉRGICOS EN EL ANCIANO", "NEUROLOGÍA",
  ("Antiparkinsonianos", ["Cada grupo tiene efectos adversos típicos",
   "Anticolinérgicos: confusión y amnesia en ancianos"]),
  ("Varón de 77 años con Parkinson", ["Inicia tratamiento", "Deterioro de memoria y confusión"]),
  {"rotulo": "¿Qué fármaco lo causa?", "ans": 0, "cards": [
      {"titulo": "BIPERIDENO", "datos": [
          ("Grupo", "Anticolinérgico", True), ("Efecto", "Confusión, amnesia", True),
          ("En ancianos", "Evitar", True)],
       "pie": "Retención urinaria, glaucoma"},
      {"titulo": "Levodopa", "datos": [
          ("Grupo", "Precursor dopamina", False), ("Efecto", "Discinesias", False),
          ("En ancianos", "Primera línea", False)],
       "pie": "Náuseas, hipotensión"},
      {"titulo": "Pramipexol", "datos": [
          ("Grupo", "Agonista dopamina", False), ("Efecto", "Alucinaciones", False),
          ("En ancianos", "Con cautela", False)],
       "pie": "Control de impulsos"},
      {"titulo": "Selegilina", "datos": [
          ("Grupo", "IMAO-B", False), ("Efecto", "Insomnio", False),
          ("En ancianos", "Posible", False)],
       "pie": "Interacciones"}]},
  ["Criterios de Beers: evitar anticolinérgicos en mayores.",
   "Retirar el fármaco y reevaluar la cognición.",
   "Levodopa es de elección en mayores de 65 años."],
  "AGS – Beers Criteria (2023) · " + HARRISON)

# SP-190 · radial
V("radial", "SP-190", "comunidad-agricola-anemia-sesiones-demostrativas", "Promoción contra la anemia",
  "SALUD PÚBLICA ENAM: ANEMIA INFANTIL", "SALUD PÚBLICA",
  ("Sesiones demostrativas", ["Las madres aprenden a preparar alimentos ricos en hierro",
   "Educación práctica con insumos de la zona"]),
  ("Comunidad agrícola y ganadera", ["Alta anemia en menores de 5 años", "Poco conocimiento de nutrición"]),
  {"rotulo": "Mapa del tema", "centro": "ANEMIA", "centro_sub": "¿Qué priorizar?", "ans": 0,
   "items": [("SESIONES DEMOSTRATIVAS", ["Aprender haciendo", "Hígado, sangrecita"]),
             ("Folletos", ["Poco impacto"]),
             ("Capacitar al personal", ["No llega a madres"]),
             ("Desparasitación en medios", ["Complementa"])],
   "ruta": ["Poco conocimiento", "Mala alimentación", "Educación práctica", "SESIONES DEMOSTRATIVAS"]},
  ["Aprovechar alimentos locales de origen animal.",
   "Suplementar hierro desde los 4 meses.",
   "Seguimiento con visitas domiciliarias."],
  "MINSA – Plan multisectorial contra la anemia (2018) · NTS 213 (2024)")

# CIR-124 · árbol
A("CIR-124", "nino-transito-hematoma-subcapsular-hepatico-2-cm-observacion", "Trauma hepático en el niño",
  "CIRUGÍA ENAM: TRAUMA HEPÁTICO", "CIRUGÍA",
  ("Trauma hepático cerrado", ["Si está hemodinámicamente estable: manejo no operatorio",
   "Observación, controles de hematocrito y reposo"]),
  ("Niño de 6 años, accidente de tránsito", ["Dolor abdominal · Hto 44 %", "FAST: líquido perihepático · TC: hematoma de 2 cm"]),
  Q("¿Hemodinámicamente estable?", [
      Q("¿Lesión sin sangrado activo?", [
          L("Sí", "OBSERVACIÓN CONTINUA", ["Hematocrito seriado", "Reposo en cama"], path=True),
          L("No: extravasación", "Angioembolización", ["Si sigue estable"])],
        edge="Sí", path=True),
      L("No", "Laparotomía", ["Tras reanimación"])], path=True),
  ("Manejo no operatorio", [("Continuar", True), ("Operar", False)], [
      ("Cuándo", ["Estable, sin peritonitis", "Inestable o peritonitis"]),
      ("Éxito", ["> 90 % en niños", "—"])]),
  ["La TC define el grado de la lesión (AAST).",
   "Transfundir solo si baja el hematocrito.",
   "El FAST positivo no obliga a operar si está estable."],
  ATLS + " · APSA – Blunt liver and spleen injury (2019)")

# PED-239 · puntaje
V("puntaje", "PED-239", "prematuro-27-semanas-oxigeno-28-dias-displasia", "Riesgo de displasia broncopulmonar",
  "PEDIATRÍA ENAM: DISPLASIA BRONCOPULMONAR", "PEDIATRÍA",
  ("Displasia broncopulmonar", ["Oxígeno a los 28 días de vida en el prematuro",
   "El factor más potente es la menor edad gestacional"]),
  ("Prematuro de 27 semanas", ["Ventilación mecánica y oxígeno prolongado", "A los 28 días: dificultad respiratoria, hiperinsuflación"]),
  {"rotulo": "Factores en el caso", "escala": "Factores", "total": 3, "max": 4,
   "total_label": "Factores presentes",
   "interpreta": "Displasia broncopulmonar",
   "items": [("Edad gestacional < 28 semanas", "Mayor", True), ("Ventilación mecánica", "1", True),
             ("Oxígeno prolongado", "1", True), ("Infección neonatal", "?", False)],
   "bandas": [("Sin O₂ a 28 d", "No DBP", "Seguimiento", False),
              ("O₂ a 28 d", "DBP", "Nutrición, O₂ y cafeína", True)]},
  ["El surfactante y la cafeína disminuyen el riesgo.",
   "Se clasifica a las 36 semanas corregidas.",
   "Prematuridad tardía tiene poco riesgo."],
  NELSON + " · NICHD – BPD definition (2001, actualización 2019)")

# GIN-246 · termómetro
V("termometro", "GIN-246", "trabajo-parto-6-7-contracciones-10-minutos-taquisistolia", "Actividad uterina",
  "OBSTETRICIA ENAM: TAQUISISTOLIA", "OBSTETRICIA",
  ("Actividad uterina en el trabajo de parto", ["Normal: 3 a 5 contracciones en 10 minutos",
   "Más de 5 en 10 min (promedio de 30 min): taquisistolia"]),
  ("Gestante a término en trabajo de parto", ["Monitoreo de 30 minutos", "6 a 7 contracciones cada 10 minutos"]),
  {"rotulo": "Contracciones en 10 minutos",
   "niveles": [("< 3", "Hipodinamia", ["Bradisistolia"]),
               ("3-5", "Normal", ["Actividad adecuada"]),
               ("> 5", "Exceso", ["TAQUISISTOLIA", "6-7 en 10 min"]),
               ("Tono alto", "Hipertonía", ["Contracción > 2 min"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta ante taquisistolia", "paso_label": "PASO",
   "pasos": [(1, "Evaluar la FCF", ["Si hay alteraciones"], True),
             (2, "Suspender oxitocina", ["Si se usa"], False),
             (3, "Tocolítico agudo", ["Si persiste con FCF alterada"], False)]},
  ["El término hiperestimulación ya no se recomienda.",
   "Posición lateral izquierda y líquidos EV.",
   "Terbutalina SC si no cede."],
  WILLIAMS + " · ACOG Practice Bulletin 106 (2009)")

# GIN-247 · puntaje
V("puntaje", "GIN-247", "ptgo-90-160-140-gestante-no-diabetica", "Prueba de tolerancia a la glucosa",
  "OBSTETRICIA ENAM: TAMIZAJE DE DIABETES GESTACIONAL", "OBSTETRICIA",
  ("PTGO de 75 g (24-28 semanas)", ["Diabetes gestacional si un valor alcanza el corte",
   "Cortes: ayunas ≥ 92, 1 h ≥ 180, 2 h ≥ 153 mg/dL"]),
  ("Gestante de 24 semanas", ["PTGO: ayunas 90, 1 hora 160", "2 horas 140 mg/dL"]),
  {"rotulo": "Valores sobre el corte", "escala": "PTGO", "total": 0, "max": 3,
   "total_label": "Valores alterados",
   "interpreta": "Gestante no diabética",
   "items": [("Ayunas 90 (corte 92)", "0", False), ("1 hora 160 (corte 180)", "0", False),
             ("2 horas 140 (corte 153)", "0", False)],
   "bandas": [("0", "Normal", "Control prenatal habitual", True),
              ("≥ 1", "Diabetes gestacional", "Dieta y automonitoreo", False)]},
  ["Basta un valor alterado para el diagnóstico.",
   "Ayunas ≥ 126 en el primer control: diabetes previa.",
   "Repetir si aparecen nuevos factores de riesgo."],
  "IADPSG (2010) · ADA – Standards of Care in Diabetes (2025)")

# PED-240 · radial
V("radial", "PED-240", "puerpera-pezones-agrietados-labios-no-evertidos-agarre", "Signos de un buen agarre",
  "PEDIATRÍA ENAM: LACTANCIA MATERNA", "PEDIATRÍA",
  ("Agarre al pecho", ["El bebé debe tomar gran parte de la areola",
   "Si solo toma el pezón: dolor, grietas y poca leche"]),
  ("Primigesta de 22 años, día 5 posparto", ["Pezones adoloridos y agrietados", "El bebé toma solo el pezón, labios poco evertidos"]),
  {"rotulo": "Mapa del tema", "centro": "AGARRE", "centro_sub": "Buen agarre", "ans": 0,
   "items": [("LABIOS EVERTIDOS", ["Hacia afuera", "Falla en el caso"]),
             ("Boca bien abierta", ["Ángulo amplio"]),
             ("Mentón en el pecho", ["Toca la mama"]),
             ("Más areola abajo", ["Que arriba"])],
   "ruta": ["Toma solo el pezón", "Grietas y dolor", "Corregir técnica", "LABIOS EVERTIDOS"]},
  ["No se necesita fórmula si se corrige la técnica.",
   "Aplicar leche materna en las grietas.",
   "Posición: panza con panza."],
  "OMS/UNICEF – Consejería en lactancia materna (2021) · MINSA (2019)")

# INF-113 · árbol
A("INF-113", "fiebre-retroocular-dengue-sin-viajes-aedes-autoctono", "Clasificación del caso de dengue",
  "INFECTOLOGÍA ENAM: VIGILANCIA DEL DENGUE", "INFECTOLOGÍA",
  ("Caso autóctono", ["Adquirido en el lugar de residencia",
   "Sin viajes y con Aedes presente en la zona"]),
  ("Paciente en zona con Aedes aegypti", ["5 días de fiebre y dolor retroocular", "Prueba positiva · sin viajes recientes"]),
  Q("¿Viajó a zona con transmisión?", [
      L("Sí", "Caso importado", ["Se infectó en otro lugar"]),
      Q("¿Hay Aedes en su zona?", [
          L("Sí", "CASO AUTÓCTONO", ["Transmisión local", "Activar control vectorial"], path=True),
          L("No", "Investigar", ["Otra vía o error"])],
        edge="No", path=True)], path=True),
  ("Clasificación", [("Por laboratorio", True), ("Por origen", False)], [
      ("Opciones", ["Probable o confirmado", "Autóctono o importado"]),
      ("En el caso", ["Confirmado", "Autóctono"])]),
  ["Notificación obligatoria en 24 horas.",
   "Búsqueda de febriles en la zona.",
   "Eliminar criaderos alrededor de la vivienda."],
  "MINSA – NTS de vigilancia de dengue (2023) · OPS (2022)")

# NRL-061 · matriz
V("matriz", "NRL-061", "fractura-base-craneo-midriasis-ojo-abajo-afuera-iii-par", "Parálisis oculomotoras",
  "NEUROLOGÍA ENAM: PARÁLISIS DEL III PAR", "NEUROLOGÍA",
  ("Parálisis del III par", ["Ojo abajo y afuera, ptosis y midriasis",
   "Causas: trauma, aneurisma o herniación del uncus"]),
  ("Varón de 28 años con TEC", ["Fractura de base de cráneo", "Midriasis derecha · ojo abajo y afuera"]),
  {"rotulo": "Par y hallazgos", "eje_x": "Rasgo", "eje_y": "Par",
   "cols": ["Posición del ojo", "Pupila"], "rows": ["III", "IV", "VI"], "caso": (0, 0),
   "cells": [[("ABAJO Y AFUERA", ["Ptosis"]), ("Midriasis", [])],
             [("Arriba", ["Diplopía al bajar"]), ("Normal", [])],
             [("Adentro", ["No abduce"]), ("Normal", [])]]},
  ["Midriasis unilateral en TEC: descartar herniación.",
   "TC urgente y valorar neurocirugía.",
   "Diabetes: III par con pupila respetada."],
  HARRISON + " · " + ATLS)

# OFT-055 · termómetro
V("termometro", "OFT-055", "soldador-esquirla-corneal-retiro-antibiotico", "Cuerpo extraño ocular",
  "OFTALMOLOGÍA ENAM: CUERPO EXTRAÑO CORNEAL", "OFTALMOLOGÍA",
  ("Cuerpo extraño corneal", ["Superficial: retirar con anestesia tópica",
   "Luego antibiótico tópico; si hay perforación, no retirar"]),
  ("Soldador de 23 años", ["Sensación de cuerpo extraño en el ojo derecho", "Esquirla corneal · visión conservada"]),
  {"rotulo": "Profundidad",
   "niveles": [("Suelto", "Conjuntiva", ["Lavado"]),
               ("Superficial", "Epitelio corneal", ["RETIRAR", "Aguja o fresa"]),
               ("Óxido", "Anillo", ["Fresa"]),
               ("Penetrante", "Intraocular", ["No retirar, derivar"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta en este caso", "paso_label": "PASO",
   "pasos": [(1, "Retirar el cuerpo extraño", ["Anestesia tópica"], True),
             (2, "Antibiótico tópico", ["Previene queratitis"], False),
             (3, "Control en 24 horas", ["Epitelización"], False)]},
  ["Usar lentes protectores al soldar.",
   "Evertir el párpado para buscar más partículas.",
   "No dar anestésico tópico para casa."],
  "AAO – Corneal foreign body (EyeWiki 2024)")

# SP-191 · embudo
V("embudo", "SP-191", "leishmaniasis-ocupacion-forma-clinica-chi-cuadrado", "Elegir la prueba estadística",
  "SALUD PÚBLICA ENAM: CHI-CUADRADO", "SALUD PÚBLICA",
  ("Pruebas de asociación", ["Depende del tipo de variables",
   "Dos variables categóricas: chi-cuadrado"]),
  ("Estudio de leishmaniasis (1200 pacientes)", ["Ocupación y forma clínica", "Ambas son categóricas"]),
  {"rotulo": "Embudo de pruebas",
   "inicio": "Dos variables a comparar",
   "candidatos": ["Chi-cuadrado", "t de Student", "ANOVA", "Regresión logística"],
   "pasos": [("Sin variables numéricas", ["t de Student", "ANOVA"]),
             ("Solo asociación bivariada", ["Regresión logística"])],
   "final": ("CHI-CUADRADO", ["Tabla de contingencia", "Frecuencias observadas y esperadas"]),
   "nota": "Si alguna frecuencia esperada es < 5: prueba exacta de Fisher."},
  ["t de Student: compara dos medias.",
   "ANOVA: compara tres o más medias.",
   "Regresión logística: varias variables a la vez."],
  GORDIS)

# INF-114 · embudo
V("embudo", "INF-114", "contacto-bacilifero-ppd-22-rx-normal-isoniazida", "Contacto con PPD positivo",
  "INFECTOLOGÍA ENAM: INFECCIÓN TUBERCULOSA LATENTE", "INFECTOLOGÍA",
  ("Infección tuberculosa latente", ["Infectado sin enfermedad: PPD positivo, Rx normal",
   "Terapia preventiva para evitar la TB activa"]),
  ("Varón de 40 años, contacto domiciliario", ["Asintomático · PPD 22 mm", "Rx normal · se descartó TB activa"]),
  {"rotulo": "Embudo de conducta",
   "inicio": "Contacto de TB bacilífera",
   "candidatos": ["Terapia preventiva", "Esquema completo", "Repetir PPD", "Nada"],
   "pasos": [("Sin enfermedad activa", ["Esquema completo"]),
             ("PPD ya es positivo (22 mm)", ["Repetir PPD", "Nada"])],
   "final": ("TERAPIA PREVENTIVA", ["Isoniazida 6 meses", "O rifapentina + isoniazida (3HP)"]),
   "nota": "Antes de iniciar se descarta siempre la TB activa."},
  ["Controlar la función hepática en mayores.",
   "Piridoxina con isoniazida.",
   "Educar sobre síntomas de TB."],
  "MINSA – NTS 200 (2023) · OMS – TB preventive treatment (2024)")

# END-068 · fases
V("fases", "END-068", "graves-tiamazol-fiebre-odinofagia-hemograma-urgente", "Riesgo de agranulocitosis",
  "ENDOCRINOLOGÍA ENAM: AGRANULOCITOSIS POR ANTITIROIDEOS", "ENDOCRINOLOGÍA",
  ("Agranulocitosis por antitiroideos", ["Rara pero grave; sobre todo en los primeros 3 meses",
   "Fiebre y odinofagia: suspender y pedir hemograma urgente"]),
  ("Varón de 34 años con Graves", ["Tratado con tiamazol y propranolol", "Fiebre alta y odinofagia intensa"]),
  {"rotulo": "Tratamiento con tiamazol", "ans": 2,
   "fases": [("Inicio", "Semana 0", "Tiamazol", ["Advertir síntomas"]),
             ("1-3 meses", "Mayor riesgo", "Vigilar", ["Fiebre, dolor de garganta"]),
             ("Síntomas", "Fiebre", "HEMOGRAMA URGENTE", ["Suspender tiamazol"])],
   "curvas": [("Riesgo", ROSE, [0.2, 0.7, 0.9, 0.6, 0.4, 0.3, 0.3])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("Hemograma urgente", True), ("Azitromicina", False), ("Ibuprofeno", False), ("Cultivo faríngeo", False)]},
  ["Neutrófilos < 500: hospitalizar y dar antibióticos.",
   "No volver a usar antitiroideos.",
   "Alternativa: yodo radiactivo o cirugía."],
  "ATA – Hyperthyroidism guidelines (2016) · " + HARRISON)

# SP-192 · termómetro
V("termometro", "SP-192", "medico-obliga-grabar-agradecimientos-consejo-regional", "Ante la falta ética de un colega",
  "SALUD PÚBLICA ENAM: ÉTICA PROFESIONAL", "SALUD PÚBLICA",
  ("Deber de informar faltas éticas", ["Si el colega persiste pese a la advertencia",
   "Se notifica al Consejo Regional del Colegio Médico"]),
  ("Médico que obliga a grabar mensajes", ["Publica agradecimientos de pacientes", "Sigue haciéndolo pese a ser advertido"]),
  {"rotulo": "Escalones de la acción",
   "niveles": [("1", "Advertir", ["Conversar con el colega"]),
               ("2", "Persiste", ["Falta reiterada"]),
               ("3", "Notificar", ["CONSEJO REGIONAL", "Del Colegio Médico"])],
   "caso_nivel": 2, "ruta_titulo": "Qué hacer en este caso", "paso_label": "PASO",
   "pasos": [(1, "Notificar al Consejo Regional", ["Por escrito"], True),
             (2, "Proteger a los pacientes", ["Confidencialidad"], False),
             (3, "No trasladar el problema", ["Ni ignorarlo"], False)]},
  ["Usar la imagen del paciente para publicidad es falta ética.",
   "La indiferencia también es complicidad.",
   "No delegar la denuncia en los pacientes."],
  CMP)

# PED-241 · fases
V("fases", "PED-241", "polihidramnios-hospital-nivel-iii-atresia-esofago", "Polihidramnios y deglución fetal",
  "PEDIATRÍA ENAM: POLIHIDRAMNIOS", "PEDIATRÍA",
  ("Polihidramnios", ["El feto regula el líquido: orina y lo traga",
   "Si no puede tragar (atresia de esófago) el líquido se acumula"]),
  ("Primigesta con polihidramnios", ["Referida a un hospital nivel III", "¿Qué descartar en el neonato?"]),
  {"rotulo": "Circuito del líquido amniótico", "ans": 2,
   "fases": [("Producción", "Orina fetal", "Riñón fetal", ["Agenesia: oligohidramnios"]),
             ("Recambio", "Deglución", "Esófago", ["Absorbe el líquido"]),
             ("Falla", "No traga", "ATRESIA DE ESÓFAGO", ["Polihidramnios", "Sonda al nacer"])],
   "curvas": [("Líquido amniótico", SKY, [0.4, 0.5, 0.55, 0.6, 0.7, 0.85, 0.95])],
   "chips_titulo": "Descartar · marcado el correcto",
   "chips": [("Atresia de esófago", True), ("Potter", False), ("Hipoplasia pulmonar", False), ("Riñón en herradura", False)]},
  ["Potter e hipoplasia pulmonar van con oligohidramnios.",
   "Pasar sonda orogástrica al nacer.",
   "Otras causas: diabetes, anomalías del SNC."],
  WILLIAMS + " · " + NELSON)
