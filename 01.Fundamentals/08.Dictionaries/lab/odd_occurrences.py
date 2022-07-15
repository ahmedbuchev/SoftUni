words_list = input().split()
words_dict = {}

for word in words_list:
    word_lower = word.lower()
    if word_lower not in words_dict:
        words_dict[word_lower] = 1
    else:
        words_dict[word_lower] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
