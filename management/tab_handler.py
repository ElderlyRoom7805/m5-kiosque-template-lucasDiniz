from menu import products


def calculate_tab(list_tab):
    total = 0

    for tab in list_tab:
        id = tab['_id']
        amount = tab['amount']
        product = []
        for prod in products:
            if prod['_id'] == id:
                product.append(prod)
        total = round(total + (product[0]['price'] * amount), 2)

    subtotal = {'subtotal': f'${total}'}

    return subtotal