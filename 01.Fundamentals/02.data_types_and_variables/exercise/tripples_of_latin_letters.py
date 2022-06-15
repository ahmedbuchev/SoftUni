number = int(input())
end_number = 97 + number
for i in range(97, end_number):
    for j in range(97, end_number):
        for k in range(97, end_number):
            print(chr(i) + chr(j) + chr(k))
