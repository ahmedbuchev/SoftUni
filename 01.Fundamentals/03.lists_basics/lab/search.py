number_of_lines = int(input())
word = input()
full_list = list()
filtered_list = list()
for i in range(number_of_lines):
    current = input()
    full_list.append(current)
    if word in current:
        filtered_list.append(current)
print(full_list)
print(filtered_list)
