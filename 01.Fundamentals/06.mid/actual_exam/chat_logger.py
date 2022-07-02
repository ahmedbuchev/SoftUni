chat_logger_list = []
command = input()

while not command == "end":
    command_list = command.split()
    if command_list[0] == "Chat":
        message = command_list[1]
        chat_logger_list.append(message)
    elif command_list[0] == "Delete":
        message = command_list[1]
        if message in chat_logger_list:
            chat_logger_list.remove(message)
    elif command_list[0] == "Edit":
        message = command_list[1]
        edited_version = command_list[2]
        if message in chat_logger_list:
            index = chat_logger_list.index(message)
            chat_logger_list[index] = edited_version
    elif command_list[0] == "Pin":
        message = command_list[1]
        if message in chat_logger_list:
            chat_logger_list.remove(message)
            chat_logger_list.append(message)
    elif command_list[0] == "Spam":
        for index in range(1, len(command_list)):
            chat_logger_list.append(command_list[index])
    command = input()
print("\n".join(chat_logger_list))
