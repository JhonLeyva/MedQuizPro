import subprocess, sys, time, json, io
from PIL import Image
def dl(fname, out, cred, tries=8):
    url="https://commons.wikimedia.org/wiki/Special:FilePath/"+fname
    for k in range(tries):
        r=subprocess.run(["curl","-sSL","-A","MedQuizPro/1.0 (educational; contact github jhonleyva/medquizpro)",url],capture_output=True)
        try:
            i=Image.open(io.BytesIO(r.stdout)).convert("RGB"); break
        except Exception:
            time.sleep(15*(k+1))
    else:
        print("FALLA",fname); return
    if i.width>1000: i=i.resize((1000,round(i.height*1000/i.width)))
    i.save(out,quality=90); json.dump({"credito":cred},open(out+".json","w"),ensure_ascii=False); print(out,i.size)
if __name__=="__main__":
    dl(*sys.argv[1:4])
