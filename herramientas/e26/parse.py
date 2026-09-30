import re, glob, json, sys
def load(f):
    t=""
    for p in sorted(glob.glob(f"txt/{f}_*.txt")):
        t+=open(p).read()+"\n"
    return t
def parse(f):
    t=load(f)
    t=re.sub(r"(?m)^\s*(Mejores médicos\.?|www\.villamedicgroup\.com|Página \| ?\d+)\s*$","",t)
    parts=re.split(r"(?m)^\s*PREGUNTA\s+(\S+)\s*$",t)
    out=[]; head=parts[0]
    for i in range(1,len(parts),2):
        num=parts[i]; body=parts[i+1]
        out.append({"src":f,"num":num,"raw":body})
    return head,out
if __name__=="__main__":
    for f in sys.argv[1:]:
        h,o=parse(f); print(f,len(o),repr(h[:200]))
        nums=[x["num"] for x in o]; print(nums[:5],nums[-5:])
        bad=[x for x in nums if not x.isdigit()]; print("nonnum",bad)
        ints=[int(x) for x in nums if x.isdigit()]
        print("missing",sorted(set(range(1,max(ints)+1))-set(ints)), "dups",[k for k in set(ints) if ints.count(k)>1])

OPT=re.compile(r"^\s*([A-E8€])\s*[\.\),:;]\s*(\S.*)$")
KEY=re.compile(r"^\s*(?:CLAVE|RESPUESTA|RPTA)\s*[:;.]?\s*([A-E8€])(?!\w)",re.I)
LET={"8":"B","€":"C"}
def join(lines):
    s=""
    for l in lines:
        l=l.strip()
        if not l: s+="\n"; continue
        if s.endswith("-") and l[:1].islower(): s=s[:-1]+l
        elif s and not s.endswith("\n"): s+=" "+l
        else: s+=l
    s=re.sub(r"\n+","\n",s).strip()
    return s
def split(q):
    L=q["raw"].split("\n")
    stem=[];opts={};cur=None;key=None;rest=[];state="stem"
    for l in L:
        if state in("stem","opt"):
            m=KEY.match(l)
            if m and opts: key=LET.get(m.group(1),m.group(1)); state="com"; continue
            m=OPT.match(l)
            exp="ABCDE"[len(opts)] if len(opts)<5 else None
            if m and exp and LET.get(m.group(1),m.group(1))==exp:
                cur=exp; opts[cur]=[m.group(2)]; state="opt"; continue
            if state=="stem": stem.append(l)
            else:
                if l.strip(): opts[cur].append(l)
        else: rest.append(l)
    com=join(rest)
    pearl=None
    m=re.search(r"VILLAPEPA\s*ENAM\s*:?\s*(.*)$",com,re.S)
    if m: pearl=m.group(1).strip(); com=com[:m.start()].strip()
    com=re.sub(r"^COMENTARIO\s+VILLAMEDIC\s*:?\s*","",com).strip()
    return {"enunciado":join(stem).replace("\n"," "),"opciones":{k:join(v).replace("\n"," ") for k,v in opts.items()},
            "clave":key,"comentario":com,"perla":pearl}
def all_(f):
    _,o=parse(f); res=[]
    for i,q in enumerate(o,1):
        d=split(q); d["src"]=f; d["n"]=i; res.append(d)
    return res
