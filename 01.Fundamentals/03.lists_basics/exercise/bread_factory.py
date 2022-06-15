energy = 100
coins = 100
event_and_num = input().split("|")
is_closed = False
for index in range(len(event_and_num)):
    event_and_num_list = event_and_num[index].split("-")
    event = event_and_num_list[0]
    number = int(event_and_num_list[1])
    if event == "rest":
        energy_before = energy
        energy += number
        if energy >= 100:
            energy = 100
            print(f"You gained {energy - energy_before} energy.")
        else:

            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - number >= 0:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

