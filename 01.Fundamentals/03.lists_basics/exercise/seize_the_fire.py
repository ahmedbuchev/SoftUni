fire_input = input().split("#")
water = int(input())
effort = 0
total_fire = 0

print("Cells:")
fire_and_value_list = []

for i in range(len(fire_input)):
    data_is_valid = False
    fire_and_value_list = fire_input[i].split(" = ")

    type_of_fire = fire_and_value_list[0]
    value_of_cell = int(fire_and_value_list[1])

    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        data_is_valid = True
    if type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        data_is_valid = True
    if type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        data_is_valid = True

    if data_is_valid:
        if water - value_of_cell < 0:
            continue
        water -= value_of_cell
        effort += 0.25 * value_of_cell
        total_fire += value_of_cell
        print(f" - {value_of_cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
