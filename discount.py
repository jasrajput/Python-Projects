import decimal

def total_cart_item(cart):
    total = 0
    for val in cart.values():
        total = total + val
    print('Total: ' + str(total))
    return total


cart_items = {
    'shirt': 1,
    'jean': 1,
    'shoes': 498,
}


full_total = total_cart_item(cart_items)

def calc_discount(price, discount):
    total_discount = float(price) * (float(discount) / 100)
    sale_price = price - total_discount
    print(sale_price)


calc_discount(full_total, 99)