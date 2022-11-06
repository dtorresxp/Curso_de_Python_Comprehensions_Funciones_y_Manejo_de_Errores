import sys                  #Preguntar el sistema operativo 
print(sys.path)

import re                   #Expresiones regulares 
text = 'Mi número de telefono es 311 123 1211, el código del país es 57, mi número de la suerte es el 17' 
result = re.findall('[0-9]+',text)        
print(result)

import time                 #Manejo de fechas
timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime()
print(result)

import collections          #Utilidad para manejar listas 
numbers = [1,1,2,1,2,1,4,5,3,3,21] 
counter = collections.Counter(numbers)
print(counter)              #Saber la frecuencia en la que aparece cada número 