#!/bin/bash
# uso: ./chk.sh content7b  → build, solapamientos, desbordes y hoja de contacto de ese módulo
set -e
python3 buildcbf.py --full
python3 overlapcb.py | tail -4
rm -rf shotscb && mkdir shotscb
node check.cjs outcb/flujogramas shotscb | grep -v '^$' | tail -6
node check2.cjs outcb/flujogramas | tail -6
rm -f ../sh_$1_*.png; python3 sheetcb.py $1
