<?php
require_once('Car.php');
require_once('Account.php');
require_once('Route.php');
require_once('Payment.php');
require_once('uberBlack.php');
require_once('uberPool.php');
require_once('uberX.php');
require_once('uberVan.php');

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$uberX->setPassenger(4);
$uberX->printDataCar();
?>