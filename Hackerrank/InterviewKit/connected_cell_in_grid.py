

def count_cells(matrix, i, j):
    if i not in range(len(matrix)) or j not in range(len(matrix[0])): return 0

    if matrix[i][j] == 0: return 0

    offset = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 1
    matrix[i][j] = 0
    for x in offset:
        count += count_cells(matrix, i+ x[0], j + x[1])

    return count



def max_region(matrix):
    maxs = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            maxs = max(maxs, count_cells(matrix, i, j))
    return maxs


rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split()])
print(max_region(matrix))
'''
def getBiggestRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion

def countCells(grid, i, j):
    if (not(i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == 0):
        return 0
    count = 1
    grid[i][j] = 0
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    count += countCells(grid, i + 1, j + 1)
    count += countCells(grid, i - 1, j - 1)
    count += countCells(grid, i - 1, j + 1)
    count += countCells(grid, i + 1, j - 1)
    return count

rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split()])
print(getBiggestRegion(matrix))
'''


