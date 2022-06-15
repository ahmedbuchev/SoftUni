gifts_list = input().split()
command = input()
command_list = command.split()

while command != "No Money":
    if "OutOfStock" in command:
        gift = command_list[1]
        while gift in gifts_list:
            gift_index = gifts_list.index(gift)
            gifts_list[gift_index] = "None"
    elif "Required" in command:
        index = int(command_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = command_list[1]
    elif "JustInCase" in command:
        gifts_list[-1] = command_list[1]

    command = input()
    command_list = command.split()
while "None" in gifts_list:
    gifts_list.remove("None")

print(" ".join(gifts_list))
