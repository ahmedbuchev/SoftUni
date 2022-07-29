stops = input()
data = input()
new_stops = ""

while not data == "Travel":
    data_unpacked = data.split(":")
    command = data_unpacked[0]

    if command == "Add Stop":
        index, string = int(data_unpacked[1]), data_unpacked[2]
        if index in range(len(stops)):
            new_stops = stops[:index] + string + stops[index:]
            stops = new_stops
        print(stops)

    elif command == "Remove Stop":
        start_index, end_index = int(data_unpacked[1]), int(data_unpacked[2])

        if start_index in range(len(stops)) and end_index in range(len(stops)):
            new_stops = stops[:start_index] + stops[end_index + 1:]
            stops = new_stops
        print(stops)

    elif command == "Switch":
        old_string, new_string = data_unpacked[1], data_unpacked[2]

        if old_string in stops:
            new_stops = stops.replace(old_string, new_string)
            stops = new_stops
        print(stops)

    data = input()

print(f"Ready for world tour! Planned stops: {stops}")

