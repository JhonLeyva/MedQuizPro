from lib import *
def A(id, texto, resp, rel): return {"id": id, "texto": texto, "respuesta": resp, "relevancia": rel}
def T(id, cat, nombre, clasif, just, res, esencial=False, bloqueante=None, cambia=None, critico=False):
    t = {"id": id, "categoria": cat, "nombre": nombre, "clasificacion": clasif, "justificacion": just, "resultado": res}
    if esencial: t["esencial"] = True
    if bloqueante: t["bloqueante"] = True; t["mensaje_bloqueo"] = bloqueante
    if cambia: t["cambia_conducta"] = cambia
    if critico: t["tiempo_critico"] = True
    return t
def LAB(titulo, items): return {"tipo": "lab", "titulo": titulo, "lab": [dict({"prueba": x[0], "valor": x[1]}, **({"etiqueta": x[2]} if len(x) > 2 and x[2] else {}), **({"ref": x[3]} if len(x) > 3 and x[3] else {})) for x in items]}
def TXT(texto): return {"tipo": "texto", "texto": texto}
