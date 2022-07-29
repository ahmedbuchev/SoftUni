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

# Ivan Shopov
# pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
# total_cost = 0
# bought_furniture = []
# command = input()
# while command != "Purchase":
#     match = re.search(pattern, command)
#     if match:
#         furniture, price , quantity = match.groups()
#         bought_furniture.append(furniture)
#         total_cost += int(quantity) * float(price)
#     command = input()
# print("Bought furniture:")
# for furniture in bought_furniture:
#     print(furniture)
# print(f"Total money spend: {total_cost:.2f}")
