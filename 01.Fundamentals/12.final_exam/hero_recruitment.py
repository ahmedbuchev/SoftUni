command = input()
heroes_dict = {}

while not command == "End":
    command_split = command.split()
    cmd = command_split[0]

    if cmd == "Enroll":
        hero_name = command_split[1]

        if hero_name not in heroes_dict:
            heroes_dict[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif cmd == "Learn":
        hero_name, spell_name = command_split[1:]

        if hero_name not in heroes_dict:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes_dict[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes_dict[hero_name].append(spell_name)

    elif cmd == "Unlearn":
        hero_name, spell_name = command_split[1:]

        if hero_name not in heroes_dict:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes_dict[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes_dict[hero_name].remove(spell_name)
    command = input()

print("Heroes:")
for key, value in heroes_dict.items():

    print(f"== {key}: {', '.join([el for el in value])}")


