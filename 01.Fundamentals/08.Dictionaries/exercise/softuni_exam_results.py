command = input()
results = {}
submissions = {}
while not command == "exam finished":
    if "banned" not in command:
        username, language, points = command.split("-")
        points = int(points)

        if username not in results:
            results[username] = {"language": [language], "points": [points]}
        else:
            if points > results[username]["points"][0]:
                results[username] = {"language": [language], "points": [points]}

        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1

    else:
        username = command.split("-")[0]
        if username in results:
            results.pop(username)
    command = input()

print("Results:")
for key, value in results.items():
    print(f"{key} | {value['points'][0]}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
