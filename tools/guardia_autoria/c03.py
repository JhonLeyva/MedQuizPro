from clib import *
REF = ["r1"]
c = {
 "id": "c03", "modalidad": "consulta", "titulo": "Dolor pélvico y flujo vaginal en una mujer de 24 años", "especialidad": "Ginecología · Infectología", "dificultad": 2, "duracion_min": 18,
 "areas_banco": ["ginecologia", "infectologia"],
 "resumen": "Consulta ginecológica ambulatoria por dolor en el bajo vientre y flujo con mal olor. Realiza la anamnesis, el examen pélvico, solicita pruebas con criterio y define tratamiento, seguimiento y derivación.",
 "contexto": "Consultorio ginecológico de un hospital con laboratorio, ecografía transvaginal y hospitalización disponible.",
 "paciente": {"edad": 24, "edad_texto": "24 años", "sexo": "F", "embarazo": False},
 "motivo": "«Tengo dolor en la parte baja del vientre y un flujo con mal olor desde hace cinco días.»",
 "referencias": [
  R("r1", "guia", "Sexually Transmitted Infections Treatment Guidelines, 2021", "Centers for Disease Control and Prevention (CDC)", "Workowski KA, Bachmann LH, Chan PA, Johnston CM et al.", 2021, "Guía de 2021, vigente según la última búsqueda; confirma si hay una edición posterior.", "Actualiza el tratamiento de las infecciones de transmisión sexual; añade metronidazol al esquema recomendado para la enfermedad inflamatoria pélvica (junto con una cefalosporina y doxiciclina) y mantiene la evaluación y el tratamiento de las parejas.", pmid="34292926", doi="10.15585/mmwr.rr7004a1"),
 ],
 "discrepancias": ["Solo se leyó el resumen de la guía CDC 2021 en PubMed: el esquema exacto, los criterios de hospitalización y las dosis deben tomarse de la guía y del protocolo local (la sensibilidad de los gérmenes y la disponibilidad de fármacos en el Perú pueden variar). No se consultó una norma técnica peruana (MINSA) de infecciones de transmisión sexual. No se fijan dosis.", "Los intervalos de laboratorio son educativos, no de un laboratorio peruano."],
 "anamnesis": [
  {"categoria": "Enfermedad actual", "preguntas": [
   A("a1", "¿Cómo es el dolor: dónde, desde cuándo y cuánto?", "En el bajo vientre de ambos lados, hace cinco días, con intensidad moderada que empeora al caminar.", "clave"),
   A("a2", "¿Cómo es el flujo vaginal: color, olor y cantidad?", "Amarillento, con mal olor y más abundante que antes.", "clave"),
   A("a3", "¿Ha tenido fiebre o escalofríos?", "Tuve fiebre de 38 °C anoche y escalofríos.", "util"),
   A("a4", "¿Tiene náuseas o vómitos y tolera los alimentos?", "No tengo náuseas y puedo comer y tomar líquidos.", "clave"),
   A("a5", "¿Tiene dolor durante las relaciones sexuales o sangrado después?", "Sí, me duele al tener relaciones y sangré un poco la semana pasada.", "util"),
   A("a6", "¿Tiene molestias al orinar?", "Un poco de ardor al orinar, sin urgencia ni sangre.", "util")]},
  {"categoria": "Ginecológico y sexual", "preguntas": [
   A("a7", "¿Cuándo fue su última regla y existe posibilidad de embarazo?", "Mi última regla fue hace tres semanas; usé pastillas anticonceptivas de forma irregular.", "clave"),
   A("a8", "¿Tiene pareja nueva y usa preservativo?", "Tengo una pareja nueva desde hace dos meses y casi no usamos preservativo.", "clave"),
   A("a9", "¿Ha tenido antes alguna infección de transmisión sexual?", "Tuve una infección vaginal hace un año, no recuerdo cuál.", "clave"),
   A("a10", "¿Usa dispositivo intrauterino u otro anticonceptivo?", "No uso DIU; solo pastillas anticonceptivas que a veces olvido.", "util"),
   A("a11", "¿Su pareja tiene síntomas?", "Mi pareja dice que tiene secreción por el pene desde hace unos días.", "util")]},
  {"categoria": "Otros", "preguntas": [
   A("a12", "¿Tiene alergias a medicamentos?", "No tengo alergias conocidas.", "clave"),
   A("a13", "¿Fuma o consume alcohol o drogas?", "No fumo; tomo alcohol ocasionalmente.", "baja")]}],
 "antecedentes": [
  {"id": "h1", "nombre": "Ginecológicos", "texto": "Menarquia a los 12 años, ciclos regulares de 28 días, sin embarazos previos.", "relevancia": "util"},
  {"id": "h2", "nombre": "Sexuales", "texto": "Inicio sexual a los 17 años, tres parejas en total.", "relevancia": "clave"},
  {"id": "h3", "nombre": "Médicos y quirúrgicos", "texto": "Sin enfermedades crónicas ni cirugías.", "relevancia": "baja"},
  {"id": "h4", "nombre": "Vacunas", "texto": "Vacuna contra el VPH incompleta; sin vacuna contra hepatitis B documentada.", "relevancia": "util"}],
 "examen": [
  {"id": "e1", "region": "General", "maniobra": "Signos vitales", "hallazgo": "T 38,0 °C, PA 108/68 mmHg, FC 96 /min, FR 16 /min.", "relevancia": "clave"},
  {"id": "e2", "region": "Abdomen", "maniobra": "Palpación abdominal", "hallazgo": "Dolor a la palpación del hipogastrio y las fosas ilíacas, sin defensa ni rebote.", "relevancia": "clave"},
  {"id": "e3", "region": "Peritoneo", "maniobra": "Búsqueda de signos de irritación peritoneal", "hallazgo": "Sin defensa ni rebote; sin signos de abdomen agudo quirúrgico.", "relevancia": "clave"},
  {"id": "e4", "region": "Pélvico", "maniobra": "Especuloscopia", "hallazgo": "Cuello uterino eritematoso con secreción mucopurulenta que sangra al roce.", "relevancia": "clave"},
  {"id": "e5", "region": "Pélvico", "maniobra": "Tacto bimanual", "hallazgo": "Dolor a la movilización del cuello uterino y del útero, con dolor en ambos anexos, sin masas palpables.", "relevancia": "clave"},
  {"id": "e6", "region": "Lumbar", "maniobra": "Puñopercusión lumbar", "hallazgo": "Sin dolor a la puñopercusión.", "relevancia": "util"},
  {"id": "e7", "region": "Inguinal", "maniobra": "Palpación de ganglios inguinales", "hallazgo": "Adenopatías inguinales pequeñas y móviles, no dolorosas.", "relevancia": "baja"}],
 "hipotesis": {"max": 3, "opciones": [
  {"id": "d1", "dx": "Enfermedad inflamatoria pélvica", "tipo": "principal", "nota": "Dolor pélvico con dolor a la movilización cervical y anexial, secreción mucopurulenta y factores de riesgo."},
  {"id": "d2", "dx": "Embarazo ectópico", "tipo": "diferencial", "nota": "Debe descartarse siempre en una mujer en edad fértil con dolor pélvico y anticoncepción irregular."},
  {"id": "d3", "dx": "Apendicitis aguda", "tipo": "diferencial", "nota": "Posible en el dolor del bajo vientre, pero aquí el dolor es bilateral y hay signos pélvicos."},
  {"id": "d4", "dx": "Pielonefritis o infección urinaria", "tipo": "diferencial", "nota": "Hay ardor al orinar, pero sin dolor lumbar ni síntomas urinarios predominantes."},
  {"id": "d5", "dx": "Cervicitis aislada sin compromiso del tracto superior", "tipo": "diferencial", "nota": "Explica el flujo, pero no el dolor a la movilización cervical y anexial."},
  {"id": "d6", "dx": "Endometriosis", "tipo": "distractor", "nota": "Es una causa crónica de dolor pélvico; el cuadro es agudo y con fiebre."},
  {"id": "d7", "dx": "Cólico renal por litiasis", "tipo": "distractor", "nota": "No hay dolor lumbar con irradiación ni hematuria."},
  {"id": "d8", "dx": "Candidiasis vulvovaginal simple", "tipo": "distractor", "nota": "No explica la fiebre ni el dolor pélvico profundo; el flujo no es característico."}]},
 "pruebas": [
  T("p1", "Embarazo", "β-hCG cualitativa o cuantitativa", "prioritaria", "Una mujer en edad fértil con dolor pélvico debe descartar un embarazo (ectópico) antes de decidir el tratamiento y los estudios.", LAB("β-hCG", [("bhcg", 1.0)]), esencial=True, bloqueante="Antes de decidir tratamiento en una mujer en edad fértil con dolor pélvico y anticoncepción irregular, debes descartar un embarazo: reconsidera las pruebas de embarazo.", cambia="Descarta un embarazo, incluido el ectópico, y permite el tratamiento ambulatorio.", critico=True),
  T("p2", "Microbiología", "Prueba molecular (NAAT) para Chlamydia trachomatis", "prioritaria", "Confirma el agente más frecuente de la enfermedad inflamatoria pélvica y orienta al manejo de la pareja.", LAB("NAAT clamidia", [("naat_clamidia", "positivo")]), esencial=True, cambia="Confirma la etiología y obliga a tratar y notificar a la pareja."),
  T("p3", "Microbiología", "Prueba molecular (NAAT) para Neisseria gonorrhoeae", "prioritaria", "Debe buscarse junto con la clamidia: cambia la cobertura y el manejo de la pareja.", LAB("NAAT gonococo", [("naat_gonococo", "negativo")]), esencial=True),
  T("p4", "Serología", "Prueba de VIH", "prioritaria", "Toda persona con una infección de transmisión sexual debe ofrecerse una prueba de VIH.", LAB("VIH", [("vih", "no reactivo")])),
  T("p5", "Serología", "VDRL o RPR (sífilis)", "prioritaria", "Se recomienda descartar sífilis en toda persona con una infección de transmisión sexual.", LAB("Sífilis", [("vdrl", "no reactivo")])),
  T("p6", "Hematología", "Hemograma completo", "razonable", "Puede apoyar la presencia de inflamación sistémica sin ser imprescindible.", LAB("Hemograma", [("leucocitos", 14.2), ("hemoglobina", 12.4), ("plaquetas", 310)])),
  T("p7", "Inflamación", "Proteína C reactiva", "razonable", "Apoya el grado de inflamación; no define el diagnóstico.", LAB("PCR", [("pcr", 4.8)])),
  T("p8", "Orina", "Examen de orina", "razonable", "Descarta una infección urinaria como causa del ardor y del dolor.", LAB("Examen de orina", [("orina_esterasa", "negativo"), ("orina_nitritos", "negativo")])),
  T("p9", "Microbiología", "Microscopía en fresco y pH vaginal", "razonable", "Busca otras causas de flujo (vaginosis, tricomoniasis) que pueden coexistir.", TXT("pH vaginal 5,0; abundantes leucocitos polimorfonucleares; sin células clave ni tricomonas móviles.")),
  T("p10", "Serología", "HBsAg (hepatitis B)", "razonable", "Se ofrece en personas con riesgo de infecciones de transmisión sexual para orientar a la vacunación.", LAB("Hepatitis B", [("hbsag", "no reactivo")])),
  T("p11", "Imagen", "Ecografía transvaginal", "razonable", "No es obligatoria para el diagnóstico, pero ayuda a descartar absceso tubo-ovárico y otras causas cuando el cuadro es más grave o dudoso.", TXT("Útero normal, anexos de aspecto normal sin masas y escaso líquido libre en el fondo de saco.")),
  T("p12", "Imagen", "Laparoscopia diagnóstica", "innecesaria", "Es invasiva y no se necesita para tratar una enfermedad inflamatoria pélvica clínica en una paciente estable.", TXT("No se realiza: procedimiento invasivo sin indicación en una paciente estable.")),
  T("p13", "Imagen", "Tomografía abdominopélvica con contraste", "innecesaria", "Irradia y no es necesaria cuando el diagnóstico clínico es claro y la paciente está estable.", TXT("No se realiza: radiación sin indicación en una paciente estable con diagnóstico clínico.")),
  T("p14", "Microbiología", "Cultivo vaginal de rutina", "innecesaria", "No agrega información útil frente a los estudios moleculares en esta situación.", TXT("Flora mixta sin relevancia para la conducta.")),
  T("p15", "Imagen", "Histerosalpingografía", "danina", "Está contraindicada en una infección pélvica aguda por el riesgo de diseminar la infección.", TXT("No se realiza: contraindicada durante la infección pélvica aguda."))
 ],
 "preguntas": {
  "interpretacion": Q("¿Cómo interpretas los hallazgos y los resultados?", [
   D("Enfermedad inflamatoria pélvica leve por Chlamydia trachomatis, sin criterios de gravedad ni absceso y con embarazo descartado", "o", "", "El dolor con dolor a la movilización cervical y anexial, la secreción mucopurulenta y la clamidia positiva confirman una EIP; la paciente está estable y la ecografía no muestra absceso."),
   D("Cervicitis aislada por clamidia sin compromiso del tracto superior, que se resuelve con una dosis única y sin otras medidas adicionales", "i", "", "El dolor a la movilización cervical y anexial indica compromiso del tracto superior: es EIP, no una cervicitis aislada."),
   D("Embarazo ectópico probable, por lo que corresponde una laparoscopía de urgencia para confirmar el diagnóstico", "i", "", "La β-hCG negativa descarta un embarazo; no corresponde a un ectópico."),
   D("Vaginosis bacteriana como causa única del cuadro, que se trata con metronidazol oral sin tratamiento de la pareja", "i", "", "La vaginosis no explica el dolor pélvico con fiebre ni la clamidia positiva; puede coexistir pero no es la causa principal."),
   D("Abdomen agudo quirúrgico con sospecha de apendicitis y absceso tubo-ovárico que exige laparotomía exploradora inmediata", "i", "", "No hay signos peritoneales ni absceso en la ecografía; la paciente está estable."),
  ], tema="Interpretación del dolor pélvico con prueba molecular positiva", comp="dx", refs=REF, peso=2),
  "diagnostico": Q("¿Cuál es el diagnóstico más probable?", [
   D("Enfermedad inflamatoria pélvica por Chlamydia trachomatis, de manejo ambulatorio por no tener criterios de gravedad", "o", "", "Cumple criterios clínicos de EIP, con confirmación microbiológica y sin signos que obliguen a hospitalizar."),
   D("Cistitis aguda no complicada por Escherichia coli, tratada con una pauta corta de antibiótico oral", "i", "", "El ardor al orinar es leve y el examen de orina es negativo; no explica la fiebre ni el dolor pélvico."),
   D("Apendicitis aguda en fase inicial, que exige observación hospitalaria y cirugía si progresa el dolor", "i", "", "El dolor es bilateral con signos pélvicos claros y sin signos peritoneales; la ecografía no sugiere otra causa."),
   D("Dismenorrea primaria con flujo fisiológico, que se maneja con antiinflamatorios y observación domiciliaria", "i", "", "El cuadro tiene fiebre, secreción mucopurulenta y dolor a la movilización: no es fisiológico."),
   D("Endometriosis con endometrioma, con indicación de tratamiento hormonal y control ginecológico programado sin otras medidas", "i", "", "Es una causa crónica; el cuadro es agudo con fiebre y signos infecciosos."),
  ], tema="Diagnóstico de la enfermedad inflamatoria pélvica", comp="dx", refs=REF, peso=3),
  "tratamiento": Q("¿Qué tratamiento indicas?", [
   D("Esquema ambulatorio con una cefalosporina intramuscular más doxiciclina y metronidazol durante 14 días, con reevaluación a las 72 horas", "o", "", "El esquema recomendado incluye cobertura de gonococo, clamidia y anaerobios; la reevaluación a las 72 horas confirma la respuesta."),
   D("Azitromicina en dosis única por vía oral como único tratamiento, y control solo si persisten los síntomas en el siguiente mes", "i", "", "Una dosis única no cubre la enfermedad del tracto superior ni los anaerobios; el esquema es combinado y prolongado."),
   D("Ciprofloxacino oral como monoterapia por una semana, sin cobertura específica para anaerobios ni reevaluación programada", "i", "", "Las fluoroquinolonas no son la primera línea y no cubren de forma fiable el gonococo ni los anaerobios."),
   D("Esperar el resultado de todos los cultivos antes de iniciar cualquier antibiótico, con analgésicos y observación en el domicilio", "p", "", "En la EIP el tratamiento empírico se inicia de inmediato: retrasarlo aumenta el riesgo de secuelas como infertilidad y embarazo ectópico."),
   D("Hospitalización obligatoria con antibióticos endovenosos durante dos semanas para todas las pacientes con enfermedad inflamatoria pélvica", "i", "", "La hospitalización se reserva para casos con criterios de gravedad, embarazo, absceso o falla del tratamiento oral."),
  ], tema="Tratamiento de la enfermedad inflamatoria pélvica", comp="tto", refs=REF, peso=2),
  "seguimiento": Q("¿Cuál es el plan de seguimiento, los signos de alarma y los criterios de derivación?", [
   D("Tratar y notificar a la pareja, abstinencia hasta completar el tratamiento, reevaluar a las 72 horas y derivar si no hay mejoría o hay absceso", "o", "", "El manejo de la pareja evita la reinfección; la reevaluación a las 72 horas detecta la falla y obliga a hospitalizar o estudiar un absceso."),
   D("Dar el alta sin tratar a la pareja porque la paciente ya recibió el antibiótico y el riesgo de reinfección es muy bajo", "i", "", "Sin tratar a la pareja la reinfección es frecuente; el manejo de contactos es parte del tratamiento."),
   D("Indicar reposo absoluto de un mes con control recién a los tres meses y sin explicar signos de alarma a la paciente", "i", "", "La paciente debe ser reevaluada a las 72 horas y conocer los signos de alarma; el reposo prolongado no es necesario."),
   D("Programar una histerectomía profiláctica para evitar nuevas infecciones y complicaciones tardías en la paciente de 24 años sin otras indicaciones", "p", "", "No hay indicación de cirugía mayor: es una decisión desproporcionada y no previene la reinfección."),
   D("Suspender la anticoncepción hormonal y no ofrecer consejería ni pruebas de otras infecciones, por tratarse de un episodio aislado", "i", "", "Se debe ofrecer consejería, pruebas de otras infecciones y prevención de nuevas infecciones, y revisar la anticoncepción."),
  ], tema="Seguimiento y manejo de contactos en la enfermedad inflamatoria pélvica", comp="dis", refs=REF, peso=2),
 },
 "informe": {
  "resumen_clinico": "Mujer de 24 años con cinco días de dolor pélvico bilateral, flujo purulento, fiebre y dispareunia, con una pareja nueva sin protección. El examen mostró cervicitis mucopurulenta con dolor a la movilización cervical y anexial; la clamidia fue positiva y la β-hCG negativa.",
  "diagnostico_final": "Enfermedad inflamatoria pélvica leve por Chlamydia trachomatis, de manejo ambulatorio.",
  "diagnosticos_diferenciales": [
   {"dx": "Embarazo ectópico", "por_que_no": "La β-hCG negativa lo descarta; siempre debe excluirse primero."},
   {"dx": "Apendicitis aguda", "por_que_no": "Dolor bilateral con signos pélvicos y sin irritación peritoneal; ecografía sin otra causa."},
   {"dx": "Pielonefritis o infección urinaria", "por_que_no": "Sin dolor lumbar ni piuria en el examen de orina."},
   {"dx": "Cervicitis aislada", "por_que_no": "El dolor a la movilización cervical y anexial indica compromiso del tracto superior."}],
  "datos_clave": ["Dolor pélvico bajo con flujo mucopurulento y fiebre.", "Pareja nueva sin preservativo y antecedente de infección vaginal.", "Dolor a la movilización cervical y anexial (criterio clínico mínimo).", "β-hCG negativa y ausencia de signos peritoneales (permiten el tratamiento ambulatorio)."],
  "razonamiento": ["En una mujer en edad fértil con dolor pélvico, descartar embarazo y ectópico primero.", "Buscar criterios clínicos de EIP: dolor pélvico y dolor a la movilización cervical o anexial.", "Evaluar la gravedad: fiebre alta, náuseas, signos peritoneales, absceso o embarazo.", "Pedir estudios para clamidia, gonococo, VIH y sífilis y, según el caso, ecografía.", "Tratar de inmediato con un esquema combinado sin esperar los resultados.", "Tratar y notificar a la pareja, reevaluar a las 72 horas y dar signos de alarma.", "Ofrecer consejería, vacunación y revisión de anticoncepción."],
  "interpretacion_laboratorio": ["β-hCG negativa: descarta embarazo y, con él, un ectópico.", "NAAT positivo para clamidia: confirma el agente; el gonococo fue negativo.", "VIH, sífilis y hepatitis B no reactivos: no hay coinfección actual (se repiten según riesgo).", "Leucocitos y PCR elevados: inflamación sistémica, compatible con EIP."],
  "tratamiento": [
   {"item": "Antibióticos", "detalle": "Cefalosporina intramuscular más doxiciclina y metronidazol durante 14 días, según el esquema de la guía vigente.", "dosis": "Las dosis y la elección exacta de fármacos deben tomarse de la guía CDC y del protocolo local; no se fijan aquí."},
   {"item": "Pareja", "detalle": "Evaluar, tratar y notificar a la pareja; abstinencia hasta completar el tratamiento.", "dosis": "No aplica."},
   {"item": "Seguimiento", "detalle": "Reevaluar a las 72 horas; derivar si no hay mejoría, si hay absceso, embarazo o intolerancia a la vía oral.", "dosis": "No aplica."},
   {"item": "Prevención", "detalle": "Consejería, vacunación (VPH y hepatitis B), prueba de VIH y sífilis periódicas y revisión de la anticoncepción.", "dosis": "No aplica."}],
  "temas_relacionados": ["Enfermedad inflamatoria pélvica", "Infecciones de transmisión sexual", "Embarazo ectópico"],
  "mensaje_clave": "En dolor pélvico en edad fértil: primero descarta embarazo; la EIP se trata de inmediato con esquema combinado y se maneja a la pareja."
 }
}
guardar_consulta(c)
