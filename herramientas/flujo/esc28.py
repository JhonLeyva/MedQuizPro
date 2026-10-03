"""Clasificaciones oficiales que se repiten en varios flujogramas (una sola definición para que sean idénticas)."""


def HTA_EMB(caso, porque, conducta):
    return dict(nombre="Trastornos hipertensivos del embarazo", orden=False,
                que="Clasificación ACOG 2020 / ISSHP 2021: PA ≥ 140/90 en dos tomas separadas por 4 horas.",
                grados=[("Antes de las 20 sem", "Hipertensión crónica", ["Previa al embarazo o antes de las 20 semanas",
                                                                       "Persiste más de 12 semanas posparto"]),
                        ("Desde las 20 sem", "Hipertensión gestacional", ["Sin proteinuria", "Sin daño de órganos",
                                                                         "Laboratorio normal"]),
                        ("Desde las 20 sem", "Preeclampsia", ["Con proteinuria ≥ 300 mg/24 h, o", "con daño de órganos aunque no haya proteinuria",
                                                             "Sin criterios de severidad"]),
                        ("Desde las 20 sem", "Preeclampsia con severidad", ["PA ≥ 160/110", "Plaquetas < 100 000", "Transaminasas ≥ 2 veces lo normal",
                                                                           "Creatinina > 1,1 mg/dL", "Edema pulmonar, cefalea o visión alterada"]),
                        ("Complicaciones", "Eclampsia y HELLP", ["Eclampsia: convulsión", "HELLP: hemólisis (DHL ≥ 600), transaminasas altas y plaquetas < 100 000"])],
                caso=caso, porque=porque, conducta=conducta)


def ITU(caso, porque, conducta):
    """Clasificación clínica de la infección urinaria (EAU 2024)."""
    return dict(nombre="Clasificación de la infección urinaria", orden=True,
                que="Guía EAU 2024: separa la infección baja, la alta y la complicada para elegir dónde y cómo tratar.",
                grados=[("Sin síntomas", "Bacteriuria asintomática", ["Urocultivo positivo sin síntomas", "Tratar solo en gestantes y antes de cirugía urológica"]),
                        ("ITU baja", "Cistitis", ["Disuria, polaquiuria, urgencia", "Sin fiebre ni dolor lumbar"]),
                        ("ITU alta", "Pielonefritis", ["Fiebre, escalofríos", "Dolor lumbar, puño percusión (+)", "Náuseas y vómitos"]),
                        ("Grave", "Urosepsis", ["Hipotensión o falla de órganos", "Obstrucción o absceso"])],
                caso=caso, porque=porque, conducta=conducta)


def PAGE(caso, porque, conducta):
    """Clasificación de Page del desprendimiento prematuro de placenta."""
    return dict(nombre="Clasificación de Page", que="Gravedad del desprendimiento prematuro de placenta: se mide por la madre, el feto y la coagulación.",
                grados=[("Grado 0", "Asintomático", ["Sin síntomas", "Se descubre al revisar la placenta después del parto"]),
                        ("Grado I", "Leve", ["Sangrado escaso", "Útero con tono normal o poco aumentado", "Feto sin sufrimiento", "Madre estable"]),
                        ("Grado II", "Moderado", ["Dolor continuo y útero hipertónico", "Feto vivo con sufrimiento (FCF alterada)", "Sin choque materno"]),
                        ("Grado III", "Grave", ["Feto muerto", "Choque materno", "IIIa sin coagulopatía · IIIb con coagulopatía"])],
                caso=caso, porque=porque, conducta=conducta)


def GLASGOW_TEC(caso, porque, conducta):
    """Gravedad del traumatismo craneoencefálico según la escala de Glasgow."""
    return dict(nombre="Gravedad del TEC por Glasgow", orden=True, que="Se usa el mejor Glasgow tras reanimar (sin sedación).",
                grados=[("Glasgow 13-15", "Leve", ["TC si hay factores de riesgo", "Observación"]),
                        ("Glasgow 9-12", "Moderado", ["TC siempre", "Hospitalizar, neurocirugía"]),
                        ("Glasgow ≤ 8", "Grave", ["Intubar", "TC y neurocirugía urgente"])],
                caso=caso, porque=porque, conducta=conducta)


def DENGUE(caso, porque, conducta, porque_titulo="Por qué el caso cae aquí"):
    """Clasificación del dengue OPS/OMS con los grupos de manejo del MINSA."""
    return dict(nombre="Clasificación del dengue (OPS/OMS)",
                que="Ordena el dengue por gravedad; el MINSA la usa para decidir dónde tratar (grupos A, B1, B2 y C).",
                grados=[("Grupos A y B1", "Dengue sin signos de alarma",
                         ["Fiebre + 2 de: náuseas, exantema, mialgias, cefalea o dolor retroocular, petequias, leucopenia",
                          "A: en casa · B1: observar si hay comorbilidad o riesgo social"]),
                        ("Grupo B2", "Dengue con signos de alarma",
                         ["Dolor abdominal intenso y continuo", "Vómitos persistentes", "Líquido acumulado o sangrado de mucosas",
                          "Letargia, hepatomegalia o hematocrito que sube"]),
                        ("Grupo C", "Dengue grave",
                         ["Choque o dificultad respiratoria por fuga de plasma", "Sangrado grave", "Daño grave de órganos"])],
                caso=caso, porque=porque, porque_titulo=porque_titulo, conducta=conducta)


def ABORTO(caso, porque, conducta):
    """Formas clínicas del aborto."""
    return dict(nombre="Formas clínicas del aborto", orden=True,
                que="Se definen por el cuello, el sangrado y la ecografía.",
                grados=[("Cuello cerrado", "Amenaza de aborto", ["Sangrado escaso", "Embrión vivo"]),
                        ("Cuello abierto", "Inevitable o en curso", ["Sangrado y dolor", "Membranas rotas o restos en el cuello"]),
                        ("Cuello abierto", "Incompleto", ["Salieron parte de los restos", "Sangrado persistente"]),
                        ("Cuello cerrado", "Completo", ["Útero vacío", "Sangrado que cede"]),
                        ("Cuello cerrado", "Retenido (frustro)", ["Embrión sin latido o saco vacío", "Sin expulsión"])],
                caso=caso, porque=porque, conducta=conducta)


def HIPERK(caso, porque, conducta):
    """Gravedad de la hiperpotasemia (UK Kidney Association 2023)."""
    return dict(nombre="Gravedad de la hiperpotasemia", que="UK Kidney Association 2023: por el nivel de K⁺ y por los cambios en el ECG.",
                grados=[("K⁺ 5,5-5,9", "Leve", ["Sin cambios en el ECG", "Corregir la causa"]),
                        ("K⁺ 6,0-6,4", "Moderada", ["Insulina + glucosa", "Monitoreo cardiaco"]),
                        ("K⁺ ≥ 6,5 o ECG alterado", "Grave", ["Gluconato de calcio EV ya", "Insulina + glucosa, salbutamol", "Valorar diálisis"])],
                caso=caso, porque=porque, conducta=conducta)
