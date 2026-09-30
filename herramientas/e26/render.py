import pymupdf, sys
import numpy as np
from PIL import Image
f=sys.argv[1]; pages=sys.argv[2:] 
d=pymupdf.open(f+'.pdf')
rng=[int(x)-1 for x in pages] if pages else range(d.page_count)
for i in rng:
    pix=d[i].get_pixmap(dpi=300)
    a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,3).astype(np.int16)
    mx=a.max(2); mn=a.min(2); sat=mx-mn
    gray=(a.mean(2)).astype(np.uint8)
    out=np.where((sat>45),255,gray).astype(np.uint8)
    Image.fromarray(out).save('img/%s_%03d.png'%(f,i+1))
