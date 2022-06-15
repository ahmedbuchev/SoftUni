def even_numbers_from_list(list_of_nums):
    return [el for el in list_of_nums if el % 2 == 0]


list_of_numbers = [int(el) for el in input().split()]
print(even_numbers_from_list(list_of_numbers))
