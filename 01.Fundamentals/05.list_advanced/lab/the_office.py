happy_list = [int(el) for el in input().split()]
factor = int(input())
multiply_list = [el * factor for el in happy_list]
average_happiness = sum(multiply_list) / len(multiply_list)
happy = [el for el in multiply_list if el >= average_happiness]

if len(happy) >= len(multiply_list) / 2:
    print(f"Score: {len(happy)}/{len(multiply_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy)}/{len(multiply_list)}. Employees are not happy!")
