# Estudio con evidencia: confianza, Repaso de hoy y tarjetas Cloze

Primera entrega de la mejora del banqueo. Son capas **complementarias**: no cambian preguntas, alternativas, claves, comentarios, flujogramas, puntaje ni el orden de las alternativas.

## Auditoría: qué existía y qué se hizo
| Estrategia | Estado antes | Ahora |
|---|---|---|
| 1. Active Recall | **Ya existía** (interruptor «Active Recall» en la vista de práctica, `main.js`) | Sin cambios |
| 2. Confianza / metacognición | No existía | **Nuevo** (`estudio.js`, `estudio.php`) |
| 3. Repetición espaciada | Existe: SM-2 propio en `flashcards_lib.php` (no FSRS) | **Se mantiene** (un solo planificador). «Repaso de hoy» lo reutiliza |
| 4. Distractores / interrogación elaborativa | No existe (los bancos no traen explicación por alternativa) | Pendiente: requiere contenido validado |
| 5. Cloze | No existía | **Nuevo** (`cloze.js`), sobre las flashcards existentes |
| 6. Interleaving por síndromes | No existe (cada pregunta solo tiene `especialidad`) | Pendiente: requiere etiquetar y validar preguntas |
| 7. Dual coding / resaltado | No existe | Pendiente: requiere palabras clave validadas |

## 1. Confianza al responder (modo estudio)
- Al elegir una alternativa **la respuesta no se revela todavía**: aparece una barra con «Adiviné · Dudaba entre dos · Estoy seguro», «Responder sin indicar» y «No volver a preguntar». Se puede cambiar de alternativa antes de confirmar. Al confirmar, todo sigue como siempre (respuesta, comentario, «Ver flujograma», flashcards, Feynman).
- **No cambia el puntaje.** Solo aparece con cuenta (sin cuenta no habría dónde guardarla) y **no aparece en simulacro**. Si el servidor falla, el banqueo sigue igual.
- Se guarda **por intento** en `intentos_respuesta` (pregunta, letra, acierto, confianza, etiqueta, modo, fecha). El **servidor** compara con la clave del banco y calcula la etiqueta; el navegador no puede falsear ninguna de las dos.

| Resultado | Etiqueta |
|---|---|
| Fallo + «Estoy seguro» | **Falso concepto de alta prioridad** |
| Fallo + adiviné / dudaba / sin indicar | Necesita refuerzo (no se asume una creencia errónea consolidada) |
| Acierto + adiviné | Posible laguna de comprensión |
| Acierto + dudaba | Acierto con dudas |
| Acierto + seguro | Acierto con seguridad (se registra; **no** declara dominio del tema) |

## 2. Repaso de hoy (`#/repaso`, nueva entrada en «Seguimiento»)
Una sola pantalla, con datos reales del propio usuario: **tarjetas vencidas** (calendario SM-2 existente → botón al repaso de flashcards), **preguntas por reforzar** (botón «Practicar» que abre una sesión con esas preguntas, con el flujo normal de práctica), **calibración** (de lo que marcaste «seguro», cuánto acertaste; con n visible y aviso si hay menos de 20 datos) y ajustes (activar/desactivar la pregunta de confianza, borrar el historial).
Regla de prioridad (simple y explicable, **no es FSRS**): una pregunta está pendiente si su último intento tiene etiqueta pendiente y sale cuando la aciertas; orden = peso de la etiqueta (4/3/2/1) + recurrencia (máx. 3); ventana de 180 días; máx. 30.

## 3. Tarjetas Cloze («completar el hueco»)
- En «Convertir en flashcard» aparece una propuesta **«Perla clínica · completar el hueco (Cloze)»** con una frase **literal del comentario docente** que contiene la respuesta correcta, con esa respuesta oculta (`{{c1::…}}`, sintaxis de Anki). **No se inventa nada**: si la respuesta no aparece en el comentario, no hay propuesta (hoy 74,7 % de las 3782 preguntas tienen una; se descartan las frases que citan «alternativa B»).
- El estudiante **revisa, edita y decide**: «Ocultar selección» (varios huecos solo si él los marca), «Quitar todos los huecos», vista previa. Solo se guarda al pulsar «Guardar tarjetas», en el mazo existente, ligada a su pregunta, con fuente. El dorso se arma solo.
- Validación en cliente **y servidor** (`fc_cloze_error`): al menos un hueco, sin huecos vacíos ni anidados, ≥ 15 caracteres visibles y ≤ 70 % oculto. En «Mis flashcards» y en el repaso se ve con el hueco tapado («Completa el hueco»). Exportación CSV: conserva la sintaxis Anki, pero para usarla como Cloze hay que importarla con ese tipo de nota.

## Datos y privacidad
Tabla nueva `intentos_respuesta` (`cuenta.php` ya usa `intentos` para limitar inicios de sesión; **no** se tocó), `ON DELETE CASCADE`. Migración `migraciones/005_intentos_respuesta.up/.down.sql` (el `.down` es destructivo). «Descargar mis datos» incluye `intentos`. Aislamiento por usuario; POST con `X-MQP` y mismo origen; tope de 200 intentos/min.

## Archivos
Nuevos: `estudio.php`, `estudio_lib.php`, `estudio.js`, `estudio.css`, `cloze.js`, `migraciones/005_*`. Modificados (mínimo): `main.js` (la respuesta en modo estudio pasa por `responderEstudio()` y se limpia la barra al cambiar de pregunta), `flashcards.js` (propuesta Cloze y su editor), `flashcards_lib.php` + `cuenta.php` (validación Cloze, exportación), `app/app.js` (ruta y acción `repaso`), `app/index.html`, `feynman_lib.php` (ver abajo).

## Corrección importante en el Tutor Feynman
3 763 de las 3 782 preguntas guardan `opciones` como **lista** (letras A–E por posición). `fy_pregunta()` solo entendía el formato objeto: el tutor recibía las alternativas rotuladas «0–4» y perdía la alternativa elegida. **Corregido** (`feynman_lib.php`) con pruebas sobre las 3 782 preguntas. Sube `feynman_lib.php` junto con esta entrega.

## Pruebas
```
php tests/estudio_test.php             # etiquetas, prioridad, calibración, validación Cloze del servidor (24)
node tests/cloze_test.js               # Cloze sobre las 3782 preguntas reales (22)
python3 tests/estudio_api_test.py      # API: servidor decide acierto/etiqueta, idempotencia, aislamiento, Cloze en servidor, exportación, cascada (36)
node tests/estudio_e2e.js              # navegador real: barra de confianza, Repaso de hoy, Cloze, sin cuenta, móvil, axe (42)
python3 tests/integridad_test.py       # banco, claves, comentarios y flujogramas intactos
```
No probado: dispositivos móviles reales ni lector de pantalla (solo emulación y axe).

## Pendiente / decisiones abiertas
- **FSRS**: no se incorporó (el planificador SM-2 actual funciona; cambiarlo exige migrar el historial de las tarjetas existentes). Recomendado solo si el repaso actual no rinde.
- **Bandeja con preguntas gemelas, interleaving por síndromes, resaltado clínico y tabla de distractores**: requieren etiquetar y validar médicamente las preguntas (no se inventan). Propuesta: piloto con 50–100 preguntas de 2 síndromes.
- La confianza viene activada por defecto en modo estudio con cuenta (1 clic extra por pregunta); se desactiva con «No volver a preguntar» o en Repaso de hoy → Ajustes.
