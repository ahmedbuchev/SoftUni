encrypted_message = input()
command = input()
new_message = ""
while not command == "Decode":
    command_split = command.split("|")
    if command_split[0] == "Move":
        number_of_letters = int(command_split[1])
        new_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif command_split[0] == "Insert":
        index, value = int(command_split[1]), command_split[2]
        new_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command_split[0] == "ChangeAll":
        substring, replacement = command_split[1], command_split[2]
        new_message = encrypted_message.replace(substring, replacement)
    encrypted_message = new_message
    command = input()
print(f"The decrypted message is: {new_message}")

