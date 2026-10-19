# Migraciones

`cuenta.php` crea y actualiza sus tablas solas (con `IF NOT EXISTS`), así que normalmente no hace falta ejecutar nada. Estos archivos son la
versión **manual y reversible** de cada cambio de esquema, para auditoría o para deshacerlo:

```
cp cuenta_datos/mqp.sqlite cuenta_datos/mqp.sqlite.copia      # SIEMPRE antes
sqlite3 cuenta_datos/mqp.sqlite < migraciones/001_flashcards.down.sql   # deshacer (borra datos de esa función)
sqlite3 cuenta_datos/mqp.sqlite < migraciones/001_flashcards.up.sql     # volver a crear
```
Las migraciones `.down.sql` que borran datos (001) están marcadas como DESTRUCTIVAS: no las ejecutes sin autorización del dueño y sin copia.
Prueba automática: `python3 tests/migraciones_test.py`.
