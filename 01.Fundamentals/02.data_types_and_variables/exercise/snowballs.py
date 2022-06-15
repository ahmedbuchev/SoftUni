import sys

number_of_snowballs = int(input())
best_score = - sys.maxsize
best_weight = 0
best_time = 0
best_quality = 0
for ball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    score = int((weight / time) ** quality)
    if score > best_score:
        best_score = score
        best_weight = weight
        best_time = time
        best_quality = quality

print(f"{best_weight} : {best_time} = {best_score} ({best_quality})")
