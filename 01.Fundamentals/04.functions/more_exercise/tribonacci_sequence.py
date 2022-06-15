def tribonacci_sequence(num):
    list_of_numbers = [0, 0, 1]
    last_three_numbers = list_of_numbers[-3::]
    for i in range(num - 1):
        list_of_numbers.append(sum(last_three_numbers))
        last_three_numbers = list_of_numbers[-3::]
    while 0 in list_of_numbers:
        list_of_numbers.remove(0)
    return list_of_numbers


number = int(input())
print(*tribonacci_sequence(number))
