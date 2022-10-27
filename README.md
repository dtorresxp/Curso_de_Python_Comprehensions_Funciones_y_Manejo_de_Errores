# Curso_de_Python_Comprehensions_Funciones_y_Manejo_de_Errores

**Nuevo Curso de Comprehension Lists, Funciones y Manejo de Errores**

<p align="center"><img width=50% src="./pictures/python_logo.png"></p>

# Table of Content 
- [Sets](#sets)

# Sets

Denominados conjuntos, las propiedades alrededor de los conjuntos es que

* Se pueden modificar.
* No tienen un orden.
* No permiten duplicados, por lo tanto, estos conjuntos sacan términos únicos y si se repiten simplemente
no los imprime o los toma en cuenta. 

# Modificando Conjuntos 

Los conjuntos se pueden manejar como listas o Strings, es decir, se pueden modificar sus elementos, medir 
su tamaño, adicionar elementos, en fin 

```Python
set_countries = {'col','mex','bol'}     #Definimos el conjunto

size = len(set_countries)               #Tamaño del conjunto
print(size)

print('col' in set_countries)           #Verificar si 'col' está en set_countries, imprime True, porque se cumple la conidición 
print('pe' in set_countries)            #Verifica si 'pe' está en set_countries, imprime False, debido a que no cumple la condición

#add
set_countries.add('pe')                 #El método .add adiciona un nuevo elemento 
print(set_countries)

# update 
set_countries.update({'arg','ecu'})     #Agrega los elementos de un conjunto al conjunto anterior
print(set_countries)

# remove 
set_countries.remove('col')             #El método remove borra el elemento col 
print(set_countries)

set_countries.discard('Ven')            # Con este método se puede borrar elementos, si el elemento no existe
print(set_countries)                    #simplemente no lo borra. 

set_countries.clear()                   #Borra todos los elementos dentro del conjunto 
print(set_countries)

```


