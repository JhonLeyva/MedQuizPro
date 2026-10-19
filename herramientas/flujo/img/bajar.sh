#!/bin/sh
# Descarga las imágenes originales (licencia libre, Wikimedia Commons) a flujo/img/orig/
# Uso: sh bajar.sh   (desde herramientas/flujo/img)
mkdir -p orig
b() { curl -sSL -A "MedQuizPro/1.0 (educational)" -o "orig/$1" "https://commons.wikimedia.org/wiki/Special:FilePath/$2?width=$3"; }
b rx_neumotorax_der.jpg "Rt_sided_pneumoD.jpg" 1000
b rx_tubo_toracico.png "ChesttubeforRtPneumo.png" 910
b rx_neumotorax_der2.png "09-01-Pneumothorax.png" 952
b ecg_tsv_d2.jpg "SVT_Lead_II.JPG" 1592
b ecg_tsv_d2b.jpg "SVT_Lead_II-2.JPG" 564
b koplik.jpg "Koplik_spots,_measles_6111_lores.jpg" 490
b sarampion_exantema.jpg "Measles_rash_PHIL_4497_lores.jpg" 700
ls -la orig
