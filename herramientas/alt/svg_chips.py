# Ajusta los chips de 3 flujogramas antiguos cuya alternativa cambió (CIR-075, OFT-015, PED-088).
# Uso: python3 alt/svg_chips.py <carpeta_svgs_viejos> <carpeta_salida>
import sys, os, re
SRC, DST = sys.argv[1], sys.argv[2]
RX = (r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="26\.0"[^>]*/>'
      r'<text x="[\d.]+" (y="[\d.]+" font-size="11"[^>]*)><tspan x="[\d.]+" dy="0">{t}</tspan></text>'
      r'(<line x1="[\d.]+" (y1="[\d.]+") x2="[\d.]+" (y2="[\d.]+")[^>]*/>)?')

def find(s, t):
    m = list(re.finditer(RX.format(t=re.escape(t)), s))
    assert len(m) == 1, (t, len(m))
    return m[0]

def build(m, x, w, t):
    r = m.group(0)
    r = re.sub(r'^<rect x="[\d.]+"', f'<rect x="{x:.1f}"', r)
    r = re.sub(r'width="[\d.]+"', f'width="{w:.1f}"', r, count=1)
    r = re.sub(r'<text x="[\d.]+"', f'<text x="{x+w/2:.1f}"', r)
    r = re.sub(r'<tspan x="[\d.]+" dy="0">[^<]*', f'<tspan x="{x+w/2:.1f}" dy="0">{t}', r)
    if m.group(5):
        r = re.sub(r'<line x1="[\d.]+"', f'<line x1="{x+22:.1f}"', r)
        r = re.sub(r' x2="[\d.]+"', f' x2="{x+w-10:.1f}"', r)
    return r

def cambia(s, viejo, nuevo, w):
    m = find(s, viejo); x = float(m.group(1))
    return s[:m.start()] + build(m, x, w, nuevo) + s[m.end():]

def rep(s, old, new):
    assert s.count(old) == 1, (old[:80], s.count(old))
    return s.replace(old, new)

# ancho = texto medido a 11 px + relleno (22 chip superior, 26 chip descartado)
s = open(f'{SRC}/punetazo-boca-nudillo-tendon-capsula-lavado-quirurgico.svg', encoding='utf-8').read()
s = cambia(s, 'Azitromicina', 'Amoxi-clavulánico y alta', 128.4 + 22)
s = cambia(s, '✕ Azitromicina', '✕ Amoxi-clavulánico y alta', 130.0 + 26)
open(f'{DST}/punetazo-boca-nudillo-tendon-capsula-lavado-quirurgico.svg', 'w', encoding='utf-8').write(s)

s = open(f'{SRC}/neonato-sonda-no-pasa-atresia-esofagica.svg', encoding='utf-8').read()
s = cambia(s, 'Sepsis', 'Reflujo gastroesofágico', 125.3 + 22)
s = cambia(s, '✕ Sepsis', '✕ Reflujo gastroesofágico', 127.0 + 26)
open(f'{DST}/neonato-sonda-no-pasa-atresia-esofagica.svg', 'w', encoding='utf-8').write(s)

s = open(f'{SRC}/glaucoma-agudo-asma-alergia-sulfas-manitol.svg', encoding='utf-8').read()
s = cambia(s, 'Dexametasona', 'Acetazolamida oral', 100.3 + 22)
# la acetazolamida es sulfonamida: su chip descartado pasa al paso 2, junto a la dorzolamida
dex = find(s, '✕ Dexametasona'); dor = find(s, '✕ Dorzolamida')
y_dor = float(dor.group(2)); x_new = float(dor.group(1)) + float(dor.group(3)) + 6
nuevo = build(dex, x_new, 84.2 + 26, '✕ Acetazolamida')
nuevo = re.sub(r'(<rect x="[\d.]+") y="[\d.]+"', rf'\1 y="{y_dor:.1f}"', nuevo)
nuevo = re.sub(r'(<text x="[\d.]+") y="[\d.]+"', rf'\1 y="{y_dor+17.5:.1f}"', nuevo)
nuevo = re.sub(r'y1="[\d.]+"', f'y1="{y_dor+13.5:.1f}"', nuevo)
nuevo = re.sub(r'y2="[\d.]+"', f'y2="{y_dor+13.5:.1f}"', nuevo)
s = s[:dex.start()] + s[dex.end():]
dor = find(s, '✕ Dorzolamida')
s = s[:dor.end()] + nuevo + s[dor.end():]
s = rep(s, '<tspan x="320.0" dy="17">lento; el corticoide no baja la</tspan><tspan x="320.0" dy="17">PIO</tspan>',
           '<tspan x="320.0" dy="17">lento: tarda horas en bajar</tspan><tspan x="320.0" dy="17">la PIO</tspan>')
open(f'{DST}/glaucoma-agudo-asma-alergia-sulfas-manitol.svg', 'w', encoding='utf-8').write(s)
print('ok 3 svgs')
