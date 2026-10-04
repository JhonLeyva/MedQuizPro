#!/bin/bash
# Copia al repo las herramientas, el contenido y las imágenes nuevas de la Entrega 3.
S=$(cd "$(dirname "$0")" && pwd); R=/home/user/MedQuizPro/herramientas/flujo
cd "$S"
cp engine5.py engine7.py engine9.py ilu7.py c28.py build28.py hoja.py indice_img.py pack30ej.py e2e30ej.cjs sync30.sh content30*.py "$R"/
mkdir -p "$R/rev30"; cp rev30/* "$R/rev30/"
cp img/pmc.py img/prep30.py img/dibujos30.py "$R/img/"
for f in img/*.jpg; do b=$(basename "$f"); [ -f "$R/img/$b" ] && cmp -s "$f" "$R/img/$b" && continue; cp "$f" "$R/img/"; done
for f in img/orig/*; do b=$(basename "$f"); [ -f "$R/img/orig/$b" ] || cp "$f" "$R/img/orig/"; done
echo sincronizado
