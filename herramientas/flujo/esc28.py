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
