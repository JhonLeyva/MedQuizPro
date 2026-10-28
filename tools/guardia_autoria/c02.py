from clib import *
REF = ["r1"]
PED = {"texto": "Sin intervalo pediátrico cargado: se interpreta según la edad con el laboratorio de referencia"}
c = {
 "id": "c02", "modalidad": "consulta", "titulo": "Fiebre y llanto al orinar en una niña de 20 meses", "especialidad": "Pediatría · Nefrología pediátrica", "dificultad": 2, "duracion_min": 18,
 "areas_banco": ["pediatria", "nefrologia"],
 "resumen": "Consulta pediátrica ambulatoria por fiebre de dos días en una niña pequeña. Realiza la anamnesis con la madre y el examen, solicita pruebas con criterio, interpreta los resultados y decide tratamiento y seguimiento.",
 "contexto": "Consultorio pediátrico de un hospital con laboratorio, ecografía y cirugía/nefrología pediátrica de referencia.",
 "paciente": {"edad": 1.67, "edad_texto": "20 meses", "sexo": "F", "embarazo": False},
 "motivo": "La madre dice: «Mi niña tiene fiebre desde hace dos días y llora cuando hace pipí.»",
 "referencias": [
  R("r1", "guia", "Urinary tract infection: clinical practice guideline for the diagnosis and management of the initial UTI in febrile infants and children 2 to 24 months", "American Academy of Pediatrics (Subcommittee on Urinary Tract Infection)", "Subcommittee on Urinary Tract Infection, Steering Committee on Quality Improvement and Management, Roberts KB", 2011, "Guía de 2011 (reafirmada posteriormente por la AAP, no verificado aquí); puede haber guías más recientes no consultadas.", "El diagnóstico exige piuria y al menos 50 000 UFC/mL de un uropatógeno en una muestra bien recolectada; se trata 7 a 14 días; se hace ecografía renal y vesical tras la primera ITU febril; la cistouretrografía no es rutinaria tras la primera ITU y no se apoya la profilaxis antibiótica en niños sin reflujo o con reflujo de grado I a IV.", pmid="21873693", doi="10.1542/peds.2011-1330"),
 ],
 "discrepancias": ["La guía AAP 2011 cubre a lactantes y niños de 2 a 24 meses con fiebre: la paciente (20 meses) está dentro de ese rango. No se consultó una norma peruana (MINSA) de infección urinaria pediátrica. Los antibióticos y sus dosis dependen del peso, el antibiograma local y el protocolo institucional: no se fijan aquí.", "El catálogo de laboratorio es de adultos: para esta paciente no inventa intervalos pediátricos y lo indica en cada resultado."],
 "anamnesis": [
  {"categoria": "Enfermedad actual", "preguntas": [
   A("a1", "¿Desde cuándo tiene fiebre y cuánto llega a subir?", "Dos días, hasta 39 °C aunque le doy paracetamol.", "clave"),
   A("a2", "¿Tiene tos, mocos, dolor de oído o dificultad para respirar?", "No tose, no tiene mocos y no se jala las orejas.", "clave"),
   A("a3", "¿Cómo orina? ¿Hay cambios en el olor, la frecuencia o el llanto?", "Orina poquito y varias veces, llora al orinar y el pañal huele fuerte.", "clave"),
   A("a4", "¿Ha tenido vómitos o diarrea?", "Un vómito ayer; no ha tenido diarrea.", "util"),
   A("a5", "¿Cómo toma líquidos y cuántos pañales moja al día?", "Toma menos de lo habitual pero moja unos cuatro o cinco pañales.", "clave"),
   A("a6", "¿Está irritable, decaída o somnolienta?", "Está irritable pero reacciona y juega un poco.", "util"),
   A("a7", "¿Le ha salido alguna erupción en la piel?", "No ha tenido ninguna erupción.", "baja")]},
  {"categoria": "Antecedentes pertinentes", "preguntas": [
   A("a8", "¿Es la primera vez que tiene una infección de orina?", "Es la primera vez que tiene fiebre sin causa clara.", "clave"),
   A("a9", "¿Cómo fueron las ecografías del embarazo y el desarrollo desde que nació?", "Los controles fueron normales y nació a término.", "util"),
   A("a10", "¿Ha tomado antibióticos en las últimas semanas?", "No ha tomado antibióticos.", "util"),
   A("a11", "¿Tiene estreñimiento o ya controla esfínteres?", "Usa pañal y evacúa a diario, sin estreñimiento.", "util"),
   A("a12", "¿Tiene sus vacunas al día?", "Sí, tiene todas las vacunas de su edad.", "baja")]}],
 "antecedentes": [
  {"id": "h1", "nombre": "Perinatales", "texto": "Parto a término, peso adecuado, sin hospitalizaciones previas.", "relevancia": "util"},
  {"id": "h2", "nombre": "Antecedentes de infecciones", "texto": "Sin infecciones urinarias previas conocidas; resfríos ocasionales.", "relevancia": "clave"},
  {"id": "h3", "nombre": "Familiares", "texto": "Una prima con reflujo vesicoureteral tratada en la infancia.", "relevancia": "util"},
  {"id": "h4", "nombre": "Alergias y medicación", "texto": "Sin alergias conocidas. Recibe solo paracetamol por la fiebre.", "relevancia": "baja"}],
 "examen": [
  {"id": "e1", "region": "General", "maniobra": "Signos vitales y peso", "hallazgo": "T 38,9 °C, FC 150 /min, FR 30 /min, SatO₂ 98 %. Peso 11 kg.", "relevancia": "clave"},
  {"id": "e2", "region": "Hidratación", "maniobra": "Estado de hidratación y perfusión", "hallazgo": "Mucosas húmedas, llenado capilar menor de 2 segundos, sin signos de deshidratación.", "relevancia": "clave"},
  {"id": "e3", "region": "Abdomen", "maniobra": "Palpación abdominal y suprapúbica", "hallazgo": "Blando; molestia a la palpación suprapúbica, sin masas ni visceromegalia.", "relevancia": "clave"},
  {"id": "e4", "region": "Genitales", "maniobra": "Inspección de genitales externos", "hallazgo": "Eritema leve vulvar, sin sinequias labiales ni lesiones.", "relevancia": "util"},
  {"id": "e5", "region": "Cabeza y cuello", "maniobra": "Otoscopia y orofaringe", "hallazgo": "Tímpanos normales y orofaringe sin exudados.", "relevancia": "util"},
  {"id": "e6", "region": "Respiratorio", "maniobra": "Auscultación pulmonar", "hallazgo": "Murmullo vesicular normal, sin sibilancias ni crepitantes.", "relevancia": "baja"},
  {"id": "e7", "region": "Neurológico", "maniobra": "Estado de alerta y signos meníngeos", "hallazgo": "Alerta, consolable, sin rigidez de nuca ni fontanela abombada.", "relevancia": "util"},
  {"id": "e8", "region": "Lumbar", "maniobra": "Puñopercusión lumbar", "hallazgo": "Llora con la maniobra, sin localizar claramente el dolor.", "relevancia": "baja"}],
 "hipotesis": {"max": 3, "opciones": [
  {"id": "d1", "dx": "Infección urinaria febril (pielonefritis aguda)", "tipo": "principal", "nota": "Fiebre sin foco respiratorio u ótico, síntomas urinarios y molestia suprapúbica en una niña pequeña."},
  {"id": "d2", "dx": "Otitis media aguda", "tipo": "diferencial", "nota": "Causa frecuente de fiebre a esta edad, pero la otoscopia fue normal."},
  {"id": "d3", "dx": "Gastroenteritis aguda", "tipo": "diferencial", "nota": "Hubo un vómito, pero no hay diarrea ni deshidratación; no explica los síntomas urinarios."},
  {"id": "d4", "dx": "Infección viral de vías respiratorias", "tipo": "diferencial", "nota": "No hay tos ni mocos; no explica el llanto al orinar."},
  {"id": "d5", "dx": "Neumonía", "tipo": "diferencial", "nota": "Sin tos ni dificultad respiratoria y con auscultación normal."},
  {"id": "d6", "dx": "Apendicitis aguda", "tipo": "distractor", "nota": "Rara a esta edad y el abdomen no muestra signos de irritación peritoneal."},
  {"id": "d7", "dx": "Enfermedad de Kawasaki", "tipo": "distractor", "nota": "Requiere fiebre prolongada y otros criterios que aquí no están."},
  {"id": "d8", "dx": "Meningitis bacteriana", "tipo": "distractor", "nota": "Sin alteración del estado de alerta ni signos meníngeos."}]},
 "pruebas": [
  T("p1", "Orina", "Examen completo de orina (tira reactiva y sedimento)", "prioritaria", "Es la prueba inicial para buscar piuria y nitritos en una niña febril sin foco claro.", LAB("Examen completo de orina", [("orina_esterasa", "positivo (+++)"), ("orina_nitritos", "positivo"), ("orina_leucocitos", 40, "Leucocitos en sedimento", PED), ("orina_hematies", 3, "Hematíes en sedimento", PED)]), esencial=True, bloqueante="Sin un examen de orina no puedes confirmar ni descartar una infección urinaria en una niña febril sin otro foco: reconsidera los estudios de orina antes de diagnosticar.", cambia="Muestra piuria y nitritos que orientan al diagnóstico y a iniciar el tratamiento.", critico=True),
  T("p2", "Microbiología", "Urocultivo con muestra obtenida por cateterismo vesical o de chorro medio limpio", "prioritaria", "El diagnóstico requiere piuria y un cultivo con al menos 50 000 UFC/mL de un uropatógeno en una muestra bien recolectada.", LAB("Urocultivo", [("urocultivo", "positivo: Escherichia coli ≥ 100 000 UFC/mL")]), esencial=True, bloqueante="Sin un urocultivo de una muestra bien recolectada no hay confirmación del diagnóstico ni antibiograma: reconsidera pedirlo antes de decidir el tratamiento.", cambia="Confirma el diagnóstico, identifica el germen y orienta el ajuste del antibiótico.", critico=True),
  T("p3", "Hematología", "Hemograma completo", "razonable", "Puede apoyar la gravedad de la infección, aunque no es imprescindible para el diagnóstico.", LAB("Hemograma", [("leucocitos", 18.2, "Leucocitos", PED), ("hemoglobina", 11.4, "Hemoglobina", PED), ("plaquetas", 360, "Plaquetas", PED)])),
  T("p4", "Inflamación", "Proteína C reactiva", "razonable", "Un valor alto orienta a compromiso renal (pielonefritis) pero no confirma el diagnóstico ni cambia el tratamiento inicial.", LAB("PCR", [("pcr", 6.8, "PCR", PED)])),
  T("p5", "Bioquímica", "Creatinina sérica", "razonable", "Valora la función renal basal ante una probable pielonefritis.", LAB("Creatinina", [("creatinina", 0.3, "Creatinina", PED)])),
  T("p6", "Microbiología", "Hemocultivo", "razonable", "Se considera en niños pequeños con aspecto enfermo; no es imprescindible en una niña bien hidratada y alerta.", TXT("Sin desarrollo bacteriano a las 48 horas.")),
  T("p7", "Imagen", "Ecografía renal y vesical", "razonable", "Se recomienda tras la primera infección urinaria febril para detectar anomalías anatómicas; no es una urgencia.", TXT("Ambos riñones de tamaño y ecogenicidad normales, sin hidronefrosis ni cicatrices; vejiga de paredes normales.")),
  T("p8", "Microbiología", "Urocultivo con muestra de bolsa colectora", "innecesaria", "La bolsa colectora da falsos positivos por contaminación y no sirve para confirmar el diagnóstico.", TXT("Resultado no interpretable: desarrollo mixto por contaminación.")),
  T("p9", "Imagen", "Cistouretrografía miccional", "innecesaria", "No se recomienda de rutina tras la primera infección urinaria; se reserva para hallazgos anormales en la ecografía o infecciones recurrentes.", TXT("No se realiza: sin indicación tras una primera infección con ecografía normal.")),
  T("p10", "Imagen", "Gammagrafía renal con DMSA", "innecesaria", "No es necesaria en la fase aguda de una primera infección y expone a radiación sin cambiar el manejo inicial.", TXT("No se realiza: sin indicación en la fase aguda.")),
  T("p11", "Imagen", "Radiografía simple de abdomen", "innecesaria", "No aporta al diagnóstico de infección urinaria y no cambia la conducta.", TXT("Patrón gaseoso inespecífico; sin relevancia para el caso.")),
  T("p12", "Imagen", "Radiografía de tórax", "innecesaria", "No hay síntomas ni signos respiratorios que justifiquen el estudio.", TXT("Sin hallazgos; no justificaba la exposición a radiación.")),
  T("p13", "Laboratorio", "Punción lumbar", "danina", "Es un procedimiento invasivo sin indicación: la niña está alerta y sin signos meníngeos.", TXT("No se realiza: procedimiento invasivo sin indicación clínica.")),
  T("p14", "Imagen", "Tomografía abdominal con contraste", "danina", "Expone a radiación y a contraste en una niña pequeña sin indicación; la ecografía es suficiente.", TXT("No se realiza: radiación y contraste innecesarios en una niña pequeña.")),
 ],
 "preguntas": {
  "interpretacion": Q("¿Cómo interpretas los resultados?", [
   D("Infección urinaria febril confirmada: piuria con nitritos positivos y urocultivo con Escherichia coli en cuenta significativa", "o", "", "Con piuria y al menos 50 000 UFC/mL de un uropatógeno en una muestra adecuada se confirma el diagnóstico; la fiebre sugiere compromiso renal."),
   D("Bacteriuria asintomática por contaminación de la muestra, que no requiere tratamiento y se resolverá espontáneamente", "i", "", "La niña tiene fiebre, síntomas y piuria con cultivo significativo en una muestra adecuada: no es una colonización."),
   D("Cistitis aislada de vías bajas sin compromiso renal, porque la niña está alerta y se hidrata bien, por lo que basta una dosis única", "i", "", "En una niña pequeña con fiebre se asume compromiso renal; la dosis única no es el tratamiento recomendado."),
   D("Resultado no concluyente por la edad: repetir la muestra con bolsa colectora y esperar tres días antes de tomar una decisión", "i", "", "La muestra fue adecuada y el cuadro es claro; la bolsa colectora no es válida para el diagnóstico y esperar tres días demora el tratamiento."),
   D("Sepsis urinaria con choque que obliga a hospitalizar en cuidados intensivos y a iniciar antibióticos por vía endovenosa de inmediato", "i", "", "La niña está estable, bien perfundida y alerta: no hay criterios de choque ni de cuidados intensivos."),
  ], tema="Interpretación del examen de orina y el urocultivo", comp="dx", refs=REF, peso=2),
  "diagnostico": Q("¿Cuál es el diagnóstico más probable?", [
   D("Infección urinaria febril (pielonefritis aguda) por Escherichia coli en una niña sin factores de riesgo conocidos", "o", "", "Reúne fiebre sin foco, síntomas urinarios, piuria con nitritos y urocultivo positivo."),
   D("Gastroenteritis aguda con deshidratación leve, que se maneja con rehidratación oral y sin necesidad de antibiótico", "i", "", "Hubo un solo vómito sin diarrea y la hidratación es adecuada; no explica los síntomas urinarios ni el cultivo."),
   D("Otitis media aguda bilateral con fiebre, que requiere tratamiento antibiótico oral dirigido a los gérmenes del oído medio", "i", "", "La otoscopia fue normal; los hallazgos apuntan al tracto urinario."),
   D("Síndrome febril viral inespecífico que se resolverá solo, con control de la fiebre y observación en el domicilio durante los días siguientes", "i", "", "Con piuria, nitritos y cultivo positivo se confirma una infección bacteriana que requiere tratamiento."),
   D("Vulvovaginitis por irritación local, tratada con higiene y cremas barrera sin necesidad de ningún estudio de orina", "i", "", "El eritema vulvar leve no explica la fiebre alta ni los resultados urinarios."),
  ], tema="Diagnóstico de la infección urinaria febril", comp="dx", refs=REF, peso=3),
  "tratamiento": Q("¿Qué tratamiento indicas?", [
   D("Antibiótico oral de 7 a 14 días dirigido por la sensibilidad local y el cultivo, con hidratación y paracetamol si hay fiebre", "o", "", "En una niña estable que tolera la vía oral el antibiótico oral por 7 a 14 días es adecuado; se ajusta al antibiograma."),
   D("Antibiótico por vía endovenosa durante 14 días con hospitalización obligatoria para todos los casos de infección urinaria febril", "i", "", "La vía oral es igual de efectiva en una niña estable que tolera líquidos; la hospitalización se reserva para casos con criterios."),
   D("Una dosis única de antibiótico oral y control en un mes, ya que la infección es la primera que presenta la niña", "i", "", "La infección febril requiere un curso de 7 a 14 días; una dosis única no es suficiente."),
   D("Nitrofurantoína oral por tres días porque tiene buena actividad urinaria y se tolera bien en los niños pequeños", "i", "", "La nitrofurantoína no alcanza niveles tisulares adecuados en una infección febril con compromiso renal."),
   D("Ácido acetilsalicílico para controlar la fiebre y antibiótico solo si persiste la fiebre después de tres días de tratamiento", "p", "", "La aspirina en niños pequeños con fiebre se asocia al síndrome de Reye; además el antibiótico no debe diferirse."),
  ], tema="Tratamiento de la infección urinaria febril", comp="tto", refs=REF, peso=2),
  "seguimiento": Q("¿Cuál es el plan de seguimiento, los signos de alarma y los criterios de derivación?", [
   D("Ecografía renal y vesical, reevaluación clínica a las 48 a 72 horas, signos de alarma y estudios adicionales solo si hay hallazgos o recurrencia", "o", "", "Tras la primera infección febril se hace ecografía; la cistouretrografía y otros estudios se reservan para hallazgos anormales o recurrencia."),
   D("Cistouretrografía miccional y gammagrafía renal de rutina tras cualquier primera infección urinaria, para descartar reflujo vesicoureteral en todos los casos", "i", "", "No se recomienda de rutina tras la primera infección; se indica ante hallazgos ecográficos anormales o recurrencia."),
   D("Profilaxis antibiótica diaria durante un año para todas las niñas tras la primera infección, aunque no haya reflujo documentado ni infecciones previas", "i", "", "No se apoya la profilaxis de rutina en niños sin reflujo o con reflujo de grado bajo a intermedio."),
   D("Alta sin control, sin explicar los signos de alarma ni cuándo regresar, porque la evolución con antibiótico suele ser favorable", "i", "", "La paciente debe ser reevaluada a las 48 a 72 horas y la familia debe conocer los signos de alarma para volver."),
   D("Derivar a cirugía pediátrica para evaluación de reimplante ureteral antes de completar el tratamiento antibiótico y sin estudios previos", "p", "", "No hay indicación de cirugía: se deriva solo ante anomalías significativas o infecciones recurrentes, con estudios previos."),
  ], tema="Seguimiento de la infección urinaria pediátrica", comp="dis", refs=REF, peso=2),
 },
 "informe": {
  "resumen_clinico": "Niña de 20 meses con fiebre de dos días sin foco respiratorio ni ótico, orina de olor fuerte con llanto al orinar y molestia suprapúbica; bien hidratada y alerta. La orina mostró piuria con nitritos y el urocultivo, Escherichia coli en cuenta significativa.",
  "diagnostico_final": "Infección urinaria febril (pielonefritis aguda) por Escherichia coli, primera infección, sin criterios de gravedad.",
  "diagnosticos_diferenciales": [
   {"dx": "Otitis media aguda", "por_que_no": "La otoscopia fue normal."},
   {"dx": "Gastroenteritis", "por_que_no": "No hubo diarrea ni deshidratación y no explica los hallazgos urinarios."},
   {"dx": "Síndrome viral", "por_que_no": "Sin síntomas respiratorios; piuria y cultivo positivos indican una infección bacteriana."},
   {"dx": "Meningitis", "por_que_no": "Estado de alerta normal y sin signos meníngeos."}],
  "datos_clave": ["Fiebre alta sin foco respiratorio ni ótico en una niña de 20 meses.", "Cambios urinarios (olor, frecuencia, llanto al orinar) y molestia suprapúbica.", "Primera infección y estado de hidratación y alerta conservados (permite manejo ambulatorio).", "Muestra de orina bien recolectada (cateterismo o chorro medio limpio)."],
  "razonamiento": ["Buscar el foco de la fiebre: respiratorio, ótico, digestivo y urinario.", "Evaluar hidratación y signos de gravedad para decidir el nivel de atención.", "Pedir examen de orina y urocultivo con una muestra bien recolectada.", "Interpretar piuria con nitritos y cultivo significativo como infección urinaria.", "Tratar 7 a 14 días con antibiótico oral dirigido, si tolera la vía oral.", "Hacer ecografía renal y vesical y reevaluar a las 48 a 72 horas.", "Reservar cistouretrografía y derivaciones para hallazgos anormales o recurrencias."],
  "interpretacion_laboratorio": ["Tira reactiva con esterasa leucocitaria y nitritos positivos y piuria en el sedimento: orina inflamatoria con bacterias.", "Urocultivo con E. coli ≥ 100 000 UFC/mL en muestra adecuada: confirma la infección.", "Leucocitosis y PCR altas: respuesta inflamatoria compatible con compromiso renal (no hay intervalos pediátricos cargados).", "Creatinina sin elevación: sin disfunción renal."],
  "tratamiento": [
   {"item": "Antibiótico", "detalle": "Oral por 7 a 14 días si está estable y tolera líquidos, dirigido por la sensibilidad local y el urocultivo.", "dosis": "La dosis depende del peso (11 kg), del fármaco y del protocolo institucional; no se fija aquí."},
   {"item": "Medidas de soporte", "detalle": "Hidratación y paracetamol para la fiebre; evitar aspirina.", "dosis": "Dosis de paracetamol por peso según protocolo."},
   {"item": "Seguimiento", "detalle": "Ecografía renal y vesical y reevaluación a las 48 a 72 horas; estudios adicionales solo si hay hallazgos anormales o recurrencia.", "dosis": "No aplica."},
   {"item": "Signos de alarma y derivación", "detalle": "Fiebre persistente tras 48 a 72 horas, rechazo de líquidos, vómitos persistentes, decaimiento; derivar si hay anomalías en la ecografía o infecciones recurrentes.", "dosis": "No aplica."}],
  "temas_relacionados": ["Infección urinaria en pediatría", "Fiebre sin foco en el lactante", "Reflujo vesicoureteral"],
  "mensaje_clave": "En una niña febril sin foco, el examen de orina y el urocultivo con muestra adecuada confirman la infección urinaria; se trata 7 a 14 días y se hace ecografía."
 }
}
guardar_consulta(c)
