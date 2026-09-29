"""Bloque 7 · parte N."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"

# INF-101 · radial
V("radial", "INF-101", "tuberculosis-meningea-corticoides-adyuvantes", "¿En qué TB se agregan corticoides?",
  "INFECTOLOGÍA ENAM: CORTICOIDES EN LA TUBERCULOSIS", "INFECTOLOGÍA",
  ("Corticoides en la tuberculosis", ["Reducen la inflamación que deja secuelas graves",
   "Indicados en la meningitis tuberculosa (y en la pericarditis)"]),
  ("Pregunta de tratamiento", ["¿En qué forma clínica se asocian corticoides?"]),
  {"rotulo": "Mapa del tema", "centro": "TB EXTRAPULMONAR", "centro_sub": "¿Corticoide?", "ans": 0,
   "items": [("MENINGITIS", ["Sí: dexametasona o prednisona", "Menos muerte y secuelas"]),
             ("Pericarditis", ["Puede considerarse"]),
             ("Pleural", ["No de rutina"]),
             ("Peritoneal", ["No de rutina"]),
             ("Osteoarticular", ["No"])],
   "ruta": ["TB del sistema nervioso", "Inflamación de meninges", "Riesgo de secuelas", "MENINGITIS"]},
  ["Dexametasona por 6-8 semanas, con retiro gradual.",
   "El esquema antituberculoso dura 9-12 meses en la meningitis.",
   "En la pulmonar no se usan corticoides de rutina."],
  "OMS – Consolidated guidelines on tuberculosis, módulo 4 (2025) · MINSA – NTS 200 (2023)")

# PED-217 · tarjetas
V("tarjetas", "PED-217", "lactante-jarabe-tos-somnolencia-depresion-respiratoria-codeina", "Jarabes para la tos en lactantes",
  "PEDIATRÍA ENAM: INTOXICACIÓN POR CODEÍNA", "PEDIATRÍA",
  ("Codeína en niños", ["Opioide antitusígeno; su metabolismo a morfina es impredecible",
   "En lactantes: somnolencia, mala succión y depresión respiratoria"]),
  ("Lactante de 2 meses con tos y congestión", ["La madre le dio un jarabe de farmacia", "Somnolencia, lactancia pobre y depresión respiratoria"]),
  {"rotulo": "¿Qué fármaco lo causó?", "ans": 0, "cards": [
      {"titulo": "CODEÍNA", "datos": [
          ("Tipo", "Opioide", True), ("Efecto", "Depresión respiratoria", True),
          ("En < 12 años", "Contraindicada", False)],
       "pie": "Antídoto: naloxona"},
      {"titulo": "Ambroxol", "datos": [
          ("Tipo", "Mucolítico", False), ("Efecto", "Poco relevante", False),
          ("En < 12 años", "No recomendado < 2 a", False)],
       "pie": "Sin sedación"},
      {"titulo": "Levocetirizina", "datos": [
          ("Tipo", "Antihistamínico", False), ("Efecto", "Sedación leve", False),
          ("En < 12 años", "Desde 6 meses", False)],
       "pie": "No causa apnea"},
      {"titulo": "Paracetamol / ibuprofeno", "datos": [
          ("Tipo", "Analgésico", False), ("Efecto", "Sin depresión", False),
          ("En < 12 años", "Seguros a dosis correctas", False)],
       "pie": "Para fiebre y dolor"}]},
  ["Los jarabes para la tos no se recomiendan en menores de 2 años.",
   "Tratar el resfrío con lavados nasales y lactancia.",
   "Depresión respiratoria por opioide: naloxona y soporte."],
  "FDA – Safety communication on codeine in children (2017) · AAP (2016)")

# GIN-225 · árbol
A("GIN-225", "parto-pretermino-previo-cervix-corto-progesterona", "Prevención del parto pretérmino",
  "OBSTETRICIA ENAM: CÉRVIX CORTO", "OBSTETRICIA",
  ("Prevenir un nuevo parto pretérmino", ["Parto pretérmino previo + cuello corto = alto riesgo",
   "La progesterona vaginal reduce el riesgo"]),
  ("Segundigesta de 35 años, 16 semanas", ["Parto prematuro previo a las 32 semanas", "Cérvix corto en la ecografía"]),
  Q("¿Parto pretérmino espontáneo previo?", [
      Q("¿Cérvix < 25 mm antes de las 24 semanas?", [
          L("Sí", "PROGESTERONA (± CERCLAJE)", ["Progesterona vaginal diaria", "Cerclaje si el cuello sigue acortándose"], path=True),
          L("No", "Progesterona y vigilancia", ["Cervicometría seriada"])],
        edge="Sí", path=True),
      L("No: cuello corto aislado", "Progesterona vaginal", ["Si < 20 mm"])], path=True),
  ("Opciones de prevención", [("Progesterona", True), ("Cerclaje", False)], [
      ("Para quién", ["Cuello corto ± parto previo", "Cuello < 25 mm con parto previo"]),
      ("Cuándo", ["16-36 semanas", "Antes de las 24 semanas"])]),
  ["El nifedipino no previene: solo es tocolítico en una amenaza activa.",
   "Los corticoides se dan cuando hay riesgo inminente, no a fecha fija.",
   "Buscar y tratar infecciones urinarias y vaginales."],
  "ACOG – Practice Bulletin 234: Prediction and prevention of spontaneous preterm birth (2021) · SMFM (2022)")

# SP-165 · radial
V("radial", "SP-165", "lactancia-exclusiva-disminuye-promocion-salud", "Niveles de intervención",
  "SALUD PÚBLICA ENAM: PROMOCIÓN DE LA LACTANCIA", "SALUD PÚBLICA",
  ("Promoción de la salud", ["Fomenta conductas saludables antes de que aparezca el daño",
   "La lactancia materna exclusiva se promueve con educación, apoyo y entornos amigables"]),
  ("Indicador en caída", ["La lactancia exclusiva baja 4 puntos por año desde hace 5 años"]),
  {"rotulo": "Mapa del tema", "centro": "INTERVENCIÓN", "centro_sub": "¿Qué nivel?", "ans": 0,
   "items": [("PROMOCIÓN", ["Conducta saludable", "Consejería, grupos de apoyo, lactarios"]),
             ("Prevención", ["Evitar una enfermedad concreta"]),
             ("Recuperación", ["Tratar al enfermo"]),
             ("Rehabilitación", ["Reducir secuelas"]),
             ("Abogacía", ["Normas: licencia, lactarios"])],
   "ruta": ["Menos lactancia exclusiva", "Es una conducta", "Fomentarla", "PROMOCIÓN"]},
  ["Lactancia exclusiva hasta los 6 meses y complementaria hasta los 2 años.",
   "Establecimientos amigos de la madre y el niño.",
   "Controlar la publicidad de sucedáneos."],
  "OMS/UNICEF – Global strategy for infant and young child feeding (2003) · MINSA – Guía de lactancia materna (2019)")

# SP-166 · tarjetas
V("tarjetas", "SP-166", "visita-domiciliaria-tb-mascarilla-ventilacion-educacion-salud", "Estrategias en la visita domiciliaria",
  "SALUD PÚBLICA ENAM: EDUCACIÓN PARA LA SALUD", "SALUD PÚBLICA",
  ("Educación para la salud", ["Enseñar para cambiar conductas que protegen la salud",
   "Mascarilla y ventilación cortan el contagio de la TB en casa"]),
  ("Visita a paciente de 30 años con TB BK (+)", ["Se le recuerda usar mascarilla", "Se explica a la familia la ventilación natural"]),
  {"rotulo": "¿Qué estrategia es?", "ans": 0, "cards": [
      {"titulo": "EDUCACIÓN PARA LA SALUD", "datos": [
          ("Qué hace", "Informa y orienta", True), ("En el caso", "Mascarilla, ventilar", True),
          ("A quién", "Paciente y familia", False)],
       "pie": "Cambia conductas"},
      {"titulo": "Salud ambiental", "datos": [
          ("Qué hace", "Modifica el entorno", False), ("En el caso", "Obras en la vivienda", False),
          ("A quién", "Comunidad", False)],
       "pie": "Agua, residuos, vivienda"},
      {"titulo": "Abogacía", "datos": [
          ("Qué hace", "Influye en políticas", False), ("En el caso", "—", False),
          ("A quién", "Autoridades", False)],
       "pie": "Normas y leyes"},
      {"titulo": "Equidad", "datos": [
          ("Qué hace", "Reduce brechas", False), ("En el caso", "—", False),
          ("A quién", "Grupos vulnerables", False)],
       "pie": "Es un principio"}]},
  ["La visita domiciliaria también sirve para estudiar contactos.",
   "Tras 2 semanas de tratamiento el contagio baja mucho.",
   "La ventilación cruzada reduce la concentración de bacilos."],
  "MINSA – NTS 200 (2023) · OMS – Health education: theoretical concepts (2012)")

# NEU-067 · fases
V("fases", "NEU-067", "empiema-drenado-pulmon-no-reexpande-decorticacion", "Evolución del derrame infectado",
  "NEUMOLOGÍA ENAM: PULMÓN ATRAPADO", "NEUMOLOGÍA",
  ("Empiema en fase organizada", ["Se forma una corteza fibrosa que atrapa el pulmón",
   "Si el pulmón no se expande tras el drenaje: decorticación"]),
  ("Varón de 60 años con neumonía y derrame", ["Se colocó tubo de drenaje", "El pulmón no reexpande · sin fístula bronquial"]),
  {"rotulo": "Fases del empiema", "ans": 2,
   "fases": [("Exudativa", "1.ª semana", "Líquido libre", ["Antibiótico ± drenaje"]),
             ("Fibrinopurulenta", "2.ª semana", "Tabiques", ["Tubo + fibrinolíticos o VATS"]),
             ("Organizada", "> 3 semanas", "DECORTICACIÓN", ["Corteza fibrosa", "Pulmón atrapado"])],
   "curvas": [("Fibrosis pleural", ROSE, [0.05, 0.15, 0.35, 0.55, 0.75, 0.9, 0.95])],
   "chips_titulo": "Tratamiento · marcado el correcto",
   "chips": [("Decorticación", True), ("Toracoplastía", False), ("Lobectomía", False), ("Neumonectomía", False)]},
  ["La decorticación se hace por VATS o toracotomía.",
   "No se reseca pulmón sano: se libera de la corteza.",
   "Toracoplastía: para cavidades crónicas con fístula."],
  "BTS – Guideline for pleural disease (Thorax 2023) · AATS – Management of empyema (2017)")

# SP-167 · fases
V("fases", "SP-167", "equipo-conflictos-lucha-control-tormenta", "Desarrollo de un equipo (Tuckman)",
  "SALUD PÚBLICA ENAM: ETAPAS DE UN EQUIPO", "SALUD PÚBLICA",
  ("Modelo de Tuckman", ["Los equipos pasan por etapas previsibles",
   "Tormenta: conflictos, resistencia y lucha por el control"]),
  ("Pregunta de gestión", ["¿Qué etapa se caracteriza por conflictos y lucha por el control?"]),
  {"rotulo": "Etapas del equipo", "ans": 1,
   "fases": [("Formación", "Forming", "Orientación", ["Dependen del líder"]),
             ("Tormenta", "Storming", "CONFLICTOS", ["Lucha por el control"]),
             ("Normalización", "Norming", "Acuerdos", ["Roles y cohesión"]),
             ("Desempeño", "Performing", "Alto rendimiento", ["Autonomía"]),
             ("Disolución", "Adjourning", "Cierre", ["Termina la tarea"])],
   "curvas": [("Conflicto", ROSE, [0.2, 0.7, 0.9, 0.5, 0.2, 0.1, 0.1]),
              ("Logro", SKY, [0.2, 0.25, 0.3, 0.55, 0.8, 0.95, 0.6])],
   "chips_titulo": "Etapa del caso · marcada la correcta",
   "chips": [("Tormenta (storming)", True), ("Formación", False), ("Normalización", False), ("Desempeño", False)]},
  ["El conflicto es normal; el líder debe mediar y aclarar roles.",
   "Saltarse la tormenta suele dejar conflictos ocultos.",
   "En normalización se fijan reglas y confianza."],
  "Tuckman BW (Psychol Bull 1965) · OPS – Liderazgo en salud (2017)")

# GIN-226 · puntaje
V("puntaje", "GIN-226", "aborto-septico-hipotension-lactato-6-cristaloides", "Shock séptico tras maniobras abortivas",
  "GINECOLOGÍA ENAM: ABORTO SÉPTICO", "GINECOLOGÍA",
  ("Shock séptico", ["Infección con hipotensión y lactato alto",
   "Primer paso: cristaloides 30 ml/kg en las primeras 3 horas + antibióticos"]),
  ("Mujer de 27 años, maniobras abortivas hace 24 h", ["PA 85/50 · FC 130 · FR 28 · T 39,5 · desorientada, piel marmórea", "Útero doloroso, flujo fétido · lactato 6 · pH 7,26"]),
  {"rotulo": "qSOFA en el caso", "escala": "qSOFA", "total": 3, "max": 3,
   "total_label": "Puntaje del caso",
   "interpreta": "Alto riesgo: shock séptico",
   "items": [("FR ≥ 22", "1", True), ("PAS ≤ 100 mmHg", "1", True), ("Alteración mental", "1", True)],
   "bandas": [("0-1", "Bajo riesgo", "Vigilar", False),
              ("≥ 2", "Sepsis probable", "Cristaloides 30 ml/kg + antibiótico", True)]},
  ["Vasopresor (noradrenalina) si la PAM sigue < 65 tras los líquidos.",
   "Antibióticos de amplio espectro en la primera hora.",
   "Evacuar el útero (control del foco) tras estabilizar."],
  "Surviving Sepsis Campaign – International guidelines (2021) · OMS – Abortion care guideline (2022)")

# CAR-071 · embudo
V("embudo", "CAR-071", "herida-precordial-beck-ecocardiograma-taponamiento", "Confirmar el taponamiento",
  "CARDIOLOGÍA ENAM: TAPONAMIENTO CARDIACO", "CARDIOLOGÍA",
  ("Taponamiento cardiaco", ["Tríada de Beck: hipotensión, ruidos apagados, yugulares ingurgitadas",
   "El ecocardiograma (o FAST pericárdico) confirma el líquido y el colapso de cavidades"]),
  ("Varón de 28 años asaltado hace 2 horas", ["Pequeña herida precordial · PA 90/60 · FC 110", "Ruidos apagados · yugulares ingurgitadas · MV presente"]),
  {"rotulo": "Embudo de exámenes",
   "inicio": "Sospecha de taponamiento",
   "candidatos": ["Ecocardiograma", "ECG", "Rx de tórax", "Troponina"],
   "pasos": [("ECG y troponina no ven el líquido", ["ECG", "Troponina"]),
             ("La Rx puede ser normal en el agudo", ["Rx de tórax"])],
   "final": ("ECOCARDIOGRAMA", ["Derrame + colapso de cavidades derechas", "Luego pericardiocentesis o toracotomía"]),
   "nota": "En trauma, el FAST pericárdico en la sala de emergencia es la forma más rápida."},
  ["El ECG puede mostrar bajo voltaje o alternancia eléctrica.",
   "No retrasar la descompresión en un paciente inestable.",
   "Pulso paradójico: caída de PAS > 10 mmHg en inspiración."],
  "ESC – Guidelines for pericardial diseases (2015) · " + ATLS)

# INF-102 · puntaje
V("puntaje", "INF-102", "diabetico-pierna-crepitacion-gas-tc-fascitis-necrosante", "Infección de piel con gas",
  "INFECTOLOGÍA ENAM: FASCITIS NECROSANTE", "INFECTOLOGÍA",
  ("Fascitis necrosante", ["Infección rápida de la fascia, con necrosis y toxicidad",
   "Crepitación o gas en la TC: emergencia quirúrgica"]),
  ("Varón de 59 años con DM2", ["24 h de aumento progresivo del volumen de la pierna", "Flogosis y crepitación · TC: gas desde la rodilla hasta la cadera"]),
  {"rotulo": "Signos de alarma", "escala": "Signos del caso", "total": 4, "max": 6,
   "total_label": "Signos presentes",
   "interpreta": "Fascitis necrosante: cirugía ya",
   "items": [("Crepitación a la palpación", "✓", True), ("Gas en la TC", "✓", True),
             ("Progresión rápida (horas)", "✓", True), ("Diabetes (riesgo)", "✓", True),
             ("Dolor desproporcionado", "?", False), ("Ampollas o necrosis", "?", False)],
   "bandas": [("Ninguno", "Celulitis", "Antibiótico", False),
              ("≥ 1", "Fascitis probable", "Desbridamiento urgente + antibióticos", True)]},
  ["Antibióticos: carbapenem o piperacilina-tazobactam + vancomicina + clindamicina.",
   "La clindamicina frena la producción de toxinas.",
   "Revisiones quirúrgicas cada 24-48 h."],
  "IDSA – Practice guidelines for skin and soft tissue infections (2014) · WSES/SIS-E (2018)")

# GIN-227 · puntaje
V("puntaje", "GIN-227", "mujer-67-cotest-negativos-descontinuar-tamizaje-cervical", "¿Cuándo dejar el tamizaje de cáncer de cuello?",
  "GINECOLOGÍA ENAM: TAMIZAJE DE CÁNCER DE CUELLO UTERINO", "GINECOLOGÍA",
  ("Fin del tamizaje cervical", ["Después de los 65 años, si los controles previos fueron negativos",
   "3 citologías o 2 co-test negativos en 10 años, el último en los últimos 5"]),
  ("Mujer de 67 años asintomática", ["Co-test negativos a los 60 y a los 65 años"]),
  {"rotulo": "Criterios para suspender", "escala": "Criterios", "total": 2, "max": 3,
   "total_label": "Criterios cumplidos",
   "interpreta": "Puede descontinuar el tamizaje",
   "items": [("Edad > 65 años", "✓", True), ("2 co-test negativos, último < 5 años", "✓", True),
             ("Sin NIC 2 o más en los últimos 25 años", "?", False)],
   "bandas": [("Falta alguno", "Continuar", "Hasta cumplir los criterios", False),
              ("Cumple", "Suspender", "Descontinuar el tamizaje", True)]},
  ["Si tuvo NIC 2+ debe seguir 25 años más.",
   "Tras histerectomía total por causa benigna tampoco se tamiza.",
   "No se hace colposcopía de rutina sin alteraciones."],
  "ACS – Cervical cancer screening guideline (2020) · USPSTF (2018)")

# GAS-072 · embudo
V("embudo", "GAS-072", "anciana-estrenida-dolor-fii-recurrente-tc-diverticulitis", "Dolor recurrente en fosa ilíaca izquierda",
  "GASTROENTEROLOGÍA ENAM: DIVERTICULITIS", "GASTROENTEROLOGÍA",
  ("Enfermedad diverticular", ["Divertículos del sigma por estreñimiento crónico",
   "Diverticulitis: dolor en FII, fiebre; se confirma con TC con contraste"]),
  ("Mujer de 70 años, estreñida crónica", ["Episodios de dolor en FII no ligados a la comida", "Hace 2 meses: dolor y náuseas que cedieron con dieta y antibióticos"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Dolor en FII recurrente en una anciana",
   "candidatos": ["Diverticulitis", "Cáncer de colon", "Colitis isquémica", "Intestino irritable"],
   "pasos": [("Episodio que cedió con antibióticos", ["Intestino irritable"]),
             ("Sin sangrado ni baja de peso descritos", ["Cáncer de colon", "Colitis isquémica"])],
   "final": ("DIVERTICULITIS (TC CON CONTRASTE)", ["Confirma y ve complicaciones", "Colonoscopía 6-8 semanas después"]),
   "nota": "La colonoscopía no se hace en la fase aguda por riesgo de perforación."},
  ["Complicaciones: absceso, fístula, perforación, estenosis.",
   "Leve sin complicaciones: dieta y a veces sin antibióticos.",
   "Fibra y líquidos previenen nuevos episodios."],
  "AGA – Clinical practice update on diverticulitis (2021) · ASCRS (2020)")

# REU-064 · puntaje
V("puntaje", "REU-064", "mujer-mialgias-generalizadas-fatiga-laboratorio-normal-fibromialgia", "Dolor generalizado con exámenes normales",
  "REUMATOLOGÍA ENAM: FIBROMIALGIA", "REUMATOLOGÍA",
  ("Fibromialgia", ["Dolor musculoesquelético difuso ≥ 3 meses, fatiga, sueño no reparador",
   "Examen y laboratorio normales"]),
  ("Mujer de 30 años con 2 años de síntomas", ["Fatiga y mialgias generalizadas que empeoran con el ejercicio", "Puntos dolorosos en cuello, hombros, lumbar y caderas · VSG, PCR, CPK y Rx normales"]),
  {"rotulo": "Datos a favor de fibromialgia", "escala": "Hallazgos del caso", "total": 5, "max": 5,
   "total_label": "Datos presentes",
   "interpreta": "Fibromialgia",
   "items": [("Dolor difuso > 3 meses", "✓", True), ("Fatiga", "✓", True),
             ("Puntos dolorosos en varias regiones", "✓", True), ("VSG, PCR y CPK normales", "✓", True),
             ("Rx sin lesiones", "✓", True)],
   "bandas": [("Con inflamación", "Otra causa", "Polimialgia, miositis", False),
              ("Sin inflamación", "Fibromialgia", "Ejercicio, educación, amitriptilina", True)]},
  ["Polimialgia reumática: > 50 años, VSG muy alta.",
   "Polimiositis: debilidad y CPK alta.",
   "El ejercicio aeróbico gradual es el tratamiento más eficaz."],
  "ACR – Fibromyalgia diagnostic criteria (2016 revision) · EULAR – Recommendations for fibromyalgia (2017)")

# NRL-057 · puntaje
V("puntaje", "NRL-057", "afasia-hemiparesia-1-hora-tc-normal-alteplasa", "ACV isquémico dentro de la ventana",
  "NEUROLOGÍA ENAM: TROMBÓLISIS EN EL ACV", "NEUROLOGÍA",
  ("Trombólisis en el ACV isquémico", ["Alteplasa EV dentro de las 4,5 horas",
   "Requiere TC sin sangrado y ausencia de contraindicaciones"]),
  ("Varón de 56 años", ["Hace 1 hora: afasia motora y hemiparesia derecha", "PA 120/70 · coagulación y glucosa normales · TC normal"]),
  {"rotulo": "Requisitos para trombolizar", "escala": "Requisitos", "total": 5, "max": 5,
   "total_label": "Requisitos cumplidos",
   "interpreta": "Candidato: alteplasa EV",
   "items": [("Inicio < 4,5 horas (1 h)", "✓", True), ("TC sin hemorragia", "✓", True),
             ("PA < 185/110", "✓", True), ("Coagulación normal", "✓", True), ("Glucosa > 50 mg/dl", "✓", True)],
   "bandas": [("Falta alguno", "No candidato", "Antiagregante y soporte", False),
              ("Todos", "Candidato", "Alteplasa 0,9 mg/kg EV", True)]},
  ["Aspirina y heparina no se dan en las primeras 24 h tras la alteplasa.",
   "Buscar oclusión de gran vaso para trombectomía.",
   "Tiempo es cerebro: puerta-aguja < 60 minutos."],
  "AHA/ASA – Guidelines for the early management of acute ischemic stroke (2019)")

# SP-168 · termómetro
V("termometro", "SP-168", "revision-sistematica-metaanalisis-integra-estudios", "Pirámide de la evidencia",
  "SALUD PÚBLICA ENAM: METAANÁLISIS", "SALUD PÚBLICA",
  ("Revisión sistemática con metaanálisis", ["Reúne y combina cuantitativamente varios estudios",
   "Más participantes: estimaciones más precisas y confiables"]),
  ("Pregunta de epidemiología", ["¿Por qué el metaanálisis da evidencia de alto nivel?"]),
  {"rotulo": "Nivel de evidencia",
   "niveles": [("Bajo", "Opinión, series", ["Casos aislados"]),
               ("Medio", "Observacionales", ["Casos y controles, cohortes"]),
               ("Alto", "Ensayos clínicos", ["Aleatorizados"]),
               ("Máximo", "RS con metaanálisis", ["INTEGRA VARIOS ESTUDIOS", "Mayor precisión"])],
   "caso_nivel": 3, "ruta_titulo": "Por qué vale más", "paso_label": "PASO",
   "pasos": [(1, "Integra resultados de varios estudios", ["Suma participantes y potencia"], True),
             (2, "Búsqueda sistemática", ["Reduce el sesgo de selección"], False),
             (3, "Evalúa heterogeneidad", ["Y calidad de cada estudio"], False)]},
  ["Su calidad depende de la calidad de los estudios incluidos.",
   "El sesgo de publicación se evalúa con el gráfico de embudo.",
   "No es más barato ni más rápido por definición."],
  "Cochrane Handbook for Systematic Reviews 6.4 (2023) · " + GORDIS)

# GIN-228 · radial
V("radial", "GIN-228", "gestante-tb-pleural-tratamiento-irregular-bajo-peso", "Tuberculosis mal tratada en el embarazo",
  "OBSTETRICIA ENAM: TUBERCULOSIS Y RESULTADO PERINATAL", "OBSTETRICIA",
  ("TB en la gestación", ["La enfermedad activa mal tratada consume a la madre",
   "Se asocia a bajo peso al nacer, prematuridad y muerte perinatal"]),
  ("Gestante de 8 semanas", ["TB pleural con tratamiento irregular"]),
  {"rotulo": "Mapa del tema", "centro": "TB MATERNA", "centro_sub": "Efectos perinatales", "ans": 0,
   "items": [("BAJO PESO AL NACER", ["Desnutrición e inflamación materna", "El más frecuente"]),
             ("Parto pretérmino", ["Riesgo aumentado"]),
             ("Muerte perinatal", ["Mayor en TB no tratada"]),
             ("TB congénita", ["Rara pero grave"]),
             ("Polihidramnios", ["No es típico"])],
   "ruta": ["TB activa", "Tratamiento irregular", "Madre consumida", "BAJO PESO AL NACER"]},
  ["Tratar bien la TB durante el embarazo mejora el pronóstico fetal.",
   "Supervisar la toma diaria (DOTS) y la adherencia.",
   "Evaluar al RN y dar terapia preventiva si está sano."],
  "OMS – Consolidated guidelines on tuberculosis, módulo 4 (2025) · " + WILLIAMS)

# REU-065 · tarjetas
V("tarjetas", "REU-065", "podagra-tras-comida-alcohol-artritis-gotosa", "Monoartritis del primer dedo",
  "REUMATOLOGÍA ENAM: ARTRITIS GOTOSA", "REUMATOLOGÍA",
  ("Gota aguda", ["Cristales de urato: dolor brusco e intenso, a menudo de noche",
   "Podagra (1.ª metatarsofalángica) tras comida abundante y alcohol"]),
  ("Varón de 50 años con sobrepeso", ["Dolor brusco en el pie izquierdo tras comida y alcohol", "1.ª metatarsofalángica y tobillo calientes e inflamados"]),
  {"rotulo": "¿Qué artritis es?", "ans": 0, "cards": [
      {"titulo": "GOTOSA", "datos": [
          ("Inicio", "Brusco, nocturno", True), ("Sitio", "1.er dedo (podagra)", True),
          ("Gatillo", "Alcohol, carnes", True), ("Líquido", "Cristales de urato", False)],
       "pie": "Colchicina, AINE, corticoide"},
      {"titulo": "Séptica", "datos": [
          ("Inicio", "Rápido, con fiebre", False), ("Sitio", "Rodilla", False),
          ("Gatillo", "Bacteriemia", False), ("Líquido", "Pus, Gram (+)", False)],
       "pie": "Drenaje + antibiótico"},
      {"titulo": "Reactiva", "datos": [
          ("Inicio", "Tras infección", False), ("Sitio", "Rodillas, tobillos", False),
          ("Gatillo", "Uretritis, diarrea", False), ("Líquido", "Estéril", False)],
       "pie": "Con conjuntivitis"},
      {"titulo": "Reumatoide", "datos": [
          ("Inicio", "Gradual", False), ("Sitio", "Manos, simétrica", False),
          ("Gatillo", "No", False), ("Líquido", "Inflamatorio", False)],
       "pie": "Poliartritis crónica"}]},
  ["No iniciar alopurinol durante la crisis si no lo tomaba.",
   "Confirmar con cristales en aguja, birrefringencia negativa.",
   "Metas: ácido úrico < 6 mg/dl a largo plazo."],
  "ACR – Guideline for the management of gout (2020) · EULAR (2016)")

# GIN-229 · embudo
V("embudo", "GIN-229", "amenorrea-sin-sangrado-tras-estrogenos-progestagenos-utero", "Amenorrea: prueba con estrógenos y progestágenos",
  "GINECOLOGÍA ENAM: AMENORREA DE ORIGEN UTERINO", "GINECOLOGÍA",
  ("Estudio de la amenorrea", ["Si no sangra ni con estrógeno + progestágeno, el endometrio no responde",
   "La falla está en el útero (sinequias: síndrome de Asherman)"]),
  ("Mujer de 19 años con 6 meses de amenorrea", ["Examen normal · test de embarazo negativo", "Tras estrógeno + progestágeno (AOC) no menstrúa"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Amenorrea sin embarazo",
   "candidatos": ["Útero", "Ovario", "Hipófisis", "Hipotálamo"],
   "pasos": [("Con hormonas externas un endometrio sano sangraría", ["Ovario", "Hipófisis", "Hipotálamo"])],
   "final": ("CAUSA UTERINA", ["Síndrome de Asherman u obstrucción", "Histeroscopía"]),
   "nota": "Si sangra con estrógeno + progestágeno, el problema es la falta de estrógenos (ovario o centro)."},
  ["Asherman: antecedente de legrados o infección endometrial.",
   "Primero se hace la prueba con progestágeno solo.",
   "Luego medir FSH para separar ovario de hipófisis."],
  "Speroff's Clinical Gynecologic Endocrinology 9.ª ed. (2019) · ASRM (2024)")

# END-061 · embudo
V("embudo", "END-061", "producto-adelgazar-taquicardia-temblor-sin-bocio-hormona-tiroidea", "Palpitaciones con un producto para adelgazar",
  "ENDOCRINOLOGÍA ENAM: TIROTOXICOSIS FACTICIA", "ENDOCRINOLOGÍA",
  ("Tirotoxicosis facticia", ["Ingesta de hormona tiroidea (a veces oculta en productos para bajar de peso)",
   "Tirotoxicosis sin bocio, con tiroglobulina baja"]),
  ("Mujer de 30 años", ["Toma un producto para adelgazar · bajó 8 kg en un mes", "FC 110 · T 38,2 · temblor fino, hiperreflexia · sin bocio · K 3"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hipermetabolismo por un producto",
   "candidatos": ["Hormona tiroidea", "Anfetaminas", "Diuréticos", "Antipsicóticos"],
   "pasos": [("Temblor fino, hiperreflexia, más deposiciones: tirotoxicosis", ["Diuréticos", "Antipsicóticos"]),
             ("Sin bocio, pérdida de peso con aumento del ritmo evacuatorio", ["Anfetaminas"])],
   "final": ("HORMONA TIROIDEA", ["TSH suprimida, T4 alta, tiroglobulina baja", "Suspender el producto y propranolol"]),
   "nota": "La tiroglobulina baja distingue la ingesta de hormona de la tiroiditis."},
  ["La captación de yodo está baja.",
   "Los productos 'naturales' para adelgazar pueden contener T3/T4.",
   "La hipokalemia puede venir de la diarrea."],
  "ATA – Guidelines for hyperthyroidism and other causes of thyrotoxicosis (2016)")

# GIN-230 · puntaje
V("puntaje", "GIN-230", "amenorrea-primaria-talla-baja-cuello-alado-turner", "Amenorrea primaria con talla baja",
  "GINECOLOGÍA ENAM: SÍNDROME DE TURNER", "GINECOLOGÍA",
  ("Síndrome de Turner (45,X)", ["Talla baja y falla ovárica (amenorrea primaria)",
   "Cuello alado, implantación baja del pelo, riñón en herradura, coartación"]),
  ("Mujer de 17 años que nunca menstruó", ["Riñón en herradura en la infancia · PA 150/95", "Talla 1,40 m · implantación baja del pelo, cuello corto y alado"]),
  {"rotulo": "Rasgos de Turner en el caso", "escala": "Rasgos del caso", "total": 6, "max": 7,
   "total_label": "Rasgos presentes",
   "interpreta": "Muy sugestivo: pedir cariotipo",
   "items": [("Amenorrea primaria", "✓", True), ("Talla baja (1,40 m)", "✓", True),
             ("Cuello alado", "✓", True), ("Implantación baja del cabello", "✓", True),
             ("Riñón en herradura", "✓", True), ("HTA (buscar coartación)", "✓", True),
             ("Tórax en escudo", "?", False)],
   "bandas": [("Pocos", "Dudoso", "Estudiar otras causas", False),
              ("Varios", "Turner probable", "Cariotipo, eco cardiaca y renal", True)]},
  ["FSH alta: hipogonadismo hipergonadotrópico.",
   "Tratamiento: hormona de crecimiento y estrógenos.",
   "Descartar coartación aórtica y válvula aórtica bicúspide."],
  "International Turner Syndrome Consensus Group – Clinical practice guidelines (2024)")

# INF-103 · árbol
A("INF-103", "hospitalizada-ceftriaxona-clindamicina-diarrea-clostridioides", "Diarrea tras antibióticos",
  "INFECTOLOGÍA ENAM: COLITIS POR CLOSTRIDIOIDES DIFFICILE", "INFECTOLOGÍA",
  ("Clostridioides difficile", ["Los antibióticos (clindamicina, cefalosporinas) alteran la flora",
   "Diarrea, dolor, a veces con moco y sangre, en hospitalizados"]),
  ("Mujer de 65 años con neumonía", ["Recibe ceftriaxona y clindamicina", "Al 5.º día: dolor abdominal y diarrea con moco y sangre"]),
  Q("¿Diarrea tras antibióticos u hospitalización?", [
      L("Sí", "C. DIFFICILE", ["Toxina o PCR en heces", "Vancomicina oral o fidaxomicina"], path=True),
      L("No", "Otras causas", ["Coprocultivo"])], path=True),
  ("Manejo de C. difficile", [("Medida", True), ("Detalle", False)], [
      ("Suspender", ["El antibiótico causal", "Si es posible"]),
      ("Tratar", ["Vancomicina oral 10 días", "Fidaxomicina alternativa"]),
      ("Aislar", ["Precauciones de contacto", "Lavado con agua y jabón"])]),
  ["El alcohol gel no mata las esporas: lavado de manos con agua y jabón.",
   "Colitis fulminante: vancomicina oral + metronidazol EV, cirugía si es necesario.",
   "Evitar antiperistálticos."],
  "IDSA/SHEA – Clinical practice guideline for C. difficile infection (2021)")

# PED-218 · radial
V("radial", "PED-218", "lactante-fiebre-piel-moteada-pulso-debil-shock-distributivo", "Tipos de shock en el lactante",
  "PEDIATRÍA ENAM: SHOCK SÉPTICO", "PEDIATRÍA",
  ("Shock séptico", ["Es distributivo: la infección altera el tono vascular",
   "En niños la PA se mantiene hasta tarde; mirar pulso, llenado capilar y piel"]),
  ("Lactante de 8 meses con 2 días de fiebre", ["FC 160 · FR 36 · irritable, rubicundo", "Pulso débil · llenado 3 s · piel moteada · PAS normal"]),
  {"rotulo": "Mapa del tema", "centro": "SHOCK", "centro_sub": "Tipo", "ans": 0,
   "items": [("DISTRIBUTIVO (SÉPTICO)", ["Fiebre + mala perfusión", "Infección"]),
             ("Hipovolémico", ["Diarrea, vómitos, hemorragia"]),
             ("Cardiogénico", ["Miocarditis, cardiopatía"]),
             ("Obstructivo", ["Neumotórax, taponamiento"]),
             ("Anafiláctico", ["Urticaria, estridor"])],
   "ruta": ["Fiebre", "Taquicardia y piel moteada", "PA aún normal", "SHOCK DISTRIBUTIVO"]},
  ["Hipotensión en el niño = shock descompensado (tardío).",
   "Bolos de cristaloide 10-20 ml/kg vigilando sobrecarga.",
   "Antibiótico en la primera hora."],
  "Surviving Sepsis Campaign – International guidelines for children (2020)")

# NEF-086 · matriz
V("matriz", "NEF-086", "diarrea-oliguria-fena-menor-1-cilindros-hialinos-prerrenal", "Tipo de lesión renal aguda",
  "NEFROLOGÍA ENAM: LESIÓN RENAL AGUDA PRERRENAL", "NEFROLOGÍA",
  ("LRA prerrenal", ["El riñón está sano pero recibe poco flujo (diarrea, falla cardiaca)",
   "FENa < 1 % y cilindros hialinos"]),
  ("Mujer de 72 años con cardiopatía coronaria", ["2 días de diarrea copiosa y oliguria · PA 90/60 · edema, crepitantes", "Creatinina 2,1 · FENa < 1 % · cilindros hialinos"]),
  {"rotulo": "Tipo y hallazgos", "eje_x": "Rasgo", "eje_y": "Tipo",
   "cols": ["FENa", "Sedimento"], "rows": ["Prerrenal", "Renal (NTA)", "Posrenal"], "caso": (0, 0),
   "cells": [[("< 1 %", ["Túbulo retiene sodio"]), ("CILINDROS HIALINOS", [])],
             [("> 2 %", []), ("Cilindros granulosos", ["Pardos, 'barro'"])],
             [("Variable", []), ("Normal o hematuria", ["Hidronefrosis en eco"])]]},
  ["Volumen efectivo bajo por diarrea y bajo gasto cardiaco.",
   "Reponer con cuidado: tiene signos de congestión.",
   "Si persiste, evoluciona a necrosis tubular."],
  "KDIGO – AKI guideline (2012) · " + HARRISON)

# GIN-231 · fases
V("fases", "GIN-231", "41-semanas-expectante-nst-liquido-amniotico", "Vigilancia fetal a las 41 semanas",
  "OBSTETRICIA ENAM: EMBARAZO EN VÍAS DE PROLONGACIÓN", "OBSTETRICIA",
  ("Monitoreo en el embarazo prolongado", ["Desde las 41 semanas, si se espera: NST + líquido amniótico",
   "Es el perfil biofísico modificado, dos veces por semana"]),
  ("Gestante de 41 semanas por eco del 1.er trimestre", ["Sin complicaciones", "Conducta expectante acordada, hospitalizada"]),
  {"rotulo": "Plan desde las 41 semanas", "ans": 1,
   "fases": [("41 sem", "Decidir", "Inducir o esperar", ["Acuerdo con la paciente"]),
             ("Si espera", "2 veces/semana", "NST + LÍQUIDO AMNIÓTICO", ["Perfil biofísico modificado"]),
             ("Alterado", "Oligohidramnios o NST no reactivo", "Terminar", ["Inducción o cesárea"]),
             ("42 sem", "Límite", "Terminar la gestación", ["Más riesgo de muerte fetal"])],
   "curvas": [("Riesgo fetal", ROSE, [0.1, 0.15, 0.25, 0.4, 0.6, 0.8, 0.95])],
   "chips_titulo": "Prueba de monitoreo · marcada la correcta",
   "chips": [("NST + líquido amniótico", True), ("Doppler umbilical", False), ("Doppler cerebral media", False), ("Arterias uterinas", False)]},
  ["El Doppler es para fetos con restricción del crecimiento, no para el postérmino normal.",
   "Oligohidramnios: bolsillo mayor < 2 cm.",
   "Ofrecer inducción a partir de las 41 semanas."],
  "ACOG – Practice Bulletin 146 (2014) · ACOG – Antepartum fetal surveillance (2021)")

# GIN-232 · embudo
V("embudo", "GIN-232", "fiebre-masa-vulvar-dolorosa-labio-mayor-absceso-bartolino", "Masa vulvar dolorosa con fiebre",
  "GINECOLOGÍA ENAM: ABSCESO DE BARTOLINO", "GINECOLOGÍA",
  ("Absceso de la glándula de Bartolino", ["La glándula está en el tercio inferior del labio mayor",
   "Obstrucción del conducto + infección: masa roja, dolorosa, que impide sentarse"]),
  ("Mujer de 25 años con fiebre", ["Dolor vulvar, no puede sentarse", "Masa ovoide de 4 cm, blanda, roja y muy dolorosa en el labio mayor derecho inferior"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Masa vulvar",
   "candidatos": ["Absceso de Bartolino", "Quiste de inclusión", "Quiste de Skene", "Acrocordón"],
   "pasos": [("Fiebre, eritema y dolor intenso: inflamación aguda", ["Quiste de inclusión", "Acrocordón"]),
             ("Tercio inferior del labio mayor, no periuretral", ["Quiste de Skene"])],
   "final": ("ABSCESO DE BARTOLINO", ["Incisión y drenaje con sonda de Word", "Marsupialización si recurre"]),
   "nota": "Mayor de 40 años con masa de Bartolino: biopsiar para descartar cáncer."},
  ["Antibiótico si hay celulitis o riesgo de ITS.",
   "Baños de asiento alivian el dolor.",
   "El drenaje simple sin sonda recurre con frecuencia."],
  "ACOG – Vulvar abscess and Bartholin gland (2023) · RCOG (2019)")

# END-062 · embudo
V("embudo", "END-062", "puerpera-hemorragia-agalactia-choque-refractario-hidrocortisona", "Choque refractario en la puérpera",
  "ENDOCRINOLOGÍA ENAM: SÍNDROME DE SHEEHAN", "ENDOCRINOLOGÍA",
  ("Síndrome de Sheehan", ["Necrosis hipofisaria por hemorragia obstétrica grave",
   "Agalactia, luego falla suprarrenal: choque que no responde a líquidos e hipoglucemia"]),
  ("Puérpera de 22 años, parto con gran hemorragia hace 1 semana", ["No puede lactar · cefalea intensa · desorientada", "PA 60/30 · FC 148 · glucosa 45 · no responde a expansores"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Choque en la puérpera",
   "candidatos": ["Crisis suprarrenal", "Shock hipovolémico", "Sepsis puerperal", "Hipotiroidismo"],
   "pasos": [("No responde a expansores plasmáticos", ["Shock hipovolémico"]),
             ("Agalactia + hipoglucemia, leucocitos normales", ["Sepsis puerperal", "Hipotiroidismo"])],
   "final": ("CRISIS SUPRARRENAL (SHEEHAN)", ["Hidrocortisona 100 mg EV primero", "Luego glucosa y demás hormonas"]),
   "nota": "Dar tiroxina antes que corticoide puede precipitar más la crisis suprarrenal."},
  ["La hipófisis crece en el embarazo y es sensible a la hipotensión.",
   "Confirmar luego con cortisol, ACTH, TSH, T4L, prolactina.",
   "Reemplazo de por vida de las hormonas deficientes."],
  "Endocrine Society – Hormonal replacement in hypopituitarism (2016) · " + HARRISON)

# OFT-051 · puntaje
V("puntaje", "OFT-051", "picadura-parpado-fiebre-proptosis-diplopia-celulitis-orbitaria", "Ojo hinchado con fiebre",
  "OFTALMOLOGÍA ENAM: CELULITIS ORBITARIA", "OFTALMOLOGÍA",
  ("Celulitis orbitaria", ["Infección detrás del septo orbitario",
   "Proptosis, dolor con los movimientos, diplopía o baja visión la separan de la preseptal"]),
  ("Varón de 15 años, picadura de insecto en el párpado", ["3 días de tumefacción, dolor y fiebre de 39 °C", "Edema palpebral intenso, exoftalmos unilateral, diplopía · leucocitos 15 000"]),
  {"rotulo": "Signos de compromiso orbitario", "escala": "Signos del caso", "total": 3, "max": 5,
   "total_label": "Signos presentes",
   "interpreta": "Celulitis orbitaria (postseptal)",
   "items": [("Proptosis (exoftalmos)", "✓", True), ("Diplopía u oftalmoplejía", "✓", True),
             ("Fiebre alta y leucocitosis", "✓", True), ("Baja de agudeza visual", "?", False),
             ("Dolor con los movimientos oculares", "?", False)],
   "bandas": [("0", "Preseptal", "Antibiótico oral", False),
              ("≥ 1", "Orbitaria", "Hospitalizar, TC y antibiótico EV", True)]},
  ["Complicaciones: absceso subperióstico, trombosis del seno cavernoso.",
   "Causa más frecuente: sinusitis etmoidal.",
   "Mucormicosis: diabético con escara negra."],
  "AAO – Orbital cellulitis (EyeWiki 2024) · " + NELSON)

# PED-219 · puntaje
V("puntaje", "PED-219", "neonato-10-dias-perdida-12-sodio-158-deshidratacion-hipernatremica", "Neonato que pierde mucho peso",
  "PEDIATRÍA ENAM: DESHIDRATACIÓN HIPERNATRÉMICA NEONATAL", "PEDIATRÍA",
  ("Deshidratación hipernatrémica neonatal", ["Lactancia insuficiente en los primeros días",
   "Pérdida > 10 % del peso, fiebre, irritabilidad, sodio alto y hemoconcentración"]),
  ("Neonato de 10 días", ["Fiebre, irritabilidad, ictericia", "Pierde 12 % del peso · Na 158 · Hto 65 %"]),
  {"rotulo": "Datos de deshidratación hipernatrémica", "escala": "Hallazgos del caso", "total": 4, "max": 5,
   "total_label": "Hallazgos presentes",
   "interpreta": "Deshidratación hipernatrémica",
   "items": [("Pérdida de peso > 10 %", "✓", True), ("Sodio > 150 mEq/L", "✓", True),
             ("Hemoconcentración (Hto 65 %)", "✓", True), ("Fiebre por deshidratación", "✓", True),
             ("Foco infeccioso claro", "—", False)],
   "bandas": [("< 7 %", "Fisiológica", "Apoyo a la lactancia", False),
              ("> 10 % + Na alto", "Hipernatrémica", "Rehidratar lento (48 h) y apoyar lactancia", True)]},
  ["La pérdida fisiológica es de hasta 7-10 % y se recupera a los 10-14 días.",
   "Bajar el sodio no más de 10-12 mEq/L al día.",
   "Evaluar la técnica de lactancia y la producción de leche."],
  "Academy of Breastfeeding Medicine – Protocol #3 (2017) · " + NELSON)

# SP-169 · tarjetas
V("tarjetas", "SP-169", "poblado-rural-disperso-cobertura-10-brigadas-itinerantes", "Llegar a la población dispersa",
  "SALUD PÚBLICA ENAM: BRIGADAS ITINERANTES", "SALUD PÚBLICA",
  ("Cobertura en zonas dispersas", ["Si la población no llega al establecimiento, el servicio va hacia ella",
   "Brigadas itinerantes de vacunación casa por casa"]),
  ("Poblado rural a 3 horas del centro de salud", ["Cobertura de vacunas < 10 % en menores de 5 años", "Las campañas dominicales no funcionaron"]),
  {"rotulo": "¿Qué estrategia funciona?", "ans": 0, "cards": [
      {"titulo": "BRIGADAS ITINERANTES", "datos": [
          ("Barrera", "Distancia: se elimina", True), ("Alcance", "Casa por casa", True),
          ("Costo", "Moderado", False)],
       "pie": "Oferta móvil"},
      {"titulo": "Sala de espera", "datos": [
          ("Barrera", "No la resuelve", False), ("Alcance", "Solo quien llega", False),
          ("Costo", "Bajo", False)],
       "pie": "Ya asistieron"},
      {"titulo": "Mensajes radiales", "datos": [
          ("Barrera", "No la resuelve", False), ("Alcance", "Informa", False),
          ("Costo", "Bajo", False)],
       "pie": "Motiva, no vacuna"},
      {"titulo": "Convocar al director", "datos": [
          ("Barrera", "No la resuelve", False), ("Alcance", "Gestión", False),
          ("Costo", "—", False)],
       "pie": "No es la solución directa"}]},
  ["Coordinar con agentes comunitarios para ubicar a los niños.",
   "Aprovechar la visita para CRED y suplementación.",
   "Registrar en el padrón nominal."],
  "MINSA – NTS 196: Esquema nacional de vacunación (2022) · OPS – Vacunación en poblaciones de difícil acceso (2019)")

# OFT-052 · puntaje
V("puntaje", "OFT-052", "miope-destellos-moscas-cortina-desprendimiento-retina", "Destellos y cortina en el campo visual",
  "OFTALMOLOGÍA ENAM: DESPRENDIMIENTO DE RETINA", "OFTALMOLOGÍA",
  ("Desprendimiento de retina", ["La retina se separa y deja de funcionar",
   "Fotopsias, moscas volantes y sombra en cortina; la miopía alta es factor de riesgo"]),
  ("Varón de 54 años con miopía severa", ["1 día de destellos, moscas volantes", "Sombra como cortina en el campo visual · menos agudeza"]),
  {"rotulo": "Síntomas de alarma", "escala": "Síntomas del caso", "total": 4, "max": 4,
   "total_label": "Síntomas presentes",
   "interpreta": "Desprendimiento de retina: urgencia",
   "items": [("Fotopsias (destellos)", "✓", True), ("Moscas volantes nuevas", "✓", True),
             ("Sombra en cortina", "✓", True), ("Miopía alta", "✓", True)],
   "bandas": [("Sin cortina", "Desprendimiento de vítreo", "Fondo de ojo en 24-48 h", False),
              ("Con cortina", "Desprendimiento de retina", "Oftalmología urgente: cirugía", True)]},
  ["Si la mácula aún está aplicada, operar pronto preserva la visión central.",
   "Glaucoma agudo: dolor, ojo rojo, presión alta.",
   "La catarata avanza lentamente, sin destellos."],
  "AAO – Preferred Practice Pattern: posterior vitreous detachment, retinal breaks and lattice (2019)")

# GIN-233 · termómetro
V("termometro", "GIN-233", "12-semanas-utero-borde-superior-pubis", "Altura del útero según las semanas",
  "OBSTETRICIA ENAM: ALTURA UTERINA A LAS 12 SEMANAS", "OBSTETRICIA",
  ("Crecimiento del útero", ["Antes de las 12 semanas está en la pelvis",
   "A las 12 semanas se palpa en el borde superior del pubis"]),
  ("Gestante normal con feto único", ["12 semanas", "¿Dónde se palpa el útero?"]),
  {"rotulo": "Semanas de gestación",
   "niveles": [("8 sem", "Intrapélvico", ["No se palpa por abdomen"]),
               ("12 sem", "Borde del pubis", ["BORDE SUPERIOR DEL PUBIS"]),
               ("16 sem", "Entre pubis y ombligo", ["A mitad de camino"]),
               ("20 sem", "Ombligo", ["Luego ~1 cm por semana"])],
   "caso_nivel": 1, "ruta_titulo": "Referencias", "paso_label": "PASO",
   "pasos": [(1, "12 semanas: sobre el pubis", ["Palpación abdominal"], True),
             (2, "20 semanas: ombligo", ["Altura uterina ≈ semanas"], False),
             (3, "36 semanas: apéndice xifoides", ["Luego desciende"], False)]},
  ["Útero mayor que la edad: gemelar, mola, miomas o error de fecha.",
   "Útero menor: error de fecha o aborto retenido.",
   "Desde la semana 20 se mide con cinta métrica."],
  WILLIAMS)

# INF-104 · termómetro
V("termometro", "INF-104", "nino-vih-tuberculina-4-mm-negativa", "Lectura del PPD según el paciente",
  "INFECTOLOGÍA ENAM: PRUEBA DE TUBERCULINA EN VIH", "INFECTOLOGÍA",
  ("Punto de corte del PPD", ["Depende del riesgo del paciente",
   "En niños con VIH, ≥ 5 mm es positivo; 4 mm es negativo"]),
  ("Preescolar de 5 años con VIH", ["Se le hace la prueba de tuberculina", "¿Qué lectura sería negativa?"]),
  {"rotulo": "Induración (mm)",
   "niveles": [("< 5", "Negativa en VIH", ["4 MM: NEGATIVA"]),
               ("≥ 5", "Positiva en VIH", ["Y contactos, inmunodeprimidos"]),
               ("≥ 10", "Positiva en otros", ["Riesgo intermedio"]),
               ("≥ 15", "Positiva en todos", ["Sin factores de riesgo"])],
   "caso_nivel": 0, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "PPD negativo no descarta TB", ["La inmunodepresión da falsos negativos"], True),
             (2, "Evaluar clínica y Rx", ["Buscar TB activa"], False),
             (3, "Terapia preventiva según norma", ["En VIH aunque el PPD sea negativo"], False)]},
  ["Se lee a las 48-72 h: se mide la induración, no el eritema.",
   "El IGRA es alternativa en vacunados con BCG.",
   "MINSA indica terapia preventiva en niños con VIH sin TB activa."],
  "MINSA – NTS 200 (2023) · CDC – Tuberculin skin testing (2024)")
