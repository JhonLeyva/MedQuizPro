"""Bloque 6 · parte E."""
from c6 import F6, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison's Principles of Internal Medicine 22.ª ed. (2025)"
GUYTON = "Guyton y Hall – Tratado de fisiología médica 14.ª ed. (2021)"

# INF-052 · matriz
V("matriz", "INF-052", "estudiante-medicina-anti-hbs-inmunidad", "Serología de la hepatitis B",
  "INFECTOLOGÍA ENAM: INMUNIDAD CONTRA HEPATITIS B", "INFECTOLOGÍA",
  ("Inmunidad contra hepatitis B", ["El anti-HBs ≥ 10 mUI/mL indica protección",
   "Vacunado: solo anti-HBs · infección pasada: anti-HBs + anti-HBc"]),
  ("Estudiante de medicina de 20 años", ["Iniciará prácticas en el hospital", "No recuerda si fue vacunado"]),
  {"rotulo": "Interpretación serológica", "eje_x": "Marcador", "eje_y": "Situación",
   "cols": ["HBsAg", "Anti-HBs", "Anti-HBc"], "rows": ["Vacunado", "Infección pasada", "Infección aguda", "Hepatitis crónica"], "caso": (0, 1),
   "cells": [[("Negativo", []), ("POSITIVO", ["≥ 10 mUI/mL"]), ("Negativo", ["Nunca se infectó"])],
             [("Negativo", []), ("Positivo", []), ("IgG positivo", [])],
             [("Positivo", []), ("Negativo", []), ("IgM positivo", [])],
             [("Positivo", ["> 6 meses"]), ("Negativo", []), ("IgG positivo", [])]]},
  ["El anti-HBc solo aparece tras la infección, nunca por la vacuna.",
   "Anti-HBs < 10: completar o repetir el esquema de 3 dosis.",
   "El personal de salud debe tener constancia de su respuesta a la vacuna."],
  "MINSA – NTS N.° 196-MINSA/DGIESP-2022 (Esquema Nacional de Vacunación) · CDC – Hepatitis B serologic test interpretation (2023)")

# CAR-042 · fases
V("fases", "CAR-042", "persona-se-desploma-calle-escena-segura", "Soporte vital básico: primeros pasos",
  "CARDIOLOGÍA ENAM: SOPORTE VITAL BÁSICO", "CARDIOLOGÍA",
  ("Soporte vital básico", ["El primer paso es comprobar que la escena sea segura",
   "Un rescatador herido no ayuda a nadie"]),
  ("Persona que se desploma en la calle", ["Usted está a su lado", "Terminó su entrenamiento en RCP"]),
  {"rotulo": "Secuencia del rescatador", "ans": 0,
   "fases": [("Seguridad", "Paso 1", "ESCENA SEGURA", ["Para usted y la víctima"]),
             ("Conciencia", "Paso 2", "¿Responde?", ["Tocar y hablar fuerte"]),
             ("Ayuda", "Paso 3", "Llamar al 106", ["Pedir un DEA"]),
             ("RCP", "Paso 4", "Compresiones 30:2", ["100-120 por minuto"])],
   "curvas": [],
   "chips_titulo": "Actuación inicial · marcado el correcto",
   "chips": [("Escena segura", True), ("¿Respira?", False), ("Boca arriba", False), ("Llamar al 106", False)]},
  ["No responde y no respira (o boquea): iniciar RCP.",
   "Compresiones de 5-6 cm, dejando que el tórax se reexpanda.",
   "Usar el DEA apenas llegue."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2020, act. 2025) · ERC – Guidelines (2025)")

# GAS-038 · embudo
V("embudo", "GAS-038", "nino-transfusion-7-semanas-ictericia-hepatitis-b", "Ictericia tras una transfusión",
  "GASTROENTEROLOGÍA ENAM: HEPATITIS B POSTRANSFUSIONAL", "GASTROENTEROLOGÍA",
  ("Hepatitis B aguda", ["Transmisión parenteral, sexual y vertical · incubación de 4 a 26 semanas",
   "Pródromo por inmunocomplejos: urticaria, artralgias, púrpura"]),
  ("Niño de 7 años con fatiga, anorexia e ictericia", ["Urticaria y lesiones purpúricas", "Transfusión hace 7 semanas en una cirugía"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Niño con ictericia tras una transfusión",
   "candidatos": ["Hepatitis B", "Hepatitis C", "Hepatitis A", "Hepatitis E", "Leptospirosis"],
   "pasos": [("Transfusión hace 7 semanas: vía parenteral", ["Hepatitis A", "Hepatitis E"]),
             ("Sin contacto con agua ni roedores", ["Leptospirosis"]),
             ("Urticaria y púrpura: pródromo por inmunocomplejos", ["Hepatitis C"])],
   "final": ("HEPATITIS B", ["Incubación de 4 a 26 semanas", "Pedir HBsAg e IgM anti-HBc"]),
   "nota": "El tamizaje de donantes redujo la hepatitis postransfusional, pero no la eliminó."},
  ["Hepatitis A y E: transmisión fecal-oral.",
   "La hepatitis C aguda suele ser asintomática.",
   "Hepatitis B en niños: alto riesgo de cronicidad."],
  "MINSA – NTS N.° 193-MINSA/DGIESP-2022 (Hepatitis B) · " + NELSON)

# NRL-029 · tarjetas
V("tarjetas", "NRL-029", "hipertenso-coma-pupilas-puntiformes-protuberancia", "Hemorragia hipertensiva: ¿dónde está?",
  "NEUROLOGÍA ENAM: HEMORRAGIA PONTINA", "NEUROLOGÍA",
  ("Hemorragia intracerebral hipertensiva", ["Sitios típicos: putamen, tálamo, protuberancia y cerebelo",
   "Protuberancia: coma, pupilas puntiformes, respiración irregular"]),
  ("Varón de 54 años hipertenso mal controlado", ["Caída súbita, no responde · Glasgow 4", "Respiración irregular, pupilas mióticas"]),
  {"rotulo": "¿Dónde sangró?", "ans": 0, "cards": [
      {"titulo": "PROTUBERANCIA", "datos": [
          ("Pupilas", "Puntiformes (mióticas)", True), ("Conciencia", "Coma profundo", True),
          ("Clave", "Respiración irregular", True)],
       "pie": "Tetraplejía, mal pronóstico"},
      {"titulo": "Tálamo", "datos": [
          ("Pupilas", "Mióticas, poco reactivas", False), ("Conciencia", "Variable", False),
          ("Clave", "Mirada hacia abajo", False)],
       "pie": "Hemianestesia contralateral"},
      {"titulo": "Putamen y cápsula interna", "datos": [
          ("Pupilas", "Normales", False), ("Conciencia", "Variable", False),
          ("Clave", "Hemiplejía, mira la lesión", False)],
       "pie": "La localización más frecuente"},
      {"titulo": "Cerebelo", "datos": [
          ("Pupilas", "Normales", False), ("Conciencia", "Alerta al inicio", False),
          ("Clave", "Ataxia, vómitos, vértigo", False)],
       "pie": "Cirugía si > 3 cm o hidrocefalia"}]},
  ["Pupilas puntiformes por lesión de la vía simpática descendente.",
   "Diagnóstico con TEM cerebral sin contraste.",
   "Controlar la PA: meta de PAS alrededor de 140 mmHg."],
  "AHA/ASA – Guideline for the management of spontaneous intracerebral hemorrhage (2022) · Adams and Victor's Principles of Neurology 12.ª ed. (2023)")

# END-027 · embudo
V("embudo", "END-027", "hemorragia-posparto-no-lacto-amenorrea-sheehan", "Amenorrea tras hemorragia posparto",
  "ENDOCRINOLOGÍA ENAM: SÍNDROME DE SHEEHAN", "ENDOCRINOLOGÍA",
  ("Síndrome de Sheehan", ["Necrosis isquémica de la hipófisis por hemorragia posparto con choque",
   "Primer signo: no puede lactar; luego amenorrea e hipopituitarismo"]),
  ("Mujer de 28 años con amenorrea", ["Hemorragia posparto con hipotensión grave", "No pudo dar de lactar"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Amenorrea tras hemorragia posparto",
   "candidatos": ["Síndrome de Sheehan", "Síndrome de Asherman", "Amenorrea hipotalámica", "Falla ovárica prematura", "Prolactinoma"],
   "pasos": [("No pudo lactar: falta prolactina", ["Prolactinoma"]),
             ("Sin legrado ni sinequias: falla la hipófisis", ["Síndrome de Asherman"]),
             ("Choque en el parto: necrosis hipofisaria", ["Amenorrea hipotalámica", "Falla ovárica prematura"])],
   "final": ("SÍNDROME DE SHEEHAN", ["Necrosis isquémica de la hipófisis", "FSH, LH y prolactina bajas"]),
   "nota": "Reponer primero el cortisol y después la tiroxina."},
  ["La hipófisis crece en el embarazo y es más sensible a la isquemia.",
   "Asherman: sinequias por legrado; la lactancia es normal.",
   "Falla ovárica: FSH alta; en Sheehan la FSH está baja."],
  "Endocrine Society – Hormonal replacement in hypopituitarism in adults (2016) · Williams Textbook of Endocrinology 15.ª ed. (2024)")

# INF-053 · embudo
V("embudo", "INF-053", "ribera-rimac-mialgia-pantorrillas-sufusion-leptospirosis", "Fiebre, ictericia y mialgias",
  "INFECTOLOGÍA ENAM: LEPTOSPIROSIS", "INFECTOLOGÍA",
  ("Leptospirosis", ["Zoonosis por contacto con agua o suelo contaminados con orina de roedores",
   "Mialgia de pantorrillas + sufusión conjuntival son características"]),
  ("Varón de 36 años de la ribera del río Rímac", ["Fiebre de 3 días y dolor de pantorrillas", "Ictericia, sufusión conjuntival, hepatoesplenomegalia"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Fiebre aguda con ictericia y mialgias",
   "candidatos": ["Leptospirosis", "Esporotricosis", "Nocardiosis", "Actinomicosis", "Lupus"],
   "pasos": [("Cuadro agudo de 3 días", ["Esporotricosis", "Actinomicosis"]),
             ("Inmunocompetente, sin lesión pulmonar", ["Nocardiosis"]),
             ("Ribera del río + pantorrillas + sufusión conjuntival", ["Lupus"])],
   "final": ("LEPTOSPIROSIS", ["Orina de roedores en el agua", "Forma ictérica: enfermedad de Weil"]),
   "nota": "Tratamiento: doxiciclina en casos leves; penicilina G o ceftriaxona en graves."},
  ["Enfermedad de Weil: ictericia, falla renal y hemorragia.",
   "Confirmación: ELISA IgM o microaglutinación (MAT).",
   "Hemorragia pulmonar: principal causa de muerte."],
  "MINSA – NTS N.° 049-MINSA/DGSP (Atención integral de leptospirosis) · OMS – Human leptospirosis: guidance for diagnosis, surveillance and control")

# SP-071 · radial
V("radial", "SP-071", "escolares-imc-mayor-25-sedentarismo", "Obesidad escolar: factores de riesgo",
  "SALUD PÚBLICA ENAM: OBESIDAD ESCOLAR", "SALUD PÚBLICA",
  ("Obesidad en escolares", ["Factores modificables principales: sedentarismo y alimentación",
   "Alcohol y tabaco no explican el exceso de peso"]),
  ("Colegio de secundaria en Lima", ["35% con IMC > 25", "8% con IMC > 30"]),
  {"rotulo": "Mapa del tema", "centro": "OBESIDAD", "centro_sub": "Escolares", "ans": 0,
   "items": [("SEDENTARISMO", ["< 60 min de actividad al día", "Pantallas > 2 horas"]),
             ("Dieta", ["Ultraprocesados, bebidas azucaradas"]),
             ("Sueño corto", ["Altera el apetito"]),
             ("Entorno", ["Kioscos no saludables"]),
             ("Genética", ["No modificable"])],
   "ruta": ["35% sobrepeso, 8% obesidad", "Factor modificable", "Alcohol y tabaco no explican", "SEDENTARISMO"]},
  ["OMS: 60 minutos diarios de actividad física moderada a vigorosa.",
   "Ley N.° 30021 de alimentación saludable y octógonos.",
   "En adolescentes se usa el IMC para la edad (percentiles o puntaje Z)."],
  "OMS – Directrices sobre actividad física y hábitos sedentarios (2020) · MINSA – Guía técnica de valoración nutricional del adolescente")

# CB-032 · matriz
V("matriz", "CB-032", "acceso-vena-femoral-medial-arteria", "Triángulo femoral: relaciones",
  "CIENCIAS BÁSICAS ENAM: ANATOMÍA DEL TRIÁNGULO FEMORAL", "CIENCIAS BÁSICAS",
  ("Vaina y triángulo femoral", ["De lateral a medial: nervio, arteria, vena, conducto femoral",
   "Referencia fiable: la vena está medial al pulso de la arteria"]),
  ("Varón de 42 años usuario de drogas EV", ["Venas de los brazos con cicatrices", "Solo son accesibles las venas femorales"]),
  {"rotulo": "Estructuras de lateral a medial", "eje_x": "Aspecto", "eje_y": "Estructura",
   "cols": ["Posición", "Uso clínico"], "rows": ["Nervio", "Arteria", "Vena", "Conducto femoral"], "caso": (2, 0),
   "cells": [[("Lateral", ["Fuera de la vaina"]), ("Bloqueo femoral", [])],
             [("Central", ["Pulso palpable"]), ("Punto de referencia", ["Punto medio inguinal"])],
             [("MEDIAL A LA ARTERIA", ["~ 1 cm medial al pulso"]), ("Acceso venoso", [])],
             [("Más medial", ["Linfáticos"]), ("Hernia femoral", [])]]},
  ["Regla mnemotécnica NAVEL: nervio, arteria, vena, espacio, linfáticos.",
   "El nervio femoral queda fuera de la vaina femoral.",
   "Guiar la punción con ecografía reduce complicaciones."],
  "Moore – Anatomía con orientación clínica 9.ª ed. (2022)")

# CIR-058 · árbol
A("CIR-058", "trauma-timon-matidez-hemotorax-tubo-toracico", "Hemotórax traumático",
  "CIRUGÍA ENAM: HEMOTÓRAX TRAUMÁTICO", "CIRUGÍA",
  ("Hemotórax traumático", ["Murmullo vesicular ausente + matidez + choque",
   "Tratamiento inmediato: tubo de drenaje torácico"]),
  ("Varón de 48 años, choque contra un poste", ["PA 80/60, FC 120, SatO₂ 88%", "MV ausente y matidez en la mitad inferior derecha"]),
  Q("¿MV ausente: matidez o timpanismo?", [
      L("Timpanismo + IY", "Neumotórax a tensión", ["Descompresión con aguja"]),
      Q("TUBO DE DRENAJE TORÁCICO", [
          L("≥ 1500 mL o 200 mL/h", "Toracotomía", ["Hemotórax masivo"]),
          L("Menor", "Observar", ["Reponer volumen, Rx de control"], path=True)],
        edge="Matidez: hemotórax", path=True)], path=True),
  ("Hemotórax vs neumotórax a tensión", [("Hemotórax", True), ("Neumotórax a tensión", False)], [
      ("Percusión", ["Matidez", "Timpanismo"]),
      ("Yugulares", ["Planas", "Ingurgitadas"]),
      ("Tratamiento", ["Tubo de tórax", "Aguja, luego tubo"])]),
  ["El diagnóstico es clínico: no esperar la TEM en un paciente inestable.",
   "Tubo de 28-32 Fr en el 5.º espacio intercostal, línea axilar media.",
   "La ventilación mecánica sin drenar puede empeorar el cuadro."],
  ATLS)

# GAS-039 · árbol
A("GAS-039", "pancreatitis-ictericia-bilirrubina-directa-colangiorresonancia", "Pancreatitis: buscar la causa",
  "GASTROENTEROLOGÍA ENAM: PANCREATITIS BILIAR", "GASTROENTEROLOGÍA",
  ("Pancreatitis aguda biliar", ["Causa más frecuente: cálculos que obstruyen la ampolla",
   "Si hay ictericia y la ecografía no aclara: colangiorresonancia"]),
  ("Mujer de 34 años con dolor, vómitos e ictericia", ["Amilasa 2400 U/L", "Bilirrubina total 4.0, directa 3.5"]),
  Q("¿Colangitis grave con sepsis?", [
      L("Sí", "CPRE urgente", ["En < 24 h"]),
      Q("¿La ecografía definió la causa?", [
          L("Sí", "Tratar la causa", ["Colecistectomía en la misma hospitalización"]),
          L("No, o sospecha de coledocolitiasis", "COLANGIORRESONANCIA", ["No invasiva", "Ve cálculos en el colédoco"], path=True)],
        edge="No", path=True)], path=True),
  ("Imágenes en pancreatitis", [("Eco", False), ("ColangioRM", True), ("TEM", False)], [
      ("Para qué", ["Litiasis vesicular", "Coledocolitiasis", "Necrosis"]),
      ("Cuándo", ["Al ingreso", "Si la eco no aclara", "Tras 72 h sin mejoría"])]),
  ["El monitoreo de la amilasa no define la causa ni la gravedad.",
   "La TEM temprana no aporta: se pide a las 72 h si no mejora.",
   "CPRE si se confirma coledocolitiasis o hay colangitis."],
  "ACG – Guideline: Management of acute pancreatitis (2024) · ASGE – Guideline on the management of choledocholithiasis (2019)")

# REU-027 · matriz
V("matriz", "REU-027", "rodilla-80000-leucocitos-artritis-septica", "Análisis del líquido sinovial",
  "REUMATOLOGÍA ENAM: ARTRITIS SÉPTICA", "REUMATOLOGÍA",
  ("Artritis séptica", ["Monoartritis aguda con líquido de > 50 000 leucocitos y PMN altos",
   "Urgencia: drenaje articular + antibiótico"]),
  ("Varón de 20 años con 2 días de dolor de rodilla", ["Tumefacción, signo del témpano (+)", "Líquido: > 80 000 leucocitos, 80% PMN"]),
  {"rotulo": "Tipos de líquido sinovial", "eje_x": "Hallazgo", "eje_y": "Líquido",
   "cols": ["Leucocitos/mm³", "% PMN"], "rows": ["Normal", "No inflamatorio", "Inflamatorio", "Séptico"], "caso": (3, 0),
   "cells": [[("< 200", []), ("< 25%", [])],
             [("200-2000", ["Artrosis"]), ("< 25%", [])],
             [("2000-50 000", ["Gota, AR"]), ("≥ 50%", ["Cristales en la gota"])],
             [("> 50 000", ["Este caso: > 80 000"]), ("> 75-80%", ["Gram y cultivo"])]]},
  ["Germen más frecuente: S. aureus; en joven sexualmente activo, pensar en gonococo.",
   "Siempre buscar cristales: gota y sepsis pueden coexistir.",
   "Tratamiento: lavado articular y antibiótico EV."],
  "EULAR – Recommendations for the management of septic arthritis (2023) · Kelley and Firestein's Textbook of Rheumatology 11.ª ed. (2020)")

# TRA-019 · termómetro
V("termometro", "TRA-019", "atropello-fractura-expuesta-conminuta-tibia-fijacion-externa", "Fractura expuesta de tibia",
  "TRAUMATOLOGÍA ENAM: FRACTURA EXPUESTA", "TRAUMATOLOGÍA",
  ("Fractura expuesta", ["Se clasifica con Gustilo-Anderson según la herida y la energía",
   "Conminuta o de alta energía: fijación externa"]),
  ("Varón de 20 años atropellado por una moto", ["Herida abierta en la pierna", "Fractura conminuta de tibia derecha"]),
  {"rotulo": "Clasificación de Gustilo",
   "niveles": [("< 1 cm", "Gustilo I", ["Herida limpia"]),
               ("1-10 cm", "Gustilo II", ["Daño moderado de partes blandas"]),
               ("> 10 cm", "Gustilo III", ["Conminuta, alta energía"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Antibiótico + antitetánica", ["Cefazolina ± gentamicina"], False),
             (2, "Lavado y desbridamiento", ["En quirófano, < 24 h"], False),
             (3, "FIJACIÓN EXTERNA", ["Estabiliza sin material interno"], True)]},
  ["Toda fractura conminuta abierta se considera Gustilo III.",
   "Yeso y tracción no permiten curar la herida.",
   "La fijación interna definitiva se difiere hasta controlar la contaminación."],
  "BOAST – Open fractures (2017, act. 2020) · Rockwood and Green's Fractures in Adults 10.ª ed. (2024)")

# SP-072 · tarjetas
V("tarjetas", "SP-072", "malaria-vivax-lima-sin-vector-ambiente", "Triada epidemiológica",
  "SALUD PÚBLICA ENAM: TRIADA EPIDEMIOLÓGICA", "SALUD PÚBLICA",
  ("Triada epidemiológica", ["Agente + hospedero + ambiente",
   "Sin el vector (ambiente) no hay transmisión de la malaria"]),
  ("Caso de malaria por P. vivax en Lima", ["Paciente de zona endémica", "En Lima no hay el mosquito vector"]),
  {"rotulo": "¿Qué elemento falla?", "ans": 0, "cards": [
      {"titulo": "AMBIENTE", "datos": [
          ("Qué es", "Clima, vector, entorno", True), ("En el caso", "Lima sin Anopheles", True),
          ("¿Favorece?", "No", True)],
       "pie": "Sin vector no hay transmisión"},
      {"titulo": "Agente", "datos": [
          ("Qué es", "El microorganismo", False), ("En el caso", "Plasmodium vivax", False),
          ("¿Favorece?", "Sí", False)],
       "pie": "Presente en la sangre"},
      {"titulo": "Hospedero", "datos": [
          ("Qué es", "Persona susceptible", False), ("En el caso", "Paciente infectado", False),
          ("¿Favorece?", "Sí", False)],
       "pie": "Fuente de infección"},
      {"titulo": "Tiempo", "datos": [
          ("Qué es", "No es de la triada", False), ("En el caso", "No aplica", False),
          ("¿Favorece?", "No aplica", False)],
       "pie": "Variable de persona, lugar y tiempo"}]},
  ["El vector de la malaria es el mosquito Anopheles.",
   "P. vivax deja hipnozoítos: primaquina para evitar recaídas.",
   "Caso importado: vigilar si aparecen casos autóctonos."],
  "OPS – Módulos de principios de epidemiología para el control de enfermedades (MOPECE) · MINSA – NTS de atención de la malaria")

# SP-073 · árbol
A("SP-073", "club-adulto-mayor-encuesta-100-poblacion", "Población y muestra",
  "SALUD PÚBLICA ENAM: POBLACIÓN DE ESTUDIO", "SALUD PÚBLICA",
  ("Población y muestra", ["Población: todos los elementos que se quiere estudiar",
   "Si se estudia al 100% no hay muestra: es un censo"]),
  ("Club del adulto mayor de un centro de salud", ["Se estudian sus características sociodemográficas", "Encuesta al 100% de los integrantes"]),
  Q("¿Se estudia al 100% de los integrantes?", [
      L("Sí", "POBLACIÓN", ["Censo: no hay muestreo"], path=True),
      Q("¿Cómo se elige la parte?", [
          L("Al azar", "Muestra probabilística", ["Aleatoria, estratificada"]),
          L("A criterio", "No probabilística", ["Por conveniencia"])],
        edge="No, solo una parte")], path=True),
  ("Términos del muestreo", [("Población", True), ("Muestra", False), ("Estrato", False)], [
      ("Qué es", ["Todos los elementos", "Subconjunto", "Subgrupo homogéneo"]),
      ("Ejemplo", ["Todo el club", "Algunos socios", "Socios por sexo"])]),
  ["La muestra debe ser representativa de la población.",
   "Muestreo estratificado: se divide en estratos y se sortea en cada uno.",
   "Conglomerado: se sortean grupos completos."],
  "Hernández-Sampieri – Metodología de la investigación 7.ª ed. (2023) · Gordis – Epidemiology 6.ª ed. (2019)")

# CAR-043 · puntaje
V("puntaje", "CAR-043", "golpe-precordial-ruidos-apagados-iy-ecocardiograma", "Trauma precordial con hipotensión",
  "CARDIOLOGÍA ENAM: TRAUMA CARDIACO", "CARDIOLOGÍA",
  ("Trauma cardiaco cerrado", ["Puede causar contusión miocárdica o taponamiento",
   "ECG y ecocardiograma de inmediato"]),
  ("Varón de 52 años con golpe precordial hace 6 horas", ["Dolor, palpitaciones y mareos · PA 90/60", "Ruidos apagados, IY (+) · troponina elevada"]),
  {"rotulo": "Tríada de Beck en el caso", "escala": "Beck", "total": 3, "max": 3,
   "total_label": "Signos presentes",
   "interpreta": "Sospecha de taponamiento cardiaco",
   "items": [("Hipotensión (PA 90/60)", "1", True), ("Ingurgitación yugular", "1", True),
             ("Ruidos cardiacos apagados", "1", True)],
   "bandas": [("0-1", "Poco probable", "ECG, troponina y monitoreo", False),
              ("2", "Posible", "Ecocardiograma", False),
              ("3", "Tríada completa", "ECG + ecocardiograma urgentes; pericardiocentesis", True)]},
  ["La troponina alta con ECG alterado sugiere contusión miocárdica.",
   "FAST o ecocardiograma: derrame pericárdico.",
   "Los diuréticos empeoran el taponamiento (depende de la precarga)."],
  "EAST – Screening for blunt cardiac injury (2012) · " + ATLS)

# PED-110 · puntaje
V("puntaje", "PED-110", "lactante-diarrea-soporoso-llenado-5-seg-bolo", "Deshidratación grave con choque",
  "PEDIATRÍA ENAM: DESHIDRATACIÓN GRAVE", "PEDIATRÍA",
  ("Deshidratación grave con choque", ["Piel fría y llenado capilar lento: choque hipovolémico",
   "Primero bolo de NaCl 0.9% 20 mL/kg y luego Plan C"]),
  ("Lactante de 10 meses con 3 días de diarrea y vómitos", ["Soporoso, ojos muy hundidos, pliegue (+)", "Piel fría · llenado capilar 5 segundos"]),
  {"rotulo": "Signos AIEPI de deshidratación grave", "escala": "AIEPI", "total": 3, "max": 4,
   "total_label": "Signos presentes",
   "interpreta": "Deshidratación grave con choque",
   "items": [("Letárgico o inconsciente", "1", True), ("Ojos hundidos", "1", True),
             ("No puede beber o bebe mal", "1", False), ("Pliegue cutáneo muy lento", "1", True)],
   "bandas": [("0-1", "No es grave", "Evaluar algún grado: Plan A o B", False),
              ("≥ 2", "Grave", "Choque: bolo NaCl 0.9% 20 mL/kg, luego Plan C", True)]},
  ["Plan C (< 12 meses): 30 mL/kg en 1 h y 70 mL/kg en 5 h.",
   "La dextrosa al 5% no expande el volumen.",
   "Pasar a SRO apenas pueda beber."],
  "OMS/OPS – AIEPI: cuadros de procedimientos · MINSA – GPC de enfermedad diarreica aguda en niños (2017)")

# HEM-022 · embudo
V("embudo", "HEM-022", "vcm-110-hipersegmentados-parestesias-megaloblastica", "Anemia macrocítica con parestesias",
  "HEMATOLOGÍA ENAM: ANEMIA MEGALOBLÁSTICA", "HEMATOLOGÍA",
  ("Anemia megaloblástica", ["Macrocitosis + neutrófilos hipersegmentados + macroovalocitos",
   "Déficit de B12: además da neuropatía (cordones posteriores)"]),
  ("Varón de 75 años con 6 meses de fatiga", ["Parestesias, menor sensibilidad vibratoria", "Hb 9 · VCM 110 · neutrófilos hipersegmentados"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Anciano con anemia y parestesias",
   "candidatos": ["Megaloblástica", "Talasemia", "Ferropénica", "Sideroblástica", "Alcohol o hepatopatía"],
   "pasos": [("VCM 110 fL: macrocítica", ["Talasemia", "Ferropénica"]),
             ("Hipersegmentados y macroovalocitos", ["Alcohol o hepatopatía"]),
             ("Sin sideroblastos en anillo; suele ser microcítica", ["Sideroblástica"])],
   "final": ("ANEMIA MEGALOBLÁSTICA", ["Por déficit de vitamina B12", "Neuropatía de cordones posteriores"]),
   "nota": "Dar B12 antes que ácido fólico: el folato solo puede empeorar la neuropatía."},
  ["Causa más frecuente de déficit de B12: anemia perniciosa.",
   "Metformina e IBP prolongados también la reducen.",
   "Homocisteína y ácido metilmalónico altos confirman el déficit de B12."],
  "BSH – Guidelines for the diagnosis and treatment of cobalamin and folate disorders (2014) · " + HARRISON)

# REU-028 · tarjetas
V("tarjetas", "REU-028", "prurito-nocturno-interdigital-escabiosis", "Prurito nocturno en el niño",
  "DERMATOLOGÍA ENAM: ESCABIOSIS", "DERMATOLOGÍA",
  ("Escabiosis", ["Prurito nocturno intenso por Sarcoptes scabiei",
   "Pápulas y surcos en pliegues interdigitales, muñecas, axilas y genitales"]),
  ("Niño de 9 años con 1 mes de prurito", ["Empeora en la noche, respeta la cara", "Pápulas en interdigitales, muñecas, glúteos y genitales"]),
  {"rotulo": "¿Qué dermatosis es?", "ans": 0, "cards": [
      {"titulo": "ESCABIOSIS", "datos": [
          ("Prurito", "Nocturno, intenso", True), ("Lesiones", "Pápulas y surcos", True),
          ("Dónde", "Interdigital, genitales", True)],
       "pie": "Tratar a todos los contactos"},
      {"titulo": "Urticaria papulosa", "datos": [
          ("Prurito", "Variable", False), ("Lesiones", "Pápula con punto central", False),
          ("Dónde", "Zonas expuestas", False)],
       "pie": "Picaduras de insectos"},
      {"titulo": "Dermatitis herpetiforme", "datos": [
          ("Prurito", "Intenso, ardoroso", False), ("Lesiones", "Vesículas agrupadas", False),
          ("Dónde", "Codos, rodillas, glúteos", False)],
       "pie": "Asociada a celiaquía"},
      {"titulo": "Exantema vírico", "datos": [
          ("Prurito", "Leve o ausente", False), ("Lesiones", "Máculas y pápulas", False),
          ("Dónde", "Tronco, generalizado", False)],
       "pie": "Con fiebre, dura días"}]},
  ["Tratamiento: permetrina 5% en todo el cuerpo, repetir a los 7 días.",
   "Alternativa: ivermectina oral en mayores de 15 kg.",
   "Lavar con agua caliente la ropa y las sábanas."],
  "IACS – Consensus criteria for the diagnosis of scabies (Br J Dermatol 2020) · Fitzpatrick's Dermatology 9.ª ed. (2019)")

# OFT-024 · embudo
V("embudo", "OFT-024", "prurito-conducto-otorrea-otitis-externa", "Otorrea con prurito del conducto",
  "OTORRINOLARINGOLOGÍA ENAM: OTITIS EXTERNA", "OTORRINOLARINGOLOGÍA",
  ("Otitis externa", ["Infección del conducto auditivo externo (Pseudomonas, S. aureus)",
   "Prurito, otalgia a la tracción del pabellón, otorrea e hipoacusia"]),
  ("Varón de 15 años con prurito intenso en el oído", ["Hipoacusia y otorrea purulenta", "T 39 °C · adenopatía retroauricular"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Adolescente con otorrea y prurito",
   "candidatos": ["Otitis externa", "Otitis media", "Otitis interna", "Celulitis", "Dermatosis"],
   "pasos": [("Sin vértigo ni nistagmo", ["Otitis interna"]),
             ("Fiebre, pus y adenopatía: infección aguda", ["Dermatosis"]),
             ("Prurito y otorrea del conducto externo", ["Otitis media", "Celulitis"])],
   "final": ("OTITIS EXTERNA", ["Pseudomonas o S. aureus", "Gotas de quinolona ± corticoide"]),
   "nota": "Dolor a la tracción del pabellón o al presionar el trago; en diabéticos mayores descartar otitis externa maligna."},
  ["Factores: humedad (nadadores), hisopos, audífonos.",
   "Limpiar el conducto antes de aplicar las gotas.",
   "Antibiótico oral si hay celulitis periauricular o fiebre persistente."],
  "AAO-HNS – Clinical practice guideline: acute otitis externa (2014) · Cummings Otolaryngology 7.ª ed. (2021)")

# NEF-040 · termómetro
V("termometro", "NEF-040", "anciana-sopor-sodio-115-tiazida", "Hiponatremia por tiazidas",
  "NEFROLOGÍA ENAM: HIPONATREMIA POR TIAZIDAS", "NEFROLOGÍA",
  ("Hiponatremia por tiazidas", ["Las tiazidas impiden diluir la orina en el túbulo distal",
   "Riesgo mayor en ancianas delgadas"]),
  ("Mujer de 78 años, desorientada y luego soporosa", ["ICC: losartán, digoxina, atorvastatina, HCTZ", "Na 115 mEq/L"]),
  {"rotulo": "Gravedad de la hiponatremia",
   "niveles": [("130-134", "Leve", ["Suele ser asintomática"]),
               ("125-129", "Moderada", ["Náuseas, cefalea"]),
               ("< 125", "Grave", ["Confusión, sopor, convulsión"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "SUSPENDER LA TIAZIDA", ["Causa del cuadro"], True),
             (2, "NaCl 3% en bolo", ["150 mL en 20 min si hay síntomas graves"], False),
             (3, "Corregir ≤ 10 mEq/L en 24 h", ["Evita la desmielinización osmótica"], False)]},
  ["Las tiazidas causan hiponatremia; los diuréticos de asa, rara vez.",
   "También dan hipopotasemia, hiperuricemia e hipercalcemia.",
   "Losartán y digoxina no bajan el sodio."],
  "European Hyponatraemia Guideline (ESE/ESICM/ERA 2014) · " + HARRISON)

# CB-033 · radial
V("radial", "CB-033", "aldosterona-celulas-principales-tubulo-colector", "Células del riñón y sus funciones",
  "CIENCIAS BÁSICAS ENAM: FISIOLOGÍA RENAL", "CIENCIAS BÁSICAS",
  ("Aldosterona", ["Actúa en las células principales del túbulo colector",
   "Aumenta ENaC y la bomba Na⁺/K⁺: reabsorbe Na⁺ y secreta K⁺"]),
  ("Pregunta de concepto", ["Células donde actúa la aldosterona", "para reabsorber sodio"]),
  {"rotulo": "Mapa del tema", "centro": "RIÑÓN", "centro_sub": "Células y funciones", "ans": 0,
   "items": [("PRINCIPALES", ["Aldosterona: ENaC y Na⁺/K⁺", "Reabsorben Na⁺, secretan K⁺"]),
             ("Intercaladas", ["Secretan H⁺ o HCO₃⁻"]),
             ("Yuxtaglomerulares", ["Producen renina"]),
             ("Mesangiales", ["Soporte del glomérulo"]),
             ("Intersticiales", ["Eritropoyetina"])],
   "ruta": ["Aldosterona", "Receptor mineralocorticoide", "↑ ENaC y bomba Na⁺/K⁺", "CÉLULAS PRINCIPALES"]},
  ["La ADH actúa en las mismas células principales (acuaporina 2).",
   "Espironolactona bloquea el receptor de la aldosterona.",
   "Amilorida bloquea el ENaC."],
  GUYTON)

# SP-074 · radial
V("radial", "SP-074", "nino-10-anos-acepta-procedimiento-asentimiento", "Decisiones en el menor de edad",
  "SALUD PÚBLICA ENAM: ASENTIMIENTO INFORMADO", "SALUD PÚBLICA",
  ("Asentimiento informado", ["El niño expresa su aceptación o negativa tras recibir información adaptada",
   "Se suma al consentimiento de los padres, no lo reemplaza"]),
  ("Pregunta de concepto", ["Niño de 10 años ante un procedimiento", "o un ensayo clínico"]),
  {"rotulo": "Mapa del tema", "centro": "MENOR DE EDAD", "centro_sub": "Toma de decisiones", "ans": 0,
   "items": [("ASENTIMIENTO", ["El niño acepta o se niega", "Con información adaptada"]),
             ("Consentimiento", ["De los padres o tutor"]),
             ("Información", ["Clara y según su edad"]),
             ("Voluntariedad", ["Sin presión"]),
             ("Revocación", ["Puede retirarse"])],
   "ruta": ["Niño de 10 años", "Información adaptada", "Expresa su voluntad", "ASENTIMIENTO"]},
  ["En ensayos sin beneficio directo, la negativa del niño debe respetarse.",
   "El consentimiento informado lo firma el adulto capaz o el representante.",
   "Base: Reglamento de Ensayos Clínicos del Perú (DS N.° 021-2017-SA)."],
  "INS – Reglamento de Ensayos Clínicos (DS N.° 021-2017-SA) · CIOMS – Pautas éticas internacionales (2016)")

# CB-034 · tarjetas
V("tarjetas", "CB-034", "antiacido-hidroxido-aluminio-hipofosfatemia", "Antiácidos y sus efectos",
  "CIENCIAS BÁSICAS ENAM: FARMACOLOGÍA DE ANTIÁCIDOS", "CIENCIAS BÁSICAS",
  ("Hidróxido de aluminio", ["Se une al fosfato en el intestino e impide su absorción",
   "Uso prolongado: hipofosfatemia, debilidad y osteomalacia"]),
  ("Mujer de 65 años con epigastralgia de larga data", ["Se automedica con hidróxido de aluminio", "Se piden análisis de laboratorio"]),
  {"rotulo": "¿Qué efecto tiene?", "ans": 0, "cards": [
      {"titulo": "HIDRÓXIDO DE ALUMINIO", "datos": [
          ("Efecto GI", "Estreñimiento", True), ("Electrolito", "Hipofosfatemia", True),
          ("Riesgo", "Osteomalacia", True)],
       "pie": "Quela el fosfato en el intestino"},
      {"titulo": "Hidróxido de magnesio", "datos": [
          ("Efecto GI", "Diarrea", False), ("Electrolito", "Hipermagnesemia", False),
          ("Riesgo", "En falla renal", False)],
       "pie": "Se combina con aluminio"},
      {"titulo": "Carbonato de calcio", "datos": [
          ("Efecto GI", "Estreñimiento", False), ("Electrolito", "Hipercalcemia", False),
          ("Riesgo", "Síndrome leche-álcali", False)],
       "pie": "Rebote ácido"},
      {"titulo": "Bicarbonato de sodio", "datos": [
          ("Efecto GI", "Eructos, distensión", False), ("Electrolito", "Alcalosis metabólica", False),
          ("Riesgo", "Sobrecarga de sodio", False)],
       "pie": "Evitar en ICC e HTA"}]},
  ["En la falla renal el aluminio se acumula: encefalopatía y osteodistrofia.",
   "Se usó como quelante de fósforo en la ERC.",
   "Una epigastralgia crónica merece estudio, no automedicación."],
  "Goodman & Gilman – Las bases farmacológicas de la terapéutica 14.ª ed. (2023)")

# SP-075 · radial
V("radial", "SP-075", "dengue-importado-aedes-participacion-comunitaria", "Prevención de dengue autóctono",
  "SALUD PÚBLICA ENAM: CONTROL DEL DENGUE", "SALUD PÚBLICA",
  ("Prevención del dengue", ["Sin criaderos no hay Aedes: la clave es eliminarlos en cada casa",
   "Requiere participación de la comunidad"]),
  ("Centro de salud I-4", ["Casos importados de dengue", "Presencia de Aedes aegypti"]),
  {"rotulo": "Mapa del tema", "centro": "DENGUE", "centro_sub": "Evitar casos autóctonos", "ans": 0,
   "items": [("COMUNIDAD", ["Eliminar criaderos", "Tapar y lavar recipientes"]),
             ("Control larvario", ["Larvicida en depósitos"]),
             ("Fumigación", ["Si hay transmisión"]),
             ("Vigilancia", ["Índice aédico, febriles"]),
             ("Febriles", ["Mosquitero y repelente"])],
   "ruta": ["Casos importados + Aedes", "Riesgo de transmisión", "Eliminar criaderos", "PARTICIPACIÓN COMUNITARIA"]},
  ["Los antipiréticos no previenen la transmisión.",
   "Evitar AINE en el dengue: usar paracetamol.",
   "Índice aédico > 2%: alto riesgo de transmisión."],
  "MINSA – NTS N.° 211-MINSA/DGIESP-2024 (Atención del dengue) · OPS – Estrategia de gestión integrada para arbovirosis (EGI-Arbovirus)")

# REU-029 · termómetro
V("termometro", "REU-029", "nina-12-anos-30-comedones-acne-leve", "Acné: grados de severidad",
  "DERMATOLOGÍA ENAM: ACNÉ", "DERMATOLOGÍA",
  ("Acné vulgar", ["Se clasifica por el tipo de lesión predominante",
   "Solo comedones: acné comedoniano (leve)"]),
  ("Niña de 12 años con acné", ["Unos 30 comedones en el rostro", "Sin pápulas ni nódulos descritos"]),
  {"rotulo": "Severidad",
   "niveles": [("Leve", "Comedoniano", ["Solo comedones"]),
               ("Moderado", "Pápulo-pustular", ["Lesiones inflamatorias"]),
               ("Grave", "Nodular", ["Nódulos, cicatrices"]),
               ("Muy grave", "Conglobata", ["Abscesos, fístulas"])],
   "caso_nivel": 0, "ruta_titulo": "Tratamiento", "paso_label": "PASO",
   "pasos": [(1, "RETINOIDE TÓPICO", ["Adapaleno o tretinoína"], True),
             (2, "+ Peróxido de benzoilo", ["± antibiótico tópico si hay pápulas"], False),
             (3, "Isotretinoína oral", ["Nodular o refractario"], False)]},
  ["El comedón (abierto o cerrado) es la lesión inicial del acné.",
   "No usar antibiótico tópico solo: genera resistencia.",
   "Isotretinoína: teratogénica, requiere anticoncepción."],
  "AAD – Guidelines of care for the management of acne vulgaris (2024)")

# OFT-025 · matriz
V("matriz", "OFT-025", "leganas-mucopurulentas-bilateral-conjuntivitis", "Tipos de conjuntivitis",
  "OFTALMOLOGÍA ENAM: CONJUNTIVITIS BACTERIANA", "OFTALMOLOGÍA",
  ("Conjuntivitis infecciosa", ["Ojo rojo sin dolor ni pérdida de visión",
   "Secreción mucopurulenta con legañas: bacteriana"]),
  ("Adolescente de 15 años con 3 días de secreción", ["Mucopurulenta, legañas en ambos ojos", "Sensación de cuerpo extraño, sin dolor · visión normal"]),
  {"rotulo": "Según la secreción", "eje_x": "Hallazgo", "eje_y": "Tipo",
   "cols": ["Secreción", "Otros signos"], "rows": ["Bacteriana", "Viral", "Alérgica"], "caso": (0, 0),
   "cells": [[("MUCOPURULENTA", ["Legañas, párpados pegados"]), ("Sin dolor", ["Visión normal"])],
             [("Acuosa", ["Adenopatía preauricular"]), ("Folículos", ["Muy contagiosa"])],
             [("Mucosa, filante", []), ("Prurito intenso", ["Papilas, atopia"])]]},
  ["Dolor, fotofobia o baja visual: pensar en queratitis, uveítis o glaucoma.",
   "Tratamiento: antibiótico tópico (tobramicina, quinolona) e higiene.",
   "Dacriocistitis: tumefacción dolorosa en el ángulo interno."],
  "AAO – Preferred Practice Pattern: Conjunctivitis (2023)")

# INF-054 · fases
V("fases", "INF-054", "adulta-cefalea-rigidez-nuca-neumococo", "Meningitis: germen según la edad",
  "INFECTOLOGÍA ENAM: MENINGITIS BACTERIANA", "INFECTOLOGÍA",
  ("Meningitis bacteriana del adulto", ["Neumococo: primera causa en adultos, a menudo tras una infección respiratoria",
   "Fiebre + rigidez de nuca + alteración de conciencia"]),
  ("Mujer de 25 años con cefalea, vómitos y somnolencia", ["Resfriado hace una semana", "Glasgow 12, T 39 °C, rigidez de nuca"]),
  {"rotulo": "Etiología según la edad", "ans": 2,
   "fases": [("Neonato", "< 1 mes", "SGB, E. coli", ["Listeria"]),
             ("Niño", "1 m-18 a", "Neumococo", ["Meningococo"]),
             ("Adulto", "18-50 a", "NEUMOCOCO", ["Meningococo"]),
             ("Mayor", "> 50 años", "Neumococo", ["+ Listeria"])],
   "curvas": [],
   "chips_titulo": "Germen · marcado el correcto",
   "chips": [("S. pneumoniae", True), ("N. meningitidis", False), ("Listeria", False), ("H. influenzae", False)]},
  ["Empírico en adultos: ceftriaxona + vancomicina + dexametasona.",
   "Agregar ampicilina si > 50 años o inmunosuprimido (Listeria).",
   "TEM antes de la punción si hay déficit focal, convulsión o Glasgow bajo."],
  "ESCMID – Guideline: diagnosis and treatment of acute bacterial meningitis (2016) · IDSA – Bacterial meningitis (2004)")

# GAS-040 · radial
V("radial", "GAS-040", "obeso-pirosis-asma-nocturna-ibp", "ERGE con síntomas extraesofágicos",
  "GASTROENTEROLOGÍA ENAM: ENFERMEDAD POR REFLUJO", "GASTROENTEROLOGÍA",
  ("Enfermedad por reflujo gastroesofágico", ["Pirosis y regurgitación; puede dar asma, tos o dolor torácico",
   "Sin signos de alarma: prueba terapéutica con IBP"]),
  ("Varón obeso de 45 años con 1 año de síntomas", ["Pirosis, dolor retroesternal atípico, disfagia", "En la noche «le ronca el pecho»"]),
  {"rotulo": "Mapa del tema", "centro": "ERGE", "centro_sub": "Manejo inicial", "ans": 0,
   "items": [("IBP 8 SEMANAS", ["Prueba terapéutica", "Antes del desayuno"]),
             ("Típicos", ["Pirosis, regurgitación"]),
             ("Extraesofágicos", ["Asma nocturna, tos, disfonía"]),
             ("Estilo de vida", ["Bajar de peso, elevar cabecera"]),
             ("Endoscopia", ["Alarma o falta de respuesta"])],
   "ruta": ["Pirosis + asma nocturna", "Obesidad: factor de riesgo", "Prueba terapéutica", "IBP"]},
  ["Si la disfagia progresa o hay pérdida de peso o sangrado: endoscopia.",
   "La pH-metría se reserva para casos refractarios.",
   "La obesidad aumenta la presión intraabdominal y el reflujo."],
  "ACG – Clinical guideline for the diagnosis and management of GERD (2022)")

# END-028 · matriz
V("matriz", "END-028", "siadh-vs-privacion-agua-osmolaridad-plasmatica", "SIADH frente a deshidratación",
  "ENDOCRINOLOGÍA ENAM: SIADH", "ENDOCRINOLOGÍA",
  ("SIADH", ["ADH alta de forma inapropiada con plasma diluido",
   "La osmolaridad plasmática los distingue: alta en privación de agua, baja en SIADH"]),
  ("Pregunta de concepto", ["Persona sana privada de agua", "frente a una persona con SIADH"]),
  {"rotulo": "Qué los diferencia", "eje_x": "Parámetro", "eje_y": "Situación",
   "cols": ["Osm. plasmática", "Osm. urinaria", "ADH"], "rows": ["Privación de agua", "SIADH"], "caso": (1, 0),
   "cells": [[("Alta (> 295)", ["Hipernatremia"]), ("Alta", ["Concentrada"]), ("Alta", ["Apropiada"])],
             [("BAJA (< 275)", ["Hiponatremia"]), ("Alta", ["Inapropiada"]), ("Alta", ["Inapropiada"])]]},
  ["En ambos casos la orina está concentrada y la ADH alta.",
   "SIADH: euvolemia, Na urinario > 30, sin edemas.",
   "Causas: cáncer de pulmón microcítico, fármacos, patología del SNC."],
  GUYTON + " · European Hyponatraemia Guideline (2014)")

# GAS-041 · fases
V("fases", "GAS-041", "necrosis-pancreatica-drenaje-3-4-semanas", "Necrosis pancreática: cuándo drenar",
  "GASTROENTEROLOGÍA ENAM: NECROSIS PANCREÁTICA", "GASTROENTEROLOGÍA",
  ("Necrosis pancreática", ["Se interviene cuando la colección está encapsulada",
   "Drenaje diferido a las 3-4 semanas: menor mortalidad"]),
  ("Mujer de 55 años con pancreatitis aguda grave", ["Sospecha de necrosis", "Se decide intervenir"]),
  {"rotulo": "Evolución de la necrosis", "ans": 2,
   "fases": [("Temprana", "Sem 1-2", "Soporte", ["Fluidos, analgesia, nutrición"]),
             ("Colección", "Sem 2-3", "Necrosis aguda", ["Aún sin pared"]),
             ("Encapsulada", "Sem 3-4", "DRENAJE", ["Percutáneo o endoscópico"]),
             ("Tardía", "> 4 sem", "Necrosectomía", ["Si el drenaje no basta"])],
   "curvas": [("Pared", SKY, [0.0, 0.05, 0.2, 0.5, 0.8, 0.95, 1.0]),
              ("Mortal.", ROSE, [0.9, 0.75, 0.5, 0.3, 0.2, 0.15, 0.1])],
   "chips_titulo": "Momento del drenaje · marcado el correcto",
   "chips": [("3-4 semanas", True), ("1-2 semanas", False), ("6-7 semanas", False), ("7-8 semanas", False)]},
  ["Indicación de drenar: necrosis infectada o sintomática.",
   "Estrategia «step-up»: drenaje primero, necrosectomía si falla.",
   "La cirugía temprana aumenta la mortalidad."],
  "ACG – Guideline: Management of acute pancreatitis (2024) · IAP/APA – Evidence-based guidelines (2013)")

# GIN-101 · árbol
A("GIN-101", "vih-prueba-rapida-8-cm-zidovudina-parto-vaginal", "VIH diagnosticado en el trabajo de parto",
  "OBSTETRICIA ENAM: VIH Y PARTO", "OBSTETRICIA",
  ("VIH en el trabajo de parto", ["Zidovudina EV durante el parto y profilaxis al RN",
   "Con dilatación avanzada: parto vaginal"]),
  ("Primigesta de 38 semanas sin controles", ["Prueba rápida de VIH (+)", "8 cm, 100% borrado, +1, membranas íntegras"]),
  Q("¿Labor avanzada o membranas rotas?", [
      L("No", "Cesárea electiva", ["+ zidovudina EV antes"]),
      L("Sí: 8 cm, +1", "ZIDOVUDINA EV + PARTO VAGINAL", ["Evitar episiotomía y amniotomía", "Iniciar TAR"], path=True)], path=True),
  ("Cuidados en el parto", [("Hacer", True), ("Evitar", False)], [
      ("Parto", ["Pinzamiento inmediato del cordón", "Episiotomía, amniotomía"]),
      ("Recién nacido", ["Profilaxis antirretroviral", "Lactancia materna"])]),
  ["Zidovudina EV: 2 mg/kg en la 1.ª hora y luego 1 mg/kg/h hasta el parto.",
   "La cesárea protege solo si se hace antes de la labor y con membranas íntegras.",
   "Sucedáneo de leche materna para el RN."],
  "MINSA – NTS N.° 159-MINSA/2019/DGIESP (Transmisión materno-infantil de VIH, sífilis y hepatitis B)")

# PSI-020 · termómetro
V("termometro", "PSI-020", "desempleo-animo-decaido-ideas-suicidas-sertralina", "Depresión: tratamiento por gravedad",
  "PSIQUIATRÍA ENAM: DEPRESIÓN CON IDEACIÓN SUICIDA", "PSIQUIATRÍA",
  ("Episodio depresivo", ["Ánimo decaído, insomnio e ideas de muerte",
   "Tratamiento: ISRS (sertralina) + psicoterapia"]),
  ("Varón de 49 años que perdió su trabajo", ["Ánimo muy decaído, insomnio", "Piensa en «quitarse la vida» · recibe soporte psicológico"]),
  {"rotulo": "Gravedad",
   "niveles": [("Leve", "Pocos síntomas", ["Funciona con esfuerzo"]),
               ("Moderada", "Más síntomas", ["Deterioro funcional"]),
               ("Grave", "Ideación suicida", ["Incapacidad marcada"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Evaluar riesgo suicida", ["Plan, medios, intentos previos"], False),
             (2, "SERTRALINA + PSICOTERAPIA", ["ISRS de primera línea"], True),
             (3, "Hospitalizar si hay plan o intento", ["O síntomas psicóticos"], False)]},
  ["El efecto del ISRS aparece en 2-4 semanas: controlar pronto.",
   "Haloperidol, risperidona y quetiapina son antipsicóticos.",
   "Al inicio del ISRS puede aumentar el riesgo suicida: vigilar."],
  "NICE – Depression in adults: treatment and management (2022) · MINSA – Guía técnica de depresión en el primer nivel")

# GIN-102 · termómetro
V("termometro", "GIN-102", "rciu-percentil-2-flujo-diastolico-invertido-terminar", "Restricción del crecimiento fetal",
  "OBSTETRICIA ENAM: RESTRICCIÓN DEL CRECIMIENTO FETAL", "OBSTETRICIA",
  ("Restricción del crecimiento intrauterino", ["Se estadifica con el Doppler",
   "Flujo diastólico invertido en la arteria umbilical: terminar desde las 30 semanas"]),
  ("Primigesta de 36 semanas con menos movimientos", ["AU 27 cm · peso fetal percentil 2", "Oligohidramnios · flujo diastólico final invertido"]),
  {"rotulo": "Estadios (Figueras-Gratacós)",
   "niveles": [("Estadio I", "PEG severo", ["Doppler con resistencia leve"]),
               ("Estadio II", "FDA ausente", ["Arteria umbilical"]),
               ("Estadio III", "Flujo reverso", ["Arteria umbilical"]),
               ("Estadio IV", "DV reverso", ["o registro patológico"])],
   "caso_nivel": 2, "ruta_titulo": "Momento del parto", "paso_label": "PASO",
   "pasos": [(1, "Estadio I: 37 semanas", ["Inducción posible"], False),
             (2, "Estadio II: 34 semanas", ["Cesárea"], False),
             (3, "TERMINAR LA GESTACIÓN", ["Estadio III desde 30 sem · cesárea"], True)]},
  ["Estadio IV: terminar desde las 26 semanas.",
   "Corticoides antenatales si es menor de 34 semanas.",
   "Sulfato de magnesio para neuroprotección si es menor de 32 semanas."],
  "FMF/Figueras & Gratacós – Stage-based approach to FGR (Fetal Diagn Ther 2014) · ISUOG – Practice guidelines: FGR (2020)")

# PED-111 · fases
V("fases", "PED-111", "neumonia-lactante-mejoria-sin-rx-control", "Neumonía: ¿Rx de control?",
  "PEDIATRÍA ENAM: NEUMONÍA ADQUIRIDA EN LA COMUNIDAD", "PEDIATRÍA",
  ("Neumonía en el niño", ["Si mejora clínicamente no necesita radiografía de control",
   "La imagen se resuelve más lento que la clínica"]),
  ("Niño de 11 meses tratado por neumonía", ["Opacidad amplia en 2/3 inferiores derechos", "Mejoría clínica marcada a los 7 días"]),
  {"rotulo": "Evolución y seguimiento", "ans": 2,
   "fases": [("Inicio", "Día 0", "Rx de diagnóstico", ["Antibiótico"]),
             ("Control", "48-72 h", "Reevaluar clínica", ["La fiebre debe ceder"]),
             ("Alta", "7-10 días", "SIN RX DE CONTROL", ["La mejoría clínica basta"]),
             ("Excepción", "4-6 sem", "Rx solo si…", ["Colapso, recurrencia"])],
   "curvas": [("Clínica", SKY, [0.2, 0.5, 0.8, 0.9, 0.95, 1.0, 1.0]),
              ("Rx", ROSE, [1.0, 1.0, 0.9, 0.8, 0.6, 0.4, 0.2])],
   "chips_titulo": "Conducta · marcada la correcta",
   "chips": [("No es necesaria", True), ("A los 10 días", False), ("Antes del alta", False), ("Por el neumólogo", False)]},
  ["Rx de control solo si hay neumonía redonda, atelectasia, derrame o síntomas persistentes.",
   "Neumonías recurrentes en el mismo lóbulo: buscar causa anatómica.",
   "La Rx puede tardar 4-6 semanas en normalizarse."],
  "BTS – Guidelines for community acquired pneumonia in children (2011) · PIDS/IDSA – Pediatric CAP guideline (2011)")

# TRA-020 · puntaje
V("puntaje", "TRA-020", "volcadura-dolor-cervical-deficit-manos-collarin", "Trauma cervical: criterios NEXUS",
  "TRAUMATOLOGÍA ENAM: TRAUMA DE COLUMNA CERVICAL", "TRAUMATOLOGÍA",
  ("Trauma de columna cervical", ["Dolor en la línea media o déficit neurológico: no se puede descartar lesión",
   "Primero inmovilizar con collarín rígido, luego imagen"]),
  ("Automovilista tras una volcadura", ["Orientado, dolor a la palpación cervical", "Menor fuerza y sensibilidad en manos"]),
  {"rotulo": "Criterios NEXUS en el caso", "escala": "NEXUS", "total": 2, "max": 5,
   "total_label": "Criterios positivos",
   "interpreta": "No se puede descartar lesión cervical",
   "items": [("Dolor en la línea media cervical", "1", True), ("Déficit neurológico focal", "1", True),
             ("Alteración de la conciencia", "1", False), ("Intoxicación", "1", False),
             ("Lesión distractora", "1", False)],
   "bandas": [("0", "Bajo riesgo", "Sin imagen ni collarín", False),
              ("≥ 1", "No se descarta", "Collarín rígido + TEM cervical", True)]},
  ["Déficit de manos: sospechar síndrome medular central.",
   "No hacer tracción ni cirugía sin estudio de imagen.",
   "Inmovilización con collarín y tabla durante el traslado."],
  ATLS + " · NEXUS – Hoffman et al. (N Engl J Med 2000)")

# PED-112 · radial
V("radial", "PED-112", "rubeola-materna-pulsos-saltones-ductus", "Rubéola congénita",
  "PEDIATRÍA ENAM: RUBÉOLA CONGÉNITA", "PEDIATRÍA",
  ("Síndrome de rubéola congénita", ["Tríada: cardiopatía (ductus), catarata y sordera",
   "Ductus: pulsos saltones y soplo continuo; puede dar insuficiencia cardiaca"]),
  ("Lactante de 2 meses con insuficiencia cardiaca", ["Prematura · madre con rubéola", "Pulsos saltones y soplo cardiaco"]),
  {"rotulo": "Mapa del tema", "centro": "RUBÉOLA", "centro_sub": "Congénita", "ans": 0,
   "items": [("CORAZÓN", ["Ductus arterioso persistente", "Estenosis pulmonar periférica"]),
             ("Ojos", ["Catarata"]),
             ("Oído", ["Sordera neurosensorial"]),
             ("SNC", ["Microcefalia"]),
             ("Piel", ["«Muffin de arándanos»"])],
   "ruta": ["Madre con rubéola", "Lactante prematura", "Pulsos saltones + soplo", "DUCTUS ARTERIOSO"]},
  ["El riesgo es máximo si la infección ocurre en el primer trimestre.",
   "La prematuridad también favorece el ductus.",
   "Prevención: vacuna SPR y verificar inmunidad antes del embarazo."],
  NELSON + " · CDC – Congenital rubella syndrome (2024)")
