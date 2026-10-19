"""Ayudantes del banco de Residentado Médico: igual que c28 pero con las preguntas del banco RM
(bancos/residentado/*.json) y etiqueta «RESIDENTADO»."""
import json, os, re, unicodedata
from c26 import S as _S, D, P, B, Q, L, NELSON, ATLS, HARRISON, WILLIAMS, SCHWARTZ, SABISTON, MINSA
from c27 import DOS, TR
import engine
engine.EXAMEN = "RM"

AQUI = os.path.dirname(os.path.abspath(__file__))
FRM = []
BANCO = {q["id"]: q for q in json.load(open(os.environ.get("RM_BANCO", os.path.join(AQUI, "rm_ejemplos.json")), encoding="utf-8"))["preguntas"]}
ESPRM = {"GIN": "GINECO-OBSTETRICIA", "CIR": "CIRUGÍA", "PED": "PEDIATRÍA", "CAR": "CARDIOLOGÍA", "INF": "INFECTOLOGÍA",
         "SP": "SALUD PÚBLICA", "NEU": "NEUMOLOGÍA", "END": "ENDOCRINOLOGÍA", "GAS": "GASTROENTEROLOGÍA", "NRL": "NEUROLOGÍA",
         "TRA": "TRAUMATOLOGÍA", "HEM": "HEMATOLOGÍA", "NEF": "NEFROLOGÍA", "PSI": "PSIQUIATRÍA", "REU": "REUMATOLOGÍA",
         "URG": "URGENCIAS", "UROL": "UROLOGÍA", "ORL": "OTORRINOLARINGOLOGÍA", "OFT": "OFTALMOLOGÍA", "DER": "DERMATOLOGÍA",
         "ANE": "ANESTESIOLOGÍA", "CB": "CIENCIAS BÁSICAS", "GEN": "GENÉTICA", "ANA": "ANATOMÍA"}
GOLD, GINA, ACOG, FIGO, AAP, NICE, IDSA, OMS, CDC, ESC = ("GOLD 2025", "GINA 2025", "ACOG", "FIGO", "AAP", "NICE", "IDSA", "OMS", "CDC", "ESC")


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t)).strip("-")[:90]


def S(tipo, id_, titulo, barra, tema, caso, perlas, fuente, op, **k):
    crit, razones, cortos = (op + ({},))[:3] if len(op) == 2 else op
    q = BANCO[id_]
    ops, ci = q["opciones"], q["correcta"]
    assert len(razones) == len(ops), f"{id_}: {len(razones)} motivos para {len(ops)} opciones"
    cols = []
    for i, o in enumerate(ops):
        t = cortos.get(i, o).strip().rstrip(".")
        assert len(t) <= 48, f"{id_}: opción larga: {t}"
        cols.append((t, i == ci))
    esp = ESPRM[id_.split("-")[1]] + " RESIDENTADO"
    return _S(tipo, id_, id_.lower() + "-" + slug(barra), titulo, barra, esp, tema, caso, perlas, fuente,
              tabla=("Opciones de la pregunta", cols, [(crit, razones)]), _reg=FRM, **k)
