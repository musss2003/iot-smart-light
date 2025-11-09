<!DOCTYPE html>
<html>
<head>
    <title>Smart Light Control</title>
    <link rel="stylesheet" href="style.css"> 
</head>
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
    
    // PHP executes the shell command based on button click
    if($action == 'TURN ON'){
        shell_exec("sudo python3 /var/www/html/turnon.py");
        $status_text = "LED is ON";
    }
    if($action == 'TURN OFF'){
        shell_exec("sudo python3 /var/www/html/turnoff.py");
        $status_text = "LED is OFF";
    }
    if($action == 'BLINK'){
        shell_exec("sudo python3 /var/www/html/blink.py > /dev/null 2>&1 &");
        $status_text = "LED is BLINKING";
    }
    
    // Display the status message with the CSS class
    echo "<div class='status-message'>$status_text</div>";
}
?>
</body>
</html>