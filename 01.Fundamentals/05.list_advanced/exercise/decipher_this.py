list_of_words = input().split()
num_as_string = ""
final_list =[]
for word in list_of_words:
    for letter in word:
        if letter.isdigit():
            num_as_string += letter
    first_letter = chr(int(num_as_string))

    word = word.replace(num_as_string, first_letter)

    num_as_string = ""
    list_of_w = list(word)
    list_of_w[1], list_of_w[-1] = list_of_w[-1], list_of_w[1]
    word = "".join(list_of_w)
    final_list.append(word)
print(" ".join(final_list))
    



