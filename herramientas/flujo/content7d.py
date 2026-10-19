"""Bloque 7 · parte D."""
from c7 import F7, Q, L, A, V, NELSON, ATLS, ROSE, VIOLET, SKY, AMBER

WILLIAMS = "Williams Obstetrics 26.ª ed. (2022)"
HARRISON = "Harrison. Principios de Medicina Interna 22.ª ed. (2025)"

# CAR-058 · termómetro
V("termometro", "CAR-058", "st-elevado-v2-v6-hipotension-shock-cardiogenico", "Infarto con hipotensión",
  "CARDIOLOGÍA ENAM: SHOCK CARDIOGÉNICO", "CARDIOLOGÍA",
  ("Shock cardiogénico", ["Infarto extenso: la bomba falla y cae el gasto",
   "Hipotensión + congestión pulmonar + hipoperfusión = Killip IV"]),
  ("Varón obeso de 50 años", ["Disnea, dolor torácico y desvanecimiento súbitos", "PA 70/40 · SatO₂ 85 % · crepitantes · ST elevado V2-V6"]),
  {"rotulo": "Clase de Killip",
   "niveles": [("I", "Sin falla", ["Sin crepitantes"]),
               ("II", "Falla leve", ["Crepitantes basales, S3"]),
               ("III", "Edema pulmonar", ["Crepitantes en todo el campo"]),
               ("IV", "Shock cardiogénico", ["PA 70/40 + CREPITANTES", "Mortalidad > 50 %"])],
   "caso_nivel": 3, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Reperfusión urgente: ICP", ["Angioplastia primaria de la arteria culpable"], True),
             (2, "Noradrenalina ± dobutamina", ["Mantener la perfusión"], False),
             (3, "Soporte mecánico", ["Si no responde a fármacos"], False)]},
  ["El ST elevado en V2-V6 indica infarto anterior extenso (descendente anterior).",
   "TEP masivo: Rx limpia, sin ST elevado en precordiales.",
   "Taponamiento y neumotórax dan yugulares ingurgitadas sin crepitantes."],
  "ESC – Guidelines for the management of acute coronary syndromes (2023)")

# INF-083 · tarjetas
V("tarjetas", "INF-083", "diabetica-escara-necrotica-destruccion-maxilar-mucormicosis", "Micosis invasiva facial",
  "INFECTOLOGÍA ENAM: MUCORMICOSIS RINOCEREBRAL", "INFECTOLOGÍA",
  ("Mucormicosis", ["Hongo que invade vasos y produce necrosis",
   "Diabético descompensado + escara negra en nariz o paladar + destrucción ósea"]),
  ("Mujer de 24 años con diabetes mal controlada", ["Dolor facial intenso, piel violácea con escara necrótica", "TC: destrucción ósea alrededor del seno maxilar"]),
  {"rotulo": "¿Qué hongo es?", "ans": 0, "cards": [
      {"titulo": "MUCORMICOSIS", "datos": [
          ("Paciente", "Diabetes, cetoacidosis", True), ("Lesión", "Escara necrótica", True),
          ("Hueso", "Destrucción rápida", True), ("Hifas", "Anchas, sin septos", False)],
       "pie": "Anfotericina B + desbridar"},
      {"titulo": "Aspergilosis", "datos": [
          ("Paciente", "Neutropénico", False), ("Lesión", "Pulmonar, sinusal", False),
          ("Hueso", "Invasión lenta", False), ("Hifas", "Delgadas, septadas", False)],
       "pie": "Voriconazol"},
      {"titulo": "Candidiasis", "datos": [
          ("Paciente", "Inmunodeprimido", False), ("Lesión", "Placas blancas", False),
          ("Hueso", "No", False), ("Hifas", "Levaduras, seudohifas", False)],
       "pie": "Fluconazol"},
      {"titulo": "Actinomicosis", "datos": [
          ("Paciente", "Mala higiene dental", False), ("Lesión", "Fístulas, gránulos", False),
          ("Hueso", "Lenta", False), ("Hifas", "Bacteria filamentosa", False)],
       "pie": "Penicilina prolongada"}]},
  ["Es una urgencia: la mortalidad es alta sin cirugía precoz.",
   "Corregir la cetoacidosis es parte del tratamiento.",
   "Puede extenderse a la órbita y al cerebro."],
  "ECMM/MSG ERC – Global guideline for the diagnosis and management of mucormycosis (Lancet Infect Dis 2019)")

# CAR-059 · puntaje
V("puntaje", "CAR-059", "ortopnea-edema-crepitantes-insuficiencia-cardiaca-furosemida", "Insuficiencia cardiaca congestiva",
  "CARDIOLOGÍA ENAM: INSUFICIENCIA CARDIACA DESCOMPENSADA", "CARDIOLOGÍA",
  ("Insuficiencia cardiaca", ["Criterios de Framingham: 2 mayores, o 1 mayor + 2 menores",
   "Con congestión (crepitantes, edema) el primer paso es el diurético de asa"]),
  ("Mujer de 65 años", ["Disnea a pequeños esfuerzos, ortopnea, palpitaciones", "FC 106 · edema 4+ · crepitantes en 2/3 inferiores"]),
  {"rotulo": "Criterios de Framingham en el caso", "escala": "Framingham", "total": 4, "max": 8,
   "total_label": "Criterios presentes",
   "interpreta": "Cumple: 2 mayores + 2 menores",
   "items": [("Ortopnea o disnea paroxística nocturna", "Mayor", True), ("Crepitantes", "Mayor", True),
             ("Ingurgitación yugular", "Mayor", False), ("Tercer ruido (galope)", "Mayor", False),
             ("Edema de miembros inferiores", "Menor", True), ("Disnea de esfuerzo", "Menor", True),
             ("Taquicardia > 120", "Menor", False), ("Hepatomegalia", "Menor", False)],
   "bandas": [("No", "No cumple", "Buscar otra causa de disnea", False),
              ("Sí", "IC congestiva", "Furosemida EV + ecocardiograma", True)]},
  ["La furosemida alivia la congestión pulmonar en minutos.",
   "Betabloqueador y espironolactona mejoran la sobrevida, pero se ajustan cuando esté compensada.",
   "La aspirina no trata la insuficiencia cardiaca."],
  "ESC – Guidelines for the diagnosis and treatment of acute and chronic heart failure (2021; actualización 2023)")

# PED-158 · puntaje
V("puntaje", "PED-158", "lactante-6-meses-se-sienta-balbucea-no-gatea-normal", "Hitos del desarrollo a los 6 meses",
  "PEDIATRÍA ENAM: DESARROLLO PSICOMOTOR", "PEDIATRÍA",
  ("Desarrollo a los 6 meses", ["Se sienta sin apoyo, balbucea, transfiere objetos y reconoce a los suyos",
   "El gateo aparece entre los 8 y 10 meses"]),
  ("Lactante de 6 meses", ["La madre se preocupa porque no gatea", "Balbucea, sonríe, se sienta solo, pasa un cubo de mano a mano"]),
  {"rotulo": "Hitos esperados a los 6 meses", "escala": "Hitos de 6 meses", "total": 4, "max": 4,
   "total_label": "Hitos cumplidos",
   "interpreta": "Desarrollo normal para su edad",
   "items": [("Se sienta sin apoyo", "✓", True), ("Balbucea", "✓", True),
             ("Transfiere objetos de una mano a otra", "✓", True), ("Sonríe y reconoce a familiares", "✓", True),
             ("Gatea (se espera a los 8-10 meses)", "—", False)],
   "bandas": [("4 de 4", "Normal", "Seguir controles de CRED", True),
              ("< 4", "Riesgo", "Evaluar con EEDP o TEPSI", False)]},
  ["No gatear a los 6 meses es normal; algunos niños nunca gatean.",
   "Señal de alarma a los 6 meses: no sostiene la cabeza o no sonríe.",
   "Retraso global: afecta dos o más áreas del desarrollo."],
  "MINSA – NTS 537: Control de crecimiento y desarrollo (2017) · CDC – Developmental milestones (2022)")

# GIN-163 · termómetro
V("termometro", "GIN-163", "macrosomico-desgarro-hasta-esfinter-anal-tercer-grado", "Desgarros perineales",
  "OBSTETRICIA ENAM: DESGARRO PERINEAL", "OBSTETRICIA",
  ("Clasificación de los desgarros", ["Se gradúa por la estructura más profunda lesionada",
   "Tercer grado: llega al esfínter anal sin romper la mucosa rectal"]),
  ("Parto de un feto de 4200 g", ["Sangrado de 1000 ml", "Desgarro con lesión muscular hasta el esfínter del ano"]),
  {"rotulo": "Grado del desgarro",
   "niveles": [("I", "Piel y mucosa", ["Solo superficie"]),
               ("II", "Músculos perineales", ["Sin esfínter"]),
               ("III", "Esfínter anal", ["LLEGA AL ESFÍNTER", "3a < 50 %, 3b > 50 %, 3c interno"]),
               ("IV", "Mucosa rectal", ["Esfínter + recto"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Reparar en sala de operaciones", ["Anestesia y buena luz", "Esfinterorrafia"], True),
             (2, "Antibiótico y laxante", ["Evitar infección y esfuerzo"], False),
             (3, "Control de continencia", ["Fisioterapia de piso pélvico"], False)]},
  ["Factores de riesgo: macrosomía, primípara, parto instrumentado.",
   "El sangrado de 1000 ml exige además buscar atonía y restos.",
   "Un desgarro no reconocido deja incontinencia fecal."],
  "RCOG – Green-top Guideline 29: Third- and fourth-degree perineal tears (2015) · " + WILLIAMS)

# PED-159 · fases
V("fases", "PED-159", "nino-diarrea-llenado-capilar-lento-hipotension-bolo-20", "Shock por deshidratación",
  "PEDIATRÍA ENAM: SHOCK HIPOVOLÉMICO POR DIARREA", "PEDIATRÍA",
  ("Deshidratación con shock", ["Pulsos débiles, llenado > 3 s, hipotensión y frialdad",
   "Se reanima con cristaloide isotónico en bolos de 20 ml/kg"]),
  ("Niño de 3 años con 2 días de diarrea y vómitos", ["FC 120 · FR 60 · llenado > 3 s · acrocianosis", "Pulsos débiles e hipotensión"]),
  {"rotulo": "Secuencia de reanimación", "ans": 0,
   "fases": [("Bolo", "0-15 min", "NACL 0,9 % 20 ML/KG", ["O Ringer lactato", "Vía EV o intraósea"]),
             ("Reevaluar", "Tras cada bolo", "Pulso, llenado, PA", ["Buscar sobrecarga"]),
             ("Repetir", "Hasta 60 ml/kg", "Si sigue en shock", ["Considerar vasopresor"]),
             ("Plan C", "Luego", "Completar rehidratación", ["Y reponer pérdidas"])],
   "curvas": [("Perfusión", SKY, [0.1, 0.25, 0.45, 0.6, 0.75, 0.85, 0.9])],
   "chips_titulo": "Primer líquido · marcado el correcto",
   "chips": [("NaCl 0,9 % 20 ml/kg", True), ("Dextrosa 5 %", False), ("Dextrosa 10 %", False), ("Plasma fresco", False)]},
  ["Las soluciones con dextrosa sola no expanden el volumen: hiponatremia.",
   "El plasma no está indicado en la deshidratación.",
   "Controlar la glucemia: el niño en shock puede tener hipoglucemia."],
  "OMS – Tratamiento de la diarrea: manual para médicos (2005) · Surviving Sepsis Campaign – Pediatric guidelines (2020)")

# PED-160 · árbol
A("PED-160", "neonato-tejido-carnoso-umbilical-nitrato-plata", "Ombligo que no cicatriza",
  "PEDIATRÍA ENAM: GRANULOMA UMBILICAL", "PEDIATRÍA",
  ("Lesiones del ombligo", ["Tejido carnoso, rosado y húmedo tras caer el cordón = granuloma",
   "Si drena orina o heces, es un remanente embrionario"]),
  ("Neonato tras la caída del cordón", ["Tejido carnoso que persiste y crece", "Secreción amarillenta"]),
  Q("¿Qué sale por el ombligo?", [
      L("Secreción serosa, tejido rosado", "GRANULOMA: NITRATO DE PLATA", ["Nitrato de plata al 10 %", "Repetir cada 3-4 días"], path=True),
      L("Orina", "Uraco persistente", ["Ecografía, cirugía"]),
      L("Heces o moco", "Conducto onfalomesentérico", ["Cirugía"]),
      L("Pus con eritema", "Onfalitis", ["Antibiótico EV"])], path=True),
  ("Granuloma umbilical", [("Clave", True), ("Detalle", False)], [
      ("Aspecto", ["Rosado, húmedo, blando", "No duele"]),
      ("Tratamiento", ["Nitrato de plata", "Sal de mesa como alternativa"]),
      ("Si no cede", ["Ligadura o escisión", "Pensar en pólipo umbilical"])]),
  ["El granuloma no tiene terminaciones nerviosas: la cauterización no duele.",
   "Proteger la piel alrededor para no quemarla.",
   "La onfalitis es una urgencia: eritema que se extiende."],
  NELSON)

# TRA-035 · fases
V("fases", "TRA-035", "politrauma-coma-sato2-84-oxigenoterapia", "Revisión primaria del trauma",
  "TRAUMATOLOGÍA ENAM: POLITRAUMATIZADO HIPOXÉMICO", "TRAUMATOLOGÍA",
  ("ABCDE del trauma", ["Se corrige cada problema en orden, antes de pasar al siguiente",
   "La hipoxemia empeora la lesión cerebral: oxígeno de inmediato"]),
  ("Politraumatizado en coma", ["PA 120/80 · FC 100 · FR 20", "SatO₂ 84 %"]),
  {"rotulo": "Orden de la atención", "ans": 1,
   "fases": [("A", "Vía aérea", "Permeable + cervical", ["Coma: asegurar vía aérea"]),
             ("B", "Ventilación", "OXIGENOTERAPIA", ["SatO₂ 84 %: O₂ ya", "Meta ≥ 94 %"]),
             ("C", "Circulación", "Control de sangrado", ["Estable en este caso"]),
             ("D", "Neurológico", "Glasgow, pupilas", ["Luego TC cerebral"]),
             ("E", "Exposición", "Evitar hipotermia", ["Revisar todo el cuerpo"])],
   "curvas": [],
   "chips_titulo": "Primera conducta · marcada la correcta",
   "chips": [("Oxigenoterapia", True), ("TC cerebral", False), ("Neurocirugía", False), ("Gases arteriales", False)]},
  ["La TC y la interconsulta vienen después de estabilizar A, B y C.",
   "Glasgow ≤ 8: intubar para proteger la vía aérea.",
   "No esperar los gases arteriales para dar oxígeno."],
  ATLS)

# PED-161 · árbol
A("PED-161", "neonato-3900-g-glucosa-40-dextrosa-8-ml", "Dosis de dextrosa en el neonato",
  "PEDIATRÍA ENAM: HIPOGLUCEMIA NEONATAL SINTOMÁTICA", "PEDIATRÍA",
  ("Hipoglucemia neonatal sintomática", ["Bolo de dextrosa al 10 %: 2 ml/kg EV (200 mg/kg)",
   "Luego infusión continua"]),
  ("Neonato postérmino de 36 h, 3900 g", ["Hipoactivo, succión pobre", "Glucosa 40 mg/dl · sin riesgo infeccioso"]),
  Q("¿Tiene síntomas?", [
      L("No", "Alimentar y controlar", ["Lactancia o fórmula, glucosa en 1 h"]),
      Q("Calcular el bolo", [
          L("2 ml/kg de dextrosa 10 %", "8 ML DE DEXTROSA 10 % EV", ["3,9 kg × 2 ml/kg ≈ 8 ml", "Luego infusión 6-8 mg/kg/min"], path=True)],
        edge="Sí", path=True)], path=True),
  ("Opciones de dosis", [("8 ml D10 %", True), ("4 ml D10 %", False), ("D5 % oral", False)], [
      ("Cálculo", ["2 ml/kg", "1 ml/kg", "Vía oral"]),
      ("Valoración", ["Correcta", "Dosis baja", "No en sintomático"])]),
  ["El postérmino grande tiene poca reserva de glucógeno.",
   "Controlar glucosa 30 minutos después del bolo.",
   "Nunca dextrosa concentrada (> 12,5 %) por vía periférica."],
  "AAP – Postnatal glucose homeostasis in late-preterm and term infants (Pediatrics 2011) · " + NELSON)

# PED-162 · matriz
V("matriz", "PED-162", "neonato-rpm-fiebre-infiltrado-leucocitosis-neutrofilia", "Hemograma según el germen",
  "PEDIATRÍA ENAM: NEUMONÍA NEONATAL BACTERIANA", "PEDIATRÍA",
  ("Neumonía neonatal precoz", ["RPM + fiebre + dificultad respiratoria + infiltrado bilateral",
   "Origen bacteriano: leucocitosis con neutrofilia (o neutropenia en casos graves)"]),
  ("Neonato de 36 h con RPM materna", ["T 38,5 °C, irritable, Silverman 6, cianosis", "Subcrepitantes · infiltrado bilateral"]),
  {"rotulo": "Patrón del hemograma", "eje_x": "Rasgo", "eje_y": "Patrón",
   "cols": ["Hallazgo", "Sugiere"], "rows": ["Bacteriano", "Viral", "Parasitario o alérgico", "Mononucleósico"], "caso": (0, 0),
   "cells": [[("LEUCOCITOSIS CON NEUTROFILIA", ["Desviación izquierda"]), ("Neumonía bacteriana", ["SGB, E. coli"])],
             [("Leucocitos normales", ["Linfocitosis"]), ("Virus", [])],
             [("Eosinofilia", []), ("Parásitos, alergia", [])],
             [("Monocitos y linfocitos", []), ("EBV, CMV", [])]]},
  ["En el neonato la neutropenia también es signo de sepsis grave.",
   "Índice inmaduros/totales > 0,2 apoya la infección.",
   "Iniciar ampicilina + gentamicina tras el hemocultivo."],
  "AAP – Management of neonates born at ≥ 35 weeks with suspected early-onset sepsis (Pediatrics 2018) · " + NELSON)

# SP-122 · radial
V("radial", "SP-122", "manejo-its-cuatro-c-no-calidad", "Las 4C de las ITS",
  "SALUD PÚBLICA ENAM: MANEJO SINDRÓMICO DE LAS ITS", "SALUD PÚBLICA",
  ("Manejo de las ITS", ["Además del fármaco, cada consulta incluye las 4C",
   "Consejería · Condones · Cumplimiento · Contactos"]),
  ("Pregunta de salud pública", ["¿Cuál no es una de las 4C?"]),
  {"rotulo": "Mapa del tema", "centro": "LAS 4C", "centro_sub": "¿Cuál sobra?", "ans": 0,
   "items": [("CALIDAD DE ATENCIÓN", ["NO es una de las 4C", "Es un principio general"]),
             ("Consejería", ["Riesgo y prevención"]),
             ("Condones", ["Entrega y uso correcto"]),
             ("Cumplimiento", ["Tomar todo el tratamiento"]),
             ("Contactos", ["Notificar y tratar parejas"])],
   "ruta": ["Consejería, condones", "Cumplimiento, contactos", "Cuatro C completas", "CALIDAD: NO ES UNA C"]},
  ["Tratar a la pareja evita la reinfección.",
   "Ofrecer pruebas de VIH, sífilis y hepatitis B en toda ITS.",
   "El manejo sindrómico trata en la primera consulta sin esperar laboratorio."],
  "MINSA – NTS 077: Manejo de infecciones de transmisión sexual · OMS – Guidelines for the management of symptomatic STIs (2021)")

# OFT-038 · tarjetas
V("tarjetas", "OFT-038", "nino-pila-boton-oido-extraccion-pinza", "Cuerpo extraño en el oído",
  "OTORRINOLARINGOLOGÍA ENAM: PILA DE BOTÓN EN EL OÍDO", "OTORRINOLARINGOLOGÍA",
  ("Cuerpos extraños en el oído", ["La conducta cambia según el objeto",
   "Pila de botón: corriente y álcali necrosan en horas; extraer ya y sin agua"]),
  ("Niño de 3 años, hace 1 hora", ["Se metió una pila de reloj al oído", "Otoscopia: pila y edema leve del conducto"]),
  {"rotulo": "¿Qué hacer según el objeto?", "ans": 0, "cards": [
      {"titulo": "PILA DE BOTÓN", "datos": [
          ("Riesgo", "Necrosis en horas", True), ("Lavado", "Prohibido", True),
          ("Conducta", "EXTRAER CON PINZA", True)],
       "pie": "Urgente, bajo visión directa"},
      {"titulo": "Insecto vivo", "datos": [
          ("Riesgo", "Dolor, lesión", False), ("Lavado", "Tras inmovilizar", False),
          ("Conducta", "Aceite o lidocaína", False)],
       "pie": "Luego extraer"},
      {"titulo": "Vegetal (semilla)", "datos": [
          ("Riesgo", "Se hincha", False), ("Lavado", "No", False),
          ("Conducta", "Pinza o gancho", False)],
       "pie": "Se hidrata con el agua"},
      {"titulo": "Objeto inerte", "datos": [
          ("Riesgo", "Bajo", False), ("Lavado", "Permitido", False),
          ("Conducta", "Lavado o pinza", False)],
       "pie": "Si la membrana está íntegra"}]},
  ["El agua o el lubricante aceleran la fuga del álcali de la pila.",
   "Si no se logra extraer: otorrino bajo microscopio y sedación.",
   "Revisar el otro oído y las fosas nasales."],
  "AAO-HNS – Clinical consensus on button battery injuries (2022) · Cummings Otolaryngology 7.ª ed. (2020)")

# SP-123 · matriz
V("matriz", "SP-123", "hipertenso-fumador-probabilidad-5-anos-incidencia-acumulada", "¿Qué indicador responde a cada pregunta?",
  "SALUD PÚBLICA ENAM: INCIDENCIA ACUMULADA Y RIESGO", "SALUD PÚBLICA",
  ("Incidencia acumulada", ["Es la probabilidad de enfermar en un periodo definido",
   "Responde: ¿qué riesgo tengo de enfermar en 5 años?"]),
  ("Paciente hipertenso y fumador", ["Pregunta su probabilidad de cardiopatía isquémica en 5 años"]),
  {"rotulo": "Indicador y pregunta que responde", "eje_x": "Rasgo", "eje_y": "Indicador",
   "cols": ["Responde a", "Unidad"], "rows": ["Incidencia acumulada", "Densidad de incidencia", "Riesgo relativo", "Fracción atribuible"], "caso": (0, 0),
   "cells": [[("PROBABILIDAD DE ENFERMAR", ["En un tiempo dado"]), ("Proporción (0 a 1)", ["Ej.: 12 % en 5 años"])],
             [("Velocidad de aparición", []), ("Casos / persona-año", [])],
             [("Cuántas veces más riesgo", ["Expuestos vs no"]), ("Sin unidad", [])],
             [("Qué parte se debe al factor", []), ("Porcentaje", [])]]},
  ["La incidencia acumulada del grupo con sus mismos factores estima su riesgo individual.",
   "El RR mide fuerza de asociación, no probabilidad absoluta.",
   "La densidad de incidencia usa tiempo-persona en el denominador."],
  "Gordis. Epidemiología 6.ª ed. (2019)")

# SP-124 · fases
V("fases", "SP-124", "hijos-dejan-hogar-ciclo-vital-dispersion", "Ciclo vital familiar",
  "SALUD PÚBLICA ENAM: CICLO VITAL FAMILIAR", "SALUD PÚBLICA",
  ("Etapas de la familia", ["Cada etapa tiene tareas y crisis esperables",
   "Dispersión: los hijos salen de casa por estudio, trabajo o pareja"]),
  ("Familia", ["Los hijos se van a estudiar, trabajar o vivir con su pareja"]),
  {"rotulo": "Etapas del ciclo", "ans": 2,
   "fases": [("Formación", "Pareja", "Unión", ["Sin hijos"]),
             ("Expansión", "Nacen hijos", "Crianza", ["Hasta el último hijo"]),
             ("Dispersión", "Salen los hijos", "HIJOS SE VAN", ["Estudio, trabajo, pareja"]),
             ("Independencia", "Nido vacío", "Pareja sola", ["Hijos independientes"]),
             ("Retiro", "Vejez", "Jubilación", ["Viudez, muerte"])],
   "curvas": [("Miembros en casa", SKY, [0.2, 0.6, 0.9, 0.75, 0.4, 0.25, 0.15])],
   "chips_titulo": "Etapa del caso · marcada la correcta",
   "chips": [("Dispersión", True), ("Expansión", False), ("Formación", False), ("Contracción", False)]},
  ["El ciclo vital ayuda a anticipar crisis normativas en la atención familiar.",
   "Expansión: desde el nacimiento del primer hijo.",
   "Nido vacío: la pareja reorganiza su relación."],
  "MINSA – Modelo de atención integral de salud basado en familia y comunidad (MAIS-BFC, 2011)")

# SP-125 · radial
V("radial", "SP-125", "valoracion-cognitiva-afectiva-sociofamiliar-adulto-mayor", "Valoración integral por etapa de vida",
  "SALUD PÚBLICA ENAM: VALORACIÓN CLÍNICA DEL ADULTO MAYOR", "SALUD PÚBLICA",
  ("Valoración clínica integral del adulto mayor", ["Incluye esferas funcional, mental (cognitiva y afectiva), social y clínica",
   "Detecta fragilidad y dependencia"]),
  ("Pregunta de atención integral", ["Estado cognitivo, afectivo y sociofamiliar", "¿En qué etapa de vida se evalúa?"]),
  {"rotulo": "Mapa del tema", "centro": "VALORACIÓN INTEGRAL", "centro_sub": "Según la etapa", "ans": 0,
   "items": [("ADULTO MAYOR", ["Cognitiva (Pfeiffer), afectiva (Yesavage)", "Sociofamiliar (Gijón), funcional (Katz)"]),
             ("Recién nacido", ["Apgar, Capurro, reflejos"]),
             ("Niño", ["CRED: crecimiento y desarrollo"]),
             ("Adolescente", ["HEADSSS, riesgo psicosocial"]),
             ("Adulto", ["Riesgo cardiovascular, tamizajes"])],
   "ruta": ["Cognitivo", "Afectivo", "Sociofamiliar", "ADULTO MAYOR (VACAM)"]},
  ["En el Perú se llama VACAM: Valoración clínica del adulto mayor.",
   "Clasifica al adulto mayor en autovalente, frágil, dependiente o geriátrico complejo.",
   "La depresión en el anciano suele pasar desapercibida."],
  "MINSA – NTS 043: Atención integral de salud de las personas adultas mayores · Guía técnica VACAM")

# PED-163 · tarjetas
V("tarjetas", "PED-163", "prematuro-cardiopatia-acianotica-ductus-permeable", "Cardiopatías acianóticas",
  "PEDIATRÍA ENAM: DUCTUS ARTERIOSO PERMEABLE", "PEDIATRÍA",
  ("Ductus arterioso persistente", ["El prematuro no cierra bien el ductus: falta músculo y la PGE2 sigue alta",
   "Es la cardiopatía acianótica más frecuente del pretérmino"]),
  ("Pregunta de neonatología", ["¿Cardiopatía acianótica más frecuente en el prematuro?"]),
  {"rotulo": "¿Cuál predomina en el prematuro?", "ans": 0, "cards": [
      {"titulo": "DUCTUS PERMEABLE", "datos": [
          ("Grupo", "Pretérmino", True), ("Soplo", "Continuo, en maquinaria", False),
          ("Pulsos", "Saltones", False), ("Cierre", "Ibuprofeno o paracetamol", False)],
       "pie": "Más frecuente en el prematuro"},
      {"titulo": "CIV", "datos": [
          ("Grupo", "Término", False), ("Soplo", "Holosistólico", False),
          ("Pulsos", "Normales", False), ("Cierre", "Espontáneo si es pequeña", False)],
       "pie": "La más frecuente en general"},
      {"titulo": "CIA", "datos": [
          ("Grupo", "Niños mayores", False), ("Soplo", "Sistólico pulmonar", False),
          ("Pulsos", "Normales", False), ("Cierre", "Dispositivo", False)],
       "pie": "Desdoblamiento fijo del S2"},
      {"titulo": "Canal AV", "datos": [
          ("Grupo", "Síndrome de Down", False), ("Soplo", "Variable", False),
          ("Pulsos", "Normales", False), ("Cierre", "Cirugía", False)],
       "pie": "Eje a la izquierda"}]},
  ["La insuficiencia cardiaca es una consecuencia, no una cardiopatía congénita.",
   "Signos: pulsos saltones, presión diferencial amplia, soplo continuo.",
   "Si fallan los fármacos: cierre quirúrgico o por cateterismo."],
  NELSON + " · AHA – Neonatal and pediatric congenital heart disease statement (2023)")

# END-049 · puntaje
V("puntaje", "END-049", "gestante-fiebre-taquicardia-150-confusa-tormenta-tiroidea", "Tirotoxicosis grave en la gestante",
  "ENDOCRINOLOGÍA ENAM: TORMENTA TIROIDEA", "ENDOCRINOLOGÍA",
  ("Tormenta tiroidea", ["Hipertiroidismo con falla de órganos: fiebre, taquicardia extrema, confusión",
   "La escala de Burch-Wartofsky estima la probabilidad"]),
  ("Gestante de 20 semanas", ["Intolerancia al calor, sudoración, diarrea", "T 39,8 °C · FC 150 · confusa · exoftalmos · bocio"]),
  {"rotulo": "Escala de Burch-Wartofsky", "escala": "Burch-Wartofsky", "total": 85, "max": 140,
   "total_label": "Puntaje del caso",
   "interpreta": "Muy sugestivo de tormenta tiroidea",
   "items": [("Temperatura 39,4-39,9 °C", "25", True), ("FC ≥ 140", "25", True),
             ("SNC: confusión o delirio", "20", True), ("Digestivo: diarrea", "10", True),
             ("Insuficiencia cardiaca leve", "5", True), ("Fibrilación auricular", "10", False)],
   "bandas": [("< 25", "Improbable", "Buscar otra causa", False),
              ("25-44", "Inminente", "Tratar si la clínica apoya", False),
              ("≥ 45", "Tormenta tiroidea", "UCI: PTU, yodo, betabloqueo, corticoide", True)]},
  ["Tirotoxicosis transitoria del embarazo: primer trimestre, sin exoftalmos ni bocio.",
   "Mola: β-hCG muy alta, útero grande para la edad gestacional.",
   "El yodo se da al menos 1 h después del PTU."],
  "ATA – Guidelines for hyperthyroidism and other causes of thyrotoxicosis (2016) · Japan Thyroid Association – Thyroid storm guidelines (2016)")

# PED-164 · fases
V("fases", "PED-164", "rn-apgar-bajo-ph-7-deficit-base-asfixia", "Del evento hipóxico a la secuela",
  "PEDIATRÍA ENAM: ASFIXIA PERINATAL", "PEDIATRÍA",
  ("Asfixia perinatal", ["Falta de oxígeno al nacer con acidosis metabólica",
   "Apgar bajo persistente + pH ≤ 7,0 o déficit de base ≥ 10-12"]),
  ("Recién nacido a término", ["Apgar 3 al minuto y 4 a los 5, 10 y 15 minutos", "pH 7,0 · HCO₃ 15 · déficit de base −10"]),
  {"rotulo": "Secuencia del daño", "ans": 1,
   "fases": [("Evento", "Intraparto", "Hipoxia", ["Placenta, cordón, parto difícil"]),
             ("Asfixia", "Al nacer", "APGAR BAJO + ACIDOSIS", ["pH ≤ 7,0", "Apgar ≤ 5 a los 5 min"]),
             ("Encefalopatía", "Primeras 72 h", "Sarnat I-III", ["Hipotonía, convulsiones"]),
             ("Secuela", "Meses-años", "Parálisis cerebral", ["Si hubo encefalopatía"])],
   "curvas": [("Daño cerebral", ROSE, [0.1, 0.3, 0.5, 0.65, 0.75, 0.8, 0.8])],
   "chips_titulo": "Diagnóstico · marcado el correcto",
   "chips": [("Asfixia perinatal", True), ("Encefalopatía hipóxico-isquémica", False), ("Depresión severa", False), ("Apnea neonatal", False)]},
  ["La encefalopatía se diagnostica con signos neurológicos, que aquí no se describen.",
   "Hipotermia terapéutica en las primeras 6 h si hay encefalopatía moderada o grave.",
   "Vigilar riñón, corazón e hígado: daño multiorgánico."],
  "AAP/ACOG – Neonatal encephalopathy and neurologic outcome 2.ª ed. (2014) · " + NELSON)

# GAS-059 · embudo
V("embudo", "GAS-059", "fumador-ictericia-acolia-masa-epigastrica-ca199-pancreas", "Ictericia obstructiva con baja de peso",
  "GASTROENTEROLOGÍA ENAM: CÁNCER DE CABEZA DE PÁNCREAS", "GASTROENTEROLOGÍA",
  ("Cáncer de páncreas", ["Cabeza: ictericia obstructiva, acolia, coluria",
   "Dolor que irradia a la espalda, baja de peso y CA 19-9 alto"]),
  ("Varón de 67 años, fumador pesado", ["2 meses de dolor epigástrico a la espalda, heces blancas", "Baja 10 kg · ictérico · masa dura de 7 cm · CA 19-9 77"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Ictericia con acolia y dolor epigástrico",
   "candidatos": ["Cáncer de páncreas", "Coledocolitiasis", "Colecistitis crónica", "Pancreatitis crónica"],
   "pasos": [("Baja de 10 kg y masa dura epigástrica", ["Coledocolitiasis", "Colecistitis crónica"]),
             ("Fumador mayor, CA 19-9 alto, sin historia de pancreatitis", ["Pancreatitis crónica"])],
   "final": ("CÁNCER DE CABEZA DE PÁNCREAS", ["TC trifásica de páncreas", "Whipple si es resecable"]),
   "nota": "Vesícula palpable no dolorosa con ictericia (Courvoisier) sugiere tumor."},
  ["El tabaco es el principal factor de riesgo modificable.",
   "El CA 19-9 sirve para seguimiento, no para tamizaje.",
   "Solo 15-20 % es resecable al diagnóstico."],
  "NCCN – Pancreatic adenocarcinoma (2025) · ESMO – Pancreatic cancer guideline (2023)")

# PED-165 · radial
V("radial", "PED-165", "lactante-diarrea-acuosa-explosiva-ecet", "Diarrea acuosa en el lactante",
  "PEDIATRÍA ENAM: DIARREA POR E. COLI ENTEROTOXIGÉNICA", "PEDIATRÍA",
  ("Diarrea secretora", ["La toxina de E. coli enterotoxigénica activa la secreción de agua y cloro",
   "Heces acuosas, explosivas, sin moco ni sangre"]),
  ("Lactante con 37,8 °C", ["Deposiciones acuosas explosivas, sin moco ni sangre", "Dolor abdominal y náuseas"]),
  {"rotulo": "Mapa del tema", "centro": "DIARREA INFECCIOSA", "centro_sub": "¿Acuosa o disentérica?", "ans": 0,
   "items": [("E. COLI ENTEROTOXIGÉNICA", ["Acuosa, secretora, sin sangre", "Toxinas termolábil y termoestable"]),
             ("Shigella", ["Disentería, fiebre alta"]),
             ("Salmonella", ["Fiebre, a veces sangre"]),
             ("Campylobacter", ["Sangre, dolor intenso"]),
             ("Rotavirus", ["Acuosa, vómitos, invierno"])],
   "ruta": ["Acuosa y explosiva", "Sin moco ni sangre", "Toxina sin invasión", "E. COLI ENTEROTOXIGÉNICA"]},
  ["Tratamiento: sales de rehidratación oral y zinc; no antibiótico de rutina.",
   "Es la causa más frecuente de diarrea del viajero.",
   "Con sangre (disentería): pensar en Shigella y dar antibiótico."],
  "OMS – Tratamiento de la diarrea: manual para médicos (2005) · " + NELSON)

# PED-166 · radial
V("radial", "PED-166", "intervencion-individual-potenciar-desarrollo-estimulacion-temprana", "Atención integral del niño",
  "PEDIATRÍA ENAM: ESTIMULACIÓN TEMPRANA", "PEDIATRÍA",
  ("Estimulación temprana", ["Intervención individual que potencia habilidades y actitudes del niño",
   "Atiende a tiempo las necesidades de su desarrollo integral"]),
  ("Pregunta de CRED", ["¿Cómo se llama esta intervención?"]),
  {"rotulo": "Mapa del tema", "centro": "ATENCIÓN DEL NIÑO", "centro_sub": "Componentes", "ans": 0,
   "items": [("ESTIMULACIÓN TEMPRANA", ["Potencia habilidades", "Motora, lenguaje, social"]),
             ("Control del desarrollo", ["Evalúa y detecta riesgos"]),
             ("Consejería nutricional", ["Alimentación adecuada"]),
             ("Inmunizaciones", ["Protege de infecciones"]),
             ("Suplementación", ["Hierro, vitamina A"])],
   "ruta": ["Intervención individual", "Atiende necesidades", "Potencia habilidades", "ESTIMULACIÓN TEMPRANA"]},
  ["El control del desarrollo evalúa; la estimulación interviene.",
   "Se enseña a los padres a hacerla en casa con juego y afecto.",
   "Prioridad en niños con riesgo biológico o social."],
  "MINSA – NTS 537: Control de crecimiento y desarrollo (2017)")

# NEF-070 · matriz
V("matriz", "NEF-070", "tumor-testicular-no-seminoma-alfafetoproteina", "Marcadores del cáncer de testículo",
  "UROLOGÍA ENAM: TUMOR TESTICULAR NO SEMINOMATOSO", "UROLOGÍA",
  ("Tumores de células germinales", ["Marcadores: AFP, β-hCG y LDH",
   "La AFP elevada indica componente no seminomatoso"]),
  ("Varón de 18 años", ["Tumor de testículo derecho", "Biopsia: no seminoma"]),
  {"rotulo": "Tumor y marcador", "eje_x": "Marcador", "eje_y": "Tumor",
   "cols": ["AFP", "β-hCG"], "rows": ["No seminoma", "Coriocarcinoma", "Seminoma puro"], "caso": (0, 0),
   "cells": [[("ELEVADA", ["Saco vitelino, embrionario"]), ("Variable", [])],
             [("Normal", []), ("Muy alta", [])],
             [("NORMAL SIEMPRE", ["Si sube, no es puro"]), ("A veces leve", [])]]},
  ["La LDH refleja la carga tumoral.",
   "Se miden antes y después de la orquiectomía inguinal.",
   "El CEA y el PSA no se usan en tumores testiculares."],
  "EAU – Guidelines on testicular cancer (2025) · NCCN – Testicular cancer (2025)")

# NEF-071 · tarjetas
V("tarjetas", "NEF-071", "nino-impetigo-previo-hematuria-edema-c3-bajo-gnpe", "Síndrome nefrítico en el niño",
  "NEFROLOGÍA ENAM: GLOMERULONEFRITIS POSTESTREPTOCÓCICA", "NEFROLOGÍA",
  ("Glomerulonefritis postestreptocócica", ["2-3 semanas tras faringitis o 3-6 tras impétigo",
   "Hematuria, edema, HTA, oliguria y C3 bajo"]),
  ("Niño de 7 años con impétigo hace 3 semanas", ["Orina escasa y hematúrica, edema palpebral", "PA 140/90 · C3 bajo"]),
  {"rotulo": "¿Qué glomerulopatía es?", "ans": 0, "cards": [
      {"titulo": "POSTESTREPTOCÓCICA", "datos": [
          ("Latencia", "2-6 semanas", True), ("Síndrome", "Nefrítico", True),
          ("C3", "Bajo, se normaliza", True), ("Edad", "Escolar", True)],
       "pie": "Sintomático: diurético y restricción de sal"},
      {"titulo": "Nefropatía por IgA", "datos": [
          ("Latencia", "1-2 días", False), ("Síndrome", "Hematuria recurrente", False),
          ("C3", "Normal", False), ("Edad", "Adolescente, adulto", False)],
       "pie": "Sinfaringítica"},
      {"titulo": "Membranoproliferativa", "datos": [
          ("Latencia", "Sin antecedente", False), ("Síndrome", "Mixto", False),
          ("C3", "Bajo persistente", False), ("Edad", "Variable", False)],
       "pie": "C3 bajo > 8 semanas: biopsia"},
      {"titulo": "Cambios mínimos", "datos": [
          ("Latencia", "—", False), ("Síndrome", "Nefrótico", False),
          ("C3", "Normal", False), ("Edad", "2-6 años", False)],
       "pie": "Proteinuria masiva, sin hematuria"}]},
  ["El C3 se normaliza en 6-8 semanas; si no, pensar en otra causa.",
   "Buen pronóstico en niños: la mayoría se recupera por completo.",
   "Tratar la infección no evita la glomerulonefritis, pero corta el contagio."],
  "KDIGO – Clinical practice guideline for the management of glomerular diseases (2021) · " + NELSON)

# PED-167 · matriz
V("matriz", "PED-167", "nina-fiebre-dolor-flanco-disuria-urocultivo", "¿Qué urocultivo confirma la ITU?",
  "PEDIATRÍA ENAM: PIELONEFRITIS EN LA NIÑA", "PEDIATRÍA",
  ("Infección urinaria en el niño", ["El examen de orina orienta; el urocultivo confirma",
   "El punto de corte depende de cómo se tomó la muestra"]),
  ("Niña de 4 años con 3 días de fiebre", ["Dolor en flancos, vómitos", "Polaquiuria, disuria y enuresis"]),
  {"rotulo": "Método de toma y umbral", "eje_x": "Rasgo", "eje_y": "Muestra",
   "cols": ["Umbral positivo", "Uso"], "rows": ["Chorro medio", "Sonda vesical", "Punción suprapúbica", "Bolsa recolectora"], "caso": (0, 0),
   "cells": [[("≥ 100 000 UFC/ML", ["Un solo germen"]), ("Niño que controla esfínteres", [])],
             [("≥ 10 000-50 000", []), ("Lactante", [])],
             [("Cualquier recuento", []), ("Lactante pequeño", [])],
             [("No confirma", ["Alta contaminación"]), ("Solo descarta si es negativo", [])]]},
  ["Fiebre + dolor en flanco = pielonefritis: tratar de inmediato tras el urocultivo.",
   "El Gram positivo en orina orienta, pero no confirma.",
   "Ecografía renal tras la primera ITU febril."],
  "AAP – Clinical practice guideline: urinary tract infection in febrile infants and children (2011, reafirmada 2016) · " + NELSON)

# TRA-036 · termómetro
V("termometro", "TRA-036", "atropello-glasgow-10-via-aerea-proteccion-cervical", "Politraumatizado con Glasgow 10",
  "TRAUMATOLOGÍA ENAM: PRIORIDADES EN EL POLITRAUMA", "TRAUMATOLOGÍA",
  ("Revisión primaria", ["Siempre empieza por la vía aérea con protección cervical",
   "Las fracturas y las heridas del cuero cabelludo esperan su turno"]),
  ("Varón de 20 años atropellado", ["PA 100/70 · FC 100 · FR 34 · Glasgow 10", "Herida en cuero cabelludo, muslo deformado · FAST (−)"]),
  {"rotulo": "Gravedad del TEC (Glasgow)",
   "niveles": [("13-15", "Leve", ["Observación, TC según riesgo"]),
               ("9-12", "Moderado", ["GLASGOW 10", "Vigilar deterioro"]),
               ("≤ 8", "Grave", ["Intubar"])],
   "caso_nivel": 1, "ruta_titulo": "Primer paso (ABCDE)", "paso_label": "PASO",
   "pasos": [(1, "Despejar vía aérea y proteger el cuello", ["Aspirar, collarín, O₂"], True),
             (2, "Ventilación y circulación", ["FR 34: buscar lesión torácica", "Comprimir la herida del cuero cabelludo"], False),
             (3, "Déficit neurológico y férula", ["Glasgow seriado; férula de fémur"], False)]},
  ["Todo politraumatizado con alteración de conciencia tiene lesión cervical hasta demostrar lo contrario.",
   "El FAST negativo no descarta todas las lesiones.",
   "Evitar hipoxia e hipotensión: duplican la mortalidad del TEC."],
  ATLS)

# PSI-032 · embudo
V("embudo", "PSI-032", "atracones-purgas-compensatorias-bulimia", "Atracones y purgas",
  "PSIQUIATRÍA ENAM: BULIMIA NERVIOSA", "PSIQUIATRÍA",
  ("Bulimia nerviosa", ["Atracones recurrentes + conductas compensatorias (vómitos, laxantes, ayuno)",
   "Peso casi normal; autoestima muy ligada al peso"]),
  ("Mujer de 21 años traída por su madre", ["Epigastralgia", "Atracones y necesidad de 'purgarse' para no subir de peso"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Preocupación por el peso con atracones",
   "candidatos": ["Bulimia", "Anorexia nerviosa", "Trastorno por atracón", "Depresión"],
   "pasos": [("Hay purgas compensatorias", ["Trastorno por atracón"]),
             ("Siente que aumentó de peso; sin restricción extrema ni bajo peso", ["Anorexia nerviosa"]),
             ("El problema central es la conducta alimentaria", ["Depresión"])],
   "final": ("BULIMIA NERVIOSA", ["Terapia cognitivo-conductual", "Fluoxetina 60 mg/día"]),
   "nota": "Vómitos repetidos: hipokalemia, erosión dental y signo de Russell."},
  ["Criterio: atracones y purgas al menos una vez por semana durante 3 meses.",
   "Controlar potasio: la hipokalemia causa arritmias.",
   "El bupropión está contraindicado: riesgo de convulsiones."],
  "APA – DSM-5-TR (2022) · APA – Practice guideline for the treatment of eating disorders (2023)")

# END-050 · árbol
A("END-050", "yodo-radiactivo-debilidad-cpk-alta-hipotiroidismo", "Debilidad tras yodo radiactivo",
  "ENDOCRINOLOGÍA ENAM: MIOPATÍA HIPOTIROIDEA", "ENDOCRINOLOGÍA",
  ("Hipotiroidismo tras yodo radiactivo", ["El yodo-131 destruye tiroides: el hipotiroidismo es esperable en meses",
   "Miopatía hipotiroidea: debilidad proximal con CPK alta"]),
  ("Mujer de 26 años", ["Recibió yodo radiactivo hace 6 meses por hipertiroidismo", "Debilidad progresiva · CPK y mioglobina altas"]),
  Q("¿Cómo está la TSH?", [
      L("Alta, T4L baja", "HIPOTIROIDISMO", ["Miopatía con CPK alta", "Levotiroxina"], path=True),
      L("Baja, T4L alta", "Hipertiroidismo persistente", ["Miopatía tirotóxica, CPK normal"]),
      L("Normal: medir calcio", "Alteración de paratiroides", ["Hipo o hiperparatiroidismo"])], path=True),
  ("Miopatía de origen tiroideo", [("Hipotiroidismo", True), ("Hipertiroidismo", False)], [
      ("CPK", ["Alta", "Normal"]),
      ("Clínica", ["Debilidad, calambres, lentitud", "Atrofia, debilidad proximal"]),
      ("Después del I-131", ["Esperable a los 2-6 meses", "Si falló el tratamiento"])]),
  ["Medir TSH y T4L a las 6-8 semanas del yodo radiactivo.",
   "La CPK se normaliza al reponer la hormona.",
   "Hipoparatiroidismo tras cirugía tiroidea, no tras yodo."],
  "ATA – Guidelines for hyperthyroidism (2016) · ATA – Guidelines for the treatment of hypothyroidism (2014)")

# PSI-033 · tarjetas
V("tarjetas", "PSI-033", "adolescente-discusion-opistotonos-crisis-psicogena", "Crisis convulsiva tras una discusión",
  "PSIQUIATRÍA ENAM: CRISIS PSICÓGENA NO EPILÉPTICA", "PSIQUIATRÍA",
  ("Crisis psicógenas no epilépticas", ["Episodios que parecen convulsiones, con desencadenante emocional",
   "Movimientos asincrónicos, opistótonos, recuperación inmediata"]),
  ("Mujer de 17 años tras discutir con su madre", ["Desconexión, movimientos tónicos, opistótonos, giros en la cama", "Recupera la conexión al terminar · sin crisis previas"]),
  {"rotulo": "¿Qué tipo de crisis?", "ans": 0, "cards": [
      {"titulo": "PSEUDOEPILÉPTICA", "datos": [
          ("Gatillo", "Emocional", True), ("Movimientos", "Asincrónicos, arco", True),
          ("Después", "Recupera al instante", True), ("Ojos", "Cerrados", False)],
       "pie": "Video-EEG normal durante la crisis"},
      {"titulo": "Tónico-clónica", "datos": [
          ("Gatillo", "Poco frecuente", False), ("Movimientos", "Sincrónicos", False),
          ("Después", "Confusión posictal", False), ("Ojos", "Abiertos", False)],
       "pie": "Mordedura lateral de lengua"},
      {"titulo": "Mioclónica", "datos": [
          ("Gatillo", "Al despertar", False), ("Movimientos", "Sacudidas breves", False),
          ("Después", "Conciencia conservada", False), ("Ojos", "Abiertos", False)],
       "pie": "Epilepsia mioclónica juvenil"},
      {"titulo": "Focal", "datos": [
          ("Gatillo", "No", False), ("Movimientos", "Un segmento", False),
          ("Después", "Déficit transitorio", False), ("Ojos", "Variable", False)],
       "pie": "Buscar lesión estructural"}]},
  ["Las escoriaciones en la punta de la lengua no son típicas de epilepsia (lateral).",
   "Confirmar con video-EEG; no iniciar antiepilépticos sin diagnóstico.",
   "Tratamiento: psicoterapia; buscar trauma o abuso."],
  "ILAE – Minimum requirements for the diagnosis of psychogenic nonepileptic seizures (Epilepsia 2013)")

# GAS-060 · árbol
A("GAS-060", "pancreatitis-cronica-baja-peso-dolor-tomografia", "Pancreatitis crónica con signos de alarma",
  "GASTROENTEROLOGÍA ENAM: PANCREATITIS CRÓNICA", "GASTROENTEROLOGÍA",
  ("Pancreatitis crónica", ["Aumenta el riesgo de cáncer de páncreas",
   "Dolor nuevo o persistente con baja de peso: imagen"]),
  ("Varón de 55 años con pancreatitis crónica alcohólica", ["Toma enzimas pancreáticas", "20 días de dolor que calma con AINE · baja 5 kg en 2 meses"]),
  Q("¿Hay signos de alarma?", [
      L("Sí: baja de peso, dolor nuevo", "TOMOGRAFÍA DE ABDOMEN", ["Descartar cáncer y pseudoquiste", "O colangio-RM"], path=True),
      L("No", "Continuar tratamiento", ["Enzimas, dejar alcohol y tabaco"])], path=True),
  ("Complicaciones de la pancreatitis crónica", [("Cáncer", True), ("Pseudoquiste", False), ("Diabetes", False)], [
      ("Clave", ["Baja de peso, ictericia", "Masa, saciedad", "Hiperglucemia"]),
      ("Estudio", ["TC, CA 19-9", "TC o ecografía", "Glucosa, HbA1c"])]),
  ["La baja de peso también puede ser maldigestión: ajustar la dosis de enzimas.",
   "No retirar las enzimas: mejoran la esteatorrea.",
   "El alcohol y el tabaco aceleran la enfermedad."],
  "ACG – Clinical guideline: Chronic pancreatitis (Am J Gastroenterol 2020)")

# NEU-046 · termómetro
V("termometro", "NEU-046", "maratonista-altura-deterioro-hipercapnia-ventilacion", "¿Cuándo ventilar?",
  "NEUMOLOGÍA ENAM: INSUFICIENCIA RESPIRATORIA HIPERCÁPNICA", "NEUMOLOGÍA",
  ("Indicación de ventilación mecánica", ["La hipoxemia se trata con oxígeno",
   "Hipercapnia grave con acidosis = falla ventilatoria: requiere ventilación"]),
  ("Maratonista de 39 años", ["Tras correr a 3600 m de altura", "Deterioro físico grave con desequilibrios importantes"]),
  {"rotulo": "Tipo y gravedad de la falla",
   "niveles": [("Tipo I", "Hipoxemia", ["SatO₂ baja, PaCO₂ normal", "Oxígeno"]),
               ("Leve", "Hipercapnia leve", ["pH > 7,35", "Vigilar"]),
               ("Grave", "Hipercapnia severa", ["PaCO₂ ALTA + ACIDOSIS", "La bomba falla"])],
   "caso_nivel": 2, "ruta_titulo": "Conducta", "paso_label": "PASO",
   "pasos": [(1, "Ventilación mecánica", ["Intubación si hay deterioro de conciencia", "VNI solo si coopera"], True),
             (2, "Corregir la causa", ["Agotamiento, edema pulmonar de altura"], False),
             (3, "Oxígeno", ["No basta si la hipercapnia sigue"], False)]},
  ["Una SatO₂ de 85 % en altura puede ser fisiológica.",
   "Dímero D y troponina no indican ventilación.",
   "Edema pulmonar de altura: descender, oxígeno y nifedipino."],
  "ERS/ATS – Guidelines on noninvasive ventilation for acute respiratory failure (2017) · " + HARRISON)

# CAR-060 · árbol
A("CAR-060", "paro-intrahospitalario-soporte-basico-monitor-desfibrilador", "Paro en la emergencia",
  "CARDIOLOGÍA ENAM: PARO CARDIACO INTRAHOSPITALARIO", "CARDIOLOGÍA",
  ("Paro cardiaco presenciado", ["Tras iniciar la RCP, lo siguiente es conectar el monitor desfibrilador",
   "El ritmo decide: descarga o no"]),
  ("Varón de 64 años con angina previa", ["En la emergencia pierde la conciencia y deja de respirar", "Soporte básico sin recuperar signos vitales"]),
  Q("¿RCP de calidad iniciada?", [
      Q("¿Ritmo en el monitor?", [
          L("FV o TV sin pulso", "MONITOR: DESCARGA", ["Desfibrilar y seguir RCP"], path=True),
          L("Asistolia o AESP", "RCP + adrenalina", ["Buscar causas reversibles"])],
        edge="Sí: colocar monitor desfibrilador", path=True),
      L("No", "Iniciar compresiones", ["30:2, 100-120/min"])], path=True),
  ("Orden de acciones", [("Monitor", True), ("Intubación", False), ("Adrenalina", False)], [
      ("Cuándo", ["Apenas llega", "Sin interrumpir la RCP", "Tras 2.ª descarga o ya en no desfibrilable"]),
      ("Por qué", ["El ritmo cambia la conducta", "No es prioridad inicial", "Después del ritmo"])]),
  ["En el paro de origen coronario el ritmo más frecuente es la FV.",
   "La intubación no debe interrumpir las compresiones.",
   "La atropina ya no se usa en la AESP ni en la asistolia."],
  "AHA – Guidelines for CPR and emergency cardiovascular care (2025)")

# NEU-047 · fases
V("fases", "NEU-047", "asma-ritmo-circadiano-crisis-madrugada", "Asma y hora del día",
  "NEUMOLOGÍA ENAM: ASMA NOCTURNA", "NEUMOLOGÍA",
  ("Ritmo circadiano del asma", ["De madrugada baja el cortisol, sube el tono vagal y cae el flujo espiratorio",
   "Las crisis son más frecuentes entre las 4 y las 6 de la mañana"]),
  ("Pregunta de fisiología", ["¿En qué horario hay más crisis de asma?"]),
  {"rotulo": "Función pulmonar a lo largo del día", "ans": 2,
   "fases": [("Noche", "20-22 h", "Flujo estable", ["Cortisol en descenso"]),
             ("Medianoche", "0-4 h", "Tono vagal alto", ["Empieza a caer el PEF"]),
             ("Madrugada", "4-6 h", "MÁS CRISIS", ["PEF en su punto más bajo"]),
             ("Mañana", "10-12 h", "Recupera", ["Cortisol alto"]),
             ("Tarde", "14-16 h", "Mejor flujo", ["PEF máximo"])],
   "curvas": [("Flujo espiratorio (PEF)", SKY, [0.75, 0.6, 0.4, 0.2, 0.5, 0.8, 0.9]),
              ("Cortisol", AMBER, [0.3, 0.15, 0.25, 0.6, 0.9, 0.7, 0.5])],
   "chips_titulo": "Horario · marcado el correcto",
   "chips": [("4 a 6 h", True), ("10 a 12 h", False), ("14 a 16 h", False), ("20 a 22 h", False)]},
  ["Despertares nocturnos por asma = mal control.",
   "La variabilidad del PEF > 10 % apoya el diagnóstico.",
   "El corticoide inhalado controla los síntomas nocturnos."],
  "GINA – Global Strategy for Asthma Management and Prevention (2025)")

# INF-084 · matriz
V("matriz", "INF-084", "gestante-fiebre-retroocular-tumbes-dengue-paracetamol", "Fiebre en el dengue: qué dar",
  "INFECTOLOGÍA ENAM: DENGUE EN LA GESTANTE", "INFECTOLOGÍA",
  ("Dengue en la gestante", ["Fiebre alta, mialgias y dolor retroocular tras estar en zona endémica",
   "Paracetamol para la fiebre; AINE y aspirina están prohibidos"]),
  ("Gestante de 19 años", ["Fiebre de 39 °C desde hoy, mialgias, dolor retroorbitario", "Estuvo en Tumbes hace 3 días"]),
  {"rotulo": "Antipirético y riesgo", "eje_x": "Rasgo", "eje_y": "Fármaco",
   "cols": ["¿Se usa?", "Riesgo"], "rows": ["Paracetamol", "Naproxeno o ketoprofeno", "Ácido acetilsalicílico"], "caso": (0, 0),
   "cells": [[("SÍ: DE ELECCIÓN", ["Máx. 4 g/día"]), ("Seguro en el embarazo", [])],
             [("No", []), ("Sangrado, cierre del ductus", ["Tercer trimestre"])],
             [("No", []), ("Sangrado por antiagregación", [])]]},
  ["Toda gestante con dengue se hospitaliza o vigila de cerca (grupo B).",
   "Signos de alarma: dolor abdominal, vómitos persistentes, sangrado, letargia.",
   "Hidratación oral abundante y controles de hematocrito."],
  "OPS – Directrices para el diagnóstico clínico y el tratamiento del dengue, chikungunya y zika (2022) · MINSA – GPC de dengue")

# INF-085 · termómetro
V("termometro", "INF-085", "diabetica-celulitis-facial-odontogena-vancomicina-clindamicina", "Infección odontógena que progresa",
  "INFECTOLOGÍA ENAM: CELULITIS FACIAL ODONTÓGENA", "INFECTOLOGÍA",
  ("Celulitis facial de origen dental", ["Flora polimicrobiana: estreptococos, anaerobios y S. aureus",
   "Si falla el tratamiento oral y hay toxicidad: EV de amplio espectro"]),
  ("Mujer diabética de 40 años con absceso molar", ["Sin mejoría con penicilina ni ciprofloxacino", "Fiebre alta, vómitos, edema facial caliente y doloroso"]),
  {"rotulo": "Gravedad",
   "niveles": [("Local", "Absceso dental", ["Drenaje + amoxicilina"]),
               ("Moderada", "Celulitis sin toxicidad", ["Amoxicilina-clavulánico oral"]),
               ("Grave", "Celulitis con fiebre alta", ["DIABÉTICA + FRACASO ORAL", "Hospitalizar, EV"])],
   "caso_nivel": 2, "ruta_titulo": "Manejo", "paso_label": "PASO",
   "pasos": [(1, "Vancomicina + clindamicina EV", ["Cubre SARM, estreptococos y anaerobios"], True),
             (2, "Drenaje del foco dental", ["Extracción o drenaje quirúrgico"], False),
             (3, "Vigilar la vía aérea", ["Angina de Ludwig, extensión cervical"], False)]},
  ["El ciprofloxacino cubre mal estreptococos y anaerobios orales.",
   "Sin drenar el foco, el antibiótico fracasa.",
   "La diabetes favorece infecciones graves y rápidas."],
  "IDSA – Practice guidelines for skin and soft tissue infections (2014) · Sanford Guide to Antimicrobial Therapy (2025)")

# NEU-048 · radial
V("radial", "NEU-048", "tbc-pleural-podagra-acido-urico-retirar-pirazinamida", "Reacciones adversas a antituberculosos",
  "NEUMOLOGÍA ENAM: GOTA POR PIRAZINAMIDA", "NEUMOLOGÍA",
  ("Efectos adversos del esquema", ["Cada fármaco tiene su toxicidad típica",
   "Pirazinamida: reduce la excreción de ácido úrico → hiperuricemia y gota"]),
  ("Varón de 28 años con TB pleural", ["Un mes de tratamiento de primera línea", "Artritis del primer ortejo · ácido úrico 12 mg/dl"]),
  {"rotulo": "Mapa del tema", "centro": "FÁRMACOS ANTI-TB", "centro_sub": "Toxicidad típica", "ans": 0,
   "items": [("PIRAZINAMIDA", ["Hiperuricemia, gota", "Hepatitis, artralgias"]),
             ("Isoniacida", ["Neuropatía (piridoxina), hepatitis"]),
             ("Rifampicina", ["Orina naranja, interacciones"]),
             ("Etambutol", ["Neuritis óptica"]),
             ("Estreptomicina", ["Ototoxicidad, nefrotoxicidad"])],
   "ruta": ["Un mes de tratamiento", "Podagra", "Ácido úrico 12", "RETIRAR PIRAZINAMIDA"]},
  ["La hiperuricemia asintomática por pirazinamida no obliga a retirarla.",
   "Con gota: retirar pirazinamida y ajustar la duración del esquema.",
   "Tratar la crisis con AINE o colchicina."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023)")

# NEU-049 · embudo
V("embudo", "NEU-049", "derrame-linfocitico-exudado-joven-ada-tuberculosis", "Derrame pleural linfocítico",
  "NEUMOLOGÍA ENAM: DERRAME PLEURAL TUBERCULOSO", "NEUMOLOGÍA",
  ("Derrame pleural tuberculoso", ["Exudado con > 50 % de linfocitos en un joven",
   "ADA > 40 U/L en líquido pleural confirma con alta probabilidad"]),
  ("Obrero de 27 años con 1 mes de fiebre y tos", ["Derrame pleural izquierdo", "Leucocitos 2500 (90 % linfocitos) · proteínas 4,9 · glucosa 67 · PAP (−)"]),
  {"rotulo": "Embudo diagnóstico",
   "inicio": "Exudado pleural en un joven",
   "candidatos": ["Tuberculosis", "Paraneumónico", "Empiema", "Neoplasia"],
   "pasos": [("90 % linfocitos, glucosa normal", ["Paraneumónico", "Empiema"]),
             ("Joven, PAP negativo, curso de un mes", ["Neoplasia"])],
   "final": ("TUBERCULOSIS PLEURAL", ["ADA en líquido pleural", "Biopsia pleural si hay duda"]),
   "nota": "La baciloscopía del líquido casi siempre es negativa: por eso se usa el ADA."},
  ["El pH y la TC no hacen el diagnóstico de TB.",
   "La tuberculina puede ser negativa al inicio.",
   "Tratamiento: esquema antituberculoso estándar."],
  "MINSA – NTS 200: Atención integral de la persona afectada por tuberculosis (2023) · BTS – Guideline for pleural disease (2023)")
