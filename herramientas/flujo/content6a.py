"""Bloque 6 · parte A."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"

# NEU-023 · termómetro
V("termometro", "NEU-023", "crisis-asmatica-torax-silente-gravedad", "Crisis asmática: gravedad",
  "NEUMOLOGÍA ENAM: CRISIS ASMÁTICA GRAVE", "NEUMOLOGÍA",
  ("Gravedad de la crisis asmática", ["Se clasifica por habla, conciencia, FR, FC, SatO₂ y auscultación",
   "Tórax silente = obstrucción extrema: riesgo vital"]),
  ("Mujer de 23 años asmática, crisis de 3 horas", ["FC 130 · FR 32 · politirajes", "Silencio auscultatorio en ambos hemitórax"]),
  {"rotulo": "Nivel de gravedad",
   "niveles": [("Leve", "Leve-moderada", ["Habla en frases", "FC < 120, SatO₂ 90-95%"]),
               ("Grave", "Grave", ["Habla con palabras", "FC > 120, FR > 30, tirajes"]),
               ("Vital", "Riesgo vital", ["TÓRAX SILENTE", "Confusión, cianosis, bradicardia"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "O₂ + SABA/ipratropio + corticoide", ["Salbutamol nebulizado continuo, corticoide sistémico"], True),
             (2, "Sulfato de magnesio EV", ["Si no responde a la primera hora"], False),
             (3, "UCI: valorar intubación", ["Si agotamiento o hipercapnia"], False)]},
  ["La polipnea y los tirajes indican gravedad, pero el tórax silente indica riesgo vital.",
   "Una PaCO₂ normal o alta en crisis es signo de agotamiento.",
   "No se usan sedantes ni se espera a la espirometría."],
  "GINA – Global Strategy for Asthma Management and Prevention (2025)")

# GAS-030 · radial
V("radial", "GAS-030", "ulcera-gastrica-agresion-defensa-mucosa", "Úlcera péptica: por qué se produce",
  "GASTROENTEROLOGÍA ENAM: FISIOPATOLOGÍA DE LA ÚLCERA PÉPTICA", "GASTROENTEROLOGÍA",
  ("Úlcera péptica", ["Aparece cuando los factores agresivos superan a los defensivos",
   "Agresión: ácido, pepsina, H. pylori, AINE · Defensa: moco, bicarbonato, prostaglandinas"]),
  ("Varón de 44 años con endoscopia alta", ["Excoriación de la mucosa en la curvatura menor", "Cerca del antro y el píloro"]),
  {"rotulo": "Mapa del tema", "centro": "MUCOSA GÁSTRICA", "centro_sub": "Agresión vs defensa", "ans": 0,
   "items": [("DESEQUILIBRIO", ["Secreción ácida > protección", "Mecanismo básico"]),
             ("H. pylori", ["Principal causa", "Erradicar siempre"]),
             ("AINE", ["Inhiben prostaglandinas", "Segunda causa"]),
             ("Moco y bicarbonato", ["Barrera defensiva"]),
             ("Flujo sanguíneo", ["Repara el epitelio"])],
   "ruta": ["Lesión de la curvatura menor", "La defensa de la mucosa falla", "El ácido la daña", "DESEQUILIBRIO"]},
  ["La úlcera gástrica se asocia más a defensa disminuida; la duodenal, a hipersecreción.",
   "Toda úlcera gástrica se biopsia para descartar cáncer.",
   "Tratamiento: IBP y erradicación de H. pylori; suspender AINE."],
  "ACG – Treatment of Helicobacter pylori infection (Am J Gastroenterol 2024) · Sleisenger and Fordtran's Gastrointestinal and Liver Disease 11.ª ed. (2021)")

# CIR-052 · puntaje
V("puntaje", "CIR-052", "dolor-periumbilical-migratorio-alvarado-nino", "Apendicitis: escala de Alvarado",
  "CIRUGÍA ENAM: APENDICITIS AGUDA EN EL ESCOLAR", "CIRUGÍA",
  ("Apendicitis aguda", ["Dolor periumbilical que migra a la fosa iliaca derecha + anorexia + vómitos",
   "La escala de Alvarado ayuda a estimar la probabilidad"]),
  ("Escolar de 6 años con 12 h de dolor periumbilical", ["Anorexia, vómitos, sin diarrea", "Dolor a la palpación en FID"]),
  {"rotulo": "Escala de Alvarado en el caso", "escala": "Alvarado", "total": 5, "max": 10,
   "total_label": "Puntaje clínico (sin laboratorio)",
   "interpreta": "Clínica sugestiva: faltan fiebre y hemograma",
   "items": [("Dolor que migra a FID", "1", True), ("Anorexia", "1", True), ("Náuseas o vómitos", "1", True),
             ("Dolor en fosa iliaca derecha", "2", True), ("Rebote", "1", False), ("Fiebre ≥ 37.3 °C", "1", False),
             ("Leucocitosis > 10 000", "2", False), ("Desviación izquierda", "1", False)],
   "bandas": [("1-4", "Poco probable", "Observar, buscar otra causa", False),
              ("5-6", "Posible", "Hemograma, ecografía y cirujano", True),
              ("7-10", "Probable", "Apendicectomía", False)]},
  ["Diagnóstico clínico: la ecografía es el primer estudio en niños.",
   "Diarrea importante orienta a gastroenteritis; la invaginación es de lactantes.",
   "En menores de 5 años se perfora con más frecuencia."],
  "WSES – Jerusalem guidelines on acute appendicitis (World J Emerg Surg 2020) · " + NELSON)

# INF-038 · tarjetas
V("tarjetas", "INF-038", "strongyloides-heces-ivermectina", "Helmintos intestinales: tratamiento",
  "INFECTOLOGÍA ENAM: ESTRONGILOIDIASIS", "INFECTOLOGÍA",
  ("Tratamiento de los helmintos intestinales", ["Cada parásito tiene su fármaco de elección",
   "Strongyloides stercoralis: ivermectina"]),
  ("Análisis de heces de rutina", ["Hallazgo de Strongyloides stercoralis"]),
  {"rotulo": "¿Qué fármaco?", "ans": 0, "cards": [
      {"titulo": "STRONGYLOIDES", "datos": [
          ("Ciclo", "Autoinfección", True), ("Riesgo", "Hiperinfestación", True),
          ("Heces", "Larvas rabditiformes", False), ("Fármaco", "IVERMECTINA", True)],
       "pie": "200 µg/kg, 1-2 días"},
      {"titulo": "Ascaris", "datos": [
          ("Ciclo", "Paso pulmonar (Löffler)", False), ("Riesgo", "Obstrucción intestinal", False),
          ("Heces", "Huevos mamelonados", False), ("Fármaco", "Albendazol", False)],
       "pie": "Dosis única"},
      {"titulo": "Enterobius", "datos": [
          ("Ciclo", "Autoinfección perianal", False), ("Riesgo", "Prurito, vulvovaginitis", False),
          ("Heces", "Test de Graham", False), ("Fármaco", "Albendazol", False)],
       "pie": "Repetir a las 2 semanas"},
      {"titulo": "Taenia", "datos": [
          ("Ciclo", "Cerdo o vaca", False), ("Riesgo", "Cisticercosis (solium)", False),
          ("Heces", "Proglótides", False), ("Fármaco", "Praziquantel", False)],
       "pie": "Dosis única"}]},
  ["Strongyloides puede persistir décadas por autoinfección.",
   "Con corticoides o HTLV-1 puede causar hiperinfestación con sepsis por gramnegativos.",
   "Albendazol es alternativa, pero menos eficaz que ivermectina."],
  "CDC – Strongyloides: Clinical care (2024) · OMS – Guideline on preventive chemotherapy for soil-transmitted helminthiases (2017)")

# NEU-024 · embudo
V("embudo", "NEU-024", "epoc-disnea-subita-hiperresonancia-neumotorax", "Disnea súbita en el EPOC",
  "NEUMOLOGÍA ENAM: NEUMOTÓRAX ESPONTÁNEO SECUNDARIO", "NEUMOLOGÍA",
  ("Disnea súbita en un paciente con EPOC", ["La rotura de bullas enfisematosas causa neumotórax secundario",
   "Hiperresonancia y murmullo disminuido de un lado = neumotórax"]),
  ("Varón de 68 años con EPOC", ["Dolor torácico y disnea súbitos, sin mejoría con O₂", "SatO₂ 86% · hiperresonancia en hemitórax derecho"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "EPOC con disnea y dolor torácico",
   "candidatos": ["Neumotórax", "TEP", "Exacerbación", "Neumonía", "Infarto"],
   "pasos": [("Inicio súbito, sin fiebre ni esputo purulento", ["Exacerbación", "Neumonía"]),
             ("Hiperresonancia unilateral", ["TEP", "Infarto"])],
   "final": ("NEUMOTÓRAX ESPONTÁNEO SECUNDARIO", ["Rx de tórax confirma", "Tubo de drenaje y hospitalizar"]),
   "nota": "En el EPOC incluso un neumotórax pequeño se drena: la reserva respiratoria es mínima."},
  ["Neumotórax primario: joven alto y delgado, sin enfermedad pulmonar.",
   "Secundario: EPOC, fibrosis quística, TB, neumonía por Pneumocystis.",
   "Si hay hipotensión y desviación traqueal: descompresión inmediata."],
  "BTS – Guideline for pleural disease (Thorax 2023)")

# SP-055 · árbol
A("SP-055", "tamizaje-violencia-familiar-csmc", "Víctima de violencia: a dónde referir",
  "SALUD PÚBLICA ENAM: ATENCIÓN DE LA VIOLENCIA FAMILIAR", "SALUD PÚBLICA",
  ("Atención de víctimas de violencia", ["El tamizaje en el primer nivel detecta los casos",
   "La atención integral en salud mental la brinda el Centro de Salud Mental Comunitario"]),
  ("Tamizaje de violencia en el consultorio de la mujer", ["Alta incidencia de casos", "Se requiere atención integral especializada"]),
  Q("¿Hay lesiones graves o riesgo vital?", [
      L("Sí", "Emergencia hospitalaria", ["Estabilizar y denunciar"]),
      Q("¿Qué necesita la víctima?", [
          L("Salud mental", "CENTRO DE SALUD MENTAL COMUNITARIO", ["Atención integral especializada", "Psicología, psiquiatría, social"], path=True),
          L("Protección legal", "Centro Emergencia Mujer", ["Ministerio de la Mujer"])],
        edge="No", path=True)], path=True),
  ("Instancias de atención", [("CSMC", True), ("CEM", False), ("Hospital", False)], [
      ("Brinda", ["Salud mental comunitaria", "Protección y patrocinio legal", "Lesiones graves"]),
      ("Sector", ["MINSA", "Ministerio de la Mujer", "MINSA"])]),
  ["Los CSMC atienden violencia, adicciones y trastornos mentales en la comunidad.",
   "El personal de salud está obligado a denunciar (Ley 30364).",
   "El INSM y los hospitales de tercer nivel son para casos complejos referidos."],
  "Ley N.° 30364 – Prevenir, sancionar y erradicar la violencia contra las mujeres · MINSA – NTS de Centros de Salud Mental Comunitarios")

# GAS-031 · matriz
V("matriz", "GAS-031", "dolor-epigastrico-7-dias-lipasa", "Pancreatitis: amilasa o lipasa",
  "GASTROENTEROLOGÍA ENAM: DIAGNÓSTICO DE PANCREATITIS AGUDA", "GASTROENTEROLOGÍA",
  ("Enzimas pancreáticas", ["Diagnóstico: 2 de 3 (dolor típico, enzimas ≥ 3 veces, imagen)",
   "La lipasa es más específica y dura más tiempo elevada"]),
  ("Varón de 50 años con alcoholismo crónico", ["Dolor epigástrico irradiado a la espalda", "Desde hace 7 días"]),
  {"rotulo": "Amilasa vs lipasa", "eje_x": "Enzima", "eje_y": "Rasgo",
   "cols": ["Amilasa", "Lipasa"], "rows": ["Se eleva", "Se normaliza", "Especificidad"], "caso": (1, 1),
   "cells": [[("6-12 h", []), ("4-8 h", [])],
             [("3-5 días", ["A los 7 días puede ser normal"]), ("8-14 DÍAS", ["Sigue alta al día 7"])],
             [("Baja", ["Parótida, intestino, riñón"]), ("Alta", ["De elección"])]]},
  ["La cifra de la enzima no se relaciona con la gravedad.",
   "En la pancreatitis alcohólica la amilasa puede no elevarse.",
   "La TC solo si hay duda diagnóstica o tras 72 h si no mejora."],
  "ACG – Guideline: Management of acute pancreatitis (Am J Gastroenterol 2024)")

# CIR-053 · tarjetas
V("tarjetas", "CIR-053", "tumoracion-inguinoescrotal-hernia-indirecta", "Hernias de la pared abdominal",
  "CIRUGÍA ENAM: HERNIA INGUINAL INDIRECTA", "CIRUGÍA",
  ("Hernias de la región inguinal", ["La indirecta sigue el conducto inguinal y baja al escroto",
   "Es la más frecuente en ambos sexos"]),
  ("Albañil de 48 años", ["Tumoración inguinoescrotal izquierda reductible", "Valsalva (+)"]),
  {"rotulo": "¿Qué hernia es?", "ans": 0, "cards": [
      {"titulo": "INGUINAL INDIRECTA", "datos": [
          ("Orificio", "Anillo profundo", True), ("Relación", "Lateral a vasos epigástricos", False),
          ("Escroto", "Llega al escroto", True), ("Clave", "La más frecuente", True)],
       "pie": "Hernioplastia electiva"},
      {"titulo": "Inguinal directa", "datos": [
          ("Orificio", "Triángulo de Hesselbach", False), ("Relación", "Medial a vasos epigástricos", False),
          ("Escroto", "Rara vez", False), ("Clave", "Adulto mayor, esfuerzo", False)],
       "pie": "Debilidad de la fascia transversalis"},
      {"titulo": "Crural", "datos": [
          ("Orificio", "Anillo femoral", False), ("Relación", "Bajo el ligamento inguinal", False),
          ("Escroto", "No", False), ("Clave", "Mujer, se estrangula", False)],
       "pie": "Cirugía siempre"},
      {"titulo": "Eventración", "datos": [
          ("Orificio", "Cicatriz quirúrgica", False), ("Relación", "Pared anterior", False),
          ("Escroto", "No", False), ("Clave", "Laparotomía previa", False)],
       "pie": "Malla"}]},
  ["La maniobra de Valsalva hace protruir cualquier hernia.",
   "Las hernias sintomáticas se operan; en varones asintomáticos puede vigilarse.",
   "Irreductible y dolorosa: descartar estrangulación."],
  "HerniaSurge Group – International guidelines for groin hernia management (Hernia 2018; actualización 2023)")

# INF-039 · fases
V("fases", "INF-039", "fiebre-iquitos-prueba-lazo-dengue", "Dengue: fases de la enfermedad",
  "INFECTOLOGÍA ENAM: DENGUE", "INFECTOLOGÍA",
  ("Dengue", ["Fiebre alta, cefalea, dolor retroocular y mialgias tras estar en zona endémica",
   "La prueba del lazo positiva refleja fragilidad capilar"]),
  ("Varón de 28 años, visitó Iquitos hace 9 días", ["3 días de fiebre, cefalea y mialgias intensas", "Petequias al tomar la PA (lazo +)"]),
  {"rotulo": "Curso clínico", "ans": 0,
   "fases": [("Febril", "Días 1-3", "FIEBRE Y MIALGIAS", ["Prueba del lazo (+)", "NS1 positivo"]),
             ("Crítica", "Días 4-6", "Fuga plasmática", ["Signos de alarma, choque"]),
             ("Recuperación", "Días 7-10", "Reabsorción", ["Riesgo de sobrecarga"])],
   "curvas": [("Fiebre", ROSE, [0.9, 0.95, 0.8, 0.3, 0.15, 0.1, 0.05]),
              ("Hto", AMBER, [0.3, 0.3, 0.4, 0.8, 0.85, 0.5, 0.35])],
   "chips_titulo": "Diagnóstico · marcada la correcta",
   "chips": [("Dengue", True), ("Malaria", False), ("Fiebre amarilla", False), ("Leptospirosis", False)]},
  ["La fase crítica empieza al caer la fiebre: vigilar signos de alarma.",
   "Paracetamol para la fiebre; evitar AINE y aspirina.",
   "Malaria: fiebre con escalofríos periódicos; leptospirosis: pantorrillas y sufusión conjuntival."],
  "OPS – Directrices para el diagnóstico clínico y el tratamiento del dengue, chikungunya y zika (2022)")

# OFT-018 · termómetro
V("termometro", "OFT-018", "cefalea-tos-nocturna-rinosinusitis-subaguda", "Rinosinusitis: según duración",
  "OTORRINOLARINGOLOGÍA ENAM: SINUSITIS SUBAGUDA", "OTORRINOLARINGOLOGÍA",
  ("Rinosinusitis por tiempo de evolución", ["Aguda < 4 semanas · subaguda 4-12 · crónica > 12",
   "Descarga posterior purulenta y tos nocturna son típicas"]),
  ("Adolescente de 12 años con cefalea de 1 mes", ["Tos nocturna y rinorrea intermitente", "Secreción purulenta en pared posterior de la faringe"]),
  {"rotulo": "Duración de los síntomas",
   "niveles": [("< 4 sem", "Aguda", ["Viral en su mayoría"]),
               ("4-12 sem", "Subaguda", ["SINUSITIS SUBAGUDA", "Bacteriana persistente"]),
               ("> 12 sem", "Crónica", ["Pólipos, alergia, anatomía"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Amoxicilina ± clavulánico", ["Cubre neumococo, H. influenzae, Moraxella"], True),
             (2, "Lavados nasales con suero", ["Alivian la descarga posterior"], False),
             (3, "Imagen solo si hay complicación", ["TC si edema orbitario o signos neurológicos"], False)]},
  ["Bacteriana si: síntomas > 10 días sin mejoría, fiebre alta con pus o empeoramiento tras mejorar.",
   "La tos nocturna por descarga posterior es frecuente en niños.",
   "La Rx de senos no se recomienda de rutina."],
  "AAP – Clinical practice guideline: acute bacterial sinusitis in children (Pediatrics 2013) · EPOS – European position paper on rhinosinusitis (2020)")

# REU-024 · radial
V("radial", "REU-024", "vesiculas-dermatoma-vih-herpes-zoster", "Lesiones vesiculares",
  "DERMATOLOGÍA ENAM: HERPES ZÓSTER", "DERMATOLOGÍA",
  ("Lesiones vesiculares", ["Dolor urente y vesículas agrupadas en un dermatoma = herpes zóster",
   "Tzanck: células gigantes multinucleadas (herpesvirus)"]),
  ("Mujer de 64 años con VIH", ["Dolor urente en hemitórax izquierdo", "Vesículas siguiendo un dermatoma · Tzanck (+)"]),
  {"rotulo": "Mapa del tema", "centro": "VESÍCULAS", "centro_sub": "Según distribución", "ans": 0,
   "items": [("HERPES ZÓSTER", ["Un dermatoma, unilateral", "Dolor previo urente"]),
             ("Herpes simple", ["Agrupadas, labios o genitales", "Recurrente"]),
             ("Varicela", ["Generalizadas", "Distintos estadios"]),
             ("Dermatitis de contacto", ["Zona de contacto", "Prurito"]),
             ("Impétigo ampolloso", ["Costras mielicéricas"])],
   "ruta": ["Dolor urente previo", "Vesículas en un dermatoma", "Tzanck: células gigantes", "HERPES ZÓSTER"]},
  ["Aciclovir o valaciclovir en las primeras 72 h; en inmunodeprimidos siempre.",
   "El zóster en menores de 50 años puede ser la primera señal de VIH.",
   "Complicación más frecuente: neuralgia postherpética."],
  "Fitzpatrick's Dermatology 9.ª ed. (2019) · CDC – Clinical overview of shingles (2024)")

# GIN-080 · árbol
A("GIN-080", "fiebre-poscesarea-utero-doloroso-endometritis", "Fiebre en el puerperio",
  "OBSTETRICIA ENAM: ENDOMETRITIS PUERPERAL", "OBSTETRICIA",
  ("Fiebre puerperal", ["Fiebre ≥ 38 °C en dos tomas después de las primeras 24 h",
   "Útero doloroso y loquios purulentos = endometritis"]),
  ("Puérpera de 3 días poscesárea", ["Fiebre 38.5 °C en dos tomas", "Útero doloroso · secreción purulenta"]),
  Q("¿Dónde está el foco?", [
      L("Útero doloroso, loquios fétidos", "ENDOMETRITIS", ["INICIAR ANTIBIÓTICOS", "Clindamicina + gentamicina EV"], path=True),
      L("Herida eritematosa", "Infección de herida", ["Abrir y drenar"]),
      L("Mama dura, roja", "Mastitis", ["Dicloxacilina, seguir lactando"]),
      L("Puño percusión (+)", "Pielonefritis", ["Urocultivo, ceftriaxona"])], path=True),
  ("Endometritis puerperal", [("Clave", True), ("Detalle", False)], [
      ("Factor", ["Cesárea (principal)", "RPM prolongada, tactos múltiples"]),
      ("Tratamiento", ["Clindamicina + gentamicina", "Hasta 24-48 h afebril"]),
      ("Si no mejora", ["Buscar absceso, restos", "Tromboflebitis pélvica"])]),
  ["La cesárea es el principal factor de riesgo.",
   "La infección es polimicrobiana: cubrir anaerobios.",
   "El legrado se reserva para restos placentarios."],
  WILLIAMS + " · OMS – Recommendations for prevention and treatment of maternal peripartum infections (2015)")

# SP-056 · fases
V("fases", "SP-056", "serumista-plan-operativo-anual-problemas", "Planificación: por dónde empezar",
  "SALUD PÚBLICA ENAM: PLAN OPERATIVO ANUAL", "SALUD PÚBLICA",
  ("Planificación sanitaria", ["Todo plan empieza por identificar y priorizar los problemas de salud",
   "Luego se fijan objetivos, actividades y recursos"]),
  ("Médico serumista, jefe de un establecimiento I-4", ["Debe presentar el plan operativo anual"]),
  {"rotulo": "Secuencia del plan", "ans": 0,
   "fases": [("Diagnóstico", "Paso 1", "PROBLEMAS SANITARIOS", ["ASIS y priorización"]),
             ("Objetivos", "Paso 2", "Metas", ["Medibles y con plazo"]),
             ("Actividades", "Paso 3", "Qué hacer", ["Responsables y cronograma"]),
             ("Recursos", "Paso 4", "Presupuesto", ["Personal e insumos"])],
   "curvas": [],
   "chips_titulo": "Primer paso · marcado el correcto",
   "chips": [("Determinar problemas", True), ("Formular metas", False), ("Definir actividades", False), ("Asignar recursos", False)]},
  ["Sin diagnóstico previo, los objetivos no responden a necesidades reales.",
   "El ASIS local es la fuente para identificar problemas.",
   "La evaluación cierra el ciclo y alimenta el siguiente plan."],
  "MINSA – Documento técnico: Metodología para el análisis de situación de salud local (2015) · CEPLAN – Guía para el planeamiento institucional (2023)")

# PSI-015 · matriz
V("matriz", "PSI-015", "vomitos-autoprovocados-adolescente-alcalosis", "Conductas purgativas y medio interno",
  "PSIQUIATRÍA ENAM: TRASTORNO DE LA CONDUCTA ALIMENTARIA", "PSIQUIATRÍA",
  ("Conductas purgativas", ["El vómito pierde HCl: alcalosis metabólica con cloro bajo",
   "Los laxantes pierden bicarbonato: acidosis metabólica"]),
  ("Adolescente de 13 años con IMC 15", ["Deshidratada y desnutrida", "Se provoca vómitos con frecuencia"]),
  {"rotulo": "Qué se pierde y qué resulta", "eje_x": "Conducta", "eje_y": "Efecto",
   "cols": ["Vómitos provocados", "Abuso de laxantes"], "rows": ["Se pierde", "Ácido-base", "Cloro", "Potasio"], "caso": (1, 0),
   "cells": [[("HCl gástrico", []), ("Bicarbonato", ["Heces"])],
             [("ALCALOSIS METABÓLICA", []), ("Acidosis metabólica", [])],
             [("Bajo", ["Hipoclorémica"]), ("Normal o alto", [])],
             [("Bajo", ["Pérdida renal"]), ("Bajo", ["Pérdida fecal"])]]},
  ["La hipokalemia es la alteración más peligrosa: arritmias.",
   "Signo de Russell y agrandamiento parotídeo delatan el vómito provocado.",
   "Corregir con suero salino y potasio; realimentar con cuidado."],
  "APA – Practice guideline for the treatment of patients with eating disorders (2023)")

# PED-092 · embudo
V("embudo", "PED-092", "cianosis-neonatal-no-mejora-oxigeno", "Cianosis neonatal que no mejora con O₂",
  "PEDIATRÍA ENAM: CARDIOPATÍA CONGÉNITA CIANÓTICA", "PEDIATRÍA",
  ("Cianosis en el recién nacido", ["Si no mejora con oxígeno al 100%, la causa es cardíaca",
   "Las cardiopatías con cortocircuito izquierda-derecha no dan cianosis"]),
  ("Recién nacido a término de 3 horas", ["Cianosis perioral y ungueal", "No mejora con oxígeno"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Recién nacido cianótico",
   "candidatos": ["Estenosis pulmonar", "Enfermedad pulmonar", "PCA", "CIV", "CIA"],
   "pasos": [("No mejora con O₂ al 100% (prueba de hiperoxia)", ["Enfermedad pulmonar"]),
             ("Cortocircuito izquierda-derecha: no dan cianosis", ["PCA", "CIV", "CIA"])],
   "final": ("ESTENOSIS PULMONAR CRÍTICA", ["Cardiopatía cianótica", "Prostaglandina E1 y ecocardiograma"]),
   "nota": "Las cardiopatías ductus-dependientes empeoran al cerrarse el conducto: prostaglandina E1."},
  ["Cianóticas: las 5 T (Fallot, transposición, tronco, tricúspide, TAPVR) y la estenosis pulmonar crítica.",
   "Tamizaje con oximetría pre y posductal a todo recién nacido.",
   "La CIV, CIA y PCA producen insuficiencia cardiaca, no cianosis."],
  "AHA – Neonatal and pediatric congenital heart disease statement (2023) · " + NELSON)

# PSI-016 · tarjetas
V("tarjetas", "PSI-016", "delirios-grandeza-persecucion-esquizofrenia", "Psicosis con delirios",
  "PSIQUIATRÍA ENAM: ESQUIZOFRENIA PARANOIDE", "PSIQUIATRÍA",
  ("Psicosis con delirios", ["Delirios de persecución y grandeza con aislamiento y descuido personal",
   "Predominio de delirios y alucinaciones = forma paranoide"]),
  ("Infectólogo de 45 años con 3 meses de aislamiento", ["Cree haber inventado una vacuna y que quieren matarlo", "Micrófonos y cámaras en su casa · desaseado"]),
  {"rotulo": "¿Qué psicosis es?", "ans": 0, "cards": [
      {"titulo": "ESQUIZOFRENIA PARANOIDE", "datos": [
          ("Delirios", "Persecución, grandeza", True), ("Ánimo", "No domina", True),
          ("Funcionamiento", "Deterioro, aislamiento", True), ("Duración", "≥ 6 meses (DSM-5)", False)],
       "pie": "Antipsicóticos"},
      {"titulo": "Trastorno delirante", "datos": [
          ("Delirios", "No extravagantes", False), ("Ánimo", "No domina", False),
          ("Funcionamiento", "Conservado", False), ("Duración", "≥ 1 mes", False)],
       "pie": "Sin alucinaciones prominentes"},
      {"titulo": "Manía psicótica", "datos": [
          ("Delirios", "Grandeza", False), ("Ánimo", "Eufórico, irritable", False),
          ("Funcionamiento", "Hiperactividad", False), ("Duración", "Episódica", False)],
       "pie": "Trastorno bipolar"},
      {"titulo": "Depresión psicótica", "datos": [
          ("Delirios", "Culpa, ruina", False), ("Ánimo", "Deprimido", False),
          ("Funcionamiento", "Inhibido", False), ("Duración", "Episódica", False)],
       "pie": "Antidepresivo + antipsicótico"}]},
  ["Con menos de 6 meses de evolución, el DSM-5 lo llama trastorno esquizofreniforme.",
   "Descartar consumo de sustancias y causas orgánicas.",
   "Burnout: agotamiento laboral sin delirios."],
  "APA – DSM-5-TR (2022) · APA – Practice guideline for the treatment of patients with schizophrenia (2020)")

# OFT-019 · matriz
V("matriz", "OFT-019", "midriasis-bilateral-tras-fondo-de-ojo", "Alteraciones pupilares",
  "OFTALMOLOGÍA ENAM: MIDRIASIS FARMACOLÓGICA", "OFTALMOLOGÍA",
  ("Alteraciones pupilares", ["Midriasis bilateral arreactiva tras dilatar la pupila = efecto del colirio",
   "Sin ptosis ni alteración de la motilidad ocular"]),
  ("Varón de 45 años tras examen de retina", ["Fotofobia y visión borrosa", "Midriasis bilateral no reactiva, sin otro déficit"]),
  {"rotulo": "Pupila, reflejos y signos", "eje_x": "Rasgo", "eje_y": "Causa",
   "cols": ["Pupila", "Signos asociados"], "rows": ["Farmacológica", "III par", "Argyll Robertson", "Horner"], "caso": (0, 0),
   "cells": [[("MIDRIASIS BILATERAL", ["Arreactiva"]), ("Ninguno", ["Tras tropicamida"])],
             [("Midriasis unilateral", []), ("Ptosis, ojo abajo y afuera", [])],
             [("Miosis irregular", ["Acomoda, no reacciona a luz"]), ("Neurosífilis", [])],
             [("Miosis unilateral", []), ("Ptosis leve, anhidrosis", [])]]},
  ["La midriasis por colirio cede en horas; la pilocarpina al 1% no la revierte.",
   "Midriasis unilateral con ptosis y dolor: descartar aneurisma de comunicante posterior.",
   "Argyll Robertson: disociación luz-acomodación."],
  "Kanski's Clinical Ophthalmology 10.ª ed. (2024)")

# GAS-032 · tarjetas
V("tarjetas", "GAS-032", "dolor-epigastrico-nocturno-ulcera-duodenal", "Dolor epigástrico urente",
  "GASTROENTEROLOGÍA ENAM: ÚLCERA DUODENAL", "GASTROENTEROLOGÍA",
  ("Dolor epigástrico urente", ["Dolor 2-5 h tras comer que despierta de noche = úlcera duodenal",
   "Sin signos de alarma: menos probable el cáncer"]),
  ("Varón de 45 años con un mes de dolor urente", ["Aparece 5-6 h después de comer y lo despierta", "Sin pérdida de peso ni disfagia"]),
  {"rotulo": "¿Qué causa el dolor?", "ans": 0, "cards": [
      {"titulo": "ÚLCERA DUODENAL", "datos": [
          ("Horario", "2-5 h tras comer", True), ("Nocturno", "Lo despierta", True),
          ("Comida", "Alivia", False), ("Alarma", "Ausente", True)],
       "pie": "IBP + erradicar H. pylori"},
      {"titulo": "Úlcera gástrica", "datos": [
          ("Horario", "Al comer", False), ("Nocturno", "Menos", False),
          ("Comida", "Empeora", False), ("Alarma", "Biopsiar siempre", False)],
       "pie": "Endoscopia con biopsia"},
      {"titulo": "ERGE", "datos": [
          ("Horario", "Tras comer, acostado", False), ("Nocturno", "Pirosis", False),
          ("Comida", "Empeora", False), ("Alarma", "Disfagia", False)],
       "pie": "IBP"},
      {"titulo": "Cáncer gástrico", "datos": [
          ("Horario", "Continuo", False), ("Nocturno", "Variable", False),
          ("Comida", "Saciedad precoz", False), ("Alarma", "Baja de peso, anemia", False)],
       "pie": "Endoscopia urgente"}]},
  ["La úlcera duodenal se asocia a H. pylori en la mayoría de casos.",
   "Signos de alarma: > 60 años, baja de peso, disfagia, anemia, vómitos, sangrado.",
   "Gastritis aguda: dolor tras AINE o alcohol, sin ritmo horario."],
  "ACG – Treatment of Helicobacter pylori infection (Am J Gastroenterol 2024) · ACG/CAG – Guideline on dyspepsia (2017)")

# PED-093 · matriz
V("matriz", "PED-093", "rpm-prolongada-hipotermia-neumonia-neonatal", "Dificultad respiratoria neonatal",
  "PEDIATRÍA ENAM: NEUMONÍA NEONATAL", "PEDIATRÍA",
  ("Dificultad respiratoria del recién nacido", ["Los antecedentes perinatales orientan la causa",
   "RPM > 18 h + hipotermia + dificultad respiratoria = neumonía/sepsis"]),
  ("RN de 36 semanas con 12 h de vida", ["Dificultad respiratoria leve e hipotermia", "Madre con RPM > 18 horas"]),
  {"rotulo": "Causas y claves", "eje_x": "Rasgo", "eje_y": "Causa",
   "cols": ["Factor de riesgo", "Clave clínica"], "rows": ["Neumonía neonatal", "Membrana hialina", "Taquipnea transitoria"], "caso": (0, 0),
   "cells": [[("RPM > 18 H", ["Corioamnionitis, SGB"]), ("Hipotermia, inestabilidad", ["Sepsis asociada"])],
             [("Prematuridad", ["< 34 semanas"]), ("Empeora en horas", ["Vidrio esmerilado"])],
             [("Cesárea sin trabajo de parto", []), ("Mejora en 24-72 h", ["Cisuras con líquido"])]]},
  ["En la sepsis neonatal la hipotermia es tan importante como la fiebre.",
   "Tratamiento empírico: ampicilina + gentamicina tras hemocultivo.",
   "Estreptococo del grupo B y E. coli son los principales agentes."],
  "AAP – Management of neonates born at ≥ 35 weeks with suspected early-onset sepsis (Pediatrics 2018) · " + NELSON)

# NEU-025 · árbol
A("NEU-025", "gestante-contacto-tb-ppd-positivo-isoniacida", "Contacto de tuberculosis",
  "NEUMOLOGÍA ENAM: INFECCIÓN TUBERCULOSA LATENTE EN LA GESTANTE", "NEUMOLOGÍA",
  ("Contactos de un caso de tuberculosis", ["Primero descartar enfermedad activa",
   "PPD (+) y Rx normal = infección latente: terapia preventiva"]),
  ("Gestante de 24 semanas asintomática", ["PPD positivo y Rx de tórax normal", "Esposo con TB pulmonar BK (+)"]),
  Q("¿Síntomas o Rx anormal?", [
      L("Sí", "Descartar TB activa", ["Baciloscopía, cultivo, prueba molecular"]),
      Q("¿PPD o IGRA positivo?", [
          L("Sí", "INFECCIÓN TB LATENTE", ["Terapia preventiva con isoniacida", "+ piridoxina; también en gestantes"], path=True),
          L("No", "Contacto sin infección", ["Repetir PPD en 8-10 semanas"])],
        edge="No", path=True)], path=True),
  ("Terapia preventiva de TB", [("Esquema", True), ("Detalle", False)], [
      ("Isoniacida", ["6-9 meses (6H)", "+ piridoxina 25 mg"]),
      ("Rifapentina + H", ["3HP semanal por 12 dosis", "No en gestantes"]),
      ("Controlar", ["Hepatotoxicidad", "Mayor riesgo en embarazo y puerperio"])]),
  ["El embarazo no contraindica la isoniacida.",
   "La Rx de tórax con protección abdominal es segura en la gestante.",
   "Los contactos menores de 5 años reciben terapia preventiva aunque el PPD sea negativo."],
  "OMS – Consolidated guidelines on tuberculosis, Module 1: Prevention (2024) · MINSA – NTS N.° 200-MINSA/DGIESP-2023 (Tuberculosis)")

# END-021 · matriz
V("matriz", "END-021", "colitis-grave-t3-baja-eutiroideo-enfermo", "Perfil tiroideo en el enfermo grave",
  "ENDOCRINOLOGÍA ENAM: SÍNDROME DEL EUTIROIDEO ENFERMO", "ENDOCRINOLOGÍA",
  ("Perfil tiroideo", ["En enfermedad grave baja la conversión de T4 a T3",
   "T3 baja con TSH y T4 libre normales = eutiroideo enfermo"]),
  ("Varón de 45 años con colitis ulcerosa agudizada", ["Consunción y apatía", "T3 total y libre bajas · T4 libre y TSH normales"]),
  {"rotulo": "Patrón de laboratorio", "eje_x": "Hormona", "eje_y": "Diagnóstico",
   "cols": ["TSH", "T4 libre", "T3"], "rows": ["Eutiroideo enfermo", "Hipotiroidismo primario", "Hipotiroidismo subclínico", "Hipotiroidismo central"], "caso": (0, 2),
   "cells": [[("Normal", []), ("Normal", []), ("BAJA", ["Menos desyodasa"])],
             [("Alta", []), ("Baja", []), ("Baja", [])],
             [("Alta", []), ("Normal", []), ("Normal", [])],
             [("Baja o normal", []), ("Baja", []), ("Baja", [])]]},
  ["Es una adaptación, no una enfermedad tiroidea: no se trata con levotiroxina.",
   "Aumenta la T3 reversa.",
   "Repetir el perfil tras la recuperación."],
  "Williams Textbook of Endocrinology 15.ª ed. (2024) · ATA – Guidelines for the treatment of hypothyroidism (2014)")

# GIN-081 · árbol
A("GIN-081", "amenorrea-9-semanas-sangrado-escaso-ecografia", "Sangrado del primer trimestre",
  "OBSTETRICIA ENAM: AMENAZA DE ABORTO", "OBSTETRICIA",
  ("Sangrado en el primer trimestre", ["Con la paciente estable, la ecografía transvaginal define el diagnóstico",
   "Embrión con latido y cuello cerrado = amenaza de aborto"]),
  ("Mujer de 25 años con 9 semanas de amenorrea", ["Dolor cólico y sangrado escaso", "Estable · cérvix cerrado"]),
  Q("¿Estable?", [
      L("No", "Abdomen agudo", ["Ectópico roto: laparotomía"]),
      Q("¿Qué muestra la ecografía TV?", [
          L("Embrión con latido", "AMENAZA DE ABORTO", ["Reposo relativo, control", "La mayoría continúa"], path=True),
          L("Embrión sin latido", "Aborto retenido", ["Misoprostol o AMEU"]),
          L("Útero vacío", "Posible ectópico", ["β-hCG seriada"])],
        edge="Sí: ECOGRAFÍA TV", path=True)], path=True),
  ("Tipos de aborto", [("Amenaza", True), ("En curso", False), ("Incompleto", False)], [
      ("Cérvix", ["Cerrado", "Abierto", "Abierto"]),
      ("Ecografía", ["Embrión vivo", "Saco descendido", "Restos"]),
      ("Conducta", ["Expectante", "Evacuación", "Evacuación"])]),
  ["La culdocentesis casi no se usa: la ecografía la reemplazó.",
   "La β-hCG sola no distingue un embarazo viable de uno no viable.",
   "No legrar sin confirmar que el embarazo no es viable."],
  "ACOG – Practice Bulletin N.° 200: Early pregnancy loss (2018, reafirmado) · MINSA – Guía de práctica clínica de emergencias obstétricas")

# NRL-022 · termómetro
V("termometro", "NRL-022", "tec-edema-papila-glasgow-descenso-salino-hipertonico", "Hipertensión endocraneana: escalones",
  "NEUROLOGÍA ENAM: HIPERTENSIÓN ENDOCRANEANA", "NEUROLOGÍA",
  ("Hipertensión endocraneana", ["Cefalea, vómitos explosivos, papiledema y descenso del Glasgow",
   "La osmoterapia (salino hipertónico o manitol) reduce la PIC"]),
  ("Varón de 30 años, 12 h tras un TEC", ["Cefalea, vómitos explosivos y fotofobia", "Papiledema · Glasgow 10 y descendiendo"]),
  {"rotulo": "Escalones de manejo de la PIC",
   "niveles": [("Nivel 0", "Medidas generales", ["Cabecera 30°, normotermia", "Normoxia, normocapnia"]),
               ("Nivel 1", "Osmoterapia", ["SALINO HIPERTÓNICO", "o manitol"]),
               ("Nivel 2", "Sedación profunda", ["Hiperventilación breve"]),
               ("Nivel 3", "Rescate", ["Craniectomía descompresiva"])],
   "caso_nivel": 1, "ruta_titulo": "Prioridades", "paso_label": "PASO",
   "pasos": [(1, "SOLUCIÓN SALINA HIPERTÓNICA", ["NaCl 3% en bolo"], True),
             (2, "Asegurar la vía aérea", ["Intubar si Glasgow ≤ 8"], False),
             (3, "TC urgente y neurocirugía", ["Evacuar hematoma si existe"], False)]},
  ["Evitar soluciones hipotónicas: aumentan el edema cerebral.",
   "Los AINE y antieméticos no tratan la causa.",
   "Tríada de Cushing: hipertensión, bradicardia y respiración irregular (herniación)."],
  "Brain Trauma Foundation – Guidelines for the management of severe TBI 4.ª ed. (2016) · SIBICC – Seattle consensus on ICP management (2019)")

# GIN-082 · embudo
V("embudo", "GIN-082", "dolor-fid-masa-anexial-hipotension-bhcg", "Dolor en FID en mujer fértil",
  "GINECOLOGÍA ENAM: SOSPECHA DE EMBARAZO ECTÓPICO", "GINECOLOGÍA",
  ("Dolor pélvico en mujer en edad fértil", ["Primero descartar embarazo con β-hCG",
   "Masa anexial dolorosa + hipotensión + irritación peritoneal = ectópico roto"]),
  ("Mujer de 20 años con dolor brusco en FID", ["PA 90/60, palidez, Blumberg (+)", "Masa anexial derecha dolorosa · ciclos irregulares"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dolor agudo en FID en mujer fértil",
   "candidatos": ["Embarazo ectópico", "Apendicitis", "Cólico renal", "EPI", "Torsión ovárica"],
   "pasos": [("Masa anexial dolorosa y dolor al movilizar el cérvix", ["Apendicitis", "Cólico renal"]),
             ("Hipotensión y palidez: hemoperitoneo", ["EPI", "Torsión ovárica"])],
   "final": ("SOSPECHA DE ECTÓPICO ROTO", ["Confirmar con β-hCG", "Inestable: laparotomía"]),
   "nota": "La β-hCG es el primer estudio en toda mujer fértil con dolor abdominal: cambia todo el enfoque."},
  ["Ectópico: la localización más frecuente es la ampolla tubárica.",
   "Con β-hCG positiva y útero vacío en la ecografía: ectópico hasta demostrar lo contrario.",
   "La TC y la Rx no son el siguiente paso en una mujer fértil."],
  "ACOG – Practice Bulletin N.° 193: Tubal ectopic pregnancy (2018) · " + WILLIAMS)

# CB-026 · radial
V("radial", "CB-026", "bebidas-energizantes-agitacion-toxindrome-simpatico", "Toxíndromes",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR CAFEÍNA", "CIENCIAS BÁSICAS",
  ("Toxíndromes", ["Taquicardia, hipertensión, agitación y arritmias = simpaticomimético",
   "La cafeína en altas dosis produce este cuadro"]),
  ("Estudiante de 21 años con 4 bebidas energizantes", ["Agitación y compromiso del sensorio", "PA 180/100 · FC 140 · ruidos arrítmicos"]),
  {"rotulo": "Mapa del tema", "centro": "TOXÍNDROMES", "centro_sub": "Signos clave", "ans": 0,
   "items": [("SIMPATICOMIMÉTICO", ["Cafeína, cocaína, anfetaminas", "Taquicardia, HTA, sudor"]),
             ("Anticolinérgico", ["Piel seca, midriasis", "Retención urinaria"]),
             ("Colinérgico", ["Miosis, secreciones", "Bradicardia"]),
             ("Opioide", ["Miosis, bradipnea", "Coma"]),
             ("Sedante-hipnótico", ["Somnolencia", "Signos vitales normales"])],
   "ruta": ["Bebidas energizantes", "Taquicardia, HTA, arritmias", "Agitación", "SIMPATICOMIMÉTICO"]},
  ["La cafeína en sobredosis causa arritmias, convulsiones e hipokalemia.",
   "Tratamiento: benzodiacepinas para la agitación; carbón activado precoz.",
   "El ataque de pánico no produce PA 180/100 ni arritmias sostenidas."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019)")

# OFT-020 · tarjetas
V("tarjetas", "OFT-020", "semilla-conducto-auditivo-extraccion", "Cuerpo extraño en el oído",
  "OTORRINOLARINGOLOGÍA ENAM: CUERPO EXTRAÑO ÓTICO", "OTORRINOLARINGOLOGÍA",
  ("Cuerpos extraños en el conducto auditivo", ["La conducta depende del tipo de objeto",
   "Material vegetal: no irrigar, porque se hincha"]),
  ("Niño de 5 años", ["Se introdujo una semilla en el conducto auditivo"]),
  {"rotulo": "¿Qué objeto es?", "ans": 0, "cards": [
      {"titulo": "VEGETAL (SEMILLA)", "datos": [
          ("Riesgo", "Se hincha con agua", True), ("Irrigar", "No", True),
          ("Extraer", "Instrumental", True)],
       "pie": "Gancho o pinza bajo visión"},
      {"titulo": "Insecto vivo", "datos": [
          ("Riesgo", "Daña el tímpano", False), ("Irrigar", "Tras inmovilizarlo", False),
          ("Extraer", "Aceite o lidocaína primero", False)],
       "pie": "Matar al insecto antes"},
      {"titulo": "Pila de botón", "datos": [
          ("Riesgo", "Necrosis química", False), ("Irrigar", "No", False),
          ("Extraer", "Urgente", False)],
       "pie": "Emergencia"},
      {"titulo": "Objeto inerte", "datos": [
          ("Riesgo", "Bajo", False), ("Irrigar", "Posible", False),
          ("Extraer", "Pinza o irrigación", False)],
       "pie": "Si el tímpano está íntegro"}]},
  ["No irrigar si hay perforación timpánica o material vegetal.",
   "Si el niño no colabora o el objeto está profundo: otorrino con sedación.",
   "Taponar con algodón empeora la impactación."],
  "AAFP – Removal of foreign bodies from the ear and nose (Am Fam Physician 2023) · Cummings Otolaryngology 7.ª ed. (2021)")

# CAR-035 · puntaje
V("puntaje", "CAR-035", "dialisis-cateter-fiebre-janeway-endocarditis", "Endocarditis: criterios de Duke",
  "CARDIOLOGÍA ENAM: ENDOCARDITIS INFECCIOSA", "CARDIOLOGÍA",
  ("Endocarditis infecciosa", ["Criterios de Duke: mayores (hemocultivos, ecocardiograma) y menores",
   "Lo primero: 3 pares de hemocultivos antes del antibiótico"]),
  ("Varón de 48 años en hemodiálisis por catéter", ["Fiebre con escalofríos y sudoración nocturna", "Lesiones de Janeway · soplo sistólico nuevo"]),
  {"rotulo": "Criterios de Duke en el caso", "escala": "Duke modificado", "total": 3, "max": 5,
   "total_label": "Criterios menores presentes",
   "interpreta": "Endocarditis posible: faltan los criterios mayores",
   "items": [("Predisposición: catéter de hemodiálisis", "m", True), ("Fiebre ≥ 38 °C", "m", True),
             ("Fenómeno vascular: Janeway", "m", True), ("Hemocultivos positivos típicos", "M", False),
             ("Ecocardiograma con vegetación", "M", False)],
   "bandas": [("3 menores", "Posible", "HEMOCULTIVOS (3 pares) y luego eco", True),
              ("2 M o 1M+3m", "Definida", "Antibiótico dirigido", False)]},
  ["Hemocultivos: 3 pares de sitios distintos antes de iniciar antibiótico.",
   "Luego ecocardiograma: transtorácico primero; transesofágico si no concluye o hay prótesis.",
   "En hemodiálisis por catéter predomina S. aureus."],
  "ESC – Guidelines for the management of endocarditis (2023) · AHA – Infective endocarditis in adults (Circulation 2015)")

# INF-040 · árbol
A("INF-040", "meningococcemia-contacto-personal-salud-rifampicina", "Contacto de meningococo",
  "INFECTOLOGÍA ENAM: QUIMIOPROFILAXIS DE MENINGOCOCO", "INFECTOLOGÍA",
  ("Enfermedad meningocócica", ["Fiebre, meningismo y púrpura = meningococcemia",
   "Los contactos cercanos reciben quimioprofilaxis en las primeras 24 h"]),
  ("Varón de 17 años con fiebre, confusión y rigidez de nuca", ["Petequias y equimosis difusas", "Profilaxis al personal que lo atendió"]),
  Q("¿Contacto cercano o con secreciones?", [
      L("Sí", "QUIMIOPROFILAXIS", ["Rifampicina 600 mg c/12 h × 2 días", "o ciprofloxacino, o ceftriaxona IM"], path=True),
      L("No", "Solo vigilancia", ["Educar sobre signos de alarma"])], path=True),
  ("Opciones de quimioprofilaxis", [("Rifampicina", True), ("Ciprofloxacino", False), ("Ceftriaxona", False)], [
      ("Dosis", ["600 mg c/12 h, 2 días", "500 mg dosis única", "250 mg IM única"]),
      ("Nota", ["Tiñe la orina, interacciones", "Adultos", "Gestantes"])]),
  ["Personal de salud: solo si hubo exposición directa a secreciones (intubación, aspiración).",
   "Isoniazida, etambutol y pirazinamida son antituberculosos: no sirven.",
   "Notificación inmediata a epidemiología."],
  "CDC – Meningococcal disease: prevention and chemoprophylaxis (2024) · MINSA – Vigilancia de enfermedad meningocócica")

# CB-027 · matriz
V("matriz", "CB-027", "incendio-sotano-monoxido-po2-alta-hipoxia-tisular", "Monóxido de carbono y oxigenación",
  "CIENCIAS BÁSICAS ENAM: INTOXICACIÓN POR MONÓXIDO DE CARBONO", "CIENCIAS BÁSICAS",
  ("Monóxido de carbono", ["Se une a la hemoglobina con 200-250 veces más afinidad que el O₂",
   "La PaO₂ puede ser normal o alta, pero los tejidos no reciben oxígeno"]),
  ("Joven de 20 años rescatado de un incendio en un sótano", ["Intubado con O₂ al 100%: PaO₂ 400 mmHg", "Lactato 6 · hipotensión"]),
  {"rotulo": "Qué mide cada parámetro", "eje_x": "Aspecto", "eje_y": "Parámetro",
   "cols": ["Qué mide", "En la intoxicación"], "rows": ["PaO₂", "SatO₂ calculada", "Oxígeno tisular"], "caso": (2, 1),
   "cells": [[("O₂ disuelto", []), ("Alta (400 mmHg)", ["Hiperoxemia"])],
             [("Estimada desde la PaO₂", []), ("Falsamente normal", ["No detecta COHb"])],
             [("Entrega real", []), ("HIPOXIA TISULAR", ["Lactato alto"])]]},
  ["La cooximetría mide la carboxihemoglobina; el pulsioxímetro común no la distingue.",
   "Tratamiento: O₂ al 100%; hiperbárico si hay coma, embarazo o COHb muy alta.",
   "En incendios considerar también intoxicación por cianuro (hidroxocobalamina)."],
  "Goldfrank's Toxicologic Emergencies 11.ª ed. (2019) · UHMS – Hyperbaric oxygen therapy indications 15.ª ed. (2023)")

# TRA-015 · radial
V("radial", "TRA-015", "futbolista-esguince-inversion-calcaneoperoneo", "Ligamentos del tobillo",
  "TRAUMATOLOGÍA ENAM: ESGUINCE DE TOBILLO", "TRAUMATOLOGÍA",
  ("Esguince de tobillo", ["La inversión lesiona el complejo ligamentario lateral",
   "Primero el peroneoastragalino anterior; luego el calcaneoperoneo"]),
  ("Futbolista de 32 años", ["Dolor e inflamación en la cara lateral del tobillo", "Esguince por inversión"]),
  {"rotulo": "Mapa del tema", "centro": "TOBILLO", "centro_sub": "Ligamentos", "ans": 1,
   "items": [("Peroneoastragalino anterior", ["El más lesionado", "Inversión en flexión plantar"]),
             ("CALCANEOPERONEO", ["Lateral", "Segundo en lesionarse"]),
             ("Peroneoastragalino posterior", ["Lesión grave"]),
             ("Deltoideo", ["Medial: eversión"]),
             ("Sindesmosis", ["Rotación externa"])],
   "ruta": ["Mecanismo de inversión", "Dolor lateral", "Complejo lateral", "CALCANEOPERONEO"]},
  ["Reglas de Ottawa para decidir la radiografía.",
   "Tratamiento funcional: protección, hielo, vendaje y carga precoz.",
   "El deltoideo (medial) se lesiona en eversión."],
  "NATA – Position statement: management of acute ankle sprains (J Athl Train 2013) · Campbell's Operative Orthopaedics 14.ª ed. (2021)")

# GIN-083 · árbol
A("GIN-083", "sangrado-tercer-trimestre-establecimiento-i2-referencia", "Sangrado del tercer trimestre en el primer nivel",
  "OBSTETRICIA ENAM: HEMORRAGIA DE LA SEGUNDA MITAD DEL EMBARAZO", "OBSTETRICIA",
  ("Sangrado después de las 22 semanas", ["Puede ser placenta previa o desprendimiento",
   "No hacer tacto vaginal: referir a un establecimiento con capacidad resolutiva"]),
  ("Gestante a término sin control prenatal en un I-2", ["Sangrado escaso continuo", "LCF 140 · sin dinámica uterina"]),
  Q("¿Sangrado con ≥ 22 semanas?", [
      L("No", "Evaluar como 1.ª mitad", ["Aborto, ectópico"]),
      Q("¿Establecimiento con cesárea y sangre?", [
          L("No (I-1 a I-3)", "REFERIR", ["Vía EV, sin tacto vaginal", "Traslado acompañado"], path=True),
          L("Sí", "Ecografía y manejo", ["Placenta previa o DPP"])],
        edge="Sí", path=True)], path=True),
  ("Hemorragia de la 2.ª mitad", [("Placenta previa", True), ("Desprendimiento", False)], [
      ("Dolor", ["Indoloro", "Doloroso"]),
      ("Útero", ["Blando", "Hipertónico"]),
      ("Tacto vaginal", ["Contraindicado", "Con cautela"])]),
  ["El tacto vaginal puede desencadenar una hemorragia masiva en la placenta previa.",
   "En el primer nivel: estabilizar, canalizar vía y referir.",
   "Clave roja si hay inestabilidad hemodinámica."],
  "MINSA – Guía de práctica clínica para la atención de emergencias obstétricas según nivel de capacidad resolutiva · " + WILLIAMS)

# PED-094 · fases
V("fases", "PED-094", "tos-paroxistica-vomito-cianosis-tos-ferina", "Tos ferina: fases",
  "PEDIATRÍA ENAM: TOS FERINA", "PEDIATRÍA",
  ("Tos ferina", ["Catarro inicial seguido de tos paroxística que termina en vómito o cianosis",
   "Entre accesos el niño está bien"]),
  ("Lactante de 7 meses", ["Congestión nasal hace 2 semanas", "Tos paroxística con vómito y cianosis; bien entre accesos"]),
  {"rotulo": "Evolución de la enfermedad", "ans": 1,
   "fases": [("Catarral", "1-2 sem", "Rinorrea", ["La más contagiosa"]),
             ("Paroxística", "2-6 sem", "TOS EN ACCESOS", ["Estridor, vómito, cianosis"]),
             ("Convalecencia", "Semanas", "Tos que cede", ["Recaídas con virus"])],
   "curvas": [("Tos", ROSE, [0.2, 0.3, 0.8, 0.95, 0.8, 0.4, 0.2]),
              ("Contagio", AMBER, [0.9, 0.95, 0.6, 0.3, 0.15, 0.05, 0.02])],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Tos ferina", True), ("SOB", False), ("Laringitis", False), ("Rinofaringitis", False)]},
  ["Tratamiento: azitromicina; también a los contactos.",
   "Leucocitosis con linfocitosis es característica.",
   "En menores de 3 meses puede presentarse solo con apneas."],
  "CDC – Pertussis: clinical overview (2024) · MINSA – NTS del esquema nacional de vacunación (2024)")

# NEF-033 · termómetro
V("termometro", "NEF-033", "urocultivo-umbral-100000-ufc", "Urocultivo: cuándo es significativo",
  "NEFROLOGÍA ENAM: DIAGNÓSTICO DE INFECCIÓN URINARIA", "NEFROLOGÍA",
  ("Urocultivo", ["En orina de chorro medio, ≥ 100 000 UFC/mL de un germen es significativo",
   "Umbrales menores valen para sonda o punción suprapúbica"]),
  ("Pregunta de concepto", ["¿Desde cuántas UFC se diagnostica infección urinaria?"]),
  {"rotulo": "UFC/mL en chorro medio",
   "niveles": [("< 10 000", "Negativo", ["Sin infección"]),
               ("10 000-99 999", "Dudoso", ["Repetir o valorar clínica", "Significativo por sonda"]),
               ("≥ 100 000", "Significativo", ["INFECCIÓN URINARIA", "Un solo germen"])],
   "caso_nivel": 2, "ruta_titulo": "Interpretación", "paso_label": "PASO",
   "pasos": [(1, "≥ 100 000 UFC/mL: ITU", ["Muestra de chorro medio con aseo"], True),
             (2, "Varios gérmenes: contaminación", ["Repetir la muestra"], False),
             (3, "Punción suprapúbica: cualquier recuento", ["Es estéril normalmente"], False)]},
  ["Bacteriuria asintomática: dos muestras ≥ 100 000 del mismo germen (una en el varón).",
   "Solo se trata en gestantes y antes de procedimientos urológicos.",
   "El sedimento orienta; el urocultivo confirma."],
  "IDSA – Clinical practice guideline for asymptomatic bacteriuria (2019) · EAU – Guidelines on urological infections (2024)")

# NEF-034 · tarjetas
V("tarjetas", "NEF-034", "calculo-radiopaco-calcio-normal-oxalato", "Tipos de cálculo urinario",
  "NEFROLOGÍA ENAM: LITIASIS POR OXALATO DE CALCIO", "NEFROLOGÍA",
  ("Tipos de cálculos", ["El oxalato de calcio es el más frecuente (≈ 70-80%)",
   "Radiopaco, sin infección ni alteración del calcio sérico"]),
  ("Varón de 35 años con cólico y hematuria", ["Cálculo radiopaco en riñón derecho", "Calcio y fósforo normales · urocultivo negativo"]),
  {"rotulo": "¿Qué cálculo es?", "ans": 0, "cards": [
      {"titulo": "OXALATO DE CALCIO", "datos": [
          ("Rx", "Radiopaco", True), ("Frecuencia", "El más común", True),
          ("pH orina", "Cualquiera", False), ("Clave", "Hipercalciuria idiopática", False)],
       "pie": "Líquidos, tiazidas, citrato"},
      {"titulo": "Ácido úrico", "datos": [
          ("Rx", "Radiolúcido", False), ("Frecuencia", "5-10%", False),
          ("pH orina", "Ácido", False), ("Clave", "Gota, quimioterapia", False)],
       "pie": "Alcalinizar la orina"},
      {"titulo": "Estruvita", "datos": [
          ("Rx", "Radiopaco", False), ("Frecuencia", "10-15%", False),
          ("pH orina", "Alcalino", False), ("Clave", "Proteus, coraliforme", False)],
       "pie": "Retirar el cálculo"},
      {"titulo": "Cistina", "datos": [
          ("Rx", "Poco radiopaco", False), ("Frecuencia", "Raro", False),
          ("pH orina", "Ácido", False), ("Clave", "Hereditario, niños", False)],
       "pie": "Cristales hexagonales"}]},
  ["La TC sin contraste es el estudio de elección en el cólico renal.",
   "Estruvita exige urocultivo positivo (gérmenes productores de ureasa).",
   "Beber más de 2.5 L de agua al día previene recurrencias."],
  "EAU – Guidelines on urolithiasis (2024) · AUA – Medical management of kidney stones (2019)")

# NEU-026 · matriz
V("matriz", "NEU-026", "acv-hospitalizado-dia-8-neumonia-gramnegativos", "Neumonía según el lugar de adquisición",
  "NEUMOLOGÍA ENAM: NEUMONÍA INTRAHOSPITALARIA", "NEUMOLOGÍA",
  ("Neumonía intrahospitalaria", ["Aparece ≥ 48 h después del ingreso",
   "Predominan los bacilos gramnegativos (Pseudomonas, Klebsiella) y S. aureus"]),
  ("Varón de 73 años hospitalizado por ACV isquémico", ["Día 8: polipnea, SatO₂ 90%", "Consolidación basal derecha"]),
  {"rotulo": "Lugar y gérmenes", "eje_x": "Aspecto", "eje_y": "Tipo",
   "cols": ["Gérmenes", "Tratamiento empírico"], "rows": ["Comunidad", "Intrahospitalaria", "Aspirativa"], "caso": (1, 0),
   "cells": [[("Neumococo", ["Atípicos, H. influenzae"]), ("Amoxicilina o ceftriaxona", ["± macrólido"])],
             [("BACILOS GRAMNEGATIVOS", ["Pseudomonas, Klebsiella", "S. aureus"]), ("Antipseudomónico", ["Piperacilina-tazobactam, cefepime"])],
             [("Anaerobios y flora oral", []), ("Ampicilina-sulbactam", [])]]},
  ["El ACV con disfagia aumenta el riesgo de aspiración.",
   "Añadir vancomicina o linezolid si hay riesgo de SARM.",
   "Tomar cultivos de secreción respiratoria antes del antibiótico."],
  "IDSA/ATS – Management of hospital-acquired and ventilator-associated pneumonia (Clin Infect Dis 2016)")

# GIN-084 · árbol
A("GIN-084", "amenorrea-secundaria-test-progesterona-anovulacion", "Amenorrea secundaria",
  "GINECOLOGÍA ENAM: AMENORREA ANOVULATORIA", "GINECOLOGÍA",
  ("Estudio de la amenorrea secundaria", ["1.° β-hCG · 2.° TSH y prolactina · 3.° prueba de progesterona",
   "Si sangra tras la progesterona: hay estrógenos y útero sano = anovulación"]),
  ("Mujer de 25 años con 1 año de amenorrea", ["β-hCG negativa · FSH, LH, prolactina y TSH normales", "Menstrúa tras progesterona por 5 días"]),
  Q("¿Sangra con progesterona?", [
      L("Sí", "ANOVULACIÓN", ["Estrógenos presentes, útero sano", "Ej.: ovario poliquístico"], path=True),
      Q("¿Sangra con estrógeno + progesterona?", [
          L("No", "Causa uterina", ["Síndrome de Asherman"]),
          L("Sí", "Falta de estrógenos", ["FSH alta: ovario · baja: hipófisis o hipotálamo"])],
        edge="No")], path=True),
  ("Causas de amenorrea secundaria", [("Anovulación", True), ("Hipotalámica", False), ("Uterina", False)], [
      ("Progesterona", ["Sangra", "No sangra", "No sangra"]),
      ("FSH", ["Normal", "Baja o normal", "Normal"]),
      ("Ejemplo", ["Ovario poliquístico", "Estrés, ejercicio", "Asherman"])]),
  ["La causa más frecuente de amenorrea secundaria es el embarazo.",
   "La anovulación crónica expone al endometrio a estrógenos sin oposición.",
   "Tratamiento: progestágeno cíclico o anticonceptivos."],
  "ASRM – Current evaluation of amenorrhea: a committee opinion (Fertil Steril 2024) · Speroff's Clinical Gynecologic Endocrinology and Infertility 9.ª ed. (2019)")
