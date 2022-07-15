command = input()
products_price = {}
products_quantity = {}
while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products_price:
        products_price[name] = price
        products_quantity[name] = quantity
    else:
        products_price[name] = price
        products_quantity[name] += quantity
    command = input()

for product, price in products_price.items():
    total_price = price * products_quantity[product]
    print(f"{product} -> {total_price:.2f}")

