import re
data = input()
furniture_name = []
total_money = 0
pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
while not data == "Purchase":

    valid_furniture = re.match(pattern, data)
    if valid_furniture:
        furniture_dict = valid_furniture.groupdict()
        furniture_name.append(furniture_dict['name'])
        total_money += float(furniture_dict['price']) * int(furniture_dict['quantity'])
    data = input()

print("Bought furniture:")
for furniture in furniture_name:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")

