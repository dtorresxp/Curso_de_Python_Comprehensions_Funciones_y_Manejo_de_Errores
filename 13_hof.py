def increment(x):
    return x+1


def high_order_function(x, func):                       #Se envia unicamente el nombre de la func sin parámetros
    return x + func(x)                                  #En el return se ejecuta la fución

increment_v2 = lambda x : x+1

high_order_function_v2 = lambda x, func : x + func(x)   #La entrada es el nombre de la funcion sin parámetros
                                                        #En la salida se ejecuta la función

def run():
    print(high_order_function(20, increment))
    print(high_order_function_v2(20,increment_v2))


if __name__ == '__main__':
    run()