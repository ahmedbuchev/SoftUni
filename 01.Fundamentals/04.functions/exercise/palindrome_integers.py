def palindrome_numbers(num_as_str):
    reversed_num_as_str = num_as_str[::-1]
    if num_as_str == reversed_num_as_str:
        return True
    return False


list_of_numbers_as_string = [el for el in input().split(", ")]

x = list(map(palindrome_numbers, list_of_numbers_as_string))
print(*x, sep="\n")
