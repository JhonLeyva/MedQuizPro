from clib import *
REF = ["r2", "r1"]
c = {
 "id": "c04", "modalidad": "consulta", "titulo": "Dolor de garganta intenso y fiebre en un joven de 22 años", "especialidad": "Medicina familiar · Infectología", "dificultad": 1, "duracion_min": 15,
 "areas_banco": ["infectologia"],
 "resumen": "Consulta ambulatoria por dolor de garganta febril. Realiza la anamnesis y el examen, solicita pruebas con criterio y define el tratamiento, los signos de alarma y el seguimiento.",
 "contexto": "Consultorio de medicina familiar con prueba rápida de antígeno estreptocócico, laboratorio básico y referencia a otorrinolaringología.",
 "paciente": {"edad": 22, "edad_texto": "22 años", "sexo": "M", "embarazo": False},
 "motivo": "«Me duele muchísimo la garganta desde hace dos días, me duele al tragar y tengo fiebre.»",
 "referencias": [
  R("r2", "guia", "Guía técnica: guía de práctica clínica para el diagnóstico y tratamiento de la faringitis aguda en el paciente pediátrico del Hospital de Emergencias Villa El Salvador", "Hospital de Emergencias Villa El Salvador (MINSA, Perú)", "Hospital de Emergencias Villa El Salvador", 2024, "Guía institucional de un hospital para niños de 1 mes a 14 años: este caso es un adulto de 22 años, así que se usa solo como apoyo parcial. No se pudo confirmar la resolución directoral ni el año exacto.", "Usa la escala de Centor modificada para decidir la prueba rápida de antígeno y el antibiótico; el cultivo no es necesario de rutina; no recomienda imágenes, indica que los títulos de antiestreptolisina (ASLO) no aportan valor diagnóstico y que la proteína C reactiva no da información útil; recomienda amoxicilina o penicilina por 10 días en estreptocócica; señala como alarma los síntomas de obstrucción de la vía aérea y refiere ante sospecha de complicaciones supurativas.", url="https://cdn.www.gob.pe/uploads/document/file/7412689/6317614-guia-de-practica-clinica-para-el-diagnostico-y-tratamiento-de-la-faringitis-aguda-en-el-paciente-pediatrico.pdf"),
  R("r1", "guia", "Clinical practice guideline for the diagnosis and management of group A streptococcal pharyngitis: 2012 update by the Infectious Diseases Society of America", "Infectious Diseases Society of America (IDSA)", "Shulman ST, Bisno AL, Clegg HW, Gerber MA et al.", 2012, "Guía de 2012; puede haber actualizaciones no consultadas en esta sesión (solo se leyó el resumen de PubMed).", "La penicilina o la amoxicilina siguen siendo los tratamientos de elección; para pacientes alérgicos a la penicilina se incluye ahora la clindamicina. Se recomienda confirmar el diagnóstico con una prueba (antígeno rápido o cultivo) antes de tratar.", pmid="22965026", doi="10.1093/cid/cis629"),
 ],
 "discrepancias": ["Solo se leyó el resumen de la guía IDSA 2012: la duración (10 días de penicilina o amoxicilina), las alternativas y la política de cultivo tras una prueba rápida negativa en adultos se basan en la práctica habitual y deben confirmarse en la guía y en la norma local. La única guía peruana hallada es pediátrica (Hospital de Emergencias Villa El Salvador, niños hasta 14 años) y se usa solo como apoyo; no hay una norma nacional para adultos. No se fijan dosis.", "Los intervalos de laboratorio son educativos, no de un laboratorio peruano."],
 "anamnesis": [
  {"categoria": "Enfermedad actual", "preguntas": [
   A("a1", "¿Desde cuándo y cómo ha evolucionado el dolor de garganta?", "Hace dos días; empezó de golpe y cada vez me duele más al tragar.", "clave"),
   A("a2", "¿Tiene tos, mocos, ronquera o dificultad para respirar?", "No tengo tos ni mocos ni ronquera.", "clave"),
   A("a3", "¿Ha tenido fiebre y cuánto?", "Fiebre de 39 °C con escalofríos desde ayer.", "clave"),
   A("a4", "¿Tiene dolor de cabeza, náuseas o dolor abdominal?", "Dolor de cabeza y un poco de náuseas.", "util"),
   A("a5", "¿Puede tragar saliva y abrir la boca con normalidad?", "Sí puedo tragar saliva y abrir la boca.", "clave"),
   A("a6", "¿Ha cambiado su voz o tiene babeo?", "Mi voz es normal, no babeo.", "util"),
   A("a7", "¿Tiene erupción en la piel o fatiga marcada en los últimos días?", "No tengo erupciones; me siento cansado por la fiebre.", "util")]},
  {"categoria": "Antecedentes pertinentes", "preguntas": [
   A("a8", "¿Alguien cercano tuvo amigdalitis o faringitis recientemente?", "Mi compañero de cuarto estuvo con dolor de garganta la semana pasada.", "util"),
   A("a9", "¿Es alérgico a la penicilina o a algún antibiótico?", "No soy alérgico a ningún medicamento.", "clave"),
   A("a10", "¿Ha tenido fiebre reumática o enfermedad del corazón?", "Nunca he tenido fiebre reumática ni problemas del corazón.", "util"),
   A("a11", "¿Cuántas veces al año tiene dolor de garganta?", "Una o dos veces al año, nunca con complicaciones.", "baja"),
   A("a12", "¿Tiene conductas sexuales de riesgo o síntomas de otras infecciones?", "No, con una sola pareja estable y sin síntomas.", "baja")]}],
 "antecedentes": [
  {"id": "h1", "nombre": "Personales", "texto": "Sin enfermedades crónicas. Sin cirugías. Vacunas completas.", "relevancia": "util"},
  {"id": "h2", "nombre": "Alergias y medicación", "texto": "Sin alergias conocidas. No toma medicación habitual.", "relevancia": "clave"},
  {"id": "h3", "nombre": "Exposición", "texto": "Convive con un compañero que tuvo dolor de garganta la semana anterior.", "relevancia": "util"},
  {"id": "h4", "nombre": "Familiares", "texto": "Sin antecedentes familiares relevantes.", "relevancia": "baja"}],
 "examen": [
  {"id": "e1", "region": "General", "maniobra": "Signos vitales", "hallazgo": "T 38,9 °C, FC 100 /min, FR 16 /min, PA 118/72 mmHg, SatO₂ 99 %.", "relevancia": "clave"},
  {"id": "e2", "region": "Orofaringe", "maniobra": "Inspección de la orofaringe y las amígdalas", "hallazgo": "Amígdalas hipertróficas y eritematosas con exudado blanquecino; petequias en el paladar; úvula en la línea media.", "relevancia": "clave"},
  {"id": "e3", "region": "Cuello", "maniobra": "Palpación de ganglios cervicales", "hallazgo": "Ganglios cervicales anteriores aumentados de tamaño y dolorosos.", "relevancia": "clave"},
  {"id": "e4", "region": "Cuello", "maniobra": "Búsqueda de trismo, rigidez o abombamiento peritonsilar", "hallazgo": "Sin trismo, sin abombamiento peritonsilar ni desviación de la úvula; voz normal.", "relevancia": "clave"},
  {"id": "e5", "region": "Abdomen", "maniobra": "Palpación del abdomen", "hallazgo": "Blando, sin esplenomegalia ni dolor.", "relevancia": "util"},
  {"id": "e6", "region": "Piel", "maniobra": "Inspección de la piel", "hallazgo": "Sin erupción cutánea.", "relevancia": "util"},
  {"id": "e7", "region": "Respiratorio", "maniobra": "Auscultación pulmonar", "hallazgo": "Murmullo vesicular normal, sin ruidos agregados.", "relevancia": "baja"}],
 "hipotesis": {"max": 3, "opciones": [
  {"id": "d1", "dx": "Faringoamigdalitis aguda estreptocócica (estreptococo del grupo A)", "tipo": "principal", "nota": "Inicio brusco con fiebre, exudado, ganglios anteriores dolorosos y ausencia de tos."},
  {"id": "d2", "dx": "Faringitis viral", "tipo": "diferencial", "nota": "Es la causa más frecuente en general, pero aquí faltan la tos y los síntomas catarrales y hay exudado."},
  {"id": "d3", "dx": "Mononucleosis infecciosa", "tipo": "diferencial", "nota": "Posible en adultos jóvenes con faringitis y ganglios, pero sin esplenomegalia ni fatiga marcada."},
  {"id": "d4", "dx": "Absceso periamigdalino", "tipo": "diferencial", "nota": "Es una complicación que debe descartarse; aquí no hay trismo ni desviación de la úvula."},
  {"id": "d5", "dx": "Infección aguda por VIH", "tipo": "diferencial", "nota": "Puede iniciar con faringitis, pero no hay riesgo ni otras manifestaciones."},
  {"id": "d6", "dx": "Epiglotitis aguda", "tipo": "distractor", "nota": "Cursa con estridor, voz apagada y dificultad respiratoria, que no hay."},
  {"id": "d7", "dx": "Reflujo gastroesofágico", "tipo": "distractor", "nota": "No causa fiebre alta, exudado ni ganglios dolorosos."},
  {"id": "d8", "dx": "Neumonía", "tipo": "distractor", "nota": "Sin tos ni signos respiratorios."}]},
 "pruebas": [
  T("p1", "Microbiología", "Prueba rápida de antígeno de estreptococo del grupo A", "prioritaria", "Confirma el diagnóstico y evita tratar con antibióticos a quien tiene una faringitis viral.", LAB("Antígeno rápido", [("antigeno_estreptococo", "positivo")]), esencial=True, bloqueante="Sin una prueba que confirme la sospecha de estreptococo no puedes decidir con seguridad si corresponde o no un antibiótico: reconsidera las pruebas microbiológicas antes de diagnosticar.", cambia="Confirma la etiología y justifica el antibiótico.", critico=True),
  T("p2", "Microbiología", "Cultivo faríngeo", "razonable", "En adultos no se requiere cultivo de respaldo tras una prueba rápida positiva; es un estudio válido pero no imprescindible.", LAB("Cultivo faríngeo", [("cultivo_faringeo", "positivo: Streptococcus pyogenes")])),
  T("p3", "Serología", "Anticuerpos heterófilos (prueba para mononucleosis)", "razonable", "Se considera en adultos jóvenes con faringitis atípica; aquí no hay esplenomegalia ni fatiga marcada.", TXT("Negativo.")),
  T("p4", "Hematología", "Hemograma completo", "innecesaria", "No confirma ni descarta el estreptococo y no cambia la conducta en un adulto estable.", LAB("Hemograma", [("leucocitos", 13.5), ("hemoglobina", 14.8), ("plaquetas", 250)])),
  T("p5", "Inflamación", "Proteína C reactiva", "innecesaria", "No distingue la etiología bacteriana de la viral de forma útil en la faringitis aguda.", LAB("PCR", [("pcr", 5.1)])),
  T("p6", "Serología", "Título de antiestreptolisina O (ASLO)", "innecesaria", "Refleja una infección previa y no sirve para el diagnóstico de la faringitis aguda.", TXT("Resultado sin utilidad para la decisión actual.")),
  T("p7", "Serología", "Prueba de VIH", "razonable", "Ofrecerla es válido en adultos jóvenes, pero no forma parte del estudio de la faringitis aguda sin riesgo.", LAB("VIH", [("vih", "no reactivo")])),
  T("p8", "Imagen", "Radiografía lateral de cuello", "innecesaria", "No hay sospecha de absceso retrofaríngeo ni de cuerpo extraño: no aporta.", TXT("Sin hallazgos relevantes.")),
  T("p9", "Imagen", "Tomografía de cuello con contraste", "innecesaria", "Irradia y no se necesita sin signos de absceso profundo ni complicación.", TXT("No se realiza: radiación sin indicación en un paciente estable sin signos de absceso.")),
  T("p10", "Laboratorio", "Biopsia de amígdala", "danina", "Es invasiva y no tiene indicación en una amigdalitis aguda sin sospecha de neoplasia.", TXT("No se realiza: procedimiento invasivo sin indicación.")),
 ],
 "preguntas": {
  "interpretacion": Q("¿Cómo interpretas los hallazgos y los resultados?", [
   D("Faringitis estreptocócica confirmada: cuatro criterios clínicos de Centor y prueba rápida positiva, sin signos de complicación local", "o", "", "Fiebre, exudado, ganglios anteriores dolorosos y ausencia de tos dan una alta probabilidad, confirmada por la prueba rápida; no hay absceso."),
   D("Faringitis viral que no requiere antibiótico, con tratamiento sintomático y reevaluación solo si empeora en los próximos días de evolución", "i", "", "La prueba rápida positiva y la clínica de alta probabilidad confirman el estreptococo: el antibiótico está indicado."),
   D("Estado de portador asintomático del estreptococo sin enfermedad aguda, por lo que no se debe tratar a la persona", "i", "", "El cuadro agudo con fiebre, exudado y ganglios dolorosos no corresponde a un portador asintomático."),
   D("Mononucleosis infecciosa con riesgo de rotura esplénica que contraindica cualquier tratamiento antibiótico en este paciente", "i", "", "No hay esplenomegalia ni síntomas sistémicos sugestivos; la prueba confirma estreptococo y los heterófilos serían negativos."),
   D("Absceso periamigdalino en formación que obliga a drenaje quirúrgico urgente por otorrinolaringología sin otros estudios", "i", "", "No hay trismo, abombamiento ni desviación de la úvula: no se sospecha un absceso."),
  ], tema="Interpretación de la faringitis con criterios de Centor", comp="dx", refs=REF, peso=2),
  "diagnostico": Q("¿Cuál es el diagnóstico más probable?", [
   D("Faringoamigdalitis aguda por estreptococo del grupo A, no complicada, en un adulto joven sin alergia a la penicilina", "o", "", "Cumple los criterios clínicos, la prueba rápida es positiva y no hay signos de complicación."),
   D("Faringitis viral por adenovirus u otro virus respiratorio, autolimitada y manejada con tratamiento de soporte únicamente", "i", "", "La clínica sin tos y la prueba positiva orientan a estreptococo, no a una etiología viral."),
   D("Mononucleosis infecciosa por virus de Epstein-Barr, que requiere reposo y evitar amoxicilina por el riesgo de erupción", "i", "", "No hay fatiga marcada ni esplenomegalia y la prueba rápida de estreptococo es positiva."),
   D("Difteria faríngea con pseudomembranas, que requiere aislamiento y antitoxina de inmediato en el centro de referencia", "i", "", "El paciente tiene vacunas completas y el exudado es el de una amigdalitis; no hay pseudomembranas adherentes."),
   D("Amigdalitis crónica recurrente con indicación de amigdalectomía programada para evitar nuevos episodios infecciosos futuros", "i", "", "Es un primer episodio agudo; no hay recurrencias que justifiquen una amigdalectomía."),
  ], tema="Diagnóstico de la faringitis estreptocócica", comp="dx", refs=REF, peso=3),
  "tratamiento": Q("¿Qué tratamiento indicas?", [
   D("Penicilina o amoxicilina durante 10 días con analgésico y antipirético, explicando la importancia de completar el esquema", "o", "", "La penicilina o la amoxicilina siguen siendo el tratamiento de elección; se completa el curso para prevenir complicaciones."),
   D("Azitromicina durante 5 días como primera elección por su comodidad de dosificación en el adulto sin alergias", "i", "", "Los macrólidos son una alternativa para alérgicos a la penicilina; no son la primera elección en un paciente sin alergia."),
   D("Amoxicilina con ácido clavulánico por 14 días para cubrir la posible coinfección anaerobia en cualquier caso de amigdalitis", "i", "", "El espectro ampliado es innecesario: la penicilina o la amoxicilina bastan en la faringitis estreptocócica."),
   D("Un corticoide sistémico a dosis altas como único tratamiento, difiriendo el antibiótico hasta ver si persiste la fiebre", "i", "", "El corticoide no trata la infección; el antibiótico no debe diferirse con una prueba positiva."),
   D("Ciprofloxacino oral durante 7 días por su amplio espectro y su buena penetración en los tejidos de la garganta", "p", "", "Las fluoroquinolonas no se recomiendan en la faringitis estreptocócica: tienen un espectro inadecuado y un riesgo innecesario de efectos adversos."),
  ], tema="Tratamiento de la faringitis estreptocócica", comp="tto", refs=REF, peso=2),
  "seguimiento": Q("¿Cuál es el plan de seguimiento, los signos de alarma y los criterios de derivación?", [
   D("Hidratación, analgesia y reposo, volver ante trismo, babeo, voz apagada o fiebre más de 72 horas, y derivar si hay absceso", "o", "", "Estos signos sugieren absceso periamigdalino u otra complicación y obligan a reevaluar y derivar; la fiebre persistente indica falla del tratamiento."),
   D("Repetir el cultivo faríngeo al terminar el antibiótico en todos los pacientes asintomáticos para comprobar la erradicación bacteriana", "i", "", "No se recomienda el cultivo de control en pacientes asintomáticos tras el tratamiento."),
   D("Indicar amigdalectomía inmediata tras el primer episodio para prevenir futuras infecciones y complicaciones en este paciente joven", "p", "", "No está indicada tras un primer episodio; es un procedimiento con riesgos sin beneficio demostrado."),
   D("Dar el alta sin explicar signos de alarma ni cuándo volver, porque la faringitis estreptocócica suele evolucionar bien con antibiótico", "i", "", "El paciente debe conocer los signos de complicación y cuándo regresar."),
   D("Indicar penicilina benzatínica semanal por un año como profilaxis para evitar la fiebre reumática en este paciente sin antecedentes", "i", "", "La profilaxis prolongada se reserva para quienes tuvieron fiebre reumática; no corresponde a este paciente."),
  ], tema="Seguimiento y signos de alarma en la faringitis", comp="dis", refs=REF, peso=2),
 },
 "informe": {
  "resumen_clinico": "Varón de 22 años con dos días de dolor de garganta de inicio brusco, fiebre de 39 °C y ausencia de tos. El examen mostró amígdalas con exudado, petequias palatinas y ganglios cervicales anteriores dolorosos, sin signos de absceso. La prueba rápida de estreptococo fue positiva.",
  "diagnostico_final": "Faringoamigdalitis aguda por estreptococo del grupo A, no complicada.",
  "diagnosticos_diferenciales": [
   {"dx": "Faringitis viral", "por_que_no": "Faltan tos y síntomas catarrales y la prueba rápida fue positiva."},
   {"dx": "Mononucleosis infecciosa", "por_que_no": "Sin esplenomegalia ni fatiga marcada; los anticuerpos heterófilos fueron negativos."},
   {"dx": "Absceso periamigdalino", "por_que_no": "Sin trismo, abombamiento ni desviación de la úvula."},
   {"dx": "Infección aguda por VIH", "por_que_no": "Sin riesgo ni otras manifestaciones; la prueba fue no reactiva."}],
  "datos_clave": ["Inicio brusco, fiebre alta y ausencia de tos.", "Exudado amigdalino con ganglios cervicales anteriores dolorosos (criterios de Centor).", "Sin trismo, babeo ni cambio de voz (descarta absceso en este momento).", "Sin alergia a la penicilina."],
  "razonamiento": ["Aplicar los criterios clínicos (fiebre, exudado, ganglios dolorosos, ausencia de tos) para estimar la probabilidad.", "Descartar signos de gravedad y complicación (trismo, babeo, voz apagada, estridor).", "Confirmar con una prueba rápida de antígeno antes de usar antibiótico.", "Tratar con penicilina o amoxicilina completando el esquema.", "Aliviar el dolor y la fiebre con medidas de soporte.", "Dar signos de alarma y cuándo regresar; no pedir cultivo de control en asintomáticos.", "Derivar si hay absceso o falla del tratamiento."],
  "interpretacion_laboratorio": ["Antígeno rápido positivo: confirma el estreptococo del grupo A en un paciente de alta probabilidad.", "Cultivo faríngeo positivo (si se pidió): confirma, aunque no era imprescindible.", "Hemograma y PCR: leucocitosis y PCR altas inespecíficas, sin utilidad para decidir.", "Anticuerpos heterófilos negativos y VIH no reactivo: descartan los diferenciales evaluados."],
  "tratamiento": [
   {"item": "Antibiótico", "detalle": "Penicilina o amoxicilina durante 10 días (la clindamicina es una opción para alérgicos a la penicilina).", "dosis": "Dosis y presentación según la guía IDSA y el protocolo local; no se fijan aquí."},
   {"item": "Soporte", "detalle": "Hidratación, reposo, analgésico y antipirético (paracetamol).", "dosis": "Dosis por peso según protocolo."},
   {"item": "Seguimiento", "detalle": "Sin cultivo de control en asintomáticos; reevaluar si la fiebre persiste más de 48 a 72 horas.", "dosis": "No aplica."},
   {"item": "Signos de alarma y derivación", "detalle": "Trismo, babeo, voz apagada, dificultad respiratoria, dolor unilateral intenso o fiebre persistente: reevaluar y derivar si hay absceso.", "dosis": "No aplica."}],
  "temas_relacionados": ["Faringoamigdalitis aguda", "Criterios de Centor", "Fiebre reumática"],
  "mensaje_clave": "Confirma la sospecha de estreptococo con una prueba, trata con penicilina o amoxicilina completa y reconoce los signos de complicación."
 }
}
guardar_consulta(c)
