#!/bin/bash
# uso: ./chk.sh content7b  → build, solapamientos, desbordes y hoja de contacto de ese módulo
set -e
python3 build8f.py
python3 overlap8.py | tail -4
rm -rf shots8 && mkdir shots8
node check.cjs out8/flujogramas shots8 | grep -v '^$' | tail -6
node check2.cjs out8/flujogramas | tail -6
rm -f ../sh_$1_*.png; python3 sheet8.py $1
