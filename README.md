# Curso_de_Python_Comprehensions_Funciones_y_Manejo_de_Errores

**Nuevo Curso de Comprehension Lists, Funciones y Manejo de Errores**

<p align="center"><img width=40% src="./pictures/python_logo.png"></p>

# Table of Content 

- [Sets](#sets)
- [Modificando Conjuntos](#modificando-conjuntos)
- [Operaciones de Conjuntos](#operaciones-de-conjuntos)

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
# Operaciones de Conjuntos 

Existen diferentes operaciones dentro del entorno de conjuntos, como unión, intesección, diferencia y diferencia simétrica

```Python
set_a = {'col','mex','bol'}         #Tenemos dos conjuntos
set_b = {'pe','bol'}

#union
set_c = set_a.union(set_b)          #Este método une los elementos del conjunto a con el conjunto b
print(set_c)
print(set_a | set_b)                #El operador "|" cumple la función de unir los conjuntos 

#intersección
set_c = set_a.intersection(set_b)   #Este método toma los elementos comúnes entre ambos conjuntos
print(set_c)
print(set_a & set_b)                #El operador "&" cumple la función de intersección

#diferencia
set_c = set_a.difference(set_b)     #Este método quita los elementos de b presentes en a
print(set_c)
print(set_a - set_b)                #El operador "-" indica diferencia 

#Diferencia simétrica 
set_c = set_a.symmetric_difference(set_b)   #Este método hace una unión sin los elementos que coinciden en común
print(set_c)
print(set_a ^ set_b)                #El operador "^" permite hacer la diferencia simétrica
```

# List Comprehension

[element for element in iterable]

En la sintáxis tenemos elemento y el ciclo donde se extraen elementos de cualquier iterable

```Python
numbers = []

for element in range(1,11):
    numbers.append(element*2)
    
print(numbers)

numbers_v2 = [element*2 for element in range(1,11)] #Por cada elemento del iterable se está agregando un 
print(numbers_v2)                                   #elemento a la lista
```

[element for element in iterable if condition]

En este caso tenemos el elemento, ciclo donde se extraen elementos de cualquier iterable y la condición opcional para filtrar elementos 

```Python
numbers = []

for i in range(1,11):
    if i%2 == 0:
        numbers.append(i*2)

print(numbers)

numbers_v2 = [i*2 for i in range(1,11) if i%2 == 0]
print(numbers_v2)
```

# Dictionary Comprehension

Al igual que las listas, tenemos una sintáxis similar, por ejemplo:

{key:value for var in iterable}

Elemento llave:valor y el Ciclo donde se extrarn elementos de cualquier iterable 

