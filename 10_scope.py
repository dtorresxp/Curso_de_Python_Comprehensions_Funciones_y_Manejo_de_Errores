price = 100

def increment():
    # price = price + 10    #Genera un error de asignación 
    price = 200
    price = price +10
    print(price)
    return price

print(price)
price_2 = increment()
print(price_2)