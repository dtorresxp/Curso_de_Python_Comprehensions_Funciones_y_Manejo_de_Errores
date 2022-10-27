from ctypes import sizeof


set_countries = {'col','mex','bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

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
