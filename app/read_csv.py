import csv

def read_csv(path):
    with open(path,'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)                              #Unión de dos arrays, por lo que la salida
            country_dict = {key:value for (key,value) in iterable}  #será una tupla, el primer valor es la
            data.append(country_dict)                               #columna y el segundo es las filas
            return data


if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data)
