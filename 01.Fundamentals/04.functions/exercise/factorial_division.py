def factorial_division(num_1, num_2):
    fact_1 = 1
    fact_2 = 1
    for i in range(1, num_1 + 1):
        fact_1 *= i
    for j in range(1, num_2 + 1):
        fact_2 *= j
    return fact_1 / fact_2


number_1 = int(input())
number_2 = int(input())
result = factorial_division(number_1, number_2)
print(f"{result:.2f}")
