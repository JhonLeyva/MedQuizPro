# Planes, cuentas y cobro

## Precios (en soles, pago único por periodo)
| Plan | Precio | Por mes |
|---|---|---|
| Gratis | S/ 0 | — |
| Premium mensual | S/ 29 | S/ 29 |
| Premium trimestral (el más elegido) | S/ 69 | S/ 23 |
| Premium anual (mejor precio) | S/ 199 | S/ 16,6 |

**Criterio.** Referencias que encontré (precios en dólares, sin verificar tipo de cambio ni régimen en Perú):
AMBOSS, membresía de estudiante: USD 19,99 al mes o USD 149 al año, y solo 50 preguntas al mes del banco
([soporte de AMBOSS](https://support.amboss.com/hc/en-us/articles/32345265867921-AMBOSS-Pricing));
Lecturio: una fuente de terceros indica USD 39,99 al mes (no verificado con Lecturio)
([Subger](https://subger.com/en/service/lecturio)). No encontré precios de plataformas peruanas de ENAM.
Se fijó el precio muy por debajo de esas referencias (≈ S/ 29 ≈ USD 8) por el poder adquisitivo del
estudiante peruano, con descuento por compromiso (trimestral −21 %, anual −43 %). Son precios iniciales:
se cambian en una línea (`PLANES` en `cuenta.php`; el texto de la landing y del app se lee de ahí en el app,
y está escrito a mano en `index.html`).

## Qué incluye cada plan (cuando los límites están activos)
- **Gratis:** banco por especialidad, flujogramas, simulacro rápido y por especialidad, progreso — 20 preguntas por día.
- **Premium:** sin tope diario, simulacro ENAM 2020 completo, todos los simuladores y el tutor de IA.

> Los límites vienen **apagados** (`MQP_LIMITES=0`). Mientras estén apagados, el plan gratuito lo incluye todo y la
> web no cambia. **Actívalos al mismo tiempo que el cobro**; el texto de precios de la landing da por hecho que existen.
> Los límites se aplican en el navegador (al iniciar una actividad): frenan el uso normal, pero no son un candado
> contra alguien que descargue `bancos/*.json` directamente. Un candado real exigiría servir las preguntas desde el
> servidor, lo que cambiaría el formato de datos y no se hizo.

## Qué pasa cuando alguien compra
1. En `app/#/planes` elige un plan (si no tiene cuenta, pasa por `#/registro` y vuelve a los planes).
2. `cuenta.php` crea el cobro en Mercado Pago y lo manda a pagar en su pantalla segura.
3. Mercado Pago avisa a `cuenta.php?a=webhook`; el servidor **consulta el pago a Mercado Pago**, comprueba estado
   *approved*, moneda PEN y monto, y solo entonces activa el plan (una sola vez por pago; renovar suma tiempo).
4. El estudiante vuelve a **`app/#/inicio?pago=ok`**: ve «¡Tu plan Premium está activo!» (la página espera hasta
   ~40 s a que llegue la confirmación) y su nombre aparece con ★ en la barra superior.

## Pasarelas: PayU o Mercado Pago
`cuenta.php` cobra con **PayU Latam** (WebCheckout, soles) o con **Mercado Pago**. Se usa PayU si está configurado
(o la que indiques con `PASARELA`). Con PayU:
- El estudiante paga en la pantalla de PayU; PayU confirma al servidor en `cuenta.php?a=payu` y el plan se activa
  **solo si la firma MD5 coincide con tu ApiKey**, el estado es aprobado (4), la moneda es PEN, el monto cubre el plan
  y la referencia corresponde a una orden creada por el propio servidor.
- Al volver, PayU lleva al estudiante a `cuenta.php?a=retorno`, que solo lo redirige a `app/#/inicio?pago=ok`
  (aprobado), `#/planes?pago=pendiente` o `#/planes?pago=error`. Esa vuelta no activa nada.
- Variables: `PAYU_MERCHANT_ID`, `PAYU_ACCOUNT_ID`, `PAYU_API_KEY` (y `PAYU_TEST=1` mientras pruebas en sandbox).
- En el panel de PayU activa la URL de confirmación (`https://TU-DOMINIO/cuenta.php?a=payu`; el cobro ya la envía en cada
  transacción, pero conviene dejarla también en la configuración técnica de tu cuenta).

## Puesta en marcha (una vez)
1. Sube `cuenta.php`, `.htaccess` y los archivos del app. La carpeta `cuenta_datos/` se crea sola
   (SQLite) y se protege con su propio `.htaccess`. Debe poder escribirse.
2. **PayU:** abre tu cuenta de comercio en PayU Perú y copia `merchantId`, `accountId` y `ApiKey`.
   **Mercado Pago:** crea una aplicación y copia el *Access Token de producción*; en Webhooks apunta a
   `https://TU-DOMINIO/cuenta.php?a=webhook` con el evento *Pagos*.
3. En Hostinger define las variables de la pasarela elegida (o copia `config.example.php` a `config.php`) y `MQP_LIMITES=1`.
5. Haz una compra real de prueba con el plan mensual antes de anunciar.

## Qué se probó y qué no
Probado en local contra pasarelas simuladas (Mercado Pago con un servidor falso; PayU con firmas calculadas igual que PayU las calcula, usando datos públicos de prueba de su documentación): registro, ingreso, límite de intentos, creación del cobro,
activación solo con pago aprobado de monto y moneda correctos, rechazo de pagos pendientes/de monto bajo/en otra
moneda/de usuario inexistente, idempotencia del aviso, renovación que suma días, límites del plan gratuito y paso
de Premium. **No probado con PayU ni Mercado Pago reales** (no hay credenciales aquí): la pantalla de pago, la entrega de la confirmación a tu dominio
y las URL de retorno deben verificarse con una compra de prueba (en PayU, primero en sandbox con `PAYU_TEST=1`). No hay recuperación de contraseña ni verificación de
correo todavía.

## Dónde se guardan las cuentas y cómo verlas
- **Base de datos:** `cuenta_datos/mqp.sqlite` (SQLite, se crea sola al primer registro). Guarda nombre, correo, universidad, examen,
  contraseña **cifrada** (hash, nunca en claro), plan, fecha de vencimiento y los pagos. La carpeta se bloquea con su propio `.htaccess`
  y está en `.gitignore`: **no se sube a GitHub**, vive solo en tu hosting.
- **Ver / descargar la lista:** define `MQP_ADMIN_TOKEN` (o `admin_token` en `config.php`) con una clave larga de 16+ caracteres y abre
  `https://TU-DOMINIO/cuenta.php?a=admin&token=TU-CLAVE` → descarga un CSV (se abre en Excel). Con `&formato=json` devuelve JSON.
  Sin esa clave definida, la acción no existe (responde 404). Nunca incluye contraseñas.
- **Copia de seguridad:** descarga `cuenta_datos/mqp.sqlite` desde el administrador de archivos de Hostinger con regularidad (es un solo archivo).
- **Progreso de estudio:** con la sesión iniciada se guarda también en el servidor (tabla `progreso`) y se fusiona entre dispositivos:
  gana la respuesta más reciente de cada pregunta, y un reinicio no se revive desde otro dispositivo. Al cerrar sesión se quita el progreso
  de ese equipo (puede ser compartido); sigue en la cuenta. Limitación conocida: si quitas una pregunta de favoritas en un dispositivo,
  otro dispositivo con la estrella puesta puede volver a marcarla.
- **Derechos del usuario (Ley 29733):** en *Perfil → Mis datos y privacidad* el usuario descarga todos sus datos o elimina su cuenta
  (se borran cuenta y progreso; los pagos se conservan sin datos personales). La cuenta exige aceptar `privacidad.html` y se guarda cuándo.
- **Antes de publicar `privacidad.html`:** reemplaza los 5 textos resaltados en amarillo (titular, DNI/RUC, domicilio, correo). Valídala con un
  abogado y revisa si debes inscribir tu banco de datos ante la Autoridad Nacional de Protección de Datos Personales. Faltan, además,
  unos Términos y condiciones (el enlace "Términos" del pie sigue apuntando al aviso legal).

## Universidades del registro
La lista está en `universidades.js` (una línea por universidad: nombre, siglas, sede). Se armó con información pública general, **no con el
registro oficial**: contrástala con la SUNEDU y ASPEFAM antes de darla por definitiva, y agrega o quita líneas en ese archivo.
