import csv, json, re, glob, os, collections
V=collections.Counter(json.load(open('vocab_bank.json')))
for k,v in json.load(open('vocab.json')).items(): V[k]+=v
def lines(f):
    L=collections.OrderedDict()
    for r in csv.DictReader(open(f), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['level']!='5' or not r['text'].strip(): continue
        k=(r['block_num'],r['par_num'],r['line_num'])
        x,y,w,h=int(r['left']),int(r['top']),int(r['width']),int(r['height'])
        if k not in L: L[k]=[x,y,x+w,y+h,[]]
        e=L[k]; e[0]=min(e[0],x); e[1]=min(e[1],y); e[2]=max(e[2],x+w); e[3]=max(e[3],y+h); e[4].append(r['text'])
    return [(a,b,c,d," ".join(t)) for a,b,c,d,t in L.values()]
def score(t):
    w=re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",t)
    good=sum(1 for x in w if V[x.lower()]>=2 or len(x)<=2)
    bad=len(w)-good
    return good-2*bad
def ov(a,b):
    h=min(a[3],b[3])-max(a[1],b[1]); 
    if h<=0: return 0
    return h/min(a[3]-a[1],b[3]-b[1])
os.makedirs('txtm',exist_ok=True)
tot=collections.Counter()
for fa in sorted(glob.glob('vA/p2_*.tsv')):
    b=os.path.basename(fa)
    LA=lines(fa); LB=lines('vB/'+b); LC=lines('vC/'+b)
    out=[]; prev=None
    for la in LA:
        best=la[4]; bs=score(best); src='A'
        for tag,LX in (('B',LB),('C',LC)):
            cands=[lx for lx in LX if ov(la,lx)>0.6 and min(la[2],lx[2])-max(la[0],lx[0])>0.8*(la[2]-la[0])]
            if len(cands)==1:
                s=score(cands[0][4])
                if s>bs: best,bs,src=cands[0][4],s,tag
        tot[src]+=1
        if prev and la[1]-prev[3]>(la[3]-la[1])*0.9: out.append("")
        out.append(best); prev=la
    open('txtm/'+b.replace('.tsv','.txt'),'w').write("\n".join(out)+"\n")
print(tot)
