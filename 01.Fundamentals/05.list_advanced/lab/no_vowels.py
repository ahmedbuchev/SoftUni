list_of_vowels = ['a', 'o', 'u', 'e', 'i']
word = input()

result_list = [el for el in word if el.lower() not in list_of_vowels]
print("".join(result_list))
