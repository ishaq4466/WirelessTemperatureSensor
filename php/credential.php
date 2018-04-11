
/*This php stores the credentials for the database server
and also it establishes the connection to the server*/
<?php


$username="root";
$password="jis";
$database="tempdb";

mysql_connect(localhost,$username,$password);
@mysql_select_db($database) or die( "Unable to select database");

?>