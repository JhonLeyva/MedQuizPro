# -*- coding: utf-8 -*-
"""Lote 2 · parte B (cirugía general: hernias, vía biliar, trauma, quemaduras, ano)."""
from lote02a import Q, L, SAB, SCH

Q(a="cirugia", cat=None, tema="Operación de Hartmann en la diverticulitis Hinchey IV", año=2015, ext=True,
  e="¿Cuál es la operación de elección en una diverticulitis sigmoidea complicada con peritonitis generalizada (Hinchey IV)?",
  o=["Whipple.", "Devine.", "Miles.", "Hartmann.", "Kock."], k="D",
  c="La peritonitis fecal (Hinchey IV) o purulenta (III) por diverticulitis es una emergencia quirúrgica. El procedimiento clásico es la operación de Hartmann: resección del sigmoides perforado, cierre del muñón rectal y colostomía terminal; se prefiere en pacientes inestables, inmunodeprimidos o con contaminación franca. En pacientes estables se puede hacer resección con anastomosis primaria y estoma derivativo de protección (ileostomía), con menor morbilidad a largo plazo; el lavado laparoscópico no se recomienda en la peritonitis fecal. La reconstrucción del tránsito se hace a los 3-6 meses, aunque hasta un 40 % de los pacientes con Hartmann nunca se reconecta. Whipple es la pancreatoduodenectomía; Miles, la resección abdominoperineal del recto; Devine, una colostomía en asa; Kock, un reservorio ileal continente.",
  f="WSES, diverticulitis aguda del colon izquierdo (2020); ASCRS, diverticulitis (2020); " + SAB)

Q(a="cirugia", cat=None, tema="Reparación herniaria sin tensión", año=2015, ext=True,
  e="¿Cuál es la técnica quirúrgica de reparación herniaria sin tensión?",
  o=["Mayo.", "Bassini.", "Lichtenstein.", "McVay.", "Shouldice."], k="C",
  c="Una reparación «sin tensión» no aproxima tejidos bajo tensión: cubre el defecto con una malla protésica de polipropileno. La técnica de Lichtenstein coloca la malla sobre la pared posterior del conducto inguinal y la fija al pubis y al ligamento inguinal, con una hendidura para el cordón. Las técnicas de Bassini, Shouldice, McVay y Mayo reparan con tejidos propios (con tensión), con recidivas altas, y hoy solo se usan si hay contraindicación a la malla (campo infectado o estrangulación con necrosis). La reparación laparoscópica (TEP o TAPP) también es sin tensión. Dolor crónico, seroma, hematoma e infección de la malla son las complicaciones más frecuentes.",
  f="EHS, guías de hernia de la ingle (2018); " + SAB)

Q(a="cirugia", cat=None, tema="Hernia de Spiegel", año=2015, ext=True,
  e="¿Cómo se llama la hernia que protruye a través de la línea semilunar (borde externo de los rectos)?",
  o=["Richter.", "Spiegel.", "Littré.", "Amyand.", "Want."], k="B",
  c="La hernia de Spiegel es una hernia ventral lateral que protruye por la aponeurosis de Spiegel, entre el borde lateral del recto abdominal (línea semilunar) y la línea arqueada, casi siempre por debajo del ombligo. Suele ser interparietal (queda cubierta por el oblicuo externo) y se palpa mal; la ecografía o la TC la confirman. Se repara por su riesgo de estrangulación. Otros epónimos: Richter (solo un lado de la pared intestinal queda atrapado, sin obstrucción completa), Littré (contiene un divertículo de Meckel), Amyand (contiene el apéndice) y Garengeot (apéndice en una hernia femoral). La hernia de Petit y la de Grynfelt son lumbares.",
  f="EHS, hernias ventrales; " + SAB + "; " + SCH)

Q(a="cirugia", cat=None, tema="Saco herniario directo: refuerzo de la pared posterior", año=2015, ext=False,
  e="Estibador de 48 años presenta hace 6 meses tumoración blanda en región inguinal derecha, reductible, es intervenido quirúrgicamente por hernioplastia. El cirujano encuentra un saco herniario directo. ¿Cuál es el manejo quirúrgico más recomendado?",
  o=["Invaginación.", "Resección.", "Refuerzo.", "Sin tratamiento.", "Ligadura."], k="C",
  c="En la hernia inguinal directa el saco protruye por la pared posterior del conducto inguinal (triángulo de Hesselbach), que está debilitada; la causa es la debilidad de la fascia transversalis y no un saco peritoneal que pueda ligarse. Por eso el saco se invagina o se reduce, sin resecarlo, y el tratamiento es el refuerzo de la pared posterior con malla (Lichtenstein o abordaje laparoscópico). En la hernia indirecta (congénita o del anillo interno) se hace la ligadura alta del saco y se repara el anillo. La hernia de un trabajador con esfuerzos físicos frecuentes tiene un riesgo mayor de recidiva: se recomienda malla y evitar cargar peso durante 2-4 semanas.",
  f="EHS, guías de hernia de la ingle (2018); " + SAB)

Q(a="cirugia", cat=None, tema="Quemadura de segundo grado profundo", año=2015, ext=True,
  e="Las quemaduras que comprometen desde la epidermis hasta la zona profunda de la dermis se clasifican como de:",
  o=["Segundo grado superficial.", "Segundo grado profundo.", "Primer grado.", "Tercer grado.", "Cuarto grado."], k="B",
  c="La profundidad de la quemadura se clasifica así: primer grado, solo epidermis (eritema doloroso, sin ampollas: quemadura solar); segundo grado superficial, hasta la dermis papilar (ampollas, base rosada húmeda, muy dolorosa, cura en 2-3 semanas sin cicatriz); segundo grado profundo, hasta la dermis reticular (base blanquecina o roja moteada, menos dolorosa, sensible solo a la presión, el pelo se arranca con facilidad, cura en más de 3 semanas con cicatriz hipertrófica y suele requerir injerto); tercer grado, espesor total (acartonada, indolora, no blanquea a la presión, requiere escarectomía e injerto); y cuarto grado, compromete fascia, músculo o hueso. La profundidad se reevalúa a las 48-72 horas.",
  f="ABA, Burn Care Guidelines; ISBI, Practice Guidelines for Burn Care (2016 y 2018); " + SCH)

Q(a="cirugia", cat=None, tema="Causa más frecuente de obstrucción en el adulto no operado", año=2015, ext=False,
  e="¿Cuál es la causa más frecuente de obstrucción intestinal en el adulto no operado?",
  o=["Hernias.", "Adherencias.", "Vólvulo.", "Cáncer de sigmoides.", "Diverticulosis."], k="A",
  c="En el adulto sin cirugía abdominal previa la causa más frecuente de obstrucción del intestino delgado es una hernia de la pared abdominal (inguinal, crural o umbilical) complicada con encarcelación o estrangulación, por eso toda obstrucción sin cicatriz quirúrgica obliga a explorar las regiones herniarias, incluso la femoral en mujeres ancianas. Las adherencias son la primera causa en el paciente operado; los tumores (colon izquierdo), el vólvulo de sigmoides y la enfermedad de Crohn siguen en frecuencia. En países en desarrollo el vólvulo de sigmoides y el íleo por áscaris pueden ser relativamente frecuentes. Una hernia no reductible con obstrucción es una emergencia quirúrgica.",
  f="WSES, obstrucción adhesiva (2018); " + SAB + "; Harrison Principios de Medicina Interna 22.ª ed.")

Q(a="cirugia", cat=None, tema="Íleo biliar: aerobilia y obstrucción", año=2015, ext=False,
  e="Mujer de 45 años, con antecedente de dispepsia a las grasas de varios años, presenta dolor tipo cólico en hipocondrio derecho que cede con antiespasmódicos. Acude a Emergencia por persistencia del dolor y distensión abdominal, náusea, vómitos y flatulencias. Rx simple de abdomen: aerobilia, asas delgadas dilatadas y niveles hidroaéreos. ¿Cuál es el diagnóstico más probable?",
  o=["Íleo funcional.", "Colecistitis aguda.", "Íleo biliar.", "Bridas y adherencias.", "Pancreatitis aguda."], k="C",
  c="Aerobilia (aire en el árbol biliar) más obstrucción del intestino delgado configura el íleo biliar: un cálculo grande (> 2,5 cm) pasa de la vesícula al duodeno por una fístula colecistoentérica (por inflamación crónica) y se impacta, sobre todo en el íleon terminal. Es más frecuente en mujeres ancianas con colelitiasis de larga data. La tríada de Rigler incluye obstrucción intestinal, aerobilia y cálculo ectópico. La TC es la prueba más sensible. El tratamiento es quirúrgico: enterolitotomía y extracción del cálculo, con colecistectomía y cierre de la fístula solo en el mismo tiempo si el paciente es joven y estable. El síndrome de Bouveret es la variante en el duodeno o el estómago. La colecistitis y la pancreatitis no producen aerobilia.",
  f=SAB + "; " + SCH + "; WSES, obstrucción adhesiva (2018)")

Q(a="cirugia", cat=None, tema="Lavado peritoneal diagnóstico positivo", año=2015, ext=False,
  e="Mujer de 25 años que, luego de un accidente de tránsito, ingresa a Emergencia por dolor abdominal difuso y progresivo. Funciones vitales: PA 100/50, pulso 95 por minuto, abdomen doloroso a la palpación en mesogastrio. Ecografía normal. Se decide realizar lavado peritoneal diagnóstico: leucocitos mayores de 500 por cc y eritrocitos mayores de 100 000 por cc. ¿Cuál es la conducta inmediata a seguir?",
  o=["Laparoscopía diagnóstica.", "Catéter venoso central.", "TAC abdominal.", "Laparotomía exploradora.", "Resonancia magnética."], k="D",
  c="El lavado peritoneal diagnóstico (LPD) es positivo con más de 10 mL de sangre en la aspiración, más de 100 000 eritrocitos/mm³, más de 500 leucocitos/mm³, bilis, contenido intestinal o amilasa elevada. En el trauma abdominal cerrado con LPD positivo y hemodinamia comprometida (PA 100/50, taquicardia leve), la conducta es la laparotomía exploradora. Hoy el LPD se usa poco: el FAST es la prueba inicial y la TC con contraste es el estudio en el paciente estable. En un paciente estable con LPD positivo, una TC puede precisar las lesiones de órganos sólidos tratables sin operar. La laparoscopía diagnóstica se reserva para el paciente estable en trauma penetrante o con dudas de lesión diafragmática.",
  f="ATLS, 11.ª ed. (2025); WSES, trauma abdominal cerrado (2017); " + SCH)

Q(a="cirugia", cat=None, tema="Maniobra de Pringle en lesión hepática", año=2015, ext=False,
  e="Durante la intervención quirúrgica de un paciente con traumatismo abdominal por arma de fuego, se evidencia lesión hepática grado II, para controlar el sangrado se decide realizar la maniobra de Pringle. ¿En qué consiste?",
  o=["Ligadura de arteria hepática común.", "Oclusión de la vena porta.", "Oclusión transitoria del ligamento hepatoduodenal.", "Ligadura del ligamento redondo.", "Taponamiento hepático."], k="C",
  c="La maniobra de Pringle consiste en comprimir con los dedos o con un clamp atraumático el ligamento hepatoduodenal (borde libre del epiplón menor), que contiene la tríada portal (vena porta, arteria hepática y colédoco), para ocluir de forma temporal el flujo de entrada al hígado y controlar el sangrado. Se tolera hasta 60 minutos en un hígado sano (se hace de forma intermitente: 15 minutos con 5 de descanso). Si el sangrado persiste a pesar de la maniobra, indica lesión de las venas suprahepáticas o de la cava retrohepática, es decir, sangrado «de salida». Se maneja con empaquetamiento perihepático, resección y cirugía de control de daños, y en centros con experiencia, exclusión vascular total. El orificio de Winslow es el punto de referencia.",
  f="ATLS, 11.ª ed. (2025); WSES, trauma hepático (2020); " + SCH)

Q(a="cirugia", cat=None, tema="Regla de los nueves en quemaduras", año=2015, ext=True,
  e="Varón de 30 años sufre quemadura con agua hervida. Examen: lesión que compromete ambas caras anteriores de las extremidades inferiores. Según la regla de los nueves, ¿cuál es la extensión de la quemadura?",
  o=["36 %.", "27 %.", "18 %.", "45 %.", "9 %."], k="C",
  c="La regla de Wallace (de los nueves) estima la superficie corporal quemada en el adulto: cabeza y cuello 9 %; cada miembro superior 9 %; tronco anterior 18 %; tronco posterior 18 %; cada miembro inferior 18 % (9 % la cara anterior y 9 % la posterior); genitales 1 %. Las caras anteriores de ambas piernas suman 9 % + 9 % = 18 %. En niños, la cabeza es proporcionalmente mayor (usar Lund-Browder) y la palma del paciente con los dedos equivale a cerca del 1 %. Solo se cuentan las quemaduras de segundo y tercer grado. Con estos datos se calcula la reposición: fórmula de Parkland, 4 mL × kg × % SCQ en 24 horas, la mitad en las primeras 8 horas desde la quemadura; objetivo diuresis de 0,5 mL/kg/h.",
  f="ABA, Burn Care Guidelines; ISBI, Practice Guidelines for Burn Care (2016 y 2018); " + SCH)

Q(a="cirugia", cat=None, tema="Eventración complicada", año=2015, ext=True,
  e="Mujer de 40 años cesareada en 3 oportunidades con tumoración parcialmente reductible a nivel de cicatriz operatoria mediana infraumbilical, hace 6 horas presenta dolor intenso tipo cólico y nota que la tumoración ha aumentado y no se reduce, con náuseas y vómitos. Examen: T 37 °C, PA 120/80 mmHg, FC 90 por minuto. Abdomen distendido, doloroso, con tumoración infraumbilical de 15 × 10 cm no reductible, ruidos hidroaéreos incrementados. ¿Cuál es el diagnóstico probable?",
  o=["Síndrome adherencial.", "Íleo adinámico.", "Eventración complicada.", "Hernia de Spiegel.", "Absceso de pared."], k="C",
  c="Una tumoración reductible sobre la cicatriz de una laparotomía previa es una eventración (hernia incisional). Cuando la masa se vuelve irreductible y dolorosa, con vómitos, distensión y aumento de ruidos hidroaéreos, se trata de una eventración complicada con obstrucción intestinal (incarcerada, con o sin estrangulación). Factores de riesgo: cirugías repetidas, obesidad, infección de herida, tabaquismo y diabetes. Tratamiento: cirugía urgente con reducción o resección del asa comprometida y reparación del defecto; en hernias grandes se prefiere malla (retrorrectal o preperitoneal) y, si hay contaminación, solo cierre primario con reparación diferida. La recidiva es mayor cuando se repara solo con suturas (hasta 50 %).",
  f="EHS, hernias incisionales (2015); " + SAB)

Q(a="cirugia", cat=None, tema="Maniobra de Pringle: hígado", año=2015, ext=True,
  e="¿En qué órgano lesionado se aplica la maniobra de Pringle?",
  o=["Bazo.", "Riñón.", "Cava.", "Hígado.", "Aorta."], k="D",
  c="La maniobra de Pringle se aplica en las lesiones hepáticas con hemorragia: al comprimir el pedículo hepático (vena porta, arteria hepática y colédoco) se interrumpe de forma temporal la entrada de sangre al hígado y se valora si el sangrado es «de entrada» (portal o arterial) o «de salida» (venas suprahepáticas, cava). La oclusión se tolera hasta 60 minutos. El bazo se controla con compresión manual o esplenectomía; el riñón, con compresión y control vascular del hilio; la aorta, con clampaje supraceliaco o REBOA; la cava, con presión directa. Las lesiones hepáticas grado IV y V (AAST) con inestabilidad requieren cirugía de control de daños, empaquetamiento y reintervención.",
  f="ATLS, 11.ª ed. (2025); WSES, trauma hepático (2020); " + SCH)

Q(a="cirugia", cat=None, tema="Fístula anal: secreción fétida cerca del ano", año=2015, ext=False,
  e="Chofer de 45 años que periódicamente presenta salida de secreción fétida por un orificio a un centímetro del ano. ¿Cuál es el diagnóstico más probable?",
  o=["Forúnculo.", "Hemorroides.", "Fisura.", "Absceso.", "Fístula."], k="E",
  c="La fístula perianal es un trayecto entre la cripta anal infectada (glándula criptoglandular) y la piel perianal. Se manifiesta como un orificio externo con secreción purulenta o fétida intermitente, prurito y episodios de dolor cuando se cierra y se forma un absceso. Más del 90 % proviene de un absceso perianal previo drenado de forma espontánea o quirúrgica. La regla de Goodsall orienta el trayecto: los orificios posteriores a la línea transversa se dirigen a la línea media posterior en trayecto curvo, y los anteriores, de forma radial recta. La clasificación de Parks (interesfintérica, transesfintérica, supraesfintérica y extraesfintérica) guía la cirugía: fistulotomía en las simples, y seton, colgajo de avance o LIFT en las complejas, para preservar la continencia. Una fístula recurrente exige descartar enfermedad de Crohn.",
  f="ASCRS, abscesos y fístulas anorrectales (2022); " + SAB)

Q(a="cirugia", cat=None, tema="Colecistitis aguda litiásica: cirugía precoz", año=2015, ext=False,
  e="Mujer de 40 años con antecedente de dispepsia a grasas, que hace 12 horas presenta dolor tipo cólico continuo en hemiabdomen superior y sensación de alza térmica. Examen: ictericia de escleras. Abdomen: dolor a la palpación en hipocondrio derecho, Murphy positivo, ruidos hidroaéreos escasos, leucocitos 18 000 con 9 abastonados. Ecografía: vesícula biliar distendida con pared engrosada e imagen de cálculo en el bacinete. ¿Cuál es la conducta a seguir?",
  o=["Cirugía urgente.", "Hidratación.", "Antibioticoterapia.", "Antiespasmódico.", "Cirugía electiva."], k="A",
  c="Dolor de más de 6 horas en hipocondrio derecho, Murphy positivo, leucocitosis con desviación a la izquierda y ecografía con vesícula distendida, pared engrosada y cálculo en el bacinete confirman una colecistitis aguda litiásica. La ictericia leve sugiere compresión del colédoco por el cálculo del bacinete (síndrome de Mirizzi) o coledocolitiasis asociada, que debe descartarse. El tratamiento definitivo es la colecistectomía laparoscópica temprana, dentro de las primeras 72 horas y hasta 7 días del inicio, que reduce complicaciones y estancia frente a la cirugía diferida (Guías de Tokio 2018 y WSES 2020). Se inicia con hidratación, analgesia y antibióticos. La cirugía electiva a las 6-8 semanas se reserva a pacientes de alto riesgo que mejoran con tratamiento médico o drenaje percutáneo de la vesícula.",
  f="Guías de Tokio 2018 (TG18); WSES, colecistitis aguda (2020); " + SAB,
  nota="El libro habla de «cirugía urgente»; hoy se recomienda colecistectomía laparoscópica temprana (≤ 72 h).")

Q(a="cirugia", cat=None, tema="Absceso perianal: drenaje", año=2015, ext=False,
  e="Varón de 40 años que hace 48 horas presenta tumoración evidente en región perianal, progresiva e invalidante. El dolor se intensifica al sentarse, caminar y defecar. Examen: tumoración flogótica y dolorosa a la palpación en región perianal. ¿Cuál es la conducta a seguir?",
  o=["Ecografía de partes blandas.", "Drenaje quirúrgico.", "Proctoscopía urgente.", "Anoscopía.", "Antibioticoterapia."], k="B",
  c="Una tumoración perianal dolorosa con signos de flogosis (calor, rubor, fluctuación) es un absceso perianal criptoglandular. Como todo absceso, su tratamiento es el drenaje quirúrgico inmediato, en consulta con anestesia local o en sala si es profundo, con incisión cercana al margen anal para reducir el trayecto de una futura fístula. Los antibióticos solo se asocian en diabetes, inmunosupresión, celulitis extensa o prótesis valvulares. Aproximadamente el 30-50 % de los abscesos evoluciona a fístula. Los abscesos isquiorrectales y supraelevadores se diagnostican con TC o RM. En el diabético con dolor desproporcionado, crepitación y fiebre, descartar gangrena de Fournier (necrosis perineal): desbridamiento urgente y antibióticos de amplio espectro.",
  f="ASCRS, abscesos y fístulas anorrectales (2022); " + SAB)

Q(a="cirugia", cat=None, tema="Signo de Murphy", año=2015, ext=True,
  e="El signo de Murphy es característico de:",
  o=["Colecistitis aguda.", "Apendicitis aguda.", "Pancreatitis aguda.", "Úlcera perforada.", "Diverticulitis."], k="A",
  c="El signo de Murphy es la interrupción brusca de la inspiración (apnea) por dolor al palpar el borde costal derecho sobre la línea medioclavicular mientras el paciente inspira profundo: el fondo vesicular inflamado desciende y golpea la mano. Es característico de la colecistitis aguda y tiene una sensibilidad cercana al 65 % y una especificidad del 87 %. El signo de Murphy ecográfico (dolor al comprimir la vesícula con el transductor) mejora el rendimiento. En ancianos y diabéticos puede faltar. Otros signos: Boas (dolor referido bajo la escápula derecha), Courvoisier-Terrier (vesícula palpable no dolorosa e ictericia: neoplasia de la cabeza del páncreas). La apendicitis se asocia con Blumberg, Rovsing y psoas.",
  f="Guías de Tokio 2018 (TG18); " + SAB)

Q(a="cirugia", cat=None, tema="Coledocolitiasis: papiloesfinterotomía endoscópica", año=2015, ext=True,
  e="¿Cuál es el tratamiento de elección en una coledocolitiasis?",
  o=["Colangiografía transparietohepática.", "Coledocotomía más dren de Kehr.", "Esfinteroplastía transduodenal.", "Coledocotomía convencional.", "Papiloesfinterotomía endoscópica."], k="E",
  c="El tratamiento actual de la coledocolitiasis es endoscópico: CPRE con esfinterotomía de la papila y extracción de los cálculos con balón o canastilla (éxito del 90-95 %). Se indica de rutina si hay colangitis, pancreatitis biliar con obstrucción persistente o cálculo visible en la imagen; en probabilidad intermedia se confirma antes con colangiorresonancia o ecoendoscopía. Si no se puede por vía endoscópica, se hace exploración quirúrgica de la vía biliar (coledocotomía con sonda de Kehr o coledocoscopía), a menudo junto con la colecistectomía laparoscópica. La esfinteroplastia transduodenal y la coledocoduodenostomía quedaron para casos seleccionados. La clave oficial de ese examen (Kehr) fue anulada por la comisión.",
  f="ASGE, coledocolitiasis (2019); ESGE, cálculos de la vía biliar (2019); Guías de Tokio 2018 (TG18)",
  nota="El libro reconoce que la clave publicada (coledocotomía con Kehr) fue errónea; se reconstruyó la opción E.")

Q(a="cirugia", cat=None, tema="Incisión en trauma abdominal penetrante", año=2015, ext=True,
  e="¿Cuál es la incisión de elección en un paciente que presenta una herida de bala en el abdomen?",
  o=["Paramediana.", "Subcostal.", "Transversa.", "Mediana.", "Boca de horno."], k="D",
  c="En la laparotomía urgente por trauma (arma de fuego o herida penetrante) la incisión de elección es la mediana xifopúbica: es rápida, avascular, permite explorar toda la cavidad y se amplía según la necesidad (supra o infraumbilical). Las incisiones subcostales, transversas o paramedianas limitan el acceso, tardan más y no permiten ver los cuatro cuadrantes. La secuencia es: control de la hemorragia (empaquetamiento, compresión, clamp), control de la contaminación (suturas, grapas) y exploración sistemática; en inestabilidad, cirugía de control de daños con cierre temporal y reintervención a las 24-48 horas («triada letal»: hipotermia, acidosis y coagulopatía).",
  f="ATLS, 11.ª ed. (2025); WSES, trauma abdominal penetrante (2017); " + SCH)

Q(a="cirugia", cat=None, tema="Apendicitis plastronada en el anciano: TC", año=2016, ext=False,
  e="¿Cuál es el estudio de imagen de elección en un anciano con sospecha de apendicitis aguda plastronada?",
  o=["Tomografía axial computarizada.", "Resonancia magnética nuclear.", "Ecografía abdominal.", "Gammagrafía.", "Rx simple de abdomen de pie."], k="A",
  c="En el adulto, y más en el anciano, que presenta pocos síntomas y complicaciones frecuentes, la tomografía con contraste es el estudio de elección en la apendicitis: tiene una sensibilidad y especificidad cercanas al 95-98 %, muestra el apéndice engrosado (> 6 mm) con inflamación de la grasa, apendicolitos, plastrón, absceso o perforación, y excluye otros diagnósticos (diverticulitis, cáncer de colon). La ecografía es de primera línea en niños y gestantes (seguida de RM). En el plastrón apendicular (masa inflamatoria con epiplón y asas adheridas) el manejo inicial es conservador con antibióticos, y si hay absceso mayor de 3-4 cm, drenaje percutáneo; la apendicectomía de intervalo se discute y en mayores de 40 años se pide colonoscopía para descartar neoplasia.",
  f="WSES, apendicitis aguda (2020); ACR, criterios de adecuación (dolor en fosa ilíaca derecha); " + SAB)

Q(a="cirugia", cat=None, tema="Medida inicial en la obstrucción intestinal (sonda nasogástrica)", año=2016, ext=False,
  e="¿Cuál es la medida inicial indicada en un paciente con obstrucción intestinal?",
  o=["Sonda nasogástrica.", "Dieta líquida.", "Antibióticos.", "Observación.", "Cirugía."], k="A",
  c="Toda obstrucción intestinal requiere dos medidas inmediatas y simultáneas: la descompresión con sonda nasogástrica (alivia la distensión, el vómito y el riesgo de aspiración) y la reposición enérgica de líquidos y electrolitos por vía endovenosa, con ayuno. Se pide también balance hídrico, sonda vesical y analgesia. Los antibióticos se agregan si hay sospecha de estrangulación; la cirugía urgente se indica ante peritonitis, estrangulación, obstrucción en asa cerrada o hernia complicada. En la obstrucción adhesiva parcial se puede administrar contraste hidrosoluble (gastrografín), que reduce la necesidad de cirugía y acorta la estancia. La dieta oral empeora la distensión y el vómito.",
  f="WSES, obstrucción adhesiva del intestino delgado (2018); " + SAB,
  nota="La clave original tenía dos respuestas (sonda nasogástrica e hidratación); se reemplazó la opción B por «dieta líquida».")

Q(a="cirugia", cat=None, tema="Hemorroides de tercer grado", año=2016, ext=False,
  e="Mujer de 60 años con estreñimiento crónico, dolor y sangrado rojo rutilante a la defecación, acompañado de protrusión de un «bulto» por el ano que la reduce con la mano. ¿Cuál es el tipo de hemorroides que presenta?",
  o=["Interna de tercer grado.", "Interna de cuarto grado.", "Interna de primer grado.", "Externa trombosada.", "Interna de segundo grado."], k="A",
  c="El sangrado rojo rutilante indoloro con el esfuerzo y el prolapso de tejido que se reduce con el dedo corresponde a hemorroides internas de tercer grado (prolapsan con el esfuerzo y requieren reducción manual). El dolor intenso con tumoración azulada dura sugiere trombosis hemorroidal externa. El estreñimiento y el esfuerzo crónico son factores de riesgo. Tratamiento: fibra, líquidos y evitar el pujo; ligadura con banda elástica, escleroterapia o coagulación infrarroja para grados I-III; hemorroidectomía (Milligan-Morgan o Ferguson, o grapada) para los grados III-IV o con mala respuesta. En una mujer de 60 años con sangrado rectal se debe descartar cáncer colorrectal con colonoscopía.",
  f="ASCRS, hemorroides (2018); " + SAB)

Q(a="cirugia", cat=None, tema="Hemorroides grado IV: tratamiento", año=2016, ext=False,
  e="¿Cuál es el tratamiento de elección en un paciente con hemorroides grado IV?",
  o=["Hemorroidectomía.", "Esfinterotomía.", "Esfinteroplastía.", "Esclerosis.", "Dieta."], k="A",
  c="Las hemorroides de grado IV permanecen prolapsadas y no se reducen; también se operan las de grado III sintomáticas que no responden a las medidas instrumentales, las hemorroides mixtas con componente externo y las trombosadas complicadas. La hemorroidectomía (Milligan-Morgan abierta o Ferguson cerrada) tiene la menor recidiva, aunque con más dolor posoperatorio; la hemorroidopexia con grapas y la desarterialización guiada por Doppler son alternativas con menos dolor y más recidiva de prolapso. Complicaciones: sangrado, retención urinaria, estenosis anal e incontinencia. La esfinterotomía lateral interna es el tratamiento de la fisura anal crónica. La dieta con fibra, la esclerosis y la ligadura corresponden a los grados I-II.",
  f="ASCRS, hemorroides (2018); " + SAB)

Q(a="cirugia", cat=None, tema="Fase proliferativa de la cicatrización", año=2016, ext=False,
  e="La fase proliferativa de la cicatrización de las heridas está entre los 4 y los 12 días. ¿Cuál es la característica de esta etapa?",
  o=["Formación de tejido de granulación.", "Detención de la síntesis del colágeno.", "Gran actividad de macrófagos.", "Invasión de los linfocitos a la herida.", "Disminuye la proliferación de células endoteliales."], k="A",
  c="La cicatrización tiene cuatro fases: hemostasia (minutos), inflamatoria (1-4 días, con neutrófilos y luego macrófagos), proliferativa (4-21 días) y de remodelación (hasta 1-2 años). En la fase proliferativa los fibroblastos sintetizan colágeno tipo III, aumenta la angiogénesis por VEGF (proliferan las células endoteliales), se forma el tejido de granulación (rosado, vascular y granular), los queratinocitos reepitelizan y los miofibroblastos contraen la herida. En la remodelación, el colágeno tipo III se sustituye por colágeno tipo I, la cicatriz gana fuerza hasta el 80 % de la piel normal. La falta de vitamina C, la desnutrición, la diabetes, los corticoides y la infección retrasan la fase proliferativa.",
  f=SAB + "; " + SCH + "; WUWHS, consenso sobre el cuidado de heridas")

Q(a="cirugia", cat=None, tema="Hernia inguinal mixta (en pantalón): Nyhus IIIB", año=2016, ext=False,
  e="Varón de 70 años es operado con el diagnóstico de hernia inguinal izquierda; en el hallazgo operatorio se encuentra que la hernia es de tipo indirecto, con anillo interno dilatado, saco herniario que comprime medialmente la fascia transversal del triángulo de Hesselbach, con contenido deslizado de vísceras en forma de pantalón. ¿Cuál es el tipo de hernia dentro de la clasificación de Nyhus?",
  o=["III-B.", "III-A.", "I.", "II.", "IV."], k="A",
  c="La clasificación de Nyhus ordena las hernias inguinales: tipo I, indirecta con anillo interno normal; II, indirecta con anillo interno dilatado y pared posterior intacta; III, defecto de la pared posterior (IIIA directa, IIIB indirecta con anillo muy dilatado que invade la pared posterior, incluida la hernia en pantalón y la deslizada, y IIIC femoral); IV, recurrente (A directa, B indirecta, C femoral, D combinada). La hernia en pantalón tiene un saco directo e indirecto a ambos lados de los vasos epigástricos inferiores, y por tanto una pared posterior debilitada: se clasifica como IIIB. Se repara con malla (Lichtenstein o laparoscópica) y se reducen o resecan los sacos.",
  f="EHS, guías de hernia de la ingle (2018); " + SAB)

Q(a="cirugia", cat=None, tema="Causa más frecuente de recidiva de hernia incisional", año=2016, ext=False,
  e="¿Cuál es la causa más frecuente de recidiva de una hernia incisional mayor de 3 cm?",
  o=["Reparación primaria con sutura.", "Edad avanzada.", "Malnutrición.", "Ascitis.", "Embarazo."], k="A",
  c="La reparación de una eventración con simple sutura de los bordes (herniorrafia) tiene recidivas de hasta el 40-50 % a 10 años, porque se hace con tensión sobre tejidos debilitados. Con malla protésica de refuerzo (retromuscular o preperitoneal, con solapamiento de 5 cm) la recidiva baja al 10 % o menos, y es el estándar en defectos mayores de 2-3 cm. Otros factores de recidiva: obesidad, tabaquismo, diabetes, infección de la herida, EPOC y aumento de presión intraabdominal. En hernias grandes se usan técnicas de separación de componentes o la inyección preoperatoria de toxina botulínica. El control previo de peso, tabaco y glucemia reduce las complicaciones.",
  f="EHS, hernias incisionales (2015); " + SAB)
