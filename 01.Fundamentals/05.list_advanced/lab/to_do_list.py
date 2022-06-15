command = input()
notes_list = [0] * 10
while not command == "End":
    importance, text = command.split("-")
    index = importance - 1
    notes_list[index] = text
    command = input()
while 0 in notes_list:
    notes_list.remove(0)
print(notes_list)
