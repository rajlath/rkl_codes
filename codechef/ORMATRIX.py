for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append([x for x in input()])
    ans = [[0 for x in range(m)] for y in range(n)]
    dirs = [[0,1], [0,-1],[1,0],[-1,0]]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                ans[i][j] = '0'
                continue
            cnt = 0
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if x < 0 or y < 0 or x >=n or y >= m:
                    continue
                cnt += matrix[x][y] == '0'
            if cnt > 0:
                ans[i][j] = str(cnt)
            else:
                ans[i][j] = '1'
            matrix[i][j] = '1'
    print(ans)

