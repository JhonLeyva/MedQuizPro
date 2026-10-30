# Misión SERUMS: sobrevive a la posta

Estación de simulación de medicina rural y comunitaria dentro del centro «Sobrevive a la Guardia». Ruta `#/serums` y `#/serums/<caso>`, tarjeta en el centro de simulación. No modifica los demás simuladores (solo se añadió la cuarta tarjeta del centro y su estilo).

## Arquitectura
| Pieza | Archivo | Papel |
|---|---|---|
| Motor puro (sin DOM ni azar) | `serums_nucleo.js` | Estado clínico determinista, reloj simulado separado del real, inventario con consumo, referencia con restricciones (vía bloqueada, sin ambulancia), eventos contextuales, taxonomía de errores, puntuación, validadores, recuperación documental, progreso y base de campaña. |
| Interfaz | `serums.js`, `serums.css` | Portada, introducción, panel de la posta, expediente con ocho pestañas, decisiones, informe A–H, registro de evidencia. |
| Casos | `serums/casos/s01…s10.json` (se escriben en `tools/serums_autoria/`) | Datos; se empaquetan en `serums_casos.js` con `python3 tools/serums_empaquetar.py` (`--check` verifica). |
| Evidencia | `serums/evidencia.json`, `serums/manifiesto.json`, `serums/indice.json` | Registro de fuentes con vigencia; índice de fragmentos con página generado con `tools/ingestar_guias.py --manifest serums/manifiesto.json --pdfs <carpeta> --salida serums/indice.json`. El índice es independiente del de la IA tutora existente. |
| Pruebas | `tests/serums_test.js`, `tests/serums_e2e.js` | Unitarias del motor y de los datos; Playwright con axe (claro y oscuro), móvil y teclado. |

## Introducción (tormenta en la sierra)
`serums.js` dibuja sobre la foto (`guardia/portadas/serums-intro.webp`, ilustración generada con IA) un lienzo en las mismas coordenadas de la imagen: lluvia en dos capas, salpicaduras en los impermeables y en el camino, focos de la posta que suben y bajan de intensidad y relámpagos ramificados. El audio `serums/audio/tormenta.mp3` (30 s, lluvia y cuatro truenos) se sintetiza con `python3 tools/serums_audio.py`; es periódico, así que se repite sin cortes, y los relámpagos siguen los instantes de sus truenos (`RELAMPAGOS` en `serums.js` y `TRUENOS` en el script). Si el navegador bloquea el audio sin gesto aparece «Activar sonido»; hay botón para silenciar. Con «reducir movimiento» solo se dibuja un fotograma. El audio es una recreación sintetizada, no una grabación real.

## Reglas del motor
- Cada decisión tiene una calidad (óptima, aceptable, incorrecta, peligrosa) y, si no es óptima, un tipo de error (omisión, comisión, demora, seguridad del paciente, recursos, comunicación, normativo).
- Puntaje de 100: decisión clínica 35, seguridad 25, recursos 15, referencia y comunicación 15, enfoque comunitario y cierre 10. Si un eje no aparece en el caso, su peso se reparte entre los demás. Un error crítico (opción peligrosa) limita el total a 74.
- Bandas: 90–100 Excelente, 75–89 Sólido, 60–74 En desarrollo, menos de 60 Necesita reforzar.
- Las opciones que necesitan insumos se bloquean si el almacén no los tiene; el consumo se descuenta del inventario persistente de la posta (navegador). «Reponer almacén» lo restablece.
- Durante el caso no se corrige: el alumno ve el paso del tiempo, los insumos usados y los eventos; la explicación llega en el informe.

## Evidencia y vigencia
El registro (`serums/evidencia.json`) distingue «Normativa vigente verificada», «Documento en revisión» y «Referencia histórica». «Verificada» significa que el documento existe en el portal oficial y que, en las normas consultadas hasta la fecha del registro, no se encontró una norma que lo derogue. La plataforma **no se actualiza sola**: la revisión periódica es humana (al menos trimestral y ante normas nuevas) y cada cambio se anota en el historial del registro.

Verificado el 30-oct-2026 en gob.pe: GPC INS N° 03-2025 (trastorno hipertensivo del embarazo), NTS 211 dengue (RM 175-2024), NTS 221 tuberculosis (RM 894-2024), NTS 242 cadena de frío (RM 074-2026, solo la resolución), NTS 249 cartera de servicios (RM 625-2026), NTS 213 anemia (aprobada por RM 251-2024 y modificada por RM 429-2024), NTS 196 esquema de vacunación (RM 884-2022, modificada), NTS 238 CRED, NTS 240 ITS. **No verificadas**: NTS 246 / RM 561-2026 (no se encontró), Guía Técnica 006-INS/CETS-2026 de HTA y NTS 247 sarampión (existencia referida por búsqueda y notas, sin abrir el documento primario). Esos tres figuran como «Documento en revisión» y no se usan en ningún caso.

Cada opción de un caso solo cita (documento, página) si esa página existe en el índice; el validador lo comprueba. Sin cita, el informe dice «pendiente de validación científica».

## Estado de los casos
Los diez casos son originales y ficticios, tienen 5 decisiones y están en estado **Pendiente de revisión clínica**. Ninguno es definitivo. Documentos que respaldan: caso 1 (referencia), 2 (GPC INS 03-2025), 3 (NTS 211), 6 (NTS 221), 8 (RM 074-2026). Los casos 4, 5, 7, 9 y 10 no tienen aún una fuente peruana verificada e indexada y lo declaran. Ninguna opción contiene dosis.

## Límites declarados
- **Evaluación en el navegador.** Los casos, con sus calidades de respuesta, se descargan al cliente; un usuario técnico podría leer o alterar el resultado. El puntaje es formativo y no alimenta rankings ni certificaciones. Para evaluación certificante habría que mover la corrección a un endpoint del servidor (el motor es puro y se puede portar), lo que no está hecho.
- **Supervisor documental.** Es una búsqueda BM25 sobre fragmentos reales con su página; no es IA generativa. Si más adelante se conecta una IA, debe limitarse a esos fragmentos.
- **Campaña de 30 días.** Solo existe la estructura (`campanaNueva`, `campanaCerrarDia`) con inventario y reputación persistentes entre días; faltan los guiones.
- La fotografía de portada es una ilustración generada con IA, declarada en pantalla; no son imágenes clínicas.
- Pendiente: revisión clínica de los diez casos; verificar NTS 246, GT 006-INS/CETS-2026 y NTS 247; indexar el anexo de la NTS 242; fuentes para diarrea, trauma, desabastecimiento, adolescente y brotes; comparar con guías internacionales cuando difieran (regla del proyecto: se citan ambas si coinciden y, si no, se declara la discrepancia).
