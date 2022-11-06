def add_taxes(item):
    item['taxes'] = item['price']*.19
    return item

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

    prices = list(map(lambda item: item['price'],items))
    print(prices)

    new_items = list(map(add_taxes,items))
    print(new_items)


if __name__ == '__main__':
    run()