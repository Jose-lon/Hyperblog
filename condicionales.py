def calcular(valor):
    pesos = float(input("Ingrese la cantidad de dinero para conversión: "))
    dolares = str(round(pesos / valor_dolar,2))
    print("Sr@ " + nombre + ", usted tiene $" + dolares + " doláres")
nombre = input("¿Cuál es su nombre?")
nombre = nombre[0].upper() + nombre[1:]
nombre = nombre.strip()
menu ="""
BIenvenido al conversor de monedas

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opción: 
"""


opcion = int(input(menu))
if opcion == 1: 
    valor_dolar = 3875
    calcular(valor_dolar)
elif opcion == 2:
    valor_dolar = 150
    calcular(valor_dolar)
elif opcion == 3:
    valor_dolar = 5040
    calcular(valor_dolar)
else: 
    print("Ingresa una opción valida")

