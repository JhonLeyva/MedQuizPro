"""Lista las opciones de más de 48 caracteres de una tanda (para darles nombre corto). Uso: python3 rev28/largas.py NN"""
import json, sys
sys.path.insert(0, ".")
from c28 import opciones
t = int(sys.argv[1])
for i in json.load(open("rev30/entrega3.json"))[t * 25:(t + 1) * 25]:
    ops, _ = opciones(i)
    for k, o in enumerate(ops):
        if len(o.strip().rstrip(".")) > 48:
            print(i, k, o)
