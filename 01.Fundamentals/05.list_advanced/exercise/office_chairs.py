num = int(input())
chairs_needed = False
free_chairs = 0
for i in range(1, num + 1):
    room = input().split()
    chairs = len(room[0])
    visitors = int(room[1])
    free_chairs += chairs - visitors
    if chairs < visitors:
        chairs_needed = True
        print(f"{visitors - chairs} more chairs needed in room {i}")
if not chairs_needed:
    print(f"Game On, {free_chairs} free chairs left")
