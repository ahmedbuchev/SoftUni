numbers_list = list(map(int, input().split(", ")))

for index in range(len(numbers_list) - 1, - 1, -1):
    if numbers_list[index] == 0:
        numbers_list.pop(index)
        numbers_list.append(0)
print(numbers_list)
