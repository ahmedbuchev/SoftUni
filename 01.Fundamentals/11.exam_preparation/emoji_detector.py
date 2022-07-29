import re

pattern = r'(?P<symbol>::|\*\*)[A-Z][a-z]{2,}(?P=symbol)'
pattern_digits = r'\d'
text = input()
cool_threshold = 1

result = [el.group() for el in re.finditer(pattern, text)]
result_digits = re.findall(pattern_digits, text)

for el in result_digits:
    cool_threshold *= int(el)

print(f'Cool threshold: {cool_threshold}')

print(f'{len(result)} emojis found in the text. The cool ones are:')
coolness = 0
for el in result:
    clear_el = el[2:-2:]
    for letter in clear_el:
        coolness += ord(letter)
    if coolness > cool_threshold:
        print(el)
    coolness = 0
