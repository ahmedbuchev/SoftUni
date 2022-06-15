def min_max_sum(list_of_nums):
    min_num = min(list_of_nums)
    max_num = max(list_of_nums)
    sum_of_nums = sum(list_of_nums)
    return min_num, max_num, sum_of_nums


list_of_numbers = [int(el) for el in input().split()]

min_number, max_number, sum_of_numbers = min_max_sum(list_of_numbers)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_of_numbers}")
