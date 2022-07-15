data = input()
force_book = {}
while not data == "Lumpawaroo":
    if "|" in data:
        force_side, force_user = data.split(" | ")
        user_in_dict = False

        for value in force_book.values():
            if force_user in value:
                user_in_dict = True
                break
        if not user_in_dict:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)

    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        for key, value in force_book.items():
            if force_user in value:
                force_book[key].pop(value.index(force_user))
                break
        if force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        else:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    data = input()

for force_side, value in force_book.items():
    if value:
        print(f"Side: {force_side}, Members: {len(value)}")
        for index in range(len(value)):
            print(f"! {value[index]}")
