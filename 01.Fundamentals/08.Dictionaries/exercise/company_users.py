data = input()

users = {}

while not data == "End":
    company, user_id = data.split(" -> ")
    if company not in users:
        users[company] = []
    if user_id not in users[company]:
        users[company].append(user_id)
    data = input()

for company, users in users.items():
    print(f"{company}")
    for index in range(len(users)):
        print(f"-- {users[index]}")


