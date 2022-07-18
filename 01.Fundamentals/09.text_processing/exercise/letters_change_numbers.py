words = input().split()
result = 0
total_sum=0

for word in words:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        result = number / first_letter_position

    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        result = number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        result -= last_letter_position

    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        result += last_letter_position

    total_sum += result
    result = 0
print(f"{total_sum:.2f}")

