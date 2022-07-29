command = input()
city_dict = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    population, gold = int(population), int(gold)
    if city not in city_dict:
        city_dict[city] = {'population': population, 'gold': gold}
    else:
        city_dict[city]['population'] += population
        city_dict[city]['gold'] += gold
    command = input()

event = input()
while not event == "End":
    event_split = event.split("=>")
    evn = event_split[0]

    if evn == "Plunder":
        town, people, gold = event_split[1:]
        people, gold = int(people), int(gold)

        city_dict[town]['population'] -= people
        city_dict[town]['gold'] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if city_dict[town]['population'] <= 0 or city_dict[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del city_dict[town]

    elif evn == "Prosper":
        town, gold = event_split[1:]
        gold = int(gold)

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_dict[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_dict[town]['gold']} gold.")

    event = input()

if city_dict:
    print(f"Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:")
    for city, value in city_dict.items():
        print(f"{city} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
