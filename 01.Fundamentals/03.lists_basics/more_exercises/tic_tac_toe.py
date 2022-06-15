first_row = [int(el) for el in input().split()]
second_row = [int(el) for el in input().split()]
third_row = [int(el) for el in input().split()]

first_player_win = False
second_player_win = False

if first_row[0] == 1 and first_row[1] == 1 and first_row[2] == 1:
    first_player_win = True
if second_row[0] == 1 and second_row[1] == 1 and second_row[2] == 1:
    first_player_win = True
if third_row[0] == 1 and third_row[1] == 1 and third_row[2] == 1:
    first_player_win = True
if first_row[0] == 1 and second_row[1] == 1 and third_row[2] == 1:
    first_player_win = True
if first_row[2] == 1 and second_row[1] == 1 and third_row[0] == 1:
    first_player_win = True
if first_row[0] == 1 and second_row[0] == 1 and third_row[0] == 1:
    first_player_win = True
if first_row[1] == 1 and second_row[1] == 1 and third_row[1] == 1:
    first_player_win = True
if first_row[2] == 1 and second_row[2] == 1 and third_row[2] == 1:
    first_player_win = True

if first_row[0] == 2 and first_row[1] == 2 and first_row[2] == 2:
    second_player_win = True
if second_row[0] == 2 and second_row[1] == 2 and second_row[2] == 2:
    second_player_win = True
if third_row[0] == 2 and third_row[1] == 2 and third_row[2] == 2:
    second_player_win = True
if first_row[0] == 2 and second_row[1] == 2 and third_row[2] == 2:
    second_player_win = True
if first_row[2] == 2 and second_row[1] == 2 and third_row[0] == 2:
    second_player_win = True
if first_row[0] == 2 and second_row[0] == 2 and third_row[0] == 2:
    second_player_win = True
if first_row[1] == 2 and second_row[1] == 2 and third_row[1] == 2:
    second_player_win = True
if first_row[2] == 2 and second_row[2] == 2 and third_row[2] == 2:
    second_player_win = True

if first_player_win:
    print("First player won")
elif second_player_win:
    print("Second player won")
else:
    print("Draw!")
