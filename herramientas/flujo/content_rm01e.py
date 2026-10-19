# -*- coding: utf-8 -*-
"""Residentado Médico · lote 1 · flujogramas 83-100 (anticoagulación, shock, emergencias y abdomen agudo)."""
from c_rm import S, P, PX, B, Q, L, TR, ATLS, HARRISON, WILLIAMS, NELSON, MINSA, ACOG, AAP
from c26 import D, ILU
import ilu7 as I
GUYTON = "Guyton y Hall Tratado de Fisiología Médica 14.ª ed."
BRAUN = "Braunwald Tratado de Cardiología 12.ª ed."
SAB = "Sabiston Tratado de Cirugía 21.ª ed."
ESC_ACS = "ESC, síndromes coronarios agudos (2023)"
ECGP = "Trazado de enseñanza MedQuizPro (no es de un paciente)"

# 83 · RM-HEM-001 · REGLA: INR
S("regla", "RM-HEM-001", "La warfarina se controla con el tiempo de protrombina expresado como INR",
  "Hematología · anticoagulación oral",
  ("Control de la warfarina", ["Inhibe la vitamina K epóxido reductasa: bajan los factores II, VII, IX y X.", "Se vigila con el tiempo de protrombina (INR)."]),
  ("Paciente de 65 años", ["Fibrilación auricular con warfarina hace 2 meses.", "Consulta por equimosis."]),
  ["Rango terapéutico: INR 2-3 (FA, TVP) y 2,5-3,5 en prótesis mitral mecánica. TTPa es para la heparina no fraccionada.",
   "INR > 4,5-10 sin sangrado: suspender y dar vitamina K oral; con sangrado mayor: vitamina K IV + concentrado de complejo protrombínico.",
   "Interacciones: antibióticos, amiodarona, alcohol y dieta rica en vitamina K."],
  "ACCP/CHEST, tratamiento antitrombótico (2021); " + "ESC/EACTS, fibrilación auricular (2024); " + HARRISON,
  op=("¿Control?", ["No: no sirve para monitorizar", "No: usado en heparina, no en warfarina", "No: control de la heparina", "No: control de la heparina", "Sí: refleja la vía extrínseca"],
      {0: "Fibrinógeno", 1: "Tiempo de reptilase", 2: "TTPa", 3: "Tiempo de trombina", 4: "Tiempo de protrombina (INR)"}),
  d=dict(rotulo="Qué hacer según el INR",
         reglas=[dict(nombre="INR del paciente", que="Meta 2-3. Más alto = más riesgo de sangrado; más bajo = riesgo de trombosis.",
                      min=0, max=10, fmt="{}", ticks=[2, 3, 4.5, 10],
                      bandas=[(0, 2, "Bajo: más dosis", 1), (2, 3, "Terapéutico", 0), (3, 4.5, "Alto: reducir dosis", 2), (4.5, 10, "Muy alto: vitamina K", 3)], caso=5, caso_txt="Equimosis: medir el INR")],
         claves_titulo="Qué medir con cada anticoagulante",
         claves=[("Warfarina", ["Tiempo de protrombina (INR)"], True), ("Heparina no fraccionada", ["TTPa"], False), ("HBPM", ["Anti-Xa si hace falta"], False)]))

# 84 · RM-CAR-032 · CUADRÍCULA: shock obstructivo
S("cuadricula", "RM-CAR-032", "El taponamiento pericárdico produce shock obstructivo",
  "Shock · clasificación",
  ("Shock obstructivo", ["Un obstáculo mecánico impide el llenado o la salida del corazón.", "La contractilidad del miocardio está conservada."]),
  ("Pregunta de teoría", ["¿Qué tipo de shock origina el taponamiento?"]),
  ["Obstructivos: taponamiento, neumotórax a tensión, embolia pulmonar masiva e hipertensión pulmonar grave.",
   "Taponamiento: tríada de Beck, pulso paradójico y colapso de cavidades derechas; drenar (pericardiocentesis o ventana pericárdica).",
   "Mientras tanto: volumen IV y evitar ventilación con presión positiva alta."],
  "ESC, enfermedades del pericardio (2015); " + ATLS + "; " + HARRISON,
  op=("¿Tipo?", ["No: es una lesión medular", "No: no hay pérdida de volumen", "No: no hay vasodilatación", "Sí: la compresión impide el llenado", "No: la bomba está intacta"],
      {0: "Neurogénico", 1: "Hipovolémico", 2: "Distributivo", 3: "Obstructivo", 4: "Cardiogénico"}),
  d=dict(rotulo="Los cuatro tipos de shock", alto_img=0,
         celdas=[("Hipovolémico", ["Pérdida de volumen", "Hemorragia, deshidratación"], None, False), ("Cardiogénico", ["Falla de la bomba", "Infarto, arritmia"], None, False),
                 ("Obstructivo", ["Obstáculo mecánico", "Taponamiento, TEP, neumotórax a tensión"], None, True), ("Distributivo", ["Vasodilatación", "Sepsis, anafilaxia, neurogénico"], None, False)],
         veredicto=("Taponamiento = shock obstructivo", "Se resuelve drenando el pericardio.")))

# 85 · RM-CAR-033 · LABORATORIO: tiazidas
S("laboratorio", "RM-CAR-033", "La hidroclorotiazida puede empeorar el perfil lipídico: se evita en dislipidemia grave",
  "Farmacología · efectos metabólicos de las tiazidas",
  ("Tiazidas", ["En dosis altas elevan colesterol, LDL, triglicéridos, glucosa y ácido úrico.", "Siguen siendo de primera línea en dosis bajas."]),
  ("Pregunta de teoría", ["¿Qué fármaco se evita con dislipidemia e hipertensión?"]),
  ["Evitar o usar dosis bajas (12,5-25 mg) en dislipidemia grave, gota o diabetes mal controlada. Clortalidona e indapamida son más potentes.",
   "IECA, ARA II y calcioantagonistas son metabólicamente neutros; la alfametildopa, neutra y de elección en el embarazo.",
   "«Contraindicado» debe leerse como «el menos recomendable»."],
  "ACC/AHA, hipertensión arterial (2025); ESC, hipertensión arterial (2024); Katzung Farmacología Básica y Clínica 15.ª ed.",
  op=("¿El menos recomendable?", ["No: neutro", "No: neutra", "No: neutro", "No: neutro", "Sí: eleva lípidos y glucosa"],
      {0: "Enalapril", 1: "Alfametildopa", 2: "Amlodipino", 3: "Valsartán", 4: "Hidroclorotiazida"}),
  d=dict(rotulo="Efectos de la hidroclorotiazida", valores=[
            ("Potasio", "Bajo", "3,5-5", "↓", "Pérdida urinaria: vigilar."), ("Sodio", "Bajo", "135-145", "↓", "Hiponatremia por tiazidas."),
            ("Colesterol y triglicéridos", "Altos", "Según meta", "↑", "Empeora la dislipidemia."), ("Glucosa", "Alta", "< 100", "↑", "Intolerancia a la glucosa."),
            ("Ácido úrico y calcio", "Altos", "Normal", "↑", "Gota; hipercalcemia.")],
         veredicto=("Hidroclorotiazida: la menos recomendable con dislipidemia", "Preferir IECA, ARA II o calcioantagonista.")))

# 86 · RM-CIR-021 · ÁRBOL: peri-paro
S("arbol", "RM-CIR-021", "Dolor torácico con pérdida de conciencia y pulso presente: primero la vía aérea y la respiración",
  "Urgencias · paciente grave sin paro",
  ("Peri-paro", ["Inconsciente, cianótico y jadeante, pero con pulso: aún no es un paro.", "La prioridad es el ABC."]),
  ("Varón de 65 años", ["Precordialgia brusca, diaforesis y pérdida de conocimiento hace 10 minutos.", "Inconsciente, cianótico y jadeante."]),
  ["Asegurar la vía aérea, dar O₂ y ventilar; monitor, acceso venoso y desfibrilador listo.",
   "Sin pulso: RCP de alta calidad (C-A-B): compresiones de 5-6 cm a 100-120 por minuto y desfibrilar si hay ritmo desfibrilable.",
   "Golpe precordial: ya no se recomienda de rutina."],
  "AHA, Soporte Vital Cardiovascular Avanzado (actualización 2025); ERC, reanimación (2021)",
  op=("¿Primera medida?", ["No: no se recomienda de rutina", "No: se reservan para el paro o el shock", "No: solo con FV/TV sin pulso", "No: no cambia la conducta inmediata", "Sí: ABC antes de todo"],
      {0: "Golpes precordiales", 1: "Vasopresores", 2: "Desfibrilación inmediata", 3: "CPK y troponina", 4: "Cuidar la función respiratoria"}),
  arbol=Q("Paciente inconsciente: ¿tiene pulso?", [
      L("Sí (este caso)", "ABC", ["Vía aérea y O₂", "Ventilar, monitor y acceso IV"], path=True),
      L("No", "RCP C-A-B", ["Compresiones 100-120/min", "Desfibrilar si FV o TV sin pulso"])], path=True))

# 87 · RM-NEF-002 · EMBUDO: antihipertensivo en ERC
S("embudo", "RM-NEF-002", "Hipertenso con enfermedad renal y hematuria: IECA como antihipertensivo",
  "Nefrología · hipertensión y enfermedad renal crónica",
  ("HTA con ERC", ["Se busca reducir la presión intraglomerular y la proteinuria.", "IECA o ARA II son de primera línea; control de creatinina y potasio."]),
  ("Varón de 68 años", ["Creatinina 3 mg/dL, anemia, edema palpebral y hematuria.", "PA 170/100 mmHg."]),
  ["Controlar creatinina y potasio a la semana; aceptar aumentos de creatinina de hasta el 30 %.",
   "Suspender si hay hiperpotasemia > 5,5 mEq/L o sospecha de estenosis bilateral de las arterias renales.",
   "Meta < 130/80 mmHg; añadir iSGLT2 y finerenona según el caso (KDIGO 2024)."],
  "KDIGO, hipertensión arterial en ERC (2021) y ERC (2024); ACC/AHA, hipertensión (2025)",
  op=("¿Fármaco?", ["Sí: reduce la presión intraglomerular", "No: se acumula con filtrado bajo", "No: segunda línea", "No: mejor como segundo fármaco", "No: pierde eficacia con filtrado < 30 mL/min"],
      {0: "Enalapril", 1: "Atenolol", 2: "Reserpina", 3: "Nifedipino", 4: "Hidroclorotiazida"}),
  d=dict(rotulo="Descarta lo que no sirve en la enfermedad renal", inicio="Antihipertensivo con creatinina de 3 mg/dL",
         candidatos=["Atenolol", "Reserpina", "Hidroclorotiazida", "Nifedipino", "Enalapril"],
         pasos=[("¿Se elimina por vía renal o pierde eficacia con filtrado bajo?", ["Atenolol", "Hidroclorotiazida"]), ("¿Es de primera línea para proteger el riñón?", ["Reserpina", "Nifedipino"])],
         final=("IECA (ENALAPRIL)", ["Baja la presión intraglomerular", "Controlar creatinina y potasio"]),
         nota="Los diuréticos de asa reemplazan a las tiazidas si el filtrado es < 30 mL/min."))

# 88 · RM-CIR-022 · MONITOR: taponamiento por herida
S("monitor", "RM-CIR-022", "Herida precordial con yugulares llenas, ruidos apagados y PVC de 15 cm de agua: taponamiento cardiaco",
  "Trauma cardiaco · taponamiento",
  ("Taponamiento por herida penetrante", ["Zona de peligro precordial: entre las líneas medioclaviculares, del borde costal a la fúrcula.", "Bastan 100-200 mL de sangre para comprimir el corazón."]),
  ("Varón de 23 años", ["Herida por arma blanca precordial.", "PA 100/60, FC 110, yugulares llenas y PVC de 15 cm de agua."]),
  ["Tríada de Beck: hipotensión, ingurgitación yugular y ruidos apagados. FAST con ventana pericárdica confirma el hemopericardio.",
   "Inestable: toracotomía o esternotomía de urgencia; pericardiocentesis solo como puente. Volumen IV mientras tanto.",
   "En el neumotórax a tensión la tráquea se desvía y el hemitórax es hiperresonante."],
  ATLS + "; Schwartz Principios de Cirugía 11.ª ed.",
  op=("¿Diagnóstico?", ["Sí: tríada de Beck", "No: tráquea desviada, hiperresonancia", "No: sin los hallazgos del ECG", "No: poco frecuente", "No: sin factores de riesgo"],
      {0: "Taponamiento cardiaco", 1: "Neumotórax a tensión", 2: "Infarto agudo de miocardio", 3: "Ruptura ventricular", 4: "Embolia pulmonar"}),
  d=dict(rotulo="Los signos vitales del caso", titulo_monitor="MONITOR · TRAUMA", ecg="taquicardia · voltajes bajos",
         valores=[("PA", "100/60", "mmHg", "bajo"), ("FC", "110", "lpm", "alto"), ("SatO₂", "95", "%", "ok"), ("PVC", "15", "cmH₂O", "alto"), ("YUGULARES", "ingurgitadas", "", "alto"), ("RUIDOS", "apagados", "", "bajo")],
         lectura=[("Hipotensión + yugulares + ruidos apagados", "Tríada de Beck.", True), ("PVC 15 cmH₂O", "Presión venosa alta: el corazón no se llena.", True),
                  ("Ecografía FAST", "Hemopericardio en segundos.", False), ("Conducta", "Toracotomía o esternotomía; volumen mientras tanto.", True)],
         veredicto=("Herida precordial + Beck = taponamiento", "Drenar y reparar el corazón.")))

# 89 · RM-CB-023 · GRÁFICA: asa presión-volumen
S("grafica", "RM-CB-023", "La precarga es el volumen al final de la diástole",
  "Fisiología cardiaca · precarga y poscarga",
  ("Precarga", ["Estiramiento de la fibra antes de contraerse.", "Se mide como volumen o presión telediastólica."]),
  ("Pregunta de teoría", ["¿Qué parámetro determina la precarga?"]),
  ["Poscarga: resistencia que debe vencer el ventrículo (presión aórtica o tensión de pared en sístole).",
   "Frank-Starling: más volumen telediastólico, más fuerza de contracción, hasta un límite.",
   "Baja la precarga: diuréticos y nitratos. La sube: volumen. Se estima con el enclavamiento capilar pulmonar."],
  GUYTON + "; " + BRAUN,
  op=("¿Precarga?", ["No: determina la poscarga", "No: no es el parámetro de precarga", "No: refleja la presión de llenado inicial", "No: determina el volumen sistólico", "Sí: telediastólico"],
      {0: "Presión al final de la sístole", 1: "Volumen al inicio de la diástole", 2: "Presión al inicio de la diástole", 3: "Volumen al final de la sístole", 4: "Volumen al final de la diástole"}),
  d=dict(rotulo="Asa presión-volumen del ventrículo izquierdo", eje_x="Volumen (mL)", eje_y="Presión (mmHg)",
         x=(0, 150, [(0, "0"), (50, "50"), (100, "100"), (150, "150")]), y=(0, 140, [(0, "0"), (40, "40"), (80, "80"), (120, "120")]),
         series=[("Asa del ventrículo", [(50, 8), (120, 10), (125, 80), (125, 120), (50, 100), (50, 8)], "#0f766e")],
         zonas=[], caso=(120, 10, "Fin de la diástole = precarga"),
         notas=[("Volumen telediastólico (≈ 120 mL)", "Precarga: llenado máximo.", True), ("Presión aórtica (≈ 120 mmHg)", "Poscarga.", False), ("Volumen telesistólico (≈ 50 mL)", "Lo que queda tras la eyección.", False)],
         veredicto=("Precarga = volumen al final de la diástole", "Se estima con la presión de enclavamiento capilar pulmonar.")))

# 90 · RM-CAR-034 · RELOJ: emergencia hipertensiva
S("reloj", "RM-CAR-034", "Emergencia hipertensiva: bajar la presión diastólica hasta 100-105 mmHg",
  "Hipertensión · emergencia hipertensiva",
  ("Emergencia hipertensiva", ["PA muy elevada (> 180/120) con daño agudo de órgano blanco.", "Se trata en cuidados intensivos con fármacos IV."]),
  ("Varón de 56 años", ["Cefalea, náuseas y alteraciones visuales.", "PA 200/140, retinopatía grado III; se inicia labetalol IV."]),
  ["Reducir la PA media 20-25 % en la primera hora, luego a 160/100-110 en 2-6 h y a lo normal en 24-48 h.",
   "Con diastólica de 140, una reducción del 25 % llega a 100-105 mmHg.",
   "Excepciones: disección aórtica (PAS < 120 en 20 minutos) y ACV isquémico (solo si > 220/120 o antes de trombólisis)."],
  "ACC/AHA, hipertensión arterial (2025); ESC, hipertensión arterial (2024); " + HARRISON,
  op=("¿Meta de PAD?", ["No: reducción excesiva", "Sí: ≈ 25 % de 140", "No: reducción excesiva", "No: reducción excesiva", "No: reducción excesiva"],
      {0: "115 a 120", 1: "100 a 105", 2: "110 a 115", 3: "80 a 90", 4: "90 a 95"}),
  d=dict(rotulo="Cuánto y cuándo bajar la presión", intro="Un descenso brusco produce isquemia cerebral, coronaria y renal.",
         pasos=[("1.ª hora", "Bajar la PAM 20-25 %", "Diastólica de 140 → 100-105", True), ("2-6 h", "160/100-110", "Objetivo intermedio", False), ("24-48 h", "Valores normales", "Pasar a vía oral", False), ("sin", "Disección aórtica", "PAS < 120 en 20 min", False)],
         tag="ESTE CASO: PRIMERA HORA", veredicto=("Diastólica a 100-105 mmHg en la primera hora", "Descenso gradual para no causar isquemia.")))

# 91 · RM-CAR-035 · CHECKLIST: cuidados posparo
S("checklist", "RM-CAR-035", "En el síndrome posparo, la encefalopatía anóxica define el pronóstico",
  "Reanimación · síndrome posparo cardiaco",
  ("Síndrome posparo", ["Lesión cerebral hipóxico-isquémica, disfunción miocárdica y reacción sistémica a la isquemia-reperfusión.", "El cerebro es el órgano más vulnerable."]),
  ("Pregunta de teoría", ["¿Cuál es el factor pronóstico más importante?"]),
  ["Control de temperatura (32-37,5 °C) y evitar la fiebre por 72 h; SatO₂ 94-98 %, PaCO₂ normal y PAM ≥ 65 mmHg.",
   "Coronariografía precoz si hay elevación del ST.",
   "No pronosticar antes de 72 h del retorno de la circulación; usar un enfoque multimodal (examen, EEG, potenciales evocados, neuroimagen y biomarcadores)."],
  "AHA, cuidados posparo cardiaco (actualización 2025); ERC-ESICM (2021)",
  op=("¿Pronóstico?", ["No: se corrige", "No: se trata", "Sí: la lesión cerebral define la evolución", "No: se trata con angioplastia", "No: consecuencia del shock"],
      {0: "Hipotermia periférica", 1: "Bradiarritmia", 2: "Encefalopatía anóxica", 3: "Isquemia coronaria", 4: "Hipoperfusión periférica"}),
  d=dict(rotulo="Cuidados después de recuperar la circulación", tag="PRONÓSTICO: CEREBRO",
         pasos=[("Oxígeno 94-98 % y PaCO₂ normal", "Evitar hiperoxia", False), ("PAM ≥ 65 mmHg", "Perfusión cerebral", False), ("Control de la temperatura", "32-37,5 °C; evitar fiebre 72 h", True), ("Coronariografía si ST elevado", "Reperfusión precoz", False)],
         no_hacer=[("Pronosticar antes de 72 h", "Falsos pronósticos sombríos"), ("Hiperventilar", "Reduce la perfusión cerebral")],
         veredicto=("La encefalopatía anóxica es el factor pronóstico principal", "Evaluar a las 72 h con varias pruebas.")))

# 92 · RM-CAR-036 · FASES: troponina
S("fases", "RM-CAR-036", "La troponina comienza a elevarse a las 4 horas del inicio del infarto",
  "Cardiopatía isquémica · cinética de la troponina",
  ("Cinética de la troponina", ["Se libera tras la necrosis: sube a las 3-4 h.", "Con ensayos de alta sensibilidad se detecta desde la primera hora."]),
  ("Pregunta de teoría", ["¿Cuándo empieza a subir la troponina?"]),
  ["Pico a las 12-48 h; elevada 7-14 días (troponina I) o más (T).",
   "ESC 0/1 h y 0/2 h: segunda muestra para confirmar o descartar.",
   "Diagnóstico: valor sobre el percentil 99 con subida o bajada, más isquemia."],
  ESC_ACS + "; Cuarta Definición Universal del Infarto (2018)",
  op=("¿Horas?", ["No: demasiado temprano", "Sí: 3-4 horas de inicio clásico", "No: demasiado tarde", "No: ligeramente temprano", "No: solo con hs-troponina"],
      {0: "2", 1: "4", 2: "6", 3: "3", 4: "1"}),
  d=dict(rotulo="Cómo evoluciona la troponina", ans=0,
         fases=[("Inicio", "3-4 horas", "SUBE", ["Con hs-troponina, desde la 1.ª hora", "Algoritmo 0/1 h o 0/2 h"]),
                ("Pico", "12-48 horas", "MÁXIMO", ["Mayor concentración", "Útil para estimar el tamaño del infarto"]),
                ("Normalización", "7-14 días", "BAJA", ["Troponina I: 7-10 días", "Troponina T: hasta 14 días"])]))

# 93 · RM-CAR-037 · DOSIS: adenosina
S("dosis", "RM-CAR-037", "Taquicardia supraventricular con QRS estrecho que no cede con maniobras vagales: adenosina",
  "Arritmias · taquicardia por reentrada",
  ("TSV por reentrada intranodal", ["QRS estrecho, regular y onda P retrógrada tras el QRS.", "La más frecuente en mujeres jóvenes."]),
  ("Mujer de 30 años", ["Palpitaciones, dolor precordial y ansiedad.", "FC 210, QRS estrecho regular, sin mejoría tras las maniobras vagales."]),
  ["Adenosina: bolo rápido de 6 mg y, si no cede, 12 mg, seguidos de lavado salino; revierte > 90 %.",
   "Si falla: verapamilo, diltiazem o betabloqueante. Inestable: cardioversión sincronizada.",
   "Contraindicada en asma grave y en fibrilación auricular preexcitada. Ablación con catéter: curativa en > 95 %."],
  "AHA/ACC/HRS, taquicardia supraventricular (2015); ESC, taquicardia supraventricular (2019); AHA, SVCA (actualización 2025)",
  op=("¿Fármaco?", ["No: es un betabloqueante de segunda línea", "No: digital, no de elección", "Sí: bloquea el nodo AV un instante", "No: último recurso", "No: calcioantagonista de segunda línea"],
      {0: "Metoprolol", 1: "Lanatósido", 2: "Adenosina", 3: "Amiodarona", 4: "Verapamilo"}),
  d=dict(rotulo="Cómo se administra la adenosina", peso=("Dosis fija", "No depende del peso"),
         pasos=[("1.ª dosis", "6 mg", "Bolo rápido IV"), ("Lavado", "20 mL", "Solución salina inmediata"), ("2.ª dosis", "12 mg", "Si no cede en 1-2 min")],
         alternativas=[("Adenosina 6 mg y luego 12 mg", "Elección", True), ("Metoprolol IV", "Segunda línea", False), ("Amiodarona", "Último recurso", False), ("Digoxina", "Inicio lento", False)],
         veredicto=("Adenosina en bolo rápido", "Efectos breves: rubor, opresión torácica y pausa.")))

# 94 · RM-NEF-003 · TERMÓMETRO: albuminuria y conducta
S("cuadro", "RM-NEF-003", "Diabético con HTA y proteinuria persistente: enalapril",
  "Nefrología · nefropatía diabética",
  ("Nefropatía diabética incipiente", ["Albuminuria persistente en un diabético hipertenso.", "IECA o ARA II retrasan la progresión."]),
  ("Varón de 45 años", ["HTA reciente y DM2 hace 5 años.", "PA 160/100, depuración 100 mL/min y proteinuria de 500 mg/24 h."]),
  ["IECA o ARA II de primera línea con albuminuria; meta PA < 130/80 mmHg.",
   "Añadir iSGLT2 (empagliflozina, dapagliflozina) y, si persiste la albuminuria, finerenona; metformina si el filtrado > 30 mL/min.",
   "Control de creatinina y potasio a los 7-14 días."],
  "ADA, estándares de atención en diabetes (2026); KDIGO, diabetes y ERC (2022) y ERC (2024); ACC/AHA, hipertensión (2025)",
  op=("¿Elección?", ["No: no protege el riñón", "No: no reduce la presión intraglomerular", "No: pierde eficacia y empeora la glucosa", "Sí: reduce la presión intraglomerular", "No: sintomático, sin efecto renal"],
      {0: "Metildopa", 1: "Amlodipino", 2: "Hidroclorotiazida", 3: "Enalapril", 4: "Furosemida"}),
  d=dict(claves_titulo="Qué añadir al IECA o ARA II en la nefropatía diabética",
         claves=[("1. IECA o ARA II", ["Enalapril: baja la presión intraglomerular"], True), ("2. iSGLT2", ["Empagliflozina o dapagliflozina"], False), ("3. Finerenona", ["Si persiste la albuminuria"], False)],
         veredicto=("Diabético, hipertenso y con albuminuria: enalapril", "Control de creatinina y potasio a los 7-14 días.")),
  clasif=dict(titulo="Categorías de albuminuria (KDIGO) y conducta", cols=["Categoría", "Albuminuria 24 h", "Cociente albúmina/creatinina", "Término", "Conducta"],
              filas=[["A1", "< 30 mg", "< 30 mg/g", "Normal o levemente aumentada", "Control anual y PA < 130/80"],
                     ["A2", "30-300 mg", "30-300 mg/g", "Moderadamente aumentada", "IECA o ARA II si hay HTA; añadir iSGLT2"],
                     ["A3", "> 300 mg", "> 300 mg/g", "Gravemente aumentada", "IECA o ARA II + iSGLT2; finerenona si persiste; nefrología"]],
              caso=[1, 2], ancho_primera=130,
              nota="Proteinuria de 500 mg/24 h: límite entre A2 y A3 (en proteinuria total, A2 es 150-500 y A3 > 500 mg/g)."))

# 95 · RM-CIR-023 · LECTURA con ecografía real: apendicitis
S("lectura", "RM-CIR-023", "Dolor migratorio a fosa ilíaca derecha, Blumberg positivo y signo de Horn: apendicitis aguda",
  "Cirugía · apendicitis aguda",
  ("Apendicitis aguda", ["Dolor periumbilical que migra a la fosa ilíaca derecha, anorexia, náuseas y fiebre baja.", "La ausencia de leucocitosis no la descarta."]),
  ("Varón de 20 años", ["Dolor súbito que se localiza en fosa ilíaca derecha.", "Blumberg (+), dolor al traccionar el testículo derecho; sin leucocitosis."]),
  ["Signo de Horn: dolor al traccionar suavemente el cordón o testículo derecho. Rovsing, psoas y obturador completan los signos.",
   "Los testículos son normales: en la torsión el dolor es escrotal e intenso, con testículo elevado.",
   "Alvarado ≥ 7 apoya; eco en niños y TC en adultos. Tratamiento: apendicectomía laparoscópica (antibióticos en casos no complicados, ensayo CODA 2020)."],
  "WSES, apendicitis aguda (2020); " + SAB + "; Kaplan et al., POCUS J 2025.",
  op=("¿Diagnóstico?", ["Sí: Blumberg y Horn en fosa ilíaca derecha", "No: cólico lumbar con hematuria", "No: sin síntomas urinarios", "No: dolor y testículo elevados", "No: testículo normal"],
      {0: "Apendicitis aguda", 1: "Litiasis renal", 2: "Infección urinaria", 3: "Torsión testicular", 4: "Orquiepididimitis"}),
  d=dict(rotulo="Signos clínicos y confirmación por ecografía", img_titulo="Ecografía de un apéndice inflamado",
         img=PX("apendicitis_pocus.jpg", 400, credito="Kaplan et al. · POCUS J 2025 · PMC12057466 · CC BY 4.0"),
         pasos=[("Blumberg y Rovsing", "Dolor al descomprimir; dolor en fosa ilíaca derecha al palpar la izquierda.", False),
                ("Signo de Horn", "Dolor al traccionar el testículo derecho: apoya apendicitis.", True),
                ("Psoas y obturador", "Dolor al extender la cadera o rotarla.", False),
                ("Ecografía: apéndice dilatado", "Los calibres (+) miden 6,8 y 8,1 mm; normal: menos de 6 mm.", False)],
         img_pie="Imagen referencial de una apendicitis aguda en la ecografía (corte corto a la izquierda y largo a la derecha; los calibres son de la propia imagen).",
         veredicto=("Apendicitis aguda: la leucocitosis no es indispensable", "Testículos normales: se descarta torsión y orquiepididimitis.")))

# 96 · RM-CIR-024 · PUNTAJE: Alvarado
S("puntaje", "RM-CIR-024", "La anorexia es el síntoma casi constante de la apendicitis: su ausencia pone en duda el diagnóstico",
  "Cirugía · apendicitis, puntaje de Alvarado",
  ("Anorexia en la apendicitis", ["Presente en 90-95 %: si el paciente tiene apetito, dudar.", "Los vómitos vienen después del dolor."]),
  ("Pregunta de teoría", ["¿Qué síntoma, si falta, pone en duda el diagnóstico?"]),
  ["Alvarado (MANTRELS): migración 1, anorexia 1, náuseas 1, defensa 2, rebote 1, fiebre 1, leucocitosis 2, desviación a la izquierda 1.",
   "0-4 baja probabilidad; 5-6 intermedia (imagen); 7-10 alta (cirugía).",
   "Si el vómito precede al dolor, pensar en gastroenteritis."],
  "WSES, apendicitis aguda (2020); " + SAB,
  op=("¿Si falta?", ["Sí: casi constante", "No: inespecífico", "No: aparece después del dolor", "No: puede faltar", "No: puede estar o no"],
      {0: "Anorexia", 1: "Malestar general", 2: "Náuseas y vómitos", 3: "Fiebre", 4: "Constipación"}),
  d=dict(rotulo="Puntaje de Alvarado: dónde pesa la anorexia", escala="Escala de Alvarado (MANTRELS)", total=1, max=10, total_label="Puntos de la anorexia",
         interpreta="Un solo dato no decide: se suma con el resto",
         items=[("Dolor que migra a la fosa ilíaca derecha", 1, False), ("Anorexia (casi constante)", 1, True), ("Náuseas o vómitos", 1, False),
                ("Dolor en la fosa ilíaca derecha", 2, False), ("Rebote (Blumberg)", 1, False), ("Temperatura > 37,3 °C", 1, False),
                ("Leucocitos > 10 000", 2, False), ("Neutrófilos > 75 %", 1, False)],
         bandas=[("0-4", "Poco probable", "Observar o alta con control.", False), ("5-6", "Posible", "Ecografía (niños) o TC (adultos).", False),
                 ("7-10", "Probable", "Evaluación quirúrgica y apendicectomía.", False)]))

# 97 · RM-CIR-025 · LECTURA con TC: vólvulo de ciego
S("lectura", "RM-CIR-025", "La malrotación y la falta de fijación del ciego son el factor más asociado al vólvulo cecal",
  "Cirugía · obstrucción intestinal, vólvulo cecal",
  ("Vólvulo cecal", ["El ciego (y el colon ascendente) se tuerce sobre su mesenterio: asa cerrada con riesgo de isquemia.", "Predisponen la malrotación, la falta de fijación y el mesenterio largo."]),
  ("Pregunta de teoría", ["¿Qué factor se asocia más al vólvulo cecal?"]),
  ["Rx: ciego distendido desplazado al cuadrante superior izquierdo («grano de café»). La TC muestra el punto de transición.",
   "No se reduce con endoscopía (a diferencia del sigmoides): tratamiento quirúrgico: hemicolectomía derecha o cecopexia si el intestino es viable.",
   "Otros factores: cirugía previa, embarazo, estreñimiento crónico."],
  "Schwartz Principios de Cirugía 11.ª ed.; " + SAB,
  op=("¿Factor?", ["Sí: ciego móvil sin fijación", "No: factor menor", "No: no causa volvulo", "No: factor menor", "No: factor secundario"],
      {0: "Malrotación", 1: "Estreñimiento", 2: "Parasitosis crónica", 3: "Psicotrópicos", 4: "Mesenterio largo"}),
  d=dict(rotulo="Lee la tomografía en este orden", img_titulo="TC de abdomen con contraste (corte coronal)",
         img=PX("rm/volvulo_ciego_tc.jpg", 330),
         pasos=[("Ciego muy dilatado", "Asa cerrada con aire y heces.", True), ("Punto de transición (flechas amarillas)", "Donde el intestino se tuerce.", False),
                ("Ciego fuera de su sitio", "Desplazado hacia arriba y a la izquierda.", False), ("Conducta", "Cirugía urgente: hemicolectomía derecha.", False)],
         img_pie="Imagen referencial de un vólvulo de ciego en la TC (las flechas amarillas marcan el punto de transición).", veredicto=("Malrotación = ciego móvil que se tuerce", "Es quirúrgico: no se reduce con colonoscopía.")))

# 98 · RM-CIR-026 · ALARMA con Rx: bridas
S("alarma", "RM-CIR-026", "Las bridas y adherencias son la primera causa de obstrucción intestinal tras una cirugía abdominal",
  "Cirugía · obstrucción intestinal posoperatoria",
  ("Obstrucción adhesiva", ["Bridas y adherencias: 55-75 % de las obstrucciones del intestino delgado.", "Pueden aparecer semanas o décadas después de la cirugía."]),
  ("Pregunta de teoría", ["¿Cuál es la causa más frecuente en un paciente operado?"]),
  ["Dolor cólico, vómitos, distensión y ausencia de gases con niveles hidroaéreos.",
   "Tratamiento inicial: ayuno, sonda nasogástrica, hidratación, electrolitos y contraste hidrosoluble (diagnóstico y tratamiento).",
   "Operar si hay estrangulación, obstrucción completa o falta de mejoría en 48-72 horas."],
  "WSES, obstrucción adhesiva del intestino delgado (2018); " + SAB,
  op=("¿Más frecuente?", ["No: segunda causa", "Sí: la primera tras cirugía abdominal", "No: segunda causa", "No: infrecuente", "No: infrecuente en el adulto"],
      {0: "Hernia crural estrangulada", 1: "Bridas y adherencias", 2: "Hernia inguinal incarcerada", 3: "Vólvulo yeyunal", 4: "Intususcepción"}),
  d=dict(rotulo="Cuándo operar una obstrucción adhesiva", lista_titulo="Signos de estrangulación",
         signos=[("Fiebre y leucocitosis", "Isquemia del asa", None), ("Dolor continuo con peritonismo", "Peritonitis", None), ("Acidosis láctica", "Isquemia", None), ("Obstrucción completa", "Sin gas distal", True), ("Sin mejoría en 48-72 h", "Fracaso del manejo conservador", True)],
         accion=("Laparotomía o laparoscopia", "Liberar las bridas y resecar lo no viable."), accion_rotulo="Si hay uno o más",
         veredicto=("Bridas y adherencias: la causa más frecuente", "Manejo conservador inicial; operar si se estrangula.")),
  banda=B("Así se ve en la radiografía", PX("bridas_rx.jpg", 280), [("Asas dilatadas", "Intestino delgado distendido."), ("Niveles hidroaéreos", "En escalera."), ("Poco gas distal", "Obstrucción."), ("Causa", "Bridas por cirugía previa.")], pie="Imagen referencial de una obstrucción intestinal por bridas en la radiografía"))

# 99 · RM-CIR-027 · REGLA: Ogilvie
S("regla", "RM-CIR-027", "La seudoobstrucción aguda del colon (Ogilvie) se asocia al uso de opioides",
  "Cirugía · seudoobstrucción del colon",
  ("Síndrome de Ogilvie", ["Dilatación masiva del colon sin obstrucción mecánica.", "En pacientes graves, tras cirugía o trauma."]),
  ("Pregunta de teoría", ["¿Con qué fármacos se relaciona?"]),
  ["Opioides, anticolinérgicos, tricíclicos, antipsicóticos y bloqueantes de calcio; también sepsis y alteraciones electrolíticas.",
   "Inicio: ayuno, sonda nasogástrica y rectal, corregir electrolitos y suspender los fármacos causantes.",
   "Neostigmina IV 2 mg con monitorización (contraindicada en obstrucción mecánica y asma grave) o descompresión colonoscópica."],
  SAB + "; Schwartz Principios de Cirugía 11.ª ed.",
  op=("¿Fármaco?", ["Sí: reducen la motilidad", "No: no relacionados", "No: no relacionados", "No: no relacionados", "No: no relacionados"],
      {0: "Narcóticos", 1: "Antipiréticos", 2: "Diuréticos", 3: "Hipoglicemiantes", 4: "Hipotensores"}),
  d=dict(rotulo="Cuándo actuar según el diámetro del ciego",
         reglas=[dict(nombre="Diámetro del ciego en la radiografía (cm)", que="< 10 cm: vigilar. 10-12 cm: neostigmina. > 12 cm o 6 días: riesgo de perforación.",
                      min=0, max=16, fmt="{}", ticks=[6, 10, 12, 16],
                      bandas=[(0, 10, "Vigilar", 0), (10, 12, "Neostigmina", 2), (12, 16, "Descomprimir", 3)], caso=11, caso_txt="Ejemplo: 11 cm")],
         claves_titulo="Manejo del síndrome de Ogilvie",
         claves=[("Soporte", ["Ayuno, sondas, electrolitos"], True), ("Neostigmina IV", ["2 mg con monitor y atropina"], False), ("Descompresión", ["Colonoscópica o quirúrgica"], False)]))

# 100 · RM-CIR-028 · GASOMETRÍA: obstrucción alta
S("gasometria", "RM-CIR-028", "Obstrucción intestinal proximal: hipopotasemia y alcalosis metabólica",
  "Cirugía · trastornos ácido-base en la obstrucción",
  ("Pérdida de jugo gástrico", ["Los vómitos eliminan ácido clorhídrico y potasio.", "Alcalosis metabólica hipoclorémica con hipopotasemia."]),
  ("Pregunta de teoría", ["¿Qué trastorno es más frecuente en la obstrucción proximal?"]),
  ["La hipovolemia activa la aldosterona: retiene sodio y elimina potasio y protones (aciduria paradójica).",
   "Obstrucción distal con isquemia: acidosis metabólica con lactato.",
   "Tratamiento: solución salina isotónica con potasio y sonda nasogástrica."],
  SAB + "; " + HARRISON,
  op=("¿Trastorno?", ["Sí: vómitos con pérdida de H⁺, Cl⁻ y K⁺", "No: la hiponatremia no es lo característico", "No: sería en obstrucción distal isquémica", "No: la respiración no se altera así", "No: no es el trastorno característico"],
      {0: "Hipopotasemia y alcalosis metabólica", 1: "Hiponatremia y alcalosis metabólica", 2: "Hipopotasemia y acidosis metabólica", 3: "Hipernatremia y alcalosis respiratoria", 4: "Hipocalcemia y acidosis metabólica"}),
  d=dict(rotulo="La gasometría del paciente que vomita (valores típicos)",
         valores=[("pH", "7,52", "7,35-7,45", "↑"), ("HCO₃⁻", "34", "22-26", "↑"), ("K⁺", "2,9", "3,5-5", "↓"), ("Cl⁻", "88", "98-106", "↓")],
         pasos=[("¿Acidemia o alcalemia?", "pH 7,52", "Alcalemia", False), ("¿Metabólica o respiratoria?", "HCO₃⁻ alto", "Alcalosis metabólica", False),
                ("¿Qué electrolitos?", "K⁺ y Cl⁻ bajos", "Hipopotasemia e hipocloremia", False), ("¿Qué hago primero?", "Hipovolemia", "SALINA ISOTÓNICA + POTASIO", True)],
         veredicto=("Alcalosis metabólica con hipopotasemia", "Se corrige con solución salina y potasio, y descomprimiendo con sonda.")))
