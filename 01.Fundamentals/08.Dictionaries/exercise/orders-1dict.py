command = input()
products = {}

while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["price"] = price
        products[name]["quantity"] += quantity
    command = input()

for product, price_quantity in products.items():
    total_price = price_quantity["price"] * price_quantity["quantity"]
    print(f"{product} -> {total_price:.2f}")

