nums = [int(el) for el in input().split(", ")]
group_of_nums = 10
counter = 0
while counter < len(nums):
    collected_numbers = []
    for n in nums:
        if group_of_nums - 10 < n <= group_of_nums:
            collected_numbers.append(n)
            counter += 1
    print(f"Group of {group_of_nums}'s: {collected_numbers}")
    group_of_nums += 10
