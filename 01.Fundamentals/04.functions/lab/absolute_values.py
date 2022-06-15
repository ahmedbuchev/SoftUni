def absolute_values(list_of_nums):
    list_of_absolute_values = [abs(el) for el in list_of_nums]
    print(list_of_absolute_values)


list_of_numbers = [float(el) for el in input().split()]
absolute_values(list_of_numbers)
