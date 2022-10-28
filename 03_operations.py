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

