list_of_numbers = input().split()
opposite_numbers = []
for i in range(len(list_of_numbers)):
    opposite_num = -int(list_of_numbers[i])
    opposite_numbers.append(opposite_num)
print(opposite_numbers)

# print([-int(el) for el in input().split()])
