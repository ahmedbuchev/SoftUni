all_friends_list = input().split(", ")
counter_blacklisted = 0
counter_lost = 0
command = input()
while not command == "Report":
    command_list = command.split()
    if command_list[0] == "Blacklist":
        name = command_list[1]
        if name in all_friends_list:
            index = all_friends_list.index(name)
            all_friends_list[index] = "Blacklisted"
            counter_blacklisted += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif command_list[0] == "Error":
        index = int(command_list[1])
        if 0 <= index < len(all_friends_list) \
                and not all_friends_list[index] == "Blacklisted" \
                and not all_friends_list[index] == "Lost":
            name = all_friends_list[index]
            all_friends_list[index] = "Lost"
            print(f"{name} was lost due to an error.")
            counter_lost += 1
    elif command_list[0] == "Change":
        index = int(command_list[1])
        new_name = command_list[2]
        if 0 <= index < len(all_friends_list):
            old_name = all_friends_list[index]
            all_friends_list[index] = new_name
            print(f"{old_name} changed his username to {new_name}.")
    command = input()
print(f"Blacklisted names: {counter_blacklisted}")
print(f"Lost names: {counter_lost}")
print(" ".join(all_friends_list))
