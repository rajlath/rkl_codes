rows , cols = [int(x) for x in input().split()]
grid = []
for i in range(rows):
    grid.append([int(x) for x in input().split()])
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            for k in range(i, rows):
                grid[k][j] = 0
sums = 0
for i in range(rows):
    sums += sum(grid[i])
print(sums)