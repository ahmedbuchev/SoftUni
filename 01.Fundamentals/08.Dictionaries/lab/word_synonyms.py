n = int(input())
synonyms = {}
for index in range(n):
    key = input()
    value = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)} ")
