# -*- coding: utf-8 -*-
"""Casos 6 a 10 de la Misión SERUMS. Casos originales y ficticios. Sin dosis."""
from lib import O, Mo, guardar
GPC, DEN, TB, FRIO = "ins-gpc03-2025", "nts211-dengue", "nts221-tb", "rm074-2026-cadena-frio"

# ---------------------------------------------------------------- 6. Sintomáticos respiratorios / TB
guardar({"id": "s06", "numero": 6, "titulo": "Tos que no se quita", "tema": "Salud pública · Tuberculosis",
 "resumen": "Un adulto con tos con flema hace tres semanas: hay que captar al sintomático respiratorio, proteger a los demás y notificar.",
 "dificultad": "intermedio", "duracion_min": 10,
 "paciente": {"titulo": "Varón de 48 años", "motivo": "Tos con flema desde hace tres semanas y pérdida de peso."},
 "vitales": {"fc": 92, "fr": 20, "temp": 37.4}, "gravedad": 1,
 "historia": [{"id": "h1", "rotulo": "Síntomas", "texto": "Tos con flema por más de 15 días, sudor nocturno y pérdida de peso."}, {"id": "h2", "rotulo": "Contacto", "texto": "Vive con su esposa y dos hijos pequeños."}],
 "examen": [{"id": "e1", "rotulo": "General", "texto": "Delgado; sin dificultad respiratoria."}],
 "pruebas": [{"id": "p1", "nombre": "Muestra de esputo", "insumo": "frasco_bk", "min": 30, "resultado": "Muestra enviada al laboratorio de referencia; el resultado tarda días."}],
 "eventos": [{"cuando": {"momento": "m4"}, "texto": "La esposa también refiere tos desde hace unas semanas.", "flags": ["contacto_sintomatico"]}],
 "momentos": [
  Mo("m1", "clinico", "Captación", "¿Cómo clasificas a este paciente?", [
   O("a", "Es un sintomático respiratorio: tos y flema de 15 días o más", "optima", "La definición operativa de sintomático respiratorio es tos con flema por 15 días o más.", ref=[(TB, 21)], min=3),
   O("b", "Esperar a que pase el resfrío", "incorrecta", "Una tos de tres semanas no se espera.", "omision", g=1),
   O("c", "Indicar un antitusivo y despedirlo", "peligrosa", "Pierde la oportunidad de diagnóstico y expone a otros.", "seguridad_paciente", g=2),
   O("d", "Pedir radiografía y no recoger esputo", "incorrecta", "La toma de muestra no debe retrasarse.", "omision", g=1, min=60)]),
  Mo("m2", "recursos", "Muestra", "¿Cómo obtienes la muestra?", [
   O("a", "Tomar la muestra en un lugar ventilado, usar un frasco y rotularlo", "optima", "Se cuidan la bioseguridad y la trazabilidad de la muestra.", cons={"frasco_bk": 1}, req={"items": {"frasco_bk": 1}}, min=20, ref=[(TB, 22)]),
   O("b", "Tomar la muestra dentro del consultorio cerrado", "incorrecta", "Aumenta el riesgo de contagio para el personal.", "seguridad_paciente", cons={"frasco_bk": 1}, req={"items": {"frasco_bk": 1}}, g=1),
   O("c", "Pedir que lleve el frasco sin rótulo", "incorrecta", "Pierde trazabilidad.", "comunicacion", cons={"frasco_bk": 1}, req={"items": {"frasco_bk": 1}}),
   O("d", "No tomar muestra", "peligrosa", "El diagnóstico no avanza.", "omision", g=2)]),
  Mo("m3", "seguridad", "Control de infecciones", "¿Qué indicaciones de prevención das?", [
   O("a", "Enseñar cobertura al toser, ventilación y uso de mascarilla mientras espera", "optima", "Reduce la transmisión mientras se aclara el diagnóstico.", min=5, pend=True),
   O("b", "Ninguna", "incorrecta", "Pierde la oportunidad de prevención.", "omision"),
   O("c", "Dejarlo en la sala de espera con otros niños", "peligrosa", "Expone a quienes son más vulnerables.", "seguridad_paciente", g=2),
   O("d", "Aislarlo sin explicar", "incorrecta", "El trato digno forma parte de la atención.", "comunicacion")]),
  Mo("m4", "referencia", "Notificación y coordinación", "¿Qué haces con la información del caso?", [
   O("a", "Inscribirlo en el registro de sintomáticos respiratorios y coordinar el envío de la muestra", "optima", "La detección y la notificación son parte del control de la tuberculosis.", ref=[(TB, 21), (TB, 22)], min=10),
   O("b", "No registrar", "incorrecta", "Se pierde el seguimiento.", "comunicacion"),
   O("c", "Registrar sin coordinar la muestra", "aceptable", "El registro es necesario pero incompleto.", "comunicacion"),
   O("d", "Esperar a que él regrese con el resultado", "incorrecta", "El establecimiento debe hacer seguimiento activo.", "omision")]),
  Mo("m5", "comunitario", "Contactos", "Ya sabes que la esposa también tose. ¿Qué haces?", [
   O("a", "Evaluar a los contactos y captar a la esposa como sintomática respiratoria", "optima", "El estudio de contactos es una acción de control.", min=15, pend=True),
   O("b", "Ignorar a los contactos", "incorrecta", "Se pierde la búsqueda de casos.", "omision"),
   O("c", "Pedirles que vengan «si se sienten mal»", "aceptable", "Depende de la iniciativa del contacto.", "omision"),
   O("d", "Informar a la comunidad el nombre del paciente", "peligrosa", "Violación de la confidencialidad.", "comunicacion", g=2)])],
 "desenlaces": {"favorable": "Se captó el caso y se inició el estudio de contactos a tiempo.", "reservado": "Hubo demora en la detección.", "desfavorable": "Se perdió seguimiento y hubo transmisión en la familia."},
 "evidencia": [TB], "pendientes": ["Solo se cita la definición de sintomático respiratorio y la notificación (NTS 221). Las acciones de bioseguridad y estudio de contactos requieren cita precisa de páginas adicionales."]})

# ---------------------------------------------------------------- 7. Desabastecimiento
guardar({"id": "s07", "numero": 7, "titulo": "Se acabó el stock", "tema": "Gestión · Desabastecimiento y priorización",
 "resumen": "El almacén de la posta casi no tiene insumos y llegan tres pacientes: debes priorizar y gestionar el pedido.",
 "dificultad": "intermedio", "duracion_min": 10,
 "paciente": {"titulo": "Tres pacientes en espera", "motivo": "Un niño con diarrea, una gestante con control y un adulto con herida."},
 "vitales": {"fc": 100}, "gravedad": 1,
 "inventario_ajuste": {"sro": 2, "suero_salino": 1, "venoclisis": 1, "vendas": 3, "oxigeno": 0},
 "historia": [{"id": "h1", "rotulo": "Almacén", "texto": "El último pedido llegó hace tres meses; hay faltantes importantes."}],
 "examen": [{"id": "e1", "rotulo": "Niño", "texto": "Diarrea con signos de deshidratación leve."}, {"id": "e2", "rotulo": "Adulto", "texto": "Herida con sangrado moderado."}],
 "pruebas": [],
 "eventos": [{"cuando": {"t": 30}, "texto": "Se acaba una de las unidades que usabas.", "inv": {"sro": -1}}],
 "momentos": [
  Mo("m1", "recursos", "Revisión", "¿Qué haces antes de atender?", [
   O("a", "Revisar el inventario y priorizar según gravedad", "optima", "Conocer lo disponible permite decidir con criterio.", min=5),
   O("b", "Usar los insumos sin revisar", "incorrecta", "Se agota lo necesario para el caso más grave.", "recursos", g=1),
   O("c", "Cerrar la posta", "incorrecta", "Deja sin atención a quienes la necesitan.", "normativo", g=1),
   O("d", "Pedir a los pacientes que traigan sus insumos", "incorrecta", "Traslada la carga a la familia.", "comunicacion")]),
  Mo("m2", "clinico", "Prioridad", "¿A quién atiendes primero?", [
   O("a", "Al paciente con mayor riesgo según su valoración", "optima", "La prioridad es clínica, no por orden de llegada.", min=5),
   O("b", "Al primero que llegó, sin valorar", "incorrecta", "Puede retrasar al más grave.", "omision", g=1),
   O("c", "Al conocido del personal", "peligrosa", "Es un criterio injusto e inseguro.", "seguridad_paciente", g=2),
   O("d", "A todos al mismo tiempo sin organización", "incorrecta", "Se pierde calidad de atención.", "omision")]),
  Mo("m3", "recursos", "Uso racional", "Hay solo dos sobres de SRO. ¿Cómo los usas?", [
   O("a", "Usarlos en el niño, enseñar a preparar suero casero seguro y registrar el faltante", "optima", "Se usa lo necesario y se documenta el faltante.", cons={"sro": 2}, req={"items": {"sro": 2}}, min=15, pend=True),
   O("b", "Guardarlos y no usarlos", "incorrecta", "El recurso existe para ser usado.", "recursos", g=1),
   O("c", "Dárselos a otro paciente sin necesidad", "incorrecta", "Uso inadecuado.", "recursos"),
   O("d", "Vender los sobres", "peligrosa", "Falta ética grave.", "normativo", g=2)]),
  Mo("m4", "referencia", "Pedido y coordinación", "¿Cómo gestionas el desabastecimiento?", [
   O("a", "Solicitar reposición por escrito, informar a la microred y registrar el faltante", "optima", "La gestión formal deja evidencia y activa la respuesta.", min=15),
   O("b", "No informar", "incorrecta", "El problema persiste.", "comunicacion"),
   O("c", "Informar verbalmente a un vecino", "incorrecta", "No es un canal oficial.", "comunicacion"),
   O("d", "Esperar al siguiente pedido", "aceptable", "No es un cierre activo.", "demora")]),
  Mo("m5", "comunitario", "Transparencia", "¿Qué le explicas a la comunidad?", [
   O("a", "Explicar la situación con honestidad y decir cómo acceder a la atención", "optima", "La transparencia mantiene la confianza.", min=10),
   O("b", "Ocultar el problema", "incorrecta", "Daña la confianza.", "comunicacion"),
   O("c", "Culpar al sistema delante de todos", "incorrecta", "No resuelve nada.", "comunicacion"),
   O("d", "No decir nada", "aceptable", "Pierde la oportunidad de informar.", "comunicacion")])],
 "desenlaces": {"favorable": "Se atendió con criterio y se activó la reposición.", "reservado": "Se atendió, pero sin gestión del faltante.", "desfavorable": "Se agotaron insumos críticos y se perjudicó a un paciente."},
 "evidencia": [], "pendientes": ["No se verificó un documento peruano de gestión de medicamentos e insumos en el primer nivel para citarlo; el caso queda pendiente de validación científica. La NTS 249-MINSA/DGAIN-2026 (RM 625-2026) define la cartera de servicios, no el manejo de stock."]})

# ---------------------------------------------------------------- 8. Vacunación y cadena de frío
guardar({"id": "s08", "numero": 8, "titulo": "Campaña de vacunación y cadena de frío", "tema": "Inmunizaciones · Cadena de frío",
 "resumen": "Jornada de vacunación en una comunidad lejana: se corta la energía y debes proteger las vacunas.",
 "dificultad": "intermedio", "duracion_min": 10,
 "paciente": {"titulo": "Jornada comunitaria", "motivo": "Se vacuna a niños en la escuela de la comunidad."},
 "vitales": {}, "gravedad": 0,
 "historia": [{"id": "h1", "rotulo": "Contexto", "texto": "La refrigeradora de la posta se apaga durante la jornada."}],
 "examen": [],
 "pruebas": [],
 "eventos": [{"cuando": {"momento": "m2"}, "texto": "Se corta la energía y la temperatura del refrigerador empieza a subir.", "flags": ["sin_energia"]}],
 "momentos": [
  Mo("m1", "recursos", "Preparación", "¿Cómo preparas la jornada?", [
   O("a", "Llevar vacunas en termo con paquetes fríos y registrar la temperatura", "optima", "El transporte debe mantener la cadena de frío.", cons={"paquetes_frios": 4}, req={"items": {"paquetes_frios": 4}}, min=15, ref=[(FRIO, 2)]),
   O("b", "Llevar las vacunas sueltas", "peligrosa", "Pueden perder potencia.", "seguridad_paciente", g=2),
   O("c", "Llevar todas las vacunas del almacén", "incorrecta", "Aumenta el riesgo de pérdida.", "recursos", g=1),
   O("d", "Suspender la jornada sin avisar", "incorrecta", "Deja a los niños sin vacunar.", "comunicacion", g=1)]),
  Mo("m2", "seguridad", "Corte de energía", "Se corta la energía en la posta. ¿Qué haces?", [
   O("a", "Trasladar las vacunas a un termo con paquetes fríos y registrar hora y temperatura", "optima", "Las vacunas se protegen y se documenta el incidente.", cons={"paquetes_frios": 4}, req={"items": {"paquetes_frios": 4}}, min=10, ref=[(FRIO, 2)]),
   O("b", "Esperar a que vuelva la luz sin hacer nada", "peligrosa", "Se arriesga la potencia de las vacunas.", "seguridad_paciente", g=2),
   O("c", "Seguir vacunando con las vacunas sin protección", "peligrosa", "Se podrían aplicar vacunas dañadas.", "seguridad_paciente", g=2),
   O("d", "Desechar todas las vacunas", "incorrecta", "Se desperdician recursos sin evaluar.", "recursos", g=1)]),
  Mo("m3", "clinico", "Decisión sobre las vacunas", "Con la temperatura registrada, ¿qué decides?", [
   O("a", "Seguir la norma vigente de cadena de frío y consultar a la microred antes de usar vacunas expuestas", "optima", "Las vacunas expuestas se evalúan según la norma, no por intuición.", ref=[(FRIO, 2)], min=15),
   O("b", "Usarlas igual: «parecen estar bien»", "peligrosa", "No se decide por apariencia.", "seguridad_paciente", g=2),
   O("c", "Descartarlas sin registro", "incorrecta", "Falta trazabilidad.", "comunicacion"),
   O("d", "Guardarlas para otra jornada sin evaluar", "incorrecta", "Podrían estar inutilizadas.", "seguridad_paciente", g=1)]),
  Mo("m4", "referencia", "Registro e información", "¿Cómo registras el incidente?", [
   O("a", "Registrar el incidente, informar a la microred y a los padres afectados", "optima", "Es una responsabilidad de seguridad.", min=10),
   O("b", "No registrar", "incorrecta", "Se oculta un riesgo.", "comunicacion"),
   O("c", "Registrar solo la hora", "aceptable", "Falta información clave.", "comunicacion"),
   O("d", "Informar solo verbalmente", "aceptable", "No deja evidencia.", "comunicacion")]),
  Mo("m5", "comunitario", "Reprogramación", "¿Cómo reprogramas la vacunación?", [
   O("a", "Reprogramar la jornada con la comunidad y comunicar fecha y lugar", "optima", "Protege la cobertura.", min=10),
   O("b", "No reprogramar", "incorrecta", "Hay niños sin vacunar.", "omision"),
   O("c", "Reprogramar sin avisar", "incorrecta", "Pierde participación.", "comunicacion"),
   O("d", "Esperar la próxima campaña", "aceptable", "Demora la protección.", "demora")])],
 "desenlaces": {"favorable": "Se protegieron las vacunas y se completó la jornada.", "reservado": "Se perdió una parte de las vacunas.", "desfavorable": "Se aplicaron vacunas comprometidas."},
 "evidencia": [FRIO], "pendientes": ["Solo se indexó la resolución RM 074-2026 (3 páginas); el anexo de la NTS 242 no se descargó. El caso no cita rangos de temperatura ni tiempos. Pendiente de validación con el anexo."]})

# ---------------------------------------------------------------- 9. Adolescente que dejó de asistir
guardar({"id": "s09", "numero": 9, "titulo": "La adolescente que dejó de venir", "tema": "Atención integral · Salud del adolescente",
 "resumen": "Una adolescente abandonó sus controles; debes retomar el contacto, escuchar y proteger su confidencialidad.",
 "dificultad": "basico", "duracion_min": 10,
 "paciente": {"titulo": "Adolescente de 16 años", "motivo": "Vuelve tras dos meses sin asistir a sus controles."},
 "vitales": {}, "gravedad": 0,
 "historia": [{"id": "h1", "rotulo": "Antecedente", "texto": "Faltó a sus controles y dejó de ir al colegio."}, {"id": "h2", "rotulo": "Hoy", "texto": "Viene sola, está callada y evita la mirada."}],
 "examen": [{"id": "e1", "rotulo": "Observación", "texto": "Aspecto cansado, tristeza visible."}],
 "pruebas": [],
 "eventos": [],
 "momentos": [
  Mo("m1", "clinico", "Acogida", "¿Cómo la recibes?", [
   O("a", "Recibirla con respeto, a solas y garantizando confidencialidad", "optima", "La confianza abre la conversación.", min=5),
   O("b", "Regañarla por faltar", "incorrecta", "Aleja a la adolescente.", "comunicacion"),
   O("c", "Hablar con su madre antes que con ella", "incorrecta", "Rompe la confidencialidad.", "comunicacion"),
   O("d", "Ignorar su silencio", "incorrecta", "Pierde información clave.", "omision")]),
  Mo("m2", "clinico", "Valoración", "¿Qué exploras?", [
   O("a", "Su salud física, emocional y social (escuela, familia, riesgos) con preguntas abiertas", "optima", "La valoración integral detecta riesgos.", min=15, pend=True),
   O("b", "Solo el peso y la talla", "aceptable", "Es parcial.", "omision"),
   O("c", "Solo preguntar si menstrúa", "incorrecta", "Visión muy limitada.", "omision"),
   O("d", "No explorar nada", "incorrecta", "Se pierde la oportunidad.", "omision")]),
  Mo("m3", "seguridad", "Señales de riesgo", "Refiere tristeza intensa y ganas de no estar. ¿Qué haces?", [
   O("a", "Explorar el riesgo de forma directa y respetuosa, acompañarla y activar la ruta de salud mental", "optima", "Ante señales de riesgo se actúa de inmediato.", min=15, pend=True, referencia="programada"),
   O("b", "Restar importancia", "peligrosa", "Puede dejarla sin protección.", "seguridad_paciente", g=2),
   O("c", "Dejarla ir sola sin plan", "peligrosa", "No asegura su protección.", "seguridad_paciente", g=2),
   O("d", "Decirle que «ya pasará»", "incorrecta", "Minimiza su malestar.", "comunicacion", g=1)]),
  Mo("m4", "referencia", "Coordinación", "¿Cómo coordinas su atención?", [
   O("a", "Coordinar con salud mental y con la familia con su consentimiento, y programar seguimiento", "optima", "La coordinación respeta sus derechos.", min=15, pend=True),
   O("b", "No coordinar", "incorrecta", "Sin red de apoyo.", "omision"),
   O("c", "Informar a toda la comunidad", "peligrosa", "Rompe la confidencialidad.", "comunicacion", g=2),
   O("d", "Coordinar sin su conocimiento", "incorrecta", "No respeta su participación.", "comunicacion")]),
  Mo("m5", "comunitario", "Reintegración", "¿Cómo ayudas a que retome sus controles?", [
   O("a", "Acordar con ella un plan de seguimiento y coordinar con la escuela solo lo que ella autorice", "optima", "Favorece la continuidad.", min=10, pend=True),
   O("b", "Citar sin explicar", "aceptable", "No genera compromiso.", "comunicacion"),
   O("c", "No hacer seguimiento", "incorrecta", "Puede volver a abandonar.", "omision"),
   O("d", "Informar a la escuela todo", "incorrecta", "Rompe la confidencialidad.", "comunicacion")])],
 "desenlaces": {"favorable": "La adolescente retomó sus controles con apoyo.", "reservado": "La adolescente volvió, pero sin plan claro.", "desfavorable": "Se perdió el contacto y se agravó su situación."},
 "evidencia": [], "pendientes": ["No se verificó la norma peruana de atención integral del adolescente ni la ruta de salud mental vigente; el caso queda pendiente de validación científica."]})

# ---------------------------------------------------------------- 10. Brote gastrointestinal
guardar({"id": "s10", "numero": 10, "titulo": "Brote de diarrea en la comunidad", "tema": "Vigilancia epidemiológica · Brotes",
 "resumen": "Varias familias de un mismo anexo enferman con diarrea; debes sospechar un brote, notificar y actuar.",
 "dificultad": "avanzado", "duracion_min": 12,
 "paciente": {"titulo": "Siete personas con diarrea", "motivo": "Familias de un mismo anexo con diarrea y vómitos en tres días."},
 "vitales": {}, "gravedad": 1,
 "historia": [{"id": "h1", "rotulo": "Contexto", "texto": "Comparten una fuente de agua y comieron en una celebración común."}],
 "examen": [{"id": "e1", "rotulo": "Casos", "texto": "Dos niños con deshidratación; el resto con síntomas leves."}],
 "pruebas": [],
 "eventos": [{"cuando": {"t": 45}, "texto": "Llegan dos casos más del mismo anexo.", "g": 1}],
 "momentos": [
  Mo("m1", "clinico", "Sospecha", "Varios casos con el mismo cuadro. ¿Qué concluyes?", [
   O("a", "Sospechar un brote con fuente común y atender primero a los más graves", "optima", "Reconocer el patrón activa la respuesta.", min=5, pend=True),
   O("b", "Tratar cada caso como aislado", "incorrecta", "Pierde la señal del brote.", "omision", g=1),
   O("c", "Esperar más casos antes de actuar", "peligrosa", "Retrasa el control.", "demora", g=2),
   O("d", "Culpar a una familia", "incorrecta", "No ayuda a controlar el brote.", "comunicacion")]),
  Mo("m2", "recursos", "Atención", "Hay dos niños con deshidratación. ¿Cómo los manejas?", [
   O("a", "Rehidratar según el estado de hidratación y priorizar a los más graves, cuidando el stock", "optima", "Atiende con criterio y cuida el recurso.", cons={"sro": 6}, req={"items": {"sro": 6}}, min=30, g=-1, pend=True),
   O("b", "Atenderlos por orden de llegada sin valorar", "incorrecta", "Puede retrasar al más grave.", "omision", g=1),
   O("c", "Usar todos los sobres en uno", "incorrecta", "Deja sin recursos al otro.", "recursos", cons={"sro": 20}, req={"items": {"sro": 20}}),
   O("d", "Referirlos a todos sin valorar", "incorrecta", "Satura el hospital.", "recursos")]),
  Mo("m3", "referencia", "Notificación", "¿Qué haces con la información del brote?", [
   O("a", "Notificar de inmediato a epidemiología según la vía oficial y registrar los casos", "optima", "La notificación oportuna activa la investigación.", min=15, pend=True),
   O("b", "No notificar", "peligrosa", "Se oculta el brote.", "seguridad_paciente", g=2),
   O("c", "Notificar al final de la semana", "incorrecta", "Retrasa la respuesta.", "demora"),
   O("d", "Notificar solo de forma verbal", "aceptable", "No deja evidencia.", "comunicacion")]),
  Mo("m4", "seguridad", "Control", "¿Qué medidas inmediatas recomiendas?", [
   O("a", "Recomendar agua segura, lavado de manos y manejo seguro de alimentos, e identificar la fuente", "optima", "Corta la transmisión.", min=15, pend=True),
   O("b", "No recomendar nada", "incorrecta", "Continúan los casos.", "omision", g=1),
   O("c", "Cerrar la posta", "incorrecta", "Deja sin atención.", "normativo", g=1),
   O("d", "Recomendar solo antibióticos para todos", "peligrosa", "Uso inadecuado de antibióticos.", "comision", g=2)]),
  Mo("m5", "comunitario", "Comunicación de riesgo", "¿Cómo informas a la comunidad?", [
   O("a", "Informar con claridad, sin culpar, y coordinar con el comité local y las autoridades", "optima", "La comunicación de riesgo favorece la cooperación.", min=15),
   O("b", "Ocultar el brote", "peligrosa", "Pone en riesgo a más personas.", "comunicacion", g=2),
   O("c", "Informar con alarma exagerada", "incorrecta", "Genera pánico.", "comunicacion"),
   O("d", "No informar", "incorrecta", "La comunidad no puede protegerse.", "comunicacion")])],
 "desenlaces": {"favorable": "Se controló el brote con notificación y medidas oportunas.", "reservado": "El brote se prolongó por demora en la respuesta.", "desfavorable": "El brote se extendió por falta de notificación."},
 "evidencia": [], "pendientes": ["La NTS 190-MINSA/CDC-2022 (RM 730-2022) regula la vigilancia de la EDA, pero su texto no se indexó; el caso no cita páginas y queda pendiente de validación científica."]})
