#!/bin/bash
# uso: ./chk.sh content7b  → build, solapamientos, desbordes y hoja de contacto de ese módulo
set -e
python3 build7f.py
python3 overlap7.py | tail -4
rm -rf shots7 && mkdir shots7
node check.cjs out7/flujogramas shots7 | grep -v '^$' | tail -6
node check2.cjs out7/flujogramas | tail -6
rm -f ../sh_$1_*.png; python3 sheet7.py $1
