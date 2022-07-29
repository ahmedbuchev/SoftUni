num = int(input())
plant_rarity_dict = {}
plant_rating_dict = {}

for _ in range(num):
    plant, rarity = input().split("<->")

    plant_rarity_dict[plant] = rarity
    plant_rating_dict[plant] = []

command = input()

while not command == "Exhibition":
    info = command.split(": ")
    cmd = info[0]

    if cmd == "Rate":
        plant, rating = info[1].split(" - ")
        rating = int(rating)
        if plant in plant_rating_dict:
            plant_rating_dict[plant].append(rating)
        else:
            print("error")

    elif cmd == "Update":
        plant, new_rarity = info[1].split(" - ")

        if plant in plant_rarity_dict:
            plant_rarity_dict[plant] = new_rarity
        else:
            print("error")

    elif cmd == "Reset":
        plant = info[1]

        if plant in plant_rating_dict:
            plant_rating_dict[plant].clear()
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")

for plant, rarity in plant_rarity_dict.items():
    if plant_rating_dict[plant]:
        avg_rating = sum(plant_rating_dict[plant]) / len(plant_rating_dict[plant])
    else:
        avg_rating = 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")

