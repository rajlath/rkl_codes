def findNextCellToFill(grid, i, j):
            for x in range(i,9):
                    for y in range(j,9):
                            if grid[x][y] == 0:
                                    return x,y
            for x in range(0,9):
                    for y in range(0,9):
                            if grid[x][y] == 0:
                                    return x,y
            return -1,-1

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:            
            secTopX, secTopY = 3 *(i/3), 3 *(j/3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
                    return True
    return False

def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            
            grid[i][j] = 0
    return False
    
inputs = []
for i in range(9):
    inputs.append(map(int,raw_input().split())) 
   
       

solveSudoku(inputs)
for i in range(9):
    print(" ".join(map(str, inputs[i])))
    
