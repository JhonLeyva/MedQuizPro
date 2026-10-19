"""Reduce PNG para revisión: python3 ver.py <archivo_png> [ancho] → scratchpad/v.png"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]); w = int(sys.argv[2]) if len(sys.argv) > 2 else 760
im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
out = "/tmp/claude-0/-home-user-MedQuizPro/7f039d94-22d8-559a-b93c-4ada98cdcd93/scratchpad/v_" + sys.argv[1].split("/")[-1]
im.save(out); print(out)
