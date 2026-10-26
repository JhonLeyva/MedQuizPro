# Tutor Feynman IA

«Explica. Comprende. Corrige. Domina.» El estudiante explica un concepto con sus palabras (voz o texto); un tutor de IA socrático detecta errores y vacíos,
lo guía con preguntas, lo ayuda a reconstruir el concepto y comprueba que lo aplica a un caso nuevo. Módulo **adicional**: no modifica el banco de preguntas,
las claves, los comentarios ni los flujogramas (ver «Integridad del contenido»).

## Dónde se abre
| Punto de entrada | Cómo |
|---|---|
| Retroalimentación de una pregunta | Botón **«Aprender con Feynman»** (junto a «Preguntar a la IA»), solo con la pregunta ya respondida. Envía el id de la pregunta y la alternativa elegida. |
| Visor «Ver algoritmo / Flujograma» | Botón **«Aprender con Feynman»** en el pie del visor (origen `flujograma`; el flujograma no se toca). |
| Sección propia | **Tutor Feynman IA** en la navegación (`app/#/feynman`): tema libre + especialidad, lista de sesiones, retomar y borrar. |

Cada sesión guarda su origen (`pregunta` / `flujograma` / `tema`), el id de la pregunta y la alternativa elegida. El servidor **lee la pregunta del banco por su id**
(`bancos/*.json`, solo lectura): enunciado, alternativas, clave y comentario no los manda el navegador, así que no se pueden falsear. Si ya hay una sesión activa de
la misma pregunta y origen, se retoma en vez de abrir otra.

## Método Feynman: las cinco fases
1 **Explicar** · 2 **Evaluar** · 3 **Preguntas socráticas** · 4 **Reconstruir** · 5 **Aplicar** (caso clínico nuevo). La fase 2 es la evaluación de la explicación
(se completa en el mismo turno en que el estudiante explica).

**El avance lo decide el servidor, no el modelo ni el navegador** (`feynman_lib.php`):
- El modelo propone evaluación y fase; `fy_validar_transicion()` solo la admite si es legal (1→3/4, 3→3/4, 4→4/5, 5→5), si no hay errores abiertos y si el nivel ≥ 3.
  Si no lo es, se reintenta **una vez** con la corrección; si vuelve a fallar, no se guarda nada y el estudiante recibe un error amable (su texto no se pierde).
- **Rúbrica de 4 niveles** (configurable en `feynman_rubrica.json`, opcional): 1 insuficiente · 2 parcial · 3 adecuada · 4 sólida. El nivel 4 solo se otorga en la fase 5
  (aplicación a una situación clínica); una intervención de menos de 80 caracteres no pasa de nivel 2. Los **criterios del tema** (3–6) los genera la IA al abrir la sesión
  y se guardan; el navegador no puede cambiarlos.
- **Ayuda gradual**: 0 pregunta socrática · 1 pista conceptual · 2 pregunta más sencilla · 3 ejemplo clínico · 4 explicación directa. El servidor fija el escalón de cada turno;
  sin progreso sube solo; «Pista» sube uno (máx. 3); «Pedir explicación» lleva directo a la fase 4. Tope de 4 intentos socráticos, 2 reconstrucciones y 2 intentos por caso.
- **«Dominado»** solo si reconstrucción ≥ 3 **y** aplicación ≥ 3 **y** ningún error abierto (`fy_dominio`). Una sola respuesta nunca basta. Lo que no se logró queda como pendiente.
- **Finalizar** solo lo hace el estudiante. Si la fase 5 no se resolvió, la sesión queda `incompleta`, con aviso, y se puede **retomar**; completada, se puede pedir **otro caso**.
- **Voz con ambigüedad**: si por dictado un término decisivo es ambiguo («acidosis» vs «alcalosis»), el tutor pide aclaración; eso **no** consume intentos, no registra errores ni evalúa.

**Contrato de respuesta** (validado en `fy_validar_turno`): `mensaje`, `pregunta_siguiente`, `aclaracion_transcripcion`, `evaluacion{nivel, justificacion, criterios[]}`, `conceptos_correctos`,
`errores[]`, `errores_corregidos[]` (solo ids que estaban abiertos), `omisiones`, `pistas`, `referencias[]` (solo fragmentos realmente entregados), `fase`, `repaso[]`. Tipos, rangos y largos
se comprueban; los marcadores `<<<`/`>>>` se neutralizan; todo lo del estudiante, del banco y de las guías se entrega al modelo como **datos**, nunca como instrucciones.

## Voz
Arquitectura **por turnos** (el estudiante revisa la transcripción antes de enviar) con interfaces intercambiables (`crearEscucha` / `crearHabla` en `feynman_voz.js`): para voz bidireccional en tiempo real
bastaría otro adaptador con la misma interfaz, sin tocar el servidor ni la lógica de fases.
- **Dictado**: `SpeechRecognition` del navegador, `es-PE`. «Escuchando» se muestra solo cuando el navegador confirma que el micrófono está abierto. Iniciar/detener/**cancelar**/reintentar,
  límite de 120 s, un único reconocimiento a la vez, permiso denegado → mensaje con instrucciones y alternativa de texto. Sin soporte (p. ej. Firefox) se escribe; el resto funciona igual.
- **Lectura del tutor**: `speechSynthesis`. Activar/desactivar (se recuerda), pausar/reanudar/detener, velocidad, una sola locución a la vez (las anteriores se invalidan por *token*),
  troceado por frases (evita el corte de Chrome), aviso si el navegador no llega a hablar. El micrófono y la voz nunca están activos a la vez.
- **Estados** (`feynman_estado.js`): preparado para escuchar · escuchando · procesando audio · analizando · reproduciendo · esperando al estudiante · error recuperable · sesión completada.
  Transiciones validadas (no se puede «analizar» sin haber enviado ni «escuchar» mientras suena el tutor). *Analizando* agrupa «analizando» y «generando»: no hay *streaming*, así que no se puede
  distinguir sin fingirlo. Con `prefers-reduced-motion` no hay animaciones.
- **Privacidad**: no se guarda ni se envía audio a MedQuizPlus. **En Chrome y Edge el dictado lo procesa el servicio de voz del fabricante del navegador** (la interfaz lo dice).

## Backend (`feynman.php`, `feynman_lib.php`)
`?a=estado|listar|ver|crear|turno|finalizar|otro_caso|reanudar|tarjetas|borrar`. Sesión de `cuenta.php` (cookie `mqp_sid`) y plan activo (igual que el tutor de IA; 401/402);
POST con cabecera `X-MQP: 1` y mismo origen; **cada consulta filtra por usuario** (ajena = 404). Idempotencia por `req_id` (reenviar no duplica), bloqueo por sesión contra envíos simultáneos (409),
`ignore_user_abort` (una llamada cancelada se guarda completa o no se guarda; la interfaz se resincroniza). Contexto mínimo al modelo: datos del turno + últimos 8 mensajes (no todo el historial).
No se envían nombre ni correo. Guías: se reutiliza `guias_lib.php` (BM25, citas `[G#]` validadas, fichas con institución/año/versión/página); **hoy `guias/` está vacío**, y la interfaz lo dice
(«conocimiento general no verificado»).

### Variables de entorno (las del tutor + opcionales)
| Variable | Para qué |
|---|---|
| `AI_API_KEY` **(obligatoria)** · `AI_PROVIDER` (`gemini`/`openai`/`anthropic`) · `AI_MODEL` · `AI_BASE_URL` | Mismas que `api.php`. Sin llave: la sección dice que no está configurado y no se simula nada (503). |
| `FEYNMAN_AI_MODEL` | Modelo solo para el tutor Feynman. Si no hay modelo: `gpt-4o-mini` (OpenAI), `claude-sonnet-5-5` (Anthropic), `gemini-2.5-flash` (Gemini). |
| `FEYNMAN_LIMITE_MINUTO` (8) · `FEYNMAN_LIMITE_DIA` (150) | Llamadas a la IA por estudiante. Cada llamada se cuenta antes de hacerla (un bucle de la interfaz no gasta de más). |
| `FEYNMAN_PRESUPUESTO_CARACTERES_DIA` (300000) | Presupuesto diario por estudiante (caracteres enviados + recibidos; aproxima tokens, no dinero). |
| `FEYNMAN_TIMEOUT` (50) | Segundos de espera al proveedor. |
También pueden ir en `config.php` (`feynman_*`, ver `config.example.php`). Los secretos nunca salen del servidor.

### Base de datos y migraciones
Tablas `feynman_sesiones`, `feynman_turnos`, `feynman_uso` en `cuenta_datos/mqp.sqlite`; `feynman.php` las crea sola (`IF NOT EXISTS`). Versión manual y reversible:
`migraciones/004_feynman.up.sql` / `.down.sql` (el `.down` es **destructivo**: copia antes el `.sqlite`). `ON DELETE CASCADE`: al eliminar la cuenta se borran sus sesiones.
«Descargar mis datos» (`cuenta.php?a=exportar`) incluye ahora `feynman` (sesiones y transcripciones propias). Se guarda **texto**, nunca audio; el estudiante puede borrar sesiones.

### Instalar y activar
1. Subir los archivos nuevos (`feynman.php`, `feynman_lib.php`, `feynman.js`, `feynman_estado.js`, `feynman_voz.js`, `feynman.css`) y los modificados (`main.js`, `app/app.js`, `app/index.html`, `cuenta.php`, `.htaccess`, `config.example.php`).
2. Definir `AI_API_KEY` (y `AI_PROVIDER`/`AI_MODEL` si no es Gemini) como variable de entorno o en `config.php`. No hay nada más que migrar.
3. Entrar con una cuenta con plan (o de dueño) → **Tutor Feynman IA**. Comprobar `feynman.php?a=estado` → `"ia_lista": true`.

## Tarjetas de repaso
Al finalizar, la IA propone tarjetas **solo sobre lo que el estudiante no logró explicar**. Se muestran para **revisar, editar o descartar**; recién al pulsar «Guardar» se crean con el sistema de flashcards existente
(`cuenta.php?a=fc_crear`, con su repaso espaciado, tema y pregunta de origen). **Nada se guarda solo.** Llevan la fuente «Tutor Feynman IA (generada por IA; revisa antes de guardar)» más la cita de guía si la hubo.

## Integridad del contenido
`python3 tests/integridad_test.py` compara con `tests/integridad_contenido.json` (huellas SHA-256 fijadas **antes** de este módulo): los 17 `bancos/*.json` (3782 preguntas: enunciados, alternativas, claves, comentarios),
`algoritmos.js`, `catalogo.js`, las carpetas `flujogramas/` (3782 archivos), `herramientas/flujo/` y `guias/`. El módulo solo **lee** el banco; no hay ninguna escritura sobre esas rutas.
Cambios en código existente (mínimos): `main.js` (2 botones y su cableado, con el patrón de «Preguntar a la IA»), `app/app.js` (1 ruta), `app/index.html` (enlaces y scripts), `cuenta.php` (clave `feynman` en la exportación), `.htaccess`, `config.example.php`.

## Pruebas
```
php tests/feynman_test.php            # lógica pedagógica: contrato, fases, rúbrica, dominio, informe (79)
node tests/feynman_ui_test.js         # estados, dictado y lectura con SpeechRecognition/speechSynthesis simulados (55)
python3 tests/feynman_api_test.py     # API de punta a punta con IA simulada: acceso, aislamiento, duplicados, concurrencia, límites, informe, tarjetas, borrado (94)
python3 tests/migraciones_test.py     # incluye 004
python3 tests/integridad_test.py      # banco, claves, comentarios y flujogramas intactos
node tests/feynman_e2e.js             # navegador real (Playwright): flujo completo, móvil, accesibilidad; AXE_PATH=…/axe.min.js SHOTS=carpeta (62)
```
**Lo que estas pruebas NO prueban**: ningún proveedor de IA real (se usa un servidor simulado solo en las pruebas; el producto no simula nada), ni un micrófono, un servicio de reconocimiento ni voces del sistema reales
(se simulan las API del navegador), ni lector de pantalla (NVDA/VoiceOver), ni dispositivos móviles reales (solo emulación de Chromium).

## Limitaciones conocidas
- **Calidad médica**: depende del modelo. Los criterios de cada tema y las evaluaciones los produce la IA (con reglas del servidor que limitan avance y «dominado»), **sin revisión médica externa**. Sin guías oficiales cargadas, lo que sale del comentario del banco es lo único contrastado.
- **El tutor no ve la imagen del flujograma**; usa el texto de la pregunta y su comentario (la imagen es un SVG sin texto estructurado accesible). Se guarda su referencia para trazabilidad.
- **Tarjetas**: su respuesta no se valida contra una fuente externa; por eso se revisan antes de guardar y se marcan como generadas por IA.
- **Voz**: depende del navegador (Chrome/Edge/Safari; Firefox no dicta). Calidad y existencia de una voz en español (es-PE/es-419) dependen del sistema. Sin transcripción en el servidor ni voz en tiempo real (preparado en la arquitectura, no implementado).
- **Gemini**: el adaptador usa el modelo de `AI_MODEL`/`FEYNMAN_AI_MODEL` o `gemini-2.5-flash` (no autodetecta como `api.php`); no se probó contra la API real.
- Solo español. Las IP «libres» del dueño de `api.php` no aplican aquí (usa una cuenta de dueño).
- Límites con SQLite en un solo servidor; suficiente para una web pequeña, no para varios servidores sin base compartida.
- **Previos al módulo**: `tests/api_test.py` tiene 5 comprobaciones que ya fallaban (esperan acceso sin plan); la auditoría axe del sitio marca `#chatLauncher` (botón flotante del chat) en todas las páginas.
