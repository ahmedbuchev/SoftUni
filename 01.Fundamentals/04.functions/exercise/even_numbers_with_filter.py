def even_numbers_from_list(num):
    if num % 2 == 0:
        return True
    return False


list_of_numbers = [int(el) for el in input().split()]

even_num_list = list(filter(even_numbers_from_list, list_of_numbers))
print(even_num_list)
