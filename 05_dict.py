import random

dict = {}

for i in range(1,11):
    dict[i] = i*2

print(dict)

dict_v2 = {i:i*2 for i in range(1,11)}  #Tener en cuenta la clave llave:valor
print(dict_v2)



countries = ["col","mex","bol","pe"]
population = {}

for country in countries:
    population[country] = random.randint(1,10000)

print(population)

population_v2 = {country:random.randint(1,10000) for country in countries}
print(population_v2)

names = ["Nico","Zule","Santi"]
ages = [12,56,98]

print(list(zip(names, ages)))

new_dict = {name:age for (name,age)in zip(names,ages)}
print(new_dict)
