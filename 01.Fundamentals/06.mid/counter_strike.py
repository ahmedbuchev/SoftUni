energy = int(input())
command = input()
won_battles = 0
not_enough_energy = False
while not command == "End of battle":
    distance = int(command)
    if energy - distance >= 0:
        energy -= distance
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles
    else:
        not_enough_energy = True
        break
    command = input()
if not_enough_energy:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
