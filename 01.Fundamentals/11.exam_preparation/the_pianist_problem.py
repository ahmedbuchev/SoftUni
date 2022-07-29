num = int(input())
pieces = {}

for index in range(num):
    piece, composer, key = input().split("|")

    pieces[piece] = {'composer': composer, 'key': key}

command = input()
while not command == "Stop":
    command_unpacked = command.split("|")
    cmd = command_unpacked[0]

    if cmd == "Add":
        piece, composer, key = command_unpacked[1:]

        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif cmd == "Remove":
        piece = command_unpacked[1]

        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif cmd == "ChangeKey":
        piece, new_key = command_unpacked[1:]

        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, value in pieces.items():
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")

