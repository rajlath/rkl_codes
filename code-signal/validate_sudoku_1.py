def sudoku2(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == ".":continue
            if not isvalid(grid, i, j):
                return False
    return True


def isvalid(grid, i, j)    :
    for x in range(9):
        if x !=j:
            if grid[i][x] == grid[i][j]:
                return False
    for x in range(9):
        if x != i:
            if grid[x][j] == grid[i][j]:
                return False
    for i in range(3):
        for j in range(3):
            x = i//3 * 3 + i
            y = j//3 * 3 + j
            if x != i and y != j:
                if grid[x][y] == grid[i][j]:
                    return False
    return True

grid = [[".",".",".","1","4",".",".","2","."],
 [".",".","6",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".","1",".",".",".",".",".","."],
 [".","6","7",".",".",".",".",".","9"],
 [".",".",".",".",".",".","8","1","."],
 [".","3",".",".",".",".",".",".","6"],
 [".",".",".",".",".","7",".",".","."],
 [".",".",".","5",".",".",".","7","."]]


print(sudoku2(grid))

