quantity = int(input())
days = int(input())

christmas_spirit = 0
budget = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += 2 * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        budget += (5 + 3) * quantity
        christmas_spirit += 13
    if day % 5 == 0:
        budget += 15 * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += 5 + 3 + 15
    if day == days and day % 10 == 0:
        christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
