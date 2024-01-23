orders = {}
price_orders = {}
while True:
    elements = input()
    if elements == 'buy':
        break
    elements = elements.split()
    product = elements[0]
    quantity = int(elements[2])
    price = float(elements[1])
    if product not in orders:
        orders[product] = 0
        price_orders[product] = 0
    orders[product] += quantity
    price_orders[product] = price

[print(f'{key} -> {orders[key]*price_orders[key]:.2f}') for key in orders]