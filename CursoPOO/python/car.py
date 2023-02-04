from account import Account

class Car:
    id          = int
    license     = str
    driver      = Account("","")
    passenger   = int

    def __init__(self, id, license, driver, passenger):
        self.id = id
        self.license = license
        self.driver =  driver
        self.passanger = passenger