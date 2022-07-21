import re

text = input()
pattern = r"(^_|(?<=\s_))[A-Za-z0-9]+\b"

result = re.finditer(pattern, text)
print(*[el.group() for el in result], sep=",")
