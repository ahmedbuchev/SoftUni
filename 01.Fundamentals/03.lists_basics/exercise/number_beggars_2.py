sums_list = input().split(", ")
count_of_beggars = int(input())

sums_list_as_num = list(map(int, sums_list))
final_list = []
for beggar in range(count_of_beggars):
    temp_sum = sum(sums_list_as_num[beggar::count_of_beggars])
    final_list.append(temp_sum)
    temp_sum = 0
print(final_list)

