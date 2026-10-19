"""Ciencias Básicas · parte I (CB-413 a CB-452)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-413 · embudo
V("embudo", "CB-413", "lumbalgia-aine-cuarto-dia-melena-indometacina", "Fármaco que causa melena",
  "CIENCIAS BÁSICAS ENAM: GASTROTOXICIDAD", CB,
  ("Úlcera por AINE", ["Inhiben las prostaglandinas protectoras",
   "La indometacina es de las más gastrotóxicas"]),
  ("Paciente de 58 años con lumbociática", ["Toma un fármaco 3 veces al día", "Al 4.º día: epigastralgia y melena"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco fármacos",
   "candidatos": ["Indometacina", "Gabapentina", "Orfenadrina", "Paracetamol"],
   "pasos": [("Es un AINE", ["Gabapentina", "Orfenadrina"]),
             ("Inhibe la COX-1 gástrica", ["Paracetamol"])],
   "final": ("INDOMETACINA", ["Úlcera y sangrado digestivo", "Melena"]),
   "nota": "Vitamina B12: sin efecto gástrico."},
  ["Riesgo: > 65 años, úlcera previa.",
   "Con corticoides o anticoagulantes.",
   "Prevención: IBP o coxib."],
  GOODMAN)

# CB-414 · termómetro
V("termometro", "CB-414", "analgesicos-aumentan-umbral-doloroso", "Umbral del dolor",
  "CIENCIAS BÁSICAS ENAM: ANALGESIA", CB,
  ("Umbral doloroso", ["Estímulo mínimo que se percibe como dolor",
   "Los analgésicos lo elevan"]),
  ("Pregunta de farmacología", ["¿Qué permiten los analgésicos?"]),
  {"rotulo": "Umbral según la situación",
   "niveles": [("Muy bajo", "Alodinia", ["Duele el tacto"]),
               ("Bajo", "Hiperalgesia", ["Inflamación"]),
               ("Alto", "ANALGESIA", ["Umbral aumentado"]),
               ("Sin sensación", "Anestesia", ["Bloqueo total"])],
   "caso_nivel": 2, "ruta_titulo": "Cómo lo elevan", "paso_label": "PASO",
   "pasos": [(1, "AINE", ["Menos sensibilización"], True),
             (2, "Opioides", ["Médula y cerebro"], True),
             (3, "Adyuvantes", ["Dolor neuropático"], False)]},
  ["Anestesia subaracnoidea: no es analgésico.",
   "Vías descendentes inhibitorias.",
   "Sensibilización central: baja el umbral."],
  GOODMAN)

# CB-415 · árbol
A("CB-415", "aine-gastropatia-cox1-prostaglandinas-protectoras", "Por qué los AINE dañan el estómago",
  "CIENCIAS BÁSICAS ENAM: GASTROPATÍA POR AINE", CB,
  ("Prostaglandinas gástricas", ["Protegen la mucosa",
   "Los AINE las suprimen"]),
  ("Pregunta de fisiopatología", ["¿Mecanismo de la gastropatía por AINE?"]),
  Q("¿Qué hacen las prostaglandinas E2 e I2?", [
      L("Sin ellas", "MENOS PROTECCIÓN", ["Menos moco y bicarbonato", "Menos flujo mucoso"], path=True),
      L("Además", "Daño tópico", ["AINE ácidos como AAS"])], path=True),
  ("Opciones falsas", [("Dice", True), ("Realidad", False)], [
      ("Bicarbonato", ["Aumenta", "Disminuye"]),
      ("Mucina", ["Aumenta", "Disminuye"])]),
  ["Más úlceras gástricas que duodenales.",
   "Sangrado a veces sin dolor previo.",
   "Misoprostol: análogo de PGE1."],
  GOODMAN)

# CB-416 · puntaje
V("puntaje", "CB-416", "aspirina-antiagregacion-irreversible-vida-plaqueta", "Duración del efecto de la aspirina",
  "CIENCIAS BÁSICAS ENAM: ANTIAGREGANTES", CB,
  ("Aspirina", ["Acetila la COX-1 plaquetaria de forma irreversible",
   "La plaqueta no fabrica nueva enzima"]),
  ("Pregunta de farmacología", ["¿Cuánto persiste el efecto antiplaquetario?"]),
  {"rotulo": "Vida de la plaqueta", "escala": "Días", "total": 10, "max": 14,
   "total_label": "Efecto antiagregante",
   "interpreta": "8-10 días",
   "items": [("Acetila COX-1", "Irreversible", True), ("Plaqueta sin núcleo", "No repone", True), ("Vida plaquetaria", "7-10 días", True)],
   "bandas": [("Horas", "Otros AINE", "Reversibles", False),
              ("8-10 días", "Aspirina", "Toda la vida plaquetaria", True),
              ("7 días", "Suspender", "Antes de cirugía", False)]},
  ["Dosis antiagregante: 75-100 mg.",
   "Valorar riesgo trombótico al suspender.",
   "Bloquea el tromboxano A2."],
  GOODMAN)

# CB-417 · matriz
V("matriz", "CB-417", "heparina-no-fraccionada-ttpa-monitoreo-tvp", "Control de los anticoagulantes",
  "CIENCIAS BÁSICAS ENAM: ANTICOAGULACIÓN", CB,
  ("Monitoreo de la anticoagulación", ["Cada fármaco se controla con una prueba",
   "La heparina no fraccionada: TTPA"]),
  ("Paciente con TVP recurrente", ["Recibe heparina no fraccionada", "¿Qué examen se usa para el control?"]),
  {"rotulo": "Prueba y antídoto", "eje_x": "Dato", "eje_y": "Fármaco",
   "cols": ["Control", "Antídoto"], "rows": ["Heparina no fracc.", "Bajo peso molec.", "Warfarina"], "caso": (0, 0),
   "cells": [[("TTPA", ["1,5-2,5 veces"]), ("Protamina", [])],
             [("Anti-Xa", ["Si hace falta"]), ("Protamina parcial", [])],
             [("INR", []), ("Vitamina K", ["Complejo protrombínico"])]]},
  ["Medir TTPA a las 6 horas.",
   "Vigilar plaquetas: días 5-10.",
   "Trombocitopenia inducida por heparina."],
  GOODMAN)

# CB-418 · árbol
A("CB-418", "fibrilacion-auricular-warfarina-equimosis-inr", "Control de la warfarina",
  "CIENCIAS BÁSICAS ENAM: WARFARINA", CB,
  ("Warfarina", ["Antagonista de la vitamina K",
   "Baja primero el factor VII"]),
  ("Paciente de 65 años con FA", ["Warfarina desde hace 2 meses", "Consulta por equimosis"]),
  Q("¿Qué anticoagulante recibe?", [
      L("Warfarina", "TIEMPO DE PROTROMBINA", ["INR: meta 2-3"], path=True),
      L("Heparina", "TTPA", ["O anti-Xa"])], path=True),
  ("INR alto con sangrado", [("Situación", True), ("Conducta", False)], [
      ("Leve", ["Equimosis", "Suspender dosis"]),
      ("Grave", ["Hemorragia", "Vitamina K + CCP"])]),
  ["Prótesis mitral mecánica: INR 2,5-3,5.",
   "Antibióticos y amiodarona la potencian.",
   "Verduras verdes la reducen."],
  "CHEST – Antithrombotic therapy guidelines (2021)")

# CB-419 · tarjetas
V("tarjetas", "CB-419", "prometazina-antihistaminico-primera-generacion-sedante", "Generaciones de antihistamínicos",
  "CIENCIAS BÁSICAS ENAM: ANTIHISTAMÍNICOS", CB,
  ("Antihistamínicos H1", ["1.ª generación: cruzan al cerebro, sedan",
   "2.ª generación: poco sedantes"]),
  ("Pregunta de farmacología", ["¿Cuál es de primera generación?"]),
  {"rotulo": "¿Qué generación?", "ans": 0, "cards": [
      {"titulo": "PROMETAZINA", "datos": [
          ("Generación", "Primera", True), ("Sedación", "Marcada", True),
          ("Grupo", "Fenotiazina", True)],
       "pie": "No en < 2 años"},
      {"titulo": "Loratadina", "datos": [
          ("Generación", "Segunda", False), ("Sedación", "Mínima", False),
          ("Uso", "Rinitis", False)],
       "pie": "Una vez al día"},
      {"titulo": "Astemizol", "datos": [
          ("Generación", "Segunda", False), ("Riesgo", "QT largo", False),
          ("Estado", "Retirado", False)],
       "pie": "Igual que terfenadina"},
      {"titulo": "Levocabastina", "datos": [
          ("Generación", "Segunda", False), ("Vía", "Tópica", False),
          ("Uso", "Ojo, nariz", False)],
       "pie": "Gotas"}]},
  ["Clorfenamina, difenhidramina: 1.ª.",
   "Efecto anticolinérgico en la 1.ª.",
   "Cetirizina, fexofenadina: 2.ª."],
  GOODMAN)

# CB-420 · matriz
V("matriz", "CB-420", "succinilcolina-despolarizante-pseudocolinesterasa", "Relajantes neuromusculares",
  "CIENCIAS BÁSICAS ENAM: RELAJANTES MUSCULARES", CB,
  ("Relajantes neuromusculares", ["Despolarizante: succinilcolina",
   "No despolarizantes: rocuronio, atracurio"]),
  ("Pregunta de farmacología", ["Bloqueo muy rápido, hidrólisis por colinesterasa"]),
  {"rotulo": "Tipo y eliminación", "eje_x": "Dato", "eje_y": "Fármaco",
   "cols": ["Tipo", "Eliminación"], "rows": ["Succinilcolina", "Rocuronio", "Atracurio"], "caso": (0, 1),
   "cells": [[("Despolarizante", ["Fasciculaciones"]), ("PSEUDOCOLINESTERASA", ["5-10 minutos"])],
             [("No despolarizante", []), ("Hígado", ["Sugammadex"])],
             [("No despolarizante", []), ("Hofmann", ["Espontánea"])]]},
  ["Hiperpotasemia en quemados.",
   "Hipertermia maligna: dantroleno.",
   "Pseudocolinesterasa atípica: parálisis larga."],
  "Miller. Anestesia 9.ª ed. (2020)")

# CB-421 · radial
V("radial", "CB-421", "misoprostol-prevencion-dano-mucoso-aine", "Misoprostol",
  "CIENCIAS BÁSICAS ENAM: PROSTAGLANDINAS", CB,
  ("Misoprostol", ["Análogo sintético de la prostaglandina E1",
   "Reemplaza a las prostaglandinas que suprimen los AINE"]),
  ("Pregunta de farmacología", ["¿Para qué está mejor indicado?"]),
  {"rotulo": "Mapa del tema", "centro": "MISOPROSTOL", "centro_sub": "PGE1", "ans": 0,
   "items": [("PREVENIR", ["Úlcera por AINE"]),
             ("Obstetricia", ["Maduración cervical", "Hemorragia posparto"]),
             ("Efecto adverso", ["Diarrea"]),
             ("Contraindicado", ["Embarazo"]),
             ("Alternativa", ["IBP"])],
   "ruta": ["AINE", "Menos prostaglandinas", "Misoprostol", "MUCOSA PROTEGIDA"]},
  ["No es de elección en Zollinger-Ellison.",
   "No erradica H. pylori.",
   "Hoy se prefieren los IBP."],
  GOODMAN)

# CB-422 · tarjetas
V("tarjetas", "CB-422", "giardiasis-metronidazol-tinidazol-tratamiento", "Tratamiento de parasitosis intestinales",
  "CIENCIAS BÁSICAS ENAM: ANTIPARASITARIOS", CB,
  ("Antiparasitarios", ["Protozoos: nitroimidazoles",
   "Helmintos: benzimidazoles"]),
  ("Pregunta de farmacología", ["¿Tratamiento de elección de la giardiasis?"]),
  {"rotulo": "¿Para qué parásito?", "ans": 0, "cards": [
      {"titulo": "METRONIDAZOL", "datos": [
          ("Parásito", "Giardia", True), ("Duración", "5-7 días", True),
          ("Alternativa", "Tinidazol", True)],
       "pie": "Nitazoxanida también"},
      {"titulo": "Albendazol", "datos": [
          ("Parásito", "Helmintos", False), ("Ejemplo", "Ascaris", False),
          ("Giardia", "Eficacia parcial", False)],
       "pie": "Benzimidazol"},
      {"titulo": "Mebendazol", "datos": [
          ("Parásito", "Helmintos", False), ("Ejemplo", "Oxiuros", False),
          ("Giardia", "No", False)],
       "pie": "Benzimidazol"},
      {"titulo": "Fluconazol", "datos": [
          ("Grupo", "Antimicótico", False), ("Uso", "Candida", False),
          ("Giardia", "No", False)],
       "pie": "No antiparasitario"}]},
  ["Hervir o clorar el agua.",
   "Diarrea grasosa y distensión.",
   "Tiabendazol: helmintos."],
  BOTERO)

# CB-423 · embudo
V("embudo", "CB-423", "nina-broncorrea-sin-mejoria-nebulizaciones-miosis-colinesterasa", "Falsa crisis asmática",
  "CIENCIAS BÁSICAS ENAM: SÍNDROME COLINÉRGICO", CB,
  ("Broncorrea que no responde", ["No es asma: es exceso de acetilcolina",
   "Miosis y fasciculaciones lo delatan"]),
  ("Niña de 3 años", ["Secreciones bronquiales, sudoración, somnolencia", "Miosis y fasciculaciones"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dificultad respiratoria",
   "candidatos": ["Inhibidor colinesterasa", "Bronquiolitis", "Anafilaxia", "Atropínicos"],
   "pasos": [("Hay miosis y fasciculaciones", ["Bronquiolitis", "Anafilaxia"]),
             ("Hay secreciones, no sequedad", ["Atropínicos"])],
   "final": ("INHIBIDOR DE COLINESTERASA", ["Organofosforado o carbamato", "Atropina hasta secar"]),
   "nota": "Atropínicos: midriasis y piel seca."},
  ["No responde a beta-2 ni ipratropio.",
   "Descontaminar piel y ropa.",
   "Pralidoxima si es organofosforado."],
  TOXI)

# CB-424 · termómetro
V("termometro", "CB-424", "corticoides-cronicos-osteoporosis-colapso-vertebral", "Efectos adversos de los corticoides",
  "CIENCIAS BÁSICAS ENAM: CORTICOTERAPIA CRÓNICA", CB,
  ("Corticoides prolongados", ["Muchos efectos adversos",
   "La osteoporosis es de los más frecuentes"]),
  ("Pregunta de farmacología", ["¿Efecto adverso más frecuente a largo plazo?"]),
  {"rotulo": "Frecuencia",
   "niveles": [("Rara", "Queratitis", ["Poco común"]),
               ("Poco frecuente", "Convulsiones", ["Excepcional"]),
               ("Frecuente", "Psicosis, HDA", ["Dosis altas"]),
               ("Muy frecuente", "OSTEOPOROSIS", ["Fracturas vertebrales"])],
   "caso_nivel": 3, "ruta_titulo": "Prevención", "paso_label": "PASO",
   "pasos": [(1, "Calcio y vitamina D", ["Desde el inicio"], True),
             (2, "Densitometría", ["Basal"], False),
             (3, "Bisfosfonatos", ["Según riesgo"], True)]},
  ["≥ 2,5 mg/día de prednisona por > 3 meses.",
   "Afecta el hueso trabecular.",
   "Fracturas aun con osteopenia."],
  "ACR – Glucocorticoid-induced osteoporosis (2022)")

# CB-425 · termómetro
V("termometro", "CB-425", "fluoxetina-menor-sedacion-antidepresivos", "Sedación de los antidepresivos",
  "CIENCIAS BÁSICAS ENAM: ANTIDEPRESIVOS", CB,
  ("Sedación antidepresiva", ["Depende del bloqueo H1, muscarínico y alfa-1",
   "Los ISRS casi no sedan"]),
  ("Pregunta de farmacología", ["¿Cuál tiene menor efecto sedante?"]),
  {"rotulo": "Grado de sedación",
   "niveles": [("Mínima", "FLUOXETINA", ["Activadora", "Tomar de mañana"]),
               ("Moderada", "Clomipramina", ["Tricíclico"]),
               ("Alta", "Trazodona", ["Uso como hipnótico"]),
               ("Muy alta", "Amitriptilina", ["Doxepina"])],
   "caso_nivel": 0, "ruta_titulo": "Por qué seda poco", "paso_label": "PASO",
   "pasos": [(1, "ISRS", ["Selectivo"], True),
             (2, "Sin bloqueo H1", ["Ni muscarínico"], True),
             (3, "Puede dar insomnio", ["Ansiedad inicial"], False)]},
  ["Vida media larga: poca retirada.",
   "Inhibe CYP2D6.",
   "Tricíclicos: cardiotóxicos."],
  GOODMAN)

# CB-426 · radial
V("radial", "CB-426", "pamoato-pirantel-colinesterasa-paralisis-espastica", "Mecanismo de los antihelmínticos",
  "CIENCIAS BÁSICAS ENAM: ANTIHELMÍNTICOS", CB,
  ("Pamoato de pirantel", ["Actúa en la unión neuromuscular del gusano",
   "Produce parálisis espástica"]),
  ("Pregunta de farmacología", ["¿Qué inhibe el pamoato de pirantel?"]),
  {"rotulo": "Mapa del tema", "centro": "HELMINTOS", "centro_sub": "Fármacos", "ans": 0,
   "items": [("PIRANTEL", ["Inhibe colinesterasa", "Agonista nicotínico"]),
             ("Benzimidazoles", ["Tubulina"]),
             ("Ivermectina", ["Canales de cloro"]),
             ("Piperazina", ["Parálisis flácida"]),
             ("Praziquantel", ["Calcio: cestodos"])],
   "ruta": ["Pirantel", "Despolariza", "Parálisis espástica", "SE EXPULSA"]},
  ["Útil en Ascaris, oxiuros, uncinarias.",
   "No combinar con piperazina.",
   "Repetir a las 2 semanas en oxiuros."],
  BOTERO)

# CB-427 · matriz
V("matriz", "CB-427", "monoxido-carbono-hipoxia-citotoxica-carboxihemoglobina", "Tipos de hipoxia",
  "CIENCIAS BÁSICAS ENAM: HIPOXIA", CB,
  ("Hipoxia tisular", ["Por poco oxígeno, poco transporte o poco uso",
   "El CO afecta transporte y respiración celular"]),
  ("Pregunta de fisiopatología", ["¿Qué causa tiene componente citotóxico?"]),
  {"rotulo": "Tipo y ejemplo", "eje_x": "Dato", "eje_y": "Tipo",
   "cols": ["Mecanismo", "Ejemplo"], "rows": ["Hipoxémica", "Isquémica", "Citotóxica"], "caso": (2, 1),
   "cells": [[("PaO2 baja", []), ("Inmersión", [])],
             [("Flujo bajo", []), ("Shock, paro, infarto", [])],
             [("Bloquea citocromo", []), ("MONÓXIDO", ["Y cianuro"])]]},
  ["Oxímetro falsamente normal con CO.",
   "Oxígeno 100 % o hiperbárico.",
   "Daño neurológico tardío."],
  HARRISON)

# CB-428 · tarjetas
V("tarjetas", "CB-428", "cisplatino-alquilante-platino-enlaces-cruzados", "Clases de antineoplásicos",
  "CIENCIAS BÁSICAS ENAM: QUIMIOTERAPIA", CB,
  ("Antineoplásicos", ["Alquilantes y platinos dañan el ADN",
   "Otros grupos tienen blancos distintos"]),
  ("Pregunta de farmacología", ["¿Cuál es alquilante?"]),
  {"rotulo": "¿Qué grupo?", "ans": 0, "cards": [
      {"titulo": "CISPLATINO", "datos": [
          ("Grupo", "Platino (alquilante)", True), ("Acción", "Enlaces cruzados", True),
          ("Toxicidad", "Riñón, oído", True)],
       "pie": "Muy emetógeno"},
      {"titulo": "Doxorrubicina", "datos": [
          ("Grupo", "Antraciclina", False), ("Acción", "Topoisomerasa II", False),
          ("Toxicidad", "Cardíaca", False)],
       "pie": "Se intercala"},
      {"titulo": "Citarabina", "datos": [
          ("Grupo", "Antimetabolito", False), ("Fase", "S", False),
          ("Uso", "Leucemias", False)],
       "pie": "Análogo de pirimidina"},
      {"titulo": "Actinomicina D", "datos": [
          ("Grupo", "Antibiótico", False), ("Acción", "Inhibe ARN", False),
          ("Uso", "Wilms", False)],
       "pie": "Antitumoral"}]},
  ["Hidratar para prevenir nefrotoxicidad.",
   "Carboplatino: menos nefrotóxico.",
   "Asparaginasa: enzima."],
  GOODMAN)

# CB-429 · fases
V("fases", "CB-429", "ciclofosfamida-profarmaco-mostaza-alquilacion-adn", "Activación de la ciclofosfamida",
  "CIENCIAS BÁSICAS ENAM: ALQUILANTES", CB,
  ("Ciclofosfamida", ["Mostaza nitrogenada",
   "Profármaco activado en el hígado"]),
  ("Pregunta de farmacología", ["¿Qué alquilante actúa directamente sobre el ADN?"]),
  {"rotulo": "De profármaco a efecto", "ans": 2,
   "fases": [("Hígado", "CYP450", "Activación", ["4-hidroxi"]),
             ("Metabolitos", "Plasma", "Mostaza", ["Y acroleína"]),
             ("Célula", "ADN", "ALQUILACIÓN", ["Guanina N7", "Enlaces cruzados"])],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Ciclofosfamida", True), ("6-mercaptopurina", False), ("Citarabina", False), ("Vincristina", False)]},
  ["Acroleína: cistitis hemorrágica.",
   "Prevención: mesna e hidratación.",
   "Uso: linfomas, nefritis lúpica."],
  GOODMAN)

# CB-430 · radial
V("radial", "CB-430", "antidepresivos-dolor-neuropatico-diabetico", "Tratamiento del dolor neuropático",
  "CIENCIAS BÁSICAS ENAM: DOLOR NEUROPÁTICO", CB,
  ("Dolor neuropático", ["Responde a antidepresivos y gabapentinoides",
   "No a los analgésicos comunes"]),
  ("Pregunta de farmacología", ["¿En qué dolor sirven los antidepresivos?"]),
  {"rotulo": "Mapa del tema", "centro": "NEUROPÁTICO", "centro_sub": "Dolor", "ans": 0,
   "items": [("NEUROPATÍA DIABÉTICA", ["Evidencia clara"]),
             ("Tricíclicos", ["Amitriptilina"]),
             ("Duales", ["Duloxetina"]),
             ("Gabapentinoides", ["Pregabalina"]),
             ("No útiles", ["Lumbalgia aguda", "Esguince, desgarro"])],
   "ruta": ["Neuropatía", "Antidepresivo", "Vía descendente", "MENOS DOLOR"]},
  ["Dosis menores que las antidepresivas.",
   "Neuralgia postherpética: también.",
   "Adultos mayores: evitar amitriptilina."],
  "NICE – Neuropathic pain (2020)")

# CB-431 · árbol
A("CB-431", "sobredosis-clonazepam-flumazenilo-cautela", "Sobredosis de benzodiacepinas",
  "CIENCIAS BÁSICAS ENAM: BENZODIACEPINAS", CB,
  ("Benzodiacepinas", ["Sobredosis aislada rara vez es mortal",
   "El flumazenilo es su antagonista"]),
  ("Mujer de 20 años", ["Ingiere 30 tabletas de clonazepam 2 mg", "¿Antídoto de elección?"]),
  Q("¿Dependencia o mezcla con tricíclicos?", [
      L("No", "FLUMAZENILO", ["Antagonista GABA-A", "Dosis pequeñas"], path=True),
      L("Sí", "Solo soporte", ["Riesgo de convulsiones"])], path=True),
  ("Cuidado con el flumazenilo", [("Riesgo", True), ("Motivo", False)], [
      ("Convulsiones", ["Abstinencia", "Tricíclicos"]),
      ("Resedación", ["Dura poco", "Vigilar horas"])]),
  ["Naloxona: para opioides.",
   "Lo principal: vía aérea.",
   "Carbón solo si es reciente."],
  TOXI)

# CB-432 · embudo
V("embudo", "CB-432", "carbamazepina-estructura-triciclica-anticonvulsivante", "Anticonvulsivante tricíclico",
  "CIENCIAS BÁSICAS ENAM: CARBAMAZEPINA", CB,
  ("Carbamazepina", ["Estructura tricíclica (iminoestilbeno)",
   "Parecida a la imipramina"]),
  ("Pregunta de farmacología", ["¿Qué anticonvulsivante se parece a los tricíclicos?"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco anticonvulsivantes",
   "candidatos": ["Carbamazepina", "Valproato", "Fenitoína", "Gabapentina"],
   "pasos": [("Tiene tres anillos", ["Valproato", "Gabapentina"]),
             ("Iminoestilbeno", ["Fenitoína"])],
   "final": ("CARBAMAZEPINA", ["Bloquea canales de sodio", "Neuralgia del trigémino"]),
   "nota": "Fenitoína: hidantoína, no tricíclica."},
  ["Hiponatremia por efecto SIADH.",
   "Agranulocitosis.",
   "Autoinducción enzimática."],
  GOODMAN)

# CB-433 · tarjetas
V("tarjetas", "CB-433", "duloxetina-irsn-neuropatia-diabetica", "Fármacos para la neuropatía diabética",
  "CIENCIAS BÁSICAS ENAM: NEUROPATÍA DIABÉTICA", CB,
  ("Neuropatía diabética dolorosa", ["Varias familias de fármacos",
   "La duloxetina es un IRSN"]),
  ("Pregunta de farmacología", ["¿Cuál inhibe la recaptación de serotonina", "y noradrenalina?"]),
  {"rotulo": "¿Cómo actúa?", "ans": 0, "cards": [
      {"titulo": "DULOXETINA", "datos": [
          ("Grupo", "IRSN", True), ("Mecanismo", "5-HT y NA", True),
          ("Dosis", "60 mg/día", True)],
       "pie": "También fibromialgia"},
      {"titulo": "Pregabalina", "datos": [
          ("Grupo", "Gabapentinoide", False), ("Mecanismo", "Alfa-2-delta", False),
          ("Efecto", "Mareo, edema", False)],
       "pie": "Canales de calcio"},
      {"titulo": "Desipramina", "datos": [
          ("Grupo", "Tricíclico", False), ("Mecanismo", "Sobre todo NA", False),
          ("Efecto", "Anticolinérgico", False)],
       "pie": "No selectivo"},
      {"titulo": "Mexiletina", "datos": [
          ("Grupo", "Antiarrítmico IB", False), ("Mecanismo", "Canales de Na", False),
          ("Uso", "Segunda línea", False)],
       "pie": "Poco usada"}]},
  ["Evitar en insuficiencia hepática.",
   "Náuseas al inicio.",
   "Venlafaxina: otro IRSN."],
  GOODMAN)

# CB-434 · matriz
V("matriz", "CB-434", "lupus-corticoides-dosis-altas-linfopenia-t", "Efectos de los corticoides en dosis altas",
  "CIENCIAS BÁSICAS ENAM: GLUCOCORTICOIDES", CB,
  ("Glucocorticoides", ["Inmunosupresores y antiinflamatorios",
   "Cambian el metabolismo"]),
  ("Mujer de 25 años con lupus", ["Artralgias, orina espumosa, eritema malar", "Corticoide oral en dosis altas"]),
  {"rotulo": "Efecto esperado", "eje_x": "Dato", "eje_y": "Proceso",
   "cols": ["Efecto real", "Opción del caso"], "rows": ["Linfocitos T", "Gluconeogénesis", "Permeabilidad capilar"], "caso": (0, 0),
   "cells": [[("DISMINUYEN", ["Linfopenia"]), ("Correcta", [])],
             [("Aumenta", ["Hiperglucemia"]), ("Falsa: dice baja", [])],
             [("Disminuye", []), ("Falsa: dice sube", [])]]},
  ["Inhiben IL-1, IL-2 y TNF.",
   "Aumentan neutrófilos circulantes.",
   "Nefritis lúpica: más micofenolato."],
  GOODMAN)

# CB-435 · puntaje
V("puntaje", "CB-435", "lidocaina-duracion-60-180-minutos-adrenalina", "Duración de los anestésicos locales",
  "CIENCIAS BÁSICAS ENAM: ANESTÉSICOS LOCALES", CB,
  ("Anestésicos locales", ["Lidocaína: inicio rápido, duración intermedia",
   "La adrenalina prolonga el efecto"]),
  ("Pregunta de farmacología", ["¿Cuánto dura la lidocaína?"]),
  {"rotulo": "Duración", "escala": "Minutos", "total": 120, "max": 480,
   "total_label": "Lidocaína sola",
   "interpreta": "60-180 minutos",
   "items": [("Inicio", "2-5 min", False), ("Sin adrenalina", "60-120", True), ("Con adrenalina", "Hasta 180+", True)],
   "bandas": [("30-60", "Procaína", "Acción corta", False),
              ("60-180", "Lidocaína", "Intermedia", True),
              ("240-480", "Bupivacaína", "Larga", False)]},
  ["Dosis máxima: 4,5 mg/kg; 7 con adrenalina.",
   "Toxicidad: sabor metálico, convulsiones.",
   "Rescate: emulsión lipídica 20 %."],
  "Miller. Anestesia 9.ª ed. (2020)")

# CB-436 · embudo
V("embudo", "CB-436", "erc-infecciones-urinarias-neuropatia-nitrofurantoina", "Neuropatía por fármacos",
  "CIENCIAS BÁSICAS ENAM: NITROFURANTOÍNA", CB,
  ("Nitrofurantoína", ["Profilaxis de infecciones urinarias",
   "Se acumula en la insuficiencia renal"]),
  ("Mujer de 50 años con ERC estadio III", ["Infecciones urinarias a repetición", "Desarrolla neuropatía periférica"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Fármacos de la paciente",
   "candidatos": ["Nitrofurantoína", "Tiamazol", "Enalapril", "Levotiroxina"],
   "pasos": [("Causa neuropatía", ["Enalapril", "Levotiroxina"]),
             ("Se acumula en ERC", ["Tiamazol"])],
   "final": ("NITROFURANTOÍNA", ["Polineuropatía sensitivomotora", "Evitar si ClCr < 30-45"]),
   "nota": "Tiamazol: agranulocitosis."},
  ["También fibrosis pulmonar.",
   "Hemólisis en déficit de G6PD.",
   "En ERC no llega a la orina."],
  GOODMAN)

# CB-437 · termómetro
V("termometro", "CB-437", "carbamazepina-oxcarbazepina-hiponatremia-siadh", "Anticonvulsivantes e hiponatremia",
  "CIENCIAS BÁSICAS ENAM: HIPONATREMIA POR FÁRMACOS", CB,
  ("Hiponatremia por anticonvulsivantes", ["Efecto parecido al SIADH",
   "Carbamazepina y oxcarbazepina"]),
  ("Pregunta de farmacología", ["¿Qué anticonvulsivante produce hiponatremia?"]),
  {"rotulo": "Riesgo de hiponatremia",
   "niveles": [("Bajo", "Lamotrigina", ["Topiramato"]),
               ("Bajo", "Fenitoína", ["Fenobarbital"]),
               ("Alto", "CARBAMAZEPINA", ["Tipo SIADH"]),
               ("Muy alto", "Oxcarbazepina", ["La más frecuente"])],
   "caso_nivel": 2, "ruta_titulo": "Vigilancia", "paso_label": "PASO",
   "pasos": [(1, "Sodio basal", ["Antes de iniciar"], True),
             (2, "Adultos mayores", ["Con diuréticos"], False),
             (3, "Síntomas", ["Confusión, crisis"], False)]},
  ["Aumenta la sensibilidad a la ADH.",
   "Suele ser leve.",
   "Topiramato: acidosis y cálculos."],
  GOODMAN)

# CB-438 · fases
V("fases", "CB-438", "metaplasia-cambio-reversible-tipo-celular-adulto", "De la metaplasia al cáncer",
  "CIENCIAS BÁSICAS ENAM: METAPLASIA", CB,
  ("Metaplasia", ["Una célula adulta es reemplazada por otra",
   "Es reversible si cesa el estímulo"]),
  ("Pregunta de patología", ["¿Cómo se llama ese cambio reversible?"]),
  {"rotulo": "Progresión posible", "ans": 0,
   "fases": [("Adaptación", "Reversible", "METAPLASIA", ["Cambia el tipo celular"]),
             ("Premaligno", "Desorden", "Displasia", ["Atipia"]),
             ("Maligno", "Invasión", "Cáncer", ["Si persiste el estímulo"])],
   "chips_titulo": "Nombre · marcado el correcto",
   "chips": [("Metaplasia", True), ("Hiperplasia", False), ("Hipertrofia", False), ("Displasia", False)]},
  ["Barrett: escamoso a cilíndrico.",
   "Fumador: cilíndrico a escamoso.",
   "Células madre se reprograman."],
  ROBBINS)

# CB-439 · radial
V("radial", "CB-439", "adaptaciones-celulares-metaplasia-hipertrofia-atrofia", "Adaptaciones celulares",
  "CIENCIAS BÁSICAS ENAM: ADAPTACIÓN CELULAR", CB,
  ("Adaptación celular", ["Cambios reversibles ante un estrés",
   "Si fallan, hay lesión y muerte"]),
  ("Pregunta de patología", ["¿Qué cambio es una adaptación?"]),
  {"rotulo": "Mapa del tema", "centro": "ADAPTACIÓN", "centro_sub": "Celular", "ans": 0,
   "items": [("METAPLASIA", ["Cambia el tipo"]),
             ("Hipertrofia", ["Más tamaño"]),
             ("Hiperplasia", ["Más número"]),
             ("Atrofia", ["Menos tamaño"]),
             ("No adaptación", ["Apoptosis, autólisis", "Cariorrexis"])],
   "ruta": ["Estrés", "Adaptación", "Si persiste", "LESIÓN"]},
  ["Cariorrexis: núcleo fragmentado.",
   "Autólisis: célula ya muerta.",
   "Apoptosis: muerte programada."],
  ROBBINS)

# CB-440 · embudo
V("embudo", "CB-440", "anaplasia-celulas-malignas-pleomorfismo", "Rasgo de las células malignas",
  "CIENCIAS BÁSICAS ENAM: NEOPLASIA", CB,
  ("Anaplasia", ["Falta de diferenciación",
   "Rasgo típico de malignidad"]),
  ("Pregunta de patología", ["¿Qué alteración caracteriza a las células malignas?"]),
  {"rotulo": "Embudo de alteraciones",
   "inicio": "Cinco alteraciones",
   "candidatos": ["Anaplasia", "Atrofia", "Hiperplasia", "Metaplasia"],
   "pasos": [("No es adaptación normal", ["Atrofia", "Hiperplasia"]),
             ("Pierde la diferenciación", ["Metaplasia"])],
   "final": ("ANAPLASIA", ["Pleomorfismo, mitosis atípicas", "Núcleos hipercromáticos"]),
   "nota": "Más anaplasia: mayor grado y peor pronóstico."},
  ["Relación núcleo/citoplasma alta.",
   "Células gigantes tumorales.",
   "Pérdida de polaridad."],
  ROBBINS)

# CB-441 · termómetro
V("termometro", "CB-441", "enfermedad-bowen-carcinoma-epidermoide-in-situ", "Progresión del cáncer de piel escamoso",
  "CIENCIAS BÁSICAS ENAM: ENFERMEDAD DE BOWEN", CB,
  ("Carcinoma epidermoide cutáneo", ["Lesión precursora, in situ, invasor",
   "Bowen: in situ (intraepitelial)"]),
  ("Pregunta de patología", ["¿Qué enfermedad es una neoplasia maligna", "intraepitelial?"]),
  {"rotulo": "Etapas",
   "niveles": [("Queratosis", "Actínica", ["Premaligna"]),
               ("In situ", "BOWEN", ["Todo el espesor", "Sin romper basal"]),
               ("Invasor", "Carcinoma", ["Atraviesa la basal"]),
               ("Metástasis", "Ganglios", ["Poco frecuente"])],
   "caso_nivel": 1, "ruta_titulo": "Descartar", "paso_label": "PASO",
   "pasos": [(1, "Darier", ["Genodermatosis"], False),
             (2, "Barrett", ["Metaplasia"], False),
             (3, "Bowen", ["Neoplasia in situ"], True)]},
  ["Placa roja descamativa.",
   "Puede simular psoriasis.",
   "3-5 % progresa a invasor."],
  "Fitzpatrick. Dermatología 9.ª ed. (2019)")

# CB-442 · fases
V("fases", "CB-442", "foliculo-tiroideo-epitelio-simple-cubico-actividad", "Epitelio del folículo tiroideo",
  "CIENCIAS BÁSICAS ENAM: TIROIDES", CB,
  ("Folículo tiroideo", ["Epitelio simple que rodea el coloide",
   "Su altura refleja la actividad"]),
  ("Pregunta de histología", ["¿Qué epitelio forma los folículos?"]),
  {"rotulo": "Según la actividad", "ans": 1,
   "fases": [("Reposo", "Poca TSH", "Plano", ["Mucho coloide"]),
             ("Normal", "Habitual", "SIMPLE CÚBICO", ["Folículo típico"]),
             ("Estimulado", "Graves", "Cilíndrico", ["Poco coloide"])],
   "chips_titulo": "Epitelio · marcado el correcto",
   "chips": [("Simple cúbico", True), ("Estratificado plano", False), ("Seudoestratificado", False), ("Cúbico estratificado", False)]},
  ["Células C: calcitonina.",
   "Carcinoma medular: células C.",
   "NIS capta yodo."],
  ROSS)

# CB-443 · termómetro
V("termometro", "CB-443", "fumador-metaplasia-escamosa-carcinoma-epidermoide", "Del epitelio bronquial al cáncer",
  "CIENCIAS BÁSICAS ENAM: CARCINOMA EPIDERMOIDE", CB,
  ("Carcinogénesis bronquial", ["El tabaco transforma el epitelio",
   "Metaplasia escamosa → displasia → carcinoma"]),
  ("Varón de 50 años fumador", ["Carcinoma epidermoide pulmonar", "¿A qué epitelio se transforma el bronquial?"]),
  {"rotulo": "Secuencia",
   "niveles": [("Normal", "Seudoestratificado", ["Ciliado"]),
               ("Metaplasia", "ESTRATIFICADO", ["ESCAMOSO"]),
               ("Displasia", "Atipia", ["Premaligna"]),
               ("Carcinoma", "Epidermoide", ["Central"])],
   "caso_nivel": 1, "ruta_titulo": "Consecuencias", "paso_label": "PASO",
   "pasos": [(1, "Pierde cilios", ["Tos, infecciones"], False),
             (2, "Escamoso", ["Más resistente"], True),
             (3, "Dejar de fumar", ["Puede revertir"], False)]},
  ["Epidermoide: hipercalcemia por PTHrP.",
   "Suele ser central.",
   "Muy ligado al tabaco."],
  ROBBINS)

# CB-444 · tarjetas
V("tarjetas", "CB-444", "cartilago-avascular-difusion-condrocitos", "Tipos de cartílago",
  "CIENCIAS BÁSICAS ENAM: CARTÍLAGO", CB,
  ("Cartílago", ["Tejido conectivo sin vasos",
   "Se nutre por difusión"]),
  ("Pregunta de histología", ["¿Qué característica tiene el cartílago?"]),
  {"rotulo": "Rasgos y tipos", "ans": 0, "cards": [
      {"titulo": "AVASCULAR", "datos": [
          ("Vasos", "No tiene", True), ("Nervios", "No tiene", True),
          ("Nutrición", "Difusión", True)],
       "pie": "Repara mal"},
      {"titulo": "Hialino", "datos": [
          ("Colágeno", "Tipo II", False), ("Sitio", "Articulaciones", False),
          ("Otro", "Tráquea", False)],
       "pie": "El más común"},
      {"titulo": "Elástico", "datos": [
          ("Fibras", "Elásticas", False), ("Sitio", "Oreja", False),
          ("Otro", "Epiglotis", False)],
       "pie": "Flexible"},
      {"titulo": "Fibrocartílago", "datos": [
          ("Colágeno", "Tipo I", False), ("Sitio", "Discos, meniscos", False),
          ("Otro", "Sínfisis", False)],
       "pie": "Resistente"}]},
  ["Artrosis: el cartílago no se regenera.",
   "Condrocitos en lagunas.",
   "Osteoide: es del hueso."],
  ROSS)

# CB-445 · radial
V("radial", "CB-445", "barrera-hematoencefalica-astrocitos-uniones-estrechas", "Barrera hematoencefálica",
  "CIENCIAS BÁSICAS ENAM: BARRERA HEMATOENCEFÁLICA", CB,
  ("Barrera hematoencefálica", ["Endotelio con uniones estrechas",
   "Los pies de los astrocitos la inducen"]),
  ("Pregunta de neurohistología", ["¿Qué célula participa en la barrera?"]),
  {"rotulo": "Mapa del tema", "centro": "BARRERA", "centro_sub": "Hematoencefálica", "ans": 0,
   "items": [("ASTROCITO", ["Pies terminales", "Inducen la barrera"]),
             ("Endotelio", ["Uniones estrechas", "Sin fenestras"]),
             ("Pericitos", ["Sostén"]),
             ("Sin barrera", ["Área postrema"]),
             ("Meningitis", ["Se abre"])],
   "ruta": ["Capilar cerebral", "Uniones estrechas", "Pies astrocitarios", "BARRERA"]},
  ["Liposolubles pasan; glucosa por GLUT1.",
   "Microglía: fagocitos.",
   "Schwann: mielina periférica."],
  ROSS)

# CB-446 · matriz
V("matriz", "CB-446", "musculo-pilomotor-alfa-1-noradrenalina", "Músculo liso y sistema autónomo",
  "CIENCIAS BÁSICAS ENAM: SISTEMA AUTÓNOMO", CB,
  ("Músculo liso autonómico", ["Unos se contraen con el simpático",
   "Otros con el parasimpático"]),
  ("Pregunta de fisiología", ["¿Qué músculo se contrae por impulsos", "noradrenérgicos?"]),
  {"rotulo": "Contracción según el sistema", "eje_x": "Sistema", "eje_y": "Músculo",
   "cols": ["Simpático", "Parasimpático"], "rows": ["Pilomotor", "Esfínter del iris", "Detrusor"], "caso": (0, 0),
   "cells": [[("CONTRAE", ["Alfa-1", "Piel de gallina"]), ("Sin inervación", [])],
             [("No actúa", ["Dilatador sí"]), ("Contrae", ["Miosis"])],
             [("Relaja", ["Beta-3"]), ("Contrae", ["Micción"])]]},
  ["Bronquios: simpático relaja.",
   "Vesícula biliar: contrae con CCK y ACh.",
   "Sudoríparas: simpáticas colinérgicas."],
  GUYTON)

# CB-447 · tarjetas
V("tarjetas", "CB-447", "tec-detritos-neuronales-microglia-fagocitosis", "Neuroglia",
  "CIENCIAS BÁSICAS ENAM: NEUROGLÍA", CB,
  ("Células gliales", ["Cada tipo tiene una función",
   "La microglía fagocita"]),
  ("Varón con contusión cerebral", ["Daño neuronal extenso", "¿Qué células fagocitan los restos?"]),
  {"rotulo": "¿Qué hace cada una?", "ans": 0, "cards": [
      {"titulo": "MICROGLÍA", "datos": [
          ("Función", "Fagocita", True), ("Origen", "Saco vitelino", True),
          ("Tipo", "Macrófago del SNC", True)],
       "pie": "VIH: nódulos microgliales"},
      {"titulo": "Astrocitos", "datos": [
          ("Función", "Barrera, gliosis", False), ("Tipos", "Fibroso, protopl.", False),
          ("Marcador", "GFAP", False)],
       "pie": "Cicatriz glial"},
      {"titulo": "Oligodendrocitos", "datos": [
          ("Función", "Mielina", False), ("Sitio", "SNC", False),
          ("Lesión", "Esclerosis múltiple", False)],
       "pie": "Varios axones"},
      {"titulo": "Ependimarias", "datos": [
          ("Función", "Revisten ventrículos", False), ("Tipo", "Epitelio", False),
          ("Relación", "LCR", False)],
       "pie": "Plexo coroideo"}]},
  ["Microglía activada: ameboidea.",
   "Presenta antígenos.",
   "Libera citocinas."],
  ROSS)

# CB-448 · fases
V("fases", "CB-448", "celulas-m-placas-peyer-transcitosis-antigenos", "Inmunidad de la mucosa intestinal",
  "CIENCIAS BÁSICAS ENAM: INMUNIDAD DE MUCOSAS", CB,
  ("Células M", ["Epitelio sobre las placas de Peyer",
   "Llevan antígenos a las células inmunes"]),
  ("Pregunta de inmunología", ["¿Qué células transportan antígenos a través", "del epitelio intestinal?"]),
  {"rotulo": "Recorrido del antígeno", "ans": 0,
   "fases": [("Luz", "Transcitosis", "CÉLULA M", ["Sin borde en cepillo"]),
             ("Bolsillo", "Basolateral", "Dendríticas", ["Y linfocitos"]),
             ("Defensa", "Folículo", "IgA secretora", ["Mucosa protegida"])],
   "chips_titulo": "Célula · marcada la correcta",
   "chips": [("Células M", True), ("Paneth", False), ("Enterocitos", False), ("Macrófagos", False)]},
  ["Salmonella y Shigella las usan.",
   "También priones y poliovirus.",
   "Paneth: defensinas."],
  ABBAS)

# CB-449 · radial
V("radial", "CB-449", "valvula-cardiaca-conectivo-denso-endocardio", "Estructura de las válvulas cardíacas",
  "CIENCIAS BÁSICAS ENAM: VÁLVULAS", CB,
  ("Válvulas cardíacas", ["Pliegues del endocardio",
   "Núcleo de tejido conectivo denso"]),
  ("Pregunta de histología", ["¿Qué tejido tiene la válvula cardíaca?"]),
  {"rotulo": "Mapa del tema", "centro": "VÁLVULA", "centro_sub": "Cardíaca", "ans": 0,
   "items": [("CONECTIVO DENSO", ["Cubierto por", "endocardio"]),
             ("Fibrosa", ["Resistencia"]),
             ("Esponjosa", ["Amortigua"]),
             ("Sin vasos", ["Se nutre por difusión"]),
             ("Endocarditis", ["Bacterias se asientan"])],
   "ruta": ["Endocardio", "Pliegue", "Núcleo denso", "VÁLVULA"]},
  ["Se continúa con el esqueleto fibroso.",
   "Fiebre reumática: fusión comisural.",
   "No es pericardio ni miocardio."],
  ROSS)

# CB-450 · árbol
A("CB-450", "vasa-vasorum-adventicia-media-externa-aortitis", "Nutrición de la pared vascular",
  "CIENCIAS BÁSICAS ENAM: PARED VASCULAR", CB,
  ("Vasa vasorum", ["Pequeños vasos de la pared de grandes vasos",
   "Irrigan la adventicia y la media externa"]),
  ("Pregunta de histología", ["¿A qué células irrigan los vasa vasorum?"]),
  Q("¿Qué capa de la pared?", [
      L("Externa", "ADVENTICIA Y MEDIA EXT.", ["Vasa vasorum"], path=True),
      L("Interna", "Íntima y media int.", ["Difusión desde la luz"])], path=True),
  ("Importancia clínica", [("Enfermedad", True), ("Efecto", False)], [
      ("Aortitis sifilítica", ["Endarteritis", "Aneurisma ascendente"]),
      ("Aterosclerosis", ["Neovasos", "Placa inestable"])]),
  ["Corteza de árbol en la aorta.",
   "En venas llegan más profundo.",
   "Disección aórtica."],
  ROSS)

# CB-451 · matriz
V("matriz", "CB-451", "inhibina-b-celulas-sertoli-fsh-varon", "Células del testículo",
  "CIENCIAS BÁSICAS ENAM: HORMONAS TESTICULARES", CB,
  ("Testículo", ["Sertoli responde a FSH",
   "Leydig responde a LH"]),
  ("Pregunta de fisiología", ["¿Qué células producen inhibina en el varón?"]),
  {"rotulo": "Célula y producto", "eje_x": "Dato", "eje_y": "Célula",
   "cols": ["Estímulo", "Produce"], "rows": ["Sertoli", "Leydig", "Germinales"], "caso": (0, 1),
   "cells": [[("FSH", []), ("INHIBINA B", ["AMH, ABP"])],
             [("LH", []), ("Testosterona", [])],
             [("Testosterona", []), ("Espermatozoides", [])]]},
  ["Inhibina B frena solo la FSH.",
   "Baja con FSH alta: daño tubular.",
   "Mujer: células de la granulosa."],
  GUYTON)

# CB-452 · árbol
A("CB-452", "prostaglandinas-semen-vesiculas-seminales", "Origen de los componentes del semen",
  "CIENCIAS BÁSICAS ENAM: GLÁNDULAS SEXUALES", CB,
  ("Semen", ["Cada glándula aporta sustancias",
   "Las prostaglandinas vienen de las vesículas"]),
  ("Pregunta de fisiología", ["¿Dónde se producen las prostaglandinas", "del semen?"]),
  Q("¿Qué glándula?", [
      L("Vesículas seminales", "PROSTAGLANDINAS", ["Fructosa, semenogelina"], path=True),
      L("Próstata", "Citrato, zinc", ["PSA, fosfatasa ácida"])], path=True),
  ("Nombre engañoso", [("Dato", True), ("Explicación", False)], [
      ("Prostaglandina", ["Nombre por próstata", "Se describió allí"]),
      ("Origen real", ["Vesícula seminal", "Mayor producción"])]),
  ["Estimulan contracciones uterinas.",
   "Favorecen el transporte espermático.",
   "Epidídimo: almacena espermatozoides."],
  GUYTON)
