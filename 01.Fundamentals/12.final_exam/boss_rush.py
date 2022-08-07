import re
num = int(input())

for _ in range(num):
    message = input()
    pattern = r"(\|[A-Z]{4,}\|):(#[A-Za-z]+\s[A-Za-z]+#)"
    result = re.findall(pattern, message)
    if result:
        name = result[0][0][1:-1]
        title = result[0][1][1:-1]

        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")

    else:
        print("Access denied!")
