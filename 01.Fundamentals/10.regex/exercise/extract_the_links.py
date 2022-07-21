import re

text = input()
pattern = r"www\.[A-Za-z0-9-]+(\.[a-z]+)+"
sites = []
while text:
    valid_sites = [el.group() for el in re.finditer(pattern, text)]
    if valid_sites:
        sites.extend(valid_sites)
    text = input()

print(*sites, sep="\n")

