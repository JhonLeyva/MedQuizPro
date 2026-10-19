#!/usr/bin/env python3
"""Extrae las preguntas del PDF «Banco comentado Residentado Médico 2014-2019» (2 columnas)
a un JSON intermedio: enunciado, opciones A-E, clave, comentario original, año y especialidad.

Uso: python3 tools/extraer_residentado.py <pdf> <salida.json>
"""
import json, re, subprocess, sys

# Secciones del índice (página impresa -> PDF = impresa + 13)
SECCIONES = [
    (1, "Anatomía"), (3, "Anestesiología"), (5, "Cardiología"), (19, "Cirugía general"),
    (47, "Dermatología"), (49, "Embriología y genética"), (51, "Endocrinología"),
    (62, "Infectología"), (90, "Gastroenterología"), (99, "Ginecología y Obstetricia"),
    (156, "Hematología"), (161, "Nefrología"), (166, "Neumología"), (178, "Neurología"),
    (189, "Oftalmología"), (191, "Otorrinolaringología"), (194, "Pediatría"),
    (235, "Psiquiatría"), (240, "Reumatología"), (242, "Salud Pública"),
    (270, "Traumatología"), (280, "Urgencias"), (290, "Urología"),
]

def especialidad(pag_impresa):
    esp = None
    for ini, nom in SECCIONES:
        if pag_impresa >= ini:
            esp = nom
    return esp

RUIDO = re.compile(r"(estudiosmyc|diosmyc|^e www\.estud|^Estudios M)", re.I)
FOOT = re.compile(r"^\W*Pág\.?\s*(\d+)\W*$", re.I)
HEAD = re.compile(r"^RM\s?(20\d\d)\s?(EXT\w*)?\s*$", re.I)
OPC = re.compile(r"^([A-E])\s?[\.\)]\s*(.*)$")
RESP = re.compile(r"^Respuest\s?a\s*([A-E])\b", re.I)

# letras con las que el OCR confunde cada opción
VAR = {"A": "A", "B": "B8", "C": "C", "D": "D0OU", "E": "E"}


def separar_opciones(txt):
    """Busca A. B. C. D. E. en orden aunque estén en una misma línea o el OCR cambie D por O/0."""
    pos, ini = {}, 0
    for L_ in "ABCDE":
        m = re.compile(r"(?:^|(?<=[\s\"”.;]))([" + VAR[L_] + r"])\s?[\.\)](?=\s|[A-ZÁÉÍÓÚÑ¿0-9])").search(txt, ini)
        if not m:
            break
        pos[L_] = (m.start(1), m.end())
        ini = m.end()
    out = {}
    letras = list(pos)
    for i, L_ in enumerate(letras):
        fin = pos[letras[i + 1]][0] if i + 1 < len(letras) else len(txt)
        out[L_] = txt[pos[L_][1]:fin].strip()
    return out


def paginas(pdf):
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    w = float(re.search(r"Page size:\s+([\d.]+) x", info).group(1))
    h = float(re.search(r"Page size:\s+[\d.]+ x ([\d.]+)", info).group(1))
    n = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    for p in range(14, n + 1):
        txt = ""
        for x in (0, w / 2):
            txt += subprocess.run(
                ["pdftotext", "-f", str(p), "-l", str(p), "-x", str(int(x)), "-y", "0",
                 "-W", str(int(w / 2)), "-H", str(int(h)), pdf, "-"],
                capture_output=True, text=True).stdout + "\n"
        yield p, txt

def main(pdf, salida):
    lineas, imp = [], 0     # imp = página impresa de la hoja actual (pie «Pág. N»; si falta, la anterior + 1)
    for p, txt in paginas(pdf):
        pie = [int(FOOT.match(l.strip()).group(1)) for l in txt.splitlines() if FOOT.match(l.strip())]
        imp = max(pie) if pie else imp + 1
        for l in txt.splitlines():
            s = l.strip()
            if s and not FOOT.match(s) and not RUIDO.search(s):
                lineas.append((s, imp, p))
    bloques, cur = [], None
    for s, pi, p in lineas:
        m = HEAD.match(s)
        if m:
            cur = {"anio": int(m.group(1)), "ext": bool(m.group(2)), "esp": especialidad(pi), "pag": pi, "pdf": p, "l": []}
            bloques.append(cur)
        elif cur is not None:
            cur["l"].append(s)
    out, descartes = [], []
    for b in bloques:
        L = b["l"]
        # enunciado: desde la línea con número hasta la primera opción A.
        try:
            ia = next(i for i, s in enumerate(L) if OPC.match(s) and OPC.match(s).group(1) == "A")
        except StopIteration:
            descartes.append((b["pag"], "sin opción A", L[:2])); continue
        enun = " ".join(L[:ia])
        mnum = re.match(r"^(\d{1,3})\s*[\.\)]\s*(.*)$", enun)
        num = int(mnum.group(1)) if mnum else None
        if mnum: enun = mnum.group(2)
        opc_txt, resp, com, modo = [], None, [], "opc"
        for s in L[ia:]:
            r = RESP.match(s)
            if r:
                resp = r.group(1).upper(); modo = "pre-com"; continue
            if s.lower().startswith("comentario"):
                modo = "com"; rest = s[len("comentario"):].strip(" :")
                if rest: com.append(rest)
                continue
            if modo == "opc":
                opc_txt.append(s)
            elif modo == "com":
                com.append(s)
        opciones = separar_opciones(" ".join(opc_txt))
        out.append({"anio": b["anio"], "extraordinario": b["ext"], "especialidad": b["esp"],
                    "pag": b["pag"], "pdf": b["pdf"], "num": num, "enunciado": enun.strip(),
                    "opciones": opciones, "clave": resp, "comentario_origen": " ".join(com)})
    json.dump({"preguntas": out, "descartes": descartes}, open(salida, "w", encoding="utf8"),
              ensure_ascii=False, indent=1)
    ok = [q for q in out if len(q["opciones"]) == 5 and q["clave"]]
    print(f"bloques {len(bloques)} · completas {len(ok)} · descartes {len(descartes)}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
