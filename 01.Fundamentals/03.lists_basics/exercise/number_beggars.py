sums_list = input().split(", ")
count_of_beggars = int(input())
final_list = []
counter = 0
temp_sum = 0
sums_list_as_digits = []

for i in range(len(sums_list)):
    sums_list_as_digits.append(int(sums_list[i]))

while counter < count_of_beggars:
    for i in range(counter, len(sums_list_as_digits), count_of_beggars):
        temp_sum += sums_list_as_digits[i]

    final_list.append(temp_sum)
    temp_sum = 0
    counter += 1

print(final_list)
