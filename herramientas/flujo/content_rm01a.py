# -*- coding: utf-8 -*-
"""Residentado Médico · lote 1 · flujogramas 1-25 (anatomía, fisiología y anestesiología)."""
from c_rm import S, P, PX, B, Q, L, TR, ATLS, HARRISON, WILLIAMS, NELSON, MINSA, ACOG, AAP
GRAY = "Gray Anatomía para estudiantes 5.ª ed."
MOORE = "Moore Anatomía con orientación clínica 8.ª ed."
PROPIO = "Esquema MedQuizPro (dibujo propio)"

# 1 · RM-CB-001 · TARJETAS: cartílagos de la laringe
S("tarjetas", "RM-CB-001", "Los cartílagos impares de la laringe son epiglotis, tiroides y cricoides",
  "Anatomía · esqueleto de la laringe",
  ("Cartílagos de la laringe", ["Nueve cartílagos: tres impares (grandes, estructurales) y tres pares (pequeños, móviles).",
                                 "Los impares sostienen; los pares mueven las cuerdas vocales."]),
  ("Pregunta de teoría", ["¿Cuál completa el trío de cartílagos impares?", "Epiglotis, tiroides y …"]),
  ["Impares: epiglotis, tiroides y cricoides. Pares: aritenoides, corniculados y cuneiformes (el triticio es inconstante).",
   "El cricoides es el único anillo completo de la vía aérea: sirve de referencia para la presión cricoidea y la cricotiroidotomía.",
   "La membrana cricotiroidea, entre tiroides y cricoides, es el sitio de la vía aérea quirúrgica de emergencia."],
  GRAY + "; Netter Atlas de Anatomía Humana 8.ª ed.; ATLS 11.ª ed. (2025).",
  op=("¿Tercer cartílago impar?", ["Sí: único anillo completo, base de la laringe", "No: es par y mueve las cuerdas vocales", "No: es par y pequeño (cartílago de Santorini)",
                                   "No: es par y está en el pliegue aritenoepiglótico", "No: inconstante, dentro del ligamento tirohioideo"]),
  d=dict(rotulo="Los cartílagos impares y uno de los pares", ans=0,
         cards=[dict(titulo="Cricoides", datos=[("Número", "Impar", True), ("Forma", "Anillo completo", True), ("Función", "Base de la laringe", True)], pie="Este caso: el tercero."),
                dict(titulo="Tiroides", datos=[("Número", "Impar", False), ("Forma", "Dos láminas (nuez)", False), ("Función", "Protege las cuerdas", False)], pie="El mayor de todos."),
                dict(titulo="Epiglotis", datos=[("Número", "Impar", False), ("Tejido", "Cartílago elástico", False), ("Función", "Cierra al deglutir", False)], pie="Evita la aspiración."),
                dict(titulo="Aritenoides", datos=[("Número", "Par", False), ("Forma", "Pirámide móvil", False), ("Función", "Abre y cierra la glotis", False)], pie="Luxación tras intubar.")]))

# 2 · RM-CB-002 · CUADRÍCULA: surcos y canales
S("cuadricula", "RM-CB-002", "La vena cefálica pasa por el surco deltopectoral, que hay que recordar en una flebotomía",
  "Anatomía · miembro superior",
  ("Vena cefálica", ["Vena superficial lateral del brazo: sube por el borde del bíceps.", "Termina en la vena axilar atravesando el surco entre deltoides y pectoral mayor."]),
  ("Pregunta de teoría", ["¿Por qué canal pasa la vena cefálica?", "Importa en la disección venosa."]),
  ["Surco deltopectoral: deltoides (lateral) y pectoral mayor (medial); contiene la vena cefálica y la rama deltoidea de la toracoacromial.",
   "Canal de Guyon (muñeca): nervio y arteria cubital. Surco bicipital: tendón de la cabeza larga del bíceps.",
   "Cefálica distal: cerca del nervio cutáneo lateral del antebrazo; el torniquete o la punción pueden lesionarlo."],
  MOORE + "; " + GRAY,
  op=("¿Por dónde pasa?", ["No: allí van el nervio y la arteria cubital (muñeca)", "No existe como canal anatómico del brazo", "Sí: entre deltoides y pectoral mayor",
                           "No: es el surco del tendón largo del bíceps", "No: es el surco del nervio radial en el húmero"]),
  d=dict(rotulo="¿Qué pasa por cada surco o canal?", alto_img=0,
         celdas=[("Surco deltopectoral", ["Vena cefálica (desemboca en la axilar)", "Este caso"], None, True),
                 ("Canal de Guyon", ["Nervio y arteria cubitales", "En la muñeca, junto al pisiforme"], None, False),
                 ("Surco bicipital", ["Tendón de la cabeza larga del bíceps", "Entre los tubérculos del húmero"], None, False),
                 ("Surco del nervio radial", ["Nervio radial y arteria braquial profunda", "En la cara posterior del húmero"], None, False)],
         veredicto=("Cefálica = surco deltopectoral", "Recuérdalo: «cefálica, cabeza del brazo, entre deltoides y pectoral».")))

# 3 · RM-CB-003 · RADIAL: ramas de las coronarias
S("radial", "RM-CB-003", "La arteria circunfleja es rama de la coronaria izquierda",
  "Anatomía · arterias coronarias",
  ("Arterias coronarias", ["Nacen en los senos aórticos: la izquierda se divide en descendente anterior y circunfleja.", "La derecha da marginal derecha y, casi siempre, la descendente posterior."]),
  ("Pregunta de teoría", ["¿De qué arteria nace la circunfleja?"]),
  ["Coronaria izquierda → descendente anterior (pared anterior y tabique) + circunfleja (pared lateral y posterior).",
   "Coronaria derecha → marginal derecha, nodo sinusal (55-60 %), nodo AV y descendente posterior en el 80 % (dominancia derecha).",
   "La mamaria interna no es coronaria: es el injerto preferido para la descendente anterior en la cirugía de revascularización."],
  MOORE + "; Braunwald Tratado de Cardiología 12.ª ed.; ESC, revascularización miocárdica (2018).",
  op=("¿Origen?", ["Sí: el tronco izquierdo se bifurca en DA y circunfleja", "No: la septal nace de la descendente anterior", "No: la marginal nace de la coronaria derecha o de la circunfleja",
                   "No: la septal posterior nace de la descendente posterior", "No: es un injerto, no una arteria coronaria"]),
  d=dict(rotulo="Las arterias coronarias y lo que irrigan", centro="TRONCO IZQUIERDO", centro_sub="coronaria izquierda", ans=1,
         items=[("DESCENDENTE ANTERIOR", ["Tabique y pared anterior"]), ("CIRCUNFLEJA", ["Pared lateral y posterior"]), ("CORONARIA DERECHA", ["Nodo sinusal, nodo AV, VD"]),
                ("MARGINAL DERECHA", ["Borde agudo del VD"]), ("DESCENDENTE POSTERIOR", ["Pared inferior y tabique posterior"])],
         ruta=["Seno aórtico izquierdo", "Tronco izquierdo corto", "Se divide en DA y circunfleja", "Circunfleja: pared lateral"]))

# 4 · RM-CB-004 · DECISIÓN: simpático y parasimpático en el corazón
S("decision", "RM-CB-004", "El plexo cardiaco nace de las ramas cervicales del vago y del tronco simpático",
  "Anatomía · inervación del corazón",
  ("Plexo cardiaco", ["Red nerviosa de la base del corazón y del arco aórtico.", "Recibe fibras simpáticas (aceleran) y vagales parasimpáticas (enlentecen)."]),
  ("Pregunta de teoría", ["¿De dónde proviene el plexo cardiaco?"]),
  ["Simpático: ganglios cervicales superior, medio e inferior y torácicos altos → ↑ frecuencia, contractilidad y conducción.",
   "Parasimpático: nervios vagos (ramos cardiacos cervicales y torácicos) → ↓ frecuencia y conducción AV.",
   "El dolor isquémico viaja por aferentes simpáticas T1-T4: por eso se irradia al brazo izquierdo y al cuello."],
  MOORE + "; Guyton y Hall Tratado de Fisiología Médica 14.ª ed.",
  op=("¿Origen?", ["Sí: vago cervical y tronco simpático", "No: el plexo es autonómico, no solo vagal ni solo simpático", "No: son raíces del plexo cervical, no cardiacas",
                   "No: T12 inerva la pared abdominal", "No: C3-C5 forman el nervio frénico"],
      {0: "Vago cervical y tronco simpático", 1: "Vago y ganglios simpáticos", 2: "Ramas cervicales anteriores y C5", 3: "Ramas anteriores del vago y T12", 4: "Ganglios simpáticos y ramas posteriores C3-C5"}),
  d=dict(rotulo="Los dos sistemas que forman el plexo", eje_y="Sistema", ancho_filas=200,
         cols=["Origen de las fibras", "Efecto en el corazón"],
         rows=[("Simpático", "Ganglios cervicales y T1-T4"), ("Parasimpático", "Nervios vagos")],
         cells=[[("Ganglios cervicales y torácicos", ["Nervios cardiacos"]), ("Acelera y contrae más", ["↑ FC, ↑ contractilidad", "Receptores beta-1"])],
                [("Ramos cardiacos del vago", ["Cervicales y torácicos"]), ("Enlentece", ["↓ FC y conducción AV", "Receptores M2"])]],
         caso=(0, 0), nota="El plexo cardiaco mezcla ambas: la pregunta pide el origen conjunto (vago + tronco simpático)."))

# 5 · RM-CB-005 · MATRIZ: circulación funcional y nutricia del pulmón
S("matriz", "RM-CB-005", "Las venas bronquiales drenan solo parte de la sangre aportada a los pulmones",
  "Anatomía · circulación pulmonar",
  ("Doble circulación del pulmón", ["Funcional: arteria pulmonar → capilar alveolar → venas pulmonares.", "Nutricia: arterias bronquiales (de la aorta) → bronquios y parénquima."]),
  ("Pregunta de teoría", ["¿Qué afirmación sobre la vascularización pulmonar es correcta?"]),
  ["Venas pulmonares: sangre oxigenada hacia la aurícula izquierda. Arterias pulmonares: sangre pobre en oxígeno hacia el pulmón.",
   "Las venas bronquiales drenan solo parte de la sangre nutricia; el resto vuelve por las venas pulmonares (cortocircuito anatómico fisiológico).",
   "Vena bronquial derecha → ácigos; izquierda → hemiácigos o intercostal superior izquierda."],
  MOORE + "; West Fisiología respiratoria 11.ª ed.",
  op=("¿Correcta?", ["No: las venas pulmonares llevan sangre oxigenada", "No: las arterias pulmonares llevan sangre desoxigenada", "No: la derecha drena en la ácigos",
                     "Sí: solo una parte; el resto va a las venas pulmonares", "No: la izquierda drena en la hemiácigos"],
      {0: "V. pulmonares: sangre pobre en O₂", 1: "A. pulmonares: sangre oxigenada", 2: "V. bronquial der. a hemiácigos", 3: "V. bronquiales: drenaje parcial", 4: "V. bronquial izq. a ácigos"}),
  d=dict(rotulo="Dos circulaciones, cuatro vasos", eje_x="Tipo de vaso", eje_y="Circulación",
         cols=["Arterias", "Venas"], rows=["Funcional (intercambio)", "Nutricia (bronquial)"], caso=(1, 1),
         cells=[[("A. pulmonares", ["Sangre desoxigenada", "Del ventrículo derecho"]), ("V. pulmonares", ["Sangre oxigenada", "A la aurícula izquierda"])],
                [("A. bronquiales", ["Nacen de la aorta", "Nutren bronquios"]), ("V. bronquiales", ["Drenan solo en parte", "ácigos / hemiácigos"])]]))

# 6 · RM-CB-006 · EMBUDO: biarticular
S("embudo", "RM-CB-006", "El gastrocnemio flexiona la planta del pie y, débilmente, la rodilla",
  "Anatomía · músculos de la pierna",
  ("Gastrocnemio", ["Es biarticular: nace en los cóndilos femorales y se inserta en el calcáneo por el tendón de Aquiles.", "Por eso actúa sobre el tobillo y sobre la rodilla."]),
  ("Pregunta de teoría", ["¿Qué músculo flexiona la planta y la rodilla?"]),
  ["Sóleo: solo cruza el tobillo, es flexor plantar y postural. Isquiotibiales: flexionan la rodilla pero no actúan sobre el tobillo.",
   "Prueba de Thompson: al comprimir la pantorrilla no hay flexión plantar si el tendón de Aquiles está roto.",
   "Reflejo aquíleo: raíz S1 (nervio tibial)."],
  MOORE + "; Netter Atlas de Anatomía Humana 8.ª ed.",
  op=("¿Cuál?", ["Sí: cruza rodilla y tobillo", "No: cruza solo el tobillo", "No: flexiona la rodilla pero no el tobillo", "No: flexiona la rodilla y no es plantar", "No: aduce el muslo"]),
  d=dict(rotulo="Descarta por lo que cruza cada músculo", inicio="Músculos de la pierna y del muslo",
         candidatos=["Sóleo", "Semitendinoso", "Semimembranoso", "Aductor mayor", "Gastrocnemio"],
         pasos=[("¿Actúa sobre el tobillo (flexión plantar)?", ["Semitendinoso", "Semimembranoso", "Aductor mayor"]),
                ("¿Cruza también la rodilla?", ["Sóleo"])],
         final=("GASTROCNEMIO", ["Biarticular", "Flexión plantar + flexión de la rodilla"]),
         nota="El sóleo solo cruza el tobillo; los isquiotibiales solo la cadera y la rodilla."))

# 7 · RM-CB-007 · LECTURA con esquema propio: hilio pulmonar
S("lectura", "RM-CB-007", "La arteria pulmonar derecha pasa por detrás de la aorta ascendente",
  "Anatomía · mediastino y hilio",
  ("Arteria pulmonar derecha", ["Más larga que la izquierda: cruza el mediastino medio.", "Pasa detrás de la aorta ascendente y de la vena cava superior y delante del bronquio principal."]),
  ("Pregunta de teoría", ["¿Cómo se ubica la arteria pulmonar derecha?"]),
  ["Hilio derecho, de adelante hacia atrás: vena pulmonar, arteria y bronquio (VAB). La arteria queda delante del bronquio.",
   "La izquierda arquea sobre el bronquio izquierdo y pasa delante de la aorta descendente.",
   "El agrandamiento de las arterias hiliares se ve en la hipertensión pulmonar y en la embolia."],
  MOORE + "; Gray Anatomía para estudiantes 5.ª ed.; Fraser y Paré Diagnosis of Diseases of the Chest 5.ª ed.",
  op=("¿Relación?", ["Sí: detrás de la aorta ascendente", "No: eso es la arteria izquierda (delante de la aorta descendente)", "No: queda delante de la vena pulmonar inferior",
                     "No: queda delante del bronquio principal", "No: cruza por detrás, no por delante"]),
  d=dict(rotulo="Ubica la arteria en el hilio", img_titulo="Hilios pulmonares (esquema)",
         img=PX("dib_hilio_pulmonar.jpg", 360, credito=PROPIO, fondo="#ffffff"), pines=[(0.36, 0.42), (0.68, 0.45)],
         pasos=[("Derecha: sale del tronco pulmonar", "Cruza el mediastino medio, detrás de la aorta.", True),
                ("Orden en el hilio derecho (VAB)", "Vena arriba y delante, arteria en el medio, bronquio atrás.", False),
                ("Izquierda: sobre el bronquio", "Arquea sobre el bronquio izquierdo.", False),
                ("Aplicación", "Agrandamiento hiliar: hipertensión pulmonar o embolia.", False)],
         img_pie="Derecha del paciente = izquierda del dibujo.",
         veredicto=("Arteria pulmonar derecha: detrás de la aorta ascendente", "Después sigue por delante del bronquio principal derecho.")))

# 8 · RM-CB-008 · BALANZA: articulaciones sinoviales vs otras
S("balanza", "RM-CB-008", "La articulación coxofemoral es de tipo sinovial",
  "Anatomía · articulaciones",
  ("Articulaciones sinoviales", ["Tienen cavidad articular, cápsula con membrana sinovial y cartílago hialino: son móviles.", "Las fibrosas y las cartilaginosas casi no se mueven."]),
  ("Pregunta de teoría", ["¿Cuál de las opciones es sinovial?"]),
  ["Sinoviales: cadera (esferoidea), rodilla, hombro, codo. Fibrosas: suturas craneales. Cartilaginosas: sínfisis púbica, discos intervertebrales, sincondrosis.",
   "«Pubocoxígea» es un músculo del suelo pélvico, no una articulación.",
   "Artrosis y artritis reumatoide afectan articulaciones sinoviales; la sínfisis púbica se afloja en el embarazo por relaxina."],
  MOORE + "; Gray Anatomía para estudiantes 5.ª ed.",
  op=("¿Sinovial?", ["Sí: cavidad, cápsula y líquido sinovial", "No: es un músculo del suelo pélvico", "No: es cartilaginosa (sínfisis)", "No: es fibrosa (sutura)", "No: es cartilaginosa (sincondrosis)"],
      {0: "Coxofemoral", 1: "Pubocoxígea", 2: "Sínfisis púbica", 3: "Sutura sagital", 4: "Sincondrosis esfenooccipital"}),
  d=dict(rotulo="¿Qué tipo de articulación es?", gana="izq", pregunta="¿Cuál se mueve libremente?",
         izq=dict(titulo="Sinoviales", peso="MÓVILES", items=["Coxofemoral (cadera)", "Rodilla y hombro", "Cavidad y líquido sinovial", "Cartílago hialino"]),
         der=dict(titulo="Fibrosas y cartilaginosas", peso="CASI FIJAS", items=["Suturas del cráneo", "Sínfisis púbica", "Discos intervertebrales", "Sincondrosis"]),
         veredicto=("Coxofemoral = sinovial", ["Es la cadera: esferoidea, con cápsula y líquido sinovial.", "Las otras opciones son fijas o ni siquiera son articulaciones."])))

# 9 · RM-CB-009 · CASCADA: del vago a las cuerdas vocales
S("cascada", "RM-CB-009", "El nervio laríngeo recurrente inerva las cuerdas vocales; el superior solo el cricotiroideo",
  "Anatomía · inervación de la laringe",
  ("Nervios de la laringe", ["Ambos son ramas del vago (X).", "El recurrente mueve casi todos los músculos; el superior tensa las cuerdas y da sensibilidad."]),
  ("Pregunta de teoría", ["¿Qué nervio inerva las cuerdas vocales?"]),
  ["Laríngeo superior: rama interna (sensitiva sobre las cuerdas) y rama externa (motor del cricotiroideo, que tensa las cuerdas).",
   "Recurrente: todos los músculos intrínsecos restantes, incluido el cricoaritenoideo posterior (único abductor). Izquierdo: rodea el arco aórtico; derecho: la subclavia.",
   "Lesión del recurrente (cirugía de tiroides, cáncer de pulmón, aneurisma): disfonía; bilateral: estridor."],
  MOORE + "; Cummings Otolaryngology 7.ª ed.; AAO-HNS, disfonía (2018).",
  op=("¿Qué nervio?", ["No: mueve la lengua", "No: es el simpático de la glándula y vasos", "Sí: motor de casi toda la laringe", "No: solo tensa las cuerdas y da sensibilidad", "No: da sensibilidad faríngea"]),
  d=dict(rotulo="Del vago a la laringe", cabeceras=("Nervio", "Qué hace"),
         pasos=[("Vago (X)", "Origen de ambos nervios laríngeos", [("Rama del neumogástrico", "", False)]),
                ("Laríngeo superior", "Tensa las cuerdas y da sensibilidad", [("Rama externa: cricotiroideo", "Voz aguda", False)]),
                ("Laríngeo recurrente", "Mueve casi toda la laringe", [("Todos los músculos intrínsecos, incluidas las cuerdas", "Este caso", True)])],
         veredicto=("Cuerdas vocales = laríngeo recurrente", "Si se lesiona: disfonía; si es bilateral, estridor.")))

# 10 · RM-CB-010 · ARBOL: compartimentos mediastínicos
S("arbol", "RM-CB-010", "En el adulto sano, la aorta descendente se localiza en el mediastino posterior",
  "Anatomía · compartimentos del mediastino",
  ("Mediastino", ["Espacio entre ambas pleuras: superior e inferior (anterior, medio, posterior).", "Cada estructura y cada tumor tiene su compartimento."]),
  ("Pregunta de teoría", ["¿Qué estructura va en el mediastino posterior?"]),
  ["Posterior: aorta descendente, esófago, conducto torácico, ácigos y hemiácigos, vagos y cadena simpática.",
   "Anterior: timo, ganglios mamarios internos, grasa. Medio: corazón, pericardio, frénicos, tráquea y bronquios principales.",
   "Tumor posterior típico: neurogénico (schwannoma). Anterior: timoma, teratoma, linfoma y bocio endotorácico."],
  MOORE + "; Netter Atlas de Anatomía Humana 8.ª ed.; Shields Thoracic Surgery 8.ª ed.",
  op=("¿Mediastino posterior?", ["Sí: está pegada a la columna", "No: el timo es anterior", "No: la mamaria interna es anterior", "No: el frénico va en el mediastino medio", "No: la tráquea está en el mediastino medio"],
      {0: "Aorta descendente", 1: "Glándula timo", 2: "Arteria mamaria interna", 3: "Nervio frénico", 4: "Tráquea"}),
  arbol=Q("¿Dónde está la estructura?", [
      L("Entre el esternón y el pericardio", "ANTERIOR", ["Timo", "Ganglios y arteria mamaria interna"]),
      L("Contiene el corazón", "MEDIO", ["Pericardio y frénicos", "Tráquea y bronquios"]),
      L("Delante de la columna (este caso)", "POSTERIOR", ["Aorta descendente", "Esófago, conducto torácico, ácigos"], path=True)], path=True))

# 11 · RM-CB-011 · FASES: reposo, esfuerzo, máximo
S("fases", "RM-CB-011", "El diafragma es el principal músculo de la inspiración",
  "Fisiología respiratoria · mecánica ventilatoria",
  ("Músculos de la inspiración", ["El diafragma genera cerca del 70 % del volumen inspiratorio en reposo.", "Los accesorios solo se reclutan si hay esfuerzo respiratorio."]),
  ("Pregunta de teoría", ["¿Cuál es el principal músculo inspiratorio?"]),
  ["Diafragma: nervio frénico (C3-C5). Al contraerse desciende y crea presión pleural más negativa.",
   "Accesorios: esternocleidomastoideo y escalenos (crisis asmática, EPOC). La espiración en reposo es pasiva.",
   "Lesión medular por encima de C3: ventilación mecánica («C3, 4, 5 mantienen vivo el diafragma»)."],
  "West Fisiología respiratoria 11.ª ed.; Guyton y Hall Tratado de Fisiología Médica 14.ª ed.",
  op=("¿Principal?", ["Sí: frénico C3-C5, 70 % del volumen", "No: accesorio de la espiración forzada", "No: es espiratorio", "No: es un músculo de la espalda y el hombro", "No: accesorio solo con esfuerzo"],
      {0: "Diafragma", 1: "Serrato posterior superior", 2: "Transverso del tórax", 3: "Trapecio", 4: "ECM (cuello)"}),
  d=dict(rotulo="Quién trabaja según el esfuerzo", ans=0,
         fases=[("Respiración tranquila", "En reposo", "DIAFRAGMA", ["Intercostales externos ayudan", "Espiración pasiva"]),
                ("Ejercicio", "Mayor demanda", "+ INTERCOSTALES", ["Más ascenso de costillas", "Espiración activa leve"]),
                ("Esfuerzo máximo o asma", "Falla respiratoria", "+ ACCESORIOS", ["Esternocleidomastoideo, escalenos", "Se ve el tiraje"])]))

# 12 · RM-CB-012 · TRANSMISIÓN (cadena): irrigación del nodo sinusal
S("transmision", "RM-CB-012", "El nodo sinusal se irriga con mayor frecuencia por una rama de la coronaria derecha",
  "Anatomía · sistema de conducción",
  ("Nodo sinusal", ["Marcapasos del corazón, entre la vena cava superior y la aurícula derecha.", "Su arteria nace de la coronaria derecha en 55-65 % de las personas."]),
  ("Pregunta de teoría", ["¿De qué arteria viene su irrigación más frecuente?"]),
  ["Arteria del nodo sinusal: coronaria derecha (55-65 %) o circunfleja (35-45 %).",
   "Arteria del nodo AV: coronaria derecha dominante, a nivel de la crux cordis.",
   "Infarto inferior (coronaria derecha): bradicardia sinusal y bloqueo AV; responden a atropina o marcapasos."],
  "Braunwald Tratado de Cardiología 12.ª ed.; " + MOORE,
  op=("¿Arteria?", ["No: irriga tabique y pared anterior", "No: irriga el borde del ventrículo derecho", "Sí: nodo sinusal en 55-65 %", "No: irriga pared lateral del ventrículo izquierdo", "No: es una rama muscular ventricular"],
      {0: "Interventricular anterior", 1: "Marginal derecha", 2: "Coronaria derecha", 3: "Marginal izquierda", 4: "Ventricular anterior"}),
  d=dict(rotulo="De la arteria a la consecuencia clínica", tag="ESTE CASO",
         eslabones=[("Coronaria derecha", "Arteria", "Origen en el seno aórtico derecho", True), ("Arteria del nodo sinusal", "Rama", "55-65 % de las personas", True),
                    ("Nodo sinusal", "Marcapasos", "Fija la frecuencia cardiaca", False), ("Nodo AV (crux cordis)", "Segundo nodo", "También de la coronaria derecha", False),
                    ("Infarto inferior", "Consecuencia", "Bradicardia y bloqueo AV", False)],
         veredicto=("Coronaria derecha irriga el nodo sinusal", "Su oclusión causa bradicardia sinusal y bloqueos auriculoventriculares.")))

# 13 · RM-CB-013 · CRONOLOGÍA vascular (embrio-mesentérica): irrigación del apéndice
S("piramide", "RM-CB-013", "La arteria apendicular es rama de la mesentérica superior, a través de la ileocólica",
  "Anatomía · irrigación del intestino",
  ("Irrigación del apéndice", ["Del intestino medio: arteria mesentérica superior.", "La arteria apendicular es terminal: no tiene colaterales."]),
  ("Pregunta de teoría", ["¿De qué arteria nace la rama del apéndice?"]),
  ["Mesentérica superior → ileocólica → cecales y apendicular. Es una arteria terminal: la trombosis causa gangrena y perforación precoz.",
   "Mesentérica inferior (colon izquierdo, recto): cólica izquierda, sigmoideas y rectal superior.",
   "Punto de Griffiths (ángulo esplénico): zona vulnerable a la colitis isquémica."],
  MOORE + "; Sabiston Tratado de Cirugía 21.ª ed.",
  op=("¿Arteria madre?", ["No: irriga el colon transverso", "No: es de la mesentérica inferior", "No: es de la mesentérica inferior (recto)", "No: es de la mesentérica inferior (sigmoides)", "Sí: la ileocólica nace de ella"]),
  d=dict(rotulo="De la aorta al apéndice", caso=3, pie="▲ origen · ▼ apéndice",
         niveles=[("Aorta", "Tronco mayor", "Da el tronco celíaco, la mesentérica superior y la inferior"),
                  ("Mesentérica superior", "Intestino medio", "Yeyuno, íleon, ciego, colon ascendente y transverso proximal"),
                  ("Arteria ileocólica", "Rama derecha", "Ileal, cólica y cecales"),
                  ("Arteria apendicular", "Rama terminal", "Por el mesoapéndice: sin colaterales")],
         veredicto=("Mesentérica superior → ileocólica → apendicular", "Por ser terminal, su trombosis produce gangrena apendicular.")))
