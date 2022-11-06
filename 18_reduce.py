from functools import reduce

def accum(counter,item):
    print('Counter=>',counter)
    print('Item=>',item)

    return counter + item

numbers = [1,2,3,4]

result = reduce(lambda counter, item : counter+item,numbers)    #La primer variable incrementará el valor y la segunda
                                                                #que es el ítem que se va a estar iterando
print(result)

result2 = reduce(accum,numbers)
print(result2)