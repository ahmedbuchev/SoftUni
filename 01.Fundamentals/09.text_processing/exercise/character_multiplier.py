first_string, second_string = input().split()
total_sum = 0
longer_string = ""
shorter_string = ""
len_to_multiply = 0
rest_len = 0

if len(first_string) > len(second_string):
    longer_string = first_string
    shorter_string = second_string

elif len(second_string) > len(first_string):
    longer_string = second_string
    shorter_string = first_string

else:   #equal
    longer_string = first_string
    shorter_string = second_string

diff = len(longer_string) - len(shorter_string)

len_to_multiply = len(longer_string) - diff
rest_len = diff
rest_word = longer_string[len(shorter_string):len(longer_string):]

for index in range(len_to_multiply):
    total_sum += ord(longer_string[index]) * ord(shorter_string[index])

if rest_len:
    for index in range(rest_len):
        total_sum += ord(rest_word[index])

print(total_sum)
