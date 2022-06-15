def order(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2


product_ = input()
quantity_ = int(input())
order_price = order(product_, quantity_)
print(f"{order_price:.2f}")
