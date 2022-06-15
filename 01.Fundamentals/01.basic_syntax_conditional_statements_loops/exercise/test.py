first_string = input()
second_string = input()
middle_string = ""
for index in range(len(first_string)):
    if first_string[index] != second_string[index]:
        middle_string = first_string[:index:]+second_string[index]+first_string[index+1::]
        first_string = middle_string
        print(middle_string)
