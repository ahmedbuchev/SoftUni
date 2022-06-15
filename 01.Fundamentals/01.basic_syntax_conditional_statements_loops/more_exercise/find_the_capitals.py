word = input()
capital_letters_indexes = []
for index in range(len(word)):
    if word[index].isupper():
        capital_letters_indexes.append(index)

print(capital_letters_indexes)
