row, col = [int(x) for x in input().split()]
grid = []
first_row = -1
first_col = col
last_col  = 0
for i in range(row):
    curr = input()
    grid.append(curr)
    if "*" in curr:
        if first_row == -1:first_row = i
        last_row = i
        first_col = min(first_col, curr.index("*"))
        last_col  = max(last_col, curr.rindex("*"))
for i in range(first_row, last_row+1):
    print(grid[i][first_col:last_col+1])

