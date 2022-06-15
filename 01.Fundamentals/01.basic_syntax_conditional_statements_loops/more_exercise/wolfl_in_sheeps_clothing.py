string_animals = input()
animal_list = string_animals.split(", ")

sheep_counter = 0
for animal in animal_list:
    if animal == "sheep":
        sheep_counter += 1
    if animal == "wolf":
        sheep_counter = 0

if sheep_counter == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
