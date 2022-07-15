resource_mineral = input()

collected_minerals = {}
while not resource_mineral == "stop":
    quantity = int(input())
    if resource_mineral not in collected_minerals:
        collected_minerals[resource_mineral] = 0
    collected_minerals[resource_mineral] += quantity
    resource_mineral = input()

for key, value in collected_minerals.items():
    print(f"{key} -> {value}")
