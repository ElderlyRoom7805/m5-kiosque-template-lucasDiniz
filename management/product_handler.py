from menu import products


def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type):
    output = []

    for product in products:
        if product['type'] == type:
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