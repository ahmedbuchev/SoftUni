neighborhood = [int(el) for el in input().split("@")]
command = input()
index = 0
counter = 0
while command != "Love!":
    command_list = [el for el in command.split()]
    index += int(command_list[1])
    if index > len(neighborhood) - 1:
        index = 0
    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")
            counter += 1
    command = input()

print(f"Cupid's last position was {index}.")
if counter == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - counter} places.")