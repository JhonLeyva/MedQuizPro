"""Ciencias Básicas · parte D (CB-213 a CB-252)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-213 · puntaje
V("puntaje", "CB-213", "paco2-normal-40-mmhg-tec-hipertension-endocraneana", "PaCO2 normal",
  "CIENCIAS BÁSICAS ENAM: GASES ARTERIALES", CB,
  ("PaCO2", ["Refleja la ventilación alveolar",
   "Normal a nivel del mar: 35-45 mmHg"]),
  ("Varón de 40 años con TEC severo", ["Coma e hiperventilación", "¿Valor normal promedio de PaCO2?"]),
  {"rotulo": "Valor de referencia", "escala": "mmHg", "total": 40, "max": 60,
   "total_label": "PaCO2 promedio",
   "interpreta": "Normal: 35-45 mmHg",
   "items": [("Límite inferior", "35", False), ("Promedio", "40", True), ("Límite superior", "45", False)],
   "bandas": [("< 35", "Hipocapnia", "Vasoconstricción cerebral", False),
              ("35-45", "Normal", "Meta en el TEC", True),
              ("> 45", "Hipercapnia", "Aumenta la PIC", False)]},
  ["Hiperventilar baja la PIC pero da isquemia.",
   "Hiperventilación breve solo ante herniación.",
   "En la altura la PaCO2 normal es menor."],
  "Brain Trauma Foundation (2016) · " + GUYTON)

# CB-214 · embudo
V("embudo", "CB-214", "nino-8-anos-sudoracion-tos-productiva-plaguicida", "Sustancia en el síndrome colinérgico",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIONES", CB,
  ("Síndrome colinérgico", ["Secreciones, miosis y fasciculaciones",
   "Exceso de acetilcolina"]),
  ("Niño de 8 años", ["Sialorrea, tos productiva, miosis", "Fasciculaciones y sudoración profusa"]),
  {"rotulo": "Embudo de sustancias",
   "inicio": "Producto desconocido",
   "candidatos": ["Organofosforado", "Hioscina", "Fenotiazina", "Paracetamol"],
   "pasos": [("Hay secreciones y miosis", ["Hioscina", "Fenotiazina"]),
             ("Síntomas inmediatos", ["Paracetamol"])],
   "final": ("ORGANOFOSFORADO", ["Inhibe la acetilcolinesterasa", "Atropina + pralidoxima"]),
   "nota": "Benzodiacepinas: sedación sin secreciones."},
  ["Hioscina: anticolinérgica, da midriasis.",
   "Paracetamol: daño hepático a las 24-72 h.",
   "Plaguicidas en casa: causa frecuente."],
  TOXI)

# CB-215 · árbol
A("CB-215", "depresion-ingesta-miosis-fasciculaciones-atropinizacion", "Tratamiento del síndrome colinérgico",
  "CIENCIAS BÁSICAS ENAM: ORGANOFOSFORADOS", CB,
  ("Intoxicación por organofosforados", ["Frecuente en intentos suicidas",
   "El pilar es la atropina"]),
  ("Varón de 23 años con depresión", ["Ingesta de sustancia desconocida", "Miosis, fasciculaciones, sialorrea"]),
  Q("¿Síndrome colinérgico?", [
      L("Sí", "ATROPINIZACIÓN", ["Dosis crecientes IV", "Hasta secar secreciones"], path=True),
      L("No", "Otro tóxico", ["Buscar toxíndrome"])], path=True),
  ("Medidas que no sirven", [("Medida", True), ("Motivo", False)], [
      ("Hemodiálisis", ["No elimina", "Liposoluble"]),
      ("Diuresis forzada", ["No elimina", "Se distribuye"])]),
  ["Metas: FC > 80 y PAS > 80 mmHg.",
   "Añadir pralidoxima.",
   "Retirar la ropa y lavar la piel."],
  TOXI)

# CB-216 · tarjetas
V("tarjetas", "CB-216", "fenitoina-hiperplasia-gingival-uso-cronico", "Efectos crónicos de los antiepilépticos",
  "CIENCIAS BÁSICAS ENAM: ANTIEPILÉPTICOS", CB,
  ("Antiepilépticos", ["Cada uno tiene efectos adversos típicos",
   "La fenitoína altera encías, piel y hueso"]),
  ("Pregunta de farmacología", ["¿Qué efecto es frecuente con la fenitoína?"]),
  {"rotulo": "¿Qué fármaco?", "ans": 0, "cards": [
      {"titulo": "FENITOÍNA", "datos": [
          ("Encías", "Hiperplasia", True), ("Piel", "Hirsutismo", True),
          ("Sangre", "Megaloblástica", True)],
       "pie": "Nistagmo y ataxia si es tóxica"},
      {"titulo": "Valproato", "datos": [
          ("Hígado", "Hepatotoxicidad", False), ("Peso", "Aumenta", False),
          ("Feto", "Tubo neural", False)],
       "pie": "Inhibidor enzimático"},
      {"titulo": "Carbamazepina", "datos": [
          ("Sodio", "Hiponatremia", False), ("Sangre", "Agranulocitosis", False),
          ("Piel", "HLA-B*1502", False)],
       "pie": "Inductor enzimático"},
      {"titulo": "Topiramato", "datos": [
          ("Riñón", "Cálculos", False), ("pH", "Acidosis", False),
          ("Peso", "Disminuye", False)],
       "pie": "Parestesias"}]},
  ["Hiperplasia gingival: 20-50 % de pacientes.",
   "Cinética no lineal: niveles saltan.",
   "Síndrome hidantoínico fetal."],
  GOODMAN)

# CB-217 · fases
V("fases", "CB-217", "descenso-testicular-conducto-inguinal-semana-28", "Descenso del testículo",
  "CIENCIAS BÁSICAS ENAM: DESCENSO TESTICULAR", CB,
  ("Descenso testicular", ["Dos fases: transabdominal e inguinoescrotal",
   "La segunda depende de andrógenos"]),
  ("Pregunta de embriología", ["¿En qué semana cruza el conducto inguinal?"]),
  {"rotulo": "Semanas de gestación", "ans": 1,
   "fases": [("Abdominal", "Sem. 8-15", "Anillo interno", ["INSL3, gubernáculo"]),
             ("Inguinal", "Sem. 26-28", "CONDUCTO", ["Cruza el canal"]),
             ("Escrotal", "Sem. 32-35", "Escroto", ["Andrógenos"])],
   "chips_titulo": "Semana · marcada la correcta",
   "chips": [("28", True), ("20", False), ("32", False), ("36", False)]},
  ["Criptorquidia: 30 % en prematuros.",
   "A término: alrededor del 3 %.",
   "Orquidopexia antes de los 18 meses."],
  LANGMAN)

# CB-218 · matriz
V("matriz", "CB-218", "enartrosis-esfericas-movimiento-poliaxial-cadera", "Ejes de las articulaciones",
  "CIENCIAS BÁSICAS ENAM: ARTICULACIONES SINOVIALES", CB,
  ("Articulaciones sinoviales", ["Se clasifican por el número de ejes",
   "Las esféricas se mueven en todos"]),
  ("Pregunta de anatomía", ["¿Qué articulaciones son poliaxiales?"]),
  {"rotulo": "Ejes y ejemplos", "eje_x": "Rasgo", "eje_y": "Ejes",
   "cols": ["Tipo", "Ejemplo"], "rows": ["Uniaxial", "Biaxial", "Multiaxial"], "caso": (2, 0),
   "cells": [[("Tróclea, trocoide", []), ("Codo, atloaxoidea", [])],
             [("Condílea, silla", []), ("Muñeca, pulgar", [])],
             [("ESFÉRICA", ["Enartrosis"]), ("Hombro, cadera", [])]]},
  ["El hombro es el más móvil y el que más se luxa.",
   "La cadera es más estable: acetábulo profundo.",
   "Planas: solo deslizan."],
  MOORE)

# CB-219 · puntaje
V("puntaje", "CB-219", "capacidad-vital-volumen-reserva-espirometria", "Capacidad vital",
  "CIENCIAS BÁSICAS ENAM: VOLÚMENES PULMONARES", CB,
  ("Volúmenes pulmonares", ["Las capacidades suman volúmenes",
   "La capacidad vital no incluye el volumen residual"]),
  ("Pregunta de fisiología", ["Aire máximo espirado tras inspiración máxima"]),
  {"rotulo": "Suma de volúmenes", "escala": "mL", "total": 4600, "max": 5800,
   "total_label": "Capacidad vital",
   "interpreta": "Capacidad vital",
   "items": [("Reserva inspiratoria", "3000", True), ("Volumen corriente", "500", True),
             ("Reserva espiratoria", "1100", True)],
   "bandas": [("3500", "Capac. inspiratoria", "VT + VRI", False),
              ("4600", "Capacidad vital", "Espirometría", True),
              ("5800", "Capac. pulmonar", "Con el residual", False)]},
  ["La CVF baja en enfermedades restrictivas.",
   "Guillain-Barré: CV < 15-20 mL/kg es alarma.",
   "El volumen residual no se espira."],
  GUYTON)

# CB-220 · radial
V("radial", "CB-220", "adolescente-albuminuria-masiva-podocitos-diafragma", "Barrera de filtración glomerular",
  "CIENCIAS BÁSICAS ENAM: GLOMÉRULO", CB,
  ("Barrera glomerular", ["Endotelio, membrana basal y podocitos",
   "El diafragma de hendidura frena las proteínas"]),
  ("Adolescente de 14 años", ["Albuminuria masiva", "¿Qué estructura está dañada?"]),
  {"rotulo": "Mapa del tema", "centro": "GLOMÉRULO", "centro_sub": "Barrera", "ans": 0,
   "items": [("PODOCITOS", ["Pedicelos borrados", "Nefrina, podocina"]),
             ("Membrana basal", ["Carga negativa"]),
             ("Endotelio", ["Fenestrado"]),
             ("Mesangio", ["Sostén, fagocitosis"]),
             ("Mácula densa", ["Regula filtrado", "y renina"])],
   "ruta": ["Proteinuria masiva", "Nefrótico", "Cambios mínimos", "PODOCITO"]},
  ["Cambios mínimos: solo al microscopio electrónico.",
   "GEFS: muerte de podocitos.",
   "Nefrótico en niños: > 40 mg/m²/h."],
  ROBBINS)

# CB-221 · matriz
V("matriz", "CB-221", "trombosis-tronco-celiaco-intestino-mesenterica-superior", "Territorios arteriales digestivos",
  "CIENCIAS BÁSICAS ENAM: IRRIGACIÓN INTESTINAL", CB,
  ("Irrigación digestiva", ["Tres troncos: celíaco, mesentérica superior",
   "y mesentérica inferior"]),
  ("Adulto mayor", ["Trombosis completa del tronco celíaco", "¿Qué órgano mantiene su irrigación?"]),
  {"rotulo": "Tronco y órganos", "eje_x": "Dato", "eje_y": "Tronco",
   "cols": ["Irriga", "Si se ocluye el celíaco"], "rows": ["Celíaco", "Mesentérica sup.", "Mesentérica inf."], "caso": (1, 1),
   "cells": [[("Estómago, hígado", ["Bazo, vesícula"]), ("Afectados", ["Colaterales ayudan"])],
             [("INTESTINO", ["Delgado, colon der."]), ("CONSERVADO", ["Irrigación directa"])],
             [("Colon izquierdo", ["Recto superior"]), ("Conservado", [])]]},
  ["Arcadas pancreatoduodenales: colateral.",
   "Isquemia crónica: suelen ocluirse 2 troncos.",
   "Ligamento arcuato: comprime el celíaco."],
  MOORE)

# CB-222 · matriz
V("matriz", "CB-222", "infarto-blanco-bazo-circulacion-terminal", "Infartos blancos y rojos",
  "CIENCIAS BÁSICAS ENAM: INFARTO", CB,
  ("Tipos de infarto", ["Blanco: órgano sólido con arteria terminal",
   "Rojo: doble circulación u oclusión venosa"]),
  ("Pregunta de patología", ["¿Dónde son típicos los infartos blancos?"]),
  {"rotulo": "Tipo y órganos", "eje_x": "Tipo", "eje_y": "Rasgo",
   "cols": ["Rojo", "Blanco"], "rows": ["Causa", "Órganos", "Aspecto"], "caso": (1, 1),
   "cells": [[("Doble irrigación", ["Oclusión venosa"]), ("Arteria terminal", ["Órgano sólido"])],
             [("Pulmón, intestino", ["Ovario torcido"]), ("BAZO", ["Riñón, corazón"])],
             [("Hemorrágico", []), ("Pálido, en cuña", [])]]},
  ["Reperfusión también da infarto rojo.",
   "Pulmón: arterias pulmonares y bronquiales.",
   "Intestino: tejido laxo y colaterales."],
  ROBBINS)

# CB-223 · árbol
A("CB-223", "nino-antipireticos-antigripales-ictericia-paracetamol", "Ictericia tras antipiréticos",
  "CIENCIAS BÁSICAS ENAM: HEPATOTOXICIDAD", CB,
  ("Hepatotoxicidad en niños", ["Dosis repetidas de paracetamol",
   "A menudo sumado en antigripales"]),
  ("Niño de 6 años", ["Recibió antipiréticos y descongestionante", "Ictericia con transaminasas muy altas"]),
  Q("¿Hay ictericia?", [
      L("Sí", "PARACETAMOL", ["Necrosis centrolobulillar", "Tratar con N-acetilcisteína"], path=True),
      L("No", "Salicilatos: Reye", ["Encefalopatía", "Bilirrubina normal"])], path=True),
  ("Diferencia con Reye", [("Paracetamol", True), ("Reye", False)], [
      ("Bilirrubina", ["Alta", "Normal"]),
      ("Causa", ["NAPQI", "Aspirina en virosis"])]),
  ["Transaminasas > 1000 UI/L.",
   "NAC útil aun tardíamente.",
   "Revisar todos los productos con paracetamol."],
  NELSON + " · " + TOXI)

# CB-224 · fases
V("fases", "CB-224", "cordones-angioblasticos-corazon-tercera-semana", "Desarrollo del corazón",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA CARDÍACA", CB,
  ("Corazón embrionario", ["Primer órgano que funciona",
   "Late hacia el día 22"]),
  ("Pregunta de embriología", ["¿Cuándo aparecen los cordones angioblásticos?"]),
  {"rotulo": "Semanas del desarrollo", "ans": 0,
   "fases": [("Semana 3", "Mediados", "CORDONES", ["Angioblásticos", "Tubos endocárdicos"]),
             ("Semana 4", "Plegamiento", "Asa cardíaca", ["Tubo único"]),
             ("Semanas 5-8", "Tabiques", "Cuatro cámaras", ["Periodo crítico"])],
   "chips_titulo": "Semana · marcada la correcta",
   "chips": [("Tercera", True), ("Segunda", False), ("Cuarta", False), ("Sexta", False)]},
  ["Cardiopatías congénitas: semanas 3 a 8.",
   "Teratógenos: rubéola, litio, alcohol.",
   "Placa cardiogénica: mesodermo esplácnico."],
  LANGMAN)

# CB-225 · embudo
V("embudo", "CB-225", "nino-centro-minero-colico-encefalopatia-plomo", "Metales en zonas mineras",
  "CIENCIAS BÁSICAS ENAM: SATURNISMO", CB,
  ("Intoxicación por plomo", ["Inhibe la síntesis del hemo",
   "En niños: encefalopatía y daño cognitivo"]),
  ("Varón de 9 años de un centro minero", ["Alteraciones de conducta y cólico", "Luego encefalopatía"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Niño expuesto a metales",
   "candidatos": ["Plomo", "Mercurio", "Arsénico", "Litio"],
   "pasos": [("Cólico abdominal y conducta", ["Litio"]),
             ("Encefalopatía infantil típica", ["Mercurio", "Arsénico"])],
   "final": ("PLOMO", ["Anemia con punteado basófilo", "Quelantes si nivel alto"]),
   "nota": "Mercurio: temblor y gingivitis. Arsénico: diarrea y QT largo."},
  ["Ribete de Burton en las encías.",
   "Bandas densas en metáfisis.",
   "Succímero oral; EDTA si hay encefalopatía."],
  TOXI)

# CB-226 · tarjetas
V("tarjetas", "CB-226", "corteza-suprarrenal-mesodermo-medula-cresta-neural", "Origen embriológico de los órganos",
  "CIENCIAS BÁSICAS ENAM: CAPAS GERMINATIVAS", CB,
  ("Glándula suprarrenal", ["Corteza y médula tienen origen distinto",
   "La corteza viene del mesodermo"]),
  ("Pregunta de embriología", ["¿Origen de la corteza suprarrenal?"]),
  {"rotulo": "¿Qué capa?", "ans": 0, "cards": [
      {"titulo": "MESODERMO", "datos": [
          ("Deriva", "CORTEZA", True), ("Origen", "Epitelio celómico", True),
          ("Produce", "Esteroides", True)],
       "pie": "Comparte SF-1 con la gónada"},
      {"titulo": "Cresta neural", "datos": [
          ("Deriva", "Médula", False), ("Células", "Cromafines", False),
          ("Produce", "Adrenalina", False)],
       "pie": "Feocromocitoma"},
      {"titulo": "Ectodermo", "datos": [
          ("Deriva", "Epidermis", False), ("También", "Sistema nervioso", False),
          ("Ejemplo", "Neurohipófisis", False)],
       "pie": "Capa externa"},
      {"titulo": "Endodermo", "datos": [
          ("Deriva", "Epitelio digestivo", False), ("También", "Tiroides", False),
          ("Ejemplo", "Hígado", False)],
       "pie": "Capa interna"}]},
  ["Zona fetal: produce DHEA.",
   "Neuroblastoma: cresta neural.",
   "Médula: neuronas simpáticas modificadas."],
  LANGMAN)

# CB-227 · radial
V("radial", "CB-227", "sertoli-hormona-antimulleriana-inhibe-no-estimula", "Funciones de la célula de Sertoli",
  "CIENCIAS BÁSICAS ENAM: TESTÍCULO", CB,
  ("Célula de Sertoli", ["Sostén de la espermatogénesis",
   "Responde a la FSH"]),
  ("Pregunta de histología", ["¿Qué función no le corresponde?"]),
  {"rotulo": "Mapa del tema", "centro": "SERTOLI", "centro_sub": "Funciones", "ans": 0,
   "items": [("AMH: INHIBE", ["No estimula Müller", "Opción falsa"]),
             ("Espermatogénesis", ["Sostén y nutrición"]),
             ("Barrera", ["Hematotesticular"]),
             ("Inhibina B", ["Frena la FSH"]),
             ("Aromatasa", ["Testosterona → estradiol"])],
   "ruta": ["FSH", "Célula de Sertoli", "AMH", "REGRESA MÜLLER"]},
  ["Sin AMH: varón con útero y trompas.",
   "Proteína fijadora de andrógenos.",
   "La testosterona es de Leydig."],
  LANGMAN)

# CB-228 · termómetro
V("termometro", "CB-228", "ferritina-deposito-hierro-vitamina-c-absorcion", "Interpretación de la ferritina",
  "CIENCIAS BÁSICAS ENAM: METABOLISMO DEL HIERRO", CB,
  ("Metabolismo del hierro", ["Ferritina: depósito · Transferrina: transporte",
   "Se absorbe 1-2 mg al día en el duodeno"]),
  ("Pregunta de bioquímica", ["¿Qué afirmación es correcta?"]),
  {"rotulo": "Ferritina sérica",
   "niveles": [("< 30 ng/mL", "Depósito vacío", ["Déficit de hierro"]),
               ("30-100", "Dudosa", ["Si hay inflamación"]),
               ("100-300", "Normal", ["Depósito adecuado"]),
               ("> 300", "Elevada", ["Inflamación o sobrecarga"])],
   "caso_nivel": 0, "ruta_titulo": "Por qué las otras fallan", "paso_label": "PASO",
   "pasos": [(1, "Vitamina C", ["Favorece la absorción"], False),
             (2, "Fitatos", ["La inhiben"], False),
             (3, "Ferritina", ["Refleja el depósito"], True)]},
  ["La ferritina es reactante de fase aguda.",
   "Solo se absorbe el 10 % del hierro ingerido.",
   "La hepcidina regula la absorción."],
  HARRISON)

# CB-229 · fases
V("fases", "CB-229", "acoplamiento-excitacion-contraccion-calcio-troponina-c", "Acoplamiento excitación-contracción",
  "CIENCIAS BÁSICAS ENAM: CONTRACCIÓN MUSCULAR", CB,
  ("Contracción del músculo estriado", ["El calcio libera los sitios de la actina",
   "Se une a la troponina C"]),
  ("Pregunta de fisiología", ["¿Qué se une a la troponina C?"]),
  {"rotulo": "Pasos de la contracción", "ans": 1,
   "fases": [("Estímulo", "Túbulos T", "Potencial", ["Retículo libera"]),
             ("Unión", "Troponina C", "CALCIO", ["Mueve tropomiosina"]),
             ("Puentes", "Actina-miosina", "Contracción", ["Gasta ATP"])],
   "chips_titulo": "Ion · marcado el correcto",
   "chips": [("Calcio", True), ("Sodio", False), ("Fosfato", False), ("Potasio", False)]},
  ["Relajación: SERCA recapta el calcio.",
   "Músculo liso: calcio-calmodulina.",
   "Rigor mortis: falta de ATP."],
  GUYTON)

# CB-230 · matriz
V("matriz", "CB-230", "noradrenalina-inhibe-motilidad-intestinal-simpatico", "Control nervioso del intestino",
  "CIENCIAS BÁSICAS ENAM: MOTILIDAD INTESTINAL", CB,
  ("Motilidad intestinal", ["Parasimpático y hormonas la estimulan",
   "El simpático la inhibe"]),
  ("Pregunta de fisiología", ["¿Qué sustancia inhibe la motilidad?"]),
  {"rotulo": "Efecto sobre la motilidad", "eje_x": "Efecto", "eje_y": "Sustancia",
   "cols": ["Motilidad", "Esfínteres"], "rows": ["Noradrenalina", "Acetilcolina", "Motilina"], "caso": (0, 0),
   "cells": [[("INHIBE", ["Simpático"]), ("Contrae", [])],
             [("Estimula", ["Parasimpático"]), ("Relaja", [])],
             [("Estimula", ["Complejo migratorio"]), ("—", [])]]},
  ["Estrés o cirugía: íleo.",
   "Serotonina y CCK: estimulan.",
   "Clonidina (alfa-2): estriñe."],
  GUYTON)

# CB-231 · embudo
V("embudo", "CB-231", "traquea-epitelio-pseudoestratificado-ciliado-caliciformes", "Epitelio de la tráquea",
  "CIENCIAS BÁSICAS ENAM: EPITELIO RESPIRATORIO", CB,
  ("Epitelio respiratorio", ["Pseudoestratificado cilíndrico ciliado",
   "Con células caliciformes"]),
  ("Pregunta de histología", ["¿Qué epitelio tiene la tráquea?"]),
  {"rotulo": "Embudo histológico",
   "inicio": "Tipos de epitelio",
   "candidatos": ["Pseudoestratificado", "Cilíndrico simple", "Escamoso", "Cuboidal estratif."],
   "pasos": [("Tiene cilios y moco", ["Escamoso", "Cuboidal estratif."]),
             ("Núcleos a distintas alturas", ["Cilíndrico simple"])],
   "final": ("PSEUDOESTRATIFICADO CILIADO", ["Todas las células tocan la basal", "Aparato mucociliar"]),
   "nota": "Tabaco: metaplasia escamosa."},
  ["Kartagener: cilios inmóviles.",
   "Bronquiectasias y situs inversus.",
   "Caliciformes: producen moco."],
  ROSS)

# CB-232 · fases
V("fases", "CB-232", "esbozos-extremidades-cuarta-semana-cresta-apical", "Desarrollo de las extremidades",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA DE EXTREMIDADES", CB,
  ("Extremidades", ["Esbozos al final de la 4.ª semana",
   "La cresta ectodérmica apical guía el crecimiento"]),
  ("Pregunta de embriología", ["¿Cuándo aparecen los esbozos?"]),
  {"rotulo": "Semanas del desarrollo", "ans": 0,
   "fases": [("Semana 4", "Días 26-28", "ESBOZOS", ["Superiores primero"]),
             ("Semanas 5-6", "Placas", "Manos y pies", ["Segmentos"]),
             ("Semanas 7-8", "Apoptosis", "Dedos", ["Separación"])],
   "chips_titulo": "Semana · marcada la correcta",
   "chips": [("Cuarta", True), ("Tercera", False), ("Séptima", False), ("Novena", False)]},
  ["Periodo crítico: semanas 4 a 8.",
   "Talidomida: focomelia.",
   "Sindactilia: falla la apoptosis."],
  LANGMAN)

# CB-233 · tarjetas
V("tarjetas", "CB-233", "hormona-luteinizante-receptor-proteina-g-ampc", "Tipos de receptores hormonales",
  "CIENCIAS BÁSICAS ENAM: RECEPTORES", CB,
  ("Receptores hormonales", ["Hidrosolubles: receptor de membrana",
   "Liposolubles: receptor intracelular"]),
  ("Pregunta de fisiología", ["¿Qué receptor usa la LH?"]),
  {"rotulo": "¿Qué receptor?", "ans": 0, "cards": [
      {"titulo": "PROTEÍNA G", "datos": [
          ("Ejemplo", "LH, FSH, TSH", True), ("Mensajero", "AMPc", True),
          ("Ubicación", "Membrana", True)],
       "pie": "7 dominios transmembrana"},
      {"titulo": "Tirosina cinasa", "datos": [
          ("Ejemplo", "Insulina", False), ("Mensajero", "Fosforilación", False),
          ("Ubicación", "Membrana", False)],
       "pie": "IGF-1"},
      {"titulo": "Intracelular", "datos": [
          ("Ejemplo", "Esteroides", False), ("Acción", "Transcripción", False),
          ("Ubicación", "Citoplasma, núcleo", False)],
       "pie": "Tiroxina también"},
      {"titulo": "Canal iónico", "datos": [
          ("Ejemplo", "Nicotínico", False), ("Acción", "Abre el canal", False),
          ("Ubicación", "Membrana", False)],
       "pie": "Neurotransmisores"}]},
  ["La hCG usa el mismo receptor que la LH.",
   "Glucagón y PTH: también AMPc.",
   "Pico de LH: ovulación."],
  GUYTON)

# CB-234 · puntaje
V("puntaje", "CB-234", "flujo-sanguineo-renal-1100-ml-min-gasto-cardiaco", "Flujo sanguíneo renal",
  "CIENCIAS BÁSICAS ENAM: HEMODINÁMICA RENAL", CB,
  ("Flujo sanguíneo renal", ["Recibe 20-22 % del gasto cardíaco",
   "Unos 1100-1200 mL/min"]),
  ("Varón de 70 kg", ["¿Cuál es su flujo sanguíneo renal?"]),
  {"rotulo": "Cálculo", "escala": "mL/min", "total": 1100, "max": 5000,
   "total_label": "Flujo renal",
   "interpreta": "≈ 1100 mL/min",
   "items": [("Gasto cardíaco", "5000", True), ("Fracción renal", "22 %", True), ("Filtrado", "125", False)],
   "bandas": [("125", "Filtrado", "Glomerular", False),
              ("660", "Flujo plasmático", "Aclaramiento de PAH", False),
              ("1100", "Flujo sanguíneo", "Ambos riñones", True)]},
  ["Fracción de filtración: 20 %.",
   "Autorregulación entre 80 y 180 mmHg.",
   "Filtrado: 180 litros al día."],
  GUYTON)

# CB-235 · radial
V("radial", "CB-235", "clindamicina-colitis-pseudomembranosa-clostridioides", "Clindamicina",
  "CIENCIAS BÁSICAS ENAM: LINCOSAMIDAS", CB,
  ("Clindamicina", ["Inhibe la subunidad 50S",
   "Activa contra grampositivos y anaerobios"]),
  ("Pregunta de farmacología", ["¿Efecto adverso más característico?"]),
  {"rotulo": "Mapa del tema", "centro": "CLINDAMICINA", "centro_sub": "Efectos", "ans": 0,
   "items": [("COLITIS", ["Pseudomembranosa", "C. difficile"]),
             ("Mecanismo", ["Ribosoma 50S"]),
             ("Espectro", ["Grampositivos", "Anaerobios"]),
             ("Uso", ["Frena toxinas", "Shock tóxico"]),
             ("Tratamiento", ["Vancomicina oral"])],
   "ruta": ["Clindamicina", "Elimina flora", "Crece C. difficile", "COLITIS"]},
  ["Toxinas A y B.",
   "Pseudomembranas amarillentas.",
   "Riesgo: megacolon tóxico."],
  GOODMAN)

# CB-236 · matriz
V("matriz", "CB-236", "uracilo-arn-timina-adn-bases-nitrogenadas", "Bases del ADN y del ARN",
  "CIENCIAS BÁSICAS ENAM: ÁCIDOS NUCLEICOS", CB,
  ("Bases nitrogenadas", ["Purinas: adenina y guanina",
   "Pirimidinas: citosina, timina y uracilo"]),
  ("Pregunta de bioquímica", ["¿Qué base no está en el ADN?"]),
  {"rotulo": "Composición", "eje_x": "Molécula", "eje_y": "Rasgo",
   "cols": ["ADN", "ARN"], "rows": ["Azúcar", "Pirimidina propia", "Cadenas"], "caso": (1, 1),
   "cells": [[("Desoxirribosa", []), ("Ribosa", [])],
             [("Timina", ["Uracilo metilado"]), ("URACILO", ["No está en el ADN"])],
             [("Doble hélice", []), ("Cadena simple", [])]]},
  ["A-T: 2 puentes de hidrógeno; G-C: 3.",
   "5-FU y metotrexato atacan la síntesis de timina.",
   "Uracilo en el ADN se repara."],
  HARPER)

# CB-237 · árbol
A("CB-237", "ileon-colon-intercambio-bicarbonato-cloro-diarrea", "Transporte de iones en el intestino",
  "CIENCIAS BÁSICAS ENAM: ABSORCIÓN INTESTINAL", CB,
  ("Íleon y colon", ["Secretan bicarbonato a la luz",
   "Y absorben cloro a cambio"]),
  ("Pregunta de fisiología", ["¿Qué ion se absorbe al secretar bicarbonato?"]),
  Q("¿Qué segmento?", [
      L("Yeyuno", "Sodio con glucosa", ["SGLT1"]),
      L("Íleon y colon", "CLORO", ["Intercambio Cl/HCO3", "Neutraliza ácidos"], path=True)], path=True),
  ("Consecuencias clínicas", [("Situación", True), ("Trastorno", False)], [
      ("Diarrea profusa", ["Pierde HCO3", "Acidosis hiperclorémica"]),
      ("Ureterosigmoidostomía", ["Orina en colon", "Acidosis hiperclorémica"])]),
  ["Cloridorrea congénita: alcalosis.",
   "Anión gap normal en la diarrea.",
   "El colon absorbe sodio por ENaC."],
  GUYTON)

# CB-238 · embudo
V("embudo", "CB-238", "trichuris-trichiura-hematofago-anemia-prolapso", "Parásitos hematófagos",
  "CIENCIAS BÁSICAS ENAM: HELMINTOS", CB,
  ("Helmintos hematófagos", ["Se alimentan de sangre de la mucosa",
   "Causan anemia ferropénica"]),
  ("Pregunta de parasitología", ["¿Qué parásito es hematófago?"]),
  {"rotulo": "Embudo parasitológico",
   "inicio": "Cinco parásitos",
   "candidatos": ["Trichuris", "Enterobius", "Ascaris", "Giardia"],
   "pasos": [("Es un helminto", ["Giardia"]),
             ("Penetra la mucosa y chupa sangre", ["Enterobius", "Ascaris"])],
   "final": ("TRICHURIS TRICHIURA", ["Tricocéfalo del colon", "Anemia y prolapso rectal"]),
   "nota": "Uncinarias: principal causa parasitaria de anemia."},
  ["Enterobius: prurito anal.",
   "Ascaris: come contenido intestinal.",
   "Tratamiento: albendazol o mebendazol."],
  BOTERO)

# CB-239 · fases
V("fases", "CB-239", "desnutricion-cronica-hiponatremia-sodio-total-aumentado", "Electrolitos en la desnutrición grave",
  "CIENCIAS BÁSICAS ENAM: DESNUTRICIÓN", CB,
  ("Desnutrición grave", ["Falla la bomba Na⁺/K⁺-ATPasa",
   "Sodio dentro de la célula, potasio fuera"]),
  ("Pregunta de fisiopatología", ["¿Qué trastorno electrolítico aparece?"]),
  {"rotulo": "Secuencia del trastorno", "ans": 1,
   "fases": [("Energía baja", "Bomba falla", "Na entra", ["K se pierde"]),
             ("Líquidos", "Edema", "HIPONATREMIA", ["Sodio total alto", "Por dilución"]),
             ("Manejo", "OMS", "ReSoMal", ["Menos sodio"])],
   "chips_titulo": "Trastorno · marcado el correcto",
   "chips": [("Hipo Na, Na total ↑", True), ("Hiperpotasemia", False), ("Hipernatremia", False), ("Hipercalcemia", False)]},
  ["También hipomagnesemia e hipofosfatemia.",
   "Líquidos con cautela: falla cardíaca.",
   "Realimentación: cuidado con el fósforo."],
  "OMS – Manejo de la desnutrición grave (2013) · " + NELSON)

# CB-240 · fases
V("fases", "CB-240", "faringitis-eritromicina-estolato-hepatitis-colestasica", "Hepatitis por eritromicina estolato",
  "CIENCIAS BÁSICAS ENAM: HEPATOTOXICIDAD", CB,
  ("Eritromicina estolato", ["Hepatitis colestásica inmunoalérgica",
   "Aparece 10-20 días después"]),
  ("Varón de 7 años", ["Tratado por faringoamigdalitis", "A los 15 días: vómitos, cólico e ictericia"]),
  {"rotulo": "Evolución", "ans": 2,
   "fases": [("Faringitis", "Día 0", "Antibiótico", ["Alérgico a penicilina"]),
             ("Tratamiento", "10 días", "Sin síntomas", ["Termina el curso"]),
             ("Día 15", "Colestasis", "ESTOLATO", ["Ictericia, cólico", "Eosinofilia"])],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Eritromicina estolato", True), ("Clindamicina", False), ("Cefradina", False), ("Ampicilina", False)]},
  ["Simula colecistitis.",
   "Se resuelve al suspenderla.",
   "Ampicilina: exantema."],
  GOODMAN)

# CB-241 · árbol
A("CB-241", "lh-celulas-leydig-testosterona-fsh-sertoli", "Eje hipófisis-testículo",
  "CIENCIAS BÁSICAS ENAM: EJE GONADAL MASCULINO", CB,
  ("Eje hipófisis-testículo", ["LH y FSH actúan sobre células distintas",
   "LH: Leydig · FSH: Sertoli"]),
  ("Pregunta de fisiología", ["¿Qué hormona estimula a las células de Leydig?"]),
  Q("¿Qué célula testicular?", [
      L("Leydig", "LUTEINIZANTE (LH)", ["Produce testosterona"], path=True),
      L("Sertoli", "FSH", ["Espermatogénesis", "Inhibina B"])], path=True),
  ("Retroalimentación", [("Hormona", True), ("Frena", False)], [
      ("Testosterona", ["Hipotálamo", "LH"]),
      ("Inhibina B", ["Hipófisis", "FSH"])]),
  ["Testosterona exógena: atrofia testicular.",
   "hCG estimula Leydig en el feto.",
   "LH actúa por AMPc."],
  GUYTON)

# CB-242 · árbol
A("CB-242", "succion-pezon-oxitocina-eyeccion-leche", "Hormonas de la lactancia",
  "CIENCIAS BÁSICAS ENAM: LACTANCIA", CB,
  ("Lactancia", ["Prolactina: produce la leche",
   "Oxitocina: la expulsa"]),
  ("Pregunta de fisiología", ["¿Qué hormona media la eyección de la leche?"]),
  Q("¿Qué acción de la mama?", [
      L("Expulsar", "OXITOCINA", ["Contrae células mioepiteliales", "Neurohipófisis"], path=True),
      L("Producir", "Prolactina", ["Adenohipófisis"])], path=True),
  ("Reflejo de succión", [("Paso", True), ("Resultado", False)], [
      ("Succión", ["Pezón", "Estímulo al hipotálamo"]),
      ("Estrés", ["Dolor, ansiedad", "Inhibe oxitocina"])]),
  ["El llanto del bebé puede activar el reflejo.",
   "Oxitocina contrae el útero al amamantar.",
   "Núcleos supraóptico y paraventricular."],
  GUYTON)

# CB-243 · embudo
V("embudo", "CB-243", "anemia-macrocitica-gastritis-atrofica-celulas-parietales", "Causa de la anemia perniciosa",
  "CIENCIAS BÁSICAS ENAM: ANEMIA PERNICIOSA", CB,
  ("Gastritis atrófica autoinmune", ["Anticuerpos contra las células parietales",
   "Falta el factor intrínseco"]),
  ("Paciente con anemia macrocítica", ["Biopsia: gastritis crónica atrófica", "¿Qué células disminuyen?"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Células de la mucosa",
   "candidatos": ["Parietales", "Principales", "Enterocitos", "Argentafines"],
   "pasos": [("Célula gástrica productora", ["Enterocitos"]),
             ("Produce factor intrínseco", ["Principales", "Argentafines"])],
   "final": ("CÉLULAS PARIETALES", ["Sin factor intrínseco", "No se absorbe B12"]),
   "nota": "Principales o cimógenas: pepsinógeno."},
  ["Aclorhidria con gastrina alta.",
   "Riesgo de carcinoide y adenocarcinoma.",
   "B12 parenteral de por vida."],
  HARRISON)

# CB-244 · tarjetas
V("tarjetas", "CB-244", "celulas-alfa-islote-glucagon-beta-insulina", "Células del islote de Langerhans",
  "CIENCIAS BÁSICAS ENAM: PÁNCREAS ENDOCRINO", CB,
  ("Islotes de Langerhans", ["Cada célula produce una hormona",
   "Alfa: glucagón"]),
  ("Pregunta de fisiología", ["¿Qué producen las células alfa?"]),
  {"rotulo": "¿Qué hormona?", "ans": 0, "cards": [
      {"titulo": "ALFA", "datos": [
          ("Hormona", "Glucagón", True), ("Efecto", "Sube glucemia", True),
          ("Ubicación", "Periferia", True)],
       "pie": "Glucagonoma: eritema migratorio"},
      {"titulo": "Beta", "datos": [
          ("Hormona", "Insulina", False), ("Efecto", "Baja glucemia", False),
          ("Ubicación", "Centro", False)],
       "pie": "Las más numerosas"},
      {"titulo": "Delta", "datos": [
          ("Hormona", "Somatostatina", False), ("Efecto", "Inhibe ambas", False),
          ("Ubicación", "Dispersas", False)],
       "pie": "Paracrina"},
      {"titulo": "PP", "datos": [
          ("Hormona", "Polipéptido P.", False), ("Efecto", "Saciedad", False),
          ("Ubicación", "Cabeza", False)],
       "pie": "Épsilon: grelina"}]},
  ["Gastrina: células G del antro.",
   "Glucagón IM revierte hipoglucemia grave.",
   "Glucagón: glucogenólisis y gluconeogénesis."],
  GUYTON)

# CB-245 · árbol
A("CB-245", "lavado-gastrico-indicado-organofosforados-recientes", "Cuándo se considera el lavado gástrico",
  "CIENCIAS BÁSICAS ENAM: DESCONTAMINACIÓN", CB,
  ("Lavado gástrico", ["Solo en ingesta reciente de un tóxico letal",
   "Con la vía aérea protegida"]),
  ("Pregunta de toxicología", ["¿En qué ingesta se indica?"]),
  Q("¿Cáustico o hidrocarburo?", [
      L("Sí", "Contraindicado", ["Lejía, muriático", "Permanganato, kerosene"]),
      L("No", "ORGANOFOSFORADOS", ["Primera hora", "Vía aérea protegida"], path=True)], path=True),
  ("Contraindicaciones", [("Tóxico", True), ("Riesgo", False)], [
      ("Cáusticos", ["Lejía, ácidos", "Perforación"]),
      ("Hidrocarburos", ["Kerosene", "Neumonitis"])]),
  ["Prioridad: atropina y descontaminar la piel.",
   "Hoy se usa mucho menos.",
   "Nunca con vía aérea no protegida."],
  TOXI)

# CB-246 · radial
V("radial", "CB-246", "nervio-espinal-accesorio-trapecio-ecm-lesion-cervical", "Nervio espinal accesorio",
  "CIENCIAS BÁSICAS ENAM: XI PAR", CB,
  ("Nervio espinal accesorio (XI)", ["Inerva trapecio y esternocleidomastoideo",
   "Superficial en el triángulo posterior"]),
  ("Varón de 52 años operado del cuello", ["No eleva el hombro derecho", "No rota la cabeza a la izquierda"]),
  {"rotulo": "Mapa del tema", "centro": "XI PAR", "centro_sub": "Accesorio", "ans": 0,
   "items": [("ESPINAL ACC.", ["Lesión derecha"]),
             ("Trapecio", ["Eleva el hombro", "Escápula alada"]),
             ("ECM", ["Gira la cara al", "lado opuesto"]),
             ("Riesgo", ["Biopsia ganglionar", "Disección de cuello"]),
             ("Trayecto", ["Triángulo posterior"])],
   "ruta": ["Tumor cervical", "Triángulo posterior", "Lesión del XI", "HOMBRO CAÍDO"]},
  ["El ECM derecho gira la cara a la izquierda.",
   "Hombro caído y doloroso.",
   "Nervio muy superficial."],
  MOORE)

# CB-247 · tarjetas
V("tarjetas", "CB-247", "intento-suicida-atropina-midriasis-bloqueador-colinergico", "Efectos tras la atropina",
  "CIENCIAS BÁSICAS ENAM: FARMACOLOGÍA AUTONÓMICA", CB,
  ("Atropina", ["Antagonista muscarínico",
   "No bloquea los receptores nicotínicos"]),
  ("Varón de 16 años tratado", ["Sequedad de mucosas, midriasis, taquicardia", "Persisten fasciculaciones"]),
  {"rotulo": "¿Qué efecto farmacológico?", "ans": 0, "cards": [
      {"titulo": "BLOQUEADOR COLINÉRGICO", "datos": [
          ("Mucosas", "Secas", True), ("Pupilas", "Midriasis", True),
          ("Corazón", "Taquicardia", True)],
       "pie": "Atropinización"},
      {"titulo": "Agonista colinérgico", "datos": [
          ("Mucosas", "Sialorrea", False), ("Pupilas", "Miosis", False),
          ("Corazón", "Bradicardia", False)],
       "pie": "Efecto opuesto"},
      {"titulo": "Bloqueador adrenérgico", "datos": [
          ("Pupilas", "Miosis leve", False), ("Corazón", "Bradicardia", False),
          ("PA", "Baja", False)],
       "pie": "Betabloqueante"},
      {"titulo": "Fasciculaciones", "datos": [
          ("Receptor", "Nicotínico", False), ("Atropina", "No actúa", False),
          ("Tratamiento", "Pralidoxima", False)],
       "pie": "Por eso persisten"}]},
  ["Fiebre o delirio: exceso de atropina.",
   "Pralidoxima antes del envejecimiento.",
   "Parasimpaticolítico = bloqueador colinérgico."],
  GOODMAN)

# CB-248 · radial
V("radial", "CB-248", "translocacion-cromosomica-robertsoniana-reciproca", "Alteraciones cromosómicas estructurales",
  "CIENCIAS BÁSICAS ENAM: CITOGENÉTICA", CB,
  ("Alteraciones estructurales", ["Cambian la forma de los cromosomas",
   "La translocación mueve un segmento a otro cromosoma"]),
  ("Pregunta de genética", ["Parte de un cromosoma se une a otro", "¿Cómo se llama?"]),
  {"rotulo": "Mapa del tema", "centro": "CROMOSOMA", "centro_sub": "Estructura", "ans": 0,
   "items": [("TRANSLOCACIÓN", ["A otro cromosoma", "Recíproca o robertsoniana"]),
             ("Inversión", ["Giro de 180°"]),
             ("Deleción", ["Pérdida de segmento"]),
             ("Duplicación", ["Segmento repetido"]),
             ("En cáncer", ["t(9;22) Filadelfia"])],
   "ruta": ["Segmento se rompe", "Se une a otro", "No homólogo", "TRANSLOCACIÓN"]},
  ["Balanceada: portador sano.",
   "Riesgo de abortos e hijos afectados.",
   "t(14;21): Down heredable."],
  "Thompson & Thompson. Genética en medicina 8.ª ed. (2016)")

# CB-249 · puntaje
V("puntaje", "CB-249", "errores-innatos-metabolismo-autosomica-recesiva", "Herencia de los errores innatos",
  "CIENCIAS BÁSICAS ENAM: ERRORES INNATOS", CB,
  ("Errores innatos del metabolismo", ["Casi todos son déficits enzimáticos",
   "La mitad de enzima basta: herencia recesiva"]),
  ("Pregunta de genética", ["¿Cómo se heredan casi todos?"]),
  {"rotulo": "Forma de herencia", "escala": "%", "total": 95, "max": 100,
   "total_label": "Autosómica recesiva",
   "interpreta": "Autosómica recesiva",
   "items": [("Padres portadores", "Sanos", True), ("Riesgo por hijo", "25 %", True),
             ("Consanguinidad", "Aumenta", True)],
   "bandas": [("≈ 95 %", "Autosómica recesiva", "Fenilcetonuria", True),
              ("Pocos", "Ligada al X", "Fabry, Hunter", False),
              ("Raros", "Dominante", "Porfiria aguda", False)]},
  ["Galactosemia y jarabe de arce: recesivas.",
   "Déficit de OTC: ligado al X.",
   "Base del tamizaje neonatal."],
  "Nelson. Errores innatos del metabolismo · " + HARPER)

# CB-250 · fases
V("fases", "CB-250", "acalasia-arequipa-vip-oxido-nitrico-esfinter", "Fisiopatología de la acalasia",
  "CIENCIAS BÁSICAS ENAM: ACALASIA", CB,
  ("Acalasia", ["Se pierden las neuronas inhibitorias",
   "Las que liberan VIP y óxido nítrico"]),
  ("Mujer de 30 años de Arequipa", ["Llenura, dolor retroesternal, regurgitación", "Esofagograma: acalasia"]),
  {"rotulo": "Secuencia", "ans": 0,
   "fases": [("Lesión", "Plexo mientérico", "SIN VIP NI NO", ["Faltan inhibitorias"]),
             ("Esfínter", "No se relaja", "EEI alto", ["Sin peristaltismo"]),
             ("Clínica", "Disfagia", "Pico de pájaro", ["Sólidos y líquidos"])],
   "chips_titulo": "Neurotransmisor · marcado el correcto",
   "chips": [("VIP", True), ("Acetilcolina", False), ("Sustancia P", False), ("Serotonina", False)]},
  ["Diagnóstico: manometría de alta resolución.",
   "Chagas produce un cuadro igual.",
   "Tratamiento: dilatación, miotomía o POEM."],
  HARRISON)

# CB-251 · termómetro
V("termometro", "CB-251", "biodisponibilidad-via-oral-menor-primer-paso", "Biodisponibilidad según la vía",
  "CIENCIAS BÁSICAS ENAM: VÍAS DE ADMINISTRACIÓN", CB,
  ("Biodisponibilidad por vía", ["IV: 100 % por definición",
   "Oral: la menor por el primer paso hepático"]),
  ("Pregunta de farmacología", ["¿Qué vía tiene menor biodisponibilidad?"]),
  {"rotulo": "Biodisponibilidad",
   "niveles": [("Oral", "La menor", ["PRIMER PASO", "Absorción incompleta"]),
               ("Subcutánea", "≈ 100 %", ["Más lenta"]),
               ("Intramuscular", "≈ 100 %", ["Rápida"]),
               ("Endovenosa", "100 %", ["Por definición"])],
   "caso_nivel": 0, "ruta_titulo": "Por qué la oral pierde", "paso_label": "PASO",
   "pasos": [(1, "Ácido y enzimas", ["Degradan el fármaco"], False),
             (2, "Glicoproteína P", ["Lo devuelve a la luz"], False),
             (3, "Primer paso", ["Hígado antes de la sangre"], True)]},
  ["Sublingual evita el primer paso.",
   "Rectal inferior: lo evita en parte.",
   "Nitroglicerina: sublingual."],
  KATZUNG)

# CB-252 · puntaje
V("puntaje", "CB-252", "perdida-cargas-membrana-basal-proteinuria-masiva", "Grados de proteinuria",
  "CIENCIAS BÁSICAS ENAM: PROTEINURIA", CB,
  ("Barrera por carga y tamaño", ["Membrana basal negativa repele la albúmina",
   "Podocitos cierran el paso"]),
  ("Pregunta de fisiopatología", ["Pérdida de cargas y poros podocitarios", "¿Qué se espera?"]),
  {"rotulo": "Proteinuria diaria", "escala": "g/día", "total": 3.5, "max": 10,
   "total_label": "Umbral nefrótico",
   "interpreta": "Proteinuria masiva",
   "items": [("Cargas negativas", "Perdidas", True), ("Poros podocitarios", "Amplios", True),
             ("Albúmina", "Pasa", True)],
   "bandas": [("0,03-0,3 g", "Microalbuminuria", "Nefropatía precoz", False),
              ("> 0,3 g", "Proteinuria", "Daño establecido", False),
              ("> 3,5 g", "Masiva", "Síndrome nefrótico", True)]},
  ["Nefrótico: hipoalbuminemia, edema, lípidos.",
   "Hematuria orienta a nefrítico.",
   "Microalbuminuria: diabetes precoz."],
  ROBBINS)
