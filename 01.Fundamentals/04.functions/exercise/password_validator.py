def password_validator(passwd):
    len_is_ok = False
    letters_and_digits = False
    at_least_two_digits = False
    passwd_list = [ch for ch in passwd]
    digit_list = []

    if 6 <= len(passwd) <= 10:
        len_is_ok = True

    if passwd.isalnum():
        letters_and_digits = True

    for letter in passwd_list:
        if letter.isdigit():
            digit_list.append(letter)
    if len(digit_list) >= 2:
        at_least_two_digits = True

    return len_is_ok, letters_and_digits, at_least_two_digits


password = input()
length_is_ok, letters_and_digits_ok, at_least_two_digits_ok = password_validator(password)

if not length_is_ok:
    print("Password must be between 6 and 10 characters")
if not letters_and_digits_ok:
    print("Password must consist only of letters and digits")
if not at_least_two_digits_ok:
    print("Password must have at least 2 digits")
if all(password_validator(password)):
    print("Password is valid")
