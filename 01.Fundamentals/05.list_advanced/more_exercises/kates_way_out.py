def where_is_kate(maze, rows):
    for x in range(maze_rows):
        for y in range(len(maze_list[x])):
            if maze_list[x][y] == 'k':
                return x + 1, y + 1


def is_kate_on_border(maze, rows, cols, x, y):
    if x == 0 or x == rows or y == 0 or y == cols:
        return True
    return False


def kate_is_moving(maze, rows, cols, x, y, cnt):
    if maze[x - 1][y] == ' ':
        maze[x - 1][y] = 'k'
        maze[x][y] = '#'
        x -= 1
        cnt += 1

    if maze[x + 1][y] == ' ':
        maze[x + 1][y] = 'k'
        maze[x][y] = '#'
        x += 1
        cnt += 1

    if maze[x][y - 1] == ' ':
        maze[x][y - 1] = 'k'
        maze[x][y] = '#'
        y -= 1
        cnt += 1

    if maze[x][y + 1] == ' ':
        maze[x][y + 1] = 'k'
        maze[x][y] = '#'
        y += 1
        cnt += 1

        return maze, x, y, cnt
    return False


maze_rows = int(input())
maze_list = []
x = 0
y = 0
moves = 0

for i in range(maze_rows):
    maze_list.append([el for el in input()])

x, y = where_is_kate(maze_list, maze_rows)

maze_cols = len(maze_list[x])

if is_kate_on_border(maze_list, maze_rows, maze_cols, x, y):
    pass
else:
    kate_is_moving(maze_list, maze_rows, maze_cols, x, y)
    if is_kate_on_border(maze_list, maze_rows, maze_cols, x, y):
        pass


