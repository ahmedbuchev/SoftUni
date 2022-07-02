nums = [int(el) for el in input().split()]
average = sum(nums) / len(nums)

above_average = [el for el in nums if el > average]
top_five = []

for index in range(5):
    max_num = max(above_average)
    top_five.append(max_num)
    above_average.remove(max_num)
print(top_five)

