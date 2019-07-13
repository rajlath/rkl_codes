def get_path(grid, row, col):
    rets = []
    k = 0
    l = 0
    while k < row and l < col:
        for i in range(l, col):
            rets.append((k, i))
        k += 1
        for i in range(k, row):
            rets.append((i, col - 1))
        col -= 1
        if k < row:
            for i in range(col - 1, (l - 1), -1):
                rets.append((row - 1,i))
        row -= 1
        if l < col:
            for i in range(row - 1, k - 1, -1):
                rets.append((i, l))
        l += 1
    return rets


rows, cols = [int(x) for x  in input().split()]
grids = [[int(x) for x  in input().split()] for _ in range(rows)]
paths = get_path(grids, rows, cols)
for i in range(len(paths)):
    print(*[x + 1 for x in paths[i]])
