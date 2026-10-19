# -*- coding: utf-8 -*-
"""Residentado Médico · lote 1 (preguntas 1-100 del libro, parte A: anatomía, anestesiología y fisiología).
Cada pregunta: dict(a=archivo del banco, cat=categoría o None, tema, año, ext, e=enunciado, o=[5 opciones], k=clave,
c=comentario docente ampliado, f=fuentes, nota=observación de revisión)."""
L = []
def Q(**k): L.append(k)

Q(a="ciencias_basicas", cat="Anatomía", tema="Cartílagos impares de la laringe", año=2014, ext=False,
  e="Los cartílagos impares de la laringe son epiglotis, tiroides y...",
  o=["Cricoides.", "Aritenoides.", "Corniculado.", "Cuneiforme.", "Triticio."], k="A",
  c="El esqueleto de la laringe tiene nueve cartílagos: tres impares (epiglotis, tiroides y cricoides) y tres pares (aritenoides, corniculados y cuneiformes). El cricoides es el único que forma un anillo completo, por eso sostiene la vía aérea y es la referencia de la cricotiroidotomía y del sitio de la presión cricoidea. El tiroides, el más grande, forma la «nuez» y protege las cuerdas vocales; la epiglotis, de cartílago elástico, cierra el vestíbulo laríngeo al deglutir. Los aritenoides se mueven sobre el cricoides y tensan o relajan las cuerdas: su luxación puede aparecer tras una intubación traumática. Los corniculados y cuneiformes son pares y pequeños, y el triticio, inconstante, está dentro del ligamento tirohioideo lateral. Regla útil: lo que es par es pequeño y móvil; lo que es impar es grande y estructural.",
  f="Gray Anatomía para estudiantes 5.ª ed.; Netter Atlas de Anatomía Humana 8.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Canal de la vena cefálica", año=2014, ext=False,
  e="¿Cuál es el canal por donde pasa la vena cefálica y que se debe recordar cuando se le realiza una flebotomía?",
  o=["Guyon.", "Torsión.", "Deltopectoral.", "Bicipital.", "Radial."], k="C",
  c="La vena cefálica, la vena superficial lateral del miembro superior, asciende por el borde lateral del bíceps y termina perforando la fascia clavipectoral dentro del surco (canal) deltopectoral, entre el deltoides y el pectoral mayor, para desembocar en la vena axilar. Por eso en la disección venosa o el acceso quirúrgico al hombro se busca en ese surco. El canal de Guyon es un túnel de la muñeca por donde pasan el nervio cubital y la arteria cubital; el canal bicipital (surco intertubercular) aloja el tendón de la cabeza larga del bíceps; el canal radial (surco del nervio radial) está en la cara posterior del húmero. Perla: la cefálica se prefiere para flebotomía en la fosa antecubital, pero el nervio cutáneo antebraquial lateral corre cerca y se puede lesionar.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Gray Anatomía para estudiantes 5.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Arteria circunfleja del corazón", año=2014, ext=False,
  e="La arteria circunfleja en el corazón es rama de la:",
  o=["Coronaria izquierda.", "Septal anterior.", "Marginal.", "Septal posterior.", "Mamaria interna."], k="A",
  c="El tronco de la arteria coronaria izquierda nace del seno aórtico izquierdo, recorre un trayecto corto detrás del tronco pulmonar y se divide en dos ramas: la arteria interventricular anterior (descendente anterior), que irriga el tabique anterior y la cara anterior del ventrículo izquierdo, y la arteria circunfleja, que rodea el surco auriculoventricular izquierdo e irriga la pared lateral y posterior del ventrículo izquierdo; en el 40 % da la arteria del nodo sinusal. Por eso su oclusión produce infartos laterales (DI, aVL, V5-V6). La coronaria derecha da la marginal derecha y la interventricular posterior en el 80 % de las personas (dominancia derecha). La arteria mamaria interna no es coronaria: se usa como injerto para la descendente anterior en la cirugía de revascularización.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Braunwald Tratado de Cardiología 12.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Origen del plexo cardiaco", año=2015, ext=False,
  e="El plexo cardiaco tiene su origen en:",
  o=["Ramas cervicales del vago y tronco simpático.", "Nervio vago y ganglios simpáticos.",
     "Ramas cervicales anteriores y ramo anterior del nervio C5.", "Ramas anteriores del vago y del nervio T12.",
     "Ganglios simpáticos y ramas posteriores de nervios C3-C5."], k="A",
  c="El plexo cardiaco, situado sobre la base del corazón y el cayado aórtico, se forma por fibras simpáticas de los ganglios cervicales superior, medio e inferior (y de los cuatro primeros ganglios torácicos) y por fibras parasimpáticas de los nervios vagos, mediante sus ramos cardiacos cervicales y torácicos. Las fibras simpáticas aumentan la frecuencia (cronotropismo), la contractilidad y la conducción; las vagales (parasimpáticas) enlentecen el nodo sinusal y el nodo auriculoventricular. Las demás opciones mezclan raíces del plexo cervical o torácicas bajas que no participan. Dato clínico: el dolor cardiaco isquémico viaja por las fibras simpáticas aferentes hacia los segmentos T1-T4, y por eso se refiere al brazo izquierdo y al cuello.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Guyton y Hall Tratado de Fisiología Médica 14.ª ed.",
  nota="Se corrigió la opción C (OCR): «nervio C5».")

Q(a="ciencias_basicas", cat="Anatomía", tema="Circulación pulmonar y bronquial", año=2015, ext=False,
  e="En relación a la vascularización pulmonar marque la alternativa que corresponde:",
  o=["Las venas pulmonares transportan sangre pobre en oxígeno.", "Las arterias pulmonares transportan sangre altamente oxigenada.",
     "La vena bronquial derecha drena en la vena hemiácigos.", "Las venas bronquiales drenan parcialmente la sangre aportada a los pulmones.",
     "La vena bronquial izquierda drena en la vena ácigos."], k="D",
  c="Los pulmones tienen dos circulaciones. La circulación funcional lleva sangre desoxigenada desde el ventrículo derecho por las arterias pulmonares hasta los capilares alveolares, y regresa oxigenada por las cuatro venas pulmonares a la aurícula izquierda (por eso A y B están invertidas). La circulación nutricia está a cargo de las arterias bronquiales (ramas de la aorta torácica) que irrigan bronquios y parénquima; solo una parte de esa sangre vuelve por las venas bronquiales, y el resto drena a las venas pulmonares, lo que explica la mezcla venosa fisiológica del cortocircuito anatómico (opción D). Drenaje: la vena bronquial derecha va a la vena ácigos y la izquierda a la hemiácigos o intercostal superior izquierda (C y E están intercambiadas).",
  f="Moore Anatomía con orientación clínica 8.ª ed.; West Fisiología respiratoria 11.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Gastrocnemio: flexión plantar y de la rodilla", año=2016, ext=False,
  e="¿Cuál es el músculo que permite la flexión plantar del pie y flexión de la rodilla?",
  o=["Gastrocnemio.", "Sóleo.", "Semitendinoso.", "Semimembranoso.", "Aductor mayor."], k="A",
  c="El gastrocnemio (gemelos) es biarticular: cruza la rodilla, donde se origina en los cóndilos femorales, y el tobillo, donde se inserta en el calcáneo por el tendón de Aquiles junto con el sóleo. Por eso flexiona la planta del pie y ayuda débilmente a flexionar la rodilla. El sóleo solo cruza el tobillo: es flexor plantar y predominantemente postural. Semitendinoso y semimembranoso (isquiotibiales) flexionan la rodilla y extienden la cadera, pero no actúan sobre el tobillo. El aductor mayor aproxima el muslo. Aplicación clínica: la rotura del tendón de Aquiles se detecta con la prueba de Thompson (al comprimir la pantorrilla no hay flexión plantar), y el reflejo aquíleo explora la raíz S1 (nervio tibial).",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Netter Atlas de Anatomía Humana 8.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Relaciones de la arteria pulmonar derecha", año=2016, ext=False,
  e="¿Cuál de los siguientes enunciados caracteriza la ubicación de la arteria pulmonar derecha?",
  o=["Posterior a la aorta ascendente.", "Anterior a la aorta descendente.", "Posterior a la vena pulmonar inferior.",
     "Posterior al bronquio principal derecho.", "Anterior a la aorta ascendente."], k="A",
  c="El tronco pulmonar se divide por debajo del arco aórtico. La arteria pulmonar derecha, más larga que la izquierda, cruza el mediastino medio pasando por detrás de la aorta ascendente y de la vena cava superior, y por delante del bronquio principal derecho, para entrar en el hilio pulmonar derecho. La arteria pulmonar izquierda, en cambio, pasa por encima del bronquio principal izquierdo y por delante de la aorta descendente. En el hilio derecho la relación de adelante hacia atrás es vena pulmonar, arteria y bronquio (VAB), de modo que la arteria queda delante del bronquio, no detrás como dice la opción D. Útil en radiología: el aumento de calibre de las arterias pulmonares se evalúa en el hilio.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Gray Anatomía para estudiantes 5.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Articulaciones sinoviales", año=2017, ext=False,
  e="¿Qué articulación es de tipo sinovial?",
  o=["Coxofemoral.", "Pubocoxígea.", "Sínfisis púbica.", "Sutura sagital.", "Sincondrosis esfenooccipital."], k="A",
  c="Las articulaciones sinoviales son las verdaderamente móviles: tienen cavidad articular, cápsula con membrana sinovial que produce líquido sinovial y cartílago hialino en las superficies; ejemplos son la coxofemoral (esferoidea, la «cadera»), la rodilla y el hombro. Las articulaciones fibrosas (suturas del cráneo, sindesmosis) y las cartilaginosas (sínfisis púbica, discos intervertebrales con fibrocartílago; sincondrosis con cartílago hialino) permiten poco o ningún movimiento. «Pubocoxígea» es un músculo del suelo pélvico, no una articulación. Perla: la artrosis y la artritis reumatoide afectan articulaciones sinoviales; la espondilitis anquilosante afecta articulaciones cartilaginosas y sinoviales sacroilíacas.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Gray Anatomía para estudiantes 5.ª ed.",
  nota="Pregunta original con 3 respuestas posibles (acromioclavicular y esternoclavicular también son sinoviales); se reemplazaron las opciones C, D y E para dejar una sola correcta.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Inervación motora de las cuerdas vocales", año=2018, ext=False,
  e="Las cuerdas vocales están inervadas por el:",
  o=["Hipogloso.", "Simpático cervical.", "Laríngeo recurrente.", "Laríngeo superior.", "Glosofaríngeo."], k="C",
  c="La laringe recibe dos ramas del vago (X): el nervio laríngeo superior, cuya rama interna da sensibilidad por encima de las cuerdas y cuya rama externa mueve el músculo cricotiroideo (tensor de las cuerdas), y el nervio laríngeo recurrente (inferior), que inerva todos los demás músculos intrínsecos, incluidos los abductores (cricoaritenoideo posterior, el único que abre la glotis) y aductores, y da sensibilidad infraglótica. Por eso una lesión del recurrente (cirugía tiroidea, cáncer de pulmón o esófago, aneurisma aórtico) produce disfonía o parálisis de la cuerda; si es bilateral, estridor. El recurrente izquierdo rodea el arco aórtico y el derecho la arteria subclavia. El hipogloso mueve la lengua y el glosofaríngeo da sensibilidad faríngea.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Cummings Otolaryngology 7.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Contenido del mediastino posterior", año=2018, ext=False,
  e="En un adulto sano, ¿qué estructura se localiza habitualmente en el mediastino posterior?",
  o=["Aorta descendente.", "Glándula timo.", "Arteria mamaria interna.", "Nervio frénico.", "Tráquea."], k="A",
  c="El mediastino se divide en superior e inferior, y el inferior en anterior, medio y posterior. El mediastino posterior queda entre el pericardio y la columna e incluye la aorta descendente, el esófago, el conducto torácico, las venas ácigos y hemiácigos, los nervios vagos y esplácnicos y los ganglios simpáticos torácicos. El timo y la arteria mamaria interna con sus ganglios están en el mediastino anterior; el corazón con el pericardio, los nervios frénicos y la bifurcación traqueal pertenecen al mediastino medio. Por eso los tumores neurogénicos del adulto (schwannoma, neurofibroma) aparecen sobre todo en el mediastino posterior, mientras que timoma, teratoma, linfoma y bocio endotorácico son anteriores.",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Netter Atlas de Anatomía Humana 8.ª ed.")

Q(a="ciencias_basicas", cat="Fisiología", tema="Músculo principal de la inspiración", año=2019, ext=False,
  e="¿Cuál es el músculo principal de la inspiración?",
  o=["Diafragma.", "Serrato posterior superior.", "Transverso del tórax.", "Trapecio.", "Esternocleidomastoideo."], k="A",
  c="El diafragma, inervado por el nervio frénico (raíces C3-C5), genera alrededor del 70-75 % del volumen inspiratorio en reposo: al contraerse desciende, aumenta el diámetro vertical del tórax y crea una presión intrapleural más negativa que llena los pulmones. Los intercostales externos elevan las costillas (movimiento «en asa de cubo») y los músculos accesorios (esternocleidomastoideo, escalenos, pectorales) solo se reclutan en esfuerzo respiratorio, como en una crisis de asma o EPOC; el transverso del tórax es espiratorio. La espiración en reposo es pasiva por retracción elástica. Perla clínica: una lesión medular por encima de C3 requiere ventilación mecánica («C3, 4 y 5 mantienen vivo el diafragma»).",
  f="West Fisiología respiratoria 11.ª ed.; Guyton y Hall Tratado de Fisiología Médica 14.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Irrigación del nodo sinusal", año=2019, ext=False,
  e="El nodo sinusal es irrigado con mayor frecuencia por una rama de la arteria...",
  o=["Interventricular anterior.", "Marginal derecha.", "Coronaria derecha.", "Marginal izquierda.", "Ventricular anterior."], k="C",
  c="El nodo sinusal, marcapasos del corazón, se ubica en la unión de la vena cava superior con la aurícula derecha y recibe su sangre de la arteria del nodo sinoauricular, que nace de la coronaria derecha en un 55-65 % de los casos y de la circunfleja (rama de la coronaria izquierda) en el resto. El nodo auriculoventricular se irriga en la mayoría por la rama del nodo AV de la coronaria derecha dominante. Por eso los infartos inferiores por oclusión de la coronaria derecha se acompañan de bradicardia sinusal y de bloqueo auriculoventricular, y suelen responder a atropina o requerir marcapasos temporal. Las demás arterias de las opciones irrigan miocardio ventricular, no el sistema de conducción.",
  f="Braunwald Tratado de Cardiología 12.ª ed.; Moore Anatomía con orientación clínica 8.ª ed.")

Q(a="ciencias_basicas", cat="Anatomía", tema="Irrigación del apéndice cecal", año=2019, ext=False,
  e="La irrigación del apéndice cecal se da a través de una rama de la arteria...",
  o=["Cólica media accesoria.", "Cólica izquierda.", "Rectal superior.", "Sigmoidea superior.", "Mesentérica superior."], k="E",
  c="El apéndice y el ciego derivan del intestino medio, irrigado por la arteria mesentérica superior. De ella nace la arteria ileocólica, que da la ileal, las cecales anterior y posterior, la cólica y la arteria apendicular, que corre por el mesoapéndice y es terminal (no tiene circulación colateral): su trombosis en la apendicitis explica la gangrena y la perforación temprana. La arteria cólica izquierda, la sigmoidea y la rectal superior provienen de la mesentérica inferior (intestino posterior). Recuerda el límite entre ambos territorios: el ángulo esplénico, donde puede ocurrir isquemia de la «zona crítica de Griffiths» (colitis isquémica).",
  f="Moore Anatomía con orientación clínica 8.ª ed.; Sabiston Tratado de Cirugía 21.ª ed.")
