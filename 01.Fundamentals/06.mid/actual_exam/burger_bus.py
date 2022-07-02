number_of_cities = int(input())
total_profit = 0
for city in range(1, number_of_cities + 1):
    city_name = input()
    earned_money = float(input())
    expenses = float(input())

    if city % 3 == 0 and not city % 5 == 0:
        expenses *= 1.5

    if city % 5 == 0:
        earned_money *= 0.9

    profit_for_current_city = earned_money - expenses
    total_profit += profit_for_current_city
    print(f"In {city_name} Burger Bus earned {profit_for_current_city:.2f} leva.")
    profit_for_current_city = 0
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
