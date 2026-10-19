"""Bloque 7 · parte F."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GUYTON = "Guyton y Hall. Tratado de fisiología médica 14.ª ed. (2021)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"

# GIN-175 · árbol
A("GIN-175", "gestante-10-semanas-confirmada-beta-hcg-innecesaria", "Exámenes en el embarazo ya confirmado",
  "OBSTETRICIA ENAM: EXÁMENES EN EL PRIMER TRIMESTRE", "OBSTETRICIA",
  ("Uso de la β-hCG", ["Sirve para diagnosticar embarazo temprano o seguir ectópico, aborto y mola",
   "Si el embarazo ya es evidente, no aporta"]),
  ("Gestante de 10 semanas con náuseas y vómitos", ["PA 100/60 · FC 100", "Útero de ~9 cm, anexos libres, sin dolor"]),
  Q("¿El embarazo ya está confirmado?", [
      Q("¿Sospecha de ectópico, aborto o mola?", [
          L("Sí", "β-hCG cuantitativa seriada", ["Con ecografía"]),
          L("No", "β-HCG INNECESARIA", ["Pedir hemograma, orina y ecografía TV", "Evaluar la hiperémesis"], path=True)],
        edge="Sí", path=True),
      L("No", "β-hCG", ["Confirma la gestación"])], path=True),
  ("Exámenes en este caso", [("Útil", True), ("No útil", False)], [
      ("Ecografía TV", ["Viabilidad, número de fetos, mola", "—"]),
      ("Hemograma y orina", ["Anemia, ITU, cetonuria", "—"]),
      ("β-hCG", ["—", "Ya hay embarazo evidente"])]),
  ["Los vómitos del primer trimestre son frecuentes; si son intensos: hiperémesis.",
   "Útero mayor que la edad gestacional con vómitos intensos: descartar mola.",
   "El ibuprofeno está contraindicado en el embarazo."],
  WILLIAMS)

# GIN-176 · termómetro
V("termometro", "GIN-176", "31-semanas-perdida-liquido-claro-rpm-corticoides-antibioticos", "Rotura prematura de membranas",
  "OBSTETRICIA ENAM: RPM PRETÉRMINO", "OBSTETRICIA",
  ("RPM pretérmino", ["La conducta depende de la edad gestacional",
   "Antes de las 34 semanas, sin infección: hospitalizar, corticoides y antibióticos"]),
  ("Gestante de 31 semanas", ["Pérdida de líquido claro por genitales", "Especuloscopía: líquido claro · cuello sin cambios · LCF 139"]),
  {"rotulo": "Edad gestacional",
   "niveles": [("< 24 sem", "Previable", ["Consejería individual"]),
               ("24-33 sem", "Pretérmino", ["31 SEMANAS", "Manejo expectante"]),
               ("34-36 sem", "Pretérmino tardío", ["Terminar la gestación"]),
               ("≥ 37 sem", "A término", ["Inducir el parto"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Hospitalizar + corticoides + antibióticos", ["Betametasona 12 mg IM × 2", "Ampicilina + eritromicina o azitromicina"], True),
             (2, "Sulfato de magnesio", ["Neuroprotección si < 32 sem y parto inminente"], False),
             (3, "Terminar si hay infección", ["Corioamnionitis o sufrimiento fetal"], False)]},
  ["Los antibióticos prolongan la latencia y reducen la infección neonatal.",
   "No hacer tactos vaginales: aumentan el riesgo de infección.",
   "Vigilar fiebre, taquicardia fetal y leucocitosis."],
  "ACOG – Practice Bulletin 217: Prelabor rupture of membranes (2020) · " + WILLIAMS)

# GIN-177 · árbol
A("GIN-177", "amenorrea-7-semanas-beta-hcg-ecografia", "Amenorrea secundaria",
  "GINECOLOGÍA ENAM: ESTUDIO DE LA AMENORREA SECUNDARIA", "GINECOLOGÍA",
  ("Amenorrea secundaria", ["Ausencia de regla ≥ 3 meses (o 3 ciclos) en quien ya menstruaba",
   "Primer paso siempre: descartar embarazo"]),
  ("Mujer de 21 años", ["7 semanas sin menstruar", "¿Qué va primero en el plan de trabajo?"]),
  Q("¿β-hCG positiva?", [
      L("Sí", "EMBARAZO: ECOGRAFÍA TV", ["β-hCG y ecografía transvaginal", "Ubicar la gestación"], path=True),
      Q("Medir TSH, prolactina y FSH", [
          L("Prolactina alta", "Hiperprolactinemia", ["Fármacos, adenoma"]),
          L("FSH alta", "Insuficiencia ovárica", ["< 40 años"]),
          L("FSH baja o normal", "Hipotalámica o SOP", ["Estrés, peso, ejercicio"])], edge="No")], path=True),
  ("Orden del estudio", [("Primero", True), ("Después", False)], [
      ("Prueba", ["β-hCG", "TSH, prolactina, FSH"]),
      ("Por qué", ["Causa más frecuente", "Si no hay embarazo"])]),
  ["El embarazo es la causa más frecuente de amenorrea secundaria.",
   "La prolactina se mide aunque no haya galactorrea.",
   "El test de progesterona evalúa estrógenos y vía de salida."],
  "ASRM – Current evaluation of amenorrhea (Fertil Steril 2024) · Speroff's Clinical Gynecologic Endocrinology 9.ª ed. (2019)")

# GIN-178 · matriz
V("matriz", "GIN-178", "bulto-vaginal-polaquiuria-cistocele-colporrafia-anterior", "Prolapso según el compartimento",
  "GINECOLOGÍA ENAM: CISTOCELE", "GINECOLOGÍA",
  ("Prolapso de órganos pélvicos", ["Se describe por compartimento: anterior, apical y posterior",
   "Anterior = vejiga (cistocele): síntomas urinarios"]),
  ("Mujer de 52 años", ["Polaquiuria y sensación de bulto vaginal hace 2 años", "Alteración del compartimento anterior"]),
  {"rotulo": "Compartimento y cirugía", "eje_x": "Rasgo", "eje_y": "Compartimento",
   "cols": ["Qué desciende", "Cirugía"], "rows": ["Anterior", "Apical", "Posterior"], "caso": (0, 1),
   "cells": [[("Vejiga (cistocele)", ["Polaquiuria, incontinencia"]), ("COLPORRAFIA ANTERIOR", ["Plastia de la fascia"])],
             [("Útero o cúpula", []), ("Histerectomía vaginal", ["Sacrocolpopexia"])],
             [("Recto (rectocele)", ["Dificultad para defecar"]), ("Colporrafia posterior", [])]]},
  ["Primera línea en prolapso leve: ejercicios de piso pélvico o pesario.",
   "La colposuspensión (Burch) trata la incontinencia de esfuerzo, no el cistocele.",
   "Clasificación POP-Q para medir el grado."],
  "ACOG/AUGS – Practice Bulletin 214: Pelvic organ prolapse (2019)")

# INF-086 · fases
V("fases", "INF-086", "meningitis-tuberculosa-esquema-hrze", "Tratamiento de la meningitis tuberculosa",
  "INFECTOLOGÍA ENAM: MENINGITIS TUBERCULOSA", "INFECTOLOGÍA",
  ("Meningitis tuberculosa", ["Forma grave de TB extrapulmonar",
   "Fase intensiva con 4 fármacos (HRZE) y fase de continuación prolongada"]),
  ("Pregunta de tratamiento", ["¿Esquema inicial de la meningitis tuberculosa?"]),
  {"rotulo": "Fases del tratamiento", "ans": 0,
   "fases": [("Intensiva", "2 meses", "HRZE", ["Isoniacida, rifampicina", "Pirazinamida, etambutol"]),
             ("Continuación", "7-10 meses", "HR", ["Isoniacida + rifampicina"]),
             ("Adyuvante", "Primeras semanas", "Corticoide", ["Dexametasona o prednisona"])],
   "curvas": [],
   "chips_titulo": "Esquema inicial · marcado el correcto",
   "chips": [("H + R + Z + E", True), ("S + H + R + Z", False), ("S + H + E + Z", False), ("H + R + E", False)]},
  ["El total del tratamiento es de 9-12 meses en la TB del sistema nervioso.",
   "Los corticoides reducen la mortalidad y las secuelas.",
   "La estreptomicina ya no forma parte del esquema de primera línea."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · OMS – Consolidated guidelines on tuberculosis, módulo 4 (2025)")

# PSI-035 · tarjetas
V("tarjetas", "PSI-035", "dislexia-dificultad-para-leer", "Trastornos del aprendizaje",
  "PSIQUIATRÍA ENAM: DISLEXIA", "PSIQUIATRÍA",
  ("Trastornos específicos del aprendizaje", ["Dificultad en una habilidad con inteligencia normal",
   "Dislexia: dificultad para leer (decodificar y comprender)"]),
  ("Pregunta de neurodesarrollo", ["¿Qué habilidad se afecta en la dislexia?"]),
  {"rotulo": "¿Qué habilidad falla?", "ans": 0, "cards": [
      {"titulo": "DISLEXIA", "datos": [
          ("Habilidad", "LECTURA", True), ("Clave", "Lee lento, invierte letras", False),
          ("Apoyo", "Enseñanza fonológica", False)],
       "pie": "El más frecuente"},
      {"titulo": "Discalculia", "datos": [
          ("Habilidad", "Matemáticas", False), ("Clave", "Cálculo, números", False),
          ("Apoyo", "Refuerzo concreto", False)],
       "pie": "Operaciones"},
      {"titulo": "Disgrafía", "datos": [
          ("Habilidad", "Escritura", False), ("Clave", "Letra, ortografía", False),
          ("Apoyo", "Terapia ocupacional", False)],
       "pie": "Expresión escrita"},
      {"titulo": "Trastorno del lenguaje", "datos": [
          ("Habilidad", "Hablar y comprender", False), ("Clave", "Frases pobres", False),
          ("Apoyo", "Terapia de lenguaje", False)],
       "pie": "Oral, no escrito"}]},
  ["Descartar primero problemas de visión y audición.",
   "No se debe a baja inteligencia ni a falta de enseñanza.",
   "El diagnóstico temprano mejora el pronóstico escolar."],
  "APA – DSM-5-TR (2022) · " + NELSON)

# NEU-052 · termómetro
V("termometro", "NEU-052", "tep-masivo-muerte-falla-ventricular-derecha", "¿De qué muere el paciente con TEP?",
  "NEUMOLOGÍA ENAM: TEP MASIVO", "NEUMOLOGÍA",
  ("TEP de alto riesgo", ["El trombo aumenta de golpe la poscarga del ventrículo derecho",
   "El VD falla, cae el gasto y se produce shock cardiogénico (obstructivo)"]),
  ("Pregunta de fisiopatología", ["¿Qué causa la muerte en el embolismo pulmonar?"]),
  {"rotulo": "Riesgo del TEP (ESC)",
   "niveles": [("Bajo", "Sin disfunción del VD", ["Anticoagular, alta precoz"]),
               ("Intermedio", "VD dilatado o troponina", ["Vigilar deterioro"]),
               ("Alto", "Shock o hipotensión", ["FALLA DEL VD → SHOCK", "Causa de muerte"])],
   "caso_nivel": 2, "ruta_titulo": "Qué ocurre", "paso_label": "PASO",
   "pasos": [(1, "Poscarga del VD sube de golpe", ["El VD se dilata e isquemiza"], True),
             (2, "Cae el llenado del VI", ["El septo se desplaza"], False),
             (3, "Shock y paro", ["Actividad eléctrica sin pulso"], False)]},
  ["La hipoxemia existe, pero no es lo que mata.",
   "En el TEP de alto riesgo se indica trombólisis sistémica.",
   "Evitar grandes volúmenes: empeoran la dilatación del VD."],
  "ESC – Guidelines for the diagnosis and management of acute pulmonary embolism (2019)")

# SP-127 · tarjetas
V("tarjetas", "SP-127", "glicemia-media-95-mediana-90-mitad-debajo", "Medidas de tendencia central",
  "SALUD PÚBLICA ENAM: MEDIA Y MEDIANA", "SALUD PÚBLICA",
  ("Media y mediana", ["La mediana divide los datos ordenados en dos mitades",
   "Si la media es mayor que la mediana, la distribución tiene cola a la derecha"]),
  ("Estudio de glicemia", ["Media 95 mg/dl", "Mediana 90 mg/dl"]),
  {"rotulo": "¿Qué dice cada medida?", "ans": 0, "cards": [
      {"titulo": "MEDIANA = 90", "datos": [
          ("Significa", "50 % tiene < 90", True), ("Extremos", "No la afectan", False),
          ("Uso", "Datos asimétricos", False)],
       "pie": "Percentil 50"},
      {"titulo": "Media = 95", "datos": [
          ("Significa", "Promedio", False), ("Extremos", "La desplazan", False),
          ("Uso", "Datos simétricos", False)],
       "pie": "Suma / número de datos"},
      {"titulo": "Moda", "datos": [
          ("Significa", "Valor más frecuente", False), ("Extremos", "No la afectan", False),
          ("Uso", "Datos categóricos", False)],
       "pie": "No se conoce aquí"},
      {"titulo": "Desviación estándar", "datos": [
          ("Significa", "Dispersión", False), ("Extremos", "La aumentan", False),
          ("Uso", "Con la media", False)],
       "pie": "No es media − mediana"}]},
  ["Media > mediana: asimetría positiva (algunos valores muy altos).",
   "En distribución normal, media = mediana = moda.",
   "La diferencia entre media y mediana no es la desviación estándar."],
  GORDIS)

# SP-128 · matriz
V("matriz", "SP-128", "300-muertes-covid-20000-habitantes-tasa-especifica-15", "Tasas con los datos del distrito",
  "SALUD PÚBLICA ENAM: TASA ESPECÍFICA DE MORTALIDAD", "SALUD PÚBLICA",
  ("Tasa específica de mortalidad", ["Muertes por una causa / población total × 1000",
   "No confundir con letalidad (muertes / enfermos)"]),
  ("Distrito de Lima, 2020", ["2000 muertes, 300 por COVID", "20 000 habitantes · 1000 contagiados"]),
  {"rotulo": "Cálculo de cada indicador", "eje_x": "Rasgo", "eje_y": "Indicador",
   "cols": ["Fórmula", "Resultado"], "rows": ["Mortalidad por COVID", "Letalidad", "Mortalidad general", "Mortalidad proporcional"], "caso": (0, 1),
   "cells": [[("300 / 20 000 × 1000", []), ("15 POR 1000", [])],
             [("300 / 1000 contagiados", []), ("30 %", [])],
             [("2000 / 20 000 × 1000", []), ("100 por 1000", [])],
             [("300 / 2000 muertes", []), ("15 %", [])]]},
  ["El denominador de una tasa es la población expuesta al riesgo.",
   "La letalidad mide la gravedad de la enfermedad.",
   "La mortalidad proporcional indica el peso de una causa entre las muertes."],
  GORDIS)

# SP-129 · radial
V("radial", "SP-129", "hombres-entre-mujeres-razon", "Razón, proporción y tasa",
  "SALUD PÚBLICA ENAM: RAZÓN", "SALUD PÚBLICA",
  ("Razón", ["Cociente entre dos cantidades distintas: el numerador no está en el denominador",
   "Ej.: n.º de hombres / n.º de mujeres"]),
  ("Pregunta de epidemiología", ["¿Cómo se llama n.º de hombres / n.º de mujeres?"]),
  {"rotulo": "Mapa del tema", "centro": "MEDIDAS", "centro_sub": "¿Qué se divide?", "ans": 0,
   "items": [("RAZÓN", ["a / b, grupos distintos", "Hombres / mujeres"]),
             ("Proporción", ["a / (a + b), de 0 a 1"]),
             ("Porcentaje", ["Proporción × 100"]),
             ("Tasa", ["Eventos / población en riesgo en un tiempo"]),
             ("Incidencia", ["Casos nuevos / población"])],
   "ruta": ["Hombres", "Mujeres", "Ninguno contiene al otro", "RAZÓN"]},
  ["Índice de masculinidad = hombres / mujeres × 100.",
   "La razón de mortalidad materna usa nacidos vivos, no mujeres.",
   "Toda tasa incluye el tiempo."],
  GORDIS)

# CB-062 · matriz
V("matriz", "CB-062", "hilio-pulmonar-bronquio-detras-derecho-debajo-izquierdo", "Relaciones del hilio pulmonar",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA DEL HILIO PULMONAR", "CIENCIAS BÁSICAS",
  ("Hilio pulmonar", ["Por él entran y salen bronquio, arteria y venas pulmonares",
   "Derecho: bronquio detrás de la arteria · Izquierdo: bronquio debajo de la arteria"]),
  ("Pregunta de anatomía", ["¿Dónde está el bronquio respecto a la arteria en cada hilio?"]),
  {"rotulo": "Posición en cada hilio", "eje_x": "Hilio", "eje_y": "Estructura",
   "cols": ["Derecho", "Izquierdo"], "rows": ["Bronquio", "Arteria pulmonar", "Venas pulmonares"], "caso": (0, 0),
   "cells": [[("DETRÁS DE LA ARTERIA", ["Bronquio eparterial alto"]), ("DEBAJO DE LA ARTERIA", ["La arteria lo cruza por arriba"])],
             [("Delante del bronquio", []), ("Lo más alto del hilio", [])],
             [("Delante y abajo", []), ("Delante y abajo", [])]]},
  ["Las venas pulmonares son las más anteriores e inferiores en ambos hilios.",
   "El bronquio derecho es más corto, ancho y vertical: allí van los cuerpos extraños.",
   "Útil para la cirugía y la lectura de la TC."],
  "Moore. Anatomía con orientación clínica 9.ª ed. (2022)")

# CB-063 · radial
V("radial", "CB-063", "tumor-lingula-pulmon-izquierdo", "Lóbulos pulmonares",
  "CIENCIAS BÁSICAS ENAM: LÍNGULA", "CIENCIAS BÁSICAS",
  ("Língula", ["Parte del lóbulo superior del pulmón izquierdo",
   "Es el equivalente del lóbulo medio del pulmón derecho"]),
  ("Trabajador en control de salud", ["Rx de tórax: tumoración en la língula"]),
  {"rotulo": "Mapa del tema", "centro": "PULMONES", "centro_sub": "¿Dónde está?", "ans": 0,
   "items": [("PULMÓN IZQUIERDO", ["Língula en el lóbulo superior", "2 lóbulos"]),
             ("Pulmón derecho", ["3 lóbulos, con lóbulo medio"]),
             ("Bronquio derecho", ["Corto, vertical"]),
             ("Carina", ["Bifurcación traqueal"]),
             ("Mediastino", ["Entre ambos pulmones"])],
   "ruta": ["Tumoración", "Língula", "Lóbulo superior izquierdo", "PULMÓN IZQUIERDO"]},
  ["La língula tiene dos segmentos: superior e inferior.",
   "Su lesión borra el borde izquierdo del corazón (signo de la silueta).",
   "Lóbulo medio: borra el borde derecho del corazón."],
  "Moore. Anatomía con orientación clínica 9.ª ed. (2022)")

# CB-064 · tarjetas
V("tarjetas", "CB-064", "co2-estimula-respiracion-quimiorreceptores-bulbo", "Control químico de la respiración",
  "CIENCIAS BÁSICAS ENAM: QUIMIORRECEPTORES CENTRALES", "CIENCIAS BÁSICAS",
  ("Quimiorreceptores", ["El CO₂ cruza la barrera hematoencefálica y baja el pH del LCR",
   "Los receptores centrales del bulbo detectan ese cambio: 70-80 % del estímulo"]),
  ("Pregunta de fisiología", ["¿Dónde están los receptores que responden al CO₂?"]),
  {"rotulo": "¿Qué receptor responde a qué?", "ans": 0, "cards": [
      {"titulo": "CENTRALES", "datos": [
          ("Sitio", "BULBO RAQUÍDEO", True), ("Estímulo", "CO₂ / H⁺ del LCR", True),
          ("Peso", "70-80 % del CO₂", False)],
       "pie": "Superficie ventral del bulbo"},
      {"titulo": "Periféricos", "datos": [
          ("Sitio", "Carotídeos, aórticos", False), ("Estímulo", "O₂ bajo (< 60)", False),
          ("Peso", "Hipoxemia", False)],
       "pie": "Vía IX y X pares"},
      {"titulo": "Mecanorreceptores", "datos": [
          ("Sitio", "Pulmón, vía aérea", False), ("Estímulo", "Distensión", False),
          ("Peso", "Hering-Breuer", False)],
       "pie": "Frenan la inspiración"},
      {"titulo": "Centro respiratorio", "datos": [
          ("Sitio", "Bulbo y protuberancia", False), ("Estímulo", "Integra señales", False),
          ("Peso", "Genera el ritmo", False)],
       "pie": "No es receptor"}]},
  ["En el EPOC con CO₂ crónico alto, el estímulo pasa a ser la hipoxemia.",
   "Por eso el oxígeno en exceso puede empeorar la hipercapnia.",
   "Los periféricos también responden al CO₂, pero en menor medida."],
  GUYTON)

# CB-065 · radial
V("radial", "CB-065", "aire-que-no-participa-hematosis-espacio-muerto", "Volúmenes y ventilación",
  "CIENCIAS BÁSICAS ENAM: ESPACIO MUERTO", "CIENCIAS BÁSICAS",
  ("Espacio muerto", ["Aire que llena la vía de conducción y no llega a intercambiar gases",
   "Anatómico: unos 150 ml en el adulto"]),
  ("Pregunta de fisiología", ["¿Cómo se llama el aire inspirado que no participa en la hematosis?"]),
  {"rotulo": "Mapa del tema", "centro": "AIRE INSPIRADO", "centro_sub": "¿Participa en la hematosis?", "ans": 0,
   "items": [("ESPACIO MUERTO", ["~150 ml, no intercambia", "Nariz a bronquiolos terminales"]),
             ("Ventilación alveolar", ["Sí intercambia gases"]),
             ("Volumen corriente", ["~500 ml por respiración"]),
             ("Volumen residual", ["Queda tras espirar"]),
             ("Capacidad vital", ["Máximo movilizable"])],
   "ruta": ["Aire que entra", "Se queda en la conducción", "No llega al alvéolo", "ESPACIO MUERTO"]},
  ["Ventilación alveolar = (VC − espacio muerto) × FR.",
   "Espacio muerto fisiológico = anatómico + alveolar (en el TEP aumenta).",
   "Respirar rápido y superficial ventila más espacio muerto."],
  GUYTON)

# CB-066 · puntaje
V("puntaje", "CB-066", "capacidad-vital-volumen-corriente-reservas", "Capacidad vital: cómo se suma",
  "CIENCIAS BÁSICAS ENAM: CAPACIDAD VITAL", "CIENCIAS BÁSICAS",
  ("Capacidades pulmonares", ["Una capacidad es la suma de dos o más volúmenes",
   "Capacidad vital = corriente + reserva inspiratoria + reserva espiratoria"]),
  ("Pregunta de fisiología", ["Capacidad vital = volumen corriente + ¿qué?"]),
  {"rotulo": "Volúmenes que suman la capacidad vital", "escala": "Volumen (adulto)", "total": 4600, "max": 5800,
   "total_label": "Capacidad vital (ml)",
   "interpreta": "CV = VC + VRI + VRE (sin el residual)",
   "items": [("Volumen corriente", "500", True), ("Volumen de reserva inspiratoria", "3000", True),
             ("Volumen de reserva espiratoria", "1100", True), ("Volumen residual", "1200", False)],
   "bandas": [("CV", "Capacidad vital", "VC + VRI + VRE: se mide con espirometría", True),
              ("CRF", "Residual funcional", "VRE + VR", False),
              ("CPT", "Pulmonar total", "CV + VR", False)]},
  ["El volumen residual no se puede espirar: se mide con pletismografía o dilución.",
   "Capacidad inspiratoria = VC + VRI.",
   "La capacidad vital baja en enfermedades restrictivas."],
  GUYTON)

# CB-067 · matriz
V("matriz", "CB-067", "difusion-oxigeno-menor-que-co2-solubilidad", "Difusión de O₂ y CO₂",
  "CIENCIAS BÁSICAS ENAM: DIFUSIÓN ALVEOLOCAPILAR", "CIENCIAS BÁSICAS",
  ("Coeficiente de difusión", ["Depende sobre todo de la solubilidad del gas",
   "El CO₂ es unas 20 veces más soluble: difunde unas 20 veces más rápido"]),
  ("Pregunta de fisiología", ["¿Cómo es la difusión del O₂ comparada con la del CO₂?"]),
  {"rotulo": "Comparación de los gases", "eje_x": "Gas", "eje_y": "Rasgo",
   "cols": ["O₂", "CO₂"], "rows": ["Solubilidad", "Coeficiente de difusión", "Gradiente alvéolo-capilar"], "caso": (1, 0),
   "cells": [[("Baja", []), ("~20 veces mayor", [])],
             [("MENOR", ["Por ser menos soluble"]), ("~20 veces mayor", [])],
             [("~60 mmHg", ["Necesita más gradiente"]), ("~5 mmHg", ["Le basta poco"])]]},
  ["Por eso la hipoxemia aparece antes que la hipercapnia en la fibrosis pulmonar.",
   "La unión a la hemoglobina no cambia la difusión por la membrana.",
   "La DLCO mide la capacidad de difusión con monóxido de carbono."],
  GUYTON)

# INF-087 · tarjetas
V("tarjetas", "INF-087", "quantiferon-infeccion-tb-sin-interferencia-bcg", "Pruebas en tuberculosis",
  "INFECTOLOGÍA ENAM: IGRA (QUANTIFERON)", "INFECTOLOGÍA",
  ("IGRA (Quantiferon)", ["Mide interferón gamma frente a antígenos propios de M. tuberculosis (ESAT-6, CFP-10)",
   "Esos antígenos no están en la BCG: no da falsos positivos en vacunados"]),
  ("Pregunta de infectología", ["¿Para qué sirve el Quantiferon?"]),
  {"rotulo": "¿Qué detecta cada prueba?", "ans": 0, "cards": [
      {"titulo": "QUANTIFERON (IGRA)", "datos": [
          ("Detecta", "Infección por TB", True), ("BCG", "NO LA AFECTA", True),
          ("Activa o latente", "No las distingue", False)],
       "pie": "Una sola muestra de sangre"},
      {"titulo": "PPD (tuberculina)", "datos": [
          ("Detecta", "Infección por TB", False), ("BCG", "Falsos positivos", False),
          ("Activa o latente", "No las distingue", False)],
       "pie": "Lectura a las 48-72 h"},
      {"titulo": "GeneXpert", "datos": [
          ("Detecta", "ADN del bacilo", False), ("BCG", "No aplica", False),
          ("Activa o latente", "Enfermedad activa", False)],
       "pie": "Y resistencia a rifampicina"},
      {"titulo": "Cultivo", "datos": [
          ("Detecta", "Bacilo vivo", False), ("BCG", "No aplica", False),
          ("Activa o latente", "Enfermedad activa", False)],
       "pie": "Sensibilidad a fármacos"}]},
  ["Ni IGRA ni PPD diagnostican TB activa.",
   "Útiles para decidir terapia preventiva en contactos.",
   "La resistencia se estudia con pruebas moleculares o cultivo."],
  "OMS – Consolidated guidelines on tuberculosis, módulo 3: diagnosis (2024) · CDC – Interferon gamma release assays (2024)")

# SP-130 · radial
V("radial", "SP-130", "covid-sale-a-trabajar-autonomia-no-maleficencia", "Conflicto entre principios éticos",
  "SALUD PÚBLICA ENAM: NO MALEFICENCIA", "SALUD PÚBLICA",
  ("Principios de la bioética", ["La autonomía tiene un límite: no dañar a otros",
   "Si mi decisión pone en riesgo a terceros, predomina la no maleficencia"]),
  ("Vendedor ambulante con COVID-19 sintomático", ["No avisa a sus vecinos y sale a trabajar", "Invoca su autonomía"]),
  {"rotulo": "Mapa del tema", "centro": "BIOÉTICA", "centro_sub": "Cuatro principios", "ans": 0,
   "items": [("NO MALEFICENCIA", ["No causar daño a otros", "Aislarse para no contagiar"]),
             ("Autonomía", ["Decidir sobre uno mismo"]),
             ("Beneficencia", ["Hacer el bien al paciente"]),
             ("Justicia", ["Reparto equitativo de recursos"]),
             ("Salud pública", ["El bien común limita lo individual"])],
   "ruta": ["Decide salir enfermo", "Contagia a terceros", "Autonomía con límite", "NO MALEFICENCIA"]},
  ["La no maleficencia se considera un deber de mínimos: obliga siempre.",
   "La cuarentena y el aislamiento tienen respaldo legal en emergencias sanitarias.",
   "La autonomía se refiere a decisiones que afectan al propio individuo."],
  "Beauchamp y Childress. Principios de ética biomédica 8.ª ed. (2019) · Ley N.° 26842 – Ley General de Salud")

# INF-088 · embudo
V("embudo", "INF-088", "ventilador-cabecera-45-grados-previene-neumonia", "Prevención de la neumonía asociada al ventilador",
  "INFECTOLOGÍA ENAM: NEUMONÍA ASOCIADA AL VENTILADOR", "INFECTOLOGÍA",
  ("Neumonía asociada a ventilación", ["Se produce por microaspiración de secreciones",
   "Elevar la cabecera 30-45° reduce la aspiración y la neumonía"]),
  ("Pregunta de cuidados intensivos", ["¿Qué medida ha reducido la neumonía por ventilador?"]),
  {"rotulo": "Embudo de medidas",
   "inicio": "Medidas propuestas",
   "candidatos": ["Cabecera elevada", "Cambiar circuito cada 24 h", "Descontaminación con norfloxacino", "Sucralfato"],
   "pasos": [("Cambiar circuitos de rutina no reduce infecciones", ["Cambiar circuito cada 24 h"]),
             ("Profilaxis de úlcera y antibióticos selectivos: sin beneficio claro o con resistencias", ["Descontaminación con norfloxacino", "Sucralfato"])],
   "final": ("CABECERA A 30-45°", ["Parte del paquete preventivo", "Con higiene oral y pausas de sedación"]),
   "nota": "Los circuitos solo se cambian si están visiblemente sucios o dañados."},
  ["Otras medidas: extubar lo antes posible, aspiración subglótica.",
   "Higiene de manos antes y después de manipular la vía aérea.",
   "Evitar la sobredistensión gástrica."],
  "SHEA/IDSA/APIC – Strategies to prevent ventilator-associated events (Infect Control Hosp Epidemiol 2022)")

# SP-131 · fases
V("fases", "SP-131", "febriles-aedes-aegypti-control-focos-extramural", "Qué hacer ante un brote de dengue",
  "SALUD PÚBLICA ENAM: CONTROL DE FOCOS DEL DENGUE", "SALUD PÚBLICA",
  ("Brote febril con Aedes aegypti", ["La prioridad del equipo extramural es cortar la transmisión",
   "Buscar casos, eliminar criaderos y controlar el vector alrededor"]),
  ("Centro de salud", ["Aumentan los pacientes febriles", "Salud ambiental reporta Aedes aegypti en la zona"]),
  {"rotulo": "Acciones del equipo", "ans": 1,
   "fases": [("Detectar", "Vigilancia", "Febriles en aumento", ["Notificar al nivel local"]),
             ("Controlar", "Extramural", "CONTACTOS Y FUENTES", ["Búsqueda de febriles", "Eliminar criaderos"]),
             ("Vector", "Intervención", "Control químico", ["Fumigación focal"]),
             ("Educar", "Comunidad", "Recipientes tapados", ["Participación vecinal"])],
   "curvas": [("Casos", ROSE, [0.2, 0.5, 0.8, 0.9, 0.6, 0.35, 0.2])],
   "chips_titulo": "Acción prioritaria · marcada la correcta",
   "chips": [("Control de contactos y fuentes", True), ("Notificación internacional", False), ("Vacunar", False), ("Antibióticos", False)]},
  ["El dengue no se trata con antibióticos.",
   "La notificación internacional es para eventos que lo requieran por el RSI.",
   "Fumigar sin eliminar criaderos no controla el brote."],
  "MINSA – NTS de vigilancia entomológica y control del Aedes aegypti · OPS – Gestión integrada de arbovirosis (2019)")

# NEF-073 · embudo
V("embudo", "NEF-073", "cirugia-pelvica-atrofia-testicular-arteria-testicular", "Testículo que se achica tras una cirugía",
  "UROLOGÍA ENAM: ATROFIA TESTICULAR POSQUIRÚRGICA", "UROLOGÍA",
  ("Irrigación del testículo", ["Arteria testicular (rama de la aorta) es la principal",
   "Si se liga o lesiona, el testículo se isquemiza y se atrofia"]),
  ("Varón de 33 años", ["Disminución del volumen testicular", "Cirugía por trauma pélvico hace un año"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Atrofia testicular tras cirugía",
   "candidatos": ["Ligadura de arteria testicular", "Sección del deferente", "Ablación del epidídimo", "Desgarro de arteria funicular"],
   "pasos": [("El volumen baja: el daño es de irrigación", ["Sección del deferente", "Ablación del epidídimo"]),
             ("La arteria funicular (deferencial) es colateral menor", ["Desgarro de arteria funicular"])],
   "final": ("LIGADURA DE LA ARTERIA TESTICULAR", ["Isquemia y atrofia del testículo", "Ecografía Doppler"]),
   "nota": "El deferente y el epidídimo afectan el transporte de espermatozoides, no el tamaño del testículo."},
  ["La arteria testicular nace de la aorta, bajo las renales.",
   "Circulación colateral: arterias deferencial y cremastérica.",
   "También puede atrofiarse tras hernioplastia o varicocelectomía."],
  "Moore. Anatomía con orientación clínica 9.ª ed. (2022) · Campbell-Walsh-Wein Urology 12.ª ed. (2020)")

# GIN-179 · puntaje
V("puntaje", "GIN-179", "preeclampsia-previa-lupus-aspirina-dosis-baja", "Prevención de la preeclampsia",
  "OBSTETRICIA ENAM: ASPIRINA PARA PREVENIR PREECLAMPSIA", "OBSTETRICIA",
  ("Profilaxis de la preeclampsia", ["Aspirina 100-150 mg por la noche desde las 12-16 semanas",
   "Indicada con 1 factor de alto riesgo o 2 moderados"]),
  ("Segundigesta de 12 semanas", ["Preeclampsia severa y parto pretérmino en la gestación anterior", "Lupus no activo · sobrepeso"]),
  {"rotulo": "Factores de riesgo del caso", "escala": "Factores de alto riesgo", "total": 2, "max": 6,
   "total_label": "Factores altos presentes",
   "interpreta": "Alto riesgo: aspirina a dosis baja",
   "items": [("Preeclampsia previa", "Alto", True), ("Enfermedad autoinmune (LES, SAF)", "Alto", True),
             ("Hipertensión crónica", "Alto", False), ("Diabetes pregestacional", "Alto", False),
             ("Enfermedad renal", "Alto", False), ("Embarazo múltiple", "Alto", False)],
   "bandas": [("0", "Riesgo habitual", "Control prenatal y calcio", False),
              ("≥ 1 alto", "Alto riesgo", "Aspirina 100-150 mg desde 12-16 sem", True)]},
  ["Se mantiene hasta las 36 semanas.",
   "El calcio también se indica si la dieta es pobre en calcio.",
   "Dieta baja en sal y vitamina D no previenen la preeclampsia."],
  "ACOG – Committee Opinion 743: Low-dose aspirin use during pregnancy (2018) · USPSTF (2021) · FIGO (2019)")

# TRA-039 · fases
V("fases", "TRA-039", "luxacion-posterior-cadera-reducida-72-h-necrosis-avascular", "Luxación de cadera: el tiempo importa",
  "TRAUMATOLOGÍA ENAM: LUXACIÓN POSTERIOR DE CADERA", "TRAUMATOLOGÍA",
  ("Luxación posterior de cadera", ["Emergencia: los vasos que nutren la cabeza femoral quedan estirados",
   "Cuanto más se tarda en reducir, más riesgo de necrosis avascular"]),
  ("Varón de 45 años tras accidente de tránsito", ["Dolor 9/10, impotencia funcional", "Luxación posterior reducida a las 72 horas"]),
  {"rotulo": "Horas hasta la reducción", "ans": 2,
   "fases": [("< 6 h", "Ideal", "Riesgo bajo", ["Reducción cerrada urgente"]),
             ("6-24 h", "Tardía", "Riesgo moderado", ["Aumenta la isquemia"]),
             ("> 24-72 h", "Muy tardía", "NECROSIS AVASCULAR", ["Colapso de la cabeza femoral", "Artrosis secundaria"])],
   "curvas": [("Riesgo de necrosis", ROSE, [0.1, 0.15, 0.3, 0.5, 0.7, 0.85, 0.95])],
   "chips_titulo": "Complicación ósea · marcada la correcta",
   "chips": [("Necrosis avascular", True), ("Anquilosis", False), ("Fractura de acetábulo", False), ("Lesión ciática", False)]},
  ["La lesión del nervio ciático es inmediata y neurológica, no ósea.",
   "La fractura del acetábulo se produce en el momento del trauma.",
   "Seguimiento con RM para detectar necrosis temprana."],
  "Rockwood and Green's Fractures in Adults 10.ª ed. (2024) · " + ATLS)

# SP-132 · puntaje
V("puntaje", "SP-132", "muerte-encefalica-retirar-soporte-ningun-valor-vulnerado", "Muerte encefálica y retiro del soporte",
  "SALUD PÚBLICA ENAM: MUERTE ENCEFÁLICA", "SALUD PÚBLICA",
  ("Muerte encefálica", ["Cese irreversible de todas las funciones del encéfalo, incluido el tronco",
   "Legalmente es la muerte: retirar el ventilador no vulnera ningún principio"]),
  ("Varón de 66 años con TEC grave en UCI", ["Diagnóstico establecido de muerte cerebral", "La junta médica decide retirar la ventilación"]),
  {"rotulo": "Criterios de muerte encefálica", "escala": "Criterios clínicos", "total": 5, "max": 5,
   "total_label": "Criterios cumplidos",
   "interpreta": "Muerte encefálica establecida",
   "items": [("Causa conocida e irreversible", "✓", True), ("Sin hipotermia, sedantes ni trastornos metabólicos", "✓", True),
             ("Coma arreactivo", "✓", True), ("Ausencia de reflejos del tronco", "✓", True),
             ("Test de apnea positivo", "✓", True)],
   "bandas": [("< 5", "No establecida", "Seguir soporte y reevaluar", False),
              ("5 de 5", "Persona fallecida", "Retirar soporte: no vulnera principios", True)]},
  ["No es eutanasia: el paciente ya está muerto.",
   "Es el momento de plantear la donación de órganos.",
   "Se informa a la familia con claridad y respeto."],
  "Ley N.° 28189 – Ley general de donación y trasplante de órganos y su reglamento · AAN – Brain death determination guideline (2023)")

# GIN-180 · árbol
A("GIN-180", "32-semanas-contracciones-regulares-1-cm-maduracion-tocolisis", "Amenaza de parto pretérmino",
  "OBSTETRICIA ENAM: AMENAZA DE PARTO PRETÉRMINO", "OBSTETRICIA",
  ("Parto pretérmino", ["Contracciones regulares con cambios cervicales antes de las 37 semanas",
   "Entre 24 y 34 semanas: corticoides + tocólisis para ganar 48 horas"]),
  ("Primigesta de 32 semanas", ["Dolor cólico y pérdida de moco", "Contracciones cada 4 min · cuello blando, 1 cm · membranas íntegras"]),
  Q("¿Contracciones regulares con cambios cervicales?", [
      Q("¿Entre 24 y 34 semanas, sin contraindicación?", [
          L("Sí", "MADURACIÓN PULMONAR + TOCÓLISIS", ["Betametasona 12 mg × 2", "Nifedipino; sulfato de Mg si < 32 sem"], path=True),
          L("No: ≥ 34 sem", "Dejar evolucionar", ["Atender el parto"])],
        edge="Sí", path=True),
      L("No", "Observación", ["Reposo y reevaluar"])], path=True),
  ("Contraindicaciones de la tocólisis", [("Contraindica", True), ("Por qué", False)], [
      ("Corioamnionitis", ["Sí", "Prolonga la infección"]),
      ("DPP o sangrado grave", ["Sí", "Riesgo materno"]),
      ("Sufrimiento fetal", ["Sí", "Hay que extraer"])]),
  ["La tocólisis sirve para completar el corticoide, no para llegar al término.",
   "No se usa reposo en casa con contracciones regulares y cambios cervicales.",
   "Buscar infección urinaria y vaginal como desencadenante."],
  "ACOG – Practice Bulletin 171: Management of preterm labor (2016) · OMS – Recomendaciones para mejorar los resultados del parto prematuro (2022)")

# GIN-181 · matriz
V("matriz", "GIN-181", "usuaria-diu-test-positivo-hilos-visibles-retirar", "Embarazo con DIU",
  "GINECOLOGÍA ENAM: EMBARAZO EN USUARIA DE DIU", "GINECOLOGÍA",
  ("Gestación con DIU colocado", ["Si los hilos se ven, se retira: baja el riesgo de aborto séptico y pretérmino",
   "Siempre descartar embarazo ectópico con ecografía"]),
  ("Usuaria de DIU", ["Retraso menstrual de 3 días, test de embarazo positivo", "Hilos del dispositivo visibles"]),
  {"rotulo": "Conducta según los hilos", "eje_x": "Rasgo", "eje_y": "Situación",
   "cols": ["Conducta", "Motivo"], "rows": ["Hilos visibles", "Hilos no visibles", "Ectópico en eco"], "caso": (0, 0),
   "cells": [[("RETIRAR EL DIU", ["Tracción suave"]), ("Menos aborto séptico", ["Y menos pretérmino"])],
             [("Ecografía", ["Ubicar el DIU"]), ("No retirar a ciegas", [])],
             [("Manejo del ectópico", []), ("Más frecuente con DIU", [])]]},
  ["Informar que retirarlo tiene un pequeño riesgo de aborto.",
   "Dejar el DIU aumenta el riesgo de aborto séptico y corioamnionitis.",
   "La ecografía confirma la ubicación de la gestación."],
  "OMS – Criterios médicos de elegibilidad para anticonceptivos 5.ª ed. (2015) · " + WILLIAMS)

# REU-054 · puntaje
V("puntaje", "REU-054", "placas-codos-artritis-interfalangicas-distales-psoriasica", "Artritis con placas en la piel",
  "REUMATOLOGÍA ENAM: ARTRITIS PSORIÁSICA", "REUMATOLOGÍA",
  ("Artritis psoriásica", ["Afecta interfalángicas distales, con FR negativo",
   "Criterios CASPAR: enfermedad articular inflamatoria + ≥ 3 puntos"]),
  ("Taxista de 42 años", ["Placas eritematodescamativas en codos · artritis de 6 meses", "FR y ANA negativos · VSG 50 · erosiones en IFD de 2.º y 3.er dedos"]),
  {"rotulo": "Criterios CASPAR en el caso", "escala": "CASPAR", "total": 3, "max": 6,
   "total_label": "Puntaje del caso",
   "interpreta": "Cumple criterios de artritis psoriásica",
   "items": [("Psoriasis actual", "2", True), ("Factor reumatoide negativo", "1", True),
             ("Distrofia ungueal", "1", False), ("Dactilitis", "1", False),
             ("Neoformación ósea yuxtaarticular (Rx)", "1", False)],
   "bandas": [("< 3", "No cumple", "Pensar en otra artritis", False),
              ("≥ 3", "Artritis psoriásica", "AINE, metotrexato o biológico", True)]},
  ["La artritis reumatoide respeta las interfalángicas distales.",
   "Reiter (artritis reactiva): uretritis, conjuntivitis y artritis tras infección.",
   "Signo radiológico típico: 'lápiz en copa'."],
  "CASPAR – Classification criteria for psoriatic arthritis (Arthritis Rheum 2006) · GRAPPA – Treatment recommendations (2021)")

# PSI-036 · tarjetas
V("tarjetas", "PSI-036", "tristeza-ideas-suicidas-alucinaciones-depresion-psicotica", "Depresión con alucinaciones",
  "PSIQUIATRÍA ENAM: DEPRESIÓN PSICÓTICA", "PSIQUIATRÍA",
  ("Depresión mayor con síntomas psicóticos", ["Episodio depresivo grave + alucinaciones o delirios",
   "Requiere antidepresivo + antipsicótico (o terapia electroconvulsiva)"]),
  ("Mujer de 50 años", ["Tristeza, desesperanza, poca concentración, ideas suicidas", "Escucha voces y ve personas que otros no ven"]),
  {"rotulo": "¿Qué trastorno afectivo es?", "ans": 0, "cards": [
      {"titulo": "DEPRESIÓN PSICÓTICA", "datos": [
          ("Ánimo", "Depresión grave", True), ("Psicosis", "Alucinaciones", True),
          ("Duración", "≥ 2 semanas", False), ("Riesgo", "Suicidio alto", True)],
       "pie": "Antidepresivo + antipsicótico"},
      {"titulo": "Depresión mayor", "datos": [
          ("Ánimo", "Depresión", False), ("Psicosis", "No", False),
          ("Duración", "≥ 2 semanas", False), ("Riesgo", "Suicidio", False)],
       "pie": "ISRS"},
      {"titulo": "Distimia", "datos": [
          ("Ánimo", "Tristeza leve", False), ("Psicosis", "No", False),
          ("Duración", "≥ 2 años", False), ("Riesgo", "Menor", False)],
       "pie": "Crónica y leve"},
      {"titulo": "Afectivo estacional", "datos": [
          ("Ánimo", "Depresión", False), ("Psicosis", "No", False),
          ("Duración", "Otoño-invierno", False), ("Riesgo", "Variable", False)],
       "pie": "Fototerapia"}]},
  ["Con ideas suicidas y psicosis: valorar hospitalización.",
   "La terapia electroconvulsiva es muy eficaz en la depresión psicótica.",
   "Diferenciar de esquizofrenia: aquí la psicosis aparece solo durante la depresión."],
  "APA – DSM-5-TR (2022) · NICE NG222: Depression in adults (2022)")

# END-051 · fases
V("fases", "END-051", "cetoacidosis-kussmaul-compensacion-renal-bicarbonato", "Compensación de la acidosis metabólica",
  "ENDOCRINOLOGÍA ENAM: CETOACIDOSIS DIABÉTICA", "ENDOCRINOLOGÍA",
  ("Compensación de la acidosis", ["Pulmón: hiperventila (Kussmaul) y baja la PaCO₂",
   "Riñón: deja de perder bicarbonato y excreta más ácido (amonio)"]),
  ("Varón diabético de 65 años", ["Trastorno de conciencia, respiración de Kussmaul", "Glucosa 400 · pH 7,23 · PaCO₂ 30 · HCO₃ 18 · cetonas (+)"]),
  {"rotulo": "Mecanismos de defensa del pH", "ans": 2,
   "fases": [("Tampones", "Segundos", "Bicarbonato, proteínas", ["Amortiguan el ácido"]),
             ("Pulmón", "Minutos-horas", "Hiperventilación", ["Kussmaul, PaCO₂ 30"]),
             ("Riñón", "Horas-días", "MENOS BICARBONATO EN ORINA", ["Reabsorbe HCO₃", "Más amonio urinario"])],
   "curvas": [("Compensación", SKY, [0.15, 0.35, 0.5, 0.6, 0.72, 0.85, 0.95])],
   "chips_titulo": "Cambio esperado · marcado el correcto",
   "chips": [("Menos excreción renal de HCO₃", True), ("Menos amonio urinario", False), ("Menos eliminación de CO₂", False), ("Amonio por el pulmón", False)]},
  ["El pulmón elimina más CO₂, no menos.",
   "El amonio se excreta por el riñón, nunca por el pulmón.",
   "Tratamiento: suero salino, insulina EV y potasio."],
  "ADA – Hyperglycemic crises in adults with diabetes: consensus report (2024) · " + GUYTON)

# PED-177 · árbol
A("PED-177", "nino-2-anos-invaginacion-liquido-libre-laparotomia", "Invaginación intestinal",
  "PEDIATRÍA ENAM: INVAGINACIÓN COMPLICADA", "PEDIATRÍA",
  ("Invaginación intestinal", ["Dolor cólico, vómitos y masa en 'salchicha'",
   "Si hay perforación, peritonitis o choque: cirugía, no enema"]),
  ("Niño de 2 años con 24 h de dolor cólico", ["Vómitos, masa alargada dolorosa, RHA metálicos", "TC: signo de la salchicha · 200 ml de líquido libre"]),
  Q("¿Signos de complicación?", [
      L("Sí: líquido libre, peritonitis", "LAPAROTOMÍA EXPLORATORIA", ["Reducción manual o resección", "Asa posiblemente necrótica"], path=True),
      L("No: estable, sin peritonitis", "Enema hidrostático o neumático", ["Bajo control ecográfico"])], path=True),
  ("Contraindicaciones del enema", [("Presente", True), ("Detalle", False)], [
      ("Perforación", ["Neumoperitoneo", "Riesgo de peritonitis"]),
      ("Peritonitis", ["Abdomen en tabla", "Asa necrótica"]),
      ("Choque", ["Inestable", "Cirugía directa"])]),
  ["Edad típica: 6 meses a 3 años.",
   "Heces en 'jalea de grosella' son un signo tardío.",
   "La ecografía es el estudio de elección para el diagnóstico."],
  "ESPR – Guidelines for imaging and reduction of intussusception (2016) · " + NELSON)

# PED-178 · termómetro
V("termometro", "PED-178", "nino-ceguera-nocturna-manchas-bitot-vitamina-a", "Xeroftalmía",
  "PEDIATRÍA ENAM: DÉFICIT DE VITAMINA A", "PEDIATRÍA",
  ("Deficiencia de vitamina A", ["Sin vitamina A no se forma rodopsina: ceguera nocturna",
   "Manchas de Bitot: placas espumosas en la conjuntiva"]),
  ("Niño de 2 años", ["Se choca con las cosas en la penumbra, fotofobia", "Xerosis conjuntival y manchas de Bitot"]),
  {"rotulo": "Etapa de la xeroftalmía (OMS)",
   "niveles": [("XN", "Ceguera nocturna", ["Primer síntoma"]),
               ("X1", "Xerosis y Bitot", ["MANCHAS DE BITOT", "Conjuntiva seca"]),
               ("X2", "Xerosis corneal", ["Córnea opaca"]),
               ("X3", "Queratomalacia", ["Úlcera, ceguera"])],
   "caso_nivel": 1, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Vitamina A 200 000 UI", ["Días 1, 2 y 14 (> 12 meses)"], True),
             (2, "Tratar la desnutrición", ["Dieta con hígado, huevo, verduras"], False),
             (3, "Suplementación preventiva", ["Cada 6 meses en zonas de riesgo"], False)]},
  ["El sarampión puede precipitar el déficit: dar vitamina A.",
   "Es la principal causa prevenible de ceguera infantil.",
   "El exceso de vitamina A también es tóxico."],
  "OMS – Xerophthalmia and night blindness for the assessment of clinical vitamin A deficiency (2014) · " + NELSON)

# NRL-047 · termómetro
V("termometro", "NRL-047", "acv-pa-208-bajar-menos-185-antes-trombolisis", "Presión arterial en el ACV agudo",
  "NEUROLOGÍA ENAM: ACV ISQUÉMICO CON HIPERTENSIÓN", "NEUROLOGÍA",
  ("PA y trombólisis", ["Solo se tromboliza si la PA es < 185/110",
   "Si está más alta, primero se baja con labetalol o nicardipino"]),
  ("Mujer de 75 años con FA anticoagulada", ["Afasia y hemiparesia derecha", "PA 208/108 · INR 1,6"]),
  {"rotulo": "Presión arterial",
   "niveles": [("< 185/110", "Apta", ["Trombólisis si < 4,5 h"]),
               ("> 185/110", "Bajar primero", ["PA 208/108", "Luego trombolizar"]),
               ("Sin trombólisis", "Tolerar", ["Tratar solo si > 220/120"])],
   "caso_nivel": 1, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Bajar PAS < 185 mmHg", ["Labetalol o nicardipino EV"], True),
             (2, "Trombólisis si es candidata", ["INR ≤ 1,7 lo permite"], False),
             (3, "Mantener < 180/105 por 24 h", ["Evita la hemorragia"], False)]},
  ["Trombolizar con PA alta aumenta la hemorragia cerebral.",
   "No dar vitamina K: el INR 1,6 no contraindica la trombólisis.",
   "Siempre TC antes para descartar sangrado."],
  "AHA/ASA – Guidelines for the early management of acute ischemic stroke (2019)")

# CAR-062 · fases
V("fases", "CAR-062", "deja-de-respirar-sin-pulso-compresiones-toracicas", "Secuencia de la reanimación",
  "CARDIOLOGÍA ENAM: PARO CARDIORRESPIRATORIO", "CARDIOLOGÍA",
  ("Reanimación cardiopulmonar", ["No responde, no respira y no tiene pulso = paro",
   "Lo primero son las compresiones de alta calidad (C-A-B)"]),
  ("Varón de 40 años en trauma shock", ["Deja de respirar y no responde", "Sin pulso carotídeo"]),
  {"rotulo": "Orden C-A-B", "ans": 0,
   "fases": [("C", "Inmediato", "COMPRESIONES", ["100-120/min, 5-6 cm", "Mínimas pausas"]),
             ("A", "Vía aérea", "Abrir vía aérea", ["Frente-mentón"]),
             ("B", "Ventilación", "30:2 o 1 cada 6 s", ["Con vía avanzada"]),
             ("D", "Desfibrilador", "Analizar ritmo", ["Descarga si FV o TV"])],
   "curvas": [],
   "chips_titulo": "Primer paso · marcado el correcto",
   "chips": [("Compresión torácica", True), ("Desfibrilar ya", False), ("Intubar", False), ("Llamar a cardiología", False)]},
  ["Si el paro es presenciado y el desfibrilador está a mano, se usa apenas llegue.",
   "Cambiar al compresor cada 2 minutos.",
   "La intubación no debe interrumpir las compresiones."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2025)")

# SP-133 · radial
V("radial", "SP-133", "covid-mascarilla-lavado-manos-medios-masivos", "Comunicación para la salud",
  "SALUD PÚBLICA ENAM: COMUNICACIÓN MASIVA EN LA PANDEMIA", "SALUD PÚBLICA",
  ("Comunicación en salud", ["Para cambiar conductas de toda la población a la vez se necesitan medios de gran alcance",
   "Televisión, radio, redes sociales"]),
  ("Inicio de la pandemia de COVID-19", ["Sin vacuna: mascarilla, lavado de manos y distanciamiento", "¿Cómo lograr que la población cumpla?"]),
  {"rotulo": "Mapa del tema", "centro": "EDUCACIÓN PARA LA SALUD", "centro_sub": "Según el alcance", "ans": 0,
   "items": [("MEDIOS MASIVOS", ["Llegan a millones al mismo tiempo", "Mensajes simples y repetidos"]),
             ("Educación a domicilio", ["Familia por familia, lento"]),
             ("Charlas laborales", ["Grupos pequeños"]),
             ("Teatro en parques", ["Aglomera a la gente"]),
             ("Consejería individual", ["Una persona"])],
   "ruta": ["Toda la población", "Sin vacuna", "Cambiar conductas rápido", "MEDIOS MASIVOS"]},
  ["En confinamiento, las actividades presenciales no eran posibles.",
   "Los mensajes deben ser claros, consistentes y basados en evidencia.",
   "Combatir la desinformación es parte de la estrategia."],
  "OMS – Risk communication and community engagement for COVID-19 (2020)")

# NEF-074 · embudo
V("embudo", "NEF-074", "tiazida-debilidad-hiporreflexia-hipokalemia-ecg", "Debilidad en un paciente con tiazida",
  "NEFROLOGÍA ENAM: HIPOPOTASEMIA POR TIAZIDAS", "NEFROLOGÍA",
  ("Hipopotasemia", ["Las tiazidas aumentan la pérdida renal de potasio",
   "Debilidad, hiporreflexia y riesgo de arritmias: ECG primero"]),
  ("Varón de 68 años con hidroclorotiazida", ["15 días de debilidad muscular, dos caídas", "Debilidad generalizada con hiporreflexia"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Debilidad generalizada en un anciano",
   "candidatos": ["Hipopotasemia", "ACV", "Neuropatía", "Crisis epiléptica"],
   "pasos": [("Debilidad difusa, sin foco ni convulsiones", ["ACV", "Crisis epiléptica"]),
             ("Toma tiazida, cuadro de 15 días con hiporreflexia", ["Neuropatía"])],
   "final": ("HIPOPOTASEMIA: ECG PRIMERO", ["Onda U, T aplanada, arritmias", "Luego potasio sérico y reposición"]),
   "nota": "El ECG es rápido y muestra si el potasio bajo ya pone en riesgo el corazón."},
  ["Tiazidas también causan hiponatremia e hiperuricemia.",
   "Reponer magnesio si está bajo: sin él no se corrige el potasio.",
   "TC, EMG y EEG no son el primer paso."],
  HARRISON + " · ESH – Guidelines for the management of arterial hypertension (2023)")

# TRA-040 · embudo
V("embudo", "TRA-040", "lactante-podalica-pliegues-asimetricos-galeazzi-ddc", "Cadera asimétrica en la lactante",
  "TRAUMATOLOGÍA ENAM: DISPLASIA DEL DESARROLLO DE LA CADERA", "TRAUMATOLOGÍA",
  ("Displasia del desarrollo de la cadera", ["Factores: mujer, podálica, primogénita, antecedente familiar",
   "Pasado el período neonatal: pliegues asimétricos, Galeazzi (+), abducción limitada"]),
  ("Lactante mujer de 11 meses", ["Nació por cesárea por podálica y macrosomía", "Pliegues glúteos asimétricos · Galeazzi (+)"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Asimetría de caderas en una lactante",
   "candidatos": ["Displasia de cadera", "Artritis de cadera", "Agenesia sacra", "Artrosis"],
   "pasos": [("Sin fiebre ni dolor agudo", ["Artritis de cadera"]),
             ("Galeazzi (+) con podálica y sexo femenino", ["Agenesia sacra", "Artrosis"])],
   "final": ("DISPLASIA DEL DESARROLLO DE CADERA", ["Rx de pelvis (> 4-6 meses)", "Reducción cerrada y yeso a esta edad"]),
   "nota": "Galeazzi: rodillas a distinta altura con caderas y rodillas flexionadas."},
  ["Ortolani y Barlow sirven en los primeros 3 meses.",
   "Ecografía hasta los 4-6 meses; luego Rx.",
   "Arnés de Pavlik solo en menores de 6 meses."],
  "AAP – Clinical practice guideline: developmental dysplasia of the hip (2016) · " + NELSON)
