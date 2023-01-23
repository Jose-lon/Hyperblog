'''
set_countries = {"col","mex","bol","col"}
#set_countries = set("col","mex","bol","col")
print(set_countries)
print(type(set_countries))
set_countries.add("pe")
set_countries.update({"ecu","ar"})
set_countries.remove("col")
set_countries.discard("ar")
#set_countries.clear()
print(set_countries)
set_countries2 = {"col","usa","sui","bol"}
set_3 = set_countries.union(set_countries2)
set_4 = set_countries | set_countries2
print(set_3 == set_4)
set_5 = set_countries.intersection(set_countries2)
set_6 = set_countries & set_countries2
print(set_5 == set_6)
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
#------------------------------------------------------
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