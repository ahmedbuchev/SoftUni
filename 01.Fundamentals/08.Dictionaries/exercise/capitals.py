countries = input().split(", ")
capitals = input().split(", ")

country_capital_dict = dict(zip(countries, capitals))

for key, value in country_capital_dict.items():
    print(f"{key} -> {value}")
