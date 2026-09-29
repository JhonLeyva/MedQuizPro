"""Bloque 7 · parte M."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"
GORDIS = "Gordis. Epidemiología 6.ª ed. (2019)"
GUYTON = "Guyton y Hall. Tratado de fisiología médica 14.ª ed. (2021)"

# GIN-221 · termómetro
V("termometro", "GIN-221", "gestante-14-semanas-hb-11-hierro-60-folico-400", "Hierro y ácido fólico en la gestante",
  "OBSTETRICIA ENAM: SUPLEMENTACIÓN EN LA GESTACIÓN", "OBSTETRICIA",
  ("Suplementación en el embarazo", ["Desde las 14 semanas: hierro + ácido fólico a toda gestante",
   "Sin anemia: dosis preventiva 60 mg de hierro + 400 µg de ácido fólico"]),
  ("Gestante de 14 semanas en control prenatal", ["Hb 11 g/dl"]),
  {"rotulo": "Hemoglobina en la gestante",
   "niveles": [("≥ 11", "Sin anemia", ["HB 11: PREVENTIVA", "60 mg + 400 µg"]),
               ("10-10,9", "Anemia leve", ["Tratamiento"]),
               ("7-9,9", "Anemia moderada", ["Tratamiento"]),
               ("< 7", "Anemia grave", ["Referir"])],
   "caso_nivel": 0, "ruta_titulo": "Dosis diaria", "paso_label": "PASO",
   "pasos": [(1, "60 mg de hierro + 400 µg de ácido fólico", ["Desde la semana 14 hasta el parto"], True),
             (2, "Con anemia: 120 mg + 800 µg", ["Y controlar Hb al mes"], False),
             (3, "Continuar en el puerperio", ["Hasta 30 días"], False)]},
  ["Ajustar la Hb según la altitud de residencia.",
   "Tomar el hierro lejos del calcio, té y café.",
   "El ácido fólico previo al embarazo previene defectos del tubo neural."],
  "MINSA – NTS 213: Prevención y control de la anemia por deficiencia de hierro (2024)")

# CB-078 · fases
V("fases", "CB-078", "digestion-proteinas-inicia-pepsina", "Digestión de las proteínas",
  "CIENCIAS BÁSICAS ENAM: PEPSINA", "CIENCIAS BÁSICAS",
  ("Digestión de proteínas", ["Empieza en el estómago con la pepsina",
   "El pepsinógeno se activa a pepsina por el ácido clorhídrico"]),
  ("Pregunta de fisiología", ["¿Qué enzima inicia la digestión de las proteínas?"]),
  {"rotulo": "Recorrido de la proteína", "ans": 0,
   "fases": [("Estómago", "pH ácido", "PEPSINA", ["Pepsinógeno + HCl", "Rompe en péptidos"]),
             ("Duodeno", "Páncreas", "Tripsina, quimotripsina", ["Elastasa, carboxipeptidasa"]),
             ("Borde en cepillo", "Enterocito", "Peptidasas", ["Dipéptidos y aminoácidos"]),
             ("Absorción", "Yeyuno", "Aminoácidos", ["Pasan a la porta"])],
   "curvas": [],
   "chips_titulo": "Enzima inicial · marcada la correcta",
   "chips": [("Pepsina", True), ("Tripsina", False), ("Elastasa", False), ("Lipasa", False)]},
  ["La enteroquinasa activa el tripsinógeno en el duodeno.",
   "La lipasa digiere grasas, no proteínas.",
   "Sin ácido gástrico, la pepsina no se activa."],
  GUYTON)

# NEU-065 · tarjetas
V("tarjetas", "NEU-065", "obrero-construccion-placas-pleurales-asbesto", "Neumoconiosis",
  "NEUMOLOGÍA ENAM: ASBESTOSIS", "NEUMOLOGÍA",
  ("Exposición al asbesto", ["Construcción, frenos, aislantes, tuberías",
   "Placas pleurales (a menudo calcificadas) y fibrosis basal"]),
  ("Obrero de construcción de 50 años, 15 años de trabajo", ["Control ocupacional", "Engrosamiento y placas pleurales basales"]),
  {"rotulo": "¿Qué polvo lo causó?", "ans": 0, "cards": [
      {"titulo": "ASBESTOSIS", "datos": [
          ("Trabajo", "Construcción, aislantes", True), ("Imagen", "Placas pleurales basales", True),
          ("Riesgo", "Mesotelioma, cáncer", False)],
       "pie": "Fibrosis en bases"},
      {"titulo": "Silicosis", "datos": [
          ("Trabajo", "Minería, canteras", False), ("Imagen", "Nódulos en vértices", False),
          ("Riesgo", "Tuberculosis", False)],
       "pie": "Ganglios en cáscara de huevo"},
      {"titulo": "Neumoconiosis del carbón", "datos": [
          ("Trabajo", "Minas de carbón", False), ("Imagen", "Nódulos en vértices", False),
          ("Riesgo", "Fibrosis masiva", False)],
       "pie": "Pulmón negro"},
      {"titulo": "Bisinosis", "datos": [
          ("Trabajo", "Algodón, textil", False), ("Imagen", "Normal", False),
          ("Riesgo", "Asma ocupacional", False)],
       "pie": "Opresión el lunes"}]},
  ["Las placas pleurales son marcador de exposición, no siempre de enfermedad.",
   "El tabaco multiplica el riesgo de cáncer de pulmón con asbesto.",
   "Latencia larga: 15-30 años."],
  "ATS – Diagnosis and initial management of nonmalignant diseases related to asbestos (2004) · " + HARRISON)

# OFT-050 · radial
V("radial", "OFT-050", "glaucoma-factor-riesgo-presion-intraocular", "Factores de riesgo del glaucoma",
  "OFTALMOLOGÍA ENAM: GLAUCOMA", "OFTALMOLOGÍA",
  ("Glaucoma", ["Neuropatía óptica con pérdida progresiva del campo visual",
   "La presión intraocular alta es el principal factor de riesgo y el único tratable"]),
  ("Pregunta de oftalmología", ["¿Cuál es el factor de riesgo más importante?"]),
  {"rotulo": "Mapa del tema", "centro": "GLAUCOMA", "centro_sub": "Factores de riesgo", "ans": 0,
   "items": [("PRESIÓN INTRAOCULAR ALTA", ["> 21 mmHg", "Único modificable"]),
             ("Edad", ["Mayor de 40 años"]),
             ("Antecedente familiar", ["Primer grado"]),
             ("Raza negra", ["Más frecuente y agresivo"]),
             ("Miopía alta", ["Riesgo menor"])],
   "ruta": ["Presión alta", "Daño del nervio óptico", "Excavación de papila", "GLAUCOMA"]},
  ["Tamizaje: toma de presión y fondo de ojo desde los 40 años.",
   "Tratamiento: colirios que bajan la presión (prostaglandinas, timolol).",
   "La pérdida de visión es irreversible."],
  "AAO – Preferred Practice Pattern: Primary open-angle glaucoma (2020) · EGS – Terminology and guidelines (2020)")

# HEM-041 · matriz
V("matriz", "HEM-041", "control-warfarina-inr", "¿Cómo se controla cada anticoagulante?",
  "HEMATOLOGÍA ENAM: CONTROL DE LA WARFARINA", "HEMATOLOGÍA",
  ("Warfarina", ["Bloquea los factores dependientes de vitamina K (II, VII, IX, X)",
   "Se controla con el INR; meta habitual 2-3"]),
  ("Pregunta de hematología", ["¿Qué examen controla el nivel terapéutico de la warfarina?"]),
  {"rotulo": "Anticoagulante y examen", "eje_x": "Rasgo", "eje_y": "Fármaco",
   "cols": ["Examen de control", "Meta"], "rows": ["Warfarina", "Heparina no fraccionada", "Heparina de bajo peso", "Anticoagulantes directos"], "caso": (0, 0),
   "cells": [[("INR", ["Tiempo de protrombina"]), ("2-3", ["2,5-3,5 en válvula mecánica"])],
             [("TTPa", []), ("1,5-2,5 veces", [])],
             [("Anti-Xa", ["Solo en casos especiales"]), ("—", [])],
             [("No rutinario", []), ("Función renal", [])]]},
  ["Muchos fármacos y alimentos modifican el INR.",
   "Las plaquetas se vigilan con heparina (trombocitopenia).",
   "Controles frecuentes al inicio y al cambiar dosis."],
  "ACCP – Antithrombotic therapy guidelines (2012; actualización) · " + HARRISON)

# PED-210 · árbol
A("PED-210", "lactante-12-meses-hb-9-7-ferritina-serica", "Confirmar la anemia ferropénica",
  "PEDIATRÍA ENAM: FERRITINA SÉRICA", "PEDIATRÍA",
  ("Anemia ferropénica", ["La ferritina refleja los depósitos de hierro",
   "Ferritina < 12 µg/L en menores de 5 años confirma la ferropenia"]),
  ("Lactante de 12 meses en control de niño sano", ["Hb 9,7 g/dl", "Leucocitos y plaquetas normales"]),
  Q("¿Hay infección o inflamación activa?", [
      L("No", "FERRITINA SÉRICA", ["< 12 µg/L confirma", "Depósitos agotados"], path=True),
      L("Sí", "Ferritina + PCR o saturación", ["La inflamación eleva la ferritina"])], path=True),
  ("Pruebas de hierro", [("Ferritina", True), ("Saturación de transferrina", False), ("VCM", False)], [
      ("Mide", ["Depósitos", "Hierro circulante", "Tamaño del hematíe"]),
      ("Papel", ["Confirma ferropenia", "Complementa", "Orienta, no confirma"])]),
  ["La hepcidina no se usa en la práctica clínica.",
   "Tratamiento: hierro 3 mg/kg/día por 6 meses.",
   "Controlar Hb al mes: debe subir ≥ 1 g/dl."],
  "MINSA – NTS 213 (2024) · OMS – Uso de la ferritina para evaluar el hierro (2020)")

# INF-099 · árbol
A("INF-099", "rn-madre-hbsag-positivo-vacuna-inmunoglobulina-12-h", "Recién nacido de madre con hepatitis B",
  "INFECTOLOGÍA ENAM: PREVENCIÓN DE HEPATITIS B VERTICAL", "INFECTOLOGÍA",
  ("Transmisión vertical de hepatitis B", ["Sin profilaxis, el RN tiene alto riesgo de hepatitis B crónica",
   "Vacuna + inmunoglobulina en las primeras 12 horas; la lactancia está permitida"]),
  ("RN a término de 1 hora", ["Madre adolescente HBsAg (+), HBeAg (−)"]),
  Q("¿Madre HBsAg positiva?", [
      L("Sí", "VACUNA + IgHB < 12 H", ["Iniciar lactancia", "Completar esquema de vacuna"], path=True),
      L("No", "Vacuna al nacer", ["Esquema habitual"])], path=True),
  ("Profilaxis del RN", [("Medida", True), ("Detalle", False)], [
      ("Vacuna hepatitis B", ["< 12 h", "Luego a los 2, 4 y 6 meses"]),
      ("Inmunoglobulina", ["< 12 h", "Otro muslo"]),
      ("Control", ["HBsAg y anti-HBs", "A los 9-12 meses"])]),
  ["La lactancia no aumenta el riesgo si se dio la profilaxis.",
   "Madre con carga viral alta: tenofovir desde las 28 semanas.",
   "Eficacia de la profilaxis combinada > 90 %."],
  "MINSA – NTS 159 (2019) · CDC – Hepatitis B perinatal transmission (2024)")

# CAR-068 · matriz
V("matriz", "CAR-068", "st-elevado-dii-diii-avf-infarto-inferior", "Localización del infarto en el ECG",
  "CARDIOLOGÍA ENAM: INFARTO DE CARA INFERIOR", "CARDIOLOGÍA",
  ("Localización del infarto", ["Las derivaciones con ST elevado señalan la cara dañada",
   "DII, DIII y aVF = cara inferior (coronaria derecha en la mayoría)"]),
  ("Varón de 58 años con 2 h de dolor precordial", ["Irradiado a mandíbula, diaforesis, palidez", "ST elevado en DII, DIII y aVF · troponina alta"]),
  {"rotulo": "Derivaciones y cara", "eje_x": "Rasgo", "eje_y": "Cara",
   "cols": ["Derivaciones", "Arteria"], "rows": ["Inferior", "Anteroseptal", "Lateral", "Anterior extensa"], "caso": (0, 0),
   "cells": [[("DII, DIII, aVF", []), ("Coronaria derecha", ["O circunfleja"])],
             [("V1-V4", []), ("Descendente anterior", [])],
             [("DI, aVL, V5-V6", []), ("Circunfleja", [])],
             [("V1-V6, DI, aVL", []), ("DA proximal", [])]]},
  ["En el infarto inferior, pedir V3R-V4R para buscar infarto de VD.",
   "Con infarto de VD evitar nitratos: hipotensión.",
   "Puede dar bradicardia y bloqueo AV."],
  "ESC – Guidelines for acute coronary syndromes (2023)")

# TRA-048 · puntaje
V("puntaje", "TRA-048", "pierna-dolor-extension-dedos-edema-pulso-debil-compartimental", "Pierna tensa tras un accidente",
  "TRAUMATOLOGÍA ENAM: SÍNDROME COMPARTIMENTAL", "TRAUMATOLOGÍA",
  ("Síndrome compartimental", ["Presión alta dentro de un compartimento que corta la circulación",
   "Signo temprano: dolor desproporcionado y al estirar los músculos pasivamente"]),
  ("Varón de 36 años, 3 h tras accidente de tránsito", ["Dolor intenso al extender los dedos del pie", "Edema marcado, pie cianótico, pulso pedio disminuido"]),
  {"rotulo": "Signos del caso", "escala": "Signos (P)", "total": 4, "max": 6,
   "total_label": "Signos presentes",
   "interpreta": "Síndrome compartimental: fasciotomía",
   "items": [("Dolor al estiramiento pasivo", "✓", True), ("Tensión y edema marcado", "✓", True),
             ("Cianosis del pie", "✓", True), ("Pulso disminuido (tardío)", "✓", True),
             ("Parestesias", "?", False), ("Parálisis", "?", False)],
   "bandas": [("Dudoso", "Sospecha", "Medir presión compartimental", False),
              ("Claro", "Diagnóstico clínico", "Fasciotomía urgente", True)]},
  ["El pulso puede estar presente hasta muy tarde: no esperar a que desaparezca.",
   "Presión compartimental > 30 mmHg o ΔP < 30: fasciotomía.",
   "Retirar yesos y vendajes apretados."],
  "BOAST 10 – Diagnosis and management of compartment syndrome of the limbs (2016) · " + ATLS)

# SP-161 · radial
V("radial", "SP-161", "microrred-morbimortalidad-priorizacion-asis", "Documentos de gestión",
  "SALUD PÚBLICA ENAM: ANÁLISIS DE SITUACIÓN DE SALUD", "SALUD PÚBLICA",
  ("ASIS", ["Documento que describe morbimortalidad y prioriza los problemas de salud",
   "Es la base para los planes"]),
  ("Jefe de microrred", ["Debe exponer al alcalde la morbimortalidad del año pasado", "Con los problemas priorizados"]),
  {"rotulo": "Mapa del tema", "centro": "DOCUMENTOS", "centro_sub": "¿Qué contiene cada uno?", "ans": 0,
   "items": [("ASIS", ["Morbimortalidad y prioridades", "Diagnóstico de salud"]),
             ("Plan local de salud", ["Acciones concertadas"]),
             ("Plan estratégico (PEI)", ["Objetivos a mediano plazo"]),
             ("Plan operativo (POI)", ["Actividades del año"]),
             ("Presupuesto", ["Asigna recursos"])],
   "ruta": ["Morbimortalidad", "Priorizar problemas", "Mostrar al alcalde", "ASIS"]},
  ["El ASIS se actualiza de forma periódica.",
   "Sirve para concertar con gobiernos locales.",
   "Incluye determinantes sociales y oferta de servicios."],
  "MINSA – Documento técnico: Metodología para el ASIS local (2015)")

# GAS-070 · árbol
A("GAS-070", "litiasis-dolor-epigastrio-espalda-ictericia-hidratacion-ev", "Pancreatitis biliar: primer paso",
  "GASTROENTEROLOGÍA ENAM: PANCREATITIS AGUDA BILIAR", "GASTROENTEROLOGÍA",
  ("Pancreatitis aguda biliar", ["Un cálculo obstruye la ampolla y activa las enzimas",
   "Primer paso: hidratación EV y analgesia; CPRE solo si hay colangitis u obstrucción persistente"]),
  ("Mujer de 45 años con litiasis vesicular", ["2 h de dolor epigástrico intenso a la espalda, náuseas y vómitos", "Ictericia escleral · dolor en epigastrio e HCD"]),
  Q("¿Hay colangitis (fiebre, ictericia, sepsis)?", [
      L("Sí", "CPRE urgente + antibióticos", ["En las primeras 24 h"]),
      L("No", "HIDRATACIÓN EV", ["Ringer lactato, analgesia", "Lipasa, eco para confirmar"], path=True)], path=True),
  ("Manejo de la pancreatitis biliar", [("Cuándo", True), ("Detalle", False)], [
      ("Hidratación", ["Desde el inicio", "Ringer lactato"]),
      ("CPRE", ["Colangitis u obstrucción", "No de rutina"]),
      ("Colecistectomía", ["En la misma hospitalización", "Evita recurrencias"])]),
  ["Los antibióticos no se dan de rutina: solo si hay infección.",
   "Los antiespasmódicos no cambian el curso.",
   "Iniciar dieta oral en cuanto tolere."],
  "ACG – Guideline: Management of acute pancreatitis (2024) · IAP/APA (2013)")

# NEF-084 · puntaje
V("puntaje", "NEF-084", "lupus-edema-orina-espumosa-proteinuria-24-horas", "Edema y orina espumosa en el lupus",
  "NEFROLOGÍA ENAM: NEFRITIS LÚPICA", "NEFROLOGÍA",
  ("Nefritis lúpica con síndrome nefrótico", ["La proteinuria de 24 h es el criterio diagnóstico",
   "≥ 3,5 g/24 h define el rango nefrótico; ≥ 0,5 g es criterio de lupus renal"]),
  ("Mujer de 30 años", ["Edema de piernas, orina espumosa, alopecia · artralgias", "PA 140/90 · eritema malar · creatinina 1,8"]),
  {"rotulo": "Criterios de síndrome nefrótico", "escala": "Criterios", "total": 1, "max": 4,
   "total_label": "Criterios confirmados",
   "interpreta": "Falta el criterio principal: medirlo",
   "items": [("Edema", "✓", True), ("Proteinuria ≥ 3,5 g/24 h", "?", False),
             ("Albúmina < 3 g/dl", "?", False), ("Hiperlipidemia", "?", False)],
   "bandas": [("Sin proteinuria", "No confirmado", "Pedir proteínas en orina de 24 h", True),
              ("Con proteinuria", "Nefrótico", "Biopsia renal: clase de nefritis", False)]},
  ["La biopsia renal define la clase (I-VI) y el tratamiento.",
   "El cociente proteína/creatinina en orina aislada es alternativa.",
   "Tratamiento: corticoides + micofenolato o ciclofosfamida."],
  "KDIGO – Clinical practice guideline for lupus nephritis (2024) · EULAR/ERA-EDTA (2019)")

# REU-062 · embudo
V("embudo", "REU-062", "nino-medallon-heraldico-arbol-de-navidad-pitiriasis-rosada", "Placa inicial y erupción en árbol de navidad",
  "DERMATOLOGÍA ENAM: PITIRIASIS ROSADA", "DERMATOLOGÍA",
  ("Pitiriasis rosada", ["Placa heráldica seguida de máculas ovaladas en 'árbol de navidad'",
   "Probable origen viral (herpes 6/7); se cura sola en 6-8 semanas"]),
  ("Niño de 7 años", ["Medallón en el tronco; a los 10 días se disemina por la espalda", "Sin prurito · rinofaringitis previa · máculas rosadas descamativas"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Placas descamativas en el tronco",
   "candidatos": ["Pitiriasis rosada", "Tiña corporis", "Dermatitis seborreica", "Psoriasis"],
   "pasos": [("Placa heráldica que precede a la erupción", ["Tiña corporis", "Psoriasis"]),
             ("Patrón en árbol de navidad en la espalda", ["Dermatitis seborreica"])],
   "final": ("PITIRIASIS ROSADA", ["Tranquilizar: autolimitada", "Emolientes; antihistamínico si pica"]),
   "nota": "En adolescentes con riesgo sexual, descartar sífilis secundaria (palmas y plantas)."},
  ["La tiña tiene borde activo y KOH positivo.",
   "La psoriasis tiene escama nacarada en codos y rodillas.",
   "No deja cicatriz."],
  "Fitzpatrick's Dermatology 9.ª ed. (2019) · " + NELSON)

# GIN-222 · embudo
V("embudo", "GIN-222", "mioma-25-mm-asintomatico-perimenopausia-observacion", "Mioma pequeño y sin síntomas",
  "GINECOLOGÍA ENAM: MIOMA UTERINO", "GINECOLOGÍA",
  ("Mioma uterino", ["Tumor benigno del músculo uterino, dependiente de estrógenos",
   "Asintomático: observación; tiende a reducirse en la menopausia"]),
  ("Mujer de 50 años asintomática", ["Mioma de 25 mm, tipo 7 (subseroso pediculado) en el fondo", "Hb 13,5 · FSH 30 (perimenopausia)"]),
  {"rotulo": "Embudo de conductas",
   "inicio": "Mioma encontrado en control",
   "candidatos": ["Observación", "Miomectomía", "Histerectomía", "Histeroscopía"],
   "pasos": [("Sin sangrado, dolor ni anemia", ["Miomectomía", "Histerectomía"]),
             ("Subseroso (tipo 7): no está en la cavidad", ["Histeroscopía"])],
   "final": ("OBSERVACIÓN", ["Control clínico y ecográfico", "Se reduce en la menopausia"]),
   "nota": "La histeroscopía sirve para miomas submucosos (tipos 0-2)."},
  ["Tratar solo si hay síntomas: sangrado, dolor, compresión, infertilidad.",
   "Crecimiento rápido en posmenopausia: descartar sarcoma.",
   "Endometrio de 2,4 mm: normal."],
  "ACOG – Practice Bulletin 228: Management of symptomatic uterine leiomyomas (2021) · FIGO (2018)")

# INF-100 · tarjetas
V("tarjetas", "INF-100", "ulcera-vulvar-indolora-limpia-chancro-sifilis", "Úlceras genitales",
  "INFECTOLOGÍA ENAM: SÍFILIS PRIMARIA", "INFECTOLOGÍA",
  ("Chancro sifilítico", ["Úlcera única, indolora, limpia, de bordes definidos e indurados",
   "Aparece ~3 semanas tras el contacto y cura sola"]),
  ("Mujer de 24 años", ["Lesión vulvar indolora de 5 días", "Úlcera limpia de 0,5 cm, bordes definidos, sin adenopatías"]),
  {"rotulo": "¿Qué úlcera es?", "ans": 0, "cards": [
      {"titulo": "SÍFILIS (CHANCRO)", "datos": [
          ("Dolor", "Indolora", True), ("Fondo", "Limpio, indurado", True),
          ("Ganglios", "Indoloros o ausentes", True), ("Tratamiento", "Penicilina benzatínica", False)],
       "pie": "Treponema pallidum"},
      {"titulo": "Herpes genital", "datos": [
          ("Dolor", "Muy dolorosa", False), ("Fondo", "Vesículas agrupadas", False),
          ("Ganglios", "Dolorosos", False), ("Tratamiento", "Aciclovir", False)],
       "pie": "Recurrente"},
      {"titulo": "Chancroide", "datos": [
          ("Dolor", "Dolorosa", False), ("Fondo", "Sucio, bordes irregulares", False),
          ("Ganglios", "Bubón supurado", False), ("Tratamiento", "Azitromicina", False)],
       "pie": "Haemophilus ducreyi"},
      {"titulo": "Linfogranuloma venéreo", "datos": [
          ("Dolor", "Úlcera fugaz", False), ("Fondo", "Pasa inadvertida", False),
          ("Ganglios", "Bubón doloroso", False), ("Tratamiento", "Doxiciclina", False)],
       "pie": "Chlamydia L1-L3"}]},
  ["Confirmar con prueba rápida treponémica y RPR/VDRL.",
   "Penicilina benzatínica 2,4 millones UI IM, dosis única.",
   "Tratar a la pareja y ofrecer prueba de VIH."],
  "CDC – STI treatment guidelines: syphilis (2021) · MINSA – NTS 077")

# NEU-066 · puntaje
V("puntaje", "NEU-066", "espirometria-reversibilidad-vef1-12-200-ml", "Prueba broncodilatadora positiva",
  "NEUMOLOGÍA ENAM: ESPIROMETRÍA EN EL ASMA", "NEUMOLOGÍA",
  ("Reversibilidad de la obstrucción", ["Tras salbutamol, el VEF₁ sube en el asma",
   "Positiva: aumento ≥ 12 % y ≥ 200 ml sobre el valor basal"]),
  ("Sospecha de asma", ["¿Qué define una prueba broncodilatadora positiva en adultos?"]),
  {"rotulo": "Criterios de reversibilidad", "escala": "Prueba broncodilatadora", "total": 2, "max": 2,
   "total_label": "Criterios que se exigen",
   "interpreta": "Ambos juntos = prueba positiva",
   "items": [("VEF₁ aumenta ≥ 12 %", "✓", True), ("VEF₁ aumenta ≥ 200 ml", "✓", True)],
   "bandas": [("< 2", "Negativa", "No descarta asma: repetir o provocación", False),
              ("2 de 2", "Positiva", "Apoya el diagnóstico de asma", True)]},
  ["Una prueba negativa no descarta el asma (puede estar controlada).",
   "En el EPOC la obstrucción persiste tras el broncodilatador.",
   "Variabilidad del PEF > 10 % también apoya el asma."],
  "GINA – Global Strategy for Asthma Management and Prevention (2025) · ATS/ERS – Interpretive strategies (2022)")

# NRL-055 · puntaje
V("puntaje", "NRL-055", "anciana-olvidos-se-pierde-no-reconoce-familia-demencia", "Deterioro cognitivo progresivo",
  "NEUROLOGÍA ENAM: DEMENCIA", "NEUROLOGÍA",
  ("Demencia", ["Deterioro cognitivo progresivo que afecta la vida diaria",
   "Curso de meses a años, con conciencia conservada (a diferencia del delirium)"]),
  ("Mujer de 85 años", ["2 años de olvidos: pierde cosas, repite preguntas, deja la hornilla prendida", "Se pierde en la calle, no reconoce familiares, dice que le roban"]),
  {"rotulo": "Dominios afectados", "escala": "Dominios cognitivos", "total": 5, "max": 6,
   "total_label": "Dominios afectados",
   "interpreta": "Demencia (probable Alzheimer)",
   "items": [("Memoria reciente", "✓", True), ("Orientación espacial", "✓", True),
             ("Funciones ejecutivas y juicio", "✓", True), ("Reconocimiento (agnosia)", "✓", True),
             ("Conducta: ideas de robo", "✓", True), ("Nivel de conciencia alterado", "—", False)],
   "bandas": [("Agudo", "Delirium", "Conciencia fluctuante, horas-días", False),
              ("Crónico", "Demencia", "Evaluar causas tratables", True)]},
  ["Descartar causas reversibles: hipotiroidismo, déficit de B12, depresión.",
   "Las ideas de robo son frecuentes en la enfermedad de Alzheimer.",
   "Tratamiento: inhibidores de colinesterasa y apoyo al cuidador."],
  "APA – DSM-5-TR (2022) · NIA-AA – Alzheimer's disease diagnostic guidelines (2024)")

# PED-211 · tarjetas
V("tarjetas", "PED-211", "rn-cianosis-al-llanto-corazon-en-bota-fallot", "Cardiopatías con cianosis o sin ella",
  "PEDIATRÍA ENAM: TETRALOGÍA DE FALLOT", "PEDIATRÍA",
  ("Tetralogía de Fallot", ["Estenosis pulmonar, CIV, aorta cabalgante e hipertrofia del VD",
   "Cianosis que empeora con el llanto; Rx con corazón 'en bota'"]),
  ("RN de 3 kg, madre de 37 años", ["Reingresa por cianosis al llanto", "Rx: corazón en forma de bota"]),
  {"rotulo": "¿Qué cardiopatía es?", "ans": 0, "cards": [
      {"titulo": "TETRALOGÍA DE FALLOT", "datos": [
          ("Cianosis", "Sí, con el llanto", True), ("Rx", "Corazón en bota", True),
          ("Flujo pulmonar", "Disminuido", False), ("Crisis", "Hipoxémicas", False)],
       "pie": "La cianótica más frecuente"},
      {"titulo": "Estenosis pulmonar", "datos": [
          ("Cianosis", "Solo si es crítica", False), ("Rx", "Arteria pulmonar dilatada", False),
          ("Flujo pulmonar", "Variable", False), ("Crisis", "No", False)],
       "pie": "Soplo eyectivo"},
      {"titulo": "CIV", "datos": [
          ("Cianosis", "No", False), ("Rx", "Cardiomegalia", False),
          ("Flujo pulmonar", "Aumentado", False), ("Crisis", "No", False)],
       "pie": "Soplo holosistólico"},
      {"titulo": "CIA", "datos": [
          ("Cianosis", "No", False), ("Rx", "Crecimiento derecho", False),
          ("Flujo pulmonar", "Aumentado", False), ("Crisis", "No", False)],
       "pie": "Desdoblamiento fijo"}]},
  ["Crisis hipoxémica: posición rodillas-pecho, O₂, morfina.",
   "Cirugía correctora en el primer año.",
   "Asociación con síndrome de DiGeorge (22q11)."],
  NELSON + " · AHA – Congenital heart disease statement (2023)")

# SP-162 · matriz
V("matriz", "SP-162", "9000-atendidos-18000-atenciones-concentracion-2", "Indicadores de consulta externa",
  "SALUD PÚBLICA ENAM: CONCENTRACIÓN", "SALUD PÚBLICA",
  ("Concentración (intensidad de uso)", ["Cuántas atenciones recibe en promedio cada atendido",
   "Atenciones / atendidos = 18 000 / 9000 = 2"]),
  ("Evaluación anual 2023", ["9000 atendidos", "18 000 atenciones"]),
  {"rotulo": "Indicador y fórmula", "eje_x": "Rasgo", "eje_y": "Indicador",
   "cols": ["Fórmula", "Resultado"], "rows": ["Concentración", "Extensión de uso", "Rendimiento hora-médico", "Utilización"], "caso": (0, 1),
   "cells": [[("Atenciones / atendidos", []), ("2", ["18 000 / 9000"])],
             [("Atendidos / población", []), ("Falta población", [])],
             [("Atenciones / horas médico", []), ("Falta horas", [])],
             [("Horas usadas / programadas", []), ("Falta dato", [])]]},
  ["Atendido: persona que viene por primera vez en el año.",
   "Atención: cada consulta, nueva o repetida.",
   "Una concentración muy alta puede indicar mala resolución."],
  "MINSA – Indicadores de gestión y evaluación hospitalaria (2013)")

# PED-212 · radial
V("radial", "PED-212", "lactante-1-mes-itu-febril-ampicilina-amikacina", "ITU febril en el lactante pequeño",
  "PEDIATRÍA ENAM: INFECCIÓN URINARIA EN EL MENOR DE 3 MESES", "PEDIATRÍA",
  ("ITU en el lactante < 3 meses", ["Riesgo de bacteriemia: hospitalizar y dar antibiótico EV",
   "Ampicilina (enterococo) + aminoglucósido (gramnegativos)"]),
  ("Lactante de 1 mes", ["3 días de fiebre, succión pobre, rechazo al alimento y vómitos", "Orina: > 100 leucocitos/campo, nitritos (+)"]),
  {"rotulo": "Mapa del tema", "centro": "ITU < 3 MESES", "centro_sub": "¿Qué antibiótico?", "ans": 0,
   "items": [("AMPICILINA + AMIKACINA EV", ["Cubre E. coli y enterococo", "7-14 días"]),
             ("Amoxicilina-clavulánico VO", ["Mayores de 3 meses"]),
             ("Cloranfenicol", ["Tóxico: síndrome gris"]),
             ("Amikacina IM 3 días", ["Insuficiente"]),
             ("Ceftriaxona", ["Evitar si hay ictericia neonatal"])],
   "ruta": ["1 mes de vida", "Fiebre y vómitos", "Riesgo de sepsis", "AMPICILINA + AMIKACINA"]},
  ["Tomar urocultivo por sonda antes del antibiótico.",
   "Hemocultivo y valorar punción lumbar en el menor de 1 mes.",
   "Ecografía renal tras la primera ITU febril."],
  "AAP – UTI guideline (2011, reafirmada 2016) · MINSA – GPC de infección urinaria en niños")

# PED-213 · puntaje
V("puntaje", "PED-213", "lactante-infecciones-repeticion-esteatorrea-fibrosis-quistica", "Infecciones respiratorias y heces grasosas",
  "PEDIATRÍA ENAM: FIBROSIS QUÍSTICA", "PEDIATRÍA",
  ("Fibrosis quística", ["Moco espeso en pulmón y páncreas (gen CFTR)",
   "Infecciones respiratorias repetidas + esteatorrea + mal crecimiento"]),
  ("Lactante de 10 meses con taquipnea y sibilancias", ["Cuadros respiratorios a repetición", "Diarreas malolientes y aceitosas · 6,7 kg a los 10 meses"]),
  {"rotulo": "Datos que sugieren fibrosis quística", "escala": "Hallazgos del caso", "total": 4, "max": 5,
   "total_label": "Hallazgos presentes",
   "interpreta": "Sospecha alta: test del sudor",
   "items": [("Infecciones respiratorias recurrentes", "✓", True), ("Esteatorrea (heces aceitosas)", "✓", True),
             ("Desnutrición o mal crecimiento", "✓", True), ("Sibilancias persistentes", "✓", True),
             ("Íleo meconial al nacer", "?", False)],
   "bandas": [("0-1", "Poco probable", "Buscar otras causas", False),
              ("≥ 2", "Sospecha alta", "Cloro en sudor ≥ 60 mmol/L confirma", True)]},
  ["Tamizaje neonatal: tripsinógeno inmunorreactivo.",
   "Tratamiento: enzimas pancreáticas, fisioterapia, antibióticos.",
   "Pseudomonas y S. aureus colonizan el pulmón."],
  "CFF – Diagnosis of cystic fibrosis: consensus guidelines (2017) · " + NELSON)

# PED-214 · termómetro
V("termometro", "PED-214", "prematuro-26-semanas-palidez-fontanela-hemorragia-intraventricular", "Hemorragia intraventricular del prematuro",
  "PEDIATRÍA ENAM: HEMORRAGIA INTRAVENTRICULAR", "PEDIATRÍA",
  ("Hemorragia intraventricular", ["Sangrado de la matriz germinal en prematuros < 32 semanas",
   "Caída brusca de Hb, fontanela abombada, deterioro clínico"]),
  ("RN de 26 semanas intubado", ["Palidez brusca y fontanela anterior tensa", "Hb 7 · PCR normal · sin signos claros de sepsis"]),
  {"rotulo": "Grado de Papile",
   "niveles": [("I", "Matriz germinal", ["Subependimaria"]),
               ("II", "Intraventricular", ["Sin dilatación"]),
               ("III", "Con dilatación", ["CAÍDA DE HB + FONTANELA", "Ventrículos dilatados"]),
               ("IV", "Parenquimatosa", ["Infarto hemorrágico"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Ecografía transfontanelar", ["Confirma y gradúa"], True),
             (2, "Soporte y transfusión", ["Evitar cambios bruscos de PA"], False),
             (3, "Vigilar hidrocefalia", ["Perímetro cefálico, ecografías seriadas"], False)]},
  ["Ocurre en los primeros 3-7 días de vida.",
   "Corticoides prenatales reducen su frecuencia.",
   "Los grados III-IV dejan más secuelas motoras."],
  NELSON + " · Papile LA (J Pediatr 1978)")

# NEF-085 · fases
V("fases", "NEF-085", "falla-renal-t-picudas-qrs-ancho-gluconato-calcio", "Tratamiento de la hiperpotasemia",
  "NEFROLOGÍA ENAM: ESTABILIZAR EL MIOCARDIO", "NEFROLOGÍA",
  ("Hiperpotasemia con cambios en el ECG", ["Primero proteger el corazón con calcio EV",
   "Luego meter potasio a las células y finalmente eliminarlo"]),
  ("Varón de 60 años con falla cardiaca, diabetes e IRA", ["ECG: T picudas, PR largo, QRS ancho"]),
  {"rotulo": "Orden del tratamiento", "ans": 0,
   "fases": [("Estabilizar", "Minutos", "GLUCONATO DE CALCIO", ["10 % 10 ml EV en 5-10 min", "Repetir si sigue el ECG"]),
             ("Redistribuir", "15-30 min", "Insulina + glucosa", ["Salbutamol nebulizado"]),
             ("Eliminar", "Horas", "Diurético, resinas", ["Diálisis si falla renal"]),
             ("Prevenir", "Después", "Revisar fármacos", ["IECA, espironolactona"])],
   "curvas": [("Potasio", ROSE, [0.95, 0.95, 0.75, 0.55, 0.4, 0.3, 0.3])],
   "chips_titulo": "Estabiliza el miocardio · marcado",
   "chips": [("Gluconato de calcio", True), ("Resinas", False), ("Furosemida", False), ("Hidrocortisona", False)]},
  ["El calcio no baja el potasio: solo protege el corazón por 30-60 min.",
   "Controlar glucosa tras la insulina.",
   "Con digoxina, dar el calcio con más cuidado."],
  "UK Kidney Association – Clinical practice guideline: hyperkalaemia (2023)")

# PED-215 · embudo
V("embudo", "PED-215", "lactante-neumonia-derrame-pleural-neumococo", "Neumonía con derrame en el lactante",
  "PEDIATRÍA ENAM: NEUMONÍA COMPLICADA", "PEDIATRÍA",
  ("Derrame paraneumónico en niños", ["El neumococo es el germen más frecuente",
   "S. aureus sigue en frecuencia (neumatoceles, empiema)"]),
  ("Lactante con neumonía bacteriana", ["Derrame pleural", "¿Germen más frecuente?"]),
  {"rotulo": "Embudo de gérmenes",
   "inicio": "Neumonía con derrame en lactante",
   "candidatos": ["S. pneumoniae", "H. influenzae", "Klebsiella", "Moraxella"],
   "pasos": [("Vacuna contra Hib en el esquema", ["H. influenzae"]),
             ("Klebsiella: adultos alcohólicos; Moraxella: otitis, sinusitis", ["Klebsiella", "Moraxella"])],
   "final": ("STREPTOCOCCUS PNEUMONIAE", ["Ampicilina o ceftriaxona EV", "Drenar si es empiema"]),
   "nota": "Con neumatoceles o tras varicela/sarampión, pensar en S. aureus."},
  ["Ecografía para cuantificar el derrame.",
   "Tubo de drenaje si es purulento, tabicado o grande.",
   "La vacuna antineumocócica reduce estas complicaciones."],
  "BTS – Guidelines for the management of pleural infection in children (2005) · " + NELSON)

# SP-163 · fases
V("fases", "SP-163", "perdidas-seguimiento-menor-muestra-mas-error-beta", "Pérdidas de seguimiento y potencia",
  "SALUD PÚBLICA ENAM: ERROR TIPO II", "SALUD PÚBLICA",
  ("Error tipo II (β)", ["No detectar una diferencia que sí existe (falso negativo)",
   "Depende del tamaño de muestra: si baja n, sube β"]),
  ("Estudio prospectivo", ["Algunos sujetos se pierden o abandonan", "¿Qué pasa con el error tipo II?"]),
  {"rotulo": "Cadena de efectos", "ans": 3,
   "fases": [("Pérdidas", "Seguimiento", "Abandonos", ["Sujetos que se van"]),
             ("Muestra", "n baja", "Menos datos", ["Menos precisión"]),
             ("Potencia", "1 − β", "Disminuye", ["Cuesta ver diferencias"]),
             ("Error β", "Resultado", "SE INCREMENTA", ["Más falsos negativos"])],
   "curvas": [("Potencia", SKY, [0.9, 0.85, 0.7, 0.55, 0.45, 0.35, 0.3]),
              ("Error β", ROSE, [0.1, 0.15, 0.3, 0.45, 0.55, 0.65, 0.7])],
   "chips_titulo": "Error tipo II · marcado el correcto",
   "chips": [("Se incrementa", True), ("Disminuye", False), ("Se mantiene", False), ("Es aleatorio", False)]},
  ["El error tipo I (α) lo fija el investigador (0,05).",
   "Las pérdidas también pueden introducir sesgo si no son al azar.",
   "Calcular la muestra previendo 10-20 % de pérdidas."],
  GORDIS)

# NRL-056 · embudo
V("embudo", "NRL-056", "otorragia-hematoma-temporal-hemicara-flacida-vii-par", "Parálisis facial tras un golpe temporal",
  "NEUROLOGÍA ENAM: FRACTURA DEL HUESO TEMPORAL", "NEUROLOGÍA",
  ("Fractura del temporal", ["Otorragia, hematoma retroauricular o temporal",
   "El nervio facial pasa por el hueso: parálisis facial periférica"]),
  ("Varón de 30 años tras accidente de tránsito", ["Pérdida transitoria de conciencia · Glasgow 13", "Otorragia, hematoma temporal derecho, hemicara derecha flácida sin surcos"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Déficit de par craneal tras TEC",
   "candidatos": ["VII par", "VIII par", "III par", "II par"],
   "pasos": [("Hemicara flácida sin surcos: motor de la cara", ["VIII par"]),
             ("Pupilas y visión no descritas como alteradas", ["III par", "II par"])],
   "final": ("VII PAR (FACIAL)", ["TC de peñasco", "Corticoides; cirugía si es inmediata y completa"]),
   "nota": "Las fracturas transversales del peñasco dañan más el facial que las longitudinales."},
  ["Parálisis facial periférica: toda la hemicara, incluida la frente.",
   "Si también hay hipoacusia, se afectó el VIII par.",
   "Proteger el ojo del lado afectado."],
  ATLS + " · Cummings Otolaryngology 7.ª ed. (2020)")

# CAR-069 · radial
V("radial", "CAR-069", "icc-fevi-35-ieca-reduce-mortalidad", "Tratamiento que reduce mortalidad en la IC",
  "CARDIOLOGÍA ENAM: INSUFICIENCIA CARDIACA CON FEVI REDUCIDA", "CARDIOLOGÍA",
  ("IC con FEVI reducida (≤ 40 %)", ["Cuatro pilares reducen la mortalidad",
   "IECA/ARA II/ARNI, betabloqueador, antialdosterónico e iSGLT2"]),
  ("Varón de 65 años con HTA y DM2", ["Fatiga, disnea, yugulares ingurgitadas, hepatomegalia, edema", "Cardiomegalia · FEVI 35 %"]),
  {"rotulo": "Mapa del tema", "centro": "IC-FEr", "centro_sub": "¿Qué baja la mortalidad?", "ans": 0,
   "items": [("IECA (o ARNI)", ["Reduce mortalidad", "Enalapril, sacubitrilo-valsartán"]),
             ("Betabloqueador", ["Carvedilol, bisoprolol"]),
             ("Antialdosterónico", ["Espironolactona"]),
             ("iSGLT2", ["Dapagliflozina"]),
             ("Diuréticos de asa", ["Solo alivian síntomas"])],
   "ruta": ["FEVI 35 %", "Activación neurohormonal", "Bloquearla", "IECA"]},
  ["La digoxina reduce hospitalizaciones, no la mortalidad.",
   "Anticoagular solo si hay FA o trombo.",
   "Subir las dosis hasta el máximo tolerado."],
  "ESC – Guidelines for heart failure (2021; actualización 2023) · AHA/ACC/HFSA (2022)")

# TRA-049 · embudo
V("embudo", "TRA-049", "adolescente-hombros-desiguales-adams-escoliosis", "Espalda asimétrica en la adolescente",
  "TRAUMATOLOGÍA ENAM: ESCOLIOSIS", "TRAUMATOLOGÍA",
  ("Escoliosis idiopática del adolescente", ["Curva lateral con rotación de la columna",
   "Test de Adams: giba costal al inclinarse hacia adelante"]),
  ("Adolescente mujer con dolor ocasional de espalda", ["Hermano con problemas de columna", "Hombros desiguales, tronco desplazado, Adams (+)"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Asimetría de espalda en la adolescente",
   "candidatos": ["Escoliosis", "Tumor medular", "Hernia discal", "Espondilosis"],
   "pasos": [("Sin dolor nocturno ni déficit neurológico", ["Tumor medular"]),
             ("Deformidad con giba al flexionar; edad joven", ["Hernia discal", "Espondilosis"])],
   "final": ("ESCOLIOSIS", ["Rx de columna completa: ángulo de Cobb", "< 25° observar · 25-40° corsé · > 45° cirugía"]),
   "nota": "Escoliosis dolorosa o con curva a la izquierda: buscar causa secundaria."},
  ["Más frecuente en niñas y con antecedente familiar.",
   "Progresa sobre todo durante el estirón puberal.",
   "El test de Adams es el tamizaje escolar."],
  "SRS – Adolescent idiopathic scoliosis (2023) · " + NELSON)

# PSI-041 · radial
V("radial", "PSI-041", "joven-cree-hermanos-envian-ruido-envenenamiento-paranoide", "Tipos de psicosis",
  "PSIQUIATRÍA ENAM: PSICOSIS PARANOIDE", "PSIQUIATRÍA",
  ("Psicosis paranoide", ["Predominan delirios de persecución y perjuicio",
   "Interpreta hechos neutros como ataques (autorreferencia), teme ser envenenada"]),
  ("Mujer de 18 años con familia disfuncional", ["Cree que sus hermanos hablan mal de ella y le envían el ruido de un avión", "No come por miedo a ser envenenada"]),
  {"rotulo": "Mapa del tema", "centro": "PSICOSIS", "centro_sub": "Según lo que predomina", "ans": 0,
   "items": [("PARANOIDE", ["Persecución, perjuicio", "Temor al envenenamiento"]),
             ("Catatónica", ["Inmovilidad, negativismo"]),
             ("Confusional", ["Desorientación, causa orgánica"]),
             ("Desorganizada", ["Lenguaje y conducta caóticos"]),
             ("Afectiva", ["Manía o depresión"])],
   "ruta": ["Ideas de perjuicio", "Autorreferencia", "Miedo a ser envenenada", "PARANOIDE"]},
  ["Descartar consumo de sustancias y causas orgánicas.",
   "Tratamiento: antipsicóticos y apoyo familiar.",
   "Si dura ≥ 6 meses con deterioro: esquizofrenia."],
  "APA – DSM-5-TR (2022) · APA – Guideline for schizophrenia (2020)")

# SP-164 · matriz
V("matriz", "SP-164", "30-muertes-menores-1-ano-600-nacidos-tmi-50", "Tasas de la población infantil",
  "SALUD PÚBLICA ENAM: MORTALIDAD INFANTIL", "SALUD PÚBLICA",
  ("Tasa de mortalidad infantil", ["Muertes de menores de 1 año / nacidos vivos × 1000",
   "30 / 600 × 1000 = 50"]),
  ("Distrito de 30 000 habitantes", ["600 nacidos vivos en el año", "30 murieron antes de cumplir un año"]),
  {"rotulo": "Indicador y cálculo", "eje_x": "Rasgo", "eje_y": "Indicador",
   "cols": ["Fórmula", "Resultado"], "rows": ["Mortalidad infantil", "Natalidad", "Mortalidad neonatal"], "caso": (0, 1),
   "cells": [[("< 1 año / nacidos vivos", ["× 1000"]), ("50 POR 1000", ["30 / 600"])],
             [("Nacidos vivos / población", ["× 1000"]), ("20 por 1000", ["600 / 30 000"])],
             [("< 28 días / nacidos vivos", []), ("Falta dato", [])]]},
  ["El denominador es nacidos vivos, no la población total.",
   "Es un indicador sensible de desarrollo y acceso a salud.",
   "La mayor parte de muertes infantiles son neonatales."],
  GORDIS)

# PED-216 · puntaje
V("puntaje", "PED-216", "lactante-convulsion-20-min-antibiotico-previo-puncion-lumbar", "Convulsión febril que no es simple",
  "PEDIATRÍA ENAM: PUNCIÓN LUMBAR EN LA CONVULSIÓN FEBRIL", "PEDIATRÍA",
  ("Convulsión febril compleja", ["Dura > 15 minutos, focal o repetida",
   "Antibiótico previo o vacunas incompletas pueden ocultar una meningitis"]),
  ("Lactante de 10 meses con fiebre de 39 °C", ["Convulsión de ~20 minutos, ahora postictal", "3 días de antibiótico automedicado · vacunas incompletas"]),
  {"rotulo": "Indicaciones de punción lumbar", "escala": "Criterios del caso", "total": 3, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Indicada la punción lumbar",
   "items": [("Crisis compleja (> 15 min)", "✓", True), ("Antibiótico previo (enmascara)", "✓", True),
             ("6-12 meses con vacunas incompletas", "✓", True), ("Signos meníngeos", "—", False)],
   "bandas": [("0", "Convulsión simple", "Bajar la fiebre, observar", False),
              ("≥ 1", "Sospecha de meningitis", "Punción lumbar", True)]},
  ["Si hay hipertensión endocraneana o inestabilidad, tratar antes de puncionar.",
   "El EEG y la TC no son la conducta inicial.",
   "Iniciar antibiótico empírico si la punción se retrasa."],
  "AAP – Clinical practice guideline: febrile seizures (2011) · " + NELSON)

# GIN-223 · termómetro
V("termometro", "GIN-223", "prolapso-ba-mas-5-lvt-6-popq-estadio-iv", "Estadificación POP-Q",
  "GINECOLOGÍA ENAM: PROLAPSO GENITAL", "GINECOLOGÍA",
  ("Sistema POP-Q", ["Mide cada punto respecto al himen (0), en cm",
   "Estadio IV: el punto más prolapsado llega a ≥ longitud vaginal total − 2 cm"]),
  ("Mujer de 62 años con bulto vaginal", ["Ba en +5 · longitud vaginal total 6 cm", "Sin pérdida de orina"]),
  {"rotulo": "Estadio POP-Q",
   "niveles": [("I", "> 1 cm sobre el himen", ["Leve"]),
               ("II", "± 1 cm del himen", ["Llega al introito"]),
               ("III", "> +1 pero < LVT − 2", ["Sale del introito"]),
               ("IV", "≥ LVT − 2 (+4 aquí)", ["BA +5: EVERSIÓN", "Casi total"])],
   "caso_nivel": 3, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Cirugía reconstructiva u obliterante", ["Según deseo de vida sexual y salud"], True),
             (2, "Pesario", ["Si no puede operarse"], False),
             (3, "Estrógeno vaginal", ["Mejora la mucosa"], False)]},
  ["Con LVT de 6 cm, el límite del estadio IV es +4.",
   "Punto Ba: pared anterior (vejiga).",
   "Evaluar la función urinaria antes de operar."],
  "ICS – POP-Q standardization (Bump RC, 1996) · ACOG/AUGS – Practice Bulletin 214 (2019)")

# GIN-224 · fases
V("fases", "GIN-224", "macrosomico-diabetica-signo-tortuga-distocia-hombros", "Distocia de hombros",
  "OBSTETRICIA ENAM: DISTOCIA DE HOMBROS", "OBSTETRICIA",
  ("Distocia de hombros", ["El hombro anterior se atasca detrás del pubis tras salir la cabeza",
   "Signo de la tortuga: la cabeza sale y se retrae contra el periné"]),
  ("Gestante diabética de 40 semanas con feto macrosómico", ["En expulsivo", "Al salir la cabeza aparece el signo de la tortuga"]),
  {"rotulo": "Qué hacer paso a paso", "ans": 0,
   "fases": [("Reconocer", "Segundos", "SIGNO DE LA TORTUGA", ["Pedir ayuda, no traccionar"]),
             ("McRoberts", "1.ª maniobra", "Muslos al abdomen", ["+ presión suprapúbica"]),
             ("Internas", "Si falla", "Rubin, Woods", ["Rotar los hombros"]),
             ("Brazo posterior", "Si falla", "Extraerlo", ["Luego maniobras extremas"])],
   "curvas": [],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Distocia de hombros", True), ("Circular de cordón", False), ("Presentación compuesta", False), ("Distocia del estrecho inferior", False)]},
  ["Factores: macrosomía, diabetes, obesidad, parto instrumentado.",
   "Nunca presionar el fondo uterino.",
   "Complicación fetal: parálisis braquial de Erb."],
  "RCOG – Green-top Guideline 42: Shoulder dystocia (2012) · ACOG – Practice Bulletin 178 (2017)")

# CAR-070 · tarjetas
V("tarjetas", "CAR-070", "taquicardia-supraventricular-cronotropico-negativo-bisoprolol", "Efecto de los fármacos sobre la frecuencia",
  "CARDIOLOGÍA ENAM: EFECTO CRONOTRÓPICO NEGATIVO", "CARDIOLOGÍA",
  ("Efecto cronotrópico", ["Negativo: baja la frecuencia cardiaca",
   "Betabloqueadores (bisoprolol) bloquean el β1 del nodo sinusal"]),
  ("Varón de 68 años con taquicardia supraventricular", ["Episodio de palpitaciones", "¿Qué fármaco baja la frecuencia?"]),
  {"rotulo": "¿Qué hace cada fármaco?", "ans": 0, "cards": [
      {"titulo": "BISOPROLOL", "datos": [
          ("Receptor", "Bloquea β1", True), ("Frecuencia", "BAJA", True),
          ("Uso", "Control de frecuencia", False)],
       "pie": "Betabloqueador cardioselectivo"},
      {"titulo": "Dobutamina", "datos": [
          ("Receptor", "Estimula β1", False), ("Frecuencia", "Sube", False),
          ("Uso", "Shock cardiogénico", False)],
       "pie": "Inotrópico positivo"},
      {"titulo": "Dopamina", "datos": [
          ("Receptor", "D1, β1, α1", False), ("Frecuencia", "Sube", False),
          ("Uso", "Hipotensión", False)],
       "pie": "Vasopresor"},
      {"titulo": "Nifedipino", "datos": [
          ("Receptor", "Canal de calcio vascular", False), ("Frecuencia", "Sube (refleja)", False),
          ("Uso", "Hipertensión", False)],
       "pie": "Dihidropiridina"}]},
  ["Verapamilo y diltiazem también bajan la frecuencia.",
   "La furosemida no tiene efecto cronotrópico.",
   "Crisis de TSV: maniobras vagales y adenosina."],
  "ESC – Guidelines for supraventricular tachycardia (2019) · Goodman & Gilman 14.ª ed. (2023)")

# REU-063 · fases
V("fases", "REU-063", "artritis-reumatoide-persiste-con-aine-metotrexato", "Escalones de tratamiento en la artritis reumatoide",
  "REUMATOLOGÍA ENAM: METOTREXATO", "REUMATOLOGÍA",
  ("Tratamiento de la AR", ["Los AINE solo alivian el dolor; no frenan el daño",
   "El FAME de primera línea es el metotrexato, apenas se diagnostica"]),
  ("Mujer de 40 años con AR hace 12 meses", ["Persisten los síntomas con AINE"]),
  {"rotulo": "Escalones", "ans": 1,
   "fases": [("Síntomas", "Puente", "AINE, corticoide", ["Mientras actúa el FAME"]),
             ("1.ª línea", "Desde el diagnóstico", "METOTREXATO", ["+ ácido fólico"]),
             ("Combinar", "Si no llega a meta", "Otro FAME", ["Sulfasalazina, hidroxicloroquina"]),
             ("Biológico", "Si persiste", "Anti-TNF, otros", ["Rituximab, tocilizumab"])],
   "curvas": [("Actividad", ROSE, [0.9, 0.8, 0.55, 0.4, 0.3, 0.2, 0.15])],
   "chips_titulo": "Fármaco a añadir · marcado el correcto",
   "chips": [("Metotrexato", True), ("Hidroxicloroquina", False), ("Sulfasalazina", False), ("Rituximab", False)]},
  ["Controlar hemograma y transaminasas; evitar alcohol.",
   "Teratógeno: anticoncepción eficaz.",
   "Meta: remisión o baja actividad (treat to target)."],
  "ACR – Guideline for the treatment of rheumatoid arthritis (2021) · EULAR (2022)")

# GAS-071 · embudo
V("embudo", "GAS-071", "suero-lechoso-dolor-epigastrico-hipertrigliceridemia-lipasa", "Pancreatitis con suero lechoso",
  "GASTROENTEROLOGÍA ENAM: PANCREATITIS POR HIPERTRIGLICERIDEMIA", "GASTROENTEROLOGÍA",
  ("Pancreatitis por triglicéridos", ["Triglicéridos > 1000 mg/dl: suero lechoso",
   "La amilasa puede salir falsamente normal; la lipasa es más fiable"]),
  ("Varón de 41 años sin alcohol ni cálculos", ["24 h de dolor epigástrico irradiado a flancos", "Suero de aspecto lechoso"]),
  {"rotulo": "Embudo de exámenes",
   "inicio": "Sospecha de pancreatitis",
   "candidatos": ["Lipasa", "Amilasa", "CPK-MB", "Electroforesis de Hb"],
   "pasos": [("CPK-MB y electroforesis no evalúan el páncreas", ["CPK-MB", "Electroforesis de Hb"]),
             ("Suero lipémico interfiere con la amilasa", ["Amilasa"])],
   "final": ("LIPASA", ["Más específica y confiable aquí", "Medir triglicéridos"]),
   "nota": "Tratamiento: ayuno, líquidos, insulina EV; plasmaféresis si es grave."},
  ["Tercera causa de pancreatitis tras cálculos y alcohol.",
   "Prevención: fibratos, dieta, control de la diabetes.",
   "Buscar diabetes descompensada, alcohol, fármacos."],
  "ACG – Management of acute pancreatitis (2024) · Endocrine Society – Hypertriglyceridemia guideline (2012)")
