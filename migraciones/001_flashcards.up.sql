-- Flashcards y su historial de repasos (cuenta.php las crea sola al primer uso; este archivo es la versión manual y reversible)
CREATE TABLE IF NOT EXISTS flashcards (
  id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
  frente TEXT NOT NULL, dorso TEXT NOT NULL, pregunta TEXT NOT NULL DEFAULT '', tema TEXT NOT NULL DEFAULT '',
  especialidad TEXT NOT NULL DEFAULT '', fuente TEXT NOT NULL DEFAULT '', huella TEXT NOT NULL,
  estado TEXT NOT NULL DEFAULT 'nuevo', facilidad REAL NOT NULL DEFAULT 2.5, intervalo INTEGER NOT NULL DEFAULT 0,
  repeticiones INTEGER NOT NULL DEFAULT 0, lapsos INTEGER NOT NULL DEFAULT 0,
  creado INTEGER NOT NULL, ultimo INTEGER NOT NULL DEFAULT 0, proximo INTEGER NOT NULL, UNIQUE (usuario, huella));
CREATE INDEX IF NOT EXISTS ix_fc_cola ON flashcards(usuario, proximo);
CREATE TABLE IF NOT EXISTS repasos (
  id INTEGER PRIMARY KEY AUTOINCREMENT, tarjeta INTEGER NOT NULL REFERENCES flashcards(id) ON DELETE CASCADE,
  usuario INTEGER NOT NULL, t INTEGER NOT NULL, calificacion TEXT NOT NULL, estado_antes TEXT NOT NULL,
  intervalo_antes INTEGER NOT NULL, intervalo_despues INTEGER NOT NULL);
CREATE INDEX IF NOT EXISTS ix_repasos_t ON repasos(usuario, t);
