# number = int(input())
# number_as_string = str(number)
# new_list = list()
# final_string = ""
# for letter in number_as_string:
#     new_list.append(letter)
# sort_list = sorted(new_list, reverse=True)
#
# for i in range(len(sort_list)):
#     final_string += sort_list[i]
#
# print(final_string)

number_as_string = input()
list_of_char = [ch for ch in number_as_string]
list_of_char.sort(reverse=True)
print("".join(list_of_char))
