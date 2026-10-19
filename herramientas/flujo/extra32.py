"""Revisión de la Entrega 3 (pedido del 5-oct-2026): escalas como guía (ESC), signos con nombre propio (TRI)
y fuentes actualizadas a 2026 (FUE). c28.S las aplica sobre la ficha original (ESC/TRI reemplazan si ya había)."""
from c26 import NELSON, ATLS, HARRISON, WILLIAMS, MINSA, SABISTON
from c27 import TR

ESC, TRI, FUE = {}, {}, {}

# ───────────────────────────── bloque 0-99 de la entrega
ESC["CIR-079"] = dict(nombre="Gravedad de la quemadura en el adulto (ABA)", que="Por la superficie quemada (regla de los 9) y la profundidad.", orden=True,
    grados=[("< 10 % SCT", "Menor", ["2.º grado superficial", "Manejo ambulatorio"]),
            ("10-20 % SCT", "Moderada", ["O 3.er grado < 10 %", "Hospitalizar"]),
            ("> 20 % SCT", "Mayor", ["3.er grado > 10 %, cara, manos, periné o inhalación", "Unidad de quemados"])],
    caso=2, porque=[("50 % de 2.º y 3.er grado", True), ("> 20 %: aparece el estado hipermetabólico", True)],
    conducta="Unidad de quemados: reanimación, nutrición enteral precoz y control del catabolismo.")
FUE["CIR-079"] = "ABA, reanimación del choque por quemaduras (2024); ISBI, guías de cuidado del quemado (2018); " + SABISTON + "."

ESC["PSI-028"] = dict(nombre="Gravedad de la anorexia nerviosa (DSM-5-TR)", que="En adultos se mide con el IMC; en menores de 18 años, con el percentil de IMC para la edad.", orden=True,
    grados=[("IMC ≥ 17", "Leve", []), ("IMC 16-16,99", "Moderada", []), ("IMC 15-15,99", "Grave", []), ("IMC < 15", "Extrema", ["Riesgo vital"])],
    caso=-1, porque=[("No se dan el peso ni la talla", True), ("A los 13 años se usa el percentil de IMC", True)],
    conducta="Medir peso, talla, IMC, signos vitales y electrolitos; hospitalizar si hay inestabilidad.")
FUE["PSI-028"] = "DSM-5-TR (APA, 2022); SAHM, manejo médico de los trastornos restrictivos en adolescentes (2022); WFSBP (2023); NICE (act. 2020)."

ESC["GIN-142"] = dict(nombre="Grado de choque en la hemorragia posparto", que="Se estima la pérdida por la clínica (pulso, presión, conciencia); el índice de choque (FC/PAS) ≥ 1 es alarma.", orden=True,
    grados=[("10-15 % · 500-1000 mL", "Compensado", ["PA normal", "Palpitaciones, mareo"]),
            ("15-30 % · 1000-1500 mL", "Leve", ["FC 100-120", "Palidez y sudor"]),
            ("30-40 % · 1500-2000 mL", "Moderado", ["PAS 70-80, FC 120-140", "Inquieta"]),
            ("> 40 % · > 2000 mL", "Grave", ["PAS < 70, FC > 140", "Letárgica, oliguria"])],
    caso=-1, porque=[("Sangrado activo: los signos vitales no se informan", True), ("Clasificar para reponer volumen", True)],
    conducta="Activar la clave roja, dos vías, cristaloides y uterotónicos mientras se revisa la cavidad.")
FUE["GIN-142"] = "FIGO, hemorragia posparto (2022); OMS, recomendaciones de HPP (2023; act. 2025); " + MINSA + ", guía de emergencias obstétricas (clave roja)."

ESC["CIR-085"] = dict(nombre="Clasificación EHS de las hernias de la línea media", que="European Hernia Society: ubicación (M1-M5) y ancho del defecto (W1 < 4 cm, W2 4-10 cm, W3 > 10 cm).", orden=True,
    grados=[("M1", "Subxifoidea", ["Hasta 3 cm bajo el xifoides"]), ("M2", "Epigástrica", ["Del xifoides al ombligo"]),
            ("M3", "Umbilical", ["3 cm alrededor del ombligo"]), ("M4", "Infraumbilical", ["Del ombligo al pubis"]),
            ("M5", "Suprapúbica", ["Hasta 3 cm sobre el pubis"])],
    caso=1, porque=[("Bulto supraumbilical en la línea media", True), ("Reductible: sale de pie", True)],
    conducta="Reparación electiva; malla si el defecto es ≥ 1 cm.")
FUE["CIR-085"] = "European y Americas Hernia Societies, hernias umbilicales y epigástricas (2020; vigente); " + SABISTON + "."

FUE["NRL-040"] = "IHS, ICHD-3 (2018); IHS, recomendaciones globales del tratamiento agudo y preventivo de la migraña (2024); AHS, migraña en emergencias (2025)."

ESC["NEF-065"] = dict(nombre="Puntaje internacional de síntomas prostáticos (IPSS)", que="7 preguntas de 0 a 5 puntos (vaciado y llenado) + calidad de vida.", orden=True,
    grados=[("0-7", "Leves", ["Vigilar y cambiar hábitos"]), ("8-19", "Moderados", ["Alfabloqueador", "+ 5-ARI si próstata > 40 mL"]),
            ("20-35", "Graves", ["Tratamiento combinado", "Cirugía si hay complicaciones"])],
    caso=1, porque=[("Síntomas de llenado y vaciado que lo molestan", True), ("Sin retención ni daño renal", True)],
    conducta="Iniciar alfabloqueador; añadir finasterida o dutasterida por el tamaño de la próstata.")
FUE["NEF-065"] = "EAU, síntomas urinarios masculinos (2025); AUA, HBP (2023; act. 2024)."

ESC["TRA-031"] = dict(nombre="Lesión de nervio periférico (Seddon)", que="Según qué parte del nervio se rompe; decide si esperar o explorar.", orden=True,
    grados=[("Neuropraxia", "Bloqueo de la conducción", ["Axón intacto", "Recupera en semanas"]),
            ("Axonotmesis", "Axón roto, vaina intacta", ["Degeneración walleriana", "Recupera ~1 mm/día"]),
            ("Neurotmesis", "Nervio seccionado", ["No recupera solo", "Cirugía"])],
    caso=0, porque=[("Fractura cerrada con parálisis desde el inicio", True), ("Es lo más frecuente en el húmero", True)],
    conducta="Ortesis de muñeca y observar 3-4 meses; electromiografía si no mejora.")

ESC["REU-043"] = dict(nombre="Gravedad de la reacción alérgica (Brown; WAO 2020)", que="Por los órganos comprometidos.", orden=True,
    grados=[("Leve", "Piel y mucosas", ["Urticaria, angioedema"]), ("Moderada", "Respiratoria, digestiva o CV leve", ["Disnea, sibilancias, vómitos", "Mareo, opresión"]),
            ("Grave", "Hipoxia, hipotensión o neurológica", ["Cianosis, SatO₂ ≤ 92 %", "PAS < 90, confusión, colapso"])],
    caso=2, porque=[("PA 80/50 y cianosis", True), ("Estridor y sibilancias", True)],
    conducta="Adrenalina IM ya; repetir cada 5-15 min; volumen y oxígeno.")
FUE["REU-043"] = "WAO, anafilaxia (2020); GA²LEN, definición y manejo de la anafilaxia (2024); EAACI (2021); AHA/ILCOR, guías de reanimación 2025."

ESC["CAR-053"] = dict(nombre="Riesgo cardiovascular y meta de LDL (ESC/EAS)", que="Cuanto más riesgo, más baja la meta de colesterol LDL.", orden=True,
    grados=[("Bajo", "Sin factores importantes", ["LDL < 116 mg/dL"]), ("Moderado", "Jóvenes con DM corta, riesgo intermedio", ["LDL < 100"]),
            ("Alto", "DM sin daño de órgano, ERC moderada", ["LDL < 70 y ↓ ≥ 50 %"]),
            ("Muy alto", "Enfermedad CV establecida o DM con daño de órgano", ["LDL < 55 y ↓ ≥ 50 %"])],
    caso=3, porque=[("Enfermedad coronaria", True), ("Además, diabético", True)],
    conducta="Estatina de alta intensidad; si no llega a la meta, ezetimiba y luego iPCSK9.")
FUE["CAR-053"] = "ESC/EAS, dislipidemias (2019; actualización focalizada 2025); ACC/AHA, dislipidemias (2026); ADA Standards of Care in Diabetes 2026."
FUE["END-044"] = "ESC/EAS, dislipidemias (2019; actualización focalizada 2025); ACC/AHA, dislipidemias (2026)."

ESC["GIN-143"] = dict(nombre="Clasificación del trazado intraparto (FIGO 2015)", que="Línea de base, variabilidad y desaceleraciones.", orden=True,
    grados=[("Normal", "Sin hipoxia", ["FCF 110-160, variabilidad 5-25", "Sin desaceleraciones repetidas"]),
            ("Sospechoso", "Falta 1 rasgo normal", ["Corregir causas reversibles", "Vigilar"]),
            ("Patológico", "Hipoxia probable", ["Bradicardia prolongada o taquisistolia", "Actuar de inmediato"])],
    caso=2, porque=[("Taquicardia y luego bradicardia tras el bolo", True), ("Hipertonía uterina", True)],
    conducta="Suspender oxitocina, decúbito lateral, tocolítico agudo; si no se recupera, parto inmediato.")
FUE["GIN-143"] = "ACOG, guía clínica n.º 10: monitoreo de la FCF intraparto (2025); FIGO, CTG intraparto (2015); Williams Obstetricia 26.ª ed. (2022)."

ESC["HEM-028"] = dict(nombre="Tipos de enfermedad de von Willebrand (ISTH)", que="Por la cantidad y la función del factor de von Willebrand.", orden=True,
    grados=[("Tipo 1", "Falta parcial (≈ 75 %)", ["FvW bajo con función conservada", "Desmopresina"]),
            ("Tipo 2", "Factor que no funciona", ["2A, 2B, 2M, 2N", "Actividad/antígeno < 0,7"]),
            ("Tipo 3", "Falta total", ["FVIII muy bajo", "Concentrado de FvW"])],
    caso=0, porque=[("Sangrado mucocutáneo familiar (autosómico dominante)", True), ("El subtipo exacto lo dan los multímeros", True)],
    conducta="Confirmar con antígeno y actividad del FvW; desmopresina para sangrados menores.")

FUE["OFT-033"] = "AAO, PPP de enfermedad por cierre angular primario (2020; vigente); European Glaucoma Society, guías 6.ª ed. (2025)."

# ───────────────────────────── bloque 100-199
from esc28 import GLASGOW_TEC

ATLS_CLASES = lambda caso, porque, conducta: dict(
    nombre="Clases de hemorragia (ATLS 11.ª)", que="Pérdida estimada de sangre en un adulto de 70 kg.", orden=True,
    grados=[("I · < 15 %", "Compensada", ["FC y PA normales"]), ("II · 15-30 %", "Leve", ["FC ↑, presión de pulso ↓", "Ansioso"]),
            ("III · 31-40 %", "Moderada", ["PAS ↓, FC > 120", "Confuso, oliguria"]), ("IV · > 40 %", "Grave", ["PAS muy baja", "Letárgico, sin diuresis"])],
    caso=caso, porque=porque, conducta=conducta)
QUEMADO = lambda caso, porque, conducta: dict(
    nombre="Gravedad de la quemadura en el adulto (ABA)", que="Por la superficie quemada de 2.º y 3.er grado y las zonas especiales.", orden=True,
    grados=[("< 10 % SCT", "Menor", ["2.º grado superficial", "Ambulatorio"]), ("10-20 % SCT", "Moderada", ["O 3.er grado < 10 %", "Hospitalizar"]),
            ("> 20 % SCT", "Mayor", ["3.er grado > 10 %, cara, manos, periné o inhalación", "Unidad de quemados; Parkland"])],
    caso=caso, porque=porque, conducta=conducta)
WELLS_TEP = lambda items, total, rango, porque, conducta: dict(
    nombre="Escala de Wells para TEP", modo="puntaje", que="Probabilidad clínica antes de la imagen.", items=items,
    total_txt=total, total_nota="TEP probable si > 4",
    rangos=[("≤ 4", "Improbable", "Dímero D"), ("> 4", "Probable", "Angio-TC")], caso_rango=rango, porque=porque, conducta=conducta)
TEP26 = "AHA/ACC/ACCP y otras, guía de embolia pulmonar aguda (2026); ESC, embolia pulmonar (2019)"

ESC["GIN-150"] = dict(nombre="Ganancia de peso según el IMC previo (IOM)", que="Cuánto debe subir de peso en todo el embarazo (gestación única).", orden=True,
    grados=[("IMC < 18,5", "Bajo peso", ["12,5-18 kg"]), ("IMC 18,5-24,9", "Normal", ["11,5-16 kg"]),
            ("IMC 25-29,9", "Sobrepeso", ["7-11,5 kg"]), ("IMC ≥ 30", "Obesidad", ["5-9 kg"])],
    caso=3, porque=[("Obesidad no corregida antes del embarazo", True)],
    conducta="Tamizar diabetes desde el primer control y limitar la ganancia a 5-9 kg.")
FUE["GIN-150"] = "ACOG, obesidad y embarazo (2021); IOM/NAM, ganancia de peso en el embarazo (2009; vigente); ADA Standards of Care in Diabetes 2026; Williams Obstetricia 26.ª ed. (2022)."

ESC["GIN-151"] = dict(nombre="Categorías de los criterios médicos de elegibilidad (OMS)", que="Cada método se califica según la enfermedad de la mujer.", orden=True,
    grados=[("1", "Sin restricción", ["Usar en cualquier caso"]), ("2", "Beneficio > riesgo", ["En general, usar"]),
            ("3", "Riesgo > beneficio", ["No se recomienda"]), ("4", "Riesgo inaceptable", ["No usar"])],
    caso=0, porque=[("DIU de cobre en LES con antifosfolípidos: categoría 1", True), ("Estrógenos: categoría 4", True)],
    conducta="Ofrecer DIU de cobre (reversible y sin hormonas).")

ESC["NRL-042"] = dict(nombre="Clasificación clínica de la miastenia (MGFA)", que="Por dónde y cuánto hay debilidad.", orden=True,
    grados=[("I", "Ocular", ["Ptosis y diplopía solas"]), ("II", "Generalizada leve", ["IIa extremidades · IIb bulbar"]),
            ("III", "Generalizada moderada", []), ("IV", "Generalizada grave", []), ("V", "Crisis miasténica", ["Intubación"])],
    caso=0, porque=[("Ptosis y visión doble", True), ("Sin debilidad de extremidades descrita", True)],
    conducta="Anti-AChR, piridostigmina y TC de tórax (timo); vigilar si se generaliza.")

ESC["NEF-068"] = dict(nombre="Grupos de grado ISUP (puntaje de Gleason)", que="El patólogo suma los dos patrones más frecuentes (3 a 5); hoy el mínimo informado es 6.", orden=True,
    grados=[("ISUP 1", "Gleason ≤ 6 (3+3)", ["Bien diferenciado", "El menos agresivo"]), ("ISUP 2", "Gleason 7 (3+4)", ["Predomina el patrón 3"]),
            ("ISUP 3", "Gleason 7 (4+3)", ["Predomina el patrón 4"]), ("ISUP 4", "Gleason 8", ["4+4, 3+5, 5+3"]),
            ("ISUP 5", "Gleason 9-10", ["El más agresivo"])],
    caso=0, porque=[("Gleason bajo («< 6» = 6 hoy): ISUP 1", True), ("Pero PSA 11,5 (10-20): sube a riesgo intermedio", True)],
    conducta="Riesgo intermedio favorable con > 10 años de vida: prostatectomía radical o radioterapia.")
FUE["NEF-068"] = "NCCN, cáncer de próstata (versión 3.2026); EAU-EANM-ESTRO-ESUR-ISUP-SIOG (2024; act. 2025); ISUP, consenso de gradación (2019)."

ESC["NRL-043"] = dict(nombre="Puntaje ICH (Hemphill) · hemorragia intracerebral", modo="puntaje", que="Predice la mortalidad a 30 días.",
    items=[("GCS", "Glasgow 3-4 (2) · 5-12 (1)", "Obnubilado: probable 5-12", 1), ("Vol", "Volumen ≥ 30 mL (1)", "No informado", None),
           ("HIV", "Sangre en los ventrículos (1)", "No informado", None), ("Infra", "Infratentorial (1)", "Fosa posterior", 1),
           ("Edad", "≥ 80 años (1)", "65 años", 0)],
    total_txt="Total: ≥ 2 con los datos dados", total_nota="de 0 a 6",
    rangos=[("0-1", "Mortalidad 0-13 %", "Manejo médico estrecho"), ("2-3", "26-72 %", "UCI; cirugía si fosa posterior con deterioro"),
            ("4-6", "97-100 %", "Pronóstico muy malo")], caso_rango=1,
    porque=[("Fosa posterior que comprime el tronco", True), ("Se deteriora: la cirugía no puede esperar", True)],
    conducta="Craniectomía suboccipital y evacuación; drenaje ventricular si hay hidrocefalia.")
FUE["NRL-043"] = "AHA/ASA, hemorragia intracerebral espontánea (2022); ESO, hemorragia intracerebral (2025); Harrison Principios de Medicina Interna 22.ª ed. (2025)."

ESC["NEU-041"] = WELLS_TEP([("TVP", "Signos de TVP (3)", "No descritos", 0), ("Alt", "Otro diagnóstico menos probable (3)", "Sí: Rx normal, no coronario", 3),
                            ("FC", "FC > 100 (1,5)", "No informada", None), ("Inm", "Inmovilización ≥ 3 días o cirugía (1,5)", "Hospitalizado", 1.5),
                            ("Prev", "TEP o TVP previa (1,5)", "No", 0), ("Hem", "Hemoptisis (1)", "No", 0), ("Ca", "Cáncer activo (1)", "No", 0)],
                           "Total: 4,5 puntos", 1, [("Otro diagnóstico menos probable (3) + hospitalizado (1,5)", True)], "Angio-TC de tórax; anticoagular si no hay contraindicación.")
FUE["NEU-041"] = TEP26 + "; ACCP/CHEST (2021)."
ESC["NEU-042"] = WELLS_TEP([("TVP", "Signos de TVP (3)", "No descritos", 0), ("Alt", "Otro diagnóstico menos probable (3)", "Sí", 3),
                            ("FC", "FC > 100 (1,5)", "Diaforesis; FC no dada", None), ("Inm", "Inmovilización ≥ 3 días o cirugía (1,5)", "2 semanas en cama", 1.5),
                            ("Prev", "TEP o TVP previa (1,5)", "No", 0), ("Hem", "Hemoptisis (1)", "No", 0), ("Ca", "Cáncer activo (1)", "No", 0)],
                           "Total: 4,5 puntos", 1, [("Inmovilizada 2 semanas (1,5) + TEP lo más probable (3)", True), ("Probable: angio-TC (el dímero D sobra)", True)],
                           "Angio-TC de tórax; si hay alergia o falla renal, gammagrafía V/Q.")
FUE["NEU-042"] = TEP26 + "; AHA/ILCOR, guías de reanimación 2025."

ESC["NEU-043"] = dict(nombre="Tamaño y gravedad del neumotórax (BTS 2023)", que="Se mide de la pared al borde del pulmón a la altura del hilio.", orden=True,
    grados=[("< 2 cm", "Pequeño", ["Estable: observar u oxígeno"]), ("≥ 2 cm", "Grande", ["O con disnea: aspirar o tubo fino"]),
            ("A tensión", "Mediastino desviado", ["Inestable: descompresión ya", "Luego tubo de tórax"])],
    caso=2, porque=[("Mediastino desviado a la izquierda", True), ("Disnea intensa y súbita", True)],
    conducta="Descompresión con aguja y tubo; videotoracoscopía si recurre.")

ESC["OFT-034"] = dict(nombre="Clasificación internacional del retinoblastoma intraocular (IIRC)", que="Grupos A a E por tamaño y siembra; predice si se salva el ojo.", orden=True,
    grados=[("A", "Tumor ≤ 3 mm", ["Lejos de la fóvea y la papila"]), ("B", "Tumor > 3 mm", ["O líquido subretiniano limitado"]),
            ("C", "Siembra localizada", []), ("D", "Siembra difusa", ["Desprendimiento extenso"]),
            ("E", "Ojo destruido", ["Glaucoma, hemorragia; enucleación"])],
    caso=-1, porque=[("El grupo se define con el fondo de ojo bajo anestesia", True), ("Leucocoria + estrabismo: referir urgente", True)],
    conducta="Fondo de ojo bajo anestesia, ecografía y RM; tratamiento según el grupo.")

ESC["END-048"] = dict(nombre="Estadios de la ERC por filtrado glomerular (KDIGO)", que="TFG en mL/min/1,73 m²; decide qué antidiabético se puede usar.", orden=True,
    grados=[("G1-G2", "≥ 60", ["Metformina dosis completa"]), ("G3a", "45-59", ["Metformina: vigilar"]),
            ("G3b", "30-44", ["Metformina a la mitad"]), ("G4", "15-29", ["Suspender metformina"]), ("G5", "< 15", ["Insulina ajustada"])],
    caso=2, porque=[("Creatinina 2,3 en varón de 57 años: TFG ≈ 31-32", True), ("Glucosa 450 y HbA1c 9,5 %: necesita insulina", True)],
    conducta="Insulina basal; metformina a la mitad o suspender según la TFG exacta.")

ESC["REU-050"] = dict(nombre="Gravedad de la psoriasis", que="Por la superficie corporal afectada (BSA) y el PASI; la eritrodermia es la forma más grave.", orden=True,
    grados=[("BSA < 3 %", "Leve", ["Tópicos: corticoide + calcipotriol"]), ("BSA 3-10 %", "Moderada", ["Fototerapia o sistémicos"]),
            ("BSA > 10 % o eritrodermia", "Grave", ["Sistémicos o biológicos", "Eritrodermia: hospitalizar"])],
    caso=2, porque=[("Eritrodermia", True), ("Uñas y cuero cabelludo comprometidos", True)],
    conducta="Hospitalizar; ciclosporina, metotrexato o biológico; nunca corticoide sistémico.")
FUE["REU-050"] = "AAD-NPF, psoriasis (2019-2021); EuroGuiDerm, tratamiento sistémico de la psoriasis (2023); NICE CG153 (act. 2017)."

ESC["CIR-092"] = QUEMADO(2, [("36 % de superficie quemada", True), ("Escaldadura en brazos y tronco", True)],
                         "Parkland (4 mL × kg × % SCQ) y traslado a unidad de quemados.")
FUE["CIR-092"] = "ABA, reanimación del choque por quemaduras (2024); ATLS 11.ª ed. (2025)."

ESC["GAS-057"] = ATLS_CLASES(2, [("PA 80/40 y FC 118: índice de choque 1,5", True), ("Ansiosa tras hematemesis abundante", True)],
                             "Dos vías gruesas, cristaloides y sangre; IBP EV y endoscopía urgente.")

ESC["OFT-037"] = dict(nombre="Grados del hifema", que="Por cuánto ocupa la sangre la cámara anterior.", orden=True,
    grados=[("Micro", "Solo células", ["Se ve con lámpara de hendidura"]), ("I", "< 1/3", []), ("II", "1/3 a 1/2", []),
            ("III", "> 1/2", []), ("IV", "Total («bola 8»)", ["Mayor riesgo de glaucoma"])],
    caso=-1, porque=[("Hifema visible con pupila deformada", True), ("El grado lo mide el oftalmólogo", True)],
    conducta="Escudo rígido, cabecera elevada y referencia urgente.")

ESC["TRA-035"] = GLASGOW_TEC(2, [("En coma al ingreso", True), ("SatO₂ 84 %: hipoxia que daña más el cerebro", True)],
                             "Oxígeno, collarín e intubación de secuencia rápida; luego TC.")
FUE["TRA-035"] = "ATLS 11.ª ed. (2025); Brain Trauma Foundation (4.ª ed., 2016)."
FUE["CIR-095"] = "ATLS 11.ª ed. (2025); EAST, trauma abdominal penetrante (2017)."
FUE["GAS-056"] = "ACG, insuficiencia hepática aguda (2023); AASLD (2011); EASL (2017)."

# ───────────────────────────── bloque 200-299
AIEPI_DESH = lambda caso, porque, conducta: dict(
    nombre="Clasificación de la deshidratación (AIEPI)", que="Dos o más signos de la fila deciden el plan.", orden=True,
    grados=[("Plan A", "Sin deshidratación", ["Alerta, bebe normal"]), ("Plan B", "Algún grado", ["Inquieto, ojos hundidos", "Bebe ávido, pliegue lento"]),
            ("Plan C", "Grave", ["Letárgico, ojos muy hundidos", "No puede beber, pliegue muy lento"])],
    caso=caso, porque=porque, conducta=conducta)
CHOQUE_OBST = lambda caso, porque, conducta: dict(ESC["GIN-142"], caso=caso, porque=porque, conducta=conducta)
FIGO_CTG = lambda caso, porque, conducta: dict(ESC["GIN-143"], caso=caso, porque=porque, conducta=conducta)

ESC["GAS-059"] = dict(nombre="Resecabilidad del cáncer de páncreas (NCCN)", que="La TC con protocolo de páncreas mira las arterias (tronco celíaco, mesentérica superior) y las venas.", orden=True,
    grados=[("Resecable", "Sin contacto vascular", ["Cirugía (Whipple) + quimioterapia"]), ("Limítrofe", "Contacto parcial", ["Quimioterapia primero, luego cirugía"]),
            ("Localmente avanzado", "Arterias rodeadas", ["Quimio ± radioterapia"]), ("Metastásico", "Hígado, peritoneo", ["Quimioterapia paliativa, prótesis biliar"])],
    caso=-1, porque=[("Masa de 7 cm, ictericia y baja de peso", True), ("La TC define el grupo", True)],
    conducta="TC con protocolo de páncreas antes de decidir cirugía.")

ESC["TRA-036"] = GLASGOW_TEC(1, [("Glasgow 10", True), ("No obliga a intubar (≤ 8 sí), pero hay que vigilar", True)],
                             "Vía aérea con collarín y oxígeno; TC cerebral al estabilizar.")
FUE["TRA-036"] = "ATLS 11.ª ed. (2025)."
FUE["TRA-039"] = "ATLS 11.ª ed. (2025); Rockwood y Green, Fracturas en el adulto 9.ª ed.; AAOS."

ESC["PSI-032"] = dict(nombre="Gravedad de la bulimia nerviosa (DSM-5-TR)", que="Por el número de conductas compensatorias (purgas) por semana.", orden=True,
    grados=[("1-3 por semana", "Leve", []), ("4-7", "Moderada", []), ("8-13", "Grave", []), ("≥ 14", "Extrema", [])],
    caso=-1, porque=[("Purgas «recurrentes»: falta la frecuencia", True), ("El peso normal la separa de la anorexia", True)],
    conducta="Terapia cognitivo-conductual y fluoxetina; buscar hipopotasemia.")

ESC["HEM-033"] = dict(nombre="Gravedad de la neutropenia", que="Por el recuento absoluto de neutrófilos (RAN).", orden=True,
    grados=[("1000-1500/µL", "Leve", ["Riesgo bajo"]), ("500-999/µL", "Moderada", ["Riesgo intermedio"]),
            ("< 500/µL", "Grave", ["Riesgo alto de sepsis"]), ("< 100/µL", "Profunda (agranulocitosis)", ["Fiebre = urgencia"])],
    caso=2, porque=[("Pregunta por la neutropenia grave (< 500)", True)],
    conducta="Revisar fármacos y suspender el sospechoso; si hay fiebre, antibiótico EV en la primera hora.")
FUE["HEM-033"] = "Harrison Principios de Medicina Interna 22.ª ed. (2025); IDSA/ASCO, neutropenia febril (2018; act. 2024)."

ESC["NEU-050"] = dict(nombre="Gravedad de la obstrucción en la EPOC (GOLD 2025)", que="Con VEF1/CVF < 0,7 tras broncodilatador, el VEF1 da el grado.", orden=True,
    grados=[("GOLD 1", "Leve", ["VEF1 ≥ 80 %"]), ("GOLD 2", "Moderada", ["VEF1 50-79 %"]), ("GOLD 3", "Grave", ["VEF1 30-49 %"]), ("GOLD 4", "Muy grave", ["VEF1 < 30 %"])],
    caso=-1, porque=[("No se da la espirometría", True), ("Además se clasifica por síntomas y exacerbaciones (grupos A, B, E)", True)],
    conducta="Espirometría al salir de la exacerbación; broncodilatador de larga acción según el grupo.")
FUE["NEU-050"] = "GOLD 2025 (y 2026); OMS, tabaquismo pasivo (2023)."

ESC["PED-169"] = AIEPI_DESH(1, [("Deshidratación moderada: algún grado", True), ("Además somnoliento y distendido: signos de gravedad", True)],
                            "Hospitalizar: hidratación y ceftriaxona EV.")

ESC["PED-170"] = dict(nombre="Zonas de Kramer (ictericia neonatal)", que="La ictericia avanza de la cabeza a los pies; estima la bilirrubina (no la reemplaza).", orden=True,
    grados=[("Zona 1", "Cabeza y cuello", ["~5-6 mg/dL"]), ("Zona 2", "Hasta el ombligo", ["~9 mg/dL"]), ("Zona 3", "Hasta la ingle y muslos", ["~12 mg/dL"]),
            ("Zona 4", "Brazos y piernas", ["~15 mg/dL"]), ("Zona 5", "Palmas y plantas", ["> 15 mg/dL"])],
    caso=2, porque=[("Ictericia hasta la región inguinal", True), ("En el día 2 con bilirrubina directa alta: no es fisiológica", True)],
    conducta="Medir bilirrubina; hemocultivo y ampicilina + gentamicina por sospecha de sepsis.")

ESC["CIR-097"] = dict(nombre="Probabilidad de cálculo en el colédoco (ASGE 2019)", que="Decide si ir directo a CPRE o estudiar antes con CPRM o ecoendoscopía.", orden=True,
    grados=[("Alta", "Cálculo visto, colangitis o bilirrubina > 4 + colédoco dilatado", ["CPRE"]),
            ("Intermedia", "Pruebas hepáticas alteradas, > 55 años o colédoco dilatado", ["CPRM o ecoendoscopía"]),
            ("Baja", "Sin ninguno", ["Seguir"])],
    caso=1, porque=[("Vía biliar dilatada e ictericia, sin cálculo visto", True), ("Después de colecistectomía: también puede ser estenosis", True)],
    conducta="Colangiorresonancia; CPRE solo si confirma algo que tratar.")

ESC["GIN-165"] = CHOQUE_OBST(-1, [("Choque hipovolémico por hemorragia profusa", True), ("La diuresis ≥ 0,5 mL/kg/h dice que la reanimación funciona", True)],
                             "Medir diuresis por sonda cada hora; sangre temprana y tratar la causa.")

ESC["GIN-168"] = FIGO_CTG(-1, [("Desaceleraciones variables: compresión del cordón", True), ("Repetidas o complicadas: el trazado empeora", True)],
                          "Cambiar de posición, suspender oxitocina, hidratar y descartar prolapso de cordón.")
FUE["GIN-168"] = "ACOG, guía clínica n.º 10: monitoreo de la FCF intraparto (2025); FIGO, monitoreo fetal intraparto (2015)."

ESC["GIN-170"] = dict(nombre="Pequeño para la edad o restricción del crecimiento (consenso Delphi, ISUOG)", que="El peso solo no basta: importa el percentil y el Doppler.", orden=True,
    grados=[("p3-p10 + Doppler normal", "Pequeño para la edad", ["Constitucional; control cada 2 semanas"]),
            ("< p3 o Doppler alterado", "Restricción del crecimiento", ["Vigilancia intensiva"]),
            ("Doppler umbilical ausente o reverso", "Restricción grave", ["Corticoides y terminar según la edad"])],
    caso=0, porque=[("Peso < p10", True), ("Líquido y Doppler umbilical normales", True)],
    conducta="Ecografía y Doppler cada 2 semanas; terminar a las 37-38 semanas si sigue igual.")
FUE["GIN-170"] = "ISUOG, restricción del crecimiento fetal (2020); FIGO (2021); SMFM (2020; act. 2024); ACOG n.º 227 (2021)."

ESC["GIN-178"] = dict(nombre="Estadios del prolapso (POP-Q)", que="Se mide el punto más descendido respecto al himen (en cm).", orden=True,
    grados=[("0", "Sin prolapso", []), ("I", "> 1 cm sobre el himen", []), ("II", "± 1 cm del himen", ["Se ve al pujar"]),
            ("III", "> 1 cm fuera del himen", ["Sin eversión total"]), ("IV", "Eversión total", [])],
    caso=-1, porque=[("Siente un bulto en la vagina (suele ser ≥ II)", True), ("El estadio se mide al examinarla", True)],
    conducta="Sintomático: pesario o colporrafia anterior; descartar incontinencia oculta.")

ESC["INF-086"] = dict(nombre="Estadios de la meningitis tuberculosa (BMRC)", que="Por la conciencia y los signos focales; predicen la mortalidad.", orden=True,
    grados=[("I", "Lúcido, sin focalidad", ["Mejor pronóstico"]), ("II", "Glasgow 11-14 o focalidad", ["Pares craneales, hemiparesia"]),
            ("III", "Glasgow ≤ 10", ["Mortalidad muy alta"])],
    caso=-1, porque=[("Pregunta de teoría: el esquema es el mismo en los tres", True), ("El estadio decide el pronóstico", True)],
    conducta="2HRZE + 10HR y dexametasona; tratar sin esperar el cultivo.")

ESC["NEU-052"] = dict(nombre="Riesgo de muerte precoz en el TEP (ESC)", que="Por la hemodinamia, el PESI simplificado, el VD y la troponina.", orden=True,
    grados=[("Alto", "Choque o PAS < 90", ["Trombólisis"]), ("Intermedio-alto", "VD dilatado + troponina alta", ["Anticoagular y vigilar"]),
            ("Intermedio-bajo", "Solo uno de los dos", ["Anticoagular"]), ("Bajo", "PESIs 0, VD normal", ["Ambulatorio posible"])],
    caso=0, porque=[("TEP masivo con choque", True), ("Muere por falla del VD", True)],
    conducta="Trombólisis sistémica; noradrenalina, sin sobrecargar de líquidos.")
FUE["NEU-052"] = TEP26 + "."

ESC["PSI-036"] = dict(nombre="Gravedad del episodio depresivo (DSM-5-TR)", que="Por el número e intensidad de síntomas; la psicosis se agrega como especificador.", orden=True,
    grados=[("Leve", "Pocos síntomas", ["Funciona con esfuerzo"]), ("Moderado", "Intermedio", []), ("Grave", "Casi todos, incapacitante", []),
            ("Grave con psicosis", "Alucinaciones o delirios", ["Antidepresivo + antipsicótico o TEC"])],
    caso=3, porque=[("Ideas suicidas", True), ("Escucha voces y ve personas", True)],
    conducta="Hospitalizar si el riesgo suicida es alto; antidepresivo + antipsicótico o TEC.")

ESC["NRL-047"] = dict(nombre="Gravedad del ACV (NIHSS)", que="0 a 42 puntos: conciencia, mirada, campos, cara, brazos, piernas, lenguaje, sensibilidad.", orden=True,
    grados=[("0", "Sin déficit", []), ("1-4", "Menor", []), ("5-15", "Moderado", []), ("16-20", "Moderado a grave", []), ("21-42", "Grave", [])],
    caso=-1, porque=[("Afasia + hemiparesia + conciencia alterada: suele ser ≥ 5", True), ("El puntaje no cambia la regla de la PA", True)],
    conducta="Bajar la PA a < 185/110 con labetalol o nicardipino y trombolizar si está en ventana.")
FUE["NRL-047"] = "AHA/ASA, ACV isquémico agudo (2019; act. 2026); ESO, trombólisis (2021) y trombectomía (2023)."

ESC["NEF-074"] = dict(nombre="Gravedad de la hipopotasemia", que="Por el K⁺ sérico y, sobre todo, por el ECG y los síntomas.", orden=True,
    grados=[("3,0-3,4 mEq/L", "Leve", ["Potasio oral"]), ("2,5-2,9", "Moderada", ["Oral o EV"]), ("< 2,5 o ECG alterado", "Grave", ["KCl EV con monitoreo"])],
    caso=-1, porque=[("Debilidad, caídas e hiporreflexia", True), ("Falta el K⁺: por eso primero el ECG", True)],
    conducta="ECG y potasio (y magnesio) de inmediato; reponer según la gravedad.")
FUE["NEF-074"] = "KDIGO, controversias en potasio (2020); Harrison Principios de Medicina Interna 22.ª ed. (2025)."

ESC["TRA-040"] = dict(nombre="Clasificación radiográfica de Tönnis (displasia de cadera)", que="Después de los 4-6 meses se usa la Rx: dónde queda el núcleo de la cabeza femoral respecto a la línea de Perkins.", orden=True,
    grados=[("I", "Núcleo medial a Perkins", ["Cadera en su sitio"]), ("II", "Lateral a Perkins, bajo el borde del acetábulo", []),
            ("III", "A la altura del borde", []), ("IV", "Sobre el borde", ["Luxación alta"])],
    caso=-1, porque=[("11 meses con Galeazzi positivo: hay acortamiento", True), ("La Rx de pelvis dará el grado", True)],
    conducta="Rx de pelvis; reducción cerrada y yeso (6-18 meses).")

ESC["GAS-062"] = dict(nombre="Estadios del cáncer gástrico (TNM, AJCC 8.ª)", que="Por la invasión de la pared (T), los ganglios (N) y las metástasis (M).", orden=True,
    grados=[("I", "Mucosa o submucosa", ["Cirugía (o endoscopía si es muy precoz)"]), ("II", "Más pared o pocos ganglios", ["Cirugía + quimioterapia"]),
            ("III", "Serosa o muchos ganglios", ["Quimioterapia perioperatoria"]), ("IV", "Metástasis a distancia", ["Virchow, ascitis, hígado: paliativo"])],
    caso=3, porque=[("Ganglio de Virchow pétreo", True), ("Ascitis (carcinomatosis)", True)],
    conducta="Endoscopía con biopsia, TC para estadificar y quimioterapia paliativa.")
TRI["NEU-049"] = TR([("Proteína LP/suero > 0,5", "Proteínas 4,9 g/dL: casi seguro", True), ("LDH LP/suero > 0,6", "No informada", None),
                     ("LDH LP > 2/3 del límite normal", "No informada", None)],
                    [("Criterios de Light (uno basta: exudado)", 0, 2)], "Exudado linfocítico con ADA > 40: tuberculosis pleural.", rotulo="Criterios con nombre propio")

# ───────────────────────────── bloque 300-399
KDIGO_LRA = lambda caso, porque, conducta: dict(
    nombre="Estadios KDIGO de lesión renal aguda", que="Por la creatinina o la diuresis (lo que sea peor).", orden=True,
    grados=[("1", "Creatinina × 1,5-1,9 o ↑ ≥ 0,3", ["Diuresis < 0,5 mL/kg/h por 6-12 h"]), ("2", "Creatinina × 2-2,9", ["< 0,5 mL/kg/h por ≥ 12 h"]),
            ("3", "Creatinina × 3, ≥ 4 o diálisis", ["< 0,3 mL/kg/h por ≥ 24 h o anuria ≥ 12 h"])],
    caso=caso, porque=porque, conducta=conducta)

ESC["GIN-184"] = dict(nombre="Placenta previa e inserción baja (ecografía transvaginal)", que="Por la distancia del borde placentario al orificio cervical interno (OCI) en el tercer trimestre.", orden=True,
    grados=[("Cubre el OCI", "Placenta previa", ["Cesárea"]), ("< 20 mm del OCI", "Inserción baja", ["Parto vaginal posible con vigilancia"]),
            ("≥ 20 mm", "Normal", ["Parto vaginal"])],
    caso=1, porque=[("Placenta de inserción baja y sangrado escaso", True), ("7 cm con presentación que tapona el borde", True)],
    conducta="Vía EV, sangre reservada, amniotomía y monitoreo; cesárea si el sangrado aumenta.")

ESC["HEM-035"] = dict(nombre="Puntaje de Qinghai del mal de montaña crónico", que="Síntomas (0-3 cada uno: disnea, sueño, cianosis, venas dilatadas, parestesias, cefalea, acúfenos) + Hb ≥ 21 en varón (3 puntos).", orden=True,
    grados=[("0-5", "Ausente", []), ("6-10", "Leve", []), ("11-14", "Moderado", []), ("≥ 15", "Grave", [])],
    caso=-1, porque=[("Hb 22 en varón: 3 puntos", True), ("Cefalea, acúfenos y cianosis suman más", True), ("Intensidad de cada síntoma no informada", True)],
    conducta="Bajar a menor altura; flebotomía si el Hto es muy alto; acetazolamida.")

ESC["END-053"] = dict(nombre="Clasificación de la obesidad por IMC (OMS)", que="IMC = peso (kg) ÷ talla² (m).", orden=True,
    grados=[("25-29,9", "Sobrepeso", []), ("30-34,9", "Obesidad I", []), ("35-39,9", "Obesidad II", ["Cirugía si hay comorbilidades"]), ("≥ 40", "Obesidad III", ["Considerar cirugía bariátrica"])],
    caso=2, porque=[("IMC 38", True)],
    conducta="Estilo de vida con ejercicio aeróbico; fármacos (semaglutida o tirzepatida) con indicación médica.")
FUE["END-053"] = "ADA Standards of Care in Diabetes 2026; Endocrine Society; AACE, obesidad (2025); OMS, IMC."

TRI["GAS-063"] = TR([("Dolor ≥ 1 día por semana", "3-4 veces al mes: cerca", None), ("Por ≥ 3 meses (inicio ≥ 6 meses)", "1 año", True),
                     ("Relacionado con la defecación", "Cede al defecar", True), ("Cambio en la frecuencia", "Alterna diarrea y estreñimiento", True),
                     ("Cambio en la forma de las heces", "Sí", True)],
                    [("Criterios de Roma IV (dolor + 2 de 3)", 0, 4)], "Sin signos de alarma y examen normal: intestino irritable mixto.", rotulo="Criterios con nombre propio")
FUE["GAS-063"] = "Roma IV (2016); ACG, intestino irritable (2021); AGA (2022); BSG (2021)."

ESC["GIN-185"] = dict(nombre="Clasificación O-RADS ecográfica (ACR 2022)", que="Riesgo de malignidad de una masa anexial por su aspecto.", orden=True,
    grados=[("O-RADS 1", "Normal", ["Folículo o quiste ≤ 3 cm"]), ("O-RADS 2", "Casi seguro benigno (< 1 %)", ["Quiste simple 3-10 cm"]),
            ("O-RADS 3", "Riesgo bajo (1-10 %)", []), ("O-RADS 4", "Intermedio (10-50 %)", []), ("O-RADS 5", "Alto (≥ 50 %)", [])],
    caso=1, porque=[("Unilocular, 4 cm, sin tabiques ni excrecencias", True), ("Premenopáusica asintomática", True)],
    conducta="Observar; control ecográfico opcional (8-12 semanas) si mide más de 5 cm.")

ESC["CIR-099"] = dict(nombre="Lesión esplénica (AAST 2018)", que="Se gradúa con la TC con contraste (hematoma, laceración, sangrado activo).", orden=True,
    grados=[("I", "Hematoma < 10 % o laceración < 1 cm", []), ("II", "Hematoma 10-50 % o laceración 1-3 cm", []),
            ("III", "Hematoma > 50 % o laceración > 3 cm", []), ("IV", "Sangrado activo intraesplénico o hiliar", []),
            ("V", "Bazo destrozado o sangrado activo libre", [])],
    caso=-1, porque=[("FAST con ~300 mL: hay sangrado", True), ("El grado lo da la TC si está estable", True)],
    conducta="Estable: TC y manejo no operatorio (± embolización). Inestable: laparotomía.")
FUE["CIR-099"] = "ATLS 11.ª ed. (2025); WSES/AAST, trauma esplénico (2017) y seguimiento no operatorio (2022)."

ESC["TRA-042"] = dict(nombre="Fracturas del escafoides según la zona (Herbert)", que="Cuanto más proximal, peor irrigada: más riesgo de no unión y necrosis.", orden=True,
    grados=[("Distal / tubérculo", "Bien irrigada", ["Yeso 6 semanas"]), ("Cintura (≈ 70 %)", "Riesgo intermedio", ["Yeso 8-12 semanas o tornillo"]),
            ("Polo proximal", "Mal irrigado", ["Necrosis avascular: tornillo"])],
    caso=-1, porque=[("Dolor en la tabaquera anatómica", True), ("La zona se ve en la Rx de escafoides (o en la RM)", True)],
    conducta="Inmovilizar con yeso de escafoides y repetir Rx o pedir RM.")

ESC["GAS-064"] = dict(nombre="Clasificación de Atlanta revisada (2012)", que="La gravedad se define por la falla orgánica y las complicaciones.", orden=True,
    grados=[("Leve", "Sin falla orgánica ni complicaciones", ["Alta en días"]), ("Moderada", "Falla orgánica < 48 h o complicación local", []),
            ("Grave", "Falla orgánica > 48 h", ["UCI"])],
    caso=0, porque=[("Ranson al ingreso 1 (solo la edad)", True), ("Sin falla orgánica descrita", True)],
    conducta="Ringer lactato moderado, analgesia y nutrición enteral temprana.")

ESC["CIR-101"] = dict(nombre="Lesión pancreática (AAST)", que="El dato clave es si se rompió el conducto pancreático principal.", orden=True,
    grados=[("I", "Contusión o laceración menor", ["Sin lesión del conducto"]), ("II", "Contusión o laceración mayor", ["Sin lesión del conducto"]),
            ("III", "Sección distal o del conducto", ["A la izquierda de la mesentérica"]), ("IV", "Sección proximal", ["Compromete la ampolla"]),
            ("V", "Destrucción de la cabeza", [])],
    caso=-1, porque=[("Hipocalcemia y leucocitosis: inflamación pancreática", True), ("TC o CPRM ve el conducto", True)],
    conducta="TC con contraste; sin lesión del conducto, manejo conservador.")

ESC["PED-185"] = dict(nombre="Tipos de osteogénesis imperfecta (Sillence)", que="Del más leve al letal.", orden=True,
    grados=[("I", "Leve", ["Escleróticas azules", "Talla casi normal"]), ("II", "Letal perinatal", ["Fracturas intraútero"]),
            ("III", "Grave, deformante", ["Huesos cortos y arqueados", "Talla baja"]), ("IV", "Moderado", ["Escleróticas normales o grises"])],
    caso=-1, porque=[("Escleróticas azules: tipo I", True), ("Huesos cortos y arqueados: más grave (III)", True)],
    conducta="Bifosfonatos y enclavado de deformidades; descartar maltrato.")

ESC["NRL-049"] = dict(nombre="Estadios del quiste en la neurocisticercosis (Escobar)", que="Por cómo se ve en la TC o la RM.", orden=True,
    grados=[("Vesicular", "Quiste vivo con escólex", ["Albendazol + corticoide"]), ("Coloidal", "Muriendo, con edema", ["Albendazol + corticoide"]),
            ("Granular nodular", "En retracción", []), ("Calcificado", "Quiste muerto", ["Solo antiepiléptico"])],
    caso=3, porque=[("Calcificaciones múltiples en la TC", True)],
    conducta="Antiepiléptico; el antiparasitario no sirve en quistes calcificados.")

ESC["PED-187"] = dict(nombre="Clasificación de la neumonía en el niño (OMS/AIEPI)", que="Por la respiración rápida y los signos de peligro.", orden=True,
    grados=[("Tos o resfrío", "Sin neumonía", ["Casa"]), ("Neumonía", "Respiración rápida o tiraje", ["Amoxicilina oral"]),
            ("Neumonía grave", "Signo de peligro, SatO₂ < 90 % o dificultad grave", ["Hospitalizar, oxígeno, antibiótico EV"])],
    caso=2, porque=[("Aleteo, polipnea y tiraje", True), ("Dificultad respiratoria marcada", True)],
    conducta="Hospitalizar, oxígeno si SatO₂ < 92 %, Rx y antibiótico.")
FUE["PED-187"] = "OMS, neumonía en el niño (2024); BTS, neumonía en niños (2011); MINSA Perú, AIEPI."

ESC["CAR-063"] = dict(nombre="Gravedad de la estenosis aórtica (ecocardiograma)", que="Velocidad máxima, gradiente medio y área valvular.", orden=True,
    grados=[("Leve", "V < 3 m/s", ["Gradiente < 20 mmHg"]), ("Moderada", "V 3-3,9 m/s", ["Gradiente 20-39"]),
            ("Grave", "V ≥ 4 m/s", ["Gradiente ≥ 40, área < 1 cm²"])],
    caso=2, porque=[("Angina, síncope y disnea (la tríada)", True), ("Pulso parvus y soplo eyectivo", True)],
    conducta="Ecocardiograma; reemplazo valvular (cirugía o TAVI).")

ESC["END-056"] = dict(nombre="Albuminuria (KDIGO)", que="Relación albúmina/creatinina en orina (o albúmina en 24 h).", orden=True,
    grados=[("A1", "< 30 mg/g", ["Normal"]), ("A2", "30-300 mg/g", ["Moderadamente aumentada"]), ("A3", "> 300 mg/g", ["Nefropatía establecida: referir"])],
    caso=2, porque=[("Albuminuria > 300 mg/24 h", True)],
    conducta="IECA/ARA II e iSGLT2; referir a nefrología o medicina interna.")

ESC["NEU-053"] = dict(nombre="Gravedad de la COVID-19 (OMS)", que="Por la oxigenación y la frecuencia respiratoria.", orden=True,
    grados=[("Leve", "Sin neumonía", []), ("Moderada", "Neumonía sin signos graves", ["SatO₂ ≥ 90 %"]),
            ("Grave", "SatO₂ < 90 % o FR > 30", ["Oxígeno, dexametasona"]), ("Crítica", "SDRA, sepsis o choque", ["UCI"])],
    caso=1, porque=[("SatO₂ 90 % y FR 26", True), ("PaO₂/FiO₂ 305", True)],
    conducta="Oxígeno convencional con meta 92-96 %; prono despierto; subir si empeora.")

ESC["INF-095"] = dict(nombre="Infecciones de piel y partes blandas (Eron)", que="Por el compromiso general y las comorbilidades; decide dónde y con qué tratar.", orden=True,
    grados=[("I", "Sin toxicidad sistémica", ["Antibiótico oral"]), ("II", "Fiebre o comorbilidad que complica", ["Oral o EV breve"]),
            ("III", "Aspecto tóxico o inestable", ["EV hospitalizado"]), ("IV", "Sepsis o fascitis necrosante", ["Cirugía + EV"])],
    caso=1, porque=[("Fiebre", True), ("Obesidad (IMC 38)", True)],
    conducta="Cefalexina o dicloxacilina; marcar bordes y vigilar signos de fascitis.")
FUE["INF-095"] = "IDSA, infecciones de piel y partes blandas (2014); WSES/SIS-E, infecciones de piel y partes blandas (2022)."

ESC["NRL-051"] = dict(nombre="Escala de discapacidad de Hughes (Guillain-Barré)", que="0 a 6; guía el tratamiento y el pronóstico.", orden=True,
    grados=[("0-1", "Sano o síntomas menores", []), ("2", "Camina 10 m sin ayuda", []), ("3", "Camina con ayuda", []),
            ("4", "En cama o silla", []), ("5", "Necesita ventilación", ["UCI"]), ("6", "Muerte", [])],
    caso=4, porque=[("SatO₂ 89 %, FR 28, cianosis y somnolencia", True), ("Falla respiratoria: necesita ventilación", True)],
    conducta="Intubar y ventilar; inmunoglobulina EV o plasmaféresis.")

ESC["NEF-079"] = KDIGO_LRA(-1, [("Falla renal aguda en choque con disfunción de órganos", True), ("La creatinina y la diuresis exactas no se dan", True)],
                           "Hemodiálisis continua (TRRC) si hay indicación (AEIOU).")
FUE["NRL-048"] = "IHS, recomendaciones globales del tratamiento preventivo de la migraña (2024); AHS (2021; act. 2024); EHF (2022)."
FUE["CIR-105"] = "ABA, criterios de referencia (2022); ATLS 11.ª ed. (2025)."
FUE["CIR-104"] = "ESVS, enfermedades de las arterias mesentéricas (2025); WSES, isquemia mesentérica aguda (2022)."
FUE["HEM-037"] = "NICE NG239, déficit de vitamina B12 (2024); BSH (2014); Harrison Principios de Medicina Interna 22.ª ed. (2025)."

# ───────────────────────────── bloque 400-499
from esc28 import HTA_EMB, ITU, HIPERK
NAC25 = "ATS, neumonía adquirida en la comunidad (2025); ATS/IDSA (2019); BTS"

ESC["NRL-052"] = GLASGOW_TEC(-1, [("Lúcido 2 h y luego estupor", True), ("Midriasis derecha, hemiparesia izquierda y Cushing: herniación", True)],
                             "Intubar si Glasgow ≤ 8, cabecera a 30°, manitol y craneotomía urgente.")
FUE["NRL-052"] = "ATLS 11.ª ed. (2025); Brain Trauma Foundation (4.ª ed., 2016)."
FUE["NEU-055"] = NAC25 + " (2009; act.)."
FUE["NEU-062"] = NAC25 + "."
FUE["NEU-063"] = NAC25 + "."

ESC["NEU-056"] = dict(ESC["NEU-053"], caso=2, porque=[("Usa músculos accesorios: dificultad respiratoria grave", True), ("Oxígeno cada vez mayor y FR 28", True)],
                      conducta="Referir al hospital: alto flujo, dexametasona y prono despierto.")

ESC["END-059"] = dict(nombre="Gravedad de la cetoacidosis (ADA 2024)", que="Por el pH, el bicarbonato y el estado mental.", orden=True,
    grados=[("Leve", "pH 7,25-7,30", ["HCO₃ 15-18, alerta"]), ("Moderada", "pH 7,00-7,24", ["HCO₃ 10-14, somnoliento"]),
            ("Grave", "pH < 7,00", ["HCO₃ < 10, estupor o coma"])],
    caso=-1, porque=[("PA 80/60 y FC 130: deshidratación grave", True), ("Glasgow 15; falta la gasometría", True)],
    conducta="Suero fisiológico EV, potasio y luego insulina en infusión; nada por vía oral.")
FUE["END-059"] = "ADA/EASD/JBDS/AACE/DTS, consenso de crisis hiperglucémicas (2024); ADA Standards of Care in Diabetes 2026."
FUE["END-051"] = "ADA/EASD/JBDS/AACE/DTS, consenso de crisis hiperglucémicas (2024); Guyton y Hall, Tratado de fisiología médica 14.ª ed."

ESC["NEF-080"] = HIPERK(2, [("K⁺ 8", True), ("Bloqueo AV de 2.º grado en el ECG", True)],
                        "Gluconato de calcio EV ya; insulina + glucosa, salbutamol y diálisis si no cede.")

ESC["OFT-046"] = dict(nombre="Clasificación de la rinitis alérgica (ARIA)", que="Por la duración y por cuánto afecta la vida diaria.", orden=False,
    grados=[("Intermitente", "< 4 días/semana o < 4 semanas", []), ("Persistente", "≥ 4 días/semana y ≥ 4 semanas", []),
            ("Leve", "Sueño y actividades normales", []), ("Moderada-grave", "Altera sueño, estudio o trabajo", [])],
    caso=-1, porque=[("10 días de síntomas: falta saber cuántos días por semana", True), ("Se clasifica por duración y por impacto", True)],
    conducta="Corticoide intranasal ± antihistamínico; prick test para confirmar la sensibilización.")
FUE["OFT-046"] = "ARIA-EAACI, revisión 2024-2025; AAAAI."

ESC["HEM-039"] = dict(nombre="Gravedad de la hemofilia (WFH)", que="Por el nivel de factor VIII (A) o IX (B).", orden=True,
    grados=[("5-40 %", "Leve", ["Sangra con cirugía o trauma"]), ("1-5 %", "Moderada", ["Sangra con traumas leves"]),
            ("< 1 %", "Grave", ["Hemartrosis espontáneas"])],
    caso=-1, porque=[("Hemartrosis tras trauma", True), ("El nivel de factor VIII aún no se mide", True)],
    conducta="Dosar factor VIII y IX; reponer factor; no AINE ni inyecciones IM.")
FUE["HEM-039"] = "WFH, guías de manejo de la hemofilia (3.ª ed., 2020; act. 2025); ISTH (2024); Harrison Principios de Medicina Interna 22.ª ed. (2025)."

ESC["PED-196"] = dict(ESC["REU-043"], caso=2, porque=[("Voz ronca y dificultad respiratoria", True), ("Cianosis", True)],
                      conducta="Adrenalina 0,01 mg/kg IM (máx. 0,3 mg) y repetir cada 5-15 min.")
FUE["PED-196"] = "WAO, anafilaxia (2020); GA²LEN (2024); EAACI (2021); AAP."

ESC["GIN-211"] = HTA_EMB(3, [("Preeclampsia con criterios de severidad", True), ("Riesgo de eclampsia hasta 24-48 h posparto", True)],
                         "Sulfato de magnesio hasta 24 h después del parto; vigilar reflejos, FR y diuresis.")
FUE["GIN-211"] = "ACOG n.º 222 (2020); ISSHP (2021); OMS, preeclampsia y eclampsia (2011; act. 2020); MINSA Perú."

ESC["PED-201"] = dict(nombre="Puntaje de apendicitis pediátrica (PAS, Samuel)", modo="puntaje", que="De 0 a 10 puntos; guía la imagen y la cirugía.",
    items=[("Tos", "Dolor en FID al toser, saltar o percutir (2)", "Rebote: probable", None), ("Anor", "Anorexia (1)", "Hiporexia", 1),
           ("Fieb", "Fiebre ≥ 38 °C (1)", "38,5 °C", 1), ("Vom", "Náuseas o vómitos (1)", "Sí", 1), ("FID", "Dolor a la palpación en FID (2)", "Sí", 2),
           ("Leu", "Leucocitos > 10 000 (1)", "12 000", 1), ("Neu", "Neutrófilos > 7500 (1)", "8500", 1), ("Migr", "Migración del dolor a FID (1)", "Sí", 1)],
    total_txt="Total: ≥ 8 puntos", total_nota="de 0 a 10",
    rangos=[("≤ 3", "Bajo", "Observar o alta con control"), ("4-6", "Intermedio", "Ecografía"), ("≥ 7", "Alto", "Cirujano; eco para confirmar")], caso_rango=2,
    porque=[("Migración, fiebre, vómitos, dolor en FID y leucocitosis con neutrofilia", True)],
    conducta="Ecografía y apendicectomía laparoscópica con antibiótico.")

ESC["CIR-111"] = ATLS_CLASES(2, [("PA 90/50 y FC 100", True), ("Peritonitis por víscera rota", True)],
                             "Sangre y cristaloides limitados; laparotomía exploradora.")
FUE["CIR-111"] = "ATLS 11.ª ed. (2025); WSES, trauma abdominal (2020)."

TRI["PED-199"] = TR([("Sibilancias recurrentes", "Desde los 4 años", True), ("Dermatitis atópica (mayor)", "Sí", True),
                     ("Padre o madre con asma (mayor)", "No se informa", None), ("Sensibilización o rinitis alérgica (menor)", "Prick (+) a ácaros", True),
                     ("Eosinofilia ≥ 4 % (menor)", "No se informa", None)],
                    [("Índice predictivo de asma (Castro-Rodríguez)", 0, 4)], "Sibilancias + 1 criterio mayor: alto riesgo de asma.", rotulo="Criterios con nombre propio")

ESC["GIN-215"] = ITU(2, [("Pielonefritis hace 15 días", True), ("Urocultivo actual negativo", True)],
                     "Urocultivo mensual hasta el parto; tratar cualquier bacteriuria.")
FUE["GIN-215"] = "ACOG; IDSA, bacteriuria asintomática (2019); EAU, infecciones urológicas (2025); Williams Obstetricia 26.ª ed. (2022); MINSA Perú."

ESC["NEF-082"] = KDIGO_LRA(-1, [("Creatinina 2,8 sin basal conocida", True), ("Oliguria con globo vesical: causa posrenal", True)],
                           "Sonda vesical ya; vigilar diuresis y potasio.")
ESC["NEF-083"] = dict(ESC["NEF-074"], porque=[("Debilidad, calambres, ROT ↓", True), ("Ondas U y T aplanada", True)],
                      conducta="Reponer KCl y magnesio; buscar trastorno alimentario.")

ESC["OFT-048"] = dict(nombre="Estadios de la retinopatía del prematuro (ICROP3)", que="Se suma la zona (I-III) y si hay enfermedad plus.", orden=True,
    grados=[("1", "Línea de demarcación", []), ("2", "Cresta", []), ("3", "Vasos nuevos sobre la cresta", ["Tipo 1: tratar en 72 h"]),
            ("4", "Desprendimiento parcial", []), ("5", "Desprendimiento total", ["Ceguera"])],
    caso=-1, porque=[("Prematura de 32 semanas con oxígeno: hay que examinarla", True), ("El estadio se ve en el primer fondo de ojo", True)],
    conducta="Primer examen a las 4 semanas de vida; controles cada 1-2 semanas.")
FUE["OFT-048"] = "ICROP3 (2021); AAP/AAO, tamizaje de ROP (2018; vigente); MINSA Perú, guía de ROP."
