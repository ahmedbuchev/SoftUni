word = input()
new_word = ""

command = input()
while not command == "Done":
    command_split = command.split()
    cmd = command_split[0]

    if cmd == "TakeOdd":
        new_word = word[1::2]
        word = new_word
        print(word)

    elif cmd == "Cut":
        index, length = int(command_split[1]), int(command_split[2])
        searched_word = word[index:index + length:]
        new_word = word.replace(searched_word, "", 1)
        word = new_word
        print(word)

    elif cmd == "Substitute":
        substring, substitute = command_split[1:]
        if substring in word:
            new_word = word.replace(substring, substitute)
            word = new_word
            print(word)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {word}")