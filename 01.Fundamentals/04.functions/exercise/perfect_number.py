def perfect_number(num):
    divisor_list = []
    for i in range(1, num):
        if num % i == 0:
            divisor_list.append(i)
    if num == sum(divisor_list):
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
