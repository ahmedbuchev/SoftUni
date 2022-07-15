n = int(input())
parking = {}
for _ in range(n):
    data = input().split()
    command = data[0]
    if command == "register":
        user, number = data[1], data[2]
        if user not in parking:
            parking[user] = number
            print(f"{user} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

    elif command == "unregister":
        user = data[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            parking.pop(user)
            print(f"{user} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
