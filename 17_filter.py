numbers = [1,2,3,4,5]

new_numbers = list(filter(lambda x: x%2 == 0, numbers))  #Siempre se valida el valor True
print(new_numbers)