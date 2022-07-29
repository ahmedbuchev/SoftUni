number_of_cars = int(input())
cars_dict = {}

for current_car in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage, fuel = int(mileage), int(fuel)

    cars_dict[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while not command == "Stop":
    command_split = command.split(" : ")
    cmd = command_split[0]

    if cmd == "Drive":
        car, distance, fuel = command_split[1:]
        distance, fuel = int(distance), int(fuel)
        if fuel > cars_dict[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['mileage'] += distance
            cars_dict[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del cars_dict[car]

    elif cmd == "Refuel":
        car, fuel = command_split[1:]
        fuel = int(fuel)

        if cars_dict[car]['fuel'] + fuel > 75:
            fuel = 75 - cars_dict[car]['fuel']
            cars_dict[car]['fuel'] = 75
        else:
            cars_dict[car]['fuel'] += fuel

        print(f"{car} refueled with {fuel} liters")

    elif cmd == "Revert":
        car, kilometers = command_split[1:]
        kilometers = int(kilometers)

        if cars_dict[car]['mileage'] - kilometers <= 10000:
            cars_dict[car]['mileage'] = 10000
        else:
            cars_dict[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
for car, value in cars_dict.items():
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

