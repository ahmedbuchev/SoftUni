import math


def longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    length_1 = math.sqrt(abs(x_1 - x_2) ** 2 + abs(y_1 - y_2) ** 2)
    length_2 = math.sqrt(abs(x_3 - x_4) ** 2 + abs(y_3 - y_4) ** 2)
    if length_1 >= length_2:
        return math.floor(x_1), math.floor(y_1), math.floor(x_2), math.floor(y_2)
    else:
        return math.floor(x_3), math.floor(y_3), math.floor(x_4), math.floor(y_4)


def closest_to_center(x_1, y_1, x_2, y_2):
    distance_to_1 = math.sqrt(x_1 ** 2 + y_1 ** 2)
    distance_to_2 = math.sqrt(x_2 ** 2 + y_2 ** 2)
    if distance_to_1 <= distance_to_2:
        return math.floor(x_1), math.floor(y_1)
    else:
        return math.floor(x_2), math.floor(y_2)


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input())

x__1, y__1, x__2, y__2 = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)

closest_point_to_center_coordinates = closest_to_center(x__1, y__1, x__2, y__2)
closest_x, closest_y = closest_point_to_center_coordinates
if x__1 == closest_x:
    print(f"({x__1}, {y__1})({x__2}, {y__2})")
else:
    print(f"({x__2}, {y__2})({x__1}, {y__1})")
