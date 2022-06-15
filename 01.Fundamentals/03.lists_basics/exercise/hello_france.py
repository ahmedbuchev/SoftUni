items_with_prices = input().split("|")
budget = float(input())

profit = 0
needed_sum = 150
sum_of_new_prices = 0
for item in range(len(items_with_prices)):
    data_is_valid = False
    item_list = items_with_prices[item].split("->")

    type_ = item_list[0]
    price = float(item_list[1])

    if type_ == "Clothes" and 0 <= price <= 50:
        data_is_valid = True
    elif type_ == "Shoes" and 0 <= price <= 35:
        data_is_valid = True
    elif type_ == "Accessories" and 0 <= price <= 20.50:
        data_is_valid = True

    if data_is_valid:
        if budget - price < 0:
            continue
        if budget < 0:
            break
        else:
            budget -= price
            new_price = price * 1.4
            sum_of_new_prices += new_price
            print(f"{new_price:.2f}", end=" ")
            profit += 0.4 * price

print()
print(f"Profit: {profit:.2f}")
money_we_have = budget + sum_of_new_prices

if money_we_have >= needed_sum:
    print("Hello, France!")
else:
    print("Not enough money.")
