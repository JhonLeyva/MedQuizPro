# -*- coding: utf-8 -*-
"""Residentado Médico · lote 1 · flujogramas 14-38 (anestesiología, fisiología cardiovascular, shock y marcadores)."""
from c_rm import S, P, PX, B, Q, L, TR, ATLS, HARRISON, WILLIAMS, NELSON, MINSA, ACOG, AAP
from c26 import D
import ilu7 as I
MILLER = "Miller Anestesia 9.ª ed."
GUYTON = "Guyton y Hall Tratado de Fisiología Médica 14.ª ed."
BRAUN = "Braunwald Tratado de Cardiología 12.ª ed."
ECGP = "Trazado de enseñanza MedQuizPro (no es de un paciente)"

# 14 · RM-CIR-001 · CUADRÍCULA: clases de antiarrítmicos
S("cuadricula", "RM-CIR-001", "La lidocaína, anestésico local, también se usa en arritmias ventriculares",
  "Farmacología · antiarrítmicos (Vaughan Williams)",
  ("Lidocaína antiarrítmica", ["Clase Ib: bloquea los canales de sodio inactivados y acorta el potencial de acción.", "Actúa solo en tejido isquémico o despolarizado: el ventrículo."]),
  ("Pregunta de teoría", ["¿En qué arritmias se usa la lidocaína?"]),
  ["Clase Ib (lidocaína, mexiletina): arritmias ventriculares del infarto, intoxicación digitálica y cirugía cardiaca.",
   "En el paro por FV/TV sin pulso refractaria a descargas: amiodarona o lidocaína (AHA).",
   "Toxicidad: parestesias periorales, tinnitus, convulsiones, bradicardia. No sirve en arritmias auriculares."],
  "AHA, Soporte Vital Cardiovascular Avanzado (actualización 2025); Goodman & Gilman Bases Farmacológicas de la Terapéutica 14.ª ed.",
  op=("¿Dónde sirve?", ["Sí: tejido ventricular isquémico", "No: el tejido auricular se recupera rápido del bloqueo", "No: no actúa sobre el nodo AV", "No: «refractarias» no es una localización", "No: no bloquea la conducción AV"]),
  d=dict(rotulo="Clases de antiarrítmicos y para qué sirven", alto_img=0,
         celdas=[("I · bloqueantes de sodio", ["Ia procainamida · Ib lidocaína · Ic flecainida", "Lidocaína = Ib (este caso)"], None, True),
                 ("II · betabloqueantes", ["Metoprolol, esmolol", "Taquicardias supraventriculares y control de la FC"], None, False),
                 ("III · bloqueantes de potasio", ["Amiodarona, sotalol", "Arritmias ventriculares y auriculares"], None, False),
                 ("IV · calcioantagonistas", ["Verapamilo, diltiazem", "TSV y control de FC en FA"], None, False)],
         veredicto=("Lidocaína = clase Ib: arritmias ventriculares", "No es útil en las auriculares.")))

# 15 · RM-CIR-002 · CASCADA: hipotensión raquídea
S("cascada", "RM-CIR-002", "La hipotensión es la complicación más frecuente de la anestesia raquídea",
  "Anestesiología · bloqueo neuroaxial",
  ("Hipotensión en la anestesia raquídea", ["El bloqueo simpático dilata arterias y, sobre todo, venas.", "Cae el retorno venoso y el gasto cardiaco; si el bloqueo es alto, también se bloquea el corazón."]),
  ("Pregunta de teoría", ["¿Cuál es la complicación más frecuente de la raquídea?"]),
  ["Más riesgo con bloqueo alto, hipovolemia, embarazo (compresión aortocava) y obesidad.",
   "Prevención: cocarga con cristaloides y desplazamiento uterino lateral en la gestante.",
   "Tratamiento: fenilefrina o efedrina; atropina si hay bradicardia."],
  MILLER + "; ASA, Practice Guidelines for Obstetric Anesthesia (2016).",
  op=("¿Más frecuente?", ["No: es poco frecuente y casi nunca grave", "No: transitorias y poco frecuentes", "Sí: el bloqueo simpático dilata los vasos", "No: es rara con agujas finas", "No: la alergia es excepcional"]),
  d=dict(rotulo="Del bloqueo simpático a la hipotensión", cabeceras=("Paso", "Qué ocurre"),
         pasos=[("Bloqueo simpático (T1-L2)", "Se pierde el tono vascular", [("Arterias y venas se dilatan", "", False)]),
                ("Cae el retorno venoso", "Sangre acumulada en las venas", [("Menos llenado del corazón", "Menor volumen sistólico", False)]),
                ("Hipotensión (± bradicardia)", "Si el bloqueo sube a T4", [("Fenilefrina o efedrina; atropina", "Tratamiento", True)])],
         veredicto=("La hipotensión es la complicación más frecuente", "Prevenir con volumen; tratar con vasopresor.")))

# 16 · RM-CIR-003 · MATRIZ: ésteres y amidas
S("matriz", "RM-CIR-003", "La procaína es el anestésico local del grupo éster de la lista",
  "Anestesiología · anestésicos locales",
  ("Ésteres y amidas", ["Se diferencian por el enlace entre el anillo aromático y la cadena amínica.", "Los ésteres se hidrolizan en el plasma; las amidas, en el hígado."]),
  ("Pregunta de teoría", ["¿Cuál de las opciones es un éster?"]),
  ["Ésteres: procaína, tetracaína, cocaína, cloroprocaína, benzocaína. Producen PABA: más alergias.",
   "Amidas: lidocaína, mepivacaína, bupivacaína, ropivacaína, prilocaína, articaína (llevan «i» antes de «caína»).",
   "Hepatopatía grave: reducir la dosis de amidas; déficit de colinesterasa: la de ésteres."],
  MILLER + "; Goodman & Gilman Bases Farmacológicas de la Terapéutica 14.ª ed.",
  op=("¿Éster?", ["No: es amida", "No: es amida", "No: es amida", "Sí: único éster de la lista", "No: es amida"],
      {0: "Lidocaína", 1: "Bupivacaína", 2: "Mepivacaína", 3: "Procaína", 4: "Ropivacaína"}),
  d=dict(rotulo="Dos familias de anestésicos locales", eje_x="Grupo", eje_y="Característica",
         cols=["Ésteres", "Amidas"], rows=["Ejemplos", "Metabolismo y alergia"], caso=(0, 0),
         cells=[[("Procaína, tetracaína, cocaína", ["Cloroprocaína, benzocaína"]), ("Lidocaína, bupivacaína, ropivacaína", ["Mepivacaína, prilocaína, articaína"])],
                [("Hidrólisis plasmática", ["Producen PABA: alergia más frecuente"]), ("Metabolismo hepático", ["Alergia rara; más estables y duraderas"])]]))

# 17 · RM-CIR-004 · ÁRBOL: variante de éster
S("arbol", "RM-CIR-004", "Entre los anestésicos de la lista, la procaína es el único éster",
  "Anestesiología · anestésicos locales (variante)",
  ("Cómo reconocer un éster", ["Los ésteres no tienen una «i» antes de «caína».", "Se hidrolizan por colinesterasas del plasma."]),
  ("Pregunta de teoría", ["¿Cuál de estos anestésicos es del grupo éster?"]),
  ["Regla práctica: las amidas llevan «i» antes de «caína» (lidocaína, bupivacaína, mepivacaína, prilocaína).",
   "La cocaína, también éster, es el único anestésico local con vasoconstricción propia.",
   "En tejido infectado y ácido disminuye la eficacia: la forma no ionizada es la que atraviesa la membrana."],
  MILLER + "; Katzung Farmacología Básica y Clínica 15.ª ed.",
  op=("¿Éster?", ["Sí: único éster de la lista", "No: es amida", "No: es amida", "No: es amida", "No: es amida"],
      {0: "Procaína", 1: "Lidocaína", 2: "Bupivacaína", 3: "Mepivacaína", 4: "Prilocaína"}),
  arbol=Q("¿Lleva una «i» antes de «caína»?", [
      L("Sí (lidocaína, bupivacaína…)", "AMIDA", ["Metabolismo hepático", "Alergia rara"]),
      L("No (este caso)", "ÉSTER: PROCAÍNA", ["Hidrólisis plasmática", "Produce PABA"], path=True)], path=True))

# 18 · RM-CIR-005 · DECISIÓN: raquídea vs epidural
S("decision", "RM-CIR-005", "La anestesia raquídea se inyecta en el espacio subaracnoideo",
  "Anestesiología · técnicas neuroaxiales",
  ("Raquídea y epidural", ["La raquídea deposita el anestésico en el líquido cefalorraquídeo (subaracnoideo).", "La epidural lo coloca fuera de la duramadre."]),
  ("Pregunta de teoría", ["¿En qué nivel se inyecta el anestésico de la raquídea?"]),
  ["Raquídea: aguja fina en L3-L4 o L4-L5, por debajo del cono medular (L1-L2): bloqueo rápido y denso con dosis bajas.",
   "Epidural: volúmenes mayores, inicio más lento, permite catéter (analgesia del parto).",
   "Contraindicaciones absolutas: rechazo, infección local, coagulopatía, hipertensión endocraneana."],
  MILLER + "; ASRA, anestesia regional en pacientes anticoagulados (4.ª ed., 2018).",
  op=("¿Nivel?", ["Sí: dentro del líquido cefalorraquídeo", "No: es la técnica epidural", "No: es anestesia local", "No: es infiltración", "No: es un bloqueo de plexo, no neuroaxial"],
      {0: "Subaracnoideo", 1: "Epidural", 2: "Local", 3: "Sitio operatorio", 4: "Plexo lumbar"}),
  d=dict(rotulo="Dos técnicas neuroaxiales", eje_y="Técnica", ancho_filas=190,
         cols=["Dónde se inyecta", "Cómo actúa"],
         rows=[("Raquídea", "Espinal"), ("Epidural", "Peridural")],
         cells=[[("Espacio subaracnoideo", ["En el LCR, L3-L4"]), ("Inicio rápido, bloqueo denso", ["Dosis baja"])],
                [("Espacio epidural", ["Fuera de la duramadre"]), ("Inicio lento, con catéter", ["Volúmenes mayores"])]],
         caso=(0, 0), nota="Raquídea = subaracnoidea: el nombre «espinal» lo recuerda."))

# 19 · RM-CIR-006 · TERMÓMETRO: escala ASA
S("termometro", "RM-CIR-006", "Mujer con colecistitis aguda e insuficiencia cardiaca congestiva: ASA IV según la clave del libro",
  "Anestesiología · riesgo anestésico (ASA)",
  ("Clasificación ASA", ["Estima el riesgo anestésico por las comorbilidades: I sano a VI muerte cerebral.", "La «E» indica urgencia."]),
  ("Mujer de 70 años", ["Colecistitis aguda y antecedente de insuficiencia cardiaca congestiva.", "¿Qué clase ASA le corresponde?"]),
  ["La insuficiencia cardiaca bien compensada es ASA III; descompensada y con cuadro séptico agudo se asigna ASA IV (clave del libro).",
   "ASA IV: enfermedad grave que es amenaza constante para la vida (infarto reciente, sepsis, IC descompensada).",
   "Cirugía urgente en ASA IV: mortalidad perioperatoria alta; requiere monitorización invasiva."],
  "ASA, Physical Status Classification System (actualización 2020); " + MILLER,
  op=("¿Clase ASA?", ["Sí: IC con cuadro agudo, amenaza para la vida", "No: es enfermedad leve", "No: IC compensada sería ASA III", "No: es el moribundo que no sobrevive sin la operación", "No: es muerte cerebral, donante"]),
  d=dict(rotulo="Clasificación ASA de menor a mayor riesgo", caso_nivel=2, ruta_titulo="Qué implica en este caso", paso_label="ESTE CASO",
         niveles=[("ASA I-II", "Sano o enfermedad leve", ["Sin limitación funcional"]), ("ASA III", "Enfermedad grave", ["IC compensada"]),
                  ("ASA IV", "Amenaza constante para la vida", ["IC descompensada, sepsis"]), ("ASA V-VI", "Moribundo o muerte cerebral", ["Sin la operación no sobrevive"])],
         pasos=[(1, "Optimizar si es posible", ["Diuréticos, O₂, corregir electrolitos"], True), (2, "Monitorización invasiva", ["Línea arterial, catéter central"], False),
                (3, "Anestesia con mínima depresión", ["Evitar cambios bruscos de volumen"], False)]),
  clasif=dict(titulo="Clasificación ASA del estado físico (ASA 2020)", cols=["Clase", "Definición", "Ejemplo"],
              filas=[["ASA I", "Paciente sano", "Sin enfermedad; no fuma ni abusa del alcohol"],
                     ["ASA II", "Enfermedad sistémica leve", "Fumador, HTA o DM controladas, obesidad leve"],
                     ["ASA III", "Enfermedad sistémica grave", "IC compensada, DM mal controlada, EPOC, IMC ≥ 40"],
                     ["ASA IV", "Enfermedad grave, amenaza constante para la vida", "IC descompensada, sepsis, infarto reciente"],
                     ["ASA V", "Moribundo: no sobrevive sin la operación", "Aneurisma roto, isquemia intestinal masiva"],
                     ["ASA VI", "Muerte cerebral, donante de órganos", "Donación de órganos"]], caso=3, ancho_primera=165,
              nota="La letra «E» se añade si la cirugía es de urgencia (p. ej., ASA IV E)."))

# 20 · RM-CIR-007 · CHECKLIST: paciente deshidratado
S("checklist", "RM-CIR-007", "En el paciente mal hidratado la complicación más frecuente de la raquídea es la hipotensión",
  "Anestesiología · prevención de hipotensión",
  ("Raquídea en el paciente hipovolémico", ["La venodilatación del bloqueo se suma a un volumen circulante ya bajo.", "La hipotensión es más rápida y profunda."]),
  ("Pregunta de teoría", ["¿Cuál es la complicación más frecuente en estos pacientes?"]),
  ["Reponer volumen antes de la punción (precarga o cocarga con cristaloides).",
   "Vasopresor (fenilefrina o efedrina) y atropina si hay bradicardia.",
   "Cefalea pospunción: 72 h, mejora acostado; inconsciencia sugiere raquídea total (rara y grave)."],
  MILLER + "; Barash Anestesia Clínica 8.ª ed.",
  op=("¿Más frecuente?", ["Sí: venodilatación + hipovolemia", "No: transitorias", "No: aparece con bloqueos altos", "No: indicaría raquídea total", "No: ocurre en 72 horas, menos frecuente"]),
  d=dict(rotulo="Cómo evitar y tratar la hipotensión", tag="MEDIDA CLAVE",
         pasos=[("Reponer volumen antes de la punción", "Cristaloides: precarga o cocarga", True), ("Posición y desplazamiento uterino", "En la gestante: izquierda", False),
                ("Fenilefrina o efedrina", "Si baja la PA", False), ("Atropina", "Si hay bradicardia", False)],
         no_hacer=[("Puncionar sin corregir la hipovolemia", "Hipotensión profunda"), ("Bloqueo alto sin vigilancia", "Bradicardia y paro")],
         veredicto=("Hipotensión: la complicación más frecuente", "Se previene con volumen y se trata con vasopresor.")))

# 21 · RM-CIR-008 · RADIAL: tipos de anestesia
S("radial", "RM-CIR-008", "La anestesia neuroaxial (raquídea y epidural) es un tipo de anestesia regional",
  "Anestesiología · clasificación de la anestesia",
  ("Tipos de anestesia", ["General (pierde la conciencia), regional (neuroaxial o de nervios), local y sedación.", "La neuroaxial es regional."]),
  ("Pregunta de teoría", ["¿Cómo se llama la anestesia neuroaxial?"]),
  ["Regional: neuroaxial (raquídea y epidural) y bloqueos de nervios periféricos.",
   "El espacio «subdural» no existe como espacio real: la inyección subdural inadvertida da un bloqueo extenso e irregular.",
   "Si la pregunta busca el nombre amplio, la opción es «regional»; la específica sería «epidural»."],
  MILLER + "; Barash Anestesia Clínica 8.ª ed.",
  op=("¿Tipo?", ["No: es analgesia con vigilancia, no neuroaxial", "No: es la vía del fármaco, no el tipo", "No: el espacio subdural no es una técnica", "No: pierde la conciencia", "Sí: bloquea raíces nerviosas, conciencia conservada"]),
  d=dict(rotulo="Los tipos de anestesia", centro="ANESTESIA", centro_sub="según la extensión", ans=1,
         items=[("GENERAL", ["Pérdida de la conciencia"]), ("REGIONAL", ["Neuroaxial y bloqueos de nervios"]), ("LOCAL", ["Infiltración en el sitio"]),
                ("SEDACIÓN", ["Calma con vigilancia"]), ("TÓPICA", ["Mucosas o piel"])],
         ruta=["Neuroaxial", "Raquídea o epidural", "Anestesia regional", "Conciencia conservada"]))

# 22 · RM-CIR-009 · ALARMA: bloqueo en quemado
S("alarma", "RM-CIR-009", "En un gran quemado con fasciotomía, la complicación más frecuente de la anestesia epidural es la hipotensión",
  "Anestesiología · epidural en el paciente quemado",
  ("Hipotensión por bloqueo simpático", ["En el quemado hay hipovolemia, fuga de plasma e inflamación sistémica.", "La epidural da hipotensión más gradual que la raquídea."]),
  ("Varón de 36 años, quemado", ["45 % de superficie con 2.º grado y 3.er grado en miembros inferiores.", "Fasciotomía; recibió 2 L de solución salina."]),
  ["Reposición con cristaloides según Parkland (4 mL × kg × % SCQ en 24 h, la mitad en las primeras 8 h) y vasopresores listos.",
   "La cefalea pospunción solo aparece si hay punción accidental de la duramadre.",
   "La parálisis respiratoria se ve con bloqueos muy altos; la relajación muscular es un efecto buscado."],
  MILLER + "; ISBI, Practice Guidelines for Burn Care (2016 y 2018).",
  op=("¿Más frecuente?", ["No: no es complicación de la epidural", "No: es un efecto buscado", "Sí: vasodilatación del bloqueo simpático", "No: solo con bloqueos muy altos", "No: solo si hay punción dural accidental"],
      {0: "Cardiopatía isquémica", 1: "Relajación muscular", 2: "Hipotensión arterial", 3: "Parálisis respiratoria", 4: "Cefalea intensa"}),
  d=dict(rotulo="Qué vigilar durante el bloqueo en el quemado", lista_titulo="Alertas en la epidural",
         signos=[("Hipotensión", "Vasodilatación del bloqueo + hipovolemia", True), ("Taquicardia", "Compensadora", True), ("Bradicardia", "Si el bloqueo sube a T4", None),
                 ("Bloqueo alto (disnea, brazos débiles)", "Parálisis respiratoria", None), ("Cefalea postural", "Solo si hay punción dural", None)],
         accion=("Cristaloides + vasopresor", "Fenilefrina o efedrina; atropina si hay bradicardia."), accion_rotulo="Si baja la PA",
         veredicto=("Hipotensión arterial: la complicación más frecuente", "Se agrava por la hipovolemia del quemado.")))

# 23 · RM-CIR-010 · REGLA: duración de los anestésicos locales
S("regla", "RM-CIR-010", "La bupivacaína es el anestésico local de acción prolongada",
  "Anestesiología · duración de los anestésicos locales",
  ("Duración de acción", ["Depende de la liposolubilidad y de la unión a proteínas.", "Bupivacaína, ropivacaína y levobupivacaína duran 2-8 h."]),
  ("Mujer de 48 años", ["Hernia inguinal crónica con anestesia epidural.", "Se busca analgesia posoperatoria prolongada."]),
  ["Corta: articaína, cloroprocaína (30-60 min). Intermedia: lidocaína, mepivacaína (1-2 h). Prolongada: bupivacaína, ropivacaína.",
   "Bupivacaína: mayor cardiotoxicidad; dosis máxima 2,5 mg/kg; evitar inyección intravascular.",
   "Intoxicación grave: emulsión lipídica al 20 % (bolo 1,5 mL/kg) y soporte vital."],
  MILLER + "; ASRA, toxicidad sistémica por anestésicos locales (2020).",
  op=("¿Prolongado?", ["No: corta", "No: intermedia", "No: corta", "No: intermedia", "Sí: 2-8 horas"],
      {0: "Articaína", 1: "Lidocaína", 2: "Cloroprocaína", 3: "Mepivacaína", 4: "Bupivacaína"}),
  d=dict(rotulo="Cuánto dura cada anestésico local",
         reglas=[dict(nombre="Duración de la anestesia (horas)", que="Corta < 1 h · intermedia 1-2 h · prolongada > 2 h.",
                      min=0, max=8, fmt="{}", ticks=[1, 2, 4, 6, 8],
                      bandas=[(0, 1, "Corta", 0), (1, 2, "Intermedia", 1), (2, 8, "Prolongada: bupivacaína", 3)], caso=6, caso_txt="BUPIVACAÍNA: 2-8 h")],
         claves_titulo="Seguridad de la bupivacaína",
         claves=[("Cardiotóxica", ["Se une con fuerza al canal de sodio cardiaco"], True), ("Dosis máxima", ["2,5 mg/kg"], False), ("Antídoto", ["Emulsión lipídica 20 %"], False)]))

# 24 · RM-CIR-011 · EMBUDO: anestesia en peritonitis
S("embudo", "RM-CIR-011", "Peritonitis difusa por apendicitis complicada: anestesia general",
  "Anestesiología · elección de la técnica",
  ("Elección de la anestesia", ["Depende de la cirugía y del estado del paciente.", "Peritonitis: lavado amplio, relajación completa y riesgo de aspiración."]),
  ("Mujer de 20 años", ["Peritonitis difusa por apendicitis complicada.", "Será intervenida de urgencia."]),
  ["Anestesia general con intubación y secuencia rápida: protege la vía aérea y relaja por completo.",
   "Neuroaxial: relativamente contraindicada por la sepsis (hipotensión, riesgo de infección neuroaxial).",
   "Óxido nitroso: evitar en íleo, porque difunde a las asas y las distiende."],
  MILLER + "; Sabiston Tratado de Cirugía 21.ª ed.; WSES, apendicitis aguda (2020).",
  op=("¿Mejor técnica?", ["No: sepsis y riesgo de hipotensión", "No: sin protección de vía aérea ni relajación", "No: no protege contra la aspiración", "Sí: relajación completa y vía aérea protegida", "No: distiende las asas en el íleo"]),
  d=dict(rotulo="Descarta las técnicas que no protegen ni relajan", inicio="Anestesia para laparotomía por peritonitis",
         candidatos=["Espinal", "Epidural", "Máscara laríngea", "Óxido nitroso", "General"],
         pasos=[("¿Protege la vía aérea del vómito y la aspiración?", ["Máscara laríngea", "Espinal"]),
                ("¿Da relajación completa sin hipotensión grave en la sepsis?", ["Epidural", "Óxido nitroso"])],
         final=("ANESTESIA GENERAL", ["Intubación con secuencia rápida", "Relajación completa para el lavado"]),
         nota="El óxido nitroso distiende las asas: se evita en el íleo."))

# 25 · RM-CB-014 · LABORATORIO: flujo sanguíneo por órgano
S("laboratorio", "RM-CB-014", "El riñón tiene el mayor flujo sanguíneo por cada 100 g de tejido",
  "Fisiología · circulación por órganos",
  ("Flujo por 100 g", ["El riñón recibe 20-25 % del gasto cardiaco en solo 300 g.", "Su flujo sirve para filtrar, no para el consumo de oxígeno."]),
  ("Pregunta de teoría", ["¿Qué órgano tiene el mayor flujo por 100 g de tejido?"]),
  ["Riñón: unos 350-400 mL/min/100 g. Cerebro: 50. Miocardio: 70-80. Hígado: 90-100 (mayor flujo absoluto, ≈ 1350 mL/min).",
   "La diferencia arteriovenosa de O₂ del riñón es pequeña: se perfunde para filtrar.",
   "El miocardio extrae casi todo el oxígeno: el aumento de demanda solo se cubre con más flujo coronario."],
  GUYTON + "; Boron y Boulpaep Fisiología Médica 3.ª ed.",
  op=("¿Mayor flujo por 100 g?", ["Sí: ≈ 360 mL/min/100 g", "No: 50 mL/min/100 g", "No: 70-80 mL/min/100 g", "No: bajo, salvo para termorregulación", "No: 90-100 mL/min/100 g"],
      {0: "Riñón", 1: "Cerebro", 2: "Miocardio", 3: "Piel", 4: "Hígado"}),
  d=dict(rotulo="Flujo sanguíneo de cada órgano", valores=[
            ("Riñón", "≈ 360", "mL/min/100 g", "↑", "Filtración glomerular: el mayor flujo por masa."),
            ("Miocardio", "70-80", "mL/min/100 g", "=", "Extrae casi todo el oxígeno que recibe."),
            ("Hígado", "90-100", "mL/min/100 g", "=", "Mayor flujo total (≈ 1350 mL/min) por su gran masa."),
            ("Cerebro", "50", "mL/min/100 g", "=", "Constante gracias a la autorregulación."),
            ("Piel", "Variable", "según la temperatura", "↓", "Regula la pérdida de calor.")],
         veredicto=("El riñón recibe el mayor flujo por 100 g", "El hígado tiene el mayor flujo total, no por gramo.")))

# 26 · RM-CB-015 · GRÁFICA: potencial de acción y refractariedad
S("grafica", "RM-CB-015", "En el período refractario absoluto el miocito no puede responder a ningún estímulo",
  "Fisiología cardiaca · potencial de acción",
  ("Período refractario absoluto", ["Canales de sodio inactivados: no se genera otro potencial de acción, sea cual sea el estímulo.", "La meseta del miocardio lo prolonga y evita el tétanos."]),
  ("Pregunta de teoría", ["¿Qué es el período refractario absoluto?"]),
  ["Absoluto: fases 0, 1, 2 y parte de la 3. Relativo: final de la fase 3, con un estímulo supraumbral.",
   "En el ECG: QRS, segmento ST y primera parte de la onda T; la fase vulnerable es el pico de la T (R sobre T).",
   "La refractariedad larga permite que el corazón se relaje y se llene entre latidos."],
  GUYTON + "; " + BRAUN,
  op=("¿Correcta?", ["Sí: ningún estímulo genera otro potencial", "No: eso describe el período relativo", "No: eso es el período relativo con estímulo supraumbral", "No: en el absoluto no hay reacción posible", "No: el calcio causa la meseta, no la refractariedad"],
      {0: "La célula no responde a ningún estímulo", 1: "Responde a un estímulo menor", 2: "Responde a un estímulo mayor", 3: "Responde a un estímulo igual", 4: "Se debe al flujo de calcio"}),
  d=dict(rotulo="Potencial de acción del miocito y refractariedad", eje_x="Tiempo (ms)", eje_y="Voltaje (mV)",
         x=(0, 300, [(0, "0"), (100, "100"), (200, "200"), (300, "300")]), y=(-90, 30, [(-90, "-90"), (-60, "-60"), (-30, "-30"), (0, "0"), (30, "+30")]),
         series=[("Potencial de acción", [(0, -90), (5, 30), (10, 20), (50, 15), (180, 10), (220, -60), (260, -90), (300, -90)], "#0f766e")],
         zonas=[(0, 200, "", "#fee2e2"), (200, 260, "", "#fef3c7")],
         caso=(100, 15, "Sin reacción posible"),
         notas=[("Refractario absoluto", "Fases 0-2 y parte de la 3: ningún estímulo genera otro potencial.", True),
                ("Refractario relativo", "Final de la fase 3: solo un estímulo mayor.", False),
                ("Fase vulnerable", "Pico de la onda T: riesgo de R sobre T.", False)],
         veredicto=("Absoluto = la célula no puede responder a un estímulo", "Evita el tétanos del miocardio y protege el llenado ventricular.")))

# 27 · RM-END-001 · LECTURA con TC: feocromocitoma
S("lectura", "RM-END-001", "Crisis hipertensivas y masa suprarrenal izquierda: pedir metanefrinas",
  "Endocrinología · feocromocitoma",
  ("Feocromocitoma", ["Tumor de células cromafines productor de catecolaminas.", "Tríada: cefalea, sudoración y palpitaciones con hipertensión paroxística."]),
  ("Varón de 35 años", ["Crisis hipertensivas repetidas y dolor abdominal.", "La TC muestra una tumoración sobre el riñón izquierdo."]),
  ["Metanefrinas fraccionadas libres en plasma u orina de 24 h (sensibilidad > 95 %); luego TC o RM y, si es extraadrenal, MIBG o PET-DOTATATE.",
   "Antes de operar: bloqueo alfa (fenoxibenzamina o doxazosina) 10-14 días; después betabloqueo. Nunca betabloqueo solo.",
   "Se asocia a MEN 2, von Hippel-Lindau y neurofibromatosis 1: tamizaje genético."],
  "Endocrine Society, feocromocitoma y paraganglioma (Lenders 2014); " + HARRISON,
  op=("¿Examen?", ["No: es para el síndrome de Cushing", "Sí: confirma el exceso de catecolaminas", "No: estudia hipertensión renovascular", "No: estudia acromegalia", "No: es para el hiperaldosteronismo"]),
  d=dict(rotulo="Lee la tomografía y confirma con laboratorio", img_titulo="TC de abdomen con contraste (corte coronal)",
         img=PX("feo_tc.jpg", 380), pines=[(0.82, 0.30)],
         pasos=[("Masa sobre el polo superior del riñón", "Región suprarrenal: sospecha de tumor suprarrenal.", True),
                ("Clínica de catecolaminas", "Crisis hipertensivas, cefalea, sudoración, palpitaciones.", False),
                ("Laboratorio: metanefrinas", "Plasmáticas libres u orina de 24 h.", True),
                ("Preparación para operar", "Alfa-bloqueo 10-14 días y luego betabloqueo.", False)],
         img_pie="Imagen referencial de un tumor suprarrenal en la tomografía",
         veredicto=("Masa suprarrenal + crisis hipertensivas = metanefrinas", "El bloqueo alfa antes de operar evita una crisis.")))

# 28 · RM-CAR-001 · ÁRBOL: clasificación de antihipertensivos
S("arbol", "RM-CAR-001", "El atenolol es un antagonista del receptor beta",
  "Farmacología · antihipertensivos",
  ("Mecanismo del atenolol", ["Betabloqueante cardioselectivo (beta-1), hidrofílico y de eliminación renal.", "Baja frecuencia, contractilidad y liberación de renina."]),
  ("Pregunta de teoría", ["¿A qué grupo de antihipertensivos pertenece el atenolol?"]),
  ["Terminan en «-olol» los betabloqueantes; labetalol y carvedilol son mixtos alfa y beta; doxazosina es alfa; metildopa y clonidina, centrales.",
   "No son de primera línea en la HTA no complicada (IECA, ARA II, calcioantagonistas, tiazidas) pero sí tras infarto y en IC con FE reducida.",
   "El atenolol se ajusta en insuficiencia renal."],
  "ACC/AHA, hipertensión arterial (2025); ESC, hipertensión arterial (2024); Katzung Farmacología Básica y Clínica 15.ª ed.",
  op=("¿Grupo?", ["Sí: bloquea receptores beta-1", "No: eso es la doxazosina", "No: eso es la metildopa", "No: eso es el labetalol o carvedilol", "No: eso es la reserpina"],
      {0: "Antagonista del receptor beta", 1: "Antagonista del receptor alfa", 2: "Adrenérgico de acción central", 3: "Antagonista mixto alfa y beta", 4: "Bloqueante de neuronas adrenérgicas"}),
  arbol=Q("¿Sobre qué receptores actúa?", [
      L("Beta (-olol)", "BETABLOQUEANTES", ["Atenolol (beta-1), metoprolol, bisoprolol"], path=True),
      L("Alfa y beta", "MIXTOS", ["Labetalol, carvedilol"]),
      L("Alfa-1 o central", "OTROS", ["Doxazosina · metildopa, clonidina"])], path=True))

# 29 · RM-CAR-002 · RELOJ: respuesta al shock
S("reloj", "RM-CAR-002", "La taquicardia sinusal es el primer mecanismo compensador de la caída de la presión en el shock",
  "Fisiología · compensación hemodinámica",
  ("Mecanismos compensadores", ["Primero el reflejo barorreceptor y el simpático (segundos).", "Luego renina-angiotensina-aldosterona y vasopresina (minutos a horas)."]),
  ("Pregunta de teoría", ["¿Cuál es el primer mecanismo compensador?"]),
  ["La taquicardia es el signo más precoz de hemorragia; la hipotensión es tardía (clase III de ATLS: 30-40 % de volemia perdida).",
   "El factor natriurético atrial sube con la sobrecarga de volumen, no con la hipovolemia.",
   "Reposición: sangre y control del sangrado, no solo cristaloides."],
  ATLS + "; " + GUYTON,
  op=("¿Primero?", ["No: es una reacción tardía a la acidosis", "Sí: el barorreflejo activa el simpático en segundos", "No: sube con la sobrecarga de volumen", "No: es un mecanismo de minutos a horas", "No: es un mecanismo de horas a días"],
      {0: "Taquipnea", 1: "Taquicardia sinusal", 2: "Aumento del factor natriurético", 3: "Elevación de renina", 4: "Mayor retención de sodio"}),
  d=dict(rotulo="Cuándo actúa cada mecanismo", intro="De lo más rápido a lo más lento.",
         pasos=[("seg", "Barorreflejo y simpático", "Taquicardia, vasoconstricción", True), ("min", "Adrenalina y noradrenalina", "Más contractilidad", False),
                ("horas", "Renina-angiotensina-aldosterona", "Retiene sodio y agua", False), ("días", "Eritropoyetina y proteínas", "Reponen el volumen", False)],
         tag="ESTE CASO: PRIMERO",
         veredicto=("Taquicardia sinusal: el mecanismo más rápido", "La hipotensión aparece tarde.")))

# 30 · RM-CAR-003 · MATRIZ: tipos de shock
S("matriz", "RM-CAR-003", "Pulso filiforme, extremidades frías y llenado capilar lento: shock con gasto cardiaco bajo",
  "Shock · clasificación hemodinámica",
  ("Tipos de shock", ["Hipovolémico, cardiogénico y obstructivo: gasto cardiaco bajo, piel fría.", "Distributivo: gasto alto, resistencias bajas, piel caliente."]),
  ("Paciente en shock", ["PA media baja, pulso filiforme, extremidades frías.", "Llenado capilar lento."]),
  ["Bajo gasto: hemorragia, infarto, embolia pulmonar, taponamiento, neumotórax a tensión.",
   "Alto gasto: sepsis, anafilaxia, shock neurogénico.",
   "El catéter de Swan-Ganz o el POCUS distinguen: enclavamiento alto = cardiogénico; bajo = hipovolémico."],
  "Surviving Sepsis Campaign (2021); " + ATLS + "; " + HARRISON,
  op=("¿Tipo?", ["No: baja resistencia es shock distributivo", "No: el gasto alto da piel caliente", "Sí: piel fría con perfusión periférica pobre", "No: coexisten gasto bajo y resistencia alta, no baja", "No: normal no cuadra con la piel fría"],
      {0: "Resistencia vascular sistémica baja", 1: "Gasto cardiaco alto", 2: "Gasto cardiaco bajo", 3: "PVC baja con gasto alto", 4: "Resistencia normal y gasto alto"}),
  d=dict(rotulo="Gasto cardiaco y resistencias en el shock", eje_x="Gasto cardiaco", eje_y="Resistencia vascular",
         cols=["Gasto bajo", "Gasto alto"], rows=["Resistencia alta (piel fría)", "Resistencia baja (piel caliente)"], caso=(0, 0),
         cells=[[("Hipovolémico · cardiogénico · obstructivo", ["Pulso filiforme, frialdad", "Este caso"]), ("Poco frecuente", ["Hipertiroidismo, anemia grave"])],
                [("Raro", ["Shock séptico tardío"]), ("Séptico · anafiláctico · neurogénico", ["Pulso saltón, piel caliente"])]]))

# 31 · RM-NEF-001 · ÁRBOL: hiponatremia
S("arbol", "RM-NEF-001", "Anasarca con hiponatremia hipervolémica y sodio urinario menor de 20 mmol/L: insuficiencia cardiaca",
  "Hiponatremia · diagnóstico diferencial",
  ("Hiponatremia hipervolémica", ["Exceso de agua y de sodio total con volumen circulante efectivo bajo.", "El riñón retiene sodio y agua: el sodio urinario es bajo."]),
  ("Paciente de 55 años", ["Anasarca e hiponatremia hipervolémica.", "Sodio urinario < 20 mmol/L."]),
  ["Hipervolémica con Na urinario bajo: insuficiencia cardiaca, cirrosis, síndrome nefrótico. Tratar con restricción de agua y sodio y diuréticos de asa.",
   "Hipovolémica con Na urinario alto: pérdida renal de sal o diuréticos. Euvolémica con Na urinario alto: SIADH.",
   "Evitar la solución salina isotónica en exceso en el hipervolémico."],
  "Guía europea de hiponatremia (ESE/ESICM/ERA-EDTA, 2014); " + HARRISON,
  op=("¿Causa?", ["No: el sodio urinario sería alto", "No: es euvolémica, sin anasarca", "Sí: anasarca con sodio urinario bajo", "No: es euvolémica, con sodio urinario alto", "No: la falla renal aguda establecida tiene sodio urinario alto"],
      {0: "Nefropatía perdedora de sal", 1: "Hipotiroidismo", 2: "Insuficiencia cardiaca", 3: "SIADH", 4: "Falla renal aguda"}),
  arbol=Q("Hiponatremia: ¿cómo está el volumen?", [
      L("Hipovolémica", "PÉRDIDA DE SAL", ["Na urinario alto: renal", "Na urinario bajo: digestivo"]),
      L("Euvolémica", "SIADH · HIPOTIROIDISMO", ["Na urinario alto (> 40)"]),
      L("Hipervolémica con anasarca (este caso)", "IC · CIRROSIS · NEFRÓTICO", ["Na urinario < 20 mmol/L", "Restringir agua y sodio; diuréticos"], path=True)], path=True))

# 32 · RM-CAR-004 · CHECKLIST: insuficiencia cardiaca derecha
S("checklist", "RM-CAR-004", "Ingurgitación yugular, hepatomegalia y ascitis son los hallazgos más específicos de insuficiencia cardiaca derecha",
  "Insuficiencia cardiaca · falla derecha e izquierda",
  ("Falla derecha", ["Congestión venosa sistémica: yugulares, hígado, ascitis, edema.", "La izquierda causa congestión pulmonar: disnea y ortopnea."]),
  ("Pregunta de teoría", ["¿Qué hallazgos indican insuficiencia derecha?"]),
  ["Derecha: ingurgitación yugular, reflujo hepatoyugular, hepatomegalia dolorosa, ascitis, derrame pleural y edema.",
   "Izquierda: disnea de esfuerzo, ortopnea, disnea paroxística nocturna, tos y estertores.",
   "La causa más frecuente de falla derecha es la falla izquierda; luego cor pulmonale. FEr: IECA/ARNI, betabloqueante, ARM e iSGLT2."],
  "ESC, insuficiencia cardiaca (actualización 2023); " + BRAUN,
  op=("¿Más específicos?", ["Sí: congestión venosa sistémica", "No: son de la falla izquierda", "No: son signos de arritmia o isquemia", "No: ortopnea y hemoptisis son pulmonares", "No: nicturia y ictericia son inespecíficas"],
      {0: "Yugular, hepatomegalia y ascitis", 1: "DPN, palpitaciones y tos", 2: "Síncope, angina y arritmia", 3: "Edema, hemoptisis y ortopnea", 4: "Nicturia, ictericia y hepatomegalia"}),
  d=dict(rotulo="Signos de congestión venosa sistémica (falla derecha)", tag="MÁS ESPECÍFICO",
         pasos=[("Ingurgitación yugular", "Presión venosa central alta; se ve con el paciente a 45°.", True),
                ("Reflujo hepatoyugular", "Al presionar el hígado 10 s, la yugular sube y se mantiene.", False),
                ("Hepatomegalia dolorosa", "Hígado de estasis; en la falla crónica, ascitis.", False),
                ("Ascitis, derrame pleural y edema de miembros", "Por presión venosa sistémica elevada.", False)],
         no_titulo="Son de la falla izquierda", no_hacer=[("Disnea paroxística nocturna", "Congestión pulmonar"), ("Ortopnea y estertores", "Congestión pulmonar"), ("Tos y hemoptisis", "Congestión pulmonar")],
         veredicto=("Yugular, hepatomegalia y ascitis = falla derecha", "Más específicos que la disnea, que es de la falla izquierda.")))

# 33 · RM-CAR-005 · DECISIÓN: soplos diastólicos
S("decision", "RM-CAR-005", "El soplo de Austin Flint se ausculta en la insuficiencia aórtica",
  "Valvulopatías · soplos diastólicos",
  ("Soplo de Austin Flint", ["Retumbo mesodiastólico apical en la insuficiencia aórtica grave.", "El chorro regurgitante hace vibrar el velo mitral anterior."]),
  ("Pregunta de teoría", ["¿En qué valvulopatía se ausculta?"]),
  ["Insuficiencia aórtica: soplo diastólico aspirativo, presión de pulso amplia, Corrigan, Musset, Quincke y Duroziez.",
   "Estenosis mitral orgánica: chasquido de apertura y primer ruido intenso (el Austin Flint no los tiene).",
   "En la insuficiencia aórtica aguda (endocarditis, disección) hay edema pulmonar y shock: cirugía urgente."],
  "ACC/AHA, valvulopatías (2020); ESC/EACTS, valvulopatías (2021); " + BRAUN,
  op=("¿Valvulopatía?", ["No: tiene chasquido de apertura", "Sí: el chorro regurgitante golpea el velo mitral", "No: da soplo sistólico", "No: soplo sistólico eyectivo", "No: soplo diastólico tricuspídeo"]),
  d=dict(rotulo="Dos soplos que suenan en la diástole", eje_y="Valvulopatía", ancho_filas=210,
         cols=["Soplo", "Signos que la distinguen"],
         rows=[("Insuficiencia aórtica", "Reflujo hacia el ventrículo"), ("Estenosis mitral", "Obstrucción del llenado")],
         cells=[[("Diastólico aspirativo + Austin Flint", ["Borde esternal izquierdo y ápex"]), ("Pulso amplio y saltón", ["Corrigan, Musset, Quincke"])],
                [("Retumbo con chasquido de apertura", ["Ápex"]), ("Primer ruido intenso, FA", ["Aurícula izquierda grande"])]],
         caso=(0, 0), nota="El Austin Flint es un retumbo funcional: no hay chasquido de apertura."))

# 34 · RM-CAR-006 · LECTURA con eco: taponamiento
S("lectura", "RM-CAR-006", "El ventrículo derecho pequeño por colapso de las cavidades derechas sugiere taponamiento",
  "Pericardio · taponamiento cardiaco",
  ("Taponamiento cardiaco", ["La presión del pericardio supera la de las cavidades derechas y las colapsa.", "Importa la velocidad del líquido más que su cantidad."]),
  ("Pregunta de teoría", ["¿Qué hallazgo ecocardiográfico sugiere taponamiento?"]),
  ["Colapso diastólico de la aurícula derecha (el más sensible) y del ventrículo derecho (el más específico); vena cava inferior dilatada fija.",
   "Clínica: tríada de Beck (hipotensión, yugular y ruidos apagados) y pulso paradójico.",
   "Tratamiento: pericardiocentesis guiada por eco o ventana pericárdica; volumen mientras tanto."],
  "ESC, enfermedades del pericardio (2015); ASE, ecocardiografía en el derrame pericárdico (2013); " + BRAUN,
  op=("¿Hallazgo?", ["No: se ve en miocardiopatía", "No: el pericardio engrosado sugiere constricción", "No: es de la constricción", "Sí: colapso diastólico de cavidades derechas", "No: un derrame escaso no comprime"],
      {0: "Miocardio engrosado", 1: "Engrosamiento pericárdico", 2: "Calcificación pericárdica", 3: "Ventrículo derecho pequeño", 4: "Derrame pericárdico escaso"}),
  d=dict(rotulo="Lee la ecografía en este orden", img_titulo="Ecografía subcostal del corazón",
         img=PX("derrame_subcostal.jpg", 400, [("flecha", 0.44, 0.66, 0.72, 0.90, "líquido pericárdico")]), pines=[(0.56, 0.74), (0.40, 0.45)],
         pasos=[("Banda negra alrededor del corazón", "Líquido pericárdico (derrame).", True),
                ("Cavidades derechas colapsadas", "Ventrículo derecho pequeño en diástole: taponamiento.", True),
                ("Vena cava inferior dilatada", "Sin variación con la respiración.", False),
                ("Clínica", "Beck: hipotensión, yugular, ruidos apagados; pulso paradójico.", False)],
         img_pie="Imagen referencial de un derrame pericárdico en la ecografía subcostal",
         veredicto=("Colapso de cavidades derechas = taponamiento", "Drenar: pericardiocentesis o ventana pericárdica.")))

# 35 · RM-PED-001 · TARJETAS: IC del lactante
S("tarjetas", "RM-PED-001", "En el lactante, la insuficiencia cardiaca se sospecha por disnea y sudoración profusa al lactar",
  "Cardiología pediátrica · insuficiencia cardiaca",
  ("Insuficiencia cardiaca en el lactante", ["La alimentación es el esfuerzo que desencadena los síntomas.", "La causa más frecuente es una cardiopatía congénita con cortocircuito."]),
  ("Pregunta de teoría", ["¿Qué sospecha de IC en un lactante pequeño?"]),
  ["Tomas cortas y repetidas, mala ganancia de peso, taquipnea, taquicardia y hepatomegalia. Ortopnea y edema son raros.",
   "CIV, ductus y canal AV se hacen sintomáticos a las 4-8 semanas, cuando baja la resistencia pulmonar.",
   "En las 2 primeras semanas pensar en lesiones ductodependientes (coartación crítica, hipoplasia de cavidades izquierdas)."],
  NELSON + "; AHA/ACC, cardiopatías congénitas del adulto (2018).",
  op=("¿Sospecha?", ["Sí: síntoma típico al lactar", "No: hallazgos tardíos", "No: orientan a enfermedad pulmonar", "No: inespecíficos", "No: indican distrés respiratorio"],
      {0: "Disnea y sudoración al lactar", 1: "Hepatomegalia y distensión", 2: "Crepitantes y polipnea", 3: "Irritabilidad y cardiomegalia", 4: "Politirajes y aleteo nasal"}),
  d=dict(rotulo="Cómo se presenta la insuficiencia cardiaca en el lactante", ans=0,
         cards=[dict(titulo="Insuficiencia cardiaca (cardiopatía con cortocircuito)", datos=[("Al lactar", "Disnea y sudor", True), ("Tomas", "Cortas y repetidas", True), ("Peso", "Mala ganancia", True)], pie="Aparece a las 4-8 semanas, cuando baja la resistencia pulmonar."),
                dict(titulo="Enfermedad respiratoria (bronquiolitis)", datos=[("Al lactar", "Tos y rechazo", False), ("Cuadro", "Fiebre y coriza", False), ("Hígado", "Normal", False)], pie="Politirajes y sibilancias; no hay hepatomegalia."),
                dict(titulo="Signos tardíos de falla cardiaca", datos=[("Hígado", "Hepatomegalia", False), ("Edema", "Raro", False), ("Ortopnea", "Rara", False)], pie="Orientan, pero no son lo primero que se nota.")]))

# 36 · RM-CAR-007 · GRÁFICA: biomarcadores del infarto
S("grafica", "RM-CAR-007", "La troponina I es el mejor marcador cardiaco para confirmar un infarto de miocardio",
  "Cardiopatía isquémica · biomarcadores",
  ("Biomarcadores del infarto", ["Las troponinas son específicas del cardiomiocito: suben a las 2-4 h y duran 7-14 días.", "La CK-MB sirve para reinfarto; la mioglobina es precoz pero inespecífica."]),
  ("Varón de 62 años", ["Dolor torácico, diaforesis y supradesnivel del ST con T negativas de V1 a V4.", "¿Qué marcador confirma el infarto?"]),
  ["Troponina de alta sensibilidad en serie (0/1 h o 0/2 h): confirma o descarta el infarto.",
   "En el STEMI no se espera la troponina para reperfundir.",
   "Cuarta definición universal (2018): elevación o caída de troponina con isquemia clínica, ECG o imagen."],
  "ESC, síndromes coronarios agudos (2023); Cuarta Definición Universal del Infarto (2018); AHA/ACC, dolor torácico (2021)",
  op=("¿Mejor marcador?", ["Sí: específica del cardiomiocito", "No: obsoleta e inespecífica", "No: precoz pero inespecífica", "No: útil para reinfarto, menos específica", "No: mide insuficiencia cardiaca"],
      {0: "Troponina I", 1: "LDH", 2: "Mioglobina", 3: "CPK-MB", 4: "Péptido natriurético atrial"}),
  d=dict(rotulo="Cuándo sube cada marcador", eje_x="Horas desde el inicio del dolor", eje_y="Veces el límite normal",
         x=(0, 72, [(0, "0"), (12, "12"), (24, "24"), (48, "48"), (72, "72 h")]), y=(0, 20, [(0, "0"), (5, "5"), (10, "10"), (20, "20")]),
         series=[("Troponina", [(0, 0), (4, 3), (24, 18), (48, 12), (72, 8)], "#0f766e"), ("CK-MB", [(0, 0), (4, 2), (18, 9), (48, 1), (72, 0.5)], "#f59e0b"), ("Mioglobina", [(0, 0), (2, 5), (8, 2), (24, 0.5)], "#94a3b8")],
         caso=(24, 18, "Pico de troponina"),
         notas=[("Troponina: sube a las 2-4 h", "Dura 7-14 días: la más específica.", True), ("CK-MB: 3-6 h", "Normal a las 48-72 h: sirve para reinfarto.", False), ("Mioglobina: 1-2 h", "Precoz pero inespecífica.", False)],
         veredicto=("Troponina I = mejor marcador del infarto", "Se mide en serie con ensayos de alta sensibilidad.")))

# 37 · RM-CAR-008 · BALANZA: riesgo cardiovascular
S("balanza", "RM-CAR-008", "Hipertensión, diabetes y dislipidemia son los factores de riesgo coronario más importantes",
  "Prevención cardiovascular · factores de riesgo",
  ("Factores de riesgo coronario", ["No modificables: edad, sexo, antecedentes familiares.", "Modificables: dislipidemia, tabaquismo, hipertensión, diabetes, obesidad y sedentarismo."]),
  ("Pregunta de teoría", ["¿Cuáles son los más importantes?"]),
  ["Estudio INTERHEART: ApoB/ApoA1, tabaquismo, hipertensión, diabetes, obesidad abdominal y factores psicosociales explican más del 90 % del riesgo de infarto.",
   "Estimar el riesgo con SCORE2 o Framingham.",
   "Metas: LDL < 70 mg/dL en prevención secundaria (< 55 en riesgo muy alto) y PA < 130/80 mmHg."],
  "ESC/EAS, dislipidemias (2019, actualización focal 2025); ACC/AHA, hipertensión (2025); INTERHEART (Lancet 2004)",
  op=("¿Mayores?", ["Sí: la tríada de mayor peso", "No: la obesidad pesa menos que la dislipidemia", "No: el sedentarismo pesa menos", "No: el estrés pesa menos", "No: el estrés y el sedentarismo pesan menos"],
      {0: "HTA, diabetes y dislipidemia", 1: "HTA, diabetes y obesidad", 2: "HTA, tabaquismo y sedentarismo", 3: "Tabaquismo, diabetes y estrés", 4: "Estrés, tabaquismo y sedentarismo"}),
  d=dict(rotulo="Qué factores pesan más", gana="izq", pregunta="¿Cuáles son los más importantes?",
         izq=dict(titulo="Los de mayor peso", peso="MAYOR", items=["Hipertensión arterial", "Diabetes mellitus", "Dislipidemia (LDL, ApoB)", "Tabaquismo"]),
         der=dict(titulo="De menor peso individual", peso="MENOR", items=["Sedentarismo", "Estrés", "Obesidad (por sí sola)", "Alcohol"]),
         veredicto=("HTA + diabetes + dislipidemia", ["Es la tríada que más se usa para estimar el riesgo.", "Se suman tabaquismo, obesidad abdominal y factores psicosociales."])))

# 38 · RM-CAR-009 · LABORATORIO: enzimas
S("laboratorio", "RM-CAR-009", "La creatinfosfoquinasa se eleva en el infarto agudo de miocardio",
  "Cardiopatía isquémica · enzimas cardiacas",
  ("CK y CK-MB", ["La CK se libera del músculo estriado; la fracción MB es del cardiomiocito.", "Hoy el marcador recomendado es la troponina."]),
  ("Pregunta de teoría", ["¿Qué enzima sube en el infarto?"]),
  ["CK-MB: sube a las 3-6 h, pico a las 12-24 h y vuelve a lo normal en 48-72 h: útil para reinfarto.",
   "GGT: colestasis y alcohol. Fosfolipasa: pancreatitis. Fosforilasa y fosfoquinasa: metabolismo del glucógeno.",
   "Troponina de alta sensibilidad: primera elección."],
  "Cuarta Definición Universal del Infarto (2018); ESC, síndromes coronarios agudos (2023); " + HARRISON,
  op=("¿Sube en el IAM?", ["Sí: se libera del cardiomiocito", "No: participa en la pancreatitis y en la señalización", "No: del metabolismo del glucógeno", "No: marcador de colestasis y alcohol", "No: del metabolismo del glucógeno"],
      {0: "Creatinfosfoquinasa", 1: "Fosfolipasa", 2: "Fosfoquinasa", 3: "GGT", 4: "Fosforilasa"}),
  d=dict(rotulo="Qué enzimas suben y qué miden", valores=[
            ("Troponina I o T", "↑ 2-4 h", "< percentil 99", "↑", "La primera elección: específica del corazón."),
            ("CK total", "↑ 4-8 h", "40-200 U/L", "↑", "También sube en músculo esquelético."),
            ("CK-MB", "↑ 3-6 h", "< 5 % de la CK", "↑", "Vuelve a lo normal en 48-72 h: reinfarto."),
            ("GGT", "Normal", "< 50", "=", "No es cardiaca: colestasis y alcohol."),
            ("LDH", "↑ 24-48 h", "140-280", "↑", "Obsoleta e inespecífica.")],
         veredicto=("La CK (fracción MB) se eleva en el infarto", "Pero la troponina es el marcador de elección.")))
