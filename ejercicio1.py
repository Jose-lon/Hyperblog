def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_inv = palabra[::-1]
    if palabra_inv == palabra:
        es_palindromo = True
    else:
        es_palindromo = False
    return es_palindromo

def run():
    palabra = input("EScribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")

if __name__ == '__main__':
    run()