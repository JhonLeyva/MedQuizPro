# -*- coding: utf-8 -*-
"""Cuatro flujogramas ENAM rehechos con imágenes reales y bloques de criterios/escalas/banderas rojas."""
import json, os
from PIL import Image
import c26
from c26 import S, B, D, P, F26
from c4 import T
import engine
from engine9 import _img
ESP = "CIRUGÍA ENAM"
AQUI = os.path.dirname(os.path.abspath(__file__))
CRED = json.load(open(os.path.join(AQUI, "creditos_idx.json"), encoding="utf-8"))


def PX(archivo, W, marcas=(), credito=None):
    ruta = os.path.join(AQUI, "img", archivo)
    w, h = Image.open(ruta).size
    if credito is None:
        try:
            credito = json.load(open(ruta + ".json", encoding="utf-8"))["credito"]
        except (OSError, KeyError):
            credito = CRED[archivo]
    return P(archivo, W, round(W * h / w), marcas, credito)


FIX = []
ECO = PX("apendicitis_pocus.jpg", 330, credito="Kaplan et al. · POCUS J 2025 · PMC12057466 · CC BY 4.0")
NOTAS_ECO = [("Apéndice dilatado y de pared gruesa", "Diámetro mayor de 6-7 mm: aquí 6,8 mm en el corte corto y 8,2 mm en el largo."),
             ("Dos cortes del mismo órgano", "Izquierda: eje corto, redondo («diana»). Derecha: eje largo, tubo ciego."),
             ("Grasa vecina más brillante", "La hiperecogenicidad periapendicular sugiere inflamación; no se comprime con la sonda."),
             ("Cuándo se pide imagen", "Alvarado intermedio (5-6), niños, embarazadas y ancianos: la eco o la TC definen.")]

# 1 · ALVARADO
S("puntaje", "CIR-140", "escala-alvarado-8-puntos-apendicitis-probable",
  "Escala de Alvarado: este caso suma 8 puntos",
  "Apendicitis aguda · escala de Alvarado", ESP,
  ("Escala de Alvarado", ["Ocho datos de clínica y laboratorio; máximo 10 puntos.",
                          "Dos datos valen 2: dolor en FID y leucocitosis > 10 000."]),
  ("Mujer de 62 años, 12 h de dolor que migró a FID", ["Anorexia, 2 vómitos, T 38,5 °C; McBurney y Blumberg (+).",
                                                       "Leucocitos 9 890 y neutrófilos 77 %."]),
  ["Leucocitos 9 890 no llegan a 10 000: no suman; los neutrófilos 77 % sí suman 1.",
   "Conducta por puntaje: 0-4 observar; 5-6 imagen (eco o TC); 7-8 evaluación quirúrgica; 9-10 apendicectomía. WSES 2020 prefiere AIR o Adult Appendicitis Score y estratificar con imagen.",
   "Signos semiológicos que apoyan: Rovsing, psoas, obturador y dolor al toser (Dunphy); Blumberg indica irritación peritoneal.",
   "Banderas rojas: defensa generalizada, rigidez, fiebre alta, taquicardia o hipotensión sugieren perforación o peritonitis: antibiótico, reanimación y cirugía urgente.",
   "Mnemotecnia MANTRELS: Migración, Anorexia, Náuseas, Tenderness (dolor FID), Rebote, Elevación de T°, Leucocitosis, Shift (desviación)."],
  "Alvarado A. Ann Emerg Med 1986; WSES, guía de apendicitis aguda de Jerusalén (2020); Kaplan et al., POCUS J 2025.",
  d=dict(rotulo="Punto por punto", escala="Escala de Alvarado", total=8, max=10,
         interpreta="Apendicitis probable: evaluación por cirugía",
         items=[("Dolor que migra a FID", 1, True), ("Anorexia", 1, True), ("Náuseas o vómitos", 1, True),
                ("Dolor en FID (McBurney)", 2, True), ("Rebote (Blumberg)", 1, True), ("Temperatura > 37,3 °C", 1, True),
                ("Leucocitos > 10 000 (tiene 9 890)", 2, False), ("Neutrófilos > 75 % (tiene 77 %)", 1, True)],
         bandas=[("0-4", "Poco probable", "Observar o alta con control.", False),
                 ("5-6", "Posible", "Observación e imagen (eco o TC).", False),
                 ("7-8", "Probable", "Evaluación por cirugía.", True),
                 ("9-10", "Muy probable", "Apendicectomía.", False)]),
  banda=B("Así se ve en la ecografía", ECO, NOTAS_ECO, pie="Apendicitis: ecografía real (ejemplo pediátrico)"),
  tabla=("Opciones de la pregunta", [("8", True), ("6", False), ("9", False), ("7", False)],
         [("Por qué", ["Suma correcta", "Olvida McBurney o rebote", "Cuenta leucocitos como 1", "Omite un ítem"])]),
  _reg=FIX)

# 2 · APENDICITIS EN EL PRIMER NIVEL
S("red", "CIR-154", "apendicitis-aguda-primer-nivel-hidratacion-antibiotico-referencia",
  "Apendicitis en un establecimiento del primer nivel: estabilizar y referir",
  "Apendicitis aguda · niveles de atención", ESP,
  ("Apendicitis aguda", ["El diagnóstico es clínico; el tratamiento es quirúrgico.",
                         "Si el establecimiento no opera, se prepara y se refiere sin demora."]),
  ("Varón de 22 años en el primer nivel", ["24 h de dolor periumbilical, náuseas y vómitos.",
                                           "T 38,7 °C, dolor en FID y Blumberg (+)."]),
  ["Apendicitis clínica en el primer nivel: hidratación EV, antibiótico EV, analgesia y referencia inmediata.",
   "Diagnóstico: dolor que migra a FID, anorexia, náuseas, fiebre y Blumberg; Alvarado 7 o más = probable. No esperar exámenes para referir.",
   "Banderas rojas para referir de emergencia: defensa o rigidez generalizada, taquicardia, hipotensión, fiebre alta o masa palpable (plastrón o absceso).",
   "Mayor riesgo de presentación atípica: niños pequeños, embarazadas y ancianos."],
  "MINSA, norma de referencia y contrarreferencia; WSES, guía de Jerusalén (2020).",
  d=dict(rotulo="Dónde está el paciente y a dónde va", caso="I-3", destino="II-1", flecha="Referir ya", tag="ESTE CASO",
         claves=[("En el primer nivel", ["Vía EV, hidratación, antibiótico EV y analgesia."], True),
                 ("Referencia inmediata", ["A un hospital con cirugía (II-1 o más)."], False),
                 ("No retrasar", ["Ni observar ni esperar exámenes: el riesgo es la perforación."], False)]),
  banda=B("Cómo se ve la apendicitis", ECO, NOTAS_ECO[:3], pie="Ecografía real de apendicitis (ejemplo pediátrico)"),
  tabla=("Opciones de la pregunta", [("Observar en el establecimiento", False), ("Hidratar, ATB y referir", True),
                                     ("Exámenes y luego referir", False), ("Referencia diferida", False)],
         [("Problema", ["No hay cirugía ahí", "Ninguno", "Retrasa sin cambiar la conducta", "Riesgo de perforación"])]),
  _reg=FIX)

# 3 · TRANSLUCENCIA NUCAL
TN = PX("tn_down.jpg", 262, [("flecha", 0.30, 0.71, 0.62, 0.86, "TN (calibres)")], credito="Moroder · Wikimedia Commons · CC BY-SA 3.0")
S("cronologia", "GIN-274", "translucencia-nucal-cronologia-tamizaje-prenatal",
  "Translucencia nucal aumentada: qué detecta cada prueba prenatal",
  "Tamizaje prenatal del primer trimestre · translucencia nucal", "GINECO-OBSTETRICIA ENAM",
  ("Tamizaje de aneuploidías en el primer trimestre",
   ["La translucencia nucal (TN) se mide entre las 11 y 13+6 semanas.",
    "Una TN mayor del percentil 95 (o ≥ 3,0-3,5 mm) eleva el riesgo de cromosomopatía (trisomía 21, 18, 13)."]),
  ("Primigesta de 35 años, 12 semanas", ["Primer control prenatal.", "Ecografía: TN por encima del percentil 95."]),
  ["La TN se mide entre las 11 y 13+6 semanas (longitud craneocaudal 45-84 mm), en corte sagital, con calibres en el borde interno de la piel y de la fascia.",
   "Tamizaje combinado: edad materna + TN + β-hCG libre + PAPP-A; con TN > p95 se ofrece ADN fetal libre o diagnóstico invasivo (biopsia de corion o amniocentesis) y ecocardiografía fetal.",
   "Otros marcadores del primer trimestre: hueso nasal ausente, regurgitación tricuspídea y flujo anormal del ductus venoso.",
   "Banderas rojas: TN ≥ 3,5 mm con cariotipo normal obliga a buscar cardiopatía y síndromes genéticos; higroma quístico o hidrops: alto riesgo.",
   "Tubo neural: alfafetoproteína y ecografía morfológica; preeclampsia: Doppler de uterinas."],
  "Williams Obstetricia 26.ª ed.; Fetal Medicine Foundation; ACOG Practice Bulletin 226 (2020); ISUOG, ecografía del primer trimestre (2023).",
  d=dict(rotulo="Hallazgo del caso y a qué riesgo apunta",
         ilu_titulo="Ecografía real de 11+6 semanas", ilu=lambda s, x, y: _img(s, x, y, TN),
         ilu_pie="Feto con trisomía 21 confirmada; calibres en la nuca (TN) y ausencia de hueso nasal.",
         tag="ESTE CASO",
         claves=[("TN aumentada → cromosomopatía fetal",
                  ["Principal riesgo: trisomía 21; también 18, 13 y cardiopatías.",
                   "Se ofrece ADN fetal libre o prueba invasiva (biopsia de corion, amniocentesis)."], True),
                 ("Tubo neural → no es la TN", ["Se busca con alfafetoproteína y ecografía morfológica (18-22 sem)."], False),
                 ("Preeclampsia precoz → no es la TN", ["Se predice con Doppler de arterias uterinas y PlGF a las 11-14 sem."], False),
                 ("Restricción del crecimiento → no es la TN", ["Se vigila con biometría y Doppler en el 3.er trimestre."], False)],
         eje_titulo="Cuándo se hace cada prueba", eje=(8, 36), paso=4, marca=12,
         hitos=[(11, 14, "TN + tamizaje combinado", "cromosomopatías", True),
                (10, 22, "ADN fetal libre", "cromosomopatías", False),
                (11, 14, "Doppler uterinas", "preeclampsia", False),
                (15, 20, "Alfafetoproteína", "tubo neural", False),
                (18, 22, "Eco morfológica", "malformaciones", False),
                (28, 36, "Biometría y Doppler", "crecimiento fetal", False)]),
  _reg=FIX)

# 4 · DISPLASIA DE CADERA
RX = PX("ddc_rx_lineas.jpg", 470)
S("arbol_imagen", "TRA-057", "displasia-cadera-lactante-9-meses-rx-pelvis-hilgenreiner-perkins",
  "Displasia de cadera a los 9 meses: la Rx de pelvis y cómo leerla",
  "Ortopedia infantil · displasia del desarrollo de la cadera (DDC)", "TRAUMATOLOGÍA ENAM",
  ("Displasia del desarrollo de la cadera",
   ["Cadera inestable o luxada desde el nacimiento; riesgo: parto podálico, sexo femenino, primogénito, familiar con DDC.",
    "El examen depende de la edad: ecografía antes de que osifique la cabeza femoral, Rx después."]),
  ("Lactante de 9 meses, parto podálico", ["Arrastra la pierna izquierda al gatear.", "Abducción limitada y miembro inferior izquierdo más corto."]),
  ["Menor de 4-6 meses: ecografía de caderas (clasificación de Graf); mayor de 4-6 meses: Rx AP de pelvis.",
   "Normal: el núcleo femoral está en el cuadrante inferointerno (bajo Hilgenreiner y medial a Perkins); en la DDC sube y se va afuera.",
   "Índice acetabular mayor de 30° al año y línea de Shenton rota apoyan displasia o luxación.",
   "Banderas rojas: limitación de la abducción, asimetría de pliegues, acortamiento del miembro, signo de Galeazzi y Ortolani/Barlow positivos; el diagnóstico tardío obliga a cirugía.",
   "Factores de riesgo: podálico, sexo femenino, primogénito, antecedente familiar y oligohidramnios; se hace tamizaje ecográfico a las 4-6 semanas si hay riesgo."],
  "Tachdjian Ortopedia Pediátrica 6.ª ed.; guía AAOS de displasia del desarrollo de la cadera; Sha et al., Front Pediatr 2023.",
  d=dict(rotulo="Qué examen pedir según la edad", tag="ESTE CASO",
         pregunta="¿Ya se osificó el núcleo de la cabeza femoral? (aparece hacia los 4-6 meses)",
         ramas=[("NO: < 4-6 meses", "Ecografía de caderas (Graf)",
                 ["El núcleo aún es cartílago y no se ve en la Rx.", "Se mide el ángulo alfa y se clasifica así:",
                  "Graf I: α ≥ 60° (normal).", "Graf IIa: α 50-59° antes de las 12 semanas (inmadurez fisiológica).",
                  "Graf IIb: α 50-59° después de las 12 semanas (displasia).", "Graf IIc: α 43-49° (displasia crítica).",
                  "Graf D, III y IV: α < 43° (descentrada o luxada).", "Ortolani: reduce la cadera luxada (clic). Barlow: luxa la cadera reducible.", "Ambas maniobras solo sirven en el recién nacido y hasta los 2-3 meses.", "Alerta: pliegues asimétricos, abducción limitada, acortamiento del miembro y signo de Galeazzi.", "En menores de 4-6 meses la Rx no decide: el núcleo aún no se ve.", "Conducta por tipo: Graf I alta; IIa control a las 4-6 semanas; IIb y IIc arnés de Pavlik; D, III y IV derivar a ortopedia infantil.", "Se tamiza con ecografía a las 4-6 semanas al lactante con podálico o antecedente familiar.", "Cuanto más temprano el diagnóstico, menos probabilidad de cirugía."]),
                ("SÍ: 9 meses", "Rx AP de pelvis y caderas",
                 ["Con el núcleo ya osificado, la Rx muestra dónde está la cabeza femoral respecto del acetábulo."])],
         ilu=lambda s, x, y: _img(s, x, y, RX), IW=470, IH=RX["H"] + 18,
         ilu_pie="Rx AP de pelvis de un niño con las líneas de referencia: Hilgenreiner (horizontal, roja), Perkin (verticales, verdes) e índice acetabular. En la DDC el núcleo queda arriba y afuera.",
         luego_titulo="Después del diagnóstico: tratamiento según la edad",
         luego=[("Menos de 6 meses", ["Arnés de Pavlik si la cadera se reduce."], False),
                ("6 a 18 meses", ["Reducción cerrada bajo anestesia (abierta si no se logra) y yeso en espica."], True),
                ("Más de 18 meses", ["Reducción abierta, a menudo con osteotomía de pelvis o fémur."], False)]),
  tabla=("Opciones de la pregunta",
         [("Rx de pelvis", True), ("Arnés de Pavlik", False), ("Ecografía de caderas", False), ("Observar 3 meses", False)],
         [("Cuándo sirve", ["Desde los 4-6 meses, con núcleo osificado", "Menores de 6 meses con cadera reducible", "Menores de 4-6 meses", "Nunca con un examen anormal"]),
          ("¿En este caso?", ["Sí", "No: tiene 9 meses y aún no hay diagnóstico", "No: el núcleo ya se osificó", "No: retrasa el tratamiento"])]),
  _reg=FIX)
