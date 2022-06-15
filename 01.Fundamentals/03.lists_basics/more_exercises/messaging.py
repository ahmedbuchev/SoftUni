number_list_as_string = input().split()
sentence_as_string = list(input())
number_as_string = []
new_list = []
sum_of_current_number = 0
for index in range(len(number_list_as_string)):
    number_as_string = list(number_list_as_string[index])
    sum_of_current_number = 0
    for num in number_as_string:
        sum_of_current_number += int(num)

    if sum_of_current_number > len(sentence_as_string):
        diff = sum_of_current_number % len(sentence_as_string)
    else:
        diff = sum_of_current_number
    new_list.append(sentence_as_string.pop(diff))

print("".join(new_list))
