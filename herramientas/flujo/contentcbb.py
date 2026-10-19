"""Ciencias Básicas · parte B (CB-133 a CB-172)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-133 · termómetro
V("termometro", "CB-133", "agua-corporal-total-nino-3-anos-65-por-ciento", "Agua corporal según la edad",
  "CIENCIAS BÁSICAS ENAM: AGUA CORPORAL", CB,
  ("Agua corporal total", ["Disminuye con la edad",
   "A los 3 años se acerca a los valores del adulto"]),
  ("Niño de 3 años", ["¿Qué porcentaje de su peso es agua?"]),
  {"rotulo": "Agua según la edad",
   "niveles": [("Prematuro", "≈ 80 %", ["Mucha agua extracelular"]),
               ("Recién nacido", "≈ 75 %", ["A término"]),
               ("Niño 1-3 años", "≈ 60-65 %", ["ESTE CASO: 65 %"]),
               ("Adulto", "50-60 %", ["Mujer menos que varón"])],
   "caso_nivel": 2, "ruta_titulo": "Por qué se deshidrata fácil", "paso_label": "PASO",
   "pasos": [(1, "Más agua por kilo", ["Y más recambio diario"], True),
             (2, "Mayor superficie", ["Más pérdidas insensibles"], False),
             (3, "Riñón inmaduro", ["Concentra menos"], False)]},
  ["El lactante tiene más agua extracelular.",
   "La grasa contiene poca agua.",
   "Diarrea en lactantes: deshidratación rápida."],
  NELSON)

# CB-134 · fases
V("fases", "CB-134", "anencefalia-neuroporo-anterior-cuarta-semana", "Cierre del tubo neural",
  "CIENCIAS BÁSICAS ENAM: DEFECTOS DEL TUBO NEURAL", CB,
  ("Neurulación", ["El tubo neural se forma en la 3.ª semana",
   "Los neuroporos se cierran en la 4.ª semana"]),
  ("Gestante de 35 semanas", ["Ecografía: feto anencefálico", "¿Cuándo se originó el defecto?"]),
  {"rotulo": "Semanas del desarrollo", "ans": 1,
   "fases": [("Semana 3", "Días 15-21", "Placa neural", ["Pliegues neurales"]),
             ("Semana 4", "Días 25-28", "CIERRE", ["Neuroporo anterior: día 25", "Posterior: día 27-28"]),
             ("Semana 5+", "Después", "Vesículas", ["Prosencéfalo, etc."])],
   "chips_titulo": "Semana del defecto · marcada la correcta",
   "chips": [("Cuarta", True), ("Segunda", False), ("Tercera", False), ("Sexta", False)]},
  ["Anencefalia: falla del neuroporo anterior.",
   "Espina bífida: falla del neuroporo posterior.",
   "Prevención: ácido fólico antes de concebir."],
  LANGMAN)

# CB-135 · árbol
A("CB-135", "furosemida-venodilatacion-precarga-edema-pulmonar", "Acciones de los diuréticos de asa",
  "CIENCIAS BÁSICAS ENAM: DIURÉTICOS DE ASA", CB,
  ("Diuréticos de asa", ["Bloquean el NKCC2 del asa de Henle",
   "Diuréticos más potentes"]),
  ("Pregunta de farmacología", ["¿Qué acción corresponde a la furosemida?"]),
  Q("¿Qué efecto aparece primero por vía IV?", [
      L("Minutos", "VENODILATACIÓN", ["Baja el llenado del VI", "Alivia el edema pulmonar"], path=True),
      L("Horas", "Diuresis", ["Pierde Na, K, Ca, Mg"])], path=True),
  ("Opciones falsas del caso", [("Dice", True), ("Realidad", False)], [
      ("Potasio", ["Lo retiene", "Lo elimina"]),
      ("Calcio", ["Lo reabsorbe", "Aumenta su excreción"])]),
  ["Útiles en la hipercalcemia tras hidratar.",
   "No estimulan la anhidrasa carbónica.",
   "Ototoxicidad con dosis altas."],
  GOODMAN)

# CB-136 · fases
V("fases", "CB-136", "musculo-anaerobio-lactato-deshidrogenasa-ciclo-cori", "Glucólisis sin oxígeno",
  "CIENCIAS BÁSICAS ENAM: METABOLISMO MUSCULAR", CB,
  ("Glucólisis anaerobia", ["Sin oxígeno, el piruvato no entra al Krebs",
   "Se reduce a lactato para regenerar NAD⁺"]),
  ("Pregunta de bioquímica", ["Músculo que se contrae sin oxígeno", "¿Qué ocurre?"]),
  {"rotulo": "Destino de la glucosa", "ans": 1,
   "fases": [("Glucólisis", "Citosol", "Piruvato", ["2 ATP", "Gasta NAD⁺"]),
             ("Anaerobia", "Sin O2", "LACTATO", ["Lactato DH", "Recupera NAD⁺"]),
             ("Hígado", "Ciclo de Cori", "Glucosa", ["Gluconeogénesis"])],
   "chips_titulo": "Qué aumenta · marcado el correcto",
   "chips": [("Lactato", True), ("Piruvato", False), ("Glucógeno", False), ("ATP", False)]},
  ["Lactato > 2 mmol/L: hipoperfusión.",
   "El piruvato no se acumula: se transforma.",
   "Durante el ejercicio baja la síntesis de glucógeno."],
  HARPER)

# CB-137 · tarjetas
V("tarjetas", "CB-137", "etambutol-neuritis-optica-rojo-verde-suspender", "Efectos adversos de los antituberculosos",
  "CIENCIAS BÁSICAS ENAM: RAM ANTITUBERCULOSA", CB,
  ("Reacciones adversas antituberculosas", ["Cada fármaco tiene un efecto típico",
   "La clínica orienta a cuál suspender"]),
  ("Mujer de 20 años con TBC", ["Tratamiento desde hace 3 meses", "Baja la visión y confunde rojo y verde"]),
  {"rotulo": "¿Qué fármaco lo causa?", "ans": 0, "cards": [
      {"titulo": "ETAMBUTOL", "datos": [
          ("Efecto", "Neuritis óptica", True), ("Clave", "Rojo-verde", True),
          ("Conducta", "Suspender", True)],
       "pie": "Reversible si se detecta a tiempo"},
      {"titulo": "Isoniacida", "datos": [
          ("Efecto", "Neuropatía", False), ("Clave", "Parestesias", False),
          ("Prevención", "Piridoxina", False)],
       "pie": "También hepatitis"},
      {"titulo": "Rifampicina", "datos": [
          ("Efecto", "Hepatitis", False), ("Clave", "Orina naranja", False),
          ("Extra", "Inductor P450", False)],
       "pie": "Interacciones"},
      {"titulo": "Pirazinamida", "datos": [
          ("Efecto", "Hiperuricemia", False), ("Clave", "Artralgias", False),
          ("Extra", "Hepatotóxica", False)],
       "pie": "Gota"}]},
  ["Evaluar agudeza y colores antes de iniciar.",
   "Ajustar el etambutol en insuficiencia renal.",
   "Estreptomicina: ototoxicidad."],
  MINSA_TB)

# CB-138 · puntaje
V("puntaje", "CB-138", "cloruro-sodio-3-por-ciento-05-meq-ml-hiponatremia", "Sodio del suero hipertónico al 3 %",
  "CIENCIAS BÁSICAS ENAM: SOLUCIONES HIPERTÓNICAS", CB,
  ("NaCl al 3 %", ["30 g de NaCl por litro",
   "30 000 ÷ 58,5 ≈ 513 mEq/L = 0,5 mEq/mL"]),
  ("Hiponatremia grave sintomática", ["¿Cuánto sodio aporta el NaCl 3 %?"]),
  {"rotulo": "Cálculo", "escala": "mEq/mL", "total": 0.5, "max": 3.4,
   "total_label": "Sodio por mL",
   "interpreta": "≈ 0,5 mEq/mL",
   "items": [("NaCl por 100 mL", "3 g", True), ("Por litro", "30 g", True),
             ("Resultado", "513 mEq/L", True)],
   "bandas": [("0,154", "NaCl 0,9 %", "Reanimación", False),
              ("0,5", "NaCl 3 %", "Hiponatremia grave", True),
              ("3,4", "NaCl 20 %", "Concentrado: diluir", False)]},
  ["Bolos de 100-150 mL en 10-20 minutos.",
   "Corregir ≤ 8-10 mEq/L en 24 horas.",
   "Exceso: desmielinización osmótica."],
  "Guía europea de hiponatremia (2014) · " + GUYTON)

# CB-139 · tarjetas
V("tarjetas", "CB-139", "quinolonas-adn-girasa-topoisomerasa-iv", "Mecanismo de los antibióticos",
  "CIENCIAS BÁSICAS ENAM: QUINOLONAS", CB,
  ("Blancos de los antibióticos", ["Pared, ribosoma, ácido fólico o ADN",
   "Las quinolonas atacan la replicación del ADN"]),
  ("Pregunta de farmacología", ["¿Cuál es el mecanismo de las quinolonas?"]),
  {"rotulo": "¿Qué inhibe?", "ans": 0, "cards": [
      {"titulo": "QUINOLONAS", "datos": [
          ("Blanco", "ADN girasa", True), ("Gramnegativos", "Girasa", True),
          ("Grampositivos", "Topo IV", True)],
       "pie": "Bactericidas"},
      {"titulo": "Rifampicina", "datos": [
          ("Blanco", "ARN polimerasa", False), ("Uso", "TBC", False),
          ("Efecto", "Bactericida", False)],
       "pie": "Transcripción"},
      {"titulo": "Aminoglucósidos", "datos": [
          ("Blanco", "Ribosoma 30S", False), ("Uso", "Gramnegativos", False),
          ("Efecto", "Bactericida", False)],
       "pie": "Síntesis proteica"},
      {"titulo": "Betalactámicos", "datos": [
          ("Blanco", "PBP", False), ("Uso", "Amplio", False),
          ("Efecto", "Bactericida", False)],
       "pie": "Pared celular"}]},
  ["Quinolonas: tendinitis y rotura del Aquiles.",
   "Alargan el QT.",
   "Se evitan en niños y gestantes."],
  GOODMAN)

# CB-140 · matriz
V("matriz", "CB-140", "apoptosis-sin-inflamacion-cuerpos-apoptoticos-necrosis", "Apoptosis frente a necrosis",
  "CIENCIAS BÁSICAS ENAM: MUERTE CELULAR", CB,
  ("Muerte celular", ["Apoptosis: programada, ordenada, por caspasas",
   "Necrosis: accidental, con rotura de membrana"]),
  ("Pregunta de patología", ["¿Qué afirmación de la apoptosis es correcta?"]),
  {"rotulo": "Rasgos comparados", "eje_x": "Tipo", "eje_y": "Rasgo",
   "cols": ["Apoptosis", "Necrosis"], "rows": ["Extensión", "Membrana", "Inflamación"], "caso": (2, 0),
   "cells": [[("Célula aislada", []), ("Grupos de células", [])],
             [("Íntegra", ["Cuerpos apoptóticos"]), ("Se rompe", ["Vierte contenido"])],
             [("NO HAY", ["Fagocitosis rápida"]), ("Sí hay", ["Neutrófilos"])]]},
  ["Picnosis y cariorrexis: núcleo condensado y roto.",
   "Fosfatidilserina expuesta atrae macrófagos.",
   "Ejemplo fisiológico: involución del timo."],
  ROBBINS)

# CB-141 · fases
V("fases", "CB-141", "testiculo-nacimiento-espermatogonias-sertoli-pubertad", "Células germinales del testículo",
  "CIENCIAS BÁSICAS ENAM: ESPERMATOGÉNESIS", CB,
  ("Espermatogénesis", ["Empieza en la pubertad",
   "Antes solo hay espermatogonias detenidas"]),
  ("Pregunta de embriología", ["¿Qué células hay en el testículo al nacer?"]),
  {"rotulo": "Etapas de la vida", "ans": 0,
   "fases": [("Nacimiento", "Cordones macizos", "ESPERMATOGONIAS", ["Y células de Sertoli"]),
             ("Pubertad", "Testosterona", "Meiosis", ["Espermatocitos"]),
             ("Adulto", "64-74 días", "Espermatozoides", ["Producción continua"])],
   "chips_titulo": "Células al nacer · marcado el correcto",
   "chips": [("Espermatogonias", True), ("Espermatocitos I", False), ("Espermátides", False), ("F. primordiales", False)]},
  ["El ovario fetal ya inicia la meiosis I.",
   "Ovocitos detenidos en profase I.",
   "Folículos primordiales: solo en el ovario."],
  LANGMAN)

# CB-142 · matriz
V("matriz", "CB-142", "homologias-genitales-labio-mayor-escroto", "Homologías de los genitales externos",
  "CIENCIAS BÁSICAS ENAM: GENITALES EXTERNOS", CB,
  ("Genitales externos", ["Parten de estructuras iguales en ambos sexos",
   "La dihidrotestosterona las masculiniza"]),
  ("Pregunta de embriología", ["¿Qué estructura masculina es homóloga", "del labio mayor?"]),
  {"rotulo": "Estructura primitiva", "eje_x": "Sexo", "eje_y": "Origen",
   "cols": ["Mujer", "Varón"], "rows": ["Tubérculo genital", "Pliegues uretrales", "Eminencias lab.-esc."], "caso": (2, 1),
   "cells": [[("Clítoris", []), ("Glande, cavernosos", [])],
             [("Labios menores", []), ("Uretra esponjosa", [])],
             [("Labios mayores", []), ("ESCROTO", ["Homólogo del caso"])]]},
  ["Seno urogenital: vestíbulo o uretra prostática.",
   "Gubernáculo: ligamento redondo en la mujer.",
   "Fusión incompleta: escroto bífido."],
  LANGMAN)

# CB-143 · tarjetas
V("tarjetas", "CB-143", "sindrome-down-trisomia-21-libre-no-disyuncion", "Cariotipos del síndrome de Down",
  "CIENCIAS BÁSICAS ENAM: GENÉTICA", CB,
  ("Síndrome de Down", ["Tres copias del cromosoma 21",
   "Tres mecanismos posibles"]),
  ("Pregunta de genética", ["¿Cuál es el cariotipo más frecuente?"]),
  {"rotulo": "Frecuencia del cariotipo", "ans": 0, "cards": [
      {"titulo": "TRISOMÍA 21 LIBRE", "datos": [
          ("Frecuencia", "≈ 95 %", True), ("Causa", "No disyunción", True),
          ("Riesgo", "Edad materna", True)],
       "pie": "Meiosis I materna"},
      {"titulo": "Translocación", "datos": [
          ("Frecuencia", "3-4 %", False), ("Tipo", "Robertsoniana", False),
          ("Riesgo", "Padre portador", False)],
       "pie": "Estudiar a los padres"},
      {"titulo": "Mosaico", "datos": [
          ("Frecuencia", "1-2 %", False), ("Causa", "Error mitótico", False),
          ("Fenotipo", "Más leve", False)],
       "pie": "Dos líneas celulares"},
      {"titulo": "Hallazgos", "datos": [
          ("Tono", "Hipotonía", False), ("Corazón", "Canal AV", False),
          ("Intestino", "Atresia duodenal", False)],
       "pie": "Pliegue palmar único"}]},
  ["Siempre se pide cariotipo.",
   "Translocación 14;21: consejo genético.",
   "Tamizaje: translucencia nucal y bioquímica."],
  "Thompson & Thompson. Genética en medicina 8.ª ed. · " + NELSON)

# CB-144 · radial
V("radial", "CB-144", "histamina-mastocitos-histidina-granulos", "Histamina",
  "CIENCIAS BÁSICAS ENAM: MEDIADORES", CB,
  ("Histamina", ["Se forma de la histidina por descarboxilación",
   "Se guarda en gránulos unida a heparina"]),
  ("Pregunta de fisiología", ["¿Qué células almacenan más histamina?"]),
  {"rotulo": "Mapa del tema", "centro": "HISTAMINA", "centro_sub": "Depósitos", "ans": 0,
   "items": [("MASTOCITOS", ["Mayor depósito", "Piel, pulmón, intestino"]),
             ("Basófilos", ["En la sangre", "Menor cantidad"]),
             ("Enterocromafines", ["Estómago: receptor H2"]),
             ("Efectos H1", ["Edema, prurito", "Broncoconstricción"]),
             ("Marcador", ["Triptasa sérica"])],
   "ruta": ["Alérgeno", "IgE en mastocito", "Degranulación", "HISTAMINA"]},
  ["La triptasa confirma la anafilaxia.",
   "H2: secreción ácida gástrica.",
   "Neuronas: vigilia (H1 central)."],
  ABBAS)

# CB-145 · embudo
V("embudo", "CB-145", "epitelio-plano-estratificado-queratinizado-epidermis", "Tipos de epitelio",
  "CIENCIAS BÁSICAS ENAM: EPITELIOS", CB,
  ("Epitelio plano estratificado", ["Queratinizado en superficies secas",
   "No queratinizado en superficies húmedas"]),
  ("Pregunta de histología", ["¿Dónde hay epitelio plano estratificado", "queratinizado?"]),
  {"rotulo": "Embudo histológico",
   "inicio": "Cinco órganos",
   "candidatos": ["Piel", "Vagina", "Esófago", "Tráquea"],
   "pasos": [("Epitelio estratificado plano", ["Tráquea"]),
             ("Superficie seca con queratina", ["Vagina", "Esófago"])],
   "final": ("PIEL (EPIDERMIS)", ["Capa córnea sin núcleos", "Resiste fricción y pérdida de agua"]),
   "nota": "Tráquea: pseudoestratificado ciliado; riñón: cúbico simple."},
  ["Boca, esófago, vagina: no queratinizado.",
   "Encía y paladar duro: paraqueratinizados.",
   "Metaplasia crónica puede queratinizarse."],
  ROSS)

# CB-146 · fases
V("fases", "CB-146", "contraccion-herida-miofibroblasto-segunda-intencion", "Contracción de la herida",
  "CIENCIAS BÁSICAS ENAM: CICATRIZACIÓN", CB,
  ("Cicatrización", ["Inflamación, proliferación y remodelación",
   "El miofibroblasto contrae los bordes"]),
  ("Pregunta de patología", ["¿Qué células contraen la herida?"]),
  {"rotulo": "Fases de la reparación", "ans": 1,
   "fases": [("Inflamatoria", "Días 1-3", "Neutrófilos", ["Limpian la herida"]),
             ("Proliferativa", "Días 4-21", "MIOFIBROBLASTO", ["Contrae la herida", "Actina de músculo liso"]),
             ("Remodelación", "Meses", "Colágeno I", ["Cicatriz madura"])],
   "chips_titulo": "Célula que contrae · marcada la correcta",
   "chips": [("Fibroblasto (miofibroblasto)", True), ("Neutrófilo", False), ("Macrófago", False), ("Fibrocito", False)]},
  ["Clave en la segunda intención.",
   "Exceso: contracturas en quemaduras.",
   "Macrófago: coordina con TGF-β y PDGF."],
  ROBBINS)

# CB-147 · matriz
V("matriz", "CB-147", "celulas-permanentes-cardiomiocito-neurona-labiles-estables", "Capacidad de regeneración",
  "CIENCIAS BÁSICAS ENAM: CICLO CELULAR", CB,
  ("Tipos de células según su división", ["Lábiles, estables y permanentes",
   "Las permanentes salieron del ciclo celular"]),
  ("Pregunta de patología", ["¿Cuál es una célula permanente?"]),
  {"rotulo": "Tipo y ejemplo", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Ciclo", "Ejemplos"], "rows": ["Lábiles", "Estables", "Permanentes"], "caso": (2, 1),
   "cells": [[("Dividen siempre", []), ("Piel, colon", ["Médula ósea"])],
             [("G0: reactivables", []), ("Hepatocito", ["Acinar, osteocito"])],
             [("Salieron del ciclo", []), ("CARDIOMIOCITO", ["Neurona"])]]},
  ["Infarto: cicatriz fibrosa, no músculo nuevo.",
   "Eritrocito: no se divide, pero su línea es lábil.",
   "Hígado: regenera tras hepatectomía parcial."],
  ROBBINS)

# CB-148 · termómetro
V("termometro", "CB-148", "ph-secreciones-digestivas-jugo-pancreatico-alcalino", "pH de las secreciones digestivas",
  "CIENCIAS BÁSICAS ENAM: FISIOLOGÍA DIGESTIVA", CB,
  ("pH de las secreciones", ["El estómago es muy ácido",
   "El páncreas neutraliza con bicarbonato"]),
  ("Pregunta de fisiología", ["¿Qué secreción tiene el pH más alto?"]),
  {"rotulo": "De ácido a alcalino",
   "niveles": [("pH 1-3,5", "Jugo gástrico", ["HCl"]),
               ("pH 6-7,4", "Saliva", ["Casi neutra"]),
               ("pH 7-7,6", "Bilis vesicular", ["Concentrada"]),
               ("pH 7,8-8,3", "JUGO PANCREÁTICO", ["Rico en bicarbonato"])],
   "caso_nivel": 3, "ruta_titulo": "Control de la secreción", "paso_label": "PASO",
   "pasos": [(1, "Ácido al duodeno", ["pH < 4,5"], False),
             (2, "Secretina", ["Células S"], True),
             (3, "Bicarbonato", ["Conductos pancreáticos"], True)]},
  ["Secreción intestinal: pH 7,5-8.",
   "Sin bicarbonato, la lipasa se inactiva.",
   "Pancreatitis crónica: esteatorrea."],
  GUYTON)

# CB-149 · matriz
V("matriz", "CB-149", "organofosforado-atropinizacion-midriasis-signos", "Atropinización en organofosforados",
  "CIENCIAS BÁSICAS ENAM: TOXICOLOGÍA", CB,
  ("Organofosforados y atropina", ["Exceso de acetilcolina: síndrome colinérgico",
   "La atropina bloquea los receptores muscarínicos"]),
  ("Paciente intoxicado ya tratado", ["Recibió atropina suficiente", "¿Qué signo tendrá?"]),
  {"rotulo": "Antes y después", "eje_x": "Momento", "eje_y": "Signo",
   "cols": ["Intoxicado", "Atropinizado"], "rows": ["Pupilas", "Secreciones", "Frecuencia"], "caso": (0, 1),
   "cells": [[("Miosis", []), ("MIDRIASIS", ["Signo del caso"])],
             [("Broncorrea", ["Sialorrea"]), ("Secas", ["Objetivo principal"])],
             [("Bradicardia", []), ("Taquicardia", ["FC > 80"])]]},
  ["Meta real: secar secreciones bronquiales.",
   "La atropina no corrige la debilidad muscular.",
   "Pralidoxima para el efecto nicotínico."],
  TOXI)

# CB-150 · radial
V("radial", "CB-150", "aldosterona-reabsorcion-sodio-colector-enac", "Hormonas que regulan el riñón",
  "CIENCIAS BÁSICAS ENAM: FISIOLOGÍA RENAL", CB,
  ("Regulación renal del sodio", ["La aldosterona es la hormona principal",
   "Actúa en el túbulo distal final y el colector"]),
  ("Pregunta de fisiología", ["¿Qué hormona regula la reabsorción de sodio?"]),
  {"rotulo": "Mapa del tema", "centro": "RIÑÓN", "centro_sub": "Hormonas", "ans": 0,
   "items": [("ALDOSTERONA", ["Reabsorbe sodio", "Elimina K y H⁺"]),
             ("ADH", ["Agua libre", "Acuaporina 2"]),
             ("Péptido natriurético", ["Elimina sodio"]),
             ("Angiotensina II", ["Vasoconstricción", "Estimula aldosterona"]),
             ("Renina", ["Enzima, no hormona"])],
   "ruta": ["Baja volemia", "Renina", "Angiotensina II", "ALDOSTERONA"]},
  ["Aumenta canales ENaC y bomba Na/K.",
   "Hiperaldosteronismo: HTA con hipopotasemia.",
   "Espironolactona: bloquea su receptor."],
  GUYTON)

# CB-151 · puntaje
V("puntaje", "CB-151", "intoxicacion-paracetamol-10-gramos-n-acetilcisteina", "Dosis tóxica de paracetamol",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR PARACETAMOL", CB,
  ("Paracetamol en sobredosis", ["Se acumula NAPQI y se agota el glutatión",
   "Riesgo hepático desde 7,5-10 g o 150 mg/kg"]),
  ("Paciente con ingesta hace 4 horas", ["20 tabletas de 500 mg", "¿Qué se indica?"]),
  {"rotulo": "Dosis ingerida", "escala": "Gramos", "total": 10, "max": 15,
   "total_label": "Total ingerido",
   "interpreta": "Tóxico: N-acetilcisteína",
   "items": [("Tabletas", "20", True), ("Por tableta", "0,5 g", True), ("Total", "10 g", True)],
   "bandas": [("< 7,5 g", "Bajo riesgo", "Observar", False),
              ("≥ 7,5-10 g", "Hepatotóxico", "N-acetilcisteína", True),
              ("Cualquier dosis", "Daño hepático", "NAC y soporte", False)]},
  ["Medir paracetamol a las 4 horas.",
   "Nomograma de Rumack-Matthew.",
   "NAC es casi 100 % eficaz antes de 8 horas."],
  TOXI)

# CB-152 · embudo
V("embudo", "CB-152", "corpusculos-hassall-medula-timo", "Corpúsculos de Hassall",
  "CIENCIAS BÁSICAS ENAM: ÓRGANOS LINFOIDES", CB,
  ("Órganos linfoides", ["Primarios: timo y médula ósea",
   "Secundarios: ganglios, bazo, placas de Peyer"]),
  ("Pregunta de histología", ["¿Qué órgano tiene corpúsculos de Hassall", "en la médula?"]),
  {"rotulo": "Embudo histológico",
   "inicio": "Órganos linfoides",
   "candidatos": ["Timo", "Ganglio", "Bazo", "Placas de Peyer"],
   "pasos": [("Tiene corteza y médula", ["Placas de Peyer"]),
             ("Epitelio reticular queratinizado", ["Ganglio", "Bazo"])],
   "final": ("TIMO", ["Hassall en la médula", "Maduración de linfocitos T"]),
   "nota": "Glomo carotídeo: quimiorreceptor, no linfoide."},
  ["Selección positiva en la corteza.",
   "Selección negativa en la médula.",
   "Hassall: favorece linfocitos T reguladores."],
  ROSS)

# CB-153 · tarjetas
V("tarjetas", "CB-153", "vertebras-cervicales-agujero-transverso-espinosa-bifida", "Rasgos de las vértebras",
  "CIENCIAS BÁSICAS ENAM: COLUMNA VERTEBRAL", CB,
  ("Vértebras por región", ["Cada región tiene rasgos propios",
   "Las cervicales tienen agujero transverso"]),
  ("Pregunta de anatomía", ["Espinosa bífida y agujero para la", "arteria vertebral"]),
  {"rotulo": "¿Qué región?", "ans": 0, "cards": [
      {"titulo": "CERVICALES", "datos": [
          ("Agujero", "Transverso", True), ("Espinosa", "Bífida", True),
          ("Arteria", "Vertebral", True)],
       "pie": "C7: vértebra prominente"},
      {"titulo": "Torácicas", "datos": [
          ("Carillas", "Costales", False), ("Espinosa", "Larga, oblicua", False),
          ("Cuerpo", "Mediano", False)],
       "pie": "Articulan costillas"},
      {"titulo": "Lumbares", "datos": [
          ("Cuerpo", "Grande", False), ("Espinosa", "Cuadrada", False),
          ("Agujero", "Triangular", False)],
       "pie": "Cargan peso"},
      {"titulo": "Sacras", "datos": [
          ("Forma", "Fusionadas", False), ("Agujeros", "Sacros", False),
          ("Número", "Cinco", False)],
       "pie": "Forman el sacro"}]},
  ["La arteria vertebral sube de C6 a C1.",
   "Puede lesionarse en fracturas del agujero.",
   "Infarto de tronco o cerebelo."],
  MOORE)

# CB-154 · radial
V("radial", "CB-154", "sensibilidad-planta-pie-nervio-tibial-plantares", "Sensibilidad del pie",
  "CIENCIAS BÁSICAS ENAM: NERVIOS DEL PIE", CB,
  ("Inervación sensitiva del pie", ["Cada zona depende de un nervio",
   "La planta: nervio tibial y sus ramas plantares"]),
  ("Pregunta de anatomía", ["¿Qué nervio da sensibilidad a la planta?"]),
  {"rotulo": "Mapa del tema", "centro": "PIE", "centro_sub": "Sensibilidad", "ans": 0,
   "items": [("TIBIAL", ["Planta del pie", "Plantar medial y lateral"]),
             ("Safeno", ["Borde medial"]),
             ("Sural", ["Borde lateral"]),
             ("Peroneo superf.", ["Dorso del pie"]),
             ("Peroneo profundo", ["1.er espacio dorsal"])],
   "ruta": ["Planta del pie", "Túnel del tarso", "Nervio tibial", "PLANTARES"]},
  ["Túnel del tarso: parestesias plantares.",
   "Neuropatía diabética: úlcera plantar.",
   "Rama calcánea: talón."],
  MOORE)

# CB-155 · árbol
A("CB-155", "prolactina-dopamina-hipotalamo-inhibicion", "Control de la prolactina",
  "CIENCIAS BÁSICAS ENAM: EJE HIPOTÁLAMO-HIPÓFISIS", CB,
  ("Prolactina", ["Única hormona hipofisaria con control inhibitorio",
   "La dopamina del hipotálamo la frena"]),
  ("Pregunta de fisiología", ["¿Dónde se produce la hormona que", "antagoniza la prolactina?"]),
  Q("¿Qué controla a la célula lactotropa?", [
      L("Inhibe", "DOPAMINA", ["Del hipotálamo", "Núcleo arcuato · receptor D2"], path=True),
      L("Estimula", "TRH", ["Hipotiroidismo: prolactina alta"])], path=True),
  ("Causas de prolactina alta", [("Causa", True), ("Mecanismo", False)], [
      ("Antipsicóticos", ["Bloquean D2", "Menos freno"]),
      ("Sección del tallo", ["No llega dopamina", "Menos freno"])]),
  ["Cabergolina: tratamiento del prolactinoma.",
   "Metoclopramida y domperidona la elevan.",
   "Hiperprolactinemia: amenorrea y galactorrea."],
  GUYTON)

# CB-156 · embudo
V("embudo", "CB-156", "arteria-tibial-posterior-planta-pie-plantares", "Irrigación del pie",
  "CIENCIAS BÁSICAS ENAM: ARTERIAS DEL PIE", CB,
  ("Arterias del pie", ["Tibial posterior: planta",
   "Pedia (tibial anterior): dorso"]),
  ("Pregunta de anatomía", ["¿Qué arteria irriga la planta del pie?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Vasos de la pierna",
   "candidatos": ["Tibial posterior", "Safenas", "Peronea", "Poplítea"],
   "pasos": [("Es una arteria", ["Safenas"]),
             ("Llega a la planta", ["Peronea", "Poplítea"])],
   "final": ("TIBIAL POSTERIOR", ["Plantar medial y lateral", "Pulso tras el maléolo medial"]),
   "nota": "El arco plantar profundo une plantar lateral y pedia."},
  ["Palpar pedio y tibial posterior juntos.",
   "Índice tobillo-brazo < 0,9: isquemia.",
   "Las safenas son venas."],
  MOORE)

# CB-157 · termómetro
V("termometro", "CB-157", "albumina-proteina-mas-abundante-plasma", "Proteínas del plasma",
  "CIENCIAS BÁSICAS ENAM: PROTEÍNAS PLASMÁTICAS", CB,
  ("Proteínas plasmáticas", ["Total 6-8 g/dL",
   "La albúmina aporta cerca del 60 %"]),
  ("Pregunta de bioquímica", ["¿Cuál es la proteína más abundante del suero?"]),
  {"rotulo": "Concentración en sangre",
   "niveles": [("Trazas", "Proteína C", ["Anticoagulante"]),
               ("Baja", "Ceruloplasmina", ["20-40 mg/dL"]),
               ("Media", "Fibrinógeno", ["200-400 mg/dL", "No está en el suero"]),
               ("Máxima", "ALBÚMINA", ["3,5-5 g/dL"])],
   "caso_nivel": 3, "ruta_titulo": "Funciones de la albúmina", "paso_label": "PASO",
   "pasos": [(1, "Presión oncótica", ["Cerca del 80 %"], True),
             (2, "Transporte", ["Bilirrubina, fármacos"], False),
             (3, "Reactante negativo", ["Baja en inflamación"], False)]},
  ["Vida media de unos 20 días.",
   "Baja en cirrosis y síndrome nefrótico.",
   "Hipoalbuminemia: edema."],
  HARPER)

# CB-158 · fases
V("fases", "CB-158", "manchas-bitot-xeroftalmia-deficit-vitamina-a", "Progresión de la xeroftalmía",
  "CIENCIAS BÁSICAS ENAM: VITAMINA A", CB,
  ("Déficit de vitamina A", ["Primero ceguera nocturna",
   "Luego queratinización de conjuntiva y córnea"]),
  ("Pregunta de nutrición", ["¿Qué déficit causa manchas de Bitot?"]),
  {"rotulo": "Etapas del daño ocular", "ans": 1,
   "fases": [("Inicial", "Retina", "Ceguera nocturna", ["Falta rodopsina"]),
             ("Conjuntiva", "Xerosis", "BITOT", ["Placa espumosa", "Temporal"]),
             ("Córnea", "Grave", "Queratomalacia", ["Ceguera"])],
   "chips_titulo": "Vitamina deficiente · marcada la correcta",
   "chips": [("Vitamina A", True), ("Vitamina C", False), ("Vitamina B1", False), ("Vitamina B12", False)]},
  ["Suplemento de vitamina A reduce mortalidad.",
   "Clave en sarampión y diarrea.",
   "Queratomalacia: urgencia."],
  "OMS – Xeroftalmía y ceguera nutricional (2023) · " + NELSON)

# CB-159 · tarjetas
V("tarjetas", "CB-159", "aminoglucosidos-ototoxicidad-nefrotoxicidad", "Toxicidad típica de los antibióticos",
  "CIENCIAS BÁSICAS ENAM: AMINOGLUCÓSIDOS", CB,
  ("Toxicidad de antibióticos", ["Cada grupo tiene un órgano diana",
   "Los aminoglucósidos dañan oído y riñón"]),
  ("Pregunta de farmacología", ["¿Qué grupo produce ototoxicidad?"]),
  {"rotulo": "¿Qué toxicidad?", "ans": 0, "cards": [
      {"titulo": "AMINOGLUCÓSIDOS", "datos": [
          ("Oído", "Ototóxicos", True), ("Riñón", "Nefrotóxicos", True),
          ("Unión NM", "Bloqueo", True)],
       "pie": "Daño auditivo irreversible"},
      {"titulo": "Quinolonas", "datos": [
          ("Tendón", "Rotura", False), ("Corazón", "QT largo", False),
          ("Cartílago", "Niños", False)],
       "pie": "Tendinitis"},
      {"titulo": "Macrólidos", "datos": [
          ("Corazón", "QT largo", False), ("Hígado", "Colestasis", False),
          ("Intestino", "Procinético", False)],
       "pie": "Inhiben CYP3A4"},
      {"titulo": "Tetraciclinas", "datos": [
          ("Dientes", "Tinción", False), ("Piel", "Fotosensible", False),
          ("Esófago", "Úlceras", False)],
       "pie": "Evitar < 8 años"}]},
  ["Dosis única diaria reduce toxicidad.",
   "Medir niveles valle.",
   "Evitar con furosemida o vancomicina."],
  GOODMAN)

# CB-160 · embudo
V("embudo", "CB-160", "astragalo-sin-inserciones-musculares-necrosis", "Hueso sin inserciones musculares",
  "CIENCIAS BÁSICAS ENAM: HUESOS DEL PIE", CB,
  ("Astrágalo (talus)", ["Casi todo cubierto de cartílago articular",
   "No recibe ningún músculo"]),
  ("Pregunta de anatomía", ["¿Qué hueso no tiene inserción muscular?"]),
  {"rotulo": "Embudo anatómico",
   "inicio": "Cinco huesos",
   "candidatos": ["Astrágalo", "Pisiforme", "Cuboides", "Rótula"],
   "pasos": [("Recibe tendón", ["Pisiforme", "Rótula"]),
             ("Recibe fibras musculares", ["Cuboides"])],
   "final": ("ASTRÁGALO", ["Solo superficies articulares", "Irrigación escasa"]),
   "nota": "Pisiforme: flexor cubital del carpo. Calcáneo: tendón de Aquiles."},
  ["Fractura del cuello: necrosis avascular.",
   "Irrigación por el cuello y el seno del tarso.",
   "Articula con tibia, peroné, calcáneo y navicular."],
  MOORE)

# CB-161 · radial
V("radial", "CB-161", "nucleo-fastigio-cerebelo-presion-arterial", "Núcleos profundos del cerebelo",
  "CIENCIAS BÁSICAS ENAM: CEREBELO", CB,
  ("Núcleos del cerebelo", ["Fastigio, globoso, emboliforme y dentado",
   "El fastigio también regula la presión arterial"]),
  ("Pregunta de neuroanatomía", ["¿Qué núcleo regula la presión arterial?"]),
  {"rotulo": "Mapa del tema", "centro": "CEREBELO", "centro_sub": "Núcleos", "ans": 0,
   "items": [("FASTIGIO", ["Equilibrio y postura", "Eleva la presión"]),
             ("Globoso", ["Interpósito"]),
             ("Emboliforme", ["Interpósito"]),
             ("Dentado", ["Movimientos finos"]),
             ("Vermis", ["Proyecta al fastigio"])],
   "ruta": ["Fastigio", "Formación reticular", "Centro vasomotor", "↑ PRESIÓN"]},
  ["Regla: fijo, glorioso, emboló al dentista.",
   "Interpósito: tono de extremidades.",
   "Dentado: pedúnculo cerebeloso superior."],
  "Snell. Neuroanatomía clínica 8.ª ed. (2019)")

# CB-162 · fases
V("fases", "CB-162", "glucogenogenesis-glucosa-udp-glucosa-glucogeno-sintasa", "Síntesis de glucógeno",
  "CIENCIAS BÁSICAS ENAM: GLUCÓGENO", CB,
  ("Glucogenogénesis", ["Empieza con la glucosa que entra a la célula",
   "La UDP-glucosa es la forma activada"]),
  ("Pregunta de bioquímica", ["¿Con qué sustrato comienza?"]),
  {"rotulo": "Pasos de la vía", "ans": 0,
   "fases": [("Inicio", "Hexocinasa", "GLUCOSA", ["Pasa a glucosa-6-P"]),
             ("Activación", "UTP", "UDP-glucosa", ["Vía glucosa-1-P"]),
             ("Unión", "Glucógeno sintasa", "Glucógeno", ["Enlaces α-1,4"])],
   "chips_titulo": "Sustrato inicial · marcado el correcto",
   "chips": [("Glucosa", True), ("Glucosa-6-P", False), ("Glucosa-1-P", False), ("Piruvato", False)]},
  ["La insulina activa la glucógeno sintasa.",
   "La enzima ramificante crea enlaces α-1,6.",
   "No confundir con gluconeogénesis."],
  HARPER)

# CB-163 · matriz
V("matriz", "CB-163", "glucosa-difusion-facilitada-glut-sglt", "Transporte de la glucosa",
  "CIENCIAS BÁSICAS ENAM: TRANSPORTE DE MEMBRANA", CB,
  ("Transporte de glucosa", ["La mayoría de células: GLUT, sin energía",
   "Intestino y riñón: SGLT con sodio"]),
  ("Pregunta de fisiología", ["¿Cómo entra la glucosa en la mayoría", "de las células?"]),
  {"rotulo": "Transportador y tipo", "eje_x": "Rasgo", "eje_y": "Sitio",
   "cols": ["Transportador", "Mecanismo"], "rows": ["Mayoría", "Músculo, grasa", "Intestino, riñón"], "caso": (0, 1),
   "cells": [[("GLUT1, 2, 3", []), ("DIFUSIÓN FACILITADA", ["A favor de gradiente"])],
             [("GLUT4", ["Depende de insulina"]), ("Difusión facilitada", [])],
             [("SGLT1 y 2", []), ("Activo secundario", ["Con sodio"])]]},
  ["Gliflozinas: inhiben SGLT2.",
   "GLUT2: hígado y célula beta.",
   "GLUT3: neuronas."],
  GUYTON)

# CB-164 · radial
V("radial", "CB-164", "melanina-melanocitos-tirosinasa-color-piel", "Color de la piel",
  "CIENCIAS BÁSICAS ENAM: PIGMENTACIÓN", CB,
  ("Pigmentación cutánea", ["La melanina da color a piel, pelo y ojos",
   "La producen los melanocitos de la capa basal"]),
  ("Pregunta de histología", ["¿Qué sustancia da color a la piel?"]),
  {"rotulo": "Mapa del tema", "centro": "MELANINA", "centro_sub": "Pigmento", "ans": 0,
   "items": [("MELANOCITO", ["Capa basal", "Tirosinasa"]),
             ("Precursor", ["Tirosina"]),
             ("Tipos", ["Eumelanina", "Feomelanina"]),
             ("Función", ["Protege del UV"]),
             ("Albinismo", ["Falta tirosinasa"])],
   "ruta": ["Tirosina", "Tirosinasa", "Melanosoma", "MELANINA"]},
  ["El número de melanocitos es similar entre razas.",
   "Vitíligo: destrucción de melanocitos.",
   "Queratina: proteína estructural."],
  ROSS)

# CB-165 · embudo
V("embudo", "CB-165", "blastomyces-dermatitidis-micosis-sistemica", "Micosis sistémicas",
  "CIENCIAS BÁSICAS ENAM: MICOLOGÍA", CB,
  ("Micosis según profundidad", ["Superficiales, cutáneas, subcutáneas",
   "Sistémicas: hongos dimórficos inhalados"]),
  ("Pregunta de microbiología", ["¿Qué hongo actúa de forma sistémica?"]),
  {"rotulo": "Embudo micológico",
   "inicio": "Cinco hongos",
   "candidatos": ["Blastomyces", "Sporothrix", "Malassezia", "Trichophyton"],
   "pasos": [("No es superficial ni cutáneo", ["Malassezia", "Trichophyton"]),
             ("Llega por inhalación", ["Sporothrix"])],
   "final": ("BLASTOMYCES DERMATITIDIS", ["Dimórfico, levadura de base ancha", "Pulmón, piel y hueso"]),
   "nota": "Sporothrix: subcutánea linfangítica (jardinería)."},
  ["Otras sistémicas: histoplasma, paracoccidioides.",
   "Malassezia: pitiriasis versicolor.",
   "Dermatofitos: tiñas."],
  MURRAY)

# CB-166 · árbol
A("CB-166", "sintesis-arn-ribonucleotidos-trifosfato-arn-polimerasa", "Sustratos de la síntesis de ácidos nucleicos",
  "CIENCIAS BÁSICAS ENAM: BIOLOGÍA MOLECULAR", CB,
  ("Polimerasas", ["Usan nucleótidos trifosfato",
   "Liberan pirofosfato como energía"]),
  ("Pregunta de bioquímica", ["¿Cuál es el precursor del ARN?"]),
  Q("¿Qué ácido nucleico se sintetiza?", [
      L("ARN", "RIBONUCLEÓTIDOS TRIFOSFATO", ["ATP, GTP, CTP, UTP", "No necesita cebador"], path=True),
      L("ADN", "Desoxirribonucleótidos TP", ["Con timina", "Necesita cebador"])], path=True),
  ("ARN polimerasa II", [("Rasgo", True), ("Dato", False)], [
      ("Produce", ["ARN mensajero", "En el núcleo"]),
      ("Inhibidor", ["Alfa-amanitina", "Seta Amanita"])]),
  ["Queda como monofosfato dentro de la cadena.",
   "Uracilo en el ARN, timina en el ADN.",
   "Amanita phalloides: hepatotoxicidad grave."],
  HARPER)

# CB-167 · fases
V("fases", "CB-167", "vitamina-b12-factor-intrinseco-ileon-terminal", "Absorción de la vitamina B12",
  "CIENCIAS BÁSICAS ENAM: VITAMINA B12", CB,
  ("Vitamina B12", ["Necesita factor intrínseco",
   "Se absorbe en el íleon terminal"]),
  ("Pregunta de fisiología", ["¿Dónde se absorbe la vitamina B12?"]),
  {"rotulo": "Recorrido de la B12", "ans": 2,
   "fases": [("Estómago", "Ácido, pepsina", "Haptocorrina", ["Factor intrínseco"]),
             ("Duodeno", "Proteasas", "B12 + FI", ["Se libera"]),
             ("Íleon terminal", "Cubilina", "ABSORCIÓN", ["Transcobalamina II"])],
   "chips_titulo": "Sitio · marcado el correcto",
   "chips": [("Íleon", True), ("Duodeno", False), ("Yeyuno", False), ("Estómago", False)]},
  ["Anemia perniciosa: falta factor intrínseco.",
   "Resección ileal y Crohn: déficit.",
   "Reservas hepáticas para 3-5 años."],
  GUYTON)

# CB-168 · tarjetas
V("tarjetas", "CB-168", "linfoma-burkitt-epstein-barr-c-myc", "Virus asociados a cáncer",
  "CIENCIAS BÁSICAS ENAM: VIRUS ONCOGÉNICOS", CB,
  ("Virus y cáncer", ["Algunos virus causan tumores específicos",
   "El VEB se asocia al linfoma de Burkitt"]),
  ("Pregunta de microbiología", ["¿Qué virus causa el linfoma de Burkitt?"]),
  {"rotulo": "¿Qué tumor causa?", "ans": 0, "cards": [
      {"titulo": "EPSTEIN-BARR", "datos": [
          ("Tumor", "Burkitt", True), ("Otro", "Nasofaringe", True),
          ("Genética", "t(8;14)", True)],
       "pie": "Burkitt endémico africano"},
      {"titulo": "Herpesvirus 8", "datos": [
          ("Tumor", "Kaposi", False), ("Otro", "Linfoma de cavidades", False),
          ("Grupo", "VIH", False)],
       "pie": "HHV-8"},
      {"titulo": "VPH 16 y 18", "datos": [
          ("Tumor", "Cuello uterino", False), ("Otro", "Ano, orofaringe", False),
          ("Proteínas", "E6, E7", False)],
       "pie": "Vacuna disponible"},
      {"titulo": "HTLV-1", "datos": [
          ("Tumor", "Leucemia T", False), ("Otro", "Paraparesia", False),
          ("Zona", "Andes, Japón", False)],
       "pie": "Retrovirus"}]},
  ["Burkitt: imagen en cielo estrellado.",
   "Ki-67 cercano al 100 %.",
   "VEB también en Hodgkin."],
  MURRAY + " · " + ROBBINS)

# CB-169 · termómetro
V("termometro", "CB-169", "nodo-auriculoventricular-segundo-marcapasos-40-60", "Jerarquía de los marcapasos",
  "CIENCIAS BÁSICAS ENAM: CONDUCCIÓN CARDÍACA", CB,
  ("Automatismo cardíaco", ["El más rápido manda",
   "Si falla, toma el mando el siguiente"]),
  ("Pregunta de fisiología", ["¿Cuál es el segundo marcapasos?"]),
  {"rotulo": "Frecuencia intrínseca",
   "niveles": [("20-40 lpm", "Purkinje", ["QRS ancho"]),
               ("30-40 lpm", "Haz de His", ["Escape infranodal"]),
               ("40-60 lpm", "NODO AV", ["Segundo marcapasos"]),
               ("60-100 lpm", "Nodo sinusal", ["Principal"])],
   "caso_nivel": 2, "ruta_titulo": "Función del nodo AV", "paso_label": "PASO",
   "pasos": [(1, "Retrasa 0,1 s", ["Aurículas se vacían"], True),
             (2, "Ritmo de unión", ["QRS estrecho"], True),
             (3, "Filtra impulsos", ["En fibrilación auricular"], False)]},
  ["Bloqueo AV completo: escape lento.",
   "Escape bajo: QRS ancho y peor pronóstico.",
   "Irrigado por la coronaria derecha."],
  GUYTON)

# CB-170 · árbol
A("CB-170", "glucosa-glomerulo-ultrafiltracion-sglt2-proximal", "La glucosa en la nefrona",
  "CIENCIAS BÁSICAS ENAM: FILTRACIÓN GLOMERULAR", CB,
  ("Manejo renal de la glucosa", ["Se filtra libremente en el glomérulo",
   "Se reabsorbe en el túbulo proximal"]),
  ("Pregunta de fisiología", ["¿Cómo pasa la glucosa al espacio de Bowman?"]),
  Q("¿En qué segmento?", [
      L("Glomérulo", "ULTRAFILTRACIÓN", ["Presión hidrostática", "Molécula pequeña"], path=True),
      L("Túbulo proximal", "Reabsorción", ["SGLT2 y SGLT1", "Activo secundario"])], path=True),
  ("Umbral renal", [("Glucemia", True), ("Orina", False)], [
      ("< 180 mg/dL", ["Normal", "Sin glucosa"]),
      ("> 180 mg/dL", ["SGLT saturado", "Glucosuria"])]),
  ["Concentración en el filtrado = plasma.",
   "Embarazo: umbral más bajo.",
   "Gliflozinas: glucosuria terapéutica."],
  GUYTON)

# CB-171 · puntaje
V("puntaje", "CB-171", "reabsorcion-agua-tubulo-proximal-65-por-ciento", "Reabsorción de agua en la nefrona",
  "CIENCIAS BÁSICAS ENAM: REABSORCIÓN TUBULAR", CB,
  ("Reabsorción de agua", ["El proximal reabsorbe dos tercios",
   "El colector hace el ajuste fino con ADH"]),
  ("Pregunta de fisiología", ["¿Dónde se reabsorbe la mayor parte del agua?"]),
  {"rotulo": "Porcentaje reabsorbido", "escala": "%", "total": 65, "max": 100,
   "total_label": "Túbulo proximal",
   "interpreta": "Mayor reabsorción",
   "items": [("Túbulo proximal", "65 %", True), ("Asa descendente", "15 %", False),
             ("Distal y colector", "Variable", False)],
   "bandas": [("65 %", "Proximal", "Isosmótico", True),
              ("15 %", "Asa", "Rama descendente", False),
              ("Resto", "Colector", "Depende de ADH", False)]},
  ["Rama ascendente: impermeable al agua.",
   "Acuaporina 1 en el proximal.",
   "Acuaporina 2 en el colector con ADH."],
  GUYTON)

# CB-172 · embudo
V("embudo", "CB-172", "kala-azar-leishmania-donovani-esplenomegalia", "Agente del kala-azar",
  "CIENCIAS BÁSICAS ENAM: LEISHMANIASIS VISCERAL", CB,
  ("Kala-azar", ["Leishmaniasis visceral",
   "Fiebre, esplenomegalia masiva y pancitopenia"]),
  ("Pregunta de parasitología", ["¿Cuál es el agente causal?"]),
  {"rotulo": "Embudo parasitológico",
   "inicio": "Fiebre con esplenomegalia",
   "candidatos": ["Leishmania", "Plasmodium", "Tripanosoma", "Lutzomyia"],
   "pasos": [("Es un parásito, no un vector", ["Lutzomyia"]),
             ("Amastigotes en macrófagos", ["Plasmodium", "Tripanosoma"])],
   "final": ("LEISHMANIA", ["L. donovani o L. infantum", "Transmite el flebótomo"]),
   "nota": "Lutzomyia es el vector en América, no el agente."},
  ["Diagnóstico: aspirado de médula o bazo.",
   "Prueba rápida rK39.",
   "Tratamiento: anfotericina B liposomal."],
  BOTERO)
