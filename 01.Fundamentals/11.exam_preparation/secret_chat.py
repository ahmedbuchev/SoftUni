message = input()
command = input()
new_message = ""
while not command == "Reveal":
    command_split = command.split(":|:")
    cmd = command_split[0]
    if cmd == "InsertSpace":
        index = int(command_split[1])
        new_message = message[:index] + " " + message[index:]
        message = new_message
        print(message)

    elif cmd == "Reverse":
        substring = command_split[1]
        if substring in message:
            new_message = message.replace(substring, "", 1)
            message = new_message + substring[::-1]
            print(message)
        else:
            print("error")

    elif cmd == "ChangeAll":
        substring, replacement = command_split[1:]

        new_message = message.replace(substring, replacement)
        message = new_message
        print(message)

    command = input()

print(f"You have a new text message: {message}")
