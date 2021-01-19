
def grid_print(grid):
    for i in range(len(grid)):
        print(grid[i])


def extract_coor(coor):
    row = coor[0]
    col = coor[1]

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
    target = grid[coor[0, coor[1]]]
    if target == 0:
        target = "X"
    else:
        print("You've missed")


grid = [[0 for i in range(5)] for j in range(5)]

coor = 1
while coor != "q":
    grid_print(grid)

    coor = str(input("Enter coordinates to bomb (eg. A4): "))

    new_coor = extract_coor(coor)
    launch_bomb(new_coor)

