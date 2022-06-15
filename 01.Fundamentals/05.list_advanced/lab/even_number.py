numbers_list = [int(el) for el in input().split(", ")]
final_list = [i for i in range(len(numbers_list)) if numbers_list[i] % 2 == 0]
print(final_list)

# number_list = list(map(int, input().split(", ")))
# found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))
# even_indices = list(filter(lambda a: a != "no", found_indices_or_no))
# print(even_indices)

# numbers_list = [int(el) for el in input().split(", ")]
# even_index_list = []
# for index, value in enumerate(numbers_list):
#     if value % 2 == 0:
#         even_index_list.append(index)
# print(even_index_list)
