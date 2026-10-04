"""Revisión completa del banco por entregas de 500 flujogramas (entrega 1 = los 500 más antiguos, bloques 1-5).
Mismo motor que la tanda de mejora (engine7.build7). Cada flujograma lleva, donde aplique:
clasificación o escala oficial con el caso ubicado (escala=), signos con nombre propio (triada=TR(...)),
imagen real que aporte (banda=B(...) con notas (título, detalle)) y la tabla con las opciones ACTUALES del banco.
El nombre de archivo y la etiqueta de especialidad salen solos (del algoritmos.js publicado y del prefijo del ID)."""
import glob, json, os, re
from c26 import S as _S, D, P, B, Q, L, NELSON, ATLS, HARRISON, WILLIAMS, SCHWARTZ, SABISTON, MINSA
from c27 import DOS, TR

AQUI = os.path.dirname(os.path.abspath(__file__))
F28 = []
BANCO = {}
for _f in glob.glob(os.path.join(AQUI, "../site/bancos/*.json")):
    for _q in json.load(open(_f, encoding="utf-8"))["preguntas"]:
        BANCO[_q["id"]] = _q
_js = open(os.path.join(AQUI, "../site/algoritmos.js"), encoding="utf-8").read()
ARCHIVO = dict(re.findall(r'"([A-Z]+-\d+)":\s*\{[^}]*?imagen:\s*"flujogramas/([^"]+)\.svg"', _js))
ESP = {"CAR": "CARDIOLOGÍA", "CIR": "CIRUGÍA", "END": "ENDOCRINOLOGÍA", "GAS": "GASTROENTEROLOGÍA",
       "GIN": "GINECO-OBSTETRICIA", "HEM": "HEMATOLOGÍA", "INF": "INFECTOLOGÍA", "NEF": "NEFROLOGÍA",
       "NEU": "NEUMOLOGÍA", "NRL": "NEUROLOGÍA", "OFT": "OFTALMOLOGÍA", "PED": "PEDIATRÍA", "PSI": "PSIQUIATRÍA",
       "REU": "REUMATOLOGÍA", "SP": "SALUD PÚBLICA", "TRA": "TRAUMATOLOGÍA", "CB": "CIENCIAS BÁSICAS"}
# Fuentes vigentes que se repiten
GOLD = "GOLD 2025"
GINA = "GINA 2025"
ADA = "ADA Standards of Care in Diabetes 2026"
KDIGO = "KDIGO"
SSC = "Surviving Sepsis Campaign 2021"
AHA = "AHA/ILCOR, guías de reanimación 2025"
OMS = "OMS"
CDC = "CDC"
ESC = "ESC"
ACOG = "ACOG"
FIGO = "FIGO"
AAP = "AAP"
NICE = "NICE"
IDSA = "IDSA"


# Claves que se proponen corregir en el banco (el flujograma ya sigue la corrección): {id: (índice correcto, motivo)}
CORRIGE = {
    "TRA-003": (3, "El palmar menor (palmar largo) no flexiona los dedos y falta en el 15 % de las personas; una herida "
                   "en la palma que impide cerrar el puño secciona los tendones flexores: flexor superficial de los dedos."),
}


def opciones(id_):
    q = BANCO[id_]
    ops = list(q["opciones"].values()) if isinstance(q["opciones"], dict) else list(q["opciones"])
    ci = q["correcta"] if "correcta" in q else "ABCDE".index(q["clave_correcta"].strip()[0])
    if id_ in CORRIGE:
        ci = CORRIGE[id_][0]
    return ops, ci


def S(tipo, id_, titulo, barra, tema, caso, perlas, fuente, op, esp=None, **k):
    """op = ("criterio de la fila", [motivo por opción], {índice: "nombre corto"}) — las opciones salen del banco."""
    crit, razones, cortos = (op + ({},))[:3] if len(op) == 2 else op
    ops, ci = opciones(id_)
    assert len(razones) == len(ops), f"{id_}: {len(razones)} motivos para {len(ops)} opciones"
    cols = []
    for i, o in enumerate(ops):
        t = cortos.get(i, o).strip().rstrip(".")
        assert len(t) <= 48, f"{id_}: opción {'ABCDE'[i]} larga para la tabla, dar nombre corto: {t}"
        cols.append((t, i == ci))
    esp = (esp or ESP[id_.split("-")[0]]) + " ENAM"
    return _S(tipo, id_, ARCHIVO[id_], titulo, barra, esp, tema, caso, perlas, fuente,
              tabla=("Opciones de la pregunta", cols, [(crit, razones)]), _reg=F28, **k)


def PA(archivo, W, marcas=(), credito="", fondo="#000000"):
    """Como P, pero el alto sale de la proporción real del archivo (evita recortes por proporción mal escrita)."""
    from PIL import Image
    w, h = Image.open(os.path.join(AQUI, "img", archivo)).size
    return P(archivo, W, round(W * h / w), marcas, credito, fondo)
