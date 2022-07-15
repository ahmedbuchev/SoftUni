command = input()
results = {}
submissions = {}
while not command == "exam finished":
    if "banned" not in command:
        username, language, points = command.split("-")

        if username not in results:
            results[username] = {language: points}

        else:
            if language not in results[username]:
                results[username][language] = points

            if points > results[username][language]:
                results[username][language] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        username = command.split("-")[0]
        if username in results:
            results.pop(username)
    command = input()

print("Results:")
for key, value in results.items():
    for k, v in value.items():
        print(f"{key} | {value[k]}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
