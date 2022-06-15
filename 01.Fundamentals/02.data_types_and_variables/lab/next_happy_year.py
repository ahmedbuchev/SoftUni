year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    string_year = str(year)
    set_year = set(string_year)
    is_happy_year = len(string_year) == len(set_year)

print(year)
