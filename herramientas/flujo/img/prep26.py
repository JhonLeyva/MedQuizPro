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
# Tanda 4. Absceso pulmonar (J. Heilman, CC BY-SA 4.0); TB cavitaria (CDC, dominio público);
# molusco contagioso (Gzzz, CC BY-SA 4.0); bastones de Auer (AFIP, dominio público);
# retinitis por CMV (National Eye Institute, dominio público)
guardar(G("absceso_heilman.png"), "absceso_rx.jpg", 500, 85)
guardar(G("tb_cdc.jpg"), "tb_cavitaria.jpg", 500, 85)
guardar(C("molusco.jpg").crop((120, 180, 640, 860)), "molusco.jpg", 520, 85)
guardar(C("auer.jpg").crop((90, 20, 330, 400)), "auer.jpg", 240, 90)
guardar(C("retinitis_cmv.jpg").crop((140, 60, 760, 560)), "retinitis_cmv.jpg", 620, 85)
# Tanda 5. Vitíligo (J. Heilman, CC BY-SA 3.0); Stevens-Johnson, mucosa (J. Heilman, CC BY-SA 3.0);
# nódulos de Heberden (Drahreg01, CC BY-SA 3.0); neurocisticercosis TC (I. L. Segamwenge, CC BY 4.0);
# ántrax/carbunco (Medicalpal, CC BY-SA 4.0); urticaria (Psixtras, CC0); micosis fungoide (Bobjgalindo, CC BY-SA 4.0)
guardar(C("vitiligo_heilman.jpg"), "vitiligo.jpg", 960, 85)
guardar(C("vitiligo_heilman.jpg").crop((470, 0, 960, 681)), "vitiligo_mano.jpg", 490, 85)
guardar(C("sjs_heilman.jpg").crop((80, 150, 880, 830)), "sjs.jpg", 800, 85)
guardar(C("heberden.jpg"), "heberden.jpg", 960, 85)
guardar(G("ncc_tc.jpg").crop((0, 292, 248, 567)), "ncc_tc.jpg", 248, 90)
guardar(C("carbunco.jpg").crop((150, 100, 900, 700)), "carbunco.jpg", 750, 85)
guardar(C("urticaria.jpg"), "urticaria.jpg", 500, 85)
guardar(C("micosis_rodilla.jpg").crop((0, 40, 960, 680)), "micosis.jpg", 960, 85)
