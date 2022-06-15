def print_char_in_range(first_char, second_char):
    return [chr(el) for el in range(ord(first_char) + 1, ord(second_char))]


first_letter = input()
second_letter = input()

result = print_char_in_range(first_letter, second_letter)
print(" ".join(result))
