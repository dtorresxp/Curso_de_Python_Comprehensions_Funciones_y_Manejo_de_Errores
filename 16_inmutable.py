def add_taxes(item):
    new_item = item.copy()                      #Se crea una nueva lista, para evitar los cambios en memoria
    new_item['taxes'] = new_item['price']*.19
    return new_item

def run():
    
    items  = [
        {
            'producto':'shirt',
            'price':100,
        },
        {
            'product':'pants',
            'price':300
        },
        {
            'product':'shoes',
            'price':200
        }
    ]

    new_items = list(map(add_taxes,items))
    print('New List')
    print(new_items)
    print('Old List')
    print(items)


if __name__ == '__main__':
    run()