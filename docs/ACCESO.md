# Acceso cerrado: solo el dueño y quien pague

Por defecto el sitio está **abierto** (nada cambia). Con `'cerrado' => '1'` en `config.php` (o la variable `MQP_CERRADO=1`):

- **Dueño:** tu cuenta marcada como dueña entra a todo sin pagar.
- **Los demás:** pueden registrarse, pero hasta tener un plan activo (pagado) solo ven Ingresar, Registro y Planes. No se descarga ningún banco, y el servidor tampoco se los entrega.
- **Contenidos protegidos** (pasan por `acceso.php` gracias al `.htaccess`): `bancos/`, `flujogramas/`, `herramientas/`, `residentado/`, `guardia/`, `consulta/`, `serums/`, `atlas3d/`, los `*_casos.js`, `algoritmos.js` y los PDF de la raíz. Sin sesión responde 401 y con sesión sin plan, 402.
- El tutor de IA y Feynman ya exigían cuenta y plan; `cuenta.php` (registro, ingreso y los avisos de cobro de las pasarelas) sigue accesible.

## Archivo `acceso_cerrado.flag`
Si existe en la raíz del sitio y `config.php` no define `'cerrado'`, el sitio queda **cerrado**. Un `'cerrado' => '0'` (o `MQP_CERRADO=0`) en `config.php` lo abre aunque el archivo exista; borrar el archivo también lo abre. Así se puede cerrar desde el repositorio sin tocar `config.php`.

## Cómo activarlo (en este orden)
1. Entra con tu cuenta, abre **Perfil → «Soy el dueño del sitio»** y escribe tu clave de administración (`admin_token`). Debe decir «Cuenta del dueño».
2. Comprueba que el cobro funciona (PayU o Mercado Pago configurados). Si no, nadie podrá pagar.
3. En `config.php` del hosting pon `'cerrado' => '1'`.
4. Verifica en una ventana de incógnito: `https://TU-SITIO/bancos/cardiologia.json` debe mostrar `{"ok":false,"acceso":"sin_sesion",…}`. Si muestra las preguntas, el hosting no aplicó las reglas de `.htaccess` (mod_rewrite) y el cierre no protege los archivos directos: vuelve a `'cerrado' => '0'` y avisa.
5. Para volver al acceso abierto: `'cerrado' => '0'`.

## Límites
- La página pública (`index.html`) sigue visible, pero su práctica gratuita usa los bancos y dejará de cargarlos con el acceso cerrado.
- Quien pague obtiene el plan por el flujo de cobro existente; un plan solo se activa desde el aviso verificado de la pasarela.
- Quien ya tenga una copia de los archivos (por ejemplo, porque el repositorio de GitHub es público) no queda cubierto: el repositorio debe pasarse a privado para proteger el contenido allí.
- `tests/acceso_test.js` y `tests/acceso_e2e.js` prueban la puerta y la interfaz con un router que imita el `.htaccess`; el `.htaccess` real solo se puede comprobar en el hosting.
