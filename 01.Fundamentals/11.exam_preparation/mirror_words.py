import re

message = input()
new_list = []
new_word = ""
final_list = []

pattern = r"(?P<sep>(#|@))([A-Za-z]{3,})(?P=sep)(?P=sep)([A-Za-z]{3,})(?P=sep)"

result = [el.group() for el in re.finditer(pattern, message)]

for el in result:
    symbol_to_remove = el[0]
    new_word = el.replace(symbol_to_remove, "")
    new_list.append(new_word)

for el in new_list:
    length = len(el)//2
    if el[:length] == el[len(el)-1:length-1:-1]:
        final_list.append(el[:length] + " <=> " + el[length:])

if not new_list:
    print("No word pairs found!")
else:
    print(f"{len(new_list)} word pairs found!")

if not final_list:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*final_list, sep=", ")

