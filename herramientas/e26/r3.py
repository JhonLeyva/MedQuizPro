import pymupdf, sys, numpy as np, io
from PIL import Image
d=pymupdf.open('p2.pdf')
mode=sys.argv[1]; T=int(sys.argv[2]); out=sys.argv[3]; pages=[int(x) for x in sys.argv[4:]] or range(1,d.page_count+1)
for n in pages:
    x=d.extract_image(d[n-1].get_images()[0][0])
    a=np.array(Image.open(io.BytesIO(x['image'])).convert('RGB')).astype(float)
    if mode=="min": g=a.min(2)
    elif mode=="minb":
        b=np.pad(a,((0,0),(1,1),(0,0)),mode='edge'); b=(b[:,:-2]+b[:,1:-1]+b[:,2:])/3; g=b.min(2)
    im=Image.fromarray(g.clip(0,255).astype(np.uint8))
    im=im.resize((im.width*4,im.height*4),Image.BICUBIC).point(lambda v: 0 if v<T else 255) if T<256 else im.resize((im.width*4,im.height*4),Image.BICUBIC)
    im.save(f'{out}/p2_{n:03d}.png')
