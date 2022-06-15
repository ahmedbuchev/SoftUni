import sys

nums_list = [int(el) for el in input().split()]
command = input()
min_num = sys.maxsize
max_mun = -sys.maxsize

while not command == "end":
    command_list = command.split()
    if command_list[0] == "exchange":
        index = int(command_list[1])
        if 0 <= index < len(nums_list):
            list_one = nums_list[:index + 1]
            list_two = nums_list[index + 1:]
            nums_list = list_two + list_one
        else:
            print("Invalid index")

    elif command_list[0] == "max":
        if command_list[1] == "even":
            even_list = [el for el in nums_list if el % 2 == 0]
            if even_list:
                print(nums_list.index(max(even_list)))
            else:
                print("No matches")
        elif command_list[1] == "odd":
            odd_list = [el for el in nums_list if el % 2 != 0]
            if odd_list:
                print(nums_list.index(max(odd_list)))
            else:
                print("No matches")

    elif command_list[0] == "min":
        if command_list[1] == "even":
            even_list = [el for el in nums_list if el % 2 == 0]
            if even_list:
                print(nums_list.index(min(even_list)))
            else:
                print("No matches")
        elif command_list[1] == "odd":
            odd_list = [el for el in nums_list if el % 2 != 0]
            if odd_list:
                print(nums_list.index(min(odd_list)))
            else:
                print("No matches")

    elif command_list[0] == "first":
        count = int(command_list[1])
        test_list = []
        if command_list[2] == "even":
            even_list = [el for el in nums_list if el % 2 == 0]

            if len(nums_list) >= count:
                if len(even_list) < count:
                    count = len(even_list)
                for i in range(count):
                    test_list.append(even_list[i])
                print(test_list)
            else:
                print("Invalid count")

        elif command_list[2] == "odd":
            odd_list = [el for el in nums_list if el % 2 != 0]

            if len(nums_list) >= count:
                if len(odd_list) < count:
                    count = len(odd_list)
                for i in range(count):
                    test_list.append(odd_list[i])
                print(test_list)
            else:
                print("Invalid count")

    elif command_list[0] == "last":
        count = int(command_list[1])
        test_list = []
        if command_list[2] == "even":

            even_list = [el for el in nums_list if el % 2 == 0]
            if len(nums_list) >= count:

                if even_list:
                    for i in range(len(even_list) - 1, -1, -1):
                        test_list.append(even_list[i])
                    print(test_list)
                else:
                    print(test_list)
            else:
                print("Invalid count")

        elif command_list[2] == "odd":
            odd_list = [el for el in nums_list if el % 2 != 0]

            if len(nums_list) >= count:
                if odd_list:
                    for i in range(len(odd_list) - 1, -1, -1):
                        test_list.append(odd_list[i])
                    print(test_list)
                else:
                    print(test_list)
            else:
                print("Invalid count")

    command = input()
print(nums_list)
