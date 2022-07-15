data = input().split()
searched_product = input().split()
stocks = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = data[index + 1]
    stocks[key] = value

for s_p in searched_product:
    if s_p in stocks:
        print(f"We have {stocks[s_p]} of {s_p} left")
    else:
        print(f"Sorry, we don't have {s_p}")
