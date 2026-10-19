"""Ciencias Básicas · parte A (CB-093 a CB-132)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-093 · termómetro
V("termometro", "CB-093", "barbituricos-tiopental-accion-ultracorta-redistribucion", "Barbitúricos según su duración",
  "CIENCIAS BÁSICAS ENAM: BARBITÚRICOS", CB,
  ("Barbitúricos", ["Potencian el GABA-A: sedación, anestesia, anticonvulsión",
   "Se clasifican por la duración de su efecto"]),
  ("Pregunta de farmacología", ["¿Cuál es el barbitúrico de acción ultracorta?"]),
  {"rotulo": "Duración del efecto",
   "niveles": [("Ultracorta", "Minutos", ["TIOPENTAL", "Inducción anestésica"]),
               ("Corta", "3-8 horas", ["Pentobarbital", "Secobarbital"]),
               ("Intermedia", "6-12 horas", ["Amobarbital"]),
               ("Prolongada", "> 12 horas", ["Fenobarbital", "Anticonvulsivante"])],
   "caso_nivel": 0, "ruta_titulo": "Por qué dura tan poco", "paso_label": "PASO",
   "pasos": [(1, "Muy liposoluble", ["Llega al cerebro en segundos"], True),
             (2, "Redistribución", ["Pasa a músculo y grasa"], True),
             (3, "Dosis repetidas", ["Se acumula y prolonga el efecto"], False)]},
  ["La redistribución, no el metabolismo, acorta su efecto.",
   "Fenobarbital: inductor enzimático y anticonvulsivante.",
   "Sobredosis: depresión respiratoria sin antídoto."],
  GOODMAN)

# CB-094 · radial
V("radial", "CB-094", "antineoplasicos-verdadero-falso-asparaginasa-cisplatino", "Antineoplásicos: verdadero o falso",
  "CIENCIAS BÁSICAS ENAM: ANTINEOPLÁSICOS", CB,
  ("Antineoplásicos", ["Actúan en fases del ciclo o en cualquier fase",
   "Alquilantes y platinos dañan el ADN por unión covalente"]),
  ("Pregunta de farmacología", ["Marcar V o F en 5 enunciados"]),
  {"rotulo": "Mapa del tema", "centro": "ANTINEOPLÁSICOS", "centro_sub": "V o F", "ans": 4,
   "items": [("1 · Falso", ["Asparaginasa: fase G1"]),
             ("2 · Falso", ["Cisplatino: platino"]),
             ("3 · Verdadero", ["Ciclofosfamida y 6-MP orales"]),
             ("4 · Verdadero", ["Procarbazina: ácido", "isopropiltereftalámico"]),
             ("5 · VERDADERO", ["Alquilantes ≈ metales", "pesados"])],
   "ruta": ["F", "F", "V", "V · V"]},
  ["Bleomicina actúa en G2; vincristina en M.",
   "Antimetabolitos (metotrexato, 5-FU) actúan en S.",
   "Cisplatino: nefrotóxico, ototóxico y muy emetógeno."],
  GOODMAN)

# CB-095 · tarjetas
V("tarjetas", "CB-095", "superfamilia-inmunoglobulinas-tcr-mhc-clase-i-ii", "Superfamilia de las inmunoglobulinas",
  "CIENCIAS BÁSICAS ENAM: INMUNOLOGÍA", CB,
  ("Superfamilia de las inmunoglobulinas", ["Proteínas con al menos un dominio tipo Ig",
   "Dos láminas beta unidas por un puente disulfuro"]),
  ("Pregunta de inmunología", ["¿Cuál no pertenece a la superfamilia?"]),
  {"rotulo": "¿Es miembro?", "ans": 0, "cards": [
      {"titulo": "TODOS MIEMBROS", "datos": [
          ("TCR", "Sí, dominios Ig", True), ("MHC I", "Sí, dominio α3", True),
          ("MHC II", "Sí, α2 y β2", True)],
       "pie": "Ninguno queda fuera"},
      {"titulo": "Otros miembros", "datos": [
          ("Correceptores", "CD4, CD8", False), ("Adhesión", "ICAM, VCAM", False),
          ("Coestímulo", "CD28, CD2", False)],
       "pie": "También receptores Fc"},
      {"titulo": "No miembros", "datos": [
          ("Integrinas", "Otra familia", False), ("Selectinas", "Tipo lectina", False),
          ("Cadherinas", "Dependen de Ca", False)],
       "pie": "Adhesión, sin dominio Ig"},
      {"titulo": "Dominio Ig", "datos": [
          ("Tamaño", "≈ 110 aminoácidos", False), ("Forma", "Láminas beta", False),
          ("Unión", "Puente S-S", False)],
       "pie": "Base de la familia"}]},
  ["El MHC I tiene β2-microglobulina, también tipo Ig.",
   "CD4 se une al MHC II; CD8 al MHC I.",
   "Elegir «ninguna» exige conocer a todos los miembros."],
  ABBAS)

# CB-096 · matriz
V("matriz", "CB-096", "intolerancia-idiosincrasia-tolerancia-definiciones", "Reacciones anormales a fármacos",
  "CIENCIAS BÁSICAS ENAM: FARMACOLOGÍA GENERAL", CB,
  ("Reacciones anormales a los fármacos", ["Pueden diferir en cantidad o en tipo",
   "Cada opción del caso cambia una definición"]),
  ("Pregunta de farmacología", ["¿Qué definición es correcta?", "Todas están intercambiadas"]),
  {"rotulo": "Definición correcta", "eje_x": "Rasgo", "eje_y": "Término",
   "cols": ["Diferencia", "Ejemplo"], "rows": ["Intolerancia", "Idiosincrasia", "Tolerancia"], "caso": (1, 0),
   "cells": [[("Cuantitativa", ["Efecto exagerado", "a dosis habitual"]), ("Tinnitus con AAS", ["a dosis baja"])],
             [("CUALITATIVA", ["Genética, no inmune"]), ("Primaquina", ["Hemólisis en G6PD"])],
             [("Efecto menor", ["Por uso repetido"]), ("Opioides", ["Obliga a subir dosis"])]]},
  ["La reacción inmunológica se llama alergia.",
   "Idiosincrasia: base farmacogenética.",
   "Tolerancia no es pasajera ni congénita."],
  GOODMAN)

# CB-097 · árbol
A("CB-097", "hipersensibilidad-gell-coombs-goodpasture-tuberculosis", "Tipos de hipersensibilidad",
  "CIENCIAS BÁSICAS ENAM: HIPERSENSIBILIDAD", CB,
  ("Clasificación de Gell y Coombs", ["I IgE · II anticuerpo contra tejido",
   "III inmunocomplejos · IV linfocitos T"]),
  ("Pregunta de inmunología", ["Relacionar tipos con ejemplos", "Goodpasture, TBC, anafilaxia, enf. del suero"]),
  Q("¿Participan anticuerpos?", [
      Q("¿Es IgE sobre mastocitos?", [
          L("Sí", "TIPO I", ["Anafilaxia (a-3)"], path=True),
          Q("¿Antígeno fijo al tejido?", [
              L("Sí", "TIPO II", ["Goodpasture (b-1)"], path=True),
              L("No", "TIPO III", ["Enf. del suero (c-4)"], path=True)], edge="No", path=True)],
        edge="Sí", path=True),
      L("No", "TIPO IV", ["Tuberculosis (d-2)", "Mediada por linfocitos T"], path=True)], path=True),
  ("Tiempo de aparición", [("Tipo I", True), ("Tipo IV", False)], [
      ("Inicio", ["Minutos", "48-72 horas"]),
      ("Prueba", ["Prick test", "PPD (tuberculina)"])]),
  ["Combinación correcta: a-3, b-1, c-4, d-2.",
   "Tipo II: anemia hemolítica, miastenia, Graves.",
   "Tipo III: lupus y glomerulonefritis posestreptocócica."],
  ABBAS)

# CB-098 · embudo
V("embudo", "CB-098", "disgenesia-reticular-scid-sin-linfocitos-ni-neutrofilos", "Inmunodeficiencia sin leucocitos",
  "CIENCIAS BÁSICAS ENAM: INMUNODEFICIENCIAS", CB,
  ("Inmunodeficiencias primarias", ["Pueden afectar células B, T, ambas o fagocitos",
   "La más grave falla en la célula madre"]),
  ("Pregunta de inmunología", ["Faltan linfocitos B, T y neutrófilos", "¿Qué inmunodeficiencia es?"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Inmunodeficiencia congénita",
   "candidatos": ["Disgenesia reticular", "DiGeorge", "Wiskott-Aldrich", "Bruton"],
   "pasos": [("Afecta B y T a la vez", ["DiGeorge", "Bruton"]),
             ("Faltan también neutrófilos", ["Wiskott-Aldrich"])],
   "final": ("DISGENESIA RETICULAR", ["Mutación de AK2 · sordera", "Trasplante de progenitores"]),
   "nota": "DiGeorge: timo ausente (T). Bruton: sin células B (BTK)."},
  ["Es la forma más grave de inmunodeficiencia combinada.",
   "Wiskott-Aldrich: eccema, plaquetas pequeñas.",
   "Sin trasplante es mortal en meses."],
  ABBAS)

# CB-099 · radial
V("radial", "CB-099", "orificios-diafragma-vena-cava-t8-centro-tendinoso", "Orificios del diafragma",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA DEL DIAFRAGMA", CB,
  ("Orificios del diafragma", ["Vena cava T8, esófago T10, aorta T12",
   "Solo el de la cava está en el centro tendinoso"]),
  ("Pregunta de anatomía", ["Abertura entre hojas anterior y derecha", "del tendón central"]),
  {"rotulo": "Mapa del tema", "centro": "DIAFRAGMA", "centro_sub": "Orificios", "ans": 0,
   "items": [("VENA CAVA", ["T8 · tendón central", "Nervio frénico der."]),
             ("Esofágico", ["T10 · pilar derecho", "Nervios vagos"]),
             ("Aórtico", ["T12 · retrocrural", "Conducto torácico"]),
             ("Inervación", ["Nervio frénico C3-C5"]),
             ("Trígono", ["Costovertebral", "Hernia de Bochdalek"])],
   "ruta": ["Tendón central", "Hojas anterior y derecha", "Nivel T8", "VENA CAVA"]},
  ["La inspiración abre el orificio de la cava.",
   "Regla: 8, 10 y 12 de arriba abajo.",
   "Hernia de Bochdalek: posterolateral, en el neonato."],
  MOORE)

# CB-100 · árbol
A("CB-100", "cuerda-del-timpano-facial-gusto-lingual", "Cuerda del tímpano",
  "CIENCIAS BÁSICAS ENAM: NERVIO FACIAL", CB,
  ("Cuerda del tímpano", ["Rama del facial que cruza la caja del tímpano",
   "Se une al nervio lingual (V3)"]),
  ("Pregunta de anatomía", ["¿Qué afirmación es verdadera?", "Todas las opciones son falsas"]),
  Q("¿Qué lleva la cuerda del tímpano?", [
      L("Gusto", "2/3 ANTERIORES", ["De la lengua", "No el tercio posterior"], path=True),
      L("Parasimpático", "Submandibular", ["Y sublingual", "Ganglio submandibular"]),
      L("No hace", "Membrana timpánica", ["Solo la cruza", "No la inerva"])], path=True),
  ("Opciones del caso", [("Dice", True), ("Realidad", False)], [
      ("Se une a", ["Nervio bucal", "Nervio lingual"]),
      ("Nace de", ["Glosofaríngeo", "Facial (VII)"])]),
  ["Por eso la opción correcta es «ninguna anterior».",
   "Tercio posterior de la lengua: IX par.",
   "Parálisis facial alta: pierde el gusto anterior."],
  MOORE)

# CB-101 · puntaje
V("puntaje", "CB-101", "bifurcacion-carotida-comun-borde-superior-tiroides-c4", "Niveles vertebrales del cuello",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA DEL CUELLO", CB,
  ("Referencias del cuello", ["Hioides C3, tiroides C4, cricoides C6",
   "La carótida común se divide en el borde superior del tiroides"]),
  ("Pregunta de anatomía", ["¿A qué nivel se divide la carótida común?"]),
  {"rotulo": "Nivel vertebral", "escala": "Vértebra", "total": 4, "max": 7,
   "total_label": "Bifurcación",
   "interpreta": "C4: borde superior del tiroides",
   "items": [("Hioides", "C3", False), ("CARTÍLAGO TIROIDES", "C4", True),
             ("Cricoides", "C6", False)],
   "bandas": [("C3", "Hioides", "Límite del suelo de boca", False),
              ("C4", "Tiroides", "Bifurcación carotídea", True),
              ("C6", "Cricoides", "Inicio de esófago y tráquea", False)]},
  ["En la bifurcación: seno carotídeo (barorreceptor).",
   "Cuerpo carotídeo: quimiorreceptor (IX par).",
   "El masaje del seno carotídeo produce bradicardia."],
  MOORE)

# CB-102 · tarjetas
V("tarjetas", "CB-102", "musculos-infrahioideos-omohioideo-en-cinta", "Músculos del hioides",
  "CIENCIAS BÁSICAS ENAM: MÚSCULOS DEL CUELLO", CB,
  ("Músculos suprahioideos e infrahioideos", ["Los supra elevan el hioide; los infra lo descienden",
   "Los infrahioideos son los «músculos en cinta»"]),
  ("Pregunta de anatomía", ["¿Cuál pertenece a los infrahioideos?"]),
  {"rotulo": "¿Infra o suprahioideo?", "ans": 0, "cards": [
      {"titulo": "OMOHIOIDEO", "datos": [
          ("Grupo", "Infrahioideo", True), ("Vientres", "Dos", True),
          ("Inervación", "Asa cervical", True)],
       "pie": "Tendón fijado a la clavícula"},
      {"titulo": "Milohioideo", "datos": [
          ("Grupo", "Suprahioideo", False), ("Función", "Piso de boca", False),
          ("Inervación", "V3", False)],
       "pie": "Diafragma oral"},
      {"titulo": "Genihioideo", "datos": [
          ("Grupo", "Suprahioideo", False), ("Función", "Eleva hioides", False),
          ("Inervación", "C1 (vía XII)", False)],
       "pie": "Sobre el milohioideo"},
      {"titulo": "Digástrico", "datos": [
          ("Grupo", "Suprahioideo", False), ("Vientres", "Dos", False),
          ("Inervación", "V3 y VII", False)],
       "pie": "Anterior V3, posterior VII"}]},
  ["Infrahioideos: esternohioideo, omohioideo,",
   "esternotiroideo y tirohioideo.",
   "El omohioideo cruza la yugular interna."],
  MOORE)

# CB-103 · embudo
V("embudo", "CB-103", "espacio-perineal-profundo-glandulas-bulbouretrales-cowper", "Contenido del periné profundo",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA DEL PERINÉ", CB,
  ("Espacios del periné", ["Profundo: transverso profundo, uretra membranosa",
   "Superficial: raíz del pene, Bartholin en la mujer"]),
  ("Pregunta de anatomía", ["¿Qué hay en el transverso profundo del periné?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Estructuras del periné masculino",
   "candidatos": ["Bulbouretrales", "Vestibulares", "Uretra prostática", "Uretra esponjosa"],
   "pasos": [("Es del varón y es una glándula", ["Vestibulares"]),
             ("Está en el espacio profundo", ["Uretra prostática", "Uretra esponjosa"])],
   "final": ("GLÁNDULAS BULBOURETRALES", ["De Cowper, junto a la uretra membranosa", "Moco lubricante preeyaculatorio"]),
   "nota": "Sus homólogas femeninas (Bartholin) están en el espacio superficial."},
  ["Cowper: espacio profundo; Bartholin: superficial.",
   "Uretra prostática: sobre el diafragma urogenital.",
   "Uretra esponjosa: dentro del cuerpo esponjoso."],
  MOORE)

# CB-104 · matriz
V("matriz", "CB-104", "tecnicas-histologicas-he-orceina-pas-sustancia-fundamental", "Tinciones en histología",
  "CIENCIAS BÁSICAS ENAM: TÉCNICAS HISTOLÓGICAS", CB,
  ("Tinciones histológicas", ["Hematoxilina: basófilo (azul) · Eosina: acidófilo (rosado)",
   "Tinciones especiales para fibras y matriz"]),
  ("Pregunta de histología", ["¿Qué afirmación es falsa?"]),
  {"rotulo": "Estructura y tinción", "eje_x": "Técnica", "eje_y": "Estructura",
   "cols": ["H-E", "Especial"], "rows": ["Fibras elásticas", "Fibras reticulares", "Sust. fundamental"], "caso": (2, 0),
   "cells": [[("Rosado pálido", ["Poco visibles"]), ("Orceína", ["Fibras oscuras"])],
             [("Poco visibles", ["Colágeno III"]), ("Plata y PAS", ["Argirófilas"])],
             [("NO SE TIÑE", ["Se pierde al fijar", "Espacio claro"]), ("PAS, alcián", ["Azul de toluidina"])]]},
  ["La sustancia fundamental no se tiñe de azul con H-E.",
   "Heterocromatina: intensamente basófila.",
   "Colágeno I: tricrómico de Masson."],
  ROSS)

# CB-105 · fases
V("fases", "CB-105", "penicilina-pbp-transpeptidasa-pared-peptidoglucano", "Síntesis de la pared bacteriana",
  "CIENCIAS BÁSICAS ENAM: BETALACTÁMICOS", CB,
  ("Pared bacteriana", ["Peptidoglucano unido por transpeptidasas (PBP)",
   "Los betalactámicos bloquean el último paso"]),
  ("Pregunta de farmacología", ["¿Dónde actúa la penicilina?"]),
  {"rotulo": "Pasos y fármacos", "ans": 2,
   "fases": [("Citoplasma", "Paso 1", "Precursores", ["Fosfomicina", "Cicloserina"]),
             ("Membrana", "Paso 2", "Transporte", ["Bacitracina", "Vancomicina"]),
             ("Pared", "Paso 3", "PBP", ["PENICILINAS", "Cefalosporinas"])],
   "chips_titulo": "Sitio de acción · marcado el correcto",
   "chips": [("Pared celular", True), ("Síntesis de ADN", False), ("Ácido fólico", False), ("Membrana", False)]},
  ["Efecto bactericida en bacterias en división.",
   "Betalactamasas: se evitan con clavulánico.",
   "SARM: PBP2a de baja afinidad."],
  GOODMAN)

# CB-106 · tarjetas
V("tarjetas", "CB-106", "rifampicina-arn-polimerasa-rpob-tuberculosis", "Mecanismo de los antituberculosos",
  "CIENCIAS BÁSICAS ENAM: ANTITUBERCULOSOS", CB,
  ("Antituberculosos de primera línea", ["Cada uno bloquea un blanco distinto",
   "La rifampicina actúa sobre la transcripción"]),
  ("Pregunta de farmacología", ["¿Cuál inhibe la ARN polimerasa?"]),
  {"rotulo": "¿Qué bloquea?", "ans": 0, "cards": [
      {"titulo": "RIFAMPICINA", "datos": [
          ("Blanco", "ARN polimerasa", True), ("Gen", "rpoB", True),
          ("Efecto", "Bactericida", True)],
       "pie": "Orina naranja · inductor P450"},
      {"titulo": "Isoniacida", "datos": [
          ("Blanco", "Ácidos micólicos", False), ("Gen", "katG, inhA", False),
          ("Efecto", "Bactericida", False)],
       "pie": "Neuropatía: piridoxina"},
      {"titulo": "Etambutol", "datos": [
          ("Blanco", "Arabinogalactano", False), ("Gen", "embB", False),
          ("Efecto", "Bacteriostático", False)],
       "pie": "Neuritis óptica"},
      {"titulo": "Estreptomicina", "datos": [
          ("Blanco", "Ribosoma 30S", False), ("Gen", "rpsL", False),
          ("Efecto", "Bactericida", False)],
       "pie": "Ototoxicidad"}]},
  ["GeneXpert detecta mutaciones de rpoB.",
   "Rifampicina reduce la eficacia de anticonceptivos.",
   "Pirazinamida actúa en medio ácido."],
  MINSA_TB + " · " + GOODMAN)

# CB-107 · fases
V("fases", "CB-107", "hematopoyesis-embrionaria-saco-vitelino-higado-medula", "Sitios de la hematopoyesis",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA", CB,
  ("Hematopoyesis prenatal", ["Cambia de sitio a lo largo del desarrollo",
   "Saco vitelino → hígado (y bazo) → médula ósea"]),
  ("Pregunta de embriología", ["¿Dónde empieza la hematopoyesis?"]),
  {"rotulo": "Fases de la hematopoyesis", "ans": 0,
   "fases": [("Mesoblástica", "Semana 3", "SACO VITELINO", ["Islotes sanguíneos"]),
             ("Hepática", "Semana 6", "Hígado", ["Con ayuda del bazo"]),
             ("Medular", "Mes 5-7", "Médula ósea", ["Principal al nacer"])],
   "curvas": [("Médula ósea", SKY, [0.0, 0.0, 0.05, 0.2, 0.5, 0.8, 0.95])],
   "chips_titulo": "Primer sitio · marcado el correcto",
   "chips": [("Saco vitelino", True), ("Hígado", False), ("Bazo", False), ("Médula ósea", False)]},
  ["Regla: saco, hígado, bazo, médula.",
   "El timo madura linfocitos T; no inicia la hematopoyesis.",
   "Extramedular en el adulto: mielofibrosis, talasemia."],
  LANGMAN)

# CB-108 · radial
V("radial", "CB-108", "triangulo-calot-cistico-hepatico-comun-arteria-cistica", "Triángulo de Calot",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA BILIAR", CB,
  ("Triángulo de Calot", ["Referencia clave en la colecistectomía",
   "Contiene la arteria cística y el ganglio de Mascagni"]),
  ("Pregunta de anatomía", ["¿Qué estructuras lo forman?"]),
  {"rotulo": "Mapa del tema", "centro": "CALOT", "centro_sub": "Triángulo", "ans": 0,
   "items": [("LÍMITES", ["Cístico, hepático común", "y arteria cística"]),
             ("Versión actual", ["Hepatocístico: borde", "inferior del hígado"]),
             ("Contenido", ["Arteria cística", "Ganglio de Mascagni"]),
             ("Riesgo", ["Lesión de vía biliar", "Hepática derecha"]),
             ("Seguridad", ["Visión crítica", "antes de cortar"])],
   "ruta": ["Colecistectomía", "Disecar Calot", "Identificar 2 estructuras", "CLIPAR"]},
  ["Límite inferior: conducto cístico.",
   "Límite medial: conducto hepático común.",
   "Límite superior: arteria cística (clásico)."],
  MOORE)

# CB-109 · árbol
A("CB-109", "curvatura-menor-gastrica-izquierda-derecha-pilorica", "Irrigación del estómago",
  "CIENCIAS BÁSICAS ENAM: IRRIGACIÓN GÁSTRICA", CB,
  ("Irrigación del estómago", ["Dos arcos: curvatura menor y curvatura mayor",
   "Todo depende del tronco celíaco"]),
  ("Pregunta de anatomía", ["¿Qué arterias forman el arco de la curvatura menor?"]),
  Q("¿Qué curvatura?", [
      L("Menor", "GÁSTRICAS IZQ. Y DER.", ["Coronaria estomáquica", "+ pilórica"], path=True),
      L("Mayor", "Gastroepiploicas", ["Derecha e izquierda", "Vasos cortos al fondo"])], path=True),
  ("Origen de cada arteria", [("Gástrica izq.", True), ("Gástrica der.", False)], [
      ("Nace de", ["Tronco celíaco", "Hepática propia"]),
      ("Otro nombre", ["Coronaria estomáquica", "Pilórica"])]),
  ["Ambas se anastomosan en el epiplón menor.",
   "Úlcera de curvatura menor: sangra la gástrica izquierda.",
   "Úlcera bulbar posterior: gastroduodenal."],
  MOORE)

# CB-110 · embudo
V("embudo", "CB-110", "diferenciacion-gonadal-sry-no-hormona-antimulleriana", "Enunciado incorrecto en embriología genital",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA GENITAL", CB,
  ("Diferenciación sexual", ["Sexo genético (fecundación) → gónada → conductos",
   "El gen SRY decide si la gónada será testículo"]),
  ("Pregunta de embriología", ["¿Qué enunciado es incorrecto?"]),
  {"rotulo": "Embudo de enunciados",
   "inicio": "Cinco afirmaciones",
   "candidatos": ["Sexo en fecundación", "Útero de Müller", "Gónadas dirigen", "Gónada por AMH"],
   "pasos": [("Verdaderas: genética y conductos", ["Sexo en fecundación", "Útero de Müller"]),
             ("Verdadera: hormonas gonadales", ["Gónadas dirigen"])],
   "final": ("GÓNADA DEPENDE DE AMH: FALSO", ["La gónada depende del gen SRY", "La AMH solo hace regresar a Müller"]),
   "nota": "Labios mayores: pliegues labioescrotales (ectodermo)."},
  ["SRY = factor determinante testicular.",
   "AMH: células de Sertoli.",
   "Sin SRY la gónada forma ovario."],
  LANGMAN)

# CB-111 · tarjetas
V("tarjetas", "CB-111", "antioxidantes-vitamina-c-e-carotenos-cobre-cofactor", "Nutrientes antioxidantes",
  "CIENCIAS BÁSICAS ENAM: ANTIOXIDANTES", CB,
  ("Antioxidantes", ["Directos: ceden electrones a los radicales libres",
   "Cofactores: solo ayudan a enzimas antioxidantes"]),
  ("Pregunta de bioquímica", ["¿Qué nutriente no es antioxidante?"]),
  {"rotulo": "¿Antioxidante directo?", "ans": 0, "cards": [
      {"titulo": "COBRE", "datos": [
          ("Tipo", "Cofactor", True), ("Enzima", "Cu/Zn-SOD", True),
          ("Libre", "Prooxidante", True)],
       "pie": "Reacción de Fenton"},
      {"titulo": "Vitamina C", "datos": [
          ("Tipo", "Directo", False), ("Medio", "Hidrosoluble", False),
          ("Extra", "Recicla vit. E", False)],
       "pie": "Antioxidante"},
      {"titulo": "Tocoferoles", "datos": [
          ("Tipo", "Directo", False), ("Medio", "Liposoluble", False),
          ("Protege", "Membranas", False)],
       "pie": "Vitamina E"},
      {"titulo": "Carotenos", "datos": [
          ("Tipo", "Directo", False), ("Ejemplo", "Betacaroteno", False),
          ("Atrapa", "Oxígeno singlete", False)],
       "pie": "Y el retinol"}]},
  ["Zinc, manganeso y selenio también son cofactores.",
   "Glutatión peroxidasa necesita selenio.",
   "El cobre libre genera radicales hidroxilo."],
  HARPER)

# CB-112 · árbol
A("CB-112", "angioedema-alergico-via-aerea-adrenalina-intramuscular", "Tratamiento del angioedema",
  "CIENCIAS BÁSICAS ENAM: ANGIOEDEMA", CB,
  ("Angioedema", ["Edema profundo de piel y mucosas",
   "Alérgico (histamina) o por bradicinina"]),
  ("Angioedema alérgico", ["Compromiso de la vía aérea", "¿Tratamiento preferente?"]),
  Q("¿Mediador principal?", [
      Q("¿Compromiso de vía aérea?", [
          L("Sí", "ADRENALINA IM", ["0,3-0,5 mg en el muslo", "Repetir cada 5-15 min"], path=True),
          L("No", "Antihistamínico", ["Y corticoide"])], edge="Histamina", path=True),
      L("Bradicinina", "C1 inhibidor", ["Hereditario o por IECA", "Icatibant"])], path=True),
  ("Adrenalina: efectos", [("Alfa", True), ("Beta", False)], [
      ("Acción", ["Vasoconstricción", "Broncodilatación"]),
      ("Resultado", ["Menos edema", "Frena mastocitos"])]),
  ["Antihistamínicos y corticoides actúan tarde.",
   "Angioedema por IECA: no responde a adrenalina.",
   "Preparar vía aérea difícil."],
  "WAO – Anaphylaxis guidance (2020) · " + HARRISON)

# CB-113 · radial
V("radial", "CB-113", "oblicuo-superior-nervio-patetico-troclear-iv-par", "Inervación de los músculos oculares",
  "CIENCIAS BÁSICAS ENAM: PARES CRANEALES", CB,
  ("Músculos extraoculares", ["Fórmula: RL6 OS4, el resto III",
   "El oblicuo superior depende del patético (IV)"]),
  ("Pregunta de anatomía", ["¿Qué nervio inerva el oblicuo mayor?"]),
  {"rotulo": "Mapa del tema", "centro": "OJO", "centro_sub": "Pares III, IV, VI", "ans": 0,
   "items": [("PATÉTICO (IV)", ["Oblicuo superior", "Mira abajo y adentro"]),
             ("Motor ocular ext.", ["VI par", "Recto lateral"]),
             ("Motor ocular común", ["III par: rectos", "sup., inf., medial"]),
             ("III par también", ["Oblicuo inferior", "Elevador del párpado"]),
             ("Clínica del IV", ["Diplopía al bajar", "escaleras"])],
   "ruta": ["Oblicuo mayor", "Tróclea", "IV par", "PATÉTICO"]},
  ["El IV par sale por la cara dorsal del tronco.",
   "Es el de trayecto intracraneal más largo.",
   "Inclina la cabeza hacia el lado sano."],
  MOORE)

# CB-114 · fases
V("fases", "CB-114", "ciclo-krebs-matriz-mitocondrial-nadh-fadh2", "Dónde ocurre cada vía",
  "CIENCIAS BÁSICAS ENAM: METABOLISMO", CB,
  ("Compartimentos del metabolismo", ["Glucólisis en el citosol",
   "Krebs y beta-oxidación en la matriz mitocondrial"]),
  ("Pregunta de bioquímica", ["¿Dónde se lleva a cabo el ciclo de Krebs?"]),
  {"rotulo": "Recorrido de la glucosa", "ans": 1,
   "fases": [("Glucólisis", "Citosol", "Piruvato", ["2 ATP netos"]),
             ("Krebs", "Mitocondria", "MATRIZ", ["3 NADH, 1 FADH2", "1 GTP, 2 CO2"]),
             ("Cadena respiratoria", "Membrana int.", "ATP", ["Fosforilación oxidativa"])],
   "chips_titulo": "Sitio del ciclo · marcado el correcto",
   "chips": [("Mitocondria", True), ("Citosol", False), ("Núcleo", False), ("Golgi", False)]},
  ["La succinato DH está en la membrana interna.",
   "Pentosas y síntesis de ácidos grasos: citosol.",
   "Ciclo de la urea: mitocondria y citosol."],
  HARPER)

# CB-115 · embudo
V("embudo", "CB-115", "pseudomonas-ceftriaxona-sin-actividad-ceftazidima", "Antibióticos contra Pseudomonas",
  "CIENCIAS BÁSICAS ENAM: ANTIPSEUDOMONAS", CB,
  ("Pseudomonas aeruginosa", ["Bacilo gramnegativo no fermentador",
   "Resistencia natural a muchos betalactámicos"]),
  ("Pregunta de farmacología", ["¿Cuál no es activo contra Pseudomonas?"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco betalactámicos",
   "candidatos": ["Ceftriaxona", "Aztreonam", "Cefoperazona", "Pip-tazo"],
   "pasos": [("Monobactámico activo", ["Aztreonam"]),
             ("Cefalosporina o penicilina antipseudomonas", ["Cefoperazona", "Pip-tazo"])],
   "final": ("CEFTRIAXONA", ["Tercera generación sin actividad", "contra Pseudomonas"]),
   "nota": "Imipenem y meropenem sí la cubren; ertapenem no."},
  ["Antipseudomonas: ceftazidima, cefepime, carbapenémicos.",
   "También ciprofloxacino y aminoglucósidos.",
   "Neutropenia febril: betalactámico antipseudomonas."],
  SANFORD)

# CB-116 · tarjetas
V("tarjetas", "CB-116", "bacteroides-fragilis-vancomicina-sin-actividad-metronidazol", "Fármacos contra Bacteroides fragilis",
  "CIENCIAS BÁSICAS ENAM: ANAEROBIOS", CB,
  ("Bacteroides fragilis", ["Anaerobio gramnegativo del colon",
   "Principal agente de abscesos intraabdominales"]),
  ("Pregunta de farmacología", ["¿Cuál no actúa contra B. fragilis?"]),
  {"rotulo": "¿Cubre B. fragilis?", "ans": 0, "cards": [
      {"titulo": "VANCOMICINA", "datos": [
          ("Espectro", "Solo grampositivos", True), ("Motivo", "No cruza membrana", True),
          ("Cubre", "NO", True)],
       "pie": "Glucopéptido grande"},
      {"titulo": "Metronidazol", "datos": [
          ("Espectro", "Anaerobios", False), ("Uso", "De elección", False),
          ("Cubre", "Sí", False)],
       "pie": "Nitroimidazol"},
      {"titulo": "Cefoxitina", "datos": [
          ("Grupo", "Cefamicina", False), ("Uso", "Profilaxis colon", False),
          ("Cubre", "Sí", False)],
       "pie": "Resistencia creciente"},
      {"titulo": "Clindamicina", "datos": [
          ("Grupo", "Lincosamida", False), ("Uso", "Anaerobios", False),
          ("Cubre", "Sí, variable", False)],
       "pie": "Resistencia creciente"}]},
  ["El cloranfenicol también cubre anaerobios.",
   "Peritonitis: cubrir enterobacterias y anaerobios.",
   "Carbapenémicos y pip-tazo: cubren B. fragilis."],
  SANFORD)

# CB-117 · termómetro
V("termometro", "CB-117", "osteomielitis-antibiotico-seis-semanas-staphylococcus", "Duración del antibiótico en infecciones",
  "CIENCIAS BÁSICAS ENAM: OSTEOMIELITIS", CB,
  ("Osteomielitis", ["Hueso mal irrigado con secuestros",
   "Requiere antibiótico prolongado"]),
  ("Pregunta de infectología", ["¿Cuántas semanas como mínimo?"]),
  {"rotulo": "Duración según infección",
   "niveles": [("1 semana", "Cistitis, celulitis", ["Cursos cortos"]),
               ("2 semanas", "Bacteriemia S. aureus", ["Sin complicaciones"]),
               ("4 semanas", "Artritis séptica", ["Endocarditis nativa"]),
               ("6 semanas", "OSTEOMIELITIS", ["Mínimo en el adulto", "Más si hay prótesis"])],
   "caso_nivel": 3, "ruta_titulo": "Manejo de la osteomielitis", "paso_label": "PASO",
   "pasos": [(1, "Cultivo del hueso", ["Antes del antibiótico"], False),
             (2, "Antibiótico ≥ 6 semanas", ["Inicio IV, luego oral"], True),
             (3, "Desbridar secuestros", ["Si hay abscesos"], False)]},
  ["Germen principal: S. aureus.",
   "Drepanocitosis: Salmonella.",
   "Punción por calzado: Pseudomonas."],
  "IDSA – Vertebral osteomyelitis guideline (2015) · " + HARRISON)

# CB-118 · matriz
V("matriz", "CB-118", "diureticos-efectos-adversos-ginecomastia-no-anemia-hemolitica", "Efectos adversos de los diuréticos",
  "CIENCIAS BÁSICAS ENAM: DIURÉTICOS", CB,
  ("Efectos adversos de los diuréticos", ["Se deducen de su mecanismo",
   "La anemia hemolítica es excepcional"]),
  ("Pregunta de farmacología", ["¿Cuál no es un efecto frecuente?"]),
  {"rotulo": "Efecto según el grupo", "eje_x": "Grupo", "eje_y": "Efecto",
   "cols": ["Tiazida/asa", "Espironolactona"], "rows": ["Metabólico", "Hormonal", "Hematológico"], "caso": (2, 0),
   "cells": [[("Frecuente", ["Hipo K, hiperglucemia", "Dislipidemia"]), ("Hiperpotasemia", ["Acidosis leve"])],
             [("Raro", ["Calambres por hipo K"]), ("Ginecomastia", ["Antiandrógeno"])],
             [("EXCEPCIONAL", ["Anemia hemolítica"]), ("No descrito", ["—"])]]},
  ["Tiazidas: hiponatremia en adultos mayores.",
   "Furosemida en dosis altas: ototoxicidad.",
   "Hiperuricemia: tiazidas y de asa."],
  GOODMAN)

# CB-119 · árbol
A("CB-119", "pie-caido-equino-nervio-peroneo-profundo-tibial-anterior", "Pie caído",
  "CIENCIAS BÁSICAS ENAM: NERVIOS DEL MIEMBRO INFERIOR", CB,
  ("Pie caído (equino)", ["Parálisis de los dorsiflexores del tobillo",
   "Marcha en steppage"]),
  ("Pregunta de anatomía", ["¿Qué nervio se lesiona?"]),
  Q("¿Qué movimiento falla?", [
      L("Dorsiflexión", "PERONEO PROFUNDO", ["Antes: tibial anterior", "Pie equino o caído"], path=True),
      L("Flexión plantar", "Tibial", ["Pie talo"]),
      L("Extensión rodilla", "Femoral", ["Cuádriceps"])], path=True),
  ("Nervio peroneo", [("Profundo", True), ("Superficial", False)], [
      ("Motor", ["Dorsiflexores", "Peroneos laterales"]),
      ("Piel", ["1.er espacio dorsal", "Dorso del pie"])]),
  ["Sitio de lesión: cuello del peroné.",
   "Causas: yeso apretado, cruzar las piernas.",
   "Tratamiento: férula antiequino."],
  MOORE)

# CB-120 · fases
V("fases", "CB-120", "anhidrasa-carbonica-acetazolamida-perdida-bicarbonato", "Inhibición de la anhidrasa carbónica",
  "CIENCIAS BÁSICAS ENAM: ACETAZOLAMIDA", CB,
  ("Anhidrasa carbónica renal", ["Permite reabsorber el 85 % del bicarbonato",
   "En el túbulo proximal"]),
  ("Pregunta de farmacología", ["¿Qué causa inhibir la anhidrasa carbónica?"]),
  {"rotulo": "Secuencia del efecto", "ans": 1,
   "fases": [("Bloqueo", "Túbulo proximal", "Acetazolamida", ["No se reabsorbe HCO3"]),
             ("Orina", "Horas", "BICARBONATURIA", ["Orina alcalina", "Pierde Na y K"]),
             ("Plasma", "Días", "Acidosis", ["Hiperclorémica"])],
   "chips_titulo": "Efecto · marcado el correcto",
   "chips": [("Menos HCO3 plasmático", True), ("Retiene K", False), ("Menos diuresis", False), ("Glucosuria", False)]},
  ["Usos: alcalosis metabólica, mal de altura, glaucoma.",
   "Efectos: hipopotasemia y parestesias.",
   "Cálculos de fosfato cálcico por orina alcalina."],
  GOODMAN)

# CB-121 · puntaje
V("puntaje", "CB-121", "diafragma-nervio-frenico-c3-c4-c5", "Raíces del nervio frénico",
  "CIENCIAS BÁSICAS ENAM: INERVACIÓN DEL DIAFRAGMA", CB,
  ("Nervio frénico", ["Única inervación motora del diafragma",
   "«C3, 4 y 5 mantienen vivo al diafragma»"]),
  ("Pregunta de anatomía", ["¿Qué nervio inerva el diafragma?"]),
  {"rotulo": "Raíces del frénico", "escala": "Raíces", "total": 3, "max": 3,
   "total_label": "Raíces que aporta",
   "interpreta": "Nervio frénico",
   "items": [("Raíz C3", "1", True), ("Raíz C4 (principal)", "1", True), ("Raíz C5", "1", True)],
   "bandas": [("Sobre C3", "Lesión alta", "Ventilación mecánica", True),
              ("C4-C5", "Parcial", "Debilidad diafragmática", False),
              ("Bajo C5", "Frénico sano", "Respira con diafragma", False)]},
  ["El frénico baja por delante del escaleno anterior.",
   "Dolor diafragmático referido al hombro (C4).",
   "XI par: trapecio y ECM; XII: lengua."],
  MOORE)

# CB-122 · puntaje
V("puntaje", "CB-122", "suero-fisiologico-nacl-09-154-meq-sodio", "Sodio de las soluciones salinas",
  "CIENCIAS BÁSICAS ENAM: SOLUCIONES", CB,
  ("Solución salina al 0,9 %", ["9 g de NaCl por litro",
   "9000 mg ÷ 58,5 = 154 mEq/L de Na y de Cl"]),
  ("Pregunta de fisiología", ["¿Cuánto sodio tiene el suero fisiológico?"]),
  {"rotulo": "Cálculo", "escala": "mEq/L", "total": 154, "max": 513,
   "total_label": "Sodio del NaCl 0,9 %",
   "interpreta": "154 mEq/L de sodio",
   "items": [("NaCl por litro", "9 g", True), ("Peso molecular", "58,5", True),
             ("Resultado", "154 mEq", True)],
   "bandas": [("130", "Ringer lactato", "Más fisiológico", False),
              ("154", "NaCl 0,9 %", "Reanimación", True),
              ("513", "NaCl 3 %", "Hiponatremia grave", False)]},
  ["Tiene más cloro que el plasma (103).",
   "Grandes volúmenes: acidosis hiperclorémica.",
   "NaCl 20 %: unos 3,4 mEq/mL."],
  GUYTON)

# CB-123 · embudo
V("embudo", "CB-123", "econazol-antimicotico-topico-no-sistemico", "Antimicóticos sistémicos y tópicos",
  "CIENCIAS BÁSICAS ENAM: ANTIMICÓTICOS", CB,
  ("Antimicóticos", ["Sistémicos: se absorben y tratan micosis profundas",
   "Tópicos: piel, uñas y mucosas"]),
  ("Pregunta de farmacología", ["¿Cuál no es antimicótico sistémico?"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco antimicóticos",
   "candidatos": ["Econazol", "Anfotericina B", "Fluconazol", "Flucitosina"],
   "pasos": [("Uso IV en micosis graves", ["Anfotericina B"]),
             ("Uso oral sistémico", ["Fluconazol", "Flucitosina"])],
   "final": ("ECONAZOL", ["Imidazol solo tópico", "Cremas y óvulos"]),
   "nota": "Ketoconazol oral: se usa poco por hepatotoxicidad."},
  ["Tópicos: clotrimazol, miconazol, nistatina.",
   "Anfotericina: nefrotóxica.",
   "Flucitosina + anfotericina en criptococosis."],
  GOODMAN)

# CB-124 · termómetro
V("termometro", "CB-124", "reacciones-cutaneas-antibioticos-betalactamicos-mas-frecuentes", "Reacciones cutáneas por antibióticos",
  "CIENCIAS BÁSICAS ENAM: ALERGIA A FÁRMACOS", CB,
  ("Reacciones cutáneas a antibióticos", ["Son el efecto alérgico más común",
   "Los betalactámicos lideran por su uso masivo"]),
  ("Pregunta de farmacología", ["¿Qué grupo causa más reacciones dérmicas?"]),
  {"rotulo": "Frecuencia de reacciones",
   "niveles": [("Baja", "Macrólidos", ["Eritromicina"]),
               ("Media", "Quinolonas", ["Fotosensibilidad"]),
               ("Alta", "Cotrimoxazol", ["Stevens-Johnson"]),
               ("Muy alta", "BETALACTÁMICOS", ["Urticaria, exantema"])],
   "caso_nivel": 3, "ruta_titulo": "Ante alergia a penicilina", "paso_label": "PASO",
   "pasos": [(1, "Precisar la reacción", ["Inmediata o tardía"], True),
             (2, "Evitar penicilinas", ["Anotar en la historia"], False),
             (3, "Valorar cefalosporinas", ["Cruce bajo con 3.ª gen."], False)]},
  ["Amoxicilina en mononucleosis: exantema no alérgico.",
   "Anafilaxia: mediada por IgE.",
   "Cotrimoxazol: reacciones graves pero menos comunes."],
  GOODMAN)

# CB-125 · árbol
A("CB-125", "profilaxis-antibiotica-indicaciones-no-gastroenteritis", "Indicaciones de profilaxis antibiótica",
  "CIENCIAS BÁSICAS ENAM: PROFILAXIS", CB,
  ("Profilaxis antibiótica", ["Solo cuando el riesgo es alto",
   "Y el beneficio está demostrado"]),
  ("Pregunta de infectología", ["¿Cuál no es indicación de profilaxis?"]),
  Q("¿Hay beneficio demostrado?", [
      L("Sí", "Indicada", ["Cardiopatía cianótica", "Contacto meningocócico", "Asplenia · RVU"]),
      L("No", "GASTROENTERITIS", ["Recidivante: viral casi siempre", "Solo rehidratar"], path=True)], path=True),
  ("Ejemplos de profilaxis", [("Situación", True), ("Fármaco", False)], [
      ("Meningococo", ["Contacto cercano", "Rifampicina o cipro"]),
      ("Asplenia", ["Niño esplenectomizado", "Penicilina"])]),
  ["El antibiótico innecesario selecciona resistencias.",
   "Endocarditis: solo cardiopatías de alto riesgo.",
   "Otitis recurrente: ya no se recomienda profilaxis."],
  SANFORD)

# CB-126 · radial
V("radial", "CB-126", "agenesia-mulleriana-rokitansky-malformacion-renal", "Agenesia mülleriana",
  "CIENCIAS BÁSICAS ENAM: MALFORMACIONES GENITALES", CB,
  ("Síndrome de Rokitansky", ["Sin útero ni 2/3 superiores de vagina",
   "Ovarios normales y cariotipo 46,XX"]),
  ("Pregunta de embriología", ["¿A qué malformaciones se asocia?"]),
  {"rotulo": "Mapa del tema", "centro": "MÜLLER", "centro_sub": "Agenesia", "ans": 0,
   "items": [("URINARIAS", ["Agenesia renal", "Riñón pélvico"]),
             ("Clínica", ["Amenorrea primaria"]),
             ("Ovarios", ["Normales"]),
             ("Esqueleto", ["Vértebras (MURCS)"]),
             ("Estudio", ["Ecografía renal"])],
   "ruta": ["Müller y Wolff juntos", "Wolff induce el riñón", "Falla común", "TRACTO URINARIO"]},
  ["Asociación en 25-40 % de los casos.",
   "Caracteres sexuales secundarios normales.",
   "Vagina corta: dilatación o neovagina."],
  LANGMAN)

# CB-127 · embudo
V("embudo", "CB-127", "surco-deltopectoral-vena-cefalica-flebotomia", "Venas del miembro superior",
  "CIENCIAS BÁSICAS ENAM: VENAS SUPERFICIALES", CB,
  ("Venas superficiales del brazo", ["Cefálica: lateral · Basílica: medial",
   "La cefálica sube por el surco deltopectoral"]),
  ("Pregunta de anatomía", ["¿Qué vena pasa entre deltoides y pectoral mayor?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Venas del brazo",
   "candidatos": ["Cefálica", "Basílica", "Humeral", "Axilar"],
   "pasos": [("Es superficial", ["Humeral", "Axilar"]),
             ("Va por el lado lateral", ["Basílica"])],
   "final": ("VENA CEFÁLICA", ["Surco deltopectoral", "Drena en la axilar"]),
   "nota": "Uso: marcapasos y catéteres por disección."},
  ["Nace en la tabaquera anatómica.",
   "Atraviesa la fascia clavipectoral.",
   "Basílica + braquiales = axilar."],
  MOORE)

# CB-128 · matriz
V("matriz", "CB-128", "articulacion-radiocarpiana-condilea-elipsoidea-biaxial", "Tipos de articulación sinovial",
  "CIENCIAS BÁSICAS ENAM: ARTICULACIONES", CB,
  ("Articulaciones sinoviales", ["Se clasifican por la forma y los ejes",
   "La muñeca es condílea (elipsoidea)"]),
  ("Pregunta de anatomía", ["¿Qué tipo es la radiocarpiana?"]),
  {"rotulo": "Tipo y ejes", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Ejes", "Ejemplo"], "rows": ["Condílea", "Enartrosis", "Trocoide"], "caso": (0, 1),
   "cells": [[("Biaxial", ["Sin rotación"]), ("RADIOCARPIANA", ["Muñeca"])],
             [("Multiaxial", ["Todos los ejes"]), ("Hombro, cadera", [])],
             [("Uniaxial", ["Rotación"]), ("Radiocubital prox.", [])]]},
  ["Tróclea: codo humerocubital.",
   "Silla de montar: trapeciometacarpiana.",
   "Plana: intercarpianas."],
  MOORE)

# CB-129 · radial
V("radial", "CB-129", "fila-proximal-carpo-pisiforme-piramidal-semilunar-escafoides", "Huesos del carpo",
  "CIENCIAS BÁSICAS ENAM: HUESOS DE LA MANO", CB,
  ("Huesos del carpo", ["Dos filas de cuatro huesos",
   "Proximal: escafoides, semilunar, piramidal, pisiforme"]),
  ("Pregunta de anatomía", ["Primera fila de adentro hacia afuera"]),
  {"rotulo": "Mapa del tema", "centro": "CARPO", "centro_sub": "Fila proximal", "ans": 0,
   "items": [("DE MEDIAL A LAT.", ["Pisiforme, piramidal", "semilunar, escafoides"]),
             ("Fila distal", ["Ganchoso, grande", "trapezoide, trapecio"]),
             ("Más fracturado", ["Escafoides"]),
             ("Más luxado", ["Semilunar"]),
             ("Sesamoideo", ["Pisiforme"])],
   "ruta": ["Pisiforme", "Piramidal", "Semilunar", "ESCAFOIDES"]},
  ["Adentro = medial (cubital).",
   "Escafoides: dolor en la tabaquera anatómica.",
   "Riesgo de necrosis del polo proximal."],
  MOORE)

# CB-130 · tarjetas
V("tarjetas", "CB-130", "sodio-corporal-total-hueso-reserva", "Dónde está el sodio del cuerpo",
  "CIENCIAS BÁSICAS ENAM: SODIO CORPORAL", CB,
  ("Distribución del sodio", ["Cerca del 40 % está en el hueso",
   "El resto casi todo en el líquido extracelular"]),
  ("Pregunta de fisiología", ["¿Qué compartimento tiene más sodio?"]),
  {"rotulo": "Reserva de sodio", "ans": 0, "cards": [
      {"titulo": "HUESO", "datos": [
          ("Porcentaje", "≈ 40 %", True), ("Forma", "Hidroxiapatita", True),
          ("Recambio", "Lento", True)],
       "pie": "Gran reserva"},
      {"titulo": "Extracelular", "datos": [
          ("Porcentaje", "≈ 50 %", False), ("Concentración", "140 mEq/L", False),
          ("Recambio", "Rápido", False)],
       "pie": "Plasma e intersticio"},
      {"titulo": "Intracelular", "datos": [
          ("Porcentaje", "< 10 %", False), ("Concentración", "10-15 mEq/L", False),
          ("Motivo", "Bomba Na/K", False)],
       "pie": "Músculo, nervio"},
      {"titulo": "Piel", "datos": [
          ("Porcentaje", "Pequeño", False), ("Forma", "Unido a matriz", False),
          ("Recambio", "Variable", False)],
       "pie": "Depósito menor"}]},
  ["La natremia no mide el sodio total.",
   "Refleja la relación sodio/agua.",
   "El sodio total define el volumen extracelular."],
  GUYTON)

# CB-131 · fases
V("fases", "CB-131", "comida-grasa-colecistocinina-colico-biliar", "Colecistocinina y cólico biliar",
  "CIENCIAS BÁSICAS ENAM: HORMONAS DIGESTIVAS", CB,
  ("Colecistocinina (CCK)", ["La liberan las células I del duodeno",
   "Estímulo: grasas y proteínas"]),
  ("Mujer de 30 años", ["Dolor abdominal tras comida grasa", "¿Qué hormona aumenta el dolor?"]),
  {"rotulo": "Secuencia tras la comida", "ans": 1,
   "fases": [("Llegada", "Minutos", "Grasa al duodeno", ["Células I"]),
             ("Hormona", "30-60 min", "CCK", ["Contrae la vesícula", "Relaja el Oddi"]),
             ("Dolor", "Cólico", "Cálculo en cístico", ["Epigastrio, hombro der."])],
   "chips_titulo": "Hormona responsable · marcada la correcta",
   "chips": [("Colecistocinina", True), ("Gastrina", False), ("Histamina", False), ("Acetilcolina", False)]},
  ["La CCK también estimula enzimas pancreáticas.",
   "Enteroquinasa: enzima, no hormona.",
   "HIDA con CCK: fracción de eyección vesicular."],
  GUYTON)

# CB-132 · termómetro
V("termometro", "CB-132", "sodio-liquido-intersticial-mayor-volumen-extracelular", "Compartimentos líquidos",
  "CIENCIAS BÁSICAS ENAM: LÍQUIDOS CORPORALES", CB,
  ("Líquidos corporales", ["Agua corporal total ≈ 60 % del peso",
   "2/3 intracelular y 1/3 extracelular"]),
  ("Pregunta de fisiología", ["¿Dónde está la mayor cantidad de sodio líquido?"]),
  {"rotulo": "Volumen en un adulto de 70 kg",
   "niveles": [("Plasma", "≈ 3 L", ["Na 140 mEq/L"]),
               ("Intersticial", "≈ 11 L", ["Na 140 mEq/L", "MÁS SODIO TOTAL"]),
               ("Intracelular", "≈ 28 L", ["Na 10-15 mEq/L"]),
               ("Transcelular", "≈ 1 L", ["LCR, sinovial"])],
   "caso_nivel": 1, "ruta_titulo": "Razonamiento", "paso_label": "PASO",
   "pasos": [(1, "Misma concentración", ["Plasma e intersticio"], False),
             (2, "Mayor volumen", ["Intersticio 3 veces más"], True),
             (3, "Más sodio total", ["Intersticial"], True)]},
  ["Intracelular: predomina el potasio.",
   "Sodio: principal catión extracelular.",
   "El riñón regula el sodio, no lo almacena."],
  GUYTON)
