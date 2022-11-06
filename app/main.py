from mod import *

data = [
        {
            'Country':'Colombia',
            'Population':51000
        },
        {
            'Country':'Bolivia',
            'Population':40000
        }
    ]

def run():
    keys, values = get_population()
    print(f'La población de {keys[0]} es {values[0]}')
    print(f'La población de {keys[1]} es {values[1]}')

    country = input("Type a Country: ").lower().capitalize()
    result2 = population_by_country(data,country)
    if result2 == None:
        print("Valor invalido")
    else:
        print(result2)

if __name__ == '__main__':
    run()