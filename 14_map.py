def second_function():
    numbers = [1,2,3,4]
    numbers_2 = [5,6,7]

    print(numbers)
    print(numbers_2)
    result = list(map(lambda x,y:x+y,numbers,numbers_2))
    print(result)

def run():
    numbers = [1,2,3,4]
    numbers_v2 = []
    numbers_v3 = list(map(lambda i : i*2,numbers))  #La función map unicamente devuelve un iterable, por lo
                                                    #tanto, se debe transformarlo a una lista. map cumple con
    for i in numbers:                               #high order function, por lo cual también recibe funciones
        numbers_v2.append(i*2)

    print(numbers)
    print(numbers_v2)
    print(numbers_v3)

if __name__ == '__main__':
    run()
    second_function()