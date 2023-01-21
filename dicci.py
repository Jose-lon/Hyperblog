poblacion_paises = {
    'argentina' : 4456,
    'brasil': 567,
    'colombia' : 4356
}

for pais in poblacion_paises.keys():
    print(pais)
for pais in poblacion_paises.values():
    print(pais)
for pais, poblacion in poblacion_paises.items():
    print(pais, poblacion)