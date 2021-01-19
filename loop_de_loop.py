def grid_print(grid):
    for i in range(len(grid)):
        print(grid[i])


def extract_coor(coor):
    row = coor[0]
    col = int(coor[1]) - 1

    if row == "A":
        row = 0
    elif row == "B":
        row = 1
    elif row == "C":
        row = 2
    elif row == "D":
        row = 3
    elif row == "E":
        row = 4

    return row, col


def launch_bomb(coor):
    try:
        target = grid[coor[0]][coor[1]]
    except (IndexError, TypeError) as e:
        print('Not in range, sir!')
        return 0
    if target == 0:
        grid[coor[0]][coor[1]] = "X"
    else:
        print("You've missed >:P")


grid = [[0 for i in range(5)] for j in range(5)]

while True:
    grid_print(grid)

    coor = str(input("Enter coordinates to bomb (eg. A4): "))
    if coor == 'q':

        break
    new_coor = extract_coor(coor)
    launch_bomb(new_coor)
print('Game over.')
