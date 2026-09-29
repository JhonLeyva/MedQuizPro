"""Bloque 7 · parte B."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"

# HEM-031 · puntaje
V("puntaje", "HEM-031", "encamada-2-semanas-pierna-edematosa-tvp", "Pierna hinchada tras estar en cama",
  "HEMATOLOGÍA ENAM: TROMBOSIS VENOSA PROFUNDA", "HEMATOLOGÍA",
  ("Trombosis venosa profunda", ["Tríada de Virchow: estasis, daño endotelial, hipercoagulabilidad",
   "Edema unilateral doloroso tras inmovilización = TVP"]),
  ("Mujer de 69 años, 2 semanas en cama por neumonía", ["Edema y dolor a la palpación en la pierna derecha", "Aumenta con el movimiento"]),
  {"rotulo": "Escala de Wells para TVP", "escala": "Wells (TVP)", "total": 3, "max": 9,
   "total_label": "Puntaje del caso",
   "interpreta": "TVP probable: ecografía Doppler",
   "items": [("Encamado > 3 días o cirugía reciente", "1", True), ("Dolor en el trayecto venoso profundo", "1", True),
             ("Edema de toda la pierna", "1", True), ("Pantorrilla > 3 cm que la otra", "1", False),
             ("Cáncer activo", "1", False), ("TVP previa documentada", "1", False),
             ("Otro diagnóstico igual de probable", "−2", False)],
   "bandas": [("≤ 1", "Improbable", "Dímero D; si es negativo, se descarta", False),
              ("≥ 2", "Probable", "Ecografía Doppler de compresión", True)]},
  ["El linfedema es indoloro y crónico; las várices no dan edema agudo.",
   "Tratamiento: anticoagular con heparina de bajo peso o anticoagulante oral directo.",
   "Complicación temida: tromboembolismo pulmonar."],
  "ASH – Guidelines for management of venous thromboembolism (Blood Adv 2020) · NICE NG158 (2023)")

# CAR-055 · árbol
A("CAR-055", "hipertenso-captopril-tos-seca-retirar-ieca", "Tos seca en el hipertenso",
  "CARDIOLOGÍA ENAM: TOS POR IECA", "CARDIOLOGÍA",
  ("Tos por IECA", ["Los IECA impiden degradar la bradicinina, que irrita la vía aérea",
   "Tos seca persistente sin otra causa: retirar el IECA"]),
  ("Varón de 62 años con captopril y amlodipino", ["Tos seca intermitente", "Neumología y ORL sin hallazgos"]),
  Q("¿Recibe un IECA?", [
      Q("¿Otra causa descartada?", [
          L("Sí", "RETIRAR CAPTOPRIL", ["Cambiar a ARA II (losartán)", "La tos cede en 1-4 semanas"], path=True),
          L("No", "Estudiar asma, ERGE, goteo", ["Rx de tórax"])],
        edge="Sí", path=True),
      L("No", "Tos crónica", ["Asma, ERGE, rinorrea posterior"])], path=True),
  ("Efectos adversos de los antihipertensivos", [("IECA", True), ("Amlodipino", False), ("ARA II", False)], [
      ("Típico", ["Tos seca, angioedema", "Edema maleolar", "Hiperpotasemia"]),
      ("Tos", ["5-35 %", "No", "Muy rara"])]),
  ["Los antitusígenos y mucolíticos no quitan la tos por IECA.",
   "El angioedema por IECA contraindica también su reintroducción.",
   "El amlodipino no produce tos."],
  "ESH – Guidelines for the management of arterial hypertension (2023)")

# HEM-032 · radial
V("radial", "HEM-032", "pancitopenia-fiebre-equimosis-farmacos-mielotoxicos", "Pancitopenia: qué preguntar",
  "HEMATOLOGÍA ENAM: PANCITOPENIA", "HEMATOLOGÍA",
  ("Pancitopenia adquirida", ["Baja de las tres series: infección, sangrado y anemia",
   "Primero buscar fármacos o tóxicos que dañen la médula"]),
  ("Mujer de 44 años con equimosis y neumonía", ["Fiebre 38,4 °C y crepitantes bilaterales", "Leucocitos 1400 · Hb 7,2 · plaquetas 35 000"]),
  {"rotulo": "Mapa del tema", "centro": "PANCITOPENIA", "centro_sub": "Causas adquiridas", "ans": 0,
   "items": [("FÁRMACOS MIELOTÓXICOS", ["Cloranfenicol, metamizol, antitiroideos", "Quimioterapia, AINE"]),
             ("Anemia aplásica", ["Autoinmune, médula vacía"]),
             ("Leucemia aguda", ["Blastos en sangre"]),
             ("Déficit de B12 o folato", ["VCM alto"]),
             ("Hiperesplenismo", ["Bazo grande, cirrosis"])],
   "ruta": ["Tres series bajas", "Infección y sangrado", "Anamnesis dirigida", "FÁRMACOS"]},
  ["La neutropenia febril es una emergencia: antibióticos de amplio espectro.",
   "El mielograma y la biopsia de médula confirman la causa.",
   "Suspender el fármaco sospechoso de inmediato."],
  "British Society for Haematology – Guidelines for the diagnosis and management of adult aplastic anaemia (2024) · " + HARRISON)

# CAR-056 · embudo
V("embudo", "CAR-056", "fiebre-2-meses-soplo-mitral-hemiparesia-endocarditis", "Fiebre, soplo y déficit neurológico",
  "CARDIOLOGÍA ENAM: ENDOCARDITIS INFECCIOSA CON EMBOLIA", "CARDIOLOGÍA",
  ("Endocarditis infecciosa", ["Fiebre prolongada + soplo + embolia = endocarditis hasta demostrar lo contrario",
   "Las vegetaciones se desprenden y ocluyen arterias cerebrales"]),
  ("Varón de 35 años con fiebre reumática de niño", ["2 meses de fiebre y baja de peso", "Hemiparesia izquierda aguda · soplo mitral · ritmo regular"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Déficit motor agudo en un joven con soplo",
   "candidatos": ["Endocarditis", "Fibrilación auricular", "Fiebre reumática", "S. antifosfolipídico"],
   "pasos": [("Ritmo regular en el examen", ["Fibrilación auricular"]),
             ("Fiebre de 2 meses con baja de peso en un adulto", ["Fiebre reumática", "S. antifosfolipídico"])],
   "final": ("ENDOCARDITIS INFECCIOSA", ["3 hemocultivos antes del antibiótico", "Ecocardiograma transesofágico"]),
   "nota": "La válvula reumática es el terreno: la endocarditis es la que emboliza."},
  ["Criterios de Duke: hemocultivos y ecocardiograma son los mayores.",
   "Embolia cerebral por vegetación grande: valorar cirugía precoz.",
   "No anticoagular por la embolia séptica: riesgo de sangrado."],
  "ESC – Guidelines for the management of endocarditis (2023)")

# INF-079 · tarjetas
V("tarjetas", "INF-079", "odinofagia-adenopatias-linfocitos-atipicos-mononucleosis", "Fiebre y adenopatías: ¿cómo se contagió?",
  "INFECTOLOGÍA ENAM: MONONUCLEOSIS INFECCIOSA", "INFECTOLOGÍA",
  ("Mononucleosis infecciosa", ["Virus de Epstein-Barr: fiebre, faringitis, adenopatías y linfocitos atípicos",
   "Se transmite por saliva: la 'enfermedad del beso'"]),
  ("Varón de 23 años con 2 semanas de malestar", ["Febrícula, odinofagia, adenopatías generalizadas", "Linfocitosis con cambios virales"]),
  {"rotulo": "¿Cuál es la vía de contagio?", "ans": 0, "cards": [
      {"titulo": "EPSTEIN-BARR", "datos": [
          ("Vía", "SALIVA (BESOS)", True), ("Clave", "Linfocitos atípicos", True),
          ("Órgano", "Ganglios, bazo", True), ("Prueba", "Monotest", False)],
       "pie": "Evitar deportes de contacto"},
      {"titulo": "Leptospirosis", "datos": [
          ("Vía", "Orina de roedor", False), ("Clave", "Mialgia en pantorrillas", False),
          ("Órgano", "Hígado, riñón", False), ("Prueba", "ELISA IgM", False)],
       "pie": "Penicilina o doxiciclina"},
      {"titulo": "Dengue", "datos": [
          ("Vía", "Aedes aegypti", False), ("Clave", "Dolor retroocular", False),
          ("Órgano", "Endotelio", False), ("Prueba", "NS1", False)],
       "pie": "Sin antivirales"},
      {"titulo": "Hepatitis A", "datos": [
          ("Vía", "Fecal-oral, ostras", False), ("Clave", "Ictericia", False),
          ("Órgano", "Hígado", False), ("Prueba", "IgM anti-VHA", False)],
       "pie": "Vacunable"}]},
  ["La amoxicilina en la mononucleosis produce un exantema característico.",
   "Riesgo de rotura esplénica: sin deportes de contacto por 3-4 semanas.",
   "Tratamiento sintomático; corticoides solo si hay obstrucción de vía aérea."],
  "CDC – Epstein-Barr virus and infectious mononucleosis: clinical overview (2024)")

# GAS-055 · fases
V("fases", "GAS-055", "metaplasia-intestinal-esofago-distal-adenocarcinoma", "De reflujo a cáncer",
  "GASTROENTEROLOGÍA ENAM: ESÓFAGO DE BARRETT", "GASTROENTEROLOGÍA",
  ("Esófago de Barrett", ["El reflujo crónico cambia el epitelio escamoso por cilíndrico con células caliciformes",
   "Es la lesión precursora del adenocarcinoma de esófago"]),
  ("Varón de 55 años con disfagia de 6 meses", ["Mucosa eritematosa 3 cm sobre la línea Z", "Biopsia: epitelio cilíndrico con caliciformes"]),
  {"rotulo": "Secuencia de la enfermedad", "ans": 2,
   "fases": [("ERGE", "Años", "Reflujo crónico", ["Pirosis, regurgitación"]),
             ("Esofagitis", "Daño", "Erosiones", ["Los Ángeles A-D"]),
             ("Barrett", "Metaplasia", "EPITELIO CILÍNDRICO", ["Con células caliciformes"]),
             ("Displasia", "Bajo o alto grado", "Precursor inmediato", ["Ablación endoscópica"]),
             ("Cáncer", "Tercio distal", "Adenocarcinoma", ["Complicación temida"])],
   "curvas": [("Riesgo de cáncer", ROSE, [0.05, 0.08, 0.15, 0.3, 0.55, 0.75, 0.95])],
   "chips_titulo": "Complicación esperada · marcada la correcta",
   "chips": [("Adenocarcinoma", True), ("Carcinoma epidermoide", False), ("Acalasia", False), ("Divertículos", False)]},
  ["El carcinoma epidermoide se asocia a tabaco y alcohol, en el tercio medio.",
   "Barrett sin displasia: endoscopia de vigilancia cada 3-5 años.",
   "Disfagia progresiva en Barrett: descartar estenosis o cáncer."],
  "ACG – Clinical guideline: Diagnosis and management of Barrett's esophagus (Am J Gastroenterol 2022)")

# NEU-042 · árbol
A("NEU-042", "postictus-disnea-subita-dimero-d-angiotem", "TEP: ¿qué examen pedir?",
  "NEUMOLOGÍA ENAM: DIAGNÓSTICO DEL TROMBOEMBOLISMO PULMONAR", "NEUMOLOGÍA",
  ("Sospecha de TEP", ["El dímero D solo sirve para descartar si es negativo",
   "Si está alto o la sospecha es alta: angio-TC de tórax"]),
  ("Mujer de 68 años, 2 semanas tras un infarto cerebral", ["Disnea grave súbita con dolor torácico y sudoración al caminar", "Dímero D > 500 ng/ml"]),
  Q("¿Está hemodinámicamente estable?", [
      L("No: choque", "Ecocardiograma a la cabecera", ["Si hay VD dilatado: trombólisis"]),
      Q("¿Dímero D (o probabilidad alta)?", [
          L("Negativo", "TEP descartado", ["Con probabilidad baja"]),
          L("Positivo", "ANGIO-TEM PULMONAR", ["Confirma el trombo", "Anticoagular"], path=True)],
        edge="Sí", path=True)], path=True),
  ("Exámenes en la sospecha de TEP", [("Angio-TEM", True), ("Doppler", False), ("ECG / Rx", False)], [
      ("Qué aporta", ["Confirma o descarta", "Halla TVP", "Otras causas"]),
      ("Cuándo", ["Primera elección", "Si no se puede angio-TEM", "Siempre, no confirman"])]),
  ["El ECG puede mostrar taquicardia sinusal o S1Q3T3, pero no confirma.",
   "La gammagrafía V/Q es alternativa si hay alergia al contraste o falla renal.",
   "El cateterismo no se usa para diagnosticar TEP."],
  "ESC – Guidelines for the diagnosis and management of acute pulmonary embolism (2019)")

# PED-149 · matriz
V("matriz", "PED-149", "nino-contacto-tb-estridor-adenopatias-hiliares", "Tuberculosis: qué muestra la Rx",
  "PEDIATRÍA ENAM: TUBERCULOSIS PRIMARIA", "PEDIATRÍA",
  ("Tuberculosis en el niño", ["La primoinfección da adenopatías hiliares y mediastinales",
   "Pueden comprimir el bronquio: estridor y tos seca con auscultación normal"]),
  ("Niño de 12 años, padre con TB desde hace un mes", ["Fiebre, estridor inspiratorio, tos seca", "PPD positivo · auscultación normal"]),
  {"rotulo": "Forma de TB y radiografía", "eje_x": "Rasgo", "eje_y": "Forma",
   "cols": ["Hallazgo en la Rx", "Quién la tiene"], "rows": ["TB primaria", "TB miliar", "TB posprimaria"], "caso": (0, 0),
   "cells": [[("ADENOPATÍAS HILIARES", ["± complejo de Ghon"]), ("Niños", ["Contacto reciente"])],
             [("Nódulos miliares", ["Granos de mijo difusos"]), ("Lactantes, inmunodeprimidos", ["Sin BCG"])],
             [("Cavitación apical", ["Lóbulos superiores"]), ("Adolescentes y adultos", ["Reactivación"])]]},
  ["El niño con TB primaria suele ser paucibacilar: aspirado gástrico o GeneXpert.",
   "Todo contacto intradomiciliario se evalúa: Rx, PPD y clínica.",
   "Sin enfermedad activa: terapia preventiva."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · " + NELSON)

# NEU-043 · radial
V("radial", "NEU-043", "joven-sano-disnea-subita-tubo-aire-bullas", "Neumotórax: ¿qué lo causó?",
  "NEUMOLOGÍA ENAM: NEUMOTÓRAX ESPONTÁNEO PRIMARIO", "NEUMOLOGÍA",
  ("Neumotórax espontáneo primario", ["Joven alto, delgado y sano", "Rotura de bullas subpleurales apicales (enfisema acinar distal o paraseptal)"]),
  ("Varón de 20 años sano, corriendo", ["Disnea súbita, murmullo abolido a la derecha", "Mediastino desviado · sale aire por el tubo"]),
  {"rotulo": "Mapa del tema", "centro": "NEUMOTÓRAX", "centro_sub": "Según la causa", "ans": 0,
   "items": [("PRIMARIO: BULLAS APICALES", ["Enfisema acinar distal (paraseptal)", "Joven sano, fumador"]),
             ("Secundario", ["EPOC, TB, fibrosis quística"]),
             ("Traumático", ["Fractura costal, herida"]),
             ("Iatrogénico", ["Catéter central, biopsia"]),
             ("Catamenial", ["Endometriosis torácica"])],
   "ruta": ["Joven sano con disnea súbita", "Murmullo abolido", "Aire por el tubo", "BULLAS SUBPLEURALES"]},
  ["El asma no produce neumotórax con desviación mediastínica en un sano.",
   "La embolia grasa aparece 24-72 h tras fracturas de huesos largos.",
   "Recidiva frecuente: videotoracoscopía con bullectomía y pleurodesis."],
  "BTS – Guideline for pleural disease (Thorax 2023)")

# INF-080 · embudo
V("embudo", "INF-080", "htlv1-diarrea-tos-larvas-rabditoides-estrongiloidosis", "Larvas en heces y esputo",
  "INFECTOLOGÍA ENAM: HIPERINFECCIÓN POR STRONGYLOIDES", "INFECTOLOGÍA",
  ("Estrongiloidosis", ["Strongyloides se reinfecta dentro del propio huésped (autoinfección)",
   "Con HTLV-1 o corticoides la carga se dispara: hiperinfección"]),
  ("Mujer de 28 años portadora de HTLV-1", ["Diarrea líquida profusa y tos", "Eosinófilos 14 % · larvas rabditoides en heces y esputo"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Parasitosis con diarrea, tos y eosinofilia",
   "candidatos": ["Estrongiloidosis", "Ascaridiasis", "Esquistosomiasis", "Oncocercosis"],
   "pasos": [("Se ven larvas, no huevos, en las heces", ["Ascaridiasis", "Esquistosomiasis"]),
             ("Afecta intestino y pulmón, no piel ni ojos", ["Oncocercosis"])],
   "final": ("ESTRONGILOIDOSIS: HIPERINFECCIÓN", ["Ivermectina diaria hasta negativizar", "Cubrir gramnegativos si hay sepsis"]),
   "nota": "HTLV-1 desvía la inmunidad y favorece la hiperinfección por Strongyloides."},
  ["Larvas en esputo = ciclo pulmonar acelerado (hiperinfección).",
   "Tamizar Strongyloides antes de dar corticoides a pacientes de zonas endémicas.",
   "Las larvas arrastran bacterias intestinales: sepsis y meningitis por gramnegativos."],
  "CDC – Strongyloides: Clinical care (2024) · " + HARRISON)

# INF-081 · termómetro
V("termometro", "INF-081", "campesino-ictericia-sufusion-conjuntival-penicilina", "Leptospirosis: gravedad",
  "INFECTOLOGÍA ENAM: LEPTOSPIROSIS", "INFECTOLOGÍA",
  ("Leptospirosis", ["Zoonosis por contacto con agua u orina de roedores",
   "Fiebre, mialgias intensas y sufusión conjuntival; forma grave con ictericia"]),
  ("Campesino de 55 años de Lurín", ["7 días de fiebre, cefalea, mialgias intensas e ictericia", "Inyección conjuntival · transaminasas < 5 veces"]),
  {"rotulo": "Forma clínica",
   "niveles": [("Leve", "Anictérica", ["Fiebre, mialgias, conjuntivas rojas"]),
               ("Grave", "Ictérica (Weil)", ["ICTERICIA + MIALGIAS", "Riesgo renal y hemorrágico"]),
               ("Crítica", "Hemorragia pulmonar", ["Distrés, alta mortalidad"])],
   "caso_nivel": 1, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "Penicilina G sódica EV", ["O ceftriaxona EV, 7 días"], True),
             (2, "Vigilar riñón y sangrado", ["Diálisis si es necesario"], False),
             (3, "Leve y ambulatoria", ["Doxiciclina o amoxicilina oral"], False)]},
  ["Transaminasas poco elevadas con bilirrubina alta: típico de leptospirosis.",
   "Mialgias en pantorrillas y sufusión conjuntival son claves.",
   "Vancomicina e imipenem no son de elección."],
  "MINSA – NTS de atención integral de la leptospirosis · OMS – Human leptospirosis: guidance for diagnosis, surveillance and control")

# INF-082 · embudo
V("embudo", "INF-082", "edema-bipalpebral-unilateral-romana-chagas", "Ojo hinchado en un niño del sur",
  "INFECTOLOGÍA ENAM: ENFERMEDAD DE CHAGAS AGUDA", "INFECTOLOGÍA",
  ("Enfermedad de Chagas", ["Trypanosoma cruzi transmitido por la chirimacha (Triatoma infestans)",
   "Signo de Romaña: edema bipalpebral unilateral + conjuntivitis + adenopatía preauricular"]),
  ("Adolescente de 12 años", ["Edema bipalpebral izquierdo, conjuntiva roja", "Adenopatía preauricular · de un valle costero del sur"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Edema palpebral unilateral en un niño",
   "candidatos": ["Tripanosomiasis", "Loxocelismo", "Bartonelosis", "Latrodectismo"],
   "pasos": [("Sin necrosis, placa livedoide ni dolor intenso", ["Loxocelismo", "Latrodectismo"]),
             ("Sur del Perú, no valles interandinos del norte", ["Bartonelosis"])],
   "final": ("CHAGAS AGUDO (SIGNO DE ROMAÑA)", ["Gota gruesa o frotis: tripomastigotes", "Benznidazol o nifurtimox"]),
   "nota": "Arequipa, Moquegua y Tacna son zonas endémicas de Triatoma infestans."},
  ["Chagas crónico: miocardiopatía, megaesófago y megacolon.",
   "Chagoma de inoculación: lesión en piel donde picó el insecto.",
   "La bartonelosis se transmite por la titira (Lutzomyia)."],
  "MINSA – NTS para la prevención y control de la enfermedad de Chagas · OPS – Guía para el diagnóstico y tratamiento de la enfermedad de Chagas (2018)")

# SP-115 · radial
V("radial", "SP-115", "discapacidad-prematura-carga-enfermedad-avad", "Medir discapacidad prematura",
  "SALUD PÚBLICA ENAM: CARGA DE ENFERMEDAD", "SALUD PÚBLICA",
  ("Carga de enfermedad", ["Mide muerte prematura y discapacidad en un solo indicador: AVAD",
   "AVAD = años de vida perdidos + años vividos con discapacidad"]),
  ("Ministro de Salud", ["Intervención para reducir la discapacidad prematura", "¿Qué regiones se beneficiaron?"]),
  {"rotulo": "Mapa del tema", "centro": "HERRAMIENTAS", "centro_sub": "¿Qué mide cada una?", "ans": 0,
   "items": [("CARGA DE ENFERMEDAD", ["AVAD por región", "Muerte prematura + discapacidad"]),
             ("ASIS", ["Diagnóstico de salud local"]),
             ("Ensayo clínico", ["Eficacia de un tratamiento"]),
             ("Estudio descriptivo", ["Frecuencia y distribución"]),
             ("Tasa de mortalidad", ["Solo cuenta muertes"])],
   "ruta": ["Meta: reducir discapacidad prematura", "Comparar regiones", "Indicador AVAD", "CARGA DE ENFERMEDAD"]},
  ["Un AVAD es un año de vida sana perdido.",
   "Permite priorizar problemas y comparar intervenciones.",
   "El ASIS usa estos indicadores, pero no es el indicador en sí."],
  "OMS – Global burden of disease: methods (2020) · MINSA – Carga de enfermedad en el Perú (2019)")

# PED-150 · árbol
A("PED-150", "lactante-sin-cicatriz-bcg-no-revacunar", "BCG sin cicatriz",
  "PEDIATRÍA ENAM: VACUNA BCG", "PEDIATRÍA",
  ("Cicatriz de BCG", ["Hasta 10-20 % de vacunados no forma cicatriz",
   "Si hay registro de vacunación, no se revacuna"]),
  ("Lactante de 4 meses", ["Sin cicatriz ni nódulo de BCG", "Carné de vacunas completo"]),
  Q("¿Tiene registro de BCG?", [
      L("Sí", "NO REQUIERE REVACUNACIÓN", ["La falta de cicatriz no indica falla", "Continuar el esquema"], path=True),
      L("No", "Aplicar BCG", ["Según el esquema MINSA"])], path=True),
  ("Vacuna BCG", [("Dato", True), ("Detalle", False)], [
      ("Cuándo", ["Al nacer, en las primeras 24 h", "RN ≥ 2000 g"]),
      ("Protege de", ["TB miliar y meníngea", "Poco contra TB pulmonar"]),
      ("Vía", ["Intradérmica", "Deltoides derecho"])]),
  ["La cicatriz aparece a las 6-12 semanas y puede no formarse.",
   "No se recomienda revacunar con BCG.",
   "Contraindicada en niños con VIH sintomático o inmunodeficiencia."],
  "MINSA – NTS 196: Esquema nacional de vacunación (2022) · OMS – Position paper on BCG vaccines (2018)")

# PED-151 · tarjetas
V("tarjetas", "PED-151", "nina-pci-sonda-vesical-fiebre-urocultivo", "Fiebre en el niño hospitalizado",
  "PEDIATRÍA ENAM: INFECCIÓN URINARIA ASOCIADA A SONDA", "PEDIATRÍA",
  ("Infección nosocomial", ["El foco suele estar en el dispositivo invasivo",
   "Sonda vesical + fiebre = infección urinaria asociada a catéter"]),
  ("Niña de 3 años con parálisis cerebral", ["Hospitalizada por deshidratación, con sonda vesical", "A los 2 días: malestar y fiebre de 39 °C"]),
  {"rotulo": "¿Dónde buscar el foco?", "ans": 0, "cards": [
      {"titulo": "ITU POR SONDA", "datos": [
          ("Dispositivo", "Sonda vesical", True), ("Inicio", "> 48 h", True),
          ("Examen", "UROCULTIVO", True)],
       "pie": "Cambiar o retirar la sonda"},
      {"titulo": "Bacteriemia por catéter", "datos": [
          ("Dispositivo", "Catéter venoso", False), ("Inicio", "> 48 h", False),
          ("Examen", "Hemocultivos", False)],
       "pie": "Central y periférico"},
      {"titulo": "Neumonía aspirativa", "datos": [
          ("Dispositivo", "Sonda gástrica", False), ("Inicio", "Variable", False),
          ("Examen", "Rx de tórax", False)],
       "pie": "Tos, crepitantes"},
      {"titulo": "Flebitis", "datos": [
          ("Dispositivo", "Vía periférica", False), ("Inicio", "Días", False),
          ("Examen", "Clínico", False)],
       "pie": "Cordón doloroso"}]},
  ["La muestra se toma de la sonda nueva o del puerto, no de la bolsa.",
   "El frotis de sangre y el mielocultivo no orientan este cuadro.",
   "Retirar la sonda lo antes posible es la mejor prevención."],
  "IDSA – Guidelines for catheter-associated urinary tract infection · CDC – CAUTI guideline (2019)")

# SP-116 · fases
V("fases", "SP-116", "viajero-exantema-igm-sarampion-importado", "Vigilancia del sarampión",
  "SALUD PÚBLICA ENAM: CASO IMPORTADO DE SARAMPIÓN", "SALUD PÚBLICA",
  ("Clasificación de casos de sarampión", ["Confirmado + exposición fuera del país en los 7-21 días previos = importado",
   "Autóctono: sin viaje, contagio dentro del país"]),
  ("Varón de 23 años", ["Hace 15 días viajó a un país con sarampión", "Fiebre, exantema maculopapular · IgM (+)"]),
  {"rotulo": "Del sospechoso a la clasificación", "ans": 2,
   "fases": [("Sospechoso", "Clínica", "Fiebre + exantema", ["Notificar en 24 h"]),
             ("Confirmado", "Laboratorio", "IgM positiva", ["O PCR"]),
             ("Por origen", "Epidemiología", "IMPORTADO", ["Viaje en los 7-21 días previos"]),
             ("Acción", "Control", "Cerco y vacunación", ["Contactos en 72 h"])],
   "curvas": [],
   "chips_titulo": "Clasificación · marcada la correcta",
   "chips": [("Importado", True), ("Autóctono", False), ("Sospechoso", False), ("Inmunizado", False)]},
  ["El período de incubación del sarampión es de 7 a 21 días.",
   "Caso relacionado a importación: se contagió de un importado dentro del país.",
   "Perú está en fase de mantener la eliminación: cada caso es alerta."],
  "OPS – Plan de acción para la sostenibilidad de la eliminación del sarampión (2023) · MINSA – Directiva de vigilancia de sarampión y rubéola")

# PED-152 · termómetro
V("termometro", "PED-152", "prematuro-34-sem-glucosa-40-tremores-bolo-ev", "Hipoglucemia neonatal",
  "PEDIATRÍA ENAM: HIPOGLUCEMIA NEONATAL", "PEDIATRÍA",
  ("Hipoglucemia neonatal", ["Glucosa < 45 mg/dl en el recién nacido",
   "Con síntomas (tremores, hipoactividad, vómitos) se trata por vía EV"]),
  ("RN de 34 semanas con 48 h de vida", ["Taquipnea, vómitos, hipoactivo, tremores", "Glucemia 40 mg/dl"]),
  {"rotulo": "Glucemia y síntomas",
   "niveles": [("≥ 45", "Normal", ["Lactancia a libre demanda"]),
               ("< 45", "Asintomática", ["Alimentar y controlar en 1 h"]),
               ("Síntomas", "Sintomática o < 25", ["TREMORES + HIPOACTIVIDAD", "Tratamiento EV"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Bolo de glucosa 200 mg/kg EV", ["2 ml/kg de dextrosa al 10 %"], True),
             (2, "Infusión 6-8 mg/kg/min", ["Controlar a los 30 min"], False),
             (3, "Buscar la causa", ["Prematuridad, sepsis, hijo de diabética"], False)]},
  ["Nunca dextrosa al 25-50 % en neonatos: riesgo de hiperglucemia de rebote y daño venoso.",
   "La vía oral no es segura con vómitos e hipoactividad.",
   "La hipoglucemia sintomática puede dejar daño neurológico."],
  "AAP – Postnatal glucose homeostasis in late-preterm and term infants (Pediatrics 2011) · " + NELSON)

# GIN-154 · fases
V("fases", "GIN-154", "gestante-calcio-desde-20-semanas", "Suplementos en el embarazo",
  "OBSTETRICIA ENAM: SUPLEMENTACIÓN DE CALCIO", "OBSTETRICIA",
  ("Suplementos en la gestación", ["Calcio desde las 20 semanas hasta el parto: reduce la preeclampsia",
   "Hierro y ácido fólico tienen su propio calendario"]),
  ("Pregunta de control prenatal", ["¿Desde y hasta cuándo se da el calcio?"]),
  {"rotulo": "Calendario de suplementos", "ans": 2,
   "fases": [("Preconcepción", "3 meses antes", "Ácido fólico", ["Previene defectos del tubo neural"]),
             ("1.er trimestre", "Hasta 13 semanas", "Ácido fólico", ["400 µg/día"]),
             ("Desde 20 semanas", "Hasta el parto", "CALCIO 2 G/DÍA", ["Previene preeclampsia"]),
             ("Puerperio", "Hasta 30 días", "Hierro", ["Continúa en la lactancia"])],
   "curvas": [],
   "chips_titulo": "Periodo del calcio · marcado el correcto",
   "chips": [("Semana 20 hasta el término", True), ("Hasta la semana 12", False), ("Semanas 13-19", False), ("Últimas 4 semanas", False)]},
  ["El hierro + ácido fólico se inicia desde la semana 14 (MINSA).",
   "El calcio y el hierro se toman separados: compiten en la absorción.",
   "Beneficio mayor en poblaciones con baja ingesta de calcio."],
  "MINSA – NTS de atención integral de salud materna · OMS – Recomendaciones sobre suplementación de calcio en el embarazo (2018)")

# PED-153 · fases
V("fases", "PED-153", "cred-primer-ano-controles-mensuales", "Controles de CRED",
  "PEDIATRÍA ENAM: CONTROL DE CRECIMIENTO Y DESARROLLO", "PEDIATRÍA",
  ("Control de crecimiento y desarrollo", ["La frecuencia cambia con la edad",
   "Primer año: 4 controles en el primer mes y luego 1 al mes"]),
  ("Norma técnica de CRED (MINSA)", ["¿Cuántos controles en el primer año?"]),
  {"rotulo": "Frecuencia por edad", "ans": 0,
   "fases": [("Primer año", "0-11 meses", "4 EN EL 1.ER MES + 1 AL MES", ["RN: 4 controles", "1-11 meses: 11 controles"]),
             ("Segundo año", "12-23 meses", "Cada 2 meses", ["6 controles"]),
             ("Preescolar", "24-59 meses", "Cada 3 meses", ["4 al año"]),
             ("Escolar", "5-11 años", "1 al año", ["Tamizajes"])],
   "curvas": [("Controles por año", SKY, [1.0, 0.9, 0.5, 0.45, 0.35, 0.3, 0.1, 0.1])],
   "chips_titulo": "Primer año · marcado el correcto",
   "chips": [("4 en el 1.er mes y 1 cada mes", True), ("6 bimensuales", False), ("4 en el año", False), ("2 semestrales", False)]},
  ["El primer año concentra más controles por el crecimiento rápido.",
   "En cada control: peso, talla, perímetro cefálico, desarrollo y vacunas.",
   "Se aprovecha para tamizar anemia desde los 6 meses."],
  "MINSA – NTS 537: Control de crecimiento y desarrollo de la niña y el niño menor de cinco años (2017)")

# SP-117 · matriz
V("matriz", "SP-117", "45-casos-nuevos-1000-personas-incidencia", "Medidas de frecuencia y asociación",
  "SALUD PÚBLICA ENAM: INCIDENCIA ACUMULADA", "SALUD PÚBLICA",
  ("Incidencia", ["Cuenta casos NUEVOS en una población en riesgo durante un periodo",
   "45 casos nuevos / 1000 personas = 45 por 1000"]),
  ("Grupo de 1000 personas", ["Aparecen 45 casos nuevos", "¿Qué medida es?"]),
  {"rotulo": "Qué se divide en cada medida", "eje_x": "Rasgo", "eje_y": "Medida",
   "cols": ["Numerador", "Denominador"], "rows": ["Incidencia", "Prevalencia", "Riesgo relativo", "Riesgo atribuible"], "caso": (0, 0),
   "cells": [[("CASOS NUEVOS", ["45"]), ("Población en riesgo", ["1000"])],
             [("Casos existentes", ["Nuevos + antiguos"]), ("Población total", [])],
             [("Incidencia en expuestos", []), ("Incidencia en no expuestos", ["Es un cociente"])],
             [("Ie − Io", ["Es una resta"]), ("No tiene", [])]]},
  ["Prevalencia ≈ incidencia × duración de la enfermedad.",
   "RR y RA necesitan comparar expuestos con no expuestos.",
   "La incidencia estima el riesgo de enfermar."],
  "Gordis. Epidemiología 6.ª ed. (2019)")

# CB-059 · matriz
V("matriz", "CB-059", "vacuna-induce-inmunidad-activa-artificial", "Tipos de inmunidad",
  "CIENCIAS BÁSICAS ENAM: INMUNIDAD ACTIVA", "CIENCIAS BÁSICAS",
  ("Inmunidad adquirida", ["Activa: el propio organismo produce anticuerpos y memoria",
   "Pasiva: recibe anticuerpos ya formados, sin memoria"]),
  ("Se administra una vacuna", ["¿Qué inmunidad induce?"]),
  {"rotulo": "Origen y tipo de inmunidad", "eje_x": "Tipo", "eje_y": "Origen",
   "cols": ["Activa", "Pasiva"], "rows": ["Artificial", "Natural"], "caso": (0, 0),
   "cells": [[("VACUNA", ["Memoria duradera", "Tarda 2-3 semanas"]), ("Inmunoglobulina, antitoxina", ["Inmediata, dura semanas"])],
             [("Infección", ["Tras enfermar"]), ("Placenta y leche", ["IgG materna, IgA"])]]},
  ["La inmunidad activa genera linfocitos de memoria.",
   "La pasiva protege de inmediato pero es transitoria.",
   "Tras una exposición a rabia o tétanos se combinan ambas."],
  "Abbas. Inmunología celular y molecular 10.ª ed. (2022)")

# SP-118 · radial
V("radial", "SP-118", "agua-hospital-pseudomonas-transmision-vehiculo", "Mecanismos de transmisión",
  "SALUD PÚBLICA ENAM: TRANSMISIÓN POR VEHÍCULO", "SALUD PÚBLICA",
  ("Transmisión indirecta por vehículo", ["Un objeto inanimado lleva el agente: agua, alimentos, instrumentos",
   "Agua potable contaminada = vehículo común"]),
  ("Hospital", ["Pseudomonas y otros gramnegativos", "Aislados en el agua potable"]),
  {"rotulo": "Mapa del tema", "centro": "TRANSMISIÓN", "centro_sub": "¿Cómo llega el agente?", "ans": 0,
   "items": [("VEHÍCULO", ["Agua, alimentos, fómites", "Brotes de fuente común"]),
             ("Aérea", ["Núcleos de gotitas < 5 µm"]),
             ("Gotas", ["> 5 µm, a menos de 1 m"]),
             ("Vectorial", ["Mosquitos, pulgas"]),
             ("Contacto directo", ["Piel, mucosas, sangre"])],
   "ruta": ["Agua del hospital", "Objeto inanimado", "Lleva gramnegativos", "VEHÍCULO"]},
  ["Medidas: clorar el agua, filtros en los puntos de uso.",
   "Pseudomonas sobrevive en ambientes húmedos y grifos.",
   "Aérea: TB, sarampión, varicela; gotas: influenza."],
  "OMS – Guidelines for drinking-water quality 4.ª ed. (2022) · Gordis. Epidemiología 6.ª ed. (2019)")

# SP-119 · árbol
A("SP-119", "acreditacion-evaluacion-personal-propio-autoevaluacion", "Acreditación de establecimientos",
  "SALUD PÚBLICA ENAM: ACREDITACIÓN EN SALUD", "SALUD PÚBLICA",
  ("Acreditación de servicios de salud", ["Proceso que verifica el cumplimiento de estándares de calidad",
   "Tiene dos fases: autoevaluación y evaluación externa"]),
  ("Proceso de acreditación", ["La valoración la hace el personal de la misma institución"]),
  Q("¿Quién evalúa?", [
      L("Personal propio", "AUTOEVALUACIÓN", ["Primera fase", "Identifica brechas internas"], path=True),
      L("Evaluadores externos", "Evaluación externa", ["Verifica y otorga la acreditación"])], path=True),
  ("Fases de la acreditación", [("Autoevaluación", True), ("Evaluación externa", False)], [
      ("Quién", ["Equipo interno", "Evaluadores acreditados"]),
      ("Para qué", ["Plan de mejora", "Otorgar acreditación"])]),
  ["La autoevaluación es obligatoria antes de pedir la evaluación externa.",
   "La acreditación tiene vigencia limitada y se renueva.",
   "Retroalimentación y juicio de expertos no son fases formales."],
  "MINSA – NTS 050: Acreditación de establecimientos de salud y servicios médicos de apoyo")

# REU-045 · termómetro
V("termometro", "REU-045", "lactante-surcos-prurito-palmas-plantas-permetrina", "Escabiosis: tratamiento por edad",
  "DERMATOLOGÍA ENAM: ESCABIOSIS", "DERMATOLOGÍA",
  ("Escabiosis", ["Prurito nocturno con surcos en muñecas, interdigitales y pliegues",
   "En lactantes afecta palmas, plantas y cara"]),
  ("Lactante de 18 meses", ["Surcos lineales y pápulas con costras", "Muñecas, tronco, manos, pies y cara"]),
  {"rotulo": "Edad del paciente",
   "niveles": [("< 2 meses", "Recién nacido", ["Azufre precipitado 5-10 %"]),
               ("≥ 2 meses", "Lactante y niño", ["LACTANTE DE 18 MESES", "Permetrina 5 %"]),
               ("> 15 kg", "Brotes o costrosa", ["Ivermectina oral"])],
   "caso_nivel": 1, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Permetrina 5 % en crema", ["En lactantes incluir cabeza y cara", "Dejar 8-12 h y lavar"], True),
             (2, "Repetir a los 7 días", ["Mata las larvas nuevas"], False),
             (3, "Tratar a todos los contactos", ["Lavar ropa con agua caliente"], False)]},
  ["El hexacloruro de benceno (lindano) es neurotóxico: no en niños.",
   "El benzoato de bencilo irrita y no es de elección en lactantes.",
   "El prurito puede durar semanas tras el tratamiento."],
  "IUSTI – European guideline for the management of scabies (2017) · CDC – Scabies: clinical care (2024)")

# NEU-044 · matriz
V("matriz", "NEU-044", "asma-mortalidad-resistencia-corticoides", "Factores de muerte por asma",
  "NEUMOLOGÍA ENAM: MORTALIDAD POR ASMA", "NEUMOLOGÍA",
  ("Riesgo de asma fatal", ["Los factores se agrupan en biológicos, ambientales, asistenciales y psicosociales",
   "Biológico: asma que no responde a los corticoides"]),
  ("Pregunta de riesgo", ["¿Cuál es un factor biológico de mortalidad?"]),
  {"rotulo": "Tipo de factor y ejemplo", "eje_x": "Rasgo", "eje_y": "Factor",
   "cols": ["Ejemplo", "Qué hacer"], "rows": ["Biológico", "Ambiental", "Asistencial", "Psicosocial"], "caso": (0, 0),
   "cells": [[("NO RESPONDE A CORTICOIDES", ["Asma grave, intubación previa"]), ("Especialista, biológicos", [])],
             [("Humo de tabaco", ["Alérgenos, contaminación"]), ("Evitar exposición", [])],
             [("Atención inadecuada", ["Sin corticoide inhalado"]), ("Plan de acción escrito", [])],
             [("Trastorno psicológico", ["Pobreza, mala adherencia"]), ("Apoyo social", [])]]},
  ["Usar más de un inhalador de rescate al mes indica mal control.",
   "Ingreso a UCI o intubación previa: alto riesgo de muerte.",
   "Los corticoides inhalados reducen la mortalidad por asma."],
  "GINA – Global Strategy for Asthma Management and Prevention (2025)")

# REU-046 · tarjetas
V("tarjetas", "REU-046", "lactante-fiebre-ampollas-flacidas-nikolsky-ritter", "Ampollas en el lactante",
  "DERMATOLOGÍA ENAM: SÍNDROME DE PIEL ESCALDADA ESTAFILOCÓCICA", "DERMATOLOGÍA",
  ("Piel escaldada estafilocócica", ["Toxinas exfoliativas de S. aureus rompen la desmogleína 1",
   "Eritema periorificial y en pliegues, ampollas flácidas, Nikolsky (+) y sin mucosas"]),
  ("Lactante con 3 días de fiebre de 39 °C", ["Irritable, no come", "Eritema periorificial y en flexuras · ampollas · Nikolsky (+)"]),
  {"rotulo": "¿Qué enfermedad ampollosa?", "ans": 0, "cards": [
      {"titulo": "ENFERMEDAD DE RITTER", "datos": [
          ("Edad", "Lactante, < 5 años", True), ("Nikolsky", "Positivo", True),
          ("Mucosas", "Respetadas", True), ("Causa", "Toxina estafilocócica", False)],
       "pie": "Oxacilina o cefazolina EV"},
      {"titulo": "Impétigo ampolloso", "datos": [
          ("Edad", "Niños", False), ("Nikolsky", "Negativo", False),
          ("Mucosas", "Respetadas", False), ("Causa", "S. aureus local", False)],
       "pie": "Lesiones localizadas"},
      {"titulo": "Pénfigo vulgar", "datos": [
          ("Edad", "Adultos", False), ("Nikolsky", "Positivo", False),
          ("Mucosas", "Afectadas", False), ("Causa", "Autoinmune", False)],
       "pie": "Corticoides"},
      {"titulo": "Epidermólisis ampollosa", "datos": [
          ("Edad", "Desde el nacimiento", False), ("Nikolsky", "Variable", False),
          ("Mucosas", "Variable", False), ("Causa", "Genética", False)],
       "pie": "Ampollas por roce"}]},
  ["La necrólisis epidérmica tóxica sí afecta mucosas y se asocia a fármacos.",
   "El despegamiento es superficial: cura sin cicatriz.",
   "Hospitalizar, antibióticos EV y cuidado de la piel como gran quemado."],
  "Fitzpatrick's Dermatology 9.ª ed. (2019) · " + NELSON)

# REU-047 · árbol
A("REU-047", "deportista-una-blanquecina-engrosada-onicomicosis", "Uña engrosada del pie",
  "DERMATOLOGÍA ENAM: ONICOMICOSIS", "DERMATOLOGÍA",
  ("Alteraciones de la uña", ["Engrosamiento, color blanco-amarillento y despegamiento distal = onicomicosis",
   "Calzado cerrado y sudor favorecen los dermatofitos"]),
  ("Adolescente deportista", ["Uñas del primer dedo de ambos pies", "Blanquecinas, engrosadas, con onicólisis distal"]),
  Q("¿Qué patrón tiene la uña?", [
      L("Engrosada, blanca-amarilla", "MICOSIS (ONICOMICOSIS)", ["KOH y cultivo", "Terbinafina oral"], path=True),
      L("Hoyuelos, mancha de aceite", "Psoriasis", ["Lesiones en piel"]),
      L("Hematoma, una sola uña", "Traumatismo", ["Antecedente de golpe"]),
      L("Líneas, alopecia, diarrea", "Déficit de zinc", ["Dermatitis periorificial"])], path=True),
  ("Onicomicosis", [("Clave", True), ("Detalle", False)], [
      ("Agente", ["Trichophyton rubrum", "Dermatofito"]),
      ("Diagnóstico", ["KOH + cultivo", "Antes de tratar"]),
      ("Tratamiento", ["Terbinafina 12 semanas", "Tópicos si es leve"])]),
  ["Afecta más el primer dedo del pie.",
   "Suele acompañarse de tiña del pie.",
   "Confirmar siempre el hongo antes de un tratamiento oral largo."],
  "AAD – Guidelines of care for onychomycosis · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# OFT-034 · embudo
V("embudo", "OFT-034", "nino-2-anos-estrabismo-sin-reflejo-retinoblastoma", "Reflejo pupilar ausente en un niño",
  "OFTALMOLOGÍA ENAM: RETINOBLASTOMA", "OFTALMOLOGÍA",
  ("Retinoblastoma", ["Tumor intraocular maligno más frecuente en niños",
   "Leucocoria y estrabismo son sus dos primeros signos"]),
  ("Niño de 2 años", ["Desviación convergente del ojo derecho", "Reflejo pupilar ausente · inflamación periorbitaria"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Leucocoria o reflejo ausente + estrabismo",
   "candidatos": ["Retinoblastoma", "Catarata", "Vítreo hiperplásico", "Endoftalmitis"],
   "pasos": [("Sin cirugía, trauma ni sepsis previos", ["Endoftalmitis"]),
             ("Aparece a los 2 años, con estrabismo e inflamación", ["Catarata", "Vítreo hiperplásico"])],
   "final": ("RETINOBLASTOMA", ["Fondo de ojo bajo anestesia + ecografía o RM", "Nunca biopsiar: riesgo de siembra"]),
   "nota": "La inflamación periorbitaria puede ser un retinoblastoma avanzado que simula celulitis."},
  ["Mutación del gen RB1; bilateral = hereditario.",
   "Buscar reflejo rojo en todo control del niño.",
   "Riesgo de segundo tumor: osteosarcoma."],
  "AAO – Retinoblastoma (EyeWiki / Basic and Clinical Science Course 2024) · " + NELSON)

# SP-120 · árbol
A("SP-120", "brote-dengue-susceptibles-enfermo-mosquito", "¿Qué hace falta para un brote de dengue?",
  "SALUD PÚBLICA ENAM: CADENA DE TRANSMISIÓN DEL DENGUE", "SALUD PÚBLICA",
  ("Cadena de transmisión", ["Un brote necesita: persona enferma (virémica), mosquito Aedes y población susceptible",
   "Si falta uno de los tres, no hay transmisión"]),
  ("Pregunta de epidemiología", ["¿Qué elementos se requieren para un brote?"]),
  Q("¿Hay Aedes aegypti?", [
      L("No", "Sin transmisión", ["Solo casos importados"]),
      Q("¿Hay un enfermo virémico?", [
          L("No", "Riesgo latente", ["Vigilancia entomológica"]),
          L("Sí, con susceptibles", "BROTE POSIBLE", ["Susceptibles + enfermo + mosquito"], path=True)],
        edge="Sí", path=True)], path=True),
  ("Elementos del brote", [("Susceptibles", True), ("Enfermo", True), ("Mosquito", True)], [
      ("Papel", ["Hospederos", "Fuente del virus", "Vector"]),
      ("Control", ["Educación, vacuna", "Aislamiento con mosquitero", "Eliminar criaderos"])]),
  ["Los criaderos permiten que haya mosquitos, pero el mosquito es el elemento necesario.",
   "El clima y la vivienda son condicionantes, no requisitos.",
   "El paciente con dengue debe usar mosquitero para cortar la cadena."],
  "OPS – Directrices para el diagnóstico clínico y el tratamiento del dengue, chikungunya y zika (2022) · MINSA – NTS de vigilancia del dengue")

# PED-154 · fases
V("fases", "PED-154", "rn-muy-bajo-peso-complicacion-inmediata-respiratoria", "Complicaciones del prematuro",
  "PEDIATRÍA ENAM: RECIÉN NACIDO DE MUY BAJO PESO", "PEDIATRÍA",
  ("Recién nacido de muy bajo peso (< 1500 g)", ["Los problemas aparecen en un orden típico",
   "Inmediato: dificultad respiratoria por déficit de surfactante"]),
  ("Pregunta de neonatología", ["¿Cuál es la complicación inmediata más frecuente?"]),
  {"rotulo": "Cuándo aparece cada complicación", "ans": 0,
   "fases": [("Inmediata", "Horas", "INSUFICIENCIA RESPIRATORIA", ["Membrana hialina", "CPAP, surfactante"]),
             ("Temprana", "Días", "HIV, sepsis, ECN", ["Hemorragia intraventricular"]),
             ("Tardía", "Semanas", "Retinopatía, DBP", ["Tamizaje de fondo de ojo"]),
             ("Largo plazo", "Meses-años", "Neurodesarrollo", ["Hidrocefalia poshemorrágica"])],
   "curvas": [("Riesgo respiratorio", ROSE, [0.95, 0.8, 0.5, 0.3, 0.2, 0.1, 0.1])],
   "chips_titulo": "Complicación inmediata · marcada la correcta",
   "chips": [("Insuficiencia respiratoria", True), ("Retinopatía", False), ("Hidrocefalia", False), ("Malabsorción", False)]},
  ["Corticoides prenatales reducen la membrana hialina.",
   "La retinopatía aparece semanas después: fondo de ojo a las 4-6 semanas.",
   "La hidrocefalia es secuela de la hemorragia intraventricular."],
  NELSON + " · European Consensus Guidelines on the management of RDS (Neonatology 2022)")

# PED-155 · árbol
A("PED-155", "rn-rpm-18-horas-fiebre-succion-debil-hemocultivo", "Sospecha de sepsis neonatal",
  "PEDIATRÍA ENAM: SEPSIS NEONATAL PRECOZ", "PEDIATRÍA",
  ("Sepsis neonatal precoz", ["Primeras 72 h; factor clave: RPM ≥ 18 h",
   "El hemocultivo es el estándar para el diagnóstico"]),
  ("RN de 5 horas, 39 semanas", ["Madre con RPM de 18 horas", "Fiebre de 38 °C y succión débil"]),
  Q("¿Tiene signos clínicos de infección?", [
      L("Sí", "HEMOCULTIVO + ANTIBIÓTICOS", ["Ampicilina + gentamicina", "Antes de la primera dosis"], path=True),
      L("No, solo riesgo", "Observación 48 h", ["Según calculadora de riesgo"])], path=True),
  ("Exámenes en la sepsis neonatal", [("Hemocultivo", True), ("PCR", False), ("Hemograma", False)], [
      ("Qué aporta", ["Confirma el germen", "Apoya, inespecífica", "Leucopenia, desviación"]),
      ("Papel", ["Estándar de oro", "Seguimiento", "Complemento"])]),
  ["Gérmenes principales: estreptococo del grupo B y E. coli.",
   "La punción lumbar se hace si el hemocultivo es positivo o hay signos neurológicos.",
   "La PCR seriada ayuda a decidir cuándo suspender antibióticos."],
  "AAP – Management of neonates born at ≥ 35 weeks with suspected early-onset sepsis (Pediatrics 2018) · " + NELSON)

# TRA-034 · tarjetas
V("tarjetas", "TRA-034", "anciana-caida-pierna-acortada-rotacion-externa-cadera", "Actitud de la pierna tras una caída",
  "TRAUMATOLOGÍA ENAM: FRACTURA DE CADERA", "TRAUMATOLOGÍA",
  ("Fractura de cadera", ["Anciana que cae y no puede mover la pierna",
   "Miembro acortado y en rotación externa = fractura de cadera"]),
  ("Mujer diabética de 85 años tras una caída", ["Dolor intenso, no moviliza la pierna derecha", "Miembro acortado y en rotación externa"]),
  {"rotulo": "¿Qué lesión es?", "ans": 0, "cards": [
      {"titulo": "FRACTURA DE CADERA", "datos": [
          ("Longitud", "Acortada", True), ("Rotación", "Externa", True),
          ("Paciente", "Anciana, caída simple", True), ("Tratamiento", "Cirugía < 48 h", False)],
       "pie": "Cuello o intertrocantérea"},
      {"titulo": "Luxación posterior", "datos": [
          ("Longitud", "Acortada", False), ("Rotación", "Interna, aducción", False),
          ("Paciente", "Joven, tablero de auto", False), ("Tratamiento", "Reducir urgente", False)],
       "pie": "Riesgo de lesión ciática"},
      {"titulo": "Luxación anterior", "datos": [
          ("Longitud", "Variable", False), ("Rotación", "Externa, abducción", False),
          ("Paciente", "Trauma grande", False), ("Tratamiento", "Reducir urgente", False)],
       "pie": "Poco frecuente"},
      {"titulo": "Fractura de tibia", "datos": [
          ("Longitud", "Deformidad en pierna", False), ("Rotación", "Distal a la rodilla", False),
          ("Paciente", "Trauma directo", False), ("Tratamiento", "Yeso o clavo", False)],
       "pie": "Riesgo compartimental"}]},
  ["Operar en las primeras 48 h reduce mortalidad y complicaciones.",
   "Rx de pelvis AP y axial de cadera confirman.",
   "Prevención: osteoporosis y caídas."],
  "AAOS – Management of hip fractures in older adults (2021)")

# CIR-090 · matriz
V("matriz", "CIR-090", "trauma-hipotension-yugulares-timpanismo-neumotorax-tension", "Choque obstructivo en el trauma",
  "CIRUGÍA ENAM: NEUMOTÓRAX A TENSIÓN", "CIRUGÍA",
  ("Lesiones torácicas que amenazan la vida", ["Yugulares + percusión + murmullo separan las causas",
   "Timpanismo con murmullo abolido e hipotensión = neumotórax a tensión"]),
  ("Varón de 35 años tras un accidente", ["PA 80/60 · FR 35 · SatO₂ 91 % · yugulares ingurgitadas", "Murmullo muy disminuido y timpanismo en hemitórax derecho"]),
  {"rotulo": "Signos que separan cada lesión", "eje_x": "Signo", "eje_y": "Lesión",
   "cols": ["Yugulares", "Percusión y murmullo"], "rows": ["Neumotórax a tensión", "Hemotórax masivo", "Taponamiento", "Contusión pulmonar"], "caso": (0, 1),
   "cells": [[("Ingurgitadas", []), ("TIMPANISMO, MV ABOLIDO", ["Desviación traqueal"])],
             [("Planas", ["Choque hipovolémico"]), ("Matidez, MV abolido", [])],
             [("Ingurgitadas", []), ("Normales", ["Ruidos cardiacos apagados"])],
             [("Normales", []), ("Crepitantes", ["Hipoxemia progresiva"])]]},
  ["Diagnóstico clínico: no esperar la Rx.",
   "Descompresión con aguja en el 4.º-5.º espacio, línea axilar media (ATLS 10-11).",
   "Luego tubo de tórax."],
  ATLS)

# CIR-091 · termómetro
V("termometro", "CIR-091", "trauma-abdominal-choque-no-responde-sangre-o-negativo", "Choque hemorrágico",
  "CIRUGÍA ENAM: CHOQUE HEMORRÁGICO", "CIRUGÍA",
  ("Choque hemorrágico", ["La clase de choque y cómo reacciona a los líquidos guían la transfusión",
   "Si no mejora con cristaloide: sangre O negativo sin esperar pruebas"]),
  ("Varón de 34 años tras un accidente de tránsito", ["PA 80/50 · FC 127 · pulso filiforme · abdomen distendido", "No responde a cristaloides: hipotensión y bradicardia"]),
  {"rotulo": "Clase de choque (ATLS)",
   "niveles": [("I", "< 15 %", ["Signos normales"]),
               ("II", "15-30 %", ["Taquicardia leve"]),
               ("III", "31-40 %", ["Hipotensión, FC > 120"]),
               ("IV", "> 40 %", ["NO RESPONDE A LÍQUIDOS", "Bradicardia: paro inminente"])],
   "caso_nivel": 3, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Sangre O Rh negativo", ["Sin esperar tipificación", "Protocolo de transfusión masiva 1:1:1"], True),
             (2, "Laparotomía de control de daños", ["Detener el sangrado"], False),
             (3, "Sangre tipo específica", ["Cuando esté disponible"], False)]},
  ["Limitar el cristaloide a 1 litro: más empeora la coagulopatía.",
   "Ácido tranexámico en las primeras 3 horas.",
   "Coloides y expansores no transportan oxígeno."],
  ATLS)

# CAR-057 · árbol
A("CAR-057", "rcp-monitor-fibrilacion-ventricular-desfibrilar", "Ritmo en el paro cardiaco",
  "CARDIOLOGÍA ENAM: FIBRILACIÓN VENTRICULAR", "CARDIOLOGÍA",
  ("Paro cardiaco", ["El ritmo del monitor decide si se desfibrila",
   "FV o TV sin pulso: descarga inmediata y seguir RCP"]),
  ("Reanimación en curso", ["El monitor muestra fibrilación ventricular"]),
  Q("¿Ritmo desfibrilable?", [
      L("Sí: FV o TV sin pulso", "DESFIBRILAR Y SEGUIR RCP", ["Descarga, luego 2 min de compresiones", "Adrenalina tras la 2.ª descarga"], path=True),
      L("No: asistolia o AESP", "RCP + adrenalina", ["Buscar causas reversibles"])], path=True),
  ("Fármacos en la FV", [("Adrenalina", False), ("Amiodarona", False), ("Lidocaína", False)], [
      ("Cuándo", ["Tras la 2.ª descarga", "Tras la 3.ª descarga", "Alternativa a amiodarona"]),
      ("Dosis", ["1 mg cada 3-5 min", "300 mg, luego 150", "1-1,5 mg/kg"])]),
  ["No detener las compresiones para mirar el monitor tras la descarga.",
   "Cada minuto sin desfibrilar baja la supervivencia 7-10 %.",
   "Los fármacos nunca reemplazan la descarga."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2025) · ERC – Guidelines (2025)")

# GIN-155 · embudo
V("embudo", "GIN-155", "18-semanas-dilatacion-sin-contracciones-incompetencia-cervical", "Dilatación sin contracciones",
  "OBSTETRICIA ENAM: INCOMPETENCIA CERVICAL", "OBSTETRICIA",
  ("Insuficiencia cervical", ["Dilatación indolora del cuello en el segundo trimestre",
   "Historia de pérdidas en el segundo trimestre sin contracciones"]),
  ("Gestante de 18 semanas con pesadez en hipogastrio", ["Partos inmaduros previos a las 27 y 25 semanas, sin contracciones", "Sin dinámica ni líquido · dilatación 5 cm, borramiento 60 %"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Cuello dilatado en el segundo trimestre",
   "candidatos": ["Incompetencia cervical", "Parto inmaduro", "Útero septado", "Útero bicorne"],
   "pasos": [("Sin contracciones uterinas", ["Parto inmaduro"]),
             ("Pérdidas previas por RPM indolora con dilatación", ["Útero septado", "Útero bicorne"])],
   "final": ("INCOMPETENCIA CERVICAL", ["Cerclaje en la próxima gestación (12-14 sem)", "Hoy: valorar cerclaje de rescate"]),
   "nota": "El diagnóstico es por la historia: dilatación sin dolor ni contracciones."},
  ["Las malformaciones uterinas causan abortos y malas presentaciones, no dilatación indolora.",
   "Cérvix < 25 mm antes de las 24 semanas con parto pretérmino previo: cerclaje.",
   "La progesterona vaginal ayuda si el cuello es corto."],
  "ACOG – Practice Bulletin 142: Cerclage for the management of cervical insufficiency (2014) · " + WILLIAMS)
