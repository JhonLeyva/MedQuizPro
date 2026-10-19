"""Ciencias Básicas · parte E (CB-253 a CB-292)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-253 · matriz
V("matriz", "CB-253", "esofago-epitelio-plano-estratificado-no-queratinizado", "Epitelio del tubo digestivo",
  "CIENCIAS BÁSICAS ENAM: EPITELIO DIGESTIVO", CB,
  ("Epitelio digestivo", ["Esófago: escamoso para resistir fricción",
   "Estómago a colon: cilíndrico simple"]),
  ("Pregunta de histología", ["¿Qué órgano tiene epitelio estratificado", "no queratinizado?"]),
  {"rotulo": "Epitelio por órgano", "eje_x": "Rasgo", "eje_y": "Órgano",
   "cols": ["Epitelio", "Función"], "rows": ["Esófago", "Estómago", "Íleon y colon"], "caso": (0, 0),
   "cells": [[("PLANO ESTRATIFICADO", ["No queratinizado"]), ("Resistir fricción", [])],
             [("Cilíndrico simple", ["Mucosecretor"]), ("Secretar", [])],
             [("Cilíndrico simple", ["Microvellosidades"]), ("Absorber", [])]]},
  ["Línea Z: cambio brusco de epitelio.",
   "Barrett: metaplasia intestinal.",
   "Carcinoma epidermoide: epitelio escamoso."],
  ROSS)

# CB-254 · radial
V("radial", "CB-254", "haz-de-his-unica-via-auriculoventricular", "Sistema de conducción",
  "CIENCIAS BÁSICAS ENAM: CONDUCCIÓN CARDÍACA", CB,
  ("Sistema de conducción", ["El esqueleto fibroso aísla aurículas y ventrículos",
   "Solo el haz de His los conecta"]),
  ("Pregunta de fisiología", ["¿Por dónde pasa el impulso a los ventrículos?"]),
  {"rotulo": "Mapa del tema", "centro": "CONDUCCIÓN", "centro_sub": "Cardíaca", "ans": 0,
   "items": [("HAZ DE HIS", ["Única vía normal", "A los ventrículos"]),
             ("Bachmann", ["A la aurícula izq."]),
             ("Internodales", ["Wenckebach, Thorel"]),
             ("Purkinje", ["Red ventricular"]),
             ("Haz de Kent", ["Vía accesoria: WPW"])],
   "ruta": ["Nodo sinusal", "Nodo AV", "HAZ DE HIS", "Ramas y Purkinje"]},
  ["WPW: PR corto y onda delta.",
   "His se divide en rama derecha e izquierda.",
   "Bloqueo infranodal: QRS ancho."],
  GUYTON)

# CB-255 · matriz
V("matriz", "CB-255", "rodilla-diartrosis-sinovial-bicondilea", "Clasificación de las articulaciones",
  "CIENCIAS BÁSICAS ENAM: ARTICULACIONES", CB,
  ("Articulaciones por su movilidad", ["Sinartrosis, anfiartrosis y diartrosis",
   "Las diartrosis tienen cavidad sinovial"]),
  ("Pregunta de anatomía", ["¿Qué tipo de articulación es la rodilla?"]),
  {"rotulo": "Movilidad y ejemplos", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Movilidad", "Ejemplo"], "rows": ["Sinartrosis", "Anfiartrosis", "Diartrosis"], "caso": (2, 1),
   "cells": [[("Inmóvil", []), ("Suturas del cráneo", [])],
             [("Poco móvil", []), ("Sínfisis, discos", [])],
             [("Móvil", ["Sinovial"]), ("RODILLA", ["Bicondílea"])]]},
  ["Rodilla: la sinovial más grande.",
   "Estabilidad: ligamentos y meniscos.",
   "Tríada de O'Donoghue en deportistas."],
  MOORE)

# CB-256 · termómetro
V("termometro", "CB-256", "tetraciclinas-diarrea-efecto-mas-frecuente", "Efectos adversos de las tetraciclinas",
  "CIENCIAS BÁSICAS ENAM: TETRACICLINAS", CB,
  ("Tetraciclinas", ["Bacteriostáticas, subunidad 30S",
   "Lo más frecuente es gastrointestinal"]),
  ("Pregunta de farmacología", ["¿Efecto adverso más frecuente?"]),
  {"rotulo": "Frecuencia",
   "niveles": [("Rara", "Hipertensión", ["Intracraneal benigna"]),
               ("Poco frecuente", "Hepatotoxicidad", ["Dosis altas, embarazo"]),
               ("Frecuente", "Fotosensibilidad", ["Piel expuesta"]),
               ("Muy frecuente", "DIARREA", ["Náuseas, epigastralgia"])],
   "caso_nivel": 3, "ruta_titulo": "Cómo tomarlas", "paso_label": "PASO",
   "pasos": [(1, "Con agua abundante", ["Evita úlcera esofágica"], True),
             (2, "Sin lácteos ni hierro", ["Reducen absorción"], False),
             (3, "Evitar < 8 años", ["Tiñen los dientes"], False)]},
  ["Tetraciclina caducada: síndrome de Fanconi.",
   "Se depositan en hueso y dientes.",
   "Doxiciclina: sin ajuste renal."],
  GOODMAN)

# CB-257 · árbol
A("CB-257", "shock-reanimacion-cristaloide-isotonico-suero-fisiologico", "Líquido inicial en el shock",
  "CIENCIAS BÁSICAS ENAM: REANIMACIÓN", CB,
  ("Reanimación del shock", ["Primero cristaloides isotónicos",
   "Bolos de 20-30 mL/kg con reevaluación"]),
  ("Pregunta de fisiología", ["¿Qué fluido se indica en el shock?"]),
  Q("¿Qué tipo de shock?", [
      L("Casi todos", "NaCl 0,9 %", ["O lactato de Ringer", "Bolos y reevaluar"], path=True),
      L("Hemorrágico", "Hemoderivados", ["Tras 1 L de cristaloide"])], path=True),
  ("Opciones que no se usan", [("Solución", True), ("Uso real", False)], [
      ("NaCl 3 %", ["Hipertónica", "Hiponatremia grave"]),
      ("NaCl 20 %", ["Concentrado", "Diluir siempre"])]),
  ["Coloides y albúmina: sin mejor sobrevida.",
   "Almidones dañan el riñón.",
   "Exceso de cristaloide: edema."],
  "Surviving Sepsis Campaign (2021) · " + ATLS)

# CB-258 · fases
V("fases", "CB-258", "diureticos-de-asa-rama-ascendente-gruesa-nkcc2", "Sitio de acción de los diuréticos",
  "CIENCIAS BÁSICAS ENAM: DIURÉTICOS", CB,
  ("Diuréticos por segmento", ["Cada grupo bloquea un transportador",
   "Los de asa: NKCC2 de la rama gruesa"]),
  ("Pregunta de farmacología", ["¿Dónde actúan los diuréticos de asa?"]),
  {"rotulo": "Recorrido de la nefrona", "ans": 1,
   "fases": [("Proximal", "Anhidrasa", "Acetazolamida", ["Bicarbonato"]),
             ("Asa de Henle", "NKCC2", "RAMA GRUESA", ["Furosemida", "25 % del sodio"]),
             ("Distal y colector", "NCC, ENaC", "Tiazidas", ["Espironolactona"])],
   "chips_titulo": "Segmento · marcado el correcto",
   "chips": [("Asa gruesa ascendente", True), ("Túbulo proximal", False), ("Túbulo distal", False), ("Colector", False)]},
  ["Pierden calcio y magnesio.",
   "Bartter imita a la furosemida.",
   "Gitelman imita a las tiazidas."],
  GOODMAN)

# CB-259 · tarjetas
V("tarjetas", "CB-259", "cromoglicato-sodico-estabilizador-mastocitos-asma", "Fármacos del asma",
  "CIENCIAS BÁSICAS ENAM: ANTIASMÁTICOS", CB,
  ("Fármacos del asma", ["Cada grupo actúa en un paso distinto",
   "El cromoglicato estabiliza al mastocito"]),
  ("Pregunta de farmacología", ["¿Qué fármaco estabiliza los mastocitos?"]),
  {"rotulo": "¿Cómo actúa?", "ans": 0, "cards": [
      {"titulo": "CROMOGLICATO", "datos": [
          ("Acción", "Estabiliza mastocito", True), ("Uso", "Preventivo", True),
          ("Crisis", "No sirve", True)],
       "pie": "También nedocromilo"},
      {"titulo": "Omalizumab", "datos": [
          ("Acción", "Anti-IgE", False), ("Uso", "Asma grave", False),
          ("Vía", "Subcutánea", False)],
       "pie": "Anticuerpo"},
      {"titulo": "Montelukast", "datos": [
          ("Acción", "Anti-CysLT1", False), ("Uso", "Asma por ejercicio", False),
          ("Vía", "Oral", False)],
       "pie": "Antileucotrieno"},
      {"titulo": "Ipratropio", "datos": [
          ("Acción", "Antimuscarínico", False), ("Uso", "EPOC, crisis", False),
          ("Vía", "Inhalada", False)],
       "pie": "Teofilina: fosfodiesterasa"}]},
  ["Pocos efectos adversos.",
   "Útil en rinitis y conjuntivitis alérgica.",
   "Ketotifeno: también estabiliza."],
  GOODMAN)

# CB-260 · matriz
V("matriz", "CB-260", "mujer-joven-miosis-fasciculaciones-carbamatos", "Carbamatos y organofosforados",
  "CIENCIAS BÁSICAS ENAM: INSECTICIDAS", CB,
  ("Inhibidores de la acetilcolinesterasa", ["Ambos dan síndrome colinérgico",
   "Difieren en la duración de la unión"]),
  ("Mujer joven", ["Sialorrea, náuseas, vómitos", "Miosis y fasciculaciones"]),
  {"rotulo": "Diferencias", "eje_x": "Grupo", "eje_y": "Rasgo",
   "cols": ["Carbamatos", "Organofosforados"], "rows": ["Unión", "Cuadro", "Pralidoxima"], "caso": (0, 0),
   "cells": [[("REVERSIBLE", ["Se recupera en horas"]), ("Irreversible", ["Envejece"])],
             [("Más corto", ["Poco SNC"]), ("Más largo", ["SNC marcado"])],
             [("Innecesaria", []), ("Útil precoz", [])]]},
  ["Aldicarb («Tres Pasitos»): carbamato.",
   "Ambos se tratan con atropina.",
   "Asma o edema pulmonar no dan miosis."],
  TOXI)

# CB-261 · tarjetas
V("tarjetas", "CB-261", "celulas-kupffer-macrofagos-sinusoides-hepaticos", "Células del hígado",
  "CIENCIAS BÁSICAS ENAM: HISTOLOGÍA HEPÁTICA", CB,
  ("Sinusoide hepático", ["Endotelio fenestrado sin membrana basal",
   "Con macrófagos y células estrelladas"]),
  ("Pregunta de histología", ["¿Cómo se llaman los macrófagos del sinusoide?"]),
  {"rotulo": "¿Qué célula?", "ans": 0, "cards": [
      {"titulo": "KUPFFER", "datos": [
          ("Tipo", "Macrófago", True), ("Sitio", "Sinusoide", True),
          ("Función", "Limpia la sangre", True)],
       "pie": "Mayor grupo de macrófagos fijos"},
      {"titulo": "Ito (estrellada)", "datos": [
          ("Sitio", "Espacio de Disse", False), ("Guarda", "Vitamina A", False),
          ("Activada", "Fibrosis", False)],
       "pie": "Cirrosis"},
      {"titulo": "Merkel", "datos": [
          ("Órgano", "Piel", False), ("Tipo", "Mecanorreceptor", False),
          ("Sitio", "Capa basal", False)],
       "pie": "Tacto"},
      {"titulo": "Paneth", "datos": [
          ("Órgano", "Intestino", False), ("Sitio", "Criptas", False),
          ("Secreta", "Defensinas", False)],
       "pie": "Lisozima"}]},
  ["Kupffer: bacterias y endotoxina portal.",
   "Ito: miofibroblastos en la fibrosis.",
   "Lieberkühn: criptas, no células."],
  ROSS)

# CB-262 · fases
V("fases", "CB-262", "aclimatacion-altura-3800-hiperventilacion-inmediata", "Aclimatación a la altura",
  "CIENCIAS BÁSICAS ENAM: FISIOLOGÍA DE LA ALTURA", CB,
  ("Aclimatación", ["Baja la PO2 inspirada",
   "Cambios en minutos, días y semanas"]),
  ("Mujer de 35 años de la costa", ["Sube a 3800 metros", "¿Qué aumenta de inmediato?"]),
  {"rotulo": "Tiempo de adaptación", "ans": 0,
   "fases": [("Inmediata", "Minutos", "VENTILACIÓN", ["Cuerpo carotídeo", "Alcalosis respiratoria"]),
             ("Días", "Riñón", "Bicarbonato", ["Compensa la alcalosis"]),
             ("Semanas", "Médula", "Eritrocitos", ["EPO, hematocrito"])],
   "chips_titulo": "Mecanismo inmediato · marcado",
   "chips": [("Ventilación", True), ("Eritrocitos", False), ("Difusión", False), ("Uso celular", False)]},
  ["2,3-DPG aumenta en días.",
   "Acetazolamida acelera la aclimatación.",
   "Mal de altura: cefalea, náuseas."],
  GUYTON)

# CB-263 · árbol
A("CB-263", "acetazolamida-mal-de-altura-anhidrasa-carbonica", "Prevención del mal de altura",
  "CIENCIAS BÁSICAS ENAM: MAL DE ALTURA", CB,
  ("Mal de montaña agudo", ["La alcalosis de la altura frena la ventilación",
   "La acetazolamida la contrarresta"]),
  ("Pregunta de farmacología", ["¿Mecanismo del diurético preventivo?"]),
  Q("¿Qué hace la acetazolamida?", [
      L("Riñón", "INHIBE ANHIDRASA", ["Pierde bicarbonato", "Acidosis metabólica leve"], path=True),
      L("Resultado", "Más ventilación", ["Acelera la aclimatación"])], path=True),
  ("Uso práctico", [("Dato", True), ("Valor", False)], [
      ("Dosis", ["Preventiva", "125 mg c/12 h"]),
      ("Inicio", ["Antes de subir", "1 día antes"])]),
  ["Efectos: parestesias, sabor metálico.",
   "Contraindicada en alergia grave a sulfas.",
   "Mejora la respiración periódica nocturna."],
  "Wilderness Medical Society – Altitude illness (2019)")

# CB-264 · árbol
A("CB-264", "glaucoma-angulo-cerrado-anticolinergicos-contraindicados", "Fármacos en el glaucoma",
  "CIENCIAS BÁSICAS ENAM: GLAUCOMA", CB,
  ("Glaucoma de ángulo cerrado", ["La midriasis cierra el ángulo iridocorneal",
   "El humor acuoso no drena"]),
  ("Mujer de 25 años con glaucoma", ["¿Qué grupo está contraindicado?"]),
  Q("¿El fármaco dilata la pupila?", [
      L("Sí", "ANTICOLINÉRGICOS", ["Atropina, hioscina", "Tricíclicos"], path=True),
      L("No", "Permitidos", ["Antibióticos, AINE"])], path=True),
  ("Crisis de ángulo cerrado", [("Signo", True), ("Tratamiento", False)], [
      ("Ojo rojo, halos", ["Dolor, vómitos", "Pilocarpina, timolol"]),
      ("Ojo duro", ["Pupila fija media", "Acetazolamida, manitol"])]),
  ["Definitivo: iridotomía con láser.",
   "Ángulo abierto: menor riesgo.",
   "Antihistamínicos de 1.ª generación también."],
  "American Academy of Ophthalmology – PACG (2020)")

# CB-265 · tarjetas
V("tarjetas", "CB-265", "ketoconazol-rifampicina-induccion-cyp3a4-fracaso", "Interacciones del ketoconazol",
  "CIENCIAS BÁSICAS ENAM: INTERACCIONES", CB,
  ("Ketoconazol", ["Se metaboliza por el CYP3A4",
   "Necesita medio ácido para absorberse"]),
  ("Mujer de 33 años con tiña inguinal", ["Ketoconazol sin mejoría a los 15 días", "¿Qué fármaco reduce su acción?"]),
  {"rotulo": "¿Qué interacción?", "ans": 0, "cards": [
      {"titulo": "RIFAMPICINA", "datos": [
          ("Efecto", "Inductor CYP3A4", True), ("Azol", "Niveles bajos", True),
          ("Resultado", "Fracaso", True)],
       "pie": "No combinar"},
      {"titulo": "Omeprazol", "datos": [
          ("Efecto", "Sube el pH", False), ("Azol", "Menos absorción", False),
          ("Resultado", "También reduce", False)],
       "pie": "Antiácidos igual"},
      {"titulo": "Amiodarona", "datos": [
          ("Efecto", "Sube por el azol", False), ("Riesgo", "QT largo", False),
          ("Sentido", "Inverso", False)],
       "pie": "Ketoconazol inhibe"},
      {"titulo": "Penicilina", "datos": [
          ("Efecto", "Ninguno", False), ("Azol", "Sin cambio", False),
          ("Resultado", "—", False)],
       "pie": "Sin interacción"}]},
  ["Ketoconazol oral: hepatotóxico.",
   "Inhibe CYP3A4: sube estatinas.",
   "Preferir terbinafina o azol tópico."],
  GOODMAN)

# CB-266 · fases
V("fases", "CB-266", "madre-rh-negativa-igg-anti-d-hemolisis-fetal", "Isoinmunización Rh",
  "CIENCIAS BÁSICAS ENAM: ENFERMEDAD HEMOLÍTICA", CB,
  ("Enfermedad hemolítica del recién nacido", ["Madre Rh negativa, feto Rh positivo",
   "Solo la IgG cruza la placenta"]),
  ("Pregunta de inmunología", ["¿Qué inmunoglobulina produce la hemólisis?"]),
  {"rotulo": "Secuencia", "ans": 2,
   "fases": [("1.er embarazo", "Parto", "Sensibilización", ["Primero IgM"]),
             ("Memoria", "Entre embarazos", "Células B", ["Cambio a IgG"]),
             ("2.º embarazo", "Placenta", "IgG ANTI-D", ["Cruza por FcRn", "Hemólisis fetal"])],
   "chips_titulo": "Inmunoglobulina · marcada la correcta",
   "chips": [("IgG", True), ("IgM", False), ("IgA", False), ("IgE", False)]},
  ["Anti-D a las 28 semanas y posparto.",
   "Hidropesía fetal en casos graves.",
   "La IgM no cruza la placenta."],
  "ACOG – Prevention of Rh D alloimmunization (2017)")

# CB-267 · árbol
A("CB-267", "piel-amarilla-escleras-blancas-carotenemia", "Piel amarilla sin ictericia",
  "CIENCIAS BÁSICAS ENAM: SEUDOICTERICIA", CB,
  ("Coloración amarilla de la piel", ["Ictericia: bilirrubina alta",
   "Carotenemia: carotenos altos"]),
  ("Mujer de 34 años asintomática", ["Piel amarilla, perfil hepático normal", "¿Qué sustancia aumenta?"]),
  Q("¿Escleras amarillas?", [
      L("No", "CAROTENO", ["Palmas y plantas", "Zanahoria, papaya"], path=True),
      L("Sí", "Bilirrubina", ["Ictericia verdadera"])], path=True),
  ("Diferencias", [("Carotenemia", True), ("Ictericia", False)], [
      ("Escleras", ["Blancas", "Amarillas"]),
      ("Bilirrubina", ["Normal", "Alta"])]),
  ["Asociada a hipotiroidismo y diabetes.",
   "Es benigna.",
   "La esclera tiene elastina que fija bilirrubina."],
  HARRISON)

# CB-268 · radial
V("radial", "CB-268", "deficit-zinc-acrodermatitis-alopecia-diarrea", "Déficit de zinc",
  "CIENCIAS BÁSICAS ENAM: OLIGOELEMENTOS", CB,
  ("Zinc", ["Cofactor de más de 300 enzimas",
   "Su déficit daña piel, pelo e intestino"]),
  ("Pregunta de nutrición", ["Dermatitis acral, alopecia y diarrea", "¿Qué falta?"]),
  {"rotulo": "Mapa del tema", "centro": "ZINC", "centro_sub": "Déficit", "ans": 0,
   "items": [("TRÍADA", ["Dermatitis acral", "Alopecia, diarrea"]),
             ("Hereditario", ["Acrodermatitis", "enteropática"]),
             ("Adquirido", ["Desnutrición, NPT"]),
             ("Otros", ["Mala cicatrización", "Infecciones"]),
             ("Tratamiento", ["Zinc oral"])],
   "ruta": ["Destete", "Menos absorción", "Lesiones periorificiales", "ZINC"]},
  ["Transportador ZIP4 defectuoso.",
   "Mejora rápida con zinc oral.",
   "Exceso de zinc: déficit de cobre."],
  NELSON)

# CB-269 · termómetro
V("termometro", "CB-269", "cancer-gastrico-precoz-mucosa-submucosa-t1", "Profundidad del cáncer gástrico",
  "CIENCIAS BÁSICAS ENAM: CÁNCER GÁSTRICO", CB,
  ("Cáncer gástrico precoz", ["Limitado a mucosa o submucosa (T1)",
   "Con o sin ganglios"]),
  ("Pregunta de patología", ["¿Hasta qué capa llega como máximo?"]),
  {"rotulo": "Capas de la pared",
   "niveles": [("Mucosa", "T1a", ["Precoz"]),
               ("Submucosa", "T1b", ["LÍMITE DEL PRECOZ"]),
               ("Muscular", "T2", ["Ya es avanzado"]),
               ("Serosa", "T3-T4", ["Avanzado"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo del precoz", "paso_label": "PASO",
   "pasos": [(1, "Endoscopía", ["Tamizaje en zonas de riesgo"], False),
             (2, "Resección endoscópica", ["Mucoso y diferenciado"], True),
             (3, "Sobrevida > 90 %", ["A 5 años"], False)]},
  ["Clasificación japonesa I, II, III.",
   "Tipo IIc: deprimido.",
   "Japón y Corea: tamizaje endoscópico."],
  "Japanese Gastric Cancer Treatment Guidelines (2021)")

# CB-270 · tarjetas
V("tarjetas", "CB-270", "hierro-absorcion-forma-ferrosa-no-ferrica", "Absorción de nutrientes",
  "CIENCIAS BÁSICAS ENAM: ABSORCIÓN INTESTINAL", CB,
  ("Absorción intestinal", ["Cada nutriente tiene su sitio y forma",
   "El hierro se absorbe como ferroso"]),
  ("Pregunta de fisiología", ["¿Qué afirmación es incorrecta?"]),
  {"rotulo": "¿Es correcto?", "ans": 0, "cards": [
      {"titulo": "HIERRO FÉRRICO", "datos": [
          ("Dice", "Se absorbe mejor", True), ("Realidad", "Mejor ferroso", True),
          ("Veredicto", "INCORRECTA", True)],
       "pie": "Fe2+ por DMT1"},
      {"titulo": "Hierro", "datos": [
          ("Sitio", "Duodeno", False), ("Ayuda", "Vitamina C", False),
          ("Veredicto", "Correcta", False)],
       "pie": "Fitatos inhiben"},
      {"titulo": "Agua", "datos": [
          ("Sitio", "Intestino delgado", False), ("Colon", "Menor parte", False),
          ("Veredicto", "Correcta", False)],
       "pie": "Mayor volumen"},
      {"titulo": "B12 y bilis", "datos": [
          ("Sitio", "Íleon", False), ("Páncreas", "Libera B12", False),
          ("Veredicto", "Correcta", False)],
       "pie": "Insuficiencia: déficit B12"}]},
  ["Sulfato ferroso en ayunas.",
   "Lejos de lácteos y té.",
   "Hepcidina frena la absorción."],
  GUYTON)

# CB-271 · radial
V("radial", "CB-271", "pelagra-niacina-dermatitis-diarrea-demencia", "Pelagra",
  "CIENCIAS BÁSICAS ENAM: VITAMINAS DEL GRUPO B", CB,
  ("Pelagra", ["Déficit de niacina (B3) o triptófano",
   "Las 3 D: dermatitis, diarrea, demencia"]),
  ("Pregunta de nutrición", ["¿Qué déficit produce pelagra?"]),
  {"rotulo": "Mapa del tema", "centro": "PELAGRA", "centro_sub": "Niacina", "ans": 0,
   "items": [("NIACINA (B3)", ["Déficit principal"]),
             ("Dermatitis", ["Zonas al sol", "Collar de Casal"]),
             ("Causas", ["Maíz, alcohol", "Isoniacida"]),
             ("Carcinoide", ["Consume triptófano"]),
             ("Hartnup", ["No absorbe triptófano"])],
   "ruta": ["Dieta de maíz", "Falta niacina", "3 D", "PELAGRA"]},
  ["Cuarta D: muerte.",
   "Tratamiento: nicotinamida.",
   "La B6 ayuda a sintetizar niacina."],
  HARPER)

# CB-272 · embudo
V("embudo", "CB-272", "mujer-soporosa-sialorrea-sibilantes-taquicardia-organofosforado", "Coma con secreciones",
  "CIENCIAS BÁSICAS ENAM: TOXICOLOGÍA", CB,
  ("Organofosforados", ["Muscarínico + nicotínico + central",
   "La taquicardia puede ser nicotínica"]),
  ("Mujer de 20 años inconsciente", ["Sialorrea, pupilas de 2 mm, fasciculaciones", "Sibilancias y taquicardia"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Mujer soporosa",
   "candidatos": ["Organofosforados", "Benzodiacepinas", "Crisis bronquial", "Estado postictal"],
   "pasos": [("Hay sialorrea y fasciculaciones", ["Benzodiacepinas", "Estado postictal"]),
             ("Hay miosis", ["Crisis bronquial"])],
   "final": ("ORGANOFOSFORADOS", ["Taquicardia no lo descarta", "Atropina + pralidoxima"]),
   "nota": "Hipoglucemia: no da secreciones ni miosis."},
  ["Taquicardia: ganglios simpáticos o hipoxia.",
   "Secar secreciones es la meta.",
   "Soporte ventilatorio si hace falta."],
  TOXI)

# CB-273 · fases
V("fases", "CB-273", "hmg-coa-reductasa-enzima-limitante-colesterol-estatinas", "Síntesis del colesterol",
  "CIENCIAS BÁSICAS ENAM: COLESTEROL", CB,
  ("Síntesis de colesterol", ["En el retículo endoplasmático del hígado",
   "Paso limitante: HMG-CoA reductasa"]),
  ("Pregunta de bioquímica", ["¿Cuál es la enzima limitante?"]),
  {"rotulo": "Pasos de la vía", "ans": 1,
   "fases": [("Inicio", "Acetil-CoA", "HMG-CoA", ["3 acetil-CoA"]),
             ("Paso limitante", "Reductasa", "MEVALONATO", ["HMG-CoA reductasa", "Estatinas"]),
             ("Final", "Escualeno", "Colesterol", ["Varios pasos"])],
   "chips_titulo": "Enzima · marcada la correcta",
   "chips": [("HMG-CoA reductasa", True), ("Lipoproteinlipasa", False), ("Elastasa", False), ("MAO", False)]},
  ["Insulina la activa; glucagón la inhibe.",
   "Estatinas: suben receptores de LDL.",
   "Síntesis mayor por la noche."],
  HARPER)

# CB-274 · matriz
V("matriz", "CB-274", "hbpm-control-anti-xa-no-ttpa-heparina", "Heparinas y su control",
  "CIENCIAS BÁSICAS ENAM: ANTICOAGULANTES", CB,
  ("Heparinas", ["Potencian la antitrombina",
   "Se controlan con pruebas distintas"]),
  ("Pregunta de farmacología", ["¿Qué afirmación es incorrecta?"]),
  {"rotulo": "Heparina y control", "eje_x": "Tipo", "eje_y": "Rasgo",
   "cols": ["No fraccionada", "Bajo peso"], "rows": ["Vía", "Control", "Trombocitopenia"], "caso": (1, 1),
   "cells": [[("IV", ["Infusión"]), ("Subcutánea", [])],
             [("TTPA", []), ("ANTI-Xa", ["No TTPA: opción falsa"])],
             [("Más riesgo", []), ("Menos riesgo", [])]]},
  ["Warfarina: INR.",
   "Proteínas C y S: anticoagulantes naturales.",
   "Anti-Xa en insuficiencia renal y embarazo."],
  GOODMAN)

# CB-275 · fases
V("fases", "CB-275", "fase-0-potencial-accion-ventricular-canales-sodio", "Potencial de acción ventricular",
  "CIENCIAS BÁSICAS ENAM: ELECTROFISIOLOGÍA", CB,
  ("Potencial de acción del ventrículo", ["Cinco fases (0 a 4)",
   "La fase 0 es la despolarización rápida"]),
  ("Pregunta de fisiología", ["¿Qué causa la fase 0?"]),
  {"rotulo": "Fases principales", "ans": 0,
   "fases": [("Fase 0", "Milisegundos", "ENTRA SODIO", ["Canales rápidos"]),
             ("Fase 2", "Meseta", "Entra calcio", ["Canales tipo L"]),
             ("Fase 3", "Repolarización", "Sale potasio", ["Canales K"])],
   "curvas": [("Potencial", SKY, [0.1, 0.95, 0.8, 0.78, 0.7, 0.3, 0.1])],
   "chips_titulo": "Fase 0 · marcado el correcto",
   "chips": [("gNa", True), ("gK", False), ("gCa", False), ("gCl", False)]},
  ["Clase I (lidocaína): bloquea sodio.",
   "Nodo sinusal: fase 0 por calcio.",
   "Fase 4: reposo por bomba Na/K."],
  GUYTON)

# CB-276 · radial
V("radial", "CB-276", "meseta-calcio-tipo-l-contractilidad-miocardio", "Meseta del potencial cardíaco",
  "CIENCIAS BÁSICAS ENAM: CONTRACTILIDAD", CB,
  ("Meseta (fase 2)", ["Entrada de calcio por canales tipo L",
   "Dispara la liberación de calcio del retículo"]),
  ("Pregunta de fisiología", ["¿Sobre qué influye la meseta?"]),
  {"rotulo": "Mapa del tema", "centro": "MESETA", "centro_sub": "Fase 2", "ans": 0,
   "items": [("CONTRACTILIDAD", ["Más calcio,", "más fuerza"]),
             ("Periodo refractario", ["Evita la tetania"]),
             ("Rianodina", ["Calcio del retículo"]),
             ("Verapamilo", ["Inotrópico negativo"]),
             ("Beta-agonistas", ["Aumentan fuerza"])],
   "ruta": ["Canal tipo L", "Calcio entra", "Retículo libera", "CONTRACCIÓN"]},
  ["Liberación de calcio inducida por calcio.",
   "No define la frecuencia cardíaca.",
   "Dura 200-300 ms."],
  GUYTON)

# CB-277 · puntaje
V("puntaje", "CB-277", "ph-720-bicarbonato-15-pco2-30-formula-winter", "Fórmula de Winter",
  "CIENCIAS BÁSICAS ENAM: EQUILIBRIO ÁCIDO-BASE", CB,
  ("Acidosis metabólica", ["pH bajo con bicarbonato bajo",
   "PCO2 esperada = 1,5 × HCO3 + 8 ± 2"]),
  ("Gasometría del caso", ["pH 7,20 · HCO3 15 mEq/L", "PCO2 30 mmHg"]),
  {"rotulo": "Compensación esperada", "escala": "mmHg", "total": 30, "max": 40,
   "total_label": "PCO2 medida",
   "interpreta": "Acidosis metabólica simple",
   "items": [("1,5 × 15", "22,5", True), ("+ 8", "30,5", True), ("Rango", "28,5-32,5", True)],
   "bandas": [("< 28,5", "Más baja", "+ alcalosis resp.", False),
              ("28,5-32,5", "Esperada", "Simple", True),
              ("> 32,5", "Más alta", "+ acidosis resp.", False)]},
  ["La compensación nunca normaliza el pH.",
   "Siguiente paso: anión gap.",
   "pH < 7,35 = acidemia."],
  HARRISON)

# CB-278 · árbol
A("CB-278", "anion-gap-elevado-salicilatos-mudpiles", "Acidosis metabólica según el anión gap",
  "CIENCIAS BÁSICAS ENAM: ANIÓN GAP", CB,
  ("Anión gap", ["Na − (Cl + HCO3): normal 8-12",
   "Aumenta con ácidos no medidos"]),
  ("Pregunta de fisiopatología", ["¿Qué causa acidosis con anión gap alto?"]),
  Q("¿Anión gap elevado?", [
      L("Sí", "ASPIRINA", ["MUDPILES", "Metanol, lactato, cetonas"], path=True),
      L("No", "Hiperclorémica", ["Diarrea, fístulas", "ATR, ureterosigmoidostomía"])], path=True),
  ("Salicilatos", [("Fase", True), ("Trastorno", False)], [
      ("Inicial", ["Estímulo respiratorio", "Alcalosis respiratoria"]),
      ("Luego", ["Desacopla mitocondria", "Acidosis con gap alto"])]),
  ["Cloruro de amonio: gap normal.",
   "Etilenglicol: cristales de oxalato.",
   "Calcular siempre el gap osmolar."],
  HARRISON)

# CB-279 · termómetro
V("termometro", "CB-279", "hidroclorotiazida-hiponatremia-adulta-mayor", "Diuréticos e hiponatremia",
  "CIENCIAS BÁSICAS ENAM: HIPONATREMIA POR FÁRMACOS", CB,
  ("Hiponatremia por diuréticos", ["Las tiazidas son las más frecuentes",
   "Mantienen la capacidad de concentrar la orina"]),
  ("Pregunta de farmacología", ["¿Qué fármaco causa más hiponatremia?"]),
  {"rotulo": "Riesgo de hiponatremia",
   "niveles": [("Bajo", "Acetazolamida", ["Acidosis"]),
               ("Bajo", "Espironolactona", ["Hiperpotasemia"]),
               ("Moderado", "Furosemida", ["Se usa en SIADH"]),
               ("Alto", "HIDROCLOROTIAZIDA", ["Mujeres mayores"])],
   "caso_nivel": 3, "ruta_titulo": "Por qué la tiazida", "paso_label": "PASO",
   "pasos": [(1, "Actúa en la corteza", ["Túbulo distal"], True),
             (2, "Médula intacta", ["Concentra la orina"], True),
             (3, "Retiene agua libre", ["Con ADH"], False)]},
  ["Aparece en las primeras semanas.",
   "Manitol: hiponatremia por dilución.",
   "Controlar sodio al iniciar."],
  GOODMAN)

# CB-280 · radial
V("radial", "CB-280", "tabique-nasal-lamina-perpendicular-etmoides-vomer", "Tabique nasal",
  "CIENCIAS BÁSICAS ENAM: NARIZ", CB,
  ("Tabique nasal", ["Parte ósea posterior y cartílago anterior",
   "Hueso: etmoides y vómer"]),
  ("Pregunta de anatomía", ["¿Qué hueso forma parte del tabique?"]),
  {"rotulo": "Mapa del tema", "centro": "TABIQUE", "centro_sub": "Nasal", "ans": 0,
   "items": [("ETMOIDES", ["Lámina perpendicular", "Arriba y adelante"]),
             ("Vómer", ["Atrás y abajo"]),
             ("Cartílago", ["Septal anterior"]),
             ("Kiesselbach", ["90 % de epistaxis"]),
             ("Hematoma", ["Drenar pronto"])],
   "ruta": ["Tabique óseo", "Parte superior", "Lámina perpendicular", "ETMOIDES"]},
  ["Pequeñas crestas: maxilar y palatino.",
   "Nariz en silla de montar: necrosis del cartílago.",
   "Esfenopalatina: epistaxis posterior."],
  MOORE)

# CB-281 · tarjetas
V("tarjetas", "CB-281", "glandulas-sebaceas-secrecion-holocrina", "Tipos de secreción glandular",
  "CIENCIAS BÁSICAS ENAM: GLÁNDULAS", CB,
  ("Mecanismos de secreción", ["Según cuánto se pierde de la célula",
   "Las sebáceas pierden la célula entera"]),
  ("Pregunta de histología", ["¿Qué tipo son las glándulas sebáceas?"]),
  {"rotulo": "¿Cómo secreta?", "ans": 0, "cards": [
      {"titulo": "HOLOCRINA", "datos": [
          ("Célula", "Muere entera", True), ("Ejemplo", "Sebácea", True),
          ("Producto", "Sebo", True)],
       "pie": "Acné: estímulo androgénico"},
      {"titulo": "Merocrina (ecrina)", "datos": [
          ("Célula", "Intacta", False), ("Ejemplo", "Sudorípara", False),
          ("Mecanismo", "Exocitosis", False)],
       "pie": "Salivales, páncreas"},
      {"titulo": "Apocrina", "datos": [
          ("Célula", "Pierde el ápice", False), ("Ejemplo", "Mamaria", False),
          ("Otra", "Axilar", False)],
       "pie": "Lípidos de la leche"},
      {"titulo": "Endocrina", "datos": [
          ("Destino", "Sangre", False), ("Conducto", "No tiene", False),
          ("Ejemplo", "Tiroides", False)],
       "pie": "Hormonas"}]},
  ["Sebáceas desembocan en el folículo piloso.",
   "Apocrinas: olor corporal.",
   "Ecrinas: termorregulación."],
  ROSS)

# CB-282 · matriz
V("matriz", "CB-282", "meromelia-ausencia-parcial-manos-pies-focomelia", "Defectos de las extremidades",
  "CIENCIAS BÁSICAS ENAM: MALFORMACIONES", CB,
  ("Defectos de extremidades", ["Se nombran según lo que falta",
   "Ocurren entre las semanas 4 y 8"]),
  ("Pregunta de embriología", ["Ausencia de manos y pies", "¿Cómo se llama?"]),
  {"rotulo": "Defecto y descripción", "eje_x": "Dato", "eje_y": "Defecto",
   "cols": ["Qué falta", "Ejemplo"], "rows": ["Amelia", "Meromelia", "Focomelia"], "caso": (1, 0),
   "cells": [[("Todo el miembro", []), ("Sin brazo", [])],
             [("PARTE DEL MIEMBRO", ["Manos o pies"]), ("Ausencia parcial", [])],
             [("Huesos largos", []), ("Aletas de foca", ["Talidomida"])]]},
  ["Sirenomelia: fusión de piernas.",
   "Sinfalangismo: fusión de falanges.",
   "Braquicefalia: forma del cráneo."],
  LANGMAN)

# CB-283 · termómetro
V("termometro", "CB-283", "dermatoma-ombligo-t10-pezon-t4", "Dermatomas de referencia",
  "CIENCIAS BÁSICAS ENAM: DERMATOMAS", CB,
  ("Dermatomas", ["Área de piel de una raíz espinal",
   "Referencias útiles en el examen neurológico"]),
  ("Pregunta de anatomía", ["¿Qué dermatoma corresponde al ombligo?"]),
  {"rotulo": "Niveles (de abajo arriba)",
   "niveles": [("T4", "Pezón", ["Cesárea: bloqueo a T4"]),
               ("T6", "Xifoides", ["Apéndice xifoides"]),
               ("T10", "OMBLIGO", ["Dolor apendicular inicial"]),
               ("L1", "Ingle", ["Región inguinal"])],
   "caso_nivel": 2, "ruta_titulo": "Utilidad clínica", "paso_label": "PASO",
   "pasos": [(1, "Nivel sensitivo", ["Lesión medular"], False),
             (2, "Dolor referido", ["Apéndice: periumbilical"], True),
             (3, "Anestesia", ["Altura del bloqueo"], False)]},
  ["L4: rótula; L5: dorso del pie.",
   "S1: borde lateral del pie.",
   "C6: pulgar; C8: meñique."],
  MOORE)

# CB-284 · termómetro
V("termometro", "CB-284", "vagina-tercio-superior-arteria-uterina-cervicovaginal", "Irrigación de la vagina",
  "CIENCIAS BÁSICAS ENAM: PELVIS FEMENINA", CB,
  ("Irrigación de la vagina", ["Cada tercio tiene su arteria",
   "Forman arterias ácigos longitudinales"]),
  ("Pregunta de anatomía", ["¿Qué arteria irriga el tercio superior?"]),
  {"rotulo": "Niveles (de abajo arriba)",
   "niveles": [("Tercio superior", "Uterina", ["RAMA CERVICOVAGINAL"]),
               ("Tercio medio", "Vaginal", ["Rama ilíaca interna"]),
               ("Tercio inferior", "Rectal media", ["Y pudenda interna"]),
               ("Vulva", "Pudenda", ["Interna y externa"])],
   "caso_nivel": 0, "ruta_titulo": "Drenaje linfático", "paso_label": "PASO",
   "pasos": [(1, "Tercio superior", ["Ganglios ilíacos"], True),
             (2, "Tercio medio", ["Ilíacos internos"], False),
             (3, "Tercio inferior", ["Inguinales"], False)]},
  ["Importa en el cáncer de cuello y vagina.",
   "La uterina cruza por encima del uréter.",
   "Ligadura de uterinas en hemorragia."],
  MOORE)

# CB-285 · fases
V("fases", "CB-285", "sertoli-sosten-espermatogenesis-epididimo-maduracion", "Maduración del espermatozoide",
  "CIENCIAS BÁSICAS ENAM: ESPERMIOGÉNESIS", CB,
  ("Formación del espermatozoide", ["La célula de Sertoli sostiene y nutre",
   "El epidídimo completa la maduración"]),
  ("Pregunta de histología", ["¿Gracias a qué célula maduran?"]),
  {"rotulo": "Etapas", "ans": 0,
   "fases": [("Túbulo", "64-74 días", "SERTOLI", ["Sostén y nutrición", "Fagocita citoplasma"]),
             ("Epidídimo", "10-14 días", "Motilidad", ["Capacidad de fecundar"]),
             ("Mujer", "Horas", "Capacitación", ["Tracto femenino"])],
   "chips_titulo": "Célula · marcada la correcta",
   "chips": [("Sertoli", True), ("Leydig", False), ("Mioides", False), ("Paneth", False)]},
  ["Barrera hematotesticular.",
   "Proteína fijadora de andrógenos.",
   "Leydig: testosterona."],
  ROSS)

# CB-286 · puntaje
V("puntaje", "CB-286", "vancomicina-infusion-rapida-sindrome-hombre-rojo", "Síndrome del hombre rojo",
  "CIENCIAS BÁSICAS ENAM: VANCOMICINA", CB,
  ("Síndrome del hombre rojo", ["Degranulación directa de mastocitos",
   "No es alergia por IgE"]),
  ("Pregunta de farmacología", ["¿Qué fármaco lo produce?"]),
  {"rotulo": "Velocidad de infusión", "escala": "Minutos", "total": 60, "max": 120,
   "total_label": "Tiempo mínimo por 1 g",
   "interpreta": "Vancomicina: ≥ 60 min",
   "items": [("Dosis", "1 g", True), ("Velocidad máx.", "10 mg/min", True), ("Premedicación", "Anti-H1", False)],
   "bandas": [("< 30 min", "Rápida", "Hombre rojo", False),
              ("≥ 60 min", "Segura", "Infusión lenta", True),
              ("Si ocurre", "Pausar", "Antihistamínico", False)]},
  ["Eritema en cara, cuello y tronco.",
   "Puede dar hipotensión.",
   "Nefrotóxica y ototóxica."],
  GOODMAN)

# CB-287 · embudo
V("embudo", "CB-287", "agricultor-midriasis-piel-seca-euforia-floripondio", "Síndrome anticolinérgico en el campo",
  "CIENCIAS BÁSICAS ENAM: PLANTAS TÓXICAS", CB,
  ("Síndrome anticolinérgico", ["Midriasis, piel seca y roja",
   "Delirio o euforia"]),
  ("Agricultor", ["Eufórico, pupilas midriáticas", "Piel seca"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Midriasis con euforia",
   "candidatos": ["Floripondio", "Cocaína", "Crack", "Heroína"],
   "pasos": [("Hay midriasis", ["Heroína"]),
             ("Piel seca, no sudorosa", ["Cocaína", "Crack"])],
   "final": ("FLORIPONDIO O CHAMICO", ["Alcaloides tropánicos", "Atropina y escopolamina"]),
   "nota": "Simpaticomiméticos: midriasis con sudoración."},
  ["Datura y Brugmansia.",
   "Uso delictivo: burundanga.",
   "Grave: fisostigmina."],
  TOXI)

# CB-288 · tarjetas
V("tarjetas", "CB-288", "gestante-tuberculosis-estreptomicina-sordera-congenita", "Antituberculosos en el embarazo",
  "CIENCIAS BÁSICAS ENAM: TBC Y GESTACIÓN", CB,
  ("TBC en la gestación", ["La TBC no tratada es más peligrosa",
   "Se evitan los aminoglucósidos"]),
  ("Pregunta de farmacología", ["¿Qué antituberculoso está contraindicado?"]),
  {"rotulo": "¿Seguro en el embarazo?", "ans": 0, "cards": [
      {"titulo": "ESTREPTOMICINA", "datos": [
          ("Riesgo", "Sordera fetal", True), ("Mecanismo", "VIII par", True),
          ("Uso", "Contraindicada", True)],
       "pie": "Aminoglucósido"},
      {"titulo": "Isoniacida", "datos": [
          ("Riesgo", "Bajo", False), ("Añadir", "Piridoxina", False),
          ("Uso", "Permitida", False)],
       "pie": "Primera línea"},
      {"titulo": "Rifampicina", "datos": [
          ("Riesgo", "Bajo", False), ("Extra", "Vitamina K", False),
          ("Uso", "Permitida", False)],
       "pie": "Primera línea"},
      {"titulo": "Etambutol", "datos": [
          ("Riesgo", "Bajo", False), ("Vigilar", "Visión", False),
          ("Uso", "Permitido", False)],
       "pie": "Pirazinamida: también"}]},
  ["Lactancia permitida.",
   "Evitar amikacina y kanamicina.",
   "Norma técnica peruana de TB."],
  MINSA_TB)

# CB-289 · árbol
A("CB-289", "pseudomonas-grave-betalactamico-mas-aminoglucosido", "Tratamiento empírico de Pseudomonas",
  "CIENCIAS BÁSICAS ENAM: PSEUDOMONAS", CB,
  ("Pseudomonas aeruginosa grave", ["Neutropenia febril, sepsis, NAV",
   "Riesgo de resistencia"]),
  ("Pregunta de farmacología", ["¿Mejor combinación empírica?"]),
  Q("¿Infección grave con riesgo de resistencia?", [
      L("Sí", "BETALACTÁMICO + AMINOGL.", ["Pip-tazo o ceftazidima", "+ amikacina"], path=True),
      L("No", "Un betalactámico", ["Antipseudomonas"])], path=True),
  ("Por qué combinar", [("Motivo", True), ("Efecto", False)], [
      ("Sinergia", ["Pared dañada", "Entra el aminoglucósido"]),
      ("Cobertura", ["Cepas resistentes", "Mientras llega cultivo"])]),
  ["Luego ajustar a un solo fármaco.",
   "Macrólidos no cubren Pseudomonas.",
   "Carbapenémicos y cefepime: alternativas."],
  SANFORD)

# CB-290 · radial
V("radial", "CB-290", "nociceptores-terminaciones-nerviosas-libres", "Receptores sensitivos de la piel",
  "CIENCIAS BÁSICAS ENAM: RECEPTORES SENSITIVOS", CB,
  ("Receptores de la piel", ["Encapsulados: tacto, presión, vibración",
   "Libres: dolor y temperatura"]),
  ("Pregunta de fisiología", ["¿Por qué receptor se percibe el dolor?"]),
  {"rotulo": "Mapa del tema", "centro": "PIEL", "centro_sub": "Receptores", "ans": 0,
   "items": [("TERMINACIONES", ["LIBRES: dolor", "A-delta y C"]),
             ("Pacini", ["Vibración"]),
             ("Meissner", ["Tacto fino"]),
             ("Merkel", ["Presión sostenida"]),
             ("Krause", ["Frío"])],
   "ruta": ["Estímulo dañino", "Sin cápsula", "Fibras A-δ y C", "DOLOR"]},
  ["Prostaglandinas sensibilizan: hiperalgesia.",
   "AINE reducen esa sensibilización.",
   "Ruffini: estiramiento."],
  GUYTON)

# CB-291 · matriz
V("matriz", "CB-291", "quimiorreceptores-centrales-paco2-perifericos-hipoxemia", "Quimiorreceptores",
  "CIENCIAS BÁSICAS ENAM: CONTROL DE LA RESPIRACIÓN", CB,
  ("Quimiorreceptores", ["Centrales: bulbo, sensibles al CO2 y pH",
   "Periféricos: carotídeos y aórticos"]),
  ("Pregunta de fisiología", ["¿Qué receptor responde más a la PaCO2 alta?"]),
  {"rotulo": "Tipo y estímulo", "eje_x": "Tipo", "eje_y": "Rasgo",
   "cols": ["Centrales", "Periféricos"], "rows": ["Estímulo", "Aporte", "EPOC"], "caso": (1, 0),
   "cells": [[("CO2 y H⁺ del LCR", []), ("PaO2 < 60", [])],
             [("70-80 % DEL CO2", ["Principal"]), ("Más rápidos", [])],
             [("Se adaptan", []), ("Cobran importancia", [])]]},
  ["EPOC hipercápnico: oxígeno controlado.",
   "SatO2 meta 88-92 %.",
   "El CO2 cruza la barrera hematoencefálica."],
  GUYTON)

# CB-292 · árbol
A("CB-292", "vena-gonadal-izquierda-renal-varicocele-izquierdo", "Drenaje de las venas gonadales",
  "CIENCIAS BÁSICAS ENAM: VENAS GONADALES", CB,
  ("Venas gonadales", ["Derecha: a la cava inferior",
   "Izquierda: a la vena renal izquierda"]),
  ("Pregunta de anatomía", ["¿Dónde desemboca la vena gonadal izquierda?"]),
  Q("¿Qué lado?", [
      L("Izquierda", "VENA RENAL IZQ.", ["En ángulo recto", "Varicocele frecuente"], path=True),
      L("Derecha", "Cava inferior", ["En ángulo agudo"])], path=True),
  ("Varicocele", [("Lado", True), ("Significado", False)], [
      ("Izquierdo", ["90 %", "Anatomía normal"]),
      ("Derecho o brusco", ["Raro", "Buscar masa"])]),
  ["Cascanueces: aorta y mesentérica.",
   "No se vacía al acostarse: sospechar tumor.",
   "Tumor renal con trombo en la vena."],
  MOORE)
