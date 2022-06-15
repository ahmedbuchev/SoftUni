budget = float(input())

flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price_per_250_ml = 1.25 * flour_price / 4

bread_counter = 0
colored_eggs = 0
price_per_bread = flour_price + eggs_price + milk_price_per_250_ml

while budget - price_per_bread > 0:
    budget -= price_per_bread
    bread_counter += 1
    colored_eggs += 3
    if bread_counter % 3 == 0:
        colored_eggs -= (bread_counter - 2)

print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

