import re

text = input()
sum_calories = 0
pattern = r'(?P<separator>#|\|)(?P<name>[a-zA-Z\s]+)' \
          r'(?P=separator)(?P<date>\d{2}/\d{2}/\d{2})' \
          r'(?P=separator)(?P<calories>[1-9][0-9]{0,3}|10000)(?P=separator)'
filtered_text = re.finditer(pattern, text)

items = []
dates = []
calories = []

for el in filtered_text:
    sum_calories += int(el.groupdict()['calories'])
    dates.append(el.groupdict()['date'])
    calories.append(el.groupdict()['calories'])
    items.append(el.groupdict()['name'])

days_can_last = sum_calories // 2000
print(f"You have food to last you for: {days_can_last} days!")

for index in range(len(items)):
    print(f"Item: {items[index]}, Best before: {dates[index]}, Nutrition: {calories[index]}")



