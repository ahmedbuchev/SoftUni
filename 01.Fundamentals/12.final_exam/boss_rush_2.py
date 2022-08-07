import re
num = int(input())

for _ in range(num):
    word = input()
    pattern = r'(\|)(?P<name>[A-Z]{4,})(\|):(#)(?P<title>[A-Za-z]+\s[A-Za-z]+)(#)'

    result = [el.groupdict() for el in re.finditer(pattern, word)]

    if result:
        for index in range(len(result)):

            name = result[index]['name']
            title = result[index]['title']

            print(f"{name}, The {title}")
            print(f">> Strength: {len(name)}")
            print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
