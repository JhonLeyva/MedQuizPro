"""Ciencias Básicas · parte F (CB-293 a CB-332)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-293 · embudo
V("embudo", "CB-293", "agenesia-conductos-muller-ausencia-utero-ovarios-normales", "Qué falta en la agenesia mülleriana",
  "CIENCIAS BÁSICAS ENAM: CONDUCTOS DE MÜLLER", CB,
  ("Conductos de Müller", ["Forman trompas, útero, cuello y vagina superior",
   "Los ovarios vienen de la cresta gonadal"]),
  ("Pregunta de embriología", ["¿Qué produce la agenesia de Müller?"]),
  {"rotulo": "Embudo embriológico",
   "inicio": "Cinco posibles hallazgos",
   "candidatos": ["Sin útero", "Sin ovarios", "Útero didelfo", "Sin vagina inferior"],
   "pasos": [("No depende de Müller", ["Sin ovarios", "Sin vagina inferior"]),
             ("Es agenesia, no fusión", ["Útero didelfo"])],
   "final": ("AUSENCIA DE ÚTERO", ["Y de la vagina superior", "Síndrome de Rokitansky"]),
   "nota": "Vagina inferior: seno urogenital."},
  ["Amenorrea primaria con caracteres normales.",
   "Buscar malformaciones renales.",
   "Útero tabicado: falla la reabsorción."],
  LANGMAN)

# CB-294 · árbol
A("CB-294", "nino-clorfenamina-5-horas-soporte-anticolinergico", "Intoxicación por antihistamínicos",
  "CIENCIAS BÁSICAS ENAM: ANTIHISTAMÍNICOS", CB,
  ("Sobredosis de antihistamínicos H1", ["Síndrome anticolinérgico",
   "Mucosas secas, rubor, midriasis, taquicardia"]),
  ("Niño que tomó un frasco de clorfenamina", ["Hace 5 horas", "Mucosas secas y rubicundo"]),
  Q("¿Delirio grave sin QRS ancho?", [
      L("No", "SINTOMÁTICO", ["Monitoreo y soporte", "Benzodiacepinas si agitación"], path=True),
      L("Sí", "Fisostigmina", ["Con monitoreo"])], path=True),
  ("Qué no sirve", [("Medida", True), ("Motivo", False)], [
      ("Carbón activado", ["Tras 5 horas", "Tarde"]),
      ("Atropina", ["Anticolinérgica", "Empeora"])]),
  ["Controlar temperatura y ritmo.",
   "Sonda vesical si hay retención.",
   "Naloxona y NAC: sin indicación."],
  TOXI)

# CB-295 · embudo
V("embudo", "CB-295", "sinfisis-pubis-fibrocartilago-articulacion-cartilaginosa", "Articulaciones cartilaginosas",
  "CIENCIAS BÁSICAS ENAM: ARTICULACIONES", CB,
  ("Articulaciones cartilaginosas", ["Sincondrosis: cartílago hialino",
   "Sínfisis: disco de fibrocartílago"]),
  ("Pregunta de anatomía", ["Dos huesos unidos por fibrocartílago", "como en el pubis"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Tipos de unión",
   "candidatos": ["Sínfisis", "Sincondrosis", "Sutura", "Gonfosis"],
   "pasos": [("Es cartilaginosa", ["Sutura", "Gonfosis"]),
             ("Usa fibrocartílago", ["Sincondrosis"])],
   "final": ("SÍNFISIS", ["Pubis, discos intervertebrales", "Poco móvil, línea media"]),
   "nota": "Sincondrosis: placa de crecimiento."},
  ["Suturas y gonfosis: fibrosas.",
   "Sindesmosis: tibioperonea distal.",
   "Manubrio-esternal: sínfisis."],
  MOORE)

# CB-296 · fases
V("fases", "CB-296", "espermatozoides-almacen-cola-epididimo", "Recorrido de los espermatozoides",
  "CIENCIAS BÁSICAS ENAM: VÍA ESPERMÁTICA", CB,
  ("Vía espermática", ["Del testículo al epidídimo y al deferente",
   "El almacén es la cola del epidídimo"]),
  ("Pregunta de anatomía", ["¿Dónde se almacenan antes de eyacular?"]),
  {"rotulo": "Recorrido", "ans": 1,
   "fases": [("Testículo", "Producción", "Inmóviles", ["Túbulos seminíferos"]),
             ("Epidídimo", "10-14 días", "ALMACÉN", ["Cola del epidídimo", "Ganan motilidad"]),
             ("Eyaculación", "Deferente", "Uretra", ["Con semen"])],
   "chips_titulo": "Sitio · marcado el correcto",
   "chips": [("Epidídimo", True), ("Vesícula seminal", False), ("Deferente", False), ("Uretra", False)]},
  ["Vesícula seminal: 60 % del semen.",
   "Próstata: PSA y citrato.",
   "Tras vasectomía: 20 eyaculaciones."],
  ROSS)

# CB-297 · fases
V("fases", "CB-297", "colico-antiemetico-blefaroespasmo-metoclopramida", "Distonía aguda por metoclopramida",
  "CIENCIAS BÁSICAS ENAM: EFECTOS EXTRAPIRAMIDALES", CB,
  ("Metoclopramida", ["Bloquea receptores D2",
   "Cruza al cuerpo estriado"]),
  ("Varón de 40 años", ["Náuseas y cólico, recibe sintomáticos", "Horas después: blefaroespasmo"]),
  {"rotulo": "Evolución", "ans": 1,
   "fases": [("Dosis", "Hora 0", "Antiemético", ["Bloqueo D2"]),
             ("Horas", "Estriado", "DISTONÍA", ["Blefaroespasmo", "Tortícolis, trismo"]),
             ("Tratamiento", "Minutos", "Biperideno", ["O difenhidramina IV"])],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Metoclopramida", True), ("Hioscina", False), ("Dimenhidrinato", False), ("Tramadol", False)]},
  ["Más en jóvenes y mujeres.",
   "Uso crónico: discinesia tardía.",
   "Hioscina: anticolinérgica, no distonía."],
  GOODMAN)

# CB-298 · radial
V("radial", "CB-298", "carotida-comun-derecha-tronco-braquiocefalico", "Ramas del cayado aórtico",
  "CIENCIAS BÁSICAS ENAM: ARCO AÓRTICO", CB,
  ("Cayado aórtico", ["Tres ramas: braquiocefálico, carótida",
   "común izquierda y subclavia izquierda"]),
  ("Pregunta de anatomía", ["¿De dónde nace la carótida común derecha?"]),
  {"rotulo": "Mapa del tema", "centro": "CAYADO", "centro_sub": "Aórtico", "ans": 0,
   "items": [("BRAQUIOCEFÁLICO", ["Carótida común der.", "Subclavia derecha"]),
             ("Carótida izq.", ["Directa del cayado"]),
             ("Subclavia izq.", ["Directa del cayado"]),
             ("Arco bovino", ["Tronco común"]),
             ("Lusoria", ["Subclavia der.", "aberrante: disfagia"])],
   "ruta": ["Cayado", "Tronco braquiocefálico", "Tras esternoclavicular", "CARÓTIDA DERECHA"]},
  ["El braquiocefálico se divide tras la articulación esternoclavicular.",
   "Arteria lusoria: pasa detrás del esófago.",
   "Arco bovino: variante frecuente."],
  MOORE)

# CB-299 · termómetro
V("termometro", "CB-299", "espermatograma-oligozoospermia-concentracion-baja", "Espermatograma según la OMS",
  "CIENCIAS BÁSICAS ENAM: INFERTILIDAD MASCULINA", CB,
  ("Espermatograma", ["Límite normal: 16 millones/mL",
   "Baja concentración: oligozoospermia"]),
  ("Pareja con 2 años sin embarazo", ["Varón de 31 años", "Baja concentración de espermatozoides"]),
  {"rotulo": "Concentración espermática",
   "niveles": [("Cero", "Azoospermia", ["Ni tras centrifugar"]),
               ("Tras centrifugar", "Criptozoospermia", ["Muy escasos"]),
               ("< 16 mill./mL", "OLIGOZOOSPERMIA", ["Este caso"]),
               ("≥ 16 mill./mL", "Normal", ["OMS 2021"])],
   "caso_nivel": 2, "ruta_titulo": "Otros términos", "paso_label": "TÉRMINO",
   "pasos": [(1, "Astenozoospermia", ["Poca motilidad"], False),
             (2, "Teratozoospermia", ["Formas < 4 %"], False),
             (3, "Repetir el examen", ["Varía mucho"], True)]},
  ["Infertilidad: 12 meses sin embarazo.",
   "Estudiar a ambos miembros de la pareja.",
   "Evitar calor y tabaco."],
  "OMS – Manual de laboratorio del semen 6.ª ed. (2021)")

# CB-300 · tarjetas
V("tarjetas", "CB-300", "masetero-nervio-mandibular-v3-masticacion", "Ramas del trigémino",
  "CIENCIAS BÁSICAS ENAM: NERVIO TRIGÉMINO", CB,
  ("Nervio trigémino (V)", ["Tres ramas: oftálmica, maxilar y mandibular",
   "Solo la mandibular es motora"]),
  ("Pregunta de anatomía", ["¿Qué nervio mueve el masetero?"]),
  {"rotulo": "¿Qué rama?", "ans": 0, "cards": [
      {"titulo": "MANDIBULAR (V3)", "datos": [
          ("Tipo", "Mixta", True), ("Motora", "Masticadores", True),
          ("Origen", "1.er arco", True)],
       "pie": "Masetero, temporal, pterigoideos"},
      {"titulo": "Maxilar (V2)", "datos": [
          ("Tipo", "Sensitiva", False), ("Zona", "Mejilla, dientes sup.", False),
          ("Sale", "Agujero redondo", False)],
       "pie": "Sin fibras motoras"},
      {"titulo": "Oftálmica (V1)", "datos": [
          ("Tipo", "Sensitiva", False), ("Zona", "Frente, córnea", False),
          ("Reflejo", "Corneal", False)],
       "pie": "Herpes zóster oftálmico"},
      {"titulo": "Facial (VII)", "datos": [
          ("Tipo", "Mixto", False), ("Motor", "Mímica facial", False),
          ("Origen", "2.º arco", False)],
       "pie": "No inerva masticadores"}]},
  ["Lesión: mandíbula se desvía al lado lesionado.",
   "V3 inerva tensor del tímpano.",
   "Explorar palpando el masetero."],
  MOORE)

# CB-301 · radial
V("radial", "CB-301", "poligono-willis-cerebrales-anteriores-posteriores", "Polígono de Willis",
  "CIENCIAS BÁSICAS ENAM: CIRCULACIÓN CEREBRAL", CB,
  ("Polígono de Willis", ["Une el sistema carotídeo y el vertebrobasilar",
   "Permite circulación colateral"]),
  ("Pregunta de neuroanatomía", ["¿Qué arterias forman el polígono?"]),
  {"rotulo": "Mapa del tema", "centro": "WILLIS", "centro_sub": "Polígono", "ans": 0,
   "items": [("CEREBRALES", ["Anteriores (A1)", "y posteriores (P1)"]),
             ("Comunicantes", ["Anterior y", "posteriores"]),
             ("Carótidas", ["Internas terminales"]),
             ("No incluye", ["Cerebral media", "Cerebelosas"]),
             ("Aneurismas", ["Comunicante anterior"])],
   "ruta": ["Carótidas", "Comunicantes", "Cerebrales A y P", "ANILLO"]},
  ["Rotura: hemorragia subaracnoidea.",
   "Aneurismas en bifurcaciones.",
   "Variantes anatómicas frecuentes."],
  "Snell. Neuroanatomía clínica 8.ª ed. (2019)")

# CB-302 · embudo
V("embudo", "CB-302", "nucleos-profundos-cerebelo-fastigio-globoso-emboliforme-dentado", "Núcleos del cerebelo",
  "CIENCIAS BÁSICAS ENAM: NÚCLEOS CEREBELOSOS", CB,
  ("Núcleos profundos del cerebelo", ["Cuatro en cada hemisferio",
   "De medial a lateral"]),
  ("Pregunta de neuroanatomía", ["¿Cuáles son los núcleos del cerebelo?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Núcleos del encéfalo",
   "candidatos": ["Fastigio", "Dentado", "Edinger-Westphal", "Putamen"],
   "pasos": [("No es del mesencéfalo", ["Edinger-Westphal"]),
             ("No es de ganglios basales", ["Putamen"])],
   "final": ("FASTIGIO, GLOBOSO, EMBOLIFORME, DENTADO", ["De medial a lateral", "Globoso + emboliforme = interpósito"]),
   "nota": "Edinger-Westphal: parasimpático de la pupila."},
  ["Fastigio: equilibrio.",
   "Dentado: movimientos finos.",
   "Putamen: ganglios basales."],
  "Snell. Neuroanatomía clínica 8.ª ed. (2019)")

# CB-303 · matriz
V("matriz", "CB-303", "plexo-cervical-ramos-anteriores-c1-c4", "Ramos de los nervios raquídeos",
  "CIENCIAS BÁSICAS ENAM: PLEXOS NERVIOSOS", CB,
  ("Nervio raquídeo", ["Se divide en ramo anterior y posterior",
   "Los plexos se forman con los anteriores"]),
  ("Pregunta de anatomía", ["¿Qué ramos forman el plexo cervical?"]),
  {"rotulo": "Ramos y función", "eje_x": "Ramo", "eje_y": "Dato",
   "cols": ["Anterior", "Posterior"], "rows": ["Forma plexos", "Inerva", "Ejemplo"], "caso": (0, 0),
   "cells": [[("SÍ", ["Cervical C1-C4"]), ("No", [])],
             [("Cuello, miembros", ["Diafragma"]), ("Músculos del dorso", [])],
             [("Frénico C3-C5", []), ("Occipital mayor", [])]]},
  ["Punto de Erb: ramas sensitivas.",
   "Asa cervical: infrahioideos.",
   "Bloqueo cervical en cirugía de tiroides."],
  MOORE)

# CB-304 · fases
V("fases", "CB-304", "diencefalo-prosencefalo-vesiculas-encefalicas", "Vesículas encefálicas",
  "CIENCIAS BÁSICAS ENAM: NEUROEMBRIOLOGÍA", CB,
  ("Vesículas encefálicas", ["Tres primarias en la 4.ª semana",
   "Cinco secundarias en la 5.ª semana"]),
  ("Pregunta de embriología", ["¿De qué vesícula deriva el diencéfalo?"]),
  {"rotulo": "Vesículas primarias", "ans": 0,
   "fases": [("Prosencéfalo", "Anterior", "DIENCÉFALO", ["Y telencéfalo", "Tálamo, hipotálamo"]),
             ("Mesencéfalo", "Medio", "Mesencéfalo", ["No se divide"]),
             ("Rombencéfalo", "Posterior", "Met- y mielencéfalo", ["Puente, cerebelo, bulbo"])],
   "chips_titulo": "Origen · marcado el correcto",
   "chips": [("Prosencéfalo", True), ("Rombencéfalo", False), ("Mesencéfalo", False), ("Metencéfalo", False)]},
  ["Tercer ventrículo: diencéfalo.",
   "Retina y nervio óptico: diencéfalo.",
   "Neurohipófisis: diencéfalo."],
  LANGMAN)

# CB-305 · tarjetas
V("tarjetas", "CB-305", "triangulo-auscultacion-trapecio-borde-medial-escapula", "Triángulos de la espalda",
  "CIENCIAS BÁSICAS ENAM: ESPALDA", CB,
  ("Triángulos de la espalda", ["Zonas con menos músculo",
   "Útiles para auscultar o sitios de hernia"]),
  ("Pregunta de anatomía", ["¿Qué limita el triángulo de auscultación?"]),
  {"rotulo": "¿Qué límites?", "ans": 0, "cards": [
      {"titulo": "AUSCULTACIÓN", "datos": [
          ("Abajo", "Dorsal ancho", True), ("Medial", "Trapecio", True),
          ("Lateral", "Borde escápula", True)],
       "pie": "Mejor al cruzar los brazos"},
      {"titulo": "Lumbar de Petit", "datos": [
          ("Medial", "Dorsal ancho", False), ("Lateral", "Oblicuo mayor", False),
          ("Base", "Cresta ilíaca", False)],
       "pie": "Hernia lumbar"},
      {"titulo": "Lumbar de Grynfeltt", "datos": [
          ("Arriba", "12.ª costilla", False), ("Medial", "Cuadrado lumbar", False),
          ("Lateral", "Oblicuo menor", False)],
       "pie": "Hernia superior"},
      {"titulo": "Uso clínico", "datos": [
          ("Auscultar", "Lóbulo inferior", False), ("Espacio", "6.º intercostal", False),
          ("Piso", "Romboides mayor", False)],
       "pie": "Poca masa muscular"}]},
  ["Piso: músculos intercostales.",
   "Segmentos posteriores del lóbulo inferior.",
   "Petit: hernia lumbar inferior."],
  MOORE)

# CB-306 · árbol
A("CB-306", "hemitiroidectomia-izquierda-disfonia-laringeo-recurrente", "Nervios en la tiroidectomía",
  "CIENCIAS BÁSICAS ENAM: NERVIOS LARÍNGEOS", CB,
  ("Nervios laríngeos", ["Recurrente: casi todos los músculos",
   "Superior externo: cricotiroideo"]),
  ("Paciente tras hemitiroidectomía izquierda", ["Queda disfónico", "¿Qué nervio se lesionó?"]),
  Q("¿Qué síntoma aparece?", [
      L("Disfonía", "RECURRENTE IZQ.", ["Laríngeo inferior", "Cuerda paramediana"], path=True),
      L("Voz fatigable", "Laríngeo superior", ["Pierde tonos agudos"])], path=True),
  ("Lesión del recurrente", [("Lado", True), ("Efecto", False)], [
      ("Unilateral", ["Una cuerda", "Disfonía, aspiración"]),
      ("Bilateral", ["Ambas cuerdas", "Estridor, traqueostomía"])]),
  ["El izquierdo rodea el cayado aórtico.",
   "Cerca de la arteria tiroidea inferior.",
   "Frénico: no causa disfonía."],
  MOORE)

# CB-307 · termómetro
V("termometro", "CB-307", "esofago-toracico-mediastino-superior-posterior", "Trayecto del esófago",
  "CIENCIAS BÁSICAS ENAM: ESÓFAGO", CB,
  ("Trayecto del esófago", ["Empieza en C6 y cruza el hiato en T10",
   "La porción torácica ocupa dos mediastinos"]),
  ("Pregunta de anatomía", ["¿En qué mediastino está el esófago torácico?"]),
  {"rotulo": "Niveles (de abajo arriba)",
   "niveles": [("Cuello", "C6-T1", ["Tras la tráquea"]),
               ("Mediast. sup.", "Torácico", ["ESÓFAGO TORÁCICO"]),
               ("Mediast. post.", "Torácico", ["ESÓFAGO TORÁCICO", "Tras la aurícula izq."]),
               ("Abdomen", "T10-T11", ["Tras el hiato"])],
   "caso_nivel": 2, "ruta_titulo": "Relaciones importantes", "paso_label": "PASO",
   "pasos": [(1, "Aurícula izquierda", ["Estenosis mitral"], False),
             (2, "Aorta descendente", ["A su izquierda"], False),
             (3, "Superior + posterior", ["Ubicación del caso"], True)]},
  ["Ecocardiograma transesofágico.",
   "Mediastino posterior: vagos, conducto torácico.",
   "Ácigos a la derecha."],
  MOORE)

# CB-308 · puntaje
V("puntaje", "CB-308", "estrecheces-esofago-cayado-aortico-cuerpos-extranos", "Estrecheces del esófago",
  "CIENCIAS BÁSICAS ENAM: ESTRECHECES ESOFÁGICAS", CB,
  ("Estrecheces fisiológicas", ["Cuatro puntos más estrechos",
   "Allí se detienen cuerpos extraños"]),
  ("Pregunta de anatomía", ["¿Qué estructura coincide con una estrechez?"]),
  {"rotulo": "Distancia desde la arcada", "escala": "cm", "total": 25, "max": 40,
   "total_label": "Cayado aórtico",
   "interpreta": "Estrechez aórtica",
   "items": [("Cricofaríngea", "15 cm", False), ("Cayado aórtico", "22-25 cm", True),
             ("Bronquio izquierdo", "27 cm", False)],
   "bandas": [("15 cm", "Cricofaríngea", "La más estrecha", False),
              ("25 cm", "Aórtica", "Cayado", True),
              ("40 cm", "Diafragmática", "Hiato", False)]},
  ["Monedas en niños: primera estrechez.",
   "Pila de botón: extraer en < 2 horas.",
   "Cáusticos: lesiones más graves ahí."],
  MOORE)

# CB-309 · tarjetas
V("tarjetas", "CB-309", "cartilagos-impares-laringe-cricoides-tiroides-epiglotis", "Cartílagos de la laringe",
  "CIENCIAS BÁSICAS ENAM: LARINGE", CB,
  ("Cartílagos laríngeos", ["Tres impares y tres pares",
   "Impares: tiroides, cricoides, epiglotis"]),
  ("Pregunta de anatomía", ["Epiglotis, tiroides y ¿cuál más?"]),
  {"rotulo": "¿Par o impar?", "ans": 0, "cards": [
      {"titulo": "CRICOIDES", "datos": [
          ("Tipo", "Impar", True), ("Forma", "Anillo completo", True),
          ("Nivel", "C6", True)],
       "pie": "Parte más estrecha en niños"},
      {"titulo": "Aritenoides", "datos": [
          ("Tipo", "Par", False), ("Función", "Cuerdas vocales", False),
          ("Movimiento", "Giran", False)],
       "pie": "Abren y cierran la glotis"},
      {"titulo": "Corniculado", "datos": [
          ("Tipo", "Par", False), ("Otro nombre", "Santorini", False),
          ("Sitio", "Sobre aritenoides", False)],
       "pie": "Pequeño"},
      {"titulo": "Cuneiforme", "datos": [
          ("Tipo", "Par", False), ("Otro nombre", "Wrisberg", False),
          ("Sitio", "Pliegue ariepiglótico", False)],
       "pie": "Pequeño"}]},
  ["Cricotirotomía: membrana cricotiroidea.",
   "Tiroides: nuez de Adán.",
   "Epiglotis: cartílago elástico."],
  MOORE)

# CB-310 · matriz
V("matriz", "CB-310", "lingula-lobulo-superior-izquierdo-silueta-cardiaca", "Lóbulos pulmonares",
  "CIENCIAS BÁSICAS ENAM: PULMONES", CB,
  ("Lóbulos pulmonares", ["Derecho: tres lóbulos · Izquierdo: dos",
   "La língula equivale al lóbulo medio"]),
  ("Paciente con tumoración en la língula", ["¿En qué lóbulo está la lesión?"]),
  {"rotulo": "Lóbulos por pulmón", "eje_x": "Pulmón", "eje_y": "Región",
   "cols": ["Derecho", "Izquierdo"], "rows": ["Superior", "Media", "Inferior"], "caso": (1, 1),
   "cells": [[("Lóbulo superior", []), ("Lóbulo superior", [])],
             [("Lóbulo medio", ["Borra borde der."]), ("LÍNGULA", ["Del lóbulo superior"])],
             [("Lóbulo inferior", []), ("Lóbulo inferior", [])]]},
  ["Signo de la silueta: borra el corazón.",
   "Izquierdo: solo cisura oblicua.",
   "Derecho: oblicua y horizontal."],
  MOORE)

# CB-311 · radial
V("radial", "CB-311", "plexo-cardiaco-vago-simpatico-cervical", "Plexo cardíaco",
  "CIENCIAS BÁSICAS ENAM: INERVACIÓN DEL CORAZÓN", CB,
  ("Plexo cardíaco", ["Mezcla fibras vagales y simpáticas",
   "Está en la base del corazón"]),
  ("Pregunta de anatomía", ["¿De dónde se origina el plexo cardíaco?"]),
  {"rotulo": "Mapa del tema", "centro": "PLEXO", "centro_sub": "Cardíaco", "ans": 0,
   "items": [("VAGO + SIMPÁTICO", ["Ramas cervicales", "del vago y tronco"]),
             ("Vago", ["Baja FC", "y conducción AV"]),
             ("Simpático", ["Ganglios cervicales", "Sube FC y fuerza"]),
             ("Dolor", ["Entra por T1-T4"]),
             ("Ubicación", ["Cayado y carina"])],
   "ruta": ["Ganglios cervicales", "Nervios cardíacos", "Vago", "PLEXO CARDÍACO"]},
  ["Dolor referido al brazo izquierdo.",
   "Ganglio estrellado: cervical inferior.",
   "T12 no participa."],
  MOORE)

# CB-312 · matriz
V("matriz", "CB-312", "circulacion-bronquial-venas-bronquiales-drenaje-parcial", "Doble circulación pulmonar",
  "CIENCIAS BÁSICAS ENAM: CIRCULACIÓN PULMONAR", CB,
  ("Circulación del pulmón", ["Pulmonar: intercambio gaseoso",
   "Bronquial: nutre los bronquios"]),
  ("Pregunta de anatomía", ["¿Qué afirmación es correcta?"]),
  {"rotulo": "Comparación", "eje_x": "Circulación", "eje_y": "Rasgo",
   "cols": ["Pulmonar", "Bronquial"], "rows": ["Origen", "Contenido", "Drenaje"], "caso": (2, 1),
   "cells": [[("Ventrículo derecho", []), ("Aorta", [])],
             [("Arteria: venosa", ["Vena: oxigenada"]), ("Oxigenada", [])],
             [("Aurícula izquierda", []), ("SOLO EN PARTE", ["Ácigos, hemiácigos", "Resto: v. pulmonares"])]]},
  ["Cortocircuito fisiológico del 2 %.",
   "Bronquial derecha: ácigos.",
   "Bronquial izquierda: hemiácigos accesoria."],
  MOORE)

# CB-313 · árbol
A("CB-313", "arteria-pulmonar-derecha-posterior-aorta-ascendente", "Relaciones de las arterias pulmonares",
  "CIENCIAS BÁSICAS ENAM: HILIOS PULMONARES", CB,
  ("Arterias pulmonares", ["El tronco se divide bajo el cayado",
   "La derecha es más larga y horizontal"]),
  ("Pregunta de anatomía", ["¿Dónde está la arteria pulmonar derecha?"]),
  Q("¿Qué arteria pulmonar?", [
      L("Derecha", "TRAS AORTA ASCENDENTE", ["Y tras la cava superior", "Delante del bronquio"], path=True),
      L("Izquierda", "Sobre el bronquio", ["Principal izquierdo"])], path=True),
  ("Hilio pulmonar", [("Lado", True), ("Arteria", False)], [
      ("Derecho", ["Delante del bronquio", "Bronquio intermedio"]),
      ("Izquierdo", ["Encima del bronquio", "Cayado encima"])]),
  ["Útil en tomografía y cirugía.",
   "Ligamento arterioso a la izquierda.",
   "Tronco pulmonar: del ventrículo derecho."],
  MOORE)

# CB-314 · matriz
V("matriz", "CB-314", "coronaria-derecha-nodo-sinusal-av-infarto-inferior", "Territorios coronarios",
  "CIENCIAS BÁSICAS ENAM: CORONARIAS", CB,
  ("Arterias coronarias", ["Derecha: nodos en la mayoría",
   "Descendente anterior: haz de His y ramas"]),
  ("Pregunta de anatomía", ["¿Qué arteria irriga los nodos sinusal y AV?"]),
  {"rotulo": "Arteria y territorio", "eje_x": "Dato", "eje_y": "Arteria",
   "cols": ["Irriga", "Si se ocluye"], "rows": ["Coronaria derecha", "Descendente ant.", "Circunfleja"], "caso": (0, 0),
   "cells": [[("NODOS SA Y AV", ["Cara inferior"]), ("Bradicardia", ["Bloqueo nodal"])],
             [("Cara anterior", ["His y ramas"]), ("Bloqueo infranodal", [])],
             [("Cara lateral", []), ("Infarto lateral", [])]]},
  ["Dominancia: quién da la descendente posterior.",
   "Bloqueo nodal: responde a atropina.",
   "Infranodal: marcapasos."],
  HARRISON)

# CB-315 · tarjetas
V("tarjetas", "CB-315", "cuerdas-vocales-laringeo-recurrente-cricoaritenoideo-posterior", "Inervación de la laringe",
  "CIENCIAS BÁSICAS ENAM: LARINGE", CB,
  ("Inervación laríngea", ["Ramas del vago",
   "El recurrente mueve las cuerdas vocales"]),
  ("Pregunta de anatomía", ["¿Qué nervio inerva las cuerdas vocales?"]),
  {"rotulo": "¿Qué nervio?", "ans": 0, "cards": [
      {"titulo": "RECURRENTE", "datos": [
          ("Motor", "Intrínsecos", True), ("Clave", "Abre la glotis", True),
          ("Sensibilidad", "Bajo cuerdas", True)],
       "pie": "Cricoaritenoideo posterior"},
      {"titulo": "Laríngeo sup. ext.", "datos": [
          ("Motor", "Cricotiroideo", False), ("Función", "Tensa cuerdas", False),
          ("Lesión", "Tonos agudos", False)],
       "pie": "Rama externa"},
      {"titulo": "Laríngeo sup. int.", "datos": [
          ("Tipo", "Sensitivo", False), ("Zona", "Sobre cuerdas", False),
          ("Reflejo", "Tusígeno", False)],
       "pie": "Rama interna"},
      {"titulo": "Hipogloso", "datos": [
          ("Motor", "Lengua", False), ("Laringe", "No", False),
          ("Lesión", "Desvía lengua", False)],
       "pie": "XII par"}]},
  ["Aneurisma o cáncer apical: disfonía.",
   "Estenosis mitral: síndrome de Ortner.",
   "Recurrente izquierdo más largo."],
  MOORE)

# CB-316 · embudo
V("embudo", "CB-316", "mediastino-posterior-aorta-descendente-contenido", "Contenido del mediastino",
  "CIENCIAS BÁSICAS ENAM: MEDIASTINO", CB,
  ("Mediastino posterior", ["Detrás del pericardio",
   "Aorta, esófago, vagos, conducto torácico"]),
  ("Pregunta de anatomía", ["¿Qué estructura está en el mediastino posterior?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Estructuras del tórax",
   "candidatos": ["Aorta descendente", "Timo", "Nervio frénico", "Tráquea"],
   "pasos": [("No está delante ni en medio", ["Timo", "Nervio frénico"]),
             ("No está en el superior", ["Tráquea"])],
   "final": ("AORTA DESCENDENTE", ["Mediastino posterior", "Con esófago y ácigos"]),
   "nota": "Mamaria interna: pared anterior."},
  ["Masas posteriores: neurogénicas.",
   "Masas anteriores: timoma, teratoma, tiroides, linfoma.",
   "Frénico: sobre el pericardio."],
  MOORE)

# CB-317 · termómetro
V("termometro", "CB-317", "colon-ascendente-mesenterica-superior-ileocolica", "Irrigación del colon",
  "CIENCIAS BÁSICAS ENAM: IRRIGACIÓN DEL COLON", CB,
  ("Irrigación del colon", ["Mesentérica superior: colon derecho",
   "Mesentérica inferior: colon izquierdo"]),
  ("Pregunta de anatomía", ["¿Qué arteria irriga el colon ascendente?"]),
  {"rotulo": "Segmentos del colon",
   "niveles": [("Ascendente", "Mes. superior", ["ILEOCÓLICA, CÓLICA DER."]),
               ("Transverso", "Mes. superior", ["Cólica media (2/3)"]),
               ("Descendente", "Mes. inferior", ["Cólica izquierda"]),
               ("Sigmoides", "Mes. inferior", ["Sigmoideas"])],
   "caso_nivel": 0, "ruta_titulo": "Zonas de riesgo", "paso_label": "PASO",
   "pasos": [(1, "Arcada de Drummond", ["Une ambos territorios"], False),
             (2, "Ángulo esplénico", ["Punto de Griffiths"], False),
             (3, "Colon derecho", ["Mesentérica superior"], True)]},
  ["Colitis isquémica: ángulo esplénico.",
   "Hemorroidal superior: mesentérica inferior.",
   "Intestino medio: mesentérica superior."],
  MOORE)

# CB-318 · radial
V("radial", "CB-318", "ligamento-inguinal-poupart-aponeurosis-oblicuo-mayor", "Región inguinal",
  "CIENCIAS BÁSICAS ENAM: CONDUCTO INGUINAL", CB,
  ("Ligamento inguinal (Poupart)", ["Borde inferior de la aponeurosis",
   "del oblicuo mayor (externo)"]),
  ("Pregunta de anatomía", ["¿De qué músculo procede?"]),
  {"rotulo": "Mapa del tema", "centro": "INGUINAL", "centro_sub": "Ligamento", "ans": 0,
   "items": [("OBLICUO MAYOR", ["Aponeurosis", "Borde replegado"]),
             ("Inserciones", ["Espina ilíaca AS", "Tubérculo púbico"]),
             ("Debajo pasa", ["Nervio, arteria", "vena femorales"]),
             ("Gimbernat", ["Ligamento lacunar"]),
             ("Hernias", ["Inguinal arriba", "Femoral abajo"])],
   "ruta": ["Oblicuo mayor", "Aponeurosis", "Borde inferior", "POUPART"]},
  ["Piso del conducto inguinal.",
   "Hernia femoral: más en mujeres.",
   "Femoral: más riesgo de estrangulación."],
  MOORE)

# CB-319 · embudo
V("embudo", "CB-319", "triada-portal-vena-porta-arteria-hepatica-conducto-biliar", "Tríada portal",
  "CIENCIAS BÁSICAS ENAM: HÍGADO", CB,
  ("Espacio porta", ["En los vértices del lobulillo",
   "Tres estructuras juntas"]),
  ("Pregunta de histología", ["La tríada portal: vena porta y ¿qué más?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Estructuras hepáticas",
   "candidatos": ["Arteria y conducto biliar", "Vena hepática", "Epiplón mayor", "Mesentérica sup."],
   "pasos": [("Está en el espacio porta", ["Vena hepática", "Epiplón mayor"]),
             ("Es propia del hígado", ["Mesentérica sup."])],
   "final": ("ARTERIA HEPÁTICA Y CONDUCTO", ["Con la vena porta", "Bilis va hacia el espacio porta"]),
   "nota": "Vena hepática: sale de la vena central."},
  ["Porta: 75 % del flujo.",
   "Arteria: 25 %, rica en oxígeno.",
   "Maniobra de Pringle."],
  ROSS)

# CB-320 · radial
V("radial", "CB-320", "cabeza-pancreas-marco-duodenal-courvoisier", "Partes del páncreas",
  "CIENCIAS BÁSICAS ENAM: PÁNCREAS", CB,
  ("Anatomía del páncreas", ["Cabeza, cuello, cuerpo y cola",
   "La cabeza está dentro del marco duodenal"]),
  ("Pregunta de anatomía", ["¿Qué parte está en la C del duodeno?"]),
  {"rotulo": "Mapa del tema", "centro": "PÁNCREAS", "centro_sub": "Partes", "ans": 0,
   "items": [("CABEZA", ["En la C duodenal", "Colédoco dentro"]),
             ("Unciforme", ["Tras la mesentérica", "superior"]),
             ("Cuello", ["Sobre la porta"]),
             ("Cuerpo", ["Delante de aorta, L1"]),
             ("Cola", ["Hilio esplénico"])],
   "ruta": ["Duodeno en C", "Concavidad", "Colédoco", "CABEZA"]},
  ["Cáncer de cabeza: ictericia indolora.",
   "Courvoisier-Terrier: vesícula palpable.",
   "Páncreas anular: obstruye duodeno."],
  MOORE)

# CB-321 · fases
V("fases", "CB-321", "arteria-apendicular-ileocolica-mesenterica-superior", "Irrigación del apéndice",
  "CIENCIAS BÁSICAS ENAM: APÉNDICE", CB,
  ("Arteria apendicular", ["Terminal, sin colaterales",
   "Rama de la ileocólica"]),
  ("Pregunta de anatomía", ["¿De qué arteria viene la apendicular?"]),
  {"rotulo": "Origen de la arteria", "ans": 0,
   "fases": [("Aorta", "Tronco", "MESENTÉRICA SUP.", ["Intestino medio"]),
             ("Rama", "Colon derecho", "Ileocólica", ["Ciego e íleon"]),
             ("Terminal", "Mesoapéndice", "Apendicular", ["Sin colaterales"])],
   "chips_titulo": "Arteria madre · marcada",
   "chips": [("Mesentérica superior", True), ("Rectal superior", False), ("Cólica izquierda", False), ("Sigmoidea", False)]},
  ["Arteria terminal: gangrena rápida.",
   "Perforación tras 24-36 horas.",
   "Seguir las tenias hasta la base."],
  MOORE)

# CB-322 · termómetro
V("termometro", "CB-322", "sosten-utero-ligamentos-cardinales-uterosacros-delancey", "Niveles de sostén del útero",
  "CIENCIAS BÁSICAS ENAM: PISO PÉLVICO", CB,
  ("Sostén pélvico (DeLancey)", ["Nivel I: cardinales y uterosacros",
   "Sostienen el útero y la cúpula"]),
  ("Pregunta de anatomía", ["¿Cuál es el principal sostén del útero?"]),
  {"rotulo": "Estructuras de sostén",
   "niveles": [("Poco sostén", "Ancho y redondo", ["Peritoneo, anteversión"]),
               ("Nivel III", "Periné", ["Tercio inferior vagina"]),
               ("Nivel II", "Paracolpos", ["Vagina media"]),
               ("Nivel I", "CARDINALES", ["Y UTEROSACROS"])],
   "caso_nivel": 3, "ruta_titulo": "Si se debilitan", "paso_label": "PASO",
   "pasos": [(1, "Partos, menopausia", ["Daño del soporte"], False),
             (2, "Descenso uterino", ["Prolapso"], True),
             (3, "Elevador del ano", ["Ayuda al sostén"], False)]},
  ["Cardinales = Mackenrodt.",
   "Uterosacros van al sacro.",
   "Redondo: mantiene anteversión."],
  MOORE)

# CB-323 · tarjetas
V("tarjetas", "CB-323", "elevador-ano-pubococcigeo-puborrectal-iliococcigeo", "Músculos del piso pélvico",
  "CIENCIAS BÁSICAS ENAM: DIAFRAGMA PÉLVICO", CB,
  ("Diafragma pélvico", ["Elevador del ano y coccígeo",
   "Elevador: tres porciones"]),
  ("Pregunta de anatomía", ["¿Qué músculo forma parte del elevador?"]),
  {"rotulo": "¿Es elevador del ano?", "ans": 0, "cards": [
      {"titulo": "PUBOCOCCÍGEO", "datos": [
          ("Grupo", "Elevador del ano", True), ("Función", "Sostén", True),
          ("Ejercicio", "Kegel", True)],
       "pie": "Con puborrectal e iliococcígeo"},
      {"titulo": "Piramidal", "datos": [
          ("Grupo", "Pared abdominal", False), ("Sitio", "Sobre el pubis", False),
          ("Función", "Tensa línea alba", False)],
       "pie": "No es pélvico"},
      {"titulo": "Transverso prof.", "datos": [
          ("Grupo", "Periné profundo", False), ("Contiene", "Cowper", False),
          ("Función", "Sostén perineal", False)],
       "pie": "Diafragma urogenital"},
      {"titulo": "Bulboesponjoso", "datos": [
          ("Grupo", "Periné superficial", False), ("Función", "Eyaculación", False),
          ("Otro", "Isquiocavernoso", False)],
       "pie": "Espacio superficial"}]},
  ["Puborrectal: ángulo anorrectal.",
   "Clave para la continencia fecal.",
   "Inervación: S3-S4 y pudendo."],
  MOORE)

# CB-324 · fases
V("fases", "CB-324", "arteria-pedia-continuacion-tibial-anterior", "Arterias de la pierna al pie",
  "CIENCIAS BÁSICAS ENAM: ARTERIAS DEL MIEMBRO INFERIOR", CB,
  ("Arterias de la pierna", ["La poplítea da la tibial anterior",
   "Esta continúa como pedia"]),
  ("Pregunta de anatomía", ["¿De qué arteria es rama la dorsal del pie?"]),
  {"rotulo": "Recorrido arterial", "ans": 1,
   "fases": [("Rodilla", "Poplítea", "Poplítea", ["Se divide"]),
             ("Pierna", "Anterior", "TIBIAL ANTERIOR", ["Cruza la membrana", "Compartimento anterior"]),
             ("Tobillo", "Dorso", "Pedia", ["Dorsal del pie"])],
   "chips_titulo": "Origen · marcado el correcto",
   "chips": [("Tibial anterior", True), ("Tibial posterior", False), ("Peronea", False), ("Poplítea", False)]},
  ["Pulso pedio: entre extensores.",
   "Falta en 10 % por variante.",
   "Palpar junto con tibial posterior."],
  MOORE)

# CB-325 · embudo
V("embudo", "CB-325", "canal-del-pulso-supinador-largo-palmar-mayor", "Canal del pulso",
  "CIENCIAS BÁSICAS ENAM: ANTEBRAZO", CB,
  ("Canal del pulso", ["Cara anterior y distal del antebrazo",
   "Contiene la arteria radial"]),
  ("Pregunta de anatomía", ["¿Qué músculos lo forman?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Pares de músculos",
   "candidatos": ["Supinador y palmar mayor", "Supinador y palmar menor", "Palmares mayor y menor", "Abductor y extensor"],
   "pasos": [("Lateral: supinador largo", ["Palmares mayor y menor", "Abductor y extensor"]),
             ("Medial: palmar mayor", ["Supinador y palmar menor"])],
   "final": ("SUPINADOR LARGO Y PALMAR MAYOR", ["Braquiorradial y flexor radial", "Arteria radial en su fondo"]),
   "nota": "Palmar menor: más medial, falta en 15 %."},
  ["Prueba de Allen antes de puncionar.",
   "Gasometría y línea arterial.",
   "Fondo: pronador cuadrado."],
  MOORE)

# CB-326 · matriz
V("matriz", "CB-326", "hombro-cinco-articulaciones-escapulotoracica-funcional", "Complejo articular del hombro",
  "CIENCIAS BÁSICAS ENAM: HOMBRO", CB,
  ("Complejo del hombro", ["Tres articulaciones anatómicas",
   "Dos funcionales, sin cartílago articular"]),
  ("Pregunta de anatomía", ["¿Cuál es la quinta articulación?"]),
  {"rotulo": "Tipo de articulación", "eje_x": "Tipo", "eje_y": "Grupo",
   "cols": ["Anatómicas", "Funcionales"], "rows": ["Ejemplo 1", "Ejemplo 2", "Ejemplo 3"], "caso": (1, 1),
   "cells": [[("Glenohumeral", []), ("Subacromial", ["Espacio subdeltoideo"])],
             [("Acromioclavicular", []), ("ESCAPULOTORÁCICA", ["Quinta del caso"])],
             [("Esternoclavicular", []), ("—", [])]]},
  ["Ritmo escapulohumeral 2:1.",
   "Pinzamiento subacromial.",
   "Manguito rotador: no es articulación."],
  "Kapandji. Fisiología articular 6.ª ed. (2012)")

# CB-327 · termómetro
V("termometro", "CB-327", "rodilla-mayor-articulacion-sinovial-bursa", "Tamaño de las articulaciones sinoviales",
  "CIENCIAS BÁSICAS ENAM: RODILLA", CB,
  ("Rodilla", ["La articulación sinovial más grande",
   "Tres compartimentos"]),
  ("Pregunta de anatomía", ["¿Cuál es la sinovial más grande?"]),
  {"rotulo": "De menor a mayor",
   "niveles": [("Tobillo", "Mediana", ["Tibioastragalina"]),
               ("Codo", "Mediana", ["Tres articulaciones"]),
               ("Hombro, cadera", "Grande", ["Esféricas"]),
               ("Rodilla", "LA MAYOR", ["Tres compartimentos"])],
   "caso_nivel": 3, "ruta_titulo": "Por qué se lesiona", "paso_label": "PASO",
   "pasos": [(1, "Poca forma ósea", ["Estable por ligamentos"], True),
             (2, "Meniscos y cruzados", ["Deporte"], False),
             (3, "Bursa suprarrotuliana", ["Derrames"], False)]},
  ["Artrocentesis más frecuente.",
   "Tríada de O'Donoghue.",
   "Femorotibial y femororrotuliana."],
  MOORE)

# CB-328 · matriz
V("matriz", "CB-328", "gastrocnemio-biarticular-flexion-rodilla-plantar", "Músculos de la pantorrilla",
  "CIENCIAS BÁSICAS ENAM: MIEMBRO INFERIOR", CB,
  ("Músculos posteriores", ["Biarticulares cruzan dos articulaciones",
   "El gastrocnemio cruza rodilla y tobillo"]),
  ("Pregunta de anatomía", ["¿Qué músculo flexiona rodilla y tobillo?"]),
  {"rotulo": "Acción por articulación", "eje_x": "Articulación", "eje_y": "Músculo",
   "cols": ["Rodilla", "Tobillo"], "rows": ["Gastrocnemio", "Sóleo", "Semitendinoso"], "caso": (0, 0),
   "cells": [[("FLEXIONA", ["Nace en el fémur"]), ("Flexión plantar", ["Tendón de Aquiles"])],
             [("No actúa", ["Nace bajo la rodilla"]), ("Flexión plantar", ["Bomba venosa"])],
             [("Flexiona", []), ("No actúa", [])]]},
  ["Sóleo: se explora con rodilla flexionada.",
   "Isquiotibiales: extienden la cadera.",
   "Tríceps sural: gemelos + sóleo."],
  MOORE)

# CB-329 · embudo
V("embudo", "CB-329", "coxofemoral-articulacion-sinovial-diartrosis", "¿Qué articulación es sinovial?",
  "CIENCIAS BÁSICAS ENAM: ARTICULACIONES SINOVIALES", CB,
  ("Articulación sinovial", ["Cápsula, membrana y líquido sinovial",
   "Cartílago articular hialino"]),
  ("Pregunta de anatomía", ["¿Cuál es sinovial?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Cinco uniones",
   "candidatos": ["Coxofemoral", "Sínfisis del pubis", "Sutura sagital", "Disco intervertebral"],
   "pasos": [("No es fibrosa", ["Sutura sagital"]),
             ("No es cartilaginosa", ["Sínfisis del pubis", "Disco intervertebral"])],
   "final": ("COXOFEMORAL", ["Enartrosis sinovial", "Rodete acetabular"]),
   "nota": "Facetarias, acromioclavicular: también sinoviales."},
  ["Ligamento redondo con arteria.",
   "Gonfosis: fibrosa.",
   "Artritis reumatoide: ataca la sinovial."],
  MOORE)

# CB-330 · termómetro
V("termometro", "CB-330", "metabolismo-basal-ayuno-12-horas-calorimetria", "Condiciones del metabolismo basal",
  "CIENCIAS BÁSICAS ENAM: METABOLISMO BASAL", CB,
  ("Metabolismo basal", ["Gasto mínimo en reposo",
   "Se mide sin efecto térmico de los alimentos"]),
  ("Pregunta de fisiología", ["¿Tras cuántas horas de ayuno se mide?"]),
  {"rotulo": "Horas de ayuno",
   "niveles": [("4 horas", "Insuficiente", ["Digestión en curso"]),
               ("8 horas", "Insuficiente", ["Efecto térmico"]),
               ("12 horas", "CORRECTO", ["Ayuno estándar"]),
               ("24 horas", "Excesivo", ["Cambia metabolismo"])],
   "caso_nivel": 2, "ruta_titulo": "Otras condiciones", "paso_label": "PASO",
   "pasos": [(1, "Despierto y en reposo", ["Acostado"], False),
             (2, "Temperatura neutra", ["Ambiente cómodo"], False),
             (3, "Ayuno de 12 horas", ["Sin ejercicio previo"], True)]},
  ["Calorimetría indirecta.",
   "Harris-Benedict lo estima.",
   "Hipertiroidismo y fiebre lo elevan."],
  GUYTON)

# CB-331 · árbol
A("CB-331", "fructosa-glut5-difusion-facilitada-enterocito", "Absorción de los monosacáridos",
  "CIENCIAS BÁSICAS ENAM: ABSORCIÓN DE AZÚCARES", CB,
  ("Absorción de monosacáridos", ["Glucosa y galactosa: con sodio",
   "Fructosa: sin sodio ni energía"]),
  ("Pregunta de fisiología", ["¿Cómo se absorbe la fructosa?"]),
  Q("¿Qué monosacárido?", [
      L("Fructosa", "DIFUSIÓN FACILITADA", ["GLUT5 apical", "Sale por GLUT2"], path=True),
      L("Glucosa, galactosa", "Activo secundario", ["SGLT1 con sodio"])], path=True),
  ("Exceso de fructosa", [("Situación", True), ("Efecto", False)], [
      ("Jugos, gaseosas", ["Mucha fructosa", "No se absorbe toda"]),
      ("En el colon", ["Fermenta", "Diarrea y gases"])]),
  ["Mejor absorción si va con glucosa.",
   "No gasta ATP.",
   "Intolerancia hereditaria: aldolasa B."],
  GUYTON)

# CB-332 · puntaje
V("puntaje", "CB-332", "metabolismo-basal-60-por-ciento-gasto-energetico", "Componentes del gasto energético",
  "CIENCIAS BÁSICAS ENAM: GASTO ENERGÉTICO", CB,
  ("Gasto energético total", ["Basal + efecto térmico + actividad",
   "El basal es el mayor componente"]),
  ("Pregunta de fisiología", ["¿Qué porcentaje es el metabolismo basal?"]),
  {"rotulo": "Reparto del gasto", "escala": "%", "total": 60, "max": 100,
   "total_label": "Metabolismo basal",
   "interpreta": "≈ 60 % del total",
   "items": [("Basal", "60 %", True), ("Actividad física", "20-30 %", False),
             ("Efecto térmico", "10 %", False)],
   "bandas": [("≈ 10 %", "Térmico", "Digerir alimentos", False),
              ("20-30 %", "Actividad", "Muy variable", False),
              ("60-70 %", "Basal", "Órganos vitales", True)]},
  ["La masa magra lo determina.",
   "Varones y jóvenes gastan más.",
   "Base del cálculo calórico."],
  GUYTON)
