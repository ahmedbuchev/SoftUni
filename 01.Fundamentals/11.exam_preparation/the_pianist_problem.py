num = int(input())
pieces = {}

for index in range(num):
    piece, composer, key = input().split("|")
    if piece not in pieces:
        pieces[piece] = {}
    pieces[piece][composer] = key

command = input()
while not command == "Stop":
    command_unpacked = command.split("|")
    cmd = command_unpacked[0]

    if cmd == "Add":
        piece, composer, key = command_unpacked[1], command_unpacked[2], command_unpacked[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {}
            pieces[piece][composer] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif cmd == "Remove":
        piece = command_unpacked[1]
        if piece in pieces:
            print(f"Successfully removed {piece}!")
            del pieces[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif cmd == "ChangeKey":
        piece, new_key = command_unpacked[1], command_unpacked[2]
        if piece in pieces:
            print(f"Changed the key of {piece} to {new_key}!")
            pieces[piece][composer] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, value in pieces.items():
    for composer, key in value.items():
        print(f"{piece} -> Composer: {composer}, Key: {key}")

