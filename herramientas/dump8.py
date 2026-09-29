import json,sys
d=json.load(open('nuevos8.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for i,q in enumerate(d[a:b],a):
    ops=" | ".join(("*" if j==q['correcta'] else "")+"ABCDE"[j]+") "+o for j,o in enumerate(q['opciones']))
    print(f"#{i} {q['id']} [{q['tema']}]\n{q['enunciado']}\n{ops}\nEXP: {q['explicacion'][:200]}\n")
