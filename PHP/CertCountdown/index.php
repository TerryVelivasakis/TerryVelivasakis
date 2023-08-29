<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.min.js" integrity="sha384-cuYeSxntonz0PPNlHhBs68uyIAVpIIOZZ5JqeqvYYIcEL727kskC66kF92t6Xl2V" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>



<?php
$servername = "127.0.0.1";
$username = "terry";
$password = "terry";

/* Create connection
$conn = new mysqli($servername, $username, $password);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully";

*/


function timeLeft($dueDate){
    $diff = strtotime($dueDate) - time();
    $temp = $diff/86400;
    $days=floor($temp);  $temp=24*($temp-$days);
    $hours=floor($temp);  $temp=60*($temp-$hours); 
    $minutes=floor($temp);  $temp=60*($temp-$minutes); 
    return $days." days ".$hours." hours ".$minutes. " minutes";
}


echo '<table class="table"><tr><th>Certification</th><th>Goal Date</th><th>Time Remaining</th></tr>';

$handle = fopen("certs.csv", "r");
for ($i = 0; $row = fgetcsv($handle ); ++$i) {
    if ($row[2] == "Passed"){
        $rowClass = "class='table-primary'";
        $passedCheer = "NAILED IT! Earned on ".date("M j, Y",strtotime($row[3]));
    } else {
        $rowClass = "";
        $passedCheer = timeLeft($row[1]);
    }

    echo "<tr $rowClass>";
    echo "<td>".$row[0]."</td>";
    echo "<td>".date("M j, Y",strtotime($row[1]))."</td>";
    echo "<td>$passedCheer</td>";
    
    echo "</tr>";
}
fclose($handle);
echo "</table>";



?>

<!--
<a href="https://academy.hackthebox.com/achievement/badge/aa7374bc-3728-11ee-acfc-bea50ffe6cb4"><img src="https://academy.hackthebox.com/storage/badges/academician.png" alt="HTB Academian" style="width:100px;height:100px;"></a>
<a href="https://academy.hackthebox.com/achievement/badge/3267a41c-30fd-11ee-acfc-bea50ffe6cb4"><img src="https://academy.hackthebox.com/storage/badges/our-favorite-seabird.png" alt="HTB Academian" style="width:100px;height:100px;"></a>
<a href="https://academy.hackthebox.com/achievement/badge/19161dd9-3727-11ee-acfc-bea50ffe6cb4"><img src="https://academy.hackthebox.com/storage/badges/tactical.png" alt="HTB Academian" style="width:100px;height:100px;"></a>
-->
