def data_types(string, num_as_str):
    if string == "int":
        num = int(num_as_str)
        print(num * 2)
    elif string == "real":
        num = float(num_as_str)
        print(f"{(num * 1.5):.2f}")
    elif string == "string":
        print(f"${num_as_str}$")


word = input()
number_as_string = input()
data_types(word, number_as_string)
