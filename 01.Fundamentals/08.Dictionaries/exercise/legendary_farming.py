data = input().split()
items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while True:
    for index in range(0, len(data), 2):
        material = data[index + 1].lower()
        quantity = int(data[index])
        if material not in items:
            items[material] = 0
        items[material] += quantity
        if items["shards"] >= 250:
            obtained = True
            items["shards"] -= 250
            print("Shadowmourne obtained!")
            break
        elif items["fragments"] >= 250:
            obtained = True
            items["fragments"] -= 250
            print("Valanyr obtained!")
            break
        elif items["motes"] >= 250:
            obtained = True
            items["motes"] -= 250
            print("Dragonwrath obtained!")
            break
    if obtained:
        break
    data = input().split()

for key, value in items.items():
    print(f"{key}: {value}")
