<!DOCTYPE html>
<html>
<head><title>Smart Light Control</title></head>
<body>
<h1>Smart Light Controller</h1>

<form method="post">
    <input type="submit" name="action" value="TURN ON">
    <input type="submit" name="action" value="TURN OFF">
    <input type="submit" name="action" value="BLINK">
</form>

<?php
if(isset($_POST['action'])){
    $action = $_POST['action'];
    if($action == 'TURN ON'){
        shell_exec("sudo python3 /var/www/html/turnon.py");
        echo "LED is ON";
    }
    if($action == 'TURN OFF'){
        shell_exec("sudo python3 /var/www/html/turnoff.py");
        echo "LED is OFF";
    }
    if($action == 'BLINK'){
        shell_exec("sudo python3 /var/www/html/blink.py > /dev/null 2>&1 &");
        echo "LED is BLINKING";
    }
}
?>
</body>
</html>





