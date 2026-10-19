/* MedQuizPlus · «Sobrevive a la Guardia» · catálogo de casos
   Cada caso es un grafo de decisiones fijo y revisable: la evolución depende SOLO de lo que el alumno elige (no de un modelo de IA).
   Los casos están redactados con manejo estándar y ampliamente aceptado, sin dosis (siempre «según protocolo institucional»).
   Las fuentes se citan por nombre; NO se verificó el texto contra el documento original ni se indica página: están marcadas como tales.
   Es una simulación educativa: no sirve para dirigir la atención de pacientes reales. */
(function () {
  "use strict";
  var OPT = "optima", ACE = "aceptable", INC = "incorrecta", PEL = "peligrosa";
  function d(id, texto, calidad, sig, expl, tema) { return { id: id, texto: texto, calidad: calidad, siguiente: sig, explicacion: expl, tema: tema || "" }; }
  function fin(tipo, titulo, mensaje) { return { final: { tipo: tipo, titulo: titulo, mensaje: mensaje } }; }

  var CASOS = [
    {
      id: "asma", titulo: "Crisis asmática en emergencia", especialidad: "Emergencias · Neumología", dificultad: 1, requiere: null,
      resumen: "Mujer joven con disnea y sibilancias. ¿Qué haces primero y cuándo la das de alta?",
      fuentes: ["GINA (Global Initiative for Asthma). Estrategia global para el manejo y la prevención del asma: manejo de las exacerbaciones agudas (edición vigente)."],
      inicio: "n1",
      nodos: {
        n1: { estado: "Mujer de 24 años, asmática conocida, llega a emergencia con 6 horas de disnea progresiva, tos y sibilancias. Habla con frases cortas y usa los músculos accesorios.",
          vitales: { FR: "28 /min", FC: "118 /min", PA: "118/74 mmHg", "SatO₂": "90 % (aire ambiente)", T: "36.8 °C" }, gravedad: 1,
          decisiones: [
            d("a", "Oxígeno titulado (SatO₂ objetivo 93–95 %) y salbutamol inhalado repetido, añadiendo bromuro de ipratropio", OPT, "n2", "Es la base del tratamiento inicial de una exacerbación moderada a grave: oxígeno titulado, β2 agonista de acción corta repetido y, en crisis moderadas a graves, ipratropio añadido.", "Tratamiento inicial de la crisis asmática"),
            d("b", "Pedir radiografía de tórax y gasometría y esperar los resultados antes de tratar", INC, "n_det", "Los estudios no deben retrasar el oxígeno ni el broncodilatador. Se trata primero y se estudia en paralelo si hace falta.", "Tratamiento inicial de la crisis asmática"),
            d("c", "Administrar una benzodiacepina para calmar la ansiedad", PEL, "n_det", "Los sedantes están contraindicados en la crisis asmática: pueden deprimir el esfuerzo respiratorio. La «ansiedad» suele ser hipoxia.", "Seguridad: sedantes en crisis asmática"),
            d("d", "Iniciar antibiótico endovenoso empírico", INC, "n_det", "Los antibióticos no se indican de rutina en la exacerbación: solo ante evidencia de infección bacteriana. Aquí retrasan lo que sí corrige la obstrucción.", "Tratamiento inicial de la crisis asmática")
          ] },
        n2: { estado: "Una hora después: habla frases más largas, aún con sibilancias espiratorias. Recibió oxígeno, salbutamol e ipratropio.",
          vitales: { FR: "24 /min", FC: "108 /min", "SatO₂": "94 % (con O₂)", PEF: "≈ 50 % de su mejor valor" }, gravedad: 1,
          decisiones: [
            d("a", "Añadir corticoide sistémico (oral o endovenoso) de inmediato y continuar los broncodilatadores", OPT, "n3", "El corticoide sistémico debe darse de forma precoz en toda exacerbación moderada a grave: acelera la resolución y reduce las recaídas.", "Corticoide sistémico precoz"),
            d("b", "Seguir solo con salbutamol y reevaluar en 2 horas", ACE, "n3", "Mejora los síntomas, pero retrasa el corticoide, que es el tratamiento antiinflamatorio de la crisis.", "Corticoide sistémico precoz"),
            d("c", "Dar de alta con salbutamol de rescate", INC, "f_adverso", "Con respuesta incompleta (PEF ≈ 50 %) el alta es prematura: alto riesgo de recaída y de reingreso grave.", "Criterios de alta")
          ] },
        n3: { estado: "A las 3–4 horas: sin oxígeno, casi sin sibilancias, camina sin dificultad.",
          vitales: { FR: "18 /min", FC: "92 /min", "SatO₂": "96 % (aire ambiente)", PEF: "≈ 75 % de su mejor valor" }, gravedad: 0,
          decisiones: [
            d("a", "Alta con corticoide oral por pocos días, inhalador con corticoide como tratamiento de control, revisión de la técnica inhalatoria, plan de acción por escrito y control en 2 a 7 días", OPT, "f_bueno", "Una crisis es la oportunidad de iniciar o ajustar el control: corticoide inhalado, técnica, plan de acción y seguimiento precoz reducen nuevas crisis.", "Plan de alta y control del asma"),
            d("b", "Alta solo con salbutamol de rescate", ACE, "f_regular", "Está estable, pero sin tratamiento de control ni plan de acción la recaída es probable.", "Plan de alta y control del asma"),
            d("c", "Mantenerla hospitalizada una semana sin cambiar el tratamiento", INC, "f_regular", "Cumple criterios de alta: la hospitalización prolongada no aporta y expone a riesgos innecesarios.", "Criterios de alta")
          ] },
        n_det: { estado: "A los 30 minutos, sin el tratamiento adecuado: somnolienta, con sibilancias casi ausentes (tórax silencioso).",
          vitales: { FR: "34 /min", FC: "136 /min", "SatO₂": "85 % (aire ambiente)", PA: "100/60 mmHg" }, gravedad: 2,
          decisiones: [
            d("a", "Tratar como crisis casi fatal: oxígeno, broncodilatadores continuos, corticoide endovenoso, sulfato de magnesio endovenoso y avisar a UCI para soporte ventilatorio", OPT, "f_rescate", "El tórax silencioso con somnolencia es signo de agotamiento y obstrucción crítica: requiere tratamiento máximo y UCI sin demora.", "Crisis asmática casi fatal"),
            d("b", "Observarla una hora más", PEL, "f_adverso", "En una crisis crítica, esperar es peligroso: puede progresar a paro respiratorio.", "Crisis asmática casi fatal")
          ] },
        f_bueno: fin("bueno", "Buen desenlace", "Fue tratada a tiempo, evolucionó bien y salió con un plan que reduce nuevas crisis."),
        f_rescate: fin("regular", "Recuperación con retraso", "Se estabilizó, pero tras un deterioro que el tratamiento inicial pudo evitar."),
        f_regular: fin("regular", "Evolución favorable, con riesgo de recaída", "Se resolvió la crisis, pero el plan de salida no previene la siguiente."),
        f_adverso: fin("adverso", "Desenlace desfavorable (educativo)", "Una decisión insegura llevó a un empeoramiento grave. Revisa qué cambiarías.")
      }
    },
    {
      id: "apendicitis", titulo: "Dolor en fosa ilíaca derecha", especialidad: "Cirugía", dificultad: 1, requiere: null,
      resumen: "Varón joven con dolor abdominal migratorio. ¿Operas, observas o pides más estudios?",
      fuentes: ["Alvarado A. A practical score for the early diagnosis of acute appendicitis. Ann Emerg Med, 1986.", "WSES (World Society of Emergency Surgery). Jerusalem Guidelines on Diagnosis and Treatment of Acute Appendicitis (actualización 2020)."],
      inicio: "n1",
      nodos: {
        n1: { estado: "Varón de 22 años con dolor abdominal de 18 horas: empezó alrededor del ombligo y migró a la fosa ilíaca derecha. Anorexia, náuseas y un vómito. A la palpación: dolor y defensa en fosa ilíaca derecha, McBurney y Blumberg positivos. Leucocitos 15 800/mm³ con 82 % de segmentados. Puntaje de Alvarado: 10/10.",
          vitales: { T: "38.1 °C", FC: "104 /min", PA: "120/76 mmHg", FR: "18 /min", "SatO₂": "98 %" }, gravedad: 1,
          decisiones: [
            d("a", "Ayuno, vía venosa con hidratación, analgesia, antibiótico y valoración quirúrgica para apendicectomía", OPT, "n2", "Cuadro típico con Alvarado alto: el diagnóstico es clínico y corresponde preparar para cirugía sin más demora.", "Apendicitis aguda: diagnóstico y manejo"),
            d("b", "Dar de alta con analgésicos y control en 48 horas", PEL, "n_perf", "Con probabilidad muy alta de apendicitis, el alta expone a perforación y peritonitis.", "Apendicitis aguda: diagnóstico y manejo"),
            d("c", "Pedir una tomografía antes de cualquier otra medida pese al cuadro típico", ACE, "n2", "Es razonable cuando hay duda diagnóstica; con un cuadro típico y Alvarado de 10 solo retrasa la decisión y expone a radiación.", "Uso racional de imágenes"),
            d("d", "Indicar un laxante y observar en casa", PEL, "n_perf", "Los laxantes están contraindicados ante sospecha de apendicitis: aumentan el riesgo de perforación.", "Apendicitis aguda: diagnóstico y manejo")
          ] },
        n2: { estado: "Se realiza la apendicectomía sin incidentes. Hallazgo: apéndice inflamado, sin perforación, absceso ni peritonitis. Ya despierto, tolera líquidos.",
          vitales: { T: "37.4 °C", FC: "88 /min", PA: "118/72 mmHg" }, gravedad: 0,
          decisiones: [
            d("a", "Sin antibióticos posoperatorios prolongados (basta la profilaxis perioperatoria), reiniciar dieta precozmente y alta temprana", OPT, "f_bueno", "En apendicitis no complicada los antibióticos posoperatorios prolongados no aportan beneficio; la recuperación precoz es lo recomendado.", "Manejo posoperatorio"),
            d("b", "Antibióticos endovenosos por 10 días y ayuno por 3 días", INC, "f_regular", "Es excesivo para una apendicitis no complicada: prolonga la estancia y aumenta riesgos sin beneficio.", "Manejo posoperatorio")
          ] },
        n_perf: { estado: "A las 48 horas regresa con dolor abdominal difuso, fiebre alta y abdomen rígido con defensa generalizada. Hay íleo. Leucocitos 22 000/mm³.",
          vitales: { T: "39.2 °C", FC: "124 /min", PA: "100/60 mmHg", FR: "24 /min" }, gravedad: 2,
          decisiones: [
            d("a", "Reanimación con líquidos, antibióticos de amplio espectro y cirugía urgente para controlar el foco", OPT, "f_rescate", "La peritonitis generalizada requiere reanimación, antibióticos y control quirúrgico del foco sin demora.", "Peritonitis por apendicitis perforada"),
            d("b", "Solicitar solo una ecografía y esperar el resultado", PEL, "f_adverso", "El cuadro ya es de abdomen agudo peritonítico: es una indicación clínica de cirugía urgente.", "Peritonitis por apendicitis perforada")
          ] },
        f_bueno: fin("bueno", "Buen desenlace", "Diagnóstico oportuno, cirugía a tiempo y recuperación rápida."),
        f_rescate: fin("regular", "Recuperación con complicación", "Se resolvió, pero con una peritonitis que se pudo evitar."),
        f_regular: fin("regular", "Evolución favorable con exceso de tratamiento", "El paciente evoluciona bien, pero el manejo posoperatorio fue más largo de lo necesario."),
        f_adverso: fin("adverso", "Desenlace desfavorable (educativo)", "El retraso en operar llevó a un empeoramiento grave. Revisa qué cambiarías.")
      }
    },
    {
      id: "eda", titulo: "Lactante con diarrea", especialidad: "Pediatría", dificultad: 2, requiere: { caso: "asma", minimo: 60 },
      resumen: "Lactante deshidratado: elige la vía de hidratación según los signos.",
      fuentes: ["OMS. The treatment of diarrhoea: a manual for physicians and other senior health workers (2005): planes A, B y C de hidratación."],
      inicio: "n1",
      nodos: {
        n1: { estado: "Lactante de 10 meses (8 kg) con diarrea acuosa de 2 días y vómitos ocasionales. Está irritable, bebe con avidez, tiene los ojos hundidos y el pliegue cutáneo se deshace con lentitud. Está despierto, llenado capilar de 2 segundos.",
          vitales: { FC: "150 /min", FR: "36 /min", T: "37.4 °C", "SatO₂": "98 %" }, gravedad: 1,
          decisiones: [
            d("a", "Plan B: solución de rehidratación oral supervisada durante 4 horas, con reevaluación", OPT, "n2", "Con signos de deshidratación (algún grado) y sin shock, la rehidratación oral supervisada es de elección.", "Deshidratación: plan B"),
            d("b", "Plan A en casa (más líquidos) y alta inmediata", INC, "n_grave", "Presenta signos de deshidratación: necesita rehidratación supervisada. En casa puede empeorar.", "Deshidratación: plan B"),
            d("c", "Hidratación endovenosa rápida de entrada", ACE, "n2", "Funciona, pero es invasiva e innecesaria: la vía oral es de elección si el niño bebe y no hay shock.", "Vía de hidratación"),
            d("d", "Iniciar antibiótico y loperamida", PEL, "n_grave", "El antidiarreico (loperamida) está contraindicado en lactantes y la diarrea acuosa no requiere antibiótico de rutina.", "Seguridad: antidiarreicos en niños")
          ] },
        n2: { estado: "A las 4 horas: tomó la solución de rehidratación, ya no tiene ojos hundidos, las mucosas están húmedas, orina y el pliegue cutáneo es normal.",
          vitales: { FC: "122 /min", FR: "30 /min", T: "37.0 °C" }, gravedad: 0,
          decisiones: [
            d("a", "Pasar al plan A: alta con solución de rehidratación tras cada deposición, zinc por 10–14 días, continuar la lactancia y la alimentación, y signos de alarma explicados", OPT, "f_bueno", "Al hidratarse se pasa a plan A. El zinc reduce la duración y la recaída, y la alimentación no se suspende.", "Plan A y zinc"),
            d("b", "Suspender la alimentación 24 horas para «descansar el intestino»", INC, "f_regular", "El ayuno prolongado empeora el estado nutricional y no acorta la diarrea: se mantiene la lactancia y la alimentación.", "Alimentación durante la diarrea")
          ] },
        n_grave: { estado: "Dos horas después: está letárgico, con ojos muy hundidos, no puede beber, el pliegue cutáneo se deshace con mucha lentitud y el pulso es débil.",
          vitales: { FC: "176 /min", FR: "46 /min", "Llenado capilar": "4 s", "SatO₂": "96 %" }, gravedad: 2,
          decisiones: [
            d("a", "Plan C: hidratación endovenosa inmediata con cristaloide isotónico, reevaluación frecuente y paso a vía oral cuando pueda beber", OPT, "f_rescate", "Con letargia y mala perfusión (deshidratación grave) se requiere reposición endovenosa inmediata.", "Deshidratación grave: plan C"),
            d("b", "Continuar solo con solución de rehidratación oral sin vía venosa", INC, "f_adverso", "Un niño letárgico que no puede beber no se rehidrata por vía oral: necesita vía endovenosa urgente.", "Deshidratación grave: plan C")
          ] },
        f_bueno: fin("bueno", "Buen desenlace", "Rehidratado por vía oral y de alta con un plan claro."),
        f_rescate: fin("regular", "Recuperación con retraso", "Se recuperó, pero tras un deterioro que una hidratación adecuada pudo evitar."),
        f_regular: fin("regular", "Evolución favorable con un error de seguimiento", "Se hidrató, pero la indicación de alimentación no fue la adecuada."),
        f_adverso: fin("adverso", "Desenlace desfavorable (educativo)", "No se corrigió a tiempo la deshidratación grave. Revisa qué cambiarías.")
      }
    },
    {
      id: "preeclampsia", titulo: "Gestante con cefalea y presión alta", especialidad: "Ginecología y Obstetricia", dificultad: 2, requiere: { caso: "apendicitis", minimo: 60 },
      resumen: "Preeclampsia con criterios de severidad: prevenir la eclampsia y decidir el parto.",
      fuentes: ["ACOG. Practice Bulletin No. 222: Gestational Hypertension and Preeclampsia (2020).", "OMS. Recomendaciones para la prevención y el tratamiento de la preeclampsia y la eclampsia (2011)."],
      inicio: "n1",
      nodos: {
        n1: { estado: "Gestante de 34 semanas, primigesta, consulta por cefalea intensa y visión borrosa desde ayer. Presión arterial confirmada a los 15 minutos. Reflejos osteotendinosos exaltados, edema de miembros inferiores y proteinuria 3+ en tira reactiva. Frecuencia cardíaca fetal normal.",
          vitales: { PA: "168/112 mmHg", FC: "96 /min", FR: "18 /min", "SatO₂": "98 %", FCF: "144 /min" }, gravedad: 1,
          decisiones: [
            d("a", "Sulfato de magnesio para prevenir convulsiones, antihipertensivo de acción rápida, laboratorio (hemograma, plaquetas, creatinina, transaminasas, LDH), monitoreo materno-fetal y preparar la interrupción del embarazo", OPT, "n2", "Con presión ≥ 160/110 y síntomas es preeclampsia con criterios de severidad: se previene la eclampsia con magnesio, se controla la presión y se evalúa a la madre y al feto.", "Preeclampsia con criterios de severidad"),
            d("b", "Solo reposo en cama y control de presión en 2 horas", INC, "n_ecl", "Es una emergencia hipertensiva obstétrica: sin tratamiento aumenta el riesgo de convulsión y de hemorragia cerebral.", "Preeclampsia con criterios de severidad"),
            d("c", "Administrar un diurético y esperar", INC, "n_ecl", "Los diuréticos no tratan la preeclampsia ni previenen convulsiones, y pueden reducir la perfusión útero-placentaria.", "Preeclampsia con criterios de severidad"),
            d("d", "Antihipertensivo, pero sin sulfato de magnesio", ACE, "n2", "Baja la presión, pero no previene las convulsiones: el magnesio es el fármaco de elección para ello.", "Sulfato de magnesio")
          ] },
        n2: { estado: "Tras estabilizar: laboratorio con plaquetas 92 000/mm³ y transaminasas elevadas (TGO 120 U/L), creatinina normal, sin sangrado. Frecuencia cardíaca fetal sin signos de sufrimiento.",
          vitales: { PA: "148/96 mmHg", FC: "90 /min", FCF: "140 /min", Plaquetas: "92 000 /mm³" }, gravedad: 1,
          decisiones: [
            d("a", "Continuar sulfato de magnesio, controlar la presión y programar la interrupción del embarazo, eligiendo la vía según el estado materno-fetal", OPT, "f_bueno", "A las 34 semanas o más, con criterios de severidad, tras estabilizar se indica la interrupción del embarazo.", "Interrupción del embarazo"),
            d("b", "Manejo expectante hospitalizada hasta las 37 semanas", INC, "n_ecl", "Con criterios de severidad, plaquetopenia y transaminasas elevadas a las 34 semanas, esperar aumenta el riesgo materno-fetal.", "Interrupción del embarazo")
          ] },
        n_ecl: { estado: "Convulsión tónico-clónica generalizada (eclampsia). Tras la crisis, la paciente está somnolienta y la frecuencia cardíaca fetal muestra bradicardia transitoria.",
          vitales: { PA: "176/116 mmHg", FC: "110 /min", "SatO₂": "92 %", FCF: "bradicardia transitoria" }, gravedad: 2,
          decisiones: [
            d("a", "Proteger la vía aérea y colocar en decúbito lateral izquierdo, oxígeno, sulfato de magnesio endovenoso, controlar la presión y planificar la interrupción tras estabilizar", OPT, "f_rescate", "En la eclampsia se asegura la vía aérea, se da magnesio, se baja la presión y se interrumpe el embarazo una vez estabilizada la madre.", "Eclampsia"),
            d("b", "Diazepam como tratamiento de primera línea", INC, "f_adverso", "El sulfato de magnesio es el tratamiento de elección; las benzodiacepinas no son de primera línea y pueden deprimir la respiración.", "Eclampsia"),
            d("c", "Cesárea inmediata sin estabilizar a la madre", INC, "f_adverso", "Operar a una paciente inestable aumenta el riesgo materno: primero se estabiliza.", "Eclampsia")
          ] },
        f_bueno: fin("bueno", "Buen desenlace", "Se previno la eclampsia y se interrumpió el embarazo en forma oportuna."),
        f_rescate: fin("regular", "Recuperación tras eclampsia", "La madre se estabilizó, pero tras una convulsión que se pudo prevenir."),
        f_adverso: fin("adverso", "Desenlace desfavorable (educativo)", "Una decisión inadecuada en la emergencia aumentó el riesgo materno-fetal. Revisa qué cambiarías.")
      }
    },
    {
      id: "sepsis", titulo: "Fiebre y confusión en una paciente diabética", especialidad: "Medicina Interna · Emergencias", dificultad: 3, requiere: { caso: "eda", minimo: 60 },
      resumen: "Choque séptico de foco urinario: primera hora, vasopresor y control del foco.",
      fuentes: ["Surviving Sepsis Campaign. International Guidelines for Management of Sepsis and Septic Shock (2021).", "EAU (European Association of Urology). Guidelines on Urological Infections: obstrucción de la vía urinaria con sepsis."],
      inicio: "n1",
      nodos: {
        n1: { estado: "Mujer de 68 años, diabética, con fiebre, escalofríos y disuria de 3 días; hoy está confusa. Piel fría y moteada en las rodillas, llenado capilar lento. Dolor a la percusión lumbar derecha. Glucosa 280 mg/dL.",
          vitales: { T: "39.1 °C", FC: "126 /min", PA: "82/44 mmHg (PAM ≈ 57)", FR: "26 /min", "SatO₂": "93 % (aire ambiente)" }, gravedad: 2,
          decisiones: [
            d("a", "Reconocer sepsis con hipoperfusión: lactato, hemocultivos y urocultivo, antibiótico de amplio espectro de inmediato y reanimación con cristaloides con reevaluación de la perfusión", OPT, "n2", "Con hipotensión e hipoperfusión se actúa en la primera hora: cultivos sin retrasar el antibiótico, cristaloides y reevaluación (las guías sugieren al menos 30 mL/kg en las primeras 3 horas).", "Sepsis: primera hora"),
            d("b", "Pedir una tomografía abdominal y esperar el resultado antes de dar el antibiótico", INC, "n_det", "Cada hora de retraso en el antibiótico aumenta la mortalidad en el choque séptico: no se espera a las imágenes.", "Sepsis: primera hora"),
            d("c", "Antibiótico oral y alta con control ambulatorio", PEL, "n_det", "Es una paciente con hipotensión y alteración del sensorio: requiere reanimación y hospitalización urgente.", "Sepsis: primera hora"),
            d("d", "Esperar los cultivos para elegir el antibiótico", INC, "n_det", "El tratamiento empírico de amplio espectro se inicia de inmediato y luego se ajusta con los cultivos.", "Sepsis: primera hora")
          ] },
        n2: { estado: "Tras recibir cristaloides y el antibiótico (cultivos tomados), persiste la hipotensión. Lactato inicial 4.8 mmol/L y poca diuresis.",
          vitales: { PA: "84/46 mmHg (PAM ≈ 58)", FC: "120 /min", Lactato: "4.8 mmol/L", Diuresis: "escasa" }, gravedad: 2,
          decisiones: [
            d("a", "Iniciar noradrenalina para una PAM ≥ 65 mmHg, ingresar a UCI, repetir el lactato y buscar el foco con imagen renal", OPT, "n3", "Si la hipotensión persiste tras la reanimación inicial se añade vasopresor (noradrenalina de primera línea), se monitoriza la perfusión y se busca el foco.", "Choque séptico: vasopresor"),
            d("b", "Seguir aumentando los cristaloides sin vasopresor", INC, "n_det", "Más volumen sin vasopresor prolonga la hipotensión y aumenta el riesgo de sobrecarga de líquidos.", "Choque séptico: vasopresor")
          ] },
        n3: { estado: "Con vasopresor, la PAM sube a 68 mmHg y el lactato baja a 2.9 mmol/L. La ecografía muestra hidronefrosis derecha con una litiasis ureteral obstructiva.",
          vitales: { PA: "100/58 mmHg (PAM ≈ 72)", FC: "104 /min", Lactato: "2.9 mmol/L", T: "38.2 °C" }, gravedad: 1,
          decisiones: [
            d("a", "Descompresión urgente de la vía urinaria (nefrostomía percutánea o catéter doble J) y continuar el antibiótico", OPT, "f_bueno", "Una obstrucción infectada es un foco que requiere control urgente: el antibiótico solo no basta.", "Control del foco"),
            d("b", "Continuar solo con antibióticos esperando que la piedra pase", INC, "f_adverso", "Sin descomprimir la vía urinaria obstruida el foco sigue activo y el choque puede reaparecer.", "Control del foco")
          ] },
        n_det: { estado: "Dos horas después: más confusa, oligúrica y con peor perfusión.",
          vitales: { PA: "70/38 mmHg", FC: "138 /min", Lactato: "6.2 mmol/L", Diuresis: "oliguria" }, gravedad: 2,
          decisiones: [
            d("a", "Reanimación completa ya: cristaloides, vasopresor, antibiótico de amplio espectro, ingreso a UCI y control del foco", OPT, "f_rescate", "Es la corrección tardía del manejo inicial: se hace todo a la vez y sin más demora.", "Choque séptico: vasopresor"),
            d("b", "Continuar la observación en sala", PEL, "f_adverso", "Con lactato en ascenso y oliguria hay choque séptico no tratado: observar es peligroso.", "Choque séptico: vasopresor")
          ] },
        f_bueno: fin("bueno", "Buen desenlace", "Sepsis reconocida a tiempo, perfusión recuperada y foco controlado."),
        f_rescate: fin("regular", "Recuperación con retraso", "Se estabilizó, pero tras horas de retraso que aumentaron el riesgo de falla orgánica."),
        f_adverso: fin("adverso", "Desenlace desfavorable (educativo)", "El retraso o la falta de control del foco llevó a un deterioro grave. Revisa qué cambiarías.")
      }
    }
  ];

  window.MQP_GUARDIA = CASOS;
  if (typeof module !== "undefined" && module.exports) module.exports = CASOS;
})();
