"""Bloque 6 · parte L."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
DSM = "APA – DSM-5-TR (2022)"

# INF-068 · puntaje
V("puntaje", "INF-068", "vih-tar-3-semanas-fiebre-adenopatias-reconstitucion-inmune", "Síndrome de reconstitución inmune",
  "INFECTOLOGÍA ENAM: SÍNDROME DE RECONSTITUCIÓN INMUNE", "INFECTOLOGÍA",
  ("Síndrome inflamatorio de reconstitución inmune (IRIS)", ["Semanas después de iniciar TAR: la inmunidad recuperada «descubre» infecciones",
   "Empeoramiento clínico mientras mejoran CD4 y carga viral"]),
  ("Varón de 32 años con VIH, CD4 70", ["3 semanas tras iniciar TAR: fiebre y adenopatías", "CD4 140 · carga viral de 1 millón a 900"]),
  {"rotulo": "Criterios de IRIS en el caso", "escala": "IRIS", "total": 4, "max": 4,
   "total_label": "Criterios presentes",
   "interpreta": "Síndrome de reconstitución inmune",
   "items": [("TAR iniciado hace pocas semanas", "1", True), ("Caída de la carga viral", "1", True),
             ("Aumento de CD4 (70 → 140)", "1", True), ("Inflamación nueva: fiebre, adenopatías", "1", True)],
   "bandas": [("0-2", "Poco probable", "Buscar infección nueva o toxicidad", False),
              ("≥ 3", "IRIS", "Continuar TAR; buscar TB o MAC; AINE o corticoide", True)]},
  ["No suspender el TAR salvo que el IRIS sea grave.",
   "Micobacterias (TB, MAC) y criptococo son causas frecuentes.",
   "Mayor riesgo con CD4 muy bajos al iniciar."],
  "DHHS – Adult and adolescent ARV guidelines (2024) · MINSA – NTS N.° 204-MINSA/DGIESP-2023 (VIH)")

# NEU-037 · puntaje
V("puntaje", "NEU-037", "neumonia-69-anos-fr-32-curb65-2-hospitalizar", "Neumonía: CURB-65",
  "NEUMOLOGÍA ENAM: GRAVEDAD DE LA NEUMONÍA", "NEUMOLOGÍA",
  ("CURB-65", ["Confusión, urea, FR ≥ 30, PA baja, edad ≥ 65",
   "Puntaje 2: hospitalizar en sala general"]),
  ("Varón de 69 años con neumonía de lóbulo medio", ["FR 32, PA 110/75, SatO₂ 94%", "Orientado · urea no alterada"]),
  {"rotulo": "CURB-65 en el caso", "escala": "CURB-65", "total": 2, "max": 5,
   "total_label": "Puntaje del caso",
   "interpreta": "Riesgo intermedio",
   "items": [("Confusión", "1", False), ("Urea > 42 mg/dL", "1", False), ("FR ≥ 30", "1", True),
             ("PAS < 90 o PAD ≤ 60", "1", False), ("Edad ≥ 65 años", "1", True)],
   "bandas": [("0-1", "Bajo", "Tratamiento ambulatorio", False),
              ("2", "Intermedio", "HOSPITALIZAR EN MEDICINA", True),
              ("3-5", "Alto", "Hospitalizar; UCI si 4-5", False)]},
  ["CRB-65 (sin urea) sirve en el primer nivel.",
   "Criterios de UCI: choque, ventilación mecánica o criterios menores ATS.",
   "Tratamiento hospitalario: betalactámico + macrólido."],
  "BTS – Guidelines for CAP in adults (2009, act. 2015) · ATS/IDSA – CAP in adults (2019)")

# TRA-026 · matriz
V("matriz", "TRA-026", "herida-compartimento-anterior-pie-caido-peroneo", "Nervios de la pierna",
  "TRAUMATOLOGÍA ENAM: LESIÓN DEL NERVIO PERONEO", "TRAUMATOLOGÍA",
  ("Nervio peroneo profundo", ["Inerva el compartimento anterior: dorsiflexión del pie",
   "Su lesión produce «pie caído» y marcha en estepaje"]),
  ("Varón de 45 años con herida punzocortante", ["Compartimento anterior de la pierna derecha", "Parestesias y pie caído"]),
  {"rotulo": "Función de cada nervio", "eje_x": "Función", "eje_y": "Nervio",
   "cols": ["Motor", "Sensibilidad"], "rows": ["Peroneo profundo", "Peroneo superficial", "Tibial", "Safeno"], "caso": (0, 0),
   "cells": [[("DORSIFLEXIÓN", ["Pie caído si se lesiona"]), ("1.er espacio interdigital", [])],
             [("Eversión", []), ("Dorso del pie", [])],
             [("Flexión plantar", ["Inversión"]), ("Planta del pie", [])],
             [("Ninguno", []), ("Cara medial de la pierna", [])]]},
  ["El peroneo común rodea la cabeza del peroné: se lesiona por fracturas o yesos apretados.",
   "Marcha en estepaje: levanta mucho la rodilla.",
   "Ortesis tobillo-pie mientras se recupera."],
  "Moore – Anatomía con orientación clínica 9.ª ed. (2022)")

# GIN-136 · puntaje
V("puntaje", "GIN-136", "tres-abortos-tvp-anti-b2-glicoproteina", "Síndrome antifosfolípido",
  "OBSTETRICIA ENAM: SÍNDROME ANTIFOSFOLÍPIDO", "OBSTETRICIA",
  ("Síndrome antifosfolípido", ["Clínica (trombosis o pérdidas gestacionales) + anticuerpos",
   "Confirmar con anti-β2 glicoproteína I, anticardiolipina o anticoagulante lúpico"]),
  ("Multigesta de 12 semanas", ["3 abortos consecutivos < 10 semanas", "TVP hace un año"]),
  {"rotulo": "Criterios de Sydney en el caso", "escala": "Sydney", "total": 2, "max": 5,
   "total_label": "Criterios presentes",
   "interpreta": "Clínica positiva: falta el laboratorio",
   "items": [("Trombosis venosa", "1", True), ("≥ 3 abortos < 10 semanas", "1", True),
             ("Anticoagulante lúpico", "1", False), ("Anticardiolipina", "1", False),
             ("Anti-β2 glicoproteína I", "1", False)],
   "bandas": [("Clínica", "Sospecha", "PEDIR ANTICUERPOS (anti-β2GPI y otros)", True),
              ("Clín. + lab.", "SAF confirmado", "Heparina + aspirina en el embarazo", False)]},
  ["Los anticuerpos deben repetirse positivos a las 12 semanas.",
   "Con trombosis previa: heparina a dosis terapéutica.",
   "La warfarina es teratogénica: cambiar a heparina."],
  "Miyakis et al. – Sydney criteria for APS (J Thromb Haemost 2006) · ACR/EULAR – APS classification criteria (2023)")

# GIN-137 · puntaje
V("puntaje", "GIN-137", "oligomenorrea-acne-acantosis-hirsutismo-ovario-poliquistico", "Síndrome de ovario poliquístico",
  "GINECOLOGÍA ENAM: SÍNDROME DE OVARIO POLIQUÍSTICO", "GINECOLOGÍA",
  ("Síndrome hiperandrogénico (SOP)", ["Oligoanovulación + hiperandrogenismo ± ovarios poliquísticos",
   "Asociado a obesidad y resistencia a la insulina (acantosis)"]),
  ("Mujer de 26 años que desea gestar", ["Oligomenorrea desde la menarquia · IMC 30", "Acné, hirsutismo, acantosis nigricans, acrocordones"]),
  {"rotulo": "Criterios de Rotterdam en el caso", "escala": "Rotterdam", "total": 2, "max": 3,
   "total_label": "Criterios presentes",
   "interpreta": "Síndrome de ovario poliquístico",
   "items": [("Oligo o anovulación", "1", True), ("Hiperandrogenismo clínico", "1", True),
             ("Ovarios poliquísticos en ecografía", "1", False)],
   "bandas": [("0-1", "No cumple", "Buscar otra causa", False),
              ("≥ 2", "SOP", "Bajar de peso; letrozol para ovular", True)]},
  ["Descartar hipotiroidismo, hiperprolactinemia e hiperplasia suprarrenal.",
   "Virilización (clitoromegalia, voz grave): pensar en tumor.",
   "Metformina mejora la resistencia a la insulina."],
  "International evidence-based guideline for PCOS (2023) · ESHRE/ASRM – Rotterdam consensus (2003)")

# PED-137 · tarjetas
V("tarjetas", "PED-137", "prematuro-27-semanas-oxigeno-3-meses-displasia", "Lactante prematuro dependiente de oxígeno",
  "PEDIATRÍA ENAM: DISPLASIA BRONCOPULMONAR", "PEDIATRÍA",
  ("Displasia broncopulmonar", ["Prematuro que sigue necesitando O₂ a las 36 semanas corregidas",
   "Por ventilación mecánica y oxígeno prolongados"]),
  ("Lactante de 3 meses con O₂ 2 L/min", ["27 semanas, 800 g · VM 9 días y VPP 33 días", "Rx: atrapamiento aéreo, cambios intersticiales"]),
  {"rotulo": "¿Qué enfermedad es?", "ans": 0, "cards": [
      {"titulo": "DISPLASIA BRONCOPULMONAR", "datos": [
          ("Edad", "Prematuro, meses", True), ("Rx", "Atrapamiento, intersticial", True),
          ("Clave", "O₂ a las 36 sem", True)],
       "pie": "VM y oxígeno prolongados"},
      {"titulo": "Membrana hialina", "datos": [
          ("Edad", "Primeras horas", False), ("Rx", "Vidrio esmerilado", False),
          ("Clave", "Falta de surfactante", False)],
       "pie": "Mejora en días"},
      {"titulo": "Fibrosis quística", "datos": [
          ("Edad", "Lactancia, niñez", False), ("Rx", "Bronquiectasias", False),
          ("Clave", "Íleo meconial, desnutrición", False)],
       "pie": "Test del sudor"},
      {"titulo": "Traqueomalacia", "datos": [
          ("Edad", "Lactante", False), ("Rx", "Normal", False),
          ("Clave", "Estridor espiratorio", False)],
       "pie": "Mejora con la edad"}]},
  ["Complicación grave: hipertensión pulmonar.",
   "Palivizumab contra VSR en la temporada.",
   "Nutrición calórica alta y control del crecimiento."],
  "NICHD – BPD definition (Jensen 2019) · " + NELSON)

# HEM-026 · radial
V("radial", "HEM-026", "nino-cromosomopatia-leucemia-sindrome-down", "Síndrome de Down: riesgos",
  "HEMATOLOGÍA ENAM: LEUCEMIA EN SÍNDROME DE DOWN", "HEMATOLOGÍA",
  ("Síndrome de Down y leucemia", ["Riesgo 10-20 veces mayor de leucemia aguda",
   "LLA y LMA megacarioblástica (M7)"]),
  ("Niño de 3 años con cromosomopatía", ["Epistaxis, hematomas, pérdida de peso", "Diagnóstico de leucemia"]),
  {"rotulo": "Mapa del tema", "centro": "SÍNDROME DE DOWN", "centro_sub": "Trisomía 21", "ans": 0,
   "items": [("LEUCEMIA", ["LLA y LMA M7", "Riesgo 10-20 veces"]),
             ("Corazón", ["Canal auriculoventricular"]),
             ("Tiroides", ["Hipotiroidismo"]),
             ("Intestino", ["Atresia duodenal, Hirschsprung"]),
             ("Cerebro", ["Alzheimer precoz"])],
   "ruta": ["Trisomía 21", "Hematopoyesis anormal", "Mielopoyesis transitoria", "LEUCEMIA"]},
  ["Trastorno mieloproliferativo transitorio neonatal: puede preceder a la LMA.",
   "Turner: coartación y cardiopatías; Klinefelter: cáncer de mama.",
   "Ecocardiograma en todo RN con síndrome de Down."],
  "AAP – Health supervision for children with Down syndrome (2022) · " + NELSON)

# REU-039 · embudo
V("embudo", "REU-039", "obrero-ulcera-labio-inferior-infiltrada-espinocelular", "Úlcera crónica del labio",
  "DERMATOLOGÍA ENAM: CARCINOMA ESPINOCELULAR DEL LABIO", "DERMATOLOGÍA",
  ("Carcinoma espinocelular del labio", ["Labio inferior expuesto al sol; sobre queilitis actínica",
   "Úlcera infiltrada que no cicatriza; puede dar metástasis ganglionares"]),
  ("Varón de 63 años, obrero de construcción", ["Úlcera de 2 cm en el labio inferior de 1 año", "Bordes irregulares, base infiltrada, costra"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Úlcera del labio inferior de 1 año",
   "candidatos": ["Espinocelular", "Queilitis actínica", "Herpes labial", "Linfoma cutáneo", "Basocelular"],
   "pasos": [("Úlcera de 1 año con base infiltrada", ["Queilitis actínica", "Herpes labial"]),
             ("Exposición solar crónica, lesión epitelial", ["Linfoma cutáneo"]),
             ("Labio inferior: el basocelular prefiere el superior", ["Basocelular"])],
   "final": ("CARCINOMA ESPINOCELULAR", ["Biopsia para confirmar", "Cirugía ± ganglios"]),
   "nota": "Palpar ganglios submentonianos y submandibulares."},
  ["Factores: sol, tabaco, VPH, inmunosupresión.",
   "Queilitis actínica: lesión precursora (tratarla).",
   "Protector solar labial en trabajadores al aire libre."],
  "NCCN – Squamous cell skin cancer (2024) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# CIR-074 · árbol
A("CIR-074", "arma-blanca-periumbilical-estable-exploracion-local", "Herida abdominal por arma blanca",
  "CIRUGÍA ENAM: TRAUMA ABDOMINAL PENETRANTE", "CIRUGÍA",
  ("Herida abdominal por arma blanca", ["Inestable, peritonitis o evisceración: laparotomía",
   "Estable: explorar localmente si la herida penetra la fascia"]),
  ("Varón de 28 años con herida de 2 horas", ["Estable · herida periumbilical de 2 cm", "Sin contractura, reacción peritoneal leve"]),
  Q("¿Inestable, peritonitis o evisceración?", [
      L("Sí", "Laparotomía exploratoria", ["Inmediata"]),
      Q("EXPLORACIÓN LOCAL DE LA HERIDA", [
          L("Viola la fascia", "Observación o laparoscopía", ["Examen seriado"], path=True),
          L("No penetra", "Cierre y alta", ["Tras observación"])],
        edge="No: estable", path=True)], path=True),
  ("Opciones en el paciente estable", [("Uso", True)], [
      ("Exploración local", ["Primer paso"]),
      ("TEM con contraste", ["Flanco o espalda"]),
      ("Laparoscopía", ["Duda de penetración"])]),
  ["El lavado peritoneal casi no se usa hoy.",
   "Arma de fuego abdominal: laparotomía casi siempre.",
   "No retirar objetos empalados fuera del quirófano."],
  ATLS + " · EAST – Evaluation and management of abdominal stab wounds (2018)")

# PED-138 · tarjetas
V("tarjetas", "PED-138", "tos-perruna-signo-campanario-parainfluenza", "Virus respiratorios en el niño",
  "PEDIATRÍA ENAM: CRUP", "PEDIATRÍA",
  ("Crup (laringotraqueítis)", ["Tos perruna, estridor y disfonía en 6 meses a 3 años",
   "Virus parainfluenza tipo 1: el más frecuente"]),
  ("Preescolar de 3 años", ["Rinorrea, fiebre y tos perruna de 12 horas", "Tiraje · Rx: signo del campanario"]),
  {"rotulo": "¿Qué virus es?", "ans": 0, "cards": [
      {"titulo": "PARAINFLUENZA", "datos": [
          ("Cuadro", "Crup", True), ("Rx", "Signo del campanario", True),
          ("Clave", "Tos perruna, estridor", True)],
       "pie": "Dexametasona ± adrenalina"},
      {"titulo": "VSR", "datos": [
          ("Cuadro", "Bronquiolitis", False), ("Rx", "Hiperinsuflación", False),
          ("Clave", "< 2 años, sibilancias", False)],
       "pie": "Soporte"},
      {"titulo": "Enterovirus y coxsackie", "datos": [
          ("Cuadro", "Herpangina, mano-pie-boca", False), ("Rx", "Normal", False),
          ("Clave", "Vesículas orales", False)],
       "pie": "Verano"},
      {"titulo": "Coronavirus", "datos": [
          ("Cuadro", "Resfriado común", False), ("Rx", "Normal", False),
          ("Clave", "Rinorrea", False)],
       "pie": "También puede dar crup"}]},
  ["Escala de Westley para la gravedad.",
   "Dexametasona oral 0.15-0.6 mg/kg dosis única.",
   "Adrenalina nebulizada si hay estridor en reposo."],
  "AAP – Croup (Pediatr Rev 2023) · " + NELSON)

# SP-097 · matriz
V("matriz", "SP-097", "internista-omite-interconsulta-negligencia", "Tipos de culpa médica",
  "SALUD PÚBLICA ENAM: NEGLIGENCIA", "SALUD PÚBLICA",
  ("Negligencia", ["Omisión de un deber o acto médico necesario",
   "No pedir una interconsulta indicada por comodidad"]),
  ("Mujer de 44 años con LES reagudizado", ["Se iniciarán corticoides a dosis altas", "El internista no pide interconsulta a psiquiatría"]),
  {"rotulo": "Formas de culpa", "eje_x": "Aspecto", "eje_y": "Tipo",
   "cols": ["Qué es", "Ejemplo"], "rows": ["Negligencia", "Imprudencia", "Impericia"], "caso": (0, 0),
   "cells": [[("OMISIÓN", ["No hace lo debido"]), ("No pedir la interconsulta", [])],
             [("Acción temeraria", ["Hace sin precaución"]), ("Operar sin condiciones", [])],
             [("Falta de pericia", ["Conocimiento o destreza"]), ("Técnica mal hecha", [])]]},
  ["Iatrogenia: daño por el acto médico, con o sin culpa.",
   "Los corticoides a dosis altas pueden causar psicosis.",
   "Documentar las decisiones en la historia clínica."],
  "CMP – Código de Ética y Deontología (2023) · Código Penal peruano, art. 124")

# PSI-027 · radial
V("radial", "PSI-027", "anorexia-adolescente-qt-largo", "Complicaciones de la anorexia",
  "PSIQUIATRÍA ENAM: COMPLICACIONES DE LA ANOREXIA", "PSIQUIATRÍA",
  ("Anorexia nerviosa: corazón", ["Desnutrición y alteraciones electrolíticas alargan el QT",
   "Riesgo de arritmias y muerte súbita"]),
  ("Adolescente de 14 años", ["1 año con pérdida de interés por comer", "Temor excesivo a engordar"]),
  {"rotulo": "Mapa del tema", "centro": "ANOREXIA", "centro_sub": "Complicaciones", "ans": 0,
   "items": [("QT LARGO", ["Arritmias, muerte súbita", "Hipopotasemia"]),
             ("Hipotensión", ["Ortostática, bradicardia"]),
             ("Amenorrea", ["Hipogonadismo"]),
             ("Osteoporosis", ["Estrógenos bajos"]),
             ("Realimentación", ["Hipofosfatemia"])],
   "ruta": ["Restricción calórica", "Desnutrición y electrolitos", "Repolarización alterada", "QT LARGO"]},
  ["ECG y electrolitos en todo paciente con anorexia.",
   "Síndrome de realimentación: fósforo, potasio y magnesio bajos.",
   "La mayor mortalidad de los trastornos psiquiátricos."],
  "APA – Practice guideline for eating disorders (2023) · " + DSM)

# GIN-138 · tarjetas
V("tarjetas", "GIN-138", "brca-paridad-satisfecha-salpinguectomia-bilateral", "Esterilización en portadora de BRCA",
  "GINECOLOGÍA ENAM: SALPINGUECTOMÍA OPORTUNISTA", "GINECOLOGÍA",
  ("Salpinguectomía bilateral", ["Anticoncepción definitiva que además reduce el riesgo de cáncer de ovario",
   "Muchos cánceres serosos se originan en la trompa"]),
  ("Mujer de 35 años con mutación BRCA", ["Paridad satisfecha", "Pide método definitivo"]),
  {"rotulo": "¿Qué procedimiento?", "ans": 0, "cards": [
      {"titulo": "SALPINGUECTOMÍA BILATERAL", "datos": [
          ("Anticoncepción", "Definitiva", True), ("Riesgo de ovario", "Lo reduce", True),
          ("Invasividad", "Laparoscópica simple", True)],
       "pie": "Oportunista"},
      {"titulo": "Ligadura tubárica", "datos": [
          ("Anticoncepción", "Definitiva", False), ("Riesgo de ovario", "Lo reduce poco", False),
          ("Invasividad", "Simple", False)],
       "pie": "Deja la trompa"},
      {"titulo": "Histerectomía", "datos": [
          ("Anticoncepción", "Definitiva", False), ("Riesgo de ovario", "No protege", False),
          ("Invasividad", "Mayor", False)],
       "pie": "Innecesaria"},
      {"titulo": "Omentectomía", "datos": [
          ("Anticoncepción", "No", False), ("Riesgo de ovario", "No", False),
          ("Invasividad", "Mayor", False)],
       "pie": "Solo en cáncer"}]},
  ["BRCA1: salpingo-ooforectomía reductora a los 35-40 años; BRCA2: 40-45.",
   "Vigilancia mamaria con RM desde los 25-30 años.",
   "Consejería genética a los familiares."],
  "ACOG – Committee Opinion N.° 774: Opportunistic salpingectomy (2019) · NCCN – Genetic/familial high-risk assessment (2024)")

# INF-069 · termómetro
V("termometro", "INF-069", "viaje-agua-no-embotellada-diarrea-acuosa-hidratacion", "Diarrea del viajero",
  "INFECTOLOGÍA ENAM: DIARREA DEL VIAJERO", "INFECTOLOGÍA",
  ("Diarrea del viajero", ["Casi siempre por E. coli enterotoxigénica; autolimitada",
   "Leve: solo hidratación oral"]),
  ("Varón de 21 años tras viajar a provincia", ["Diarrea acuosa sin sangre, 5 al día", "No interrumpe sus actividades · signos vitales normales"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "Tolerable", ["No altera actividades"]),
               ("Moderada", "Interfiere", ["Limita actividades"]),
               ("Grave", "Incapacitante", ["Disentería o fiebre alta"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "HIDRATACIÓN ORAL", ["Sales de rehidratación"], True),
             (2, "Loperamida ± azitromicina", ["Diarrea moderada"], False),
             (3, "Azitromicina", ["Grave o con sangre"], False)]},
  ["Loperamida no se usa si hay sangre o fiebre.",
   "Metronidazol solo si se confirma Giardia.",
   "Prevención: agua segura y lavado de manos."],
  "ISTM – Expert consensus on travelers' diarrhea (J Travel Med 2017) · CDC Yellow Book (2024)")

# PED-139 · termómetro
V("termometro", "PED-139", "neumonia-fiebre-persistente-toracocentesis-pus-tubo-fibrinoliticos", "Empiema en el niño",
  "PEDIATRÍA ENAM: EMPIEMA", "PEDIATRÍA",
  ("Empiema pleural", ["Neumonía con fiebre persistente pese al antibiótico",
   "Pus en la toracocentesis: tubo de tórax + fibrinolíticos"]),
  ("Escolar de 7 años con neumonía", ["5 días de ceftriaxona, sigue febril", "MV disminuido en base derecha · toracocentesis: pus"]),
  {"rotulo": "Etapas del empiema",
   "niveles": [("Exudativo", "Líquido claro", ["Antibiótico"]),
               ("Fibrinopur.", "Pus y tabiques", ["Drenar"]),
               ("Organizado", "Cáscara pleural", ["Cirugía"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Continuar antibiótico EV", ["Cubrir neumococo y S. aureus"], False),
             (2, "TUBO + FIBRINOLÍTICOS", ["Uroquinasa o alteplasa"], True),
             (3, "VATS o decorticación", ["Si falla el drenaje"], False)]},
  ["Toracocentesis repetidas no bastan para un empiema.",
   "Fibrinolíticos y VATS tienen resultados similares en niños.",
   "Evolución a largo plazo casi siempre buena."],
  "BTS – Guidelines for pleural infection in children (2005) · APSA – Empyema in children (2012)")

# NRL-039 · árbol
A("NRL-039", "hemiparesia-afasia-6-horas-trombectomia", "Ictus isquémico a las 6 horas",
  "NEUROLOGÍA ENAM: TROMBECTOMÍA MECÁNICA", "NEUROLOGÍA",
  ("Reperfusión en el ictus isquémico", ["Trombólisis EV hasta 4.5 horas",
   "Oclusión de gran vaso: trombectomía hasta 6 h (y hasta 24 h seleccionados)"]),
  ("Varón de 72 años con hemiparesia y afasia de 6 h", ["NIHSS 10 · TC sin hemorragia ni infarto extenso", "Estenosis carotídea izquierda del 80%"]),
  Q("¿Menos de 4.5 horas?", [
      L("Sí", "Trombólisis EV", ["Alteplasa o tenecteplasa"]),
      Q("¿Oclusión de gran vaso?", [
          L("Sí, < 24 h", "TROMBECTOMÍA MECÁNICA", ["± angioplastia carotídea"], path=True),
          L("No", "Antiagregación", ["Y prevención secundaria"])],
        edge="No: 6 horas", path=True)], path=True),
  ("Reperfusión", [("Trombólisis EV", False), ("Trombectomía", True)], [
      ("Ventana", ["< 4.5 h", "< 6 h (hasta 24 h)"]),
      ("Requisito", ["Sin hemorragia", "Oclusión de gran vaso"])]),
  ["No bajar la PA si no es > 185/110 antes de reperfundir.",
   "Luego: endarterectomía o stent carotídeo por la estenosis del 80%.",
   "Rehabilitación temprana tras estabilizar."],
  "AHA/ASA – Guidelines for the early management of acute ischemic stroke (2019, act. 2026)")

# GIN-139 · fases
V("fases", "GIN-139", "hemorragia-posparto-atonia-refractaria-balon", "Hemorragia posparto refractaria",
  "OBSTETRICIA ENAM: HEMORRAGIA POSPARTO", "OBSTETRICIA",
  ("Hemorragia posparto por atonía", ["Uterotónicos y compresión bimanual primero",
   "Si fallan: taponamiento con balón intrauterino"]),
  ("Puérpera inmediata tras feto macrosómico", ["Útero no contraído, 3 cm sobre el ombligo", "Oxitocina, ergometrina y misoprostol sin efecto"]),
  {"rotulo": "Escalones de la clave roja", "ans": 2,
   "fases": [("Inicio", "Minutos", "Uterotónicos", ["Oxitocina, ergometrina, misoprostol"]),
             ("Compresión", "Minutos", "Bimanual", ["Masaje uterino"]),
             ("Refractaria", "Si persiste", "BALÓN INTRAUTERINO", ["Puente a cirugía o traslado"]),
             ("Cirugía", "Si falla", "B-Lynch, histerectomía", ["Ligaduras vasculares"])],
   "curvas": [("Sangrado", ROSE, [0.6, 0.8, 0.85, 0.7, 0.4, 0.2, 0.1])],
   "chips_titulo": "Siguiente paso · marcado el correcto",
   "chips": [("Taponamiento con balón", True), ("Histerectomía", False), ("Ácido tranexámico", False), ("Embolización", False)]},
  ["Ácido tranexámico en las primeras 3 horas, junto al resto de medidas.",
   "En el primer nivel, el balón permite referir con menos sangrado.",
   "Causas: las «4 T» (tono, trauma, tejido, trombina)."],
  "OMS – Recomendaciones para la prevención y tratamiento de la HPP (2023) · MINSA – Guía de atención de emergencias obstétricas")

# NEU-038 · árbol
A("NEU-038", "neumonia-derrame-pleural-toracocentesis", "Neumonía con derrame pleural",
  "NEUMOLOGÍA ENAM: DERRAME PARANEUMÓNICO", "NEUMOLOGÍA",
  ("Derrame paraneumónico", ["Todo derrame significativo en neumonía se punciona",
   "El análisis decide si hay que drenar"]),
  ("Varón de 78 años con neumonía", ["Consolidación de lóbulo inferior izquierdo", "Derrame pleural izquierdo en la TC"]),
  Q("¿Derrame significativo?", [
      L("Sí", "TORACOCENTESIS", ["pH, glucosa, Gram, cultivo"], path=True),
      L("Mínimo", "Solo antibiótico", ["Vigilar"])], path=True),
  ("¿Cuándo colocar tubo?", [("Criterio", True)], [
      ("pH", ["< 7.2"]),
      ("Glucosa", ["< 60 mg/dL"]),
      ("Aspecto o Gram", ["Pus o Gram positivo"])]),
  ["Criterios de Light: exudado vs trasudado.",
   "Espirometría y difusión no aportan en la fase aguda.",
   "Empiema: tubo de tórax y antibiótico prolongado."],
  "BTS – Guideline for pleural disease (2023) · " + HARRISON)

# CAR-051 · fases
V("fases", "CAR-051", "losartan-hctz-pa-150-90-amlodipino", "HTA no controlada: siguiente paso",
  "CARDIOLOGÍA ENAM: TRIPLE TERAPIA ANTIHIPERTENSIVA", "CARDIOLOGÍA",
  ("Escalonamiento en HTA", ["ARA II + tiazida sin meta: agregar calcioantagonista",
   "Triple terapia: IECA/ARA II + tiazida + amlodipino"]),
  ("Mujer de 54 años con losartán e hidroclorotiazida", ["Buena adherencia y dieta hiposódica", "PA 150/90 · creatinina y potasio normales"]),
  {"rotulo": "Escalones", "ans": 1,
   "fases": [("Paso 1", "Inicio", "ARA II + tiazida", ["Dos fármacos"]),
             ("Paso 2", "Sin meta", "+ AMLODIPINO", ["Triple terapia"]),
             ("Paso 3", "Resistente", "+ Espironolactona", ["Si el K lo permite"])],
   "curvas": [("PA", ROSE, [0.9, 0.85, 0.7, 0.65, 0.5, 0.45, 0.4])],
   "chips_titulo": "Fármaco · marcado el correcto",
   "chips": [("Amlodipino", True), ("Clortalidona", False), ("Aliskiren", False), ("Hidralazina", False)]},
  ["No combinar IECA + ARA II + aliskiren.",
   "Clortalidona sería otro diurético de la misma clase.",
   "Preferir combinaciones en una sola pastilla."],
  "ESC/ESH – Guidelines for the management of arterial hypertension (2023) · AHA/ACC – High blood pressure guideline (2017, act. 2025)")

# PED-140 · puntaje
V("puntaje", "PED-140", "lactante-fimosis-fiebre-3-dias-urocultivo", "Fiebre sin foco en el lactante",
  "PEDIATRÍA ENAM: FIEBRE SIN FOCO", "PEDIATRÍA",
  ("Fiebre sin foco en el lactante", ["La infección urinaria es la infección bacteriana grave más frecuente",
   "Confirmar con urocultivo por sonda"]),
  ("Lactante varón de 11 meses", ["Fiebre de 3 días (39.5 °C) y vómitos", "Sin foco · fimosis"]),
  {"rotulo": "Riesgo de ITU en el varón", "escala": "Riesgo de ITU", "total": 4, "max": 4,
   "total_label": "Factores presentes",
   "interpreta": "Probabilidad alta de ITU",
   "items": [("No circuncidado (fimosis)", "1", True), ("Fiebre ≥ 39 °C", "1", True),
             ("Fiebre > 24 horas", "1", True), ("Sin otra fuente de fiebre", "1", True)],
   "bandas": [("0-1", "Riesgo bajo", "Observar", False),
              ("≥ 2", "Riesgo alto", "UROCULTIVO por sonda + examen de orina", True)]},
  ["La bolsa colectora solo sirve si sale negativa.",
   "Iniciar antibiótico tras tomar la muestra.",
   "Ecografía renal y vesical tras la primera ITU febril."],
  "AAP – UTI clinical practice guideline, 2-24 months (2011, reafirmado 2016) · " + NELSON)

# CIR-075 · embudo
V("embudo", "CIR-075", "punetazo-boca-nudillo-tendon-capsula-lavado-quirurgico", "Mordedura humana en el puño",
  "CIRUGÍA ENAM: MORDEDURA HUMANA", "CIRUGÍA",
  ("Mordedura de puño cerrado", ["Herida en el nudillo al golpear la boca: flora oral en la articulación",
   "Alto riesgo de artritis séptica: exploración y lavado quirúrgico"]),
  ("Varón de 18 años que golpeó a su agresor", ["Herida de 3 horas en el nudillo", "Afecta el tendón extensor y la cápsula del 2.º MCF"]),
  {"rotulo": "Embudo de conductas",
   "inicio": "Herida del nudillo por dientes",
   "candidatos": ["Lavado quirúrgico", "Solo AINE", "Cierre primario", "Vacuna y antibióticos", "Azitromicina"],
   "pasos": [("Compromete tendón y articulación", ["Solo AINE"]),
             ("Mordedura: no se cierra", ["Cierre primario"]),
             ("El antibiótico no reemplaza el lavado", ["Vacuna y antibióticos", "Azitromicina"])],
   "final": ("EXPLORACIÓN QUIRÚRGICA Y LAVADO", ["+ amoxicilina-clavulánico", "Antitetánica"]),
   "nota": "Gérmenes: Eikenella corrodens, estreptococos, S. aureus y anaerobios."},
  ["Explorar con la mano en puño para ver la lesión tendinosa.",
   "Inmovilizar en posición funcional y elevar.",
   "Control a las 24-48 h."],
  "IDSA – Skin and soft tissue infections: bite wounds (2014) · Green's Operative Hand Surgery 8.ª ed. (2022)")

# GIN-140 · fases
V("fases", "GIN-140", "cono-nic3-seguir-tamizaje-20-anos", "Seguimiento tras NIC 3",
  "GINECOLOGÍA ENAM: SEGUIMIENTO POSCONIZACIÓN", "GINECOLOGÍA",
  ("Tamizaje tras tratar NIC 2-3", ["El riesgo de cáncer sigue alto por décadas",
   "Continuar el tamizaje 20 años, aunque pase los 65"]),
  ("Mujer de 55 años con NIC 3", ["Tratada con cono cervical", "¿Hasta cuándo el tamizaje?"]),
  {"rotulo": "Después del cono", "ans": 3,
   "fases": [("Cono", "Año 0", "Tratamiento", ["Márgenes libres"]),
             ("Control", "6 y 12 meses", "Prueba VPH", ["± citología"]),
             ("Rutina", "Cada 3 años", "Tamizaje", ["Si es negativo"]),
             ("Duración", "20 AÑOS", "SEGUIR TAMIZANDO", ["Aunque pase los 65"])],
   "curvas": [],
   "chips_titulo": "Tiempo · marcado el correcto",
   "chips": [("20 años", True), ("15 años", False), ("Hasta los 65", False), ("Hasta los 60", False)]},
  ["ASCCP 2019 sugiere incluso 25 años de seguimiento.",
   "Tras histerectomía por NIC: seguir con citología de cúpula.",
   "Vacunar contra VPH también reduce recurrencias."],
  "ACS/ASCCP/ASCP – Screening guidelines for cervical cancer (2012) · ASCCP – Risk-based management consensus (2019)")

# CB-050 · fases
V("fases", "CB-050", "semanas-2-a-8-organogenesis-periodo-embrionario", "Periodos del desarrollo",
  "CIENCIAS BÁSICAS ENAM: PERIODO EMBRIONARIO", "CIENCIAS BÁSICAS",
  ("Periodo embrionario", ["De la 2.ª a la 8.ª semana tras la concepción",
   "Organogénesis: máximo riesgo de malformaciones estructurales"]),
  ("Pregunta de concepto", ["Periodo de la organogénesis", "(semanas 2 a 8)"]),
  {"rotulo": "Desarrollo prenatal", "ans": 1,
   "fases": [("Preimplantación", "Sem 0-2", "«Todo o nada»", ["Muere o sigue normal"]),
             ("Embrionario", "Sem 2-8", "ORGANOGÉNESIS", ["Malformaciones mayores"]),
             ("Fetal", "Sem 9 al parto", "Crecimiento", ["Defectos funcionales"])],
   "curvas": [("Riesgo", ROSE, [0.1, 0.5, 0.95, 0.8, 0.4, 0.25, 0.15])],
   "chips_titulo": "Periodo · marcado el correcto",
   "chips": [("Embrionario", True), ("Fetal", False), ("Preimplantación", False), ("Teratogénico", False)]},
  ["Semanas contadas desde la concepción (no desde la FUR).",
   "El SNC es sensible durante todo el embarazo.",
   "Evitar teratógenos antes de saber que está embarazada."],
  "Langman – Embriología médica 14.ª ed. (2019) · Moore – The Developing Human 11.ª ed. (2020)")

# PED-141 · termómetro
V("termometro", "PED-141", "neonato-48-h-pezones-planos-perdida-peso-hipernatremia", "Pérdida de peso en el neonato",
  "PEDIATRÍA ENAM: DESHIDRATACIÓN HIPERNATRÉMICA", "PEDIATRÍA",
  ("Deshidratación hipernatrémica neonatal", ["Lactancia insuficiente en los primeros días",
   "Pérdida de peso > 10%, orina y heces escasas, irritabilidad y letargia"]),
  ("Neonato de 48 horas", ["Madre primigesta con pezones planos", "Ictericia, llanto y letargia · pérdida de peso > 10%"]),
  {"rotulo": "Pérdida de peso",
   "niveles": [("< 7%", "Esperada", ["Lactancia adecuada"]),
               ("7-10%", "Vigilar", ["Evaluar la técnica"]),
               ("> 10%", "Excesiva", ["Riesgo de hipernatremia"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "SODIO SÉRICO", ["Confirma la hipernatremia"], True),
             (2, "Rehidratar lento", ["Bajar el Na ≤ 12 mEq/L al día"], False),
             (3, "Apoyo a la lactancia", ["Técnica y pezones"], False)]},
  ["Corregir rápido causa edema cerebral y convulsiones.",
   "Pesar a todo RN a los 3-5 días de vida.",
   "Diabetes insípida y Cushing no explican este cuadro."],
  "ABM – Clinical protocol #3: Supplementary feedings in the healthy term breastfed neonate (2017) · " + NELSON)

# CIR-076 · matriz
V("matriz", "CIR-076", "agua-hirviendo-manos-eritema-sin-ampollas-analgesia", "Quemaduras: grado y manejo",
  "CIRUGÍA ENAM: QUEMADURA DE PRIMER GRADO", "CIRUGÍA",
  ("Quemadura de primer grado (epidérmica)", ["Eritema doloroso sin ampollas",
   "Cura en días: solo analgesia oral e hidratante"]),
  ("Mujer de 25 años con agua hirviendo", ["Manos con eritema, sin flictenas ni ampollas", "Estable, motilidad conservada"]),
  {"rotulo": "Según la profundidad", "eje_x": "Aspecto", "eje_y": "Grado",
   "cols": ["Aspecto", "Tratamiento"], "rows": ["Primer grado", "2.º superficial", "2.º profundo", "Tercer grado"], "caso": (0, 1),
   "cells": [[("Eritema", ["Sin ampollas"]), ("ANALGESIA ORAL", ["Hidratante"])],
             [("Ampollas", ["Blanquea"]), ("Curación y apósito", [])],
             [("No blanquea", ["Menos dolor"]), ("Escisión e injerto", [])],
             [("Blanca, acartonada", ["Indolora"]), ("Injerto", [])]]},
  ["Primer grado no cuenta para el % de SCQ.",
   "Enfriar con agua corriente 20 minutos.",
   "Antibióticos no son necesarios."],
  "ABA – Advanced Burn Life Support Course (2022) · ISBI – Practice guidelines for burn care (2016)")

# TRA-027 · árbol
A("TRA-027", "escolar-pie-plano-flexible-sin-dolor-no-tratar", "Pie plano en el niño",
  "TRAUMATOLOGÍA ENAM: PIE PLANO FLEXIBLE", "TRAUMATOLOGÍA",
  ("Pie plano flexible", ["El arco aparece al ponerse de puntillas",
   "Sin dolor ni limitación: no requiere tratamiento"]),
  ("Escolar de 6 años con «pies chuecos»", ["Pie plano flexible", "Sin dolor ni limitación funcional"]),
  Q("¿Aparece el arco de puntillas?", [
      Q("¿Dolor o limitación?", [
          L("No", "NO REQUIERE TRATAMIENTO", ["Explicar y controlar"], path=True),
          L("Sí", "Plantillas blandas", ["Estiramientos"])],
        edge="Sí: flexible", path=True),
      L("No: rígido", "Estudiar", ["Coalición tarsal, astrágalo vertical"])], path=True),
  ("Flexible vs rígido", [("Flexible", True), ("Rígido", False)], [
      ("Arco de puntillas", ["Aparece", "No aparece"]),
      ("Conducta", ["Observar", "Rx y ortopedista"])]),
  ["Es normal hasta los 6-8 años.",
   "Las plantillas rígidas no forman el arco.",
   "Acortamiento del Aquiles: estiramientos."],
  "AAOS – Flexible flatfoot in children (OrthoInfo 2023) · Lovell and Winter's Pediatric Orthopaedics 8.ª ed. (2020)")

# CIR-077 · embudo
V("embudo", "CIR-077", "prolapso-hemorroidal-reduccion-manual-tercer-grado", "Grado de las hemorroides",
  "CIRUGÍA ENAM: HEMORROIDES DE TERCER GRADO", "CIRUGÍA",
  ("Hemorroides de tercer grado", ["Prolapsan con el esfuerzo y hay que reducirlas con la mano",
   "Tratamiento: ligadura con banda o hemorroidectomía"]),
  ("Varón de 30 años con estreñimiento", ["Sangrado rectal por 7 meses", "Tumoración que sale y la reduce manualmente"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Tumoración anal que se reduce con la mano",
   "candidatos": ["Tercer grado", "Primer grado", "Segundo grado", "Cuarto grado", "Prolapso rectal"],
   "pasos": [("Sale por el ano: prolapsa", ["Primer grado"]),
             ("No se reduce sola", ["Segundo grado"]),
             ("Se reduce con la mano; paquetes, no anillos", ["Cuarto grado", "Prolapso rectal"])],
   "final": ("TERCER GRADO", ["Reducción manual", "Ligadura o hemorroidectomía"]),
   "nota": "Fibra y agua para el estreñimiento, en todos los grados."},
  ["Cuarto grado: irreductible, riesgo de trombosis.",
   "Prolapso rectal: pliegues concéntricos.",
   "Descartar cáncer colorrectal si hay factores de riesgo."],
  "ASCRS – Clinical practice guidelines for the management of hemorrhoids (2018)")

# CIR-078 · tarjetas
V("tarjetas", "CIR-078", "epoc-coronario-fractura-radio-bloqueo-periferico", "Anestesia en paciente de alto riesgo",
  "CIRUGÍA ENAM: ANESTESIA REGIONAL", "CIRUGÍA",
  ("Bloqueo de nervio periférico", ["Anestesia solo del miembro operado",
   "Evita intubar y altera poco la hemodinamia: ideal en EPOC y coronarios"]),
  ("Adulto mayor de 70 años", ["EPOC sin tratamiento y cardiopatía coronaria", "Fractura expuesta de radio derecho"]),
  {"rotulo": "¿Qué anestesia conviene?", "ans": 0, "cards": [
      {"titulo": "BLOQUEO DE NERVIO PERIFÉRICO", "datos": [
          ("Vía aérea", "Sin intubar", True), ("Hemodinamia", "Estable", True),
          ("Uso", "Plexo braquial: brazo", True)],
       "pie": "Ideal en EPOC y coronarios"},
      {"titulo": "General balanceada", "datos": [
          ("Vía aérea", "Intubación", False), ("Hemodinamia", "Depresión cardiaca", False),
          ("Uso", "Cirugía mayor", False)],
       "pie": "Riesgo respiratorio en EPOC"},
      {"titulo": "Raquídea", "datos": [
          ("Vía aérea", "Sin intubar", False), ("Hemodinamia", "Hipotensión", False),
          ("Uso", "Abdomen inferior y piernas", False)],
       "pie": "No sirve para el brazo"},
      {"titulo": "Epidural", "datos": [
          ("Vía aérea", "Sin intubar", False), ("Hemodinamia", "Hipotensión", False),
          ("Uso", "Tórax, abdomen, piernas", False)],
       "pie": "No para el antebrazo"}]},
  ["Bloqueo supraclavicular o axilar para antebrazo y mano.",
   "Guiado por ecografía: más seguro y eficaz.",
   "Vigilar toxicidad por anestésico local."],
  "ASA – Practice advisory for regional anesthesia (2023) · Miller's Anesthesia 9.ª ed. (2020)")

# GAS-049 · puntaje
V("puntaje", "GAS-049", "hepatitis-c-ascitis-albumina-24-inr-17-cirrosis-descompensada", "Cirrosis: Child-Pugh",
  "GASTROENTEROLOGÍA ENAM: CIRROSIS DESCOMPENSADA", "GASTROENTEROLOGÍA",
  ("Cirrosis hepática descompensada", ["Ascitis, ictericia, hemorragia variceal o encefalopatía",
   "Hepatitis C crónica no tratada como causa"]),
  ("Varón de 58 años con hepatitis C", ["Ascitis moderada, edema, circulación colateral", "Albúmina 2.4, bilirrubina 3.1, INR 1.7, plaquetas 85 000"]),
  {"rotulo": "Child-Pugh en el caso", "escala": "Child-Pugh", "total": 12, "max": 15,
   "total_label": "Puntaje del caso",
   "interpreta": "Child-Pugh C: descompensada",
   "items": [("Bilirrubina 3.1 (> 3)", "3", True), ("Albúmina 2.4 (< 2.8)", "3", True),
             ("INR 1.7 (1.7-2.3)", "2", True), ("Ascitis moderada", "3", True),
             ("Sin encefalopatía", "1", True)],
   "bandas": [("5-6", "Child A", "Compensada", False),
              ("7-9", "Child B", "Descompensación inicial", False),
              ("10-15", "Child C", "Descompensada: evaluar trasplante", True)]},
  ["Tratar la hepatitis C con antivirales de acción directa.",
   "Tamizar hepatocarcinoma con ecografía cada 6 meses.",
   "MELD para priorizar trasplante."],
  "AASLD/IDSA – HCV guidance (2023) · EASL – Decompensated cirrhosis (2018)")

# SP-098 · matriz
V("matriz", "SP-098", "foda-baja-calidad-sin-recursos-debilidades", "Análisis FODA",
  "SALUD PÚBLICA ENAM: ANÁLISIS FODA", "SALUD PÚBLICA",
  ("Análisis FODA", ["Internos: fortalezas y debilidades · externos: oportunidades y amenazas",
   "Baja calidad y falta de recursos propios: debilidades"]),
  ("Médico jefe de un establecimiento", ["Servicios de baja calidad", "Sin recursos financieros"]),
  {"rotulo": "Matriz FODA", "eje_x": "Efecto", "eje_y": "Origen",
   "cols": ["Positivo", "Negativo"], "rows": ["Interno", "Externo"], "caso": (0, 1),
   "cells": [[("Fortalezas", ["Personal capacitado"]), ("DEBILIDADES", ["Baja calidad, sin dinero"])],
             [("Oportunidades", ["Convenios, programas"]), ("Amenazas", ["Epidemias, recortes"])]]},
  ["Lo interno la institución puede cambiarlo; lo externo no.",
   "Estrategias: usar fortalezas para aprovechar oportunidades.",
   "Base de la planificación estratégica."],
  "MINSA – Documento técnico de planeamiento estratégico · OPS – Gestión en salud")

# PED-142 · radial
V("radial", "PED-142", "prematuro-28-semanas-rop-saturacion-90-95", "Retinopatía del prematuro",
  "PEDIATRÍA ENAM: RETINOPATÍA DEL PREMATURO", "PEDIATRÍA",
  ("Retinopatía del prematuro", ["Vascularización anormal de la retina inmadura; el O₂ alto la favorece",
   "Mantener SatO₂ 90-95% y asegurar los controles oftalmológicos"]),
  ("RN de 28 semanas y 1200 g", ["Ventilación y oxígeno prolongados", "A las 35 semanas: ROP con progresión"]),
  {"rotulo": "Mapa del tema", "centro": "ROP", "centro_sub": "Retinopatía del prematuro", "ans": 0,
   "items": [("SATO₂ 90-95%", ["Evitar la hiperoxia", "+ controles continuos"]),
             ("Riesgo", ["< 32 sem o < 1500 g"]),
             ("Tamizaje", ["A las 4-6 semanas de vida"]),
             ("Tratamiento", ["Láser o anti-VEGF"]),
             ("Secuelas", ["Miopía, desprendimiento"])],
   "ruta": ["Prematuro de 28 semanas", "Oxígeno prolongado", "ROP que progresa", "SatO₂ 90-95% + CONTROLES"]},
  ["Saturaciones > 95% aumentan la ROP grave.",
   "No hay evidencia de que la EPO o los corticoides la eviten.",
   "Seguimiento oftalmológico hasta la vascularización completa."],
  "AAP/AAO – Screening examination of premature infants for ROP (2018) · " + NELSON)

# GAS-050 · embudo
V("embudo", "GAS-050", "vomitos-alcohol-hematemesis-mallory-weiss", "Hematemesis tras vómitos",
  "GASTROENTEROLOGÍA ENAM: SÍNDROME DE MALLORY-WEISS", "GASTROENTEROLOGÍA",
  ("Síndrome de Mallory-Weiss", ["Desgarro de la mucosa de la unión gastroesofágica",
   "Tras vómitos intensos, a menudo por alcohol"]),
  ("Varón de 30 años con hematemesis", ["Vómitos incoercibles el día anterior tras alcohol", "Estable, sin estigmas de hepatopatía"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Hematemesis tras vómitos",
   "candidatos": ["Mallory-Weiss", "Várices esofágicas", "Úlcera gástrica", "Gastritis erosiva", "Boerhaave"],
   "pasos": [("Vómitos intensos antes de sangrar", ["Úlcera gástrica", "Gastritis erosiva"]),
             ("Sin estigmas de hepatopatía", ["Várices esofágicas"]),
             ("Estable, sin dolor torácico ni enfisema", ["Boerhaave"])],
   "final": ("MALLORY-WEISS", ["Desgarro de la unión GE", "Suele ceder solo"]),
   "nota": "Endoscopia: terapia hemostática solo si sangra activamente."},
  ["Boerhaave: rotura transmural, dolor torácico y enfisema; es una emergencia.",
   "IBP y antieméticos.",
   "Mayoría no requiere transfusión."],
  "ACG – Upper GI and ulcer bleeding guideline (2021) · Sleisenger and Fordtran's 11.ª ed. (2021)")

# HEM-027 · radial
V("radial", "HEM-027", "lma-pronostico-citogenetica", "Pronóstico en leucemia mieloide aguda",
  "HEMATOLOGÍA ENAM: PRONÓSTICO DE LA LMA", "HEMATOLOGÍA",
  ("Factores pronósticos en LMA", ["La citogenética al diagnóstico es el más importante",
   "Define el riesgo (ELN) y la necesidad de trasplante"]),
  ("Pregunta de concepto", ["Factor pronóstico más importante", "al diagnóstico de LMA"]),
  {"rotulo": "Mapa del tema", "centro": "LMA", "centro_sub": "Factores pronósticos", "ans": 0,
   "items": [("CITOGENÉTICA", ["El más importante", "t(8;21), inv(16): favorable"]),
             ("Edad", ["> 60 años: peor"]),
             ("Leucocitos", ["Hiperleucocitosis"]),
             ("LMA secundaria", ["Tras mielodisplasia o quimio"]),
             ("Mutaciones", ["NPM1 +, FLT3-ITD −"])],
   "ruta": ["LMA al diagnóstico", "Cariotipo y genética", "Riesgo ELN", "CITOGENÉTICA"]},
  ["Cariotipo complejo, −5, −7 o TP53: riesgo adverso.",
   "t(15;17): leucemia promielocítica, excelente pronóstico con ATRA.",
   "Riesgo adverso: trasplante alogénico en primera remisión."],
  "ELN – Diagnosis and management of AML in adults (Blood 2022)")

# CIR-079 · fases
V("fases", "CIR-079", "quemado-50-taquicardia-fiebre-catabolismo-hipermetabolismo", "Metabolismo del gran quemado",
  "CIRUGÍA ENAM: HIPERMETABOLISMO DEL QUEMADO", "CIRUGÍA",
  ("Estado hipermetabólico", ["Catecolaminas, cortisol y citocinas elevan el metabolismo",
   "Taquicardia, fiebre, hiperglucemia y catabolismo proteico"]),
  ("Varón de 45 años con quemaduras del 50%", ["24 horas después, en reanimación", "Taquicardia, fiebre, hiperglucemia, catabolismo"]),
  {"rotulo": "Fases metabólicas", "ans": 1,
   "fases": [("Ebb", "0-48 h", "Hipometabolismo", ["Choque, gasto bajo"]),
             ("Flow", "Desde 24-48 h", "HIPERMETABOLISMO", ["Taquicardia, fiebre, catabolismo"]),
             ("Recuperación", "Meses", "Anabolismo", ["Hasta 2 años"])],
   "curvas": [("Metab.", ROSE, [0.4, 0.35, 0.7, 0.95, 0.9, 0.7, 0.5])],
   "chips_titulo": "Causa · marcada la correcta",
   "chips": [("Hipermetabolismo", True), ("Sepsis incipiente", False), ("Insuf. suprarrenal", False), ("Acidosis láctica", False)]},
  ["Nutrición enteral temprana y alta en proteínas.",
   "Propranolol y oxandrolona reducen el catabolismo.",
   "La fiebre del quemado no siempre es infección."],
  "ABA – Advanced Burn Life Support Course (2022) · Herndon – Total Burn Care 5.ª ed. (2018)")

# GAS-051 · puntaje
V("puntaje", "GAS-051", "anciano-perdida-peso-hematoquecia-anemia-colonoscopia", "Sospecha de cáncer colorrectal",
  "GASTROENTEROLOGÍA ENAM: CÁNCER COLORRECTAL", "GASTROENTEROLOGÍA",
  ("Cáncer colorrectal", ["Signos de alarma: edad, baja de peso, sangrado, anemia, cambio del hábito",
   "Examen inicial: colonoscopía completa con biopsia"]),
  ("Varón de 64 años", ["Cansancio, pérdida de 10 kg", "Estreñimiento, hematoquecia, palidez"]),
  {"rotulo": "Signos de alarma en el caso", "escala": "Alarma", "total": 5, "max": 5,
   "total_label": "Signos presentes",
   "interpreta": "Alta sospecha de cáncer",
   "items": [("Edad > 50 años", "1", True), ("Pérdida de peso (10 kg)", "1", True),
             ("Hematoquecia", "1", True), ("Anemia (palidez)", "1", True),
             ("Cambio del hábito intestinal", "1", True)],
   "bandas": [("0", "Sin alarma", "Manejo sintomático", False),
              ("≥ 1", "Alarma", "COLONOSCOPÍA completa con biopsia", True)]},
  ["TEM: para estadificar después de confirmar.",
   "El enema opaco ya no se usa para diagnóstico.",
   "CEA para seguimiento, no para diagnóstico."],
  "NCCN – Colon cancer (2024) · ACG – Colorectal cancer screening (2021)")

# PSI-028 · puntaje
V("puntaje", "PSI-028", "adolescente-miedo-engordar-distorsion-restriccion-anorexia", "Anorexia nerviosa: criterios",
  "PSIQUIATRÍA ENAM: ANOREXIA NERVIOSA", "PSIQUIATRÍA",
  ("Anorexia nerviosa", ["Restricción que lleva a bajo peso, miedo a engordar y distorsión de la imagen",
   "Los tres criterios son necesarios (DSM-5)"]),
  ("Adolescente de 13 años", ["Miedo intenso a ganar peso", "Percepción alterada de su peso · restricción de la ingesta"]),
  {"rotulo": "Criterios DSM-5 en el caso", "escala": "DSM-5", "total": 3, "max": 3,
   "total_label": "Criterios presentes",
   "interpreta": "Anorexia nerviosa",
   "items": [("Restricción que lleva a bajo peso", "1", True), ("Miedo intenso a engordar", "1", True),
             ("Alteración de la imagen corporal", "1", True)],
   "bandas": [("< 3", "No cumple", "Otro trastorno alimentario", False),
              ("3", "Anorexia nerviosa", "Equipo multidisciplinario; realimentación cuidadosa", True)]},
  ["Bulimia: atracones + conductas compensatorias con peso normal.",
   "Trastorno por evitación: sin miedo a engordar.",
   "Ya no se exige amenorrea en el DSM-5."],
  DSM + " · NICE – Eating disorders: recognition and treatment (2020)")
