# -*- coding: utf-8 -*-
"""Residentado Médico · lote 7 · paquete 18 · módulo p73 · 17 flujogramas de salud pública y bioestadística (RM-SP-061 a 077)."""
from c_rm import S, P, PX, B, Q, L, TR

GOR = "Gordis, Epidemiología 6.ª ed. (2019)"
SZK = "Szklo y Nieto, Epidemiology: Beyond the Basics 3.ª ed. (2014)"
LAST = "Last, A Dictionary of Epidemiology 6.ª ed. (2014)"
ALT = "Altman y Bland, BMJ 1995;310:298"

# 061 · ANTES Y DESPUÉS
S("antes_despues", "RM-SP-061", "En una distribución asimétrica se describe con mediana y rango intercuartilar",
  "Bioestadística · medidas de resumen",
  ("Distribución asimétrica", ["Pocos valores extremos arrastran la media hacia la cola.", "Se eligen medidas resistentes a esos extremos."]),
  ("Pregunta de elección", ["¿Qué medidas de tendencia central y de dispersión se usan en una distribución asimétrica?"]),
  ["Simétrica y normal: media y desviación estándar; casi 95 % de los valores cae a ±2 desviaciones.",
   "Asimétrica (estancia hospitalaria, ingresos, carga viral): la media y la desviación estándar se distorsionan por los extremos.",
   "Se reporta mediana (Q1-Q3): el rango intercuartilar abarca el 50 % central, entre los percentiles 25 y 75.",
   "Pista: si la media supera mucho a la mediana, la cola derecha es larga; luego se usan pruebas no paramétricas. Mezclar medidas no es coherente."],
  "Altman y Bland, Statistics notes: the normal distribution (BMJ 1995;310:298); " + GOR + ".",
  op=("¿Medidas de elección?", ["No: ambas se distorsionan con los extremos", "Sí: ambas son resistentes a los extremos", "No: mezcla una medida resistente con una sensible", "No: mezcla una medida sensible con una resistente", "No: son medidas burdas; el rango usa solo dos valores"],
      {0: "Media y desviación estándar", 1: "Mediana y rango intercuartilar", 2: "Mediana y desviación estándar", 3: "Media y rango intercuartilar", 4: "Moda y rango"}),
  d=dict(rotulo="Qué cambia al pasar de una distribución simétrica a una asimétrica",
         antes=dict(titulo="Simétrica (normal)", datos=[("Forma", "Campana: media = mediana = moda"), ("Tendencia central", "Media"), ("Dispersión", "Desviación estándar"), ("Se informa", "Media ± DE"), ("Pruebas", "Paramétricas")]),
         despues=dict(titulo="Asimétrica (sesgada)", datos=[("Forma", "Cola larga: la media sigue a la cola"), ("Tendencia central", "Mediana"), ("Dispersión", "Rango intercuartilar"), ("Se informa", "Mediana (Q1-Q3)"), ("Pruebas", "No paramétricas")]),
         intervencion="Aparecen valores extremos en una cola",
         cambios=[("La media se desplaza hacia la cola", "mejora"), ("La desviación estándar se infla", "mejora"), ("La mediana y el rango intercuartilar casi no cambian", "igual")],
         veredicto=("Asimétrica = mediana y rango intercuartilar", "Moda y rango son demasiado burdos; combinar una medida sensible con una resistente no es coherente.")))

# 062 · PRUEBAS
S("pruebas", "RM-SP-062", "La sensibilidad es el porcentaje de enfermos que la prueba detecta como positivos",
  "Epidemiología · sensibilidad",
  ("Sensibilidad", ["Verdaderos positivos entre todos los enfermos: VP / (VP + FN).", "Es una propiedad de la prueba; no cambia con la prevalencia."]),
  ("Pregunta de definición", ["¿Qué concepto corresponde al porcentaje de enfermos detectados por la prueba?"]),
  ["Sensibilidad = VP / (VP + FN): de cada 100 enfermos, cuántos dan positivo. Especificidad = VN / (VN + FP): sanos con resultado negativo.",
   "Muy sensible con resultado negativo descarta (SnNout); muy específica con resultado positivo confirma (SpPin).",
   "Valor predictivo positivo: entre los positivos, cuántos están enfermos; depende de la prevalencia. Prevalencia e incidencia no son propiedades de una prueba.",
   "Para tamizaje se prefiere una prueba muy sensible (no perder enfermos) y se confirma con una específica."],
  "Altman y Bland, Diagnostic tests 1: sensitivity and specificity (BMJ 1994;308:1552); " + GOR + ".",
  op=("¿Enfermos detectados?", ["No: son los sanos con resultado negativo", "No: son los casos existentes en una población", "No: es la proporción de positivos realmente enfermos", "Sí: verdaderos positivos entre los enfermos", "No: son los casos nuevos en un periodo"],
      {}),
  d=dict(rotulo="Ejemplo ilustrativo: 1000 personas, 100 enfermas", enfermedad="Enfermedad de ejemplo", prueba="Prueba",
         vp=90, fp=90, fn=10, vn=810, pide="sens",
         lado=[("Sensibilidad = 90 %", ["Detecta 90 de los 100 enfermos."], True), ("Especificidad = 90 %", ["810 de 900 sanos dan negativo."], False),
               ("Valor predictivo positivo = 50 %", ["90 de 180 positivos; cambia con la prevalencia."], False)],
         veredicto=("Sensibilidad = enfermos con prueba positiva", "Prevalencia e incidencia miden la enfermedad en la población, no a la prueba.")))

# 063 · BALANZA
S("balanza", "RM-SP-063", "En casos y controles el control es una persona sin la enfermedad, de la misma población que los casos",
  "Epidemiología · selección del grupo control",
  ("Casos y controles", ["Parte del desenlace: compara enfermos (casos) con no enfermos (controles).", "Mide la exposición hacia atrás; su medida es el odds ratio."]),
  ("Pregunta de diseño", ["¿Cómo debe estar integrado el grupo control?"]),
  ["Control: persona sin la enfermedad, de la misma población fuente que los casos, que representa la exposición de esa población.",
   "Entre los controles hay expuestos y no expuestos en la proporción real; exigir solo expuestos o solo no expuestos impide calcular el odds ratio.",
   "Útil en enfermedades raras, de larga latencia y en brotes, porque es rápido y barato. Sesgos propios: de selección y de recuerdo.",
   "Los enfermos, sean expuestos o no, son casos y no pueden ser controles."],
  GOR + "; Wacholder et al., Am J Epidemiol 1992;135:1042-50; " + SZK + ".",
  op=("¿Quién es el control?", ["No: son casos, tienen la enfermedad", "No: se excluirían los no expuestos", "Sí: sin la enfermedad, de la misma población", "No: son casos, tienen la enfermedad", "No: son casos, ya enfermaron"],
      {0: "Los enfermos expuestos a la causa", 1: "Personas sanas, expuestas a la causa", 2: "Personas sin la enfermedad en estudio", 3: "Los enfermos no expuestos a la causa", 4: "Los sanos que enfermaron por la causa"}),
  d=dict(rotulo="Control válido frente a control inválido", gana="izq", pregunta="¿Quién puede ser control?",
         izq=dict(titulo="Control válido", peso="SIN LA ENFERMEDAD", items=["No tiene la enfermedad en estudio (este caso)", "Sale de la misma población fuente que los casos", "Incluye expuestos y no expuestos", "Permite calcular el odds ratio"]),
         der=dict(titulo="No es control", peso="ENFERMOS", items=["Los enfermos, expuestos o no, son casos", "Solo expuestos o solo no expuestos distorsiona la comparación", "Quien enfermó por la causa es un caso", "Sin comparación de exposición no hay odds ratio"]),
         veredicto=("Control = persona sin la enfermedad en estudio", ["Debe ser de la misma población fuente.", "Los enfermos nunca son controles."])))

# 064 · TARJETAS
S("tarjetas", "RM-SP-064", "Comparar mortalidad con las tasas por edad de otra ciudad es la razón estandarizada de mortalidad",
  "Epidemiología · estandarización de tasas",
  ("Estandarización indirecta", ["Aplica las tasas por edad de una población de referencia a la estructura por edad de la población estudiada.", "Elimina el efecto de la edad."]),
  ("Lima y Tokio", ["Con las tasas por edad de cáncer de estómago de Tokio, Lima tendría 0,78 veces las muertes que presenta.", "¿A qué medida se refiere?"]),
  ["La edad confunde la comparación de tasas brutas: una ciudad con más ancianos tiene más muertes aunque el riesgo individual sea igual.",
   "Estandarización directa: aplica las tasas por edad de cada población a una población tipo. Indirecta: calcula muertes esperadas con las tasas de una referencia.",
   "Razón estandarizada de mortalidad (REM o SMR) = muertes observadas entre esperadas; 1 es igualdad, menor de 1 menor mortalidad, mayor de 1 exceso.",
   "El riesgo relativo y el número necesario para tratar o dañar miden el efecto de una exposición o intervención, no ajustan por edad."],
  GOR + "; " + LAST + ".",
  op=("¿Medida del enunciado?", ["No: compara expuestos con no expuestos", "No: mide el beneficio de una intervención", "No: es un modelo de interacción de riesgos", "No: mide el perjuicio de una intervención", "Sí: compara muertes observadas y esperadas"],
      {}),
  d=dict(rotulo="Medidas que se confunden con la estandarización", ans=4,
         cards=[dict(titulo="Razón estandarizada de mortalidad", datos=[("Compara", "Muertes observadas y esperadas", True), ("Ajusta por", "Estructura por edad", True), ("Referencia", "Tasas por edad de otra población", True)], pie="Este caso."),
                dict(titulo="Riesgo relativo", datos=[("Compara", "Incidencia en expuestos y no expuestos", False), ("Ajusta por", "No ajusta por edad", False), ("Sirve para", "Asociación de una exposición", False)], pie="Es de cohortes."),
                dict(titulo="Número necesario para tratar", datos=[("Mide", "Pacientes tratados por evento evitado", False), ("Calcula", "1 / reducción absoluta del riesgo", False), ("Sirve para", "Beneficio de un tratamiento", False)], pie="Es de ensayos."),
                dict(titulo="Número necesario para dañar", datos=[("Mide", "Expuestos por cada daño", False), ("Calcula", "1 / aumento absoluto del riesgo", False), ("Sirve para", "Perjuicio de una intervención", False)], pie="Es de seguridad.")]))

# 065 · CASCADA
S("cascada", "RM-SP-065", "Incidencia triple con igual prevalencia en varones: la letalidad es mayor y la duración, menor",
  "Epidemiología · prevalencia, incidencia y duración",
  ("Prevalencia = incidencia × duración", ["En una población estable, P ≈ I × D.", "Duración corta: los enfermos salen pronto por curación o muerte."]),
  ("Enfermedad con diferencia por sexo", ["Incidencia tres veces mayor en varones.", "Prevalencia igual en ambos sexos. ¿Cuál es la mejor explicación?"]),
  ["Si la incidencia de los varones triplica la de las mujeres y la prevalencia es igual, la duración en los varones debe ser más corta.",
   "Los varones salen del grupo de enfermos con más rapidez, porque se curan antes o porque mueren antes: mayor letalidad.",
   "Duración más corta en las mujeres haría aún mayor la prevalencia masculina; factores de riesgo más frecuentes explican la incidencia, no la igualdad.",
   "La mortalidad bruta no es específica de la enfermedad, y una población masculina mayor no cambia las tasas."],
  GOR + "; " + SZK + ".",
  op=("¿Mejor explicación?", ["No: la mortalidad general no es específica", "No: aumentaría más la diferencia", "Sí: acorta la duración entre los casos", "No: explica la incidencia, no la prevalencia", "No: las tasas no dependen del tamaño"],
      {0: "Mayor mortalidad bruta en varones", 1: "Duración más corta en mujeres", 2: "Mayor letalidad en varones", 3: "Factores de riesgo más frecuentes en varones", 4: "Mayor población de varones"}),
  d=dict(rotulo="Por qué una incidencia triple no eleva la prevalencia", cabeceras=("Mecanismo", "Qué se observa"),
         pasos=[("Incidencia triple en varones", "Entran tres veces más casos nuevos que en mujeres", [("Explicada por los factores de riesgo", "", False)]),
                ("Mayor letalidad en varones", "Los casos mueren o se curan antes", [("Duración media más corta en varones", "", True)]),
                ("Prevalencia ≈ incidencia × duración", "Triple incidencia × duración reducida", [("Prevalencia igual en ambos sexos", "", False)]),
                ("Lectura del enunciado", "Lo que falta explicar es la duración, no la incidencia", [("Letalidad mayor = opción correcta", "", True)])],
         veredicto=("Igual prevalencia con más incidencia = menor duración", "Se explica por una letalidad mayor en varones.")),
  clasif=dict(titulo="Prevalencia según incidencia y duración (P ≈ I × D)", cols=["Situación", "Incidencia", "Duración", "Prevalencia"],
              filas=[["Varones (este caso)", "Alta (×3)", "Corta por mayor letalidad", "Igual"], ["Mujeres", "Baja (×1)", "Más larga", "Igual"],
                     ["Duración más corta en mujeres", "Baja", "Menor", "Aún más baja que en varones"]], caso=0, ancho_primera=230))

# 066 · EMBUDO
S("embudo", "RM-SP-066", "En un brote con 20 enfermos y un testigo cada uno, el OR de 3,5 viene de un estudio de casos y controles",
  "Epidemiología · investigación de un brote",
  ("Brote por alimentos", ["Se busca con rapidez el alimento responsable.", "Con pocos afectados y sin conocer a todos los expuestos, se compara a enfermos con testigos."]),
  ("Brote en una fábrica", ["20 trabajadores afectados, cada uno con un testigo.", "Mayonesa: OR 3,5 e IC 95 % de 1,9 a 7,2. ¿Qué diseño se usó?"]),
  ["Casos y controles va del desenlace a la exposición; la medida de asociación es el odds ratio, aquí 3,5 para la mayonesa.",
   "El intervalo de confianza de 95 % (1,9 a 7,2) no incluye el 1: la asociación es estadísticamente significativa.",
   "Cohorte retrospectiva (tasa de ataque y riesgo relativo) solo si se conoce a todos los comensales. Transversal mide exposición y enfermedad a la vez.",
   "Ecológico y correlacional trabajan con datos de grupos, no con personas."],
  GOR + "; " + SZK + ".",
  op=("¿Diseño?", ["Sí: de enfermos a exposición, con odds ratio", "No: exigiría conocer a todos los comensales", "No: mide exposición y enfermedad a la vez", "No: usa datos de grupos", "No: usa datos de grupos, no de personas"],
      {}),
  d=dict(rotulo="Cómo se llega al diseño", inicio="Brote por alimentos: 20 enfermos, un testigo cada uno",
         candidatos=["Casos y controles", "Cohortes", "Transversal", "Ecológico", "Correlacional"],
         pasos=[("¿Parte de los enfermos y los compara con testigos sanos?", ["Cohortes"]),
                ("¿Usa datos de personas y no de grupos?", ["Ecológico", "Correlacional"]),
                ("¿Compara dos grupos, no mide todo en una sola muestra?", ["Transversal"])],
         final=("ESTUDIO DE CASOS Y CONTROLES", ["Odds ratio 3,5 para la mayonesa", "IC 95 % sin incluir el 1"]),
         nota="Con todos los comensales enumerados sería una cohorte retrospectiva con tasas de ataque."))

# 067 · CUADRO
S("cuadro", "RM-SP-067", "El error tipo I es concluir que el tratamiento es efectivo cuando no lo es: un falso positivo",
  "Bioestadística · errores de la prueba de hipótesis",
  ("Error tipo I (alfa)", ["Rechazar la hipótesis nula cuando es cierta.", "Su probabilidad se fija antes del estudio, por convención en 0,05."]),
  ("Ensayo clínico de un fármaco nuevo", ["La hipótesis nula afirma que no hay diferencia con el control.", "¿A qué conclusión lleva un error tipo I?"]),
  ["Error tipo I (alfa): concluir que el tratamiento es eficaz cuando no lo es, un falso positivo. El valor de p se compara con alfa.",
   "Error tipo II (beta): no detectar un efecto real, falso negativo; el poder (1 - beta) suele fijarse en 80 a 90 %.",
   "Las comparaciones múltiples y los análisis intermedios repetidos aumentan el error tipo I; se corrigen con métodos como Bonferroni.",
   "No hay influencia en la efectividad sería no rechazar la hipótesis nula; la elección de la variable y de pruebas bilaterales no definen el error tipo I."],
  "Altman y Bland, BMJ 1995;310:298; " + GOR + ".",
  op=("¿Conclusión del error tipo I?", ["Sí: rechaza la hipótesis nula cierta", "No: describe el error tipo II", "No: sería no rechazar la hipótesis nula", "No: es un error de diseño, no de inferencia", "No: la bilateralidad no define el error"],
      {0: "Positiva falsa de que es efectivo", 1: "Negativa falsa de que no es efectivo", 2: "No hay influencia en la efectividad", 3: "Selección inadecuada de la variable", 4: "Se deben usar pruebas bilaterales"}),
  d=dict(veredicto=("Error tipo I = falso positivo (alfa)", "El falso negativo, que pierde un efecto real, es el error tipo II.")),
  clasif=dict(titulo="Decisión del ensayo frente a la realidad", cols=["Realidad", "Se rechaza la hipótesis nula", "No se rechaza la hipótesis nula"],
              filas=[["El fármaco no es efectivo", "Error tipo I (alfa): falso positivo", "Decisión correcta"],
                     ["El fármaco sí es efectivo", "Decisión correcta (poder = 1 - beta)", "Error tipo II (beta): falso negativo"]], caso=0, ancho_primera=200,
              nota="Alfa suele ser 0,05; el poder suele fijarse en 80 a 90 %."))

# 068 · RADIAL
S("radial", "RM-SP-068", "Estudiar los casos nuevos de una enfermedad en un periodo es medir la incidencia",
  "Epidemiología · incidencia frente a prevalencia",
  ("Incidencia", ["Casos nuevos aparecidos en un periodo en la población en riesgo.", "Expresa la velocidad con que las personas pasan de sanas a enfermas."]),
  ("Malaria en Tembladera", ["217 casos hasta julio de 2012.", "35 casos nuevos en agosto. ¿Cómo se denomina al estudio de los nuevos casos?"]),
  ["Los 35 casos de agosto empiezan en ese mes: corresponde a la incidencia. Entre la población sin enfermedad en riesgo da la tasa de incidencia.",
   "Con el tiempo-persona como denominador se obtiene la densidad de incidencia.",
   "Los 217 casos acumulados incluyen antiguos y nuevos: eso es prevalencia, no sirve para esta pregunta.",
   "Riesgo relativo y riesgo atribuible comparan expuestos con no expuestos; morbilidad es un término general."],
  GOR + "; " + LAST + ".",
  op=("¿Estudio de casos nuevos?", ["Sí: casos que empiezan en el periodo", "No: compara expuestos y no expuestos", "No: incluye casos antiguos y nuevos", "No: mide el exceso de riesgo en expuestos", "No: es un término general de enfermedad"],
      {}),
  d=dict(rotulo="Qué mide cada término con los datos de la malaria", centro="INCIDENCIA", centro_sub="35 casos nuevos en agosto", ans=0,
         items=[("PREVALENCIA", ["217 casos: antiguos y nuevos"]), ("RIESGO RELATIVO", ["Compara expuestos con no expuestos"]),
                ("RIESGO ATRIBUIBLE", ["Exceso de riesgo debido a la exposición"]), ("MORBILIDAD", ["Término general de presencia de enfermedad"])],
         ruta=["Población libre de malaria", "Se observa agosto", "35 casos empiezan en el periodo", "Incidencia"]))

# 069 · DOS PREGUNTAS
S("dos_preguntas", "RM-SP-069", "La razón de mortalidad materna se expresa por 100 000 nacidos vivos",
  "Salud pública · mortalidad materna",
  ("Razón de mortalidad materna", ["Muertes maternas por cada 100 000 nacidos vivos en un año.", "Es razón porque los nacidos vivos no son la población en riesgo exacta."]),
  ("Pregunta de indicador", ["La razón de muerte materna se calcula con muertes maternas entre nacidos vivos, multiplicado por..."]),
  ["Muerte materna (OMS): la de una mujer durante el embarazo o en los 42 días tras su terminación, por causa relacionada con el embarazo o agravada por él, no accidental.",
   "Razón de mortalidad materna = muertes maternas / nacidos vivos × 100 000. Los nacidos vivos aproximan a las embarazadas, dato difícil de obtener.",
   "Es indicador indirecto de acceso a control prenatal, parto institucional y cuidados obstétricos de emergencia.",
   "No se confunde con la tasa de mortalidad materna, cuyo denominador son las mujeres en edad fértil."],
  "OMS, Trends in maternal mortality 2000 to 2020 (Ginebra, 2023); " + GOR + ".",
  op=("¿Constante?", ["No: no es la constante convencional", "No: no es la constante convencional", "No: no es la constante convencional", "No: se usa para tasas de mortalidad general", "Sí: por 100 000 nacidos vivos"],
      {}),
  d=dict(rotulo="Dos pasos para leer el indicador", pasos=[
            ("¿Qué va en el numerador y en el denominador?", "Muertes maternas entre nacidos vivos del mismo año", "El denominador son nacidos vivos, no embarazadas: por eso es razón y no tasa."),
            ("¿Por cuánto se multiplica?", "Por 100 000 nacidos vivos", "Con 1000 se expresa la mortalidad general; 10 000, 50 000 y 150 000 no son la convención.")],
         veredicto=("Razón de mortalidad materna = muertes maternas / nacidos vivos × 100 000", "Muerte materna: hasta 42 días tras terminar el embarazo.")),
  clasif=dict(titulo="Constantes de uso habitual en los indicadores", cols=["Indicador", "Denominador", "Constante"],
              filas=[["Razón de mortalidad materna", "Nacidos vivos", "100 000"], ["Tasa de mortalidad bruta", "Población a mitad del año", "1000"],
                     ["Tasa de mortalidad infantil", "Nacidos vivos", "1000"]], caso=0, ancho_primera=270))

# 070 · ÁRBOL
S("arbol", "RM-SP-070", "Para probar rho = 0 en una correlación de Pearson se usa la distribución t de Student",
  "Bioestadística · correlación de Pearson",
  ("Coeficiente de correlación de Pearson", ["Mide fuerza y sentido de una relación lineal entre dos variables cuantitativas.", "Varía de -1 a +1; rho es su valor poblacional."]),
  ("HDL y albúmina en daño hepático", ["Se calcula el coeficiente r entre ambas.", "Para probar rho = 0, ¿la distribución de qué prueba se usa?"]),
  ["Hipótesis nula: rho = 0, no hay relación lineal. Estadístico: t = r · raíz(n - 2) / raíz(1 - r²), con n - 2 grados de libertad.",
   "Requiere variables aproximadamente normales; si no, se usa la correlación de Spearman (no paramétrica).",
   "F es del análisis de varianza; z, de comparar proporciones o medias con muestras grandes; binomial, de eventos dicotómicos; chi cuadrado, de variables categóricas.",
   "La correlación no implica causalidad."],
  ALT + "; " + GOR + ".",
  op=("¿Distribución de la prueba?", ["No: es del análisis de varianza", "Sí: t con n - 2 grados de libertad", "No: es de proporciones o medias con muestra grande", "No: es de eventos dicotómicos", "No: es de variables categóricas"],
      {0: "F", 1: "T de Student", 2: "Z", 3: "Binomial", 4: "Chi cuadrado"}),
  arbol=Q("Contrastar rho = 0 entre dos variables cuantitativas", [
      L("Varias medias o varianzas", "F", ["Análisis de varianza", "Compara varianzas"]),
      L("Dos variables cuantitativas (este caso)", "T DE STUDENT", ["t con n - 2 grados de libertad", "Variables aproximadamente normales"], path=True),
      L("Proporciones o muestra grande", "Z", ["Compara proporciones o medias", "Varianza conocida"]),
      L("Variables categóricas", "CHI CUADRADO", ["Prueba de independencia", "Tablas de frecuencias"])], path=True))

# 071 · RELOJ
S("reloj", "RM-SP-071", "Dos mamografías falsas negativas seguidas con sensibilidad de 90 %: 0,10 × 0,10 = 1/100",
  "Epidemiología · probabilidad de eventos independientes",
  ("Falso negativo", ["Es el complemento de la sensibilidad: 1 - sensibilidad.", "En una mujer enferma solo importa la sensibilidad."]),
  ("Mamografía anual", ["Sensibilidad 90 % y especificidad 98 %, pruebas independientes.", "¿Probabilidad de dos mamografías negativas seguidas en una mujer con cáncer?"]),
  ["Mujer con cáncer: se usa la sensibilidad. Falsos negativos = 100 % - 90 % = 10 % = 0,10.",
   "Eventos independientes: se multiplican. 0,10 × 0,10 = 0,01, es decir 1 por 100.",
   "La especificidad (98 %) corresponde a las sanas: es un dato distractor.",
   "La independencia falla si el tumor es difícil de ver (mama densa): un falso negativo haría más probable el siguiente."],
  GOR + "; Altman y Bland, BMJ 1994;308:1552.",
  op=("¿Probabilidad?", ["No: usa la especificidad (2 %)", "No: suma en vez de multiplicar", "No: error de cálculo", "No: error de cálculo", "Sí: 0,10 × 0,10 = 0,01"],
      {}),
  d=dict(rotulo="Cómo se calcula la probabilidad", intro="De la sensibilidad a dos falsos negativos consecutivos.",
         pasos=[("1", "Mujer con cáncer: sensibilidad 90 %", "Solo importa la sensibilidad", False), ("2", "Falso negativo = 1 - 0,90 = 0,10", "Complemento de la sensibilidad", False),
                ("3", "Dos años independientes: 0,10 × 0,10", "Eventos independientes se multiplican", True), ("4", "= 0,01 = 1/100", "Opción E", False)],
         tag="RESULTADO",
         veredicto=("Probabilidad = 0,10 × 0,10 = 1/100", "La especificidad de 98 % no interviene en una mujer enferma.")))

# 072 · PIRÁMIDE
S("piramide", "RM-SP-072", "La vía respiratoria es la de diseminación infecciosa más importante y más difícil de controlar",
  "Epidemiología · vías de transmisión",
  ("Cadena de transmisión", ["La puerta de salida y la vía determinan qué tan fácil es cortar la cadena.", "Respirar no se puede evitar."]),
  ("Pregunta de control", ["¿Cuál es la vía de diseminación infecciosa más importante y difícil de controlar?"]),
  ["Respiratoria: al toser, estornudar o hablar salen gotículas y aerosoles que alcanzan a muchas personas en espacios cerrados; causa epidemias rápidas.",
   "Digestiva (cólera, hepatitis A, tifoidea): se controla con lavado de manos, saneamiento, cloración del agua e higiene de alimentos.",
   "Piel y tracto urinario: rutas de poco alcance poblacional. Placenta: afecta a un binomio madre-hijo y se previene con tamizaje, como en sífilis o VIH.",
   "Medidas en vía aérea: vacunación, ventilación, mascarilla y aislamiento respiratorio."],
  GOR + "; " + LAST + ".",
  op=("¿Vía más difícil de controlar?", ["No: ruta de poco alcance poblacional", "No: se corta con saneamiento e higiene", "Sí: aerosoles que no se pueden evitar", "No: ruta de poco alcance poblacional", "No: afecta a un binomio madre-hijo"],
      {}),
  d=dict(rotulo="Vías de diseminación, de la más a la menos difícil de controlar", caso=0, ancho=380, tag="OPCIÓN CORRECTA",
         niveles=[("A", "Tracto respiratorio", "Gotículas y aerosoles: afectan a muchos y no se evitan."),
                  ("B", "Tracto digestivo", "Agua y alimentos: se controla con saneamiento e higiene."),
                  ("C", "Piel y tracto urinario", "Contacto directo: alcance poblacional limitado."),
                  ("D", "Placenta", "Un solo binomio madre-hijo: se previene con tamizaje.")],
         pie="▲ más difícil de controlar · ▼ más fácil",
         veredicto=("Vía aérea = difícil de controlar y la más importante", "La placenta y la piel afectan a pocas personas; el tracto digestivo se corta con saneamiento.")))
