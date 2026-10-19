"""Ciencias Básicas · parte H (CB-373 a CB-412)."""
from ccb import FCB, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER
from refcb import *

CB = "CIENCIAS BÁSICAS"

# CB-373 · puntaje
V("puntaje", "CB-373", "testosterona-fetal-leydig-semana-7-8-hcg", "Inicio de la testosterona fetal",
  "CIENCIAS BÁSICAS ENAM: GÓNADA FETAL", CB,
  ("Testículo fetal", ["SRY en la semana 6 forma el testículo",
   "Leydig produce testosterona desde la semana 7-8"]),
  ("Pregunta de embriología", ["¿Desde qué semana se produce testosterona?"]),
  {"rotulo": "Semanas de gestación", "escala": "Semana", "total": 7, "max": 40,
   "total_label": "Inicio",
   "interpreta": "Semana 7-8",
   "items": [("SRY activo", "Sem. 6", False), ("Testosterona", "Sem. 7-8", True), ("Pico", "Sem. 12-14", False)],
   "bandas": [("6", "SRY", "Gónada a testículo", False),
              ("7-8", "Leydig", "Inicia testosterona", True),
              ("12-14", "Pico", "Estímulo de hCG", False)]},
  ["Primero la estimula la hCG placentaria.",
   "Luego la LH fetal.",
   "Sertoli: hormona antimülleriana."],
  LANGMAN)

# CB-374 · matriz
V("matriz", "CB-374", "circulacion-fetal-cortocircuitos-derecha-izquierda", "Cortocircuitos fetales",
  "CIENCIAS BÁSICAS ENAM: CIRCULACIÓN FETAL", CB,
  ("Circulación fetal", ["Pulmón sin aire: resistencia muy alta",
   "La sangre evita el pulmón por tres cortocircuitos"]),
  ("Pregunta de fisiología", ["¿Qué afirmación es incorrecta?"]),
  {"rotulo": "Cortocircuito y dirección", "eje_x": "Dato", "eje_y": "Shunt",
   "cols": ["Conecta", "Dirección"], "rows": ["Foramen oval", "Conducto arterioso", "Conducto venoso"], "caso": (0, 1),
   "cells": [[("AD → AI", []), ("DER → IZQ", ["No izq → der"])],
             [("Pulmonar → aorta", []), ("Der → izq", [])],
             [("Umbilical → cava", []), ("Evita el hígado", [])]]},
  ["PaO2 fetal: 25-40 mmHg.",
   "Ventrículo derecho: 60-65 % del gasto.",
   "Al nacer, los shunts se cierran."],
  GUYTON)

# CB-375 · termómetro
V("termometro", "CB-375", "fecundacion-pronucleos-femenino-masculino", "Del gameto al embrión",
  "CIENCIAS BÁSICAS ENAM: FECUNDACIÓN", CB,
  ("Fecundación", ["Termina con la formación del cigoto",
   "Los pronúcleos se forman en esta etapa"]),
  ("Pregunta de embriología", ["¿Cuándo se forman los pronúcleos?"]),
  {"rotulo": "Etapas en orden",
   "niveles": [("Gametogénesis", "Antes", ["Óvulo y espermatozoide"]),
               ("Fecundación", "Ampolla", ["PRONÚCLEOS"]),
               ("Segmentación", "Días 1-3", ["Blastómeros"]),
               ("Gastrulación", "Semana 3", ["Tres capas"])],
   "caso_nivel": 1, "ruta_titulo": "Qué pasa en la fecundación", "paso_label": "PASO",
   "pasos": [(1, "Termina meiosis II", ["2.º corpúsculo polar"], False),
             (2, "Pronúcleos", ["Femenino y masculino"], True),
             (3, "Se unen", ["Cigoto diploide"], False)]},
  ["Sexo genético al fecundar.",
   "Ocurre en la ampolla de la trompa.",
   "Luego empieza la segmentación."],
  LANGMAN)

# CB-376 · termómetro
V("termometro", "CB-376", "pulmon-fetal-canalicular-surfactante-20-24-semanas", "Etapas del desarrollo pulmonar",
  "CIENCIAS BÁSICAS ENAM: MADURACIÓN PULMONAR", CB,
  ("Pulmón fetal", ["Cinco etapas",
   "Surfactante desde las semanas 20-24"]),
  ("Pregunta de embriología", ["¿Cuándo aparecen alvéolos primitivos", "y surfactante?"]),
  {"rotulo": "Etapas pulmonares",
   "niveles": [("Seudoglandular", "Sem. 5-17", ["Bronquios"]),
               ("Canalicular", "Sem. 16-26", ["SEMANAS 20-24", "Neumocitos II"]),
               ("Sacular", "Sem. 24-36", ["Más surfactante"]),
               ("Alveolar", "Sem. 36-8 años", ["Alvéolos maduros"])],
   "caso_nivel": 1, "ruta_titulo": "Utilidad clínica", "paso_label": "PASO",
   "pasos": [(1, "Viabilidad", ["23-24 semanas"], True),
             (2, "Corticoides", ["24-34 semanas"], False),
             (3, "Membrana hialina", ["Si falta surfactante"], False)]},
  ["Betametasona acelera el surfactante.",
   "Lecitina/esfingomielina > 2: madurez.",
   "Etapa embrionaria: brote pulmonar."],
  LANGMAN)

# CB-377 · árbol
A("CB-377", "agenesia-conducto-wolff-rinon-ureter-vesicula-seminal", "Funciones del conducto de Wolff",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA URINARIA", CB,
  ("Conducto mesonéfrico", ["Emite el brote ureteral",
   "En el varón forma la vía seminal"]),
  ("Varón con agenesia de un conducto de Wolff", ["¿Qué falta en ese lado?"]),
  Q("¿Qué forma el conducto de Wolff?", [
      L("Brote ureteral", "RIÑÓN Y URÉTER", ["Induce el metanefros"], path=True),
      L("Vía seminal", "VESÍCULA SEMINAL", ["Y deferente"], path=True)], path=True),
  ("Hallazgos asociados", [("Sexo", True), ("Buscar", False)], [
      ("Varón", ["Agenesia renal", "Vesícula y deferente"]),
      ("Mujer", ["Agenesia renal", "Malformación mülleriana"])]),
  ["Sin brote ureteral no hay riñón.",
   "Por eso falta todo en un lado.",
   "Ecografía renal en estos casos."],
  LANGMAN)

# CB-378 · embudo
V("embudo", "CB-378", "madurez-fetal-pulmon-surfactante-organo-limitante", "Órgano que define la madurez fetal",
  "CIENCIAS BÁSICAS ENAM: MADUREZ FETAL", CB,
  ("Madurez fetal", ["El feto está maduro si puede respirar",
   "El pulmón es el órgano limitante"]),
  ("Pregunta de obstetricia básica", ["¿Qué órgano define la madurez?"]),
  {"rotulo": "Embudo fisiológico",
   "inicio": "Órganos fetales",
   "candidatos": ["Pulmones", "Sistema nervioso", "Hígado", "Riñones"],
   "pasos": [("Pueden madurar tras nacer", ["Sistema nervioso", "Hígado"]),
             ("Ya funciona en el útero", ["Riñones"])],
   "final": ("PULMONES", ["Sacos alveolares y surfactante", "Membrana hialina si faltan"]),
   "nota": "Corticoides prenatales: 24-34 semanas."},
  ["Principal causa de muerte del prematuro.",
   "Surfactante evita el colapso alveolar.",
   "Test de L/E en líquido amniótico."],
  "Williams Obstetrics 26.ª ed. (2022)")

# CB-379 · termómetro
V("termometro", "CB-379", "metanefros-rinon-definitivo-quinta-semana", "Sistemas renales del embrión",
  "CIENCIAS BÁSICAS ENAM: EMBRIOLOGÍA RENAL", CB,
  ("Tres sistemas renales", ["Pronefros, mesonefros y metanefros",
   "Solo el metanefros queda"]),
  ("Pregunta de embriología", ["¿Cuándo aparece el riñón definitivo?"]),
  {"rotulo": "Orden de aparición",
   "niveles": [("Pronefros", "Semana 4", ["No funciona"]),
               ("Mesonefros", "Semanas 4-8", ["Transitorio"]),
               ("Metanefros", "SEMANA 5", ["Riñón definitivo"]),
               ("Orina", "Semana 10-12", ["Líquido amniótico"])],
   "caso_nivel": 2, "ruta_titulo": "Cómo se forma", "paso_label": "PASO",
   "pasos": [(1, "Brote ureteral", ["Del conducto de Wolff"], True),
             (2, "Blastema", ["Metanéfrico"], False),
             (3, "Nefronas", ["Inducción recíproca"], False)]},
  ["Agenesia bilateral: secuencia de Potter.",
   "Oligohidramnios e hipoplasia pulmonar.",
   "Mesonefros deja el conducto de Wolff."],
  LANGMAN)

# CB-380 · tarjetas
V("tarjetas", "CB-380", "sindrome-patau-trisomia-13-holoprosencefalia", "Trisomías y síndromes",
  "CIENCIAS BÁSICAS ENAM: CROMOSOMOPATÍAS", CB,
  ("Aneuploidías frecuentes", ["Cada síndrome tiene su cariotipo",
   "Patau corresponde a la trisomía 13"]),
  ("Recién nacido con síndrome de Patau", ["¿Qué anomalía cromosómica tiene?"]),
  {"rotulo": "¿Qué cariotipo?", "ans": 0, "cards": [
      {"titulo": "TRISOMÍA 13", "datos": [
          ("Síndrome", "Patau", True), ("Clave", "Línea media", True),
          ("Signos", "Polidactilia", True)],
       "pie": "Holoprosencefalia, labio hendido"},
      {"titulo": "Trisomía 18", "datos": [
          ("Síndrome", "Edwards", False), ("Clave", "Puños cerrados", False),
          ("Pies", "En mecedora", False)],
       "pie": "Occipucio prominente"},
      {"titulo": "Trisomía 21", "datos": [
          ("Síndrome", "Down", False), ("Clave", "Hipotonía", False),
          ("Corazón", "Canal AV", False)],
       "pie": "La más frecuente"},
      {"titulo": "Monosomía X", "datos": [
          ("Síndrome", "Turner", False), ("Clave", "Talla baja", False),
          ("Corazón", "Coartación", False)],
       "pie": "47,XXY: Klinefelter"}]},
  ["> 80 % de Patau muere antes del año.",
   "Aplasia cutis en el cuero cabelludo.",
   "Riñones poliquísticos."],
  "Thompson & Thompson. Genética en medicina 8.ª ed. (2016)")

# CB-381 · embudo
V("embudo", "CB-381", "polidactilia-onfalocele-hipotonia-retraso-patau", "Síndrome con polidactilia y onfalocele",
  "CIENCIAS BÁSICAS ENAM: SÍNDROMES GENÉTICOS", CB,
  ("Síndromes cromosómicos", ["Patau: defectos de la línea media",
   "Polidactilia y onfalocele"]),
  ("Pregunta de genética", ["Retraso, polidactilia, pie valgo", "Onfalocele e hipotonía"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Cinco síndromes",
   "candidatos": ["Patau", "Edwards", "Down", "Turner"],
   "pasos": [("Defectos múltiples graves", ["Turner"]),
             ("Polidactilia con hipotonía", ["Edwards", "Down"])],
   "final": ("PATAU (TRISOMÍA 13)", ["Polidactilia postaxial", "Onfalocele, holoprosencefalia"]),
   "nota": "Edwards: hipertonía y dedos cabalgados."},
  ["Down: hipotonía sin polidactilia.",
   "Klinefelter: sin malformaciones graves.",
   "Tamizaje del primer trimestre."],
  NELSON)

# CB-382 · puntaje
V("puntaje", "CB-382", "vida-media-50-por-ciento-concentracion-plasmatica", "Vida media de un fármaco",
  "CIENCIAS BÁSICAS ENAM: FARMACOCINÉTICA", CB,
  ("Vida media (t½)", ["Tiempo para que la concentración baje a la mitad",
   "t½ = 0,693 × Vd / aclaramiento"]),
  ("Pregunta de farmacología", ["¿Cómo se llama el tiempo para reducir al 50 %?"]),
  {"rotulo": "Concentración que queda", "escala": "%", "total": 50, "max": 100,
   "total_label": "Tras 1 vida media",
   "interpreta": "Vida media",
   "items": [("1 vida media", "50 %", True), ("2 vidas medias", "25 %", False), ("4-5 vidas medias", "≈ 3-6 %", False)],
   "bandas": [("1 t½", "50 %", "Definición", True),
              ("4-5 t½", "Equilibrio", "Con dosis repetidas", False),
              ("4-5 t½", "Eliminado", "Al suspender", False)]},
  ["Vida media larga: dosis de carga.",
   "Amiodarona, digoxina.",
   "Ventana terapéutica: eficaz a tóxica."],
  KATZUNG)

# CB-383 · matriz
V("matriz", "CB-383", "fenitoina-inductor-enzimatico-valproato-inhibidor", "Inductores e inhibidores enzimáticos",
  "CIENCIAS BÁSICAS ENAM: INTERACCIONES", CB,
  ("Citocromo P450", ["Inductores: bajan los niveles de otros fármacos",
   "Inhibidores: los suben"]),
  ("Pregunta de farmacología", ["¿Qué fármaco es inductor enzimático?"]),
  {"rotulo": "Efecto sobre el P450", "eje_x": "Efecto", "eje_y": "Fármaco",
   "cols": ["Tipo", "Consecuencia"], "rows": ["Fenitoína", "Valproato", "Gabapentina"], "caso": (0, 0),
   "cells": [[("INDUCTOR", ["CYP3A4, CYP2C"]), ("Baja anticonceptivos", ["Warfarina"])],
             [("Inhibidor", []), ("Sube lamotrigina", [])],
             [("Ninguno", ["No se metaboliza"]), ("Pocas interacciones", [])]]},
  ["Inductores: carbamazepina, rifampicina.",
   "Fenobarbital y hierba de San Juan.",
   "Fenitoína: osteomalacia por vitamina D."],
  GOODMAN)

# CB-384 · radial
V("radial", "CB-384", "union-neuromuscular-acetilcolina-receptor-nicotinico", "Unión neuromuscular",
  "CIENCIAS BÁSICAS ENAM: PLACA MOTORA", CB,
  ("Unión neuromuscular", ["Único neurotransmisor: acetilcolina",
   "Receptor nicotínico de la placa"]),
  ("Pregunta de fisiología", ["¿Qué neurotransmisor actúa en la unión", "neuromuscular?"]),
  {"rotulo": "Mapa del tema", "centro": "PLACA", "centro_sub": "Motora", "ans": 0,
   "items": [("ACETILCOLINA", ["Único transmisor"]),
             ("Miastenia", ["Anticuerpos contra", "el receptor"]),
             ("Lambert-Eaton", ["Canales de calcio"]),
             ("Botulínica", ["Bloquea liberación"]),
             ("Relajantes", ["Rocuronio, succinil."])],
   "ruta": ["Potencial", "Entra calcio", "Libera ACh", "PLACA"]},
  ["Acetilcolinesterasa la degrada.",
   "Piridostigmina en miastenia.",
   "Nicotínico: canal iónico."],
  GUYTON)

# CB-385 · termómetro
V("termometro", "CB-385", "cefuroxima-cefepima-ceftazidima-cefadroxilo-generaciones", "Generaciones de cefalosporinas",
  "CIENCIAS BÁSICAS ENAM: CEFALOSPORINAS", CB,
  ("Cefalosporinas", ["Más generación: más gramnegativos",
   "La 4.ª cubre también Pseudomonas"]),
  ("Pregunta de farmacología", ["Relacionar 4 fármacos con su generación"]),
  {"rotulo": "Generación",
   "niveles": [("1.ª", "Cefadroxilo (d-1)", ["Grampositivos"]),
               ("2.ª", "Cefuroxima (a-2)", ["H. influenzae"]),
               ("3.ª", "Ceftazidima (c-3)", ["Pseudomonas"]),
               ("4.ª", "Cefepima (b-4)", ["Amplio espectro"])],
   "caso_nivel": 3, "ruta_titulo": "Combinación", "paso_label": "PAR",
   "pasos": [(1, "a-2 · b-4", ["Cefuroxima, cefepima"], True),
             (2, "c-3 · d-1", ["Ceftazidima, cefadroxilo"], True),
             (3, "5.ª generación", ["Ceftarolina: SARM"], False)]},
  ["Cefoxitina: cefamicina de 2.ª.",
   "Ceftriaxona: no cubre Pseudomonas.",
   "Cefazolina: profilaxis."],
  SANFORD)

# CB-386 · embudo
V("embudo", "CB-386", "colestasis-farmacos-clorpromazina-paracetamol-hepatocelular", "Fármacos y colestasis",
  "CIENCIAS BÁSICAS ENAM: DAÑO HEPÁTICO POR FÁRMACOS", CB,
  ("Hepatotoxicidad por fármacos", ["Colestásica: FA y GGT altas",
   "Hepatocelular: transaminasas muy altas"]),
  ("Pregunta de farmacología", ["¿Cuál no causa colestasis intrahepática?"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco fármacos",
   "candidatos": ["Paracetamol", "Clorpromazina", "Carbamazepina", "Anovulatorios"],
   "pasos": [("Clásicos colestásicos", ["Clorpromazina", "Anovulatorios"]),
             ("También colestásico", ["Carbamazepina"])],
   "final": ("PARACETAMOL", ["Daño hepatocelular", "Necrosis centrolobulillar"]),
   "nota": "Nifedipina y amoxi-clavulánico también pueden dar colestasis."},
  ["Índice R: tipo de daño.",
   "Eritromicina estolato: colestasis.",
   "NAPQI en la sobredosis."],
  HARRISON)

# CB-387 · embudo
V("embudo", "CB-387", "cefoxitina-bacteroides-fragilis-cefamicina", "Cefalosporina contra anaerobios",
  "CIENCIAS BÁSICAS ENAM: CEFAMICINAS", CB,
  ("Cefamicinas", ["Cefoxitina y cefotetán",
   "Resisten betalactamasas de Bacteroides"]),
  ("Pregunta de farmacología", ["¿Qué cefalosporina actúa contra B. fragilis?"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco cefalosporinas",
   "candidatos": ["Cefoxitina", "Cefalotina", "Cefuroxima", "Ceftriaxona"],
   "pasos": [("Resiste betalactamasas", ["Cefalotina", "Cefuroxima"]),
             ("Tiene grupo metoxi", ["Ceftriaxona"])],
   "final": ("CEFOXITINA", ["Cefamicina activa contra anaerobios", "Profilaxis colorrectal"]),
   "nota": "Resistencia de B. fragilis en aumento."},
  ["Alternativas: metronidazol, carbapenémicos.",
   "Cefotaxima: poca acción anaerobia.",
   "Infecciones pélvicas leves."],
  SANFORD)

# CB-388 · árbol
A("CB-388", "polimixina-membrana-no-sintesis-proteica", "Sitio de acción de los antibióticos",
  "CIENCIAS BÁSICAS ENAM: MECANISMOS ANTIBIÓTICOS", CB,
  ("Blancos antibióticos", ["Pared, membrana, ribosoma, ácidos nucleicos",
   "Las polimixinas rompen la membrana"]),
  ("Pregunta de farmacología", ["¿Cuál no inhibe la síntesis de proteínas?"]),
  Q("¿Actúa en el ribosoma?", [
      L("No", "POLIMIXINA", ["Membrana celular", "Detergente catiónico"], path=True),
      Q("¿Qué subunidad?", [
          L("30S", "Aminoglucósidos", ["Tetraciclinas"]),
          L("50S", "Macrólidos", ["Clindamicina"])], edge="Sí")], path=True),
  ("Uso de polimixinas", [("Dato", True), ("Detalle", False)], [
      ("Indicación", ["Último recurso", "Gramnegativos MDR"]),
      ("Toxicidad", ["Riñón", "Neurotoxicidad"])]),
  ["Colistina: polimixina E.",
   "Acinetobacter y KPC.",
   "30S: aminoglucósidos y tetraciclinas."],
  GOODMAN)

# CB-389 · puntaje
V("puntaje", "CB-389", "lepra-lepromatosa-dapsona-rifampicina-clofazimina", "Esquema de la lepra multibacilar",
  "CIENCIAS BÁSICAS ENAM: LEPRA", CB,
  ("Lepra multibacilar", ["Siempre terapia combinada",
   "Rifampicina: la más bactericida"]),
  ("Pregunta de farmacología", ["¿Con qué se asocia la dapsona", "para evitar resistencia?"]),
  {"rotulo": "Esquema OMS", "escala": "Meses", "total": 12, "max": 12,
   "total_label": "Duración",
   "interpreta": "Rifampicina + dapsona + clofazimina",
   "items": [("Rifampicina", "600 mg/mes", True), ("Dapsona", "100 mg/día", True), ("Clofazimina", "Mes y día", True)],
   "bandas": [("6", "Paucibacilar", "Mismo esquema", False),
              ("12", "Multibacilar", "Lepromatosa", True),
              ("1 dosis", "Rifampicina", "Mata > 99 %", False)]},
  ["Dapsona: hemólisis en déficit de G6PD.",
   "Clofazimina tiñe la piel.",
   "Igual que TBC: combinar."],
  "OMS – Guía de lepra (2018)")

# CB-390 · árbol
A("CB-390", "quemado-tercer-grado-pseudomonas-ceftazidima", "Antibiótico en quemado con Pseudomonas",
  "CIENCIAS BÁSICAS ENAM: INFECCIÓN EN QUEMADOS", CB,
  ("Quemaduras e infección", ["La escara húmeda favorece Pseudomonas",
   "Puede dar sepsis"]),
  ("Paciente con quemaduras de tercer grado", ["Fiebre persistente", "Cultivo: Pseudomonas aeruginosa"]),
  Q("¿Cubre Pseudomonas?", [
      L("Sí", "CEFTAZIDIMA", ["3.ª generación", "Más aminoglucósido si es grave"], path=True),
      L("No", "Otras cefalosporinas", ["Cefaclor, cefalotina", "Cefoxitina, cefuroxima"])], path=True),
  ("Además del antibiótico", [("Medida", True), ("Motivo", False)], [
      ("Desbridar", ["Escara", "Foco infectado"]),
      ("Cultivos", ["Seriados", "Ajustar"])]),
  ["Ectima gangrenoso.",
   "Alternativas: cefepime, pip-tazo.",
   "Carbapenémicos en cepas resistentes."],
  SANFORD)

# CB-391 · árbol
A("CB-391", "anafilaxia-penicilina-pseudomonas-aztreonam", "Antibiótico en alergia grave a penicilina",
  "CIENCIAS BÁSICAS ENAM: ALERGIA A BETALACTÁMICOS", CB,
  ("Alergia a penicilina", ["Las penicilinas quedan prohibidas",
   "El aztreonam casi no tiene reacción cruzada"]),
  ("Paciente con anafilaxia previa por penicilina", ["Infección grave por Pseudomonas"]),
  Q("¿Hubo anafilaxia a penicilina?", [
      L("Sí", "AZTREONAM", ["Monobactámico", "Cubre Pseudomonas"], path=True),
      L("No", "Betalactámico", ["Pip-tazo, ceftazidima"])], path=True),
  ("Cuidado", [("Fármaco", True), ("Riesgo", False)], [
      ("Ceftazidima", ["Misma cadena", "Cruce con aztreonam"]),
      ("Carbapenémicos", ["Cruce bajo", "Evitar si anafilaxia"])]),
  ["Aztreonam no cubre grampositivos.",
   "Ni anaerobios.",
   "Combinar según el foco."],
  SANFORD)

# CB-392 · embudo
V("embudo", "CB-392", "infeccion-abdominal-nosocomial-piperacilina-tazobactam", "Cobertura intraabdominal nosocomial",
  "CIENCIAS BÁSICAS ENAM: INFECCIÓN INTRAABDOMINAL", CB,
  ("Infección intraabdominal nosocomial", ["Cubrir enterobacterias, Pseudomonas",
   "y anaerobios"]),
  ("Paciente inmunosuprimido", ["Infección abdominal grave hospitalaria", "Sospecha de Pseudomonas y anaerobios"]),
  {"rotulo": "Embudo de esquemas",
   "inicio": "Cinco esquemas",
   "candidatos": ["Pip-tazo", "Amp-sulbactam", "Aztreonam + amikacina", "Ceftriaxona + clinda"],
   "pasos": [("Cubre Pseudomonas", ["Amp-sulbactam", "Ceftriaxona + clinda"]),
             ("Cubre anaerobios", ["Aztreonam + amikacina"])],
   "final": ("PIPERACILINA-TAZOBACTAM", ["Cubre los tres grupos", "Con control del foco"]),
   "nota": "Alternativa: imipenem o meropenem."},
  ["Drenaje o cirugía del foco.",
   "Ajustar según cultivos.",
   "Amikacina + penicilina: mala en abscesos."],
  "IDSA – Intra-abdominal infections (2010) · " + SANFORD)

# CB-393 · matriz
V("matriz", "CB-393", "claritromicina-no-actua-pared-ribosoma-50s", "Antibióticos según su blanco",
  "CIENCIAS BÁSICAS ENAM: MACRÓLIDOS", CB,
  ("Blancos antibióticos", ["Pared: betalactámicos, vancomicina",
   "Ribosoma: macrólidos"]),
  ("Pregunta de farmacología", ["¿Cuál no inhibe la síntesis de la pared?"]),
  {"rotulo": "Blanco y ejemplo", "eje_x": "Dato", "eje_y": "Blanco",
   "cols": ["Ejemplo", "Efecto"], "rows": ["Pared celular", "Ribosoma 50S", "Membrana"], "caso": (1, 0),
   "cells": [[("Imipenem, vancomicina", ["Bacitracina"]), ("Bactericida", [])],
             [("CLARITROMICINA", ["No actúa en pared"]), ("Bacteriostático", [])],
             [("Polimixinas", []), ("Bactericida", [])]]},
  ["Macrólidos: ARN 23S.",
   "Vancomicina: D-Ala-D-Ala.",
   "Bacitracina: bactoprenol."],
  GOODMAN)

# CB-394 · radial
V("radial", "CB-394", "campylobacter-jejuni-azitromicina-resistencia-quinolonas", "Diarrea por Campylobacter",
  "CIENCIAS BÁSICAS ENAM: CAMPYLOBACTER", CB,
  ("Campylobacter jejuni", ["Diarrea por pollo mal cocido",
   "Resistente a quinolonas en el Perú"]),
  ("Pregunta de infectología", ["¿Fármaco de elección?"]),
  {"rotulo": "Mapa del tema", "centro": "CAMPYLOBACTER", "centro_sub": "jejuni", "ans": 0,
   "items": [("AZITROMICINA", ["De elección"]),
             ("Quinolonas", ["Alta resistencia"]),
             ("Clínica", ["Disentería, dolor", "Simula apendicitis"]),
             ("Guillain-Barré", ["Mimetismo", "molecular"]),
             ("Tratar si", ["Grave, sangre", "Gestante, inmunodep."])],
   "ruta": ["Pollo crudo", "Diarrea", "Caso grave", "AZITROMICINA"]},
  ["Suele autolimitarse.",
   "Artritis reactiva.",
   "Ampicilina no sirve."],
  SANFORD)

# CB-395 · tarjetas
V("tarjetas", "CB-395", "ceftazidima-cefalosporina-antipseudomonas-avibactam", "Cefalosporinas y Pseudomonas",
  "CIENCIAS BÁSICAS ENAM: CEFALOSPORINAS ANTIPSEUDOMONAS", CB,
  ("Cefalosporinas antipseudomonas", ["Ceftazidima, cefoperazona y cefepime",
   "Ninguna de 1.ª o 2.ª generación"]),
  ("Pregunta de farmacología", ["¿Cuál tiene acción antipseudomonas?"]),
  {"rotulo": "¿Cubre Pseudomonas?", "ans": 0, "cards": [
      {"titulo": "CEFTAZIDIMA", "datos": [
          ("Generación", "3.ª", True), ("Pseudomonas", "Sí", True),
          ("Combinada", "Con avibactam", True)],
       "pie": "Neutropenia febril"},
      {"titulo": "Cefalotina", "datos": [
          ("Generación", "1.ª", False), ("Pseudomonas", "No", False),
          ("Uso", "Grampositivos", False)],
       "pie": "Como cefazolina"},
      {"titulo": "Cefradina", "datos": [
          ("Generación", "1.ª", False), ("Pseudomonas", "No", False),
          ("Uso", "Piel", False)],
       "pie": "Oral"},
      {"titulo": "Cefoxitina", "datos": [
          ("Grupo", "Cefamicina", False), ("Pseudomonas", "No", False),
          ("Uso", "Anaerobios", False)],
       "pie": "Profilaxis colon"}]},
  ["Cefepime: 4.ª generación.",
   "Ceftazidima-avibactam: KPC, OXA-48.",
   "Fibrosis quística."],
  SANFORD)

# CB-396 · radial
V("radial", "CB-396", "meningitis-tuberculosa-dexametasona-corticoides", "Corticoides en la tuberculosis",
  "CIENCIAS BÁSICAS ENAM: TUBERCULOSIS", CB,
  ("Corticoides en la TBC", ["Reducen la inflamación en sitios críticos",
   "Mejor evidencia: meningitis tuberculosa"]),
  ("Pregunta de infectología", ["¿En qué forma se añaden corticoides?"]),
  {"rotulo": "Mapa del tema", "centro": "TBC", "centro_sub": "Corticoides", "ans": 0,
   "items": [("MENINGITIS", ["Menos mortalidad", "y secuelas"]),
             ("Pericarditis", ["Menos constricción"]),
             ("Miliar grave", ["Con falla respiratoria"]),
             ("IRIS", ["Pacientes con VIH"]),
             ("No de rutina", ["Pulmonar, pleural", "peritoneal"])],
   "ruta": ["Meningitis TBC", "Dexametasona", "6-8 semanas", "MENOS SECUELAS"]},
  ["Tratamiento de 9-12 meses.",
   "Previene hidrocefalia y vasculitis.",
   "Reducir la dosis gradualmente."],
  MINSA_TB)

# CB-397 · matriz
V("matriz", "CB-397", "aminoglucosidos-viii-par-vestibular-coclear", "Ototoxicidad de los aminoglucósidos",
  "CIENCIAS BÁSICAS ENAM: OTOTOXICIDAD", CB,
  ("Aminoglucósidos y VIII par", ["Dañan la porción vestibular y la coclear",
   "Unos más una, otros más la otra"]),
  ("Pregunta de farmacología", ["¿Dónde se presenta la disfunción del VIII par?"]),
  {"rotulo": "Fármaco y daño", "eje_x": "Dato", "eje_y": "Fármaco",
   "cols": ["Predomina", "Síntoma"], "rows": ["Estreptomicina", "Gentamicina", "Amikacina"], "caso": (0, 0),
   "cells": [[("VESTIBULAR Y COCLEAR", ["Más vestibular"]), ("Vértigo, ataxia", [])],
             [("Vestibular", []), ("Oscilopsia", [])],
             [("Coclear", []), ("Hipoacusia, acúfenos", [])]]},
  ["Daño irreversible.",
   "Primero se pierden los agudos.",
   "Mutación mitocondrial m.1555A>G."],
  GOODMAN)

# CB-398 · termómetro
V("termometro", "CB-398", "azitromicina-sin-ajuste-renal-eliminacion-biliar", "Ajuste renal de los antibióticos",
  "CIENCIAS BÁSICAS ENAM: INSUFICIENCIA RENAL", CB,
  ("Antibióticos e insuficiencia renal", ["Los de eliminación renal se ajustan",
   "La azitromicina se elimina por bilis"]),
  ("Pregunta de farmacología", ["¿Cuál no requiere ajuste en IR severa?"]),
  {"rotulo": "Necesidad de ajuste",
   "niveles": [("Ninguna", "AZITROMICINA", ["Eliminación biliar"]),
               ("Mínima", "Ceftriaxona", ["Doble vía"]),
               ("Sí", "Ceftazidima", ["Levofloxacino"]),
               ("Crítica", "Amikacina", ["Nefrotóxica"])],
   "caso_nivel": 0, "ruta_titulo": "Por qué la azitromicina", "paso_label": "PASO",
   "pasos": [(1, "Bilis y heces", ["Poca orina"], True),
             (2, "Vida media larga", ["≈ 68 horas"], False),
             (3, "Esquemas cortos", ["3-5 días"], False)]},
  ["Sin ajuste: doxiciclina, clindamicina.",
   "Linezolid y moxifloxacino tampoco.",
   "Vancomicina: ajustar por niveles."],
  SANFORD)

# CB-399 · fases
V("fases", "CB-399", "sulfonamidas-dihidropteroato-sintasa-paba-trimetoprima", "Vía del folato bacteriano",
  "CIENCIAS BÁSICAS ENAM: SULFONAMIDAS", CB,
  ("Folato bacteriano", ["La bacteria lo sintetiza desde PABA",
   "El humano lo obtiene de la dieta"]),
  ("Pregunta de farmacología", ["¿Mecanismo de las sulfonamidas?"]),
  {"rotulo": "Pasos de la vía", "ans": 0,
   "fases": [("PABA", "Dihidropteroato", "SULFONAMIDAS", ["Inhibición competitiva"]),
             ("Dihidrofolato", "Reductasa", "Trimetoprima", ["Bloqueo secuencial"]),
             ("Tetrahidrofolato", "Síntesis", "Purinas", ["Y timidina"])],
   "chips_titulo": "Mecanismo · marcado el correcto",
   "chips": [("Dihidropteroato sintasa", True), ("ADN girasa", False), ("Transpeptidasa", False), ("Ribosoma 30S", False)]},
  ["Cotrimoxazol: sinergia bactericida.",
   "Kernícterus en neonatos.",
   "Hemólisis en déficit de G6PD."],
  GOODMAN)

# CB-400 · embudo
V("embudo", "CB-400", "ninas-licuado-flores-alucinaciones-midriasis-atropinicos", "Intoxicación por plantas en niñas",
  "CIENCIAS BÁSICAS ENAM: TOXÍNDROME ANTICOLINÉRGICO", CB,
  ("Síndrome anticolinérgico", ["Seco, rojo, caliente, ciego y loco",
   "Plantas con alcaloides tropánicos"]),
  ("Cuatro niñas preescolares", ["Licuado de hierbas y flores", "Alucinaciones, piel roja y midriasis"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Intoxicación por plantas",
   "candidatos": ["Atropínicos", "Carbamatos", "Organoclorados", "Inhibidores AChE"],
   "pasos": [("Hay midriasis y sequedad", ["Carbamatos", "Inhibidores AChE"]),
             ("Hay alucinaciones sin convulsión", ["Organoclorados"])],
   "final": ("ATROPÍNICOS", ["Floripondio, chamico", "Soporte y benzodiacepinas"]),
   "nota": "Grave: fisostigmina."},
  ["Taquicardia, retención urinaria.",
   "Hipertermia.",
   "DDT: convulsiones."],
  TOXI)

# CB-401 · fases
V("fases", "CB-401", "alcoholico-metanol-vision-etanol-fomepizol", "Toxicidad del metanol",
  "CIENCIAS BÁSICAS ENAM: METANOL", CB,
  ("Metanol", ["Se vuelve tóxico al metabolizarse",
   "El ácido fórmico daña la retina"]),
  ("Varón alcohólico de 54 años", ["Compromiso de la visión", "Sospecha de metanol"]),
  {"rotulo": "Metabolismo del metanol", "ans": 0,
   "fases": [("Alcohol DH", "Bloquear aquí", "ETANOL", ["O fomepizol", "Compite por la enzima"]),
             ("Formaldehído", "Aldehído DH", "Ácido fórmico", ["Tóxico"]),
             ("Daño", "Retina", "Ceguera", ["Acidosis con gap"])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Etanol", True), ("Piridoxina", False), ("Cianocobalamina", False), ("Tiamina", False)]},
  ["Ácido folínico elimina el fórmico.",
   "Hemodiálisis en casos graves.",
   "Gap osmolar alto."],
  TOXI)

# CB-402 · termómetro
V("termometro", "CB-402", "nino-hierro-vomitos-diarrea-sangre-deferoxamina", "Fases de la intoxicación por hierro",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR HIERRO", CB,
  ("Intoxicación por hierro", ["> 20 mg/kg: síntomas · > 60 mg/kg: grave",
   "Primero efecto corrosivo digestivo"]),
  ("Preescolar de 3 años", ["Ingirió dosis tóxica de hierro", "¿Primeras manifestaciones?"]),
  {"rotulo": "Fases",
   "niveles": [("0,5-6 h", "Digestiva", ["VÓMITOS, DIARREA", "CON SANGRE"]),
               ("6-24 h", "Latente", ["Mejoría aparente"]),
               ("12-48 h", "Shock", ["Acidosis, coagulopatía"]),
               ("2-3 días", "Hepática", ["Necrosis"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Soporte y fluidos", ["Primero"], True),
             (2, "Deferoxamina IV", ["Casos graves"], True),
             (3, "Carbón activado", ["No adsorbe hierro"], False)]},
  ["Tabletas prenatales de los padres.",
   "Estenosis pilórica tardía.",
   "Radiografía: tabletas radiopacas."],
  TOXI)

# CB-403 · fases
V("fases", "CB-403", "potencial-accion-musculo-esqueletico-acetilcolina-placa", "Inicio del potencial muscular",
  "CIENCIAS BÁSICAS ENAM: EXCITACIÓN MUSCULAR", CB,
  ("Músculo esquelético", ["No se contrae sin orden nerviosa",
   "La acetilcolina inicia el potencial"]),
  ("Pregunta de fisiología", ["¿Qué se secreta para iniciar el potencial?"]),
  {"rotulo": "Pasos en la placa", "ans": 1,
   "fases": [("Terminal", "Calcio entra", "Potencial nervioso", ["Canales de calcio"]),
             ("Liberación", "Vesículas", "ACETILCOLINA", ["Receptor nicotínico"]),
             ("Músculo", "Sodio entra", "Potencial", ["Túbulos T"])],
   "chips_titulo": "Sustancia · marcada la correcta",
   "chips": [("Acetilcolina", True), ("Noradrenalina", False), ("Potasio", False), ("Cloro", False)]},
  ["Músculo liso y cardíaco: automatismo.",
   "Acetilcolinesterasa la degrada.",
   "Luego: calcio y troponina C."],
  GUYTON)

# CB-404 · tarjetas
V("tarjetas", "CB-404", "ipratropio-antagonista-muscarinico-broncodilatador", "Broncodilatadores",
  "CIENCIAS BÁSICAS ENAM: BRONCODILATADORES", CB,
  ("Broncodilatadores", ["Beta-2 agonistas y anticolinérgicos",
   "El ipratropio bloquea receptores muscarínicos"]),
  ("Pregunta de farmacología", ["¿Mecanismo del bromuro de ipratropio?"]),
  {"rotulo": "¿Cómo actúa?", "ans": 0, "cards": [
      {"titulo": "IPRATROPIO", "datos": [
          ("Blanco", "Muscarínico M3", True), ("Acción", "Antagonista", True),
          ("Inicio", "15-30 min", True)],
       "pie": "Tiotropio: prolongado"},
      {"titulo": "Salbutamol", "datos": [
          ("Blanco", "Beta-2", False), ("Acción", "Agonista", False),
          ("Inicio", "Minutos", False)],
       "pie": "Rescate"},
      {"titulo": "Montelukast", "datos": [
          ("Blanco", "CysLT1", False), ("Acción", "Antagonista", False),
          ("Uso", "Control", False)],
       "pie": "Antileucotrieno"},
      {"titulo": "Teofilina", "datos": [
          ("Blanco", "Fosfodiesterasa", False), ("Acción", "Inhibe", False),
          ("Margen", "Estrecho", False)],
       "pie": "Metilxantina"}]},
  ["Amonio cuaternario: poco sistémico.",
   "Boca seca.",
   "EPOC y crisis asmática grave."],
  GOODMAN)

# CB-405 · árbol
A("CB-405", "artritis-reumatoide-diclofenaco-cox-prostaglandinas", "Mecanismo de los AINE",
  "CIENCIAS BÁSICAS ENAM: AINE", CB,
  ("AINE", ["Inhiben la ciclooxigenasa",
   "Bajan prostaglandinas y tromboxanos"]),
  ("Paciente con artritis reumatoide", ["Diclofenaco por 3 semanas", "¿Por qué mejoró?"]),
  Q("¿Qué enzima inhibe el diclofenaco?", [
      L("COX-1 y COX-2", "MENOS PROSTAGLANDINAS", ["Analgesia, antiinflamación"], path=True),
      L("Receptores opioides", "No actúa", ["Eso es de opioides"])], path=True),
  ("Efectos según COX", [("COX-1", True), ("COX-2", False)], [
      ("Fisiológica", ["Estómago, riñón", "Inflamación"]),
      ("Al inhibir", ["Úlcera, sangrado", "Analgesia"])]),
  ["No frenan la destrucción articular.",
   "Añadir metotrexato.",
   "Coxibs: menos daño gástrico."],
  GOODMAN)

# CB-406 · radial
V("radial", "CB-406", "cocaina-vasoconstrictora-ester-recaptacion-vvvf", "Cocaína: verdadero o falso",
  "CIENCIAS BÁSICAS ENAM: COCAÍNA", CB,
  ("Cocaína", ["Alcaloide de la hoja de coca",
   "Bloquea la recaptación de monoaminas"]),
  ("Pregunta de farmacología", ["Marcar V o F en 4 afirmaciones"]),
  {"rotulo": "Mapa del tema", "centro": "COCAÍNA", "centro_sub": "V o F", "ans": 3,
   "items": [("1 · Verdadero", ["Vasoconstrictora"]),
             ("2 · Verdadero", ["Éster benzoico", "y metilecgonina"]),
             ("3 · Verdadero", ["Bloquea recaptación", "de noradrenalina"]),
             ("4 · FALSO", ["No es antagonista", "del GABA"]),
             ("Riesgos", ["Infarto, ACV", "Disección aórtica"])],
   "ruta": ["V", "V", "V", "F"]},
  ["Único anestésico local vasoconstrictor.",
   "Dopamina: euforia y adicción.",
   "Evitar betabloqueantes."],
  GOODMAN)

# CB-407 · matriz
V("matriz", "CB-407", "anfetamina-libera-noradrenalina-dopamina-serotonina", "Estimulantes del SNC",
  "CIENCIAS BÁSICAS ENAM: ESTIMULANTES", CB,
  ("Estimulantes", ["Aumentan monoaminas en la sinapsis",
   "Por liberación o por bloqueo de recaptación"]),
  ("Pregunta de farmacología", ["¿Qué liberan las anfetaminas?"]),
  {"rotulo": "Mecanismo y transmisores", "eje_x": "Dato", "eje_y": "Fármaco",
   "cols": ["Mecanismo", "Transmisores"], "rows": ["Anfetamina", "Cocaína", "MDMA"], "caso": (0, 1),
   "cells": [[("Libera vesículas", ["VMAT2"]), ("NA, DA Y 5-HT", [])],
             [("Bloquea recaptación", []), ("NA, DA, 5-HT", [])],
             [("Libera", []), ("Sobre todo 5-HT", ["Hipertermia"])]]},
  ["Usos: TDAH y narcolepsia.",
   "Intoxicación: psicosis e hipertermia.",
   "No libera acetilcolina ni histamina."],
  GOODMAN)

# CB-408 · embudo
V("embudo", "CB-408", "hipertenso-captopril-tos-seca-bk-negativo-ieca", "Tos crónica en un hipertenso",
  "CIENCIAS BÁSICAS ENAM: EFECTOS DE LOS IECA", CB,
  ("Tos por IECA", ["Acumulan bradicinina y sustancia P",
   "Tos seca en 5-20 %"]),
  ("Varón de 38 años con captopril", ["Tos seca de 20 días", "BK negativo, radiografía normal"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Tos de 3 semanas",
   "candidatos": ["IECA", "TBC reactivada", "Neumonía atípica", "Diurético de asa"],
   "pasos": [("BK y radiografía normales", ["TBC reactivada", "Neumonía atípica"]),
             ("Recibe tiazida, no de asa", ["Diurético de asa"])],
   "final": ("TOS POR IECA", ["Suspender el captopril", "Cambiar a losartán"]),
   "nota": "Desaparece en 1-4 semanas."},
  ["Más en mujeres y asiáticos.",
   "Losartán no sube bradicinina.",
   "Angioedema: otro efecto de IECA."],
  GOODMAN)

# CB-409 · termómetro
V("termometro", "CB-409", "adrenalina-dosis-alta-alfa-1-vasoconstriccion", "Efectos de la adrenalina según la dosis",
  "CIENCIAS BÁSICAS ENAM: CATECOLAMINAS", CB,
  ("Adrenalina", ["Actúa sobre receptores alfa y beta",
   "En dosis altas predomina alfa-1"]),
  ("Pregunta de farmacología", ["Dosis alta IV rápida sube la presión", "¿Por qué?"]),
  {"rotulo": "Dosis y receptor",
   "niveles": [("Baja", "Beta-2", ["Vasodilata músculo"]),
               ("Media", "Beta-1", ["Más FC y fuerza"]),
               ("Alta", "ALFA-1", ["Vasoconstricción", "Sube la PA"]),
               ("Paro", "1 mg IV", ["Perfusión coronaria"])],
   "caso_nivel": 2, "ruta_titulo": "Uso clínico", "paso_label": "PASO",
   "pasos": [(1, "Anafilaxia", ["Vía IM"], False),
             (2, "IV rápida", ["Riesgo de crisis"], True),
             (3, "Paro cardíaco", ["Cada 3-5 min"], False)]},
  ["IV rápida: arritmias, isquemia.",
   "No es inotrópico negativo.",
   "Beta-2: broncodilatación."],
  GOODMAN)

# CB-410 · árbol
A("CB-410", "adulto-mayor-podagra-hidroclorotiazida-hiperuricemia", "Gota por fármacos",
  "CIENCIAS BÁSICAS ENAM: HIPERURICEMIA FARMACOLÓGICA", CB,
  ("Fármacos que suben el ácido úrico", ["Tiazidas y diuréticos de asa",
   "También aspirina en dosis bajas"]),
  ("Varón de 70 años hipertenso", ["Dolor e hinchazón del primer dedo", "Podagra"]),
  Q("¿Recibe diurético?", [
      L("Tiazida", "HIDROCLOROTIAZIDA", ["Menos excreción de urato", "Causa la crisis"], path=True),
      L("Otros", "Revisar", ["Aspirina, ciclosporina"])], path=True),
  ("Alternativa antihipertensiva", [("Fármaco", True), ("Urato", False)], [
      ("Losartán", ["ARA II", "Uricosúrico"]),
      ("Amlodipino", ["Calcioantagonista", "Neutro o baja"])]),
  ["Pirazinamida y etambutol: suben urato.",
   "Insulina y levotiroxina: no.",
   "Tratar la crisis con colchicina o AINE."],
  "ACR – Gout management guideline (2020)")

# CB-411 · fases
V("fases", "CB-411", "naloxona-revierte-depresion-respiratoria-opioides", "Acción de la naloxona",
  "CIENCIAS BÁSICAS ENAM: OPIOIDES", CB,
  ("Naloxona", ["Antagonista puro de receptores mu",
   "Revierte la depresión respiratoria"]),
  ("Pregunta de toxicología", ["¿Qué evita la naloxona?"]),
  {"rotulo": "Evolución tras la dosis", "ans": 0,
   "fases": [("Minutos", "IV, IM o nasal", "RESPIRA", ["Revierte depresión", "Y miosis"]),
             ("30-90 min", "Vida media", "Efecto cede", ["Opioide persiste"]),
             ("Horas", "Vigilar", "Redosificar", ["O infusión"])],
   "chips_titulo": "Evita · marcado el correcto",
   "chips": [("Depresión respiratoria", True), ("Abstinencia", False), ("Midriasis", False), ("Taquicardia", False)]},
  ["En dependientes precipita abstinencia.",
   "Metadona dura más que la naloxona.",
   "No buscar el despertar completo."],
  TOXI)

# CB-412 · embudo
V("embudo", "CB-412", "postoperatorio-analgesico-convulsiones-tramadol", "Analgésico que causa convulsiones",
  "CIENCIAS BÁSICAS ENAM: TRAMADOL", CB,
  ("Tramadol", ["Opioide débil que inhibe recaptación",
   "de serotonina y noradrenalina"]),
  ("Varón de 30 años tras colecistectomía", ["Recibe un analgésico", "A las 2 horas: convulsiones"]),
  {"rotulo": "Embudo de fármacos",
   "inicio": "Cinco analgésicos",
   "candidatos": ["Tramadol", "Ketorolaco", "Celecoxib", "Paracetamol"],
   "pasos": [("No es AINE", ["Ketorolaco", "Celecoxib"]),
             ("Baja el umbral convulsivo", ["Paracetamol"])],
   "final": ("TRAMADOL", ["Convulsiones aun a dosis habituales", "Síndrome serotoninérgico"]),
   "nota": "Meperidina: riesgo parecido (normeperidina)."},
  ["Tratar con benzodiacepinas.",
   "Naloxona no revierte las convulsiones.",
   "Evitar con ISRS o IMAO."],
  GOODMAN)
