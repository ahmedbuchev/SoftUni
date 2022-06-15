def odd_and_even_sum(num_as_str):
    even_sum = 0
    odd_sum = 0
    for ch in num_as_str:
        digit = int(ch)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return odd_sum, even_sum


number_as_string = input()
sum_of_odd_numbers, sum_of_even_numbers = odd_and_even_sum(number_as_string)
print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")
