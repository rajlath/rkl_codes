def sudoku2(grid):
    for i in range(9):
        if not isValidList([grid[i][j] for j in range(9)] or not isValidList([grid[j][i] for j in range(9)])):
            return False
    for i in range(3):
        for j in range(3):
            if not isValidList([grid[m][n] for n in range(3 * j, 3 * j + 3) for m in range(3 * i, 3 * i + 3)]):
                return False
    return True


def isValidList(xs):
    xs = [x for x in xs if x != "."]
    return len(set(xs)) == len(xs)

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