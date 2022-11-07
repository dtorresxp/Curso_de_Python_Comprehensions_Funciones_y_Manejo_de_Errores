with open("./text.txt",'r+',) as file:  #El permiso de r+ permite leer y escribir, sin embargo si se cambia a
    for line in file:                   #w+ el va a sobreescribir el archivo 
        print(line)
    
    file.write("Nuevas cosas en este archivo\n")
    file.write("Otra linea\n")
    file.write("Más linea\n")

