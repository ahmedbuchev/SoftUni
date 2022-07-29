raw_activation_key = input()

command = input()
while not command == "Generate":
    command_split = command.split(">>>")
    cmd = command_split[0]

    if cmd == "Contains":
        substring = command_split[1]

        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif cmd == "Flip":
        upper_or_lower, start_index, end_index = command_split[1:]
        start_index, end_index = int(start_index), int(end_index)

        if upper_or_lower == "Upper":
            new_word = raw_activation_key[:start_index] + \
                   raw_activation_key[start_index:end_index:].upper() + \
                   raw_activation_key[end_index:]
        else:
            new_word = raw_activation_key[:start_index] + \
                   raw_activation_key[start_index:end_index:].lower() + \
                   raw_activation_key[end_index:]
        raw_activation_key = new_word
        print(raw_activation_key)

    elif cmd == "Slice":
        start_index, end_index = int(command_split[1]), int(command_split[2])

        new_word = raw_activation_key[:start_index] + raw_activation_key[end_index:]

        raw_activation_key = new_word
        print(raw_activation_key)
    command = input()

print(f"Your activation key is: {raw_activation_key}")
