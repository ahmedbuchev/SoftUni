import re

word = input()

pattern = r"(?<=(?P<symbol>(\=|/)))[A-Z][A-Za-z]{2,}(?=(?P=symbol))"

filtered = [el.group() for el in re.finditer(pattern, word)]

travel_points = sum([len(destination) for destination in filtered])

print(f'Destinations: {", ".join(filtered)}')
print(f"Travel Points: {travel_points}")
