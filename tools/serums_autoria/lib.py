"""Ayudas para escribir los casos de la Misión SERUMS. Los casos se escriben en Python y se guardan en serums/casos/*.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(__file__), "..", "..", "serums", "casos")
PEND = "Pendiente de revisión clínica"

def O(id, texto, cal, retro, err=None, min=5, g=0, cons=None, flags=None, sig=None, ref=None, req=None, nflag=None, referencia=None, pend=False):
    o = {"id": id, "texto": texto, "calidad": cal, "retro": retro, "min": min}
    if err: o["error"] = err
    if g: o["g"] = g
    if cons: o["cons"] = cons
    if flags: o["flags"] = flags
    if sig: o["sig"] = sig
    if ref: o["ref"] = [{"doc": d, "pag": p} for d, p in ref]
    if req: o["req"] = req
    if nflag: o["bloquea_si"] = nflag
    if referencia: o["referencia"] = referencia
    if pend: o["pendiente"] = True
    return o

def Mo(id, eje, titulo, texto, ops, **kw):
    m = {"id": id, "eje": eje, "titulo": titulo, "texto": texto, "opciones": ops}
    m.update(kw)
    return m

def guardar(caso):
    caso.setdefault("estado_publicacion", PEND)
    os.makedirs(RAIZ, exist_ok=True)
    with open(os.path.join(RAIZ, caso["id"] + ".json"), "w", encoding="utf-8") as f:
        json.dump(caso, f, ensure_ascii=False, indent=1)
