import re

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

emails = [el.group() for el in re.finditer(pattern, text)]
print(*emails, sep="\n")

# Ivan Shopov
#
# some_string = input()
# pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
# matches = re.findall(pattern, some_string)
# for match in matches:
#     print(match[0])