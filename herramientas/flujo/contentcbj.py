"""Ciencias Básicas · parte J (CB-453 a CB-485)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-453 · tarjetas
V("tarjetas", "CB-453", "testosterona-celulas-leydig-intersticio-lh", "Células productoras de hormonas",
  "CIENCIAS BÁSICAS ENAM: CÉLULAS DE LEYDIG", CB,
  ("Testículo endocrino", ["Leydig: testosterona, en el intersticio",
   "Sertoli: dentro del túbulo"]),
  ("Pregunta de histología", ["¿Qué célula produce la testosterona?"]),
  {"rotulo": "¿Qué produce?", "ans": 0, "cards": [
      {"titulo": "LEYDIG", "datos": [
          ("Produce", "Testosterona", True), ("Estímulo", "LH", True),
          ("Sitio", "Intersticio", True)],
       "pie": "Cristales de Reinke"},
      {"titulo": "Sertoli", "datos": [
          ("Produce", "Inhibina, AMH", False), ("Estímulo", "FSH", False),
          ("Sitio", "Túbulo", False)],
       "pie": "Sostén germinal"},
      {"titulo": "Paneth", "datos": [
          ("Produce", "Defensinas", False), ("Órgano", "Intestino", False),
          ("Sitio", "Criptas", False)],
       "pie": "Lisozima"},
      {"titulo": "Germinativas", "datos": [
          ("Producen", "Espermatozoides", False), ("Inicio", "Pubertad", False),
          ("Sitio", "Túbulo", False)],
       "pie": "Espermatogonias"}]},
  ["DHT en próstata y piel.",
   "Tumor de Leydig: pubertad precoz.",
   "La testosterona intratesticular es muy alta."],
  ROSS)

# CB-454 · matriz
V("matriz", "CB-454", "pancreas-exocrino-acinos-serosos-zimogeno", "Tipos de glándulas exocrinas",
  "CIENCIAS BÁSICAS ENAM: GLÁNDULAS EXOCRINAS", CB,
  ("Glándulas exocrinas", ["Serosas: secreción acuosa rica en enzimas",
   "Mucosas: moco espeso"]),
  ("Pregunta de histología", ["¿De qué tipo son los acinos del páncreas?"]),
  {"rotulo": "Glándula y secreción", "eje_x": "Dato", "eje_y": "Glándula",
   "cols": ["Tipo", "Producto"], "rows": ["Páncreas", "Parótida", "Sublingual"], "caso": (0, 0),
   "cells": [[("SEROSA", ["Gránulos de zimógeno"]), ("Enzimas", ["Tripsinógeno, lipasa"])],
             [("Serosa", []), ("Amilasa", [])],
             [("Mucosa", ["Predominio"]), ("Moco", [])]]},
  ["Centroacinares: bicarbonato.",
   "CCK estimula enzimas.",
   "Secretina estimula bicarbonato."],
  ROSS)

# CB-455 · embudo
V("embudo", "CB-455", "vesicula-biliar-epitelio-cilindrico-simple-rokitansky", "Epitelio de la vesícula biliar",
  "CIENCIAS BÁSICAS ENAM: VESÍCULA BILIAR", CB,
  ("Vesícula biliar", ["Concentra la bilis 5-10 veces",
   "Epitelio cilíndrico simple"]),
  ("Pregunta de histología", ["¿Qué epitelio reviste la vesícula?"]),
  {"rotulo": "Embudo histológico",
   "inicio": "Cinco epitelios",
   "candidatos": ["Cilíndrico simple", "Pseudoestratificado", "Cúbico simple", "Plano estratificado"],
   "pasos": [("Es simple, no estratificado", ["Pseudoestratificado", "Plano estratificado"]),
             ("Células altas que absorben", ["Cúbico simple"])],
   "final": ("CILÍNDRICO SIMPLE", ["Con microvellosidades", "Absorbe agua y electrolitos"]),
   "nota": "Sin muscular de la mucosa ni submucosa."},
  ["Senos de Rokitansky-Aschoff.",
   "Vesícula en porcelana: riesgo de cáncer.",
   "Tumores invaden pronto."],
  ROSS)

# CB-456 · radial
V("radial", "CB-456", "adenopatia-inguinal-carcinoma-escamoso-canal-anal", "Drenaje de los ganglios inguinales",
  "CIENCIAS BÁSICAS ENAM: DRENAJE LINFÁTICO", CB,
  ("Ganglios inguinales", ["Drenan piel, genitales externos, ano bajo",
   "y miembro inferior"]),
  ("Varón de 63 años", ["Ganglio inguinal duro de 1,5 cm", "Biopsia: carcinoma escamoso"]),
  {"rotulo": "Mapa del tema", "centro": "INGUINALES", "centro_sub": "Ganglios", "ans": 0,
   "items": [("CANAL ANAL", ["Bajo la línea", "pectínea: escamoso"]),
             ("Genitales externos", ["Pene, escroto, vulva"]),
             ("Piel", ["Abdomen bajo, periné"]),
             ("No drenan", ["Testículo: paraaórticos"]),
             ("Recto, próstata", ["Ganglios pélvicos"])],
   "ruta": ["Carcinoma escamoso", "Ganglio inguinal", "Territorio escamoso", "ANO"]},
  ["VPH 16 en el cáncer anal.",
   "Recto y sigmoides: adenocarcinoma.",
   "Tercio inferior de vagina: inguinales."],
  MOORE)

# CB-457 · termómetro
V("termometro", "CB-457", "reaccion-leucemoide-neutrofilica-hemorragia-hemolisis", "Reacción leucemoide",
  "CIENCIAS BÁSICAS ENAM: LEUCOCITOSIS", CB,
  ("Reacción leucemoide", ["Leucocitosis reactiva > 50 000/µL",
   "Puede confundirse con leucemia"]),
  ("Pregunta de hematología", ["¿Dónde se observa una reacción leucemoide", "neutrofílica?"]),
  {"rotulo": "Leucocitos por µL",
   "niveles": [("4000-11 000", "Normal", ["Fórmula habitual"]),
               ("11 000-50 000", "Leucocitosis", ["Infección común"]),
               ("> 50 000", "LEUCEMOIDE", ["Hemorragia, hemólisis", "Sepsis grave"]),
               ("Blastos", "Leucemia", ["Clonal"])],
   "caso_nivel": 2, "ruta_titulo": "Diferenciar de LMC", "paso_label": "PASO",
   "pasos": [(1, "Fosfatasa alcalina", ["Alta en leucemoide"], True),
             (2, "BCR-ABL", ["Ausente"], True),
             (3, "Sin basofilia", ["Reactiva"], False)]},
  ["Mononucleosis: linfocitos atípicos.",
   "Parásitos: eosinofilia.",
   "Tumores con G-CSF también."],
  HARRISON)

# CB-458 · fases
V("fases", "CB-458", "infeccion-subclinica-seroconversion-titulos-anticuerpos", "Espectro de la infección",
  "CIENCIAS BÁSICAS ENAM: EPIDEMIOLOGÍA DE LA INFECCIÓN", CB,
  ("Infección subclínica", ["No hay signos ni síntomas",
   "Solo se detecta por laboratorio"]),
  ("Pregunta de microbiología", ["¿Qué indica una infección subclínica?"]),
  {"rotulo": "Del contacto a la clínica", "ans": 1,
   "fases": [("Exposición", "Contacto", "Agente", ["Puede no infectar"]),
             ("Subclínica", "Sin síntomas", "ANTICUERPOS", ["Suben o bajan", "Seroconversión"]),
             ("Clínica", "Síntomas", "Enfermedad", ["Signos visibles"])],
   "chips_titulo": "Indicador · marcado el correcto",
   "chips": [("Cambio de anticuerpos", True), ("Aislar el agente", False), ("Síntomas", False), ("Infectividad", False)]},
  ["Cambio de 4 veces en sueros pareados.",
   "Transmiten sin saberlo.",
   "Polio, hepatitis A en niños."],
  "Gordis. Epidemiología 6.ª ed. (2019)")

# CB-459 · radial
V("radial", "CB-459", "macrofago-inmunidad-innata-fagocitosis-citocinas", "Componentes de la inmunidad innata",
  "CIENCIAS BÁSICAS ENAM: INMUNIDAD INNATA", CB,
  ("Inmunidad innata", ["Barreras, células y moléculas",
   "El macrófago fagocita y secreta citocinas"]),
  ("Pregunta de inmunología", ["¿Qué componente fagocita y secreta citocinas?"]),
  {"rotulo": "Mapa del tema", "centro": "INNATA", "centro_sub": "Inmunidad", "ans": 0,
   "items": [("MACRÓFAGO", ["Fagocita", "TNF, IL-1, IL-6"]),
             ("Epitelio", ["Barrera física"]),
             ("TNF-alfa", ["Molécula, no célula"]),
             ("Lectina", ["Activa complemento"]),
             ("Receptores Toll", ["Reconocen PAMP"])],
   "ruta": ["Microbio", "Receptor Toll", "Fagocitosis", "CITOCINAS"]},
  ["Presenta antígenos a los linfocitos T.",
   "Une innata y adaptativa.",
   "Neutrófilos: primera línea."],
  ABBAS)

# CB-460 · puntaje
V("puntaje", "CB-460", "esplenomegalia-masiva-linfomas-lmc-mielofibrosis", "Tamaño del bazo",
  "CIENCIAS BÁSICAS ENAM: ESPLENOMEGALIA", CB,
  ("Esplenomegalia masiva", ["Bazo > 1000-1500 g o que cruza la línea media",
   "Causas limitadas"]),
  ("Pregunta de hematología", ["¿Dónde hay esplenomegalia masiva?"]),
  {"rotulo": "Peso del bazo", "escala": "Gramos", "total": 1500, "max": 2000,
   "total_label": "Masiva",
   "interpreta": "Linfomas, LMC, mielofibrosis",
   "items": [("Normal", "≈ 150 g", False), ("Moderada", "500 g", False), ("Masiva", "> 1500 g", True)],
   "bandas": [("< 500 g", "Leve", "Sepsis, ICC", False),
              ("500-1500", "Moderada", "Tuberculosis", False),
              ("> 1500 g", "Masiva", "Linfoma, LMC", True)]},
  ["También malaria y kala-azar.",
   "Enfermedad de Gaucher.",
   "Riesgo: infartos e hiperesplenismo."],
  HARRISON)

# CB-461 · tarjetas
V("tarjetas", "CB-461", "ige-anafilaxia-atopia-mastocitos-fceri", "Clases de inmunoglobulinas",
  "CIENCIAS BÁSICAS ENAM: INMUNOGLOBULINAS", CB,
  ("Inmunoglobulinas", ["Cada clase tiene una función",
   "La IgE media la alergia inmediata"]),
  ("Pregunta de inmunología", ["¿Qué inmunoglobulina está alta en la atopia?"]),
  {"rotulo": "¿Qué hace cada una?", "ans": 0, "cards": [
      {"titulo": "IgE", "datos": [
          ("Función", "Alergia, parásitos", True), ("Receptor", "FcεRI", True),
          ("Célula", "Mastocito", True)],
       "pie": "Omalizumab: anti-IgE"},
      {"titulo": "IgG", "datos": [
          ("Función", "Memoria", False), ("Placenta", "La cruza", False),
          ("Nivel", "La más abundante", False)],
       "pie": "Opsonina"},
      {"titulo": "IgM", "datos": [
          ("Función", "Infección inicial", False), ("Forma", "Pentámero", False),
          ("Complemento", "Lo activa", False)],
       "pie": "Infección aguda"},
      {"titulo": "IgA", "datos": [
          ("Función", "Mucosas", False), ("Forma", "Dímero", False),
          ("Extra", "Leche materna", False)],
       "pie": "IgD: receptor B"}]},
  ["Th2 e IL-4 favorecen la IgE.",
   "Triptasa: activación de mastocitos.",
   "Helmintos también suben la IgE."],
  ABBAS)

# CB-462 · radial
V("radial", "CB-462", "bacteroides-fragilis-capsula-zwitterionica-abscesos", "Virulencia de Bacteroides fragilis",
  "CIENCIAS BÁSICAS ENAM: BACTEROIDES", CB,
  ("Bacteroides fragilis", ["Flora normal del colon",
   "Fuera de su sitio forma abscesos"]),
  ("Pregunta de microbiología", ["¿Qué componente induce los abscesos?"]),
  {"rotulo": "Mapa del tema", "centro": "B. FRAGILIS", "centro_sub": "Virulencia", "ans": 0,
   "items": [("CÁPSULA", ["Zwitteriónica", "Induce abscesos"]),
             ("Betalactamasa", ["Resiste penicilinas"]),
             ("LPS", ["Poca endotoxina"]),
             ("Tratamiento", ["Drenar + metronidazol"]),
             ("Origen", ["Perforación intestinal"])],
   "ruta": ["Perforación", "Sale del colon", "Cápsula", "ABSCESO"]},
  ["Activa linfocitos T e IL-17.",
   "Inhibe la fagocitosis.",
   "Carbapenémicos también sirven."],
  MURRAY)

# CB-463 · árbol
A("CB-463", "neonato-meningitis-cocobacilos-grampositivos-listeria", "Meningitis neonatal según el Gram",
  "CIENCIAS BÁSICAS ENAM: MENINGITIS NEONATAL", CB,
  ("Meningitis neonatal", ["Estreptococo B, E. coli y Listeria",
   "El Gram orienta al germen"]),
  ("Neonato con meningitis", ["LCR: cocobacilos grampositivos", "Intra y extracelulares"]),
  Q("¿Qué muestra el Gram?", [
      L("Bacilos gram +", "LISTERIA", ["Resiste cefalosporinas", "Dar ampicilina"], path=True),
      L("Cocos gram + en cadena", "Estreptococo B", ["S. agalactiae"]),
      L("Bacilos gram −", "E. coli", ["Klebsiella"])], path=True),
  ("Esquema empírico", [("Edad", True), ("Antibióticos", False)], [
      ("< 1 mes", ["Neonato", "Ampicilina + cefotaxima"]),
      ("1-3 meses", ["Lactante", "Igual, cubrir Listeria"])]),
  ["Madre: lácteos sin pasteurizar.",
   "También en mayores de 50 años.",
   "E. coli con antígeno K1."],
  NELSON)

# CB-464 · árbol
A("CB-464", "nino-3-anos-meningitis-cocobacilos-gramnegativos-hib", "Meningitis infantil según el Gram",
  "CIENCIAS BÁSICAS ENAM: MENINGITIS BACTERIANA", CB,
  ("Meningitis en niños", ["Neumococo, meningococo y Hib",
   "El Gram orienta"]),
  ("Niño de 3 años con meningitis", ["LCR: cocobacilos gramnegativos"]),
  Q("¿Qué muestra el Gram?", [
      L("Cocobacilos gram −", "H. INFLUENZAE", ["Tipo b", "Revisar vacunas"], path=True),
      L("Diplococos gram +", "Neumococo", ["El más común hoy"]),
      L("Diplococos gram −", "Meningococo", ["Petequias"])], path=True),
  ("Manejo", [("Medida", True), ("Detalle", False)], [
      ("Antibiótico", ["Ceftriaxona", "O cefotaxima"]),
      ("Dexametasona", ["Antes o con la dosis", "Menos sordera"])]),
  ["Vacuna pentavalente: Hib.",
   "Contactos: rifampicina.",
   "Secuela típica: hipoacusia."],
  NELSON)

# CB-465 · fases
V("fases", "CB-465", "vibrio-cholerae-toxina-gangliosido-gm1-ampc", "Mecanismo de la toxina colérica",
  "CIENCIAS BÁSICAS ENAM: CÓLERA", CB,
  ("Toxina colérica", ["Toxina AB5",
   "Las subunidades B se unen al gangliósido GM1"]),
  ("Paciente que llega de la selva", ["Diarrea acuosa abundante, vómitos", "Hipotensión · cultivo: V. cholerae"]),
  {"rotulo": "Secuencia", "ans": 0,
   "fases": [("Unión", "Subunidad B", "GANGLIÓSIDO GM1", ["Receptor de membrana"]),
             ("Entrada", "Subunidad A", "Gs activada", ["Ribosilación ADP"]),
             ("Efecto", "AMPc alto", "Diarrea", ["CFTR secreta cloro", "Agua de arroz"])],
   "chips_titulo": "Receptor · marcado el correcto",
   "chips": [("Gangliósido GM1", True), ("GM2", False), ("Proteína G", False), ("PDGF", False)]},
  ["Hasta 1 litro por hora.",
   "Rehidratar es lo principal.",
   "Epidemia en el Perú en 1991."],
  MURRAY)

# CB-466 · matriz
V("matriz", "CB-466", "lcr-linfocitario-hipoglucorraquia-meningitis-tuberculosa", "Patrones del LCR",
  "CIENCIAS BÁSICAS ENAM: LÍQUIDO CEFALORRAQUÍDEO", CB,
  ("Líquido cefalorraquídeo", ["Células, glucosa y proteínas",
   "Cada meningitis tiene su patrón"]),
  ("Paciente inmunocompetente", ["Cefalea y fiebre de 3 semanas, diplopía", "LCR linfocitario, glucosa baja, proteínas altas"]),
  {"rotulo": "Patrón del LCR", "eje_x": "Dato", "eje_y": "Causa",
   "cols": ["Células", "Glucosa"], "rows": ["Bacteriana", "Viral", "Tuberculosa"], "caso": (2, 1),
   "cells": [[("Neutrófilos", ["Miles"]), ("Muy baja", [])],
             [("Linfocitos", []), ("Normal", [])],
             [("Linfocitos", ["Cientos"]), ("BAJA", ["Proteínas muy altas"])]]},
  ["ADA alta en el LCR.",
   "GeneXpert y cultivo.",
   "VIH: descartar criptococo."],
  HARRISON)

# CB-467 · embudo
V("embudo", "CB-467", "shock-toxico-estafilococico-tsst1-superantigeno", "Toxina del shock tóxico",
  "CIENCIAS BÁSICAS ENAM: TOXINAS ESTAFILOCÓCICAS", CB,
  ("Toxinas de S. aureus", ["Cada toxina causa un cuadro",
   "TSST-1: shock tóxico"]),
  ("Pregunta de microbiología", ["¿Qué sustancia causa el shock tóxico?"]),
  {"rotulo": "Embudo de toxinas",
   "inicio": "Productos de S. aureus",
   "candidatos": ["TSST-1", "Coagulasa", "Exfoliativa", "Leucocidina"],
   "pasos": [("Es un superantígeno", ["Coagulasa", "Leucocidina"]),
             ("Da shock, no piel escaldada", ["Exfoliativa"])],
   "final": ("TSST-1", ["Activa hasta 20 % de linfocitos T", "Tormenta de citocinas"]),
   "nota": "Exfoliativa: síndrome de piel escaldada."},
  ["Fiebre, hipotensión, eritrodermia.",
   "Descamación de palmas y plantas.",
   "Añadir clindamicina."],
  MURRAY)

# CB-468 · puntaje
V("puntaje", "CB-468", "flora-colonica-anaerobios-bacteroides-predominante", "Flora del colon",
  "CIENCIAS BÁSICAS ENAM: MICROBIOTA", CB,
  ("Microbiota del colon", ["10¹¹ a 10¹² bacterias por gramo",
   "Más del 99 % son anaerobias"]),
  ("Pregunta de microbiología", ["¿Especie predominante en el colon?"]),
  {"rotulo": "Composición", "escala": "%", "total": 99, "max": 100,
   "total_label": "Anaerobios",
   "interpreta": "Bacteroides predomina",
   "items": [("Anaerobios", "> 99 %", True), ("Relación", "1000 : 1", True), ("E. coli", "Minoritaria", False)],
   "bandas": [("< 1 %", "Facultativos", "E. coli, enterococo", False),
              ("> 99 %", "Anaerobios", "Bacteroides", True),
              ("Clave", "Funciones", "Vitamina K, butirato", False)]},
  ["Perforación: infección polimicrobiana.",
   "Bifidobacterium también abunda.",
   "Protege contra patógenos."],
  MURRAY)

# CB-469 · tarjetas
V("tarjetas", "CB-469", "staphylococcus-aureus-capsula-antifagocitica-virulencia", "Factores de virulencia de S. aureus",
  "CIENCIAS BÁSICAS ENAM: STAPHYLOCOCCUS AUREUS", CB,
  ("Virulencia de S. aureus", ["Superficie, enzimas y toxinas",
   "La cápsula evita la fagocitosis"]),
  ("Pregunta de microbiología", ["¿Qué inhibe la opsonización y fagocitosis?"]),
  {"rotulo": "¿Qué hace?", "ans": 0, "cards": [
      {"titulo": "CÁPSULA", "datos": [
          ("Efecto", "Antifagocítica", True), ("Mecanismo", "Oculta opsoninas", True),
          ("Serotipos", "5 y 8", True)],
       "pie": "Polisacárido"},
      {"titulo": "Proteína A", "datos": [
          ("Efecto", "Une Fc de IgG", False), ("Resultado", "Menos opsonización", False),
          ("Sitio", "Pared", False)],
       "pie": "También antifagocítica"},
      {"titulo": "Coagulasa", "datos": [
          ("Efecto", "Forma fibrina", False), ("Uso", "Identificación", False),
          ("Barrera", "Absceso", False)],
       "pie": "Diferencia de S. epidermidis"},
      {"titulo": "Panton-Valentine", "datos": [
          ("Efecto", "Mata leucocitos", False), ("Clínica", "Neumonía necrot.", False),
          ("Asociada", "SARM comunitario", False)],
       "pie": "Leucocidina"}]},
  ["Ácido teicoico: adherencia.",
   "Peptidoglicano: activa complemento.",
   "Membrana: no es factor antifagocítico."],
  MURRAY)

# CB-470 · embudo
V("embudo", "CB-470", "campylobacter-jejuni-guillain-barre-mimetismo", "Campylobacter y Guillain-Barré",
  "CIENCIAS BÁSICAS ENAM: CAMPYLOBACTER", CB,
  ("Guillain-Barré posinfeccioso", ["Mimetismo molecular con gangliósidos",
   "C. jejuni es la infección previa más común"]),
  ("Pregunta de microbiología", ["¿Qué especie de Campylobacter se asocia?"]),
  {"rotulo": "Embudo de especies",
   "inicio": "Especies de Campylobacter",
   "candidatos": ["C. jejuni", "C. fetus", "C. coli", "C. lari"],
   "pasos": [("Causa diarrea común", ["C. fetus"]),
             ("Lipooligosacárido tipo GM1", ["C. coli", "C. lari"])],
   "final": ("C. JEJUNI", ["25-40 % de los Guillain-Barré", "Forma axonal AMAN"]),
   "nota": "C. fetus: bacteriemia en inmunodeprimidos."},
  ["Brote en el Perú en 2019.",
   "1 a 3 semanas tras la diarrea.",
   "Inmunoglobulina IV o plasmaféresis."],
  MURRAY)

# CB-471 · matriz
V("matriz", "CB-471", "estreptolisina-s-no-inmunogena-o-aso", "Estreptolisinas O y S",
  "CIENCIAS BÁSICAS ENAM: STREPTOCOCCUS PYOGENES", CB,
  ("Hemolisinas del estreptococo A", ["Estreptolisina O: lábil al oxígeno",
   "Estreptolisina S: estable, no inmunógena"]),
  ("Pregunta de microbiología", ["¿Qué característica no tiene la estreptolisina S?"]),
  {"rotulo": "Comparación", "eje_x": "Toxina", "eje_y": "Rasgo",
   "cols": ["Estreptolisina O", "Estreptolisina S"], "rows": ["Oxígeno", "Inmunógena", "Hemólisis"], "caso": (1, 1),
   "cells": [[("Lábil", []), ("Estable", [])],
             [("Sí: ASO", ["Fiebre reumática"]), ("NO", ["Sin anticuerpos"])],
             [("Profunda", []), ("Beta en agar", ["Lisa eritrocitos", "y leucocitos"])]]},
  ["ASO: infección reciente.",
   "Estreptolisina S daña lisosomas.",
   "También lisa plaquetas."],
  MURRAY)

# CB-472 · radial
V("radial", "CB-472", "helicobacter-pylori-ureasa-amoniaco-virulencia", "Virulencia de Helicobacter pylori",
  "CIENCIAS BÁSICAS ENAM: HELICOBACTER PYLORI", CB,
  ("Helicobacter pylori", ["Sobrevive en el ácido gástrico",
   "La ureasa es clave para colonizar"]),
  ("Pregunta de microbiología", ["¿En qué bacteria la ureasa indica virulencia?"]),
  {"rotulo": "Mapa del tema", "centro": "H. PYLORI", "centro_sub": "Virulencia", "ans": 0,
   "items": [("UREASA", ["Amoníaco neutraliza", "el ácido"]),
             ("Flagelos", ["Llega al moco"]),
             ("CagA", ["Oncoproteína"]),
             ("VacA", ["Citotoxina"]),
             ("Diagnóstico", ["Aliento con urea", "Ureasa rápida"])],
   "ruta": ["Urea gástrica", "Ureasa", "Amoníaco", "SOBREVIVE"]},
  ["Úlcera, cáncer gástrico, MALT.",
   "Campylobacter intestinales: sin ureasa clave.",
   "Erradicación: IBP + antibióticos."],
  MURRAY)

# CB-473 · termómetro
V("termometro", "CB-473", "legionella-antigeno-urinario-serogrupo-1", "Pruebas para Legionella",
  "CIENCIAS BÁSICAS ENAM: LEGIONELLA", CB,
  ("Legionella pneumophila", ["Neumonía grave con hiponatremia",
   "Prueba rápida: antígeno en orina"]),
  ("Pregunta de microbiología", ["¿Muestra preferida para el diagnóstico?"]),
  {"rotulo": "Rapidez de la prueba",
   "niveles": [("Semanas", "Serología", ["Retrospectiva"]),
               ("3-5 días", "Cultivo BCYE", ["Referencia"]),
               ("Horas", "PCR", ["Secreciones"]),
               ("Minutos", "ANTÍGENO EN ORINA", ["Serogrupo 1"])],
   "caso_nivel": 3, "ruta_titulo": "Cuándo sospechar", "paso_label": "PASO",
   "pasos": [(1, "Neumonía grave", ["Con hiponatremia"], False),
             (2, "Diarrea, confusión", ["Bradicardia relativa"], False),
             (3, "Antígeno urinario", ["Positivo por semanas"], True)]},
  ["Solo detecta el serogrupo 1.",
   "Aire acondicionado, torres de agua.",
   "Macrólidos o quinolonas."],
  "IDSA/ATS – Community-acquired pneumonia (2019)")

# CB-474 · tarjetas
V("tarjetas", "CB-474", "clostridium-botulinum-neurotoxina-paralisis-flacida", "Especies de Clostridium",
  "CIENCIAS BÁSICAS ENAM: CLOSTRIDIUM", CB,
  ("Género Clostridium", ["Bacilos grampositivos anaerobios",
   "Cada especie tiene su toxina"]),
  ("Pregunta de microbiología", ["¿Qué especie causa un cuadro neurológico?"]),
  {"rotulo": "¿Qué causa?", "ans": 0, "cards": [
      {"titulo": "C. BOTULINUM", "datos": [
          ("Toxina", "Botulínica", True), ("Efecto", "Parálisis flácida", True),
          ("Diana", "SNARE", True)],
       "pie": "Conservas caseras, miel"},
      {"titulo": "C. tetani", "datos": [
          ("Toxina", "Tetanospasmina", False), ("Efecto", "Espástica", False),
          ("Puerta", "Heridas", False)],
       "pie": "También neurológico"},
      {"titulo": "C. difficile", "datos": [
          ("Toxina", "A y B", False), ("Efecto", "Colitis", False),
          ("Riesgo", "Antibióticos", False)],
       "pie": "Pseudomembranas"},
      {"titulo": "C. perfringens", "datos": [
          ("Toxina", "Alfa", False), ("Efecto", "Gangrena gaseosa", False),
          ("Otro", "Intoxicación", False)],
       "pie": "Mionecrosis"}]},
  ["Botulismo: descendente y simétrico.",
   "Midriasis y boca seca.",
   "Antitoxina y ventilación."],
  MURRAY)

# CB-475 · termómetro
V("termometro", "CB-475", "anaerobios-poco-frecuentes-infeccion-urinaria", "Anaerobios según el sitio",
  "CIENCIAS BÁSICAS ENAM: ANAEROBIOS", CB,
  ("Infecciones por anaerobios", ["Nacen de mucosas colonizadas",
   "Boca, colon y tracto genital femenino"]),
  ("Pregunta de microbiología", ["¿Dónde son menos frecuentes los anaerobios?"]),
  {"rotulo": "Frecuencia de anaerobios",
   "niveles": [("Muy baja", "URINARIA", ["Orina oxigenada", "E. coli"]),
               ("Alta", "Genital femenina", ["EPI, endometritis"]),
               ("Alta", "Maxilofacial", ["Odontógena"]),
               ("Muy alta", "Abdominal", ["Partes blandas prof."])],
   "caso_nivel": 0, "ruta_titulo": "Pistas de anaerobios", "paso_label": "PISTA",
   "pasos": [(1, "Mal olor", ["Secreción fétida"], False),
             (2, "Gas en tejidos", ["Crepitación"], False),
             (3, "Necrosis", ["Abscesos"], False)]},
  ["Absceso pulmonar por aspiración.",
   "Periuretrales: anaerobios posibles.",
   "Cubrir con metronidazol."],
  MURRAY)

# CB-476 · árbol
A("CB-476", "clostridioides-difficile-vancomicina-oral-fidaxomicina", "Tratamiento de C. difficile",
  "CIENCIAS BÁSICAS ENAM: COLITIS POR C. DIFFICILE", CB,
  ("Infección por C. difficile", ["Diarrea tras antibióticos",
   "Primera línea: vancomicina oral o fidaxomicina"]),
  ("Pregunta de farmacología", ["¿Antibiótico más eficaz?"]),
  Q("¿Forma fulminante?", [
      L("No", "VANCOMICINA ORAL", ["125 mg c/6 h, 10 días", "O fidaxomicina"], path=True),
      L("Sí", "Vanco oral + metronidazol IV", ["Evaluar cirugía"])], path=True),
  ("Recurrencias", [("Opción", True), ("Detalle", False)], [
      ("Fidaxomicina", ["Menos recaídas", "Macrólido"]),
      ("Trasplante fecal", ["Múltiples recaídas", "Muy eficaz"])]),
  ["Vancomicina IV no llega al colon.",
   "Suspender el antibiótico causal.",
   "Metronidazol: solo si no hay otra."],
  "IDSA/SHEA – C. difficile guideline (2021)")

# CB-477 · matriz
V("matriz", "CB-477", "anopheles-metamorfosis-completa-sin-ninfa", "Ciclos de los vectores",
  "CIENCIAS BÁSICAS ENAM: ENTOMOLOGÍA MÉDICA", CB,
  ("Metamorfosis de insectos", ["Completa: huevo, larva, pupa, adulto",
   "Incompleta: huevo, ninfa, adulto"]),
  ("Pregunta de parasitología", ["¿Qué estadio no tiene Anopheles?"]),
  {"rotulo": "Vector y ciclo", "eje_x": "Dato", "eje_y": "Vector",
   "cols": ["Metamorfosis", "¿Ninfa?"], "rows": ["Anopheles", "Triatomino", "Garrapata"], "caso": (0, 1),
   "cells": [[("Completa", ["Pupa acuática"]), ("NO TIENE", ["Opción correcta"])],
             [("Incompleta", []), ("Sí", ["Chagas"])],
             [("Ácaro", []), ("Sí", [])]]},
  ["Larvas de Anopheles: paralelas al agua.",
   "Solo la hembra pica.",
   "Malaria en Loreto."],
  BOTERO)

# CB-478 · fases
V("fases", "CB-478", "strongyloides-larva-filariforme-penetra-piel-autoinfeccion", "Ciclo de Strongyloides",
  "CIENCIAS BÁSICAS ENAM: ESTRONGILOIDIASIS", CB,
  ("Strongyloides stercoralis", ["Infecta por la piel",
   "Puede autoinfectar al mismo huésped"]),
  ("Pregunta de parasitología", ["¿Cuál es la forma infectante?"]),
  {"rotulo": "Ciclo en el huésped", "ans": 0,
   "fases": [("Piel", "Suelo húmedo", "L. FILARIFORME", ["Penetra la piel", "Al andar descalzo"]),
             ("Pulmón", "Sangre", "Migración", ["Sube y se deglute"]),
             ("Intestino", "Duodeno", "Hembra", ["Larvas rabditiformes"])],
   "chips_titulo": "Forma infectante · marcada",
   "chips": [("Larva filariforme", True), ("Huevo", False), ("L. rabditiforme", False), ("Adulto", False)]},
  ["Hiperinfección con corticoides o HTLV-1.",
   "Heces: larvas, no huevos.",
   "Ivermectina."],
  BOTERO)

# CB-479 · embudo
V("embudo", "CB-479", "sida-pneumocystis-muestras-hemocultivo-inutil", "Muestras para Pneumocystis",
  "CIENCIAS BÁSICAS ENAM: PNEUMOCYSTIS", CB,
  ("Pneumocystis jirovecii", ["No crece en cultivos convencionales",
   "Se busca en muestras respiratorias"]),
  ("Paciente con sida y neumonía", ["Sospecha de Pneumocystis", "¿Qué muestra no es útil?"]),
  {"rotulo": "Embudo de muestras",
   "inicio": "Cinco muestras",
   "candidatos": ["Hemocultivo", "Lavado broncoalveolar", "Esputo inducido", "Biopsia pulmonar"],
   "pasos": [("Muestra respiratoria útil", ["Lavado broncoalveolar", "Esputo inducido"]),
             ("Útil pero invasiva", ["Biopsia pulmonar"])],
   "final": ("HEMOCULTIVO", ["No crece ni está en sangre", "No sirve"]),
   "nota": "Lavado: > 90 % de sensibilidad."},
  ["Tinción de Grocott o PCR.",
   "CD4 < 200, LDH alta.",
   "Cotrimoxazol + corticoide si PaO2 < 70."],
  MURRAY)

# CB-480 · radial
V("radial", "CB-480", "cuerpos-negri-rabia-inclusion-intracitoplasmatica", "Inclusiones virales",
  "CIENCIAS BÁSICAS ENAM: RABIA", CB,
  ("Inclusiones virales", ["Cada virus deja una huella típica",
   "Negri: rabia, en el citoplasma neuronal"]),
  ("Pregunta de microbiología", ["¿En qué infección aparecen cuerpos de Negri?"]),
  {"rotulo": "Mapa del tema", "centro": "INCLUSIONES", "centro_sub": "Virales", "ans": 0,
   "items": [("NEGRI", ["Rabia", "Purkinje, hipocampo"]),
             ("Cowdry A", ["Herpes: nuclear"]),
             ("Ojo de búho", ["Citomegalovirus"]),
             ("Coilocitos", ["Virus del papiloma"]),
             ("Henderson-P.", ["Molusco contagioso"])],
   "ruta": ["Mordedura", "Nervios periféricos", "Neuronas", "NEGRI"]},
  ["Perros y murciélagos en el Perú.",
   "Hidrofobia y aerofobia.",
   "Profilaxis: vacuna e inmunoglobulina."],
  MURRAY)

# CB-481 · radial
V("radial", "CB-481", "parotiditis-paperas-paramyxovirus-orquitis", "Parotiditis epidémica",
  "CIENCIAS BÁSICAS ENAM: PAROTIDITIS", CB,
  ("Paperas", ["Virus ARN de la familia Paramyxoviridae",
   "Gotitas respiratorias, incubación 16-18 días"]),
  ("Pregunta de microbiología", ["¿Agente etiológico de la parotiditis?"]),
  {"rotulo": "Mapa del tema", "centro": "PAPERAS", "centro_sub": "Virus", "ans": 0,
   "items": [("PARAMIXOVIRUS", ["Orthorubulavirus"]),
             ("Orquitis", ["Varones pospúberes"]),
             ("Meningitis", ["Aséptica"]),
             ("Pancreatitis", ["Amilasa alta"]),
             ("Prevención", ["Vacuna SPR"])],
   "ruta": ["Gotitas", "Parótidas", "Inflamación", "PAPERAS"]},
  ["SPR a los 12 y 18 meses.",
   "Aislar 5 días.",
   "Sordera unilateral."],
  MURRAY)

# CB-482 · embudo
V("embudo", "CB-482", "ciclo-pulmonar-ascaris-necator-strongyloides-loeffler", "Helmintos con ciclo pulmonar",
  "CIENCIAS BÁSICAS ENAM: CICLO DE LOOSS", CB,
  ("Ciclo pulmonar", ["Las larvas pasan por el pulmón",
   "Pueden causar síndrome de Löffler"]),
  ("Pregunta de parasitología", ["¿Qué parásitos hacen ciclo pulmonar?"]),
  {"rotulo": "Embudo parasitológico",
   "inicio": "Cinco parásitos",
   "candidatos": ["Ascaris", "Strongyloides", "Toxocara", "Enterobius"],
   "pasos": [("Pasa por el pulmón", ["Enterobius"]),
             ("Completa su ciclo en humanos", ["Toxocara"])],
   "final": ("1, 2 Y 5", ["Ascaris, Necator, Strongyloides", "Síndrome de Löffler"]),
   "nota": "Toxocara: larva migrans, no completa ciclo."},
  ["Tos, sibilancias, eosinofilia.",
   "Infiltrados migratorios.",
   "Ancylostoma también."],
  BOTERO)

# CB-483 · matriz
V("matriz", "CB-483", "strongyloides-penetracion-cutanea-no-fecalismo", "Vías de infección parasitaria",
  "CIENCIAS BÁSICAS ENAM: TRANSMISIÓN PARASITARIA", CB,
  ("Transmisión de parásitos", ["Fecalismo: ingerir huevos o quistes",
   "Penetración cutánea: larvas del suelo"]),
  ("Pregunta de parasitología", ["¿Qué enteroparásito no se transmite", "por fecalismo?"]),
  {"rotulo": "Vía de entrada", "eje_x": "Dato", "eje_y": "Parásito",
   "cols": ["Vía", "Forma"], "rows": ["Ascaris, Trichuris", "Strongyloides", "Entamoeba"], "caso": (1, 0),
   "cells": [[("Fecal-oral", []), ("Huevo embrionado", [])],
             [("PIEL", ["Andar descalzo"]), ("Larva filariforme", [])],
             [("Fecal-oral", []), ("Quiste", [])]]},
  ["Uncinarias: también por la piel.",
   "Larva currens en la piel.",
   "Baermann para el diagnóstico."],
  BOTERO)

# CB-484 · tarjetas
V("tarjetas", "CB-484", "blastocystis-no-acido-alcohol-resistente-coccidias", "Protozoos intestinales",
  "CIENCIAS BÁSICAS ENAM: BLASTOCYSTIS", CB,
  ("Tinción ácido-alcohol resistente", ["Ziehl-Neelsen modificado",
   "Tiñe coccidias, no Blastocystis"]),
  ("Pregunta de parasitología", ["¿Qué no corresponde a Blastocystis?"]),
  {"rotulo": "¿Ácido-alcohol resistente?", "ans": 0, "cards": [
      {"titulo": "BLASTOCYSTIS", "datos": [
          ("Ácido-alcohol", "NO", True), ("Tipo", "Anaerobio estricto", True),
          ("Formas", "Vacuolar, ameboide", True)],
       "pie": "Organelos tipo mitocondria"},
      {"titulo": "Cryptosporidium", "datos": [
          ("Ácido-alcohol", "Sí", False), ("Tamaño", "4-6 µm", False),
          ("Grupo", "VIH", False)],
       "pie": "Coccidia"},
      {"titulo": "Cyclospora", "datos": [
          ("Ácido-alcohol", "Variable", False), ("Tamaño", "8-10 µm", False),
          ("Tratamiento", "Cotrimoxazol", False)],
       "pie": "Coccidia"},
      {"titulo": "Cystoisospora", "datos": [
          ("Ácido-alcohol", "Sí", False), ("Forma", "Ovalada", False),
          ("Tratamiento", "Cotrimoxazol", False)],
       "pie": "Coccidia"}]},
  ["Patogenicidad discutida.",
   "Si hay síntomas: metronidazol.",
   "Inmunofluorescencia y PCR."],
  BOTERO)

# CB-485 · árbol
A("CB-485", "geohelmintiasis-ascaris-trichuris-maduran-suelo", "Parasitosis transmitidas por el suelo",
  "CIENCIAS BÁSICAS ENAM: GEOHELMINTIASIS", CB,
  ("Geohelmintiasis", ["Huevos o larvas maduran en el suelo",
   "Ascaris, Trichuris, uncinarias, Strongyloides"]),
  ("Pregunta de parasitología", ["¿Cuáles son transmitidas por el suelo?"]),
  Q("¿El huevo madura en el suelo?", [
      L("Sí", "ASCARIS, TRICHURIS", ["Y uncinarias"], path=True),
      L("No", "Otras vías", ["Oxiuros: persona a persona", "Fasciola: berros"])], path=True),
  ("Prevención", [("Medida", True), ("Efecto", False)], [
      ("Saneamiento", ["Letrinas", "Menos huevos"]),
      ("Desparasitar", ["Albendazol", "Escolares"])]),
  ["Anemia y desnutrición en niños.",
   "Selva y zonas rurales.",
   "Amebiasis: quistes, no suelo."],
  BOTERO)
