name = input()
house = ""
all_names_are_sorted = True
while name != "Welcome!":
    name_length = len(name)
    if name == "Voldemort":
        print("You must not speak of that name!")
        all_names_are_sorted = False
        break
    if name_length < 5:
        house = "Gryffindor"
    elif name_length == 5:
        house = "Slytherin"
    elif name_length == 6:
        house = "Ravenclaw"
    elif name_length > 6:
        house = "Hufflepuff"
    print(f"{name} goes to {house}.")
    name = input()
if all_names_are_sorted:
    print("Welcome to Hogwarts.")
