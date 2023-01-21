import random

def run():
    numero_adivi = random.randint(1, 100)
    numero_int = int(input("Intente adivinar el número: "))
    while numero_int != numero_adivi:
        if numero_int < numero_adivi:
            print("Es un número más grande que ese")
            numero_int = int(input("Intenta de nuevo: "))
        else: 
            print("Es un número más pequeño que ese")
            numero_int = int(input("Intenta de nuevo: "))
    print("GANASTE")

if __name__ == '__main__':
    run()