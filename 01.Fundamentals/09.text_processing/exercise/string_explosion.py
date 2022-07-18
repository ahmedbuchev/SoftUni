word = input()
explosion_strength = 0
clear_word = ""

for index in range(len(word)):
    if explosion_strength > 0 and word[index] != ">":
        explosion_strength -= 1
    elif word[index] == ">":
        explosion_strength += int(word[index + 1])
        clear_word += word[index]
    else:
        clear_word += word[index]

print(clear_word)
