"""Cuatro flujogramas de muestra del bloque ENAM 2026 con imágenes reales (licencia libre) o dibujos propios.
Diseños nuevos: 13 comparador · 14 escalera · 19 mapa corporal de signos · 20 árbol con imagen."""
import os
from c4 import T
from engine6 import build6, ilu_nino_sarampion, ilu_rx_ddc

F = []


def V(tipo, id_, archivo, titulo, barra, esp, tema, caso, d, perlas, fuente, tabla=None):
    F.append(dict(tipo=tipo, id=id_, archivo=archivo, titulo=titulo, barra=barra, esp=esp,
                  tema={"title": tema[0], "lines": tema[1]}, caso={"title": caso[0], "lines": caso[1]},
                  d=d, perlas=perlas, fuente=fuente, tabla=T(*tabla) if tabla else None))


# 1 ── CIR-136 · Neumotórax traumático (diseño 13: COMPARADOR con 2 Rx reales)
V("comparador", "CIR-136", "neumotorax-traumatico-rx-antes-despues-toracostomia",
  "Neumotórax traumático derecho: de la Rx al tubo de tórax",
  "Trauma de tórax · neumotórax y toracostomía con tubo", "CIRUGÍA ENAM: TRAUMA",
  ("Neumotórax en el trauma de tórax",
   ["Aire en la pleura que colapsa el pulmón: murmullo vesicular (MV) abolido y timpanismo del mismo lado.",
    "El tratamiento es el tubo de tórax conectado a sello de agua."]),
  ("Varón de 30 años, accidente de tránsito",
   ["Disnea súbita; FC 100, PA 90/60, FR 26, SatO₂ 91 %.",
    "MV abolido y timpanismo en el hemitórax derecho."]),
  dict(rotulo="Cómo se ve y qué cambia el tubo (Rx reales de referencia)", IH=400, tag="ESTE CASO",
       imgs=[dict(titulo="Antes: neumotórax derecho", archivo="rx_neumotorax_grande.jpg", on=True,
                  marcas=[("flecha", 0.105, 0.60, 0.22, 0.86, "Borde del pulmón\ncolapsado"),
                          ("flecha", 0.22, 0.30, 0.30, 0.08, "Aire negro sin trama pulmonar")],
                  pie="El lado derecho del paciente (izquierda de la imagen) está negro y sin trama: el pulmón "
                      "quedó colapsado hacia el hilio. Por eso el MV está abolido y hay timpanismo.",
                  credito="Rx: James Heilman, MD · Wikimedia Commons · CC BY 3.0 · se quitó la flecha original"),
             dict(titulo="Después: tubo de tórax", archivo="rx_tras_drenaje.jpg",
                  marcas=[("flecha", 0.12, 0.635, 0.36, 0.80, "Tubo de drenaje\n(pigtail)"),
                          ("flecha", 0.14, 0.44, 0.42, 0.14, "Pulmón reexpandido:\nla trama llega a la pared")],
                  pie="Con el tubo a sello de agua el aire sale y el pulmón vuelve a llegar a la pared torácica "
                      "(otro paciente, neumotórax derecho tratado).",
                  credito="Rx: Bonilla A, et al. · Wikimedia Commons · CC BY 4.0 · recorte")],
       lectura_titulo="Qué hacer en la emergencia",
       lectura=[("Diagnóstico clínico", ["Trauma + disnea + MV abolido + timpanismo = neumotórax.",
                                         "Si hay inestabilidad no se espera la Rx."], False),
                ("Tubo de tórax", ["5.º espacio intercostal, entre línea axilar anterior y media, por encima del "
                                   "borde superior de la costilla; conectado a sello de agua."], True),
                ("Si hay signos de tensión", ["Shock, ingurgitación yugular, tráquea desviada: descompresión "
                                              "inmediata con aguja (5.º espacio, línea axilar media) y luego tubo."], False)]),
  ["MV abolido + timpanismo tras un trauma = neumotórax; si además hay shock, pensar en tensión y descomprimir sin esperar la Rx.",
   "El tubo entra por el borde superior de la costilla: por el borde inferior corre el paquete vasculonervioso.",
   "Toracotomía solo si el tubo drena más de 1500 mL de sangre al inicio o más de 200 mL/h por 2-4 horas."],
  "ATLS 11.ª ed. (2025); Schwartz Principios de Cirugía 11.ª ed. Imágenes: Wikimedia Commons (licencia en cada imagen).",
  ("Opciones de la pregunta",
   [("Toracotomía", False), ("Intubación", False), ("Pericardiocentesis", False), ("Tubo de tórax", True)],
   [("Cuándo se indica", ["Drenaje inicial > 1500 mL o > 200 mL/h por 2-4 h", "Vía aérea en riesgo; con neumotórax, después del tubo",
                          "Taponamiento cardiaco (tríada de Beck)", "Neumotórax o hemotórax"]),
    ("¿En este caso?", ["No: todavía no se ha drenado nada", "No como primer paso: la presión positiva agrava el neumotórax",
                        "No: el problema es pleural", "Sí"])]))

# 2 ── CAR-079 · TSV inestable (diseño 14: ESCALERA + ECG real)
V("escalera", "CAR-079", "taquicardia-supraventricular-inestable-ecg-escalera-cardioversion",
  "TSV con inestabilidad: salto directo a la cardioversión sincronizada",
  "Taquicardias de QRS estrecho · manejo según estabilidad", "CARDIOLOGÍA ENAM",
  ("Taquicardia supraventricular paroxística (TSV)",
   ["Taquicardia regular de QRS estrecho, de 150 a 250 lpm, por reentrada.",
    "Antes de elegir el tratamiento se decide si el paciente está estable o inestable."]),
  ("Varón de 56 años con palpitaciones y mareo",
   ["FC 180 x', PA 80/50 mmHg, Glasgow 13.", "ECG: taquicardia regular de QRS estrecho."]),
  dict(rotulo="El trazo y la escalera de tratamiento",
       img=dict(titulo="ECG real en DII: TSV a 179 lpm", archivo="ecg_tsv_d2.jpg", IH=223,
                marcas=[("corchete", 0.2883, 0.3298, 0.66, "RR iguales en todo el trazo: regular", True, 0.12),
                        ("flecha", 0.4535, 0.36, 0.47, 0.90, "QRS estrecho (< 0,12 s)"),
                        ("flecha", 0.478, 0.45, 0.70, 0.90, "No se ven ondas P"),
                        ("caja", 0.512, 0.012, 0.596, 0.085, "FC ≈ 180 lpm", 0.44, 0.05)],
                pie="Todos los RR son iguales, el QRS es angosto y no hay ondas P antes de cada QRS "
                    "(quedan escondidas en la onda T): taquicardia supraventricular por reentrada.",
                credito="Trazo: Displaced y James Heilman, MD · Wikimedia Commons · dominio público"),
       check_titulo="¿Está inestable?",
       check=[("PA 80/50 mmHg: hipotensión", True), ("Glasgow 13: alteración de la conciencia", True),
              ("Otros signos: dolor torácico, edema pulmonar, síncope", False)],
       veredicto="INESTABLE: cardioversión ya",
       peldanos=[("Maniobras vagales", ["Valsalva modificada o masaje carotídeo si no hay soplo."]),
                 ("Adenosina EV", ["6 mg en bolo rápido con lavado; si no cede, 12 mg."]),
                 ("Verapamilo, diltiazem o betabloqueador", ["Si la adenosina falla o está contraindicada."]),
                 ("Cardioversión sincronizada", ["Con sedación, 50-100 J; se sube la energía si no revierte."])],
       ans=3, tag="ESTE CASO",
       leyenda_estable="Estable: se sube un peldaño solo si el anterior no revierte la taquicardia.",
       leyenda_inestable="Inestable (este caso): salto directo al último peldaño, sin esperar fármacos."),
  ["Taquicardia con hipotensión, alteración de conciencia, dolor torácico o edema pulmonar = inestable: cardioversión eléctrica sincronizada inmediata.",
   "Sincronizada para no descargar sobre la onda T (evita la fibrilación ventricular); con sedación si está consciente.",
   "Estable: maniobras vagales → adenosina 6 mg → 12 mg → verapamilo, diltiazem o betabloqueador."],
  "Guías AHA de soporte vital cardiovascular avanzado 2020 (actualización 2023); guía ESC de TSV 2019. Trazo: Wikimedia Commons (dominio público).",
  ("Opciones de la pregunta",
   [("Adenosina EV", False), ("Vagal + lidocaína", False), ("Amiodarona 300 mg", False), ("Cardioversión sincronizada", True)],
   [("Cuándo se usa", ["TSV estable, tras maniobras vagales", "Vagales: TSV estable; la lidocaína no sirve en QRS estrecho",
                       "300 mg es la dosis del paro; en QRS ancho estable se usan 150 mg", "Toda taquicardia inestable con pulso"]),
    ("¿En este caso?", ["No: retrasa la cardioversión", "No", "No", "Sí"])]))

# 3 ── PED-247 · Sarampión (diseño 19: MAPA CORPORAL + fotos reales CDC)
V("mapa_signos", "PED-247", "sarampion-mapa-corporal-exantema-cefalocaudal-koplik",
  "Sarampión: los signos en orden y dónde aparecen",
  "Enfermedades exantemáticas de la infancia · sarampión", "PEDIATRÍA ENAM",
  ("Sarampión",
   ["Virus muy contagioso: en no vacunados da fiebre alta, las «3 C» (tos, coriza y conjuntivitis) y luego exantema.",
    "En el Perú es de notificación obligatoria inmediata."]),
  ("Niño de 1 año 5 meses que llegó de Italia",
   ["Sin vacunas. 4 días de fiebre de 39 °C, rinorrea, conjuntivitis y tos.",
    "Hoy exantema maculopapular que empezó en la cara y bajó."]),
  dict(rotulo="Mapa del cuerpo: qué signo aparece y dónde", PH=500, tag="ESTE CASO",
       ilu_titulo="El niño del caso", ilu=lambda s, x, y: ilu_nino_sarampion(s, x, y),
       ilu_pie="Más rojo donde empezó (cara y detrás de las orejas), más tenue donde llega al final (piernas).",
       signos=[dict(tit="Pródromo: fiebre alta, tos y coriza",
                    lines=["3-4 días de fiebre de 39 °C o más con catarro intenso, antes del exantema."]),
               dict(tit="Conjuntivitis", lines=["Ojos rojos, lagrimeo y fotofobia: es la tercera «C»."]),
               dict(tit="Manchas de Koplik (patognomónicas)",
                    lines=["Puntos blanquecinos como granos de sal sobre la mucosa de la mejilla enrojecida, frente a los molares.",
                           "Salen 1-2 días antes del exantema."],
                    foto=dict(archivo="koplik.jpg", ratio=204 / 280,
                              marcas=[("circulo", 0.555, 0.64, 0.17, "Koplik", 0.30, 0.10)],
                              credito="Foto: CDC (PHIL 6111) · dominio público")),
               dict(tit="Exantema maculopapular cefalocaudal", on=True,
                    lines=["Empieza en la línea del cabello y detrás de las orejas; en 3 días baja al tronco y las extremidades y confluye.",
                           "Luego se aclara en el mismo orden y deja descamación fina."],
                    foto=dict(archivo="sarampion_exantema.jpg", ratio=485 / 700,
                              marcas=[("flecha", 0.47, 0.24, 0.50, 0.88, "Máculas y pápulas que confluyen")],
                              credito="Foto: CDC (PHIL 4497) · dominio público"))]),
  ["Fiebre alta + tos + coriza + conjuntivitis en un niño no vacunado, y luego exantema que baja de la cara a los pies = sarampión.",
   "Koplik es patognomónico, pero sale antes del exantema y dura poco: si no se ve, no descarta.",
   "Caso sospechoso: notificación inmediata, aislamiento respiratorio y vitamina A; se confirma con IgM o PCR."],
  "Nelson Tratado de Pediatría 22.ª ed.; MINSA-CDC Perú, vigilancia de sarampión y rubeola. Fotos: CDC Public Health Image Library (dominio público).",
  ("Diferencial de los exantemas de la pregunta",
   [("Sarampión", True), ("Rubeola", False), ("Exantema súbito", False), ("Escarlatina", False)],
   [("Pródromo", ["Fiebre alta con tos, coriza y conjuntivitis", "Leve; ganglios retroauriculares y occipitales",
                  "Fiebre alta 3-5 días, sin catarro", "Faringitis con exudado"]),
    ("Exantema", ["Maculopapular, cefalocaudal, confluye", "Rosado, cefalocaudal, no confluye; dura 3 días",
                  "Sale al caer la fiebre; empieza en el tronco", "Áspero «en lija», con palidez alrededor de la boca"]),
    ("Edad típica", ["Cualquiera, si no está vacunado", "Escolares y adultos jóvenes", "6 a 24 meses", "3 a 15 años"])]))

# 4 ── TRA-057 · Displasia de cadera (diseño 20: ÁRBOL CON IMAGEN + esquema de Rx dibujado)
V("arbol_imagen", "TRA-057", "displasia-cadera-lactante-9-meses-rx-pelvis-hilgenreiner-perkins",
  "Displasia de cadera a los 9 meses: la Rx de pelvis y cómo leerla",
  "Ortopedia infantil · displasia del desarrollo de la cadera (DDC)", "TRAUMATOLOGÍA ENAM",
  ("Displasia del desarrollo de la cadera",
   ["Cadera inestable o luxada desde el nacimiento; riesgo: parto podálico, sexo femenino, primogénito, familiar con DDC.",
    "El examen depende de la edad: ecografía antes de que osifique la cabeza femoral, Rx después."]),
  ("Lactante de 9 meses, parto podálico",
   ["Arrastra la pierna izquierda al gatear.", "Abducción limitada y miembro inferior izquierdo más corto."]),
  dict(rotulo="Qué examen pedir según la edad", tag="ESTE CASO",
       pregunta="¿Ya se osificó el núcleo de la cabeza femoral? (aparece hacia los 4-6 meses)",
       ramas=[("NO: < 4-6 meses", "Ecografía de caderas (Graf)",
               ["El núcleo aún es cartílago y no se ve en la Rx.", "Se mide el ángulo alfa: normal 60° o más.",
                "Se acompaña de Ortolani y Barlow."]),
              ("SÍ: 9 meses", "Rx AP de pelvis y caderas",
               ["Con el núcleo ya osificado, la Rx muestra dónde está la cabeza femoral respecto del acetábulo."])],
       ilu=lambda s, x, y: ilu_rx_ddc(s, x, y), IW=560, IH=300,
       ilu_pie="Esquema dibujado de la Rx. Cadera izquierda (derecha de la imagen): núcleo pequeño arriba y afuera, "
               "techo acetabular empinado (índice acetabular aumentado) y línea de Shenton rota.",
       luego_titulo="Después del diagnóstico: tratamiento según la edad",
       luego=[("Menos de 6 meses", ["Arnés de Pavlik si la cadera se reduce."], False),
              ("6 a 18 meses", ["Reducción cerrada bajo anestesia (abierta si no se logra) y yeso en espica."], True),
              ("Más de 18 meses", ["Reducción abierta, a menudo con osteotomía de pelvis o fémur."], False)]),
  ["Menor de 4-6 meses: ecografía de caderas; mayor de 4-6 meses: Rx AP de pelvis.",
   "Normal: el núcleo femoral está en el cuadrante inferointerno (bajo Hilgenreiner y medial a Perkins); en la DDC sube y se va afuera.",
   "Índice acetabular mayor de 30° al año y línea de Shenton rota apoyan displasia o luxación."],
  "Tachdjian Ortopedia Pediátrica 6.ª ed.; guía AAOS de displasia del desarrollo de la cadera.",
  ("Opciones de la pregunta",
   [("Rx de pelvis", True), ("Arnés de Pavlik", False), ("Ecografía de caderas", False), ("Observar 3 meses", False)],
   [("Cuándo sirve", ["Desde los 4-6 meses, con núcleo osificado", "Menores de 6 meses con cadera reducible",
                      "Menores de 4-6 meses", "Nunca con un examen anormal"]),
    ("¿En este caso?", ["Sí", "No: tiene 9 meses y aún no hay diagnóstico", "No: el núcleo ya se osificó",
                        "No: retrasa el tratamiento"])]))

if __name__ == "__main__":
    out = "out27demo/flujogramas"
    os.makedirs(out, exist_ok=True)
    for f in F:
        open(f"{out}/{f['archivo']}.svg", "w").write(build6(f))
        print(f["id"], f["archivo"], os.path.getsize(f"{out}/{f['archivo']}.svg") // 1024, "KB")
