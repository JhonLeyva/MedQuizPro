"""Bloque 8 · parte A."""
from c8 import F8, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"
HARPER = "Harper. Bioquímica ilustrada 32.ª ed. (2023)"
ROBBINS = "Robbins y Cotran. Patología estructural y funcional 10.ª ed. (2021)"
CMP = "Colegio Médico del Perú – Código de Ética y Deontología (2023)"

# REU-066 · termómetro
V("termometro", "REU-066", "adolescente-nodulos-quisticos-espalda-acne-grave", "Gravedad del acné",
  "DERMATOLOGÍA ENAM: ACNÉ GRAVE", "DERMATOLOGÍA",
  ("Clasificación del acné", ["Se gradúa por el tipo de lesión predominante",
   "Nódulos y quistes definen el acné grave (noduloquístico)"]),
  ("Adolescente varón", ["Cara, tórax y espalda: comedones, pápulo-pústulas", "Nódulos quísticos y lesiones que aumentan"]),
  {"rotulo": "Grado según la lesión",
   "niveles": [("Leve", "Comedoniano", ["Comedones abiertos y cerrados"]),
               ("Moderado", "Pápulo-pustular", ["Pápulas y pústulas"]),
               ("Mod. grave", "Muchas pústulas", ["Algunos nódulos"]),
               ("Grave", "Noduloquístico", ["NÓDULOS Y QUISTES", "Riesgo de cicatrices"])],
   "caso_nivel": 3, "ruta_titulo": "Tratamiento del acné grave", "paso_label": "PASO",
   "pasos": [(1, "Isotretinoína oral", ["Tratamiento de elección"], True),
             (2, "Anticoncepción y controles", ["Teratógena · perfil lipídico"], False),
             (3, "Puente: antibiótico oral", ["Doxiciclina + tópico"], False)]},
  ["Retinoide tópico en el acné comedoniano.",
   "Peróxido de benzoílo evita la resistencia a antibióticos.",
   "El acné grave deja cicatrices: tratar precozmente."],
  "AAD – Guidelines of care for acne vulgaris (2024) · Fitzpatrick. Dermatología 9.ª ed.")

# GAS-073 · árbol
A("GAS-073", "cirrotico-alergia-ceftriaxona-pbe-quinolona", "Antibiótico en la peritonitis bacteriana espontánea",
  "GASTROENTEROLOGÍA ENAM: PBE Y ALERGIA", "GASTROENTEROLOGÍA",
  ("Peritonitis bacteriana espontánea", ["Líquido ascítico con ≥ 250 PMN/mm³",
   "Elección: cefalosporina de 3.ª generación; alternativa: quinolona"]),
  ("Varón de 55 años con cirrosis", ["Fiebre, dolor abdominal · 500 PMN/mm³", "Alérgico a la ceftriaxona · creatinina 1,4"]),
  Q("¿PMN ≥ 250/mm³ en el líquido ascítico?", [
      Q("¿Alergia a cefalosporinas?", [
          L("Sí", "FLUOROQUINOLONA", ["Ciprofloxacino o levofloxacino", "Si no la recibía como profilaxis"], path=True),
          L("No", "Ceftriaxona o cefotaxima", ["5 días"])],
        edge="Sí", path=True),
      L("No", "No es PBE", ["Vigilar y repetir si hay clínica"])], path=True),
  ("Además del antibiótico", [("Albúmina", True), ("Diuréticos", False)], [
      ("Indicación", ["Creatinina > 1 o bilirrubina > 4", "Suspender si hay lesión renal"]),
      ("Objetivo", ["Prevenir síndrome hepatorrenal", "Evitan más daño renal"])]),
  ["Albúmina 1,5 g/kg el día 1 y 1 g/kg el día 3.",
   "Tras el episodio: profilaxis secundaria de por vida.",
   "Paracentesis de control a las 48 h si no mejora."],
  "EASL – Clinical practice guidelines on decompensated cirrhosis (2018) · AASLD (2021)")

# CB-079 · tarjetas
V("tarjetas", "CB-079", "catalasa-peroxidasa-peroxido-hidrogeno-antioxidante", "Enzimas de óxido-reducción",
  "CIENCIAS BÁSICAS ENAM: HIDROPEROXIDASAS", "CIENCIAS BÁSICAS",
  ("Las oxidorreductasas", ["Transfieren electrones o hidrógeno",
   "Las hidroperoxidasas destruyen peróxidos y radicales libres"]),
  ("Pregunta de bioquímica", ["¿Qué enzimas protegen contra los radicales libres?"]),
  {"rotulo": "¿Qué enzima protege?", "ans": 0, "cards": [
      {"titulo": "HIDROPEROXIDASAS", "datos": [
          ("Ejemplos", "Catalasa, peroxidasa", True), ("Sustrato", "Peróxidos (H₂O₂)", True),
          ("Función", "Antioxidante", True)],
       "pie": "Glutatión peroxidasa usa selenio"},
      {"titulo": "Oxidasas", "datos": [
          ("Ejemplos", "Citocromo oxidasa", False), ("Sustrato", "O₂ como aceptor", False),
          ("Función", "Cadena respiratoria", False)],
       "pie": "Forman agua"},
      {"titulo": "Deshidrogenasas", "datos": [
          ("Ejemplos", "Lactato DH", False), ("Sustrato", "NAD⁺, FAD", False),
          ("Función", "Transfieren H", False)],
       "pie": "No usan O₂"},
      {"titulo": "Oxigenasas", "datos": [
          ("Ejemplos", "Citocromo P450", False), ("Sustrato", "O₂ al sustrato", False),
          ("Función", "Hidroxilación", False)],
       "pie": "Metabolismo de fármacos"}]},
  ["La superóxido dismutasa convierte O₂⁻ en H₂O₂.",
   "La catalasa convierte H₂O₂ en agua y oxígeno.",
   "Vitaminas C y E: antioxidantes no enzimáticos."],
  HARPER)

# PED-220 · embudo
V("embudo", "PED-220", "trofozoito-dos-nucleos-diarrea-grasa-metronidazol", "Parásito con dos núcleos en heces",
  "PEDIATRÍA ENAM: GIARDIASIS", "PEDIATRÍA",
  ("Giardiasis", ["Protozoo del intestino delgado: diarrea grasosa, distensión",
   "Trofozoíto piriforme con dos núcleos («cara»)"]),
  ("Niño de 3 años", ["Diarrea persistente amarillenta con moco", "Heces: trofozoíto elipsoidal con dos núcleos"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Diarrea persistente en el niño",
   "candidatos": ["Giardia", "Entamoeba", "Cryptosporidium", "Helmintos"],
   "pasos": [("Protozoo, no huevo de helminto", ["Helmintos"]),
             ("Dos núcleos, sin sangre", ["Entamoeba", "Cryptosporidium"])],
   "final": ("GIARDIA LAMBLIA", ["Metronidazol 15 mg/kg/día por 5-7 días", "Alternativa: tinidazol o nitazoxanida"]),
   "nota": "Albendazol y praziquantel tratan helmintos; el bitionol, trematodos."},
  ["Contagio fecal-oral: agua no tratada, guarderías.",
   "Puede causar malabsorción y falla de crecimiento.",
   "Tratar a los contactos sintomáticos."],
  NELSON + " · CDC – Giardiasis (2024)")

# GIN-234 · árbol
A("GIN-234", "amenorrea-5-semanas-saco-10-mm-sin-embrion-control", "Saco gestacional sin embrión",
  "OBSTETRICIA ENAM: GESTACIÓN TEMPRANA", "OBSTETRICIA",
  ("Diagnóstico de pérdida gestacional", ["Saco ≥ 25 mm sin embrión o embrión ≥ 7 mm sin latido",
   "Por debajo de esos límites: repetir ecografía"]),
  ("Mujer de 22 años, 5 semanas", ["Sangrado escaso · cuello cerrado", "Saco de 10 mm sin embrión"]),
  Q("¿Saco ≥ 25 mm sin embrión?", [
      L("Sí", "Pérdida gestacional", ["Misoprostol, AMEU o expectante"]),
      Q("¿Saco pequeño y edad temprana?", [
          L("Sí", "CONTROL ECOGRÁFICO", ["Repetir en 7-14 días", "No evacuar todavía"], path=True),
          L("No", "Sospecha de ectópico", ["β-hCG seriada"])],
        edge="No", path=True)], path=True),
  ("Criterios ecográficos", [("Pérdida segura", False), ("Control", True)], [
      ("Saco sin embrión", ["≥ 25 mm", "< 25 mm"]),
      ("Embrión sin latido", ["≥ 7 mm", "< 7 mm"])]),
  ["Evacuar por error una gestación viable es un daño grave.",
   "El embrión se ve desde las 6 semanas por vía vaginal.",
   "Descartar embarazo ectópico si el útero está vacío."],
  "ACOG – Practice Bulletin 200: Early pregnancy loss (2018) · SRU (2013)")

# TRA-050 · radial
V("radial", "TRA-050", "luxacion-posterior-cadera-pie-caido-nervio-ciatico", "Luxación de cadera y nervios",
  "TRAUMATOLOGÍA ENAM: LUXACIÓN DE CADERA", "TRAUMATOLOGÍA",
  ("Luxación posterior de cadera", ["La más frecuente: golpe en la rodilla con cadera flexionada",
   "El nervio ciático pasa detrás de la articulación"]),
  ("Pregunta de anatomía", ["¿Qué nervio se lesiona en la luxación posterior?"]),
  {"rotulo": "Mapa del tema", "centro": "LUXACIÓN", "centro_sub": "De cadera", "ans": 0,
   "items": [("POSTERIOR", ["Nervio ciático", "Pie caído"]),
             ("Anterior", ["Nervio femoral", "Vasos femorales"]),
             ("Central", ["Fractura del acetábulo"]),
             ("Complicación", ["Necrosis avascular"]),
             ("Conducta", ["Reducir < 6 horas"])],
   "ruta": ["Accidente de tránsito", "Rodilla contra tablero", "Cabeza femoral atrás", "CIÁTICO"]},
  ["Postura: flexión, aducción y rotación interna.",
   "Rama peronea del ciático: la más afectada.",
   "La reducción precoz reduce la necrosis avascular."],
  "Rockwood and Green's Fractures in Adults 10.ª ed. · " + ATLS)

# CB-080 · fases
V("fases", "CB-080", "herida-cortante-proliferacion-fibroblasto-colageno", "Fases de la cicatrización",
  "CIENCIAS BÁSICAS ENAM: REPARACIÓN TISULAR", "CIENCIAS BÁSICAS",
  ("Cicatrización de heridas", ["Hemostasia e inflamación, proliferación y remodelación",
   "El fibroblasto sintetiza colágeno y matriz extracelular"]),
  ("Varón de 35 años con herida cortante", ["¿Qué célula es la principal en la reparación?"]),
  {"rotulo": "Fases de la reparación", "ans": 1,
   "fases": [("Inflamatoria", "Días 1-4", "Neutrófilos", ["Macrófagos limpian"]),
             ("Proliferativa", "Días 4-21", "FIBROBLASTO", ["Colágeno III", "Tejido de granulación"]),
             ("Remodelación", "3 sem - 1 año", "Maduración", ["Colágeno I", "Miofibroblasto contrae"])],
   "curvas": [("Colágeno", SKY, [0.05, 0.1, 0.4, 0.7, 0.85, 0.9, 0.95])],
   "chips_titulo": "Célula principal · marcada la correcta",
   "chips": [("Fibroblasto", True), ("Miofibroblasto", False), ("Fibrocito", False), ("Neutrófilo", False)]},
  ["El miofibroblasto (actina) contrae la herida.",
   "El fibrocito es un fibroblasto en reposo.",
   "La vitamina C es necesaria para el colágeno."],
  ROBBINS)

# CB-081 · termómetro
V("termometro", "CB-081", "lidocaina-parestesia-peribucal-desorientacion-oxigeno", "Toxicidad por anestésicos locales",
  "CIENCIAS BÁSICAS ENAM: ANESTÉSICOS LOCALES", "CIENCIAS BÁSICAS",
  ("Toxicidad sistémica por anestésicos locales", ["Síntomas neurológicos y luego cardiovasculares",
   "Primero: detener la infiltración, oxígeno y vía aérea"]),
  ("Mujer de 20 años, exéresis de lipoma", ["Hormigueo de lengua y labios tras lidocaína al 2 %", "Desorientada · PA 90/60 · SatO₂ 90 %"]),
  {"rotulo": "Gravedad de la toxicidad",
   "niveles": [("Inicial", "Síntomas leves", ["Sabor metálico, tinnitus"]),
               ("Moderada", "SNC afectado", ["PERIBUCAL + CONFUSIÓN", "Hipoxemia"]),
               ("Grave", "Convulsiones", ["Coma"]),
               ("Crítica", "Colapso cardiaco", ["Arritmias, paro"])],
   "caso_nivel": 1, "ruta_titulo": "Qué hacer en este caso", "paso_label": "PASO",
   "pasos": [(1, "Oxígeno al 100 % y vía aérea", ["Evita hipoxia y acidosis"], True),
             (2, "Benzodiacepina si convulsiona", ["Midazolam"], False),
             (3, "Emulsión lipídica 20 %", ["Si hay toxicidad grave"], False)]},
  ["Dosis máxima de lidocaína: 4,5 mg/kg (7 con adrenalina).",
   "Aspirar antes de inyectar para evitar la vía intravascular.",
   "No es alergia: los corticoides no sirven."],
  "ASRA – Checklist for local anesthetic systemic toxicity (2020) · Miller's Anesthesia 9.ª ed.")

# NRL-058 · puntaje
V("puntaje", "NRL-058", "motociclista-ojos-al-dolor-sonidos-retira-glasgow-8", "Escala de coma de Glasgow",
  "NEUROLOGÍA ENAM: ESCALA DE GLASGOW", "NEUROLOGÍA",
  ("Escala de Glasgow", ["Ocular (1-4) + verbal (1-5) + motora (1-6)",
   "≤ 8: TEC grave, asegurar la vía aérea"]),
  ("Varón de 20 años, accidente de moto", ["Abre los ojos solo al dolor", "Sonidos incomprensibles · retira ante el dolor"]),
  {"rotulo": "Glasgow del caso", "escala": "Glasgow", "total": 8, "max": 15,
   "total_label": "Puntaje del caso",
   "interpreta": "TEC grave: intubar",
   "items": [("Ocular: al dolor", "2", True), ("Verbal: sonidos incomprensibles", "2", True),
             ("Motora: retira al dolor", "4", True)],
   "bandas": [("13-15", "TEC leve", "Observar, TC según riesgo", False),
              ("9-12", "TEC moderado", "TC y hospitalizar", False),
              ("≤ 8", "TEC grave", "Intubar y TC urgente", True)]},
  ["En cada componente se anota lo mejor que logra.",
   "Localiza el dolor = 5; retira = 4; flexión anormal = 3.",
   "Palabras inapropiadas = 3; sonidos = 2."],
  ATLS + " · Teasdale G. Lancet Neurol (2014)")

# PED-221 · matriz
V("matriz", "PED-221", "dpp-neonato-sarnat-iii-ph-6-5-hipotermia", "Estadios de Sarnat",
  "PEDIATRÍA ENAM: ENCEFALOPATÍA HIPÓXICO-ISQUÉMICA", "PEDIATRÍA",
  ("Encefalopatía hipóxico-isquémica", ["Asfixia perinatal con acidosis grave y alteración neurológica",
   "Moderada o grave: hipotermia terapéutica antes de las 6 horas"]),
  ("Neonato de 1 hora, cesárea por DPP", ["Letárgico, hipoactivo, hiporrefléxico, Moro incompleto", "Sarnat III · pH 6,5"]),
  {"rotulo": "Estadio y conducta", "eje_x": "Rasgo", "eje_y": "Sarnat",
   "cols": ["Conciencia", "Conducta"], "rows": ["I (leve)", "II (moderado)", "III (grave)"], "caso": (2, 1),
   "cells": [[("Hiperalerta", ["Tono normal"]), ("Observar", ["Buen pronóstico"])],
             [("Letargia", ["Hipotonía, convulsiones"]), ("Hipotermia", ["< 6 horas"])],
             [("Estupor o coma", ["Flacidez, sin Moro"]), ("HIPOTERMIA", ["33,5 °C por 72 h"])]]},
  ["Criterios: ≥ 36 semanas, pH ≤ 7,0 o Apgar ≤ 5 a los 10 min.",
   "Convulsiones: fenobarbital, no anticonvulsivante oral.",
   "Se enfría el cuerpo entero y luego se recalienta lento."],
  "AAP – Hypothermia and neonatal encephalopathy (2014) · " + NELSON)

# PED-222 · embudo
V("embudo", "PED-222", "lactante-11-meses-hb-9-ferritina-baja-hierro", "Anemia microcítica en el lactante",
  "PEDIATRÍA ENAM: ANEMIA FERROPÉNICA", "PEDIATRÍA",
  ("Anemia ferropénica", ["La causa más frecuente de anemia en el lactante",
   "Tratamiento: hierro oral 3 mg/kg/día por 6 meses (MINSA)"]),
  ("Lactante de 11 meses", ["Baja ganancia ponderal · Hb 9 g/dL", "Microcítica e hipocrómica · ferritina baja"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Anemia en el lactante",
   "candidatos": ["Ferropénica", "Megaloblástica", "Renal", "Talasemia"],
   "pasos": [("Microcítica: no es megaloblástica", ["Megaloblástica"]),
             ("Ferritina baja: falta hierro", ["Talasemia", "Renal"])],
   "final": ("ANEMIA FERROPÉNICA", ["Hierro oral (sulfato o polimaltosado)", "Control de Hb al mes, 3 y 6 meses"]),
   "nota": "La eritropoyetina es para la anemia renal; la B12 y el folato, para la megaloblástica."},
  ["Dar el hierro lejos de la leche.",
   "Consejería: alimentos de origen animal ricos en hierro.",
   "Suplemento preventivo desde los 4 meses."],
  "MINSA – NTS 213: Prevención y control de la anemia (2024) · " + NELSON)

# PED-223 · tarjetas
V("tarjetas", "PED-223", "sindrome-nefrotico-nino-podocitos-cambios-minimos", "Lesiones del síndrome nefrótico",
  "PEDIATRÍA ENAM: SÍNDROME NEFRÓTICO", "PEDIATRÍA",
  ("Síndrome nefrótico en la infancia", ["Proteinuria masiva, hipoalbuminemia, edema",
   "80-90 % son de cambios mínimos y responden a corticoides"]),
  ("Pregunta de nefrología pediátrica", ["¿Cuál es la lesión más frecuente en niños?"]),
  {"rotulo": "¿Qué lesión es la más frecuente?", "ans": 0, "cards": [
      {"titulo": "CAMBIOS MÍNIMOS", "datos": [
          ("Edad típica", "2-6 años", True), ("Microscopía óptica", "Normal", True),
          ("Corticoides", "Responde", True)],
       "pie": "Fusión de podocitos"},
      {"titulo": "Esclerosis focal", "datos": [
          ("Edad típica", "Adolescente", False), ("Microscopía óptica", "Esclerosis", False),
          ("Corticoides", "A menudo resiste", False)],
       "pie": "Segunda causa"},
      {"titulo": "Membranosa", "datos": [
          ("Edad típica", "Adulto", False), ("Microscopía óptica", "MB engrosada", False),
          ("Corticoides", "Poca", False)],
       "pie": "Anti-PLA2R"},
      {"titulo": "Membranoproliferativa", "datos": [
          ("Edad típica", "Escolar", False), ("Microscopía óptica", "Doble contorno", False),
          ("Corticoides", "Poca", False)],
       "pie": "C3 bajo"}]},
  ["No se biopsia al inicio si la clínica es típica.",
   "Prednisona 60 mg/m²/día por 4-6 semanas.",
   "Biopsia si no responde o hay rasgos atípicos."],
  "KDIGO – Glomerular diseases guideline (2021) · " + NELSON)

# SP-170 · radial
V("radial", "SP-170", "irc-avanzada-gestante-junta-medica-aborto-terapeutico", "Principios bioéticos",
  "SALUD PÚBLICA ENAM: ABORTO TERAPÉUTICO", "SALUD PÚBLICA",
  ("Aborto terapéutico", ["Legal en el Perú si es el único medio para salvar la vida de la gestante",
   "Lo decide una junta médica con consentimiento de la paciente"]),
  ("Multigesta de 18 semanas", ["Insuficiencia renal crónica avanzada", "El embarazo pone en riesgo su vida"]),
  {"rotulo": "Mapa del tema", "centro": "PRINCIPIOS", "centro_sub": "Bioéticos", "ans": 0,
   "items": [("BENEFICENCIA", ["Proteger la vida materna", "Hacer el bien"]),
             ("Autonomía", ["Ella lo solicita"]),
             ("No maleficencia", ["No causar daño"]),
             ("Justicia", ["Trato equitativo"])],
   "ruta": ["Riesgo de muerte", "Junta médica", "Actuar por su bien", "BENEFICENCIA"]},
  ["Guía técnica nacional de aborto terapéutico (2014).",
   "Plazo: hasta las 22 semanas.",
   "Requiere consentimiento informado escrito."],
  "MINSA – Guía técnica de interrupción terapéutica del embarazo (2014) · " + CMP)

# SP-171 · árbol
A("SP-171", "parto-andino-pertinencia-cultural-entrega-placenta", "Parto con pertinencia cultural",
  "SALUD PÚBLICA ENAM: INTERCULTURALIDAD", "SALUD PÚBLICA",
  ("Parto vertical con adecuación intercultural", ["Respeta posición, acompañante, abrigo y costumbres",
   "La familia puede llevarse la placenta para enterrarla"]),
  ("Serumista en zona rural andina", ["Establecimiento con parto culturalmente adecuado", "¿Qué hacer con la placenta?"]),
  Q("¿La familia desea la placenta?", [
      L("Sí", "ENTREGAR LA PLACENTA", ["Preguntar a la familia", "Embolsada, con indicaciones de entierro"], path=True),
      L("No", "Eliminar como residuo biológico", ["Según bioseguridad"])], path=True),
  ("Adecuación intercultural", [("Se respeta", True), ("Se evita", False)], [
      ("Posición", ["Vertical si la elige", "Obligar a la litotomía"]),
      ("Placenta", ["Entregarla si la piden", "Decidir sin preguntar"])]),
  ["La norma técnica de parto vertical es del MINSA (2016).",
   "Permitir un acompañante elegido por la gestante.",
   "Ofrecer bebidas calientes y abrigo."],
  "MINSA – NTS 121: Atención del parto vertical con adecuación intercultural (2016)")

# CB-082 · radial
V("radial", "CB-082", "insuficiencia-renal-pielonefritis-convulsiones-imipenem", "Antibióticos y efectos adversos",
  "CIENCIAS BÁSICAS ENAM: NEUROTOXICIDAD DEL IMIPENEM", "CIENCIAS BÁSICAS",
  ("Imipenem", ["Carbapenémico que baja el umbral convulsivo (antagonista GABA-A)",
   "Riesgo mayor con falla renal sin ajuste de dosis"]),
  ("Varón de 58 años con insuficiencia renal", ["En tratamiento por pielonefritis", "Presenta convulsiones bruscas"]),
  {"rotulo": "Mapa del tema", "centro": "EFECTO ADVERSO", "centro_sub": "¿Qué fármaco?", "ans": 0,
   "items": [("IMIPENEM", ["Convulsiones", "Peor si falla renal"]),
             ("Amikacina", ["Nefro y ototoxicidad"]),
             ("Ceftriaxona", ["Barro biliar"]),
             ("Ampicilina", ["Rash, alergia"]),
             ("Quinolonas", ["Tendinitis, convulsiones"])],
   "ruta": ["Falla renal", "Se acumula", "Bloquea GABA-A", "IMIPENEM"]},
  ["Ajustar dosis de carbapenémicos al filtrado glomerular.",
   "Meropenem tiene menor riesgo convulsivo.",
   "Tratar las convulsiones con benzodiacepinas."],
  "Goodman & Gilman. Bases farmacológicas 14.ª ed. (2023)")

# SP-172 · fases
V("fases", "SP-172", "ensayo-clinico-poscomercializacion-farmacovigilancia-fase-iv", "Fases del ensayo clínico",
  "SALUD PÚBLICA ENAM: ENSAYOS CLÍNICOS", "SALUD PÚBLICA",
  ("Desarrollo de un fármaco", ["Cuatro fases, de pocos voluntarios a toda la población",
   "La fase IV vigila efectos raros tras la comercialización"]),
  ("Pregunta de epidemiología", ["¿En qué fase se estudian efectos graves tras la aprobación?"]),
  {"rotulo": "Fases del ensayo", "ans": 3,
   "fases": [("Fase I", "Decenas", "Seguridad", ["Sanos, dosis"]),
             ("Fase II", "Cientos", "Eficacia", ["Enfermos, dosis útil"]),
             ("Fase III", "Miles", "Comparación", ["Frente al estándar"]),
             ("Fase IV", "Población", "FARMACOVIGILANCIA", ["Tras aprobación", "Efectos raros"])],
   "curvas": [("Participantes", SKY, [0.05, 0.1, 0.2, 0.35, 0.55, 0.8, 0.95])],
   "chips_titulo": "Fase del caso · marcada la correcta",
   "chips": [("IV", True), ("III", False), ("II", False), ("I", False)]},
  ["La aprobación sanitaria llega tras la fase III.",
   "Fase IV detecta efectos poco frecuentes.",
   "En el Perú se notifica a la DIGEMID."],
  GORDIS + " · OMS – Farmacovigilancia (2024)")

# SP-173 · radial
V("radial", "SP-173", "modelo-cuidado-integral-enfoques-interculturalidad", "Enfoques del cuidado integral",
  "SALUD PÚBLICA ENAM: MODELO DE CUIDADO INTEGRAL", "SALUD PÚBLICA",
  ("Modelo de Cuidado Integral de Salud (MCI)", ["Por curso de vida, para la persona, familia y comunidad",
   "Se basa en enfoques transversales, como la interculturalidad"]),
  ("Pregunta de gestión", ["¿En qué enfoque se desarrolla el MCI?"]),
  {"rotulo": "Mapa del tema", "centro": "MCI", "centro_sub": "Enfoques", "ans": 0,
   "items": [("INTERCULTURALIDAD", ["Adecuar a la cultura", "Es un enfoque"]),
             ("Derechos humanos", ["Salud como derecho"]),
             ("Género", ["Equidad"]),
             ("Territorial", ["Según el lugar"]),
             ("Promoción", ["Es una acción, no enfoque"])],
   "ruta": ["Población diversa", "Cuidado integral", "Enfoque transversal", "INTERCULTURALIDAD"]},
  ["Rehabilitación y recuperación son tipos de intervención.",
   "El MCI organiza el cuidado por curso de vida.",
   "Incluye la participación de la comunidad."],
  "MINSA – Modelo de Cuidado Integral de Salud por Curso de Vida (RM 030-2020)")

# GIN-235 · matriz
V("matriz", "GIN-235", "histerectomia-vaginal-previa-punto-c-mas-6-cupula", "Compartimentos del prolapso",
  "GINECOLOGÍA ENAM: PROLAPSO DE CÚPULA", "GINECOLOGÍA",
  ("Sistema POP-Q", ["Cada punto mide un compartimento vaginal respecto al himen",
   "Punto C: cuello uterino o cúpula si no hay útero"]),
  ("Mujer de 55 años, G5 P5005", ["Histerectomía vaginal hace 5 años", "Bulto vaginal · punto C +6"]),
  {"rotulo": "Punto y prolapso", "eje_x": "Dato", "eje_y": "Pared",
   "cols": ["Puntos", "Prolapso"], "rows": ["Anterior", "Apical", "Posterior"], "caso": (1, 1),
   "cells": [[("Aa y Ba", []), ("Cistocele", ["Uretrocele si es Aa"])],
             [("C (y D)", ["Sin útero: cúpula"]), ("CÚPULA VAGINAL", ["Tras histerectomía"])],
             [("Ap y Bp", []), ("Rectocele", ["Enterocele alto"])]]},
  ["Valores positivos: por fuera del himen.",
   "Tratamiento: colposacropexia o fijación sacroespinosa.",
   "Pesario si no desea o no puede operarse."],
  "ACOG – Practice Bulletin 214: Pelvic organ prolapse (2019) · Bump RC. AJOG (1996)")

# SP-174 · tarjetas
V("tarjetas", "SP-174", "cirujano-curacion-sin-guantes-no-maleficencia", "Principios de la bioética",
  "SALUD PÚBLICA ENAM: NO MALEFICENCIA", "SALUD PÚBLICA",
  ("No maleficencia", ["«Primero, no hacer daño»",
   "Incumplir la bioseguridad expone al paciente a infecciones"]),
  ("Cirujano de guardia", ["Cura una herida cortante sin usar guantes"]),
  {"rotulo": "¿Qué principio falla?", "ans": 0, "cards": [
      {"titulo": "NO MALEFICENCIA", "datos": [
          ("Idea", "No dañar", True), ("En el caso", "Sin guantes", True),
          ("Riesgo", "Infección", True)],
       "pie": "Bioseguridad"},
      {"titulo": "Beneficencia", "datos": [
          ("Idea", "Hacer el bien", False), ("En el caso", "Curar la herida", False),
          ("Riesgo", "—", False)],
       "pie": "Sí se cumple"},
      {"titulo": "Autonomía", "datos": [
          ("Idea", "Decidir", False), ("En el caso", "No se afecta", False),
          ("Riesgo", "—", False)],
       "pie": "Consentimiento"},
      {"titulo": "Justicia", "datos": [
          ("Idea", "Equidad", False), ("En el caso", "No se afecta", False),
          ("Riesgo", "—", False)],
       "pie": "Recursos"}]},
  ["Los guantes protegen al paciente y al personal.",
   "Técnica aséptica en toda curación.",
   "El error por descuido también es maleficencia."],
  CMP + " · Beauchamp y Childress. Principios de ética biomédica 8.ª ed.")

# CB-083 · matriz
V("matriz", "CB-083", "amoxicilina-30-minutos-habones-hipersensibilidad-tipo-i", "Tipos de hipersensibilidad",
  "CIENCIAS BÁSICAS ENAM: HIPERSENSIBILIDAD", "CIENCIAS BÁSICAS",
  ("Clasificación de Gell y Coombs", ["Cuatro mecanismos inmunitarios de daño",
   "Tipo I: inmediato, IgE y mastocitos (urticaria, anafilaxia)"]),
  ("Escolar de 7 años con amoxicilina", ["A los 30 minutos: habones pruriginosos", "Tronco y extremidades"]),
  {"rotulo": "Tipo y mecanismo", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["Mediador", "Tiempo"], "rows": ["I", "II", "III", "IV"], "caso": (0, 1),
   "cells": [[("IgE, mastocito", []), ("MINUTOS", ["Urticaria, anafilaxia"])],
             [("IgG contra célula", []), ("Horas", ["Hemólisis"])],
             [("Inmunocomplejos", []), ("Días", ["Enfermedad del suero"])],
             [("Linfocitos T", []), ("48-72 h", ["Dermatitis de contacto"])]]},
  ["Tratar con antihistamínico y suspender el fármaco.",
   "Si hay compromiso respiratorio: adrenalina IM.",
   "Registrar la alergia en la historia clínica."],
  "Abbas. Inmunología celular y molecular 10.ª ed. (2022)")

# PSI-042 · embudo
V("embudo", "PSI-042", "atracones-vomitos-autoprovocados-arritmia-hipopotasemia", "Alteraciones por vómitos",
  "PSIQUIATRÍA ENAM: BULIMIA NERVIOSA", "PSIQUIATRÍA",
  ("Bulimia nerviosa", ["Atracones seguidos de conductas compensatorias (vómitos, laxantes)",
   "Complicación electrolítica más frecuente: hipopotasemia"]),
  ("Escolar de 12 años", ["Atracones y vómitos autoprovocados por 1 año", "Ruidos cardiacos arrítmicos"]),
  {"rotulo": "Embudo del trastorno",
   "inicio": "Vómitos repetidos",
   "candidatos": ["Hipopotasemia", "Hipernatremia", "Hipercalcemia", "Hipermagnesemia"],
   "pasos": [("Se pierde ácido y potasio gástrico", ["Hipercalcemia", "Hipermagnesemia"]),
             ("Alcalosis y aldosterona: más K⁺ en orina", ["Hipernatremia"])],
   "final": ("HIPOPOTASEMIA", ["Con alcalosis metabólica hipoclorémica", "Riesgo de arritmias"]),
   "nota": "Las arritmias del caso orientan a hipopotasemia: pedir ECG y electrolitos."},
  ["Signo de Russell: callos en el dorso de la mano.",
   "Erosión dental y agrandamiento parotídeo.",
   "Tratamiento: terapia cognitivo-conductual y fluoxetina."],
  "APA – DSM-5-TR (2022) · NICE – Eating disorders (2020)")

# CIR-114 · tarjetas
V("tarjetas", "CIR-114", "injerto-arterial-acceso-percutaneo-femoral-comun", "Accesos arteriales percutáneos",
  "CIRUGÍA ENAM: ACCESO VASCULAR", "CIRUGÍA",
  ("Acceso arterial percutáneo", ["Se prefiere una arteria grande, superficial y comprimible",
   "La femoral común es la de elección en procedimientos endovasculares"]),
  ("Pregunta de cirugía vascular", ["¿Qué arteria se usa para el acceso percutáneo?"]),
  {"rotulo": "¿Qué acceso se elige?", "ans": 0, "cards": [
      {"titulo": "FEMORAL COMÚN", "datos": [
          ("Calibre", "Grande", True), ("Compresión", "Sobre la cabeza femoral", True),
          ("Uso", "De elección", True)],
       "pie": "Punción bajo el ligamento inguinal"},
      {"titulo": "Radial", "datos": [
          ("Calibre", "Pequeño", False), ("Compresión", "Fácil", False),
          ("Uso", "Coronariografía", False)],
       "pie": "Menos sangrado"},
      {"titulo": "Humeral", "datos": [
          ("Calibre", "Mediano", False), ("Compresión", "Difícil", False),
          ("Uso", "Alternativa", False)],
       "pie": "Riesgo de lesionar nervio"},
      {"titulo": "Ilíaca externa", "datos": [
          ("Calibre", "Grande", False), ("Compresión", "Imposible", False),
          ("Uso", "No percutánea", False)],
       "pie": "Hematoma retroperitoneal"}]},
  ["Punción alta: sangrado retroperitoneal.",
   "Punción baja: pseudoaneurisma o fístula.",
   "La carótida no se usa como acceso rutinario."],
  "Rutherford's Vascular Surgery 10.ª ed. (2022)")

# NEF-087 · árbol
A("NEF-087", "criptorquidia-operada-masa-testicular-solida-bhcg", "Masa testicular sólida",
  "UROLOGÍA ENAM: CÁNCER DE TESTÍCULO", "UROLOGÍA",
  ("Tumor testicular", ["Masa sólida en varón joven: cáncer hasta demostrar lo contrario",
   "Marcadores antes de operar: β-hCG, AFP y LDH"]),
  ("Varón de 35 años", ["Criptorquidia operada en la infancia", "Masa testicular sólida de 5 cm"]),
  Q("¿Masa sólida en la ecografía?", [
      Q("¿Sospecha de tumor germinal?", [
          L("Sí", "MARCADORES (β-hCG)", ["β-hCG, AFP y LDH", "Luego orquiectomía inguinal"], path=True),
          L("No", "Seguimiento", ["Lesión benigna"])],
        edge="Sí", path=True),
      L("No: quística", "Hidrocele o espermatocele", ["Transiluminación positiva"])], path=True),
  ("Marcadores", [("Seminoma", True), ("No seminoma", False)], [
      ("β-hCG", ["Puede elevarse", "Elevada"]),
      ("AFP", ["Normal", "Elevada (saco vitelino)"])]),
  ["Nunca biopsiar por vía escrotal.",
   "Criptorquidia: riesgo aumenta aun tras la orquidopexia.",
   "PSA es de próstata y CA 125 de ovario."],
  "EAU – Guidelines on testicular cancer (2024) · Campbell-Walsh Urology 12.ª ed.")

# SP-175 · puntaje
V("puntaje", "SP-175", "codigo-etica-riesgo-mayor-consentimiento-escrito", "Consentimiento informado",
  "SALUD PÚBLICA ENAM: AUTONOMÍA", "SALUD PÚBLICA",
  ("Consentimiento informado", ["Expresa el principio de autonomía",
   "Escrito si el procedimiento tiene riesgo mayor que el mínimo"]),
  ("Pregunta de ética", ["Artículo del Código de Ética del CMP", "¿Con qué principio se relaciona?"]),
  {"rotulo": "Requisitos del consentimiento", "escala": "Requisitos", "total": 5, "max": 5,
   "total_label": "Requisitos cumplidos",
   "interpreta": "Consentimiento válido: autonomía",
   "items": [("Información suficiente", "1", True), ("Comprensión", "1", True),
             ("Voluntariedad", "1", True), ("Capacidad para decidir", "1", True),
             ("Por escrito si hay riesgo", "1", True)],
   "bandas": [("< 5", "Incompleto", "No es válido", False),
              ("5 de 5", "Válido", "Respeta la autonomía", True)]},
  ["El paciente puede revocarlo en cualquier momento.",
   "En menores firman los padres; el niño da su asentimiento.",
   "Emergencia vital: se actúa sin demora y se deja constancia."],
  CMP + " · Ley 29414 de derechos de los usuarios de salud")

# INF-105 · árbol
A("INF-105", "interno-corte-palma-emergencia-exposicion-ocupacional", "Accidente con material cortante",
  "INFECTOLOGÍA ENAM: EXPOSICIÓN OCUPACIONAL", "INFECTOLOGÍA",
  ("Exposición ocupacional", ["Contacto con sangre o fluidos durante el trabajo asistencial",
   "Lavado, reporte y profilaxis posexposición en < 72 horas"]),
  ("Interno de medicina en emergencia", ["Corte en la palma durante una atención", "¿Cómo se clasifica la exposición al VIH?"]),
  Q("¿Ocurrió durante el trabajo asistencial?", [
      Q("¿Contacto con sangre o fluido de riesgo?", [
          L("Sí", "EXPOSICIÓN OCUPACIONAL", ["Lavar con agua y jabón", "Reportar y evaluar la fuente"], path=True),
          L("No", "Sin riesgo", ["Solo curación"])],
        edge="Sí", path=True),
      L("No", "Exposición no ocupacional", ["Sexual o por otras vías"])], path=True),
  ("Conducta", [("Hacer", True), ("No hacer", False)], [
      ("Herida", ["Lavar con agua y jabón", "Exprimir o usar lejía"]),
      ("VIH", ["TAR 28 días si la fuente es de riesgo", "Esperar el resultado de la fuente"])]),
  ["Iniciar la profilaxis idealmente en las primeras 2 horas.",
   "Pruebas basales de VIH, VHB y VHC al trabajador.",
   "Vacunar contra hepatitis B al personal de salud."],
  "MINSA – NTS 204: Profilaxis posexposición al VIH (2023) · CDC (2025)")

# INF-106 · fases
V("fases", "INF-106", "chancro-curado-papulas-palmares-rpr-1-320-benzatinica", "Etapas de la sífilis",
  "INFECTOLOGÍA ENAM: SÍFILIS SECUNDARIA", "INFECTOLOGÍA",
  ("Sífilis adquirida", ["Primaria (chancro), secundaria (exantema) y latente",
   "La temprana se trata con una dosis de penicilina benzatínica"]),
  ("Varón de 23 años", ["Chancro indoloro que curó solo hace 2 meses", "Pápulas palmares · RPR 1/320 · TPHA +"]),
  {"rotulo": "Etapas de la sífilis", "ans": 1,
   "fases": [("Primaria", "3 semanas", "Chancro", ["Úlcera indolora"]),
             ("Secundaria", "2-3 meses", "SÍFILIS SECUNDARIA", ["Pápulas palmoplantares", "RPR alto"]),
             ("Latente", "Años", "Sin síntomas", ["Solo serología"]),
             ("Terciaria", "Décadas", "Gomas, aorta", ["Neurosífilis"])],
   "curvas": [("Título de RPR", ROSE, [0.1, 0.5, 0.95, 0.7, 0.4, 0.3, 0.25])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Penicilina benzatínica", True), ("Ceftriaxona", False), ("Azitromicina", False), ("Ciprofloxacino", False)]},
  ["Penicilina benzatínica 2,4 millones UI IM, dosis única.",
   "Latente tardía: una dosis semanal por 3 semanas.",
   "Controlar el RPR a los 6 y 12 meses."],
  "MINSA – NTS 204: ITS (2023) · CDC – STI Treatment Guidelines (2021)")

# GIN-236 · puntaje
V("puntaje", "GIN-236", "gestante-36-semanas-epigastralgia-i3-magnesio-referencia", "Preeclampsia con signos de severidad",
  "OBSTETRICIA ENAM: PREECLAMPSIA EN EL PRIMER NIVEL", "OBSTETRICIA",
  ("Preeclampsia con signos de severidad", ["Basta un criterio de severidad (PA, síntomas o laboratorio)",
   "En el primer nivel: sulfato de magnesio y referir"]),
  ("Gestante de 36 semanas en un I-3", ["Epigastralgia desde hace 1 hora", "PA 150/90 · LCF 140 · sin dinámica"]),
  {"rotulo": "Criterios de severidad en el caso", "escala": "Criterios", "total": 1, "max": 5,
   "total_label": "Criterios presentes",
   "interpreta": "Preeclampsia severa",
   "items": [("Epigastralgia o dolor en HCD", "1", True), ("PA ≥ 160/110", "0", False),
             ("Cefalea o visión borrosa", "0", False), ("Plaquetas < 100 000", "?", False),
             ("Transaminasas o creatinina altas", "?", False)],
   "bandas": [("0", "Sin severidad", "Control y referencia", False),
              ("≥ 1", "Con severidad", "Magnesio y referir", True)]},
  ["Sulfato de magnesio 4 g EV en 20 min + mantenimiento.",
   "Antihipertensivo si PA ≥ 160/110.",
   "Referir acompañada, con vía segura."],
  "MINSA – Guía de emergencias obstétricas (2023) · ACOG Practice Bulletin 222 (2020)")

# NEF-088 · termómetro
V("termometro", "NEF-088", "colico-lumbar-irradiado-genitales-analgesia-aine", "Manejo del cólico renal",
  "UROLOGÍA ENAM: CÓLICO RENAL", "UROLOGÍA",
  ("Cólico renal", ["Dolor lumbar cólico irradiado a genitales, hematuria",
   "Primero: analgesia (AINE); la conducta sobre el cálculo depende del tamaño"]),
  ("Mujer de 48 años con cuadros previos", ["Dolor lumbar derecho irradiado a genitales", "Orina oscura · puñopercusión positiva"]),
  {"rotulo": "Conducta según el cálculo",
   "niveles": [("< 5 mm", "Expulsión probable", ["Analgesia, esperar"]),
               ("5-10 mm", "Terapia expulsiva", ["Tamsulosina"]),
               ("> 10 mm", "Remoción", ["LEOC o ureteroscopia"]),
               ("Complicado", "Fiebre o anuria", ["Catéter doble J urgente"])],
   "caso_nivel": 0, "ruta_titulo": "Primer paso en este caso", "paso_label": "PASO",
   "pasos": [(1, "Analgesia con AINE", ["Diclofenaco o ketorolaco"], True),
             (2, "Hidratación normal", ["Sin forzar líquidos"], False),
             (3, "Ecografía o uroTAC", ["Tamaño y ubicación"], False)]},
  ["Los AINE reducen la presión en la vía urinaria.",
   "Opioide si el AINE no basta o está contraindicado.",
   "Antibiótico solo si hay infección."],
  "EAU – Guidelines on urolithiasis (2024) · Campbell-Walsh Urology 12.ª ed.")

# TRA-051 · fases
V("fases", "TRA-051", "fractura-expuesta-antibiotico-primera-hora", "Tiempos en la fractura abierta",
  "TRAUMATOLOGÍA ENAM: FRACTURA ABIERTA", "TRAUMATOLOGÍA",
  ("Fractura abierta", ["Comunicación del foco con el exterior: alto riesgo de infección",
   "Lo más importante: antibiótico precoz, en la primera hora"]),
  ("Pregunta de traumatología", ["¿Cuál es la medida más importante?"]),
  {"rotulo": "Tiempos del manejo", "ans": 0,
   "fases": [("Llegada", "< 1 hora", "ANTIBIÓTICO", ["Cefazolina ± gentamicina", "Antitetánica"]),
             ("Quirófano", "< 24 horas", "Lavado", ["Desbridamiento"]),
             ("Estabilizar", "Mismo acto", "Fijación", ["Externa o interna"]),
             ("Cierre", "Días", "Cobertura", ["Colgajos si falta piel"])],
   "curvas": [("Riesgo de infección", ROSE, [0.2, 0.35, 0.5, 0.6, 0.7, 0.8, 0.9])],
   "chips_titulo": "Medida clave · marcada la correcta",
   "chips": [("Antibiótico temprano", True), ("Fijación externa", False), ("Tracción", False), ("Inmunización pasiva", False)]},
  ["Clasificación de Gustilo-Anderson: I, II y III.",
   "Tipo III: agregar cobertura para gramnegativos.",
   "No cerrar primariamente heridas contaminadas."],
  "BOAST 4: Open fractures (2017) · " + ATLS)

# NEF-089 · embudo
V("embudo", "NEF-089", "pielonefritis-10-dias-persiste-fiebre-absceso-renal", "Pielonefritis que no mejora",
  "UROLOGÍA ENAM: ABSCESO RENAL", "UROLOGÍA",
  ("Pielonefritis sin mejoría", ["Si la fiebre persiste 48-72 h con antibiótico adecuado",
   "Buscar complicaciones: obstrucción o absceso (TC)"]),
  ("Varón de 28 años", ["10 días de fiebre y dolor en fosa renal izquierda", "E. coli sensible · no mejora con el tratamiento"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Pielonefritis que no responde",
   "candidatos": ["Absceso renal", "Prostatitis", "TB renal", "Cáncer renal"],
   "pasos": [("Clínica de fosa renal, no prostática", ["Prostatitis"]),
             ("Cuadro agudo con germen común", ["TB renal", "Cáncer renal"])],
   "final": ("ABSCESO RENAL", ["TC con contraste para confirmar", "Drenaje percutáneo si > 5 cm"]),
   "nota": "Los abscesos pequeños (< 3 cm) suelen curar solo con antibióticos."},
  ["Factores: diabetes, litiasis, obstrucción.",
   "La ecografía descarta hidronefrosis.",
   "La TB renal es insidiosa, con piuria estéril."],
  "EAU – Guidelines on urological infections (2024) · " + HARRISON)

# NEU-068 · matriz
V("matriz", "NEU-068", "neumonia-atipica-mycoplasma-sin-pared-azitromicina", "Neumonía típica y atípica",
  "NEUMOLOGÍA ENAM: NEUMONÍA ATÍPICA", "NEUMOLOGÍA",
  ("Neumonía atípica", ["Mycoplasma, Chlamydophila, Legionella: sin pared o intracelulares",
   "No responden a betalactámicos: macrólido (azitromicina)"]),
  ("Pregunta de tratamiento", ["Sospecha clínica de neumonía atípica", "¿Qué antibiótico indicar?"]),
  {"rotulo": "Tipo y tratamiento", "eje_x": "Rasgo", "eje_y": "Neumonía",
   "cols": ["Agente", "Antibiótico"], "rows": ["Típica", "Atípica"], "caso": (1, 1),
   "cells": [[("Neumococo", ["Consolidación lobar"]), ("Amoxicilina", ["Betalactámico"])],
             [("Mycoplasma", ["Tos seca, infiltrado intersticial"]), ("AZITROMICINA", ["Macrólido o doxiciclina"])]]},
  ["Clínica: febrícula, tos seca, cefalea, poco hallazgo físico.",
   "Mycoplasma puede dar crioaglutininas y miringitis.",
   "En adultos también sirve una quinolona respiratoria."],
  "ATS/IDSA – Community-acquired pneumonia guideline (2019) · " + HARRISON)

# SP-176 · termómetro
V("termometro", "SP-176", "establecimiento-i4-upss-obligatoria-patologia-clinica", "Categorías del primer nivel",
  "SALUD PÚBLICA ENAM: CATEGORIZACIÓN", "SALUD PÚBLICA",
  ("Categorías del primer nivel", ["I-1 a I-4, de menor a mayor capacidad resolutiva",
   "Desde el I-3, patología clínica (laboratorio) es obligatoria"]),
  ("Pregunta de gestión", ["¿Qué UPSS es obligatoria en un I-4?"]),
  {"rotulo": "Categoría y UPSS",
   "niveles": [("I-1", "Profesional no médico", ["Sin UPSS obligatoria"]),
               ("I-2", "Con médico", ["Consulta externa"]),
               ("I-3", "Centro de salud", ["Consulta y patología clínica"]),
               ("I-4", "Con internamiento", ["PATOLOGÍA CLÍNICA", "Internamiento, farmacia"])],
   "caso_nivel": 3, "ruta_titulo": "UPSS obligatorias del I-4", "paso_label": "UPSS",
   "pasos": [(1, "Patología clínica", ["Laboratorio clínico"], True),
             (2, "Consulta externa y farmacia", ["Obligatorias"], False),
             (3, "Internamiento", ["Propio del I-4"], False)]},
  ["El centro quirúrgico es opcional en el I-4.",
   "Banco de sangre y UCI: segundo y tercer nivel.",
   "UPSS: unidad productora de servicios de salud."],
  "MINSA – NTS 021: Categorías de establecimientos del sector salud (2011)")

# CB-084 · fases
V("fases", "CB-084", "jardin-lesion-necrotica-hemolisis-anuria-loxosceles", "Evolución del loxoscelismo",
  "CIENCIAS BÁSICAS ENAM: LOXOSCELISMO", "CIENCIAS BÁSICAS",
  ("Loxoscelismo", ["Picadura de la araña casera (Loxosceles laeta)",
   "Forma cutáneo-visceral: hemólisis, hematuria e insuficiencia renal"]),
  ("Varón de 28 años, trabajó en el jardín", ["Lesión necrótica en el tobillo · anuria, hematuria", "Hb 8,5 · creatinina 3,8"]),
  {"rotulo": "Evolución tras la picadura", "ans": 1,
   "fases": [("Cutánea", "Primeras horas", "Placa livedoide", ["Dolor urente", "Necrosis"]),
             ("Visceral", "24-72 horas", "HEMÓLISIS", ["Hematuria, ictericia", "Falla renal"]),
             ("Secuela", "Semanas", "Úlcera", ["Cicatriz"])],
   "curvas": [("Hemólisis", ROSE, [0.05, 0.3, 0.8, 0.95, 0.6, 0.3, 0.1])],
   "chips_titulo": "Tratamiento inicial · marcado el correcto",
   "chips": [("Hidratación enérgica", True), ("Corticoides", False), ("Transfusión", False), ("Antibiótico tópico", False)]},
  ["La hidratación protege al riñón de la hemoglobinuria.",
   "Suero antiloxosceles en las primeras horas.",
   "Hemodiálisis si la falla renal progresa."],
  "MINSA – NTS 129: Manejo de accidentes por animales ponzoñosos (2016)")

# TRA-052 · árbol
A("TRA-052", "anciana-caida-codo-supracondilea-no-desplazada-ferula-90", "Fractura supracondílea en el adulto mayor",
  "TRAUMATOLOGÍA ENAM: FRACTURA SUPRACONDÍLEA", "TRAUMATOLOGÍA",
  ("Fractura distal del húmero", ["Mínimamente desplazada: manejo conservador",
   "Férula braquiopalmar posterior con el codo a 90°"]),
  ("Mujer de 70 años", ["Caída sobre el codo derecho", "Rx: fractura supracondílea lineal, mínimo desplazamiento"]),
  Q("¿Fractura desplazada o inestable?", [
      L("Sí", "Reducción y fijación", ["Placas y tornillos"]),
      Q("¿Estado neurovascular normal?", [
          L("Sí", "FÉRULA CON CODO A 90°", ["Braquiopalmar posterior", "3-4 semanas"], path=True),
          L("No", "Urgencia quirúrgica", ["Explorar arteria y nervios"])],
        edge="No", path=True)], path=True),
  ("Tipos de inmovilización", [("Codo distal", True), ("Diáfisis", False)], [
      ("Férula", ["Posterior, codo a 90°", "Colgante o de coaptación"]),
      ("Objetivo", ["Estabilizar la epífisis", "Alinear por gravedad"])]),
  ["Vigilar pulso radial y nervio mediano.",
   "Movilización precoz para evitar rigidez del codo.",
   "En niños: riesgo de contractura de Volkmann."],
  "Rockwood and Green's Fractures in Adults 10.ª ed. (2024)")
