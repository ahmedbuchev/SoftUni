command = input()
coffees_count = 0
while not command == "END":
    if command.lower() == "cat" or command.lower() == "dog" or\
            command.lower() == "coding" or command.lower() == "movie":
        if command.islower():
            coffees_count += 1
        if command.isupper():
            coffees_count += 2

    command = input()

if coffees_count > 5:
    print("You need extra sleep")
else:
    print(coffees_count)
