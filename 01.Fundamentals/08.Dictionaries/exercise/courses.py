data = input()
softuni_courses = {}
while not data == "end":
    course, name = data.split(" : ")
    if course not in softuni_courses:
        softuni_courses[course] = []
    softuni_courses[course].append(name)
    data = input()

for key, value in softuni_courses.items():
    print(f"{key}: {len(softuni_courses[key])}")
    for index in range(len(value)):
        print(f"-- {value[index]}")
