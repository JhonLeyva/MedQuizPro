"""Ciencias Básicas · parte C (CB-173 a CB-212)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-173 · matriz
V("matriz", "CB-173", "cianosis-central-lengua-mucosas-periferica-lechos", "Cianosis central y periférica",
  "CIENCIAS BÁSICAS ENAM: CIANOSIS", CB,
  ("Cianosis", ["Hemoglobina reducida > 5 g/dL",
   "Central: sangre arterial desaturada · Periférica: flujo lento"]),
  ("Pregunta de semiología", ["¿Dónde se observa la cianosis central?"]),
  {"rotulo": "Tipo y localización", "eje_x": "Tipo", "eje_y": "Rasgo",
   "cols": ["Central", "Periférica"], "rows": ["Causa", "Dónde verla", "Lengua"], "caso": (1, 0),
   "cells": [[("Hipoxemia", ["Pulmón, shunt"]), ("Flujo lento", ["Frío, shock"])],
             [("LENGUA Y MUCOSA", ["Oral, labios"]), ("Uñas, manos", ["Pies, peribucal"])],
             [("Azulada", []), ("Rosada", [])]]},
  ["La lengua es el sitio más fiable.",
   "Acrocianosis del recién nacido: normal.",
   "Cianosis de la lengua en el neonato: no es normal."],
  "Argente-Álvarez. Semiología médica 3.ª ed. (2021)")

# CB-174 · árbol
A("CB-174", "mosaicismo-error-mitotico-post-cigoto", "Mecanismos de las aneuploidías",
  "CIENCIAS BÁSICAS ENAM: GENÉTICA", CB,
  ("Aneuploidías", ["Pueden nacer de la meiosis o de la mitosis",
   "El mosaico tiene dos líneas celulares"]),
  ("Pregunta de genética", ["¿Qué mecanismo produce un mosaicismo?"]),
  Q("¿Cuándo ocurre el error?", [
      L("Meiosis", "Trisomía completa", ["Gameto anómalo", "Todas las células"]),
      L("Mitosis del cigoto", "MOSAICO", ["Dos líneas celulares", "Tras la fecundación"], path=True),
      L("Dos cigotos", "Quimera", ["Fusión, no mosaico"])], path=True),
  ("Ejemplos de mosaico", [("Síndrome", True), ("Cariotipo", False)], [
      ("Down", ["Mosaico", "47,+21 / 46"]),
      ("Turner", ["Mosaico", "45,X / 46,XX"])]),
  ["Cuanto antes el error, más células afectadas.",
   "Fenotipo del mosaico: suele ser más leve.",
   "Quimera: dos cigotos fusionados."],
  "Thompson & Thompson. Genética en medicina 8.ª ed. (2016)")

# CB-175 · puntaje
V("puntaje", "CB-175", "biodisponibilidad-90-por-ciento-circulacion-sistemica", "Biodisponibilidad de un fármaco",
  "CIENCIAS BÁSICAS ENAM: FARMACOCINÉTICA", CB,
  ("Biodisponibilidad (F)", ["Fracción de la dosis que llega intacta",
   "a la circulación sistémica"]),
  ("Pregunta de farmacología", ["Biodisponibilidad del 90 %", "¿Qué significa?"]),
  {"rotulo": "Destino de la dosis", "escala": "%", "total": 90, "max": 100,
   "total_label": "Llega a la sangre",
   "interpreta": "90 % accede a la circulación",
   "items": [("Dosis administrada", "100 %", True), ("Se pierde antes", "10 %", False),
             ("Llega intacta", "90 %", True)],
   "bandas": [("100 %", "Vía IV", "Por definición", False),
              ("90 %", "Este fármaco", "Alta biodisponibilidad", True),
              ("Baja", "Primer paso", "Nitroglicerina oral", False)]},
  ["Se calcula con el área bajo la curva oral vs IV.",
   "El 10 % no solo se pierde en el hígado.",
   "Sublingual evita el primer paso."],
  KATZUNG)

# CB-176 · tarjetas
V("tarjetas", "CB-176", "aminoglucosidos-no-penetran-snc-meningitis", "Rasgos de los aminoglucósidos",
  "CIENCIAS BÁSICAS ENAM: AMINOGLUCÓSIDOS", CB,
  ("Aminoglucósidos", ["Muy polares: atraviesan mal las membranas",
   "Bactericidas dependientes de la concentración"]),
  ("Pregunta de farmacología", ["¿Qué característica no les es propia?"]),
  {"rotulo": "¿Propio o no?", "ans": 0, "cards": [
      {"titulo": "NO PROPIO", "datos": [
          ("SNC", "Penetran mal", True), ("Meningitis", "No sirven solos", True),
          ("Aun con", "Inflamación", True)],
       "pie": "Opción falsa del caso"},
      {"titulo": "Espectro", "datos": [
          ("Gramnegativos", "Muy activos", False), ("Anaerobios", "Inactivos", False),
          ("TBC", "Estrepto, amikacina", False)],
       "pie": "Necesitan oxígeno"},
      {"titulo": "Dosis", "datos": [
          ("Tipo", "Concentración", False), ("Efecto", "Postantibiótico", False),
          ("Esquema", "Una vez al día", False)],
       "pie": "Menos toxicidad"},
      {"titulo": "Toxicidad", "datos": [
          ("Riñón", "Necrosis tubular", False), ("Oído", "Irreversible", False),
          ("Factor", "Valle alto", False)],
       "pie": "Medir niveles"}]},
  ["Meningitis por gramnegativos: cefalosporinas de 3.ª.",
   "Sinergia con betalactámicos.",
   "Bloqueo neuromuscular: cuidado en miastenia."],
  GOODMAN)

# CB-177 · tarjetas
V("tarjetas", "CB-177", "cefazolina-primera-generacion-profilaxis-quirurgica", "Generaciones de cefalosporinas",
  "CIENCIAS BÁSICAS ENAM: CEFALOSPORINAS", CB,
  ("Cefalosporinas", ["Cada generación amplía hacia gramnegativos",
   "La cefazolina es de primera generación"]),
  ("Pregunta de farmacología", ["¿Qué afirmación de la cefazolina es falsa?"]),
  {"rotulo": "¿Qué generación?", "ans": 0, "cards": [
      {"titulo": "1.ª GENERACIÓN", "datos": [
          ("Ejemplo", "CEFAZOLINA", True), ("Espectro", "Grampositivos", True),
          ("Uso", "Profilaxis", True)],
       "pie": "No es de 2.ª: opción falsa"},
      {"titulo": "2.ª generación", "datos": [
          ("Ejemplo", "Cefuroxima", False), ("Extra", "H. influenzae", False),
          ("Cefamicina", "Cefoxitina", False)],
       "pie": "Anaerobios: cefoxitina"},
      {"titulo": "3.ª generación", "datos": [
          ("Ejemplo", "Ceftriaxona", False), ("Espectro", "Gramnegativos", False),
          ("Pseudomonas", "Ceftazidima", False)],
       "pie": "Buen paso al LCR"},
      {"titulo": "4.ª generación", "datos": [
          ("Ejemplo", "Cefepima", False), ("Espectro", "Amplio", False),
          ("Pseudomonas", "Sí", False)],
       "pie": "5.ª: ceftarolina (SARM)"}]},
  ["Profilaxis: 2 g IV antes de la incisión.",
   "No cubre enterococo ni SARM.",
   "Pobre contra B. fragilis."],
  SANFORD)

# CB-178 · termómetro
V("termometro", "CB-178", "asa-iv-angina-inestable-riesgo-anestesico", "Clasificación ASA",
  "CIENCIAS BÁSICAS ENAM: RIESGO ANESTÉSICO", CB,
  ("Clasificación ASA", ["Estado físico previo a la anestesia",
   "Del I (sano) al VI (donante)"]),
  ("Varón de 70 años", ["HTA, bypass aortobifemoral, hemiparesia antigua", "Angina inestable actual"]),
  {"rotulo": "Estado físico ASA",
   "niveles": [("ASA II", "Leve", ["HTA controlada"]),
               ("ASA III", "Grave limitante", ["Vasculopatía, ACV antiguo"]),
               ("ASA IV", "Amenaza la vida", ["ANGINA INESTABLE"]),
               ("ASA V", "Moribundo", ["Muere sin cirugía"])],
   "caso_nivel": 2, "ruta_titulo": "Cómo se clasifica", "paso_label": "PASO",
   "pasos": [(1, "Buscar lo más grave", ["Angina inestable"], True),
             (2, "¿Amenaza constante?", ["Sí: ASA IV"], True),
             (3, "Antecedentes estables", ["Solo serían ASA III"], False)]},
  ["ASA I: sano. ASA VI: muerte encefálica.",
   "Infarto o ACV < 3 meses: ASA IV.",
   "Se añade E si es cirugía de emergencia."],
  "ASA Physical Status Classification System (2020)")

# CB-179 · matriz
V("matriz", "CB-179", "fibras-dolor-a-delta-c-rapido-lento", "Fibras que conducen el dolor",
  "CIENCIAS BÁSICAS ENAM: NOCICEPCIÓN", CB,
  ("Fibras aferentes", ["Se clasifican por diámetro y mielina",
   "El dolor viaja por A-delta y C"]),
  ("Pregunta de fisiología", ["¿Qué fibras transmiten el dolor?"]),
  {"rotulo": "Tipo de fibra", "eje_x": "Rasgo", "eje_y": "Fibra",
   "cols": ["Conducción", "Lleva"], "rows": ["A-delta", "C", "A-beta"], "caso": (0, 1),
   "cells": [[("Mielínica fina", ["5-30 m/s"]), ("DOLOR RÁPIDO", ["Agudo, localizado"])],
             [("Amielínica", ["0,5-2 m/s"]), ("DOLOR LENTO", ["Sordo, urente"])],
             [("Mielínica gruesa", []), ("Tacto, vibración", ["Cierra la compuerta"])]]},
  ["Llegan al asta posterior (láminas I, II, V).",
   "Suben por el haz espinotalámico.",
   "Fibras B: preganglionares autonómicas."],
  GUYTON)

# CB-180 · radial
V("radial", "CB-180", "dolor-postoperatorio-nociceptivo-analgesia-multimodal", "Tipos de dolor",
  "CIENCIAS BÁSICAS ENAM: DOLOR", CB,
  ("Clasificación del dolor", ["Nociceptivo: por daño tisular",
   "Neuropático: por lesión del nervio"]),
  ("Pregunta de fisiología", ["¿Qué tipo es el dolor postoperatorio?"]),
  {"rotulo": "Mapa del tema", "centro": "DOLOR", "centro_sub": "Tipos", "ans": 0,
   "items": [("NOCICEPTIVO", ["Postoperatorio", "Somático y visceral"]),
             ("Neuropático", ["Urente, lancinante", "Postoracotomía"]),
             ("Psicógeno", ["Sin lesión orgánica"]),
             ("Nociplástico", ["Fibromialgia"]),
             ("Manejo", ["Analgesia multimodal"])],
   "ruta": ["Incisión", "Inflamación", "Nociceptores", "NOCICEPTIVO"]},
  ["Paracetamol + AINE + opioide si hace falta.",
   "Infiltración de la herida y bloqueos.",
   "El neuropático puede cronificarse."],
  "Miller. Anestesia 9.ª ed. (2020)")

# CB-181 · puntaje
V("puntaje", "CB-181", "apache-ii-puntaje-alto-mayor-mortalidad", "Escala APACHE II",
  "CIENCIAS BÁSICAS ENAM: ESCALAS DE GRAVEDAD", CB,
  ("APACHE II", ["Gravedad en las primeras 24 h de UCI",
   "A mayor puntaje, mayor mortalidad"]),
  ("Pregunta de medicina crítica", ["¿Qué afirmación es incorrecta?"]),
  {"rotulo": "Componentes y puntaje", "escala": "APACHE II", "total": 25, "max": 71,
   "total_label": "Ejemplo de puntaje",
   "interpreta": "Alto = peor pronóstico",
   "items": [("12 variables fisiológicas", "0-60", True), ("Edad", "0-6", True),
             ("Enfermedad crónica", "0-5", True)],
   "bandas": [("0-9", "Baja", "Mortalidad < 10 %", False),
              ("10-24", "Intermedia", "Riesgo creciente", False),
              ("≥ 25", "Alta", "Mortalidad > 50 %", True)]},
  ["Incluye temperatura, PAM y Glasgow.",
   "Pancreatitis: APACHE II ≥ 8 es grave.",
   "Ranson espera 48 horas."],
  "Knaus WA. Crit Care Med (1985) · " + HARRISON)

# CB-182 · radial
V("radial", "CB-182", "tronco-celiaco-ramas-gastrica-izquierda-curvatura-menor", "Ramas del tronco celíaco",
  "CIENCIAS BÁSICAS ENAM: TRONCO CELÍACO", CB,
  ("Tronco celíaco", ["Tres ramas: gástrica izquierda, hepática",
   "común y esplénica"]),
  ("Pregunta de anatomía", ["¿Qué arteria recorre la curvatura menor?"]),
  {"rotulo": "Mapa del tema", "centro": "CELÍACO", "centro_sub": "Tronco", "ans": 0,
   "items": [("GÁSTRICA IZQ.", ["Curvatura menor", "Ramas esofágicas"]),
             ("Hepática común", ["Gastroduodenal", "Gástrica derecha"]),
             ("Esplénica", ["Vasos cortos", "Gastroepiploica izq."]),
             ("Gastroepiploicas", ["Curvatura mayor"]),
             ("Gastroduodenal", ["Úlcera bulbar"])],
   "ruta": ["Tronco celíaco", "Rama más pequeña", "Sube al cardias", "CURVATURA MENOR"]},
  ["Vena gástrica izquierda: vía de las várices.",
   "Gastroduodenal: sangrado de úlcera posterior.",
   "Esplénica: la rama más grande."],
  MOORE)

# CB-183 · tarjetas
V("tarjetas", "CB-183", "ganglios-gastricos-grupo-11-arteria-esplenica", "Estaciones ganglionares gástricas",
  "CIENCIAS BÁSICAS ENAM: CÁNCER GÁSTRICO", CB,
  ("Clasificación japonesa (JGCA)", ["Grupos 1-6: perigástricos",
   "Grupos 7-12: arterias del tronco celíaco"]),
  ("Pregunta de anatomía quirúrgica", ["¿Dónde está el grupo 11?"]),
  {"rotulo": "¿Qué arteria?", "ans": 0, "cards": [
      {"titulo": "GRUPO 11", "datos": [
          ("Sitio", "Arteria esplénica", True), ("11p", "Proximal", True),
          ("D2", "Incluye 11p", True)],
       "pie": "Linfadenectomía D2"},
      {"titulo": "Grupo 7", "datos": [
          ("Sitio", "Gástrica izquierda", False), ("D2", "Sí", False),
          ("Grupo", "Celíaco", False)],
       "pie": "Coronaria estomáquica"},
      {"titulo": "Grupo 8", "datos": [
          ("Sitio", "Hepática común", False), ("D2", "8a", False),
          ("Grupo", "Celíaco", False)],
       "pie": "Anterior"},
      {"titulo": "Grupos 9 y 10", "datos": [
          ("9", "Tronco celíaco", False), ("10", "Hilio esplénico", False),
          ("12", "Hepatoduodenal", False)],
       "pie": "Resto de estaciones"}]},
  ["Extraer al menos 16 ganglios.",
   "Grupos 1-2 paracardiales, 3-4 curvaturas.",
   "5 suprapilórico, 6 infrapilórico."],
  "Japanese Gastric Cancer Treatment Guidelines (2021)")

# CB-184 · fases
V("fases", "CB-184", "glucocorticoides-receptor-intracelular-transcripcion", "Mecanismo de los glucocorticoides",
  "CIENCIAS BÁSICAS ENAM: CORTICOIDES", CB,
  ("Glucocorticoides", ["Liposolubles: atraviesan la membrana",
   "Actúan como factores de transcripción"]),
  ("Pregunta de farmacología", ["¿Dónde actúan los glucocorticoides?"]),
  {"rotulo": "Pasos del efecto", "ans": 0,
   "fases": [("Citoplasma", "Minutos", "RECEPTOR", ["Intracelular", "Se suelta de HSP90"]),
             ("Núcleo", "Horas", "ADN", ["Se une al GRE del ADN"]),
             ("Efecto", "Horas-días", "Proteínas", ["Lipocortina ↑", "NF-κB ↓"])],
   "chips_titulo": "Sitio de acción · marcado el correcto",
   "chips": [("Receptor intracelular", True), ("AMPc", False), ("Proteína G", False), ("Tirosina cinasa", False)]},
  ["Igual actúan esteroides sexuales y tiroxina.",
   "Efecto genómico: tarda horas.",
   "Inhiben indirectamente la fosfolipasa A2."],
  GOODMAN)

# CB-185 · fases
V("fases", "CB-185", "celulas-intersticiales-cajal-ondas-lentas-marcapaso", "Marcapaso intestinal",
  "CIENCIAS BÁSICAS ENAM: MOTILIDAD DIGESTIVA", CB,
  ("Células intersticiales de Cajal", ["Entre las capas musculares, junto al plexo",
   "Generan las ondas lentas"]),
  ("Pregunta de fisiología", ["¿Qué células son el marcapaso digestivo?"]),
  {"rotulo": "Del ritmo a la contracción", "ans": 0,
   "fases": [("Ritmo", "3/min estómago", "CAJAL", ["Ondas lentas"]),
             ("Umbral", "Estímulo", "Espigas", ["Neural u hormonal"]),
             ("Músculo", "Contracción", "Peristaltismo", ["Coordinado"])],
   "chips_titulo": "Marcapaso · marcado el correcto",
   "chips": [("Intersticiales de Cajal", True), ("Neuronas", False), ("Parietales", False), ("Enterocitos", False)]},
  ["Expresan c-KIT (CD117).",
   "GIST: tumor de estas células, responde a imatinib.",
   "Duodeno: 12 ondas por minuto."],
  GUYTON)

# CB-186 · árbol
A("CB-186", "secretina-inhibe-acido-estimula-bicarbonato", "Acciones de la secretina",
  "CIENCIAS BÁSICAS ENAM: SECRETINA", CB,
  ("Secretina", ["La liberan las células S del duodeno",
   "Estímulo: quimo ácido con pH < 4,5"]),
  ("Pregunta de fisiología", ["¿Qué no es función de la secretina?"]),
  Q("¿Sobre qué órgano?", [
      L("Páncreas y bilis", "Estimula", ["Bicarbonato y agua", "Secreción biliar"]),
      L("Estómago", "INHIBE EL ÁCIDO", ["Y la gastrina", "Estimula pepsinógeno"], path=True)], path=True),
  ("Secretina y gastrina", [("Secretina", True), ("Gastrina", False)], [
      ("Ácido gástrico", ["Lo inhibe", "Lo estimula"]),
      ("Estímulo", ["Ácido en duodeno", "Proteínas, distensión"])]),
  ["Fue la primera hormona descubierta.",
   "Gastrinoma: sube paradójicamente con secretina.",
   "Retrasa el vaciamiento gástrico."],
  GUYTON)

# CB-187 · puntaje
V("puntaje", "CB-187", "volumen-diario-secreciones-digestivas-gastrica-1500", "Volumen de las secreciones digestivas",
  "CIENCIAS BÁSICAS ENAM: SECRECIONES DIGESTIVAS", CB,
  ("Secreciones digestivas", ["Unos 7-8 litros al día",
   "Valores de referencia de Guyton"]),
  ("Pregunta de fisiología", ["¿Qué relación es incorrecta?", "Dice: gástrica 2500 mL"]),
  {"rotulo": "Volumen diario (mL)", "escala": "mL/día", "total": 1500, "max": 2500,
   "total_label": "Gástrica real",
   "interpreta": "2500 mL es incorrecto",
   "items": [("Saliva", "1000", False), ("Páncreas y bilis", "1000 c/u", False),
             ("Gástrica", "1500", True)],
   "bandas": [("1000", "Saliva, bilis", "Páncreas igual", False),
              ("1500", "Gástrica", "No 2500", True),
              ("1800", "Intestino", "Delgado", False)]},
  ["Vómitos: alcalosis hipoclorémica.",
   "Diarrea: acidosis metabólica.",
   "Brunner y colon: unos 200 mL cada uno."],
  GUYTON)

# CB-188 · tarjetas
V("tarjetas", "CB-188", "celula-parietal-acido-clorhidrico-factor-intrinseco", "Células de la mucosa gástrica",
  "CIENCIAS BÁSICAS ENAM: HISTOLOGÍA GÁSTRICA", CB,
  ("Glándulas gástricas", ["Cada célula tiene una secreción",
   "La parietal produce ácido y factor intrínseco"]),
  ("Pregunta de fisiología", ["¿Qué secretan las células parietales?"]),
  {"rotulo": "¿Qué secreta?", "ans": 0, "cards": [
      {"titulo": "PARIETAL", "datos": [
          ("Secreta", "HCl", True), ("También", "Factor intrínseco", True),
          ("Bomba", "H⁺/K⁺-ATPasa", True)],
       "pie": "Estímulo: histamina, gastrina, ACh"},
      {"titulo": "Principal", "datos": [
          ("Secreta", "Pepsinógeno", False), ("También", "Lipasa gástrica", False),
          ("Zona", "Fondo glandular", False)],
       "pie": "Cimógena"},
      {"titulo": "Mucosa", "datos": [
          ("Secreta", "Moco", False), ("También", "Bicarbonato", False),
          ("Zona", "Cuello", False)],
       "pie": "Protección"},
      {"titulo": "Célula G", "datos": [
          ("Secreta", "Gastrina", False), ("Zona", "Antro", False),
          ("Estímulo", "Proteínas", False)],
       "pie": "Endocrina"}]},
  ["Omeprazol bloquea la bomba de protones.",
   "Anemia perniciosa: destruye parietales.",
   "Histamina: receptor H2 de la parietal."],
  GUYTON)

# CB-189 · radial
V("radial", "CB-189", "pancreatoduodenal-superior-rama-gastroduodenal", "Irrigación del páncreas",
  "CIENCIAS BÁSICAS ENAM: IRRIGACIÓN PANCREÁTICA", CB,
  ("Arcadas pancreatoduodenales", ["Superiores: de la gastroduodenal",
   "Inferiores: de la mesentérica superior"]),
  ("Pregunta de anatomía", ["¿De dónde nace la pancreatoduodenal", "posterosuperior?"]),
  {"rotulo": "Mapa del tema", "centro": "PÁNCREAS", "centro_sub": "Arterias", "ans": 0,
   "items": [("GASTRODUODENAL", ["Pancreatoduodenales", "superiores"]),
             ("Mesentérica sup.", ["Pancreatoduodenales", "inferiores"]),
             ("Esplénica", ["Cuerpo y cola"]),
             ("Hepática común", ["Origen de la", "gastroduodenal"]),
             ("Arcada", ["Une celíaco y", "mesentérica"])],
   "ruta": ["Tronco celíaco", "Hepática común", "Gastroduodenal", "PANCREATODUODENAL"]},
  ["Circulación colateral si se ocluye un tronco.",
   "Úlcera bulbar posterior: gastroduodenal.",
   "Termina como gastroepiploica derecha."],
  MOORE)

# CB-190 · embudo
V("embudo", "CB-190", "conducto-wolff-derivados-no-tubulos-seminiferos", "Derivados del conducto de Wolff",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA GENITAL MASCULINA", CB,
  ("Conducto mesonéfrico (Wolff)", ["Con testosterona forma las vías espermáticas",
   "Epidídimo, deferente, vesícula seminal, eyaculador"]),
  ("Pregunta de embriología", ["¿Qué estructura no deriva de él?"]),
  {"rotulo": "Embudo embriológico",
   "inicio": "Estructuras masculinas",
   "candidatos": ["Túbulos seminíferos", "Epidídimo", "Deferente", "Vesícula seminal"],
   "pasos": [("Derivan del conducto de Wolff", ["Epidídimo", "Deferente"]),
             ("También de Wolff", ["Vesícula seminal"])],
   "final": ("TÚBULOS SEMINÍFEROS", ["Nacen de los cordones sexuales", "No del conducto de Wolff"]),
   "nota": "Conductillos eferentes: túbulos mesonéfricos."},
  ["En la mujer queda el conducto de Gartner.",
   "La testosterona mantiene el conducto de Wolff.",
   "Sertoli y Leydig: gónada, no Wolff."],
  LANGMAN)

# CB-191 · matriz
V("matriz", "CB-191", "efecto-muscarinico-hipotension-no-hipertension", "Efectos muscarínicos y nicotínicos",
  "CIENCIAS BÁSICAS ENAM: SISTEMA COLINÉRGICO", CB,
  ("Receptores colinérgicos", ["Muscarínicos: órganos del parasimpático",
   "Nicotínicos: ganglios y placa motora"]),
  ("Pregunta de farmacología", ["¿Qué no es un efecto muscarínico?"]),
  {"rotulo": "Efecto según receptor", "eje_x": "Receptor", "eje_y": "Órgano",
   "cols": ["Muscarínico", "Nicotínico"], "rows": ["Ojo, glándulas", "Corazón", "Vasos y PA"], "caso": (2, 0),
   "cells": [[("Miosis", ["Broncorrea, epífora"]), ("—", [])],
             [("Bradicardia", ["M2"]), ("Taquicardia", ["Ganglios simpáticos"])],
             [("HIPOTENSIÓN", ["Vasodilatación NO"]), ("Hipertensión", ["Médula suprarrenal"])]]},
  ["La hipertensión es efecto nicotínico.",
   "DUMBELS: signos muscarínicos.",
   "Fasciculaciones: placa motora (nicotínico)."],
  GOODMAN)

# CB-192 · embudo
V("embudo", "CB-192", "adolescente-soporoso-convulsiones-fasciculaciones-organofosforado", "Diagnóstico del síndrome colinérgico",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIONES", CB,
  ("Síndrome colinérgico", ["Muscarínico + nicotínico + central",
   "Típico de organofosforados y carbamatos"]),
  ("Paciente de 15 años", ["Soporoso, vómitos, diarrea, sialorrea", "Miosis, broncoespasmo, fasciculaciones"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Coma con convulsiones",
   "candidatos": ["Organofosforados", "Salicilatos", "Benzodiacepinas", "Meningitis"],
   "pasos": [("Hay miosis con secreciones", ["Salicilatos", "Meningitis"]),
             ("Hay fasciculaciones", ["Benzodiacepinas"])],
   "final": ("ORGANOFOSFORADOS", ["Inhiben la acetilcolinesterasa", "Atropina + pralidoxima"]),
   "nota": "Salicilatos: taquipnea y alcalosis, sin miosis."},
  ["Frecuente por plaguicidas en zonas agrícolas.",
   "Medir colinesterasa eritrocitaria.",
   "No esperar el resultado para tratar."],
  TOXI)

# CB-193 · tarjetas
V("tarjetas", "CB-193", "acinetobacter-baumannii-hospitalario-multirresistente", "Patógenos y su contexto",
  "CIENCIAS BÁSICAS ENAM: INFECCIONES NOSOCOMIALES", CB,
  ("Infecciones hospitalarias", ["Gramnegativos no fermentadores",
   "Sobreviven en superficies y equipos"]),
  ("Pregunta de microbiología", ["¿Qué enunciado es correcto?"]),
  {"rotulo": "¿Es correcto?", "ans": 0, "cards": [
      {"titulo": "ACINETOBACTER", "datos": [
          ("Ámbito", "Hospitalario", True), ("Infección", "NAV, catéter", True),
          ("Resistencia", "Multirresistente", True)],
       "pie": "Colistina o tigeciclina"},
      {"titulo": "Neumococo", "datos": [
          ("Norfloxacina", "No sirve", False), ("Ámbito", "Comunidad", False),
          ("Uso", "Levofloxacino", False)],
       "pie": "Opción falsa"},
      {"titulo": "Enterococo", "datos": [
          ("Nosocomial", "≈ 10 %", False), ("No es", "30 %", False),
          ("Resistencia", "Vancomicina", False)],
       "pie": "Opción falsa"},
      {"titulo": "S. epidermidis", "datos": [
          ("Meticilina", "Resistente", False), ("Infección", "Catéteres", False),
          ("Uso", "Vancomicina", False)],
       "pie": "Opción falsa"}]},
  ["Candida: frecuente en nutrición parenteral.",
   "Acinetobacter: cocobacilo gramnegativo.",
   "Higiene de manos: principal prevención."],
  MURRAY)

# CB-194 · matriz
V("matriz", "CB-194", "antidotos-paracetamol-n-acetilcisteina-flumazenil-naloxona", "Antídotos específicos",
  "CIENCIAS BÁSICAS ENAM: ANTÍDOTOS", CB,
  ("Antídotos", ["Cada tóxico tiene su antagonista",
   "El caso pide el par correcto"]),
  ("Pregunta de toxicología", ["¿Qué antídoto está bien emparejado?"]),
  {"rotulo": "Tóxico y antídoto", "eje_x": "Dato", "eje_y": "Tóxico",
   "cols": ["Antídoto", "Mecanismo"], "rows": ["Paracetamol", "Benzodiacepinas", "Opioides"], "caso": (0, 0),
   "cells": [[("N-ACETILCISTEÍNA", ["Par correcto"]), ("Repone glutatión", [])],
             [("Flumazenil", ["No naloxona"]), ("Antagonista GABA-A", [])],
             [("Naloxona", []), ("Antagonista mu", [])]]},
  ["Metanol y etilenglicol: fomepizol o etanol.",
   "Talio: azul de Prusia.",
   "Carbamatos: atropina."],
  TOXI)

# CB-195 · fases
V("fases", "CB-195", "jarisch-herxheimer-penicilina-sifilis-secundaria", "Reacción de Jarisch-Herxheimer",
  "CIENCIAS BÁSICAS ENAM: SÍFILIS", CB,
  ("Jarisch-Herxheimer", ["Lisis masiva de espiroquetas",
   "Liberación de citocinas tras el antibiótico"]),
  ("Pregunta de infectología", ["Horas después de la penicilina", "¿Cómo se llama la reacción?"]),
  {"rotulo": "Evolución tras la dosis", "ans": 1,
   "fases": [("Dosis", "Hora 0", "Penicilina", ["Treponemas mueren"]),
             ("2-24 horas", "Citocinas", "JARISCH-HERXHEIMER", ["Fiebre, escalofríos", "Mialgias"]),
             ("< 24 horas", "Remite", "Resolución", ["Antipiréticos"])],
   "chips_titulo": "Nombre de la reacción · marcado el correcto",
   "chips": [("Jarisch-Herxheimer", True), ("Weinberg", False), ("Takata", False), ("Nonne-Apelt", False)]},
  ["No es alergia: no suspender la penicilina.",
   "Gestante: vigilar contracciones.",
   "También en leptospirosis y borreliosis."],
  "CDC – STI Treatment Guidelines (2021)")

# CB-196 · fases
V("fases", "CB-196", "insuficiencia-cardiaca-derecha-edema-signo-tardio", "Signos de la insuficiencia cardíaca derecha",
  "CIENCIAS BÁSICAS ENAM: EDEMA", CB,
  ("Edema", ["Necesita varios litros en el intersticio",
   "Antes solo sube el peso"]),
  ("Pregunta de fisiopatología", ["¿Qué afirmación sobre el edema es falsa?"]),
  {"rotulo": "Orden de aparición", "ans": 2,
   "fases": [("Primero", "Precoz", "Yugulares", ["Reflujo hepatoyugular"]),
             ("Después", "Intermedio", "Hepatomegalia", ["Congestiva"]),
             ("Tardío", "Varios litros", "EDEMA", ["Signo tardío", "Declive, vespertino"])],
   "chips_titulo": "Opción falsa · marcada",
   "chips": [("Edema precoz", True), ("Empeora en el día", False), ("Sacro si encamado", False), ("Depende de gravedad", False)]},
  ["El edema cardíaco sigue la gravedad.",
   "Nefrótico: párpados por la mañana.",
   "Encamado: región sacra."],
  HARRISON)

# CB-197 · radial
V("radial", "CB-197", "oponente-pulgar-nervio-mediano-rama-recurrente", "Nervios de la mano",
  "CIENCIAS BÁSICAS ENAM: MANO", CB,
  ("Inervación de la mano", ["Eminencia tenar: mediano",
   "Interóseos y aductor del pulgar: cubital"]),
  ("Pregunta de anatomía", ["¿Qué nervio inerva el oponente del pulgar?"]),
  {"rotulo": "Mapa del tema", "centro": "MANO", "centro_sub": "Nervios", "ans": 0,
   "items": [("MEDIANO", ["Oponente, abductor corto", "Rama recurrente"]),
             ("Cubital", ["Interóseos", "Aductor del pulgar"]),
             ("Radial", ["Extensores", "Sin músculos intrínsecos"]),
             ("Mediano alto", ["Mano de predicador"]),
             ("Garra cubital", ["4.º y 5.º dedos"])],
   "ruta": ["Oponente", "Eminencia tenar", "Rama recurrente", "MEDIANO"]},
  ["Túnel carpiano: atrofia tenar.",
   "Signo de Froment: lesión cubital.",
   "Radial: mano caída."],
  MOORE)

# CB-198 · árbol
A("CB-198", "politrauma-shock-hematocrito-20-paquete-globular", "Reposición en el shock hemorrágico",
  "CIENCIAS BÁSICAS ENAM: SHOCK HEMORRÁGICO", CB,
  ("Shock hemorrágico", ["Limitar el cristaloide a 1 L",
   "Transfundir pronto hemoderivados"]),
  ("Varón de 36 años, accidente de tránsito", ["Shock con hematocrito de 20 %", "Sigue hipotenso tras 1 L de cristaloide"]),
  Q("¿Responde a 1 L de cristaloide?", [
      L("Sí, sostenida", "Vigilar", ["Buscar lesiones"]),
      Q("¿Hemorragia masiva?", [
          L("No", "PAQUETE GLOBULAR", ["Concentrado de hematíes", "Control del sangrado"], path=True),
          L("Sí", "Protocolo 1:1:1", ["Hematíes, plasma, plaquetas"])], edge="No o transitoria", path=True)], path=True),
  ("Tríada letal", [("Problema", True), ("Evitar", False)], [
      ("Coagulopatía", ["Dilución", "Exceso de cristaloide"]),
      ("Hipotermia", ["Fluidos fríos", "Calentar"])]),
  ["Ácido tranexámico en las primeras 3 horas.",
   "Coloides no mejoran la sobrevida.",
   "Control quirúrgico del sangrado."],
  ATLS)

# CB-199 · matriz
V("matriz", "CB-199", "nino-sustancia-desconocida-toxindrome-colinergico", "Toxíndromes",
  "CIENCIAS BÁSICAS ENAM: TOXÍNDROMES", CB,
  ("Toxíndromes", ["Grupos de signos que orientan al tóxico",
   "Pupilas y secreciones son la clave"]),
  ("Niño de 5 años", ["Diarrea, vómitos, bradicardia", "Miosis, sialorrea, fasciculaciones"]),
  {"rotulo": "Signos clave", "eje_x": "Signo", "eje_y": "Toxíndrome",
   "cols": ["Pupilas", "Secreciones"], "rows": ["Colinérgico", "Anticolinérgico", "Opioide"], "caso": (0, 0),
   "cells": [[("MIOSIS", ["Con fasciculaciones"]), ("Aumentadas", ["Sialorrea, diarrea"])],
             [("Midriasis", []), ("Secas", ["Piel roja, caliente"])],
             [("Miosis", ["Depresión respiratoria"]), ("Normales", [])]]},
  ["Simpaticomimético: midriasis con sudoración.",
   "Causa típica: organofosforados.",
   "Tratar con atropina."],
  TOXI)

# CB-200 · tarjetas
V("tarjetas", "CB-200", "alopurinol-xantina-oxidasa-uricemia", "Fármacos en la gota",
  "CIENCIAS BÁSICAS ENAM: GOTA", CB,
  ("Tratamiento de la gota", ["Crisis: antiinflamatorios",
   "Base: bajar el ácido úrico"]),
  ("Pregunta de farmacología", ["¿Qué fármaco reduce la uricemia?"]),
  {"rotulo": "¿Baja el ácido úrico?", "ans": 0, "cards": [
      {"titulo": "ALOPURINOL", "datos": [
          ("Blanco", "Xantina oxidasa", True), ("Uricemia", "Baja", True),
          ("Meta", "< 6 mg/dL", True)],
       "pie": "HLA-B*5801: reacciones graves"},
      {"titulo": "Colchicina", "datos": [
          ("Blanco", "Microtúbulos", False), ("Uricemia", "No cambia", False),
          ("Uso", "Crisis", False)],
       "pie": "Profilaxis al iniciar"},
      {"titulo": "Indometacina", "datos": [
          ("Blanco", "COX", False), ("Uricemia", "No cambia", False),
          ("Uso", "Crisis", False)],
       "pie": "AINE"},
      {"titulo": "Furosemida", "datos": [
          ("Blanco", "NKCC2", False), ("Uricemia", "Sube", False),
          ("Riesgo", "Crisis", False)],
       "pie": "Diurético"}]},
  ["Iniciar alopurinol a dosis baja.",
   "Cuidado con azatioprina.",
   "Previene la lisis tumoral."],
  "ACR – Gout management guideline (2020)")

# CB-201 · árbol
A("CB-201", "lavado-gastrico-contraindicado-caustico-alcali", "Cuándo no hacer lavado gástrico",
  "CIENCIAS BÁSICAS ENAM: DESCONTAMINACIÓN", CB,
  ("Lavado gástrico", ["Hoy se usa muy poco",
   "Solo ingesta reciente de un tóxico letal"]),
  ("Pregunta de toxicología", ["¿En qué ingesta está contraindicado?"]),
  Q("¿Es un cáustico?", [
      L("Sí", "CONTRAINDICADO", ["Álcalis o ácidos", "Riesgo de perforación"], path=True),
      Q("¿Es un hidrocarburo?", [
          L("Sí", "Contraindicado", ["Aspiración"]),
          L("No", "Valorar", ["Primera hora, vía aérea"])], edge="No")], path=True),
  ("Ante un cáustico", [("Hacer", True), ("Evitar", False)], [
      ("Primero", ["Vía aérea", "Inducir vómito"]),
      ("Luego", ["Endoscopía 12-48 h", "Carbón activado"])]),
  ["Aspirina, diazepam, barbitúricos: no lo contraindican.",
   "Álcalis: necrosis por licuefacción.",
   "No neutralizar el cáustico."],
  TOXI)

# CB-202 · embudo
V("embudo", "CB-202", "bradicardia-50-miosis-sudoracion-peristaltismo-organofosforado", "Diagnóstico ante miosis y bradicardia",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIONES", CB,
  ("Signos muscarínicos", ["Bradicardia, miosis, sudoración",
   "Aumento del peristaltismo"]),
  ("Varón de 32 años", ["FC 50 lpm, miosis, sudoración", "Peristaltismo aumentado"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Intoxicación posible",
   "candidatos": ["Organofosforado", "Cocaína", "Botulismo", "Arsénico"],
   "pasos": [("Hay miosis y bradicardia", ["Cocaína"]),
             ("Hay exceso de acetilcolina", ["Botulismo", "Arsénico"])],
   "final": ("ORGANOFOSFORADO", ["Inhibe la acetilcolinesterasa", "Síndrome muscarínico"]),
   "nota": "Botulismo: midriasis, sequedad y parálisis descendente."},
  ["Cocaína: taquicardia, midriasis, HTA.",
   "Arsénico: gastroenteritis y QT largo.",
   "Mercurio: temblor y gingivitis."],
  TOXI)

# CB-203 · radial
V("radial", "CB-203", "eritromicina-qt-largo-canales-herg-torsades", "Efectos de los macrólidos",
  "CIENCIAS BÁSICAS ENAM: MACRÓLIDOS", CB,
  ("Macrólidos", ["Eritromicina, claritromicina, azitromicina",
   "Bloquean canales de potasio hERG"]),
  ("Pregunta de farmacología", ["¿Qué puede producir la eritromicina?"]),
  {"rotulo": "Mapa del tema", "centro": "ERITROMICINA", "centro_sub": "Efectos", "ans": 0,
   "items": [("QT LARGO", ["Torsades de pointes"]),
             ("Motilina", ["Cólicos", "Procinético"]),
             ("CYP3A4", ["Inhibe: estatinas", "warfarina"]),
             ("Estolato", ["Hepatitis colestásica"]),
             ("Riesgo QT", ["Hipo K, hipo Mg"])],
   "ruta": ["Eritromicina", "Bloquea hERG", "Repolarización lenta", "QT LARGO"]},
  ["Azitromicina: menor riesgo, no nulo.",
   "Evitar con antipsicóticos y quinolonas.",
   "No produce onda delta ni bloqueo AV."],
  GOODMAN)

# CB-204 · árbol
A("CB-204", "nino-kerosene-asintomatico-observar-6-horas-radiografia", "Ingesta de hidrocarburos",
  "CIENCIAS BÁSICAS ENAM: HIDROCARBUROS", CB,
  ("Hidrocarburos", ["El riesgo es la neumonitis por aspiración",
   "Nunca inducir el vómito"]),
  ("Niño de 3 años", ["Bebió kerosene hace 1 hora", "Asintomático, pulmones y saturación normales"]),
  Q("¿Tiene síntomas respiratorios?", [
      L("No", "OBSERVAR 6 HORAS", ["Con radiografía de tórax", "Alta si sigue normal"], path=True),
      L("Sí", "Hospitalizar", ["Oxígeno", "Ventilación si es grave"])], path=True),
  ("Qué evitar", [("Medida", True), ("Motivo", False)], [
      ("Vómito o lavado", ["Inducir", "Aspiración"]),
      ("Aceite o carbón", ["Dar", "No sirven"])]),
  ["Sin antibióticos ni corticoides de rutina.",
   "La radiografía puede tardar en alterarse.",
   "Tos o taquipnea: signos de aspiración."],
  NELSON)

# CB-205 · termómetro
V("termometro", "CB-205", "fractura-diafisis-humero-canal-torsion-nervio-radial", "Nervios según el nivel de fractura",
  "CIENCIAS BÁSICAS ENAM: FRACTURAS DEL HÚMERO", CB,
  ("Húmero y nervios", ["Cada nivel pone en riesgo un nervio",
   "El radial rodea la diáfisis por el canal de torsión"]),
  ("Pregunta de anatomía", ["Fractura del canal de torsión", "¿Qué nervio se lesiona?"]),
  {"rotulo": "Niveles del húmero",
   "niveles": [("Cuello", "Quirúrgico", ["Axilar (circunflejo)"]),
               ("Diáfisis media", "Canal de torsión", ["NERVIO RADIAL"]),
               ("Supracondílea", "Distal", ["Mediano, braquial"]),
               ("Epitróclea", "Medial", ["Cubital"])],
   "caso_nivel": 1, "ruta_titulo": "Lesión del radial", "paso_label": "PASO",
   "pasos": [(1, "Mano caída", ["No extiende muñeca"], True),
             (2, "Tríceps conservado", ["Ramas altas"], False),
             (3, "Neuroapraxia", ["Recupera en 3-4 meses"], False)]},
  ["Fractura de Holstein-Lewis: tercio distal.",
   "Hipoestesia en el dorso de la 1.ª comisura.",
   "Férula de muñeca en extensión."],
  MOORE)

# CB-206 · matriz
V("matriz", "CB-206", "canal-epitrocleo-olecraniano-nervio-cubital-tunel", "Nervios del codo",
  "CIENCIAS BÁSICAS ENAM: NERVIOS DEL CODO", CB,
  ("Nervios en el codo", ["Cubital: detrás de la epitróclea",
   "Mediano y radial: por delante"]),
  ("Pregunta de anatomía", ["Lesión del canal epitrócleo-olecraniano"]),
  {"rotulo": "Nervio y sitio", "eje_x": "Dato", "eje_y": "Nervio",
   "cols": ["Sitio", "Signo"], "rows": ["Radial", "Mediano", "Cubital"], "caso": (2, 0),
   "cells": [[("Canal de torsión", []), ("Mano caída", [])],
             [("Túnel carpiano", []), ("Mano de predicador", [])],
             [("EPITRÓCLEO-OLECRANIANO", ["Túnel cubital"]), ("Mano en garra", ["4.º y 5.º dedos"])]]},
  ["«Hueso de la risa»: nervio cubital.",
   "Empeora con el codo flexionado.",
   "Froment: debilidad del aductor."],
  MOORE)

# CB-207 · fases
V("fases", "CB-207", "raticida-hidroxicumarina-fitomenadiona-vitamina-k1", "Intoxicación por raticidas cumarínicos",
  "CIENCIAS BÁSICAS ENAM: CUMARÍNICOS", CB,
  ("Rodenticidas cumarínicos", ["Bloquean la vitamina K epóxido reductasa",
   "Caen los factores II, VII, IX y X"]),
  ("Mujer de 20 años", ["Ingiere un raticida con hidroxicumarina", "¿Terapia específica?"]),
  {"rotulo": "Evolución tras la ingesta", "ans": 1,
   "fases": [("Ingesta", "Horas", "Sin síntomas", ["INR aún normal"]),
             ("24-72 horas", "Factores bajan", "VITAMINA K1", ["Fitomenadiona", "Semanas"]),
             ("Sangrado", "Grave", "Complejo protrombínico", ["O plasma fresco"])],
   "chips_titulo": "Terapia específica · marcada la correcta",
   "chips": [("Fitomenadiona", True), ("Factor VIII", False), ("Lavado gástrico", False), ("Atropina", False)]},
  ["Supercumarinas: efecto por meses.",
   "Controlar el INR.",
   "El factor VIII no depende de la vitamina K."],
  TOXI)

# CB-208 · embudo
V("embudo", "CB-208", "pozo-septico-acido-sulfhidrico-knockdown", "Gases tóxicos",
  "CIENCIAS BÁSICAS ENAM: GASES TÓXICOS", CB,
  ("Ácido sulfhídrico (H2S)", ["Descomposición de materia orgánica",
   "Olor a huevo podrido que luego no se percibe"]),
  ("Varón de 25 años en un pozo séptico", ["Irritación de mucosas, cianosis, disnea", "Pierde la conciencia"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Gas en un espacio cerrado",
   "candidatos": ["Ácido sulfhídrico", "Monóxido de carbono", "Cianuro", "Vapores nitrosos"],
   "pasos": [("Irrita mucosas", ["Monóxido de carbono", "Cianuro"]),
             ("Pozo séptico: materia orgánica", ["Vapores nitrosos"])],
   "final": ("ÁCIDO SULFHÍDRICO", ["Bloquea la citocromo oxidasa", "Oxígeno al 100 % y soporte"]),
   "nota": "Rescatistas sin equipo también caen."},
  ["Paraliza el olfato a concentraciones altas.",
   "Puede causar edema pulmonar.",
   "Monóxido: no irrita, piel rojo cereza."],
  TOXI)

# CB-209 · termómetro
V("termometro", "CB-209", "nino-3-anos-miosis-sialorrea-roncantes-atropina-ev", "Gravedad de la intoxicación colinérgica",
  "CIENCIAS BÁSICAS ENAM: ORGANOFOSFORADOS", CB,
  ("Intoxicación colinérgica", ["La gravedad la marcan las secreciones",
   "y la respiración"]),
  ("Niño de 3 años", ["Miosis, sialorrea, fasciculaciones", "Roncantes pulmonares bilaterales"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "Muscarínico", ["Náuseas, miosis"]),
               ("Moderada", "Con broncorrea", ["ESTE CASO", "Roncantes"]),
               ("Grave", "Respiratoria", ["Hipoxemia, coma"]),
               ("Crítica", "Paro", ["Convulsiones"])],
   "caso_nivel": 1, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Atropina EV", ["0,02-0,05 mg/kg"], True),
             (2, "Duplicar c/5 min", ["Hasta secar"], True),
             (3, "Pralidoxima", ["Si es organofosforado"], False)]},
  ["Fisostigmina empeoraría el cuadro.",
   "Naloxona: solo opioides.",
   "Descontaminar la piel y la ropa."],
  TOXI)

# CB-210 · fases
V("fases", "CB-210", "embriaguez-brazo-sobre-mesa-mano-caida-radial", "Parálisis del «sábado por la noche»",
  "CIENCIAS BÁSICAS ENAM: NERVIO RADIAL", CB,
  ("Compresión del nervio radial", ["Contra el húmero, en el canal de torsión",
   "Neuroapraxia por presión prolongada"]),
  ("Varón de 28 años", ["Durmió ebrio apoyado sobre una mesa", "No extiende la muñeca ni los dedos"]),
  {"rotulo": "Evolución", "ans": 1,
   "fases": [("Noche", "Horas", "Compresión", ["Sin cambiar de posición"]),
             ("Mañana", "Lesión", "RADIAL", ["Mano caída", "Dorso de la 1.ª comisura"]),
             ("Semanas", "Recupera", "Neuroapraxia", ["Férula y fisioterapia"])],
   "chips_titulo": "Nervio · marcado el correcto",
   "chips": [("Radial", True), ("Cubital", False), ("Mediano", False), ("Axilar", False)]},
  ["El alcohol anula el reflejo de moverse.",
   "Tríceps conservado.",
   "Pronóstico excelente."],
  MOORE)

# CB-211 · matriz
V("matriz", "CB-211", "vagina-proximal-conductos-muller-seno-urogenital", "Origen del aparato genital femenino",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA DE LA VAGINA", CB,
  ("Origen de la vagina", ["Parte superior: conductos de Müller",
   "Parte inferior: seno urogenital"]),
  ("Pregunta de embriología", ["¿De dónde viene la parte proximal de la vagina?"]),
  {"rotulo": "Estructura y origen", "eje_x": "Dato", "eje_y": "Estructura",
   "cols": ["Origen", "Anomalía"], "rows": ["Útero y trompas", "Vagina superior", "Vagina inferior"], "caso": (1, 0),
   "cells": [[("Müller", []), ("Útero bicorne", ["Didelfo"])],
             [("MÜLLER", ["Fusionados"]), ("Agenesia", ["Rokitansky"])],
             [("Seno urogenital", []), ("Himen imperforado", ["Tabique transverso"])]]},
  ["Wolff involuciona en la mujer.",
   "Resto: conducto de Gartner.",
   "El himen separa ambos orígenes."],
  LANGMAN)

# CB-212 · árbol
A("CB-212", "nino-neumonia-sarm-teicoplanina-vancomicina", "Antibiótico en la neumonía estafilocócica",
  "CIENCIAS BÁSICAS ENAM: SARM", CB,
  ("S. aureus resistente a meticilina", ["PBP2a: resiste todos los betalactámicos",
   "Tratamiento: glucopéptidos o linezolid"]),
  ("Niño con neumonía estafilocócica", ["Resistente a meticilina", "¿Antibiótico de elección?"]),
  Q("¿Sensible a meticilina?", [
      L("Sí (SAMS)", "Oxacilina", ["O cefazolina"]),
      L("No (SARM)", "GLUCOPÉPTIDO", ["Vancomicina o teicoplanina", "Alternativa: linezolid"], path=True)], path=True),
  ("Opciones que fallan", [("Fármaco", True), ("Motivo", False)], [
      ("Ceftriaxona", ["Betalactámico", "PBP2a"]),
      ("Dicloxacilina", ["Betalactámico", "PBP2a"])]),
  ["Drenar el empiema si existe.",
   "Vigilar neumatoceles.",
   "Clindamicina solo en cepas sensibles y leves."],
  SANFORD)
