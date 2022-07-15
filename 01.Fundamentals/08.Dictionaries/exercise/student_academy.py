n = int(input())
students = {}
filtered_students = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        filtered_students[student] = average_grade

for student, average_grade in filtered_students.items():
    print(f"{student} -> {average_grade:.2f}")
