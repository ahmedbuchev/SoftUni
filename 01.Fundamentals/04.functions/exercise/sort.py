def sort_nums_in_list(list_of_nums):
    return sorted(list_of_nums)


list_of_numbers = [int(el) for el in input().split()]
print(sort_nums_in_list(list_of_numbers))
