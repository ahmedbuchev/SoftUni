nums_list = input().split()
k = int(input())
index = 0
counter = 0
final_list = []
while nums_list:
    counter += 1
    if counter % k == 0:
        final_list.append(nums_list.pop(index))
    else:
        index += 1

    if index >= len(nums_list):
        index = 0

# final_list = [int(el) for el in final_list]
# print("[", end="")
# for index in range(len(final_list)):
#     print(f"{final_list[index]}", end="")
#     if not index == len(final_list) - 1:
#         print(",", end="")
# print("]")
print(str(final_list).replace(' ', '').replace('\'', ''))
