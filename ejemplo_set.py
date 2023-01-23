
set_countries = {"col","mex","bol","col"}
'''
#set_countries = set("col","mex","bol","col")
print(set_countries)
print(type(set_countries))
set_countries.add("pe")
set_countries.update({"ecu","ar"})
set_countries.remove("col")
set_countries.discard("ar")
#set_countries.clear()
print(set_countries)
'''
set_countries2 = {"col","usa","sui","bol"}
'''
set_3 = set_countries.union(set_countries2)
set_4 = set_countries | set_countries2
print(set_3 == set_4)
'''
set_5 = set_countries.intersection(set_countries2)
set_6 = set_countries & set_countries2
print(set_5 )
'''
set_7 = set_countries.difference(set_countries2)
set_8 = set_countries - set_countries2
print(set_7 == set_8)
set_9 = set_countries.symmetric_difference(set_countries2)
set_10 = set_countries ^ set_countries2
print(set_9 == set_10)
'''
#-----------------------------------------------
'''
numbers = []
for element in range(1,11):
    numbers.append(element)
print(numbers)

numbers_v2 = [element for element in range(1,11) if element%2 != 0]
print(numbers_v2)
'''
#------------------------------------------------
'''
dict = {}
for i in range(1,11):
    dict[i] = i 
print(dict)

dict_v2 = {i: i for i in range(1,11)}
print(dict == dict_v2)

import random
popu = {}
country = ["col","ecu","usa","chi"]

for i in country:
    popu[i] = random.randint(1,10)

print(popu)

popu_v2 = {i: random.randint(1,10) for i in country}

print(popu_v2)
'''
#------------------------------------------------------
'''
names = ["nico","zule","santi"]
ages = [12,56,89]
new_dict = {name: age for (name, age) in zip(names,ages)}
print(new_dict)

new_dict_v2 = {}
h = 0
for i in names:
    new_dict_v2[i] = ages[h]
    h += 1
print(new_dict_v2) 
'''
#------------------------------------------------------
'''
countries = ["col","mex","bol","pe"]

population_v2 = { country: random.randint(1,100) for country in countries}
print(population_v2)

filter = {country: population for (country, population) in population_v2.items() if population > 20}
print(filter)
#-------------------------------------------------------
text = "Porque nadie me entiende"
unique = { c: text.count(c) for c in text if c not in "aeiou"}
print(unique)
#-------------------------------------------------
full_name = lambda name, last_name: f'Full name is {name.capitalize()} {last_name.capitalize()}'
print(full_name("jose", "londoño"))
name = ["jose", "londoño"]
full_name2 = list(map(lambda name: name.capitalize(), name))
print("Full name is " + full_name2[0] + " " + full_name2[1])
#---------------------------------------------------------
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]
result = list(map(lambda x, y :  x + y , numbers_1, numbers_2))
print(result)
'''
#-------------------------------------------------
'''
items= [
    {
        "product": "camisa",
        "price": 100
    },
    {
        "product": "pantalon",
        "price": 200
    },
    {
        "product": "pantalon",
        "price": 300
    }
]

print(list(map(lambda item: item["price"], items)))
def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    return new_item
items_taxes = list(map(add_taxes,items))
print(items_taxes)
print(items)
#dict.copy() resuelve la mutabilidad en memoria de los diccionarios
'''
#--------------------------------------------------------
'''
numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda f:f % 2 == 0, numbers))
print(new_numbers)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

new_list = list(filter(lambda item: item['home_team_result'] == 'Draw', matches))

print(new_list)
'''
#-------------------------------------
'''
import functools

number = [1,2,3,4]

def accum(counter, item):
    return item * counter

result = functools.reduce(accum, number)
print(result)
'''
#--------------------------
'''
import sys
print(sys.path)

import time
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
counter = collections.Counter(numbers)
print(counter)
'''
#--------------------------------
#order["total"] for order in orders se crea una lista con los valores del
#item "total" de un diccionario llamado orders
'''
my_iter = iter(range(1,11))
print(next(my_iter))
print(next(my_iter))
'''
#-----------------------------------
#raise Exception("message") lanza errores personalizados
'''
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
'''
#assert 1 != 1, "Uno es igual que uno" el assert permite mensajes personalizados de error
#file = open('./text.txt')
#file.read()
#file.readline()
#file.close()
'''
with open('./text.txt', "r+") as file: #permisos de escritura y lectura
    file.write("nuevas cosas en este archivo")
    print(file.read())
'''
#---------------------------------------------
'''
import csv

with open(path, "r") as file:
    reader = csv.reader(file, demiliter=",")
    header = next(reader)
    data = []
    for i in reader:
        iterable = zip(header, i)
        dict = {key: value for key, value in iterable}
        data.append(dict)
'''
#-----------------------cod