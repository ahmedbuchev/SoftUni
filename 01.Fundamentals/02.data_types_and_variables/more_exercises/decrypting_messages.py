key = int(input())
lines = int(input())
decrypted_word = ""
for i in range(lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    decrypted_word += new_letter

print(decrypted_word)
