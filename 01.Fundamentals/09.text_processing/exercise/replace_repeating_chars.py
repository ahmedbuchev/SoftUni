word = input()

clear_word = ""
previous_letter = ""
for letter in word:
    if letter != previous_letter:
        clear_word += letter

    previous_letter = letter

print(clear_word)
