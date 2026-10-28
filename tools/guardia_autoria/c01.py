from lib import *
def A(id, texto, resp, rel): return {"id": id, "texto": texto, "respuesta": resp, "relevancia": rel}
def T(id, cat, nombre, clasif, just, res, esencial=False, bloqueante=False, cambia=None, critico=False):
    t = {"id": id, "categoria": cat, "nombre": nombre, "clasificacion": clasif, "justificacion": just, "resultado": res}
    if esencial: t["esencial"] = True
    if bloqueante: t["bloqueante"] = True; t["mensaje_bloqueo"] = "Todavía no tienes datos de función tiroidea que permitan confirmar o descartar la sospecha y decidir con seguridad: reconsidera los estudios de laboratorio antes de formular el diagnóstico."
    if cambia: t["cambia_conducta"] = cambia
    if critico: t["tiempo_critico"] = True
    return t
def LAB(titulo, items): return {"tipo": "lab", "titulo": titulo, "lab": [dict({"prueba": x[0], "valor": x[1]}, **({"etiqueta": x[2]} if len(x) > 2 and x[2] else {}), **({"ref": x[3]} if len(x) > 3 and x[3] else {})) for x in items]}
def TXT(texto): return {"tipo": "texto", "texto": texto}
REF = ["r2", "r1"]
c = {
 "id": "c01", "modalidad": "consulta", "titulo": "Cansancio, aumento de peso y frío en una mujer de 38 años", "especialidad": "Medicina interna · Endocrinología", "dificultad": 2, "duracion_min": 18,
 "areas_banco": ["endocrinologia"],
 "resumen": "Consulta ambulatoria de una mujer con síntomas de seis meses. Realiza la anamnesis y el examen, decide qué pruebas pedir, interpreta los resultados y define el tratamiento y el seguimiento.",
 "contexto": "Consultorio de medicina interna de un hospital: laboratorio general, ecografía y derivación a endocrinología disponibles.",
 "paciente": {"edad": 38, "edad_texto": "38 años", "sexo": "F", "embarazo": False},
 "motivo": "«Doctor, me siento cansada todo el tiempo, he subido de peso y siento mucho frío.»",
 "referencias": [
  R("r2", "guia", "Guía técnica: guía de práctica clínica para el diagnóstico y tratamiento de hipotiroidismo primario del adulto en el Hospital de Emergencias Villa El Salvador", "Hospital de Emergencias Villa El Salvador (MINSA, Perú)", "Hospital de Emergencias Villa El Salvador", 2024, "Guía institucional de un hospital (no una guía nacional de MINSA); no se pudo confirmar el número de la resolución directoral que la aprobó (fecha estimada por el archivo: 2024). Su texto se basa en ATA 2014 y NICE 2019.", "Propone TSH como primera prueba con T4 libre si la TSH está alta, levotiroxina como tratamiento de elección (1,6 µg/kg/día en menores de 65 años sin enfermedad cardiovascular; 25 a 50 µg/día con titulación en mayores de 65 años o con enfermedad cardiovascular) y control de TSH cada 3 meses hasta estabilizarla y luego una vez al año; no recomienda la ecografía ni la gammagrafía de rutina.", url="https://cdn.www.gob.pe/uploads/document/file/6161140/5435978-guia-de-practica-clinica-para-el-diagnostico-y-tratamiento-de-hipotiroidismo-primario-del-adulto.pdf"),
  R("r1", "guia", "Clinical practice guidelines for hypothyroidism in adults: cosponsored by the American Association of Clinical Endocrinologists and the American Thyroid Association", "American Thyroid Association / American Association of Clinical Endocrinologists", "Garber JR, Cobin RH, Gharib H et al.", 2012, "Guía de 2012; puede haber actualizaciones o guías más recientes que no se consultaron en esta sesión (solo el resumen de PubMed).", "El diagnóstico de hipotiroidismo primario se basa en la TSH elevada con T4 libre baja; el tratamiento de elección es la levotiroxina en monoterapia, y el seguimiento se hace con TSH tras el ajuste de dosis.", pmid="22954017", doi="10.1089/thy.2012.0205"),
 ],
 "discrepancias": ["No se encontró una guía nacional de MINSA ni de EsSalud de hipotiroidismo del adulto; sí una guía institucional del Hospital de Emergencias Villa El Salvador (leída completa), que sigue ATA 2014 y NICE 2019 y propone TSH cada 3 meses hasta estabilizar, mientras la ATA/AACE 2012 (solo se leyó su resumen) indica 6 a 8 semanas. El calendario exacto de controles (TSH a las 6 a 8 semanas tras ajustar la dosis) y la dosis por peso se toman de la práctica habitual y del protocolo local: confirma en la guía y no se fijan dosis aquí.", "Los intervalos de laboratorio son educativos, no de un laboratorio peruano; el anticuerpo anti-TPO y la TSH dependen del ensayo."],
 "anamnesis": [
  {"categoria": "Enfermedad actual", "preguntas": [
   A("a1", "¿Desde cuándo tiene el cansancio y cómo ha evolucionado?", "Unos 6 meses, cada vez peor. Me cuesta levantarme por las mañanas.", "clave"),
   A("a2", "¿Ha cambiado su peso en este tiempo?", "Subí unos 7 kilos sin cambiar lo que como.", "clave"),
   A("a3", "¿Cómo tolera el frío y el calor?", "Siento frío casi todo el tiempo, aun en verano; mis compañeras están en polo y yo con chompa.", "clave"),
   A("a4", "¿Cómo es su evacuación intestinal?", "Estreñida: voy al baño cada tres o cuatro días.", "util"),
   A("a5", "¿Cómo están su ánimo y su concentración?", "Más apagada y se me olvidan las cosas del trabajo.", "util"),
   A("a6", "¿Ha notado palpitaciones, temblor o sudoración?", "No, al contrario, siento el corazón lento.", "util"),
   A("a7", "¿Tiene dolor en el pecho o falta de aire?", "No tengo dolor ni falta de aire.", "baja")]},
  {"categoria": "Ginecológico y planificación", "preguntas": [
   A("a8", "¿Cómo son sus menstruaciones?", "Me baja cada 25 días y sangro más que antes.", "util"),
   A("a9", "¿Podría estar embarazada o planea estarlo pronto?", "Mi última regla fue hace dos semanas, uso preservativo y no planeo embarazarme por ahora.", "clave")]},
  {"categoria": "Hábitos y medicación", "preguntas": [
   A("a10", "¿Toma medicamentos, suplementos o productos naturales?", "Ninguno regularmente; a veces un multivitamínico.", "util"),
   A("a11", "¿Fuma o consume alcohol?", "No fumo y tomo alcohol muy rara vez.", "baja"),
   A("a12", "¿Ha recibido radiación en el cuello o ha tenido una cirugía del cuello?", "No, nunca.", "util")]}],
 "antecedentes": [
  {"id": "h1", "nombre": "Antecedentes familiares", "texto": "Madre con una enfermedad de la tiroides en tratamiento con una pastilla diaria. Padre sano.", "relevancia": "clave"},
  {"id": "h2", "nombre": "Antecedentes personales", "texto": "Sin enfermedades conocidas. No diabetes ni hipertensión.", "relevancia": "util"},
  {"id": "h3", "nombre": "Antecedentes gineco-obstétricos", "texto": "Una gestación y un parto por cesárea hace seis años, sin complicaciones.", "relevancia": "util"},
  {"id": "h4", "nombre": "Alergias y medicación", "texto": "Sin alergias conocidas. Sin medicación habitual.", "relevancia": "baja"}],
 "examen": [
  {"id": "e1", "region": "General", "maniobra": "Signos vitales y antropometría", "hallazgo": "PA 118/76 mmHg, FC 56 /min, T 36,1 °C, FR 14 /min. Peso 78 kg, IMC 29.", "relevancia": "clave"},
  {"id": "e2", "region": "Cuello", "maniobra": "Palpación de la tiroides", "hallazgo": "Aumento difuso y pequeño de la glándula, de consistencia firme, indoloro, sin nódulos ni adenopatías.", "relevancia": "clave"},
  {"id": "e3", "region": "Piel y anexos", "maniobra": "Inspección de la piel y el cabello", "hallazgo": "Piel seca y fría, cabello quebradizo, cejas laterales ralas.", "relevancia": "util"},
  {"id": "e4", "region": "Neurológico", "maniobra": "Reflejos osteotendinosos", "hallazgo": "Fase de relajación lenta del reflejo aquíleo.", "relevancia": "util"},
  {"id": "e5", "region": "Cara y extremidades", "maniobra": "Búsqueda de edema", "hallazgo": "Edema facial leve y pretibial sin fóvea.", "relevancia": "util"},
  {"id": "e6", "region": "Cardiopulmonar", "maniobra": "Auscultación cardíaca y pulmonar", "hallazgo": "Ruidos cardíacos rítmicos y lentos, sin soplos. Pulmones limpios.", "relevancia": "baja"},
  {"id": "e7", "region": "Abdomen", "maniobra": "Palpación abdominal", "hallazgo": "Blando, depresible, sin masas ni dolor.", "relevancia": "baja"}],
 "hipotesis": {"max": 3, "opciones": [
  {"id": "d1", "dx": "Hipotiroidismo primario (probable tiroiditis autoinmune)", "tipo": "principal", "nota": "Síntomas y signos típicos, bocio difuso firme y antecedente familiar tiroideo."},
  {"id": "d2", "dx": "Anemia ferropénica por menstruaciones abundantes", "tipo": "diferencial", "nota": "Explica el cansancio y puede coexistir, pero no el frío, la bradicardia ni el bocio."},
  {"id": "d3", "dx": "Trastorno depresivo", "tipo": "diferencial", "nota": "Puede dar cansancio y alteración de la concentración, pero no explica el aumento de peso con frío, la piel seca ni el bocio."},
  {"id": "d4", "dx": "Síndrome de ovario poliquístico", "tipo": "diferencial", "nota": "Puede asociar aumento de peso y alteraciones menstruales; no explica la bradicardia, el frío ni el bocio."},
  {"id": "d5", "dx": "Apnea obstructiva del sueño", "tipo": "diferencial", "nota": "Explica la fatiga y el aumento de peso, pero no los hallazgos físicos tiroideos."},
  {"id": "d6", "dx": "Hipertiroidismo", "tipo": "distractor", "nota": "Cursa con pérdida de peso, intolerancia al calor y taquicardia: el cuadro es el opuesto."},
  {"id": "d7", "dx": "Insuficiencia suprarrenal primaria", "tipo": "distractor", "nota": "Cursa con pérdida de peso, hipotensión y pigmentación, que no hay."},
  {"id": "d8", "dx": "Diabetes mellitus tipo 2", "tipo": "distractor", "nota": "Puede dar cansancio y aumento de peso, pero no explica el frío, la bradicardia ni el bocio."}]},
 "pruebas": [
  T("p1", "Endocrinología", "TSH", "prioritaria", "Es la prueba inicial de elección ante la sospecha de enfermedad tiroidea primaria.", LAB("TSH", [("tsh", 18.6)]), esencial=True, bloqueante=True, cambia="La TSH confirma el hipotiroidismo primario y fija la indicación de tratamiento."),
  T("p2", "Endocrinología", "T4 libre", "prioritaria", "Con la TSH elevada permite distinguir el hipotiroidismo clínico del subclínico y orientar el tratamiento.", LAB("T4 libre", [("t4l", 0.5)]), esencial=True, cambia="Diferencia hipotiroidismo clínico de subclínico y modifica la urgencia y la dosis de inicio."),
  T("p3", "Endocrinología", "Anticuerpos anti-TPO", "razonable", "Apoya la etiología autoinmune y el pronóstico de progresión, aunque no cambia el tratamiento inicial.", LAB("Anti-TPO", [("anti_tpo", 420)])),
  T("p4", "Hematología", "Hemograma completo", "razonable", "Útil por el cansancio y las menstruaciones abundantes: puede mostrar anemia asociada.", LAB("Hemograma", [("hemoglobina", 11.2), ("leucocitos", 6.1), ("plaquetas", 280), ("vcm", 86)])),
  T("p5", "Bioquímica", "Perfil lipídico (colesterol total y LDL)", "razonable", "El hipotiroidismo puede elevar el colesterol; ayuda a valorar el riesgo cardiovascular.", LAB("Perfil lipídico", [("colesterol_total", 248), ("ldl", 162)])),
  T("p6", "Bioquímica", "Glucosa en ayunas", "razonable", "Descarta una diabetes como contribuyente al cansancio y al aumento de peso.", LAB("Glucosa", [("glucosa", 92)])),
  T("p7", "Bioquímica", "Creatinina sérica", "razonable", "Valora la función renal antes de iniciar un tratamiento prolongado y descarta otra causa de fatiga.", LAB("Creatinina", [("creatinina", 0.8)])),
  T("p8", "Endocrinología", "β-hCG en sangre", "razonable", "Una mujer en edad fértil debe descartar un embarazo antes de iniciar tratamiento y antes de estudios con radiación.", LAB("β-hCG", [("bhcg", 1.2)])),
  T("p9", "Hematología", "Ferritina", "razonable", "Orienta a un déficit de hierro por menstruaciones abundantes, que puede coexistir con el hipotiroidismo.", LAB("Ferritina", [("ferritina", 22)])),
  T("p10", "Imagen", "Ecografía de tiroides", "razonable", "Confirma el bocio difuso y descarta nódulos, sin ser imprescindible para iniciar el tratamiento.", TXT("Glándula tiroides aumentada de tamaño con ecogenicidad difusamente heterogénea, sin nódulos sólidos ni adenopatías.")),
  T("p11", "Endocrinología", "T3 total o libre", "innecesaria", "En el hipotiroidismo primario no aporta al diagnóstico ni modifica la conducta; puede ser normal.", TXT("T3 dentro de lo esperable para este patrón: no cambia el diagnóstico ni el manejo.")),
  T("p12", "Endocrinología", "Cortisol sérico matutino", "innecesaria", "No hay sospecha clínica de insuficiencia suprarrenal (sin hipotensión ni pérdida de peso).", TXT("Cortisol matutino dentro de lo esperable. Sin relevancia para el caso.")),
  T("p13", "Imagen", "Resonancia magnética de silla turca", "innecesaria", "El cuadro corresponde a un hipotiroidismo primario; la hipófisis se estudia solo si la TSH es baja o inapropiadamente normal con T4 libre baja.", TXT("No se realiza: sin indicación. Se evita un estudio costoso sin utilidad.")),
  T("p14", "Imagen", "Punción aspirativa con aguja fina de tiroides", "innecesaria", "No hay nódulos sospechosos; no se punciona un bocio difuso sin nódulos.", TXT("No se realiza: sin nódulos, no hay indicación de punción.")),
  T("p15", "Imagen", "Gammagrafía tiroidea con yodo radiactivo", "danina", "Expone a radiación sin indicación en una mujer en edad fértil, y la captación no cambia el manejo de un hipotiroidismo evidente.", TXT("No se realiza: sin indicación y con radiación innecesaria en una paciente en edad fértil.")),
  T("p16", "Imagen", "Tomografía de cuello con contraste yodado", "danina", "La sobrecarga de yodo y la radiación son innecesarias; el contraste puede alterar la función tiroidea y no aporta al diagnóstico.", TXT("No se realiza: la sobrecarga de yodo puede alterar el cuadro sin aportar al diagnóstico.")),
 ],
 "preguntas": {
  "interpretacion": Q("¿Cómo interpretas los resultados de laboratorio?", [
   D("Hipotiroidismo primario clínico con anti-TPO positivo, compatible con tiroiditis autoinmune y anemia leve asociada", "o", "", "La TSH alta con T4 libre baja define un hipotiroidismo primario; el anti-TPO apoya la etiología autoinmune y la hemoglobina baja es un hallazgo asociado."),
   D("Hipotiroidismo central por falla hipofisaria, pues la T4 libre es baja y debe estudiarse la hipófisis con resonancia magnética", "i", "", "En el hipotiroidismo central la TSH es baja o inapropiadamente normal; aquí está muy elevada, lo que indica enfermedad primaria."),
   D("Hipotiroidismo subclínico, con TSH aumentada y T4 libre normal, que no requiere ninguna medida adicional por ahora", "i", "", "La T4 libre está baja: se trata de un hipotiroidismo clínico, no subclínico."),
   D("Hipertiroidismo con anticuerpos positivos, por lo que corresponde iniciar antitiroideos y beta bloqueo de manera inmediata", "p", "", "La TSH elevada con T4 libre baja indica hipotiroidismo; los antitiroideos empeorarían la función tiroidea."),
   D("Síndrome del enfermo eutiroideo por una enfermedad aguda de fondo, con función tiroidea que se normalizará sin tratamiento", "i", "", "No hay enfermedad aguda grave; el patrón con bocio y anticuerpos corresponde a una enfermedad tiroidea primaria."),
  ], tema="Interpretación de la función tiroidea", comp="dx", refs=REF, peso=2),
  "diagnostico": Q("¿Cuál es el diagnóstico más probable?", [
   D("Hipotiroidismo primario por tiroiditis crónica autoinmune (tiroiditis de Hashimoto) con bocio difuso y antecedente familiar", "o", "", "Reúne síntomas típicos, bocio difuso firme, antecedente familiar tiroideo, TSH alta con T4 libre baja y anti-TPO positivo."),
   D("Hipotiroidismo por déficit de yodo, frecuente en zonas con baja ingesta, como causa principal en esta paciente de la costa", "i", "", "Hay anticuerpos positivos y antecedente familiar; la causa más probable es autoinmune, no el déficit de yodo."),
   D("Tiroiditis subaguda con fase hipotiroidea, que cursa con dolor cervical y requiere antiinflamatorios y observación posterior", "i", "", "No hubo dolor ni cuadro viral previo y la tiroides no es dolorosa: no corresponde a una tiroiditis subaguda."),
   D("Enfermedad de Graves en fase de agotamiento con hipotiroidismo, para la cual corresponde tratamiento con antitiroideos de síntesis", "p", "", "No hay antecedentes de hipertiroidismo; los antitiroideos empeorarían la función tiroidea en una paciente hipotiroidea."),
   D("Depresión mayor con síntomas somáticos, sin enfermedad tiroidea de fondo, que debe tratarse con un antidepresivo por varias semanas", "i", "", "Los hallazgos físicos y de laboratorio demuestran una enfermedad tiroidea; tratar solo la depresión deja sin tratar la causa."),
  ], tema="Diagnóstico del hipotiroidismo", comp="dx", refs=REF, peso=3),
  "tratamiento": Q("¿Qué tratamiento indicas?", [
   D("Levotiroxina oral en ayunas con dosis ajustada al peso y a la edad, en monoterapia, con explicación de la adherencia", "o", "", "La levotiroxina en monoterapia es el tratamiento de elección del hipotiroidismo; se toma en ayunas y su dosis se ajusta al peso y a la TSH."),
   D("Liotironina (T3) como tratamiento inicial por su acción más rápida sobre los síntomas de la paciente fatigada", "i", "", "La T3 sola o combinada no es el tratamiento recomendado de rutina; la levotiroxina en monoterapia es el estándar."),
   D("Extracto de tiroides desecado de origen animal por considerarse un tratamiento más natural y bien tolerado", "i", "", "No se recomienda: el contenido hormonal es variable y no hay ventaja sobre la levotiroxina."),
   D("Observación sin tratamiento durante seis meses y repetir la TSH, dado que los síntomas son inespecíficos y comunes", "i", "", "Con TSH muy elevada y T4 libre baja con síntomas, el tratamiento está indicado; esperar prolonga el cuadro."),
   D("Metimazol a dosis bajas para regular la función tiroidea hasta que la TSH se normalice por completo en los controles", "p", "", "El metimazol reduce la producción hormonal: empeoraría un hipotiroidismo ya presente."),
  ], tema="Tratamiento del hipotiroidismo", comp="tto", refs=REF, peso=2),
  "seguimiento": Q("¿Cuál es el plan de seguimiento, los signos de alarma y los criterios de derivación?", [
   D("Control programado de TSH tras iniciar el tratamiento, con signos de alarma y derivación ante nódulos o falta de respuesta", "o", "", "La TSH se controla de forma programada tras iniciar o ajustar la dosis (la guía peruana del hospital propone cada 3 meses hasta estabilizarla y la ATA/AACE, a las 6 a 8 semanas); se educa sobre los signos de sobredosificación y se deriva ante nódulos, falta de respuesta o dudas diagnósticas."),
   D("Control de TSH recién al año, sin ajustes intermedios, porque la levotiroxina alcanza su efecto estable de forma inmediata y completa", "i", "", "El efecto pleno tarda semanas: el control inicial es mucho más frecuente (cada 6 semanas a 3 meses según la guía) y solo luego pasa a ser anual."),
   D("Suspender la levotiroxina cuando desaparezcan los síntomas y repetir la TSH solo si reaparecen en los meses siguientes", "i", "", "El hipotiroidismo autoinmune requiere tratamiento sostenido; la mejoría de síntomas no es motivo de suspensión."),
   D("Derivar a todas las pacientes a cirugía de tiroides por el bocio difuso y diferir cualquier tratamiento médico hasta la operación", "p", "", "Un bocio difuso por tiroiditis no requiere cirugía; derivar a operar sin indicación expone a riesgos innecesarios."),
   D("Control de la TSH solo si la paciente refiere síntomas nuevos y sin explicar a la paciente los signos de sobredosificación", "i", "", "El seguimiento debe ser programado y la paciente debe conocer los signos de sobredosificación para consultar a tiempo."),
  ], tema="Seguimiento del hipotiroidismo", comp="dis", refs=REF, peso=2),
 },
 "informe": {
  "resumen_clinico": "Mujer de 38 años con seis meses de cansancio, aumento de peso, intolerancia al frío, estreñimiento y menstruaciones abundantes, con bradicardia, piel seca, bocio difuso firme y antecedente familiar de enfermedad tiroidea.",
  "diagnostico_final": "Hipotiroidismo primario por tiroiditis crónica autoinmune (Hashimoto), con anemia leve asociada.",
  "diagnosticos_diferenciales": [
   {"dx": "Anemia ferropénica", "por_que_no": "Puede coexistir (hay hemoglobina baja y ferritina baja) pero no explica el bocio, la bradicardia ni el frío."},
   {"dx": "Depresión", "por_que_no": "No explica el aumento de peso con frío, el bocio ni la TSH elevada."},
   {"dx": "Síndrome de ovario poliquístico", "por_que_no": "No explica la bradicardia, el bocio ni la alteración tiroidea."},
   {"dx": "Hipotiroidismo central", "por_que_no": "La TSH muy elevada indica una causa primaria."}],
  "datos_clave": ["Cansancio, aumento de peso e intolerancia al frío de seis meses.", "Bradicardia, piel seca, relajación lenta de reflejos y bocio difuso firme.", "Antecedente familiar de enfermedad tiroidea.", "Mujer en edad fértil sin gestación (importante antes de tratar y de pedir estudios con radiación)."],
  "razonamiento": ["Reunir los síntomas y signos que orientan a hipotiroidismo y descartar el cuadro opuesto.", "Preguntar por embarazo y planificación y por antecedentes familiares tiroideos.", "Explorar la tiroides y buscar signos de hipotiroidismo.", "Pedir primero TSH y T4 libre; completar con estudios razonables según el contexto.", "Interpretar el patrón (TSH alta, T4 libre baja, anti-TPO positivo).", "Tratar con levotiroxina en monoterapia y programar el control de TSH.", "Educar sobre signos de alarma y derivar si hay nódulos o falta de respuesta."],
  "interpretacion_laboratorio": ["TSH muy alta y T4 libre baja: hipotiroidismo primario clínico.", "Anti-TPO alto: apoya una causa autoinmune.", "Hemoglobina y ferritina bajas: anemia leve por déficit de hierro asociada.", "Colesterol total y LDL altos: dislipidemia secundaria que suele mejorar al tratar el hipotiroidismo."],
  "tratamiento": [
   {"item": "Levotiroxina", "detalle": "Monoterapia oral en ayunas con dosis ajustada al peso, la edad y las comorbilidades.", "dosis": "Guía del Hospital de Emergencias Villa El Salvador (adultos < 65 años sin enfermedad cardiovascular): 1,6 µg/kg/día, o 50 µg/día con aumentos de 25 µg cada 2 a 3 meses; 25 a 50 µg/día con titulación si ≥ 65 años o enfermedad cardiovascular. Confirma con tu protocolo."},
   {"item": "Seguimiento", "detalle": "Control de TSH tras el inicio o el ajuste de dosis (ATA/AACE: a las 6 a 8 semanas; guía del Hospital de Emergencias Villa El Salvador: cada 3 meses hasta estabilizar) y luego una vez al año.", "dosis": "No aplica."},
   {"item": "Anemia por déficit de hierro", "detalle": "Tratar según protocolo si se confirma el déficit.", "dosis": "Según protocolo institucional."},
   {"item": "Signos de alarma y derivación", "detalle": "Palpitaciones, temblor o pérdida de peso (sobredosificación); aparición de nódulos o crecimiento rápido del cuello; falta de respuesta o duda diagnóstica.", "dosis": "No aplica."}],
  "temas_relacionados": ["Hipotiroidismo y tiroiditis de Hashimoto", "Interpretación de la función tiroidea", "Dislipidemia secundaria"],
  "mensaje_clave": "Ante síntomas de hipotiroidismo, la TSH con T4 libre confirman el diagnóstico; se trata con levotiroxina en monoterapia y se controla la TSH."
 }
}
guardar_consulta(c)
