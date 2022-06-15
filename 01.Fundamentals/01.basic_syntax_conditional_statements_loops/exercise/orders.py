number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 0 or days > 31:
        continue
    if capsules_count < 1 or capsules_count > 2000:
        continue
    price_per_order = price_per_capsule * days * capsules_count
    total_price += price_per_order
    print(f"The price for the coffee is: ${price_per_order:.2f}")
print(f"Total: ${total_price:.2f}")
