"""Bloque 6 · parte I."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
GUYTON = "Guyton y Hall – Tratado de fisiología médica 14.ª ed. (2021)"

# GIN-121 · embudo
V("embudo", "GIN-121", "amenorrea-6-semanas-choque-culdocentesis-ectopico-roto", "Choque en mujer con amenorrea",
  "GINECOLOGÍA ENAM: EMBARAZO ECTÓPICO ROTO", "GINECOLOGÍA",
  ("Embarazo ectópico roto", ["Amenorrea + dolor abdominal + choque hipovolémico",
   "Culdocentesis positiva: sangre en el fondo de saco de Douglas"]),
  ("Mujer de 24 años que se desmayó", ["FUR hace 6 semanas · PA 80/50, FC 110", "Abdomen doloroso · culdocentesis (+)"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Amenorrea con dolor y choque",
   "candidatos": ["Ectópico roto", "Aborto incompleto", "Aborto en curso", "Cuerpo lúteo hemorrágico", "Apendicitis"],
   "pasos": [("Sangrado interno, no vaginal", ["Aborto incompleto", "Aborto en curso"]),
             ("Culdocentesis (+): hemoperitoneo", ["Apendicitis"]),
             ("Amenorrea de 6 semanas y choque grave", ["Cuerpo lúteo hemorrágico"])],
   "final": ("EMBARAZO ECTÓPICO ROTO", ["Hemoperitoneo con choque", "Laparotomía o laparoscopia urgente"]),
   "nota": "Inestable: no esperar la ecografía ni la β-hCG; reanimar y operar."},
  ["Sitio más frecuente: ampolla de la trompa.",
   "Factores: EPI previa, cirugía tubárica, DIU, ectópico previo.",
   "Metotrexato solo en ectópico no roto y estable."],
  "ACOG – Practice Bulletin N.° 193: Tubal ectopic pregnancy (2018) · MINSA – Guía de atención de emergencias obstétricas")

# SP-086 · termómetro
V("termometro", "SP-086", "autoexamen-mama-prevencion-secundaria", "Niveles de prevención",
  "SALUD PÚBLICA ENAM: PREVENCIÓN SECUNDARIA", "SALUD PÚBLICA",
  ("Prevención secundaria", ["Detección precoz en una etapa sin síntomas o inicial",
   "El autoexamen busca descubrir el cáncer de mama temprano"]),
  ("Pregunta de concepto", ["Autoexamen de mama", "¿Qué tipo de prevención es?"]),
  {"rotulo": "Niveles de prevención",
   "niveles": [("Primaria", "Evitar la enfermedad", ["Vacunas, estilos de vida"]),
               ("Secundaria", "Detectar temprano", ["Tamizaje, autoexamen"]),
               ("Terciaria", "Limitar el daño", ["Rehabilitación"]),
               ("Cuaternaria", "Evitar iatrogenia", ["Sobremedicalización"])],
   "caso_nivel": 1, "ruta_titulo": "Detección del cáncer de mama", "paso_label": "PASO",
   "pasos": [(1, "AUTOEXAMEN DE MAMA", ["Conocer las mamas; consultar si hay cambios"], True),
             (2, "Examen clínico de mamas", ["Por personal de salud"], False),
             (3, "Mamografía", ["Según edad y riesgo"], False)]},
  ["Todas las pruebas de detección precoz son prevención secundaria.",
   "El autoexamen tiene poca evidencia de reducir mortalidad, pero sí de alertar.",
   "Primaria: evitar obesidad, alcohol y promover la lactancia."],
  "MINSA – Plan nacional de prevención y control del cáncer de mama (2021) · Leavell y Clark – Niveles de prevención")

# CB-043 · tarjetas
V("tarjetas", "CB-043", "pielolitotomia-hipoestesia-muslo-anterior-nervio-femoral", "Nervios del miembro inferior",
  "CIENCIAS BÁSICAS ENAM: NERVIO FEMORAL", "CIENCIAS BÁSICAS",
  ("Nervio femoral (L2-L4)", ["Sensibilidad: cara anterior del muslo y medial de la pierna (safeno)",
   "Motor: cuádriceps; reflejo rotuliano"]),
  ("Varón de 63 años tras pielolitotomía derecha", ["Hipoestesia en la cara anterior del muslo", "Y en la cara medial de la pierna"]),
  {"rotulo": "¿Qué nervio se lesionó?", "ans": 0, "cards": [
      {"titulo": "FEMORAL", "datos": [
          ("Sensibilidad", "Muslo anterior, pierna medial", True), ("Motor", "Cuádriceps", True),
          ("Reflejo", "Rotuliano", True)],
       "pie": "Cerca del psoas en la cirugía renal"},
      {"titulo": "Ciático", "datos": [
          ("Sensibilidad", "Pierna y pie", False), ("Motor", "Isquiotibiales", False),
          ("Reflejo", "Aquiliano", False)],
       "pie": "Inyección glútea, cadera"},
      {"titulo": "Tibial", "datos": [
          ("Sensibilidad", "Planta del pie", False), ("Motor", "Flexión plantar", False),
          ("Reflejo", "Aquiliano", False)],
       "pie": "Túnel del tarso"},
      {"titulo": "Sural", "datos": [
          ("Sensibilidad", "Borde lateral del pie", False), ("Motor", "Ninguno", False),
          ("Reflejo", "Ninguno", False)],
       "pie": "Se usa para biopsia de nervio"}]},
  ["El nervio safeno es la rama sensitiva terminal del femoral.",
   "Lesión por separadores que comprimen el psoas.",
   "Obturador: cara medial del muslo y aductores."],
  "Moore – Anatomía con orientación clínica 9.ª ed. (2022)")

# END-034 · puntaje
V("puntaje", "END-034", "ketoconazol-hiperpigmentacion-hiponatremia-cortisol-bajo", "Insuficiencia suprarrenal por ketoconazol",
  "ENDOCRINOLOGÍA ENAM: INSUFICIENCIA SUPRARRENAL", "ENDOCRINOLOGÍA",
  ("Insuficiencia suprarrenal", ["El ketoconazol inhibe la síntesis de cortisol",
   "ACTH alta (hiperpigmentación) y sin aumento tras la estimulación"]),
  ("Mujer de 45 años con ketoconazol por 6 meses", ["Debilidad, vómitos, hipotensión ortostática", "Hiperpigmentación · Na 130, glucosa 65"]),
  {"rotulo": "Hallazgos en el caso", "escala": "Insuficiencia suprarrenal", "total": 6, "max": 7,
   "total_label": "Hallazgos presentes",
   "interpreta": "Cortisol disminuido",
   "items": [("Debilidad y pérdida de peso", "1", True), ("Náuseas, vómitos, dolor abdominal", "1", True),
             ("Hipotensión ortostática", "1", True), ("Hiperpigmentación", "1", True),
             ("Hiponatremia (130)", "1", True), ("Hipoglucemia (65)", "1", True),
             ("Hiperpotasemia", "1", False)],
   "bandas": [("0-2", "Poco probable", "Buscar otra causa", False),
              ("≥ 3", "Insuficiencia suprarrenal", "Hidrocortisona; suspender ketoconazol", True)]},
  ["Prueba de ACTH sin aumento de cortisol: insuficiencia suprarrenal.",
   "K normal: la aldosterona está menos afectada.",
   "En crisis: hidrocortisona 100 mg EV + suero salino con dextrosa."],
  "Endocrine Society – Diagnosis and treatment of primary adrenal insufficiency (2016) · " + HARRISON)

# CAR-048 · matriz
V("matriz", "CAR-048", "infarto-hipotension-iy-crepitantes-precarga-alta", "Hemodinamia de los tipos de choque",
  "CARDIOLOGÍA ENAM: CHOQUE CARDIOGÉNICO", "CARDIOLOGÍA",
  ("Choque cardiogénico", ["Falla de bomba: la sangre se acumula antes del corazón",
   "Precarga alta (IY, crepitantes), gasto bajo, resistencias altas"]),
  ("Varón de 50 años con dolor opresivo de 30 min", ["PA 80/50, piel fría, llenado > 5 s", "IY (+), crepitantes · troponina alta"]),
  {"rotulo": "Perfil hemodinámico", "eje_x": "Parámetro", "eje_y": "Choque",
   "cols": ["Precarga", "Gasto cardiaco", "RVS"], "rows": ["Hipovolémico", "Cardiogénico", "Distributivo", "Obstructivo"], "caso": (1, 0),
   "cells": [[("Baja", []), ("Bajo", []), ("Alta", [])],
             [("ALTA", ["IY +, crepitantes"]), ("Bajo", []), ("Alta", ["Piel fría"])],
             [("Baja o normal", []), ("Alto", []), ("Baja", ["Piel caliente"])],
             [("Alta", ["Taponamiento, TEP"]), ("Bajo", []), ("Alta", [])]]},
  ["No dar volumen a ciegas en el choque cardiogénico.",
   "Tratamiento: inotrópicos, vasopresor y revascularización urgente.",
   "Ecocardiograma para descartar complicaciones mecánicas."],
  "AHA – Contemporary management of cardiogenic shock (Circulation 2017) · ESC – ACS guidelines (2023)")

# SP-087 · embudo
V("embudo", "SP-087", "adulta-mayor-hijo-agresor-amenaza-denuncia", "Violencia contra la persona adulta mayor",
  "SALUD PÚBLICA ENAM: VIOLENCIA CONTRA EL ADULTO MAYOR", "SALUD PÚBLICA",
  ("Violencia contra el adulto mayor", ["Agresión física y amenaza de muerte: riesgo alto",
   "El médico debe denunciar ante las autoridades"]),
  ("Viuda de 81 años", ["Vive con su hijo alcohólico al que mantiene", "Agresiones físicas y amenazas de muerte"]),
  {"rotulo": "Embudo de conductas",
   "inicio": "Adulta mayor agredida por su hijo",
   "candidatos": ["Denunciar", "Terapia familiar", "Cambio de hábito", "Dar sedantes", "Avisar a la enfermera"],
   "pasos": [("Agresión física y amenaza de muerte: riesgo alto", ["Terapia familiar", "Cambio de hábito"]),
             ("Los sedantes no la protegen", ["Dar sedantes"]),
             ("La obligación es del médico", ["Avisar a la enfermera"])],
   "final": ("DENUNCIAR A LAS AUTORIDADES", ["Policía, fiscalía o CEM", "Medidas de protección"]),
   "nota": "Registrar las lesiones y el relato en la historia clínica."},
  ["Ley N.° 30490 de la persona adulta mayor.",
   "Ley N.° 30364: el personal de salud debe denunciar la violencia familiar.",
   "Evaluar riesgo de lesiones graves y necesidad de refugio."],
  "Ley N.° 30364 y su reglamento · Ley N.° 30490 · MINSA – Guía técnica de atención de la violencia familiar")

# PED-127 · árbol
A("PED-127", "neonato-febril-puncion-fallida-antibiotico-parenteral", "Neonato febril",
  "PEDIATRÍA ENAM: NEONATO FEBRIL", "PEDIATRÍA",
  ("Neonato febril", ["Alto riesgo de infección bacteriana grave",
   "El antibiótico no se retrasa si falla la punción lumbar"]),
  ("Neonato de 2 semanas", ["Fiebre 38.9 °C, irritable, succión débil", "Hemocultivo, orina y marcadores tomados · PL fallida"]),
  Q("¿Se logró la punción lumbar?", [
      L("Sí", "LCR + antibiótico", ["Cultivo y citoquímico"]),
      L("No, falló", "ANTIBIÓTICOS PARENTERALES", ["Iniciar ya", "Repetir la PL después"], path=True)], path=True),
  ("Esquema empírico", [("< 7 días", False), ("8-28 días", True)], [
      ("Fármacos", ["Ampicilina + gentamicina", "Ampicilina + cefotaxima"]),
      ("Si meningitis", ["Ampicilina + cefotaxima", "Dosis meníngeas"])]),
  ["Todo neonato febril se hospitaliza.",
   "El LCR sigue siendo útil hasta 24-48 h después del antibiótico.",
   "La TC o la ecografía no reemplazan la punción lumbar."],
  "AAP – Evaluation and management of well-appearing febrile infants 8 to 60 days (2021) · " + NELSON)

# SP-088 · radial
V("radial", "SP-088", "escenario-iii-dengue-alcalde-intersectorialidad", "Principios de la APS",
  "SALUD PÚBLICA ENAM: INTERSECTORIALIDAD", "SALUD PÚBLICA",
  ("Intersectorialidad", ["Varios sectores (municipio, educación, empresas) trabajan juntos",
   "Necesaria ante problemas como el dengue"]),
  ("Escenario III de dengue", ["El médico jefe convoca al alcalde", "Y a instituciones públicas y privadas"]),
  {"rotulo": "Mapa del tema", "centro": "APS", "centro_sub": "Principios", "ans": 0,
   "items": [("INTERSECTORIALIDAD", ["Alcalde e instituciones", "Acción conjunta"]),
             ("Equidad", ["Según necesidad"]),
             ("Participación", ["Comunidad organizada"]),
             ("Solidaridad", ["Apoyo mutuo"]),
             ("Justicia social", ["Derechos"])],
   "ruta": ["Escenario III de dengue", "Convoca al alcalde", "Sectores público y privado", "INTERSECTORIALIDAD"]},
  ["Escenario III: transmisión de dengue.",
   "El municipio lidera el recojo de inservibles.",
   "Salud no puede controlar el vector sola."],
  "OPS – La renovación de la APS en las Américas (2007) · MINSA – NTS N.° 211-MINSA/DGIESP-2024 (Dengue)")

# END-035 · embudo
V("embudo", "END-035", "cervicalgia-post-faringitis-vsg-58-de-quervain", "Tiroides dolorosa con tirotoxicosis",
  "ENDOCRINOLOGÍA ENAM: TIROIDITIS SUBAGUDA", "ENDOCRINOLOGÍA",
  ("Tiroiditis subaguda de De Quervain", ["Tras una infección viral: tiroides dolorosa + tirotoxicosis",
   "VSG alta, anticuerpos negativos, captación baja"]),
  ("Mujer de 48 años con 3 semanas de cervicalgia", ["Faringitis hace 2 meses · palpitaciones, baja de peso", "Tiroides dolorosa · TSH baja, T4 alta · VSG 58"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Tirotoxicosis con cuello doloroso",
   "candidatos": ["De Quervain", "Graves", "Hashimoto", "Facticia", "Tiroiditis supurativa"],
   "pasos": [("Tiroides dolorosa tras faringitis", ["Graves", "Facticia"]),
             ("Anti-TPO y antitiroglobulina negativos", ["Hashimoto"]),
             ("Sin masa fluctuante ni sepsis", ["Tiroiditis supurativa"])],
   "final": ("TIROIDITIS DE DE QUERVAIN", ["Subaguda granulomatosa", "AINE + propranolol"]),
   "nota": "Fases: tirotoxicosis → hipotiroidismo transitorio → recuperación."},
  ["Corticoide si el dolor no cede con AINE.",
   "No se usan antitiroideos: no hay síntesis aumentada.",
   "La captación de yodo está baja."],
  "ATA – Guidelines for hyperthyroidism and other causes of thyrotoxicosis (2016)")

# PSI-021 · termómetro
V("termometro", "PSI-021", "puerpera-22-dias-tristeza-autolesion-depresion-posparto", "Trastornos del ánimo en el puerperio",
  "PSIQUIATRÍA ENAM: DEPRESIÓN POSPARTO", "PSIQUIATRÍA",
  ("Depresión posparto", ["Episodio depresivo en las semanas tras el parto (> 2 semanas)",
   "Culpa, incapacidad para cuidar al bebé, ideas de autolesión"]),
  ("Puérpera de 36 años, 22 días tras su primer parto", ["Llanto, tristeza, miedo", "Se siente incapaz de cuidar al bebé · ideas de autolesión"]),
  {"rotulo": "Espectro en el puerperio",
   "niveles": [("< 2 sem", "Tristeza posparto", ["Leve, se resuelve sola"]),
               ("> 2 sem", "Depresión posparto", ["Incapacidad, culpa, autolesión"]),
               ("Delirios", "Psicosis posparto", ["Alucinaciones: urgencia"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Evaluar riesgo de autolesión", ["Y riesgo para el bebé"], False),
             (2, "PSICOTERAPIA + ISRS", ["Sertralina: compatible con lactancia"], True),
             (3, "Hospitalizar si el riesgo es alto", ["O hay psicosis"], False)]},
  ["Tamizaje con la escala de Edimburgo (EPDS).",
   "La tristeza posparto afecta al 50-80% y dura menos de 2 semanas.",
   "Psicosis posparto: pensar en trastorno bipolar."],
  "ACOG – Clinical Practice Guideline N.° 5: Perinatal depression (2023) · APA – DSM-5-TR (2022)")

# NEF-049 · tarjetas
V("tarjetas", "NEF-049", "litiasis-vesical-grande-cistolitotricia-laser", "Litiasis vesical: tratamiento",
  "NEFROLOGÍA ENAM: LITIASIS VESICAL", "NEFROLOGÍA",
  ("Litiasis vesical", ["Suele deberse a obstrucción del tracto de salida (HBP)",
   "Tratamiento de elección: cistolitotricia endoscópica transuretral"]),
  ("Pregunta de concepto", ["Litiasis vesical sintomática y grande", "que no responde a medidas conservadoras"]),
  {"rotulo": "¿Qué tratamiento es más eficaz?", "ans": 0, "cards": [
      {"titulo": "CISTOLITOTRICIA LÁSER", "datos": [
          ("Eficacia", "Alta (> 90%)", True), ("Uso", "Primera elección", True),
          ("Vía", "Endoscópica transuretral", True)],
       "pie": "Tratar también la causa (HBP)"},
      {"titulo": "LEOC", "datos": [
          ("Eficacia", "Menor", False), ("Uso", "Si no tolera cirugía", False),
          ("Vía", "Externa", False)],
       "pie": "Quedan fragmentos"},
      {"titulo": "Disolución médica", "datos": [
          ("Eficacia", "Solo ácido úrico", False), ("Uso", "Casos seleccionados", False),
          ("Vía", "Oral (alcalinizar)", False)],
       "pie": "Lenta"},
      {"titulo": "Anticolinérgicos", "datos": [
          ("Eficacia", "Ninguna", False), ("Uso", "No tratan el cálculo", False),
          ("Vía", "Oral", False)],
       "pie": "Pueden retener orina"}]},
  ["Cálculos muy grandes: cistolitotomía percutánea o abierta.",
   "Buscar y corregir la obstrucción del cuello vesical.",
   "Cuerpo extraño o sonda crónica también forman cálculos."],
  "EAU – Guidelines on urolithiasis: bladder stones (2024)")

# GIN-122 · puntaje
V("puntaje", "GIN-122", "vomitos-incoercibles-cetonuria-hiponatremia-hiperemesis", "Hiperémesis gravídica",
  "OBSTETRICIA ENAM: HIPERÉMESIS GRAVÍDICA", "OBSTETRICIA",
  ("Hiperémesis gravídica", ["Vómitos persistentes con deshidratación, cetosis y alteración electrolítica",
   "Pérdida de peso > 5%; requiere hospitalización"]),
  ("Segundigesta de 11 semanas", ["Vómitos incoercibles de 1 mes · baja 2 kg", "FC 100, PA 90/60, mucosas secas · cetonuria, Na 130"]),
  {"rotulo": "Criterios en el caso", "escala": "Hiperémesis", "total": 4, "max": 5,
   "total_label": "Criterios presentes",
   "interpreta": "Hiperémesis gravídica",
   "items": [("Vómitos persistentes", "1", True), ("Deshidratación", "1", True),
             ("Cetonuria", "1", True), ("Alteración electrolítica (Na 130)", "1", True),
             ("Pérdida de peso > 5%", "1", False)],
   "bandas": [("0-1", "NVE leve", "Dieta y doxilamina-piridoxina", False),
              ("≥ 2", "Hiperémesis", "Hospitalizar: fluidos, tiamina, antiemético EV", True)]},
  ["Tiamina antes de la dextrosa: previene la encefalopatía de Wernicke.",
   "Descartar embarazo molar o múltiple con ecografía.",
   "Puede cursar con hipertiroidismo transitorio (β-hCG alta)."],
  "ACOG – Practice Bulletin N.° 189: Nausea and vomiting of pregnancy (2018) · RCOG – Green-top Guideline N.° 69 (2024)")

# OFT-030 · embudo
V("embudo", "OFT-030", "sonda-nasogastrica-sangrado-tabique-anterior-kiesselbach", "Sangrado al pasar una sonda nasal",
  "OTORRINOLARINGOLOGÍA ENAM: PLEXO DE KIESSELBACH", "OTORRINOLARINGOLOGÍA",
  ("Plexo de Kiesselbach", ["Red vascular en el tabique nasal anterior (área de Little)",
   "Origen del 90% de las epistaxis"]),
  ("Pregunta de concepto", ["Localización más frecuente de sangrado", "al introducir una sonda nasogástrica"]),
  {"rotulo": "Embudo de opciones",
   "inicio": "Sangrado al introducir una sonda",
   "candidatos": ["Tabique anterior", "Tabique posterior", "Seno paranasal", "Vestíbulo nasal", "Cornete inferior"],
   "pasos": [("La sonda roza primero la parte anterior", ["Tabique posterior", "Seno paranasal"]),
             ("Mucosa muy vascular y expuesta", ["Vestíbulo nasal", "Cornete inferior"])],
   "final": ("TABIQUE NASAL ANTERIOR", ["Plexo de Kiesselbach", "Presión digital 10-15 min"]),
   "nota": "Lubricar la sonda y dirigirla hacia el piso nasal, no hacia arriba."},
  ["Arterias del plexo: etmoidal anterior, esfenopalatina, palatina mayor y labial superior.",
   "Epistaxis posterior (esfenopalatina): ancianos e hipertensos.",
   "Taponamiento anterior si la presión no basta."],
  "AAO-HNS – Clinical practice guideline: Nosebleed (epistaxis) (2020)")

# PED-128 · árbol
A("PED-128", "otitis-media-alergia-leve-amoxicilina-cefdinir", "Otitis media en niño alérgico a amoxicilina",
  "PEDIATRÍA ENAM: OTITIS MEDIA AGUDA", "PEDIATRÍA",
  ("Otitis media aguda", ["Tímpano abombado, opaco y poco móvil con fiebre",
   "Alergia leve (no anafiláctica) a amoxicilina: cefalosporina (cefdinir)"]),
  ("Niño de 3 años con fiebre 39.5 °C", ["Azitromicina 3 días sin mejoría · urticaria leve con amoxicilina", "Membrana timpánica amarilla, opaca, poco móvil"]),
  Q("¿Alergia a la penicilina?", [
      L("No", "Amoxicilina 80-90 mg/kg/día", ["10 días en < 2 años"]),
      Q("¿Qué tipo de reacción?", [
          L("Leve, no inmediata", "CEFDINIR", ["Cefalosporina oral"], path=True),
          L("Anafilaxia", "Clindamicina o macrólido", ["Sin betalactámicos"])],
        edge="Sí", path=True)], path=True),
  ("Si falla a las 48-72 h", [("Primera línea", False), ("Siguiente paso", True)], [
      ("Sin alergia", ["Amoxicilina", "Amoxicilina-clavulánico"]),
      ("Alergia leve", ["Cefdinir o cefuroxima", "Ceftriaxona IM 3 días"])]),
  ["Macrólidos: alta resistencia del neumococo.",
   "Cotrimoxazol no se recomienda para OMA.",
   "Paladar hendido aumenta el riesgo de otitis media."],
  "AAP – Clinical practice guideline: Acute otitis media (2013) · " + NELSON)

# TRA-023 · radial
V("radial", "TRA-023", "caida-mano-extendida-escafoides-arteria-radial", "Fractura de escafoides",
  "TRAUMATOLOGÍA ENAM: FRACTURA DE ESCAFOIDES", "TRAUMATOLOGÍA",
  ("Fractura de escafoides", ["La irrigación entra por el polo distal (rama de la arteria radial)",
   "Riesgo de necrosis avascular del polo proximal"]),
  ("Niño de 8 años que cae sobre la mano", ["Mano derecha extendida", "Fractura del escafoides"]),
  {"rotulo": "Mapa del tema", "centro": "ESCAFOIDES", "centro_sub": "Fractura", "ans": 0,
   "items": [("ARTERIA RADIAL", ["Irriga de distal a proximal", "Necrosis del polo proximal"]),
             ("Mecanismo", ["Caída con la mano extendida"]),
             ("Clínica", ["Dolor en la tabaquera anatómica"]),
             ("Rx", ["4 proyecciones; repetir a los 10-14 días"]),
             ("Tratamiento", ["Yeso con el pulgar incluido"])],
   "ruta": ["Caída sobre la mano", "Fractura del escafoides", "Rama de la radial", "ARTERIA RADIAL"]},
  ["El hueso del carpo que más se fractura.",
   "Rx normal con dolor en la tabaquera: inmovilizar y repetir o RM.",
   "Complicaciones: pseudoartrosis y necrosis avascular."],
  "AAOS – Scaphoid fractures (OrthoInfo 2023) · Moore – Anatomía con orientación clínica 9.ª ed. (2022)")

# NEF-050 · puntaje
V("puntaje", "NEF-050", "creatinina-5-anemia-8-meses-enfermedad-renal-cronica", "¿Falla renal aguda o crónica?",
  "NEFROLOGÍA ENAM: ENFERMEDAD RENAL CRÓNICA", "NEFROLOGÍA",
  ("Enfermedad renal crónica", ["Daño o TFG < 60 por más de 3 meses",
   "Anemia, HTA y evolución larga sugieren cronicidad"]),
  ("Mujer de 40 años con 8 meses de cansancio", ["PA 160/100, palidez, edema", "Hb 7.8 · creatinina 5 · urea 120"]),
  {"rotulo": "Datos de cronicidad en el caso", "escala": "Cronicidad", "total": 3, "max": 5,
   "total_label": "Datos presentes",
   "interpreta": "Enfermedad renal crónica (G5)",
   "items": [("Evolución > 3 meses (8 meses)", "1", True), ("Anemia marcada (Hb 7.8)", "1", True),
             ("HTA y edema", "1", True), ("Riñones pequeños en la ecografía", "1", False),
             ("Hiperfosfatemia e hipocalcemia", "1", False)],
   "bandas": [("0-1", "Sugiere aguda", "Buscar una causa aguda", False),
              ("≥ 2", "Crónica", "TFG < 15: preparar terapia de reemplazo", True)]},
  ["Anemia de la ERC: déficit de eritropoyetina.",
   "Pedir ecografía renal: riñones pequeños confirman cronicidad.",
   "Causas frecuentes: diabetes, HTA, glomerulopatías."],
  "KDIGO – Clinical practice guideline for the evaluation and management of CKD (2024)")

# GAS-046 · fases
V("fases", "GAS-046", "hbsag-igm-antihbc-positivos-hepatitis-b-aguda", "Serología de la hepatitis B",
  "GASTROENTEROLOGÍA ENAM: HEPATITIS B AGUDA", "GASTROENTEROLOGÍA",
  ("Hepatitis B aguda", ["HBsAg positivo + IgM anti-HBc positivo",
   "Anti-HBs aún negativo"]),
  ("Mujer de 50 años", ["HBsAg (+), IgM anti-HBc (+)", "Anti-HBc total (+) · anti-HBs (−)"]),
  {"rotulo": "Marcadores en el tiempo", "ans": 1,
   "fases": [("Incubación", "4-12 sem", "HBsAg aparece", ["Sin síntomas"]),
             ("Aguda", "1-3 meses", "HBsAg + IgM ANTI-HBc", ["Anti-HBs negativo"]),
             ("Ventana", "Semanas", "Solo IgM anti-HBc", ["HBsAg ya negativo"]),
             ("Curación", "> 6 meses", "Anti-HBs +", ["IgG anti-HBc"])],
   "curvas": [("HBsAg", ROSE, [0.2, 0.7, 0.9, 0.4, 0.05, 0.0, 0.0]),
              ("IgM", AMBER, [0.0, 0.3, 0.8, 0.9, 0.5, 0.2, 0.05]),
              ("Anti-HBs", SKY, [0.0, 0.0, 0.0, 0.1, 0.5, 0.8, 0.9])],
   "chips_titulo": "Fase · marcada la correcta",
   "chips": [("Aguda", True), ("Incubación", False), ("Recuperación", False), ("Convalecencia", False)]},
  ["HBsAg > 6 meses: hepatitis B crónica.",
   "El anti-HBc total incluye la IgM, por eso también es positivo.",
   "HBeAg positivo indica replicación activa."],
  "AASLD – Hepatitis B guidance (2018) · MINSA – NTS N.° 193-MINSA/DGIESP-2022 (Hepatitis B)")

# CAR-049 · árbol
A("CAR-049", "fa-pa-70-30-dolor-toracico-cardioversion-electrica", "Fibrilación auricular inestable",
  "CARDIOLOGÍA ENAM: FIBRILACIÓN AURICULAR INESTABLE", "CARDIOLOGÍA",
  ("Taquiarritmia inestable", ["Hipotensión, dolor torácico, alteración de conciencia o IC aguda",
   "Cardioversión eléctrica sincronizada inmediata"]),
  ("Varón de 54 años diabético y coronario", ["Dolor torácico, diaforesis, palpitaciones", "PA 70/30, FC 187 · ECG: fibrilación auricular"]),
  Q("¿Signos de inestabilidad?", [
      L("Sí: PA 70/30, dolor", "CARDIOVERSIÓN ELÉCTRICA", ["Sincronizada, con sedación"], path=True),
      Q("¿FA de < 48 horas?", [
          L("Sí", "Control de ritmo o FC", ["Betabloqueante, amiodarona"]),
          L("No o no se sabe", "Control de FC + anticoagular", ["3 semanas antes de cardiovertir"])],
        edge="No")], path=True),
  ("Signos de inestabilidad", [("Signo", True)], [
      ("Hemodinámico", ["Hipotensión, choque"]),
      ("Cardiaco", ["Dolor isquémico, IC aguda"]),
      ("Neurológico", ["Alteración de la conciencia"])]),
  ["Energía inicial en FA: 120-200 J bifásico.",
   "Verapamilo y digoxina no sirven en el paciente inestable.",
   "Anticoagular después según CHA₂DS₂-VASc."],
  "AHA – ACLS: Adult tachyarrhythmia with a pulse algorithm (2020, act. 2025) · ESC – AF guidelines (2024)")

# PSI-022 · puntaje
V("puntaje", "PSI-022", "palpitaciones-ahogo-muerte-inminente-ataque-panico", "Ataque de pánico: criterios",
  "PSIQUIATRÍA ENAM: ATAQUE DE PÁNICO", "PSIQUIATRÍA",
  ("Ataque de pánico", ["Miedo intenso súbito que alcanza su máximo en minutos",
   "Requiere ≥ 4 síntomas de una lista de 13 (DSM-5)"]),
  ("Mujer de 50 años", ["Palpitaciones, ahogo, sensación de muerte inminente", "Episodio similar hace 3 meses · examen cardiovascular normal"]),
  {"rotulo": "Síntomas DSM-5 en el caso", "escala": "DSM-5", "total": 4, "max": 13,
   "total_label": "Síntomas presentes",
   "interpreta": "Ataque de pánico (≥ 4)",
   "items": [("Palpitaciones", "1", True), ("Sudoración", "1", True), ("Temblor", "1", False),
             ("Sensación de ahogo", "1", True), ("Asfixia", "1", False), ("Dolor torácico", "1", False),
             ("Náuseas", "1", False), ("Mareo", "1", False), ("Escalofríos o calor", "1", False),
             ("Parestesias", "1", False), ("Desrealización", "1", False),
             ("Miedo a perder el control", "1", False), ("Miedo a morir", "1", True)],
   "bandas": [("< 4", "Síntomas limitados", "Buscar otra causa", False),
              ("≥ 4", "Ataque de pánico", "Descartar causa orgánica; ISRS + TCC si recurre", True)]},
  ["Trastorno de pánico: ataques recurrentes + preocupación por nuevos ataques.",
   "Descartar IAM, arritmias, hipertiroidismo y feocromocitoma.",
   "Benzodiacepinas solo por poco tiempo."],
  "APA – DSM-5-TR (2022) · NICE – Generalised anxiety disorder and panic disorder (2020)")

# NEU-032 · puntaje
V("puntaje", "NEU-032", "quimioterapia-disnea-subita-hemoptisis-tromboembolia", "Tromboembolia pulmonar: Wells",
  "NEUMOLOGÍA ENAM: TROMBOEMBOLIA PULMONAR", "NEUMOLOGÍA",
  ("Tromboembolia pulmonar", ["Disnea súbita, dolor pleurítico y hemoptisis",
   "Cáncer y quimioterapia son factores de riesgo mayores"]),
  ("Mujer de 65 años en quimioterapia por cáncer de mama", ["Disnea súbita, dolor torácico, hemoptisis", "Edema de MMII · ECG: VD dilatado"]),
  {"rotulo": "Escala de Wells en el caso", "escala": "Wells (TEP)", "total": 8, "max": 12.5,
   "total_label": "Puntaje del caso",
   "interpreta": "Probabilidad alta de TEP",
   "items": [("Signos de TVP", "3", True), ("TEP es el diagnóstico más probable", "3", True),
             ("FC > 100", "1.5", False), ("Inmovilización o cirugía reciente", "1.5", False),
             ("TVP o TEP previos", "1.5", False), ("Hemoptisis", "1", True),
             ("Cáncer activo", "1", True)],
   "bandas": [("0-1", "Baja", "Dímero D", False),
              ("2-6", "Intermedia", "Dímero D o angio-TC", False),
              ("> 6", "Alta", "Angio-TC; anticoagular sin esperar", True)]},
  ["Con hipotensión persistente (TEP de alto riesgo): trombólisis.",
   "Rx con «joroba de Hampton» o signo de Westermark.",
   "En cáncer: HBPM o anticoagulante oral directo."],
  "ESC – Guidelines for the diagnosis and management of acute pulmonary embolism (2019)")

# OFT-031 · radial
V("radial", "OFT-031", "glaucoma-betabloqueante-topico-timolol", "Fármacos para el glaucoma",
  "OFTALMOLOGÍA ENAM: TRATAMIENTO DEL GLAUCOMA", "OFTALMOLOGÍA",
  ("Tratamiento del glaucoma", ["Bajar la presión intraocular para proteger el nervio óptico",
   "Betabloqueantes tópicos (timolol): reducen la producción de humor acuoso"]),
  ("Pregunta de concepto", ["Fármaco común para bajar la PIO", "en pacientes con glaucoma"]),
  {"rotulo": "Mapa del tema", "centro": "GLAUCOMA", "centro_sub": "Bajar la PIO", "ans": 0,
   "items": [("BETABLOQUEANTES", ["Timolol", "↓ producción de humor acuoso"]),
             ("Prostaglandinas", ["Latanoprost: ↑ salida"]),
             ("Alfa-2 agonistas", ["Brimonidina"]),
             ("Inhibidores de AC", ["Dorzolamida, acetazolamida"]),
             ("Mióticos", ["Pilocarpina"])],
   "ruta": ["Glaucoma", "PIO alta", "Colirio hipotensor", "BETABLOQUEANTE"]},
  ["Timolol: evitar en asma, EPOC y bradicardia.",
   "Los corticoides tópicos pueden subir la PIO.",
   "Análogos de prostaglandinas: primera línea actual (una gota diaria)."],
  "AAO – Preferred Practice Pattern: Primary open-angle glaucoma (2020) · EGS – Terminology and guidelines 5.ª ed. (2020)")

# NEF-051 · fases
V("fases", "NEF-051", "orina-lavado-carne-amigdalitis-edema-furosemida", "Glomerulonefritis postestreptocócica",
  "NEFROLOGÍA ENAM: GLOMERULONEFRITIS POSTESTREPTOCÓCICA", "NEFROLOGÍA",
  ("Glomerulonefritis postestreptocócica", ["Síndrome nefrítico 1-3 semanas tras faringitis",
   "Sobrecarga de volumen e HTA: furosemida + restricción de sal y agua"]),
  ("Varón de 15 años con amigdalitis hace 3 semanas", ["Orina «lavado de carne», oliguria, edema", "PA 160/85 · creatinina 3 · cilindros hemáticos"]),
  {"rotulo": "Curso de la enfermedad", "ans": 2,
   "fases": [("Infección", "Día 0", "Faringitis", ["Estreptococo del grupo A"]),
             ("Latencia", "1-3 sem", "Sin síntomas", ["Se forman complejos"]),
             ("Nefrítico", "Semana 3", "FUROSEMIDA", ["Edema, HTA, oliguria"]),
             ("Resolución", "6-8 sem", "C3 normal", ["Hematuria puede durar"])],
   "curvas": [("C3", SKY, [0.9, 0.9, 0.3, 0.2, 0.4, 0.7, 0.9]),
              ("Creat.", ROSE, [0.2, 0.2, 0.8, 0.9, 0.6, 0.35, 0.2])],
   "chips_titulo": "Medida · marcada la correcta",
   "chips": [("Furosemida", True), ("Suero fisiológico", False), ("Gluconato de calcio", False), ("Insulina", False)]},
  ["El suero fisiológico empeora la sobrecarga de volumen.",
   "Complemento C3 bajo que se normaliza a las 6-8 semanas.",
   "Si el C3 sigue bajo: pensar en otra glomerulonefritis."],
  "KDIGO – Clinical practice guideline for glomerular diseases (2021) · " + NELSON)

# SP-089 · radial
V("radial", "SP-089", "hipertensa-mismo-medico-5-anos-longitudinalidad", "Atributos de la atención primaria",
  "SALUD PÚBLICA ENAM: LONGITUDINALIDAD", "SALUD PÚBLICA",
  ("Longitudinalidad", ["Atención por el mismo profesional a lo largo del tiempo",
   "Crea confianza y mejora el control de las enfermedades crónicas"]),
  ("Adulta mayor con HTA hace 5 años", ["Acude cada 3 meses al centro de salud", "Siempre la atiende el mismo médico"]),
  {"rotulo": "Mapa del tema", "centro": "APS", "centro_sub": "Atributos (Starfield)", "ans": 0,
   "items": [("LONGITUDINALIDAD", ["El mismo médico en el tiempo", "Relación de confianza"]),
             ("Primer contacto", ["Puerta de entrada"]),
             ("Integralidad", ["Todas las necesidades"]),
             ("Coordinación", ["Con otros niveles"]),
             ("Enfoque familiar", ["Y comunitario"])],
   "ruta": ["HTA hace 5 años", "Controles trimestrales", "El mismo médico", "LONGITUDINALIDAD"]},
  ["Coordinación: integrar la atención entre niveles.",
   "Primer contacto: accesibilidad como puerta de entrada.",
   "Integralidad: atender todos los problemas, no solo la HTA."],
  "Starfield – Primary care: balancing health needs, services and technology (1998) · OPS – Redes integradas de servicios de salud (2010)")

# GIN-123 · tarjetas
V("tarjetas", "GIN-123", "gestante-8-semanas-bacteriuria-asintomatica-nitrofurantoina", "Bacteriuria asintomática en la gestante",
  "OBSTETRICIA ENAM: BACTERIURIA ASINTOMÁTICA", "OBSTETRICIA",
  ("Bacteriuria asintomática en el embarazo", ["Urocultivo ≥ 100 000 UFC sin síntomas",
   "Se trata siempre: evita la pielonefritis y el parto pretérmino"]),
  ("Gestante de 8 semanas asintomática", ["Control prenatal", "Urocultivo: E. coli > 100 000 UFC"]),
  {"rotulo": "¿Qué antibiótico?", "ans": 0, "cards": [
      {"titulo": "NITROFURANTOÍNA", "datos": [
          ("¿Segura?", "Sí", True), ("Precaución", "Evitar al término", True),
          ("Uso", "Bacteriuria y cistitis", True)],
       "pie": "5-7 días"},
      {"titulo": "Amoxicilina-clavulánico", "datos": [
          ("¿Segura?", "Sí", False), ("Precaución", "Resistencia de E. coli", False),
          ("Uso", "Según antibiograma", False)],
       "pie": "Alternativa"},
      {"titulo": "Cotrimoxazol", "datos": [
          ("¿Segura?", "Evitar", False), ("Precaución", "1.er trimestre y término", False),
          ("Uso", "Antifolato; kernícterus", False)],
       "pie": "No en la gestante"},
      {"titulo": "Gentamicina", "datos": [
          ("¿Segura?", "Evitar", False), ("Precaución", "Ototóxica fetal", False),
          ("Uso", "Pielonefritis grave", False)],
       "pie": "Parenteral"}]},
  ["Tamizaje con urocultivo en el primer control prenatal.",
   "Urocultivo de control 1-2 semanas después del tratamiento.",
   "Cefalexina o amoxicilina son alternativas según el antibiograma."],
  "ACOG – Clinical consensus N.° 4: Urinary tract infections in pregnant individuals (2023) · MINSA – Guía de atención prenatal")

# CIR-065 · árbol
A("CIR-065", "fracturas-costales-dobles-movimiento-paradojal-intubacion", "Tórax inestable",
  "CIRUGÍA ENAM: TÓRAX INESTABLE", "CIRUGÍA",
  ("Tórax inestable", ["Fractura de ≥ 3 costillas en 2 puntos: movimiento paradojal",
   "El problema es la contusión pulmonar subyacente"]),
  ("Mujer de 70 años tras accidente de tránsito", ["4.ª a 7.ª costillas fracturadas en 2 puntos, movimiento paradojal", "FR 30, SatO₂ 90%, PA 90/70"]),
  Q("¿Insuficiencia respiratoria?", [
      L("Sí: FR 30, SatO₂ 90, choque", "INTUBACIÓN Y VENTILACIÓN MECÁNICA", ["Estabiliza la pared desde dentro"], path=True),
      L("No", "O₂ + analgesia", ["Bloqueo intercostal o epidural"])], path=True),
  ("Tórax inestable", [("Hacer", True), ("Evitar", False)], [
      ("Vía aérea", ["Intubar si hay falla", "Esperar al agotamiento"]),
      ("Pared", ["Analgesia eficaz", "Vendaje circular apretado"]),
      ("Líquidos", ["Reponer con juicio", "Sobrecarga (edema)"])]),
  ["Edad avanzada y ≥ 3 costillas: mayor mortalidad.",
   "La contusión pulmonar empeora en 24-48 h.",
   "Fijación quirúrgica costal en casos seleccionados."],
  ATLS + " · EAST – Rib fracture guideline (2017)")

# PSI-023 · termómetro
V("termometro", "PSI-023", "litio-6-convulsiones-hemodialisis", "Intoxicación por litio",
  "PSIQUIATRÍA ENAM: INTOXICACIÓN POR LITIO", "PSIQUIATRÍA",
  ("Intoxicación por litio", ["Temblor, ataxia, disartria, confusión, convulsiones y arritmias",
   "Litio muy alto con síntomas neurológicos o falla renal: hemodiálisis"]),
  ("Mujer de 52 años con trastorno bipolar", ["Intento de suicidio: convulsiones, somnolencia, ataxia", "Litio 6 mEq/L · creatinina 1.8 · RC arrítmicos"]),
  {"rotulo": "Litio sérico (mEq/L)",
   "niveles": [("0.6-1.2", "Terapéutico", ["Rango de mantenimiento"]),
               ("1.5-2.5", "Leve", ["Temblor, náuseas"]),
               ("2.5-4", "Moderada", ["Confusión, ataxia"]),
               ("> 4", "Grave", ["Convulsiones, arritmias"])],
   "caso_nivel": 3, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Suspender litio + fluidos", ["Suero isotónico"], False),
             (2, "HEMODIÁLISIS", ["El litio se dializa muy bien"], True),
             (3, "Medir litio después", ["Rebote a las 6-12 h"], False)]},
  ["Los diuréticos (tiazidas) aumentan el litio: no usarlos.",
   "El carbón activado no adsorbe litio.",
   "IECA, AINE y deshidratación elevan los niveles."],
  "EXTRIP – Extracorporeal treatment for lithium poisoning (Clin J Am Soc Nephrol 2015) · Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# SP-090 · matriz
V("matriz", "SP-090", "ppd-11-mm-sano-causa-necesaria-no-suficiente", "Tipos de causa",
  "SALUD PÚBLICA ENAM: CAUSALIDAD", "SALUD PÚBLICA",
  ("Causa necesaria pero no suficiente", ["Sin M. tuberculosis no hay TB (necesaria)",
   "Pero infectarse no basta para enfermar (no suficiente)"]),
  ("Varón sano de 26 años", ["PPD de 11 mm: infectado", "No tiene la enfermedad"]),
  {"rotulo": "Necesaria × suficiente", "eje_x": "¿Suficiente?", "eje_y": "¿Necesaria?",
   "cols": ["Suficiente", "No suficiente"], "rows": ["Necesaria", "No necesaria"], "caso": (0, 1),
   "cells": [[("Siempre causa", ["Rara en la práctica"]), ("M. TUBERCULOSIS", ["Sin él no hay TB; no basta"])],
             [("Causa por sí sola", ["Hay otras vías"]), ("Factor de riesgo", ["Tabaco y cáncer"])]]},
  ["Solo 5-10% de los infectados desarrolla TB en su vida.",
   "Factores que ayudan a enfermar: VIH, desnutrición, diabetes.",
   "Modelo de Rothman: causas componentes y suficientes."],
  "Rothman – Causes (Am J Epidemiol 1976) · Gordis – Epidemiology 6.ª ed. (2019)")

# GIN-124 · matriz
V("matriz", "GIN-124", "29-semanas-percentil-8-doppler-umbilical-rciu-temprano", "Feto pequeño: PEG o RCIU",
  "OBSTETRICIA ENAM: RESTRICCIÓN DEL CRECIMIENTO TEMPRANA", "OBSTETRICIA",
  ("RCIU temprano", ["Antes de las 32 semanas: peso < p10 con Doppler umbilical alterado",
   "Origen placentario; asociado a preeclampsia"]),
  ("Gestante de 29 semanas asintomática", ["PA 130/90 · AU 24 cm", "Peso fetal p8 · Doppler umbilical alterado"]),
  {"rotulo": "Clasificación", "eje_x": "Aspecto", "eje_y": "Tipo",
   "cols": ["Criterio", "Doppler"], "rows": ["PEG", "RCIU temprano", "RCIU tardío"], "caso": (1, 0),
   "cells": [[("Peso p3-p10", ["Crecimiento normal"]), ("Normal", ["Pequeño sano"])],
             [("< 32 SEMANAS", ["p < 10 + Doppler alterado"]), ("Umbilical alterado", ["Placentario"])],
             [("≥ 32 semanas", ["p < 3 o p < 10 + Doppler"]), ("Cerebral media", ["Redistribución"])]]},
  ["El RCIU temprano se asocia a preeclampsia: vigilar la PA.",
   "Seguimiento con Doppler seriado.",
   "Corticoides si se prevé parto antes de las 34 semanas."],
  "ISUOG – Practice guidelines: Diagnosis and management of FGR (2020) · Gordijn et al. – Delphi consensus (2016)")

# NEF-052 · embudo
V("embudo", "NEF-052", "ibuprofeno-oliguria-creatinina-3-nefropatia-toxica", "Falla renal tras automedicación",
  "NEFROLOGÍA ENAM: NEFROTOXICIDAD POR AINE", "NEFROLOGÍA",
  ("Nefrotoxicidad por AINE", ["Vasoconstricción de la arteriola aferente + nefritis intersticial",
   "Riesgo alto en ancianos hipertensos"]),
  ("Mujer de 72 años hipertensa", ["Ibuprofeno por 10 días · oliguria", "Creatinina 3, K 6 · cilindros granulosos · riñones normales"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Falla renal aguda en anciana",
   "candidatos": ["Nefropatía tóxica", "Deshidratación", "Nefropatía diabética", "HTA mal controlada", "Obstrucción"],
   "pasos": [("Edema y PA alta: no está deshidratada", ["Deshidratación"]),
             ("Sin diabetes; glucosa 115", ["Nefropatía diabética"]),
             ("Inicio agudo tras ibuprofeno, riñones normales", ["HTA mal controlada", "Obstrucción"])],
   "final": ("NEFROPATÍA TÓXICA", ["Por AINE", "Suspender y vigilar potasio"]),
   "nota": "Evitar AINE en ancianos, falla renal, IC y uso de IECA o diuréticos."},
  ["«Triple golpe»: AINE + IECA/ARA II + diurético.",
   "Cilindros granulosos: necrosis tubular aguda.",
   "Tratar la hiperpotasemia de 6 mEq/L."],
  "KDIGO – Clinical practice guideline for acute kidney injury (2012) · " + HARRISON)

# TRA-024 · radial
V("radial", "TRA-024", "fractura-abierta-complicacion-infeccion", "Complicaciones de la fractura abierta",
  "TRAUMATOLOGÍA ENAM: FRACTURAS ABIERTAS", "TRAUMATOLOGÍA",
  ("Fractura abierta", ["El hueso comunica con el exterior: contaminación bacteriana",
   "Complicación más frecuente: infección (osteomielitis)"]),
  ("Pregunta de concepto", ["Complicación más común", "de las fracturas abiertas"]),
  {"rotulo": "Mapa del tema", "centro": "FRACTURA ABIERTA", "centro_sub": "Complicaciones", "ans": 0,
   "items": [("INFECCIÓN", ["La más frecuente", "Osteomielitis"]),
             ("Compartimental", ["Aun con herida abierta"]),
             ("Neurovascular", ["Explorar pulsos"]),
             ("Pseudoartrosis", ["Retardo de consolidación"]),
             ("Embolia grasa", ["Huesos largos"])],
   "ruta": ["Herida que llega al hueso", "Contaminación", "Riesgo según Gustilo", "INFECCIÓN"]},
  ["Antibiótico en la primera hora: cefazolina ± gentamicina.",
   "Lavado y desbridamiento en quirófano.",
   "El riesgo de infección sube con el grado de Gustilo."],
  "BOAST – Open fractures (2017, act. 2020) · Rockwood and Green's Fractures in Adults 10.ª ed. (2024)")

# GIN-125 · árbol
A("GIN-125", "meconio-espeso-lcf-100-cesarea-emergencia", "Bradicardia fetal con meconio espeso",
  "OBSTETRICIA ENAM: SUFRIMIENTO FETAL", "OBSTETRICIA",
  ("Estado fetal no tranquilizador", ["Bradicardia fetal persistente + meconio espeso",
   "Lejos del expulsivo: cesárea de emergencia"]),
  ("Multigesta de 39 semanas", ["LCF 100 · 3 cm, 70%, −3", "Rotura de membranas: meconio espeso"]),
  Q("¿Bradicardia fetal persistente?", [
      L("No", "Vigilar el trabajo de parto", ["Monitoreo continuo"]),
      Q("¿Parto inminente?", [
          L("No: 3 cm, −3", "CESÁREA DE EMERGENCIA", ["Neonatólogo en sala"], path=True),
          L("Sí: expulsivo", "Parto vaginal asistido", ["Fórceps o vacuum"])],
        edge="Sí: LCF 100", path=True)], path=True),
  ("Líquido meconial", [("Fluido", False), ("Espeso", True)], [
      ("Riesgo", ["Menor", "Aspiración de meconio"]),
      ("Conducta", ["Vigilar", "Parto pronto si FCF anormal"])]),
  ["FCF normal: 110-160 lpm.",
   "La inducción con oxitocina empeora la hipoxia.",
   "Reanimación intrauterina mientras se prepara la cesárea."],
  "ACOG – Practice Bulletin N.° 116: Management of intrapartum FHR tracings (2010, reafirmado 2021) · " + WILLIAMS)

# NEU-033 · fases
V("fases", "NEU-033", "alpinista-esputo-espumoso-sato2-75-oxigeno", "Edema pulmonar de altura",
  "NEUMOLOGÍA ENAM: EDEMA PULMONAR DE ALTURA", "NEUMOLOGÍA",
  ("Edema pulmonar de altura", ["Vasoconstricción pulmonar hipóxica: edema no cardiogénico",
   "Tratamiento: oxígeno y descenso; nifedipino como apoyo"]),
  ("Alpinista de 35 años bajado a Huaraz", ["Disnea, tos con esputo espumoso", "SatO₂ 75%, crepitantes · Rx: infiltrados, corazón normal"]),
  {"rotulo": "Evolución y manejo", "ans": 2,
   "fases": [("Ascenso", "> 2500 m", "Hipoxia", ["Vasoconstricción pulmonar"]),
             ("Edema", "Días 2-4", "Tos espumosa", ["Crepitantes, cianosis"]),
             ("Manejo", "Inmediato", "OXÍGENO", ["Meta SatO₂ > 90%"]),
             ("Refractario", "Horas", "Nifedipino", ["Cámara hiperbárica"])],
   "curvas": [("SatO₂", SKY, [0.9, 0.6, 0.4, 0.35, 0.7, 0.85, 0.9])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("Oxígeno", True), ("Ventilación mecánica", False), ("Furosemida", False), ("Seguir descendiendo", False)]},
  ["La furosemida no se usa: el paciente suele estar hipovolémico.",
   "Si no hay oxígeno disponible, descender es lo principal.",
   "Prevención: ascenso gradual; nifedipino en susceptibles."],
  "Wilderness Medical Society – Clinical practice guidelines for acute altitude illness (2024)")

# CIR-066 · tarjetas
V("tarjetas", "CIR-066", "motociclista-hipotension-fc-72-sin-sangrado-neurogenico", "Tipos de choque en trauma",
  "CIRUGÍA ENAM: CHOQUE NEUROGÉNICO", "CIRUGÍA",
  ("Choque neurogénico", ["Lesión medular alta: pierde el tono simpático",
   "Hipotensión sin taquicardia, piel caliente; no responde a cristaloides"]),
  ("Motociclista tras accidente hace 1 hora", ["PA 80/40, FC 72, pulsos buenos", "FAST negativo · sin sangrado · no responde a cristaloides"]),
  {"rotulo": "¿Qué choque es?", "ans": 0, "cards": [
      {"titulo": "NEUROGÉNICO", "datos": [
          ("FC", "Normal o baja (72)", True), ("Piel", "Caliente, pulsos buenos", True),
          ("Clave", "Sin sangrado, FAST (−)", True)],
       "pie": "Vasopresor; inmovilizar columna"},
      {"titulo": "Hipovolémico", "datos": [
          ("FC", "Taquicardia", False), ("Piel", "Fría, pálida", False),
          ("Clave", "Sangrado, FAST (+)", False)],
       "pie": "El más frecuente en trauma"},
      {"titulo": "Cardiogénico", "datos": [
          ("FC", "Variable", False), ("Piel", "Fría", False),
          ("Clave", "IY +, crepitantes", False)],
       "pie": "Contusión miocárdica"},
      {"titulo": "Obstructivo", "datos": [
          ("FC", "Taquicardia", False), ("Piel", "Fría", False),
          ("Clave", "IY +, neumotórax o taponamiento", False)],
       "pie": "Descomprimir"}]},
  ["En trauma, siempre descartar primero el choque hemorrágico.",
   "Atropina si hay bradicardia sintomática.",
   "Choque medular: pérdida de reflejos, no es lo mismo que neurogénico."],
  ATLS + " · AANS/CNS – Guidelines for acute cervical spine and spinal cord injuries (2013)")

# PED-129 · matriz
V("matriz", "PED-129", "crianza-aves-disenteria-bacilo-curvo-campylobacter-azitromicina", "Disentería en el niño",
  "PEDIATRÍA ENAM: DISENTERÍA POR CAMPYLOBACTER", "PEDIATRÍA",
  ("Disentería por Campylobacter", ["Bacilo gramnegativo curvo, asociado a aves de corral",
   "Tratamiento: SRO, paracetamol y azitromicina"]),
  ("Lactante de 11 meses con crianza de aves", ["Deposiciones con moco y sangre, fiebre 39 °C", "Ojos hundidos · coprocultivo: bacilo curvo gramnegativo"]),
  {"rotulo": "Germen y tratamiento", "eje_x": "Aspecto", "eje_y": "Germen",
   "cols": ["Fuente", "Antibiótico"], "rows": ["Campylobacter", "Shigella", "Salmonella", "E. coli O157"], "caso": (0, 1),
   "cells": [[("Aves de corral", ["Bacilo curvo"]), ("AZITROMICINA", ["+ SRO"])],
             [("Persona a persona", ["Dosis infectiva baja"]), ("Azitromicina o cipro", [])],
             [("Huevos, pollo", []), ("Solo < 3 meses o graves", [])],
             [("Carne poco cocida", ["Síndrome urémico"]), ("No dar antibiótico", [])]]},
  ["Nunca loperamida en niños con disentería.",
   "Campylobacter se asocia a Guillain-Barré.",
   "Rehidratación oral según el plan de AIEPI."],
  "OMS/OPS – AIEPI · IDSA – Clinical practice guidelines for infectious diarrhea (2017)")

# CB-044 · tarjetas
V("tarjetas", "CB-044", "discusion-taquicardia-hipertension-catecolaminas", "Reacción al estrés agudo",
  "CIENCIAS BÁSICAS ENAM: REACCIÓN AL ESTRÉS", "CIENCIAS BÁSICAS",
  ("Reacción simpática al estrés", ["Noradrenalina (terminales simpáticas) y adrenalina (médula suprarrenal)",
   "Aumentan la FC y la PA en segundos"]),
  ("Varón de 60 años tras una discusión", ["Taquicardia", "Presión arterial elevada"]),
  {"rotulo": "¿Qué lo media?", "ans": 0, "cards": [
      {"titulo": "NORADRENALINA Y ADRENALINA", "datos": [
          ("Origen", "Simpático y médula suprarrenal", True), ("Efecto", "↑ FC y PA", True),
          ("Rapidez", "Segundos", True)],
       "pie": "Lucha o huida"},
      {"titulo": "Acetilcolina", "datos": [
          ("Origen", "Parasimpático", False), ("Efecto", "↓ FC", False),
          ("Rapidez", "Segundos", False)],
       "pie": "Reposo y digestión"},
      {"titulo": "Cortisol", "datos": [
          ("Origen", "Corteza suprarrenal", False), ("Efecto", "Glucosa, PA", False),
          ("Rapidez", "Minutos a horas", False)],
       "pie": "Eje hipotálamo-hipófisis"},
      {"titulo": "Dopamina y serotonina", "datos": [
          ("Origen", "SNC", False), ("Efecto", "Ánimo, recompensa", False),
          ("Rapidez", "Variable", False)],
       "pie": "No median la taquicardia"}]},
  ["Receptores β1: aumentan FC y contractilidad.",
   "Receptores α1: vasoconstricción y aumento de la PA.",
   "La médula suprarrenal secreta sobre todo adrenalina (80%)."],
  GUYTON)

# NEU-034 · fases
V("fases", "NEU-034", "tb-bk-positivo-perfil-hepatico-antes-tratamiento", "Tuberculosis: antes de tratar",
  "NEUMOLOGÍA ENAM: INICIO DEL TRATAMIENTO DE TB", "NEUMOLOGÍA",
  ("Evaluación antes del tratamiento de TB", ["Isoniazida, rifampicina y pirazinamida son hepatotóxicas",
   "Perfil hepático basal antes de iniciar"]),
  ("Varón de 28 años", ["TB pulmonar", "BK en esputo (+++)"]),
  {"rotulo": "Plan de tratamiento", "ans": 0,
   "fases": [("Antes", "Día 0", "PERFIL HEPÁTICO", ["+ VIH, glucosa, creatinina"]),
             ("Fase 1", "2 meses", "HRZE diario", ["Fase intensiva"]),
             ("Fase 2", "4 meses", "HR", ["Fase de continuación"]),
             ("Control", "Mensual", "BK de control", ["Y perfil si hay síntomas"])],
   "curvas": [],
   "chips_titulo": "Examen · marcado el correcto",
   "chips": [("Perfil hepático", True), ("Repetir BK", False), ("PPD", False), ("TC pulmonar", False)]},
  ["Si las transaminasas suben > 5 veces (o > 3 con síntomas): suspender.",
   "El PPD no sirve cuando ya hay diagnóstico bacteriológico.",
   "Prueba de sensibilidad rápida a isoniazida y rifampicina."],
  "MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis) · OMS – Consolidated guidelines on TB treatment (2022)")
