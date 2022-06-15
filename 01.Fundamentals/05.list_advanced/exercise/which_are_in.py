first_list = input().split(", ")
second_list = input().split(", ")
final_list = []
for word_1 in first_list:
    for word_2 in second_list:
        if word_1 in word_2 and word_1 not in final_list:
            final_list.append(word_1)
print(final_list)
