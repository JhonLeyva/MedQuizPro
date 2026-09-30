import pymupdf, sys, numpy as np, io
from PIL import Image, ImageFilter
d=pymupdf.open('p2.pdf')
pages=[int(x) for x in sys.argv[2:]] or range(1,d.page_count+1)
T=int(sys.argv[1])
for n in pages:
    x=d.extract_image(d[n-1].get_images()[0][0])
    im=Image.open(io.BytesIO(x['image'])).convert('RGB')
    a=np.array(im).astype(float)
    g=a.mean(2)
    # watermark: bluish mid-gray -> white
    b=a[:,:,2]-a[:,:,0]
    g=np.where((g>115)&(g<200)&(b>15),255,g)
    im=Image.fromarray(g.clip(0,255).astype(np.uint8)).resize((592*4,835*4),Image.LANCZOS)
    im=im.point(lambda v: 0 if v<T else 255)
    im.save('img/p2_%03d.png'%n)
