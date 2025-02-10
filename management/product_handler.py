from menu import products


def get_product_by_id(id):
    if type(id) is not int:
        raise TypeError('product id must be an int')
    
    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(search_type):
    if type(search_type) is not str:
        raise TypeError('product type must be a str')
    
    output = []

    for product in products:
        if product['type'] == search_type:
            output.append(product)

    return output


def add_product(menu, **kwargs):
    id = 0
    list_ids = []
    
    if len(menu) == 0:
        id = 1
    else:
        for product in products:
            list_ids.append(int(product["_id"]))
        max_id_list = sorted(list_ids, reverse=True)
        last_product = max_id_list[0]
        id = last_product + 1
        
    kwargs["_id"] = id
    menu.append(kwargs)
    
    return kwargs


def menu_report():
    product_count = len(products)
    total = 0

    for product in products:
        total = total + product['price']
    average_price = round(total / product_count, 2)
    
    types = {'bakery': 0, 'dairy': 0, 'drink': 0, 'fruit': 0, 'vegetable': 0}

    for product in products:
        for key in types:
            if key == product['type']:
                types[key] = types[key] + 1

    most_common_type = {'most_common': 0, 'type': ''}

    for key, value in types.items():
        if value > most_common_type['most_common']:
            most_common_type['most_common'] = value
            most_common_type['type'] = key

    return (f'Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type['type']}')
