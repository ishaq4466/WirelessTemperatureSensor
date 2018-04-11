/* This php file finally fetches the temperature value from
tempdb and display it in the html section ;-) */
<?php
include_once('credential.php');

$query="SELECT * FROM templog";
$result=mysql_query($query);
$num =mysql_numrows($result);
$i=0;
while($i<$num)
{
            $datetime=mysql_result($result,$i,"date");
            $temp=mysql_result($result,$i,"temperature");
            $i++;
}
mysql_close();
?>
<!DOCTYPE html>
<html>

        <h1> Temperatue is <?php echo $temp?></h1>

</html>
