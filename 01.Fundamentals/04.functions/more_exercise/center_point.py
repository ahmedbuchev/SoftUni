import math


def closest_to_center(x_1, y_1, x_2, y_2):
    distance_to_1 = math.sqrt(x_1 ** 2 + y_1 ** 2)
    distance_to_2 = math.sqrt(x_2 ** 2 + y_2 ** 2)
    if distance_to_1 <= distance_to_2:
        return math.floor(x_1), math.floor(y_1)
    else:
        return math.floor(x_2), math.floor(y_2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_to_center(x1, y1, x2, y2))
