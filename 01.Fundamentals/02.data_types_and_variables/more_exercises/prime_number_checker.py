number = int(input())
is_prime = None
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
    is_prime = True
if is_prime:
    print("True")
else:
    print("False")
