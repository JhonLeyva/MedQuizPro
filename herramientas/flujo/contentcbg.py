"""Ciencias Básicas · parte G (CB-333 a CB-372)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-333 · matriz
V("matriz", "CB-333", "gluconeogenesis-higado-rinon-glucosa-6-fosfatasa", "Órganos de la gluconeogénesis",
  "CIENCIAS BÁSICAS ENAM: GLUCONEOGÉNESIS", CB,
  ("Gluconeogénesis", ["Glucosa nueva desde lactato, alanina, glicerol",
   "Necesita glucosa-6-fosfatasa para liberarla"]),
  ("Pregunta de bioquímica", ["¿Dónde ocurre principalmente?"]),
  {"rotulo": "Órgano y capacidad", "eje_x": "Dato", "eje_y": "Órgano",
   "cols": ["Gluconeogénesis", "Glucosa-6-fosfatasa"], "rows": ["Hígado y riñón", "Músculo", "Cerebro"], "caso": (0, 0),
   "cells": [[("SÍ", ["Riñón: 40 % en ayuno"]), ("Tiene", ["Libera glucosa"])],
             [("No", ["Solo usa su glucógeno"]), ("No tiene", [])],
             [("No", ["Solo consume"]), ("No tiene", [])]]},
  ["Ciclo de Cori: lactato al hígado.",
   "Ciclo glucosa-alanina.",
   "Insuficiencia hepática: hipoglucemia."],
  HARPER)

# CB-334 · fases
V("fases", "CB-334", "sglt2-tubulo-proximal-reabsorcion-glucosa-gliflozinas", "Reabsorción renal de glucosa",
  "CIENCIAS BÁSICAS ENAM: TRANSPORTE TUBULAR", CB,
  ("Glucosa en el túbulo proximal", ["SGLT2 reabsorbe la mayor parte",
   "SGLT1 completa el resto"]),
  ("Pregunta de fisiología", ["¿Qué transportador reabsorbe la glucosa?"]),
  {"rotulo": "A lo largo del proximal", "ans": 0,
   "fases": [("Segmento S1", "Inicial", "SGLT2", ["90 % de la glucosa", "Alta capacidad"]),
             ("Segmento S3", "Final", "SGLT1", ["10 % restante"]),
             ("Salida", "Basolateral", "GLUT2", ["Hacia la sangre"])],
   "chips_titulo": "Transportador · marcado el correcto",
   "chips": [("SGLT-2", True), ("GLUT-1", False), ("GLUT-3", False), ("SGLT-1", False)]},
  ["Gliflozinas: glucosuria de 70 g/día.",
   "Protegen corazón y riñón.",
   "Riesgo: cetoacidosis euglucémica."],
  GUYTON)

# CB-335 · árbol
A("CB-335", "lactosa-glucosa-galactosa-deficit-lactasa-nino", "Disacáridos y sus monosacáridos",
  "CIENCIAS BÁSICAS ENAM: CARBOHIDRATOS", CB,
  ("Disacáridos de la dieta", ["Las disacaridasas del borde en cepillo",
   "los parten en monosacáridos"]),
  ("Niño de 3 años", ["Diarrea crónica que empeora con la leche", "Sospecha de déficit de lactasa"]),
  Q("¿Qué disacárido?", [
      L("Lactosa", "GLUCOSA + GALACTOSA", ["Lactasa", "Leche"], path=True),
      L("Sacarosa", "Glucosa + fructosa", ["Sacarasa"]),
      L("Maltosa", "Glucosa + glucosa", ["Maltasa"])], path=True),
  ("Déficit de lactasa", [("Paso", True), ("Resultado", False)], [
      ("Lactosa al colon", ["No se parte", "Diarrea osmótica"]),
      ("Fermentación", ["Bacterias", "Gas e hidrógeno"])]),
  ["Prueba de hidrógeno espirado.",
   "Secundario tras gastroenteritis.",
   "Heces ácidas."],
  HARPER)

# CB-336 · tarjetas
V("tarjetas", "CB-336", "acidos-grasos-libres-albumina-transporte-plasma", "Transporte de lípidos en la sangre",
  "CIENCIAS BÁSICAS ENAM: LÍPIDOS PLASMÁTICOS", CB,
  ("Lípidos en el plasma", ["Son insolubles: viajan unidos",
   "Cada lípido tiene su transportador"]),
  ("Pregunta de bioquímica", ["¿Cómo viajan los ácidos grasos libres?"]),
  {"rotulo": "¿Qué los transporta?", "ans": 0, "cards": [
      {"titulo": "ALBÚMINA", "datos": [
          ("Lleva", "Ácidos grasos libres", True), ("Origen", "Lipólisis", True),
          ("Destino", "Músculo, hígado", True)],
       "pie": "Varios sitios de unión"},
      {"titulo": "Quilomicrones", "datos": [
          ("Lleva", "TG de la dieta", False), ("Origen", "Intestino", False),
          ("Apo", "B-48", False)],
       "pie": "Vía linfática"},
      {"titulo": "VLDL", "datos": [
          ("Lleva", "TG del hígado", False), ("Origen", "Hígado", False),
          ("Apo", "B-100", False)],
       "pie": "Se vuelve LDL"},
      {"titulo": "HDL", "datos": [
          ("Lleva", "Colesterol", False), ("Hacia", "El hígado", False),
          ("Apo", "A-I", False)],
       "pie": "Transporte reverso"}]},
  ["Ácidos grasos desplazan bilirrubina en el neonato.",
   "Lipólisis: catecolaminas y glucagón.",
   "La insulina frena la lipólisis."],
  HARPER)

# CB-337 · radial
V("radial", "CB-337", "aceite-pescado-omega-3-epa-dha-anchoveta", "Familias de ácidos grasos",
  "CIENCIAS BÁSICAS ENAM: ÁCIDOS GRASOS", CB,
  ("Ácidos grasos", ["Saturados, omega-9, omega-6 y omega-3",
   "El pescado es rico en omega-3"]),
  ("Pregunta de nutrición", ["¿Qué predomina en el aceite de pescado?"]),
  {"rotulo": "Mapa del tema", "centro": "GRASAS", "centro_sub": "Familias", "ans": 0,
   "items": [("OMEGA-3", ["EPA y DHA", "Pescado azul"]),
             ("Omega-6", ["Araquidónico", "Más inflamatorio"]),
             ("Omega-9", ["Oleico", "Aceite de oliva"]),
             ("Saturados", ["Palmítico, esteárico"]),
             ("Efecto EPA", ["Baja triglicéridos"])],
   "ruta": ["Anchoveta", "Aceite de pescado", "Omega-3", "EPA"]},
  ["DHA: retina y cerebro fetal.",
   "Menos eicosanoides inflamatorios.",
   "El Perú produce aceite de anchoveta."],
  HARPER)

# CB-338 · fases
V("fases", "CB-338", "hdl-transporte-reverso-colesterol-abca1-lcat", "Transporte reverso del colesterol",
  "CIENCIAS BÁSICAS ENAM: LIPOPROTEÍNAS", CB,
  ("Transporte reverso", ["Lleva el colesterol de los tejidos al hígado",
   "Lo realiza la HDL"]),
  ("Pregunta de bioquímica", ["¿Qué lipoproteína hace el transporte inverso?"]),
  {"rotulo": "Pasos del transporte", "ans": 1,
   "fases": [("Tejidos", "ABCA1", "Salida", ["Colesterol del macrófago"]),
             ("Plasma", "LCAT", "HDL", ["Esterifica y retiene", "Apo A-I"]),
             ("Hígado", "Receptor SR-B1", "Bilis", ["Eliminación"])],
   "chips_titulo": "Lipoproteína · marcada la correcta",
   "chips": [("HDL", True), ("LDL", False), ("VLDL", False), ("IDL", False)]},
  ["HDL bajo: factor de riesgo.",
   "Varones < 40, mujeres < 50 mg/dL.",
   "LDL lleva colesterol a los tejidos."],
  HARPER)

# CB-339 · puntaje
V("puntaje", "CB-339", "trigliceridos-tejido-adiposo-mayor-reserva-energia", "Reservas de energía del cuerpo",
  "CIENCIAS BÁSICAS ENAM: RESERVAS ENERGÉTICAS", CB,
  ("Reservas de energía", ["Grasa: 9 kcal/g y casi sin agua",
   "Glucógeno: 4 kcal/g y muy hidratado"]),
  ("Pregunta de bioquímica", ["¿Cuál es la mayor reserva de energía?"]),
  {"rotulo": "Kilocalorías de reserva", "escala": "Miles de kcal", "total": 100, "max": 120,
   "total_label": "Triglicéridos",
   "interpreta": "La mayor reserva",
   "items": [("Triglicéridos", "> 100 000", True), ("Proteína muscular", "≈ 25 000", False),
             ("Glucógeno total", "≈ 2 000", False)],
   "bandas": [("≈ 0,08", "Glucosa sangre", "Unos 20 g", False),
              ("≈ 2", "Glucógeno", "Hígado y músculo", False),
              ("> 100", "Triglicéridos", "Tejido adiposo", True)]},
  ["Glucógeno hepático: 12-24 h de ayuno.",
   "El muscular solo sirve al músculo.",
   "La proteína no es reserva."],
  HARPER)

# CB-340 · radial
V("radial", "CB-340", "leptina-adipocito-hipotalamo-saciedad", "Leptina",
  "CIENCIAS BÁSICAS ENAM: HORMONAS DEL APETITO", CB,
  ("Leptina", ["La producen los adipocitos",
   "Informa al hipotálamo de la grasa corporal"]),
  ("Pregunta de fisiología", ["¿Dónde se sintetiza la leptina?"]),
  {"rotulo": "Mapa del tema", "centro": "LEPTINA", "centro_sub": "Hormona", "ans": 0,
   "items": [("TEJIDO ADIPOSO", ["Proporcional a", "la grasa"]),
             ("Núcleo arcuato", ["Frena NPY", "Activa POMC"]),
             ("Efecto", ["Menos apetito", "Más gasto"]),
             ("Reproducción", ["Amenorrea si baja"]),
             ("Grelina", ["Estómago: da hambre"])],
   "ruta": ["Más grasa", "Más leptina", "Hipotálamo", "SACIEDAD"]},
  ["Obesidad: leptina alta con resistencia.",
   "Déficit congénito: obesidad grave.",
   "Atletas y anorexia: amenorrea."],
  GUYTON)

# CB-341 · termómetro
V("termometro", "CB-341", "dieta-acidos-grasos-cadena-corta-media-escasos", "Longitud de los ácidos grasos",
  "CIENCIAS BÁSICAS ENAM: GRASAS DE LA DIETA", CB,
  ("Ácidos grasos por longitud", ["La dieta tiene sobre todo cadena larga",
   "Pocos de cadena media y corta"]),
  ("Pregunta de nutrición", ["¿Qué ácidos grasos escasean en la dieta?"]),
  {"rotulo": "Número de carbonos",
   "niveles": [("< 6 C", "Corta", ["ESCASA", "Fibra en el colon"]),
               ("6-12 C", "Media", ["ESCASA", "Coco, leche"]),
               ("14-22 C", "Larga", ["La mayoría"]),
               ("> 22 C", "Muy larga", ["Peroxisomas"])],
   "caso_nivel": 1, "ruta_titulo": "Uso de la cadena media", "paso_label": "PASO",
   "pasos": [(1, "Sin sales biliares", ["Absorción directa"], True),
             (2, "Vena porta", ["Sin quilomicrones"], True),
             (3, "Uso clínico", ["Malabsorción, quilotórax"], False)]},
  ["Butirato: nutre al colonocito.",
   "Palmítico, oleico, linoleico: larga.",
   "Aceite de coco: cadena media."],
  HARPER)

# CB-342 · matriz
V("matriz", "CB-342", "ayuno-prolongado-oxidacion-acidos-grasos-cetogenesis", "Metabolismo en ayuno y tras comer",
  "CIENCIAS BÁSICAS ENAM: AYUNO", CB,
  ("Ayuno y alimentación", ["Ayuno: baja la insulina, suben contrarreguladoras",
   "Se usan grasas y cuerpos cetónicos"]),
  ("Pregunta de bioquímica", ["¿Cuándo aumenta la oxidación de grasas?"]),
  {"rotulo": "Estado metabólico", "eje_x": "Estado", "eje_y": "Proceso",
   "cols": ["Ayuno prolongado", "Posprandial"], "rows": ["Insulina", "Lipólisis", "Beta-oxidación"], "caso": (2, 0),
   "cells": [[("Baja", ["Glucagón alto"]), ("Alta", [])],
             [("Aumenta", ["Lipasa sensible"]), ("Disminuye", [])],
             [("AUMENTA", ["Cuerpos cetónicos"]), ("Disminuye", ["Síntesis de grasa"])]]},
  ["Malonil-CoA bajo libera la CPT-I.",
   "El cerebro usa cetonas.",
   "Ahorra glucosa y proteínas."],
  HARPER)

# CB-343 · árbol
A("CB-343", "triptofano-serotonina-hidroxilacion-descarboxilacion", "Destinos del triptófano",
  "CIENCIAS BÁSICAS ENAM: AMINOÁCIDOS", CB,
  ("Triptófano", ["Aminoácido esencial",
   "Precursor de serotonina, melatonina y niacina"]),
  ("Pregunta de bioquímica", ["Hidroxilación y descarboxilación", "¿Qué neurotransmisor se forma?"]),
  Q("¿Qué vía sigue el triptófano?", [
      L("Hidroxilasa + descarboxilasa", "SEROTONINA", ["5-HT", "Enterocromafines"], path=True),
      L("Vía quinurenina", "Niacina", ["Si falta: pelagra"])], path=True),
  ("Derivados", [("Molécula", True), ("Dónde", False)], [
      ("Melatonina", ["De la serotonina", "Glándula pineal"]),
      ("5-HIAA", ["Metabolito urinario", "Carcinoide"])]),
  ["La descarboxilasa usa vitamina B6.",
   "Histidina → histamina.",
   "Glutamato → GABA."],
  HARPER)

# CB-344 · fases
V("fases", "CB-344", "l-arginina-oxido-nitrico-sintasa-gmpc", "Síntesis del óxido nítrico",
  "CIENCIAS BÁSICAS ENAM: ÓXIDO NÍTRICO", CB,
  ("Óxido nítrico", ["Se forma a partir de L-arginina",
   "Relaja el músculo liso por GMPc"]),
  ("Pregunta de bioquímica", ["¿Cuál es el precursor del óxido nítrico?"]),
  {"rotulo": "Vía del óxido nítrico", "ans": 0,
   "fases": [("Sustrato", "Endotelio", "L-ARGININA", ["Óxido nítrico sintasa", "Libera citrulina"]),
             ("Difusión", "Músculo liso", "Guanilato ciclasa", ["Sube GMPc"]),
             ("Efecto", "Relajación", "Vasodilatación", ["Baja la presión"])],
   "chips_titulo": "Precursor · marcado el correcto",
   "chips": [("L-arginina", True), ("Renina", False), ("Calmodulina", False), ("Acetilcolina", False)]},
  ["Nitratos liberan óxido nítrico.",
   "Sildenafilo: frena la degradación del GMPc.",
   "Sepsis: exceso de iNOS."],
  GUYTON)

# CB-345 · tarjetas
V("tarjetas", "CB-345", "gaba-principal-neurotransmisor-inhibidor-encefalo", "Neurotransmisores excitadores e inhibidores",
  "CIENCIAS BÁSICAS ENAM: NEUROTRANSMISORES", CB,
  ("Neurotransmisores", ["GABA: principal inhibidor del encéfalo",
   "Glutamato: principal excitador"]),
  ("Pregunta de fisiología", ["¿Principal neurotransmisor inhibidor?"]),
  {"rotulo": "¿Excita o inhibe?", "ans": 0, "cards": [
      {"titulo": "GABA", "datos": [
          ("Efecto", "Inhibe", True), ("Sitio", "Encéfalo", True),
          ("Receptor", "GABA-A (cloro)", True)],
       "pie": "Benzodiacepinas, alcohol"},
      {"titulo": "Glicina", "datos": [
          ("Efecto", "Inhibe", False), ("Sitio", "Médula, tronco", False),
          ("Toxina", "Estricnina", False)],
       "pie": "Inhibidor medular"},
      {"titulo": "Glutamato", "datos": [
          ("Efecto", "EXCITA", False), ("Receptor", "NMDA, AMPA", False),
          ("Exceso", "Excitotoxicidad", False)],
       "pie": "No es inhibidor"},
      {"titulo": "Acetilcolina", "datos": [
          ("Efecto", "Excita", False), ("Sitio", "Placa motora", False),
          ("SNC", "Memoria", False)],
       "pie": "Alzheimer: disminuye"}]},
  ["GABA se forma del glutamato (B6).",
   "Baclofeno: GABA-B.",
   "Isoniacida en sobredosis: convulsiones."],
  GUYTON)

# CB-346 · embudo
V("embudo", "CB-346", "melatonina-glandula-pineal-epifisis-ritmo-circadiano", "Glándula que produce melatonina",
  "CIENCIAS BÁSICAS ENAM: MELATONINA", CB,
  ("Melatonina", ["Sincroniza el ritmo sueño-vigilia",
   "Se secreta en la oscuridad"]),
  ("Pregunta de fisiología", ["¿Dónde se produce la melatonina?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Estructuras del encéfalo",
   "candidatos": ["Epífisis", "Hipotálamo", "Adenohipófisis", "Neurohipófisis"],
   "pasos": [("No es la hipófisis", ["Adenohipófisis", "Neurohipófisis"]),
             ("Glándula, no núcleo", ["Hipotálamo"])],
   "final": ("EPÍFISIS (PINEAL)", ["Desde la serotonina", "Pico de 2 a 4 de la madrugada"]),
   "nota": "El núcleo supraquiasmático la regula por vía simpática."},
  ["La luz frena su secreción.",
   "Insomnio del adulto mayor, jet lag.",
   "Tumor pineal: síndrome de Parinaud."],
  GUYTON)

# CB-347 · fases
V("fases", "CB-347", "higado-ciclo-urea-amoniaco-desaminacion", "Eliminación del nitrógeno",
  "CIENCIAS BÁSICAS ENAM: CICLO DE LA UREA", CB,
  ("Ciclo de la urea", ["El hígado convierte el amoníaco en urea",
   "Empieza en la mitocondria"]),
  ("Pregunta de bioquímica", ["¿Qué función hepática en el metabolismo proteico?"]),
  {"rotulo": "Del aminoácido a la orina", "ans": 2,
   "fases": [("Aminoácido", "Desaminación", "Amoníaco", ["Tóxico para el cerebro"]),
             ("Mitocondria", "CPS I, OTC", "Carbamoil-P", ["Inicio del ciclo"]),
             ("Citosol", "Arginasa", "UREA", ["Sale por la orina"])],
   "chips_titulo": "Función · marcada la correcta",
   "chips": [("Formación de urea", True), ("Ácido sulfúrico", False), ("Desalquilación", False), ("Inmunoglobulinas", False)]},
  ["Encefalopatía hepática: amoníaco alto.",
   "Tratamiento: lactulosa y rifaximina.",
   "Déficit de OTC: ligado al X."],
  HARPER)

# CB-348 · embudo
V("embudo", "CB-348", "beriberi-deficit-tiamina-vitamina-b1", "Vitamina del beriberi",
  "CIENCIAS BÁSICAS ENAM: TIAMINA", CB,
  ("Beriberi", ["Déficit de tiamina (B1)",
   "Falla la energía en nervio y corazón"]),
  ("Pregunta de nutrición", ["¿Qué carencia produce beriberi?"]),
  {"rotulo": "Embudo de vitaminas",
   "inicio": "Vitaminas del grupo B y C",
   "candidatos": ["Tiamina", "Niacina", "Piridoxina", "Ácido ascórbico"],
   "pasos": [("No es la vitamina C", ["Ácido ascórbico"]),
             ("Neuropatía y falla cardíaca", ["Niacina", "Piridoxina"])],
   "final": ("TIAMINA (B1)", ["Cofactor de piruvato DH", "Seco: nervio · húmedo: corazón"]),
   "nota": "Niacina: pelagra. Vitamina C: escorbuto."},
  ["Alcohol, arroz pulido, bariátrica.",
   "Tiamina antes de la glucosa.",
   "Shoshin: forma fulminante."],
  HARPER)

# CB-349 · embudo
V("embudo", "CB-349", "deficit-cobre-anemia-neutropenia-osteoporosis-hipopigmentacion", "Oligoelemento deficiente",
  "CIENCIAS BÁSICAS ENAM: COBRE", CB,
  ("Déficit de cobre", ["Falla la ceruloplasmina, lisil oxidasa",
   "y tirosinasa"]),
  ("Pregunta de nutrición", ["Anemia refractaria, neutropenia, osteoporosis", "Hipopigmentación y ataxia"]),
  {"rotulo": "Embudo de minerales",
   "inicio": "Cinco minerales",
   "candidatos": ["Cobre", "Hierro", "Zinc", "Yodo"],
   "pasos": [("Anemia que no responde al hierro", ["Hierro"]),
             ("Hueso, pigmento y neutrófilos", ["Zinc", "Yodo"])],
   "final": ("COBRE", ["Cofactor de varias enzimas", "Menkes: forma genética"]),
   "nota": "Exceso de zinc causa déficit de cobre."},
  ["Adulto: mielopatía similar a B12.",
   "Prematuros con leche de vaca.",
   "Cirugía bariátrica."],
  HARPER)

# CB-350 · fases
V("fases", "CB-350", "vitamina-c-hidroxilacion-prolina-colageno-escorbuto", "Síntesis de colágeno",
  "CIENCIAS BÁSICAS ENAM: COLÁGENO", CB,
  ("Colágeno", ["Triple hélice de procolágeno",
   "Necesita hidroxilar prolina y lisina"]),
  ("Pregunta de bioquímica", ["¿Qué se necesita para sintetizar colágeno?"]),
  {"rotulo": "Pasos de la síntesis", "ans": 0,
   "fases": [("Retículo", "Hidroxilasas", "VITAMINA C", ["Prolina y lisina"]),
             ("Ensamblaje", "Triple hélice", "Procolágeno", ["Estable"]),
             ("Fuera", "Entrecruzado", "Fibra", ["Lisil oxidasa"])],
   "chips_titulo": "Cofactor · marcado el correcto",
   "chips": [("Vitamina C", True), ("Biotina", False), ("Ácido fólico", False), ("Vitamina E", False)]},
  ["Escorbuto: encías que sangran.",
   "Petequias perifoliculares.",
   "Camu camu: rico en vitamina C."],
  HARPER)

# CB-351 · árbol
A("CB-351", "alcoholico-wernicke-korsakoff-tiamina-antes-glucosa", "Wernicke-Korsakoff",
  "CIENCIAS BÁSICAS ENAM: ENCEFALOPATÍA DE WERNICKE", CB,
  ("Encefalopatía de Wernicke", ["Déficit de tiamina",
   "Confusión, oftalmoplejía, ataxia"]),
  ("Pregunta de nutrición", ["¿Qué deficiencia causa Wernicke-Korsakoff?"]),
  Q("¿Alcohólico con confusión?", [
      L("Sí", "TIAMINA IV", ["Antes de la glucosa", "Dosis altas"], path=True),
      L("Sin tratar", "Korsakoff", ["Amnesia, confabulación"])], path=True),
  ("Zonas dañadas", [("Estructura", True), ("Signo", False)], [
      ("Cuerpos mamilares", ["Atrofia", "Memoria"]),
      ("Tálamo medial", ["Lesión", "Confusión"])]),
  ["Tríada completa en un tercio.",
   "También en hiperémesis y bariátrica.",
   "Urgencia médica."],
  HARRISON)

# CB-352 · termómetro
V("termometro", "CB-352", "xeroftalmia-manchas-bitot-signo-nino-pequeno", "Clasificación de la xeroftalmía",
  "CIENCIAS BÁSICAS ENAM: DÉFICIT DE VITAMINA A", CB,
  ("Xeroftalmía (OMS)", ["Signos oculares del déficit de vitamina A",
   "Bitot: signo objetivo más útil en niños"]),
  ("Pregunta de nutrición", ["¿Signo de mayor valor diagnóstico en niños?"]),
  {"rotulo": "Gravedad ocular",
   "niveles": [("XN", "Ceguera nocturna", ["Difícil de detectar"]),
               ("X1B", "BITOT", ["Signo objetivo clave"]),
               ("X2", "Xerosis corneal", ["Córnea seca"]),
               ("X3", "Queratomalacia", ["Urgencia, ceguera"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Vitamina A oral", ["Dosis altas"], True),
             (2, "Repetir al día y semanas", ["Según OMS"], False),
             (3, "Suplementar", ["Programas periódicos"], False)]},
  ["> 0,5 % de Bitot: problema de salud pública.",
   "Reduce mortalidad infantil.",
   "Ceguera nocturna: primer síntoma."],
  "OMS – Xeroftalmía y ceguera nutricional (2023)")

# CB-353 · tarjetas
V("tarjetas", "CB-353", "ceruloplasmina-cobre-wilson-proteinas-transportadoras", "Proteínas transportadoras del plasma",
  "CIENCIAS BÁSICAS ENAM: PROTEÍNAS TRANSPORTADORAS", CB,
  ("Transportadoras plasmáticas", ["Casi todas las sintetiza el hígado",
   "Cada una lleva una sustancia"]),
  ("Pregunta de bioquímica", ["¿Qué proteína transporta el cobre?"]),
  {"rotulo": "¿Qué transporta?", "ans": 0, "cards": [
      {"titulo": "CERULOPLASMINA", "datos": [
          ("Lleva", "Cobre (90 %)", True), ("Extra", "Ferroxidasa", True),
          ("Baja en", "Wilson", True)],
       "pie": "ATP7B defectuoso"},
      {"titulo": "Transferrina", "datos": [
          ("Lleva", "Hierro", False), ("Alta en", "Ferropenia", False),
          ("Saturación", "20-45 %", False)],
       "pie": "Transporte, no depósito"},
      {"titulo": "Haptoglobina", "datos": [
          ("Capta", "Hemoglobina", False), ("Baja en", "Hemólisis", False),
          ("Tipo", "Fase aguda", False)],
       "pie": "Marcador de hemólisis"},
      {"titulo": "Transcortina", "datos": [
          ("Lleva", "Cortisol", False), ("Sube con", "Estrógenos", False),
          ("Otra", "Prealbúmina: T4", False)],
       "pie": "Globulina fijadora"}]},
  ["Wilson: ceruloplasmina < 20 mg/dL.",
   "Anillo de Kayser-Fleischer.",
   "Cobre urinario alto."],
  HARPER)

# CB-354 · matriz
V("matriz", "CB-354", "vitamina-e-antioxidante-liposoluble-membranas", "Vitaminas liposolubles",
  "CIENCIAS BÁSICAS ENAM: VITAMINAS LIPOSOLUBLES", CB,
  ("Vitaminas A, D, E y K", ["Se absorben con las grasas",
   "La vitamina E es el antioxidante de las membranas"]),
  ("Pregunta de nutrición", ["¿Cuál es la función de la vitamina E?"]),
  {"rotulo": "Función y déficit", "eje_x": "Dato", "eje_y": "Vitamina",
   "cols": ["Función", "Déficit"], "rows": ["Vitamina A", "Vitamina E", "Vitamina K"], "caso": (1, 0),
   "cells": [[("Visión, epitelios", []), ("Ceguera nocturna", [])],
             [("ANTIOXIDANTE", ["Membranas celulares"]), ("Hemólisis, ataxia", [])],
             [("Coagulación", ["II, VII, IX, X"]), ("Sangrado", [])]]},
  ["Déficit de E: fibrosis quística, colestasis.",
   "Vitamina C regenera a la E.",
   "Vitamina D: calcio y fósforo."],
  HARPER)

# CB-355 · árbol
A("CB-355", "vitamina-b12-transporte-activo-factor-intrinseco-cubilina", "Mecanismo de absorción de la B12",
  "CIENCIAS BÁSICAS ENAM: ABSORCIÓN DE B12", CB,
  ("Absorción de B12", ["Unida al factor intrínseco en el íleon",
   "Endocitosis mediada por receptor"]),
  ("Pregunta de fisiología", ["¿Cómo se absorbe principalmente la B12?"]),
  Q("¿Con factor intrínseco?", [
      L("Sí", "TRANSPORTE ACTIVO", ["Receptor cubilina", "1,5-2 µg por comida"], path=True),
      L("No", "Difusión pasiva", ["Solo ≈ 1 % de la dosis"])], path=True),
  ("Uso terapéutico", [("Vía", True), ("Dosis", False)], [
      ("Oral alta", ["Aprovecha el 1 %", "1000-2000 µg/día"]),
      ("Parenteral", ["Clásica", "Anemia perniciosa"])]),
  ["Sale unida a transcobalamina II.",
   "Necesita calcio y pH neutro.",
   "Reservas para 3-5 años."],
  GUYTON)

# CB-356 · matriz
V("matriz", "CB-356", "beriberi-humedo-edema-insuficiencia-alto-gasto", "Beriberi seco y húmedo",
  "CIENCIAS BÁSICAS ENAM: BERIBERI", CB,
  ("Formas del beriberi", ["Seco: neurológico",
   "Húmedo: cardiovascular"]),
  ("Pregunta de nutrición", ["¿Con qué cursa el beriberi húmedo?"]),
  {"rotulo": "Forma y signos", "eje_x": "Forma", "eje_y": "Rasgo",
   "cols": ["Seco", "Húmedo"], "rows": ["Sistema", "Signo clave", "Forma grave"], "caso": (1, 1),
   "cells": [[("Nervios", []), ("Corazón", [])],
             [("Polineuropatía", ["Debilidad distal"]), ("EDEMA", ["Falla de alto gasto"])],
             [("Atrofia", []), ("Shoshin", ["Shock, acidosis"])]]},
  ["Responde rápido a tiamina IV.",
   "Infantil: afonía y falla cardíaca.",
   "Taquicardia y cardiomegalia."],
  HARRISON)

# CB-357 · puntaje
V("puntaje", "CB-357", "mielomeningocele-acido-folico-periconcepcional-dosis", "Ácido fólico preconcepcional",
  "CIENCIAS BÁSICAS ENAM: DEFECTOS DEL TUBO NEURAL", CB,
  ("Prevención de defectos del tubo neural", ["Ácido fólico antes y al inicio del embarazo",
   "Reduce el riesgo 50-70 %"]),
  ("Pregunta de embriología", ["¿Qué previene el mielomeningocele?"]),
  {"rotulo": "Dosis según el riesgo", "escala": "mg/día", "total": 0.4, "max": 5,
   "total_label": "Dosis habitual",
   "interpreta": "Ácido fólico",
   "items": [("Inicio", "1 mes antes", True), ("Hasta", "Semana 12", True), ("Dosis", "0,4 mg", True)],
   "bandas": [("0,4 mg", "Riesgo habitual", "Todas las mujeres", True),
              ("4-5 mg", "Alto riesgo", "Hijo previo, valproato", False),
              ("Harina", "Fortificación", "Perú", False)]},
  ["Tubo neural cierra en la 4.ª semana.",
   "Metotrexato y trimetoprima: riesgo.",
   "Diabetes y obesidad: dosis alta."],
  "OMS – Suplementación de ácido fólico (2015)")

# CB-358 · tarjetas
V("tarjetas", "CB-358", "fluor-no-esencial-efecto-caries-fluorosis", "Minerales esenciales y no esenciales",
  "CIENCIAS BÁSICAS ENAM: MINERALES", CB,
  ("Minerales", ["Esenciales: su falta causa enfermedad",
   "El flúor tiene efectos sin ser esencial"]),
  ("Pregunta de nutrición", ["¿Qué mineral actúa sin ser esencial?"]),
  {"rotulo": "¿Esencial?", "ans": 0, "cards": [
      {"titulo": "FLÚOR", "datos": [
          ("Esencial", "No", True), ("Efecto", "Previene caries", True),
          ("Exceso", "Fluorosis", True)],
       "pie": "Fluorapatita en el esmalte"},
      {"titulo": "Sílice", "datos": [
          ("Esencial", "No claro", False), ("Efecto", "Poco demostrado", False),
          ("Exceso", "Silicosis inhalada", False)],
       "pie": "Oligoelemento dudoso"},
      {"titulo": "Vanadio y níquel", "datos": [
          ("Esencial", "No claro", False), ("Efecto", "Poco demostrado", False),
          ("Humanos", "Sin déficit", False)],
       "pie": "Trazas"},
      {"titulo": "Estaño", "datos": [
          ("Esencial", "No", False), ("Efecto", "Sin función", False),
          ("Humanos", "Sin déficit", False)],
       "pie": "Sin papel conocido"}]},
  ["Flúor en sal, agua y pastas.",
   "Fluorosis dental: manchas.",
   "Fluorosis esquelética si es crónica."],
  HARPER)

# CB-359 · radial
V("radial", "CB-359", "vitamina-k-carboxilacion-factores-coagulacion", "Vitamina K",
  "CIENCIAS BÁSICAS ENAM: VITAMINA K", CB,
  ("Vitamina K", ["Cofactor de la gamma-glutamil carboxilasa",
   "Activa factores de coagulación"]),
  ("Pregunta de nutrición", ["¿Qué acción corresponde a la vitamina K?"]),
  {"rotulo": "Mapa del tema", "centro": "VITAMINA K", "centro_sub": "Coagulación", "ans": 0,
   "items": [("FACTORES", ["II, VII, IX, X", "Proteínas C y S"]),
             ("Warfarina", ["Bloquea su reciclaje"]),
             ("Déficit", ["TP e INR largos"]),
             ("Recién nacido", ["1 mg IM al nacer"]),
             ("Antioxidante", ["No: esa es la E"])],
   "ruta": ["Vitamina K", "Carboxilación", "Unen calcio", "COAGULACIÓN"]},
  ["Enfermedad hemorrágica del neonato.",
   "Leche materna: poca vitamina K.",
   "Antídoto de cumarínicos."],
  HARPER)

# CB-360 · fases
V("fases", "CB-360", "vitamina-d-calcitriol-receptor-nuclear-esteroide", "Activación de la vitamina D",
  "CIENCIAS BÁSICAS ENAM: VITAMINA D", CB,
  ("Vitamina D", ["Actúa como hormona esteroidea",
   "Receptor nuclear (VDR)"]),
  ("Pregunta de nutrición", ["¿Qué vitamina actúa como hormona esteroidea?"]),
  {"rotulo": "Pasos de activación", "ans": 2,
   "fases": [("Piel", "Rayos UVB", "Colecalciferol", ["Desde 7-dehidrocolesterol"]),
             ("Hígado", "25-hidroxilasa", "25-OH-D", ["Forma que se mide"]),
             ("Riñón", "1-alfa-hidroxilasa", "CALCITRIOL", ["Hormona activa", "Receptor nuclear"])],
   "chips_titulo": "Vitamina · marcada la correcta",
   "chips": [("Vitamina D", True), ("Vitamina A", False), ("Vitamina E", False), ("Vitamina K", False)]},
  ["Raquitismo en el niño.",
   "Osteomalacia en el adulto.",
   "ERC: dar calcitriol."],
  HARPER)

# CB-361 · tarjetas
V("tarjetas", "CB-361", "segundo-mensajero-ampc-ip3-intracelular", "Segundos mensajeros",
  "CIENCIAS BÁSICAS ENAM: SEÑALIZACIÓN CELULAR", CB,
  ("Segundo mensajero", ["Molécula intracelular que amplifica la señal",
   "Sirve a varias hormonas y neurotransmisores"]),
  ("Pregunta de fisiología", ["¿Qué es un segundo mensajero?"]),
  {"rotulo": "Ejemplos", "ans": 0, "cards": [
      {"titulo": "DEFINICIÓN", "datos": [
          ("Dónde", "Intracelular", True), ("Responde a", "Hormonas y NT", True),
          ("Función", "Amplifica", True)],
       "pie": "Opción correcta del caso"},
      {"titulo": "AMPc", "datos": [
          ("Enzima", "Adenilato ciclasa", False), ("Proteína G", "Gs y Gi", False),
          ("Ejemplo", "Glucagón", False)],
       "pie": "PKA"},
      {"titulo": "IP3 y DAG", "datos": [
          ("Enzima", "Fosfolipasa C", False), ("Proteína G", "Gq", False),
          ("Efecto", "Sube calcio", False)],
       "pie": "PKC"},
      {"titulo": "GMPc", "datos": [
          ("Enzima", "Guanilato ciclasa", False), ("Activador", "Óxido nítrico", False),
          ("Efecto", "Relaja músculo", False)],
       "pie": "Péptido natriurético"}]},
  ["Esteroides no lo necesitan.",
   "Primer mensajero: hormona.",
   "Calcio también es segundo mensajero."],
  GUYTON)

# CB-362 · árbol
A("CB-362", "corticoides-cicatrizacion-lenta-vitamina-a-revierte", "Cicatrización con corticoides",
  "CIENCIAS BÁSICAS ENAM: CICATRIZACIÓN", CB,
  ("Corticoides y heridas", ["Frenan inflamación, fibroblastos y colágeno",
   "La vitamina A contrarresta ese efecto"]),
  ("Pregunta de farmacología", ["¿Qué vitamina revierte el efecto", "de los corticoides?"]),
  Q("¿Paciente con corticoides crónicos?", [
      L("Sí", "VITAMINA A", ["Oral o tópica", "Estimula epitelización"], path=True),
      L("No", "Cuidado habitual", ["Nutrición, zinc"])], path=True),
  ("Otros factores", [("Factor", True), ("Efecto", False)], [
      ("Vitamina C", ["Cofactor", "No revierte corticoides"]),
      ("Zinc", ["Cofactor", "Mejora la reparación"])]),
  ["Diabetes y desnutrición retrasan.",
   "Útil antes de cirugía.",
   "Vitamina E no revierte."],
  "Sabiston. Tratado de cirugía 21.ª ed. (2022)")

# CB-363 · radial
V("radial", "CB-363", "riboflavina-b2-glositis-queilitis-papilas-linguales", "Déficit de riboflavina",
  "CIENCIAS BÁSICAS ENAM: VITAMINA B2", CB,
  ("Riboflavina (B2)", ["Forma FMN y FAD",
   "Su falta daña piel y mucosas"]),
  ("Pregunta de nutrición", ["¿Qué caracteriza el déficit de B2?"]),
  {"rotulo": "Mapa del tema", "centro": "B2", "centro_sub": "Riboflavina", "ans": 0,
   "items": [("LENGUA", ["Atrofia de papilas", "Color magenta"]),
             ("Labios", ["Queilitis angular"]),
             ("Piel", ["Seborreica"]),
             ("Ojo", ["Fotofobia", "Vasos en córnea"]),
             ("Causas", ["Alcohol, desnutrición"])],
   "ruta": ["Falta B2", "Sin FAD", "Mucosas dañadas", "GLOSITIS"]},
  ["Suele acompañar otros déficits B.",
   "Neuropatía: más B1, B6, B12.",
   "Fuentes: lácteos, huevo."],
  HARPER)

# CB-364 · fases
V("fases", "CB-364", "zona-pelucida-enzimas-acrosomicas-acrosina", "Barreras en la fecundación",
  "CIENCIAS BÁSICAS ENAM: FECUNDACIÓN", CB,
  ("Fecundación", ["El espermatozoide cruza tres barreras",
   "La zona pelúcida la abren las enzimas del acrosoma"]),
  ("Pregunta de embriología", ["¿Cómo penetra la zona pelúcida?"]),
  {"rotulo": "Barreras del ovocito", "ans": 1,
   "fases": [("Corona radiata", "Primera", "Hialuronidasa", ["Y movimiento"]),
             ("Zona pelúcida", "Segunda", "ACROSOMA", ["Acrosina", "Tras unirse a ZP3"]),
             ("Membrana", "Tercera", "Fusión", ["Reacción cortical"])],
   "chips_titulo": "Mecanismo · marcado el correcto",
   "chips": [("Enzimas acrosómicas", True), ("Reacción cortical", False), ("Activación del óvulo", False), ("Lipasas", False)]},
  ["Reacción cortical: bloquea polispermia.",
   "Ocurre en la ampolla tubárica.",
   "Completa la segunda meiosis."],
  LANGMAN)

# CB-365 · puntaje
V("puntaje", "CB-365", "vesicula-seminal-fructosa-60-por-ciento-semen", "Composición del semen",
  "CIENCIAS BÁSICAS ENAM: SEMEN", CB,
  ("Semen", ["Vesículas seminales: la mayor parte",
   "Aportan fructosa, la energía del espermatozoide"]),
  ("Pregunta de fisiología", ["¿Dónde se produce la fructosa seminal?"]),
  {"rotulo": "Aporte al volumen", "escala": "%", "total": 60, "max": 100,
   "total_label": "Vesículas seminales",
   "interpreta": "Fructosa: vesícula seminal",
   "items": [("Vesículas seminales", "60-70 %", True), ("Próstata", "20-30 %", False), ("Testículo", "≈ 5 %", False)],
   "bandas": [("≈ 5 %", "Testículo", "Espermatozoides", False),
              ("20-30 %", "Próstata", "PSA, citrato", False),
              ("60-70 %", "Vesícula", "Fructosa", True)]},
  ["Sin fructosa: agenesia de deferentes.",
   "Cowper: moco preeyaculatorio.",
   "PSA licúa el semen."],
  GUYTON)

# CB-366 · fases
V("fases", "CB-366", "reaccion-acrosomica-union-zp3-zona-pelucida", "Momento de la reacción acrosómica",
  "CIENCIAS BÁSICAS ENAM: REACCIÓN ACROSÓMICA", CB,
  ("Reacción acrosómica", ["Se desencadena al unirse a la ZP3",
   "Antes de atravesar la zona pelúcida"]),
  ("Pregunta de embriología", ["¿Cuándo ocurre la reacción acrosómica?"]),
  {"rotulo": "Secuencia", "ans": 1,
   "fases": [("Capacitación", "Tracto femenino", "Cambia membrana", ["Horas"]),
             ("Unión a ZP3", "Zona pelúcida", "REACCIÓN", ["Entra calcio", "Libera acrosina"]),
             ("Fusión", "Membranas", "Pronúcleos", ["2.ª meiosis"])],
   "chips_titulo": "Momento · marcado el correcto",
   "chips": [("Al unirse a la ZP3", True), ("Tras el pronúcleo", False), ("Con el 2.º polar", False), ("Tras penetrar", False)]},
  ["La progesterona del cúmulo ayuda.",
   "Es previa a cruzar la zona.",
   "Pronúcleos: después de la fusión."],
  LANGMAN)

# CB-367 · termómetro
V("termometro", "CB-367", "blastulacion-cavitacion-blastocisto-implantacion", "Etapas del desarrollo inicial",
  "CIENCIAS BÁSICAS ENAM: DESARROLLO INICIAL", CB,
  ("Primeras semanas", ["Segmentación, blastulación, gastrulación",
   "La cavitación forma el blastocisto"]),
  ("Pregunta de embriología", ["¿En qué etapa hay cavitación e implantación?"]),
  {"rotulo": "Etapas en orden",
   "niveles": [("Segmentación", "Días 1-3", ["Mórula"]),
               ("Blastulación", "Días 4-10", ["CAVITACIÓN", "Implantación"]),
               ("Gastrulación", "Semana 3", ["Tres capas"]),
               ("Organogénesis", "Sem. 4-8", ["Órganos"])],
   "caso_nivel": 1, "ruta_titulo": "El blastocisto", "paso_label": "PASO",
   "pasos": [(1, "Entra líquido", ["En la mórula"], True),
             (2, "Embrioblasto", ["Y trofoblasto"], False),
             (3, "Implanta", ["Días 6-10"], True)]},
  ["Sale de la zona pelúcida antes de implantar.",
   "Trofoblasto: futura placenta.",
   "Embarazo ectópico: implantación anómala."],
  LANGMAN)

# CB-368 · matriz
V("matriz", "CB-368", "bridas-amnioticas-amputacion-dedos-disrupcion", "Tipos de defectos congénitos",
  "CIENCIAS BÁSICAS ENAM: DISMORFOLOGÍA", CB,
  ("Defectos congénitos", ["Se clasifican por su mecanismo",
   "Disrupción: destruye un tejido normal"]),
  ("Recién nacido", ["Amputación de dedos por bridas amnióticas", "¿Qué tipo de defecto es?"]),
  {"rotulo": "Mecanismo y ejemplo", "eje_x": "Dato", "eje_y": "Defecto",
   "cols": ["Mecanismo", "Ejemplo"], "rows": ["Malformación", "Disrupción", "Deformación"], "caso": (1, 1),
   "cells": [[("Intrínseco", []), ("Labio leporino", [])],
             [("Causa externa", ["Sobre tejido normal"]), ("BRIDAS AMNIÓTICAS", ["Amputaciones"])],
             [("Fuerza mecánica", []), ("Pie equino", ["Oligohidramnios"])]]},
  ["Displasia: organización celular anómala.",
   "Bajo riesgo de recurrencia.",
   "Lesiones asimétricas."],
  LANGMAN)

# CB-369 · embudo
V("embudo", "CB-369", "trofoblasto-placenta-corion-sincitiotrofoblasto", "Derivados del trofoblasto",
  "CIENCIAS BÁSICAS ENAM: PLACENTA", CB,
  ("Trofoblasto", ["Capa externa del blastocisto",
   "Forma la parte fetal de la placenta"]),
  ("Pregunta de embriología", ["¿Qué se origina del trofoblasto?"]),
  {"rotulo": "Embudo embriológico",
   "inicio": "Estructuras del embrión",
   "candidatos": ["Placenta", "Epidermis", "Alantoides", "Saco vitelino"],
   "pasos": [("No viene del embrioblasto", ["Alantoides", "Saco vitelino"]),
             ("No es del ectodermo", ["Epidermis"])],
   "final": ("PLACENTA", ["Citotrofoblasto y sincitiotrofoblasto", "Produce hCG"]),
   "nota": "Mola y coriocarcinoma: se vigilan con hCG."},
  ["Sincitiotrofoblasto invade el endometrio.",
   "Lactógeno placentario.",
   "Embrioblasto: embrión y amnios."],
  LANGMAN)

# CB-370 · radial
V("radial", "CB-370", "eritropoyetina-fetal-higado-rinon-hif", "Eritropoyetina fetal",
  "CIENCIAS BÁSICAS ENAM: ERITROPOYESIS FETAL", CB,
  ("Eritropoyetina (EPO)", ["En el feto: sobre todo el hígado",
   "En el adulto: el riñón"]),
  ("Pregunta de fisiología", ["¿Dónde se produce la EPO fetal?"]),
  {"rotulo": "Mapa del tema", "centro": "EPO", "centro_sub": "Fetal", "ans": 0,
   "items": [("HÍGADO FETAL", ["Principal fuente"]),
             ("Riñón adulto", ["Fibroblastos", "peritubulares"]),
             ("Estímulo", ["Hipoxia vía HIF"]),
             ("Placenta", ["No deja pasar", "la EPO materna"]),
             ("Prematuro", ["Anemia por", "poca EPO"])],
   "ruta": ["Hipoxia fetal", "HIF estable", "Hígado", "EPO"]},
  ["El HIF estimula, no inhibe, la EPO.",
   "Hijo de diabética: policitemia.",
   "Empieza en el primer trimestre."],
  GUYTON)

# CB-371 · tarjetas
V("tarjetas", "CB-371", "quiste-conducto-gartner-resto-wolff-pared-vaginal", "Quistes de la vagina y la vulva",
  "CIENCIAS BÁSICAS ENAM: QUISTES GENITALES", CB,
  ("Quistes vaginales", ["Cada uno tiene un origen distinto",
   "Gartner: resto del conducto de Wolff"]),
  ("Pregunta de embriología", ["¿Qué caracteriza al quiste de Gartner?"]),
  {"rotulo": "¿Qué quiste?", "ans": 0, "cards": [
      {"titulo": "GARTNER", "datos": [
          ("Origen", "Conducto de Wolff", True), ("Sitio", "Pared anterolat.", True),
          ("Epitelio", "Cúbico", True)],
       "pie": "Anomalías renales asociadas"},
      {"titulo": "Bartholin", "datos": [
          ("Origen", "Glándula vestibular", False), ("Sitio", "Introito post.", False),
          ("Complicación", "Absceso", False)],
       "pie": "Marsupialización"},
      {"titulo": "Skene", "datos": [
          ("Origen", "Parauretral", False), ("Sitio", "Junto a uretra", False),
          ("Clínica", "Disuria", False)],
       "pie": "Homólogo prostático"},
      {"titulo": "De inclusión", "datos": [
          ("Origen", "Trauma, episiotomía", False), ("Sitio", "Tercio inferior", False),
          ("Epitelio", "Escamoso", False)],
       "pie": "El más frecuente"}]},
  ["Suelen ser asintomáticos.",
   "Herlyn-Werner-Wunderlich.",
   "Diferenciar del divertículo uretral."],
  LANGMAN)

# CB-372 · puntaje
V("puntaje", "CB-372", "genitales-externos-diferenciacion-completa-semana-12", "Cronología de los genitales externos",
  "CIENCIAS BÁSICAS ENAM: DIFERENCIACIÓN SEXUAL", CB,
  ("Genitales externos", ["Iguales hasta la 7.ª semana",
   "Diferenciación completa hacia la semana 12"]),
  ("Pregunta de embriología", ["¿Cuándo termina la diferenciación?"]),
  {"rotulo": "Semanas de gestación", "escala": "Semana", "total": 12, "max": 40,
   "total_label": "Diferenciación completa",
   "interpreta": "Semana 12",
   "items": [("Indiferenciados", "Hasta sem. 7", False), ("Inicio", "Sem. 9", False), ("Completa", "Sem. 12", True)],
   "bandas": [("≤ 7", "Indiferenciado", "Tubérculo genital", False),
              ("9-12", "Diferenciación", "DHT en el varón", True),
              ("> 12", "Crecimiento", "Solo aumenta", False)]},
  ["Ecografía del 1.er trimestre puede fallar.",
   "HSC en fetos XX: genitales ambiguos.",
   "Mujer: no necesita hormonas."],
  LANGMAN)
