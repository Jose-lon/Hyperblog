def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador += 1
        potencia_2 = 2**contador

    potencia_2 = 2**1
    for contador1 in range(10):
        potencia_2 = 2**contador1
        print("2 elevado a " + str(contador1) + " es igual a: " + str(potencia_2))

if __name__ == '__main__':
    run()