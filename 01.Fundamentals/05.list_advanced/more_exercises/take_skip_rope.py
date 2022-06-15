message = input()
nums_list = []
non_nums_list = []

for letter in message:
    if letter.isdigit():
        nums_list.append(letter)
    else:
        non_nums_list.append(letter)
nums_list = [int(el) for el in nums_list]

take_list = [nums_list[i] for i in range(len(nums_list)) if i % 2 == 0]
skip_list = [nums_list[i] for i in range(len(nums_list)) if i % 2 != 0]

final_list = []
start = 0
for i in range(len(take_list)):
    final_list += non_nums_list[start:take_list[i]+start]
    start += take_list[i] + skip_list[i]

print("".join(final_list))
