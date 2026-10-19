"""Arma el paquete de los 10 ejemplos de la tanda de mejora (imagen real + tríadas + verificación de encaje).
Uso: python3 build27.py out27ej <IDs> && node check27.cjs out27ej/flujogramas out27ej/png && python3 pack27ej.py"""
import json, os, re, shutil, zipfile

B = "out27ej/pack"
ZIP = "../../MedQuizPro_ejemplo_10_flujogramas_mejorados.zip"
order = json.load(open("out27ej/order.json"))
shutil.rmtree(B, ignore_errors=True)
os.makedirs(f"{B}/flujogramas")
os.makedirs(f"{B}/vistas")
js = open("../site/algoritmos.js").read()


def js_str(t):
    return t.replace("\\", "\\\\").replace('"', '\\"')


for i, archivo, titulo, tipo, tri in order:
    shutil.copy(f"out27ej/flujogramas/{archivo}.svg", f"{B}/flujogramas/")
    shutil.copy(f"out27ej/png/{archivo}.png", f"{B}/vistas/")
    # El nombre del archivo no cambia; solo se actualizan el título y el texto alternativo.
    m = re.search(r'"%s":\s*\{[^}]*\}' % re.escape(i), js)
    assert m and f'flujogramas/{archivo}.svg' in m.group(0), i
    blk = re.sub(r'titulo:\s*"(?:[^"\\]|\\.)*"', 'titulo: "%s"' % js_str(titulo), m.group(0))
    blk = re.sub(r'alt:\s*"(?:[^"\\]|\\.)*"', 'alt: "Flujograma: %s"' % js_str(titulo), blk)
    js = js[:m.start()] + blk + js[m.end():]
open(f"{B}/algoritmos.js", "w").write(js)

LEEME = """MedQuizPro · 10 ejemplos de flujogramas mejorados
==================================================

Qué es
------
Diez flujogramas ya publicados, rehechos con el nuevo estándar antes de aplicar el cambio a 500:
  1. Imagen real (licencia libre, con crédito) en lugar de dibujos que no informan.
     Cada imagen lleva marcas en español que señalan el hallazgo exacto.
  2. Tríada / tétrada / péntada con nombre propio, solo donde la explicación lo pide:
     cada signo dice si está en el caso («EN EL CASO») o no se menciona («NO DESCRITO»).
  3. Todo encaja: se corrigió la insignia numerada que se salía de su nota y la línea
     punteada que cruzaba el título en el diseño de fases. Un verificador nuevo
     (check27.cjs) revisa que nada se salga de su recuadro ni se pise.

Cómo instalar
-------------
Copiar la carpeta flujogramas/ y algoritmos.js sobre los del sitio (los nombres de
archivo no cambian; algoritmos.js solo actualiza el título de estos 10).
En vistas/ hay una imagen PNG de cada flujograma para revisarlos rápido.

Los 10 ejemplos
---------------
{lista}

Imágenes usadas (Wikimedia Commons)
-----------------------------------
- Colangiorresonancia con coledocolitiasis · Hellerhoff · CC BY-SA 3.0 (se borraron flechas y letras rojas del autor)
- Derrame pericárdico, vista subcostal (UOTW 25) · Ben Smith · CC BY-SA 4.0 (se recortó y se borraron íconos del equipo)
- ECG con alternancia eléctrica · Jer5150 · CC BY-SA 3.0 (solo la derivación V1)
- Hematoma epidural, TC axial · Hellerhoff · CC BY-SA 4.0 (recorte)
- Tetralogía de Fallot, esquema rotulado en español · LadyofHats y Pitana · CC BY-SA 4.0 (mitad de Fallot)
- Tumor de Pancoast · Jmarchn · CC BY-SA 3.0 (se borró la letra «P» del autor)
- Síndrome de Horner (Miosis.jpg) · Waster · CC BY 2.5 (franja de los ojos)
- Embarazo tubario por laparoscopía · Hic et nunc · CC BY-SA 3.0
- Encefalopatía de Wernicke, RM FLAIR · Jto410 · CC BY-SA 3.0 (recorte)
- Esquistocitos en la PTT · Hospital Universitario de Berna · CC BY-SA 4.0 (círculos azules del autor)
- Desprendimiento de placenta, pieza quirúrgica · Mikael Häggström · CC0 (sin la regla con texto)
- Neumonía del lóbulo inferior izquierdo · James Heilman · CC BY 3.0 (se borraron el círculo y los textos del equipo)
Las imágenes son de otros pacientes con el mismo hallazgo; así se indica bajo cada una.
"""
lista = "\n".join(f"  {k + 1:2d}. {i} · {t}{'  [con tríada]' if tri else ''}" for k, (i, a, t, _, tri) in enumerate(order))
open(f"{B}/LEEME.txt", "w").write(LEEME.replace("{lista}", lista))
if os.path.exists(ZIP):
    os.remove(ZIP)
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(B):
        for f in sorted(files):
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, B))
print("ok", ZIP, os.path.getsize(ZIP) // 1024, "KB")
