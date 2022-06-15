def positive_or_negative(num_1, num_2, num_3):
    list_of_nums = [num_1, num_2, num_3]
    list_of_negative_nums = [el for el in list_of_nums if el < 0]

    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        return "zero"

    if len(list_of_negative_nums) == 1:
        return "negative"

    if len(list_of_negative_nums) == 2:
        return "positive"

    if len(list_of_negative_nums) == 3:
        return "negative"

    if not list_of_negative_nums:
        return "positive"


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(positive_or_negative(number_1, number_2, number_3))
