<?php
// Router para `php -S` que imita las reglas de .htaccess (los contenidos pasan por acceso.php). Solo para pruebas.
$u = rawurldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH) ?: '/'); $u = ltrim($u, '/');
if (preg_match('#^(bancos|flujogramas|herramientas|residentado|guardia|consulta|serums|atlas3d)/(.+)$#', $u) || preg_match('#^((guardia_casos|guardia_lab|guardia_biblioteca|guardia_uci|consulta_casos|serums_casos|algoritmos)\.js)$#', $u) || preg_match('#^([^/]+\.pdf)$#', $u)) {
    $_GET['f'] = $u; require $_SERVER["DOCUMENT_ROOT"] . "/acceso.php"; return true;
}
return false;
