import json,re,glob
from fix import fix2
import man1
LEAD=[r"^(?:Esto es lo de siempre|Lo de siempre), como vimos en clase:\s*",r"^Como (?:repetimos siempre|insistimos|vimos|lo vimos|dijimos) en clase(?: Villamedic)?,?\s*",
      r"^En clase lo dijimos claro:\s*",r"^Esto lo trabajamos en clase y vuelve:\s*",r"^Esto cae todos los años y lo repetimos:\s*",r"^lo de siempre, como vimos en clase:\s*"]
def clean_com(c):
    c=c.strip()
    for p in LEAD: c=re.sub(p,"",c,flags=re.I)
    c=re.sub(r"\bVillamedic\b\s*","",c)
    return c[:1].upper()+c[1:]
out=[]
# PDF 1
A={}
for l in open('a1.txt'):
    n,e,t=l.rstrip('\n').split('|'); A[int(n)]=(e,t)
for r in json.load(open('p1.json')):
    n=r['n']
    if n in man1.EXC: out.append({"src":"PDF1","n":n,"excluida":man1.EXC[n]}); continue
    ops={k:fix2(v) for k,v in r['opciones'].items()}
    ops.update(man1.OPT.get(n,{}))
    enu=fix2(r['enunciado']); com=clean_com(fix2(r['comentario']))
    for a,b in man1.REP.get(n,[]):
        enu=enu.replace(a,b); com=com.replace(a,b); ops={k:v.replace(a,b) for k,v in ops.items()}
    e,t=A[n]
    out.append({"src":"PDF1","n":n,"esp":e,"tema":t,"enunciado":enu,"opciones":[ops[k] for k in "ABCD"],"clave":r['clave'],"comentario":com})
# PDF 2
txt="\n".join(open(f).read() for f in sorted(glob.glob('t2/*.txt')))
for blk in re.split(r"\n(?=@\d+\|)",txt):
    blk=blk.strip()
    if not blk.startswith("@"): continue
    head,*rest=blk.split("\n")
    n,e,t=head[1:].split("|",2); n=int(n)
    if e=="X": out.append({"src":"PDF2","n":n,"excluida":t}); continue
    d={}
    for l in rest:
        m=re.match(r"^([EABCDKMP]): (.*)$",l)
        if m: d[m.group(1)]=m.group(2).strip()
    com=d["M"]+" "+d["P"]
    out.append({"src":"PDF2","n":n,"esp":e,"tema":t,"enunciado":d["E"],"opciones":[d[k] for k in "ABCD"],"clave":d["K"],"comentario":com})
json.dump(out,open('cand.json','w'),ensure_ascii=False,indent=1)
ok=[x for x in out if 'excluida' not in x]
import collections
print(len(out),len(ok),collections.Counter(x['esp'] for x in ok))
assert all(x['clave'] in 'ABCD' and len(x['opciones'])==4 and all(x['opciones']) for x in ok)
