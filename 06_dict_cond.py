import random

countries = ["col","mex","bol","pe"]

population_v2 = {country:random.randint(1,10000) for country in countries}
print(population_v2)

result = {country:population for (country,population) in population_v2.items() if population > 4000}
print(result)

text = "Hola, soy Mario Riascos programador backend python"

unique = {ch:text.count(ch) for ch in text if ch in 'aeiou'}
print(unique)