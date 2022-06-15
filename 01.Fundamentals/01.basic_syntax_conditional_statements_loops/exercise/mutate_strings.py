starting_string = input()
ending_string = input()

for i in range(len(starting_string)):
    if starting_string[i] != ending_string[i]:
        new_string = starting_string[:i] + ending_string[i] + starting_string[i + 1:]
        starting_string = new_string
        print(starting_string)
