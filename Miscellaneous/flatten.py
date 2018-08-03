grid =  [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]

row = len(grid)
col = len(grid[0])
cnt = 0
i = 0
while i < row - 2:
    j = 0
    while j < col - 2:
        if print([grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]):cnt += 1
        j += 1
    i+=1



