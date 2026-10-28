"""Catálogo extensible de pruebas de laboratorio → guardia/laboratorio.json.
HONESTIDAD DE LAS FUENTES: no se pudo consultar en esta sesión ningún intervalo de un laboratorio peruano ni los textos de MINSA/INS/EsSalud (los dominios no son accesibles
desde el entorno). Por eso todo intervalo numérico es «educativo»: rango habitual en adultos de textos de medicina de laboratorio, NO verificado contra un documento concreto
y NO específico del Perú. Siempre prevalece el intervalo del laboratorio que procesa la muestra. Solo se marcan como «verificada» las cifras con respaldo en una fuente leída.
Intervalo de referencia ≠ umbral diagnóstico ≠ objetivo terapéutico ≠ valor crítico: se guardan en campos distintos (`intervalos` vs `umbrales`). No se incluyen valores críticos
porque ninguno tiene fuente verificable (cada laboratorio define los suyos)."""
import json, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EDU = "Intervalo educativo de adultos (rango habitual en textos de medicina de laboratorio). No verificado contra un documento específico ni propio del Perú; prevalece el del laboratorio que procesa la muestra."
T = []
def P(id, nombre, cat, unidad, ivs=None, umbrales=None, adv=None, metodo="Depende del laboratorio y del equipo", sin=None, cual=None, normal=None, fuente=None, tipo_fuente="educativo", conv=None):
    e = {"id": id, "nombre": nombre, "categoria": cat, "unidad": unidad, "sinonimos": sin or [], "intervalos": ivs or [], "umbrales": umbrales or [], "metodo": metodo, "fuente_tipo": tipo_fuente, "fuente": fuente or EDU, "advertencias": adv or [], "criticos": None}
    if cual: e["cualitativa"] = True; e["normal"] = normal
    if conv: e["conversion"] = conv
    T.append(e)
def iv(bajo, alto, sexo="todos", emin=None, emax=None, cond=None, texto=None):
    d = {"sexo": sexo, "bajo": bajo, "alto": alto}
    if emin is not None: d["edad_min"] = emin
    if emax is not None: d["edad_max"] = emax
    if cond: d["condicion"] = cond
    d["texto"] = texto or ("%s–%s" % (bajo, alto) if bajo is not None and alto is not None else ("< %s" % alto if alto is not None else "> %s" % bajo))
    return d
def U(tipo, texto, pmid=None, fuente=None): return {"tipo": tipo, "texto": texto, "pmid": pmid or "", "fuente": fuente or ""}
ADU = dict(emin=18)
H, B, E, RH, CO, GA, MC, EN, OR, MI, SE, ES = "Hematología", "Bioquímica", "Electrolitos", "Función renal y hepática", "Coagulación", "Gasometría", "Marcadores cardíacos", "Endocrinología", "Orina", "Microbiología", "Serología", "Pruebas especiales"
ALT_HB = "En altitud la hemoglobina normal es mayor: la norma peruana NTS N.° 213-MINSA/DGIESP-2024 adopta los puntos de corte de anemia de la OMS 2024 y los ajusta por altitud (la OMS 2024 modifica el ajuste desde 500 m s. n. m.). No se pudo leer su tabla en esta sesión: usa la norma vigente y el calculador oficial."
# --- Hematología
P("hemoglobina", "Hemoglobina", H, "g/dL", [iv(13.5, 17.5, "M", **ADU), iv(12.0, 15.5, "F", **ADU), iv(10.5, None, "F", cond="gestacion-t2", texto="Punto de corte de anemia: < 10,5 g/dL (2.º trimestre)")],
  [U("umbral_diagnostico", "OMS 2024 (citada en el editorial peruano): anemia si Hb < 10,5 g/dL en gestantes del 2.º trimestre y en niños de 6 a 23 meses.", "39166631", "Gonzales GF, Suarez VJ. Rev Peru Med Exp Salud Publica 2024;41(2):102-4")],
  [ALT_HB, "El intervalo del 2.º trimestre es un punto de corte de anemia (umbral), no un intervalo de referencia; para 1.er y 3.er trimestre y otras edades no hay valor cargado: consulta la norma."], conv="hemoglobina", sin=["Hb"])
P("hematocrito", "Hematocrito", H, "%", [iv(41, 53, "M", **ADU), iv(36, 46, "F", **ADU)], adv=[ALT_HB], sin=["Hto"])
P("leucocitos", "Leucocitos", H, "×10³/µL", [iv(4.5, 11.0, **ADU)], sin=["WBC", "recuento de leucocitos"],
  umbrales=[U("umbral_diagnostico", "Guías de Tokio 2018 (colangitis): leucocitos < 4 o > 10 ×10³/µL cuentan como criterio de inflamación sistémica.", "29032610", "Kiriyama S et al. J Hepatobiliary Pancreat Sci 2018")])
P("plaquetas", "Plaquetas", H, "×10³/µL", [iv(150, 400, **ADU)], sin=["PLT"], adv=["En dengue la caída de plaquetas acompaña a la fase crítica; la cifra aislada no indica transfusión."])
P("vcm", "Volumen corpuscular medio", H, "fL", [iv(80, 100, **ADU)], sin=["VCM", "MCV"])
P("ferritina", "Ferritina", H, "ng/mL", [iv(24, 336, "M", **ADU), iv(11, 307, "F", **ADU)], adv=["Es reactante de fase aguda: sube con la inflamación aunque el hierro esté bajo."])
# --- Bioquímica
P("glucosa", "Glucosa en ayunas", B, "mg/dL", [iv(70, 99, **ADU)], [U("umbral_diagnostico", "Una glucemia ≥ 200 mg/dL al azar con síntomas, o ≥ 126 mg/dL en ayunas confirmada, es criterio de diabetes (criterio educativo de ADA).", "", "ADA Standards of Care (no consultado en texto completo)")], conv="glucosa", sin=["glicemia", "glucemia"])
P("hba1c", "Hemoglobina glicosilada (HbA1c)", EN, "%", [iv(4.0, 5.6, **ADU)], [U("umbral_diagnostico", "≥ 6,5 % es criterio de diabetes (criterio educativo de ADA).", "", "ADA Standards of Care (no consultado en texto completo)")], adv=["Puede alterarse con anemias, hemoglobinopatías o recambio eritrocitario."])
P("albumina", "Albúmina sérica", B, "g/dL", [iv(3.5, 5.0, **ADU)])
P("ldh", "Lactato deshidrogenasa (LDH)", B, "U/L", [iv(140, 280, **ADU)], adv=["Muy dependiente del método; inespecífica."])
P("osmolaridad", "Osmolaridad sérica", B, "mOsm/kg", [iv(275, 295, **ADU)])
P("bhb", "β-hidroxibutirato (cetonemia)", B, "mmol/L", [iv(0, 0.6, **ADU)], [U("objetivo_terapeutico", "Un β-hidroxibutirato < 0,6 mmol/L se usa como una de las condiciones de resolución de la cetoacidosis diabética (consenso ADA/EASD 2024; no verificado en texto completo).", "39052901", "Umpierrez GE et al. Diabetes Care 2024")], adv=["Distingue de la cetonuria (acetoacetato) que no mide el β-hidroxibutirato."])
# --- Electrolitos
P("sodio", "Sodio", E, "mmol/L", [iv(135, 145, **ADU)], sin=["Na"])
P("potasio", "Potasio", E, "mmol/L", [iv(3.5, 5.0, **ADU)], [U("objetivo_terapeutico", "En la cetoacidosis diabética se retrasa la insulina si el potasio es < 3,5 mmol/L y se busca mantener 4–5 mmol/L durante el tratamiento (consenso ADA/EASD 2024; no verificado en texto completo).", "39052901", "Umpierrez GE et al. Diabetes Care 2024")], adv=["La hemólisis de la muestra eleva falsamente el potasio."], sin=["K"])
P("cloro", "Cloro", E, "mmol/L", [iv(98, 107, **ADU)], sin=["Cl"])
P("bicarbonato", "Bicarbonato sérico (CO₂ total)", E, "mmol/L", [iv(22, 29, **ADU)])
P("calcio", "Calcio total", E, "mg/dL", [iv(8.5, 10.5, **ADU)], adv=["Se corrige por albúmina; el calcio iónico refleja mejor el estado fisiológico."], conv="calcio")
P("calcio_ionico", "Calcio iónico", E, "mmol/L", [iv(1.12, 1.32, **ADU)], adv=["Depende del pH y del tipo de muestra (sangre entera o suero)."])
P("magnesio", "Magnesio", E, "mg/dL", [iv(1.7, 2.2, **ADU)])
P("fosforo", "Fósforo (fosfato)", E, "mg/dL", [iv(2.5, 4.5, **ADU)])
P("anion_gap", "Brecha aniónica (anion gap)", E, "mmol/L", [iv(8, 12, **ADU)], adv=["El valor de referencia cambia con el método (con o sin potasio) y con la albúmina."])
# --- Función renal y hepática
P("creatinina", "Creatinina sérica", RH, "mg/dL", [iv(0.7, 1.3, "M", **ADU), iv(0.6, 1.1, "F", **ADU)], [U("umbral_diagnostico", "Guías de Tokio 2018: creatinina > 2,0 mg/dL cuenta como disfunción renal en la colangitis grado III.", "29032610", "Kiriyama S et al. J Hepatobiliary Pancreat Sci 2018")], conv="creatinina", adv=["Sube tarde en la lesión renal aguda y depende de la masa muscular."])
P("urea", "Urea / nitrógeno ureico (BUN)", RH, "mg/dL", [iv(7, 20, **ADU)], adv=["Se informa como nitrógeno ureico (BUN) o como urea; no son lo mismo."])
P("bilirrubina_total", "Bilirrubina total", RH, "mg/dL", [iv(0.1, 1.2, **ADU)], [U("umbral_diagnostico", "Guías de Tokio 2018: bilirrubina total ≥ 2 mg/dL cuenta como colestasis en el diagnóstico de colangitis.", "29032610", "Kiriyama S et al. J Hepatobiliary Pancreat Sci 2018")], conv="bilirrubina_total")
P("bilirrubina_directa", "Bilirrubina directa", RH, "mg/dL", [iv(0.0, 0.3, **ADU)])
P("ast", "AST (TGO)", RH, "U/L", [iv(10, 40, **ADU)], sin=["TGO"], adv=["Se eleva también en la lesión muscular y la hemólisis."])
P("alt", "ALT (TGP)", RH, "U/L", [iv(7, 55, **ADU)], sin=["TGP"])
P("fosfatasa_alcalina", "Fosfatasa alcalina", RH, "U/L", [iv(44, 147, **ADU)], adv=["Aumenta en la gestación por origen placentario y en el crecimiento óseo."])
P("ggt", "Gamma-glutamil transferasa (GGT)", RH, "U/L", [iv(8, 61, "M", **ADU), iv(5, 36, "F", **ADU)])
P("lipasa", "Lipasa", RH, "U/L", [iv(0, 160, **ADU)], adv=["Muy dependiente del método."])
# --- Coagulación
P("inr", "INR", CO, "(índice)", [iv(0.8, 1.2, **ADU)], [U("umbral_diagnostico", "Guías de Tokio 2018: INR > 1,5 cuenta como disfunción hepática en la colangitis grado III.", "29032610", "Kiriyama S et al. J Hepatobiliary Pancreat Sci 2018")])
P("tp", "Tiempo de protrombina", CO, "s", [iv(11, 13.5, **ADU)])
P("ttpa", "Tiempo de tromboplastina parcial activada (TTPa)", CO, "s", [iv(25, 35, **ADU)])
P("fibrinogeno", "Fibrinógeno", CO, "mg/dL", [iv(200, 400, **ADU)], adv=["Aumenta en la gestación y en la inflamación."])
P("dimero_d", "Dímero D", CO, "µg/mL FEU", [iv(0, 0.5, **ADU)], adv=["Muy dependiente del método; es inespecífico y aumenta en la gestación, la infección y el posoperatorio."])
# --- Gasometría
P("ph", "pH arterial", GA, "(unidades)", [iv(7.35, 7.45, **ADU)])
P("pco2", "PaCO₂", GA, "mmHg", [iv(35, 45, **ADU)])
P("po2", "PaO₂", GA, "mmHg", [iv(80, 100, **ADU)], adv=["Valores a nivel del mar y respirando aire ambiente. En altitud la PaO₂ normal es menor (relevante en el Perú)."])
P("hco3", "Bicarbonato (gasometría)", GA, "mmol/L", [iv(22, 26, **ADU)])
P("exceso_base", "Exceso de base", GA, "mmol/L", [iv(-2, 2, **ADU)])
P("lactato", "Lactato", GA, "mmol/L", [iv(0.5, 2.0, **ADU)], [U("umbral_diagnostico", "Sepsis-3: en el choque séptico se exige lactato > 2 mmol/L pese a una reposición adecuada, además de la necesidad de vasopresor.", "26903338", "Singer M et al. JAMA 2016")], adv=["Distingue lactato arterial de venoso; también sube por causas no sépticas."])
# --- Marcadores cardíacos
P("troponina", "Troponina cardíaca de alta sensibilidad", MC, "ng/L", [{"sexo": "todos", "bajo": None, "alto": None, "texto": "Percentil 99 del ensayo de cada laboratorio (no hay un valor universal)"}],
  [U("umbral_diagnostico", "Cuarta definición universal del infarto: se define lesión miocárdica por un valor por encima del percentil 99 del límite superior de referencia del ensayo.", "30153967", "Thygesen K et al. J Am Coll Cardiol 2018")], adv=["Los ensayos no son intercambiables: en cada caso se muestra el percentil 99 del ensayo supuesto. Se eleva en muchas causas de lesión miocárdica distintas del infarto."])
# --- Endocrinología
P("tsh", "TSH", EN, "mUI/L", [iv(0.4, 4.0, **ADU)], adv=["En la gestación cambian los límites (revisión sistemática PMID 35861700); no se cargan cifras de embarazo en esta versión."])
P("t4l", "T4 libre", EN, "ng/dL", [iv(0.8, 1.8, **ADU)], adv=["Depende del método."])
P("anti_tpo", "Anticuerpos anti-TPO", EN, "UI/mL", [iv(0, 35, **ADU)], adv=["El punto de corte depende del ensayo."])
P("bhcg", "β-hCG cuantitativa", EN, "mUI/mL", [iv(0, 5, "F", **ADU), iv(None, None, "F", cond="gestacion-t1", texto="En gestación temprana no hay un valor «normal» único: se interpreta con la ecografía y la evolución seriada")], adv=["Intervalo en mujeres no gestantes. En la gestación temprana no hay un «normal» único: se interpreta con la ecografía y la evolución seriada."])
# --- Inflamación y pruebas especiales
P("pcr", "Proteína C reactiva", ES, "mg/dL", [iv(0, 1.0, **ADU)], [U("umbral_diagnostico", "Guías de Tokio 2018: PCR ≥ 1 mg/dL cuenta como criterio de inflamación sistémica en la colangitis.", "29032610", "Kiriyama S et al. J Hepatobiliary Pancreat Sci 2018")])
P("procalcitonina", "Procalcitonina", ES, "ng/mL", [iv(0, 0.1, **ADU)], adv=["Orienta pero no confirma infección bacteriana."])
P("cd4", "Linfocitos T CD4", ES, "células/µL", [iv(500, 1500, **ADU)], [U("umbral_diagnostico", "En los ensayos de TB-VIH, el inicio precoz del antirretroviral benefició sobre todo a quienes tenían CD4 < 50 células/µL.", "22010914", "Havlir DV et al. N Engl J Med 2011")])
P("carga_viral", "Carga viral del VIH", ES, "copias/mL", [{"sexo": "todos", "bajo": None, "alto": None, "texto": "Indetectable bajo tratamiento eficaz (el límite depende del ensayo)"}])
# --- Orina
P("orina_densidad", "Densidad urinaria", OR, "(g/mL)", [iv(1.003, 1.030, **ADU)])
P("orina_ph", "pH urinario", OR, "(unidades)", [iv(4.5, 8.0, **ADU)])
P("orina_leucocitos", "Leucocitos en sedimento urinario", OR, "/campo 400×", [iv(0, 5, **ADU)], adv=["Una piuria sin cultivo no basta para diagnosticar infección urinaria."])
P("orina_hematies", "Hematíes en sedimento urinario", OR, "/campo 400×", [iv(0, 2, **ADU)])
P("orina_esterasa", "Esterasa leucocitaria (tira reactiva)", OR, "", cual=True, normal="negativo")
P("orina_nitritos", "Nitritos (tira reactiva)", OR, "", cual=True, normal="negativo")
P("orina_cetonas", "Cetonas en orina (tira reactiva)", OR, "", cual=True, normal="negativo")
P("orina_glucosa", "Glucosa en orina (tira reactiva)", OR, "", cual=True, normal="negativo")
# --- Microbiología y serología (cualitativas)
for id_, nom in [("hemocultivo", "Hemocultivo"), ("urocultivo", "Urocultivo"), ("xpert_mtb", "Prueba molecular para M. tuberculosis (Xpert MTB/RIF)"), ("baciloscopia", "Baciloscopia de esputo")]:
    P(id_, nom, MI, "", cual=True, normal="negativo", adv=["Resultado cualitativo: se informa con identificación y sensibilidad cuando hay desarrollo."])
for id_, nom in [("vih", "Prueba de VIH (tamizaje)"), ("hbsag", "HBsAg"), ("vdrl", "VDRL / RPR"), ("ns1", "NS1 de dengue"), ("igm_dengue", "IgM anti-dengue")]:
    P(id_, nom, SE, "", cual=True, normal="no reactivo", adv=["Una prueba de tamizaje reactiva requiere confirmación."])
json.dump({"version": 1, "fecha": "2026-10-28", "aviso": EDU, "pruebas": T}, open(os.path.join(RAIZ, "guardia", "laboratorio.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(T), "pruebas")
