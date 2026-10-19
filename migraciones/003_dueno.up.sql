-- Marca de «cuenta del dueño». cuenta.php la añade sola; manual: solo si la columna no existe (SQLite no tiene ADD COLUMN IF NOT EXISTS).
ALTER TABLE usuarios ADD COLUMN dueno INTEGER NOT NULL DEFAULT 0;
