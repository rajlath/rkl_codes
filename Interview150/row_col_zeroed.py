'''
given a m X n grid,
makes all elements of row zero if row contains any zero
makes all elements of col zero if col contains any zero
'''
def zeroed_matrix(grid):
    rows = [False] * len(grid)
    cols = [False] * len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                rows[i] = True
                cols[i] = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if rows[i] or cols[j]:grid[i][j] = 0
    return grid


grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1]]
print( zeroed_matrix(grid))











