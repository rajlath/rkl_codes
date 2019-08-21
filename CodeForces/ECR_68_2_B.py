for _ in range(int(input())):
    row, col = [int(x) for x in input().split()]
    grid = [[x for x in input()] for _ in range(row)]
    rowc, colc = [0] * row, [0] * col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "*":
                rowc[i] += 1
                colc[j] += 1
    ans = int(10e18)
    for i in range(row):
        for j in range(col):
            k = rowc[i] + colc[j] - (grid[i][j] == "*")
            ans = min(row + col - 1 - k, ans)
    print(ans)
