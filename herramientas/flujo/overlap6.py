import re, glob
# detecta cajas de nodos (rect con rx=10 y ancho > 100) o hexágonos que se solapen
bad = 0
for f in sorted(glob.glob("out6/flujogramas/*.svg")):
    s = open(f).read()
    boxes = []
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" rx="10"', s):
        x, y, w, h = map(float, m.groups())
        if 100 < w < 900 and h > 40:
            boxes.append((x, y, x + w, y + h))
    for m in re.finditer(r'<polygon points="([^"]+)" fill="#fffbeb"', s):
        pts = [tuple(map(float, p.split(","))) for p in m.group(1).split()]
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        boxes.append((min(xs), min(ys), max(xs), max(ys)))
    boxes = list(set(boxes))
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i], boxes[j]
            ix = min(a[2], b[2]) - max(a[0], b[0]); iy = min(a[3], b[3]) - max(a[1], b[1])
            inside = (a[0] >= b[0] and a[2] <= b[2] and a[1] >= b[1] and a[3] <= b[3]) or (b[0] >= a[0] and b[2] <= a[2] and b[1] >= a[1] and b[3] <= a[3])
            if ix > 2 and iy > 2 and not inside:
                bad += 1; print(f.split("/")[-1], [round(v) for v in a], [round(v) for v in b])
print("solapamientos:", bad)
