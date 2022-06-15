string = input().lower()
counter = 0

searched_words = ["sand", "water", "fish", "sun"]

for word in searched_words:
    counter += string.count(word)
print(counter)
