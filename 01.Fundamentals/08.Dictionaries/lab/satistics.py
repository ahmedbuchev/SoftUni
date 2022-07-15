command = input()
stocks = {}
while not command == "statistics":
    key, value = command.split(": ")
    if key in stocks:
        stocks[key] += int(value)
    else:
        stocks[key] = int(value)
    command = input()
print("Products in stock:")
for key, value in stocks.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(stocks)}")
print(f"Total Quantity: {sum(stocks.values())}")
