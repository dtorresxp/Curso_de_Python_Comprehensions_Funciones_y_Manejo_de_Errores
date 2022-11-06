def increment(x):
    return x+1

# Para transformar en una lambda function se reconocen los parametros de entrada
# y los parámetros de salida, en este caso input = x y output = x+1

increment_v2 = lambda x : x+1
full_name = lambda name, last_name : str(name) + " " + str(last_name)

def run():
    result = increment(10)
    print(result)

    result = increment_v2(20)
    print(result)

    print(full_name("Mario","Riascos"))

if __name__ == '__main__':
    run()