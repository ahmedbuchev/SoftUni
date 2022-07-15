data = input().split()

letters = {}

for word in data:
    for char in word:
        if char not in letters:
            letters[char] = 0
        letters[char] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")
