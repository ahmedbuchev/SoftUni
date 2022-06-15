num_of_electrons = int(input())
counter = 1
electron_distribution = []
while num_of_electrons > 0:
    current_layer = 2 * counter ** 2
    if num_of_electrons > current_layer:
        num_of_electrons -= current_layer
        electron_distribution.append(current_layer)
    else:
        electron_distribution.append(num_of_electrons)
        num_of_electrons = 0

    counter += 1

print(electron_distribution)
