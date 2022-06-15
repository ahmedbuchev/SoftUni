times_list = list(map(int, input().split()))
middle = len(times_list) // 2
left_times_list = times_list[:middle]
right_times_list = times_list[(len(times_list) - 1): middle: - 1]
left_time_sum = 0
right_time_sum = 0
for l_time in left_times_list:
    if l_time == 0:
        left_time_sum *= 0.8
    else:
        left_time_sum += l_time

for r_time in right_times_list:
    if r_time == 0:
        right_time_sum *= 0.8
    else:
        right_time_sum += r_time

if left_time_sum < right_time_sum:
    print(f"The winner is left with total time: {left_time_sum:.1f}")

elif right_time_sum < left_time_sum:
    print(f"The winner is right with total time: {right_time_sum:.1f}")