"""Arma MedQuizPro_bancos_alternativas_corregidas.zip (17 bancos + 3 flujogramas + LEEME + CSV de cambios).
Uso: python3 alt/aplicar.py && python3 alt/svg_chips.py <svgs_viejos> alt/out/flujogramas
     && cp alt/out/bancos/*.json site/bancos/ && python3 alt/pack.py"""
import csv, io, json, os, zipfile
from collections import Counter

ZIP = "../MedQuizPro_bancos_alternativas_corregidas.zip"
cambios = json.load(open("alt/out/cambios.json", encoding="utf-8"))
for c in cambios:
    c[0] = c[0].replace(".json", "")
por_banco = Counter(c[0] for c in cambios)
preguntas = len({c[1] for c in cambios})
claves = [c for c in cambios if c[5]]

csv_buf = io.StringIO()
w = csv.writer(csv_buf)
w.writerow(["banco", "id", "letra", "antes", "ahora", "es_la_correcta"])
for c in cambios:
    w.writerow(c[:5] + ["sí" if c[5] else ""])

L = ["MedQuizPro · Bancos con alternativas corregidas", "=" * 48, "",
     "QUÉ SE HIZO",
     f"- Se cambiaron {len(cambios)} alternativas en {preguntas} preguntas de los 17 bancos (2380 preguntas en total).",
     "- Se quitaron los rellenos: «Faltan datos», «Ninguna de las anteriores», «Todas las anteriores»,",
     "  «Ninguna», «No se puede determinar» y similares.",
     "- También se cambiaron las alternativas absurdas que venían del PDF original",
     "  (por ejemplo «Colonoscopia» en un trauma de cráneo u «Omeprazol» en un tumor de Pancoast).",
     "- Cada alternativa nueva es un distractor creíble para ESE caso clínico: un diagnóstico,",
     "  examen o tratamiento que un alumno podría elegir, pero que no es el correcto.",
     "- La respuesta correcta sigue en la misma letra en todas las preguntas. No se tocó el",
     "  enunciado, la clave, el tema ni el año.", "",
     f"CASOS ESPECIALES ({len(claves)}): se reescribió el texto de la opción correcta"]
for c in claves:
    L.append(f"- {c[1]} ({c[2]}): «{c[3]}» → «{c[4]}»")
L += ["  En las 3 de Ciencias Básicas la correcta era «Ninguna anterior»: se cambió por la respuesta",
      "  explícita y se ajustó la explicación. Las otras 2 son correcciones de redacción.",
      "- Se dejó «Ninguno» en SP-132 porque ahí ES la respuesta correcta (no se vulnera ningún valor).", "",
      "FLUJOGRAMAS",
      "- Solo 3 flujogramas mostraban una alternativa cambiada; vienen corregidos en flujogramas/:",
      "  CIR-075 (Azitromicina → Amoxi-clavulánico y alta), OFT-015 (Dexametasona → Acetazolamida oral,",
      "  ahora descartada por la alergia a sulfas) y PED-088 (Sepsis → Reflujo gastroesofágico).",
      "- Los demás flujogramas no muestran las alternativas cambiadas: no hay que tocarlos.", "",
      "CÓMO INSTALAR",
      "1. En el servidor, reemplaza la carpeta bancos/ por la de este ZIP (los 17 archivos).",
      "2. Copia los 3 archivos de flujogramas/ dentro de la carpeta flujogramas/ (reemplaza).",
      "3. Recarga la página con Ctrl+F5.", "",
      "CAMBIOS POR BANCO"]
for b, n in sorted(por_banco.items()):
    L.append(f"- {b}: {n}")
L += ["", "La lista completa (antes → ahora) está en cambios_alternativas.csv (se abre con Excel).", "",
      "DETALLE (pregunta, letra: antes → ahora)"]
for c in cambios:
    L.append(f"{c[1]} ({c[2]}): {c[3]} → {c[4]}")

if os.path.exists(ZIP):
    os.remove(ZIP)
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir("site/bancos")):
        z.write(f"site/bancos/{f}", f"bancos/{f}")
    for f in sorted(os.listdir("alt/out/flujogramas")):
        z.write(f"alt/out/flujogramas/{f}", f"flujogramas/{f}")
    z.writestr("LEEME.txt", "\n".join(L) + "\n")
    z.writestr("cambios_alternativas.csv", "﻿" + csv_buf.getvalue())
print("ok", ZIP, os.path.getsize(ZIP) // 1024, "KB")
