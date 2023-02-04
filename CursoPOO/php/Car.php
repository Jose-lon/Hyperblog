<?php
require_once("account.php");
class Car {
  public $id;
  public $license;
  public $driver;
  protected $passengers;

  public function __construct($license, $driver) {
      $this->license = $license;
      $this->driver = $driver;
    }

  public function PrintDataCar(){
      echo "
          Licencia: $this->license
          Driver: {$this->driver->name}
          Número de pasajeros: $this->passengers
          
      ";
    }

  public function getPassenger() {
    return $this->passengers;
  }

  public function setPassenger($passenger) {
        
    if ($passenger == 4) {
        $this->passengers = $passenger;
    }
    else {
        echo "Necesitas asignar 4 pasajeros";
    }

  }
}
?>