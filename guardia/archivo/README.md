# Casos de prueba anteriores (v1) — archivados, no se cargan

`casos_prueba_v1.js` contiene los 8 casos de demostración que tenía el módulo «Sobrevive a la Guardia» antes de la versión 2
(`asma`, `apendicitis`, `eda`, `preeclampsia`, `sepsis`, `iam`, `hpp`, `neumotorax`). Eran contenido de prueba: sus fuentes estaban citadas por nombre,
sin verificar, y la documentación (`docs/FUNCIONES_NUEVAS.md`) los marcaba como pendientes de revisión médica.

- No están en la base de datos: eran un archivo estático. Por eso no hay migración ni se tocó el banco de preguntas, sus respuestas, explicaciones ni flujogramas.
- El progreso de los alumnos (`preferencias.guardia.casos.<id>`) **no se borra**: los ids antiguos siguen guardados y simplemente no se muestran ni cuentan.
- Para restaurarlos (reversible): `git mv guardia/archivo/casos_prueba_v1.js guardia_casos_v1.js`, añadir un `<script>` en `app/index.html` y concatenar `window.MQP_GUARDIA`.
