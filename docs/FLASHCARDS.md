# Flashcards y repaso espaciado

**Qué hace.** En la retroalimentación de cada pregunta (banco, y simuladores durante la revisión) y en el visor de flujograma
aparece «Convertir en flashcard». Abre un panel con 1 o 2 tarjetas editables; el alumno marca cuáles guardar. «Mis Flashcards»
(`app/#/flashcards`) lista, edita, borra, exporta a CSV (compatible con Anki) y ofrece el repaso.

**De dónde sale el contenido.** Solo del banco: enunciado, respuesta correcta y comentario docente de la pregunta. No hay IA
ni fuentes externas en esta versión, y no se inventa contenido médico. La tarjeta «Mi error frecuente» solo aparece si el alumno
falló, y reutiliza la misma explicación del banco.

**Repaso.** Planificador propio en `flashcards_lib.php` (variante de SM-2 con pasos de aprendizaje; tabla de intervalos en el
encabezado del archivo). No es FSRS: FSRS necesita pesos entrenados con repasos reales. El servidor calcula las fechas y los
intervalos que muestran los botones (Otra vez / Difícil / Bien / Fácil). Una tarjeta nueva nunca cuenta como conocida.

**Datos (`cuenta_datos/mqp.sqlite`, creadas automáticamente, nada se borra ni se altera):**
`flashcards` (tarjeta, origen `pregunta`, `fuente`, estado, facilidad, intervalo, repeticiones, lapsos, creado, último, próximo;
única por usuario + huella pregunta/frente) y `repasos` (historial: fecha, calificación, intervalo antes/después).
Ambas tienen `ON DELETE CASCADE`: borrar la cuenta borra sus tarjetas. «Descargar mis datos» las incluye.

**API (`cuenta.php`, exige sesión):** `fc_crear`, `fc_listar`, `fc_cola`, `fc_repasar`, `fc_editar`, `fc_borrar`, `fc_exportar`.
Límites: 8 tarjetas por envío, 3000 por cuenta; un doble clic no cuenta dos repasos (control con `ultimo`).

**Pruebas.** `php tests/flashcards_test.php` (planificador, huella). La API y la interfaz se probaron con Playwright.

**Pendiente.** Generar tarjetas con IA (necesita la llave del tutor y revisión del resultado), vincular tarjetas a guías.
