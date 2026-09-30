import re,sys
from PIL import Image
mod=sys.argv[1]; pick=sys.argv[2:] 
src=open(mod+'.py').read()
names=re.findall(r'^(?:V\("\w+", |A\()"([A-Z]+-\d+)", "([^"]+)"',src,re.M)
if pick: names=[n for n in names if n[0] in pick]
for k in range(0,len(names),8):
    ims=[Image.open(f'shotscb/{n}.png') for _,n in names[k:k+8]]
    W=600; th=[im.resize((W,int(im.height*W/im.width))) for im in ims]
    H=max(i.height for i in th)
    sh=Image.new('RGB',(W*4,H*((len(th)+3)//4)),'white')
    for i,im in enumerate(th): sh.paste(im,((i%4)*W,(i//4)*H))
    sh.save(f'../sh_{mod}_{k//8}.png')
print(len(names))
