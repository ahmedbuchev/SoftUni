journal = [el for el in input().split(", ")]
command = input()
while command != "Craft!":
    data = command.split(" - ")
    cmd = data[0]
    item = data[1]

    if cmd == "Collect":
        if item not in journal:
            journal.append(item)
    elif cmd == "Drop":
        if item in journal:
            while item in journal:
                journal.remove(item)
    elif cmd == "Combine Items":
        old_new_item = item.split(":")
        old_item = old_new_item[0]
        new_item = old_new_item[1]
        if old_item in journal:
            index_old = journal.index(old_item)
            journal.insert(index_old + 1, new_item)
    elif cmd == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
    command = input()
print(", ".join(journal))
