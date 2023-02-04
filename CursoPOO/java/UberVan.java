import java.utils.ArrayList;
import jav.utill.Map;

class UberVan extends Car {
    Map<String, ArrayList<String, Integer>> typeCatAccepted;
    ArrayList<String> seatMaterial;
    private Integer passenger;

    public UberVan(String license, Account driver, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatMaterial) {
        super(license, driver);
        this.typeCatAccepted = typeCatAccepted;
        this.seatMaterial = seatMaterial;
    }

    @Override

    public void setPassenger(Integer passenger) {
        if(passenger == 6){
            this.passenger = passenger;
        }else{
            System.out.println("Necesitas agregar 6 pasajeros");
        }
    }

}