"""Bloque ENAM 2026 · Pediatría (parte 3)."""
from c26 import S, D, P, B, ILU, Q, L, NELSON, MINSA
from engine7 import _img_draw
import ilu7 as I

O = I.ORANGE
ESP = "PEDIATRÍA ENAM"

# PED-273 · Prevenir displasia broncopulmonar en sala de partos · RADIAL + franja
S("radial", "PED-273", "prematuro-29-semanas-sala-partos-pieza-t-presiones-definidas",
  "Prematuro de 29 semanas en sala de partos: ventilar con pieza en T y presiones definidas",
  "Neonatología · reanimación del prematuro", ESP,
  ("Displasia broncopulmonar desde la sala de partos", ["El pulmón prematuro se daña por exceso de presión y volumen y por exceso de oxígeno.",
                                                        "Lo que más protege al inicio: presiones controladas y PEEP desde la primera ventilación."]),
  ("Recién nacido de 29 semanas", ["Se atiende en sala de partos y pasará a la UCIN.", "¿Qué intervención reduce más el riesgo de displasia?"]),
  ["Pieza en T: fija la presión inspiratoria (PIP) y da PEEP/CPAP constante: menos volutrauma.",
   "En el prematuro < 32 semanas no se estimula con energía: se seca, se envuelve en bolsa plástica y se da calor.",
   "La meta de SatO₂ va subiendo por minutos (no 94-98 % de entrada) y la restricción hídrica no es la medida clave."],
  "ILCOR y AHA, reanimación neonatal (2020-2025); " + NELSON + ".",
  d=dict(rotulo="Las cuatro opciones frente al caso", ans=0, centro="Prematuro de 29 semanas: proteger el pulmón",
         items=[("Pieza en T con presiones definidas", ["PIP y PEEP fijas: menos barotrauma y volutrauma"]),
                ("Secado y estimulación enérgica", ["En < 32 semanas: bolsa plástica y calor, no frotar"]),
                ("SatO₂ 94-98 % de entrada", ["Exceso de oxígeno: más daño pulmonar"]),
                ("Restricción hídrica < 140 mL/kg/día", ["No es la intervención clave en sala de partos"])],
         ruta=["Prematuro < 32 semanas", "Calor y bolsa plástica", "CPAP o VPP con pieza en T", "UCIN"]),
  banda=B("Reanimador con pieza en T", D(lambda s, x, y: I.pieza_t(s, x, y), 330, 170),
          ["Se ajusta la presión inspiratoria máxima (PIP).", "La PEEP mantiene abiertos los alveolos entre respiraciones.",
           "Cada ventilación entrega la misma presión: el pulmón sufre menos."], ans=0),
  tabla=("Opciones de la pregunta", [("Pieza en T con presiones definidas", True), ("Secado y estimulación enérgica", False),
                                     ("SatO₂ 94-98 %", False), ("Restricción hídrica", False)],
         [("¿Previene DBP?", ["Sí", "No: hipotermia y no protege", "No: exceso de O₂", "No es lo principal"])]))

# PED-274 · Disentería en niña de riesgo · ÁRBOL + franja
S("arbol", "PED-274", "disenteria-nina-desnutrida-cardiopatia-coprocultivo-antibiotico",
  "Disentería en niña con desnutrición y cardiopatía: coprocultivo e iniciar antibiótico",
  "Enfermedad diarreica aguda · disentería", ESP,
  ("Disentería (diarrea con sangre)", ["Casi siempre bacteriana e invasiva: Shigella es la principal en niños.",
                                       "Se trata con antibiótico; en el niño de riesgo no se espera el cultivo."]),
  ("Anita, 15 meses", ["Cardiopatía congénita y desnutrición moderada; 3 días de heces con moco, 2 con sangre.",
                       "Hidratada, conectada; abdomen globuloso con ruidos aumentados, no doloroso."]),
  ["Diarrea con sangre = disentería: antibiótico empírico (ciprofloxacino o azitromicina según la norma).",
   "Con desnutrición o cardiopatía: tomar coprocultivo e iniciar el antibiótico sin esperar el resultado.",
   "El hemocultivo no es el estudio para disentería en una niña estable."],
  MINSA + ", guía de enfermedad diarreica aguda en niños; OMS.",
  arbol=Q("¿Hay sangre en las heces (disentería)?", [
      L("No", "Diarrea acuosa", ["Hidratación y zinc; sin antibiótico"]),
      Q("¿Desnutrición, cardiopatía u otro factor de riesgo?", [
          L("No", "Antibiótico oral empírico", ["Control a las 48 h"]),
          L("Sí", "COPROCULTIVO E INICIAR ANTIBIÓTICO", ["No esperar el resultado", "Ajustar con el antibiograma"], path=True)],
        edge="Sí", path=True)], path=True),
  banda=B("Germen más probable (Gram, esquema)", D(lambda s, x, y: I.gram(s, x + 20, y, "bacilos_neg", sc=1.1), 280, 180),
          ["Bacilos gramnegativos: Shigella, Campylobacter, E. coli invasiva.", "Invaden la mucosa: moco y sangre en las heces.",
           "Desnutrición y cardiopatía: más riesgo de complicarse."], ans=2),
  tabla=("Opciones de la pregunta", [("Coprocultivo e iniciar antibiótico", True), ("Coprocultivo y esperar", False),
                                     ("Hemocultivo y esperar", False), ("Hemocultivo e iniciar antibiótico", False)],
         [("Problema", ["Ninguno", "Retrasa el tratamiento", "Estudio equivocado y retrasa", "Estudio equivocado"])]))


# PED-275 · Loxoscelismo cutáneo-visceral · MAPA DE SIGNOS (foto real + dibujo)
def _loxo(s, x, y):
    _img_draw(s, x + 37, y, P("loxosceles.jpg", 220, 220,
                              [("circulo", 0.548, 0.405, 0.1, "«violín»", 0.06, 0.06)],
                              credito="Mampato · Wikimedia Commons · dominio público"))
    p = (f'<rect x="0" y="0" width="294" height="140" rx="10" fill="{I.SKIN}" stroke="{I.SKIN_D}" stroke-width="1.5"/>'
         + I.E(147, 64, 112, 52, "#fecaca", "none", 0) + I.E(147, 64, 78, 38, "#f8fafc", "none", 0)
         + I.P("M105 64 C108 42 136 34 160 40 C186 46 192 70 180 84 C164 98 124 96 110 84 Z", "#7e22ce", "#581c87", 1.5, 'opacity="0.8"')
         + I.E(148, 64, 16, 11, "#111827", "none", 0)
         + "".join(I.C(cx, cy, 5, "#9f1239", "#7f1d1d", 1) for cx, cy in [(122, 56), (172, 58), (132, 84), (166, 80)])
         + I.t(147, 132, "rojo, blanco y violeta con centro negro", "#7f1d1d", 10.5))
    I.g(s, x, y + 252, p)


S("mapa_signos", "PED-275", "placa-livida-centro-necrotico-hemolisis-orina-oscura-loxoscelismo",
  "Placa violácea con centro negro y hemólisis: loxoscelismo cutáneo-visceral",
  "Accidentes por animales ponzoñosos · arañas", ESP,
  ("Loxoscelismo", ["Mordedura de Loxosceles laeta, la «araña de los rincones» de las casas.",
                    "Cutáneo: placa necrótica. Cutáneo-visceral: además hemólisis y daño renal."]),
  ("Niño de 6 años, zona urbana de la costa norte", ["Hace 2 días «picadura» en el abdomen, hoy placa violácea con centro negro y ampollas de sangre.",
                                                     "Fiebre, palidez, orina rojiza; Hb 12 → 8 g/dL, bilirrubina indirecta alta."]),
  ["Placa livedoide necrótica + hemólisis (anemia, orina oscura, bilirrubina indirecta) = loxoscelismo cutáneo-visceral.",
   "Hospitalizar: hidratación, vigilar función renal, suero antiloxosceles si es precoz; corticoides según norma.",
   "Latrodectus da dolor y contracturas, sin necrosis; el escorpión, dolor local y síntomas autonómicos."],
  MINSA + ", norma de atención de accidentes por animales ponzoñosos; " + NELSON + ".",
  d=dict(rotulo="La araña y la lesión", PH=500, tag="ESTE CASO",
         ilu_titulo="La causa y la lesión",
         ilu=_loxo,
         ilu_pie="Arriba: Loxosceles (foto real). Abajo: placa livedoide (esquema).",
         signos=[dict(tit="Placa livedoide necrótica", lines=["Violácea, centro negro, ampollas de sangre."]),
                 dict(tit="Hemólisis", lines=["Palidez; hemoglobina de 12 a 8 g/dL."]),
                 dict(tit="Orina rojiza", lines=["Hemoglobinuria: riesgo de falla renal."]),
                 dict(tit="Bilirrubina indirecta alta", lines=["Destrucción de glóbulos rojos."]),
                 dict(tit="Causa: loxoscelismo cutáneo-visceral", on=True, lines=["Mordedura de Loxosceles laeta."])]),
  tabla=("Opciones de la pregunta", [("Escorpionismo", False), ("Loxoscelismo", True), ("Latrodectismo", False), ("Tarantulismo", False)],
         [("Clave", ["Dolor local, síntomas autonómicos", "Necrosis + hemólisis", "Dolor y contracturas, sin necrosis",
                     "Irritación local leve"])]))

# PED-276 · Hipotiroidismo congénito (ictericia prolongada) · MAPA DE SIGNOS
_ictericia = {k: "#fde68a" for k in ("cabeza", "torax", "abdomen", "brazo_d", "brazo_i", "pierna_d", "pierna_i")}
_hernia = I.E(120, 214, 9, 7, "#fbcfe8", "#9d174d", 1.5) + I.E(120, 24, 16, 9, "#fef9c3", "#a16207", 1.5, 'stroke-dasharray="3 2"')
S("mapa_signos", "PED-276", "neonato-15-dias-postermino-ictericia-prolongada-hernia-umbilical-hipotiroidismo",
  "Ictericia prolongada con hernia umbilical, hipotonía y fontanela grande: hipotiroidismo congénito",
  "Neonatología · ictericia prolongada", ESP,
  ("Ictericia prolongada del recién nacido", ["Ictericia que dura más de 14 días: siempre se estudia.",
                                              "Si se acompaña de hipotonía, hernia umbilical y fontanela grande: tiroides."]),
  ("Neonato de 15 días, nacido a las 42 semanas", ["Lactancia exclusiva; ictérico desde el 3.er día.",
                                                   "Hernia umbilical, tono disminuido y fontanela anterior grande."]),
  ["Ictericia prolongada + hernia umbilical + hipotonía + fontanela grande = hipotiroidismo congénito.",
   "Confirmar con TSH y T4 libre y dar levotiroxina sin esperar si el cuadro es claro.",
   "Atresia biliar: acolia y bilirrubina directa alta; galactosemia: vómitos, hipoglucemia y sepsis."],
  NELSON + "; AAP y ESPE, hipotiroidismo congénito.",
  d=dict(rotulo="Los signos del recién nacido", tag="ESTE CASO",
         ilu_titulo="El recién nacido del caso",
         ilu=lambda s, x, y: I.bebe(s, x + 27, y + 10, _ictericia, extra=_hernia,
                                    marcas=[(1, 150, 108), (2, 146, 222), (3, 60, 282), (4, 150, 20)], sc=1.0),
         ilu_pie="1 ictericia, 2 hernia umbilical, 3 hipotonía, 4 fontanela grande.",
         signos=[dict(tit="Ictericia prolongada", lines=["Más de 14 días; bilirrubina indirecta."]),
                 dict(tit="Hernia umbilical", lines=["Pared abdominal débil."]),
                 dict(tit="Hipotonía", lines=["Tono muscular disminuido."]),
                 dict(tit="Fontanela anterior grande", lines=["Retraso de la maduración ósea."]),
                 dict(tit="Causa: hipotiroidismo congénito", on=True, lines=["Falta hormona tiroidea; el postérmino es otra pista."])]),
  tabla=("Opciones de la pregunta", [("Galactosemia", False), ("Enfermedad de Gilbert", False), ("Atresia de vías biliares", False),
                                     ("Hipotiroidismo congénito", True)],
         [("Clave", ["Vómitos, hipoglucemia, sepsis", "Leve, en adolescentes", "Acolia, bilirrubina directa", "Hernia, hipotonía, fontanela"])]))


# PED-277 · Varicela complicada con celulitis · MAPA DE SIGNOS (foto real + dibujo)
def _varicela(s, x, y):
    _img_draw(s, x + 49, y, P("varicela.jpg", 196, 252,
                              [("circulo", 0.613, 0.345, 0.07, "vesícula", 0.55, 0.06),
                               ("circulo", 0.38, 0.575, 0.06, "pápula", 0.04, 0.70)],
                              credito="CDC · Wikimedia Commons · dominio público"))
    p = (I.P("M60 10 C100 0 194 0 234 10 L244 110 H50 Z", I.SKIN, I.SKIN_D, 2)
         + I.P("M147 12 L147 108", "none", I.SKIN_D, 1.2, 'stroke-dasharray="3 3"')
         + I.E(104, 38, 30, 18, "#fca5a5", I.RED, 2, 'opacity="0.9"')
         + I.puntos_piel((60, 20, 234, 100), 18, "#be123c", (2, 3.5), 7)
         + I.t(104, 74, "celulitis", I.RED, 11) + I.t(22, 16, "D", I.MUTED, 11, "start") + I.t(272, 16, "I", I.MUTED, 11, "end"))
    I.g(s, x, y + 286, p)


S("mapa_signos", "PED-277", "escolar-exantema-polimorfo-placa-eritematosa-dolorosa-varicela-celulitis",
  "Exantema en distintas etapas y luego placa roja dolorosa: varicela complicada con celulitis",
  "Enfermedades exantemáticas · varicela", ESP,
  ("Varicela y sus complicaciones", ["Exantema pruriginoso en oleadas: máculas, pápulas, vesículas y costras a la vez.",
                                     "La complicación más frecuente es la sobreinfección bacteriana de la piel."]),
  ("Escolar de 8 años", ["Hace 1 semana fiebre 2 días y luego exantema pruriginoso con vesículas y costras.",
                         "Hoy placa roja, elevada y dolorosa en el hemitórax derecho superior."]),
  ["Lesiones en distintas etapas al mismo tiempo = varicela.",
   "Placa roja, caliente y dolorosa sobre las lesiones = celulitis (S. pyogenes o S. aureus): antibiótico.",
   "Si la fiebre vuelve o la placa avanza rápido, pensar en fascitis necrotizante."],
  NELSON + "; AAP, Red Book (2024).",
  d=dict(rotulo="Los signos del niño", PH=500, tag="ESTE CASO",
         ilu_titulo="El exantema y la complicación",
         ilu=_varicela,
         ilu_pie="Arriba: varicela (foto real). Abajo: tórax de frente con celulitis en el lado derecho (esquema).",
         signos=[dict(tit="Fiebre antes del exantema", lines=["Pródromo corto de 1-2 días."]),
                 dict(tit="Lesiones en todas las etapas", lines=["Mácula, pápula, vesícula y costra a la vez."]),
                 dict(tit="Prurito", lines=["El rascado abre la puerta a las bacterias."]),
                 dict(tit="Placa roja, elevada y dolorosa", lines=["Celulitis del hemitórax derecho."]),
                 dict(tit="Causa: varicela + celulitis", on=True, lines=["Sobreinfección por estreptococo o estafilococo."])]),
  tabla=("Opciones de la pregunta", [("Rubeola - empiema", False), ("Exantema súbito - estreptodermia", False),
                                     ("Sarampión - urticaria", False), ("Varicela - celulitis", True)],
         [("Clave", ["Exantema sin vesículas", "Exantema tras bajar la fiebre", "Tos, coriza, conjuntivitis", "Vesículas y costras + placa dolorosa"])]))


# PED-278 · Asma persistente leve · TERMÓMETRO + franja
def _semana(s, x, y):
    dias = ["L", "M", "M", "J", "V", "S", "D"]
    sint = {1, 3, 5}
    p = I.t(0, 14, "Día", I.SLATE, 11, "start") + I.t(0, 74, "Noche", I.SLATE, 11, "start")
    for k, dd in enumerate(dias):
        cx = 70 + k * 44
        on = k in sint
        p += f'<rect x="{cx-18}" y="0" width="36" height="42" rx="6" fill="{I.ORANGE_L if on else "#f8fafc"}" stroke="{O if on else "#cbd5e1"}" stroke-width="1.5"/>'
        p += I.t(cx, 16, dd, I.SLATE, 10.5) + (I.t(cx, 34, "tos", O, 10) if on else "")
        p += f'<rect x="{cx-18}" y="56" width="36" height="30" rx="6" fill="#eef2ff" stroke="#cbd5e1" stroke-width="1.5"/>'
        p += I.t(cx, 76, "duerme", "#4338ca", 8.5, fw=700)
    p += I.t(160, 108, "3 días con síntomas; ninguna noche despierta", I.INK, 11)
    I.g(s, x, y, p)


S("termometro", "PED-278", "nina-7-anos-sibilancias-mas-2-veces-semana-sin-despertares-asma-persistente-leve",
  "Síntomas más de 2 veces por semana, pero no diarios y sin despertares: asma persistente leve",
  "Asma en pediatría · clasificación de gravedad", ESP,
  ("Clasificación del asma (5-11 años)", ["Se mira la frecuencia de síntomas de día y de noche, la limitación y las crisis.",
                                          "El peor dato manda la clasificación."]),
  ("Niña de 7 años con asma", ["En el último mes: tos y sibilancias más de 2 veces por semana, no a diario.",
                               "Sin despertares nocturnos, sin emergencias ni limitación importante."]),
  ["Intermitente: síntomas ≤ 2 días por semana. Persistente leve: > 2 días por semana, pero no diario.",
   "Moderada: síntomas diarios o despertares > 1 por semana. Grave: todo el día y casi todas las noches.",
   "Persistente leve: controlador diario con corticoide inhalado a dosis baja."],
  "NAEPP EPR-3; GINA (2024); " + NELSON + ".",
  d=dict(rotulo="Gravedad del asma y tratamiento",
         niveles=[("Intermitente", "≤ 2 días por semana", ["Noches ≤ 2 al mes", "Sin limitación"]),
                  ("Persistente leve", "> 2 días, no diario", ["Noches 3-4 al mes", "Limitación menor"]),
                  ("Moderada", "Persistente: diario", ["Noches > 1 por semana", "Alguna limitación"]),
                  ("Grave", "Persistente: todo el día", ["Casi todas las noches", "Limitación marcada"])],
         caso_nivel=1, ruta_titulo="Qué se hace", paso_label="ESTE CASO",
         pasos=[(1, "Corticoide inhalado a dosis baja", ["Controlador diario"], True),
                (2, "Salbutamol a demanda", ["Para las crisis"], False),
                (3, "Reevaluar en 1-3 meses", ["Técnica inhalatoria y adherencia"], False)]),
  banda=B("Su semana típica", D(_semana, 380, 116),
          ["Tos y sibilancias 3 días por semana: más de 2, pero no a diario.", "Ninguna noche se despierta.",
           "No faltó al colegio ni fue a emergencia."], ans=0),
  tabla=("Opciones de la pregunta", [("Intermitente", False), ("Persistente moderada", False), ("Persistente grave", False),
                                     ("Persistente leve", True)],
         [("¿Encaja?", ["No: pasa de 2 por semana", "No: no es diario", "No", "Sí"])]))


# PED-279 · Primera convulsión afebril del lactante · EMBUDO + franja
def _tubos(s, x, y):
    it = [("Glucosa", "#fde68a"), ("Sodio", "#bae6fd"), ("Calcio", "#e9d5ff"), ("Magnesio", "#bbf7d0")]
    p = ""
    for k, (nom, col) in enumerate(it):
        cx = 40 + k * 84
        p += (f'<rect x="{cx-12}" y="6" width="24" height="86" rx="10" fill="#ffffff" stroke="#64748b" stroke-width="2"/>'
              + f'<rect x="{cx-10}" y="40" width="20" height="50" rx="9" fill="{col}"/>'
              + f'<rect x="{cx-15}" y="0" width="30" height="12" rx="3" fill="{O if k < 3 else "#94a3b8"}"/>'
              + I.t(cx, 112, nom, I.INK, 11))
    I.g(s, x, y, p)


S("embudo", "PED-279", "lactante-8-meses-primera-convulsion-afebril-sin-focalidad-trastorno-hidroelectrolitico",
  "Primera convulsión sin fiebre ni focalidad en un lactante: buscar un trastorno hidroelectrolítico",
  "Convulsiones en el lactante · primera crisis afebril", ESP,
  ("Primera convulsión afebril del lactante", ["Antes de pensar en epilepsia se descartan causas agudas y corregibles.",
                                               "Glucosa, sodio, calcio y magnesio bajos son frecuentes en el lactante."]),
  ("Lactante de 8 meses", ["Episodio convulsivo; afebril, en estado posictal.",
                           "Fontanela anterior cerrada, sin signos de focalización."]),
  ["Primera crisis afebril sin focalidad: lo más probable es una causa metabólica o hidroelectrolítica.",
   "Pedir glucosa, sodio, calcio y magnesio de inmediato y corregir.",
   "Epilepsia requiere crisis repetidas no provocadas; meningitis suele dar fiebre."],
  NELSON + "; AAP, primera crisis no febril.",
  d=dict(rotulo="De la convulsión a la causa", inicio="Lactante de 8 meses con primera convulsión afebril",
         candidatos=["Meningitis", "Craneosinostosis", "Epilepsia", "Trastorno hidroelectrolítico"],
         pasos=[("¿Fiebre, fontanela abombada o rigidez de nuca?", ["Meningitis"]),
                ("¿Cráneo deformado con suturas fusionadas?", ["Craneosinostosis"]),
                ("¿Crisis repetidas sin causa aguda?", ["Epilepsia"])],
         final=("Trastorno hidroelectrolítico", ["Glucosa, sodio, calcio, magnesio"]),
         nota="Sin fiebre, sin foco y primera crisis: primero descartar una causa metabólica aguda."),
  banda=B("Lo que se pide primero", D(_tubos, 330, 120),
          ["Glucosa: la hipoglucemia es la causa corregible más rápida.", "Sodio y calcio bajos (hiponatremia, hipocalcemia).",
           "Magnesio si el calcio no sube."]),
  tabla=("Opciones de la pregunta", [("Craneosinostosis", False), ("Epilepsia", False), ("Trastorno hidroelectrolítico", True),
                                     ("Meningitis", False)],
         [("¿Encaja?", ["No causa convulsiones", "Es la primera crisis", "Sí", "Sin fiebre"])]))

# PED-280 · Resfríos frecuentes en guardería · CRITERIOS
_moco = I.P("M104 80 Q100 92 104 100", "none", "#38bdf8", 3) + I.P("M116 80 Q120 92 116 100", "none", "#38bdf8", 3)
S("criterios", "PED-280", "nino-2-anos-guarderia-8-resfrios-al-ano-variante-normal",
  "Ocho resfríos al año en un niño que va a guardería: es normal",
  "Infecciones respiratorias · ¿inmunodeficiencia?", ESP,
  ("Infecciones respiratorias frecuentes", ["Un niño sano que va a guardería puede tener 6-8 resfríos al año, o más.",
                                            "Se estudia la inmunidad solo si hay señales de alarma."]),
  ("Niño de 2 años en guardería", ["8 rinofaringitis autolimitadas en 12 meses.",
                                   "Sin hospitalizaciones ni neumonías; padres preocupados."]),
  ["Resfríos leves y autolimitados en guardería: variante normal; explicar y reforzar la higiene respiratoria.",
   "Señales de alarma: ≥ 2 neumonías al año, infecciones graves o por gérmenes raros, falla de crecimiento, antecedente familiar.",
   "No hace falta retirarlo de la guardería ni pensar en asma por los resfríos."],
  "Fundación Jeffrey Modell, 10 señales de alarma; AAP; " + NELSON + ".",
  d=dict(rotulo="¿Hay señales de inmunodeficiencia?", tag="ESTE CASO",
         lista_titulo="Señales de alarma",
         items=[("Dos o más neumonías en un año", False, "Ninguna neumonía"),
                ("Infecciones que necesitan hospitalización o antibiótico EV", False, "Sin hospitalizaciones"),
                ("Infecciones graves o por gérmenes raros", False, "Solo resfríos leves"),
                ("Falla de crecimiento", False, "Previamente sano"),
                ("Antecedente familiar de inmunodeficiencia", None, "No se menciona")],
         umbral="basta 1 señal", veredicto="Sin señales de alarma: resfríos esperables en guardería; higiene respiratoria",
         img_titulo="El niño", img=D(lambda s, x, y: I.nino(s, x + 5, y, extra=_moco, marcas=[(1, 140, 88), (2, 110, 140)], sc=0.8), 230, 310),
         img_pie="1 resfríos leves (rinofaringitis); 2 pulmones sanos, sin neumonías.",
         claves_titulo="Qué decir a los padres",
         claves=[("Es normal", ["6-8 resfríos al año en guardería; el sistema inmune «aprende»."], True),
                 ("No retirarlo", ["No hay enfermedad que lo justifique."], False),
                 ("Volver si", ["Neumonía, dificultad para respirar o fiebre persistente."], False)]),
  tabla=("Opciones de la pregunta", [("6-8 al año es habitual; higiene", True), ("> 4 al año es anormal", False),
                                     ("Minimizar; volver solo si hay fiebre", False), ("Sugiere asma; aislarlo", False)],
         [("Problema", ["Ninguno", "Falso y alarma", "No educa ni previene", "Sin base"])]))

# PED-281 · Espina bífida oculta · COMPARADOR (dibujos)
S("comparador", "PED-281", "lactante-2-meses-hoyuelo-mechon-pelo-lumbosacro-espina-bifida-oculta",
  "Hoyuelo con mechón de pelo lumbosacro y examen normal: espina bífida oculta",
  "Defectos del tubo neural · disrafia espinal", ESP,
  ("Disrafias espinales", ["Abiertas: la médula o las meninges salen a la superficie (mielomeningocele, meningocele).",
                           "Ocultas: piel intacta con marcas en la línea media (mechón, hoyuelo, mancha)."]),
  ("Lactante de 2 meses en control sano", ["Desarrollo y neurológico normales.",
                                           "Hoyuelo con mechón de pelo denso en la línea media lumbosacra; sin masa ni salida de LCR."]),
  ["Mechón de pelo o hoyuelo en la línea media lumbosacra con piel intacta = espina bífida oculta.",
   "Ecografía de columna (antes de los 3-6 meses) para descartar médula anclada.",
   "Seno dérmico: orificio con trayecto que puede drenar o infectarse; meningocele y mielomeningocele: masa visible."],
  NELSON + "; AAP, estigmas cutáneos de disrafia espinal.",
  d=dict(rotulo="Oculta frente a abierta", IH=250, tag="ESTE CASO",
         imgs=[dict(titulo="Espina bífida oculta", on=True, ilu=lambda s, x, y: I.columna_disrafia(s, x + 107, y, "oculta"),
                    pie="Arco vertebral sin cerrar, piel intacta con mechón de pelo; médula en su sitio."),
               dict(titulo="Mielomeningocele", ilu=lambda s, x, y: I.columna_disrafia(s, x + 107, y, "mielomeningocele"),
                    pie="Médula y meninges fuera, en un saco abierto; hay déficit neurológico.")],
         lectura_titulo="Otras opciones",
         lectura=[("Espina bífida oculta", ["Piel intacta, mechón u hoyuelo, examen normal."], True),
                  ("Seno dérmico", ["Orificio con trayecto; puede drenar o dar meningitis."], False),
                  ("Meningocele", ["Masa quística con meninges, cubierta de piel."], False)]),
  tabla=("Opciones de la pregunta", [("Seno dérmico", False), ("Mielomeningocele", False), ("Espina bífida oculta", True), ("Meningocele", False)],
         [("Clave", ["Orificio con trayecto", "Saco abierto, déficit", "Mechón con piel intacta", "Masa quística"])]))

# PED-282 · Dengue con signos de alarma · SEMÁFORO
_rash = I.puntos_piel((72, 110, 148, 230), 40, "#e11d48", (1.8, 3), 3)
S("semaforo", "PED-282", "nina-7-anos-dengue-dolor-abdominal-vomitos-persistentes-hospitalizacion-sala",
  "Dengue con dolor abdominal y vómitos persistentes: signos de alarma, hospitalizar en sala",
  "Enfermedades metaxénicas · dengue en niños", ESP,
  ("Dengue: grupos de manejo", ["A: sin signos de alarma, en casa. B: con signos de alarma, hospitalizar.",
                                "C: dengue grave (shock, sangrado grave, falla de órganos), cuidados intensivos."]),
  ("Niña de 7 años en zona de brote", ["3 días de fiebre alta, cefalea, mialgias y rash.",
                                       "Hace 12 h dolor abdominal difuso y vómitos persistentes (> 3 en 1 hora)."]),
  ["Dolor abdominal intenso y vómitos persistentes son signos de alarma: anuncian fuga de plasma.",
   "Dengue con signos de alarma sin shock: hospitalizar en sala, cristaloides EV y hematocrito seriado.",
   "La fase crítica empieza al bajar la fiebre (días 3-7): vigilar de cerca."],
  "OPS, guía de dengue (2016); " + MINSA + ", norma técnica de dengue.",
  d=dict(rotulo="Imagen del caso y semáforo de conducta",
         ilu_titulo="La niña del caso",
         ilu=ILU(D(lambda s, x, y: I.nino(s, x + 24, y, extra=_rash, marcas=[(1, 110, 200), (2, 110, 88), (3, 150, 130)], sc=0.84), 270, 320)),
         ilu_pie="1 dolor abdominal, 2 vómitos persistentes, 3 rash.",
         check_titulo="¿Qué tiene?",
         check=[("Dolor abdominal intenso", False), ("Vómitos persistentes", False),
                ("Sin shock ni sangrado grave", True), ("Consciente, sin falla de órganos", True)],
         ans=1, tag="ESTE CASO",
         luces=[("Sin signos de alarma (A)", "Casa", ["Hidratación oral, paracetamol; volver si aparecen signos de alarma."]),
                ("Con signos de alarma (B)", "Hospitalizar en sala", ["Cristaloides EV y hematocrito seriado."]),
                ("Dengue grave (C)", "Cuidados intensivos", ["Shock, sangrado grave o falla de órganos."])]),
  tabla=("Opciones de la pregunta", [("UCI pediátrica", False), ("Observar en emergencia", False), ("Hospitalizar en sala", True),
                                     ("Ambulatorio con SRO", False)],
         [("¿Cuándo?", ["Dengue grave", "Insuficiente con signos de alarma", "Signos de alarma: este caso", "Sin signos de alarma"])]))

# PED-283 · Lactancia adecuada en el neonato · ÁRBOL CON IMAGEN
S("arbol_imagen", "PED-283", "neonato-3-dias-perdida-7-peso-diuresis-adecuada-reforzar-lactancia",
  "Neonato de 3 días que perdió 7 % y orina bien: reforzar la lactancia y vigilar el peso",
  "Lactancia materna · pérdida de peso neonatal", ESP,
  ("Pérdida de peso en los primeros días", ["Todo recién nacido pierde peso: se acepta hasta cerca del 10 %.",
                                            "Recupera el peso de nacimiento hacia los 10-14 días."]),
  ("Neonato de 3 días, madre primigesta", ["Perdió 7 %; orina ≥ 4 veces al día, deposiciones amarillas, buena succión.",
                                           "Activo, sin deshidratación; «quiere mamar a cada rato»."]),
  ["Pérdida ≤ 10 % con buena diuresis, deposiciones de transición y buena succión: lactancia eficaz.",
   "Mamar a menudo (8-12 veces al día) es normal: estimula la producción de leche.",
   "Fórmula, extractor o electrolitos no están indicados; reforzar técnica y control de peso en 48-72 h."],
  "OMS/UNICEF, lactancia materna; AAP (2022); " + MINSA + ".",
  d=dict(rotulo="¿La lactancia es eficaz?", tag="ESTE CASO",
         pregunta="Recién nacido que pierde peso: ¿hay signos de lactancia eficaz?",
         ramas=[("No: pérdida > 10 %, poca orina o succión débil", "Evaluar la lactancia y al bebé", ["Observar una toma; electrolitos si hay deshidratación.",
                                                                                                    "Suplementar solo si está indicado."]),
                ("Sí: pierde 7 %, orina bien, succiona bien", "Reforzar la técnica y vigilar el peso",
                 ["Libre demanda, buena posición y agarre.", "Control de peso en 48-72 h."])],
         ilu=lambda s, x, y: I.linea_xy(s, x, y, [(0, 0), (1, -3), (2, -5.5), (3, -7), (4, -6.5), (5, -5), (7, -3), (10, -0.5)],
                                        (0, 10), (-12, 2), "Días de vida", "% del peso al nacer",
                                        bandas=[(-12, -10, "#fecaca", "> 10 %: evaluar"), (-10, 2, "#bbf7d0", "esperable")],
                                        marca=(3, -7, "día 3: -7 %"), W=320, H=180),
         IW=380, IH=240,
         ilu_pie="La curva baja los primeros días y se recupera hacia el día 10; el caso está en la zona verde.",
         luego_titulo="Qué enseñar",
         luego=[("Libre demanda", ["8-12 tomas al día es lo normal."], True),
                ("Posición y agarre", ["Boca bien abierta, labio evertido, areola dentro."], False),
                ("Señales de alarma", ["Poca orina, ictericia intensa, letargia."], False)]),
  tabla=("Opciones de la pregunta", [("Extracción con equipo", False), ("Reforzar técnica y vigilar peso", True),
                                     ("Electrolitos séricos", False), ("Fórmula cada 3 horas", False)],
         [("Problema", ["No hay indicación", "Ninguno", "Sin signos de deshidratación", "Desplaza la lactancia"])]))

# PED-284 · Ahogamiento con hipotermia · ÁRBOL + franja
_frio = {k: "#dbeafe" for k in ("cabeza", "torax", "abdomen", "brazo_d", "brazo_i", "pierna_d", "pierna_i")}
S("arbol", "PED-284", "lactante-ahogamiento-agua-fria-paro-sin-signos-muerte-iniciar-rcp",
  "Lactante sacado de un canal de agua fría, en paro y sin signos de muerte: iniciar RCP ya",
  "Ahogamiento · reanimación pediátrica", ESP,
  ("Ahogamiento con hipotermia", ["El frío protege al cerebro: hay recuperaciones tras paros largos en agua fría.",
                                  "«Nadie está muerto hasta estar caliente y muerto»."]),
  ("Lactante de 6 meses, centro de salud rural", ["Encontrado sumergido en un canal; 45 min de traslado.",
                                                  "Sin respiración ni pulso, muy frío; pupilas algo dilatadas, córneas transparentes, sin rigidez."]),
  ["Sin signos de muerte irreversible (rigidez, livideces fijas, lesiones incompatibles): iniciar RCP de inmediato.",
   "En el ahogamiento la causa es hipóxica: empezar con 5 ventilaciones de rescate y seguir 15:2 (2 reanimadores).",
   "Recalentar mientras se reanima; la desfibrilación solo si hay ritmo desfibrilable."],
  "ERC y AHA, reanimación pediátrica y ahogamiento (2021-2025).",
  arbol=Q("¿Hay signos de muerte irreversible (rigidez, livideces fijas)?", [
      L("Sí", "No iniciar RCP", ["Certificar según norma"]),
      L("No", "INICIAR RCP DE INMEDIATO", ["5 ventilaciones de rescate y luego 15:2", "Recalentar mientras se reanima",
                                           "Referir con RCP continua"], path=True)], path=True),
  banda=B("El lactante del caso", D(lambda s, x, y: I.bebe(s, x + 30, y, _frio, marcas=[(1, 150, 60), (2, 44, 182), (3, 120, 160)], sc=0.9), 250, 300),
          ["Córneas transparentes: no hay signos de muerte.", "Sin rigidez: los brazos se mueven.",
           "Muy frío (hipotermia): el frío protege al cerebro."], ans=0),
  tabla=("Opciones de la pregunta", [("Desfibrilación inmediata", False), ("No iniciar RCP", False), ("Solo ventilación con O₂", False),
                                     ("Iniciar RCP de inmediato", True)],
         [("Problema", ["No hay ritmo desfibrilable documentado", "No hay signos de muerte", "Sin pulso: necesita compresiones",
                        "Ninguno"])]))

# PED-285 · Síndrome nefrótico corticorresistente · CRONOLOGÍA
_edema = I.E(95, 60, 9, 4, "#bfdbfe", "#3b82f6", 1.2) + I.E(125, 60, 9, 4, "#bfdbfe", "#3b82f6", 1.2)
S("cronologia", "PED-285", "sindrome-nefrotico-sin-remision-8-semanas-prednisona-biopsia-renal",
  "Síndrome nefrótico sin remisión tras 8 semanas de prednisona: biopsia renal",
  "Nefrología pediátrica · síndrome nefrótico", ESP,
  ("Síndrome nefrótico en el niño", ["Casi siempre es de cambios mínimos y responde a la prednisona: no se biopsia de entrada.",
                                     "Si no responde (corticorresistente), la biopsia define la lesión y el tratamiento."]),
  ("Niño de 4 años con anasarca", ["Proteinuria masiva, hipoalbuminemia, hiperlipidemia.",
                                   "Prednisona 60 mg/m²/día 6 semanas y luego 40 mg/m² en días alternos; a las 8 semanas sin remisión (80 mg/m²/h)."]),
  ["Sin remisión tras un curso completo de prednisona = corticorresistente: biopsia renal.",
   "La biopsia suele mostrar glomeruloesclerosis focal y segmentaria; el estudio genético se pide junto o después.",
   "Primera línea en corticorresistencia: inhibidores de calcineurina; la ciclofosfamida es para corticodependencia."],
  "KDIGO (2021); IPNA, síndrome nefrótico corticorresistente (2020); " + NELSON + ".",
  d=dict(rotulo="El niño y el tiempo de tratamiento", tag="ESTE CASO",
         ilu_titulo="El niño del caso",
         ilu=ILU(D(lambda s, x, y: I.nino(s, x + 88, y + 4, {"abdomen": "#bfdbfe", "pierna_d": "#dbeafe", "pierna_i": "#dbeafe"},
                                          extra=_edema, marcas=[(1, 146, 58), (2, 110, 200), (3, 150, 320)], sc=0.7), 330, 280)),
         ilu_pie="Anasarca: 1 párpados, 2 abdomen (ascitis), 3 piernas.",
         claves=[("Biopsia renal", ["Corticorresistente: hay que ver la lesión."], True),
                 ("Ciclofosfamida", ["Para corticodependencia, no para resistencia."], False),
                 ("Micofenolato", ["No es la primera línea; va tras la biopsia."], False)],
         eje_titulo="Semanas de prednisona", eje=(0, 12), paso=2, marca=8, unidad="sem",
         eje_nombre="semanas de tratamiento",
         hitos=[(0, 6, "Prednisona 60 mg/m²/día", "fase diaria", False),
                (6, 12, "40 mg/m² en días alternos", "fase alterna", False),
                (0, 4, "Remisión esperada", "la mayoría en 4 semanas", False),
                (8, 10, "Este caso: sin remisión", "biopsia renal", True)]),
  tabla=("Opciones de la pregunta", [("Ciclofosfamida", False), ("Estudio genético", False), ("Micofenolato", False), ("Biopsia renal", True)],
         [("¿Ahora?", ["No: es para dependencia", "Complementa, no reemplaza", "No es primera línea", "Sí"])]))

# PED-286 · Objetivo del CRED · CICLO
_tallimetro = (f'<rect x="196" y="6" width="14" height="366" rx="3" fill="#fef3c7" stroke="#a16207" stroke-width="1.5"/>'
               + "".join(f'<line x1="196" y1="{20+k*18}" x2="{204 if k % 2 else 210}" y2="{20+k*18}" stroke="#a16207" stroke-width="1.2"/>' for k in range(20))
               + I.P("M150 14 H214", "none", "#a16207", 3))
S("ciclo", "PED-286", "control-crecimiento-desarrollo-cred-objetivo-vigilancia-integral",
  "Objetivo del CRED: vigilar de forma integral el crecimiento y desarrollo para actuar a tiempo",
  "Salud del niño · control de crecimiento y desarrollo", ESP,
  ("Control de crecimiento y desarrollo (CRED)", ["Norma técnica del MINSA para niñas y niños menores de 5 años.",
                                                  "Mira todo: crecimiento, desarrollo, alimentación, vacunas y entorno."]),
  ("Pregunta de norma", ["¿Cuál es el objetivo principal del CRED en el primer nivel?"]),
  ["Objetivo: vigilar de manera continua e integral el crecimiento y desarrollo para detectar a tiempo riesgos o alteraciones.",
   "Con lo detectado se hacen acciones de prevención y promoción (consejería, suplementos, vacunas, referencia).",
   "No es un trámite antropométrico ni solo la entrega de suplementos o vacunas."],
  MINSA + ", NTS de control de crecimiento y desarrollo de la niña y el niño menor de cinco años.",
  d=dict(rotulo="El ciclo de cada control", tag="ESTE CASO",
         img_titulo="En cada control",
         img=D(lambda s, x, y: I.nino(s, x + 30, y, extra=_tallimetro, marcas=[(1, 110, 30), (2, 48, 224), (3, 110, 150)], sc=0.86), 280, 330),
         img_pie="1 crecimiento (peso y talla), 2 desarrollo, 3 alimentación y salud.",
         centro="Vigilancia integral", ans=2,
         pasos=[("Evaluar crecimiento", "peso, talla, perímetro"), ("Evaluar desarrollo", "motor, lenguaje, social"),
                ("Detectar a tiempo", "riesgos o alteraciones"), ("Intervenir", "consejería, suplementos, vacunas"),
                ("Seguir", "próximo control o referencia")],
         claves_titulo="Por qué no las otras",
         claves=[("Solo registrar medidas", ["No es un requisito administrativo."], False),
                 ("Solo suplementos y vacunas", ["Son parte, no el objetivo."], False),
                 ("Solo nutrición y examen", ["Olvida el desarrollo y el entorno."], False)]),
  tabla=("Opciones de la pregunta", [("Registrar la curva", False), ("Suplementos y vacunas", False), ("Vigilancia integral y detección", True),
                                     ("Solo evaluación nutricional", False)],
         [("¿Objetivo principal?", ["No: es una herramienta", "No: es una acción", "Sí", "No: es incompleto"])]))

# PED-287 · PTI con sangrado mucoso · TERMÓMETRO + franja
S("termometro", "PED-287", "nina-3-anos-plaquetas-25000-epistaxis-persistente-pti-prednisona",
  "PTI con epistaxis que no cede: prednisona 2 mg/kg/día",
  "Hematología pediátrica · púrpura trombocitopénica inmune", ESP,
  ("Púrpura trombocitopénica inmune (PTI)", ["Destrucción inmune de plaquetas en un niño sano, a menudo tras un virus.",
                                             "Se trata según el sangrado, no solo por el número de plaquetas."]),
  ("Niña de 3 años", ["5 días de petequias y hematomas en piernas; epistaxis que no cede con taponamiento.",
                      "Solo plaquetas bajas (25 000/µL); lámina periférica normal."]),
  ["Sin sangrado o solo piel: observar. Sangrado de mucosas: prednisona (2-4 mg/kg/día, 5-7 días) o inmunoglobulina EV.",
   "Sangrado grave (SNC, digestivo): inmunoglobulina + metilprednisolona + plaquetas.",
   "Con frotis normal y cuadro típico no hace falta mielograma antes de la prednisona."],
  "ASH, guía de PTI (2019); " + NELSON + ".",
  d=dict(rotulo="Nivel de sangrado y tratamiento",
         niveles=[("Sin sangrado", "Solo plaquetas bajas", ["Observar"]),
                  ("Piel", "Petequias, hematomas", ["Observar y educar"]),
                  ("Mucosas", "Epistaxis que no cede", ["Tratar: prednisona"]),
                  ("Grave", "SNC o digestivo", ["Emergencia"])],
         caso_nivel=2, ruta_titulo="Qué se hace", paso_label="ESTE CASO",
         pasos=[(1, "Prednisona 2 mg/kg/día", ["5-7 días y luego suspender"], True),
                (2, "Alternativa: inmunoglobulina EV", ["Sube las plaquetas más rápido"], False),
                (3, "Sangrado grave", ["IgIV + metilprednisolona + plaquetas"], False)]),
  banda=B("Frotis de sangre (esquema)", D(lambda s, x, y: I.frotis(s, x, y, "plaquetas_bajas", sc=1.1), 330, 220),
          ["Glóbulos rojos de forma normal.", "Casi no se ven plaquetas.", "Sin blastos: no parece leucemia."], ans=1),
  tabla=("Opciones de la pregunta", [("Ácido tranexámico", False), ("Prednisona 2 mg/kg/día", True), ("Dexametasona 0,6 mg/kg", False),
                                     ("Metilprednisolona 30 mg/kg", False)],
         [("Comentario", ["Coadyuvante local, no trata la PTI", "Este caso", "Menos usada en niños", "Para sangrado grave"])]))

# PED-288 · Sífilis congénita con madre no tratada · MATRIZ + franja
S("matriz", "PED-288", "recien-nacido-madre-vdrl-sin-tratamiento-sifilis-congenita-penicilina-g-sodica",
  "Recién nacido de madre con sífilis no tratada: penicilina G sódica EV por 10 días",
  "Infecciones congénitas · sífilis", ESP,
  ("Sífilis congénita: manejo del recién nacido", ["Se decide con el tratamiento de la madre, el examen del bebé y sus títulos.",
                                                   "Madre no tratada: el bebé se trata aunque esté sano."]),
  ("Recién nacido a término, asintomático", ["Madre con VDRL 1:32 sin tratamiento.",
                                             "VDRL del recién nacido 1:64 (el doble, no 4 veces)."]),
  ["Madre sin tratamiento = sífilis congénita posible: penicilina G sódica (cristalina) EV por 10 días.",
   "Títulos del bebé ≥ 4 veces los de la madre o examen anormal = probada o muy probable: mismo esquema de 10 días.",
   "La benzatínica en dosis única es solo si la madre fue bien tratada y el bebé está normal."],
  "CDC, guía de ITS (2021); " + MINSA + ", norma de eliminación de sífilis congénita.",
  d=dict(rotulo="Escenario y tratamiento del recién nacido", eje_x="Qué hacer", eje_y="Escenario", caso=(1, 1),
         cols=["Cómo se reconoce", "Tratamiento", "Seguimiento"],
         rows=["Probada o muy probable", "Posible", "Menos probable", "Improbable"],
         cells=[[("Examen anormal", ["o títulos ≥ 4 veces la madre"]), ("Penicilina G EV", ["10 días"]), ("VDRL seriado", ["y LCR"])],
                [("Madre no tratada", ["bebé normal, títulos < 4 veces"]), ("Penicilina G EV 10 días", ["Este caso"]), ("VDRL seriado", ["hasta negativizar"])],
                [("Madre tratada en el embarazo", ["> 4 semanas antes del parto"]), ("Benzatínica 1 dosis", ["IM"]), ("VDRL seriado", ["hasta negativizar"])],
                [("Madre tratada antes del embarazo", ["títulos bajos y estables"]), ("Sin tratamiento", ["o benzatínica si dudas"]), ("VDRL", ["según norma"])]]),
  banda=B("Títulos del caso", D(lambda s, x, y: I.lab_barras(s, x, y, [("Madre", "1:32", 5, False), ("Recién nacido", "1:64", 6, True),
                                                                      ("4 veces la madre", "1:128", 7, False)],
                                                             W=330, xmax=8, titulo="VDRL (diluciones)", ref=None), 330, 130),
          ["La madre nunca recibió tratamiento: basta para tratar al bebé.", "El bebé tiene el doble, no 4 veces: no se considera probada.",
           "Escenario «posible»: penicilina G sódica EV 10 días."], ans=2),
  tabla=("Opciones de la pregunta", [("Ceftriaxona 7 días", False), ("Observar y repetir VDRL", False), ("Penicilina G sódica 10-14 días", True),
                                     ("Benzatínica 1 dosis", False)],
         [("Problema", ["No es de elección", "Deja sin tratar", "Ninguno", "Solo si la madre fue tratada"])]))

# PED-289 · Síndrome hemofagocítico secundario · CRITERIOS
S("criterios", "PED-289", "escolar-infeccion-piel-citopenias-transaminasas-trigliceridos-sindrome-hemofagocitico",
  "Tras una infección: citopenias, transaminasas y triglicéridos altos: síndrome hemofagocítico secundario",
  "Hematología pediátrica · síndrome hemofagocítico", ESP,
  ("Síndrome hemofagocítico (HLH)", ["Activación inmune descontrolada: los macrófagos comen células de la sangre.",
                                     "Secundario a infecciones, tumores o enfermedades reumáticas; es grave."]),
  ("Escolar de 8 años", ["Fiebre 5 días e infección de piel tratada con oxacilina; persiste decaído.",
                         "Leucocitos 2000, plaquetas 40 000, AST 660, ALT 730, triglicéridos 300."]),
  ["Fiebre + citopenias + transaminasas altas + triglicéridos altos tras una infección = sospechar HLH secundario.",
   "Confirmar con los criterios HLH-2004 (5 de 8): pedir ferritina, fibrinógeno, CD25 soluble y médula ósea.",
   "La leucemia y la aplasia no explican los triglicéridos ni las transaminasas; la hepatitis no explica las citopenias."],
  "Criterios HLH-2004 (Histiocyte Society); " + NELSON + ".",
  d=dict(rotulo="Criterios HLH-2004 en el caso", tag="ESTE CASO",
         lista_titulo="Criterios (se necesitan 5 de 8)",
         items=[("Fiebre ≥ 38,5 °C", True, "Fiebre de 5 días"),
                ("Triglicéridos ≥ 265 mg/dL o fibrinógeno bajo", True, "Triglicéridos 300"),
                ("Citopenias en 2 de 3 líneas", False, "Plaquetas 40 000; neutrófilos 1720 y Hb 11 no llegan al corte"),
                ("Esplenomegalia", False, "Sin visceromegalias"),
                ("Ferritina ≥ 500 ng/mL", None, "Falta pedirla"),
                ("Hemofagocitosis en médula ósea", None, "Falta el estudio")],
         umbral="5 de 8 para confirmar", veredicto="Sospecha alta: pedir ferritina, fibrinógeno y médula ósea para confirmar",
         img_titulo="Hemofagocitosis (esquema)", img=D(lambda s, x, y: I.frotis(s, x + 3, y, "hemofagocito", sc=0.75), 230, 156),
         img_pie="Macrófago con glóbulos rojos y plaquetas en su interior.",
         claves_titulo="Por qué no las otras",
         claves=[("Leucemia o aplasia", ["No explican triglicéridos ni transaminasas altos."], False),
                 ("Hepatitis viral", ["No explica las citopenias ni los triglicéridos."], False),
                 ("Lo más probable", ["Síndrome hemofagocítico secundario a la infección."], True)]),
  tabla=("Opciones de la pregunta", [("Leucemia linfoblástica", False), ("Aplasia medular", False), ("Hemofagocítico secundario", True),
                                     ("Hepatitis viral", False)],
         [("¿Explica todo?", ["No", "No", "Sí", "No"])]))
