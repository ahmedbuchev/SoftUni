usernames = input().split(", ")

valid_usernames = []
strip_username = ""
for user in usernames:
    strip_username = user.strip()
    if 3 <= len(user) <= 16 and \
            (user.isalnum() or "-" in user or "_" in user) and \
            len(user) == len(strip_username):
        valid_usernames.append(user)

for name in valid_usernames:
    print(name)

