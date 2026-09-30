"""Imágenes reales del bloque ENAM 2026 (tanda a tanda). Lee orig/ y escribe JPG finales."""
from PIL import Image
from prep import guardar

G = lambda f: Image.open("orig/" + f).convert("L")
C = lambda f: Image.open("orig/" + f).convert("RGB")
# Íleo biliar (Hellerhoff, CC BY-SA 4.0): Rx y TC coronal del mismo paciente
guardar(G("ileo_biliar.jpg").crop((0, 0, 478, 432)), "ib_rx.jpg", 478, 85)
guardar(G("ileo_biliar.jpg").crop((548, 455, 960, 803)), "ib_tc.jpg", 412, 85)
# Neumoperitoneo (Bill Rhodes, CC BY 2.0)
guardar(G("neumoperitoneo.jpg").crop((20, 10, 940, 780)), "neumoperitoneo.jpg", 700, 80)
# Seudoquiste pancreático (J. Heilman, CC BY-SA 3.0)
guardar(G("seudoquiste.png").crop((0, 0, 920, 751)), "seudoquiste.jpg", 700, 80)
# Gemelos bicoriales a las 8 semanas (Nevit Dilmen, CC BY-SA 3.0): se recorta el texto del equipo
guardar(G("gemelar_lambda.jpg").crop((0, 0, 491, 290)), "gemelar_lambda.jpg", 491, 85)
# Loxosceles laeta (Mampato, dominio público) y varicela (CDC, dominio público)
guardar(C("loxosceles.jpg").crop((160, 180, 580, 600)), "loxosceles.jpg", 420, 85)
guardar(C("varicela.jpg").crop((0, 100, 500, 744)), "varicela.jpg", 500, 85)
