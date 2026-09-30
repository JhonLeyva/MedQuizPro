import json,sys,collections
sys.path.insert(0,'.')
from rules import CATS,clasif
from ov1 import OV
F='/home/user/MedQuizPro/herramientas/site/bancos/ciencias_basicas.json'
d=json.load(open(F))
res={}
for p in d['preguntas']:
    i=int(p['id'][3:]); c=OV.get(i, clasif(p))
    assert c is not None, p['id']
    res[p['id']]=CATS[c]
c=collections.Counter(res.values())
for k in CATS: print(c[k],k)
json.dump(res,open('clasif.json','w'),ensure_ascii=False,indent=0)
