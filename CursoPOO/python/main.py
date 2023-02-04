from car import Car
from account import Account

if __name__ == "__main__":
    car =  Car("qweqweqweq","AMS123", Account("Andrés Herrera", "DFT345"),4)
    print(vars(car))
    print(vars(car.driver))
