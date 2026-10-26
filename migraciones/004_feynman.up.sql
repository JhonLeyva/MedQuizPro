-- Tutor Feynman IA: sesiones, turnos y registro de uso de la IA (feynman.php las crea solo al primer uso; este archivo es la versión manual y reversible).
-- Las sesiones y sus turnos se borran con la cuenta (ON DELETE CASCADE). No se guarda audio, solo el texto de cada intervención.
CREATE TABLE IF NOT EXISTS feynman_sesiones (
  id TEXT PRIMARY KEY, usuario INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
  origen TEXT NOT NULL, pregunta_id TEXT NOT NULL DEFAULT '', elegida TEXT NOT NULL DEFAULT '', flujograma TEXT NOT NULL DEFAULT '',
  tema TEXT NOT NULL, especialidad TEXT NOT NULL DEFAULT '', estado TEXT NOT NULL DEFAULT 'activa', fase INTEGER NOT NULL DEFAULT 1,
  datos TEXT NOT NULL, procesando_hasta INTEGER NOT NULL DEFAULT 0, creado INTEGER NOT NULL, actualizado INTEGER NOT NULL, finalizado INTEGER NOT NULL DEFAULT 0);
CREATE INDEX IF NOT EXISTS ix_fy_ses ON feynman_sesiones(usuario, actualizado);
CREATE TABLE IF NOT EXISTS feynman_turnos (
  id INTEGER PRIMARY KEY AUTOINCREMENT, sesion TEXT NOT NULL REFERENCES feynman_sesiones(id) ON DELETE CASCADE,
  n INTEGER NOT NULL, rol TEXT NOT NULL, texto TEXT NOT NULL, via TEXT NOT NULL DEFAULT 'texto', fase INTEGER NOT NULL,
  accion TEXT NOT NULL DEFAULT 'responder', req_id TEXT, meta TEXT NOT NULL DEFAULT '{}', creado INTEGER NOT NULL, UNIQUE (sesion, n));
CREATE UNIQUE INDEX IF NOT EXISTS ux_fy_req ON feynman_turnos(sesion, req_id) WHERE req_id IS NOT NULL;
CREATE TABLE IF NOT EXISTS feynman_uso (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER NOT NULL, t INTEGER NOT NULL, chars INTEGER NOT NULL DEFAULT 0);
CREATE INDEX IF NOT EXISTS ix_fy_uso ON feynman_uso(usuario, t);
