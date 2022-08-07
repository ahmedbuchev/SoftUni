message = input()

command = input()
while not command == "Finish":
    command_split = command.split()
    cmd = command_split[0]

    if cmd == "Replace":
        current_char, new_char = command_split[1:]

        new_message = message.replace(current_char, new_char)
        message = new_message
        print(message)

    elif cmd == "Cut":
        start_index, end_index = command_split[1:]
        start_index, end_index = int(start_index), int(end_index)

        if start_index in range(len(message)) and end_index in range(len(message)):
            new_message = message[:start_index] + message[end_index + 1:]
            message = new_message
            print(message)
        else:
            print("Invalid indices!")

    elif cmd == "Make":
        upper_or_lower = command_split[1]

        if upper_or_lower == "Upper":
            new_message = message.upper()
            message = new_message
            print(message)
        elif upper_or_lower == "Lower":
            new_message = message.lower()
            message = new_message
            print(message)

    elif cmd == "Check":
        string = command_split[1]

        if string in message:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif cmd == "Sum":
        start_index, end_index = command_split[1:]
        start_index, end_index = int(start_index), int(end_index)

        if start_index in range(len(message)) and end_index in range(len(message)):
            substring = message[start_index:end_index + 1]
            substring_ascii = [ord(ch) for ch in substring]
            sum_ascii = sum(substring_ascii)
            print(sum_ascii)
        else:
            print("Invalid indices!")

    command = input()
