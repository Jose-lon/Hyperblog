import java.utils.ArrayList;
import jav.utill.Map;

class UberBlack extends Car {
    Map<String, ArrayList<String, Integer>> typeCarAccepted;
    ArrayList<String> seatMaterial;

    public UberBlack(String license, Account driver, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }

}