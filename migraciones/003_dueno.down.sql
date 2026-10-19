-- Requiere SQLite 3.35 o superior. Quita la marca de dueño de todas las cuentas.
ALTER TABLE usuarios DROP COLUMN dueno;
