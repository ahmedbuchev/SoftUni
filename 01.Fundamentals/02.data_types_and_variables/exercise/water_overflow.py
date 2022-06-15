capacity = 255
number_of_lines = int(input())
water_inside_the_tank = 0
for i in range(number_of_lines):
    current_liters_of_water = int(input())
    if current_liters_of_water <= capacity:
        capacity -= current_liters_of_water
        water_inside_the_tank += current_liters_of_water
    else:
        print("Insufficient capacity!")
print(water_inside_the_tank)