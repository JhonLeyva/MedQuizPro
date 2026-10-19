"""Cuatro flujogramas de muestra del bloque ENAM 2026, con ilustración propia del caso."""
import os
from c4 import T
from engine5 import (build5, ilu_cuerpo_nueve, ilu_pelvis_hernias, ilu_rx_volvulo, ilu_eco_tn,
                     ORANGE, GREEN, RED)
from engine3 import AMBER
from engine import TEAL

F = []


def V(tipo, id_, archivo, titulo, barra, esp, tema, caso, d, perlas, fuente, tabla=None):
    F.append(dict(tipo=tipo, id=id_, archivo=archivo, titulo=titulo, barra=barra, esp=esp,
                  tema={"title": tema[0], "lines": tema[1]}, caso={"title": caso[0], "lines": caso[1]},
                  d=d, perlas=perlas, fuente=fuente, tabla=T(*tabla) if tabla else None))


# 1 ── CIR-133 · Parkland (diseño: CÁLCULO + cuerpo con regla de los 9)
V("calculo", "CIR-133", "quemado-parkland-regla-de-los-nueve",
  "Quemadura del 30 %: cálculo de Parkland paso a paso",
  "Quemaduras · reposición de líquidos con la fórmula de Parkland", "CIRUGÍA ENAM: QUEMADOS",
  ("Reanimación con líquidos en el gran quemado",
   ["La superficie quemada (SCQ) se estima con la regla de los 9 y solo cuenta la quemadura de 2.º y 3.º grado.",
    "Parkland = 4 mL × peso (kg) × % SCQ en 24 h, con lactato de Ringer."]),
  ("Varón de 36 años, 70 kg, explosión de gas",
   ["Flictenas en tórax, abdomen, brazos y cara anterior de muslos; SCQ estimada 30 %.",
    "Piden el volumen total de 24 h."]),
  dict(rotulo="Del cuerpo quemado al volumen de cristaloide",
       ilu_titulo="Regla de los 9 (adulto)", ilu=lambda s, x, y: ilu_cuerpo_nueve(
           s, x, y, {"torax", "abdomen", "brazo_d", "brazo_i", "muslo_d", "muslo_i"}),
       ilu_pie="Naranja: zonas del caso. Cada miembro inferior vale 18 % y la espalda 18 %. El enunciado da SCQ = 30 %.",
       tag="ESTE CASO",
       pasos=[("Datos del caso", ["Peso: 70 kg · SCQ de 2.º y 3.º grado: 30 %.",
                                   "El eritema simple (1.er grado) no se suma."], False),
              ("Fórmula de Parkland", ["4 mL × 70 kg × 30 % = 8 400 mL en 24 horas.",
                                        "Es el volumen TOTAL que pide la pregunta."], True),
              ("Cómo se reparte", ["La mitad (4 200 mL) en las primeras 8 h desde la quemadura;",
                                   "la otra mitad (4 200 mL) en las 16 h siguientes."], False),
              ("Cómo se ajusta", ["Meta de diuresis: 0,5-1 mL/kg/h = 35-70 mL/h en este paciente.",
                                  "Guías actuales: 2-4 mL/kg/% para evitar la sobrecarga."], False)],
       reparto=dict(titulo="Reparto de los 8 400 mL en 24 horas",
                    tramos=[("primeras 8 h", 8, "4 200 mL", ORANGE), ("16 h siguientes", 16, "4 200 mL", TEAL)])),
  ["Parkland: 4 mL × kg × % SCQ = volumen de 24 h; la mitad en las primeras 8 h desde la quemadura, no desde el ingreso.",
   "4 200 mL es solo la mitad (primeras 8 h); 10 500 mL sale de usar 5 mL por kg y por %.",
   "El mejor monitor de la reanimación es la diuresis horaria (0,5-1 mL/kg/h en adultos)."],
  "ATLS 11.ª ed. (2025); guía ISBI 2016 y American Burn Association.",
  ("Opciones de volumen", [("4 200 mL", False), ("8 400 mL", True), ("10 500 mL", False)],
   [("De dónde sale", ["Solo la mitad: primeras 8 h", "4 × 70 × 30 (24 h)", "5 × 70 × 30: fórmula errada"]),
    ("¿Es el total de 24 h?", ["No", "Sí", "No"])]))

# 2 ── CIR-158 · Hernia obturatriz (diseño: ANATOMÍA + pelvis con los 4 orificios)
V("anatomia", "CIR-158", "hernia-obturatriz-mapa-pelvico-howship-romberg",
  "Hernia obturatriz: dónde sale cada hernia de la ingle",
  "Hernias de la pared y del piso pélvico · diagnóstico por localización", "CIRUGÍA ENAM: HERNIAS",
  ("Hernias de la región inguinal y pélvica",
   ["Cada hernia sale por un orificio distinto; la localización y los signos dicen cuál es.",
    "Las que salen por orificios estrechos (femoral, obturatriz) se estrangulan más."]),
  ("Mujer de 82 años, delgada, con obstrucción",
   ["Dolor cólico, distensión y dolor irradiado a la cara interna del muslo derecho.",
    "Howship-Romberg (+); masa dolorosa en la pared pélvica al tacto vaginal."]),
  dict(rotulo="Mapa de la pelvis: cuatro orificios, cuatro hernias",
       ilu_titulo="Pelvis vista de frente", ilu=lambda s, x, y: ilu_pelvis_hernias(s, x, y, 4),
       ilu_pie="El punto 4 (agujero obturador) es el de este caso: por ahí pasa el nervio obturador.",
       ans=4, tag="ESTE CASO",
       puntos=[("Inguinal indirecta", ["Sale por el anillo inguinal profundo, lateral a los vasos epigástricos.",
                                        "Varón joven; baja hacia el escroto."]),
               ("Inguinal directa", ["Empuja la pared posterior (triángulo de Hesselbach), medial a los epigástricos.",
                                     "Varón mayor; se estrangula poco."]),
               ("Femoral", ["Debajo del ligamento inguinal, medial a la vena femoral.",
                            "Mujer; bulto en la raíz del muslo."]),
               ("Obturatriz", ["Sale por el agujero obturador y comprime el nervio obturador.",
                               "Anciana delgada; no se ve bulto: se palpa por tacto vaginal o rectal."])],
       signo=dict(muslo=True, titulo="Signo de Howship-Romberg",
                  lines=["Dolor o parestesias en la cara interna del muslo que empeoran al extender, abducir o rotar "
                         "hacia dentro la cadera: la hernia aprieta el nervio obturador.",
                         "Con obstrucción intestinal en una anciana delgada, este signo casi confirma la hernia obturatriz."])),
  ["Hernia obturatriz = «hernia de la anciana delgada»: obstrucción intestinal + Howship-Romberg (+).",
   "No da bulto visible: se sospecha por el dolor en la cara interna del muslo y se confirma con TC.",
   "La femoral también es de mujeres, pero da un bulto bajo el ligamento inguinal y no afecta al nervio obturador."],
  "Schwartz Principios de Cirugía 11.ª ed.; Sabiston Tratado de Cirugía 21.ª ed.")

# 3 ── CIR-150 · Vólvulo de sigmoides (diseño: SEMÁFORO + Rx «grano de café»)
V("semaforo", "CIR-150", "volvulo-sigmoides-semaforo-devolvulacion",
  "Vólvulo de sigmoides: el semáforo de la isquemia decide la conducta",
  "Obstrucción de colon · vólvulo de sigmoides", "CIRUGÍA ENAM: OBSTRUCCIÓN INTESTINAL",
  ("Vólvulo de sigmoides",
   ["El sigmoides largo y redundante gira sobre su mesenterio: obstrucción en asa cerrada.",
    "La conducta depende de si el asa ya sufre (isquemia, perforación) o todavía está viable."]),
  ("Varón de 71 años, 4 días de distensión",
   ["Sin flatos, abdomen timpánico, RHA ausentes, ampolla rectal vacía.",
    "Estable, afebril, leucocitos 9000; Rx: «grano de café»."]),
  dict(rotulo="Imagen del caso y semáforo de conducta",
       ilu_titulo="Rx simple de abdomen", ilu=lambda s, x, y: ilu_rx_volvulo(s, x, y),
       ilu_pie="Asa sigmoidea muy dilatada que nace en la pelvis y apunta al hipocondrio derecho.",
       check_titulo="¿Hay signos de sufrimiento del asa?",
       check=[("Afebril (T 37 °C)", True), ("Hemodinamia estable (PA 124/82, FC 90)", True),
              ("Leucocitos normales (9000/mm³)", True), ("Sin defensa ni irritación peritoneal", True)],
       ans=0, tag="ESTE CASO",
       luces=[("Asa viable, sin isquemia", "Devolvulación endoscópica",
               ["Rectosigmoidoscopia que destuerce y deja sonda rectal; luego sigmoidectomía electiva por recurrencia."]),
              ("Falla o recurrencia", "Cirugía programada o urgente",
               ["Si no se logra destorcer o reaparece: sigmoidectomía."]),
              ("Isquemia, perforación o peritonitis", "Laparotomía de urgencia",
               ["Fiebre, leucocitosis, defensa o mucosa negra en la endoscopía: resección (Hartmann)."])]),
  ["Rx con «grano de café» = vólvulo de sigmoides; es típico del anciano con estreñimiento crónico.",
   "Sin signos de isquemia, primero se destuerce por endoscopía; la cirugía es para el asa sufriente o el fracaso.",
   "La neostigmina es para la pseudoobstrucción (Ogilvie), no para una torsión mecánica."],
  "Sabiston Tratado de Cirugía 21.ª ed.; guía ASCRS de vólvulo de colon (2021).")

# 4 ── GIN-274 · Translucencia nucal (diseño: CRONOLOGÍA + ecografía de 12 semanas)
V("cronologia", "GIN-274", "translucencia-nucal-cronologia-tamizaje-prenatal",
  "Translucencia nucal aumentada: qué detecta cada prueba prenatal",
  "Tamizaje prenatal del primer trimestre · translucencia nucal", "GINECO-OBSTETRICIA ENAM",
  ("Tamizaje de aneuploidías en el primer trimestre",
   ["La translucencia nucal (TN) se mide entre las 11 y 13+6 semanas.",
    "Una TN mayor del percentil 95 eleva el riesgo de cromosomopatía (trisomía 21, 18, 13)."]),
  ("Primigesta de 35 años, 12 semanas",
   ["Primer control prenatal.", "Ecografía: TN por encima del percentil 95."]),
  dict(rotulo="Hallazgo del caso y a qué riesgo apunta",
       ilu_titulo="Ecografía de 12 semanas", ilu=lambda s, x, y: ilu_eco_tn(s, x, y),
       ilu_pie="La banda oscura de la nuca está engrosada: TN por encima del percentil 95.",
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
  ["La TN se mide entre las 11 y 13+6 semanas (longitud craneocaudal 45-84 mm).",
   "TN > p95 = mayor riesgo de aneuploidía: ofrecer ADN fetal libre o diagnóstico invasivo y ecocardiografía fetal.",
   "Tubo neural: alfafetoproteína y ecografía morfológica; preeclampsia: Doppler de uterinas."],
  "Williams Obstetricia 26.ª ed.; Fetal Medicine Foundation; ACOG Practice Bulletin 226 (2020).")

if __name__ == "__main__":
    os.makedirs("out26demo/flujogramas", exist_ok=True)
    for f in F:
        open(f"out26demo/flujogramas/{f['archivo']}.svg", "w").write(build5(f))
        print(f["id"], f["archivo"])
