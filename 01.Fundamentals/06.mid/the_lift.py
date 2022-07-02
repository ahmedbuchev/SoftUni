people = int(input())
lift = [int(el) for el in input().split()]
for index in range(len(lift)):
    empty_places_in_wagon = 4 - lift[index]
    if empty_places_in_wagon > 0:
        if people - empty_places_in_wagon >= 0:
            people -= empty_places_in_wagon
            lift[index] += empty_places_in_wagon
        else:
            lift[index] = people
            people = 0
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift, sep=" ")
elif people == 0 and len(lift) > lift.count(4):
    print("The lift has empty spots!")
    print(*lift, sep=" ")
else:
    print(*lift, sep=" ")

