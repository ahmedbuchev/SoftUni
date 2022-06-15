import math

persons = int(input())
capacity = int(input())

tours = math.ceil(persons / capacity)

print(tours)