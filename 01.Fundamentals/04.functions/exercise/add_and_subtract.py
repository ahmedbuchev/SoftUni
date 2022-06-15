def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum_1, num_3):
    return sum_1 - num_3


def add_and_subtract(num_1, num_2, num_3):
    sum_1 = sum_numbers(num_1, num_2)
    result = subtract(sum_1, num_3)

    return result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))
