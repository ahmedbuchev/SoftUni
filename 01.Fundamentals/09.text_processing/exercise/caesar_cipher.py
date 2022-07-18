word = input()
encrypted_word = ""
for letter in word:
    encrypted_word += chr(ord(letter) + 3)

print(encrypted_word)
