# -*- coding: utf-8 -*-
"""Casos 1 a 5 de la Misión SERUMS. Casos originales y ficticios. No contienen dosis: toda dosis exige cita documental verificada."""
from lib import O, Mo, guardar
GPC, DEN, TB, FRIO = "ins-gpc03-2025", "nts211-dengue", "nts221-tb", "rm074-2026-cadena-frio"

# ---------------------------------------------------------------- 1. Niño con dificultad respiratoria
guardar({"id": "s01", "numero": 1, "titulo": "Un niño que respira con dificultad", "tema": "Pediatría · Infecciones respiratorias",
 "resumen": "Lactante con tos, fiebre y tiraje en una posta de altura, con pocos balones de oxígeno y un hospital a horas de distancia.",
 "dificultad": "intermedio", "duracion_min": 12,
 "paciente": {"titulo": "Niño de 14 meses", "motivo": "La madre lo trae porque «respira rápido y se hunde el pecho»."},
 "vitales": {"fc": 168, "fr": 58, "sat": 88, "temp": 38.6}, "gravedad": 2,
 "historia": [{"id": "h1", "rotulo": "Evolución", "texto": "Tos y fiebre desde hace tres días; hoy rechaza el pecho y está decaído."},
  {"id": "h2", "rotulo": "Contexto", "texto": "Vive en una comunidad a 3 400 m s. n. m.; cocina con leña dentro de la vivienda."}],
 "examen": [{"id": "e1", "rotulo": "Respiración", "texto": "Tiraje subcostal marcado y aleteo nasal."}, {"id": "e2", "rotulo": "Estado general", "texto": "Somnoliento, se deja explorar con poca reacción."}],
 "pruebas": [{"id": "p1", "nombre": "Pulsioximetría", "insumo": None, "min": 2, "resultado": "Saturación 88 % respirando aire ambiente."}],
 "eventos": [{"cuando": {"t": 25}, "texto": "Pasan 25 minutos y el niño se agota más: la frecuencia respiratoria sube.", "g": 1}],
 "momentos": [
  Mo("m1", "clinico", "Valoración inicial", "El niño tiene tiraje y está decaído. ¿Qué haces primero?", [
   O("a", "Buscar signos de peligro, medir frecuencia respiratoria y saturación", "optima", "Reconocer gravedad y medir saturación orienta el nivel de soporte y la referencia.", min=3),
   O("b", "Indicar una radiografía de tórax antes de cualquier otra medida", "incorrecta", "La posta no tiene radiografía y retrasaría la estabilización.", "demora", min=20, g=1),
   O("c", "Recetar tratamiento oral y citar en una semana", "peligrosa", "Un niño con signos de dificultad respiratoria no debe irse sin soporte ni referencia.", "seguridad_paciente", g=2),
   O("d", "Tranquilizar a la madre y observar en casa", "incorrecta", "Subestima la gravedad y pierde tiempo crítico.", "omision", min=10, g=1)]),
  Mo("m2", "recursos", "Oxígeno", "La saturación es 88 %. Quedan pocos balones de oxígeno. ¿Cómo lo usas?", [
   O("a", "Dar oxígeno guiado por saturación y vigilar cuánto queda para el traslado", "optima", "Se oxigena con objetivo y se cuida el recurso para el traslado.", cons={"oxigeno": 1}, req={"items": {"oxigeno": 1}}, min=5, g=-1),
   O("b", "Esperar unos minutos a ver si mejora sin oxígeno", "peligrosa", "La hipoxemia persistente no se espera.", "seguridad_paciente", g=2, min=15),
   O("c", "Dejar oxígeno al máximo continuo sin vigilar el stock", "aceptable", "Oxigena, pero agota el recurso que necesitarás durante el traslado.", "recursos", cons={"oxigeno": 2}, req={"items": {"oxigeno": 2}}, min=5, g=-1),
   O("d", "Nebulizar sin oxígeno suplementario", "incorrecta", "No corrige la hipoxemia.", "comision", min=15, g=1)]),
  Mo("m3", "referencia", "Referencia", "El niño necesita mayor capacidad resolutiva. ¿Cómo organizas el traslado?", [
   O("a", "Referencia de emergencia acompañada, con oxígeno y hoja de referencia", "optima", "Traslado acompañado, con soporte y documento, es lo que exige una referencia segura.", ref=[(DEN, 9)], cons={"oxigeno": 1}, req={"items": {"oxigeno": 1}}, referencia="emergencia", min=15, g=-1),
   O("b", "Pedir a la familia que lo lleve por su cuenta al día siguiente", "peligrosa", "Se pierde la oportunidad y no hay soporte durante el viaje.", "seguridad_paciente", g=2, referencia="rechazada"),
   O("c", "Solicitar ambulancia pero enviarlo sin acompañante ni oxígeno", "incorrecta", "Sin soporte, la hipoxemia puede empeorar en el camino.", "seguridad_paciente", g=1, referencia="emergencia", min=15),
   O("d", "Hospitalizarlo en la posta", "incorrecta", "Una posta I-2 no tiene la capacidad para internar a un niño con hipoxemia.", "normativo", min=30, g=1)]),
  Mo("m4", "referencia", "Comunicación con el hospital", "Antes de que salga la ambulancia, ¿qué haces?", [
   O("a", "Avisar al hospital receptor y entregar un resumen clínico", "optima", "La comunicación previa prepara la recepción y evita demoras.", min=5),
   O("b", "No avisar: ya lo evaluarán al llegar", "incorrecta", "Sin aviso el niño puede esperar en la puerta de emergencia.", "comunicacion", g=1),
   O("c", "Avisar solo a la familia", "incorrecta", "La coordinación entre establecimientos es parte de la referencia.", "comunicacion"),
   O("d", "Llamar al hospital después de media hora", "aceptable", "Avisar tarde es mejor que no hacerlo, pero reduce la preparación.", "demora", min=30)]),
  Mo("m5", "comunitario", "Después del traslado", "El niño ya fue referido. ¿Qué haces con la familia y la comunidad?", [
   O("a", "Educar sobre signos de alarma, coordinar seguimiento con el agente comunitario y registrar", "optima", "El cierre comunitario previene recaídas y asegura la contrarreferencia.", min=10),
   O("b", "No hacer nada más: el caso ya salió de la posta", "incorrecta", "Se pierde el seguimiento y la prevención del entorno.", "omision"),
   O("c", "Solo anotar el nombre en el cuaderno", "aceptable", "Registra, pero no educa ni organiza el seguimiento.", "omision", min=3),
   O("d", "Culpar a la madre por llegar tarde", "incorrecta", "No ayuda y debilita la confianza de la comunidad.", "comunicacion")])],
 "desenlaces": {"favorable": "El niño llegó con soporte y se recuperó en el hospital.", "reservado": "El niño llegó tarde y quedó en observación prolongada.", "desfavorable": "El niño empeoró durante la demora y el traslado."},
 "evidencia": [DEN], "pendientes": ["Norma/guía peruana de infecciones respiratorias agudas e IRA/neumonía infantil: no verificada ni indexada; las decisiones clínicas del caso quedan pendientes de validación científica."]})

# ---------------------------------------------------------------- 2. Gestante con hipertensión severa
guardar({"id": "s02", "numero": 2, "titulo": "Gestante con presión muy alta", "tema": "Salud materna · Trastorno hipertensivo del embarazo",
 "resumen": "Gestante de 34 semanas con cefalea y presión muy elevada en una posta sin médico especialista; hay que estabilizar y referir.",
 "dificultad": "avanzado", "duracion_min": 12,
 "paciente": {"titulo": "Gestante de 28 años", "motivo": "Acude con dolor de cabeza intenso y visión borrosa."},
 "vitales": {"fc": 98, "pas": 168, "pad": 114, "temp": 36.8}, "gravedad": 2,
 "historia": [{"id": "h1", "rotulo": "Gestación", "texto": "34 semanas. Sus controles prenatales fueron irregulares."}, {"id": "h2", "rotulo": "Síntomas", "texto": "Cefalea intensa desde la mañana y manchas en la visión."}],
 "examen": [{"id": "e1", "rotulo": "Presión arterial", "texto": "168/114 mm Hg en dos tomas separadas."}, {"id": "e2", "rotulo": "Obstétrico", "texto": "Feto vivo; sin sangrado."}],
 "pruebas": [{"id": "p1", "nombre": "Proteinuria en tira reactiva", "insumo": None, "min": 5, "resultado": "Proteinuria positiva."}],
 "eventos": [{"cuando": {"t": 30}, "texto": "La paciente presenta un aumento de la cefalea y náuseas.", "g": 1}],
 "momentos": [
  Mo("m1", "clinico", "Clasificación", "Con estos datos, ¿qué conclusión tomas?", [
   O("a", "Sospechar preeclampsia con criterios de severidad y activar clave azul", "optima", "Presión muy elevada con síntomas obliga a activar la clave azul y referir.", ref=[(GPC, 11), (GPC, 14)], min=3),
   O("b", "Tomar la presión de nuevo la próxima semana", "peligrosa", "Hay riesgo de convulsión y daño materno-fetal inmediato.", "seguridad_paciente", g=2, ref=[(GPC, 11)]),
   O("c", "Tratar solo el dolor de cabeza", "incorrecta", "La cefalea es un signo de severidad, no un problema aislado.", "omision", g=1),
   O("d", "Pedir primero una ecografía en el centro de salud más cercano", "incorrecta", "Retrasa la estabilización y la referencia.", "demora", min=40, g=1)]),
  Mo("m2", "seguridad", "Estabilización", "Mientras organizas el traslado, ¿qué haces?", [
   O("a", "Vía aérea permeable, vía endovenosa, sonda y sulfato de magnesio según la clave azul del documento vigente", "optima", "Es el manejo inicial que describe la guía para el primer nivel.", ref=[(GPC, 11), (GPC, 14)], cons={"sulfato_mg": 5, "suero_salino": 1, "venoclisis": 1, "foley": 1}, req={"items": {"sulfato_mg": 5, "suero_salino": 1, "venoclisis": 1, "foley": 1}}, min=15, g=-1),
   O("b", "Esperar a que llegue la ambulancia sin iniciar nada", "peligrosa", "El manejo inicial no se retrasa hasta el hospital.", "omision", g=2, min=30, ref=[(GPC, 76)]),
   O("c", "Iniciar solo el antihipertensivo sin prevenir convulsiones", "incorrecta", "Falta el componente de prevención de convulsiones descrito en la clave azul.", "omision", cons={"antihipertensivo": 1}, g=1, ref=[(GPC, 11)]),
   O("d", "Dar el sulfato de magnesio sin vía venosa asegurada ni vigilancia", "incorrecta", "Requiere acceso y vigilancia durante el traslado.", "seguridad_paciente", g=1)]),
  Mo("m3", "referencia", "Referencia de emergencia", "¿Cómo derivas a la paciente?", [
   O("a", "Referencia de emergencia acompañada por personal y con hoja de referencia", "optima", "La guía pide referir a un nivel de mayor complejidad con acompañamiento.", ref=[(GPC, 11)], referencia="emergencia", min=15, g=-1),
   O("b", "Indicarle que acuda al hospital cuando pueda", "peligrosa", "No cumple una referencia de emergencia.", "seguridad_paciente", g=2, referencia="rechazada"),
   O("c", "Referir sin acompañante", "incorrecta", "Aumenta el riesgo durante el traslado.", "seguridad_paciente", g=1, referencia="emergencia"),
   O("d", "Esperar al día siguiente para completar exámenes", "incorrecta", "Los exámenes no deben retrasar la referencia.", "demora", g=1, min=60)]),
  Mo("m4", "referencia", "Comunicación", "Antes de salir, ¿qué coordinas con el hospital?", [
   O("a", "Avisar el diagnóstico de sospecha, el manejo ya dado y la hora estimada de llegada", "optima", "Una referencia útil comunica lo realizado.", min=5),
   O("b", "No coordinar para no perder tiempo", "incorrecta", "Sin aviso, el hospital no se prepara.", "comunicacion"),
   O("c", "Coordinar solo con la familia", "incorrecta", "No sustituye la coordinación entre establecimientos.", "comunicacion"),
   O("d", "Registrar la referencia solo después de varias horas", "aceptable", "El registro tardío es mejor que ninguno, pero pierde utilidad.", "comunicacion", min=60)]),
  Mo("m5", "comunitario", "Seguimiento", "¿Cómo continúas con la paciente tras el traslado?", [
   O("a", "Coordinar la contrarreferencia y el seguimiento del puerperio", "optima", "El seguimiento posterior cierra el ciclo de atención.", min=10),
   O("b", "No hacer seguimiento", "incorrecta", "Se pierde la continuidad.", "omision"),
   O("c", "Esperar a que la familia vuelva por su cuenta", "aceptable", "Depende de la iniciativa de la familia.", "omision"),
   O("d", "Cerrar el caso sin registro", "incorrecta", "Sin registro no hay trazabilidad.", "comunicacion")])],
 "desenlaces": {"favorable": "La paciente llegó estabilizada y recibió manejo especializado.", "reservado": "La paciente llegó con demora y requirió cuidados intensivos.", "desfavorable": "Hubo una complicación grave por el retraso."},
 "evidencia": [GPC], "pendientes": ["Las cantidades de la clave azul se encuentran en la guía citada (p. 11 y 14); no se reproducen dosis en esta ficha. Falta revisión por un obstetra."]})

# ---------------------------------------------------------------- 3. Fiebre en zona tropical
guardar({"id": "s03", "numero": 3, "titulo": "Fiebre en la selva", "tema": "Enfermedades tropicales · Dengue",
 "resumen": "Adulto joven con fiebre de cuatro días en zona con dengue; aparecen signos de alarma y hay que decidir la observación o la referencia.",
 "dificultad": "intermedio", "duracion_min": 12,
 "paciente": {"titulo": "Varón de 22 años", "motivo": "Fiebre y malestar desde hace cuatro días."},
 "vitales": {"fc": 104, "pas": 100, "pad": 70, "temp": 38.9}, "gravedad": 1,
 "historia": [{"id": "h1", "rotulo": "Contexto", "texto": "Vive en zona con casos de dengue; hay zancudos en la vivienda."}, {"id": "h2", "rotulo": "Síntomas", "texto": "Dolor abdominal que aumenta y vómitos repetidos desde hoy."}],
 "examen": [{"id": "e1", "rotulo": "Abdomen", "texto": "Dolor a la palpación del hipocondrio derecho."}, {"id": "e2", "rotulo": "Piel", "texto": "Petequias aisladas; sangrado leve de encías."}],
 "pruebas": [{"id": "p1", "nombre": "Prueba rápida de dengue", "insumo": "prueba_dengue", "min": 20, "resultado": "Positiva."}],
 "eventos": [{"cuando": {"momento": "m3"}, "texto": "El paciente se muestra más decaído y con mareo al incorporarse.", "g": 1}],
 "momentos": [
  Mo("m1", "clinico", "Clasificación", "El paciente tiene fiebre, dolor abdominal, vómitos y sangrado de encías. ¿Qué haces?", [
   O("a", "Considerar dengue con signos de alarma y buscar otros signos de gravedad", "optima", "Dolor abdominal, vómitos persistentes y sangrado son signos de alarma.", ref=[(DEN, 12), (DEN, 11)], min=5, g=0),
   O("b", "Tratarlo como un resfrío común", "incorrecta", "Pasa por alto la fase crítica.", "omision", g=1),
   O("c", "Enviarlo a casa con control a la semana", "peligrosa", "Con signos de alarma no se envía a casa sin vigilancia.", "seguridad_paciente", g=2, ref=[(DEN, 12)]),
   O("d", "Esperar el resultado de laboratorio para decidir", "incorrecta", "La clínica, no la prueba, determina la conducta urgente.", "demora", min=40, g=1)]),
  Mo("m2", "recursos", "Prueba diagnóstica", "¿Cómo usas las pruebas disponibles?", [
   O("a", "Usar la prueba rápida de dengue y registrar el caso para la notificación", "optima", "Apoya la vigilancia sin retrasar el manejo.", cons={"prueba_dengue": 1}, req={"items": {"prueba_dengue": 1}}, min=20),
   O("b", "No usar ninguna prueba", "aceptable", "Se puede actuar por clínica, pero se pierde información para la vigilancia.", "omision"),
   O("c", "Usar todas las pruebas rápidas del stock", "incorrecta", "Consume el recurso que necesitan otros pacientes.", "recursos", cons={"prueba_dengue": 10}, req={"items": {"prueba_dengue": 10}}),
   O("d", "Enviar al paciente a otra ciudad por la prueba", "incorrecta", "Retrasa la atención por una prueba que no cambia la urgencia.", "demora", min=120, g=1)]),
  Mo("m3", "seguridad", "Manejo inicial", "El paciente se marea al ponerse de pie. ¿Cómo lo manejas?", [
   O("a", "Mantenerlo en observación, vigilar signos vitales, hidratar y preparar la referencia", "optima", "La observación y la referencia oportuna son lo indicado ante signos de alarma.", ref=[(DEN, 10), (DEN, 9)], cons={"suero_salino": 1, "venoclisis": 1}, req={"items": {"suero_salino": 1, "venoclisis": 1}}, min=15, g=-1),
   O("b", "Dar un medicamento para la fiebre y dejarlo ir", "peligrosa", "Pierde la ventana de seguimiento.", "seguridad_paciente", g=2),
   O("c", "Indicar un medicamento antiinflamatorio habitual", "peligrosa", "Algunos antiinflamatorios pueden aumentar el riesgo de sangrado.", "comision", g=2, pend=True),
   O("d", "Solo observar sin medir signos vitales", "incorrecta", "Sin mediciones no se detecta el deterioro.", "omision", g=1)]),
  Mo("m4", "referencia", "Referencia", "¿Cómo decides la referencia?", [
   O("a", "Referir a un establecimiento con mayor capacidad, con hoja de referencia y aviso previo", "optima", "La referencia es la transferencia de responsabilidad al nivel resolutivo.", ref=[(DEN, 9)], referencia="emergencia", min=15, g=-1),
   O("b", "No referir: se quedará en la posta", "incorrecta", "La posta no puede manejar un deterioro rápido.", "normativo", g=1),
   O("c", "Referir sin documento", "incorrecta", "Pierde información clínica importante.", "comunicacion", referencia="emergencia"),
   O("d", "Referir sin aviso", "aceptable", "Se envía, pero el hospital no se prepara.", "comunicacion", referencia="emergencia", min=15)]),
  Mo("m5", "comunitario", "Comunidad", "¿Qué haces con el entorno del paciente?", [
   O("a", "Notificar el caso y coordinar el control del vector con la comunidad", "optima", "El control del vector corta la transmisión.", min=10),
   O("b", "No hacer nada con el entorno", "incorrecta", "Se pierde la oportunidad de prevención.", "omision"),
   O("c", "Solo notificar sin acciones comunitarias", "aceptable", "Notificar es necesario, pero insuficiente.", "omision"),
   O("d", "Prohibir que los vecinos acudan a la posta", "incorrecta", "Daña la relación con la comunidad.", "comunicacion")])],
 "desenlaces": {"favorable": "El paciente llegó a tiempo y se recuperó.", "reservado": "El paciente llegó con deterioro y necesitó más cuidados.", "desfavorable": "El paciente empeoró por la demora."},
 "evidencia": [DEN], "pendientes": ["Los líquidos y el manejo de volumen se ajustan a la norma; la ficha no incluye cantidades. Falta revisión por infectólogo o internista."]})

# ---------------------------------------------------------------- 4. Diarrea persistente
guardar({"id": "s04", "numero": 4, "titulo": "Diarrea que no cede", "tema": "Pediatría · Enfermedad diarreica",
 "resumen": "Niño de dos años con diarrea de varios días, deshidratado, en una comunidad sin agua segura y con pocos sobres de sales de rehidratación.",
 "dificultad": "basico", "duracion_min": 10,
 "paciente": {"titulo": "Niño de 2 años", "motivo": "Diarrea hace cinco días y está muy sediento."},
 "vitales": {"fc": 140, "fr": 32, "temp": 37.8}, "gravedad": 1,
 "historia": [{"id": "h1", "rotulo": "Evolución", "texto": "Deposiciones líquidas varias veces al día; orina poco."}, {"id": "h2", "rotulo": "Entorno", "texto": "La familia toma agua de un río sin hervirla."}],
 "examen": [{"id": "e1", "rotulo": "Hidratación", "texto": "Ojos hundidos, mucosa seca y bebe con avidez."}],
 "pruebas": [],
 "eventos": [{"cuando": {"t": 40}, "texto": "Pasa el tiempo sin rehidratar y el niño se muestra más decaído.", "g": 1}],
 "momentos": [
  Mo("m1", "clinico", "Valoración", "¿Qué evalúas primero?", [
   O("a", "El estado de hidratación y los signos de gravedad", "optima", "La deshidratación determina el plan de manejo.", min=4, pend=True),
   O("b", "Pedir un examen de heces antes de actuar", "incorrecta", "No cambia el manejo inicial y retrasa la rehidratación.", "demora", min=60, g=1),
   O("c", "Dar un antidiarreico", "peligrosa", "No se recomienda en niños.", "comision", g=2, pend=True),
   O("d", "Indicar ayuno", "incorrecta", "El ayuno no es lo indicado en la diarrea infantil.", "comision", g=1, pend=True)]),
  Mo("m2", "recursos", "Rehidratación", "Quedan pocos sobres de sales de rehidratación oral (SRO). ¿Qué haces?", [
   O("a", "Rehidratar por vía oral con SRO y enseñar a la madre a preparar la mezcla", "optima", "Es el tratamiento de primera línea cuando se tolera la vía oral.", cons={"sro": 4}, req={"items": {"sro": 4}}, min=30, g=-1, pend=True),
   O("b", "Indicar solo líquidos caseros sin SRO", "aceptable", "Ayuda, pero no repone electrolitos adecuadamente.", "recursos", min=10, pend=True),
   O("c", "Usar todo el stock de SRO en este niño", "incorrecta", "Deja sin recursos a otros niños.", "recursos", cons={"sro": 20}, req={"items": {"sro": 20}}),
   O("d", "No rehidratar y derivar sin tratamiento", "incorrecta", "Se pierde la oportunidad de corregir la deshidratación.", "omision", g=1)]),
  Mo("m3", "seguridad", "Reevaluación", "Tras la rehidratación, ¿qué haces?", [
   O("a", "Reevaluar la hidratación y decidir si necesita referencia", "optima", "La reevaluación guía la conducta.", min=10, g=-1),
   O("b", "Dar de alta sin reevaluar", "incorrecta", "Podría persistir la deshidratación.", "omision", g=1),
   O("c", "Referir sin haber rehidratado", "aceptable", "Referir puede ser razonable, pero la rehidratación inicial no debería esperar.", "demora"),
   O("d", "Dar antibiótico de rutina", "incorrecta", "No toda diarrea requiere antibiótico.", "comision", g=1, pend=True)]),
  Mo("m4", "referencia", "Criterio de referencia", "Si el niño no mejora, ¿qué haces?", [
   O("a", "Referir con hoja de referencia y avisar", "optima", "Cuando falla el manejo en el primer nivel se refiere.", referencia="emergencia", min=15),
   O("b", "Esperar un día más", "incorrecta", "Aumenta el riesgo de deshidratación grave.", "demora", g=1),
   O("c", "No referir: la madre decide", "incorrecta", "La decisión clínica corresponde al personal.", "normativo", g=1),
   O("d", "Referir sin aviso", "aceptable", "Se refiere, pero sin coordinación.", "comunicacion", referencia="emergencia")]),
  Mo("m5", "comunitario", "Agua y saneamiento", "¿Qué haces para evitar nuevos casos?", [
   O("a", "Educar sobre el agua segura, el lavado de manos y coordinar con la comunidad", "optima", "La prevención está en el agua y la higiene.", min=10, pend=True),
   O("b", "No hacer nada", "incorrecta", "Se pierde la oportunidad de prevenir.", "omision"),
   O("c", "Dar solo un volante", "aceptable", "Informa, pero sin acompañamiento.", "omision"),
   O("d", "Culpar a la familia", "incorrecta", "No ayuda.", "comunicacion")])],
 "desenlaces": {"favorable": "El niño se rehidrató y mejoró.", "reservado": "El niño necesitó más atención.", "desfavorable": "El niño tuvo una deshidratación grave."},
 "evidencia": [], "pendientes": ["No se verificó una norma clínica peruana vigente sobre manejo de la enfermedad diarreica en el niño; el caso entero está pendiente de validación científica. La NTS 190-MINSA/CDC-2022 (RM 730-2022) trata solo de vigilancia epidemiológica."]})

# ---------------------------------------------------------------- 5. Trauma con carretera bloqueada
guardar({"id": "s05", "numero": 5, "titulo": "Trauma con la carretera bloqueada", "tema": "Emergencias · Trauma y referencia",
 "resumen": "Un obrero cae de un camión: fractura abierta de pierna. Un huaico bloquea la vía y la ambulancia no puede llegar.",
 "dificultad": "avanzado", "duracion_min": 12,
 "paciente": {"titulo": "Varón de 35 años", "motivo": "Cayó de un camión; dolor intenso en la pierna derecha."},
 "vitales": {"fc": 118, "pas": 105, "pad": 68}, "gravedad": 2,
 "historia": [{"id": "h1", "rotulo": "Mecanismo", "texto": "Caída desde unos tres metros; no perdió la conciencia."}],
 "examen": [{"id": "e1", "rotulo": "Pierna derecha", "texto": "Herida con hueso expuesto y sangrado moderado."}, {"id": "e2", "rotulo": "Resto del cuerpo", "texto": "Sin otros dolores referidos."}],
 "pruebas": [],
 "eventos": [{"cuando": {"momento": "m3"}, "texto": "Llega el aviso: un huaico bloqueó la carretera. La ambulancia no puede pasar.", "flags": ["via_bloqueada"]}],
 "momentos": [
  Mo("m1", "seguridad", "Evaluación primaria", "¿Cuál es tu primera acción?", [
   O("a", "Asegurar la escena, evaluar vía aérea, respiración y circulación y controlar el sangrado", "optima", "Se prioriza lo que amenaza la vida.", cons={"vendas": 3}, req={"items": {"vendas": 3}}, min=5, g=-1, pend=True),
   O("b", "Examinar solo la pierna", "incorrecta", "Puede pasar por alto otras lesiones.", "omision", g=1),
   O("c", "Mover al paciente sin inmovilizar", "peligrosa", "Puede agravar la lesión.", "seguridad_paciente", g=2),
   O("d", "Retrasar la atención hasta ver radiografías", "incorrecta", "Sin radiografía en la posta; retrasa el control inicial.", "demora", g=1, min=40)]),
  Mo("m2", "clinico", "Inmovilización", "¿Cómo manejas la pierna?", [
   O("a", "Cubrir la herida con apósito limpio e inmovilizar con férula", "optima", "Protege la herida y limita el daño.", cons={"ferula": 1, "vendas": 2}, req={"items": {"ferula": 1, "vendas": 2}}, min=10, g=-1, pend=True),
   O("b", "Reducir la fractura a la fuerza en la posta", "peligrosa", "Es un procedimiento que no corresponde a este nivel.", "comision", g=2),
   O("c", "Dejar la pierna sin inmovilizar", "incorrecta", "Aumenta el dolor y el riesgo.", "omision", g=1),
   O("d", "Aplicar un torniquete sin criterio", "incorrecta", "Sin indicación puede causar daño.", "comision", g=1, pend=True)]),
  Mo("m3", "referencia", "Referencia con vía bloqueada", "Informan que la carretera está bloqueada. ¿Qué decides?", [
   O("a", "Coordinar un traslado alternativo (otra ruta o medio) manteniendo al paciente estabilizado", "optima", "Las restricciones de la vía obligan a buscar alternativas sin perder la estabilización.", referencia="emergencia", min=30, g=0),
   O("b", "Solicitar la ambulancia como si nada ocurriera", "incorrecta", "La ambulancia no podrá llegar.", "comunicacion", nflag="via_bloqueada", min=60, g=1),
   O("c", "Abandonar el traslado y mantenerlo en la posta sin plan", "peligrosa", "La posta no puede ofrecer manejo definitivo.", "seguridad_paciente", g=2),
   O("d", "Enviarlo con un familiar en moto", "incorrecta", "Traslado inseguro de un paciente con fractura abierta.", "seguridad_paciente", g=1)]),
  Mo("m4", "referencia", "Comunicación", "Mientras buscas una ruta, ¿qué haces?", [
   O("a", "Mantener comunicación con el hospital y con el centro de coordinación y registrar la hora de cada paso", "optima", "Comunicar y registrar sostiene la referencia.", min=5),
   O("b", "Cortar la comunicación", "incorrecta", "Pierdes apoyo.", "comunicacion"),
   O("c", "Avisar solo a la familia", "incorrecta", "No sustituye la coordinación.", "comunicacion"),
   O("d", "Avisar tarde", "aceptable", "Avisar tarde es mejor que no avisar.", "demora", min=30)]),
  Mo("m5", "comunitario", "Registro y seguimiento", "Una vez resuelto el traslado, ¿qué haces?", [
   O("a", "Registrar el evento, la demora por la vía bloqueada y coordinar la contrarreferencia", "optima", "El registro respalda la mejora de los servicios.", min=10),
   O("b", "No registrar", "incorrecta", "Se pierde trazabilidad.", "comunicacion"),
   O("c", "Registrar sin mencionar la vía bloqueada", "aceptable", "Falta información sobre la demora.", "comunicacion"),
   O("d", "Cerrar el caso", "incorrecta", "No hay seguimiento.", "omision")])],
 "desenlaces": {"favorable": "El paciente se trasladó por una ruta alternativa y recibió tratamiento.", "reservado": "El traslado se demoró y hubo riesgo de infección.", "desfavorable": "La demora produjo una complicación grave."},
 "evidencia": [], "pendientes": ["No se verificó una guía peruana específica de trauma ortopédico ni de fractura expuesta; las decisiones están pendientes de validación científica. La referencia se apoya en definiciones generales."]})
