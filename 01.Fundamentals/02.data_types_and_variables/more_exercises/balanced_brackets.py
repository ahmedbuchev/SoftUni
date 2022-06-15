number_of_lines = int(input())
is_balanced = False
opening_brackets = 0
closing_brackets = 0
for i in range(number_of_lines):
    letter = input()
    if letter == "(":
        opening_brackets += 1

    if letter == ")":
        closing_brackets += 1
    if opening_brackets == 1 and closing_brackets == 1:
        opening_brackets = 0
        closing_brackets = 0

is_balanced = opening_brackets == closing_brackets
if opening_brackets > 1 or closing_brackets > 1:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
