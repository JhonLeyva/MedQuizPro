-- Intentos de respuesta con confianza (tabla «intentos_respuesta»; «intentos» ya la usa cuenta.php para limitar inicios de sesión) (estudio.php los crea solo al primer uso; este archivo es la versión manual y reversible).
-- No contiene audio ni texto libre: pregunta, letra elegida, acierto, nivel de confianza y etiqueta calculada por el servidor.
CREATE TABLE IF NOT EXISTS intentos_respuesta (
  id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
  pregunta TEXT NOT NULL, elegida TEXT NOT NULL DEFAULT '', correcta INTEGER NOT NULL, confianza TEXT, etiqueta TEXT NOT NULL,
  modo TEXT NOT NULL DEFAULT 'estudio', req_id TEXT, t INTEGER NOT NULL);
CREATE INDEX IF NOT EXISTS ix_intres_u ON intentos_respuesta(usuario, pregunta, t);
CREATE UNIQUE INDEX IF NOT EXISTS ux_intres_req ON intentos_respuesta(usuario, req_id) WHERE req_id IS NOT NULL;
