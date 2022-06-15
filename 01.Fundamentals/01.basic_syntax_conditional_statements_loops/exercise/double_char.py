word = input()

while word != "End":
    if word != "SoftUni":
        for letter in word:
            print(letter * 2, end="")
        print()
    word = input()
