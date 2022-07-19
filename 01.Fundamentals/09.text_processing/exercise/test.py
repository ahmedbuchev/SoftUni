# def numbers(num_1, num_2):
#     for el in range(num_1, num_2 + 1):
#         if el % 2 == 0 and el % 5 == 0:
#             print(el, end=" ")
#
#
# numbers(1, 1001)

print(*[el for el in range(1, 1001) if el % 2 == 0 and el % 5 == 0])
