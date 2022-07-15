command = input()
phonebook = {}
while "-" in command:
    name, number = command.split("-")
    phonebook[name] = number
    command = input()

num = int(command)

for index in range(num):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
