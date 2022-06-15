list_of_input = input().split()
list_of_int = list(map(int, list_of_input))
numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    list_of_int.remove(min(list_of_int))

list_of_str = list(map(str, list_of_int))
print(", ".join(list_of_str))
