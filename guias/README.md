# Guías clínicas para «Preguntar a la IA de la Guía»

Aquí van los **documentos oficiales** que la IA podrá citar. Hoy `manifest.json` está vacío: hasta que cargues documentos, la IA solo usa el comentario docente del banco.

1. Copia los PDF en `guias/pdf/` (son públicos: normas técnicas y guías de práctica clínica del MINSA, guías de organismos como OMS, ACOG, GINA, Surviving Sepsis…). Respeta la licencia de cada documento.
2. Descríbelos en `manifest.json` (una ficha por PDF). Todos los campos son obligatorios salvo los marcados (opcional):
```json
{
  "id": "gina-2024", "archivo": "GINA-2024.pdf",
  "titulo": "Global Strategy for Asthma Management and Prevention", "institucion": "Global Initiative for Asthma (GINA)",
  "pais": "Internacional", "tipo": "internacional", "anio": 2024, "version": "Informe 2024",
  "estado": "vigente",
  "url": "https://…", "reemplazada_por": "", "temas": ["asma"], "fecha_consulta": "2026-10-19"
}
```
   - `tipo`: `nacional` o `internacional`. `estado`: `vigente`, `reemplazada` o `retirada` (si es reemplazada, indica `reemplazada_por`).
3. Genera el índice y verifícalo (necesita `pdftotext`):
```
python3 tools/ingestar_guias.py
python3 tools/verificar_indice.py        # comprueba que cada fragmento está en la página que declara
```
4. Sube `guias/indice.json` (y los PDF si quieres que el alumno pueda abrirlos) al hosting. PDF escaneados sin texto necesitan OCR antes.

**Modo espejo MINSA vs. internacional:** ver `comparaciones.json` y `docs/FUNCIONES_NUEVAS.md`.
