# -*- coding: utf-8 -*-
"""Residentado Médico · 4 ejemplos con diseños nuevos: capas, venn, carriles, farmaco."""
from c_rm import S, P, PX, B, Q, L, TR, ATLS, HARRISON, WILLIAMS, NELSON, MINSA, ACOG, AAP
SCHW = "Schwartz Principios de Cirugía 11.ª ed."

# 1 · CAPAS · quemadura de segundo grado profundo
S("capas", "RM-CIR-058", "La quemadura que llega a la dermis reticular es de segundo grado profundo",
  "Quemaduras · profundidad por capas",
  ("Profundidad de la quemadura", ["Se clasifica por la capa más profunda lesionada: epidermis, dermis papilar, dermis reticular, grasa o plano profundo.",
                                   "Define el dolor, el color, el tiempo de curación y si hace falta injerto."]),
  ("Quemadura hasta la zona profunda de la dermis", ["Compromete epidermis y toda la dermis hasta su capa reticular.", "¿Cómo se clasifica?"]),
  ["Segundo grado superficial: dermis papilar; ampollas, base rosada, muy dolorosa, cura en 2-3 semanas sin cicatriz.",
   "Segundo grado profundo: dermis reticular; base blanquecina o moteada, poco dolorosa, cura en más de 3 semanas con cicatriz y suele necesitar injerto.",
   "Tercer grado: espesor total, acartonada e indolora. Cuarto grado: fascia, músculo o hueso. Reevaluar la profundidad a las 48-72 horas."],
  "ABA, Burn Care Guidelines; ISBI, Practice Guidelines for Burn Care (2016, 2018); " + SCHW + "; Walsh et al., Cureus 2026 (PMC13675068).",
  op=("¿Qué grado?", ["No: queda en la dermis papilar, con ampollas y sin cicatriz", "Sí: llega a la dermis reticular, cura en más de 3 semanas", "No: solo epidermis, eritema sin ampollas",
                      "No: espesor total, indolora y acartonada", "No: compromete fascia, músculo o hueso"], {}),
  d=dict(rotulo="Cada capa de la piel y el grado que se alcanza al llegar a ella", prof=2, tag="HASTA AQUÍ",
         lateral_titulo="Si la lesión llega hasta esta capa",
         capas=[("Epidermis", "0,05-0,1 mm", "#fbd5c4", "Primer grado", "Eritema doloroso, sin ampollas (quemadura solar)."),
                ("Dermis papilar", "Superficial", "#f5b8a2", "Segundo grado superficial", "Ampollas, base rosada y húmeda, muy dolorosa; cura sin cicatriz."),
                ("Dermis reticular", "Profunda", "#e89c84", "Segundo grado profundo", "Base blanquecina o moteada, poco dolorosa; cicatriz hipertrófica, injerto."),
                ("Hipodermis (grasa)", "Espesor total", "#fbe38e", "Tercer grado", "Escara acartonada, indolora, no blanquea; escarectomía e injerto."),
                ("Fascia, músculo, hueso", "Plano profundo", "#d4b896", "Cuarto grado", "Pérdida de tejido profundo; cirugía mayor, riesgo de amputación.")],
         veredicto=("Epidermis + toda la dermis = segundo grado profundo", "Cicatriza lento (más de 3 semanas) y deja cicatriz: se plantea injerto temprano.")),
  banda=B("Así se ve una quemadura dérmica", PX("quemadura_dia0.jpg", 230),
          [("Lecho rosado y blanquecino", "Zona desbridada: dermis expuesta de espesor intermedio."), ("Restos de ampollas en el contorno", "Indican compromiso al menos de la dermis papilar."),
           ("Evolución", "La profundidad cambia en 48-72 h: se reevalúa antes de decidir injerto.")], pie="Pierna con quemadura dérmica, día 0"))

# 2 · VENN · colangitis aguda (triada de Charcot)
S("venn", "RM-CIR-114", "En la colangitis aguda coinciden dolor, fiebre e ictericia; la CPRE confirma y drena",
  "Vía biliar · síndromes que se superponen",
  ("Colangitis aguda", ["Infección de la vía biliar obstruida: triada de Charcot (dolor, fiebre, ictericia).", "Con hipotensión y confusión: pentada de Reynolds."]),
  ("Pregunta de teoría", ["¿Qué examen confirma y trata a la vez la colangitis aguda?"]),
  ["Criterios de Tokio 2018: inflamación sistémica (fiebre, PCR) + colestasis (ictericia, pruebas hepáticas) + imagen de dilatación o causa de obstrucción.",
   "Grado I leve: antibióticos y drenaje en 24-48 h. Grado II: drenaje en 24 h. Grado III (disfunción orgánica): drenaje urgente y soporte en UCI.",
   "La CPRE permite drenar y extraer cálculos; si falla, drenaje percutáneo transhepático o cirugía."],
  "Guías de Tokio 2018 (TG18); ESGE, CPRE y colangitis (2021); ASGE, coledocolitiasis (2019).",
  op=("¿Examen de elección?", ["No: no visualiza la vía biliar", "No: orienta (dilatación) pero no trata", "Sí: confirma y drena en el mismo acto",
                               "No: es la alternativa si la CPRE falla", "No: define la causa pero no drena"], {}),
  d=dict(rotulo="Tres signos, cuatro síndromes: la intersección de los tres es la colangitis", caso="ABC",
         conjuntos=[("Dolor en hipocondrio derecho", "#2563eb"), ("Fiebre con escalofríos", "#dc2626"), ("Ictericia", "#ca8a04")],
         regiones={"A": ["Cólico biliar"], "B": ["Sepsis de otro foco"], "C": ["Hepatitis, hemólisis"], "AB": ["Colecistitis aguda"],
                   "AC": ["Litiasis del colédoco"], "BC": ["Absceso hepático"], "ABC": ["COLANGITIS", "(Charcot)"]},
         lado_titulo="Qué hacer con la intersección",
         lado=[("Los tres signos juntos", ["Triada de Charcot: sospecha colangitis aguda."], True), ("Confirmar y drenar", ["CPRE: diagnóstico y tratamiento a la vez."], True),
               ("Antes de la CPRE", ["Ecografía, hemocultivos y antibióticos de amplio espectro."], False)],
         veredicto=("CPRE = examen de elección en la colangitis aguda", "Visualiza la vía biliar, drena la bilis infectada y extrae el cálculo.")))

# 3 · CARRILES · trauma abdominal hipotenso con líquido libre
S("carriles", "RM-CIR-109", "Trauma abdominal con hipotensión y líquido libre: la ruta termina en laparotomía exploradora",
  "Trauma · ruta por servicios",
  ("Hemoperitoneo con inestabilidad", ["Trauma cerrado, hipotensión, hematocrito de 15 % y 500 mL de líquido libre en la ecografía.", "Cada servicio tiene su tarea; no se retrasa el quirófano."]),
  ("Pregunta de conducta", ["¿Qué medida se debe seguir?"]),
  ["Inestable + líquido libre = laparotomía exploradora; la tomografía es para el paciente estable.",
   "Reanimación de control de daños: hemoderivados 1:1:1, pocos cristaloides, hipotensión permisiva y ácido tranexámico en la primera hora.",
   "Evitar la tríada letal: hipotermia, acidosis y coagulopatía."],
  "WSES, trauma abdominal cerrado (2017); Guía europea de sangrado y coagulopatía en trauma (2023); ATLS, 11.ª ed. (2025).",
  op=("¿Conducta?", ["No: es inestable, no se observa", "No: requiere traslado y retrasa el control del sangrado", "No: la ecografía ya mostró el líquido",
                     "Sí: control quirúrgico del sangrado", "No: los coloides no controlan el sangrado"], {}),
  d=dict(rotulo="Quién hace qué, en orden", carriles=["Emergencia", "Imagen", "Banco de sangre", "Sala de operaciones"],
         pasos=[(0, "ABCDE y 2 vías gruesas", "Hipotensión permisiva, calentar al paciente", False), (1, "Ecografía FAST", "Líquido libre en Morrison", False),
                (2, "Transfusión masiva", "Hematíes, plasma, plaquetas 1:1:1", False), (3, "Laparotomía exploradora", "Control del sangrado", True)],
         veredicto=("Hemodinámicamente inestable + FAST positivo = quirófano", "No se pasa por tomografía ni lavado peritoneal.")),
  banda=B("Así se ve el líquido libre", PX("fast_morison.jpg", 300), [("Franja negra en el espacio hepatorrenal", "Es sangre libre (anecoica) entre el hígado y el riñón."), ("Flecha", "Marca el líquido en el espacio de Morison."),
                                                                        ("Positiva e inestable", "No se pide más imagen: se opera.")], pie="FAST con líquido libre en Morison"))

# 4 · FÁRMACO · tramadol y convulsiones
S("farmaco", "RM-CIR-094", "El tramadol baja el umbral convulsivo por su acción serotoninérgica y noradrenérgica",
  "Farmacología · ruta del tramadol",
  ("Tramadol", ["Opioide débil, agonista μ que además inhibe la recaptación de serotonina y noradrenalina.", "Se activa en el hígado por CYP2D6."]),
  ("Convulsiones tras un analgésico", ["Posoperatorio de colecistectomía; 2 horas después, crisis tonicoclónicas.", "¿Qué analgésico se relaciona?"]),
  ["Riesgo mayor con dosis altas, insuficiencia renal o hepática, epilepsia o con ISRS, tricíclicos e IMAO (también síndrome serotoninérgico).",
   "Tratamiento: benzodiazepinas y suspender el fármaco; la naloxona no revierte bien las convulsiones.",
   "Los AINE producen gastropatía, sangrado y nefrotoxicidad, pero no convulsiones; el paracetamol, hepatotoxicidad en sobredosis."],
  "PROSPECT, analgesia en colecistectomía laparoscópica (2020); Katzung Farmacología Básica y Clínica 15.ª ed.; OMS, escalera analgésica.",
  op=("¿Analgésico?", ["Sí: baja el umbral convulsivo", "No: AINE con riesgo digestivo y renal", "No: AINE, no produce convulsiones", "No: hepatotoxicidad solo en sobredosis", "No: AINE selectivo con riesgo cardiovascular"], {}),
  d=dict(rotulo="Recorrido del fármaco hasta la convulsión",
         zonas=[("Sangre", "#e0f2fe"), ("Hígado", "#fef3c7"), ("Membrana neuronal", "#dcfce7"), ("Sinapsis", "#fee2e2")],
         pasos=[(0, "Tramadol por vía oral o IV", "Absorción rápida", False), (1, "CYP2D6 → metabolito activo (O-desmetiltramadol)", "Mayor afinidad por el receptor μ", False),
                (2, "Agonista del receptor μ", "Analgesia y depresión respiratoria", False), (3, "Bloquea la recaptación de serotonina y noradrenalina", "Más monoaminas en la sinapsis", True),
                (3, "Menor umbral convulsivo", "Crisis tonicoclónica", True)],
         veredicto=("Opioide + inhibidor de la recaptación = riesgo de convulsión", "Dosis altas o interacciones con antidepresivos lo aumentan.")))
